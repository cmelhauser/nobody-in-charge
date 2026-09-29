#!/usr/bin/env python3
"""Render the standalone reference primer to PDF.

Why this file exists. The primer's PDF was being produced by a hand-typed pandoc command
that lived nowhere, so its typography was whatever the last person typed. On 16 August
2026 it was rendering at LaTeX's default article margins rather than the one inch the
project wanted, and four paragraphs of long monospace file paths were running outside the
type block. Fixing that by adding `header-includes` to the primer's own YAML worked, but
put raw LaTeX into a Markdown source that `tools/check_chapter.py` reads as prose, and the
checker correctly objected. The settings therefore live here, exactly as the book's live in
`tools/build_book.py`, and the Markdown stays clean.

The typography deliberately matches the book, so the standalone primer and the copy bound
into the book as an appendix look like the same document.

  geometry        a4paper, 1 inch margins
  mainfont        TeX Gyre Pagella, as the book
  tolerance       1500 with emergencystretch 4em, so TeX prefers a slightly loose line
                  to one that runs into the margin. Long unbreakable tokens, file paths
                  and identifiers, are what overflow without it.
  hyphenat[htt]   lets \\texttt spans break, which is where the overflow was
  tabcolsep 4pt   wide result tables were the other cause

Run from anywhere:
    python3 tools/build_primer.py
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from source_date import epoch as source_date_epoch

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "reference" / "PRIMER-steps-and-traditions.md"
OUT = ROOT / "reference" / "PRIMER-steps-and-traditions.pdf"

# The revision date printed on the primer, declared rather than read off the clock.
# See the note in build() for why it is neither computed nor hard-coded and unchecked.
REVISED_DATE = '22 September 2026'

# Passed as pandoc -V variables rather than written into the source, so that the Markdown
# contains no LaTeX. Keep in step with the HEADER in tools/build_book.py.
VARIABLES = [
    ("documentclass", "article"),
    ("classoption", "11pt"),
    ("geometry", "a4paper"),
    ("geometry", "margin=1in"),
    ("mainfont", "TeX Gyre Pagella"),
    ("linestretch", "1.06"),
    ("colorlinks", "true"),
    ("linkcolor", "black"),
    ("urlcolor", "black"),
]

HEADER_INCLUDES = r"""
\usepackage{microtype}
\usepackage{booktabs}
\usepackage{longtable}
\setlength{\emergencystretch}{4em}
\tolerance=1500
\hbadness=1500
\usepackage[htt]{hyphenat}
\usepackage{xurl}
\usepackage{etoolbox}
% Load the language so hyphenation patterns are certainly active.
\usepackage[english]{babel}
\usepackage{ragged2e}
% Pandoc's \raggedright stops TeX hyphenating, and TeX will not hyphenate the first
% word of a paragraph, which is what a table cell's content is. Both have to go for a
% long word in a narrow column to break. Column fractions are not stable across pandoc
% versions, so a column that is roomy here can be narrow elsewhere.
\newcommand{\nictabragged}{\RaggedRight\hspace{0pt}}
\AtBeginEnvironment{longtable}{\footnotesize\let\raggedright\nictabragged}
\setlength{\tabcolsep}{4pt}
"""


def main() -> int:
    if not SRC.exists():
        raise SystemExit("primer source not found: %s" % SRC)
    engine = next((n for n in ("xelatex", "tectonic") if shutil.which(n)), None)
    if engine is None:
        raise SystemExit("no PDF engine found; install xelatex or tectonic")

    header = ROOT / "build" / "primer-header.tex"
    header.parent.mkdir(parents=True, exist_ok=True)
    header.write_text(HEADER_INCLUDES.strip() + "\n")

    # Declared, not computed. This was `date.today()` until 27 September 2026, for a good
    # reason: the primer had carried a hard-coded "6 August 2026" through a substantial
    # revision on the 17th, which is how a date in a source file goes wrong, since nothing
    # checked it and nobody looked at it. Computing it fixed that and introduced the opposite
    # fault, because continuous integration rebuilds on every push and the printed date then
    # recorded when a machine last ran pandoc. Something checks it now:
    # tools/check_docs.py fails if REVISED_DATE is older than the last commit touching the
    # primer, or if the rendered PDF does not carry it. Change it when the primer changes.
    cmd = ["pandoc", str(SRC), "-o", str(OUT), "--pdf-engine=" + engine,
           "-M", "date=Revised " + REVISED_DATE,
           "--include-in-header", str(header)]
    for key, value in VARIABLES:
        cmd += ["-V", "%s=%s" % (key, value)]

    # A fixed timestamp from REVISED_DATE makes a rebuild of unchanged text byte-identical;
    # tools/source_date.py says why. A caller's own SOURCE_DATE_EPOCH wins.
    env = dict(os.environ)
    env.setdefault("SOURCE_DATE_EPOCH", str(source_date_epoch("primer")))
    res = subprocess.run(cmd, capture_output=True, text=True, env=env)
    log = ROOT / "build" / "primer-pandoc.log"
    log.write_text(res.stdout + res.stderr)
    if res.returncode != 0:
        # Print the lines that name the failure, then the tail. Tail alone is not enough:
        # on a cold runner tectonic emits dozens of "note: downloading" lines after the
        # error, so the last forty lines can be entirely package fetches.
        lines = (res.stdout + res.stderr).splitlines()
        errs = [ln for ln in lines
                if re.search(r"^!|error:|Error|Undefined|not loadable|not found|LaTeX Error", ln)]
        tail = (errs[-25:] + ["--- tail ---"] + lines[-15:]) if errs else lines[-40:]
        sys.stderr.write("\n".join(tail) + "\n")
        raise SystemExit("pandoc failed, see %s" % log)

    overfull = sum(1 for line in (res.stdout + res.stderr).splitlines()
                   if "Overfull" in line)
    print("wrote %s using %s" % (OUT, engine))
    print("overfull boxes: %d" % overfull)
    if overfull:
        print("WARNING: content is running outside the type block; see " + str(log))
    return 0


if __name__ == "__main__":
    sys.exit(main())
