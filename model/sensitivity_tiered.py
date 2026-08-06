"""Tiered and randomized-matrix robustness screens for the corrected model."""
import hashlib
import importlib.util
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "aa_group_model.py")
OUT = os.path.abspath(os.path.join(HERE, "..", "research", "tiered.json"))
H, SEEDS, DRAWS = 1560, 3, 1000

spec = importlib.util.spec_from_file_location("m", MODEL)
m = importlib.util.module_from_spec(spec)
sys.modules["m"] = m
spec.loader.exec_module(m)
BASE_S, BASE_G = m.S.copy(), m.GOV.copy()

# Tier by how much evidence constrains the value, not by whether its form was borrowed.
TIER1 = ["lam_exog", "lam0", "drop0", "churn", "cost", "contrib"]
TIER2 = [
    "delta0", "p_gate", "hill_n", "hill_k", "psi", "omega", "act_thr",
    "exp_thr", "drop_k",
]
TIER3 = ["k_ident", "k_proof", "k_conf", "k_couns", "k_recip", "het_sd"]
BOUNDS = {
    "hill_n": (1.01, None), "p_gate": (0.05, None),
    "act_thr": (0.01, 0.45), "exp_thr": (0.5, 0.95), "omega": (0.0, 1.0),
}


def _rederive():
    m.GOVW[:] = m.GOV / np.maximum(m.GOV.sum(0, keepdims=True), 1e-12)
    m.BETA[:] = m.S.sum(1) / m.S.sum(1).max()
    m.Snorm[:] = m.S / m.S.sum(1, keepdims=True)


def _run(P=None, attraction_T11=None):
    rows = [
        m.simulate(m.FULL, P=P, seed=s, T_end=H, attraction_T11=attraction_T11)
        for s in range(SEEDS)
    ]
    viable = [x for x in rows if x["endpoint_viable"]]
    return (
        sum(x["endpoint_viable"] for x in rows) / SEEDS,
        float(np.mean([x["est_mean"] for x in viable])) if viable else 0.0,
        float(np.mean([x["N"] for x in rows])),
        sum(x["endpoint_exists"] for x in rows) / SEEDS,
    )


def _jitter(key, value, rng):
    levels = {
        **{x: 0.25 for x in TIER1},
        **{x: 0.25 for x in TIER2},
        **{x: 0.50 for x in TIER3},
    }
    level = levels.get(key, 0.50)
    new_value = value * rng.uniform(1 - level, 1 + level)
    low, high = BOUNDS.get(key, (None, None))
    if low is not None:
        new_value = max(new_value, low)
    if high is not None:
        new_value = min(new_value, high)
    return new_value


def _tiered_one(draw):
    rng = np.random.default_rng(np.random.SeedSequence([11, 1, draw]))
    P = {
        key: (
            max(5, int(round(_jitter(key, value, rng))))
            if key == "cap"
            else _jitter(key, value, rng)
            if np.isscalar(value)
            else value
        )
        for key, value in m.DEFAULTS.items()
    }
    P["a"] = m.DEFAULTS["a"] * rng.uniform(0.5, 1.5, 12)
    m.S[:] = BASE_S * rng.uniform(0.5, 1.5, BASE_S.shape)
    m.GOV[:] = BASE_G * rng.uniform(0.5, 1.5, BASE_G.shape)
    _rederive()
    return _row(P)


def _randmat_one(draw):
    rng = np.random.default_rng(np.random.SeedSequence([7, 2, draw]))
    m.S[:] = np.where(BASE_S > 0, rng.uniform(0.05, 1.0, BASE_S.shape), 0.0)
    m.GOV[:] = np.where(BASE_G > 0, rng.uniform(0.05, 1.0, BASE_G.shape), 0.0)
    _rederive()
    return _row(None)


def _row(P):
    full = _run(P)
    attraction = _run(P, attraction_T11=0.0)
    no_referral_P = {} if P is None else dict(P)
    no_referral_P["lam_exog"] = 0.0
    referral = _run(no_referral_P)
    return dict(
        full_s=full[0], full_q=full[1], full_N=full[2], full_exists=full[3],
        att_s=attraction[0], att_N=attraction[2], att_exists=attraction[3],
        ref_s=referral[0], ref_q=referral[1], ref_N=referral[2],
        ref_exists=referral[3],
    )


def _save(data):
    tmp = OUT + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(data, fh)
    os.replace(tmp, OUT)


if __name__ == "__main__":
    workers = int(sys.argv[1]) if sys.argv[1:] else 4
    model_hash = hashlib.sha256(open(MODEL, "rb").read()).hexdigest()
    script_hash = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if (
        out.get("_meta", {}).get("model_sha256") != model_hash
        or out.get("_meta", {}).get("script_sha256") != script_hash
    ):
        out = {}
    out["_meta"] = dict(
        schema_version=3,
        status="incomplete",
        model_sha256=model_hash,
        script_sha256=script_hash,
        script="model/sensitivity_tiered.py",
        seeds=SEEDS,
        seed_range=[0, SEEDS - 1],
        draws=DRAWS,
        horizon=H,
        dt=0.5,
        draw_rng="independent SeedSequence keyed by design and draw index",
        role="tiered and structural-matrix screening; 1,000 perturbation draws in each design, three seeds per draw",
        attraction_intervention="pure T11 attraction path; governance held at one",
    )
    for key, worker in (("tiered", _tiered_one), ("randmat", _randmat_one)):
        rows = out.get(key, [])
        todo = range(len(rows), DRAWS)
        print(f"{key}: {len(rows)} of {DRAWS}; running {DRAWS-len(rows)}", flush=True)
        if len(rows) < DRAWS:
            with ProcessPoolExecutor(workers) as executor:
                for row in executor.map(worker, todo, chunksize=1):
                    rows.append(row)
                    out[key] = rows
                    if len(rows) % 5 == 0:
                        _save(out)
        out[key] = rows
        _save(out)

    out["_meta"]["tiered_draws_completed"] = len(out.get("tiered", []))
    out["_meta"]["random_matrix_draws_completed"] = len(out.get("randmat", []))
    out["_meta"]["status"] = (
        "complete"
        if len(out.get("tiered", [])) == DRAWS and len(out.get("randmat", [])) == DRAWS
        else "incomplete"
    )
    _save(out)
    print("ALL DONE" if out["_meta"]["status"] == "complete" else "PARTIAL", flush=True)
