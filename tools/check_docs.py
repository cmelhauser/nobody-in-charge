#!/usr/bin/env python3
"""Fail when documentation states a count the repository contradicts.

Every other checker here verifies a number that came out of a cache. This one verifies the
sentences, because the sweep of 24 August 2026 found that all the drift had collected in
exactly the place nothing was reading: prose describing the repository itself.

None of those findings was scientific. They were counts and enumerations a tool could have
re-derived and nothing did. Six sentences said continuous integration had two jobs five days
after a third was added. `AGENTS.md` claimed five checkers, by name, under a line promising the
count was "countable from the tree", while the tree held six. Three files gave a corpus total of
31 and then listed seven, ten and none of the eleven record-only sources. The totals were right
and the enumerations were short, which is the failure mode that reads as correct.

So the rule this file enforces is narrow: **a sentence asserting how many of something this
repository has must agree with how many it has.** Each check derives the true value first, then
scans tracked Markdown for claims about it.

What is deliberately not checked:

  historical waypoints   `research/progress-log.md` is the dated record and its counts are
                         frozen at the moment they were written. `CLAUDE.md`'s source boundary
                         narrates growth the same way, so patterns here match only present-tense
                         phrasing ("holds 31 sources"), never a waypoint ("bringing the corpus
                         to 26").
  superseded blocks      a blockquote is how this project keeps a claim it has retired. Quoted
                         lines are skipped, which is what makes `BOOK-PLAN.md`'s 2 August
                         paragraph legal.
  generated output       `build/` is rebuilt from sources that are themselves checked.

Page counts need the rendered PDFs. All three are committed, so in practice they are present
and the check runs everywhere; the skip path exists for a tree where one has been deleted or not
yet built, and reports itself rather than passing silently, because a check that did not run is
not a check that succeeded. The `documents` job runs this file after rebuilding the PDFs from
source, which is the only place a page count is confirmed against a fresh build.

Run from anywhere:  python3 tools/check_docs.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Prose in this project spells small numbers. A claim is wrong whichever way it is written.
WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "twenty-one": 21, "twenty-five": 25, "thirty": 30,
    "thirty-one": 31, "thirty-two": 32, "thirty-three": 33,
}
CANONICAL_MODEL = "c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952"

passes: list[str] = []
failures: list[str] = []
skips: list[str] = []


def ok(message: str) -> None:
    passes.append(f"OK: {message}")


def fail(message: str) -> None:
    failures.append(f"FAIL: {message}")


def skip(message: str) -> None:
    skips.append(f"SKIP: {message}")


def value_of(token: str) -> int | None:
    """Read a count written as digits or as a word."""
    token = token.strip().lower()
    if token.isdigit():
        return int(token)
    return WORDS.get(token)


def tracked_markdown() -> list[Path]:
    """Tracked Markdown, less the generated book and the dated progress log."""
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z", "*.md"],
        check=True, capture_output=True,
    )
    paths = []
    for item in proc.stdout.split(b"\0"):
        if not item:
            continue
        rel = item.decode()
        if rel.startswith("build/") or rel == "research/progress-log.md":
            continue
        paths.append(ROOT / rel)
    return paths


def prose_lines(path: Path) -> list[tuple[int, str]]:
    """Numbered lines, minus blockquotes, which is how this project keeps retired claims."""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []
    return [
        (n, line) for n, line in enumerate(text.splitlines(), 1)
        if not line.lstrip().startswith(">")
    ]


def assert_claims(label: str, expected: int, pattern: re.Pattern[str], group: int = 1) -> None:
    """Every present-tense claim matching `pattern` must state `expected`."""
    wrong: list[str] = []
    seen = 0
    for path in tracked_markdown():
        rel = path.relative_to(ROOT)
        for number, line in prose_lines(path):
            for match in pattern.finditer(line):
                claimed = value_of(match.group(group))
                if claimed is None:
                    continue
                seen += 1
                if claimed != expected:
                    wrong.append(f"{rel}:{number}: says {match.group(group)!r}, tree has {expected}")
    if wrong:
        for item in wrong:
            fail(f"{label} ({item})")
    else:
        ok(f"{label} is {expected}, and {seen} claim(s) in tracked prose agree")


# --------------------------------------------------------------------------------------
# The derivations. Each answers its question from the tree, never from another document.
# --------------------------------------------------------------------------------------

def ci_jobs() -> list[str]:
    """Top-level job keys in the workflow, read without a YAML dependency.

    The `jobs:` mapping is at column 0 and its members at column 2. That is enough structure
    to count them, and it keeps this checker in the network-free job, which needs pip and
    nothing else.
    """
    text = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    names, inside = [], False
    for line in text.splitlines():
        if re.match(r"^jobs:\s*$", line):
            inside = True
            continue
        if inside:
            if line and not line.startswith(" ") and not line.startswith("#"):
                break
            found = re.match(r"^  ([A-Za-z0-9_-]+):\s*$", line)
            if found:
                names.append(found.group(1))
    return names


def check_ci_jobs() -> None:
    jobs = ci_jobs()
    if not jobs:
        fail("could not read job names from .github/workflows/ci.yml")
        return
    assert_claims(
        "continuous-integration job count",
        len(jobs),
        re.compile(r"(?:GitHub Actions runs|CI has)\s+([a-z]+|\d+)\s+jobs", re.IGNORECASE),
    )
    # "runs all three jobs", "runs both jobs" -- the same claim in a different shape.
    assert_claims(
        "job count in run_ci_locally descriptions",
        len(jobs),
        re.compile(r"runs\s+all\s+([a-z]+|\d+)\s+(?:continuous-integration\s+|CI\s+)?jobs",
                   re.IGNORECASE),
    )
    stale = re.compile(r"runs\s+both\s+(?:continuous-integration\s+|CI\s+)?jobs", re.IGNORECASE)
    hits = [
        f"{p.relative_to(ROOT)}:{n}"
        for p in tracked_markdown() for n, line in prose_lines(p) if stale.search(line)
    ]
    if len(jobs) != 2 and hits:
        for hit in hits:
            fail(f"'runs both jobs' but the workflow has {len(jobs)} ({hit})")
    else:
        ok(f"no prose says 'both jobs' while the workflow defines {len(jobs)}")

    # Every job named in prose must exist, which catches a rename as well as a miscount.
    named = re.compile(r"`(lint|unit-tests|checkers|documents|release)`")
    unknown = []
    for path in tracked_markdown():
        for number, line in prose_lines(path):
            for match in named.finditer(line):
                job = match.group(1)
                if job not in jobs and job != "release":
                    unknown.append(f"{path.relative_to(ROOT)}:{number}: names job `{job}`")
    if unknown:
        for item in unknown:
            fail(f"prose names a job the workflow does not define ({item})")
    else:
        ok(f"every CI job named in prose exists: {', '.join(jobs)}")


def check_checker_inventory() -> None:
    checkers = sorted(p.name for p in (ROOT / "tools").glob("check_*.py"))
    # build_corpus.py --check is a checker by behaviour and is counted as one in AGENTS.md.
    total = len(checkers) + 1
    assert_claims(
        "checker count",
        total,
        re.compile(r"\b([a-z]+|\d+)\s+checkers\b", re.IGNORECASE),
    )
    named = re.compile(r"`(check_[a-z_]+\.py)`")
    missing = []
    for path in tracked_markdown():
        for number, line in prose_lines(path):
            for match in named.finditer(line):
                if not (ROOT / "tools" / match.group(1)).exists():
                    missing.append(f"{path.relative_to(ROOT)}:{number}: {match.group(1)}")
    if missing:
        for item in missing:
            fail(f"prose names a checker that does not exist ({item})")
    else:
        ok(f"every checker named in prose exists ({total} counting build_corpus.py --check)")


def corpus_counts() -> tuple[int, int]:
    total, record_only = 0, 0
    for meta in sorted((ROOT / "research/incorporated").glob("*/metadata.json")):
        total += 1
        if json.loads(meta.read_text(encoding="utf-8")).get("record_only"):
            record_only += 1
    return total, record_only


def check_corpus() -> None:
    total, record_only = corpus_counts()
    # Present-tense only. "bringing the corpus to 26" is history and must stay legal.
    assert_claims(
        "corpus size",
        total,
        re.compile(r"(?:holds|of the|Eleven of the)\s+(\d+)\s+sources", re.IGNORECASE),
    )
    assert_claims(
        "corpus size in 'present N' phrasing",
        total,
        re.compile(r"corpus to its present\s+(\d+)", re.IGNORECASE),
    )
    assert_claims(
        "record-only count",
        record_only,
        re.compile(r"\b([A-Za-z]+|\d+)\s+(?:of the \d+ )?sources are\s+\*{0,2}(?:held as )?record only",
                   re.IGNORECASE),
    )
    assert_claims(
        "record-only count in 'N of the M sources are record only'",
        record_only,
        re.compile(r"\b([A-Za-z]+|\d+)\s+of the \d+ sources are held as record only", re.IGNORECASE),
    )


def check_model_scripts() -> None:
    scripts = [p.name for p in (ROOT / "model").glob("*.py") if p.name != "aa_group_model.py"]
    assert_claims(
        "analysis-script count",
        len(scripts),
        re.compile(r"\b([a-z]+|\d+)\s+analysis scripts\b", re.IGNORECASE),
    )


def check_chapters() -> None:
    # ch00-preface and ch00b-introduction are front matter, not numbered chapters. The book
    # is "25 chapters plus the preface and the introduction", and that is the claim checked.
    chapters = [
        p for p in (ROOT / "manuscript").glob("ch*.md")
        if re.match(r"^ch(?!00)\d{2}-", p.name)
    ]
    assert_claims(
        "chapter count",
        len(chapters),
        re.compile(r"\b(\d+)-chapter\b"),
    )
    assert_claims(
        "chapter count in 'N chapters plus preface'",
        len(chapters),
        re.compile(r"\b(\d+)\s+chapters plus"),
    )


def check_local_runner() -> None:
    """The runner's own header must document every job it implements."""
    path = ROOT / "tools/run_ci_locally.sh"
    text = path.read_text(encoding="utf-8")
    implemented = set(re.findall(r'\$job"\s*=\s*([a-z][a-z-]*)', text)) - {"all"}
    header = text.split("set -", 1)[0]
    documented = set(re.findall(
        r"^#\s+(lint|unit-tests|checkers|checks|documents)\s{2,}",
        header,
        re.MULTILINE,
    ))
    missing = implemented - documented
    if missing:
        fail(
            "tools/run_ci_locally.sh implements a job its usage does not document: "
            + ", ".join(sorted(missing))
        )
    else:
        ok(f"run_ci_locally.sh documents every job it implements: {', '.join(sorted(implemented))}")


