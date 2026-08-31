"""B7 L3 — Testing a leaf for starch (INVESTIGATION).

Authored against Design's approved page,
`docs/ks3/design-reference/b7/b7-03-testing-a-leaf-for-starch.dc.html` (584 lines), under the
MRB-220 build contract and `docs/ks3/b7-inventory/PAYLOAD-SCHEMA.md`.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted" and the three rung-2
distractors rewritten under MRB-177, all of which are named below. The five
steps, the five method cards, the six outcomes, both confrontations, all four
rungs and the two foot lines came out of `node tools/extract_design_payload.js`
and the page's own markup, not off a keyboard.

⚠️⚠️ THE SAFETY WORDING IS THE MOST IMPORTANT THING ON THIS PAGE ⚠️⚠️
─────────────────────────────────────────────────────────────────────────
NOTES-B7 flag 14, and Mide's gate under MRB-233. This is the ONE lesson in the
build where a student could read the page as permission to do something, and
FIVE separate strings carry the safety teaching. All five are lifted
byte-identical, none is paraphrased, softened, merged or improved, and they are
listed here so a future edit has to walk past them:

  1. `key_note`, last sentence — "Never heat ethanol over a naked flame."
  2. Method card 3's `gloss` — "Ethanol boils at 78 °C and its vapour catches
     fire easily, so it is heated by standing the tube in hot water — never
     over a flame."
  3. `safety_note` (the foot line) — ethanol highly flammable, water bath only,
     no naked flame in the room; iodine stains and irritates; boiling water and
     hot apparatus need eye protection and a teacher present; follow your
     school's own risk assessment.
  4. Ladder rung 3's `q` requires the safety point, and its fourth criterion
     names both the water bath and the flammability.
  5. The instrument's `flame` verdict — the SAFETY branch, first in precedence,
     which stops the bench rather than spoiling its data.

`safety_note` and not `convention_note`, unlike b5-06, b6-03, b3-05 and b4-01.
Those foot lines are declarations about provenance; this one is a list of
laboratory hazards, and `build_ks3.py` prints `safety_note` in the treatment
reserved for exactly that (`<p class="ks3-legal ks3-safety">`). Routing a real
hazard list through the plain legal class would waste the one treatment the key
stage keeps for "never light a candle without an adult". §8.10 keeps it small,
at the bottom edge, and never a callout — which is where Design draws it.

⚖️ FAULT PRECEDENCE IS THE PEDAGOGY, AND IT IS ORDERED ──────────────────
Safety first (a naked flame stops the bench outright), then the faults that
DESTROY the result (no ethanol, no destarching), then the ones that only
OBSCURE it (no boiling, no softening). A branch that reported the wrong fault
first would teach the wrong lesson about which mistakes matter, so the order is
authored as DATA — `precedence` — rather than left to the insertion order of a
dict and a comment. See the `precedence` note on the block itself.

── ⊕ THE STATUTORY POSITION: WS, NOT `covers: []` ───────────────────────

The brief for this pass said to author `covers: []` if the honest position is
that the lesson carries no statement of its own, and NOTES-B7 §0 says exactly
that: *"b7-03 carries no statement of its own — it is the practical the other
three are argued from, which is why it is placed third rather than second."*

That is right about the SUBJECT statements and wrong about the field.
`architecture.md` §5.7.1 is a RULE, not a judgement call: **every
`INVESTIGATION` lesson anchors `covers` on the `KS3.WS.*` statement it teaches**,
because §10.2 requires `covers` non-empty and a WS-primary lesson owns no
subject statement by design. §7.5 lists all eighteen of them and this lesson is
named in the list. `food-tests` (`KS3.WS.ANA.03`), `substance-misuse-and-
decisions` (`KS3.WS.ANA.05`) and `testing-the-model` (`KS3.WS.ATT.02`) are the
three already on disk and all three do it this way. An empty `covers` would
fail the done-list and break a pattern seventeen other lessons keep.

So: two WS statements, no subject statement, and NOTES-B7 §0's claim survives
intact — all three PHOT statements stay owned by b7-01, b7-02 and b7-04.

  `KS3.WS.EXP.04` — *use appropriate techniques, apparatus, and materials
  during fieldwork and laboratory work, paying attention to health and safety.*
  The spine of the page: five steps with a reason each, and the safety point
  that rung 3 requires and the bench enforces.

  `KS3.WS.EXP.03` — *…including identifying independent, dependent and control
  variables.* The destarching argument, which is the lesson's real intellectual
  claim: `PLANT-06`, the bench's `destarch` branch, rung 2, and rung 4's
  designed two-set-up investigation. WS statements are exempt from §4.4's
  exactly-once ownership (§5.7.1), so claiming two costs no other lesson
  anything.

── ⊕ TWO SCIENCE CORRECTIONS, BOTH IN *Going further*, BOTH REPORTED ────

Standing authority for this pass: where Design is wrong and the author is sure,
correct it and report it. Both corrections are in one sentence-pair of the
stretch layer and both are Mide's to confirm. NOTES-B7 flag 15 asked for a
ruling on this paragraph, which is where they were found.

1. **"until it burst" → a plant cell does not burst.** Design wrote *"a cell
   that filled itself with dissolved sugar would draw water in by osmosis until
   it burst"*. A leaf cell has a cellulose cell wall. `b1-03`, approved and
   live, teaches the opposite in three places:
     * *"It holds the cell's shape and stops it bursting."*
     * *"Water floods into a plant cell and the wall is what pushes back —
       without it the cell would swell until it split."*
     * *"Put an animal cell in pure water and there is nothing to push back —
       it swells and splits."*
   A student who has done B1 would be reading a direct contradiction. Design's
   own next clause already has it right — *"a bag of syrup under pressure"* —
   so the sentence was arguing against itself. Corrected to swelling hard
   against the wall, which keeps the argument, keeps the rhetoric, and makes
   the glycogen parallel at the end of the paragraph sharper rather than
   weaker: an animal cell, with no wall, is the one that would burst.

2. **"by osmosis" / "osmotic pull" → KS3 does not teach osmosis by name.**
   Nothing in `ks3_data/` uses the word in student-facing prose; the B1 review
   pack records B1 L6 describing a contractile vacuole *"again avoiding osmosis
   by name"*, and `b4-05` teaches guard cells going turgid without it. Design's
   paragraph used the term twice, unglossed, in the one place NOTES-B7 flag 15
   itself identifies as *"the one place B7 assumes an idea the B-series has not
   formally taught"*. Rewritten as water being pulled in after the sugar, which
   is the mechanism in words a student your age already has. The idea is not
   dropped — only the untaught label.

Nothing else in the paragraph moves. If Mide wants osmosis named at KS3 that is
a key-stage ruling, not a b7-03 edit, and it would want `b1-06` and `b4-05`
changing with it.

── What could not be lifted, and why ────────────────────────────────────

1. **The two inline `<a href>`s in "Think again".** Design links the words
   *Food tests* and *Substance misuse and decisions* to `b3-02-food-tests.html`
   and `b6-03-substance-misuse-and-decisions.html`. Those hrefs are the design
   deck's flat filenames; the built site serves
   `/ks3/biology/nutrition-and-digestion/food-tests.html`, so carrying them
   verbatim would ship two 404s inside teaching prose. The WORDS are unchanged
   and both targets are carried as real edges — `food-tests` in `requires`,
   `substance-misuse-and-decisions` in `references` — which is Design's own
   endmatter and §4.6's single-source rule agreeing with each other.

2. **The method cards lose their numbered chips.** Design draws an accent
   `1`…`5` tile beside each of the five names; `r_rule` renders `term` + `gloss`
   and has no number slot. Document order carries the sequence, the names are
   unchanged, and card 1 still opens *"Two days in the dark"* — b6-03 gave up
   *"Question 1"*…*"Question 4"* in the identical component for the identical
   reason. ⚠️ Card 3's name keeps *"in a water bath"*; that is not decoration.

3. **`#s-method`'s `<h2>` level and the key fact's nesting.** The display line
   *"Five steps. None of them optional."* is authored as the rule block's
   `statement` and the renderer decides the tag. Design nests the KEY FACT
   inside the band panel on a `--ks3-card` ground; lifted to a top-level block
   it takes `band`, which is MRB-208's ruled identity for the box and what
   every other top-level key fact in the key stage uses. b6-03 resolved the
   identical arrangement the identical way. No word changes.

4. **Design draws THREE endmatter link cards; the engine emits two.** "Before
   this lesson" is `requires` and "Connects to" is `references` under
   `connects_heading`; "At GCSE this becomes" is `ks4_becomes`. All four links
   survive, in Design's grouping. `ks4_links` gives way to `ks4_becomes` —
   §4.8.1 D makes the two mutually exclusive.

5. **The fourth rail stop is Design's, and it stays.** ⊕ **REVERSED 18 Aug
   2026 (MRB-249).** This item used to read "One rail stop comes off — the
   defect B4 found on every page". Design draws FOUR stops and `#s-method`
   ticks on `s.everRan` (page line 381), which is the BENCH's predicate, one
   section to the left (page line 380); because `#s-method` is an eyebrow, a
   display line, five static cards and a key fact, with no control, no
   commitment and no field, the reading was that MRB-208's completion rule
   ruled it out, that `ks3_parity.check_rail_reachable` would fail it outright
   for carrying none of `_DONE_SIGNALS`, and that inventing a demand Design did
   not draw is closed to this build. So THREE stops shipped.

   That is overruled twice. MRB-205 binds and is not re-argued — Design draws,
   we render, nothing invented and nothing dropped, page wins over engine — and
   a stop that a gate could not express is a gate to fix, which is what
   rail-level mirror resolution in `wireRail`'s `paint()` now does. And
   Design's `isDone()` states the condition: it is rail-level and returns the
   identical expression for `#s-bench` and then for `#s-method`, because the
   five steps done properly are the payoff of having run it badly. The section
   holds no control because the bench already took the commitment. That is a
   MIRROR.

   So the stop is declared: anchor `s-method`, `mirrors: "s-bench"`,
   `done_when: "iodine_added"` — the bench's own predicate, named as borrowed,
   and gated by `check_rail_matches_design` against
   `docs/ks3/rail-manifest.md`. b5-06's `#s-designs`, b6-03's `#s-four`,
   b4-01's `#s-parts` and b3-02's `#s-limits` are restored the same way. The
   section keeps its anchor, as it always did.

⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026, AND RUNG 2 IS REPAIRED.
  rung 1 (recall): correct 11w against distractors of 9 / 8 / 11. Clean as
                   drawn, and untouched — its distractors already state wrong
                   RULES in the correct answer's own shape ("To kill the leaf
                   so…", "To sterilise the leaf so…").
  rung 2 (apply):  correct 17w against 17 / 18 / 15. It measured 17w against
                   5 / 5 / 6 as Design drew it — the widest tell in the unit,
                   and a student could have scored the rung without reading it.

  Mide ruled the CONSTRUCT rather than the instance: the correct answer states
  a RULE — subject, condition, consequence — so distractors that state
  one-clause wrong CONCLUSIONS make it longest by construction. Each of the
  three now states a WRONG RULE in the same shape, with the misconception as
  the consequence, and each is a belief students actually hold:
    A — *a leaf makes its starch and uses it within a day* (starch accumulates;
        this is the belief the whole destarching step exists to defeat).
    C — *iodine turns blue-black when it reaches the green pigment* (`PLANT-05`
        stated as a rule).
    D — *this leaf had light and it made starch* (one condition, one result, no
        comparison — the lesson's own point, offered as reasoning).
  **The correct option is unchanged, `answer: 1` is unchanged, the gate's
  threshold is unchanged, and all three of Design's corrections are unchanged
  and byte-identical** — each already answers the rule its distractor now
  states, which is itself evidence the beliefs were the right ones to pick.

✅ CLEARED BY MIDE — MRB-233 (3b), 31 Aug 2026. Flags 13 and 14 are CLOSED.
  This block used to open "⚑ For Mide's science gate" and ask for both. It is
  kept in place, and the two flags rewritten under their own numbers, because
  a future pass that reads them as still-open will go looking for a sign-off
  that has already happened — or worse, will "apply" wording that is already
  the approved wording and move bytes on a page nobody asked to change.
  * flag 13 — CONFIRMED against the technicians' version recorded in
    NOTES-B7 §3 flag 13. The method and its timings: destarch two days in the
    dark, boil in water about a minute, boil in ethanol in a water bath, dip
    in hot water, spread on a white tile, add iodine. `STEPS` below carries
    that order step for step, and the two timings that exist are both on it —
    `destarch` "Two days in a dark cupboard" and `boil` "About a minute in a
    beaker of boiling water". `soften` is "A few seconds", which the
    technicians' version leaves unnumbered and school practice agrees with.
    Nothing moved: the confirmation is that nothing needed to.
  * flag 14 — SIGNED OFF by Mide, who signs the risk assessments here. The
    wording below is the APPROVED wording, and it was already in the file —
    authored to flag 14 clause for clause and rendering on the live page. The
    ruling APPLIES it rather than changing it, so this lesson's student-facing
    bytes are unchanged by MRB-233.
  * flag 15 — *why starch and not glucose*. Two corrections above; the glycogen
    parallel is kept and `glycogen` appears nowhere else in KS3, which is the
    right place for it — the stretch layer is where a new name is allowed.
  * Rung 4's second criterion introduces **soda lime**, which appears nowhere
    else in `ks3_data/` yet. NOTES-B7 §1.1 gives it to b7-01's
    `reactant-remover` as a dial, and b7-01 is this lesson's first `requires`
    edge, so the assumption is sound in sequence — but it is an assumption
    across lessons and it is recorded rather than hidden.
"""

