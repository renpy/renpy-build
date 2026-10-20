import importlib.util
import os
from pathlib import Path
import plistlib
import shutil
import sys
import tempfile
from types import ModuleType
import unittest
from unittest.mock import patch


ROOT: Path = Path(__file__).resolve().parents[1]


class ProjectInterface:

    def info(self, message: str) -> None:
        pass

    def success(self, message: str) -> None:
        pass

    def fail(self, message: str) -> None:
        raise AssertionError(message)


class IOSProjectTests(unittest.TestCase):
    """Check both plist producers through the project creation interface."""

    create: ModuleType

    @classmethod
    def setUpClass(cls) -> None:
        dependency = ROOT / os.environ.get("RENPY_BUILD_TMP", "tmp") / "source" / "xcodeprojer-master"
        spec = importlib.util.spec_from_file_location("renios_create", ROOT / "renios/buildlib/renios/create.py")
        assert spec is not None and spec.loader is not None
        cls.create = importlib.util.module_from_spec(spec)

        with patch.object(sys, "path", [str(dependency), *sys.path]):
            spec.loader.exec_module(cls.create)

    def assert_scene_configuration(self, plist: dict) -> None:
        manifest = plist["UIApplicationSceneManifest"]
        self.assertIs(manifest["UIApplicationSupportsMultipleScenes"], False)
        configurations = manifest["UISceneConfigurations"]["UIWindowSceneSessionRoleApplication"]
        self.assertEqual(len(configurations), 1)
        self.assertEqual(configurations[0]["UISceneConfigurationName"], "SDLSceneConfiguration")
        self.assertEqual(configurations[0]["UISceneDelegateClassName"], "SDLUIKitSceneDelegate")
        self.assertNotIn("UISceneStoryboardFile", configurations[0])
        self.assertEqual(plist["UILaunchStoryboardName"], "Launch Screen")
        self.assertIs(plist["UIRequiresFullScreen"], True)
        self.assertEqual(
            set(plist["UISupportedInterfaceOrientations"]),
            {"UIInterfaceOrientationLandscapeRight", "UIInterfaceOrientationLandscapeLeft"},
        )

    def test_prototype_adopts_single_scene_lifecycle(self) -> None:
        with (ROOT / "renios/prototype/Info.plist").open("rb") as source:
            self.assert_scene_configuration(plistlib.load(source))

    def test_generated_project_adopts_scenes_and_preserves_customization(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            staging = Path(directory)
            prototype = staging / "prototype"
            project = prototype / "prototype.xcodeproj"
            project.mkdir(parents=True)
            shutil.copyfile(
                ROOT / "renios/prototype/prototype.xcodeproj/project.pbxproj", project / "project.pbxproj"
            )
            shutil.copyfile(ROOT / "renios/prototype/Info.plist", prototype / "Info.plist")
            environment = os.environ.copy()
            environment.pop("RENPY_TEST_IOS", None)

            with patch.object(self.create, "RENIOS", str(staging)), patch.dict(os.environ, environment, clear=True):
                destination = staging / "generated"
                self.create.create_project(ProjectInterface(), str(destination), name="Scene Game", version="2.3")

            with (destination / "Info.plist").open("rb") as source:
                plist = plistlib.load(source)

            self.assert_scene_configuration(plist)
            self.assertEqual(plist["CFBundleShortVersionString"], "2.3")
            self.assertEqual(plist["CFBundleIdentifier"], "$(PRODUCT_BUNDLE_IDENTIFIER)")
            with (destination / "SceneGame.xcodeproj/project.pbxproj").open() as source:
                root, _ = self.create.xcodeprojer.parse(source.read())

            settings = [
                item["buildSettings"] for item in root["objects"].values()
                if item.get("isa") == "XCBuildConfiguration"
            ]
            self.assertTrue(any(item.get("PRODUCT_BUNDLE_IDENTIFIER") == "com.domain.SceneGame" for item in settings))
            self.assertTrue(any(item.get("PRODUCT_NAME") == "Scene Game" for item in settings))


if __name__ == "__main__":
    unittest.main()
