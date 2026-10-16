"""Direct tests of seven tools and the local CI runner, which the integration tests reach only through the gate.

`tests/test_tools_integration.py` runs the tools as commands. These import them and call their
functions, with every output redirected into a temporary directory, so that a branch that the
real repository never takes (a corrupt PDF, an incomplete cache, a note with the wrong shape)
is exercised on purpose rather than discovered when it happens. Nothing here writes into the
repository. None of it is in the coverage gate, which is the canonical model; see `.coveragerc`.
"""
from __future__ import annotations

import ast
import hashlib
import json
import shutil
import subprocess
import sys
import types
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import build_note  # noqa: E402
import check_docs  # noqa: E402
import check_fonts  # noqa: E402
import check_pdfs  # noqa: E402
import freeze_release_manifest as freeze  # noqa: E402
import inventory_model_choices as inventory  # noqa: E402
import summarize_release_gate as gate  # noqa: E402


# ----------------------------------------------------------------- freeze_release_manifest

def test_digest_is_the_sha256_of_the_file(tmp_path):
    f = tmp_path / "x.bin"
    f.write_bytes(b"abc" * 1_000_000)          # larger than the one-megabyte read block
    assert freeze.digest(f) == hashlib.sha256(b"abc" * 1_000_000).hexdigest()


def test_json_shape_describes_without_copying(tmp_path):
    d = tmp_path / "d.json"
    d.write_text(json.dumps({"meta": 1, "result": 2, "12|3": 4, "a_b": 5}))
    shape = freeze.json_shape(d)
    assert shape["valid"] and shape["type"] == "dict"
    assert shape["top_level_keys"] == 4 and shape["numeric_job_keys"] == 1
    assert shape["has_meta"] and shape["has_result"]

    lst = tmp_path / "l.json"
    lst.write_text("[1, 2, 3]")
    assert freeze.json_shape(lst) == {"valid": True, "type": "list", "length": 3}

    bad = tmp_path / "b.json"
    bad.write_text("{not json")
    shape = freeze.json_shape(bad)
    assert shape["valid"] is False and shape["error"].startswith("JSONDecodeError")


def _fake_tree(root: Path) -> None:
    for rel, text in {
        "model/a.py": "x = 1\n",
        "model/cache.json": '{"meta": {}}',
        "model/notes.txt": "excluded suffix",
        "tools/__pycache__/skipped.py": "skipped part",
        "research/staged/skipped.md": "skipped part",
        "research/log.md": "included",
        "research/data.csv": "excluded suffix",
        "README.md": "top level, named",
        "OTHER.md": "top level, not named",
    }.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)


def test_included_follows_the_inventory_rules(tmp_path, monkeypatch):
    monkeypatch.setattr(freeze, "ROOT", tmp_path)
    _fake_tree(tmp_path)
    keep = {rel for rel in ("model/a.py", "model/cache.json", "research/log.md", "README.md")}
    drop = {"model/notes.txt", "tools/__pycache__/skipped.py", "research/staged/skipped.md",
            "research/data.csv", "OTHER.md"}
    assert all(freeze.included(tmp_path / r) for r in keep)
    assert not any(freeze.included(tmp_path / r) for r in drop)


