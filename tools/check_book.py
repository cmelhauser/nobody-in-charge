#!/usr/bin/env python3
"""Book-level coherence checks. Run from the repo root:

    python3 tools/check_book.py

`check_chapter.py` checks one file against the house style. It cannot see anything that
lives between files, and every error found on 2 August 2026 lived between files. This
checks the seven things that went wrong, so they fail loudly next time.

    1  figures       every decimal in a chapter traceable to the notebook, model, or cache
    2  intervals     simulation figures carry a sample size and an interval
    3  repetition    shared phrasing across every pair of chapters, main text only
    4  forward       cross-references that point at undrafted chapters
    5  status        the same quantity stated differently in different files
    6  history       claims about the project's past that the progress log does not support
    7  sources       citations attributing content to a saved source that lacks it

Exit code 1 if any FAIL. Warnings do not fail.
"""
import re, os, sys, json, glob, hashlib, itertools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def P(*a): return os.path.join(ROOT, *a)

FAILS, WARNS, NOTES = [], [], []
def fail(sec, msg): FAILS.append((sec, msg))
def warn(sec, msg): WARNS.append((sec, msg))
def note(sec, msg): NOTES.append((sec, msg))

CHAPTERS = sorted(glob.glob(P('manuscript', 'ch*.md')))


def body(path, main_only=True):
    t = open(path).read()
    if main_only:
        i = t.find('## The Machinery')
        if i > 0: t = t[:i]
    return t


def words(path, main_only=True):
    t = re.sub(r'`[^`]*`', ' ', body(path, main_only))
    return re.sub(r'[^a-z ]', ' ', t.lower()).split()


def grams(w, n):
    return set(tuple(w[i:i + n]) for i in range(len(w) - n + 1))


# --- 1. every decimal in a chapter must be traceable to a computational source --------
def check_figures():
    nbp = P('model', 'book-calculations.ipynb')
    if not os.path.exists(nbp):
        fail('figures', 'notebook not found'); return
    nb = json.load(open(nbp))
    blob = []
    for c in nb['cells']:
        if c['cell_type'] != 'code': continue
        blob.append(''.join(c['source']))
        for o in c.get('outputs', []):
            blob.append(''.join(o.get('text', [])))
    # The released notebooks are compact verification artifacts rather than duplicated raw
    # result stores. Cache and model source are therefore part of the traceability corpus.
    # Cache identity/completeness is checked independently by tools/check_release.py.
    blob.append(open(P('model', 'aa_group_model.py')).read())
    for cache in glob.glob(P('research', '*.json')):
        if os.path.basename(cache) in {'audit-pre-correction-manifest.json',
                                       'kurtz-1991-verification-index.json'}:
            continue
        blob.append(open(cache).read())
    B = '\n'.join(blob)
    # roundings of an asserted value are acceptable; flag only what cannot be reached
    def reachable(n):
        if n in B: return True
        try: v = float(n)
        except ValueError: return True
        d = len(n.split('.')[1])
        for cand in re.findall(r'\d+\.\d+', B):
            try:
                if round(float(cand), d) == v: return True
            except ValueError: pass
        return False
    # Strip identifiers before looking for figures. A DOI, an ISBN or a journal volume
    # is not a computed quantity, and flagging one is the checker crying wolf.
    STRIP = re.compile(r'doi:\S+|10\.\d{4,}/\S+|ISBN[\s:0-9X-]+', re.I)
    # A decimal quoted from a historical source is not a model output and has no business
    # in the notebook. Each exemption names the source it came from, so the reader of this
    # file can check it the same way the notebook is checked. Added deliberately, one at a
    # time; do not turn this into a blanket rule for numbers with a citation nearby.
    SOURCE_FIGURES = {
        '14.3': "Jellinek's estimate, via Maxwell 1950: per-capita distilled spirits "
                "consumption, ages 15+, fell 14.3 per cent between 1840 and 1850",
        '4.9':  "the same passage: the 1840 base of 4.9 gallons per capita",
        '0.053': "Carrell, Sacerdote and West (2013): the predicted grade-point gain for "
                 "the bottom third of the academic distribution",
        '0.061': "the same paper: the observed treatment effect on the lowest-ability "
                 "students, negative",
        '0.055': "the same paper: the p-value on that effect",
    }
    bad = [(os.path.basename(p), n) for p in CHAPTERS
           for n in sorted(set(re.findall(r'\d+\.\d+', STRIP.sub(' ', open(p).read()))))
           if n not in SOURCE_FIGURES and not reachable(n)]
    if bad:
        for f, n in bad:
            fail('figures', f'{f}: {n} is not in the notebook, model, or cache, even as a rounding')
    else:
        note('figures', f'all decimals across {len(CHAPTERS)} chapters trace to a computational source')


