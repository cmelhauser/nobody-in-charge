"""Frozen release invariants.

CLAUDE.md states a small number of facts as non-negotiable for this release. Each one
is pinned here so that changing it fails the build loudly, rather than being noticed by
a reader comparing prose against a cache.

If one of these tests fails, the correct response is almost never to edit the test.
It is to establish whether the model was changed deliberately, and if so to run the
whole synchronization rule in CLAUDE.md before touching this file.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import aa_group_model as m

ROOT = Path(__file__).resolve().parents[1]

# The canonical model identity quoted in CLAUDE.md, the appendix, and the README.
CANONICAL_MODEL_SHA256 = "c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952"


def test_canonical_model_hash_is_unchanged():
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
    assert m.VIABILITY_THRESHOLD == 5


def test_registered_sensitivity_values_decompose_to_one_hundred_and_eighteen():
    """22 scalar defaults, 12 step speeds, 49 nonzero S cells, 35 nonzero GOV cells."""
    scalars = [k for k, v in m.DEFAULTS.items() if not isinstance(v, np.ndarray)]
    step_speeds = len(m.DEFAULTS["a"])
    s_cells = int((m.S != 0).sum())
    gov_cells = int((m.GOV != 0).sum())
    assert (len(scalars), step_speeds, s_cells, gov_cells) == (22, 12, 49, 35)
    assert len(scalars) + step_speeds + s_cells + gov_cells == 118


def test_the_model_choice_inventory_matches_the_current_model():
    """tools/check_release.py enforces this too; it is pinned here so a unit run catches it."""
    inventory = ROOT / "research" / "model-choice-inventory.json"
    if not inventory.exists():
        return
    data = json.loads(inventory.read_text())
    recorded = data.get("model_sha256") or data.get("model_hash")
    if recorded:
        assert recorded == CANONICAL_MODEL_SHA256


def test_semantic_and_executable_objects_stay_distinct():
    """A1 forbids collapsing B and C. A refactor that made them equal would be a bug."""
    assert not np.allclose(m.semantic_overlap(), m.executable_linear_coupling())
