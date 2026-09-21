"""Integration tests for the command-line tools.

These run each tool for real against the repository and assert it succeeds. They are
not unit tests and they are not in the coverage gate; see the scope note in
`.coveragerc` for why. What they buy is the thing that actually breaks in a project
like this: a checker that stops importing, a builder whose pandoc invocation rots, or
a release gate that starts passing because it stopped looking.

Anything that renders a PDF or executes a release design is skipped unless the
environment asks for it, because those take minutes and need a TeX toolchain. Set
NIC_SLOW_TESTS=1 to include them.

The group headed "generated outputs match what generates them" goes one step further and
compares committed files with what their generators would write now, so a registered cache, a
notebook or a derived report cannot go stale without a failure.
"""
from __future__ import annotations

import hashlib
import importlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import types
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


# --------------------------------------- generated outputs match what generates them

def test_skip_artifacts_skips_exactly_the_artifact_checks():
    """`--skip-artifacts` must omit the six rendered-PDF checks and nothing else.

    It once counted its own notice as a passed check while the documents describing it said
    seven were omitted. Totals are compared rather than verdicts, so this holds in a fresh
    clone, where the full gate's freshness checks cannot pass.
    """
    import re

    def counts(*args):
        out = run("tools/check_release.py", *args).stdout
        found = re.search(r"(\d+) checks passed; (\d+) failed(?:; (\d+) skipped)?", out)
        assert found, out
        return [int(g or 0) for g in found.groups()]

    full, skipping = counts(), counts("--skip-artifacts")
    assert full[2] == 0 and skipping[2] == 6
    assert skipping[0] + skipping[1] + 6 == full[0] + full[1]


def test_both_notebooks_execute_clean():
    """Continuous integration otherwise never executes them; `check_book.py` reads their
    committed outputs. `--no-write` leaves the committed notebooks untouched."""
    for args in ((), ("--paper",)):
        result = run("tools/run_notebook.py", "--no-write", *args)
        assert result.returncode == 0, result.stdout + result.stderr
        assert result.stdout.strip().splitlines()[-1] == "CLEAN", result.stdout


def test_notebooks_match_their_generator():
    """The committed notebooks' code must be what `tools/regenerate_notebooks.py` writes.

    A cache registered in the generator but not regenerated into the notebooks would leave
    them checking the old set, and nothing else would notice.
    """
    import json

    import regenerate_notebooks

    for path, generated in regenerate_notebooks.build().items():
        committed = json.loads(path.read_text())
        assert ([(c["cell_type"], "".join(c["source"])) for c in committed["cells"]]
                == [(c["cell_type"], "".join(c["source"])) for c in generated["cells"]]), path.name


def test_robustness_report_is_current():
    """`research/ROBUSTNESS-RESULTS.md` must be what its generator writes from the caches.

    The release gate checks only that the report is newer than every cache, which a fresh
    clone satisfies whatever the report says.
    """
    import summarize_robustness

    assert summarize_robustness.render() == summarize_robustness.OUT.read_text()


def test_decay_ordering_reproduces_its_cache(monkeypatch):
    """`research/decay_ordering.json` must be what `model/decay_ordering.py` computes.

    Recomputes one cell of each condition from scratch against the cached row, and checks
    that the job list the script would run is the one the cache recorded.
    """
    import hashlib
    import json

    import decay_ordering

    monkeypatch.setitem(sys.modules, "m", None)  # _load registers the model as "m"
    cache = json.loads((ROOT / "research" / "decay_ordering.json").read_text())
    meta = cache["meta"]
    assert meta["status"] == "complete"
    assert meta["script_sha256"] == hashlib.sha256(
        (ROOT / "model" / "decay_ordering.py").read_bytes()).hexdigest()
    jobs = decay_ordering.jobs()
    assert meta["jobs_completed"] == len(jobs) == 4800
    assert all(cache[str(i)]["job"] == list(job) for i, job in enumerate(jobs))
    for job in ((0, "referral", 0), (-25, "attraction", 1), (-50, "full", 2)):
        got, want = decay_ordering._one(job), cache[str(jobs.index(job))]
        for key in ("pc", "scen", "seed", "N", "exists", "viable", "closed"):
            assert got[key] == want[key], (job, key)
        for key in ("practice", "maint"):
            assert got[key] == pytest.approx(want[key], rel=1e-9, abs=1e-12), (job, key)


