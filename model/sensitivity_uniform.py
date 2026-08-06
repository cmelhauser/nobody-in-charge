"""Global simultaneous-perturbation screening for the corrected model.

There are 334 independent draws at each of three perturbation amplitudes
(1,002 draws total).  Each draw uses three common seeds for the full model,
the pure T11-attraction intervention, and the no-exogenous-referral condition.
The draw index seeds its own generator, so parallel execution is deterministic
and a partially completed cache can be resumed without changing later draws.
"""
import hashlib
import importlib.util
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "aa_group_model.py")
OUT = os.path.abspath(os.path.join(HERE, "..", "research", "sens3.json"))
H, SEEDS, DRAWS = 1560, 3, 334

spec = importlib.util.spec_from_file_location("m", MODEL)
m = importlib.util.module_from_spec(spec)
sys.modules["m"] = m
spec.loader.exec_module(m)
BASE_S, BASE_G = m.S.copy(), m.GOV.copy()


def _rederive():
    m.GOVW[:] = m.GOV / np.maximum(m.GOV.sum(0, keepdims=True), 1e-12)
    m.BETA[:] = m.S.sum(1) / m.S.sum(1).max()
    m.Snorm[:] = m.S / m.S.sum(1, keepdims=True)


def _run(P, attraction_T11=None):
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


def _one(job):
    level_code, draw = job
    level = level_code / 1000.0
    rng = np.random.default_rng(np.random.SeedSequence([11, level_code, draw]))
    lo, hi = 1 - level, 1 + level
    P = {
        k: (
            max(5, int(round(v * rng.uniform(lo, hi))))
            if k == "cap"
            else v * rng.uniform(lo, hi)
            if np.isscalar(v)
            else v
        )
        for k, v in m.DEFAULTS.items()
    }
    P["a"] = m.DEFAULTS["a"] * rng.uniform(lo, hi, 12)
    m.S[:] = BASE_S * rng.uniform(lo, hi, BASE_S.shape)
    m.GOV[:] = BASE_G * rng.uniform(lo, hi, BASE_G.shape)
    _rederive()
    full = _run(P)
    attraction = _run(P, attraction_T11=0.0)
    no_referral_P = dict(P)
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
        script="model/sensitivity_uniform.py",
        seeds=SEEDS,
        seed_range=[0, SEEDS - 1],
        draws=DRAWS,
        draws_total=3 * DRAWS,
        horizon=H,
        dt=0.5,
        draw_rng="independent SeedSequence([11, amplitude_thousandths, draw_index])",
        role="global screening; 1,002 independent perturbation draws across three amplitudes, three seeds per draw",
        attraction_intervention="pure T11 attraction path; governance held at one",
    )
    for level_code in (125, 250, 500):
        key = f"g{level_code}"
        rows = out.get(key, [])
        todo = [(level_code, d) for d in range(len(rows), DRAWS)]
        print(f"{key}: {len(rows)} of {DRAWS}; running {len(todo)}", flush=True)
        if todo:
            with ProcessPoolExecutor(workers) as executor:
                for row in executor.map(_one, todo, chunksize=1):
                    rows.append(row)
                    out[key] = rows
                    if len(rows) % 5 == 0:
                        _save(out)
        out[key] = rows
        _save(out)

    # A compact legacy OAT block is retained for backward compatibility.  The
    # authoritative four-distance OAT results live in research/oat_full.json.
    if "oat" not in out:
        oat = {}
        for key, value in m.DEFAULTS.items():
            if not np.isscalar(value) or key == "cap":
                continue
            result = {}
            for tag, multiplier in (("low", 0.75), ("high", 1.25)):
                P = {"lam_exog": 0.0, key: value * multiplier}
                if key == "lam_exog":
                    P["lam_exog"] = 0.0
                result[tag] = _run(P)[0]
            oat[key] = result
        out["oat"] = oat

    out["_meta"]["global_draws_completed"] = sum(
        len(out.get(key, [])) for key in ("g125", "g250", "g500")
    )
    out["_meta"]["status"] = (
        "complete"
        if out["_meta"]["global_draws_completed"] == 3 * DRAWS
        else "incomplete"
    )
    _save(out)
    print("ALL DONE" if out["_meta"]["status"] == "complete" else "PARTIAL", flush=True)
