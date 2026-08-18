"""B9 L4 — Pollinators and food security (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b9/b9-04-pollinators-and-food-security.dc.html` (521 lines), her
author's notes `docs/ks3/design-reference/b9/NOTES-B9.md`, and the B9 payload schema
`docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md` §0, §1, §2, §3, §4, §8, §11, §12,
§14 and §15, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the two items listed under "What could not be lifted", and except rung
2's three distractors, which MRB-177 required to be rebuilt at the distractor —
the working is below and the corrections attached to them are untouched. The
twelve foods, the four `WHO_CARDS`, both marked rungs and both self-marked
rungs came out of the page's own `FOODS`, `WHO_CARDS`, `RUNGS` and `SELF_RUNGS`
arrays via `node tools/extract_design_payload.js`, not off a keyboard.

── `covers`: ECO.02 whole, and ECO.01's fourth clause ────────────────────

`KS3.B.ECO.02` reads, in full: *the importance of plant reproduction through
insect pollination in human food security*. This lesson is that statement and
nothing else is, so it is owned whole.

`KS3.B.ECO.01d` — *"Insect pollinated crops as a case of interdependence"* — is
the sub-clause `ks3_data/substatements.py` minted for exactly this page.
`build_ks3.validate()` enforces exactly-once ownership across the key stage, so
it is claimed here and the PARENT `KS3.B.ECO.01` is not: (a), (b) and (c) belong
to b9-01, b9-02 and b9-03, and a lesson that claimed the parent would take all
four clauses off its three siblings.

── The instrument: two bars that must never become one ───────────────────

`#s-bench` is `supermarket-shelf`, on `ks3-block ks3-dark ks3-practical` (page
line 105), so `practical` is MEASURED from Design's own markup rather than
inferred from the kind name — payload schema §0 rule 2.

⚖️ **THE GAP BETWEEN THE TWO BARS IS THE ENTIRE LESSON.** Twelve foods, each
with a share of the shelf's calories and a share of its vitamins and minerals,
and a pollinator-dependence fraction that decides how much of the crop survives.
Both share columns sum to 100, so each bar is a clean percentage of its own
total, and with the pollinators gone the two totals go in visibly different
directions:

    calories   22 + 20 + 14 + 12          =  68.0   the four that need no insect
             + 8×0.85 + 4×0.1 + 2×0.1     =   7.4
             + 3×0.3 + 6×0 + 2×0.2        =   1.3
             + 1×0.5 + 6×0                =   0.5
                                            ─────
                                             77.2   → 77%

    vitamins    4 +  3 +  4 +  8          =  19.00
             + 9×0.85 + 10×0.1 + 11×0.1   =   9.75
             + 12×0.3 + 9×0 + 12×0.2      =   6.00
             + 3×0.5 + 15×0               =   1.50
                                            ─────
                                             36.25  → 36%

Seventy-seven against thirty-six. Nobody starves on 77% of the calories, and
nobody stays healthy on 36% of the vitamins, and the `none` note says both of
those things in one sentence with the two computed figures in it. The renderer
REFUSES a payload whose two bars land on the same figure, and refuses one where
the vitamin bar falls less far than the calorie bar, because either would be the
lesson deleted rather than a number changed.

⛔ **THE TWO NUMBERS ARE NOT AUTHORED ANYWHERE.** `notes["none"]` carries `{cal}`
and `{vit}` and `shared/ks3.js` fills them from the same arithmetic the bars are
drawn from. A note quoting `77%` as a literal would be a note that is wrong on
the *half* setting and wrong again the moment a food's share is corrected;
`_b9_placeholders()` fails the build if either brace is missing.

⚖️ **AND THE DIAL DOUBLES AS THE TEACHING LABEL.** At full pollination each tile
prints the food's `how` — *wind-pollinated*, *grown from tubers*, *pollinated by
midges* — instead of a status. A student therefore reads WHY wheat is about to
survive before finding out that it does, and the swap to *gone* is a change of
words in the same mono line rather than a change of component. That is Design's,
it is what the parity row on `.ks3-ss-foodstatus` measures, and it is why every
food declares a `how` even though four of them will never move.

⚠️ **THREE STATES, TWO BUTTONS, AND NO PATH FROM `half` BACK TO `all`.** *Remove
every insect pollinator* toggles `none ↔ all`; *Lose half of them* sets `half`
unconditionally and nothing returns from it but a reload. Measured off Design's
`onToggle`/`onHalf` (page lines 494–497) and left alone — inventing a third
button would be inventing a control.

⚠️ **`progress` opens on `all`, and the order is load-bearing.**
`_progress_readout` prints the FIRST authored state at rest, so a map that
opened on `none` would ship a page saying the pollinators were gone while the
shelf was still intact. `all` is written first for that reason and not for
tidiness.

── The stage predicate is MONOTONIC, and Design's is not ─────────────────

Design's own `isDone()` reads:

    if (id === 's-bench') return s.level !== 'all';
    if (id === 's-who')   return s.level !== 'all';        // page lines 385–386

which UNTICKS both stops the moment a student presses *Bring the pollinators
back*. Under MRB-208 the rail is completion-based and what a student has found
out cannot be un-found by pressing restore, so the engine pass made the
predicate monotonic (`shared/ks3.js`, `wireSupermarketShelf`'s `ever` flag):
the stop ticks the first time `level` leaves `all` and stays ticked.

This is contract R4 — a defect on an approved page that a ruling already covers
is corrected, not reproduced — and the ratchet is the engine's, not this
module's. It is recorded here because `done_when: "pollinators_removed"` is
authored against the corrected behaviour: the condition the page can reach is
*the pollinators have been removed at least once*, not *are removed now*.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ──────────────────

Design draws four (page lines 306–312) and `docs/ks3/rail-manifest.md` line 101
records them: `s-hook s-bench s-who s-ladder`, with `s-who=s-bench`.
`#s-who` is an eyebrow, a display statement, four static cards and a key fact —
no control, no commitment, no field, no reveal — and Design completes it by
pointing her rail-level `isDone()` at the bench's own state, one section to the
left. That relationship is a MIRROR, `wireRail`'s `paint()` resolves it at rail
level where Design resolves it, and `ks3_parity.check_rail_matches_design` fails
the build if three ship. `label` and `short` are Design's own `RAIL` and
`RAIL_SHORT` strings, SHELF / "The shelves" and WHO / "Who pollinates" included.

`#s-think` and `#s-keynote` are on NO rail, and that is Design's too. `#s-think`
here is static markup — two quotes, two bodies, an amber-topped divider, no
options and no reveal — so it is a `confrontation` under payload schema §3 and
contract R1's `predict` branch does not reach it.

── What could not be lifted byte-identical, and why ─────────────────────

1. **`b3-04` in the hook reveal.** Design writes *"which is the distinction
   `<a href="b3-04-when-diet-goes-wrong.html">b3-04</a>` was about."* A student
   cannot resolve a slot code, and printing one is exactly the platform leakage
   §8.10 exists to stop. `rich()` allows `<em>` and `<strong>` and nothing else,
   so no hyperlink survives anywhere on the page in any case — and where the
   link TEXT is already a lesson title that costs nothing but the tag, which is
   what happens to the identical link in `#s-think`'s first body. Here the link
   text is a CODE, so dropping the tag alone would leave `b3-04` in front of a
   student:

       Design:  which is the distinction <a …>b3-04</a> was about
       Built:   which is the distinction When diet goes wrong was about

   The destination is not lost — `when-diet-goes-wrong` is carried as a real
   `references` edge, which is Design's own "Connects to" card and is where the
   engine puts cross-lesson navigation.

   ⚠️ The inline `style="color: var(--ks3-alert);"` on that anchor goes with the
   tag, and should. Amber is a wrong IDEA being confronted (§8), and this is a
   navigation link inside a correct answer.

2. **Rung 2's three distractors.** MRB-177, and the working is in the next
   section. No correction, no correct option, no option ORDER and no `answer`
   index moved; three wrong options were rebuilt into the shape the correct one
   is already in.

⚑ **The `b9-03` edge is `requires`, not `references`, and it is not
duplicated.** Design's "Before this lesson" card names *Disturbing a food web*
and *A balanced diet* and both are in `requires`. b9-03 puts bees in its web
with **no feeding line at all** — they are a service, not a meal — and removing
them still empties the wood; this lesson is the payoff of that, and the edge is
the same edge whichever key it is written on. b8-01 set the precedent for not
writing a slug twice, and nothing on this page prints `b9-03` as a code.

── ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN, RUNG 2 REBUILT ───────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor by
≥4 words or by ≥1.4×.

**Rung 1 is clean as Design drew it and is untouched.** All four options are a
single food name — Wheat / Apples / Almonds / Strawberries — so every option is
one word, the correct one cannot be strictly the longest, and a student cannot
pick by shape. This is the second construct the MRB-177 ruling names: on a
"which of these is X?" rung the correct answer names an ITEM rather than a rule,
so its distractors name items. Same principle, different shape. Nothing here
needed rebuilding and nothing was rebuilt.

**Rung 2 as delivered was a live tell, and it is the exact construct the ruling
describes.** Design's correct option states a RULE — subject (*most calories*),
condition (*come from wind-pollinated cereals*), consequence (*so the real loss
would be vitamins and variety rather than energy*) — and all three distractors
stated a short wrong REASON in one clause. A rule needs three parts and a reason
needs one:

    Design   A  8w · B correct 18w · C 12w · D 7w
             correct is strictly longest, gap 6 ≥ 4        ✗ TELL

So the distractors are rebuilt as WRONG RULES in the same three-part shape, each
carrying the belief it always carried, with the misconception as the consequence:

    Built    A 17w · B correct 18w · C 16w · D 17w
             gap 1, ratio 1.06                             ✓ clean

The construct is what changed, not the threshold, and the correct answer was not
shortened by a word. Each rebuilt option, its belief and its provenance:

  * **A** — `ECO-07`, this lesson's own register entry, in the student's own
    voice. Design: *"Nothing — almost all our food is insect-pollinated"*.
    Built: the same claim stated as a rule, so that what a student rejects is a
    RULE about which crops need insects rather than a bare exclamation. The
    shelf is the evidence and Design's correction already says so.

  * **C** — belief written for this rung; no register entry supplies it, and it
    is deliberately NOT minted. *"Bees are not in decline, so the claim is
    about nothing"* is a wrong idea about EVIDENCE rather than about pollination,
    it is confronted only in this one correction, and the standing rule is that
    nothing is registered ahead of the lesson that needs it. Design's correction
    is the one that separates managed honeybees from wild pollinators and it is
    untouched.

  * **D** — belief written for this rung, and it is the one the *Going further*
    layer exists to price: *"hand pollination does the same job, so it is a
    substitute"*. Not registered, for the same reason as C. Design's correction
    — *"a measure of the loss, not a solution to it"* — is untouched and is what
    makes the Sichuan paragraph land.

Rungs 3 and 4 are self-marked, carry five criteria each and are lifted whole:
`length_tell()` skips them, having no options to measure.

── Misconceptions: ECO-07 and ECO-08, and one legal absence ─────────────

⚠️ **The `ECO` prefix row does not yet exist in
`docs/ks3/misconception-register.md`** — grepped, and the only `ECO` string in
the file is the permanent reservation *"`ECO-12` — is `NOS-04`."* That file is
not this pass's to edit (contract §0), so the two statements are authored here in
register voice, byte-identical to Design's two quoted beliefs (page lines 269 and
274), and are reported for whoever opens the row. No gate resolves an id against
the register file, so the lesson builds either way; what is at risk is the
register's completeness, not this page.

Payload schema §14 pre-allocated `ECO-07` and `ECO-08` to this lesson before
dispatch, so six parallel passes could not collide. Neither is renumbered.

Both `confronted_by` values resolve against the BUILT page (MRB-244): `s-think`
is the confrontation block's emitted anchor. `#s-who`'s four cards reinforce
`ECO-08` and are deliberately not named as its `confronted_by` — the band states
the correct account, and the belief is taken apart in `#s-think`, which is where
the student is standing when it happens.

`ECO-07` declares `elicited_by: "s-hook"` and that is measured: hook option A,
*"Almost all crops would fail and there would be famine"*, is the belief in the
student's own words, and a student commits to it or declines to before the page
names it. Under MRB-248 a present value must be true on its own page, and this
one is.

`ECO-08` declares **no `elicited_by` at all**, and that is measured rather than
forgotten. Nothing on this page asks a student to state that keeping a hive is
conservation, or offers it as an option — the four hook options are about the
food supply, and the ladder is about crops and about the poster's claim. The
belief arrives already held and is confronted directly. Absence is legal under
MRB-248 for exactly this case, and `RESP-01` and `RESP-05` are the precedent;
inventing an element name to fill the key would be worse than the gap.

⚑ For Mide's science gate — every NOTES-B9 flag landing on THIS lesson, and
  what was checked against it. Four flags, four checked, **none corrected**:

  * flag 9   **Opening the lesson by naming a false quotation** (the hook).
             CHECKED AND LEFT. The page never asserts the quotation; its own
             second sentence says Einstein *"never said it"*, and the hook's
             whole job is that a claim which is repeated is not thereby true.
             ⚖️ This is the one shape where naming a false claim is safer than
             not naming it: a student has already met this poster, and a lesson
             that taught the correct account without touching the sentence they
             have actually seen would leave the sentence intact. It is Mide's
             call and it is flagged; nothing was softened while it is open.

  * flag 10  **The twelve dependence values, tomatoes at 0.7 and milk at 0.15.**
             CHECKED AND LEFT, and both are defensible as drawn. Tomatoes are
             buzz-pollinated — the flower releases pollen to a specific
             vibration frequency, honeybees cannot produce it and bumblebees
             can, which is why glasshouse growers buy bumblebee colonies rather
             than hives; a 0.7 loss is a claim about YIELD AND FRUIT QUALITY,
             not about whether any fruit sets at all, and glasshouse tomatoes
             set poorly without them. Milk at 0.15 runs through fodder — clover
             and other insect-pollinated legumes in leys and silage — and 15%
             is a small enough number to be honest about an indirect route.
             ⚖️ Both are directional and the page's legal line already calls
             every share illustrative. The two numbers are load-bearing in the
             OPPOSITE direction to the misconception: milk at 0.15 and potatoes
             at 0 are what stop the shelf overstating the loss, which is the
             whole argument of `ECO-07`.

  * flag 11  **"More managed honeybee colonies now than fifty years ago"**, and
             wild pollinators as the ones declining (`#s-think`, and the first
             `WHO_CARDS` entry). CHECKED AND LEFT, and the framing is the right
             one. Global managed colony counts have risen over that period —
             the trend is driven by regions outside Europe and North America,
             and Design's sentence says *"in the world"* rather than *"in
             Britain"*, which is the clause that makes it true. The decline
             claim is about wild species: Britain's ~250 solitary bee species
             plus the bumblebees, several of which are in serious decline, and
             several of which pollinate crops more effectively than honeybees.
             ⚖️ The two halves are about two different populations and the page
             keeps them apart in every sentence. That separation is `ECO-08`
             and it must not be tidied into one claim about "bees".

  * flag 12  **Hand pollination in Sichuan** (*Going further*). CHECKED AND
             LEFT. The practice is real and long-running in the apple and pear
             orchards there; the CAUSE is genuinely disputed — pesticide use,
             habitat loss and the simple economics of cheap labour all appear in
             different accounts — and Design's paragraph says so in as many
             words rather than using it as a parable. ⚖️ *"Why it started is
             disputed"* is load-bearing and may not be trimmed: without it the
             paragraph becomes the morality tale the sentence exists to refuse.
             What the paragraph does establish is a PRICE, in working days per
             hectare, and that is what makes it a food-security point and not a
             wildlife one.

  * flag 17  **No figures, and it is MEASURED.** `<img>`, `<figure>` and
             `<picture>` each appear ZERO times on this page — grepped, not
             assumed. §4.10 allows an empty `figures` for a lesson carried by
             its interactives. Nothing is declared, because declaring a slot the
             page never references would invent a sourcing task in
             `docs/ks3/diagram-manifest.md`. Flag 17 asks for a drawn food web
             in b9-01 and b9-03 and is not dropped by this — it is Mide's to
             rule on, and it is the strongest outstanding diagram request in the
             biology build.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes six times: *the calories survive and the
variety does not, and that is a serious problem which is not starvation*. Big
question ("you would not starve … you would also never eat an apple"), hook
reveal ("enough energy and a diet that made you ill"), the bench's `none` note
("nobody starves … nobody stays healthy"), the KEY FACT ("cereals supply most of
our calories; insect-pollinated crops supply most of the variety"), `#s-think`'s
first body ("enough energy and widespread deficiency diseases"), rung 2's correct
option and the key note all say the same thing at the same size. Nothing above is
walked back below, and the *Going further* layer adds a price and retracts
nothing.

── Keys this pass authors and where each is read (contract R5) ──────────

    progress    {"all","half","none"}   `_b9_progress` → `_KIND_HEAD_FROM`
                                        → `setCountState()` in shared/ks3.js
    foods       name/dep/cal/vit/how    `data-shares` + `data-how` per tile
    bars        label + colour_token    `--ss-fill` on `.ks3-ss-fill`
    notes       all/none/half           `data-notes`, `{cal}`/`{vit}` filled
    remove_label / restore_label        `data-remove-label` / `-restore-label`,
                                        swapped on the toggle each draw
    half_label                          the second button's face
    gone_label / unaffected_label /
    part_label                          the three tile statuses after loss > 0

⚠️ **The three status labels ARE authored** even though `r_supermarket_shelf`
defaults them to the identical bytes. They are student-facing strings that came
off Design's own `renderVals()` (page lines 434–436), and a default is the
engine's opinion about content: the day someone changes the fallback, an authored
page should not change with it.

⛔ **NO RUNTIME STATE IS AUTHORED** (payload schema §0 rule 3). Design's state bag
holds `hookChoice`, `level`, `answers`, `text`, `checked`, `ticks` and `active`;
every one is a value the runtime owns, and under R5 a key with no read site fails
`ks3_key_audit.py`. The renderer initialises its own state and `level` opens on
`all`.

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
instrument class at (0,1,0). That is the engine pass's problem rather than this
module's, and it is recorded here because this payload is what feeds it; as of
MRB-245 `ks3_parity.check_dark_text_specificity()` gates it.
"""

