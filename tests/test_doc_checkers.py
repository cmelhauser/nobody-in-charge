"""Tests for `tools/check_docs.py`, `tools/check_fonts.py` and `tools/check_pdfs.py`.

Every test builds a small scratch repository under `tmp_path` in which one claim is wrong and
asserts that the matching check fails with the right message, and a twin in which the claim is
right and the check passes. Nothing here needs pandoc, tectonic, fontconfig, Git history, or a
network, and nothing is written into the repository tree: `check_docs.ROOT` is redirected to
the scratch tree, `tracked_markdown` is replaced by a glob of it, and the two places the
checkers shell out (`git`, `fc-list`, `pdftotext`, the release gate) are replaced by fakes.

The older tests in `tests/test_tools_direct.py` cover other parts of the same three tools; this
file is self-contained and does not import from it.
"""
from __future__ import annotations

import subprocess
import sys
import types
from pathlib import Path

import check_docs
import check_fonts
import check_pdfs
import pytest

pypdf = pytest.importorskip("pypdf")

# The real function, captured before the fixture below replaces it on the module.
REAL_TRACKED_MARKDOWN = check_docs.tracked_markdown

MATRIX = ("        python-version: ${{ github.event_name == 'pull_request' && "
          "fromJSON('[\"3.12\"]') || fromJSON('[\"3.11\", \"3.12\"]') }}\n")


# ============================================================================== check_docs


@pytest.fixture
def tree(tmp_path, monkeypatch):
    """Return a scratch repository root for check_docs, with fresh and empty result lists."""
    for name in ("passes", "failures", "skips"):
        monkeypatch.setattr(check_docs, name, [])
    monkeypatch.setattr(check_docs, "ROOT", tmp_path)
    monkeypatch.setattr(check_docs, "tracked_markdown",
                        lambda: sorted(tmp_path.rglob("*.md")))
    return tmp_path


def write(root: Path, rel: str, text: str = "") -> Path:
    """Create `rel` under `root` (with parents) holding `text`, and return its path."""
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def workflow(root: Path, *jobs: str) -> None:
    """Write a `ci.yml` that defines the named jobs, with the two-list Python matrix."""
    body = "name: ci\njobs:\n" + "".join(f"  {job}:\n    runs-on: x\n" for job in jobs)
    write(root, ".github/workflows/ci.yml", body + MATRIX)


def test_value_of_reads_digits_and_words():
    """value_of reads digits and spelled-out numbers, and gives None for anything else.

    Every prose count claim is converted through it, so a misread number would either drop a
    claim silently or compare the wrong figure.
    """
    assert check_docs.value_of("12") == 12
    assert check_docs.value_of(" Seven ") == 7
    assert check_docs.value_of("thirty-three") == 33
    assert check_docs.value_of("banana") is None


def test_tracked_markdown_drops_generated_output_and_the_progress_log(monkeypatch):
    """tracked_markdown keeps hand-written Markdown from the git listing.

    It must drop build output and the append-only progress log, otherwise generated text and
    history would be read as live claims.
    """
    listing = b"README.md\0build/book.md\0research/progress-log.md\0sub/A.md\0\0"
    monkeypatch.setattr(check_docs.subprocess, "run",
                        lambda *a, **k: types.SimpleNamespace(stdout=listing))
    names = [p.relative_to(check_docs.ROOT).as_posix() for p in REAL_TRACKED_MARKDOWN()]
    assert names == ["README.md", "sub/A.md"]


def test_prose_lines_skip_blockquotes_and_unreadable_files(tree):
    """prose_lines skips blockquotes and files it cannot read.

    Blockquotes quote retired claims on purpose, so reading them would flag the quotation. A
    directory or an undecodable file must give an empty list rather than an exception.
    """
    quoted = write(tree, "Q.md", "kept\n> retired claim\n   > indented retired claim\nalso kept\n")
    assert check_docs.prose_lines(quoted) == [(1, "kept"), (4, "also kept")]
    (tree / "dir.md").mkdir()
    (tree / "binary.md").write_bytes(b"\xff\xfe\x00bad")
    assert check_docs.prose_lines(tree / "dir.md") == []
    assert check_docs.prose_lines(tree / "binary.md") == []


def test_assert_claims_passes_fails_and_ignores_unreadable_numbers(tree):
    """assert_claims fails only on a readable number that disagrees with the tree.

    A word with no numeric value is not a claim. This pins the shared mechanism behind every
    count check: the failure message, the clean case and the pass message.
    """
    import re
    write(tree, "A.md", "It has three widgets and 4 widgets and many widgets.\n")
    pattern = re.compile(r"\b(\w+) widgets")
    check_docs.assert_claims("widget count", 3, pattern)
    # "4" is wrong; "three" is right; "many" has no numeric value and is not a claim.
    assert len(check_docs.failures) == 1
    assert "A.md:1: says '4', tree has 3" in check_docs.failures[0]
    check_docs.failures.clear()
    check_docs.assert_claims("widget count", 3, re.compile(r"\b(three) widgets"))
    assert check_docs.failures == []
    assert "is 3, and 1 claim(s)" in check_docs.passes[0]


# ---------------------------------------------------------------------------- the CI jobs


def test_ci_jobs_reads_column_two_keys_under_jobs(tree):
    """ci_jobs returns the keys indented two spaces under `jobs:` and nothing else.

    Comments, top-level keys and keys after the section must be ignored, or every job-count
    claim would be checked against the wrong list.
    """
    text = ("name: x\njobs:\n  lint:\n    runs-on: a\n  # a comment\n  unit-tests:\n"
            "    steps: []\n# top-level comment\nafter:\n  not_a_job:\n")
    write(tree, ".github/workflows/ci.yml", text)
    assert check_docs.ci_jobs() == ["lint", "unit-tests"]


def test_check_ci_jobs_fails_when_the_workflow_has_no_jobs(tree):
    """A workflow with no readable jobs fails with a named message.

    Without it the check would compare prose against zero jobs and could pass vacuously after
    ci.yml is broken or moved.
    """
    write(tree, ".github/workflows/ci.yml", "name: nothing\n")
    check_docs.check_ci_jobs()
    assert check_docs.failures == ["FAIL: could not read job names from .github/workflows/ci.yml"]


def test_check_ci_jobs_catches_a_miscount_and_the_both_jobs_phrasing(tree):
    """A wrong job count, in two phrasings, and 'runs both jobs' are each reported.

    The workflow has three jobs while the prose says two, four and 'both'. Each failure names
    the file and line, covering the ways prose drifts when a job is added.
    """
    workflow(tree, "lint", "unit-tests", "checkers")
    write(tree, "A.md", "GitHub Actions runs two jobs.\n"
                        "tools/run_ci_locally.sh runs all four jobs.\n"
                        "It runs both jobs.\n")
    check_docs.check_ci_jobs()
    failed = "\n".join(check_docs.failures)
    assert "continuous-integration job count (A.md:1: says 'two', tree has 3)" in failed
    assert "job count in run_ci_locally descriptions (A.md:2: says 'four', tree has 3)" in failed
    assert "'runs both jobs' but the workflow has 3 (A.md:3)" in failed


