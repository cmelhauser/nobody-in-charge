"""Tests of the document build tools: the book, primer and note builders and their helpers.

Covers `tools/build_book.py`, `tools/build_primer.py`, `tools/build_note.py`,
`tools/source_date.py` and `tools/tool_help.py`.

None of this needs pandoc, tectonic or the TeX Gyre Pagella font, and none of it writes into
the repository. Two techniques are used:

* the functions are called directly, with the module's path constants (`ROOT`, `SRC`, `OUT`,
  `BUILD` and so on) monkeypatched into `tmp_path` and `subprocess.run` replaced by a fake that
  plays the part of pandoc, so every branch (a missing source, no PDF engine, a failed render,
  overfull boxes) is exercised on purpose; and
* the command-line entry points are run as real subprocesses, from a copy of the tools in a
  temporary tree, with a stub `pandoc` and `tectonic` on the PATH, so the `__main__` blocks and
  exit codes are checked as a user would meet them.

The byte-for-byte output of the real builds is checked elsewhere (the release gate); these
tests check the logic that produces it.
"""
from __future__ import annotations

import importlib
import os
import re
import shutil
import stat
import subprocess
import sys
import types
from datetime import datetime, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

# Imported by name once `tools/` is on the path, rather than with import statements below the
# path change, so no module-level-import exemption is needed.
build_book = importlib.import_module("build_book")
build_note = importlib.import_module("build_note")
build_primer = importlib.import_module("build_primer")
source_date = importlib.import_module("source_date")
tool_help = importlib.import_module("tool_help")

# ----------------------------------------------------------------------------- helpers

def completed(returncode=0, stdout="", stderr=""):
    """Stand-in for `subprocess.CompletedProcess` as the builders read it."""
    return types.SimpleNamespace(returncode=returncode, stdout=stdout, stderr=stderr)


class FakePandoc:
    """A replacement for `subprocess.run` that records each call and plays pandoc.

    `result` is what every call returns. When the caller passed `check=True` and the result
    is a failure, it raises `CalledProcessError` exactly as the real function would. If
    `result` is an exception instance it is raised instead (for example `FileNotFoundError`).
    """

    def __init__(self, result=None):
        """Remember what each call should return; `None` means a successful conversion."""
        self.result = completed(stdout="converted\n") if result is None else result
        self.calls: list[tuple[list[str], dict]] = []

    def __call__(self, cmd, **kwargs):
        """Record the call, then return or raise as configured."""
        self.calls.append((list(cmd), kwargs))
        if isinstance(self.result, BaseException):
            raise self.result
        if kwargs.get("check") and self.result.returncode != 0:
            raise subprocess.CalledProcessError(self.result.returncode, cmd)
        return self.result


def only_tectonic(name):
    """Fake `shutil.which`: tectonic is installed and xelatex is not."""
    return "/bin/tectonic" if name == "tectonic" else None


def midnight(text, fmt):
    """Epoch seconds for `text` parsed with `fmt`, as midnight UTC."""
    return int(datetime.strptime(text, fmt).replace(tzinfo=timezone.utc).timestamp())


# --------------------------------------------------------------------------- tool_help

def test_help_requested_prints_the_doc_and_exits_zero(capsys):
    """Help requested prints the doc and exits zero."""
    for flag in ("-h", "--help"):
        with pytest.raises(SystemExit) as stop:
            tool_help.help_requested("  Usage text.\n", ["--other", flag])
        assert stop.value.code == 0
        assert capsys.readouterr().out == "Usage text.\n"


def test_help_requested_says_so_when_a_tool_has_no_docstring(capsys):
    """Help requested says so when a tool has no docstring."""
    with pytest.raises(SystemExit):
        tool_help.help_requested(None, ["--help"])
    assert "No usage is documented" in capsys.readouterr().out


def test_help_requested_returns_quietly_without_a_help_flag(capsys):
    """Help requested returns quietly without a help flag."""
    assert tool_help.help_requested("Usage.", ["--date", "1 May 2027"]) is None
    assert tool_help.help_requested("Usage.", []) is None
    assert capsys.readouterr().out == ""


def test_help_requested_reads_sys_argv_by_default(monkeypatch, capsys):
    """Help requested reads sys argv by default."""
    monkeypatch.setattr(sys, "argv", ["tool.py", "--help"])
    with pytest.raises(SystemExit):
        tool_help.help_requested("From argv.")
    assert capsys.readouterr().out == "From argv.\n"
    # The program name itself is never mistaken for a flag.
    monkeypatch.setattr(sys, "argv", ["--help"])
    assert tool_help.help_requested("Not asked.") is None


# ------------------------------------------------------------------------- source_date