def test_build_and_main_write_a_repository_relative_manifest(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(freeze, "ROOT", tmp_path)
    _fake_tree(tmp_path)
    (tmp_path / "research").mkdir(exist_ok=True)

    manifest = freeze.build("pre-correction")
    assert manifest["path_semantics"] == "repository-relative"
    assert manifest["project_root"] == "." and manifest["file_count"] == 4
    assert manifest["files"]["model/cache.json"]["json"]["valid"] is True
    assert str(tmp_path) not in json.dumps(manifest)

    explicit = tmp_path / "out.json"
    monkeypatch.setattr(sys, "argv", ["freeze", "post-correction", "--output", str(explicit)])
    assert freeze.main() == 0
    assert json.loads(explicit.read_text())["label"] == "post-correction"
    assert not explicit.with_suffix(".json.tmp").exists()

    monkeypatch.setattr(sys, "argv", ["freeze", "pre-correction"])
    assert freeze.main() == 0
    assert (tmp_path / "research" / "audit-pre-correction-manifest.json").exists()
    assert "wrote" in capsys.readouterr().out


# -------------------------------------------------------------------------- check_pdfs

@pytest.fixture
def clean_pdf_state(monkeypatch):
    for name in ("failures", "notes", "skips"):
        monkeypatch.setattr(check_pdfs, name, [])


class _Obj(dict):
    """A dict that answers get_object() with itself, like a pypdf indirect reference."""

    def get_object(self):
        return self


def test_require_sorts_into_notes_and_failures(clean_pdf_state):
    check_pdfs.require(True, "fine")
    check_pdfs.require(False, "broken")
    assert check_pdfs.notes == ["OK: fine"] and check_pdfs.failures == ["FAIL: broken"]


def test_embedded_looks_for_a_glyph_program(clean_pdf_state):
    with_program = _Obj({"/FontDescriptor": _Obj({"/FontFile2": 1})})
    without = _Obj({"/FontDescriptor": _Obj({"/FontName": "x"})})
    none_at_all = _Obj({})
    composite = _Obj({"/DescendantFonts": [_Obj({"/FontDescriptor": _Obj({"/FontFile3": 1})})]})
    assert check_pdfs.embedded(with_program) is True
    assert check_pdfs.embedded(without) is False
    assert check_pdfs.embedded(none_at_all) is False
    assert check_pdfs.embedded(composite) is True


def _bbox(*extents):
    pages = "".join(f'<page><word xMin="{lo}" xMax="{hi}"/></page>' for lo, hi in extents)
    return types.SimpleNamespace(stdout=pages + "<page></page>")


def test_ink_check_skips_without_poppler(clean_pdf_state, monkeypatch):
    monkeypatch.setattr(check_pdfs.shutil, "which", lambda _name: None)
    check_pdfs.check_ink(Path("x.pdf"), "x.pdf")
    assert check_pdfs.skips and check_pdfs.skips[0].startswith("SKIP: x.pdf")
    assert not check_pdfs.notes and not check_pdfs.failures


def test_ink_check_passes_and_breaches(clean_pdf_state, monkeypatch):
    monkeypatch.setattr(check_pdfs.shutil, "which", lambda _name: "/usr/bin/pdftotext")
    monkeypatch.setattr(check_pdfs.subprocess, "run", lambda *a, **k: _bbox((72, 500), (80, 510)))
    check_pdfs.check_ink(Path("x.pdf"), "x.pdf")
    assert check_pdfs.notes and "closest" in check_pdfs.notes[0] and not check_pdfs.failures

    monkeypatch.setattr(check_pdfs.subprocess, "run",
                        lambda *a, **k: _bbox((72, 500), (5, 510), (72, 590)))
    check_pdfs.check_ink(Path("x.pdf"), "x.pdf")
    assert check_pdfs.failures and "breached on pages [2, 3]" in check_pdfs.failures[0]


def test_check_reports_a_missing_file(clean_pdf_state, monkeypatch, tmp_path):
    monkeypatch.setattr(check_pdfs, "ROOT", tmp_path)
    check_pdfs.check("absent/doc.pdf", 1)
    assert check_pdfs.failures == ["FAIL: doc.pdf: exists"]


def test_check_reports_a_file_that_is_not_a_pdf(clean_pdf_state, monkeypatch, tmp_path):
    (tmp_path / "bad.pdf").write_bytes(b"this is not a pdf" * 100)
    monkeypatch.setattr(check_pdfs, "ROOT", tmp_path)
    check_pdfs.check("bad.pdf", 1)
    assert len(check_pdfs.failures) == 1 and "parses as a PDF" in check_pdfs.failures[0]


def test_check_reports_a_blank_page_of_the_wrong_size(clean_pdf_state, monkeypatch, tmp_path):
    pypdf = pytest.importorskip("pypdf")
    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=300, height=300)
    with (tmp_path / "blank.pdf").open("wb") as fh:
        writer.write(fh)
    monkeypatch.setattr(check_pdfs, "ROOT", tmp_path)
    monkeypatch.setattr(check_pdfs.shutil, "which", lambda _name: None)
    check_pdfs.check("blank.pdf", 2)
    failed = " | ".join(check_pdfs.failures)
    assert "floor is 2" in failed and "page size is A4" in failed and "text extractable" in failed
    assert any("all 0 fonts embedded" in n for n in check_pdfs.notes)
    assert check_pdfs.skips


