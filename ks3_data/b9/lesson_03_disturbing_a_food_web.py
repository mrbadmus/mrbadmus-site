"""B9 L3 — Disturbing a food web (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b9/b9-03-disturbing-a-food-web.dc.html` (610 lines), her author's
notes `docs/ks3/design-reference/b9/NOTES-B9.md`, and the B9 payload schema
`docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md` §0, §1, §2, §4, §7, §11, §12 and §14,
under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the two listed under "What could not be lifted", both of which are
platform slot codes rather than science words. The eight web lines, the six
species with their eighteen consequence texts and six verdicts, the three rule
cards, both marked rungs and both self-marked rungs came out of the page's own
`WEB_LINES`, `SPECIES`, `RULE_CARDS`, `RUNGS` and `SELF_RUNGS` arrays via
`node tools/extract_design_payload.js`, not off a keyboard.

── `covers` is one clause of a bullet that splits four ways ──────────────

`KS3.B.ECO.01` reads *"the interdependence of organisms in an ecosystem,
including food webs and insect pollinated crops"*, and `ks3_data/substatements.py`
splits it four ways for B9. This lesson owns **(c)**: *"What interdependence
means when a web is disturbed: removing one species reaches further than the
links it feeds along."* The substatement's own minting comment names this page's
bench as the reason the clause is separate from (b) — bees in the web with no
feeding line at all, and removing them still empties it.

`KS3.B.ECO.03` — *organisms affecting and affected by their environment,
including the accumulation of toxic materials* — is `touches`, not `covers`. It
is not split, `verify_ks3.py` gates `covers` for exactly-once ownership, and its
load-bearing clause is the whole of b9-05. This page leans on the first half of
it and teaches none of it.

── The instrument: a wood you take one species out of ───────────────────

`#s-bench` is `remove-a-species`, on `ks3-block ks3-dark ks3-practical` (page
line 104), so `practical` is MEASURED from Design's own class attribute rather
than inferred from the kind name — payload schema §0 rule 2, and contract §4
records that B1 got two of six wrong by inferring it.

⚖️ **THE BEES HAVE NO FEEDING LINE, AND THAT IS THE WHOLE UNIT'S STRONGEST
LINK.** `web_lines` gives them *"Bees pollinate the wildflowers"* — a service,
not a meal — and nothing in the wood eats them. Removing them still empties the
web three rounds later, and their verdict says so out loud: *"The bees are in no
food chain here and their removal still empties the web. Feeding is not the only
kind of dependence."* That sentence is the setup for the next lesson, and it
only works because the web is drawn with the gap in it. A revision that
"tidies" the web by giving the bees a feeding line, or drops them because they
have none, destroys the unit.

⚖️ **THE OAK IS THE ONE REMOVAL WHERE THE WEB DOES NOT REORGANISE.** Every other
verdict describes a redistribution — six species changed, the owls squeezed out,
the effect running from a predator down to the plants. The producer's describes a
loss the web cannot absorb: *"Removing the producer removes the energy itself."*
It is the contrast case, and it is the reason there are six removals rather than
five. NOTES flag 7 asks Mide whether it is worth including; that is his call and
not the port's, and it is carried across as drawn.

⚠️ **EXACTLY THREE ROUNDS PER SPECIES.** Design's `caterpillars` carries a
FOURTH round object at page line 363 — `{ title: '', body: '' }` — which she
filters out at draw time (`sp.rounds.filter(r => r.title)`), so the page never
shows it and her counter still reads "of 3". It is an editing artefact. It is
NOT carried across: `r_remove_a_species` has no filter and refuses an empty
round at build time, and under R5 an empty round is a dead payload entry that
would draw a numbered row with nothing in it and count towards "all three
rounds". Verified in the report by count, not by eye.

⚖️ **`web_lines` IS PROSE, NOT A GRAPH.** Eight sentences of who-eats-whom. No
adjacency structure is authored here and none is drawn on Design's page — the
lines are a `grid` of `<li>`s. NOTES flag 17 says a drawn web *"would improve
b9-01 and b9-03 more than any other illustration in the biology build"* and that
it is **not in the diagram manifest**. `figures` stays empty (§4.10, and see
below); inventing an adjacency payload to feed a diagram nobody has drawn would
be inventing a component, which MRB-205 forbids.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ─────────────────

Design draws four (page lines 313–318) and her `isDone()` gives `s-rules` the
BENCH's predicate, character for character, one section to the left:

    if (id === 's-bench') return s.everDone;
    if (id === 's-rules') return s.everDone;      // page line 449

`#s-rules` is an eyebrow, a display statement, three static cards and a key
fact: no control, no commitment, no field, no reveal. It carries none of the
five DOM signals `doneByDom()` reads, which is why the payload schema's §4
originally told this unit to author three stops and drop it.

That instruction is REVERSED. MRB-205 binds and is not re-argued: Design draws,
we render; the page wins over the engine. A band holding *Effects travel
sideways*, *Alternative routes absorb shocks* and *Effects are delayed* is the
payoff of the bench beside it — it carries no control precisely because the
instrument already took the student's commitment. So the stop is declared with
`mirrors: "s-bench"`, `wireRail`'s `paint()` resolves it at rail level (which is
the level Design resolves it at), and `ks3_parity.check_rail_matches_design`
fails the build against `docs/ks3/rail-manifest.md` if a page ships three.

`short` and `label` are Design's own `RAIL_SHORT` and `RAIL` strings, byte for
byte: HOOK / "The ladybirds", BENCH / "Take one out", RULES / "Three rules",
LADDER / "Mastery ladder".

⚠️ `#s-think` and `#s-keynote` are on NO rail, and that is measured rather than
forgotten — neither is a stop on Design's own page. `#s-think` here is static
markup with two quotes and two bodies and no commitment to make, so contract R1
makes it a `confrontation` and not a `predict`.

── What could not be lifted byte-identical, and why ─────────────────────

Both are platform slot codes. No science word moves in either.

1. **`b9-04` in the bees' third round.** Design writes *"…turns out to hold up
   two vertebrates — which is b9-04's subject."* A student cannot resolve a slot
   code, and printing one is exactly the platform leakage §8.10 exists to stop.
   Resolved to the lesson TITLE, which is how b8-01 and b7-04 resolved the
   identical shape:

       Design:  which is b9-04's subject
       Built:   which is the subject of Pollinators and food security

   The destination is not lost — `pollinators-and-food-security` is carried as a
   real `references` edge, and it is Design's own "Connects to" card.

2. **`B11` in the second confrontation.** Design writes *"Extinction has no undo
   — that is what the word means, and it is `<a href="b11-03-when-the-
   environment-changes-extinction.html">B11's subject</a>`."* `rich()` allows
   `<em>` and `<strong>` and nothing else, so no hyperlink survives anywhere on
   the page. That costs nothing where the link TEXT is already a lesson title;
   here it is a UNIT CODE, so dropping the tag would leave `B11's subject` in
   front of a student:

       Design:  and it is <a …>B11's subject</a>
       Built:   and it is the subject of When the environment changes:
                extinction

   `when-the-environment-changes-extinction` is carried in `references`. NOTES
   §3 calls this a forward link that "does not yet resolve" — it does: the slug
   is in `ks3_data/structure.py` line 172 and an unauthored slot renders an
   honest coming-soon page, which is the structure-first guarantee (§11 decision
   8) and not a broken edge.

⚠️ Nothing else moved. In particular the hook's *"Kill every ladybird in the
wood"*, the caterpillars' *"A pest, from the tree's point of view"* and the
bees' *"They are here for a different reason"* are Design's and are carried as
drawn; each of the three is doing work no softer sentence would do.

── ⚑ For Mide's science gate — the NOTES flags landing on THIS lesson ───

Three flags, three checked, **none corrected**:

  * flag 3   **"A pair of blue tits needs about a hundred caterpillars a day"**
             (NOTES cites b9-01 and b9-03). CHECKED — and on THIS page there is
             no figure to check. Design's caterpillars round 2 reads *"a pair
             needs hundreds of caterpillars a day in spring"*, which is
             unquantified beyond an order of magnitude and is comfortably true:
             published figures for a blue tit pair provisioning a brood run to
             several hundred and often above a thousand caterpillars a day at
             peak. The flag's "usually quoted higher" concern lands on b9-01's
             hundred, not on this page's *hundreds*. Nothing added and nothing
             softened; MRB-225 says a claim shrinks until it is true, and this
             one is already inside its own hedge.

  * flag 7   **The oak wood web** — eight species, six removals, three rounds
             each, and whether the *remove the oak* case is worth including.
             CHECKED AND LEFT WHOLE. Every outcome is a plausible direction
             rather than a prediction and the legal line says exactly that. The
             oak case is the only removal where the web does not reorganise and
             it is what makes the other five mean something — see the ⚖️ note
             above. Whether it stays is Mide's ruling, not the port's, and it is
             carried across so that there is something to rule on.

  * flag 17  **No diagram, and the web is prose.** CHECKED AND LEFT. `<img>`,
             `<figure>` and `<picture>` each appear ZERO times on this page —
             grepped, not assumed — and no foot line names a slot. `figures` is
             empty under §4.10. Declaring one would invent a sourcing task in
             `docs/ks3/diagram-manifest.md` for a drawing nobody has commissioned.
             The flag is not dropped by this; it is now the strongest outstanding
             diagram request in the biology build and it is Mide's.

⚑ **Flag 8 (Yellowstone) is RESOLVED and VERIFIED PRESENT.** The ruling of
16 Aug required the elk-and-willow chain taught and *"the wolves changed the
rivers"* gone. Measured in the delivered bytes: `river`, `rivers` and `meander`
appear **zero times** on this page, and the stretch layer runs wolf → elk
numbers and elk behaviour → willow and aspen → beaver → what lives in the water,
closing on chain versus web. Carried across exactly as delivered. **This page
never mentions a river and nothing in it may introduce one.** NOTES flag 8 also
predicted that the ruling "removes the unit's only outbound link to `b6-03`" —
it did not: `b6-03` survives as Design's own *Connects to* card and is carried
in `references` below.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

The lesson makes one claim five times — *an effect travels along every route out
of a missing species, and the routes that matter are often sideways*. The hook
reveal (blue tits neglecting caterpillars, "a second attack… from a different
direction"), every third round on the bench, rule card one, `#s-think`'s first
paragraph, rung 2's correct option and the key note all say it at the same size.
The stretch layer adds Yellowstone and retracts nothing. The one apparent
counter-example — the oak, where the web empties rather than reorganising — is
stated as a contrast in its own verdict and in rule card two's *alternative
routes*, so it narrows the claim where the claim was already narrow rather than
walking it back.

── ⊕ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS ARE CLEAN ──

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor by
≥4 words or by ≥1.4×:

    rung 1  correct 9w vs 8 / 10 / 8   — not strictly longest      ✓ clean
    rung 2  correct 14w vs 5 / 7 / 12  — gap 2, ratio 1.17         ✓ clean

**No distractor on this page was rewritten, and none needed to be.** That is the
construct, not luck. On rung 1 the correct answer states a RULE — subject,
because-clause, consequence — and all three distractors state wrong rules in the
same three-part shape: *remove the control and the pest gets scarcer*, *fewer
insect species means the tree does better*, *a species nothing eats has no
connections*. On rung 2 the construct is "which of these is X?", which the
MRB-177 ruling explicitly allows a different shape for: the correct answer NAMES
A SPECIES with the route to it, and two distractors name species with their own
route while the third refuses the question. Same subject, same kind of
consequence.

⚖️ **Rung 2's first option is five words and it is still not a length tell.**
"The mice, whose numbers rise" is short because the belief is short — it is
`ECO-05` at its most confident, the effect stopping one step below the removed
species — and Design's correction says so: *"True, and everyone predicts it."*
The gate measures the correct option against the LONGEST distractor (12w), not
the shortest, and it passes with room. Recorded so a later pass does not "fix" a
clean rung by padding a belief students hold in five words.

Each distractor's belief, for the register and for anyone re-reading the rungs:

    rung 1 B  written here — "If a predator was controlling a pest, removing the
              predator makes the pest scarcer." A misreading of the word
              *control* as *sustain*. No register entry supplies it.
    rung 1 C  written here — "Fewer insect species in a wood means the trees do
              better." The all-insects-are-pests rule. No register entry.
    rung 1 D  written here — "A species' connections are only the things that
              eat it." `ECO-05`'s near neighbour and deliberately not filed as
              it: `ECO-05` is about how FAR an effect travels, this one is about
              which links a species has at all. Design's correction names the
              distinction — "What eats a species is only half of its
              connections."
    rung 2 A  `ECO-05` — the effect stops at what is directly below.
    rung 2 C  written here — "Two predators in the same wood must be competitors,
              so removing one helps the other." No register entry supplies it.
    rung 2 D  written here — "A top predator has nothing depending on it, because
              nothing eats it." `ECO-05` upside down, and distinct enough to be
              worth its own sentence: it is a claim about the TOP of a web rather
              than about the reach of an effect.

Only `ECO-05` is minted; the five written beliefs stay here rather than being
minted, because nothing on the page confronts any of them head-on as its own
wrong idea and the register's standing rule is that nothing is registered ahead
of the lesson that needs it.

── Misconception ids: ECO-05 and ECO-06 ─────────────────────────────────

⚠️ **The `ECO` prefix row does not yet exist in
`docs/ks3/misconception-register.md`.** Grepped: no `ECO-*` row is open, and the
only `ECO` mention in the file is the permanent gap. That file is **not this
pass's to edit** (contract §0), so the two statements are authored here in
register voice, byte-identical to Design's quoted beliefs, and are reported for
whoever opens the row.

⛔ **`ECO-12` must never be minted** — the register permanently reserves it
(*"`ECO-12` — is `NOS-04`"*). NOTES-B9 §4's instruction to open the family with
twelve entries is superseded by the register. Nothing in this lesson goes near
it; recorded so a later pass reaching for the next free `ECO` number skips it.

Both values of both keys resolve against the BUILT page (MRB-244 for
`confronted_by`, MRB-248 for `elicited_by`): `s-hook`, `s-bench` and `s-think`
are all emitted as section ids. A rung shorthand would not resolve and is not
used.

⚖️ **`ECO-06`'s `elicited_by` is `s-bench`, and it is the reset button.** The
bench's reset is labelled **"Put it back"** — Design's own words, and the second
confrontation's quote is *"If it goes wrong, you just put the species back."*
Pressing it restores the wood instantly and completely, which is the belief
performed rather than stated. That is a real elicitation and not a stretched
one: the student does the thing, and the paragraph two sections down takes it
apart. It is named as `s-bench` (the section) rather than as the activity id for
no reason beyond both resolving; the section is what a student is looking at.

── Keys this pass authors and where each is read (contract R5) ──────────

    progress {none,mid,all}   `_b9_head` → `_head_counter`, build_ks3.py L15693
    web_label / web_lines     `r_remove_a_species`, the `.ks3-rs-web` panel
    tabs_label / species      the tab row and one hidden panel per removal
    still_here_label          `data-still-label` → `wireRemoveASpecies` L14051
    removed_label             `data-removed-label` → the same, L14052
    step_first_label          `data-first-label`, the button's resting state
    step_label                `data-step-label`, its state after one press
    step_spent_label          `data-spent-label`, its state at round three
    reset_label               the second button, drawn as static text

⚠️ **`still_here_label` and `removed_label` are keys the payload schema did not
anticipate.** §7's sketch has neither, because Design composes the panel's
headline in JavaScript — `sp.label + ' — still in the wood'` and
`sp.label + ' removed'` (page line 494). The engine pass added them and
`r_remove_a_species` raises if either omits `{name}`, so the composition is
authored once here rather than hard-coded in the renderer and the six species
labels stay the single source of their own names. Followed the engine, and the
schema is the thing that was incomplete.

⛔ **NO RUNTIME STATE IS AUTHORED** (payload schema §0 rule 3). Design's state
bag holds `species`, `shown`, `everDone` and `active`; all four are values the
runtime owns, and under R5 a key with no read site fails `ks3_key_audit.py`. The
renderer initialises its own state and opens on the first species, which is
Design's `state.species = 'ladybirds'` and `SPECIES[0]` — so unlike b8-01's
ledger there is no `start` key to author, and its absence is measured rather
than forgotten.
"""

