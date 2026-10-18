#!/usr/bin/env python3
"""Check that the TeX Gyre Pagella files installed here are the ones CI builds with.

Both the book and the primer ask for TeX Gyre Pagella by name, and the glyph outlines and
metrics inside the font files change the layout. On 14 October 2026 the book and primer rebuilt
on the CI runner differed from the PDFs committed from the author's machine, with the same
tectonic (0.17.0) and the same pandoc (3.10.2). The four font files were the only difference:
every one had a different SHA-256 from the copy CI downloads from CTAN. The paper does not use
the font and was byte-identical.

So the four hashes CI downloads are pinned here, and the `documents` job runs this with
`--strict` after fetching them: a change at the CTAN mirror then fails the job with a sentence,
and the pins are updated deliberately, with the PDFs rebuilt and re-read, as the pandoc pin is.

Run without `--strict` on a developer machine and it only reports, because installing different
fonts is the developer's decision and a mismatch does not make a build wrong, only unable to
match CI's byte for byte.

  python3 tools/check_fonts.py                 look for the installed files and report
  python3 tools/check_fonts.py --dir DIR       check the four files in DIR
  python3 tools/check_fonts.py --strict ...    exit 1 on a mismatch or a missing file

Run from anywhere.
"""
from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

# SHA-256 of the files the CI runner downloaded from the CTAN mirrors on 14 October 2026.
PINS = {
    "texgyrepagella-regular.otf": "44e64260716d8f2bbe412baa1ee99b7c995190ac4573177c24def0b9200438c7",
    "texgyrepagella-bold.otf": "dd4f9b69f0b24f1fb9be8634abf1fce2009e5c68a30842a3e9f5d6e535900abd",
    "texgyrepagella-italic.otf": "069bb27f48eb98a741715227fc6e4b7baf3639c29fc13925f70d1ed8884ac29a",
    "texgyrepagella-bolditalic.otf": "556fd64655a92bd9f5485ae2c03f7b9cdaf745a27a91d7edb3c3abde997206d2",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def candidate_dirs() -> list[Path]:
    """Directories that may hold the installed files: fontconfig's answer, then the usual places."""
    found: list[Path] = []
    if shutil.which("fc-list"):
        out = subprocess.run(["fc-list", ":family=TeX Gyre Pagella", "file"],
                             capture_output=True, text=True, check=False).stdout
        for line in out.splitlines():
            path = Path(line.strip().removesuffix(":").strip())      # a path may itself hold colons
            if path.name.lower() in PINS and path.parent not in found:
                found.append(path.parent)
    home = Path.home()
    if os.environ.get("XDG_DATA_HOME"):
        found.append(Path(os.environ["XDG_DATA_HOME"]) / "fonts")
    found += [home / ".local" / "share" / "fonts", home / "Library" / "Fonts",
              Path("/Library/Fonts"), Path("/usr/share/fonts")]
    return [d for d in dict.fromkeys(found) if d.is_dir()]


def locate(name: str, directories: list[Path]) -> Path | None:
    """The file called `name` (a pin, lower case) in or under any directory, whatever its case:
    fontconfig lists the same file as TeXGyrePagella-Regular.otf on some systems.
    """
    for directory in directories:
        if (directory / name).is_file():
            return directory / name
        for path in directory.rglob("*"):
            if path.name.lower() == name and path.is_file():
                return path
    return None


def compare(directories: list[Path]) -> tuple[list[str], list[str]]:
    """(matching files, problems), each a printable line."""
    good, bad = [], []
    for name, pinned in PINS.items():
        path = locate(name, directories)
        if path is None:
            bad.append(f"MISSING {name}: not found in {', '.join(map(str, directories)) or 'any known directory'}")
        elif digest(path) == pinned:
            good.append(f"OK {name}: matches the CI font")
        else:
            bad.append(f"MISMATCH {name}: {path} is not the file CI builds with "
                       f"(sha256 {digest(path)[:16]}..., pinned {pinned[:16]}...)")
    return good, bad


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    directories = candidate_dirs()
    if "--dir" in argv:
        position = argv.index("--dir")
        if position + 1 >= len(argv) or argv[position + 1].startswith("--"):
            raise SystemExit("--dir needs a directory")
        directories = [Path(argv[position + 1])]
    good, bad = compare(directories)
    for line in good + bad:
        print(line)
    if bad:
        print(f"\n{len(bad)} of {len(PINS)} font files differ from CI's. PDFs built here that use "
              "TeX Gyre Pagella (the book and the primer) will not match CI's byte for byte.")
        if strict and any(line.startswith("MISMATCH") for line in bad):
            print("On the runner a mismatch means the CTAN mirror now serves a different file (a stale "
                  "cached copy is discarded before this check): update PINS deliberately, then rebuild "
                  "and re-read the PDFs.")
        elif strict:
            print("On the runner a missing file means the font download or install step failed.")
        return 1 if strict else 0
    print(f"\nall {len(PINS)} font files match CI's")
    return 0


if __name__ == "__main__":
    from tool_help import help_requested
    help_requested(__doc__)
    sys.exit(main(sys.argv[1:]))
