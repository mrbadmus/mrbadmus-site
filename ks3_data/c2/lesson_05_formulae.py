"""C2 L5 — Formulae (MODEL).

Authored against Design's approved page,
`docs/ks3/design-reference/c2/c2-05-formulae.dc.html` (731 lines), and its
measured specification, `docs/ks3/c2-inventory/PAYLOAD-MAP.md` §6.

Every student-facing string is byte-identical to the approved page.

── Most of it is not a substance, and that is the point ────────────────

Three pairs × three counts × three counts = 27 combinations, of which FIVE
are substances. Design's NOTES §8 calls the refusal "the first honest thing a
formula builder can teach", and it is aimed squarely at ATOM-09 — the idea
that a small number changes how much of the substance there is. Twenty-two
answers of "not a substance" are the argument.

⊕ **One addition inside the drawn component.** Design's page never banks the
substance the builder OPENS on: `mark()` is the setState callback of the three
control groups only, so the H₂O on screen at mount is displayed, named and
drawn, and cannot be counted unless the student navigates away and back (map
F6). It is banked at mount here. It contradicts nothing on the page.

⚠️ **The not-a-substance name uses ASCII digits** — `H3O2 — not a substance`,
not `H₃O₂` — while every authored name below uses proper subscripts. That is
Design's own line 641 and the page wins; changing it is Mide's call, not a
build decision.

── MRB-204 does not engage here ────────────────────────────────────────

No `formula` block, no triangle, no FIFA, no worked example. This is a MODEL
lesson with no calculation in it, so the four-part ruling has nothing to bind.

⚑ For Mide's science gate, from Design's NOTES:
  * flag 15 — H₂O₂ described as bleaching hair, burning skin and having been
    used as rocket fuel. All true of concentrated peroxide, not of the three
    per cent bottle in a bathroom. Confirm the wording is not alarming about
    that one.
  * flag 16 — glucose C₆H₁₂O₆ and ethanoic acid C₂H₄O₂ both reducing to CH₂O
    in the stretch layer: empirical-formula territory a year early, assessed
    on nothing.
  * flag 17 — rung 4 (`Na₁Cl₁`) requires two independent corrections: that a
    1 is never written, and that salt is not separate particles.
"""

