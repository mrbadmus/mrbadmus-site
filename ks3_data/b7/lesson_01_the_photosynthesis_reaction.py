"""B7 L1 — The photosynthesis reaction (PROCESS).

Authored against Design's approved page,
`docs/ks3/design-reference/b7/b7-01-the-photosynthesis-reaction.dc.html` (588 lines), under
the MRB-220 build contract and `docs/ks3/b7-inventory/PAYLOAD-SCHEMA.md`.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted" and the three rung-2
distractors rewritten under MRB-177, both sections below. The four dials, the
three readouts, the seven iodine verdicts, the four part cards, the four hook
options and all four ladder rungs came out of the page's own `<script>`, not
off a keyboard.

── ⚠️ THE ARROW IS DRAWN, AND THERE IS NO SLOT TO TYPE ONE INTO ─────────

This lesson is the first consumer of the MRB-204 arrow amendment, and the
whole point of the `equation` payload below is that **the arrow is not a
string**. NOTES-B7 flag 4: the design system's fonts have no U+2192, so a typed
arrow falls back to a system font mid-line. Design draws it as an inline SVG
inside the equation component (page line 167), measured:

    viewBox "0 0 60 24", width 60, height 24,
    path "M2 12h48M42 5l8 7-8 7",
    fill none, stroke currentColor, stroke-width 3, round caps and joins,
    colour var(--ks3-accent-text)

That geometry belongs to the engine, exactly as `_BEAM` does — it is Design's
drawing, not content. What is authored here is `reactants`, `arrow`, `products`
and `condition`. `arrow` holds the WORD the arrow means — **"gives"** — which
is its accessible name and nothing else. Three consequences, all deliberate:

  * there is no field an author could put a character into that would render
    between the two halves, so the class of defect flag 4 names cannot recur
    on this page;
  * the accessible name is composed from the same four strings a sighted
    student reads, so it cannot drift from them;
  * "gives" is the word the page itself uses everywhere the arrow is spoken —
    the key note ("Carbon dioxide + water gives glucose + oxygen") and all four
    rung-1 options. The drawn arrow and the spoken arrow are one authored word.

Elsewhere in the build (b3-06, b4-02, c1-06) the arrow IS typed inside JS
strings. That inconsistency is pre-existing, it is NOT resolved here, and
NOTES-B7 flag 4 asks for one ruling: drawn everywhere, or typed everywhere.

── ⚖️ NO COVER-TRIANGLE AND NO COVER-BAR, AND THAT IS THE RULING ────────

MRB-204 as amended gives the TRIANGLE to a product (`A = B × C`) and the
BALANCE BEAM plus part–whole BAR to a sum or a conservation statement. This is
neither. It is a chemical change: two substances are consumed and two
different substances are produced, and no quantity on the left is recoverable
by covering a quantity on the right. A triangle over
`carbon dioxide + water → glucose + oxygen` would teach that
`water = glucose × oxygen ÷ carbon dioxide`, which is not merely unhelpful but
false; a part–whole bar would teach that the products sum to the reactants as
named substances, which is the conservation-of-mass claim c2-06 owns and is not
what a word summary says. So the block carries `equation` and nothing else, and
the two cover components are absent by decision rather than by omission.

The rest of MRB-204's staging is also absent, and for the same reason: Design
draws no worked example and no fill-the-steps panel on this page, and MRB-205
closes inventing a component she did not draw. The step where the student
produces the summary themselves exists — it is rung 1, which is where the
ladder already puts it.

── The shell of `#s-summary` is MEASURED, and it is `rule`, not `formula` ─

Page line 161: `background: var(--ks3-band); border: 3px solid var(--ks3-ink);
border-radius: var(--ks3-r-block); padding: 34px 32px`, with a LEFT-aligned
display statement at `max-width: 26ch`. That is `.ks3-rule` — "a 3px ink border
and no shadow are what separate it from a `.ks3-block`" (`r_rule`'s own
docstring). `.ks3-formula` is centred with no max-width, which this section is
not. Contract §4 says measure the shell from Design's markup and follow the
measurement rather than the kind name, so the block is `rule`.

The `equation` payload is identical either way; if the commander prefers
`formula` for MRB-204 lineage it is a one-word change to `type` and nothing
else moves.

── What could not be lifted, and why ────────────────────────────────────

1. **The two inline `<a href>`s in the second confrontation.** Design links
   *Conservation of energy* (`p1-03`) and *the next unit* (`b8-01`) inside the
   prose. `rich()` allows `<em>` and `<strong>` and nothing else, so the WORDS
   are unchanged and the hyperlinks are dropped. Neither destination is lost:
   both become `references` edges, which is where the engine puts cross-lesson
   navigation. b3-07, b4-02, b4-03, b4-05 and b5-02 resolved the identical case
   the identical way.

2. **Design draws THREE endmatter link cards; the engine emits one list per
   card and the middle one carries four edges, not Design's two.** "Before this
   lesson" (`b1-03`, `p1-01`) is `requires`. "Connects to" (`b7-02`, `b4-05`)
   is `references`, plus the two stripped links from 1 above. Nothing Design
   named is lost and no heading changes.

3. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

4. **The instrument's section heading loses its `<h2>` level.** Design draws
   *"Four things it needs. Remove any one."* as an `<h2>` inside `#s-bench`
   beside a mono progress line. It is authored as the instrument's `heading`
   and the renderer decides the tag. No word changes.

5. **The foot line is a `convention_note`, not a `safety_note`.** Nothing in it
   is a safety instruction — it is a statement of how far the bench can be
   trusted plus a note on where van Helmont's figures come from. Routing it
   through `safety_note` would print it in the treatment reserved for "never
   light a candle without an adult", which devalues the safety line. b3-05,
   b3-07, b4-01 and b5-06 resolve the identical foot line the identical way.
   (B7's real safety line is b7-03's, and it is that lesson's to carry.)

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-summary` came off the rail. Design draws FOUR stops and `#s-summary` ticks
on `s.everTested` (page line 409) — the BENCH's predicate, character for
character, one section to the left (page line 408) — and because `#s-summary`
is an eyebrow, a display statement, an equation, four static cards and a key
fact, with no control, no commitment and no field, the argument was that
MRB-208 confined the rail to sections requiring the student to do something and
that `ks3_parity.check_rail_reachable` would fail the stop outright: the
assertion looks for one of five literal DOM signals in the anchored section —
`data-stage-done`, `class="ks3-rung`, `data-reveal`, `ks3-reveal-btn`,
`class="ks3-option` — and `#s-summary` emits none of them, so the stop could
never tick however `done_when` were spelled. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. That a gate could not express the stop
is a fact about the gate, and the gate has moved — `wireRail`'s `paint()`
resolves the tick at RAIL level, where Design computes it, instead of hunting
for a signal inside the section.

And Design's `isDone()` says what the condition is. It is a rail-level function
and it returns the identical expression for `#s-bench` and then for
`#s-summary`. The word summary is the payoff of the bench beside it: it emits
none of the five signals precisely because the bench already took the student's
commitment. That is a MIRROR, not an alias.

So the fourth stop is declared: anchor `s-summary`, `mirrors: "s-bench"`,
`done_when: "leaf_tested"` — the bench's own predicate, named as borrowed, and
gated by `ks3_parity.check_rail_matches_design` against
`docs/ks3/rail-manifest.md`. b5-06's `#s-designs`, b4-01's `#s-parts`, b4-03's
`#s-built`, c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-01's `#s-nutrients` and
b3-02's `#s-limits` are restored the same way. The section keeps its anchor, as
it always did, and NOTES-B7 §3's "four in all four lessons" is now followed
rather than reported.

⊕ MRB-177 LENGTH PARITY — RUNG 2 IS REPAIRED; RUNG 1 IS CLEAN.

  rung 1 (recall): correct 8w against distractors of 8 / 10 / 7. The correct
                   answer is not even the longest. Untouched.
  rung 2 (apply):  as delivered, correct 14w against 9 / 9 / 8 — `length_tell`
                   fires (14 is strictly longest and clears the field by 5).
                   After: 14w against 15 / 16 / 14. Passes.

  Mide ruled the CONSTRUCT rather than the instance. Design's correct option
  names a SOURCE and then what becomes of it — "Carbon dioxide from the air,
  built into glucose and then into the plant's structures" — while all three
  distractors named a source and appended a one-clause wrong REASON ("The soil,
  which is why plants need good soil"). The correct answer was therefore longer
  by construction, and a student could score the rung without reading it.

  The three distractors are rewritten in the correct answer's own shape —
  source, route, fate — with the misconception as the fate. Nothing is padded;
  each states a belief a student your age actually holds:

    A  soil up the roots and into the wood — PLANT-01, this unit's headline
       misconception and the one the hook and `#s-think` both attack.
    C  the water it was given, turned into tissue — van Helmont's OWN
       conclusion, and true of a living plant's wet mass, which is what makes
       it the hard one.
    D  sunlight converted into plant material — light becoming matter.

  **The correct option is unchanged, `answer: 1` is unchanged, and all three
  `feedback` corrections are unchanged and byte-identical**, because each still
  answers exactly the belief its rewritten distractor states. That is the test
  of whether a rewrite has changed what the question measures, and it passes.

⚑ FOR MIDE'S SCIENCE GATE — verified, corrected or flagged, in that order.

  VERIFIED, and left alone:
  * Van Helmont, 5 lb → 2.3 kg (2.268), 169 lb 3 oz → 77 kg (76.74), 2 oz →
    57 g (56.70). All three round correctly. The *gain* of "74 kilograms" is
    right and is better than the 75 a reader might expect: 76.74 − 2.27 =
    74.47, i.e. it is computed from the unrounded figures, not from 77 − 2.3.
  * "Nearly all the dry mass of that willow was carbon dioxide … The hydrogen
    came from the water." Exactly right, and the page is right about the part
    most texts get wrong: in cellulose the carbon AND the oxygen came from CO₂
    (~93% of dry mass between them) and only the hydrogen came from water. The
    O₂ released came from the water. Nothing to correct.
  * Carbon dioxide "about 0.04% of the air — four molecules in every ten
    thousand", and the big question's "four hundredths of one per cent". All
    three say 0.04%; the real figure is ~0.042%. Sound at KS3, and internally
    consistent.
  * "Almost all the oxygen in the atmosphere was made this way." Correct.
  * Rung 1 penalises sunlight on the LEFT. Preserved exactly — option C is
    "carbon dioxide + water + sunlight gives glucose + oxygen" and its
    correction is Design's own. This is the lesson's spine and nothing near it
    was touched.

  FLAGGED, not changed — each is a judgement that belongs to the examiner gate,
  not to an authoring pass:
  * **200 lb → "90 kg".** 200 lb is 90.72 kg, which rounds to 91. It is the one
    conversion on the page that rounds away from nearest rather than to it. It
    is within the same tolerance as 5 lb → "2.3 kg" and it keeps the hook's two
    soil figures identical ("planted it in 90 kg", "The soil was 90 kg"), so
    changing it would cost more than it buys — but it is the one number I would
    not have written that way. NOTES-B7 flag 1 asks for exactly this ruling.
  * **Rung 2 asks about a 3 kg SUNFLOWER, which is wet mass.** A living 3 kg
    plant is mostly water, so "where has almost all that mass come from?" is
    strictly answered by water, while the marked-correct option is carbon
    dioxide. Design handles it in distractor C's correction — "Water is most of
    the plant's wet mass … Dry the plant out, though" — which concedes the
    point and redirects to dry mass. Rewriting the STEM would change what a
    marked question measures, and that is Mide's gate. Reported, unchanged.
    (NOTES-B7 flag 2's hedge is the same argument in the hook, where the page
    says "dry mass" explicitly and is unimpeachable.)
  * **The bench mixes two classic apparatus.** The lede is a pot plant under a
    bell jar; the second readout is "Oxygen bubbles off the pondweed". Every
    individual claim is true and the legal line declares the bench a simplified
    model, but no single piece of glassware has both a soda-lime bell jar, a
    "not watered" dial and bubbling pondweed. Left byte-identical.
  * NOTES-B7 flag 7 lands here: PLANT-02 is confronted by pointing at P1's
    conservation of energy and forward at B8. Both pointers survive as
    `references` edges.
  * NOTES-B7 flag 12 — no diagram. See `figures` below.

⚑ APOSTROPHE DRIFT IN DESIGN'S OWN DELIVERY, reported not normalised.
  The page's HTML prose uses ASCII `'` ("the plant's food at all", "Van
  Helmont's pot", "the world's forests") while its `<script>` strings use
  `\\u2019` ("the plant’s mass", "the plant’s structures"). Byte-identity means
  each string below carries the mark its own source carries, so this module is
  mixed exactly as the page is. It is a Design delivery artefact and it is the
  commander's to normalise across the unit if it is worth normalising.
"""