# --- 2. simulation figures must carry a sample size and an interval --------------------
SIM_OUT = re.compile(r'\b\d{1,4}\s*(?:seeds|runs|replications|draws)\b|Monte Carlo', re.I)
EXACT   = re.compile(r'\bexact\b|closed[- ]form|deterministic|not simulated|\btheorem\b'
                     r'|\barithmetic\b|analytic', re.I)
SIZE    = re.compile(r'\b\d{2,4}\s*(?:seeds|runs|replications|draws)\b'
                     r'|\b(?:ten|thirty|four hundred|two thousand|twenty-five)\s*'
                     r'(?:seeds|runs|replications|draws)\b', re.I)
INTV    = re.compile(r'standard error|interval|\bSE\b|plus or minus|±|\+/-'
                     r'|per cent of draws|confidence|Wilson', re.I)
SMALL   = re.compile(r'\b(?:ten|10|three|3|five|5)\s*seeds\b', re.I)

def check_intervals():
    """A Machinery must not present simulation output without a sample size and an
    interval. A Machinery whose figures are exact says so and is exempt: the point of
    rule 5 is that the two are distinguished, not that everything carries an error bar."""
    for p in CHAPTERS:
        t = open(p).read(); nm = os.path.basename(p)
        i = t.find('## The Machinery')
        mach = t[i:] if i > 0 else ''
        if not mach: continue
        hits = list(SIM_OUT.finditer(mach))
        if not hits: continue                         # no simulation output presented
        # A retrospective mention ("these WERE Monte Carlo, they are now closed-form") is
        # a chapter obeying rule 5, not breaking rule 2. Exempt when exactness is declared
        # in the same breath.
        live = [m for m in hits
                if not EXACT.search(mach[max(0, m.start() - 400):m.start() + 400])]
        if not live: continue
        if not SIZE.search(mach):
            fail('intervals', f'{nm}: presents simulation output with no sample size')
        if not INTV.search(mach):
            fail('intervals', f'{nm}: presents simulation output with no interval or error')
        for m in SMALL.finditer(mach):
            ctx = mach[max(0, m.start() - 160):m.start() + 160]
            # Added 2 August 2026 for Chapter 23, which is a list of corrections and so
            # names superseded sample sizes throughout. "quoted ... from ten seeds" and
            # "found by" are retrospective constructions; the check is for a chapter still
            # RELYING on a small sample, not one confessing to having done so.
            if not re.search(r'was wrong|until|recomputed|previously|earlier|old |had been'
                             r'|quoted .{0,60}from|found by|error|superseded|no longer'
                             r'|recomput\w*|replications',
                             ctx, re.I):
                fail('intervals', f'{nm}: quotes "{m.group(0)}" as a live figure; minimum is 400')


# --- 3. repetition across every pair of chapters ---------------------------------------
# Quotations and the statement of the theorem are supposed to recur. Anything else is not.
ALLOWED = [
    'sheer survival value', 'relied upon to be right', 'as it grows if and only',
    'fixed share of the group', 'quarterly journal of studies on alcohol',
    'most famous reformed drunkard in america', 'three of them turn out to be the',
    'alcoholics anonymous has around two million members',
    'all present what is missing is invisible', 'he has twenty two years he was',
    # The short text of Tradition 3, quoted in Chapters 2 and 19 for different purposes.
    # Quoting a source in two chapters is not duplication of prose. Added 2 August 2026.
    'membership is a desire',
]
def check_repetition():
    W = {p: words(p) for p in CHAPTERS}
    total, flagged = 0, 0
    for a, b in itertools.combinations(CHAPTERS, 2):
        sh = grams(W[a], 8) & grams(W[b], 8)
        total += len(sh)
        for s in sh:
            j = ' '.join(s)
            if not any(x in j for x in ALLOWED):
                flagged += 1
                warn('repetition', f'{os.path.basename(a)[:6]} / {os.path.basename(b)[:6]}: "{j}"')
    note('repetition', f'{total} shared 8-grams across all pairs, {flagged} not on the allow-list')