# ── the twelve foods (page lines 316–329) ────────────────────────────────
#
# `dep` is the fraction of the crop lost with NO insect pollinators; `cal` and
# `vit` are this food's share of the shelf's calories and of its vitamins and
# minerals. Both share columns sum to 100 by construction, which is what makes
# each bar a clean percentage of its own total.
#
# ⚖️ THE FIRST FOUR ARE THE ARGUMENT. Wheat, rice and maize are wind-pollinated
# grasses and potatoes are grown from tubers, so `dep` is 0 on all four and they
# carry 68 of the shelf's 100 calorie points between them. `r_supermarket_shelf`
# REFUSES a shelf with no `dep: 0` food, in those words, because without one the
# bench teaches "no bees, no food" — the belief `#s-think` exists to break.
#
# ⚖️ AND ALMONDS AND COCOA ARE THE OTHER END. `dep: 1` is a crop that GOES, not
# one that dims, and the renderer refuses a shelf where nothing reaches 1 for the
# same reason: "gone" is the tile state the lesson turns on. Cocoa is pollinated
# by midges rather than by bees, which is `ECO-08`'s point made as a data row.
#
# ⚑ NOTES-B9 flag 10 lands on `Tomatoes` (0.7) and `Milk` (0.15). Both checked
# and left; the working is in the docstring.
FOODS = [
    {"name": "Bread (wheat)", "dep": 0, "cal": 22, "vit": 4,
     "how": "wind-pollinated"},
    {"name": "Rice", "dep": 0, "cal": 20, "vit": 3,
     "how": "wind-pollinated"},
    {"name": "Sweetcorn (maize)", "dep": 0, "cal": 14, "vit": 4,
     "how": "wind-pollinated"},
    {"name": "Potatoes", "dep": 0, "cal": 12, "vit": 8,
     "how": "grown from tubers"},
    {"name": "Milk", "dep": 0.15, "cal": 8, "vit": 9,
     "how": "cattle feed partly insect-pollinated"},
    {"name": "Apples", "dep": 0.9, "cal": 4, "vit": 10,
     "how": "insect-pollinated"},
    {"name": "Strawberries", "dep": 0.9, "cal": 2, "vit": 11,
     "how": "insect-pollinated"},
    {"name": "Tomatoes", "dep": 0.7, "cal": 3, "vit": 12,
     "how": "bumblebee-pollinated"},
    {"name": "Almonds", "dep": 1, "cal": 6, "vit": 9,
     "how": "entirely insect-pollinated"},
    {"name": "Broccoli", "dep": 0.8, "cal": 2, "vit": 12,
     "how": "insect-pollinated"},
    {"name": "Coffee", "dep": 0.5, "cal": 1, "vit": 3,
     "how": "partly insect-pollinated"},
    {"name": "Chocolate (cocoa)", "dep": 1, "cal": 6, "vit": 15,
     "how": "pollinated by midges"},
]

