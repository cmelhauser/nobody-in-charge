"""Tests for the four book-level checkers: check_book, check_chapter, check_portability, withheld.

Each checker is exercised two ways. The functions are called directly against small fixture
trees built under `tmp_path`, with the module's root constants redirected there, so every
branch is reached without touching the repository. The command-line entry points are also run
as subprocesses from a copy of the tools in a temporary tree, so `--help`, the exit codes and
the printed report are checked end to end.

Nothing here needs pandoc, tectonic, fonts, the network or the git-ignored source documents,
and nothing is written into the repository tree. The name the withheld-name machinery guards
is never written down: these tests use an invented name and swap its digest into the module,
as `tests/test_tools_integration.py` does.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import types
from pathlib import Path

import check_book
import check_chapter
import check_portability
import pytest
import withheld

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"

# An invented name, so that no test stores the real one.
INVENTED = ("vexmoor", "quillon vexmoor")


def write(path: Path, text: str) -> Path:
    """Write `text` to `path`, creating parent directories, and return the path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


# ============================================================================= withheld

@pytest.fixture
def invented_name(monkeypatch):
    """Replace the withheld digests with those of the invented name for one test."""
    monkeypatch.setattr(withheld, "WITHHELD",
                        {hashlib.sha256(term.encode()).hexdigest() for term in INVENTED})


def test_withheld_digests_are_sha256_hex_and_hold_no_plaintext():
    """The committed set is two 64-hex digests, so the file stores no readable name."""
    assert len(withheld.WITHHELD) == 2
    assert all(len(d) == 64 and set(d) <= set("0123456789abcdef") for d in withheld.WITHHELD)


def test_real_digests_do_not_flag_ordinary_prose():
    """With the real set loaded, plain prose is clean (nothing here names anyone)."""
    assert not withheld.prints_withheld("A founding teacher left; the sangha abolished the office.")
    assert not withheld.is_withheld("recovery dharma")


def test_is_withheld_sees_through_case_possessives_and_compounds(invented_name):
    """Whole term and each apostrophe or hyphen piece are tested, case-insensitively."""
    for form in ("Vexmoor", "VEXMOOR", "vexmoor's", "vexmoor\u2019s", "vexmoor-style",
                 "Quillon Vexmoor", "quillon vexmoor's"):
        assert withheld.is_withheld(form), form
    for form in ("quillon", "moor", "quillon moor", ""):
        assert not withheld.is_withheld(form), form


def test_prints_withheld_checks_words_pairs_and_line_breaks(invented_name):
    """Single words, adjacent pairs and a pair split across a line break are all found."""
    assert withheld.prints_withheld("He taught with Vexmoor for years.")
    assert withheld.prints_withheld("taught by Quillon\nVexmoor until 2019")
    assert withheld.prints_withheld("Quillon Vexmoor")
    assert not withheld.prints_withheld("taught by a founding teacher until 2019")
    assert not withheld.prints_withheld("")
    assert not withheld.prints_withheld("a")      # too short to be a WORD token at all
    assert not withheld.prints_withheld("12345 !!! ---")


def test_word_pattern_keeps_possessives_and_compounds_as_one_token():
    """The tokenizer keeps both apostrophes and hyphens inside a token."""
    assert withheld.WORD.findall("anne's well-known \u201cteacher\u201d it\u2019s") == [
        "anne's", "well-known", "teacher", "it\u2019s"]
    assert withheld.JOINERS.split("a'b\u2019c-d") == ["a", "b", "c", "d"]


# ============================================================================= check_portability

def _marker_lines() -> dict[str, str]:
    """Lines that each carry one forbidden marker, assembled so this file stays clean."""
    slash = "/"
    return {
        "posix": "see " + slash + "Users" + slash + "someone/project",
        "home": "at " + slash + "home" + slash + "someone",
        "workspace": "in " + slash + "workspace" + slash + "repo",
        "uri": "open file" + ":" + "//somewhere",
        "windows": "run C" + ":" + "\\temp\\x",
        "windows_slash": "run d" + ":" + "/data",
        "tilde": "cd ~" + slash + "projects",
    }


def test_findings_walks_a_tree_without_git_and_reports_each_label(tmp_path, monkeypatch):
    """Without .git every text file is read; skipped kinds and directories are not."""
    monkeypatch.setattr(check_portability, "ROOT", tmp_path)
    lines = _marker_lines()
    write(tmp_path / "a.md", "clean\n" + lines["posix"] + "\n")
    write(tmp_path / "docs" / "b.py", lines["uri"] + " and " + lines["tilde"] + "\n")
    write(tmp_path / "c.json", lines["windows"] + "\n")
    write(tmp_path / "d.tex", lines["windows_slash"] + "\n" + lines["home"] + "\n")
    write(tmp_path / "e.yml", lines["workspace"] + "\n")
    # OCR transcriptions under research/ are source data and are skipped on purpose.
    write(tmp_path / "research" / "ocr.txt", lines["posix"] + "\n")
    # A .txt outside research/ is still checked.
    write(tmp_path / "notes.txt", lines["home"] + "\n")
    # Suffixes outside TEXT_SUFFIXES, and ignored directories, are never opened.
    write(tmp_path / "image.png", lines["posix"] + "\n")
    write(tmp_path / ".venv" / "lib.md", lines["posix"] + "\n")
    write(tmp_path / "pkg" / "__pycache__" / "x.py", lines["posix"] + "\n")
    # Bytes that are not UTF-8 are skipped rather than reported.
    (tmp_path / "binary.md").write_bytes(b"\xff\xfe\x00 not utf-8 " + lines["posix"].encode())

    hits = check_portability.findings()
    by_file = {hit.split(":")[0]: hit for hit in hits}
    assert set(by_file) == {"a.md", str(Path("docs") / "b.py"), "c.json", "d.tex", "e.yml",
                            "notes.txt"}
    assert by_file["a.md"] == "a.md:2: /" + "Users/"
    assert "file:" + "//, home-relative path" in by_file[str(Path("docs") / "b.py")]
    assert "Windows absolute path" in by_file["c.json"]
    d_hits = [h for h in hits if h.startswith("d.tex")]
    assert len(d_hits) == 2
    assert "Windows absolute path" in d_hits[0] and d_hits[1].endswith("/" + "home/")
    assert by_file["e.yml"].endswith("/" + "workspace/")
    assert by_file["notes.txt"].endswith("/" + "home/")


