"""B3 L1 — A balanced diet (CLASSIFY).

Authored against Design's approved page,
`docs/ks3/design-reference/b3/b3-01-a-balanced-diet.dc.html` (594 lines), under the MRB-220
build contract. Shape follows `ks3_data/c1/lesson_02_solids_liquids_and_gases.py`.

Every student-facing string is lifted from the approved page. The four
exceptions are listed under "What could not be lifted" below, and none of them
is a sentence of science.

── The flagship, and why it is one instrument rather than seven ─────────

`#s-plate` is `band-commit`, on `ks3-block ks3-dark ks3-practical` — Design's
own markup (page line 113), which is where the `practical` shell comes from and
not an inference. Seven nutrients, three amount bands, and a reveal that stays
locked until every one of the seven has been placed.

⚖️ THE LOCK IS THE PEDAGOGY, and it is the whole difference between this and
B2's `job-sort`. The sorter opens each row the instant that row is decided,
which is right there: a student finds out about item 1 before committing on
item 2, and the sequence teaches. Here the argument is the SPREAD — two
nutrients in hundreds of grams, three in tens, two in milligrams — and nobody
is surprised by a spread they were shown a seventh at a time. The block's own
lede says so: *a guess you did not make cannot be wrong, and a guess that is
never wrong teaches you nothing.*

⚖️ THE VERDICT HAS THREE BRANCHES AND THE ALL-SAME ONE IS THE POINT. NOTES-B3
§3.1 names it as the branch that must not be dropped, and it is: a student who
puts all seven in one band is the student this lesson exists for, and this is
the only place in the page where "balanced means equal amounts" is read back to
them in their own answer rather than argued against in the abstract.
`r_band_commit` raises without all three.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-nutrients` came off the rail. Design draws FOUR stops and `#s-nutrients`
ticks on `s.plateOpen` (page line 420) — the PREVIOUS section's predicate,
verbatim — and since the section is an eyebrow, a display line, a seven-row
table and a key fact, emitting no control, no commit and no field, MRB-208's
"the rail carries only sections that require the student to do something"
looked to rule it out. So the lesson shipped THREE stops and called
`ks3_parity.check_rail_reachable` honest for it.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; no invented or
dropped page structure; page wins over engine. Declaring three stops where
Design drew four is not rendering what Design drew.

And Design's own `isDone()` states the tick condition rather than leaving it to
be inferred. It is a rail-level function, and it returns the identical
expression for `#s-plate` and then for `#s-nutrients`. The seven-row table is
the payoff of the plate beside it; it carries no control because the plate has
already taken the student's commitment. That is a MIRROR, and `wireRail`'s
`paint()` in `shared/ks3.js` resolves mirrors at rail level.

So the fourth stop is declared: anchor `s-nutrients`, `mirrors: "s-plate"`,
`done_when: "all_seven_committed_and_opened"` — the plate's own predicate,
named as borrowed rather than smuggled. `ks3_parity.check_rail_matches_design`
gates the built rail against `docs/ks3/rail-manifest.md`. c1-02's `#s-matrix`
and b3-07's `#s-four` are restored the same way. The section always kept its
anchor; it now also makes a claim to be completable, and it is reachable.

── What could not be lifted, and why ────────────────────────────────────

1. **The seven mono food sub-lines in `#s-nutrients`.** Design's name column is
   two lines: the nutrient in 18px/700 and its food sources in 13px mono muted
   ("bread, rice, potato"). `r_comparison` emits `.ks3-compare-name` as ONE
   span and the stylesheet is not this run's to change, so the sub-line has no
   home. All seven strings are DROPPED FROM THE TABLE and reported. They are
   not lost from the page: `#s-plate`'s seven `hint` values are Design's own
   longer form of the same list ("bread, rice, pasta, potato"), directly above.
   The fix, if the table is to win, is a `sub` key on a comparison row.

2. **The `Nutrient` column heading.** `r_comparison`'s header row emits an
   empty name cell by construction; the two content captions are authored and
   render.

3. **Design's endmatter is TWO cards and the engine emits ONE.** She draws
   "Next in this unit" (Food tests) and "Connects to" (When diet goes wrong,
   Energy stores). `r_endmatter` has one middle card, so all three edges sit in
   it under Design's own second heading. Nothing is lost but the split.

4. **`ks4_links` gives way to `ks4_becomes`.** Design's third card is authored
   prose and §4.8.1 D makes the two mutually exclusive. The KS4 bridge edge is
   what is given up; c1-06, b3-07 and all six C2 lessons resolve it the same
   way.

⚑ For Mide's science gate — ONE REAL CONTRADICTION, LIFTED UNCHANGED:

  * **The key fact and the bench disagree about the counts.** The key fact
    (page line 189) says *"Three of the seven are measured in hundreds of
    grams. Three are measured in milligrams."* The bench's own bands put TWO in
    hundreds of grams (carbohydrate 300 g, water 2000 g), THREE in tens (lipid
    70 g, protein 45 g, fibre 25 g) and TWO in the trace band (vitamins 0.2 g,
    minerals 5 g) — and the bench's `close` verdict says exactly that, in the
    same section: *"two nutrients in hundreds of grams, three in tens, two in
    milligrams."* Three sentences on one page, two of which agree with the data
    and one of which does not. **Design's wording is lifted unchanged**, per
    the c1-02 precedent: the numbers are a content call and content is Mide's
    gate, not the build's. The cheapest repair is "Two of the seven are
    measured in hundreds of grams. Two are measured in milligrams." — but it is
    a repair to a sentence a qualified examiner should choose.
  * NOTES-B3 §4 flags 1–4 are open on this lesson: the seven daily figures, the
    B12 arithmetic behind "two hundred million times", "four months" to die on
    Plate A, and the Takaki Kanehiro framing. All four are authored as
    delivered.
"""