def test_epoch_matches_each_documents_declared_date():
    """Epoch matches each documents declared date."""
    book = re.search(r"^DRAFT_DATE = '([^']+)'", (ROOT / "tools/build_book.py").read_text(),
                     re.MULTILINE).group(1)
    primer = re.search(r"^REVISED_DATE = '([^']+)'",
                       (ROOT / "tools/build_primer.py").read_text(), re.MULTILINE).group(1)
    paper = re.search(r"\\date\{\\normalsize ([A-Z][a-z]+ \d{4})",
                      (ROOT / "paper/anonymity-as-an-aggregation-condition.tex").read_text()
                      ).group(1)
    assert source_date.epoch("book") == midnight(book, "%d %B %Y")
    assert source_date.epoch("primer") == midnight(primer, "%d %B %Y")
    assert source_date.epoch("paper") == midnight(paper, "%B %Y")
    assert source_date.declared_date("book").tzinfo is timezone.utc


def test_declared_date_reads_whatever_file_it_is_pointed_at(monkeypatch, tmp_path):
    """Declared date reads whatever file it is pointed at."""
    doc = tmp_path / "doc.txt"
    doc.write_text("noise\nDRAFT_DATE = '1 January 2027'\n")
    monkeypatch.setattr(source_date, "ROOT", tmp_path)
    monkeypatch.setitem(source_date.DECLARED, "book",
                        (doc, r"^DRAFT_DATE = '([^']+)'", "%d %B %Y"))
    assert source_date.epoch("book") == midnight("1 January 2027", "%d %B %Y")


def test_declared_date_refuses_a_file_with_no_declaration(monkeypatch, tmp_path):
    """Declared date refuses a file with no declaration."""
    doc = tmp_path / "doc.txt"
    doc.write_text("nothing declared here\n")
    monkeypatch.setattr(source_date, "ROOT", tmp_path)
    monkeypatch.setitem(source_date.DECLARED, "book",
                        (doc, r"^DRAFT_DATE = '([^']+)'", "%d %B %Y"))
    with pytest.raises(SystemExit) as stop:
        source_date.declared_date("book")
    assert "doc.txt declares no date for the book" in str(stop.value)


def test_source_date_main_prints_the_epoch(monkeypatch, capsys):
    """Source date main prints the epoch."""
    monkeypatch.setattr(sys, "argv", ["source_date.py", "primer"])
    assert source_date.main() == 0
    assert capsys.readouterr().out.strip() == str(source_date.epoch("primer"))


@pytest.mark.parametrize("argv", [["source_date.py"], ["source_date.py", "novel"],
                                  ["source_date.py", "book", "primer"]])
def test_source_date_main_rejects_bad_usage(monkeypatch, capsys, argv):
    """Source date main rejects bad usage."""
    monkeypatch.setattr(sys, "argv", argv)
    assert source_date.main() == 2
    captured = capsys.readouterr()
    assert captured.out == "" and "usage: python3 tools/source_date.py" in captured.err


# ------------------------------------------------------------------ build_primer (direct)

@pytest.fixture
def primer_tree(monkeypatch, tmp_path):
    """Point the primer builder at a temporary tree with a source and only tectonic."""
    src = tmp_path / "reference" / "PRIMER.md"
    src.parent.mkdir()
    src.write_text("# Primer\n\nBody.\n")
    monkeypatch.setattr(build_primer, "ROOT", tmp_path)
    monkeypatch.setattr(build_primer, "SRC", src)
    monkeypatch.setattr(build_primer, "OUT", tmp_path / "reference" / "PRIMER.pdf")
    monkeypatch.setattr(build_primer.shutil, "which", only_tectonic)
    monkeypatch.delenv("SOURCE_DATE_EPOCH", raising=False)
    return tmp_path


def test_primer_refuses_without_its_source(monkeypatch, primer_tree):
    """Primer refuses without its source."""
    monkeypatch.setattr(build_primer, "SRC", primer_tree / "absent.md")
    with pytest.raises(SystemExit) as stop:
        build_primer.main()
    assert "primer source not found" in str(stop.value)


def test_primer_refuses_without_a_pdf_engine(monkeypatch, primer_tree):
    """Primer refuses without a pdf engine."""
    monkeypatch.setattr(build_primer.shutil, "which", lambda _name: None)
    with pytest.raises(SystemExit) as stop:
        build_primer.main()
    assert "no PDF engine found" in str(stop.value)


def test_primer_build_writes_the_header_and_log_and_reports_clean(
        monkeypatch, primer_tree, capsys):
    """Primer build writes the header and log and reports clean."""
    fake = FakePandoc(completed(stdout="all good\n"))
    monkeypatch.setattr(build_primer.subprocess, "run", fake)
    assert build_primer.main() == 0

    (cmd, kwargs), = fake.calls
    assert cmd[0] == "pandoc" and "--pdf-engine=tectonic" in cmd
    assert cmd[cmd.index("-M") + 1] == "date=Revised " + build_primer.REVISED_DATE
    assert "geometry=margin=1in" in cmd and "mainfont=TeX Gyre Pagella" in cmd
    assert kwargs["check"] is False
    # The date stamp comes from the declared date unless the caller already set one.
    assert kwargs["env"]["SOURCE_DATE_EPOCH"] == str(source_date.epoch("primer"))

    header = primer_tree / "build" / "primer-header.tex"
    assert header.read_text() == build_primer.HEADER_INCLUDES.strip() + "\n"
    assert (primer_tree / "build" / "primer-pandoc.log").read_text() == "all good\n"
    out = capsys.readouterr().out
    assert "using tectonic" in out and "overfull boxes: 0" in out and "WARNING" not in out


