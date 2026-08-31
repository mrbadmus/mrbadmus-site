"""P11 L1 — Density (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p11/p11-01-density.dc.html`.

Her page wins outright. The pan balance, the six-material bench, the
triangle, both worked examples, both attempt questions and all four rungs
are hers, ported from her JavaScript constants rather than from her HTML —
a `.dc.html` renders every one of them from a `{{ }}` hole and an HTML
comparison would have reported a match against anything.

── ⚖️ MRB-204 · A TRIANGLE, AND `m` IS THE LETTER ON TOP ─────────────

`m = d × V` is a genuine PRODUCT, so the triangle is right and the mass
goes above the line with the density and the volume beside each other
below it. That is exactly what Design draws — her `<text>` elements put
`m` at y=100 above the divider and `d × V` at y=182 below it — and her
`COVERS` map gives the three arrangements verbatim:

    d → density = mass ÷ volume
    m → mass = density × volume
    V → volume = mass ÷ density

Her button ORDER is `d, m, V` and she opens with `d` covered, so the
triangle is authored `order: ["left", "top", "right"]`, `covered: "left"`.

⊕ **HER UNIT-PAIRING LINE MOVES DOWN ONE BLOCK.** She sets *"g with cm³
gives g/cm³ · kg with m³ gives kg/m³"* in display type between the result
and the rule; the shared `r_cover_triangle` emits its closing stack in the
fixed order rule → units → condition, so it lands last, in the
`condition` slot — which is the slot's own meaning (*the statement that
makes every question on the page solvable*) and its typography. Ordering
only; every word is hers. Registered.

── ⚖️ THE BENCH HAS A THIRD BRANCH, AND IT IS WATER ──────────────────

Her verdict is `const floats = T.d < 1.00;`, so **water** — one of her six
tabs — falls to the else branch and the bench tells a student that water
dropped in water *sinks*, at *"over 1.00 g/cm³"*, when it is exactly 1.00
and does neither. 5A.1's equal-state rule, and the alveoli defect exactly.
The `same` branch is added and it is the most useful state on the bench:
1.00 is the line the other five materials are read against.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's two marked rungs both put the correct answer at index 0, as do
all eight across P11. **Her option TEXT and every correction are verbatim;
only the ORDER moves.** This lesson takes indices **1 and 3**. Engine
policy, not a register row.

── ⚠️ MRB-177 · ONE DISTRACTOR FINISHED, ON HER SET ──────────────────

Rung 2's correct answer is 31 words against a longest distractor of 15 —
a length tell a student can score without reading. Remedied at the
DISTRACTOR, never at the correct answer and never at the index: her
option C now finishes its own wrong rule ("…so it comes out at the same
number for oak and for gold alike") instead of stopping at "how much you
have". Her correction for it already answers exactly that sentence.
Registered in `DEPARTURES-P11.md`.

── ⚠️ NO CHILDLINE BLOCK. NO DRAFT MARKINGS. ─────────────────────────
"""

