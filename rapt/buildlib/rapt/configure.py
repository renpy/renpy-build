import json
import os
import re
from . import plat

__ = plat.__

# Taken from https://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html
JAVA_KEYWORDS = """
abstract    continue    for    new    switch
assert***    default    goto*    package    synchronized
boolean    do    if    private    this
break    double    implements    protected    throw
byte    else    import    public    throws
case    enum****    instanceof    return    transient
catch    extends    int    short    try
char    final    interface    static    void
class    finally    long    strictfp**    volatile
const*    float    native    super    while
true false null
""".replace("*", "").split()


class Configuration(object):

    def __init__(self, directory):

        self.package = None
        self.name = None
        self.icon_name = None
        self.version = None
        self.numeric_version = None
        self.orientation = "sensorLandscape"
        self.permissions = [ "VIBRATE" ]
        self.include_pil = False
        self.include_sqlite = False
        self.layout = None
        self.source = False
        self.expansion = False
        self.google_play_key = None
        self.google_play_salt = None
        self.store = "none"
        self.update_icons = True
        self.update_always = True

        try:
            with file(os.path.join(directory, ".android.json"), "r") as f:
                d = json.load(f)

            self.__dict__.update(d)
        except:
            pass

        if self.orientation == "landscape":
            self.orientation = "sensorLandscape"

    def save(self, directory):

        with file(os.path.join(directory, ".android.json"), "w") as f:
            json.dump(self.__dict__, f)


def set_version(config, value):
    """
    Sets the version, and tries to set the numeric versions based on the
    version number.
    """

    config.version = value

    try:
        v = 0

        for i in config.version.split('.'):
            v *= 100
            v += int(i)

        config.numeric_version = str(v)
    except:
        pass


def configure(interface, directory, default_name=None, default_version=None):

    config = Configuration(directory)

    if config.name is None:
        config.name = default_name

    config.name = interface.input(__("What is the full name of your application? This name will appear in the list of installed applications."), config.name)

    if config.icon_name is None:
        config.icon_name = config.name

    config.icon_name = interface.input(__("What is the short name of your application? This name will be used in the launcher, and for application shortcuts."), config.icon_name)

    config.package = interface.input(__("What is the name of the package?\n\nThis is usually of the form com.domain.program or com.domain.email.program. It may only contain ASCII letters and dots. It must contain at least one dot."), config.package)

    config.package = config.package.strip().lower()

    if not config.package:
        interface.fail(__("The package name may not be empty."))

    if " " in config.package:
        interface.fail(__("The package name may not contain spaces."))

    if "." not in config.package:
        interface.fail(__("The package name must contain at least one dot."))

    for part in config.package.split('.'):
        if not part:
            interface.fail(__("The package name may not contain two dots in a row, or begin or end with a dot."))

        if not re.match(r"[a-zA-Z_]\w*$", part):
            interface.fail(__("Each part of the package name must start with a letter, and contain only letters, numbers, and underscores."))

        if part in JAVA_KEYWORDS:
            interface.fail(__("{} is a Java keyword, and can't be used as part of a package name.").format(part))

    if config.version is None:
        config.version = default_version

    version = interface.input(__("What is the application's version?\n\nThis should be the human-readable version that you would present to a person. It must contain only numbers and dots."), config.version)

    if not re.match(r'^[\d\.]+$', version):
        interface.fail(__("The version number must contain only numbers and dots."))

    set_version(config, version)

    config.numeric_version = interface.input(__("What is the version code?\n\nThis must be a positive integer number, and the value should increase between versions."), config.numeric_version)

    if not re.match(r'^[\d]+$', config.numeric_version):
        interface.fail(__("The numeric version must contain only numbers."))

    config.orientation = interface.choice(__("How would you like your application to be displayed?"), [
        ("sensorLandscape", __("In landscape orientation.")),
        ("portrait", __("In portrait orientation.")),
        ("sensor", __("In the user's preferred orientation.")),
        ], config.orientation)

    if plat.renpy:
        config.store = interface.choice(__("Which app store would you like to support in-app purchasing through?"), [
            ("play", __("Google Play.")),
            ("amazon", __("Amazon App Store.")),
            ("all", __("Both, in one app.")),
            ("none", __("Neither.")),
            ], config.store)

    if config.store in [ "play", "none" ]:
        config.expansion = interface.choice(__("Would you like to create an expansion APK?") + "\n\n" + __("Automatically installing expansion APKs {a=https://issuetracker.google.com/issues/160942333}may not work on Android 11{/a}."), [
            (False, __("No. Size limit of 100 MB on Google Play, but can be distributed through other stores and sideloaded.")),
            (True, __("Yes. 2 GB size limit, but won't work outside of Google Play. (Read the documentation to get this to work.)"))
            ], config.expansion)

    if not plat.renpy:

        config.layout = interface.choice("How is your application laid out?", [
            ("internal", "A single directory, that will be placed on device internal storage."),
            ("split", "Multiple directories that correspond to internal and asset storage."),
            ], config.layout)

        config.source = interface.yesno_choice("Do you want to include the Python source code of your application in the archive? If you include it once, you'll need to include it always.", config.source)

        permissions = " ".join(config.permissions)
        permissions = interface.input("""\
What permissions should your application have? Possible permissions include:

INTERNET (network access), VIBRATE (vibration control).

Please enter a space-separated list of permissions.""", permissions)
        config.permissions = permissions.split()

    if plat.renpy:

        if not config.expansion:
            internet = "INTERNET" in config.permissions
            internet = interface.yesno_choice(__("Do you want to allow the app to access the Internet?"), internet)
        else:
            internet = False # included in template.

        permissions = [ i for i in config.permissions if i not in [ "INTERNET" ] ]

        if internet:
            permissions.append("INTERNET")

        config.permissions = permissions

    config.update_always = interface.choice(
        __("Do you want to automatically update the Java source code?"), [
            (True, __("Yes. This is the best choice for most projects.")),
            (False, __("No. This may require manual updates when Ren'Py or the project configuration changes."))
            ], config.update_always)

    config.save(directory)


def set_config(iface, directory, var, value):

    config = Configuration(directory)

    if var == "version":
        set_version(config, value)
    elif var == "permissions":
        config.permissions = value.split()
    elif hasattr(config, var):
        setattr(config, var, value)
    else:
        iface.fail(__("Unknown configuration variable: {}").format(var))

    config.save(directory)
