#!/usr/bin/env python3
"""Verify the three rendered PDFs are sound documents, not merely present.

`tools/check_release.py` asks whether each artifact exists, is nontrivial, and is newer than
its sources. That is a freshness question, and a corrupt file of the right age satisfies it.
This asks whether the thing renders.

  parses            a PDF the reader cannot open is not a document, whatever it weighs
  page count        a truncated build produces a valid short PDF; the floors catch a
                    collapse, not a page of drift
  page size         all three are A4 by construction, and a silent geometry change would
                    otherwise stay invisible until somebody printed one
  fonts embedded    a PDF referencing a font it does not embed renders differently on a
                    machine that lacks it
  text extractable  catches an encoding failure that looks right on screen and yields
                    nothing to a search, a screen reader, or the citation checker
  ink inside page   measures the rendered result rather than the build log

Everything except the last uses pypdf, which is a pip dependency and needs nothing from the
system. That matters: the first version of this file shelled out to poppler, passed on the
author's machine, and failed on the runner, which had no `pdfinfo`. A checker with an
undeclared system dependency is a checker that does not run.

The ink measurement still needs poppler's `pdftotext -bbox`, because pypdf's text
transformation matrices are not reliable enough for the purpose: on a correct page they put
a left edge at -0.3pt, which would fail a bound the typesetting has not actually breached.
So that one check runs where poppler exists and reports itself skipped where it does not,
rather than passing silently. It is the least load-bearing of the six, because the
overfull-box gate already catches text leaving the type block from TeX's side.

On the bound: it is the paper edge, not the type block. Microtype sets terminal punctuation a
point or two into the margin deliberately, so a type-block bound would fail on correct work.
What cannot be correct is ink at the edge of the sheet.

Run from anywhere:  python3 tools/check_pdfs.py
"""
from __future__ import annotations

import re
import shutil
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
skips: list[str] = []


def require(ok: bool, message: str) -> None:
    (notes if ok else failures).append(("OK: " if ok else "FAIL: ") + message)


def embedded(font_ref) -> bool:
    """True if this font object carries its own glyph program."""
    font = font_ref.get_object()
    descriptor = font.get("/FontDescriptor")
    if descriptor is None and "/DescendantFonts" in font:
        descriptor = font["/DescendantFonts"][0].get_object().get("/FontDescriptor")
    if descriptor is None:
        return False
    d = descriptor.get_object()
    return any(k in d for k in ("/FontFile", "/FontFile2", "/FontFile3"))


def check_ink(path: Path, name: str) -> None:
    """Measure how close the rendered ink comes to the edge of the sheet."""
    if not shutil.which("pdftotext"):
        skips.append(f"SKIP: {name}: ink measurement needs poppler's pdftotext")
        return
    out = subprocess.run(["pdftotext", "-bbox", str(path), "-"],
                         capture_output=True, text=True, check=False).stdout
    closest, breached = A4_W, []
    for i, page in enumerate(out.split("<page")[1:], 1):
        xs_min = [float(x) for x in re.findall(r'xMin="([\d.]+)"', page)]
        xs_max = [float(x) for x in re.findall(r'xMax="([\d.]+)"', page)]
        if not xs_min:
            continue
        left, right = min(xs_min), max(xs_max)
        closest = min(closest, left, A4_W - right)
        if left < EDGE_MARGIN or right > A4_W - EDGE_MARGIN:
            breached.append(i)
    require(not breached,
            f"{name}: ink stays {EDGE_MARGIN:.0f}pt clear of the paper edge "
            f"(closest {closest:.1f}pt)"
            + (f"; breached on pages {breached[:5]}" if breached else ""))


def check(rel: str, min_pages: int) -> None:
    import pypdf

    path = ROOT / rel
    name = Path(rel).name
    if not path.exists():
        require(False, f"{name}: exists")
        return

    try:
        reader = pypdf.PdfReader(str(path))
        pages = reader.pages
        n = len(pages)
    except Exception as exc:                                    # noqa: BLE001
        require(False, f"{name}: parses as a PDF ({type(exc).__name__})")
        return
    require(True, f"{name}: parses as a PDF")
    require(n >= min_pages, f"{name}: has {n} pages, floor is {min_pages}")

    box = pages[0].mediabox
    w, h = float(box.width), float(box.height)
    require(abs(w - A4_W) < SIZE_TOLERANCE and abs(h - A4_H) < SIZE_TOLERANCE,
            f"{name}: page size is A4 ({w:.0f} x {h:.0f} pt)")

    seen, missing = set(), set()
    for page in pages:
        for key, ref in (page.get("/Resources", {}) or {}).get("/Font", {}).items():
            base = str(ref.get_object().get("/BaseFont", key))
            if base in seen:
                continue
            seen.add(base)
            if not embedded(ref):
                missing.add(base)
    require(not missing,
            f"{name}: all {len(seen)} fonts embedded"
            + (f"; not embedded: {', '.join(sorted(missing)[:3])}" if missing else ""))

    words = sum(len((p.extract_text() or "").split()) for p in pages)
    require(words > 500, f"{name}: text extractable ({words:,} words)")

    check_ink(path, name)


def main() -> int:
    try:
        import pypdf                                            # noqa: F401
    except ImportError:
        raise SystemExit("pypdf is required; pip install -r requirements-dev.txt") from None
    for rel, floor in DOCUMENTS.items():
        check(rel, floor)
    for line in notes:
        print(line)
    for line in skips:
        print(line)
    for line in failures:
        print(line)
    # Skips are counted apart from passes. A check that did not run is not a check that
    # succeeded, and reporting it as one is how a checker comes to mean nothing.
    tail = f"; {len(skips)} skipped" if skips else ""
    print(f"\n{len(notes)} checks passed; {len(failures)} failed{tail}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