# ── the five steps (page lines 311–322, via extract_design_payload.js) ───
#
# Step `3b` is not a sixth step: it is the choice WITHIN step 3, and Design
# gives it its own row so that a student has to make it rather than inherit it.
# Its option ids are `bath` / `flame` rather than `yes` / `no`, which is why the
# safety branch is keyed `flame` and not `heat` — see `precedence` below.
STEPS = [
    {"id": "destarch", "num": "1", "title": "Destarch the plant",
     "detail": "Two days in a dark cupboard before the experiment begins.",
     "options": [{"id": "yes", "label": "Done"},
                 {"id": "no", "label": "Skipped"}]},

    {"id": "boil", "num": "2", "title": "Boil the leaf in water",
     "detail": "About a minute in a beaker of boiling water.",
     "options": [{"id": "yes", "label": "Done"},
                 {"id": "no", "label": "Skipped"}]},

    {"id": "ethanol", "num": "3", "title": "Boil in ethanol",
     "detail": "In a tube of ethanol, stood in hot water.",
     "options": [{"id": "yes", "label": "Done"},
                 {"id": "no", "label": "Skipped"}]},

    # ⚠️ SAFETY CONTROL. NOTES-B7 §1.3: "the only place in B7 where a wrong
    # choice ends the experiment rather than spoiling it". Design's own detail
    # line says so to the student without saying why yet — the verdict does
    # that.
    {"id": "heat", "num": "3b", "title": "How the ethanol is heated",
     "detail": "The choice that matters more than any other on this bench.",
     "options": [{"id": "bath", "label": "Water bath"},
                 {"id": "flame", "label": "Bunsen, directly"}]},

    {"id": "soften", "num": "4", "title": "Dip in hot water",
     "detail": "A few seconds, then spread flat on a white tile.",
     "options": [{"id": "yes", "label": "Done"},
                 {"id": "no", "label": "Skipped"}]},
]

