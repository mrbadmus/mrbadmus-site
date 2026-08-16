"""B5 L8 — Seed dispersal (CLASSIFY).

Authored against Design's approved page,
`KS3 B5 lessons/b5-08-seed-dispersal.dc.html` (595 lines), under the MRB-220
build contract. Every student-facing string is lifted byte-identical from that
page except the items listed under "What could not be lifted", none of which is
a sentence of science. The eight specimens, the five methods, the five method
buttons and all four ladder rungs came out of
`node tools/extract_design_payload.js`, not off a keyboard.

── ⚑ A RULED STATUTORY GAP LIVES IN THIS LESSON ─────────────────────────

`KS3.B.REP.02` asks for a *"quantitative investigation of some dispersal
mechanisms"*. This page has none: it is a CLASSIFY lesson and the student
measures nothing anywhere on it — eight specimens sorted by observable
structure into five methods, and not one number taken. Design's own NOTES-B5
flag 43 raises exactly this and asks for a decision rather than an opinion.

Ruled 16 Aug 2026 (MRB-244): **build what is on disk.** No practical, no timing
activity and no measurement has been invented here — that would be a component
Design did not draw (MRB-205), and it would also close the gap in the register
while leaving it open on the page a student actually reads.

`covers` claims `KS3.B.REP.02c` AS MINTED, at the bullet's full width with the
quantitative words in it, so that what is missing stays legible against what is
claimed. The same gap is recorded in `ks3_data/substatements.py`,
`ks3_data/biology_b5_reproduction.py` and `ks3_data/b5/__init__.py`; this is the
fourth record of it and the one that sits on the lesson itself. Flag 43 is
carried for Mide below.

Its visible consequence in this record: `ws` claims `analysis-and-evaluation`
and NOT `measurement`. Nothing on the page is measured, so nothing is claimed.

── ⚑ TELEOLOGY IS THE LESSON, AND IT IS NOT REINTRODUCED IN THIS FILE ───

NOTES-B5 flag 44. The page's first confrontation attacks *so that*, *wants to*
and *tries to* by name, and rung 3's fifth success criterion marks a student
down for using them. A plant with a structure that lands its seeds further away
leaves more descendants; it intends nothing.

So every string in this file that is MINE rather than Design's — the two
`vocabulary` definitions' worth of prose, the misconception statements, the
figure caption, the comments — is written without purpose language. A `demand`,
a definition or a criterion of my own that said *so that* would undo the lesson
from inside its own record, past every gate, in copy no reviewer is reading for
science.

Two of Design's own strings sit close to that line and are lifted unchanged,
because the page wins (MRB-205) and both are defensible as function rather than
intention:
  * the hook's commit — *"Why is it worth so much to a plant to move its seeds
    away?"* — where "worth" is a cost-benefit reading, and the reveal answers it
    in exactly those terms;
  * the blackberry's `why` — *"The timing is part of the design"* — design in
    the sense of the arrangement, not of a designer. Flagged, not altered.

── THE RAIL LOSES A STOP, AND IT IS THE DEFECT MRB-208 NAMES ────────────

Design draws FOUR stops (`RAIL`, page lines 318–323) and `isDone` (page line
429) ticks `#s-methods` on `Object.keys(s.opened).length >= 8` — the SORT's
predicate, character for character, one section to the left. `#s-methods` is an
eyebrow, a display statement, a five-row table and a key fact: no control, no
commitment, no field. `ks3_parity.check_rail_reachable` would fail it for
exactly that, and inventing a demand Design did not draw is closed to this build
(MRB-205).

So this lesson declares THREE stops. Same call, same reasoning and same shape as
c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-01's `#s-nutrients`, b3-07's
`#s-four` and b4-01's `#s-parts`. `#s-methods` KEEPS ITS ANCHOR, so every hash
link into it still works; it simply stops claiming to be completable.

`#s-think` is not a candidate for the fourth stop either: on this page it is two
quotes and two paragraphs with nothing to answer, so MRB-220 R1 — which promotes
a *committing* `#s-think` to `predict` — does not reach it.

⚑ NOTES-B5 §6 says "Rail stops: four in every lesson in the unit." That is
Design's intention and it is recorded here rather than silently met.

── What could not be lifted byte-identical, and why ─────────────────────

1. **The two inline links, in `#s-think` and in Going further.** Design writes
   *"This is <a href="b11-02-natural-selection.html">natural selection</a>
   again"* and *"the method that settled it borrows from
   <a href="b10-02-chromosomes-genes-and-dna.html">DNA</a>"*. `rich()` permits
   `<em>` and `<strong>` and nothing else, so an anchor would render as visible
   tag soup. The WORDS are unchanged and the hyperlinks are dropped — the same
   resolution as b3-07, b4-03 and b4-05.

   `natural-selection` is not lost: Design's own "Connects to" card names it, so
   it renders in the end matter, which is where the engine puts cross-lesson
   navigation. **`chromosomes-genes-and-dna` IS lost as a link**, and is
   deliberately NOT added to `references` to compensate: Design's end matter
   does not name it, and adding an edge she did not draw is as much an invention
   as adding a component. Reported rather than fixed. It is recorded in
   `touches` as `KS3.B.INH.02`, which is where a named-not-taught statement
   belongs.

2. **The `#s-methods` column captions do double duty, exactly as the engine
   intends.** Design prints "The structure that gives it away" and "What it
   costs the plant" once as column heads; `r_comparison` emits each caption
   again inside every cell, hidden by CSS above 820px, so a stacked row on a
   phone still says which column it came from. One authored string, two uses —
   not a second authoring.

3. **The key fact leaves Design's nested panel by exactly one level, and stays
   nested.** She draws it inside `#s-methods` on the card ground with the accent
   offset shadow; `r_comparison` is the one block with a nested key-fact slot,
   so it renders where she drew it, with `ground: "card"`.

4. **Design draws THREE endmatter link cards; the engine emits its fixed
   three.** "Before this lesson" (`fertilisation-seeds-and-fruit`) maps to
   `requires`; "Connects to" (`variation-and-competitive-success`,
   `natural-selection`) maps to `references` under her own heading; "At GCSE
   this becomes" maps to `ks4_becomes`. Nothing is dropped and no heading is
   lost — this is the one page in the run whose end matter fits the engine's
   shape without compromise.

5. **`ks4_links` gives way to `ks4_becomes`.** Design's third card is authored
   prose and §4.8.1 D makes the two mutually exclusive.

6. **The mono span in the legal line.** Design sets `b5-dispersal-specimens` in
   `var(--ks3-font-mono)` inside the sentence; a foot line is escaped, so the
   figure id renders as plain body text. The words are unchanged. Routed through
   `convention_note` and NOT `safety_note`: nothing in it is a safety
   instruction — it is a note about what the specimens are and a declaration
   about artwork that does not exist yet — and printing it in the treatment
   reserved for "never light a candle without an adult" devalues the safety
   line. b3-05, b3-07 and b4-01 resolve the identical foot line identically.

── Misconception ids ────────────────────────────────────────────────────

`REPRO-15` and `REPRO-16` are pre-allocated to this lesson by the commander, and
the register is maintained centrally — five parallel authors collided on B4's
family and this is the fix. **A THIRD belief is confronted on this page and it
takes `REPRO-24`**, minted here and reported: the sort's declared hard case, the
belief that a seed with no wing and no parachute cannot be wind-dispersed. It is
not a third entry in Design's "Think again" — it lives in the instrument (poppy,
specimen 03) and in rung 2, which is titled "The one that catches people" for
that reason. NOTES-B5 §2.6 calls it "the instrument's hard case and it should
not be softened", and a belief that a page spends a specimen and a marked rung
on is a misconception whether or not it is quoted in amber.

⚑ For Mide's science gate — NOTES-B5 §3 flags landing on THIS lesson:
  * flag 39 — the eight specimens and their five categories, **especially poppy
    as wind** by the censer mechanism. Design's own words: the one a marker
    might get wrong. Authored as delivered.
  * flag 40 — the burdock and Velcro story: de Mestral, 1941, "the next decade".
  * flag 41 — *"On a dry breezy day some travel a kilometre"* in the dandelion,
    against Going further's *"most seeds land within a few metres"*. Both are on
    the page and the pairing is deliberate; it is also the one place where a
    student meets the average and the tail in the same lesson.
  * flag 42 — dispersal distances measured by genotyping adult trees and
    seedlings, and the claim that the long tail matters more than the average.
  * flag 43 — **the statutory gap above.** Ruled, recorded, not closed.
  * flag 44 — **the teleology paragraph**, and rung 3 marking a student down for
    *wants* and *tries*. Design asks whether that is the right hill at KS3. This
    record is written on the assumption that it is; if it is not, this lesson is
    where the answer lands first.
  * flag 13 — `b5-dispersal-specimens` is named in Design's legal line and is
    not in `docs/ks3/diagram-manifest.md`. Declared at `status: "needed"`
    (§4.10, not a build blocker) so it is a tracked sourcing task rather than a
    dangling reference. Nothing is invented to fill it.

⚑ One page-internal tension of my own, reported not ruled (MRB-205):
  the `#s-sort` lede says *"three of these eight are wind-dispersed although
  only two look it"*, and the same block's poppy `why` says *"This is the one
  that catches people"*. Both are true and consistent. What sits oddly is the
  hook's option A — *"So the species can spread into new areas"* — which the
  reveal calls *"a consequence of dispersal, not the reason for it"*, while the
  Going further's closing argument is that the long tail *"is how a species
  reaches a new wood, recolonises after a fire, and shifts its range"*. Read
  together the page says spreading is real but is not the explanation, which is
  the correct distinction and is nowhere stated in those terms. Lifted
  unchanged either way; it is teaching copy, not a build fault.
"""

