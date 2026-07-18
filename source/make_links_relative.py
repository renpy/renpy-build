import pathlib
import sys
import os


def main():
    root = pathlib.Path(sys.argv[1]).resolve()

    for i in root.rglob("*"):
        if not i.is_symlink():
            continue

        target = os.readlink(i)

        if not target.startswith("/"):
            continue

        if target.startswith(str(root)):
            continue

        target = str(root) + str(target)

        i.unlink()
        os.symlink(target, i)

        print(i, "->", target)


if __name__ == "__main__":
    main()