def test_check_ci_jobs_accepts_true_claims_and_both_jobs_for_two(tree):
    """True job claims pass, including 'both jobs' when there are exactly two.

    The job names quoted in backticks exist in the workflow. This guards against false positives
    that would block correct documentation.
    """
    workflow(tree, "lint", "unit-tests")
    write(tree, "A.md", "GitHub Actions runs two jobs. It runs both jobs. Job `lint` and\n"
                        "`unit-tests` and the `release` workflow.\n")
    check_docs.check_ci_jobs()
    assert check_docs.failures == []
    assert any("no prose says 'both jobs'" in line for line in check_docs.passes)
    assert any("every CI job named in prose exists: lint, unit-tests" in line
               for line in check_docs.passes)


def test_check_ci_jobs_catches_a_job_name_the_workflow_lacks(tree):
    """Prose naming a CI job the workflow does not define is a failure.

    The failure carries the location. It catches documentation that outlives a renamed or
    removed job.
    """
    workflow(tree, "lint")
    write(tree, "A.md", "Run the `documents` job.\n")
    check_docs.check_ci_jobs()
    assert any("A.md:1: names job `documents`" in line for line in check_docs.failures)


# ------------------------------------------------------------------- the checker inventory


def test_check_checker_inventory_counts_build_corpus_as_one(tree):
    """The checker count is the check_*.py files plus build_corpus.py --check.

    Two check files therefore make three checkers, and a true claim of three that names a real
    file passes. This pins the counting rule.
    """
    write(tree, "tools/check_a.py")
    write(tree, "tools/check_b.py")
    write(tree, "A.md", "There are three checkers; `check_a.py` runs first.\n")
    check_docs.check_checker_inventory()
    assert check_docs.failures == []
    assert "3 counting build_corpus.py --check" in check_docs.passes[-1]


def test_check_checker_inventory_catches_a_miscount_and_a_phantom_checker(tree):
    """A wrong checker count and a phantom check_*.py name are both reported.

    This catches prose that keeps naming a deleted or never-created checker, or whose total has
    gone stale.
    """
    write(tree, "tools/check_a.py")
    write(tree, "A.md", "We keep five checkers. See `check_ghost.py`.\n")
    check_docs.check_checker_inventory()
    failed = "\n".join(check_docs.failures)
    assert "checker count (A.md:1: says 'five', tree has 2)" in failed
    assert "prose names a checker that does not exist (A.md:1: check_ghost.py)" in failed


# --------------------------------------------------------------------------- the corpus


def corpus(root: Path) -> None:
    """Two sources, one of them record only."""
    write(root, "research/incorporated/Alpha_2000/metadata.json", '{"record_only": true}')
    write(root, "research/incorporated/Beta_2001/metadata.json", "{}")


def test_corpus_counts_reads_the_record_only_flag(tree):
    """corpus_counts returns (sources, record_only) from the metadata files.

    One of the two fixture sources sets record_only, giving (2, 1). Every corpus-size claim is
    checked against this pair.
    """
    corpus(tree)
    assert check_docs.corpus_counts() == (2, 1)


def test_check_corpus_passes_when_every_claim_matches(tree):
    """Every supported corpus phrasing that matches the tree passes.

    Four claims pass with no failures, and a 'bringing the corpus to 26' milestone is history
    and is ignored. This guards against flagging dated narrative as a stale count.
    """
    corpus(tree)
    write(tree, "A.md", "The project holds 2 sources.\nThe corpus to its present 2 is shown.\n"
                        "One sources are record only.\n"
                        "one of the 2 sources are held as record only.\n"
                        "Waypoint: bringing the corpus to 26 is history and is not read.\n")
    check_docs.check_corpus()
    assert check_docs.failures == []
    assert len(check_docs.passes) == 4


def test_check_corpus_catches_each_stale_claim(tree):
    """Each of the four corpus phrasings is reported when its number is stale.

    The source total, the 'present N' form, the record-only count and the 'N of the M' form each
    fail with the tree value. This catches numbers that go stale when a source is added.
    """
    corpus(tree)
    write(tree, "A.md", "The project holds 9 sources.\nThe corpus to its present 9 is shown.\n"
                        "Six sources are record only.\n"
                        "Six of the 9 sources are held as record only.\n")
    check_docs.check_corpus()
    failed = "\n".join(check_docs.failures)
    assert "corpus size (A.md:1: says '9', tree has 2)" in failed
    assert "corpus size in 'present N' phrasing (A.md:2" in failed
    assert "record-only count (A.md:3: says 'Six', tree has 1)" in failed
    assert "record-only count in 'N of the M sources are record only' (A.md:4" in failed


# --------------------------------------------------------- analysis scripts and chapters


def test_check_model_scripts_excludes_the_model_itself(tree):
    """The analysis-script count leaves out aa_group_model.py.

    Three files under model/ count as two scripts, so only the claim of three fails. This keeps
    the canonical model out of the tally.
    """
    for name in ("aa_group_model.py", "one.py", "two.py"):
        write(tree, f"model/{name}")
    write(tree, "A.md", "It has 2 analysis scripts.\nIt has three analysis scripts.\n")
    check_docs.check_model_scripts()
    assert len(check_docs.failures) == 1
    assert "A.md:2: says 'three', tree has 2" in check_docs.failures[0]


def test_check_chapters_counts_numbered_chapters_only(tree):
    """Only numbered chapters count; the preface and introduction do not.

    A '25-chapter' claim fails against two chapters, and the 'N chapters plus preface' phrasing
    is read separately and passes.
    """
    for name in ("ch00-preface.md", "ch00b-introduction.md", "ch01-a.md", "ch02-b.md"):
        write(tree, f"manuscript/{name}")
    write(tree, "A.md", "A 25-chapter book.\nIt has 2 chapters plus the preface.\n")
    check_docs.check_chapters()
    assert len(check_docs.failures) == 1
    assert "A.md:1: says '25', tree has 2" in check_docs.failures[0]
    assert any("chapter count in 'N chapters plus preface' is 2" in p for p in check_docs.passes)


# ----------------------------------------------------------------------- the local runner


RUNNER = """#!/usr/bin/env bash
# Usage:
#   lint        run ruff
#   checkers    run the checkers
#   {extra}
set -euo pipefail
if [ "$job" = lint ]; then :; fi
if [ "$job" = checkers ]; then :; fi
if [ "$job" = documents ]; then :; fi
if [ "$job" = all ]; then :; fi
"""


