"""B11 L1 — Variation and competitive success (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b11/b11-01-variation-and-competitive-success.dc.html`
(582 lines), her author's notes `docs/ks3/design-reference/b11/NOTES-B11.md`, and
the B11 payload schema `docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md` §0, §1, §2, §6,
§7, §8, §9, §11, §12, §13 and §14, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the two listed under "What could not be lifted" and rung 2's three
distractors, which MRB-177 required. The five mice, the five environments with
their twenty-five per-mouse rationales, the four competition cards, both marked
rungs and both self-marked rungs came out of the page's own `MICE`, `ENVS`,
`COMPETE_CARDS`, `RUNGS` and `SELF_RUNGS` arrays via
`tools/extract_design_payload.js`, not off a keyboard. **No survival percentage,
no rationale and no correction was retyped**, and every authored string in this
file was diffed back against that extraction after the fact rather than checked
by eye.

── `covers` is ONE HALF of a two-part clause, and the seam is the bullet's own ─

`KS3.B.INH.05` reads, in full: *the variation between species and between
individuals of the same species meaning some organisms compete more
successfully, which can drive natural selection*. `substatements.py` splits it
at *which can drive*, and the split is the reason this lesson and b11-02 exist
separately:

    KS3.B.INH.05a  variation meaning some organisms compete more successfully —
                   and that which variation helps depends on WHERE the organism
                   is.                                              ← THIS LESSON
    KS3.B.INH.05b  how that difference in competitive success, repeated over
                   generations, drives natural selection.                ← b11-02

`05a` is a statement about a population AT ONE MOMENT and `05b` is a statement
about that moment REPEATING. The comment in `substatements.py` records why they
are taught apart: teaching them in one sitting is what produces the belief that
an individual adapts during its own life, which is the most expensive
misconception in the unit. **Nothing in this file runs a generation.** The bench
has no clock, the mice never change, and the word *selection* appears nowhere in
the lesson body — it is `ks4_becomes` and the *Connects to* card, and that is
deliberate.

── ⚖️ THE LESSON'S OWN POINT, AND EVERY PART OF THE PAGE SERVES IT ──────

From the KEY FACT, which is schema §9 verbatim: **which variation gives an
advantage depends entirely on the conditions, and the conditions change — so
there is no such thing as a generally superior individual.** That is the
foundation the whole unit stands on, and `EVOL-01` and `EVOL-02` are the two
ways to get it wrong — one by naming a fixed winning trait (strength), one by
naming a fixed winning animal.

It is drawn five times over:

  * the hook offers three named "best variations" and one refusal, and the
    reveal endorses the refusal before a single number is on screen;
  * the bench runs the SAME five animals through five worlds and the column
    reshuffles every time — thick coat 90 in the winter and 25 in the drought,
    small and quick 45 then 85, the identical reversal read backwards;
  * `#s-three`'s key fact says it in one sentence;
  * rung 3 asks the student to explain the reversal and *say what this means for
    the idea of a "better" animal*;
  * the key note closes on *no variation is an advantage in general*.

⛔ **NO AUTHORED COMMENT, BENCH VERDICT OR LADDER CORRECTION IN THIS FILE
IMPLIES A RANKING THAT HOLDS ACROSS ENVIRONMENTS.** The verdict line judges one
COLUMN and says so; `best here` and `worst here` both carry the word *here*, in
words as well as in colour, and that word is the whole instrument. The one place
a general claim is made is rung 2's correct option — *best fitted to the current
conditions* — and it carries "current" for the same reason.

── The instrument: a bench with no run button, and a MEASURED shell ────

`#s-bench` is `advantage-bench`, on `ks3-block ks3-dark ks3-practical` (page
line 105, quoted verbatim in schema §0.3), so `practical` is MEASURED from
Design's own class attribute rather than inferred from the kind name — contract
§4 records that B1 got two of six wrong by inferring it. `ks3_data/b11/__init__.py`
holds the map, written in one pass by the engine because four authors work this
unit in parallel and a lost entry there would ship a bare list past a green
kinds gate.

⚖️ **SWITCHING IS THE EXPERIMENT.** There is no run button, no reset and no
prediction: five tabs, each of which sets the environment and records that it
has been seen. So **`run_label`, `reset_label` and `verdicts` are NOT authored**
— Design draws none of those controls, and a key with no read site is a dead key
under contract R5. `verdicts` in particular would be the wrong shape twice over:
this bench never judges the student, and the per-environment verdict line is
already carried as `envs[].verdict`.

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0.4). Design's state bag holds `env`
and `seen`; both are the runtime's. Nor is an opening environment authored:
schema §0.4's exception is for an opening selection that is NOT first in its
list, and `winter` IS `environments[0]`, so the renderer's default of index 0
already ships Design's page. `_KIND_HEAD_START["advantage-bench"] = 1` for the
same reason — the bench opens ON an environment, and an environment you are
looking at is one you have seen, so the resting bytes read "1 of 5 conditions
tried" rather than "0 of 5".

⚖️ **THE PERCENTAGES ARE THE BAR AS WELL AS THE NUMBER**, so they are whole
integers and `r_advantage_bench` refuses anything else: a string or a fraction
would draw a plausible row with an impossible bar. And `chances` / `whys` are
MAPS KEYED BY SUBJECT ID (schema §1), never parallel arrays — a parallel array
silently pairs a mouse with another mouse's survival number the moment anyone
reorders the list, and the renderer checks the key sets in both directions.

── ⚠️ THE `disease` TIE, and the one place the port departs from Design ─

`disease` is `{big: 45, thick: 45, fast: 45, bold: 30, pale: 45}`. Design's own
`isBest` is `c === Math.max(...)`, so **four of the five mice carry
`45% survive · best here` in green at once**, underneath a verdict that reads
*"None of the visible variations helps."* Schema §11 item 4 records it; NOTES
does not mention it.

The payload is authored AS MEASURED and the fix lives in the renderer:
`_b11_ab_extremes` marks nothing unless the column has a unique maximum AND a
unique minimum, so `disease` ships five muted bars and lets the verdict do the
teaching. **Do not "resolve" the tie by nudging one of the four 45s.** The tie
IS the panel — it is what sets up rung 4 and hands off to b11-04, and a panel
that says no variation helps while painting four green winners teaches the
opposite of its own sentence.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page lines 302–307) and her `isDone()` gives `s-three` the
BENCH's predicate, character for character, one line further down:

    if (id === 's-bench') return n >= 3;
    if (id === 's-three') return n >= 3;          // page lines 423–424

`#s-three` is an eyebrow, a display statement, four static cards and a key fact:
no control, no commitment, no field, no reveal. It is the PAYOFF of the bench
beside it and carries no control precisely because the bench has already taken
the student's attention. That relationship is a MIRROR, `wireRail`'s `paint()`
resolves it at rail level — which is the level Design computes it at — and
`ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`, whose row for this page reads
`s-hook s-bench s-three s-ladder | s-three=s-bench`.

⚠️ Schema §8's struck paragraph — *author three stops and drop the band* — is
REVERSED by the ⊕ block at the head of the same section, and the "commander's
call" text below it is RULED: **the mirror.** Four is what Design drew and four
is what ships. Shipping three fails the build.

⚖️ **THREE OF FIVE IS DESIGN'S OWN THRESHOLD AND IT IS READ TWICE**, once for
the bench and once for the mirror. `build_ks3._B11_AB_THRESHOLD` holds it, and
`r_advantage_bench` refuses a bench with fewer than three environments because
that would ship two rail stops no student could ever tick. Three is also the
point at which a student has switched the world twice and can have seen the same
animal at the top and at the bottom of the column.

`#s-think` and `#s-keynote` are on no rail, and that is Design's too:
`#s-keynote` asks nothing, and `#s-think` here is static markup — two quotes,
two bodies, no options, no reveal, no button — so it is a `confrontation` and
not contract R1's `predict`. Schema §7, measured on all four B11 pages.

── What could not be lifted byte-identical, and why ────────────────────

1. **A HYPERLINK WHOSE TEXT IS A POSITION, in `#s-think`'s second body.**
   Design writes *"…which is precisely how extinctions happen, and it is
   `<a href="b11-03-…">the subject two lessons from here</a>`."* `rich()` allows
   `<em>` and `<strong>` and nothing else, so no anchor survives anywhere on the
   page. Where the link TEXT is already a lesson title that costs nothing
   (b10-05's case); here the text is a POSITION, so dropping the tag alone would
   leave a student with nothing to follow and an ordering claim a school's own
   scheme may not honour. Resolved to the lesson TITLE, exactly as b9-02 and
   b9-03 resolved the identical shape:

       Design:  and it is <a …>the subject two lessons from here</a>
       Built:   and it is the subject of When the environment changes:
                extinction

   The destination is not lost: `when-the-environment-changes-extinction` is
   carried in `references` — see the note there, because it is the ONE edge in
   this record that is not on one of Design's endmatter cards.

2. **Rung 2's three distractors — MRB-177, and the reason the rung had to be
   repaired rather than lifted.** Worked in full below. Nothing else on the
   ladder moved.

Two `<em>` runs in the hook's reveal and four in `#s-think` DO survive, because
`rich()` renders them and every one is load-bearing: *in a particular set of
conditions* is the hook's whole answer, *best fitted to these conditions* is the
definition rung 2 marks, and *well adapted to a particular environment* against
*advanced* or *superior* is the contrast the second confrontation exists for.

⚠️ No sequence leak to repair. `Year 7`, `Year 8`, `Year 9`, `Year 10`, `Year 11`
and `half-term` appear ZERO times in Design's bytes — grepped, not assumed, and
now GATED by `verify_ks3.py` rather than left to contract law. The page does
contain "a mild year" and "in a hard winter carrying them", which are durations
and seasons in the content and name no point in a scheme of work, and the dates
in *Going further* (1977, 1983) are the science.

── ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN, RUNG 2 REPAIRED AT THE DISTRACTORS ─

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor
by ≥4 words or by ≥1.4×.

    rung 1  correct 10w vs 10 / 12 /  7  — not strictly longest    ✓ as drawn
    rung 2  correct 12w vs  5 /  6 /  6  — gap 6, ratio 2.00       ✗ TRIPPED (both)
    rung 2  correct 12w vs 13 / 13 / 15  — not strictly longest    ✓ repaired

**Rung 1 needed nothing and nothing was done to it.** All four options answer
*what does that show?* in the same grammar, three of them beginning *That…* and
stating a wrong lesson, and the longest option on the rung is a DISTRACTOR
(C, 12w). That is the construct MRB-177's ruling asked for, arrived at by
Design.

**Rung 2 is the rung MRB-177 usually trips, and it tripped here for exactly the
reason the ruling names.** The correct option states a two-part DEFINITION —
*best fitted to the current conditions*, AND *leaving the most surviving
offspring* — because that second half is the whole point of the rung, while each
distractor named a single property in a noun phrase. A definition needs two parts
and a noun phrase needs one, so the correct answer was longer BY CONSTRUCTION
and `length_tell()` measured the construction.

**Fixed at the distractor, per MRB-177. The correct option is untouched, the
answer index is untouched (still 1, Design's), and no correction was edited** —
`feedback` is Design's three corrections, byte-identical, still keyed to the
options they answer. Each distractor keeps its belief exactly and gains the
correct option's own second clause, joined with the same ", and":

    A  before  5w  The strongest and healthiest individuals
       after  13w  The strongest and healthiest individuals, and the ones that
                   win a direct fight
       → still EVOL-01 undisguised, and Design's correction — "Strength is one
         variation among many… in a drought the animal that needs least water
         wins" — answers the longer form better than the shorter one, because
         "wins a direct fight" is precisely the arena a drought does not have.

    C  before  6w  The individuals that live the longest
       after  13w  The individuals that live the longest, and the ones that
                   avoid dying young
       → the added clause is longevity restated, which is what the belief is;
         Design's correction ("An organism that lives fifty years and never
         breeds leaves nothing behind") lands on both halves at once.

    D  before  6w  The most advanced or highly evolved
       after  15w  The most advanced or highly evolved, and the ones highest up
                   the tree of life
       → the scala naturae in the student's own words, which is the belief
         "most advanced" is a polite version of; Design's correction ("There is
         no ranking of advancement in biology") is an answer to the ladder image
         directly.

    B  correct 12w, UNCHANGED: "Best fitted to the current conditions, and
       leaving the most surviving offspring"

⚖️ Note what the repair does NOT do. It does not make any distractor
self-evidently wrong — each is a belief a thirteen-year-old genuinely holds,
stated in the voice they hold it in — and it does not change the connective
between the correct option and its distractors, which would have swapped a
length tell for a grammar one. All four options now read as the same kind of
answer to the same question, which is the construct the ruling asked for.

── Misconception ids: EVOL-01 and EVOL-02, and EVOL-09 is UNUSED ───────

Schema §12's pre-allocation for b11-01, and the two beliefs Design's `#s-think`
quotes, in her page order. Both statements are her own bytes (page lines 172 and
177) in register voice, with the curly quotes stripped — the renderer draws
those.

**Two beliefs were found and two ids were used. `EVOL-09`, this lesson's named
spare, is UNCLAIMED and stays permanently unused**, exactly like `DRUG-07`. It
is never re-pointed at a different belief in a later pass. No second spare was
needed, so nothing was reached past the table (schema §12).

⊕ **THE `EVOL` PREFIX ROW IS OPEN, AND IT AGREES WITH THIS FILE.** Schema §11
item 5 records that NOTES-B11 §4 claims these eight were "written into"
`docs/ks3/misconception-register.md` and that `grep -n "EVOL"` returned nothing
— the fourth delivery in a row to claim it. It was opened by the register pass
during this run and read rather than assumed, at the end of this run because
that file is in flight and is not this pass's to edit (contract §0). Its
`EVOL-01` and `EVOL-02` rows match the two authored here on statement, on
`elicited_by` and on `confronted_by`. Nothing to reconcile.

**NOTES-B11 §4 asks `EVOL-01` to carry `natural-selection` in `reappears_in`.**
It does, in the register — which is the only place `reappears_in` exists. It is
a register column and not a lesson key: `grep -rn reappears_in build_ks3.py
ks3_data/` returns three docstring mentions and no read site, and authoring one
here would be a dead key under contract R5.

Both `confronted_by` values are `s-think` and both resolve against the BUILT
page (MRB-244). The two `elicited_by` values are deliberately DIFFERENT, because
the two beliefs are offered as commitments in two different places, and this
file and the register arrived at the same split independently:

  * `EVOL-01` → `s-hook`. Hook option A — *Being the largest and strongest* —
    is the belief in the student's own words, and the hook is the only place on
    the page where it is offered as something to commit to. Rung 2 confronts it
    but cannot elicit it, because by then the bench has spent five environments
    showing that strength is one variation among several.
  * `EVOL-02` → `s-ladder`. Rung 3 asks the student to *say what this means for
    the idea of a "better" animal*, which is where the belief is committed to in
    writing; criterion 5 is the one the student marks themselves against.

── Keys this pass authors that the RENDERER reads (contract R5) ────────

Named explicitly rather than left to be discovered. Every one is measured off
`r_advantage_bench` (`build_ks3.py`, `_b7_need` at the top of it) and the
generic activity shell:

    tabs_label        the mono label over the five environment tabs
    subjects          the five mice — one list, read by every environment, so
                      the student's eye tracks one row while the world changes
    envs              tabs + one panel each, EVERY panel in the document,
                      each carrying `chances`, `whys` and `verdict`
    best_suffix /     appended to the figure by `_B11_AB_CHANCE`, and suppressed
    worst_suffix      entirely on a column with no unique extreme
    progress_suffix   → `_KIND_HEAD_FROM["advantage-bench"]`, composed into
                      `{n} of {total} conditions tried`; the denominator comes
                      from `_KIND_HEAD_TOTAL`, which counts the environments,
                      and the numerator opens at 1 via `_KIND_HEAD_START`
    eyebrow /         the practical shell's head row (`r_activity`)
    heading / prompt

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
component class at (0,1,0), so every colour rule for it is written at (0,2,0)
under `.ks3-dark …` and `ks3_parity.check_dark_text_specificity()` resolves it
on the real cascade. Recorded here because this payload is what feeds it.

── The forward references from B10, resolved ──────────────────────────

`ks3_data/b10/lesson_01_variation_continuous_and_discontinuous.py` carries
`{"unit": "B11", "lesson": "variation-and-competitive-success"}` in `references`
— authored as a reference rather than a `requires` precisely so that it could
ship before this lesson existed, since an unknown `requires` target fails the
build while an unbuilt reference renders as a coming-soon line. **This record
landing resolves it, and nothing in b10-01 changes.** The edge is reciprocated
here as a `requires`, which is Design's own first *Before this lesson* card.

── figures: [] and MEASURED ───────────────────────────────────────────

`<img>`, `<figure>`, `<picture>` and `background-image` each appear ZERO times
on this page — grepped, not assumed — and every one of the ten `<svg>` elements
is UI furniture: the nav chevron, the rail tick, the ladder's tick and cross
marks, the four endmatter arrows. Schema §13 says the same across all four B11
pages.

**The one B11 diagram ruled is the peppered-moth pair, and it belongs to b11-02,
not to this lesson** (schema §14, flag 16: camouflage is irreducibly visual and
`SVG_ART` now draws it inline). Nothing in b11-01 is spatial: the bench draws
five columns of bars out of DOM and the argument is that the column reshuffles,
which is a comparison over time rather than a picture. Declaring a figure slot
here would invent a sourcing task in `docs/ks3/diagram-manifest.md` for a drawing
nothing on the page references. **No figure is needed and none is requested.**

── ⚑ For Mide's science gate ──────────────────────────────────────────

Schema §14 already ruled every NOTES-B11 flag landing on this lesson, on this
run's standing authority, and this pass re-opened none of them:

  * flag 1   **The survival percentages are illustrative.** Ruled acceptable, as
             in B9 and B10, because the page's own legal line says so in front
             of the student: *"The survival percentages are teaching values
             chosen to show how the ranking changes, not measurements."* That is
             MRB-225 performed in the drawing.
  * flag 2   **"Fittest" as best-fitted PLUS reproductive success**, including
             the mayfly-versus-fifty-years comparison. Ruled correct and the
             definition worth having; the mayfly earns its place. Rung 2's
             correct option carries both halves and so does the confrontation.
  * flag 3   **The Grants' finches** — Daphne Major, the 1977 drought, a
             measurable increase in beak depth within one generation, the
             reversal after the 1983 rains. Ruled correct, and *"evolution
             watched rather than reconstructed"* a fair framing. Lifted whole
             into `stretch`.

Two things are reported to Mide as findings rather than stopped on, and both are
COPY rather than numbers — see the notes at the two strings themselves:

  * the `crowded` verdict's second sentence is loose (schema §2), and
  * NOTES-B11 §1.1 overclaims the pale mouse's reversal (schema §11 item 1).
    ⚠️ **The page is right and the notes are wrong. Do not "restore" the notes'
    version.** Measured, pale is 75 in the winter — SECOND, behind thick at 90 —
    and 25 against the owl — SECOND-WORST, above bold at 20. Design's own
    verdict copy is careful and correct. Raising pale to the winter maximum
    would demote the thick coat and destroy the exact reversal rung 3 is built
    on, which is the only extremal reversal on the bench.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes: *an advantage is only ever an advantage in
particular conditions*. The hook's reveal, all five verdicts, both `#s-think`
bodies, the key fact, rung 1's correct option, rung 3's criteria 4 and 5 and the
key note all say it at the same size. The stretch layer adds the Galápagos case
and retracts nothing: it is the same claim in a real population with real
measurements, and it ends on the strongest available point — that no bird ever
changed its own beak, which is `EVOL-02` refuted with forty years of data.
"""


