"""Tests of the release gate, the notebook runner and the notebook generator.

`tools/check_release.py` is exercised against a complete synthetic repository built in a
temporary directory, so every pass and every failure branch of the gate runs on purpose and
none needs the real caches, a TeX toolchain, pandoc, fonts or a network. Only the canonical
model is read from the real checkout, because the gate hashes and executes it. Each test
breaks exactly one thing in the synthetic tree and asserts the matching `FAIL:` line.

`tools/run_notebook.py` is run against tiny notebooks written to a temporary directory: a
clean one, one whose cell raises, one that records a failed assertion, one with a silent cell,
stale stored output, and a missing file. `tools/regenerate_notebooks.py` is checked for the
cell format it writes and for the files `main()` produces, with its output redirected.

Nothing here writes into the repository.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import check_release as cr  # noqa: E402
import regenerate_notebooks as regen  # noqa: E402
import run_notebook as rn  # noqa: E402

# ---------------------------------------------------------------------------------------
# check_release: a synthetic, complete repository
# ---------------------------------------------------------------------------------------

OLD, MID, NEW = 1_700_000_000, 1_700_000_100, 1_700_000_200   # source < report < artifact

EXTRA_META = {
    "sens3.json": {"global_draws_completed": 1002},
    "tiered.json": {"tiered_draws_completed": 1000, "random_matrix_draws_completed": 1000},
    "oat_full.json": {"perturbations_completed": 944},
    "morris.json": {"r": 20},
    "sobol.json": {"n_base": 1024},
}

NOTEBOOKS = ("model/book-calculations.ipynb",
             "paper/anonymity-as-an-aggregation-condition.ipynb")
PDFS = ("build/nobody-in-charge.pdf",
        "paper/anonymity-as-an-aggregation-condition.pdf",
        "reference/PRIMER-steps-and-traditions.pdf")


def _write(path: Path, text: str = "", mtime: int | None = None) -> Path:
    """Write a file for the synthetic tree, creating parents and optionally pinning mtime.

    The gate compares modification times, so the builders must control them exactly.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    if mtime is not None:
        os.utime(path, (mtime, mtime))
    return path


def _notebook(path: Path, stored: str = "ok") -> None:
    cell = {"cell_type": "code", "source": ["print(1)\n"],
            "outputs": [{"output_type": "stream", "name": "stdout", "text": [stored]}]}
    _write(path, json.dumps({"cells": [{"cell_type": "markdown", "source": ["x"]}, cell]}),
           OLD)


def _build_tree(root: Path) -> None:
    """Write a repository the gate passes, with every mtime ordered source < report < PDF."""
    model_hash = cr.sha256(cr.MODEL)
    for filename, (meta_key, script_name) in cr.CACHES.items():
        script = _write(root / script_name, f"# {script_name}\n", OLD)
        meta = {"status": "complete", "model_sha256": model_hash, "jobs_expected": 3,
                "jobs_completed": 3, "script_sha256": cr.sha256(script),
                **EXTRA_META.get(filename, {})}
        _write(root / "research" / filename, json.dumps({meta_key: meta}), OLD)
    _write(root / "research" / "ROBUSTNESS-RESULTS.md", "report", MID)
    _write(root / "research" / "model-choice-inventory.json", json.dumps({
        "model_sha256": model_hash,
        "registered_set": {"total": 118},
        "protective_index_step_consumption_cells": 17}), OLD)
    for d in ("staged", "incorporated/Maxwell_1950", "incorporated/Golub_Jackson_2010"):
        (root / "research" / d).mkdir(parents=True, exist_ok=True)
    for rel in NOTEBOOKS:
        _notebook(root / rel)
    _write(root / "manuscript" / "01-one.md", "Plain prose.", OLD)
    _write(root / "manuscript" / "02-two.md", "More plain prose.", OLD)
    _write(root / "appendix" / "APPENDIX.md", "appendix", OLD)
    _write(root / "reference" / "PRIMER-steps-and-traditions.md", "primer", OLD)
    _write(root / "paper" / "anonymity-as-an-aggregation-condition.tex", "tex", OLD)
    _write(root / "tools" / "build_book.py", "# build", OLD)
    _write(root / "tools" / "check_portability.py", "raise SystemExit(0)\n", OLD)
    for rel in PDFS:
        _write(root / rel, "x" * 20_000, NEW)


