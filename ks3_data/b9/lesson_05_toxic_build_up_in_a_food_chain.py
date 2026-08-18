"""B9 L5 — Toxic build-up in a food chain (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b9/b9-05-toxic-build-up-in-a-food-chain.dc.html` (575 lines), her
author's notes `docs/ks3/design-reference/b9/NOTES-B9.md`, and the B9 payload schema
`docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md` §0, §1, §2, §4, §9, §11, §12 and §14,
under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the six figures ruled below and the two items under "What could not be
lifted". The three persistence settings, the six chain rows, the three
condition cards, both marked rungs and both self-marked rungs came out of the
page's own `CHEMS`, `LEVELS`, `COND_CARDS`, `RUNGS` and `SELF_RUNGS` arrays,
not off a keyboard.

── ⊕ RULING 1 — THE INSTRUMENT WINS, AND THE PROSE IS WHAT CHANGES ───────

Design's bench has SIX rows — lake water, algae, water fleas, minnows, perch,
ospreys — and the persistent chemical multiplies ×10 per step from 0.003 ppm:

    0.0030 → 0.030 → 0.300 → 3.0 → 30 → 300 ppm

Five steps, so the ospreys carry **300 ppm, a hundred thousand times** the
concentration in the water, and the harmful verdict computes
`round(300 / 0.003) = 100,000` from the bench's own state.

Design's prose, her rung 3 and NOTES-B9 §1.5 and flag 13 all describe a
FIVE-row chain running 0.003 → 25 ppm, "roughly ten thousand times". They are
wrong; the bench is right, and the bench is what has been built.

⚖️ **THE BENCH IS NOT TRIMMED TO FIVE ROWS.** Dropping a row would break the
×1 control — the flat line that is the whole comparison — before it fixed any
prose, and an instrument that contradicts its own page teaches a student that
one of the two is lying. Here it is the page. So the prose moves. Every figure
that changed, before and after, on the record:

  1. **The bench eyebrow.**
         Design:  At the bench · one lake, five levels
         Built:   At the bench · one lake, six levels
     `LEVELS` has six entries; the eyebrow counted the organisms and forgot
     the water they stand in, which is level one and the source of everything
     above it.

  2. **The hook's water concentration.**
         Design:  washes into a lake at 0.0003 parts per million — three
                  ten-thousandths of a milligram in a litre
         Built:   washes into a lake at 0.003 parts per million — three
                  thousandths of a milligram in a litre
     The bench starts at 0.003 ppm on all three settings and rung 3 already
     said 0.003; the hook was the only place in the lesson carrying a third
     figure. The gloss moves with it — 1 ppm in water is 1 mg per litre, so
     0.003 ppm is three thousandths of a milligram in a litre.

  3. **The hook's osprey concentration.**
         Design:  the pesticide in their bodies measures 25 parts per million
         Built:   the pesticide in their bodies measures 300 parts per million

  4. **The hook's commit question.**
         Design:  How did the concentration rise by tens of thousands of times?
         Built:   How did the concentration rise by a hundred thousand times?

  5. **The hook's reveal.**
         Design:  Do that four times up a chain and the concentration climbs
                  by four factors of ten.
         Built:   Do that five times up a chain and the concentration climbs
                  by five factors of ten.
     Six rows is water plus five feeding steps, and 10**5 is the 100,000.

  6. **Rung 3's question.**
         Design:  is found at 25 ppm in the ospreys nesting there. Explain how
                  the concentration rose by roughly ten thousand times
         Built:   is found at 300 ppm in the ospreys nesting there. Explain how
                  the concentration rose by roughly a hundred thousand times
     Rung 3 is the rung that asks the student to explain the number the bench
     has just shown them. It was asking about a number the bench never prints.

Nothing else moved. The KEY FACT, the key note, the three condition cards, both
`#s-think` bodies, the *Going further* paragraph and the legal line carry no
figure that the bench contradicts, and all are byte-identical.

⚑ **FOR MIDE, and it is the same flag NOTES-B9 13 raises.** At `harm = 1 ppm`
the six-row persistent chain flags THREE rows as *above the level that causes
harm* — minnows at 3.0, perch at 30, ospreys at 300 — and the KEY FACT says
*the animals at the top are harmed first*. The two are reconcilable (the key
fact is about the order harm APPEARS over years of exposure, not about which
rows sit above a line on a finished chain) but they are not obviously so on
screen. The threshold is Design's `HARM = 1.0` and it has not been touched:
moving it is a science decision and this pass does not have that gate. Raising
it to 10 would flag perch and ospreys only; raising it to 100 would flag the
ospreys alone and make the bench say exactly what the key fact says.

── ⊕ RULING 2 — FAT-SOLUBILITY, NOT WATER-SOLUBILITY, IS THE MECHANISM ───

A fat-soluble substance is stored in body fat and is not excreted, so it
accumulates over a lifetime and is passed on concentrated when that animal is
eaten. A water-soluble substance is filtered out in urine about as fast as it
arrives, which is exactly why the ×1 setting stays flat.

This is already live as a WRITTEN DISTRACTOR — rung 1's water-soluble option,
with Design's own correction saying that dissolving in water is *the property
that stops accumulation* — so a body that said otherwise would contradict its
own quiz on the same screen. Every label, note, verdict and body sentence here
keeps it: the settings are `persistent` (*Persistent, fat-soluble*, ×10),
`partial` (*Slowly broken down*, ×3) and `soluble` (*Water-soluble, excreted*,
×1); the first card in `#s-two` says the chemical is not excreted *usually
because it dissolves in fat rather than water*; `#s-think`'s second body closes
on *how long does it last and does it dissolve in fat*; and *Going further*
names *persistent and fat-soluble* as "the two properties on the bench above".

── The instrument: a persistence dial, and never a toxicity dial ─────────

`#s-bench` is `bioaccumulation`, on `ks3-block ks3-dark ks3-practical` (page
line 105), so `practical` is MEASURED from Design's own markup rather than
inferred from the kind name — payload schema §0 rule 2, and contract §4 records
that B1 got two of six wrong by inferring it.

⚖️ **THE ×1 SETTING IS THE CONTROL AND IT IS NOT THE BORING ONE.** It produces
a flat line and its verdict is the only one of the three that computes no
number — the chemical is excreted as fast as it arrives, so no organism holds
more than any other. That flat line is what proves the mechanism is
PERSISTENCE and not TOXICITY, which is the claim rung 1 marks and `#s-think`
confronts. Nothing on the bench varies how poisonous the chemical is. The
renderer refuses a payload with none, or with two, and `ks3_parity`'s
`b9-chem-control` drive runs the control in its own document rather than as a
branch of `b9-chain-poisoned`, because a control measured in the same document
as the treatment is not a control.

⚠️ **FOUR-BRANCH NUMBER FORMATTING, REPRODUCED EXACTLY** (page line 449):
`≥10 → 0 dp`, `≥1 → 1 dp`, `≥0.01 → 3 dp`, else `4 dp`. It is what puts
`0.0030` and `300` in the same column without either reading as noise, and the
threshold is per VALUE, not per setting. `build_ks3._b9_ppm` and `ks3.js`'s
`b9Ppm` are one rule in two languages. Verified at every row of every setting:

    persistent ×10   0.0030  0.030  0.300  3.0   30    300   → harmful, 100,000×
    partial    ×3    0.0030  0.0090 0.027  0.081 0.243 0.729 → below harm
    soluble    ×1    0.0030  0.0030 0.0030 0.0030 0.0030 0.0030 → flat

The middle setting is what stops the lesson reading as a binary: it accumulates
and still does not reach harm over this chain, and its verdict says so —
*slower breakdown is not the same as no accumulation*.

⚖️ **THE LAKE WATER IS DRAWN AT THE BOTTOM.** The level list is
`flex-direction: column-reverse`, exactly as b9-01's chain is, so a student
reads the chain the way the contamination travels. There is a parity row on it
and a drive that measures the two bounding rectangles.

── FOUR rail stops, and the band stop is a MIRROR (MRB-249) ──────────────

Design draws four (page lines 315–321) and her `isDone()` gives `s-two` the
BENCH's predicate, character for character, one section to the right:

    if (id === 's-bench') return s.everTopped;
    if (id === 's-two')   return s.everTopped;      // page line 393

`#s-two` is an eyebrow, a display statement, three static cards and a key fact:
no control, no commitment, no field, no reveal. Payload schema §4 originally
told this unit to author three stops and drop it. That instruction is REVERSED
— MRB-205 binds and is not re-argued: Design draws, we render, and the page
wins over the engine. A band holding the two conditions the whole lesson turns
on is teaching, not a spacer, and it is the PAYOFF of the instrument beside it:
it carries no control precisely because the bench has already taken the
student's commitment.

So the stop is declared with `mirrors: "s-bench"` and the same `done_when`,
`wireRail`'s `paint()` resolves it at rail level where Design resolves it,
nothing ticks on load, and `ks3_parity.check_rail_matches_design` gates the
built rail against `docs/ks3/rail-manifest.md`, whose row for this page reads
`s-hook s-bench s-two s-ladder | s-two=s-bench`.

`#s-think` and `#s-keynote` are on no rail, and that is correct — neither is a
stop on Design's own page.

── `#s-think` is a `confrontation`, measured, not assumed ────────────────

Static markup: `ks3-mis-head`, a `ks3-mis-quote`, a body, a `border-top` rule, a
second quote and a second body. **No `ks3-options`, no `sc-if` reveal, no
button, no state.** Contract R1 makes `#s-think` a `predict` only where it asks
for a commitment and then reveals; this asks for none, so it is a
`confrontation`, it emits no `data-stage-done`, and it is not a rail stop.

── What could not be lifted byte-identical, and why ─────────────────────

Neither is a science word. Both are the same defect: a build-internal
identifier printed where a student would read it.

1. **`b9-01` in the first confrontation.** Design writes *"…while most of the
   food's mass is respired away as carbon dioxide and water — which is the
   b9-01 arithmetic again, running in the other direction."* A student cannot
   resolve a slot code, and printing one is exactly the platform leakage §8.10
   exists to stop. Resolved to the lesson TITLE, which is how b7-04 and b8-01
   resolved the identical shape:

       Design:  which is the b9-01 arithmetic again
       Built:   which is the arithmetic of Food chains and food webs again

   The destination is not lost — `food-chains-and-food-webs` is Design's own
   first "Before this lesson" card and is carried as a real `requires` edge,
   which is where the engine puts cross-lesson navigation.

2. **Nothing else.** Measured: this page contains no `<a href>` inside a hook
   or confrontation body (schema §11's list of stripped inline links names
   b9-01, b9-02, b9-03 and b9-04, and not this page), no year reference, and no
   half-term reference. The sequence-is-data rule costs this lesson nothing.

── ⊕ MRB-177 LENGTH PARITY — MEASURED, AND BOTH RUNGS WERE FIXED ────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`). The gate flags a correct option that is
strictly the longest AND clears the longest distractor by ≥4 words or ≥1.4×.
Design's sets, as delivered, BOTH FAIL it:

    rung 1  correct 11w vs 4 / 5 / 6   — gap 5, ratio 1.83   ✗ TELL
    rung 2  correct 22w vs 10 / 6 / 5  — gap 12, ratio 2.20  ✗ TELL

This is the construct `verify_ks3.py` names as the standing finding, met for
the twenty-first time: the correct answer states a RULE — subject, condition,
consequence — while each distractor states a short wrong REASON in one clause.
A rule needs three parts and a wrong reason needs one, so the correct answer is
longer BY CONSTRUCTION.

**Fixed at the distractor, as the 17 Aug 2026 ruling requires. No correct
option was shortened and no correct option was touched at all.** Every
distractor now states a WRONG RULE in the same subject–condition–consequence
shape, with the misconception as the consequence:

    rung 1  correct 11w vs 12 / 14 / 13 — not the longest      ✓ clean
    rung 2  correct 22w vs 22 / 18 / 16 — tied, not strictly   ✓ clean

**Design's option ORDER, both `answer` indices and all six corrections are
byte-identical.** Each correction was checked against its rewritten option and
every one still answers it — which is the test that the belief did not move:
the consequence clause added to each distractor is the thing its correction was
already refuting.

Distractor by distractor, with the register id where one supplies the belief:

    rung 1 · B  "It is extremely poisonous, so it does more damage at every
                 level"
                Belief WRITTEN FOR THIS RUNG, not in the register: *a chemical
                builds up because of how poisonous it is*. It is the
                persistence/toxicity confusion the ×1 control exists to break,
                but it is not `ECO-09` (which is about the molecule changing)
                and it is not `ECO-10` (which is about where you measure).
                Design's correction, unchanged: "How poisonous it is decides
                the damage once it arrives. Whether it builds up is a separate
                question about persistence."

    rung 1 · C  "It dissolves easily in water, so every organism in the lake
                 takes it in"
                ⚖️ THE FAT-SOLUBILITY DISTRACTOR, KEPT. Belief WRITTEN FOR THIS
                RUNG: *anything that dissolves in water gets into everything,
                so it builds up*. This is the one ruling 2 above turns on and
                the body copy is consistent with it everywhere. Design's
                correction, unchanged: "That makes it easier to excrete, so it
                is the property that stops accumulation — the water-soluble
                option on the bench does not build up at all."

    rung 1 · D  "It is used in large quantities, so more of it reaches every
                 organism"
                Belief WRITTEN FOR THIS RUNG: *the amount sprayed is what
                decides the concentration at the top*. Design's correction,
                unchanged: "Quantity affects the starting concentration. A
                large amount of something that breaks down still does not
                concentrate up a chain."

    rung 2 · A  "The perch's body converts the chemical into a stronger form,
                 so the same dose measures higher once it is inside a predator"
                `ECO-09` in the student's own words — the belief `#s-think`'s
                first quote confronts. Design's correction, unchanged: "Nothing
                is converted. The molecule leaving the minnow and the molecule
                in the perch are the same molecule."

    rung 2 · C  "The perch drinks more lake water, so it takes in more of the
                 chemical than the minnows do"
                Belief WRITTEN FOR THIS RUNG: *an animal picks the chemical up
                from the water it lives in, not from what it eats*. It is
                `ECO-10`'s cousin and not `ECO-10` itself, which is a claim
                about what a safe water measurement settles. Design's
                correction, unchanged: "Almost all of the intake comes through
                food, not water. That is what makes it a food chain problem."

    rung 2 · D  "Larger animals absorb chemicals faster, so the biggest animal
                 in a chain always carries the most"
                Belief WRITTEN FOR THIS RUNG: *size, not position in the chain,
                decides the concentration*. Design's correction answers the
                added consequence exactly and is unchanged: "Size is not the
                mechanism. A large animal at the bottom of a chain — a basking
                shark eating plankton — accumulates far less than a small one
                near the top."

The hook's four options are a WAGER and are never marked — no `answer` key — so
`length_tell()` skips them, as it does every unmarked set. They are lifted
untouched.

── The three condition cards keep all four of their parts ───────────────

Design's `COND_CARDS` are `kind` + `name` + `body` (page lines 331–335) — a mono
accent tag, a display name, a body. `_rule_card()` reads `role` (or `label`)
for the tag, `term`/`name`/`title` for the name, and `gloss`/`body`/`close` for
the body, so the shape maps one-to-one and the tag renders in its own
treatment. `kind` is renamed to `role` and nothing is joined, dropped or
invented.

The KEY FACT is authored NESTED, `{"ref": …, "ground": "card"}` inside the
`rule` block, which is Design's own arrangement (page lines 168–171: inside
`#s-two`, on `--ks3-card` with the 5px accent offset shadow). The section is
already `--ks3-band` and band on band is invisible. Never amber.

── ⚑ For Mide's science gate — every NOTES-B9 flag landing on this lesson ─

Three flags, three checked. One CORRECTED (13, by ruling 1 above), two left.

  * flag 13  **The bioaccumulation figures.** CORRECTED, and it is ruling 1.
             NOTES describes five levels and 0.003 → 25 ppm; the delivered
             bench has six rows and reaches 300 ppm at ×10. The bench won and
             six prose figures moved to meet it. The harm threshold of 1 ppm
             is untouched and is the open half of this flag — see the ⚑ under
             ruling 1 for what moving it would buy.

  * flag 14  **DDT, eggshell thinning, *Silent Spring* 1962, and continued
             indoor use for malaria control** (*Going further*). CHECKED AND
             LEFT, all of it, including the last clause NOTES asks about by
             name. It is the sentence that stops the story being a morality
             tale: DDT is still used indoors for malaria control in some
             countries because the disease kills people now, and Design's own
             framing — *"Both facts are true at once, which is what makes it a
             real decision rather than a moral"* — is what makes it a decision
             a student can be asked to hold rather than a slogan. Removing it
             would leave a story in which the only honest answer was obvious,
             which is not what happened and is not what a student should take
             from it. If Mide wants it out it is one sentence and it is the
             last one in the layer.

  * flag 15  **The tuna and swordfish mercury advice** (rung 4). CHECKED AND
             LEFT as a rung. It is real, current, published public-health
             advice, and the rung does not give health advice — it hands the
             student the advice as GIVEN and asks them to explain it from food
             chains, which is a transfer task in exactly the shape rung 4
             always takes. Nothing in the rung tells a student what to eat, and
             the five criteria mark chain position, chain length, persistence,
             lifespan and the conclusion. No safety note is warranted and none
             is authored; the foot line is a `convention_note` about the
             bench's own numbers.

── ⚠️ Where the page disagrees with itself, and is left alone ────────────

The hook says the birds were gone *twenty years later*; `#s-think`'s second
body says the osprey is *exposed to fifty years of lake water*. Neither is a
bench figure, neither is quoted by any computed verdict, and both are inside
their own hedges — the hook is one lake's story and the confrontation is the
general case. Recorded rather than harmonised: byte-identical is the rule and
the ruling above is its only exemption.
"""