# --- 4. forward references into undrafted chapters -------------------------------------
NUM = {w: i for i, w in enumerate(
    'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen '
    'Fifteen Sixteen Seventeen Eighteen Nineteen Twenty'.split())}
NUM.update({'Twenty-One': 21, 'Twenty-Two': 22, 'Twenty-Three': 23, 'Twenty-Four': 24,
            'Twenty-Five': 25})

def check_forward():
    drafted = {0} | {int(re.search(r'ch(\d+)', os.path.basename(p)).group(1)) for p in CHAPTERS}
    for p in CHAPTERS:
        t = open(p).read()
        refs = set()
        for m in re.finditer(r'Chapters? ([A-Z][a-z]+(?:-[A-Z][a-z]+)?)'
                             r'(?: (?:to|through|and) ([A-Z][a-z]+))?', t):
            for g in m.groups():
                if g in NUM: refs.add(NUM[g])
        fwd = sorted(r for r in refs if r not in drafted)
        if fwd:
            warn('forward', f'{os.path.basename(p)} points at undrafted {fwd}; '
                            'fine if deliberate, but it is an obligation')
    if not [w for w in WARNS if w[0] == 'forward']:
        note('forward', 'no chapter references an undrafted chapter')


# --- 5. the same quantity stated differently in different files ------------------------
def check_status():
    def read(p): return open(P(p)).read() if os.path.exists(P(p)) else ''
    readme = read('README.md')
    nbp = P('model', 'book-calculations.ipynb')
    if os.path.exists(nbp):
        nb = json.load(open(nbp))
        n = sum(''.join(''.join(o.get('text', [])) for o in c.get('outputs', [])).count('  OK ')
                for c in nb['cells'] if c['cell_type'] == 'code')
        bad = sum(''.join(''.join(o.get('text', [])) for o in c.get('outputs', [])).count('  FAIL')
                  for c in nb['cells'] if c['cell_type'] == 'code')
        # A cell can carry an outputs entry whose text is the empty string, which is what a
        # cell that raised before printing anything leaves behind if the exception is not
        # stored. `not c.get('outputs')` is true only for a MISSING list, so that case passed
        # silently. On 2 August 2026 cell 4 had been broken that way since before the session
        # began: it referenced an undefined name, produced nothing, and no check saw it.
        # Look at the TEXT, not at the presence of the list.
        def _txt(c): return ''.join(''.join(o.get('text', [])) for o in c.get('outputs', []))
        empty = [i for i, c in enumerate(nb['cells'])
                 if c['cell_type'] == 'code' and c.get('source') and not _txt(c).strip()]
        # And a cell that calls check() must show at least one result line, or it did not run.
        # `def check(` is the setup cell defining the helper, not a cell using it.
        def _calls_check(c):
            s = re.sub(r'def check\(', '', ''.join(c['source']))
            return bool(re.search(r'(?<![\w.])check\(', s))
        silent = [i for i, c in enumerate(nb['cells'])
                  if c['cell_type'] == 'code' and _calls_check(c)
                  and '  OK ' not in _txt(c) and '  FAIL' not in _txt(c)]
        if bad: fail('status', f'notebook has {bad} stored assertion failures')
        if empty: fail('status', f'notebook code cells with blank output: {empty}')
        if silent: fail('status', f'notebook cells call check() but stored no result: {silent}')
        m = re.search(r'makes (\d+) assertions', readme)
        if m and int(m.group(1)) != n:
            fail('status', f'README says {m.group(1)} assertions, notebook stores {n}')
        else:
            note('status', f'notebook: {n} assertions stored, {bad} failures')
    wc = sum(len(open(p).read().split()) for p in CHAPTERS)
    m = re.search(r'about ([\d,]+) words', readme)
    if m:
        stated = int(m.group(1).replace(',', ''))
        if abs(stated - wc) > 1500:
            fail('status', f'README says ~{stated:,} words, chapters total {wc:,}')
        else:
            note('status', f'{len(CHAPTERS)} chapter files, {wc:,} words, README agrees')
    m = re.search(r'plus (\d+) of 25 chapters', readme)
    if m and int(m.group(1)) != len(CHAPTERS) - 1:
        fail('status', f'README says {m.group(1)} chapters, {len(CHAPTERS)-1} exist besides the preface')