def test_check_passes_the_committed_paper(clean_pdf_state):
    paper = ROOT / "paper" / "anonymity-as-an-aggregation-condition.pdf"
    if not paper.exists():
        pytest.skip("the paper is not built here")
    check_pdfs.check("paper/anonymity-as-an-aggregation-condition.pdf", 20)
    assert check_pdfs.failures == []
    assert any("fonts embedded" in n for n in check_pdfs.notes)


def test_main_counts_passes_failures_and_skips(clean_pdf_state, monkeypatch, capsys):
    monkeypatch.setattr(check_pdfs, "DOCUMENTS", {})
    assert check_pdfs.main() == 0
    assert "0 checks passed; 0 failed" in capsys.readouterr().out

    check_pdfs.notes.append("OK: one")
    check_pdfs.skips.append("SKIP: two")
    check_pdfs.failures.append("FAIL: three")
    assert check_pdfs.main() == 1
    assert "1 checks passed; 1 failed; 1 skipped" in capsys.readouterr().out


def test_main_names_the_missing_dependency(monkeypatch):
    monkeypatch.setitem(sys.modules, "pypdf", None)             # makes `import pypdf` fail
    with pytest.raises(SystemExit) as stop:
        check_pdfs.main()
    assert "pypdf is required" in str(stop.value)


# -------------------------------------------------------------------------- build_note

NOTE = """# Short title: the rest of it

*Written on 3 October 2026*

## First section

Some text.

---

## Second section

| Page | Item | Note |
|---|---|---|
| 1 | a | b |
| 2 | c | d |
"""


def test_prepare_returns_scratch_markdown_and_the_running_head():
    markdown, title, short, when = build_note.prepare(NOTE)
    assert title == "Short title: the rest of it" and short == "Short title"
    assert when == "3 October 2026"
    assert markdown.startswith("---\ntitle: ") and "\ndate: " in markdown
    assert "\n---\n\n## Second section" not in markdown.split("---\n", 2)[2].replace("\n\n\n", "\n\n")
    assert build_note.WEIGHTED in markdown
    # The table is kept with its heading, not split from it.
    heading = markdown.index("## Second section")
    assert 0 < markdown.index("\\needspace{") < markdown.index(build_note.WEIGHTED)
    assert markdown.index("\\needspace{") < heading


def test_prepare_keeps_a_table_with_its_header_row_when_no_heading_leads_in():
    note = NOTE.replace("## Second section\n\n", "Text before the table.\n\n")
    note = note.replace("---\n\nText before", "---\n\n## Third section\n\nText before")
    markdown, *_ = build_note.prepare(note)
    assert markdown.index("\\needspace{") < markdown.index(build_note.WEIGHTED)


@pytest.mark.parametrize("bad, reason", [
    ("no title here\n\n*x*\n\nbody\n", "does not open with a title"),
    ("# T: x\nnot blank\n*Dated 3 October 2026*\n\nok\n", "does not open with a title"),
    ("# NoColon\n\n*Dated 3 October 2026*\n\n## S\n\n" + build_note.WEIGHTED + "\n", "unexpected title"),
    ("# T: x\n\n*No date here*\n\n## S\n\nbody\n", "unexpected title"),
    ("# T: x\n\nDated 3 October 2026\n\n## S\n\nbody\n", "unexpected title"),
])
def test_prepare_refuses_a_note_with_the_wrong_opening(bad, reason):
    with pytest.raises(SystemExit) as stop:
        build_note.prepare(bad)
    assert reason in str(stop.value)


