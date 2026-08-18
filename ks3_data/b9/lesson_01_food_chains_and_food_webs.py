"""B9 L1 — Food chains and food webs (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b9/b9-01-food-chains-and-food-webs.dc.html` (563 lines), her
author's notes `docs/ks3/design-reference/b9/NOTES-B9.md`, and the B9 payload schema
`docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md` §0, §1, §2, §4, §5, §11, §12 and §14,
under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the two listed under "What could not be lifted" and the three rung-2
distractors rewritten under MRB-177, each of which is recorded below with its
before and after. The three chains, the four role cards, both marked rungs and
both self-marked rungs came out of the page's own `CHAINS`, `ROLE_CARDS`,
`RUNGS` and `SELF_RUNGS` arrays via `tools/extract_design_payload.js`, not off a
keyboard.

── `covers` is one clause, and it is the one the whole unit hangs from ──

`KS3.B.ECO.01a` reads, in full: *interdependence shown as food chains and food
webs: who eats whom, and what happens to the energy along the way*. The two
halves of that clause are the two halves of this page — `#s-roles` answers *who
eats whom* with four job titles and the web-versus-chain paragraph, and
`#s-bench` answers *what happens to the energy* by making the student climb it
and watch nine tenths of it fail to arrive at every step.

`ECO.01b`, `c` and `d` belong to b9-02, b9-03 and b9-04 and are not touched
here; `build_ks3.validate()` enforces exactly-once ownership, so a second claim
would fail the build rather than quietly double up.

── B9 OWNS THE TROPHIC 10:1, AND THIS IS THE PAGE THAT EARNS IT ─────────

Schema §0.7 and `ks3_data/b9/__init__.py`: the one-tenth-per-level figure is
this unit's for the whole key stage, and b9-01 is where a student meets it as a
MEASUREMENT rather than as a stated fact. B7 flag 19 raised the ratio without
owning it and it leaked forward once already. Nothing after this lesson
re-teaches it; b9-05 runs the same arithmetic in the opposite direction and
cites this bench for the ratio itself.

`r_chain_ledger` refuses any `factor` but ten, with a message that says why. It
is not a tuning constant: the legal line calls a tenth a teaching average, rung
2 asks what became of the other ninety per cent, rung 3's first criterion is the
figure, rung 4's last criterion is a warning against treating it as exact, and
the hook's reveal counts *four steps* down to a ten-thousandth. Change the
factor and seven authored strings on this one page become false, silently.

── The instrument: a ladder of figures drawn upside down on purpose ────

`#s-bench` is `chain-ledger`, on `ks3-block ks3-dark ks3-practical` (page line
105), so `practical` is MEASURED from Design's own markup rather than inferred
from the kind name — payload schema §0 rule 2, and contract §4 records that B1
got two of six wrong by inferring it.

⚖️ **THE PRODUCER IS AT THE BOTTOM AND THAT IS THE CLAIM, NOT THE STYLING.**
Design's level list is `flex-direction: column-reverse`, so `data-i="0"` — the
grass, the ten thousand kilojoules — is drawn lowest and the student reads
upwards in the direction the energy travels. Flip the list to ordinary document
order and the same numbers make the opposite claim, in a lesson whose
most-marked misconception (`ECO-01`, and Design says examiners mark it) is
exactly about which way the arrows point. The rule lives in `shared/ks3.css` and
there is a parity row on it.

⚖️ **THE VERDICT LINE IS COMPUTED, NEVER AUTHORED PER CHAIN.** Three authored
fragments — `lead`, `mid`, `tail` — with two figures derived from the chain's
own length between them. That is the whole design: a fourth chain needs no new
prose and cannot disagree with the ladder of figures above it. Verified against
Design's own expression (page lines 453 and 515–517) at all three chains:

    field  4 levels   10,000 → 1,000 → 100 → 10 kJ    "10 arrived here — 0.1%"
    wood   4 levels   10,000 → 1,000 → 100 → 10 kJ    "10 arrived here — 0.1%"
    sea    5 levels   10,000 → … → 10 → 1 kJ           "1 arrived here — 0.01%"

⚠️ **`0.10 → 0.1` AND `0.01` SURVIVES UNTOUCHED.** Design's rule is
`toFixed(2).replace(/\\.?0+$/, '')`, and the difference between those two
outputs is the whole difference between a four-level chain and a five-level one
— which is the argument the sea chain exists to make. `_b9_strip2` reproduces
it rather than tidying it.

⛔ **`startChain` IS NOT AUTHORED.** Design ships it as a tweak prop (enum
`field`/`wood`/`sea`, default `field`) and it is an author's preview dial, not
content — schema §5's ⚑. The renderer opens on `chains[0]`, which IS `field`, so
the page opens exactly as Design's does and no key is authored that nothing
reads. (b8-01 authored the equivalent key for the opposite reason: its default
was `AMOUNTS[1]`, so omitting it would have changed the page.)

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0 rule 3). Design's state bag holds
`shown` and `everTopped`; both are the runtime's, `wireChainLedger` initialises
them itself, and under R5 a key with no read site fails `ks3_key_audit.py`.

⊖ **`energy_unit` and `pct_suffix` are NOT authored either.** They exist on the
renderer and their defaults are `" kJ"` and `"% of the original"` — Design's own
bytes, character for character. Authoring them would restate the shipped default
in a second place where a later edit could make the two disagree.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page lines 305–310) and her `isDone()` gives `s-roles` the
BENCH's predicate, character for character, one section to the left:

    if (id === 's-bench') return s.everTopped;
    if (id === 's-roles') return s.everTopped;      // page line 400

`#s-roles` is an eyebrow, a display statement, four static cards, a closing
paragraph and a key fact: no control, no commitment, no field, no reveal. It is
the PAYOFF of the ledger beside it, and it carries no control precisely because
the bench has already taken the student's commitment. That relationship is a
MIRROR, `wireRail`'s `paint()` resolves it at rail level — which is the level
Design computes it at — and `ks3_parity.check_rail_matches_design` gates the
built rail against `docs/ks3/rail-manifest.md`, where this page's row reads
`s-hook s-bench s-roles s-ladder | s-roles=s-bench`.

⚠️ Payload schema §4's tables are correct as MEASUREMENT and its instruction to
*author three stops and drop the band* is REVERSED at the head of the same
section. Four is what Design drew and four is what ships. Shipping three fails
the build.

`#s-think` and `#s-keynote` are on no rail, and that is Design's too:
`#s-keynote` asks nothing, and `#s-think` here is static markup — two quotes,
two bodies, no options, no reveal, no button — so it is a `confrontation` and
not contract R1's `predict`. Schema §3, measured on all six pages.

── What could not be lifted byte-identical, and why ────────────────────

Both are build-internal identifiers. No science word moves in either.

1. **`b7-04` in the sea chain's producer note.** Design writes *"Microscopic
   algae doing the photosynthesis you met in b7-04 — roughly half the world's
   total."* A student cannot resolve a slot code, and printing one is exactly
   the platform leakage §8.10 exists to stop. Resolved to the lesson TITLE, the
   way b7-04 and b8-01 resolved the identical shape:

       Design:  the photosynthesis you met in b7-04
       Built:   the photosynthesis you met in Why almost all life depends on it

   The destination is not lost — `why-almost-all-life-depends-on-it` is Design's
   own first *Before this lesson* card and is carried in `requires`.

2. **The `Conservation of energy` hyperlink in `#s-think`.** `rich()` allows
   `<em>` and `<strong>` and nothing else, so no anchor survives anywhere on the
   page. Here that costs nothing at all: the link TEXT is already the lesson
   title, so every word is kept and only the tag goes, and
   `conservation-of-energy` is Design's second *Before this lesson* card and is
   in `requires`. The two `<em>` runs in the FIRST confrontation body — *eats*
   and *energy travels this way* — are kept, because `rich()` renders them and
   the contrast between the two phrases is the whole paragraph.

⚠️ No sequence leak to repair on this page: `year`, `Year` and `half-term`
appear zero times in Design's bytes, checked rather than assumed.

── ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN, RUNG 2 REPAIRED ─────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor by
≥4 words or by ≥1.4×.

    rung 1  correct 11w vs 13 / 8 / 12   — not strictly longest      ✓ as drawn
    rung 2  correct 19w vs  3 / 13 / 10  — gap 6, ratio 1.46         ✗ TRIPPED
    rung 2  correct 19w vs 20 / 21 / 21  — not strictly longest      ✓ repaired

**Rung 1 is Design's, untouched, and it did not need touching.** The correct
answer names a DIRECTION and gives the reason for it, and so do two of the three
distractors — arrows as appetite, arrows as two-way — while the fourth states a
different wrong rule of the same size, that direction is a drawing convention
rather than a claim. Same subject, same shape, same kind of consequence, which
is what MRB-177 asks for, and the parity falls out of the construct rather than
being imposed on it.

**Rung 2 tripped both arms at once** and it is the construct MRB-177 named,
exactly: Design's correct option states a RULE with two branches (most was
respired and warmed the surroundings; the rest went to decomposers) while all
three distractors stated a one-clause wrong REASON — *"It was destroyed"* is
three words. The correct answer was therefore longer BY CONSTRUCTION, and a
student could have scored the rung without reading it.

Each distractor is rewritten as a WRONG RULE in the correct answer's own shape —
where the energy went, and what follows from its having gone there — keeping
Design's clause verbatim at the front and gaining the consequence the belief
licenses:

    r2 A  it was destroyed
          + "as it passed up the chain, so there is less energy in the world
             than there was"                                        3w → 20w
    r2 C  it stayed in the parts the animal could not reach
          + "so the loss is leftovers on the ground"               13w → 21w
    r2 D  it was used up in movement and no longer exists
          + "so an active animal passes on less than a still one"  10w → 21w

**The correct option is unchanged, `answer: 1` is unchanged, Design's option
ORDER is unchanged, and all three of her corrections are byte-identical.** Each
still answers exactly the belief its rewritten distractor states, and two of the
three now land harder:

  * A now ends on *there is less energy in the world than there was*, which is
    the conservation claim head-on, and the correction's first clause is
    "Energy is never destroyed — that rule has no exceptions".
  * C now says the loss IS leftovers, as a rule, and the correction's "most of
    the loss is respiration, not leftovers" contradicts precisely that.

⚖️ **The four rewritten and unrewritten options now run 20 / 19 / 21 / 21, so
the correct answer is the SHORTEST by one word and there is no tell in either
direction.** That was deliberate: padding the distractors past the correct
answer would trade one tell for its mirror image, which a class works out just
as fast.

⚑ For Mide's science gate — every NOTES-B9 flag landing on THIS lesson, and
  what was checked against it. Four flags, four checked, **none corrected**:

  * flag 1   **The 10% rule.** CHECKED AND LEFT. The page never states it as a
             measurement: the key fact says *"only about a tenth"*, rung 2's
             stem says *"about 10%"*, rung 4's fifth criterion explicitly marks
             a student for *"avoiding treating the 10% figure as exact, or
             noting that it is an average rather than a measurement"*, and the
             legal line gives the real range as *"a few per cent to around
             twenty"*. That is MRB-225 performed in the drawing — the claim is
             already stated at the size that is true, and the hedge is marked
             rather than merely printed. Published trophic efficiencies do run
             roughly 2–20%, with ~10% the long-standing teaching average
             (Lindeman), so the figure and the hedge are both defensible.
             **The one thing that must not happen is a later pass "tidying" the
             hedges** — four separate strings carry them and all four are
             load-bearing.

  * flag 2   **The three chains, and whether the sea chain should run to orca.**
             CHECKED AND LEFT. All three are plausible British examples and the
             role labels are right at every level. The sea chain's fifth level
             is the reason the chain-length argument is visible at all: with
             three four-level chains the verdict line would print the same two
             figures three times and the tab row would teach nothing. It is also
             the only level on the page that reaches ONE kilojoule, which is
             what makes *"add one more level and there would be a tenth of that
             again"* concrete. Orcas do take seals, so the link is real.
             ⚑ It is arguable whether the marine chain is best drawn as five
             discrete levels — real marine webs are less tidy than that — and
             that is Mide's call, not the port's. If he wants it cut to four,
             the cost is the whole 0.01% branch and both figures in the verdict.

  * flag 3   **"A pair of blue tits needs something like a hundred caterpillars
             a day to raise a brood."** CHECKED, LEFT, AND FLAGGED UP RATHER
             THAN DOWN. Design's own note asks whether it is usually quoted
             higher; it is. The commonly cited figure for a blue tit brood is
             several hundred to around a thousand caterpillars a DAY at peak
             demand, over a fortnight or more. **Design's number therefore errs
             SAFE — it understates — and the sentence's work is the timing point
             beside it** ("which is why they time their nesting to the
             caterpillar peak"), which is unaffected by the size of the number.
             MRB-225 says a claim shrinks until it is true; it does not license
             enlarging a claim that is already inside its own hedge, and
             *"something like"* is that hedge. Left as drawn. ⚑ If Mide wants
             the higher figure it lands in exactly one string, this note, and
             nowhere else in the lesson — no arithmetic depends on it.

  * flag 4   **Whales eating krill two levels up** (*Going further*). CHECKED
             AND LEFT. Baleen whales feed on krill, krill graze phytoplankton,
             so a blue whale sits at the third level — two steps above the
             producers — and that is exactly what the paragraph says. The
             argument it is making is the arithmetic one: the largest animals
             that have ever existed have to feed near the bottom of a chain
             because there is not enough energy anywhere else, which is the
             lesson's own claim applied somewhere new. Nothing in it overstates.

  * flag 17  **No diagrams anywhere in B9, and a drawn food web is the obvious
             candidate.** MEASURED on this page rather than assumed: `<img>`,
             `<figure>` and `<picture>` each appear ZERO times, and every `<svg>`
             is the nav chevron or a `ks3-mark` icon. `figures` is therefore
             empty by §4.10, and declaring a slot the page never references
             would invent a sourcing task in `docs/ks3/diagram-manifest.md`.
             The flag is NOT dropped by this and it is Mide's to rule on — B9's
             nearest thing to a diagram is this bench, which is a bar chart of
             one number.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes six times: *energy is not lost, it leaves this
chain*. The hook's reveal ("there is not enough energy left"), the bench's
per-level notes ("most of what a rabbit eats is respired to stay alive"),
`#s-think`'s second body ("nothing has gone missing; it has left this chain,
which is a different claim"), the key fact, rung 2's correct option, rung 3's
second criterion and the key note all say the same thing at the same size. The
stretch layer adds the land-use argument and the whale case and retracts nothing.

── Misconception ids: ECO-01 and ECO-02, and the family opens here ─────

⚠️ **The `ECO` prefix row does not yet exist in
`docs/ks3/misconception-register.md`.** Grepped: nine prefixes are open and
`ECO` is not among them. Schema §14 pre-allocates `ECO-01`…`ECO-11` across the
unit's six lessons and permanently forbids `ECO-12`, which the register has
already reserved with the note *"`ECO-12` — is `NOS-04`"*. **That file is not
this pass's to edit** (contract §0), so the two statements are authored here in
register voice, byte-identical to Design's own quoted beliefs, and are reported
for whoever opens the row. No gate resolves an id against the register file, so
the lesson builds either way; what is at risk is the register's completeness.

Both values resolve against the BUILT page (MRB-244): `s-think` is the
confrontation block's emitted anchor and `s-ladder` is the ladder's. `s-ladder`
is the honest `elicited_by` for both — rung 1's option B is `ECO-01` stated in
the student's own words and rung 2's option A is `ECO-02` stated in the
student's own words, and the ladder is the only place on this page where either
belief is offered as something to commit to. The hook's four options are about
why chains STOP and carry neither belief; `#s-bench` shows a consequence and
asks for no verdict.

── Keys this pass authors that the RENDERER reads (contract R5) ────────

Named explicitly rather than left to be discovered. Every one is measured off
`r_chain_ledger` and `wireChainLedger`:

    progress    {"before", "after"}   → `_KIND_HEAD_FROM["chain-ledger"]`,
                                        converted to a head counter whose
                                        denominator comes from chains[0]
    start_kj    the top of the ladder, and `data-start-kj`
    factor      refused unless it is ten — see the ⚖️ above
    tabs_label  the mono label over the tab row
    chains      tabs + one panel each, every panel in the document
    step_label  / step_spent_label → the up button's two states
    reset_label the reset button
    verdict     three fragments, two computed figures

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
component class at (0,1,0); every B9 colour rule is written at (0,2,0) under
`.ks3-dark …` and `ks3_parity.check_dark_text_specificity()` resolves it on the
real cascade. Recorded here because this payload is what feeds it.

── One place Design's page and the ENGINE disagree, and it is reported ─

Design's `#s-roles` runs: eyebrow, display statement, four cards, the
web-versus-chain paragraph, THEN the key fact box. `r_rule()` emits the nested
key fact BEFORE `close`, so the built page runs: cards, key fact, paragraph.
`build_ks3.py` belongs to the engine pass and is not this module's to edit
(contract §0), so the record is authored against the renderer as it stands and
the ordering is reported. Nothing is joined, dropped or invented — the same four
strings and the same paragraph ship, one slot apart.
"""