# --- 6. claims about the project's own past ---------------------------------------------
# Widened 2 August 2026: I wrote "for two months of work" into CLAUDE.md while documenting
# this very rule, and the old pattern did not catch it because it only matched a bare "for
# months". Numbered durations count.
HIST = re.compile(r'for months|for years|for several sessions|had survived several'
                  r'|has been (?:true|wrong) for|months later, '
                  r'|for (?:\w+|\d+) (?:days|weeks|months|years) of work'
                  r'|for (?:two|three|four|five|six|several|many|\d+) (?:days|weeks|months|years)',
                  re.I)
def check_history():
    log = open(P('research', 'progress-log.md')).read() if os.path.exists(P('research', 'progress-log.md')) else ''
    dated = bool(re.search(r'\b20\d\d\b', log))
    # Widened 16 August 2026. The rule is about claims regarding THIS PROJECT's history, and
    # the four files below are exactly where such a claim would live, but they were not being
    # scanned: HANDOFF.md and BOOK-PLAN.md narrate the project's own course, and AGENTS.md and
    # AGENT_VERIFY.md instruct an agent about it. All four were clean when added, so this
    # closes a gap rather than papering over a finding. Chapters stay out on purpose: their
    # durations are sourced history about the Washingtonians and AA, or model output, neither
    # of which the progress log is the authority for.
    # Widened again 18 August 2026 for CHANGELOG.md and RELEASING.md. A changelog is a
    # narration of this project's own history and is the most likely place for an
    # unsupportable duration claim to appear next; RELEASING.md explains why the version is
    # what it is, which is the same kind of statement. Both were clean when added.
    targets = [P('CLAUDE.md'), P('README.md'), P('appendix', 'APPENDIX.md'),
               P('research', 'PARAMETERS.md'), P('HANDOFF.md'), P('AGENTS.md'),
               P('AGENT_VERIFY.md'), P('BOOK-PLAN.md'), P('CHANGELOG.md'),
               P('RELEASING.md')] + glob.glob(P('plans', '*.md'))
    for p in targets:
        if not os.path.exists(p): continue
        for ln, line in enumerate(open(p).read().split('\n'), 1):
            if not HIST.search(line): continue
            if '"' in line or line.lstrip().startswith('- '): continue   # quoted example
            if re.search(r'if you are about to say|The rule:|grep research', line, re.I):
                continue                                                  # the rule itself
            if re.search(r'cannot be supported|was written by me|do not say it'
                         r'|unverifiable|no dates', line, re.I): continue
            # The rule is about claims regarding THIS PROJECT's history, which the undated
            # progress log cannot support. A duration inside the simulated world is a model
            # output with a notebook assertion behind it and is checkable in the ordinary
            # way. Added 2 August 2026 when PART-5-PLAN.md said a starved group "looks
            # completely healthy for years", which is notebook section 14 and not a claim
            # about the project at all.
            # NOTE the first attempt at this exemption keyed on words like "group" and
            # "member" and would have silenced the check across most of the plans. It was
            # narrowed to markers that only appear when the sentence is about the runs, and
            # regression-tested by reinserting a genuine project-history duration claim,
            # which it still catches. Do not widen it.
            if re.search(r'\b(simulat\w*|seeds?|horizon|notebook|runs?|trajector\w*|'
                         r'model says|in the model|per cent of draws)\b', line, re.I): continue
            fail('history', f'{os.path.relpath(p, ROOT)}:{ln} claims a duration; '
                            'the progress log is undated, so this cannot be checked')
    if not dated:
        warn('history', 'research/progress-log.md carries no dates, so no duration claim '
                        'anywhere in the project is verifiable')
    if not [f for f in FAILS if f[0] == 'history']:
        note('history', 'no unverifiable duration claims in the instructions or plans')


