"""B8 L4 — Fermentation and what we use it for (PROCESS).

Authored against Claude Design's approved page,
`KS3 B8 lessons/b8-04-fermentation.dc.html` (604 lines), her author's notes
`KS3 B8 lessons/NOTES-B8.md`, and the B8 payload schema
`docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md` §5, §7, §8, §9 and §10, under the
MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", the three MRB-225
shrinks and the three rung-2 distractors repaired under MRB-177 — all itemised
below. The two route cards, both marked rungs, both self-marked rungs, the four
dials and the ten outcome branches came out of
`node tools/extract_design_payload.js`, not off a keyboard.

── `covers` is CLAUSE (b) of a compound bullet ──────────────────────────

`KS3.B.RESP.03` reads, in full:

    the process of anaerobic respiration in humans and micro-organisms,
    including fermentation, and a word summary for anaerobic respiration

It names two organisms' worth of one process, and the commander split it during
integration (`ks3_data/substatements.py`, minted for B8):

    KS3.B.RESP.03a   anaerobic respiration in humans, + the word summary
    KS3.B.RESP.03b   anaerobic respiration in MICRO-ORGANISMS, incl. fermentation

This lesson owns (b) and only (b). (a) is b8-03's and is `touches` here, because
rung 1's second option and its correction both lean on it — "That is human
muscle, and the bacteria in yoghurt" only means anything to a student who has
met the human route already, which is why this lesson `requires` b8-03.

The clause's own words — *including fermentation* — are discharged twice over:
the bench IS a fermenter, and the band panel states both word summaries as the
two routes a micro-organism can take.

── The instrument: FOUR DIALS, TEN BRANCHES, EIGHT OUTCOME TEXTS ────────

`#s-bench` is `fermenter`, on `ks3-block ks3-dark ks3-practical` (page line
105), so `practical` is MEASURED off Design's markup rather than inferred from
the kind name — schema §0 rule 2, and contract §4 records that B1 got two of six
wrong by inferring it.

⚠️ **NOTES-B8 §2.4 counts four branches; the page has EIGHT distinct outcome
texts.** NOTES is counting the precedence tree and the page is the leaves: the
fermenting branch splits by organism × temperature (four texts) and the aerobic
branch splits by organism (two). The page is right; schema §11 item 2 says the
same. Eight are authored.

**Ten branch records carry those eight texts**, and the extra two are not
padding. `killed` and `starved` share one outcome text across both organisms but
NOT one product panel — a killed yeast vessel lists carbon dioxide and ethanol,
a killed bacteria vessel lists lactic acid and gas — so each of those two
outcomes needs one record per organism to carry its own `products`. Design gets
the same result from one branch plus a conditional in the render; a first-match
list cannot, and a first-match list is what removes the string sniff below.

**Order is the pedagogy and it is Design's own comment** (page line 442):
*"Order matters: killed beats starved beats aerobic beats fermenting."* A dead
organism with no sugar in an open vessel reports as DEAD, not as three things at
once, and a student changing one dial at a time meets one cause at a time.

⚑ **SCIENCE CORRECTION 1 — the bacteria-open product panel contradicted itself,
and the fix is structural.** Design computes `aerobic = out.line.indexOf(
'oxygen') >= 0` (page line 478) — a string sniff on the reaction text. It is
wrong on one live branch: yoghurt bacteria in an open, stirred vessel take
`line = "contaminated"`, which contains no `"oxygen"`, so the sniff falls
through to the anaerobic bacteria list and the bench prints **"Lactic acid
100 units"** directly underneath its own heading *"Poor conditions for these
bacteria"* and its own body text saying these bacteria *"do their work without
oxygen"*. Lactic acid is what the FERMENTATION route makes, and that route is
the one that runs when oxygen is absent; an aerobic, open, stirred, contaminated
vessel does not hand you a hundred units of it.

Fixed by authoring `products` per branch, so nothing is ever derived from
`line`. The corrected branch reports what an open stirred vessel of these
bacteria actually leaves you with: **no usable lactic acid and no gas** — the
milk does not set. The claim is deliberately shrunk to "none you could use"
rather than "none" (MRB-225): lactic acid bacteria are aerotolerant and traces
of acid are still made, so a flat zero would be a second false absolute
replacing the first. The teaching point — seal the vessel or you do not get
yoghurt — is exactly the one Design's body text already makes, and it now agrees
with the numbers above it.

⚖️ **What the rate of 100 means on that branch, since it is kept.** Schema §5.1
measures the aerobic branch at rate 100 and that figure is Design's, so it
stands: something in an open stirred vessel IS growing at full pelt — *"every
other organism in the room"*, in Design's own words. The rate row reports the
vessel, the product rows report what you can take out of it, and the body text
is what joins them. If Mide would rather the rate row read 0 on this one branch,
it moves in one place — `aerobic-bacteria` below — and nothing else changes.

⚖️ **The yeast open-and-stirred branch is NOT a failure state** (NOTES-B8 flag
16, schema §5.1). It is how baker's yeast is manufactured — aerated, stirred,
fed — and Design's own text says so. Rate 100, tone not amber, and it is the
branch that earns the sentence *"why a brewer seals the vessel"*. Checked and
left exactly as drawn, and recorded here so a later pass cannot read "aerobic"
as "wrong" and turn it into an error message.

⚑ The bench opens **already set as a brewery** (`start` == the `brewery`
preset), so pressing *Set it up as a brewery* first changes nothing visible
while still counting toward `done_after`. Measured, deliberate-looking, and
harmless — recorded so a later pass does not "fix" it into a different opening
state and cost the brewery/yoghurt contrast its symmetry.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to be headed "THREE
rail stops, not Design's four". Design draws four (`RAIL`, page lines 316–321)
and `#s-two` ticks on `s.seen >= 2` (page line 403) — the BENCH's predicate,
character for character, one section to the left (page line 402). `#s-two` is
an eyebrow, a display statement, two static route cards and a key fact: no
control, no commitment, no field. The argument was that
`ks3_parity.check_rail_reachable()` fails a stop whose section carries none of
the five DOM signals `doneByDom()` reads, that MRB-208 confined the rail to
sections requiring the student to do something, and that ALIASING the stop to
the bench would tick it for something done in a different section. So THREE
stops shipped.

Two things overrule that.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine.

And page line 403 is not an alias — it is Design, in a rail-level function,
saying what completes the stop. The two routes are the payoff of the four dials
beside them; `#s-two` carries no control precisely because the bench already
took the student's commitment. That is a MIRROR, and `wireRail`'s `paint()`
resolves mirrors at rail level rather than searching the section for a signal.

So the fourth stop is declared: anchor `s-two`, `mirrors: "s-bench"`,
`done_when: "two_setups_tried"` — with Design's `ROUTES` / "Two routes" pair
restored to it — and `check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`. All four B7 pages, b4-03 `#s-built`, b5-06
`#s-designs`, b6-03 `#s-four`, c1-02 `#s-matrix` and the rest are restored the
same way. **`#s-two` keeps its anchor**, as it always did.

NOTES-B8 §4's "four in all five" is now followed rather than reported. Schema
§7's pre-dispatch three-stop ruling is superseded; its text has not been re-cut,
so read that count as historical.

── ⊕ MRB-225 — THREE CLAIMS SHRUNK UNTIL THEY ARE TRUE ──────────────────

⚑ **SCIENCE CORRECTION 2 — rung 2's stem, and NOTES-B8 flag 15.** Design asks
*"Why is there no alcohol in the finished loaf?"* As written that is false: a
trace of ethanol survives baking in the crumb (commonly quoted at a few tenths
of a percent), which is precisely what NOTES flag 15 says the lesson does not
mention. A rung stem is not a place to state something a keen student can look
up and find wrong, and MRB-225 says the claim shrinks until it is true rather
than being taught and later walked back. **Two words:**

    Design:  Why is there no alcohol in the finished loaf?
    Built:   Why is there almost no alcohol in the finished loaf?

The correct option, the `answer` index, the option order and all three
corrections are untouched, and the science the rung measures — ethanol boils at
78 °C, well below baking temperature, so it leaves as vapour — is unchanged. The
hook reveal's *"the alcohol leaves through the crust"* is left as drawn: it says
the alcohol leaves, which it does, and does not claim a zero.

⚑ **SCIENCE CORRECTION 3 — insulin is not all made by bacteria.** Design's
*Going further* says *"made by bacteria carrying an inserted human gene"*.
Almost all insulin IS made by a genetically modified micro-organism in a
fermenter, but a large share of it — the world's largest producer's entire
output — is made in **yeast**, not bacteria. Shrunk to the true version:

    Design:  now made by bacteria carrying an inserted human gene
    Built:   now made by micro-organisms — bacteria or yeast — carrying an
             inserted human gene

Six words, and the paragraph is stronger for it: the two organisms on the bench
are the two organisms in the industry, which is the point the layer's last
sentence already makes.

⚑ **NOTES-B8 flag 17 — RULED, AND THE CLAUSE IS CUT.** Design's first
confrontation ended a sentence with *"which is why weak beer was safer than
water in medieval cities"*, and flags it herself: widely repeated, questioned by
historians, and *"the one line in B8 that is history rather than science"*. Her
own recommendation is keep-as-an-aside or cut.

Cut, and the true half of the sentence kept:

    Design:  Alcohol does the same job by different means, which is why weak
             beer was safer than water in medieval cities.
    Built:   Alcohol does the same job by different means.

The claim that survives — ethanol preserves, as lactic acid does — is the one
the paragraph needs, and it is not in dispute. It is NOT moved to *Going
further*: that layer is industrial fermentation, and importing a contested
historical claim into it would preserve the claim rather than remove it, while
adding student-facing copy to a layer Design wrote about something else. If Mide
wants the history, it comes back as one sentence in `stretch`, hedged, and this
docstring is where its removal is recorded.

── NOTES-B8 flags landing on this lesson: checked, and what was done ────

  * flag 15  **"Bread: the ethanol evaporates."** CHECKED, AND THE STEM SHRUNK
             — see science correction 2. The mechanism is right: ethanol boils
             at 78 °C and a bread crumb reaches about 98 °C, so the great
             majority of it goes. What was wrong was the absolute.

  * flag 16  **Yeast in an open stirred vessel respires aerobically, and that
             is how yeast is manufactured.** CHECKED AND LEFT, unaltered, and
             defended above. It is correct — baker's yeast is produced in
             aerated, stirred, fed-batch culture precisely to keep the organism
             on the aerobic route and off the ethanol one — and it is rarely
             taught. Mide's confirmation is still wanted; nothing here depends
             on it, because confirming or softening the claim does not turn the
             branch into a failure state.

  * flag 17  **"Weak beer was safer than water in medieval cities."** RULED AND
             CUT — above.

  * flag 18  **Industrial fermentation** (Going further): insulin from GM
             micro-organisms versus pig and cattle pancreases, penicillin from a
             fungus, Quorn, ethanol fuel in Brazil. CHECKED AND LEFT, with the
             one shrink at science correction 3. Recombinant human insulin
             replaced animal-pancreas extract from the early 1980s and animal
             insulin is essentially gone; penicillin is grown from *Penicillium*
             in fermenters; Quorn is a fungal mycoprotein grown in a fermenter
             and harvested as food; Brazil runs a very large sugar-cane ethanol
             fuel industry and most of its new cars are flex-fuel. Every claim
             holds. "Several thousand litres" errs SMALL — industrial vessels
             run to tens of thousands — which is the safe direction.

  * flag 21  **No diagrams in the unit.** `figures: []` here is MEASURED, not
             assumed: `<img>`, `<figure>` and `<picture>` appear zero times on
             this page, and the only SVG on it is UI furniture (nav chevron,
             rail tick, endmatter arrows, ladder marks). §4.10 allows an empty
             `figures` for a lesson carried by its interactives. Nothing is
             declared, because declaring a slot means writing a caption and a
             caption would pre-empt the ruling flag 21 asks for. The flag is not
             dropped — it is Mide's.

── ⊕ MRB-177 LENGTH PARITY — RUNG 2 FAILED, RUNG 1 DID NOT ──────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one):

    AS DESIGN DREW THEM                      AFTER THE REPAIR
    rung 1  correct  4w vs 2 / 4 / 3   ✓     untouched, byte-identical
    rung 2  correct 14w vs 6 / 10 / 4  ✗     correct 14w vs 14 / 13 / 14   ✓

Rung 1 passes as drawn — the correct answer NAMES TWO PRODUCTS and so do its
distractors, which is the "same shape" construct arriving by itself — and it is
therefore not touched. Rung 2 tripped the gate on the ≥4-word arm, by exactly 4:
a student could have scored it by picking the long one.

**The correct option is unchanged, the `answer` index is unchanged, Design's
option ORDER is unchanged, all three corrections are byte-identical, and the
gate's threshold is untouched.** Three distractors gained the consequence the
belief they already carried licenses:

    r2 A  waste is reabsorbed, nothing is wasted  + "because nothing a cell
          makes is ever wasted"
    r2 C  bread yeast is a different organism     + "only the gas"
    r2 D  ethanol is acid-like                    + "the way an alkali cancels
          an acid in a beaker"

None of the three is in the register: `RESP-07` and `RESP-08` are this lesson's
two entries and neither is a ladder belief. All three beliefs are named in the
report, and each is one a student your age actually holds — "living things do
not waste anything" is the same intuition that makes urea and carbon dioxide
hard to teach; "bread yeast must be a different kind" is the standard rescue
when a student cannot accept beer and bread sharing a reaction; and "flour
neutralises it" is chemistry vocabulary reaching for the nearest verb it knows.
Design's own corrections answer all three unchanged, which is the test that the
repair was to the construct and not to the science.

── What could not be lifted byte-identical, and why ─────────────────────

1. **The two route cards keep every string, in Design's own treatments.**
   `_rule_card` reads `role` (mono accent tag), `term` (display name), `chips`
   (the inset panel), `gloss` (body) and `examples` (the muted foot line) — one
   slot per part Design drew, so `who`, `name`, `equation`, `note` and `uses`
   all survive with no joining and nothing invented. This is the first B-unit
   card in the key stage that did not have to give something up; b7-04's three
   job cards lost their inset treatment because that shape did not exist yet.

2. **The two inline links in `#s-think` lose their `<a>` tags and keep their
   words.** `rich()` allows `<em>` and `<strong>` and nothing else. Design links
   *Unicellular organisms* and *Enzymes in digestion*, and both link texts are
   lesson TITLES rather than build codes, so dropping the tag costs no meaning
   — b4-05's precedent exactly. Both destinations survive as real edges:
   `unicellular-organisms` in `requires`, `enzymes-in-digestion` in
   `references`, and Design draws both in her own endmatter as well.

3. ⚠️ **A BUILD-INTERNAL LESSON CODE IN STUDENT PROSE, resolved.** The killed
   branch's body says *"this is the same permanent change you met in b3-06"*.
   A student cannot resolve a slot code, and §8.10 exists to stop exactly this
   leakage. Resolved to the lesson TITLE, which is the string Design herself
   uses for the same destination in her own `#s-think` link and endmatter:

       Design:  the same permanent change you met in b3-06
       Built:   the same permanent change you met in Enzymes in digestion

   Every science word is unchanged, and the destination is carried as a real
   `references` edge rather than as text.

4. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

5. **The bench's section heading loses its `<h2>` level.** Design draws "Set the
   conditions, see what you have made" as an `<h2>` inside `#s-bench` beside a
   mono counter; it is authored as the instrument's `heading` and the renderer
   decides the tag. No word changes. Same for the ladder's `<h2>`.

── Keys this pass authors that the ENGINE pass must wire (contract R5) ───

`r_fermenter` does not exist in `build_ks3.py` yet — it belongs to the engine
pass, not to this one — so the read sites this payload needs are named here
rather than left to be discovered. All of them are schema §5 keys:

    progress   {"zero", "some"}   page line 521; `{n}` is the set-up count and
                                  `{s}` is Design's own plural marker
                                  (`s.seen === 1 ? '' : 's'`)
    rate_label "Rate {n}% of maximum"   page lines 131 + 530; `{n}` is the
                                  matched branch's `rate`
    branches   ORDERED, first match wins on `when`. A branch with no `products`
               is a defect, not a default — see science correction 1
    products   `value` prints as drawn and the bar fills to the branch `rate`;
               `none_text` prints as drawn and the bar fills to 0. No third key
               is needed and none is authored
    done_after 2, Design's own `seen >= 2`; the bench emits
               `data-stage-done="1"` at that count and nothing else on it can
               complete it

⚠️ **`segment` is NOT authored**, though schema §5 lists it. `ks3_data/b8/
__init__.py::_INSTRUMENT_SEGMENTS` supplies it for the whole unit in one place,
deliberately, and an authored copy would be a key with no read site (R5). Same
as all four B7 instruments.

⚠️ **No runtime state is authored** (schema §0 rule 3). The dial positions and
the set-up count are values the runtime owns; `start` is the opening
arrangement, which is authored because Design's `BREWERY` constant is the
page's own opening arrangement and not a runtime value.

⚠️ **U+2192 IS TYPED IN THREE PLACES AND THAT IS AN ENGINE PROBLEM, NOT A
CONTENT ONE.** The bench's `line` strings and the two route-card chips carry
Design's own arrow — `glucose → ethanol + carbon dioxide`. `r_equation` refuses
a typed arrow because the design system's five latin woff2 subsets have no
U+2192, so one falls back to a system font mid-line. These are not `r_equation`
blocks: they are Design's drawn reaction lines inside a bench panel and inside a
mono inset chip, and she types the character in both. Authored as she drew them.
**The engine pass should confirm the mono face actually carries the glyph in
`.ks3-rule-chip` and in the bench's reaction line, and draw it if not** — this
module cannot fix a font problem and inventing a different arrow word here would
change three student-facing strings for a reason no student would see.
"""

