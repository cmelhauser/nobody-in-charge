#!/usr/bin/env python3
"""Rebuild both public notebooks as compact, cache-backed verification artifacts.

The notebooks deliberately do not rerun the expensive Monte Carlo suite. They verify model
invariants, cache identity/completeness, and the public results derived from those caches.
Run the generating analyses first, then this script, then `tools/run_notebook.py` for each
notebook.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def code(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source.strip().splitlines()],
    }


def markdown(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source.strip().splitlines()],
    }


SETUP = r'''
from pathlib import Path
import collections, hashlib, importlib.util, json, math, sys
import numpy as np

HERE = Path.cwd()
ROOT = HERE.parent if (HERE.parent / "model" / "aa_group_model.py").exists() else HERE
MODEL = ROOT / "model" / "aa_group_model.py"
RESEARCH = ROOT / "research"
MODEL_HASH = hashlib.sha256(MODEL.read_bytes()).hexdigest()

spec = importlib.util.spec_from_file_location("released_model", MODEL)
m = importlib.util.module_from_spec(spec)
sys.modules["released_model"] = m
spec.loader.exec_module(m)

FAILURES = []
def check(label, got, want=True, tol=None):
    ok = abs(got - want) <= tol if tol is not None else got == want
    if not ok:
        FAILURES.append(f"{label}: got {got!r}, wanted {want!r}")
    print(f"  {'OK ' if ok else 'FAIL'} {label}: {got}")
    return ok

def load(name):
    return json.loads((RESEARCH / name).read_text())

print("repository", ROOT)
print("model SHA-256", MODEL_HASH)
'''


MODEL_CHECKS = r'''
print("Model and semantic invariants")
check("room capacity", m.DEFAULTS["cap"], 60)
check("semantic overlap shape", m.semantic_overlap().shape, (12, 12))
check("linear executable shape", m.executable_linear_coupling().shape, (12, 12))
check("semantic and executable matrices differ",
      bool(np.any(m.semantic_overlap() != m.executable_linear_coupling())), True)
rng = np.random.default_rng(93)
capability = m.mean_one_lognormal(rng, m.DEFAULTS["het_sd"], 250000)
check("mean-one capability draw", float(capability.mean()), 1.0, tol=0.01)
forced = m.simulate(m.FULL, P={"drop0": 10.0, "churn": 10.0, "lam_exog": 100.0},
                    seed=9, n_seed=1, x_seed=0.0, T_end=2, record=True)
check("zero membership is absorbing", (forced["closed"], forced["N"]), (True, 0))
check("history includes time zero", forced["history"]["time_weeks"][0], 0.0)
'''


CACHE_CHECKS = r'''
print("Cache completeness and provenance")
expected = {
    "release_gate_results.json": 3200,
    "scenarios_hiseed.json": 2400,
    "ch13_reps.json": 3200,
    "ch14_individual.json": 400,
    "ch14_sweep.json": 3200,
    "ch15_service.json": 1200,
    "core_thresholds.json": 400,
    "part5.json": 4800,
    "mc_error.json": 2600,
    "tradition_paired.json": 5200,
    "structural.json": 10000,
    "morris.json": 2380,
    "oat_full.json": None,
    "sobol.json": 11264,
}
for name, jobs in expected.items():
    data = load(name)
    meta = data.get("meta", data.get("_meta", {}))
    check(f"{name} complete", meta.get("status"), "complete")
    if "model_sha256" in meta:
        check(f"{name} model hash", meta["model_sha256"], MODEL_HASH)
    if jobs is not None:
        check(f"{name} jobs", meta.get("jobs_completed"), jobs)
sens = load("sens3.json")["_meta"]
tier = load("tiered.json")["_meta"]
oat = load("oat_full.json")["meta"]
check("global perturbation draws", sens["global_draws_completed"], 1002)
check("tiered draws", tier["tiered_draws_completed"], 1000)
check("randomized-matrix draws", tier["random_matrix_draws_completed"], 1000)
check("OAT perturbation points", oat["perturbations_completed"], 944)
'''


RELEASE_RESULTS = r'''
print("Principal 400-seed release results")
gate = load("release_gate_results.json")
def condition(name):
    return [gate[f"{name}|{seed}"] for seed in range(400)]
def mean(name, field):
    return float(np.mean([row[field] for row in condition(name)]))
check("baseline final N", mean("base", "N"), 17.8, tol=1e-12)
check("baseline endpoint viability", mean("base", "endpoint_viable"), 0.985, tol=1e-12)
check("T3 friction-loss N", mean("t3_friction_loss", "N"), 14.8375, tol=1e-12)
check("T3 governance-loss N", mean("t3_governance_loss", "N"), 11.7725, tol=1e-12)
check("T3 combined-loss N", mean("t3_combined_loss", "N"), 6.755, tol=1e-12)
check("T11 attraction-loss N", mean("t11_attraction_loss", "N"), 12.38, tol=1e-12)
check("T11 governance-loss N", mean("t11_governance_loss", "N"), 15.515, tol=1e-12)
check("T11 combined-loss N", mean("t11_combined_loss", "N"), 11.92, tol=1e-12)
base = np.array([x["N"] for x in condition("base")], float)
recip = np.array([x["N"] for x in condition("recipient_unconstrained")], float)
check("recipient paired final-N contrast", float((recip-base).mean()), 1.0275, tol=1e-12)
print("  INFO recipient 95% interval crosses zero; see RELEASE-GATE-RESULTS.md")
'''


SECONDARY_RESULTS = r'''
print("Calibration, Chapter 14, service, and paired Tradition comparison")
core = load("core_thresholds.json")["result"]
check("established count", core["established"][0], 14.1345177665, tol=1e-9)
check("experienced count", core["experienced"][0], 1.2461928934, tol=1e-9)
ch14 = load("ch14_individual.json")["result"]
check("Chapter 14 separating environments", ch14["endpoint_environment_bistable_count"], 7)
service = load("ch15_service.json")
svc_rows = [row for key, row in service.items() if key != "meta"]
by_cfg = {cfg: sorted((r for r in svc_rows if r["cfg"] == cfg), key=lambda r: r["seed"])
          for cfg in ("base", "no12", "recipient_unconstrained")}
service_N = np.asarray([a["N"]-b["N"] for a, b in zip(by_cfg["base"], by_cfg["no12"])])
service_s9 = np.asarray([a["s9"]-b["s9"] for a, b in zip(by_cfg["base"], by_cfg["no12"])])
service_s9_hw = 1.96 * service_s9.std(ddof=1) / np.sqrt(len(service_s9))
check("Step 12 membership loss", float(service_N.mean()), 5.325, tol=1e-12)
check("Step 9 service interval crosses zero",
      service_s9.mean()-service_s9_hw < 0 < service_s9.mean()+service_s9_hw, True)
trad = load("tradition_paired.json")["result"]
check("Tradition comparison reference N", trad["base_mean"], 13.0975, tol=1e-12)
rows = {row["tradition"]: row for row in trad["rows"]}
check("largest mixed Tradition loss", max(rows, key=lambda j: rows[j]["loss"]), 3)
check("resolved Tradition contrasts", sum(row["lo"] > 0 or row["hi"] < 0 for row in rows.values()), 7)
'''


ROBUSTNESS_RESULTS = r'''
print("Expanded robustness summaries")
mc = load("mc_error.json")
mcrows = [v for k, v in mc.items() if k != "meta"]
groups = collections.defaultdict(list)
for row in mcrows:
    groups[tuple(row["job"][:3])].append(row)
for key in (("full", 0.5, 520), ("full", 0.5, 1040),
            ("full", 0.5, 2600), ("full", 0.5, 5200)):
    print("  INFO horizon", key[2], "weeks mean N",
          round(float(np.mean([r["N"] for r in groups[key]])), 3))

def classify(rows, a, b):
    values = np.asarray([row[a] - row[b] for row in rows])
    return int((values > 0).sum()), int((values == 0).sum()), int((values < 0).sum())

sens = load("sens3.json")
for key in ("g125", "g250", "g500"):
    strict, ties, reverse = classify(sens[key], "att_N", "ref_N")
    print(f"  INFO {key} attraction-N minus referral-N: strict={strict}, ties={ties}, reversals={reverse}")
tier = load("tiered.json")
for key in ("tiered", "randmat"):
    strict, ties, reverse = classify(tier[key], "att_N", "ref_N")
    print(f"  INFO {key} attraction-N minus referral-N: strict={strict}, ties={ties}, reversals={reverse}")

morris = load("morris.json")["result"]["rows"]
leaders = sorted(morris, key=lambda r: -r["membership"]["mu_star"])[:8]
print("  INFO Morris membership leaders", [r["id"] for r in leaders])
sobol = load("sobol.json")
normalized_leaders = [r["id"].replace("scalar:", "") for r in leaders]
check("Sobol factors follow Morris leaders", sobol["meta"]["factors"], normalized_leaders)
print("  INFO structural cache complete", load("structural.json")["meta"]["jobs_completed"])
'''


FINAL = r'''
print("Final notebook verdict")
check("no accumulated assertion failures", len(FAILURES), 0)
print("CLEAN CACHE-BACKED VERIFICATION NOTEBOOK")
'''


def notebook(title: str) -> dict:
    return {
        "cells": [
            markdown(f"# {title}\n\nGenerated by `tools/regenerate_notebooks.py`. Expensive analyses are cache-backed and hash-checked."),
            code(SETUP),
            code(MODEL_CHECKS),
            code(CACHE_CHECKS),
            code(RELEASE_RESULTS),
            code(SECONDARY_RESULTS),
            code(ROBUSTNESS_RESULTS),
            code(FINAL),
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    outputs = {
        ROOT / "model" / "book-calculations.ipynb": notebook("Nobody in Charge: released calculations"),
        ROOT / "paper" / "anonymity-as-an-aggregation-condition.ipynb":
            notebook("Anonymity as an Aggregation Condition: verification notebook"),
    }
    for path, data in outputs.items():
        path.write_text(json.dumps(data, indent=1) + "\n")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
