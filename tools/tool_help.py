"""`-h` and `--help` for the command-line tools: print the tool's own docstring and stop.

Until 29 September 2026 only `freeze_release_manifest.py`, which uses argparse, answered
`--help`. Every other tool ignored arguments it did not know, so asking one for help ran it:
`build_book.py --help` rebuilt the book, `regenerate_notebooks.py --help` rewrote both
notebooks, and `build_corpus.py --help` normalized the corpus. Each tool's docstring already
says what it does and how to run it, so that is what `--help` now prints, before anything else
happens. `tests/test_tools_integration.py` runs every tool with `--help` and fails if one does
not exit cleanly with its docstring or changes a tracked file.

Each tool calls this first thing in its `if __name__ == "__main__":` block, so importing a tool
from a test is unaffected.
"""
from __future__ import annotations

import sys


def help_requested(doc: str | None, argv: list[str] | None = None) -> None:
    """Print `doc` and exit 0 if the arguments ask for help; otherwise return."""
    args = sys.argv[1:] if argv is None else argv
    if any(arg in ("-h", "--help") for arg in args):
        print((doc or "No usage is documented for this tool.").strip())
        raise SystemExit(0)