# ── the two route cards (page lines 347–354, via extract_design_payload.js) ─
#
# `role` · `term` · `chips` · `gloss` · `examples` are Design's `who` · `name` ·
# `equation` · `note` · `uses`, one slot each — see "What could not be lifted" 1.
# The two equations are the statutory word summaries for clause (b) and are the
# reason this panel is not decoration.
ROUTE_CARDS = [
    {"role": "A single-celled fungus",
     "term": "Yeast",
     "chips": ["glucose → ethanol + carbon dioxide"],
     "gloss": "Two products, one of them a gas. Which one you want decides "
              "what you build: a baker wants the gas and lets the ethanol "
              "evaporate, a brewer wants the ethanol and lets the gas escape "
              "through an airlock.",
     "examples": "Bread, beer, wine, cider, and ethanol for fuel."},

    {"role": "Bacteria",
     "term": "Lactic acid bacteria",
     "chips": ["glucose → lactic acid"],
     "gloss": "One product, no gas. The acid curdles milk protein, which is "
              "what thickens yoghurt, and it drops the pH low enough that "
              "spoilage organisms cannot grow.",
     "examples": "Yoghurt, cheese, sauerkraut, kimchi, sourdough’s sour taste, "
                 "and salami."},
]

# ── the four dials (page lines 324–342) ─────────────────────────────────
#
# Nine buttons in four groups. Every press increments the set-up count, which is
# what `done_after` counts — a student who changes one dial twice has still
# tried two set-ups, and Design's own counter says so.
DIALS = [
    {"id": "organism", "name": "Organism",
     "options": [{"id": "yeast", "label": "Yeast"},
                 {"id": "bacteria", "label": "Yoghurt bacteria"}]},
    {"id": "oxygen", "name": "Oxygen",
     "options": [{"id": "sealed", "label": "Sealed vessel"},
                 {"id": "open", "label": "Open and stirred"}]},
    {"id": "temp", "name": "Temperature",
     "options": [{"id": "cold", "label": "4 °C"},
                 {"id": "warm", "label": "30 °C"},
                 {"id": "hot", "label": "80 °C"}]},
    {"id": "sugar", "name": "Sugar",
     "options": [{"id": "yes", "label": "Supplied"},
                 {"id": "no", "label": "None"}]},
]