def test_primer_build_keeps_a_callers_source_date_epoch(monkeypatch, primer_tree):
    """Primer build keeps a callers source date epoch."""
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "12345")
    fake = FakePandoc()
    monkeypatch.setattr(build_primer.subprocess, "run", fake)
    build_primer.main()
    assert fake.calls[0][1]["env"]["SOURCE_DATE_EPOCH"] == "12345"


def test_primer_build_warns_about_overfull_boxes_but_succeeds(monkeypatch, primer_tree, capsys):
    """Primer build warns about overfull boxes but succeeds."""
    monkeypatch.setattr(build_primer.subprocess, "run",
                        FakePandoc(completed(stderr="Overfull \\hbox (3pt too wide)\n")))
    assert build_primer.main() == 0
    out = capsys.readouterr().out
    assert "overfull boxes: 1" in out and "WARNING: content is running outside" in out


def test_primer_failure_shows_the_lines_that_name_it(monkeypatch, primer_tree, capsys):
    """Primer failure shows the lines that name it."""
    monkeypatch.setattr(build_primer.subprocess, "run",
                        FakePandoc(completed(1, "chatter\n! Undefined control sequence.\n")))
    with pytest.raises(SystemExit) as stop:
        build_primer.main()
    assert "pandoc failed, see" in str(stop.value)
    err = capsys.readouterr().err
    assert "! Undefined control sequence." in err and "--- tail ---" in err
    assert (primer_tree / "build" / "primer-pandoc.log").exists()


def test_primer_failure_falls_back_to_the_tail_when_nothing_names_it(
        monkeypatch, primer_tree, capsys):
    """Primer failure falls back to the tail when nothing names it."""
    monkeypatch.setattr(build_primer.subprocess, "run",
                        FakePandoc(completed(1, "only chatter\n")))
    with pytest.raises(SystemExit):
        build_primer.main()
    err = capsys.readouterr().err
    assert "only chatter" in err and "--- tail ---" not in err


# -------------------------------------------------------------------- build_note (direct)

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


@pytest.fixture
def note_tree(monkeypatch, tmp_path):
    """Point the note builder at a temporary tree with a valid note and only tectonic."""
    src = tmp_path / "note.md"
    src.write_text(NOTE)
    monkeypatch.setattr(build_note, "ROOT", tmp_path)
    monkeypatch.setattr(build_note, "SRC", src)
    monkeypatch.setattr(build_note, "OUT", tmp_path / "build" / "note.pdf")
    monkeypatch.setattr(build_note.shutil, "which", only_tectonic)
    return tmp_path


def test_note_prepare_rewrites_the_table_and_drops_the_rules():
    """Note prepare rewrites the table and drops the rules."""
    markdown, title, short, when = build_note.prepare(NOTE)
    assert (title, short, when) == ("Short title: the rest of it", "Short title",
                                    "3 October 2026")
    assert markdown.startswith('---\ntitle: "Short title:`\\\\\\\\`{=latex} the rest of it"\n')
    assert 'date: "*Written on 3 October 2026*"' in markdown
    assert "\n---\n" not in markdown.split("\n---\n\n", 1)[1]          # the in-body rule is gone
    assert markdown.count(build_note.WEIGHTED) == 1
    assert "|---|---|---|" not in markdown
    # Two data rows: room for 2 + 1 + 5 lines is asked for above the heading.
    heading = markdown.index("## Second section")
    assert markdown.index("\\needspace{8\\baselineskip}") < heading


def test_note_prepare_places_the_space_request_above_a_bare_table():
    """Note prepare places the space request above a bare table."""
    note = NOTE.replace("## Second section\n\n", "Text before the table.\n\n")
    note = note.replace("---\n\nText before", "---\n\n## Third section\n\nText before")
    markdown, *_ = build_note.prepare(note)
    assert markdown.index("\\needspace{") < markdown.index(build_note.WEIGHTED)
    assert markdown.index("Text before the table.") < markdown.index("\\needspace{")


@pytest.mark.parametrize("bad, reason", [
    ("no title here\n\n*x*\n\nbody\n", "does not open with a title"),
    ("# T: x\nnot blank\n*Dated 3 October 2026*\n\nok\n", "does not open with a title"),
    ("# NoColon\n\n*Dated 3 October 2026*\n\n## S\n\nbody\n", "unexpected title"),
    ("# T: x\n\n*No date here*\n\n## S\n\nbody\n", "unexpected title"),
    ("# T: x\n\nDated 3 October 2026\n\n## S\n\nbody\n", "unexpected title"),
])
def test_note_prepare_refuses_the_wrong_opening(bad, reason):
    """Note prepare refuses the wrong opening."""
    with pytest.raises(SystemExit) as stop:
        build_note.prepare(bad)
    assert reason in str(stop.value)


