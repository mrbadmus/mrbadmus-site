"""B4 L5 — Stomata and gas exchange in plants (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b4/b4-05-stomata-and-gas-exchange-in-plants.dc.html` (565 lines),
its author's notes `docs/ks3/design-reference/b4/NOTES-B4.md`, and the B4 payload schema
`docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md` §5, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except where this docstring says otherwise, and every exception is here.

── The contrast is NOT plant versus animal ──────────────────────────────

NOTES-B4 §2 is explicit and the whole lesson depends on it: the contrast is
*respiration versus photosynthesis inside the same organism*, and the payoff is
that at one light level the difference is zero. "Plants do the opposite of
animals" is the misconception the lesson exists to kill, not its structure.

── ⚑ THE DAWN PRESET DID NOT LAND IN THE BALANCED WINDOW ────────────────

Design's curve is `photosynthesis = 9 × (1 − e^(−light / 32))`, respiration is
flat at 2.0, and the compensation point is `|net| < 0.25`. Solving that:

    light          photosynthesis      net        branch
    0  Midnight        0.00          −2.00        release
    7                  1.77          −0.23        BALANCED
    8                  1.99          −0.01        BALANCED   ← exact at 8.04
    9                  2.21          +0.21        BALANCED
    21 Dawn            4.33          +2.33        uptake
    48 Overcast        6.99          +4.99        uptake
    100 Bright noon    8.61          +6.61        uptake

So on Design's page, pressing *Dawn* reads **Net uptake of carbon dioxide** —
and the balanced branch's own first sentence is *"This is the dawn reading from
the hook."* The page contradicts itself, and the hook it points back at is the
lesson's whole payoff. NOTES-B4 §3.4 states the preset is tuned to sit inside
the window; against Design's own constants it is not. The B4 payload schema §5
measured the same arithmetic independently and requires the author to make the
page agree with itself, by one of two routes.

**Taken here: `presets[dawn].value = 21 → 8`, with `balanced_preset = "dawn"`
so the build holds it there.** Reasons, in order:

1. It preserves **every authored string byte-identical**, including the
   balanced verdict's claim to be the dawn reading. The other route rewrites an
   approved, science-bearing paragraph and severs the hook↔bench link that is
   the lesson's payoff.
2. `21` is not a science-bearing figure. The page's own foot line says the
   rates are *relative units chosen to make the two processes comparable, not
   measured values*, and dawn at 8/100 of full light is if anything the more
   plausible reading of the two.
3. It is the slip R4 describes — a stated intention (NOTES §3.4) contradicted
   by the page's own arithmetic — not an intention.

⚑ This is a DEVIATION from Design's drawn value and it is Mide's to rule on.
If he prefers Design's `21`, the fix is this one integer plus deleting
`balanced_preset`, and then `verdicts.balanced.why` must lose its opening
sentence or the page goes back to contradicting itself. Do not widen
`balanced_window`: at ±2.4 every reading from midnight to overcast would report
itself as balanced.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-stomata` came off the rail. Design draws FOUR stops and `#s-stomata` ticks
on `s.moved` (page line 395) — the LEDGER's predicate, verbatim, one section to
the left — and because the section is an eyebrow, a display line, four cards, a
closing card and a key fact with no control, no commit and no field, the
reading was that MRB-208 forbade the stop and that
`ks3_parity.check_rail_reachable` would fail it for carrying none of the
signals `doneByDom()` reads. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. A gate that would have failed the stop
is a gate to fix, not a reason to drop what Design drew — which is what
`check_rail_matches_design` and rail-level mirrors now do.

And `s.moved` written twice is Design stating the tick condition. `isDone()` is
a rail-level function and returns the identical expression for `#s-ledger` and
then for `#s-stomata`. The stomata are the payoff of having moved the light:
the section holds no control because the ledger already took the student's
commitment. That is a MIRROR, resolved at rail level in `wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-stomata`, `mirrors: "s-ledger"`,
`done_when: "light_moved"` — the ledger's own predicate, named as borrowed, and
gated against `docs/ks3/rail-manifest.md`. c1-02's `#s-matrix`, b3-02's
`#s-limits`, b3-04's `#s-three` and b3-07's `#s-four` are restored the same
way. `#s-stomata` keeps its anchor, as it always did.

── What could not be lifted byte-identical, and why ─────────────────────

1. **The four `#s-stomata` card TAGS.** Design's card is three parts — a mono
   accent tag, a display name, a body — and the shipped `rule` card is `term`
   and `gloss`. Tag and name are joined with Design's own middle-dot idiom (the
   joiner it uses in "Breathing and gas exchange · Contrast" and "At the bench ·
   turn the light up"), so both strings survive and neither is invented. Same
   resolution as b3-04's three imbalance columns and b3-07's four feature cards.
   Reported; the fix, if the card is to win, is a `tag` key on a rule card.

2. **The fifth card becomes `rule.close`.** Design draws "Same four
   requirements, third organ" as a full-width card BELOW the grid, not as a
   fifth cell in it — the four above it are one taxonomy and it is a closing
   statement about three organs. `r_rule`'s `close` is a full-measure paragraph
   below the cards, which is that shape; the tag keeps Design's own `<strong>`
   treatment and joins the paragraph, exactly as b3-07's "Remove it and:" line
   does. Every byte present, in Design's order.

3. **The key fact leaves Design's band panel.** She nests it inside
   `#s-stomata`; `r_rule` has no nested key-fact slot (only `r_comparison`
   does), so it renders as its own top-level block directly under the panel, on
   the band ground every other top-level key fact in the key stage takes. The
   words and the order are unchanged. Design's nested box sits on `--ks3-card`
   because it is inside a band panel; at top level `band` is the 5:1 default.

4. **The inline link in the third confrontation.** Design writes "the muscular
   work you met in <a href="b4-02-how-breathing-works.html">How breathing
   works</a>". `rich()` allows `<em>` and `<strong>` and nothing else, so the
   WORDS are unchanged and the hyperlink is dropped. The destination is not
   lost: `how-breathing-works` is added to `references`, which is where the
   engine puts cross-lesson navigation. Same handling as b3-07's two links.

5. **The `<em>` in the foot line.** Design sets *Photosynthesis* in italic in
   "B7 <em>Photosynthesis</em> owns the reaction itself"; `t()` escapes markup
   in a foot line, so it renders as plain text. The sentence is otherwise
   unchanged. Same as b3-07's mono figure id.

6. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

── The endmatter's middle card carries FOUR edges, not Design's two ─────

Design draws `alveoli-built-for-exchange` and `animal-and-plant-cells`. Two are
added, both because a destination Design DID name would otherwise be lost:

* `how-breathing-works` — the stripped inline link, see 4 above.
* `the-photosynthesis-reaction` (B7) — the foot line names B7 as the owner of
  the reaction, and §4.6's single-source rule says this lesson points at it and
  never repeats it. B7 is not authored, and the generator renders an unauthored
  target as `<span class="ks3-pending">The photosynthesis reaction <em>(Photo-
  synthesis — coming soon)</em></span>` rather than a dead link (build_ks3.py,
  "Cross-discipline references (§4.6) — must render gracefully BEFORE the
  referenced unit exists"). Nothing else in the build reads `references`: the
  forward-reference gate in `verify_ks3.py` reads `requires` and `reference_to`,
  so a reference to a later unit cannot fail it — and B7 is Year 8 like B4 in
  any case. Neither edge carries a `why`; Design's endmatter cards carry none.

── Ladder length parity (MRB-177) — MEASURED, both marked rungs PASS ────

    rung 1   correct 6 words, distractors 3 / 11 / 5. The correct option is not
             the longest, so there is no length tell.
    rung 2   correct 8 words, distractors 5 / 8 / 9. Likewise.

No distractor was touched. A correct option that is not a length tell must not
be "fixed".

⚑ For Mide's science gate — NOTES-B4's own flags, carried here so they are
  visible beside the content:
  * flag 15  **the compensation point is taught BY NAME**, which is normally a
             GCSE or A-level term. Design introduces it as a label for
             something the student has just produced on the bench, not as
             vocabulary to learn — so it is the balanced verdict's `tag` and it
             is deliberately NOT in `vocabulary`, which becomes the browse
             page's "Words this unit gives you" chips. Built as drawn. Confirm,
             or tell us to keep the phenomenon and drop the name.
  * flag 16  the rates are relative units, not measured, and the balancing
             light level varies hugely by species. Both are in the foot line,
             lifted, and they are load-bearing honesty about the model.
  * flag 17  guard cells open the pore by becoming turgid, with no potassium
             ions and no ABA. Confirm the depth.
  * flag 18  CAM in GOING FURTHER, including that a pineapple leaf tastes sour
             in the morning and not in the evening. Design has not verified the
             tasting claim and neither have we.
  * flag 19  the B7 boundary — this lesson claims what B7 will own, and B7 is
             not authored. Carried as a `references` edge, above.
  * flag 20  **no figure slot is named on this page.** The foot line names none,
             and NOTES' suggestion that a labelled stoma / guard-cell pair
             "would be the obvious second slot" is a suggestion, not a
             reference: declaring it would invent a sourcing task for artwork
             the page never asks for. `figures` is empty and that is measured,
             not an omission.
  * ⚖️ MRB-225 holds. The stretch layer adds a strategy, retracts nothing above
    it, and the body's claim that stomata are a trade-off is what makes CAM
    legible.
"""