# The opening state AND the state the reset button restores — Design's `FULL`
# (page line 324), authored rather than derived. It is content, not runtime
# state: it is the map behind the button labelled "Fresh leaf, full method",
# exactly as `leaf-tuner`'s `oak` is the map behind "set it to a real oak leaf"
# (schema §3). Unlike b7-02, this bench OPENS on the good state — the student
# breaks a working method rather than fixing a broken one, which is what makes
# every verdict a consequence of their own choice.
FULL = {"destarch": "yes", "boil": "yes", "ethanol": "yes",
        "heat": "bath", "soften": "yes"}

# ── the six outcomes (page lines 423–459) ───────────────────────────────
#
# Schema §4 names the fields `tag` / `head` / `why` / `conclude`; Design's own
# object calls them tag / title / body / conclusion. The schema wins on naming,
# the page wins on every word.
#
# ⚖️ `conclude` is the field that matters, and Design gives it its own rule and
# its own bold label on the page. Four of the six say some version of *no*, and
# the two that do not are the safety branch (which says the question does not
# arise) and the full method (which says yes, and then says why it is allowed
# to). Nothing here marks the student right or wrong — a bench shows a
# consequence, it does not award a tick (schema §0 rule 6).
VERDICTS = {
    # ① SAFETY. First, always. This branch is not about the quality of the
    # data and its own `why` says so — the practical has ended.
    "flame": {
        "tag": "Stop — the test never happened",
        "head": "The ethanol caught fire.",
        "why": "Ethanol boils at 78 °C and its vapour ignites readily. Held "
               "over a Bunsen it goes up, and the fire is at head height in a "
               "room full of people. This is the one mistake on this bench "
               "that is not about the quality of your data.",
        "conclude": "No. Stand the tube in hot water and let the water carry "
                    "the heat — the water bath is not fussiness, it is the "
                    "reason this practical is allowed in schools at all."},

    # ② RESULT-DESTROYING. No ethanol: the colour change is invisible under
    # the chlorophyll, so there is no reading at all.
    "ethanol": {
        "tag": "Result unreadable",
        "head": "A dark green leaf with iodine on it.",
        "why": "The chlorophyll is still in the leaf, so the leaf is green, "
               "the iodine is orange-brown, and any blue-black underneath is "
               "invisible against it. You have a stained green leaf and no "
               "information.",
        "conclude": "Nothing. Not a wrong answer — no answer, which is worse, "
                    "because a wrong answer at least tells you to look "
                    "again."},

    # ③ RESULT-DESTROYING, and this is where PLANT-06 dies. The student skips
    # the two days, gets a strong positive, and reads a verdict that says the
    # positive proves nothing. The register (docs/ks3/misconception-register.md)
    # names THIS block as the belief's `confronted_by` for exactly that reason:
    # it is killed by running it, not by being told.
    "destarch": {
        "tag": "No control",
        "head": "Blue-black everywhere — including under the foil.",
        "why": "The covered half went black too. The plant had been making "
               "starch for days before you covered anything, and that starch "
               "is still sitting in every leaf. Your foil changed today; the "
               "starch is older than that.",
        "conclude": "Nothing about light. The result is real and it is "
                    "unusable, because you cannot tell when the starch was "
                    "made. Destarch for two days and start again."},

    # ④ RESULT-OBSCURING. Cells alive and waxy, so the iodine goes in
    # unevenly — a pattern you cannot trust rather than no pattern at all.
    "boil": {
        "tag": "Result unreliable",
        "head": "Patchy, faint, and different every time.",
        "why": "The cells were never killed or opened up, so the iodine soaks "
               "in unevenly through a leaf that is still waxy and intact. "
               "Some patches go dark, some do not, and repeating it gives a "
               "different pattern.",
        "conclude": "Not safely. You cannot tell whether a pale patch means "
                    "no starch or just no iodine — which is exactly the "
                    "ambiguity the method exists to remove."},

    # ⑤ RESULT-OBSCURING, and the mildest of the five: the chemistry worked
    # and the damage is to the pattern, which is still what the experiment was
    # about. The only `conclude` on the bench that says "partly".
    "soften": {
        "tag": "Result partly readable",
        "head": "The leaf crumbled as you spread it.",
        "why": "Ethanol leaves the leaf brittle and shrivelled. It tore along "
               "the fold and part of the covered half is now in three pieces, "
               "so the boundary you were trying to look at is gone.",
        "conclude": "Partly. The chemistry worked and the fragments do show a "
                    "difference, but the pattern is what this experiment is "
                    "about, and you have damaged the pattern."},

    # ⑥ FALLBACK — nothing skipped, water bath. The covered half is the
    # control, and the last sentence is the lesson: the word "needed" has to be
    # earned. (Design's straight double quotes around "needed" are hers and are
    # kept; the rest of the payload uses curly.)
    "full": {
        "tag": "A result you can use",
        "head": "Blue-black in the exposed half. Orange-brown under the foil.",
        "why": "Both halves are on one leaf, so they shared the same water, "
               "temperature, carbon dioxide and age. Light is the only "
               "difference between them, and starch appeared only where light "
               "fell.",
        "conclude": "Yes: light is needed for photosynthesis in this plant. "
                    "The covered half is the control, and it is the only "
                    "reason that sentence is allowed to contain the word "
                    "\"needed\"."},
}

