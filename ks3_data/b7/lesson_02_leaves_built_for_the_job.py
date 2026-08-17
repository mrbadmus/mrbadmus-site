"""B7 L2 — Leaves built for the job (MODEL).

Authored against Claude Design's approved page,
`KS3 B7 lessons/b7-02-leaves-built-for-the-job.dc.html` (579 lines), its
author's notes `KS3 B7 lessons/NOTES-B7.md` (§1.2, flags 8–12, §3) and
`docs/ks3/b7-inventory/PAYLOAD-SCHEMA.md`, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted" and the two changes
argued under "What was corrected". The four dials, the twelve dial options, the
five feature cards, the six habitat verdicts, the four hook options and all four
ladder rungs came out of `node tools/extract_design_payload.js` and the page's
own `renderVals()`, not off a keyboard.

── ⚖️ THE INSTRUMENT OPENS ON A DELIBERATELY BAD LEAF ───────────────────

`START` is enormous, thick and fleshy, many stomata, no cuticle. That is not a
default anybody forgot to tidy — it IS the lesson. The student's first instinct
(make it bigger, give it more holes) pushes the water readout further up, and
`Set it to a real oak leaf` is the REVEAL rather than the starting point.
Authoring a sensible opening state would delete the lesson.

⚠️ `start` IS NOT RUNTIME STATE and PAYLOAD-SCHEMA §0 rule 3 does not reach it.
Rule 3 bars `picks` / `tested` / `ran` / `shown` — values the runtime owns and
mutates. `start` is the authored CONTENT the runtime initialises from, and it
has two read sites in the same component: the opening state, and `Start again`,
which returns to it. The schema's §3 sketch lists `oak` and not `start`; that is
a schema omission, not a licence to drop the opening leaf, and it is reported.

    START  area=huge   thick=thick  stomata=many    cuticle=none
           → rate 1.35 × 0.65 × 1.25 × 1     = 110%
           → water 1.9 × 0.75 × 1.7 × 1.5    = 363%   verdict `swamp`
    OAK    area=broad  thick=thin   stomata=normal  cuticle=normal
           → rate 100%, water 100%                    verdict `oak`

⚑ THE NUMBERS ARE INVENTED TEACHING VALUES. The relative directions are right;
the magnitudes are illustrative. The page says so in its own foot line, that
line is carried whole as `convention_note`, and it is load-bearing rather than
decorative — it is what makes an explicitly illustrative model honest. NOTES-B7
flag 9 asks Mide to confirm that an explicitly illustrative model is acceptable
here.

── The rail is THREE stops, not Design's four ──────────────────────────

Design draws `s-hook`, `s-tuner`, `s-features`, `s-ladder`, and her own tick
function (page lines 396–402) reads:

    if (id === 's-tuner')    return s.moved;
    if (id === 's-features') return s.moved;

— stage three's predicate is stage two's, character for character. `#s-features`
is an eyebrow, a display statement, five static cards and a key fact: no
control, no commitment, no field. `ks3_parity.check_rail_reachable` fails a stop
whose section carries none of the signals `doneByDom()` looks for, and there is
no demand in the section to promote; inventing a control Design did not draw is
closed to this build (MRB-205). So the stop comes OFF the rail rather than
ticking on its neighbour's state.

`#s-features` keeps its anchor and its scroll-margin, so every hash link into it
still works. Identical call, identical reasoning, to b4-03's `#s-built`,
b5-06's `#s-designs`, b4-05's `#s-stomata`, b3-07's `#s-four`, c1-02's
`#s-matrix` and c1-05's `#s-scale`. `#s-think` is not a candidate either — on
this page it is two quotes and two paragraphs with nothing to answer, so
MRB-220 R1 (which promotes a *committing* `#s-think` to `predict`) does not
reach it.

⚑ NOTES-B7 §3 says "Rail stops: four in all four lessons." That is Design's
intention and it is recorded here rather than silently met: a fourth stop on
this page could only ever tick on the bench's state.

── `figures: []`, and that is MEASURED, not an omission ────────────────

The page draws no `<img>`, no `<figure>` and no placeholder, and its foot line
names no diagram slot — checked against `.ks3-legal` (page line 299), which is
entirely about the tuner being a teaching model. §4.10 allows an empty `figures`
for a lesson carried by its interactives.

⚑ **NOTES-B7 FLAG 12 IS NOT DISCHARGED BY THIS FILE AND IS NOT DROPPED.** A leaf
cross-section is the obvious candidate for this lesson and is **not in
`docs/ks3/diagram-manifest.md`**; Design taught the internal structure in the
five `#s-features` cards instead. Flag 12 asks for a ruling on whether a
cross-section is wanted and at what label depth *before* anything is
commissioned. Nothing is invented here to fill the gap and no figure slot is
declared, because declaring one would pre-empt the ruling with a caption. It is
Mide's to rule on.

── Stomata and guard cells are REFERENCED, not taught ──────────────────

NOTES-B7 flag 11 and §4.6's single-source rule. `stomata-and-gas-exchange-in-
plants` (B4 L5, `KS3.B.GAS.04`) owns them whole. This page names them on one
feature card, uses them as a dial, and says on the card itself whose subject
their opening and closing is. That sentence is a POINTER, and the pointer is
also carried as a `references` edge so the student has somewhere to go. Nothing
here expands into a teaching block, and nothing here restates b4-05's content —
if this lesson is ever edited, keep it that way.

── ⊕ What was CORRECTED, and why I was sure ────────────────────────────

1. **A build-internal lesson code was printed to a student.** Design's fourth
   feature card ends *"Their opening and closing is b4-05's subject."* `b4-05`
   is this repository's slot code. A student has never seen it, cannot resolve
   it, and it is precisely the platform self-explanation §8.10 bars from student
   prose — the same class of thing as writing a year group into a lesson body.
   Resolved to the lesson's own title, which is what the student can actually
   find and what `r_endmatter` prints on the edge two cards below:

       was:  Their opening and closing is b4-05's subject.
       now:  Their opening and closing is the subject of Stomata and gas
             exchange in plants.

   No science moves; the referent is the same lesson. Reported rather than
   quietly done, because **the same pattern recurs across the unit** — NOTES-B7
   §3 records that `b7-03` "leans on b6-03 by name" — and one ruling should
   cover all of B7 rather than four passes each deciding.

2. **Rung 2 was a length tell, and MRB-177 (ruled 17 Aug 2026) fixes the
   CONSTRUCT.** As drawn, the correct option ran 18 words against distractors of
   7 / 8 / 13 — it cleared the longest by 5, failing `length_tell()`'s ≥4-word
   threshold, and a student could have scored the rung without reading it. The
   correct answer states a RULE (subject, condition, consequence); the three
   distractors stated one-clause wrong REASONS, so it was longer BY
   CONSTRUCTION. Each distractor now states a WRONG RULE in the same shape, with
   the misconception as the consequence and the same belief underneath it:

       was  7w  "Green light is weaker than red light"
       now 17w  "Green light is weaker than red light, so a plant under a green
                 filter receives less energy"
       was  8w  "The green filter is blocking the carbon dioxide"
       now 20w  "A green filter blocks carbon dioxide as well as light, so the
                 pondweed runs short of the gas it needs"
       was 13w  "The plant is already green, so it does not need any more green"
       now 18w  "A leaf is already full of green, so adding more green light
                 cannot top it up any further"

   **The correct option is unchanged, `answer: 1` is unchanged, the gate's
   threshold is unchanged, and all three `feedback` corrections are still
   byte-identical** — each was already the right answer to its distractor's
   belief, and the beliefs did not move. Nothing is padded: every added clause
   is the consequence a student who holds that belief would actually draw.
   Rung 1 is clean as drawn and is untouched.

   ⚑ Rewriting a distractor changes what a marked question measures, which is
   Mide's gate. On b5-06 and b4-03 the replacement copy was his. This copy is
   not, and it is flagged for the same gate.

── What could not be lifted byte-identical, and why ────────────────────

1. **The feature cards lose their `where` line as a separate line.** Design
   draws three lines per card — a mono accent location ("Top layer"), a display
   name ("Palisade cells"), then the job. `r_rule`'s cards are `term` + `gloss`
   and have no third slot. The location is science on a MODEL lesson about where
   things sit in a leaf, so it is JOINED to the name with " · " rather than
   dropped: `"%s · %s" % (name, where)`. Identical resolution, identical
   separator, to `ks3_data/b5/lesson_02`'s five step cards. No word changes.

2. **The key fact is nested inside `#s-features` on the page and renders under
   it here.** Design draws it inside the band panel; `r_rule` has no nested
   `key_fact` slot (`r_comparison` does, and this section is not a comparison —
   it is five one-column cards). It is emitted as the very next block in
   document order, so a reader sees it in the same place. Same resolution as
   `ks3_data/b5/lesson_02`'s `#s-fert`.

3. **The instrument's section heading loses its `<h2>` level.** "Try to win on
   both readouts" is authored as the instrument's `heading` and the renderer
   decides the tag. No word changes.

4. **Design draws FOUR endmatter cards; the engine's grid is three plus the
   tutor.** Here they map exactly — "Before this lesson" is `requires`,
   "Connects to" is `references`, "At GCSE this becomes" is `ks4_becomes`, and
   the tutor card is `tutor`. Nothing is lost. This is the first B-series page
   where the engine's fixed grid and Design's drawing agree card for card, and
   it is worth recording as the shape that does NOT need the b4-03 / b5-06
   two-cards-into-one compromise.

5. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

6. **The page's own apostrophe inconsistency is carried as drawn.** `#s-think`
   writes *"an object's colour"* with a straight `'` while every other
   possessive on the page uses `’`. MRB-205 says the page wins and that a page
   contradicting itself is reported rather than silently ruled on. Lifted with
   the straight apostrophe.

── The shell is MEASURED, and the engine pass owns the map ─────────────

`#s-tuner` is `ks3-block ks3-dark ks3-practical` (page line 105), so the segment
is `practical` — measured from Design's own markup, per PAYLOAD-SCHEMA §0 rule 2
and build-contract §4, not inherited from the hook above it. Under the B5/B6
`_normalise()` mechanism the segment is NOT authored on the block: it lives in
`ks3_data/b7/__init__.py`'s `_INSTRUMENT_SEGMENTS`, which the ENGINE pass owns
and writes in one pass. **`"leaf-tuner": "practical"` must be in that dict.** A
missing entry does not fail the build — it renders the instrument as an unlifted
block and ships a bare list past a green kinds gate.

⚠️ THE INSTRUMENT IS ON INK. `.ks3-dark p` is (0,1,1) and beats a bare
instrument class at (0,1,0) — the defect that shipped a B4 chain label at
1.21:1, invisible, past a green kinds gate. That is the renderer's problem
rather than this module's, and it is recorded here because this payload is what
feeds it.

⚑ For Mide's science gate — the NOTES-B7 flags landing on THIS lesson:
  * **flag 8** — chlorophyll absorbs red and blue and reflects green, with the
    purple-pink grow-lamp example and the green-filter pondweed result. All
    three verified against the absorption spectra of chlorophylls a and b
    (maxima near 430 and 662 nm, and 453 and 642 nm; the 500–570 nm band is
    poorly absorbed and is what reaches the eye). The page's framing — that the
    misconception is "the exact opposite" — is right, and a green leaf really is
    throwing green light away. Blue-plus-red horticultural LEDs really do read
    as magenta. Nothing changed.
  * **flag 9** — the tuner numbers are invented teaching values, declared in the
    foot line. See above.
  * **flag 10** — autumn colour. Verified and PRECISE as drawn: the page says
    *"the yellows and oranges"* were present all summer, which is true of the
    carotenoids and xanthophylls and would NOT have been true of the reds
    (anthocyanins are largely synthesised in autumn, not unmasked). Design chose
    the two colours the claim holds for. Nitrogen and magnesium really are the
    expensive atoms recovered when chlorophyll is dismantled — magnesium sits at
    the centre of the ring and four nitrogens hold it. Nothing changed.
  * **flag 11** — stomata and guard cells referenced, not taught. See above; the
    only edit is the lesson code resolved to the lesson title.
  * **flag 12** — no diagrams, and the leaf cross-section is not in the
    manifest. See above; `figures` is EMPTY and the flag stands.
  * the cactus claim in the second confrontation — *"a cactus has done away with
    leaves altogether and photosynthesises in its stem, its spines being leaves
    that gave up the job entirely."* Correct: cactus spines are modified leaves,
    developing from leaf primordia in the areole, and the stem is the
    photosynthetic organ. (*Pereskia* keeps true leaves and is well beyond KS3.)
    Nothing changed.
"""