# ── the seven, at the bench (page lines 347–362) ────────────────────────
#
# `band` is the answer and `mass` is what the panel prints beside it. The
# `hint` is Design's food-source line, and it is now the ONLY place the food
# sources appear — see "What could not be lifted" 1.
PLATE = [
    {"name": "Carbohydrate", "hint": "bread, rice, pasta, potato",
     "band": "lots", "mass": "about 300 g",
     "why": "The bulk of the plate, and the body’s first choice of fuel. "
            "Almost every cell can respire glucose, and your brain can use "
            "very little else."},
    {"name": "Lipid (fat and oil)", "hint": "oils, butter, nuts, oily fish",
     "band": "some", "mass": "about 70 g",
     "why": "Tens of grams, not hundreds — but not zero. It carries more than "
            "twice the energy per gram of carbohydrate, builds every cell "
            "membrane, and is the only way vitamins A, D, E and K can be "
            "absorbed."},
    {"name": "Protein", "hint": "meat, fish, eggs, beans, lentils",
     "band": "some", "mass": "about 45 g",
     "why": "Tens of grams. Protein is the only nutrient that supplies the "
            "nitrogen needed to build and repair tissue, so a growing "
            "13-year-old needs a steady supply rather than a large one."},
    {"name": "Vitamins", "hint": "fruit, vegetables, dairy, liver",
     "band": "trace", "mass": "about 0.2 g in total",
     "why": "A fifth of a gram covers all thirteen of them together. They "
            "release no energy at all — they let the reactions that do release "
            "energy actually run."},
    {"name": "Minerals", "hint": "dairy, red meat, leafy greens, salt",
     "band": "trace", "mass": "about 5 g in total",
     "why": "A few grams, mostly calcium, and then iron, iodine and the rest "
            "in milligrams. Iron is 14 mg a day; miss it and your blood cannot "
            "carry oxygen properly."},
    {"name": "Dietary fibre", "hint": "wholegrains, skins, pulses, vegetables",
     "band": "some", "mass": "about 25 g",
     "why": "Tens of grams of something you never absorb. It is not digested "
            "and not respired — it gives the gut muscles something to push "
            "against, which is what keeps everything moving."},
    {"name": "Water", "hint": "drinks, and most of your food",
     "band": "lots", "mass": "about 2000 g",
     "why": "Two kilograms — by far the largest requirement on the list, and "
            "the one you die from fastest without. Every reaction in you "
            "happens in solution."},
]

