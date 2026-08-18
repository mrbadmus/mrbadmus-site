"""B11 L3 — When the environment changes: extinction (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b11/b11-03-when-the-environment-changes-extinction.dc.html`
(596 lines), her author's notes `docs/ks3/design-reference/b11/NOTES-B11.md` §2
flags 7–11, and the B11 payload schema
`docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md` §0, §1, §4, §6, §7, §8, §9, §11, §12,
§13 and §14, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the five listed under "What could not be lifted". The four species, the
five pressures, all twenty outcome texts, the four risk cards, both marked rungs
and both self-marked rungs came out of the page's own `SPECIES`, `PRESSURES`,
`OUTCOMES`, `RISK_CARDS`, `RUNGS` and `SELF_RUNGS` arrays via
`tools/extract_design_payload.js`, and the page prose out of the delivered
markup. No score, criterion or correction was retyped.

── `covers` is one clause and this lesson owns the whole of it ─────────

`KS3.B.INH.06` reads, in full: *changes in the environment which may leave
individuals within a species, and some entire species, less well adapted to
compete successfully and reproduce, which in turn may lead to extinction*. It is
not sub-split in `ks3_data/substatements.py` — only `INH.05` is, into the a/b
pair b11-01 and b11-02 own — so it is owned whole, and `build_ks3.validate()`
enforces exactly-once ownership across the unit.

── ⚖️ THE TEACHING POINT IS THAT VULNERABILITY IS A PROPERTY, NOT A RANKING ─

From the KEY FACT, which is schema §9 verbatim: **a species becomes extinct when
the environment changes faster than it can adapt, or in ways its existing
variation cannot cope with — and specialists, slow breeders, small ranges and low
genetic variation are what make that likely.** The lesson is built so that the
answer to "why did this one die and that one live?" is never *strength*:

  * the hook's four options put size and strength first and priority third, and
    the reveal endorses neither — it endorses generations and variation;
  * the bench is a MATRIX rather than a league table, so the same species is
    green under one pressure and amber under another, and the panda's
    `predator` cell is a high score whose own text says it explains nothing;
  * the band section names the four properties and nothing else;
  * rung 1's first distractor is *It is small and not very strong*, and its
    correction answers with the brown rat.

⛔ **Nothing in this file marks a species as good or bad.** The bench gives an
outcome and a reason; the only thing on the page that marks correctness is the
ladder (schema §0.7).

── The instrument: a 4 × 5 matrix, and the pairing must never be positional ─

`#s-bench` is `pressure-bench`, on `ks3-block ks3-dark ks3-practical` (page
line 105), so `practical` is MEASURED from Design's own class attribute rather
than inferred from the kind name — schema §0 rule 3, and contract §4 records
that B1 got two of six wrong by inferring it.

⚖️ **`scores` AND `outcomes` ARE MAPS KEYED BY PRESSURE ID, NEVER PARALLEL
ARRAYS** (schema §1, last paragraph). Twenty outcome texts and twenty scores are
joined to their species and their pressure by NAME. A parallel array would still
render a complete, plausible bench after a reorder, with the dormouse's
habitat-loss verdict printed under the panda — which is a science error no gate
could see. Both dimensions carry all five keys; there is no default and no gap.

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0 rule 4). Design's state bag holds
`species`, `pressure` and `seen`, and all three are the runtime's. That includes
the OPENING PAIR: Design opens on `dormouse` × `habitat`, which is the worst
cell on the bench and is deliberately where the lesson starts, and `dormouse` is
`SPECIES[1]` rather than `SPECIES[0]`. Schema §0 rule 4 is explicit that §4
records the opening values as **prose, not as keys**, so the opening selection is
the renderer's to hold and is NOT authored here. ⚑ Reported to the engine pass:
if `r_pressure_bench` defaults to index 0 it will open on the brown rat, and the
page then opens on the one row with no amber cell in it.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page lines 375–380) and her `isDone()` gives `s-risk` the
BENCH's predicate, character for character, one section to the left:

    if (id === 's-bench') return n >= 4;
    if (id === 's-risk') return n >= 4;          // page lines 429–430

`#s-risk` is an eyebrow, a display statement, four static cards and the key fact:
no control, no commitment, no field, no reveal. It is the PAYOFF of the bench
beside it and carries no control precisely because the bench has already taken
the student's commitment. That relationship is a MIRROR, `wireRail`'s `paint()`
resolves it at rail level — which is the level Design computes it at — and
`ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`.

⚠️ Schema §8's struck paragraph — *author three stops and drop the band* — is
REVERSED by the ⊕ block at the head of the same section. Four is what Design drew
and four is what ships. Shipping three fails the build.

⚖️ **FOUR COMBINATIONS IS DESIGN'S OWN THRESHOLD AND IT IS READ TWICE**, once for
the bench and once for the mirror. It is also the point at which a student has
necessarily moved on both axes: `seen` opens seeded with one pair, and reaching
four requires at least one species change and at least one pressure change, so
nobody can tick the stop by pressing one tab four times.

`#s-think` and `#s-keynote` are on no rail, and that is Design's too:
`#s-keynote` asks nothing, and `#s-think` here is static markup — two quotes,
two bodies, no options, no reveal, no button — so it is a `confrontation` and
not contract R1's `predict`. Schema §7, measured on all four B11 pages.

── ⭐ THE FORWARD REFERENCE FROM b9-03, RESOLVED ───────────────────────

`ks3_data/b9/lesson_03_disturbing_a_food_web.py` carries
`{"unit": "B11", "lesson": "when-the-environment-changes-extinction"}` in
`references` — authored as a reference rather than a `requires` precisely so
that it could ship before this lesson existed, since an unknown `requires` target
fails the build while an unbuilt reference renders as a coming-soon line. It has
been rendering as *(Evolution, extinction and biodiversity — coming soon)*.
**This record landing resolves it to a real link, and NOTHING in b9-03 changes.**
The edge is reciprocated here as a `requires`, which is Design's own second
*Before this lesson* card, and `#s-think`'s second body is what makes it real:
it names that lesson by title where Design drew a hyperlink.

── What could not be lifted byte-identical, and why ────────────────────

**1. ⚠️ THE FRACTION IN `#s-think`'s SECOND BODY — NOTES flag 11, and the one
copy change ruled in this unit.** Schema §14 rules it in full. Design asked to
*"soften or attach a figure you are happy to defend"*; the answer is that there
is no defensible fraction here. The number moves enormously with the counting
rule — whether a semi-synthetic derivative counts, whether "inspired by a natural
scaffold" counts, which drug classes are in scope, which window of approvals is
measured — and surveys of newly approved small-molecule drugs land nearer a third
to a half. Two thirds sits at the top of the range. So the proportion comes out
and KIND goes in, with named examples:

    Design:  Two thirds of modern medicines can be traced back to compounds
             found in living organisms, and the ones in a species that dies out
             unstudied are not recoverable.

    Built:   A great many of our medicines began as compounds found in living
             things — aspirin from willow bark, penicillin from a mould, the
             anticancer drug vincristine from the Madagascar periwinkle — and
             the ones in a species that dies out unstudied are not recoverable.

Three examples, all of them true in a way that cannot decay: salicin from willow
bark behind aspirin, penicillin from a *Penicillium* mould, and vincristine from
the Madagascar periwinkle, still used against childhood leukaemia. The periwinkle
is chosen over the Pacific yew because it makes the lesson's own point — a plant
from one of the most extinction-pressed floras on Earth. **A student who
remembers three drugs has the point; a fraction can become wrong, and this one
already is depending on who counts.** The closing clause is Design's, unchanged,
and it is what the whole sentence exists to set up.

⚠️ This edits authored prose in a `#s-think` BODY, which is permitted: MRB-177's
never-edit-a-correction rule applies to LADDER options, and this is not one. The
rest of the block is byte-identical; one sentence moved.

**2. A STRIPPED HYPERLINK in the same body.** Design writes *"as `<a href="b9-03-
disturbing-a-food-web.html">`Disturbing a food web`</a>` showed"*. `rich()` allows
`<em>` and `<strong>` and nothing else, so no hyperlink survives anywhere on a
built page. It costs nothing here, because the link TEXT is already the lesson
title — the b9-02 finding that a POSITIONAL link text ("the next lesson") must be
resolved to a title does not arise. The edge is carried as a `requires`.

**3. `b11-02` in the rat × disease outcome text — a slot code (§8.10).** Design
writes *"…which is natural selection doing exactly what b11-02 described."* A
student cannot resolve a slot code, and printing one is exactly the platform
leakage §8.10 exists to stop:

    Design:  doing exactly what b11-02 described
    Built:   doing exactly what the Natural selection lesson described

The word *lesson* is carried deliberately: without it the sentence reads
"natural selection doing exactly what Natural selection described", which is a
stutter rather than a pointer. The destination is Design's own first *Before this
lesson* card and is carried in `requires`.

**4. `b9-02` in rung 1's fourth correction — the same shape, resolved the same
way**, as b9-02, b8-01 and b7-04 each resolved it:

    Design:  that is b9-02’s cycle
    Built:   that is the cycle in Predator and prey

⚠️ **This destination is NOT carried as an edge, deliberately.** Design draws
exactly two *Connects to* cards and two *Before this lesson* cards; adding
`predator-and-prey` to `references` to justify the pointer would put a fifth
endmatter card on a page she drew with four, which is a design change and not a
repair. The title is resolvable from the unit browse page, which is what a
student actually has. Reported rather than fixed either way.

**5. Rung 2's three distractors — MRB-177.** Worked below.

Everything else stands as delivered, including `A *new* predator` in rung 1's
fourth correction: the asterisks are Design's own and her page prints them
literally, exactly as b5-01's *matures and is released* does, so they are lifted
rather than converted to `<em>`.

── ⊕ MRB-177 LENGTH PARITY — RUNG 2 REPAIRED, RUNG 1 CLEAN ─────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor by
≥4 words or by ≥1.4×.

**Rung 1 is clean as drawn and nothing on it is touched.** Correct 10w against
7 / 9 / 4 — strictly longest, but the gap to the longest distractor is ONE word
and the ratio is 1.11, so it clears both thresholds comfortably. The construct is
why: all four options are short properties of a species in the same grammar,
three of them *It has…* / *It is…*, so there is no rule in the set for a correct
answer to be longer than.

**Rung 2 as Design drew it FAILS the gate**, and it is the construct MRB-177 was
ruled against: the correct answer states a RULE with its evidence attached, while
all three distractors state a bare verdict in one clause.

    correct  17w  "Yes — over 99% of all species that ever lived are extinct,
                   mostly long before humans existed"
    B        11w  "No — species only die out when people damage the environment"
    C        11w  "Yes, and that means current extinctions are nothing to worry
                   about"
    D        11w  "Only for species that were badly adapted in the first place"

    strictly longest, gap 6 and ratio 1.55 → TELL, on both thresholds at once.
    A student who has read nothing can pick it.

The ruling fixes the CONSTRUCT and not the threshold, so **the correct option is
untouched, the `answer` index is untouched and all three corrections are
untouched.** Each distractor gains the same second element the correct option
already has — a reason clause — keeping the belief Design chose, because Design's
correction is what marks it:

    B  belief: extinction only happens because of us — `EVOL-05`
       Design:  No — species only die out when people damage the environment  11w
       Built:   …damage the environment, by hunting or by clearing habitat    17w
       Design's correction — "There have been five mass extinctions in the
       fossil record, and the most famous of them predates humans by sixty-six
       million years." — refutes the *only when people* claim whether or not the
       human causes are enumerated, so it answers the rebuilt option exactly as
       it answered the first.

    C  belief: extinction is natural, therefore the current rate does not matter
       Design:  Yes, and that means current extinctions are nothing to worry
                about                                                         11w
       Built:   …nothing to worry about, since the process would happen anyway 17w
       The added clause IS the unstated inference the correction breaks: "the
       first half is right and the conclusion does not follow… what matters is
       the rate."

    D  belief: only badly adapted species go extinct
       Design:  Only for species that were badly adapted in the first place    11w
       Built:   …in the first place, since a well adapted one survives         17w
       The added clause is answered head-on by Design's own correction —
       "species that go extinct were usually well adapted — to conditions that
       then changed."

    repaired: correct 17w against 17 / 17 / 17 — TIED, not strictly longest ✓

A four-way tie is the cleanest outcome available: a student who counts words
learns nothing in either direction.

── Misconception ids: EVOL-05 and EVOL-06, and EVOL-11 is UNUSED ───────

Schema §12's pre-allocation for b11-03, and the two beliefs Design's `#s-think`
quotes, in her page order. Both statements are her own bytes (page lines 176 and
180), in register voice with the curly quotes stripped — `_quoted()` draws those.

**Two beliefs were found and two ids were used. `EVOL-11`, this lesson's named
spare, is UNCLAIMED and stays permanently unused**, exactly like `DRUG-07`. No
second spare was needed, so there was nothing to stop and report.

⊕ **THE `EVOL` PREFIX ROW IS OPEN, AND IT AGREES WITH THIS FILE.** Schema §11
item 5 recorded that NOTES §4's claim to have written the entries in was false
when measured, so the register was checked rather than assumed: it now carries
the prefix row (line 120) and rows for all eight ids (lines 1037–1044). Its
`EVOL-05` and `EVOL-06` rows match the two authored here on statement, on
`elicited_by` and on `confronted_by`, including the absence below. Nothing to
reconcile, and that file is not this pass's to edit.

**`EVOL-06` declares NO `elicited_by`, and that is measured rather than
forgotten.** *Takes its place* occurs exactly once on this page, inside the
`#s-think` quote itself. The hook asks which species survives a change; rung 1
asks what makes a species vulnerable and rung 2 whether extinction is natural;
the bench has no commit gate at all. Nothing on the page asks a student to state
that belief before it is taken apart. Absence is legal for `elicited_by` under
MRB-248 — `verify_ks3.py` checks only that a value which IS present names an
element on the page — and inventing an anchor to fill the field would fail the
gate it was invented to satisfy. `EVOL-05` does have one: rung 2's option B is
the belief in the student's own words, and the ladder is where it is marked.

NOTES §4 asks `EVOL-06` to carry `disturbing-a-food-web` in `reappears_in`. That
column lives in the REGISTER, not on the lesson record — no `ks3_data` lesson
has ever carried a `reappears_in` key — and the register already records the edge
in prose beneath its table. Checked, not duplicated.

── Keys this pass authors that the RENDERER reads (contract R5) ────────

Named explicitly rather than left to be discovered. Every one is schema §4's
block literal, which is the contract the engine pass is building against:

    species_label /   the two mono labels over the two tab rows
    pressure_label
    progress_suffix   the mono counter in the bench's top-right
    trait_labels      the four mono captions in the trait grid
    species           tabs + the trait grid, each carrying `scores`
    pressures         tabs + the pressure name and note
    outcomes          the twenty texts, keyed [species][pressure]
    outcome_label /   the readout row over the bar, and the unit after the
    outcome_suffix    number in it
    bands             the two thresholds that pick the bar's colour
    eyebrow /         the practical shell's head row
    title / intro

⚠️ `pressure-bench` was NOT yet registered in `ACTIVITY_KIND_RENDERERS` when
this pass ran — the engine agent is mid-flight in `build_ks3.py`. That is
expected and no renderer was added here; the keys above are authored against
schema §4 and their read sites arrive with the instrument.

── figures: [] and MEASURED ───────────────────────────────────────────

`<img>`, `<figure>` and `<picture>` each appear ZERO times on this page —
grepped, not assumed — and every `<svg>` is the nav chevron, a rail tick, a
ladder mark or an endmatter arrow. Schema §13 says the same across all four B11
pages. **The unit's one ruled diagram is the peppered moth pair and it belongs to
b11-02** (schema §14, flag 16); nothing in THIS lesson is spatial. Declaring a
figure slot here would invent a sourcing task in `docs/ks3/diagram-manifest.md`
for a drawing nothing on the page references.

── ⚑ For Mide's science gate — every NOTES-B11 flag landing on THIS lesson ─

Five flags, five checked, **one corrected**. Schema §14 ruled all five on 18 Aug
2026 and none is re-opened here.

  * flag 7   **Over 99% of species extinct, five mass extinctions, end-Permian
             ~90% of marine species, end-Cretaceous 66 Mya.** RULED STANDARD,
             ship as drawn. All four appear in `#s-think`'s first body and in
             rung 2, and they agree with each other across the page.
  * flag 8   **"Tens to hundreds of times the background rate."** RULED: the
             conservative range is the RIGHT choice where published estimates
             run much higher. ⛔ Do not raise it in a later pass. It appears
             twice — the think-again body and rung 2's third correction — and
             both say the same number, which is what makes the page checkable.
  * flag 9   **The four species and their trait descriptions.** RULED accurate,
             ship as drawn, and the dormouse detail — will not cross open
             ground, one small litter, a strict seasonal diet — is doing most of
             the teaching work. It is what rung 3's five criteria are written
             against.
  * flag 10  **Kakapo: flightless, freeze response, breeding tied to mast years,
             a low point of 51.** RULED correct, ship as drawn, and the named
             recovery programme is wanted.
  * flag 11  **"Two thirds of modern medicines."** ⚠️ **CORRECTED** — the one
             copy change ruled in this unit. Before and after are quoted in full
             under "What could not be lifted" 1.

── ⚠️ A MEASURED OVERSTATEMENT IN THE NOTES, AND NO CELL WAS BENT TO FIX IT ─

Schema §11 item 2. NOTES §1.3 says *"Every species is resilient to at least one
pressure and vulnerable to at least one, so no row reads as a simple ranking."*
Measured against the bands the page itself renders (≥65 green, 40–64 muted,
<40 amber): the dormouse and the panda hold the claim, but **the brown rat has
no cell below 65 and the herring gull none below 60, so neither has a single
amber cell.** The rat row IS a simple ranking — it is good at everything.

**The claim is the overstatement; the matrix is right.** No score was lowered and
no cell was added, because the two generalists are on the bench precisely BECAUSE
they shrug almost everything off, and the lesson runs on the dormouse/panda
contrast rather than on a symmetry — rung 3 asks for the rat against the dormouse
by name. Design's sentence is hers to withdraw. Reported, not repaired.

⊕ One consequence, and it was CORRECTED rather than flagged on. Design's bench
intro ended *"and note that no species is robust against everything"* — the same
overstatement one step further in, and this pass lifted it byte-identical and
raised it, which was the correct default. The commander corrected it on 18 Aug
2026: the general claim is true of the world, but "note that" instructs the
student to observe it HERE, and the brown rat's lowest score is 65 and the
herring gull's 60, so neither shows a vulnerability at all. The clause now names
what the bench does demonstrate — that a species can be tough against one
pressure and helpless against another — which is also the lesson's own point.
The scores were NOT touched; bending the evidence to fit the prose is the wrong
repair and the schema says so.

── One number a later pass might read as a contradiction, and should not ─

The big question opens *"More than nine in ten of all the species that have ever
lived are gone"*, and `#s-think` says *"over ninety-nine per cent"*. Both are
true and the second implies the first; the big question is the weaker, safer
statement in the place a student meets first, and the exact figure arrives where
it is argued for. Left exactly as drawn.

── OTHER LAW, checked rather than assumed ─────────────────────────────

**No year and no half-term anywhere in the page's bytes.** `Year 7`…`Year 11`
and `half-term` appear zero times — now gated in `verify_ks3.py`. The lesson
carries a great many years, and every one of them is content: *fifty years*,
*sixty-six million years*, *one small litter a year*, *one cub every two years*,
*two to four years apart*. None names a school year or a point in a scheme of
work.

**§8.10 — no platform self-explanation.** Two slot codes were resolved; see
"What could not be lifted" 3 and 4. Nothing on the page explains the site to the
student.

**Amber is a wrong IDEA, never the student.** The bench paints sub-40 outcomes in
`--ks3-alert`, which is amber doing a second job as a data colour — schema §11
records it as a build-wide observation for the design pass, not a payload key,
and it does not breach §0.7 because nothing on the bench marks the student.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes: *what decides survival is whether existing
variation and the rate of reproduction can keep up with the change*. The hook's
reveal, all twenty outcome texts, the four risk cards, the key fact, rung 2's
correct option and the key note all say it at the same size. *Going further*
adds the kakapo and retracts nothing: every one of that bird's vulnerabilities is
named as a trait that USED TO BE an advantage, which is the lesson's own claim
applied to a species whose environment changed under it.
"""