def test_check_local_runner_fails_for_an_undocumented_job_and_passes_when_documented(tree):
    """check_local_runner compares the jobs the script implements with those it documents.

    A job in the code but missing from the usage text fails, and documenting it passes. This
    stops the runner gaining a hidden job.
    """
    write(tree, "tools/run_ci_locally.sh", RUNNER.format(extra="(nothing)"))
    check_docs.check_local_runner()
    assert check_docs.failures == [
        "FAIL: tools/run_ci_locally.sh implements a job its usage does not document: documents"]

    check_docs.failures.clear()
    write(tree, "tools/run_ci_locally.sh", RUNNER.format(extra="documents   render the PDFs"))
    check_docs.check_local_runner()
    assert check_docs.failures == []
    assert "checkers, documents, lint" in check_docs.passes[0]


# ------------------------------------------------------------------------- the model hash


def test_check_model_hash_reads_the_label_on_the_line_or_above(tree):
    """A non-canonical digest fails only when it is labelled as the model hash.

    The label may be on the same line or on the line above. Digests with another label, or none,
    are left alone, so other hashes do not raise false alarms.
    """
    wrong, other = "a" * 64, "b" * 64
    write(tree, "A.md", "\n".join([
        f"Model hash: `{wrong}`",                     # labelled the model, not canonical
        f"Analysis script hash: `{other}`",           # labelled as something else: fine
        f"Model SHA-256: `{check_docs.CANONICAL_MODEL}`",   # canonical: fine
        "",
        "The model hash is",
        "",
        f"`{wrong}`",                                 # label comes from the line above
        "",
        f"`{other}`",                                 # no label anywhere above: fine
    ]) + "\n")
    check_docs.check_model_hash()
    assert check_docs.failures == [
        "FAIL: a non-canonical digest is labelled as the model hash (A.md:1)",
        "FAIL: a non-canonical digest is labelled as the model hash (A.md:7)",
    ]


def test_check_model_hash_passes_when_nothing_is_mislabelled(tree):
    """A document quoting only the canonical model digest passes.

    It records no failure and exactly one pass, confirming that correct documentation is not
    flagged.
    """
    write(tree, "A.md", f"Model: {check_docs.CANONICAL_MODEL}\n")
    check_docs.check_model_hash()
    assert check_docs.failures == [] and len(check_docs.passes) == 1


# ------------------------------------------------------------------------------- links


def test_check_links_flags_only_broken_relative_links(tree):
    """Only a relative link whose target file is missing is a failure.

    Existing files, fragments, web and mailto URLs and in-page anchors are ignored, so valid
    references do not raise false alarms.
    """
    write(tree, "exists.md")
    write(tree, "sub/B.md", "[up](../exists.md#section)\n")
    write(tree, "A.md", "[ok](exists.md) [frag](exists.md#h) [web](https://x.org) "
                        "[mail](mailto:a@b.c) [self](#top) [bad](gone.md)\n")
    check_docs.check_links()
    assert check_docs.failures == ["FAIL: broken relative link (A.md:1: gone.md)"]


def test_check_links_passes_when_every_link_resolves(tree):
    """When every relative link resolves, check_links passes.

    It records no failure and a pass saying so, which pins the success path a clean repository
    takes.
    """
    write(tree, "exists.md")
    write(tree, "A.md", "[ok](exists.md)\n")
    check_docs.check_links()
    assert check_docs.failures == [] and "resolves" in check_docs.passes[0]


# --------------------------------------------------------------------- release gate totals


def completed(stdout: str, returncode: int = 0):
    """Build a CompletedProcess with the given stdout and return code.

    It stands in for the result of a mocked subprocess.run call.
    """
    return subprocess.CompletedProcess([], returncode, stdout=stdout, stderr="")


def test_release_gate_totals_adds_failures_back_in(monkeypatch):
    """release_gate_totals reads the gate's summary line and adds failures back in.

    Ten passed and two failed means twelve checks run, and three skipped makes fifteen in all.
    The gate exits nonzero here and its output must still be parsed.
    """
    out = "noise\n10 checks passed; 2 failed; 3 skipped\n"
    monkeypatch.setattr(check_docs.subprocess, "run", lambda *a, **k: completed(out, 1))
    assert check_docs.release_gate_totals() == {"run": 12, "skipped": 3, "full": 15}


@pytest.mark.parametrize("stdout", [
    "no summary line at all\n",
    "10 checks passed; 0 failed; 3 skipped\nFAIL: cache exists: x\n",
    "10 checks passed; 0 failed; 3 skipped\nx is not valid JSON\n",
])
def test_release_gate_totals_is_none_when_the_gate_ran_short(monkeypatch, stdout):
    """release_gate_totals gives None when the gate output shows it did not run fully.

    No summary line, a missing cache or an invalid JSON file all count. This stops an incomplete
    run from setting the counts prose is held to.
    """
    monkeypatch.setattr(check_docs.subprocess, "run", lambda *a, **k: completed(stdout))
    assert check_docs.release_gate_totals() is None


def test_gate_claims_ignore_reported_speech_and_unreadable_numbers():
    """gate_claims_contradicting ignores reported speech and numbers it cannot read.

    Only the wrong total is returned, and the count of claims seen excludes the superseded
    wording and the non-number, so quoting an old figure does not fail.
    """
    totals = {"run": 10, "skipped": 3, "full": 13}
    lines = [
        ("a:1", "which runs 10 of the 13 release checks"),            # right
        ("a:2", "which runs 10 of the 14 release checks"),            # wrong total
        ("a:3", "the old text said omits seven checks; it omits three"),   # reported speech
        ("a:4", "the gate omits plenty checks"),                      # not a number
    ]
    wrong, seen = check_docs.gate_claims_contradicting(totals, lines)
    assert seen == 2 and len(wrong) == 1 and wrong[0].startswith("a:2:")


def test_check_release_gate_counts_skips_when_the_totals_are_unavailable(tree, monkeypatch):
    """The gate-count check skips, rather than fails, when the totals are unavailable.

    A missing gate result is an environmental gap and not a documentation error.
    """
    monkeypatch.setattr(check_docs, "release_gate_totals", lambda: None)
    check_docs.check_release_gate_counts()
    assert check_docs.failures == [] and "release gate's totals" in check_docs.skips[0]