def test_candidate_files_uses_the_git_index_when_a_git_dir_exists(tmp_path, monkeypatch):
    """With a .git directory the file list comes from `git ls-files -z`."""
    monkeypatch.setattr(check_portability, "ROOT", tmp_path)
    (tmp_path / ".git").mkdir()
    calls = []

    def fake_run(cmd, **kwargs):
        """Record the command and keywords of the call and return a fixed NUL-separated listing."""
        calls.append((cmd, kwargs))
        return types.SimpleNamespace(stdout=b"one.md\0sub/two.py\0\0")

    monkeypatch.setattr(check_portability.subprocess, "run", fake_run)
    files = check_portability.candidate_files()
    assert files == [tmp_path / "one.md", tmp_path / "sub" / "two.py"]
    cmd, kwargs = calls[0]
    assert cmd[:3] == ["git", "-C", str(tmp_path)] and "ls-files" in cmd
    assert kwargs["check"] is True and kwargs["capture_output"] is True


def test_a_failing_git_listing_is_not_swallowed(tmp_path, monkeypatch):
    """If `git ls-files` fails in a checkout the exception propagates (the tool then exits 1)."""
    monkeypatch.setattr(check_portability, "ROOT", tmp_path)
    (tmp_path / ".git").mkdir()

    def broken(cmd, **kwargs):
        """Stand in for subprocess.run by always failing as `git ls-files` would outside a repo."""
        raise subprocess.CalledProcessError(128, cmd)

    monkeypatch.setattr(check_portability.subprocess, "run", broken)
    with pytest.raises(subprocess.CalledProcessError):
        check_portability.candidate_files()


def test_findings_skips_an_indexed_file_that_cannot_be_read(tmp_path, monkeypatch):
    """A path the index lists but the disk lacks (OSError) is skipped, not fatal."""
    monkeypatch.setattr(check_portability, "ROOT", tmp_path)
    write(tmp_path / "real.md", _marker_lines()["tilde"] + "\n")
    monkeypatch.setattr(check_portability, "candidate_files",
                        lambda: [tmp_path / "missing.md", tmp_path / "real.md",
                                 tmp_path / "skip.png"])
    assert check_portability.findings() == ["real.md:1: home-relative path"]


def test_main_prints_clean_report_and_returns_zero(tmp_path, monkeypatch, capsys):
    """No findings: one PORTABLE line and exit status 0."""
    monkeypatch.setattr(check_portability, "ROOT", tmp_path)
    write(tmp_path / "ok.md", "relative/path/only.md\n")
    assert check_portability.main() == 0
    assert capsys.readouterr().out.startswith("PORTABLE: no tracked machine-specific")


def test_main_lists_findings_and_returns_one(tmp_path, monkeypatch, capsys):
    """Findings: a heading, one indented line each, and exit status 1."""
    monkeypatch.setattr(check_portability, "ROOT", tmp_path)
    write(tmp_path / "bad.md", "x\n" + _marker_lines()["uri"] + "\n")
    assert check_portability.main() == 1
    out = capsys.readouterr().out
    assert out.splitlines()[0] == "Machine-specific paths found:"
    assert "  bad.md:2: file:" + "//" in out


def _copy_tools(tmp_path: Path, *names: str) -> Path:
    """Copy the named tools plus tool_help.py into tmp_path/tools and return the new script dir."""
    dest = tmp_path / "tools"
    dest.mkdir(parents=True, exist_ok=True)
    for name in (*names, "tool_help.py", "withheld.py"):
        shutil.copy(TOOLS / name, dest / name)
    return dest


def _run(script: Path, *args: str, cwd: Path) -> subprocess.CompletedProcess:
    """Run a script with the current interpreter and capture its output."""
    return subprocess.run([sys.executable, str(script), *args], cwd=cwd,
                          capture_output=True, text=True, timeout=300, check=False)


def test_portability_cli_exit_codes_and_help(tmp_path):
    """The script exits 0 on a clean tree, 1 on a dirty one, and prints its docstring for -h."""
    scripts = _copy_tools(tmp_path / "repo", "check_portability.py")
    write(tmp_path / "repo" / "ok.md", "fine\n")
    script = scripts / "check_portability.py"
    clean = _run(script, cwd=tmp_path)
    assert clean.returncode == 0 and "PORTABLE" in clean.stdout
    helped = _run(script, "--help", cwd=tmp_path)
    assert helped.returncode == 0 and "Fail when tracked project text" in helped.stdout
    write(tmp_path / "repo" / "bad.md", _marker_lines()["tilde"] + "\n")
    dirty = _run(script, cwd=tmp_path)
    assert dirty.returncode == 1 and "bad.md:1: home-relative path" in dirty.stdout


# ============================================================================= check_chapter

def chapter_text(*, head="# Chapter One\n## A Title\n", body="Plain narrative here.\n",
                 parts=None, refs=None, machinery=True) -> str:
    """Build a chapter that passes every rule unless a keyword argument breaks one."""
    parts = parts if parts is not None else check_chapter.WANT_PARTS
    if refs is None:
        refs = ("**Read in full**\n\n- Smith (2000).\n\n"
                "**Cited at a remove**\n\n- Jones (1990).\n\n"
                "**What was not read**\n\nNothing.\n")
    text = head + "\n" + body
    if machinery:
        text += "\n---\n\n## The Machinery\n\n"
        for part in parts:
            text += f"### {part}\n\nText.\n\n"
        if refs:
            text = text.replace("### 4. References\n\nText.\n\n", "### 4. References\n\n" + refs)
    return text


@pytest.fixture
def no_textstat(monkeypatch):
    """Make `import textstat` fail, whether or not the library is installed."""
    monkeypatch.setitem(sys.modules, "textstat", None)


def fake_textstat(monkeypatch, grade: float) -> None:
    """Install a stand-in `textstat` module whose grade is fixed."""
    module = types.ModuleType("textstat")
    module.__dict__["flesch_kincaid_grade"] = lambda text: grade
    monkeypatch.setitem(sys.modules, "textstat", module)


def run_check(tmp_path: Path, text: str, name="ch09-x.md", capsys=None):
    """Write a chapter file, check it, and return (passed, printed output)."""
    path = write(tmp_path / name, text)
    ok = check_chapter.check(str(path))
    return ok, capsys.readouterr().out


