# Project handoff — expanded robustness and synchronized release

**Written:** 2026-08-06  
**Canonical project:** `/Users/melhauserc/Documents/Claude/nobody-in-charge`  
**Status:** Paused at the user's request because of usage limits. No analysis process is running. The work is substantial but not release-complete.

## 1. Objective and decisions that must not change

Finish a rigorous, internally synchronized release of the model, manuscript, paper, primer, appendix, notebooks, plans, PDFs, and independent verification brief.

The user clarified the sampling request as follows:

- Keep the modeled room/group capacity at **60**. Do not change it to 400 or 1,000.
- Keep the confirmatory stochastic analyses at **400 paired seeds**.
- Increase robustness through more sensitivity draws, parameter perturbations, structural variants, and formal screens—not through a 1,000-person group and not by silently changing the confirmatory estimand.

The executable model is currently frozen and should not be edited unless a newly discovered defect requires an explicit, documented decision:

```text
model/aa_group_model.py
SHA-256 c3823f72cabd454a778464a5a31c13fd09161f2a533b95b315ce833c7add3952
```

Key interpretation decisions already adopted throughout the project:

- `B = S @ GOV.T` is semantic overlap, not the executable update operator.
- Normalized `C = Snorm @ GOVW.T`, the state map, and trajectory effects are distinct objects.
- The recipient term is a low-practice/high-practice potential-helper opportunity ratio, not literal newcomer/veteran measurement; the override is cleanly separated.
- Tradition 3 has separate resource-governance and inverse-practice dropout-friction paths and is evaluated with a paired factorial design.
- Tradition 11 has separate governance and attraction paths; the pure-attraction intervention is the headline intervention.
- `N = 0` is permanently closed. Keep existence (`N > 0`), endpoint viability (`N > 5`), final `N`, first crossing, recovery, and closure distinct.
- Heterogeneity is mean-one lognormal: `exp(N(-sigma^2/2, sigma))`.
- The `rho` exercise is a proxy-averaging demonstration only.
- Composition effects are paired but unresolved; do not claim equivalence.
- The practice scale is cardinal only within the model.
- The sensitivity registry contains **118 numeric values**: 22 scalars, 12 step speeds, 49 nonzero `S` cells, and 35 nonzero `GOV` cells. The protective index-step count is **17**, not 35.

## 2. Source boundary

The deferred corpus under `research/staged/` is intentionally **not incorporated** and is reserved for the next iteration. Do not cite it as evidence, and do not report those staged works as accidental omissions during this release audit.

The active Maxwell and Golub–Jackson sources have been moved under:

- `research/incorporated/Maxwell_1950/`
- `research/incorporated/Golub_Jackson_2010/`

The original Maxwell copy was retained; the identical newly staged duplicate was removed as requested.

## 3. Completed analysis and validated results

All counts below are completed simulation rows unless described as draws or parameter jobs. Their caches include metadata in addition to those rows.

### Confirmatory and focused analyses

- `research/release_gate_results.json`: 3,200 rows, 400 paired seeds across 8 cells.
  - Baseline final `N = 17.800` (95% CI 16.917–18.683); existence 100%; viability 98.5%; closure 0%.
  - T3 friction loss: `N = 14.8375`; viability 94%; closure 0.75%.
  - T3 governance loss: `N = 11.7725`; viability 91.25%; closure 2%.
  - T3 combined loss: `N = 6.755`; existence 75%; viability 54.75%; closure 25%.
  - T11 pure attraction loss: `N = 12.38`; viability 98.5%; closure 0%.
  - T11 governance loss: `N = 15.515`; viability 98%; closure 0%.
  - T11 combined loss: `N = 11.92`; viability 98.5%; closure 0%.
  - Recipient override: `N = 18.8275`; viability 98.75%; closure 0%.
  - Paired final-`N` T3 effects: friction 2.962 (1.848–4.077), governance 6.027 (5.043–7.012), combined 11.045 (10.030–12.060), interaction -2.055 (-3.414 to -0.696).
  - Paired final-`N` T11 effects: attraction 5.420 (4.515–6.325), governance 2.285 (1.214–3.356), combined 5.880 (4.972–6.788), interaction 1.825 (0.755–2.895).
  - Recipient effect 1.028 (-0.259–2.314), unresolved.
