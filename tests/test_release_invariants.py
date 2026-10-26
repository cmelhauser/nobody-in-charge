"""Frozen release invariants.

CLAUDE.md states a small number of facts as non-negotiable for this release. Each one
is pinned here so that changing it fails the build loudly, rather than being noticed by
a reader comparing prose against a cache.

If one of these tests fails, the correct response is almost never to edit the test.
It is to establish whether the model was changed deliberately, and if so to run the
whole synchronization rule in CLAUDE.md before touching this file.

Run with `python3 -m pytest tests/test_release_invariants.py`. These tests read the model,
CLAUDE.md, the appendix and the model-choice inventory from the repository root; they need
no source document and no network.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

import aa_group_model as m
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# The canonical model identity, quoted in CLAUDE.md and the appendix (both checked below),
# the README and other documents.
CANONICAL_MODEL_SHA256 = "c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952"


def test_canonical_model_hash_is_unchanged():
    """The model file's SHA-256 equals the release identity, so any edit to it fails the build."""
    digest = hashlib.sha256((ROOT / "model" / "aa_group_model.py").read_bytes()).hexdigest()
    assert digest == CANONICAL_MODEL_SHA256, (
        "model/aa_group_model.py has changed. Every hash-linked cache, both notebooks, "
        "the appendix, the paper and the primer are pinned to the old digest. See the "
        "synchronization rule in CLAUDE.md before proceeding."
    )


def test_the_documents_agree_with_the_model_hash():
    """The digest is quoted in prose in several places; none may drift."""
    for relative in ("CLAUDE.md", "appendix/APPENDIX.md"):
        text = (ROOT / relative).read_text(encoding="utf-8", errors="ignore")
        assert CANONICAL_MODEL_SHA256 in text, f"{relative} no longer quotes the model hash"


def test_room_capacity_remains_sixty():
    """The release did not increase membership to 400 or 1,000."""
    assert m.DEFAULTS["cap"] == 60


def test_viability_threshold_remains_five():
    """The endpoint viability line stays at N > 5, as every cache and chapter assumes."""
    assert m.VIABILITY_THRESHOLD == 5


def test_registered_sensitivity_values_decompose_to_one_hundred_and_eighteen():
    """22 scalar defaults, 12 step speeds, 49 nonzero S cells, 35 nonzero GOV cells."""
    scalars = [k for k, v in m.DEFAULTS.items() if not isinstance(v, np.ndarray)]
    step_speeds = len(np.asarray(m.DEFAULTS["a"]))
    s_cells = int((m.S != 0).sum())
    gov_cells = int((m.GOV != 0).sum())
    assert (len(scalars), step_speeds, s_cells, gov_cells) == (22, 12, 49, 35)
    assert len(scalars) + step_speeds + s_cells + gov_cells == 118


def test_the_model_choice_inventory_matches_the_current_model():
    """tools/check_release.py enforces this too; it is pinned here so a unit run catches it."""
    inventory = ROOT / "research" / "model-choice-inventory.json"
    assert inventory.exists()
    data = json.loads(inventory.read_text())
    assert data["model_sha256"] == CANONICAL_MODEL_SHA256


def test_semantic_and_executable_objects_stay_distinct():
    """A1 forbids collapsing B and C. A refactor that made them equal would be a bug."""
    assert not np.allclose(m.semantic_overlap(), m.executable_linear_coupling())


def _undocumented(path: Path) -> list[tuple[str, int]]:
    """Return (name, line) for every module, class and function in `path` with no docstring."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = [] if ast.get_docstring(tree) else [("<module>", 1)]
    for node in ast.walk(tree):
        kinds = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
        if isinstance(node, kinds) and not ast.get_docstring(node):
            found.append((node.name, node.lineno))
    return found


def test_every_definition_in_the_tools_and_tests_has_a_docstring():
    """Every module, class, function, method and nested helper in tools/ and tests/ is documented.

    ruff's D rules cover the public definitions; this walk also covers nested helpers and
    private functions, so the code stays fully commented, not just mostly.
    """
    missing = [f"{path.relative_to(ROOT)}:{line} {name}"
               for folder in ("tools", "tests")
               for path in sorted((ROOT / folder).glob("*.py"))
               for name, line in _undocumented(path)]
    assert missing == []


def test_every_undocumented_frozen_definition_is_described_in_the_sidecar():
    """Each definition in model/*.py without a docstring has a row in model/FUNCTIONS.md.

    The model scripts are hash-frozen and cannot gain docstrings, so model/FUNCTIONS.md carries
    them. A row is `name (line)`; this fails if a script gains an undocumented definition or the
    line numbers drift, which means the sidecar needs regenerating (and the script was edited).
    """
    sidecar = (ROOT / "model" / "FUNCTIONS.md").read_text(encoding="utf-8")
    missing = [f"{path.name}:{line} {name}"
               for path in sorted((ROOT / "model").glob("*.py"))
               for name, line in _undocumented(path)
               if f"`{name} ({line})`" not in sidecar]
    assert missing == []