def test_a_conforming_chapter_is_ok(tmp_path, capsys, no_textstat):
    """A chapter with the full structure passes with status OK and no grade."""
    ok, out = run_check(tmp_path, chapter_text(), capsys=capsys)
    assert ok is True
    assert out.startswith("ch09-x.md") and " OK " in out.splitlines()[0]
    assert "FK n/a" in out and "FAIL" not in out and "warn" not in out


def test_flesch_kincaid_grade_is_reported_and_warns_above_ten(tmp_path, capsys, monkeypatch):
    """With textstat present the grade is printed; above 10 it is a warning, not a failure."""
    fake_textstat(monkeypatch, 12.34)
    ok, out = run_check(tmp_path, chapter_text(), capsys=capsys)
    assert ok is True and "FK 12.3" in out
    assert "warn  FK grade 12.3; aim under 10" in out
    fake_textstat(monkeypatch, 6.0)
    ok, out = run_check(tmp_path, chapter_text(), capsys=capsys)
    assert ok is True and "FK 6.0" in out and "warn" not in out


def test_long_sentences_warn_but_do_not_fail(tmp_path, capsys, no_textstat):
    """A sentence over 45 words is a warning."""
    sentence = " ".join(["word"] * 50) + ". Short one."
    ok, out = run_check(tmp_path, chapter_text(body=sentence + "\n"), capsys=capsys)
    assert ok is True and "warn  1 sentence(s) over 45 words" in out
    assert " warn " in out.splitlines()[0]


def test_missing_machinery_fails_and_skips_reference_rules(tmp_path, capsys, no_textstat):
    """No Machinery heading is one structural failure and part 4 is not then demanded."""
    ok, out = run_check(tmp_path, chapter_text(machinery=False), capsys=capsys)
    assert ok is False
    assert "FAIL  no Machinery section" in out
    assert "Machinery parts wrong: []" in out
    assert "no '### 4. References'" not in out


def test_heading_rules_apply_to_the_first_four_lines(tmp_path, capsys, no_textstat):
    """The first heading must be '# Chapter ...' and the second '## ...'."""
    ok, out = run_check(tmp_path, chapter_text(head="Intro\nmore\n"), capsys=capsys)
    assert ok is False
    assert "first heading must be '# Chapter <Word>'" in out
    assert "second heading must be '## <Title>'" in out


def test_machinery_part_headings_must_match_exactly(tmp_path, capsys, no_textstat):
    """Wrong or reordered numbered parts fail; unnumbered ### lines inside it are ignored."""
    parts = ["1. What the model says", "3. Notes on sources", "2. The technical version",
             "4. References"]
    ok, out = run_check(tmp_path, chapter_text(parts=parts), capsys=capsys)
    assert ok is False and "Machinery parts wrong" in out


def test_main_text_must_not_use_subheadings_or_tables(tmp_path, capsys, no_textstat):
    """### in the narrative and a pipe table in the narrative each fail."""
    body = "Intro.\n\n### Not allowed\n\n| a | b |\n|---|---|\n| 1 | 2 |\n"
    ok, out = run_check(tmp_path, chapter_text(body=body), capsys=capsys)
    assert ok is False
    assert "no ### subheadings in main text" in out
    assert "no tables in main text" in out


def test_latex_dollar_and_stray_commands_fail(tmp_path, capsys, no_textstat):
    """A dollar sign and a bare backslash command are both reported."""
    ok, out = run_check(tmp_path, chapter_text(body="Cost is $5 and \\alpha\n"), capsys=capsys)
    assert ok is False
    assert "no LaTeX; inline symbols in plain text" in out
    assert "bare LaTeX commands left behind: ['\\\\alpha']" in out


def test_em_dash_fails_in_prose_but_not_in_a_quotation(tmp_path, capsys, no_textstat):
    """An em dash fails unless the line is a blockquote."""
    dash = "\u2014"
    ok, out = run_check(tmp_path, chapter_text(body=f"A {dash} B\n"), capsys=capsys)
    assert ok is False and "em-dash in author prose" in out
    ok, out = run_check(tmp_path, chapter_text(body=f"> quoted {dash} source\n"), capsys=capsys)
    assert ok is True


def test_front_and_back_matter_skip_structure_but_keep_prose_rules(tmp_path, capsys, no_textstat):
    """The preface and primer need no Machinery or chapter heading, yet are still style-checked."""
    ok, out = run_check(tmp_path, "Just prose, no headings.\n", name="ch00-preface.md",
                        capsys=capsys)
    assert ok is True
    ok, out = run_check(tmp_path, "Just prose.\n", name="ch00b-introduction.md", capsys=capsys)
    assert ok is True
    ok, out = run_check(tmp_path, "Primer prose with $x.\n",
                        name="PRIMER-steps-and-traditions.md", capsys=capsys)
    assert ok is False and "no LaTeX" in out and "no Machinery" not in out


def test_missing_references_section_fails(tmp_path, capsys, no_textstat):
    """A Machinery with no '### 4. References' is reported even if the parts list is wrong."""
    ok, out = run_check(tmp_path, chapter_text(parts=check_chapter.WANT_PARTS[:3], refs=""),
                        capsys=capsys)
    assert ok is False and "no '### 4. References' section" in out


def test_reference_headings_must_be_canonical_ordered_unique_and_required(
        tmp_path, capsys, no_textstat):
    """Odd, out-of-order, duplicate and missing reference headings are each reported."""
    refs = ("**Cited at a remove**\n\n- a\n\n**Read in full**\n\n- b\n\n**Read in full**\n\n"
            "- c\n\n**Surprise heading**\n\n- d\n")
    ok, out = run_check(tmp_path, chapter_text(refs=refs), capsys=capsys)
    assert ok is False
    assert "non-canonical reference heading(s): Surprise heading" in out
    assert "reference headings out of canonical order" in out
    assert "duplicate reference headings" in out
    assert "references missing the 'What was not read' heading" in out


def test_trailing_colon_or_full_stop_on_a_heading_is_tolerated(tmp_path, capsys, no_textstat):
    """`**Read in full.**` and `**Read in full:**` still count as the canonical heading."""
    refs = ("**Read in full.**\n\n- a\n\n**Cited at a remove:**\n\n- b\n\n"
            "**What was not read.**\n\nNothing.\n")
    ok, out = run_check(tmp_path, chapter_text(refs=refs), capsys=capsys)
    assert ok is True, out


