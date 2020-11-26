import xcodeprojer
import shutil
import os
import plistlib
import re
import sys

RENIOS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__.decode(sys.getfilesystemencoding())))))


def replace_name(o, template, replacement, path=()):
    if isinstance(o, dict):
        for k in list(o.keys()):
            o[k] = replace_name(o[k], template, replacement, path + (k,))

        return o

    elif isinstance(o, list):

        new_o = [ ]

        for i, v in enumerate(o):
            new_o.append(replace_name(v, template, replacement, path + (i,)))

        o[:] = new_o

        return o

    elif isinstance(o, basestring):
        return o.replace(template, replacement)

    else:
        raise Exception("Unknown Xcode entry %r at %r." % (o, path))


def create_project(interface, dest, name=None, version="1.0"):
    """
    Copies the prototype project to `dest`, which must not already exists. Renames the
    Xcode project to `name`.xcodeproj.
    """

    if name is None:
        name = os.path.basename(dest)

    if version is None:
        return

    shortname = re.sub(r'[^-_A-Za-z0-9]', '', name)

    if os.path.exists(dest):
        interface.fail("{} already exists. If you would like to create an new project, please move the existing project out of the way.".format(dest))

    prototype = os.path.join(RENIOS, "prototype")

    interface.info("Copying prototype project...")

    shutil.copytree(prototype, dest)

    interface.info("Updating project with new name...")

    # Update the Xcode project.

    def rm(name):
        path = os.path.join(dest, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.exists(path):
            os.unlink(path)

    rm("base")
    rm("prototype.xcodeproj/project.xcworkspace")
    rm("prototype.xcodeproj/xcuserdata")

    os.rename(os.path.join(dest, "prototype.xcodeproj"), os.path.join(dest, name + ".xcodeproj"))

    pbxproj = os.path.join(dest, name + ".xcodeproj", "project.pbxproj")

    with open(pbxproj, "r") as f:
        root, _parseinfo = xcodeprojer.parse(f.read())

    root = replace_name(root, "XHTE5H7Z79", "TEAMID")
    root = replace_name(root, "org.renpy.prototype", "com.domain." + shortname)
    root = replace_name(root, "prototype", name)

    output = xcodeprojer.unparse(root, format="xcode", projectname=name)

    with open(pbxproj + ".new", "w") as f:
        f.write(output)

    try:
        os.unlink(pbxproj)
    except:
        pass

    os.rename(pbxproj + ".new", pbxproj)

    plist = dict(
        CFBundleDevelopmentRegion="en",
        CFBundleDisplayName="$(PRODUCT_NAME)",
        CFBundleExecutable="$(EXECUTABLE_NAME)",
        CFBundleIdentifier="$(PRODUCT_BUNDLE_IDENTIFIER)",
        CFBundleInfoDictionaryVersion="6.0",
        CFBundleName="$(PRODUCT_NAME)",
        CFBundlePackageType="APPL",
        CFBundleShortVersionString=version,
        CFBundleSignature="????",
        CFBundleVersion=1,
        LSRequiresIPhoneOS=True,
        UIRequiresFullScreen=True,
        UIStatusBarHidden=True,
        UISupportedInterfaceOrientations=[
            "UIInterfaceOrientationLandscapeRight",
            "UIInterfaceOrientationLandscapeLeft",
            ]
        )

    plistlib.writePlist(plist, os.path.join(dest, "Info.plist"))

    interface.success("Created the Xcode project.")
