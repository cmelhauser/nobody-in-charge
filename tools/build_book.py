"""Assemble the whole book into build/nobody-in-charge.md, then render it.

Why this file exists. The book had been rendering since 2 August 2026, but the
assembler was described in `research/progress-log.md` rather than stored, and README
pointed at that description. A build step that lives only in prose is not reproducible,
and the first person to need it would have had to reconstruct it from the output. It is
now a script.

What it assembles, in order:

  front matter        the YAML header, with the date taken from --date or today
  preface             manuscript/ch00-preface.md
  introduction        manuscript/ch00b-introduction.md
  Parts One to Six    a title page, then the chapters of that part
  Appendices          a title page, then the technical appendix, the primer and the
                      working paper

Three transformations, all of them on the build copy only. THE SOURCE FILES ARE NEVER
WRITTEN TO.

  1. Each source opens with `# Chapter Nine` on one line and `## Confident and Wrong`
     on the next. Those are merged into `# Chapter Nine: Confident and Wrong`, so that
     pandoc's --top-level-division=chapter gives one chapter per file and the table of
     contents at depth 1 lists chapters rather than every section inside them.
  2. Four Unicode subscripts are mapped to plain digits, because the body font lacks
     the glyphs and the book's own convention already writes T11 and delta0 that way.
  3. YAML front matter in an included file is stripped, since only the assembled
     document carries a header.

The working paper is LaTeX and is converted by pandoc, with its headings shifted down
one level so its sections sit inside the appendix chapter rather than becoming chapters
of the book. The paper's own PDF remains the authoritative rendering of the paper; this
copy exists so the book is self-contained.

Run:
    python3 tools/build_book.py            assemble and render
    python3 tools/build_book.py --no-pdf   assemble only
"""
import os
import re
import shutil
import subprocess
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BUILD = os.path.join(ROOT, 'build')
OUT_MD = os.path.join(BUILD, 'nobody-in-charge.md')
OUT_PDF = os.path.join(BUILD, 'nobody-in-charge.pdf')
PAPER_TEX = os.path.join(ROOT, 'paper', 'anonymity-as-an-aggregation-condition.tex')

# The body font lacks these glyphs. The book writes T11 and delta0 in plain digits
# anyway, so the build copy is made consistent with the book's own convention.
SUBSCRIPTS = {'₀': '0', '₁': '1', '₂': '2', '₃': '3',
              '₄': '4', '₅': '5', '₆': '6', '₇': '7',
              '₈': '8', '₉': '9'}

HEADER = """---
title: "Nobody in Charge"
subtitle: "How a Fellowship of Drunks Solved a Problem in Mathematics Without Knowing It"
author:
  - "Human Author: Christopher Melhauser"
  - "AI Writing Collaborator: theonlymuffinbot"
  - "Models: Anthropic Claude Opus 5; OpenAI GPT-5.6 Sol/Terra"
date: "Draft of {date}"
documentclass: report
classoption: [11pt, oneside]
geometry: [a4paper, margin=1.05in]
mainfont: "TeX Gyre Pagella"
linestretch: 1.06
toc: true
toc-depth: 1
numbersections: false
colorlinks: true
linkcolor: black
urlcolor: black
header-includes:
  - \\usepackage{{microtype}}
  - \\usepackage{{booktabs}}
  - \\usepackage{{longtable}}
  - \\setlength{{\\emergencystretch}}{{3em}}
  - \\usepackage[htt]{{hyphenat}}
  - \\usepackage{{xurl}}
  - \\usepackage{{etoolbox}}
  - \\AtBeginEnvironment{{longtable}}{{\\footnotesize}}
  - \\usepackage{{titlesec}}
  - \\titleformat{{\\chapter}}[display]{{\\normalfont\\Large\\bfseries}}{{}}{{0pt}}{{\\Large}}
  - \\titlespacing*{{\\chapter}}{{0pt}}{{0pt}}{{28pt}}
---
"""

PART_PAGE = """
\\clearpage
\\thispagestyle{{empty}}
\\vspace*{{0.32\\textheight}}
\\begin{{center}}
{{\\Large\\bfseries {title}}}{sub}
\\end{{center}}
\\clearpage
"""