def test_note_prepare_refuses_a_rule_that_does_not_open_a_section():
    """Note prepare refuses a rule that does not open a section."""
    note = NOTE.replace("---\n\n## Second section", "---\n\nplain text\n\n## Second section")
    with pytest.raises(SystemExit) as stop:
        build_note.prepare(note)
    assert "line 9: a rule that does not open a section" in str(stop.value)


def test_note_prepare_requires_exactly_one_three_column_table():
    """Note prepare requires exactly one three column table."""
    with pytest.raises(SystemExit) as stop:
        build_note.prepare(NOTE.split("| Page")[0])
    assert "found 0" in str(stop.value)
    with pytest.raises(SystemExit) as stop:
        build_note.prepare(NOTE + "\n" + NOTE.split("## Second section\n\n")[1])
    assert "found 2" in str(stop.value)


def test_note_main_refuses_without_the_note_or_an_engine(monkeypatch, note_tree):
    """Note main refuses without the note or an engine."""
    monkeypatch.setattr(build_note, "SRC", note_tree / "absent.md")
    with pytest.raises(SystemExit) as stop:
        build_note.main()
    assert "note not found" in str(stop.value)

    monkeypatch.setattr(build_note, "SRC", note_tree / "note.md")
    monkeypatch.setattr(build_note.shutil, "which", lambda _name: None)
    with pytest.raises(SystemExit) as stop:
        build_note.main()
    assert "no PDF engine found" in str(stop.value)


def test_note_main_builds_with_the_running_head_filled_in(monkeypatch, note_tree, capsys):
    """Note main builds with the running head filled in."""
    seen = {}

    def run(cmd, **kwargs):
        # The scratch files exist only while pandoc runs, so read them from inside the fake.
        seen["header"] = Path(cmd[cmd.index("--include-in-header") + 1]).read_text()
        seen["markdown"] = Path(cmd[1]).read_text()
        seen["cmd"], seen["kwargs"] = cmd, kwargs
        return completed(stdout="fine\n")

    monkeypatch.setattr(build_note.subprocess, "run", run)
    assert build_note.main() == 0

    assert "@SHORT@" not in seen["header"] and "@DATE@" not in seen["header"]
    assert "Short title" in seen["header"] and "Working note, 3 October 2026" in seen["header"]
    assert seen["markdown"].startswith("---\ntitle: ")
    assert "title-meta=Short title: the rest of it" in seen["cmd"]
    assert "geometry=headheight=14pt" in seen["cmd"] and seen["kwargs"]["check"] is False
    assert (note_tree / "build").is_dir()
    out = capsys.readouterr().out
    assert "wrote build/note.pdf using tectonic" in out and "overfull boxes: 0" in out


def test_note_main_lists_overfull_boxes_without_failing(monkeypatch, note_tree, capsys):
    """Note main lists overfull boxes without failing."""
    monkeypatch.setattr(build_note.subprocess, "run",
                        FakePandoc(completed(stdout="Overfull \\hbox (3pt too wide)\nok\n")))
    assert build_note.main() == 0
    out = capsys.readouterr().out
    assert "overfull boxes: 1" in out and "WARNING" in out
    assert "  Overfull \\hbox (3pt too wide)" in out


def test_note_main_failure_shows_the_lines_that_name_it(monkeypatch, note_tree, capsys):
    """Note main failure shows the lines that name it."""
    monkeypatch.setattr(build_note.subprocess, "run",
                        FakePandoc(completed(1, "chatter\n! Undefined control sequence.\n")))
    with pytest.raises(SystemExit) as stop:
        build_note.main()
    assert str(stop.value) == "pandoc failed"
    err = capsys.readouterr().err
    assert "! Undefined control sequence." in err and "--- tail ---" in err

    monkeypatch.setattr(build_note.subprocess, "run", FakePandoc(completed(1, "only chatter\n")))
    with pytest.raises(SystemExit):
        build_note.main()
    err = capsys.readouterr().err
    assert "only chatter" in err and "--- tail ---" not in err


# -------------------------------------------------------------------- build_book (direct)

def test_read_returns_utf8_text_and_fails_loudly_on_a_missing_file(tmp_path):
    """Read returns utf8 text and fails loudly on a missing file."""
    f = tmp_path / "x.md"
    f.write_text("héllo ₁\n", encoding="utf-8")
    assert build_book.read(f) == "héllo ₁\n"
    with pytest.raises(OSError):
        build_book.read(tmp_path / "absent.md")


def test_strip_front_matter_removes_only_a_leading_yaml_block():
    """Strip front matter removes only a leading yaml block."""
    assert build_book.strip_front_matter("---\ntitle: x\n---\n\n\nBody\n") == "Body\n"
    assert build_book.strip_front_matter("No front matter\n---\nrule\n") == \
        "No front matter\n---\nrule\n"
    # An opening fence that is never closed is left alone rather than eating the document.
    assert build_book.strip_front_matter("---\nunclosed\nBody\n") == "---\nunclosed\nBody\n"