def test_decay_reversal_reproduces_its_cache(monkeypatch):
    """`research/decay_reversal.json` must be what `model/decay_reversal.py` computes."""
    import hashlib
    import json

    import decay_reversal

    monkeypatch.setitem(sys.modules, "m", None)  # _load registers the model as "m"
    cache = json.loads((ROOT / "research" / "decay_reversal.json").read_text())
    meta = cache["meta"]
    assert meta["status"] == "complete"
    assert meta["script_sha256"] == hashlib.sha256(
        (ROOT / "model" / "decay_reversal.py").read_bytes()).hexdigest()
    jobs = decay_reversal.jobs()
    assert meta["jobs_completed"] == len(jobs) == 3600
    assert all(cache[str(i)]["job"] == list(job) for i, job in enumerate(jobs))
    for job in ((-10, "referral", 0), (-15, "attraction", 1), (-20, "full", 2)):
        got, want = decay_reversal._one(job), cache[str(jobs.index(job))]
        for key in ("pc", "scen", "seed", "N", "exists", "viable", "closed"):
            assert got[key] == want[key], (job, key)
        for key in ("practice", "maint"):
            assert got[key] == pytest.approx(want[key], rel=1e-9, abs=1e-12), (job, key)


def test_decay_reversal_is_the_ordering_design_at_other_levels():
    """The two decay caches are read as one series, which requires one design.

    Everything but the docstring, the level list and the two names must match, so that
    `decay_reversal.json` cannot drift into a different horizon, intervention or outcome
    definition from `decay_ordering.json` while the prose still reports them together.
    """
    import ast

    def body(path: Path) -> str:
        tree = ast.parse(path.read_text())
        if ast.get_docstring(tree) is not None:
            tree.body = tree.body[1:]
        return ast.unparse(tree)

    theirs = body(ROOT / "model" / "decay_ordering.py")
    ours = (body(ROOT / "model" / "decay_reversal.py")
            .replace("decay_reversal", "decay_ordering")
            .replace("LEV = [-10, -15, -20]", "LEV = [0, -25, -50, -75]"))
    assert ours == theirs


# The script is hash-pinned, so its `json.dump(out, open(tmp, "w"))` cannot be given a
# `with` block without invalidating the cache it wrote. CPython closes the handle as soon as
# the call returns, which is what the assertions below check; the ResourceWarning is ignored
# here and nowhere else.
@pytest.mark.filterwarnings("ignore::ResourceWarning",
                            "ignore::pytest.PytestUnraisableExceptionWarning")
def test_decay_ordering_saves_atomically(tmp_path, monkeypatch):
    import json

    import decay_ordering

    out = tmp_path / "decay_ordering.json"
    monkeypatch.setattr(decay_ordering, "OUT", str(out))
    decay_ordering._save({"meta": {"status": "incomplete"}, "0": {"N": 3}})
    assert json.loads(out.read_text()) == {"meta": {"status": "incomplete"}, "0": {"N": 3}}
    assert not (tmp_path / "decay_ordering.json.tmp").exists()


def test_generator_entry_points_write_what_they_render(tmp_path, monkeypatch, capsys):
    import json

    import regenerate_notebooks
    import summarize_robustness

    monkeypatch.setattr(summarize_robustness, "ROOT", tmp_path)
    monkeypatch.setattr(summarize_robustness, "OUT", tmp_path / "report.md")
    monkeypatch.setattr(summarize_robustness, "render", lambda: "text")
    summarize_robustness.main()
    assert (tmp_path / "report.md").read_text() == "text"

    notebook = tmp_path / "notebook.ipynb"
    monkeypatch.setattr(regenerate_notebooks, "ROOT", tmp_path)
    monkeypatch.setattr(regenerate_notebooks, "build", lambda: {notebook: {"cells": []}})
    regenerate_notebooks.main()
    assert json.loads(notebook.read_text()) == {"cells": []}
    assert capsys.readouterr().out.split() == ["report.md", "notebook.ipynb"]


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


# ------------------------------------------------------------------ the withheld name
#
# These use an invented name, because a test that stored the real one would publish it. Each
# swaps the digest set in tools/withheld.py for the invented name's, then checks that the
# corpus builder leaves it out and the checkers find it.

INVENTED = ("vexmoor", "quillon vexmoor")