# (part title, part subtitle, [chapter files in order])
PARTS = [
    ("Part One", "The First Fellowship", [
        "ch01-chases-tavern.md",
        "ch02-the-fade.md",
        "ch03-the-man-who-was-the-movement.md",
        "ch04-akron.md",
        "ch05-twelve-points.md",
        "ch06-the-sociologist.md",
    ]),
    ("Part Two", "The Condition", [
        "ch07-how-a-room-decides.md",
        "ch08-the-condition.md",
        "ch09-confident-and-wrong.md",
        "ch10-rotation-has-to-be-wide.md",
        "ch11-what-the-washingtonians-lacked.md",
    ]),
    ("Part Three", "The Member", [
        "ch12-twelve-dials.md",
        "ch13-can-you-skip-a-step.md",
        "ch14-the-leaky-bucket.md",
        "ch15-helping-is-not-the-reward.md",
    ]),
    ("Part Four", "Where the Two Halves Meet", [
        "ch16-the-pairing-that-isnt.md",
        "ch17-what-a-tradition-carries.md",
        "ch18-two-kinds-of-rule.md",
    ]),
    ("Part Five", "How Groups Die", [
        "ch19-you-cannot-close-the-door.md",
        "ch20-three-ways-to-starve.md",
        "ch21-the-healthy-looking-corpse.md",
        "ch22-what-you-cannot-engineer.md",
    ]),
    ("Part Six", "What I Do Not Know", [
        "ch23-the-wrong-turns.md",
        "ch24-what-would-settle-it.md",
        "ch25-what-a-model-cannot-tell-you.md",
    ]),
]


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def strip_front_matter(text):
    """Remove a leading YAML block. Only the assembled document carries a header."""
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            return text[end + 5:].lstrip('\n')
    return text


def demote_subscripts(text):
    for k, v in SUBSCRIPTS.items():
        text = text.replace(k, v)
    return text


def merge_title(text):
    """`# Chapter Nine` + `## Confident and Wrong` -> `# Chapter Nine: Confident and Wrong`."""
    return re.sub(r'^# ([^\n]+)\n+## ([^\n]+)\n', r'# \1: \2\n', text, count=1)


def part_page(title, subtitle=None):
    sub = '\\\\[0.6em]\n{\\large\\itshape %s}' % subtitle if subtitle else ''
    return PART_PAGE.format(title=title, sub=sub)


def chapter(path):
    return demote_subscripts(merge_title(strip_front_matter(read(path)))).rstrip() + '\n'


