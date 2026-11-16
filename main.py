#!/usr/bin/env python3
"""Make the AI judge excited (ai-excited-01) — entry program.

Writes one image to /output/entry.png by copying the image bundled
in this repository. No network, fully deterministic: every run writes
the same bytes.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.jpg"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
