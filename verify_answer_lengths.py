#!/usr/bin/env python3
"""MRB-297 · The OTHER answer tell: option LENGTH.

`verify_answer_positions.py` (MRB-278) watches WHERE the correct answer sits.
Nothing watched HOW LONG it is, and the KS3 physics audit of 28 Aug 2026
measured what that cost: across the 840 authored physics bank questions, a
student who ignored the physics entirely and always picked the longest option
scored **35.1%** against 25% by chance — **56.2% in P11**. The same tell sat in
the lesson hooks, which are live on pages today, more heavily than in the bank.

── WHAT IS MEASURED, AND WHY IT IS NOT "IS THE CORRECT ONE THE LONGEST" ──

The obvious test — "is the correct option the longest string" — is the wrong
one, in both directions:

  · It fires on a one-character difference. A correct answer 63 characters
    long beside a distractor of 61 is not a tell; no child sees it. Counting
    those inflates the finding and, worse, invites a fix of ONE PADDING
    CHARACTER that moves the number without changing anything a student sees.
  · It cannot say how big the giveaway actually is, because it says nothing
    about the questions where no option stands out at all.

So this gate measures **the exploit, not the property**. For each set of
options it asks: is there an option that is longest by a CLEAR margin —
`MARGIN` characters or more clear of the runner-up? If there is not, a
length-guessing student has nothing to go on and the set is skipped. If there
is, the set counts, and the gate records whether that visibly-longest option
was the correct one.

The resulting number is exactly the thing the audit reported and the thing a
student could exploit: **when the shape of the options tells you something, how
often is what it tells you right?** Chance is 25%.

── THE THREE CORPORA ────────────────────────────────────────────────────

All three are AUTHORED and served verbatim (`build_ks3.py` emits options in
authored order — the MRB-278 ruling), so measuring the source measures what a
student receives.

  · `bank`   — `ks3_data/<unit>/questions_*.py`, the pool a weekly assignment
               draws from (`ks3_assignment_bank`). NOT live for physics: 0
               rows on production as of 31 Aug 2026, which is why the physics
               tell had to be fixed BEFORE the export, not after.
               ⊕ CORRECTED 1 Sep 2026: physics was NOT 0 rows. It had been
               exported on 30 Aug at 23:36 UTC, carrying the full 43.9%
               giveaway, and was live to students for two days. The pools were
               repaired on 1 Sep and re-verified row by row against source.
  · `ladder` — the four rungs baked into every lesson page. LIVE.
  · `hook`   — `phenomenon.options` on the lesson dict. LIVE. Carries an
               integer `answer` index in `ks3_data` on **70 of 70** physics
               lessons, so none is skipped.
               ⊕ This paragraph used to read "62 of 70 … the 8 that do not
               resolve are all of P1". That was true when this gate was
               written and P1's eight hooks were the estate's only unwatched
               MCQ corpus. They were never unresolvable — every reveal names
               one option — so MRB-297 wrote the index down, and the gate
               went red the same minute: 5 of the 5 hooks with a visible
               margin had the correct answer as the longest option, on eight
               live pages. Fixed. The lesson is that a corpus nothing can
               measure reports no defects, which is not the same as having
               none.

── HOW IT FAILS ─────────────────────────────────────────────────────────

A scope (one corpus, whole or one unit within it) is RED when the rate is both

  · **practically** bad — above `HI` (or below `LO`, see below); and
  · **statistically** real — a one-sided binomial test against p = 0.25
    rejects at `ALPHA`.

Both conditions, deliberately. Significance alone would fail a corpus of 800 on
a five-point drift nobody could exploit; a bare threshold alone would fail a
unit on 3 questions out of 4. A tell has to be both big and real to be a tell.

**The test is two-sided.** A corpus where the correct answer is almost NEVER the
visibly longest is also giving the game away — "never pick the long one" turns a
four-option question into a three-option one, which is worth 8 points. The audit
asked for this explicitly, and it is the failure mode a careless fix of the
first direction produces. `LO` is the floor.

── THE BASELINES, AND WHY THIS GATE IS NOT GREEN BY BEING BLIND ─────────

⚠️ **Biology and chemistry are worse than physics ever was, and they are LIVE.**
Measured 31 Aug 2026 from the same source: the bio/chem bank runs at **52.7%**
(C9 88.2%, C10 85.7%, C7 85.7%, C8 74.1%) and the bio/chem ladder — baked into
lesson pages a student reads today — at **46.5%**. Those 1,380 bank questions
are in `ks3_assignment_bank` on production and are being set as homework now.

That debt is NOT this gate's to fix and NOT this run's to fix: MRB-297 is the
physics lane, and rewriting live chemistry options from a physics branch would
collide with the chemistry remediation lane. So each already-red bio/chem scope
carries a dated `BASELINE` row below, recording the exact (n, k) it was found
at. A baselined scope passes at or below its recorded rate and **fails the
moment it gets worse**.

The rows are written here, in the gate, rather than in a docs file, because a
baseline is a debt and a debt kept in the thing that measures it cannot be
mislaid. Every row is a live defect awaiting its own run. **Deleting a row is
how this debt gets paid; raising one is not a fix.**

⚠️ **KS4 is not watched by this gate.** `all_subtopics_*.py` has a different
option shape and `generate_site_v5.make_new_quiz` reshuffles at build time —
which cures position but does nothing at all for length. Whether KS4 carries the
same tell is UNMEASURED. Recorded here so it is a known gap and not an
assumption.
"""