def test_check_release_gate_counts_reads_markdown_workflows_and_the_gate_source(
        tree, monkeypatch):
    """Gate-count claims are read from Markdown, the workflow and the gate's own source.

    A consistent set passes, and a Markdown claim of nine against thirteen then fails with its
    location, so no place that quotes the figures escapes.
    """
    monkeypatch.setattr(check_docs, "release_gate_totals",
                        lambda: {"run": 10, "skipped": 3, "full": 13})
    write(tree, "tools/check_release.py", "# the same 13 checks\n")
    write(tree, ".github/workflows/ci.yml", "# `--skip-artifacts` omits three checks\n")
    write(tree, "A.md", "which runs 10 of the 13 release checks\n")
    check_docs.check_release_gate_counts()
    assert check_docs.failures == []
    assert "10 checks under --skip-artifacts and skips 3, 13 in all, and 3 claim(s)" \
        in check_docs.passes[0]

    write(tree, "B.md", "which runs 9 of the 13 release checks\n")
    check_docs.passes.clear()
    check_docs.check_release_gate_counts()
    assert any("B.md:1" in f and "gives 9 checks run" in f for f in check_docs.failures)


# ------------------------------------------------------------------------ Python versions


def test_check_python_versions_flags_a_wrong_list(tree):
    """A Python version list that differs from the workflow matrix is a failure.

    Only the wrong list in A.md fails. CHANGELOG.md is history and is never read, and the pull-
    request '3.12 only' sentence is not mistaken for a list.
    """
    workflow(tree, "lint")
    write(tree, "CHANGELOG.md", "Python 3.9 and 3.10 once.\n")       # history: never read
    write(tree, "A.md", "CI runs Python 3.11, 3.12 and 3.13.\n\nOn pulls Python 3.12 only.\n")
    check_docs.check_python_versions()
    assert len(check_docs.failures) == 1
    assert "A.md:1: says 3.11, 3.12, 3.13, the matrix runs 3.11, 3.12" in check_docs.failures[0]


# ------------------------------------------------------------------------- page counts


def blank_pdf(path: Path, pages: int) -> None:
    """Write a PDF of `pages` blank A4 pages."""
    path.parent.mkdir(parents=True, exist_ok=True)
    writer = pypdf.PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=595.276, height=841.89)
    with path.open("wb") as handle:
        writer.write(handle)


def three_pdfs(root: Path, book: int = 3, paper: int = 2, primer: int = 1) -> None:
    """Write the three rendered documents at the paths check_page_counts expects."""
    blank_pdf(root / "build/nobody-in-charge.pdf", book)
    blank_pdf(root / "paper/anonymity-as-an-aggregation-condition.pdf", paper)
    blank_pdf(root / "reference/PRIMER-steps-and-traditions.pdf", primer)


def test_check_page_counts_skips_naming_the_unbuilt_documents(tree):
    """check_page_counts skips, naming the documents, when some PDFs are not built.

    A fresh clone without renders therefore cannot fail on page numbers.
    """
    blank_pdf(tree / "build/nobody-in-charge.pdf", 1)
    check_docs.check_page_counts()
    assert check_docs.failures == []
    assert "not built: paper, primer" in check_docs.skips[0]


def test_check_page_counts_skips_without_pypdf(tree, monkeypatch):
    """check_page_counts skips with an explicit message when pypdf cannot be imported.

    Setting sys.modules['pypdf'] to None forces the import to fail. The dependency is optional,
    so its absence must not raise or fail the check.
    """
    three_pdfs(tree)
    monkeypatch.setitem(sys.modules, "pypdf", None)             # makes `import pypdf` fail
    check_docs.check_page_counts()
    assert check_docs.skips == ["SKIP: page-count claims (pypdf not installed)"]


def test_check_page_counts_compares_every_claim_with_the_rendered_page_count(tree):
    """Each page-count phrasing is compared with the PDF's real page count.

    Five true claims pass, and a further claim of nine pages for a three-page book fails with
    the tree value. This catches prose that drifts from the render.
    """
    three_pdfs(tree)
    write(tree, "A.md", "The book 3 pages long.\nIt runs to 3 pages.\n"
                        "paper 2, primer 1\n"
                        "`x.tex`, 2 pages\n")
    check_docs.check_page_counts()
    assert check_docs.failures == [] and len(check_docs.passes) == 5

    write(tree, "B.md", "The book 9 pages long.\n")
    check_docs.check_page_counts()
    assert any("B.md:1: says '9', tree has 3" in f for f in check_docs.failures)


# ------------------------------------------------------------------------ paper decimals


def test_check_paper_decimals_skips_without_the_stored_output(tree):
    """check_paper_decimals skips when the notebook or its stored output is missing.

    It records one skip for no notebook and a second for a notebook without the decimals line. A
    figure that cannot be read cannot be compared, so this must not fail.
    """
    check_docs.check_paper_decimals()
    assert len(check_docs.skips) == 1
    write(tree, "paper/anonymity-as-an-aggregation-condition.ipynb", "{}")
    check_docs.check_paper_decimals()
    assert len(check_docs.skips) == 2


def test_check_paper_decimals_holds_the_quoted_figure_to_the_notebook(tree):
    """The decimals figure quoted in AGENT_VERIFY.md must equal the notebook's.

    With the notebook printing 4, a line saying 4 passes and one saying 5 fails, keeping the
    verifier's expectation tied to the output.
    """
    write(tree, "paper/anonymity-as-an-aggregation-condition.ipynb",
          '{"text": "decimals printed in the paper: 4"}')
    write(tree, "AGENT_VERIFY.md", "currently 4 of them\ncurrently 5 of them\n")
    check_docs.check_paper_decimals()
    assert len(check_docs.failures) == 1
    assert "AGENT_VERIFY.md:2: says '5', tree has 4" in check_docs.failures[0]


# ------------------------------------------------------------------ the declared dates


class FakeGit:
    """Stands in for `subprocess.run` in the date checks.

    `shallow` answers the shallow-clone question; `stamp` is the date of the last change to
    any source ("" for no history); `log_fails` makes `git log` exit non-zero.
    """

    def __init__(self, stamp="2026-01-01", shallow=False, log_fails=False):
        """Set what the fake repository will answer."""
        self.stamp, self.shallow, self.log_fails = stamp, shallow, log_fails

    def __call__(self, cmd, **kwargs):
        """Answer `rev-parse` with the shallow flag and anything else as `git log`."""
        if "rev-parse" in cmd:
            return completed("true\n" if self.shallow else "false\n")
        return completed(self.stamp + "\n", 1 if self.log_fails else 0)


def dated_tree(root: Path, book_date="1 January 2026", primer_date="2 February 2026",
               paper_date="January 2026") -> None:
    """Build a tree in which every declared date agrees with its artifact."""
    write(root, "tools/build_book.py", f"DRAFT_DATE = '{book_date}'\n")
    write(root, "tools/build_primer.py", f"REVISED_DATE = '{primer_date}'\n")
    write(root, "build/nobody-in-charge.md", f'---\ndate: "Draft of {book_date}"\n---\n')
    (root / "reference").mkdir(exist_ok=True)
    (root / "reference/PRIMER-steps-and-traditions.pdf").write_bytes(b"%PDF placeholder")
    write(root, "paper/anonymity-as-an-aggregation-condition.tex",
          f"\\date{{\\normalsize {paper_date} (draft)}}\n")