# ── Design's three persistence settings, page lines 321–328 ─────────────
#
# ⚖️ EXACTLY ONE ×1 SETTING AND IT IS THE CONTROL. `soluble` is the flat line.
# The renderer raises if there is not exactly one, and `b9-chem-control` drives
# it in its own document. Do not remove it as "the boring one".
#
# ⚖️ FAT-SOLUBILITY IS THE MECHANISM — ruling 2. `persistent` is stored in fat
# and never excreted; `soluble` is filtered out by the kidneys within days.
# Every note below says so and rung 1's third option is the same claim as a
# wrong rule.
CHEMICALS = [
    {"id": "persistent", "label": "Persistent, fat-soluble",
     "factor": 10, "start": 0.003,
     "tab_note": "Cannot be broken down by the body and dissolves in fat, so "
                 "it is stored rather than excreted. Every dose an organism "
                 "ever takes in stays with it."},
    {"id": "partial", "label": "Slowly broken down",
     "factor": 3, "start": 0.003,
     "tab_note": "The body can break some of it down between meals, so only "
                 "part of each dose is kept. It still accumulates — just more "
                 "slowly."},
    {"id": "soluble", "label": "Water-soluble, excreted",
     "factor": 1, "start": 0.003,
     "tab_note": "Dissolves in water rather than fat, so the kidneys remove "
                 "it within days. Nothing is stored, so nothing can "
                 "concentrate."},
]