# ── the eight specimens (page lines 335–368, via extract_design_payload.js) ──
#
# ⚠️ NOT RETYPED. `desc`, `tell` and `why` are science-bearing prose and carry
# Design's own typographic apostrophes and em dashes.
#
# `desc` describes STRUCTURE ONLY and never pictures or names the mechanism —
# that is what makes the sort evidence-based rather than recall, and it is why
# `tell` exists as a separate field: the deciding feature is an observable, not
# a guess about what the plant is for. NOTES-B5 §2.6.
SPECIMENS = [
    {"id": "dandelion", "label": "Dandelion", "name": "Dandelion",
     "answer": "wind",
     "desc": "A single tiny seed, a few milligrams, carrying a spray of fine "
             "white hairs on a thin stalk above it.",
     "tell": "A parachute of hairs on a seed light enough for it to matter.",
     "why": "The hairs give a large surface area against the air and almost no "
            "extra mass, so the whole thing falls very slowly. Falling slowly "
            "is the entire trick: the longer it takes to reach the ground, the "
            "longer the wind has to carry it sideways. On a dry breezy day "
            "some travel a kilometre."},
    {"id": "sycamore", "label": "Sycamore", "name": "Sycamore key",
     "answer": "wind",
     "desc": "A hard seed at one end of a stiff papery blade about four "
             "centimetres long, curved along its length.",
     "tell": "One asymmetric wing, which makes it spin rather than drop.",
     "why": "The off-centre wing makes it autorotate on the way down, like a "
            "helicopter rotor with the engine off, and that slows the fall by "
            "a factor of several. A heavier seed than a dandelion’s can "
            "then still be moved by wind — not a kilometre, but well "
            "clear of the parent tree’s shade."},
    # ⚖️ THE HARD CASE, AND IT IS NOT SOFTENED. No parachute and no wing, and
    # still wind. `REPRO-24` is the belief this specimen exists to break.
    {"id": "poppy", "label": "Poppy", "name": "Poppy capsule",
     "answer": "wind",
     "desc": "A dry pepper-pot capsule on a long thin stem, with a ring of "
             "small holes opening under the rim. Hundreds of dust-fine seeds "
             "inside.",
     "tell": "Holes near the top of a capsule on a long springy stem.",
     "why": "This is the one that catches people, because there is no "
            "parachute and no wing. The stem sways in the wind and the seeds "
            "are shaken out through the holes a few at a time, then blown "
            "along the ground. The long stem and the small high holes are both "
            "essential: the capsule only empties when something is moving it, "
            "so the seeds leave on windy days and stay put on still ones."},
    {"id": "blackberry", "label": "Blackberry", "name": "Blackberry",
     "answer": "inside",
     "desc": "Sweet dark flesh in clustered segments, each holding one small "
             "hard pip. Green, hard and sour a fortnight earlier.",
     "tell": "Edible flesh around a seed with a very tough coat.",
     "why": "The flesh is payment and the pip is the cargo. Its coat survives "
            "the whole passage through a bird or a mammal, and it is deposited "
            "some distance away in a small heap of fertiliser. The timing is "
            "part of the design: the fruit stays hard, sour and green until "
            "the seeds inside are ready, and only then turns black and sweet."},
    {"id": "goosegrass", "label": "Goosegrass",
     "name": "Goosegrass, or cleavers", "answer": "on",
     "desc": "Small round green fruits in pairs, covered in tiny stiff hooked "
             "bristles. The whole plant sticks to clothing.",
     "tell": "Hooks on the outside, and nothing edible anywhere.",
     "why": "No flesh, no reward and no cooperation required — this one "
            "is stealing the ride. The hooks catch in fur or wool, the animal "
            "carries the fruit until it grooms or brushes past something, and "
            "the seed is dropped wherever that happens. Cheap for the plant, "
            "since hooks cost far less to build than sugar."},
    {"id": "burdock", "label": "Burdock", "name": "Burdock burr",
     "answer": "on",
     "desc": "A dense round burr, two centimetres across, made of many stiff "
             "bracts each ending in a backward-facing hook.",
     "tell": "The same hook principle, built at a larger scale.",
     "why": "Worth knowing for what it caused. In 1941 a Swiss engineer, "
            "George de Mestral, pulled burdock burrs out of his dog’s "
            "coat, looked at one under a microscope, saw hooks catching in "
            "loops of fur — and spent the next decade turning that into "
            "Velcro. A dispersal mechanism, copied exactly."},
    {"id": "coconut", "label": "Coconut", "name": "Coconut",
     "answer": "water",
     "desc": "A very large seed inside a thick fibrous husk, waterproof and "
             "full of air spaces, with its own store of liquid inside.",
     "tell": "A buoyant, waterproof case around a seed too heavy for anything "
             "else to move.",
     "why": "Far too heavy for wind and far too big for an animal to carry, so "
            "the husk does the work: it floats, keeps salt water out, and can "
            "survive months at sea before washing up on a beach and "
            "germinating. Every coconut palm on a remote island arrived that "
            "way."},
    {"id": "gorse", "label": "Gorse", "name": "Gorse pod", "answer": "flung",
     "desc": "A small dry pod that twists as it dries in hot sun and splits "
             "open with an audible crack.",
     "tell": "A pod that dries, twists and tears itself apart.",
     "why": "The two halves of the drying pod pull against each other until "
            "the seam gives way, and the sudden release flings the seeds "
            "several metres. On a hot still afternoon a gorse bank crackles "
            "continuously. This is the only method on the list that needs no "
            "wind, no water and no animal — the plant supplies the energy "
            "itself, stored in the way the pod dried."},
]

