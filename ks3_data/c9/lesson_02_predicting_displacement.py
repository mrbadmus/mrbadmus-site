"""C9 L2 — Predicting displacement (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c9/c9-02-predicting-displacement.dc.html`, and her
author's notes `NOTES-C9.md` §1, §3, §4 flags 6–9, §6 (`MATL-05`, `MATL-06`)
and §10.

── ⚑ THE STATUTORY ANCHOR IS `KS3.WS.EXP.02`, AND THAT IS A RULING ──────

This lesson teaches no new subject content by design: the series came from
c9-01 and the displacement rule from C5-04. It is where the order becomes a
PREDICTION. `NOTES-C9.md` §1 asks whether `KS3.WS.ANA.03` (identifying
patterns) would be the better anchor.

**It would not.** ANA.03 describes what the SYNTHESIS PANEL does once the deck
is sorted — one moment, at the end. EXP.02 — "make predictions using
scientific knowledge and understanding" — describes what the student does
EIGHT TIMES, one card at a time, before anything runs. The archetype is what
the student does, and so is the anchor. WS statements are exempt from
exactly-once ownership (§5.7), so nothing is displaced by the choice.

── ⚖️ NO CARD STORES ITS OWN OUTCOME ────────────────────────────────────

Each card names what is ADDED and what is INSIDE the compound, and
`_deck_happens` decides from the ranked strip printed above them. That is the
instrument's whole argument — sort the eight and the rule is the only thing
left standing — and it would be undone by a per-card `happens` flag, which
could be authored against the series the student is reading beside it. The
renderer REFUSES a payload carrying one, and checks each authored observation
against the derived outcome in both directions.

── SCIENCE FLAGS ────────────────────────────────────────────────────────

⚑ Flag 6 — ZINC IN IRON SULFATE IS REAL BUT SLOW, AND THE HEDGE IS KEPT. It
is much less obvious than the copper displacements and the observation says
so. Dropping the card would be easier and worse: it is the only card where the
two metals are ADJACENT in the series, and a rule that only works on
well-separated pairs is not the rule the lesson claims.

⚑ Flag 7 — CARBON WITH COPPER OXIDE IS IN THE DECK, AND IT BELONGS THERE.
KEPT. It is the same rule with a non-metal, it is why carbon is in the series
at all, and it previews c9-03 without teaching it.

⚑ Flag 8 — THERMITE IS NAMED AND EXPLICITLY EXCLUDED. KEPT. `NOTES-C9.md` §5.3
offers to remove it if the editorial line is "do not name what a student might
try". The line is the opposite one, and it is C8's chlorine ruling again:
naming a thing and saying plainly that it is not a school experiment at any
scale is more protective than silence, because a student who meets it
elsewhere — and they will, it is on every video site — meets it here first
with the frame attached. No temperature figure is quoted and no method is
given.

⚑ Flag 9 — sacrificial zinc anodes explained purely by position in the series,
with no electrochemistry. KEPT and correct at this level.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

This lesson holds **index 2** (recall) and **index 3** (apply); Design put
both at 0. Only the order moves and no option text is edited.
"""

