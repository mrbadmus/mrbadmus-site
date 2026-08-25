"""P11 L4 — Why ice floats (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p11/p11-04-why-ice-floats.dc.html`.

Her page wins outright. The glass of ice cubes, the four substances
weighed as a solid and as their own melt, the comparison line at 1.00 and
all four rungs are hers, ported from her JavaScript constants rather than
from her HTML.

── ⚖️ THE CONTRAST IS THE INSTRUMENT, AND THREE OF THE FOUR AGREE ────

Candle wax, aluminium and iron all pack closer on freezing; water does the
opposite. The bench's whole argument is that the exception is ONE tab out
of four, so `r_matter_bench` refuses an `ice` payload where any substance
has the same density in both states — a tie would fall to whichever branch
was written second and say something false.

── ⚖️ "ABOUT A NINTH ABOVE THE SURFACE" IS THE SEAWATER FIGURE ───────

Her closing note says a floating lump of ice sits *"with about a ninth of
it above the surface"*. A ninth is about 11%, and it is the figure for ice
in SEAWATER (density about 1.025). This page is about fresh water at 1.00,
where the fraction above is `1 − 0.92 ÷ 1.00` = 8% — which is what her own
rung 1 marks correct (*"About 8%"*) and what her own Think-again says
(*"about 92% of itself below the surface"*). Two sentences on one page
against one, and the two are the ones a student is marked on.

The figure is now DERIVED from the two densities in the payload rather
than typed, so it is 8% here and would move with them. Registered.

── ⚖️ `#s-think` IS THE THIRD RAIL STOP ──────────────────────────────

Design's `DONE` reads `s.answers.r1 !== null || s.hookChoice !== null`.
See the package note.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's two marked rungs both put the correct answer at index 0. **Her
option TEXT and every correction are verbatim; only the ORDER moves.**
This lesson takes indices **2 and 0**.

── ⚠️ MRB-177 · TWO DISTRACTORS FINISHED, ON HER SETS ────────────────

Both marked rungs are length tells (17w against 10w; 31w against 14w).
Remedied at the DISTRACTOR both times, and in both cases her own
correction already answers the finished sentence. Registered.

── ⚠️ NO CHILDLINE BLOCK. NO DRAFT MARKINGS. ─────────────────────────
"""

