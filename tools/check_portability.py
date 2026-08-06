#!/usr/bin/env python3
"""Fail when tracked project text contains machine-specific absolute paths."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    ".bib", ".cfg", ".csv", ".ipynb", ".json", ".log", ".md", ".py",
    ".rst", ".tex", ".toml", ".tsv", ".txt", ".yaml", ".yml",
}
IGNORED_PARTS = {".git", "__pycache__", ".ipynb_checkpoints", ".venv"}
POSIX_MARKERS = tuple("/" + name + "/" for name in ("Users", "home", "workspace"))
FILE_URI = "file" + "://"
WINDOWS_ABSOLUTE = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]")
HOME_RELATIVE = re.compile(r"(?<![A-Za-z0-9])~[\\/]")


def candidate_files() -> list[Path]:
    """Use the Git index when available; otherwise inspect the portable reference copy."""
    if (ROOT / ".git").exists():
        proc = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z"],
            check=True,
            capture_output=True,
        )
        return [ROOT / item.decode() for item in proc.stdout.split(b"\0") if item]
    return [
        path for path in ROOT.rglob("*")
        if path.is_file() and not any(part in IGNORED_PARTS for part in path.parts)
    ]


def findings() -> list[str]:
    hits: list[str] = []
    for path in candidate_files():
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if path.suffix.lower() == ".txt" and rel.parts[:1] == ("research",):
            # Historical transcriptions and OCR are source data, not operational references;
            # broken layout frequently resembles drive or home-path syntax.
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            labels = [marker for marker in POSIX_MARKERS if marker in line]
            if FILE_URI in line:
                labels.append(FILE_URI)
            if WINDOWS_ABSOLUTE.search(line):
                labels.append("Windows absolute path")
            if HOME_RELATIVE.search(line):
                labels.append("home-relative path")
            if labels:
                hits.append(f"{rel}:{line_number}: {', '.join(labels)}")
    return hits


def main() -> int:
    hits = findings()
    if hits:
        print("Machine-specific paths found:")
        for hit in hits:
            print(f"  {hit}")
        return 1
    print("PORTABLE: no tracked machine-specific absolute paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