def test_prepare_refuses_a_rule_that_does_not_open_a_section():
    note = NOTE.replace("---\n\n## Second section", "---\n\nplain text\n\n## Second section")
    with pytest.raises(SystemExit) as stop:
        build_note.prepare(note)
    assert "a rule that does not open a section" in str(stop.value)


def test_prepare_requires_exactly_one_three_column_table():
    with pytest.raises(SystemExit) as stop:
        build_note.prepare(NOTE.split("| Page")[0])
    assert "found 0" in str(stop.value)
    with pytest.raises(SystemExit) as stop:
        build_note.prepare(NOTE + "\n" + NOTE.split("## Second section\n\n")[1])
    assert "found 2" in str(stop.value)


def _point_note_at(monkeypatch, tmp_path, text=NOTE):
    src = tmp_path / "note.md"
    src.write_text(text)
    monkeypatch.setattr(build_note, "SRC", src)
    monkeypatch.setattr(build_note, "OUT", ROOT / "build" / "scratch-note-test.pdf")
    return src


def _fake_pandoc(returncode, output):
    def run(cmd, **kwargs):
        assert cmd[0] == "pandoc" and "--pdf-engine=tectonic" in cmd
        assert any(a.startswith("title-meta=") for a in cmd)
        return types.SimpleNamespace(returncode=returncode, stdout=output, stderr="")
    return run


def test_main_refuses_without_the_note_or_an_engine(monkeypatch, tmp_path):
    monkeypatch.setattr(build_note, "SRC", tmp_path / "absent.md")
    with pytest.raises(SystemExit) as stop:
        build_note.main()
    assert "note not found" in str(stop.value)

    _point_note_at(monkeypatch, tmp_path)
    monkeypatch.setattr(build_note.shutil, "which", lambda _name: None)
    with pytest.raises(SystemExit) as stop:
        build_note.main()
    assert "no PDF engine found" in str(stop.value)


def test_main_reports_a_clean_build_and_an_overfull_one(monkeypatch, tmp_path, capsys):
    _point_note_at(monkeypatch, tmp_path)
    monkeypatch.setattr(build_note, "ROOT", tmp_path)
    monkeypatch.setattr(build_note, "OUT", tmp_path / "out" / "note.pdf")
    monkeypatch.setattr(build_note.shutil, "which",
                        lambda name: "/bin/tectonic" if name == "tectonic" else None)

    monkeypatch.setattr(build_note.subprocess, "run", _fake_pandoc(0, "fine\n"))
    assert build_note.main() == 0
    assert "overfull boxes: 0" in capsys.readouterr().out

    monkeypatch.setattr(build_note.subprocess, "run",
                        _fake_pandoc(0, "Overfull \\hbox (3pt too wide)\n"))
    assert build_note.main() == 0
    out = capsys.readouterr().out
    assert "overfull boxes: 1" in out and "WARNING" in out and "Overfull" in out.split("WARNING")[1]


def test_main_shows_the_lines_that_name_a_failure(monkeypatch, tmp_path, capsys):
    _point_note_at(monkeypatch, tmp_path)
    monkeypatch.setattr(build_note, "OUT", tmp_path / "note.pdf")
    monkeypatch.setattr(build_note.shutil, "which",
                        lambda name: "/bin/tectonic" if name == "tectonic" else None)

    monkeypatch.setattr(build_note.subprocess, "run",
                        _fake_pandoc(1, "chatter\n! Undefined control sequence.\nmore\n"))
    with pytest.raises(SystemExit) as stop:
        build_note.main()
    assert "pandoc failed" in str(stop.value)
    err = capsys.readouterr().err
    assert "! Undefined control sequence." in err and "--- tail ---" in err

    monkeypatch.setattr(build_note.subprocess, "run", _fake_pandoc(1, "only chatter\n"))
    with pytest.raises(SystemExit):
        build_note.main()
    err = capsys.readouterr().err
    assert "only chatter" in err and "--- tail ---" not in err


