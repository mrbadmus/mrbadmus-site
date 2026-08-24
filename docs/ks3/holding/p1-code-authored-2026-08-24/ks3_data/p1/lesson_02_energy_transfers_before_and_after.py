"""P1 L2 — Energy transfers: before and after (MODEL).

p1-01 gave the student five nouns. This lesson gives them the sentence:
*this store went down, that store went up.* Nothing else. It is deliberately
the shortest sentence in the unit, because it is the one every later lesson
has to be able to lean on.

── ⚖️ THE SCIENCE RULING THIS LESSON IS BUILT ON ────────────────────────

**Describe the two ends. Do not narrate the middle.** `KS3.P.CIS.02` asks for
a comparison of the starting conditions with the final conditions; it does not
ask for a story about what the energy did on the way, and the story is where
every wrong idea gets in ("the energy turns into", "the energy travels along
the wire and becomes"). So the bench has a BEFORE column and an AFTER column
and no middle column at all, and the account it reveals is always two
sentences of the same shape.

**Gravity is a force, not a supply.** `ENER-10` is the misconception this
lesson is built to kill, and it is the most commonly held wrong idea in the
whole of KS3 energy: a falling object is thought to be GETTING energy FROM
gravity, as though gravity were a tank. It is not. The gravitational store was
filled when the object was lifted — by whoever lifted it — and falling empties
it again. Gravity is what makes the emptying happen; it is not what is in the
store, and it does not go down when the store does.

⚠️ **The store belongs to the object AND the Earth.** The bench says so on the
one row where it matters and the confrontation says it in full. A student who
places the store inside the falling object alone cannot answer "filled by
what?" and will reach for gravity, which is exactly how `ENER-10` forms.

── The six processes are the bullet's own six ──────────────────────────

`KS3.P.ECT.03` lists them: "changing motion, dropping an object, completing an
electrical circuit, stretching a spring, metabolism of food, burning fuels".
The bench has six rows and they are those six, in that order. Nothing was
added to make a better bench and nothing was dropped to make a shorter one.

── The pathway is NAMED but is not the answer ──────────────────────────

Each account ends with a `by` line naming which of the four pathways carried
it, because p1-01 taught the word and a lesson that then never used it has
taught vocabulary rather than physics. It is the third line of the account and
never the thing the student is asked to commit to — one commitment per row.
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    "slug":        "energy-transfers-before-and-after",
    "title":       "Energy transfers: before and after",
    "discipline":  "physics",
    "unit":        "energy-transfers",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.P.CIS.02b` is the comparison method; `KS3.P.ECT.03` is the list of
    # processes the bench runs. Two statements, one lesson — permitted by
    # §4.4 rule 3, which forbids one statement in two lessons and not this.
    "covers":      ["KS3.P.CIS.02b", "KS3.P.ECT.03"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires":    ["energy-stores"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   [],
    "connects_heading": "Next in this unit",

    # ⊕ Authored so the page keeps its own 160-character summary
    # rather than a truncated `big_question` (MRB-257 audit 6.12).
    "meta_description": "Describe any change by naming the store that went down and "
                        "the store that went up. And why gravity is a force, not a "
                        "store.",

    "big_question": "A conker falls off a tree and speeds up all the way "
                    "down. Something had to go down for its speed to go up. "
                    "Most people say gravity. Gravity is not a store.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops. The bench carries six commitments and is the whole middle of
    # the lesson; splitting it would be two instruments asking one question.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The falling conker", "done_when": "committed"},
        {"anchor": "s-ba",     "short": "BEFORE/AFTER",
         "label": "Six changes, accounted for",
         "done_when": "all_six_accounted"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Where the falling comes from", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "It leaves the branch at nothing and hits the ground at "
                 "about twenty miles an hour.",
        "prompt": "A conker sits on a branch all summer doing nothing. The "
                  "stalk gives way and a second later it is moving fast "
                  "enough to dent a car roof. Nobody pushed it and nothing "
                  "was added to it.",
        "commit": "Its kinetic store filled on the way down. Which store "
                  "emptied to fill it?",
        "options": [
            "Gravity's store, which is what gravity is for",
            "The gravitational store, which was filled when the tree grew "
            "the conker up there",
            "The conker's own chemical store, used up as it fell",
            "No store emptied — falling is free",
        ],
        "reveal": "The gravitational store — and the tree filled it, over "
                  "weeks, using its own chemical store to build the conker "
                  "high up rather than on the ground. Gravity is not a store "
                  "and never was. It is the force that let the store empty "
                  "once the stalk gave way.",
    },

    "misconceptions": [
        {"id": "ENER-10",
         "statement": "A falling object gains energy from gravity, which "
                      "supplies it.",
         "elicited_by": "think-commit-gravity",
         "confronted_by": "think-commit-gravity"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every change in physics can be written the same way. Look "
                 "at the situation before. Look at the situation after. Say "
                 "which store went down and which store went up. That is the "
                 "whole sentence, and the amount that left one is the amount "
                 "that arrived at the other."},

        {"type": "rule", "id": "the-sentence",
         "eyebrow": "The sentence",
         "statement": "One store went down. Another store went up. By the "
                      "same amount.",
         "close": "That is the whole account. Everything else — the pushing, "
                  "the burning, the current — is how it got from the first "
                  "to the second."},

        # #s-ba — the flagship. Ink-dark practical.
        {"type": "before-after-bench", "id": "six-changes", "anchor": "s-ba",
         "eyebrow": "At the bench · six changes",
         "heading": "Two moments, and the difference between them",
         "head_counter": {"format": "{n} of 6 accounted for", "total": 6},
         "demand": "investigate",
         "targets": "ENER-10",
         "prompt": "Pick a change. Read the before and the after. Commit to "
                   "which store emptied, then open the account.",
         "gate": {"prompt": "Commit first. In every one of the six changes "
                            "below, how does the total amount of energy after "
                            "compare with the total before?",
                  "options": ["It is always less, because some is used up",
                              "It is always the same",
                              "It is always more, because the change adds "
                              "some",
                              "It depends which change you pick"]},
         "stores": [
             {"id": "kinetic", "label": "Kinetic"},
             {"id": "thermal", "label": "Thermal"},
             {"id": "gravitational", "label": "Gravitational"},
             {"id": "elastic", "label": "Elastic"},
             {"id": "chemical", "label": "Chemical"},
         ],
         "commit_prompt": "Which store empties?",
         "labels": {"before": "BEFORE", "after": "AFTER",
                    "down": "The store that emptied",
                    "up": "The store that filled",
                    "by": "Carried by"},
         "resting": "Pick a change to read it.",
         # The six are `KS3.P.ECT.03`'s own six, in the bullet's own order.
         "changes": [
             {"id": "motion", "label": "Changing motion",
              "scene": "A cyclist pushes off from a standstill and gets up "
                       "to speed along a flat road.",
              "before": "Stopped. Her muscles are full of the glucose her "
                        "breakfast turned into.",
              "after": "Moving at 6 metres per second. Less glucose in the "
                       "muscles, and she is slightly warmer.",
              "down": "chemical", "up": "kinetic",
              "by": "a force moving something",
              "note": "The chemical store in her muscles emptied. Most of "
                      "what left it went to her kinetic store; the rest "
                      "warmed her, which is why cycling makes you hot."},
             {"id": "dropping", "label": "Dropping an object",
              "scene": "A conker falls from a branch four metres up.",
              "before": "Still, four metres above the ground.",
              "after": "Moving fast, at ground level.",
              "down": "gravitational", "up": "kinetic",
              "by": "a force moving something",
              "note": "The gravitational store belongs to the conker AND the "
                      "Earth together, and it empties as the gap between "
                      "them closes. Gravity is the force that does the "
                      "emptying. It is not the thing that emptied."},
             {"id": "circuit", "label": "Completing an electrical circuit",
              "scene": "A torch is switched on and left on until the cell "
                       "goes flat.",
              "before": "A fresh cell. Dark room.",
              "after": "A flat cell. A room that is very slightly warmer.",
              "down": "chemical", "up": "thermal",
              # ⊖ CORRECTED. Two pathways run here and the row named one. The
              # current carries it out of the cell; radiation carries it from
              # the bulb to the walls, which is what the note already says.
              "by": "an electric current, then radiation",
              "note": "The cell's chemical store emptied. Nothing stored the "
                      "light: it crossed the room, landed on the walls, and "
                      "filled their thermal store. The current was the route, "
                      "not the thing that emptied."},
             {"id": "spring", "label": "Stretching a spring",
              "scene": "You pull a spring out to twice its length and hold "
                       "it there.",
              "before": "A loose spring lying on the bench.",
                "after": "The same spring at twice its length, held.",
              "down": "chemical", "up": "elastic",
              "by": "a force moving something",
              "note": "Your muscles' chemical store emptied and the spring's "
                      "elastic store filled. Let go and it runs backwards — "
                      "the elastic store empties into a kinetic one."},
             {"id": "food", "label": "Metabolism of food",
              "scene": "A runner eats a banana at the start of a race and "
                       "runs for twenty minutes.",
              "before": "A banana. A runner at rest.",
              "after": "No banana. A runner who is moving and noticeably hot.",
              "down": "chemical", "up": "thermal",
              # ⊖ CORRECTED. This row named THERMAL as the store that filled
              # and `a force moving something` as the route — and that route
              # is the one that fills a KINETIC store. The pathway now matches
              # the store the row declares.
              "by": "heating",
              "note": "The banana's chemical store emptied. A little went to "
                      "her kinetic store, through her legs pushing on the "
                      "ground; most of it warmed her muscles, and heating "
                      "carried that out to her skin and the air. That is why "
                      "a runner is hot and why the air around her is too."},
             {"id": "fuel", "label": "Burning fuels",
              "scene": "A gas hob heats a pan of water from cold to boiling.",
              "before": "A gas supply, and a pan of water at 20 degrees.",
              "after": "Less gas. Water at 100 degrees, and a warm kitchen.",
              "down": "chemical", "up": "thermal",
              "by": "heating",
              "note": "The gas and the oxygen it burns with are the chemical "
                      "store. It empties into the pan's thermal store, and "
                      "into the kitchen's, which is the part nobody wanted."},
         ],
         "close": [
             "Six changes, six sentences, and every one has the same shape: "
             "one store down, one store up.",
             "Four of the six empty a chemical store, which is worth "
             "noticing. Almost everything a person or a machine does starts "
             "there.",
         ]},

        {"type": "key-fact", "ref": "down-then-up"},

        # ⚑ The discrimination `ENER-10` turns on, held side by side rather
        # than argued in prose. Two columns, four rows, and the last row is
        # the one that decides it.
        {"type": "comparison", "id": "force-or-store",
         "eyebrow": "The one that catches everybody",
         "eyebrow_tone": "accent-text",
         "statement": "Gravity is one thing. The gravitational store is "
                      "another.",
         "ground": "band",
         "columns": [
             {"caption": "Gravity", "tone": "on-dark"},
             {"caption": "The gravitational store", "tone": "on-dark"},
         ],
         "row_tones": ["ink", "ink"],
         "rows": [
             {"name": "What it is",
              "cells": ["A force, measured in newtons.",
                        "An amount of energy, measured in joules."]},
             {"name": "Whose it is",
              "cells": ["It acts between the object and the Earth.",
                        "It belongs to the object and the Earth together, "
                        "and to the gap between them."]},
             {"name": "Does it run out?",
              "cells": ["No. It is the same at the top and at the bottom.",
                        "Yes. It empties as the object comes down and fills "
                        "as it goes up."]},
             {"name": "In a fall",
              "cells": ["It is what makes the store empty.",
                        "It is what empties."]},
         ]},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Four words",
         "lead": "Say your answer out loud before you turn each card over.",
         "terms": ["Transfer", "System", "Gravitational store",
                   "Chemical store"]},

        {"type": "misconception", "id": "think-commit-gravity",
         "anchor": "s-think", "targets": "ENER-10"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "key_facts": [
        {"id": "down-then-up",
         "text": "Every change moves energy from one store to another. Name "
                 "the store that went down and the store that went up, and "
                 "you have described the change completely.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    "vocabulary": [
        {"term": "Transfer",
         "definition": "Energy moving from one store to another.",
         "note": "Nothing is created and nothing is destroyed in a transfer. "
                 "What leaves one store arrives somewhere else."},
        {"term": "System",
         "definition": "Everything you have decided to include when you "
                       "compare the before and the after.",
         "note": "Draw the line too small and energy appears to vanish. The "
                 "conker's system has to include the Earth."},
        {"term": "Gravitational store",
         "definition": "The store that fills when an object and the Earth "
                       "are moved further apart, and empties when they come "
                       "closer.",
         "note": "It is not gravity, and it does not belong to the object on "
                 "its own."},
        {"term": "Chemical store",
         "definition": "The store held by a set of substances because of "
                       "which substances they are.",
         "note": "Fuel, food and a cell are all chemical stores. Four of the "
                 "six changes on this page empty one."},
    ],

    "activities": [
        {"id": "think-commit-gravity",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-10",
         "prompt": "An astronaut on the Moon drops a hammer and it falls, "
                   "slowly. Gravity there is about a sixth of ours. Commit "
                   "before you read on.",
         "options": [
             "Gravity supplies the energy, so the Moon supplies less of it",
             "The hammer gets its energy from its own weight",
             "Gravity supplies nothing; a store was filled when it was lifted",
             "Nothing empties at all, because the Moon has no atmosphere",
         ],
         "reveal": [
             "Gravity supplies nothing, on the Moon or here. It is a force, "
             "and a force is not an amount of energy — it is measured in "
             "newtons and a store is measured in joules. Asking how much "
             "energy gravity has is like asking how many metres a kilogram "
             "is.",
             "What actually filled the store was the astronaut, when she "
             "lifted the hammer. She emptied a chemical store in her muscles "
             "to do it, and the gravitational store she filled is smaller on "
             "the Moon than it would be here — because lifting is easier "
             "there. She gets back exactly what she put in, which is why the "
             "hammer falls slowly.",
         ]},
    ],

    "ladder": {
        "recall": {
            "q": "A ball is rolling along a flat floor and slowly comes to a "
                 "stop. Which store empties?",
            "options": [
                "Gravitational",
                "Kinetic",
                "Elastic",
                "Chemical",
            ],
            "answer": 1,
            "feedback": {
                0: "The ball stays on the floor throughout, so its height "
                   "never changes and no gravitational store moves.",
                2: "Nothing is stretched, squashed or bent, so no elastic "
                   "store is involved.",
                3: "No substance is reacting. The store that empties is the "
                   "one to do with movement.",
            }},
        "apply": {
            "q": "A bungee jumper has just reached the lowest point of the "
                 "jump and is momentarily still. Comparing that moment with "
                 "the moment she stepped off the platform, which store has "
                 "filled the most?",
            "options": [
                "Kinetic, because she has been moving fast",
                "Chemical, because jumping is hard work",
                "Elastic, in the stretched cord",
                "Gravitational, because she has moved a long way",
            ],
            "answer": 2,
            "feedback": {
                0: "She is still at that instant, so her kinetic store is "
                   "empty. It filled and then emptied again on the way down.",
                1: "Nothing is reacting. She stepped off; no chemical store "
                   "was filled by falling.",
                3: "She has moved a long way DOWN, so her gravitational "
                   "store has emptied, not filled.",
            }},
        "explain": {
            "q": "A student writes: \"The car speeds up because the engine "
                 "gives it energy, and it slows down because the energy is "
                 "used up by friction.\" Rewrite both halves as before-and-"
                 "after sentences, naming the stores.",
            "field_label": "Your two sentences",
            "placeholder": "Speeding up: the chemical store in…",
            "success": [
                "Speeding up: names the chemical store in the fuel as the "
                "one that empties.",
                "Speeding up: names the kinetic store as the one that fills.",
                "Slowing down: names the kinetic store as the one that "
                "empties.",
                "Slowing down: names a thermal store — of the brakes, the "
                "tyres, the road or the air — as the one that fills.",
                "Says that nothing is used up: the energy is still there, in "
                "a store nobody wanted it in.",
            ]},
        "produce": {
            "q": "Write the before-and-after account for a firework: from the "
                 "moment it is lit on the ground to the moment the last spark "
                 "goes out. Name every store that changes, in the order it "
                 "changes, and say which pathway carries each transfer.",
            "field_label": "Your account",
            "placeholder": "Before: an unlit firework on the ground…",
            "success": [
                "Starts with a chemical store in the gunpowder.",
                "Names a kinetic store filling as it is pushed upwards.",
                "Names a gravitational store filling as it rises.",
                "Names a thermal store filling — the air, the case and the "
                "sparks are all hot.",
                "Names at least two different pathways, and does not call "
                "light or sound a store.",
            ]},
    },

    "key_note": "Compare the situation before with the situation after, and "
                "say which store went down and which went up. Gravity is a "
                "force, not a store: a falling object empties a "
                "gravitational store that was filled when something lifted "
                "it.",

    "stretch": [
        {"type": "explainer", "id": "where-you-draw-the-line",
         "text": "Where you draw the edge of the system decides whether your "
                 "account balances. Take just the conker and energy appears "
                 "from nowhere. Take the conker and the Earth and it balances "
                 "exactly. Take the cyclist alone and she seems to lose "
                 "energy for no reason; take the cyclist, the bike, the road "
                 "and the air and nothing is missing. Physicists choose the "
                 "line on purpose, and choosing it badly is the single most "
                 "common way an energy account comes out wrong."},
    ],

    "support": [],

    "safety_note": "",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why gravity is not a store?",
              "cta": "Ask about this lesson",
              "anchor": "s-ba"},

    "ks4_becomes": "Energy transfers described quantitatively, and the "
                   "kinetic and gravitational equations used to check that an "
                   "account balances.",

    "ws": ["analysis-and-evaluation"],

    "review_state": "draft",
}
