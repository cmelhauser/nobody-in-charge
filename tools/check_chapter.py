#!/usr/bin/env python3
"""House-style check. Run against any chapter file before calling it done.

    python3 tools/check_chapter.py manuscript/ch09-confident-and-wrong.md
    python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
    python3 tools/check_chapter.py      # checks every manuscript/ch*.md

Enforces the conventions established across Part One and Chapter 8.
Every rule below exists because a chapter broke it once.

Reads: each file named on the command line; with no arguments, the first of
`manuscript/ch*.md`, `ch*.md` and `../manuscript/ch*.md` (relative to the working directory)
that matches anything. Imports `textstat` if it is installed, for a Flesch-Kincaid grade;
without it the grade is reported as "FK n/a" and nothing else changes.
Writes: one status line per file and any FAIL or warn lines to standard output.
Exit codes: 0 when no file has a FAIL (warnings do not count), 1 when any file does, 2 when
no arguments were given and no chapter files were found. A named file that cannot be opened
raises, so the interpreter exits 1 with a traceback.
"""
import glob
import os
import re
import sys

WANT_PARTS = ['1. What the model says', '2. The technical version',
              '3. Notes on sources', '4. References']

# Front matter: prose only, no Machinery, no chapter heading. The introduction joined the
# preface here on 2 August 2026. Both address the reader rather than making a claim, and
# neither carries a figure of its own: every number they quote is asserted in the chapter it
# belongs to, which is why they need no Machinery of their own.
FRONT_MATTER = ('ch00-preface', 'ch00b-introduction')

# Back matter: the same structural exemption, for a different reason. The primer is an
# appendix, not a chapter. It has no Machinery because it *is* machinery: every figure in it
# is copied from a chapter's Machinery, the notebook or a cached JSON, and it produces no
# result of its own. Added 5 August 2026, when running this checker over the primer produced
# four FAILs, all of them the checker insisting a non-chapter be a chapter. The house rule is
# to fix the check rather than the prose, so the exemption is structural only: the primer is
# still held to every notation, punctuation and sentence-length rule below.
#
# What this exemption COSTS, stated here because it is not obvious. Skipping the structural
# block also skips the reference-heading rules, so the primer's own reference section is not
# checked for canonical headings or their order. It has them, and nothing enforces that it
# keeps them.
BACK_MATTER = ('PRIMER-steps-and-traditions',)


