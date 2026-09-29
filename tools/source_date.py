#!/usr/bin/env python3
"""The build timestamp for each rendered document, taken from the date it declares.

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
  paper    the month in the paper's `\\date{...}`, on its first day at midnight UTC

`tools/check_docs.py` already holds each of those dates to the sources it describes.

Run from anywhere:  python3 tools/source_date.py book|primer|paper
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DECLARED = {
    "book": (ROOT / "tools" / "build_book.py", r"^DRAFT_DATE = '([^']+)'", "%d %B %Y"),
    "primer": (ROOT / "tools" / "build_primer.py", r"^REVISED_DATE = '([^']+)'", "%d %B %Y"),
    "paper": (ROOT / "paper" / "anonymity-as-an-aggregation-condition.tex",
              r"\\date\{\\normalsize ([A-Z][a-z]+ \d{4})", "%B %Y"),
}


def declared_date(document: str) -> datetime:
    path, pattern, fmt = DECLARED[document]
    found = re.search(pattern, path.read_text(encoding="utf-8"), re.MULTILINE)
    if not found:
        raise SystemExit(f"{path.relative_to(ROOT)} declares no date for the {document}")
    return datetime.strptime(found.group(1), fmt).replace(tzinfo=timezone.utc)


def epoch(document: str) -> int:
    """Seconds since 1970 for the document's declared date, as SOURCE_DATE_EPOCH expects."""
    return int(declared_date(document).timestamp())


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in DECLARED:
        print("usage: python3 tools/source_date.py book|primer|paper", file=sys.stderr)
        return 2
    print(epoch(sys.argv[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