def test_an_entry_marked_read_must_sit_under_read_in_full(tmp_path, capsys, no_textstat):
    """An entry saying it was read in full, filed under 'Cited at a remove', fails."""
    refs = ("**Read in full**\n\n- Smith (2000).\n\n**Cited at a remove**\n\n"
            "- Jones (1990), which I **now read in full** since.\n\n"
            "- Other (1980), **read at source** last week.\n\n"
            "**What was not read**\n\nNothing.\n")
    ok, out = run_check(tmp_path, chapter_text(refs=refs), capsys=capsys)
    assert ok is False
    assert out.count("an entry marked as read sits under 'Cited at a remove'") == 2


def test_a_canonical_heading_used_inline_fails(tmp_path, capsys, no_textstat):
    """'**What was not read.** Some prose' on one line is not a heading."""
    refs = ("**Read in full**\n\n- a\n\n**Cited at a remove**\n\n- b\n\n"
            "**What was not read.** Everything else.\n")
    ok, out = run_check(tmp_path, chapter_text(refs=refs), capsys=capsys)
    assert ok is False
    assert "canonical heading used inline rather than on its own line: What was not read" in out


def test_main_returns_one_with_a_message_when_a_file_fails(tmp_path, capsys, no_textstat):
    """main() checks every file (no short-circuit) and returns 1 if any failed."""
    good = write(tmp_path / "ch01-a.md", chapter_text())
    bad = write(tmp_path / "ch02-b.md", chapter_text(body="$x$\n"))
    assert check_chapter.main([str(bad), str(good)]) == 1
    out = capsys.readouterr().out
    assert "ch01-a.md" in out and "ch02-b.md" in out
    assert out.rstrip().endswith("fix the FAILs before calling the chapter done")


def test_main_returns_zero_when_all_files_pass(tmp_path, capsys, no_textstat):
    """All clear is printed and the status is 0."""
    good = write(tmp_path / "ch01-a.md", chapter_text())
    assert check_chapter.main([str(good)]) == 0
    assert capsys.readouterr().out.rstrip().endswith("all clear")


def test_main_with_no_arguments_finds_chapters_from_each_supported_directory(
        tmp_path, capsys, monkeypatch, no_textstat):
    """With no arguments the first matching glob wins: repo root, then here, then ../manuscript."""
    monkeypatch.setattr(sys, "argv", ["check_chapter.py"])
    root = tmp_path / "root"
    write(root / "manuscript" / "ch01-a.md", chapter_text())
    monkeypatch.chdir(root)
    assert check_chapter.main() == 0
    assert "ch01-a.md" in capsys.readouterr().out

    here = tmp_path / "here"
    write(here / "ch02-b.md", chapter_text())
    monkeypatch.chdir(here)
    assert check_chapter.main() == 0
    assert "ch02-b.md" in capsys.readouterr().out

    sibling = tmp_path / "sibling"
    write(sibling / "manuscript" / "ch03-c.md", chapter_text())
    (sibling / "sub").mkdir()
    monkeypatch.chdir(sibling / "sub")
    assert check_chapter.main() == 0
    assert "ch03-c.md" in capsys.readouterr().out


def test_main_with_no_arguments_and_no_chapters_returns_two(tmp_path, capsys, monkeypatch):
    """Nothing to check is exit status 2 with an instruction, not a silent pass."""
    monkeypatch.setattr(sys, "argv", ["check_chapter.py"])
    monkeypatch.chdir(tmp_path)
    assert check_chapter.main() == 2
    assert "no chapter files found; pass paths explicitly" in capsys.readouterr().out


def test_chapter_cli_exit_codes_help_and_missing_file(tmp_path):
    """The script exits 0 or 1 on a verdict, prints usage for --help, and raises on a bad path."""
    script = TOOLS / "check_chapter.py"
    good = write(tmp_path / "ch01-a.md", chapter_text())
    bad = write(tmp_path / "ch02-b.md", chapter_text(body="$x$\n"))
    assert _run(script, str(good), cwd=tmp_path).returncode == 0
    failed = _run(script, str(bad), cwd=tmp_path)
    assert failed.returncode == 1 and "FAIL  no LaTeX" in failed.stdout
    helped = _run(script, "-h", cwd=tmp_path)
    assert helped.returncode == 0 and "House-style check" in helped.stdout
    assert "ch01-a.md" not in helped.stdout
    empty = tmp_path / "empty"
    empty.mkdir()
    nothing = _run(script, cwd=empty)
    assert nothing.returncode == 2
    missing = _run(script, str(tmp_path / "absent.md"), cwd=tmp_path)
    assert missing.returncode == 1 and "FileNotFoundError" in missing.stderr


# ============================================================================= check_book

@pytest.fixture
def book(tmp_path, monkeypatch):
    """check_book pointed at an empty fixture repository, with its findings lists cleared."""
    monkeypatch.setattr(check_book, "ROOT", str(tmp_path))
    monkeypatch.setattr(check_book, "CHAPTERS", [])
    for findings in (check_book.FAILS, check_book.WARNS, check_book.NOTES):
        findings.clear()
    yield check_book
    for findings in (check_book.FAILS, check_book.WARNS, check_book.NOTES):
        findings.clear()


def put_chapters(book, tmp_path: Path, chapters: dict[str, str]) -> None:
    """Write chapter files under manuscript/ and register them as the book's chapters."""
    paths = [str(write(tmp_path / "manuscript" / name, text)) for name, text in chapters.items()]
    book.CHAPTERS[:] = sorted(paths)


def code_cell(source: str, output: str | None = None) -> dict:
    """A notebook code cell with optional stored stdout."""
    outputs = [] if output is None else [{"output_type": "stream", "text": output.splitlines(True)}]
    return {"cell_type": "code", "source": source.splitlines(True), "outputs": outputs}


def write_notebook(tmp_path: Path, cells: list[dict]) -> None:
    """Write model/book-calculations.ipynb with the given cells."""
    write(tmp_path / "model" / "book-calculations.ipynb", json.dumps({"cells": cells}))


def sections(findings) -> list[str]:
    """The section names of a findings list, in order."""
    return [sec for sec, _ in findings]


def messages(findings, sec: str) -> list[str]:
    """The messages recorded in one section."""
    return [msg for s, msg in findings if s == sec]


def test_path_and_reading_helpers(book, tmp_path):
    """P joins onto the (redirected) root; the readers return text and parsed JSON."""
    assert book.P("a", "b.md") == str(tmp_path / "a" / "b.md")
    path = write(tmp_path / "x.txt", "caf\u00e9")
    assert book.read_text(str(path)) == "caf\u00e9"
    assert book.read_text(str(path), encoding="utf-8", errors="ignore") == "caf\u00e9"
    assert book.read_json(str(write(tmp_path / "x.json", '{"k": [1]}'))) == {"k": [1]}


