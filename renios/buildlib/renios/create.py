import xcodeprojer
import shutil
import os
import plistlib
import re
import sys

RENIOS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def replace_name(o, template, replacement, path=()):
    if isinstance(o, dict):
        for k in list(o.keys()):
            o[k] = replace_name(o[k], template, replacement, path + (k,))

        return o

    elif isinstance(o, list):
        new_o = []

        for i, v in enumerate(o):
            new_o.append(replace_name(v, template, replacement, path + (i,)))

        o[:] = new_o

        return o

    elif isinstance(o, str):
        return o.replace(template, replacement)

    else:
        raise Exception(f"Unknown Xcode entry {o!r} at {path!r}.")


# Copytree - taken from shuiti
def copytree(src, dst, symlinks=False, ignore=None):
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    os.makedirs(dst)
    for name in names:
        if name in ignored_names:
            continue

        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        if symlinks and os.path.islink(srcname):
            linkto = os.readlink(srcname)
            os.symlink(linkto, dstname)
        elif os.path.isdir(srcname):
            copytree(srcname, dstname, symlinks, ignore)
        else:
            shutil.copy(srcname, dstname)


def create_project(interface, dest, name=None, version="1.0"):
    """
    Copies the prototype project to `dest`, which must not already exists. Renames the
    Xcode project to `name`.xcodeproj.
    """

    if name is None:
        name = os.path.basename(dest)

    if version is None:
        return

    shortname = re.sub(r"[^-_A-Za-z0-9]", "", name) or "project"

    if os.path.exists(dest):
        interface.fail(
            f"{dest} already exists. If you would like to create an new project, please move the existing project out of the way."
        )

    prototype = os.path.join(RENIOS, "prototype")

    interface.info("Copying prototype project...")

    copytree(prototype, dest)

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

    os.rename(os.path.join(dest, "prototype.xcodeproj"), os.path.join(dest, shortname + ".xcodeproj"))

    pbxproj = os.path.join(dest, shortname + ".xcodeproj", "project.pbxproj")

    with open(pbxproj) as f:
        root, _parseinfo = xcodeprojer.parse(f.read())

    if not "RENPY_TEST_IOS" in os.environ:
        root = replace_name(root, "XHTE5H7Z79", "TEAMID")
        root = replace_name(root, "org.renpy.prototype", "com.domain." + shortname)
        root = replace_name(root, "prototype", name)
    else:
        root = replace_name(root, "XHTE5H7Z79", "XHTE5H7Z79")
        root = replace_name(root, "org.renpy.prototype", "org.renpy.prototype")
        root = replace_name(root, "prototype", "prototype")

    root = replace_name(root, "-lpython2.7", f"-lpython{sys.version_info.major}.{sys.version_info.minor}")

    output = xcodeprojer.unparse(root, format="xcode", projectname=name)

    with open(pbxproj + ".new", "wb") as f:
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
        CFBundleVersion="1",
        UILaunchStoryboardName="Launch Screen",
        LSRequiresIPhoneOS=True,
        UIRequiresFullScreen=True,
        UIStatusBarHidden=True,
        UISupportedInterfaceOrientations=[
            "UIInterfaceOrientationLandscapeRight",
            "UIInterfaceOrientationLandscapeLeft",
        ],
    )

    plist_fn = os.path.join(dest, "Info.plist")

    with open(plist_fn, "wb") as f:
        plistlib.dump(plist, f)

    interface.success("Created the Xcode project.")
