"""B4 L1 — The gas exchange system (SYSTEM).

Authored against Design's approved page,
`KS3 B4 lessons/b4-01-the-gas-exchange-system.dc.html` (577 lines), under the
MRB-220 build contract, with the instrument authored against
`docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md` §1.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", none of which is a
sentence of science. The four gas rows, the three prediction buttons, the six
route cards and all four ladder rungs came out of
`node tools/extract_design_payload.js`, not off a keyboard.

── `covers` is the SUB-ID, not the whole bullet ─────────────────────────

`KS3.B.GAS.01` is *"the structure and functions of the gas exchange system in
humans, including adaptations to function"*, and `ks3_data/substatements.py`
splits it at its own "including". This lesson owns **`KS3.B.GAS.01a`** — the
parts air passes through and what each one does. It must NOT claim `GAS.01`
whole: `alveoli-built-for-exchange` owns `GAS.01b`, the adaptations clause, and
§5.7's exactly-once rule would fail the build on the overlap. The six-part route
here stops at *what the alveoli are*; *why they are shaped that way* is lesson 3
and this page deliberately does not answer it.

── The flagship: the prediction is what unlocks the evidence ────────────

`#s-air` is `gas-compare`, on `ks3-block ks3-dark ks3-practical` (page line
114), so `practical` is MEASURED from Design's own markup rather than inherited
from the block above it. Four gases, one up/down/same prediction each, and
"Analyse both bags" stays locked until all four are committed — a student who
could read the table first and then say what they expected has predicted
nothing.

⚖️ THE CLAMP IS THE ONE DISHONEST PIXEL, AND THE NUMERAL IS WHAT REDEEMS IT.
`min_bar_pct` is left at the schema's 1.5 default, which draws carbon dioxide's
0.04% bar about 37× too wide so that it is visible at all. That is why
`in_label` and `out_label` are authored on every row and why they sit beside
the bar: the bar says *that* it changed, and the numeral is the only thing on
the page that says *by how much*. NOTES-B4 §3.1 makes the same point in the
same words.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-parts` came off the rail. Design draws FOUR stops and `#s-parts` ticks on
`s.airOpen` (page line 417) — the BENCH's predicate, verbatim, one section to
the left — and because `#s-parts` is an eyebrow, a statement, six static cards
and a key fact with no control, no commitment and no field, the reading was
that MRB-208's completion rule forbade the stop and
`ks3_parity.check_rail_reachable` would fail it for carrying none of the
signals `doneByDom()` reads. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. Dropping a stop Design drew is not
rendering what Design drew.

And Design's `isDone()` states the tick condition rather than leaving it to be
inferred. It is a rail-level function and it returns the identical expression
for `#s-air` and then for `#s-parts`. The route in is the payoff of the two
bags beside it; the section holds no control because the bench has already
taken the student's commitment. That is a MIRROR, resolved at rail level in
`wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-parts`, `mirrors: "s-air"`,
`done_when: "both_bags_analysed"` — the bench's own predicate, named as
borrowed rather than smuggled, and gated by `check_rail_matches_design` against
`docs/ks3/rail-manifest.md`. c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-01's
`#s-nutrients` and b3-02's `#s-limits` are restored the same way. The section
keeps its anchor, as it always did, so the tutor card's `#s-parts` link and
every hash link into it still work.

── What could not be lifted, and why ────────────────────────────────────

1. **The route cards' NUMBER CHIPS, and their column.** Design draws `#s-parts`
   as an `<ol>` of six full-width cards, each with an ink `01`–`06` chip.
   `r_rule` emits a `<ul>` on a `repeat(auto-fit, minmax(220px, 1fr))` grid and
   has no slot for a numeral. Document order is preserved, so the route still
   reads in order; the chips are DROPPED rather than smuggled into the card
   text. Reported. The fix, if the chips are to win, is an `index` flag on
   `rule` — not a new block type, because §5.1.1's vocabulary is closed and
   `render_blocks` raises on anything outside it.

2. **The `role` tag is FOLDED into the card term, not dropped.** Design sets it
   in mono accent type on the same baseline as the part's name
   (`Alveoli` / `Gas exchange — the only place`), and `r_rule`'s card is two
   parts. All six roles are DIFFERENT strings and every one of them is science
   — "Transport" and "Gas exchange — the only place" are the whole argument of
   the section — so dropping them the way b3-02 dropped its repeated `It cannot
   say` tag would lose content. They are joined to the name with " · ", which
   is b3-05's `#s-two` precedent (`Mechanical digestion · Making pieces
   smaller`) and Design's own separator elsewhere on the page. Both strings
   survive byte-identical.

3. **The key fact leaves Design's band panel.** She nests it inside `#s-parts`;
   `r_rule` has no nested key-fact slot (only `r_comparison` does), so it
   renders as its own top-level block directly under the panel, on the band
   ground every other top-level key fact in the key stage takes. The words are
   unchanged and the order is unchanged.

4. **Design draws TWO endmatter link cards; the engine emits one.** Her
   "Next in this unit" (`how-breathing-works`) and "Connects to"
   (`levels-of-organisation`, `alveoli-built-for-exchange`) are one card in
   `r_endmatter`, headed by `connects_heading`. All three links live in it, the
   forward one first, under "Connects to" — b3-01 resolved the identical layout
   the identical way. The heading "Next in this unit" is what is given up; no
   link is.

5. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

⚑ For Mide's science gate — NOTES-B4 §4 flags landing on THIS lesson:
  * flag 2 — the composition figures (78 / 21 / 0.04 → 78 / 16 / 4, warmer and
    saturated), and whether water vapour given as "variable, often low" →
    "saturated" rather than as percentages is acceptable. Authored as
    delivered; the two words are the `in_label` / `out_label` of the h2o row.
  * flag 3 — *"You keep roughly a quarter of the oxygen you take in."* 21 → 16
    is 24%. The hook's reveal and rung 4 both depend on the phrasing.
  * flag 4 — ~500 million alveoli. Stated twice on this page (route card 05 and
    the third confrontation) and once more in b4-03.
  * flag 5 — *"about twenty-three generations of branching"* (Weibel), in route
    card 04 and again in the third confrontation.
  * flag 6 — *"a piece of fresh lung tissue floats"*, used to argue against the
    balloon picture. True of inflated lung.
  * flag 7 — the nitrogen stretch layer, which forward-references B9 and C6.
  * flag 20 — `b4-gas-exchange-labelled` is named in Design's legal line and is
    not in `docs/ks3/diagram-manifest.md`. Declared here at `status: "needed"`
    (§4.10, not a build blocker) so it is a tracked sourcing task rather than a
    dangling reference. Nothing is invented to fill it.

⚑ One wording flag of my own, and the page WINS pending your call:
  the `#s-parts` statement reads *"Six parts, and only the last one exchanges
  anything."* — but the sixth card is the ribs, intercostal muscles and
  diaphragm, which exchange nothing and are explicitly "not part of the airway
  at all". The exchanger is the fifth. Read as "the last part of the airway" it
  is right; read literally it is not. Lifted byte-identical either way, because
  MRB-205 says the page wins and this is a sentence of teaching copy, not a
  build fault.
"""