# ── the four species (page lines 313–345 of the script block) ────────────
#
# Design's order — generalist, specialist, specialist, generalist — and the
# order is the argument: the two rows either side of the middle are the
# comparison rung 3 asks for by name. `dormouse` is SPECIES[1] and is where
# Design's page OPENS; that opening selection is the renderer's (schema §0
# rule 4) and is deliberately not authored here.
#
# ⛔ `scores` IS A MAP KEYED BY PRESSURE ID, NEVER A LIST. All five keys are
# required on every species; there is no default and no gap. See the docstring.
SPECIES = [
    # ⚠️ THE ROW WITH NO AMBER CELL, AND IT IS NOT A DEFECT. Every one of
    # the rat's five scores is 65 or above, so the bench paints it green five
    # times over. Schema §11 item 2 measured the same thing: NOTES §1.3's claim
    # that every species is vulnerable to at least one pressure does not hold
    # here. The claim is the overstatement; the matrix is right, and no cell is
    # bent to rescue the sentence. The generalist that shrugs everything off is
    # WHY the rat is on the bench — rung 3 runs on the contrast with the
    # dormouse, not on a symmetry.
    {"id": "rat",
     "name": "Brown rat",
     "diet": "Anything at all",
     "breeding": "Up to five litters a year",
     "range": "Every continent except Antarctica",
     "variation": "Very high",
     "scores": {"habitat": 85, "climate": 80, "predator": 70,
                "disease": 65, "hunting": 75}},
    # ⚖️ THE SPECIES THE LESSON IS ACTUALLY ABOUT, and the row Design opens
    # on. Three amber cells and one green one: `hunting` at 80 is the pressure
    # it is SAFE from, and its outcome text turns that into the argument —
    # "which is why the population is still falling for the other four
    # reasons". ⛑ NOTES flag 9, checked and left: the three trait lines are
    # accurate and are doing most of the teaching work in the lesson.
    {"id": "dormouse",
     "name": "Hazel dormouse",
     "diet": "Hazelnuts, flowers and insects, in a strict seasonal order",
     "breeding": "One small litter a year",
     "range": "Fragments of southern English woodland",
     "variation": "Low, and falling as populations are cut off",
     "scores": {"habitat": 15, "climate": 30, "predator": 45,
                "disease": 35, "hunting": 80}},
    # ⛑ `predator` = 70 IS DELIBERATELY A HIGH SCORE THAT EXPLAINS NOTHING,
    # and its outcome text says so in terms. Schema §4 is explicit that if a
    # later pass ever tidies this row to read uniformly bleak, the pedagogy is
    # lost: a student has to meet a resilience that is beside the point.
    {"id": "panda",
     "name": "Giant panda",
     "diet": "Bamboo, almost exclusively",
     "breeding": "One cub every two years at best",
     "range": "Mountain forest in central China",
     "variation": "Low",
     "scores": {"habitat": 20, "climate": 25, "predator": 70,
                "disease": 40, "hunting": 35}},
    # The second row with no amber cell — disease at 60 is muted, not
    # vulnerable. See the rat's note; same measurement, same answer.
    {"id": "gull",
     "name": "Herring gull",
     "diet": "Fish, waste, chips, almost anything",
     "breeding": "A clutch a year, long-lived",
     "range": "Coasts and increasingly towns across the northern hemisphere",
     "variation": "High",
     "scores": {"habitat": 80, "climate": 70, "predator": 75,
                "disease": 60, "hunting": 65}},
]