# ── the four cards in the band (page lines 331–336) ──────────────────────
#
# Design's `kind` is the mono accent tag and maps to `role`, which is the slot
# `_rule_card()` reads for it. All three strings per card survive unchanged and
# nothing is joined.
#
# ⚖️ THE FOUR CARDS ARE `ECO-08` STATED POSITIVELY. Farmed / in trouble /
# overlooked / what they need — the honeybee is named first and set aside first,
# so that "save the bees" has somewhere to land other than a hive. The fourth
# card is the answer to the question the misconception asks badly, and it is a
# landscape answer, which is why this sits in a food security lesson.
#
# ⚑ NOTES-B9 flag 11 lands on the first card. Checked and left; see the docstring.
WHO_CARDS = [
    {"role": "Farmed, not wild", "name": "Honeybees",
     "body": "Kept in hives and moved to crops by lorry. Numerous, useful, and "
             "not the group that is disappearing — there are more managed "
             "colonies now than fifty years ago."},
    {"role": "The ones in trouble", "name": "Wild bees",
     "body": "Around 250 solitary bee species in Britain, plus the bumblebees. "
             "Several are better at pollinating crops than honeybees, and "
             "several are in serious decline."},
    {"role": "Overlooked", "name": "Hoverflies, moths and beetles",
     "body": "Hoverflies work in colder weather than bees will, moths "
             "pollinate at night, and cocoa depends on tiny midges. "
             "Pollination is not a bee monopoly."},
    {"role": "What they need", "name": "Flowers, nests, fewer sprays",
     "body": "Flowers across the whole season rather than one crop’s brief "
             "bloom, rough ground and hedges to nest in, and insecticides used "
             "sparingly."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 157 character for character.
    "slug":        "pollinators-and-food-security",
    "title":       "Pollinators and food security",
    "discipline":  "biology",
    "unit":        "ecosystems-and-interdependence",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # ECO.02 whole, plus ECO.01's fourth clause. The PARENT ECO.01 is not
    # claimed — see the docstring; (a), (b) and (c) are b9-01, b9-02 and b9-03's
    # and `build_ks3.validate()` enforces exactly-once ownership.
    "covers":      ["KS3.B.ECO.02", "KS3.B.ECO.01d"],
    # Named, used, and owned elsewhere. REP.02a is b5-06's flowers-and-
    # pollination, which is where a student met what pollination physically IS;
    # this page never re-teaches the mechanism and starts from the service.
    # NUT.03 is b3-01's balanced diet, which the whole vitamin argument leans on
    # and which the hook reveal and `#s-think` both point back at.
    "touches":     ["KS3.B.REP.02a", "KS3.B.NUT.03"],
    "beyond_statutory": False,
    "threads":     [{"id": "interdependence", "level": 3},
                    {"id": "cells-and-systems", "level": 1}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. b9-03 is the setup: it
    # puts bees in an eight-species web with no feeding line at all and removing
    # them still empties the wood. `build_ks3.py` silently skips a slug it
    # cannot find, and both of these build.
    "requires":    ["disturbing-a-food-web", "a-balanced-diet"],
    "assumes":     [],
    # Design's "Connects to" card, in her order. `when-diet-goes-wrong` is also
    # the destination of the two stripped inline links — the hook reveal's slot
    # code and `#s-think`'s title link — so the edge carries both.
    "references":  [{"unit": "B3", "lesson": "when-diet-goes-wrong"},
                    "toxic-build-up-in-a-food-chain"],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Food security, the biological factors threatening it, and "
                   "the trade-offs in intensive and sustainable farming.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "If every insect pollinator vanished tonight, you would not "
                    "starve. You would also never eat an apple, a strawberry, "
                    "an almond, a tomato or a square of chocolate again. Both "
                    "halves of that sentence matter.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them and as `docs/ks3/rail-manifest.md` line
    # 101 records them. `s-who` is the third: no control of its own, so it
    # mirrors `s-bench` and ticks on the shelf's predicate. `short` and `label`
    # are Design's own `RAIL_SHORT` and `RAIL` strings (page lines 306–312).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "The poster",
         "done_when": "committed"},
        # Design's own threshold, kept in substance and corrected in direction:
        # `s.level !== 'all'` (page line 385). The engine's predicate is
        # MONOTONIC — restoring the pollinators does not untick a stop the
        # student has reached — so the condition this names is "the pollinators
        # have been removed at least once". See the docstring.
        {"anchor": "s-bench", "short": "SHELF", "label": "The shelves",
         "done_when": "pollinators_removed"},
        {"anchor": "s-who", "short": "WHO", "label": "Who pollinates",
         "mirrors": "s-bench", "done_when": "pollinators_removed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. C is the correct one
    # and the reveal says so at once.
    #
    # ⚖️ Option A is `ECO-07` in the student's own words, which is why the
    # misconception below names `s-hook` as its `elicited_by`. The student who
    # picks A has stated the belief before the page names it. Option D is the
    # "bees means honey" version and is the shape `#s-who`'s third card answers.
    #
    # ⚠️ The inline link to `b3-04` is resolved to the lesson TITLE — "What
    # could not be lifted" 1 — and the edge is carried in `references`.
    "phenomenon": {
        "kind": "narrative",
        "title": "“If bees disappeared, humans would have four years to live.”",
        # ⚑ NOTES-B9 flag 9. The page names the quotation as false in its own
        # second sentence; nothing here asserts it. See the docstring.
        "prompt": "You have probably seen this on a poster, usually attributed "
                  "to Einstein, who never said it. It is repeated because "
                  "people want a reason to care about bees. The real reason is "
                  "more interesting than the invented one, and it survives "
                  "being checked.",
        "commit": "What would actually happen to the world's food supply?",
        "options": [
            "Almost all crops would fail and there would be famine",
            "Very little would change — farmers would manage",
            "The staple cereals would survive; the fruit and vegetables would "
            "not",
            "Only honey would disappear",
        ],
        "reveal": "The staples would survive. Wheat, rice and maize are "
                  "pollinated by wind and need no insect at all, and they "
                  "supply most of the world's calories. What would collapse is "
                  "almost everything else: the fruit, the nuts, the "
                  "vegetables, the coffee and the chocolate — the foods that "
                  "carry the vitamins and minerals a diet needs. You would "
                  "have enough energy and a diet that made you ill, which is "
                  "the distinction When diet goes wrong was about.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Payload schema §14's pre-allocation. Both statements are Design's own
    # quoted beliefs, byte-identical from page lines 269 and 274, in register
    # voice.
    #
    # ⚠️ The `ECO` prefix row is NOT yet open in
    # `docs/ks3/misconception-register.md` — see the docstring. That file is not
    # this pass's to edit; the statements below are what belongs in it.
    #
    # ⛔ `ECO-12` is permanently reserved by the register as `NOS-04` and is not
    # this lesson's to touch. Neither id below is renumbered.
    #
    # Both `confronted_by` values resolve against the BUILT page (MRB-244):
    # `s-think` is the confrontation block's emitted anchor.
    "misconceptions": [
        # Elicited by the hook: option A is this belief, and the student commits
        # to it or declines to before the page names it. Confronted in
        # `#s-think`, whose first body sends them back to the shelf's two bars
        # for the evidence, and marked in rung 2, whose distractor A states the
        # same belief as a rule.
        {"id": "ECO-07",
         "statement": "No bees, no food — we would starve within a few years.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        # No `elicited_by`: nothing on this page asks the student to state this
        # belief or offers it as an option. Measured, not forgotten — absence is
        # legal under MRB-248 and inventing an element name would be worse than
        # the gap. `#s-who`'s four cards state the correct account and are
        # deliberately not named here; the belief is taken apart in `#s-think`.
        {"id": "ECO-08",
         "statement": "Save the bees — keep a hive of honeybees.",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B9, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ "wind-pollinated" is glossed even though it is b5-06's word, because
    # four of the twelve tiles print it and it is the half of the shelf that
    # makes `ECO-07` false. It is glossed as the CONTRAST, not re-taught.
    "vocabulary": [
        {"term": "pollination",
         "definition": "Moving pollen from one flower to another so that seed "
                       "or fruit can form.",
         "note": "No pollination, no fruit — however healthy the plant is."},
        {"term": "pollinator",
         "definition": "An animal that carries pollen between flowers while "
                       "feeding.",
         "note": "Bees, hoverflies, moths, beetles and midges all do it."},
        {"term": "wind-pollinated",
         "definition": "A plant whose pollen is carried by air rather than by "
                       "an animal.",
         "note": "The cereals are all wind-pollinated, which is why they "
                 "survive."},
        {"term": "food security",
         "definition": "Whether a population can reliably get enough food, and "
                       "food of the right kind.",
         "note": "Enough calories is only half of it."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and the foot line names no slot.
    # Declaring one would invent a sourcing task in
    # `docs/ks3/diagram-manifest.md`. NOTES-B9 flag 17 is not dropped by this.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b9/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md §8.
        {"type": "supermarket-shelf", "id": "which-foods-survive",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · empty the shelves",
         "heading": "Which foods survive?",
         "prompt": "Twelve foods from an ordinary shop. Remove the insect "
                   "pollinators and see what is left, then read what has "
                   "happened to the two numbers underneath — because they do "
                   "not fall by the same amount, and that is the whole lesson.",
         # Design's mono line beside the heading (page line 490): three named
         # states, no number in any of them. ⚠️ `all` is FIRST because the
         # readout prints the first authored state at rest and the shelf opens
         # intact — see the docstring.
         "progress": {"all": "shelf intact",
                      "half": "half the pollinators",
                      "none": "no pollinators"},

         "foods": FOODS,

         # ⛔ TWO BARS, `cal` THEN `vit`, AND NEVER ONE. The order is the order
         # the `none` note reads them out in, and the renderer refuses any other
         # pair. Two labels and two colours is what stops them reading as one
         # quantity; the grid wraps to two ROWS at a narrow width rather than
         # merging, and there is a parity row that squeezes the container to
         # prove it.
         "bars": [{"id": "cal", "label": "Calories still available",
                   "colour_token": "--ks3-ok"},
                  {"id": "vit", "label": "Vitamins and minerals",
                   "colour_token": "--ks3-alert"}],

         "remove_label": "Remove every insect pollinator",
         "restore_label": "Bring the pollinators back",
         "half_label": "Lose half of them",

         # The three tile statuses once the dial has moved. At `loss == 0` the
         # tile prints the food's `how` instead — the dial doubles as the
         # teaching label. `{n}` is filled by the runtime from the surviving
         # fraction; a literal percentage here would be wrong on eleven tiles.
         "gone_label": "gone",
         "unaffected_label": "unaffected",
         "part_label": "{n}% of the crop",

         # ⛔ `{cal}` AND `{vit}` ARE NOT OPTIONAL IN `none`. They are computed
         # from the same arithmetic the bars are drawn from, and the whole point
         # of the sentence is that it reads the gap aloud. `_b9_placeholders()`
         # fails the build if either is missing.
         "notes": {
             "all": "The shelf as it is. Four of these twelve foods need no "
                    "insect at all, and between them they carry most of the "
                    "calories.",
             "none": "Calories down to {cal}%, vitamins and minerals down to "
                     "{vit}%. Nobody starves on what is left, and nobody stays "
                     "healthy on it either. That gap between the two bars is "
                     "the honest version of the argument for pollinators.",
             "half": "Halve the pollinators rather than removing them, and the "
                     "effect is a partial one — smaller crops, misshapen "
                     "fruit, higher prices. This is closer to what is actually "
                     "happening than the all-or-nothing version.",
         }},

        # #s-who — the band panel, and rail stop 3, mirroring `s-bench`. No
        # control of its own: it is the payoff of the shelf beside it, and it is
        # where `ECO-08` is answered positively.
        {"type": "rule", "anchor": "s-who",
         "eyebrow": "Who actually does the pollinating",
         "statement": "Mostly not the insect on the poster.",

         "cards": WHO_CARDS,

         # Design nests the key fact inside this section (page lines 338–341) on
         # the CARD ground with the accent offset shadow. `card`, because the
         # section itself is `band` and band on band is invisible.
         "key_fact": {"ref": "calories-and-variety-come-from-different-crops",
                      "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "ECO-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-who on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 341
    # and identical to payload schema §12's b9-04 entry.
    "key_facts": [
        {"id": "calories-and-variety-come-from-different-crops",
         "text": "Insect pollination is a service one group of organisms "
                 "provides to another, and human food supply depends on it. "
                 "Wind-pollinated cereals supply most of our calories; "
                 "insect-pollinated crops supply most of the variety, the "
                 "vitamins and the minerals.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and `_quoted()` adds the quotation marks, so the
        # beliefs are authored bare. The block asks for no commitment on
        # Design's page (measured: static markup, no options, no reveal, no
        # button, payload schema §3), so it is a `confrontation` and not a
        # `predict`, and it is not a rail stop.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "ECO-07",
         "statements": [
             # ⚖️ This paragraph is the reason the shelf is upstream of it in the
             # document. The student has just watched the calorie bar hold at 77
             # while the vitamin bar fell to 36, and the sentence that names
             # "enough energy and widespread deficiency diseases" is that
             # measurement in words. ⚠️ The `When diet goes wrong` link loses
             # its tag and keeps every word — the link text is already the
             # lesson title — and the edge is in `references`.
             {"quote": "No bees, no food — we would starve within a few years.",
              "body": ["Overstating a real problem is not a harmless way of "
                       "getting people to care, because the overstatement is "
                       "the part that gets checked. Wheat, rice, maize, barley "
                       "and oats are wind-pollinated and between them provide "
                       "the majority of the calories eaten on Earth; they "
                       "would be entirely unaffected. What the exaggeration "
                       "hides is a genuine and more specific problem: the "
                       "crops that do depend on insects are the fruit, nuts "
                       "and vegetables that supply vitamin C, vitamin A, "
                       "folate, iron and calcium, and losing them means a "
                       "population with enough energy and widespread "
                       "deficiency diseases — the situation When diet goes "
                       "wrong describes. That is worth acting on, it is "
                       "defensible against anyone who checks it, and it does "
                       "not need a fake quotation from Einstein attached to "
                       "it."]},
             # ⚑ NOTES-B9 flag 11 lands here. Checked and left; the two claims
             # are about two different populations and the paragraph keeps them
             # apart in every sentence. See the docstring.
             {"quote": "Save the bees — keep a hive of honeybees.",
              "body": ["Honeybees are a farmed animal. There are more managed "
                       "honeybee colonies in the world now than there were "
                       "fifty years ago, and a beekeeper adding a hive is "
                       "doing roughly what a farmer does by keeping chickens — "
                       "useful, but not conservation. The pollinators actually "
                       "in decline are the wild ones: solitary bees, of which "
                       "Britain has around 250 species, along with bumblebees, "
                       "hoverflies, moths and beetles. Several studies find "
                       "these wild insects pollinate crops more effectively "
                       "than honeybees do, and a dense hive in a poor "
                       "landscape can compete with them for the few flowers "
                       "there are. What wild pollinators need is flowers "
                       "through the whole season, undisturbed ground and "
                       "hedges to nest in, and fewer insecticides. Those are "
                       "landscape decisions, which is why this appears in a "
                       "lesson about food security rather than a lesson about "
                       "pets."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — rung 1 CLEAN AND UNTOUCHED, rung 2 REBUILT AT
    # THE DISTRACTOR. rung 1: four one-word food names, so the correct option
    # cannot be strictly the longest. rung 2 as delivered was 18w correct
    # against 8 / 12 / 7 — gap 6, a live tell — because the correct answer
    # stated a RULE and each distractor stated a one-clause wrong REASON. The
    # three distractors now state WRONG RULES in the same subject-condition-
    # consequence shape: 17 / 18 / 16 / 17, gap 1, ratio 1.06. Every correction
    # is Design's, unedited, and no correct option was shortened. Full working,
    # and the provenance of each rebuilt belief, in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Which crops depend on insects",
            "q": "Which of these would be least affected if all insect "
                 "pollinators disappeared?",
            # ⚖️ FOUR FOOD NAMES, AND THAT IS WHY THE RUNG IS CLEAN. The correct
            # answer names an ITEM and all three distractors name items, so a
            # student cannot pick by shape or by length. This is the second
            # construct the MRB-177 ruling names and it needs no rebuilding.
            # Design's option order and all three corrections are byte-identical.
            "options": [
                "Wheat",
                "Apples",
                "Almonds",
                "Strawberries",
            ],
            "answer": 0,
            "feedback": {
                1: "Apple trees need insects to carry pollen between flowers, "
                   "and orchards are often stocked with hives at blossom time "
                   "for exactly that reason.",
                2: "Almonds are the extreme case — entirely dependent, and the "
                   "crop that hires more hives than any other in the world.",
                3: "Poorly pollinated strawberries do form, but they come out "
                   "small and misshapen. The crop is not lost so much as "
                   "ruined.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A poster says losing bees would mean worldwide starvation "
                 "within four years. What is wrong with the claim?",
            # ⊕ MRB-177. Three distractors REBUILT as wrong rules; the correct
            # option, the option ORDER, the `answer` index and all three
            # corrections are Design's and are untouched.
            #
            #   A — `ECO-07`, this lesson's own register entry: almost every
            #       crop needs an insect, so the calories go too. Design's
            #       "Nothing —" opener is kept because the question asks what is
            #       wrong with the claim and this option answers "nothing".
            #   C — belief written for this rung; no register entry supplies it
            #       and none is minted. It is a wrong idea about EVIDENCE — bee
            #       numbers are fine, so the claim is about nothing — and it is
            #       confronted only here.
            #   D — belief written for this rung, and none is minted. Hand
            #       pollination does the same job, so it is a substitute. The
            #       *Going further* layer is what prices it.
            "options": [
                "Nothing — almost every crop we eat is insect-pollinated, so "
                "the calories would go with everything else",
                "Most calories come from wind-pollinated cereals, so the real "
                "loss would be vitamins and variety rather than energy",
                "Bees are not actually in decline, so a claim resting on their "
                "disappearance describes nothing real",
                "Hand pollination does the same job as an insect, so growers "
                "would simply pollinate the crops themselves",
            ],
            "answer": 1,
            "feedback": {
                0: "Look at the shelf. The four foods supplying most of the "
                   "calories are pollinated by wind or grown from tubers.",
                2: "Managed honeybees are doing reasonably well; wild "
                   "pollinators are genuinely declining. The claim is "
                   "exaggerated, not baseless.",
                3: "It is done in a few places and it is enormously expensive "
                   "in labour. It is a measure of the loss, not a solution to "
                   "it.",
            }},
        # Both self-marked rungs are lifted whole from Design's `SELF_RUNGS`,
        # five criteria each, in her order.
        "explain": {
            "title": "Rung 3 · Explain the two numbers",
            "q": "On the bench, removing insect pollinators takes far more "
                 "from the vitamin bar than from the calorie bar. Explain why, "
                 "and say what a population living on the remaining food would "
                 "suffer from.",
            "field_label": "Your explanation",
            "placeholder": "The foods that supply most of the calories…",
            # The fifth criterion is the whole of `ECO-07` marked as a criterion
            # rather than as prose, which is why the confrontation above can
            # stay static and still be assessed.
            "success": [
                "Says the main calorie foods are cereals and potatoes, which "
                "are wind-pollinated or grown without pollination.",
                "Says the insect-pollinated foods are mainly fruit, nuts and "
                "vegetables.",
                "Says those foods supply a large share of the vitamins and "
                "minerals in a diet.",
                "Concludes that the energy supply survives while the nutrient "
                "supply collapses.",
                "Names deficiency disease, or the distinction between having "
                "enough to eat and having a balanced diet.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A farm grows one crop across every field — oilseed rape, "
                 "which flowers for three weeks in spring and is "
                 "insect-pollinated. The farmer cannot understand why wild bee "
                 "numbers on the land keep falling despite so much blossom. "
                 "Explain the problem, and suggest two changes.",
            "field_label": "Your answer",
            "placeholder": "Three weeks of flowers means…",
            # Criteria 3 and 4 are `ECO-08`'s answer asked as a question: the
            # rung marks whether a student reaches for habitat and forage rather
            # than for a hive.
            "success": [
                "Says the bees have an enormous food supply for three weeks "
                "and almost nothing for the rest of the year.",
                "Says pollinators are active across many months and need "
                "flowers throughout that period.",
                "Identifies a second problem — nowhere to nest, or the effect "
                "of insecticides on the crop.",
                "Suggests a concrete change: wildflower margins, hedgerows, "
                "later mowing, a second flowering crop, or reduced spraying.",
                "Links it back to the farmer’s own interest — the crop needs "
                "the pollinators, so this is not only a conservation argument.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Many crops depend on insects to transfer pollen between "
                "flowers, and without it those plants set little or no fruit "
                "or seed. Cereals are wind-pollinated and supply most of our "
                "calories, so a loss of pollinators would not cause starvation "
                "— it would remove most of the fruit, nuts and vegetables, and "
                "with them most of the vitamins and minerals in the diet. Wild "
                "pollinators, not managed honeybees, are the ones in decline.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B9 flag 12 is this whole paragraph. Checked and left; the working
    # is in the docstring.
    #
    # ⚖️ MRB-225 holds: the layer adds a PRICE — what the free service costs
    # once it has to be bought in human working days — and retracts nothing
    # above it. Design's own hedge, "Why it started is disputed", is
    # load-bearing and may not be trimmed: it is what stops the paragraph
    # becoming a parable.
    "stretch": [
        {"type": "explainer", "id": "what-the-free-service-costs",
         "text": "In parts of Sichuan in China, apple and pear growers have "
                 "pollinated their orchards by hand for decades, climbing the "
                 "trees with pots of pollen and brushes made from cigarette "
                 "filters and chicken feathers. It works, the fruit sets, and "
                 "it takes a person a day to do what a few hundred bees would "
                 "do in an afternoon. Why it started is disputed — heavy "
                 "pesticide use, loss of wild habitat and the profitability of "
                 "hand pollination in a region with plentiful labour all "
                 "appear in different accounts — and it is worth being careful "
                 "with the story rather than using it as a simple parable. "
                 "What it does establish is a price. Insect pollination is a "
                 "service that has always been free, and where it has been "
                 "lost, the replacement cost has been measured in human "
                 "working days per hectare. That is what makes it a food "
                 "security question and not only a wildlife one."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check a claim you have seen about bees?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 297) and nothing in it is a safety
    # instruction — it is a note about how far the shelf can be trusted.
    # Routing it through `safety_note` would print it in the treatment reserved
    # for "never light a candle without an adult", which devalues the safety
    # line.
    #
    # ⚑ It is NOTES-B9 flag 10's honest half and it is load-bearing: it is the
    # page telling the student that the twelve shares are illustrative
    # proportions rather than a measurement, and that most crops set a reduced
    # crop rather than none — which is the same distinction the `half` setting
    # makes with the dial.
    "convention_note": "The shelf is a teaching model. The calorie and "
                       "nutrient bars are illustrative proportions for these "
                       "twelve foods, not a calculation for a real diet or a "
                       "national food supply, and crops differ in how "
                       "completely they depend on insects — many set a reduced "
                       "crop rather than none. Published estimates of the share "
                       "of global food production that depends on animal "
                       "pollination vary widely with how the question is asked.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The whole lesson is a claim being checked against a measurement: rung 2
    # asks what is wrong with a poster, which is analysis and evaluation, and
    # the hook's refusal to repeat a quotation because it is popular is
    # scientific attitudes in its plainest form.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
