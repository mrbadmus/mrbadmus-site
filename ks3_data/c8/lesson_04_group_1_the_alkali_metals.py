"""C8 L4 — Group 1: the alkali metals (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c8/c8-04-group-1-the-alkali-metals.dc.html`, and her
author's notes `NOTES-C8.md` §1, §3, §4, §5 flags 10–13, §6 (`PTAB-07`) and §7.

── THE ARCHETYPE IS MODEL, AND DESIGN'S "PATTERN" IS NOT A FAMILY ───────

Design's README labels this lesson PATTERN and c8-06 APPLY. **Neither is one of
the seven architecture families** (§6: MODEL, PROCESS, SYSTEM, CONTRAST,
CLASSIFY, QUANTITATIVE, INVESTIGATION), and `structure.py` takes only those.
They are mapped by RHYTHM, which is what §6 says a family is:

    c8-04  PATTERN → MODEL      one idea — the outer electron's distance from
                                the nucleus — explains a whole column's
                                behaviour, driven by a flagship parameter
                                instrument with a predict-gate at each step
    c8-05  PATTERN → CONTRAST   two groups, one discriminating difference: the
                                DIRECTION of the trend. CONTRAST also carries
                                the heaviest rung 3, which suits the lesson
                                that breaks the rule
    c8-06  APPLY   → MODEL      one idea — a full outer shell — explains
                                behaviour where there is no series to
                                extrapolate along

── ⭐ THIS LESSON BUILDS THE TREND THAT THE NEXT ONE BREAKS ─────────────

`PTAB-08` is the unit's most valuable register entry and it does not exist
without this pair. c8-04 establishes "reactivity increases going down a group"
on a trough the student runs three times; c8-05 hands them a grid where it runs
the other way. Merging the two (§7's plan) would turn the reversal into a
sentence. That is the argument that kept three group lessons (MRB-281, R1).

── ⚑ FLAG 11 · THERE IS NO DENSITY TREND, AND SAYING SO IS NOW A CHECK ──

Lithium 0.53, sodium 0.97, potassium 0.86. **That is not monotonic**, so
"denser going down" is false and "less dense going down" is equally false.
Design's NOTES §5 flag 11 asked for the omission to be confirmed. The
commander's ruling (R4) UPGRADED it from an omission to a positive
instruction: NO SENTENCE ANYWHERE MAY IMPLY A DENSITY TREND.

So it is asserted rather than remembered. `r_water_trough` walks every
headline, observation, lead and closing paragraph SENTENCE BY SENTENCE and
fails the build where a density word and a direction word appear in one
sentence. Sentence grain, not blob grain, deliberately: "they all float" and
"reactivity increases down the group" are both true and belong in one
paragraph, and a cruder check would have forbidden the honest version.

What the lesson says instead is the true thing — all three float — and that is
all it says.

── ⚑ ORDER IS DATA (the C5 ruling, carried) ─────────────────────────────

Design's `METALS` array carries no `rank`; the array ORDER is the trend. This
build authors `rank: 0, 1, 2` explicitly and `r_water_trough` reads the order
off it, refusing gaps and ties. Re-sorting the payload for layout therefore
cannot re-teach the group. Same ruling C5-04 asked for and C8-05 depends on.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

This lesson holds **index 3** (recall) and **index 2** (apply); Design put both
at 0. Only the order moves — no option text is changed on either rung, because
both already pass MRB-177 (recall runs 5/5/4/5 words; apply runs 15/9/12/9,
longest by three and 1.25x).

── SCIENCE FLAGS ────────────────────────────────────────────────────────

⚑ Flag 10 — the trend explained by atomic size and the outer electron's
distance. KEPT (R4), in the stretch layer, and it is the mechanism that makes
c8-05's reversal predictable rather than arbitrary.

⚑ Flag 11 — melting points lithium 180 °C, sodium 98 °C, potassium 63 °C.
KEPT and correct. Sodium's 98 °C is load-bearing: it is why the ball melts,
which is the whole of `PTAB-07`.

⚑ Flag 12 — potassium's lilac flame and possible spitting. KEPT, correct, and
the spitting is why the apparatus line is on this lesson.

⚑ Flag 13 — the rubidium predictions are extrapolations and are flagged as
such on the page ("You have never seen it and you can still describe it").
KEPT — that IS the lesson, and `PT.04a` is exactly the skill.

⊕ `ENER-03` from C7 reappears here — `reappears_in` is recorded on C7's own
record, pointing at this slug. `PTAB-07` and `ENER-03` are both heat coming OUT
of a reaction read as heat that went IN, elicited by different phenomena, and
they stay separate.
"""

