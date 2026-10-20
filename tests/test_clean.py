import argparse
import contextlib
import io
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from renpybuild import __main__ as cli


class CleanTests(unittest.TestCase):
    """Exercise cleanup against isolated build trees, never the real build."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1])
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.tmp = self.root / "tmp"

        environment = patch.dict(os.environ)
        environment.start()
        self.addCleanup(environment.stop)
        os.environ.pop("RENPY_BUILD_TMP", None)

        root = patch.object(cli, "root", self.root, create=True)
        root.start()
        self.addCleanup(root.stop)

    def create_state(self, scope: str, module: str = "python3") -> tuple[Path, Path]:
        directory = self.tmp / "build" / f"{module}.{scope}"
        directory.mkdir(parents=True)
        (directory / "object.o").write_text("build artifact")

        marker = self.tmp / "complete" / f"build-{module}.{scope}"
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text("complete")
        return directory, marker

    def run_clean(self, platforms: str = "", archs: str = "") -> None:
        cli.clean(argparse.Namespace(platforms=platforms, archs=archs))

    def assert_state(self, state: tuple[Path, Path], exists: bool) -> None:
        for path in state:
            with self.subTest(path=path):
                self.assertEqual(path.exists(), exists)

    def test_filters_remove_only_selected_state(self) -> None:
        cases = [
            ("platform", "ios", "", {"ios", "ios-arm64", "ios-sim-arm64", "ios-sim-x86_64"}),
            ("architecture", "", "arm64", {"ios-arm64", "mac-arm64"}),
            ("intersection", "ios", "sim-arm64", {"ios", "ios-sim-arm64"}),
            ("shared_architecture", "", "x86_64", {"linux-x86_64", "windows-x86_64"}),
            ("multiple", "ios, linux", "arm64, x86_64", {"ios", "ios-arm64", "linux", "linux-x86_64"}),
            ("nonexistent_pair", "windows", "arm64", {"windows"}),
        ]
        scopes = [
            "host", "cross-ios-arm64", "cross-ios-sim-arm64", "cross-android-arm64_v8a",
            "ios", "mac", "linux", "windows", "ios-arm64", "ios-sim-arm64",
            "ios-sim-x86_64", "mac-arm64", "linux-x86_64", "windows-x86_64",
            "android-arm64_v8a", "web-wasm", "not-ios-arm64", "ios-arm64-extra",
        ]

        for label, platforms, archs, removed in cases:
            with self.subTest(label=label):
                self.tmp = self.root / label
                os.environ["RENPY_BUILD_TMP"] = label
                states = {scope: self.create_state(scope) for scope in scopes}
                extra_marker = self.tmp / "complete" / "unpack-toolchain.cross-ios-arm64"
                extra_marker.write_text("complete")
                selected_marker = self.tmp / "complete" / "install-python3.ios-arm64"
                selected_marker.write_text("complete")

                self.run_clean(platforms, archs)

                for scope, state in states.items():
                    self.assert_state(state, scope not in removed)
                self.assertTrue(extra_marker.exists())
                self.assertEqual(selected_marker.exists(), "ios-arm64" not in removed)

    def test_filtered_clean_preserves_sources_installs_and_outputs(self) -> None:
        selected = self.create_state("ios-arm64")
        preserved = [
            self.tmp / "source", self.tmp / "host", self.tmp / "cross.ios-arm64",
            self.tmp / "install.ios-arm64", self.tmp / "py",
            self.root / "renpy" / "tmp" / "gen", self.root / "renpy" / "web",
            self.root / "renpy" / "renios", self.root / "renpy" / "rapt",
        ]
        for directory in preserved:
            directory.mkdir(parents=True)
            (directory / "keep").write_text("preserve")

        self.run_clean("ios")

        self.assert_state(selected, False)
        for directory in preserved:
            self.assertEqual((directory / "keep").read_text(), "preserve")

    def test_full_clean_retains_legacy_behavior(self) -> None:
        self.create_state("host")
        self.create_state("cross-ios-arm64")
        removed = [
            self.tmp / "build", self.tmp / "complete", self.tmp / "host",
            self.tmp / "source", self.tmp / "install.ios-arm64",
            self.tmp / "install.linux-x86_64", self.root / "renpy" / "tmp" / "gen",
            self.root / "renpy" / "web", self.root / "renpy" / "renios",
            self.root / "renpy" / "rapt",
        ]
        preserved = [
            self.tmp / "cross.ios-arm64", self.tmp / "tars", self.tmp / "py",
            self.root / "source", self.root / "renpy" / "lib",
        ]
        for directory in removed + preserved:
            directory.mkdir(parents=True, exist_ok=True)
            (directory / "artifact").write_text("artifact")

        self.run_clean()

        for directory in removed:
            self.assertFalse(directory.exists(), str(directory))
        for directory in preserved:
            self.assertTrue((directory / "artifact").exists(), str(directory))

    def test_custom_tmp_does_not_clean_default_tmp(self) -> None:
        default_state = self.create_state("ios-arm64")
        self.tmp = self.root / "custom"
        selected = self.create_state("ios-arm64")
        os.environ["RENPY_BUILD_TMP"] = str(self.tmp)

        self.run_clean("ios")

        self.assert_state(default_state, True)
        self.assert_state(selected, False)

    def test_missing_state_directories_are_not_created(self) -> None:
        for platforms, archs in [("ios", ""), ("", "arm64"), ("", "")]:
            with self.subTest(platforms=platforms, archs=archs):
                self.run_clean(platforms, archs)
                self.assertFalse(self.tmp.exists())

    def test_invalid_filters_fail_before_deleting_anything(self) -> None:
        state = self.create_state("ios-arm64")
        for platforms, archs in [("ios,unknown", ""), ("ios", "unknown")]:
            with self.subTest(platforms=platforms, archs=archs):
                with contextlib.redirect_stderr(io.StringIO()) as errors:
                    with self.assertRaises(SystemExit) as raised:
                        self.run_clean(platforms, archs)

                self.assertEqual(raised.exception.code, 1)
                self.assertIn("is not known", errors.getvalue())
                self.assert_state(state, True)

    def test_deletion_errors_propagate(self) -> None:
        state = self.create_state("ios-arm64")
        with patch.object(cli.shutil, "rmtree", side_effect=PermissionError("denied")):
            with self.assertRaises(PermissionError):
                self.run_clean("ios")

        self.assert_state(state, True)

    def test_cli_filter_placement_and_aliases(self) -> None:
        cases = [
            (["clean", "--platform", "ios", "--arch", "sim-arm64"], "ios", "sim-arm64"),
            (["--platform", "ios", "--arch", "sim-arm64", "clean"], "ios", "sim-arm64"),
            (["clean", "--platforms", "ios,mac", "--archs", "arm64"], "ios,mac", "arm64"),
            (["--platform", "ios", "clean", "--arch", "sim-arm64"], "ios", "sim-arm64"),
            (["--arch", "arm64", "clean", "--platform", "ios"], "ios", "arm64"),
            (["--platform", "mac", "clean", "--platform", "ios"], "ios", ""),
            (["--arch", "arm64", "clean", "--arch", "sim-arm64"], "", "sim-arm64"),
            (["clean"], "", ""),
        ]
        for arguments, platforms, archs in cases:
            with self.subTest(arguments=arguments):
                with patch("sys.argv", ["renpybuild", *arguments]), patch.object(cli, "clean") as clean:
                    cli.main()

                clean.assert_called_once()
                args = clean.call_args.args[0]
                self.assertEqual(args.platforms, platforms)
                self.assertEqual(args.archs, archs)


if __name__ == "__main__":
    unittest.main()