def check_model_hash() -> None:
    """Any digest whose own label calls it the model hash must be the canonical one.

    The repository is full of legitimate non-canonical digests: every cache records the hash
    of the analysis script that wrote it, and every source record carries the hash of the
    document consulted. So the test is the label attached to this digest, not the neighbourhood
    it sits in. The label is whatever precedes the digest on its line, or, when the digest
    stands alone, the nearest preceding non-empty line.
    """
    digest = re.compile(r"\b[0-9a-f]{64}\b")
    claims_model = re.compile(r"\bmodel\b", re.IGNORECASE)
    claims_other = re.compile(r"analysis|script|scan|PDF|document|file|source", re.IGNORECASE)
    wrong = []
    for path in tracked_markdown():
        lines = prose_lines(path)
        for index, (number, line) in enumerate(lines):
            for found in digest.finditer(line):
                if found.group(0) == CANONICAL_MODEL:
                    continue
                label = line[: found.start()].strip(" `-*:")
                if not label:
                    for _, earlier in reversed(lines[max(0, index - 3): index]):
                        if earlier.strip():
                            label = earlier
                            break
                if claims_model.search(label) and not claims_other.search(label):
                    wrong.append(f"{path.relative_to(ROOT)}:{number}")
    if wrong:
        for item in wrong:
            fail(f"a non-canonical digest is labelled as the model hash ({item})")
    else:
        ok("every digest labelled as the model hash is the canonical one")


