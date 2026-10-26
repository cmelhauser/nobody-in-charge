# Errata for the frozen analysis scripts

The scripts in this directory are hash-frozen. Each one records its SHA-256 in the cache it
produced, and `tools/check_release.py` fails when a script no longer matches its cache, so
correcting a docstring or a comment in one of them would discard hours of computed results for
no change in any number. Their stale pointers and slips are therefore recorded here, in a file
no cache depends on. Appendix A10.1 maps the retired appendix identifiers; this file adds the
rest. If a script is ever rerun for another reason, correct its entries below in the same commit
and delete the rows.

`aa_group_model.py` carries no file, chapter, cache or section pointer. Its module docstring says
member heterogeneity "converts individual bistability into graded group-level response". The
corrected audit found a high-start and low-start split in only 7 of 400 environments
(`research/ch14_individual.json`; Chapter 14), and the paper's third limitation says the mechanism
the sentence describes is not established. Read the sentence as the original design intent.

| Script and line | It says | What is true now |
|---|---|---|
| `core_thresholds.py:9` | `exp_thr` is what "appendix A6 and Chapter 4 mean by" an experienced member | A6 is numerical resolution. The calibration statement is in A11 item 1; Chapter 4 is still right |
| `mc_error.py:11` | "Euler step of 0.5 half-weeks" | `dt` is 0.5 weeks, not half-weeks |
| `morris_screen.py:24` | governance cancels exactly in "appendix A5.3" | the cancellation is in A2.3; A5.3 is now the Chapter 14 correction |
| `part5_runs.py:4` | the endpoint table is "notebook section 1" | the book notebook block `scenarios_hiseed` (the notebooks have no numbered sections) |
| `part5_runs.py:25` | "Appendix A3.4" | A4 (retired identifier; see A10.1) |
| `part5_runs.py:44` | `H = 1560  # 30 years in half-weeks` | 1560 is weeks (thirty years at 52 weeks) |
| `resource_list_test.py:3`, `:31` | "Appendix A5.6", "A5.4", "A9", "A5.4b" | A7.1 (the design registry), A7.3, A7.6 and A8; bare A5.4 is now "Trajectories and selection", and the vacuity of multiplicative designs is recorded in A7.1 |
| `scenarios_hiseed.py:9` | the table matches "the notebook's section 1" | the notebook block `scenarios_hiseed` |
| `sobol_indices.py:5`, `:65` | "appendix A4.6 and A5.5", "A5.5" | A7.5, Morris and Sobol results |
| `structural_variants.py:3`, `:29` | A5.6 "What no design covers"; "the same five decline scenarios as `scenarios_hiseed.py`" | A7.1 lists the designs and none that combine failure modes; `scenarios_hiseed.py` now runs six conditions with different names |
| `tradition_paired.py:5` | "Notebook section 3" | the book notebook has no numbered sections; the paired Tradition comparison is under "Calibration, Chapter 14, service, and paired Tradition comparison" |
| `tradition_paired.py:10` | "`CLAUDE.md` rule 0" | the statistical rules are the "Statistical rules" section of `CLAUDE.md`; it has no numbered rules |
| `tradition_paired.py:23` | "Horizon 1040 half-weeks, twenty years" | 1040 is weeks |
| `ch13_reps.py:51` | the design "expands to 1,000; only replications 400..999 are new work" | `REPS` is 400 and `CLAUDE.md` keeps 400-seed confirmatory designs; no expansion to 1,000 was made |
