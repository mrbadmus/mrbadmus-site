"""B3 L3 — Energy in food and what you need (QUANTITATIVE).

Authored against Design's approved page,
`docs/ks3/design-reference/b3/b3-03-energy-in-food-and-what-you-need.dc.html` (602 lines),
under the MRB-220 build contract.

── `KS3.B.NUT.02` IS SPLIT, AND THIS LESSON OWNS B3'S HALF ──────────────

Ruled by Mide on 16 Aug 2026 (MRB-232), and recorded in three places that now
agree: `docs/ks3/statutory-register.md`, `ks3_data/structure.py` and
`ks3_data/b3/__init__.py`. The bullet is two lessons wearing one line:

    B3  what you need and why — requirements, imbalance, and what follows
        from getting it wrong.
    P2  comparing energy values from food labels in kJ — the arithmetic and
        the units.

`covers` is `KS3.B.NUT.02a`, the clause and not the parent, for the same reason
b3-07 claims `KS3.B.NUT.04c`: the split is real and the sub-ID is the honest
handle on it. The pair is registered in `ks3_data/substatements.py` — `a` to
B3, `b` to P2 — and this module deliberately did not write that entry: the two
clauses cross a UNIT boundary and had to be minted in one pass by whoever owns
the ruling, not from one end of it. This file only claims `a`. Nothing here
owns the parent, so `validate()` rule 5 stays satisfied.

**Every link to P2 is a `references` EDGE and never prose.** Both are authored
below with `unit: "P2"`, and the first carries Design's own `label` because
"Energy in food" alone, printed in a card on a page called *Energy in food and
what you need*, reads as a link to this lesson.

⚖️ MY READING OF WHETHER THE DELIVERED PAGE STAYS ON B3'S SIDE. It does, but
not by a wide margin, and the report says so with line numbers. The ledger
(page lines 105–166) is entirely requirement-and-intake and is squarely B3's.
`#s-maths` (168–192) is the one to watch: sum 1 totals portions, sum 2
subtracts intake from requirement, and sum 3 turns a label figure into a
percentage of a requirement. All three are *comparisons against a
requirement* — which is the clause this lesson owns — rather than *energy
calculations*: nothing derives a joule, converts a unit, or uses power and
time. The nearest thing to a crossing is sum 3's `1050 ÷ 9500 × 100 = 11%`,
because a percentage of a label figure is the shape of P2's work; it stays on
this side because the denominator is a PERSON's requirement and the note under
it is about whose requirement it is, which is B3's whole point and not P2's.
The forward-pointer panel then hands the joule itself to Physics explicitly.
Nothing is silently built and nothing is silently dropped.

── THREE SEQUENCE STRINGS REWRITTEN, and why ────────────────────────────

Year and half-term are DATA (`ks3_data/school_schemes.py`,
`default_sequence.py`) — the same lesson is taught in different years by
different schools, so a year printed in a lesson page's bytes is wrong for
every school that does not happen to share Design's assumption. All three of
this page's are removed, and each names the SUBJECT instead:

1. page line 189, the panel's mono label
     before  `Forward pointer · Year 9`
     after   `Forward pointer · Physics`
2. page line 190, inside the panel's prose
     before  `You will meet that in Year 9, in <a href="p2-01-energy-in-food.html">Energy in food</a> and <a href="p2-03-calculating-energy-transferred.html">Calculating energy transferred</a>.`
     after   `You will meet that in Physics, in the unit Energy at home.`
   The two anchors are removed as well as the year: under MRB-232 a link to P2
   is an EDGE, and both are authored as `references` below. `rich()` admits
   only `<em>` and `<strong>` in any case, so an `<a>` here would have rendered
   as visible tag soup.
3. page line 301, the endmatter heading
     before  `<h2>Continues in Year 9</h2>`
     after   `Continues in Physics`
   Authored as `connects_heading`; the `<h2>` is engine-emitted from it, so
   there was never a heading to write.

── The flagship: the person is the control ──────────────────────────────

`#s-ledger` is `person-ledger`, on `ks3-block ks3-dark ks3-practical` (page
line 105). Twelve foods, five eaters, one running total, and a match panel that
tells the student to switch person **without changing the food**. NOTES-B3 §3.3
names that instruction as the thing that must not be lost — it is the
experiment, and without it the ledger is a calculator.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-maths` came off the rail. Design draws FOUR stops and `#s-maths` ticks on
`Object.keys(s.plate).length > 0` (page line 423) — the LEDGER's predicate,
verbatim, one section to the left — and since `#s-maths` is an eyebrow, a
display line, three worked sums, a key fact and the forward pointer, with no
control, no commit and no field, MRB-208's "the rail carries only sections that
require the student to do something" looked to rule it out. So the lesson
shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; no invented or
dropped page structure; page wins over engine. Three stops where Design drew
four is not rendering what Design drew.

And the repeated predicate is Design saying how the stop ticks, not Design
being careless. `isDone()` is rail-level and returns the same expression for
`#s-ledger` and then for `#s-maths`, because the three sums are what the ledger
was for: the section carries no control because the ledger already took the
student's commitment. That is a MIRROR, resolved at rail level in `wireRail`'s
`paint()`.

So the fourth stop is declared: anchor `s-maths`, `mirrors: "s-ledger"`,
`done_when: "food_on_the_plate"` — the ledger's own predicate, named as
borrowed. `ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`. b3-01's `#s-nutrients`, b3-02's `#s-limits`,
b3-07's `#s-four` and c1-02's `#s-matrix` are restored the same way. The anchor
survives as it always did, so the tutor card's `#s-maths` link still lands.

── What could not be lifted, and why ────────────────────────────────────

1. **`#s-maths` is one band section on Design's page and four blocks here.**
   She draws a band panel containing three sum cards, a key fact and the
   forward pointer. The engine has no band panel that can hold a mono,
   multi-line working block, so the section becomes: a `rule` for the panel's
   eyebrow and statement, three `worked-example` blocks on the inset ground for
   the sums, the `key-fact`, and a second `rule` for the forward pointer. Every
   authored word survives and the document order is Design's exactly; what is
   lost is the single frame around them.

2. **The monospace alignment of the three workings.** Design lays each sum out
   as one pre-formatted mono block, with the figures right-aligned under each
   other and a `————` rule above the total. `r_fifa`'s step list has no
   pre-formatted slot, so each LINE of each sum is a step — every number and
   every label survives, the column alignment and the four rule lines do not.

3. **Each sum's note moves from after the working to before it.** The
   `worked-example` shell's order is eyebrow → heading → prompt → fifa, and
   `prompt` is the only prose slot. All three notes read as ledes rather than
   as codas; none of them is contradicted by the move.

4. **Sum 3's last line gains the label `share`.** Design's other two workings
   label their final line (`total`, `shortfall`) and this one does not;
   `r_fifa` renders a nameless step as an empty `<strong>`. One word, added
   inside a component Design drew, and reported.

5. **The forward-pointer panel is a `rule` block, not a dashed inset panel.**
   NOTES-B3 §6 says the panel is content and must not be restyled into a
   generic aside, and it is not: a `rule` keeps its own mono eyebrow and its
   own band panel, so it still reads as a deliberate forward pointer rather
   than as body prose. What it does not have is Design's dashed border, and
   `shared/ks3.css` is not this run's to change. `r_rule` always emits a
   statement paragraph, so this block ships one that is empty — the panel has
   no display-type line and inventing one would restructure Design's prose.
   The clean fix is a `forward` block type, or an optional statement on `rule`.

6. **A prose link to P1 loses its anchor.** Page line 204 opens *"You met this
   in <a>Energy stores</a>"*; `rich()` admits only `<em>` and `<strong>`, so
   the words stay and the link does not. It is NOT promoted to a `references`
   edge, because Design's endmatter card for this lesson lists two entries and
   adding a third would draw a link she did not.

⚑ For Mide's science gate:
  * NOTES-B3 §4 flags 7 and 8: the five requirement figures (5800 / 9500 /
    9000 / 13 500 / 25 000 kJ, the rower's being the one most likely to be
    challenged) and the twelve food kJ values, which are plausible portion
    figures rather than food-table ones. Both authored as delivered.
  * The three workings check out arithmetically: 3120 + 2400 + 450 + 1050 =
    7020; 9500 − 7020 = 2480; 1050 ÷ 9500 × 100 = 11.05…%. So do both marked
    rungs: 1100 + 1750 + 320 + 2400 + 2 × 1050 = 7670, and 9500 − 7670 = 1830,
    which Design rounds to "about 1800"; and 1050 ÷ 5800 = 18.1%.
  * ⚖️ MRB-225 holds. The bomb-calorimeter paragraph is history of measurement
    and lives in GOING FURTHER, and it retracts nothing above it — the body
    never claims the label figure is what the body extracts, and the layer
    explains why the fibre figure had to be corrected downwards.
"""

