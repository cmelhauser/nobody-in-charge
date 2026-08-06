"""
Stochastic model of an AA group: members, resources, traditions, membership flow.

Design principles:
  * The causal chain runs one way: member states produce group RESOURCES; the
    TRADITIONS are group-level policy variables governing resource supply;
    resources feed step growth.
  * Protective traditions (4, 6, 7, 9, 10) act only as multipliers on the
    enabling traditions they guard.
  * Membership is endogenous. Inflow = exogenous referrals (courts, treatment)
    + attraction via members' Step-12 practice and Tradition 11.
  * Tradition 3 has two separately controllable paths: resource governance and
    inverse-practice-weighted dropout friction. Tradition 11 likewise has
    resource-governance and attraction paths. The default uses both paths; the
    split controls support clean mechanism comparisons.
  * Individual capacity is Hill-gated (bistability, per the relapse
    literature); member heterogeneity converts individual bistability into
    graded group-level response.
"""
import numpy as np

NSTEP = 12
RES = ["admission","identify","proof","confidential","counsel","recipient","continuity","pressure"]

# step -> resource consumption (the S matrix from the first-principles derivation)
S = np.array([
 [0.8,1.0,0.3,0.0,0.0,0.0,0.2,0.1],
 [0.0,0.4,1.0,0.0,0.1,0.0,0.2,0.0],
 [0.0,0.0,0.2,0.0,0.3,0.0,0.1,0.1],
 [0.0,0.1,0.0,0.0,0.3,0.0,0.0,0.4],
 [0.0,0.1,0.0,1.0,0.3,0.0,0.2,0.1],
 [0.0,0.0,0.1,0.0,0.2,0.0,0.0,0.3],
 [0.0,0.0,0.1,0.0,0.1,0.0,0.0,0.2],
 [0.0,0.0,0.0,0.1,0.4,0.0,0.0,0.3],
 [0.0,0.0,0.0,0.3,0.9,0.0,0.1,0.2],
 [0.0,0.0,0.0,0.1,0.2,0.0,0.5,0.7],
 [0.0,0.0,0.1,0.0,0.1,0.0,0.2,0.4],
 [0.2,0.1,0.1,0.0,0.1,1.0,0.6,0.3],
], float)
Snorm = S / S.sum(axis=1, keepdims=True)
BETA  = S.sum(axis=1); BETA = BETA/BETA.max()      # derived group-dependence
VIABILITY_THRESHOLD = 5

DEFAULTS = dict(
    a       = np.array([.30,.25,.25,.18,.22,.20,.20,.18,.15,.25,.20,.22]),
    delta0  = 0.06, psi = 0.20, p_gate = 1.5,
    hill_n  = 3.0,  hill_k = 0.12, omega = 0.75,
    k_ident = 3.0, k_proof = 3.0, k_conf = 2.0, k_couns = 3.0, k_recip = 2.0,
    exp_thr = 0.50, act_thr = 0.10,
    lam0    = 0.050,       # attraction -> inflow scaling (per unit att, per week)
    lam_exog= 0.12,        # exogenous arrivals/week (courts, treatment, desperation)
    churn   = 0.004,      # practice-INDEPENDENT weekly exit (moves, deaths)
    drop0   = 0.035,       # baseline weekly dropout hazard at zero practice
    drop_k  = 4.0,         # how strongly early practice protects against dropout
    cap     = 60,          # room capacity
    cost    = 50.0, contrib = 2.0,   # weekly rent, average basket per established member
    het_sd  = 0.55,        # lognormal sd of member-level growth capability
)

# tradition -> resource governance (the G matrix from the first-principles derivation)
GOV = np.array([
 [0.2,0.5,0.3,0.3,0.2,0.1,0.9,0.6],   # T1 unity
 [0.0,0.0,0.0,0.1,0.9,0.0,0.2,0.2],   # T2 group conscience
 [1.0,0.4,0.0,0.0,0.0,0.8,0.1,0.0],   # T3 open membership
 [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],   # T4 autonomy      (protective)
 [0.1,0.4,0.5,0.0,0.0,0.9,0.3,0.2],   # T5 one purpose
 [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],   # T6 no endorsement (protective)
 [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],   # T7 self-support   (protective)
 [0.0,0.1,0.1,0.3,0.1,0.0,0.0,0.0],   # T8 non-professional
 [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],   # T9 no hierarchy   (protective)
 [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],   # T10 no outside    (protective)
 [0.0,0.2,0.7,0.0,0.0,0.6,0.2,0.0],   # T11 attraction
 [0.1,0.3,0.0,1.0,0.1,0.0,0.1,0.0],   # T12 anonymity
], float)
GOVW = GOV / np.maximum(GOV.sum(axis=0, keepdims=True), 1e-12)   # column-normalised