# ── the outcome tree (page lines 442–471), FLATTENED AND ORDERED ────────
#
# ⚠️ FIRST MATCH WINS, and the order below is Design's own comment: killed beats
# starved beats aerobic beats fermenting. Every `when` is read as "all of these
# dials are in these positions"; a branch matches when every pair matches.
#
# Ten records, eight outcome texts. `killed` and `starved` each carry one text
# across both organisms but need one record per organism to carry their own
# product panel — see the docstring.
#
# ⛔ `products` IS AUTHORED PER BRANCH AND IS NEVER DERIVED FROM `line`. Design
# sniffs the reaction text for the word "oxygen" (page line 478) and that sniff
# is wrong on `aerobic-bacteria`, where it prints a hundred units of a
# fermentation product under a heading saying the conditions are poor. Science
# correction 1 in the docstring.
BRANCHES = [
    # 1. KILLED — 80 °C. Rate 0. The one irreversible dial on the bench.
    {"id": "killed-yeast",
     "when": {"organism": "yeast", "temp": "hot"},
     "rate": 0,
     "line": "no reaction",
     "title": "Nothing, and nothing will happen now",
     # ⚠️ "b3-06" resolved to the lesson TITLE — "What could not be lifted" 3.
     "body": "At 80 °C the organism’s enzymes are denatured and the cells are "
             "dead. Cooling the vessel will not bring them back — this is the "
             "same permanent change you met in Enzymes in digestion, and it is "
             "why a baker uses warm water rather than hot.",
     "products": [{"name": "Carbon dioxide", "tone": "alert",
                   "none_text": "none"},
                  {"name": "Ethanol", "tone": "ok", "none_text": "none"}]},

    {"id": "killed-bacteria",
     "when": {"organism": "bacteria", "temp": "hot"},
     "rate": 0,
     "line": "no reaction",
     "title": "Nothing, and nothing will happen now",
     "body": "At 80 °C the organism’s enzymes are denatured and the cells are "
             "dead. Cooling the vessel will not bring them back — this is the "
             "same permanent change you met in Enzymes in digestion, and it is "
             "why a baker uses warm water rather than hot.",
     "products": [{"name": "Lactic acid", "tone": "alert",
                   "none_text": "none"},
                  {"name": "Gas produced", "tone": "ok",
                   "none_text": "none — this route makes no gas"}]},

    # 2. STARVED — no sugar. Rate 0, organism alive and unharmed. This is the
    # branch that makes "fermentation is respiration" concrete: no substrate,
    # no products, however perfect the other three dials are.
    {"id": "starved-yeast",
     "when": {"organism": "yeast", "sugar": "no"},
     "rate": 0,
     "line": "no reaction",
     "title": "Nothing — no fuel",
     "body": "A living organism with nothing to respire. Fermentation is "
             "respiration, and respiration needs a substrate: no sugar, no "
             "products, however perfect the other three dials are.",
     "products": [{"name": "Carbon dioxide", "tone": "alert",
                   "none_text": "none"},
                  {"name": "Ethanol", "tone": "ok", "none_text": "none"}]},

    {"id": "starved-bacteria",
     "when": {"organism": "bacteria", "sugar": "no"},
     "rate": 0,
     "line": "no reaction",
     "title": "Nothing — no fuel",
     "body": "A living organism with nothing to respire. Fermentation is "
             "respiration, and respiration needs a substrate: no sugar, no "
             "products, however perfect the other three dials are.",
     "products": [{"name": "Lactic acid", "tone": "alert",
                   "none_text": "none"},
                  {"name": "Gas produced", "tone": "ok",
                   "none_text": "none — this route makes no gas"}]},

    # 3. AEROBIC — open and stirred, organism alive, sugar supplied. Rate 100.
    #
    # ⚖️ THIS ONE IS NOT A FAILURE STATE. It is how yeast is manufactured, the
    # body text says so, and it is the branch that teaches why a brewer seals
    # the vessel. Tone is not amber and the rate is full. NOTES-B8 flag 16.
    {"id": "aerobic-yeast",
     "when": {"organism": "yeast", "oxygen": "open"},
     "rate": 100,
     "line": "glucose + oxygen → carbon dioxide + water",
     "title": "Fast growth, and no alcohol",
     "body": "With oxygen available, yeast respires aerobically instead — it "
             "gets far more energy per glucose, so it grows and divides "
             "quickly, and produces carbon dioxide and water rather than "
             "ethanol. This is exactly how yeast itself is manufactured, in "
             "open stirred tanks. It is also why a brewer seals the vessel: to "
             "force the organism down the route that makes the product.",
     "products": [{"name": "Carbon dioxide", "tone": "alert",
                   "value": "100 units"},
                  {"name": "Ethanol", "tone": "ok", "none_text": "none"}]},

    # ⚑ SCIENCE CORRECTION 1 LIVES HERE. Design's string sniff printed "Lactic
    # acid 100 units" under "Poor conditions for these bacteria" — a
    # fermentation product at full yield on an aerobic branch. What an open,
    # stirred, contaminated vessel of these bacteria actually leaves you with is
    # nothing you can use: the milk does not set. "None you could use" rather
    # than "none", because these bacteria are aerotolerant and traces of acid
    # are still made — a flat zero would swap one false absolute for another.
    {"id": "aerobic-bacteria",
     "when": {"organism": "bacteria", "oxygen": "open"},
     "rate": 100,
     "line": "contaminated",
     "title": "Poor conditions for these bacteria",
     "body": "Lactic acid bacteria of this kind do their work without oxygen, "
             "and an open stirred vessel also invites in every other organism "
             "in the room. Seal it if you want yoghurt rather than a science "
             "experiment.",
     "products": [{"name": "Lactic acid", "tone": "alert",
                   "none_text": "none you could use — the milk does not set"},
                  {"name": "Gas produced", "tone": "ok",
                   "none_text": "none — this route makes no gas"}]},

    # 4. FERMENTING — everything else. Rate 12 cold, 100 warm. Four texts.
    #
    # The cold pair is the temperature teaching: alive, unharmed, and slow,
    # which is a different idea from dead and is why the 4 °C dial exists next
    # to the 80 °C one. Rung 4 marks the difference between the two.
    {"id": "ferment-yeast-cold",
     "when": {"organism": "yeast", "temp": "cold"},
     "rate": 12,
     "line": "glucose → ethanol + carbon dioxide",
     "title": "Slow fermentation — a sourdough in the fridge",
     "body": "At 4 °C the yeast is alive and unharmed, and everything is "
             "happening slowly — molecules collide less often. Bakers use this "
             "deliberately: an overnight cold rise gives more time for flavour "
             "to develop while the dough inflates gently.",
     "products": [{"name": "Carbon dioxide", "tone": "alert",
                   "value": "12 units"},
                  {"name": "Ethanol", "tone": "ok", "value": "12 units"}]},

    {"id": "ferment-yeast-warm",
     "when": {"organism": "yeast", "temp": "warm"},
     "rate": 100,
     "line": "glucose → ethanol + carbon dioxide",
     "title": "Beer, wine, or a rising loaf",
     "body": "Sealed, warm and fed. Ethanol and carbon dioxide are being "
             "produced steadily. A brewer lets the gas out through an airlock "
             "and keeps the liquid; a baker keeps the gas in the dough and "
             "lets the ethanol boil off in the oven. Same reaction, opposite "
             "product wanted.",
     "products": [{"name": "Carbon dioxide", "tone": "alert",
                   "value": "100 units"},
                  {"name": "Ethanol", "tone": "ok", "value": "100 units"}]},

    {"id": "ferment-bacteria-cold",
     "when": {"organism": "bacteria", "temp": "cold"},
     "rate": 12,
     "line": "glucose → lactic acid",
     "title": "Barely anything — this is why yoghurt lives in the fridge",
     "body": "The bacteria are alive and almost inactive. This is exactly why "
             "a finished yoghurt is refrigerated — not to stop the bacteria "
             "being there, but to slow them almost to a halt so it does not "
             "keep souring.",
     "products": [{"name": "Lactic acid", "tone": "alert",
                   "value": "12 units"},
                  {"name": "Gas produced", "tone": "ok",
                   "none_text": "none — this route makes no gas"}]},

    {"id": "ferment-bacteria-warm",
     "when": {"organism": "bacteria", "temp": "warm"},
     "rate": 100,
     "line": "glucose → lactic acid",
     "title": "Yoghurt",
     "body": "Sealed and warm with sugar available. Lactic acid is "
             "accumulating, the pH is falling, and the milk protein is "
             "curdling into a thick set. Left too long it becomes unpleasantly "
             "sour, so the maker chills it to stop the reaction where they "
             "want it.",
     "products": [{"name": "Lactic acid", "tone": "alert",
                   "value": "100 units"},
                  {"name": "Gas produced", "tone": "ok",
                   "none_text": "none — this route makes no gas"}]},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 149 character for character.
    "slug":        "fermentation",
    "title":       "Fermentation and what we use it for",
    "discipline":  "biology",
    "unit":        "respiration",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # Clause (b) of the compound RESP.03 bullet — the micro-organism half. See
    # the docstring; the split is the commander's, minted in substatements.py.
    "covers":      ["KS3.B.RESP.03b"],
    # RESP.01 is the reaction itself, b8-01/b8-02's, assumed throughout and
    # never restated here. RESP.03a is b8-03's human clause, which rung 1's
    # second correction leans on and this lesson `requires`.
    "touches":     ["KS3.B.RESP.01", "KS3.B.RESP.03a"],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 2},
                    {"id": "cells-and-systems", "level": 2},
                    {"id": "substances-and-reactions", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's endmatter: "Before this lesson → Anaerobic respiration in humans,
    # Unicellular organisms"; "Connects to → Bacteria in the gut, Enzymes in
    # digestion". `unicellular-organisms` is also the destination of the first
    # stripped inline link in `#s-think`, and `enzymes-in-digestion` is the
    # destination of both the second one and the killed branch's resolved
    # lesson code — "What could not be lifted" 2 and 3.
    "requires":    ["anaerobic-respiration-in-humans", "unicellular-organisms"],
    "assumes":     [],
    "references":  [{"unit": "B3", "lesson": "bacteria-in-the-gut"},
                    {"unit": "B3", "lesson": "enzymes-in-digestion"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Industrial fermenters and their control systems, "
                   "biotechnology, and genetically modified organisms making "
                   "human proteins.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Bread, yoghurt, cheese, soy sauce, vinegar, chocolate, and "
                    "every alcoholic drink there has ever been. All of them are "
                    "the waste products of something respiring without oxygen, "
                    "and we built a civilisation on them before we knew that.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them and as NOTES-B8 §4 requires. `s-two` is
    # the third: no control of its own, so it mirrors `s-bench` and ticks on
    # the bench's `s.seen >= 2` — see the docstring, which supersedes schema
    # §7's count. `short` and `label` are Design's own `RAIL_SHORT` and `RAIL`
    # strings (page lines 316–322), `ROUTES` / "Two routes" included.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "The holes",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.seen >= 2` (page line 402). Two
        # set-ups tried — a single dial press is not a comparison.
        {"anchor": "s-bench", "short": "BENCH", "label": "Four dials",
         "done_when": "two_setups_tried"},
        {"anchor": "s-two", "short": "ROUTES", "label": "Two routes",
         "mirrors": "s-bench", "done_when": "two_setups_tried"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # A wager, never marked — no `answer` key. B is the right one and the reveal
    # says so at once: the hook is not a trick, it is the claim the page earns.
    "phenomenon": {
        "kind": "narrative",
        "title": "A loaf of bread is full of holes. Something put them there.",
        "prompt": "Cut a slice and count them: hundreds of bubbles, each one a "
                  "pocket of gas trapped in dough that set around it in the "
                  "oven. The dough went in flat and came out twice the size. "
                  "Nothing was pumped into it.",
        "commit": "What made the holes?",
        "options": [
            "The yeast cells swelling up as they grow",
            "Carbon dioxide released by yeast respiring",
            "Air already in the dough expanding in the oven",
            "Steam from the water in the dough",
        ],
        "reveal": "Carbon dioxide, breathed out by yeast. Yeast is a living "
                  "single-celled fungus, and in dough it is short of oxygen, "
                  "so it respires anaerobically — releasing carbon dioxide, "
                  "which inflates the dough, and ethanol, which boils off in "
                  "the oven. Bread is risen by a waste gas, and the alcohol "
                  "leaves through the crust.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # `RESP-07` and `RESP-08` are the commander's pre-allocation and both
    # statements are Design's own quoted beliefs, verbatim off `#s-think` (page
    # lines 186 and 190). `RESP-14` is this lesson's named spare and is
    # deliberately left UNUSED — a permanent gap, like `PLANT-09`..`12`,
    # `DRUG-07` and `REPRO-17`/`20`/`21`/`23`. Do not re-point it.
    #
    # ⚠️ The `RESP` prefix row did not exist in
    # `docs/ks3/misconception-register.md` when this module was written — the
    # engine pass owns that file and opens the family. Both statements below are
    # the rows it must carry, and they are quoted from the page rather than
    # composed here so the two cannot drift.
    #
    # Both values resolve against the BUILT page (MRB-244 / MRB-248): `s-think`
    # is the confrontation block's anchor and `s-bench` is the instrument's, and
    # both are emitted as `id="…"`. `s-bench` is a rail stop; the gate wants an
    # emitted element, not a completion signal, so either would do.
    "misconceptions": [
        {"id": "RESP-07",
         "statement": "Fermenting is just food going off in a controlled way.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
        # ⚖️ Elicited at the BENCH, and this is not a formality. A student who
        # thinks yeast is a raising powder has no reason to expect the 80 °C
        # dial to kill anything or the sugar dial to matter at all; setting
        # either and reading "the cells are dead" or "a living organism with
        # nothing to respire" is where they state the belief to themselves.
        # `#s-think` is where it dies.
        {"id": "RESP-08",
         "statement": "Yeast is a powder — a raising agent, like baking powder.",
         "elicited_by": "s-bench",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B8, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    "vocabulary": [
        {"term": "fermentation",
         "definition": "Anaerobic respiration carried out by a micro-organism, "
                       "and the products we take from it.",
         "note": "It is respiration, not decay — the organism is alive and "
                 "feeding."},
        {"term": "yeast",
         "definition": "A single-celled fungus that respires sugar to ethanol "
                       "and carbon dioxide when it has no oxygen.",
         "note": "A living organism, not a chemical raising agent."},
        {"term": "ethanol",
         "definition": "The alcohol in beer, wine and cider — a waste product "
                       "of yeast fermenting sugar.",
         "note": "It boils at 78 °C, well below the temperature inside a "
                 "baking loaf."},
        {"term": "lactic acid",
         "definition": "The acid some bacteria make from sugar without oxygen, "
                       "and the same acid a human muscle makes.",
         "note": "It curdles milk protein and drops the pH, which is what sets "
                 "yoghurt and keeps it."},
        {"term": "fermenter",
         "definition": "A vessel in which a chosen micro-organism is grown "
                       "under controlled conditions to make a product.",
         "note": "Temperature, pH, oxygen and food supply are the controls — "
                 "the dials on the bench, scaled up."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` appear zero
    # times on this page and its foot line names no slot. NOTES-B8 flag 21 is
    # not dropped by this — it is Mide's to rule on.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b8/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED, not inherited.
        #
        # ⚠️ THIS INSTRUMENT IS ON INK. `.ks3-dark p` is (0,1,1) and beats a
        # bare instrument class at (0,1,0). Gated since MRB-245 by
        # `ks3_parity.check_dark_text_specificity()`; recorded here because this
        # payload is what feeds it.
        #
        # Payload keys follow docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md §5.
        {"type": "fermenter", "id": "four-dials", "anchor": "s-bench",
         "demand": "investigate",
         "eyebrow": "At the bench · one vessel, four dials",
         "heading": "Set the conditions, see what you have made",
         "prompt": "The same four dials that a brewer, a baker and a yoghurt "
                   "maker all set differently. Change one and the product "
                   "changes with it — or you get nothing at all, which is just "
                   "as informative.",
         # `{n}` is the set-up count; `{s}` is Design's plural marker.
         "progress": {"zero": "nothing changed yet",
                      "some": "{n} set-up{s} tried"},

         "dials": DIALS,
         # Design's `BREWERY` constant, which is also the first preset — the
         # bench opens already set up as a brewery. See the docstring.
         "start": {"organism": "yeast", "oxygen": "sealed", "temp": "warm",
                   "sugar": "yes"},
         "presets": [
             {"id": "brewery", "label": "Set it up as a brewery",
              "dials": {"organism": "yeast", "oxygen": "sealed",
                        "temp": "warm", "sugar": "yes"}},
             {"id": "dairy", "label": "Set it up as a yoghurt maker",
              "dials": {"organism": "bacteria", "oxygen": "sealed",
                        "temp": "warm", "sugar": "yes"}},
         ],

         "rate_label": "Rate {n}% of maximum",
         "outcome_label": "What you have made",
         "branches": BRANCHES,
         "done_after": 2},

        # #s-two — the band panel, `rule` with the two route cards. Rail stop
        # 3, mirroring `s-bench`. See the docstring.
        {"type": "rule", "anchor": "s-two",
         "eyebrow": "Two fermentations, two products",
         "statement": "Which organism decides what you get.",
         "cards": ROUTE_CARDS,
         # Design nests the key fact inside this section (page lines 175–178),
         # on the CARD ground, because the section itself is band and band on
         # band is invisible. Her own arrangement, kept — b7-01's precedent.
         "key_fact": {"ref": "fermentation-is-anaerobic-respiration",
                      "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "RESP-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Byte-identical to the page (line 177), and it is the statutory clause
    # stated in one sentence: fermentation IS anaerobic respiration in
    # micro-organisms, with both word summaries.
    "key_facts": [
        {"id": "fermentation-is-anaerobic-respiration",
         "text": "Fermentation is anaerobic respiration in micro-organisms. In "
                 "yeast, glucose gives ethanol + carbon dioxide; in bacteria "
                 "such as those in yoghurt, glucose gives lactic acid. What we "
                 "call the food is the organism's waste.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment, on Design's page and
        # here, so it is not a rail stop and emits no completion contract.
        # (Contract R1 makes `#s-think` a `predict` in B2, C1 and C2 because on
        # THOSE pages it gates a reveal behind a commitment. All five B8 pages
        # are static markup, like B1's and B7's, so they stay confrontations.)
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "RESP-07",
         "statements": [
             # ⚑ NOTES-B8 flag 17 RULED HERE: the medieval-beer clause is cut
             # and the true half of its sentence kept. See the docstring.
             {"quote": "Fermenting is just food going off in a controlled way.",
              "body": ["It is closer to the opposite. Milk left on a windowsill "
                       "spoils because whatever lands in it grows; milk turned "
                       "into yoghurt is deliberately given one chosen organism "
                       "and the conditions that organism likes, and the lactic "
                       "acid it produces drops the pH far enough that the "
                       "spoilage organisms cannot grow. That is why yoghurt "
                       "keeps longer than the milk it was made from, why "
                       "sauerkraut survived European winters, and why every "
                       "traditional cuisine has fermented foods in it. Alcohol "
                       "does the same job by different means. The pattern is "
                       "worth holding onto: a fermented food is one where we "
                       "picked the micro-organism first, and the waste product "
                       "it makes is exactly what keeps everything else out."]},
             # ⚠️ Two inline links stripped, both link texts kept — they are
             # lesson TITLES, not codes. "What could not be lifted" 2.
             {"quote": "Yeast is a powder — a raising agent, like baking "
                       "powder.",
              "body": ["Baking powder is a chemical that releases carbon "
                       "dioxide when it gets wet and warm, and it works in a "
                       "bowl of anything. Yeast is a living organism: a "
                       "single-celled fungus, of the kind you met in "
                       "Unicellular organisms, dried into a state where it "
                       "survives on a shelf and revives in warm water. "
                       "Everything a baker does follows from that. You give it "
                       "sugar because it needs feeding; you use warm water "
                       "because it is a living thing with enzymes and an "
                       "optimum temperature; you do not use boiling water, "
                       "because that denatures the enzymes and kills it, "
                       "exactly as in Enzymes in digestion; and you wait, "
                       "because it is respiring at its own pace and cannot be "
                       "hurried. A packet of dried yeast contains billions of "
                       "dormant cells, and a dead one raises nothing."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY. Rung 1 PASSES as drawn (4w against 4w — the
    # correct answer names two products and so do its distractors) and is
    # byte-identical. Rung 2 failed by exactly 4 words and its three distractors
    # are rewritten as wrong RULES of the same shape. Correct option, `answer`
    # index, option order and all six corrections unchanged. Working in the
    # docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · The yeast equation",
            "q": "What does yeast produce when it respires anaerobically?",
            # UNTOUCHED — 4w correct against 2 / 4 / 3, no tell.
            "options": [
                "Ethanol and carbon dioxide",
                "Lactic acid",
                "Carbon dioxide and water",
                "Oxygen and glucose",
            ],
            "answer": 0,
            "feedback": {
                1: "That is human muscle, and the bacteria in yoghurt. Yeast "
                   "takes the other anaerobic route.",
                2: "Those are the products of aerobic respiration — the "
                   "complete breakdown. Anaerobically the job is left "
                   "unfinished.",
                3: "That is photosynthesis, and yeast cannot photosynthesise — "
                   "it is a fungus with no chlorophyll.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            # ⚑ SCIENCE CORRECTION 2 / NOTES-B8 flag 15: "no alcohol" → "almost
            # no alcohol". A trace of ethanol survives in the crumb, so the
            # absolute was false as written. Two words; the rung measures the
            # same thing. See the docstring.
            "q": "Dough contains yeast, which produces ethanol. Why is there "
                 "almost no alcohol in the finished loaf?",
            "options": [
                # 14w — was "The yeast reabsorbs it before baking" (6w). The
                # belief it already carried, given the rule that licenses it:
                # a living thing does not waste anything it has made.
                "The yeast reabsorbs it before baking, because nothing a cell "
                "makes is ever wasted",
                # 14w — Design's, unchanged.
                "It evaporates in the oven — ethanol boils well below the "
                "temperature of baking",
                # 13w — was "Bread yeast is a different species that makes no
                # alcohol" (10w). The consequence names what the student thinks
                # is left: the gas and nothing else.
                "Bread yeast is a different species that makes no alcohol, "
                "only the gas",
                # 14w — was "The flour neutralises it" (4w). The belief is that
                # ethanol behaves like an acid; the added clause states the
                # wrong rule it comes from.
                "The flour neutralises it, the way an alkali cancels an acid "
                "in a beaker",
            ],
            "answer": 1,
            "feedback": {
                0: "It does not. The ethanol is a waste product being got rid "
                   "of, not a store being kept.",
                2: "It is essentially the same organism doing the same "
                   "reaction. What differs is what happens to the products "
                   "afterwards.",
                3: "Ethanol is not an acid and there is nothing to neutralise. "
                   "It leaves as a vapour.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the yoghurt",
            "q": "Explain how warm milk becomes yoghurt, and why the yoghurt "
                 "keeps for longer in the fridge than the milk it was made "
                 "from.",
            "field_label": "Your explanation",
            "placeholder": "Bacteria are added to the milk…",
            "success": [
                "Says particular bacteria are added to warm milk deliberately.",
                "Says they respire the sugar in the milk anaerobically and "
                "produce lactic acid.",
                "Says the acid lowers the pH, which curdles the milk protein "
                "and thickens it.",
                "Says the low pH stops spoilage micro-organisms from growing.",
                "Concludes that the yoghurt therefore keeps longer — the "
                "chosen organism has made the milk uninhabitable for the "
                "others.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Design an investigation to find the temperature at which "
                 "yeast ferments fastest. Say what you would measure, what you "
                 "would keep the same, and what shape of result you would "
                 "expect — and explain what happens above the optimum.",
            "field_label": "Your design",
            "placeholder": "I would set up several flasks of yeast and sugar "
                           "solution…",
            "success": [
                "Sets up several identical flasks of yeast and sugar solution, "
                "each at a different temperature in a water bath.",
                "Measures the rate as bubbles of carbon dioxide per minute, or "
                "gas volume collected in a fixed time.",
                "Keeps the same the mass of yeast, the sugar concentration, "
                "the volume of solution and the time allowed.",
                "Predicts the rate rising with temperature to an optimum and "
                "then falling sharply.",
                # The criterion the bench's 80 °C dial exists to earn, and the
                # one that separates cold-and-slow from hot-and-dead.
                "Explains the fall above the optimum as the yeast’s enzymes "
                "being denatured — and notes this is permanent, so cooling the "
                "flask does not restore it.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Byte-identical to the page (line 267).
    "key_note": "Fermentation is anaerobic respiration carried out by "
                "micro-organisms. Yeast, a single-celled fungus, converts "
                "glucose to ethanol and carbon dioxide — the gas raises bread "
                "and the ethanol makes beer and wine. Bacteria convert sugars "
                "to lactic acid, which is how yoghurt, cheese and sauerkraut "
                "are made and why they keep. Both need sugar, warmth and no "
                "oxygen, and both stop if the organism is killed.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B8 flag 18, checked in full and left, with ONE shrink: insulin is
    # made by micro-organisms, bacteria OR yeast, not by bacteria alone. See
    # science correction 3 in the docstring.
    #
    # ⚖️ MRB-225 holds: the layer scales the bench up and retracts nothing above
    # it. Its last sentence is what makes the four dials the point of the page
    # rather than a toy.
    "stretch": [
        {"type": "explainer", "id": "the-same-vessel-scaled-up",
         "text": "The same vessel, scaled up, is one of the workhorses of "
                 "modern industry. Almost all the insulin used by people with "
                 "diabetes is now made by micro-organisms — bacteria or yeast "
                 "— carrying an inserted human gene, grown in fermenters of "
                 "several thousand litres; before that it was extracted from "
                 "the pancreases of pigs and cattle, which was expensive, in "
                 "short supply, and not quite human insulin. Antibiotics "
                 "including penicillin are grown the same way, from a fungus. "
                 "Quorn is a fungus grown in a fermenter and harvested as "
                 "food. Ethanol for fuel is made by yeast on an industrial "
                 "scale from sugar cane, and in Brazil a large share of cars "
                 "run on it. What every one of these has in common is a tank, "
                 "a chosen organism, a food supply, and careful control of "
                 "temperature, pH and oxygen — the four dials on the bench "
                 "above, with a bigger vessel."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work out what your dials would produce?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 306) and nothing in it is a safety
    # instruction — it is a note about how far the bench's model can be trusted.
    # Routing it through `safety_note` would print it in the treatment reserved
    # for "never light a candle without an adult". Byte-identical, and its last
    # sentence is load-bearing: it is the page telling the student that the
    # sugar dial is standing in for lactose.
    "convention_note": "The bench is a simplified model: rate is shown as a "
                       "percentage of the best case with one organism at a "
                       "time, and real fermentation also depends on pH, on how "
                       "much alcohol or acid has already built up, and on the "
                       "strain being used. Yoghurt bacteria work on lactose, "
                       "the sugar in milk, which the bench treats as sugar in "
                       "general.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is four independent variables against one outcome, and rung 4
    # asks for a full investigation design — control variables, a measured rate,
    # a predicted shape and an explanation of the fall past the optimum.
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