- `research/scenarios_hiseed.json`: 2,400 rows. Referral loss ends at `N = 0.51`, existence 10.5%, viability 2.75%, closure 89.5%; referral plus attraction loss ends at `N = 0.0025`, existence 0.25%, viability 0%, closure 99.75%.
- `research/ch13_reps.json`: 3,200 rows. Proxy averaging results are complete; at `rho = 0`, nonpositive estimated effects occur in 53.5% and 55.5% of the one- and three-proxy designs, respectively.
- `research/ch15_service.json`: 1,200 rows. Removing T12 lowers final `N` by 5.325 (4.437–6.213), practice by 0.01497 (0.00765–0.02229), maintenance by 0.01351 (0.00788–0.01915); the Step 9 change is unresolved.
- `research/core_thresholds.json`: 400 runs. Viability 394/400; all-run final `N = 17.8`; viable-only `N = 18.0`; established count 14.13; experienced count 1.25. The old 45-member/9-core target failed and was not retuned.
- `research/part5.json`: 4,800 rows. T3 dose sweep and trajectories are complete. Composition contrasts are unresolved: concentrated-even 0.2925 (-0.898–1.483), split-even -0.3475 (-1.472–0.777), with no equivalence margin.
- `research/ch14_sweep.json`: 3,200 rows. The group-level maintenance sweep is complete.
- `research/ch14_individual.json`: 400 endpoint environments. Individual separation greater than 0.05 appears in only 7/400 (1.75%); the old bistability constants are obsolete.
- `research/mc_error.json`: 2,600 rows. Timestep contrasts remain unresolved. The horizon screen shows final `N` continuing from 17.8 at 30 years to 15.64 at 100 years, so no equilibrium claim is allowed.
- `research/tradition_paired.json`: 5,200 rows. Seven tradition effects resolve and five do not; the reference final `N` is 13.0975 with SD 5.6664.
- Deterministic caches, including `part2_influence.json` and `resource_list.json`, are complete.

### Expanded robustness already complete

- `research/sens3.json`: **1,002 global draws**.
  - Global ±12.5%: attraction-loss minus referral-loss final `N` strict/tie/reversal = 301/0/33; viability = 323/10/1; existence = 318/16/0. Full model is viable in all three repetitions for 302/334 draws and exists in all three for 334/334.
  - Global ±25%: final `N` = 251/1/82; viability = 269/64/1; existence = 262/72/0. Full model viable in all three for 291/334 and exists for 325/334.
  - Global ±50%: final `N` = 213/17/104; viability = 201/117/16; existence = 215/117/2. Full model viable in all three for 256/334 and exists for 287/334.
- `research/tiered.json`: **1,000 tiered draws plus 1,000 randomized executable-matrix draws**.
  - Tiered final `N` strict/tie/reversal = 783/10/207; viability = 818/165/17; existence = 821/177/2. Full model viable in all repetitions for 833/1,000 and exists for 943/1,000.
  - Randomized matrices final `N` = 1,000/0/0; viability = 1,000/0/0; existence = 999/1/0. Full model viable in all repetitions for 784/1,000 and exists for 1,000/1,000.
- `research/structural.json`: **10,000 rows across five architectures**. Referral loss is worse than pure attraction loss on final `N`, existence, and viability in every architecture. The old three-architecture size reversal is retired.
  - Base: attraction `N = 12.38`, existence 1.0, viability 0.985; referral `N = 0.51`, existence 0.105, viability 0.0275.
  - Flat gate: attraction 6.6125/0.87/0.6575; referral 0.745/0.12/0.055.
  - T3 admission: same as base.
  - Capacity-all: attraction 14.73/1.0/1.0; referral 2.0025/0.2575/0.1225.
  - Piecewise-linear clipped response: attraction 13.0375/1.0/0.995; referral 1.02/0.145/0.0575.
- `research/RELEASE-GATE-RESULTS.md` has been generated from the completed confirmatory cache.

## 4. Exact paused checkpoint

The active command was stopped with `SIGTERM`, and a process check found no remaining OAT, Morris, or Sobol workers.