def check_links() -> None:
    link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    broken = []
    for path in tracked_markdown():
        for number, line in prose_lines(path):
            for match in link.finditer(line):
                target = match.group(1).split("#")[0].strip()
                if not target or target.startswith(("http", "mailto:", "#")):
                    continue
                if not (path.parent / target).resolve().exists():
                    broken.append(f"{path.relative_to(ROOT)}:{number}: {target}")
    if broken:
        for item in broken:
            fail(f"broken relative link ({item})")
    else:
        ok("every relative Markdown link resolves")


def check_page_counts() -> None:
    """Page-count claims, against the rendered PDFs when they exist."""
    documents = {
        "book": ROOT / "build/nobody-in-charge.pdf",
        "paper": ROOT / "paper/anonymity-as-an-aggregation-condition.pdf",
        "primer": ROOT / "reference/PRIMER-steps-and-traditions.pdf",
    }
    absent = [name for name, path in documents.items() if not path.exists()]
    if absent:
        skip(f"page-count claims (not built: {', '.join(absent)}); run the builders first")
        return
    try:
        from pypdf import PdfReader
    except ImportError:
        skip("page-count claims (pypdf not installed)")
        return
    pages = {name: len(PdfReader(str(path)).pages) for name, path in documents.items()}
    assert_claims("book page count", pages["book"], re.compile(r"book\s+(\d+)\s+pages"))
    assert_claims("book page count in 'N-page PDF'", pages["book"],
                  re.compile(r"runs to\s+(\d+)\s+pages"))
    assert_claims("primer page count", pages["primer"], re.compile(r"primer\s+(\d+)\s*$"))


def main() -> int:
    check_ci_jobs()
    check_checker_inventory()
    check_corpus()
    check_model_scripts()
    check_chapters()
    check_local_runner()
    check_model_hash()
    check_links()
    check_page_counts()

    for line in passes:
        print(line)
    for line in skips:
        print(line)
    for line in failures:
        print(line)
    tail = f"; {len(skips)} skipped" if skips else ""
    print(f"\n{len(passes)} checks passed; {len(failures)} failed{tail}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