# ── the three chains (page lines 324–345) ────────────────────────────────
#
# Field 4 levels, oak wood 4, open sea 5. The DIFFERENT LENGTHS are the
# argument: `r_chain_ledger` refuses a payload with fewer than two chains for
# that reason, and the verdict line's two figures fall out of the length rather
# than being authored per chain. Design's order is kept — `field` is `chains[0]`
# and therefore the tab the page opens on, which is her `startChain` default.
#
# ⚠️ The sea chain's producer note has `b7-04` resolved to its lesson title —
# "What could not be lifted" 1. The destination survives in `requires`.
CHAINS = [
    {"id": "field", "label": "A field",
     "levels": [
         {"name": "Grass", "role": "Producer",
          "note": "Ten thousand kilojoules captured from sunlight and built "
                  "into plant material."},
         {"name": "Rabbits", "role": "Primary consumer",
          "note": "Most of what a rabbit eats is respired to stay alive and "
                  "stay warm, or passes straight through. Only a tenth becomes "
                  "rabbit."},
         {"name": "Foxes", "role": "Secondary consumer",
          "note": "A fox is a warm, active hunter, so its bill for simply "
                  "existing is high. A tenth again reaches this level."},
         {"name": "Golden eagle", "role": "Tertiary consumer",
          "note": "Ten kilojoules of the original ten thousand. This is why "
                  "eagles hold territories of many square kilometres and why "
                  "there are so few of them."},
     ]},
    {"id": "wood", "label": "An oak wood",
     "levels": [
         {"name": "Oak leaves", "role": "Producer",
          "note": "One large oak supports the whole of the rest of this chain, "
                  "and hundreds of other species besides."},
         {"name": "Caterpillars", "role": "Primary consumer",
          "note": "Caterpillars are unusually efficient eaters — they do "
                  "little but eat — but most of the leaf still goes to "
                  "respiration and droppings."},
         # ⚑ NOTES-B9 flag 3. The hundred understates rather than overstates;
         # checked and left, and the working is in the docstring. "Something
         # like" is the hedge and it is load-bearing.
         {"name": "Blue tits", "role": "Secondary consumer",
          "note": "A pair of blue tits needs something like a hundred "
                  "caterpillars a day to raise a brood, which is why they time "
                  "their nesting to the caterpillar peak."},
         {"name": "Sparrowhawk", "role": "Tertiary consumer",
          "note": "Ten kilojoules. One sparrowhawk needs the small birds of a "
                  "whole wood, and the wood can support one pair."},
     ]},
    # ⚖️ FIVE levels, and the fifth is why this chain is on the page. It is the
    # only level in the lesson that reaches one kilojoule, and the only one that
    # makes the verdict line print 0.01% instead of 0.1% — which is what the
    # tab row is for. NOTES-B9 flag 2 asks whether it should stop at the seal;
    # dropping the orca costs the whole 0.01% branch. Mide's call.
    {"id": "sea", "label": "The open sea",
     "levels": [
         # ⚠️ `b7-04` resolved to its lesson title — "What could not be lifted" 1.
         {"name": "Phytoplankton", "role": "Producer",
          "note": "Microscopic algae doing the photosynthesis you met in Why "
                  "almost all life depends on it — roughly half the world’s "
                  "total."},
         {"name": "Zooplankton", "role": "Primary consumer",
          "note": "Drifting animals grazing the algae, in numbers nobody can "
                  "count."},
         {"name": "Herring", "role": "Secondary consumer",
          "note": "A hundred kilojoules of the original ten thousand."},
         {"name": "Seals", "role": "Tertiary consumer",
          "note": "Ten kilojoules. A seal eats several kilograms of fish a day "
                  "and it is already scraping the bottom of the barrel."},
         {"name": "Orca", "role": "Quaternary consumer",
          "note": "One kilojoule of the ten thousand — a ten-thousandth. This "
                  "is about as far as any chain on Earth goes, and orcas hunt "
                  "across whole oceans to make it work."},
     ]},
]