`research/oat_full.json` is valid JSON and uses atomic incremental saves. It contains the baseline and **8 of 118 completed parameter jobs**:

```text
scalar:delta0
scalar:hill_k
scalar:hill_n
scalar:k_ident
scalar:k_proof
scalar:omega
scalar:p_gate
scalar:psi
```

This is 64 of the planned 944 OAT perturbation points. Its metadata remains `status: incomplete`, as it should. Resume with:

```bash
cd /Users/melhauserc/Documents/Claude/nobody-in-charge
python3 model/sensitivity_oat_full.py 8
```

The script will recognize the matching hashes and skip the 8 completed parameter jobs. Current analysis-script hashes:

```text
306802d14cbd1f32b47a6ca3e87701160f0487593647126f4177754dba136ea4  model/sensitivity_oat_full.py
17b0e54d301f6a34ab9816bbabcfad6f2b66fd45ed848c7ef246d2bb12a0c20d  model/morris_screen.py
d7fb5bf63f089a27b799711443d936d515b8398ba5a94ac267c0de52e73b1d5d  model/sobol_indices.py
```

## 5. Remaining analysis, in required order

1. Finish OAT and confirm `research/oat_full.json` reports 118 parameter jobs, 944 perturbations, and `status: complete`.
2. Run the expanded Morris screen:

   ```bash
   python3 model/morris_screen.py 8
   ```

   It evaluates 20 trajectories over all 118 factors: 2,380 model points, five common-random-number seeds per point. It is a screen, not a confirmatory confidence design.
3. Inspect `research/morris.json` and rank factors by the membership outcome's `mu_star`.
4. Before running Sobol, update **only** `FACTORS` in `model/sobol_indices.py` to the actual eight Morris leaders. Scalar identifiers must be converted from `scalar:name` to `name`; `a:i` identifiers may remain as written. If an `S` or `GOV` cell ranks in the top eight, extend the Sobol evaluator carefully rather than pretending it is a scalar default.
5. Run Sobol only after that factor update:

   ```bash
   python3 model/sobol_indices.py 8
   ```

   The design is 1,024 base rows, 10,240 Saltelli points, plus 1,024 residual-noise points: 11,264 cached evaluations, five seeds per point.
6. Generate the combined robustness report:

   ```bash
   python3 tools/summarize_robustness.py
   ```

Do not edit a completed analysis script after generating its cache unless the associated cache is deliberately invalidated and rerun; the release gate checks both model and script hashes.

## 6. Documentation already revised

The following source documents have received major corrections and synchronization work:

- `appendix/APPENDIX.md`: replaced with a concise, current, self-contained technical appendix. Section A7.5 still awaits final OAT/Morris/Sobol results.
- `research/PARAMETERS.md`: replaced with the current audit and robustness designs. Section 8 awaits final OAT/Morris/Sobol results.
- `AGENT_VERIFY.md`: replaced with a read-only, fail-closed independent verification brief. It needs final OAT/Morris/Sobol expectations and artifact status.
- `reference/PREFACE.md`: global, tiered, matrix, and structural sensitivity claims corrected.
- `paper/anonymity-as-an-aggregation-condition.tex`: abstract, conclusion, structural analysis, design language, source boundary, trajectories, and old reversal claims corrected.
- Manuscript chapters 1, 2, 6, 16, 18, 21, 23, and 24: counts, dating, source locations, structural-history wording, outcome definitions, and unsupported contemporary membership claims corrected.
- `reference/PRIMER-steps-and-traditions.md`: stale model values, registered-value language, Maxwell provenance, and staged-corpus boundary corrected.
- Project plans: Part 3, Part 5, release plan, and `CLAUDE.md` now reflect the current proxy, structural, and verification decisions.
- `README.md`: substantially revised, but its run status and release sequence must be updated after completion.
- Added `tools/regenerate_notebooks.py` and `tools/summarize_robustness.py`.
- Expanded `tools/check_release.py` to require the complete caches, expanded designs, source boundary, stored notebook output, semantic invariants, and fresh artifacts.

`python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md` already reported all clear apart from nonblocking long-sentence warnings. The appendix is not in chapter format, so a chapter-check failure on it is irrelevant.