# ── the five pressures (the script block's `PRESSURES`) ──────────────────
#
# `label` is the tab; `name` is the sentence that heads the panel; `note` is
# the line underneath it that says what the pressure DOES. The five are the causes
# of extinction a KS3 student can name, and `hunting` is last and deliberately
# so — its note is the only one that ends on a decision.
PRESSURES = [
    {"id": "habitat", "label": "Habitat loss",
     "name": "Half the habitat is cleared",
     "note": "The commonest cause of extinction today. What remains is also "
             "broken into fragments that populations cannot move between."},
    {"id": "climate", "label": "Climate shift",
     "name": "The climate warms by two degrees",
     "note": "Seasons shift, so food appears earlier or later than the "
             "species expects, and the suitable zone moves — usually "
             "polewards or uphill."},
    {"id": "predator", "label": "A new predator",
     "name": "A predator arrives that was never here before",
     "note": "Introduced by people, usually. The local species has no evolved "
             "defence against it, because nothing like it has ever hunted "
             "them."},
    {"id": "disease", "label": "A new disease",
     "name": "A disease sweeps through",
     "note": "Survival depends on whether anyone in the population happens to "
             "carry resistance — which is a question about genetic variation, "
             "not about strength."},
    {"id": "hunting", "label": "Hunting",
     "name": "The species is hunted or collected",
     "note": "Direct removal by people, for food, for trade or as a pest. The "
             "only pressure on this bench that can be switched off by a "
             "decision."},
]