# ── the four dials (page lines 333–351) ─────────────────────────────────
#
# `f` is a factor between 0 and 1 and **rate is the PRODUCT of the four**, so
# removing any one takes the rate to zero. That is the whole bench: the four
# are not weighted contributors, they are jointly necessary.
#
# The instrument OPENS with everything present — first option of every dial,
# which is what the page's `DEFAULTS` says and what `chosen()` falls back to.
# No `defaults` key is authored because there is nothing for it to say that the
# ordering does not already say. ⚖️ This is the OPPOSITE of b7-02's
# `leaf-tuner`, which opens on a deliberately bad leaf: here the student's move
# is to take something away, so the opening state has to be intact.
DIALS = [
    {"id": "light", "name": "Light",
     "options": [
         {"id": "bright", "label": "Bright", "f": 1},
         {"id": "dim", "label": "Dim", "f": 0.35},
         {"id": "dark", "label": "Dark cupboard", "f": 0},
     ]},
    {"id": "co2", "name": "Carbon dioxide",
     "options": [
         {"id": "normal", "label": "Normal air", "f": 1},
         {"id": "none", "label": "Soda lime absorbs it", "f": 0},
     ]},
    {"id": "water", "name": "Water",
     "options": [
         {"id": "watered", "label": "Watered", "f": 1},
         {"id": "dry", "label": "Not watered", "f": 0},
     ]},
    {"id": "leaf", "name": "The leaf tested",
     "options": [
         {"id": "green", "label": "Green part", "f": 1},
         {"id": "white", "label": "White part of a variegated leaf", "f": 0},
     ]},
]

