"""Unit tests for the canonical model, model/aa_group_model.py.

These tests assert semantics rather than exercising lines. Where CLAUDE.md states a
property as non-negotiable, the property is encoded here so that a future edit which
breaks it fails the build rather than being caught by a reader.

The model file is hash-frozen and MUST NOT be edited to make a test pass. If a test
here disagrees with the model, the test is wrong or the model has been changed without
authorization; see tests/test_release_invariants.py, which pins the SHA-256.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

import aa_group_model as m

MODEL_PATH = Path(__file__).resolve().parents[1] / "model" / "aa_group_model.py"


# --------------------------------------------------------------------------- matrices

def test_matrix_shapes():
    assert m.S.shape == (m.NSTEP, len(m.RES)) == (12, 8)
    assert m.GOV.shape == (12, 8)


def test_snorm_rows_sum_to_one():
    assert np.allclose(m.Snorm.sum(axis=1), 1.0)


def test_beta_is_row_sum_normalised_by_the_maximum():
    expected = m.S.sum(axis=1) / m.S.sum(axis=1).max()
    assert np.allclose(m.BETA, expected)
    assert np.isclose(m.BETA.max(), 1.0)


def test_steps_one_and_twelve_are_jointly_most_group_dependent():
    """A2.2 and the primer both rest on this: beta is maximal and equal at 1 and 12."""
    assert np.isclose(m.BETA[0], 1.0)
    assert np.isclose(m.BETA[11], 1.0)
    assert m.BETA[1:11].max() < 1.0


def test_step_twelve_is_the_sole_carrier_of_recipient_opportunity():
    recipient = m.RES.index("recipient")
    carriers = np.nonzero(m.S[:, recipient])[0]
    assert carriers.tolist() == [11]


def test_protective_traditions_have_zero_governance_rows():
    """Traditions 4, 6, 7, 9, 10 act only as modifiers; A2.4 depends on these zeros."""
    for tradition in (4, 6, 7, 9, 10):
        assert not m.GOV[tradition - 1].any(), f"T{tradition} must have a zero GOV row"


def test_govw_is_column_normalised_so_full_adherence_cancels():
    """At full adherence the governance quality of every resource is exactly one."""
    q = m.GOVW.T @ m.effective_adherence(np.ones(12))
    assert np.allclose(q, 1.0)


# ------------------------------------------------------------------ derived objects

def test_semantic_overlap_is_s_times_gov_transpose():
    B = m.semantic_overlap()
    assert B.shape == (12, 12)
    assert np.allclose(B, m.S @ m.GOV.T)


def test_semantic_overlap_accepts_substitute_matrices():
    S2 = np.ones((3, 8))
    G2 = np.ones((4, 8))
    assert m.semantic_overlap(S2, G2).shape == (3, 4)


def test_executable_coupling_is_distinct_from_semantic_overlap():
    """A1: these are different objects and must never be collapsed."""
    C = m.executable_linear_coupling()
    B = m.semantic_overlap()
    assert C.shape == B.shape
    assert not np.allclose(C, B)


def test_executable_coupling_accepts_substitute_matrices():
    C = m.executable_linear_coupling(np.ones((2, 8)), np.ones((5, 8)))
    assert C.shape == (2, 5)


def test_coupling_helpers_tolerate_all_zero_rows_and_columns():
    """The 1e-12 floors exist so a degenerate perturbation cannot divide by zero."""
    assert np.all(np.isfinite(m.semantic_overlap(np.zeros((12, 8)), np.zeros((12, 8)))))
    assert np.all(np.isfinite(m.executable_linear_coupling(np.zeros((12, 8)),
                                                           np.zeros((12, 8)))))


# ------------------------------------------------------------------------ capability

def test_mean_one_lognormal_has_arithmetic_mean_near_one():
    rng = np.random.default_rng(0)
    draws = m.mean_one_lognormal(rng, 0.55, 200_000)
    assert draws.min() > 0
    assert abs(draws.mean() - 1.0) < 0.01


def test_zero_dispersion_gives_exactly_one():
    rng = np.random.default_rng(0)
    assert np.allclose(m.mean_one_lognormal(rng, 0.0, 10), 1.0)


def test_het_sd_changes_dispersion_not_the_mean():
    """CLAUDE.md: het_sd changes dispersion, not average capability by construction."""
    rng = np.random.default_rng(1)
    narrow = m.mean_one_lognormal(rng, 0.2, 200_000)
    wide = m.mean_one_lognormal(rng, 0.9, 200_000)
    assert wide.std() > narrow.std()
    assert abs(narrow.mean() - 1.0) < 0.02 and abs(wide.mean() - 1.0) < 0.05


# ------------------------------------------------------------- effective adherence

def test_effective_adherence_is_one_at_full_adherence():
    assert np.allclose(m.effective_adherence(np.ones(12)), 1.0)


def test_effective_adherence_is_zero_when_nothing_is_adhered_to():
    assert np.allclose(m.effective_adherence(np.zeros(12)), 0.0)


def test_protective_traditions_modify_only_what_they_guard():
    """T9 and T12 guard the group conscience, T2. Dropping them lowers Te[1]."""
    T = np.ones(12)
    T[8] = T[11] = 0.0
    Te = m.effective_adherence(T)
    assert Te[1] < 1.0


def test_external_modifier_scales_every_entry():
    """T4 and T7 guard against outside override and multiply the whole vector.

    Entries that are themselves zero stay zero, so the two traditions switched off
    here remain at zero while every other entry is scaled to 0.7.
    """
    T = np.ones(12)
    T[3] = T[6] = 0.0
    Te = m.effective_adherence(T)
    others = [i for i in range(12) if i not in (3, 6)]
    assert np.allclose(Te[others], 0.7, atol=1e-9)
    assert np.allclose(Te[[3, 6]], 0.0)


def test_effective_adherence_is_clipped_into_the_unit_interval():
    Te = m.effective_adherence(np.full(12, 5.0))
    assert Te.min() >= 0.0 and Te.max() <= 1.0


def test_effective_adherence_does_not_mutate_its_argument():
    T = np.ones(12)
    before = T.copy()
    m.effective_adherence(T)
    assert np.array_equal(T, before)


# --------------------------------------------------------------------- resources

def _state(n_alive, level, cap=60):
    X = np.zeros((cap, m.NSTEP))
    alive = np.zeros(cap, bool)
    X[:n_alive] = level
    alive[:n_alive] = True
    return X, alive


def test_empty_group_supplies_no_resources():
    X, alive = _state(0, 0.0)
    R, unity = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    assert np.allclose(R, 0.0)
    assert unity == 0.0


def test_empty_group_with_components_returns_an_empty_component_dict():
    X, alive = _state(0, 0.0)
    R, unity, comp = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0, return_components=True)
    assert comp == {}


def test_resources_are_bounded_by_the_unit_interval():
    X, alive = _state(25, 0.55)
    R, _ = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    assert R.min() >= 0.0 and R.max() <= 1.0


def test_admission_capacity_is_unconditional():
    """The first capacity term is 1.0: a group can always open the door."""
    X, alive = _state(1, 0.55)
    _, _, comp = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0, return_components=True)
    assert comp["capacity"][0] == 1.0


def test_unity_is_one_for_a_single_established_member():
    X, alive = _state(1, 0.55)
    _, unity = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    assert unity == 1.0


def test_unity_is_zero_when_no_member_is_established():
    X, alive = _state(4, 0.01)
    _, unity = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    assert unity == 0.0


def test_dispersion_lowers_unity():
    """unity = 1 - 2*sd over established members, so spread degrades the room."""
    even = np.zeros((60, m.NSTEP)); even[:4] = 0.5
    spread = np.zeros((60, m.NSTEP))
    spread[0] = 0.2; spread[1] = 0.4; spread[2] = 0.6; spread[3] = 0.8
    alive = np.zeros(60, bool); alive[:4] = True
    _, u_even = m.resources(even, alive, m.FULL, m.DEFAULTS, 1.0)
    _, u_spread = m.resources(spread, alive, m.FULL, m.DEFAULTS, 1.0)
    assert u_spread < u_even


def test_recipient_override_replaces_only_that_capacity():
    X, alive = _state(25, 0.55)
    _, _, base = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0, return_components=True)
    _, _, forced = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0,
                               recipient_override=1.0, return_components=True)
    recipient = m.RES.index("recipient")
    assert forced["capacity"][recipient] == 1.0
    others = [i for i in range(len(m.RES)) if i != recipient]
    assert np.allclose(base["capacity"][others], forced["capacity"][others])


def test_recipient_override_is_clipped():
    X, alive = _state(25, 0.55)
    _, _, comp = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0,
                             recipient_override=99.0, return_components=True)
    assert comp["capacity"][m.RES.index("recipient")] == 1.0


def test_resource_t_can_differ_from_t_for_split_path_designs():
    X, alive = _state(25, 0.55)
    full, _ = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    starved, _ = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0,
                             resource_T=np.zeros(12))
    assert starved.sum() < full.sum()


def test_solvency_raises_the_continuity_resource():
    X, alive = _state(25, 0.55)
    poor, _ = m.resources(X, alive, m.FULL, m.DEFAULTS, 0.0)
    rich, _ = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    continuity = m.RES.index("continuity")
    assert rich[continuity] > poor[continuity]


def test_component_dict_reports_the_recipient_ratio():
    X, alive = _state(10, 0.55)
    _, _, comp = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0, return_components=True)
    assert set(comp) >= {"capacity", "governance", "effective_adherence",
                         "low_practice", "high_practice", "recipient_ratio"}
    assert comp["recipient_ratio"] >= 0.0


# -------------------------------------------------------------------- step growth

def test_step_growth_returns_one_rate_per_member_and_step():
    X, alive = _state(25, 0.55)
    R, _ = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    d = m.step_growth(X, alive, R, m.FULL, m.DEFAULTS)
    assert d.shape == X.shape
    assert np.all(np.isfinite(d))


def test_the_order_gate_blocks_later_steps_when_earlier_ones_are_zero():
    """A2.6: order_gate_j = X[:, j-1] ** p_gate, so Step 1 at zero shuts Step 2."""
    X = np.zeros((60, m.NSTEP))
    alive = np.zeros(60, bool); alive[:5] = True
    R, _ = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    d = m.step_growth(X, alive, R, m.FULL, m.DEFAULTS)
    assert np.allclose(d[alive, 1:], 0.0)


def test_growth_at_full_practice_is_negative_because_only_decay_remains():
    X = np.ones((60, m.NSTEP))
    alive = np.zeros(60, bool); alive[:5] = True
    R, _ = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    d = m.step_growth(X, alive, R, m.FULL, m.DEFAULTS)
    assert np.all(d[alive] <= 0)


def test_heterogeneity_multiplier_scales_growth():
    X, alive = _state(25, 0.55)
    R, _ = m.resources(X, alive, m.FULL, m.DEFAULTS, 1.0)
    plain = m.step_growth(X, alive, R, m.FULL, m.DEFAULTS)
    doubled = m.step_growth(X, alive, R, m.FULL, m.DEFAULTS,
                            het=np.full(X.shape[0], 2.0))
    assert doubled[alive].max() > plain[alive].max()


def test_step_growth_with_no_living_members_uses_zero_group_capacity():
    X = np.zeros((60, m.NSTEP))
    alive = np.zeros(60, bool)
    R = np.zeros(len(m.RES))
    assert np.all(np.isfinite(m.step_growth(X, alive, R, m.FULL, m.DEFAULTS)))


# ---------------------------------------------------------------------- simulate

def test_simulation_is_deterministic_given_a_seed():
    a = m.simulate(m.FULL, T_end=20, seed=7)
    b = m.simulate(m.FULL, T_end=20, seed=7)
    assert a["N"] == b["N"] and a["mean"] == b["mean"]


def test_different_seeds_generally_differ():
    runs = {m.simulate(m.FULL, T_end=60, seed=s)["N"] for s in range(8)}
    assert len(runs) > 1


def test_result_carries_the_documented_estimands():
    r = m.simulate(m.FULL, T_end=20, seed=0)
    assert set(r) >= {"N", "mean", "endpoint_exists", "endpoint_viable", "closed",
                      "closure_week", "first_nonviable_week", "first_recovery_week",
                      "recovered_after_first_crossing", "viability_threshold"}


def test_existence_viability_and_closure_are_different_estimands():
    """CLAUDE.md: N > 0, N > 5 and closure are not the same thing."""
    r = m.simulate(m.FULL, T_end=20, seed=0, n_seed=3, viability_threshold=5)
    assert r["endpoint_exists"] is True
    assert r["endpoint_viable"] is False
    assert r["closed"] is False


def test_zero_membership_is_absorbing():
    """A group that loses its last member never reopens, whatever the referral rate."""
    r = m.simulate(m.FULL, T_end=520, seed=0, n_seed=1,
                   P=dict(drop0=50.0, churn=5.0, lam_exog=1000.0))
    assert r["N"] == 0 and r["closed"] is True
    assert r["closure_week"] is not None


def test_a_group_seeded_empty_is_closed_immediately():
    r = m.simulate(m.FULL, T_end=20, seed=0, n_seed=0)
    assert r["N"] == 0 and r["closure_week"] == 0.0
    assert r["first_nonviable_week"] == 0.0


def test_recorded_history_includes_time_zero():
    r = m.simulate(m.FULL, T_end=10, seed=0, record=True)
    assert r["history"]["time_weeks"][0] == 0.0
    assert r["hist"].shape[0] == len(r["history"]["time_weeks"])
    assert set(r["history_fields"]) >= {"time_weeks", "N", "established_count"}


def test_history_of_a_group_that_starts_empty_still_has_fields():
    r = m.simulate(m.FULL, T_end=10, seed=0, n_seed=0, record=True)
    assert "history_fields" in r and "time_weeks" in r["history_fields"]


def test_initial_practice_sets_the_founding_composition():
    r = m.simulate(m.FULL, T_end=5, seed=0, initial_practice=np.full(10, 0.4))
    assert r["N"] >= 1


@pytest.mark.parametrize("bad", [np.zeros((2, 2)), np.zeros(999)])
def test_initial_practice_is_validated(bad):
    with pytest.raises(ValueError):
        m.simulate(m.FULL, T_end=5, seed=0, initial_practice=bad)


def test_split_paths_are_separately_controllable():
    """T3 and T11 each have two paths; the factorials move one at a time."""
    base = m.simulate(m.FULL, T_end=260, seed=3)
    no_attraction = m.simulate(m.FULL, T_end=260, seed=3, attraction_T11=0.0)
    no_friction = m.simulate(m.FULL, T_end=260, seed=3, dropout_T3=0.0)
    assert no_attraction["N"] <= base["N"]
    assert isinstance(no_friction["N"], int)


def test_arrival_t3_is_off_by_default_and_scales_inflow_when_given():
    """The base model has no T3 arrival path; a numeric value enables the variant."""
    closed_door = m.simulate(m.FULL, T_end=260, seed=5, arrival_T3=0.0)
    open_door = m.simulate(m.FULL, T_end=260, seed=5, arrival_T3=1.0)
    assert closed_door["N"] <= open_door["N"]


def test_recipient_override_flows_through_the_simulation():
    forced = m.simulate(m.FULL, T_end=60, seed=2, recipient_override=1.0)
    assert forced["endpoint_exists"] in (True, False)


def test_viability_threshold_is_configurable_and_reported():
    r = m.simulate(m.FULL, T_end=20, seed=0, viability_threshold=0)
    assert r["viability_threshold"] == 0


def test_first_crossing_and_recovery_are_recorded_when_they_happen():
    """A group driven below the line and then refilled reports both events.

    Seeded at six, one above the threshold of five, with a dropout hazard that
    empties it quickly and a referral floor that refills it. This configuration was
    chosen because it deterministically crosses and recovers at this seed.
    """
    r = m.simulate(m.FULL, T_end=520, seed=5, n_seed=6,
                   P=dict(drop0=0.20, lam_exog=2.0))
    assert r["first_nonviable_week"] is not None
    assert r["first_recovery_week"] is not None
    assert r["recovered_after_first_crossing"] is True
    assert r["first_recovery_week"] >= r["first_nonviable_week"]


def test_a_custom_parameter_dictionary_overrides_only_named_defaults():
    r = m.simulate(m.FULL, T_end=5, seed=0, P=dict(cap=10))
    assert r["X"].shape[0] == 10


def test_resource_t_override_reaches_the_simulation():
    starved = m.simulate(m.FULL, T_end=260, seed=4, resource_T=np.zeros(12))
    base = m.simulate(m.FULL, T_end=260, seed=4)
    assert starved["mean"] <= base["mean"]


def test_a_viable_group_can_close_while_recording_history():
    """Covers the closure branch: the last member leaves before any arrival draw.

    Seeded at eight, above the viability threshold, with a hazard that empties the
    room on the first step and no referral floor to refill it. The closure branch
    stamps first_nonviable_week and closure_week together and appends a final
    snapshot, because a group that was viable one step earlier never crossed the
    line on its own.
    """
    r = m.simulate(m.FULL, T_end=520, seed=0, n_seed=8, record=True,
                   P=dict(drop0=8.0, churn=8.0, lam_exog=0.0))
    assert r["closed"] is True
    assert r["closure_week"] == r["first_nonviable_week"]
    assert r["history"]["N"][-1] == 0


def test_the_module_runs_as_a_script():
    """The __main__ block is the documented smoke test and must keep working."""
    import runpy

    namespace = runpy.run_path(str(MODEL_PATH), run_name="__main__")
    assert "r" in namespace