LESSON = {
    "slug":  "predicting-displacement",
    "title": "Predicting displacement",
    "discipline": "chemistry",
    "unit": "Metals and materials",
    "family": "MODEL",

    # ⚑ WS anchor — see the docstring. WS statements are exempt from
    # exactly-once ownership (§5.7).
    "covers": ["KS3.WS.EXP.02"],
    "touches": ["KS3.C.MATS.01", "KS3.C.MATS.02"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    "requires": ["the-reactivity-series"],
    "assumes": [],
    "references": ["displacement", "the-reactivity-series"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "An iron nail goes into blue copper sulfate and comes out "
                    "coated in copper. Nobody added any copper. So where did "
                    "it come from — and could you have said so in advance?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The coated nail",   "done_when": "committed"},
        {"anchor": "s-rule",   "short": "RULE",
         "label": "The six and the rule", "mirrors": "s-hook",
         "done_when": "committed"},
        {"anchor": "s-deck",   "short": "DECK",
         "label": "Eight proposals",   "done_when": "all_eight_run"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Slow is not impossible", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "An iron nail is dropped into blue copper sulfate solution "
                 "and left for ten minutes.",
        "prompt": "It comes out coated in soft pink-brown copper, and the "
                  "blue of the solution has faded towards pale green. Nobody "
                  "added copper to the nail. Nobody took the nail out and "
                  "dipped it in anything.",
        "commit": "Where did the copper on the nail come from?",
        "options": [
            "It was already on the nail, under the surface",
            "It came out of the solution, pushed out by the iron",
            "The iron changed into copper where the two met",
            "The blue dye dried onto the nail and darkened",
        ],
        "reveal": "It came <strong>out of the solution</strong>. The blue "
                  "colour was copper joined to sulfate; iron is the more "
                  "reactive of the two metals, so the iron took the sulfate "
                  "and the copper was left with nowhere to go but out, as the "
                  "metal. The fading blue and the growing brown coat are the "
                  "same event seen twice.",
    },

    "misconceptions": [
        {"id": "MATL-05",
         "statement": "Any metal will displace any other if it is left long "
                      "enough.",
         "elicited_by": "think-commit-time",
         "confronted_by": "think-commit-time"},
        # ⚑ NOTES-C9 §6 anchors this on `rung-2` / `rung-2-feedback`, neither
        # of which the ladder emits (MRB-244 / MRB-248). The deck elicits it
        # — three of its eight cards are the reverse of a card that worked —
        # and the closing panel confronts it by naming the missing column.
        {"id": "MATL-06",
         "statement": "A less reactive metal can push a more reactive one out "
                      "of its compound.",
         "elicited_by": "deck-eight",
         "confronted_by": "deck-close"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "That is a <strong>displacement reaction</strong>: a more "
                 "reactive metal takes the place of a less reactive one in "
                 "its compound. The less reactive metal is pushed out — "
                 "displaced — as the element."},
        {"type": "explainer",
         "text": "The useful part is that it is not a surprise. Both metals "
                 "have a place in the reactivity series, and comparing the "
                 "two places tells you the answer before you run anything."},

        # ── #s-rule — the reference. No control; mirrors the hook.
        {"type": "rule", "anchor": "s-rule",
         "eyebrow": "Reference · keep this one open",
         "statement": "Higher displaces lower. Lower never displaces higher.",
         "close": "Find the metal you are adding, find the metal inside the "
                  "compound, and see which one is nearer the top. Carbon "
                  "counts here too, even though it is not a metal."},

        # ── #s-deck — eight proposals. Light `ks3-block` → `check`.
        {"type": "prediction-deck", "id": "deck-eight", "anchor": "s-deck",
         "eyebrow": "Your turn · eight proposals",
         "heading": "Commit to an answer, then run it.",
         "demand": "predict",
         "head_counter": {"format": "{n} of {total} run", "start": 0,
                          "total": 8},
         "options": [{"id": "yes", "label": "It happens"},
                     {"id": "no",  "label": "Nothing happens"}],
         "verdict_yes": "It happens.",
         "verdict_no": "Nothing happens.",
         # ⚖️ DERIVED, NEVER STORED. Five of the eight resolve to a reaction
         # and the renderer checks that count against this claim.
         "happens_claim": 5,
         # ⚠️ CARBON SITS ABOVE ZINC. It used to be ranked 3, below iron
         # (C9-5, chem audit 25 Aug 2026) — which contradicted lesson 1's
         # own series ("below aluminium and above zinc") and made lesson 3's
         # extraction bench impossible, since smelting iron and zinc oxides
         # with carbon REQUIRES carbon above them both. No card in the deck
         # could expose it (the only carbon card pits it against copper,
         # below it either way), so every derived outcome stayed green
         # around the wrong model. Re-ranked; no observation, count or
         # equation changes.
         "strip": [
             {
                 "name": "Magnesium",
                 "rank": 0,
                 "tag": "",
             },
             {
                 "name": "Carbon",
                 "rank": 1,
                 "tag": "non-metal",
             },
             {
                 "name": "Zinc",
                 "rank": 2,
                 "tag": "",
             },
             {
                 "name": "Iron",
                 "rank": 3,
                 "tag": "",
             },
             {
                 "name": "Copper",
                 "rank": 4,
                 "tag": "",
             },
             {
                 "name": "Silver",
                 "rank": 5,
                 "tag": "",
             },
         ],
         "proposals": [
             {
                 "id": "c1",
                 "added": "Magnesium",
                 "inside": "Copper",
                 "label": "Magnesium ribbon in copper sulfate solution",
                 "setup": "A cleaned magnesium ribbon stood in a tube of blue copper"
                           " sulfate solution.",
                 "obs": "The blue drains out of the solution within a minute, a soft"
                         " brown-pink solid builds on the ribbon, and the tube becomes hot"
                         " enough to notice.",
                 "eq": [
                           "magnesium + copper sulfate",
                           "magnesium sulfate + copper",
                       ],
             },
             {
                 "id": "c2",
                 "added": "Copper",
                 "inside": "Magnesium",
                 "label": "Copper wire in magnesium sulfate solution",
                 "setup": "A coil of clean copper wire stood in a tube of colourless"
                           " magnesium sulfate solution.",
                 "obs": "The wire stays bright and the solution stays colourless. It"
                         " looks the same after a week on the windowsill.",
             },
             {
                 "id": "c3",
                 "added": "Zinc",
                 "inside": "Copper",
                 "label": "Zinc granules in copper sulfate solution",
                 "setup": "A few zinc granules dropped into blue copper sulfate solution.",
                 "obs": "The blue fades, the granules go dull brown-pink, and the tube"
                         " warms.",
                 "eq": [
                           "zinc + copper sulfate",
                           "zinc sulfate + copper",
                       ],
             },
             {
                 "id": "c4",
                 "added": "Iron",
                 "inside": "Zinc",
                 "label": "Iron filings in zinc sulfate solution",
                 "setup": "Iron filings tipped into colourless zinc sulfate solution.",
                 "obs": "The filings stay grey and the solution stays colourless. Nothing"
                         " collects, nothing fades.",
             },
             {
                 "id": "c5",
                 "added": "Copper",
                 "inside": "Silver",
                 "label": "Copper wire in silver nitrate solution",
                 "setup": "A coil of clean copper wire stood in colourless silver nitrate"
                           " solution.",
                 "obs": "Grey needles of silver grow along the wire, and the solution"
                         " turns a faint blue as copper goes into it.",
                 "eq": [
                           "copper + silver nitrate",
                           "copper nitrate + silver",
                       ],
             },
             {
                 "id": "c6",
                 "added": "Silver",
                 "inside": "Copper",
                 "label": "Silver wire in copper sulfate solution",
                 "setup": "A length of silver wire stood in blue copper sulfate solution.",
                 "obs": "The wire stays bright, the blue stays exactly as blue as it"
                         " started.",
             },
             {
                 "id": "c7",
                 "added": "Zinc",
                 "inside": "Iron",
                 "label": "Zinc granules in iron sulfate solution",
                 "setup": "Zinc granules dropped into pale green iron sulfate solution.",
                 "obs": "The pale green fades and a dark grey deposit collects on the"
                         " granules. It is slower and far less obvious than the copper"
                         " ones, and it does happen.",
                 "eq": [
                           "zinc + iron sulfate",
                           "zinc sulfate + iron",
                       ],
             },
             {
                 "id": "c8",
                 "added": "Carbon",
                 "inside": "Copper",
                 "label": "Carbon powder heated with copper oxide",
                 "setup": "Black copper oxide mixed with carbon powder in a test tube and"
                           " heated strongly.",
                 "obs": "The mixture glows, and when it cools there are specks of pink-"
                         " brown copper in the black. The gas given off turns limewater"
                         " cloudy.",
                 "eq": [
                           "carbon + copper oxide",
                           "copper + carbon dioxide",
                       ],
             },
         ],
         "close_id": "deck-close",
         "close_title": "Sort the eight by what happened and the rule is the "
                        "only thing left.",
         "close": [
             "Every one that happened had the added element <strong>above"
             "</strong> the one in the compound. Every one that did nothing "
             "had it below. There is no third column — no “slowly”, "
             "no “a bit”, no “eventually”.",
         ]},

        {"type": "key-fact", "ref": "higher-displaces-lower"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Displacement", "Compound", "Prediction", "Sulfate",
                   "Impossible"]},

        {"type": "misconception", "id": "think-commit-time",
         "anchor": "s-think", "targets": "MATL-05"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "activities": [
        {"id": "think-commit-time",
         "kind": "predict",
         "demand": "explain",
         "targets": "MATL-05",
         "prompt": "It is a reasonable instinct — most slow things are just "
                   "slow. Commit before you read on.",
         # ⚑ MRB-177 — 14, 15, 13, 14 words.
         "options": [
             "Right — given enough time every combination gets round to "
             "reacting",
             "Wrong — copper is below magnesium, so this one does not happen "
             "at all",
             "Right, because a reaction that is slow enough looks like no "
             "reaction",
             "Wrong — it would happen at once if the solution were warmed "
             "first",
         ],
         "reveal": [
             "Time changes how <strong>fast</strong> a reaction goes. It "
             "cannot change whether the reaction goes at all. Magnesium holds "
             "sulfate more strongly than copper does, so a copper strip has "
             "nothing to offer and nothing happens — in ten minutes, in ten "
             "years.",
             "This is the difference between <strong>slow</strong> and "
             "<strong>impossible</strong>, and it is worth being precise "
             "about. Iron in dilute acid is slow: sparse bubbles, but it is "
             "going. Copper in magnesium sulfate is not slow. It is not "
             "happening.",
         ]},
    ],

    "key_facts": [
        {"id": "higher-displaces-lower", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "A more reactive metal displaces a less reactive one from "
                 "its compound. The other way round does not happen — not "
                 "slowly, not with heating, not eventually."},
    ],

    "ladder": {
        # index 2 — moved from Design's 0.
        "recall": {
            "q": "Which of these is a displacement reaction?",
            "options": [
                "Magnesium burning in oxygen",
                "Copper carbonate heated until it turns black",
                "Zinc added to copper sulfate solution",
                "Hydrochloric acid added to sodium hydroxide solution",
            ],
            "answer": 2,
            "feedback": {
                0: "That is combustion — magnesium joining oxygen, not taking "
                   "another metal's place.",
                1: "That is thermal decomposition — one compound falling "
                   "apart on heating.",
                3: "That is neutralisation. There is no metal being pushed "
                   "out of anything.",
            }},

        # index 3 — moved from Design's 0.
        "apply": {
            "q": "Copper wire in silver nitrate grows grey needles. Silver "
                 "wire in copper sulfate does nothing. Which statement "
                 "explains the pair?",
            "options": [
                "Silver is above copper in the series, so silver is too "
                "reactive to be displaced by anything",
                "Silver nitrate is a stronger solution, so it reacts with "
                "whatever is put into it",
                "The more expensive metal always ends up as the solid, so "
                "silver had to come out",
                "Copper is above silver in the series, so copper can take "
                "silver's place but silver cannot take copper's",
            ],
            "answer": 3,
            "feedback": {
                0: "It is the other way round — copper is above silver, which "
                   "is why the copper wire worked and the silver one did "
                   "not.",
                1: "Concentration changes how fast a possible reaction goes. "
                   "It cannot start an impossible one.",
                2: "Price is a fact about people. The series is a fact about "
                   "the metals.",
            }},

        "explain": {
            "q": "A strip of zinc is left in iron sulfate solution and very "
                 "little seems to happen. Explain whether a reaction is "
                 "taking place, and how you would decide.",
            "field_label": "Your explanation",
            "placeholder": "Zinc is above iron, so…",
            "success": [
                "Says zinc is above iron in the reactivity series.",
                "Says a reaction is therefore possible and is happening.",
                "Says it is slow rather than absent, because the two metals "
                "are close together in the series.",
                "Describes leaving it longer and looking for a dark deposit "
                "on the zinc.",
                "Distinguishes slow from impossible — copper in zinc sulfate "
                "would show nothing at any time.",
            ]},

        "produce": {
            "q": "Steel ships carry blocks of zinc bolted to the hull below "
                 "the waterline, and the blocks are replaced every few years. "
                 "Explain what the zinc is doing and why zinc was chosen.",
            "field_label": "Your answer",
            "placeholder": "The zinc is there because…",
            "success": [
                "Says zinc is above iron in the reactivity series.",
                "Says the zinc reacts in preference to the iron.",
                "Says the hull is protected while the zinc lasts.",
                "Says the block is used up, which is why it is replaced.",
                "Says a metal BELOW iron would not work, because it would "
                "not react in preference to it.",
            ]},
    },

    "key_note": "In a displacement reaction a more reactive metal takes the "
                "place of a less reactive metal in its compound, and the less "
                "reactive metal is released as the element. Comparing the two "
                "positions in the reactivity series predicts the result, "
                "including when the result is no reaction. Carbon obeys the "
                "same rule: it displaces the metals below it from their "
                "oxides, which is why it is placed in the series at all.",

    "stretch": [
        # ⚑ Flag 8. Named and explicitly excluded — see the docstring for why
        # naming it is the protective choice. No temperature and no method.
        {"type": "explainer", "id": "thermite",
         "text": "The most violent displacement in ordinary use is aluminium "
                 "powder with iron oxide. Aluminium is well above iron, takes "
                 "the oxygen, and leaves iron so hot that it runs as a "
                 "liquid — which is how lengths of railway track are welded "
                 "together in the field, with no power supply for miles. "
                 "<strong>It is not a school experiment at any scale</strong> "
                 "and nothing about it is worth improvising."},
        {"type": "explainer", "id": "sacrificial-zinc",
         "text": "Ships carry blocks of zinc bolted to the hull below the "
                 "waterline. Zinc is above iron in the series, so when "
                 "seawater attacks the steel the zinc reacts instead — it is "
                 "the more reactive metal and it goes first. The blocks are "
                 "eaten away and replaced every few years, which is far "
                 "cheaper than replacing a hull. The whole design rests on "
                 "one fact about the order and no other chemistry at all."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Displacement",
         "definition": "A reaction in which a more reactive metal takes the "
                       "place of a less reactive one in its compound.",
         "note": "Higher displaces lower, and never the other way round."},
        {"term": "Compound",
         "definition": "Two or more elements chemically joined, so that "
                       "neither behaves as it did on its own.",
         "note": "The blue in copper sulfate is copper that is not copper "
                 "yet."},
        {"term": "Prediction",
         "definition": "Saying what will happen before it happens, from "
                       "something you already know.",
         "note": "Here it is the series, and it works eight times out of "
                 "eight."},
        {"term": "Sulfate",
         "definition": "The part of a compound that the metal is joined to "
                       "in copper sulfate, zinc sulfate and the rest.",
         "note": "It stays put; the metals swap around it."},
        {"term": "Impossible",
         "definition": "Not merely slow. A reaction the series rules out does "
                       "not happen at any speed.",
         "note": "The most useful word on the page."},
    ],

    "safety_note": "The deck is a simulation. The copper displacements are a "
                   "standard class practical and need a written risk "
                   "assessment; the aluminium reaction described under "
                   "“Going further” is not done in schools at "
                   "any scale.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why waiting longer cannot help?",
              "cta": "Ask about this lesson",
              "anchor": "s-deck"},

    "ks4_becomes": "Displacement as electron transfer, oxidation and "
                   "reduction, ionic half equations, and the series used to "
                   "predict cell voltages.",

    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],
    "review_state": "draft",
}