# ── the three readouts (page lines 519–526) ─────────────────────────────
#
# ⚑ SCHEMA GAP, followed from the page. §2 gives a readout `{id, label,
# suffix}`, which cannot express any of the three things Design's counters
# actually do:
#   `scale` — the value at full rate. Oxygen is `Math.round(rate * 40)`, the
#             other two are the rate percentage itself. Without it the oxygen
#             counter reads 100 bubbles a minute.
#   `zero`  — the string at zero rate, and it is NOT uniform: "none" for the
#             two "units an hour" counters, "0 per minute" for the bubbles.
#   `tone`  — Design gives each bar its own colour and the distinction is
#             legible: --ks3-alert, --ks3-ok, --ks3-on-dark-muted. Oxygen is
#             the green one because it is the readout you can actually watch.
# The BAR width is the rate percentage on all three, independent of `scale`.
READOUTS = [
    {"id": "glucose", "label": "Glucose being made",
     "scale": 100, "suffix": "units an hour", "zero": "none",
     "tone": "alert"},
    {"id": "oxygen", "label": "Oxygen bubbles off the pondweed",
     "scale": 40, "suffix": "per minute", "zero": "0 per minute",
     "tone": "ok"},
    {"id": "co2", "label": "Carbon dioxide taken from the jar",
     "scale": 100, "suffix": "units an hour", "zero": "none",
     "tone": "muted"},
]

# Design's mono eyebrow over the iodine panel (page line 153) is FIXED across
# every branch. Schema §2 puts `tag` inside each verdict, so each verdict
# declares it — the shape the schema asked for, written once here so seven
# copies cannot drift into six and a typo.
TAG = "Iodine test on a leaf"

# The three headlines the iodine gives (page line 531). They are a function of
# RATE, not of which dial moved, which is why five of the seven verdicts share
# one.
NO_STARCH = "Orange-brown — no starch"
SOME_STARCH = "Faint blue-black — a little starch"
STARCH = "Blue-black — starch present"

