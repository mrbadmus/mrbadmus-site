"""B5 L6 — Flowers and pollination (SYSTEM).

Authored against Design's approved page,
`KS3 B5 lessons/b5-06-flowers-and-pollination.dc.html` (584 lines), under the
MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", none of which is a
sentence of science. The nine parts, the nine jobs, the five design rows, the
four hook options and all four ladder rungs came out of
`node tools/extract_design_payload.js`, not off a keyboard.

── `covers` is the SUB-ID, not the whole bullet ─────────────────────────

`KS3.B.REP.02` is *"reproduction in plants, including flower structure, wind
and insect pollination, fertilisation, seed and fruit formation and dispersal,
including quantitative investigation of some dispersal mechanisms"*, and
`ks3_data/substatements.py` splits it into three. This lesson owns
**`KS3.B.REP.02a`** — flower structure, and wind and insect pollination. It
must NOT claim `REP.02` whole: `fertilisation-seeds-and-fruit` owns `02b` and
`seed-dispersal` owns `02c`, and §5.7's exactly-once rule would fail the build
on the overlap. This page stops at the moment the pollen lands and says so in
its own key fact — *"the next lesson is about what happens after the pollen
lands"*.

── ⚠️ TELEOLOGY IS EXCLUDED, AND THE PAGE IS BUILT AROUND THE EXCLUSION ──

NOTES-B5 flag 44 binds here and on `seed-dispersal`. A flower does not have a
delivery problem because it wants offspring; it has structures whose
consequences are reproductive. Nothing authored in this module — no `demand`,
no definition, no caption, no `done_when` — says *so that*, *wants to* or
*tries to*, and the vocabulary definitions below were written against that
constraint rather than compressed from the job strings by habit.

Three of Design's own strings sit close to the line and are lifted whole
anyway, because MRB-205 says the page wins and because none of them attributes
intention to a plant. They are reported rather than softened:

  * the big question — *"a reproductive organ with a delivery problem"*. A
    problem stated as a situation (the gametes are in two places, the plant
    cannot move), not as a want.
  * the hook reveal — *"grass throws its pollen into the air and hopes"*. The
    verb belongs to the sentence's rhetoric, and the same sentence immediately
    reduces it to arithmetic: *"a wind-pollinated plant compensates with
    quantity"*.
  * the nectary's *why* and the DESIGNS rows — *payment*, *courier*, *pays the
    visiting insect for its trouble*. This is an economic metaphor about a cost
    the plant measurably incurs, which is the opposite move from a teleological
    one: it explains the structure by what it costs rather than by what it is
    for.

── The flagship: nine parts, and every distractor is a real job ─────────

`#s-parts` is `flower-jobs`, on `ks3-block ks3-dark ks3-practical` (page line
104), so `practical` is MEASURED from Design's own markup — the table in
`ks3_data/b5/__init__.py` — rather than inherited from the hook above it.

⚖️ **Every wrong option is the correct job of a different part**, drawn from
the shared pool of nine. NOTES-B5 §2.4 is explicit that inventing wrong answers
destroys the instrument's second purpose, and the page says the same thing to
the student in its own prompt: *"Every wrong option here is the right answer
for a different part, so a guess still teaches you something."* Two of the four
option sets are built from that rule in a way that carries the lesson's third
misconception on its own: `ovule` lists `ovary` and `ovary` lists `ovule`, so
the confusion between the container and the thing contained is elicited by the
instrument and then answered in the ovule's `why`.

── One rail stop comes off, and it is the defect B4 found on every page ─

Design draws FOUR stops and `#s-designs` ticks on `Object.keys(s.opened).length
>= 9` (page line 421) — the INSTRUMENT's predicate, character for character,
one section to the left (page line 420). MRB-208 ruled the rail is
completion-based and carries only sections that require the student to do
something; `#s-designs` is an eyebrow, a display statement, a lede, five static
comparison rows and a key fact, with no control, no commitment and no field.
`ks3_parity.check_rail_reachable` would fail it for exactly that. Inventing a
demand Design did not draw is closed to this build. So the lesson declares
THREE stops — the same call, the same reasoning and the same shape as b4-01's
`#s-parts`, b4-03's `#s-built`, c1-02's `#s-matrix`, c1-05's `#s-scale`,
b3-01's `#s-nutrients` and b3-02's `#s-limits`. The section keeps its anchor,
so every hash link into it still works.

── What could not be lifted, and why ────────────────────────────────────

1. **The `#s-designs` LEDE.** Design writes *"Read down the column. Every
   difference follows from one decision — whether the pollen is going to be
   carried by an animal or by the air."* `r_comparison` has an eyebrow, a
   display statement, columns, rows and a nested key fact, and no lede slot.
   b4-03 gave up the identical paragraph in the identical position for the
   identical reason.

   ⚠️ **This one is not the same kind of loss as b4-03's, and it is reported
   as a finding rather than as housekeeping.** b4-03's lede was a pointer at
   another lesson, which §4.6's single-source rule turns into an edge. This one
   is the organising claim of the section: that every row below it follows from
   a single decision. The rows still say it five times over and the key note
   says it once more, so nothing is left unsaid — but the sentence that names
   the structure of the argument is gone. The fix, if it is to win, is a `lede`
   slot on `r_comparison`, which is an engine change this pass does not own.

2. **The instrument's section heading loses its `<h2>` level.** Design draws
   *"What is each part actually for?"* as an `<h2>` inside `#s-parts` beside a
   mono counter. It is authored as the instrument's `heading` and the renderer
   decides the tag. No word changes.

3. **The two figure ids leave their mono type.** Design sets
   `b5-flower-parts-labelled` and `b5-wind-vs-insect` in
   `var(--ks3-font-mono)` inside the legal sentence; a foot line is escaped, so
   they render in body copy. The words are unchanged. b4-01 resolved the
   identical sentence the identical way.

4. **Design draws TWO endmatter link cards; the engine emits one.** Her "Next
   in this unit" (`fertilisation-seeds-and-fruit`) and "Connects to"
   (`gametes-and-fertilisation`, `pollinators-and-food-security`) are one card
   in `r_endmatter`, headed by `connects_heading`. All three links live in it,
   the forward one first. b3-01, b4-01 and b4-03 resolved the identical layout
   the identical way. The heading "Next in this unit" is what is given up; no
   link is.

5. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

⚑ MRB-177 LENGTH PARITY — MEASURED, AND RUNG 2 IS A TELL. NOT REWRITTEN.
  rung 1 (recall): correct 9w against distractors of 8 / 7 / 7. Clean.
  rung 2 (apply):  correct **14w** against a longest distractor of **10w**.
  `verify_ks3.length_tell` fires at a gap of ≥4, so this trips it.

  It is a tell exactly as Design drew it, and it is NOT rewritten here, for the
  reason the `KNOWN_TELLS` register itself gives: rewriting a distractor
  changes what a marked question measures, and that is Mide's gate, not an
  authoring pass's. `verify_ks3.py` is also an engine-owned file this pass does
  not edit. The entry that registers it is
  `("flowers-and-pollination", "ladder apply")`, and adding it is the
  commander's call.

  Worth knowing before that call is taken: the correct option is
  *"It is wind-pollinated — it has nothing to attract with because it attracts
  nothing"*, and the em dash counts as a token under `[^\\s]+`. Without it the
  option measures 13w against 10w and does not trip the gate at all. The tell
  is one punctuation mark wide.

⚑ For Mide's science gate — NOTES-B5 §3 flags landing on THIS lesson:
  * flag 31 — the nectary as a part in its own right, one of nine. Not every
    textbook does that, and it is the ninth tab of the flagship.
  * flag 32 — *"some patterns are only visible in ultraviolet light, which bees
    can see and we cannot."* In the petal's `why`.
  * flag 33 — Darwin's orchid: 1862 prediction, *praedicta* named 1903 (the
    page says "forty-one years later"), first filmed feeding "another ninety
    years" after that. Dates and rounding, in the stretch layer.
  * flag 34 — *"a large share of what the world eats"*, unquantified, in the
    second confrontation.
  * flag 13 — `b5-flower-parts-labelled` and `b5-wind-vs-insect` are named in
    Design's legal line and neither is in `docs/ks3/diagram-manifest.md`.
    Declared here at `status: "needed"` (§4.10, not a build blocker) so they
    are tracked sourcing tasks rather than dangling references. Nothing is
    invented to fill them. Flag 13 asks for a ruling on WHAT is illustrated
    before anything is commissioned; the captions below are what this page
    teaches and no more.

⚑ MISCONCEPTION IDS — THE PRE-ALLOCATION AND NOTES-B5 DISAGREE, AND THE
  PRE-ALLOCATION IS FOLLOWED. This lesson was allocated `REPRO-11` and
  `REPRO-12` by the commander because five parallel authors collided on B4's
  family. NOTES-B5 §5 says something different: that `REPRO-11` is the
  attribution error in `lifestyle-and-the-developing-foetus` — *"the statement
  it confronts is a reasoning error about attribution rather than a factual
  error about biology"* — and that the family runs `REPRO-01` to `REPRO-17`.
  Those two numberings cannot both hold. The allocation is followed because it
  is the one written for a parallel run; the collision is reported rather than
  resolved here, because `docs/ks3/misconception-register.md` is the
  commander's file and B5's REPRO entries are not in it yet.

  The third belief this page confronts takes **`REPRO-22`**, as instructed.
"""

