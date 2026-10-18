#!/usr/bin/env python3
"""Fail when tracked project text contains machine-specific absolute paths.

Every tracked path must be repository-relative or derived at runtime, because the repository
is public and a home directory or workspace root in it would publish the author's machine.

Run from anywhere:  python3 tools/check_portability.py

Reads: every text file the Git index lists (see `TEXT_SUFFIXES`), or, in a copy that has no
`.git`, every text file under the repository root except caches and virtual environments.
Writes: nothing but its report on standard output.
What counts as a finding: a POSIX user-home or workspace directory prefix, a file URI, a
Windows drive-letter path, or a home-relative tilde path. The literal forms are not spelled
out here because this file is itself scanned.
Exit codes: 0 when there is no finding and 1 when at least one file and line is listed. If
`git ls-files` fails in a checkout, the resulting exception is not caught, so Python exits 1
with a traceback.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    ".bib", ".cfg", ".csv", ".ipynb", ".json", ".log", ".md", ".py",
    ".rst", ".tex", ".toml", ".tsv", ".txt", ".yaml", ".yml",
}
# Only consulted in a copy with no Git index: in a checkout, `git ls-files` already leaves
# these out.
IGNORED_PARTS = {".git", "__pycache__", ".ipynb_checkpoints", ".venv"}
# The markers are assembled from pieces so that this file does not itself contain the
# strings it forbids and flag itself.
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
    """Return one `path:line: label, label` string for every offending line.

    Only files whose suffix is in `TEXT_SUFFIXES` are read. A file that is not valid UTF-8
    or cannot be opened is skipped rather than reported, since it cannot be text.
    """
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
    """Print the report and return the process exit code (0 clean, 1 findings)."""
    hits = findings()
    if hits:
        print("Machine-specific paths found:")
        for hit in hits:
            print(f"  {hit}")
        return 1
    print("PORTABLE: no tracked machine-specific absolute paths")
    return 0


if __name__ == "__main__":
    from tool_help import help_requested
    help_requested(__doc__)
    raise SystemExit(main())