# ── the iodine verdicts (page lines 468–475) ────────────────────────────
#
# ⚑ SCHEMA GAP, followed from the page. §2 declares six branches — one per
# dial, plus `multiple` and `none`. The page has SEVEN, because "nothing
# removed" splits in two: dim light is a REDUCTION, not a removal, and it has
# its own verdict ("the plant is limited, not stopped") which is the only place
# on the page a student meets a rate between zero and full. That branch is
# `low`, and dropping it would collapse the lesson's one non-binary reading
# into "starch present".
#
# ⚖️ Unlike b7-03's `method-breaker`, **precedence here is not load-bearing**:
# every single-dial branch is guarded by `missing.length === 1` on the page, so
# at most one can ever match and the order they are written in cannot change an
# outcome. Recorded because the sibling instrument's ordering IS load-bearing
# and the two must not be maintained as if they were the same problem.
VERDICTS = {
    "light": {
        "tag": TAG, "head": NO_STARCH,
        "why": "Chlorophyll, carbon dioxide and water all present, and "
               "nothing made. Light supplies the energy the reaction needs, "
               "and no amount of raw material substitutes for it."},
    "co2": {
        "tag": TAG, "head": NO_STARCH,
        "why": "The soda lime absorbed the carbon dioxide, so the carbon the "
               "glucose is built from never arrived. This is the one that "
               "convinces people the mass really does come from the air."},
    "water": {
        "tag": TAG, "head": NO_STARCH,
        "why": "No water means no hydrogen for the glucose — and in a real "
               "plant the stomata also close, which shuts the carbon dioxide "
               "out as well. Two reasons, one result."},
    # The variegated leaf, and the page says why it is the best of the four:
    # every other condition is held identical a centimetre away. Rung 3 is this
    # branch written out as an explanation.
    "leaf": {
        "tag": TAG, "head": NO_STARCH,
        "why": "No chlorophyll in the white tissue, so no light energy was "
               "absorbed there and no glucose was built. Every other "
               "condition was identical to the green part a centimetre away, "
               "which is what makes this the cleanest test of the four."},
    # ⚖️ PEDAGOGY, NOT A FALLBACK (schema §2). Delete this branch and a student
    # can remove three things at once and learn nothing. `{missing}` is the
    # engine's substitution point for the removed dials' names, joined with
    # " and " — page line 473, `missing.join(' and ')`.
    "multiple": {
        "tag": TAG, "head": NO_STARCH,
        "why": "More than one thing is missing: {missing}. The reaction needs "
               "all four, so removing any of them is enough on its own — for "
               "a fair test, take away one at a time."},
    # Nothing removed, but the light is dim: rate low rather than zero.
    "low": {
        "tag": TAG, "head": SOME_STARCH,
        "why": "Some starch, faintly. Everything the reaction needs is "
               "present and the light is dim, so the rate is low rather than "
               "zero — the plant is limited, not stopped."},
    # Nothing removed, full rate. Carries the answer to "why starch and not
    # glucose?", which b7-03 then owns in full.
    "none": {
        "tag": TAG, "head": STARCH,
        "why": "Starch is present, so glucose was made and stored. Starch is "
               "the storage form, which is why a leaf is tested for starch "
               "rather than for glucose: glucose is used or converted within "
               "hours, and starch stays put."},
}