# ── the four dials (page lines 319–339, via extract_design_payload.js) ──
#
# `r` = contribution to photosynthesis rate, `w` = contribution to water lost.
# Both are multipliers on an oak-leaf baseline of 1, and the readouts are the
# PRODUCT of the four — which is why no single dial can win on both.
#
# ⚑ These are invented teaching values. See the docstring and the foot line.
# The directions are what carry the science: more area and more stomata raise
# both readouts and raise water faster; thickness and a waxy cuticle buy water
# back and cost rate.
DIALS = [
    {"id": "area", "name": "Surface area",
     "options": [
         {"id": "narrow", "label": "Needle",   "r": 0.35, "w": 0.3},
         {"id": "broad",  "label": "Broad",    "r": 1,    "w": 1},
         {"id": "huge",   "label": "Enormous", "r": 1.35, "w": 1.9},
     ]},
    {"id": "thick", "name": "Thickness",
     "options": [
         {"id": "thin",  "label": "Thin",             "r": 1,    "w": 1},
         {"id": "thick", "label": "Thick and fleshy",  "r": 0.65, "w": 0.75},
     ]},
    {"id": "stomata", "name": "Stomata",
     "options": [
         {"id": "few",    "label": "Few",    "r": 0.5,  "w": 0.4},
         {"id": "normal", "label": "Normal", "r": 1,    "w": 1},
         {"id": "many",   "label": "Many",   "r": 1.25, "w": 1.7},
     ]},
    {"id": "cuticle", "name": "Waxy cuticle",
     "options": [
         {"id": "none",   "label": "None",   "r": 1,   "w": 1.5},
         {"id": "normal", "label": "Normal", "r": 1,   "w": 1},
         {"id": "thick",  "label": "Thick",  "r": 0.9, "w": 0.6},
     ]},
]

