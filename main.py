#!/usr/bin/env python3
"""news-image-20261117 entry program (V3).

Copies the bundled front-page image (entry.png, next to this file) to
$MAKEFUN_OUTPUT_DIR/entry.png, defaulting to /output/entry.png.
Offline, standard library only, deterministic: the output bytes are
exactly the stored image bytes on every run.
"""
import os
import shutil
import sys
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def check_source(source: Path) -> None:
    """Fail early with a clear message if the bundled page is unusable."""
    if not source.is_file():
        print(f"error: entry image not found: {source}", file=sys.stderr)
        raise SystemExit(1)
    with source.open("rb") as handle:
        signature = handle.read(len(PNG_SIGNATURE))
    if signature != PNG_SIGNATURE:
        print(f"error: bundled image is not a PNG file: {source}", file=sys.stderr)
        raise SystemExit(1)


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    check_source(source)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / "entry.png"
    shutil.copyfile(source, destination)
    print(f"Published {source.name} -> {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
