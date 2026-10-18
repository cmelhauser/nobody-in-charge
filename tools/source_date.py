#!/usr/bin/env python3
r"""Print the build timestamp for a rendered document, taken from the date it declares.

TeX stamps a creation date and a document ID into every PDF it writes, so the book, the paper
and the primer came out byte-different on every rebuild even when nothing in them had changed.
A local CI run therefore left all three committed PDFs modified, and the progress log has
recorded that churn, and its manual revert, since 17 August 2026.

Every TeX engine this project uses honours `SOURCE_DATE_EPOCH`, the reproducible-builds
convention: with it set, the PDF carries that time instead of the clock's and two builds of the
same source are identical. The time is taken from the date each document already declares, so
it moves only when the document's own date does:

  book     `DRAFT_DATE` in tools/build_book.py, at midnight UTC
  primer   `REVISED_DATE` in tools/build_primer.py, at midnight UTC
  paper    the month in the paper's `\date{...}`, on its first day at midnight UTC

`tools/check_docs.py` already holds each of those dates to the sources it describes.

Run from anywhere:  python3 tools/source_date.py book|primer|paper

Other tools import `epoch()` rather than running this one: `build_book.py` and `build_primer.py`
set `SOURCE_DATE_EPOCH` from it themselves, and the paper's build (a plain `tectonic` call
in CI and `tools/run_ci_locally.sh`) takes it from this command's output.

Reads:      the one source file that declares the date (listed above), never writing to it.
Writes:     the epoch, as a bare integer, to standard output.
Exit codes: 0 on success; 2 for a missing or unknown document name (usage goes to standard
            error); a `SystemExit` with a message when the source declares no date.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# document -> (file that declares its date, regex whose group 1 is the date text, strptime
# format). The book and primer declare a day; the paper declares only a month, so its epoch
# is the first of that month. Patterns are anchored on the declaration itself, not on prose
# that merely mentions it, and the book/primer ones rely on the single-quoted constants in
# the build scripts being left in that exact form.
DECLARED = {
    "book": (ROOT / "tools" / "build_book.py", r"^DRAFT_DATE = '([^']+)'", "%d %B %Y"),
    "primer": (ROOT / "tools" / "build_primer.py", r"^REVISED_DATE = '([^']+)'", "%d %B %Y"),
    "paper": (ROOT / "paper" / "anonymity-as-an-aggregation-condition.tex",
              r"\\date\{\\normalsize ([A-Z][a-z]+ \d{4})", "%B %Y"),
}


def declared_date(document: str) -> datetime:
    """Return the date `document` declares, as midnight UTC.

    `document` must be a key of `DECLARED`. Exits with a message naming the file if the
    declaration cannot be found, because a silent fallback would stamp the clock's time into
    the PDF, which is the defect this module exists to prevent. Midnight UTC keeps the
    result independent of the machine's time zone.
    """
    path, pattern, fmt = DECLARED[document]
    found = re.search(pattern, path.read_text(encoding="utf-8"), re.MULTILINE)
    if not found:
        raise SystemExit(f"{path.relative_to(ROOT)} declares no date for the {document}")
    return datetime.strptime(found.group(1), fmt).replace(tzinfo=timezone.utc)


def epoch(document: str) -> int:
    """Seconds since 1970 for the document's declared date, as SOURCE_DATE_EPOCH expects."""
    return int(declared_date(document).timestamp())


def main() -> int:
    """Print the epoch for the document named on the command line; return the exit status.

    Returns 2, with usage on standard error, unless there is exactly one argument and it
    names a known document; returns 0 after printing the epoch.
    """
    if len(sys.argv) != 2 or sys.argv[1] not in DECLARED:
        print("usage: python3 tools/source_date.py book|primer|paper", file=sys.stderr)
        return 2
    print(epoch(sys.argv[1]))
    return 0


if __name__ == "__main__":
    from tool_help import help_requested
    help_requested(__doc__)
    sys.exit(main())
