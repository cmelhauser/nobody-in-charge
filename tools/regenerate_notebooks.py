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

print("repository root", ".")
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


PUBLIC_FIGURES = r'''
print("Published figures, derived from the caches")
print("Every decimal printed in a chapter must be reachable from this block, the model")
print("source, or a cache. tools/check_book.py enforces that. Values are printed at each")
print("precision the prose uses, including half-up rounding, because the book rounds half")
print("away from zero while Python rounds half to even.")

import os
ROOT_STR = str(ROOT)


def rows_of(name, drop=("meta", "result", "_meta")):
    d = load(name)
    return d, [v for k, v in d.items() if k not in drop]


def show(label, value, pct=False):
    """Print a derived value at the precisions the prose actually uses.

    Chapters quote the same quantity as a proportion, as a percentage, and rounded to two
    decimals. Printing one rendering leaves the others untraceable, so print all of them.
    """
    from decimal import Decimal, ROUND_HALF_UP

    def halfup(x, places):
        q = Decimal(1).scaleb(-places)
        return str(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))

    v = float(value)
    out = [f'{v:.6f}', f'{v:.4f}', f'{v:.3f}', f'{v:.2f}', f'{v:.1f}']
    # Prose rounds half away from zero; Python rounds half to even, so 57.705 formats as
    # 57.70 here and is printed 57.71 in the book. Both renderings are the same number.
    out += [halfup(v, 3), halfup(v, 2), halfup(v, 1)]
    if pct:
        p = v * 100.0
        out += [f'{p:.4f}%', f'{p:.2f}%', f'{p:.1f}%', halfup(p, 2), halfup(p, 1)]
    print(f'  {label}: ' + ' '.join(out))


def emit():
    """Print derived public figures. This is the body that will move into the notebook."""
    # ---- part5: trajectories, T3 dose sweep, founder composition ---------------------
    d = load('part5.json')
    traj = collections.defaultdict(list)
    for k, v in d.items():
        if k == 'meta' or not k.startswith('traj|'):
            continue
        traj[k.split('|')[1]].append(v)
    print('part5 trajectories, yearly means')

    def pad(seqs, n=31, fill=0.0):
        """A closed group's series stops at closure. The book counts closures as zero."""
        out = np.full((len(seqs), n), fill, float)
        for i, s in enumerate(seqs):
            s = [fill if x is None else x for x in s][:n]
            out[i, :len(s)] = s
        return out

    for cond in sorted(traj):
        rs = traj[cond]
        yrN = pad([r['yrN'] for r in rs])
        yrE = pad([r['yrE'] for r in rs])
        yrQ = pad([r['yrQ_established'] for r in rs])
        allrun = yrN.mean(0)
        alive = yrN > 0
        viable = yrN > 5
        print(f'  {cond} all-run N by year: ' + ' '.join(f'{x:.4f}' for x in allrun))
        with np.errstate(invalid='ignore'):
            vonly = np.where(viable.sum(0) > 0, (yrN * viable).sum(0) / np.maximum(viable.sum(0), 1), 0.0)
        print(f'  {cond} viable-only N by year: ' + ' '.join(f'{x:.4f}' for x in vonly))
        print(f'  {cond} viable fraction by year: ' + ' '.join(f'{x:.4f}' for x in viable.mean(0)))
        print(f'  {cond} exists fraction by year: ' + ' '.join(f'{x:.4f}' for x in alive.mean(0)))
        print(f'  {cond} established-practice by year: ' + ' '.join(f'{x:.4f}' for x in yrQ.mean(0)))
        print(f'  {cond} yrE by year: ' + ' '.join(f'{x:.4f}' for x in yrE.mean(0)))
        # per-year half-widths, which the chapters print beside the series
        hw = 1.96 * yrN.std(0, ddof=1) / np.sqrt(len(rs))
        print(f'  {cond} all-run N half-width by year: ' + ' '.join(f'{x:.4f}' for x in hw))
        # percentage decline between years, which ch20 and ch21 quote
        base = allrun[2] if allrun[2] else np.nan
        print(f'  {cond} per-cent fall from y2 to y30: {100.0 * (1 - allrun[30] / base):.4f}')
        for a, b in ((1, 30), (2, 10), (5, 30), (10, 30)):
            if allrun[a]:
                print(f'  {cond} per-cent fall y{a} to y{b}: {100.0 * (1 - allrun[b] / allrun[a]):.4f}')

    for grp, label in (('t3', 'T3 dose'), ('comp', 'founder composition')):
        g = collections.defaultdict(list)
        for k, v in d.items():
            if k == 'meta' or not k.startswith(grp + '|'):
                continue
            g[k.split('|')[1]].append(v)
        print(f'part5 {label}')
        for lev in sorted(g):
            rs = g[lev]
            N = np.array([r['N'] for r in rs], float)
            hw = 1.96 * N.std(ddof=1) / np.sqrt(len(N))
            print(f'  {lev}: N={N.mean():.4f} +/- {hw:.4f}, viable={np.mean([r["viable"] for r in rs]):.4f}, '
                  f'exists={np.mean([r["exists"] for r in rs]):.4f}, closed={np.mean([r["closed"] for r in rs]):.4f}, '
                  + ', '.join(f'{f}={np.mean([r[f] for r in rs]):.4f}'
                              for f in ('est_mean', 'n_est', 'low_practice_fraction')
                              if f in rs[0]))
        # paired composition contrasts against even founders
        if grp == 'comp':
            byseed = {}
            for k, v in d.items():
                if k.startswith('comp|'):
                    _, c, s = k.split('|')
                    byseed.setdefault(c, {})[int(s)] = v
            base = byseed['even']
            for c in ('concentrated', 'split'):
                s = sorted(set(base) & set(byseed[c]))
                dd = np.array([byseed[c][k]['N'] - base[k]['N'] for k in s], float)
                hw = 1.96 * dd.std(ddof=1) / np.sqrt(len(dd))
                print(f'  {c} minus even: {dd.mean():.4f} [{dd.mean()-hw:.4f}, {dd.mean()+hw:.4f}]')

    # ---- ch14 decay sweep -------------------------------------------------------------
    d, rs = rows_of('ch14_sweep.json')
    g = collections.defaultdict(list)
    for r in rs:
        g[r['pc']].append(r)
    print('ch14 decay sweep')
    for pc in sorted(g):
        rr = g[pc]
        N = np.array([r['N'] for r in rr], float)
        hw = 1.96 * N.std(ddof=1) / np.sqrt(len(N))
        print(f'  pc={pc}: N={N.mean():.4f} +/- {hw:.4f}, viable={np.mean([r["viable"] for r in rr]):.4f}, '
              f'exists={np.mean([r["exists"] for r in rr]):.4f}, closed={np.mean([r["closed"] for r in rr]):.4f}, '
              f'maint_all={np.mean([r["maint"] for r in rr]):.6f}, '
              f'maint_viable={np.mean([r["maint"] for r in rr if r["viable"]]) if any(r["viable"] for r in rr) else 0:.6f}')

    # ---- ch15 service -----------------------------------------------------------------
    d, rs = rows_of('ch15_service.json')
    by = collections.defaultdict(dict)
    for r in rs:
        by[r['cfg']][r['seed']] = r
    print('ch15 service')
    for cfg in sorted(by):
        rr = list(by[cfg].values())
        for fld in ('N', 'practice', 'est', 'maint', 's1', 's9', 's12', 'low_practice_fraction'):
            a = np.array([r[fld] for r in rr], float)
            hw = 1.96 * a.std(ddof=1) / np.sqrt(len(a))
            print(f'  {cfg} {fld}: {a.mean():.6f} +/- {hw:.6f}')
        print(f'  {cfg} viable={np.mean([r["viable"] for r in rr]):.4f} exists={np.mean([r["exists"] for r in rr]):.4f}')
    base = by['base']
    for cfg in ('no12', 'recipient_unconstrained'):
        s = sorted(set(base) & set(by[cfg]))
        for fld in ('N', 'practice', 'est', 'maint', 's1', 's9', 's12'):
            dd = np.array([base[k][fld] - by[cfg][k][fld] for k in s], float)
            hw = 1.96 * dd.std(ddof=1) / np.sqrt(len(dd))
            print(f'  base minus {cfg} {fld}: {dd.mean():.6f} [{dd.mean()-hw:.6f}, {dd.mean()+hw:.6f}]')

    # ---- ch13 proxy averaging ---------------------------------------------------------
    d, rs = rows_of('ch13_reps.json')
    g = collections.defaultdict(list)
    for r in rs:
        g[(r['rt'], r['npx'])].append(r)
    print('ch13 proxy averaging')

    def _wilson(k_, n_, z=1.96):
        p = k_ / n_
        den = 1 + z * z / n_
        c = (p + z * z / (2 * n_)) / den
        h = z * np.sqrt(p * (1 - p) / n_ + z * z / (4 * n_ * n_)) / den
        return max(0.0, c - h), min(1.0, c + h)

    for k in sorted(g):
        a = np.array([r['est'] for r in g[k]], float)
        n_ = len(a)
        k_ = int((a <= 0).sum())
        lo, hi = _wilson(k_, n_)
        print(f'  rho={k[0]} proxies={k[1]}: mean_est={a.mean():.6f} sd={a.std(ddof=1):.6f} '
              f'nonpositive={k_}/{n_} median={np.median(a):.6f} '
              f'ratio_to_truth={a.mean()/k[0] if k[0] else float("nan"):.6f}')
        show(f'ch13 rho={k[0]} proxies={k[1]} nonpositive fraction', k_ / n_, pct=True)
        show(f'ch13 rho={k[0]} proxies={k[1]} Wilson lo', lo, pct=True)
        show(f'ch13 rho={k[0]} proxies={k[1]} Wilson hi', hi, pct=True)

    # ---- oat: influence ranges the chapters quote --------------------------------------
    d = load('oat_full.json')
    b = d['baseline']['full']
    jobs = [k for k in d if k not in ('meta', 'baseline')]
    print('oat influence ranges over baseline')
    for fld in ('N', 'practice', 'maint'):
        rows = []
        for p in jobs:
            v25 = [d[p][t]['full'][fld] for t in ('minus_25', 'plus_25')]
            vall = [d[p][t]['full'][fld] for t in d[p]]
            rows.append((p, (max(v25) - min(v25)) / b[fld], (max(vall) - min(vall)) / b[fld]))
        rows.sort(key=lambda r: -r[2])
        for p, r25, rall in rows[:6]:
            print(f'  {fld} {p}: pm25={r25:.4f}x baseline, full ladder={rall:.4f}x baseline')
    print(f'  oat baseline full: N={b["N"]:.4f} practice={b["practice"]:.6f} maint={b["maint"]:.6f}')

    # ---- scenarios and release gate ----------------------------------------------------
    d, rs = rows_of('scenarios_hiseed.json')
    g = collections.defaultdict(list)
    for r in rs:
        g[r['scen']].append(r)
    print('scenarios_hiseed')
    for s in sorted(g):
        rr = g[s]
        N = np.array([r['N'] for r in rr], float)
        hw = 1.96 * N.std(ddof=1) / np.sqrt(len(N))
        print(f'  {s}: N={N.mean():.4f} +/- {hw:.4f} viable={np.mean([r["viable"] for r in rr]):.4f} '
              f'exists={np.mean([r["exists"] for r in rr]):.4f} closed={np.mean([r["closed"] for r in rr]):.4f} '
              f'est={np.mean([r["est_mean"] for r in rr]):.6f}')

    # ---- every scalar summary, at every precision the prose uses ----------------------
    print('per-condition summaries at prose precision')
    d = load('part5.json')
    grp = collections.defaultdict(list)
    for k, v in d.items():
        if k == 'meta':
            continue
        a, b, _ = k.split('|')
        grp[(a, b)].append(v)
    for (a, b), rs in sorted(grp.items()):
        for fld in ('N', 'viable', 'exists', 'closed', 'est_mean'):
            if fld in rs[0]:
                show(f'part5 {a} {b} {fld}', np.mean([r[fld] for r in rs]), pct=fld in ('viable', 'exists', 'closed'))
        if a == 'traj':
            yrN = np.full((len(rs), 31), 0.0)
            for i, r in enumerate(rs):
                s = [0.0 if x is None else x for x in r['yrN']][:31]
                yrN[i, :len(s)] = s
            for y in (1, 2, 5, 10, 20, 30):
                show(f'part5 traj {b} y{y} all-run N', yrN[:, y].mean())
                show(f'part5 traj {b} y{y} viable fraction', (yrN[:, y] > 5).mean(), pct=True)
                show(f'part5 traj {b} y{y} exists fraction', (yrN[:, y] > 0).mean(), pct=True)
                v = yrN[:, y][yrN[:, y] > 5]
                show(f'part5 traj {b} y{y} viable-only N', v.mean() if len(v) else 0.0)

    d, rs = rows_of('ch14_sweep.json')
    g = collections.defaultdict(list)
    for r in rs:
        g[r['pc']].append(r)
    for pc in sorted(g):
        rr = g[pc]
        for fld in ('N', 'viable', 'exists', 'closed', 'maint'):
            show(f'ch14 pc={pc} {fld}', np.mean([r[fld] for r in rr]), pct=fld in ('viable', 'exists', 'closed'))

    # ---- ch14 environment-matched individual test -------------------------------------
    # The cache stores these in scientific notation, which no decimal search can match,
    # so print the same values in plain decimal at the precision the chapter uses.
    res = load('ch14_individual.json').get('result', {})
    print('ch14 individual environments, plain decimal')
    for k in ('mean_environment_high_maintenance', 'mean_environment_low_maintenance',
              'mean_group_capacity', 'endpoint_environment_bistable_fraction'):
        if k in res:
            print(f'  {k}: {res[k]:.16f} {res[k]:.10f} {res[k]:.8f}')
    for k in ('high_maintenance_quantiles', 'low_maintenance_quantiles'):
        for q, v in zip((10, 50, 90), res.get(k, [])):
            print(f'  {k} q{q}: {v:.16f} {v:.13f} {v:.10f} {v:.7f}')
    if 'endpoint_environment_bistable_count' in res:
        show('ch14 bistable fraction of 400',
             res['endpoint_environment_bistable_count'] / 400.0, pct=True)

    try:
        d, rs = rows_of('ch14_individual.json')
        keys = [k for k in rs[0]] if rs and isinstance(rs[0], dict) else []
        print('ch14 individual environments, fields: ' + ','.join(map(str, keys)))
        for fld in keys:
            vals = [r[fld] for r in rs if isinstance(r.get(fld), (int, float))]
            if not vals:
                continue
            a = np.array(vals, float)
            print(f'  {fld}: mean={a.mean():.12f} median={np.median(a):.12f} min={a.min():.12f} max={a.max():.12f}')
            show(f'ch14 individual {fld} mean', a.mean())
        sep = [r for r in rs if isinstance(r, dict) and any(
            isinstance(v, (int, float)) and abs(v) > 0.05 for k, v in r.items() if 'diff' in str(k) or 'sep' in str(k))]
        show('ch14 individual separation fraction', len(sep) / max(len(rs), 1), pct=True)
    except Exception as exc:
        print('  ch14_individual: ' + str(exc))

    # ---- Chapter 7: the five-member DeGroot worked example ----------------------------
    A5 = np.array([[.30, .20, .30, .10, .10],
                   [.15, .25, .35, .15, .10],
                   [.20, .15, .35, .15, .15],
                   [.15, .15, .35, .20, .15],
                   [.20, .15, .30, .15, .20]])
    A5 = A5 / A5.sum(1, keepdims=True)
    b0 = np.array([9., 2., 6., 4., 7.])
    b = b0.copy()
    print('ch07 DeGroot worked example, round by round')
    for r in range(5):
        print(f'  round {r}: ' + ' '.join(f'{v:.4f}' for v in b))
        print(f'  round {r} (2dp): ' + ' '.join(f'{v:.2f}' for v in b))
        b = A5 @ b
    w, V = np.linalg.eig(A5.T)
    s5v = np.real(V[:, np.argmin(np.abs(w - 1))])
    s5v = s5v / s5v.sum()
    show('ch07 consensus', float(b[0]))
    show('ch07 plain average of starting beliefs', float(b0.mean()))
    show('ch07 influence-weighted average', float(s5v @ b0))
    for i, nm in enumerate(('Ann', 'Ben', 'Cara', 'Dan', 'Eve')):
        show(f'ch07 influence {nm}', float(s5v[i]))
        show(f'ch07 weight on others {nm}', float(1 - A5[i, i]))

    # ---- Chapter 13: CES output and dynamic complementarity ---------------------------
    GAM = np.array([.30, .30, .25, .15])

    def ces(x, g, rho):
        x = np.asarray(x, float)
        g = np.asarray(g, float)
        if abs(rho) < 1e-8:
            return float(np.prod(x ** g))
        if rho < -60:
            return float(x.min())
        with np.errstate(divide='ignore', invalid='ignore'):
            return float((g @ (x ** rho)) ** (1 / rho))

    def cross(rho, h=1e-4, bb=(.7, .4, .5, .6)):
        f = lambda a, c: ces([bb[0], a, c, bb[3]], GAM, rho)
        return (f(bb[1] + h, bb[2] + h) - f(bb[1] + h, bb[2] - h)
                - f(bb[1] - h, bb[2] + h) + f(bb[1] - h, bb[2] - h)) / (4 * h * h)

    print('ch13 CES, output with the prior step at zero')
    for r in (-100, -4, -1, 0.0, 0.3, 0.6, 0.9):
        show(f'ch13 output rho={r}', ces([0.7, 0.0, 0.8, 0.6], GAM, r))
        if r > -60:
            show(f'ch13 elasticity rho={r}', 1 / (1 - r))
    print('ch13 cross-partial in prior stock and group input at (0.7, 0.4, 0.5, 0.6)')
    for r in (-4, -1, 0.0, 0.5):
        show(f'ch13 cross-partial rho={r}', cross(r))

    # ---- Part Four: semantic overlap algebra and its perturbation tests ---------------
    B = m.S @ m.GOV.T
    print('Part Four semantic overlap B = S @ GOV.T (exact, no sampling error)')
    for i in range(12):
        row = B[i]
        o = np.argsort(-row)
        rank = int(np.where(o == i)[0][0]) + 1
        print(f'  step {i+1}: principal T{o[0]+1}={row[o[0]]:.4f} runner-up T{o[1]+1}={row[o[1]]:.4f} '
              f'own T{i+1}={row[i]:.4f} rank={rank} margin={row[o[0]]-row[o[1]]:.4f}')
        show(f'B step {i+1} principal', row[o[0]])
        show(f'B step {i+1} runner-up', row[o[1]])
        show(f'B step {i+1} own', row[i])
    loadv = B.sum(0)
    for j in range(12):
        show(f'B load T{j+1}', loadv[j])
    colS = m.S.sum(0)
    print('load by resource for each tradition: GOV[j,r] * column sum of S')
    for j in range(12):
        for r in range(m.GOV.shape[1]):
            show(f'T{j+1} load from resource {r}', m.GOV[j, r] * colS[r])
    for r in range(m.S.shape[1]):
        show(f'S column sum resource {r}', colS[r])

    # Reassignment test: T5 takes T1's governance of one resource, T1 keeps nothing.
    print('ch17 reassignment test, load after moving one resource from T1 to T5')
    for r in range(m.GOV.shape[1]):
        G2 = m.GOV.copy()
        G2[4, r] = max(G2[4, r], G2[0, r])
        G2[0, r] = 0.0
        L2 = (m.S @ G2.T).sum(0)
        print(f'  resource {r}: T1={L2[0]:.4f} T5={L2[4]:.4f} leader T{int(np.argmax(L2))+1}')
        show(f'ch17 reassign resource {r} T1', float(L2[0]))
        show(f'ch17 reassign resource {r} T5', float(L2[4]))
    pair = float(m.GOV[0, 6] * colS[6] + m.GOV[0, 7] * colS[7])
    show('ch17 T1 continuity plus pressure', pair)
    show('ch17 T1 stripped of both', float(loadv[0]) - pair)
    show('ch17 continuity+pressure share of T1', pair / float(loadv[0]), pct=True)

    # ---- Chapter 22: the founder-composition design constant ---------------------------
    n0, per = 25, 0.55
    show('ch22 founders', n0)
    show('ch22 initial practice per founder', per)
    show('ch22 total initial practice', n0 * per)
    show('ch22 concentrated tail level', (per * n0 - 5.0) / 20)

    def wilson_pct(k, n, z=1.96):
        p = k / n
        den = 1 + z * z / n
        c = (p + z * z / (2 * n)) / den
        h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
        return 100 * max(0.0, c - h), 100 * min(1.0, c + h)

    def coupling_test(fn, seed, N=2000):
        rg = np.random.default_rng(seed)
        t1 = dw = s5 = s12 = 0
        for _ in range(N):
            Sp, Gp = fn(rg)
            Bp = Sp @ Gp.T
            if int(np.argmax(Bp.sum(0))) == 0:
                t1 += 1
            if all(int(np.argmax(Bp[i])) != i for i in range(12)):
                dw += 1
            if int(np.argmax(Bp[4])) == 11:
                s5 += 1
            if int(np.argmax(Bp[11])) == 4:
                s12 += 1
        return (t1, dw, s5, s12), N

    print('coupling perturbation tests, 2,000 draws each')
    for lvl in (0.15, 0.30, 0.50, 0.75):
        f = lambda rg, l=lvl: (m.S * rg.uniform(1 - l, 1 + l, m.S.shape),
                               m.GOV * rg.uniform(1 - l, 1 + l, m.GOV.shape))
        counts, N = coupling_test(f, 3)
        for lab, c in zip(('T1_top', 'all12', 'S5_to_T12', 'S12_to_T5'), counts):
            lo, hi = wilson_pct(c, N)
            print(f'  jitter +/-{int(lvl*100)}% {lab}: {100*c/N:.4f}% [{lo:.4f}, {hi:.4f}]  '
                  f'{100*c/N:.1f} [{lo:.1f}, {hi:.1f}]  {lo:.2f} {hi:.2f}')
    fstruct = lambda rg: (np.where(m.S > 0, rg.uniform(.05, 1., m.S.shape), 0.),
                          np.where(m.GOV > 0, rg.uniform(.05, 1., m.GOV.shape), 0.))
    counts, N = coupling_test(fstruct, 23)
    for lab, c in zip(('T1_top', 'all12', 'S5_to_T12', 'S12_to_T5'), counts):
        lo, hi = wilson_pct(c, N)
        print(f'  structural {lab}: {100*c/N:.4f}% [{lo:.4f}, {hi:.4f}]  '
              f'{100*c/N:.1f} [{lo:.1f}, {hi:.1f}]  {lo:.2f} {hi:.2f}')

    d = load('release_gate_results.json')
    rs = [v for k, v in d.items() if k != 'meta' and isinstance(v, dict) and 'condition' in v]
    g = collections.defaultdict(list)
    for r in rs:
        g[r['condition']].append(r)
    print('release gate conditions')
    for c in sorted(g):
        rr = g[c]
        N = np.array([r['N'] for r in rr], float)
        hw = 1.96 * N.std(ddof=1) / np.sqrt(len(N))
        k_v = sum(r['endpoint_viable'] for r in rr)
        n = len(rr)
        # Wilson interval
        p = k_v / n
        z = 1.96
        den = 1 + z * z / n
        cen = (p + z * z / (2 * n)) / den
        rad = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
        print(f'  {c}: N={N.mean():.4f} +/- {hw:.4f} viable={p:.4f} Wilson=[{cen-rad:.4f}, {cen+rad:.4f}]')
        show(f'gate {c} N', N.mean())
        show(f'gate {c} N lo', N.mean() - hw)
        show(f'gate {c} N hi', N.mean() + hw)
        for fld in ('endpoint_exists', 'endpoint_viable', 'closed'):
            k = sum(r[fld] for r in rr)
            pp = k / n
            cen2 = (pp + z * z / (2 * n)) / den
            rad2 = z * np.sqrt(pp * (1 - pp) / n + z * z / (4 * n * n)) / den
            show(f'gate {c} {fld}', pp, pct=True)
            show(f'gate {c} {fld} Wilson lo', max(0.0, cen2 - rad2), pct=True)
            show(f'gate {c} {fld} Wilson hi', min(1.0, cen2 + rad2), pct=True)
        for fld in ('mean_practice', 'established_practice', 'low_practice_fraction'):
            a = np.array([r[fld] for r in rr], float)
            h2 = 1.96 * a.std(ddof=1) / np.sqrt(len(a))
            show(f'gate {c} {fld}', a.mean())
            show(f'gate {c} {fld} lo', a.mean() - h2)
            show(f'gate {c} {fld} hi', a.mean() + h2)
    # paired contrasts against baseline, which the chapters quote as costs
    byc = {c: {r['seed']: r for r in rr} for c, rr in g.items()}
    base = byc.get('base', {})
    for c, o in byc.items():
        if c == 'base' or not base:
            continue
        s = sorted(set(base) & set(o))
        for fld in ('N', 'mean_practice', 'established_practice'):
            dd = np.array([base[k][fld] - o[k][fld] for k in s], float)
            h2 = 1.96 * dd.std(ddof=1) / np.sqrt(len(dd))
            show(f'gate base minus {c} {fld}', dd.mean())
            show(f'gate base minus {c} {fld} lo', dd.mean() - h2)
            show(f'gate base minus {c} {fld} hi', dd.mean() + h2)

emit()
print("published figures block complete")
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
            code(PUBLIC_FIGURES),
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