@pytest.fixture
def primer_text(monkeypatch):
    """Make pypdf's reader return controllable first-page text for the primer."""
    state = {"text": "Revised 2 February 2026"}

    class Reader:
        def __init__(self, _path):
            self.pages = [types.SimpleNamespace(extract_text=lambda: state["text"])]

    monkeypatch.setattr(pypdf, "PdfReader", Reader)
    return state


def test_check_document_dates_passes_when_text_artifacts_and_history_agree(
        tree, monkeypatch, primer_text):
    """Declared dates that agree with their artifacts and Git history all pass.

    The book, primer and paper checks produce no failure and no skip. This is the baseline the
    failing variants depart from.
    """
    dated_tree(tree)
    monkeypatch.setattr(check_docs.subprocess, "run", FakeGit("2026-01-01"))
    check_docs.check_document_dates()
    assert check_docs.failures == [] and check_docs.skips == []
    joined = "\n".join(check_docs.passes)
    assert "the assembled book carries the declared draft date, 1 January 2026" in joined
    assert "the rendered primer carries the declared revision date, 2 February 2026" in joined
    assert "the paper's date January 2026 is not older" in joined


def test_check_document_dates_fails_when_sources_changed_after_the_declared_date(
        tree, monkeypatch, primer_text):
    """A source changed after a declared date fails the book, primer and paper checks.

    Each failure names the change date from Git, so a document cannot keep an old date after its
    sources move.
    """
    dated_tree(tree)
    monkeypatch.setattr(check_docs.subprocess, "run", FakeGit("2026-12-01"))
    check_docs.check_document_dates()
    failed = "\n".join(check_docs.failures)
    assert "the sources for the book's draft date changed on 2026-12-01" in failed
    assert "the sources for the primer's revision date changed on 2026-12-01" in failed
    assert "the sources for the paper's date changed on 2026-12-01" in failed


def test_check_document_dates_skips_the_history_comparison_when_it_cannot_be_made(
        tree, monkeypatch, primer_text):
    """The history comparison skips, and does not fail, when Git cannot answer.

    A shallow clone, a failing git log and an empty history each give three skips with the
    reason. Missing history is an environmental limit, not a stale date.
    """
    dated_tree(tree)
    monkeypatch.setattr(check_docs.subprocess, "run", FakeGit(shallow=True))
    check_docs.check_document_dates()
    assert check_docs.failures == [] and len(check_docs.skips) == 3
    assert all("shallow clone" in s for s in check_docs.skips)

    check_docs.skips.clear()
    monkeypatch.setattr(check_docs.subprocess, "run", FakeGit(log_fails=True))
    check_docs.check_document_dates()
    assert len(check_docs.skips) == 3 and all("no Git history" in s for s in check_docs.skips)

    check_docs.skips.clear()
    monkeypatch.setattr(check_docs.subprocess, "run", FakeGit(stamp=""))
    check_docs.check_document_dates()
    assert len(check_docs.skips) == 3


def test_check_document_dates_reports_a_stale_or_unbuilt_book(tree, monkeypatch, primer_text):
    """The assembled book fails if dated wrongly or undated, and skips if it is not built.

    These are the three states of that artifact, each with its own message.
    """
    dated_tree(tree)
    monkeypatch.setattr(check_docs.subprocess, "run", FakeGit("2026-01-01"))
    write(tree, "build/nobody-in-charge.md", 'date: "Draft of 3 March 2025"\n')
    check_docs.check_document_dates()
    assert any("is dated 3 March 2025 and tools/build_book.py declares 1 January 2026"
               in f for f in check_docs.failures)

    check_docs.failures.clear()
    write(tree, "build/nobody-in-charge.md", "no header at all\n")
    check_docs.check_document_dates()
    assert any("is dated nothing" in f for f in check_docs.failures)

    check_docs.failures.clear()
    (tree / "build/nobody-in-charge.md").unlink()
    check_docs.check_document_dates()
    assert any("build/nobody-in-charge.md is not built" in s for s in check_docs.skips)


def test_check_document_dates_reports_an_unreadable_primer(tree, monkeypatch, primer_text):
    """A primer without its declared date fails; an unreadable one skips.

    A wrong 'Revised' date on the first page fails, a missing pypdf skips and a missing PDF
    skips as not built. The check fails when it can read a wrong date and skips when it cannot
    read at all.
    """
    dated_tree(tree)
    monkeypatch.setattr(check_docs.subprocess, "run", FakeGit("2026-01-01"))
    primer_text["text"] = "Revised 9 September 2020"
    check_docs.check_document_dates()
    assert any("does not print 'Revised 2 February 2026'" in f for f in check_docs.failures)

    check_docs.failures.clear()
    monkeypatch.setitem(sys.modules, "pypdf", None)
    check_docs.check_document_dates()
    assert any("pypdf not installed" in s for s in check_docs.skips)

    check_docs.skips.clear()
    (tree / "reference/PRIMER-steps-and-traditions.pdf").unlink()
    check_docs.check_document_dates()
    assert any("the PDF is not built" in s for s in check_docs.skips)


def test_check_document_dates_reports_declarations_it_cannot_read(
        tree, monkeypatch, primer_text):
    """An unreadable date declaration is a failure, never a pass.

    A missing DRAFT_DATE, an unparseable REVISED_DATE and a paper date macro without a month each
    fail with their own message.
    """
    dated_tree(tree)
    monkeypatch.setattr(check_docs.subprocess, "run", FakeGit("2026-01-01"))
    write(tree, "tools/build_book.py", "# no declaration\n")
    write(tree, "tools/build_primer.py", "REVISED_DATE = 'sometime soon'\n")
    write(tree, "paper/anonymity-as-an-aggregation-condition.tex", "\\date{unreadable}\n")
    check_docs.check_document_dates()
    failed = "\n".join(check_docs.failures)
    assert "tools/build_book.py declares no DRAFT_DATE" in failed
    assert "REVISED_DATE in tools/build_primer.py is not a date this checker can read" in failed
    assert "the paper's \\date no longer names a month" in failed


# --------------------------------------------------------------------- the handoff date


def test_check_handoff_date_enforces_the_handoffs_own_staleness_rule(tree):
    """HANDOFF.md must be dated no earlier than the newest progress-log entry.

    An equal date passes, and a handoff dated 5 March against a 6 March entry fails, quoting the
    log date as the handoff's own rule requires.
    """
    write(tree, "research/progress-log.md", "## 4 March 2026\n\n### 6 March 2026\n\ntext\n")
    write(tree, "HANDOFF.md", "Last updated 6 March 2026\n")
    check_docs.check_handoff_date()
    assert check_docs.failures == []
    assert "HANDOFF.md is dated 6 March 2026" in check_docs.passes[0]

    write(tree, "HANDOFF.md", "Last updated 5 March 2026\n")
    check_docs.check_handoff_date()
    assert "by its own rule the handoff is stale" in check_docs.failures[0]
    assert "06 March 2026" in check_docs.failures[0]


