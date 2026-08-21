"""C8 L6 — Group 0 and why groups exist (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c8/c8-06-group-0-and-why-groups-exist.dc.html`, and
her author's notes `NOTES-C8.md` §1, §3, §4, §5 flags 8, 9, 17–19, §6
(`PTAB-09`, `PTAB-10`) and §7.

The unit's capstone. Design's README labels it APPLY, which is not one of the
seven families (§6); it is mapped to **MODEL** by rhythm — one idea, a full
outer shell, explaining a whole class of behaviour where there is no series to
extrapolate along. That is also exactly the clause it owns, `PT.04c`.

── SIX RAIL STOPS, NOT FIVE ─────────────────────────────────────────────

Every other C8 lesson has five. This one has six — hook, shells, file, uses,
think, ladder — and it is matched stop for stop against Design (MRB-249).

── ⊖ R2 · THE FORWARD LINK TO c8-07 IS NOT AUTHORED HERE ────────────────

`NOTES-C8.md` §7 records this page as linking forward to
`c8-07-metal-and-non-metal-oxides.html`, "which does not exist", and asks for
it to be treated as a build blocker. Two things resolve it and neither is a
placeholder:

1. **The slot now EXISTS** (MRB-281, R1). `structure.py` carries
   `metal-and-non-metal-oxides` as C8's seventh slot, so the generated
   prev/next link resolves to a real, routable coming-soon page. It is no
   longer an intra-unit dead link.
2. **No forward-link PROSE is authored in this record.** MRB-257 ruled that a
   placeholder is the build's backlog printed to a twelve-year-old, and a
   sentence in a lesson body pointing at a lesson that is not there is exactly
   that. The unit index already carries unbuilt slots as coming-soon rows;
   that convention needs no help from prose, and it resolves on its own the
   day c8-07 ships.

Endmatter prev/next is GENERATED from unit order by the engine, never
hand-written here (§8.10 / audit law 16), so there is nothing to remove when
c8-07 arrives either.

── ⚠️ THIS LESSON TOUCHES `PT.06` AND DOES NOT COVER IT ─────────────────

Unknown W (group 2, period 3) asks what magnesium's oxide does to indicator,
and its answer states the rule: metals form basic oxides, non-metals form
acidic ones. That is `KS3.C.PT.06` content arriving in a prediction card.

It is recorded in `touches`, NOT in `covers`. **`PT.06` remains uncovered and
this does not close the hole** — one card applying a rule is not the CONTRAST
lesson §7 asks for, and ownership is what the register counts. It is kept
because it is true (MRB-225), because it is the same predict-from-the-address
move as the other three cards, and because a student meeting the rule once
here is better served than one who meets it nowhere.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

This lesson holds **index 2** (recall) and **index 1** (apply), completing
C8's twelve marked rungs at three of each index. Only the order moves; neither
rung needed a distractor re-authored, because on both the correct option is
not the longest (recall 7 against 10/6/6; apply 8 against 8/6/5).

── SCIENCE FLAGS ────────────────────────────────────────────────────────

⚑ Flag 8 — argon absent from Mendeleev's table, isolated 1894, caught by
weighing. KEPT (R4) and correct; it closes the loop opened in c8-02's stretch.

⚑ Flag 9 — group number = outer electrons, and **helium's two are the authored
exception**. The shell strip draws eight places and fills two for helium, so
the row would show two dots beside the word "full" — which a student is right
to disbelieve. `r_shell_strip` therefore REFUSES a row flagged `full` with
`n != slots` unless it carries a `detail` saying why, and group 0's detail
says it: "Helium manages it with two electrons, the rest with eight."

⚑ Flag 17 — XENON, BARTLETT 1962. KEPT (R4). It is textbook MRB-225: the
lesson says "reacts with nothing" and the stretch layer says the footnote,
and the footnote does not RETRACT the rule — the rule is stated as almost
completely unreactive throughout, so nothing in the body is taken back by a
later sentence.

⚑ FLAG 18 — THE FACT STAYS, THE EDITORIAL EDGE GOES (R4). Design's paragraph
opened "Helium is the one that should worry you" and closed "and a substantial
share of the world's supply goes into party balloons". The CONTRAST is the
lesson — helium is the only element that escapes the planet, and it is the only
coolant cold enough for an MRI magnet — and it is kept in full.

⊖ Both editorial lines are CUT and the paragraph re-authored so the seam lands
as a sentence rather than as a raw deletion. Moralising at twelve-year-olds
about something some of them had at a birthday is not teaching, and it fails
"write for every student in the room": the child who had the balloons did not
choose the supply chain, and the one who did not have them learns nothing from
being told the others were wasteful. The scarcity is stated; the blame is not
apportioned.

⚑ Flag 19 — neon signs as excitation and emission, explicitly NOT a chemical
reaction. KEPT, correct, and it is physics arriving in a chemistry unit on
purpose — it is the third judgement in a block about why unreactive is useful.

⚠️ **SHELL-STRIP STOPS SHORT OF SHELLS-WITHIN-SHELLS DELIBERATELY AND IS TO BE
LEFT THERE** (NOTES-C8 §4). One row is one OUTER shell. Drawing inner shells
would make the picture right and the lesson unreadable, and "group number =
outer electrons" is the whole of what c8-03 and this lesson claim.
"""

