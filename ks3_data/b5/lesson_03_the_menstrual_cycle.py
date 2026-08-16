"""B5 L3 — The menstrual cycle (PROCESS).

Authored against Claude Design's approved page,
`KS3 B5 lessons/b5-03-the-menstrual-cycle.dc.html` (594 lines), its author's
notes `KS3 B5 lessons/NOTES-B5.md`, and the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`).

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", none of which is a
sentence of science. The four events, both marked rungs, both self-marked rungs
and every string the dial prints came out of
`node tools/extract_design_payload.js` and out of the page's own markup, not off
a keyboard.

── ⚠️ TONE IS A GATE ON THIS LESSON, AND IT IS SHARPER HERE ─────────────

`ks3_data/b5/__init__.py` carries the unit's ruling. What it means on THIS page,
because this is the lesson where a reader may or may not be described by the
subject:

**Design writes "a person's cycle" throughout and never "your cycle", and that
third-person choice is ruled.** The hook asks about *a person's* cycle; rung 1
asks about *someone's* cycles; rung 4 asks about *two people*. Nothing on the
page addresses the reader as someone who has cycles, and nothing tells the
reader what to do about their own. NOTES-B5 §4 asks for exactly that to be
confirmed as tone rather than as science, and it is carried below as a design
flag rather than acted on.

The copy is lifted. It is not softened, not sharpened, and no warning is added
to it — a warning would be an authoring pass editorialising over a register a
teacher chose, and it would be the one thing on the page a student could tell
was added. The legal line goes where §8.10 puts it: `convention_note`, small, at
the bottom edge, plain `.ks3-legal`, never a callout.

⚑ **ONE second-person sentence exists on the page and it is lifted as drawn.**
The Going further layer closes *"Anything personal about your own cycle is a
question for a school nurse, doctor or pharmacist rather than a calculation."*
That is the only "your … cycle" in the lesson, it is a signpost rather than
teaching copy, and the legal line does the same thing in the same words. Under
MRB-205 the page wins; it is reported rather than rewritten, because whether the
signpost is allowed to break third person is Mide's call and not this pass's.

── `covers` is the SUB-ID, and the exclusion is the point ───────────────

`KS3.B.REP.01` is the human-reproduction bullet and `ks3_data/substatements.py`
splits it at its own clause list. This lesson owns **`KS3.B.REP.01c`** — *"The
menstrual cycle, without details of hormones."*

The exclusion is not a formality and the page honours it exactly: the lining is
*held ready* and then *no longer held*, and nothing that does the holding is
named anywhere. No hormone, no gland, no "chemical messenger". NOTES-B5 flag 17
asks whether that silence is the right reading of the exclusion, or whether the
softer reading — unnamed chemical messengers — was intended. Authored as
delivered; the flag is carried below.

The page's own endmatter says what the exclusion defers: *"The four hormones
that control the cycle, the graphs that go with them, and how contraception and
fertility treatment work on that control."* That is `ks4_becomes`, and it is the
only place hormones are mentioned on the page.

── ⚖️ THE INSTRUMENT CARRIES THE WHOLE TEACHING POINT ───────────────────

`#s-dial` is `cycle-dial`, on `ks3-block ks3-dark ks3-practical` (page line
106), so `practical` is MEASURED from Design's own markup and not inherited.

**The release day is DERIVED as `length − 14` and is never stored.** Design's
own `renderVals()` computes `const rel = len - LUTEAL;` (page line 442) and
`LUTEAL` is 14. The fortnight AFTER release is the fixed part; the building
phase before it is what stretches. So 21 → day 7, 28 → day 14, 35 → day 21, and
a dial that always read "day 14" would teach the exact belief the lesson exists
to kill. `luteal` and `shed` are authored as the two constants; no release day
appears anywhere in this file, in any phase text, or in any note.

Rail credit follows the same argument: the stage completes when **two different
lengths have been seen**, not when the slider reaches the end. Walking day 1 to
day 28 without touching a length chip demonstrates nothing this lesson claims.

⚑ **NOTES-B5 flag 14 — the arithmetic this whole lesson rests on. FOR MIDE.**
  Design flags it herself as the one she would want answered first, and it is
  two questions rather than one:
    1. Is `release = length − 14` right? The interval from release to the next
       period is the steadier one and is usually given as 12–16 days; the page
       rounds it to "about a fortnight" and derives a day from it.
    2. Is deriving a DAY arithmetically acceptable at KS3 at all, rather than
       teaching a range?
  Authored exactly as delivered, including the hedges Design chose ("roughly",
  "about", "nearer day 21"). Nothing is hardened and nothing is softened.

── The rail loses a stop, and it is the defect four units have now found ─

Design draws FOUR stops and `#s-events` ticks on `Object.keys(s.seen).length
>= 2` (page line 392) — the DIAL's predicate, verbatim, one section to the left.
`#s-events` is an eyebrow, a display statement, four static cards and a key
fact: no control, no commitment, no field. MRB-208 ruled the rail is
completion-based and carries only sections that require the student to do
something, and `ks3_parity.check_rail_reachable` fails a section carrying none
of the signals `doneByDom()` reads — which a `rule` panel carries none of.

So the lesson declares THREE stops. Same call, same reasoning and same shape as
b4-01's `#s-parts`, b3-06's `#s-three`, c1-02's `#s-matrix` and c1-05's
`#s-scale`. **The section keeps its anchor**, so every hash link into `#s-events`
still resolves.

Design's dropped stop is `{id: 's-events', label: 'Four events'}`, short
`EVENTS`. Recorded here because the label is hers and is otherwise lost.

── What could not be lifted, and why ────────────────────────────────────

1. **The events' NUMBER CHIPS.** Design draws `#s-events` as an `<ol>` of four
   cards, each with an ink `01`–`04` chip. `r_rule` emits a `<ul>` of term/gloss
   cards and has no slot for a numeral. Document order is preserved, so the four
   events still read in order; the chips are DROPPED rather than smuggled into
   the card text. Same finding as b4-01, and the fix — if the chips are to win —
   is an `index` flag on `rule`, not a new block type: §5.1.1's vocabulary is
   closed and `render_blocks` raises on anything outside it.

2. **⚑ The PROMOTION of event 03 is dropped, and it is a real loss.** Design
   paints the *Release* card on `--ks3-inset` with a 3px border and an accent
   number chip while the other three are `--ks3-card` at 2px (page lines
   536–539), and NOTES-B5 §1 names that promotion as the shape of the lesson:
   *"then four events, with release promoted."* `r_rule`'s cards carry no
   emphasis flag and inventing one is an engine change this pass does not make
   (build contract §0). Every word of the card survives; only its weight is
   lost. **Reported, not worked around.** b5-02 and b5-07 promote a step in the
   same way and will meet this identically — it is one flag on `rule`, once.

3. **The `when` line is FOLDED into the card term, not dropped.** Design sets it
   in mono accent type on the same baseline as the event's name (`Release` /
   `About a fortnight before the next period`). All four are different strings
   and every one is science — *"About a fortnight before the next period"* is
   the whole claim of the lesson — so they are joined to the name with " · ",
   which is b4-01's precedent (`Alveoli · Gas exchange — the only place`) and
   Design's own separator elsewhere on this page. Both strings survive
   byte-identical.

4. **The key fact leaves Design's band panel.** She nests it inside `#s-events`;
   `r_rule` has no nested key-fact slot (only `r_comparison` does), so it renders
   as its own top-level block directly under the panel, on the band ground every
   other top-level key fact in the key stage takes. The words and the order are
   unchanged.

5. **Design draws TWO endmatter link cards; the engine emits one.** Her "Next in
   this unit" (`gestation-placenta-and-birth`) and "Connects to"
   (`human-reproductive-systems`, `gametes-and-fertilisation`) are one card in
   `r_endmatter`, headed by `connects_heading`. All three links live in it, the
   forward one first, under "Connects to" — b4-01 and b3-01 resolved the
   identical layout the identical way, and "Connects to" is the heading Design
   draws over two of the three. The heading "Next in this unit" is what is given
   up; no link is.

   `requires` stays EMPTY for the same reason: Design draws no "Before this
   lesson" card, and a `requires` edge would render one she did not draw.

6. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

7. **The legal line's mono `<span>`.** `convention_note` escapes, so
   `b5-cycle-timeline` renders in body copy rather than in mono. The words are
   unchanged. b4-01 resolved this the same way.

8. **`vocabulary` definitions are AUTHORED, not lifted.** Design draws no
   keyword block anywhere in B5, so these never reach the lesson body: the terms
   become the unit page's chips and the reading-age gate's exclusion list, which
   matters here because "oviduct", "uterus" and "menstrual cycle" would
   otherwise count against the page. `verify_ks3.py` requires the list to be
   non-empty. Every definition below is assembled from the page's OWN sentences
   and adds no claim the page does not make; three of the six are the page's
   words verbatim. Flagged because they are the only student-reachable strings
   in this file that Design did not write.

── ⚑ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS FAIL ───────

Measured with `verify_ks3.py`'s own `length_tell()` heuristic, not by eye:

    ladder recall (rung 1): correct 11w against a longest distractor of 6w
                            → flagged (gap 5 ≥ 4)
    ladder apply  (rung 2): correct 12w against a longest distractor of 8w
                            → flagged (gap 4 ≥ 4)

Both are Design's option sets exactly as drawn. **Nothing here is rewritten.**
Rewriting a distractor changes what a marked question measures, which
verify_ks3.py's own register says in as many words is Mide's gate and not an
authoring pass's — and `verify_ks3.py` is the engine pass's file under build
contract §0, so this pass neither rewrites the options nor registers the
exemption. Reported with the measurements so it can be ruled on.

── Figures are declared and NOT drawn (§4.10) ───────────────────────────

Design's legal line names ONE slot on this page, `b5-cycle-timeline`, and no
artwork exists for it. It is declared at `status: "needed"` so the manifest
counts it as a sourcing task rather than losing it. Nothing is invented to fill
it, and no `figure` block is added to `core` — Design draws no figure slot, and
one here would be a component nobody drew. NOTES-B5 flag 13 asks Mide to confirm
what he wants illustrated across the unit before anything is commissioned.

⚑ For Mide's science gate — NOTES-B5 flags landing on THIS lesson:
  * flag 14 — `release = length − 14`, and whether deriving a day
    arithmetically is right at KS3. See above; it is the lesson's central claim.
  * flag 15 — three fixed lengths (21 / 28 / 35) rather than a free slider.
    Design's reasoning: the fixed set makes 7 / 14 / 21 visible at a glance,
    where a free slider would be more honest about the messiness.
  * flag 16 — days 1–5 as the bleeding window (commonly given as 2–7 days).
  * flag 17 — no hormones anywhere, and whether *held ready* / *no longer held*
    is what the statutory exclusion means.
  * flag 18 — *"one person's own cycles vary between themselves"*, which is the
    part of the misconception most often left out.
  * flag 19 — the Going further cites daily-temperature, hormone-test and
    app-data studies and quotes no figure, deliberately.
  * flag 5, carried from b5-02 and reused here — the egg is fertilisable for
    "roughly a day" (usually given as 12–24 hours). It appears in event 03 and
    in the dial's release-day ovary panel.

⚑ Two page-internal inconsistencies, both reported rather than silently ruled
  (MRB-205):
  1. **Typography, not science.** The page body writes straight apostrophes
     ("one person's own cycles", line 194) and the script constants write
     curly ones ("one person’s cycles vary between themselves", rung 4
     criterion 4). Both are lifted byte-identical FROM THEIR OWN SOURCE, so this
     file carries both forms deliberately. Normalising either would break the
     byte-identity rule against the half it changed.
  2. **The hook's reveal and event 03 give the same fact in two registers.** The
     reveal says a 28-day cycle releases "around day 14"; event 03 says "near
     day 14". Not a contradiction, and noted only because the numbers are the
     lesson's argument and a reviewer will read both.
"""

