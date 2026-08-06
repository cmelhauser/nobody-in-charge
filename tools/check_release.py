#!/usr/bin/env python3
"""Independent release gate for model, caches, notebooks, prose, and PDFs.

This checker deliberately overlaps the notebook and book checkers. A release gate should
fail closed when an analysis is incomplete, hash-stale, semantically inconsistent, or when
a rendered artifact predates its source.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "model" / "aa_group_model.py"

CACHES = {
    "release_gate_results.json": ("meta", "model/release_gate_analysis.py"),
    "scenarios_hiseed.json": ("meta", "model/scenarios_hiseed.py"),
    "ch15_service.json": ("meta", "model/ch15_service.py"),
    "core_thresholds.json": ("meta", "model/core_thresholds.py"),
    "part5.json": ("meta", "model/part5_runs.py"),
    "ch14_sweep.json": ("meta", "model/ch14_sweep.py"),
    "ch14_individual.json": ("meta", "model/ch14_individual.py"),
    "mc_error.json": ("meta", "model/mc_error.py"),
    "morris.json": ("meta", "model/morris_screen.py"),
    "oat_full.json": ("meta", "model/sensitivity_oat_full.py"),
    "sobol.json": ("meta", "model/sobol_indices.py"),
    "structural.json": ("meta", "model/structural_variants.py"),
    "tradition_paired.json": ("meta", "model/tradition_paired.py"),
    "sens3.json": ("_meta", "model/sensitivity_uniform.py"),
    "tiered.json": ("_meta", "model/sensitivity_tiered.py"),
    "ch13_reps.json": ("meta", "model/ch13_reps.py"),
    "part2_influence.json": ("meta", "model/part2_influence.py"),
    "resource_list.json": ("meta", "model/resource_list_test.py"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_model():
    spec = importlib.util.spec_from_file_location("release_check_model", MODEL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    failures: list[str] = []
    notes: list[str] = []
    model_hash = sha256(MODEL)

    def require(ok: bool, message: str):
        (notes if ok else failures).append(("OK: " if ok else "FAIL: ") + message)

    for filename, (meta_key, script_name) in CACHES.items():
        path = ROOT / "research" / filename
        require(path.exists(), f"cache exists: research/{filename}")
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text())
        except Exception as exc:
            failures.append(f"FAIL: research/{filename} is not valid JSON: {exc}")
            continue
        meta = data.get(meta_key, {})
        require(meta.get("status") == "complete", f"research/{filename} status is complete")
        if "model_sha256" in meta:
            require(meta["model_sha256"] == model_hash,
                    f"research/{filename} matches current model hash")
        expected = meta.get("jobs_expected")
        completed = meta.get("jobs_completed")
        if expected is not None:
            require(completed == expected,
                    f"research/{filename} completed {expected} registered jobs")
        script = ROOT / script_name
        require(script.exists(), f"analysis source exists: {script_name}")
        if script.exists() and "script_sha256" in meta:
            require(meta["script_sha256"] == sha256(script),
                    f"research/{filename} matches current analysis hash")

    # Expanded perturbation designs requested for this release.
    sens = json.loads((ROOT / "research" / "sens3.json").read_text()).get("_meta", {})
    require(sens.get("global_draws_completed") == 1002,
            "global screen contains 1,002 independent perturbation draws")
    tier = json.loads((ROOT / "research" / "tiered.json").read_text()).get("_meta", {})
    require(tier.get("tiered_draws_completed") == 1000,
            "tiered screen contains 1,000 perturbation draws")
    require(tier.get("random_matrix_draws_completed") == 1000,
            "randomized-matrix screen contains 1,000 perturbation draws")
    oat = json.loads((ROOT / "research" / "oat_full.json").read_text()).get("meta", {})
    require(oat.get("perturbations_completed") == 944,
            "multi-level OAT contains 944 perturbation points")
    morris = json.loads((ROOT / "research" / "morris.json").read_text()).get("meta", {})
    require(morris.get("r") == 20, "Morris screen contains 20 trajectories")
    sobol = json.loads((ROOT / "research" / "sobol.json").read_text()).get("meta", {})
    require(sobol.get("n_base") == 1024, "Sobol design has a 1,024-row base sample")

    robustness_report = ROOT / "research" / "ROBUSTNESS-RESULTS.md"
    require(robustness_report.exists(), "expanded robustness report exists")
    if robustness_report.exists():
        cache_paths = [ROOT / "research" / name for name in CACHES]
        require(robustness_report.stat().st_mtime >= max(p.stat().st_mtime for p in cache_paths),
                "expanded robustness report is newer than every registered cache")

    # Executable semantic invariants.
    mm = load_model()
    require(mm.DEFAULTS["cap"] == 60, "modeled room capacity remains 60")
    require(mm.semantic_overlap().shape == (12, 12), "semantic overlap is 12 by 12")
    require(mm.executable_linear_coupling().shape == (12, 12),
            "linear executable coupling is 12 by 12")
    require(not (mm.semantic_overlap() == mm.executable_linear_coupling()).all(),
            "semantic and executable coupling objects remain distinct")
    forced = mm.simulate(mm.FULL, P={"drop0": 10.0, "churn": 10.0, "lam_exog": 100.0},
                         seed=9, n_seed=1, x_seed=0.0, T_end=2, record=True)
    require(forced["closed"] and forced["N"] == 0,
            "zero membership is absorbing before same-step arrivals")
    require(forced["history"]["time_weeks"][0] == 0.0,
            "recorded histories include the time-zero state")

    inventory = json.loads((ROOT / "research" / "model-choice-inventory.json").read_text())
    require(inventory.get("model_sha256") == model_hash,
            "model-choice inventory matches current model hash")
    require(inventory.get("registered_set", {}).get("total") == 118,
            "registered sensitivity set is 118 values")
    require(inventory.get("protective_index_step_consumption_cells") == 17,
            "protective index-step count is 17, not 35")

    require((ROOT / "research" / "staged").is_dir(),
            "deferred next-round corpus remains under research/staged")
    require((ROOT / "research" / "incorporated" / "Maxwell_1950").is_dir(),
            "Maxwell active source is under research/incorporated")
    require((ROOT / "research" / "incorporated" / "Golub_Jackson_2010").is_dir(),
            "Golub-Jackson active source is under research/incorporated")

    # Notebook stored-output integrity. End-to-end execution is a separate required command.
    for rel in ("model/book-calculations.ipynb",
                "paper/anonymity-as-an-aggregation-condition.ipynb"):
        path = ROOT / rel
        nb = json.loads(path.read_text())
        code = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]
        require(all(c.get("outputs") for c in code), f"{rel} has stored output for every code cell")
        rendered = "\n".join(json.dumps(c.get("outputs", [])) for c in code)
        require("Traceback" not in rendered and "  FAIL" not in rendered,
                f"{rel} stores no traceback or failed assertion")

    # Public language that would reintroduce audited semantic errors.
    public = [*sorted((ROOT / "manuscript").glob("*.md")),
              ROOT / "appendix" / "APPENDIX.md",
              ROOT / "reference" / "PRIMER-steps-and-traditions.md",
              ROOT / "paper" / "anonymity-as-an-aggregation-condition.tex"]
    joined = "\n".join(p.read_text() for p in public)
    banned = {
        r"exactly two simulation (claims|results).*survive":
            "no universal two-result sensitivity claim",
        r"the model found the (two-tier )?division":
            "two-tier coding is not described as model-discovered",
        r"at least three instruments per latent":
            "rho exercise does not claim a three-instrument rule",
        r"dead groups count as zero":
            "endpoint nonviability is not mislabeled as death",
    }
    for pattern, label in banned.items():
        require(re.search(pattern, joined, re.I | re.S) is None, label)

    # Rendered artifacts must not predate their public sources.
    artifacts = {
        "build/nobody-in-charge.pdf": [*public, ROOT / "tools" / "build_book.py"],
        "paper/anonymity-as-an-aggregation-condition.pdf":
            [ROOT / "paper" / "anonymity-as-an-aggregation-condition.tex"],
        "reference/PRIMER-steps-and-traditions.pdf":
            [ROOT / "reference" / "PRIMER-steps-and-traditions.md"],
    }
    for rel, sources in artifacts.items():
        artifact = ROOT / rel
        require(artifact.exists() and artifact.stat().st_size > 10_000,
                f"rendered artifact exists and is nontrivial: {rel}")
        if artifact.exists():
            require(artifact.stat().st_mtime >= max(p.stat().st_mtime for p in sources),
                    f"rendered artifact is newer than its sources: {rel}")

    for line in notes:
        print(line)
    for line in failures:
        print(line)
    print(f"\n{len(notes)} checks passed; {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
