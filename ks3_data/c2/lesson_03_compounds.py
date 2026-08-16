"""C2 L3 — Compounds (CONTRAST).

Authored against Design's approved page,
`docs/ks3/design-reference/c2/c2-03-compounds.dc.html` (771 lines), and its
measured specification, `docs/ks3/c2-inventory/PAYLOAD-MAP.md` §4.

Every student-facing string is byte-identical to the approved page. `RAIL`,
`TESTS`, `SORT`, `RUNGS` and `SELF_RUNGS` came out of the node extractor; the
gate options, the state and ratio labels, both dish captions, both alt texts,
the two verdict words and the two progress formats were lifted from the line
ranges the payload map records.

── The proportion control is the lesson ────────────────────────────────

Three proportions in the mixture, each of which changes the drawing; heat it
and the control REFUSES. NOTES §3.3: the disable "is itself the lesson" — a
compound's proportion is not adjustable. It is enforced on the button, in the
handler and in the drawing, and it is the single thing about this instrument
that must not be softened for tidiness.

The CONTRAST family's pattern holds and is authored as data: the vivid tests
(the look, and even the glow) settle nothing, and the quiet one — weigh what
actually combines — settles everything. `settles` per test picks the verdict
word, so the pattern is legible in the record rather than only in the prose.

⚑ For Mide's science gate, from Design's NOTES:
  * flag 7 — iron sulfide 7 g : 4 g (Fe:S = 56:32 = 7:4 exactly), the reaction
    exothermic and self-sustaining, and the safety line at the foot of the page.
  * flag 8 — the drawn lattice. Iron(II) sulfide is a 1:1 giant structure and
    the diagram is a fair KS3 picture; it is not molecules. This is the single
    visual in the unit Design most wants an examiner's eye on.
  * flag 9 — steel as a mixture (sort item 3). Alloys are mixtures at KS3.
  * flag 10 — the hydrogen/oxygen stretch, and the phrase "same ratio by atoms".
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 169 character for character.
    "slug":        "compounds",
    "title":       "Compounds",
    "discipline":  "chemistry",
    "unit":        "atoms-elements-and-compounds",
    "family":      "CONTRAST",

    # ── curriculum position ─────────────────────────────────────────────────
    "covers":      ["KS3.C.AEC.02b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 2},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    "requires":    ["elements"],
    "assumes":     [],
    "references":  ["chemical-symbols"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Iron and sulfur in a dish. Same two elements before and "
                    "after heating — and afterwards the magnet is useless. "
                    "What changed?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",  "label": "The magnet stops",
         "done_when": "committed"},
        {"anchor": "s-bench", "short": "BENCH",
         "label": "Four tests, two states", "done_when": "all_tests_seen"},
        {"anchor": "s-sort",  "short": "SORT",  "label": "Four substances",
         "done_when": "all_items_decided"},
        {"anchor": "s-think", "short": "THINK", "label": "Still in there",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "The magnet worked five minutes ago.",
        "prompt": "Grey iron filings and yellow sulfur powder, stirred "
                  "together. Hold a magnet over the dish and the iron jumps "
                  "out of it. Stir it back in, heat one corner until it glows, "
                  "and the glow spreads by itself through the whole dish. What "
                  "is left is a dull grey-black solid — and the magnet now "
                  "does nothing at all.",
        "commit": "Where has the iron gone?",
        "options": [
            "It melted and ran to the bottom of the dish",
            "It joined with the sulfur to make a different substance",
            "The sulfur has coated each piece of iron",
            "It burnt away and left the sulfur behind",
        ],
        "reveal": "Every iron atom is still in the dish; not one has been "
                  "lost. They are now joined to sulfur atoms, and the "
                  "substance they are part of is not iron. It has its own "
                  "properties, and being magnetic is not one of them.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    "misconceptions": [
        {"id": "ATOM-06",
         "statement": "A compound is a very thoroughly mixed mixture.",
         "elicited_by": "iron-and-sulfur",
         "confronted_by": "iron-and-sulfur"},
        {"id": "ATOM-07",
         "statement": "The iron is still in there, so it must still be "
                      "magnetic — the sulfur is just covering it up.",
         "elicited_by": "think-commit-magnet",
         "confronted_by": "think-commit-magnet"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Mixing changes nothing about the substances — it just puts "
                 "them in the same place. A chemical reaction joins their "
                 "atoms together, and what comes out is a new substance: a "
                 "<strong>compound</strong>."},

        # #s-bench — the flagship. Ink-dark practical, one canvas.
        {"type": "mixture-compound-dish", "id": "iron-and-sulfur",
         "anchor": "s-bench",
         "eyebrow": "At the bench · the same two elements, twice",
         "heading": "Test the mixture. Heat it. Test it again.",
         "head_counter": {"format": "{n} of 4 tests run", "total": 4,
                          "start": 1},
         "demand": "investigate",
         "targets": "ATOM-06",
         "prompt": "Four tests, two states. Three of the four give an "
                   "interesting answer in both states, and only one of them "
                   "settles anything.",
         "gate": {"prompt": "Commit first. In the mixture you can use any "
                            "amounts you like. What about after heating?",
                  "options": [
                      "Any amounts still work — it is the same two elements",
                      "Only one exact proportion joins up; anything extra is "
                      "left over",
                      "The proportion changes depending on how hot it gets",
                      "Half of each always reacts",
                  ]},
         "labels": {"dish": "The dish", "ratio": "How much of each",
                    "before": "Before heating", "after": "After heating"},
         "states": [
             {"heated": False, "label": "Stirred together"},
             {"heated": True, "label": "Heated until it glows"},
         ],
         # ⚖️ Three proportions, and every one of them is DISABLED once the
         # dish is heated. That refusal is the lesson.
         "ratios": ["Mostly sulfur", "Half and half", "Mostly iron"],
         "ratio_fracs": [0.30, 0.50, 0.70],
         "start_ratio": 1,
         "dish_alt": {
             "mixed": "A particle diagram of a mixture: separate iron "
                      "particles and sulfur particles scattered side by side "
                      "in no fixed proportion.",
             "heated": "A particle diagram of iron sulfide: every iron "
                       "particle is joined to one sulfur particle, in a "
                       "regular repeating arrangement."},
         "dish_note": {
             "mixed": "Two kinds of particle in the same dish, in whatever "
                      "proportion you chose. Nothing is joined to anything.",
             "heated": "One iron atom to one sulfur atom, all the way "
                       "through, and the proportion is not adjustable."},
         # Drawn on the canvas, in mono, at the corners and the foot.
         "captions": {
             "left_mixed": "BEFORE HEATING \u00b7 A MIXTURE",
             "left_heated": "AFTER HEATING \u00b7 IRON SULFIDE",
             "right_mixed": "two kinds of particle, side by side",
             "right_heated": "every iron atom joined to one sulfur atom",
             "iron": "iron",
             "sulfur": "sulfur"},
         "verdict_words": {"settles": "Settles it.",
                           "not": "Settles nothing."},
         "tests": [
             {"id": "look", "name": "Look at it",
              "before": "Grey specks and yellow powder, clearly two different things side by side.",
              "after": "A dull grey-black solid, the same all the way through.",
              "settles": False,
              "verdict": "Interesting, and it settles nothing. Grind the mixture finely enough and it looks uniform too."},
             {"id": "magnet", "name": "Hold a magnet over it",
              "before": "The grey specks jump out and cling to the magnet. The yellow powder is left behind.",
              "after": "Nothing moves at all.",
              "settles": True,
              "verdict": "This one does settle it. The iron can be pulled out of a mixture because it is still iron; it cannot be pulled out afterwards because there is no longer any iron there — only iron atoms, joined to sulfur."},
             {"id": "ratio", "name": "Weigh what combines",
              "before": "Any amounts at all. Nine parts iron to one of sulfur, or the other way round — it is still a mixture of iron and sulfur.",
              "after": "Always 7 g of iron to every 4 g of sulfur. Add extra of either and the extra is left over, unreacted.",
              "settles": True,
              "verdict": "The quiet test, and the strongest. A mixture can be any proportion. A compound has one, and it is not negotiable."},
             {"id": "acid", "name": "Add dilute acid",
              "before": "Bubbles of a gas that burns with a squeaky pop, and the smell of nothing much.",
              "after": "Bubbles of a gas that stinks of rotten eggs.",
              "settles": True,
              "verdict": "Different substance in, different substance out. The mixture gives hydrogen because the iron in it reacts as iron; the compound gives hydrogen sulfide, which nothing in the dish could have given before."},
         ]},

        {"type": "key-fact", "ref": "fixed-proportion"},

        # #s-sort — verdict-cards, column layout, prose headline, on inset.
        {"type": "verdict-cards", "id": "mixture-or-compound", "anchor": "s-sort",
         "ground": "inset",
         "eyebrow": "Your turn · four substances",
         "heading": "Mixture or compound?",
         "head_counter": {"format": "{n} of 4 decided", "total": 4},
         "demand": "classify",
         "prompt": "One question decides all four: does its composition have "
                   "to be exactly that, or could it be anything?",
         "layout": "column",
         "headline": "prose",
         "options": ["Mixture", "Compound"],
         "items": [
             {"id": "x1",
              "headline": "Sea water.",
              "answer": "Mixture.",
              "why": "The saltiness varies from sea to sea and from place to place in the same sea. Boil it off and the salt is back, unchanged."},
             {"id": "x2",
              "headline": "Carbon dioxide, the gas that comes out of a fire extinguisher.",
              "answer": "Compound.",
              "why": "Always one carbon atom to two oxygen atoms, wherever it comes from — a volcano, your lungs or a factory. It puts out fires, which neither carbon nor oxygen does."},
             {"id": "x3",
              "headline": "Steel, made by adding a little carbon to iron.",
              "answer": "Mixture.",
              "why": "The amount of carbon is chosen by the steelmaker and changes the properties. Anything whose recipe can be adjusted is a mixture."},
             {"id": "x4",
              "headline": "Sugar, however carefully it is purified.",
              "answer": "Compound.",
              "why": "Carbon, hydrogen and oxygen in a fixed ratio. It is not a mixture of those three: carbon is black, hydrogen and oxygen are gases, and sugar is a sweet white solid."},
         ]},

        {"type": "misconception", "id": "think-commit-magnet", "anchor": "s-think",
         "targets": "ATOM-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "fixed-proportion",
         "text": "A mixture can be any proportion and can be separated again. "
                 "A compound is one fixed proportion, joined in a reaction, "
                 "and behaves like neither element that made it.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-magnet",
         "kind": "predict",
         "demand": "explain",
         "targets": "ATOM-07",
         "prompt": "Every iron atom that went into the dish is still in the "
                   "dish. Commit to what that does and does not mean.",
         "options": [
             "The iron atoms are all there, so the substance is still magnetic",
             "The iron atoms are all there, but the substance they make is "
             "not iron",
             "The iron atoms were destroyed by the heat",
             "The iron atoms turned into sulfur atoms",
         ],
         "reveal": [
             "The atoms are all present and the element is not. Being magnetic "
             "is a property of <em>iron</em> — of iron atoms arranged in iron, "
             "with nothing else joined to them. In iron sulfide each iron atom "
             "is bonded to a sulfur atom, and the substance those atoms now "
             "make is not magnetic, not shiny, and does not behave like either "
             "of the things that went in.",
             "This is the whole idea of a compound, and it is why sodium — a "
             "metal that catches fire in water — and chlorine — a poisonous "
             "green gas — join to make the salt on your chips. The properties "
             "belong to the substance, not to the shopping list of atoms in it.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        "recall": {
            "q": "What is a compound?",
            "options": [
                "Two or more elements chemically joined together",
                "Two or more elements mixed together thoroughly",
                "Any substance made of more than one atom",
                "A substance that cannot be broken down at all",
            ],
            "answer": 0,
            "feedback": {
                1: "Mixing puts them in the same place. Nothing has joined, and a magnet or a filter can still take them apart.",
                2: "Close, and it needs the atoms to be of different elements. Oxygen gas is two atoms joined and is still an element.",
                3: "That is nearer to an element. A compound can be broken down — it just takes a chemical reaction rather than a magnet.",
            }},
        "apply": {
            "q": "Iron and sulfur react in a fixed ratio of 7 g to 4 g. A student heats 7 g of iron with 8 g of sulfur. What do they get?",
            "options": [
                "Iron sulfide, with 4 g of sulfur left over unreacted",
                "A compound with twice as much sulfur in it",
                "Twice as much iron sulfide",
                "A mixture, because the amounts were wrong",
            ],
            "answer": 0,
            "feedback": {
                1: "The proportion in a compound is not adjustable. Extra sulfur cannot join if there is no iron left for it to join to.",
                2: "The iron ran out. Doubling one ingredient does not double a product that needs both.",
                3: "The 7 g and 4 g that can react still do. What is left over is unreacted sulfur sitting in with the compound.",
            }},
        "explain": {
            "q": "Explain how you could tell, using two different tests, whether a grey-black powder is a mixture of iron and sulfur or the compound iron sulfide. Say what each test would show in each case.",
            "field_label": "Your method",
            "placeholder": "First I would…",
            "success": [
                "Names a magnet, and says the iron would be pulled out of the mixture and nothing would move for the compound.",
                "Names a second test — dilute acid, or weighing what reacts — and says what each would show.",
                "Says the mixture keeps the properties of both elements.",
                "Says the compound has its own properties, belonging to neither element.",
                "Does not use appearance alone as evidence.",
            ]},
        "produce": {
            "q": "A mixture of hydrogen and oxygen explodes when a spark is applied. Water is made of the same two elements and is used to put fires out. Explain how both can be true, and say what a chemist would have to do to turn one into the other.",
            "field_label": "Your answer",
            "placeholder": "In the mixture the atoms are…",
            "success": [
                "Says in the mixture the two gases are separate and each behaves as itself.",
                "Says in water the atoms are chemically joined, in a fixed ratio.",
                "Says a compound has properties belonging to neither element.",
                "Says a chemical reaction — a spark — is what joins them, and that electricity can split water back.",
                "Says the atoms themselves are unchanged throughout; only what they are joined to changes.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A compound is two or more elements chemically joined, in a "
                "fixed proportion, making a substance with its own properties. "
                "A mixture is the same elements in the same place, in any "
                "proportion, each still behaving as itself — and it can be "
                "separated again without a reaction.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    "stretch": [
        {"type": "explainer", "id": "hydrogen-and-oxygen",
         "text": "A mixture of hydrogen and oxygen gas is one of the most "
                 "dangerous things you can have in a laboratory: a spark and "
                 "it detonates. Join the same atoms chemically, in the ratio "
                 "of two to one, and you get water — which you use to put "
                 "fires out. Same elements, same ratio by atoms, and the "
                 "difference between the two is only whether the atoms are "
                 "bonded. That difference is worth more than almost anything "
                 "else in chemistry."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── safety (§1.5) — not copyright, and not a callout ────────────────────
    "safety_note": "Heating iron and sulfur produces a small amount of "
                   "hydrogen sulfide, which smells of rotten eggs and is "
                   "toxic. This one belongs in a fume cupboard, done by a "
                   "teacher.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why the magnet stops working?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Bonding — what actually holds the atoms of a compound "
                   "together, and why that changes everything about the "
                   "substance.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