def load_tool(name: str, monkeypatch):
    """Import a tool by path, with `tools/` importable and the withheld set swapped."""
    monkeypatch.syspath_prepend(str(ROOT / "tools"))
    withheld = importlib.import_module("withheld")
    monkeypatch.setattr(withheld, "WITHHELD",
                        {hashlib.sha256(term.encode()).hexdigest() for term in INVENTED})
    if name == "withheld":
        return withheld
    spec = importlib.util.spec_from_file_location(f"nic_{name}", ROOT / "tools" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_the_withheld_set_still_holds_both_digests():
    """Emptying the set would pass every test below while enforcing nothing."""
    spec = importlib.util.spec_from_file_location("nic_withheld_as_committed",
                                                  ROOT / "tools" / "withheld.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert len(module.WITHHELD) == 2
    assert all(re.fullmatch(r"[0-9a-f]{64}", digest) for digest in module.WITHHELD)


def test_the_withheld_test_sees_through_possessives_and_compounds(monkeypatch):
    withheld = load_tool("withheld", monkeypatch)
    for form in ("Vexmoor", "vexmoor's", "vexmoor’s", "vexmoor-style",
                 "Quillon Vexmoor", "quillon vexmoor's"):
        assert withheld.is_withheld(form), form
    for form in ("quillon", "moor", "quillon moor"):
        assert not withheld.is_withheld(form), form
    assert withheld.prints_withheld("taught by Quillon\nVexmoor until 2019")
    assert not withheld.prints_withheld("taught by a founding teacher until 2019")


def test_build_index_leaves_a_withheld_word_out(tmp_path, monkeypatch):
    build_corpus = load_tool("build_corpus", monkeypatch)
    doc = tmp_path / "doc.txt"
    doc.write_text("Quillon Vexmoor's retreats, and the Vexmoor years, ended in 2019.\n")
    vocab = build_corpus.build_index(doc, "a work", "0" * 64)["vocab"]
    assert "retreats" in vocab and "quillon" in vocab
    assert not [token for token in vocab if "vexmoor" in token]


def test_corpus_check_flags_a_withheld_index_word_and_the_build_strips_it(
        tmp_path, monkeypatch, capsys):
    """Record-only indexes have no document to rebuild from, so the word is stripped in place."""
    build_corpus = load_tool("build_corpus", monkeypatch)
    monkeypatch.setattr(build_corpus, "RESEARCH", tmp_path)
    monkeypatch.setattr(build_corpus, "INCORP", tmp_path / "incorporated")
    (tmp_path / "SOURCES.md").write_text("")
    source = tmp_path / "incorporated" / "Record_2000"
    source.mkdir(parents=True)
    index = source / "Record_2000_verification-index.json"
    record = {"work": "w", "source_sha256": "0" * 64, "record_only": True,
              "vocab": ["alpha", "vexmoor", "zeta"]}
    index.write_text(json.dumps(record) + "\n")

    monkeypatch.setattr(sys, "argv", ["build_corpus.py", "--check"])
    assert build_corpus.main() == 1
    assert "verification index lists a withheld name: Record_2000" in capsys.readouterr().out
    assert json.loads(index.read_text()) == record

    monkeypatch.setattr(sys, "argv", ["build_corpus.py"])
    assert build_corpus.main() == 0
    assert json.loads(index.read_text()) == {**record, "vocab": ["alpha", "zeta"]}


def test_check_book_finds_a_withheld_name_in_an_index(tmp_path, monkeypatch):
    check_book = load_tool("check_book", monkeypatch)
    index = tmp_path / "Record_2000_verification-index.json"
    index.write_text(json.dumps({"vocab": ["alpha", "vexmoor", "zeta"]}))
    prose = tmp_path / "prose.md"
    prose.write_text("Nothing here names anyone.\n")

    check_book.check_withheld_names([str(index), str(prose), str(tmp_path / "missing.md")])
    names = [msg for section, msg in check_book.FAILS if section == "names"]
    assert len(names) == 1 and "Record_2000_verification-index.json" in names[0]

    check_book.FAILS.clear()
    check_book.check_withheld_names([str(prose)])
    assert not check_book.FAILS
    assert any(section == "names" for section, _ in check_book.NOTES)


def test_the_name_scan_reads_every_tracked_text_file_and_no_source_document(monkeypatch):
    """A fixed list of prose files is how the name sat in two indexes unread."""
    check_book = load_tool("check_book", monkeypatch)
    index = check_book.P("research", "incorporated", "RecoveryDharma_2023",
                         "RecoveryDharma_2023_verification-index.json")
    corpus = check_book.P("research", "incorporated")

    def no_git(*args, **kwargs):
        raise OSError("git is not installed")

    for label in ("with git", "without git"):
        if label == "without git":
            monkeypatch.setattr(check_book, "subprocess", types.SimpleNamespace(
                run=no_git, CalledProcessError=subprocess.CalledProcessError))
        files = check_book.tracked_text_files()
        assert index in files, label
        assert check_book.P("research", "SOURCES.md") in files, label
        assert not [f for f in files if f.endswith(".txt") and f.startswith(corpus)], label
