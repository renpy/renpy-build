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
        self.numeric_version = 1
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
        self.heap_size = None

        try:
            with open(os.path.join(directory, ".android.json"), "r") as f:
                d = json.load(f)

            self.__dict__.update(d)
        except:
            pass

        if self.orientation == "landscape":
            self.orientation = "sensorLandscape"

    def save(self, directory):

        with open(os.path.join(directory, ".android.json"), "w") as f:
            json.dump(self.__dict__, f)


    def set_heap_size(self, newSize, gradle_dir):
        """
        Sets the Java Heap Size for Gradle in gradle.properties.
        """

        with open(gradle_dir, "r+") as g:
            contents = g.read()
            contents = contents.replace("org.gradle.jvmargs=-Xmx" + str(self.heap_size) + "g\n", 
                "org.gradle.jvmargs=-Xmx" + str(newSize) + "g\n")
            g.seek(0)
            g.write(contents)

    def get_heap_size(self):
        """
        Gets the Java Heap Size from gradle.properties
        """

        with open(plat.path("project/gradle.properties"), "r") as heap:
            for line in heap.readlines():
                if "org.gradle.jvmargs" in line:
                    heapValue = line

        heapValue = heapValue.replace('org.gradle.jvmargs=-Xmx', "").replace('g\n', "")
        self.heap_size = heapValue

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

    config.version = version

    config.get_heap_size()

    heap_size = interface.input(__("How much RAM (in GB) do you want to allocate to Gradle?\nThis must be a positive integer number."), config.heap_size)

    if not re.match(r'^[\d]+$', heap_size):
        interface.fail(__("The RAM size must contain only numbers and be positive."))
    
    config.set_heap_size(heap_size, plat.path("project/gradle.properties"))

    config.orientation = interface.choice(__("How would you like your application to be displayed?"), [
        ("sensorLandscape", __("In landscape orientation.")),
        ("portrait", __("In portrait orientation.")),
        ("sensor", __("In the user's preferred orientation.")),
        ], config.orientation)

    config.store = "all"

    permissions = [ i for i in config.permissions if i not in [ "INTERNET" ] ]
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