# ── the four stomata cards (page lines 338–347) ─────────────────────────
#
# ⚠️ TAG · NAME, joined. See "What could not be lifted" 1. The joiner is
# Design's own middle dot and both authored strings are present unchanged.
STOMATA_CARDS = [
    {"term": "The pore · A stoma is a gap between two cells",
     "gloss": "Not a hole in a wall — a gap held open between a pair of curved "
              "guard cells. Most are on the underside of the leaf, where they "
              "are shaded and sheltered, and a square millimetre of leaf may "
              "carry several hundred."},
    {"term": "The control · Guard cells open it by swelling",
     "gloss": "When water moves into the guard cells they become turgid and "
              "bow apart, opening the pore. When water leaves they go limp and "
              "the pore closes. The plant controls its gas exchange by moving "
              "water, not by moving muscle."},
    {"term": "The trade-off · Every open stoma loses water",
     "gloss": "The inside of a leaf is wet, because diffusion needs a moist "
              "surface. So a pore open enough for carbon dioxide to diffuse in "
              "is open enough for water vapour to diffuse out — the two cannot "
              "be separated."},
    {"term": "The consequence · Wilting is a decision, not a failure",
     "gloss": "A plant short of water closes its stomata, which stops water "
              "loss and simultaneously stops photosynthesis. It is choosing "
              "survival over growth, and it is why a hot dry afternoon slows a "
              "crop even in full sunshine."},
]