def test_recorders_append_section_message_pairs(book):
    """fail, warn and note each append to their own list."""
    book.fail("s", "f")
    book.warn("s", "w")
    book.note("s", "n")
    assert book.FAILS == [("s", "f")] and book.WARNS == [("s", "w")]
    assert book.NOTES == [("s", "n")]


def test_body_words_and_grams(book, tmp_path):
    """Chapter text is cut at the Machinery; words drops code and punctuation; grams are sets."""
    text = "Alpha `code span` beta, GAMMA!\n## The Machinery\nhidden\n"
    path = str(write(tmp_path / "c.md", text))
    assert book.body(path).strip() == "Alpha `code span` beta, GAMMA!"
    assert "hidden" in book.body(path, main_only=False)
    assert book.words(path) == ["alpha", "beta", "gamma"]
    assert "hidden" in book.words(path, main_only=False)
    assert book.grams(["a", "b", "c", "d"], 2) == {("a", "b"), ("b", "c"), ("c", "d")}
    assert book.grams(["a"], 2) == set()
    # A heading at offset 0 is not cut (i > 0 is required), so a lone machinery file keeps it.
    start = str(write(tmp_path / "d.md", "## The Machinery\nonly\n"))
    assert "only" in book.body(start)


def test_reachable_accepts_exact_rounded_and_non_numeric_strings(book):
    """A decimal is reachable if present, a rounding of a present value, or not a number."""
    blob = "values 0.1234 and 12.5"
    assert book.reachable("0.1234", blob)
    assert book.reachable("0.12", blob)              # a substring of 0.1234
    assert book.reachable("0.13", "x 0.126 y")       # not a substring, but 0.126 rounds to it
    assert book.reachable("12.5", blob)
    assert not book.reachable("0.14", blob)
    assert book.reachable("not-a-number", blob)      # never flag what is not a number
    assert not book.reachable("9.99", "")


def test_check_figures_reports_missing_notebook(book):
    """No notebook is a failure in the figures section and nothing else is attempted."""
    book.check_figures()
    assert book.FAILS == [("figures", "notebook not found")]


def figure_tree(tmp_path: Path) -> None:
    """A notebook, model source and caches that together make some decimals reachable."""
    write_notebook(tmp_path, [
        {"cell_type": "markdown", "source": ["prose 7.77 is ignored\n"]},
        code_cell("x = 0.250\n", "result 0.3333\n"),
    ])
    write(tmp_path / "model" / "aa_group_model.py", "CAP = 60.5\n")
    write(tmp_path / "research" / "cache.json", '{"v": 1.125, "w": 0.126}')
    # These two caches are excluded from the traceability corpus on purpose.
    write(tmp_path / "research" / "audit-pre-correction-manifest.json", '{"v": 8.888}')
    write(tmp_path / "research" / "kurtz-1991-verification-index.json", '{"v": 9.999}')


def test_check_figures_passes_when_every_decimal_traces(book, tmp_path):
    """Notebook source and output, model source, caches and roundings all make a decimal OK."""
    figure_tree(tmp_path)
    put_chapters(book, tmp_path, {
        "ch01-a.md": "Values 0.250, 0.3333, 60.5, 1.125 and 0.13 (a rounding of 0.126) appear.\n"
                     "A DOI doi:10.1234/abc.5.6 and ISBN 978-0-12.3 are identifiers.\n"
                     "From the sources: 14.3 and 4.9, 0.053, 0.061, 0.055.\n",
    })
    book.check_figures()
    assert book.FAILS == []
    assert messages(book.NOTES, "figures") == [
        "all decimals across 1 chapters trace to a computational source"]


def test_check_figures_flags_an_untraceable_decimal_and_excluded_caches(book, tmp_path):
    """A decimal found only in an excluded cache, or nowhere, is reported per chapter."""
    figure_tree(tmp_path)
    put_chapters(book, tmp_path, {"ch01-a.md": "Good 0.250. Bad 8.888 and 9.999 and 4.2468.\n"})
    book.check_figures()
    failed = messages(book.FAILS, "figures")
    assert sorted(m.split(":")[1].split(" is")[0].strip() for m in failed) == [
        "4.2468", "8.888", "9.999"]
    assert all(m.startswith("ch01-a.md: ") for m in failed)
    assert not book.NOTES


SIM_BODY = "Results come from 50 runs with standard error 0.1 each.\n"


def machinery(text: str) -> str:
    """Chapter text whose Machinery holds `text`."""
    return "Narrative.\n\n## The Machinery\n\n" + text


def test_check_intervals_skips_chapters_with_no_simulation_output(book, tmp_path):
    """No Machinery, a Machinery with no simulation words, and an exact one all pass."""
    put_chapters(book, tmp_path, {
        "ch01-a.md": "No machinery here at all.\n",
        "ch02-b.md": machinery("Pure algebra only.\n"),
        "ch03-c.md": machinery("Monte Carlo was replaced; the result is now closed-form.\n"),
    })
    book.check_intervals()
    assert book.FAILS == []


def test_check_intervals_requires_size_and_interval_for_live_output(book, tmp_path):
    """Live simulation output with neither a size nor an interval fails twice."""
    put_chapters(book, tmp_path, {"ch01-a.md": machinery("A Monte Carlo study was run.\n")})
    book.check_intervals()
    assert messages(book.FAILS, "intervals") == [
        "ch01-a.md: presents simulation output with no sample size",
        "ch01-a.md: presents simulation output with no interval or error",
    ]


def test_check_intervals_accepts_output_with_size_and_interval(book, tmp_path):
    """Both present: no failure."""
    put_chapters(book, tmp_path, {"ch01-a.md": machinery(SIM_BODY)})
    book.check_intervals()
    assert book.FAILS == []


def test_check_intervals_flags_a_small_live_sample_but_not_a_retrospective_one(book, tmp_path):
    """'ten seeds' relied on today fails; the same words in a confession do not."""
    filler = "pad " * 120
    live = machinery(SIM_BODY + filler + "We use ten seeds for this.\n" + filler)
    retro = machinery(SIM_BODY + filler + "This was wrong when quoted from ten seeds.\n" + filler)
    put_chapters(book, tmp_path, {"ch01-a.md": live, "ch02-b.md": retro})
    book.check_intervals()
    assert messages(book.FAILS, "intervals") == [
        'ch01-a.md: quotes "ten seeds" as a live figure; minimum is 400']


