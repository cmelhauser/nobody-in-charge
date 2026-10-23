#!/usr/bin/env python3
"""Rebuild both public notebooks as compact, cache-backed verification artifacts.

The notebooks deliberately do not rerun the expensive Monte Carlo suite. They verify model
invariants, cache identity/completeness, and the public results derived from those caches.
Run the generating analyses first, then this script, then `tools/run_notebook.py` for each
notebook.

Run from anywhere:  python3 tools/regenerate_notebooks.py

Writes model/book-calculations.ipynb and paper/anonymity-as-an-aggregation-condition.ipynb
(paths derived from this file's location), each as indent-1 JSON with a trailing newline, and
prints the two repository-relative paths. It reads no cache and runs no cell: the notebooks
come out with empty outputs and no execution counts, and `tools/run_notebook.py` is what
fills the outputs in. The cell source lives in this file as the string constants below, which
is why they carry lines over the length limit: wrapping one would change the notebook.
Exit status is 0 unless a file cannot be written.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def code(source: str) -> dict:
    """Return a notebook code cell for `source`, with no outputs and no execution count.

    Leading and trailing blank lines are stripped and each line gets its own newline, which is
    the line-list form nbformat stores.
    """
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source.strip().splitlines()],
    }


def markdown(source: str) -> dict:
    """Return a notebook markdown cell for `source`, split into newline-terminated lines."""
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
    "part2_influence.json": None,
    "mc_error.json": 2600,
    "tradition_paired.json": 5200,
    "structural.json": 10000,
    "morris.json": 2380,
    "oat_full.json": None,
    "sobol.json": 11264,
    "decay_ordering.json": 4800,
    "decay_reversal.json": 3600,
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

_dec = [v for n in ("decay_ordering.json", "decay_reversal.json")
        for k, v in load(n).items() if k != "meta"]
def _dcell(pc, scen):
    return [r for r in _dec if r["pc"] == pc and r["scen"] == scen]
check("decay ordering: every cell holds seeds 0-399",
      all(sorted(r["seed"] for r in _dcell(pc, sc)) == list(range(400))
          for pc in (0, -10, -15, -20, -25, -50, -75)
          for sc in ("full", "attraction", "referral")), True)
check("decay ordering at the default rate reproduces released full-adherence mean N",
      round(float(np.mean([r["N"] for r in _dcell(0, "full")])), 2), 17.8)
check("decay ordering at the default rate reproduces released attraction-loss mean N",
      round(float(np.mean([r["N"] for r in _dcell(0, "attraction")])), 2), 12.38)
check("decay ordering at the default rate reproduces released referral-loss viability",
      sum(r["viable"] for r in _dcell(0, "referral")), 11)
def _paired_mean(pc, fld):
    a = {r["seed"]: r for r in _dcell(pc, "attraction")}
    b = {r["seed"]: r for r in _dcell(pc, "referral")}
    return float(np.mean([a[s][fld] - b[s][fld] for s in sorted(a)]))
check("decay reversal: membership ordering still holds 15 per cent lower",
      round(_paired_mean(-15, "N"), 2), 6.35)
check("decay reversal: membership ordering is reversed 20 per cent lower",
      round(_paired_mean(-20, "N"), 2), -2.79)
check("decay reversal: viability ordering holds at every new level",
      [round(_paired_mean(pc, "viable"), 4) for pc in (-10, -15, -20)],
      [0.8575, 0.67, 0.455])
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
    """Print derived public figures at the precisions the chapters use."""
    # ---- part4: matrix tests that Chapters Sixteen to Eighteen quote ------------------------
    # The threshold test, the principal-supplier counts and the index-mate ranks were computed
    # for those chapters in an earlier notebook whose sections 11 to 11d no longer exist; they
    # are rebuilt here from the model's own S and GOV so the figures stand on a visible computation.
    print('part4 threshold test and principal suppliers (Chapters Sixteen to Eighteen)')
    Sm = np.array(m.S, float)
    Gm = np.array(m.GOV, float)
    Bm = np.round(Sm @ Gm.T, 12)           # rounded so exact ties stay ties
    rowsum = Sm.sum(1)
    cstar = np.round(Bm.max(1) / rowsum, 12)  # strength an index-mate would need to govern everything its Step consumes
    live = Gm[Gm > 0]
    show('live GOV entries (count)', float(live.size))
    show('mean live GOV entry', float(live.mean()))
    show('median live GOV entry', float(np.median(live)))
    protective = [3, 5, 6, 8, 9]           # Steps 4, 6, 7, 9, 10: the index-mate governs nothing
    enabling = [i for i in range(12) if i not in protective]
    for i in range(12):
        show(f'threshold c* for Step {i + 1}', float(cstar[i]))
    for label, idx in (('protective', protective), ('enabling', enabling), ('all twelve', list(range(12)))):
        show(f'mean c* {label}', float(cstar[idx].mean()))
        show(f'min c* {label}', float(cstar[idx].min()))
        show(f'max c* {label}', float(cstar[idx].max()))
    check('live GOV entries', int(live.size), 35)
    check('every protective c* exceeds the mean live entry',
          bool((cstar[protective] > live.mean()).all()), True)
    check('every protective c* exceeds the median live entry',
          bool((cstar[protective] > np.median(live)).all()), True)
    check('protective c* range starts below the enabling range',
          bool(cstar[protective].min() < cstar[enabling].min()), True)
    check('protective c* range ends below the enabling range',
          bool(cstar[protective].max() < cstar[enabling].max()), True)
    ranks = [1 + int((Bm[i] > Bm[i, i]).sum()) for i in range(12)]
    print('  index-mate competition rank by Step (ties share): ' + ' '.join(map(str, ranks)))
    check('index-mate competition ranks', ranks, [2, 7, 7, 8, 5, 7, 7, 4, 8, 8, 4, 6])
    sole, tied_steps, runner = collections.Counter(), [], collections.Counter()
    for i in range(12):
        lead = [j + 1 for j in range(12) if Bm[i, j] == Bm[i].max()]
        if len(lead) == 1:
            sole[lead[0]] += 1
            second = sorted(set(Bm[i]), reverse=True)[1]
            for j in range(12):
                if Bm[i, j] == second:
                    runner[j + 1] += 1
        else:
            tied_steps.append((i + 1, lead))
    print('  sole principal supplier counts by Tradition: ' + str(dict(sorted(sole.items()))))
    print('  steps with an exact tie at the top: ' + str(tied_steps))
    print('  sole-lead runner-up counts by Tradition: ' + str(dict(sorted(runner.items()))))
    check('unity sole principal suppliers', sole[1], 4)
    check('group conscience sole principal suppliers', sole[2], 3)
    check('exact top ties', tied_steps, [(4, [1, 2])])

    # ---- part2: the closed forms Chapters Nine and Ten quote ---------------------------------
    print('part2 closed forms (Chapters Nine and Ten)')
    alpha = 0.35

    def rotation_row(n, pool):
        """Influence vector of a rotating pool: every row of the cycle-averaged matrix is this one."""
        member = alpha / pool + (pool - 1) / pool * (1 - alpha) / (n - 1)
        return member, (1 - alpha) / (n - 1)

    def rotation_error(n, pool):
        member, other = rotation_row(n, pool)
        return float(np.sqrt(pool * member ** 2 + (n - pool) * other ** 2) * np.sqrt(2 / np.pi))

    for pool in (3, 6, 12, 25, 50, 100, 400):
        show(f'rotation N=400 pool {pool} max influence', rotation_row(400, pool)[0])
        show(f'rotation N=400 pool {pool} error', rotation_error(400, pool))
        show(f'rotation N=400 pool {pool} alpha/pool', alpha / pool)
    show('flat benchmark error N=400', float(np.sqrt(400 * (1 / 400) ** 2) * np.sqrt(2 / np.pi)))
    for n in (50, 100, 200, 400, 800):
        show(f'rotation pool 12 N={n} max influence', rotation_row(n, 12)[0])
        show(f'rotation pool 12 N={n} multiple of flat', rotation_row(n, 12)[0] * n)
        need = next(r for r in range(1, n + 1) if rotation_row(n, r)[0] <= 2.0 / n)
        print(f'  pool needed within a factor of two of flat at N={n}: {need} ({100.0 * need / n:.1f} per cent of N)')
    check('pool needed at N=400', next(r for r in range(1, 401) if rotation_row(400, r)[0] <= 2.0 / 400), 104)
    check('pool needed at N=800', next(r for r in range(1, 801) if rotation_row(800, r)[0] <= 2.0 / 800), 208)
    caucus = np.sqrt(3 * (1 / 6) ** 2 + 397 * (0.5 / 397) ** 2) * np.sqrt(2 / np.pi)
    show('caucus of three holding half, N=400, error', float(caucus))
    show('caucus of three holding half, N=400, each member share', 1 / 6)
    closed = np.sqrt(5 * (1 / 5) ** 2) * np.sqrt(2 / np.pi)
    show('closed core of five returning nothing, error', float(closed))

    # ---- part2 influence: the regime, elder and prescription tables Chapters Eight to Eleven quote --
    # Chapters Eight, Nine and Eleven and the paper print influence weights and consensus errors for
    # flat, dominant, caucus and closed-core regimes, the elder-statesman family and the twenty-six-per-
    # cent contrast. They come from model/part2_influence.py and its cache; this block reads the cache
    # (and rebuilds the caucus and closed core from their stated constructions) so that they stand in
    # the notebook with assertions, and not only in the loose any-decimal-in-any-cache test.
    print('part2 influence regimes and elders (Chapters Eight to Eleven)')
    P2 = load('part2_influence.json')
    dominance = {row['alpha']: row for row in P2['dominance']}
    sizes = (10, 50, 250, 500)
    flat_err, dom_err, cau_err, core_err = {}, {}, {}, {}
    for n in sizes:
        for label, alpha_, store in (('flat', 0.0, flat_err), ('dominant', 0.35, dom_err)):
            top, err = dominance[alpha_][str(n)]
            show(f'{label} N={n} max influence', top)
            show(f'{label} N={n} error', err)
            store[n] = err
        cau_err[n] = float(np.sqrt(3 * (1 / 6) ** 2 + (n - 3) * (0.5 / (n - 3)) ** 2) * np.sqrt(2 / np.pi))
        core_err[n] = float(np.sqrt(5 * (1 / 5) ** 2) * np.sqrt(2 / np.pi))
        show(f'caucus of 3 holding half N={n} error', cau_err[n])
        show(f'closed core of 5 N={n} error', core_err[n])
    show('caucus of 3 holding half, each member', 1 / 6)
    show('closed core of 5, each member', 1 / 5)
    show('closed core of 5, share held in aggregate', 5 * (1 / 5))
    show('closed core of 5, share held outside the core', 1 - 5 * (1 / 5))
    for n in (10, 500):
        spread = max(flat_err[n], dom_err[n], cau_err[n], core_err[n]) / min(
            flat_err[n], dom_err[n], cau_err[n], core_err[n])
        show(f'four regimes, largest error over smallest, N={n}', spread)
    check('four regimes within about 40 per cent at N=10', round(core_err[10] / flat_err[10], 2), 1.41)
    check('four regimes about a factor of ten apart at N=500', round(core_err[500] / flat_err[500], 1), 10.0)
    check('dominant error limit at N=500 (0.35 * sqrt(2/pi))', round(dom_err[500], 3), 0.280)
    for alpha_ in (0.05, 0.1):
        top, err = dominance[alpha_]['1000']
        show(f'dominant {alpha_} N=1000 error', err)
        show(f'dominant {alpha_} N=1000 error over flat', err / dominance[0.0]['1000'][1])
    show('flat N=1000 error', dominance[0.0]['1000'][1])
    check('five per cent dominant over flat at N=1000', round(dominance[0.05]['1000'][1] / dominance[0.0]['1000'][1], 2), 1.84)
    check('ten per cent dominant over flat at N=1000', round(dominance[0.1]['1000'][1] / dominance[0.0]['1000'][1], 1), 3.3)
    elders = {(row['elders'], row['alpha_elder']): row for row in P2['elders']}
    for n in (10, 50, 250, 1000):
        top, err, _, ratio = elders[(3, 0.1)][str(n)]
        show(f'3 elders at 0.10 N={n} max influence', top)
        show(f'3 elders at 0.10 N={n} error', err)
        show(f'3 elders at 0.10 N={n} error over flat', ratio)
    check('3 elders at 0.10 error ratios', [round(elders[(3, 0.1)][str(n)][3], 2) for n in (10, 50, 250, 1000)],
          [1.01, 1.08, 1.35, 2.08])
    for row in P2['elders_vs_prescription']:
        tag = f"{row['elders']} elders at {row['alpha_elder']} office {row.get('alpha_office')}"
        for n in (10, 25, 50, 250, 1000):
            if str(n) in row:
                show(f'prescription {tag} N={n} multiple of flat', row[str(n)][2])
    firsts = [row['elders_vs_prescription'][0][str(n)][2] for row in [P2] for n in (50, 100, 250, 500, 1000)]
    check('rotation-only prescription holds at 2.0 from N=50', [round(v, 3) for v in firsts], [1.996] * 5)
    check('rotation-only prescription at N=10 and 25',
          [round(P2['elders_vs_prescription'][0][str(n)][2], 2) for n in (10, 25)], [1.82, 2.11])
    clique = P2['scaling'][0]
    imbalance = P2['scaling'][1]
    for n in (10, 1000):
        show(f'clique of three, inward to one, N={n} each member', clique[str(n)][0])
        show(f'imbalanced member N={n} share', imbalance[str(n)][0])

    # The random control asks whether the book's use of maximum influence as a proxy for the 2-norm of the
    # influence vector (which alone sets the consensus error) is an artefact of the hand-built families.
    # Random row-stochastic matrices, 200 seeded draws per cell; deterministic given that seed.
    print('part2 random-network controls (Chapter Eight proxy)')
    control = collections.defaultdict(list)
    for row in P2['random_control']:
        control[row['n']].append(row)
        show(f"random network N={row['n']} concentration {row['conc']} mean max influence", row['max_mean'])
        show(f"random network N={row['n']} concentration {row['conc']} mean error", row['err_mean'])
        show(f"random network N={row['n']} concentration {row['conc']} corr(max influence, error)", row['corr_max_err'])
    rows = P2['random_control']
    check('random control cells (3 sizes x 5 concentrations, 200 draws each)', len(rows), 15)
    check('random control: mean error is sqrt(2/pi) times mean 2-norm in every cell',
          all(abs(r['err_mean'] - np.sqrt(2 / np.pi) * r['l2_mean']) < 1e-9 for r in rows), True)
    check('random control: max influence and error correlate positively in every cell, from 0.35 to 0.97',
          [round(min(r['corr_max_err'] for r in rows), 2), round(max(r['corr_max_err'] for r in rows), 2)],
          [0.35, 0.97])
    check('random control: mean error falls as attention flattens, at every size',
          all(all(a['err_mean'] > b['err_mean'] for a, b in zip(rs, rs[1:])) for rs in control.values()), True)
    check('random control: the flattest cell sits within 0.5 per cent of the flat error',
          all(abs(rs[-1]['err_mean'] / (np.sqrt(2 / np.pi) / np.sqrt(n)) - 1) < 0.005 for n, rs in control.items()), True)

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

    # Paired year-ten contrasts in established-member practice against the full-adherence group.
    # Quality is read among viable groups, so a pair counts only where both runs are viable at
    # year ten (more than five members); a closed run's series stops before year ten. The
    # interval is a normal 95 per cent interval on the paired differences, as the book's others.
    print('part5 paired established-practice contrast at year 10, viable in both')
    full = {int(k.split('|')[2]): v for k, v in d.items() if k.startswith('traj|full|')}
    for cond, label in (('t11_attraction_loss', 'invisible'), ('referral_loss', 'unreferred'),
                        ('t3_combined_loss', 'unwelcoming')):
        other = {int(k.split('|')[2]): v for k, v in d.items() if k.startswith(f'traj|{cond}|')}
        diffs = []
        for seed in sorted(set(full) & set(other)):
            a, b = full[seed], other[seed]
            if len(a['yrN']) > 10 and len(b['yrN']) > 10 and a['yrN'][10] > 5 and b['yrN'][10] > 5:
                diffs.append(b['yrQ_established'][10] - a['yrQ_established'][10])
        diffs = np.array(diffs)
        half = 1.96 * diffs.std(ddof=1) / np.sqrt(len(diffs))
        print(f'  {label} minus full: n={len(diffs)} mean={diffs.mean():.4f} '
              f'[{diffs.mean() - half:.4f}, {diffs.mean() + half:.4f}]')
        check(f'{label} paired practice interval crosses zero at year 10',
              bool(diffs.mean() - half <= 0 <= diffs.mean() + half), cond == 't11_attraction_loss')

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

    # ---- decay ordering at 400 paired seeds -------------------------------------------
    # The one-at-a-time screen reverses the attraction-minus-referral ordering on final
    # membership at large downward moves of delta0, on three seeds. These are the 400-seed
    # re-estimates at seven distances, paired by seed across all twenty-one cells: the
    # default rate and 25, 50 and 75 per cent lower from decay_ordering.json, and 10, 15
    # and 20 per cent lower, which locate the membership reversal, from decay_reversal.json.
    cells = collections.defaultdict(dict)
    for _name in ('decay_ordering.json', 'decay_reversal.json'):
        for r in rows_of(_name)[1]:
            cells[(r['pc'], r['scen'])][r['seed']] = r
    print('decay ordering at 400 paired seeds')

    def _wilson(k, n, z=1.96):
        p = k / n
        den = 1 + z * z / n
        c = (p + z * z / (2 * n)) / den
        h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
        return c - h, c + h

    for pc in sorted({k[0] for k in cells}, reverse=True):
        rate = m.DEFAULTS['delta0'] * (1 + pc / 100)
        show(f'decay ordering pc={pc} delta0', rate)
        show(f'decay ordering pc={pc} half-life weeks', math.log(2) / rate)
        for scen in ('full', 'attraction', 'referral'):
            rr = list(cells[(pc, scen)].values())
            N = np.array([r['N'] for r in rr], float)
            show(f'decay ordering pc={pc} {scen} N', N.mean())
            show(f'decay ordering pc={pc} {scen} N half-width', 1.96 * N.std(ddof=1) / np.sqrt(len(N)))
            for fld in ('viable', 'exists', 'closed'):
                k = sum(r[fld] for r in rr)
                lo, hi = _wilson(k, len(rr))
                print(f'  decay ordering pc={pc} {scen} {fld}: {k} of {len(rr)}')
                show(f'decay ordering pc={pc} {scen} {fld} fraction', k / len(rr), pct=True)
                show(f'decay ordering pc={pc} {scen} {fld} Wilson lo', lo, pct=True)
                show(f'decay ordering pc={pc} {scen} {fld} Wilson hi', hi, pct=True)
        a, b = cells[(pc, 'attraction')], cells[(pc, 'referral')]
        seeds = sorted(set(a) & set(b))
        for fld in ('N', 'viable', 'exists'):
            dd = np.array([a[s][fld] - b[s][fld] for s in seeds], float)
            hw = 1.96 * dd.std(ddof=1) / np.sqrt(len(dd))
            print(f'  decay ordering pc={pc} attraction minus referral {fld}: strict={int((dd > 0).sum())}, '
                  f'ties={int((dd == 0).sum())}, reversals={int((dd < 0).sum())}')
            for sign, name in ((1, 'attraction minus referral'), (-1, 'referral minus attraction')):
                show(f'decay ordering pc={pc} {name} {fld}', sign * dd.mean())
                show(f'decay ordering pc={pc} {name} {fld} lo', sign * dd.mean() - hw)
                show(f'decay ordering pc={pc} {name} {fld} hi', sign * dd.mean() + hw)

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
        # Ties are real in this matrix, and the product can split one by a bit: step 4's T1
        # and T2 are both 0.35 and come out 5.6e-17 apart, and steps 6, 7, 9 and 10 tie at
        # zero with four or five others. numpy's default sort orders ties differently on
        # different machines, so the principal and the rank printed here depended on the
        # machine. Values rounded to 12 places and a stable sort name the lower-numbered
        # tradition in a tie, and the rank is the competition rank CLAUDE.md prescribes,
        # which a tie shares: one more than the number of traditions strictly above.
        row = np.round(B[i], 12)
        o = np.argsort(-row, kind='stable')
        rank = 1 + int((row > row[i]).sum())
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

    def hu(x, places):
        """Half-up rendering of a percentage, as the prose rounds; 67.35 is 67.4, not 67.3."""
        from decimal import Decimal, ROUND_HALF_UP
        return str(Decimal(repr(round(float(x), 10))).quantize(Decimal(1).scaleb(-places),
                                                                 rounding=ROUND_HALF_UP))

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
                  f'{hu(100*c/N, 1)} [{hu(lo, 1)}, {hu(hi, 1)}]  {hu(lo, 2)} {hu(hi, 2)}')
    fstruct = lambda rg: (np.where(m.S > 0, rg.uniform(.05, 1., m.S.shape), 0.),
                          np.where(m.GOV > 0, rg.uniform(.05, 1., m.GOV.shape), 0.))
    counts, N = coupling_test(fstruct, 23)
    for lab, c in zip(('T1_top', 'all12', 'S5_to_T12', 'S12_to_T5'), counts):
        lo, hi = wilson_pct(c, N)
        print(f'  structural {lab}: {100*c/N:.4f}% [{lo:.4f}, {hi:.4f}]  '
              f'{hu(100*c/N, 1)} [{hu(lo, 1)}, {hu(hi, 1)}]  {hu(lo, 2)} {hu(hi, 2)}')

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

def emit_paper_extras():
    """Figures the paper prints that the chapters do not, or prints at other precision."""
    # Wilson intervals on the decline table's viable fractions. The chapters print the
    # fraction; the paper prints the interval beside it.
    def _wilson(k_, n_, z=1.96):
        p = k_ / n_
        den = 1 + z * z / n_
        c = (p + z * z / (2 * n_)) / den
        h = z * math.sqrt(p * (1 - p) / n_ + z * z / (4 * n_ * n_)) / den
        return max(0.0, c - h), min(1.0, c + h)

    d = load("part5.json")
    traj = collections.defaultdict(list)
    for key, row in d.items():
        if key == "meta" or not key.startswith("traj|"):
            continue
        traj[key.split("|")[1]].append(row)
    for cond, rows in sorted(traj.items()):
        yr = np.zeros((len(rows), 31))
        for i, r in enumerate(rows):
            s = [0.0 if x is None else x for x in r["yrN"]][:31]
            yr[i, :len(s)] = s
        for y in (5, 10, 20, 30):
            for lab, mask in (("viable", yr[:, y] > 5), ("exists", yr[:, y] > 0)):
                lo, hi = _wilson(int(mask.sum()), len(rows))
                show(f"part5 {cond} y{y} {lab} Wilson lo", lo, pct=True)
                show(f"part5 {cond} y{y} {lab} Wilson hi", hi, pct=True)

    # Structural variants and the horizon series, to two decimals.
    d, rs = rows_of("structural.json")
    g = collections.defaultdict(list)
    for key, row in d.items():
        if key == "meta":
            continue
        variant, scenario, _seed = key.split("|")
        g[(variant, scenario)].append(row)
    for (variant, scenario), rows in sorted(g.items()):
        for fld in ("N", "exists", "viable"):
            show(f"structural {variant} {scenario} {fld}",
                 np.mean([r[fld] for r in rows]), pct=fld in ("exists", "viable"))

    mc = load("mc_error.json")
    mcrows = [v for k, v in mc.items() if k != "meta"]
    hg = collections.defaultdict(list)
    for row in mcrows:
        hg[tuple(row["job"][:3])].append(row)
    for key in sorted(hg, key=lambda x: (x[0], x[2], x[1])):
        rows = hg[key]
        show(f"mc {key[0]} dt={key[1]} h={key[2]} N", np.mean([r["N"] for r in rows]))

    sob = load("sobol.json")["result"]
    for outcome in ("membership", "mean_practice"):
        show(f"sobol {outcome} sum S1", sum(sob[outcome]["S1"]))
        show(f"sobol {outcome} sum ST", sum(sob[outcome]["ST"]))

    # Governance sparsity pricing: flip k cells confined to the enabling rows, so the
    # two-tier split is held fixed, and ask how often each Part Four claim survives.
    # This is the paper's table and has no cache; it is seeded and recomputed here.
    spec = importlib.util.spec_from_file_location("ec", str(ROOT / "model" / "elicitation_compare.py"))
    ec = importlib.util.module_from_spec(spec)
    sys.modules["ec"] = ec
    spec.loader.exec_module(ec)
    #
    # Since 3 October 2026 it is computed exactly and strictly. A flipped cell takes exactly
    # 0.5, so a Step's strongest Traditions often tie exactly, and floating point broke those
    # ties in the last bit in an order that depends on the processor: an emulated x86 printed
    # 53.2 per cent where every real machine printed 53.0. Every weight in S and GOV is a
    # multiple of 0.01, so the products below, taken on the weights times 100, are exact.
    # And a claim holds in a draw only where it holds strictly, because a tie is not
    # support: a Step whose own Tradition ties for the top does not count as index-pairing
    # failing. The draws are the same as before. `ec.consequences` is left as it is, because
    # its hash is pinned for the elicitation; these are its four claims with ties made
    # explicit.
    live = [(j, r) for j in range(12) for r in range(8) if j not in ec.PROTECTIVE]
    check("enabling cells available to flip", float(len(live)), 56.0, tol=0.01)
    S100 = np.round(m.S * 100)
    check("every S weight is in hundredths", bool(np.allclose(m.S * 100, S100, atol=1e-9)))
    check("every GOV weight is in hundredths",
          bool(np.allclose(m.GOV * 100, np.round(m.GOV * 100), atol=1e-9)))

    def unique_top(v):
        top = np.flatnonzero(v == v.max())
        return int(top[0]) if len(top) == 1 else None

    rng = np.random.default_rng(20260802)
    ND = 2000
    for k in (1, 2, 3, 4, 6, 8, 12, 16):
        c = dict(all12=0, t1=0, s5=0, s12=0)
        for _ in range(ND):
            G = m.GOV.copy()
            for i in rng.choice(len(live), k, replace=False):
                j, r = live[i]
                G[j, r] = 0.0 if G[j, r] > 0 else 0.5
            B = S100 @ np.round(G * 100).T
            c["all12"] += all(B[i].max() > B[i, i] for i in range(12))
            c["t1"] += unique_top(B.sum(0)) == 0
            c["s5"] += unique_top(B[4]) == 11
            c["s12"] += unique_top(B[11]) == 4
        for lab, v in c.items():
            show(f"sparsity {k} flips {lab}", v / ND, pct=True)
            lo, hi = _wilson(v, ND)
            show(f"sparsity {k} flips {lab} Wilson lo", lo, pct=True)
            show(f"sparsity {k} flips {lab} Wilson hi", hi, pct=True)


emit()
emit_paper_extras()
print("published figures block complete")
'''


PAPER_TRACEABILITY = r'''
print("Paper traceability")
print("Every decimal the paper prints must be reachable from the model source, a hash-linked")
print("cache, or the derived block above. tools/check_book.py enforces this for the chapters;")
print("nothing enforced it for the paper until this cell, which is why the paper notebook is no")
print("longer a copy of the book notebook.")

import glob as _glob, io as _io, os as _os, re as _re
from contextlib import redirect_stdout as _redirect

_buf = _io.StringIO()
with _redirect(_buf):
    emit()
    emit_paper_extras()
_derived = _buf.getvalue()

_corpus = [MODEL.read_text()]
for _f in sorted(_glob.glob(str(RESEARCH / "*.json"))):
    if _os.path.basename(_f) == "audit-pre-correction-manifest.json":
        continue
    _corpus.append(open(_f, errors="ignore").read())
_corpus.append(_derived)
_blob = "\n".join(_corpus)
_cands = _re.findall(r"\d+\.\d+", _blob)

def _reachable(n):
    if n in _blob:
        return True
    d = len(n.split(".")[1])
    _target = float(n)
    for c in _cands:
        try:
            if round(float(c), d) == _target:
                return True
        except ValueError:
            pass
    return False

_tex = (ROOT / "paper" / "anonymity-as-an-aggregation-condition.tex").read_text()
_tex = _re.sub(r"(?<!\\)%.*", "", _tex)                      # LaTeX comments are not claims
_tex = _re.sub(r"doi:\S+|10\.\d{4,}/\S+|ISBN[\s:0-9X-]+", " ", _tex, flags=_re.I)
_SOURCE_FIGURES = {"0.053", "0.061"}  # Carrell, Sacerdote and West (2013), as the paper cites it
_nums = sorted(set(_re.findall(r"\d+\.\d+", _tex)) - _SOURCE_FIGURES)
_missing = [n for n in _nums if not _reachable(n)]
print(f"  INFO decimals printed in the paper: {len(_nums)}")
check("every paper decimal traces to the model, a cache, or a derivation", _missing, [])
'''


PAPER_CLAIMS = r'''
print("Paper headline claims against the caches")

_gate = load("release_gate_results.json")
_rows = [v for k, v in _gate.items() if k != "meta" and isinstance(v, dict) and "condition" in v]
_by = collections.defaultdict(dict)
for _r in _rows:
    _by[_r["condition"]][_r["seed"]] = _r
check("release gate holds 3,200 runs", len(_rows), 3200)
check("eight conditions", len(_by), 8)

for _cond, _want in (("base", 17.8000), ("t3_friction_loss", 14.8375),
                     ("t3_governance_loss", 11.7725), ("t3_combined_loss", 6.7550),
                     ("t11_attraction_loss", 12.3800), ("t11_governance_loss", 15.5150),
                     ("t11_combined_loss", 11.9200), ("recipient_unconstrained", 18.8275)):
    _n = float(np.mean([r["N"] for r in _by[_cond].values()]))
    check(f"paper table: {_cond} mean final N", round(_n, 4), _want)

_base = _by["base"]
def _paired(cond):
    _s = sorted(set(_base) & set(_by[cond]))
    _d = np.asarray([_base[k]["N"] - _by[cond][k]["N"] for k in _s], float)
    _hw = 1.96 * _d.std(ddof=1) / math.sqrt(len(_d))
    return _d.mean(), _d.mean() - _hw, _d.mean() + _hw

for _cond, _eff in (("t3_combined_loss", 11.045), ("t11_attraction_loss", 5.420)):
    _m, _lo, _hi = _paired(_cond)
    check(f"paper: baseline minus {_cond}", round(_m, 3), _eff)
    check(f"paper: {_cond} interval excludes zero", bool(_lo > 0), True)

_s = sorted(set(_base) & set(_by["recipient_unconstrained"]))
_d = np.asarray([_by["recipient_unconstrained"][k]["N"] - _base[k]["N"] for k in _s], float)
_hw = 1.96 * _d.std(ddof=1) / math.sqrt(len(_d))
check("paper: recipient contrast is unresolved, interval crosses zero",
      bool(_d.mean() - _hw < 0 < _d.mean() + _hw), True)

_sob = load("sobol.json")
check("paper: Sobol runs on eight factors", len(_sob["meta"]["factors"]), 8)
check("paper: membership first-order column is admissible, no S1 above its ST",
      any(a > b for a, b in zip(_sob["result"]["membership"]["S1"],
                                _sob["result"]["membership"]["ST"])), False)
check("paper: practice first-order column is withheld, delta0 inverts",
      _sob["result"]["mean_practice"]["S1"][1] > _sob["result"]["mean_practice"]["ST"][1], True)

_st = load("structural.json")
_sg = collections.defaultdict(list)
for _k, _r in _st.items():
    if _k == "meta":
        continue
    _v, _sc, _ = _k.split("|")
    _sg[(_v, _sc)].append(_r)
for _v in _st["meta"]["variants"]:
    _a, _rf = _sg[(_v, "attraction")], _sg[(_v, "referral")]
    check(f"paper: referral loss is worse than attraction loss in {_v}",
          all(np.mean([x[f] for x in _a]) > np.mean([x[f] for x in _rf])
              for f in ("N", "exists", "viable")), True)
'''


FINAL = r'''
print("Final notebook verdict")
check("no accumulated assertion failures", len(FAILURES), 0)
print("CLEAN CACHE-BACKED VERIFICATION NOTEBOOK")
'''


def notebook(title: str, blurb: str, extra: tuple = ()) -> dict:
    """Return one notebook as a dict: a title cell, the shared check cells, then `extra`.

    Every notebook gets the same setup, model, cache, release, secondary, robustness and
    figure cells, so the two stay in step. `extra` holds the source of cells that only this
    notebook has (the paper's claim and traceability checks), placed before the final verdict.
    """
    return {
        "cells": [
            markdown(
                f"# {title}\n\n{blurb}\n\n"
                "Generated by `tools/regenerate_notebooks.py`. "
                "Expensive analyses are cache-backed and hash-checked."
            ),
            code(SETUP),
            code(MODEL_CHECKS),
            code(CACHE_CHECKS),
            code(RELEASE_RESULTS),
            code(SECONDARY_RESULTS),
            code(ROBUSTNESS_RESULTS),
            code(PUBLIC_FIGURES),
            *[code(c) for c in extra],
            code(FINAL),
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def build() -> dict:
    """Both notebooks as the generator writes them, keyed by path, for main() and the tests."""
    return {
        ROOT / "model" / "book-calculations.ipynb": notebook(
            "Nobody in Charge: released calculations",
            "Verifies the model's identity and semantics, every registered cache's completeness "
            "and provenance, the released results, and the derivation of every figure the "
            "chapters print. `tools/check_book.py` checks the chapters against this notebook's "
            "output."),
        ROOT / "paper" / "anonymity-as-an-aggregation-condition.ipynb": notebook(
            "Anonymity as an Aggregation Condition: verification notebook",
            "Everything the book notebook verifies, and then two things specific to the paper. "
            "It re-derives the paper's headline claims from the caches, and it checks that every "
            "decimal the paper prints is reachable from the model source, a hash-linked cache, or "
            "a derivation shown here. Nothing enforced that for the paper before: the chapters "
            "have `tools/check_book.py` and the paper had no equivalent, which is why this "
            "notebook used to be a copy of the book's.",
            extra=(PAPER_CLAIMS, PAPER_TRACEABILITY)),
    }


def main() -> None:
    """Write both notebooks from `build()` and print each path relative to the repository."""
    for path, data in build().items():
        path.write_text(json.dumps(data, indent=1) + "\n")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    from tool_help import help_requested
    help_requested(__doc__)
    main()
