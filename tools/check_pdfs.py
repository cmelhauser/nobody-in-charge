#!/usr/bin/env python3
"""Verify the three rendered PDFs are sound documents, not merely present.

`tools/check_release.py` asks whether each artifact exists, is nontrivial, and is newer
than its sources. That is a freshness question and it is satisfied by a corrupt file of
the right age. This asks whether the thing renders.

What it checks, and why each one is here rather than assumed:

  parses             A PDF that pdfinfo cannot read is not a document, however many
                     bytes it has.
  page count         A truncated build produces a valid short PDF. The floors are
                     deliberately loose; they catch a collapse, not a page of drift.
  page size          All three are A4 by construction. A silent geometry change would
                     otherwise be invisible until someone printed one.
  fonts embedded     A PDF referencing a font it does not embed renders differently on
                     a machine that lacks it. Every font here must be embedded.
  text extractable   Catches an encoding failure that looks correct on screen and yields
                     nothing to a search, a screen reader, or the citation checker.
  ink inside page    The overfull-box gate reads the TeX log, so it only sees what TeX
                     chose to warn about. This measures the rendered result instead.

On the last one: the bound is the paper edge, not the type block. Terminal punctuation is
deliberately set a point or two into the margin by microtype, so a type-block bound would
fail on correct typesetting. What cannot be correct is ink at the paper's edge.

Run from anywhere:  python3 tools/check_pdfs.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

A4_W, A4_H = 595.276, 841.890
SIZE_TOLERANCE = 2.0          # points
EDGE_MARGIN = 18.0            # a quarter inch of paper that must stay blank

DOCUMENTS = {
    "build/nobody-in-charge.pdf": 200,
    "paper/anonymity-as-an-aggregation-condition.pdf": 20,
    "reference/PRIMER-steps-and-traditions.pdf": 10,
}

failures: list[str] = []
notes: list[str] = []


def require(ok: bool, message: str) -> None:
    (notes if ok else failures).append(("OK: " if ok else "FAIL: ") + message)


def run(cmd: list[str]) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, check=False).stdout
    except FileNotFoundError:
        raise SystemExit(f"{cmd[0]} not found; install poppler to run this check") from None


def check(rel: str, min_pages: int) -> None:
    path = ROOT / rel
    name = Path(rel).name
    if not path.exists():
        require(False, f"{name}: exists")
        return

    info = run(["pdfinfo", str(path)])
    pages = re.search(r"^Pages:\s+(\d+)", info, re.M)
    require(bool(pages), f"{name}: parses as a PDF")
    if not pages:
        return

    n = int(pages.group(1))
    require(n >= min_pages, f"{name}: has {n} pages, floor is {min_pages}")

    size = re.search(r"^Page size:\s+([\d.]+) x ([\d.]+)", info, re.M)
    if size:
        w, h = float(size.group(1)), float(size.group(2))
        require(abs(w - A4_W) < SIZE_TOLERANCE and abs(h - A4_H) < SIZE_TOLERANCE,
                f"{name}: page size is A4 ({w:.0f} x {h:.0f} pt)")

    fonts = run(["pdffonts", str(path)])
    rows = [ln for ln in fonts.splitlines()[2:] if ln.strip()]
    not_embedded = [ln.split()[0] for ln in rows
                    if len(ln.split()) > 3 and ln.split()[3].lower() == "no"]
    require(not not_embedded,
            f"{name}: all {len(rows)} fonts embedded"
            + (f"; not embedded: {', '.join(not_embedded[:3])}" if not_embedded else ""))

    text = run(["pdftotext", str(path), "-"])
    require(len(text.split()) > 500,
            f"{name}: text extractable ({len(text.split()):,} words)")

    bbox = run(["pdftotext", "-bbox", str(path), "-"])
    worst_left, worst_right, bad_pages = A4_W, 0.0, []
    for i, page in enumerate(bbox.split("<page")[1:], 1):
        xs_min = [float(x) for x in re.findall(r'xMin="([\d.]+)"', page)]
        xs_max = [float(x) for x in re.findall(r'xMax="([\d.]+)"', page)]
        if not xs_min:
            continue
        left, right = min(xs_min), max(xs_max)
        worst_left, worst_right = min(worst_left, left), max(worst_right, right)
        if left < EDGE_MARGIN or right > A4_W - EDGE_MARGIN:
            bad_pages.append(i)
    require(not bad_pages,
            f"{name}: ink stays {EDGE_MARGIN:.0f}pt clear of the paper edge "
            f"(closest {min(worst_left, A4_W - worst_right):.1f}pt)"
            + (f"; breached on pages {bad_pages[:5]}" if bad_pages else ""))


def main() -> int:
    for rel, floor in DOCUMENTS.items():
        check(rel, floor)
    for line in notes:
        print(line)
    for line in failures:
        print(line)
    print(f"\n{len(notes)} checks passed; {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
