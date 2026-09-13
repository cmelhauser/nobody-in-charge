#!/usr/bin/env python3
"""Render the 1939 working-manuscript note to PDF.

The note is research/incorporated/WorkingManuscript_1939/edits_and_suggested_uses.md. Its
PDF cannot sit beside it: every .pdf under research/incorporated/ is git-ignored as a source
document, tests/test_tools_integration.py fails if one is tracked, and build_corpus.py would
take a second PDF in that directory for the source itself. It is written to build/, next to
the book, and rebuilt by this script rather than by a hand-typed pandoc command, for the
reason given at the top of tools/build_primer.py.

The typography matches the primer: A4, one inch margins, TeX Gyre Pagella, and the same
tolerance and table settings. Four things are specific to the note, and none changes a word
of it. They are made to a scratch copy; the source is only read.

  title block     the H1 becomes the title, broken after its colon, and the italic dateline
                  under it is set beneath at text size, where it fits on one line
  table columns   pandoc sizes pipe-table columns by the dashes in the separator row, and
                  the source's equal dashes would give the short page-number column a third
                  of the line; the scratch copy weights them 10:30:52
  table breaks    the table is short, so it is kept on one page with its heading rather than
                  split a few rows from the foot of a page
  section breaks  every horizontal rule in the note stands immediately before a section
                  heading, so the rules are dropped and each section opens with a hairline
                  instead. This is checked, not assumed.

The running head is taken from the title and the dateline, so it cannot drift from them.

Run from anywhere:
    python3 tools/build_note.py
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from itertools import takewhile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "research" / "incorporated" / "WorkingManuscript_1939" / "edits_and_suggested_uses.md"
OUT = ROOT / "build" / "WorkingManuscript_1939-edits-and-suggested-uses.pdf"

VARIABLES = [
    ("documentclass", "article"),
    ("classoption", "11pt"),
    ("geometry", "a4paper"),
    ("geometry", "margin=1in"),
    ("geometry", "headheight=14pt"),
    ("mainfont", "TeX Gyre Pagella"),
    ("linestretch", "1.06"),
    # Pandoc's template otherwise redefines \paragraph in a way titlesec does not expect.
    ("subparagraph", "true"),
]

# @SHORT@ and @DATE@ are filled from the note. Placeholders rather than str.format, so the
# LaTeX braces need no doubling.
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
\usepackage[english]{babel}
\usepackage{ragged2e}
\usepackage{needspace}
% As the primer: let a long word in a narrow table column break. See tools/build_book.py.
\newcommand{\nictabragged}{\RaggedRight\hspace{0pt}}
\AtBeginEnvironment{longtable}{\small\let\raggedright\nictabragged}
% The dateline is passed as the date, so titling sets it and pandoc's \large subtitle
% does not.
\usepackage{titling}
\setlength{\droptitle}{-3em}
\pretitle{\begin{center}\LARGE}
\posttitle{\par\end{center}\vspace{0.1em}}
\preauthor{}
\postauthor{}
\predate{\begin{center}\normalsize}
\postdate{\par\vspace{1.4ex}\rule{4em}{0.4pt}\end{center}\vspace{0.4em}}
\usepackage{titlesec}
\titleformat{\section}{\titlerule\vspace{0.8ex}\normalfont\Large}{}{0pt}{}
\titlespacing*{\section}{0pt}{3.2ex plus 1ex minus 0.2ex}{1.2ex plus 0.2ex}
\titleformat{\subsection}{\normalfont\large\itshape}{}{0pt}{}
\titlespacing*{\subsection}{0pt}{2.4ex plus 0.8ex minus 0.2ex}{0.6ex plus 0.2ex}
% The note's list items run to several lines; pandoc's tight lists set them flush.
\providecommand{\tightlist}{}
\renewcommand{\tightlist}{\setlength{\itemsep}{0.35\baselineskip}\setlength{\parskip}{0pt}}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyhead[L]{\footnotesize\itshape @SHORT@}
\fancyhead[R]{\footnotesize\itshape Working note, @DATE@}
\fancyfoot[C]{\footnotesize\thepage}
\fancypagestyle{plain}{\fancyhf{}\renewcommand{\headrulewidth}{0pt}\fancyfoot[C]{\footnotesize\thepage}}
\clubpenalty=10000
\widowpenalty=10000
"""

