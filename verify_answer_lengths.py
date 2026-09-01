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
  · `hook`   — `phenomenon.options` on the lesson dict. Carries an integer
               `answer` index in `ks3_data` on **70 of 70** physics lessons,
               so none is skipped.
               ⚠️ **NOT GRADED, AND THIS GATE USED TO SAY IT WAS.** ⊕ CORRECTED
               1 Sep 2026 by the fourth cold double-check. `r_activity_options`
               in `ks3_art/kit.py` is one line of design law — *"R3: chosen,
               never correct. No data-correct, no green, never disabled."* The
               built markup bears it out: a hook option carries `data-i` and
               `aria-pressed` and nothing else, and the reveal opens the same
               whichever one is pressed. **The `answer` index never reaches the
               page.** It is read by this file and by nothing else in the repo.
               So a hook length tell is not worth marks and cannot be exploited
               for any, and the claim in this run's own commits — "a giveaway
               on eight live pages" — was wrong. It is measured and PRINTED
               here, because a corpus where the right answer systematically
               looks different still teaches a habit that transfers to the
               ladder, which IS graded. It does not gate. ⚠️ If R3 is ever
               reversed (Design's R10, unruled), the hook ships graded and this
               must gate again — see `HOOK_GATES` below.
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

⚠️ **AND NEITHER IS THE BIO/CHEM HOOK CORPUS — 115 sets, 66 of them with a
visibly longest option.** Every biology and chemistry lesson carries
`phenomenon.answer = None`, so nothing here knows which option is right and the
sets cannot be measured. That is a corpus 14 times the size of the P1 one whose
absence this gate was written about. It is now printed at the head of every run
by `report_skipped()` rather than left invisible in the output — measuring it
needs the index authored, which is the bio/chem lane's work, not this gate's.

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

# ── rank baselines · same rule as BASELINE above: only a scope that is RED
# TODAY gets a row, and a row is a debt, not permission to decay.
RANK_BASELINE = {
    # ⚠️ EVERY ROW HERE IS MEASURED AT THIS RUN'S BRANCH POINT, 834624da7 —
    # the state it INHERITED — not at the state it left behind. That is the
    # whole point: a baseline taken after the work would let the work grade
    # itself, and a tell MOVED from one rank to another would pass unnoticed.
    # Measured 1 Sep 2026 by `git archive 834624da7` and re-running this
    # file's own filter over it.
    # ⚠️ NOT `origin/main`, which has moved seven commits ahead with other
    # lanes' biology work (b3-07, b4-03) that this branch does not carry.
    # Baselining against a tree containing changes this run never saw would
    # have failed it for someone else's edits — it did, by one set, before
    # this was caught.
    #
    # bio/chem — untouched by this run, live on production, its own lane's
    # debt. HEAD matches main to within one set in every cell.
    ("bank",   "BIO+CHEM", 0): (338, 218),   # 64.5% at rank 1
    ("bank",   "BIO+CHEM", 1): (338, 32),    #  9.5% at rank 2
    ("bank",   "BIO+CHEM", 2): (338, 8),     #  2.4% at rank 3
    ("ladder", "BIO+CHEM", 0): (68, 46),     # 67.6% at rank 1
    ("ladder", "BIO+CHEM", 2): (68, 1),      #  1.5% at rank 3
    #
    # physics — the depleted middle ranks are inherited, not made here.
    ("bank",   "PHYSICS", 2): (365, 15),     #  4.1% at rank 3 on main
    ("ladder", "PHYSICS", 2): (77, 3),       #  3.9% at rank 3 on main
    #
    # ⚠️ NO ROW FOR PHYSICS RANK 2, IN EITHER CORPUS, DELIBERATELY. Main had
    # bank 27.7% and ladder 33.8%; this run pushed them to 35.8% and 38.9% by
    # lengthening distractors past correct answers, which is a REGRESSION and
    # is fixed rather than recorded. Rank 1 is where the work went and it
    # shows: physics bank rank 1 went 52.3% -> 24.7% and the whole physics
    # bank distribution's chi-square fell from 186 to 37.
    #
    # ⊕ CORRECTED 1 Sep 2026 — "IS FIXED" WAS NOT TRUE, AND THIS COMMENT IS
    # THE REASON THE GATE STAYED GREEN OVER IT. Nine sets were moved and the
    # single-margin figures came down to 34.6% and 34.3% — which passes only
    # because `HI` is 0.35. A fourth cold reviewer re-measured at every margin
    # and found the physics bank's rank 2 fires this gate's OWN giveaway rule
    # at margins 7, 8, 9 and 10. The gate was green in a two-value window and
    # red on either side of it, which is not a measurement, it is a coincidence
    # with a constant.
    #
    # ⚠️ SO THE SINGLE-MARGIN RANK CHECK BELOW NO LONGER GATES ANYTHING ON ITS
    # OWN. It prints, because the table is readable. Two measures gate now, and
    # neither can be tuned by choosing a threshold:
    #
    #   `RANK_ALL_BASELINE`  the rank distribution over EVERY set, no margin
    #                        filter at all. The denominator is the whole corpus
    #                        — 840 physics bank questions, always — so it
    #                        cannot be moved by edits that push sets in or out
    #                        of a filtered pool, which is exactly what made the
    #                        earlier before/after comparisons unreadable.
    #   `SWEEP_BASELINE`     the WORST rate at any rank at any margin from 3 to
    #                        10. If a fix only works at one margin, this sees it.
}

# ── the two measures that actually gate · added 1 Sep 2026 ──────────────
#
# ⚠️ READ THIS BEFORE TOUCHING EITHER TABLE. Both are measured at this run's
# branch point, `834624da7` — the state the branch INHERITED — by `git archive`
# and re-running this file's own functions over the extracted tree. A baseline
# taken after the work would let the work grade itself.

# 1 · THE RANK DISTRIBUTION OVER EVERY SET, WITH NO MARGIN FILTER.
#
# The filtered measure has a moving denominator: an edit that changes any
# option's length can push a whole set into or out of the measured pool, so a
# rate can rise while the number of exploitable questions falls, and fall while
# it rises. Both happened in this run and both were misread. Over the whole
# corpus the denominator is fixed — 840 physics bank questions, 140 physics
# ladder rungs, every time — so a change in the rate is a change in the thing.
#
# Chance is 25% at every rank. Rows only for scopes that are RED TODAY at the
# branch point; a row is a debt, never permission to decay.
RANK_ALL_BASELINE = {
    # bio/chem — untouched by this run, live on production, its own lane's debt
    ("bank",   "BIO+CHEM", 0): (1380, 493),   # 35.7% at rank 1
    ("ladder", "BIO+CHEM", 0): (230, 101),    # 43.9% at rank 1
    # physics bank — the tell the audit found, at the state it was found in
    ("bank",   "PHYSICS", 0): (840, 317),     # 37.7% at rank 1
    # physics ladder rank 3 — inherited, not made here
    ("ladder", "PHYSICS", 2): (140, 15),      # 10.7% at rank 3, the mirror
    # physics hooks — NOT GATED (see HOOK_GATES); rows kept so the printed
    # line can say what it inherited rather than only what it is
    ("hook", "PHYSICS", 0): (62, 31),         # 50.0% at rank 1
    ("hook", "PHYSICS", 1): (62, 25),         # 40.3% at rank 2
    ("hook", "PHYSICS", 2): (62, 5),          #  8.1% at rank 3, mirror
    ("hook", "PHYSICS", 3): (62, 1),          #  1.6% at rank 4, mirror
}

# 2 · THE WORST RATE AT EACH RANK AT ANY MARGIN FROM 3 TO 10.
#
# `MARGIN` is a judgement about what a reader can see, and a fix aimed at one
# value of it is a fix aimed at a constant. Sweeping is the answer: whatever a
# student's threshold of perception actually is, it is somewhere in 3..10, and
# the gate holds the worst case across all of them.
#
# ⚠️ ⊕ REWRITTEN 1 Sep 2026 BY THE FIFTH COLD DOUBLE-CHECK, WHICH FOUND THREE
# FAULTS IN THE FIRST VERSION, EACH OF WHICH HID A REAL REGRESSION.
#
#   1. IT WAS KEYED BY SCOPE, NOT BY RANK, and so compared magnitudes across
#      different exploits. The physics bank printed "rank 4 at margin 10:
#      43.8% GIVEAWAY BASELINED 53.4%" — and that 53.4% is RANK 1 at margin 7.
#      "Pick the shortest" had gone 21.3% -> 43.8% (p = 5e-6) and was passing
#      against a baseline for a different strategy entirely. The tell had been
#      INVERTED, not removed, and one rank-blind scalar hid it. Keyed by rank
#      now, so a baseline can only ever excuse the thing it measured.
#   2. IT TOOK THE MAXIMUM, so `_hot()` could only ever return "GIVEAWAY" —
#      the largest of four rates is >= 25% by construction. The MIRROR half of
#      the check was unreachable from here. It now walks every cell.
#   3. ⚠️ AND IT CARRIED A ROW FOR A SCOPE THAT WAS NEVER RED. `("ladder",
#      "PHYSICS"): 0.348` was taken from the branch point's worst CELL without
#      checking whether that cell was red, and 34.78% is below `HI` — so it
#      was not. Re-measured at 834624da7: the physics ladder was red at NO
#      margin and NO rank. That row was the only thing holding this gate green
#      over a "pick the second-longest" tell this run's own edits created, and
#      it broke the rule written a few lines above it in this same file.
#      **A baseline is now derived only from cells that were actually red**,
#      and this table is what that produces.
SWEEP_BASELINE = {
    # (corpus, group, rank) -> worst rate at that rank across margins 3..10,
    # AT THE BRANCH POINT, and only where that cell was RED there.
    # GIVEAWAY rows — the rate is too HIGH, so "no worse" means "not above".
    ("bank",   "BIO+CHEM", 0): 0.6915,   # margin 8, 139/201
    ("bank",   "PHYSICS",  0): 0.5340,   # margin 7, 173/324
    ("ladder", "BIO+CHEM", 0): 0.8095,   # margin 10, 34/42
    ("hook",   "PHYSICS",  0): 0.6471,   # margin 6, 22/34 — not gated
    # MIRROR rows — the rate is too LOW, so "no worse" means "not below".
    ("bank",   "BIO+CHEM", 1): 0.0647,   # margin 8, 13/201
    ("bank",   "BIO+CHEM", 2): 0.0000,   # margin 8, 0/201
    ("bank",   "PHYSICS",  2): 0.0085,   # margin 10, 2/235
    ("ladder", "BIO+CHEM", 1): 0.0476,   # margin 10, 2/42
    ("ladder", "BIO+CHEM", 2): 0.0000,   # margin 8, 0/54
    ("ladder", "PHYSICS",  2): 0.0145,   # margin 9, 1/69
    ("hook",   "PHYSICS",  2): 0.0000,   # margin 5, 0/41 — not gated
    ("hook",   "PHYSICS",  3): 0.0000,   # margin 10, 0/26 — not gated
}
# ⚠️ NO ROW FOR ("ladder", "PHYSICS", 1), DELIBERATELY. The physics ladder's
# rank 2 was not red at the branch point at any margin. If it is red now, that
# is this run's doing and this run's to fix, not to excuse.
SWEEP_MARGINS = range(3, 11)

# ⚠️ THE HOOK CORPUS IS MEASURED AND PRINTED BUT DOES NOT GATE, because it is
# not graded — see the docstring. Flip this to True the day design law R3 is
# reversed and a hook option starts carrying a correctness marker; the
# baselines above are already recorded for that day.
HOOK_GATES = False

# ── PROVED TO FIRE, 1 Sep 2026 ──────────────────────────────────────────
# A gate that has never gone red for a reason is a gate nobody has tested.
# Each check below was run against `collect()`'s real output with one defect
# injected, and each caught the defect it exists for:
#
#   M1  90 physics bank answers pushed from rank 1 to rank 2 by lengthening
#       the runner-up past the correct option — the EXACT edit this run made
#       nine times. Distribution 268/249/148/175 -> 178/339/148/175.
#       `report_ranks_all` RED on bank/PHYSICS rank 2. The old single-margin
#       check was green on this.
#   M2  40 physics ladder answers padded 25 characters. Both checks RED.
#   M3  45 physics ladder answers padded 9 characters — small enough that the
#       single-margin table at MARGIN 6 absorbs much of it.
#       `report_ranks_all` RED on ladder/PHYSICS rank 1.
#
# ⚠️ The sweep stayed green on M1, correctly: its baseline is the 53.4% worst
# case this branch INHERITED, and M1 is still better than that. The two checks
# cover different things and both are needed — that is why there are two.


def worse_than_baseline(n, k, base_rate, hot):
    """Is this scope DETECTABLY worse than the state it inherited?

    ⚠️ NOT `rate > base_rate`, which is what the first version of this rule
    was, and it is the wrong test on a proportion. On a 95-set scope a strict
    inequality fires on two sets, which is inside sampling noise — and a gate
    that goes red on noise is a gate people learn to re-run rather than read.
    It also fired the other way: an improvement of one set in 140 was failed,
    because the direction of "no worse" is opposite for the two tells.

    So the question asked here is the one that has an answer: given the
    baseline's own rate, would a scope this size land this far the wrong side
    of it by chance? A one-sided binomial against the BASELINE rate, at the
    same `ALPHA` as everything else. Being at or the right side of the
    baseline always passes; being worse fails only when the corpus is big
    enough for "worse" to mean anything.
    """
    if hot == "GIVEAWAY":
        if k <= base_rate * n:
            return False
        return binom_tail_ge(k, n, base_rate) < ALPHA
    if k >= base_rate * n:
        return False
    return binom_tail_le(k, n, base_rate) < ALPHA


PHYS = {"P%d" % i for i in range(1, 13)}
FAIL = []


def _binom_pmf(i, n, p):
    """One binomial term, in log space.

    ⚠️ NOT `math.comb(n, i) * p**i * (1-p)**(n-i)`, which is what this was.
    That is exact and fine at n = 70, and it raises OverflowError the moment a
    corpus is big enough to matter: `math.comb(1380, 493)` is a 400-digit
    integer and Python refuses to multiply it by a float. The gate crashed on
    the bio/chem bank the first time the rank check was pointed at it. Logs
    have no such ceiling.
    """
    if p <= 0.0:
        return 1.0 if i == 0 else 0.0
    if p >= 1.0:
        return 1.0 if i == n else 0.0
    log = (math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
           + i * math.log(p) + (n - i) * math.log(1.0 - p))
    return math.exp(log) if log > -745.0 else 0.0


def binom_tail_ge(k, n, p):
    """P(X >= k) for X ~ Binomial(n, p). No scipy in this repo."""
    return sum(_binom_pmf(i, n, p) for i in range(k, n + 1))


def binom_tail_le(k, n, p):
    return sum(_binom_pmf(i, n, p) for i in range(0, k + 1))


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


def collect(skipped=None):
    """(corpus, unit, where, options, correct_idx) per measurable set.

    `skipped`, if given, is a dict this fills with the sets it could NOT
    measure — see `report_skipped` for why that is not optional.
    """
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
                elif skipped is not None:
                    # No `answer` index, so nothing here knows which option is
                    # right and the set cannot be measured. It is RECORDED,
                    # not dropped — see `report_skipped`.
                    grp = "PHYSICS" if code in PHYS else "BIO+CHEM"
                    b = skipped.setdefault(("hook", grp), [0, 0])
                    b[0] += 1
                    if visibly_longest(texts(ph["options"])) is not None:
                        b[1] += 1
    for rec in qb.load_bank():
        for q in rec["questions"]:
            ci = [i for i, o in enumerate(q["options"]) if o.get("correct")]
            if len(ci) != 1:
                continue
            sets.append(("bank", rec["unit"], q.get("id"),
                         texts(q["options"]), ci[0]))
    return sets


def rank_of(opts, ans):
    """Where the correct option sits when the four are ordered longest-first.

    ⚠️ ADDED 1 Sep 2026 BY THE THIRD COLD DOUBLE-CHECK, AND IT IS THE MOST
    IMPORTANT THING IN THIS FILE.

    Until now this gate only ever asked about RANK 1 — is the correct option
    the visibly longest. That is one exploit of four, and a fix aimed at it
    does not remove the information, it MOVES it. That is not hypothetical:
    MRB-297 widened one distractor in each of six hooks to push the correct
    answer off rank 1 — ⚠️ chasing an exploit that does not exist, because the
    hook is ungraded (R3); see the corpus list in the docstring — and measured
    on the same 70 sets

        pick the longest      34.3% -> 25.7%   (fixed)
        pick the 2nd longest  34.3% -> 42.9%   p = 0.0008   (created)

    A student who picks the second-longest option now does better than one who
    picks the longest ever did, and the old check could not see it, because
    `visibly_longest()` never looks below rank 1. The gate was gameable and it
    was gamed by its own author.

    So every rank is measured, under the same two-condition rule the rest of
    the file uses. Length carries no information only when the correct answer
    is equally likely to be the longest, the second, the third or the
    shortest — that is the property; rank 1 was only ever a proxy for it.
    """
    order = sorted(range(len(opts)), key=lambda j: (-len(opts[j]), j))
    r = order.index(ans)
    # ⚠️ AND THE RANK ONLY COUNTS IF A STUDENT COULD IDENTIFY IT.
    # "Pick the second-longest" is only a strategy if the second-longest can
    # be told apart from the first and the third. Counting every set makes the
    # measure obey differences of one or two characters that nobody perceives
    # — and then demands they be shuffled, which is precisely the padding
    # this file's own opening refuses. Measured on the physics hooks: the raw
    # distribution says rank 2 is 42.9% and looks alarming; filtered to the
    # positions a reader can actually resolve it is 4 sets in 70, all at rank
    # 4, with nothing significant anywhere. The raw number was an artefact of
    # invisible differences. The ladder, filtered the same way, keeps a real
    # signal — so the filter is not a way of making the problem go away.
    lens = [len(opts[j]) for j in order]
    gaps = []
    if r > 0:
        gaps.append(lens[r - 1] - lens[r])
    if r < len(order) - 1:
        gaps.append(lens[r] - lens[r + 1])
    if any(g < MARGIN for g in gaps):
        return None
    return r


def rank_all(opts, ans):
    """The correct option's rank by length, with NO margin filter.

    Ties broken by authored order, which is arbitrary and therefore fair: it
    cannot be steered by an edit. The point of this measure is its fixed
    denominator — every four-option set counts, always — so a rate here means
    the same thing before and after a change. See `RANK_ALL_BASELINE`.
    """
    return sorted(range(len(opts)), key=lambda j: (-len(opts[j]), j)).index(ans)


def _hot(n, k, alpha=None):
    """"GIVEAWAY" / "MIRROR" / "" for k of n against chance, both conditions.

    `alpha` overrides `ALPHA` — the sweep passes a corrected one. See
    `SWEEP_CELLS` for why.
    """
    if n == 0:
        return ""
    a = ALPHA if alpha is None else alpha
    rate = k / n
    if rate > HI and binom_tail_ge(k, n, CHANCE) < a:
        return "GIVEAWAY"
    if rate < LO and binom_tail_le(k, n, CHANCE) < a:
        return "MIRROR"
    return ""


# ⚠️ THE SWEEP TESTS EVERY RANK AT EVERY MARGIN, WHICH IS A LOT OF TESTS, AND
# A THRESHOLD APPLIED ONCE PER TEST IS NOT THE SAME THRESHOLD.
#
# 8 margins x 4 ranks x 4 corpus-groups is about 130 cells per run. At
# `ALPHA` = 0.01 each, roughly one of them is expected to look significant on
# a corpus with no tell in it at all — so an uncorrected sweep is a gate that
# goes red on healthy data and teaches people to re-run it. The cells are also
# nested subsets of each other and therefore highly correlated, which makes
# Bonferroni conservative rather than wrong.
#
# So the sweep divides `ALPHA` by the number of cells it actually tested on
# this run, counted rather than assumed. Measured 1 Sep 2026: 132 cells, so
# the corrected threshold is 7.6e-5. What that changes, on the tree that
# prompted it: physics bank rank 2 at margin 9 (p = 8.8e-5) and physics ladder
# rank 2 at margin 3 (p = 0.0069) stop being findings, and physics bank rank 4
# at margin 10 (p = 5.1e-6) remains one. The whole-corpus check above is a
# SINGLE test per rank and is not corrected — it does not need to be.
SWEEP_ALPHA_NOTE = "ALPHA / cells tested"


def report_ranks_all(tally):
    """PRIMARY CHECK — the whole-corpus rank distribution, fixed denominator."""
    bad = []
    print("  RANK OVER EVERY SET — no margin filter, so the denominator is the")
    print("  whole corpus and a rate means the same thing before and after a")
    print("  change. This is the measure that gates. Chance is 25% at each rank.")
    for (corpus, grp) in sorted(tally):
        cnt = tally[(corpus, grp)]
        n = sum(cnt)
        if n < 20:
            continue
        gates = HOOK_GATES if corpus == "hook" else True
        cells, fails = [], False
        for r, k in enumerate(cnt):
            hot = _hot(n, k)
            tag = ""
            if hot:
                base = RANK_ALL_BASELINE.get((corpus, grp, r))
                if base is None:
                    tag = " " + hot
                    if gates:
                        fails = True
                        bad.append("%s/%s rank %d (whole corpus)"
                                   % (corpus, grp, r + 1))
                else:
                    br = base[1] / base[0]
                    if worse_than_baseline(n, k, br, hot):
                        tag = " %s WORSE THAN ITS BASELINE %.1f%%" % (hot, 100 * br)
                        if gates:
                            fails = True
                            bad.append("%s/%s rank %d (whole corpus)"
                                       % (corpus, grp, r + 1))
                    else:
                        tag = " %s BASELINED %.1f%%" % (hot, 100 * br)
            cells.append("r%d %4d/%d=%5.1f%%%s" % (r + 1, k, n, 100 * k / n, tag))
        mark = "✅" if not fails else "❌"
        note = "" if gates else "   (measured, not gated — R3: hooks are ungraded)"
        print("  %s %-16s %s%s" % (mark, "%s %s" % (corpus, grp),
                                   " · ".join(cells), note))
    return bad


def report_sweep(sets):
    """PRIMARY CHECK — every rank at every margin from 3 to 10.

    A fix shaped to one `MARGIN` shows up here as a number that is fine at the
    value this file happens to ship and bad two either side of it. That is
    precisely what this run did to its own headline figure, and the
    single-margin table could not see it.

    ⚠️ EVERY CELL IS WALKED, NOT JUST THE WORST ONE. The first version took the
    maximum rate per scope, which is >= 25% by construction, so it could never
    report a MIRROR — and a fix that creates a strong "never pick the long one"
    at one particular margin is exactly the kind this check exists to catch.
    """
    bad = []
    cells = {}                      # (corpus, grp, rank) -> (rate, M, n, k)
    # Two passes: the first counts the cells so the second can correct for
    # how many tests are being run. See the note on `SWEEP_ALPHA_NOTE`.
    tested = 0
    corrected = [ALPHA]
    for _pass in (0, 1):
      if _pass:
        corrected[0] = ALPHA / max(1, tested)
        tested = 0
        cells = {}
      for M in SWEEP_MARGINS:
          tal = collections.defaultdict(lambda: [0, 0, 0, 0])
          for corpus, unit, _w, opts, ans in sets:
              if len(opts) != 4:
                  continue
              grp = "PHYSICS" if unit in PHYS else "BIO+CHEM"
              order = sorted(range(4), key=lambda j: (-len(opts[j]), j))
              r = order.index(ans)
              lens = [len(opts[j]) for j in order]
              if r > 0 and lens[r - 1] - lens[r] < M:
                  continue
              if r < 3 and lens[r] - lens[r + 1] < M:
                  continue
              tal[(corpus, grp)][r] += 1
          for key, cnt in tal.items():
              n = sum(cnt)
              if n < 20:
                  continue
              for r, k in enumerate(cnt):
                  tested += 1
                  hot = _hot(n, k, alpha=corrected[0])
                  if not hot:
                      continue
                  # Keep the WORST margin for this rank, in the direction that
                  # rank is bad in: highest for a giveaway, lowest for a mirror.
                  cur = cells.get((key[0], key[1], r))
                  rate = k / n
                  if cur is None or (rate > cur[0] if hot == "GIVEAWAY"
                                     else rate < cur[0]):
                      cells[(key[0], key[1], r)] = (rate, M, n, k, hot)
    print()
    print("  WORST CELL AT EACH RANK ACROSS MARGINS 3..10 — a fix that only")
    print("  works at the margin this file happens to ship is not a fix. This")
    print("  gates. Only cells that are RED somewhere in the sweep are listed.")
    if not cells:
        print("  ✅ no rank in any corpus is red at any margin in 3..10")
    for key in sorted(cells):
        corpus, grp, r = key
        rate, M, n, k, hot = cells[key]
        gates = HOOK_GATES if corpus == "hook" else True
        base = SWEEP_BASELINE.get(key)
        fails = False
        if base is None:
            tag = " %s — NO BASELINE: this rank was not red at the branch point" % hot
            fails = gates
        elif worse_than_baseline(n, k, base, hot):
            tag = " %s WORSE THAN ITS BASELINE %.1f%%" % (hot, 100 * base)
            fails = gates
        else:
            tag = " %s BASELINED %.1f%%" % (hot, 100 * base)
        if fails:
            bad.append("%s/%s rank %d across margins" % (corpus, grp, r + 1))
        note = "" if gates else "   (measured, not gated)"
        print("  %s %-16s rank %d at margin %2d: %3d/%-4d = %5.1f%%%s%s"
              % ("✅" if not fails else "❌", "%s %s" % (corpus, grp),
                 r + 1, M, k, n, 100 * rate, tag, note))
    return bad


def report_ranks(rank_tally):
    """The full rank distribution, per corpus per group. Fails like the rest."""
    bad = []
    print("  RANK OF THE CORRECT OPTION BY LENGTH — 1 is longest, 4 shortest,")
    print("  counting only the sets where that position is VISIBLE (every "
          "bounding gap >= %d chars)." % MARGIN)
    print("  Chance is 25% at every rank; a fix that only flattens rank 1 has "
          "moved the tell, not removed it.")
    for key in sorted(rank_tally):
        corpus, grp = key
        cnt = rank_tally[key]
        n = sum(cnt)
        if n < 20:                      # too few to say anything
            continue
        cells = []
        for r, k in enumerate(cnt):
            rate = k / n
            hot = ""
            if rate > HI and binom_tail_ge(k, n, CHANCE) < ALPHA:
                hot = "GIVEAWAY"
            elif rate < LO and binom_tail_le(k, n, CHANCE) < ALPHA:
                hot = "MIRROR"
            excused = False
            if hot:
                base = RANK_BASELINE.get((corpus, grp, r))
                # ⚠️ "NO WORSE" POINTS THE OTHER WAY FOR THE TWO TELLS, and
                # getting that backwards excuses a real regression while
                # failing a real improvement. A GIVEAWAY is a rate that is too
                # HIGH, so no-worse means rate <= baseline. A MIRROR is a rate
                # that is too LOW, so no-worse means rate >= baseline. Caught
                # by the physics ladder's rank 3 going 15/140 to 16/140 — an
                # improvement — and being failed for it.
                if base is not None:
                    br = base[1] / base[0]
                    excused = (rate <= br + 1e-9 if hot == "GIVEAWAY"
                               else rate >= br - 1e-9)
                # ⊕ 1 Sep 2026 — THIS TABLE NO LONGER GATES. It is read at
                # one value of `MARGIN`, and a fix aimed at one value of a
                # judgement constant is a fix aimed at the constant. What
                # gates is `report_ranks_all` (no filter, fixed denominator)
                # and `report_sweep` (worst across margins 3..10). This stays
                # because it is the most readable view of the distribution,
                # and because the two that gate are harder to eyeball.
                if not excused:
                    bad.append("%s/%s rank %d" % (corpus, grp, r + 1))
            cells.append("r%d %2d/%d=%4.1f%%%s"
                         % (r + 1, k, n, 100 * rate,
                            (" " + hot + (" BASELINED" if excused else ""))
                            if hot else ""))
        fails = any(("GIVEAWAY" in c or "MIRROR" in c) and "BASELINED" not in c
                    for c in cells)
        print("  %s %-9s %s" % ("‼️" if fails else "· ",
                                "%s %s" % (corpus, grp), " · ".join(cells)))
    print("  (‼️ marks a hot cell at this one margin. It does not fail the "
          "run — see the two checks above.)")
    return []


def report_skipped(skipped):
    """Say out loud what this gate cannot see. Not optional.

    ⚠️ A GATE THAT SILENTLY SKIPS A CORPUS REPORTS NO DEFECTS IN IT, WHICH IS
    NOT THE SAME AS THERE BEING NONE. This gate was written after exactly that
    happened: P1's eight hooks had no `answer` index, so nothing measured them,
    so nothing was wrong with them — until the index was written down and five
    of five turned out to be giveaways.

    ⊕ ADDED 1 Sep 2026 by the second cold double-check, which found the same
    shape still here and larger: **all 115 biology and chemistry hooks carry
    `answer = None`**, 66 of them have a visibly longest option, and the gate
    printed no line for them at all — so the omission was invisible in the
    output rather than merely unreported. It is now the first thing printed.
    """
    if not skipped:
        return
    print("  ⚠️  NOT MEASURED — these sets carry no `answer` index, so nothing")
    print("      here knows which option is right. Reported, not hidden.")
    for (corpus, grp), (n, vis) in sorted(skipped.items()):
        print("      %-6s %-10s %3d set(s) skipped, %d of them with a visibly "
              "longest option" % (corpus, grp, n, vis))
    print()


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
    ranks = collections.defaultdict(lambda: [0, 0, 0, 0])
    ranks_all = collections.defaultdict(lambda: [0, 0, 0, 0])
    skipped = {}
    sets = list(collect(skipped))
    for corpus, unit, _where, opts, ans in sets:
        grp = "PHYSICS" if unit in PHYS else "BIO+CHEM"
        if len(opts) == 4:
            ranks_all[(corpus, grp)][rank_all(opts, ans)] += 1
            r = rank_of(opts, ans)
            if r is not None:
                ranks[(corpus, grp)][r] += 1
        j = visibly_longest(opts)
        if j is None:
            continue
        for scope in ("whole corpus %s" % grp, unit):
            tally[(corpus, scope)][0] += 1
            tally[(corpus, scope)][1] += (j == ans)

    print()
    report_skipped(skipped)
    FAIL.extend(report_ranks_all(ranks_all))
    FAIL.extend(report_sweep(sets))
    print()
    report_ranks(ranks)
    print()

    for corpus in ("bank", "ladder", "hook"):
        keys = [k for k in tally if k[0] == corpus]
        print()
        if not keys:
            # ⚠️ ⊕ 1 Sep 2026 — THIS USED TO BE `continue`, AND SILENCE READ AS
            # CLEAN. A corpus with no visibly-longest option anywhere printed
            # no line at all, so "measured and found nothing" and "not
            # measured" looked identical in the output — which is the exact
            # defect this whole file exists to catch, sitting in the file.
            # `verdict()` has had the right words for `n == 0` all along and
            # was never reached.
            print("  ✅ %s" % verdict(corpus, "whole corpus", 0, 0)[1])
            continue

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
    # ⚠️ ⊕ 1 Sep 2026 — THIS LINE USED TO SAY "no corpus or unit lets option
    # length answer the question", WHICH IS NOT WHAT GREEN MEANS HERE. Five
    # scopes are baselined giveaways: they DO let length answer the question
    # and they pass because they are recorded debts that have not got worse.
    # `docs/ks3/gate-caption-agreement.md` quoted the old wording as a
    # guarantee. Green means "no scope is worse than what it inherited, and
    # nothing new has appeared" — which is a real thing, and a smaller one.
    debts = len(BASELINE) + len(RANK_ALL_BASELINE) + len(SWEEP_BASELINE)
    print("verify_answer_lengths: OK — nothing new, and no scope worse than "
          "the state it inherited.")
    print("  ⚠️  %d baselined scope(s) still let length answer the question. "
          "Green is not clean." % debts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