def check(path: str) -> bool:
    """Check one chapter file against the house style and print its verdict.

    Prints a status line (OK, warn or FAIL, the word count and the Flesch-Kincaid grade)
    followed by one indented line per FAIL and per warning. Returns True when the file has no
    FAIL, so callers can run it over many files without short-circuiting. Front and back
    matter (see `FRONT_MATTER` and `BACK_MATTER`) skip the structural rules but keep the
    notation, punctuation and readability rules.
    """
    with open(path) as fh:
        t = fh.read()
    name = os.path.basename(path)
    fails, warns = [], []
    is_front = (any(name.startswith(f) for f in FRONT_MATTER)
                or any(name.startswith(b) for b in BACK_MATTER))

    # --- structure ---
    if is_front:
        # front matter still obeys the prose rules below, but has no Machinery
        # and no chapter heading. Skip the structural block.
        narrative, mach = t, ''
    elif '## The Machinery' not in t:
        fails.append("no Machinery section")
        narrative, mach = t, ''
    else:
        i = t.index('## The Machinery')
        narrative, mach = t[:i], t[i:]

    if not is_front:
        head = t.split('\n')[:4]
        if not any(ln.startswith('# Chapter ') for ln in head):
            fails.append("first heading must be '# Chapter <Word>'")
        if not any(ln.startswith('## ') for ln in head):
            fails.append("second heading must be '## <Title>'")

        got = [re.sub(r'^### ', '', ln) for ln in mach.split('\n')
               if ln.startswith('### ') and len(ln) > 4 and ln[4].isdigit()]
        if got != WANT_PARTS:
            fails.append(f"Machinery parts wrong: {got}")

    # --- main-text style ---
    if re.findall(r'^### ', narrative, re.M):
        fails.append("no ### subheadings in main text; separate sections with ---")
    if '\n|---' in narrative:
        fails.append("no tables in main text; put figures in Machinery part 2 and "
                     "render them as prose in the narrative")

    # --- notation and punctuation ---
    if '$' in t:
        fails.append("no LaTeX; inline symbols in plain text, display equations as > blockquotes")
    stray = re.findall(r'\\[a-zA-Z]+', t)
    if stray:
        fails.append(f"bare LaTeX commands left behind: {sorted(set(stray))[:6]}")
    for line in t.split('\n'):
        if '\u2014' in line and not line.strip().startswith('>'):
            fails.append("em-dash in author prose (quoted sources may keep theirs)")
            break

    # --- sourcing discipline ---
    # The reference section has exactly five permitted headings, in this order. Anything else
    # is a FAIL rather than a warning: the section had grown 27 heading variants before it was
    # normalised on 2 August 2026, which made it impossible to see at a glance what a chapter
    # had actually read. Not every heading must appear, but those that do must be canonical,
    # must be in this order, and must each be on a line of their own.
    CANON = ['Read in full', 'Cited at a remove', 'Referenced but not reproduced',
             'Internal, and reproducible from this repository', 'What was not read']
    if mach and not is_front:
        refs_i = mach.find('### 4. References')
        refs = mach[refs_i:] if refs_i >= 0 else ''
        if not refs:
            fails.append("no '### 4. References' section")
        else:
            heads = [m.group(1).rstrip(':.')
                     for m in re.finditer(r'^\*\*(.+?)[:.]?\*\*\s*$', refs, re.M)]
            odd = [h for h in heads if h not in CANON]
            if odd:
                fails.append('non-canonical reference heading(s): ' + '; '.join(odd))
            idx = [CANON.index(h) for h in heads if h in CANON]
            if idx != sorted(idx):
                fails.append('reference headings out of canonical order: ' + ', '.join(heads))
            if len(set(heads)) != len(heads):
                fails.append('duplicate reference headings: ' + ', '.join(heads))
            for req in ('Read in full', 'Cited at a remove', 'What was not read'):
                if req not in heads:
                    fails.append(f"references missing the '{req}' heading")
            # An entry marked as read must sit under Read in full. On 28 September 2026 five
            # were found under "Cited at a remove", each marked **Read in full** or **Now read
            # at source** in place when it was read in August instead of being moved, so the
            # heading and the entry contradicted each other in plain sight.
            marker = re.compile(r'\*\*(?:now )?(?:read in full|read at source)\b[^*]*\*\*', re.I)
            sections = re.split(r'^\*\*(' + '|'.join(re.escape(c) for c in CANON) +
                                r')[:.]?\*\*\s*$', refs, flags=re.M)
            # re.split with one capture group alternates [preamble, heading, body, ...].
            for sect_head, body in zip(sections[1::2], sections[2::2], strict=True):
                if sect_head == 'Read in full':
                    continue
                for entry in (e for e in body.split('\n\n') if marker.search(e)):
                    fails.append(f"an entry marked as read sits under '{sect_head}': "
                                 f"{entry.strip()[:60]}...")
            # An inline lead like "**What was not read.** Some prose" is not a heading and was
            # how sixteen chapters ended up with the statement buried inside another section.
            for m in re.finditer(r'^\*\*(' + '|'.join(re.escape(c) for c in CANON) +
                                 r')[^*]*\*\*[ \t]+\S', refs, re.M):
                fails.append('canonical heading used inline rather than on its own line: '
                             f'{m.group(1)}')

    # --- readability ---
    prose = " ".join(ln.strip() for ln in narrative.split('\n')
                     if ln.strip() and not ln.startswith(('#', '|', '>')))
    words = len(prose.split())
    try:
        import textstat
        fk = textstat.flesch_kincaid_grade(prose)
        # Target is under 10; above that a chapter is probably carrying too much abstraction
        # per sentence. (textstat is optional and not in requirements-dev.txt, so the grades
        # drafted chapters actually get are not recorded here.)
        if fk > 10.0:
            warns.append(f"FK grade {fk:.1f}; aim under 10")
        grade = f"FK {fk:.1f}"
    except ImportError:
        grade = "FK n/a"
    longs = [s for s in re.split(r'(?<=[.!?]) ', prose) if len(s.split()) > 45]
    if longs:
        warns.append(f"{len(longs)} sentence(s) over 45 words")

    status = "FAIL" if fails else ("warn" if warns else "OK")
    print(f"{name:<40}{status:<6}{words:>6}w  {grade}")
    for f in fails:
        print(f"    FAIL  {f}")
    for w in warns:
        print(f"    warn  {w}")
    return not fails


def main(argv: list[str] | None = None) -> int:
    """Check the files named in `argv` (default `sys.argv[1:]`) and return an exit code.

    With no files named, look for chapters from the repository root, the manuscript folder or
    a sibling of it, taking the first pattern that matches. Returns 0 when every file is
    clean, 1 when any file has a FAIL, and 2 when there was nothing to check.
    """
    args = sys.argv[1:] if argv is None else argv
    if args:
        targets = args
    else:
        # run from the repo root, the manuscript folder, or anywhere in between
        for pat in ('manuscript/ch*.md', 'ch*.md', '../manuscript/ch*.md'):
            targets = sorted(glob.glob(pat))
            if targets:
                break
        if not targets:
            print("no chapter files found; pass paths explicitly")
            return 2
    results = [check(p) for p in targets]   # no short-circuit; check every file
    ok = all(results)
    print("\nall clear" if ok else "\nfix the FAILs before calling the chapter done")
    return 0 if ok else 1


if __name__ == '__main__':
    from tool_help import help_requested
    help_requested(__doc__)
    sys.exit(main())