def test_demote_subscripts_maps_all_ten_digits():
    """Demote subscripts maps all ten digits."""
    assert build_book.demote_subscripts("T₁₁ δ₀ ₂₃₄₅₆₇₈₉") == "T11 δ0 23456789"
    assert build_book.demote_subscripts("plain 1") == "plain 1"


def test_merge_title_joins_the_first_two_headings_only():
    """Merge title joins the first two headings only."""
    text = "# Chapter Nine\n\n## Confident and Wrong\n\nBody\n\n# Later\n\n## Other\n"
    merged = build_book.merge_title(text)
    assert merged.startswith("# Chapter Nine: Confident and Wrong\n")
    assert "# Later\n\n## Other" in merged            # count=1: later headings are untouched


def test_part_page_with_and_without_a_subtitle():
    """Part page with and without a subtitle."""
    with_sub = build_book.part_page("Part One", "The First Fellowship")
    assert "{\\Large\\bfseries Part One}\\\\[0.6em]\n{\\large\\itshape The First Fellowship}" \
        in with_sub
    bare = build_book.part_page("Appendices")
    assert "{\\Large\\bfseries Appendices}\n\\end{center}" in bare
    assert "itshape" not in bare


def test_chapter_returns_a_cleaned_chapter_ending_in_one_newline(tmp_path):
    """Chapter returns a cleaned chapter ending in one newline."""
    f = tmp_path / "ch.md"
    f.write_text("---\nx: y\n---\n# Chapter One\n\n## The Title\n\nBody T₁₁.\n\n\n")
    assert build_book.chapter(f) == "# Chapter One: The Title\n\nBody T11.\n"


def test_unwrap_pm_rewrites_plus_minus_and_intervals_in_table_rows_only():
    """Unwrap pm rewrites plus minus and intervals in table rows only."""
    md = ("Prose with [0.9860, 0.9996] and $1.5 \\pm 2.0$ kept as is?\n"
          "| a | $29.40 \\pm 1.16$ | \\[0.9860, 0.9996\\] |\n"
          "  | indented \\[0.1, 0.2\\] |\n")
    out = build_book.unwrap_pm(md)
    lines = out.split("\n")
    # The plus-minus rewrite applies everywhere; the interval rewrite only inside table rows.
    assert lines[0] == "Prose with [0.9860, 0.9996] and 1.5 ± 2.0 kept as is?"
    assert lines[1] == "| a | 29.40 ± 1.16 | 0.9860 to 0.9996 |"
    assert lines[2] == "  | indented 0.1 to 0.2 |"


def test_soften_splits_long_words_at_known_suffixes_only():
    """Soften splits long words at known suffixes only."""
    shy = "\u00ad"
    assert build_book.soften("unwelcoming") == f"unwelcom{shy}ing"
    assert build_book.soften("consideration") == f"considera{shy}tion"
    assert build_book.soften("measurement and understandable") == \
        f"measure{shy}ment and understand{shy}able"
    # "ed" is not a suffix we split, words under eleven letters are left alone, and so are
    # long words with no listed ending.
    assert build_book.soften("hypothesized") == "hypothesized"
    assert build_book.soften("shortening") == "shortening"          # ten letters
    assert build_book.soften("abcdefghijk") == "abcdefghijk"


def test_resolve_paper_crossrefs_replaces_labels_and_references_with_words():
    """Resolve paper crossrefs replaces labels and references with words."""
    def ref(kind, name):
        return f'[\\[{kind}:{name}\\]](#{kind}:{name}){{reference-type="ref" reference="x"}}'

    md = ('Heading [\\[prop:one\\]]{#prop:one label="prop:one"} text\n'
          f"See {ref('eq', 'err')}, {ref('prop', 'one')}, {ref('tab', 'm')}, "
          f"{ref('sec', 's')} and {ref('fig', 'f')}.\n"
          f"Equation {ref('eq', 'err')} and equation ({ref('prop', 'one')}) hold.\n"
          "Equation (the table above) too.\n")
    out = build_book.resolve_paper_crossrefs(md)
    assert "label=" not in out and "[\\[" not in out
    assert ("See the consensus-error equation above, the proposition above, the table above, "
            "the section above and above.") in out
    assert "Equation the" not in out and "equation the" not in out
    assert "the consensus-error equation above and the proposition above hold." in out
    assert "the table above too." in out


def test_resolve_paper_crossrefs_escapes_list_markers_in_table_cells():
    """Resolve paper crossrefs escapes list markers in table cells."""
    md = "\n| 2. Welfare | x |\n  3. indented\n  . lost one\n| . piped lost one\nplain 4. text\n"
    out = build_book.resolve_paper_crossrefs(md)
    assert "\n| 2\\. Welfare | x |" in out
    assert "\n  3\\. indented" in out
    assert "\n  1\\. lost one" in out
    assert "\n| 1\\. piped lost one" in out
    assert "plain 4. text" in out