# ------------------------------------------------------------------ summarize_release_gate

def test_formatters_and_ranks():
    import numpy as np

    assert gate.pct(0.1234) == "12.3%"
    # Exact halves go up, as the book rounds them, and numpy floats are accepted.
    assert gate.pct(0.9925) == "99.3%" and gate.pct(0.9125) == "91.3%"
    assert gate.pct(np.float64(0.9925)) == "99.3%"
    assert gate.ci_mean({"mean": 1, "lo": 0.5, "hi": 1.5}) == "1.000 [0.500, 1.500]"
    assert gate.ci_prop({"proportion": 0.5, "lo": 0.25, "hi": 0.75}) == "50.0% [25.0%, 75.0%]"
    M = np.array([[1.0, 1.0, 0.0], [0.0, 2.0, 1.0], [0.5, 0.2, 0.0]])
    assert gate.top_sets(M) == [[1, 2], [2], [1]]
    assert gate.ranks(M) == [1, 1, 3]            # competition rank: ties share, zeros rank last
    cache = {"meta": {"nseed": 2}, "a|0": {"v": 1}, "a|1": {"v": 2}}
    assert gate.rows(cache, "a") == [{"v": 1}, {"v": 2}]


def test_the_report_regenerates_exactly_as_committed(tmp_path, monkeypatch, capsys):
    out = tmp_path / "RELEASE-GATE-RESULTS.md"
    monkeypatch.setattr(gate, "OUT", out)
    gate.main()
    assert out.read_text() == gate.OUT.read_text()
    assert out.read_text() == (ROOT / "research" / "RELEASE-GATE-RESULTS.md").read_text()
    assert "includes zero, so the clean recipient-capacity ablation is unresolved" in out.read_text()
    assert "wrote" in capsys.readouterr().out


def test_the_report_refuses_an_incomplete_cache(tmp_path, monkeypatch):
    cache = json.loads(gate.CACHE.read_text())
    cache["meta"]["status"] = "running"
    partial = tmp_path / "cache.json"
    partial.write_text(json.dumps(cache))
    monkeypatch.setattr(gate, "CACHE", partial)
    monkeypatch.setattr(gate, "OUT", tmp_path / "never-written.md")
    with pytest.raises(RuntimeError, match="incomplete"):
        gate.main()
    assert not (tmp_path / "never-written.md").exists()


def test_the_report_says_when_the_recipient_interval_excludes_zero(tmp_path, monkeypatch):
    cache = json.loads(gate.CACHE.read_text())
    contrast = cache["summary"]["paired_contrasts"]["recipient_unconstrained_minus_base"]["N"]
    contrast.update(mean=2.0, lo=1.0, hi=3.0)
    changed = tmp_path / "cache.json"
    changed.write_text(json.dumps(cache))
    monkeypatch.setattr(gate, "CACHE", changed)
    monkeypatch.setattr(gate, "OUT", tmp_path / "report.md")
    gate.main()
    text = (tmp_path / "report.md").read_text()
    assert "excludes zero, so the clean recipient-capacity ablation is resolved" in text


# ------------------------------------------------------------- inventory_model_choices

SNIPPET = """
S = [[0, 3]]
GOV = [[0.5]]
DEFAULTS = {"x": 2}
NSTEP = 7
limit: int = 9
other = 11
flag = True
text = "ignored"
def effective_adherence(): return 1.5
def resources(): return 2.5
def step_growth(): return 3.5
def simulate(): return 4.5
def helper(): return 5.5
"""