LESSON = {
    "slug":  "group-0-and-why-groups-exist",
    "title": "Group 0 and why groups exist",
    "discipline": "chemistry",
    "unit": "The periodic table",
    "family": "MODEL",

    "covers": ["KS3.C.PT.04c"],
    # ⚠️ PT.06 is TOUCHED here and remains UNCOVERED. See the docstring.
    "touches": ["KS3.C.PT.03a", "KS3.C.PT.04a", "KS3.C.PT.04b",
                "KS3.C.PT.06"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3},
                {"id": "particles-and-matter", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 55,

    "requires": ["group-7-the-halogens"],
    "assumes": [],
    "references": ["groups-and-periods", "group-1-the-alkali-metals",
                   "the-atom-daltons-model"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "Argon is one per cent of the air and has been going in "
                    "and out of human lungs for as long as there have been "
                    "lungs. Chemists analysed air for a century and missed "
                    "it. How do you miss an element that common?",

    # SIX stops. Every other C8 lesson has five.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The element nobody found", "done_when": "committed"},
        {"anchor": "s-shells", "short": "SHELLS",
         "label": "Group number is outer electrons",
         "done_when": "all_four_opened"},
        {"anchor": "s-file",   "short": "FILE",
         "label": "Four unknown elements", "done_when": "all_four_predicted"},
        {"anchor": "s-uses",   "short": "USES",
         "label": "Three uses",          "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Not because they are gases", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",      "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Mendeleev's table had no room for argon, because nobody "
                 "knew argon existed.",
        "prompt": "It makes up nearly one per cent of the air. It had been "
                  "going in and out of every pair of human lungs for as long "
                  "as there had been lungs. Chemists had been analysing air "
                  "for a century and missed it entirely.",
        "commit": "How do you miss an element that common?",
        "options": [
            "It had not arrived in the atmosphere yet",
            "Because it forms no compounds, so it left no trace to find",
            "The instruments of the time were not sensitive enough",
            "It was mistaken for oxygen every time",
        ],
        "reveal": "Because the way you found an element in 1869 was to look "
                  "at its compounds — and argon has none. It reacts with "
                  "nothing, so it leaves no trace in any reaction, no colour "
                  "in any flame test, no residue in any analysis. It was "
                  "finally caught in 1894 by weighing: nitrogen taken from "
                  "air was consistently a fraction heavier than nitrogen made "
                  "in the lab, and the difference was argon hiding inside the "
                  "sample.",
    },

    "misconceptions": [
        {"id": "PTAB-09",
         "statement": "The noble gases are unreactive because they are gases.",
         "elicited_by": "think-commit-gas",
         "confronted_by": "think-commit-gas"},

        # ⚑ NOTES-C8 §6 proposes `uses-block` / `uses-reveal`. Neither is
        # emitted — `r_predict_cards` gives each card a `data-pcard-card`
        # value, not an `id` and not a `data-activity` — so both would fail
        # MRB-244 / MRB-248. The join names the ACTIVITY that owns the whole
        # block: three cards, each of which is somebody paying money for a gas
        # BECAUSE it does nothing.
        {"id": "PTAB-10",
         "statement": "Unreactive means useless.",
         "elicited_by": "uses-three",
         "confronted_by": "uses-three"},
    ],

    # ── the confrontation (Law 3) ───────────────────────────────────────
    # ⚠️ AUTHORED IN `activities`, NOT LIFTED FROM `core`. `_normalise`
    # lifts INSTRUMENT kinds only, so a `misconception` core block whose id
    # names no activity renders as NOTHING AT ALL — `r_activity` returns an
    # empty string and the section, its `id`, its `data-activity` and its
    # rail stop all vanish. The page still builds and still reads.
    #
    # ⚑ The QUOTE is not authored here: `_confrontations` takes it from the
    # row for `targets` in `docs/ks3/misconception-register.md`, so the
    # register and the page have one source and cannot drift.
    "activities": [
        {"id": "think-commit-gas",
         "kind": "predict",
         "demand": "explain",
         "targets": "PTAB-09",
         "prompt": "They are all gases, and they all fail to react. Commit before"
                    " you read on.",
         # ⚑ MRB-177 / MRB-278 — THE DISTRACTORS ARE RE-AUTHORED AND THE
         # CORRECT OPTION IS UNTOUCHED. Design's set gave the answer away on
         # length alone, which turns a commitment device into a shape puzzle:
         # a student picks the long one, never commits to the belief, and is
         # therefore never confronted with it. Each distractor now states its
         # wrong RULE at full length, which is what MRB-177 asks for.
         # 16, 18, 16, 16 words.
         "options": [
             "Right — the atoms in a gas are spread too far apart to meet and"
             " react",
             "Wrong — fluorine and oxygen are gases and both react fiercely;"
             " the reason is the full outer shell",
             "Right, because the atoms in a noble gas never come close enough"
             " to touch each other",
             "Wrong — they do react readily enough, but far too slowly for"
             " anyone to ever notice",
         ],
         "reveal": [
             "Fluorine is a gas and it is the most reactive element there"
             " is. Chlorine is a gas and it attacks almost every metal."
             " Oxygen is a gas and nothing burns without it. Being a gas has"
             " no bearing on whether an element reacts.",
             "The noble gases are unreactive because their outer shells are"
             " full — there is no electron they need to lose and no space for"
             " one to arrive. <strong>And it works the other way round too:"
             " they are gases because they are unreactive.</strong> Their"
             " atoms have so little attraction for each other that nothing"
             " holds them together as a liquid or a solid except at extreme"
             " cold.",
         ]},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Group 0 — helium, neon, argon, krypton, xenon — are the "
                 "<strong>noble gases</strong>. Colourless, invisible, and so "
                 "unreactive that for decades they were thought to form no "
                 "compounds at all."},
        {"type": "explainer",
         "text": "The reason is the same one behind every group in the table. "
                 "An atom's <strong>outer shell</strong> of electrons is what "
                 "does the reacting, and the group number tells you how many "
                 "electrons are in it. Group 0 atoms have a "
                 "<strong>full</strong> outer shell. There is nothing to lose "
                 "and no room to gain, so there is no reaction to have."},

        # ── #s-shells — the one idea. Light `ks3-block` → `check`.
        {"type": "shell-strip", "id": "shells-four", "anchor": "s-shells",
         "eyebrow": "Reference · the one idea behind all of it",
         "heading": "Group number is outer electrons",
         "demand": "investigate",
         "lead": "Every trend in this unit falls out of this single column of "
                 "numbers. Tap a row to see what it forces the element to do.",
         "head_counter": {"format": "{n} of {total} opened", "start": 0,
                          "total": 4},
         "slots": 8,
         "rows": [
             {"id": "g1", "tag": "Group 1", "n": 1,
              "title": "Group 1 · one outer electron",
              "summary": "One outer electron — one to get rid of.",
              "detail": "Reacting means losing that single electron, and one "
                        "is an easy number to lose. Going down the group the "
                        "atoms get bigger, the outer electron sits further "
                        "from the nucleus, and it goes more easily still — "
                        "which is why potassium is more violent than "
                        "lithium."},
             {"id": "g2", "tag": "Group 2", "n": 2,
              "title": "Group 2 · two outer electrons",
              "summary": "Two outer electrons — two to get rid of, which is "
                         "harder.",
              "detail": "Losing two takes more energy than losing one, so "
                        "group 2 metals are less reactive than their "
                        "neighbours in group 1. Magnesium sits quietly in "
                        "cold water; sodium, one square to the left, does "
                        "not."},
             {"id": "g7", "tag": "Group 7", "n": 7,
              "title": "Group 7 · seven outer electrons",
              "summary": "Seven outer electrons — one short of full.",
              "detail": "Reacting means grabbing one more electron to "
                        "complete the shell. A small atom pulls that incoming "
                        "electron in hard, so fluorine at the top of the "
                        "group is ferocious — and the bigger atoms lower down "
                        "pull less, so reactivity falls going down. Same size "
                        "argument as group 1, opposite conclusion."},
             # `full` with n == slots, so the detail is not forced — but it
             # carries helium's exception, which is flag 9's whole content.
             {"id": "g0", "tag": "Group 0", "n": 8, "full": True,
              "title": "Group 0 · a full outer shell",
              "summary": "A full outer shell — nothing to lose, no room to "
                         "gain.",
              "detail": "There is no electron the atom needs to shed and no "
                        "gap for one to fill, so there is no reaction "
                        "available. This is not shyness or slowness: it is "
                        "the absence of anything to react about. Helium "
                        "manages it with two electrons, the rest with "
                        "eight."},
         ]},

        {"type": "key-fact", "ref": "group-is-outer-electrons"},

        # ── #s-file — four unknowns. `predict-cards`, placement 4 of 5.
        {"type": "predict-cards", "id": "file-four", "anchor": "s-file",
         "eyebrow": "Your turn · four unknown elements",
         "heading": "You are told the group and nothing else. Predict anyway.",
         "demand": "predict",
         "head_counter": {"format": "{n} of {total} predicted", "start": 0,
                          "total": 4},
         "items": [
             {"id": "u1", "tag": "Element X · group 1, period 5",
              "q": "A colleague drops a piece into water while you are out of "
                   "the room. What should you expect to have happened?",
              "options": [{"id": "a", "label": "Nothing at all"},
                          {"id": "b", "label": "A violent reaction"},
                          {"id": "c", "label": "It dissolved quietly"}],
              "answer": "A violent reaction, and worse than potassium's — "
                        "period 5 puts it below potassium in the column, and "
                        "group 1 gets more reactive downwards. The element is "
                        "rubidium. Expect hydrogen, a burst of flame and an "
                        "alkaline solution."},
             {"id": "u2", "tag": "Element Y · group 0, period 4",
              "q": "What will Y react with?",
              "options": [{"id": "a", "label": "Water"},
                          {"id": "b", "label": "Oxygen"},
                          {"id": "c", "label": "Essentially nothing"}],
              "answer": "Essentially nothing. Group 0 means a full outer "
                        "shell, and a full shell means no reaction to have. "
                        "The element is krypton, and you can leave it in a "
                        "jar with anything on the shelf for a century."},
             {"id": "u3", "tag": "Element Z · group 7, period 5",
              "q": "Z is added to a solution of potassium chloride. What "
                   "happens?",
              "options": [{"id": "a", "label": "Chlorine is displaced"},
                          {"id": "b", "label": "Nothing"},
                          {"id": "c", "label": "The solution turns green"}],
              "answer": "Nothing. Period 5 puts Z below chlorine in group 7, "
                        "and reactivity falls going down — so it cannot "
                        "displace something above it. The element is iodine, "
                        "and this is the tube you already ran in the last "
                        "lesson."},
             # ⚠️ This card TOUCHES PT.06. It does not cover it, and PT.06
             # remains the unit's uncovered statement. See the docstring.
             {"id": "u4", "tag": "Element W · group 2, period 3",
              "q": "W is burned in air. What is the product, and what would "
                   "it do to universal indicator once dissolved?",
              "options": [{"id": "a",
                           "label": "An oxide; the solution is alkaline"},
                          {"id": "b",
                           "label": "An oxide; the solution is acidic"},
                          {"id": "c",
                           "label": "A hydroxide; the solution is neutral"}],
              # ⚑ Opens with the option's own words, as all fifteen cards
              # in the unit do. Design's draft opened "An oxide, and the
              # solution is alkaline", which names the choice in substance but
              # not verbatim; `r_predict_cards` asserts the reveal names one
              # of the buttons under it, and the assertion is right.
              "answer": "An oxide; the solution is alkaline. Metals form "
                        "oxides that are bases; non-metals form oxides that "
                        "are acidic. Group 2 period 3 is magnesium, which "
                        "burns with a brilliant white flame to give magnesium "
                        "oxide — a base you have already used to make a "
                        "salt."},
         ],
         "close_id": "file-close",
         "close_title": "You have just described four elements you were told "
                        "almost nothing about.",
         "close": [
             "One number — the group — was enough to say how each would "
             "react, what it would react with, and roughly how hard. That is "
             "what the periodic table is for. It is not a list of the "
             "elements; it is a machine for predicting elements you have "
             "never met.",
         ]},

        # ── #s-uses — three judgements. `predict-cards`, placement 5 of 5.
        {"type": "predict-cards", "id": "uses-three", "anchor": "s-uses",
         "eyebrow": "Three uses · unreactive is the point",
         "heading": "Why anyone pays for a gas that does nothing",
         "demand": "judge",
         "head_counter": {"format": "{n} of {total} decided", "start": 0,
                          "total": 3},
         "items": [
             {"id": "v1",
              "q": "Airships and weather balloons are filled with helium. "
                   "Hydrogen is lighter and cheaper. Why is helium used?",
              "options": [{"id": "a", "label": "Helium lifts more"},
                          {"id": "b", "label": "Hydrogen burns"},
                          {"id": "c", "label": "Hydrogen leaks faster"}],
              "answer": "Because hydrogen burns and helium cannot. Hydrogen "
                        "does give slightly more lift, and it is far cheaper "
                        "— but a hydrogen airship is a bomb waiting for a "
                        "spark, as the Hindenburg demonstrated in 1937. "
                        "Paying more for the gas that will not react is the "
                        "entire point."},
             {"id": "v2",
              "q": "The inside of a filament light bulb is filled with argon "
                   "rather than air. Why?",
              "options": [{"id": "a", "label": "Argon conducts electricity"},
                          {"id": "b",
                           "label": "Argon stops the filament burning away"},
                          {"id": "c",
                           "label": "Argon makes the light brighter"}],
              "answer": "Argon stops the filament burning away. The filament "
                        "runs white hot, and in air it would react with "
                        "oxygen and burn through in seconds. Argon surrounds "
                        "it with something that will not react at any "
                        "temperature the bulb reaches. The same trick shields "
                        "a weld from the air."},
             {"id": "v3",
              "q": "Neon signs glow orange-red. Is the neon reacting?",
              "options": [{"id": "a", "label": "Yes, it burns"},
                          {"id": "b",
                           "label": "No — the atoms are excited by "
                                    "electricity and give out light"},
                          {"id": "c", "label": "Yes, with the glass"}],
              "answer": "No — the atoms are excited by electricity and give "
                        "out light. Passing a current through the gas pushes "
                        "its electrons into higher energy levels; when they "
                        "drop back they release the energy as light. Nothing "
                        "is used up and nothing new is made, which is why a "
                        "neon tube can run for decades. The colour is a "
                        "physical process, not a chemical one."},
         ]},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Noble gas", "Full outer shell", "Unreactive", "Inert",
                   "Excitation"]},

        {"type": "misconception", "id": "think-commit-gas",
         "anchor": "s-think", "targets": "PTAB-09"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "key_facts": [
        {"id": "group-is-outer-electrons", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "The group number is the number of outer electrons. Group 0 "
                 "has a full outer shell, so it reacts with nothing — and "
                 "that one fact is why every group has the family "
                 "resemblance it does."},
    ],

    "ladder": {
        # index 2 — moved from Design's 0. Option texts unchanged.
        "recall": {
            "q": "Why are the group 0 elements unreactive?",
            "options": [
                "They are gases, and gases are too spread out to react",
                "Their atoms are too heavy to move",
                "Their outer shell of electrons is already full",
                "They have no electrons at all",
            ],
            "answer": 2,
            "feedback": {
                0: "Fluorine and oxygen are gases and both react ferociously. "
                   "Being a gas is not the reason.",
                1: "Helium is the second lightest element there is, and just "
                   "as unreactive as the heavy ones.",
                3: "Every atom has electrons. Group 0 atoms have a complete "
                   "outer shell of them.",
            }},

        # index 1 — moved from Design's 0. Option texts unchanged.
        "apply": {
            "q": "What does an element's group number tell you about its "
                 "atoms?",
            "options": [
                "How many electrons the atom has in total",
                "How many electrons are in the outer shell",
                "How many shells the atom has",
                "How heavy the atom is",
            ],
            "answer": 1,
            "feedback": {
                0: "That is the atomic number. Chlorine has 17 electrons in "
                   "total but 7 in its outer shell.",
                2: "That is the period number, read down the side of the "
                   "table.",
                3: "Mass increases across a period as well as down a group — "
                   "the group number says nothing about it directly.",
            }},

        "explain": {
            "q": "Explain why elements in the same group react in similar "
                 "ways, using group 1 and group 0 as your two examples.",
            "field_label": "Your explanation",
            "placeholder": "Elements in the same group have…",
            "success": [
                "Says elements in a group have the same number of outer "
                "electrons.",
                "Says it is the outer electrons that take part in reactions.",
                "Says group 1 atoms all have one outer electron to lose, so "
                "they all react in the same way.",
                "Says group 0 atoms all have a full outer shell, so none of "
                "them react.",
                "Says this is why one member of a group predicts the "
                "behaviour of the rest.",
            ]},

        "produce": {
            "q": "A new element is made in a laboratory and placed in "
                 "group 1, period 8. Predict three things about it — and then "
                 "explain why the prediction is harder to trust than the one "
                 "you made for rubidium.",
            "field_label": "Your answer",
            "placeholder": "It should be a soft metal that…",
            "success": [
                "Predicts a soft metal with one outer electron.",
                "Predicts it reacts with water to give a hydroxide and "
                "hydrogen.",
                "Predicts it is more reactive than every element above it in "
                "the group.",
                "Says the prediction relies on the trend continuing beyond "
                "where it has been tested.",
                "Notes that only a few atoms of such elements are ever made, "
                "and they decay in moments, so the prediction may never be "
                "checked.",
            ]},
    },

    "key_note": "Group 0, the noble gases, have full outer shells of "
                "electrons and so are almost completely unreactive. The group "
                "number of any element tells you how many electrons are in "
                "its outer shell, and that number is the reason elements in "
                "the same column react in the same way. Being unreactive is "
                "useful: it is why argon fills light bulbs and helium fills "
                "airships.",

    "stretch": [
        {"type": "explainer", "id": "bartlett-1962",
         "text": "“Reacts with nothing” turned out to be slightly "
                 "too strong. In 1962 Neil Bartlett persuaded xenon — the "
                 "biggest of the ordinary noble gases, whose outer electrons "
                 "are furthest from the nucleus and least tightly held — to "
                 "form a compound with a platinum fluoride, and a shelf of "
                 "xenon compounds followed. Nothing has ever been made from "
                 "helium or neon. The rule survives with a footnote, which is "
                 "what usually happens to good rules."},
        # ⚑ FLAG 18, RE-AUTHORED (R4). The fact and the contrast are kept in
        # full; the two editorial lines are cut and the seam closed as a
        # sentence. See the docstring.
        {"type": "explainer", "id": "helium-escapes",
         "text": "Helium is the only element on Earth that genuinely gets "
                 "away. It is made underground by the slow radioactive decay "
                 "of heavy elements and collected as a by-product of natural "
                 "gas, and once it is released it is light enough to leave "
                 "the atmosphere altogether — there is no getting it back. It "
                 "is also the only coolant cold enough for the "
                 "superconducting magnets in an MRI scanner. An element that "
                 "cannot be manufactured, cannot be recovered and cannot be "
                 "substituted is a genuinely finite thing, and helium is the "
                 "clearest example of one in the whole table."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Noble gas",
         "definition": "One of the group 0 elements — a colourless gas with a "
                       "full outer shell, which reacts with almost nothing.",
         "note": "Helium, neon, argon, krypton, xenon."},
        {"term": "Full outer shell",
         "definition": "An outer shell with no space left in it, so the atom "
                       "has no electron to lose and no room to gain one.",
         "note": "Eight electrons, except helium, which manages it with two."},
        {"term": "Unreactive",
         "definition": "Takes part in few reactions or none at all.",
         "note": "Not the same as useless — that is the whole of #s-uses."},
        {"term": "Inert",
         "definition": "Another word for unreactive, used especially of a gas "
                       "put somewhere to keep air out.",
         "note": "The argon in a light bulb is doing an inert job."},
        {"term": "Excitation",
         "definition": "Pushing an atom's electrons to a higher energy level, "
                       "so that they give out light when they drop back.",
         "note": "What a neon sign does. It is physics, not a reaction."},
    ],

    "safety_note": "",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why a full shell means no reaction?",
              "cta": "Ask about this lesson",
              "anchor": "s-shells"},

    "ks4_becomes": "Electron configurations written out shell by shell, ionic "
                   "bonding as the transfer of outer electrons, and the noble "
                   "gas structure as the target both sides are aiming at.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