# ── the four gases (page lines 345–354, via extract_design_payload.js) ───
#
# ⚠️ `in_label` / `out_label` are AUTHORED, never composed from the percentages.
# Water vapour's two cells are words — "variable, often low" → "saturated" —
# because Design deliberately refused to give it as a number, and a template
# built from `in_pct` would print "1%" for a figure the page will not claim.
# PAYLOAD-SCHEMA.md §1 requires both for the same reason.
GASES = [
    {"id": "n2", "name": "Nitrogen",
     "in_pct": 78, "out_pct": 78, "change": "same",
     "in_label": "78%", "out_label": "78%",
     "verdict": "unchanged"},
    {"id": "o2", "name": "Oxygen",
     "in_pct": 21, "out_pct": 16, "change": "down",
     "in_label": "21%", "out_label": "16%",
     "verdict": "falls by about a quarter"},
    {"id": "co2", "name": "Carbon dioxide",
     "in_pct": 0.04, "out_pct": 4, "change": "up",
     "in_label": "0.04%", "out_label": "4%",
     "verdict": "rises a hundredfold"},
    {"id": "h2o", "name": "Water vapour",
     "in_pct": 1, "out_pct": 6, "change": "up",
     "in_label": "variable, often low", "out_label": "saturated",
     "verdict": "rises — and it is warmer"},
]