def test_check_handoff_date_fails_without_a_date_on_either_side(tree):
    """A missing date on either side of the handoff comparison is a failure.

    A progress log with no dated entry and a HANDOFF.md with no 'Last updated' date each fail,
    since a staleness test missing one side must not pass by default.
    """
    write(tree, "research/progress-log.md", "no dated entry\n")
    write(tree, "HANDOFF.md", "Last updated 5 March 2026\n")
    check_docs.check_handoff_date()
    write(tree, "research/progress-log.md", "## 4 March 2026\n")
    write(tree, "HANDOFF.md", "undated\n")
    check_docs.check_handoff_date()
    assert len(check_docs.failures) == 2
    assert all("no 'Last updated' date" in f for f in check_docs.failures)


# ------------------------------------------------------------------ own total and notebooks


def test_check_own_total_counts_itself(tree):
    """check_own_total counts itself in the total it compares.

    One check already ran, so with this one the total is 2 and matches HANDOFF.md. It pins the
    off-by-one that omitting the check's own pass would cause.
    """
    write(tree, "HANDOFF.md", "| `tools/check_docs.py` | 2 checks, 0 failed |\n")
    check_docs.passes.append("OK: one")                           # one ran, and this is a second
    check_docs.check_own_total()
    assert check_docs.failures == [] and "has 2 checks, as HANDOFF.md:1" in check_docs.passes[-1]


def test_check_notebook_assertions_counts_printed_output_not_source(tree):
    """Notebook assertions are counted from printed output, not from source code.

    The cell's source has a print call, but only the OK and FAIL lines in its output count,
    giving three. Only the paper claim of nine fails.
    """
    import json
    cell = {"source": ["print('  OK ', '  FAIL')"],
            "outputs": [{"text": ["  OK a\n", "  OK b\n", "  FAIL c\n"]}, {"data": {}}]}
    notebook = json.dumps({"cells": [cell]})
    write(tree, "model/book-calculations.ipynb", notebook)
    write(tree, "paper/anonymity-as-an-aggregation-condition.ipynb", notebook)
    write(tree, "HANDOFF.md",
          "| `model/book-calculations.ipynb` | 4 cells, 3 assertions |\n"
          "The paper notebook runs 4 and 9\n")
    check_docs.check_notebook_assertions()
    assert len(check_docs.failures) == 1
    assert "paper notebook assertion count (HANDOFF.md:2: says '9', tree has 3)" \
        in check_docs.failures[0]


# ------------------------------------------------------------------------------- main


CHECKS = ["check_ci_jobs", "check_checker_inventory", "check_corpus", "check_model_scripts",
          "check_chapters", "check_local_runner", "check_model_hash", "check_links",
          "check_release_gate_counts", "check_python_versions", "check_page_counts",
          "check_paper_decimals", "check_notebook_assertions", "check_document_dates",
          "check_handoff_date", "check_own_total"]


def test_main_runs_every_check_in_order_and_reports_a_clean_run(tree, monkeypatch, capsys):
    """Running main calls every registered check in a fixed order and exits 0 when none fail.

    The summary has no 'skipped' clause when nothing was skipped. This pins the check list and
    the clean-run status.
    """
    order = []
    for name in CHECKS:
        monkeypatch.setattr(check_docs, name, lambda name=name: order.append(name))
    check_docs.passes.append("OK: fine")
    assert check_docs.main() == 0
    assert order == CHECKS
    out = capsys.readouterr().out
    assert "OK: fine" in out and "1 checks passed; 0 failed\n" in out
    assert "skipped" not in out


def test_main_exits_one_and_prints_skips_before_failures(tree, monkeypatch, capsys):
    """Running main exits 1 on any failure and prints passes, then skips, then failures.

    The summary reports all three counts, and the order leaves the failures nearest the prompt.
    """
    for name in CHECKS:
        monkeypatch.setattr(check_docs, name, lambda: None)
    check_docs.passes.append("OK: fine")
    check_docs.skips.append("SKIP: could not run")
    check_docs.failures.append("FAIL: wrong")
    assert check_docs.main() == 1
    out = capsys.readouterr().out
    assert out.index("OK: fine") < out.index("SKIP: could not run") < out.index("FAIL: wrong")
    assert "1 checks passed; 1 failed; 1 skipped" in out


# ============================================================================ check_fonts