def semantic_overlap(S_matrix=None, GOV_matrix=None):
    """Author-coded semantic overlap B = S G^T.

    This object is useful for describing which Step-resource and
    Tradition-resource codes overlap. It is not the state-update map, a
    transition matrix, or a trajectory effect.
    """
    Sm = S if S_matrix is None else np.asarray(S_matrix, float)
    Gm = GOV if GOV_matrix is None else np.asarray(GOV_matrix, float)
    return Sm @ Gm.T


def executable_linear_coupling(S_matrix=None, GOV_matrix=None):
    """No-capacity coefficient map C from effective adherence to Step bundles.

    The full executable response also includes effective_adherence, member-side
    resource capacity, clipping, BETA, growth gates, state, births, and deaths.
    """
    Sm = S if S_matrix is None else np.asarray(S_matrix, float)
    Gm = GOV if GOV_matrix is None else np.asarray(GOV_matrix, float)
    sn = Sm / np.maximum(Sm.sum(axis=1, keepdims=True), 1e-12)
    gw = Gm / np.maximum(Gm.sum(axis=0, keepdims=True), 1e-12)
    return sn @ gw.T


def mean_one_lognormal(rng, sigma, size):
    """Draw positive capability multipliers with arithmetic expectation one."""
    sigma = float(sigma)
    return np.exp(rng.normal(-0.5 * sigma * sigma, sigma, size))

def effective_adherence(T):
    """Protective traditions raise the EFFECTIVE adherence of what they guard.
    Applied ONCE each -- no stacking, no double counting.."""
    Te = T.astype(float).copy()
    Te[1] = T[1]*(0.6+0.4*0.5*(T[8]+T[11]))     # T9, T12 guard group conscience
    Te[4] = T[4]*(0.6+0.4*0.5*(T[5]+T[9]))      # T6, T10 guard primary purpose
    ext   = 0.7+0.3*0.5*(T[3]+T[6])             # T4, T7 guard against outside override
    return np.clip(Te*ext, 0, 1)

def resources(X, alive, T, P, solvent, resource_T=None, recipient_override=None,
              return_components=False):
    """Resource r is supplied by member capacity, scaled by a GOVERNANCE-WEIGHTED
    AVERAGE of the adherence of the traditions that govern r.  Averaging (not
    multiplying) is what stops a 20% shortfall compounding into 50%.

    resource_T can differ from T in split-path designs. The recipient capacity
    is opportunity per potential helper: low-practice members divided by
    high-practice members, passed through a saturation curve. The proxy contains
    no tenure, cohort, sponsorship, or matching state. recipient_override, when
    supplied, replaces only that capacity while holding S, BETA, and all other
    mechanisms fixed.
    """
    sat = lambda c,k: c/(c+k)
    if alive.sum()==0:
        empty = (np.zeros(len(RES)), 0.0)
        return (*empty, {}) if return_components else empty
    lv   = X[alive].mean(axis=1)
    core = lv > P['act_thr']; exp = lv > P['exp_thr']; low_practice = ~core
    Tr   = T if resource_T is None else np.asarray(resource_T, float)
    Te   = effective_adherence(Tr)
    q    = GOVW.T @ Te                      # quality of governance for each resource, in [0,1]
    unity = 1-2*lv[core].std() if core.sum()>1 else (1.0 if core.sum()==1 else 0.0)
    unity = float(np.clip(unity,0,1))

    recipient_ratio = low_practice.sum()/max(exp.sum(),1.0)
    recipient_capacity = sat(recipient_ratio, P['k_recip'])
    if recipient_override is not None:
        recipient_capacity = float(np.clip(recipient_override, 0, 1))
    cap = np.array([                        # member-side capacity for each resource
        1.0,
        sat(core.sum(), P['k_ident']) * unity,
        sat(exp.sum(),  P['k_proof']),
        sat(exp.sum(),  P['k_conf']),
        sat(exp.sum(),  P['k_couns']),
        recipient_capacity,                 # opportunity per high-practice potential helper
        (0.45+0.55*solvent) * unity,
        unity,
    ])
    result = np.clip(cap*q, 0, 1)
    if return_components:
        comp = dict(capacity=cap.copy(), governance=q.copy(), effective_adherence=Te.copy(),
                    low_practice=int(low_practice.sum()), high_practice=int(exp.sum()),
                    recipient_ratio=float(recipient_ratio))
        return result, unity, comp
    return result, unity

