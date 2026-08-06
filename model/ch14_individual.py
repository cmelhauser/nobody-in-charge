"""Recheck Chapter 14's individual bistability in corrected group environments.

The old notebook fixed resource supply and group support at constants taken from the
pre-correction model.  Mean-centring capability changes the endpoint population and
therefore those state-dependent quantities.  This script first obtains 400 corrected
full-adherence endpoint environments.  It then places a capability-one test member at a
high and a low initial state in each frozen environment and integrates both to an
attractor.  This tests whether the chapter's bistability premise is present in the
released model's own environments rather than in an obsolete hand-copied environment.
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
OUT = os.path.abspath(os.path.join(HERE, "..", "research", "ch14_individual.json"))
NSEED, H, DT = 400, 1560, 0.5


def _load():
    spec = importlib.util.spec_from_file_location("m", MODEL)
    mm = importlib.util.module_from_spec(spec)
    sys.modules["m"] = mm
    spec.loader.exec_module(mm)
    return mm


def _environment(seed):
    mm = _load()
    run = mm.simulate(mm.FULL, seed=seed, T_end=H, dt=DT)
    levels = run["X"][run["alive"]].mean(axis=1)
    established = int((levels > mm.DEFAULTS["act_thr"]).sum())
    solvent = min(1.0, established * mm.DEFAULTS["contrib"] / mm.DEFAULTS["cost"])
    resources, _, components = mm.resources(
        run["X"], run["alive"], mm.FULL, mm.DEFAULTS, solvent,
        return_components=True,
    )
    maintenance = run["X"][run["alive"]][:, 9:12].mean(axis=1)
    own = maintenance ** mm.DEFAULTS["hill_n"] / (
        mm.DEFAULTS["hill_k"] ** mm.DEFAULTS["hill_n"]
        + maintenance ** mm.DEFAULTS["hill_n"]
    )
    return dict(
        seed=seed,
        N=run["N"],
        endpoint_viable=int(run["endpoint_viable"]),
        resources=[float(x) for x in resources],
        group_capacity=float(own.mean()) if len(own) else 0.0,
        experienced=int(components["high_practice"]),
    )


def _settle(mm, initial, resources, group_capacity, capability=None, decay=None,
            horizon=800.0, dt=0.5):
    initial = np.asarray(initial, float)
    if initial.ndim == 1:
        initial = initial[None, :]
    resources = np.asarray(resources, float)
    if resources.ndim == 1:
        resources = resources[None, :]
    n = len(initial)
    capability = np.ones(n) if capability is None else np.broadcast_to(capability, (n,))
    decay = np.full(n, mm.DEFAULTS["delta0"]) if decay is None else np.broadcast_to(decay, (n,))
    group_capacity = np.broadcast_to(np.asarray(group_capacity, float), (n,))
    peer = (1 - mm.BETA)[None, :] + mm.BETA[None, :] * (resources @ mm.Snorm.T)
    weights = np.linspace(0.05, 1.0, mm.NSTEP)
    X = initial.copy()
    for _ in range(int(horizon / dt)):
        gate = np.ones_like(X)
        gate[:, 1:] = np.clip(X[:, :-1], 0, 1) ** mm.DEFAULTS["p_gate"]
        maintenance = X[:, 9:12].mean(axis=1)
        own = maintenance ** mm.DEFAULTS["hill_n"] / (
            mm.DEFAULTS["hill_k"] ** mm.DEFAULTS["hill_n"]
            + maintenance ** mm.DEFAULTS["hill_n"]
        )
        capacity = own + (1 - own) * mm.DEFAULTS["omega"] * group_capacity
        capacity_by_step = 1 - weights[None, :] * (1 - capacity[:, None])
        growth = mm.DEFAULTS["a"] * gate * peer * capacity_by_step * capability[:, None]
        d = np.repeat(decay[:, None], mm.NSTEP, axis=1)
        d[:, :11] *= 1 + mm.DEFAULTS["psi"] * (1 - X[:, 1:12])
        X = np.clip(X + dt * (growth * (1 - X) - d * X), 0, 1)
    return X


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
        out.get("meta", {}).get("model_sha256") != model_hash
        or out.get("meta", {}).get("script_sha256") != script_hash
    ):
        out = {}
    out["meta"] = dict(
        schema_version=1,
        status="incomplete",
        model_sha256=model_hash,
        script_sha256=script_hash,
        script="model/ch14_individual.py",
        nseed=NSEED,
        seed_range=[0, NSEED - 1],
        horizon=H,
        dt=DT,
        jobs_expected=NSEED,
        frozen_environment_test="capability-one member, high versus low initial state",
    )
    todo = [seed for seed in range(NSEED) if str(seed) not in out]
    print(f"{NSEED-len(todo)} of {NSEED}; running {len(todo)}", flush=True)
    if todo:
        with ProcessPoolExecutor(workers) as executor:
            for seed, row in zip(todo, executor.map(_environment, todo)):
                out[str(seed)] = row
                if (seed + 1) % 20 == 0:
                    _save(out)

    done = sum(str(seed) in out for seed in range(NSEED))
    out["meta"]["jobs_completed"] = done
    if done == NSEED:
        mm = _load()
        rows = [out[str(seed)] for seed in range(NSEED)]
        resources = np.asarray([row["resources"] for row in rows])
        group_capacity = np.asarray([row["group_capacity"] for row in rows])
        high = _settle(mm, np.full((NSEED, mm.NSTEP), 0.95), resources, group_capacity)
        low = _settle(mm, np.full((NSEED, mm.NSTEP), 0.02), resources, group_capacity)
        high_maintenance = high[:, 9:12].mean(axis=1)
        low_maintenance = low[:, 9:12].mean(axis=1)
        bistable = (high_maintenance - low_maintenance) > 0.05

        mean_resources = resources.mean(axis=0)
        mean_group_capacity = float(group_capacity.mean())
        high_mean_env = _settle(
            mm, np.full(mm.NSTEP, 0.95), mean_resources, mean_group_capacity
        )[0]
        low_mean_env = _settle(
            mm, np.full(mm.NSTEP, 0.02), mean_resources, mean_group_capacity
        )[0]
        out["result"] = dict(
            mean_resources=[float(x) for x in mean_resources],
            mean_group_capacity=mean_group_capacity,
            endpoint_environment_bistable_count=int(bistable.sum()),
            endpoint_environment_bistable_fraction=float(bistable.mean()),
            endpoint_environment_bistable_seeds=[
                int(seed) for seed, flag in enumerate(bistable) if flag
            ],
            high_maintenance_quantiles=[
                float(x) for x in np.quantile(high_maintenance, [0.1, 0.5, 0.9])
            ],
            low_maintenance_quantiles=[
                float(x) for x in np.quantile(low_maintenance, [0.1, 0.5, 0.9])
            ],
            mean_environment_high_state=[float(x) for x in high_mean_env],
            mean_environment_low_state=[float(x) for x in low_mean_env],
            mean_environment_high_maintenance=float(high_mean_env[9:12].mean()),
            mean_environment_low_maintenance=float(low_mean_env[9:12].mean()),
            conclusion=(
                "typical-member bistability is common in corrected endpoint environments"
                if bistable.mean() >= 0.5
                else "typical-member bistability is rare in corrected endpoint environments"
                if bistable.any()
                else "no capability-one bistability in corrected endpoint environments"
            ),
        )
        out["meta"]["status"] = "complete"
    _save(out)
    print("ALL DONE" if out["meta"]["status"] == "complete" else "PARTIAL", flush=True)