@pytest.fixture
def tree(tmp_path, monkeypatch):
    """A passing synthetic repository, installed as the gate's ROOT."""
    _build_tree(tmp_path)
    monkeypatch.setattr(cr, "ROOT", tmp_path)
    return tmp_path


def _gate(monkeypatch, capsys, *flags):
    """Run check_release.main() with the given flags; return its exit code and stdout.

    Every gate test asserts on that pair, so one helper keeps them uniform.
    """
    monkeypatch.setattr(sys, "argv", ["check_release.py", *flags])
    code = cr.main()
    return code, capsys.readouterr().out


def _edit_json(path: Path, mutate) -> None:
    """Mutate a JSON file in place while keeping its modification time.

    Only the content changes, so a test breaks one field without also tripping a freshness
    check.
    """
    data = json.loads(path.read_text())
    mutate(data)
    stat = path.stat()
    path.write_text(json.dumps(data))
    os.utime(path, (stat.st_atime, stat.st_mtime))


def test_sha256_is_the_hash_of_the_bytes(tmp_path):
    """Pin sha256 to the known digest of the bytes b'abc'.

    Every cache, script and model-hash comparison in the gate rests on it.
    """
    f = tmp_path / "f"
    f.write_bytes(b"abc")
    assert cr.sha256(f) == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


def test_load_model_returns_the_canonical_module():
    """The gate loads the real model (capacity 60) without caching it in sys.modules.

    A cached copy could leak a stale model between checks.
    """
    model = cr.load_model()
    assert model.DEFAULTS["cap"] == 60
    assert "release_check_model" not in sys.modules      # private: never cached globally


def test_gate_passes_on_a_complete_tree(tree, monkeypatch, capsys):
    """The complete synthetic repository passes every check, with no FAIL and no SKIP.

    Each later failure test is then attributable to the one thing it breaks.
    """
    code, out = _gate(monkeypatch, capsys)
    assert code == 0
    assert "FAIL" not in out and "SKIP" not in out
    assert "0 failed" in out and "checks passed" in out
    assert "OK: modeled room capacity remains 60" in out


def test_skip_artifacts_reports_six_skips_and_does_not_need_the_pdfs(tree, monkeypatch, capsys):
    """--skip-artifacts passes without the PDFs and reports exactly six skipped checks.

    The pull-request checkers job relies on that, and a skipped check must not count as passed.
    """
    for rel in PDFS:
        (tree / rel).unlink()
    code, out = _gate(monkeypatch, capsys, "--skip-artifacts")
    assert code == 0
    assert out.count("SKIP: ") == 6
    assert "6 skipped (--skip-artifacts" in out


@pytest.mark.parametrize("damage, expected", [
    ("missing", "FAIL: rendered artifact exists and is nontrivial: build/nobody-in-charge.pdf"),
    ("tiny", "FAIL: rendered artifact exists and is nontrivial: build/nobody-in-charge.pdf"),
    ("stale", "FAIL: rendered artifact is newer than its sources: build/nobody-in-charge.pdf"),
])
def test_a_missing_tiny_or_stale_pdf_fails_the_gate(tree, monkeypatch, capsys, damage, expected):
    """A PDF that is absent, trivially small or older than its sources fails the gate.

    Otherwise an empty or stale render could be released.
    """
    pdf = tree / "build" / "nobody-in-charge.pdf"
    if damage == "missing":
        pdf.unlink()
    elif damage == "tiny":
        pdf.write_text("x")
    else:
        os.utime(pdf, (OLD - 5, OLD - 5))
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert expected in out


def test_a_missing_cache_is_a_failure_not_a_crash(tree, monkeypatch, capsys):
    """A missing cache and a missing report give FAIL lines rather than an exception.

    The gate then lists every problem in one run.
    """
    (tree / "research" / "part5.json").unlink()
    (tree / "research" / "ROBUSTNESS-RESULTS.md").unlink()   # its mtime check needs every cache
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert "FAIL: cache exists: research/part5.json" in out
    assert "FAIL: expanded robustness report exists" in out


def test_an_unparsable_cache_is_reported_with_its_error(tree, monkeypatch, capsys):
    """A cache that is not valid JSON fails by name instead of crashing the gate.

    The reader sees which file is corrupt.
    """
    (tree / "research" / "part5.json").write_text("{not json")
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert "FAIL: research/part5.json is not valid JSON" in out