def test_check_repetition_warns_on_a_shared_eight_word_run(book, tmp_path):
    """Exactly one 8-word run in common between two chapters is one warning."""
    shared = "the quick brown fox jumps over the lazy"
    put_chapters(book, tmp_path, {
        "ch01-a.md": f"Intro alpha beta. {shared} dog today.\n",
        "ch02-b.md": f"Other start gamma. {shared} cat tomorrow.\n",
        "ch03-c.md": "Wholly different words appear in this particular chapter only.\n",
    })
    book.check_repetition()
    warned = list(book.WARNS)
    assert warned == [("repetition", f'ch01-a / ch02-b: "{shared}"')]
    assert messages(book.NOTES, "repetition") == [
        "1 shared 8-grams across all pairs, 1 not on the allow-list"]


def test_check_repetition_ignores_allow_listed_phrases(book, tmp_path):
    """A shared run that contains an allow-listed phrase is counted but not flagged."""
    shared = "membership is a desire to stop drinking now"
    put_chapters(book, tmp_path, {
        "ch01-a.md": f"Intro alpha beta. {shared} and so on.\n",
        "ch02-b.md": f"Other start gamma. {shared} but then not.\n",
    })
    book.check_repetition()
    assert book.WARNS == []
    assert messages(book.NOTES, "repetition") == [
        "1 shared 8-grams across all pairs, 0 not on the allow-list"]


def test_check_forward_warns_about_undrafted_chapters(book, tmp_path):
    """Chapter references to numbers with no file warn; drafted ones and unknown words do not."""
    put_chapters(book, tmp_path, {
        "ch01-a.md": "See Chapter Two. Chapters Three to Twenty-Five matter. Chapter Banana.\n",
        "ch02-b.md": "Back to Chapter One. Also Chapters Two through Three.\n",
    })
    book.check_forward()
    # The second group only takes a single capitalised word, so "Twenty-Five" reads as Twenty.
    assert [(sec, msg.split(";")[0]) for sec, msg in book.WARNS] == [
        ("forward", "ch01-a.md points at undrafted [3, 20]"),
        ("forward", "ch02-b.md points at undrafted [3]")]
    assert not book.NOTES


def test_check_forward_notes_when_nothing_dangles(book, tmp_path):
    """No undrafted reference gives the ok note."""
    put_chapters(book, tmp_path, {"ch01-a.md": "Chapter Zero and Chapter One.\n"})
    book.check_forward()
    assert messages(book.NOTES, "forward") == ["no chapter references an undrafted chapter"]


def test_check_status_with_no_notebook_and_no_readme_is_quiet(book, tmp_path):
    """With neither file there is nothing to compare."""
    put_chapters(book, tmp_path, {"ch01-a.md": "one two three\n"})
    book.check_status()
    assert book.FAILS == [] and book.NOTES == []


def test_check_status_counts_assertions_and_compares_with_the_readme(book, tmp_path):
    """Assertion count, word count and chapter count are each compared with README."""
    write_notebook(tmp_path, [
        {"cell_type": "markdown", "source": ["text"]},
        code_cell("def check(x):\n    print(x)\n", "setup shown\n"),
        code_cell("check(1)\ncheck(2)\n", "  OK one\n  OK two\n"),
    ])
    put_chapters(book, tmp_path, {"ch00-preface.md": "w " * 100, "ch01-a.md": "w " * 100})
    write(tmp_path / "README.md",
          "The notebook makes 2 assertions. About 200 words... about 200 words in the book, "
          "plus 1 of 25 chapters.\n")
    book.check_status()
    assert book.FAILS == []
    assert messages(book.NOTES, "status") == [
        "notebook: 2 assertions stored, 0 failures",
        "2 chapter files, 200 words, README agrees",
    ]


def test_check_status_reports_every_kind_of_disagreement(book, tmp_path):
    """Stored failures, blank outputs, silent check cells and README mismatches all fail."""
    write_notebook(tmp_path, [
        code_cell("check(1)\n", "  OK fine\n  FAIL broken\n"),
        code_cell("x = undefined_name\n"),                   # blank output
        code_cell("check(3)\n", "no result lines here\n"),   # calls check, shows nothing
        code_cell("", None),                                  # no source: not 'blank'
    ])
    put_chapters(book, tmp_path, {"ch01-a.md": "w " * 10})
    write(tmp_path / "README.md",
          "It makes 9 assertions and has about 5,000 words, plus 4 of 25 chapters.\n")
    book.check_status()
    failed = messages(book.FAILS, "status")
    assert "notebook has 1 stored assertion failures" in failed
    assert "notebook code cells with blank output: [1]" in failed
    assert "notebook cells call check() but stored no result: [2]" in failed
    assert "README says 9 assertions, notebook stores 1" in failed
    assert any(m.startswith("README says ~5,000 words, chapters total 10") for m in failed)
    assert "README says 4 chapters, 0 exist besides the preface" in failed


def test_check_history_flags_unsupported_duration_claims_only(book, tmp_path):
    """A bare project-history duration fails; the documented exemptions do not."""
    write(tmp_path / "research" / "progress-log.md", "Entry 3 June 2026.\n")
    write(tmp_path / "README.md", "\n".join([
        "We worked on this for months before it settled.",                  # flagged
        'A quoted example: "for months" is what not to write.',             # quoted
        "- for years the list item is an example",                          # bullet
        "The rule: do not say for months.",                                 # the rule itself
        "That claim cannot be supported: for several sessions it held.",    # correction
        "In the simulated group the effect held for years.",                # model world
        "Two lines later had survived several rewrites.",                   # flagged
        "An ordinary sentence.",
    ]) + "\n")
    write(tmp_path / "plans" / "PLAN.md", "It has been wrong for a long time.\nOK for 3 weeks.\n")
    book.check_history()
    failed = messages(book.FAILS, "history")
    tail = ("; a bare duration cannot be checked against the progress log, "
            "so cite the dated entry instead")
    assert failed == [
        "README.md:1 claims a duration" + tail,
        "README.md:7 claims a duration" + tail,
        str(Path("plans") / "PLAN.md") + ":1 claims a duration" + tail,
        str(Path("plans") / "PLAN.md") + ":2 claims a duration" + tail,
    ]
    assert book.WARNS == [] and book.NOTES == []