# ── the two readouts (page lines 514–519) ───────────────────────────────
#
# The `id` is how the renderer knows which product it is showing, and it is also
# what the tone follows: Design paints the rate bar `--ks3-ok` and the water bar
# `--ks3-alert`, and each bar's width is the percentage HALVED and clamped at
# 100, so a full bar means 200% of an oak leaf. Those three facts are
# measurement and they belong in the renderer; they are recorded here rather
# than authored as keys, because a key with no read site is a dead key (R5).
READOUTS = [
    {"id": "rate",  "label": "Photosynthesis rate", "suffix": "% of an oak leaf"},
    {"id": "water", "label": "Water lost per day",  "suffix": "% of an oak leaf"},
]

# ── the five feature cards (page lines 344–350) ─────────────────────────
#
# `where` is joined to `name` with " · " — see "What could not be lifted" 1.
# The job prose is untouched except for the resolved lesson code on the fourth
# card — see "What was corrected" 1.
#
# ⚠️ Order is Design's and is load-bearing: it walks DOWN through the leaf —
# whole leaf, top layer, middle, underside — and then the veins, which are the
# one feature that is everywhere at once. Sorting these would break the reading.
FEATURES = [
    ("The whole leaf", "Broad and flat",
     "Intercepts as much light as possible for the tissue it took to build, "
     "and puts every cell close to a surface."),
    ("Top layer", "Palisade cells",
     "Tall cells packed with chloroplasts, stacked directly under a "
     "transparent upper skin where the light is strongest."),
    ("Middle", "Spongy layer and air spaces",
     "Open channels that let carbon dioxide diffuse to every photosynthesising "
     "cell, and give oxygen a way out."),
    ("Underside", "Stomata and guard cells",
     "Adjustable holes for gas exchange, on the shaded underside where less "
     "water evaporates. Their opening and closing is the subject of Stomata "
     "and gas exchange in plants."),
    ("Throughout", "Veins",
     "Xylem brings water up from the roots, phloem carries the sugar away, and "
     "the vein network holds the blade rigid and flat."),
]