@pytest.mark.parametrize("mutate, expected", [
    (lambda m: m.update(status="running"), "FAIL: research/part5.json status is complete"),
    (lambda m: m.update(model_sha256="0" * 64),
     "FAIL: research/part5.json matches current model hash"),
    (lambda m: m.update(jobs_completed=2),
     "FAIL: research/part5.json completed 3 registered jobs"),
    (lambda m: m.update(script_sha256="0" * 64),
     "FAIL: research/part5.json matches current analysis hash"),
])
def test_an_incomplete_or_stale_cache_fails(tree, monkeypatch, capsys, mutate, expected):
    """A cache with the wrong status, model hash, job count or script hash fails.

    That catches a cache computed under a different model or script than the one in the tree.
    """
    _edit_json(tree / "research" / "part5.json", lambda d: mutate(d["meta"]))
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert expected in out


def test_a_cache_without_optional_fields_is_not_over_checked(tree, monkeypatch, capsys):
    """No model hash, job counts or script hash recorded: only the status is required."""
    _edit_json(tree / "research" / "part5.json", lambda d: d.update(meta={"status": "complete"}))
    code, out = _gate(monkeypatch, capsys)
    assert code == 0
    assert "research/part5.json matches current model hash" not in out


def test_a_missing_analysis_script_fails_and_skips_its_hash(tree, monkeypatch, capsys):
    """A missing analysis script fails once and is not also compared by hash.

    Hashing a file that cannot be read would raise or add a misleading second failure.
    """
    (tree / "model" / "part5_runs.py").unlink()
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert "FAIL: analysis source exists: model/part5_runs.py" in out
    assert "research/part5.json matches current analysis hash" not in out


@pytest.mark.parametrize("filename, key, field, value, expected", [
    ("sens3.json", "_meta", "global_draws_completed", 1001, "1,002 independent perturbation"),
    ("tiered.json", "_meta", "tiered_draws_completed", 5, "tiered screen contains 1,000"),
    ("tiered.json", "_meta", "random_matrix_draws_completed", 5, "randomized-matrix screen"),
    ("oat_full.json", "meta", "perturbations_completed", 5, "multi-level OAT contains 944"),
    ("morris.json", "meta", "r", 19, "Morris screen contains 20 trajectories"),
    ("sobol.json", "meta", "n_base", 512, "Sobol design has a 1,024-row base sample"),
])
def test_each_registered_design_count_is_enforced(tree, monkeypatch, capsys, filename, key,
                                                  field, value, expected):
    """Each registered release design count fails the gate when its recorded value is off.

    The counts are 1,002, 1,000, 1,000, 944, 20 and 1,024, so a cache from a smaller run must
    not pass as the release run.
    """
    _edit_json(tree / "research" / filename, lambda d: d[key].update({field: value}))
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert any(line.startswith("FAIL: ") and expected in line for line in out.splitlines())


def test_a_design_cache_that_is_missing_raises_rather_than_passing(tree, monkeypatch, capsys):
    """With the Sobol cache absent the count checks raise FileNotFoundError.

    A missing design must never be read as a satisfied one.
    """
    (tree / "research" / "sobol.json").unlink()
    with pytest.raises(FileNotFoundError):
        _gate(monkeypatch, capsys)


def test_a_report_older_than_a_cache_fails(tree, monkeypatch, capsys):
    """The robustness report must be newer than every registered cache.

    A report left behind by a later recomputation would describe numbers that no longer exist.
    """
    os.utime(tree / "research" / "ROBUSTNESS-RESULTS.md", (OLD - 5, OLD - 5))
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert "FAIL: expanded robustness report is newer than every registered cache" in out


@pytest.mark.parametrize("mutate, expected", [
    (lambda d: d.update(model_sha256="0" * 64), "model-choice inventory matches current model"),
    (lambda d: d.update(registered_set={"total": 117}), "registered sensitivity set is 118"),
    (lambda d: d.update(protective_index_step_consumption_cells=35),
     "protective index-step count is 17, not 35"),
])
def test_the_model_choice_inventory_is_enforced(tree, monkeypatch, capsys, mutate, expected):
    """The inventory must carry the current model hash, a registered set of 118 and 17 step cells.

    A drifted inventory would misstate which choices were registered.
    """
    _edit_json(tree / "research" / "model-choice-inventory.json", mutate)
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert any(line.startswith("FAIL: ") and expected in line for line in out.splitlines())