# The three prediction buttons, identical on every row (page lines 356–360).
# `id` is what `gases[].change` is matched against — the renderer raises if a
# row's right answer is not among these, so a row can never be unanswerable.
CHOICES = [
    {"id": "up", "label": "Goes up"},
    {"id": "down", "label": "Goes down"},
    {"id": "same", "label": "Stays the same"},
]

# ── the six parts of the route (page lines 362–369) ─────────────────────
#
# Design's `role` is joined to `name` with " · " — see "What could not be
# lifted" 2. The `what` prose is untouched.
ROUTE = [
    ("Nose and mouth", "Conditioning",
     "Air is warmed to body temperature, moistened, and filtered by hairs and "
     "mucus. Breathing through the nose does this far better than through the "
     "mouth, which is why cold dry air through an open mouth irritates the "
     "airways."),
    ("Trachea", "Transport",
     "A single tube down the front of the neck, held open by C-shaped rings of "
     "cartilage so it cannot collapse when the pressure inside drops. Lined "
     "with mucus and cilia that sweep trapped dust and bacteria back up."),
    ("Bronchi", "Transport",
     "The trachea divides into two, one bronchus to each lung. Still wide, "
     "still ringed with cartilage, still lined with cilia. No exchange happens "
     "here."),
    ("Bronchioles", "Transport",
     "Each bronchus divides again and again — about twenty-three generations "
     "of branching in total — into ever narrower tubes with muscle in their "
     "walls instead of cartilage. That muscle is what narrows in an asthma "
     "attack."),
    ("Alveoli", "Gas exchange — the only place",
     "Around 500 million tiny air sacs, each wrapped in capillaries, each with "
     "a wall one cell thick. This is where oxygen enters the blood and carbon "
     "dioxide leaves it, and it is the only place in the body where that "
     "happens."),
    ("Ribs, intercostal muscles and diaphragm", "Moving the air",
     "Not part of the airway at all — the machinery that changes the volume of "
     "the chest, and so moves air in and out. The lungs contain no muscle of "
     "their own and cannot move themselves. That is the next lesson."),
]