# ── the five mice (page lines 335–341) ───────────────────────────────────
#
# ⚖️ ONE LIST, READ BY EVERY ENVIRONMENT, AND THAT IS THE INSTRUMENT. Design
# keeps `MICE` as a top-level constant and gives each environment only numbers
# and sentences, so the student's eye tracks one row down the bench while the
# world changes underneath it. A per-environment roster would let two panels
# disagree about which animals are on the bench, and the reversal rung 3 asks
# about — thick coat 90 in the winter, 25 in the drought — would quietly become
# a comparison between two different lists. `r_advantage_bench` checks the key
# sets of `chances` and `whys` against these ids in BOTH directions for the same
# reason.
#
# The order is Design's and it is not alphabetical: `big` and `thick` first
# because they are the two a student expects to win, `fast` third because it is
# the one that overturns them, and `pale` last because it is the only variation
# on the bench that is about being SEEN rather than about the body.
SUBJECTS = [
    {"id": "big", "name": "Large, heavy build"},
    {"id": "thick", "name": "Thick coat"},
    {"id": "fast", "name": "Small and quick"},
    {"id": "bold", "name": "Bold and exploratory"},
    {"id": "pale", "name": "Pale sandy fur"},
]

# ── the five environments (page lines 343–393) ───────────────────────────
#
# ⛔ THE NUMBERS ARE THE LESSON, NOT DECORATION. Each column is a ranking, and
# the argument is what happens to a ROW when you read across the five. Two
# reversals are exact and they are the same reversal read in both directions:
#
#     thick    90 (winter, column max)  →  25 (drought, column min)
#     fast     45 (winter, column min)  →  85 (drought, column max)
#
# Rung 3 is built on the first of those, and the drought verdict names both
# halves. ⚠️ Neither may be softened: they are the only extremal reversal on the
# bench, and NOTES-B11 §1.1's claim that `pale` is a third one is measurably
# wrong — see the docstring, and do not "fix" the numbers to match the notes.
#
# `label` is the TAB and `name` is the PANEL HEADLINE and they are not the same
# string: the tab reads "A hard winter" where the panel reads "A hard winter,
# snow for eight weeks". `r_advantage_bench` requires both and says so.
#
# ⚖️ `winter` IS `environments[0]` and therefore the tab the page opens on —
# Design's own `env: 'winter'` — so no opening selection is authored (schema
# §0.4). It is also the right one to open on: it is the environment where the
# thick coat wins, which is the answer a student expects, and the drought is the
# very next tab.
ENVIRONMENTS = [
    {"id": "winter", "label": "A hard winter",
     "name": "A hard winter, snow for eight weeks",
     "note": "Food is scarce and buried, and the cold is relentless. Losing "
             "heat is now the main way to die.",
     "chances": {"big": 70, "thick": 90, "fast": 45, "bold": 55, "pale": 75},
     "whys": {
         "big": "A large body loses heat more slowly than a small one, and fat "
                "reserves last. It also needs more food, which is scarce.",
         "thick": "Insulation is exactly what this winter demands, and it "
                  "costs almost nothing to carry.",
         "fast": "A small body loses heat fast relative to its mass, and speed "
                 "is no defence against cold.",
         "bold": "Willing to search further for buried food, which helps — and "
                 "is exposed to the cold while doing it.",
         # ⚑ 75 is SECOND, behind thick at 90. NOTES-B11 §1.1 says "best in
         # snow"; it is not, and Design's own sentence never claims it is —
         # it says the owl finds pale fur hard to see, which is true and is
         # what the owl panel then reverses. Schema §11 item 1.
         "pale": "Pale fur against snow is difficult for an owl to see, which "
                 "is worth a great deal in a winter with no cover."},
     "verdict": "The thick coat wins, and it is the mouse that will suffer "
                "most in the next environment on the list."},
    # ⚖️ THE REVERSAL, and the panel rung 3 is written about. Same five animals,
    # nothing about any of them changed, and the top and the bottom of the
    # column have swapped ends.
    {"id": "drought", "label": "A long drought",
     "name": "A long drought, no rain for months",
     "note": "Water is the limit, and heat is the danger. Every gram of body "
             "has to be kept cool and supplied.",
     "chances": {"big": 40, "thick": 25, "fast": 85, "bold": 60, "pale": 70},
     "whys": {
         "big": "A big body needs more water and more food, and there is "
                "neither. Size is now a bill rather than an asset.",
         "thick": "The insulation that saved this mouse in winter now traps "
                  "heat it cannot lose. The worst place on the bench to be.",
         "fast": "Small, light, needs little water and cools easily. The "
                 "animal that struggled in January is thriving.",
         "bold": "Finds the few remaining water sources, and takes risks doing "
                 "it.",
         "pale": "Pale fur reflects sunlight and matches dry ground, so it "
                 "stays cooler and stays hidden."},
     "verdict": "The thick coat has gone from best to worst, and the small "
                "quick mouse from worst to best. Nothing about either animal "
                "changed."},
    {"id": "owl", "label": "An owl moves in",
     "name": "A barn owl takes up residence",
     "note": "A new predator hunting at night by sight and sound. The ground "
             "is dark peaty soil.",
     "chances": {"big": 35, "thick": 55, "fast": 80, "bold": 20, "pale": 25},
     "whys": {
         "big": "Slower to reach cover and a larger target. Being conspicuous "
                "has suddenly become expensive.",
         "thick": "Neither helped nor harmed by the coat. This mouse survives "
                  "on average.",
         "fast": "Quick to cover and a small target. Speed is worth more "
                 "tonight than anything else.",
         "bold": "Bold means out in the open more often, which is precisely "
                 "the wrong habit to have when something is hunting.",
         "pale": "Pale fur on dark peat is the most visible thing in the "
                 "field. The camouflage that saved it in snow now advertises "
                 "it."},
     # ⚑ The verdict is CAREFUL where NOTES-B11 §1.1 is not: it says pale fur
     # is a liability here and was an advantage in the snow — directional, and
     # true — and never claims either extreme. 25 is second-worst, above bold
     # at 20. Lifted exactly; the last sentence is the lesson in eight words.
     "verdict": "Boldness and pale fur are the liabilities here — and pale fur "
                "was an advantage in the snow. The variation has not changed; "
                "the background has."},
    {"id": "crowded", "label": "Overcrowding",
     "name": "A mild year, and the population doubles",
     "note": "No shortage of weather to worry about — but too many mice, too "
             "little food, and constant competition for burrows.",
     "chances": {"big": 80, "thick": 50, "fast": 45, "bold": 75, "pale": 50},
     "whys": {
         "big": "Wins direct confrontations over food and burrows. In a crowd, "
                "size finally pays for itself.",
         "thick": "No advantage and no cost in a mild year. Average.",
         "fast": "Quick, but repeatedly displaced from food by larger mice. "
                 "Speed does not win an argument.",
         "bold": "Explores beyond the crowded area and finds unoccupied ground "
                 "and untouched food.",
         "pale": "Colour is irrelevant to this problem, so this mouse sits in "
                 "the middle."},
     # ⚖️ CORRECTED 18 Aug 2026 under this run's science authority. The
     # authoring pass flagged the second sentence as "loose" and lifted it
     # byte-identical, which was the right default — it is not an author's
     # call. Measured against this bench's own numbers it is not loose, it is
     # FALSE, and a student who repeated it would be marked wrong.
     #
     # Design wrote: "Note that the drought’s loser is this environment’s
     # winner." The drought column reads big 40, thick 25, fast 85, bold 60,
     # pale 70 — so the drought's loser is `thick`, and `thick` scores 50 here,
     # middling. The sentence names a relationship the page's own data denies,
     # two panels apart, where a student can check it in four seconds.
     #
     # The TEACHING POINT is untouched and is why this is a repair rather than
     # a cut: `big` does badly in the drought (40, second-worst) and wins here
     # (80, best), which is the reversal the whole lesson turns on. Only the
     # superlative moves — "the drought’s loser" becomes "the mouse that did
     # badly in the drought", which is true of `big` and keeps Design's
     # sentence, rhythm and point. No number was bent to fit the prose; that
     # would have been the other way to make this consistent and it is the
     # wrong way, because the numbers are the evidence the student reads.
     "verdict": "Size wins where the competition is with your own kind rather "
                "than with the weather. Note that the mouse that did badly in "
                "the drought is this environment’s winner."},
    # ⚠️ THE TIE PANEL, AND THE MOST IMPORTANT ONE ON THE BENCH. Four mice on
    # 45 and one on 30, so the column has NO unique maximum — `_b11_ab_extremes`
    # therefore marks nothing best and nothing worst, every bar stays muted, and
    # the verdict does the teaching. Design's own renderer paints four green
    # winners here under a sentence that says none of them helps; schema §2
    # rules the tie and `build_ks3.py` implements it. See the docstring.
    #
    # ⚖️ This is the panel rung 4 is written about and the hand-off to b11-04:
    # the variation that will matter cannot be known in advance, which is why a
    # population needs variation it is not currently using.
    {"id": "disease", "label": "A new disease",
     "name": "A virus sweeps through the population",
     "note": "Nothing to outrun and nothing to hide from. Resistance is "
             "decided by which versions of certain genes an animal happens to "
             "carry.",
     "chances": {"big": 45, "thick": 45, "fast": 45, "bold": 30, "pale": 45},
     "whys": {
         "big": "No protection. Size is irrelevant to a virus.",
         "thick": "No protection. The coat does nothing here.",
         "fast": "No protection. You cannot outrun an infection.",
         "bold": "Actively worse — more contact with more mice means more "
                 "chance of catching it.",
         "pale": "No protection, and no penalty."},
     "verdict": "None of the visible variations helps. Whatever decides who "
                "survives this is something none of these mice can be seen to "
                "have — which is why a population needs variation it is not "
                "currently using."},
]