@pytest.mark.parametrize("directory, expected", [
    ("staged", "the acquisition record remains under research/staged"),
    ("incorporated/Maxwell_1950", "Maxwell active source is under research/incorporated"),
    ("incorporated/Golub_Jackson_2010", "Golub-Jackson active source"),
])
def test_the_source_directories_are_required(tree, monkeypatch, capsys, directory, expected):
    """The staged record and the Maxwell and Golub-Jackson directories must exist.

    The claims built on those sources need the layout to be intact.
    """
    (tree / "research" / directory).rmdir()
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert any(line.startswith("FAIL: ") and expected in line for line in out.splitlines())


def test_a_notebook_code_cell_without_stored_output_fails(tree, monkeypatch, capsys):
    """A notebook code cell with empty stored output fails the gate.

    check_book.py and readers use the stored outputs, so an unrun cell shows nothing.
    """
    path = tree / NOTEBOOKS[0]
    _edit_json(path, lambda d: d["cells"][1].update(outputs=[]))
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert f"FAIL: {NOTEBOOKS[0]} has stored output for every code cell" in out


@pytest.mark.parametrize("stored", ["Traceback (most recent call last)", "  FAIL something"])
def test_a_stored_traceback_or_failed_assertion_fails(tree, monkeypatch, capsys, stored):
    """A notebook that stores a traceback or a '  FAIL' line fails the gate.

    A broken or failing notebook must not ship with its error saved in the file.
    """
    _notebook(tree / NOTEBOOKS[1], stored=stored)
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert f"FAIL: {NOTEBOOKS[1]} stores no traceback or failed assertion" in out


@pytest.mark.parametrize("phrase, label", [
    ("Exactly two simulation results survive.", "no universal two-result sensitivity claim"),
    ("The model found the division.", "two-tier coding is not described as model-discovered"),
    ("at least three instruments per latent", "rho exercise does not claim a three-instrument"),
    ("dead groups count as zero", "endpoint nonviability is not mislabeled as death"),
])
def test_retired_language_in_public_text_fails(tree, monkeypatch, capsys, phrase, label):
    """Each retired phrase planted in a chapter produces its matching FAIL label.

    Superseded claims must not survive in public text.
    """
    chapter = tree / "manuscript" / "02-two.md"
    stat = chapter.stat()
    chapter.write_text(f"Prose, then: {phrase}\n")
    os.utime(chapter, (stat.st_atime, stat.st_mtime))
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert f"FAIL: {label}" in out


def test_a_failing_portability_check_is_reported_line_by_line(tree, monkeypatch, capsys):
    """A nonzero check_portability.py fails the gate and its offending lines are echoed.

    A host-specific path can then be found from the gate output alone.
    """
    (tree / "tools" / "check_portability.py").write_text(
        "print('tools/x.py:3: a host path')\nraise SystemExit(1)\n")
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert "FAIL: tracked project text contains no machine-specific absolute paths" in out
    assert "FAIL: tools/x.py:3: a host path" in out


def test_a_missing_portability_checker_fails_without_crashing(tree, monkeypatch, capsys):
    """A missing check_portability.py fails the portability check instead of raising.

    The gate still completes and reports it.
    """
    (tree / "tools" / "check_portability.py").unlink()
    code, out = _gate(monkeypatch, capsys)
    assert code == 1
    assert "FAIL: tracked project text contains no machine-specific absolute paths" in out


# ---------------------------------------------------------------------------------------
# run_notebook
# ---------------------------------------------------------------------------------------

def _make_nb(path: Path, *sources: str, stored: dict[int, str] | None = None) -> Path:
    """Write a notebook of one markdown cell, then a code cell per source."""
    cells: list[dict] = [{"cell_type": "markdown", "metadata": {}, "source": ["# title\n"]}]
    for i, src in enumerate(sources, start=1):
        outputs = ([{"output_type": "stream", "name": "stdout", "text": [stored[i]]}]
                   if stored and i in stored else [])
        cells.append({"cell_type": "code", "execution_count": 7, "metadata": {},
                      "outputs": outputs, "source": src.splitlines(keepends=True)})
    path.write_text(json.dumps({"cells": cells, "metadata": {}, "nbformat": 4,
                                "nbformat_minor": 5}, indent=1))
    return path


