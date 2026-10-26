"""Tests of the report generators and the corpus builder, on fixtures and temporary trees.

Covers `tools/summarize_release_gate.py`, `tools/summarize_robustness.py`,
`tools/inventory_model_choices.py` and `tools/build_corpus.py`. The three report tools are run
against the committed caches and model, with every output redirected into `tmp_path`, so the
committed reports are only ever read. `build_corpus.py` is run against small invented corpora
built under `tmp_path`; its path constants (`ROOT`, `RESEARCH`, `INCORP`) are monkeypatched
before anything runs, so no test can write into `research/incorporated/`. The only word
treated as withheld here is an invented one, patched in for the test, so nothing in this file
names a real withheld person and the real digest set is never consulted.

Nothing here needs pandoc, tectonic, fonts, a network, or any git-ignored source document.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import inventory_model_choices as inventory
import pytest
import summarize_release_gate as gate
import summarize_robustness as robustness

ROOT = Path(__file__).resolve().parents[1]

# An invented word standing in for a withheld name in every corpus test below.
INVENTED = "vexmoor"


def fake_is_withheld(token: str) -> bool:
    """Stand-in for `withheld.is_withheld`: true for the invented word and its possessive."""
    return token.lower().startswith(INVENTED)


# ------------------------------------------------------------------ summarize_release_gate

def test_gate_formatters_round_half_up_and_format_intervals():
    """Pin the release-gate number formatters and tie-aware ranking.

    A drift to banker's rounding or a tie-breaking sort would silently change numbers in the
    committed report.
    """
    import numpy as np

    assert gate.pct(0.9925) == "99.3%"           # half to even would print 99.2
    assert gate.pct(0.0) == "0.0%"
    assert gate.ci_mean({"mean": 2, "lo": 1, "hi": 3}) == "2.000 [1.000, 3.000]"
    assert gate.ci_prop({"proportion": 0.5, "lo": 0.25, "hi": 0.75}) == "50.0% [25.0%, 75.0%]"
    M = np.array([[1.0, 1.0], [0.0, 0.0]])
    assert gate.top_sets(M) == [[1, 2], [1, 2]]  # exact ties, including a row of zeros
    assert gate.ranks(M) == [1, 1]
    assert gate.rows({"meta": {"nseed": 1}, "c|0": {"v": 7}}, "c") == [{"v": 7}]


def test_gate_loads_the_model_by_path():
    """Check that `load_model` imports the canonical model file by path.

    The summary must read the frozen model rather than whatever `aa_group_model` happens to be on
    `sys.path`.
    """
    module = gate.load_model()
    assert module.__name__ == "summary_model"
    assert hasattr(module, "semantic_overlap")


def test_gate_report_matches_the_committed_report(tmp_path, monkeypatch, capsys):
    """Require the regenerated gate report to equal the committed one.

    This catches a stale report or a generator change that was not propagated, without touching
    the committed file.
    """
    out = tmp_path / "RELEASE-GATE-RESULTS.md"
    monkeypatch.setattr(gate, "OUT", out)
    gate.main()
    assert out.read_text() == (ROOT / "research" / "RELEASE-GATE-RESULTS.md").read_text()
    assert capsys.readouterr().out.startswith("wrote ")


def test_gate_refuses_an_incomplete_cache_before_writing(tmp_path, monkeypatch):
    """Check that an unfinished cache stops `main` before any output exists.

    A partial cache must never be summarised into a report that looks final.
    """
    cache = json.loads(gate.CACHE.read_text())
    cache["meta"]["status"] = "running"
    partial = tmp_path / "cache.json"
    partial.write_text(json.dumps(cache))
    out = tmp_path / "never.md"
    monkeypatch.setattr(gate, "CACHE", partial)
    monkeypatch.setattr(gate, "OUT", out)
    with pytest.raises(RuntimeError, match="incomplete"):
        gate.main()
    assert not out.exists()


def test_gate_states_when_the_recipient_interval_excludes_zero(tmp_path, monkeypatch):
    """Pin the report's wording when the recipient interval excludes zero.

    This pins the conditional wording so it cannot claim resolution (or silence) regardless of the
    data.
    """
    cache = json.loads(gate.CACHE.read_text())
    cache["summary"]["paired_contrasts"]["recipient_unconstrained_minus_base"]["N"].update(
        mean=2.0, lo=1.0, hi=3.0)
    changed = tmp_path / "cache.json"
    changed.write_text(json.dumps(cache))
    out = tmp_path / "report.md"
    monkeypatch.setattr(gate, "CACHE", changed)
    monkeypatch.setattr(gate, "OUT", out)
    gate.main()
    assert "excludes zero, so the clean recipient-capacity ablation is resolved" in out.read_text()


# ---------------------------------------------------------------- summarize_robustness

def test_robustness_helpers():
    """Pin the arithmetic of the `hw` and `classify` helpers.

    A change to either shifts every interval and support count in the robustness report.
    """
    assert robustness.hw([1.0, 3.0]) == pytest.approx(1.96)      # SD sqrt(2) over sqrt(2)
    rows = [{"a": 2, "b": 1}, {"a": 1, "b": 1}, {"a": 0, "b": 1}]
    assert robustness.classify(rows, "a", "b") == (1, 1, 1)


def test_robustness_report_matches_the_committed_report():
    """Require `render()` to reproduce the committed `ROBUSTNESS-RESULTS.md` exactly.

        This catches a report that has drifted from the caches or generator, which would leave
    prose disagreeing with the numbers.
    """
    assert robustness.render() == (ROOT / "research" / "ROBUSTNESS-RESULTS.md").read_text()


def test_robustness_main_writes_the_rendered_text(tmp_path, monkeypatch, capsys):
    """Check that `main` writes exactly what `render` returns.

    This pins the write step and the console message separately from the report content.
    """
    monkeypatch.setattr(robustness, "ROOT", tmp_path)
    monkeypatch.setattr(robustness, "OUT", tmp_path / "report.md")
    monkeypatch.setattr(robustness, "render", lambda: "rendered text")
    robustness.main()
    assert (tmp_path / "report.md").read_text() == "rendered text"
    assert capsys.readouterr().out.strip() == "report.md"


def _patched_load(monkeypatch, name, edit):
    """Make `robustness.load(name)` return the real cache after `edit` has altered it."""
    real = robustness.load

    def load(requested):
        """Return the real cache for `requested`, edited in place when it is the named one."""
        data = real(requested)
        if requested == name:
            edit(data)
        return data

    monkeypatch.setattr(robustness, "load", load)


def test_robustness_refuses_an_incomplete_cache(monkeypatch):
    """Check that `render` fails on a cache that is still running.

    A report built from an unfinished cache would present partial results as final.
    """
    _patched_load(monkeypatch, "sobol.json", lambda d: d["meta"].update(status="running"))
    with pytest.raises(AssertionError, match=r"sobol\.json incomplete"):
        robustness.render()


def test_robustness_refuses_a_cache_keyed_to_another_model(monkeypatch):
    """Check that `render` fails on a cache keyed to another model.

    Caches are keyed to the canonical model, so a cache from another model must not feed the
    report.
    """
    _patched_load(monkeypatch, "mc_error.json",
                  lambda d: d["meta"].update(model_sha256="0" * 64))
    with pytest.raises(AssertionError, match=r"mc_error\.json model hash"):
        robustness.render()


def test_robustness_insists_on_four_hundred_structural_seeds(monkeypatch):
    """Delete one structural-cache entry and require `render` to fail its seed-count assertion.

        The confirmatory rule is 400 seeds, so a short cache must stop the report rather than be
    summarised.
    """
    def drop_one(data):
        """Delete one non-meta entry so the structural cache is a seed short."""
        victim = next(k for k in data if k != "meta")
        del data[victim]

    _patched_load(monkeypatch, "structural.json", drop_one)
    with pytest.raises(AssertionError):
        robustness.render()


# ------------------------------------------------------------- inventory_model_choices

SNIPPET = """
S = [[0, 3]]
GOV = [[0.5]]
DEFAULTS = {"x": 2}
NSTEP = 7
limit: int = 9
flag = True


