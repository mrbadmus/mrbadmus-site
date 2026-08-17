"""B6 L3 — Substance misuse and decisions (INVESTIGATION).

Authored against Design's approved page,
`KS3 B6 lessons/b6-03-substance-misuse-and-decisions.dc.html` (597 lines),
under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the three items listed under "What could not be lifted", none of which
is a sentence of science. On this unit that is a safeguarding rule as much as
an accuracy one (`ks3_data/b6/__init__.py`, "TONE IS A GATE"): nothing here is
softened, sharpened, or given a warning it was not drawn with.

── `covers` — WS anchor AND the substatement, and both are honest ───────

§5.7.1 rules that an INVESTIGATION lesson anchors `covers` on the Working
Scientifically statement it teaches, "and declares no subject statement it does
not genuinely own" — clause 3 of the same rule then says a subject statement
may be added "only if the lesson genuinely owns it and no other lesson does".
Both halves apply here, so `covers` carries both IDs:

  * `KS3.WS.ANA.05` — *evaluate data, showing awareness of potential sources of
    random and systematic error* — is the lesson in one line. All five faults
    in the instrument are SYSTEMATIC: selection of the sample (c2), confounding
    (c3), absence of a control and a conflict of interest (c4), survivorship
    (c5), and a fact about the substance's history offered as data at all (c1).
    And the page teaches the random/systematic distinction outright: rung 1's
    "The sample is too small" is answered *"It might be large — and that would
    not help"*, and c3's verdict is *"size fixes noise, not confusion"*. That
    sentence is ANA.05's own distinction in a student's words.
  * `KS3.B.HLTH.01c` — *substance misuse: its effects, and how a claim made
    about a drug is judged as evidence* — is minted in `ks3_data/substatements.py`
    FOR THIS LESSON and for no other. The key note carries the first clause
    ("Substance misuse means using a substance in a way that damages health —
    including legal ones, and including medicines taken wrongly") and the whole
    page carries the second. Dropping it to take the WS anchor alone would
    leave the unit's only statutory statement covered two-thirds, and the
    clause would be owned by nobody.

The precedent is `ks3_data/b1/lesson_02_using_a_microscope.py`, the other
INVESTIGATION lesson that genuinely owns a subject clause: `["KS3.WS.EXP.05",
"KS3.B.CELLS.01b"]`, same shape, same reasoning. `b3-02` and `c1-06` carry a WS
statement alone because they own no subject clause — not because a subject
clause is forbidden.

── The flagship: five claims, five faults, and no invented distractor ───

`#s-claims` is `claim-check`, on `ks3-block ks3-dark ks3-practical` (page line
104), so `practical` is MEASURED from Design's own markup; `ks3_data/b6/__init__.py`
maps it and lifts it into `activities[]`.

⚖️ THE 1:1 MAPPING IS THE PEDAGOGY, AND IT IS WHY THE POOL IS FIVE.
Each fault is the correct answer for exactly one claim, so **every wrong pick
is still a true statement about evidence** — the student who puts "no comparison
group" on the grandad claim has said something true about evidence and attached
it to the wrong argument, which is a different and more useful error than
guessing. NOTES-B6 §2.3 states the rule and closes the door on distractors:
*"Do not add invented distractors."* Nothing here is invented; the pool is
Design's five, and `answer` is asserted below to be a bijection onto them.

⚖️ NOTHING ON THE OPTION BUTTON SAYS RIGHT OR WRONG. Design's own note at page
line 518: *"House rule: the bench does not mark right and wrong. It highlights
the pick, then the verdict panel names the fault in a sentence (as b5-01
does)."* Her `faultOptions` style proves it — the chosen option takes
`--ks3-alert` border and a 10% white wash, the unchosen ones fade to `.5`
opacity once checked, and no branch of that expression is ever green or red.
Only the ladder marks correctness (MRB-208 / MRB-196 R10). The verdict eyebrow
is the sole verdict, in words: "That is the fault" / "Not the main fault here".

── One rail stop comes off, and it is the defect C1 already found ───────

Design draws FOUR stops and `#s-four` ticks on `opened >= CLAIMS.length` (page
line 421) — the BENCH's predicate, verbatim, one section to the left. MRB-208
ruled the rail is completion-based and carries only sections that require the
student to do something; `#s-four` is an eyebrow, a display statement, four
static cards and a key fact, with no control, no commitment and no field.
`ks3_parity.check_rail_reachable` fails a stop whose section carries none of
the signals `doneByDom()` reads, and inventing a demand Design did not draw is
closed to this build. So the lesson declares THREE stops — the same call and
the same shape as c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-01's
`#s-nutrients`, b3-02's `#s-limits` and b4-01's `#s-parts`. The section keeps
its anchor, so every hash link into it still works.

── What could not be lifted, and why ────────────────────────────────────

1. **The four cards' `Question 1`–`Question 4` chips, and their column.**
   Design draws `#s-four` as a grid of four cards, each with a mono accent
   `Question n` label above the name. `r_rule` emits `<li><p class="ks3-rule-
   term">…</p><p class="ks3-rule-gloss">…</p></li>` and has no slot for a
   third line. Document order is preserved, so the four questions still read
   in the order the eyebrow promises ("Four questions, asked in this order"),
   and the chips are DROPPED rather than folded into the card term — unlike
   b4-01's `role` tags, which were science ("Gas exchange — the only place"),
   these are positional labels the eyebrow already states. Same finding, same
   resolution, as b4-01's `01`–`06` number chips. Reported; the fix, if the
   chips are to win, is an `index` flag on `rule`.

2. **The support layer's eyebrow.** Design heads the referral block *"If any of
   this is about you or someone you know"*; `lesson_page` calls
   `r_layer(..., "ks3-support", "Need a hand?")` with the heading hard-coded,
   and `build_ks3.py` is not this author's file to change. The BODY — which is
   the whole safeguarding content, including "the services listed in your
   school's PSHE materials" — is lifted byte-identical and the block renders in
   Design's own position and treatment. The heading is the one string given up.
   **Reported for the engine pass: `r_layer` needs a per-lesson heading
   override before this unit ships**, because "Need a hand?" reads as help with
   the science on a block that is about help with a substance.

3. **The `<em>` around *Going further* in the foot line.** `convention_note`
   goes through `t()`, which escapes, so the tags would print as text. The
   words are unchanged and the emphasis is what is given up; b4-01 and b5-03
   resolve the identical escaped foot line the identical way.

── ⊕ MRB-177 · RULED 17 Aug 2026 · BOTH marked rungs are repaired ───────

Mide ruled the SHAPE rather than the twenty instances. The ruling, because it
is what the option sets below are now built to: on a recall or apply rung the
correct answer states a RULE — subject, condition, consequence — while the
distractors stated one-clause wrong REASONS. The correct answer was therefore
longer by construction, and a student could score the question without reading
it. A distractor must state a WRONG RULE instead: the same shape as the correct
answer, with the misconception as the consequence. Length parity then follows
from the construct, so nothing had to be trimmed.

Six distractors across the two marked rungs are Mide's own replacement copy,
applied verbatim. **Neither correct option was touched, neither `answer` index
moved, and `verify_ks3.py`'s threshold is unchanged.** Measured after:

  * `ladder recall` — correct **12w** against 16 / 15 / 17. No longer the
    longest option at all.
  * `ladder apply` — correct **16w** against 16 / 17 / 17. No longer strictly
    the longest.

⛔ SUPERSEDED, KEPT AS HISTORY. This section used to record the two rungs as
tells "exactly as drawn" — recall 12w against 8w (gap 4, ratio 1.50), apply 16w
against 9w (gap 7, ratio 1.78) — and closed: *"NOT rewritten, and NOT registered
here: `KNOWN_TELLS` lives in `verify_ks3.py`, which this author does not own,
and the register's own comment says rewriting a distractor changes what a marked
question measures — that is Mide's gate, not this script's."* It was his gate,
and he has now passed through it. The two `substance-misuse-and-decisions`
entries in `KNOWN_TELLS` are consequently stale; the commander deletes them, and
`verify_ks3.py` is still not this author's file.

One feedback string moved with its distractor: rung 2's correction for option D
answered a claim about "other healthy habits" that is no longer offered, and was
rewritten in the same voice and length band. The other five corrections already
answered the new wording and were left byte-identical.

⚑ For Mide's science gate — NOTES-B6 §3 flags landing on THIS lesson:
  * **flag 12 — the five claims are INVENTED, and so are their study numbers.**
    The 500 sixth-formers, the four marks, the 22 of 30, the 90% of reviewers
    and the sixty years of daily drinking are all authored examples. Design
    declares it on the page in the foot line ("the studies described in them
    are invented examples with invented numbers") and the line is lifted whole,
    so the invented/real boundary is stated to the student as well as here. The
    Doll and Hill study in *Going further* — around 40,000 British doctors from
    1951 — is REAL and is the one named study on the page. Authored as
    delivered; the boundary is on the record.
  * **flag 13 — *"regular use is a clear minority at this age"***, and the
    stronger claim in the same paragraph that correcting the misperception
    changes behaviour on its own. Both are well supported and neither is given
    with a citation a student could check. NOTES-B6 says this is the one place
    in the unit where a footnote with a source would be accepted. Authored as
    delivered; flagged for your call. If a source is wanted it goes in
    `convention_note` (§8.10 — small, bottom edge, never a callout), not into
    the confrontation, which would then be arguing from an authority in the
    middle of a lesson about not doing that.
  * **flag 14 — no diagrams and no figure slots.** VERIFIED on this page: no
    `<img>`, no `<figure>`, no `<svg>` other than the nav chevron, the rail
    tick and the ladder's mark/arrow glyphs, and nothing named in the foot
    line. `figures` is `[]` — measured, not omitted, and nothing is invented to
    fill it.

⚑ Two page-internal observations, reported rather than ruled on (MRB-205):
  * **Two apostrophe conventions in one page.** The static copy uses straight
    apostrophes throughout ("It's natural", "it's the chemicals", "molecule's"),
    while every string in the `data-dc-script` payload uses the curly `’`
    ("One person’s story", "seller’s own website"). Both are lifted
    exactly as they appear in their own source, so the built page reproduces
    the inconsistency rather than quietly normalising it. Typography, not
    science; Design's to close if she wants one convention.
  * **The hook's option B and its reveal touch `DRUG-01`.** "It is legal to buy
    it in this country" is offered and rejected ("what a shop is allowed to
    sell … [is a fact] about the world around the substance"), which is the
    same belief b6-01 confronts as *"Drugs are illegal substances."* It is NOT
    declared below and no near-duplicate is minted for it: nothing on this page
    confronts it — the hook rejects it in a clause — so an honest
    `confronted_by` does not exist here. The register's `reappears_in` on
    `DRUG-01` is the right home for it, which is the commander's file.
"""