import collections
import math
import os
import sys

# One option must be this many characters clear of the runner-up before a
# length-guessing student has anything to see. Below it, the set is skipped.
MARGIN = 6

HI = 0.35      # above this, and significant, the long option is a giveaway
LO = 0.12      # below this, and significant, "never pick the long one" is one
ALPHA = 0.01   # one-sided binomial against p = 0.25
CHANCE = 0.25

# ── baselines · measured 31 Aug 2026 · every row is a live defect ────────
# scope key -> (n, k) as found. Passing means "no worse than this".
# See "THE BASELINES" above before touching one.
# ⚠️ ONLY scopes that are RED TODAY get a row. A row on a scope that currently
# passes is not a record of debt — it is permission to decay up to that rate
# later, granted by nobody. Eleven rows; every one is a live defect.
BASELINE = {
    # bio/chem bank — live in ks3_assignment_bank on production, set as
    # homework now. 218 of 414 = the worst corpus in the key stage.
    ("bank", "whole corpus BIO+CHEM"): (414, 218),
    ("bank", "B3"): (22, 12), ("bank", "B5"): (21, 13), ("bank", "B9"): (21, 13),
    ("bank", "C5"): (17, 12), ("bank", "C6"): (26, 17), ("bank", "C7"): (21, 18),
    ("bank", "C8"): (27, 20), ("bank", "C9"): (17, 15), ("bank", "C10"): (28, 24),
    # bio/chem ladder — baked into lesson pages a student reads today
    ("ladder", "whole corpus BIO+CHEM"): (99, 46),
}

PHYS = {"P%d" % i for i in range(1, 13)}
FAIL = []


def binom_tail_ge(k, n, p):
    """P(X >= k) for X ~ Binomial(n, p). Exact; no scipy in this repo."""
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i)
               for i in range(k, n + 1))


def binom_tail_le(k, n, p):
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i)
               for i in range(0, k + 1))


def texts(options):
    """Options are plain strings (hook, some rungs) or dicts with 'text'."""
    out = []
    for o in options:
        out.append(o if isinstance(o, str) else str(o.get("text", "")))
    return out


def visibly_longest(opts):
    """Index of the option longest by MARGIN or more, else None."""
    lens = [len(t) for t in opts]
    if len(lens) < 2:
        return None
    order = sorted(range(len(lens)), key=lambda j: -lens[j])
    if lens[order[0]] - lens[order[1]] < MARGIN:
        return None
    return order[0]