def effective_adherence(): return 1.5
def resources(): return 2.5
def step_growth(): return 3.5
def simulate(): return 4.5
def helper(): return 5.5
"""


def test_inventory_visitor_classifies_by_assignment_then_function():
    """Pin how the inventory visitor categorises numeric literals.

    This pins the classification rules (structural zeros, registered values, named function maps,
    implementation constants) and that booleans are not counted as numbers.
    """
    import ast

    visitor = inventory.Visitor()
    visitor.visit(ast.parse(SNIPPET))
    by_value = {(r["value"], r["assignment"], r["function"]): r["category"] for r in visitor.rows}
    assert by_value[(0, "S", None)] == "authored structural zero"
    assert by_value[(3, "S", None)] == "registered sensitivity value"
    assert by_value[(0.5, "GOV", None)] == "registered sensitivity value"
    assert by_value[(2, "DEFAULTS", None)] == "registered sensitivity value"
    assert by_value[(7, "NSTEP", None)] == "fixed model or analysis choice"
    assert by_value[(9, "limit", None)] == "implementation, derived, or numerical constant"
    assert by_value[(1.5, None, "effective_adherence")].endswith("protective-adherence map")
    assert by_value[(2.5, None, "resources")].endswith("resource capacity")
    assert by_value[(3.5, None, "step_growth")].endswith("state-update map")
    assert by_value[(4.5, None, "simulate")] == "fixed experiment or population-process choice"
    assert by_value[(5.5, None, "helper")].startswith("implementation")
    assert all(not isinstance(r["value"], bool) for r in visitor.rows)   # `True` is not a number


def test_inventory_registered_set_is_the_118_decomposition():
    """Pin the 118-value registered set and its 22 + 12 + 49 + 35 split.

    This guards the headline count the project quotes, so a change to the model cannot go
    unnoticed in the inventory.
    """
    data = inventory.build()
    registered = data["registered_set"]
    assert registered["total"] == 118
    assert (registered["scalar_defaults"], registered["step_speeds"],
            registered["S_nonzero_cells"], registered["GOV_nonzero_cells"]) == (22, 12, 49, 35)
    assert data["model_sha256"] == inventory.sha(inventory.MODEL)
    text = inventory.markdown(data)
    assert "exactly **118 numeric values**" in text


def test_inventory_main_writes_to_the_redirected_paths_and_keeps_its_timestamp(
        tmp_path, monkeypatch):
    """Check inventory output paths and that unchanged content keeps its timestamp.

    Rewriting identical content with a fresh timestamp would dirty the tree on every run.
    """
    json_out, md_out = tmp_path / "inv.json", tmp_path / "inv.md"
    monkeypatch.setattr(inventory, "JSON_OUT", json_out)
    monkeypatch.setattr(inventory, "MD_OUT", md_out)
    assert inventory.unchanged_apart_from_timestamp(inventory.build()) is None   # no file yet
    inventory.main()
    first = json.loads(json_out.read_text())
    inventory.main()
    second = json.loads(json_out.read_text())
    assert second["created_utc"] == first["created_utc"]       # unchanged content, same stamp
    assert md_out.read_text() == inventory.markdown(second)

    moved = dict(second, model_sha256="0" * 64)
    assert inventory.unchanged_apart_from_timestamp(moved) is None   # content moved

    json_out.write_text("{not json")
    assert inventory.unchanged_apart_from_timestamp(second) is None  # unreadable: stamp anew


# ------------------------------------------------------------------------- build_corpus

CHECK_BOOK = """\
SUBJECTS = [
    'sheer survival value',  # the book's most-cited source
    'group conscience', ' , ',
    'rotating leadership',
]
OTHER = ['not a subject']
"""

LEDGER = """\
# Sources