# ── the five faults (page lines 330–336) ────────────────────────────────
#
# ⚠️ THE POOL IS CLOSED. Five faults for five claims, one each. Adding a sixth
# "obviously wrong" option would break the property the whole instrument is
# built on — that a wrong pick is still a true statement about evidence — and
# NOTES-B6 §2.3 forbids it in as many words.
FAULTS = [
    {"id": "origin",
     "text": "Where the substance came from is not evidence about what it "
             "does."},
    {"id": "sample",
     "text": "The people asked are not a fair sample of the group being "
             "described."},
    {"id": "cause",
     "text": "Two things happening together has been treated as one causing "
             "the other."},
    {"id": "control",
     "text": "There is no comparison group, and the people asked were chosen "
             "by the seller."},
    {"id": "single",
     "text": "One person’s story cannot tell you the risk for anyone "
             "else."},
]

# ── the five claims (page lines 338–364) ────────────────────────────────
#
# ⚑ INVENTED, INCLUDING THE NUMBERS — NOTES-B6 flag 12, and the page says so
# in its own foot line. They are the shapes of arguments people really make.
CLAIMS = [
    {"id": "c1", "label": "Natural", "answer": "origin",
     "text": "“Cannabis is safe — it is a plant, and people have "
             "used it for thousands of years.”",
     "evidence": "It grows in the ground with no chemicals added, and it has "
                 "been used in many cultures for centuries.",
     "why": "Both halves of the evidence are about the history of the plant "
            "rather than its effect on a body. Deadly nightshade also grows "
            "in the ground and has also been known for centuries. Long use "
            "tells you a substance does not kill most people quickly, which "
            "is a much weaker claim than safe — the harms being argued "
            "about here are effects on the developing brain that appear over "
            "years.",
     "settle": "Studies following large numbers of users and non-users "
               "forward over years, recording mental and physical health "
               "outcomes, with the users’ use recorded before anything "
               "went wrong."},

    {"id": "c2", "label": "Everyone does", "answer": "sample",
     "text": "“Most people our age vape — it is normal now.”",
     "evidence": "Twenty-two of the thirty people in my friendship group and "
                 "my form have tried it, and I see people vaping outside "
                 "school every day.",
     "why": "Your friendship group is not a random sample of your age, and "
            "neither is the group standing outside school — people who "
            "vape are visible and talk about it, people who do not are doing "
            "nothing you would notice. This is the same fault as testing a "
            "new drug only on people who volunteered because they already "
            "liked it.",
     "settle": "A national survey that samples tens of thousands of pupils "
               "chosen at random rather than by who is easy to see, and asks "
               "about regular use rather than about ever trying it once."},

    {"id": "c3", "label": "Energy drinks", "answer": "cause",
     "text": "“Energy drinks improve your exam results.”",
     "evidence": "A study of 500 sixth-formers found that those who drank "
                 "energy drinks during study leave scored on average four "
                 "marks higher than those who did not.",
     # ⚖️ "size fixes noise, not confusion" is the sentence `KS3.WS.ANA.05`
     # is anchored on — random error against systematic error, in a student's
     # words. It is the reason this claim is the largest study on the board
     # and still the worst evidence.
     "why": "The two groups chose themselves, and they differ in more than "
            "the drink. Students who revise for long hours late at night are "
            "exactly the students who buy energy drinks, so revision hours "
            "could produce the whole difference. The study is large and still "
            "cannot tell you which way the arrow points — size fixes "
            "noise, not confusion.",
     "settle": "Take one group of students, split them at random into two, "
               "give one the drink and the other an identical-tasting drink "
               "with no caffeine, and compare. Randomising is what breaks the "
               "link between the drink and everything else about the person."},

    {"id": "c4", "label": "Herbal cure", "answer": "control",
     "text": "“This herbal supplement cures anxiety — nine out of "
             "ten users agree.”",
     "evidence": "Reviews on the seller’s own website: 90% of the people "
                 "they asked said they felt calmer after taking it for a "
                 "month.",
     "why": "Nobody was compared with anything. Anxiety varies week to week "
            "and improves for many people anyway, so “felt calmer after "
            "a month” would be reported by a good fraction of people "
            "given a tablet with nothing in it. On top of that, the seller "
            "chose which reviews to publish and profits from the answer, and "
            "no dose is stated at all.",
     "settle": "A trial where neither the patients nor the assessors know who "
               "received the supplement and who received an identical dummy, "
               "with the results published by someone with nothing to sell."},

    {"id": "c5", "label": "My grandad", "answer": "single",
     "text": "“Drinking every day cannot be that harmful — my "
             "grandad did it and lived to 90.”",
     "evidence": "One person, known personally, who drank daily for sixty "
                 "years and stayed well.",
     "why": "Risk is a statement about how often something happens across "
            "many people, so a single case can never contradict it — "
            "people survive things that are dangerous all the time. There is "
            "also a hidden bias in who you get to hear about: the drinkers "
            "who died at 55 are not around to be anyone’s example, so "
            "the survivors are the only ones telling you their story.",
     "settle": "Death and illness rates for many thousands of daily drinkers "
               "compared with similar non-drinkers, which is how the risk was "
               "estimated in the first place."},
]