# ── Design's six chain rows, page lines 330–337 ─────────────────────────
#
# ⚖️ SIX, NOT FIVE — ruling 1. Water plus five feeding steps is what makes the
# persistent setting land on 300 ppm and 100,000×.
#
# ⚠️ The `eats` line is the MECHANISM, not a caption: *eat thousands of algae*,
# *eat hundreds of perch a year* is WHY the concentration multiplies rather
# than merely persisting. The renderer refuses a row without one.
#
# Drawn `column-reverse`, so the lake water is at the BOTTOM. There is a parity
# row on it and a drive that measures it.
LEVELS = [
    {"name": "Lake water",  "eats": "the source"},
    {"name": "Algae",       "eats": "absorbs from the water"},
    {"name": "Water fleas", "eats": "eat thousands of algae"},
    {"name": "Minnows",     "eats": "eat hundreds of water fleas"},
    {"name": "Perch",       "eats": "eat dozens of minnows"},
    {"name": "Ospreys",     "eats": "eat hundreds of perch a year"},
]

# ── Design's three condition cards, page lines 331–335 ──────────────────
#
# `kind` → `role` for `_rule_card()`'s mono accent tag. Nothing else moves.
# Card one is ruling 2 in Design's own words: not excreted *usually because it
# dissolves in fat rather than water*.
COND_CARDS = [
    {"role": "Condition one", "name": "It persists",
     "body": "The chemical is not broken down by enzymes and not excreted — "
             "usually because it dissolves in fat rather than water, so it is "
             "stored in the body instead of being filtered out."},
    {"role": "Condition two", "name": "Predators eat many",
     "body": "Each organism eats many of the level below over its life. All "
             "the toxin from all those bodies ends up in one, so the "
             "concentration multiplies."},
    {"role": "Why the top suffers", "name": "Long chains, small numbers",
     "body": "The animals at the top are few, slow-breeding and long-lived — "
             "so they accumulate for longest, and a population that loses its "
             "adults takes decades to recover."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 158 character for character.
    "slug":        "toxic-build-up-in-a-food-chain",
    "title":       "Toxic build-up in a food chain",
    "discipline":  "biology",
    "unit":        "ecosystems-and-interdependence",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.ECO.03` — "how organisms affect, and are affected by, their
    # environment, including the accumulation of toxic materials". The named
    # example in the statutory bullet IS this lesson, and no other lesson in
    # the key stage runs the accumulation arithmetic. Owned whole: the
    # statement has no sub-clauses in `ks3_data/substatements.py`, so it cannot
    # be split, and `build_ks3.validate()` enforces exactly-once ownership.
    #
    # ⚠️ NOTES-B9 §0 says ECO.03 is covered "by b9-03 and b9-05". Two owners is
    # a build failure, so it is one: b9-03's own clause is `KS3.B.ECO.01c`
    # (what interdependence means when a web is disturbed), which
    # `substatements.py` mints for it by name. b9-03 TOUCHES ECO.03; this
    # lesson owns it.
    "covers":      ["KS3.B.ECO.03"],
    # Named, used, and owned elsewhere. ECO.01a is b9-01's food chains — this
    # page runs the same 10:1 arithmetic in the opposite direction and never
    # re-teaches it (payload schema §0 rule 7: B9 owns the ratio, b9-01 states
    # it, nothing else re-declares it). ECO.01c is b9-03's disturbed web, which
    # the `#s-two` third card leans on in one clause about slow-breeding
    # top predators and does not teach.
    "touches":     ["KS3.B.ECO.01a", "KS3.B.ECO.01c"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "substances-and-reactions", "level": 2},
                    {"id": "energy", "level": 1}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. `food-chains-and-food-
    # webs` is also the destination of the stripped `b9-01` slot code in the
    # first confrontation — see "What could not be lifted" 1 — and is not
    # repeated in `references`, because the edge already exists here.
    "requires":    ["food-chains-and-food-webs", "disturbing-a-food-web"],
    "assumes":     [],
    # Design's "Connects to" card, in her order.
    "references":  [{"unit": "B6", "lesson": "what-drugs-do-to-the-body"},
                    "sampling-an-ecosystem"],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Bioaccumulation and biomagnification, persistent organic "
                   "pollutants, and the regulation of pesticides.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A concentration far too low to harm anything in the water "
                    "can still kill the bird at the top of the chain. Nothing "
                    "is added along the way. The arithmetic does it.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 315–321). `s-two` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate — see the docstring, which also supersedes payload
    # schema §4's three-stop count. `short` and `label` are Design's own
    # `RAIL_SHORT` and `RAIL` strings, TWO / "Two conditions" included.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Safe in water",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.everTopped` (page line 391). The
        # stop ticks when the student has climbed a chain to the top once, not
        # when a setting has been pressed — switching settings reveals nothing.
        {"anchor": "s-bench", "short": "BENCH", "label": "Climb the chain",
         "done_when": "chain_topped"},
        {"anchor": "s-two", "short": "TWO", "label": "Two conditions",
         "mirrors": "s-bench", "done_when": "chain_topped"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. C is the correct one
    # and the reveal says so at once; the hook is not a trick, it is a claim the
    # bench then has to earn in parts per million.
    #
    # ⚖️ Option B is `ECO-09` in the student's own words, which is why the
    # misconception below names `s-hook` as its `elicited_by`. The student who
    # picks B has stated the belief before the page names it.
    #
    # ⚠️ FOUR FIGURES CHANGED HERE — ruling 1, items 2, 3, 4 and 5. The water,
    # the ospreys, the commit question and the reveal's factor count now all
    # match the bench a student is about to run.
    "phenomenon": {
        "kind": "narrative",
        "title": "Safe in the water. Lethal in the osprey.",
        "prompt": "A pesticide is sprayed on farmland and washes into a lake "
                  "at 0.003 parts per million — three thousandths of a "
                  "milligram in a litre, far below anything that could harm a "
                  "fish. Twenty years later the fish-eating birds are gone, "
                  "and the pesticide in their bodies measures 300 parts per "
                  "million.",
        "commit": "How did the concentration rise by a hundred thousand times?",
        "options": [
            "The birds drank enormous amounts of lake water",
            "The chemical reacted and became stronger inside the animals",
            "Each organism keeps what it takes in, and each predator eats many "
            "of them",
            "More pesticide was sprayed every year",
        ],
        "reveal": "Nobody added anything. Two facts do all the work: the "
                  "chemical is not broken down or excreted, so it stays in the "
                  "body for life; and each organism eats many of the organisms "
                  "below it. A fish that eats a thousand contaminated water "
                  "fleas keeps a thousand doses in one body. Do that five "
                  "times up a chain and the concentration climbs by five "
                  "factors of ten.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # The commander's pre-allocation, payload schema §14. Both statements are
    # Design's own quoted beliefs, byte-identical from page lines 187 and 191,
    # in register voice.
    #
    # ⚠️ The `ECO` prefix row is NOT yet open in
    # `docs/ks3/misconception-register.md` and that file is not this pass's to
    # edit. The two rows below are what belongs in it; they are reported for
    # minting alongside `ECO-01`…`ECO-08` and `ECO-11` from the five sibling
    # passes.
    #
    # ⛔ `ECO-12` MUST NOT BE MINTED, here or anywhere, ever. The register
    # permanently reserves it: its belief is `NOS-04`, which b9-06 owns.
    # NOTES-B9 §4 asks for twelve `ECO` ids; the register supersedes it.
    #
    # Both values resolve against the BUILT page (MRB-244/MRB-248): `s-hook`,
    # `s-bench` and `s-think` are all emitted as section anchors.
    "misconceptions": [
        # Elicited by the hook: option B is this belief, word for word, and the
        # student commits to it or declines to before the page names it. It is
        # also rung 2's first option, restated as a wrong rule. Confronted in
        # `#s-think`, whose first body takes the molecule apart from the
        # concentration.
        {"id": "ECO-09",
         "statement": "The poison gets stronger as it goes up the chain.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        # Elicited by the bench: row one is the lake water and it reads "no
        # measurable effect" on every setting including the persistent one, so
        # the student is holding a safe water reading in their hand and has to
        # decide what it settles. On the ×1 control it settles everything; on
        # ×10 the same reading ends a hundred thousand times higher five rows
        # up. Confronted in `#s-think`'s second body, which is the history of
        # exactly this reasoning being used to approve pesticides.
        {"id": "ECO-10",
         "statement": "If the level in the water is safe, the ecosystem is "
                      "safe.",
         "elicited_by": "s-bench",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B9, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ "fat-soluble" and "water-soluble" are both here, glossed as a PAIR,
    # because ruling 2 is the whole mechanism and the pair is what rung 1's
    # third option turns on.
    "vocabulary": [
        {"term": "bioaccumulation",
         "definition": "The build-up of a substance in an organism because it "
                       "takes it in faster than it can get rid of it.",
         "note": "It needs no chemistry beyond the substance staying put."},
        {"term": "persistent",
         "definition": "Not broken down — by an organism, or in the "
                       "environment, for years or decades.",
         "note": "Persistence, not toxicity, is what decides whether "
                 "something builds up."},
        {"term": "fat-soluble",
         "definition": "Dissolves in fat rather than in water, so a body "
                       "stores it instead of filtering it out.",
         "note": "Water-soluble is the opposite: the kidneys remove it in "
                 "days, so nothing accumulates."},
        {"term": "parts per million",
         "definition": "A unit of concentration: one part of the substance in "
                       "a million parts of everything else.",
         "note": "In water, 1 ppm is about 1 milligram in a litre."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED — payload schema §15, which grepped all six B9
    # pages. `<img>`, `<figure>` and `<picture>` each appear zero times here;
    # every `<svg>` on the page is the nav chevron or a `ks3-mark` icon.
    # Declaring one would invent a sourcing task in
    # `docs/ks3/diagram-manifest.md`. NOTES-B9 flag 17 (a drawn food web, for
    # b9-01 and b9-03) is not dropped by this and is not this page's to answer.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b9/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md §9.
        {"type": "bioaccumulation", "id": "follow-the-concentration-up",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         # ⚠️ FIGURE CHANGED — ruling 1, item 1. Design's eyebrow says "five
         # levels" and `LEVELS` has six; it counted the organisms and forgot
         # the water they stand in.
         "eyebrow": "At the bench · one lake, six levels",
         "heading": "Follow the concentration up",
         "prompt": "Choose how persistent the chemical is — whether the body "
                   "can break it down — then climb the chain. The persistence "
                   "dial is the one that decides everything.",
         # Design's mono line beside the heading (page line 108). `_b9_head`
         # converts it into the head counter: format from `before`, `full` from
         # `after`, opening at level 1 because a student is already looking at
         # the lake water. Without the conversion the resting bytes would read
         # `level {n} of {total}` with the braces on screen.
         "progress": {"before": "level {n} of {total}",
                      "after": "top of the chain"},

         "tabs_label": "The chemical",
         "chemicals": CHEMICALS,
         "levels": LEVELS,

         # Design's `HARM = 1.0` (page line 329), untouched. Every row is
         # measured against it. See the ⚑ in the docstring: at six rows this
         # flags minnows, perch and ospreys, and whether that is the right
         # threshold is Mide's call, not this pass's.
         "harm": 1.0,
         "harm_verdict": "above the level that causes harm",
         "safe_verdict": "no measurable effect",

         "step_label": "Who eats them?",
         "step_spent_label": "Top of the chain",
         "reset_label": "Back to the water",

         # ⚖️ THREE BRANCHES, AND ONLY TWO OF THEM QUOTE A NUMBER. `{ppm}` and
         # `{times}` are filled from the bench's own state — a verdict that
         # quoted a fixed figure would be wrong on every setting but one — and
         # `flat` carries neither, because the control is the branch with no
         # figure to report. `b9-chem-control` fails the build if a digit ever
         # appears in it.
         "verdicts": {
             "flat": "Flat all the way up. The chemical is excreted as fast "
                     "as it arrives, so no organism holds more than any other "
                     "and nothing is at risk. The concentration in the water "
                     "was the whole story — which is exactly why the "
                     "persistent case caught everyone out.",
             "harmful": "The ospreys are carrying {ppm} ppm — roughly {times} "
                        "times the concentration in the water, and enough to "
                        "stop them breeding. Not one molecule was added after "
                        "the spraying. Every one of them came out of the lake.",
             "below": "The concentration climbed to {ppm} ppm at the top — a "
                      "real build-up, and below the level that causes harm "
                      "here. Slower breakdown is not the same as no "
                      "accumulation; a longer chain or a longer exposure would "
                      "still get there.",
         }},

        # #s-two — the band panel, and the section that discharges
        # KS3.B.ECO.03. Rail stop 3, mirroring `s-bench`; see the docstring.
        {"type": "rule", "anchor": "s-two",
         "eyebrow": "Two conditions, and it needs both",
         "statement": "Remove either one and nothing accumulates.",
         "cards": COND_CARDS,
         # Design nests the key fact inside this section (page lines 168–171)
         # on the CARD ground with the accent offset shadow. `card`, because
         # the section itself is `band` and band on band is invisible.
         "key_fact": {"ref": "it-concentrates-at-every-step",
                      "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "ECO-09"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-two on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 171
    # and identical to payload schema §12's b9-05 entry.
    #
    # ⚑ "The animals at the top are harmed first" against a six-row bench at
    # harm = 1 ppm: see the flag under ruling 1 in the docstring. The sentence
    # is Design's, is science-bearing, and is not this pass's to edit.
    "key_facts": [
        {"id": "it-concentrates-at-every-step",
         "text": "A toxic substance that cannot be broken down or excreted "
                 "accumulates in each organism and becomes more concentrated "
                 "at every step up a food chain, because each predator eats "
                 "many of the organisms below it. The animals at the top are "
                 "harmed first, at concentrations that are harmless lower "
                 "down.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, payload
        # schema §3), so it is a `confrontation` and not a `predict`, it is not
        # a rail stop, and it emits no completion contract.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "ECO-09",
         "statements": [
             # `ECO-09`. This paragraph is why the bench is upstream of it in
             # the document: the student has just watched one molecule's
             # concentration climb without the molecule changing.
             #
             # ⚠️ `b9-01` resolved to its lesson title — "What could not be
             # lifted" 1. The destination is already in `requires`.
             {"quote": "The poison gets stronger as it goes up the chain.",
              "body": ["The molecule is identical at the top of the chain and "
                       "at the bottom — it has not been strengthened, "
                       "activated or changed in any way. What rises is the "
                       "<em>concentration</em>: how much of it there is in "
                       "each kilogram of animal. Nothing is added; things are "
                       "collected. A water flea takes in a tiny amount and "
                       "keeps it. A minnow eats a hundred water fleas and now "
                       "holds a hundred tiny amounts in one small body. A "
                       "perch eats fifty minnows, and an osprey eats a hundred "
                       "perch across a season. At every step the toxin from "
                       "many bodies is packed into one, while most of the "
                       "food's mass is respired away as carbon dioxide and "
                       "water — which is the arithmetic of Food chains and "
                       "food webs again, running in the other direction. The "
                       "energy shrinks by ten times a level; the toxin does "
                       "not shrink at all, so its concentration climbs by "
                       "roughly the same factor."]},
             # `ECO-10`, and it is a history lesson rather than a correction:
             # this reasoning is what several decades of pesticide approvals
             # actually ran on. It closes on ruling 2 in Design's own words —
             # how long does it last, and does it dissolve in fat.
             {"quote": "If the level in the water is safe, the ecosystem is "
                       "safe.",
              "body": ["This was the actual reasoning behind several decades "
                       "of pesticide approvals, and it is why the effect took "
                       "so long to notice. A safety limit set by testing the "
                       "water, or by testing a single dose on a single animal, "
                       "misses two things: that the chemical persists rather "
                       "than passing through, and that a food chain "
                       "concentrates whatever persists. The osprey is not "
                       "exposed to lake water — it is exposed to fifty years "
                       "of lake water, collected by other organisms and "
                       "delivered in a fish. Modern approval of a pesticide "
                       "therefore asks a different question: not only <em>how "
                       "toxic is it</em> but <em>how long does it last and "
                       "does it dissolve in fat</em>. Those two properties, "
                       "not the raw toxicity, decide whether a chemical "
                       "becomes a problem at the top of a chain."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — MEASURED, BOTH MARKED RUNGS FAILED AS
    # DELIVERED, BOTH FIXED AT THE DISTRACTOR. rung 1 was 11w against 4 / 5 / 6
    # and is now 11w against 12 / 14 / 13; rung 2 was 22w against 10 / 6 / 5
    # and is now 22w against 22 / 18 / 16. No correct option was touched, no
    # `answer` index moved, Design's option ORDER is unchanged, and all six
    # corrections are byte-identical and still answer their rewritten options.
    # Full working, distractor by distractor, in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Which chemicals build up",
            "q": "Which property makes a pollutant likely to accumulate up a "
                 "food chain?",
            # All four now state a RULE — a property, a condition, and what
            # follows from it — which is what keeps the rung clean: the student
            # cannot pick by shape. B is the persistence/toxicity confusion the
            # ×1 control exists to break; C is ruling 2 inverted and is the
            # distractor the whole body copy is kept consistent with; D is the
            # belief that the amount sprayed decides the figure at the top.
            "options": [
                "It cannot be broken down or excreted, so organisms keep it",
                "It is extremely poisonous, so it does more damage at every "
                "level",
                "It dissolves easily in water, so every organism in the lake "
                "takes it in",
                "It is used in large quantities, so more of it reaches every "
                "organism",
            ],
            "answer": 0,
            "feedback": {
                1: "How poisonous it is decides the damage once it arrives. "
                   "Whether it builds up is a separate question about "
                   "persistence.",
                2: "That makes it easier to excrete, so it is the property "
                   "that stops accumulation — the water-soluble option on the "
                   "bench does not build up at all.",
                3: "Quantity affects the starting concentration. A large "
                   "amount of something that breaks down still does not "
                   "concentrate up a chain.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Why is the concentration higher in a perch than in the "
                 "minnows it eats?",
            # ⚖️ Option A is `ECO-09` stated as a wrong rule, which is why it
            # is the same length as the correct answer rather than the four
            # words a student's own version of it would take. That is the
            # MRB-177 fix working as intended: the belief did not move, the
            # SHAPE it is written in did.
            "options": [
                "The perch's body converts the chemical into a stronger form, "
                "so the same dose measures higher once it is inside a predator",
                "The perch eats many minnows and keeps the toxin from all of "
                "them, while most of the food's mass is respired away",
                "The perch drinks more lake water, so it takes in more of the "
                "chemical than the minnows do",
                "Larger animals absorb chemicals faster, so the biggest animal "
                "in a chain always carries the most",
            ],
            "answer": 1,
            "feedback": {
                0: "Nothing is converted. The molecule leaving the minnow and "
                   "the molecule in the perch are the same molecule.",
                2: "Almost all of the intake comes through food, not water. "
                   "That is what makes it a food chain problem.",
                3: "Size is not the mechanism. A large animal at the bottom "
                   "of a chain — a basking shark eating plankton — accumulates "
                   "far less than a small one near the top.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the build-up",
            # ⚠️ TWO FIGURES CHANGED — ruling 1, item 6. Design asked for 25
            # ppm and "roughly ten thousand times"; the bench beside this rung
            # prints 300 ppm and computes 100,000×. The rung was asking a
            # student to explain a number the page never shows them.
            "q": "A pesticide measured at 0.003 ppm in a lake is found at 300 "
                 "ppm in the ospreys nesting there. Explain how the "
                 "concentration rose by roughly a hundred thousand times, "
                 "given that nobody added any more pesticide.",
            "field_label": "Your explanation",
            "placeholder": "The pesticide cannot be broken down…",
            # The fifth criterion is `ECO-09` marked as a criterion rather than
            # as prose, which is why the confrontation above can stay static
            # and still be assessed.
            "success": [
                "Says the pesticide cannot be broken down or excreted, so each "
                "organism keeps all it takes in.",
                "Says each organism eats a large number of the organisms below "
                "it.",
                "Says the toxin from all of those bodies therefore ends up in "
                "one body.",
                "Says most of the food's mass is respired away or excreted "
                "while the toxin is not, so the toxin becomes more "
                "concentrated in each kilogram of animal.",
                "Says the effect multiplies at every level, so a long chain "
                "produces an enormous factor — and states that the molecule "
                "itself is unchanged.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            # ⚑ NOTES-B9 flag 15. Checked and left as a rung: the advice is
            # handed to the student as GIVEN and they are asked to explain it
            # from food chains. Nothing here tells a student what to eat.
            "q": "Health advice tells pregnant women to limit how much tuna "
                 "and swordfish they eat, because of mercury, while sardines "
                 "and prawns carry no such warning. Explain the difference "
                 "using what you know about food chains.",
            "field_label": "Your answer",
            "placeholder": "Tuna and swordfish are…",
            "success": [
                "Says tuna and swordfish are large predatory fish near the top "
                "of long marine food chains.",
                "Says sardines and prawns feed at or near the bottom of the "
                "chain, so far fewer steps have happened.",
                "Says mercury is not broken down or excreted, so it "
                "accumulates in the body over the animal's life.",
                "Says the top predators are also long-lived, so they have been "
                "accumulating for many years.",
                "Concludes that the concentration in the flesh is therefore "
                "much higher in the predatory fish, even though both live in "
                "the same sea.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Lifted byte-identical from page line 262. It quotes no figure, so ruling
    # 1 does not reach it.
    "key_note": "A toxic substance builds up in a food chain when it cannot be "
                "broken down or excreted. Each organism keeps what it takes "
                "in, and each predator eats many of the organisms below it, so "
                "the concentration multiplies at every level. Animals at the "
                "top of long chains are affected first, at concentrations that "
                "are harmless in the water and harmless in the organisms lower "
                "down.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B9 flag 14 is this paragraph, and it is checked and left whole,
    # including the last clause the flag asks about by name — the working is in
    # the docstring. Design's own hedges are load-bearing: "credited with" and
    # "is judged smaller" are what keep it a decision rather than a verdict.
    #
    # ⚖️ It also names ruling 2 out loud — "persistent and fat-soluble — the
    # two properties on the bench above" — so the layer and the dial agree.
    "stretch": [
        {"type": "explainer", "id": "what-ddt-cost-and-what-it-still-saves",
         "text": "DDT was the miracle insecticide of the 1940s: cheap, "
                 "effective, and credited with saving millions of lives from "
                 "malaria and typhus. Its inventor received a Nobel Prize. Two "
                 "decades later, ornithologists noticed that peregrines, "
                 "ospreys and bald eagles were laying eggs with shells so thin "
                 "they broke under the weight of the incubating parent, and "
                 "the populations were collapsing. The chemical was persistent "
                 "and fat-soluble — the two properties on the bench above — "
                 "and it had concentrated up every chain it entered. Rachel "
                 "Carson's <em>Silent Spring</em> put the evidence in front of "
                 "the public in 1962; DDT was banned for agricultural use in "
                 "most countries during the 1970s, and the birds recovered. "
                 "The awkward part of the story is still live: DDT is still "
                 "used in some countries for malaria control indoors, because "
                 "the disease kills people now and the ecological cost is "
                 "judged smaller than the alternative. Both facts are true at "
                 "once, which is what makes it a real decision rather than a "
                 "moral."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work out which chemicals would and would not "
                      "build up?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 297) and nothing in it is a safety
    # instruction — it is a note about how far the bench's numbers can be
    # trusted. Routing it through `safety_note` would print it in the treatment
    # reserved for "never light a candle without an adult", which devalues the
    # safety line.
    #
    # ⚑ It is also the honest half of NOTES-B9 flag 13 and is load-bearing
    # after ruling 1: the page tells the student the concentrations are round
    # numbers chosen to show the pattern, which is exactly what 0.003 → 300
    # is, and what makes correcting the prose to the bench a correction rather
    # than a new claim about DDT.
    "convention_note": "The concentrations on the bench are round numbers "
                       "chosen to show the pattern; they are of the same order "
                       "as figures reported for DDT in lake food chains but "
                       "are not taken from a particular study. Real "
                       "accumulation depends on the chemical, the species, the "
                       "length of the chain and how long the exposure has "
                       "lasted.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is a quantitative model with a CONTROL in it — the ×1 setting —
    # and the lesson's central claim is established by comparing the control
    # against the treatment rather than by asserting it. Rung 2 asks for a
    # conclusion to be defended against a strongly held alternative, and rung 4
    # applies it to a case the page never showed.
    "ws": ["analysis-and-evaluation", "experimental-skills"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