LESSON = {
    "slug": "density",
    "title": "Density",
    "discipline": "physics",
    "unit": "Matter and the particle model",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.PHYC.02"],
    "touches": ["KS3.WS.ANA.01", "KS3.WS.MEA.02"],
    "beyond_statutory": False,
    "threads": [{"id": "particles", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 60,

    # ⚠️ EMPTY, AND DESIGN'S PAGE LINKS BACKWARDS TO `p10-05`. That edge
    # crosses into P10, which is a different lane and is not in this tree; a
    # `requires` naming a lesson the registry cannot resolve fails
    # `validate()` with UNKNOWN PREREQUISITE. Authored empty here — the
    # engine's own endmatter then says this is where the unit starts, which
    # is true — and it is one line to add when the lanes merge. Registered.
    "requires": [],
    "assumes": [],
    "references": ["why-ice-floats", "temperature-and-internal-energy",
                   {"unit": "C1", "lesson": "solids-liquids-and-gases",
                    "why": "Where the spacing of the particles in each state "
                           "comes from — this lesson measures what that "
                           "spacing does to a density."}],
    "ks4_links": [],

    "meta_description": "A kilogram of lead and a kilogram of feathers weigh "
                        "the same, and everybody still feels it is wrong. "
                        "What they are reaching for is density.",

    "big_question": "A kilogram of lead and a kilogram of feathers weigh the "
                    "same. Everybody knows that, and everybody still feels it "
                    "is wrong. What they are reaching for is a different "
                    "quantity altogether.",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "Which is heavier",        "done_when": "committed"},
        {"anchor": "s-bench",   "short": "BENCH",
         "label": "The density table",       "done_when": "gate_and_a_control"},
        # ⚠️ MRB-208 — the `s-formula` id goes on the ATTEMPT panel, because
        # Design's own `DONE` for it reads `!!s.cfifaOpen` and her `Cfifa`
        # component fires `onOpen` from the Check button and nowhere else.
        # Same seam as `p7-01`.
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Triangle and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",          "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A block of iron and a block of oak balance exactly.",
        "prompt": "On the pan balance in front of you: a small lump of iron "
                  "on the left, a large block of oak on the right. The beam "
                  "is dead level. The oak is about twelve times the size.",
        "commit": "Which one is heavier?",
        "options": [
            "The iron, because a metal always weighs more than wood",
            "The oak, because there is so much more of it on the pan",
            "They weigh the same, because the balance is level",
            "It depends on the shape of each of the two blocks",
        ],
        "answer": 2,
        "reveal": "They weigh the same — that is what a level balance means. "
                  "What differs is size: it takes about twelve times as much "
                  "oak to match one lump of iron. Heavy is a property of the "
                  "object; density is a property of the material, and it is "
                  "the second one that lets you compare iron with oak at all.",
    },

    "misconceptions": [
        {"id": "PART-14",
         "statement": "Heavy things are dense and light things are not.",
         "elicited_by": "s-hook",
         "confronted_by": "think-heavy-is-not-dense"},
        # ⚠️ NO `elicited_by`, AND THAT IS HONEST RATHER THAN AN OMISSION.
        # Nothing on this page asks a student to commit to why things float:
        # the hook asks which block is heavier and the bench gate asks what
        # halving does to a density. MRB-248 makes absence legal here for
        # exactly this case, and inventing a value would make the register
        # record intent rather than fact.
        {"id": "PART-15",
         "statement": "Things float because they are light and sink because "
                      "they are heavy.",
         "confronted_by": "think-heavy-is-not-dense"},
        {"id": "PART-16",
         "statement": "Cut a block in half and its density halves, because "
                      "there is half as much of it.",
         "elicited_by": "bench",
         "confronted_by": "bench"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Density</strong> is how much mass is packed into a "
                 "given amount of space. It is worked out by dividing the "
                 "mass of a sample by the volume that sample takes up, and it "
                 "is measured in <strong>grams per cubic centimetre</strong> "
                 "(g/cm³) or in <strong>kilograms per cubic metre</strong> "
                 "(kg/m³). Those are the only two pairings you will meet: "
                 "grams go with cubic centimetres and kilograms go with cubic "
                 "metres. There is no such unit as kg/cm³ or g/m³, so if a "
                 "question gives you a mass in one family and a volume in the "
                 "other, converting one of them is the first line of the "
                 "working."},
        {"type": "explainer",
         "text": "The word people usually reach for is <em>heavy</em>, and it "
                 "is the wrong word, because heavy is about a particular "
                 "object. A paving slab is heavy and a chip of the same stone "
                 "is not, and they are the same material at the same density. "
                 "Density is a property of the <strong>material</strong>: "
                 "every cubic centimetre of iron has a mass of 7.87 g whether "
                 "it came from a girder or from a nail."},
        {"type": "explainer",
         "text": "That is why cutting something in half does not change its "
                 "density. You halve the mass, and you halve the volume at "
                 "the same time, and the ratio of one to the other is "
                 "untouched. It is also why density identifies things — "
                 "measure a mass, measure a volume, divide, and the number "
                 "that comes out tells you what the material is."},

        # ── #s-bench · six materials, one balance, one cylinder ────────
        {"type": "matter-bench",
         "id": "bench",
         "anchor": "s-bench",
         "model": "density",
         "eyebrow": "At the bench · six materials, one balance, one "
                    "measuring cylinder",
         "heading": "Same volume, very different masses.",
         # ⚠️ A MAP OF NAMED STATES, NOT A STRING. The shell owns the head
         # row and drives this through `setCountState`; the drawer never
         # reads `progress`, which is what keeps the readout from being
         # printed twice (the live P4/P5/P6 defect).
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Pick a material, choose how big a block of it you want, and "
                 "read the mass off the balance. The bars are the density "
                 "league table — and they do not move when you change the "
                 "volume.",
         "gate": {
             "prompt": "Commit first. You take a 100 cm³ block of aluminium "
                       "and cut it exactly in half. What happens to its "
                       "density?",
             "options": [
                 "It halves, because there is half as much of it",
                 "It doubles, because it is more concentrated now",
                 "It stays at 2.70 g/cm³, because mass and volume both halved",
                 "It cannot be worked out without weighing both halves",
             ],
             "answer": 2,
         },
         "tabs_label": "The material on the balance",
         "start_tab": 3,
         "tabs": [
             {"id": "oak",       "label": "Oak",       "name": "oak",
              "d": "0.65"},
             {"id": "ice",       "label": "Ice",       "name": "ice",
              "d": "0.92"},
             {"id": "water",     "label": "Water",     "name": "water",
              "d": "1.00"},
             {"id": "aluminium", "label": "Aluminium", "name": "aluminium",
              "d": "2.70"},
             {"id": "iron",      "label": "Iron",      "name": "iron",
              "d": "7.87"},
             {"id": "gold",      "label": "Gold",      "name": "gold",
              "d": "19.30"},
         ],
         "slider": {"label": "Volume of the block",
                    "values": [10, 20, 50, 100, 200, 500],
                    "start": 3,
                    "value_label": "{v} cm³"},
         "bars_caption": "Density of each material, to scale against gold",
         "bars_alt": "A bar chart of density for six materials, from oak at "
                     "0.65 grams per cubic centimetre to gold at 19.30, with "
                     "{name} highlighted.",
         # ⚠️ ONE BAR PER TAB, AND THE IDS MATCH — the drawer refuses a
         # mismatch, because the model highlights the selected tab's bar and
         # a mismatch would highlight nothing while the alt text says
         # otherwise.
         "bars": [
             {"id": "oak",       "label": "{label}",
              "value": "{d} g/cm³", "sub": "{mass} g for {v} cm³"},
             {"id": "ice",       "label": "{label}",
              "value": "{d} g/cm³", "sub": "{mass} g for {v} cm³"},
             {"id": "water",     "label": "{label}",
              "value": "{d} g/cm³", "sub": "{mass} g for {v} cm³"},
             {"id": "aluminium", "label": "{label}",
              "value": "{d} g/cm³", "sub": "{mass} g for {v} cm³"},
             {"id": "iron",      "label": "{label}",
              "value": "{d} g/cm³", "sub": "{mass} g for {v} cm³"},
             {"id": "gold",      "label": "{label}",
              "value": "{d} g/cm³", "sub": "{mass} g for {v} cm³"},
         ],
         "readouts": [
             {"id": "vol", "label": "The cylinder says",
              "value": "{v} cm³", "sub": "the space the block takes up"},
             {"id": "mass", "label": "The balance says",
              "value": "{mass_f}", "sub": "mass of that much {name}"},
             {"id": "density", "label": "So the density is",
              "value": "{d} g/cm³", "sub": "{mass} ÷ {v}"},
             {"id": "verdict", "label": "Dropped in water it",
              "value": "{verdict}", "sub": "{verdict_sub}"},
         ],
         # ⚠️ THE VERDICT WORD IS SELECTED FROM THE VALUE, NEVER AUTHORED
         # BESIDE A CONTROL (5A.1) — which is what makes the water case true
         # by construction rather than by somebody remembering.
         "words": {
             "float_verdict": "floats",
             "sink_verdict": "sinks",
             "same_verdict": "stays put",
             "float_sub": "under 1.00 g/cm³",
             "sink_sub": "over 1.00 g/cm³",
             "same_sub": "exactly 1.00 g/cm³",
         },
         "notes": {
             "floats": "A {v} cm³ block of {name} has a mass of {mass_f}, so "
                       "every single cubic centimetre of it carries {d} g. "
                       "Move the volume slider and the mass changes with it — "
                       "but the bar does not move, because the mass and the "
                       "volume change together and their ratio does not. That "
                       "ratio is the density, and it belongs to the material, "
                       "not to the block. At under 1.00 g/cm³ this one "
                       "floats: a cubic centimetre of it is lighter than the "
                       "cubic centimetre of water it would have to push out "
                       "of the way.",
             "sinks": "A {v} cm³ block of {name} has a mass of {mass_f}, so "
                      "every single cubic centimetre of it carries {d} g. "
                      "Move the volume slider and the mass changes with it — "
                      "but the bar does not move, because the mass and the "
                      "volume change together and their ratio does not. That "
                      "ratio is the density, and it belongs to the material, "
                      "not to the block. At over 1.00 g/cm³ this one sinks: a "
                      "cubic centimetre of it is heavier than the cubic "
                      "centimetre of water it would have to push out of the "
                      "way.",
             "same": "A {v} cm³ block of {name} has a mass of {mass_f}, so "
                     "every single cubic centimetre of it carries {d} g. Move "
                     "the volume slider and the mass changes with it — but "
                     "the bar does not move, because the mass and the volume "
                     "change together and their ratio does not. That ratio is "
                     "the density, and it belongs to the material, not to the "
                     "block. At exactly 1.00 g/cm³ this one does neither: a "
                     "cubic centimetre of it weighs exactly as much as the "
                     "cubic centimetre it would have to push out of the way, "
                     "so it stays where you put it. This is the line the "
                     "other five bars are read against.",
         }},

        {"type": "formula",
         "id": "density-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Density = mass ÷ volume",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. The mass m sits above a "
                           "dividing line; the density d and the volume V sit "
                           "below it, multiplied together. Covering one "
                           "letter leaves the way to work it out.",
             "order": ["left", "top", "right"],
             "covered": "left",
             "top":   {"label": "m", "button": "Cover m",
                       "result": "mass = density × volume", "text": ""},
             "left":  {"label": "d", "button": "Cover d",
                       "result": "density = mass ÷ volume", "text": ""},
             "right": {"label": "V", "button": "Cover V",
                       "result": "volume = mass ÷ density", "text": ""},
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["m · mass of the sample · g or kg",
                           "V · volume the sample takes up · cm³ or m³",
                           "d · density of the material · g/cm³ or kg/m³"],
                 "condition": "g with cm³ gives g/cm³ · kg with m³ gives "
                              "kg/m³",
             },
         }},

        {"type": "worked-example", "id": "cfifa-density-plain"},
        {"type": "worked-example", "id": "cfifa-density-convert"},
        {"type": "check", "id": "your-turn-density", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "density-is-mass-over-volume"},

        {"type": "misconception", "id": "think-heavy-is-not-dense",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-density-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A block has a mass of 54 g and a volume of 20 cm³. What "
                    "is its density?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "54 g stays 54 g · 20 cm³ stays 20 cm³",
              "note": "The answer is wanted in g/cm³, and the mass is already "
                      "in grams and the volume already in cubic centimetres, "
                      "so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "density = mass ÷ volume",
              "note": "Cover d on the triangle: m sits over V, so you "
                      "divide."},
             {"letter": "I", "label": "Insert",
              "line": "density = 54 g ÷ 20 cm³",
              "note": "Mass on top, because density is how much mass sits in "
                      "each cubic centimetre."},
             {"letter": "F", "label": "Fine-tune",
              "line": "54 ÷ 20 = 2.7",
              "note": "Grams divided by cubic centimetres leaves grams per "
                      "cubic centimetre."},
             {"letter": "A", "label": "Answer",
              "line": "density = 2.70 g/cm³",
              "note": "Which identifies it: that is aluminium."},
         ]},

        {"id": "cfifa-density-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A block has a mass of 1.2 kg and a volume of 150 cm³. "
                    "What is its density in g/cm³?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1.2 kg × 1000 = 1200 g",
              "note": "A mass in kilograms with a volume in cubic centimetres "
                      "is a mismatched pair — kg/cm³ is not a unit. Bring the "
                      "mass into grams and it pairs with cm³."},
             {"letter": "F", "label": "Formula",
              "line": "density = mass ÷ volume",
              "note": "Cover d on the triangle: m sits over V, so you "
                      "divide."},
             {"letter": "I", "label": "Insert",
              "line": "density = 1200 g ÷ 150 cm³",
              "note": "The converted mass goes in. The 1.2 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "1200 ÷ 150 = 8",
              "note": "Grams divided by cubic centimetres leaves grams per "
                      "cubic centimetre."},
             {"letter": "A", "label": "Answer",
              "line": "density = 8.00 g/cm³",
              "note": "Insert 1.2 instead of 1200 and the answer comes out "
                      "0.008 g/cm³ — light enough to float on a puddle."},
         ]},

        {"id": "your-turn-density",
         "kind": "p11-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "check_label": "Check your working",
         "reveal_label": "The five lines · tick what you had",
         # The bench's opening state: tab 3 is aluminium at 2.70 g/cm³ and
         # the slider rests at 100 cm³, so the mass is 270.0 g. These are the
         # bytes a crawler and a JavaScript-off reader get; `data-template`
         # beside them is what the wiring refills from live state.
         "rest": {"mass": "270.0", "mass_f": "270.0 g", "v": "100",
                  "name": "aluminium", "d": "2.70"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your block: {mass} g of {name}, taking up {v} cm³.",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{mass} g stays {mass} g · {v} cm³ stays {v} cm³",
                   "note": "The balance reads grams and the cylinder reads "
                           "cubic centimetres, which is what g/cm³ needs, so "
                           "there is nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "density = mass ÷ volume",
                   "note": "Cover d on the triangle: m sits over V, so you "
                           "divide."},
                  {"letter": "I", "label": "Insert",
                   "line": "density = {mass} g ÷ {v} cm³",
                   "note": "Mass on top. Both readings come from the same "
                           "block."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{mass} ÷ {v} = {d}",
                   "note": "Grams divided by cubic centimetres leaves grams "
                           "per cubic centimetre."},
                  {"letter": "A", "label": "Answer",
                   "line": "density = {d} g/cm³",
                   "note": "Change the volume slider and this line does not "
                           "change. That is the whole point of a density."},
              ],
              "close": "The five lines give {d} g/cm³ — the bar for {name} on "
                       "the chart above."},
             {"id": "q2", "tab": "Question 2",
              "head": "A steel bolt has a mass of 0.039 kg and a volume of "
                      "5.0 cm³. What is its density in g/cm³?",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "0.039 kg × 1000 = 39 g",
                   "note": "Kilograms with cubic centimetres is a mismatched "
                           "pair. Grams go with cm³, kilograms go with m³ — "
                           "pick one family and stay in it."},
                  {"letter": "F", "label": "Formula",
                   "line": "density = mass ÷ volume",
                   "note": "Cover d on the triangle: m sits over V, so you "
                           "divide."},
                  {"letter": "I", "label": "Insert",
                   "line": "density = 39 g ÷ 5.0 cm³",
                   "note": "The converted mass goes in. The 0.039 never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "39 ÷ 5.0 = 7.8",
                   "note": "Grams divided by cubic centimetres leaves grams "
                           "per cubic centimetre."},
                  {"letter": "A", "label": "Answer",
                   "line": "density = 7.80 g/cm³",
                   "note": "Insert 0.039 instead of 39 and the bolt comes out "
                           "less dense than air."},
              ],
              "close": "The five lines give 7.80 g/cm³ — steel, near the iron "
                       "bar on the chart. The whole question turned on the "
                       "first one."},
         ]},

        # ⚠️ PLAIN `predict`, as everywhere else in the key stage. `#s-think`
        # is NOT a rail stop on this page — Design's third stop is the CFIFA
        # block — so the section needs no completion contract of its own.
        {"id": "think-heavy-is-not-dense",
         "kind": "predict",
         "demand": "explain",
         "targets": "PART-14",
         "statements": [
             {"quote": "Heavy things are dense and light things are not.",
              "targets": "PART-14",
              "body": [
                  "Heavy is about the object; dense is about the material. A "
                  "polystyrene packing block the size of a fridge is awkward "
                  "to carry and has a density of about 0.02 g/cm³ — a "
                  "fiftieth that of water. A gold ring is light enough to "
                  "forget you are wearing and has a density of 19.30. The two "
                  "words answer different questions, and only one of them "
                  "survives cutting the object up.",
              ]},
             {"quote": "Things float because they are light and sink because "
                       "they are heavy.",
              "targets": "PART-15",
              "body": [
                  "An oil tanker floats and a 5p coin sinks. What decides it "
                  "is not the weight but how that weight compares with the "
                  "weight of the water pushed out of the way — a comparison "
                  "of densities, not of masses. Below 1.00 g/cm³ a thing "
                  "floats on water however large it is; above, it sinks "
                  "however small. It is also why the same coin sinks in water "
                  "and floats in mercury, which has a density of 13.5.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "density-is-mass-over-volume",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Density is mass ÷ volume. The units come in matched pairs — "
                 "grams with cubic centimetres gives g/cm³, kilograms with "
                 "cubic metres gives kg/m³ — and there is no such unit as "
                 "kg/cm³ or g/m³, so a mismatched pair must be converted "
                 "before you divide. Density belongs to the material, not the "
                 "object: cut a block in half and both halves have the same "
                 "density. Anything below 1.00 g/cm³, or 1000 kg/m³, floats "
                 "on water."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 1 and 3.
    # Design put both at 0; her option TEXT and every correction are verbatim
    # and only the ORDER moves.
    "ladder": {
        "recall": {
            "q": "A stone has a mass of 240 g and displaces 80 cm³ of water. "
                 "What is its density?",
            "options": [
                "19 200 g/cm³ — multiply the two",
                "3.0 g/cm³",
                "0.33 g/cm³ — divide the volume by the mass",
                "3.0 g — the stone is what you weighed",
            ],
            "answer": 1,
            "feedback": {
                0: "Multiplying mass by volume gives a number with no "
                   "meaning. Cover d on the triangle and m sits over V, so "
                   "you divide.",
                2: "That is the division upside down. Density is how much "
                   "mass sits in each cubic centimetre, so the mass goes on "
                   "top.",
                3: "The number is right and the unit is wrong. Grams divided "
                   "by cubic centimetres leaves grams per cubic centimetre.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A student says a 2 kg block of oak must be denser than a "
                 "50 g lump of gold, because the oak is forty times heavier. "
                 "What is right?",
            "options": [
                "The student is right, because a bigger mass always means a "
                "bigger density.",
                # ⚠️ MRB-177 — Design's distractor, FINISHED. Her correct
                # option is 31 words against a longest distractor of 15, a
                # tell at the ≥4-word threshold. Remedied here, at the
                # distractor, and the added clause states the wrong rule
                # completely rather than padding it — her own correction for
                # this option already answers exactly this sentence.
                "They have the same density, because density does not depend "
                "on how much you have, so it comes out at the same number for "
                "oak and for gold alike.",
                "The oak is denser, but only because wood contains water.",
                "The gold is far denser. Heavier says how much there is; "
                "denser says how much mass sits in each cubic centimetre, and "
                "only the second is a property of the material.",
            ],
            "answer": 3,
            "feedback": {
                0: "Mass on its own says nothing about density — you also "
                   "need the volume. That 2 kg of oak takes up about "
                   "3000 cm³; the gold takes up under 3.",
                1: "Density does not depend on how much you have, which is "
                   "true — but oak and gold are different materials, so their "
                   "densities are different numbers.",
                2: "The verdict is wrong and so is the reason. Even soaking "
                   "wet, oak stays under about 1.1 g/cm³; gold is 19.30.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Describe how you would find the density of a small "
                 "irregular stone using a balance, a measuring cylinder and "
                 "water, and say why the cylinder is needed at all.",
            "field_label": "Your method",
            "placeholder": "First put the stone on the balance and…",
            "success": [
                "Finds the mass of the dry stone on the balance first, in "
                "grams.",
                "Part-fills the measuring cylinder with water and records the "
                "reading.",
                "Lowers the stone in fully and records the new reading.",
                "Takes the difference between the two readings as the volume "
                "in cm³.",
                "Divides mass by volume and gives the unit as g/cm³, "
                "explaining that a density needs both a mass and a volume.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A steel ship floats even though steel has a density of "
                 "about 7.9 g/cm³. A solid steel bar of the same mass sinks. "
                 "Explain the difference using density, and predict what "
                 "happens if the hull fills with water.",
            "field_label": "Your answer",
            "placeholder": "The ship is not solid steel, so…",
            "success": [
                "Says the ship is mostly air, not solid steel.",
                "Says the density that matters is the mass of the whole ship "
                "divided by the whole volume it takes up, hull and air "
                "together.",
                "Says that average density comes out below 1.00 g/cm³, so it "
                "floats.",
                "Says the solid bar has the same mass in a far smaller "
                "volume, so its density stays at 7.9 g/cm³ and it sinks.",
                "Predicts that water filling the hull replaces the air, "
                "pushing the average density above 1.00 g/cm³, and the ship "
                "sinks.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Density is mass divided by volume, measured in g/cm³ or in "
                "kg/m³ — 1.00 g/cm³ is the same density as 1000 kg/m³. The "
                "two units in the pair must match: grams go with cubic "
                "centimetres and kilograms with cubic metres, and if the "
                "question hands you one of each, converting is the first "
                "thing you do. Density is a property of the material rather "
                "than of the object, so a block and a chip of the same "
                "substance share it, and cutting something in half changes "
                "neither. Finding a density means two measurements and one "
                "division: a mass from a balance, and a volume from a "
                "cylinder or from displacement. Below 1.00 g/cm³ a material "
                "floats on water; above it, it sinks.",

    "stretch": [
        {"id": "what-sets-a-density",
         "type": "explainer",
         "text": "The numbers vary so widely because they are set by two "
                 "things at once: how heavy the individual atoms are, and how "
                 "tightly the structure packs them. Osmium, the densest "
                 "element at 22.6 g/cm³, wins on both counts — heavy atoms in "
                 "a tight hexagonal arrangement. Lithium, at 0.53, has light "
                 "atoms in a loose one, and would float on water if it did "
                 "not react with it violently first."},
        {"id": "archimedes-and-the-crown",
         "type": "explainer",
         "text": "Archimedes is supposed to have solved a density problem in "
                 "the bath and gone straight out into the streets of Syracuse "
                 "to announce it. The story is almost certainly invented; the "
                 "physics underneath it is not. A crown of pure gold and a "
                 "crown of gold mixed with silver have the same mass and "
                 "different volumes, so measuring the volume by displacement "
                 "settles the question without damaging the crown. Every "
                 "hydrometer in a brewery and every battery tester in a "
                 "garage is still doing the same trick."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "density",
         "definition": "How much mass is packed into a given amount of space: "
                       "the mass of a sample divided by its volume, in g/cm³ "
                       "or kg/m³. It belongs to the material, not to the "
                       "object."},
        {"term": "mass",
         "definition": "How much matter something is made of, measured on a "
                       "balance in grams or kilograms. It is a property of "
                       "the particular object."},
        {"term": "volume",
         "definition": "The amount of space something takes up, in cm³ or m³. "
                       "For an irregular solid it is found by displacement — "
                       "the rise in the water it is lowered into."},
        {"term": "displacement",
         "definition": "Measuring a volume by how much water an object pushes "
                       "out of the way. The difference between the two "
                       "cylinder readings is the object's volume."},
    ],

    "tutor": {
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a mass and a volume and want the density?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Density in kg/m³, the required practical for regular and "
                   "irregular solids and for liquids, and density as the link "
                   "between particle spacing and state of matter.",

    # ⚖️ MRB-297 · Mide's wording, approved 30 Aug 2026. Not to be edited.
    "safety_note": "Eye protection on. Wipe up spilled water straight away — "
                   "a wet floor is the real hazard here. Measuring cylinders "
                   "tip easily, so keep them back from the edge of the bench.",

    "convention_note": "The bench is a teaching model. Densities are quoted "
                       "at room temperature and ordinary pressure to two "
                       "decimal places: oak 0.65, ice 0.92, water 1.00, "
                       "aluminium 2.70, iron 7.87 and gold 19.30 g/cm³. Real "
                       "timber varies widely with species and moisture "
                       "content, and the figure for oak is a typical seasoned "
                       "value rather than a measurement of a particular "
                       "piece. Masses shown are calculated from the quoted "
                       "density and the chosen volume, and are rounded to one "
                       "decimal place.",

    "ws": ["measurement", "analysis-and-evaluation"],
}