**Blair, J. (1888).** *The temperance movement.* Boston: Publisher.
Reprint note on the second line.
**Saved:** the scan as `blair-1888-the-temperance-movement.txt`.

An unrelated paragraph.
"""


def load_corpus_tool(tmp_path, monkeypatch):
    """Import a private copy of build_corpus with every path constant inside `tmp_path`."""
    spec = importlib.util.spec_from_file_location("nic_report_build_corpus",
                                                  ROOT / "tools" / "build_corpus.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    (root / "tools").mkdir(parents=True)
    (root / "tools" / "check_book.py").write_text(CHECK_BOOK)
    research = root / "research"
    (research / "incorporated").mkdir(parents=True)
    (research / "SOURCES.md").write_text(LEDGER)
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "RESEARCH", research)
    monkeypatch.setattr(module, "INCORP", research / "incorporated")
    monkeypatch.setattr(module, "is_withheld", fake_is_withheld)
    return module


@pytest.fixture
def corpus(tmp_path, monkeypatch):
    """Provide a private `build_corpus` module whose paths all lie under `tmp_path`.

    Every corpus test uses it so none can write into the real `research/incorporated/`.
    """
    return load_corpus_tool(tmp_path, monkeypatch)


def run_main(corpus, monkeypatch, *flags):
    """Run the corpus tool's `main` with the given flags and return its exit status.

    It sets `sys.argv` through monkeypatch so the flags are undone after each test.
    """
    monkeypatch.setattr(sys, "argv", ["build_corpus.py", *flags])
    return corpus.main()


def test_corpus_constants_stay_inside_the_temporary_tree(corpus, tmp_path):
    """Check that the fixture's `ROOT`, `RESEARCH` and `INCORP` all sit under `tmp_path`.

        If the monkeypatching ever failed, later tests would write into the real research tree, so
    this fails first.
    """
    for path in (corpus.ROOT, corpus.RESEARCH, corpus.INCORP):
        assert tmp_path in path.parents


def test_sha256_hashes_across_chunk_boundaries(corpus, tmp_path):
    """Check the tool's SHA-256 against `hashlib` for a multi-chunk file.

    This catches an off-by-one when reading in chunks, which would corrupt the stored source
    hashes.
    """
    data = b"x" * (3 * (1 << 20) + 5)
    f = tmp_path / "big.bin"
    f.write_bytes(data)
    assert corpus.sha256(f) == hashlib.sha256(data).hexdigest()


def test_citation_is_lifted_from_the_ledger(corpus):
    """Check that `citation_from_ledger` lifts exactly one ledger entry.

    Citations copied into `citation.md` must be the ledger's own text and no more.
    """
    cite = corpus.citation_from_ledger("blair-1888-the-temperance-movement")
    assert cite.splitlines()[0].startswith("**Blair, J. (1888).**")
    assert "Reprint note on the second line." in cite
    assert "An unrelated paragraph" not in cite              # stops at the blank line
    assert corpus.citation_from_ledger("not-in-the-ledger") is None


def test_citation_needs_a_bold_lead_in_within_forty_lines(corpus):
    """Place a stem sixty lines below any bold lead-in and require no citation to be found.

        This pins the search window so a stem mentioned in passing is not given an unrelated
    entry.
    """
    (corpus.RESEARCH / "SOURCES.md").write_text(
        "plain line\n" * 60 + "see `orphan-stem` here\n")
    assert corpus.citation_from_ledger("orphan-stem") is None


def test_registered_subjects_are_read_from_the_checker(corpus):
    """Check that registered subjects are read from `check_book.py`.

    The index must follow the checker's registry, not a copy that can go stale.
    """
    assert corpus.registered_subjects() == [
        "sheer survival value", "group conscience", "rotating leadership"]
    (corpus.ROOT / "tools" / "check_book.py").write_text("NOTHING = 1\n")
    assert corpus.registered_subjects() == []


def test_fuzzy_in_tolerates_ocr_noise_but_not_absence(corpus):
    """Pin the fuzzy matcher: it forgives OCR noise in long terms but not absence.

    It must forgive OCR noise without reporting subjects the document lacks. Terms of five
    characters or fewer match exactly, so "chose" is never mistaken for "chase".
    """
    blob = "." * 20 + "sheer surviv0l value" + " at length, said the committee"
    assert corpus.fuzzy_in("sheer survival value", blob)               # one-character noise
    assert corpus.fuzzy_in("committee", blob)                          # exact substring
    assert not corpus.fuzzy_in("rotating leadership", blob)
    assert not corpus.fuzzy_in("a term longer than the blob itself", "short")
    assert corpus.fuzzy_in("chase", "a long chase")                     # short term, exact
    assert not corpus.fuzzy_in("chase", "the purchase of coal")         # inside another word
    assert not corpus.fuzzy_in("chase", "she chose it, and left")      # one letter off: refused
    assert not corpus.fuzzy_in("sheer survival value", "z" * 30)       # first letter never occurs
    assert not corpus.fuzzy_in("sheer survival value", "z" * 30 + "sheer surv")  # tail too short


def test_build_index_is_vocabulary_only_and_drops_the_withheld_word(corpus, tmp_path):
    """Check that a built index is vocabulary only and drops the withheld word.

    The index is committed in a public repository, so it must contain no prose and no withheld
    name.
    """
    doc = tmp_path / "doc.txt"
    doc.write_text("The group conscience met now. Sheer surviv0l value, said Vexmoor's friend. "
                   "A b c.\n")
    index = corpus.build_index(doc, "a work", "f" * 64)
    assert index["source_sha256"] == "f" * 64 and index["source_file"] == "doc.txt"
    assert index["work"] == "a work"
    assert index["words"] == len(doc.read_text().split())
    assert "conscience" in index["vocab"]
    assert "a" not in index["vocab"]                          # single characters dropped
    assert "vexmoor's" not in index["vocab"]                  # the possessive of a withheld word
    assert not [t for t in index["vocab"] if INVENTED in t]
    assert index["subjects_present"] == ["group conscience", "sheer survival value"]
    assert index["subjects_checked"] == sorted(
        ["sheer survival value", "group conscience", "rotating leadership"])
    assert "Vexmoor" not in json.dumps(index)


def test_ensure_dir_creates_nested_directories(corpus):
    """Check that `ensure_dir` creates the directory and is idempotent.

    Normalization calls it repeatedly, so it must be idempotent.
    """
    made = corpus.ensure_dir("New_2000")
    assert made == corpus.INCORP / "New_2000" and made.is_dir()
    assert corpus.ensure_dir("New_2000") == made             # idempotent


def test_move_falls_back_to_a_plain_move_outside_a_repository(corpus, tmp_path):
    """Move a file when `ROOT` is not a git repository and check a same-path move does nothing.

    Git-ignored documents cannot be `git mv`-ed, so the fallback is what actually moves them.
    """
    src, dst = tmp_path / "a.txt", tmp_path / "b.txt"
    src.write_text("hello")
    corpus.move(src, dst)                                     # ROOT is not a repository
    assert not src.exists() and dst.read_text() == "hello"
    corpus.move(dst, dst)                                     # same path is a no-op
    assert dst.read_text() == "hello"


def test_move_prefers_git_mv_for_a_tracked_file(corpus):
    """Check that `move` uses `git mv` so a tracked file stays tracked.

    That proves tracked files keep their history through `git mv` rather than a plain move that
    would leave them untracked.
    """
    repo = corpus.ROOT
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    src = repo / "tracked.txt"
    src.write_text("hello")
    subprocess.run(["git", "add", "tracked.txt"], cwd=repo, check=True)
    dst = repo / "moved.txt"
    corpus.move(src, dst)
    assert dst.read_text() == "hello" and not src.exists()
    staged = subprocess.run(["git", "status", "--porcelain"], cwd=repo,
                            capture_output=True, text=True, check=True).stdout
    assert "A  moved.txt" in staged        # tracked by git mv; a plain move would be untracked


def test_check_mode_reports_loose_files_and_unrenamed_directories(corpus, monkeypatch, capsys):
    """Check that `--check` reports loose files and unrenamed directories.

    It must also change nothing on disk, since check mode only reports drift.
    """
    (corpus.RESEARCH / "blair-1888-the-temperance-movement.txt").write_text("text")
    (corpus.RESEARCH / "blair-1888-the-temperance-movement.md").write_text("not a document")
    (corpus.INCORP / "AA_Tradition_P17").mkdir()
    (corpus.INCORP / "stray-file.txt").write_text("a file, not a source directory")

    assert run_main(corpus, monkeypatch, "--check") == 1
    out = capsys.readouterr().out
    assert "FAIL: loose document: blair-1888-the-temperance-movement.txt" in out
    assert "FAIL: directory not normalized: AA_Tradition_P17 -> AAWS_2024_P17" in out
    assert ".md" not in out                                    # only document suffixes count
    assert "2 corpus problems" in out
    # Check mode moved nothing and wrote no record into the directory it reported.
    assert (corpus.RESEARCH / "blair-1888-the-temperance-movement.txt").exists()
    assert (corpus.INCORP / "AA_Tradition_P17").is_dir()
    assert not (corpus.INCORP / "AAWS_2024_P17").exists()


def test_build_mode_normalizes_and_writes_the_record(corpus, monkeypatch, capsys):
    """Check that build mode normalizes the layout and writes each record.

    This is the end-to-end contract for what the corpus builder commits and what it leaves out.
    """
    (corpus.RESEARCH / "blair-1888-the-temperance-movement.txt").write_text(
        "The group conscience met. Vexmoor spoke.\n")
    (corpus.INCORP / "AA_Tradition_P17").mkdir()
    (corpus.INCORP / "AA_Tradition_P17" / "scan.pdf").write_bytes(b"%PDF fake")
    misnamed = corpus.INCORP / "Krout_1925"
    misnamed.mkdir()
    (misnamed / "whatever.DJVU").write_bytes(b"djvu bytes")

    assert run_main(corpus, monkeypatch) == 0
    out = capsys.readouterr().out
    assert "indexes written or refreshed: 1" in out and "  Blair_1888" in out
    assert out.rstrip().endswith("corpus normalized")

    blair = corpus.INCORP / "Blair_1888"
    assert (blair / "Blair_1888.txt").exists()
    assert not (corpus.RESEARCH / "blair-1888-the-temperance-movement.txt").exists()
    citation = (blair / "citation.md").read_text()
    assert citation.startswith("# Citation\n\n**Blair, J. (1888).**")
    assert "Copied from `research/SOURCES.md`" in citation

    meta = json.loads((blair / "metadata.json").read_text())
    assert meta["id"] == "Blair_1888"
    assert meta["legacy_stem"] == "blair-1888-the-temperance-movement"
    assert meta["rights_note"] == corpus.DEFAULT_RIGHTS
    assert meta["documents"]["Blair_1888.txt"]["tracked_in_git"] is False
    digest = hashlib.sha256((blair / "Blair_1888.txt").read_bytes()).hexdigest()
    assert meta["documents"]["Blair_1888.txt"]["sha256"] == digest

    index = json.loads((blair / "Blair_1888_verification-index.json").read_text())
    assert index["source_sha256"] == digest
    assert index["work"].startswith("Blair, J. (1888). The temperance movement.")
    assert not [t for t in index["vocab"] if INVENTED in t]

    # Renamed directory, its document kept, a named rights note, and no text index (a PDF).
    p17 = corpus.INCORP / "AAWS_2024_P17"
    assert (p17 / "AAWS_2024_P17.pdf").exists()
    p17_meta = json.loads((p17 / "metadata.json").read_text())
    assert "Copyrighted AAWS literature" in p17_meta["rights_note"]
    assert not list(p17.glob("*verification-index.json"))

    assert (misnamed / "Krout_1925.djvu").exists() and not (misnamed / "whatever.DJVU").exists()
    krout = json.loads((misnamed / "metadata.json").read_text())
    assert krout["rights_note"] == corpus.RIGHTS["Krout_1925"]


def test_a_second_run_changes_nothing(corpus, monkeypatch, capsys):
    """Check that a second build changes nothing and `--check` then passes.

    A non-idempotent build would dirty the tree on every run and hide real drift.
    """
    (corpus.RESEARCH / "blair-1888-the-temperance-movement.txt").write_text("Some text here.\n")
    assert run_main(corpus, monkeypatch) == 0

    def snapshot():
        """Map each file under the corpus to its bytes, to compare before and after a rebuild."""
        return {str(p.relative_to(corpus.INCORP)): p.read_bytes()
                for p in sorted(corpus.INCORP.rglob("*")) if p.is_file()}

    before = snapshot()
    capsys.readouterr()
    assert run_main(corpus, monkeypatch) == 0
    assert "indexes written or refreshed: 0" in capsys.readouterr().out
    assert snapshot() == before
    assert run_main(corpus, monkeypatch, "--check") == 0
    assert "0 corpus problems" in capsys.readouterr().out


def test_existing_metadata_is_kept_and_an_unknown_rights_note_survives(corpus, monkeypatch):
    """Check that existing metadata and an unknown rights note survive a build.

    The builder must not overwrite rights decisions the Human Author has recorded.
    """
    source = corpus.INCORP / "Unlisted_2001"
    source.mkdir()
    (source / "metadata.json").write_text(json.dumps(
        {"id": "custom-id", "rights_note": "Author permission on file.", "url": "https://x.test"}))
    assert run_main(corpus, monkeypatch) == 0
    meta = json.loads((source / "metadata.json").read_text())
    assert meta["id"] == "custom-id" and meta["url"] == "https://x.test"
    assert meta["rights_note"] == "Author permission on file."
    assert meta["legacy_stem"] is None and meta["documents"] == {}


def _source_with_index(corpus, name="Held_2002", text="alpha beta gamma\n"):
    """Create a source holding one text document and return its index path.

    The index itself is not written, so each test controls when it is built.
    """
    source = corpus.INCORP / name
    source.mkdir()
    (source / f"{name}.txt").write_text(text)
    return source, source / f"{name}_verification-index.json"


def test_a_stale_or_corrupt_index_is_flagged_and_then_rebuilt(corpus, monkeypatch, capsys):
    """Check that stale or corrupt indexes are flagged, then rebuilt only in build mode.

    This is how a re-acquired document is kept from verifying citations against an old vocabulary.
    """
    source, index = _source_with_index(corpus)
    assert run_main(corpus, monkeypatch, "--check") == 1       # no index yet
    assert "verification index missing or stale: Held_2002" in capsys.readouterr().out
    assert not index.exists()

    assert run_main(corpus, monkeypatch) == 0
    good = index.read_text()
    assert json.loads(good)["vocab"] == ["alpha", "beta", "gamma"]

    (source / "Held_2002.txt").write_text("alpha beta delta\n")  # the document was re-acquired
    assert run_main(corpus, monkeypatch, "--check") == 1
    assert "verification index missing or stale: Held_2002" in capsys.readouterr().out
    assert index.read_text() == good                            # check mode did not rebuild

    index.write_text("{not json")                               # unreadable counts as stale
    assert run_main(corpus, monkeypatch) == 0
    assert json.loads(index.read_text())["vocab"] == ["alpha", "beta", "delta"]


def test_work_label_comes_from_the_citation_or_falls_back_to_the_directory(
        corpus, monkeypatch):
    """Check how an index's `work` label is derived from the citation.

    The label must be short and stable, whatever shape the citation file has.
    """
    source, index = _source_with_index(corpus)
    (source / "citation.md").write_text("# Citation, with no blank line anywhere")
    assert run_main(corpus, monkeypatch) == 0
    assert json.loads(index.read_text())["work"] == "Held_2002"       # one block: no work line

    index.unlink()
    (source / "citation.md").write_text("# Citation\n\n**Bold** `code` line\nwrapped.\n\nTail.\n")
    assert run_main(corpus, monkeypatch) == 0
    assert json.loads(index.read_text())["work"] == "Bold code line wrapped."

    index.unlink()
    (source / "citation.md").write_text("# Citation\n\n" + "w" * 400 + "\n\nTail.\n")
    assert run_main(corpus, monkeypatch) == 0
    assert json.loads(index.read_text())["work"] == "w" * 300         # capped


def test_a_withheld_word_is_flagged_in_check_mode_and_stripped_in_build_mode(
        corpus, monkeypatch, capsys):
    """Check that a withheld word is flagged by `--check` and stripped by a build.

    A committed vocabulary publishes every word in it, so a withheld name must be both detectable
    and removable.
    """
    source = corpus.INCORP / "Record_2000"
    source.mkdir()
    index = source / "Record_2000_verification-index.json"
    record = {"work": "w", "source_sha256": "0" * 64, "vocab": ["alpha", INVENTED, "zeta"]}
    index.write_text(json.dumps(record) + "\n")

    assert run_main(corpus, monkeypatch, "--check") == 1
    assert "verification index lists a withheld name: Record_2000" in capsys.readouterr().out
    assert json.loads(index.read_text()) == record

    assert run_main(corpus, monkeypatch) == 0
    assert "  Record_2000" in capsys.readouterr().out
    assert json.loads(index.read_text())["vocab"] == ["alpha", "zeta"]
    assert INVENTED not in index.read_text()


def test_the_three_statements_of_footing_must_agree(corpus, monkeypatch, capsys):
    """Check that `--check` flags disagreement between the statements of footing.

    Build mode must neither report nor repair them, since the footing is the Human Author's
    decision.
    """
    holds = corpus.INCORP / "Holds_2003"
    holds.mkdir()
    (holds / "Holds_2003.pdf").write_bytes(b"%PDF")
    (holds / "metadata.json").write_text(json.dumps({"record_only": True}))

    claims = corpus.INCORP / "Claims_2004"
    claims.mkdir()
    (claims / "source_summary.md").write_text("**Record only.** No document is stored.\n")

    quoted = corpus.INCORP / "Quoted_2005"
    quoted.mkdir()
    (quoted / "source_summary.md").write_text("Intro.\n\nThe phrase **Record only** is quoted.\n")

    consistent = corpus.INCORP / "Consistent_2006"
    consistent.mkdir()
    (consistent / "metadata.json").write_text(json.dumps({"record_only": True}))
    (consistent / "source_summary.md").write_text("**Record only.** Nothing is held.\n")

    assert run_main(corpus, monkeypatch, "--check") == 1
    out = capsys.readouterr().out
    assert "FAIL: record-only source holds a document: Holds_2003" in out
    assert "FAIL: summary opens as record only but metadata does not: Claims_2004" in out
    assert "Quoted_2005" not in out and "Consistent_2006" not in out
    assert "2 corpus problems" in out

    # A build run neither reports nor repairs them: only `--check` prints problems.
    assert run_main(corpus, monkeypatch) == 0
    assert (holds / "Holds_2003.pdf").exists()


def test_an_unreadable_index_on_a_record_only_source_is_reported_not_raised(
        corpus, monkeypatch, capsys):
    """Check that a record-only source with a corrupt index is reported instead of crashing.

    A record-only source has no document to rebuild from, so the withheld-name pass is the only
    thing that reads its index; it used to raise on malformed JSON, which hid every other
    problem in the run.
    """
    source = corpus.INCORP / "Record_2000"
    source.mkdir()
    (source / "Record_2000_verification-index.json").write_text("{not json")

    assert run_main(corpus, monkeypatch, "--check") == 1
    assert "verification index is not valid JSON: Record_2000" in capsys.readouterr().out


def test_index_is_stale_for_a_changed_hash_or_an_unrecorded_subject(corpus):
    """Check `index_is_stale` against a changed hash and against a missing or extra subject.

    An index must be refused when its document was re-acquired, or when a subject was
    registered after it was built; a subject registered and since removed must not matter.
    """
    subjects = ["group conscience", "rotating leadership"]
    index = {"source_sha256": "a" * 64, "subjects_checked": list(subjects)}
    assert not corpus.index_is_stale(index, "a" * 64, subjects)
    assert corpus.index_is_stale(index, "b" * 64, subjects)                # hash differs
    assert corpus.index_is_stale(index, "a" * 64, [*subjects, "new subject"])   # not recorded
    assert not corpus.index_is_stale(index, "a" * 64, subjects[:1])        # extra is harmless
    assert corpus.index_is_stale({"source_sha256": "a" * 64}, "a" * 64, subjects)  # none at all


def test_an_index_that_omits_a_registered_subject_is_flagged_then_rebuilt(
        corpus, monkeypatch, capsys):
    """Check that an index built before a subject was registered is reported and rebuilt.

    The document is unchanged, so the hash still matches; only the subject list is out of date.
    `--check` must report it without writing, and a build must refresh it.
    """
    _source, index = _source_with_index(corpus, text="the group conscience met\n")
    assert run_main(corpus, monkeypatch) == 0
    record = json.loads(index.read_text())
    assert record["subjects_present"] == ["group conscience"]

    record["subjects_checked"].remove("rotating leadership")           # registered later
    index.write_text(json.dumps(record) + "\n")
    older = index.read_text()
    capsys.readouterr()
    assert run_main(corpus, monkeypatch, "--check") == 1
    assert "verification index missing or stale: Held_2002" in capsys.readouterr().out
    assert index.read_text() == older                                  # check mode wrote nothing

    assert run_main(corpus, monkeypatch) == 0
    assert "  Held_2002" in capsys.readouterr().out
    assert "rotating leadership" in json.loads(index.read_text())["subjects_checked"]
    assert run_main(corpus, monkeypatch, "--check") == 0


def test_neither_mode_creates_an_empty_directory_for_a_registered_source(
        corpus, monkeypatch):
    """Check that no directory is created for a registered source that has no document.

    `--check` promises to change nothing, and a build has nothing to put in such a directory.
    """
    assert run_main(corpus, monkeypatch, "--check") == 0
    assert list(corpus.INCORP.iterdir()) == []
    assert run_main(corpus, monkeypatch) == 0
    assert list(corpus.INCORP.iterdir()) == []


def test_the_documents_note_does_not_promise_a_url_for_every_source(corpus, monkeypatch):
    """Check that the generated `documents_note` also points to SOURCES.md for sources with no URL.

    Some sources record no URL, so the note must not say every one has a recorded URL.
    """
    source = corpus.INCORP / "NoUrl_2001"
    source.mkdir()
    assert run_main(corpus, monkeypatch) == 0
    note = json.loads((source / "metadata.json").read_text())["documents_note"]
    assert "research/SOURCES.md" in note and "where no URL is recorded" in note


def test_grosh_is_not_described_as_an_internet_archive_scan(corpus, monkeypatch):
    """Check that the Grosh rights note names its HathiTrust provenance, not the default.

    The default asserts an Internet Archive scan, which is false for this Google-digitised copy.
    """
    source = corpus.INCORP / "Grosh_1842"
    source.mkdir()
    assert run_main(corpus, monkeypatch) == 0
    note = json.loads((source / "metadata.json").read_text())["rights_note"]
    assert "HathiTrust" in note and "Internet Archive" not in note


def test_a_typographic_apostrophe_makes_the_same_token_as_a_straight_one(corpus, tmp_path):
    """Check that a typographic apostrophe yields the straight-apostrophe token.

    A source set in curly quotes must not lose "book's" to a split into "book" and a dropped
    single letter, or its vocabulary would differ from the same text in straight quotes.
    """
    doc = tmp_path / "curly.txt"
    curly = "\N{RIGHT SINGLE QUOTATION MARK}"
    doc.write_text(f"The book{curly}s co-founder won{curly}t say.\n")
    vocab = corpus.build_index(doc, "a work", "f" * 64)["vocab"]
    assert "book's" in vocab and "won't" in vocab and "co-founder" in vocab
    assert not [t for t in vocab if curly in t]