# ── the four part cards (page lines 355–360) ────────────────────────────
#
# `role` is Design's mono accent tag and it is science, not decoration: it is
# the only place on the page that sorts the four substances into reactant and
# product AND says where each one comes from or goes. Rung 1 is that sorting.
PART_CARDS = [
    {"role": "Reactant · from the air", "name": "Carbon dioxide",
     "body": "Diffuses in through the stomata on the underside of the leaf. "
             "This is where nearly all of a plant’s mass comes from."},
    {"role": "Reactant · from the soil", "name": "Water",
     "body": "Taken up by root hair cells and carried to every leaf. It "
             "supplies the hydrogen in glucose."},
    {"role": "Product · kept", "name": "Glucose",
     "body": "A sugar, and an energy store. Used for respiration, converted "
             "to starch for storage, or built into cellulose for new cell "
             "walls."},
    {"role": "Product · released", "name": "Oxygen",
     "body": "A waste product of the reaction, diffusing out through the "
             "stomata. Almost all the oxygen in the atmosphere was made this "
             "way."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 139 character for character.
    "slug":        "the-photosynthesis-reaction",
    "title":       "The photosynthesis reaction",
    "discipline":  "biology",
    "unit":        "photosynthesis",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # Both statements are claimed WHOLE — neither needs a substatement split,
    # and nothing else in the key stage claims either (checked: `PHOT.01`
    # appears once more in the data, as a `touches` on b4-05; `NUT.06` appears
    # nowhere at all).
    #
    #   PHOT.01  the reactants in, and products of, photosynthesis, and a word
    #            summary for photosynthesis  →  #s-summary, and rung 1.
    #   NUT.06   plants making carbohydrates in their leaves by photosynthesis
    #            and gaining mineral nutrients and water from the soil via
    #            their roots  →  the van Helmont treatment. All three clauses
    #            are taught: carbohydrate made in the leaf (the glucose card,
    #            the starch verdicts), water from the soil via the roots (the
    #            water card, "taken up by root hair cells"), and minerals from
    #            the soil (the hook reveal's 57 grams, and #s-think's
    #            "milligram quantities to build particular molecules").
    "covers":      ["KS3.B.PHOT.01", "KS3.B.NUT.06"],
    # Named but not taught, each by exactly one sentence. The stomata are
    # b4-05's (NOTES-B7 flag 11 puts the ownership line there and this page
    # stays the right side of it); respiration is B8's and is pointed at, not
    # explained; the producer sentence in #s-think reaches PHOT.02, which b7-04
    # owns.
    "touches":     ["KS3.B.RESP.01", "KS3.B.PHOT.02"],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 2},
                    {"id": "energy", "level": 2},
                    {"id": "cells-and-systems", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. Both are cross-unit and
    # both exist.
    "requires":    ["animal-and-plant-cells", "energy-stores"],
    "assumes":     [],
    # Design's "Connects to" card is the first two; the last two are the
    # destinations of the stripped inline links in #s-think, which is where the
    # engine puts cross-lesson navigation ("What could not be lifted" 1).
    #
    # ⚠️ `aerobic-respiration` is B7's ONE forward reference and B8 is not
    # authored, so it renders through the graceful-pending path — an unlinked
    # `<span class="ks3-pending">Aerobic respiration <em>(Respiration — coming
    # soon)</em></span>` — rather than a dead link. Same mechanism and same
    # reason as c1-06's `why-ice-floats` edge into P11. It becomes a live link
    # the moment B8 lands, with nothing to change here.
    "references":  ["leaves-built-for-the-job",
                    {"unit": "B4",
                     "lesson": "stomata-and-gas-exchange-in-plants"},
                    {"unit": "P1", "lesson": "conservation-of-energy"},
                    {"unit": "B8", "lesson": "aerobic-respiration"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "The balanced symbol equation, limiting factors and rate "
                   "graphs, and the light-dependent and light-independent "
                   "stages.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A tree is mostly made of air. That sentence sounds like a "
                    "trick, and it is the literal truth: the wood, the bark "
                    "and the leaves were assembled from a gas that makes up "
                    "four hundredths of one per cent of the atmosphere.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them and as NOTES-B7 §3 requires.
    # `s-summary` is the third: no control of its own, so it mirrors `s-bench`
    # and ticks on the bench's predicate — see the docstring. `short` and
    # `label` are Design's own `RAIL_SHORT` and `RAIL` strings (page lines
    # 323–329).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "The willow",
         "done_when": "committed"},
        # Design's own threshold, kept: the stop ticks when the student has run
        # the iodine test at least once (`s.everTested`, page line 408), not
        # when a dial has been touched. Turning a dial is not an investigation
        # until you look at what it did.
        {"anchor": "s-bench", "short": "BENCH", "label": "Take one away",
         "done_when": "leaf_tested"},
        {"anchor": "s-summary", "short": "SUMMARY", "label": "Word summary",
         "mirrors": "s-bench", "done_when": "leaf_tested"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key.
    #
    # ⚖️ The reveal calls van Helmont "half right" and says so twice over: he
    # PROVED it was not the soil, and then concluded wrongly that it was all
    # water. That is the shape of the lesson — a decisive experiment whose
    # conclusion was still wrong — and it is why the same figures come back in
    # #s-think as the thing that settles PLANT-01.
    "phenomenon": {
        "kind": "narrative",
        "title": "The tree gained 74 kilograms. The soil lost 57 grams.",
        "prompt": "In the 1640s Jan van Helmont weighed a willow shoot — "
                  "2.3 kg — and planted it in 90 kg of dried soil in a pot he "
                  "covered to keep dust out. He gave it nothing but water for "
                  "five years, then weighed both again. The willow was 77 kg. "
                  "The soil was 90 kg, short by about 57 grams.",
        "commit": "Where did the other 74 kilograms come from?",
        "options": [
            "The soil in the pot",
            "The water it was given",
            "The air around it",
            "The sunlight falling on it",
        ],
        "reveal": "Mostly from the air. Van Helmont proved it was not the "
                  "soil, which was the point of weighing it, and then "
                  "concluded it must all have been the water — half right, "
                  "and the best available answer for another century. Nearly "
                  "all the dry mass of that willow was carbon dioxide taken "
                  "from the air through the leaves. The hydrogen came from "
                  "the water; the 57 grams of soil were minerals, needed in "
                  "tiny amounts and not the plant's food at all.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Both statements are lifted byte-identical from
    # `docs/ks3/misconception-register.md` lines 596–597, and both `elicited_by`
    # / `confronted_by` values are the register's own. Each names a SECTION
    # ANCHOR this page emits — `s-hook` at core[0] and `s-think` at core[3] —
    # which is what the MRB-244 gate resolves against on the BUILT page.
    #
    # `PLANT-09` is this lesson's pre-allocated spare and is deliberately left
    # unclaimed, permanently, like `DRUG-07` and `REPRO-17`/`20`/`21`/`23`.
    # It is never to be re-pointed at a different belief.
    "misconceptions": [
        # Elicited by the hook honestly: option A *is* this belief, and a
        # student who holds it will pick it before reading anything else.
        {"id": "PLANT-01",
         "statement": "Plants get their food from the soil.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        # Not asked for anywhere before the block that kills it, so the block
        # is named for both ends — the register's own reading, and b4-01's and
        # b5-06's pattern.
        {"id": "PLANT-02",
         "statement": "Photosynthesis makes energy.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B7, so these never reach the
    # lesson body: the TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list.
    #
    # ⚠️ Every definition is authored, not lifted, and each is written as what
    # the thing IS or what happens to it — never what it is "for". `chlorophyll`
    # is the one that has to be careful: it absorbs light, and the absorbing is
    # not a purpose.
    "vocabulary": [
        {"term": "photosynthesis",
         "definition": "The reaction in which a plant builds glucose from "
                       "carbon dioxide and water, using light energy, and "
                       "releases oxygen.",
         "note": None},
        {"term": "reactant",
         "definition": "A substance used up in a reaction. It appears on the "
                       "left of the summary.",
         "note": "Light is not one. No part of it ends up in the glucose."},
        {"term": "product",
         "definition": "A substance made in a reaction. It appears on the "
                       "right of the summary.",
         "note": None},
        {"term": "chlorophyll",
         "definition": "The green pigment in a leaf. It absorbs the light "
                       "energy photosynthesis requires.",
         "note": "The white parts of a variegated leaf have none, and make no "
                 "starch."},
        {"term": "glucose",
         "definition": "The sugar built in photosynthesis. It is an energy "
                       "store.",
         "note": None},
        {"term": "starch",
         "definition": "The insoluble store glucose is converted into in a "
                       "leaf.",
         "note": "A leaf is tested for starch rather than glucose because "
                 "starch stays put."},
        {"term": "producer",
         "definition": "An organism that makes its own food rather than "
                       "taking it from something else.",
         "note": None},
        {"term": "mineral",
         "definition": "A dissolved substance taken from the soil through the "
                       "roots, in milligram quantities.",
         "note": "Minerals are not food and are not a raw material for this "
                 "reaction."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND DELIBERATELY SO — schema §7, measured rather than assumed.
    # This page draws no <img>, no <figure> and no placeholder, and its legal
    # line names no diagram slot, so there is nothing to declare at `needed`.
    # NOTES-B7 flag 12 names a leaf cross-section as the obvious candidate for
    # the unit and records that Design taught the internal structure in b7-02's
    # five cards instead. That flag is Mide's to rule on and is NOT dropped by
    # this pass; inventing a slot here to fill the gap would be a component
    # nobody drew (MRB-205).
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b7/__init__.py::_normalise, which leaves the `practical`
        # shell behind it.
        #
        # ⚠️ SHELL MEASURED, NOT GUESSED: page line 105 is
        # `ks3-block ks3-dark ks3-practical`, so `segment` is `practical` —
        # ink-dark ground. Contract §4 records that B1 got two of six wrong by
        # inferring the shell from the kind name.
        #
        # ⚠️ THIS INSTRUMENT IS ON INK. `.ks3-dark p` is (0,1,1) and beats a
        # bare instrument class at (0,1,0) — the defect that shipped a B4 chain
        # label at 1.21:1 past a green kinds gate. That is the renderer's
        # problem rather than this module's, and it is recorded here because
        # this payload is what feeds it.
        #
        # ⛔ NO RUNTIME STATE IS AUTHORED (schema §0 rule 3). NOTES-B7 §1.1
        # lists `picks: {}` and `tested: bool` in its payload sketch; those are
        # values the runtime owns, not content, and under contract R5 a key
        # with no read site fails `ks3_key_audit.py`. The renderer initialises
        # its own state.
        {"type": "reactant-remover", "id": "take-one-away",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · take one thing away",
         "heading": "Four things it needs. Remove any one.",
         "prompt": "A pot plant under a bell jar, kept for a day, then one "
                   "leaf tested for starch. Change the conditions and watch "
                   "three readouts: the rate of the reaction, the oxygen "
                   "coming off, and what the iodine test says.",
         # Design's mono line beside the heading (page line 509): the two
         # states of the section, not a counter.
         "progress": {"before": "not tested yet", "after": "leaf tested"},

         "dials": DIALS,

         # The panel's own two lines (page lines 517–518). `missing_prefix` is
         # followed by the removed dials' names joined with ", ".
         "setup": {"all_present": "Everything present",
                   "missing_prefix": "Missing: "},
         "rate": {"label": "Rate", "suffix": "% of maximum"},

         "readouts": READOUTS,

         # Schema §1: `reset_label`, never `clear_label` or `again_label`.
         # `test_label` is §2's name for the commit button; `tested_label` is
         # its spent state (page line 527). **No `run_label`** — schema §2
         # offers one and this bench has no second button for it to name, so
         # authoring it would be a dead key under R5.
         "test_label": "Test a leaf with iodine",
         "tested_label": "Tested",
         "reset_label": "Reset the bell jar",

         "verdicts": VERDICTS},

        # #s-summary — the word summary. Shell measured as `rule`, not
        # `formula`; the arrow is DRAWN and there is no cover component. Rail
        # stop 3, mirroring `s-bench`. All three decisions are argued in full
        # in the docstring.
        {"type": "rule", "anchor": "s-summary",
         "eyebrow": "The word summary",
         "statement": "Two reactants in, two products out.",

         # ⚠️ THE ARROW IS NOT A CHARACTER. `arrow` is the WORD the drawn arrow
         # means, and it is the component's accessible name — the same word the
         # key note and all four rung-1 options use when they speak the
         # summary aloud. The SVG geometry is Design's and lives in the engine
         # (measured values in the docstring). There is deliberately no field
         # here that a U+2192 could be typed into.
         #
         # `condition` is the mono line Design sets full-width beneath the row
         # (page line 169). It is the reaction condition, and the key fact
         # directly under it is the reason it is a separate field rather than
         # part of either side: light and chlorophyll are needed and are not
         # raw materials.
         "equation": {
             "reactants": "carbon dioxide + water",
             "arrow":     "gives",
             "products":  "glucose + oxygen",
             "condition": "requires light energy, absorbed by chlorophyll",
         },

         "cards": PART_CARDS,

         # Design nests the key fact inside this section (page lines 182–185).
         # `card`, because the section itself is `band` and band on band is
         # invisible — the same arrangement and the same reason as b5-06's
         # nested fact inside its comparison.
         "key_fact": {"ref": "light-is-not-a-raw-material", "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "PLANT-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-summary, on the card ground — Design's own arrangement.
    #
    # ⚠️ "above and below the arrow, not in it" is Design's phrasing and it is
    # lifted whole. Design's DRAWING puts the condition line beneath the row
    # rather than literally above and below the arrow head; the sentence is
    # idiomatic about how reaction conditions are written and the teaching in
    # it — that light and chlorophyll are conditions and not reactants — is
    # exactly right and is what rung 1 marks. Reported, not softened.
    "key_facts": [
        {"id": "light-is-not-a-raw-material",
         "text": "Photosynthesis builds glucose from carbon dioxide and "
                 "water, using light energy absorbed by chlorophyll, and "
                 "releases oxygen. Light and chlorophyll are needed for the "
                 "reaction but are not raw materials — they appear above and "
                 "below the arrow, not in it.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second after the
        # first behind an amber-topped divider — `r_confrontation` renders
        # exactly that from `statements[]`. The block asks for no commitment,
        # on Design's page and here, so it is not a rail stop and emits no
        # completion contract. (Contract R1 makes `#s-think` a `predict` in B2,
        # C1 and C2 because on THOSE pages it gates a reveal behind a
        # commitment. This page's is static markup, like B1's, B4's and B5's,
        # so it stays a confrontation. Same rule, different block.)
        #
        # ⚠️ Design's second body carries two inline `<a href>`s, to
        # `p1-03-conservation-of-energy.html` and
        # `b8-01-aerobic-respiration.html`. `rich()` allows `<em>` and
        # `<strong>` and nothing else, so the WORDS are unchanged and the
        # hyperlinks are dropped; both destinations survive as `references`
        # edges. The two `<em>` runs in the FIRST body — <em>plant food</em>
        # and <em>producer</em> — are inside `rich()`'s allowance and render.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "PLANT-01",
         "statements": [
             {"quote": "Plants get their food from the soil.",
              "body": ["A plant takes water and dissolved minerals from the "
                       "soil, and neither of those is food. Food means "
                       "something that can be broken down to release energy, "
                       "and minerals cannot — they are needed in milligram "
                       "quantities to build particular molecules, in the same "
                       "way that the iron in your diet is essential and is "
                       "not a meal. Van Helmont's pot settled this in the "
                       "1640s: 74 kilograms of new willow appeared and the "
                       "soil weighed almost exactly what it had at the start. "
                       "The word <em>plant food</em> on a bottle in a garden "
                       "centre is a marketing name for a mineral mix, and it "
                       "is the reason this misconception survives. A plant is "
                       "the one kind of organism on Earth that does not need "
                       "to find food, because it makes its own; that is what "
                       "<em>producer</em> means, and it is the whole reason "
                       "the rest of us can exist."]},
             {"quote": "Photosynthesis makes energy.",
              "body": ["Nothing makes energy. You met the rule in "
                       "Conservation of energy: energy is transferred between "
                       "stores and never created, and a plant is not an "
                       "exception to the laws of physics. What photosynthesis "
                       "does is take energy that is already arriving as light "
                       "and store it chemically, by building glucose "
                       "molecules that hold more energy than the carbon "
                       "dioxide and water they were made from. The sunlight "
                       "is not a reactant — no atom of it ends up in the "
                       "glucose — which is exactly why it sits above the "
                       "arrow in the summary rather than on the left of it. "
                       "Getting this straight now matters, because "
                       "respiration in the next unit is the reaction that "
                       "takes that energy back out of the store, and neither "
                       "reaction can be understood if energy is being "
                       "invented in one of them."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026. Rung 1 is clean and
    # untouched (8w correct against 8 / 10 / 7 — the correct answer is not even
    # the longest). Rung 2's three distractors are rewritten so that each
    # states a WRONG RULE in the correct answer's own shape — source, route,
    # fate — rather than a source plus a one-clause wrong reason. Correct
    # option, `answer: 1` and all three `feedback` corrections are unchanged
    # and byte-identical. 14w against 15 / 16 / 14 after. Full argument in the
    # docstring.
    "ladder": {
        # ⚖️ THE RUNG THE UNIT TURNS ON. Option 2 puts sunlight on the LEFT of
        # the summary and is marked WRONG, and its correction is the same
        # sentence the key fact and #s-think both make. Nothing in this rung
        # was touched.
        "recall": {
            "title": "Rung 1 · The summary",
            "q": "Which line is the word summary for photosynthesis?",
            "options": [
                "carbon dioxide + water gives glucose + oxygen",
                "glucose + oxygen gives carbon dioxide + water",
                "carbon dioxide + water + sunlight gives glucose + oxygen",
                "minerals + water gives glucose + oxygen",
            ],
            "answer": 0,
            "feedback": {
                1: "That is respiration — the same four substances, the other "
                   "way round. Getting the direction wrong is the most common "
                   "error in this topic.",
                2: "Very nearly. Light is needed but is not a reactant — no "
                   "part of it ends up in the glucose — so it belongs above "
                   "the arrow, not on the left of it.",
                3: "Minerals are taken from the soil in tiny amounts to build "
                   "particular molecules. They are not a raw material for "
                   "this reaction, and there are nowhere near enough of them "
                   "to be.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A sunflower seed weighing 0.1 g grows into a plant weighing "
                 "3 kg. Where has almost all that mass come from?",
            # ⊕ MRB-177, 17 Aug 2026. Options 0, 2 and 3 rewritten as wrong
            # RULES in the correct answer's shape. Option 1 and `answer` are
            # Design's, unchanged.
            "options": [
                "The soil, drawn up through the roots and built into the wood "
                "and the leaves",
                "Carbon dioxide from the air, built into glucose and then "
                "into the plant’s structures",
                "The water it was given, taken up by the roots and turned "
                "into new plant tissue",
                "The sunlight falling on the leaves, converted into plant "
                "material as it is absorbed",
            ],
            "answer": 1,
            # All three unchanged from Design, and each still answers exactly
            # the belief its rewritten distractor states — which is the test of
            # whether the rewrite changed what the question measures.
            "feedback": {
                0: "Weigh the soil before and after, as van Helmont did. It "
                   "barely changes — nowhere near three kilograms leaves the "
                   "pot.",
                2: "Water is most of the plant’s wet mass and it does supply "
                   "the hydrogen. Dry the plant out, though, and what is left "
                   "— the wood, the fibres, the starch — is built mostly from "
                   "carbon that arrived as a gas.",
                3: "Light carries energy, not matter. Nothing about a beam of "
                   "light has any mass to donate to a stem.",
            }},
        # The variegated-leaf branch of the bench, written out as an
        # explanation — criterion 5 is the fair-test argument the instrument's
        # `leaf` verdict makes in one sentence.
        "explain": {
            "title": "Rung 3 · Explain the variegated leaf",
            "q": "A variegated leaf, green in the middle and white at the "
                 "edges, is destarched in the dark for two days, left in "
                 "bright light for a day, then tested with iodine. The middle "
                 "goes blue-black; the edges stay orange-brown. Explain the "
                 "result, and say why this plant is a better test than using "
                 "two separate plants.",
            "field_label": "Your explanation",
            "placeholder": "The green part contains…",
            "success": [
                "Says the green parts contain chlorophyll and the white parts "
                "do not.",
                "Says chlorophyll absorbs the light energy that "
                "photosynthesis requires.",
                "Says the green parts therefore made glucose, which was "
                "stored as starch, so iodine turned blue-black there.",
                "Says the white parts made no glucose and so had no starch, "
                "leaving the iodine orange-brown.",
                "Says both parts had identical light, carbon dioxide, water "
                "and temperature because they are on one leaf, so chlorophyll "
                "is the only variable — which two plants could not guarantee.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A grower has a greenhouse of tomatoes in good soil, watered "
                 "automatically, in a bright and warm greenhouse in June. "
                 "Yields have stopped rising. She is offered four upgrades: "
                 "more mineral feed, extra lighting, a carbon dioxide supply, "
                 "or a bigger pot for each plant. Say which you would advise "
                 "and why, and how you would test your advice before buying "
                 "for the whole greenhouse.",
            "field_label": "Your answer",
            "placeholder": "The condition most likely to be limiting is…",
            "success": [
                "Identifies carbon dioxide as the most likely factor holding "
                "the rate back, because air is only about 0.04% carbon "
                "dioxide while light, water and warmth are already plentiful "
                "in June.",
                "Rules out extra lighting on the grounds that light is "
                "already plentiful at that time of year.",
                "Rules out more minerals and bigger pots by explaining that "
                "minerals are needed in tiny amounts and are not the raw "
                "material for photosynthesis.",
                "Proposes testing on part of the greenhouse only, with the "
                "rest left unchanged as a comparison.",
                "Says the two sections must otherwise be treated identically, "
                "and that yield should be measured the same way in both.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # ⚠️ Speaks the arrow as the word "gives", which is the same word the drawn
    # component carries as its accessible name. One authored word, two places.
    "key_note": "Carbon dioxide + water gives glucose + oxygen, using light "
                "energy absorbed by chlorophyll. The carbon dioxide comes "
                "from the air through the leaves, the water from the soil "
                "through the roots, and almost all of a plant's mass comes "
                "from the carbon dioxide rather than from the soil. Remove "
                "light, carbon dioxide, water or chlorophyll and the reaction "
                "stops.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES-B7 flag 5. The 0.04% figure and both consequences are Design's and
    # are on Mide's list; the paragraph's real subject is that a trace gas can
    # be the thing holding a whole system back, which is what rung 4 asks the
    # student to reason with.
    "stretch": [
        {"type": "explainer", "id": "four-molecules-in-ten-thousand",
         "text": "Carbon dioxide is about 0.04% of the air — four molecules "
                 "in every ten thousand. Every oak beam in a cathedral roof "
                 "was assembled out of that trace, one molecule at a time, by "
                 "leaves working at a rate slow enough that the tree took two "
                 "centuries to do it. Two consequences follow. The first is "
                 "agricultural: because the supply is so thin, carbon dioxide "
                 "is often the factor holding a greenhouse crop back, and "
                 "growers pipe it in deliberately to raise the concentration. "
                 "The second is planetary: a growing forest is taking carbon "
                 "out of the atmosphere and locking it into wood, which is "
                 "why what happens to the world's forests appears in every "
                 "calculation about the climate. Burning that wood, or "
                 "letting it rot, returns exactly the carbon the tree "
                 "removed."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own flagship, which is a real
    # destination on the page it is printed on (§4.8.1 C) — and the right one:
    # the bench is where "light is needed but is not a reactant" is something
    # you can do rather than read.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work through why light is not a reactant?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note` — see "What could not be lifted" 5.
    # Design draws ONE plain `.ks3-legal` paragraph here and nothing in it is a
    # safety instruction: it declares the bench a simplified model, names the
    # two ways a real plant does not behave like it, and says where van
    # Helmont's numbers come from.
    "convention_note": "The bench is a simplified model. Rate is shown as a "
                       "percentage of this plant's maximum with one condition "
                       "changed at a time; real rates depend on temperature "
                       "and on several conditions at once, and a plant "
                       "deprived of water wilts and closes its stomata rather "
                       "than switching off cleanly. Van Helmont's figures are "
                       "as he reported them, converted from pounds and "
                       "ounces.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is one-variable-at-a-time and says so to the student in the
    # `multiple` verdict; rung 3 asks why one leaf beats two plants; rung 4
    # asks for a comparison section and an identically measured yield. The hook
    # is a decisive experiment whose conclusion was still wrong, which is the
    # attitudes strand rather than the skills one.
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation",
           "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