LESSON = {
    "slug": "why-ice-floats",
    "title": "Why ice floats",
    "discipline": "physics",
    "unit": "Matter and the particle model",
    "family": "CONTRAST",

    "covers": ["KS3.P.PMOD.01"],
    "touches": ["KS3.WS.ANA.04"],
    "beyond_statutory": False,
    "threads": [{"id": "particles", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["temperature-and-internal-energy"],
    "assumes": ["density"],
    "references": ["density",
                   {"unit": "C1", "lesson": "changes-of-state",
                    "why": "What melting and freezing do to the arrangement "
                           "of the particles — this lesson measures what that "
                           "does to a density."},
                   {"unit": "C1", "lesson": "solids-liquids-and-gases",
                    "why": "The general rule this lesson finds the exception "
                           "to."}],
    "ks4_links": [],

    "meta_description": "Solids sink in their own melt. Water does not — and "
                        "if it did, ponds would freeze from the bottom up and "
                        "take everything in them with it.",

    "big_question": "Solids sink in their own melt. Iron does, wax does, "
                    "aluminium does. Water does not — and if it did, ponds "
                    "would freeze from the bottom and take everything in them "
                    "with it.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Ice cubes on top", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Solid against liquid", "done_when": "gate_and_a_control"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Water is the odd one", "done_when": "hook_or_first_rung"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Every ice cube in the glass is sitting on top.",
        "prompt": "A glass of water with four ice cubes in it. All four "
                  "float, most of each cube under the surface, a small dome "
                  "above. The cubes were made from that same water.",
        "commit": "Why does the ice float on the water it came from?",
        "options": [
            "Ice is lighter than water, because it is frozen",
            "Ice is less dense than the water it came from",
            "The ice is held up by bubbles trapped in it",
            "Cold things always float on warm things",
        ],
        "answer": 1,
        "reveal": "Less dense than the water it came from — and that is a "
                  "genuinely strange thing for a solid to be. Freeze almost "
                  "anything else and the solid sinks in its own melt, because "
                  "cooling packs particles closer together. Water does the "
                  "opposite: as it freezes, each molecule is locked into an "
                  "open hexagonal cage that holds its neighbours further "
                  "apart than they were in the liquid. The ice expands by "
                  "about 9%, its density drops to 0.92 g/cm³, and it floats.",
    },

    "misconceptions": [
        {"id": "PART-20",
         "statement": "Ice floats because it is lighter than water.",
         "elicited_by": "s-hook",
         "confronted_by": "think-water-is-the-odd-one"},
        {"id": "PART-21",
         "statement": "Water expands when it freezes, so it must expand when "
                      "it is heated too.",
         "confronted_by": "think-water-is-the-odd-one"},
        {"id": "PART-22",
         "statement": "Cold things float on warm things — it is being cold "
                      "that makes ice sit on top.",
         "elicited_by": "s-hook",
         "confronted_by": "s-ladder"},
        # ⊕ RE-CONFRONTED, NOT RE-MINTED. `PART-03` was opened by C1's
        # `solids-liquids-and-gases` and the register predicts it resurfacing
        # in P11. This is the page where it is genuinely live — a student
        # explaining a 9% expansion reaches for "the molecules got bigger" —
        # and rung 3's own success criteria are what take it apart: the
        # expansion is BIGGER GAPS, and the mass has not changed.
        {"id": "PART-03",
         "statement": "The particles themselves change — they melt, or get "
                      "softer, or expand — when a substance changes state.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Cooling a substance normally makes it denser. The particles "
                 "slow down, they no longer need as much room to move about "
                 "in, and they settle closer together — so the same mass "
                 "occupies less volume. Freeze it and it contracts again as "
                 "the particles lock into a tight regular pattern. A lump of "
                 "the solid dropped into its own melt sinks."},
        {"type": "explainer",
         "text": "<strong>Water breaks this rule.</strong> Liquid water is at "
                 "its densest at about 4 °C. Cool it further and it starts to "
                 "<em>expand</em>, and at 0 °C, as it freezes, it expands "
                 "sharply — by roughly 9%. The mass has not changed, so the "
                 "density falls from 1.00 g/cm³ to 0.92, and the ice floats."},
        {"type": "explainer",
         "text": "The cause is the shape of the water molecule and the way it "
                 "bonds. Each molecule can hold hands with four others at "
                 "fixed angles, and in the solid those bonds lock into an "
                 "open hexagonal cage with a gap in the middle. In the liquid "
                 "the same molecules jostle and slip past one another and, on "
                 "average, sit closer together than the cage allows. Freezing "
                 "water builds the cage, and the cage takes up more room."},

        # ── #s-bench · four substances, solid and liquid ───────────────
        {"type": "matter-bench",
         "id": "bench",
         "anchor": "s-bench",
         "model": "ice",
         "eyebrow": "At the bench · four substances, each weighed as a solid "
                    "and as its own melt",
         "heading": "Solid on the left, its own liquid on the right.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Pick a substance and switch between its solid and its "
                 "liquid. Watch which of the two bars is longer — and notice "
                 "that one substance out of the four disagrees with the other "
                 "three.",
         "gate": {
             "prompt": "Commit first. Molten iron is poured, and a lump of "
                       "solid iron is dropped into it. What happens to the "
                       "lump?",
             "options": [
                 "It floats, the way ice floats on water",
                 "It sinks, because the solid is denser than the melt",
                 "It stays where it is put, because both are iron",
                 "It dissolves instantly",
             ],
             "answer": 1,
         },
         "tabs_label": "The substance",
         "start_tab": 0,
         "tabs": [
             {"id": "water", "label": "Water", "name": "water",
              "solid": "0.92", "liquid": "1.00", "mp": "0 °C"},
             {"id": "wax", "label": "Candle wax", "name": "candle wax",
              "solid": "0.93", "liquid": "0.90", "mp": "about 60 °C"},
             {"id": "aluminium", "label": "Aluminium", "name": "aluminium",
              "solid": "2.70", "liquid": "2.38", "mp": "660 °C"},
             {"id": "iron", "label": "Iron", "name": "iron",
              "solid": "7.87", "liquid": "6.98", "mp": "1538 °C"},
         ],
         # ⚠️ A TWO-POSITION SLIDER, AND ITS VALUES ARE WORDS. Design's
         # `SLIDER = ['solid', 'liquid']` and her value label prints the word
         # itself. The bar ids match the two positions, which is what lets
         # the model put the focus ring on the state actually on the balance.
         "slider": {"label": "State on the balance",
                    "values": ["solid", "liquid"],
                    "start": 0,
                    "value_label": "{sv}"},
         "bars_caption": "Density as a solid and as a liquid, compared within "
                         "each substance",
         "bars_alt": "Three density bars for {name}: solid {solid}, liquid "
                     "{liquid}, and liquid water at 1.00 grams per cubic "
                     "centimetre.",
         "bars": [
             {"id": "solid", "label": "As a solid",
              "value": "{solid} g/cm³",
              "sub": "below its melting point of {mp}"},
             {"id": "liquid", "label": "As its own liquid",
              "value": "{liquid} g/cm³",
              "sub": "just above the same melting point"},
             {"id": "water", "label": "Liquid water, for comparison",
              "value": "1.00 g/cm³",
              "sub": "the line everything is judged against for floating in "
                     "a pond",
              "muted": True},
         ],
         "readouts": [
             {"id": "sample", "label": "On the balance",
              "value": "{name}, {sv}", "sub": "melting point {mp}"},
             {"id": "density", "label": "Density",
              "value": "{cur} g/cm³", "sub": "mass in every cubic centimetre"},
             {"id": "change", "label": "Freezing changes the density by",
              "value": "{change}", "sub": "{direction}"},
             {"id": "verdict", "label": "Solid on its own melt",
              "value": "{verdict}", "sub": "{verdict_sub}"},
         ],
         "words": {
             "float_verdict": "floats",
             "sink_verdict": "sinks",
             "float_sub": "solid is the lighter of the two",
             "sink_sub": "solid is the heavier of the two",
             "expands": "density falls, so the solid expands",
             "contracts": "density rises, so the solid contracts",
         },
         "notes": {
             "odd": "Water is the exception on this bench. Freezing it makes "
                    "it {change_abs}% less dense rather than more, because "
                    "each molecule in ice is locked into an open hexagonal "
                    "cage that holds its neighbours further apart than "
                    "jostling in the liquid did. The solid ends up at {solid} "
                    "g/cm³ against {liquid} for the liquid, so it floats — "
                    "with about {above}% of it above the surface and the rest "
                    "below.",
             "ordinary": "This is the ordinary case. Freezing {name} packs "
                         "the particles closer, so the solid at {solid} g/cm³ "
                         "is denser than the liquid at {liquid} and a lump of "
                         "it sinks straight to the bottom of its own melt. "
                         "Switch to water and the two bars swap over, which "
                         "is the whole point of this page.",
         }},

        {"type": "key-fact", "ref": "ice-is-the-exception"},

        {"type": "misconception", "id": "think-water-is-the-odd-one",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-water-is-the-odd-one",
         "kind": "matter-think",
         "demand": "explain",
         "targets": "PART-20",
         "ticks_when": "The hook is committed, or ladder rung 1 is answered "
                       "— Design's own predicate for this stop, and neither "
                       "control is inside this section.",
         "statements": [
             {"quote": "Ice floats because it is lighter than water.",
              "targets": "PART-20",
              "body": [
                  "A block of ice the size of a car is far heavier than a "
                  "teaspoon of water and it still floats. What matters is not "
                  "the weight of the object but its density against the "
                  "density of the water it has to push aside. Ice is "
                  "0.92 g/cm³ against water’s 1.00, so any lump of ice of any "
                  "size floats — and it sits with about 92% of itself below "
                  "the surface, which is where the phrase “tip of the "
                  "iceberg” comes from.",
              ]},
             {"quote": "Water expands when it freezes, so it must expand when "
                       "it is heated too.",
              "targets": "PART-21",
              "body": [
                  "It does, above 4 °C — and between 0 °C and 4 °C it does "
                  "the opposite, contracting as it warms. That narrow band is "
                  "called the anomalous expansion of water, and it is why the "
                  "densest water in a pond sits at 4 °C at the bottom, with "
                  "colder water above it and ice on top. Everything about how "
                  "a pond freezes, and about what survives the winter in it, "
                  "follows from those four degrees.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "ice-is-the-exception",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Almost every substance is denser as a solid than as its own "
                 "liquid, so the solid sinks in the melt. Water is the "
                 "exception: freezing expands it by about 9%, so ice at "
                 "0.92 g/cm³ floats on water at 1.00 — which is why ponds "
                 "freeze from the top down."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 0.
    "ladder": {
        "recall": {
            "q": "Ice has a density of 0.92 g/cm³ and liquid water "
                 "1.00 g/cm³. What fraction of a floating iceberg is above "
                 "the surface?",
            "options": [
                # ⚠️ MRB-177 — Design's distractor, FINISHED. Her correct
                # option is 17 words against a longest distractor of 10.
                # Remedied at the distractor; the added clause states the
                # wrong rule completely and her own correction answers it.
                "About 92%, because ice is 0.92 as dense as water, so 92% of "
                "it shows above the surface.",
                "Half, because floating means half in and half out.",
                "About 8% — the ratio 0.92 to 1.00 means roughly 92% of it "
                "sits below the waterline.",
                "None of it — ice floats level with the surface.",
            ],
            "answer": 2,
            "feedback": {
                0: "The 0.92 is the fraction submerged, not the fraction "
                   "showing. A floating object sinks until it has pushed "
                   "aside its own weight of water.",
                1: "Floating means the weight of water pushed aside equals "
                   "the object’s weight. How much sticks out depends on the "
                   "two densities.",
                3: "Something less dense than water must stick out, or it "
                   "would be pushing aside more water than its own weight.",
            },
            "title": "Rung 1 · Read the comparison"},
        "apply": {
            "q": "A student says ice floats because it is cold, and cold "
                 "things float. What is wrong?",
            "options": [
                "Temperature is not what decides floating — density is. Cold "
                "liquid water sinks below warmer water, and it is only the "
                "change of structure on freezing that makes ice less dense.",
                "Nothing is wrong — cold things are always less dense.",
                # ⚠️ MRB-177 — finished, for the same reason. Her correction
                # names the paper clip, so the finished distractor is the
                # sentence that correction was written against.
                "Ice does not float; it is held up by the surface of the "
                "water, in the same way that surface holds up a paper clip "
                "laid flat on it.",
                "Ice floats because air is trapped inside it as it freezes.",
            ],
            "answer": 0,
            "feedback": {
                1: "Cooling normally makes things denser, not less dense. "
                   "That is why cold water sinks in a pond and why almost "
                   "every other solid sinks in its own melt.",
                2: "Ice genuinely floats, with about 92% of it submerged. "
                   "Surface tension holds up a paper clip, not an iceberg.",
                3: "Bubbles help a little in real pond ice, and pure "
                   "bubble-free ice still floats. The reason is the open "
                   "crystal structure, not the air.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why a bottle of water left in the freezer can "
                 "split, and why the same bottle full of cooking oil does "
                 "not.",
            "field_label": "Your explanation",
            "placeholder": "When the water freezes, the molecules…",
            "success": [
                "Says water expands by about 9% when it freezes.",
                "Says the expansion happens because the molecules lock into "
                "an open structure with bigger gaps.",
                "Says the bottle is a fixed volume, so the ice pushes "
                "outwards with enough force to split it.",
                "Says the mass has not changed — only the volume, and so the "
                "density.",
                "Says oil contracts on freezing like most substances, so it "
                "takes up less room rather than more.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Explain why a pond freezes from the top down, and what "
                 "would happen to life in it if ice were denser than water.",
            "field_label": "Your answer",
            "placeholder": "The ice forms at the surface and stays there "
                           "because…",
            "success": [
                "Says ice forms at the surface, where the water is losing "
                "energy to the cold air.",
                "Says the ice is less dense than the water, so it stays on "
                "top instead of sinking.",
                "Says the layer of ice then insulates the water underneath, "
                "slowing further freezing.",
                "Says fish and plants survive in liquid water below the ice.",
                "Says that if ice were denser it would sink, fresh water "
                "would freeze at the surface again, and the pond would freeze "
                "solid from the bottom up, killing what lives in it.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "When almost any substance freezes, its particles pack closer "
                "together, the solid is denser than the liquid, and a lump of "
                "the solid sinks in its own melt. Water is the exception. Its "
                "molecules lock into an open hexagonal structure on freezing, "
                "so it expands by about 9%: ice is 0.92 g/cm³ against liquid "
                "water’s 1.00, and it floats with roughly 92% of its volume "
                "below the surface. This is why a pond freezes from the top "
                "down, why the ice layer insulates the water beneath it, and "
                "why life in fresh water survives a winter at all.",

    "stretch": [
        {"id": "freeze-thaw",
         "type": "explainer",
         "text": "The expansion is powerful enough to be a geological force. "
                 "Water that seeps into a crack in a rock and freezes pushes "
                 "outwards with a pressure of tens of megapascals — far more "
                 "than the rock can take — and the crack widens a little "
                 "every time it thaws and refreezes. Repeated over enough "
                 "winters this is freeze–thaw weathering, and it is a major "
                 "reason mountain roads need resurfacing and mountains "
                 "themselves fall apart."},
        {"id": "cells-and-pipes",
         "type": "explainer",
         "text": "The same property runs through biology and engineering. "
                 "Cells burst when frozen because the water in them expands, "
                 "which is why frozen fruit goes soft and why organs for "
                 "transplant cannot simply be put in a freezer. Water pipes "
                 "split for the same reason, and always at the weakest point "
                 "rather than where the ice formed. Cryobiologists get round "
                 "it with antifreeze compounds that stop the hexagonal cage "
                 "forming in the first place."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "anomalous expansion",
         "definition": "Water's odd behaviour between 0 °C and 4 °C, where "
                       "cooling makes it expand instead of contract. It is "
                       "why the densest water in a pond sits at 4 °C at the "
                       "bottom."},
        {"term": "melting point",
         "definition": "The temperature at which a substance changes between "
                       "solid and liquid. The two densities on this bench are "
                       "measured just below it and just above it."},
        {"term": "hexagonal structure",
         "definition": "The open six-sided cage water molecules lock into as "
                       "they freeze, with a gap in the middle. It holds them "
                       "further apart than they sat in the liquid."},
        {"term": "freeze–thaw weathering",
         "definition": "Rock broken apart by water that seeps into a crack, "
                       "freezes, expands and widens it — a little more every "
                       "winter."},
    ],

    "tutor": {
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to know why water is the one that breaks the rule?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Density changes at changes of state, the particle model "
                   "of solids and liquids, and hydrogen bonding as the reason "
                   "water behaves unlike other small molecules.",

    "convention_note": "The bench is a teaching model. Densities are quoted "
                       "just below and just above each substance’s melting "
                       "point, to two decimal places: water 0.92 solid and "
                       "1.00 liquid; candle wax about 0.93 and 0.90; "
                       "aluminium 2.70 and 2.38; iron 7.87 and 6.98 g/cm³. "
                       "Candle wax is a mixture rather than a single compound "
                       "and its figures vary between blends. The 1.00 g/cm³ "
                       "comparison line is liquid water at 4 °C. Percentage "
                       "changes, and the fraction of a floating lump above "
                       "the surface, are calculated from the quoted pairs.",

    "ws": ["analysis-and-evaluation"],
}