# ── the table (page lines 364–372) ──────────────────────────────────────
#
# ⚠️ `food` is authored here and read by NOTHING, deliberately and reported:
# see "What could not be lifted" 1. It is kept beside the row it belongs to so
# that adding a `sub` key to `r_comparison` is a one-line change rather than a
# re-lift from the reference page.
NUTRIENTS = [
    {"name": "Carbohydrate", "food": "bread, rice, potato",
     "job": "Broken down to glucose and respired for energy. The store the "
            "body reaches for first.",
     "lack": "Tiredness, and the body starts breaking down its own fat and "
             "then its own protein for fuel."},
    {"name": "Lipid", "food": "oils, nuts, oily fish",
     "job": "Energy store, insulation, and the raw material of every cell "
            "membrane. Carries vitamins A, D, E and K.",
     "lack": "Those four vitamins cannot be absorbed. Skin and nerves are "
             "affected before anything else shows."},
    {"name": "Protein", "food": "eggs, fish, beans",
     "job": "Broken into amino acids and rebuilt into muscle, enzymes, "
            "antibodies and haemoglobin. Growth and repair.",
     "lack": "Growth stops, wounds heal slowly, and fluid collects in the "
             "tissues. Kwashiorkor in severe cases."},
    {"name": "Vitamins", "food": "fruit, vegetables, dairy",
     "job": "Small molecules that make specific reactions possible. Thirteen "
            "of them, each with its own job.",
     "lack": "A specific deficiency disease per vitamin — scurvy without C, "
             "rickets without D, beriberi without B1."},
    {"name": "Minerals", "food": "dairy, red meat, greens",
     "job": "Elements built into structures and carriers: calcium into bone, "
            "iron into haemoglobin, iodine into thyroid hormone.",
     "lack": "Anaemia without iron, weak bones without calcium, goitre "
             "without iodine."},
    {"name": "Dietary fibre", "food": "wholegrains, pulses",
     "job": "Not digested and not absorbed. Adds bulk so gut muscles have "
            "something to grip and push.",
     "lack": "Constipation, and a raised long-term risk of bowel disease."},
    {"name": "Water", "food": "drinks and food",
     "job": "The solvent every reaction in the body happens in, and the "
            "transport medium for blood, urine and digestion.",
     "lack": "Concentration and temperature control fail within hours. Death "
             "in days — faster than for any other nutrient."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 78 character for character.
    "slug":        "a-balanced-diet",
    "title":       "A balanced diet",
    "discipline":  "biology",
    "unit":        "nutrition-and-digestion",
    "family":      "CLASSIFY",

    # ── curriculum position ─────────────────────────────────────────────────
    # The whole of `KS3.B.NUT.01`, which is a single uncompounded bullet: the
    # seven nutrients, each with its function and its deficiency. The table and
    # the bench between them deliver all three halves of it.
    "covers":      ["KS3.B.NUT.01"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 1},
                    {"id": "substances-and-reactions", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 45,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires`: Design draws no "Before this lesson" card, and the engine
    # omits an empty one. All three of her forward and sideways links live in
    # the middle card — see "What could not be lifted" 3.
    "requires":    [],
    "assumes":     [],
    "references":  ["food-tests",
                    "when-diet-goes-wrong",
                    {"unit": "P1", "lesson": "energy-stores",
                     "label": "Energy stores",
                     "why": "Where the chemical store in food is developed as "
                            "energy rather than as nutrition."}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    # Renders only because `ks4_links` is empty — Design's card 3 is prose.
    "ks4_becomes": "Nutrient requirements, malnutrition, and the biochemistry "
                   "of carbohydrates, lipids and proteins as polymers.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Seven things your diet has to contain. You need about "
                    "300 g of one of them a day and 0.000001 g of another. "
                    "Both are essential. What does “balanced” actually mean?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-nutrients` is the third: it holds
    # no control of its own and mirrors `s-plate`, ticking on the plate's
    # predicate — see the docstring. `short` and `label` are Design's own
    # `RAIL_SHORT` and `RAIL` strings (page lines 333–339).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "One orange",
         "done_when": "committed"},
        # A SET of seven, then the reveal. `wireBandCommit` ticks only when the
        # gate has been discharged and opened, so the stop cannot tick on a
        # partial plate and cannot tick on load.
        {"anchor": "s-plate",  "short": "BENCH",  "label": "Build a day",
         "done_when": "all_seven_committed_and_opened"},
        {"anchor": "s-nutrients", "short": "SEVEN", "label": "The seven",
         "mirrors": "s-plate", "done_when": "all_seven_committed_and_opened"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "Two plates. One of them will kill you in about four months.",
        "prompt": "Plate A is white rice, chicken, oil, water and salt — every "
                  "day, nothing else. It has carbohydrate, protein, lipid, "
                  "minerals and water in roughly the right amounts. Plate B is "
                  "the same food plus one orange. The person eating Plate A "
                  "dies. The person eating Plate B is fine.",
        "commit": "One orange. What is it doing?",
        "options": [
            "Supplying energy the rest of the plate is missing",
            "Supplying about 50 mg of one substance the body cannot make",
            "Making the meal easier to digest",
            "Adding water, which the rest of the plate lacks",
        ],
        "reveal": "The orange supplies about 50 milligrams of vitamin C — one "
                  "twenty-thousandth of the mass of the meal. It carries no "
                  "useful energy at all. Without it, the protein holding your "
                  "body together cannot be made properly, and you bleed to "
                  "death from the inside. Balance is not about amounts being "
                  "similar.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ THE `DIET` FAMILY IS NOT IN `docs/ks3/misconception-register.md`.
    # NOTES-B3 §5 says fifteen entries were "minted, not proposed"; the
    # register has no `DIET` row at all. The ids below are this lesson's share
    # of a range the unit has to register in ONE pass, and this module
    # deliberately does not write them — the register is shared with the other
    # seven lessons, authored in parallel, and b3-07 made the same call and the
    # same note. Allocation is by lesson order and by the two constraints NOTES
    # §5 pins: `DIET-06` is the energy one and belongs to b3-03 (it is the row
    # that must stay separate from `ENERGY-12`), `DIET-08` is b3-04's, and
    # `DIET-11`–`DIET-14` are b3-06's and b3-07's. That leaves 01–03 here.
    #
    # Nothing fails meanwhile: `_misconception_quote` resolves from THIS list,
    # and the block carries its own `statements`, which win over the register
    # (build_ks3.py:2504).
    "misconceptions": [
        {"id": "DIET-01",
         "statement": "A balanced diet means equal amounts of each food group.",
         # The bench elicits it — a student who puts all seven in one band has
         # just stated the belief in their own answer — and the same bench's
         # all-same verdict is the first thing that confronts it. `#s-think`
         # then confronts it in words.
         "elicited_by": "seven-bands",
         "confronted_by": "think-balanced"},
        {"id": "DIET-02",
         "statement": "Vitamins give you energy.",
         "elicited_by": "think-balanced",
         "confronted_by": "think-balanced"},
        {"id": "DIET-03",
         "statement": "Fat is bad for you, so a healthy diet has none in it.",
         "elicited_by": "think-balanced",
         "confronted_by": "think-balanced"},
    ],

    # Design draws no keyword block anywhere in B3, so these definitions never
    # reach the lesson body. The TERMS do reach a student, as the unit page's
    # "Words this unit gives you" chips, and the reading-age gate reads them as
    # its exclusion list — which matters on this page, because "carbohydrate",
    # "deficiency" and "kwashiorkor" would otherwise all count against it.
    "vocabulary": [
        {"term": "nutrient",
         "definition": "A substance in food that the body needs in order to "
                       "work, grow or repair itself.",
         "note": "There are seven, and none of them is optional."},
        {"term": "carbohydrate",
         "definition": "The nutrient the body breaks down to glucose and "
                       "respires first for energy.",
         "note": None},
        {"term": "lipid",
         "definition": "Fats and oils: an energy store, an insulator, and the "
                       "material every cell membrane is built from.",
         "note": "‘Lipid’ is the scientific word for fats and oils together."},
        {"term": "protein",
         "definition": "The nutrient broken into amino acids and rebuilt into "
                       "muscle, enzymes and antibodies. Growth and repair.",
         "note": None},
        {"term": "vitamin",
         "definition": "A small molecule needed in tiny amounts that makes "
                       "particular reactions in the body possible.",
         "note": "A vitamin carries no energy of its own."},
        {"term": "mineral",
         "definition": "An element the body builds into a structure or a "
                       "carrier — calcium into bone, iron into haemoglobin.",
         "note": None},
        {"term": "dietary fibre",
         "definition": "Plant material the body cannot digest, which gives the "
                       "gut muscles something to push against.",
         "note": None},
        {"term": "deficiency",
         "definition": "Going short of one particular nutrient, and the "
                       "specific illness that follows from it.",
         "note": None},
    ],

    # Nothing on this page references a figure, and NOTES-B3 §4 flag 24's two
    # named slots (`b3-gut-labelled`, `b3-villus-labelled`) belong to b3-05 and
    # b3-07. Present and empty, never absent.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-plate — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b3/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 113), so the shell is measured and not inherited.
        {"type": "band-commit", "id": "seven-bands", "anchor": "s-plate",
         "demand": "investigate",
         "eyebrow": "At the bench · build a day",
         "heading": "Set the amounts yourself, then see the real ones",
         # Opens at ZERO. Design's own `plateProgress` also opens at zero
         # (`setCount` of an empty map), so nothing is corrected here.
         "head_counter": {"format": "{n} of 7 set", "total": 7, "start": 0},
         "prompt": "For each of the seven, choose how much a 13-year-old "
                   "needs in one day. Commit to all seven before you open "
                   "the answers.",

         # ⚠️ `miss_label` is AUTHORED rather than composed. Design writes
         # `'Actually ' + band.label.toLowerCase()`, which lower-cases an
         # authored phrase in the browser; the day a band is called "Milligrams
         # of Iron" that becomes wrong, and it puts a string transformation
         # between a student and a sentence either way.
         "bands": [
             {"id": "lots",  "label": "Hundreds of grams",
              "miss_label": "Actually hundreds of grams"},
             {"id": "some",  "label": "Tens of grams",
              "miss_label": "Actually tens of grams"},
             {"id": "trace", "label": "Milligrams or less",
              "miss_label": "Actually milligrams or less"},
         ],
         "hit_label": "You had it",
         "rows": PLATE,

         "open_label": "Show the real amounts",
         "commit_format": "{n} of {total} committed",
         "commit_done": "Opened",
         "verdict_eyebrow": "Your day, scored",
         "verdict_format": "{n} of {total} in the right band.",
         # ⚖️ THREE BRANCHES, AND `all_same` IS TESTED FIRST. See the docstring:
         # an all-same day happens to score 3, which would otherwise fall
         # through to `spread` and never hear the one thing this block exists
         # to say.
         "verdicts": {
             "all_same": "You put all seven in the same band — which is "
                         "exactly the wrong idea this lesson exists to kill. "
                         "Read the amounts again: 2000 g of water and 0.2 g of "
                         "vitamins are both correct, and they are ten thousand "
                         "times apart.",
             "close": "Notice what the spread looks like: two nutrients in "
                      "hundreds of grams, three in tens, two in milligrams. "
                      "Balanced describes seven separate targets, not seven "
                      "similar piles.",
             "spread": "The usual misses are lipid and fibre. Lipid feels like "
                       "it should be near zero and is not; fibre feels like a "
                       "trace and is 25 g — more than half a day’s protein, of "
                       "something you never absorb at all.",
         }},

        # #s-nutrients — the seven-row table. Rail stop 3, mirroring
        # `s-plate`; see the docstring. `r_comparison` is the component: band ground, 3px ink
        # border, dark header row, zebra rows, a nested key fact — which is
        # Design's markup (page lines 159–190) element for element, minus the
        # name column's second line.
        {"type": "comparison", "anchor": "s-nutrients",
         "eyebrow": "The seven",
         "eyebrow_tone": "accent-text",
         "statement": "What each one is for, and what goes wrong without it.",
         "ground": "band",
         "columns": [
             {"caption": "What your body does with it", "tone": "on-dark"},
             {"caption": "Without enough", "tone": "alert"},
         ],
         # Design paints the job cell in `--ks3-ink` and the deficiency cell in
         # `--ks3-ink-body` — the consequence reads one step quieter than the
         # function, which is a real distinction and is kept.
         "row_tones": ["ink", "ink-body"],
         "rows": [{"name": n["name"], "cells": [n["job"], n["lack"]]}
                  for n in NUTRIENTS],
         # ⚑ Lifted unchanged and flagged for the science gate: the counts in
         # this sentence disagree with the bench's own bands and with the
         # bench's `close` verdict. See the docstring.
         "key_fact": {"ref": "balanced-means-targets", "ground": "card"}},

        {"type": "misconception", "id": "think-balanced",
         "anchor": "s-think", "targets": "DIET-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside the comparison, on the card ground — Design's own
    # arrangement, and the same one c1-02 uses when a key fact sits inside a
    # band panel.
    "key_facts": [
        {"id": "balanced-means-targets",
         "text": "Balanced means each nutrient in the amount that nutrient "
                 "needs — not the same amount of each. Three of the seven are "
                 "measured in hundreds of grams. Three are measured in "
                 "milligrams. None of them is optional.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `seven-bands` is authored inline in `core` and lifted here by
    # `ks3_data/b3/__init__.py::_normalise`.
    "activities": [
        # Design draws THREE wrong ideas in one "Think again" block, separated
        # by amber-topped dividers — `r_confrontation` renders exactly that
        # from `statements[]`, and an authored statement wins over the register
        # (build_ks3.py:2504), which is what keeps Design's wording rather than
        # the register's.
        #
        # ⚠️ This block asks for NO commitment, on Design's page and here. It
        # is therefore not a rail stop and emits no `data-stage-done` — the
        # `confrontation` shell's dispatch entry deliberately omits it, because
        # a section that asks for nothing can never discharge a contract.
        {"id": "think-balanced",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "DIET-01",
         "statements": [
             {"quote": "A balanced diet means equal amounts of each food "
                       "group.",
              "body": ["Look at the two ends of the table you have just "
                       "filled in. A 13-year-old needs roughly 300 g of "
                       "carbohydrate and about 0.0000015 g of vitamin B12 in "
                       "a day — a difference of two hundred million times. "
                       "Eating them in equal amounts would mean 300 g of "
                       "vitamin B12, which would be a lifetime supply for "
                       "four hundred thousand people and would poison you "
                       "long before you finished the plate. The word balanced "
                       "describes a set of seven different targets being met "
                       "at once, like seven dials each reading correctly. It "
                       "has never meant seven equal piles."]},
             {"quote": "Vitamins give you energy.",
              "body": ["They do not, and this is worth being exact about. "
                       "Only three of the seven nutrients release energy when "
                       "they are respired: carbohydrate, lipid and protein. A "
                       "vitamin tablet has an energy content of zero — you "
                       "could eat the whole bottle and be no better fuelled "
                       "than before. What vitamins do is let the reactions "
                       "that release energy actually happen: vitamin B1 is "
                       "part of the machinery that gets glucose into "
                       "respiration, so someone short of it is exhausted "
                       "despite eating plenty. Feeling tired because you lack "
                       "a vitamin is not the same as feeling tired because "
                       "you lack fuel, and the fix is different."]},
             {"quote": "Fat is bad for you, so a healthy diet has none in it.",
              "body": ["Lipids are a required nutrient, not a permitted vice. "
                       "Every cell membrane in you — and there are about "
                       "thirty trillion of them — is built from lipid, and "
                       "vitamins A, D, E and K only dissolve in fat, so a "
                       "diet with no lipid in it cannot deliver them however "
                       "much you eat. What is true is that lipid carries more "
                       "than twice the energy per gram of carbohydrate, so it "
                       "is easy to take in far more energy than you need "
                       "without noticing. That is a statement about quantity, "
                       "not about the nutrient being harmful."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # `title` carries Design's finished heading; `_rung_title` strips the
    # "Rung N · " prefix and the engine puts the number back.
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS PASS.
    #   rung 1: correct 4w against distractors of 4 / 4 / 5 — the correct
    #           option is not the longest at all, so it cannot be a tell.
    #   rung 2: correct 7w against distractors of 6 / 5 / 8 — likewise.
    # No distractor was rewritten, because there was nothing to repair; the
    # measurement is recorded so a later edit knows what it is changing.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Which three",
            "q": "Which nutrients release energy when the body respires them?",
            "options": [
                "Carbohydrate, lipid and protein",
                "Carbohydrate, lipid and vitamins",
                "Carbohydrate and lipid only",
                "All seven, in different amounts",
            ],
            "answer": 0,
            "feedback": {
                1: "Vitamins have an energy content of zero. They make "
                   "energy-releasing reactions possible without supplying any "
                   "energy themselves.",
                2: "Close — but protein can be respired too. The body prefers "
                   "to use it for growth and repair, and falls back on burning "
                   "it when the other two run short.",
                3: "Fibre and water are never respired at all, and neither are "
                   "vitamins or minerals. Only three of the seven carry "
                   "energy.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A student is tired all the time. They eat plenty of bread, "
                 "pasta and rice but almost no meat, fish or leafy vegetables. "
                 "A doctor finds their blood cannot carry oxygen properly. "
                 "What is missing?",
            "options": [
                "Carbohydrate — they need more fuel",
                "Iron — a mineral, needed in milligrams",
                "Water — they are dehydrated",
                "Vitamin C — they are getting no fruit",
            ],
            "answer": 1,
            "feedback": {
                0: "They are eating plenty of carbohydrate. Reaching for ‘more "
                   "fuel’ is the trap: the fuel is there and cannot be used "
                   "properly.",
                2: "Dehydration does cause tiredness, but it would not stop "
                   "the blood carrying oxygen in the way described. That "
                   "points at haemoglobin.",
                3: "Low vitamin C causes scurvy: bleeding gums and poor "
                   "healing. It does not stop blood carrying oxygen.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the two ends",
            "q": "A 13-year-old needs about 300 g of carbohydrate and about "
                 "14 mg of iron each day — twenty thousand times less iron. "
                 "Explain why both are described as essential, and why the "
                 "amounts are so different.",
            "field_label": "Your explanation",
            "placeholder": "Both are essential because… but the amounts differ "
                           "because…",
            "success": [
                "Says carbohydrate is used as fuel and is respired "
                "continuously, so it is used up and must be replaced in bulk.",
                "Says iron is built into a structure — haemoglobin — rather "
                "than burnt, so it is not consumed in the same way.",
                "States that essential means the body cannot make it and fails "
                "without it, which is true of both regardless of amount.",
                "Names a consequence of going short of iron specifically, not "
                "just ‘being unhealthy’.",
                "Explicitly rejects the idea that a bigger requirement means a "
                "more important nutrient.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A sports drink advertises itself as ‘packed with "
                 "energy-giving vitamins’. The bottle lists sugars 32 g and "
                 "eight vitamins. Say what is wrong with the claim, what is "
                 "actually supplying the energy, and why the vitamins might "
                 "still be worth having in it.",
            "field_label": "Your answer",
            "placeholder": "The claim is wrong because…",
            "success": [
                "Says vitamins supply no energy, so ‘energy-giving vitamins’ "
                "is false as written.",
                "Identifies the 32 g of sugar as the actual source of the "
                "energy.",
                "Explains that some vitamins are part of the machinery that "
                "releases energy from glucose, which is probably what the "
                "claim is distorting.",
                "Says the vitamins are not useless — gives one honest reason "
                "they might belong in the drink.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A healthy diet contains carbohydrate, lipid, protein, "
                "vitamins, minerals, dietary fibre and water. Carbohydrate, "
                "lipid and protein are the only three that release energy; "
                "protein also builds and repairs. The other four are needed in "
                "far smaller amounts and are needed just as absolutely — fibre "
                "and water are not even absorbed as fuel, and you cannot live "
                "without either.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # MRB-225: history of science lives HERE, and nothing above is retracted by
    # it. Takaki's trial does not withdraw the seven nutrients; it shows how
    # one of them was found.
    "stretch": [
        {"type": "explainer", "id": "takaki-and-the-barley-ships",
         "text": "In the 1880s the Japanese Navy was losing sailors to "
                 "beriberi — weakness, swelling, heart failure — while the "
                 "Army was not. Takaki Kanehiro noticed the two forces ate "
                 "differently and ran what amounted to a fleet-sized "
                 "experiment: one ship on the usual polished white rice, "
                 "another with barley and vegetables added. The barley ship "
                 "came home almost untouched. He had no idea why, because "
                 "vitamin B1 would not be identified for another forty years, "
                 "and he was ridiculed for suggesting food could be the cause "
                 "of a disease everyone assumed was an infection. The "
                 "interesting part is that he was right about the fix while "
                 "being wrong about the mechanism, which happens in science "
                 "far more often than the tidy version admits."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # Design heads the card "Ask Mr Badmus AI" and puts the question in the
    # paragraph under it; the CTA points back at the bench.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why a milligram can matter as much as a "
                      "gram?",
              "cta": "Ask about this lesson",
              "anchor": "s-plate"},

    # ⚠️ `convention_note`, NOT `safety_note`. This is a note about how the
    # numbers on the page were taken and who they belong to; routing it through
    # `safety_note` would print it in the treatment reserved for "never light a
    # candle without an adult", which devalues the safety line on every page
    # that has a real one. MRB-228 added this slot for exactly this case.
    "convention_note": "Figures are typical daily requirements for a "
                       "13-year-old and are for learning the principle, not "
                       "for planning anyone's meals. Individual needs differ; "
                       "dietary advice comes from a doctor or a registered "
                       "dietitian.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