# ── the four events (page lines 335–344, via extract_design_payload.js) ──
#
# `when` is joined to `name` with " · " — see "What could not be lifted" 3. The
# `what` prose is untouched, and the `01`–`04` chips and the promotion of event
# 03 are lost with `r_rule`'s card shape — see 1 and 2.
EVENTS = [
    ("The lining breaks down", "Days 1–5 — the period",
     "The lining built during the last cycle is no longer being held, so it "
     "breaks down and passes out through the vagina. By convention the first "
     "day of bleeding is day 1 of the cycle, which is simply the easiest day "
     "to notice."),
    ("Building, and one egg maturing", "From about day 5 to release",
     "The uterus lining thickens again with tissue and blood vessels, while in "
     "one ovary a single egg cell finishes maturing. This is the stretchy part "
     "of the cycle: it is longer in a long cycle and shorter in a short one."),
    ("Release", "About a fortnight before the next period",
     "The mature egg cell leaves the ovary and is drawn into the oviduct, "
     "where it can be fertilised for roughly a day. In a 28-day cycle that "
     "falls near day 14; in a 21-day cycle nearer day 7; in a 35-day cycle "
     "nearer day 21."),
    ("Held ready", "The fortnight after release",
     "The lining is at its thickest and is kept that way. If a fertilised egg "
     "implants, it stays and the cycle stops here. If none does, it breaks "
     "down — and that is event 1 of the next cycle."),
]