# ── the three pairs the builder offers ───────────────────────────────────
# Page lines 366–370. `aName`/`bName` are the LIVE captions of the two count
# groups and change with the pair, which is why they are authored per pair
# rather than as two fixed labels.
PAIRS = [
             {"id": "ho", "a": "H", "b": "O",
              "aName": "Hydrogen atoms", "bName": "Oxygen atoms"},
             {"id": "co", "a": "C", "b": "O",
              "aName": "Carbon atoms", "bName": "Oxygen atoms"},
             {"id": "nacl", "a": "Na", "b": "Cl",
              "aName": "Sodium atoms", "bName": "Chlorine atoms"},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 171 character for character.
    "slug":        "formulae",
    "title":       "Formulae",
    "discipline":  "chemistry",
    "unit":        "atoms-elements-and-compounds",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚑ The formulae half of AEC.03; `chemical-symbols` owns the symbols half.
    "covers":      ["KS3.C.AEC.03b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 2},
                    {"id": "particles", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    "requires":    ["chemical-symbols"],
    "assumes":     [],
    "references":  ["conservation-of-mass"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "One of these bottles is drinking water. The other "
                    "bleaches hair and has been used as rocket fuel. The "
                    "difference is one atom.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FIVE stops. The page's `hint-placeholder-count="4"` at line 54 is stale.
    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",  "label": "One atom apart",
         "done_when": "committed"},
        {"anchor": "s-builder", "short": "BUILD", "label": "Build a formula",
         "done_when": "three_substances_found"},
        {"anchor": "s-limit",   "short": "LIMIT", "label": "Where it runs out",
         "done_when": "committed"},
        {"anchor": "s-think",   "short": "THINK",
         "label": "Big and small numbers", "done_when": "committed"},
        {"anchor": "s-ladder",  "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "H₂O and H₂O₂. One extra oxygen atom.",
        "prompt": "Both are clear, colourless liquids made of nothing but "
                  "hydrogen and oxygen. One falls out of the sky and you drink "
                  "it. The other burns skin, bleaches hair, and in "
                  "concentrated form has been used to launch rockets.",
        "commit": "What is actually different about them?",
        "options": [
            "One is more concentrated than the other",
            "Each particle of one has an extra oxygen atom",
            "One has something dissolved in it",
            "They are the same substance at different temperatures",
        ],
        "reveal": "Nothing is dissolved in anything. Each particle of one has "
                  "two hydrogen atoms and one oxygen; each particle of the "
                  "other has two hydrogens and two oxygens. That single extra "
                  "atom, in every particle, makes a different substance — and "
                  "the formula is how you say so.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    "misconceptions": [
        {"id": "ATOM-09",
         "statement": "The small number in a formula changes how much of the "
                      "substance there is.",
         "elicited_by": "build-a-formula",
         "confronted_by": "build-a-formula"},
        {"id": "ATOM-10",
         "statement": "2H₂O and H₂O₂ both have four atoms "
                      "written down, so they must be the same thing.",
         "elicited_by": "think-commit-big-small",
         "confronted_by": "think-commit-big-small"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A formula lists which elements are in a substance and counts "
                 "the atoms of each. The small number written low, after a "
                 "symbol, counts the atoms of that element in one particle."},

        # #s-builder — the flagship. Ink-dark practical, one canvas.
        {"type": "formula-builder", "id": "build-a-formula", "anchor": "s-builder",
         "eyebrow": "The model · change one number",
         "heading": "Build a formula and see what you have made",
         # ⊖ CORRECTED, and reported. Design's readout promises FIVE
         # (`'{n} of 5 real substances found'`, page line 622) while the stage
         # ticks at THREE (line 572). Map F5 records the contradiction and
         # leaves the call open.
         #
         # The correction is to the LABEL, never to what ticks — the B2 pass's
         # precedent, where b2-03's counter could read "5 of 4" and the count
         # was clamped rather than the tick condition changed. Every other
         # counter in C2 is a completion bar whose total IS its tick condition
         # (5 of 5 steps, 6 of 6 decided, 4 of 4 tests, 9 of 9 placed), and
         # these two were the only outliers. So the total becomes what the
         # stage actually requires, and `setCount`'s existing clamp means a
         # student who finds all five reads "3 of 3" — a completion bar that
         # has completed, rather than a promise the gate does not keep.
         #
         # ⚑ It changes one of Design's strings, so it is Mide's to confirm.
         # The alternative — raising the tick to five — would change what
         # ticks, which the precedent forbids.
         "head_counter": {"format": "{n} of 3 real substances found",
                          "total": 3},
         "done_at": 3,
         "demand": "investigate",
         "targets": "ATOM-09",
         "prompt": "Two elements, and a count for each. Most combinations are "
                   "not substances at all — which is the first thing worth "
                   "knowing about formulae.",
         "gate": {"prompt": "Commit first. If you change the 2 in H₂O "
                            "to a 3, what have you got?",
                  "options": ["More water", "A different substance",
                              "Thicker water",
                              "The same thing written differently"]},
         "labels": {"pairs": "Two elements"},
         "pairs": PAIRS,
         "counts": [1, 2, 3],
         "start": {"pair": "ho", "a": 2, "b": 1},
         "colours": {"H": "#F4E9D8", "O": "#8FB7FF", "C": "#C6B9A7", "Na": "#FFC53D", "Cl": "#7FB3A8"},
         "alt": {"template": "A particle diagram of {name}",
                 "molecule": ", drawn as joined circles labelled with their "
                             "symbols.",
                 "giant": ", drawn as a repeating stack of alternating atoms.",
                 "none": "An empty particle view: no substance has this "
                         "formula."},
         "captions": {"molecule": "one particle",
                      "giant": "a repeating stack, going on in every "
                               "direction"},
         # ⚖️ 22 of the 27 combinations land here, and that IS the lesson.
         "not_found": {
             "name_suffix": " — not a substance",
             "note": "Atoms do not join in any combination you like. How many "
                     "of each can bond is fixed by the elements themselves, "
                     "which is why most of the formulae you could invent do "
                     "not exist.",
             "canvas_lines": ["no substance with this formula",
                              "not every combination of atoms is a substance"]},
         # The five reachable substances, keyed pair:countA:countB.
         "known": {
             "ho:2:1": {"name": "H₂O — water",
                          "note": "Two hydrogen atoms and one oxygen atom in every particle. You are about 60% of this.",
                          "atoms": [{"s": "O", "x": 0, "y": 0, "r": 26}, {"s": "H", "x": -46, "y": 30, "r": 18}, {"s": "H", "x": 46, "y": 30, "r": 18}],
                          "bonds": [[0, 1], [0, 2]]},
             "ho:2:2": {"name": "H₂O₂ — hydrogen peroxide",
                          "note": "One more oxygen in each particle than water, and a completely different substance: it bleaches, it burns skin, and it breaks down into water and oxygen.",
                          "atoms": [{"s": "H", "x": -78, "y": 26, "r": 18}, {"s": "O", "x": -30, "y": 0, "r": 26}, {"s": "O", "x": 30, "y": 0, "r": 26}, {"s": "H", "x": 78, "y": 26, "r": 18}],
                          "bonds": [[0, 1], [1, 2], [2, 3]]},
             "co:1:1": {"name": "CO — carbon monoxide",
                          "note": "One carbon, one oxygen. Colourless, odourless, and it kills by taking the place of oxygen in your blood.",
                          "atoms": [{"s": "C", "x": -28, "y": 0, "r": 26}, {"s": "O", "x": 28, "y": 0, "r": 28}],
                          "bonds": [[0, 1]]},
             "co:1:2": {"name": "CO₂ — carbon dioxide",
                          "note": "One carbon and two oxygens. Breathed out by every living thing, and the gas that puts out fires.",
                          "atoms": [{"s": "O", "x": -62, "y": 0, "r": 28}, {"s": "C", "x": 0, "y": 0, "r": 26}, {"s": "O", "x": 62, "y": 0, "r": 28}],
                          "bonds": [[0, 1], [1, 2]]},
             "nacl:1:1": {"name": "NaCl — sodium chloride, or salt",
                          "note": "One sodium for every chlorine — but not as separate particles. This one is a giant repeating stack, and the formula gives the ratio.",
                          "giant": True},
         }},

        {"type": "key-fact", "ref": "which-and-how-many"},

        # #s-limit — the MODEL family's *where it breaks* step, on inset.
        # ⚠️ THREE options, not four. The only three-option commit in KS3,
        # recorded so a later pass does not "correct" it.
        {"type": "model-limit", "id": "where-it-runs-out", "anchor": "s-limit",
         "ground": "inset",
         "eyebrow": "Where the model runs out",
         "heading": "NaCl is not a particle with one of each in it",
         "demand": "explain",
         "prompt": "Everything so far has treated a formula as a recipe for "
                   "one particle. For salt that is not what is happening, and "
                   "the model has to bend.",
         "cards": [
             {"ground": "card",
              "caption": "A molecule · CO₂",
              "text": "Separate particles float about, each one made of "
                      "exactly one carbon and two oxygens. You could, in "
                      "principle, pick one out. The formula counts the atoms "
                      "in that particle."},
             {"ground": "ink",
              "caption": "A giant structure · NaCl",
              "text": "A single grain of salt is billions of sodium and "
                      "chlorine atoms locked in one repeating stack, with no "
                      "separate particles at all. NaCl is a "
                      "<strong>ratio</strong> — one sodium for every chlorine "
                      "— not a count of what is in one particle."},
         ],
         # ⚑ MRB-220. Design's wording was "So what does the formula for salt
         # tell you?" — a real Law 4 gate (commit, options, reveal all present)
         # whose PROMPT never named the action, so §2.4's card check read the
         # grid as tappable with nothing asked first. The commitment is Design's
         # and unchanged; the sentence now says when to make it. No science moved.
         "commit": "Decide before you tap a card: what does the formula for "
                   "salt tell you?",
         "options": [
             "How many atoms are in one particle of salt",
             "The ratio of sodium atoms to chlorine atoms in the stack",
             "How many grains are in a spoonful",
         ],
         "reveal": "The formula still tells you the proportion, and that is "
                   "what it was always doing. For a molecule the proportion "
                   "happens to be the contents of one particle as well; for a "
                   "giant structure it is only the proportion. A model that "
                   "has to be told where it stops applying is more useful than "
                   "one that pretends it never does."},

        {"type": "misconception", "id": "think-commit-big-small",
         "anchor": "s-think", "targets": "ATOM-10"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "which-and-how-many",
         "text": "A formula says which elements are present and how many atoms "
                 "of each. Change one of those numbers and you have not "
                 "changed the amount — you have changed the substance.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-big-small",
         "kind": "predict",
         "demand": "explain",
         "targets": "ATOM-10",
         "prompt": "One of those is a big number at the front, and one is a "
                   "small number at the back. Commit before you read on.",
         "options": [
             "They are the same — four atoms either way",
             "2H₂O is two particles of water; H₂O₂ is one "
             "particle of a different substance",
             "2H₂O is a bigger particle than H₂O₂",
             "Only one of them is a real substance",
         ],
         "reveal": [
             "<strong>2H₂O</strong> is two particles of water. Two of "
             "the same thing you drink. <strong>H₂O₂</strong> is "
             "one particle of hydrogen peroxide, which is a different "
             "substance entirely.",
             "A big number in front multiplies whole particles and changes "
             "<em>how much</em> you have. A small number after a symbol counts "
             "atoms inside one particle and changes <em>what</em> you have. It "
             "is the difference between two glasses of water and a bottle of "
             "bleach.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        "recall": {
            "q": "How many atoms are there altogether in one particle of H₂SO₄?",
            "options": [
                "Seven",
                "Three",
                "Four",
                "Eight",
            ],
            "answer": 0,
            "feedback": {
                1: "Three is the number of elements — H, S and O. The question asks for atoms, so the small numbers have to be counted too.",
                2: "Four is the number of oxygen atoms alone. Add the two hydrogens and the sulfur.",
                3: "Close: 2 hydrogens + 1 sulfur + 4 oxygens. The sulfur has no small number, which means one, not two.",
            }},
        "apply": {
            "q": "What is the difference between 2CO₂ and C₂O₄?",
            # ⊕ MRB-177, ruled 17 Aug 2026 — the three distractors now state
            # wrong RULES, in the same shape as the correct option. The
            # correct option and its index are unchanged.
            "options": [
                "2CO₂ is two particles of carbon dioxide; C₂O₄ would be a single particle with twice as much in it",
                "The same atoms in the same numbers make the same substance, however the formula is written",
                "The big number counts particles and the small number counts atoms, so 2CO₂ holds more atoms altogether",
                "A number written in front makes a mixture, and a number written below makes a compound",
            ],
            "answer": 0,
            "feedback": {
                1: "The same atoms, arranged completely differently. One is two ordinary particles; the other would be one particle twice the size.",
                2: "Both come to two carbons and four oxygens. Totalling the atoms does not distinguish them, and that is exactly the trap.",
                3: "Both describe one substance. The 2 in front is an amount, not a second ingredient.",
            }},
        "explain": {
            "q": "Explain why H₂O and H₂O₂ are different substances rather than different amounts of the same one, and say what would happen if you tried to make water by removing an oxygen atom.",
            "field_label": "Your explanation",
            "placeholder": "Each particle of hydrogen peroxide…",
            "success": [
                "Says each particle of hydrogen peroxide has one more oxygen atom than a particle of water.",
                "Says a change inside the particle makes a different substance, not more or less of the same one.",
                "Names at least one way the two behave differently.",
                "Says removing an oxygen atom would be a chemical reaction, not a separation.",
                "Does not describe hydrogen peroxide as water with something dissolved in it.",
            ]},
        "produce": {
            "q": "A student writes the formula for salt as Na₁Cl₁ and says it means one particle containing one sodium and one chlorine atom. Two things are wrong. Say what they are, and give the version a chemist would write.",
            "field_label": "Your answer",
            "placeholder": "The first problem is…",
            "success": [
                "Says a 1 is never written — a symbol with no number after it already means one.",
                "Says salt is not made of separate particles containing one of each.",
                "Says it is a giant structure of atoms in a repeating stack.",
                "Says the formula gives the ratio of sodium to chlorine, which is one to one.",
                "Gives NaCl as the correct version.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A formula gives the elements in a substance and the number of "
                "atoms of each. A small number after a symbol counts atoms "
                "inside one particle; a big number in front counts particles. "
                "For a giant structure like NaCl the formula gives the ratio, "
                "because there is no single particle to count.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    "stretch": [
        {"type": "explainer", "id": "empirical-hint",
         "text": "Glucose is C₆H₁₂O₆ and ethanoic acid "
                 "— vinegar — is C₂H₄O₂. Divide both down "
                 "and they reach the same ratio: one carbon, two hydrogens, "
                 "one oxygen. Same proportions, wildly different substances, "
                 "because what differs is how many atoms are in each particle "
                 "and how they are joined. It is the first hint that a formula "
                 "is not the whole story, and the reason chemists eventually "
                 "needed structures as well as formulae."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Confused by big numbers and small numbers?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Balancing equations, and working out a formula from the "
                   "masses that react.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