# --- 7. citations against saved sources -------------------------------------------------
# For every source saved as full text in the active research root or research/incorporated/,
# check that chapters citing it for a subject actually could have got that subject from it.
# Deliberately exclude research/staged/: physical presence there is not incorporation.
SAVED = {
    'marsh-1866':    'Marsh',
    'krout-1925':    'Krout',
    'gough-1869':    'Gough',
    'eddy-1887':     'Eddy',
    'crothers-1911': 'Crothers',
    'harrison-1860': 'Harrison',
    'hawkins-1862':  'Hawkins',
    'blair-1888':    'Blair',
    'fehlandt-1904': 'Fehlandt',
    'fatimah-2025':  'Fatimah',
    'grosh-1842':    'Grosh',
    'maxwell-1950':  'Maxwell',
}
# Kurtz is added at run time from its verification index; see check_sources().
SUBJECTS = ['sons of temperance', 'mitchell', 'beecher', 'washingtonian',
            'maudlin', 'hypocrites', 'moral suasion',
            'double-well', 'steepness', 'timeline followback',
            # Added when Grosh 1842 was catalogued. Kept specific rather than generic:
            # a subject like "sectarian" appears near several source names and would
            # manufacture pairs the check cannot adjudicate.
            'pocket companion', 'publicity and freedom', 'utica', 'reformed inebriates',
            # Added when Maxwell 1950 was catalogued, 2 August 2026. The book's most-cited
            # source and, until then, the only one no citation could be checked against.
            'sheer survival value', 'jellinek', 'annapolis', 'chase', 'zug', 'vickers',
            # Added 10 August 2026 with the three copyrighted works catalogued that day:
            # the Twelve and Twelve, Rohr (2011) and the Kurtz talk. Each phrase was checked
            # to be literally present in exactly one of the three and absent from the other
            # two, so a citation-subject pair here discriminates between them rather than
            # passing on any of the three indifferently.
            # "rotating leadership" was tried here and removed the same day. It is the
            # book's own vocabulary as well as the Twelve and Twelve's, so it appears in
            # chapters that are not citing that source, and the first run paired it with
            # Gough in Chapter 2. That is the manufactured pair the note above warns
            # against, so the subject goes rather than the checker being loosened.
            'elder statesmen', 'bleeding deacon', 'entrenched power',
            'total disclosure', 'mental reservation', 'communion of saints']

def fuzzy_in(term, blob, thresh=0.72):
    """Is `term` present allowing OCR noise? Slides a window and scores position-wise
    character agreement. Needed because these are 1880s scans: Eddy renders Mitchell as
    Mitrhell, Mituhell and MitrLell on the same page."""
    term = term.lower(); L = len(term)
    if term in blob: return True
    first = term[0]
    start = 0
    while True:
        k = blob.find(first, start)
        if k < 0 or k + L > len(blob): return False
        w = blob[k:k + L]
        # Both are exactly L; the guard above rejects a short tail.
        if sum(a == b for a, b in zip(w, term, strict=True)) / L >= thresh: return True
        start = k + 1

def window(seg, name, texts, sentences=2):
    """The span in which a source name is taken to be doing the citing.

    Originally this was a flat 400 characters on the same line, which is too coarse.
    Two false positives on 2 August 2026 came from it and neither was a misattribution:
    a references list where Krout's entry adjoined a mention of the Pocket Companion,
    and a passage where Grosh is discussed in one sentence and Blair quoted in the next.
    A citation belongs to the nearest preceding source name and rarely runs past the
    sentence after it, so the window now ends at whichever comes first: the start of
    another saved source's name, or the end of the second sentence.
    """
    body = seg[len(name):]
    cut = len(body)
    for other in texts:
        if other == name: continue
        k = body.find(other)
        if 0 <= k < cut: cut = k
    ends = [m.end() for m in re.finditer(r'[.!?]["\u2019\')]*\s', body[:cut])]
    if len(ends) >= sentences: cut = min(cut, ends[sentences - 1])
    return (name + body[:cut]).lower()