# ── the four role cards (page lines 347–352) ─────────────────────────────
#
# Design's `kind` is the mono accent tag and maps to `role`, which is the slot
# `_rule_card()` reads for it. All three strings per card survive unchanged and
# nothing is joined — this is the slot b7-01's four part cards shipped empty
# `<li>`s for before MRB-245 repaired it.
#
# ⚖️ The fourth card is the one a scheme of work usually gets wrong, and its
# last sentence is why it is here: decomposers are NOT the end of the chain,
# they are underneath all of it. Nothing in the bench draws them — the ledger is
# a single thread — so this card is the only place on the page that says where
# the droppings and the dead material go, and rung 2's correct option depends on
# a student having read it.
ROLE_CARDS = [
    {"role": "Bottom of every chain", "name": "Producers",
     "body": "Plants and algae. They do not eat — they build their own food, "
             "so they are the point where energy enters the living world."},
    {"role": "Level two", "name": "Primary consumers",
     "body": "Herbivores: the animals that eat producers. The most numerous "
             "animals in almost every ecosystem, because this is where the "
             "food is."},
    {"role": "Levels three and up",
     "name": "Secondary and tertiary consumers",
     "body": "Predators, and the predators of predators. Rarer at every step "
             "up, and each one needs a larger area to feed from."},
    {"role": "Everywhere at once", "name": "Decomposers",
     "body": "Bacteria and fungi feeding on dead material and droppings from "
             "every level. They are not the end of the chain — they are "
             "underneath all of it, returning the minerals to the soil."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 154 character for character.
    "slug":        "food-chains-and-food-webs",
    "title":       "Food chains and food webs",
    "discipline":  "biology",
    "unit":        "ecosystems-and-interdependence",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.ECO.01a` — who eats whom, and what happens to the energy along the
    # way — owned whole. `#s-roles` discharges the first half and `#s-bench` the
    # second. See the docstring; b, c and d belong to b9-02, b9-03 and b9-04.
    "covers":      ["KS3.B.ECO.01a"],
    # Named, used, and owned elsewhere. PHOT.01 is b7-01's and is what the
    # producer level of every chain rests on — the page says "captured from
    # sunlight" and does not re-teach it. RESP.01 is b8-02's and is where the
    # missing ninety per cent goes: `#s-think`'s second body and rung 2's
    # correct option both name respiration and neither explains it.
    "touches":     ["KS3.B.PHOT.01", "KS3.B.RESP.01"],
    "beyond_statutory": False,
    # `interdependence` starts here — this is the first lesson in the key stage
    # that draws it. `energy` is at `secure`: the student has conservation from
    # P1 and the two reactions from B7 and B8, and this is where the three are
    # used together on something new.
    "threads":     [{"id": "interdependence", "level": 1},
                    {"id": "energy", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. Both are also the
    # destinations of the two links this page loses to `rich()` — the sea
    # chain's `b7-04` and `#s-think`'s `Conservation of energy` — so both edges
    # are carried whether or not the anchor survives.
    "requires":    ["why-almost-all-life-depends-on-it",
                    "conservation-of-energy"],
    "assumes":     [],
    # Design's "Connects to" card, in her order.
    #
    # ⚠️ `aerobic-respiration` MUST carry its unit. A bare slug in `references`
    # is resolved against the CURRENT unit — unlike `requires`, which resolves
    # across the key stage — so the bare form built a link to
    # `/ks3/biology/ecosystems-and-interdependence/aerobic-respiration.html`,
    # which is not a page. `check_internal_links` caught it; the dict form is
    # what b8-01 uses for the same reason.
    "references":  ["predator-and-prey",
                    {"unit": "B8", "lesson": "aerobic-respiration"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Trophic levels, pyramids of biomass, and calculating the "
                   "efficiency of energy transfer between levels.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Nobody has ever found a food chain with ten links in it. "
                    "There is a reason, it is arithmetic, and it decides the "
                    "shape of every ecosystem on Earth.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 305–310). `s-roles` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # ledger's predicate — Design's own `isDone()`, page line 400. `short` and
    # `label` are her `RAIL_SHORT` and `RAIL` strings, "Job titles" included.
    # Shipping three fails `check_rail_matches_design`; see the docstring.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Why chains stop",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.everTopped` (page line 399). Sticky
        # by her design and monotonic by ours — the stop records that the
        # student reached the top of a chain once, and switching tabs restarts
        # the climb without untucking it.
        {"anchor": "s-bench", "short": "BENCH", "label": "Climb the chain",
         "done_when": "chain_topped"},
        {"anchor": "s-roles", "short": "ROLES", "label": "Job titles",
         "mirrors": "s-bench", "done_when": "chain_topped"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer.
    # B is the correct one and the reveal says so at once; the hook is not a
    # trick, it is the claim the bench then has to earn in kilojoules.
    #
    # ⚖️ None of the four is `ECO-01` or `ECO-02`, which is why neither
    # misconception names `s-hook` as its `elicited_by`. All four are wrong
    # answers to "why do chains stop", and the three wrong ones are the three
    # a class actually offers: size, speed, and appetite.
    "phenomenon": {
        "kind": "narrative",
        "title": "Why is there no animal that eats the animal that eats the "
                 "eagle?",
        "prompt": "Chains stop. Grass, rabbit, fox — and then nothing. Four or "
                  "five links is about the limit anywhere in the world, on "
                  "land or at sea, and the rule holds whether the organisms "
                  "are enormous or microscopic.",
        "commit": "What stops food chains getting longer?",
        "options": [
            "Top predators are too big for anything to hunt",
            "There is not enough energy left to support another level",
            "Animals higher up are too fast to catch",
            "Nothing wants to eat a predator",
        ],
        # ⚑ NOTES-B9 flag 1's first site. "About a tenth" and "four steps …
        # ten-thousandth" are the same arithmetic the bench runs, and the legal
        # line hedges the ratio. Checked and left; see the docstring.
        "reveal": "There is not enough energy left. Only about a tenth of what "
                  "one level holds passes to the next, so after four steps you "
                  "are down to a ten-thousandth of what the plants captured. A "
                  "predator at the sixth level would have to hunt an area the "
                  "size of a county to feed itself, and no such animal exists "
                  "— the arithmetic forbids it.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §14's pre-allocation, and the two beliefs Design's `#s-think`
    # quotes. Both statements are her own bytes, page lines 187 and 191, in
    # register voice.
    #
    # ⚠️ The `ECO` prefix row is NOT yet open in
    # `docs/ks3/misconception-register.md` — see the docstring. That file is not
    # this pass's to edit; the two rows that belong in it are reported.
    #
    # ⛔ `ECO-12` MUST NOT BE MINTED by any B9 pass. The register permanently
    # reserves it ("`ECO-12` — is `NOS-04`"), and NOTES-B9 §4's instruction to
    # open the family with twelve ids is superseded by that reservation.
    #
    # Both `confronted_by` values resolve against the BUILT page (MRB-244):
    # `s-think` is the confrontation block's emitted anchor. Both `elicited_by`
    # values are `s-ladder`, which is where each belief is offered as something
    # to commit to — rung 1 option B and rung 2 option A respectively.
    "misconceptions": [
        {"id": "ECO-01",
         "statement": "The arrow points at what the animal eats.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "ECO-02",
         "statement": "Ninety per cent of the energy is lost at each level.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B9, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ "trophic level" is included although the page never uses the phrase:
    # the page says "level" throughout and GCSE says "trophic level", so the
    # chip is where the two are joined. It is glossed, not taught.
    "vocabulary": [
        {"term": "food chain",
         "definition": "One route through an ecosystem, showing which organism "
                       "is eaten by which.",
         "note": "The arrows show the direction energy travels."},
        {"term": "food web",
         "definition": "All the feeding routes in an ecosystem drawn on top of "
                       "each other.",
         "note": "The truthful picture. A chain is one thread pulled out of "
                 "it."},
        {"term": "producer",
         "definition": "An organism that builds its own food rather than "
                       "eating, so energy enters the living world through it.",
         "note": "Plants and algae. Always at the bottom."},
        {"term": "consumer",
         "definition": "An organism that gets its energy by eating other "
                       "organisms.",
         "note": "Primary eats producers, secondary eats primary, and so on "
                 "up."},
        {"term": "decomposer",
         "definition": "A bacterium or fungus that feeds on dead material and "
                       "droppings, returning the minerals to the soil.",
         "note": "Underneath every level, not on the end of the chain."},
        {"term": "trophic level",
         "definition": "A feeding level in a chain, counted from the producers "
                       "upwards.",
         "note": "The GCSE name for what this lesson calls a level."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and every `<svg>` is chrome. NOTES-B9
    # flag 17 asks for a drawn food web and is not dropped by this; declaring a
    # slot the page never references would invent a sourcing task in
    # `docs/ks3/diagram-manifest.md`.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b9/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md §5. The
        # read sites are listed in the docstring; `startChain`, `shown`,
        # `everTopped`, `energy_unit` and `pct_suffix` are all deliberately
        # absent and each has its own reason there.
        {"type": "chain-ledger", "id": "follow-the-energy-up",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · climb the chain",
         "heading": "Follow the energy up",
         "prompt": "Ten thousand kilojoules of sunlight energy captured by the "
                   "producers at the bottom. Step up one level at a time and "
                   "watch what arrives — and where the rest of it went.",
         # Design's mono line beside the heading (page line 500). `before`
         # carries both placeholders because the denominator follows the tab —
         # four levels on the field and the wood, five on the sea — and
         # `_KIND_HEAD_TOTAL` seeds the resting value from `chains[0]`.
         "progress": {"before": "level {n} of {total}",
                      "after": "top of the chain"},

         "tabs_label": "The chain",
         # ⚖️ TEN THOUSAND IN, AND A FACTOR OF TEN. B9 owns the trophic 10:1 for
         # the whole key stage (schema §0.7) and `r_chain_ledger` refuses any
         # other factor. Seven authored strings on this page would become false
         # if it moved; see the docstring.
         "start_kj": 10000,
         "factor": 10,
         "chains": CHAINS,

         "step_label": "Who eats them?",
         "step_spent_label": "Nothing above this",
         "reset_label": "Back to the producers",
         # ⚖️ THREE FRAGMENTS, TWO COMPUTED FIGURES, NO PER-CHAIN PROSE. The
         # amount and the percentage are derived from the chain's own length,
         # which is why the four-level chains land on "10 … 0.1%" and the sea
         # chain on "1 … 0.01%" out of one expression. Design's page lines 515
         # to 517, split at the two numbers.
         "verdict": {
             "lead": "Ten thousand kilojoules entered at the bottom and ",
             "mid":  " arrived here — ",
             "tail": "% of it. Add one more level and there would be a tenth "
                     "of that again, which is not enough to build an animal "
                     "out of. That is the whole reason chains stop.",
         }},

        # #s-roles — the band panel, and the section that discharges the first
        # half of KS3.B.ECO.01a. Rail stop 3, mirroring `s-bench`.
        #
        # ⚠️ `close` renders AFTER the nested key fact, where Design draws it
        # before. `r_rule()` is the engine pass's and is not this module's to
        # edit; reported. See the docstring's last section.
        {"type": "rule", "anchor": "s-roles",
         "eyebrow": "Everyone has a job title",
         "statement": "A web is chains that share their members.",

         "cards": ROLE_CARDS,

         # Design nests the key fact inside this section (page lines 173–176)
         # on the CARD ground with the 5px accent offset shadow. `card`, because
         # the section itself is `--ks3-band` and band on band is invisible —
         # the same arrangement and the same reason as b7-01's and b8-01's.
         "key_fact": {"ref": "arrows-follow-the-energy", "ground": "card"},

         # The web-versus-chain paragraph, page line 171. It is the only place
         # in the lesson that says what a WEB is, which is half the title.
         "close": "A food chain is one route through an ecosystem. A food web "
                  "is all the routes at once, drawn on top of each other, "
                  "because almost nothing eats only one thing and almost "
                  "nothing is eaten by only one thing. The web is the truthful "
                  "picture; the chain is a single thread pulled out of it so "
                  "it can be talked about."},

        {"type": "misconception", "id": "the-arrow-and-the-ninety-per-cent",
         "anchor": "s-think", "targets": "ECO-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-roles on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 175
    # and identical to payload schema §12's b9-01 entry.
    "key_facts": [
        {"id": "arrows-follow-the-energy",
         "text": "The arrows in a food chain show the direction energy "
                 "travels, so they point from the organism being eaten to the "
                 "organism eating it. Only about a tenth of the energy at each "
                 "level reaches the next, which is why chains are short and "
                 "top predators are rare.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, schema
        # §3), so it is a `confrontation` and not a `predict`, it is not a rail
        # stop, and it emits no completion contract. Contract R1's `predict`
        # branch applies where `#s-think` gates a reveal behind a commitment;
        # no B9 page does.
        {"id": "the-arrow-and-the-ninety-per-cent",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "ECO-01",
         "statements": [
             # ECO-01. The two `<em>` runs are kept — `rich()` renders them —
             # because the contrast between "eats" and "energy travels this
             # way" is the whole paragraph and italics are how it is made.
             {"quote": "The arrow points at what the animal eats.",
              "body": ["Draw it that way and every arrow in the diagram is "
                       "backwards. The arrow is not saying <em>eats</em>; it "
                       "is saying <em>energy travels this way</em>, so it "
                       "always points from the eaten towards the eater — grass "
                       "to rabbit, rabbit to fox. The fox does not send "
                       "anything to the rabbit. Once you read arrows as energy "
                       "rather than as appetite, several things become easy: "
                       "you can see instantly which organisms are producers, "
                       "because nothing points into them from another "
                       "organism; you can count how many steps energy has "
                       "taken from the Sun; and a food web stops looking like "
                       "a tangle and starts looking like a map of where the "
                       "energy goes. Examiners mark arrow direction, and it is "
                       "the single most common lost mark in this topic."]},
             # ECO-02, and the reason the bench is upstream of it in the
             # document: "follow it" is a real instruction about an instrument
             # the student has already climbed. The `Conservation of energy`
             # link loses its tag and keeps every word — the link TEXT is
             # already the lesson title, and the edge is in `requires`.
             #
             # ⚖️ "It has left this chain, which is a different claim" is the
             # sentence the whole misconception turns on, and it is what makes
             # this a correction of a WORD rather than of a number. The ninety
             # per cent is not in dispute anywhere on the page; where it went
             # is.
             {"quote": "Ninety per cent of the energy is lost at each level.",
              "body": ["Lost is the wrong word, and you have already met why "
                       "in Conservation of energy: energy is never destroyed, "
                       "so it has to be somewhere. Follow it. Most of it was "
                       "released by respiration and ended up warming the "
                       "surroundings — a rabbit spends most of what it eats "
                       "simply staying alive and staying warm. Some passes out "
                       "undigested and goes to the decomposers, along with "
                       "everything in the rabbit when it eventually dies. A "
                       "little is in parts the fox does not eat. Nothing has "
                       "gone missing; it has left this chain, which is a "
                       "different claim. The reason the number matters is not "
                       "bookkeeping but shape: it makes each level about a "
                       "tenth the size of the one below, and after four or "
                       "five levels there is nothing left to build an animal "
                       "out of."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN AS DRAWN, RUNG 2 REPAIRED. rung 1
    # correct 11w against 13 / 8 / 12 (not strictly longest); rung 2 correct 19w
    # against 3 / 13 / 10 as delivered, which tripped BOTH arms of the gate, and
    # 20 / 21 / 21 after each distractor is rewritten as a wrong RULE in the
    # correct answer's own shape. The correct option, `answer`, Design's option
    # ORDER and every one of her six corrections are byte-identical. Full
    # working, with the before and after of all three, in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Read the arrows",
            "q": "A food chain is written: lettuce, slug, hedgehog. Which way "
                 "do the arrows point, and why?",
            # Design's four, untouched. Three of them name a DIRECTION and give
            # a reason for it and the fourth denies that direction is a claim
            # at all — four wrong rules of the same size about the same thing,
            # so a student cannot pick by shape.
            #
            #   A  correct
            #   B  ECO-01 — "the arrows show what each animal eats"
            #   C  authored belief: energy travels both ways along a chain,
            #      because eating is a two-way relationship
            #   D  authored belief: arrow direction is a drawing convention
            #      rather than a claim about the world
            "options": [
                "Lettuce to slug to hedgehog — the arrows follow the energy",
                "Hedgehog to slug to lettuce — the arrows show what each "
                "animal eats",
                "Both ways, because energy moves in both directions",
                "It does not matter as long as the organisms are in order",
            ],
            "answer": 0,
            "feedback": {
                1: "That is the most common error in this topic. The arrow "
                   "means energy travels this way, not this one eats that one.",
                2: "Energy does not move back down a chain. A hedgehog gives "
                   "nothing to a slug except, eventually, material for the "
                   "decomposers.",
                3: "It matters, and it is marked. An arrow drawn the wrong way "
                   "says something false about where the energy goes.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Only about 10% of the energy at one level reaches the next. "
                 "What happened to the other 90%?",
            # ⊕ MRB-177, 18 Aug 2026. Options 0, 2 and 3 rewritten as wrong
            # RULES in the correct answer's shape — where the energy went, and
            # what follows from its having gone there. Option 1 and `answer`
            # are Design's, unchanged. Each rewrite keeps Design's own clause
            # verbatim at the front.
            #
            #   A  ECO-02 — the energy is "lost", read as destroyed
            #   B  correct, Design's, unchanged
            #   C  authored belief: the ninety per cent is the parts of the
            #      food the animal could not get at
            #   D  authored belief: energy can be "used up" — movement consumes
            #      it out of existence
            "options": [
                # 20w. Was "It was destroyed" (3w). The added clause is the
                # conservation claim head-on, which is what the correction's
                # first sentence answers.
                "It was destroyed as it passed up the chain, so there is less "
                "energy in the world than there was",
                # 19w — Design's, unchanged.
                "Most was released by respiration and warmed the surroundings; "
                "the rest went to decomposers in droppings and dead material",
                # 21w. Was "It stayed in the parts of the plant the animal
                # could not reach" (13w). Now states the leftovers reading as a
                # rule, which "most of the loss is respiration, not leftovers"
                # contradicts precisely.
                "It stayed in the parts of the plant the animal could not "
                "reach, so the loss is leftovers on the ground",
                # 21w. Was "It was used up in movement and no longer exists"
                # (10w). The consequence the belief licenses: activity as the
                # thing that destroys energy.
                "It was used up in movement and no longer exists, so an active "
                "animal passes on less than a still one",
            ],
            "answer": 1,
            # All three unchanged from Design, and each still answers exactly
            # the belief its rewritten distractor states — which is the test of
            # whether the rewrite changed what the question measures.
            "feedback": {
                0: "Energy is never destroyed — that rule has no exceptions, "
                   "including in biology. It went somewhere; the question is "
                   "where.",
                2: "Some did, and that is a real part of the answer — but most "
                   "of the loss is respiration, not leftovers.",
                3: "Movement transfers energy to the surroundings by friction "
                   "and warming. Used up is not a thing energy can be.",
            }},
        # ⚖️ Criterion 5 is the rung's whole point and it is why the question
        # asks for the impossible case as well as the shape. "Impossible in a
        # stable ecosystem" rather than "unusual" is the difference between a
        # student who has understood the arithmetic and one who has memorised a
        # pyramid.
        "explain": {
            "title": "Rung 3 · Explain the shape",
            "q": "In almost every ecosystem there are far more producers than "
                 "primary consumers, and far more primary consumers than top "
                 "predators. Explain why, and say what would have to be true "
                 "for an ecosystem to have more foxes than rabbits.",
            "field_label": "Your explanation",
            "placeholder": "Only about a tenth of the energy…",
            "success": [
                "Says only about a tenth of the energy at each level is passed "
                "on to the next.",
                "Says the rest is used in respiration or passed to decomposers "
                "rather than destroyed.",
                "Says each level therefore has far less energy available to it "
                "than the one below.",
                "Concludes that fewer organisms, or smaller ones, can be "
                "supported at each step up.",
                "Says more foxes than rabbits is impossible in a stable "
                "ecosystem — there would not be enough food energy to support "
                "them — rather than merely unusual.",
            ]},
        # ⚑ NOTES-B9 flag 1 again, and its strictest site: criterion 5 MARKS a
        # student for refusing to treat the ratio as exact. That is the hedge
        # made assessable rather than merely printed, and it is why the legal
        # line and this criterion have to say the same thing.
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A country wants to feed more people from the same farmland. "
                 "An adviser suggests converting land currently used to raise "
                 "cattle over to growing wheat. Explain the energy argument in "
                 "favour, and give one honest limitation of it.",
            "field_label": "Your answer",
            "placeholder": "Eating the wheat directly means…",
            "success": [
                "Says eating crops directly puts people at the first consumer "
                "level rather than the second.",
                "Says a level is lost when the crop is fed to cattle, so about "
                "a tenth as much energy reaches people.",
                "Concludes the same land therefore feeds more people as wheat "
                "than as beef.",
                "Gives a genuine limitation — for example that much grazing "
                "land is too poor, steep or wet to grow crops on, or that a "
                "diet needs more than energy.",
                "Avoids treating the 10% figure as exact, or notes that it is "
                "an average rather than a measurement.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Producers capture energy from sunlight; consumers get theirs "
                "by eating; decomposers release the rest back. Arrows point in "
                "the direction energy travels, from eaten to eater. About a "
                "tenth of the energy at each level reaches the next, the rest "
                "having been used in respiration or passed to decomposers, "
                "which is why food chains are short and a food web has far "
                "more organisms at the bottom than at the top.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B9 flag 4 lives in the last two sentences and is checked and left;
    # the working is in the docstring. ⚖️ MRB-225 holds: the layer applies the
    # lesson's own arithmetic to land use and to body size and retracts nothing
    # above it. Design's own hedge — "that is not an argument that nobody
    # should eat beef" — is load-bearing and must not be trimmed: it is what
    # keeps a science page from making a dietary argument it cannot support.
    "stretch": [
        {"type": "explainer", "id": "what-the-tenth-decides-about-land",
         "text": "The same arithmetic decides what a country can feed itself "
                 "on. A hectare of wheat eaten as bread feeds people at the "
                 "first consumer level; the same hectare grown as feed for "
                 "cattle and eaten as beef feeds them at the second, with "
                 "about a tenth as much arriving. That is not an argument that "
                 "nobody should eat beef — cattle graze land that will not "
                 "grow wheat, and grass is inedible to us — but it is why the "
                 "two are not interchangeable, and why the question of how "
                 "much land a diet requires has a hard number attached to it. "
                 "The same rule explains something odder at sea: whales are "
                 "enormous, and the largest of them feed on krill, only two "
                 "levels up. An animal that size at the fifth level is "
                 "impossible, so the biggest animals that have ever existed "
                 "eat some of the smallest."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to build a chain from your own local wildlife?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 300) and nothing in it is a safety
    # instruction — it is a note about how far the bench's figures can be
    # trusted. Routing it through `safety_note` would print it in the treatment
    # reserved for "never light a candle without an adult".
    #
    # ⚑ NOTES-B9 flag 1's fourth and last site, and the one that does the real
    # work: it gives the honest range. It must keep saying the same thing as
    # rung 4's fifth criterion, which MARKS the same hedge.
    "convention_note": "The tenth-of-the-energy rule is a teaching average. "
                       "Real transfer efficiencies range from a few per cent "
                       "to around twenty depending on the organisms and the "
                       "ecosystem, and the figures on the bench are rounded to "
                       "make the pattern readable rather than taken from a "
                       "particular study.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is a quantitative model whose figures the student is explicitly
    # told to distrust at the edges, and rung 4 asks for an argument AND an
    # honest limitation of it — which is the analysis-and-evaluation strand
    # rather than an experimental one. Nothing on this page is measured, so
    # `experimental-skills` and `measurement` are not claimed.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