# ── the twenty outcome texts (the script block's `OUTCOMES`) ─────────────
#
# ⚠️ TWENTY INDIVIDUALLY WRITTEN TEXTS, keyed [species][pressure]. Nothing here
# is generated, concatenated or templated, and schema §4 is explicit that a
# paraphrase of any one of them is a science edit made by accident. All twenty
# are lifted byte-identical except the one slot code in `rat` × `disease` —
# "What could not be lifted" 3.
#
# ⛑ `panda` × `predator` is the cell that exists to explain nothing, and it
# says so: "This is the one pressure it handles well, and it explains nothing about
# why the species is in trouble." `dormouse` × `hunting` does the same job
# in the other direction. Neither is a stray high score to be tidied away.
OUTCOMES = {
    "rat": {
        "habitat": "Rats eat anything and live anywhere, including places "
                   "people build. Half the woodland gone is barely an "
                   "inconvenience — they move into the other half and into "
                   "the town beside it.",
        "climate": "A generalist with a huge range simply shifts. There is "
                   "nowhere it currently lives that it could not leave.",
        "predator": "High numbers, fast breeding and no fussiness. A new "
                    "predator takes a lot of rats and the population replaces "
                    "them within a season.",
        "disease": "A large, varied population almost certainly contains "
                   "resistant individuals. Numbers crash and then recover "
                   "from the survivors — which is natural selection doing "
                   "exactly what the Natural selection lesson described.",
        "hunting": "People have been trying to eliminate rats for centuries "
                   "with poison, traps and dogs, and have never managed it "
                   "anywhere they have not first eliminated the food and "
                   "shelter.",
    },
    "dormouse": {
        "habitat": "The worst case on the bench. Dormice will not cross open "
                   "ground, so clearing half the wood does not halve the "
                   "population — it strands the remainder in fragments too "
                   "small to be viable, each one slowly losing variation.",
        "climate": "A warmer winter interrupts hibernation, which burns fat "
                   "reserves the animal cannot replace, and shifting seasons "
                   "break the strict order of foods it depends on.",
        "predator": "Nocturnal and arboreal, so it avoids some new predators "
                    "— but with one litter a year it replaces losses very "
                    "slowly.",
        "disease": "Small, isolated populations with low variation are "
                   "unlikely to contain resistant individuals, and there is "
                   "no route for survivors to recolonise from elsewhere.",
        "hunting": "Not hunted, and legally protected. This is the one "
                   "pressure it is safe from — which is why the population is "
                   "still falling for the other four reasons.",
    },
    "panda": {
        "habitat": "Bamboo forest cleared for farmland and roads, and pandas "
                   "will not cross the gaps. The remaining populations are "
                   "isolated from each other, which is a genetic problem as "
                   "well as a spatial one.",
        "climate": "Bamboo is slow to move and much of the suitable zone "
                   "would shift uphill beyond where the mountains stop. A "
                   "specialist can only follow its food if the food can move.",
        "predator": "A large adult panda has essentially no natural "
                    "predators. This is the one pressure it handles well, and "
                    "it explains nothing about why the species is in trouble.",
        "disease": "Low genetic variation across a small isolated population "
                   "is the textbook setup for a disease outbreak with no "
                   "resistant survivors.",
        "hunting": "Hunting was a serious historical cause and is now heavily "
                   "suppressed by protection — an example of the one pressure "
                   "a decision can actually remove.",
    },
    "gull": {
        "habitat": "Gulls have responded to habitat loss by moving into "
                   "towns, where the food is abundant and the roofs make "
                   "excellent cliffs. Generalists convert a problem into an "
                   "opportunity.",
        "climate": "A wide range and a varied diet mean a warming climate "
                   "shifts where they are rather than whether they are.",
        "predator": "Large, aggressive, colonial and quite capable of driving "
                    "off most things. Not a species that struggles with "
                    "predators.",
        "disease": "Dense colonies spread disease efficiently, which pulls "
                   "the score down — but the population is large and varied "
                   "enough to contain resistance.",
        "hunting": "Legally protected in the UK and widely disliked; culls "
                   "are local and the population is not limited by them.",
    },
}