# ── the nine jobs (page lines 325–335, via extract_design_payload.js) ────
#
# The shared pool. Every part's four options are keys into THIS dict, which is
# what makes each distractor another part's correct answer rather than an
# invention — NOTES-B5 §2.4, and the page's own prompt says it to the student.
JOBS = {
    "pollen":  "Makes pollen grains, each carrying a male gamete nucleus.",
    "hold":    "Holds the anther up and out, where pollen can be taken away.",
    "catch":   "A sticky or feathery surface that catches pollen grains.",
    "route":   "A stalk that raises the catching surface and gives the pollen "
               "tube its route down.",
    "ovary":   "Contains the ovules, and becomes the fruit after "
               "fertilisation.",
    "ovule":   "Contains a female gamete nucleus, and becomes the seed after "
               "fertilisation.",
    "attract": "Attracts insects by colour and scent, and gives them a "
               "platform to land on.",
    "protect": "Encloses and protects the whole flower while it is still a "
               "bud.",
    "pay":     "Produces a sugary liquid that pays the visiting insect for "
               "its trouble.",
}

# ── the nine parts (page lines 337–365) ─────────────────────────────────
#
# `group` is Design's mono alert-coloured tag beside the part name, and it is
# science: it is the only place on the page that assigns each part to male,
# female or neither, which is exactly what rung 3 asks the student to do.
# `options` are the four job KEYS shown, in Design's order — the correct one is
# first in every set, and the renderer is responsible for not making that a
# tell (the page shuffles nothing; A is always right, which is a finding
# reported to the commander, not something this module can fix by reordering
# without changing what the student reads).
PARTS = [
    {"id": "anther", "label": "Anther", "name": "Anther",
     "group": "Male part · stamen", "answer": "pollen",
     "options": ["pollen", "hold", "catch", "ovule"],
     "why": "Pollen grains are not gametes and it is worth being exact: each "
            "grain is a tough case carrying a nucleus that will become the "
            "male gamete. The anther’s whole job is manufacture and "
            "release — it splits open when the pollen is ready."},

    {"id": "filament", "label": "Filament", "name": "Filament",
     "group": "Male part · stamen", "answer": "hold",
     "options": ["hold", "route", "pollen", "protect"],
     "why": "A stalk, and position is everything. In an insect-pollinated "
            "flower it puts the anther exactly where a visiting insect must "
            "brush past it; in a wind-pollinated one it dangles the anther "
            "outside the flower where the wind can shake it."},

    {"id": "stigma", "label": "Stigma", "name": "Stigma",
     "group": "Female part · carpel", "answer": "catch",
     "options": ["catch", "attract", "route", "ovary"],
     "why": "The receiving surface, and its texture tells you how the pollen "
            "arrives. Sticky and small means pollen is being delivered by an "
            "animal; large and feathery means it is being fished out of "
            "moving air."},

    {"id": "style", "label": "Style", "name": "Style",
     "group": "Female part · carpel", "answer": "route",
     "options": ["route", "hold", "catch", "pay"],
     "why": "Two jobs in one stalk. It holds the stigma up where pollen will "
            "reach it, and once a grain has landed the pollen tube grows down "
            "through it to the ovary — which is the whole of the next "
            "lesson."},

    {"id": "ovary", "label": "Ovary", "name": "Ovary",
     "group": "Female part · carpel", "answer": "ovary",
     "options": ["ovary", "ovule", "protect", "catch"],
     "why": "Note what it becomes. Every fruit you have ever eaten was the "
            "ovary of a flower, swollen after fertilisation — which is "
            "why a pea pod, a tomato and an apple are all fruits whatever a "
            "greengrocer calls them."},

    # ⚖️ This `why` is where REPRO-22 dies. The option set above it is the
    # elicitation: `ovule` and `ovary` each carry the other as a distractor.
    {"id": "ovule", "label": "Ovule", "name": "Ovule",
     "group": "Female part · inside the ovary", "answer": "ovule",
     "options": ["ovule", "ovary", "pollen", "route"],
     "why": "The female half of the pairing, and the one students most often "
            "confuse with the ovary that contains it. One ovule becomes one "
            "seed, so counting the seeds in a fruit tells you how many ovules "
            "were fertilised."},

    {"id": "petal", "label": "Petal", "name": "Petal",
     "group": "Neither · attraction", "answer": "attract",
     "options": ["attract", "protect", "pay", "catch"],
     "why": "An advertisement, not a reproductive organ — which is why "
            "the plants that need no advertising have no petals worth the "
            "name. Colour, pattern and scent are all aimed at a specific kind "
            "of visitor, and some patterns are only visible in ultraviolet "
            "light, which bees can see and we cannot."},

    {"id": "sepal", "label": "Sepal", "name": "Sepal",
     "group": "Neither · protection", "answer": "protect",
     "options": ["protect", "attract", "hold", "pay"],
     "why": "The small green flaps under the petals. Before the flower opened "
            "they were the outside of the bud, and everything delicate was "
            "folded up inside them."},

    {"id": "nectary", "label": "Nectary", "name": "Nectary",
     "group": "Neither · payment", "answer": "pay",
     "options": ["pay", "attract", "ovule", "pollen"],
     "why": "Nectar is a real cost: the plant makes sugar by photosynthesis "
            "and then gives some of it away. It is worth it, because a paid "
            "courier that visits flower after flower of the same species "
            "delivers pollen far more reliably than the wind ever could."},
]