# The five method buttons, identical under every specimen (page lines 326–333).
# `id` is what `specimens[].answer` is matched against, so a specimen can never
# be unanswerable. Design's order, which is not the order of the table below —
# the buttons run wind, water, inside, on, flung and the table runs the same
# way, so the two agree and neither is sorted by frequency.
METHOD_CHOICES = [
    {"id": "wind",   "label": "Wind"},
    {"id": "water",  "label": "Water"},
    {"id": "inside", "label": "Inside an animal — eaten"},
    {"id": "on",     "label": "On an animal — hooked to fur"},
    {"id": "flung",  "label": "Flung by the plant itself"},
]

# ── the five methods, as `#s-methods`' comparison rows (page lines 370–381) ──
#
# Two columns, and they are the two Design captioned: the observable that
# identifies the method, and what it costs the plant. The cost column is the
# section's whole argument — "Nothing here is free" — and it is what keeps the
# five from reading as a list of nice ideas.
METHODS = [
    {"name": "Wind",
     "tell": "A parachute of hairs, a stiff wing, or a shaker capsule on a "
             "long stem. Always a very light seed.",
     "cost": "Cheap per seed, but almost all of them land somewhere useless, "
             "so the plant makes very large numbers."},
    {"name": "Water",
     "tell": "A buoyant, waterproof case — fibrous, corky or air-filled.",
     "cost": "Expensive to build and only available to plants growing by "
             "water, but it moves seeds no other method could shift at all."},
    {"name": "Inside an animal",
     "tell": "Sweet, coloured flesh around a seed with a very tough coat.",
     "cost": "The most expensive of all — the plant gives away sugar it "
             "made itself — and the most reliable, because the courier "
             "travels a long way and leaves the seed with fertiliser."},
    {"name": "On an animal",
     "tell": "Hooks, barbs or a sticky surface. No reward offered.",
     "cost": "Very cheap: hooks cost almost nothing compared with flesh. The "
             "trade-off is no control over where the animal goes or when it "
             "grooms."},
    {"name": "Flung by the plant",
     "tell": "A dry pod that twists and splits, often audibly.",
     "cost": "Cheap, and independent of weather, wind and animals — but "
             "the range is metres rather than kilometres."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 129 character for character (§8.4).
    "slug":        "seed-dispersal",
    "title":       "Seed dispersal",
    "discipline":  "biology",
    "unit":        "reproduction",
    "family":      "CLASSIFY",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `c` clause of the split bullet, AS MINTED — at the bullet's full
    # width, quantitative words included. See the docstring: the gap is ruled
    # open, and narrowing the claim here would hide it.
    "covers":      ["KS3.B.REP.02c"],
    # Named, not taught. INH.05 is the confrontation's own argument — variation,
    # competing more successfully, natural selection — which B11 owns and this
    # page borrows in one paragraph. INH.02 is the DNA fingerprinting in Going
    # further, and it is also where the dropped inline link to
    # `chromosomes-genes-and-dna` is accounted for.
    "touches":     ["KS3.B.INH.05", "KS3.B.INH.02"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 1},
                    {"id": "evidence-and-explanation", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's three endmatter cards map one-to-one onto the engine's three.
    "requires":    ["fertilisation-seeds-and-fruit"],
    "assumes":     [],
    "references":  [{"unit": "B11", "lesson": "variation-and-competitive-success"},
                    {"unit": "B11", "lesson": "natural-selection"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Adaptation, competition and the way populations spread "
                   "through an environment.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "The worst place a seed can land is directly underneath "
                    "the plant that made it. Everything on this page follows "
                    "from that.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # THREE stops. Design draws four; `s-methods` is dropped — see the
    # docstring. `short` and `label` are Design's own `RAIL_SHORT` and `RAIL`
    # strings (page lines 318–324).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Why move?",
         "done_when": "committed"},
        # Design's own threshold, kept: the stop ticks when all EIGHT specimens
        # have been checked, not on the first. A stop that ticked on one
        # specimen would call the sort finished at an eighth of it — and the
        # eighth that matters most is the poppy, which is specimen 03.
        {"anchor": "s-sort", "short": "SORT", "label": "Sort the eight",
         "done_when": "all_eight_checked"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3). Option A is the
    # teleological answer (`REPRO-15`) and the reveal is what takes it apart.
    "phenomenon": {
        "kind": "narrative",
        "title": "Parachutes, hooks, wings, explosives and bribes. All for a "
                 "journey of a few metres.",
        "prompt": "A plant that has just spent a season building a fruit then "
                  "spends more on getting rid of it. Whatever the seeds are "
                  "being moved away from must be costing them something.",
        "commit": "Why is it worth so much to a plant to move its seeds away?",
        "options": [
            "So the species can spread into new areas",
            "Because a seedling under its parent competes with it and loses",
            "To get the seeds away from animals that would eat them",
            "So the seeds can find soil with more minerals in it",
        ],
        "reveal": "Because the parent is the competition. A seedling "
                  "germinating in its parent's shade is asking for light that "
                  "is already taken, water from soil that is already being "
                  "drained, and minerals from ground that has been stripped "
                  "for years — against an opponent a thousand times its "
                  "size that got there first. It loses. Spreading into new "
                  "territory is a consequence of dispersal, not the reason for "
                  "it; the immediate problem is much closer to home.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    #
    # ⚠️ The `REPRO` family is maintained CENTRALLY in
    # `docs/ks3/misconception-register.md` by the commander, because five
    # parallel authors collided on B4's family. `REPRO-15` and `REPRO-16` are
    # pre-allocated to this lesson and nothing else here is mine to number.
    #
    # `REPRO-24` is the exception and it is minted here and reported: the third
    # belief this page confronts is not in Design's amber block at all. It is
    # the instrument's declared hard case (poppy, specimen 03) and rung 2's
    # whole subject. See the docstring.
    #
    # `elicited_by` is honest per entry. 15 really is surfaced by the hook —
    # option A is the belief, in the student's own commitment, before the
    # reveal. 16 is not asked for anywhere before the block that kills it, so
    # the block is named for both. 24 is elicited AND confronted inside the
    # sort: the student commits to a method for the poppy and then finds out.
    "misconceptions": [
        {"id": "REPRO-15",
         "statement": "Plants disperse their seeds so the species can spread "
                      "to new places.",
         "elicited_by": "hook",
         "confronted_by": "two-wrong-ideas"},
        {"id": "REPRO-16",
         "statement": "Fruit is food the plant provides for animals.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
        {"id": "REPRO-24",
         "statement": "A seed with no wing and no parachute cannot be "
                      "dispersed by wind.",
         "elicited_by": "sort-the-eight",
         "confronted_by": "sort-the-eight"},
    ],

    # Design draws no keyword block anywhere in B5, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list — which matters here,
    # because "dispersal", "germinate", "capsule", "burr" and "husk" would
    # otherwise all count against the page.
    #
    # ⚠️ MY WORDS, NOT DESIGN'S, so NOTES-B5 flag 44 binds on every one of
    # them: each definition says what the structure DOES, never what a plant
    # is trying to achieve. There is no "so that" and no "in order to" below,
    # and there must not be.
    "vocabulary": [
        {"term": "dispersal",
         "definition": "The movement of seeds away from the plant that made "
                       "them.",
         "note": "Classify a specimen by the structure that does the moving."},
        {"term": "germinate",
         "definition": "To begin growing from a seed into a young plant.",
         "note": None},
        {"term": "capsule",
         "definition": "A dry fruit with holes or slits that the seeds leave "
                       "through.",
         "note": "A poppy capsule empties only while something is shaking it."},
        {"term": "burr",
         "definition": "A fruit or seed head covered in hooks that catch in "
                       "fur, wool or clothing.",
         "note": None},
        {"term": "husk",
         "definition": "The tough outer covering of a fruit or seed.",
         "note": "A coconut's husk is fibrous and full of air spaces, and it "
                 "floats."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # Design's legal line names this slot and no artwork exists for it, so it
    # is DECLARED at `needed` rather than dropped: the manifest is generated
    # from this field, which turns a dangling reference into a tracked sourcing
    # task. `needed` is not a build blocker. NOTES-B5 flag 13 lists it as one
    # of ten across the unit, and calls the plant slots the easiest to source.
    #
    # No `figure` block is added to `core`: Design draws no figure slot on the
    # page, and one here would be a component nobody drew (MRB-205).
    #
    # ⚠️ The caption describes STRUCTURE and nothing else — a plate that
    # labelled each specimen with its method would answer the instrument's
    # eight questions before the student read them.
    "figures": [
        {"id": "b5-dispersal-specimens",
         "kind": "diagram",
         "caption": "The eight specimens drawn to scale from their structures "
                    "and left unlabelled by method: dandelion, sycamore key, "
                    "poppy capsule, blackberry, goosegrass, burdock burr, "
                    "coconut and gorse pod.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-sort — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b5/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so the segment is MEASURED and not inherited.
        {"type": "disperse-sort", "id": "sort-the-eight", "anchor": "s-sort",
         "demand": "classify",
         "eyebrow": "Sort the specimens · eight fruits and seeds",
         "heading": "Classify by what you can see",
         "head_counter": {"format": "{n} of 8 checked", "total": 8},
         "prompt": "Read the description, choose a method, then check it. "
                   "Judge each one on its structure alone — the plant's "
                   "name tells you nothing, and three of these eight are "
                   "wind-dispersed although only two look it.",

         "specimens": SPECIMENS,
         "choices": METHOD_CHOICES,

         # ⚖️ LOCKED UNTIL A METHOD IS CHOSEN, per specimen. Design's own gate
         # (page line 529): commitment is what buys the answer, and the options
         # lock once it is open so the student cannot quietly change their mind
         # after reading it.
         "choose_prompt": "How is it dispersed?",
         "reveal_label": "Check it",
         "hints": {"idle": "Choose a method first.",
                   "ready": "Ready.",
                   "opened": "Now try another specimen."},
         "verdicts": {"right": "Correct", "wrong": "Not this one"},

         # ⚖️ THE DECIDING FEATURE IS AN OBSERVABLE STRUCTURE, NEVER AN
         # INTENTION. Every one of the eight `tell` strings names something a
         # student can see on the specimen — hairs, one asymmetric wing, holes
         # near the top, edible flesh, hooks, a buoyant case, a pod that twists.
         # None of them says what the plant is for. That is the difference
         # between this instrument and a memory test, and it is also flag 44
         # holding at the level of a single line of copy.
         "tell_label": "Deciding feature",
         "specimen_label": "Specimen"},

        # #s-methods — the band panel. NOT on the rail; see the docstring.
        # `comparison` is the component: five rows, two captioned columns and
        # the nested key fact Design draws inside the panel.
        {"type": "comparison", "anchor": "s-methods",
         "eyebrow": "One problem · five answers",
         "eyebrow_tone": "accent-text",
         "statement": "Nothing here is free. Read what each method costs.",
         "ground": "band",
         "columns": [
             {"caption": "The structure that gives it away"},
             {"caption": "What it costs the plant"},
         ],
         # Design paints both cells at the same weight: the identifying
         # structure and its price are read together, and neither is the quiet
         # one.
         "row_tones": ["ink", "ink"],
         "rows": [{"name": m["name"], "cells": [m["tell"], m["cost"]]}
                  for m in METHODS],
         "key_fact": {"ref": "one-problem", "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "REPRO-15"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # One per lesson, nested in the comparison above. Never amber (MRB-208).
    "key_facts": [
        {"id": "one-problem",
         "text": "Every dispersal structure is a solution to one problem: a "
                 "seed that germinates beneath its parent competes with a "
                 "large established plant for light, water and minerals, and "
                 "usually loses. Classify a specimen by the structure you can "
                 "see, not by the plant it came from.",
         "placement": "nested",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment, on Design's page and
        # here, so it is not a rail stop and emits no completion contract.
        #
        # ⚠️ Both bodies are Design's, byte-identical, with the anchor around
        # "natural selection" dropped and `<em>` kept. The `<em>` tags are
        # load-bearing: they are what puts *so that*, *wants*, *tries*, *now*
        # and *not yet* in the student's eye as words being quoted rather than
        # used.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "REPRO-15",
         "statements": [
             {"quote": "Plants disperse their seeds so the species can spread "
                       "to new places.",
              "body": ["Nothing in a plant intends anything, and the sentence "
                       "quietly assumes a plan. What actually happened has no "
                       "foresight in it at all: among the seeds of long-dead "
                       "plants, some happened to have a slightly better wing, "
                       "a stickier hook, sweeter flesh. Those seeds landed "
                       "further from the parent more often, more of them "
                       "survived, and more of them grew into plants carrying "
                       "the same feature. Repeat for a few million generations "
                       "and every plant around you has dispersal machinery — "
                       "not because any of them wanted to travel, but because "
                       "the ones whose seeds did not travel left fewer "
                       "descendants. This is natural selection again, and the "
                       "test of whether you have the idea is whether you can "
                       "describe a dandelion parachute without using the words "
                       "<em>so that</em>, <em>wants</em> or <em>tries</em>."]},
             {"quote": "Fruit is food the plant provides for animals.",
              "body": ["The flesh is a fee, and the seed is what is being "
                       "smuggled. Look at how carefully the arrangement is "
                       "engineered against the animal's interest: the seed "
                       "inside has a coat tough enough to survive the whole "
                       "journey through a gut and come out able to grow, in "
                       "the middle of a small heap of fertiliser some distance "
                       "from the parent. Notice also the timing. An unripe "
                       "blackberry is green, hard, sour and often mildly "
                       "toxic, and it becomes sweet, soft and black only when "
                       "the seeds inside are finished — the colour change is a "
                       "signal that says <em>now</em>, and everything before "
                       "it says <em>not yet</em>. And plenty of fruits are "
                       "lethal to us while being perfectly good bird food, "
                       "because we are not the customer they are advertising "
                       "to. Payment, not generosity."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED with `verify_ks3.py`'s own
    # `length_tell()` heuristic, and BOTH MARKED RUNGS PASS.
    #   rung 1: correct 11w against distractors of 8 / 6 / 9. It is the longest,
    #           but it clears the longest distractor by 2 words (< 4) and by
    #           1.22× (< 1.4×), so neither threshold fires.
    #   rung 2: correct 3w against distractors of 2 / 2 / 3 — tied with the
    #           longest distractor, so it is not strictly the longest at all.
    # No distractor was rewritten, because there was nothing to repair.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Read the structure",
            "q": "A fruit you have never seen before is covered in small stiff "
                 "hooks and has no flesh on it. How is it dispersed?",
            "options": [
                "By wind — the hooks catch the air",
                "On the outside of an animal, caught in fur or feathers",
                "Inside an animal, after being eaten",
                "By hooking itself into the soil where it falls",
            ],
            "answer": 1,
            "feedback": {
                0: "Hooks add mass and no lift. A wind-dispersed fruit needs a "
                   "parachute or a wing, and needs to be light.",
                2: "Nothing about it is edible. A fruit dispersed that way pays "
                   "with flesh; this one pays nothing.",
                3: "That would place the seed directly under its parent — "
                   "the one outcome every dispersal mechanism exists to avoid.",
            }},
        # ⚖️ `REPRO-24`'s marked test. The three wrong answers are the three
        # methods a student can name from a picture; the right one is the
        # specimen with neither wing nor parachute.
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Which of these is wind-dispersed?",
            "options": [
                "A blackberry",
                "A poppy capsule",
                "A coconut",
                "A gorse pod",
            ],
            "answer": 1,
            "feedback": {
                0: "Sweet flesh around a hard pip — dispersed inside an "
                   "animal that eats it.",
                2: "Far too heavy for wind. The buoyant fibrous husk is the "
                   "clue: this one floats.",
                3: "The pod twists as it dries and flings its own seeds. The "
                   "plant provides the energy itself.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the whole idea",
            "q": "Explain why seed dispersal matters to a plant, then describe "
                 "three different methods, giving for each the structure that "
                 "identifies it and why that structure works.",
            "field_label": "Your explanation",
            "placeholder": "A seed that lands under its parent…",
            # ⚑ Criterion 5 is flag 44 as a mark scheme. It is Design's, lifted
            # whole, and it is the reason the rest of the unit reads as it does.
            "success": [
                "Says a seedling under its parent competes with it for light, "
                "water and minerals, and usually loses.",
                "Describes three genuinely different methods from the five.",
                "Gives the identifying structure for each one — parachute "
                "or wing, buoyant husk, flesh, hooks, splitting pod.",
                "Explains how each structure achieves the movement, not just "
                "that it does.",
                "Avoids saying the plant wants or tries to do anything.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "You find an unfamiliar seed: four millimetres across, hard, "
                 "smooth, with no wings or hooks, and it came out of a bright "
                 "red fleshy fruit. Say how it is most likely dispersed, state "
                 "the evidence you used, and give one prediction you could "
                 "test to check.",
            "field_label": "Your answer",
            "placeholder": "The evidence I would use is…",
            "success": [
                "Concludes it is dispersed inside an animal that eats the "
                "fruit.",
                "Uses the evidence: fleshy fruit, bright colour as a signal, "
                "small hard seed with a tough coat.",
                "Rules out at least one other method using the absent "
                "structures — no wing, no hook, too heavy for wind.",
                "Gives a testable prediction — for example that the seeds "
                "still germinate after passing through a bird, or that unripe "
                "fruits are green and sour.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Seeds are dispersed because a seedling under its parent "
                "competes with it and loses. Wind dispersal uses parachutes, "
                "wings or a shaker capsule and needs a very light seed. Water "
                "dispersal needs a buoyant waterproof case. Animal dispersal "
                "comes in two forms: hooks that catch on fur, and edible flesh "
                "around a seed with a coat tough enough to survive being "
                "eaten. Some plants fling their own seeds from a pod that "
                "dries and splits. Classify by the structure in front of you, "
                "not by the plant's name.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES-B5 flag 42. This is the strongest "how do we know" in the plant
    # half, and it is also the only place in the lesson where a distance is
    # measured at all — by geneticists, not by the student. That is exactly the
    # shape of the ruled gap: the page can say how dispersal distance IS
    # measured without the student measuring anything.
    #
    # ⚠️ The inline link on "DNA" is dropped; the words are unchanged.
    "stretch": [
        {"type": "explainer", "id": "how-far-does-a-seed-go",
         "text": "How far does a seed actually go? You cannot follow one, so "
                 "for most of the history of the subject the answer was a "
                 "guess. The method that settled it borrows from DNA: take a "
                 "plot of forest, take a small sample from every adult tree of "
                 "one species and record each tree's genetic fingerprint, then "
                 "fingerprint the seedlings on the ground. Because each "
                 "seedling's DNA carries a combination that could only have "
                 "come from particular parents, every seedling can be matched "
                 "to the tree it came from — and the distance between them "
                 "measured. What comes back is always the same shape of graph. "
                 "Most seeds land within a few metres of the parent, the "
                 "numbers fall away sharply with distance, and there is a long "
                 "thin tail of seeds that travelled hundreds of metres or "
                 "further. That tail is small and it matters more than all the "
                 "rest: it is how a species reaches a new wood, recolonises "
                 "after a fire, and shifts its range as the climate changes. "
                 "The rare events are the ones doing the important work, which "
                 "is a hard thing to see if you only measure the average."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check how to classify a specimen you have "
                      "never seen?",
              "cta": "Ask about this lesson",
              "anchor": "s-sort"},

    # ⊕ MRB-228's `convention_note`, not `safety_note` — see the docstring.
    # Design's one plain `.ks3-legal` paragraph: what the specimens are, the
    # fruit/seed distinction she made in the previous lesson, and the figure
    # declaration. The mono span around the figure id renders as body text
    # because a foot line is escaped; the words are unchanged.
    "convention_note": "The specimens are typical British examples described "
                       "from their structures. Several of them are strictly "
                       "fruits rather than seeds — a dandelion “seed"
                       "” and a sycamore “key” are both "
                       "single-seeded fruits — which is the distinction "
                       "drawn in the previous lesson. The specimen plate is "
                       "declared in the lesson record as "
                       "b5-dispersal-specimens, awaiting illustration.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # ⚑ `measurement` is deliberately NOT claimed. The student measures nothing
    # on this page — that is the ruled REP.02 gap, and claiming the strand here
    # would make the gap invisible to the one register that could still catch
    # it. What the lesson does do is classify from evidence and rule methods
    # out from absent structures, which is analysis and evaluation.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
