"""B7 L4 — Why almost all life depends on it (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b7/b7-04-why-almost-all-life-depends-on-it.dc.html` (443 lines),
her author's notes `docs/ks3/design-reference/b7/NOTES-B7.md`, and the B7 payload schema
`docs/ks3/b7-inventory/PAYLOAD-SCHEMA.md` §5, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted" and the six ladder
distractors repaired under MRB-177, both of which are itemised below. The six
food chains, the three job cards, the four hook options, both marked rungs and
both self-marked rungs came out of `node tools/extract_design_payload.js`, not
off a keyboard.

── `covers` is the WHOLE bullet, and it is a three-part one ──────────────

`KS3.B.PHOT.02` reads, in full:

    the dependence of almost all life on Earth on the ability of photosynthetic
    organisms, such as plants and algae, to use sunlight in photosynthesis to
    build organic molecules that are an essential energy store and to maintain
    levels of oxygen and carbon dioxide in the atmosphere

Three claims in one sentence — an energy store, oxygen, carbon dioxide — and
`ks3_data/substatements.py` does NOT split it, so this lesson owns it whole and
must discharge all three. It does, and the mapping is one-to-one with Design's
`#s-jobs` cards, which is why that section is not decoration:

    organic molecules as an essential energy store   Job one
    maintaining the level of oxygen                  Job two
    maintaining the level of carbon dioxide          Job three

The "dependence of almost all life" clause is what the flagship is for: six
foods, six chains, one destination. The word *almost* is discharged in the
stretch layer (chemosynthesis), which is the only place in the unit that says
what the hedge in the lesson title is hedging against.

── The flagship: six chains, and two of them are the reason it exists ────

`#s-trace` is `trace-it-back`, on `ks3-block ks3-dark ks3-practical` (page line
104), so `practical` is MEASURED from Design's own markup rather than inherited
from the hook above it — payload schema §0 rule 2, and §4 of the build contract
records that B1 got two of six wrong.

⚖️ **Honey and mushroom do not end where a student expects, and they are not
smoothed into the shape of the other four.** The mushroom's first link says, in
Design's own words, that a fungus is *not a plant* and *cannot photosynthesise
at all* — and its chain then runs back to photosynthesis anyway, through dead
material, arriving at *"Photosynthesis, some time ago"*. That is the "almost"
argued from the plate instead of from the title, and it is what rung 2 tests.
Honey is the other: the bee is a manufacturer that adds no sugar, so the
shortest chemical journey on the plate belongs to the food that looks least
like a leaf. Flattening either into "eat plant, eat animal, done" would delete
the instrument's whole reason for being six foods rather than two.

The chains are deliberately different LENGTHS — bread 3 links, salmon 5 — so
the step count varies and the destination does not, which is the sentence the
prompt makes to the student. Every verdict's step count is Design's and every
one of them checks out against its own chain (`len(chain) - 1`): steak 3,
bread 2, salmon 4, cheese 3, mushroom 3, honey 3.

── FOUR rail stops — Design's fourth restored (MRB-249) ──────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that `#s-jobs`
came off the rail. Design draws FOUR stops and `#s-jobs` ticks on
`s.everArrived` (page line 423) — the INSTRUMENT's predicate, character for
character, one section to the left (page line 422) — and because `#s-jobs` is
an eyebrow, a display statement, three static cards and a key fact, with no
control, no commitment and no field, the reading was that
`ks3_parity.check_rail_reachable` fails a stop whose section carries none of
the completion signals `doneByDom()` reads, that MRB-208 confined the rail to
sections requiring the student to do something, and that inventing a demand
Design did not draw is closed to this build. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. The gate naming the defect was the
gate looking in the wrong place — the tick is computed at rail level, and
that is where mirrors are now resolved, in `wireRail`'s `paint()`.

And Design's `isDone()` states the tick condition. It is a rail-level function
returning the identical expression for `#s-trace` and then for `#s-jobs`. The
three jobs are the payoff of having traced the chain back; the section holds no
control because the instrument already took the student's commitment. That is a
MIRROR.

So the fourth stop is declared: anchor `s-jobs`, `mirrors: "s-trace"`,
`done_when: "chain_traced"` — the instrument's own predicate, named as
borrowed, and gated by `check_rail_matches_design` against
`docs/ks3/rail-manifest.md`. b4-05's `#s-stomata`, b5-06's `#s-designs`,
b4-01's `#s-parts`, b4-03's `#s-built`, c1-02's `#s-matrix`, c1-05's
`#s-scale`, b3-01's `#s-nutrients`, b3-02's `#s-limits`, b3-04's `#s-three` and
b3-07's `#s-four` are restored the same way. The section keeps its anchor, as
it always did — and `PLANT-08` resolves against it exactly as before, because
`elicited_by` needs an emitted `id`, which is independent of the rail.

── What could not be lifted byte-identical, and why ─────────────────────

1. **The three `#s-jobs` card TAGS.** Design's card is four parts — a mono
   accent tag (*Job one*), a display name, a body, and an inset panel starting
   *Without it:* — and the shipped `rule` card is `term` and `gloss`. Tag and
   name are joined with the middle-dot idiom the page itself uses in "At the
   bench · follow it back", and body and inset are joined in Design's order, so
   all four strings survive and none is invented. What is given up is the INSET
   TREATMENT: the *Without it:* sentence renders in the body of the card rather
   than in its own panel. b4-05's four stomata cards and b3-07's four feature
   cards resolved the identical shape the identical way. The fix, if the card
   is to win, is a `tag` key and a `consequence` key on a rule card — an engine
   change this pass does not own.

2. **The key fact leaves Design's band panel.** She nests it inside `#s-jobs`
   (page lines 167–170); `r_rule` has no nested key-fact slot — only
   `r_comparison` does — so it renders as its own top-level block directly
   under the panel, on the band ground every other top-level key fact in the
   key stage takes. The words and the order are unchanged. Same handling as
   b4-05's.

3. **The inline link in the second confrontation, and this one costs a word.**
   Design writes *"Plants also respire continuously, which is
   `<a href="b4-05-stomata-and-gas-exchange-in-plants.html">b4-05's subject</a>`
   and worth having straight before this claim is repeated."* `rich()` allows
   `<em>` and `<strong>` and nothing else, so the hyperlink cannot survive.

   ⚠️ b4-05's precedent — drop the tag, keep the words — does not transfer
   cleanly here, because its link text was a lesson TITLE and this one is a
   lesson CODE. Left as plain text, "b4-05's subject" puts an internal build
   identifier in front of a student, which is meaningless to them and is the
   kind of platform leakage §8.10 exists to stop. So the code is replaced by
   what it stands for, which is the string Design uses for the same
   destination in her own endmatter:

       Design:  which is <a …>b4-05's subject</a> and worth having straight
       Built:   which is the subject of Stomata and gas exchange in plants
                and worth having straight

   Every science word is unchanged. The destination is not lost:
   `stomata-and-gas-exchange-in-plants` is in `references`, which is where the
   engine puts cross-lesson navigation, and Design draws it in "Connects to"
   as well.

4. **`p1-01` moves from "Before this lesson" to "Connects to".** Design draws
   TWO prerequisites — `the-photosynthesis-reaction` and `energy-stores` — and
   `requires` in `build_ks3.py` accepts a plain slug only, looks it up in the
   registry, and **silently skips a slug it cannot find**. P1 is authored and
   held for MRB-223, so `energy-stores` in `requires` would not render as
   pending; it would render as nothing at all, and the link Design drew would
   disappear with no error anywhere. `references` is the field with the
   graceful-pending path — it emits
   `<span class="ks3-pending">Energy stores <em>(Energy transfers — coming
   soon)</em></span>` — so the edge goes there, first in the card, and the link
   survives the wait. The heading it sits under is what is given up; no link
   is. Same resolution b4-05 used for its B7 edge, one unit in the other
   direction.

5. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

6. **The instrument's section heading loses its `<h2>` level.** Design draws
   "Trace a meal to a leaf" as an `<h2>` inside `#s-trace` beside a mono
   counter. It is authored as the instrument's `heading` and the renderer
   decides the tag. No word changes.

── ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026. BOTH MARKED RUNGS FAILED ─

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one):

    AS DESIGN DREW THEM                      AFTER THE REPAIR
    rung 1  correct 15w vs 8 / 7 / 9   ✗     correct 15w vs 16 / 16 / 15   ✓
    rung 2  correct 22w vs 13 / 10 / 8 ✗     correct 22w vs 24 / 19 / 20   ✓

Both tripped the gate on the ≥4-word arm, by 6 and 9 words respectively. A
student could have scored both rungs without reading them.

Mide ruled the CONSTRUCT rather than the instance: on a rule-stating rung the
correct answer states a RULE — subject, condition, consequence — while the
distractors stated one-clause wrong REASONS, so the correct answer was longer
BY CONSTRUCTION. A distractor must state a WRONG RULE instead, in the same
shape, with the misconception as the consequence. Length parity then follows
from the construct rather than from padding.

**The correct option of each rung is unchanged, both `answer` indices are
unchanged, Design's option ORDER is unchanged, and the gate's threshold is
unchanged.** Six distractors were rewritten, each keeping the belief it
already carried and gaining the consequence that belief licenses:

    r1 B  oxygen-as-a-service   + "so its role in a chain is supplying air"
    r1 C  producer = quantity   + "so the word is about quantity rather than food"
    r1 D  producer = top        + "because everything else depends on it"
    r2 A  compost = own food    + "so it needs no producer"
    r2 C  minerals = energy     + "so sunlight never enters its chain"
    r2 D  dead ≠ in the chain   + "what is dead has stopped being part of any chain"

⚖️ **All six of Design's corrections are byte-identical and none needed
moving.** Each already answered the consequence rather than the clause — r1 D's
"It is at the bottom — the base that everything else is standing on" answers
the rewritten option better than the original, because the rewritten option now
concedes the dependence and gets only the direction wrong. That is the sign
the repair was to the construct and not to the science.

⚑ For Mide's science gate — NOTES-B7's own flags landing on THIS lesson, plus
  what was checked against them:

  * flag 16a  **"Roughly half of all photosynthesis happens in the sea."**
              CHECKED AND LEFT. Marine net primary production is a little under
              half of the global total on the standard estimates, and gross
              production splits differ again; "roughly half" sits inside every
              published range and Design's own foot line already says the split
              *"varies between estimates and with the season"*. The hedge is
              honest and it is stated three times consistently — think-again,
              salmon verdict, key note. Nothing changed.

  * flag 16b  **"being the planet's only oxygen supply is not one of them."**
              CHECKED AND LEFT — and this is a valuable correction, not an
              overreach. It is the standard answer to the "the Amazon makes 20%
              of the world's oxygen" claim: a mature forest is close to
              oxygen-neutral, because production and consumption are in balance
              once respiration and decay are counted. Two notes for the gate.
              (i) Design's *"consumes much of what it produces"* UNDERSTATES
              rather than overstates, so the sentence errs safe. (ii) She
              attributes the consumption to *"every one of its cells respires
              day and night"* — at steady state the balancing is done largely
              by decomposers rather than by the trees' own cells. That is a
              simplification, not an error, and it is left as drawn under
              MRB-205. Worth one word from Mide either way.

  * flag 17   **"No oxygen worth mentioning ... for the first two billion
              years"**, and oxygen as a waste product poisonous to most life at
              the time. CHECKED AND LEFT. Earth formed about 4.54 billion years
              ago and the Great Oxidation Event is dated to about 2.4 billion
              years ago, so "the first two billion years" is right and rounds
              downward, which is the safe direction. ⚑ **NOTES-B7 says this
              "forward-references B11". On the approved page it does not** —
              `#s-think`'s only link is to b4-05, and the paragraph names no
              later unit. No B11 edge is authored, because authoring one would
              invent a reference the page does not make. Recorded rather than
              quietly fixed.

  * flag 18   **The chemosynthesis layer: 1977, hydrothermal vents, tube worms,
              energy from chemical reactions rather than light.** CHECKED AND
              LEFT. The Galápagos Rift vent communities were found in 1977, at
              about two and a half kilometres depth, and the giant tube worms
              there do reach two metres. Date, depth and length all hold.

  * flag 19   **Trophic arithmetic — "around ten kilograms of grass for every
              kilogram of cow", and rung 3's criterion that a field feeds far
              more people as wheat than as beef.** AUTHORED AS DRAWN, AND THE
              OWNERSHIP QUESTION IS REPORTED, NOT ANSWERED. The 10:1 is the
              conventional teaching value for one trophic step and it is not
              wrong. What is at issue is §4.6's single-source rule: **B9
              `food-chains-and-food-webs` owns trophic levels**, and this lesson
              states the ratio and its consequence before B9 exists. It is
              stated as an OBSERVATION about one chain rather than taught as a
              rule with a name — no "trophic level", no "10%", no pyramid —
              which is the reference-not-restatement side of the line b4-05 and
              b7-03 already sit on. It is nonetheless the earliest the number
              appears in the key stage, and whether it should is Mide's call.
              If it moves, it moves in two places: the steak chain's third note
              and rung 3's fifth criterion.

  * ⊕ ONE OVERSTATEMENT, CORRECTED 17 Aug 2026 (MRB-245, commander).
    ⛔ Superseded, kept as the record: this entry used to read "ONE
    OVERSTATEMENT, REPORTED AND NOT CORRECTED", and argued that the sentence
    reads as the only BIOLOGICAL route inside a biology unit, making it a
    hedging question for the examiner gate rather than a factual error.

    That reasoning was too generous to the page. Job three said *"Photosynthesis
    is the only large-scale process that removes it"* and the inset repeated it
    as *"the one route out of the atmosphere"*. As written it is false, and not
    marginally: the ocean dissolves carbon dioxide on a scale comparable to the
    entire land biosphere, and silicate weathering is the long-term geological
    sink that sets the planet's thermostat. Neither is biological, and neither
    is small. The card also contradicted ITSELF — it already named *ocean
    sediment* as a destination, which cannot be true if photosynthesis is the
    only route.

    Corrected under the standing rule that where an approved page contradicts a
    matter of fact, the fact wins, and Mide's gate is the check. The edit is the
    narrowest that makes it true — "the only large-scale **biological** process"
    and "the **living world's** one route out" — and the card's teaching point,
    that the living world has exactly one way of taking carbon back out,
    survives it intact.

  * ⚑ TELEOLOGY, REPORTED. The honey chain's third note reads *"A sugar
    solution the plant manufactures deliberately, to pay pollinators for a
    delivery service."* — the strongest purposive wording in the unit, and it
    sits on the same page as the confrontation that says *"Nothing in biology
    is done <em>for</em> another organism's benefit."* The two are reconcilable
    (the nectar buys the PLANT a delivery, which is a cost explained by what it
    returns, not by what it wants) and it is the same economic metaphor b5-06
    lifted whole from Design's nectary card. Lifted unchanged under MRB-205,
    flagged rather than softened.

  * ⚑ ONE SOFT FIGURE. The salmon chain's last link is *"Sunlight on the top
    hundred metres of ocean"*. The euphotic zone is conventionally given as
    about 200 m in clear open ocean, and much shallower in productive coastal
    water; the great majority of marine production does happen in the top
    hundred metres, so the figure is defensible teaching rather than an error,
    and it is not changed. Noted because it is the one number on the page that
    would move if a reviewer wanted the textbook value.

  * flag 12   **No figures, and it is measured.** This page draws no `<img>`,
    no `<figure>` and no placeholder, and its foot line names no slot. §4.10
    allows an empty `figures` for a lesson carried by its interactives. Nothing
    is declared, because declaring a slot the page never references would
    invent a sourcing task in `docs/ks3/diagram-manifest.md`. Flag 12 is not
    dropped — it is Mide's to rule on.

── Keys this pass authors that the ENGINE pass must wire (contract R5) ───

R5 says no key is authored without a read site in the same pass. The renderer
for `trace-it-back` belongs to the engine pass, not to this one, so the read
sites for the instrument's payload are named here explicitly rather than left
to be discovered. Three of these are shapes the payload schema §5 does not
anticipate, because Design's page carries STATE-DEPENDENT labels the schema
lists as single strings:

    head_counter  {"format", "done"}     page line 508  (`traceProgress`)
    steps_label   {"idle", "done"}       page line 514  (`stepsLabel`)
    step_label    str                    page line 531  (`backLabel`, idle)
    done_label    str                    page line 531  (`backLabel`, arrived)

`{n}` in `steps_label.done` is `len(chain) - 1`; `{n}` and `{total}` in
`head_counter.format` are the links revealed and the chain's length.

⚠️ **`close` is NOT authored, and its absence is measured.** Payload schema §5
lists it as *"the closing paragraph after the payoff"*. Design's `#s-trace`
draws no such paragraph — the block ends at the verdict panel (page line 148)
and the next thing on the page is `#s-jobs`. Authoring one would be inventing
student-facing copy under MRB-205 and a key with no drawn source under R5. It
is reported as a schema item with no counterpart on this page rather than
filled.

⚠️ **No runtime state is authored** (payload schema §0 rule 3). NOTES-B7 §1.4
lists `food` and `shown` in its payload sketch; both are values the runtime
owns. `startFood` is likewise not authored — it is Design's editor tweak prop,
its default is `steak`, and `steak` is `foods[0]`, so a renderer that opens on
the first food reproduces it without a key.
"""