# ── the four cards in the band section (page lines 396–401) ──────────────
#
# THREE PLUS ONE, AND THE SPLIT IS THE SECTION. Design's `kind` is the mono
# accent tag and it reads "Between members of one species" on the first three
# and "Against everything else" on the fourth — so the card grid says, in its
# own layout, that competition WITHIN a species is the ordinary case and that
# predators and disease are a different kind of filter doing the same job.
#
# `kind` maps to `role`, `name` to `name` and `body` to `body`, which are the
# slots `_rule_card()` reads for them (b7-01's shape exactly). ⛔ There is no
# example line on this page's cards — b10-01's `examples` slot is not authored
# here, because Design draws three paragraphs and no fourth part, and an empty
# one is what MRB-245 was raised to stop.
#
# ⚖️ The fourth card is the one that stops the section being a list of
# resources: it concedes that predators and disease are not competition and
# then says they are the same filter, which is what makes the bench's owl panel
# and disease panel belong on a page about competing.
COMPETE_CARDS = [
    {"role": "Between members of one species",
     "name": "Food and water",
     "body": "The most common competition, and the one that bites first. "
             "Every organism eating the same thing in the same place is a "
             "rival."},
    {"role": "Between members of one species",
     "name": "Space and shelter",
     "body": "Territory, a burrow, a nest site, a place on the rock. Often "
             "more limiting than food, and usually settled by size or by who "
             "arrived first."},
    {"role": "Between members of one species",
     "name": "Mates",
     "body": "Only some individuals breed. This is where fitness is finally "
             "counted, because surviving without reproducing contributes "
             "nothing to the next generation."},
    {"role": "Against everything else",
     "name": "Predators and disease",
     "body": "Not competition exactly, but the same filter: whichever "
             "variations happen to help you avoid being eaten or infected are "
             "the ones that get passed on."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 171 character for character.
    "slug":        "variation-and-competitive-success",
    "title":       "Variation and competitive success",
    "discipline":  "biology",
    "unit":        "evolution-extinction-and-biodiversity",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.INH.05a` — variation meaning some organisms compete more
    # successfully, and which variation helps depending on where the organism
    # is. The `b` clause (that difference repeated over generations) is
    # b11-02's, and `validate()` enforces exactly-once ownership; see the
    # docstring for why the seam is where it is.
    "covers":      ["KS3.B.INH.05a"],
    # Named, used, and owned elsewhere. `05b` is b11-02's and this lesson sets
    # it up without teaching it — the hook's reveal says the winner changes,
    # and nothing here runs a second generation. `INH.06` is b11-03's, and the
    # second confrontation reaches it explicitly: a species superbly suited to
    # one place is badly placed if the place changes, "which is precisely how
    # extinctions happen".
    "touches":     ["KS3.B.INH.05b", "KS3.B.INH.06"],
    "beyond_statutory": False,
    # `genes-and-evolution` at `secure`: the student met variation as data in
    # b10-01 and as species boundaries in b10-05, and this is where the thread
    # is finally used to explain an OUTCOME rather than to describe a pattern.
    # `structure-function` at `secure` for the same reason one step across —
    # every one of the twenty-five rationales on the bench is "how it is built
    # explains what it does", conditioned on where it is standing, and Design's
    # own *Connects to* card points at b7-02, which is the structure-function
    # lesson.
    "threads":     [{"id": "genes-and-evolution", "level": 3},
                    {"id": "structure-function", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. `variation-continuous-
    # and-discontinuous` is the b10-01 edge this lesson RESOLVES (see the
    # docstring): b10-01 carries the forward reference in dict form precisely
    # so it could ship before B11 existed. Both are bare slugs — `requires`
    # resolves across the whole key stage.
    "requires":    ["variation-continuous-and-discontinuous",
                    "predator-and-prey"],
    "assumes":     [],
    # Design's "Connects to" card, in her order — PLUS one.
    #
    # ⚠️ `when-the-environment-changes-extinction` is NOT on either endmatter
    # card. It is here because `#s-think`'s second body links to it inline and
    # `rich()` strips the anchor, so the destination would otherwise be lost
    # entirely; b9-02 and b9-03 both carry the same edge for the same reason
    # ("What could not be lifted" 1). All three are bare slugs: b11-02 and
    # b11-03 are in THIS unit, and `leaves-built-for-the-job` resolves because
    # `references` accepts a bare slug for a lesson that exists — the dict form
    # b10-01 needed was for a unit that did not yet.
    "references":  ["natural-selection", "leaves-built-for-the-job",
                    "when-the-environment-changes-extinction"],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Selection pressures, adaptation, and the evidence for "
                   "evolution from the fossil record and from living "
                   "populations.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "No two individuals in a population are identical. Most of "
                    "the time that is a curiosity. When something goes wrong — "
                    "a drought, a cold winter, a new predator — it becomes the "
                    "most important fact about them.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 302–307). `s-three` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate — Design's own `isDone()`, page lines 423–424. `short`
    # and `label` are her `RAIL_SHORT` and `RAIL` strings, "Until it is not"
    # and "Competing for" included, which are half-sentences by design because
    # the rail is 104px wide. Shipping three fails
    # `check_rail_matches_design`; see the docstring.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Until it is not",
         "done_when": "committed"},
        # Design's own threshold, kept: three of the five seen (page line 423).
        # Sticky by her design and monotonic by ours — `seen` is a set that is
        # only ever added to, and there is no reset to untick it.
        {"anchor": "s-bench", "short": "BENCH", "label": "Change the world",
         "done_when": "three_conditions_seen"},
        # The MIRROR. Design gives it the bench's predicate character for
        # character one line further down, so the stop ticks the moment the
        # bench does and nothing ticks on load.
        {"anchor": "s-three", "short": "COMPETE", "label": "Competing for",
         "mirrors": "s-bench",
         "done_when": "three_conditions_seen"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer
    # (schema §6: all four B11 hooks are four-option single-choice with the
    # reveal behind a commitment, and no option is correct).
    #
    # ⚖️ THE OPTION SET IS THE LESSON'S ERROR SPACE, and D is the refusal the
    # reveal endorses. A, B and C each name a fixed winning variation — and the
    # bench then shows each of the three losing badly somewhere: strength loses
    # the drought, speed loses the crowded field, camouflage is irrelevant to
    # the disease. **OPTION A IS `EVOL-01`**, and it is the reason this section
    # is that belief's `elicited_by`.
    "phenomenon": {
        "kind": "narrative",
        "title": "A thick coat is an advantage. Until it is not.",
        "prompt": "Two mice in the same litter, one with a noticeably thicker "
                  "coat. Which of them does better depends entirely on what "
                  "happens next — and the same is true of every difference "
                  "between them: size, speed, appetite, colour, boldness.",
        "commit": "Which variation in a population is the best one to have?",
        "options": [
            # A: EVOL-01, word for word, and this is its `elicited_by`
            "Being the largest and strongest",
            # B: the same error with a different trait — the owl panel's winner
            "Being the fastest",
            # C: the same error again — and the disease panel answers it
            "Being best camouflaged",
            # D: the refusal, which is what the reveal endorses
            "It depends entirely on the conditions",
        ],
        # The two `<em>` runs survive: `rich()` renders them, and "in a
        # particular set of conditions" is the whole answer.
        "reveal": "There is no best one. An advantage is only ever an "
                  "advantage <em>in a particular set of conditions</em>, and "
                  "the conditions change. Being large helps you win fights and "
                  "costs you more food; a thick coat saves you in a cold "
                  "winter and overheats you in a warm one. The bench below "
                  "runs the same population through five different "
                  "environments and the winner changes every time.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §12's pre-allocation for b11-01, and the two beliefs Design's
    # `#s-think` quotes, in her page order. Both statements are her own bytes,
    # page lines 172 and 177, in register voice.
    #
    # ⊕ The `EVOL` prefix row was opened in
    # `docs/ks3/misconception-register.md` by the register pass during this
    # run, and its rows for these two ids agree with these on all three fields.
    # That file is not this pass's to edit (contract §0); read at the end of
    # the run because it was in flight. See the docstring.
    #
    # ⛔ `EVOL-09` is this lesson's named SPARE and is NOT claimed: two beliefs
    # were found and two ids were used. It stays permanently unused rather than
    # being re-pointed at anything later (schema §12).
    #
    # The two `elicited_by` values are deliberately different — hook option A
    # for the first, rung 3's ask for the second — and the reasoning is in the
    # docstring. Both `confronted_by` values are `s-think`, the confrontation
    # block's emitted anchor, and all four resolve against the BUILT page
    # (MRB-244).
    "misconceptions": [
        {"id": "EVOL-01",
         "statement": "Survival of the fittest means the strongest survive.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "EVOL-02",
         "statement": "Some individuals are just better than others.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B11, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ EVERY ONE IS GLOSSED WITH ITS CONDITION ATTACHED, because a chip that
    # said "advantage: a variation that helps an organism survive" would teach
    # the exact belief the page spends five environments taking apart.
    # `variation` is deliberately absent — it is b10-01's chip and this lesson
    # uses it rather than introducing it — and so is `natural selection`, which
    # is b11-02's and is not taught here at all.
    "vocabulary": [
        {"term": "competition",
         "definition": "Two or more organisms needing the same limited "
                       "resource, so that one getting it means another does "
                       "not.",
         "note": "Usually fiercest between members of the same species, "
                 "because they need exactly the same things."},
        {"term": "resource",
         "definition": "Something an organism needs and there is not enough "
                       "of: food, water, space, shelter, a mate.",
         "note": "More are born than the resources can support. That is what "
                 "makes it a competition."},
        {"term": "advantage",
         "definition": "A variation that makes an individual more likely to "
                       "survive and reproduce in the conditions it is "
                       "actually in.",
         "note": "Always in some conditions. There is no such thing as an "
                 "advantage in general."},
        {"term": "adapted",
         "definition": "Suited to a particular environment by the variations "
                       "an organism happens to have.",
         "note": "Biologists say well adapted to a place, never advanced or "
                 "superior."},
        {"term": "fitness",
         "definition": "How well an individual is fitted to its current "
                       "conditions, counted by how many surviving offspring "
                       "it leaves.",
         "note": "Nothing to do with strength or with how long an organism "
                 "lives."},
        {"term": "environment",
         "definition": "Everything around an organism that affects it: the "
                       "weather, the ground, the food, the predators, the "
                       "other members of its own species.",
         "note": "Change it and the ranking changes with it."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>`, `<picture>` and
    # `background-image` each appear zero times on this page — grepped — and
    # all ten `<svg>` elements are chrome. Schema §13 says the same of all four
    # B11 pages. The one B11 diagram ruled is the peppered-moth pair and it is
    # b11-02's, not this lesson's; nothing here is spatial. See the docstring.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b11/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md §2. The
        # read sites are listed in the docstring; `run_label`, `reset_label`,
        # `verdicts`, an opening environment, and both `env` and `seen` are
        # deliberately absent and each has its own reason there.
        {"type": "advantage-bench", "id": "change-the-world-not-the-mice",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · one population, five conditions",
         "heading": "Change the world, not the mice",
         "prompt": "The same five mice every time. Only the conditions "
                   "change, and the survival column changes with them. Watch "
                   "one mouse across all five and see how often the same "
                   "animal is at the top and at the bottom.",

         # The mono label over the five tabs, and the mono word at the end of
         # the head readout. `_KIND_HEAD_FROM` composes
         # "{n} of {total} conditions tried" from the suffix, `_KIND_HEAD_TOTAL`
         # counts the environments and `_KIND_HEAD_START` opens the numerator
         # at 1 — so the denominator is a fact about the payload rather than a
         # number authored twice, and the resting bytes read "1 of 5 conditions
         # tried" exactly as Design's first paint does.
         #
         # ⚠️ NO LEADING SPACE. Schema §2 quotes Design's JS literal
         # `' conditions tried'`; the composer is `"{n} of {total} %s"`, so the
         # space is the format's and a second one here would ship "1 of 5␣␣
         # conditions tried". Reported as a schema/engine disagreement — the
         # built bytes match the page either way only in this spelling.
         "tabs_label": "The conditions",
         "progress_suffix": "conditions tried",

         # ⛔ THESE TWO CARRY THEIR OWN SEPARATOR, and that is not a slip. The
         # renderer composes `"%d%s%s" % (chance, "% survive", suffix)`, so the
         # suffix is concatenated straight onto "45% survive" with nothing
         # between — the middot and the spaces are part of the string Design
         # wrote. ⚖️ AND BOTH CARRY THE WORD "here", which is the instrument's
         # whole argument said out loud: nothing on this bench is best, only
         # best in this column. Suppressed entirely on a column with no unique
         # extreme, which is the `disease` panel — see the docstring.
         "best_suffix": " · best here",
         "worst_suffix": " · worst here",

         "subjects": SUBJECTS,
         "envs": ENVIRONMENTS},

        # #s-three — the band panel, rail stop 3, mirroring `s-bench`. Design
        # draws eyebrow, statement, four cards, key fact — and NO closing
        # paragraph, so `close` is absent and the ordering finding b9-01
        # reported (`r_rule` emits the nested key fact before `close`) cannot
        # arise on this page.
        {"type": "rule", "anchor": "s-three",
         "eyebrow": "What they are competing for",
         # ⚖️ Malthus in seven words, and it is the premise the whole unit
         # needs: without it, variation is a curiosity rather than a filter.
         "statement": "More are born than can possibly survive.",

         "cards": COMPETE_CARDS,

         # Design nests the key fact inside this section (page lines 158–161)
         # on the CARD ground with the 5px accent offset shadow. `card`,
         # because the section itself is `--ks3-band` and band on band is
         # invisible — the same arrangement and the same reason as b7-01's,
         # b8-01's, b9-01's and b10-01's.
         "key_fact": {"ref": "no-generally-superior-individual",
                      "ground": "card"}},

        {"type": "misconception", "id": "fittest-is-not-strongest",
         "anchor": "s-think", "targets": "EVOL-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-three on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 161
    # and identical to payload schema §9's b11-01 entry.
    #
    # ⚖️ ITS LAST CLAUSE IS THE UNIT'S FOUNDATION and no later pass may drop
    # it: "so there is no such thing as a generally superior individual" is the
    # conclusion `EVOL-02` denies, and the two clauses before it are the
    # premises that force it — resources are limited, and the conditions
    # change.
    "key_facts": [
        {"id": "no-generally-superior-individual",
         "text": "Individuals of a species vary, and resources are limited, so "
                 "some compete more successfully than others. Which variation "
                 "gives an advantage depends entirely on the conditions, and "
                 "the conditions change — so there is no such thing as a "
                 "generally superior individual.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, no
        # `sc-if`, schema §7), so it is a `confrontation` and not a `predict`,
        # it is not a rail stop, and it emits no completion contract. Contract
        # R1's `predict` branch applies where `#s-think` gates a reveal behind
        # a commitment; no B11 page does.
        {"id": "fittest-is-not-strongest",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "EVOL-01",
         "statements": [
             # EVOL-01. ⚑ NOTES-B11 flag 2, ruled correct in schema §14: the
             # definition is best-fitted PLUS reproductive success, and the
             # mayfly earns its place. The `<em>` run is kept — `rich()`
             # renders it — because "best fitted to these conditions" is the
             # definition rung 2 marks, and the key-fits-a-lock image is what
             # makes "fitted" mean something other than "fit".
             #
             # ⚖️ Note the order of the two halves. The paragraph spends five
             # sentences on best-fitted and then says "and the measure is not
             # survival at all in the end" — so a student who stops early has
             # the first half right, and a student who reads on gets the half
             # that actually decides it. Do not compress them.
             {"quote": "Survival of the fittest means the strongest survive.",
              "body": ["Fittest here means <em>best fitted to these "
                       "conditions</em>, in the sense that a key fits a lock — "
                       "not fittest in the sense of a gym. It is regularly the "
                       "small, the drab and the unimpressive that come "
                       "through. In a drought, the animal that needs least "
                       "water wins; in a famine, the one that survives on "
                       "least food; against a new disease, the one that "
                       "happens to be resistant, which may be the sickliest "
                       "animal in the group in every other respect. A stag "
                       "with enormous antlers wins fights and starves in a "
                       "hard winter carrying them. And the measure is not "
                       "survival at all in the end — it is how many surviving "
                       "offspring an individual leaves. An organism that lives "
                       "fifty years and never breeds has a fitness of zero; a "
                       "mayfly that lives one day and lays five hundred eggs "
                       "has done everything that counts."]},
             # EVOL-02. The three `<em>` runs are the TEST, stated as one
             # phrase biologists use against two they do not, and they are the
             # reason this body cannot be flattened: "well adapted to a
             # particular environment" against "advanced" or "superior" is the
             # whole correction, and it lands as a contrast or not at all.
             #
             # ⚠️ THE LINK IS GONE AND THE TITLE IS IN ITS PLACE — "What could
             # not be lifted" 1. Design's anchor text is a POSITION ("the
             # subject two lessons from here"), which a stripped tag would
             # leave unfollowable and which claims an ordering a school's own
             # scheme may not honour. The edge is carried in `references`.
             {"quote": "Some individuals are just better than others.",
              "body": ["Better at what, and in what conditions? Change the "
                       "environment on the bench above and the ranking "
                       "reshuffles, using the same five animals with the same "
                       "five sets of characteristics. A large mouse dominates "
                       "a food pile and needs more of it; a bold mouse finds "
                       "new food first and meets the owl first; a thick coat "
                       "is life in January and a burden in July. This is why "
                       "biologists are careful to say <em>well adapted to a "
                       "particular environment</em> rather than "
                       "<em>advanced</em> or <em>superior</em>, and it is not "
                       "a politeness. A species that is superbly suited to one "
                       "place is, by that same specialisation, badly placed if "
                       "the place changes — which is precisely how extinctions "
                       "happen, and it is the subject of When the environment "
                       "changes: extinction."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN AS DRAWN, RUNG 2 REPAIRED AT THE
    # DISTRACTORS. rung 1 correct 10w against 10 / 12 / 7 (the longest option
    # on the rung is a DISTRACTOR); rung 2 correct 12w against 5 / 6 / 6 as
    # drawn — gap 6 and ratio 2.00, tripping BOTH thresholds — repaired to 12w
    # against 13 / 13 / 15. **No correct option was shortened, no `answer`
    # index moved, no correction edited and no distractor padded with filler:
    # each of the three gained the correct option's own second clause, keeping
    # its belief exactly.** Full before/after working in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Advantage in context",
            "q": "Pale sandy fur is an advantage in snow and a disadvantage on "
                 "dark soil. What does that show?",
            # Design's four, UNTOUCHED. All four answer "what does that show?"
            # in the same grammar, three of them beginning "That…" and stating
            # a wrong lesson, and the longest option on the rung is a
            # distractor. That is the MRB-177 construct arrived at by Design.
            #
            #   A  correct — the lesson the bench draws five times
            #   B  EVOL-02's shape: a variation ranked in general
            #   C  authored belief: the animal adapts to suit the ground —
            #      the Lamarckian error b11-02 owns, met here first
            #   D  authored belief: one variation outranks the rest everywhere
            "options": [
                "Whether a variation is an advantage depends on the "
                "environment",
                "That pale fur is generally a poor variation to have",
                "That the mouse can change its fur colour to suit the ground",
                "That camouflage matters more than anything else",
            ],
            "answer": 0,
            # All three corrections are Design's, byte-identical.
            "feedback": {
                1: "It is excellent in one of the two environments described. "
                   "General is the word that does not apply.",
                2: "It cannot. The fur an animal has is the fur it has — the "
                   "environment does the choosing, not the mouse.",
                3: "It mattered against the owl and was irrelevant to the "
                   "disease. That is the same point again.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "What does \"fittest\" mean in \"survival of the fittest\"?",
            # ⊕ MRB-177: THE THREE DISTRACTORS ARE REPAIRED, THE CORRECT
            # OPTION AND THE ANSWER INDEX ARE DESIGN'S. As drawn, the correct
            # option stated a two-part definition (fitted AND offspring) while
            # each distractor named one property in a noun phrase, so it was
            # longer by construction — 12w against 5 / 6 / 6. Each distractor
            # now carries the same second clause the correct option does,
            # joined with the same ", and", and each added clause RESTATES its
            # own belief rather than diluting it:
            #
            #   A  EVOL-01 — strength wins → and wins a direct fight. Design's
            #      correction answers the arena as well as the trait.
            #   B  correct, unchanged: fitted to CURRENT conditions, and
            #      offspring. "Current" is the word the whole lesson turns on.
            #   C  longevity → and avoiding dying young, which is longevity
            #      said twice, which is what the belief is.
            #   D  "most advanced" → and highest up the tree of life: the
            #      scala naturae in the student's own words.
            "options": [
                "The strongest and healthiest individuals, and the ones that "
                "win a direct fight",
                "Best fitted to the current conditions, and leaving the most "
                "surviving offspring",
                "The individuals that live the longest, and the ones that "
                "avoid dying young",
                "The most advanced or highly evolved, and the ones highest up "
                "the tree of life",
            ],
            "answer": 1,
            # ⛔ ALL THREE CORRECTIONS ARE DESIGN'S, BYTE-IDENTICAL AND
            # UNEDITED — MRB-177 forbids touching a correction, and none needed
            # touching: each still answers the belief its own option states,
            # and A's answers the repaired form better than the original.
            "feedback": {
                0: "Strength is one variation among many, and it is often the "
                   "wrong one. In a drought the animal that needs least water "
                   "wins.",
                2: "Length of life counts for nothing on its own. An organism "
                   "that lives fifty years and never breeds leaves nothing "
                   "behind.",
                3: "There is no ranking of advancement in biology. A bacterium "
                   "that thrives where nothing else can is superbly fitted to "
                   "it.",
            }},
        "explain": {
            # ⚖️ THE RUNG THE BENCH IS BUILT FOR, and `EVOL-02`'s
            # `elicited_by`. It hands the student the one exact reversal on the
            # bench — thick coat 90 then 25 — and asks for both results and
            # then for what it means for the idea of a "better" animal.
            # Criterion 3 is the load-bearing one: the mouse itself did not
            # change. Criterion 5 is the belief, in the student's own hand.
            "title": "Rung 3 · Explain a reversal",
            "q": "On the bench, the thick-coated mouse is the most likely to "
                 "survive the winter and the least likely to survive the "
                 "drought. Explain both results, and say what this means for "
                 "the idea of a \"better\" animal.",
            "field_label": "Your explanation",
            "placeholder": "In winter the thick coat…",
            "success": [
                "Says the thick coat reduces heat loss, which is the main "
                "danger in a hard winter.",
                "Says in a drought the same coat traps heat the animal needs "
                "to lose.",
                "Makes clear the mouse itself did not change — only the "
                "conditions did.",
                "Concludes that an advantage is relative to a particular "
                "environment.",
                "States that there is therefore no generally better "
                "individual, only one better suited to current conditions.",
            ]},
        "produce": {
            # ⚖️ THE HAND-OFF TO B11-04, and the reason the `disease` panel
            # exists. It asks the student to argue for variation that is doing
            # nothing at all right now, which is the hardest idea in the unit
            # and the one gene banks are for. Criterion 4 is where extinction
            # risk enters, one lesson before b11-03 owns it.
            "title": "Rung 4 · Take it somewhere new",
            "q": "On the disease bench, none of the five visible variations "
                 "protects the mice. Explain why a population still benefits "
                 "from having lots of variation it is not currently using, and "
                 "what that implies for a population reduced to very few "
                 "individuals.",
            "field_label": "Your answer",
            "placeholder": "The variation that matters against a new disease…",
            "success": [
                "Says the variation that will matter against a future threat "
                "cannot be known in advance.",
                "Says a population with more variation is more likely to "
                "contain some individuals that happen to survive it.",
                "Says those survivors pass their versions on, so the "
                "population recovers.",
                "Says a population reduced to very few individuals has lost "
                "most of its variation.",
                "Concludes that such a population is much more likely to be "
                "wiped out by a change it happens to be unsuited to.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Individuals within a species vary, and more offspring are "
                "produced than the resources can support, so they compete — "
                "for food, water, space, mates and escape from predators. "
                "Variations that suit the current conditions make an "
                "individual more likely to survive and reproduce. Which "
                "variations those are depends on the conditions, so no "
                "variation is an advantage in general.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B11 flag 3, ruled correct in schema §14: Daphne Major, the 1977
    # drought, a measurable increase in beak depth within one generation, the
    # reversal after the 1983 rains, and "evolution watched rather than
    # reconstructed" as a fair framing. Do not soften any of it.
    #
    # ⚖️ MRB-225 holds: the layer applies the lesson's own claim to a real
    # population with real measurements and retracts nothing above it. Its
    # second-to-last sentence is the whole lesson in one data set, and the last
    # clause of that sentence — "with no bird ever changing its own beak" — is
    # the b11-02 Lamarckian error refused in advance.
    "stretch": [
        {"type": "explainer", "id": "the-grants-and-the-finches",
         "text": "Peter and Rosemary Grant spent forty years measuring finches "
                 "on Daphne Major, a small island in the Galápagos, catching "
                 "and weighing essentially every bird on it year after year. "
                 "In the drought of 1977 the small soft seeds ran out and only "
                 "the large tough ones were left, and the finches with "
                 "slightly deeper, stronger beaks survived at a much higher "
                 "rate. The average beak depth in the population measurably "
                 "increased in a single generation. Then in 1983 came "
                 "exceptional rains, the small soft seeds returned in "
                 "abundance, and the average beak size went back down. That is "
                 "the whole of this lesson in one data set: the same "
                 "variation, an advantage in one year and a disadvantage six "
                 "years later, with no bird ever changing its own beak. It is "
                 "also one of the few places where evolution has been watched "
                 "happening rather than reconstructed afterwards."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination
    # on the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to test a variation against conditions of your "
                      "own?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 292) and nothing in it is a safety
    # instruction — it is a note about where the numbers came from and what the
    # bench leaves out. Routing it through `safety_note` would print it in the
    # treatment reserved for "never light a candle without an adult".
    #
    # ⚑ NOTES-B11 flag 1 lands here, and this line is where the page is honest
    # about it in front of the student: the percentages are teaching values,
    # said at the size that is true (MRB-225). Its second sentence is the more
    # interesting half — it names the simplification the bench MAKES, one
    # variation per mouse, which is the assumption rung 3 quietly relies on.
    "convention_note": "The survival percentages are teaching values chosen to "
                       "show how the ranking changes, not measurements. Real "
                       "fitness depends on many characteristics at once, on "
                       "chance, and on what the rest of the population is "
                       "doing; the bench isolates one variation per mouse to "
                       "make the point readable.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is `interpret observations and data, including identifying
    # patterns and using data to draw conclusions` (ANA.03) performed rather
    # than described — the student reads five columns and the pattern is that
    # the ranking moves — and rung 3 is ANA.04, an explanation of data in
    # relation to a claim. Nothing here is measured, planned or collected by
    # the student, so neither the experimental strand nor `measurement` is
    # claimed even though the bench prints numbers.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
