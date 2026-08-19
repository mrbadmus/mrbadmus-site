"""B8 L1 — Aerobic respiration (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b8/b8-01-aerobic-respiration.dc.html` (586 lines), her author's
notes `docs/ks3/design-reference/b8/NOTES-B8.md`, and the B8 payload schema
`docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md` §2, §7, §8, §9 and §10, under the
MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the three items listed under "What could not be lifted", each of which is
a build-internal identifier or a sequence leak rather than a science word. The
four amounts, the three fact cards, the three exits, both marked rungs and both
self-marked rungs came out of the page's own `AMOUNTS`, `FACT_CARDS`, `RUNGS`
and `SELF_RUNGS` arrays, not off a keyboard.

── `covers` is one clause, and it is the smallest in the unit ────────────

`KS3.B.RESP.02` reads, in full: *a word summary for aerobic respiration*. That
is one sentence of statute and this lesson discharges it in `#s-summary`, where
the summary is drawn as an equation row — glucose + oxygen, a drawn arrow,
carbon dioxide + water — with the energy line beneath it as a CONDITION rather
than as a product. Rung 1 is the same statement asked as a question, and its
fourth option ("glucose + oxygen gives energy") is the exact error the condition
line exists to prevent.

`KS3.B.RESP.01` is `touches`, not `covers`. NOTES-B8 §0 gives it to b8-01 and
b8-02 *together*; `build_ks3.validate()` enforces exactly-once ownership, so it
cannot be claimed twice. b8-02 owns it, because RESP.01's load-bearing clause is
*the breakdown of organic molecules to enable all the other chemical processes
necessary for life* and that clause is the whole of b8-02. This page names
aerobic respiration and never claims the "enables everything else" argument —
its `What for` fact card points at it in one sentence and stops.

── The instrument: a ledger that balances because it cannot do otherwise ─

`#s-bench` is `mass-ledger`, on `ks3-block ks3-dark ks3-practical` (page line
105), so `practical` is MEASURED from Design's own markup rather than inferred
from the kind name — payload schema §0 rule 2, and contract §4 records that B1
got two of six wrong by inferring it.

⚖️ **`per_gram` is authored as RATIOS, and that is the whole argument.** The
model is `C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O` by mass: 180 + 6×32 = 372 in, 6×44 +
6×18 = 372 out. Per gram of glucose both sides come to 2.0667, so the two
printed totals are equal BY CONSTRUCTION at any amount, before any rounding —
which is what the page's own legal line claims and what `#s-think`'s second
paragraph sends the student back to check. A per-amount lookup table would print
the same four rows and would make the balance a coincidence the author arranged
rather than a consequence of the equation. It is not authored as one.

Verified against Design's printing rule at all four amounts (`x >= 100 ?
round(x) : x.toFixed(1)`), each column summing to its own printed total:

    Teaspoon   4 g   4.0 + 4.3  = 8.3 g   |  5.9 + 2.4  = 8.3 g   |     62 kJ
    Banana    25 g  25.0 + 26.7 = 51.7 g  | 36.7 + 15.0 = 51.7 g  |    390 kJ
    Pasta     90 g  90.0 + 96.0 = 186 g   |  132 + 54.0 = 186 g   |  1,404 kJ
    A day    300 g   300 + 320  = 620 g   |  440 + 180  = 620 g   |  4,680 kJ

⚠️ **The 100 g threshold is per VALUE, not per amount.** At 90 g the same panel
prints `132 g` beside `54.0 g`. That is Design's rule applied honestly and it is
reproduced rather than tidied — a student comparing the columns is reading the
totals, and changing the rule changes the printed totals. `units.dp_below` is
100 and it is a value threshold.

⚠️ **`units.group_thousands` exists because `toLocaleString()` is not a
formatting rule.** Design writes `kJ.toLocaleString()` (page line 521), which is
the *browser's* locale. A student whose browser is set to a European locale
would be shown `1.404 kJ`, which reads as one and a bit. The comma is authored.

⛔ **ENERGY SITS OUTSIDE BOTH TOTALS AND STAYS THERE.** `totals` names three
slots — `in`, `out`, `energy` — and the third is deliberately not summed into
either. That is not decoration: it is the visual form of the argument that
energy is not a substance. Three things on this page depend on the student
having seen it in its own column: the third exit row ("Energy — Not an exit at
all"), the `close` line under the exits panel, and rung 1's fourth distractor.
Folding it into a total would silently unteach all three.

── FOUR rail stops — Design's fourth restored (MRB-249) ──────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to be headed "THREE
rail stops, not Design's four". Design draws four (page lines 342–348) and her
`isDone()` gives `s-summary` the BENCH's predicate, character for character,
one section to the left:

    if (id === 's-bench')   return s.exits;
    if (id === 's-summary') return s.exits;      // page line 418

`#s-summary` is an eyebrow, a display statement, a drawn equation, three static
cards and a key fact: no control, no commitment, no field, no reveal. The
argument was that `ks3_parity.check_rail_reachable()` fails a stop whose
section carries none of the five DOM signals `doneByDom()` reads, that MRB-208
confined the rail to sections requiring the student to do something, and that
ALIASING would tick a stop for something done in a different section. So the
lesson shipped THREE stops.

Two things overrule that.

MRB-205 binds and is not re-argued: Design draws, we render; no invented and no
dropped page structure; page wins over engine. Dropping a stop Design drew is
not rendering what Design drew.

And the second line above is not an alias — it is Design, in a rail-level
function, saying what completes the stop. The word summary is the PAYOFF of the
ledger beside it: it carries no control precisely because the bench has already
taken the student's commitment. That relationship has a name now — a MIRROR —
and `wireRail`'s `paint()` resolves mirrors at rail level, where Design
computes them, rather than hunting for a DOM signal inside the section.

So the fourth stop is declared: anchor `s-summary`, `mirrors: "s-bench"`,
`done_when: "exits_shown"` — SUMMARY / "Word summary", Design's own strings —
and `ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`. b7-01's own `#s-summary`, b7-04's `#s-jobs`,
b4-05's `#s-stomata`, b5-06's `#s-designs` and the rest are restored the same
way. **The section keeps its anchor**, as it always did.

⚠️ Payload schema §7 pre-ruled the THREE-stop count for all five B8 pages. That
pre-ruling is superseded here and in b8-02 to b8-05; the schema's own text has
not been re-cut, so read §7's count as historical.

── What could not be lifted byte-identical, and why ─────────────────────

All three are build-internal identifiers or a sequence leak. No science word
moves in any of them.

1. **`b3-06` in the pasta note.** Design writes *"The starch is digested to
   glucose first — that is b3-06's job — and this is what arrives."* A student
   cannot resolve a slot code, and printing one is exactly the platform leakage
   §8.10 exists to stop. Resolved to the lesson TITLE, which is how b7-04
   resolved the identical shape:

       Design:  that is b3-06’s job
       Built:   that is the job of Enzymes in digestion

   The destination is not lost — `enzymes-in-digestion` is carried as a real
   `references` edge, which is where the engine puts cross-lesson navigation.

2. **`b4-01` in the first confrontation.** Design writes *"that distinction is
   `<a href="b4-01-the-gas-exchange-system.html">b4-01's</a>`, which is the
   lesson to revisit if it still feels blurred."* `rich()` allows `<em>` and
   `<strong>` and nothing else, so no hyperlink survives anywhere on the page;
   that costs nothing where the link TEXT is already a lesson title (the two
   *Conservation of mass* links and the *Gametes and fertilisation* link all
   keep their words and lose only the tag). Here the link text is a CODE, so
   dropping the tag would leave `b4-01's` in front of a student:

       Design:  that distinction is <a …>b4-01's</a>, which is the lesson
       Built:   that distinction is the subject of The gas exchange system,
                which is the lesson

   `the-gas-exchange-system` is already in `requires` — Design's own "Before
   this lesson" card — so the edge was never at risk.

3. **The fourth amount's TAB LABEL, which is a sequence leak.** Design's label
   is *"A day of a Year 9 student"*. Year and half-term never appear in a lesson
   page's bytes (§8.4 / the sequence-is-data rule), because a school can place
   this unit anywhere and a student who is not in that year is told the page is
   not for them. Rewritten to the standing phrasing:

       Design:  A day of a Year 9 student
       Built:   A day of a student your age

   ⚖️ **Design's `name` and `note` for the same amount are untouched** — "A whole
   day of carbohydrate" and "Around 300 g of carbohydrate a day, respired
   steadily whether you are running or asleep." The number, which is the science,
   is in those two strings and not in the tab. Nothing quantitative moves.

── The three fact cards keep all four of their parts ────────────────────

Design's `FACT_CARDS` are `kind` + `name` + `body` (page lines 365–369) — a mono
accent tag, a display name, a body. `_rule_card()` in `build_ks3.py` reads
`role` (or `label`) for the tag, `term`/`name`/`title` for the name, and
`gloss`/`body`/`close` for the body, so the shape maps one-to-one and the tag
renders in its own treatment. `kind` is renamed to `role` and **nothing is
joined, dropped or invented** — this is the repair `_rule_card` took under
MRB-245 after b7-01's four part cards shipped as empty `<li>`s. b7-04 had to
join its tag into its term with a middle dot; this lesson does not, because the
slot now exists.

Likewise the KEY FACT is authored NESTED, `{"ref": …, "ground": "card"}` inside
the `rule` block, which is Design's own arrangement (page lines 201–204: inside
`#s-summary`, on `--ks3-card` with the 5px accent offset shadow). `r_rule()`
takes a nested key fact and defaults it to `card` for the reason this page
needs — the section is already `--ks3-band` and band on band is invisible. Same
as b7-01. Never amber: measured, the box is card + ink outline + accent shadow.

── ⊕ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS ARE CLEAN ──

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so `+` counts as one and an em dash counts as
one). The gate flags a correct option that is strictly the longest AND clears
the longest distractor by ≥4 words or by ≥1.4×:

    rung 1  correct 8w vs 8 / 4 / 5   — not strictly longest       ✓ clean
    rung 2  correct 11w vs 9 / 6 / 3  — gap 2, ratio 1.22          ✓ clean

**No distractor on this page was rewritten, and none needed to be.** That is not
luck, it is the construct: on rung 1 the correct answer states an EQUATION and
all three distractors state equations — right substances wrong direction, a
missing reactant, energy as a product. On rung 2 the correct answer names an
EXIT ROUTE for the mass and all three distractors name routes or fates for the
same mass — converted to energy, out in urine and sweat, turned into muscle.
Same subject, same shape, same kind of consequence, which is exactly what the
MRB-177 ruling asks for and is why the length parity falls out rather than being
imposed. Every option, every `answer` index, Design's option ORDER and all six
corrections are byte-identical.

⚖️ **Rung 2's fourth option is three words long and it is still not a length
tell.** "Turned into muscle" is short because the belief is short; it is the
"fat turns into muscle" claim, which is one of the most widely held in the
subject, and padding it into a rule would make it sound more considered than the
student's own version of it. The gate measures the correct option against the
LONGEST distractor (9w), not the shortest, and it passes with room. Recorded so
a later pass does not "fix" a clean rung.

⚑ For Mide's science gate — every NOTES-B8 flag landing on THIS lesson, and
  what was checked against it. Five flags, five checked, **none corrected**:

  * flag 1   **"Most of the fat you lose is breathed out"** (hook reveal, and
             rung 2's correct option). CHECKED AND LEFT, UNQUANTIFIED, and the
             claim as Design drew it is TRUE AS WRITTEN. The published split
             (Meerman & Brown, 2014) is about 84% of the mass exhaled as carbon
             dioxide and about 16% leaving as water; "most of it was breathed
             out as carbon dioxide, and the rest left as water" is precisely
             that, without a figure. MRB-225 says a claim shrinks until it is
             true; it does not say add numbers to a claim that is already
             inside its own hedge. Nothing was added. If Mide wants the split
             stated it lands in exactly two places — the hook reveal and rung
             2's correct option — and the second is a correct answer, which
             makes it a ruling rather than an edit.

  * flag 2   **The ledger arithmetic and 15.6 kJ per gram.** CHECKED AND LEFT,
             and both halves verify. The mass ratios are the balanced equation
             (180 : 192 : 264 : 108, both sides 372) and the four-amount table
             above reproduces every printed figure including the two rounding
             asymmetries at 90 g. 15.6 kJ/g is the standard energy density of
             glucose — 2,803 kJ per mole ÷ 180 g per mole = 15.57 — and the
             page's legal line already calls the energy figures approximate.
             The energy column is OUTSIDE both totals and stays there; see the
             ⛔ note above for the three strings that depend on it.

  * flag 3   **"Respiration is not burning"** (`#s-think`, first belief).
             CHECKED AND LEFT, and the framing is the right one. The paragraph
             does not deny the chemistry — its own first sentence concedes that
             the overall equation is the same as burning sugar — and then
             locates the difference where it actually is: uncontrolled release
             at high temperature versus a long series of small enzyme-controlled
             steps at 37 °C, with no flame and no ignition. That is MRB-225
             satisfied in Design's own drawing: the claim is stated at the size
             that is true, and no later sentence takes any of it back. The
             schemes that teach "respiration is a form of combustion" are the
             ones with the overstatement, not this page. ⚑ One soft figure
             inside it: "several hundred degrees" for a sugar flame UNDERSTATES
             (a sugar flame is well above a thousand), so it errs safe, and the
             sentence's work is the contrast with 37 °C rather than the number.

  * flag 4   **Mitochondria as former bacteria, about a billion and a half
             years ago, own DNA, own division** (*Going further*). CHECKED AND
             LEFT. Endosymbiosis is the accepted explanation, which is exactly
             how Design words it — *"the accepted explanation is that they
             began as free-living bacteria"* — rather than as a bare fact.
             Mitochondria do carry their own small circular genome and do
             divide on their own schedule. Published dates for the mitochondrial
             endosymbiosis span roughly 1.45–2.0 billion years ago; "about a
             billion and a half" sits at the recent end of that range and is
             inside it. Left as drawn, and the hedge in "accepted explanation"
             is load-bearing — it is what makes this a *how do we know* story in
             the stretch layer rather than a disclaimer bolted to a claim.

  * flag 5   **"By some counts a third of its volume"** (heart muscle cell
             mitochondria, *Going further*). CHECKED AND LEFT — and this is the
             flag the dispatch expected to need softening, so the working is
             given in full. Mitochondrial volume density in mammalian
             cardiomyocytes is genuinely around a third: rodent hearts are
             commonly reported near 35%, human left-ventricular myocytes
             typically in the 23–32% band, and the figure varies with species,
             chamber and training state. "A third" therefore sits at the top of
             the human range and inside the mammalian one. ⚖️ **Design has
             already shrunk the claim herself: "by some counts" is an explicit
             attribution, and it is true that some counts give a third.** That
             is the MRB-225 move performed in the drawing, so performing it
             again would be softening a claim that is not overstated. The three
             words "by some counts" are load-bearing and must not be trimmed by
             a later pass. If Mide wants the human band specifically, the
             narrowest edit is "by some counts a quarter to a third of its
             volume", in this one sentence only — the figure appears nowhere
             else in the lesson, and the sentence beside it ("a skin cell has a
             fraction of that") is a comparison and survives either wording.

  * flag 21  **No figures, and it is MEASURED.** `<img>`, `<figure>` and
             `<picture>` each appear ZERO times on this page — grepped, not
             assumed — and the foot line names no slot. §4.10 allows an empty
             `figures` for a lesson carried by its interactives. Nothing is
             declared, because declaring a slot the page never references would
             invent a sourcing task in `docs/ks3/diagram-manifest.md`. Flag 21
             names a mitochondrion as the obvious candidate and it is not
             dropped by this — it is Mide's to rule on.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the one claim that could have gone wrong, because the lesson makes it
five times: *mass is conserved, energy is transferred, energy is not a
substance*. Hook reveal ("Nothing was converted into energy — energy is
transferred"), the ledger's two matching totals, the third exit row ("Not an
exit at all"), the `close` line ("The third has none"), `#s-think`'s second
paragraph, rung 1's fourth correction and rung 2's first correction all say the
same thing at the same size. Nothing above is walked back below. The stretch
layer adds the origin of mitochondria and retracts nothing.

── Misconception ids: RESP-01 and RESP-02, and a spare left unused ───────

⚠️ **The `RESP` prefix row does not yet exist in
`docs/ks3/misconception-register.md`.** Grepped: fourteen prefixes are open and
`RESP` is not among them. NOTES-B8 §5 asserts the ten entries were "written into
the register with a new prefix row"; they were not — the identical claim
NOTES-B5 and NOTES-B7 made about `REPRO` and `PLANT`, third occurrence. Payload
schema §11.4 records it. **That file is not this pass's to edit** (contract §0),
so the two statements are authored here in register voice, byte-identical to
Design's quoted beliefs, and are reported for whoever opens the row. No gate
resolves an id against the register file — `verify_ks3.py`, `ks3_parity.py` and
`build_ks3.py` do not read it — so the lesson builds either way; what is at risk
is the register's completeness, not this page.

`RESP-11` is this lesson's named spare and is deliberately left **UNUSED** — a
permanent gap, the same discipline as `DRUG-07`, `REPRO-17`/`20`/`21`/`23` and
`PLANT-09`..`12`. Do not re-point it and do not renumber down into it.

Both values resolve against the BUILT page (MRB-244): `s-think` is the
confrontation block's emitted anchor and `s-hook` is the hook's. `RESP-01` gets
no `elicited_by` at all, and that is measured rather than forgotten — nothing on
this page asks the student to state "respiration is just slow burning" or offers
it as an option; the belief arrives already held. Absence is legal (MRB-248) and
inventing an element name to fill the key would be worse than the gap.

── Keys this pass authors that the ENGINE pass must wire (contract R5) ───

R5 says no key is authored without a read site in the same pass. The renderer
for `mass-ledger` belongs to the engine pass, so the read sites are named here
explicitly rather than left to be discovered. Every one is measured off Design's
own `renderVals()`:

    progress    {"before", "after"}                page line 504 (`benchProgress`)
    per_gram    ratios × `grams`                    page lines 350–352, 461
    units       `dp_below` → the `fmt()` rule       page line 462
                `group_thousands` → the comma       page line 521 (see ⚠️ above)
    totals      three labels, three slots           page lines 154–156
    run_label   idle state of the reveal button     page line 522
    ran_label   spent state of the same button      page line 522
    close       the line under the exits panel      page line 530 (`exitsNote`)

⚠️ **`start` IS authored and its value is load-bearing.** Design's `startAmount`
default is `banana`, which is `AMOUNTS[1]` and NOT the first tab — so a renderer
that opens on the first amount does NOT reproduce the page. (b7-04 omitted the
equivalent key precisely because its default WAS index 0; the reasoning is the
same and the answer is opposite.) The ledger opens on a banana because 25 g is
the amount whose four figures a student can hold in their head at once.

⛔ **NO RUNTIME STATE IS AUTHORED** (payload schema §0 rule 3). NOTES-B8 §2.1's
payload sketch implies `amount` and `exits`; both are values the runtime owns,
and under R5 a key with no read site fails `ks3_key_audit.py`. The renderer
initialises its own state, and `exits` is one-way — Design draws no un-reveal.

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
instrument class at (0,1,0). That is the engine pass's problem rather than this
module's, and it is recorded here because this payload is what feeds it; as of
MRB-245 `ks3_parity.check_dark_text_specificity()` gates it.
"""

