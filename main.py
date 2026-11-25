#!/usr/bin/env python3
"""Write one childhood memory, a single sentence, to /output/entry.txt.

The memory is fixed text: the same bytes on every run, with no input,
no network access and no third-party packages.
"""
import os

ENTRY = (
    "My kite is still in the oak behind the school, I think, because I "
    "watched it snag there in June and never once went back to look, and "
    "as long as I don't check, it's still flying."
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Also leave a copy beside this script for a local run.
    try:
        local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(local, "w", encoding="utf-8", newline="\n") as f:
            f.write(ENTRY)
        os.chmod(local, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