def collect():
    """(corpus, unit, where, n_options, correct_idx, longest_idx) per set."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ks3_data
    import ks3_data.question_bank as qb

    sets = []
    for u in ks3_data.build_units():
        code = u.get("code")
        for l in u.get("lessons", []):
            if not l.get("authored"):
                continue
            for rung, r in (l.get("ladder") or {}).items():
                if not (isinstance(r, dict) and r.get("options")):
                    continue
                a = r.get("answer")
                if not (isinstance(a, int) and 0 <= a < len(r["options"])):
                    continue
                sets.append(("ladder", code, "%s/%s" % (l["slug"], rung),
                             texts(r["options"]), a))
            ph = l.get("phenomenon")
            if isinstance(ph, dict) and ph.get("options"):
                a = ph.get("answer")
                if isinstance(a, int) and 0 <= a < len(ph["options"]):
                    sets.append(("hook", code, l["slug"],
                                 texts(ph["options"]), a))
    for rec in qb.load_bank():
        for q in rec["questions"]:
            ci = [i for i, o in enumerate(q["options"]) if o.get("correct")]
            if len(ci) != 1:
                continue
            sets.append(("bank", rec["unit"], q.get("id"),
                         texts(q["options"]), ci[0]))
    return sets


def verdict(corpus, scope, n, k):
    """(ok, line). Applies HI/LO, ALPHA, and any recorded baseline."""
    if n == 0:
        return True, "%-6s %-24s no set has a visibly longest option" % (
            corpus, scope)
    rate = k / n
    base = BASELINE.get((corpus, scope))
    tag = ""
    hot = ""
    if rate > HI and binom_tail_ge(k, n, CHANCE) < ALPHA:
        hot = "the long option is a giveaway"
    elif rate < LO and binom_tail_le(k, n, CHANCE) < ALPHA:
        hot = "the long option is never right — the mirror tell"
    ok = not hot
    if hot and base:
        bn, bk = base
        if rate <= bk / bn + 1e-9:
            ok = True
            tag = " · BASELINED %.1f%% (31 Aug 2026), not worse — a live defect awaiting its own run" % (
                100.0 * bk / bn)
        else:
            tag = " · WORSE THAN ITS BASELINE %.1f%%" % (100.0 * bk / bn)
    line = "%-6s %-24s %3d set(s), longest-is-correct %3d = %5.1f%%%s%s" % (
        corpus, scope, n, k, 100.0 * rate, (" · " + hot) if hot else "", tag)
    return ok, line


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("verify_answer_lengths — MRB-297 · the option-length tell "
          "(margin %d chars, chance %.0f%%)" % (MARGIN, 100 * CHANCE))

    tally = collections.defaultdict(lambda: [0, 0])   # (corpus, scope)->[n,k]
    for corpus, unit, _where, opts, ans in collect():
        j = visibly_longest(opts)
        if j is None:
            continue
        grp = "PHYSICS" if unit in PHYS else "BIO+CHEM"
        for scope in ("whole corpus %s" % grp, unit):
            tally[(corpus, scope)][0] += 1
            tally[(corpus, scope)][1] += (j == ans)

    for corpus in ("bank", "ladder", "hook"):
        keys = [k for k in tally if k[0] == corpus]
        if not keys:
            continue
        print()

        def sortkey(k):
            s = k[1]
            if s.startswith("whole"):
                return (0, s, 0)
            return (1, s[0], int(s[1:]))
        for key in sorted(keys, key=sortkey):
            n, k = tally[key]
            ok, line = verdict(corpus, key[1], n, k)
            print("  %s %s" % ("✅" if ok else "❌", line))
            if not ok:
                FAIL.append("%s/%s" % (corpus, key[1]))

    print()
    if FAIL:
        print("verify_answer_lengths: ❌ FAIL — %d scope(s): %s"
              % (len(FAIL), ", ".join(FAIL)))
        return 1
    print("verify_answer_lengths: OK — no corpus or unit lets option length "
          "answer the question.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