def step_growth(X, alive, R, T, P, het=None):
    hill = lambda M: M**P['hill_n']/(P['hill_k']**P['hill_n']+M**P['hill_n'])
    G    = Snorm @ R                                    # each step's resource bundle
    gate = np.ones_like(X); gate[:,1:] = np.clip(X[:,:-1],0,1)**P['p_gate']
    peer = (1-BETA) + BETA*G
    own  = hill(X[:,9:12].mean(axis=1))
    Gcap = own[alive].mean() if alive.sum() else 0.0
    C    = own + (1-own)*P['omega']*Gcap
    # The capacity gate models collapse in members with something to maintain.
    # An arrival has nothing to maintain, so the gate phases in with step
    # index: it barely touches Steps 1-3 and fully binds Steps 8-12.
    wgt  = np.linspace(0.05, 1.0, NSTEP)          # per-step exposure to the gate
    Cm   = 1.0 - wgt[None,:]*(1.0 - C[:,None])
    g    = P['a']*gate*peer*Cm
    if het is not None: g = g*het[:,None]
    d    = np.full(X.shape, P['delta0']); d[:,:11] *= (1+P['psi']*(1-X[:,1:12]))
    return g*(1-X) - d*X

def simulate(T, P=None, T_end=520, dt=0.5, seed=0, n_seed=25, x_seed=0.55,
             record=False, resource_T=None, dropout_T3=None, attraction_T11=None,
             recipient_override=None, initial_practice=None, arrival_T3=None,
             viability_threshold=VIABILITY_THRESHOLD):
    """Simulate one group.

    T gives the default adherence for every path. resource_T, dropout_T3, and
    attraction_T11 override one path at a time for mechanism-factorial designs.
    arrival_T3 is normally None because T3 has no arrival path in the base
    model; a numeric value enables an explicit admission-path variant.
    initial_practice may be a vector of founder practice levels. A group with
    zero members is closed permanently; a group at or below viability_threshold
    but above zero continues and may recover.
    """
    P = {**DEFAULTS, **(P or {})}
    T = np.asarray(T, float)
    resource_T = T.copy() if resource_T is None else np.asarray(resource_T, float)
    dropout_T3 = float(T[2] if dropout_T3 is None else dropout_T3)
    attraction_T11 = float(T[10] if attraction_T11 is None else attraction_T11)
    rng = np.random.default_rng(seed)
    cap = P['cap']
    X = np.zeros((cap,NSTEP)); alive = np.zeros(cap,bool)
    het = mean_one_lognormal(rng, P['het_sd'], cap)
    if initial_practice is None:
        X[:n_seed] = x_seed
    else:
        initial_practice = np.asarray(initial_practice, float)
        if initial_practice.ndim != 1 or len(initial_practice) > cap:
            raise ValueError('initial_practice must be a one-dimensional vector no longer than cap')
        n_seed = len(initial_practice)
        X[:n_seed] = initial_practice[:, None]
    alive[:n_seed] = True

    def snapshot(time_weeks):
        n_now = int(alive.sum())
        levels = X[alive].mean(axis=1) if n_now else np.array([])
        established = levels > P['act_thr'] if n_now else np.array([], bool)
        experienced = levels > P['exp_thr'] if n_now else np.array([], bool)
        return dict(
            time_weeks=float(time_weeks),
            N=n_now,
            all_member_practice=float(levels.mean()) if n_now else 0.0,
            established_count=int(established.sum()) if n_now else 0,
            established_practice=float(levels[established].mean())
            if n_now and established.sum() else 0.0,
            experienced_count=int(experienced.sum()) if n_now else 0,
            low_practice_fraction=float((levels <= P['act_thr']).mean()) if n_now else 0.0,
        )

    history = [snapshot(0.0)] if record else []
    initial_viable = int(alive.sum()) > viability_threshold
    first_nonviable_week = None if initial_viable else 0.0
    first_recovery_week = None
    closure_week = 0.0 if alive.sum() == 0 else None
    was_viable = initial_viable
    for step in range(int(T_end/dt)):
        n = alive.sum()
        if n==0: break
        lv = X[alive].mean(axis=1)
        established = (lv > P['act_thr']).sum()
        solvent = 1.0 if established*P['contrib'] >= P['cost'] else \
                  float(np.clip(established*P['contrib']/P['cost'],0,1))
        R,unity = resources(X, alive, T, P, solvent, resource_T=resource_T,
                            recipient_override=recipient_override)
        X = np.clip(X + dt*step_growth(X, alive, R, T, P, het), 0, 1)
        X[~alive] = 0.0
        # ---- outflow: dropout hazard falls with practice
        # dropout keyed to EARLY-step practice: a newcomer who has taken Step 1 is
        # far more likely to stay, even though steps 4-12 are still gated behind it.
        # The dropout path is inverse-practice weighted. It does not measure
        # tenure or identify demographic newcomers.
        early = X[:, :3].mean(axis=1)
        low_practice_weight = np.exp(-6.0*X.mean(axis=1))
        t3_frict = 1.0 + (1.0 - dropout_T3)*low_practice_weight
        h = P['drop0']*np.exp(-P['drop_k']*early)*t3_frict + P['churn']
        die = alive & (rng.random(cap) < h*dt)
        alive[die]=False; X[die]=0.0
        # Closure is evaluated before the arrival draw. Once the last living
        # member exits, there is no continuing group for an exogenous referral
        # to enter; N=0 is therefore permanently absorbing.
        if alive.sum() == 0:
            time_weeks = (step + 1) * dt
            if first_nonviable_week is None:
                first_nonviable_week = float(time_weeks)
            closure_week = float(time_weeks)
            was_viable = False
            if record:
                history.append(snapshot(time_weeks))
            break
        # ---- inflow: attraction (T11) through members carrying the message (T3 opens the door)
        # Inflow = exogenous referral floor + attraction. Arrival does not
        # depend on the group's welcome; staying does (Tradition 3 -> retention).
        att = X[alive,11].sum() if alive.sum() else 0.0
        lam = P['lam_exog'] + P['lam0']*att*attraction_T11
        if arrival_T3 is not None:
            lam *= float(arrival_T3)
        k = rng.poisson(max(lam*dt,0))
        free = np.where(~alive)[0][:k]
        alive[free]=True; X[free]=0.02
        het[free]=mean_one_lognormal(rng, P['het_sd'], len(free))

        time_weeks = (step + 1) * dt
        n_after = int(alive.sum())
        viable = n_after > viability_threshold
        if was_viable and not viable and first_nonviable_week is None:
            first_nonviable_week = float(time_weeks)
        if first_nonviable_week is not None and not was_viable and viable and first_recovery_week is None:
            first_recovery_week = float(time_weeks)
        if n_after == 0 and closure_week is None:
            closure_week = float(time_weeks)
        was_viable = viable
        if record:
            history.append(snapshot(time_weeks))
    n=alive.sum()
    lv = X[alive].mean(axis=1) if n else np.array([])
    est = lv > P['act_thr'] if n else np.array([],bool)
    out = dict(N=int(n), mean=float(lv.mean()) if n else 0.0,
               n_est=int(est.sum()) if n else 0,
               est_mean=float(lv[est].mean()) if n and est.sum() else 0.0,
               newcomer_frac = float((lv<=P['act_thr']).mean()) if n else 0.0,
               output = float(lv.sum()) if n else 0.0,
               endpoint_exists=bool(n > 0),
               endpoint_viable=bool(n > viability_threshold),
               viability_threshold=int(viability_threshold),
               first_nonviable_week=first_nonviable_week,
               first_recovery_week=first_recovery_week,
               recovered_after_first_crossing=bool(first_recovery_week is not None),
               closure_week=closure_week,
               closed=bool(n == 0),
               X=X, alive=alive)
    if record:
        fields = list(history[0]) if history else [
            'time_weeks', 'N', 'all_member_practice', 'established_count',
            'established_practice', 'experienced_count', 'low_practice_fraction']
        out['history_fields'] = fields
        out['history'] = {field: np.array([row[field] for row in history]) for field in fields}
        out['hist'] = np.column_stack([out['history'][field] for field in fields])
    return out

FULL = np.ones(12)
if __name__ == "__main__":
    r = simulate(FULL)
    print("full Tradition adherence ->", {k:round(v,3) for k,v in r.items() if k in ('N','mean','newcomer_frac','output')})