# ── the six chains (page lines 313–397, via extract_design_payload.js) ───
#
# Chain order is the order the student walks it: index 0 is the food on the
# plate and the last index is where it came from. The instrument reveals them
# BACKWARDS, one link per press, which is why the notes read as answers to
# "where did that come from?" rather than as a narrative forwards.
#
# ⚖️ Honey and mushroom are the two that do not land where a student expects.
# See the docstring — they are not smoothed into the shape of the other four,
# and the mushroom's first note contradicts the lesson title on purpose before
# its last note resolves it.
FOODS = [
    {"id": "steak", "label": "Steak", "name": "Steak",
     "chain": [
         {"name": "Steak on the plate",
          "note": "Muscle tissue, built from protein the animal assembled."},
         {"name": "The cow",
          "note": "Everything in it was built from what it ate. A cow eats no "
                  "meat at all."},
         # ⚑ NOTES-B7 flag 19. The 10:1 is conventional and B9 owns trophic
         # levels; it is stated here as an observation about one chain, with no
         # name and no rule attached. See the docstring.
         {"name": "Grass",
          "note": "Around ten kilograms of grass for every kilogram of cow — "
                  "most of what the cow eats is respired away to keep the cow "
                  "alive."},
         {"name": "Photosynthesis in the grass leaf",
          "note": "Carbon dioxide from the air, water from the soil, energy "
                  "from sunlight falling on a field."},
     ],
     "verdict": "Three steps from a field to a plate, and every gram of it was "
                "carbon dioxide before the grass got hold of it."},

    {"id": "bread", "label": "Bread", "name": "Bread",
     "chain": [
         {"name": "A slice of bread",
          "note": "Mostly starch, plus the protein that makes the dough "
                  "stretch."},
         {"name": "Wheat grain",
          "note": "A seed — a store of starch the plant packed for its own "
                  "seedling, which we intercept."},
         {"name": "Photosynthesis in the wheat leaf",
          "note": "Glucose made in the leaves, moved to the developing grain "
                  "and stored as starch."},
     ],
     "verdict": "Two steps, the shortest chain on the plate. Eating a producer "
                "directly is the most efficient thing you can do with a "
                "field."},

    {"id": "salmon", "label": "Salmon", "name": "Salmon",
     "chain": [
         {"name": "A salmon fillet",
          "note": "From the sea, and nothing green anywhere near it."},
         {"name": "Small fish and shrimp-like animals",
          "note": "What a salmon hunts."},
         {"name": "Zooplankton",
          "note": "Tiny drifting animals, each a fraction of a millimetre "
                  "across, eaten in enormous numbers."},
         {"name": "Phytoplankton",
          "note": "Microscopic algae drifting in the sunlit surface water. "
                  "They photosynthesise exactly as a leaf does, with "
                  "chlorophyll and the same reaction."},
         # ⚑ "the top hundred metres" is a soft figure — see the docstring.
         {"name": "Sunlight on the top hundred metres of ocean",
          "note": "Below that depth there is not enough light, which is why "
                  "almost all sea life lives in a thin layer at the top."},
     ],
     "verdict": "Four steps, and the producer at the end is invisible. Roughly "
                "half the world’s photosynthesis is done by organisms "
                "like these."},

    {"id": "cheese", "label": "Cheese", "name": "Cheese",
     "chain": [
         {"name": "Cheese",
          "note": "Milk protein and fat, curdled and matured — bacteria do the "
                  "maturing."},
         {"name": "Milk from a cow",
          "note": "Produced from what the cow ate, by an animal that eats only "
                  "plants."},
         {"name": "Grass and silage",
          "note": "Silage is preserved grass, which is how a dairy herd is fed "
                  "in winter."},
         {"name": "Photosynthesis in the grass leaf",
          "note": "The same field as the steak, and the same reaction."},
     ],
     "verdict": "Three steps. The bacteria that ripen the cheese are living on "
                "the same sugars and proteins, one further down the chain "
                "again."},

    # ⚖️ THE CASE THAT LOOKS LIKE A COUNTER-EXAMPLE. Link 0 says a fungus
    # cannot photosynthesise; link 3 says the molecules it lives on were built
    # by photosynthesis anyway. That gap between the two is the instrument, and
    # rung 2 is the same question asked in words.
    {"id": "mushroom", "label": "Mushroom", "name": "Mushroom",
     "chain": [
         {"name": "A mushroom",
          "note": "Not a plant. Fungi have no chlorophyll and cannot "
                  "photosynthesise at all."},
         {"name": "Threads through compost or dead wood",
          "note": "The mushroom is the fruiting body; the organism is a "
                  "network of threads digesting dead material from the outside "
                  "in."},
         {"name": "Dead plant material",
          "note": "Straw, wood, leaf litter — built by a plant that is no "
                  "longer alive."},
         {"name": "Photosynthesis, some time ago",
          "note": "The molecules the fungus is living on were assembled in a "
                  "leaf, possibly years earlier."},
     ],
     "verdict": "Three steps, and it is the case that looks like an exception "
                "and is not. A decomposer is not outside the chain — it is at "
                "the end of it."},

    # ⚑ The honey chain's third note is the unit's strongest purposive wording
    # and it is lifted unchanged under MRB-205. See the docstring.
    {"id": "honey", "label": "Honey", "name": "Honey",
     "chain": [
         {"name": "Honey",
          "note": "Concentrated sugar, and almost nothing else."},
         {"name": "Bees",
          "note": "They collect nectar and evaporate the water off it. They "
                  "add enzymes; they do not add sugar."},
         {"name": "Nectar in a flower",
          "note": "A sugar solution the plant manufactures deliberately, to "
                  "pay pollinators for a delivery service."},
         {"name": "Photosynthesis in the plant",
          "note": "The sugar in nectar is glucose the plant made from carbon "
                  "dioxide."},
     ],
     "verdict": "Three steps, and the shortest chemical journey of the six: "
                "the sugar you taste is close to the sugar the leaf built."},
]