def test_convert_paper_runs_pandoc_and_tidies_the_result(monkeypatch):
    """Convert paper runs pandoc and tidies the result."""
    fake = FakePandoc(completed(stdout="T₁ value $1.5 \\pm 2$ here\n\n"))
    monkeypatch.setattr(build_book.subprocess, "run", fake)
    assert build_book.convert_paper() == "T1 value 1.5 ± 2 here\n"
    (cmd, kwargs), = fake.calls
    assert cmd[:2] == ["pandoc", build_book.PAPER_TEX]
    assert "--shift-heading-level-by=1" in cmd and "markdown-simple_tables" in cmd
    assert kwargs["check"] is True


@pytest.mark.parametrize("failure", [FileNotFoundError("pandoc"),
                                     completed(returncode=2)])
def test_convert_paper_stops_the_build_when_pandoc_is_unusable(monkeypatch, failure):
    """Convert paper stops the build when pandoc is unusable."""
    monkeypatch.setattr(build_book.subprocess, "run", FakePandoc(failure))
    with pytest.raises(SystemExit) as stop:
        build_book.convert_paper()
    assert "could not convert the paper" in str(stop.value)


def make_book_tree(root: Path) -> None:
    """Create the minimum source tree `assemble` reads, with a recognisable line in each."""
    manuscript = root / "manuscript"
    manuscript.mkdir(parents=True)
    names = ["ch00-preface.md", "ch00b-introduction.md"]
    names += [name for _title, _sub, files in build_book.PARTS for name in files]
    for number, name in enumerate(names):
        (manuscript / name).write_text(
            f"---\nignored: yes\n---\n# Chapter {number}\n\n## Title {number}\n\nBody T₁₁ {name}\n")
    (root / "appendix").mkdir()
    (root / "appendix" / "APPENDIX.md").write_text("# Technical Appendix\n\nAppendix body δ₀.\n")
    (root / "reference").mkdir()
    (root / "reference" / "PRIMER-steps-and-traditions.md").write_text(
        "---\ntitle: Primer\n---\n# Primer title\n\nPrimer body T₃.\n")


@pytest.fixture
def book_tree(monkeypatch, tmp_path):
    """Point the book builder at a temporary tree and a fake pandoc."""
    make_book_tree(tmp_path)
    build = tmp_path / "build"
    monkeypatch.setattr(build_book, "ROOT", tmp_path)
    monkeypatch.setattr(build_book, "BUILD", str(build))
    monkeypatch.setattr(build_book, "OUT_MD", str(build / "book.md"))
    monkeypatch.setattr(build_book, "OUT_PDF", str(build / "book.pdf"))
    monkeypatch.setattr(build_book, "PAPER_TEX", str(tmp_path / "paper.tex"))
    monkeypatch.setattr(build_book.shutil, "which", only_tectonic)
    monkeypatch.delenv("SOURCE_DATE_EPOCH", raising=False)
    fake = FakePandoc(completed(stdout="Paper text T₂.\n"))
    monkeypatch.setattr(build_book.subprocess, "run", fake)
    return tmp_path, fake


def test_assemble_orders_the_book_and_transforms_only_the_copy(book_tree):
    """Assemble orders the book and transforms only the copy."""
    root, _fake = book_tree
    before = {p: p.read_bytes() for p in root.rglob("*.md")}
    text = build_book.assemble("1 May 2027")

    assert text.startswith('---\ntitle: "Nobody in Charge"')
    assert 'date: "Draft of 1 May 2027"' in text
    # Front matter in chapters is stripped, titles merged, subscripts demoted.
    assert "ignored: yes" not in text and "₁" not in text and "₀" not in text
    assert "# Chapter 0: Title 0\n" in text and "Body T11 ch01-chases-tavern.md" in text
    # Order: preface, introduction, then Parts One to Six, then the three appendices.
    marks = ["ch00-preface.md", "ch00b-introduction.md", "Part One", "ch01-chases-tavern.md",
             "Part Two", "Part Three", "Part Four", "Part Five", "Part Six",
             "ch25-what-a-model-cannot-tell-you.md", "Appendices", "# Technical Appendix",
             "# Appendix: What the Model Says About the Twelve Steps and the Twelve Traditions",
             "# Appendix: The Working Paper", "Paper text T2."]
    positions = [text.index(m) for m in marks]
    assert positions == sorted(positions)
    # The primer's own H1 is replaced, not repeated, and its front matter is gone.
    assert "Primer title" not in text and "title: Primer" not in text
    assert "Primer body T3." in text
    # Sources are never written to.
    assert {p: p.read_bytes() for p in root.rglob("*.md")} == before


def test_assemble_includes_the_appendix_body_with_subscripts_demoted(book_tree):
    """Assemble includes the appendix body with subscripts demoted."""
    text = build_book.assemble("1 May 2027")
    assert "Appendix body δ0." in text


