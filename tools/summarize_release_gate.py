#!/usr/bin/env python3
"""Render the corrected release-gate cache as a human-auditable report."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "research" / "release_gate_results.json"
MODEL = ROOT / "model" / "aa_group_model.py"
OUT = ROOT / "research" / "RELEASE-GATE-RESULTS.md"


def load_model():
    spec = importlib.util.spec_from_file_location("summary_model", MODEL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def pct(x):
    return f"{100*x:.1f}%"


def ci_mean(s):
    return f"{s['mean']:.3f} [{s['lo']:.3f}, {s['hi']:.3f}]"


def ci_prop(s):
    return f"{pct(s['proportion'])} [{pct(s['lo'])}, {pct(s['hi'])}]"


def top_sets(M):
    return [[int(j)+1 for j in np.flatnonzero(np.isclose(row, row.max()))] for row in M]


def ranks(M):
    return [int(1 + np.sum(row > row[i])) for i, row in enumerate(M)]


def rows(cache, cond):
    return [cache[f"{cond}|{seed}"] for seed in range(cache["meta"]["nseed"])]


def main():
    cache = json.loads(CACHE.read_text())
    if cache["meta"]["status"] != "complete":
        raise RuntimeError("release-gate cache is incomplete")
    mm = load_model()
    summary = cache["summary"]
    labels = {
        "base": "Baseline",
        "t3_friction_loss": "T3 friction loss only",
        "t3_governance_loss": "T3 governance loss only",
        "t3_combined_loss": "T3 combined loss",
        "t11_attraction_loss": "T11 attraction loss only",
        "t11_governance_loss": "T11 governance loss only",
        "t11_combined_loss": "T11 combined loss",
        "recipient_unconstrained": "Recipient capacity forced to one",
    }
    lines = [
        "# Corrected Release-Gate Results",
        "",
        "This is the human-readable view of research/release_gate_results.json. It is generated",
        "from the cache, not copied by hand.",
        "",
        "## Provenance and design",
        "",
        f"- Model SHA-256: {cache['meta']['model_sha256']}",
        f"- Analysis SHA-256: {cache['meta']['script_sha256']}",
        f"- Jobs: {cache['meta']['jobs_completed']} of {cache['meta']['jobs_expected']}",
        f"- Seeds: 0-{cache['meta']['nseed']-1}, paired across conditions",
        f"- Horizon: {cache['meta']['horizon_weeks']} weeks; dt={cache['meta']['dt_weeks']} week; "
        f"{int(cache['meta']['horizon_weeks']/cache['meta']['dt_weeks']):,} integration steps",
        "- Endpoint existence is N>0. Endpoint viability is N>5. N=0 is permanent closure.",
        "- Crossing N<=5 is not absorbing; recovery above 5 is recorded.",
        "- Continuous intervals are normal 95% intervals for paired or unpaired means as labelled.",
        "- Binary condition intervals are Wilson intervals; binary contrasts retain pairing and report exact McNemar p-values in the cache.",
        "",
        "## Condition outcomes",
        "",
        "| Condition | Final N, mean [95% CI] | P(N>0) [95% CI] | P(N>5) [95% CI] | Ever crossed N<=5 | Recovered after crossing | P(N=0) |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for cond in cache["meta"]["conditions"]:
        s = summary["conditions"][cond]
        rr = rows(cache, cond)
        cross = sum(r["first_nonviable_week"] is not None for r in rr)
        rec = sum(r["recovered_after_first_crossing"] for r in rr)
        lines.append(
            f"| {labels[cond]} | {ci_mean(s['N'])} | {ci_prop(s['endpoint_exists'])} | "
            f"{ci_prop(s['endpoint_viable'])} | {cross}/{cache['meta']['nseed']} | "
            f"{rec}/{cross if cross else 0} | {ci_prop(s['closed'])} |"
        )

    lines += [
        "",
        "A crossing followed by recovery does not imply the run remained viable thereafter.",
        "Endpoint viability and first passage answer different questions.",
        "",
        "## Paired mechanism contrasts",
        "",
        "Positive final-N contrasts below mean the intact or unconstrained first condition ends larger.",
        "",
        "| Contrast | Paired final-N difference [95% CI] | Paired viability risk difference [95% CI] |",
        "|---|---:|---:|",
    ]
    contrast_order = [
        ("T3 friction: baseline minus loss", "t3_friction_loss"),
        ("T3 governance: baseline minus loss", "t3_governance_loss"),
        ("T3 combined: baseline minus loss", "t3_combined_loss"),
        ("T11 attraction: baseline minus loss", "t11_attraction_loss"),
        ("T11 governance: baseline minus loss", "t11_governance_loss"),
        ("T11 combined: baseline minus loss", "t11_combined_loss"),
        ("Recipient unconstrained minus baseline", "recipient_unconstrained_minus_base"),
    ]
    for label, key in contrast_order:
        c = summary["paired_contrasts"][key]
        lines.append(f"| {label} | {ci_mean(c['N'])} | {ci_mean(c['endpoint_viable'])} |")

    lines += [
        "",
        "## Factorial interactions",
        "",
        "The interaction is baseline - path-loss - governance-loss + combined-loss.",
        "",
        "| Tradition | Outcome | Path loss with governance intact [95% CI] | Governance loss with other path intact [95% CI] | Interaction [95% CI] |",
        "|---|---|---:|---:|---:|",
    ]
    for label in ("t3", "t11"):
        for outcome in ("N", "endpoint_viable"):
            f = summary["factorials"][label][outcome]
            lines.append(
                f"| {label.upper()} | {outcome} | {ci_mean(f['path_loss_at_governance_intact'])} | "
                f"{ci_mean(f['governance_loss_at_other_path_intact'])} | "
                f"{ci_mean(f['loss_interaction'])} |"
            )

    recipient = summary["paired_contrasts"]["recipient_unconstrained_minus_base"]["N"]
    recipient_verdict = (
        "includes zero, so the clean recipient-capacity ablation is unresolved"
        if recipient["lo"] <= 0 <= recipient["hi"]
        else "excludes zero, so the clean recipient-capacity ablation is resolved at the 5% level"
    )
    lines += [
        "",
        "The two paths for each Tradition are reported separately and jointly; the interaction",
        "term shows why their contrasts must not be added. The recipient intervention changes only",
        f"recipient capacity and gives a paired final-N contrast of {recipient['mean']:.3f} ",
        f"[{recipient['lo']:.3f}, {recipient['hi']:.3f}]. That interval {recipient_verdict}.",
        "",
        "## Viability-threshold sensitivity",
        "",
        "| Condition | P(N>0) | P(N>1) | P(N>3) | P(N>5) | P(N>10) |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for cond in ("base", "t3_combined_loss", "t11_attraction_loss", "t11_combined_loss"):
        ns = np.array([r["N"] for r in rows(cache, cond)])
        vals = [pct(float(np.mean(ns > k))) for k in (0, 1, 3, 5, 10)]
        lines.append(f"| {labels[cond]} | " + " | ".join(vals) + " |")

    B = mm.semantic_overlap()
    C = mm.executable_linear_coupling()
    raw_top, exe_top = top_sets(B), top_sets(C)
    lines += [
        "",
        "## Semantic overlap versus executable linear coupling",
        "",
        "B = S GOV^T is the raw author-coded semantic overlap. C = Snorm GOVW^T is the",
        "no-capacity linear map from effective adherence to Step resource bundles. Neither is",
        "the full state-update map or a trajectory effect.",
        "",
        "| Step | Raw B maximizing Tradition set | Raw own-index competition rank | C maximizing Tradition set | C own-index competition rank |",
        "|---:|---:|---:|---:|---:|",
    ]
    rb, rc = ranks(B), ranks(C)
    for i in range(12):
        lines.append(f"| {i+1} | {raw_top[i]} | {rb[i]} | {exe_top[i]} | {rc[i]} |")
    lines += [
        "",
        f"Raw loads: {', '.join(f'T{i+1}={v:.4f}' for i,v in enumerate(B.sum(0)))}.",
        "",
        f"Linear executable loads: {', '.join(f'T{i+1}={v:.4f}' for i,v in enumerate(C.sum(0)))}.",
        "",
        "Step 4 has a raw T1/T2 tie. Competition ranks preserve exact ties and structural zeros.",
        "",
        "## Heterogeneity correction",
        "",
        "Capability is drawn as exp(N(-sigma^2/2, sigma)), so its arithmetic expectation is one.",
        "Changing het_sd now changes dispersion without mechanically changing mean capability.",
        "",
    ]
    OUT.write_text("\n".join(lines))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
