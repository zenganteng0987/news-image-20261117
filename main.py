#!/usr/bin/env python3
"""news-image-20261117 entry program.

Copies the bundled front-page image (entry.png, next to this file) to
$MAKEFUN_OUTPUT_DIR/entry.png, defaulting to /output/entry.png.
Offline, standard library only, deterministic: the output bytes are
exactly the stored image bytes on every run.
"""
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        print(f"error: entry image not found: {source}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
