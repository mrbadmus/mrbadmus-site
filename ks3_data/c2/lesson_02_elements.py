"""C2 L2 — Elements (CLASSIFY).

Authored against Design's approved page,
`docs/ks3/design-reference/c2/c2-02-elements.dc.html` (648 lines), and its
measured specification, `docs/ks3/c2-inventory/PAYLOAD-MAP.md` §3.

Every student-facing string below is byte-identical to the approved page:
`RAIL`, `TESTS`, `SAMPLES`, `RUNGS` and `SELF_RUNGS` came out of
`node tools/extract_design_payload.js`, and the strings inside `renderVals()`
— the hook and think options, the budget line, the verdict button labels —
were lifted from the line ranges the payload map records.

── The budget is the lesson ─────────────────────────────────────────────

Eight tests across six samples, and it is GLOBAL. Design's NOTES §3.2:
*"the budget is the pedagogy, not a game mechanic. With unlimited tests the
student runs everything and learns nothing about which evidence discriminates.
If Code drops the budget the lesson quietly becomes a click-through."* It is
a `data-props` dial on Design's page (4–24, default 8), which the platform has
no prop concept for; it is authored here instead, which is the same dial in a
place a teacher's build can reach.

Brass is on the bench precisely because it is the most convincing-looking
sample and is not an element.

── Reproduced, not corrected ───────────────────────────────────────────

* **The instrument never marks.** The verdict panel fires on the student's
  verdict whether or not that verdict was right, and it is the only place a
  sample is named. `element` is authored on every sample and read by nothing
  (map N16) — correctness data waiting for a marker that R3 says must not
  arrive here. Kept and flagged, not deleted.
* **Four rail stops, not five.** The only four-stop page in the unit: there is
  no second task block between the bench and `#s-think`.
"""