# ⚖️ THE BIJECTION IS ASSERTED, NOT ASSUMED. If a future edit gives two claims
# the same fault, the instrument silently stops being 1:1 — one fault becomes
# unreachable and one wrong pick stops being "the right fault for a different
# claim", which is the property the block's own prompt promises the student.
# The build should fail on that rather than ship it.
_ANSWERS = [c["answer"] for c in CLAIMS]
assert sorted(_ANSWERS) == sorted(f["id"] for f in FAULTS), (
    "claim-check: the five claims must map onto the five faults exactly "
    "once each — see NOTES-B6 §2.3 and the block's own prompt")

# ── the four questions (page lines 366–371) ─────────────────────────────
#
# `num` ("Question 1" … "Question 4") is DROPPED — see "What could not be
# lifted" 1. Document order carries the order the eyebrow promises.
TEST_CARDS = [
    {"term": "How many, and who?",
     "gloss": "Thirty friends is not a sample of a nation. Ask how the people "
              "were chosen, not just how many there were."},
    {"term": "Compared with what?",
     "gloss": "A result with nothing to compare it against is not a result. "
              "Who was the group that did not get the thing?"},
    {"term": "Who is telling me?",
     "gloss": "Someone who profits from the answer is not disqualified, but "
              "their evidence needs checking by someone who does not."},
    {"term": "Together, or because?",
     "gloss": "Two things rising at once is where investigations start, not "
              "where they finish. Something else may be causing both."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 135 character for character.
    "slug":        "substance-misuse-and-decisions",
    "title":       "Substance misuse and decisions",
    "discipline":  "biology",
    "unit":        "health-and-drugs",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # WS anchor per §5.7.1, plus the one subject clause this lesson genuinely
    # owns and no other lesson teaches. See the docstring.
    "covers":      ["KS3.WS.ANA.05", "KS3.B.HLTH.01c"],
    # Named but not taught: the claims are about cannabis, vaping, caffeine and
    # daily drinking, and the page deliberately teaches none of their effects —
    # b6-01 owns what a drug does once in the blood, b6-02 owns alcohol and
    # tobacco smoke. This lesson borrows them as arguments to be judged.
    "touches":     ["KS3.B.HLTH.01a", "KS3.B.HLTH.01b"],
    "beyond_statutory": False,
    # Level 1 and one thread only. Working Scientifically is deliberately NOT a
    # thread (§4.7), and this lesson's subject content is a definition and five
    # borrowed arguments — an encounter with bodies and systems, not a
    # development of one.
    "threads":     [{"id": "cells-and-systems", "level": 1}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design draws a "Before this lesson" card with both earlier lessons in the
    # unit, which `requires` renders; and a "Connects to" card with the two
    # cross-unit lessons, which `references` renders under Design's own
    # heading. All four targets are authored and live (NOTES-B6 §4).
    "requires":    ["what-drugs-do-to-the-body", "alcohol-and-smoking"],
    "assumes":     [],
    # §4.6 single-source: these are edges, never repeated prose. c1-06 owns how
    # a model earns trust; b3-02 owns what a colour change is worth. Neither
    # idea is re-taught here.
    "references":  [{"unit": "C1", "lesson": "testing-the-model"},
                    {"unit": "B3", "lesson": "food-tests"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Evaluating evidence: sample size, control groups, placebo "
                   "and double-blind trials, peer review, and the difference "
                   "between correlation and cause.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Nobody decides anything from a table of facts. They "
                    "decide from what they have heard, from what they think "
                    "everyone else is doing, and from claims that sound like "
                    "evidence and are not. This lesson is about telling the "
                    "difference.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # THREE stops. Design draws four; `s-four` is dropped — see the docstring.
    # `short` and `label` are Design's own `RAIL_SHORT` and `RAIL` strings
    # (page lines 320–326).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "It is natural",
         "done_when": "committed"},
        # Design's own threshold, kept: `opened >= CLAIMS.length` — every claim
        # checked, not merely picked. A stop that ticked on the first verdict
        # would call the bench finished at a fifth of it.
        {"anchor": "s-claims", "short": "CLAIMS", "label": "Find the fault",
         "done_when": "all_five_checked"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3). The reveal
    # names the last one, which is what makes it a hook rather than a quiz.
    #
    # ⚠️ TONE. The hook's four options are the four bad reasons a student
    # actually hears, offered without comment; option B is legality and option
    # C is what everyone else does. Neither is scolded — the reveal says what
    # each one is a fact ABOUT, and stops.
    "phenomenon": {
        "kind": "narrative",
        "title": "“It's natural, so it can't do you much harm.”",
        "prompt": "Deadly nightshade is natural. Foxglove is natural. Tobacco "
                  "is a plant, and so is the source of the strongest "
                  "painkillers in the hospital. Every one of them grew out of "
                  "the ground without human help, and the ground has no "
                  "opinion about your health.",
        "commit": "Which of these actually tells you whether a substance will "
                  "harm you?",
        "options": [
            "It comes from a plant rather than a factory",
            "It is legal to buy it in this country",
            "Lots of people you know use it and seem fine",
            "Evidence about what it does to a body, at that dose",
        ],
        "reveal": "Only the last one. Where a molecule came from, what a shop "
                  "is allowed to sell, and how many people you know who use "
                  "it are all facts about the world around the substance. "
                  "What it does to a body, at that amount, is the only "
                  "question with a biological answer — and answering it "
                  "takes evidence of a particular shape.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ ID ALLOCATION IS PRE-ASSIGNED, not chosen here. The `DRUG` family is
    # opened by `ks3_data/b6/__init__.py` at `DRUG-01`…`DRUG-06`, two per
    # lesson, and this lesson owns 05 and 06 — pre-allocated because B4's five
    # parallel authors collided twice on `BREATH` ids. The register
    # (`docs/ks3/misconception-register.md`) is maintained centrally and does
    # not yet carry a `DRUG` row; that is the commander's file, not this one.
    #
    # ⊕ `DRUG-09` is the THIRD belief this page confronts, and it is outside
    # the two-per-lesson block by allocation rather than by drift. It is the
    # subject of claim c5 AND of ladder rung 2 — the only belief on the page
    # attacked twice — and rung 2's own title calls it "The one that catches
    # people". `elicited_by` and `confronted_by` are both the bench, honestly:
    # the student picks a fault for the grandad claim before the verdict panel
    # names survivorship bias, and no other block touches it.
    #
    # `DRUG-01` ("Drugs are illegal substances.", b6-01's, confronted there) is
    # NOT declared — see the docstring's second page observation.
    "misconceptions": [
        {"id": "DRUG-05",
         "statement": "If it's natural, it's safe — it's the chemicals that "
                      "hurt you.",
         # Claim c1 is this belief with evidence attached, and the student has
         # to name its fault before the confrontation kills it.
         "elicited_by": "find-the-fault",
         "confronted_by": "two-wrong-ideas"},
        {"id": "DRUG-06",
         "statement": "Everyone my age is doing it.",
         "elicited_by": "find-the-fault",
         "confronted_by": "two-wrong-ideas"},
        {"id": "DRUG-09",
         "statement": "One person who came to no harm disproves a risk.",
         "elicited_by": "find-the-fault",
         "confronted_by": "find-the-fault"},
    ],

    # Design draws no keyword block anywhere in B6, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list. Every definition is
    # the page's own idea in the page's own register — clinical, no scare copy,
    # and `substance misuse` is the key note's sentence rather than a new one.
    "vocabulary": [
        {"term": "substance misuse",
         "definition": "Using a substance in a way that damages health.",
         "note": "Including legal ones, and including medicines taken "
                 "wrongly."},
        {"term": "sample",
         "definition": "The people actually studied, standing in for the much "
                       "larger group being described.",
         "note": "How they were chosen matters as much as how many there "
                 "were."},
        {"term": "comparison group",
         "definition": "The group that did not get the thing being tested, "
                       "measured the same way as the group that did.",
         "note": "A result with nothing to compare it against is not a "
                 "result."},
        {"term": "correlation",
         "definition": "Two things changing together, without anything yet "
                       "saying that one causes the other.",
         "note": "Where an investigation starts, not where it finishes."},
        {"term": "dummy",
         "definition": "An identical-looking, identical-tasting version with "
                       "the active ingredient left out.",
         "note": "Called a placebo at GCSE."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚑ NOTES-B6 flag 14, VERIFIED against this page: no diagram is drawn, no
    # figure slot is named, and the foot line declares nothing. The instrument
    # is the visual. Empty is MEASURED, not an omission — and nothing is
    # invented to fill it.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-claims — the flagship, authored inline and lifted into
        # activities[] by ks3_data/b6/__init__.py::_normalise, which leaves the
        # `practical` shell behind it. Design's block is `ks3-block ks3-dark
        # ks3-practical` (page line 104), so the segment is measured, not
        # inherited — and the ground is INK, so every text rule the renderer
        # adds must out-specify `.ks3-dark p` at (0,1,1) or the label ships
        # invisible for the sixth time (`ks3_data/b6/__init__.py`).
        #
        # ⚠️ Payload source: `docs/ks3/b6-inventory/PAYLOAD-SCHEMA.md` does not
        # exist yet and `r_claim_check` is not in `build_ks3.py` yet, so the
        # keys below follow NOTES-B6 §2.3's declared payload —
        # `{claims: [{id, label, text, evidence, answer, why, settle}],
        #   faults: [5], picks: {}, opened: {}}` — plus the shell key names
        # already standard across the key stage (`eyebrow`, `heading`,
        # `head_counter`, `prompt`, `labels`, `verdicts`), read off c2-01's
        # `claim-switch` and b4-01's `gas-compare`. If the engine's schema
        # lands with different names, this block is the only thing that moves.
        {"type": "claim-check", "id": "find-the-fault", "anchor": "s-claims",
         "demand": "evaluate",
         "targets": "DRUG-09",
         "eyebrow": "At the bench · five claims, five faults",
         "heading": "Find the fault in the evidence",
         "head_counter": {"format": "{n} of 5 checked", "total": 5},
         "prompt": "Each claim comes with the evidence someone offered for "
                   "it. Every fault in the list below is the real fault of "
                   "one of these five claims, so a wrong answer still teaches "
                   "you something about the claim you picked it for.",

         "claims": CLAIMS,
         "faults": FAULTS,

         "labels": {
             "claims": "The claim",
             "evidence": "The evidence offered",
             "faults": "What is wrong with that evidence?",
             "settle": "What would settle it:",
         },
         # ⚖️ The ONLY verdict on the block, and it is in words. Nothing on an
         # option button ever says right or wrong — see the docstring.
         "verdicts": {"right": "That is the fault",
                      "wrong": "Not the main fault here"},
         # The button is the reveal, and it is disabled until a fault is
         # picked: commitment is what buys the verdict.
         "check_label": "Check it",
         "checked_label": "Checked",
         "tally": {"format": "{n} still to check",
                   "done": "all five claims checked"}},

        # #s-four — the band panel. NOT on the rail; see the docstring.
        # `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid — Design's markup
        # (page lines 155–167) minus the `Question n` chips.
        {"type": "rule", "anchor": "s-four",
         "eyebrow": "Four questions, asked in this order",
         "statement": "You do not need to know the science to test the "
                      "evidence.",
         "cards": TEST_CARDS},

        # Design nests this inside `#s-four`; `r_rule` has no nested key-fact
        # slot (only `r_comparison` does), so it renders directly under the
        # panel in document order, on the band ground every other top-level key
        # fact in the key stage takes. The words and the order are unchanged.
        {"type": "key-fact", "ref": "a-claim-is-only-as-good"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "DRUG-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # The four questions of `#s-four`, in one sentence, in the order the cards
    # ask them.
    "key_facts": [
        {"id": "a-claim-is-only-as-good",
         "text": "A claim about a drug is only as good as the evidence behind "
                 "it. Ask how many people were studied, whether there was a "
                 "group to compare against, who paid for the answer, and "
                 "whether two things happening together has been mistaken for "
                 "one causing the other.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second after the
        # first behind an amber-topped divider — `r_confrontation` renders
        # exactly that from `statements[]`, and an authored statement wins over
        # the register. The block asks for no commitment, on Design's page and
        # here, so it is not a rail stop and emits no completion contract.
        #
        # ⚠️ TONE, and it is the reason neither of these is trimmed. The first
        # answers "natural means safe" with chemistry, not with disapproval —
        # it says why nicotine exists at all, and it defends the pharmacy on
        # the grounds of a KNOWN dose rather than on the grounds of authority.
        # The second is the flag-13 paragraph: it names the sampling fault, and
        # then refuses the comforting reading of its own point ("This is not a
        # comfort exercise"). Both are lifted whole.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "DRUG-05",
         "statements": [
             {"quote": "If it's natural, it's safe — it's the chemicals that "
                       "hurt you.",
              "body": ["Every substance in this lesson is a chemical, "
                       "including the water you drank at break. A plant does "
                       "not manufacture its molecules for your benefit; "
                       "several of them are made specifically to poison "
                       "whatever tries to eat the plant, which is why "
                       "nicotine exists at all. Ricin, cyanide and the "
                       "digitalis in foxglove leaves are natural, and the "
                       "purest paracetamol in the pharmacy is made in a "
                       "factory to a known dose, which is precisely what "
                       "makes it safe to use. So <em>natural</em> and "
                       "<em>synthetic</em> tell you about a molecule's "
                       "history and nothing about its effects; the questions "
                       "that matter are what it does in the body and in what "
                       "amount. Herbal products carry an extra problem the "
                       "pharmacy does not: the dose in a leaf varies with the "
                       "plant, the season and the soil, so even a genuinely "
                       "useful herbal remedy is a medicine of unknown "
                       "strength."]},
             # ⚑ NOTES-B6 flag 13 lives in this paragraph — twice. "regular
             # use in a clear minority at this age", and the claim that
             # correcting the misperception changes behaviour on its own.
             # Neither carries a citation a student could check. Lifted whole.
             {"quote": "Everyone my age is doing it.",
              "body": ["Ask a year group to estimate what fraction of them "
                       "drinks, smokes or vapes regularly, and the average "
                       "guess comes out far above the real figure — every "
                       "time this is measured, in every country it is "
                       "measured in. The reason is a sampling fault you have "
                       "already met: the people doing it are visible and talk "
                       "about it, the people not doing it are not doing "
                       "anything noticeable, so your sample is the loud end "
                       "of the room. National surveys of tens of thousands of "
                       "pupils consistently put regular use in a clear "
                       "minority at this age. This is not a comfort exercise. "
                       "The misjudged figure does real work, because "
                       "believing something is normal is one of the strongest "
                       "predictors of starting it — which means an inaccurate "
                       "estimate is a genuine cause, and correcting it "
                       "changes behaviour on its own."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026, AND BOTH RUNGS ARE FIXED.
    # Six distractors are Mide's replacement copy, applied verbatim; both
    # correct options, both `answer` indices and the gate's threshold are
    # untouched. Each distractor now states a WRONG RULE in the same shape as
    # the correct answer, so length parity follows from the construct.
    #   rung 1 (recall): correct 12w against distractors of 16 / 15 / 17.
    #   rung 2 (apply):  correct 16w against distractors of 16 / 17 / 17.
    #
    # ⛔ Superseded, kept: this block used to read "MEASURED, AND BOTH MARKED
    # RUNGS FAIL … 12w against 5 / 8 / 4 … 16w against 9 / 7 / 8 … NOT
    # rewritten — rewriting a distractor changes what a marked question
    # measures, and that is Mide's gate." It was, and he ruled. See the
    # docstring for the ruling in full.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Name the fault",
            "q": "An advert says a sleep supplement works because 94% of the "
                 "customers who reviewed it on the company’s website "
                 "slept better. What is the main fault?",
            "options": [
                "There is no comparison group, and the company chose which "
                "reviews appeared",
                "A result only counts when the sample is large, and this one "
                "was far too small",
                "A natural supplement cannot change the body, so any effect "
                "people report must be imagined",
                "Sleep is a feeling rather than a measurement, so no claim "
                "about it can ever be tested",
            ],
            "answer": 0,
            "feedback": {
                # ⚖️ The random/systematic distinction, and the reason
                # `KS3.WS.ANA.05` is the anchor: more people does not fix a
                # sample that chose itself.
                1: "It might be large — and that would not help. "
                   "Thousands of self-selected reviews with nothing to "
                   "compare them against are still not evidence.",
                2: "Plenty of natural substances have real effects; that is "
                   "why the pharmacy is full of them. The problem here is the "
                   "shape of the evidence, not the origin of the pill.",
                3: "It can, in a sleep laboratory or with a simple diary. The "
                   "study did not fail for lack of a measurement — it "
                   "failed for lack of a control.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Someone answers a warning about daily drinking with "
                 "“my grandad drank every day and lived to 90”. Why "
                 "does that not weaken the warning?",
            "options": [
                "A person who beats a risk has usually understated the habit, "
                "so the story is unreliable",
                "Because a risk is about rates across many people, and one "
                "case cannot contradict a rate",
                "Alcohol affects every body in exactly the same way, so what "
                "happened to him happens to everyone",
                "One person who came to no harm shows the risk was never "
                "real, whatever the figures say",
            ],
            "answer": 1,
            "feedback": {
                0: "Do not attack the story — assume it is completely "
                   "true. It still does not touch the claim, and that is the "
                   "point worth understanding.",
                2: "It does not — people differ. That is exactly why the "
                   "evidence has to be about many people rather than one.",
                # ⊕ MRB-177, 17 Aug 2026. Rewritten with the distractor above
                # it: the old correction opened "He may have" and answered a
                # distractor about other healthy habits, which no longer
                # exists. Same voice, same length band, same job.
                3: "A survivor does not cancel a figure. A risk that is not a "
                   "certainty predicts survivors — finding one is what the "
                   "rate said would happen, not evidence against it.",
            }},
        "explain": {
            "title": "Rung 3 · Design the test",
            "q": "A company claims its drink improves reaction times. Design "
                 "a fair test of that claim, and say why each feature of your "
                 "design is there.",
            "field_label": "Your design",
            "placeholder": "I would take one large group and…",
            "success": [
                "Uses a large group of people rather than a few volunteers "
                "who already like the drink.",
                "Splits them at random into two groups — and says that "
                "randomising is what stops the groups differing in other "
                "ways.",
                "Gives the second group an identical-looking, "
                "identical-tasting drink without the active ingredient.",
                "Measures reaction time the same way, at the same time of "
                "day, for both groups.",
                "Says the people measuring the results should not know who "
                "had which drink, and explains why that matters.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A video shared in a group chat has someone in a white coat "
                 "saying a substance is “completely safe, and the studies "
                 "prove it”. It has two million views and thousands of "
                 "agreeing comments. Work out what you actually know from "
                 "this, and list what you would check before believing it.",
            "field_label": "Your answer",
            "placeholder": "What I know from the video itself is…",
            # ⚠️ Criterion 2's inner quotes are STRAIGHT on the page while the
            # rest of the payload uses curly. Lifted as written — see the
            # docstring's apostrophe note.
            "success": [
                "Says the number of views and comments measures popularity, "
                "not accuracy.",
                "Says a white coat and the word \"studies\" are not the same "
                "as a named study anyone can read.",
                "Asks who made the video and whether they gain from the "
                "claim.",
                "Says “safe” needs an amount attached to it — "
                "safe at what dose, for how long, for whom.",
                "Names a way to check: look for the study itself, or ask a "
                "pharmacist, a GP, the school nurse or a teacher rather than "
                "the group chat.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Substance misuse means using a substance in a way that "
                "damages health — including legal ones, and including "
                "medicines taken wrongly. Claims about drugs are tested the "
                "same way as any other claim: how many people, compared with "
                "whom, reported by whom, and does the evidence show a cause "
                "or only two things happening together. Where a substance "
                "came from tells you nothing, and what you think everyone "
                "else is doing is usually wrong.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B6 flag 12's other half: this is the ONE REAL study on the page,
    # and the page's foot line says so. Doll and Hill, around 40,000 British
    # doctors from 1951 — the number and the naming are both flagged for the
    # science gate and both are authored as delivered.
    "stretch": [
        {"type": "explainer", "id": "the-doctors-study",
         "text": "In 1950 the link between smoking and lung cancer was an "
                 "argument, not a fact — plenty of doctors smoked, and "
                 "tobacco companies pointed out, correctly, that a "
                 "correlation is not a cause. Richard Doll and Austin "
                 "Bradford Hill answered it properly: they recruited around "
                 "40,000 British doctors, recorded what each one smoked, and "
                 "then waited. Following the same people forward for decades "
                 "meant the smoking was recorded <em>before</em> anyone "
                 "became ill, so it could not be explained away as sick "
                 "people misremembering. The death rate climbed with the "
                 "number of cigarettes, and it fell in the doctors who "
                 "stopped. That study design — large, prospective, "
                 "dose-related, reversible on stopping — is why the link is "
                 "now considered settled, and it is the standard every claim "
                 "in this lesson is measured against."},
    ],

    # ── the support layer — the referral block, carried AS DRAWN ────────────
    #
    # ⚠️ THIS IS A SAFEGUARDING BLOCK, NOT SCAFFOLDING, and it is the one place
    # in the lesson that addresses the reader about their own life. Every
    # clause is load-bearing:
    #   * it says what the lesson IS (how to test a claim, which is the
    #     science) and hands pressure and the law to PSHE and RSE, which is
    #     where they belong and where a teacher is present;
    #   * it names four real routes — a trusted adult, the school nurse, a
    #     pharmacist, a GP — and singles out the pharmacist because a
    #     pharmacist needs no appointment and gives no lecture, which is
    #     exactly what a student who is frightened needs to hear;
    #   * it points at "your school's PSHE materials" for the national
    #     confidential services rather than naming one. Design's reason
    #     (NOTES-B6 §1): a named helpline in a lesson page goes stale, and
    #     naming one is a safeguarding decision rather than an authoring one.
    #     **Carried as drawn. Mide may override; nobody else should.**
    # Nothing is softened, no dose or threshold appears, and no warning is
    # added that Design did not draw.
    #
    # ⊕ MRB-244 — RESOLVED. The eyebrow is no longer lost: `r_layer` gained a
    # `support_heading` override (falling back to the old hard-coded string, so
    # no shipped page moves), and this lesson takes it. Design's eyebrow,
    # lifted byte-identical. Two authors flagged the loss independently, which
    # is what made it a defect rather than a preference.
    "support_heading": "If any of this is about you or someone you know",
    "support": [
        {"type": "explainer", "id": "if-this-is-about-you",
         "text": "This lesson teaches how to test a claim, which is the "
                 "science. What to do about pressure from people you like, "
                 "and what the law says, belong in your PSHE and RSE lessons "
                 "and are worth taking there. If any of this is about your "
                 "own home, your own use, or someone you are worried about, "
                 "talk to a trusted adult, the school nurse, a pharmacist or "
                 "a GP — and a pharmacist will answer a question about a "
                 "substance without an appointment and without a lecture. "
                 "Your school's PSHE materials list the national confidential "
                 "services by name."},
    ],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to test a claim you have actually seen?",
              "cta": "Ask about this lesson",
              "anchor": "s-claims"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph here and nothing in it is a safety instruction —
    # it is a declaration about the provenance of the five claims and a
    # disclaimer. Routing it through `safety_note` would print it in the
    # treatment reserved for "never light a candle without an adult", which
    # devalues the safety line; §8.10 puts a legal note small, at the bottom
    # edge, never as a callout. b3-05, b4-01 and b5-03 resolve the identical
    # foot line the identical way.
    #
    # ⚑ This line is what makes NOTES-B6 flag 12 visible to the STUDENT: the
    # claims are invented and their numbers are invented, and the doctors'
    # study is not. It is lifted whole; only the `<em>` around "Going further"
    # is lost, because `convention_note` is escaped.
    "convention_note": "The five claims are written for this lesson. They are "
                       "the shapes of arguments people really make, not "
                       "quotations from named sources, and the studies "
                       "described in them are invented examples with invented "
                       "numbers. The doctors' study in Going further is real. "
                       "Nothing on this page is medical or legal advice.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `analysis-and-evaluation` is the anchor's own strand — five pieces of
    # evidence evaluated and a fault named in each.
    # `scientific-attitudes` — "who is telling me?", the seller who profits,
    # and the Doll and Hill layer, which is publication and peer scrutiny.
    # `experimental-skills` — rung 3 designs a controlled, randomised, blinded
    # trial, and every claim's "what would settle it" names the enquiry that
    # would answer it.
    "ws": ["analysis-and-evaluation", "scientific-attitudes",
           "experimental-skills"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