from ._oak_wood import oak_wood


# ── the web (page lines 321–330) ─────────────────────────────────────────
#
# ⚖️ PROSE, NOT A GRAPH. Eight lines, and line 7 is the one the unit turns on:
# the bees are given a SERVICE and no feeding line, and nothing in the wood eats
# them. See the docstring. Line 8's decomposers are likewise fed by everything
# and eaten by nothing, which is what lets the oak's third round land.
WEB_LINES = [
    "Caterpillars and aphids feed on oak leaves and sap",
    "Ladybirds eat aphids, and nothing else",
    "Blue tits eat caterpillars and aphids",
    "Mice eat acorns and seeds from the wildflowers",
    "Owls eat mice",
    "Sparrowhawks eat blue tits, and mice when they must",
    "Bees pollinate the wildflowers",
    "Fungi and bacteria decompose everything that dies",
]

# ── the six removals (page lines 332–385) ────────────────────────────────
#
# Six species × three rounds = eighteen consequence texts, plus six verdicts.
# All twenty-four lifted byte-identical via `tools/extract_design_payload.js`.
#
# ⚠️ `caterpillars` has THREE rounds here and FOUR on Design's page. The fourth
# is `{ title: '', body: '' }`, an editing artefact she filters at draw time;
# `r_remove_a_species` refuses an empty round at build time. See the docstring.
#
# The order is Design's and it is a teaching order: a specialist with one line
# out of it, then a middle-of-the-web generalist, then the top predator, then
# the removal a gardener would actually make, then the species with no feeding
# line at all, and finally the producer — the one the web cannot absorb.
SPECIES = [
    {"id": "ladybirds", "label": "Ladybirds",
     "why": "On a simple diagram they have exactly one line coming out of "
            "them.",
     "rounds": [
         {"title": "Straight away",
          "body": "Nothing is eating aphids except the blue tits, and aphids "
                  "breed extremely fast. Aphid numbers climb steeply within a "
                  "season."},
         {"title": "A season or two later",
          "body": "Blue tits switch towards the easy aphid supply and take "
                  "fewer caterpillars, so caterpillar numbers rise as well. "
                  "The oak is now losing sap to aphids and leaves to "
                  "caterpillars at the same time."},
         {"title": "Further out",
          "body": "A tree under that much pressure grows less and produces "
                  "fewer acorns. Fewer acorns means fewer mice, and fewer mice "
                  "means the owls have a bad year — four steps from an insect "
                  "that never went near an owl."},
     ],
     "verdict": "Six of the eight species changed, and the two that started "
                "the story — ladybirds and aphids — are the least interesting "
                "part of it."},

    {"id": "bluetits", "label": "Blue tits",
     "why": "They sit in the middle of this web, eating two things and being "
            "eaten by one.",
     "rounds": [
         {"title": "Straight away",
          "body": "Both caterpillars and aphids increase, because their main "
                  "bird predator has gone. The oak comes under pressure from "
                  "two directions at once."},
         {"title": "A season or two later",
          "body": "Ladybirds do well on the aphid glut, but they cannot eat "
                  "caterpillars and cannot make up the difference. "
                  "Sparrowhawks have lost their main prey and hunt mice "
                  "instead."},
         {"title": "Further out",
          "body": "Mice are now hunted by both owls and sparrowhawks, so "
                  "mouse numbers fall, and the owls — who eat nothing else — "
                  "are squeezed out by a competitor that arrived because of a "
                  "change three species away."},
     ],
     "verdict": "Every species in the wood except the bees and the decomposers "
                "changed, and the owls suffered most from losing a bird they "
                "never competed with."},

    {"id": "owls", "label": "Owls",
     "why": "A top predator. Nothing eats an owl, so it looks like the safest "
            "species to remove.",
     "rounds": [
         {"title": "Straight away",
          "body": "Mouse numbers rise, held back only by the sparrowhawks, who "
                  "take mice occasionally rather than as a main food."},
         {"title": "A season or two later",
          "body": "More mice means more acorns and wildflower seeds eaten. "
                  "Fewer seeds germinate, and the flowers begin to thin out."},
         # ⚖️ This is rung 2's correct answer, reached at the bench first. The
         # effect has run from the TOP of the web to the BOTTOM and then out to
         # an insect that eats nothing in it.
         {"title": "Further out",
          "body": "Fewer wildflowers means less for the bees, whose numbers "
                  "drop — and the flowers that remain are pollinated less, so "
                  "they set fewer seeds again. Removing the top of the web has "
                  "damaged the bottom of it."},
     ],
     "verdict": "The effect ran from a predator down to the plants and then to "
                "an insect that has nothing to do with either. Top predators "
                "are usually the species whose removal travels furthest."},

    {"id": "caterpillars", "label": "Caterpillars",
     "why": "A pest, from the tree’s point of view. This is the removal a "
            "gardener would choose.",
     "rounds": [
         {"title": "Straight away",
          "body": "The oak loses fewer leaves and grows better for a season. "
                  "So far, exactly what was wanted."},
         # ⚑ NOTES-B9 flag 3 lands here. "Hundreds" is checked and left — see
         # the docstring; the figure the flag doubts is b9-01's hundred.
         {"title": "A season or two later",
          "body": "Blue tits lose the food they raise their chicks on — a pair "
                  "needs hundreds of caterpillars a day in spring — and far "
                  "fewer chicks survive. Blue tit numbers fall sharply."},
         {"title": "Further out",
          "body": "With fewer blue tits, aphids are barely predated and "
                  "increase; the oak is attacked by sap-suckers instead of "
                  "leaf-eaters. Sparrowhawks, short of blue tits, turn to "
                  "mice, and owl numbers fall."},
         # ⚠️ DESIGN'S FOURTH ROUND — `{title: '', body: ''}` — IS NOT HERE.
         # She filters it at draw time; this renderer refuses it at build time.
     ],
     "verdict": "The tree gained one good season and then lost the birds that "
                "were protecting it from something else. Removing a pest is "
                "not the same as solving a problem."},

    # ⚖️ THE SPECIES WITH NO FEEDING LINE. Nothing eats the bees and the bees
    # eat nothing here; their only connection to the web is a service. Removing
    # them empties it anyway. This is b9-04's setup and the unit's strongest
    # link — see the docstring.
    {"id": "bees", "label": "Bees",
     "why": "They eat nothing in this web and nothing in it eats them. They "
            "are here for a different reason.",
     "rounds": [
         {"title": "Straight away",
          "body": "The wildflowers are not pollinated, so they set almost no "
                  "seed. Nothing looks wrong for a year, because the plants "
                  "are already grown."},
         {"title": "A season or two later",
          "body": "The next generation of wildflowers barely appears. Ground "
                  "cover thins, and the seeds mice depend on become scarce."},
         # ⚠️ `b9-04` RESOLVED TO ITS LESSON TITLE — "What could not be lifted"
         # 1. The destination survives as a `references` edge and as Design's
         # own "Connects to" card. Nothing else in the sentence moves.
         {"title": "Further out",
          "body": "Mouse numbers fall, and the owls with them. An insect "
                  "connected to this web only by a service, not by a feeding "
                  "line, turns out to hold up two vertebrates — which is the "
                  "subject of Pollinators and food security."},
     ],
     "verdict": "The bees are in no food chain here and their removal still "
                "empties the web. Feeding is not the only kind of dependence."},

    # ⚖️ THE CONTRAST CASE. Every other verdict describes a redistribution;
    # this one describes a loss the web cannot absorb. NOTES flag 7 asks
    # whether it stays — that is Mide's, and it is carried across so there is
    # something to rule on.
    {"id": "oak", "label": "The oak",
     "why": "The producer. Everything else here ultimately runs on it.",
     "rounds": [
         {"title": "Straight away",
          "body": "Caterpillars and aphids have nothing to eat and collapse. "
                  "Acorns stop, so the mice lose their main winter food."},
         {"title": "A season or two later",
          "body": "Blue tits and ladybirds lose their prey; owls lose the "
                  "mice. Every consumer in the wood is now short of food, and "
                  "there is no alternative producer at this scale."},
         {"title": "Further out",
          "body": "The decomposers have a brief glut of dead wood and leaf "
                  "litter and then nothing arriving. Without a producer the "
                  "web does not reorganise — it empties."},
     ],
     "verdict": "Every other removal redistributed the energy in the wood. "
                "Removing the producer removes the energy itself, which is the "
                "one loss a web cannot absorb."},
]