ROUTE_CARDS = [{"term": "%s · %s" % (name, role), "gloss": what}
               for name, role, what in ROUTE]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 114 character for character.
    "slug":        "the-gas-exchange-system",
    "title":       "The gas exchange system",
    "discipline":  "biology",
    "unit":        "breathing-and-gas-exchange",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `a` clause of the split bullet — the parts and their jobs. See the
    # docstring; `b` belongs to `alveoli-built-for-exchange`.
    "covers":      ["KS3.B.GAS.01a"],
    # Named but not taught: the key fact and the second confrontation both turn
    # on respiration being a different process (B8 owns it), and the route ends
    # in a hierarchy of organs (B1's CELLS.06).
    "touches":     ["KS3.B.RESP.01", "KS3.B.CELLS.06"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 1},
                    {"id": "substances-and-reactions", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires`: Design draws no "Before this lesson" card, this is the
    # unit's first lesson, and the engine omits an empty card. All three of her
    # forward and sideways links live in the middle card — see "What could not
    # be lifted" 4.
    "requires":    [],
    "assumes":     [],
    "references":  ["how-breathing-works",
                    {"unit": "B1", "lesson": "levels-of-organisation"},
                    "alveoli-built-for-exchange"],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "The gas exchange system in detail, ventilation rates, and "
                   "the link to aerobic and anaerobic respiration.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Breathe out into a bag and analyse it. There is four "
                    "times more oxygen in there than carbon dioxide. Most "
                    "people are surprised, and the surprise is worth taking "
                    "seriously.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-parts` is the third: no control of
    # its own, so it mirrors `s-air` and ticks on the bench's predicate — see
    # the docstring. `short` and `label` are Design's own `RAIL_SHORT` and
    # `RAIL` strings (page lines 337–343).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Mouth-to-mouth",
         "done_when": "committed"},
        # Design's own threshold, kept: the stage ticks when the REVEAL opens,
        # and the reveal cannot open until all four gases are committed. A stop
        # that ticked on the first prediction would call the bench finished at
        # a quarter of it.
        {"anchor": "s-air", "short": "BAGS", "label": "Two bags",
         "done_when": "both_bags_analysed"},
        {"anchor": "s-parts", "short": "ROUTE", "label": "The route in",
         "mirrors": "s-air", "done_when": "both_bags_analysed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "Mouth-to-mouth resuscitation works.",
        "prompt": "You breathe out into someone who has stopped breathing, and "
                  "it keeps them alive. Their blood is re-oxygenated by air "
                  "that has already been through your lungs.",
        "commit": "What does that tell you about the air you breathe out?",
        "options": [
            "It has no oxygen left — something else must be keeping them alive",
            "It still contains most of the oxygen that went in",
            "It is mostly carbon dioxide, which the body can use in an "
            "emergency",
            "It works only because the rescuer breathes very deeply first",
        ],
        "reveal": "It is still mostly the air that went in. Of every 100 parts "
                  "of air you exhale, about 78 are nitrogen, about 16 are "
                  "oxygen and about 4 are carbon dioxide. You keep roughly a "
                  "quarter of the oxygen you take in and pass the rest "
                  "straight back out — which is exactly why exhaled air can "
                  "keep someone else alive.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ The `BREATH` family is NOT yet in `docs/ks3/misconception-register.md`
    # — NOTES-B4 §5 mints thirteen for this unit and the commander maintains
    # the register centrally. These are the first three, in Design's page order,
    # and the numbering is the one NOTES gives: b4-03's diffusion pair has to
    # land on BREATH-06/07 (they are PART-10/11 for the third time), which is
    # only true if this lesson takes 01–03.
    #
    # `elicited_by` is honest per entry: the bench really does surface 01 —
    # the student commits to what happens to oxygen and to carbon dioxide
    # before seeing either — while 02 and 03 are not asked for anywhere before
    # the block that kills them, so the block is named for both. b3-04's
    # `think-balanced` is the same pattern.
    "misconceptions": [
        {"id": "BREATH-01",
         "statement": "You breathe in oxygen and breathe out carbon dioxide.",
         "elicited_by": "two-bags",
         "confronted_by": "three-wrong-ideas"},
        {"id": "BREATH-02",
         "statement": "Breathing and respiration are the same thing.",
         "elicited_by": "three-wrong-ideas",
         "confronted_by": "three-wrong-ideas"},
        {"id": "BREATH-03",
         "statement": "Your lungs are hollow bags that fill up like balloons.",
         "elicited_by": "three-wrong-ideas",
         "confronted_by": "three-wrong-ideas"},
    ],

    # Design draws no keyword block anywhere in B4, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list — which matters here,
    # because "trachea", "bronchioles", "alveoli" and "cilia" would otherwise
    # all count against the page.
    "vocabulary": [
        {"term": "breathing",
         "definition": "Moving air in and out of the lungs, using muscles.",
         "note": "A mechanical process, not a chemical one."},
        {"term": "gas exchange",
         "definition": "Oxygen and carbon dioxide swapping between the air in "
                       "the alveoli and the blood.",
         "note": "It happens nowhere else in the body."},
        {"term": "respiration",
         "definition": "The chemical reaction inside every cell that releases "
                       "energy from glucose.",
         "note": "Plants do it too, and they do not breathe."},
        {"term": "trachea",
         "definition": "The single tube from the throat to the lungs, held "
                       "open by rings of cartilage.",
         "note": None},
        {"term": "bronchioles",
         "definition": "The narrowest branches of the airway, with muscle in "
                       "their walls instead of cartilage.",
         "note": None},
        {"term": "alveoli",
         "definition": "The tiny air sacs at the end of the airway where gas "
                       "exchange happens.",
         "note": "About 500 million of them, each wall one cell thick."},
        {"term": "cilia",
         "definition": "Tiny hairs lining the airway that sweep trapped dust "
                       "and bacteria back up.",
         "note": None},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # Design's legal line names this slot and no artwork exists for it, so it is
    # DECLARED at `needed` rather than dropped: the manifest is generated from
    # this field, which turns a dangling reference into a tracked sourcing task.
    # `needed` is not a build blocker. No `figure` block is added to `core` —
    # Design draws no figure slot on the page, and one here would be a
    # component nobody drew. The caption describes only what this lesson
    # teaches: the six parts, with the muscles shown around the lungs rather
    # than as part of the airway, which is the route's own last card.
    "figures": [
        {"id": "b4-gas-exchange-labelled",
         "kind": "diagram",
         "caption": "The human gas exchange system, labelled: nose and mouth, "
                    "trachea, bronchi, bronchioles and alveoli, with the ribs, "
                    "intercostal muscles and diaphragm drawn around the lungs "
                    "rather than as part of the airway.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-air — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b4/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 114), so the segment is measured and not inherited.
        # Payload keys follow docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md §1.
        {"type": "gas-compare", "id": "two-bags", "anchor": "s-air",
         "demand": "investigate",
         "eyebrow": "At the bench · two bags of air",
         "heading": "Predict the numbers, then see them",
         "head_counter": {"format": "{n} of 4 predicted", "total": 4},
         "prompt": "For each gas, say what happens to it between going in and "
                   "coming out.",

         "gases": GASES,
         "choices": CHOICES,

         # ⚖️ LOCKED UNTIL ALL FOUR ARE COMMITTED. The button is the reveal and
         # there is no separate run control: commitment is what buys the
         # evidence.
         "reveal_label": "Analyse both bags",
         "count": {"committed": "{n} of {total} committed",
                   "scored": "{n} of {total} predicted correctly"},

         # The reveal table's three headings. They are also the per-cell
         # captions below 880px, where the header row hides — so a stacked
         # figure still says which bag it came out of.
         "table": {"gas": "Gas",
                   "inhaled": "Inhaled air",
                   "exhaled": "Exhaled air"},

         # `min_bar_pct` is left at the schema default of 1.5. See the docstring
         # — the clamp is why the numerals beside the bars are not optional.
         "close_lead": "The two that matter:",
         "close": "oxygen falls from 21 to 16, so you removed about a quarter "
                  "of it. Carbon dioxide rises from 0.04 to 4, a hundredfold "
                  "increase — but it is still only a twenty-fifth of the bag. "
                  "Nitrogen is unchanged: your body has no use for it and no "
                  "way of using it. Exhaled air is warmer and saturated with "
                  "water vapour, which is why you can see your breath on a "
                  "cold day."},

        # #s-parts — the band panel. Rail stop 3, mirroring `s-air`; see the
        # docstring. `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid on the option
        # border — Design's markup (page lines 172–189) minus the number chips.
        {"type": "rule", "anchor": "s-parts",
         "eyebrow": "The route in",
         "statement": "Six parts, and only the last one exchanges anything.",
         "cards": ROUTE_CARDS},

        # Design nests this inside `#s-parts`; `r_rule` has no nested slot, so
        # it renders directly under the panel in document order. See "What
        # could not be lifted" 3.
        {"type": "key-fact", "ref": "three-different-words"},

        {"type": "misconception", "id": "three-wrong-ideas",
         "anchor": "s-think", "targets": "BREATH-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "three-different-words",
         "text": "Breathing is the movement of air in and out. Gas exchange is "
                 "oxygen and carbon dioxide swapping between air and blood, "
                 "and it happens only in the alveoli. Respiration is a "
                 "chemical reaction inside every cell. Three different things, "
                 "three different words.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # THREE wrong ideas in one "Think again" block, each after the last
        # behind an amber-topped divider — `r_confrontation` renders exactly
        # that from `statements[]`, and an authored statement wins over the
        # register. The block asks for no commitment, on Design's page and
        # here, so it is not a rail stop and emits no completion contract.
        {"id": "three-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "BREATH-01",
         "statements": [
             {"quote": "You breathe in oxygen and breathe out carbon dioxide.",
              "body": ["Read that sentence as a statement about the contents "
                       "of the two bags and it is badly wrong. You breathe in "
                       "air that is 21% oxygen and breathe out air that is 16% "
                       "oxygen — so the largest gas in both directions is "
                       "nitrogen, and the second largest in both directions is "
                       "oxygen. Carbon dioxide is the fourth thing in the bag, "
                       "behind water vapour on a warm day. What is true is "
                       "that oxygen moves <em>into</em> the blood and carbon "
                       "dioxide moves <em>out of</em> it, which is a claim "
                       "about direction of movement rather than about "
                       "composition. Write “oxygen diffuses from the alveoli "
                       "into the blood, and carbon dioxide diffuses from the "
                       "blood into the alveoli” and you have said something "
                       "defensible."]},
             {"quote": "Breathing and respiration are the same thing.",
              "body": ["They are separated by about a metre and by the whole "
                       "of chemistry. Breathing is a mechanical process "
                       "performed by muscles, moving air between the "
                       "atmosphere and your alveoli. Respiration is a chemical "
                       "reaction — glucose and oxygen releasing energy — "
                       "happening in the mitochondria of every one of your "
                       "cells, including the ones in your toes. A plant "
                       "respires and does not breathe. A person on a "
                       "ventilator is being breathed for, and is respiring "
                       "entirely on their own. If you use the word respiration "
                       "to mean breathing in an exam, you have made a mistake "
                       "examiners consider significant, because the two are "
                       "studied in different chapters for a reason."]},
             {"quote": "Your lungs are hollow bags that fill up like balloons.",
              "body": ["A lung is not a bag with air in it — it is a "
                       "solid-feeling sponge, and a piece of fresh lung tissue "
                       "floats. The bronchi divide about twenty-three times, "
                       "each branch narrower than the last, ending in some 500 "
                       "million alveoli. Nothing in that structure is a single "
                       "open cavity. The reason matters: a balloon has almost "
                       "no surface area for its volume, and gas exchange is "
                       "limited entirely by surface area. Every one of those "
                       "twenty-three divisions exists to turn a bag into a "
                       "surface."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS PASS.
    #   rung 1: correct 1w against distractors of 1 / 3 / 2 — the correct
    #           option is not the longest, so length is no tell.
    #   rung 2: correct 1w against distractors of 2 / 1 / 2 — likewise.
    # No distractor was rewritten, because there was nothing to repair.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Three words",
            "q": "A plant in a dark cupboard is releasing carbon dioxide. "
                 "Which of the three processes is it carrying out?",
            "options": [
                "Breathing",
                "Respiration",
                "Gas exchange only",
                "All three",
            ],
            "answer": 1,
            "feedback": {
                0: "Plants have no muscles to move air and no airway. Nothing "
                   "is being ventilated.",
                2: "Gases do move in and out of a plant, but the question is "
                   "what is producing the carbon dioxide — and that is a "
                   "chemical reaction in the cells.",
                3: "A plant never breathes. Reserve that word for muscular "
                   "ventilation of an airway.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Which gas makes up the largest part of the air you breathe "
                 "OUT?",
            "options": [
                "Carbon dioxide",
                "Oxygen",
                "Nitrogen",
                "Water vapour",
            ],
            "answer": 2,
            "feedback": {
                0: "Only about 4%. It rises a hundredfold and is still the "
                   "fourth thing in the bag — this is the most common wrong "
                   "answer in the topic.",
                1: "Second, at about 16%. Closer than most people think, but "
                   "not the largest.",
                3: "Exhaled air is saturated with water vapour, but saturated "
                   "still means only a few per cent.",
            }},
        "explain": {
            "title": "Rung 3 · Rewrite the sentence",
            "q": "A student writes: “We breathe in oxygen and breathe out "
                 "carbon dioxide.” Explain what is wrong with it as a "
                 "statement about the air, and write a version that is "
                 "defensible. Use figures.",
            "field_label": "Your answer",
            "placeholder": "The sentence is wrong because… A better version "
                           "is…",
            "success": [
                "Gives the inhaled figures — about 21% oxygen and 0.04% carbon "
                "dioxide.",
                "Gives the exhaled figures — about 16% oxygen and 4% carbon "
                "dioxide.",
                "Points out that exhaled air still contains far more oxygen "
                "than carbon dioxide.",
                "Notes that nitrogen is the largest component both ways and is "
                "unchanged.",
                "Rewrites it as a claim about direction of diffusion rather "
                "than about composition.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Explain why mouth-to-mouth resuscitation can keep someone "
                 "alive, using the composition figures. Then say why a "
                 "rescuer’s own breathing rate rises while they do it, and "
                 "which of the three processes that change belongs to.",
            "field_label": "Your answer",
            "placeholder": "It works because the exhaled air still contains…",
            "success": [
                "States that exhaled air still contains about 16% oxygen, "
                "enough to oxygenate the casualty’s blood.",
                "Notes that oxygen will diffuse into the casualty’s blood "
                "because their blood oxygen is lower still.",
                "Explains the rescuer’s faster breathing as their own muscles "
                "working harder and respiring faster.",
                "Correctly assigns the raised rate to breathing, driven by the "
                "products of respiration — not to gas exchange failing.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Air travels through the trachea, bronchi and bronchioles to "
                "about 500 million alveoli, where gas exchange happens. "
                "Inhaled air is 21% oxygen and 0.04% carbon dioxide; exhaled "
                "air is about 16% oxygen and 4% carbon dioxide, warmer and "
                "saturated with water vapour. Nitrogen is unchanged. "
                "Breathing, gas exchange and respiration are three different "
                "processes.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES-B4 flag 7: this forward-references B9 and C6, and does it as a
    # closing thought rather than as content either unit has to honour.
    "stretch": [
        {"type": "explainer", "id": "the-element-you-cannot-touch",
         "text": "Nitrogen is 78% of every breath you have ever taken and your "
                 "body does nothing with any of it — you exhale exactly what "
                 "you inhaled. Yet nitrogen is in every protein and every "
                 "strand of DNA in you, so you plainly acquire it somehow. The "
                 "answer is that you get all of it from food, because breaking "
                 "the triple bond in N₂ is beyond any animal. Certain bacteria "
                 "can do it, some of them living in nodules on the roots of "
                 "pea and bean plants, and everything else on Earth ultimately "
                 "depends on that chemistry. You are breathing your own most "
                 "essential element in and straight back out again, twenty "
                 "thousand times a day, unable to touch it."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still mixing up breathing, gas exchange and "
                      "respiration?",
              "cta": "Ask about this lesson",
              "anchor": "s-parts"},

    # ⊕ MRB-228's `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph here and nothing in it is a safety instruction —
    # it is a note about how the figures on this page were taken, and a
    # declaration about a figure that has not been drawn yet. Routing it
    # through `safety_note` would print it in the treatment reserved for
    # "never light a candle without an adult", which devalues the safety line.
    # b3-05 and b3-07 resolve the identical foot line the identical way.
    #
    # ⚠️ The figure id keeps its plain text; Design sets it in mono inside the
    # sentence and a foot line is escaped, so the id renders in body copy and
    # the words are unchanged.
    "convention_note": "Composition figures are rounded typical values for a "
                       "person at rest; exhaled composition changes with "
                       "activity and with how long the breath is held. The "
                       "labelled diagram is declared in the lesson record as "
                       "b4-gas-exchange-labelled, awaiting illustration.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is predict-then-read-the-data: four committed predictions
    # scored against a table the student then has to interpret.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