# ── the five eaters (page lines 337–348) ────────────────────────────────
#
# ⚠️ `lower` is authored, and one of them is a CORRECTION. Design writes
# `person.name.toLowerCase()` to build the match headline, which turns
# "An Olympic rower in training" into "an olympic rower in training" — a proper
# adjective lower-cased by a string method. The authored form keeps the capital.
PEOPLE = [
    {"id": "child", "label": "4-year-old", "name": "A 4-year-old",
     "lower": "a 4-year-old", "need": 5800,
     "why": "Small body, so little tissue to keep warm and fuel — but growing "
            "fast, and a surprising share of the total goes into building new "
            "tissue rather than moving about."},
    {"id": "teen", "label": "13-year-old", "name": "A 13-year-old",
     "lower": "a 13-year-old", "need": 9500,
     "why": "Almost an adult’s requirement, in a body that is still smaller "
            "than one. Adolescent growth is the most energy-expensive period "
            "of a human life after infancy."},
    {"id": "adult", "label": "Office worker",
     "name": "An adult with a desk job",
     "lower": "an adult with a desk job", "need": 9000,
     "why": "Full adult size, no growth to pay for, and very little movement. "
            "Roughly three quarters of this goes on simply staying alive and "
            "at 37 °C."},
    {"id": "builder", "label": "Bricklayer",
     "name": "An adult doing heavy manual work",
     "lower": "an adult doing heavy manual work", "need": 13500,
     "why": "The same body as the office worker, doing eight hours of "
            "lifting. The difference between these two rows is activity and "
            "nothing else."},
    {"id": "rower", "label": "Olympic rower",
     "name": "An Olympic rower in training",
     # ⊕ CORRECTED. See the note above this list.
     "lower": "an Olympic rower in training", "need": 25000,
     "why": "Large muscular body plus six hours of hard training. Athletes at "
            "this level struggle to eat enough, which is a problem most people "
            "never have."},
]

