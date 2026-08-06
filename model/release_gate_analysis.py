#!/usr/bin/env python3
"""Confirmatory mechanism-factorial analysis for the 6 August release gate.

The analysis uses 400 paired seeds, a 1,560-week horizon, and dt=0.5. It separates
the governance and non-governance paths of Traditions 3 and 11, and implements a
clean recipient-capacity override without changing S, BETA, or any other Step
weight. Zero membership, endpoint existence, endpoint viability (N > 5), first
passage, recovery, and final membership are stored as separate outcomes.

The cache contains per-seed records, summaries, pairing-aware contrasts, and
source hashes. It is resumable and written atomically.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import os
import platform
import sys
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODEL = HERE / "aa_group_model.py"
OUT = ROOT / "research" / "release_gate_results.json"
NSEED = 400
HORIZON = 1560
DT = 0.5

CONDITIONS = (
    "base",
    "t3_friction_loss",
    "t3_governance_loss",
    "t3_combined_loss",
    "t11_attraction_loss",
    "t11_governance_loss",
    "t11_combined_loss",
    "recipient_unconstrained",
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_model():
    spec = importlib.util.spec_from_file_location("release_model", MODEL)
    module = importlib.util.module_from_spec(spec)
    sys.modules["release_model"] = module
    spec.loader.exec_module(module)
    return module


def settings(mm, condition):
    T = mm.FULL.copy()
    kw = {}
    if condition == "t3_friction_loss":
        kw["dropout_T3"] = 0.0
    elif condition == "t3_governance_loss":
        resource = mm.FULL.copy()
        resource[2] = 0.0
        kw["resource_T"] = resource
    elif condition == "t3_combined_loss":
        resource = mm.FULL.copy()
        resource[2] = 0.0
        kw.update(resource_T=resource, dropout_T3=0.0)
    elif condition == "t11_attraction_loss":
        kw["attraction_T11"] = 0.0
    elif condition == "t11_governance_loss":
        resource = mm.FULL.copy()
        resource[10] = 0.0
        kw["resource_T"] = resource
    elif condition == "t11_combined_loss":
        resource = mm.FULL.copy()
        resource[10] = 0.0
        kw.update(resource_T=resource, attraction_T11=0.0)
    elif condition == "recipient_unconstrained":
        kw["recipient_override"] = 1.0
    elif condition != "base":
        raise ValueError(condition)
    return T, kw


def one(job):
    condition, seed = job
    mm = load_model()
    T, kw = settings(mm, condition)
    r = mm.simulate(T, seed=seed, T_end=HORIZON, dt=DT, **kw)
    return {
        "condition": condition,
        "seed": seed,
        "N": r["N"],
        "endpoint_exists": int(r["endpoint_exists"]),
        "endpoint_viable": int(r["endpoint_viable"]),
        "mean_practice": r["mean"],
        "established_practice": r["est_mean"],
        "low_practice_fraction": r["newcomer_frac"],
        "first_nonviable_week": r["first_nonviable_week"],
        "recovered_after_first_crossing": int(r["recovered_after_first_crossing"]),
        "first_recovery_week": r["first_recovery_week"],
        "closed": int(r["closed"]),
        "closure_week": r["closure_week"],
    }


def normal_summary(values):
    x = np.asarray(values, float)
    n = len(x)
    mean = float(x.mean())
    se = float(x.std(ddof=1) / math.sqrt(n)) if n > 1 else 0.0
    return {"n": n, "mean": mean, "se": se, "lo": mean - 1.96 * se, "hi": mean + 1.96 * se}


def wilson(values):
    x = np.asarray(values, int)
    n = len(x)
    count = int(x.sum())
    p = count / n
    z = 1.96
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return {"n": n, "count": count, "proportion": p, "lo": centre - half, "hi": centre + half,
            "method": "Wilson score, z=1.96"}


def paired_continuous(a, b):
    return normal_summary(np.asarray(a, float) - np.asarray(b, float)) | {
        "estimand": "mean paired difference, first minus second",
    }


def exact_binomial_two_sided(k, n):
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, i) for i in range(0, min(k, n - k) + 1)) / (2 ** n)
    return min(1.0, 2 * tail)


def paired_binary(a, b):
    a = np.asarray(a, int)
    b = np.asarray(b, int)
    d = a - b
    s = normal_summary(d)
    b_only = int(((a == 0) & (b == 1)).sum())
    a_only = int(((a == 1) & (b == 0)).sum())
    discordant = a_only + b_only
    return s | {
        "estimand": "paired risk difference, first minus second",
        "first_only": a_only,
        "second_only": b_only,
        "discordant": discordant,
        "mcnemar_exact_p": exact_binomial_two_sided(min(a_only, b_only), discordant),
    }


def rows_by_condition(cache):
    return {
        cond: [cache[f"{cond}|{seed}"] for seed in range(NSEED)]
        for cond in CONDITIONS
    }


def summarize(cache):
    groups = rows_by_condition(cache)
    continuous = ("N", "mean_practice", "established_practice", "low_practice_fraction")
    binary = ("endpoint_exists", "endpoint_viable", "recovered_after_first_crossing", "closed")
    summary = {}
    for cond, rows in groups.items():
        summary[cond] = {
            **{key: normal_summary([r[key] for r in rows]) for key in continuous},
            **{key: wilson([r[key] for r in rows]) for key in binary},
            "first_nonviable": {
                "count": sum(r["first_nonviable_week"] is not None for r in rows),
                "week_among_crossers": normal_summary(
                    [r["first_nonviable_week"] for r in rows if r["first_nonviable_week"] is not None]
                ) if any(r["first_nonviable_week"] is not None for r in rows) else None,
            },
            "closure_week_among_closed": normal_summary(
                [r["closure_week"] for r in rows if r["closure_week"] is not None]
            ) if any(r["closure_week"] is not None for r in rows) else None,
        }

    pairs = {
        "t3_friction_loss": ("base", "t3_friction_loss"),
        "t3_governance_loss": ("base", "t3_governance_loss"),
        "t3_combined_loss": ("base", "t3_combined_loss"),
        "t11_attraction_loss": ("base", "t11_attraction_loss"),
        "t11_governance_loss": ("base", "t11_governance_loss"),
        "t11_combined_loss": ("base", "t11_combined_loss"),
        "recipient_unconstrained_minus_base": ("recipient_unconstrained", "base"),
    }
    contrasts = {}
    for name, (first, second) in pairs.items():
        a, b = groups[first], groups[second]
        contrasts[name] = {
            **{key: paired_continuous([r[key] for r in a], [r[key] for r in b])
               for key in continuous},
            **{key: paired_binary([r[key] for r in a], [r[key] for r in b])
               for key in ("endpoint_exists", "endpoint_viable", "closed")},
            "first": first,
            "second": second,
        }

    factorials = {}
    for label, path_loss, gov_loss, combined in (
        ("t3", "t3_friction_loss", "t3_governance_loss", "t3_combined_loss"),
        ("t11", "t11_attraction_loss", "t11_governance_loss", "t11_combined_loss"),
    ):
        factorials[label] = {}
        for key in continuous + ("endpoint_exists", "endpoint_viable", "closed"):
            base = np.array([r[key] for r in groups["base"]], float)
            path = np.array([r[key] for r in groups[path_loss]], float)
            gov = np.array([r[key] for r in groups[gov_loss]], float)
            both = np.array([r[key] for r in groups[combined]], float)
            factorials[label][key] = {
                "path_loss_at_governance_intact": normal_summary(base - path),
                "governance_loss_at_other_path_intact": normal_summary(base - gov),
                "loss_interaction": normal_summary(base - path - gov + both),
            }
    return {"conditions": summary, "paired_contrasts": contrasts, "factorials": factorials}


def save(cache):
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, OUT)


def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    batch = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9
    script = Path(__file__).resolve()
    current_model_hash = sha256(MODEL)
    current_script_hash = sha256(script)
    cache = json.loads(OUT.read_text()) if OUT.exists() else {}
    old_meta = cache.get("meta", {})
    # A script-hash change may only enlarge the registered seed range. Stable
    # condition|seed keys let an otherwise compatible cache retain completed seeds.
    if (old_meta.get("model_sha256") not in (None, current_model_hash)
            or old_meta.get("conditions") not in (None, list(CONDITIONS))
            or old_meta.get("horizon_weeks") not in (None, HORIZON)
            or old_meta.get("dt_weeks") not in (None, DT)):
        cache = {}
    meta = {
        "schema_version": 2,
        "status": "incomplete",
        "analysis": "paired mechanism-factorial release gate",
        "created_or_updated_utc": datetime.now(timezone.utc).isoformat(),
        "model_sha256": current_model_hash,
        "script_sha256": current_script_hash,
        "script": str(script.relative_to(ROOT)),
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "conditions": list(CONDITIONS),
        "nseed": NSEED,
        "seed_range": [0, NSEED - 1],
        "horizon_weeks": HORIZON,
        "dt_weeks": DT,
        "viability_rule": "N > 5 at endpoint; N=0 is permanent closure; 0<N<=5 may recover",
        "pairing": "common seed and random stream across conditions",
        "jobs_expected": len(CONDITIONS) * NSEED,
    }
    cache["meta"] = meta
    jobs = [(condition, seed) for condition in CONDITIONS for seed in range(NSEED)]
    missing = [job for job in jobs if f"{job[0]}|{job[1]}" not in cache][:batch]
    print(f"{len(jobs)-len(missing)} or more of {len(jobs)} present; running {len(missing)}", flush=True)
    if missing:
        completed = 0
        with ProcessPoolExecutor(workers) as ex:
            for job, result in zip(missing, ex.map(one, missing)):
                cache[f"{job[0]}|{job[1]}"] = result
                completed += 1
                if completed % 40 == 0:
                    cache["meta"]["jobs_completed"] = sum(
                        f"{c}|{s}" in cache for c, s in jobs
                    )
                    save(cache)
        save(cache)
    complete = sum(f"{c}|{s}" in cache for c, s in jobs)
    cache["meta"]["jobs_completed"] = complete
    cache["meta"]["status"] = "complete" if complete == len(jobs) else "incomplete"
    if complete == len(jobs):
        cache["summary"] = summarize(cache)
    save(cache)
    print(f"{complete}/{len(jobs)}; {cache['meta']['status']}", flush=True)
    return 0 if complete == len(jobs) else 2


if __name__ == "__main__":
    raise SystemExit(main())