# ── the five design rows (page lines 367–373) ───────────────────────────
#
# Read DOWN a column, which is what `r_comparison` draws: `feature` is the row
# name, and the two cells are the two strategies. Neither column is the quiet
# one — both designs work, which is the section's closing claim — so
# `row_tones` is ink on ink.
DESIGNS = [
    ("Petals",
     "Large, coloured and often scented, with a platform to land on.",
     "Small, green or absent altogether. There is nobody to impress."),
    ("Nectar",
     "Produced in nectaries — the payment for the visit.",
     "None. Wind cannot be paid."),
    ("Pollen",
     "Sticky or spiky so it clings to an insect. Made in modest amounts, "
     "because delivery is targeted.",
     "Smooth, light and dry so it drifts. Made in enormous amounts, because "
     "almost all of it is wasted."),
    ("Anthers",
     "Held inside the flower, positioned so a visiting insect must brush "
     "against them.",
     "Dangling outside on long thin filaments, where the slightest wind "
     "shakes the pollen loose."),
    ("Stigma",
     "Small and sticky, inside the flower where the insect will touch it.",
     "Large and feathery, hanging outside like a net to catch pollen from "
     "the air."),
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 127 character for character.
    "slug":        "flowers-and-pollination",
    "title":       "Flowers and pollination",
    "discipline":  "biology",
    "unit":        "reproduction",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `a` clause of the split bullet — flower structure, and wind and
    # insect pollination. See the docstring; `b` and `c` belong to the two
    # lessons after this one.
    "covers":      ["KS3.B.REP.02a"],
    # Named but not taught. The key fact, the style's `why` and the ovary's
    # `why` all point forward at fertilisation and fruit (REP.02b owns it), and
    # the nectary's `why` plus the endmatter link reach the pollination-and-
    # food-security argument that B9 owns.
    "touches":     ["KS3.B.REP.02b", "KS3.B.ECO.02"],
    "beyond_statutory": False,
    "threads":     [{"id": "structure-function", "level": 2},
                    {"id": "cells-and-systems", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires`: Design draws no "Before this lesson" card, and the engine
    # omits an empty one. All three of her forward and sideways links live in
    # the middle card — see "What could not be lifted" 4.
    "requires":    [],
    "assumes":     [],
    "references":  ["fertilisation-seeds-and-fruit",
                    "gametes-and-fertilisation",
                    {"unit": "B9", "lesson": "pollinators-and-food-security"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Plant reproduction in full, self- and cross-pollination, "
                   "and pollination as an ecosystem service under threat.",

    # ── framing ─────────────────────────────────────────────────────────────
    # ⚠️ Teleology check, docstring bullet 1: "a delivery problem" is a
    # situation — two gametes, two places, no movement — not a want.
    "big_question": "A flower is not a decoration. It is a reproductive organ "
                    "with a delivery problem: the gametes are in two places "
                    "and the plant cannot move.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # THREE stops. Design draws four; `s-designs` is dropped — see the
    # docstring. `short` and `label` are Design's own `RAIL_SHORT` and `RAIL`
    # strings (page lines 317–323).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Grass flowers",
         "done_when": "committed"},
        # Design's own threshold, kept verbatim: the stop ticks when all NINE
        # parts have been checked, not when the first one has. A stop that
        # ticked on the first check would call the instrument finished at a
        # ninth of it.
        {"anchor": "s-parts", "short": "PARTS", "label": "Match the job",
         "done_when": "all_nine_parts_checked"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    #
    # ⚠️ Teleology check, docstring bullet 2: the reveal's "throws its pollen
    # into the air and hopes" is lifted whole. The same sentence reduces it to
    # quantity two clauses later, which is the non-teleological reading the
    # rest of the page runs on.
    "phenomenon": {
        "kind": "narrative",
        "title": "Grass has flowers. You have walked past millions of them "
                 "without noticing.",
        "prompt": "So have oak, birch, hazel, wheat and rice. None of them "
                  "has petals worth looking at, and every one of them flowers "
                  "— which tells you something about what petals are "
                  "actually for.",
        "commit": "Why is it grass pollen that causes hay fever, and not rose "
                  "pollen?",
        "options": [
            "Grass pollen irritates the nose more strongly",
            "Grass is wind-pollinated, so it releases huge amounts into the "
            "air",
            "There is simply far more grass than there are roses",
            "Rose pollen stays trapped inside the petals",
        ],
        "reveal": "Because grass throws its pollen into the air and hopes. "
                  "Wind carries nothing reliably, so a wind-pollinated plant "
                  "compensates with quantity: light, smooth, dry grains "
                  "released in enormous numbers, most of which land nowhere "
                  "useful and some of which land in your nose. A rose hands "
                  "its pollen to a bee. It makes a fraction as much, the "
                  "grains are sticky rather than airborne, and almost none of "
                  "it is ever loose in the air to breathe in. Hay fever is a "
                  "side effect of one pollination strategy.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ The `REPRO` family is NOT yet in `docs/ks3/misconception-register.md`
    # — the commander maintains it centrally, and B5's entries are minted as
    # the eight lessons are written. These three are the ids allocated to this
    # lesson; the disagreement with NOTES-B5 §5's own numbering is in the
    # docstring and is reported, not resolved here.
    #
    # `elicited_by` is honest per entry. REPRO-12 really is surfaced by the
    # hook — a student who does not know wind pollination exists cannot answer
    # the hay-fever question — and REPRO-22 really is surfaced by the
    # instrument, whose `ovule` and `ovary` option sets each carry the other as
    # a distractor. REPRO-11 is not asked for anywhere before the block that
    # kills it, so the block is named for both ends. b4-01's `three-wrong-
    # ideas` is the same pattern.
    "misconceptions": [
        {"id": "REPRO-11",
         "statement": "Flowers are the pretty part of the plant.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
        {"id": "REPRO-12",
         "statement": "All flowers are pollinated by insects.",
         "elicited_by": "s-hook",
         "confronted_by": "two-wrong-ideas"},
        # ⊕ The third belief, minted at the id the commander allocated for it.
        # It is a structural confusion rather than a claim a student would say
        # out loud, and the instrument is where it lives: it is elicited by two
        # option sets and answered in the ovule's `why`.
        {"id": "REPRO-22",
         "statement": "The ovule and the ovary are the same thing.",
         "elicited_by": "nine-parts",
         "confronted_by": "nine-parts"},
    ],

    # Design draws no keyword block anywhere in B5, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list.
    #
    # ⚠️ Every definition below is authored, not lifted, and every one was
    # written against NOTES-B5 flag 44: a part is defined by what it is and
    # what happens in it, never by what it is "for". Where Design's own job
    # string is already a clean structural definition — `ovary`, `ovule` — it
    # is used unchanged rather than paraphrased.
    "vocabulary": [
        {"term": "pollination",
         "definition": "The transfer of pollen from an anther to a stigma.",
         "note": "Nothing has fused yet. That is fertilisation, and it comes "
                 "afterwards."},
        {"term": "stamen",
         "definition": "The male part of a flower: the anther and the "
                       "filament.",
         "note": None},
        {"term": "carpel",
         "definition": "The female part of a flower: the stigma, style, ovary "
                       "and ovules.",
         "note": None},
        {"term": "anther",
         "definition": "The part of the stamen in which pollen grains are "
                       "made.",
         "note": "It splits open when the pollen is ready."},
        {"term": "filament",
         "definition": "The stalk that holds the anther up and out from the "
                       "flower.",
         "note": None},
        {"term": "stigma",
         "definition": "The surface at the top of the carpel on which pollen "
                       "grains land.",
         "note": "Sticky and small on an insect-pollinated flower; large and "
                 "feathery on a wind-pollinated one."},
        {"term": "style",
         "definition": "The stalk between the stigma and the ovary.",
         "note": "A pollen tube grows down through it after a grain lands."},
        {"term": "ovary",
         "definition": "Contains the ovules, and becomes the fruit after "
                       "fertilisation.",
         "note": None},
        {"term": "ovule",
         "definition": "Contains a female gamete nucleus, and becomes the "
                       "seed after fertilisation.",
         "note": "One ovule becomes one seed."},
        {"term": "nectary",
         "definition": "The part of a flower in which nectar, a sugary "
                       "liquid, is produced.",
         "note": None},
        {"term": "sepal",
         "definition": "One of the small green flaps that enclosed the flower "
                       "while it was still a bud.",
         "note": None},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # Design's legal line names BOTH of these slots and no artwork exists for
    # either, so they are DECLARED at `needed` rather than dropped: the
    # manifest is generated from this field, which turns two dangling
    # references into two tracked sourcing tasks. `needed` is not a build
    # blocker. No `figure` block is added to `core` — Design draws no figure
    # slot on the page, and one here would be a component nobody drew.
    #
    # The captions describe only what this lesson teaches. NOTES-B5 flag 13
    # asks for a ruling on what is illustrated and at what depth before
    # anything is commissioned, and nothing here pre-empts it: the first
    # caption is the nine parts and their three groups, the second is the five
    # comparison rows. Neither invents a structure the page does not name.
    "figures": [
        {"id": "b5-flower-parts-labelled",
         "kind": "diagram",
         "caption": "A generalised flower cut in half and labelled: sepal and "
                    "petal on the outside, the anther and filament together "
                    "as the stamen, the stigma, style, ovary and ovules "
                    "together as the carpel, and the nectary at the base.",
         "status": "needed"},
        {"id": "b5-wind-vs-insect",
         "kind": "diagram",
         "caption": "An insect-pollinated flower and a wind-pollinated flower "
                    "side by side, showing petals, nectary, the position of "
                    "the anthers, the texture of the stigma and the grains of "
                    "pollen for each.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-parts — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b5/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so the segment is measured and not inherited.
        #
        # ⚠️ EVERY B5 INSTRUMENT IS ON INK. `.ks3-dark p` is (0,1,1) and beats
        # a bare instrument class at (0,1,0) — the defect that shipped a B4
        # chain label at 1.21:1. That is the renderer's problem rather than
        # this module's, and it is recorded here because this payload is what
        # feeds it.
        {"type": "flower-jobs", "id": "nine-parts", "anchor": "s-parts",
         "demand": "investigate",
         "eyebrow": "Match the job · nine parts",
         "heading": "What is each part actually for?",
         "head_counter": {"format": "{n} of 9 checked", "total": 9},
         "prompt": "Pick a part, then choose its job. Every wrong option here "
                   "is the right answer for a different part, so a guess "
                   "still teaches you something.",
         "options_lead": "Which job belongs to it?",

         "jobs": JOBS,
         "parts": PARTS,

         "reveal_label": "Check it",
         "hints": {"idle": "Choose a job first.",
                   "ready": "Ready.",
                   "opened": "Now try another part."},
         "verdict": {"right": "Correct",
                     "wrong": "Not this one — that job belongs to "
                              "another part"}},

        # #s-designs — the band-panel comparison. NOT on the rail; see the
        # docstring. Design's lede is the one thing lost — "What could not be
        # lifted" 1.
        {"type": "comparison", "anchor": "s-designs",
         "eyebrow": "Two solutions to one problem",
         "eyebrow_tone": "accent-text",
         "statement": "Hire a courier, or throw it into the wind.",
         "ground": "band",
         "columns": [
             {"caption": "Insect-pollinated", "tone": "on-dark"},
             {"caption": "Wind-pollinated", "tone": "on-dark"},
         ],
         # Design paints both cells at the same weight — neither strategy is
         # the quiet one, which is the section's own closing claim: "Both
         # designs work."
         "row_tones": ["ink", "ink"],
         "rows": [{"name": feature, "cells": [insect, wind]}
                  for feature, insect, wind in DESIGNS],
         # Design nests the key fact inside this panel, and `r_comparison` has
         # the slot for it. `card`, because the panel itself is `band` and band
         # on band is invisible.
         "key_fact": {"ref": "pollination-is-transfer", "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "REPRO-11"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside the comparison, on the card ground — Design's own
    # arrangement (page lines 176–179), and the same one b3-01 and b1-06 use.
    "key_facts": [
        {"id": "pollination-is-transfer",
         "text": "Pollination is the transfer of pollen from an anther to a "
                 "stigma. That is the whole definition. Nothing has yet "
                 "fused, no gamete has met another, and the next lesson is "
                 "about what happens after the pollen lands.",
         "placement": "top-level",
         "ground": "card",
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
        # page's is static markup, like B1's and B4's, so it stays a
        # confrontation. Same rule, different block.)
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "REPRO-11",
         "statements": [
             {"quote": "Flowers are the pretty part of the plant.",
              "body": ["Flowers are reproductive organs, and every feature "
                       "you find attractive about them is an advertisement "
                       "aimed at something else. The colour is a signal to an "
                       "animal with good colour vision. The scent is a signal "
                       "to one that hunts by smell, often at night. The "
                       "nectar is payment — a sugar solution the plant "
                       "manufactures at real cost, purely to make the visit "
                       "worth an insect’s time. Even the landing "
                       "platform of a petal is engineering: it holds the "
                       "insect in the position where the anthers will brush "
                       "its back. None of it is aimed at us. It is worth "
                       "noticing what follows from that, too — a plant "
                       "that has no need to advertise does not bother, which "
                       "is why grasses and most large trees have flowers so "
                       "plain that most people have never recognised one."]},
             {"quote": "All flowers are pollinated by insects.",
              "body": ["Most of the plant material around you is "
                       "wind-pollinated. Every grass, which includes wheat, "
                       "rice, maize, barley and oats — so a large share "
                       "of what the world eats — plus oak, beech, birch, "
                       "hazel and most of the other big trees. These plants "
                       "make flowers with no petals, no scent and no nectar, "
                       "because there is nobody to attract. What they have "
                       "instead is anthers dangling outside the flower on "
                       "long thin filaments where the wind can shake them, "
                       "feathery stigmas held out like nets to catch what "
                       "drifts past, and pollen produced in quantities that "
                       "make the second half of a June afternoon unbearable "
                       "for anyone with hay fever. Both designs work. They "
                       "simply pay for delivery in different currencies: one "
                       "in sugar, the other in sheer number of grains."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED. Rung 1 is clean; rung 2 is a tell at
    # 14w against 10w and is NOT rewritten. Full reasoning in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Define it precisely",
            "q": "Which of these is pollination?",
            "options": [
                "A pollen nucleus fusing with an ovule nucleus",
                "The transfer of pollen from an anther to a stigma",
                "An insect drinking nectar from a flower",
                "An ovary swelling to become a fruit",
            ],
            "answer": 1,
            "feedback": {
                0: "That is fertilisation, and it happens later, inside the "
                   "ovary. Pollination gets the pollen to the right place; it "
                   "does not join anything.",
                2: "That is the insect’s reason for being there. "
                   "Pollination is what happens to the plant as a side "
                   "effect.",
                3: "That happens after fertilisation, which is itself after "
                   "pollination. Three events, three names.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A flower has no petals, no scent and no nectar, with "
                 "anthers hanging outside on long filaments. What can you "
                 "conclude?",
            "options": [
                "It is a dead or damaged flower",
                "It is wind-pollinated — it has nothing to attract with "
                "because it attracts nothing",
                "It reproduces without pollination",
                "It is pollinated at night, so colour would be wasted",
            ],
            "answer": 1,
            "feedback": {
                0: "It is a perfectly healthy flower. Every grass in the "
                   "country looks like this.",
                2: "It is pollinated like any other flowering plant. Only the "
                   "delivery method differs.",
                3: "Night-pollinated flowers do exist — and they are "
                   "usually pale and strongly scented, because scent works in "
                   "the dark. This flower has given up on attraction "
                   "altogether.",
            }},
        "explain": {
            "title": "Rung 3 · Name the parts and their jobs",
            "q": "Name the male and female parts of a flower and give the job "
                 "of each. Then explain what pollination is, in one sentence, "
                 "and say why the petals are not part of either group.",
            "field_label": "Your answer",
            "placeholder": "The male parts are…",
            "success": [
                "Names the male parts — anther (makes pollen) and "
                "filament (holds it in position).",
                "Names the female parts — stigma, style, ovary and "
                "ovules, with a job for each.",
                "Defines pollination as the transfer of pollen from an anther "
                "to a stigma.",
                "Says the petals attract pollinators rather than making or "
                "receiving gametes.",
                "Makes clear that pollen and ovules carry the gametes, and "
                "that nothing has fused yet.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "You are given two unlabelled flowers, one wind-pollinated "
                 "and one insect-pollinated, and no other information. "
                 "Describe three observations you would make to tell them "
                 "apart, and explain what each observation tells you about "
                 "how the pollen travels.",
            "field_label": "Your answer",
            "placeholder": "First I would look at…",
            "success": [
                "Gives three usable observations — for example petals, "
                "anther position, stigma texture, presence of nectar.",
                "Explains each in terms of delivery: attraction and payment "
                "for an animal, exposure and catching area for wind.",
                "Mentions the pollen itself — sticky and scarce, or "
                "smooth, light and abundant.",
                "Says that both are pollination, and that the difference is "
                "only in how the pollen is carried.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "The male parts of a flower are the stamens: anther and "
                "filament. The female parts are the carpel: stigma, style, "
                "ovary and ovules. Pollen made in the anthers contains the "
                "male gamete nucleus; the ovules contain the female gamete "
                "nucleus. Pollination is the transfer of pollen from an "
                "anther to a stigma, by insect or by wind. Insect-pollinated "
                "flowers advertise and pay: coloured petals, scent, nectar, "
                "sticky pollen. Wind-pollinated flowers do neither: small "
                "dull flowers, exposed anthers, feathery stigmas, and vast "
                "amounts of light smooth pollen.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES-B5 flag 33: the dates and the rounding are Design's and are on
    # Mide's list. The paragraph's real subject is not the orchid — it is what
    # makes a claim strong, which is why `ws` carries scientific-attitudes.
    "stretch": [
        {"type": "explainer", "id": "the-moth-that-had-to-exist",
         "text": "In 1862 Darwin was sent an orchid from Madagascar with a "
                 "nectar spur nearly thirty centimetres long and the nectar "
                 "at the very bottom of it. Any insect wanting that reward "
                 "would have to reach the whole way down, and in doing so "
                 "would be forced against the flower’s pollen. He "
                 "published the obvious conclusion: there must be a moth in "
                 "Madagascar with a tongue about thirty centimetres long, "
                 "otherwise this flower could not be pollinated and would not "
                 "exist. It was treated as an absurdity — one reviewer "
                 "thought it showed how far the theory could be pushed. "
                 "Forty-one years later, in 1903, a hawkmoth with a proboscis "
                 "of the required length was collected in Madagascar and "
                 "given the subspecies name <em>praedicta</em>, the predicted "
                 "one. It was another ninety years before anyone actually "
                 "filmed one feeding at the flower and confirmed the "
                 "mechanism in full. That is the shape of a strong scientific "
                 "claim: it is not merely consistent with what has been seen, "
                 "it says in advance what must be found, and it can be shown "
                 "wrong by anyone who looks and does not find it."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own flagship, which is a real
    # destination on the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check which parts are male and which are "
                      "female?",
              "cta": "Ask about this lesson",
              "anchor": "s-parts"},

    # ⊕ MRB-228's `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph here and nothing in it is a safety instruction —
    # it is a note about how far the generalised flower can be trusted, and a
    # declaration about two figures that have not been drawn yet. Routing it
    # through `safety_note` would print it in the treatment reserved for
    # "never light a candle without an adult", which devalues the safety line.
    # b3-05, b3-07 and b4-01 resolve the identical foot line the identical way.
    #
    # ⚠️ Both figure ids keep their plain text; Design sets them in mono inside
    # the sentence and a foot line is escaped, so they render in body copy and
    # the words are unchanged.
    "convention_note": "The flower described is a generalised one: many real "
                       "flowers lack petals, sepals or nectaries, some carry "
                       "only male or only female parts, and a few carry them "
                       "on separate plants entirely. The labelled flower "
                       "diagram is declared in the lesson record as "
                       "b5-flower-parts-labelled and the wind-and-insect "
                       "comparison as b5-wind-vs-insect, both awaiting "
                       "illustration.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The instrument is classification against evidence, and rung 4 asks for
    # three observations and what each one licenses. The stretch layer is about
    # what makes a claim testable, which is the attitudes strand.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