def check_sources():
    texts = {}
    # No source document is committed. Every source carries a vocabulary-only verification
    # index instead, which is enough to confirm that a cited subject appears in the work and
    # is not a redistributable copy. That pattern started with Kurtz (1991), which is in
    # copyright, and now covers the whole corpus; see research/SOURCES.md and .gitignore.
    # Indexes are found by directory name so a source is identified the same way whether or
    # not its document happens to be present in a given working copy.
    # A vocabulary set has no word order, so a phrase cannot be confirmed from it. Each index
    # therefore also records which registered subjects the real document contains, decided
    # against the text when the index was built and stamped with that file's SHA-256.
    subjects_present = {}
    # A source is identified in prose by the leading token of its directory name, so that
    # token has to be distinctive. "AA" is not: it appears on nearly every page of a book
    # about Alcoholics Anonymous, and a two-letter name manufactures thousands of spurious
    # citation-subject pairs. Corpus directories therefore use a distinguishing name
    # (Grapevine_1946, BigBook_1939, AAWS_2024_P17). Three characters is the floor: "ATU"
    # is distinctive and appears only as that abbreviation, while "AA" is not and is
    # refused here rather than silently trusted.
    def source_name(path):
        token = os.path.basename(os.path.dirname(path)).split('_')[0]
        return token if len(token) >= 3 else None

    for f in glob.glob(P('research', '**', '*_verification-index.json'), recursive=True):
        d = json.load(open(f))
        name = source_name(f)
        if name is None:
            warn('sources', f'corpus directory name is too short to identify citations: {f}')
            continue
        texts[name] = ' ' + ' '.join(d['vocab']) + ' '
        if 'subjects_present' in d:
            subjects_present[name] = set(d['subjects_present'])
    for f in glob.glob(P('research', '*-verification-index.json')):
        d = json.load(open(f))
        name = re.match(r'([A-Z][a-z]+)', d['work']).group(1)
        texts.setdefault(name, ' ' + ' '.join(d['vocab']) + ' ')
    # A working copy that still has the documents gets the stronger check for free: full
    # text beats a vocabulary set, because it preserves word order. Documents are found by
    # directory name under the normalized layout, and by legacy stem for older checkouts.
    full_text = set()
    for d in sorted(glob.glob(P('research', 'incorporated', '*'))):
        token = os.path.basename(d).split('_')[0]
        name = token if len(token) >= 3 else None
        doc = os.path.join(d, os.path.basename(d) + '.txt')
        if name and os.path.exists(doc):
            texts[name] = re.sub(r'\s+', ' ', open(doc, errors='ignore').read()).lower()
            full_text.add(name)
    for stem, name in SAVED.items():
        hits = (glob.glob(P('research', stem + '*.txt')) +
                glob.glob(P('research', 'incorporated', '**', stem + '*.txt'), recursive=True))
        if hits:
            texts[name] = re.sub(r'\s+', ' ', open(hits[0], errors='ignore').read()).lower()
            full_text.add(name)
    if not texts:
        warn('sources', 'no full-text sources found in research/'); return
    checked = 0
    for p in CHAPTERS:
        t = open(p).read(); nm = os.path.basename(p)
        for name, blob in texts.items():
            for m in re.finditer(re.escape(name) + r'[^\n]{0,400}', t):
                seg = window(m.group(0), name, texts)
                # A note recording that a source does NOT contain something is the
                # correction, not the error. Do not flag the fix as the bug.
                # "the sources checker" only appears when a chapter is recording that this
                # very check caught a misattribution. Added 2 August 2026 for Chapter 23's
                # table of corrections, where the row naming the error has no room for the
                # word "misattribution" that exempts the prose version.
                if re.search(r'does not (?:mention|contain)|not mention|misattribut'
                             r'|no mention of|is not in|corrected here|sources check', seg):
                    continue
                for subj in SUBJECTS:
                    if subj in seg:
                        checked += 1
                        # Prefer the document when this working copy has it, because word
                        # order survives there. Otherwise use the phrase decision recorded in
                        # the verification index, which was made against the document.
                        if name in full_text:
                            ok = fuzzy_in(subj, blob)
                        elif name in subjects_present:
                            ok = subj in subjects_present[name]
                        else:
                            ok = fuzzy_in(subj, blob)
                        if not ok:
                            fail('sources', f'{nm}: cites {name} for "{subj}" but the recorded '
                                            f'content of {name} does not contain it in any spelling')
    if not [f for f in FAILS if f[0] == 'sources']:
        note('sources', f'{checked} citation-subject pairs checked against '
                        f'{len(texts)} saved sources, all supported')