LESSON = {
    "slug":  "group-1-the-alkali-metals",
    "title": "Group 1 — the alkali metals",
    "discipline": "chemistry",
    "unit": "The periodic table",
    "family": "MODEL",

    "covers": ["KS3.C.PT.04a"],
    "touches": ["KS3.C.PT.03a", "KS3.C.PT.05"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3},
                {"id": "energy", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    "requires": ["groups-and-periods"],
    "assumes": [],
    "references": ["acids-and-alkalis", "exothermic-reactions",
                   "the-ph-scale-and-indicators"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "Cut a lump of sodium and the fresh surface is a mirror "
                    "for about four seconds, then dulls while you watch. "
                    "Nothing touched it. What is attacking it?",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "Four seconds of shine", "done_when": "committed"},
        {"anchor": "s-trough",  "short": "TROUGH",
         "label": "The water trough",   "done_when": "all_three_run"},
        {"anchor": "s-predict", "short": "PREDICT",
         "label": "Three predictions",  "done_when": "all_three_predicted"},
        {"anchor": "s-think",   "short": "THINK",
         "label": "Why the ball melted", "done_when": "committed"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",     "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A lump of sodium is kept in a jar of oil. Lift it out and "
                 "it is dull grey. Cut it and the cut surface is a mirror — "
                 "for about four seconds.",
        "prompt": "The shine dulls while you watch. Nothing touched it, "
                  "nothing was added, and the room is at ordinary "
                  "temperature.",
        "commit": "What is happening to the fresh surface?",
        "options": [
            "It is drying out as the oil evaporates off it",
            "It is reacting with the oxygen in the room",
            "It is cooling down and losing its shine",
            "The knife left a film of metal dust on it",
        ],
        "reveal": "It is reacting with the oxygen in the room. Sodium is "
                  "reactive enough that plain air is an attack: the shiny "
                  "metal is turning into a dull layer of sodium oxide within "
                  "seconds of being exposed. That is also why it lives under "
                  "oil — the oil keeps air and water off it. <strong>The "
                  "whole of group 1 behaves like this, and it gets worse as "
                  "you go down.</strong>",
    },

    "misconceptions": [
        {"id": "PTAB-07",
         "statement": "Sodium melted because the water was hot.",
         "elicited_by": "think-commit-melt",
         "confronted_by": "think-commit-melt"},
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
        {"id": "think-commit-melt",
         "kind": "predict",
         "demand": "explain",
         "targets": "PTAB-07",
         "prompt": "The water was straight from the tap. Commit before you read"
                    " on.",
         # ⚑ MRB-177 / MRB-278 — THE DISTRACTORS ARE RE-AUTHORED AND THE
         # CORRECT OPTION IS UNTOUCHED. Design's set gave the answer away on
         # length alone, which turns a commitment device into a shape puzzle:
         # a student picks the long one, never commits to the belief, and is
         # therefore never confronted with it. Each distractor now states its
         # wrong RULE at full length, which is what MRB-177 asks for.
         # 13, 15, 13, 13 words.
         "options": [
             "Right — water straight from the tap could never have melted a"
             " metal",
             "Wrong — the reaction gives out the heat, and sodium melts at"
             " only 98 °C",
             "Right, because a metal only ever melts when it is heated from"
             " outside",
             "Wrong — the sodium did not melt at all, it simply dissolved"
             " away",
         ],
         "reveal": [
             "The heat came from the reaction, not from the water. Sodium"
             " reacting with water gives out energy — and sodium melts at"
             " only 98 °C, which is a low melting point for a metal. The"
             " reaction produces enough heat, fast enough, to melt the piece"
             " of sodium taking part in it.",
             "Potassium goes one step further: it releases the same energy"
             " even faster, and the hydrogen being produced catches fire in"
             " it. <strong>The ball of molten metal is evidence about the"
             " reaction, not about the trough.</strong>",
         ]},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Group 1 is the first column: lithium, sodium, potassium and "
                 "three more below them. They are all soft, all light enough "
                 "to float on water, and all far too reactive to exist as the "
                 "metal anywhere in nature."},
        {"type": "explainer",
         "text": "They are called the <strong>alkali metals</strong> because "
                 "of what they leave behind. Drop one into water and it makes "
                 "a hydroxide, which dissolves — and a dissolved hydroxide is "
                 "an alkali: metal + water → metal hydroxide + hydrogen."},

        # ── #s-trough — three metals, one at a time. Light block → `check`.
        {"type": "water-trough", "id": "trough-three", "anchor": "s-trough",
         "eyebrow": "Your turn · the water trough",
         "heading": "One small piece, one trough of water, indicator already "
                    "added.",
         "demand": "predict",
         "resting": "Choose a metal, predict, then drop it in.",
         "head_counter": {"format": "{n} of {total} run", "start": 0,
                          "total": 3},
         "predict_prompt": "Predict before you drop it in.",
         "predict_options": [
             {"id": "calm",     "label": "A steady fizz"},
             {"id": "fast",     "label": "Fast enough to melt"},
             {"id": "fire",     "label": "It catches fire"},
         ],
         # ⚠️ RANK, NOT ARRAY POSITION. See the docstring.
         "metals": [
             {"id": "li", "name": "Lithium", "rank": 0,
              "data": "melts at 180 °C · floats",
              "headline": "A steady fizz that lasts nearly a minute.",
              "obs": ["Floats on the surface and stays as a solid lump.",
                      "Fizzes steadily, giving off hydrogen from all over its "
                      "surface.",
                      "Gradually gets smaller and disappears.",
                      "The indicator turns purple: the solution left behind "
                      "is alkaline."],
              "eq_right": "lithium hydroxide + hydrogen"},
             {"id": "na", "name": "Sodium", "rank": 1,
              "data": "melts at 98 °C · floats",
              "headline": "Melts into a ball and skates across the surface.",
              "obs": ["Floats, then melts into a silver ball within a second "
                      "or two.",
                      "Whizzes around the surface, pushed by the hydrogen "
                      "streaming off it.",
                      "Fizzes hard and may finish with an orange flame.",
                      "The indicator turns purple: sodium hydroxide has "
                      "formed."],
              "eq_right": "sodium hydroxide + hydrogen"},
             {"id": "k", "name": "Potassium", "rank": 2,
              "data": "melts at 63 °C · floats",
              "headline": "Sets fire to its own hydrogen. Lilac flame, and "
                          "sometimes a bang at the end.",
              "obs": ["Melts instantly and moves faster than the sodium did.",
                      "The hydrogen catches fire, burning with a lilac flame.",
                      "Can crack or spit at the end of the reaction.",
                      "The indicator turns purple: potassium hydroxide has "
                      "formed."],
              "eq_right": "potassium hydroxide + hydrogen"},
         ],
         "close_id": "trough-close",
         "close_title": "All three did the same thing. Only the violence "
                        "changed.",
         "close": [
             "Every one of them floated, fizzed, produced hydrogen and left "
             "an alkaline solution behind. That sameness is what a group is. "
             "What changes going down the column is how hard the reaction is "
             "pushed: lithium steady, sodium fast enough to melt itself, "
             "potassium hot enough to set its own hydrogen alight.",
             "<strong>Reactivity increases going down group 1.</strong>",
         ]},

        {"type": "key-fact", "ref": "hydroxide-and-hydrogen"},

        # ── #s-predict — rubidium. `predict-cards`, placement 3 of 5.
        {"type": "predict-cards", "id": "predict-rubidium",
         "anchor": "s-predict",
         "eyebrow": "Three predictions · rubidium",
         "heading": "The next one down. You have never seen it and you can "
                    "still describe it.",
         "demand": "predict",
         "lead": "Rubidium sits directly below potassium. Commit to each "
                 "prediction before you read what actually happens.",
         "head_counter": {"format": "{n} of {total} predicted", "start": 0,
                          "total": 3},
         "items": [
             {"id": "p1",
              "q": "Will rubidium be harder or softer to cut than potassium?",
              "options": [{"id": "a", "label": "Harder"},
                          {"id": "b", "label": "Softer"},
                          {"id": "c", "label": "The same"}],
              "answer": "Softer. The group gets softer going down — lithium "
                        "is the firmest of them and each one below cuts more "
                        "easily. Rubidium is soft enough to deform under its "
                        "own weight in a warm room."},
             {"id": "p2",
              "q": "How will rubidium react with water?",
              "options": [{"id": "a",
                           "label": "Less violently than potassium"},
                          {"id": "b",
                           "label": "More violently than potassium"},
                          {"id": "c", "label": "It will not react"}],
              "answer": "More violently than potassium — the trend continues. "
                        "Rubidium reacts so fast that the hydrogen ignites "
                        "instantly and the reaction is usually described as "
                        "explosive. Caesium, one further down, shatters the "
                        "container."},
             {"id": "p3",
              "q": "What will the solution left behind do to universal "
                   "indicator?",
              "options": [{"id": "a", "label": "Turn it red"},
                          {"id": "b", "label": "Leave it green"},
                          {"id": "c", "label": "Turn it purple"}],
              "answer": "Turn it purple. It makes rubidium hydroxide, which "
                        "is a strong alkali, exactly as the other three do. "
                        "This is the part that does not change down the "
                        "group — the products are the same family every time, "
                        "and only the speed changes."},
         ]},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Six words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Alkali metal", "Hydroxide", "Alkali", "Reactivity",
                   "Trend", "Outer electron"]},

        {"type": "misconception", "id": "think-commit-melt",
         "anchor": "s-think", "targets": "PTAB-07"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "key_facts": [
        {"id": "hydroxide-and-hydrogen", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "Group 1 metals react with water to give a metal hydroxide "
                 "and hydrogen, leaving an alkaline solution. Reactivity "
                 "increases down the group."},
    ],

    "ladder": {
        # index 3 — moved from Design's 0. Option texts unchanged.
        "recall": {
            "q": "What are the products when a group 1 metal reacts with "
                 "water?",
            "options": [
                "A metal oxide and hydrogen",
                "A salt and water",
                "A metal hydroxide and oxygen",
                "A metal hydroxide and hydrogen",
            ],
            "answer": 3,
            "feedback": {
                0: "The oxide is what forms in air. In water it is the "
                   "hydroxide, which dissolves to make an alkali.",
                1: "That is neutralisation. There is no acid here.",
                2: "The gas given off is hydrogen — it pops with a lit "
                   "splint.",
            }},

        # index 2 — moved from Design's 0. Option texts unchanged.
        "apply": {
            "q": "Why is the trend in group 1 the opposite way round to what "
                 "most students expect?",
            "options": [
                "Reactivity decreases going down, because the atoms get "
                "heavier",
                "Reactivity stays the same, because they are all in the same "
                "group",
                "Reactivity increases going down, because the outer electron "
                "is further out and easier to lose",
                "The trend depends on the temperature of the water",
            ],
            "answer": 2,
            "feedback": {
                0: "Heavier does not mean less reactive: caesium is the "
                   "heaviest of the four you meet and by far the most "
                   "violent.",
                1: "Same group means the same kind of reaction, not the same "
                   "vigour.",
                3: "The order is the same in cold water, warm water and air. "
                   "It is a property of the atoms.",
            }},

        "explain": {
            "q": "A piece of sodium put on water melts into a ball within a "
                 "second. Explain where the heat came from, and why the same "
                 "thing does not happen to lithium.",
            "field_label": "Your explanation",
            "placeholder": "The heat came from…",
            "success": [
                "Says the heat is released by the reaction, not taken from "
                "the water.",
                "Says the reaction between sodium and water is exothermic.",
                "Says sodium melts at only 98 °C, which is low for a metal.",
                "Says the reaction releases enough energy fast enough to "
                "reach that temperature.",
                "Says lithium reacts more slowly and melts at 180 °C, so it "
                "never gets there.",
            ]},

        "produce": {
            "q": "Caesium is two places below potassium in group 1. Write a "
                 "description of what you would expect to see if a small "
                 "piece were dropped into water, and justify every part of "
                 "it from the trend.",
            "field_label": "Your answer",
            "placeholder": "I would expect caesium to…",
            "success": [
                "Says it would float, because all the group 1 metals do.",
                "Says the reaction would be more violent than potassium's.",
                "Says the hydrogen would ignite, or the reaction would be "
                "explosive.",
                "Says it would produce caesium hydroxide and hydrogen, the "
                "same products as the others.",
                "Justifies the violence by the outer electron being further "
                "from the nucleus and easier to lose.",
            ]},
    },

    "key_note": "The group 1 metals are soft, shiny when cut and less dense "
                "than most metals — lithium, sodium and potassium all float "
                "on water. They react with water to give a metal hydroxide "
                "and hydrogen, and the hydroxide makes the water alkaline. "
                "Reactivity increases down the group, which is why they are "
                "stored under oil.",

    "stretch": [
        {"type": "explainer", "id": "why-the-trend",
         "text": "The reason for the trend is the outer electron. Every "
                 "group 1 atom has exactly one, and reacting means losing it. "
                 "Going down the group the atoms get bigger, so that outer "
                 "electron sits further from the nucleus and is held on less "
                 "tightly — easier to lose means more reactive. The same "
                 "argument run in reverse explains why group 7 does the "
                 "opposite, which is the next lesson."},
        {"type": "explainer", "id": "never-found-as-metal",
         "text": "No group 1 metal has ever been found as the metal in "
                 "nature; they are all locked into compounds. Sodium and "
                 "potassium were only isolated in 1807, when Humphry Davy "
                 "passed electricity through their molten hydroxides — the "
                 "first time anyone had taken an element apart with a "
                 "battery. Both are now indispensable: potassium in every "
                 "fertiliser, sodium in every cell of your body, and lithium "
                 "in the battery of whatever you are reading this on."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Alkali metal",
         "definition": "One of the group 1 elements — soft, light, and "
                       "reactive enough that it is stored under oil.",
         "note": "Named for what they leave in the water, not for the metal."},
        {"term": "Hydroxide",
         "definition": "The compound a group 1 metal makes with water, which "
                       "dissolves to give an alkaline solution.",
         "note": "Sodium hydroxide, potassium hydroxide, and so on down."},
        {"term": "Alkali",
         "definition": "A soluble base. It turns universal indicator purple "
                       "and has a pH above 7.",
         "note": "C6's word, arriving again with a new source."},
        {"term": "Reactivity",
         "definition": "How readily an element takes part in a reaction, and "
                       "how vigorously it does so.",
         "note": "Not the same as how heavy or how hard it is."},
        {"term": "Trend",
         "definition": "A change that runs steadily in one direction through "
                       "a group or across a period.",
         "note": "Group 1's runs down. Group 7's does not."},
        {"term": "Outer electron",
         "definition": "The electron in the outermost shell. Group 1 atoms "
                       "have exactly one, and reacting means losing it.",
         "note": "Further out, further down the group — and easier to lose."},
    ],

    "safety_note": "Every reaction on this page is a teacher demonstration, "
                   "behind a safety screen, with the smallest piece that can "
                   "be cut and eye protection worn by everyone in the room. "
                   "Potassium can crack or spit at the end of the reaction, "
                   "which is why the screen stays up until the fizzing has "
                   "stopped. Nothing here is a class practical at any scale.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why reactivity increases downwards?",
              "cta": "Ask about this lesson",
              "anchor": "s-trough"},

    "ks4_becomes": "Explaining the trend with atomic radius and shielding, "
                   "and writing balanced and ionic equations for the "
                   "reactions with water.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