FEATURE_CARDS = [{"term": "%s · %s" % (name, where), "gloss": job}
                 for where, name, job in FEATURES]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 140 character for character. Slugs are
    # permanent (§8.4) and are the join for every `requires` edge.
    "slug":        "leaves-built-for-the-job",
    "title":       "Leaves built for the job",
    "discipline":  "biology",
    "unit":        "photosynthesis",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.PHOT.03` — "the adaptations of leaves for photosynthesis" — the
    # third PHOT bullet, owned WHOLE. One bullet, one lesson, nothing to split:
    # b7-01 owns PHOT.01 (reactants, products, word summary) and b7-04 owns
    # PHOT.02 (the dependence of almost all life).
    "covers":      ["KS3.B.PHOT.03"],
    # Named and used, owned elsewhere. The stomata dial and the fourth feature
    # card use GAS.04 without teaching it (b4-05 owns it, §4.6); the hook, the
    # readouts and the key note assume the reaction without stating it (b7-01
    # owns PHOT.01).
    "touches":     ["KS3.B.GAS.04", "KS3.B.PHOT.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "structure-function", "level": 3},
                    {"id": "particles", "level": 2},
                    {"id": "energy", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's endmatter, card for card. "Before this lesson" names two, and
    # both are `requires`: b7-01 is the reaction this lesson's leaf performs,
    # and b1-04 is where a student first met a cell shaped by its job.
    #
    # ⚑ `the-photosynthesis-reaction` is a slot in structure.py and is being
    # authored in this same run by a parallel pass. `requires` resolves against
    # the REGISTRY, which is built from structure.py, so the edge is valid
    # whether or not that module has landed yet; until it does, the target
    # renders as its coming-soon page. Reported so nobody reads a green build
    # as proof the lesson exists.
    "requires":    ["the-photosynthesis-reaction",
                    "specialised-cells"],
    "assumes":     [],
    # Both cross a unit boundary, so both take the dict form (§4.6). The first
    # is the edge that makes the fourth feature card a pointer rather than a
    # teaching block.
    "references":  [{"unit": "B4",
                     "lesson": "stomata-and-gas-exchange-in-plants"},
                    {"unit": "B4", "lesson": "alveoli-built-for-exchange"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    # Renders only because `ks4_links` is empty — Design's third endmatter card
    # is prose, not a link, and this is the slot §4.8.1 D added for it.
    "ks4_becomes": "Leaf cross-sections, transpiration and the potometer, and "
                   "limiting factors on the rate of photosynthesis.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A leaf has to catch light, let a gas in, and not dry out — "
                    "and the second and third of those pull in opposite "
                    "directions. Every feature you can name is a settlement "
                    "between them.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # THREE stops. Design draws four; `s-features` is dropped — see the
    # docstring. `short` and `label` are Design's own `RAIL_SHORT` and `RAIL`
    # strings (page lines 309–315).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Every hole leaks", "done_when": "committed"},
        # Design's own predicate, kept: `s.moved` goes true the moment any dial
        # option or the oak button is pressed. One press is a real commitment
        # here — it is the act of changing the leaf and watching both readouts
        # move — so this is not the b3-02 case where a bench of twenty would
        # have ticked after one.
        {"anchor": "s-tuner",  "short": "TUNER",
         "label": "Build a leaf", "done_when": "any_dial_moved"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key.
    #
    # ⚖️ The correct-sounding option is D and it is "none of them", which is the
    # whole shape of the lesson: the first three are each a real improvement to
    # one readout and each is charged for. A student who picks A, B or C has not
    # made a mistake — they have made the move the tuner is about to price.
    "phenomenon": {
        "kind": "narrative",
        "title": "Every hole that lets carbon dioxide in lets water out.",
        "prompt": "A leaf needs an opening for the gas it is built from. The "
                  "same opening leaks water, and a plant that runs dry cannot "
                  "photosynthesise at all. Broad leaves catch more light and "
                  "lose more water; thick leaves hold more chloroplasts and "
                  "light cannot reach the ones at the bottom.",
        "commit": "Which single change would make a leaf photosynthesise "
                  "faster at no cost?",
        "options": [
            "Give it more stomata, so more carbon dioxide gets in",
            "Make it broader, so it catches more light",
            "Make it thicker, so it holds more chloroplasts",
            "None of them — each one costs the plant something",
        ],
        "reveal": "None of them. Every one raises the rate and charges for it, "
                  "which is why leaves in a wet forest, a hedgerow and a desert "
                  "are shaped so differently while doing the same chemistry. "
                  "Adaptation is not a list of improvements — it is a "
                  "compromise struck for one particular place.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Ids are PRE-ALLOCATED by PAYLOAD-SCHEMA §6 and the statements are lifted
    # byte-identical from `docs/ks3/misconception-register.md` rows 598–599.
    # `PLANT-10` is this lesson's spare and stays PERMANENTLY UNUSED, like
    # `DRUG-07` and `REPRO-17`/`20`/`21`/`23` — it is not re-pointed at a
    # different belief, because ids are permanent.
    #
    # Both names resolve against the BUILT page (MRB-244): `s-think` is the
    # confrontation section's anchor and `s-tuner` is the instrument section's,
    # and both are emitted as real element ids.
    #
    # `elicited_by` is honest per entry, and they differ. PLANT-03 is not asked
    # for anywhere before the block that kills it, so the block is named for
    # both ends. PLANT-04 really is surfaced by the instrument: the tuner opens
    # on an enormous leaf and the student's first move is usually to make it
    # bigger still, which is the belief acted out before it is named.
    "misconceptions": [
        {"id": "PLANT-03",
         "statement": "Leaves are green because chlorophyll uses green light.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
        {"id": "PLANT-04",
         "statement": "The bigger the leaf, the better the plant.",
         "elicited_by": "s-tuner",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block on this page, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list.
    #
    # ⚠️ Every definition below is authored, not lifted, and every one is
    # written structurally — what the thing IS and what happens in it, never
    # what it is "for". That is not house style here, it is this page's own
    # argument: "Adaptation is not a list of improvements — it is a compromise
    # struck for one particular place." A definition that said "so that the
    # plant can…" would contradict the lesson two blocks above it.
    #
    # `stoma` is glossed and NOT taught (§4.6, b4-05 owns it): the entry says
    # what the pore is and stops before the guard cells' mechanism.
    "vocabulary": [
        {"term": "adaptation",
         "definition": "A feature of an organism that works well in the "
                       "conditions where it lives.",
         "note": "Better in one place, not better in general."},
        {"term": "chlorophyll",
         "definition": "The green pigment inside a chloroplast that absorbs "
                       "light.",
         "note": "It absorbs strongly in the red and the blue, and reflects "
                 "the green in the middle."},
        {"term": "chloroplast",
         "definition": "The part of a plant cell in which photosynthesis "
                       "happens.",
         "note": None},
        {"term": "palisade cells",
         "definition": "Tall cells packed with chloroplasts, in a layer just "
                       "under the upper surface of a leaf.",
         "note": None},
        {"term": "spongy layer",
         "definition": "The loose layer in the middle of a leaf, with air "
                       "spaces between the cells.",
         "note": "The air spaces are how carbon dioxide reaches cells that are "
                 "nowhere near a hole."},
        {"term": "cuticle",
         "definition": "The waxy layer covering the outer surface of a leaf.",
         "note": "Water evaporates far more slowly through wax than through a "
                 "bare cell wall."},
        {"term": "stoma",
         "definition": "A small pore in the surface of a leaf, through which "
                       "gases move in and out.",
         "note": "More than one is stomata. They are mostly on the underside."},
        {"term": "xylem",
         "definition": "The tissue that carries water up from the roots.",
         "note": None},
        {"term": "phloem",
         "definition": "The tissue that carries dissolved sugar away from the "
                       "leaf.",
         "note": None},
        {"term": "diffusion",
         "definition": "The spreading of a substance from where there is more "
                       "of it to where there is less.",
         "note": "It gets slower the further the substance has to travel, "
                 "which is why a leaf is thin."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # EMPTY, deliberately, and MEASURED: the page draws no <img>, no <figure>
    # and no placeholder, and its foot line names no diagram slot. NOTES-B7
    # flag 12 stands open — see the docstring. Nothing is declared here, because
    # declaring a slot means writing a caption, and a caption would pre-empt the
    # ruling flag 12 asks for.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-tuner — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b7/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED — see the docstring.
        {"type": "leaf-tuner", "id": "build-a-leaf", "anchor": "s-tuner",
         "demand": "investigate",
         "eyebrow": "At the bench · build a leaf",
         "heading": "Try to win on both readouts",
         # The mono counter beside the heading. `idle` is Design's own text
         # before anything has been touched, and it is the one string in the
         # counter that is not computed.
         "head_counter": {"format": "{rate}% rate · {water}% water",
                          "idle": "nothing changed yet"},
         "prompt": "Four dials, two readouts, and the readouts disagree. Push "
                   "the rate up and watch the water loss follow it. The verdict "
                   "at the bottom says where your leaf could actually live.",

         "dials":    DIALS,
         "readouts": READOUTS,

         # ⚖️ THE OPENING LEAF IS DELIBERATELY BAD. See the docstring. Two read
         # sites: the initial state, and `Start again`, which returns to it.
         "start": {"area": "huge", "thick": "thick",
                   "stomata": "many", "cuticle": "none"},
         # The REVEAL, not the default.
         "oak":   {"area": "broad", "thick": "thin",
                   "stomata": "normal", "cuticle": "normal"},
         "oak_label":   "Set it to a real oak leaf",
         "reset_label": "Start again",

         # ── the six habitat verdicts (page lines 453–472) ────────────────
         #
         # ⚠️ ORDER IS THE CASCADE AND IT IS LOAD-BEARING. Design evaluates
         # these as an if/else chain on the two percentages, so an earlier
         # branch wins outright. The thresholds are the renderer's and are
         # recorded here as comments rather than authored as keys (R5 — a key
         # with no read site is a dead key). Read the branch id as the
         # condition:
         #
         #   swamp     water > 150 and rate >= 90
         #   worst     water > 150                    (rate < 90 by then)
         #   desert    rate  <  45 and water < 60
         #   oak       rate  >= 85 and water <= 115
         #   slow      rate  <  45                    (water >= 60 by then)
         #   middling  everything else
         #
         # All six are reachable, checked against the dial values above:
         #   swamp    huge/thick/many/none      110% / 363%   ← the opening leaf
         #   worst    broad/thick/many/none      81% / 191%
         #   desert   needle/thin/few/thick      16% /   7%
         #   oak      broad/thin/normal/normal  100% / 100%   ← the oak button
         #   slow     needle/thin/many/none      44% /  77%
         #   middling broad/thin/few/normal      50% /  40%
         #
         # ⚑ `worst` is pedagogy, not a fallback: it is the branch that tells a
         # student they have spent water and bought nothing, and points them at
         # the dial that did it. Deleting it would let that leaf read as merely
         # thirsty.
         #
         # No `tag`. PAYLOAD-SCHEMA §3 sketches one per branch; on this page the
         # label above the verdict is "Where this leaf could live" and it is the
         # SAME on all six, so it is the block's chrome rather than per-branch
         # data. Authoring it six times would pretend it varies. Reported.
         "verdicts": {
             "swamp": {
                 "head": "A swamp, and nowhere drier",
                 "why": "A fast leaf with a serious thirst. In a rainforest or "
                        "a marsh, where the roots can always replace what the "
                        "leaf loses, this wins. Put it on a hillside in July "
                        "and it wilts by lunchtime, and a wilted leaf "
                        "photosynthesises at nothing."},
             "worst": {
                 "head": "The worst of both",
                 "why": "Heavy water loss and a poor rate to show for it. "
                        "Something here is costing water without buying light "
                        "— look for the dial that raised the loss without "
                        "raising the rate."},
             "desert": {
                 "head": "A desert survivor",
                 "why": "Very little water lost, and a slow rate accepted as "
                        "the price. Real plants built like this grow for years "
                        "to reach the size an oak manages in a season, and they "
                        "are still there when the fast ones have died."},
             "oak": {
                 "head": "Roughly the leaf on the tree outside",
                 "why": "A high rate at a water cost a temperate climate can "
                        "supply. This is the settlement an oak, a sycamore and "
                        "most British hedgerow plants have arrived at — not the "
                        "maximum of either readout, which is the point."},
             "slow": {
                 "head": "Slow, and not saving much",
                 "why": "The rate has fallen further than the water loss. "
                        "Whatever this leaf is paying for, it is not getting "
                        "enough back."},
             "middling": {
                 "head": "Workable, in a mild place",
                 "why": "A middling leaf: neither the fastest nor the "
                        "toughest. Most plants in a wood live somewhere in this "
                        "region, tuned by how much light their neighbours leave "
                        "them."},
         }},

        # #s-features — the band panel. NOT on the rail; see the docstring.
        # `r_rule` is the shell Design drew: band ground, 3px ink border, no
        # shadow, an eyebrow, a display statement and a card list.
        {"type": "rule", "anchor": "s-features",
         "eyebrow": "Five features, five jobs",
         "statement": "Nothing in a leaf is there for decoration.",
         "cards": FEATURE_CARDS},

        # Design nests this inside `#s-features`; `r_rule` has no nested slot,
        # so it renders directly under the panel in document order. See "What
        # could not be lifted" 2.
        {"type": "key-fact", "ref": "each-feature-costs-water"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "PLANT-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # `card` ground, because Design's panel is already `band` and band on band
    # is invisible. Amber is reserved for misconceptions (README) and this box
    # takes the accent offset shadow, per MRB-208.
    "key_facts": [
        {"id": "each-feature-costs-water",
         "text": "A leaf is broad to catch light, thin so carbon dioxide can "
                 "reach every cell, packed with chloroplasts near the top "
                 "surface, riddled with air spaces inside, and holed "
                 "underneath so gas can get in. Each of those features costs "
                 "water, and the leaf you find in any habitat is the "
                 "compromise that works there.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second after the first
        # behind an amber-topped divider — `r_confrontation` renders exactly
        # that from `statements[]`, and an authored statement wins over the
        # register. The block asks for no commitment, on Design's page and here,
        # so it is not a rail stop and emits no completion contract. (MRB-220 R1
        # makes `#s-think` a `predict` in B2, C1 and C2 because on THOSE pages
        # it gates a reveal behind a commitment. This page's is static markup,
        # like B1's, B4's and B5's, so it stays a confrontation.)
        #
        # ⚠️ "an object's colour" carries a straight apostrophe, as drawn. See
        # "What could not be lifted" 6.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "PLANT-03",
         "statements": [
             {"quote": "Leaves are green because chlorophyll uses green light.",
              "body": ["It is the exact opposite. You see an object's colour "
                       "because that is the light it sends back to you, so a "
                       "green leaf is a leaf throwing green light away. "
                       "Chlorophyll absorbs strongly in the red and the blue "
                       "and hardly touches the green in the middle, which is "
                       "reflected and reaches your eye. That is why the growing "
                       "lamps in a commercial glasshouse are an odd purple-pink "
                       "rather than white or green: the grower is paying for "
                       "the two colours the plant can actually use and not "
                       "wasting money making the plant look nice. The same "
                       "logic explains an experiment you can look up: pondweed "
                       "under a green filter bubbles far more slowly than under "
                       "a red or blue one, even though the room looks perfectly "
                       "well lit to you. Your eyes are not a light meter for a "
                       "plant."]},
             {"quote": "The bigger the leaf, the better the plant.",
              "body": ["Then the desert would be full of banana plants, and it "
                       "is not — a cactus has done away with leaves altogether "
                       "and photosynthesises in its stem, its spines being "
                       "leaves that gave up the job entirely. Every square "
                       "centimetre of leaf is another square centimetre losing "
                       "water, and in a dry place the leaf that catches the "
                       "most light is the leaf that kills the plant first. Look "
                       "at what actually grows in each habitat and you can read "
                       "the local compromise off the plants: broad thin leaves "
                       "on a forest floor where light is scarce and water is "
                       "not, needles on a pine that must survive a frozen "
                       "winter when liquid water is unavailable, tiny waxy "
                       "leaves on heather in the wind. Better does not exist on "
                       "its own in biology. Better here, in this place, is the "
                       "only version of the word that means anything."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026, AND RUNG 2 IS REPAIRED.
    #   rung 1 (recall): correct 13w against distractors of 12 / 6 / 6. It is
    #                    the longest, but it clears the longest distractor by
    #                    ONE word and by ×1.08 — under both thresholds. Clean,
    #                    and untouched by the ruling.
    #   rung 2 (apply):  correct 18w (unchanged) against 17 / 20 / 18. The
    #                    correct option is no longer the longest at all.
    #                    Before the repair: 18 against 7 / 8 / 13, failing the
    #                    ≥4-word gap by 5.
    #
    # The three replacement distractors and the reasoning are in the docstring
    # under "What was corrected" 2. The correct option, `answer: 1` and all
    # three `feedback` strings are unchanged and byte-identical.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Feature to job",
            "q": "Why are the palisade cells at the top of the leaf rather "
                 "than the bottom?",
            "options": [
                "They hold the chloroplasts, and the light is strongest "
                "nearest the upper surface",
                "They keep the leaf rigid, and the top needs the most support",
                "They are where the stomata are",
                "Water arrives at the top first",
            ],
            "answer": 0,
            "feedback": {
                1: "That is the veins’ job. Palisade cells are working cells, "
                   "not structural ones.",
                2: "Stomata are mostly on the underside, in the shade, where "
                   "less water evaporates from an open hole.",
                3: "Water arrives through the veins, which run right through "
                   "the leaf. Position in the leaf is about the light.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Pondweed under a green filter bubbles far more slowly than "
                 "under a red one, although the room looks bright. Why?",
            "options": [
                # ⊕ MRB-177, 17 Aug 2026. Each distractor now states a WRONG
                # RULE in the correct answer's own shape, with the misconception
                # as the consequence. The beliefs are Design's and did not move,
                # so all three corrections below are unchanged.
                "Green light is weaker than red light, so a plant under a "
                "green filter receives less energy",
                "Chlorophyll reflects green light rather than absorbing it, so "
                "green light delivers almost no energy to the plant",
                "A green filter blocks carbon dioxide as well as light, so the "
                "pondweed runs short of the gas it needs",
                "A leaf is already full of green, so adding more green light "
                "cannot top it up any further",
            ],
            "answer": 1,
            "feedback": {
                0: "The lamp is the same and the filters pass a similar amount "
                   "of light. What differs is which colour, and whether the "
                   "plant can absorb it.",
                2: "A filter changes the light and nothing else. Everything "
                   "else about the tube is unchanged.",
                3: "Colour is not a supply of anything. The leaf looks green "
                   "because green is what it sends back — it cannot use it, so "
                   "it does not keep it.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the thinness",
            "q": "A leaf is typically less than half a millimetre thick. "
                 "Explain why being thin helps, and why simply making a leaf "
                 "thicker would not double the rate of photosynthesis.",
            "field_label": "Your explanation",
            "placeholder": "Being thin means…",
            "success": [
                "Says carbon dioxide has to diffuse from the stomata to the "
                "photosynthesising cells.",
                "Says a short diffusion distance means the gas arrives "
                "quickly, so no cell is starved of it.",
                "Says light is absorbed as it passes through the leaf, so "
                "cells deeper down receive less of it.",
                "Concludes that extra chloroplasts low in a thick leaf would "
                "sit in dim light and receive carbon dioxide slowly, so they "
                "would add little.",
                "Notes that a thicker leaf also costs more tissue to build and "
                "to keep alive — or gives another cost, such as weight or "
                "shading.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Design a leaf for a plant living on the floor of a "
                 "rainforest, where light is very scarce and water is not, and "
                 "a second leaf for a plant on a hot dry hillside. Give three "
                 "features of each and justify them against the two readouts "
                 "on the bench.",
            "field_label": "Your answer",
            "placeholder": "On the forest floor I would make the leaf…",
            "success": [
                "Forest floor: broad or very large surface area, justified by "
                "the scarcity of light.",
                "Forest floor: accepts the high water loss, because water is "
                "plentiful there.",
                "Dry hillside: small surface area, few stomata, or a thick "
                "waxy cuticle — at least two of these.",
                "Dry hillside: says the cost of those features is a lower rate "
                "of photosynthesis, and that the plant therefore grows slowly.",
                "States explicitly that neither leaf is better in general — "
                "each is the compromise that suits its habitat.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Leaves are broad and flat to intercept light, thin so gases "
                "diffuse quickly to every cell, and have their "
                "chloroplast-packed palisade cells near the upper surface "
                "where the light is strongest. Air spaces inside carry carbon "
                "dioxide to those cells, veins deliver water and carry sugars "
                "away, and a waxy cuticle limits water loss. Chlorophyll "
                "absorbs red and blue light and reflects green.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES-B7 flag 10. The paragraph's real subject is not autumn colour — it
    # is that the whole lesson runs backwards as well as forwards: the same
    # compromise, read at the moment a tree decides the leaf no longer pays.
    "stretch": [
        {"type": "explainer", "id": "autumn-is-the-same-fact",
         "text": "Autumn is the same fact seen from the other side. The yellows "
                 "and oranges in a beech wood in October were in the leaf all "
                 "summer, masked by so much chlorophyll that you could not see "
                 "them. As the days shorten the tree dismantles its chlorophyll "
                 "and withdraws the useful atoms into the twigs — nitrogen and "
                 "magnesium are expensive and worth recovering — and the "
                 "pigments left behind are the ones that were always there. "
                 "Then the leaf is dropped, because a broad thin leaf is a "
                 "liability in a winter when the water in the soil is frozen "
                 "and unavailable: the tree would go on losing water through "
                 "stomata it could not replace. An evergreen makes the opposite "
                 "bet, with small tough waxy needles that lose little enough to "
                 "keep through the winter and photosynthesise on mild days."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own flagship, which is a real destination
    # on the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to test a leaf design against a habitat?",
              "cta": "Ask about this lesson",
              "anchor": "s-tuner"},

    # ⊕ MRB-228's `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph here and nothing in it is a safety instruction — it
    # is a statement about how far the tuner's numbers can be trusted, which is
    # exactly what the convention slot exists for. Routing it through
    # `safety_note` would print it in the treatment reserved for "never light a
    # candle without an adult", which devalues the safety line.
    #
    # ⚑ THIS LINE IS LOAD-BEARING, not decoration. It is the only place the page
    # tells a student that the percentages are invented teaching values, and
    # NOTES-B7 flag 9 turns on it. It is lifted whole.
    "convention_note": "The tuner is a teaching model, not a measurement. Rate "
                       "and water loss are shown as percentages of a healthy "
                       "oak leaf in bright summer conditions, with temperature, "
                       "wind and root supply held constant; real leaves also "
                       "trade against wind damage, herbivores, shading by their "
                       "neighbours and the cost of building the tissue. The "
                       "habitat verdicts are illustrative.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The tuner is a model with two competing readouts and no winning setting,
    # and rung 4 asks the student to justify a design against both — that is
    # analysis and evaluation. The second confrontation's closing claim, that
    # "better" has no meaning without a place, is the attitudes strand.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