# Names this project has undertaken not to print, stored as SHA-256 of the lowercased
# form so that enforcing the rule does not require writing the name in the repository.
#
# There is one entry. The founder of the organization Recovery Dharma split from in 2019
# is named in `RecoveryDharma_2023` in connection with its collapse, and the project's
# rule, in CLAUDE.md and in that source's own metadata, is that he is named nowhere here.
# The structural claim, that the predecessor was organized around a founding teacher and
# the successor abolished the office, does not need the name, and this project cannot
# adjudicate an allegation about a living person. The appendix named him anyway between
# 16 and 17 August 2026, and it shipped in a rendered PDF before this check existed.
WITHHELD = {
    '56d447a05a7c48cdd011b0485110052b6cf0ecdad090fe4e70d98aae3a8d71be',  # full name
    '4d8d163722179946e84391aa25ab3a73b3a02b3202d0eebd0d0d882e51a1431c',  # surname alone
}


def check_withheld_names():
    """Fail if a name the project has undertaken not to print appears in prose."""
    targets = (glob.glob(P('manuscript', '*.md')) + glob.glob(P('reference', '*.md'))
               + glob.glob(P('plans', '*.md'))
               + [P('appendix', 'APPENDIX.md'), P('README.md'), P('HANDOFF.md'),
                  P('CLAUDE.md'), P('AGENTS.md'), P('AGENT_VERIFY.md'),
                  P('paper', 'anonymity-as-an-aggregation-condition.tex')])
    hits = 0
    for path in targets:
        if not os.path.exists(path):
            continue
        text = open(path, encoding='utf-8', errors='ignore').read()
        words = re.findall(r"[A-Za-z][A-Za-z'-]+", text)
        grams = [w.lower() for w in words]
        # Deliberately ragged: the second iterable is one shorter, which is the point
        # of a bigram. strict would raise on every call.
        grams += [f'{a.lower()} {b.lower()}'
                  for a, b in zip(words, words[1:], strict=False)]
        for g in set(grams):
            if hashlib.sha256(g.encode()).hexdigest() in WITHHELD:
                hits += 1
                fail('names', f'{os.path.basename(path)}: prints a name the project '
                              f'has undertaken to withhold')
                break
    if not hits:
        note('names', 'no withheld name appears in the manuscript, appendix, primer or paper')


if __name__ == '__main__':
    for fn in (check_figures, check_intervals, check_repetition, check_forward,
               check_status, check_history, check_sources,
               check_withheld_names):
        try:
            fn()
        except Exception as e:
            fail(fn.__name__, f'check itself failed: {type(e).__name__}: {e}')
    for sec, msg in NOTES: print(f'  ok    {sec:<11}{msg}')
    for sec, msg in WARNS: print(f'  warn  {sec:<11}{msg}')
    for sec, msg in FAILS: print(f'  FAIL  {sec:<11}{msg}')
    print(f'\n{len(FAILS)} failures, {len(WARNS)} warnings')
    print('book-level checks clear' if not FAILS else 'fix the FAILs')
    sys.exit(1 if FAILS else 0)