def test_main_writes_the_markdown_and_stops_with_no_pdf(monkeypatch, book_tree, capsys):
    """Main writes the markdown and stops with no pdf."""
    root, fake = book_tree
    monkeypatch.setattr(sys, "argv", ["build_book.py", "--no-pdf", "--date", "2 June 2028"])
    assert build_book.main() is None
    md = (root / "build" / "book.md").read_text()
    assert 'date: "Draft of 2 June 2028"' in md
    assert re.search(r"wrote .*book\.md, \d+ words", capsys.readouterr().out)
    assert len(fake.calls) == 1                        # only the paper conversion; no render


def test_main_uses_the_declared_date_and_ignores_a_dangling_date_flag(monkeypatch, book_tree):
    """Main uses the declared date and ignores a dangling date flag."""
    root, _fake = book_tree
    monkeypatch.setattr(sys, "argv", ["build_book.py", "--no-pdf", "--date"])
    build_book.main()
    assert f'date: "Draft of {build_book.DRAFT_DATE}"' in (root / "build" / "book.md").read_text()


def test_main_renders_the_pdf_with_a_fixed_timestamp(monkeypatch, book_tree, capsys):
    """Main renders the pdf with a fixed timestamp."""
    root, fake = book_tree
    monkeypatch.setattr(sys, "argv", ["build_book.py"])
    build_book.main()
    cmd, kwargs = fake.calls[-1]
    assert cmd[0] == "pandoc" and cmd[1] == str(root / "build" / "book.md")
    assert "--pdf-engine=tectonic" in cmd and "--top-level-division=chapter" in cmd
    assert kwargs["check"] is False
    assert kwargs["env"]["SOURCE_DATE_EPOCH"] == str(source_date.epoch("book"))
    assert (root / "build" / "pandoc.log").read_text() == "Paper text T₂.\n"
    assert "using tectonic" in capsys.readouterr().out


def test_main_keeps_a_callers_source_date_epoch(monkeypatch, book_tree):
    """Main keeps a callers source date epoch."""
    _root, fake = book_tree
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "999")
    monkeypatch.setattr(sys, "argv", ["build_book.py"])
    build_book.main()
    assert fake.calls[-1][1]["env"]["SOURCE_DATE_EPOCH"] == "999"


def test_main_needs_a_pdf_engine_unless_told_not_to_render(monkeypatch, book_tree):
    """Main needs a pdf engine unless told not to render."""
    monkeypatch.setattr(build_book.shutil, "which", lambda _name: None)
    monkeypatch.setattr(sys, "argv", ["build_book.py"])
    with pytest.raises(SystemExit) as stop:
        build_book.main()
    assert "no PDF engine found" in str(stop.value)


def test_main_failure_shows_the_lines_that_name_it(monkeypatch, book_tree, capsys):
    """Main failure shows the lines that name it."""
    _root, _fake = book_tree
    calls = {"n": 0}

    def run(cmd, **kwargs):
        calls["n"] += 1
        if calls["n"] == 1:                              # the paper conversion succeeds
            return completed(stdout="Paper text.\n")
        return completed(1, "chatter\n! LaTeX Error: File not found.\n")

    monkeypatch.setattr(build_book.subprocess, "run", run)
    monkeypatch.setattr(sys, "argv", ["build_book.py"])
    with pytest.raises(SystemExit) as stop:
        build_book.main()
    assert "pandoc failed, see" in str(stop.value) and "pandoc.log" in str(stop.value)
    err = capsys.readouterr().err
    assert "! LaTeX Error: File not found." in err and "--- tail ---" in err


def test_main_failure_falls_back_to_the_tail(monkeypatch, book_tree, capsys):
    """Main failure falls back to the tail."""
    calls = {"n": 0}

    def run(cmd, **kwargs):
        calls["n"] += 1
        return completed(stdout="Paper text.\n") if calls["n"] == 1 else completed(1, "dull\n")

    monkeypatch.setattr(build_book.subprocess, "run", run)
    monkeypatch.setattr(sys, "argv", ["build_book.py"])
    with pytest.raises(SystemExit):
        build_book.main()
    err = capsys.readouterr().err
    assert "dull" in err and "--- tail ---" not in err


# ------------------------------------------------------- command lines, as a user runs them

TOOLS_WITH_MAIN = ["build_book.py", "build_primer.py", "build_note.py", "source_date.py"]


def clean_env(**extra: str) -> dict[str, str]:
    """Return the environment for a command-line run: no inherited date stamp, no coverage hooks.

    The end-to-end tests run copies of the tools from a temporary tree. Leaving the coverage
    variables in place would make the coverage subprocess patch measure those copies as extra
    files, which are not the repository's tools and would only dilute the report.
    """
    env = {k: v for k, v in os.environ.items()
           if k != "SOURCE_DATE_EPOCH" and not k.startswith("COVERAGE")}
    env.update(extra)
    return env


def run_cli(script: Path, *args: str, cwd: Path, path: str | None = None):
    """Run a tool as a command and capture it, with an optional replacement PATH."""
    env = clean_env(**({"PATH": path} if path is not None else {}))
    return subprocess.run([sys.executable, str(script), *args], cwd=cwd, env=env,
                          capture_output=True, text=True, timeout=120, check=False)


