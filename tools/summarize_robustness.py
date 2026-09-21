#!/usr/bin/env python3
"""Generate research/ROBUSTNESS-RESULTS.md from the expanded release caches."""
from __future__ import annotations

import collections
import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "research"
OUT = R / "ROBUSTNESS-RESULTS.md"


def load(name):
    return json.loads((R / name).read_text())


def hw(values):
    a = np.asarray(values, float)
    return 1.96 * a.std(ddof=1) / math.sqrt(len(a))


def classify(rows, left, right):
    d = np.asarray([row[left] - row[right] for row in rows], float)
    return int((d > 0).sum()), int((d == 0).sum()), int((d < 0).sum())


def render() -> str:
    """The report's full text, so a test can compare it with the committed file."""
    lines = [
        "# Expanded Robustness Results",
        "",
        "Generated from the JSON caches by `tools/summarize_robustness.py`. Screening",
        "parameter points use three or five common seeds and are not confirmatory replications.",
        "The principal condition contrasts remain the separate 400-seed analyses, and the",
        "decay-ordering section below is one of them rather than a screen.",
        "",
    ]

    model_hash = hashlib.sha256((ROOT / "model" / "aa_group_model.py").read_bytes()).hexdigest()
    lines += ["## Provenance", "", f"- Model SHA-256: `{model_hash}`"]
    for name in ("mc_error.json", "tradition_paired.json", "structural.json", "sens3.json",
                 "tiered.json", "oat_full.json", "decay_ordering.json", "decay_reversal.json",
                 "morris.json", "sobol.json"):
        data = load(name)
        meta = data.get("meta", data.get("_meta", {}))
        assert meta.get("status") == "complete", f"{name} incomplete"
        if "model_sha256" in meta:
            assert meta["model_sha256"] == model_hash, f"{name} model hash"
        lines.append(f"- `{name}`: complete, script `{meta.get('script', 'legacy')}`")

    mc = load("mc_error.json")
    mcrows = [v for k, v in mc.items() if k != "meta"]
    groups = collections.defaultdict(list)
    for row in mcrows:
        groups[tuple(row["job"][:3])].append(row)
    lines += [
        "", "## Integration and horizon", "",
        "| Scenario | dt | Horizon years | Seeds | Mean N [95% half-width] | Existence | Viability | Closure |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key in sorted(groups, key=lambda x: (x[0], x[2], x[1])):
        scen, dt, horizon = key
        rows = groups[key]
        nvals = [r["N"] for r in rows]
        lines.append(
            f"| {scen} | {dt:g} | {horizon/52:g} | {len(rows)} | "
            f"{np.mean(nvals):.3f} [{hw(nvals):.3f}] | "
            f"{np.mean([r['exists'] for r in rows]):.3f} | "
            f"{np.mean([r['viable'] for r in rows]):.3f} | "
            f"{np.mean([r['closed'] for r in rows]):.3f} |"
        )
    base200 = {r["seed"]: r for r in groups[("full", 0.5, 1560)] if r["seed"] < 200}
    lines += ["", "Paired final-N differences relative to `dt=0.5`:", ""]
    for dt in (1.0, 0.25, 0.125):
        comp = {r["seed"]: r for r in groups[("full", dt, 1560)]}
        d = np.asarray([comp[s]["N"] - base200[s]["N"] for s in range(200)], float)
        lines.append(f"- `dt={dt:g}` minus `dt=0.5`: {d.mean():.3f} [{d.mean()-hw(d):.3f}, {d.mean()+hw(d):.3f}].")
    lines.append("None resolves. The horizon series continues to move and is not a steady-state proof.")

    trad = load("tradition_paired.json")
    lines += [
        "", "## Paired Tradition degradation", "",
        f"Reference membership is {trad['result']['base_mean']:.4f}; cross-seed SD is "
        f"{trad['result']['base_sd']:.4f}. T3 and T11 are mixed adherence interventions.",
        "", "| Tradition | Loss [95% interval] | t |", "|---:|---:|---:|",
    ]
    for row in sorted(trad["result"]["rows"], key=lambda r: -r["loss"]):
        lines.append(f"| T{row['tradition']} | {row['loss']:.3f} [{row['lo']:.3f}, {row['hi']:.3f}] | {row['t']:.2f} |")

    structural = load("structural.json")
    sg = collections.defaultdict(list)
    for key, row in structural.items():
        if key == "meta":
            continue
        variant, scenario, _seed = key.split("|")
        sg[(variant, scenario)].append(row)
    lines += [
        "", "## Structural variants", "",
        "| Variant | Scenario | Mean N | Existence | Viability |",
        "|---|---|---:|---:|---:|",
    ]
    for variant in structural["meta"]["variants"]:
        for scenario in structural["meta"]["scenarios"]:
            rows = sg[(variant, scenario)]
            assert len(rows) == 400
            lines.append(
                f"| {variant} | {scenario} | {np.mean([r['N'] for r in rows]):.3f} | "
                f"{np.mean([r['exists'] for r in rows]):.3f} | "
                f"{np.mean([r['viable'] for r in rows]):.3f} |"
            )
    lines += ["", "Attraction-minus-referral structural ordering by variant:", ""]
    for variant in structural["meta"]["variants"]:
        att = sg[(variant, "attraction")]
        ref = sg[(variant, "referral")]
        lines.append(
            f"- `{variant}`: mean-N difference "
            f"{np.mean([r['N'] for r in att])-np.mean([r['N'] for r in ref]):.3f}; "
            f"viability difference "
            f"{np.mean([r['viable'] for r in att])-np.mean([r['viable'] for r in ref]):.3f}; "
            f"existence difference "
            f"{np.mean([r['exists'] for r in att])-np.mean([r['exists'] for r in ref]):.3f}."
        )

    lines += ["", "## Global, tiered, and randomized-matrix screens", ""]
    designs = []
    sens = load("sens3.json")
    designs += [(key, sens[key]) for key in ("g125", "g250", "g500")]
    tier = load("tiered.json")
    designs += [(key, tier[key]) for key in ("tiered", "randmat")]
    lines += [
        "Positive strict counts below mean the pure-attraction-loss condition ends larger or",
        "more viable than referral loss. Ties are reported separately.", "",
        "| Design | Draws | N strict/tie/reversal | Viability strict/tie/reversal | Existence strict/tie/reversal | Full viable in all 3 seeds |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name, rows in designs:
        cn = classify(rows, "att_N", "ref_N")
        cv = classify(rows, "att_s", "ref_s")
        ce = classify(rows, "att_exists", "ref_exists")
        full = sum(r["full_s"] == 1 for r in rows)
        lines.append(f"| {name} | {len(rows)} | {cn[0]}/{cn[1]}/{cn[2]} | {cv[0]}/{cv[1]}/{cv[2]} | {ce[0]}/{ce[1]}/{ce[2]} | {full}/{len(rows)} |")

    oat = load("oat_full.json")
    points = []
    for pid, values in oat.items():
        if pid in ("meta", "baseline"):
            continue
        for tag, scenarios in values.items():
            points.append((pid, tag, scenarios))
    assert len(points) == 944
    n_d = np.asarray([p[2]["attraction"]["N"] - p[2]["referral"]["N"] for p in points])
    v_d = np.asarray([p[2]["attraction"]["surv"] - p[2]["referral"]["surv"] for p in points])
    e_d = np.asarray([p[2]["attraction"]["exists"] - p[2]["referral"]["exists"] for p in points])
    lines += [
        "", "## Multi-level one-at-a-time screen", "",
        f"Across 944 points, the attraction-minus-referral final-N ordering is strict/tie/reversal "
        f"{int((n_d>0).sum())}/{int((n_d==0).sum())}/{int((n_d<0).sum())}. Endpoint-viability "
        f"ordering is {int((v_d>0).sum())}/{int((v_d==0).sum())}/{int((v_d<0).sum())}.",
        f"Existence ordering is {int((e_d>0).sum())}/{int((e_d==0).sum())}/{int((e_d<0).sum())}.",
        f"Full adherence is viable in all three seeds at {sum(p[2]['full']['surv']==1 for p in points)} of 944 points and exists in all three at {sum(p[2]['full']['exists']==1 for p in points)} points.",
    ]

    morris = load("morris.json")
    cells = collections.defaultdict(dict)
    for name in ("decay_ordering.json", "decay_reversal.json"):
        for key, row in load(name).items():
            if key != "meta":
                cells[(row["pc"], row["scen"])][row["seed"]] = row
    levels = sorted({k[0] for k in cells}, reverse=True)
    lines += [
        "", "## Decay-ordering confirmation", "",
        "The multi-level screen's `delta0` membership reversals, re-estimated at 400 seeds shared by",
        "all twenty-one cells, so every contrast is paired by common random numbers. Full adherence",
        "otherwise, 1,560 weeks, dt 0.5. Attraction is the pure T11 attraction path with governance",
        "held at one; referral is `lam_exog = 0`. The default rate and 25, 50 and 75 per cent lower",
        "come from `decay_ordering.json`; 10, 15 and 20 per cent lower, which locate the membership",
        "reversal, from `decay_reversal.json`, whose design differs only in its level list.", "",
        "| delta0 change | Condition | Mean N [95% half-width] | Existence | Viability | Closure |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for pc in levels:
        for scen in ("full", "attraction", "referral"):
            rows = list(cells[(pc, scen)].values())
            nvals = [r["N"] for r in rows]
            lines.append(
                f"| {pc}% | {scen} | {np.mean(nvals):.3f} [{hw(nvals):.3f}] | "
                f"{np.mean([r['exists'] for r in rows]):.3f} | "
                f"{np.mean([r['viable'] for r in rows]):.3f} | "
                f"{np.mean([r['closed'] for r in rows]):.3f} |")
    lines += [
        "", "Attraction-minus-referral paired differences:", "",
        "| delta0 change | Outcome | Mean [95% paired interval] | Strict | Tied | Reversed |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for pc in levels:
        a, b = cells[(pc, "attraction")], cells[(pc, "referral")]
        seeds = sorted(set(a) & set(b))
        for fld in ("N", "viable", "exists"):
            diff = np.asarray([a[s][fld] - b[s][fld] for s in seeds], float)
            h = hw(diff)
            lines.append(
                f"| {pc}% | {fld} | {diff.mean():.3f} [{diff.mean() - h:.3f}, {diff.mean() + h:.3f}] | "
                f"{int((diff > 0).sum())} | {int((diff == 0).sum())} | {int((diff < 0).sum())} |")

    lines += [
        "", "## Morris screen", "",
        "Twenty trajectories; values are output change per unit proportional parameter change.",
        "High sigma indicates interaction or nonlinearity and does not separate them.", "",
        "| Membership rank | Factor | mu | mu* | sigma |", "|---:|---|---:|---:|---:|",
    ]
    leaders = sorted(morris["result"]["rows"], key=lambda r: -r["membership"]["mu_star"])
    for rank, row in enumerate(leaders[:15], 1):
        x = row["membership"]
        lines.append(f"| {rank} | {row['id']} | {x['mu']:.3f} | {x['mu_star']:.3f} | {x['sigma']:.3f} |")

    sobol = load("sobol.json")
    factors = sobol["meta"]["factors"]
    lines += [
        "", "## Sobol decomposition", "",
        "The decomposition is conditional on the eight listed Morris leaders and the stated",
        "plus-or-minus 25 per cent ranges. First-order and total-order intervals are bootstrap",
        "intervals over base rows.", "",
        "| Factor | Membership S1 [95%] | Membership ST [95%] | Practice S1 [95%] | Practice ST [95%] |",
        "|---|---:|---:|---:|---:|",
    ]
    for i, factor in enumerate(factors):
        cells = []
        for outcome in ("membership", "mean_practice"):
            r = sobol["result"][outcome]
            cells += [f"{r['S1'][i]:.3f} [{r['S1_lo'][i]:.3f}, {r['S1_hi'][i]:.3f}]",
                      f"{r['ST'][i]:.3f} [{r['ST_lo'][i]:.3f}, {r['ST_hi'][i]:.3f}]"]
        lines.append(f"| {factor} | " + " | ".join(cells) + " |")
    lines += ["", f"Noise-replicate total-order diagnostics: {sobol['result']['noise_floor_ST']}." , ""]

    return "\n".join(lines)


def main():
    OUT.write_text(render())
    print(OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