# ── the five method cards (page lines 326–332) ──────────────────────────
#
# `r_rule` reads `term` + `gloss`; Design's `name` + `why`. The numbered chips
# are lost — "What could not be lifted" 2.
#
# ⚠️ Card 3 carries safety string #2 of five. It is byte-identical, including
# "78 °C", "catches fire easily" and "never over a flame". Do not compress it
# into the foot line; a student reading the method reads this one and may never
# reach the foot line at all.
METHOD_CARDS = [
    {"term": "Destarch the plant",
     "gloss": "Two days in the dark with no light to photosynthesise by. The "
              "plant respires away the starch it was holding, so anything "
              "found afterwards was made during your experiment. This is the "
              "control, and without it no result means anything."},

    {"term": "Boil the leaf in water",
     "gloss": "Kills the cells so nothing changes while you work, and breaks "
              "down the membranes so that iodine can get into the cells "
              "later. It also softens the waxy surface."},

    {"term": "Boil in ethanol, in a water bath",
     "gloss": "Ethanol dissolves chlorophyll, so the green drains out and a "
              "colour change becomes visible. Ethanol boils at 78 °C and its "
              "vapour catches fire easily, so it is heated by standing the "
              "tube in hot water — never over a flame."},

    {"term": "Dip in hot water",
     "gloss": "Ethanol leaves the leaf pale, brittle and shrivelled. A few "
              "seconds in hot water softens it enough to spread flat without "
              "it crumbling."},

    {"term": "Spread out and add iodine",
     "gloss": "On a white tile, so the colour is read against a neutral "
              "background. Blue-black where starch is present, orange-brown "
              "where it is not."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 141 character for character.
    "slug":        "testing-a-leaf-for-starch",
    "title":       "Testing a leaf for starch",
    "discipline":  "biology",
    "unit":        "photosynthesis",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # WS anchors per §5.7.1 and NO subject statement — see the docstring. All
    # three PHOT statements stay with b7-01, b7-02 and b7-04.
    "covers":      ["KS3.WS.EXP.04", "KS3.WS.EXP.03"],
    # Named and used but not taught here. The bench's full-method verdict
    # concludes that light is needed for photosynthesis, and *Going further*
    # argues about where the day's glucose goes — both are b7-01's to own
    # (PHOT.01 and the leaf half of NUT.06). This lesson borrows them as the
    # thing the practical is evidence FOR.
    "touches":     ["KS3.B.PHOT.01", "KS3.B.NUT.06"],
    "beyond_statutory": False,
    # Level 1 on both, and deliberately. Working Scientifically is not a thread
    # (§4.7) — it is the separate axis this lesson is anchored on. What is left
    # is an encounter with a colour-change test and with leaf cells, not a
    # development of either. b3-02, the other colour-change practical, declares
    # the same pair at the same level.
    "threads":     [{"id": "substances-and-reactions", "level": 1},
                    {"id": "cells-and-systems", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design draws "Before this lesson" (b7-01, b3-02) and "Connects to"
    # (b7-02, b6-03). NOTES-B7 §3 confirms all four exist; none is forward.
    #
    # ⚠️ b3-02 and b6-03 are also the two lessons the "Think again" prose names
    # by title. Design links them inline; the words stay and the LINKS live
    # here — "What could not be lifted" 1, and §4.6's single-source rule, which
    # says a pointer at another lesson is an edge rather than a repeat.
    "requires":    ["the-photosynthesis-reaction",
                    {"unit": "B3", "lesson": "food-tests"}],
    "assumes":     [],
    "references":  ["leaves-built-for-the-job",
                    {"unit": "B6", "lesson": "substance-misuse-and-decisions",
                     "why": "Where the same fault — a measurement with nothing "
                            "to compare it against — is met in evidence about "
                            "people rather than in a leaf."}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Required practical work on photosynthesis, limiting "
                   "factors, and writing a method that another person could "
                   "follow exactly.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Four preparation steps before a single drop of iodine "
                    "touches the leaf. Every one of them exists because "
                    "somebody once left it out and got a result they could not "
                    "read.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-method` is the third: no control of
    # its own, so it mirrors `s-bench` and ticks on the bench's predicate — see
    # "What could not be lifted" 5. `short` and `label` are Design's own
    # `RAIL_SHORT` and `RAIL` strings (page lines 303–309).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Straight on",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.everRan` — the stop ticks when the
        # iodine has actually been added at least once, not when a step has
        # been toggled. Toggling is free; committing to a run is the act the
        # bench exists for.
        {"anchor": "s-bench", "short": "BENCH", "label": "Run it badly",
         "done_when": "iodine_added"},
        {"anchor": "s-method", "short": "METHOD", "label": "Five steps",
         "mirrors": "s-bench", "done_when": "iodine_added"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3). The reveal
    # names option B and then does the thing that makes this a hook rather than
    # a quiz: it draws out the consequence the student did not ask for — the
    # chlorophyll is gone BEFORE the iodine arrives, which is the whole of
    # PLANT-05 four sections early.
    "phenomenon": {
        "kind": "narrative",
        "title": "Put iodine straight onto a green leaf and you learn nothing.",
        "prompt": "The leaf is green, the iodine is orange-brown, and whatever "
                  "happens underneath is invisible. It is also waterproof on "
                  "both surfaces and its cells are alive and still working. "
                  "Three problems, and each one has its own step in the "
                  "method.",
        "commit": "Why is the leaf boiled in ethanol before the iodine goes "
                  "on?",
        "options": [
            "To kill the leaf so it stops photosynthesising",
            "To dissolve the chlorophyll out so a colour change shows",
            "To dissolve the starch so the iodine can reach it",
            "To sterilise it before the test",
        ],
        "reveal": "To dissolve the chlorophyll out, so the leaf goes pale and "
                  "any colour change can actually be seen. Notice what that "
                  "means: by the time the iodine arrives, the chlorophyll has "
                  "already been poured down the sink. Whatever turns "
                  "blue-black, it is not that.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ IDS ARE PRE-ALLOCATED, not chosen here: schema §6 gives this lesson
    # `PLANT-05` and `PLANT-06` and reserves `PLANT-11` as a spare. **The spare
    # is deliberately left unused** — this page confronts two beliefs and only
    # two, and an unclaimed spare stays permanently unused like `DRUG-07` and
    # `REPRO-17`/`20`/`21`/`23`. Both statements are lifted byte-identical from
    # `docs/ks3/misconception-register.md` lines 600–601.
    #
    # `elicited_by` and `confronted_by` are the register's own values and both
    # name section anchors this page emits, which is what verify_ks3.py's
    # MRB-244 check resolves against (`id="…"` or `data-activity="…"` on the
    # BUILT page).
    #
    # ⚖️ PLANT-06 is the only entry in the family confronted somewhere other
    # than `s-think`, and the register says why in its own words: the
    # method-breaker lets the student skip the destarching and then read a
    # verdict saying the positive result proves nothing. The belief is killed
    # by running it. `s-think` still elicits it — the second confrontation
    # quotes it — but the block that KILLS it is the bench, and the register's
    # rule is that `confronted_by` names the killer.
    "misconceptions": [
        {"id": "PLANT-05",
         "statement": "The leaf goes black because the iodine reacts with the "
                      "chlorophyll.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
        {"id": "PLANT-06",
         "statement": "Just pick a leaf and test it — the destarching is a "
                      "waste of two days.",
         "elicited_by": "s-think",
         "confronted_by": "s-bench"},
    ],

    # Design draws no keyword block anywhere in B7, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list. Every definition is
    # authored, and every one is written to say what the thing IS and what
    # happens in it — `destarch` is defined by the two days and their
    # consequence, not by "so that you can prove something".
    "vocabulary": [
        {"term": "starch",
         "definition": "An insoluble carbohydrate made of many glucose "
                       "molecules joined together.",
         "note": "The form a plant stores its glucose in."},
        {"term": "iodine solution",
         "definition": "A test for starch: it turns blue-black where starch "
                       "is present and stays orange-brown where it is not.",
         "note": "It says nothing about anything else in the leaf."},
        {"term": "destarching",
         "definition": "Leaving a whole plant in the dark for about two days, "
                       "so the starch it was holding is used up.",
         "note": "Anything found afterwards was made during the experiment."},
        {"term": "ethanol",
         "definition": "A liquid that dissolves chlorophyll, leaving the leaf "
                       "pale.",
         "note": "It boils at 78 °C and catches fire easily, so it is heated "
                 "in a water bath and never over a flame."},
        {"term": "control",
         "definition": "The part of an investigation that everything else is "
                       "compared against.",
         "note": "Here it is the destarched plant, and the half of the leaf "
                 "under the foil."},
    ],

    # ── figures (§7 of the schema) ──────────────────────────────────────────
    # ⚑ EMPTY IS MEASURED, NOT AN OMISSION. This page draws no `<img>`, no
    # `<figure>` and no placeholder, and its foot line declares no slot.
    # NOTES-B7 flag 12 names a leaf cross-section as the obvious candidate for
    # the unit and records that Design taught the internal structure in b7-02's
    # five cards instead. §4.10 allows an empty `figures` for a lesson carried
    # by its interactives. Nothing is invented to fill the gap, and the flag is
    # Mide's to rule on rather than this pass's to close.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b7/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so `practical` is MEASURED from her own markup —
        # schema §0 rule 2 — and not inherited from the hook above it.
        #
        # ⚠️ THE GROUND IS INK. `.ks3-dark p` is (0,1,1) and beats a bare
        # instrument class at (0,1,0); on B4 that shipped a chain label at
        # 1.21:1 past a green build. Every text rule the renderer adds for this
        # instrument must out-specify it. That is the engine pass's problem and
        # it is recorded here because this payload is what feeds it.
        #
        # ⛔ NO RUNTIME STATE IS AUTHORED (schema §0 rule 3). NOTES-B7 §1.3
        # lists `picks` and `ran` in its payload; both are the runtime's, not
        # content's, and a key with no read site fails ks3_key_audit.py under
        # R5. The renderer initialises its own state from `full`.
        {"type": "method-breaker", "id": "run-it-badly", "anchor": "s-bench",
         "demand": "investigate",
         "targets": "PLANT-06",
         "eyebrow": "At the bench · leave a step out and see",
         "heading": "Run the test badly on purpose",
         "prompt": "One leaf from a plant that has been in bright light all "
                   "day, half of it covered with foil. Switch any step off, "
                   "choose how you heat the ethanol, then add the iodine and "
                   "read what you get.",

         "steps": STEPS,
         "full": FULL,
         "verdicts": VERDICTS,

         # ⚖️ FAULT PRECEDENCE, AS DATA. Schema §4 calls the order load-bearing
         # and it is: report "the leaf crumbled" ahead of "you skipped the
         # destarching" and the bench teaches that a torn leaf and an
         # undatable result are the same size of mistake. Safety first, then
         # the two that DESTROY the result, then the two that only OBSCURE it;
         # `full` is the fallback when no entry matches.
         #
         # A branch id that is a STEP id fires when that step is skipped
         # (`picks[id] == "no"`). `flame` is the exception and is named for an
         # OPTION id rather than a step id, deliberately: `heat` is never
         # "skipped", it is answered one of two ways, and naming the branch
         # after the wrong answer keeps the rule "id names the fault" true for
         # all five. It fires on ethanol used AND heated over a flame — skip
         # the ethanol and there is no fire to have, which is why the `ethanol`
         # row dims the `heat` row on Design's own page (page line 509).
         "precedence": ["flame", "ethanol", "destarch", "boil", "soften"],

         # Design's mono counter, top-right of the block head. Three states,
         # not a count of a fixed total, so it cannot use `head_counter`'s
         # `{n} of N` shape — see the report.
         "progress": {"idle": "not run yet",
                      "full": "full method",
                      "one": "{n} step skipped",
                      "many": "{n} steps skipped"},

         "run_label": "Add the iodine",
         "run_done_label": "Iodine added",
         "reset_label": "Fresh leaf, full method",
         # Design gives the conclusion its own rule and its own bold label, and
         # NOTES-B7 §1.3 calls it "the part that matters". It is authored
         # rather than hard-coded in the renderer because it is the question
         # the whole lesson asks.
         "conclude_label": "Can you conclude anything?"},

        # #s-method — the band panel. Rail stop 3, mirroring `s-bench`; see
        # "What could not be lifted" 5. `rule` is the component: band ground, 3px ink border, an
        # accent-text eyebrow and a display statement, then a card list —
        # Design's markup (page lines 148–160) minus the number chips.
        {"type": "rule", "anchor": "s-method",
         "eyebrow": "The method, and why each step is in it",
         "statement": "Five steps. None of them optional.",
         "cards": METHOD_CARDS},

        # Design nests this inside `#s-method`; `r_rule` has no nested key-fact
        # slot (only `r_comparison` does), so it renders directly under the
        # panel in document order, on the band ground every other top-level key
        # fact in the key stage takes. The words and the order are unchanged.
        {"type": "key-fact", "ref": "iodine-turns-blue-black"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "PLANT-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "iodine-turns-blue-black",
         "text": "Iodine solution turns blue-black in the presence of starch "
                 "and stays orange-brown without it. A leaf must be destarched "
                 "first, then killed, decolourised and softened, or the result "
                 "cannot be read or trusted.",
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
        # (Build-contract R1 makes `#s-think` a `predict` in B2, C1 and C2
        # because on THOSE pages it gates a reveal behind a commitment. This
        # page's is static markup, like B1's, B4's, B5's and B6's, so it stays
        # a confrontation. Same rule, different block.)
        #
        # ⚠️ Both bodies lose an inline `<a href>` and keep every word — "What
        # could not be lifted" 1. The `<em>` emphasis is kept; `rich()` carries
        # it, and in both cases it is doing work: "it is *the control*" is the
        # sentence the whole lesson turns on, and "*no comparison group*" is
        # the name of a fault the student already owns from b6-03.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "PLANT-05",
         "statements": [
             # ⚖️ PLANT-05 dies on a timing argument, not on an assertion: the
             # chlorophyll left in step 3 and the iodine does not arrive until
             # step 5. Then two observations a student can check — potato and
             # bread go blue-black with no chlorophyll ever present, and the
             # white parts of a variegated leaf stay orange-brown, which is the
             # exact opposite of what the belief predicts.
             {"quote": "The leaf goes black because the iodine reacts with the "
                       "chlorophyll.",
              "body": ["The chlorophyll is not there. It was dissolved out "
                       "into the ethanol in step 3, which is the step that "
                       "turns the ethanol green and the leaf pale, and the "
                       "iodine does not go on until step 5 — by which time the "
                       "green pigment is in a beaker on the other side of the "
                       "bench. Two more observations finish the argument. A "
                       "slice of potato has no chlorophyll and never has had, "
                       "and iodine turns it blue-black instantly; so does a "
                       "piece of bread. And the white parts of a variegated "
                       "leaf, which have no chlorophyll to react with, stay "
                       "orange-brown when the green parts go black — the "
                       "opposite of what this idea predicts. Iodine is a test "
                       "for starch, nothing else, and that is why it is used "
                       "identically in Food tests on food that was never "
                       "green."]},
             # PLANT-06 is ELICITED here and killed at the bench — see the
             # misconceptions note. This paragraph names the fault; the
             # instrument makes the student meet it.
             {"quote": "Just pick a leaf and test it — the destarching is a "
                       "waste of two days.",
              "body": ["Then a positive result proves nothing, because you "
                       "cannot tell whether the starch was made today under "
                       "the conditions you were testing or last Tuesday in "
                       "ordinary daylight. Starch is the storage form: a leaf "
                       "accumulates it over days and holds onto it. "
                       "Destarching — the whole plant in a dark cupboard for "
                       "two days, respiring away its store with no light to "
                       "replace it — is not preparation, it is <em>the "
                       "control</em>. It is what lets you say the starch you "
                       "found was made during the experiment. This is exactly "
                       "the fault you met as <em>no comparison group</em> in "
                       "Substance misuse and decisions, wearing different "
                       "clothes: a measurement with nothing to compare it "
                       "against is not a result."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026. Rung 1 is clean as drawn and
    # untouched (11w against 9 / 8 / 11). Rung 2's three distractors are
    # rewritten to state WRONG RULES in the correct answer's own shape; correct
    # option, `answer: 1`, all three corrections and the gate's threshold are
    # unchanged, and it now measures 17w against 17 / 18 / 15. Full reasoning
    # and the three beliefs are in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Why that step",
            "q": "What is the purpose of boiling the leaf in ethanol?",
            "options": [
                "To kill the leaf so no more starch is made",
                "To dissolve the starch out of the cells",
                "To remove the chlorophyll so a colour change can be seen",
                "To sterilise the leaf so bacteria do not affect the result",
            ],
            "answer": 2,
            "feedback": {
                0: "The boiling water in step 2 has already done that. Ethanol "
                   "is there for the colour.",
                1: "That would destroy the thing you are testing for. Starch "
                   "is insoluble and stays exactly where it was.",
                3: "Nothing in this practical depends on sterility. The "
                   "problem being solved is that green leaves hide colour "
                   "changes.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A leaf is picked straight from a plant on a windowsill, "
                 "tested properly, and goes blue-black. What has been shown?",
            # ⊕ MRB-177, 17 Aug 2026. Options 0, 2 and 3 are rewritten; option
            # 1 is Design's, byte-identical. Each distractor now states the
            # wrong rule a student would have to believe to pick it.
            "options": [
                "That the plant photosynthesised today, because a leaf makes "
                "its starch and uses it within a day",
                "That the leaf contains chlorophyll, since iodine turns "
                "blue-black when it reaches the green pigment in a leaf",
                "That light is needed for photosynthesis, because this leaf "
                "had light and it made starch",
                "Almost nothing — without destarching first, there is no way "
                "to know when the starch was made",
            ],
            "answer": 3,
            # All three are Design's own corrections, byte-identical. Each
            # already denies the rule its rewritten distractor now states,
            # which is why the rewrite needed no new feedback: 0's "Starch
            # accumulates and stays put" answers "uses it within a day", 2
            # answers the chlorophyll rule directly, and 3 answers reasoning
            # from one leaf under one condition.
            "feedback": {
                0: "Or last week. Starch accumulates and stays put, so a "
                   "positive result on a plant that was never destarched "
                   "cannot be dated.",
                1: "Iodine says nothing about chlorophyll, which had been "
                   "dissolved away before the iodine was added.",
                2: "Nothing was covered up and nothing was compared. One leaf "
                   "under one condition cannot show that anything was needed.",
            }},
        # ⚠️ SAFETY, string #4 of five. The question REQUIRES the safety point
        # and criterion 4 names both halves of it — the water bath and the
        # flammability. Neither the demand nor the criterion is optional
        # phrasing; a method written without them does not meet this rung.
        "explain": {
            "title": "Rung 3 · Write the method",
            "q": "Write the method for testing a leaf for starch as "
                 "instructions someone else could follow, giving a reason for "
                 "each step. Include the safety point.",
            "field_label": "Your method",
            "placeholder": "First, destarch the plant by…",
            "success": [
                "Destarch the whole plant in the dark for about two days, and "
                "says this is so any starch found was made during the "
                "experiment.",
                "Boil the leaf in water, and says this kills the cells and "
                "makes them permeable to iodine.",
                "Boil in ethanol, and says this removes the chlorophyll so the "
                "colour change can be seen.",
                "Says the ethanol is heated in a water bath because it is "
                "highly flammable — no naked flame.",
                "Dip in hot water to soften, spread on a white tile, add "
                "iodine; blue-black means starch, orange-brown means none.",
            ]},
        # ⚑ Criterion 2 introduces soda lime, which no other KS3 lesson on
        # disk mentions yet. NOTES-B7 §1.1 gives it to b7-01's dial, and b7-01
        # is this lesson's first `requires` edge — recorded in the docstring so
        # the dependency is visible rather than assumed.
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Design an investigation using this test to show that carbon "
                 "dioxide is needed for photosynthesis. Say what your two "
                 "set-ups are, what you keep the same, and what result would "
                 "support your hypothesis.",
            "field_label": "Your design",
            "placeholder": "I would take two destarched plants…",
            "success": [
                "Starts with destarched plants, and says why.",
                "Puts one plant in a sealed container with soda lime to absorb "
                "the carbon dioxide, and one in a sealed container without it.",
                "Keeps light, temperature, water and the type of plant the "
                "same in both.",
                "Leaves both in bright light for the same length of time, then "
                "tests a leaf from each in the same way.",
                "States the result that would support the hypothesis: "
                "blue-black from the plant with carbon dioxide, orange-brown "
                "from the one without.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # ⚠️ SAFETY, string #1 of five, and it is the LAST SENTENCE of the thing a
    # student photographs. That placement is Design's and it is right: the note
    # is the method in one paragraph, and the last thing it says is the one
    # thing that must not be got wrong. Byte-identical, and it is never merged
    # into the foot line.
    "key_note": "Destarch the plant in the dark for two days. Boil the leaf in "
                "water to kill it and make it permeable, boil it in ethanol in "
                "a water bath to remove the chlorophyll, dip it in hot water "
                "to soften it, spread it on a white tile and add iodine. "
                "Blue-black means starch; orange-brown means none. Never heat "
                "ethanol over a naked flame.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⊕ TWO SCIENCE CORRECTIONS LIVE IN THIS PARAGRAPH, both in the docstring
    # and both on Mide's gate:
    #   * "would draw water in by osmosis until it burst" → a walled plant cell
    #     does not burst, and b1-03 teaches that it does not. Now: pulls water
    #     in after it and swells hard against its wall, which is what Design's
    #     own next clause ("a bag of syrup under pressure") already said.
    #   * "exerts no osmotic pull at all" → KS3 does not name osmosis anywhere,
    #     by ruling. Now: "pulls in no water at all". The idea is kept; the
    #     untaught label is not.
    # Every other word is Design's, including the glycogen parallel — which the
    # first correction sharpens, because an animal cell has no wall and IS the
    # one that would burst.
    "stretch": [
        {"type": "explainer", "id": "why-starch-and-not-glucose",
         "text": "Photosynthesis makes glucose, so why does the test look for "
                 "starch? Because glucose is soluble, and a cell that filled "
                 "itself with dissolved sugar would pull water in after it and "
                 "swell hard against its wall — a leaf storing its day's "
                 "production as glucose would be a bag of syrup under "
                 "pressure. Starch is hundreds of glucose molecules joined "
                 "into one insoluble molecule: it sits in the chloroplast as a "
                 "grain, takes up little room, pulls in no water at all, and "
                 "can be broken back down to glucose when the plant needs it "
                 "at night. That is also why it stays put long enough to be "
                 "found the next morning, which is the only reason this "
                 "practical works. The same argument explains why animals "
                 "store glucose as glycogen rather than as sugar in the "
                 "blood."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own flagship, which is a real
    # destination on the page it is printed on (§4.8.1 C), and its question is
    # the bench's question — "whether your result actually shows what you
    # think" is `conclude_label` in the student's own words.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check whether your result actually shows what "
                      "you think?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⚠️⚠️ SAFETY, string #3 of five, AND THE ONLY `safety_note` IN B7.
    #
    # `safety_note`, NOT `convention_note` — the split matters and this is the
    # side of it that has never come up before in the B-series' recent units.
    # b5-06, b6-03, b3-05 and b4-01 all routed their foot line through
    # `convention_note` because none of them was a safety instruction: they
    # were declarations about a generalised flower, invented claims, or figures
    # not yet drawn. This one is a list of laboratory hazards with a named
    # control for each, and `build_ks3.py` gives `safety_note` its own class
    # (`ks3-legal ks3-safety`) for exactly this. §8.10 keeps it small, at the
    # bottom edge, never a callout — which is where Design draws it.
    #
    # ⛔ APPROVED WORDING — Mide signed it off 31 Aug 2026 (MRB-233 · 3b), and
    # it is STILL not to be edited without him. The line used to read "LIFTED
    # BYTE-IDENTICAL AND NOT TO BE EDITED WITHOUT MIDE", which was true while
    # the wording was authored-but-unsigned; it is now the wording the person
    # who signs this school's risk assessments has approved, which raises the
    # bar on changing it rather than lowering it. Every clause
    # is load-bearing: the bench is not a risk assessment; ethanol is heated
    # only in a water bath AND there is no naked flame in the ROOM (not merely
    # under the tube — a neighbouring group's Bunsen is the hazard); iodine
    # stains and irritates skin and eyes; boiling water and hot apparatus need
    # eye protection and a teacher present; and the school's own risk
    # assessment is what actually governs. MRB-233, NOTES-B7 flag 14.
    "safety_note": "The bench is a simulation of the practical, not a "
                   "substitute for it, and it is not a risk assessment. In a "
                   "real laboratory: ethanol is highly flammable and is heated "
                   "only in a water bath with no naked flame in the room; "
                   "iodine solution stains and irritates skin and eyes; "
                   "boiling water and hot apparatus need eye protection and a "
                   "teacher present. Follow your school's own risk assessment.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `experimental-skills-and-investigations` is the anchor's own strand — a
    # method, its apparatus, and health and safety (`KS3.WS.EXP.04`), plus the
    # control variable rung 4 designs around (`KS3.WS.EXP.03`).
    # `analysis-and-evaluation` — every one of the six verdicts ends on what
    # the result licenses, and rung 2 is that question with nothing else in it.
    # `scientific-attitudes` — `KS3.WS.ATT.03`, evaluate risks: the bench's
    # first branch is a hazard, not a data fault, and the student meets it by
    # choosing it.
    #
    # ⚑ SPELLING — the commander's B7 ruling, and a divergence reported rather
    # than resolved here. The roster is CLOSED at four and nothing validates
    # it, so a typo ships silently. This file takes `experimental-skills`, the
    # ruled spelling and the one architecture.md §5.7 lists.
    #
    # On disk today it is the MINORITY spelling: ten lessons use
    # `experimental-skills-and-investigations` — `statutory-register.md`'s own
    # instruction, *"Tag as `ws: ["experimental-skills-and-investigations"]`"* —
    # and only `b6/lesson_03` uses the short one. Two spellings of one strand
    # break a strand-coverage audit the day someone writes it, and §5.7.4
    # requires that audit. Normalising the tree is the commander's call, not an
    # authoring pass's; B7 is at least internally consistent either way.
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation",
           "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