# ── the twelve foods (page lines 350–363) ───────────────────────────────
#
# ⚠️ `kj_label` is authored rather than composed. Design writes
# `f.kj === 0 ? '0 kJ' : f.kj + ' kJ each'`, and the branch matters: a single
# template would print "0 kJ each" against a glass of water, which claims a
# portion size for something that has none.
FOODS = [
    {"id": "toast", "name": "Toast and butter", "kj": 780,
     "kj_label": "780 kJ each"},
    {"id": "cereal", "name": "Bowl of cereal with milk", "kj": 1100,
     "kj_label": "1100 kJ each"},
    {"id": "banana", "name": "Banana", "kj": 450, "kj_label": "450 kJ each"},
    {"id": "apple", "name": "Apple", "kj": 320, "kj_label": "320 kJ each"},
    {"id": "sandwich", "name": "Cheese sandwich", "kj": 1750,
     "kj_label": "1750 kJ each"},
    {"id": "pasta", "name": "Plate of pasta and sauce", "kj": 2400,
     "kj_label": "2400 kJ each"},
    {"id": "chicken", "name": "Chicken breast and rice", "kj": 2100,
     "kj_label": "2100 kJ each"},
    {"id": "yoghurt", "name": "Pot of yoghurt", "kj": 520,
     "kj_label": "520 kJ each"},
    {"id": "nuts", "name": "Handful of nuts", "kj": 1250,
     "kj_label": "1250 kJ each"},
    {"id": "juice", "name": "Glass of orange juice", "kj": 380,
     "kj_label": "380 kJ each"},
    {"id": "chocolate", "name": "Chocolate bar", "kj": 1050,
     "kj_label": "1050 kJ each"},
    {"id": "water", "name": "Glass of water", "kj": 0, "kj_label": "0 kJ"},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py lines 104–105 character for character. The
    # slug is Design's delivery and is the one exception §8.4 allows, because
    # the slot has never generated a page — see the register's ruling.
    "slug":        "energy-in-food-and-what-you-need",
    "title":       "Energy in food and what you need",
    "discipline":  "biology",
    "unit":        "nutrition-and-digestion",
    "family":      "QUANTITATIVE",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚑ The CLAUSE, not the parent. `KS3.B.NUT.02` is split between B3 and P2
    # (MRB-232); this lesson owns *what you need and why*. The sub-ID is not
    # yet in `ks3_data/substatements.py` and this module does not put it there —
    # see the docstring.
    "covers":      ["KS3.B.NUT.02a"],
    "touches":     ["KS3.B.NUT.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 1},
                    {"id": "cells-and-systems", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚖️ MRB-232: the only route from this lesson to P2 is these two edges.
    # Neither exists as prose anywhere on the page, and the forward-pointer
    # panel names the SUBJECT and the unit rather than linking.
    #
    # P2 is not authored yet, so both render as Design's honest pending state —
    # the label, then "(Energy at home — coming soon)" — rather than as a dead
    # link. That is the §9 slice guarantee working, not a gap.
    "requires":    ["a-balanced-diet"],
    "assumes":     [],
    "references":  [
        # Design's own label. Without it the card would print the target's
        # title, "Energy in food", inside a lesson called *Energy in food and
        # what you need* — where it reads as a link back to this page.
        {"unit": "P2", "lesson": "energy-in-food",
         "label": "Energy in food (Physics)",
         "why": "Where comparing energy values from labels in kJ is taught as "
                "physics — the arithmetic and the units."},
        # No label: the target's own title is exactly what Design prints.
        {"unit": "P2", "lesson": "calculating-energy-transferred",
         "why": "Where a joule is derived from power and time rather than "
                "counted off a packet."},
    ],
    # ⊕ CORRECTED. Design's heading is "Continues in Year 9"; year is data, not
    # bytes. See the docstring, rewrite 3.
    "connects_heading": "Continues in Physics",
    "ks4_links":   [],
    "ks4_becomes": "Energy budgets, metabolic rate, and the effect of exercise "
                   "and body composition on requirement.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A label says 1050 kJ. Your body needs about 9500 kJ a "
                    "day. Neither number means anything until you know whose "
                    "day it is.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-maths` is the third: no control of
    # its own, so it mirrors `s-ledger` and ticks on the ledger's predicate —
    # see the docstring. `short` and `label` are Design's own strings (page
    # lines 329–335).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Same food",
         "done_when": "committed"},
        # Design's own predicate, kept: the stop asks the student to put food
        # on the plate. `wirePersonLedger` ticks on the portion count, so it
        # cannot tick on load and un-ticks if the day is emptied.
        {"anchor": "s-ledger", "short": "LEDGER", "label": "Feed a day",
         "done_when": "food_on_the_plate"},
        {"anchor": "s-maths", "short": "MATHS", "label": "On paper",
         "mirrors": "s-ledger", "done_when": "food_on_the_plate"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "Two people eat exactly the same food for a month.",
        "prompt": "Same meals, same portions, same times — about 11 000 kJ a "
                  "day each. One is a 68-year-old who spends the day reading. "
                  "The other is a 25-year-old cyclist covering 120 km a day. "
                  "After a month, one has gained mass and one has lost it.",
        "commit": "Same food in. Why the different outcome?",
        "options": [
            "The cyclist digests food more efficiently",
            "They transfer very different amounts of energy in a day",
            "The older person’s body stores food instead of using it",
            "11 000 kJ is the wrong amount for both of them",
        ],
        "reveal": "There is no such thing as the right amount of food. There "
                  "is only the amount that matches what a particular body "
                  "transfers in a day — and that number differs by a factor of "
                  "two between the two people in this paragraph.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ The `DIET` family is NOT in `docs/ks3/misconception-register.md`; the
    # full allocation argument is in `lesson_01_a_balanced_diet.py`. `DIET-06`
    # is pinned to this lesson by NOTES-B3 §5 — it is the row that must keep a
    # confrontation separate from `ENERGY-12`, which is the physics side of the
    # same belief, and the split is exactly MRB-232's seam.
    "misconceptions": [
        {"id": "DIET-06",
         "statement": "The energy in food gets used up and disappears.",
         "elicited_by": "feed-a-day",
         "confronted_by": "think-requirement"},
        {"id": "DIET-07",
         "statement": "Everyone needs about the same amount of food in a day.",
         # The ledger elicits it: a student who builds one day and then moves
         # the person under it has just watched the belief fail.
         "elicited_by": "feed-a-day",
         "confronted_by": "think-requirement"},
    ],

    # Design draws no keyword block anywhere in B3, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list.
    "vocabulary": [
        {"term": "kilojoule",
         "definition": "The unit energy in food is measured in. One kilojoule "
                       "is a thousand joules.",
         "note": "Written kJ. A packet may also print calories, which are an "
                 "older unit for the same thing."},
        {"term": "energy requirement",
         "definition": "The amount of energy a particular person needs to take "
                       "in over a day.",
         "note": "It belongs to the person, never to the food."},
        {"term": "intake",
         "definition": "The total energy in everything a person eats and "
                       "drinks over a day.",
         "note": None},
        {"term": "surplus",
         "definition": "Taking in more energy than you transfer, so the extra "
                       "is stored.",
         "note": None},
        {"term": "shortfall",
         "definition": "Taking in less energy than you transfer, so stores are "
                       "broken down to make up the difference.",
         "note": None},
    ],

    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-ledger — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b3/__init__.py::_normalise. Design's block is
        # `ks3-block ks3-dark ks3-practical` (page line 105).
        {"type": "person-ledger", "id": "feed-a-day", "anchor": "s-ledger",
         "demand": "investigate",
         "eyebrow": "At the bench · feed a person for a day",
         "heading": "Pick who you are feeding, then add food",
         # `total` is the ledger's real ceiling: twelve foods, six portions
         # each before the button wraps to zero. It exists so `setCount`'s
         # clamp has a true number rather than a guess — the format itself
         # quotes no total.
         "head_counter": {"format": "{n} portions on the plate", "total": 72,
                          "start": 0},

         "group_label": "Who is eating",
         "people": PEOPLE,
         "start_person": "teen",
         "need_format": "Needs {need} kJ / day",
         "total_format": "{total} kJ of {need} kJ",
         "balance": {
             "empty": "empty plate",
             "matched": "balanced for this person",
             "surplus": "{n} kJ surplus — stored",
             "short": "{n} kJ short — stores drawn on",
         },

         "food_label": "Tap to add a portion · tap again to remove one",
         "foods": FOODS,
         "count_format": "×{n}",
         "max_per_food": 6,

         "clear_label": "Empty the day",
         "portions": {"empty": "nothing added yet",
                      "some": "{n} portions, {total} kJ"},

         "tolerance": 5,
         # ⚖️ THE COPY THAT MUST NOT BE LOST (NOTES-B3 §3.3). Without the
         # instruction to switch person and keep the food, a match reads as
         # having finished, and the instrument stops being an experiment.
         "match": {
             "eyebrow": "Within 5% of the target",
             "head": "That day matches {person}.",
             "why": "Now switch person without changing the food. The same "
                    "plate is a surplus for one body and a shortfall for "
                    "another, and nothing about the food has changed — which "
                    "is the whole idea.",
         }},

        # #s-maths — Design's band panel, as four blocks. See "What could not
        # be lifted" 1. Rail stop 3, mirroring `s-ledger`.
        {"type": "rule", "anchor": "s-maths",
         "eyebrow": "Doing it on paper",
         "statement": "Three sums, and the units that make them behave."},

        {"type": "worked-example", "id": "sum-total"},
        {"type": "worked-example", "id": "sum-compare"},
        {"type": "worked-example", "id": "sum-share"},

        {"type": "key-fact", "ref": "requirement-belongs-to-the-person"},

        # ⊕ The forward pointer, rewritten sequence-free. NOTES-B3 §6: it is
        # content, and it is not restyled into a generic aside — it keeps its
        # own mono eyebrow and its own panel. See "What could not be lifted" 5
        # for the dashed border and the empty statement paragraph.
        {"type": "rule", "id": "forward-pointer",
         "eyebrow": "Forward pointer · Physics",
         "statement": "",
         "close": "You have used kJ here as a bookkeeping unit — energy in "
                  "versus energy needed. The full treatment belongs to "
                  "Physics: what a joule actually is, how energy is "
                  "transferred rather than used up, and how to calculate it "
                  "from power and time. You will meet that in Physics, in the "
                  "unit Energy at home. Nothing here contradicts it; it is the "
                  "same joule, counted less formally."},

        {"type": "misconception", "id": "think-requirement",
         "anchor": "s-think", "targets": "DIET-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "requirement-belongs-to-the-person",
         "text": "Energy requirement is not a property of food. It is a "
                 "property of the person eating it — set by their size, their "
                 "age, their growth and how much they move.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `feed-a-day` is authored inline in `core` and lifted here by
    # `ks3_data/b3/__init__.py::_normalise`.
    "activities": [
        # ── the three worked sums (page lines 365–375) ───────────────────
        # `ground: "inset"` is Design's own card surface inside the band panel,
        # measured off her markup; `.ks3-worked[data-ground="inset"]` is the
        # rule that carries it. Each LINE of each working is a step — see
        # "What could not be lifted" 2 — and the note is the `prompt`, which is
        # the shell's only prose slot and puts it above the working rather than
        # below it (3).
        {"id": "sum-total",
         "kind": "worked-example",
         "demand": "calculate",
         "ground": "inset",
         "eyebrow": "Sum 1",
         "heading": "Total the day up",
         "prompt": "Nothing clever — multiply each portion by how many, then "
                   "add. Marks are lost far more often on arithmetic and on "
                   "forgetting a portion than on method.",
         "fifa": [
             {"name": "4 slices toast and butter", "line": "4 × 780 = 3120 kJ"},
             {"name": "1 plate of pasta", "line": "= 2400 kJ"},
             {"name": "1 banana", "line": "= 450 kJ"},
             {"name": "1 chocolate bar", "line": "= 1050 kJ"},
             {"name": "total", "line": "= 7020 kJ"},
         ]},
        {"id": "sum-compare",
         "kind": "worked-example",
         "demand": "calculate",
         "ground": "inset",
         "eyebrow": "Sum 2",
         "heading": "Compare with the requirement",
         "prompt": "A shortfall is not automatically a fault in the day — it "
                   "is a statement that stores will be drawn on. Over one day "
                   "that is normal. Over a month it becomes mass loss.",
         "fifa": [
             {"name": "requirement (13-year-old)", "line": "= 9500 kJ"},
             {"name": "intake", "line": "= 7020 kJ"},
             {"name": "shortfall", "line": "9500 − 7020 = 2480 kJ"},
         ]},
        {"id": "sum-share",
         "kind": "worked-example",
         "demand": "calculate",
         "ground": "inset",
         "eyebrow": "Sum 3",
         "heading": "Turn a label into a share",
         "prompt": "The same bar is 18% of a 4-year-old’s day and 4% of a "
                   "rower’s. A percentage on a packet is only meaningful once "
                   "you say whose requirement it is a percentage of — which is "
                   "exactly what packets do not say.",
         "fifa": [
             {"name": "bar", "line": "= 1050 kJ"},
             {"name": "requirement", "line": "= 9500 kJ"},
             # ⊕ `share` is added: Design labels the last line of her other two
             # workings and not this one, and a nameless step renders an empty
             # <strong>. See "What could not be lifted" 4.
             {"name": "share", "line": "1050 ÷ 9500 × 100 = 11%"},
         ]},

        # ── the think-again block (page lines 194–206) ────────────────────
        # TWO wrong ideas in one block, separated by an amber-topped divider.
        # No commitment is asked for, on Design's page or here, so it is not a
        # rail stop and emits no completion contract.
        {"id": "think-requirement",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "DIET-07",
         "statements": [
             {"quote": "Everyone needs about 2000 calories a day.",
              "body": ["That figure is a labelling convention, not a fact "
                       "about a person. It exists so packets can print a "
                       "percentage, and it is the rounded average for an adult "
                       "woman doing moderate activity. Run the bench above "
                       "through all five people and the honest range is "
                       "roughly 5000 to 20 000 kJ a day — a fourfold spread, "
                       "and the top of it is a professional athlete rather "
                       "than an extreme case. A 4-year-old fed an adult's day "
                       "would be badly overfed; a rower fed a 4-year-old's day "
                       "would collapse in a week. When a question gives you a "
                       "number for a requirement, that number belongs to "
                       "somebody, and part of the answer is saying who."]},
             {"quote": "The energy in food gets used up and disappears.",
              # ⊕ The anchor on "Energy stores" is removed and the words kept —
              # `rich()` admits only <em> and <strong>. See "What could not be
              # lifted" 6.
              "body": ["You met this in Energy stores and it comes back "
                       "wearing a chef's hat. Nothing about eating destroys "
                       "energy. The chemical store in your food is "
                       "transferred: some to movement when you walk, some to "
                       "the chemical store of new tissue while you grow, and — "
                       "this is the part people miss — the great majority of "
                       "it to the thermal store of your surroundings. You are "
                       "a 70-watt heater. Sit in a small room with the door "
                       "shut and the temperature rises measurably, and that "
                       "rise is the energy from your breakfast, still entirely "
                       "present, just no longer anywhere useful. “Where did "
                       "the energy go” always has an answer."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS PASS.
    #   rung 1: correct 10w against distractors of 11 / 10 / 9 — the correct
    #           option is not strictly the longest, so it cannot be a tell.
    #   rung 2: correct 8w against distractors of 6 / 12 / 8 — likewise.
    # No distractor was rewritten, because there was nothing to repair.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Do the sum",
            "q": "A 13-year-old needing 9500 kJ eats: cereal (1100 kJ), a "
                 "cheese sandwich (1750 kJ), an apple (320 kJ), pasta "
                 "(2400 kJ) and two chocolate bars (1050 kJ each). What is "
                 "their intake, and how does it compare?",
            "options": [
                "7670 kJ — about 1800 kJ short of the requirement",
                "6620 kJ — they forgot to count the second chocolate bar",
                "7670 kJ — about 1800 kJ more than the requirement",
                "9500 kJ — the intake always matches the requirement",
            ],
            "answer": 0,
            "feedback": {
                1: "That is the total with only one bar. Read the portion "
                   "counts before adding — this is the single most common slip "
                   "in this kind of question.",
                2: "The arithmetic is right and the comparison is the wrong way "
                   "round. 7670 is less than 9500, so it is a shortfall.",
                3: "Nothing makes intake match requirement automatically. The "
                   "whole point of the sum is that it usually does not.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A chocolate bar label says “1050 kJ — 11% of your daily "
                 "needs”. A 4-year-old eats one. What share of their day is "
                 "it?",
            "options": [
                "11% — the label states it",
                "About 18%, because their requirement is much lower",
                "About 6%, because a smaller person gets more from the same "
                "food",
                "You cannot say without knowing their mass exactly",
            ],
            "answer": 1,
            "feedback": {
                0: "The label states a percentage of a standard adult figure. "
                   "It cannot know who is holding the bar, and the "
                   "4-year-old’s requirement is far lower.",
                2: "A smaller body does not extract more energy from a bar. "
                   "The bar’s energy is fixed; what changes is the size of the "
                   "requirement it is being compared against.",
                3: "You cannot be precise, but you can absolutely say the "
                   "share is bigger. Refusing to reason from an approximate "
                   "figure is its own mistake.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the pair",
            "q": "The office worker and the bricklayer in the bench above are "
                 "the same age and size, but their requirements differ by "
                 "4500 kJ a day. Explain where that difference goes, and why "
                 "the 4-year-old needs less than either despite growing "
                 "fastest.",
            "field_label": "Your explanation",
            "placeholder": "The bricklayer needs more because…",
            "success": [
                "Attributes the 4500 kJ difference to activity — muscles "
                "contracting for hours require energy transfer.",
                "Says the two bodies are otherwise identical, so activity is "
                "the only variable.",
                "Explains the 4-year-old’s lower total by their much smaller "
                "body: less tissue to keep warm and to maintain.",
                "Notes that growth does claim a share of a child’s "
                "requirement, and that it is still smaller in total than an "
                "adult’s maintenance.",
                "Avoids saying anyone ‘uses up’ energy — uses transferred, or "
                "stored, instead.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A school wants one standard lunch, the same portion for "
                 "every pupil aged 11 to 16. Using what you now know about "
                 "requirements, say what is wrong with the plan, what you "
                 "would do instead, and one thing you would need to find out "
                 "first.",
            "field_label": "Your answer",
            "placeholder": "One portion cannot work because…",
            "success": [
                "Says requirements vary substantially across this age range, "
                "so one portion cannot match all of them.",
                "Names at least two things the requirement depends on — age, "
                "size, sex, growth, activity.",
                "Proposes something workable: variable portions, second "
                "helpings, or a base meal plus add-ons.",
                "Names a real thing to find out — the age spread, activity "
                "levels, or how much pupils actually eat rather than are "
                "served.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Energy in food is measured in kilojoules. A person's daily "
                "requirement depends on their age, size, sex, rate of growth "
                "and level of activity, so there is no single correct figure. "
                "Take in more than you transfer and the surplus is stored; "
                "take in less and stores are broken down.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # MRB-225: the history of the measurement lives HERE, and it retracts
    # nothing above — the body never claims the label figure is what the body
    # extracts, and this explains why the fibre figure had to be corrected.
    "stretch": [
        {"type": "explainer", "id": "the-bomb-calorimeter",
         "text": "The numbers on a food packet were originally obtained by "
                 "burning the food. A weighed sample goes into a sealed steel "
                 "vessel packed with oxygen, the vessel sits in a known mass "
                 "of water, and the sample is ignited electrically; the rise "
                 "in water temperature gives the energy released. The device "
                 "is called a bomb calorimeter, and the name is literal enough "
                 "that early ones occasionally lived up to it. It measures the "
                 "total chemical energy in the sample, which is why the figure "
                 "for dietary fibre had to be corrected downwards later — a "
                 "calorimeter happily burns cellulose, and your gut cannot "
                 "digest a gram of it. The instrument was answering a "
                 "chemistry question when what was wanted was a biology one."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check a requirement calculation of your own?",
              "cta": "Ask about this lesson",
              "anchor": "s-maths"},

    # ⚠️ `convention_note`, NOT `safety_note` — a note about where the numbers
    # came from and a duty-of-care line, not a bench hazard. Routing it through
    # the safety treatment would devalue the line on b3-02, which has a real
    # one.
    "convention_note": "Requirement figures are rounded typical values used to "
                       "teach the principle. They are not a guide for anyone's "
                       "own eating, and this lesson does not set targets for "
                       "any individual. Questions about your own diet belong "
                       "with a doctor or a registered dietitian.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["measurement", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