@pytest.mark.parametrize("x, y, expected", [
    ("12", "12", True),
    ("12", "13", False),                 # whole numbers are counts: exact
    ("5.7428", "5.7427", True),          # one unit in the last printed place
    ("5.7428", "5.7430", False),         # two units
    ("0.5", "0.50", True),
    ("1.0000000001e5", "1.0e5", True),   # full-length floats: relative 1e-9
    ("1.0e5", "1.1e5", False),
    ("3.0", "3", True),                  # a decimal against a whole number, within a unit
    ("3.5", "3", False),
])
def test_same_number(x, y, expected):
    """same_number takes exact whole numbers, one printed unit for decimals, 1e-9 for floats.

    Anything looser would excuse real drift in a count or a result, and anything stricter would
    fail across machines.
    """
    assert rn.same_number(x, y) is expected


@pytest.mark.parametrize("stored, fresh, expected", [
    ("a 1 b 2\n", "a 1 b 2\n", True),
    ("p = 5.7428\n", "p = 5.7427\n", True),
    ("count 12\n", "count 13\n", False),
    ("word 1\n", "other 1\n", False),               # text differs outside the numbers
    ("1 2\n", "1\n", False),                        # different number of lines
    ("1 2 3\n", "1 2\n", False),                    # different number of numbers
    ("a\nb\n", "a\nb\n", True),
])
def test_same_output(stored, fresh, expected):
    """same_output excuses only the numeric differences same_number allows.

    A changed word or a different number of lines or numbers must be rejected, or --check could
    not see real drift.
    """
    assert rn.same_output(stored, fresh) is expected


def test_stale_lines_pairs_lines_and_pads_the_shorter_side():
    """stale_lines reports (cell, stored, fresh) only for lines that differ.

    It pads the shorter side with empty strings and skips markdown cells, agreeing cells and
    cells with no stored output key.
    """
    nb = {"cells": [
        {"cell_type": "markdown"},
        {"cell_type": "code", "outputs": [{"text": ["a 1\n", "b 2\n"]}]},
        {"cell_type": "code", "outputs": [{"text": ["same 3\n"]}]},
        {"cell_type": "code"},                       # no stored output key at all
    ]}
    outs = {1: "a 1\nb 9\nextra\n", 2: "same 3\n", 3: ""}
    assert rn.stale_lines(nb, outs) == [(1, "b 2", "b 9"), (1, "", "extra")]


def test_a_clean_notebook_runs_and_its_outputs_are_written_back(tmp_path, capsys):
    """A clean run exits 0, counts cells and assertions, and writes each cell's stdout back.

    Cells share one namespace, the working directory is restored and the stored execution count
    is cleared.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "x = 2\nprint('  OK first', x)\n",
                  "print('  OK second', x)")
    before = os.getcwd()
    assert rn.main(notebook=str(nb)) == 0
    out = capsys.readouterr().out
    assert "2 code cells run" in out and "2 assertions" in out
    assert "outputs written back" in out and out.rstrip().endswith("CLEAN")
    assert os.getcwd() == before                       # the working directory is restored
    cells = json.loads(nb.read_text())["cells"]
    assert cells[0] == {"cell_type": "markdown", "metadata": {}, "source": ["# title\n"]}
    assert cells[1]["outputs"] == [{"output_type": "stream", "name": "stdout",
                                    "text": ["  OK first 2\n"]}]
    assert cells[1]["execution_count"] is None


def test_cells_run_in_the_notebooks_own_directory(tmp_path, capsys):
    """Cells execute with the working directory set to the notebook's own folder.

    Relative cache paths then resolve the same way wherever the runner is launched.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "import os; print(os.getcwd())")
    assert rn.main(notebook=str(nb)) == 0
    capsys.readouterr()
    text = json.loads(nb.read_text())["cells"][1]["outputs"][0]["text"][0]
    assert Path(text.strip()).resolve() == tmp_path.resolve()