# ── the four amounts (page lines 354–363) ────────────────────────────────
#
# `grams` is the only number the model needs; oxygen, carbon dioxide, water and
# energy are all derived from it through `per_gram`, which is what makes the two
# totals match by construction rather than by arrangement. See the docstring.
#
# ⚠️ The fourth `label` is the ONE student-facing string on this page that is
# not Design's, and it is a sequence leak rather than a science word — see
# "What could not be lifted" 3. Its `name` and `note`, which carry the 300 g,
# are untouched.
AMOUNTS = [
    {"id": "teaspoon", "label": "A teaspoon of sugar",
     "name": "A teaspoon of sugar", "grams": 4,
     "note": "Roughly one sugar cube, or what goes in a cup of tea."},

    # Design's `startAmount` default, and `start` below points at it.
    {"id": "banana", "label": "A banana", "name": "A banana", "grams": 25,
     "note": "About 25 g of sugar, once the starch in it has been digested."},

    # ⚠️ `b3-06` resolved to its lesson title — "What could not be lifted" 1.
    # The destination survives as a `references` edge.
    {"id": "meal", "label": "A plate of pasta", "name": "A plate of pasta",
     "grams": 90,
     "note": "The starch is digested to glucose first — that is the job of "
             "Enzymes in digestion — and this is what arrives."},

    # ⚠️ LABEL REWRITTEN. Design: "A day of a Year 9 student".
    {"id": "day", "label": "A day of a student your age",
     "name": "A whole day of carbohydrate", "grams": 300,
     "note": "Around 300 g of carbohydrate a day, respired steadily whether "
             "you are running or asleep."},
]