EVENT_CARDS = [{"term": "%s · %s" % (name, when), "gloss": what}
               for name, when, what in EVENTS]


# ── the dial's three cycle lengths (page lines 331, 466–471) ────────────
#
# ⚠️ `note` is the sentence the dial prints once a second length has been seen,
# and Design keys it on the DERIVED release day, not on the length: `rel === 7`,
# `rel === 21`, else the 28-day case. With `luteal` fixed at 14 the two are the
# same partition, and keying it on the length the student actually pressed is
# the honest authored form — the release day is derived and is never stored,
# which is the whole argument of the instrument.
#
# ⚠️ NO RELEASE DAY IS AUTHORED ANYWHERE IN THIS RECORD. The day 7 / 14 / 21 in
# these notes are Design's own prose about what the marker did, not the value
# the marker is drawn from.
LENGTHS = [
    {"days": 21, "label": "21 days",
     "note": "A 21-day cycle releases around day 7 — and still has about a "
             "fortnight left afterwards. The short cycle is short at the "
             "front."},
    {"days": 28, "label": "28 days",
     "note": "The 28-day case, where release lands on day 14. Every other "
             "cycle length moves that number, which is why day 14 is not a "
             "fact about people."},
    {"days": 35, "label": "35 days",
     "note": "A 35-day cycle releases around day 21, two weeks later than a "
             "21-day cycle does, and the fortnight after release is the same. "
             "All the extra length sits in the building phase."},
]