def test_no_write_leaves_the_file_untouched(tmp_path, capsys):
    """With write=False the notebook stays byte-identical and no write message appears.

    That is what makes --no-write safe on committed notebooks.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "print('  OK')")
    original = nb.read_bytes()
    assert rn.main(notebook=str(nb), write=False) == 0
    assert nb.read_bytes() == original
    assert "outputs written back" not in capsys.readouterr().out


def test_a_cell_that_raises_is_reported_and_blocks_the_write(tmp_path, capsys):
    """A raising cell is reported with its traceback, the run exits 1 and the file is not written.

    The run continues past the failure to list every broken cell, and good stored outputs are
    never overwritten by a broken run.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "print('  OK before')\nraise ValueError('boom')",
                  "print('  OK still runs')")
    original = nb.read_bytes()
    assert rn.main(notebook=str(nb)) == 1
    out = capsys.readouterr().out
    assert "CELL 1 RAISED" in out and "ValueError: boom" in out
    assert "outputs written back" not in out and out.rstrip().endswith("NOT CLEAN")
    assert "2 code cells run" in out                  # the run continued past the failure
    assert nb.read_bytes() == original


def test_a_recorded_assertion_failure_is_reported_but_outputs_still_written(tmp_path, capsys):
    """A recorded FAILURES entry exits 1 but the outputs are still written back.

    The failing line is then visible in the saved notebook.
    """
    nb = _make_nb(tmp_path / "n.ipynb",
                  "FAILURES = ['the check named x']\nprint('  FAIL the check named x')")
    assert rn.main(notebook=str(nb)) == 1
    out = capsys.readouterr().out
    assert "1 ASSERTION FAILURES" in out and "the check named x" in out
    assert "outputs written back" in out              # so the failure is visible in the file
    assert "  FAIL the check named x" in nb.read_text()


def test_a_cell_with_no_output_is_flagged(tmp_path, capsys):
    """A code cell that prints nothing is flagged, fails the run and is stored with no outputs.

    A silent cell verifies nothing.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "y = 1", "print('  OK')")
    assert rn.main(notebook=str(nb)) == 1
    out = capsys.readouterr().out
    assert "cells producing NO output: [1]" in out
    cells = json.loads(nb.read_text())["cells"]
    assert cells[1]["outputs"] == []                  # a silent cell is stored with no outputs


def test_check_passes_when_stored_output_matches_and_never_writes(tmp_path, capsys):
    """With check=True, stored output that agrees to printed precision passes without a write.

    The comparison must tolerate last-digit differences between machines.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "print('  OK 5.7427')", stored={1: "  OK 5.7428\n"})
    original = nb.read_bytes()
    assert rn.main(notebook=str(nb), check=True) == 0
    assert nb.read_bytes() == original
    assert "STALE" not in capsys.readouterr().out


def test_check_fails_on_stale_stored_output(tmp_path, capsys):
    """With check=True a stored 460 against a fresh 451 fails and prints both lines.

    It leaves the file untouched; this is the staleness that went unnoticed in the paper
    notebook.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "print('  OK 451')", stored={1: "  OK 460\n"})
    original = nb.read_bytes()
    assert rn.main(notebook=str(nb), check=True) == 1
    out = capsys.readouterr().out
    assert "CELL 1 STORES STALE OUTPUT" in out
    assert "stored:   OK 460" in out and "fresh:    OK 451" in out
    assert "1 stale line(s)" in out
    assert nb.read_bytes() == original


def test_a_missing_notebook_raises_before_any_cell_runs(tmp_path):
    """A nonexistent notebook path raises FileNotFoundError immediately.

    It must not report a clean run of zero cells.
    """
    with pytest.raises(FileNotFoundError):
        rn.main(notebook=str(tmp_path / "absent.ipynb"))


def _run_cli(*args: str) -> subprocess.CompletedProcess:
    """Run tools/run_notebook.py as a subprocess from the repository root.

    The command-line tests need the real argument parsing and exit status.
    """
    return subprocess.run([sys.executable, str(ROOT / "tools" / "run_notebook.py"), *args],
                          capture_output=True, text=True, cwd=ROOT, check=False)


def test_command_line_runs_a_notebook_given_by_absolute_path(tmp_path):
    """The command line accepts an absolute notebook path with --no-write and reports CLEAN.

    It exits 0.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "print('  OK')")
    result = _run_cli("--no-write", str(nb))
    assert result.returncode == 0 and "CLEAN" in result.stdout