def test_check_history_warns_when_the_log_is_undated_and_notes_when_clean(book, tmp_path):
    """No years in the log is a warning; no duration claims is the ok note."""
    write(tmp_path / "research" / "progress-log.md", "no dates here\n")
    write(tmp_path / "README.md", "Nothing to see.\n")
    book.check_history()
    assert messages(book.WARNS, "history") == [
        "research/progress-log.md carries no dates, so no duration claim anywhere in the "
        "project is verifiable"]
    assert messages(book.NOTES, "history") == [
        "no unverifiable duration claims in the instructions or plans"]


def test_check_history_tolerates_a_missing_log(book):
    """No progress log at all is treated as undated, not as an error."""
    book.check_history()
    assert sections(book.WARNS) == ["history"] and sections(book.NOTES) == ["history"]


def test_fuzzy_in_tolerates_ocr_noise_and_rejects_absence(book):
    """Exact hits pass; a one-letter misreading passes; unrelated text and short tails do not."""
    assert book.fuzzy_in("Mitchell", "he met mitchell there")
    assert book.fuzzy_in("mitchell", "he met mitrhell there")
    assert book.fuzzy_in("mitchell", "mituhell and mitrlell")
    assert not book.fuzzy_in("mitchell", "nothing relevant here at all")
    assert not book.fuzzy_in("mitchell", "ends with mit")           # window runs past the end
    assert not book.fuzzy_in("zzz", "")
    assert book.fuzzy_in("chase", "a long chase")                    # short term, exact
    assert not book.fuzzy_in("chase", "the purchase of coal")        # inside another word
    assert not book.fuzzy_in("chase", "she chose it, and left")      # one letter off: refused


def test_window_stops_at_another_source_name_or_after_two_sentences(book):
    """The citation window ends at the next saved source's name or the second sentence."""
    texts = {"Marsh": "", "Krout": ""}
    seg = "Marsh wrote of Mitchell and Beecher. Then Krout wrote of Utica. More text."
    assert book.window(seg, "Marsh", texts) == "marsh wrote of mitchell and beecher. then "
    two = "Marsh said A. Then B! And C."
    assert book.window(two, "Marsh", texts) == "marsh said a. then b! "
    assert book.window("Marsh alone", "Marsh", texts) == "marsh alone"
    # A closing quotation mark after the full stop belongs to the sentence it ends.
    assert book.window('Marsh said "Hi." Next. Later.', "Marsh", texts, sentences=1) == (
        'marsh said "hi." ')


def source_tree(tmp_path: Path) -> None:
    """A small research tree: indexes, a document, a legacy text and a short-named directory."""
    inc = tmp_path / "research" / "incorporated"
    write(inc / "Alpha_1900" / "Alpha_1900_verification-index.json",
          json.dumps({"vocab": ["alpha"], "subjects_present": ["mitchell"]}))
    write(inc / "Alpha_1901" / "Alpha_1901_verification-index.json",
          json.dumps({"vocab": ["more"], "subjects_present": ["jellinek"]}))
    write(inc / "AA_2000" / "AA_2000_verification-index.json", json.dumps({"vocab": []}))
    write(inc / "Beta_1900" / "Beta_1900_verification-index.json", json.dumps({"vocab": ["b"]}))
    write(inc / "Beta_1900" / "Beta_1900.txt", "Beta\ndiscusses   the Washingtonian movement.\n")
    write(inc / "Beta_1901" / "Beta_1901.txt", "Also total disclosure is here.\n")
    write(inc / "Ab_1900" / "Ab_1900.txt", "too short a name to use\n")
    write(tmp_path / "research" / "Kurtz-verification-index.json",
          json.dumps({"work": "Kurtz (1991)", "vocab": ["moral suasion", "alcoholics"]}))
    write(tmp_path / "research" / "marsh-1866-extra.txt", "Marsh describes a Bleeding Deacon.\n")


def test_check_sources_judges_each_citation_against_the_right_evidence(book, tmp_path):
    """Index decisions, full text, pooled directories, legacy files and exemptions."""
    source_tree(tmp_path)
    put_chapters(book, tmp_path, {"ch01-a.md": "\n".join([
        "Alpha reported that Mitchell was there.",                     # in index decisions: ok
        "Alpha also noted Beecher.",                                    # not recorded: FAIL
        "Alpha's sibling record mentions Jellinek.",                    # pooled from Alpha_1901: ok
        "Beta describes the Washingtonian meetings.",                   # in full text: ok
        "Beta cites Beecher once.",                                     # absent from text: FAIL
        "Beta also covers total disclosure.",                           # pooled second document: ok
        "Kurtz argued for moral suasion.",                              # vocabulary only: ok
        "Kurtz argued for sons of temperance.",                         # vocabulary only: FAIL
        "Marsh wrote about the bleeding deacon.",                       # legacy text file: ok
        "Alpha does not mention Beecher.",                              # correction: exempt
        "Alpha is silent here. The sources checker caught a Mitchell.", # exempt phrase
        "Nothing relevant on this line at all.",
    ]) + "\n"})
    book.check_sources()
    failed = messages(book.FAILS, "sources")
    assert len(failed) == 3, failed
    assert any('cites Alpha for "beecher"' in m for m in failed)
    assert any('cites Beta for "beecher"' in m for m in failed)
    assert any('cites Kurtz for "sons of temperance"' in m for m in failed)
    assert all(m.startswith("ch01-a.md: ") for m in failed)
    assert any("too short to identify citations" in m for m in messages(book.WARNS, "sources"))
    assert not book.NOTES


def test_check_sources_notes_success_and_pairs_checked(book, tmp_path):
    """When every pair is supported the note counts pairs and sources."""
    source_tree(tmp_path)
    put_chapters(book, tmp_path, {"ch01-a.md": "Alpha reported that Mitchell was there.\n"})
    book.check_sources()
    assert book.FAILS == []
    note = messages(book.NOTES, "sources")[0]
    assert note.startswith("1 citation-subject pairs checked against ")
    assert note.endswith("saved sources, all supported")


def test_check_sources_warns_when_there_is_nothing_to_check_against(book, tmp_path):
    """No indexes and no documents is a warning, and the chapters are not examined."""
    put_chapters(book, tmp_path, {"ch01-a.md": "Alpha said Mitchell.\n"})
    book.check_sources()
    assert messages(book.WARNS, "sources") == ["no full-text sources found in research/"]
    assert book.FAILS == [] and book.NOTES == []