# ── the light presets (page lines 331–336) ──────────────────────────────
#
# ⚑ `dawn` is 8, and Design drew 21. This is the retune argued in the
# docstring — the ONLY value on this page that is not Design's own, and the
# reason it moved is that Design's own copy says it should be inside the
# balanced window and her arithmetic puts it two units of net flow outside it.
# `balanced_preset` below makes the renderer raise if it ever drifts back out.
PRESETS = [
    {"id": "dark",   "label": "Midnight",    "value": 0},
    {"id": "dawn",   "label": "Dawn",        "value": 8},
    {"id": "cloudy", "label": "Overcast",    "value": 48},
    {"id": "bright", "label": "Bright noon", "value": 100},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 118 character for character.
    "slug":        "stomata-and-gas-exchange-in-plants",
    "title":       "Stomata and gas exchange in plants",
    "discipline":  "biology",
    "unit":        "breathing-and-gas-exchange",
    "family":      "CONTRAST",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.GAS.04` — "the role of leaf stomata in gas exchange in plants" —
    # owned WHOLE. One bullet, one lesson, nothing to split. The lesson touches
    # photosynthesis and respiration and owns neither: B7 owns the reaction
    # (foot line, and the `references` edge) and B8 owns respiration.
    "covers":      ["KS3.B.GAS.04"],
    "touches":     ["KS3.B.PHOT.01", "KS3.B.RESP.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "structure-function", "level": 2},
                    {"id": "energy", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's endmatter: "Before this lesson → Exercise, asthma and smoking";
    # "Connects to → Alveoli: built for exchange, Animal and plant cells". The
    # two additions are argued in the docstring.
    "requires":    ["exercise-asthma-and-smoking"],
    "assumes":     [],
    "references":  ["alveoli-built-for-exchange",
                    {"unit": "B1", "lesson": "animal-and-plant-cells"},
                    "how-breathing-works",
                    {"unit": "B7", "lesson": "the-photosynthesis-reaction"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Leaf structure and adaptation, transpiration, limiting "
                   "factors in photosynthesis, and the compensation point.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A plant respires every second of its life, exactly like "
                    "you. In daylight it also does something else, and the two "
                    "run at once.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-stomata` is the third: no control
    # of its own, so it mirrors `s-ledger` and ticks on the ledger's predicate
    # — see the docstring. `short` and `label` are Design's own strings (page
    # lines 321–327).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Flat line at dawn",
         "done_when": "committed"},
        # Design's own threshold, kept: the stage ticks when the student has
        # MOVED the light, not when the section is reached. A ledger nobody has
        # driven has shown them one state out of a hundred and one.
        {"anchor": "s-ledger", "short": "LEDGER", "label": "Two processes",
         "done_when": "light_moved"},
        {"anchor": "s-stomata", "short": "STOMA", "label": "Stomata",
         "mirrors": "s-ledger", "done_when": "light_moved"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "Seal a healthy plant in a jar with a carbon dioxide sensor. "
                 "At dawn, the reading stops falling.",
        "prompt": "Overnight the carbon dioxide in the jar rose steadily. As "
                  "the light came up it began to fall. Then, at one particular "
                  "light level in the early morning, it held perfectly steady "
                  "for several minutes — neither rising nor falling — before "
                  "starting to fall again.",
        "commit": "What is the plant doing during those steady minutes?",
        "options": [
            "Nothing — it is between processes",
            "Only photosynthesis, at a very low rate",
            "Respiring and photosynthesising at exactly equal rates",
            "It has closed its stomata so no gas can move",
        ],
        "reveal": "Both processes at full tilt, cancelling out. The plant is "
                  "respiring and producing carbon dioxide at exactly the rate "
                  "photosynthesis is consuming it. A flat line does not mean "
                  "nothing is happening — here it means two things are "
                  "happening at identical rates, and it is the single best "
                  "piece of evidence that plants never stop respiring.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ `BREATH-12` and `BREATH-13` are the ids NOTES-B4 §5 pins to THIS
    # lesson: "the most persistent misconception in KS3 biology", with B7's
    # `the-photosynthesis-reaction` and `why-almost-all-life-depends-on-it`
    # named as the resurfacing sites that should re-confront rather than
    # restate. The `BREATH` family has no row in
    # `docs/ks3/misconception-register.md` yet — NOTES mints thirteen, the
    # rows were never written, and the commander reconciles all five lessons'
    # numbering in one pass. Nothing machine-reads the register, so the build
    # is unaffected.
    #
    # ⊕ COMMANDER'S CALL, MRB-244 — the third wrong idea GETS an id.
    #
    # It was authored inline in `statements[]` with no register entry, on the
    # correct reasoning that NOTES numbers the family to 13 and both of this
    # lesson's pinned ids were spent. The family goes to 15 instead.
    #
    # NOTES' thirteen was always over-subscribed: five pages carry fifteen
    # quotes. Leaving the surplus two id-less would have reached the student
    # either way — an authored statement wins over the register in
    # `r_confrontation` — but an id is not for the student, it is the JOIN. The
    # note four lines up says B7 re-confronts this lesson's ideas rather than
    # restating them, and a misconception with no id cannot be joined to a
    # later unit, counted, or re-confronted on purpose. That is the same defect
    # class as a fact kept away from its subject, so both surplus quotes are
    # minted: `BREATH-14` on `how-breathing-works` and `BREATH-15` here.
    "misconceptions": [
        {"id": "BREATH-12",
         "statement": "Plants take in carbon dioxide and give out oxygen. "
                      "Animals do the opposite.",
         # The ledger elicits it: the student drags the light to zero and
         # watches the net bar flip to the same direction as their own
         # breathing, before the block below names the belief.
         "elicited_by": "light-ledger",
         "confronted_by": "think-net"},
        {"id": "BREATH-13",
         "statement": "Plants respire at night and photosynthesise in the day.",
         "elicited_by": "light-ledger",
         "confronted_by": "think-net"},
        # ⊕ MRB-244. The statement is lifted from the quote authored in
        # `think-net` below and the two must stay identical — the confrontation
        # is what the student reads, this row is what the register joins on.
        # `elicited_by` is the block itself, not the ledger: the ledger never
        # surfaces this belief (it draws no stoma and moves no air), so
        # claiming it elicits it would be a false join. Same shape b4-01 used
        # for the two ideas nothing on its page asks for first.
        {"id": "BREATH-15",
         "statement": "Plants breathe through their stomata.",
         "elicited_by": "think-net",
         "confronted_by": "think-net"},
    ],

    # Design draws no keyword block anywhere in B4, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list.
    #
    # ⚠️ "compensation point" is deliberately ABSENT. NOTES-B4 flag 15 is
    # explicit that Design introduces it as a label for a phenomenon the
    # student has just produced and not as vocabulary to learn; a chip under
    # "Words this unit gives you" would make it exactly the second thing.
    "vocabulary": [
        {"term": "stoma",
         "definition": "A pore in the leaf surface that gases diffuse through, "
                       "held open between two guard cells.",
         "note": "Plural: stomata. Most are on the underside of the leaf."},
        {"term": "guard cell",
         "definition": "One of the pair of cells that opens and closes a stoma "
                       "by taking in or losing water.",
         "note": None},
        {"term": "diffusion",
         "definition": "The spreading of a substance from where it is more "
                       "concentrated to where it is less concentrated, with "
                       "nothing pushing it.",
         "note": "It is the only way gases move in and out of a leaf."},
        {"term": "net movement",
         "definition": "What is left when two opposite flows are subtracted "
                       "from each other — the only part a sensor outside the "
                       "leaf can see.",
         "note": "A net of zero means two flows are equal, not that both have "
                 "stopped."},
        {"term": "turgid",
         "definition": "Swollen and firm because the cell is full of water.",
         "note": None},
    ],

    # ⚠️ EMPTY, AND MEASURED. This page's foot line names no figure slot —
    # unlike b4-01's and b4-03's, which name `b4-gas-exchange-labelled`.
    # NOTES-B4 flag 20 suggests a labelled stoma / guard-cell pair "would be
    # the obvious second slot" and says it has not invented one; declaring it
    # here would invent a sourcing task in `docs/ks3/diagram-manifest.md` for
    # artwork this page never references.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-ledger — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b4/__init__.py::_normalise. Design's block is
        # `ks3-block ks3-dark ks3-practical` (page line 110), so `practical` is
        # measured, not inherited. Payload keys follow
        # docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md §5 exactly.
        {"type": "two-process-ledger", "id": "light-ledger",
         "anchor": "s-ledger", "demand": "investigate",
         "eyebrow": "At the bench · turn the light up",
         "heading": "Two processes, one net figure",
         "head_counter": {"off": "currently dark", "on": "light adjusted"},
         "prompt": "Respiration is the top bar. Photosynthesis is the second. "
                   "What a sensor outside the leaf measures is only the "
                   "difference — the third.",

         "start_light": 0,
         "light_label": "Light level",
         "light_aria": "Light level",
         "dark_label": "darkness",
         "light_format": "{n} units",
         "presets": PRESETS,

         # ⚖️ RESPIRATION IS FLAT AND NEVER MOVES. It is a constant, not a
         # curve evaluated somewhere — that constancy is the entire contrast
         # the lesson is built on, and every rung, both confrontations and the
         # key note depend on the top bar not moving when the slider does.
         "resp_rate": 2,
         "curve": {"max": 9, "constant": 32, "scale": 9},
         "balanced_window": 0.25,
         # ⚑ The renderer raises unless this preset's light value lands inside
         # the balanced window. See the docstring: it is the gate that keeps
         # `verdicts.balanced.why`'s "This is the dawn reading from the hook"
         # true, and it is why `dawn` is 8.
         "balanced_preset": "dawn",
         "rate_format": "{v} units",

         "respiration": {
             "name": "Respiration — uses oxygen, makes carbon dioxide",
             "note": "Flat. Drag the light from one end to the other and this "
                     "bar does not move — that is the whole point."},
         "photosynthesis": {
             "name": "Photosynthesis — uses carbon dioxide, makes oxygen",
             "note_dark": "Zero in darkness. No light, no photosynthesis — but "
                          "the bar above is unaffected.",
             "note_light": "Rises with light, then levels off as other factors "
                           "become limiting."},
         "net": {
             "name": "What a sensor outside the leaf measures",
             "in_format": "net CO₂ in {v} units",
             "out_format": "net CO₂ out {v} units",
             "note": "Only the difference is visible from outside. Both "
                     "processes are always running underneath this figure."},

         # ⚖️ THREE BRANCHES, AND THE MIDDLE ONE IS THE LESSON. The verdict
         # flips tag, headline and reasoning together; `balanced` is the
         # compensation point and it is the only branch the hook points at.
         "verdicts": {
             "balanced": {
                 "tag": "The compensation point",
                 "head": "Flat line — and both processes at full rate.",
                 "why": "This is the dawn reading from the hook. "
                        "Photosynthesis is consuming carbon dioxide at exactly "
                        "the rate respiration produces it, so nothing appears "
                        "to happen. A sensor cannot tell this apart from a "
                        "dead plant, which is why the reasoning matters more "
                        "than the reading."},
             "uptake": {
                 "tag": "Net uptake of carbon dioxide",
                 "head": "Carbon dioxide moving in, oxygen moving out.",
                 "why": "Photosynthesis is outrunning respiration, so the "
                        "plant absorbs more carbon dioxide than it produces. "
                        "Respiration has not stopped — look at the top bar. It "
                        "is simply hidden underneath a larger opposite flow."},
             "release": {
                 "tag": "Net release of carbon dioxide",
                 "head": "Carbon dioxide moving out, oxygen moving in — the "
                         "same direction as you.",
                 "why": "In darkness only respiration is running, so the plant "
                        "takes in oxygen and gives out carbon dioxide, exactly "
                        "as an animal does. This is the reading that shows "
                        "plants and animals are not opposites."},
         }},

        # #s-stomata — the band panel. Rail stop 3, mirroring `s-ledger`; see
        # the docstring. `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid — Design's markup
        # (page lines 156–173) with the tags folded into the terms.
        {"type": "rule", "anchor": "s-stomata",
         "eyebrow": "How the gases get in",
         "statement": "A hole you can shut, and the price of shutting it.",
         "cards": STOMATA_CARDS,
         # Design's full-width card below the grid. Its tag keeps her own
         # <strong> treatment; see "What could not be lifted" 2.
         "close": "<strong>Same four requirements, third organ</strong> A leaf "
                  "meets the same four requirements as a villus and an "
                  "alveolus: a large internal surface where the air spaces "
                  "meet the cells, a very short diffusion distance from air "
                  "space to cell, a maintained concentration difference — the "
                  "cells consume whichever gas they need, keeping its level "
                  "low inside — and a moist surface, which is exactly why "
                  "water is lost through an open stoma. Three organs, three "
                  "shapes, one set of rules."},

        # Design nests this inside `#s-stomata`; `r_rule` has no nested slot, so
        # it renders directly under the panel in document order. See "What
        # could not be lifted" 3.
        {"type": "key-fact", "ref": "gases-diffuse-net-difference"},

        {"type": "misconception", "id": "think-net",
         "anchor": "s-think", "targets": "BREATH-12"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "gases-diffuse-net-difference",
         "text": "Gases diffuse in and out of a leaf through stomata, mostly "
                 "on the underside, opened and closed by guard cells. Plants "
                 "respire continuously and photosynthesise only in light; the "
                 "net movement of gas is the difference between the two.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # THREE wrong ideas in one "Think again" block, each behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and an authored statement wins over the register. The
        # block asks for no commitment, on Design's page and here, so it is not
        # a rail stop and emits no completion contract.
        {"id": "think-net",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "BREATH-12",
         "statements": [
             {"quote": "Plants take in carbon dioxide and give out oxygen. "
                       "Animals do the opposite.",
              "body": ["This describes photosynthesis and then calls it the "
                       "whole of plant biology. Every living cell respires — "
                       "glucose plus oxygen, releasing energy — and a plant "
                       "cell is not an exception, because a plant needs energy "
                       "to grow, to transport minerals and to make new tissue "
                       "in exactly the way you do. What is true is that in "
                       "good light photosynthesis runs several times faster "
                       "than respiration, so the net flow reverses and a "
                       "sensor outside the leaf records oxygen coming out. The "
                       "word doing all the work in that sentence is "
                       "<em>net</em>. Set the light to zero on the bench above "
                       "and the plant releases carbon dioxide and absorbs "
                       "oxygen — the same direction as you."]},
             {"quote": "Plants respire at night and photosynthesise in the day.",
              "body": ["Almost right, and wrong in the way that costs marks. "
                       "Respiration does not switch on at dusk; it never "
                       "switches off at all. In the middle of a bright "
                       "afternoon a leaf is respiring at exactly the rate it "
                       "was respiring at midnight — the top bar on the bench "
                       "does not move when you drag the light. What changes is "
                       "only the second bar. At night respiration is the "
                       "<em>only</em> process running, which is why it becomes "
                       "visible; during the day it is hidden underneath a "
                       "larger opposite flow. A process you cannot detect is "
                       "not a process that has stopped."]},
             # ⚠️ Design's inline link to `How breathing works` is dropped and
             # the words are unchanged — see "What could not be lifted" 4.
             {"quote": "Plants breathe through their stomata.",
              "body": ["Stomata are holes, and holes do not breathe. Nothing "
                       "in a plant does the muscular work you met in How "
                       "breathing works — there is no diaphragm, no rib cage, "
                       "no pressure difference generated, and no ventilation. "
                       "Gases arrive and leave entirely by diffusion, driven "
                       "by nothing but the concentration difference the cells "
                       "themselves create by consuming one gas or the other. A "
                       "plant does not breathe, and this is not a small verbal "
                       "distinction: it is why a plant can be metres tall with "
                       "no circulation of air inside it at all, and why leaves "
                       "have to be thin."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS PASS.
    #   rung 1: correct 6w against distractors of 3 / 11 / 5 — not the longest.
    #   rung 2: correct 8w against distractors of 5 / 8 / 9 — not the longest.
    # No distractor was rewritten, because there was nothing to repair.
    "ladder": {
        "recall": {
            "title": "Rung 1 · When does a plant respire",
            "q": "When does a plant respire?",
            "options": [
                "Only at night",
                "Only in the day, using the glucose it has just made",
                "All the time, day and night",
                "Only when it is growing",
            ],
            "answer": 2,
            "feedback": {
                0: "Night is only when respiration becomes visible, because "
                   "nothing is masking it. The rate itself does not change — "
                   "watch the top bar as you move the light.",
                1: "Backwards. Respiration continues in the dark, using "
                   "glucose stored earlier — which is exactly why the carbon "
                   "dioxide in a sealed jar rises overnight.",
                3: "Every living cell respires continuously, growing or not. "
                   "Even a dormant seed respires, slowly.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A sealed jar containing a plant shows no change in carbon "
                 "dioxide for ten minutes in dim light. What is happening?",
            "options": [
                "Nothing — the plant is dormant",
                "Photosynthesis and respiration are happening at equal rates",
                "Photosynthesis has stopped and respiration has not started",
                "The stomata have closed, so no gas can move",
            ],
            "answer": 1,
            "feedback": {
                0: "A flat reading is not an idle plant. Two processes are "
                   "running and cancelling, which is a very different "
                   "situation from neither running.",
                2: "Respiration never stops, so it cannot be waiting to start. "
                   "And if only respiration were running, the carbon dioxide "
                   "would be rising.",
                3: "Closed stomata would also stop water loss and would show "
                   "up as a flat line only by accident. In dim light the "
                   "simplest explanation is two equal opposite rates.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the net figure",
            "q": "Explain why a plant absorbs carbon dioxide in bright light "
                 "but releases it in darkness, without saying that respiration "
                 "stops or starts. Use the words net, rate and continuously.",
            "field_label": "Your explanation",
            "placeholder": "Respiration runs continuously at…",
            "success": [
                "States that respiration runs continuously at a roughly steady "
                "rate, in light and dark.",
                "States that photosynthesis runs only in light, and faster in "
                "brighter light.",
                "Says that in bright light photosynthesis exceeds respiration, "
                "so the net movement of carbon dioxide is inwards.",
                "Says that in darkness only respiration is running, so the net "
                "movement is outwards.",
                "Uses the word net correctly and never says respiration stops.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A grower keeps greenhouse lights on for 24 hours to maximise "
                 "growth. A colleague argues this wastes electricity because "
                 "the plants also need a dark period. Using this lesson, say "
                 "what continuous light does and does not achieve, and what "
                 "evidence would settle the argument.",
            "field_label": "Your answer",
            "placeholder": "Continuous light means photosynthesis…",
            "success": [
                "Says continuous light keeps photosynthesis running, so net "
                "carbon dioxide uptake and net growth continue through the "
                "night.",
                "Notes that respiration continues regardless, so it is not the "
                "thing being switched on or off.",
                "Recognises that the claim about needing darkness is a "
                "separate biological question, not settled by gas exchange "
                "alone.",
                "Proposes a fair test — identical plants, one on continuous "
                "light and one on a day/night cycle, comparing growth against "
                "energy used.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Stomata are pores in the leaf surface, mostly on the "
                "underside, controlled by a pair of guard cells. Gases move "
                "through them by diffusion only — plants do not breathe. "
                "Plants respire all the time; they photosynthesise only in "
                "light. The net gas movement is the difference between the two "
                "rates, and at one particular light level it is zero.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    "stretch": [
        {"type": "explainer", "id": "cam-photosynthesis",
         "text": "Cacti and pineapples solve the stomatal dilemma by moving it "
                 "in time rather than solving it. Opening a stoma in desert "
                 "daylight loses catastrophic amounts of water, so these "
                 "plants keep them shut all day and open them at night, when "
                 "the air is cool and damp. Carbon dioxide taken in at night "
                 "is fixed into an acid and stored in the cells until morning, "
                 "then released internally and fed into photosynthesis behind "
                 "closed stomata. It is called CAM photosynthesis, and it "
                 "costs energy and limits growth rate — which is why cacti "
                 "grow so slowly, and why the strategy only makes sense where "
                 "water, not time, is the thing in shortest supply. Taste a "
                 "pineapple leaf early in the morning and it is noticeably "
                 "sour; by evening it is not."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check what the flat line at dawn actually "
                      "means?",
              "cta": "Ask about this lesson",
              "anchor": "s-ledger"},

    # ⚠️ `convention_note`, NOT `safety_note`. There is nothing to be careful
    # of on this page — this is a statement about how the numbers on the bench
    # were taken and where the reaction itself is taught, and MRB-228 gave that
    # its own foot slot precisely so it does not ship in the treatment reserved
    # for "never light a candle without an adult". Design's `<em>` around
    # *Photosynthesis* is lost to `t()`; the words are unchanged.
    "convention_note": "Rates on the bench are relative units chosen to make "
                       "the two processes comparable, not measured values. The "
                       "light level at which the two balance differs widely "
                       "between species and conditions. B7 Photosynthesis owns "
                       "the reaction itself; this lesson covers only the "
                       "movement of gases.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