def test_check_fonts_digest_is_the_sha256_of_the_file(tmp_path):
    """check_fonts.digest returns the SHA-256 of the file's bytes.

    The known digest of b'abc' fixes it. The pinned-font comparison means nothing if this hash
    is wrong.
    """
    path = tmp_path / "f.otf"
    path.write_bytes(b"abc")
    assert check_fonts.digest(path) == (
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")


def test_check_fonts_locate_prefers_the_direct_hit_and_searches_subdirectories(tmp_path):
    """The locate function finds a font by name regardless of case, searching subdirectories.

    A file directly in the directory wins over a nested one, and an absent font gives None. A
    wrong pick would hash the wrong file.
    """
    name = "texgyrepagella-bold.otf"
    nested = tmp_path / "deep" / "er"
    nested.mkdir(parents=True)
    (nested / "TeXGyrePagella-Bold.otf").write_bytes(b"x")
    assert check_fonts.locate(name, [tmp_path]) == nested / "TeXGyrePagella-Bold.otf"
    (tmp_path / name).write_bytes(b"y")
    assert check_fonts.locate(name, [tmp_path]) == tmp_path / name
    assert check_fonts.locate("texgyrepagella-italic.otf", [tmp_path]) is None


def test_check_fonts_candidate_dirs_without_fontconfig_uses_the_usual_places(
        tmp_path, monkeypatch):
    """Without fc-list, candidate_dirs falls back to the usual font directories.

    These are the XDG data directory and the macOS Library fonts. Absent directories are dropped
    and XDG_DATA_HOME counts only while set, so a Mac without fontconfig still finds its fonts.
    """
    home = tmp_path / "home"
    xdg = tmp_path / "xdg"
    (home / "Library" / "Fonts").mkdir(parents=True)
    (xdg / "fonts").mkdir(parents=True)
    monkeypatch.setattr(check_fonts.shutil, "which", lambda _name: None)
    monkeypatch.setattr(check_fonts.Path, "home", classmethod(lambda cls: home))
    monkeypatch.setenv("XDG_DATA_HOME", str(xdg))
    dirs = check_fonts.candidate_dirs()
    assert xdg / "fonts" in dirs and home / "Library" / "Fonts" in dirs
    assert home / ".local" / "share" / "fonts" not in dirs        # absent directories are dropped

    monkeypatch.delenv("XDG_DATA_HOME")
    assert xdg / "fonts" not in check_fonts.candidate_dirs()


def test_check_fonts_candidate_dirs_lists_each_fontconfig_directory_once(
        tmp_path, monkeypatch):
    """With fc-list, candidate_dirs keeps each Pagella font directory exactly once.

    A directory listed for two Pagella files appears once, and one holding only unrelated fonts
    is left out, so the search neither repeats nor wanders.
    """
    first, second = tmp_path / "a", tmp_path / "b"
    first.mkdir()
    second.mkdir()
    listing = (f"{first}/TeXGyrePagella-Regular.otf: \n{first}/texgyrepagella-bold.otf:\n"
               f"{second}/unrelated.otf:\n\n")
    monkeypatch.setattr(check_fonts.shutil, "which", lambda _name: "/usr/bin/fc-list")
    monkeypatch.setattr(check_fonts.subprocess, "run", lambda *a, **k: completed(listing))
    monkeypatch.setattr(check_fonts.Path, "home", classmethod(lambda cls: tmp_path / "none"))
    monkeypatch.delenv("XDG_DATA_HOME", raising=False)
    found = check_fonts.candidate_dirs()
    assert found.count(first) == 1 and second not in found


def test_check_fonts_main_scans_the_default_directories_when_no_dir_is_given(
        monkeypatch, capsys):
    """Without --dir, main scans candidate_dirs and reports each missing font.

    With nothing found it prints MISSING for all four and exits 0, or 1 under --strict with the
    install-step message. Strictness turns a report into a gate.
    """
    monkeypatch.setattr(check_fonts, "candidate_dirs", lambda: [])
    assert check_fonts.main([]) == 0
    out = capsys.readouterr().out
    assert out.count("MISSING") == 4 and "not found in any known directory" in out
    assert check_fonts.main(["--strict"]) == 1
    assert "font download or install step failed" in capsys.readouterr().out


def test_check_fonts_main_reports_success_when_every_file_matches(
        tmp_path, monkeypatch, capsys):
    """Running main with --strict succeeds when all four font files match their pins.

    It returns 0 and says all four match CI's, the path a correctly provisioned machine takes.
    """
    import hashlib
    for name in check_fonts.PINS:
        (tmp_path / name).write_bytes(b"font")
    monkeypatch.setattr(check_fonts, "PINS", {
        name: hashlib.sha256(b"font").hexdigest() for name in check_fonts.PINS})
    assert check_fonts.main(["--strict", "--dir", str(tmp_path)]) == 0
    assert "all 4 font files match CI's" in capsys.readouterr().out


# ============================================================================ check_pdfs


@pytest.fixture
def pdf_state(monkeypatch):
    """Fresh result lists for check_pdfs, with the repository root pointed at a scratch tree."""
    for name in ("failures", "notes", "skips"):
        monkeypatch.setattr(check_pdfs, name, [])
    monkeypatch.setattr(check_pdfs.shutil, "which", lambda _name: None)   # no poppler


def pdf_with_font(path: Path, font_descriptor, pages: int = 1) -> None:
    """Write a PDF whose pages all reference one font; None omits the glyph program."""
    from pypdf.generic import DictionaryObject, NameObject

    writer = pypdf.PdfWriter()
    font = DictionaryObject({NameObject("/Type"): NameObject("/Font"),
                             NameObject("/Subtype"): NameObject("/Type1"),
                             NameObject("/BaseFont"): NameObject("/Helvetica")})
    if font_descriptor is not None:
        descriptor = DictionaryObject({NameObject("/FontFile"): writer._add_object(
            DictionaryObject())})
        font[NameObject("/FontDescriptor")] = writer._add_object(descriptor)
    fonts = DictionaryObject({NameObject("/F1"): writer._add_object(font)})
    for _ in range(pages):
        page = writer.add_blank_page(width=595.276, height=841.89)
        page[NameObject("/Resources")] = DictionaryObject({NameObject("/Font"): fonts})
    with path.open("wb") as handle:
        writer.write(handle)


def test_check_pdfs_flags_an_unembedded_font_and_accepts_an_embedded_one(
        pdf_state, monkeypatch, tmp_path):
    """check_pdfs fails a PDF with a font that has no embedded glyph program.

    The failure names the font, while a PDF whose font is embedded is noted as all embedded. An
    unembedded font would render differently on another machine.
    """
    pdf_with_font(tmp_path / "bare.pdf", None)
    pdf_with_font(tmp_path / "full.pdf", True)
    monkeypatch.setattr(check_pdfs, "ROOT", tmp_path)

    check_pdfs.check("bare.pdf", 1)
    assert any("not embedded: /Helvetica" in f for f in check_pdfs.failures)

    for name in ("failures", "notes", "skips"):
        getattr(check_pdfs, name).clear()
    check_pdfs.check("full.pdf", 1)
    assert any("all 1 fonts embedded" in n and "not embedded" not in n
               for n in check_pdfs.notes)


def test_check_pdfs_counts_a_font_shared_by_several_pages_once(pdf_state, monkeypatch, tmp_path):
    """A font used on every page of a two-page PDF is counted once.

    Without deduplication the embedded-font report would grow with the page count.
    """
    pdf_with_font(tmp_path / "two.pdf", True, pages=2)
    monkeypatch.setattr(check_pdfs, "ROOT", tmp_path)
    check_pdfs.check("two.pdf", 2)
    assert any("all 1 fonts embedded" in n for n in check_pdfs.notes)


def test_check_pdfs_reports_a_file_that_is_not_a_pdf(pdf_state, monkeypatch, tmp_path):
    """A file that is not a PDF gives one 'parses as a PDF' failure, not an exception.

    A corrupt render therefore produces a readable failure instead of a traceback.
    """
    (tmp_path / "bad.pdf").write_bytes(b"this is not a pdf" * 100)
    monkeypatch.setattr(check_pdfs, "ROOT", tmp_path)
    check_pdfs.check("bad.pdf", 1)
    assert len(check_pdfs.failures) == 1
    assert check_pdfs.failures[0].startswith("FAIL: bad.pdf: parses as a PDF (")


def test_check_pdfs_reports_a_withheld_name_in_the_rendered_text(
        pdf_state, monkeypatch, tmp_path):
    """check_pdfs fails a PDF whose text prints a name the project withholds.

    prints_withheld is forced to True, and the 'prints no name' check fails. This is the last
    defence for a name the repository undertakes never to print.
    """
    pdf_with_font(tmp_path / "full.pdf", True)
    monkeypatch.setattr(check_pdfs, "ROOT", tmp_path)
    monkeypatch.setattr(check_pdfs, "prints_withheld", lambda _text: True)
    check_pdfs.check("full.pdf", 1)
    assert any("prints no name the project has undertaken to withhold" in f
               for f in check_pdfs.failures)


def test_check_pdfs_main_checks_every_registered_document(pdf_state, monkeypatch, tmp_path, capsys):
    """Running main checks every registered document, so a missing one fails the run.

    two.pdf does not exist, giving exit 1, while one.pdf passes. With no poppler, the ink
    measurement is skipped, not failed.
    """
    pdf_with_font(tmp_path / "one.pdf", True)
    monkeypatch.setattr(check_pdfs, "ROOT", tmp_path)
    monkeypatch.setattr(check_pdfs, "DOCUMENTS", {"one.pdf": 1, "two.pdf": 1})
    assert check_pdfs.main() == 1                                # two.pdf does not exist
    out = capsys.readouterr().out
    assert "FAIL: two.pdf: exists" in out and "OK: one.pdf: parses as a PDF" in out
    assert "SKIP: one.pdf: ink measurement needs poppler" in out


def test_check_pdfs_embedded_looks_for_a_glyph_program_on_the_font_or_its_descendant():
    """The embedded function looks for a glyph program on the font or on its descendant font.

    A FontFile2 on the font and a FontFile3 on a composite font's descendant count. A descriptor
    with no font file, or an empty font, does not.
    """
    class Obj(dict):
        """A dict that answers get_object() with itself, like a pypdf indirect reference."""

        def get_object(self):
            return self

    plain = Obj({"/FontDescriptor": Obj({"/FontFile2": 1})})
    bare = Obj({"/FontDescriptor": Obj({"/FontName": "x"})})
    composite = Obj({"/DescendantFonts": [Obj({"/FontDescriptor": Obj({"/FontFile3": 1})})]})
    assert check_pdfs.embedded(plain) and check_pdfs.embedded(composite)
    assert not check_pdfs.embedded(bare) and not check_pdfs.embedded(Obj({}))


def test_check_pdfs_ink_check_measures_pdftotext_boxes(pdf_state, monkeypatch):
    """check_ink measures how close pdftotext's word boxes come to the paper edge.

    A page with no words is ignored, and pages whose ink is too near the left or right edge are
    listed, here pages 2 and 3. It catches clipped text that overfull warnings miss.
    """
    def boxes(*extents):
        pages = "".join(f'<page><word xMin="{lo}" xMax="{hi}"/></page>' for lo, hi in extents)
        return completed(pages + "<page></page>")        # the last page has no words at all

    monkeypatch.setattr(check_pdfs.shutil, "which", lambda _name: "/usr/bin/pdftotext")
    monkeypatch.setattr(check_pdfs.subprocess, "run", lambda *a, **k: boxes((72, 500)))
    check_pdfs.check_ink(Path("x.pdf"), "x.pdf")
    assert check_pdfs.notes and not check_pdfs.failures

    monkeypatch.setattr(check_pdfs.subprocess, "run",
                        lambda *a, **k: boxes((72, 500), (5, 510), (72, 590)))
    check_pdfs.check_ink(Path("x.pdf"), "x.pdf")
    assert "breached on pages [2, 3]" in check_pdfs.failures[0]


def test_check_pdfs_main_names_the_missing_dependency(monkeypatch):
    """Running main exits with a message naming pypdf when it cannot be imported.

    The cause is stated plainly instead of appearing as a traceback.
    """
    monkeypatch.setitem(sys.modules, "pypdf", None)
    with pytest.raises(SystemExit) as stop:
        check_pdfs.main()
    assert "pypdf is required" in str(stop.value)


def test_check_fonts_reports_mismatches_missing_files_and_bad_arguments(tmp_path, capsys):
    """The compare function reports MISMATCH and MISSING; main handles bad arguments.

    A report-only run exits 0, --strict exits 1 and tells the reader to update PINS
    deliberately, and a --dir with no directory exits with a clear message.
    """
    (tmp_path / "texgyrepagella-regular.otf").write_bytes(b"not the pinned font")
    good, bad = check_fonts.compare([tmp_path])
    assert good == [] and bad[0].startswith("MISMATCH texgyrepagella-regular.otf")
    assert bad[1].startswith("MISSING texgyrepagella-bold.otf")

    assert check_fonts.main(["--dir", str(tmp_path)]) == 0           # report only
    assert check_fonts.main(["--strict", "--dir", str(tmp_path)]) == 1
    assert "update PINS deliberately" in capsys.readouterr().out
    for argv in (["--dir"], ["--dir", "--strict"]):
        with pytest.raises(SystemExit) as stop:
            check_fonts.main(argv)
        assert "--dir needs a directory" in str(stop.value)


def test_check_docs_python_version_helpers_and_failure_paths(tree):
    """The Python-version helpers and failure paths behave as documented.

    ci_python_versions gives None for matrices it cannot read, and python_version_claims ignores
    a version outside a Python context. A workflow lacking the two-list line fails, and a
    correct pair passes.
    """
    assert check_docs.ci_python_versions("python-version: ${{ matrix.x }}\n") is None
    assert check_docs.ci_python_versions(
        "python-version: ${{ fromJSON('[\"3.12\"]') }}\n") is None
    assert check_docs.python_version_claims("3.12 only, in a paragraph about something else") == []
    assert check_docs.python_version_claims("Python 3.11, 3.12 and 3.13") == [
        ("list", ["3.11", "3.12", "3.13"])]

    write(tree, ".github/workflows/ci.yml", "jobs: {}\n")
    check_docs.check_python_versions()
    assert "no two-list python-version line" in check_docs.failures[0]

    check_docs.failures.clear()
    workflow(tree, "lint")
    write(tree, "A.md", "Python 3.11 and 3.12, and 3.12 only on pull requests Python.\n")
    check_docs.check_python_versions()
    assert check_docs.failures == []
    assert "CI tests Python 3.11, 3.12 on main and 3.12 on pull requests" in check_docs.passes[0]


def test_check_docs_own_total_and_notebooks_report_each_way_they_can_be_wrong(tree):
    """The notebook and own-total checks report each way they can go wrong.

    Absent notebooks skip, check_own_total skips after an earlier skip, and it fails when
    HANDOFF.md states no total or a wrong one.
    """
    check_docs.check_notebook_assertions()
    assert len(check_docs.skips) == 2

    check_docs.skips.clear()
    check_docs.skips.append("SKIP: earlier")
    check_docs.check_own_total()
    assert len(check_docs.skips) == 2
    assert "how many checks check_docs.py runs" in check_docs.skips[1]

    check_docs.skips.clear()
    write(tree, "HANDOFF.md", "nothing about it\n")
    check_docs.check_own_total()
    assert "does not state how many checks" in check_docs.failures[0]

    check_docs.failures.clear()
    write(tree, "HANDOFF.md", "| `tools/check_docs.py` | 7 checks |\n")
    check_docs.check_own_total()
    assert "says check_docs.py has 7 checks, it has 1" in check_docs.failures[0]