## 7. Prose still pending after the final screens

Replace the remaining old OAT/Morris/Sobol numbers only after the new caches are complete:

- `manuscript/ch01-chases-tavern.md`, near the sensitivity paragraph around line 223.
- `manuscript/ch06-the-sociologist.md`, near the old thirty-draw/87%/236-point paragraph around line 108.
- `manuscript/ch12-twelve-dials.md`, near the old OAT ranking and old `.4386`, `.0045`, and `.1458` values around lines 34 and 167.
- `paper/anonymity-as-an-aggregation-condition.tex`, sensitivity section near line 1083.
- `appendix/APPENDIX.md`, section A7.5.
- `research/PARAMETERS.md`, section 8.
- `AGENT_VERIFY.md`, the expected final-screen and release sections.
- `README.md`, status and final reproduction order.

Run a final stale-language audit, excluding JSON and PDF files:

```bash
rg -n --glob '!*.json' --glob '!*.pdf' \
  '236|two hundred and thirty-six|235 of 236|two hundred and thirty-five|exactly two simulation|two results that survive|three of (the )?four|1,190 evaluations|25 replications per cell|41\.7|7\.7|23\.4|11\.9|47\.3 members|0\.1458|100 / 100 / 87|97%|73%|58%|94%' \
  manuscript paper reference appendix research/PARAMETERS.md README.md CLAUDE.md BOOK-PLAN.md plans AGENT_VERIFY.md
```

Some hits in explicit correction histories may be legitimate. Audit them rather than deleting them mechanically.

Also search public prose narrowly for language that treats the executable low-practice/high-practice proxy as literal “newcomer” and “veteran” measurement. Ordinary historical prose may still use those words; only proxy-identification claims need correction. Review endpoint “survival/death” terminology so it does not conflate existence, viability, and absorbing closure.

## 8. Notebook, check, and build sequence

After all caches and prose are final:

```bash
python3 tools/regenerate_notebooks.py
python3 tools/run_notebook.py
python3 tools/run_notebook.py --paper
python3 tools/check_book.py
python3 tools/check_chapter.py reference/PRIMER-steps-and-traditions.md
python3 tools/build_book.py
tectonic --outdir paper paper/anonymity-as-an-aggregation-condition.tex
pandoc reference/PRIMER-steps-and-traditions.md \
  -o reference/PRIMER-steps-and-traditions.pdf --pdf-engine=tectonic
python3 tools/check_release.py
```

If the primer's existing paper size or margins are encoded elsewhere, preserve them rather than accepting layout drift. Reorder the README and appendix reproduction blocks so all three PDFs are built before the final release check.

Expected final PDFs:

- `build/nobody-in-charge.pdf`
- `paper/anonymity-as-an-aggregation-condition.pdf`
- `reference/PRIMER-steps-and-traditions.pdf`

The PDFs currently on disk predate the latest source edits and must not be treated as current deliverables.

## 9. Required PDF QA

After rebuilding, use `pdfinfo` to record page counts and sizes; render every page with Poppler; inspect contact sheets for all pages; and inspect representative or suspicious pages at high/original resolution. Check for clipped equations, bad page breaks, overflow, missing glyphs, stale tables, blank pages, and inconsistent headers. The release gate also requires each PDF to be nontrivial and newer than its public sources.

## 10. Final synchronization

The canonical project is the Claude folder named above. The intended mirror is:

```text
/Users/melhauserc/Documents/Codex/2026-08-05/nobody-in-charge-review
```

That mirror has **not** been brought up to date with this paused state. After the canonical release passes, perform a read-only `rsync --dry-run` comparison, then synchronize carefully, and verify that the mirror matches. Do not delete user material or unrelated metadata merely to force equality.

## 11. Current release condition

`tools/check_release.py` is expected to fail at this checkpoint because OAT is incomplete; Morris, Sobol, and `research/ROBUSTNESS-RESULTS.md` are not final; notebooks have not been regenerated; and PDFs have not been rebuilt. This is intentional and is the correct fail-closed state.

The next agent should resume at section 5, preserve all completed caches, update every dependent claim from the completed results, then run the full notebook, source, PDF, release, and mirror checks before calling the project finished.