def convert_paper():
    """Convert the LaTeX paper to markdown, its sections one level down.

    Shifting is what keeps the paper's `\\section{Introduction}` from becoming a chapter
    of the book. With the shift its sections are `##`, which the depth-1 contents page
    does not list, so the paper appears in the table of contents as one entry.
    """
    try:
        md = subprocess.run(
            # `-simple_tables` matters. As a simple table the paper's mapping table is one
            # line per row, so nothing can wrap and it converts to a 211-character table
            # whose relative column widths are then computed against a 72-column reference,
            # putting it about three line widths wide and off the page. Disabling simple
            # tables emits a grid table whose cells wrap at --columns instead.
            ['pandoc', PAPER_TEX, '-t', 'markdown-simple_tables', '--columns=90',
             '--shift-heading-level-by=1'],
            capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        raise SystemExit('could not convert the paper: %s' % exc)
    return demote_subscripts(resolve_paper_crossrefs(md)).strip() + '\n'


def resolve_paper_crossrefs(md):
    """Neutralize LaTeX cross-reference markup that does not survive the round trip.

    The paper is LaTeX, and its `\\label`/`\\eqref` machinery converts to pandoc link
    syntax that the second pass renders literally, so the book printed `[eq:err]` and
    `[prop:one]` where the paper prints a number. The paper's own PDF remains the
    authoritative rendering; inside the book these become plain words rather than dead
    identifiers. A numbered scheme would require numbering the paper's floats a second
    time in the book's own sequence, which would then disagree with the paper.
    """
    # Anchor spans that pandoc emits for \label, e.g. [\[prop:one\]]{#prop:one label="..."}
    md = re.sub(r'\[\\\[[^\]]*?\\\]\]\{#[^}]*?\}\s*', '', md)
    # Reference links, e.g. [\[eq:err\]](#eq:err){reference-type="ref" reference="eq:err"}
    def _ref(match):
        target = match.group(1)
        if target.startswith('eq:'):
            return 'the consensus-error equation above'
        if target.startswith('prop:'):
            return 'the proposition above'
        if target.startswith('tab:'):
            return 'the table above'
        if target.startswith('sec:'):
            return 'the section above'
        return 'above'
    md = re.sub(r'\[\\\[[^\]]*?\\\]\]\(#([^)]*?)\)\{reference-type="[^"]*"\s*reference="[^"]*"\}',
                _ref, md)
    # A leading "N." in a table cell is read as an ordered-list marker. Pandoc's LaTeX
    # reader escapes every number except 1, which is the default list start and is dropped
    # outright, so the paper's mapping table lost the "1." from its Common welfare row.
    # Escape the survivors, then restore the one that was eaten.
    # The replacements above are noun phrases, so a preceding "Equation" or "equation ("
    # left over from the LaTeX would read "Equation the consensus-error equation above".
    md = re.sub(r'\b[Ee]quation\s+\((the [^)]*? above)\)', r'\1', md)
    md = re.sub(r'\b[Ee]quation\s+(the [a-z-]+ equation above)', r'\1', md)
    md = re.sub(r'\b[Ee]quation\s+(the proposition above)', r'\1', md)

    # Cells arrive either indented (simple and multiline tables) or after a pipe (grid and
    # pipe tables), so both openings have to be handled.
    md = re.sub(r'(\n(?:\s{2,}|\|\s*))(\d{1,2})\.(\s+\S)',
                lambda m: f'{m.group(1)}{m.group(2)}\\.{m.group(3)}', md)
    md = re.sub(r'(\n(?:\s{2,}|\|\s*))\.(\s+\S)',
                lambda m: f'{m.group(1)}1\\.{m.group(2)}', md)
    return md


def assemble(build_date):
    out = [HEADER.format(date=build_date)]
    out.append(chapter(os.path.join(ROOT, 'manuscript', 'ch00-preface.md')))
    out.append(chapter(os.path.join(ROOT, 'manuscript', 'ch00b-introduction.md')))

    for title, subtitle, files in PARTS:
        out.append(part_page(title, subtitle))
        for name in files:
            out.append(chapter(os.path.join(ROOT, 'manuscript', name)))

    out.append(part_page('Appendices'))

    # Appendix one: the technical appendix, unchanged and still titled as the rest of
    # the book refers to it. Its section numbers (A2, A5.4 and so on) are cited from
    # chapters by name, so the title is deliberately not renumbered here.
    out.append(demote_subscripts(strip_front_matter(
        read(os.path.join(ROOT, 'appendix', 'APPENDIX.md')))).rstrip() + '\n')

    # Appendix two: the primer. Its own H1 is replaced so the chapter heading names it
    # as an appendix in the contents page.
    primer = strip_front_matter(read(os.path.join(
        ROOT, 'reference', 'PRIMER-steps-and-traditions.md')))
    primer = re.sub(
        r'^# [^\n]+\n',
        '# Appendix: What the Model Says About the Twelve Steps and the Twelve Traditions\n',
        primer, count=1)
    out.append(demote_subscripts(primer).rstrip() + '\n')

    # Appendix three: the working paper the book grew out of.
    out.append('# Appendix: The Working Paper\n\n'
               '*Anonymity as an Aggregation Condition: Governance, Resource Structure,\n'
               'and Membership Dynamics in Twelve-Step Mutual-Aid Organizations.*\n\n'
               'This is the academic paper the book grew out of, reproduced so that the\n'
               'book is self-contained. Its LaTeX source at\n'
               '`paper/anonymity-as-an-aggregation-condition.tex` remains the single\n'
               'source of truth for this document, and `paper/'
               'anonymity-as-an-aggregation-condition.pdf`\n'
               'is its authoritative rendering; the copy below is converted from that\n'
               'source at build time and its typesetting is the book\'s rather than the\n'
               "paper's.\n")
    out.append(convert_paper())

    return '\n'.join(out)


def main():
    build_date = date.today().strftime('%-d %B %Y')
    for i, arg in enumerate(sys.argv):
        if arg == '--date' and len(sys.argv) > i + 1:
            build_date = sys.argv[i + 1]

    os.makedirs(BUILD, exist_ok=True)
    text = assemble(build_date)
    with open(OUT_MD, 'w', encoding='utf-8') as fh:
        fh.write(text)
    print('wrote %s, %d words' % (OUT_MD, len(text.split())))

    if '--no-pdf' in sys.argv:
        return
    engine = next((name for name in ('xelatex', 'tectonic') if shutil.which(name)), None)
    if engine is None:
        raise SystemExit('no PDF engine found; install xelatex or tectonic')
    cmd = ['pandoc', OUT_MD, '-o', OUT_PDF, '--pdf-engine=' + engine,
           '--top-level-division=chapter']
    res = subprocess.run(cmd, capture_output=True, text=True)
    log = os.path.join(BUILD, 'pandoc.log')
    with open(log, 'w', encoding='utf-8') as fh:
        fh.write(res.stdout + res.stderr)
    if res.returncode != 0:
        raise SystemExit('pandoc failed, see %s' % log)
    print('wrote %s using %s' % (OUT_PDF, engine))


if __name__ == '__main__':
    main()