def test_visitor_classifies_every_kind_of_literal():
    visitor = inventory.Visitor()
    visitor.visit(ast.parse(SNIPPET))
    by_value = {(r["value"], r["assignment"], r["function"]): r["category"] for r in visitor.rows}
    assert by_value[(0, "S", None)] == "authored structural zero"
    assert by_value[(3, "S", None)] == "registered sensitivity value"
    assert by_value[(2, "DEFAULTS", None)] == "registered sensitivity value"
    assert by_value[(7, "NSTEP", None)] == "fixed model or analysis choice"
    assert by_value[(9, "limit", None)] == "implementation, derived, or numerical constant"
    assert by_value[(1.5, None, "effective_adherence")].startswith("fixed structural choice: protective")
    assert by_value[(2.5, None, "resources")].endswith("resource capacity")
    assert by_value[(3.5, None, "step_growth")].endswith("state-update map")
    assert by_value[(4.5, None, "simulate")] == "fixed experiment or population-process choice"
    assert by_value[(5.5, None, "helper")].startswith("implementation")
    assert not any(isinstance(r["value"], (bool, str)) for r in visitor.rows)


def test_the_registered_set_is_the_118_and_the_markdown_says_so():
    data = inventory.build()
    reg = data["registered_set"]
    assert (reg["scalar_defaults"], reg["step_speeds"],
            reg["S_nonzero_cells"], reg["GOV_nonzero_cells"], reg["total"]) == (22, 12, 49, 35, 118)
    assert data["model_sha256"] == hashlib.sha256(inventory.MODEL.read_bytes()).hexdigest()
    text = inventory.markdown(data)
    assert "exactly **118 numeric values**" in text and "| Category |" in text