# ── the four phases the dial reads out (page lines 446–463) ─────────────
#
# ⚠️ THE BOUNDARIES ARE DERIVED, NEVER STORED — exactly like the release day,
# and for the same reason. Design's `renderVals()` branches `day <= SHED` →
# `day < rel` → `day === rel` → else, where `rel = length − luteal`. A phase
# carrying a `from`/`to` pair would freeze the boundaries at one cycle length
# and the dial would stop being about anything.
PHASES = [
    {"id": "shed", "label": "Period",
     "ovary": "Nothing has been released. Egg cells are present, and one of "
              "them will begin the run of maturing that ends in this cycle’s "
              "release.",
     "uterus": "The lining built during the last cycle is breaking down and "
               "passing out through the vagina. This is the bleeding, and it "
               "is why day 1 is easy to identify."},
    {"id": "build", "label": "Building",
     "ovary": "One egg cell is completing its maturing inside the ovary. It "
              "has been there, immature, since before birth.",
     "uterus": "The lining is thickening again — new tissue and new blood "
               "vessels, built ready in case a fertilised egg arrives."},
    {"id": "release", "label": "Release",
     "ovary": "The mature egg cell leaves the ovary and is drawn into the "
              "oviduct. It can be fertilised for roughly a day from now.",
     "uterus": "The lining is nearly at full thickness. Nothing about it has "
               "changed today — the event is happening in the other organ."},
    {"id": "held", "label": "Held ready",
     "ovary": "The egg is in the oviduct, or has already broken down. No "
              "further egg is released this cycle.",
     "uterus": "The lining is at its thickest and is being held that way. If a "
               "fertilised egg implants it stays; if not, it breaks down and "
               "the next cycle begins."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 124 character for character. Slugs are
    # permanent (§8.4) and are the join for every progress record.
    "slug":        "the-menstrual-cycle",
    "title":       "The menstrual cycle",
    "discipline":  "biology",
    "unit":        "reproduction",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `c` clause of the split bullet — the cycle, WITHOUT hormone detail.
    # See the docstring: the exclusion is honoured by naming nothing that does
    # the holding, and `ks4_becomes` is where the hormones are deferred to.
    "covers":      ["KS3.B.REP.01c"],
    # EMPTY, and deliberately. The page names fertilisation, the oviduct and
    # implantation — but every one of those is a SIBLING CLAUSE of this
    # lesson's own bullet (`REP.01b`, `REP.01d`), owned by b5-02 and b5-04.
    # `touches` names statements outside the lesson's own bullet, and this
    # lesson reaches outside it nowhere.
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires` and no `before_this`: Design draws no "Before this lesson"
    # card and the engine would emit one from either. All three of her links
    # live in the middle card, the forward one first — see "What could not be
    # lifted" 5.
    "requires":    [],
    "assumes":     [],
    "references":  ["gestation-placenta-and-birth",
                    "human-reproductive-systems",
                    "gametes-and-fertilisation"],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    # The only mention of hormones on the page, and it is a deferral rather
    # than teaching. Lifted from the endmatter's third card.
    "ks4_becomes": "The four hormones that control the cycle, the graphs that "
                   "go with them, and how contraception and fertility "
                   "treatment work on that control.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Two organs, one repeating month. An egg matures in an "
                    "ovary while a lining is built in the uterus — and the two "
                    "are timed against each other.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # THREE stops. Design draws four; `s-events` is dropped — see the docstring.
    # `short` and `label` are Design's own `RAIL_SHORT` and `RAIL` strings
    # (page lines 323–329).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Not day 14",
         "done_when": "committed"},
        # Design's own threshold, kept: `Object.keys(s.seen).length >= 2`. The
        # stage ticks when a SECOND cycle length has been seen, not when the
        # slider reaches the end — walking every day of one cycle demonstrates
        # nothing this lesson claims. The instrument opens with `{28: true}`
        # already seen, so the count starts at one and nothing is ticked on
        # load (MRB-208).
        {"anchor": "s-dial", "short": "DIAL", "label": "Walk the days",
         "done_when": "two_lengths_seen"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3), and no length
    # tell is possible in an unmarked set.
    #
    # ⚠️ Third person, and it is the ruled register: "A person's cycle is 32
    # days long", never "your cycle". Lifted exactly.
    "phenomenon": {
        "kind": "narrative",
        "title": "Day 14 is not when the egg is released. It is when the egg "
                 "is released in a 28-day cycle.",
        "prompt": "Ordinary cycles run anywhere from about 21 days to about "
                  "35, and the same person's cycles vary between themselves. "
                  "So the day the egg is released cannot be the same number "
                  "for everybody.",
        "commit": "A person's cycle is 32 days long. Roughly when is the egg "
                  "released?",
        "options": [
            "Day 14 — it is the same day for everyone",
            "Day 16 — halfway through the cycle",
            "Around day 18 — about a fortnight before the next period",
            "There is no way to say even roughly",
        ],
        # `<em>` survives: `r_hook` puts the reveal through `rich()`.
        "reveal": "Around day 18 — and you get there by counting "
                  "<em>backwards</em>. The gap between the egg being released "
                  "and the next period is close to a fortnight in almost "
                  "everyone. The part that stretches or shrinks is the "
                  "building phase before release. So a 21-day cycle releases "
                  "around day 7, a 28-day cycle around day 14, a 35-day cycle "
                  "around day 21, and the famous number turns out to be one "
                  "case rather than the rule.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ IDs are PRE-ALLOCATED by the commander (MRB-244) because eight authors
    # work this unit in parallel and five of them collided on B4's family. This
    # lesson owns `REPRO-05` and `REPRO-06` and nothing else; the third belief
    # below takes `REPRO-19`, allocated out of band at the end of the family for
    # exactly that reason. No id is minted here, and
    # `docs/ks3/misconception-register.md` is the commander's file — the three
    # statements are reported for writing into it.
    #
    # `elicited_by` is honest per entry. REPRO-05 really is surfaced by the
    # hook, which asks the student to commit to a release day before anything
    # is explained, and again by the dial, which moves the marker under them.
    # REPRO-06 and REPRO-19 are asked for nowhere before the block that kills
    # them, so the block is named for both — b4-01's pattern.
    #
    # ⚑ REPRO-19 is the THIRD belief on the page and it has no quote of its
    # own: Design confronts it inside REPRO-06's paragraph ("Nor is any of it
    # waste the body was storing up… The uterus is not disposing of something;
    # it is resetting.") and again in rung 2's distractor B and its correction
    # ("Nothing is being disposed of."). It is a distinct belief with a distinct
    # correction, so it is registered rather than folded into REPRO-06.
    #   The runner-up, and reported so it can be ruled on rather than lost: the
    # belief that the day of release is *completely unpredictable*, offered as
    # hook option D and again as rung 1 distractor D. It is answered only in a
    # rung correction, the page partly CONCEDES it ("a calendar alone predicts
    # this badly"), and it is closer to a claim of ignorance than to a wrong
    # model — so it is not minted.
    "misconceptions": [
        {"id": "REPRO-05",
         "statement": "The cycle is 28 days and the egg comes out on day 14.",
         "elicited_by": "hook",
         "confronted_by": "think-twenty-eight"},
        {"id": "REPRO-06",
         "statement": "A period is the unfertilised egg leaving the body.",
         "elicited_by": "think-twenty-eight",
         "confronted_by": "think-twenty-eight"},
        {"id": "REPRO-19",
         "statement": "Period blood is waste the body has been storing up and "
                      "is getting rid of.",
         "elicited_by": "think-twenty-eight",
         "confronted_by": "think-twenty-eight"},
    ],

    # ── vocabulary ──────────────────────────────────────────────────────────
    # Design draws no keyword block in B5, so these never reach the lesson body:
    # the TERMS become the unit page's chips and the reading-age gate's
    # exclusion list. Definitions are AUTHORED, assembled from the page's own
    # sentences — see "What could not be lifted" 8. Clinical and function-first,
    # third person, no euphemism, and no claim the page does not make.
    #
    # "ovulation" is deliberately absent: the page never uses the word, and
    # giving a student a term the lesson does not use is a term they will not
    # find when they look for it.
    "vocabulary": [
        {"term": "menstrual cycle",
         "definition": "The repeating monthly cycle in which an egg cell "
                       "matures and is released from an ovary while the lining "
                       "of the uterus is built up and then broken down.",
         "note": "Two organs, timed against each other."},
        {"term": "uterus",
         "definition": "The organ whose lining is built up ready to receive a "
                       "fertilised egg.",
         "note": None},
        {"term": "lining",
         "definition": "The layer of tissue and blood vessels built up inside "
                       "the uterus, held ready, and broken down if no "
                       "fertilised egg implants.",
         "note": "It is what leaves the body during a period."},
        {"term": "ovary",
         "definition": "The organ in which egg cells are stored and in which "
                       "one finishes maturing each cycle before it is "
                       "released.",
         "note": None},
        {"term": "oviduct",
         "definition": "The tube the released egg cell is drawn into, where it "
                       "can be fertilised for roughly a day.",
         "note": None},
        {"term": "period",
         "definition": "The days at the start of a cycle when the lining "
                       "breaks down and passes out through the vagina.",
         "note": "Day 1 of the cycle is its first day — a place to start "
                 "counting, not the start of the process."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # Design's legal line names this slot and no artwork exists for it, so it is
    # DECLARED at `needed` rather than dropped: the manifest is generated from
    # this field, which turns a dangling reference into a tracked sourcing task.
    # `needed` is not a build blocker. The caption describes only what this
    # lesson teaches, and names no release day — the diagram has to show the
    # release marker MOVING with the length or it would draw the misconception.
    "figures": [
        {"id": "b5-cycle-timeline",
         "kind": "diagram",
         "caption": "One cycle drawn as a timeline for each of the three "
                    "lengths, 21, 28 and 35 days: the bleeding window at the "
                    "start, the building phase, release a fortnight before the "
                    "end, and the fortnight in which the lining is held ready "
                    "— with the release marker landing on a different day in "
                    "each of the three.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-dial — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b5/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 106), so the segment is MEASURED, not inherited — and it
        # is on INK, so every text rule in the instrument's CSS must be scoped
        # to at least (0,2,0) to beat `.ks3-dark p`. That is the engine pass's
        # business and is recorded in `ks3_data/b5/__init__.py`.
        {"type": "cycle-dial", "id": "walk-the-days", "anchor": "s-dial",
         "demand": "investigate",
         "eyebrow": "Set a cycle · walk the days",
         "heading": "One month, two organs",
         "head_counter": {"format": "{n} of 3 lengths tried", "total": 3},
         "prompt": "Choose a cycle length, then move through the days. Watch "
                   "where the release day lands each time you change the "
                   "length.",

         # ⚖️ THE TWO CONSTANTS THE WHOLE INSTRUMENT IS DERIVED FROM.
         # `luteal` is Design's `LUTEAL = 14` and `shed` her `SHED = 5`
         # (page lines 332–333). The release day is `length − luteal`,
         # computed, never stored; the phase boundaries are computed from the
         # same two numbers. See the docstring and NOTES-B5 flag 14.
         "luteal": 14,
         "shed": 5,

         "lengths": LENGTHS,
         "length_label": "Cycle length",
         # Design's opening state: `{length: 28, day: 1, seen: {28: true}}`.
         # The 28-day case is where the misconception lives, so the dial opens
         # on it and the student's first press is the one that breaks it.
         "start_length": 28,
         "start_day": 1,
         # Rail credit is TWO DIFFERENT LENGTHS, not the end of the slider —
         # Design's `Object.keys(s.seen).length >= 2`, and NOTES-B5 §2.1 says
         # so in as many words.
         "credit_lengths": 2,

         # The day control: a slider between the −/+ buttons that exist for
         # keyboard and small screens. Labels are Design's own `aria-label`s
         # (page lines 138–140).
         "day_label": "Day of cycle",
         "prev_label": "Previous day",
         "next_label": "Next day",

         # The track's three captions and the readout above the panels.
         # `{n}` is the day; the release caption's day is DERIVED.
         "track": {"start": "Day 1",
                   "release": "Release · day {n}",
                   "last": "Day {n}"},
         "day_format": "Day {n}",

         # The two readout panels, and the four phases they read out. Phase
         # order is Design's branch order and the boundaries are derived —
         # see PHASES.
         "panels": {"ovary": "In an ovary", "uterus": "In the uterus"},
         "phases": PHASES,

         # The note under the panels before a second length has been seen. It
         # is an instruction to change the length, which is the one thing the
         # instrument needs the student to do; after that each length prints
         # its own note.
         "note_prompt": "Now change the cycle length and watch the release "
                        "marker move. That movement is the point of this "
                        "instrument."},

        # #s-events — the band panel. NOT on the rail; see the docstring.
        # `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid — Design's markup
        # (page lines 163–181) minus the number chips and minus event 03's
        # promotion.
        {"type": "rule", "anchor": "s-events",
         "eyebrow": "The cycle, in four events",
         "statement": "It ends where it starts, which is why it is drawn as a "
                      "circle.",
         "cards": EVENT_CARDS},

        # Design nests this inside `#s-events`; `r_rule` has no nested slot, so
        # it renders directly under the panel in document order. See "What
        # could not be lifted" 4.
        {"type": "key-fact", "ref": "two-organs-at-once"},

        {"type": "misconception", "id": "think-twenty-eight",
         "anchor": "s-think", "targets": "REPRO-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "two-organs-at-once",
         "text": "The menstrual cycle is two things happening at once in two "
                 "different organs: one egg cell maturing and being released "
                 "from an ovary, and the lining of the uterus being built up "
                 "and then broken down. Day 1 is the first day of bleeding — a "
                 "place to start counting, not the start of the process.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and an authored statement wins over the register.
        # The block asks for no commitment, on Design's page and here, so it is
        # not a rail stop and emits no completion contract (this is B1's
        # `confrontation` case, not the MRB-220 R1 `predict` case).
        #
        # ⚠️ The second statement's paragraph confronts TWO beliefs — REPRO-06
        # and REPRO-19 — and is lifted whole. Splitting it into two statements
        # would give Design a third quote she did not draw.
        {"id": "think-twenty-eight",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "REPRO-05",
         "statements": [
             # Quotes are bare: `_quoted()` strips and re-wraps in “ ” exactly
             # once, which is what Design draws.
             {"quote": "The cycle is 28 days and the egg comes out on day 14.",
              "body": ["Twenty-eight is an average of many people's cycles, "
                       "and averages are not rules — no more than <em>the "
                       "average family has 1.7 children</em> describes an "
                       "actual family. Cycles from about 21 to about 35 days "
                       "are entirely ordinary, and one person's own cycles "
                       "vary from month to month, which is the part most often "
                       "left out. What is fairly steady is the other end: the "
                       "gap from release to the next period is close to a "
                       "fortnight in almost everyone. That is why the "
                       "arithmetic runs backwards from the end of the cycle "
                       "rather than forwards from day 1, and it is why a "
                       "calendar alone predicts this badly. If you take one "
                       "number away from this lesson, take the range rather "
                       "than the average."]},
             {"quote": "A period is the unfertilised egg leaving the body.",
              "body": ["It is not, and the sizes make that obvious once you "
                       "have them. An egg cell is about 0.1 mm across — barely "
                       "visible, and nothing you could ever see leave. What "
                       "leaves is the lining of the uterus: the layer of "
                       "tissue and blood vessels that was built up over the "
                       "previous few weeks, breaking down and passing out "
                       "through the vagina because no fertilised egg implanted "
                       "in it. The egg itself simply breaks down where it is, "
                       "unnoticed. Nor is any of it waste the body was storing "
                       "up: it is a lining that was built for a job, kept "
                       "ready for about a fortnight, and cleared when the job "
                       "did not arrive. Then it is built again. The uterus is "
                       "not disposing of something; it is resetting."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚑ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS FAIL. Neither
    # option set is rewritten; see the docstring for the measurements and for
    # why the repair is not this pass's to make.
    #
    # Rungs 3 and 4 are Design's `SELF_RUNGS`: the student marks themselves
    # against her criteria, and only the ladder scores.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Use the rule",
            "q": "Someone’s cycles are 24 days long. Roughly which day is the "
                 "egg released?",
            "options": [
                "Day 12 — halfway through",
                "About day 10 — roughly a fortnight before the next period",
                "Day 14, the same as everybody",
                "It is completely unpredictable",
            ],
            "answer": 1,
            "feedback": {
                0: "Halfway is a guess that only works by accident. The steady "
                   "interval is the one after release, not the one before it.",
                2: "Day 14 is release in a 28-day cycle only. In a 24-day "
                   "cycle it would leave just ten days before the next "
                   "period.",
                3: "The exact day cannot be pinned down, but the pattern is "
                   "not random — counting back about a fortnight gets you "
                   "close.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "What leaves the body during a period?",
            "options": [
                "The unfertilised egg cell",
                "The lining of the uterus, built up during the previous few "
                "weeks",
                "Blood the body has no further use for",
                "Part of the ovary",
            ],
            "answer": 1,
            "feedback": {
                0: "An egg is 0.1 mm across — far too small to see, and it "
                   "breaks down where it is. What you can see is not the egg.",
                # ⚑ This correction is REPRO-19's, and it is the only place the
                # belief is answered outside the confrontation paragraph.
                2: "Nothing is being disposed of. A lining was built for a "
                   "job, held ready, and cleared when no fertilised egg "
                   "arrived — then built again.",
                3: "The ovary is not shed. It releases one egg cell and stays "
                   "where it is.",
            }},
        "explain": {
            "title": "Rung 3 · Describe one whole cycle",
            "q": "Describe what happens in the ovary and in the uterus across "
                 "one complete cycle. Say what event day 1 is counted from, "
                 "and make clear which two things are happening at the same "
                 "time.",
            "field_label": "Your description",
            "placeholder": "Day 1 is counted from…",
            "success": [
                "Says day 1 is the first day of bleeding, and that this is a "
                "counting convention.",
                "Says the uterus lining breaks down and passes out over "
                "roughly the first five days.",
                "Says the lining then thickens again while one egg cell "
                "matures in an ovary — both at once.",
                "Says the mature egg is released into the oviduct roughly a "
                "fortnight before the next period.",
                "Says the lining is held ready, and breaks down again if no "
                "fertilised egg implants.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Two people have cycles of 26 and 34 days. Working from day "
                 "1, say roughly when each releases an egg, explain why the "
                 "eight-day difference is not shared evenly across the cycle, "
                 "and give one reason a calendar still cannot predict the day "
                 "reliably.",
            "field_label": "Your answer",
            "placeholder": "Counting back a fortnight from the end…",
            "success": [
                "Gives roughly day 12 and roughly day 20, by counting back "
                "about a fortnight from the end.",
                "Says the interval from release to the next period is close to "
                "a fortnight in both.",
                "Says the difference therefore falls almost entirely in the "
                "building phase before release.",
                # ⚠️ Curly apostrophe, lifted from the script constant. The
                # page body writes the same phrase with a straight one — see
                # the docstring's second page-internal inconsistency.
                "Gives a reason a calendar fails — one person’s cycles vary "
                "between themselves, so the next length is not known in "
                "advance.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "In the ovaries, one egg cell finishes maturing and is "
                "released roughly a fortnight before the next period. In the "
                "uterus, the lining thickens ready to receive a fertilised "
                "egg, is held for about a fortnight, and breaks down if none "
                "implants — which is the period, and day 1 of the next cycle. "
                "Cycle lengths of about 21 to 35 days are ordinary and vary "
                "within one person; 28 days is an average, not a rule.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES-B5 flag 19: the studies are cited and no figure is quoted, which is
    # deliberate — every figure Design could quote either dates or is disputed.
    #
    # ⚑ The last sentence carries the page's only second person ("your own
    # cycle"). It is a signpost, not teaching copy, and it is lifted as drawn.
    # See the tone note at the head of this file.
    "stretch": [
        {"type": "explainer", "id": "where-twenty-eight-came-from",
         "text": "Where did 28 come from? It is close to the average of a "
                 "large number of cycles, it is close to a lunar month, and "
                 "those two coincidences together gave it a grip on the "
                 "subject that the evidence never supported. When researchers "
                 "began tracking large numbers of real cycles — first with "
                 "daily temperature and hormone tests, more recently with app "
                 "data from millions of users — the picture that came back was "
                 "a spread, not a number: most cycles somewhere in the "
                 "twenties or low thirties, the same person often varying by "
                 "several days between one cycle and the next, and the day of "
                 "release scattered accordingly. The steadier interval is the "
                 "one after release. This is a good example of a general "
                 "problem with averages in biology: the average is a real fact "
                 "about the population and can still describe almost nobody in "
                 "it. Anything personal about your own cycle is a question for "
                 "a school nurse, doctor or pharmacist rather than a "
                 "calculation."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check why the counting runs backwards?",
              "cta": "Ask about this lesson",
              "anchor": "s-dial"},

    # ⊕ MRB-228's `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph and nothing in it is a safety instruction: it is a
    # note about how the numbers on this page were taken, a statement of what
    # the lesson deliberately does not cover, a signpost, and a declaration
    # about a figure not yet drawn. Routing it through `safety_note` would
    # print it in the treatment reserved for "never light a candle without an
    # adult", which devalues the safety line — and §8.10 puts a legal note
    # small, at the bottom edge, never as a callout. b4-01, b3-05 and b3-07
    # resolve the identical foot line the identical way.
    #
    # ⚠️ Lifted whole. The signpost sentence is part of it and is not trimmed,
    # rewritten or promoted into the body of the lesson.
    "convention_note": "Cycle lengths and the day of release are typical "
                       "values: about 21 to 35 days is ordinary, and one "
                       "person's cycles vary between themselves. Hormone names "
                       "and hormone graphs are deliberately outside Key Stage "
                       "3 and are met at GCSE. This lesson covers the biology; "
                       "anything personal belongs with your school nurse, "
                       "doctor or a trusted adult, and relationships and "
                       "consent are covered in RSE and PSHE. The labelled "
                       "cycle diagram is declared in the lesson record as "
                       "b5-cycle-timeline, awaiting illustration.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `analysis-and-evaluation`: the dial is a model the student changes one
    # variable in and reads the consequence out of, and rung 4 asks for two
    # cases to be compared and a limitation given.
    # `scientific-attitudes`: the lesson's argument is that an average can be a
    # real fact about a population and describe almost nobody in it, and the
    # Going further makes that a claim about evidence rather than about cycles.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