def test_command_line_resolves_a_relative_path_from_the_repository_root(tmp_path):
    """A relative notebook path is resolved from the repository root and works with --check.

    The result must not depend on the caller's working directory.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "print('  OK')", stored={1: "  OK\n"})
    relative = os.path.relpath(nb, ROOT)
    result = _run_cli("--check", relative)
    assert result.returncode == 0 and "CLEAN" in result.stdout


def test_command_line_exit_status_is_nonzero_when_a_cell_raises(tmp_path):
    """The command line exits 1 and shows the exception when a cell raises.

    That exit status is what lets the runner act as a gate.
    """
    nb = _make_nb(tmp_path / "n.ipynb", "1 / 0")
    result = _run_cli(str(nb))
    assert result.returncode == 1 and "ZeroDivisionError" in result.stdout


def test_command_line_missing_notebook_fails(tmp_path):
    """A missing notebook gives a nonzero exit and a FileNotFoundError on stderr.

    The tool must not succeed quietly on a bad path.
    """
    result = _run_cli(str(tmp_path / "absent.ipynb"))
    assert result.returncode != 0 and "FileNotFoundError" in result.stderr


# ---------------------------------------------------------------------------------------
# regenerate_notebooks
# ---------------------------------------------------------------------------------------

def test_code_cell_is_empty_of_outputs_and_strips_surrounding_blank_lines():
    """regen.code builds a code cell with no outputs and a null execution count.

    Its source is newline-terminated lines with outer blank lines stripped, so regenerated
    notebooks are deterministic.
    """
    cell = regen.code("\n\nx = 1\ny = 2\n\n")
    assert cell == {"cell_type": "code", "execution_count": None, "metadata": {},
                    "outputs": [], "source": ["x = 1\n", "y = 2\n"]}


def test_markdown_cell_splits_into_newline_terminated_lines():
    """regen.markdown strips outer blank lines and keeps interior ones.

    Every line ends in a newline, the format Jupyter stores.
    """
    cell = regen.markdown("\n# T\n\ntext\n")
    assert cell == {"cell_type": "markdown", "metadata": {}, "source": ["# T\n", "\n", "text\n"]}


def test_notebook_places_extra_cells_before_the_final_verdict():
    """regen.notebook inserts extra cells before the closing verdict cell, which stays last.

    It also writes the standard title block and a python3 kernelspec, so every generated
    notebook has the same frame.
    """
    plain = regen.notebook("Title", "Blurb")
    extra = regen.notebook("Title", "Blurb", extra=("print('a')", "print('b')"))
    assert len(extra["cells"]) == len(plain["cells"]) + 2
    assert extra["cells"][-1] == plain["cells"][-1] == regen.code(regen.FINAL)
    assert extra["cells"][-3]["source"] == ["print('a')\n"]
    title = "".join(plain["cells"][0]["source"])
    assert title.startswith("# Title\n\nBlurb\n\nGenerated by `tools/regenerate_notebooks.py`.")
    assert title.endswith("cache-backed and hash-checked.\n")
    assert plain["nbformat"] == 4 and plain["metadata"]["kernelspec"]["name"] == "python3"


def test_build_returns_the_two_public_notebooks():
    """regen.build returns the book and paper notebooks in order, the paper with two more cells.

    No code cell carries stored outputs, since those come from run_notebook.
    """
    built = regen.build()
    assert [p.relative_to(regen.ROOT).as_posix() for p in built] == list(NOTEBOOKS)
    book, paper = built.values()
    assert len(paper["cells"]) == len(book["cells"]) + 2
    assert all(c["outputs"] == [] for n in built.values() for c in n["cells"]
               if c["cell_type"] == "code")


def test_main_writes_compact_indent_one_json_and_prints_relative_paths(tmp_path, monkeypatch,
                                                                       capsys):
    """regen.main writes indent-one JSON with a trailing newline and prints the relative path.

    Regenerated files then diff cleanly and the output names no host path.
    """
    monkeypatch.setattr(regen, "ROOT", tmp_path)
    target = tmp_path / "out.ipynb"
    monkeypatch.setattr(regen, "build", lambda: {target: {"cells": [], "nbformat": 4}})
    regen.main()
    assert target.read_text() == json.dumps({"cells": [], "nbformat": 4}, indent=1) + "\n"
    assert capsys.readouterr().out == "out.ipynb\n"