# ── the three jobs (page lines 399–415) ─────────────────────────────────
#
# One card per clause of `KS3.B.PHOT.02`. See the docstring's mapping table —
# dropping any one of these three would leave a third of the statement
# unclaimed while the register still read as covered.
#
# ⚠️ TAG · NAME joined, and BODY + "Without it:" joined. See "What could not be
# lifted" 1. The joiner is the page's own middle dot; all four of Design's
# strings are present and unchanged, and what is lost is the inset panel the
# fourth one renders in.
JOB_CARDS = [
    {"term": "Job one · The way in for energy",
     "gloss": "Energy enters almost every food chain on Earth at one point: a "
              "photosynthetic organism capturing sunlight. Everything above "
              "that is spending what a producer captured. Without it: nothing "
              "above the producers has any source of energy at all, and the "
              "chains empty from the bottom up."},
    {"term": "Job two · The oxygen in the air",
     "gloss": "The atmosphere is about a fifth oxygen and all of it is "
              "biological in origin — released over billions of years as a "
              "waste product of splitting water. Without it: no new oxygen is "
              "added, while every respiring organism keeps consuming what is "
              "there."},
    # ⊕ SCIENCE CORRECTION, MRB-245, 17 Aug 2026. Two words added: "biological"
    # and "living".
    #
    # Design wrote "Photosynthesis is the only large-scale process that removes
    # it" and "the one route out of the atmosphere". As written that is false,
    # and not marginally: the ocean dissolves carbon dioxide on a scale
    # comparable to the whole land biosphere, and silicate weathering is the
    # long-term geological sink that sets the planet's thermostat. Neither is
    # biological and neither is small.
    #
    # The card also contradicted ITSELF — it already names "ocean sediment" as
    # somewhere the carbon ends up, which cannot be true if photosynthesis is
    # the only route.
    #
    # Corrected rather than flagged, under the standing rule that where an
    # approved page contradicts a matter of fact the fact wins. It is the
    # narrowest possible edit: the teaching point of this card is that the
    # LIVING world's only way of taking carbon back out is photosynthesis, and
    # that survives the correction intact. Nothing else on the card moves.
    {"term": "Job three · Taking carbon back out",
     "gloss": "Respiration, decay and burning all put carbon dioxide into the "
              "air. Photosynthesis is the only large-scale biological process "
              "that removes it, locking carbon into wood, roots and ocean "
              "sediment. Without it: carbon dioxide only ever rises, because "
              "the living world's one route out of the atmosphere has been "
              "closed."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 142 character for character.
    "slug":        "why-almost-all-life-depends-on-it",
    "title":       "Why almost all life depends on it",
    "discipline":  "biology",
    "unit":        "photosynthesis",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.PHOT.02` owned WHOLE — three clauses, three job cards, no split in
    # `ks3_data/substatements.py`. See the docstring.
    "covers":      ["KS3.B.PHOT.02"],
    # Named, used, and owned elsewhere. PHOT.01 is b7-01's reaction, which this
    # page assumes throughout and never restates. RESP.01 is B8's, and it is
    # named in the think-again block, in job one and in rung 3's own wording.
    # ECO.01 is B9's, and it is the trophic arithmetic — flag 19, docstring.
    "touches":     ["KS3.B.PHOT.01", "KS3.B.RESP.01", "KS3.B.ECO.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 2},
                    {"id": "cells-and-systems", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's endmatter: "Before this lesson → The photosynthesis reaction,
    # Energy stores"; "Connects to → Fuels and energy resources, Stomata and
    # gas exchange in plants". `energy-stores` moves into the second card
    # because `requires` silently drops an unbuilt slug — "What could not be
    # lifted" 4.
    "requires":    ["the-photosynthesis-reaction"],
    "assumes":     [],
    # Design's document order, with the demoted prerequisite first.
    # `stomata-and-gas-exchange-in-plants` also carries the stripped inline
    # link out of `#s-think` — "What could not be lifted" 3 — and is the lesson
    # that owns `BREATH-12` and `BREATH-13`, which this page cites and does not
    # re-declare.
    "references":  [{"unit": "P1", "lesson": "energy-stores"},
                    {"unit": "P2", "lesson": "fuels-and-energy-resources"},
                    {"unit": "B4",
                     "lesson": "stomata-and-gas-exchange-in-plants"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Trophic levels and biomass transfer, the carbon cycle, and "
                   "the evidence behind human effects on atmospheric carbon "
                   "dioxide.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "One reaction, running in leaves and in water you cannot "
                    "see into, is the doorway through which almost all the "
                    "energy in the living world arrives — and the source of "
                    "every breath you have ever taken.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-jobs` is the third: no control of
    # its own, so it mirrors `s-trace` and ticks on the instrument's predicate
    # — see the docstring. `short` and `label` are Design's own `RAIL_SHORT`
    # and `RAIL` strings (page lines 308–312).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Every meal",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.everArrived` (page line 422). The
        # stop ticks when ONE chain has been walked to its producer, not when
        # a food has been picked — a tab press reveals nothing.
        {"anchor": "s-trace", "short": "TRACE", "label": "Trace it back",
         "done_when": "chain_traced"},
        {"anchor": "s-jobs", "short": "JOBS", "label": "Three jobs",
         "mirrors": "s-trace", "done_when": "chain_traced"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. Option D is the
    # correct one and the reveal says so immediately, which is the point: the
    # hook is not a trick, it is a claim the rest of the page has to earn.
    "phenomenon": {
        "kind": "narrative",
        "title": "Every meal you have ever eaten was once a leaf.",
        "prompt": "A steak is a cow, and a cow is grass. That one is easy. The "
                  "awkward cases are the ones that look nothing like a plant — "
                  "a fish finger, a slice of cheese, a mushroom — and they are "
                  "where the rule is either true or not.",
        "commit": "Which of these did not begin with photosynthesis?",
        "options": [
            "A fish finger, from a fish that ate other fish",
            "A glass of milk",
            "A mushroom, which is not a plant at all",
            "None of them — every one traces back to photosynthesis",
        ],
        "reveal": "All of them did. Every chain runs back to something that "
                  "took in carbon dioxide and built a sugar out of it — grass, "
                  "wheat, or microscopic algae drifting in the sea. The "
                  "mushroom is the interesting one: fungi cannot "
                  "photosynthesise at all, so they feed on material that "
                  "something else built, which puts them further down the same "
                  "chain rather than outside it.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Both ids and both `elicited_by`/`confronted_by` values are the
    # commander's pre-allocation, and both statements are lifted byte-identical
    # from `docs/ks3/misconception-register.md`. `PLANT-12` is this lesson's
    # spare and is deliberately left UNUSED — a permanent gap, like `DRUG-07`
    # and `REPRO-17`/`20`/`21`/`23`. Do not re-point it.
    #
    # ⚠️ `BREATH-12` and `BREATH-13` are NOT re-declared here. `PLANT-08` is
    # deliberately distinct from `BREATH-12` and the line between them is
    # PURPOSE: B4's entry is about the DIRECTION of gas exchange; this one is
    # about oxygen being a WASTE PRODUCT rather than a service. B7 cites b4-05
    # rather than restating it — in the confrontation's own last sentence and
    # in the `references` edge — which is the register's standing rule, "cite,
    # do not re-declare". Opening on a belief and pointing at it is a
    # reappearance, and reappearances live in the register, not in a second
    # `misconceptions` row.
    #
    # Both values resolve against the BUILT page (MRB-244): `s-think` is the
    # confrontation block's anchor and `s-jobs` is the rule block's, and both
    # are emitted as `id="…"`. Whether `s-jobs` is a rail stop is beside the
    # point here — the gate wants an emitted element, not a completion signal.
    "misconceptions": [
        {"id": "PLANT-07",
         "statement": "Plants do the photosynthesising — trees are the lungs "
                      "of the planet.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
        # Elicited by the jobs panel: job two names the oxygen in the air and
        # its inset says what stops if it is removed, which is where a student
        # states the belief to themselves. The panel already calls oxygen a
        # waste product; `#s-think` is where the "for us" half dies.
        {"id": "PLANT-08",
         "statement": "Plants make oxygen for us to breathe.",
         "elicited_by": "s-jobs",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B7, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚑ "chemosynthesis" is included and the call is reported. It is a stretch-
    # layer term, and b4-05 deliberately EXCLUDED "compensation point" on the
    # grounds that Design introduced it as a label rather than as vocabulary.
    # This one is different: it is the only word on the page that explains the
    # "almost" in the lesson's own title, and a student who reads Going further
    # meets it as a named process. NOTES-B7 flag 18 asks Mide whether he wants
    # the hedge explained at all; if the answer is no, this chip goes with it.
    "vocabulary": [
        {"term": "producer",
         "definition": "An organism that builds its own organic molecules from "
                       "simple raw materials, instead of eating something "
                       "else's.",
         "note": "It is at the bottom of a food chain, not the top."},
        {"term": "photosynthetic organism",
         "definition": "Any organism that carries out photosynthesis: plants, "
                       "algae, and some bacteria.",
         "note": "Not only plants. Roughly half of the world's photosynthesis "
                 "happens in the sea."},
        {"term": "phytoplankton",
         "definition": "Microscopic algae drifting in the sunlit surface water "
                       "of seas and lakes.",
         "note": "Each one photosynthesises with chlorophyll, exactly as a "
                 "leaf does."},
        {"term": "organic molecule",
         "definition": "A molecule built around carbon by a living thing — a "
                       "sugar, a starch, a protein, a fat.",
         "note": None},
        {"term": "decomposer",
         "definition": "An organism that feeds on dead material, digesting it "
                       "from the outside and absorbing what is released.",
         "note": "It sits at the end of a food chain, not outside one."},
        {"term": "chemosynthesis",
         "definition": "Building sugars using energy released by chemical "
                       "reactions, instead of energy from light.",
         "note": "Found at deep-sea vents where no light has ever reached."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. This page draws no `<img>`, no `<figure>` and no
    # placeholder, and its foot line names no slot. Declaring one would invent
    # a sourcing task in `docs/ks3/diagram-manifest.md` for artwork the page
    # never references. NOTES-B7 flag 12 is not dropped by this — it is Mide's.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-trace — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b7/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so the segment is MEASURED and not inherited.
        #
        # ⚠️ THIS INSTRUMENT IS ON INK. `.ks3-dark p` is (0,1,1) and beats a
        # bare instrument class at (0,1,0) — the defect that shipped a B4 chain
        # label at 1.21:1 past a green kinds gate. That is the engine pass's
        # problem rather than this module's, and it is recorded here because
        # this payload is what feeds it.
        #
        # Payload keys follow docs/ks3/b7-inventory/PAYLOAD-SCHEMA.md §5, with
        # the four state-dependent labels the schema does not anticipate named
        # in the docstring under "Keys this pass authors".
        {"type": "trace-it-back", "id": "trace-a-meal", "anchor": "s-trace",
         "demand": "investigate",
         "eyebrow": "At the bench · follow it back",
         "heading": "Trace a meal to a leaf",
         "head_counter": {"format": "step {n} of {total}",
                          "done": "chain traced"},
         "prompt": "Pick something off the plate and step backwards through "
                   "the chain that supplied it. Count the steps — and notice "
                   "that the number changes while the destination never does.",

         "options_label": "On the plate",
         "foods": FOODS,

         # `{n}` is `len(chain) - 1`. The idle string is Design's own and is
         # deliberately not a count: before the student presses anything there
         # is no number to show.
         "steps_label": {"idle": "follow it back",
                         "done": "{n} steps back to a producer"},
         "step_label": "Where did that come from?",
         "done_label": "You have reached a producer",
         "reset_label": "Start again"},

        # #s-jobs — the band panel, `rule` with a three-card grid. Rail stop
        # 3, mirroring `s-trace`; see the docstring. One card per clause of
        # KS3.B.PHOT.02.
        {"type": "rule", "anchor": "s-jobs",
         "eyebrow": "Three things it does for everything else",
         "statement": "Food, air, and the balance between them.",
         "cards": JOB_CARDS},

        # Design nests this inside `#s-jobs` (page lines 167–170); `r_rule` has
        # no nested key-fact slot, so it renders directly under the panel in
        # document order. "What could not be lifted" 2.
        {"type": "key-fact", "ref": "photosynthetic-organisms-are-producers"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "PLANT-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # `band` because it is a top-level block here rather than nested; Design's
    # nested box sits on `--ks3-card` only because it is inside a band panel.
    "key_facts": [
        {"id": "photosynthetic-organisms-are-producers",
         "text": "Photosynthetic organisms — plants on land, algae and "
                 "plankton in the sea — are the producers. They build the "
                 "organic molecules that almost every other living thing eats, "
                 "they released the oxygen in the atmosphere, and they take "
                 "carbon dioxide back out of it.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment, on Design's page
        # and here, so it is not a rail stop and emits no completion contract.
        # (Build-contract R1 makes `#s-think` a `predict` in B2, C1 and C2
        # because on THOSE pages it gates a reveal behind a commitment. This
        # page's is static markup, like B1's, B4's and B5's, so it stays a
        # confrontation. Same rule, different block.)
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "PLANT-07",
         "statements": [
             # ⚑ NOTES-B7 flag 16, both halves. Checked and left as drawn; the
             # reasoning is in the docstring. `<em>` survives `rich()`.
             {"quote": "Plants do the photosynthesising — trees are the lungs "
                       "of the planet.",
              "body": ["Roughly half of all photosynthesis on Earth happens in "
                       "the sea, carried out by algae and phytoplankton, most "
                       "of them single cells too small to see without a "
                       "microscope. A drifting organism a hundredth of a "
                       "millimetre across, in numbers no one can count, "
                       "matches every forest and grassland on land put "
                       "together. Rainforests are irreplaceable for a long "
                       "list of reasons, and being the planet's only oxygen "
                       "supply is not one of them — a mature forest also "
                       "consumes much of what it produces, since every one of "
                       "its cells respires day and night. Keep the vocabulary "
                       "honest and this stays clear: the group that matters is "
                       "<em>photosynthetic organisms</em>, which includes "
                       "plants, algae and some bacteria. Restricting the idea "
                       "to green things with roots leaves out half the "
                       "planet's production and most of its producers."]},
             # ⚑ NOTES-B7 flag 17 lives in this paragraph, and the last
             # sentence is the b4-05 citation — the link is stripped and the
             # lesson named instead. "What could not be lifted" 3.
             {"quote": "Plants make oxygen for us to breathe.",
              "body": ["Not for us, and not for anything. Oxygen is a waste "
                       "product: the plant is building glucose, and oxygen is "
                       "what is left over from splitting water to do it. There "
                       "was no oxygen worth mentioning in the atmosphere for "
                       "the first two billion years of Earth's history, and "
                       "the organisms that eventually filled it with the stuff "
                       "were bacteria releasing a gas that was, at the time, "
                       "poisonous to almost everything alive. Breathing "
                       "animals appeared afterwards, in an atmosphere that was "
                       "already there — the sequence runs the other way round "
                       "from the way the sentence implies. Nothing in biology "
                       "is done <em>for</em> another organism's benefit, and a "
                       "plant that gave away useful material on purpose would "
                       "be out-competed by one that did not. Plants also "
                       "respire continuously, which is the subject of Stomata "
                       "and gas exchange in plants and worth having straight "
                       "before this claim is repeated."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026. BOTH marked rungs failed as
    # Design drew them (15w against 9, and 22w against 13) and both are
    # repaired by rewriting distractors into wrong RULES of the same shape.
    # Correct options, `answer` indices, option order and all six corrections
    # are unchanged. Full working, with the before-and-after counts, is in the
    # docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Producers",
            "q": "What does it mean to call a plant a producer?",
            "options": [
                # 15w — Design's, unchanged.
                "It builds its own organic molecules from simple raw "
                "materials, instead of eating something else’s",
                # 16w — `PLANT-08` wearing a rule. Was "It produces oxygen for
                # other organisms to breathe" (8w).
                "It makes the oxygen other organisms breathe, so its role in a "
                "chain is supplying air",
                # 16w — the word-association error, given its consequence. Was
                # "It produces more offspring than it needs" (7w).
                "It produces more offspring than it needs, so the word is "
                "about quantity rather than food",
                # 15w — the inverted position. Was "It is at the top of the
                # food chain" (9w). The new clause CONCEDES the dependence,
                # which is what makes the existing correction land harder.
                "It sits at the top of a food chain, because everything else "
                "depends on it",
            ],
            "answer": 0,
            "feedback": {
                1: "Oxygen is a waste product, and it is not made for anyone. "
                   "Producer is about food, not about air.",
                2: "That is true of most organisms and has nothing to do with "
                   "the term.",
                3: "It is at the bottom — the base that everything else is "
                   "standing on.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A mushroom is not green and cannot photosynthesise. Does it "
                 "depend on photosynthesis?",
            "options": [
                # 24w — was "No — it makes its own food from the compost it
                # grows in" (13w). Design's own "the compost it grows in" is
                # kept inside the rewritten rule.
                "No — an organism that takes its food straight from the "
                "compost it grows in is making its own, so it needs no "
                "producer",
                # 22w — Design's, unchanged.
                "No — a fungus takes its energy from the minerals in the soil, "
                "so sunlight never enters its chain",
                # 19w — was "No — fungi get their energy from the soil
                # minerals" (10w).
                "Yes — it feeds on dead material that a photosynthetic "
                "organism built, so it sits at the end of the same chain",
                # 20w — was "Only if it is growing on a living plant" (8w).
                "Only if it is growing on a living plant — what is dead has "
                "stopped being part of any chain",
            ],
            "answer": 2,
            "feedback": {
                0: "Feeding on something is not making your own food. The "
                   "compost is dead plant material, and a fungus is digesting "
                   "what a plant built.",
                1: "Minerals supply no energy, to a fungus or to anything "
                   "else. That is the same mistake as thinking plants feed on "
                   "soil.",
                3: "Dead or alive makes no difference to where the molecules "
                   "came from. Either way they were assembled by "
                   "photosynthesis.",
            }},
        "explain": {
            "title": "Rung 3 · Follow the energy",
            "q": "Explain how the energy in a beef burger got there, starting "
                 "from the Sun. Use the words producer, photosynthesis, "
                 "glucose and respiration.",
            "field_label": "Your explanation",
            "placeholder": "Light from the Sun fell on…",
            "success": [
                "Says light energy from the Sun was absorbed by chlorophyll in "
                "grass leaves.",
                "Says photosynthesis used that energy to build glucose from "
                "carbon dioxide and water — so the grass is the producer.",
                "Says the energy is now stored chemically in molecules the "
                "plant built.",
                "Says the cow ate the grass and used some of that energy, "
                "storing the rest in its own tissues.",
                # ⚑ NOTES-B7 flag 19. This criterion and the steak chain's
                # third note are the two places the trophic arithmetic appears;
                # if Mide moves it to B9, it moves in both. See the docstring.
                "Says most of what the cow ate was released again by "
                "respiration rather than passed on, which is why a field feeds "
                "far more people as wheat than as beef.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Coal is often described as \"ancient sunlight\". Explain "
                 "what that means, where the carbon in a lump of coal came "
                 "from, and what burning it does to the atmosphere.",
            "field_label": "Your answer",
            "placeholder": "The coal formed from…",
            "success": [
                "Says coal formed from plants that lived and photosynthesised "
                "hundreds of millions of years ago.",
                "Says the carbon in those plants came from carbon dioxide in "
                "the atmosphere of the time.",
                "Says the energy stored chemically in the coal is energy those "
                "plants captured from sunlight.",
                "Says the plant material was buried before it could fully "
                "decay, so the carbon was locked away instead of returning to "
                "the air.",
                "Says burning it returns that carbon dioxide to the atmosphere "
                "— releasing in a moment what was removed over millions of "
                "years, faster than photosynthesis can take it back out.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Photosynthetic organisms are producers: they build organic "
                "molecules from carbon dioxide and water using light, and "
                "everything that cannot do this depends on them, directly or "
                "through a chain. They also released the oxygen in the "
                "atmosphere and continue to take carbon dioxide out of it. "
                "Roughly half of the world's photosynthesis happens in the "
                "sea.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B7 flag 18: 1977, the vents, the tube worms. Checked and left.
    # This paragraph is what discharges the word "almost" in the lesson title,
    # and it is the only place in B7 that names a route by which energy enters
    # a living system without sunlight. `<em>` survives `rich()`.
    #
    # ⚖️ MRB-225 holds: the layer adds a case, retracts nothing above it, and
    # the body's "almost every food chain" is what makes the exception legible.
    "stretch": [
        {"type": "explainer", "id": "the-almost-in-the-title",
         "text": "The word <em>almost</em> in this lesson's title is doing "
                 "real work. Two and a half kilometres down, where no light "
                 "has ever reached, hot water loaded with dissolved chemicals "
                 "pours out of cracks in the sea floor and whole communities "
                 "live around it — tube worms two metres long, crabs, clams. "
                 "At the base of those food chains are bacteria that build "
                 "sugars using energy released from chemical reactions instead "
                 "of energy from light, a process called chemosynthesis. They "
                 "were found in 1977, and they mattered immediately: until "
                 "then, sunlight was assumed to be the only way energy could "
                 "enter a living system. It is a useful thing to know when "
                 "people speculate about life on a moon with a frozen ocean "
                 "and no daylight at all."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own flagship, which is a real
    # destination on the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to trace something that is not on the plate "
                      "above?",
              "cta": "Ask about this lesson",
              "anchor": "s-trace"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph and nothing in it is a safety instruction — it is
    # a note about how far the six chains and the land-and-sea split can be
    # trusted. Routing it through `safety_note` would print it in the treatment
    # reserved for "never light a candle without an adult", which devalues the
    # safety line. b3-05, b3-07, b4-01 and b5-06 resolve the identical foot
    # line the identical way.
    #
    # ⚑ Its second sentence is the honest half of NOTES-B7 flag 16 and is
    # load-bearing: it is the page telling the student that "roughly half" is
    # an estimate, not a measurement.
    "convention_note": "The chains are simplified to one line each: real diets "
                       "are webs, a farmed salmon eats feed made from several "
                       "sources, and a cow's rumen bacteria sit between the "
                       "grass and the cow. The land-and-sea split of global "
                       "photosynthesis is an approximate figure that varies "
                       "between estimates and with the season.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The instrument is inference from evidence run backwards, and both self-
    # marked rungs ask for a causal chain to be built and defended. The stretch
    # layer is about an assumption being overturned by an observation, which is
    # the attitudes strand ("scientific methods and theories develop as earlier
    # explanations are modified to take account of new evidence").
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