# ── the four tests, offered against every sample ─────────────────────────
# Page lines 325–330. Three of the four are the interesting ones and all
# three are worthless, which is the whole argument of the lesson.
TESTS = [
             {"id": "look", "label": "Look at it closely"},
             {"id": "conduct", "label": "Test whether it conducts"},
             {"id": "table", "label": "Look for it on the periodic table"},
             {"id": "break", "label": "Try to break it down"},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 168 character for character.
    "slug":        "elements",
    "title":       "Elements",
    "discipline":  "chemistry",
    "unit":        "atoms-elements-and-compounds",
    "family":      "CLASSIFY",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚑ The element half of AEC.02; `compounds` owns the other half. See
    # `ks3_data/substatements.py` and the flag in `ks3_data/chemistry_c2_atoms.py`.
    "covers":      ["KS3.C.AEC.02a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 1},
                    {"id": "particles", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    "requires":    ["the-atom-daltons-model"],
    "assumes":     [],
    "references":  ["compounds"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Everything there has ever been is built from about a "
                    "hundred kinds of atom. So how do you tell whether the "
                    "thing in front of you is one of them?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops (page lines 318–323) — the only four-stop page in C2.
    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",  "label": "On the list or not",
         "done_when": "committed"},
        {"anchor": "s-bench", "short": "TESTS", "label": "Six samples",
         "done_when": "all_samples_decided"},
        {"anchor": "s-think", "short": "THINK", "label": "Brass",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚑ NOTES flag 3 is Mide's: "a phone contains about sixty of them" is
    # commonly quoted as 60–70 elements in a smartphone. Confirm, or give a
    # figure you are happy to defend.
    "phenomenon": {
        "kind": "narrative",
        "title": "A phone contains about sixty of them. There are only about "
                 "a hundred to choose from.",
        "prompt": "Every substance in the world — every rock, gas, liquid, "
                  "plastic, medicine and living thing — is built from the same "
                  "short list. Not a long list. About a hundred entries, and "
                  "roughly sixty of them are in the phone in your pocket.",
        "commit": "If you had a sample of something, how would you find out "
                  "whether it was on that list?",
        "options": [
            "See whether it looks like a metal",
            "Test whether it conducts electricity",
            "Try to break it down into anything simpler",
            "Weigh it and measure its melting point",
        ],
        "reveal": "Only one of those four actually settles it, and it is not "
                  "the one that tells you the most about the substance. An "
                  "element is a substance made of only one kind of atom — so "
                  "the test is whether anything simpler can be got out of it.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Statements stored WITHOUT curly quotes; the renderer adds them.
    "misconceptions": [
        {"id": "ATOM-03",
         "statement": "Brass is a metal, and metals are elements, so brass is "
                      "an element.",
         "elicited_by": "think-commit-brass",
         "confronted_by": "think-commit-brass"},
        {"id": "ATOM-04",
         "statement": "An element is a pure substance, so anything pure is an "
                      "element.",
         "elicited_by": "six-samples",
         "confronted_by": "six-samples"},
        {"id": "ATOM-05",
         "statement": "Reacting violently means being broken down.",
         "elicited_by": "six-samples",
         "confronted_by": "six-samples"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "An <strong>element</strong> is a substance made of one kind "
                 "of atom and nothing else. Copper is copper atoms; sulfur is "
                 "sulfur atoms. That is the whole definition, and none of it "
                 "is about how the substance looks."},

        # #s-bench — the flagship. A LIGHT `.ks3-block` (→ `check`): the only
        # page in the unit with no practical and no canvas.
        {"type": "test-budget-bench", "id": "six-samples", "anchor": "s-bench",
         "eyebrow": "Your turn · six unlabelled samples",
         "heading": "Eight tests. Six samples. Choose carefully.",
         # Three live numbers in one line. `budget` is a constant and is baked
         # into the format at build time; `left` and `n` move.
         "head_counter": {
             "format": "{left} of {budget} tests left · {n} of 6 decided",
             "constants": {"budget": 8},
             "start_extra": {"left": 8},
             "total": 6,
             "tone": "accent"},
         "demand": "classify",
         "targets": "ATOM-04",
         "prompt": "Each test costs one of your eight. You need a verdict on "
                   "all six samples, so you cannot run everything on "
                   "everything — and one of the four tests is worth far more "
                   "than the others.",
         # ⚖️ Design's teaching dial: 4 makes it brutal, 24 makes it pointless.
         "budget": 8,
         "labels": {"ask": "Your verdict on this sample", "decided": " \u00b7"},
         "verdicts": [
             {"id": "yes", "label": "It is an element"},
             {"id": "no", "label": "It is not an element"},
         ],
         "tests": TESTS,
         # ⚑ NOTES flags 5 and 6 are Mide's: sample 6 says reacting violently
         # with water builds a compound rather than taking sodium apart,
         # without naming the products; and sample 2's "two to one by volume"
         # for the electrolysis of water. Both confirmed by him, not here.
         "samples": [
             {"id": "s1", "tab": "Sample 1",
              "name": "Sample 1",
              "look": "A dull orange solid that can be bent without snapping.",
              # Correctness data with no marker behind it (map N16). Design's
              # intent, kept and flagged rather than deleted.
              "element": True,
              "name2": "Copper — an element.",
              "results": {
                  "look": "Orange, metallic, bendable. Copper looks like this; so does brass, and so does bronze.",
                  "conduct": "It conducts electricity well. So does every other metal on this bench, and so does salt water.",
                  "table": "There is an entry: copper, Cu. That settles it, though it is looking the answer up rather than finding it out.",
                  "break": "Heated, electrolysed and treated with acid, nothing simpler ever comes out of it.",
              },
              "why": "Nothing simpler can be got out of it, and it has its own entry on the periodic table. Made of copper atoms only."},
             {"id": "s2", "tab": "Sample 2",
              "name": "Sample 2",
              "look": "A colourless liquid with no smell.",
              # Correctness data with no marker behind it (map N16). Design's
              # intent, kept and flagged rather than deleted.
              "element": False,
              "name2": "Water — not an element. It is a compound.",
              "results": {
                  "look": "Clear, colourless, runny. Indistinguishable by eye from a dozen other liquids.",
                  "conduct": "Pure water barely conducts at all. Tap water does, because of what is dissolved in it.",
                  "table": "No entry called water anywhere on the table.",
                  "break": "Pass electricity through it and two different gases come off, in a fixed ratio of two to one by volume.",
              },
              "why": "Two different gases came out of it, so it was made of more than one kind of atom all along."},
             {"id": "s3", "tab": "Sample 3",
              "name": "Sample 3",
              "look": "A bright yellow powder that smells faintly of nothing much.",
              # Correctness data with no marker behind it (map N16). Design's
              # intent, kept and flagged rather than deleted.
              "element": True,
              "name2": "Sulfur — an element.",
              "results": {
                  "look": "Yellow, powdery, does not look remotely like a metal.",
                  "conduct": "It does not conduct at all. Neither does sugar, and sugar is not an element.",
                  "table": "There is an entry: sulfur, S.",
                  "break": "Nothing simpler can be got out of it by heating, dissolving or electrolysis.",
              },
              "why": "Not everything on the list is a metal. Yellow powder, one kind of atom."},
             {"id": "s4", "tab": "Sample 4",
              "name": "Sample 4",
              "look": "A hard, shiny, gold-coloured metal that rings when tapped.",
              # Correctness data with no marker behind it (map N16). Design's
              # intent, kept and flagged rather than deleted.
              "element": False,
              "name2": "Brass — not an element. It is a mixture of copper and zinc.",
              "results": {
                  "look": "Shiny, gold-coloured, hard. The most convincing-looking sample on the bench.",
                  "conduct": "It conducts well, like every metal here.",
                  "table": "No entry called brass. There is copper, and there is zinc.",
                  "break": "Its composition can be varied — 70% copper and 30% zinc, or 60/40 — and it can be separated. Nothing fixed about it.",
              },
              "why": "The most metal-looking sample here is not an element at all. Metal describes how it behaves; element describes what it is made of."},
             {"id": "s5", "tab": "Sample 5",
              "name": "Sample 5",
              "look": "A colourless gas that does nothing obvious.",
              # Correctness data with no marker behind it (map N16). Design's
              # intent, kept and flagged rather than deleted.
              "element": False,
              "name2": "Air — not an element. It is a mixture of several gases.",
              "results": {
                  "look": "Invisible. Looking at it tells you precisely nothing.",
                  "conduct": "It does not conduct under ordinary conditions.",
                  "table": "No entry called air. There is nitrogen, oxygen, argon.",
                  "break": "Cooled until it liquefies and then warmed slowly, it separates into several different gases with different boiling points.",
              },
              "why": "It separates into several gases, and the proportions vary from place to place. Nothing about being invisible makes something simple."},
             {"id": "s6", "tab": "Sample 6",
              "name": "Sample 6",
              "look": "A soft, silvery metal that has to be kept under oil.",
              # Correctness data with no marker behind it (map N16). Design's
              # intent, kept and flagged rather than deleted.
              "element": True,
              "name2": "Sodium — an element.",
              "results": {
                  "look": "Silvery when freshly cut, and it dulls over within seconds in air.",
                  "conduct": "It conducts, like every metal here.",
                  "table": "There is an entry: sodium, Na.",
                  "break": "Nothing simpler comes out of it. It reacts violently with water, which makes something more complicated, not something simpler.",
              },
              "why": "Reacting violently is not the same as breaking down. A reaction with water builds a compound out of it; it does not take it apart."},
         ],
         "close": "Six verdicts. Every one of them turned on the same "
                  "question — can anything simpler be got out of it — and none "
                  "of them turned on how the sample looked. Shine, colour and "
                  "conducting were the three most interesting results you "
                  "could buy, and all three were worthless."},

        {"type": "key-fact", "ref": "one-kind-of-atom"},

        {"type": "misconception", "id": "think-commit-brass", "anchor": "s-think",
         "targets": "ATOM-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "one-kind-of-atom",
         "text": "An element is made of one kind of atom, and cannot be broken "
                 "down into anything simpler by chemistry. Nothing about how "
                 "it looks will tell you.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-brass",
         "kind": "predict",
         "demand": "explain",
         "targets": "ATOM-03",
         "prompt": "Brass is hard, shiny, gold-coloured, conducts electricity "
                   "and rings when you hit it. Commit before you read on.",
         "options": [
             "Brass is an element — it is a metal",
             "Brass is not an element — it is copper and zinc mixed",
             "Brass is an element, but only when it is pure",
             "There is no way to tell without heating it",
         ],
         "reveal": [
             "Brass is copper and zinc, mixed while both are molten. There is "
             "no such thing as a brass atom, and brass has no entry on the "
             "periodic table. Every metallic thing in the sentence is true and "
             "none of it settles anything: <strong>metal</strong> describes "
             "how a substance behaves, and <strong>element</strong> describes "
             "what it is made of. Steel, bronze and solder are all in the same "
             "position.",
             "This is the useful thing about brass: it is more useful than "
             "either of the metals in it, and that is why it exists. Behaving "
             "like a metal is not evidence of being an element. It is evidence "
             "of having metal atoms in it, and mixtures have those too.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        "recall": {
            "q": "What makes a substance an element?",
            "options": [
                "It is made of only one kind of atom",
                "It is a pure metal",
                "It cannot be melted or boiled",
                "It is found naturally rather than made in a factory",
            ],
            "answer": 0,
            "feedback": {
                1: "Sulfur, oxygen and carbon are all elements and none of them is a metal.",
                2: "Every element can be melted and boiled at some temperature. That is a physical change, and it takes nothing apart.",
                3: "Several elements are made artificially and are still elements. Where it came from is not the test.",
            }},
        "apply": {
            "q": "A student has an unknown silvery solid. Which single result would settle whether it is an element?",
            "options": [
                "Electricity passed through it produces two new substances",
                "It conducts electricity",
                "It is shiny and can be hammered flat",
                "It melts at a definite temperature",
            ],
            "answer": 0,
            "feedback": {
                1: "Copper conducts and is an element; brass conducts and is not. A shared property discriminates nothing.",
                2: "True of copper, brass, steel and solder — two of which are not elements.",
                3: "Compounds have definite melting points too. Water melts at exactly 0 °C and is not an element.",
            }},
        "explain": {
            "q": "A student says \"gold is an element because it is shiny and expensive, and brass is not because it is cheap\". Their conclusion about both is right and their reasoning is wrong. Explain why, and give the reasoning that works.",
            "field_label": "Your explanation",
            "placeholder": "Being shiny or expensive has nothing to do with…",
            "success": [
                "Says that appearance and value have nothing to do with being an element.",
                "Says an element is made of one kind of atom.",
                "Says gold cannot be broken down into anything simpler, and that this is the reason.",
                "Says brass is made of copper and zinc, so it is more than one kind of atom.",
                "Notes that getting the right answer for the wrong reason will fail on the next sample.",
            ]},
        "produce": {
            "q": "Before electricity was available, chemists thought several substances were elements that turned out not to be — including one they called \"soda\". Explain how a new technique can move something off the list, and whether that means the earlier chemists were careless.",
            "field_label": "Your answer",
            "placeholder": "A substance was called an element because…",
            "success": [
                "Says a substance is called an element when nothing simpler can be got out of it by the methods available.",
                "Says a new method — electricity — could take apart things that heating and acids could not.",
                "Says the substance was therefore never an element; the list was wrong, not the substance.",
                "Says the earlier chemists were not careless: they reported what their methods could show.",
                "Draws the general point — the list depends on what can be done, so it can change.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "An element is a substance made of only one kind of atom. "
                "There are about a hundred, they are the entries on the "
                "periodic table, and the test is always the same: can anything "
                "simpler be got out of it? Looking like a metal proves nothing.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES flag 2 is Mide's: "about a hundred kinds", 118 entries, roughly
    # 94 natural, "fewer than thirty needed by living things". Confirm all
    # three numbers.
    "stretch": [
        {"type": "explainer", "id": "six-elements",
         "text": "Ninety-nine per cent of your body is six elements — oxygen, "
                 "carbon, hydrogen, nitrogen, calcium and phosphorus — and "
                 "almost all of the oxygen and hydrogen is water. The "
                 "remaining one per cent includes iron you cannot carry oxygen "
                 "without, and iodine you cannot grow properly without. Fewer "
                 "than thirty of the hundred are known to be needed by living "
                 "things at all, and every one of the atoms in you was made "
                 "inside a star or in the collision of two of them. There is "
                 "no such thing as a fresh atom."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why brass is not an element?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "The periodic table as an organised list, and why the "
                   "elements fall into groups at all.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