def test_timestamp_is_kept_while_the_content_is_unchanged(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(inventory, "JSON_OUT", tmp_path / "inv.json")
    monkeypatch.setattr(inventory, "MD_OUT", tmp_path / "inv.md")
    data = inventory.build()
    assert inventory.unchanged_apart_from_timestamp(data) is None       # no file yet

    inventory.main()
    first = json.loads((tmp_path / "inv.json").read_text())
    inventory.main()
    second = json.loads((tmp_path / "inv.json").read_text())
    assert first == second                                              # same stamp, same bytes
    assert (tmp_path / "inv.md").read_text() == inventory.markdown(second)
    assert "wrote" in capsys.readouterr().out

    changed = dict(data, model_sha256="0" * 64)
    assert inventory.unchanged_apart_from_timestamp(changed) is None   # content moved: new stamp

    (tmp_path / "inv.json").write_text("{broken")
    assert inventory.unchanged_apart_from_timestamp(data) is None


def test_the_committed_inventory_is_current():
    committed = json.loads((ROOT / "research" / "model-choice-inventory.json").read_text())
    now = inventory.build()
    for d in (committed, now):
        d.pop("created_utc")
    assert committed == now


def test_subprocess_import_does_not_run_anything():
    """Importing a tool must not write files: the module bodies are definitions only."""
    code = ("import sys; sys.path.insert(0, 'tools'); import freeze_release_manifest, "
            "inventory_model_choices, summarize_release_gate, build_note, check_pdfs")
    result = subprocess.run([sys.executable, "-c", code], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert result.stdout == ""


# ------------------------------------------------------------------------------ check_docs

MATRIX = ("        python-version: ${{ github.event_name == 'pull_request' && "
          "fromJSON('[\"3.12\"]') || fromJSON('[\"3.11\", \"3.12\", \"3.13\"]') }}\n")


@pytest.fixture
def docs_tree(tmp_path, monkeypatch):
    """A scratch repository root for check_docs, with fresh result lists."""
    for name in ("passes", "failures", "skips"):
        monkeypatch.setattr(check_docs, name, [])
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    (tmp_path / ".github" / "workflows" / "ci.yml").write_text("jobs:\n  unit:\n" + MATRIX)
    monkeypatch.setattr(check_docs, "ROOT", tmp_path)
    monkeypatch.setattr(check_docs, "tracked_markdown",
                        lambda: sorted(tmp_path.glob("*.md")))
    return tmp_path


def test_ci_python_versions_reads_both_lists():
    assert check_docs.ci_python_versions(MATRIX) == (["3.12"], ["3.11", "3.12", "3.13"])
    assert check_docs.ci_python_versions("python-version: ${{ matrix.x }}\n") is None
    one = "python-version: ${{ fromJSON('[\"3.12\"]') }}\n"
    assert check_docs.ci_python_versions(one) is None
    assert check_docs.ci_python_versions("") is None


def test_the_real_workflow_has_the_two_lists():
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    on_pull_request, on_main = check_docs.ci_python_versions(workflow)
    assert on_pull_request == ["3.12"] and set(on_pull_request) <= set(on_main)


def test_python_version_claims_read_lists_across_wrapped_lines():
    text = "unit tests run across Python 3.11, 3.12,\n3.13 and 3.14; on pull requests Python 3.12\nonly."
    assert check_docs.python_version_claims(text) == [
        ("list", ["3.11", "3.12", "3.13", "3.14"]), ("only", ["3.12"])]
    assert check_docs.python_version_claims("Python 3.12 and 3.13") == [("list", ["3.12", "3.13"])]
    assert check_docs.python_version_claims("Python 3 is used; version 3.14.1") == []


def test_check_python_versions_passes_and_catches_a_short_list(docs_tree):
    (docs_tree / "A.md").write_text("It runs Python 3.11, 3.12 and 3.13 on main and 3.12 only on pulls.\n")
    (docs_tree / "CHANGELOG.md").write_text("History: Python 3.11 and 3.12 once ran.\n")
    (docs_tree / "B.md").write_text("> Retired: Python 3.10 and 3.11.\n")
    check_docs.check_python_versions()
    assert check_docs.failures == [] and "2 claim(s)" in check_docs.passes[0]

    (docs_tree / "C.md").write_text("Unit tests\nrun on Python 3.11 and 3.12.\n\nOn pulls, Python 3.13 only.\n")
    check_docs.passes.clear()
    check_docs.check_python_versions()
    wrong = " ".join(check_docs.failures)
    assert "C.md:1: says 3.11, 3.12, the matrix runs 3.11, 3.12, 3.13" in wrong
    assert "C.md:4: says 3.13, the matrix runs 3.12" in wrong


def test_check_python_versions_fails_without_a_matrix(docs_tree):
    (docs_tree / ".github" / "workflows" / "ci.yml").write_text("jobs: {}\n")
    check_docs.check_python_versions()
    assert check_docs.failures and "no two-list python-version line" in check_docs.failures[0]


def test_check_own_total_reads_the_handoff_table(docs_tree):
    check_docs.passes.extend(["OK: a", "OK: b"])                  # two ran, and this is a third
    (docs_tree / "HANDOFF.md").write_text("| `tools/check_docs.py` | 3 checks, 0 failed |\n")
    check_docs.check_own_total()
    assert check_docs.failures == [] and "has 3 checks" in check_docs.passes.pop()

    (docs_tree / "HANDOFF.md").write_text("| `tools/check_docs.py` | 9 checks, 0 failed |\n")
    check_docs.check_own_total()
    assert "says check_docs.py has 9 checks, it has 3" in check_docs.failures[0]

    check_docs.failures.clear()
    (docs_tree / "HANDOFF.md").write_text("nothing about it\n")
    check_docs.check_own_total()
    assert "does not state how many checks" in check_docs.failures[0]


def test_check_own_total_waits_for_a_full_run(docs_tree):
    check_docs.skips.append("SKIP: no pypdf")
    check_docs.check_own_total()
    assert check_docs.failures == [] and len(check_docs.skips) == 2


def test_check_own_total_waits_for_a_clean_run(docs_tree):
    check_docs.failures.append("an earlier failure")
    check_docs.check_own_total()
    assert check_docs.failures == ["an earlier failure"] and len(check_docs.skips) == 1


def test_version_claims_need_the_word_python():
    assert check_docs.python_version_claims("tested on 3.11, 3.12 and 3.13") == []
    assert check_docs.python_version_claims("Python 3.12 only") == [("only", ["3.12"])]


# ------------------------------------------------------------------------ run_ci_locally

def test_local_ci_says_when_a_job_could_not_run(tmp_path):
    """A job that could not run is not a job that passed: the verdict names it."""
    bare = tmp_path / "bin"
    bare.mkdir()
    (bare / "dirname").symlink_to(shutil.which("dirname"))
    result = subprocess.run([shutil.which("bash"), str(ROOT / "tools" / "run_ci_locally.sh"), "documents"],
                            cwd=ROOT, capture_output=True, text=True,
                            env={"PATH": str(bare)})
    assert result.returncode == 1, result.stdout + result.stderr    # nothing ran is not a pass
    assert "NOT RUN: pandoc or tectonic missing: the documents job not run" in result.stdout
    assert "nothing ran" in result.stdout and "local CI clear" not in result.stdout


# ----------------------------------------------------------------------------- check_fonts

def _fonts_in(tmp_path, names=None, content=b"font"):
    for name in (names or check_fonts.PINS):
        (tmp_path / name).write_bytes(content)
    return tmp_path


def test_check_fonts_matches_the_pinned_hashes(tmp_path, monkeypatch):
    content = b"a font"
    monkeypatch.setattr(check_fonts, "PINS",
                        {name: hashlib.sha256(content).hexdigest()
                         for name in check_fonts.PINS})
    good, bad = check_fonts.compare([_fonts_in(tmp_path, content=content)])
    assert len(good) == 4 and bad == []


def test_check_fonts_reports_a_mismatch_and_a_missing_file(tmp_path):
    names = list(check_fonts.PINS)
    _fonts_in(tmp_path, names[:3], content=b"not the pinned font")
    good, bad = check_fonts.compare([tmp_path])
    assert good == [] and len(bad) == 4
    assert sum(line.startswith("MISMATCH") for line in bad) == 3
    assert sum(line.startswith("MISSING") for line in bad) == 1


def test_check_fonts_strict_exits_nonzero_only_when_asked(tmp_path, capsys):
    _fonts_in(tmp_path, content=b"wrong")
    assert check_fonts.main(["--dir", str(tmp_path)]) == 0
    assert "will not match CI's byte for byte" in capsys.readouterr().out
    assert check_fonts.main(["--strict", "--dir", str(tmp_path)]) == 1
    with pytest.raises(SystemExit):
        check_fonts.main(["--dir"])


def test_check_fonts_pins_are_four_distinct_sha256_digests():
    assert len(check_fonts.PINS) == 4 and len(set(check_fonts.PINS.values())) == 4
    assert all(len(h) == 64 and set(h) <= set("0123456789abcdef") for h in check_fonts.PINS.values())


def test_check_fonts_finds_files_by_any_case_and_guards_its_arguments(tmp_path, capsys):
    (tmp_path / "TeXGyrePagella-Regular.otf").write_bytes(b"x")
    assert check_fonts.locate("texgyrepagella-regular.otf", [tmp_path]).name.lower() == "texgyrepagella-regular.otf"
    assert check_fonts.locate("texgyrepagella-bold.otf", [tmp_path]) is None
    with pytest.raises(SystemExit):
        check_fonts.main(["--dir", "--strict"])
    assert check_fonts.main(["--strict", "--dir", str(tmp_path)]) == 1
    assert "update PINS deliberately" in capsys.readouterr().out


def test_check_fonts_candidate_dirs_reads_fontconfig_output(tmp_path, monkeypatch):
    font_dir = tmp_path / "with:colon"
    font_dir.mkdir()
    listing = f"{font_dir}/TeXGyrePagella-Bold.otf: \n"
    monkeypatch.setattr(check_fonts.shutil, "which", lambda name: "/usr/bin/fc-list")
    monkeypatch.setattr(check_fonts.subprocess, "run",
                        lambda *a, **k: subprocess.CompletedProcess(a, 0, stdout=listing, stderr=""))
    assert font_dir in check_fonts.candidate_dirs()