# ── the three fact cards (page lines 365–369) ────────────────────────────
#
# Design's `kind` is the mono accent tag and maps to `role`, which is the slot
# `_rule_card()` reads for it. All four strings per card survive unchanged and
# nothing is joined — see the docstring. Where / When / What for, in her order:
# the three questions a PROCESS lesson has to answer about its reaction.
FACT_CARDS = [
    {"role": "Where", "name": "In the mitochondria",
     "body": "Every living cell has them, and cells that work hardest have the "
             "most. Not in the lungs, not in the blood — in the cells "
             "themselves."},
    {"role": "When", "name": "Continuously",
     "body": "There is no off switch. A cell that stops respiring for more "
             "than a few minutes dies, which is what makes this the reaction "
             "the others depend on."},
    # ⚖️ This card is the whole of `KS3.B.RESP.01`'s second clause, in three
    # lines, and it is deliberately not expanded: b8-02 owns that statement and
    # this is a reference rather than a restatement (§4.6).
    {"role": "What for", "name": "Every other process",
     "body": "Movement, keeping warm, building new molecules, active "
             "transport, nerve signals. The energy is not stored again — it is "
             "spent."},
]

# ── the three exits (page lines 525–529) ─────────────────────────────────
#
# ⛔ The third row is not a fourth product. It is the argument that energy is
# not a substance, made as a row in a list of exits so that a student who has
# just watched two totals match sees why the third figure was never in either.
# `close` below is the sentence that names it. See the docstring's ⛔ note.
EXITS = [
    {"name": "Carbon dioxide",
     "route": "Dissolves into the blood, is carried to the lungs, and diffuses "
              "into the alveoli. You breathe it out without noticing — this is "
              "the exit almost nobody names."},
    {"name": "Water",
     "route": "Some is used by the body, some leaves in urine and sweat, and a "
              "surprising amount leaves as vapour in your breath. Breathe on a "
              "cold window and that is respiration you are looking at."},
    {"name": "Energy",
     "route": "Not an exit at all. It is transferred to the cell to do work, "
              "and what is not used usefully warms you — which is why a room "
              "full of people gets hot."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 146 character for character.
    "slug":        "aerobic-respiration",
    "title":       "Aerobic respiration",
    "discipline":  "biology",
    "unit":        "respiration",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.RESP.02` — "a word summary for aerobic respiration" — owned whole
    # and discharged by `#s-summary` and rung 1. See the docstring.
    "covers":      ["KS3.B.RESP.02"],
    # Named, used, and owned elsewhere. RESP.01 is b8-02's, and this page's
    # `What for` card points at it in three lines without teaching it. PHOT.01
    # is b7-01's, and it is the whole of the `#s-summary` statement ("read from
    # right to left"). AEC.04 is c2-06's conservation of mass, which the hook,
    # the ledger and the second confrontation all lean on and none restates.
    "touches":     ["KS3.B.RESP.01", "KS3.B.PHOT.01", "KS3.C.AEC.04"],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 2},
                    {"id": "substances-and-reactions", "level": 2},
                    {"id": "cells-and-systems", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. Both exist and both
    # build, so both stay in `requires` — `build_ks3.py` silently skips a slug
    # it cannot find, which is the trap b7-04 hit with an unbuilt P1 edge.
    "requires":    ["the-photosynthesis-reaction", "the-gas-exchange-system"],
    "assumes":     [],
    # Design's "Connects to" card is the first two, in her order. The last two
    # are the destinations of stripped inline links: `enzymes-in-digestion` from
    # the pasta note ("What could not be lifted" 1) and `gametes-and-
    # fertilisation` from the stretch layer. `the-gas-exchange-system` carries a
    # stripped link too and is not repeated here — it is already in `requires`.
    "references":  [{"unit": "C2", "lesson": "conservation-of-mass"},
                    "why-every-cell-respires",
                    {"unit": "B3", "lesson": "enzymes-in-digestion"},
                    {"unit": "B5", "lesson": "gametes-and-fertilisation"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "The balanced symbol equation, ATP as the energy currency, "
                   "and the metabolic rate calculations behind respirometer "
                   "data.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "The reaction that keeps you alive is the photosynthesis "
                    "equation run backwards, at body temperature, without a "
                    "flame — and its main product leaves through your mouth "
                    "without you noticing.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-summary` is the third: no control
    # of its own, so it mirrors `s-bench` and ticks on the ledger's predicate —
    # see the docstring, which also supersedes payload schema §7's three-stop
    # count. `short` and `label` are Design's own `RAIL_SHORT` and `RAIL`
    # strings (page lines 342–348), SUMMARY / "Word summary" included.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Ten kilograms",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.exits` (page line 417). The stop
        # ticks when the student has asked where it all goes, not when a tab
        # has been pressed — switching amounts reveals nothing new.
        {"anchor": "s-bench", "short": "LEDGER", "label": "The ledger",
         "done_when": "exits_shown"},
        {"anchor": "s-summary", "short": "SUMMARY", "label": "Word summary",
         "mirrors": "s-bench", "done_when": "exits_shown"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. C is the correct one
    # and the reveal says so at once; the hook is not a trick, it is a claim the
    # ledger then has to earn in grams.
    #
    # ⚖️ Option A is `RESP-02` in the student's own words, which is why the
    # misconception below names `s-hook` as its `elicited_by`. The student who
    # picks A has stated the belief before the page names it.
    #
    # ⚠️ The inline link to `Conservation of mass` loses its tag and keeps every
    # word — the link TEXT is already the lesson title, so nothing is lost but
    # the anchor, and the edge is carried in `references`.
    "phenomenon": {
        "kind": "narrative",
        "title": "Someone loses 10 kg of fat. Where does the 10 kg go?",
        "prompt": "The mass has to go somewhere — matter is not destroyed, as "
                  "you established in Conservation of mass. Ten kilograms left "
                  "a person's body, and almost nobody, including most adults, "
                  "can say by which exit.",
        "commit": "Which way did it leave?",
        "options": [
            "It was converted into energy and stopped existing",
            "It left in urine and sweat",
            "It was breathed out",
            "It turned into muscle",
        ],
        # ⚑ NOTES-B8 flag 1. "Most … and the rest left as water" is true as
        # written and is left unquantified — see the docstring.
        "reveal": "Most of it was breathed out as carbon dioxide, and the rest "
                  "left as water. Fat is mostly carbon and hydrogen; "
                  "respiration joins that carbon to oxygen and the result is a "
                  "gas you exhale. You lose weight through your lungs. Nothing "
                  "was converted into energy — energy is transferred, and the "
                  "atoms all still exist somewhere.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # The commander's pre-allocation. Both statements are Design's own quoted
    # beliefs, byte-identical from page lines 212 and 216, in register voice.
    #
    # ⚠️ The `RESP` prefix row is NOT yet open in
    # `docs/ks3/misconception-register.md` — see the docstring. That file is not
    # this pass's to edit; the statements below are what belongs in it.
    #
    # `RESP-11` is this lesson's spare and is deliberately left UNUSED, a
    # permanent gap. Do not re-point it.
    #
    # Both `confronted_by` values resolve against the BUILT page (MRB-244):
    # `s-think` is the confrontation block's emitted anchor, `s-hook` is the
    # hook's. A rung shorthand would not resolve and is not used.
    "misconceptions": [
        # No `elicited_by`: nothing on this page asks the student to state this
        # belief or offers it as an option. Measured, not forgotten — absence is
        # legal and inventing an element name would be worse than the gap.
        {"id": "RESP-01",
         "statement": "Respiration is just slow burning.",
         "confronted_by": "s-think"},
        # Elicited by the hook: option A is this belief, word for word, and the
        # student commits to it or declines to before the page names it.
        # Confronted in `#s-think`, whose second paragraph sends them back to
        # the ledger's two matching totals for the evidence.
        {"id": "RESP-02",
         "statement": "The fat is converted into energy, so the mass "
                      "disappears.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B8, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ "breathing" is included even though it is B4's word, because the
    # respiration/breathing confusion is half of `RESP-01` and the key fact
    # ends on it. It is glossed as the CONTRAST, not re-taught.
    "vocabulary": [
        {"term": "aerobic respiration",
         "definition": "The reaction that transfers energy from glucose using "
                       "oxygen, producing carbon dioxide and water.",
         "note": "Aerobic means with oxygen."},
        {"term": "mitochondria",
         "definition": "The structures inside a cell where aerobic respiration "
                       "happens.",
         "note": "Cells that work hardest carry the most of them."},
        {"term": "glucose",
         "definition": "A sugar, and the fuel most cells respire.",
         "note": "Starch has to be digested to glucose before a cell can use "
                 "it."},
        {"term": "breathing",
         "definition": "The muscular job of moving air in and out of the "
                       "lungs.",
         "note": "It supplies the reaction. It is not the reaction."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and the foot line names no slot.
    # Declaring one would invent a sourcing task in
    # `docs/ks3/diagram-manifest.md`. NOTES-B8 flag 21 is not dropped by this.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b8/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md §2. The
        # read sites the engine pass must wire are listed in the docstring.
        {"type": "mass-ledger", "id": "the-books-balance",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · weigh both sides",
         "heading": "The books have to balance",
         "prompt": "The energy transferred is not part of either total.",
         # Design's mono line beside the heading (page line 504): the two
         # states of the section, not a counter.
         "progress": {"before": "ledger only", "after": "exits shown"},

         "options_label": "Glucose respired",
         "amounts": AMOUNTS,
         # LOAD-BEARING: `banana` is AMOUNTS[1], not [0]. See the docstring.
         "start": "banana",

         # The model, from the balanced equation — RATIOS, never a per-amount
         # table. 180 g glucose + 192 g oxygen gives 264 g carbon dioxide +
         # 108 g water; both sides come to 2.0667 per gram of glucose, so the
         # two totals are equal by construction at any amount. The energy
         # figure is NOTES flag 2 and is on Mide's gate.
         "per_gram": {"oxygen": 192 / 180,
                      "carbon_dioxide": 264 / 180,
                      "water": 108 / 180,
                      "kj": 15.6},

         "columns":  {"in": "Goes in", "out": "Comes out"},
         "rows_in":  [{"id": "glucose", "name": "Glucose"},
                      {"id": "oxygen", "name": "Oxygen"}],
         "rows_out": [{"id": "carbon_dioxide", "name": "Carbon dioxide"},
                      {"id": "water", "name": "Water"}],
         # ⛔ THREE slots, and the third is NOT summed into either of the other
         # two. See the docstring — three strings on this page depend on the
         # student having seen the energy figure in its own column.
         "totals":   {"in": "Total in", "out": "Total out",
                      "energy": "Energy transferred"},
         # `dp_below` is a per-VALUE threshold, so at 90 g the panel prints
         # "132 g" beside "54.0 g" — Design's rule applied honestly.
         # `group_thousands` authors the comma rather than inheriting the
         # browser's locale from `toLocaleString()`.
         "units":    {"mass": " g", "energy": " kJ",
                      "dp_below": 100, "group_thousands": True},

         "run_label": "Where does it all go?",
         "ran_label": "Exits shown",
         "exits_label": "Which way each product leaves",
         "exits": EXITS,
         "close": "Two of those three have mass and are in the ledger. The "
                  "third has none, which is exactly why it is listed "
                  "separately — energy is not a substance leaving the body."},

        # #s-summary — the band panel, and the section that discharges
        # KS3.B.RESP.02. Rail stop 3, mirroring `s-bench`; see the docstring.
        {"type": "rule", "anchor": "s-summary",
         "eyebrow": "The word summary",
         "statement": "Photosynthesis, read from right to left.",

         # ⚠️ THE ARROW IS NOT A CHARACTER. `arrow` holds the WORD the drawn
         # arrow means — the same word all four of rung 1's options use when
         # they speak the summary aloud — and the SVG geometry is Design's and
         # lives in the engine. There is deliberately no field a U+2192 could
         # be typed into; the design system's latin subsets do not carry one.
         #
         # `condition` is Design's mono line set full-width beneath the row
         # (page line 188). It is where the energy goes, and it is a separate
         # field for the same reason b7-01's is: energy is not a product, and
         # rung 1's fourth option is the error this line prevents.
         "equation": {
             "reactants": "glucose + oxygen",
             "arrow":     "gives",
             "products":  "carbon dioxide + water",
             "condition": "energy is transferred from the glucose to the cell",
         },

         "cards": FACT_CARDS,

         # Design nests the key fact inside this section (page lines 201–204)
         # on the CARD ground with the accent offset shadow. `card`, because
         # the section itself is `band` and band on band is invisible — the
         # same arrangement and the same reason as b7-01's.
         "key_fact": {"ref": "respiration-is-a-reaction-not-a-breath",
                      "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "RESP-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-summary on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 203
    # and identical to payload schema §9's b8-01 entry.
    "key_facts": [
        {"id": "respiration-is-a-reaction-not-a-breath",
         "text": "Aerobic respiration is glucose + oxygen giving carbon "
                 "dioxide + water, releasing energy the cell can use. It "
                 "happens in the mitochondria of every living cell, "
                 "continuously, and it is a chemical reaction — not breathing, "
                 "which is the muscular job that supplies it.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, payload
        # schema §8), so it is a `confrontation` and not a `predict`, it is not
        # a rail stop, and it emits no completion contract. Contract R1's
        # `predict` branch applies where `#s-think` gates a reveal behind a
        # commitment; no B8 page does.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "RESP-01",
         "statements": [
             # ⚑ NOTES-B8 flag 3. Checked and left; the reasoning is in the
             # docstring. The first sentence CONCEDES the shared equation and
             # the paragraph then locates the difference — no claim is made
             # here that a later sentence takes back.
             #
             # ⚠️ `b4-01` resolved to its lesson title — "What could not be
             # lifted" 2. The destination is already in `requires`.
             {"quote": "Respiration is just slow burning.",
              "body": ["The overall equation is the same as burning sugar, and "
                       "that is where the resemblance stops. Set fire to "
                       "glucose and it releases everything it has in one "
                       "uncontrolled rush at several hundred degrees — "
                       "useless to a cell, and fatal to it. Respiration takes "
                       "the same molecule apart in a long series of small "
                       "enzyme-controlled steps at 37 °C, capturing the energy "
                       "in usable amounts along the way, and it needs no flame "
                       "and no spark to start. The comparison is worth making "
                       "precisely because of where it breaks: a fire is a "
                       "reaction that has escaped control, and a cell is the "
                       "opposite. The other half of the confusion is the word "
                       "itself. Respiration is a chemical reaction inside "
                       "cells; breathing is the muscular job that delivers the "
                       "oxygen for it, and that distinction is the subject of "
                       "The gas exchange system, which is the lesson to "
                       "revisit if it still feels blurred."]},
             # This paragraph is why the ledger is upstream of it in the
             # document: "Look at the ledger above" is a real instruction to a
             # real instrument the student has already run, and the two
             # matching totals are the evidence. The `Conservation of mass`
             # link loses its tag and keeps its words.
             {"quote": "The fat is converted into energy, so the mass "
                       "disappears.",
              "body": ["Mass cannot turn into energy in a chemical reaction — "
                       "that is the whole content of Conservation of mass, and "
                       "biology does not get an exemption. Look at the ledger "
                       "above: every atom that goes in comes out, and the two "
                       "totals are identical to the gram. What the glucose or "
                       "fat supplies is a store of chemical energy, and "
                       "respiration transfers that energy to the cell while "
                       "rearranging exactly the same atoms into carbon dioxide "
                       "and water. The carbon you exhale today was in your "
                       "breakfast, and before that in a plant, and before that "
                       "in the air. Weigh the reactants and weigh the products "
                       "and nothing has gone missing; the only thing that has "
                       "moved is energy, from a store to where it was "
                       "needed."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — MEASURED, BOTH MARKED RUNGS CLEAN, NOTHING
    # REWRITTEN. rung 1 correct 8w against 8 / 4 / 5 (not strictly longest);
    # rung 2 correct 11w against 9 / 6 / 3 (gap 2, ratio 1.22). Both are inside
    # `length_tell()` because the distractors already state the same KIND of
    # thing as the correct answer — equations on rung 1, exit routes for the
    # same mass on rung 2. Full working in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · The summary",
            "q": "Which is the word summary for aerobic respiration?",
            # All four are equations, which is what keeps the rung clean: the
            # student cannot pick by shape. B is photosynthesis (the single
            # most common error in the topic and Design says so in its own
            # correction), C drops a reactant, D makes energy a product — the
            # error `#s-summary`'s condition line exists to prevent.
            "options": [
                "glucose + oxygen gives carbon dioxide + water",
                "carbon dioxide + water gives glucose + oxygen",
                "oxygen gives carbon dioxide",
                "glucose + oxygen gives energy",
            ],
            "answer": 0,
            "feedback": {
                1: "That is photosynthesis. Same four substances, opposite "
                   "direction, and mixing them up is the single most common "
                   "error in this topic.",
                2: "Nothing has been built from nothing. Oxygen alone is not a "
                   "fuel — the carbon in the carbon dioxide has to come from "
                   "the glucose.",
                3: "Energy is not a substance and cannot be a product. There "
                   "are two products with mass, and the energy is transferred "
                   "as they form.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A person loses 10 kg of fat over a year. Where has almost "
                 "all of that mass gone?",
            # ⚑ The correct option is NOTES-B8 flag 1's second site. If Mide
            # rules the 84/16 split should be stated, it lands here and in the
            # hook reveal — and this one is a correct answer, so it is a
            # ruling rather than an edit. See the docstring.
            #
            # ⚖️ Option D is three words and is still not a length tell: the
            # gate measures against the LONGEST distractor, the belief is short
            # because students hold it short, and padding it would make it
            # sound more considered than their own version. Do not "fix" it.
            "options": [
                "It was converted into energy and no longer exists",
                "Breathed out as carbon dioxide, with the rest leaving as "
                "water",
                "Passed out in urine and sweat",
                "Turned into muscle",
            ],
            "answer": 1,
            "feedback": {
                0: "Mass is not converted into energy in a chemical reaction. "
                   "Weigh both sides of the ledger above: nothing is missing.",
                2: "Some water leaves that way, but the carbon — which is most "
                   "of the mass — leaves as a gas through the lungs.",
                3: "Muscle is built from protein and would show as a weight "
                   "gain, not a loss. The fat itself has gone somewhere, and "
                   "it left as gas.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the exercise change",
            "q": "When you run, you breathe faster and deeper and your heart "
                 "beats harder. Explain why, starting from what your muscle "
                 "cells are doing.",
            "field_label": "Your explanation",
            "placeholder": "The muscle cells are contracting, which…",
            # The fifth criterion is `RESP-01`'s second half marked as a
            # criterion rather than as prose, which is why the confrontation
            # above can stay static and still be assessed.
            "success": [
                "Says the working muscle cells need more energy, so they "
                "respire faster.",
                "Says faster respiration uses up glucose and oxygen more "
                "quickly and makes carbon dioxide more quickly.",
                "Says breathing faster and deeper gets more oxygen into the "
                "blood and removes carbon dioxide from it.",
                "Says the heart beats harder to deliver that blood to the "
                "muscles more quickly.",
                "Makes clear that breathing and respiration are two different "
                "things — breathing supplies the reaction, it is not the "
                "reaction.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Germinating peas are sealed in a flask with a thermometer, "
                 "alongside a second flask of peas that have been boiled and "
                 "cooled. Both are left overnight. Predict what happens to the "
                 "temperature, the oxygen and the carbon dioxide in each "
                 "flask, and explain why the boiled peas are there.",
            "field_label": "Your answer",
            "placeholder": "In the flask of living peas…",
            # Criteria 4 and 5 are the `experimental-skills` half of `ws`: the
            # boiled flask is a control and the rung marks whether the student
            # can say what it controls FOR.
            "success": [
                "Predicts the living peas warm up, because respiration "
                "transfers energy and not all of it does useful work.",
                "Predicts oxygen falls and carbon dioxide rises in the living "
                "flask.",
                "Predicts no change of any kind in the boiled flask, because "
                "those peas are dead and are not respiring.",
                "Says the boiled peas are the control — they rule out warming "
                "or gas changes caused by anything other than living cells.",
                "Notes that both flasks must be otherwise identical, including "
                "being at the same starting temperature.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Glucose + oxygen gives carbon dioxide + water, and energy is "
                "transferred to the cell. It happens in the mitochondria of "
                "every living cell, all the time, in small enzyme-controlled "
                "steps at body temperature. No mass is lost: every atom in the "
                "reactants appears in the products, which is why weight lost "
                "as fat leaves mostly through the lungs.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B8 flags 4 and 5 both live in this one paragraph, and both are
    # checked and left — the working is in the docstring. Design's own hedges
    # are load-bearing in both: "by some counts" attributes the third, and "the
    # accepted explanation" is what makes endosymbiosis a *how do we know*
    # story rather than a bare assertion. Neither may be trimmed.
    #
    # ⚖️ MRB-225 holds: the layer adds the origin of the organelle and retracts
    # nothing above it. The `Gametes and fertilisation` link loses its tag and
    # keeps its words.
    "stretch": [
        {"type": "explainer", "id": "what-mitochondria-used-to-be",
         "text": "Mitochondria are where the reaction happens, and how many a "
                 "cell has tells you what it does for a living. A heart muscle "
                 "cell, contracting every second of your life without a break, "
                 "is packed with them — by some counts a third of its volume. "
                 "A skin cell has a fraction of that. Sperm cells carry a "
                 "spiral of mitochondria wrapped around the base of the tail, "
                 "powering the only journey they will ever make, and you met "
                 "that in Gametes and fertilisation. Stranger still, "
                 "mitochondria have their own small loop of DNA and divide on "
                 "their own schedule, which is why the accepted explanation is "
                 "that they began as free-living bacteria absorbed by a larger "
                 "cell about a billion and a half years ago and never left. "
                 "Every breath you take supplies oxygen to what were once "
                 "someone else's cells."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check where the atoms in your breakfast ended "
                      "up?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ MRB-257 · audit 6.4 — RULED BY MIDE, and the wording is the ruling.
    # The safeguarding blocks named no confidential service: a sweep for
    # childline|0800 1111|nspcc|samaritans|papyrus|frank|shout across all 58
    # rendered pages returned ZERO. This is a public site, and the student who
    # most needs this block is reading it at 11pm, when "your school's PSHE
    # materials" is not reachable. The service is Childline, the number is
    # 0800 1111, joined by a spaced em dash. Shout and FRANK were offered and
    # NOT taken up. The PSHE deferral STAYS as the daytime route — Childline is
    # the out-of-hours one, not a replacement for it.
    #
    # ⚠️ THE TREATMENT IS THE RULING TOO (§8.10): a small `ks3-legal` foot line
    # alongside the existing school-nurse / pharmacist / GP routes, NEVER a
    # callout block. A helpline should be findable and quiet.
    #
    # ⊕ Also audit 6.19 — this was the ONE body-related hook in 58 lessons with
    # no closing safeguarding line ("Someone loses 10 kg of fat. Where does the
    # 10 kg go?"). Every other body-touching page carries one; this closes it.
    "safeguarding_note": "If any of this is about you or someone you know, "
                         "talk to someone you trust — a parent or carer, a "
                         "teacher, your school nurse, a pharmacist or your "
                         "GP. Out of school hours: Childline — 0800 1111, "
                         "free and confidential.",

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 332) and nothing in it is a safety
    # instruction — it is a note about how far the ledger can be trusted.
    # Routing it through `safety_note` would print it in the treatment reserved
    # for "never light a candle without an adult", which devalues the safety
    # line. b3-05, b3-07, b4-01, b5-06 and b7-04 resolve the identical foot line
    # the identical way.
    #
    # ⚑ Its first clause is the honest half of NOTES-B8 flag 2 and is
    # load-bearing: it is the page telling the student that the totals match
    # BECAUSE of the equation, not because someone measured them and got lucky.
    "convention_note": "The ledger is calculated from the balanced equation "
                       "and rounded, so the two totals match to the gram by "
                       "construction. Real bodies respire fats and proteins as "
                       "well as glucose, the proportions shift with diet and "
                       "activity, and some of the water made is retained "
                       "rather than exhaled. Energy figures are approximate "
                       "values per gram of glucose.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The ledger is a quantitative model whose whole point is that the totals
    # can be checked rather than believed, and rung 2 asks for a conclusion to
    # be defended against a strongly held alternative — analysis and
    # evaluation. Rung 4 is a control-and-variables question in everything but
    # name: identify the control, say what it controls for, and name what must
    # be held identical.
    "ws": ["analysis-and-evaluation", "experimental-skills"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
