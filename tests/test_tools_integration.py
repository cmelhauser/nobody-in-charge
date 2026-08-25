"""Integration tests for the command-line tools.

These run each tool for real against the repository and assert it succeeds. They are
not unit tests and they are not in the coverage gate; see the scope note in
`.coveragerc` for why. What they buy is the thing that actually breaks in a project
like this: a checker that stops importing, a builder whose pandoc invocation rots, or
a release gate that starts passing because it stopped looking.

Anything that renders a PDF or executes a release design is skipped unless the
environment asks for it, because those take minutes and need a TeX toolchain. Set
NIC_SLOW_TESTS=1 to include them.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SLOW = os.environ.get("NIC_SLOW_TESTS") == "1"
requires_slow = pytest.mark.skipif(not SLOW, reason="set NIC_SLOW_TESTS=1 to run")


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], cwd=ROOT,
                          capture_output=True, text=True, timeout=1800)


# ------------------------------------------------------------------ fast checkers

def test_check_book_reports_no_failures():
    result = run("tools/check_book.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 failures" in result.stdout


def test_check_portability_finds_no_absolute_paths():
    result = run("tools/check_portability.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "no tracked machine-specific absolute paths" in result.stdout


def test_check_docs_matches_the_tree():
    """Counts stated in prose must match the repository they describe.

    This one has a property the other checkers do not: it verifies claims about the tree,
    so it fails when a job, checker, source or chapter is added without the prose that
    counts them being updated. That is the drift the 24 August 2026 sweep found.
    """
    result = run("tools/check_docs.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 failed" in result.stdout


def test_check_docs_catches_a_miscount(tmp_path):
    """A checker that has never failed is a checker nobody has tested.

    Copying the tree would be slow, so this asserts on the derivation instead: the checker
    must report the same job count the workflow actually defines.
    """
    result = run("tools/check_docs.py")
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    jobs = len([
        line for line in workflow.split("jobs:", 1)[-1].splitlines()
        if line.startswith("  ") and line.rstrip().endswith(":")
        and not line.startswith("    ") and not line.strip().startswith("#")
    ])
    assert f"job count is {jobs}" in result.stdout, result.stdout


def test_check_chapter_accepts_the_primer():
    result = run("tools/check_chapter.py", "reference/PRIMER-steps-and-traditions.md")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "all clear" in result.stdout


@pytest.mark.parametrize("chapter", sorted(
    p.name for p in (ROOT / "manuscript").glob("ch*.md")))
def test_every_chapter_passes_its_own_checker(chapter):
    result = run("tools/check_chapter.py", f"manuscript/{chapter}")
    assert result.returncode == 0, result.stdout + result.stderr


def test_corpus_reports_no_drift():
    result = run("tools/build_corpus.py", "--check")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 corpus problems" in result.stdout


@requires_slow
def test_release_gate_passes():
    """The fail-closed gate. If this goes red the release is not shippable.

    Behind the slow marker because part of what it checks is that each rendered PDF
    is at least as new as every source feeding it. A fresh clone gives every file the
    same checkout timestamp, and checkout order can leave a source a fraction of a
    second ahead of its artifact, so this must run against artifacts that were
    actually built. The full CI job rebuilds them first; locally they are already
    current.
    """
    result = run("tools/check_release.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 failed" in result.stdout


# ------------------------------------------------------------- structural checks

def test_every_tool_is_syntactically_importable():
    """A tool that no longer parses would otherwise fail only when someone ran it."""
    import py_compile

    for path in sorted((ROOT / "tools").glob("*.py")):
        py_compile.compile(str(path), doraise=True)


def test_every_model_script_is_syntactically_valid():
    import py_compile

    for path in sorted((ROOT / "model").glob("*.py")):
        py_compile.compile(str(path), doraise=True)


def test_no_source_document_is_tracked_by_git():
    """The corpus rule: no PDF, text, djvu or epub source is ever committed."""
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT,
                             capture_output=True, text=True).stdout.splitlines()
    offenders = [
        p for p in tracked
        if p.startswith(("research/incorporated/", "research/staged/"))
        and p.lower().endswith((".pdf", ".txt", ".djvu", ".epub"))
    ]
    assert offenders == [], f"source documents must not be committed: {offenders}"


def test_the_canonical_model_is_tracked():
    tracked = subprocess.run(["git", "ls-files", "model/aa_group_model.py"],
                             cwd=ROOT, capture_output=True, text=True).stdout
    assert tracked.strip() == "model/aa_group_model.py"


# ------------------------------------------------------------------ slow builders

@requires_slow
@pytest.mark.skipif(shutil.which("pandoc") is None, reason="pandoc not installed")
def test_the_primer_builds_without_overfull_boxes():
    result = run("tools/build_primer.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "overfull boxes: 0" in result.stdout


@requires_slow
@pytest.mark.skipif(shutil.which("pandoc") is None, reason="pandoc not installed")
def test_the_book_assembles():
    result = run("tools/build_book.py", "--no-pdf")
    assert result.returncode == 0, result.stdout + result.stderr
    assert (ROOT / "build" / "nobody-in-charge.md").exists()