# ── the three rule cards (page lines 387–391) ────────────────────────────
#
# Design's `kind` is the mono accent tag and maps to `role`, which is the slot
# `_rule_card()` reads for it; `name` and `body` map one to one. All three
# strings per card survive unchanged and nothing is joined, dropped or
# invented — this is the repair `_rule_card` took under MRB-245 after b7-01's
# four part cards shipped as empty `<li>`s.
#
# ⚖️ Card two is where the oak's verdict gets its general form: a web with many
# alternative routes absorbs a loss, and one with few does not. Card three is
# the one a student is least likely to arrive at on their own and the reason
# the bench's rounds are named for seasons rather than numbered steps.
RULE_CARDS = [
    {"role": "Rule one", "name": "Effects travel sideways",
     "body": "Not only up and down the chain. The species that suffers most is "
             "often a competitor, or something that shared a predator, rather "
             "than anything the removed species touched."},
    {"role": "Rule two", "name": "Alternative routes absorb shocks",
     "body": "A predator that eats six things barely notices losing one. A "
             "specialist that eats one thing does not survive losing it. Which "
             "is why webs with more connections are steadier."},
    {"role": "Rule three", "name": "Effects are delayed",
     "body": "Populations take seasons or years to respond, so the damage from "
             "a removal often appears long after anyone is still watching for "
             "it."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 156 character for character.
    "slug":        "disturbing-a-food-web",
    "title":       "Disturbing a food web",
    "discipline":  "biology",
    "unit":        "ecosystems-and-interdependence",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.ECO.01c` — what interdependence means when a web is disturbed.
    # Owned whole and discharged by `#s-bench` and `#s-rules`. See the
    # docstring; the substatement's own minting comment names this bench.
    "covers":      ["KS3.B.ECO.01c"],
    # Named, leaned on, owned elsewhere. ECO.03's toxic-accumulation clause is
    # b9-05's and this page teaches none of it; ECO.01's parent is split four
    # ways and (a) is b9-01's, which this lesson assumes throughout and never
    # restates — the 10:1 figure in particular is b9-01's to teach for the
    # whole key stage and appears nowhere here.
    "touches":     ["KS3.B.ECO.03", "KS3.B.ECO.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "interdependence", "level": 3},
                    {"id": "energy", "level": 2}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. Both are B9 and both
    # build.
    "requires":    ["food-chains-and-food-webs", "predator-and-prey"],
    "assumes":     [],
    # Design's "Connects to" card is the first two, in her order. The third is
    # the destination of the stripped link in `#s-think` — see "What could not
    # be lifted" 2. `pollinators-and-food-security` is also where the bees'
    # third round now points in words.
    "references":  ["pollinators-and-food-security",
                    {"unit": "B6", "lesson": "substance-misuse-and-decisions"},
                    {"unit": "B11",
                     "lesson": "when-the-environment-changes-extinction"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Trophic cascades, keystone species, and the effect of "
                   "biodiversity on the stability of an ecosystem.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Pull one thread out of a web and the whole thing moves. "
                    "The species that end up in trouble are usually not the "
                    "ones anybody was thinking about.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 313–318). `s-rules` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate. See the docstring, which also supersedes payload
    # schema §4's three-stop instruction. `short` and `label` are Design's own
    # `RAIL_SHORT` and `RAIL` strings.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "The ladybirds",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.everDone` (page line 448) — one
        # removal followed all the way to round three. Switching species
        # restarts the count and does NOT untick it, which is why the flag is
        # sticky in her code and in ours.
        {"anchor": "s-bench", "short": "BENCH", "label": "Take one out",
         "done_when": "removal_followed"},
        {"anchor": "s-rules", "short": "RULES", "label": "Three rules",
         "mirrors": "s-bench", "done_when": "removal_followed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. C is the one the
    # reveal bears out, and it says so at once; the hook is not a trick, it is
    # the claim the bench then has to earn one removal at a time.
    #
    # ⚖️ Option A is `ECO-05` in the student's own words — ladybirds and oaks
    # are not connected, so the effect cannot travel — which is why the
    # misconception below names `s-hook` as its `elicited_by`. Option D is the
    # same belief hedged: the effect travels, but so slowly it does not count.
    "phenomenon": {
        "kind": "narrative",
        "title": "Kill every ladybird in the wood. What happens to the oak "
                 "tree?",
        "prompt": "A ladybird has never touched an oak leaf, and an oak tree "
                  "has no opinion about ladybirds. There are three organisms "
                  "in between them. The question is whether an effect can "
                  "travel that far.",
        "commit": "What is your prediction?",
        "options": [
            "Nothing — ladybirds and oaks are not connected",
            "The oak does better, with one fewer insect in the wood",
            "The oak does worse, and from two directions at once",
            "The oak is affected, but only after twenty years",
        ],
        "reveal": "It reaches the oak. No ladybirds means aphids multiply; "
                  "aphids drain sap from the young shoots and the tree grows "
                  "less. Along the way the blue tits get an easy meal of "
                  "aphids and neglect the caterpillars, so caterpillar numbers "
                  "rise as well — a second attack on the same tree, arriving "
                  "from a different direction. Effects in a web do not stop at "
                  "the organisms you would have drawn a line to.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # The commander's pre-allocation, payload schema §14. Both statements are
    # Design's own quoted beliefs, byte-identical from page lines 181 and 185,
    # in register voice.
    #
    # ⚠️ The `ECO` prefix row is NOT yet open in
    # `docs/ks3/misconception-register.md` — see the docstring. That file is
    # not this pass's to edit; the two entries below are what belongs in it.
    # ⛔ `ECO-12` is a permanent gap and must never be minted: it is `NOS-04`.
    #
    # All four values resolve against the BUILT page (MRB-244 / MRB-248):
    # `s-hook`, `s-bench` and `s-think` are all emitted section ids.
    "misconceptions": [
        # Elicited by the hook: option A is this belief word for word, and the
        # student commits to it or declines to before the page names it.
        # Confronted in `#s-think`, whose first paragraph walks the blue-tit
        # removal out three species sideways.
        {"id": "ECO-05",
         "statement": "Removing a species only affects the things directly "
                      "above and below it.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        # ⚖️ Elicited by the BENCH, and specifically by its reset button, which
        # is labelled "Put it back" — the belief performed rather than stated.
        # See the docstring. Confronted in `#s-think`'s second paragraph, and
        # the oak's verdict is the bench's own version of the same answer.
        {"id": "ECO-06",
         "statement": "If it goes wrong, you just put the species back.",
         "elicited_by": "s-bench",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B9, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ Deliberately none of b9-01's words — producer, consumer, decomposer,
    # food chain and food web are that lesson's to give, and re-glossing them
    # here would make the chips claim this page teaches them. These four are
    # what THIS page adds.
    "vocabulary": [
        {"term": "interdependence",
         "definition": "Organisms in an ecosystem depending on one another, so "
                       "that a change in one changes the others.",
         "note": "Not only through feeding — the bees in this wood eat nothing "
                 "in it."},
        {"term": "specialist",
         "definition": "An organism that depends on one food, or very few.",
         "note": "It has the least to fall back on when one of them goes."},
        {"term": "generalist",
         "definition": "An organism that feeds on many different things.",
         "note": "Losing one of them barely registers, which is what makes a "
                 "web with many routes steadier."},
        {"term": "top predator",
         "definition": "An animal at the top of a web, with nothing that "
                       "hunts it.",
         "note": "Nothing eats it. Plenty still depends on it."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and no foot line names a slot. The
    # web is eight lines of prose and Design drew no diagram. NOTES-B9 flag 17
    # asks for one and is not dropped by this; declaring a slot here would
    # invent a sourcing task in `docs/ks3/diagram-manifest.md` for a drawing
    # nobody has commissioned.
    # ⊕ DRAWN, 18 Aug 2026 — Mide's diagram ruling. The same wood as b9-01,
    # this time with no thread marked, because this lesson is not about one
    # route through the web: it is about what happens to the whole web when a
    # species leaves it.
    #
    # This is the page that most needed a drawing. Design's bench states the
    # web as eight sentences under the heading "Who eats whom", and then asks
    # the student to remove a species and follow the consequence three rounds
    # out. Following a consequence through a web means holding the web in your
    # head; the eight sentences are the web ENCODED, and a student who has to
    # decode them first is spending their working memory on the decoding rather
    # than on the reasoning the bench is for. The diagram is that decoding done
    # once, on the page, before the bench asks for it.
    #
    # It is placed BEFORE `#s-bench` for that reason, which is the one point
    # where the document order departs from Design's. Nothing is displaced —
    # hook still comes first, the bench still follows, and the eight sentences
    # stay exactly where and as they are.
    "figures": [
        oak_wood(
            "b9-oak-wood-web",
            title="The food web of the oak wood the bench works on",
            desc="Organisms in an oak wood arranged in rows by what they eat, "
                 "the same wood the bench below removes a species from. "
                 "Producers at the bottom: the oak and wildflowers. Above "
                 "them the plant eaters: caterpillars and aphids on the oak, "
                 "mice on acorns and seeds, and bees. Above those, animals "
                 "that eat plant eaters: blue tits on caterpillars and aphids, "
                 "ladybirds on aphids alone, owls on mice. At the top a "
                 "sparrowhawk, eating blue tits — and also mice, a line that "
                 "reaches down past a whole row. Fungi and bacteria sit in "
                 "their own row off the ladder, feeding on dead material from "
                 "every level. Every arrow points from the organism being "
                 "eaten towards the one eating it, because that is the "
                 "direction the energy travels. A dashed line from the bees to "
                 "the wildflowers is labelled pollinates, and carries no "
                 "energy — which is why removing the bees does not starve "
                 "anything directly.",
            caption="The wood, before anything is taken out of it. Count the "
                    "arrows into and out of each organism before you choose "
                    "one to remove — the ones with a single line are not "
                    "always the ones that matter least."),
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b9/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md §7, plus
        # the two headline labels §7 did not anticipate. Read sites are listed
        # in the docstring.
        # The web the bench operates on, shown before it is worked. See the
        # `figures` note above for why this one block sits ahead of the
        # flagship rather than after it.
        {"type": "figure", "ref": "b9-oak-wood-web", "anchor": "s-web"},

        {"type": "remove-a-species", "id": "take-one-out",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · one oak wood, eight species",
         "heading": "Take one out and follow it",
         # Design's mono line beside the heading (page line 493). Three states,
         # and the middle one carries the live count.
         "progress": {"none": "nothing removed yet",
                      "mid": "round {n} of {total}",
                      "all": "all three rounds"},

         "web_label": "Who eats whom",
         "web_lines": WEB_LINES,

         "tabs_label": "Remove",
         "species": SPECIES,

         # ⚠️ NOT IN THE PAYLOAD SCHEMA, and authored because Design composes
         # the panel headline from the species' own label rather than writing
         # twelve headlines. `{name}` is required by `r_remove_a_species` and
         # filled by `wireRemoveASpecies`. See the docstring.
         "still_here_label": "{name} — still in the wood",
         "removed_label": "{name} removed",

         "step_first_label": "Remove it",
         "step_label": "And then?",
         "step_spent_label": "Followed to the end",
         # ⚖️ `ECO-06`'s elicitation, and the reason the misconception above
         # names this section. One press and the wood is whole again.
         "reset_label": "Put it back"},

        # #s-rules — the band panel, and the section that turns six worked
        # removals into three rules. Rail stop 3, mirroring `s-bench`; see the
        # docstring.
        {"type": "rule", "anchor": "s-rules",
         "eyebrow": "Three things a web does",
         "statement": "Connected does not mean fragile, and it does not mean "
                      "safe.",

         "cards": RULE_CARDS,

         # Design nests the key fact inside this section (page lines 170–174)
         # on the CARD ground with the accent offset shadow. `card`, because
         # the section itself is `band` and band on band is invisible — the
         # same arrangement and the same reason as b8-01's.
         "key_fact": {"ref": "a-removal-reaches-what-it-never-touched",
                      "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "ECO-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-rules on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 173
    # and identical to payload schema §12's b9-03 entry.
    "key_facts": [
        {"id": "a-removal-reaches-what-it-never-touched",
         "text": "Removing one species changes the numbers of species it never "
                 "touched, because every organism in a web is connected to "
                 "every other through some route. A web with many alternative "
                 "routes absorbs the change; a web with few does not.",
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
         "targets": "ECO-05",
         "statements": [
             # The `<em>chain</em>` survives `rich()`, which allows `<em>` and
             # `<strong>` and nothing else. The emphasis is load-bearing: the
             # sentence is about the difference between a chain and a web and
             # the italic is what carries it.
             {"quote": "Removing a species only affects the things directly "
                       "above and below it.",
              "body": ["That is what a food <em>chain</em> would predict, and "
                       "it is why the chain is a teaching device rather than a "
                       "description. In a web, an effect travels along every "
                       "route out of the missing species and keeps going, and "
                       "the routes that matter most are often sideways rather "
                       "than up and down. Take the blue tits out of the wood: "
                       "caterpillars increase, obviously — but so do aphids, "
                       "because blue tits were eating those too, and the "
                       "ladybirds now have more food than they can use while "
                       "the sparrowhawks have lost their main prey and start "
                       "taking mice instead, which affects the owls. Three or "
                       "four species deep, and none of them shares a line with "
                       "a blue tit on a simple diagram. The practical "
                       "consequence is that you cannot predict the result of a "
                       "removal by looking only at what the species ate and "
                       "what ate it."]},
             # ⚠️ `B11` resolved to its lesson title — "What could not be
             # lifted" 2. The destination is carried in `references`.
             #
             # This paragraph is why the bench is upstream of it in the
             # document: the student has already pressed "Put it back" and
             # watched the wood return whole, and this is the page saying that
             # a real one does not.
             {"quote": "If it goes wrong, you just put the species back.",
              "body": ["Sometimes you can, and it is expensive, slow and often "
                       "only partly successful. Frequently you cannot, because "
                       "while the species was absent the ecosystem rearranged "
                       "itself: another organism moved into the space, the "
                       "plants it depended on died out, or the population that "
                       "would have been the source is extinct. Extinction has "
                       "no undo — that is what the word means, and it is the "
                       "subject of When the environment changes: extinction. "
                       "Even where a return is possible, the wood you put the "
                       "species back into is not the wood it left. This is the "
                       "reason ecologists argue for caution rather than "
                       "confidence: not because every disturbance is a "
                       "disaster, but because the outcome genuinely cannot be "
                       "predicted in advance, and the experiment cannot be run "
                       "twice."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — MEASURED, BOTH MARKED RUNGS CLEAN, NOTHING
    # REWRITTEN. rung 1 correct 9w against 8 / 10 / 8 (not strictly longest);
    # rung 2 correct 14w against 5 / 7 / 12 (gap 2, ratio 1.17). Both are
    # inside `length_tell()` because the distractors already state the same
    # KIND of thing as the correct answer — wrong rules on rung 1, named
    # species with their own route on rung 2. Every distractor's belief is
    # written out in the docstring, with the one register id among them.
    #
    # Every option, every `answer` index, Design's option ORDER and all six
    # corrections are byte-identical.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Follow one step",
            "q": "All the ladybirds in the wood are killed by a pesticide. "
                 "What is the immediate effect?",
            # All four state a rule in the same three-part shape — subject,
            # because-clause, consequence — so the student cannot pick by
            # form. B inverts the meaning of "control", C is the
            # all-insects-are-pests rule, D says a species' only connections
            # are the things that eat it.
            "options": [
                "Aphid numbers rise, because their main predator has gone",
                "Aphid numbers fall, because ladybirds were controlling them",
                "The oak grows better, with fewer insects in the wood",
                "Nothing, because ladybirds are not eaten by anything",
            ],
            "answer": 0,
            "feedback": {
                1: "Read that one again — controlling means keeping numbers "
                   "down. Remove the control and the numbers go up.",
                2: "One fewer insect species, and it was the one eating "
                   "another insect. The oak gets worse, not better.",
                3: "What eats a species is only half of its connections. What "
                   "it eats matters just as much.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Owls are removed from the wood. Which species is affected "
                 "that most people would not predict?",
            # ⚖️ Option A is five words and is still not a length tell: the
            # gate measures against the LONGEST distractor (12w), the belief is
            # short because students hold it short — it is `ECO-05` at its most
            # confident — and padding it would make it sound more considered
            # than their own version. Do not "fix" it.
            #
            # The correct answer is the owls' third round at the bench, which
            # the student has already been able to reach.
            "options": [
                "The mice, whose numbers rise",
                "The bees, because more mice eat more wildflower seeds and "
                "the flowers thin out",
                "The sparrowhawks, because owls were their competitors",
                "None — owls are at the top, so nothing depends on them",
            ],
            "answer": 1,
            "feedback": {
                0: "True, and everyone predicts it. The question is asking "
                   "what happens after that.",
                2: "A reasonable thought, but in this web sparrowhawks eat "
                   "blue tits mainly and take mice only when they must — more "
                   "mice is if anything a small gain.",
                3: "That is exactly the assumption the bench is built to "
                   "break. Removing the top of a web changes the bottom of it.",
            }},
        "explain": {
            "title": "Rung 3 · Trace a chain of effects",
            "q": "Blue tits disappear from the wood. Trace the effects through "
                 "at least three further species, saying what causes each "
                 "step, and finish by explaining why a food chain diagram "
                 "would not have predicted the last one.",
            "field_label": "Your explanation",
            "placeholder": "With no blue tits…",
            # The fifth criterion is `ECO-05` marked as a criterion rather than
            # as prose, which is why the confrontation above can stay static
            # and still be assessed.
            "success": [
                "Says caterpillars and aphids both increase, because blue tits "
                "ate both.",
                "Says the oak is affected, losing leaves to caterpillars and "
                "sap to aphids.",
                "Says sparrowhawks lose their main prey and hunt mice more.",
                "Says mouse numbers fall, so owls are affected — a species "
                "with no direct link to a blue tit.",
                "Explains that a chain shows one route only, while the effect "
                "travelled sideways through a shared predator.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A farmer sprays an insecticide on a field bordering the "
                 "wood. It kills aphids, and it also kills ladybirds and most "
                 "other insects. Predict what happens over the following two "
                 "years, and explain why the aphid problem often comes back "
                 "worse than before.",
            "field_label": "Your answer",
            "placeholder": "In the first weeks…",
            # Criteria 2 and 3 are the rung's whole argument: prey recover
            # faster than predators do, from a much lower base, so the control
            # arrives late and small. Criterion 5 is rule card one asked for in
            # a new setting.
            "success": [
                "Says aphid numbers crash immediately, along with everything "
                "else the spray reached.",
                "Says the aphids recover quickly, because they breed far "
                "faster than their predators do.",
                "Says the predators — ladybirds especially — recover slowly, "
                "and start from a much smaller number.",
                "Concludes the aphids can therefore reach higher numbers than "
                "before, with nothing left to control them.",
                "Identifies a wider consequence — insect-eating birds losing "
                "food, or pollinators being killed along with the pest.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Every organism in a food web is connected to every other by "
                "some route, so removing one changes the numbers of species it "
                "never touched. Effects travel sideways as well as up and "
                "down, and they take time to appear. A web with many "
                "alternative feeding routes absorbs a loss more easily than "
                "one with few, and a species that has gone cannot reliably be "
                "put back.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B9 flag 8, RESOLVED 16 Aug and VERIFIED PRESENT in the delivered
    # bytes. The ruled chain — wolf → elk numbers and elk behaviour → willow
    # and aspen → beaver → what lives in the water — is here in full, and the
    # overclaim it replaced is gone: `river`, `rivers` and `meander` appear
    # ZERO times on Design's page and zero times here. ⛔ Nothing in this
    # lesson may reintroduce a river, a stream or an aquatic example.
    #
    # ⚖️ MRB-225 holds: the layer adds Yellowstone and retracts nothing above
    # it. The closing `<em>` survives `rich()` and is load-bearing — it is the
    # sentence being quoted and refused, not the page's own claim.
    "stretch": [
        {"type": "explainer", "id": "what-the-wolves-reached",
         "text": "Wolves were hunted out of Yellowstone National Park by the "
                 "1920s and reintroduced in 1995, and what the park has shown "
                 "since is how far past its own prey a top predator reaches. "
                 "Elk numbers fell. Elk behaviour changed too — they stopped "
                 "feeding for long spells in the open valley bottoms where "
                 "they were easiest to ambush. Willow and aspen, the plants "
                 "elk browse hardest, began growing back along those streams. "
                 "Beavers need willow, and beavers returned to the stretches "
                 "where it recovered; their dams then changed what could live "
                 "in the water. Follow the links: a wolf never touches a "
                 "willow, and never touches a beaver. It is joined to the "
                 "willow through the elk and to the beaver through the willow, "
                 "and that is enough. This is the difference between a chain "
                 "and a web. Pull one strand hard and things you were not "
                 "watching move — which is why <em>remove the predator and "
                 "there will simply be more prey</em> is never the whole "
                 "answer."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination
    # on the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to trace a removal through a web of your own?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 301) and nothing in it is a safety
    # instruction — it is a note about how far the bench can be trusted.
    # Routing it through `safety_note` would print it in the treatment reserved
    # for "never light a candle without an adult", which devalues the safety
    # line. b8-01 and five B3–B7 lessons resolve the identical foot line the
    # identical way.
    #
    # ⚑ It is the honest half of NOTES-B9 flag 7 and it is load-bearing: the
    # page telling the student that eighteen consequence texts are plausible
    # directions rather than predictions, and that three rounds on a screen are
    # years in a wood.
    "convention_note": "The wood is a teaching web of eight species. Real "
                       "woodland webs contain hundreds, the outcomes described "
                       "are plausible directions rather than predictions, and "
                       "effects that appear here in three rounds take years in "
                       "a real ecosystem and do not always arrive.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # Rungs 3 and 4 both ask for a reasoned explanation and a prediction
    # defended against a plausible alternative — analysis and evaluation. The
    # second confrontation is scientific attitudes in the strict sense: it is
    # about what evidence can settle when the experiment cannot be run twice.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