@pytest.mark.parametrize("tool", TOOLS_WITH_MAIN)
def test_help_flag_prints_the_docstring_and_runs_nothing(tool, tmp_path):
    """Help flag prints the docstring and runs nothing."""
    result = run_cli(ROOT / "tools" / tool, "--help", cwd=tmp_path)
    assert result.returncode == 0, result.stderr
    first = {"build_book.py": "Assemble the whole book",
             "build_primer.py": "Render the standalone reference primer",
             "build_note.py": "Render the 1939 working-manuscript note",
             "source_date.py": "Print the build timestamp"}[tool]
    assert first in result.stdout and "Exit codes:" in result.stdout
    assert list(tmp_path.iterdir()) == []


def test_source_date_command_line(tmp_path):
    """Source date command line."""
    script = ROOT / "tools" / "source_date.py"
    ok = run_cli(script, "book", cwd=tmp_path)
    assert ok.returncode == 0 and ok.stdout.strip() == str(source_date.epoch("book"))
    bad = run_cli(script, "nonsense", cwd=tmp_path)
    assert bad.returncode == 2 and "usage:" in bad.stderr


def stub_toolchain(tmp_path: Path) -> str:
    """Create stub `pandoc` and `tectonic` executables and return a PATH that finds them.

    The stub pandoc writes a placeholder PDF when given `-o`, and otherwise prints Markdown
    to standard output the way the paper conversion expects. It reports one overfull box when
    `FAKE_OVERFULL` is set, and fails when `FAKE_FAIL` is set.
    """
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    pandoc = bin_dir / "pandoc"
    pandoc.write_text(
        f"#!{sys.executable}\n"
        "import os, sys\n"
        "args = sys.argv[1:]\n"
        "if os.environ.get('FAKE_FAIL'):\n"
        "    print('! Undefined control sequence.'); sys.exit(1)\n"
        "if '-o' in args:\n"
        "    open(args[args.index('-o') + 1], 'wb').write(b'%PDF-stub')\n"
        "    print('Overfull \\\\hbox (1pt too wide)' if os.environ.get('FAKE_OVERFULL') "
        "else 'ok')\n"
        "else:\n"
        "    print('Paper text.')\n")
    tectonic = bin_dir / "tectonic"
    tectonic.write_text("#!/bin/sh\nexit 0\n")
    for stub in (pandoc, tectonic):
        stub.chmod(stub.stat().st_mode | stat.S_IXUSR)
    return str(bin_dir) + os.pathsep + os.environ["PATH"]


def copy_tools(tmp_path: Path) -> Path:
    """Copy the tools a builder needs into `tmp_path/tools`, so ROOT resolves to `tmp_path`."""
    dest = tmp_path / "tools"
    dest.mkdir()
    for name in ("build_book.py", "build_primer.py", "source_date.py", "tool_help.py"):
        shutil.copy(ROOT / "tools" / name, dest / name)
    return dest


def test_primer_command_line_end_to_end_with_stub_pandoc(tmp_path):
    """Primer command line end to end with stub pandoc."""
    tools = copy_tools(tmp_path)
    (tmp_path / "reference").mkdir()
    (tmp_path / "reference" / "PRIMER-steps-and-traditions.md").write_text("# Primer\n")
    path = stub_toolchain(tmp_path)

    ok = run_cli(tools / "build_primer.py", cwd=tmp_path, path=path)
    assert ok.returncode == 0, ok.stdout + ok.stderr
    assert "overfull boxes: 0" in ok.stdout
    assert (tmp_path / "reference" / "PRIMER-steps-and-traditions.pdf").read_bytes() \
        == b"%PDF-stub"
    assert (tmp_path / "build" / "primer-header.tex").exists()

    (tmp_path / "reference" / "PRIMER-steps-and-traditions.md").unlink()
    gone = run_cli(tools / "build_primer.py", cwd=tmp_path, path=path)
    assert gone.returncode == 1 and "primer source not found" in gone.stderr


def test_book_command_line_end_to_end_with_stub_pandoc(tmp_path):
    """Book command line end to end with stub pandoc."""
    tools = copy_tools(tmp_path)
    make_book_tree(tmp_path)
    path = stub_toolchain(tmp_path)

    ok = run_cli(tools / "build_book.py", "--date", "5 May 2029", cwd=tmp_path, path=path)
    assert ok.returncode == 0, ok.stdout + ok.stderr
    assert 'date: "Draft of 5 May 2029"' in (tmp_path / "build" / "nobody-in-charge.md").read_text()
    assert (tmp_path / "build" / "nobody-in-charge.pdf").read_bytes() == b"%PDF-stub"

    # A failing render exits 1 and names the failure; the repository is untouched either way.
    failed = subprocess.run([sys.executable, str(tools / "build_book.py")], cwd=tmp_path,
                            env=clean_env(FAKE_FAIL="1", PATH=path), capture_output=True,
                            text=True, timeout=120, check=False)
    assert failed.returncode == 1
    assert "could not convert the paper" in failed.stderr