SEPARATOR = re.compile(r"\|(?:-{3,}\|){3}")
WEIGHTED = "|" + "-" * 10 + "|" + "-" * 30 + "|" + "-" * 52 + "|"


def prepare(text: str) -> tuple[str, str, str, str]:
    """Return the scratch Markdown, the plain title, the running title and the date."""
    lines = text.splitlines()
    if len(lines) < 5 or not lines[0].startswith("# ") or lines[1] or lines[3]:
        raise SystemExit("note does not open with a title, a blank line and a dateline")
    title, dateline = lines[0][2:], lines[2]
    short, colon, rest = title.partition(": ")
    when = re.search(r"\b\d{1,2} [A-Z][a-z]+ \d{4}\b", dateline)
    if not colon or not when or not dateline.startswith("*"):
        raise SystemExit("unexpected title or dateline: %r / %r" % (title, dateline))

    body, tables = [], 0
    for i, line in enumerate(lines[4:], start=4):
        if line == "---":
            following = next((ln for ln in lines[i + 1:] if ln.strip()), "")
            if not following.startswith("## "):
                raise SystemExit("line %d: a rule that does not open a section" % (i + 1))
            continue
        if SEPARATOR.fullmatch(line):
            # Ask for room for the whole table before its heading, or before its header
            # row if no heading leads into it. Rows here run to one or two lines.
            rows = sum(1 for _ in takewhile(lambda ln: ln.startswith("|"), lines[i + 1:]))
            at = len(body) - 1
            k = at - 1
            while k >= 0 and not body[k].strip():
                k -= 1
            if k >= 0 and body[k].startswith("#"):
                at = k
            body[at:at] = ["\\needspace{%d\\baselineskip}" % (rows + rows // 2 + 5), ""]
            line, tables = WEIGHTED, tables + 1
        body.append(line)
    if tables != 1:
        raise SystemExit("expected one three-column table, found %d; revisit WEIGHTED" % tables)

    # A raw \\ rather than \newline: inside the centred title \\ is \@centercr, while
    # \newline adds an \hfil that pushes the first line off centre.
    front = ["---",
             "title: " + json.dumps(short + ":`\\\\`{=latex} " + rest, ensure_ascii=False),
             "date: " + json.dumps(dateline, ensure_ascii=False),
             "---", ""]
    return "\n".join(front + body) + "\n", title, short, when.group(0)


def main() -> int:
    if not SRC.exists():
        raise SystemExit("note not found: %s" % SRC)
    engine = next((n for n in ("xelatex", "tectonic") if shutil.which(n)), None)
    if engine is None:
        raise SystemExit("no PDF engine found; install xelatex or tectonic")

    markdown, title, short, when = prepare(SRC.read_text(encoding="utf-8"))
    header = HEADER_INCLUDES.strip().replace("@SHORT@", short).replace("@DATE@", when)
    OUT.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        md, tex = Path(tmp) / "note.md", Path(tmp) / "header.tex"
        md.write_text(markdown, encoding="utf-8")
        tex.write_text(header + "\n", encoding="utf-8")
        # title-meta is set explicitly because the title carries a raw line break, which
        # pandoc would otherwise have to guess at when it writes the PDF's title field.
        cmd = ["pandoc", str(md), "-o", str(OUT), "--pdf-engine=" + engine,
               "--shift-heading-level-by=-1",
               "--include-in-header", str(tex),
               "-V", "title-meta=" + title]
        for key, value in VARIABLES:
            cmd += ["-V", "%s=%s" % (key, value)]
        res = subprocess.run(cmd, capture_output=True, text=True)

    lines = (res.stdout + res.stderr).splitlines()
    if res.returncode != 0:
        # As build_primer.py: the lines naming the failure, then the tail.
        errs = [ln for ln in lines
                if re.search(r"^!|error:|Error|Undefined|not loadable|not found|LaTeX Error", ln)]
        tail = (errs[-25:] + ["--- tail ---"] + lines[-15:]) if errs else lines[-40:]
        sys.stderr.write("\n".join(tail) + "\n")
        raise SystemExit("pandoc failed")

    overfull = sum(1 for line in lines if "Overfull" in line)
    print("wrote %s using %s" % (OUT.relative_to(ROOT), engine))
    print("overfull boxes: %d" % overfull)
    if overfull:
        print("WARNING: content is running outside the type block")
        for line in lines:
            if "Overfull" in line:
                print("  " + line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