# ── the four risk cards in the band section ──────────────────────────────
#
# `kind` is Design's mono accent tag — "Risk factor one" … "Risk factor four" —
# and it maps to `role`, which is the slot `_rule_card()` reads for it. The four
# ARE the key fact, laid out, and their ORDER is Design's: the least visible one
# is last and its body says so.
#
# ⚖️ There is no `examples` line on any of the four. Design draws three elements
# per card — tag, name, body — and the mono example slot b10-01's cards use is
# simply not on this page. An authored empty string would ship an empty <li>.
RISK_CARDS = [
    {"role": "Risk factor one",
     "name": "Specialist diet or habitat",
     "body": "A species that needs one food or one habitat has nothing to "
             "fall back on when that thing changes. Generalists survive "
             "changes that wipe out specialists in the same place."},
    {"role": "Risk factor two",
     "name": "Slow reproduction",
     "body": "Natural selection works through generations. A species "
             "producing one offspring every two years gets very few attempts "
             "before conditions change again."},
    {"role": "Risk factor three",
     "name": "Small or fragmented range",
     "body": "A species in one valley can be wiped out by one event. "
             "Fragmenting a range also stops populations mixing, so each "
             "fragment loses variation separately."},
    {"role": "Risk factor four",
     "name": "Low genetic variation",
     "body": "The most important and the least visible. Selection can only "
             "work with variation that already exists — a population that has "
             "lost it has nothing to select from."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 173 character for character.
    "slug":        "when-the-environment-changes-extinction",
    "title":       "When the environment changes: extinction",
    "discipline":  "biology",
    "unit":        "evolution-extinction-and-biodiversity",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.INH.06` — environmental change leaving individuals and species less
    # able to compete and reproduce, which may lead to extinction — owned WHOLE.
    # It is not sub-split in `substatements.py`; see the docstring.
    "covers":      ["KS3.B.INH.06"],
    # Named, used, and owned elsewhere. `INH.05b` is b11-02's: this page's hook
    # reveal and the rat's disease outcome both invoke natural selection and
    # neither teaches it. `ECO.03` is B9's — how organisms affect and are
    # affected by their environment — which is what four of the five pressures
    # are, and which b9-03 owns the disturbance half of.
    "touches":     ["KS3.B.INH.05b", "KS3.B.ECO.03"],
    "beyond_statutory": False,
    # `genes-and-evolution` at `secure`: the thread was encountered in B5, and
    # developed in B10 and across B11's first two lessons; here the student uses
    # it to explain an outcome for a species they were not taught, which is what
    # level 3 means. `interdependence` is also at 3 and was secured in B9 — this
    # lesson USES it (habitat fragments, a new predator, a food web that runs on
    # without the missing species) rather than building it.
    "threads":     [{"id": "genes-and-evolution", "level": 3},
                    {"id": "interdependence", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. `disturbing-a-food-web`
    # is the b9-03 edge this lesson RESOLVES (see the docstring) and it is also
    # where `#s-think`'s second body points in words. Both are bare slugs:
    # `requires` resolves across the whole key stage.
    "requires":    ["natural-selection", "disturbing-a-food-web"],
    "assumes":     [],
    # Design's "Connects to" card, in her order.
    #
    # ⚠️ `pollinators-and-food-security` MUST carry its unit. A bare slug in
    # `references` is resolved against the CURRENT unit — unlike `requires` — so
    # the bare form would build a link to a B11 page that does not exist.
    # `biodiversity-and-gene-banks` is b11-04 and is correctly bare.
    "references":  ["biodiversity-and-gene-banks",
                    {"unit": "B9",
                     "lesson": "pollinators-and-food-security"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Causes of extinction, the fossil record as evidence, and "
                   "the biological and economic arguments for maintaining "
                   "biodiversity.",

    # ── framing ─────────────────────────────────────────────────────────────
    # ⚖️ "More than nine in ten" is the weaker of the page's two figures and is
    # deliberate; `#s-think` gives "over ninety-nine per cent" where it is argued
    # for. Both are true and the second implies the first. See the docstring.
    "big_question": "More than nine in ten of all the species that have ever "
                     "lived are gone. Extinction is not a failure of the "
                     "system — it is the system, and the question worth "
                     "asking is what makes a species vulnerable to it.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-risk` is the third: no control of its
    # own, so it mirrors `s-bench` and ticks on the bench's predicate — Design's
    # own `isDone()`, page lines 429–430. `short` and `label` are her
    # `RAIL_SHORT` and `RAIL` strings. Shipping three fails
    # `check_rail_matches_design`; see the docstring.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Same wood",
         "done_when": "committed"},
        # Design's own threshold, kept: four species-pressure combinations seen
        # (page line 429). Sticky by her design and monotonic by ours — `seen` is
        # a map that is only ever added to, and there is no reset to untick it.
        {"anchor": "s-bench", "short": "BENCH", "label": "Who survives",
         "done_when": "four_combinations_seen"},
        # The MIRROR. Design gives it the bench's predicate character for
        # character one line further down, so the stop ticks the moment the
        # bench does and nothing ticks on load.
        {"anchor": "s-risk", "short": "RISK", "label": "Four risks",
         "mirrors": "s-bench",
         "done_when": "four_combinations_seen"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer
    # (schema §6: no option is correct, any choice reveals the same paragraph).
    # B is the one the reveal endorses, and the reveal opens with it word for
    # word.
    #
    # ⚖️ A, C AND D ARE THE THREE WAYS A STUDENT EXPLAINS SURVIVAL WITHOUT
    # REACHING FOR VARIATION — strength, priority, and a rule made by people.
    # A is `EVOL-01`'s shape (b11-01's id, not claimed here); D is the one a
    # student is likeliest to believe because it is nearly true of hunting and
    # not at all true of the other four pressures, which is exactly what the
    # bench then shows them.
    "phenomenon": {
        "kind": "narrative",
        "title": "Two species meet the same change. One survives it.",
        "prompt": "A woodland is cleared to half its size. The wood mice are "
                  "fine within a few years. The dormice, living in the same "
                  "wood, eating from the same trees, do not come back. Both "
                  "faced exactly the same event.",
        "commit": "What is most likely to decide which species survives a "
                  "change?",
        "options": [
            "Which species is larger and stronger",
            "How quickly it can produce generations with variation that suits "
            "the new conditions",
            "Which species was there first",
            "Whether the species is protected by law",
        ],
        "reveal": "How quickly it can produce a new generation with the "
                  "variation the new conditions favour. A wood mouse breeds "
                  "several times a year and eats almost anything; a dormouse "
                  "has one small litter, eats a narrow range of foods and "
                  "will not cross open ground. Natural selection needs "
                  "generations and variation to work with, and the dormouse "
                  "has less of both.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §12's pre-allocation for b11-03, and the two beliefs Design's
    # `#s-think` quotes, in her page order. Both statements are her own bytes in
    # register voice, with the curly quotes stripped — `_quoted()` draws those.
    #
    # ⛔ `EVOL-11` is this lesson's named SPARE and is NOT claimed: two beliefs
    # were found and two ids were used. It stays permanently unused rather than
    # being re-pointed at anything later (schema §12).
    #
    # ⚠️ `EVOL-06` DECLARES NO `elicited_by` AND THAT IS MEASURED, not an
    # omission — nothing on this page asks the student to commit to it before it
    # is taken apart. Absence is legal (MRB-248); an invented anchor would fail
    # the gate. The register's own row records the same absence. See the
    # docstring.
    "misconceptions": [
        {"id": "EVOL-05",
         "statement": "Extinction is unnatural — it only happens because of "
                       "us.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "EVOL-06",
         "statement": "If a species goes extinct, another one just takes its "
                       "place.",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B11, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its exclusion
    # list. Every definition below is authored, not lifted.
    #
    # ⚖️ `specialist` and `generalist` are glossed as a TRADE-OFF rather than as
    # good and bad, because the bench spends four rows making that point and a
    # chip that called a specialist "worse at surviving" would undo it.
    # `biodiversity` is deliberately absent: it is b11-04's chip.
    "vocabulary": [
        {"term": "extinction",
         "definition": "The permanent loss of a species, when the last "
                       "individual of it dies.",
         "note": "There is no coming back from it, which is what makes it "
                 "different from a population crash."},
        {"term": "specialist",
         "definition": "A species that depends on one food, one habitat or one "
                       "narrow set of conditions.",
         "note": "Very good at the thing it does, and with nothing to fall "
                 "back on when that thing changes."},
        {"term": "generalist",
         "definition": "A species that can use many foods and live in many "
                       "places.",
         "note": "Rarely the best at anything, and very hard to get rid of."},
        {"term": "genetic variation",
         "definition": "The differences in genes between individuals in the "
                       "same population.",
         "note": "Selection can only work with variation that is already "
                 "there."},
        {"term": "mass extinction",
         "definition": "An episode in which a very large share of the world's "
                       "species dies out in a short stretch of geological "
                       "time.",
         "note": "Five are recorded in the fossil record; the largest was at "
                 "the end of the Permian."},
        {"term": "background rate",
         "definition": "The slow, steady rate at which species go extinct in "
                       "ordinary times.",
         "note": "The number current rates are compared against, which is what "
                 "makes the comparison checkable."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and every `<svg>` is chrome. Schema §13
    # says the same of all four B11 pages. The unit's one ruled diagram is the
    # peppered moth pair and it belongs to b11-02.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b11/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md §4. The
        # read sites are listed in the docstring; the opening species, the
        # opening pressure and `seen` are deliberately absent and the reason is
        # there too.
        {"type": "pressure-bench", "id": "who-survives-what",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · four species, five pressures",
         "title": "Who survives what",
         # ⚖️ LAST CLAUSE CORRECTED 18 Aug 2026, under this run's science
         # authority. The authoring pass lifted it byte-identical and flagged
         # it, which was right — it is not an author's call.
         #
         # Design wrote "— and note that no species is robust against
         # everything." The general claim is TRUE of the world, and that is
         # what made it easy to leave. The defect is not the claim, it is the
         # word "note": this is an instruction to observe something IN THIS
         # BENCH, and this bench does not show it. The brown rat's lowest score
         # is 65 and the herring gull's is 60; neither has a single cell in the
         # amber band. A student who dutifully applies all five pressures to
         # the rat watches it shrug off every one of them and reads a sentence
         # saying that cannot happen.
         #
         # The repair is NOT to give the rat a vulnerability. Schema §11 item 2
         # says so and it is right: the matrix is measured from Design's page,
         # and bending data to fit prose is the wrong direction — the same
         # reasoning that governs b11-01's `crowded` verdict, corrected in the
         # same pass.
         #
         # So the clause becomes the claim the bench DOES demonstrate, which is
         # also the one the lesson exists to teach: a species can be tough
         # against one pressure and helpless against another. The panda and the
         # dormouse show it on the first two presses. Same sentence shape, same
         # instruction to look, and now there is something there to see.
         "intro": "Each species is described by four things that decide its "
                  "resilience. Apply a pressure and see how it copes — and "
                  "note how a species can be tough against one pressure and "
                  "helpless against another.",

         # The two mono labels over the two tab rows, and the mono counter in
         # the head. Design composes "{n} combination(s) tried"; §1 names the
         # authored word `progress_suffix` and the format is composed by the
         # renderer, so the resting bytes read a real number rather than "{n}".
         "species_label": "The species",
         "pressure_label": "What happens",
         "progress_suffix": "combination(s) tried",

         # The four mono captions over the trait grid, in Design's order, which
         # is also the order of the four risk cards below — diet, breeding,
         # range, variation. That parallel is the section-to-section argument
         # and a reorder would break it silently.
         "trait_labels": ["Diet", "Breeding rate", "Range",
                          "Genetic variation"],

         "species": SPECIES,
         "pressures": PRESSURES,
         "outcomes": OUTCOMES,

         "outcome_label": "Population after fifty years",
         "outcome_suffix": "% of the original population",

         # ⛔ THE TWO THRESHOLDS THAT COLOUR THE BAR, and they are the reason
         # the rat row has no amber cell — 65 is the floor of green and the
         # rat's worst score IS 65. Authored once, read once, and NOT tuned to
         # rescue a sentence in the notes. See the docstring.
         "bands": {"ok": 65, "mid": 40}},

        # #s-risk — the band panel, rail stop 3, mirroring `s-bench`. Design
        # draws eyebrow, statement, four cards, key fact — and NO closing
        # paragraph, so `close` is absent.
        {"type": "rule", "anchor": "s-risk",
         "eyebrow": "What makes a species vulnerable",
         "statement": "Four properties, and the same four every time.",

         "cards": RISK_CARDS,

         # Design nests the key fact inside this section on the CARD ground with
         # the 5px accent offset shadow. `card`, because the section itself is
         # `--ks3-band` and band on band is invisible — the same arrangement and
         # the same reason as b7-01's, b8-01's, b9-01's and b10-01's.
         "key_fact": {"ref": "extinction-is-a-question-of-rate-and-variation",
                      "ground": "card"}},

        {"type": "misconception", "id": "extinction-is-natural-and-permanent",
         "anchor": "s-think", "targets": "EVOL-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-risk on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical and identical to
    # payload schema §9's b11-03 entry.
    #
    # ⚖️ ITS LAST THREE WORDS ARE THE LESSON. "Extinction is permanent" is the
    # sentence `EVOL-06` denies, and no later pass may soften it into "very hard
    # to reverse" — the think-again's closing line about de-extinction projects
    # is written to earn exactly this wording.
    "key_facts": [
        {"id": "extinction-is-a-question-of-rate-and-variation",
         "text": "A species becomes extinct when the environment changes "
                 "faster than it can adapt, or in ways its existing variation "
                 "cannot cope with. Specialists, slow breeders, species with "
                 "small ranges and populations with little genetic variation "
                 "are the most vulnerable. Extinction is permanent.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, no `sc-if`,
        # schema §7), so it is a `confrontation` and not a `predict`, it is not a
        # rail stop, and it emits no completion contract.
        {"id": "extinction-is-natural-and-permanent",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "EVOL-05",
         "statements": [
             # EVOL-05. The `<em>` run on "rate" is kept — `rich()` renders it —
             # because the whole paragraph is built to land on that one word:
             # the argument for acting is not that extinction is unnatural, it
             # is that the rate has changed. ⚖️ Note what the correction does
             # NOT do: it does not let anybody off, and it says so in its own
             # middle sentence.
             {"quote": "Extinction is unnatural — it only happens because of "
                       "us.",
              "body": ["Over ninety-nine per cent of all species that have "
                      "ever existed are extinct, and the overwhelming "
                      "majority died out long before there were any humans. "
                      "There have been five mass extinctions in the fossil "
                      "record; the largest, at the end of the Permian, "
                      "removed something like nine tenths of marine species, "
                      "and the most famous ended the non-bird dinosaurs "
                      "sixty-six million years ago after an asteroid impact. "
                      "Species go extinct in ordinary times too, at a slow "
                      "background rate, simply because environments change. "
                      "None of that lets anybody off. What is different now "
                      "is the <em>rate</em>: current extinction rates are "
                      "estimated at tens to hundreds of times the background "
                      "rate, driven by habitat loss, introduced species, "
                      "hunting and a changing climate. The argument for "
                      "acting is not that extinction is unnatural — it is "
                      "that we have made it happen far faster than it "
                      "otherwise would, which is a claim you can check with "
                      "numbers."],
             },
             # EVOL-06. ⚠️ THIS BODY CARRIES THE ONE COPY CHANGE RULED IN B11 —
             # NOTES flag 11, schema §14. The fraction is out and three named
             # examples are in; before and after are quoted in full in the
             # docstring. The stripped hyperlink to `disturbing-a-food-web` is
             # in the same paragraph and is "What could not be lifted" 2.
             # Everything else here is byte-identical.
             {"quote": "If a species goes extinct, another one just takes its "
                       "place.",
              "body": ["Something usually does move into the space, "
                      "eventually, and eventually is doing a great deal of "
                      "work in that sentence. After each mass extinction the "
                      "recovery of diversity took millions of years — not "
                      "centuries. In the meantime the ecosystem runs without "
                      "whatever the missing species was doing, and as "
                      "Disturbing a food web showed, the effects reach "
                      "species that had no obvious connection to it. There is "
                      "also the matter of what is lost: an extinct species "
                      "takes with it a genetic combination that took millions "
                      "of years to assemble and that nothing else has. A "
                      "great many of our medicines began as compounds found "
                      "in living things — aspirin from willow bark, "
                      "penicillin from a mould, the anticancer drug "
                      "vincristine from the Madagascar periwinkle — and the "
                      "ones in a species that dies out unstudied are not "
                      "recoverable. De-extinction projects exist and are "
                      "technically interesting; none has restored a "
                      "functioning population of a lost species, and none is "
                      "a reason to be relaxed about losing one."],
             },
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN AS DRAWN, RUNG 2 REPAIRED AT THE
    # DISTRACTORS. rung 1 correct 10w against 7 / 9 / 4 (gap 1, ratio 1.11 —
    # clears both thresholds and nothing on it is touched); rung 2 correct 17w
    # against 11 / 11 / 11 as drawn, which fails on BOTH thresholds at once, and
    # 17 against 17 / 17 / 17 as built. No correct option was shortened, no
    # `answer` index moved, no correction edited and no distractor invented — a
    # reason clause was added to each, in the correct option's own shape, and the
    # belief each states is unchanged. Full working in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Read the risk",
            "q": "Which of these makes a species most likely to become "
                  "extinct when its environment changes?",
            # Design's four, UNTOUCHED. All four state a short property of a
            # species in the same grammar, so there is no rule in the set for a
            # correct answer to be longer than.
            #
            #   A  correct — specialist diet AND slow breeding, the two risk
            #      factors that compound
            #   B  the belief the whole lesson is against: extinction is about
            #      strength
            #   C  the safest position on the bench, offered as if it were the
            #      most dangerous
            #   D  a real pressure confused with a NEW one, which is the
            #      distinction the `predator` column is built on
            "options": [
                "It eats only one kind of food and breeds slowly",
                "It is small and not very strong",
                "It has a large population spread over several countries",
                "It has many predators",
            ],
            "answer": 0,
            # All three corrections are Design's. ⚠️ D's carries a resolved slot
            # code — "What could not be lifted" 4 — and its `*new*` asterisks
            # are Design's own and are lifted rather than converted.
            "feedback": {
                1: "Size and strength are neither here nor there. Rats are "
                   "small and among the most resilient animals alive.",
                2: "That is one of the safest positions to be in. A wide "
                   "range means a local disaster is survivable.",
                3: "Species live alongside their predators indefinitely — "
                   "that is the cycle in Predator and prey. A *new* predator "
                   "is a different matter.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Is extinction a natural process?",
            # ⚠️ THE THREE DISTRACTORS ARE REBUILT — MRB-177. The correct option
            # is Design's, byte-identical, at index 0. Each distractor keeps its
            # belief and gains the reason clause the correct option already had,
            # which is what takes the set to a four-way tie at 17 words. Full
            # before-and-after in the docstring.
            #
            #   A  correct: yes, and here is the evidence
            #   B  EVOL-05 — extinction only happens because of us
            #   C  the opposite failure: natural, therefore nothing to worry
            #      about
            #   D  only badly adapted species go extinct
            "options": [
                "Yes — over 99% of all species that ever lived are extinct, "
                "mostly long before humans existed",
                "No — species only die out when people damage the "
                "environment, by hunting or by clearing habitat",
                "Yes, and that means current extinctions are nothing to worry "
                "about, since the process would happen anyway",
                "Only for species that were badly adapted in the first place, "
                "since a well adapted one survives",
            ],
            "answer": 0,
            # All three corrections are Design's, byte-identical. C's is the one
            # that does the lesson's real work: it CONCEDES the first half and
            # then refuses the inference, which is the same move the think-again
            # makes at greater length.
            "feedback": {
                1: "There have been five mass extinctions in the fossil "
                   "record, and the most famous of them predates humans by "
                   "sixty-six million years.",
                2: "The first half is right and the conclusion does not "
                   "follow. What matters is the rate, which is now estimated "
                   "at tens to hundreds of times the background level.",
                3: "Species that go extinct were usually well adapted — to "
                   "conditions that then changed. Being well fitted to one "
                   "environment is what makes a specialist vulnerable.",
            }},
        "explain": {
            # ⚖️ THE RUNG THE BENCH IS BUILT FOR. It names the rat and the
            # dormouse — the two rows the student can compare cell by cell —
            # and holds the EVENT constant so the answer cannot be "the change
            # was worse for one of them". Four risk factors, at least three
            # required, which is Design's own wording.
            "title": "Rung 3 · Explain the difference",
            "q": "A brown rat and a hazel dormouse live in the same wood, "
                  "and half of it is cleared. Explain why the rat population "
                  "recovers and the dormouse population may not, referring to "
                  "at least three of the four risk factors.",
            "field_label": "Your explanation",
            "placeholder": "The rat eats almost anything, so…",
            "success": [
                "Says the rat is a generalist and the dormouse a specialist, "
                "and explains why that matters when habitat changes.",
                "Says the rat breeds several times a year and the dormouse "
                "once, so the rat replaces losses far faster.",
                "Says the dormouse will not cross open ground, so the "
                "remaining wood is fragmented into isolated populations.",
                "Says isolated populations lose genetic variation, leaving "
                "less for selection to act on.",
                "Concludes that the rat population recovers while the "
                "dormouse population may decline to nothing even though the "
                "event was identical.",
            ]},
        "produce": {
            # Three conservation options, one choice, and the criteria mark the
            # REASONING rather than the choice — criterion 2 asks only that the
            # reason is grounded in the risk factors. Criterion 3 is where the
            # lesson's least visible risk factor is cashed out: linking
            # populations addresses genetic variation as well as space.
            "title": "Rung 4 · Take it somewhere new",
            "q": "A conservation team can do one of three things for an "
                  "endangered woodland species: increase the size of the "
                  "reserve, plant hedgerows linking the reserve to another "
                  "population twenty miles away, or start a captive breeding "
                  "programme. Argue for one, using what you know about the "
                  "risk factors, and say what the other two would and would "
                  "not fix.",
            "field_label": "Your answer",
            "placeholder": "The problem I would prioritise is…",
            "success": [
                "Identifies which risk factor each option addresses — range, "
                "fragmentation and genetic variation, or numbers.",
                "Makes a clear choice and gives a reason grounded in the risk "
                "factors rather than in preference.",
                "Recognises that linking populations addresses genetic "
                "variation as well as space, which the other two do not.",
                "Notes a limitation of captive breeding — that it does not "
                "fix the habitat the animals would return to, or that captive "
                "populations lose variation too.",
                "Acknowledges that the options are not equally cheap or "
                "equally quick, and that a real decision involves a "
                "trade-off.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Environments change, and a species survives only if its "
                "existing variation allows some individuals to cope and it "
                "can produce new generations fast enough. Specialists, slow "
                "breeders, small ranges and low genetic variation all raise "
                "the risk. Extinction has happened throughout Earth's "
                "history, including five mass extinctions; what is different "
                "now is how fast it is happening and why.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B11 flag 10 lives here and is RULED CORRECT (schema §14):
    # flightless, freeze response, breeding tied to mast years, a low point of
    # 51, and a named recovery programme is wanted. ⚖️ MRB-225 holds: the layer
    # applies the lesson's own claim to one species and retracts nothing above
    # it. Its argument is that every kakapo vulnerability is a former advantage,
    # which is the risk-factor list read backwards, and its last clause is the
    # honest one — recovery is possible, and here is roughly what it costs.
    "stretch": [
        {"type": "explainer", "id": "the-kakapo-and-what-recovery-costs",
         "text": "Kakapo are large flightless parrots from New Zealand, and "
                 "every one of their vulnerabilities is a feature that used "
                 "to be an advantage. New Zealand had no land mammals, so "
                 "there was nothing to run from: flight was an unnecessary "
                 "expense and the kakapo gave it up, freezing when threatened "
                 "instead — a superb defence against a hunting eagle that "
                 "looks for movement, and a fatal one against a stoat that "
                 "hunts by smell. They breed only in years when a particular "
                 "tree fruits heavily, which can be two to four years apart, "
                 "and lay very few eggs. Every one of those traits was well "
                 "fitted to New Zealand before humans arrived with rats, cats "
                 "and stoats. The population fell to 51 birds. Every living "
                 "kakapo is now individually named, radio-tagged and "
                 "monitored, and the population is slowly climbing — which "
                 "tells you both that recovery is possible and roughly what "
                 "it costs."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work out which pressures a species you know would "
              "survive?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph and nothing in it is a safety instruction — it is a
    # note about which numbers on the bench are real and which are illustrative.
    # Routing it through `safety_note` would print it in the treatment reserved
    # for "never light a candle without an adult".
    #
    # ⚑ NOTES flag 9 lands on its first clause and is ruled accurate. The second
    # clause is MRB-225 performed in the drawing: the fifty-year figures are
    # named as illustrative in front of the student, and the last sentence gives
    # the reason that matters scientifically — real extinctions involve several
    # pressures at once, which is precisely what a one-pressure bench cannot
    # show.
    "convention_note": "The four species are real and their traits are "
                       "accurately described; the fifty-year population "
                       "figures are illustrative outcomes for a single "
                       "pressure applied in isolation, not projections. Real "
                       "extinctions almost always involve several pressures "
                       "at once, which is one reason they are hard to "
                       "predict.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is `interpret observations and data, identifying patterns and
    # using observations to draw conclusions` performed rather than described —
    # twenty outcomes across a matrix the student navigates themselves — and
    # rung 3 marks exactly that. Rung 4 is an evaluation of three options against
    # criteria with a trade-off acknowledged, which is the attitudes strand:
    # evaluating risks, and understanding that a decision is not settled by the
    # science alone. Nothing here is measured by the student, so `measurement`
    # is not claimed.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