def test_tracked_text_files_uses_git_and_drops_non_text_and_corpus_documents(book, tmp_path):
    """Git's list is filtered to text suffixes, existing files, and not corpus .txt files."""
    write(tmp_path / "a.md", "x")
    write(tmp_path / "b.png", "x")
    write(tmp_path / "research" / "incorporated" / "S_1" / "doc.txt", "source document")
    write(tmp_path / "research" / "incorporated" / "S_1" / "index.json", "{}")
    write(tmp_path / "research" / "staged" / "other.txt", "staged")
    write(tmp_path / "research" / "notes.txt", "kept")
    listing = "a.md\0b.png\0missing.md\0research/incorporated/S_1/doc.txt\0" \
              "research/incorporated/S_1/index.json\0research/staged/other.txt\0" \
              "research/notes.txt\0"
    book.subprocess = types.SimpleNamespace(
        run=lambda *a, **k: types.SimpleNamespace(stdout=listing.encode()),
        CalledProcessError=subprocess.CalledProcessError)
    try:
        files = book.tracked_text_files()
    finally:
        book.subprocess = subprocess
    assert files == sorted([book.P("a.md"), book.P("research", "incorporated", "S_1", "index.json"),
                            book.P("research", "notes.txt")])


@pytest.mark.parametrize("failure", [OSError("no git"),
                                     subprocess.CalledProcessError(128, "git")])
def test_tracked_text_files_falls_back_to_a_directory_walk(book, tmp_path, failure):
    """With no usable git the walk finds text files and still avoids the source documents."""
    write(tmp_path / "a.md", "x")
    write(tmp_path / "sub" / "b.json", "{}")
    write(tmp_path / "research" / "incorporated" / "S_1" / "doc.txt", "source document")

    def broken(*args, **kwargs):
        """Stand in for subprocess.run by raising the parametrized failure."""
        raise failure

    book.subprocess = types.SimpleNamespace(run=broken,
                                            CalledProcessError=subprocess.CalledProcessError)
    try:
        files = book.tracked_text_files()
    finally:
        book.subprocess = subprocess
    assert files == [book.P("a.md"), book.P("sub", "b.json")]


def test_check_withheld_names_flags_a_file_without_printing_the_name(
        book, tmp_path, invented_name):
    """A hit names the file, not the name; unreadable paths are skipped; a clean scan notes ok."""
    index = write(tmp_path / "idx.json", json.dumps({"vocab": ["alpha", "vexmoor"]}))
    prose = write(tmp_path / "prose.md", "Nothing here names anyone.\n")
    book.check_withheld_names([str(index), str(prose), str(tmp_path / "missing.md"),
                               str(tmp_path)])
    failed = messages(book.FAILS, "names")
    assert failed == ["idx.json: prints a name the project has undertaken to withhold"]
    assert "vexmoor" not in failed[0].lower()
    assert book.NOTES == []

    book.FAILS.clear()
    book.check_withheld_names([str(prose)])
    assert book.FAILS == []
    assert sections(book.NOTES) == ["names"]


def test_check_withheld_names_defaults_to_every_tracked_text_file(book, tmp_path, monkeypatch):
    """With no explicit list the scan takes tracked_text_files()."""
    seen = write(tmp_path / "seen.md", "clean\n")
    monkeypatch.setattr(book, "tracked_text_files", lambda: [str(seen)])
    book.check_withheld_names()
    assert book.FAILS == [] and sections(book.NOTES) == ["names"]


def test_main_runs_every_check_and_turns_a_crash_into_a_failure(book, monkeypatch, capsys):
    """A check that raises is reported as a FAIL naming the check; the exit status is 1."""
    def good():
        """A check that records one note and one warning, then returns normally."""
        book.note("good", "all fine")
        book.warn("good", "but look")

    def broken():
        """A check that crashes, to show main() reports it as a failure."""
        raise RuntimeError("boom")

    monkeypatch.setattr(book, "CHECKS", (good, broken))
    assert book.main() == 1
    out = capsys.readouterr().out
    assert "  ok    good       all fine" in out
    assert "  warn  good       but look" in out
    assert "  FAIL  broken     check itself failed: RuntimeError: boom" in out
    assert "1 failures, 1 warnings" in out and out.rstrip().endswith("fix the FAILs")


def test_main_returns_zero_when_every_check_is_clear(book, monkeypatch, capsys):
    """No failures: status 0 and the all-clear line."""
    monkeypatch.setattr(book, "CHECKS", (lambda: book.note("x", "fine"),))
    assert book.main() == 0
    assert capsys.readouterr().out.rstrip().endswith("book-level checks clear")


def test_the_check_list_covers_all_eight_checks(book):
    """CHECKS names every check function exactly once, in report order."""
    assert [fn.__name__ for fn in book.CHECKS] == [
        "check_figures", "check_intervals", "check_repetition", "check_forward",
        "check_status", "check_history", "check_sources", "check_withheld_names"]


def minimal_repo(root: Path) -> None:
    """A tiny but complete repository for which every book-level check passes."""
    write_notebook(root, [code_cell("check(1)\n", "  OK fine\n")])
    write(root / "model" / "aa_group_model.py", "VALUE = 0.5\n")
    write(root / "research" / "progress-log.md", "Entry 1 June 2026.\n")
    write(root / "README.md", "The notebook makes 1 assertions.\n")
    write(root / "manuscript" / "ch01-a.md", "Chapter text 0.5 here.\n")


def test_book_cli_exit_codes_report_and_help(tmp_path):
    """The script, run from a copy, exits 0 on a sound tree, 1 on a broken one, and has --help."""
    scripts = _copy_tools(tmp_path / "repo", "check_book.py")
    script = scripts / "check_book.py"
    minimal_repo(tmp_path / "repo")
    clean = _run(script, cwd=tmp_path)
    assert clean.returncode == 0, clean.stdout + clean.stderr
    assert "0 failures" in clean.stdout and "book-level checks clear" in clean.stdout
    assert "  ok    figures" in clean.stdout and "  ok    names" in clean.stdout
    helped = _run(script, "--help", cwd=tmp_path)
    assert helped.returncode == 0 and "Book-level coherence checks" in helped.stdout
    write(tmp_path / "repo" / "manuscript" / "ch02-b.md", "An unexplained 7.7777 figure.\n")
    broken = _run(script, cwd=tmp_path)
    assert broken.returncode == 1
    assert "FAIL  figures" in broken.stdout and "fix the FAILs" in broken.stdout
