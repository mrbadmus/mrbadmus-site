"""C9 L4 — Ceramics, polymers and composites (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c9/c9-04-ceramics-polymers-and-composites.dc.html`,
and her author's notes `NOTES-C9.md` §1, §3, §4 flags 16–20, §6 (`MATL-11` to
`MATL-13`), §8 and §10.

── ⭐ THE UNIT CHANGES THE SUBJECT HERE, DELIBERATELY ────────────────────

Three lessons of metals and an order derived from evidence, and then this one
asks which material — not which metal. That is not a loss of focus; it is the
point at which "strong" stops being a single word. A bicycle frame does not
care about the reactivity series at all.

── ⚖️ EXACTLY ONE MATERIAL FITS EACH JOB, AND IT IS COMPUTED ────────────

The match is derived from the requirement tag sets and never authored, so a
job cannot be given an answer its own requirements do not select. Two winners
means the job does not discriminate; none means it cannot be done. Both are
refused.

⚖️ **AND A REJECTION IS REPORTED AS THE NAMED REQUIREMENT IT FAILS, NEVER AS A
COUNT.** "Fails 2 of 4" teaches nothing; "it passes carbon dioxide, so the
drink goes flat in days" teaches the lesson. So every material must carry a
REASON for every requirement it does not meet, and `meets` and `fails` must
partition the requirements a material is judged on — that gap is exactly where
a silent "no reason given" would come from.

── SCIENCE FLAGS ────────────────────────────────────────────────────────

⚑ Flag 16 — concrete spalling when heated and cooled, which is why reinforced
concrete loses the pizza-oven job. KEPT and correct.

⚑ Flag 17 — POLYETHENE PASSING CARBON DIOXIDE, so a fizzy drink stored in it
goes flat in days where PET holds it. KEPT with the timescale, which is the
requirement that decides the bottle job. Polyethene is markedly more permeable
to carbon dioxide than PET; "days" is the right order of magnitude for a thin
bottle wall and the sentence is not asked to be more precise than that.

⚑ Flag 18 — GLASS TREATED AS A CERAMIC. KEPT. Some sources separate glasses
from ceramics on structural grounds, and at KS3 the split would cost more than
it buys: both are fired from minerals, both are hard, stiff and brittle, and
the stove window is won by a glass-ceramic, which is the case that would make
a separate family confusing rather than clarifying.

⚑ Flag 19 — "STRONGER BUT BRITTLE" VS "WEAKER BUT TOUGH", and the hook
asserting that the china plate is the STRONGER material. KEPT, and it is the
best sentence in the lesson: the plate takes far more force before it fails,
and it fails all at once. `MATL-13` is the belief that strong and tough are
one property, and the hook has to commit to the counter-intuitive half of it
before the rung can confront it.

⚑ Flag 20 — composite recycling: "currently shredded, burned for its energy,
or buried". KEPT, hedged with "currently" on purpose — it is an active
engineering problem and a page that said "cannot be recycled" would be wrong
within a few years.

── ⊖ THE COMPOSITE CROSS-SECTION IS STILL NOT DECLARED ──────────────────

`NOTES-C9.md` §8 offers one figure for the whole unit: a composite
cross-section, fibres in a surround, drawn once, "because `c9-04`'s key fact
describes a structure the page never shows". It is a fair offer and it is
DECLINED for now. Audit law 8 says declare only what will be drawn, and a
figure declared here would be the unit's only one, would need a drawer in
`ks3_art/c9.py`, and would put the unit into the MRB-254 responsive-figure
sweep for a single illustration. The key fact describes the structure in words
that a student can hold. Recorded as an open offer rather than silently
dropped.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

This lesson holds **index 3** (recall) and **index 2** (apply), completing
C9's eight marked rungs at two of each index. Only the order moves.
"""

LESSON = {
    "slug":  "ceramics-polymers-and-composites",
    "title": "Ceramics, polymers and composites",
    "discipline": "chemistry",
    "unit": "Metals and materials",
    "family": "CONTRAST",

    "covers": ["KS3.C.MATS.03"],
    "touches": ["KS3.C.PT.05"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 2},
                {"id": "particles-and-matter", "level": 2}],
    "typical_year": 9,
    "typical_minutes": 55,

    "requires": ["getting-metals-out-of-rocks"],
    "assumes": [],
    "references": ["metals-and-non-metals", "polymers-and-plastics"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "A china plate shatters on a tiled floor and a plastic "
                    "beaker bounces. But you could stand on the plate and it "
                    "would hold you. So which of the two is the stronger "
                    "material?",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "Plate and beaker",  "done_when": "committed"},
        {"anchor": "s-classes", "short": "FAMILIES",
         "label": "Three families",    "mirrors": "s-hook",
         "done_when": "committed"},
        {"anchor": "s-bench",   "short": "BENCH",
         "label": "Four jobs",         "done_when": "all_four_matched"},
        {"anchor": "s-think",   "short": "THINK",
         "label": "Plastic is not one thing", "done_when": "committed"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A china dinner plate and a plastic beaker are knocked off "
                 "the same table onto the same tiled floor.",
        "prompt": "The plate breaks into eleven pieces. The beaker bounces "
                  "twice and rolls under a chair. Yet you could stand on the "
                  "plate and it would hold you, and standing on the beaker "
                  "would flatten it.",
        "commit": "So which of the two is the stronger material?",
        "options": [
            "The beaker, because it survived the fall undamaged",
            "The plate, because it takes far more force to break",
            "Neither — they are equally strong in different ways",
            "The beaker, because plastics are modern materials",
        ],
        "reveal": "The plate is the <strong>stronger</strong> one — it takes "
                  "far more force to break. It is also <strong>brittle"
                  "</strong>: it cannot bend even slightly, so when it does "
                  "fail it fails all at once. The beaker is weaker and "
                  "<strong>tough</strong>: it gives, absorbs the knock and "
                  "comes back. Two different properties, and “which is "
                  "better” is not a question until you know what the "
                  "material has to survive.",
    },

    "misconceptions": [
        {"id": "MATL-11",
         "statement": "If a material shatters, it must be weak.",
         "elicited_by": "hook",
         "confronted_by": "hook"},
        {"id": "MATL-12",
         "statement": "Plastic is one material.",
         "elicited_by": "think-commit-plastic",
         "confronted_by": "think-commit-plastic"},
        # ⚑ NOTES-C9 §6 anchors `MATL-13` on `rung-2` / `rung-2-feedback`,
        # neither of which the ladder emits. The bench elicits it — every
        # rejection names the property the material lacks — and the closing
        # panel confronts it.
        {"id": "MATL-13",
         "statement": "Strong and tough are the same property.",
         "elicited_by": "bench-four",
         "confronted_by": "bench-close"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook"},

        {"type": "explainer",
         "text": "Metals are not the only useful materials, and most things "
                 "around you are not metal. Three other families do most of "
                 "the work: <strong>ceramics</strong>, <strong>polymers"
                 "</strong> and <strong>composites</strong>."},
        {"type": "explainer",
         "text": "Each family behaves in a characteristic way, because of "
                 "what it is made of. Knowing the family tells you roughly "
                 "what a material will do before you have ever handled it."},

        # ── #s-classes — the reference. No control; mirrors the hook.
        {"type": "rule", "anchor": "s-classes",
         "eyebrow": "Reference · keep this one open",
         "statement": "Three families",
         "cards": [
             {"term": "Ceramics",
              "gloss": "Clay or minerals, fired hard. Hard and stiff, stand "
                       "high temperatures, do not conduct electricity, and "
                       "brittle — they crack rather than bend. Brick, "
                       "porcelain, glass, the tile on a bathroom floor."},
             {"term": "Polymers",
              "gloss": "Very long chains of atoms, mostly from crude oil. "
                       "Light, easily shaped into anything, usually flexible "
                       "and tough, and they soften or burn when heated. "
                       "Polythene, PET, nylon, the case of the device you "
                       "are reading this on."},
             {"term": "Composites",
              "gloss": "Two materials built into one, so the result does "
                       "what neither could alone: stiff fibres take the "
                       "pull, and the material around them holds the fibres "
                       "in place and spreads the load. Reinforced concrete, "
                       "carbon fibre, plywood, bone."},
         ],
         "close": "Every one of those properties is a tendency, not a law. "
                  "There are polymers that will sit in an oven and ceramics "
                  "you can see through, and the bench below has both."},

        # ── #s-bench — four jobs, six materials. Exactly one match each.
        {"type": "spec-bench", "id": "bench-four", "anchor": "s-bench",
         "eyebrow": "Your turn · four jobs",
         "heading": "Four jobs, six materials on the shelf. One material fits "
                    "each job.",
         "demand": "classify",
         "resting": "Pick a job, then pick a material.",
         "head_counter": {"format": "{n} of {total} matched", "start": 0,
                          "total": 4},
         "verdict_yes": "That one fits.",
         "verdict_no": "Not this one.",
         "reqs": {
             "red-heat": "stands red heat",
             "thermal-cycle": "survives daily heating and cooling",
             "stiff": "stiff under load",
             "cheap": "cheap by the square metre",
             "light": "light",
             "clear": "see-through",
             "gas-tight": "holds pressurised gas in",
             "no-shatter": "does not shatter when dropped",
             "flex-tough": "takes repeated flexing and knocks",
         },
         "materials": [
             {
                 "id": "firebrick",
                 "name": "Firebrick",
                 "cls": "ceramic",
                 "meets": [
                              "red-heat",
                              "thermal-cycle",
                              "stiff",
                              "cheap",
                          ],
                 "fails": {
                              "light": "a brick weighs what a brick weighs, and a frame made of them"
                                        " would need a lorry",
                              "clear": "it is opaque, and firing clay will never make it otherwise",
                              "gas-tight": "fired clay is full of tiny holes — that porosity is part of why"
                                            " it insulates so well",
                              "no-shatter": "dropped on a hard floor it cracks straight through",
                              "flex-tough": "it does not flex at all; the first bend is a crack",
                          },
             },
             {
                 "id": "glassceramic",
                 "name": "Heat-proof glass-ceramic",
                 "cls": "ceramic",
                 "meets": [
                              "red-heat",
                              "thermal-cycle",
                              "stiff",
                              "clear",
                              "gas-tight",
                          ],
                 "fails": {
                              "cheap": "a sheet of it costs many times what the same area of firebrick"
                                        " does",
                              "light": "a pane thick enough to be safe is heavy",
                              "no-shatter": "a sharp knock on a corner and it goes — it is still a ceramic",
                              "flex-tough": "it has no give, so repeated flexing finds the smallest scratch"
                                             " and runs a crack out of it",
                          },
             },
             {
                 "id": "polythene",
                 "name": "Polythene",
                 "cls": "polymer",
                 "meets": [
                              "cheap",
                              "light",
                              "no-shatter",
                              "flex-tough",
                          ],
                 "fails": {
                              "red-heat": "it softens in hot water and melts not far above that",
                              "thermal-cycle": "the first heating is the last one — there is nothing left to"
                                                " cycle",
                              "stiff": "a sheet of it bends between your fingers",
                              "clear": "it comes out milky rather than clear, like a supermarket milk"
                                        " bottle",
                              "gas-tight": "carbon dioxide seeps out through it, and a fizzy drink stored in"
                                            " it goes flat in days",
                          },
             },
             {
                 "id": "pet",
                 "name": "PET",
                 "cls": "polymer",
                 "meets": [
                              "cheap",
                              "light",
                              "clear",
                              "gas-tight",
                              "no-shatter",
                              "flex-tough",
                          ],
                 "fails": {
                              "red-heat": "it buckles in an oven and softens in boiling water",
                              "thermal-cycle": "it deforms on the first strong heating, so there is no second"
                                                " one",
                              "stiff": "an empty bottle crumples in one hand — it is the pressure inside"
                                        " that keeps a full one firm",
                          },
             },
             {
                 "id": "carbon",
                 "name": "Carbon-fibre composite",
                 "cls": "composite",
                 "meets": [
                              "stiff",
                              "light",
                              "no-shatter",
                              "flex-tough",
                          ],
                 "fails": {
                              "red-heat": "the resin holding the fibres together chars long before anything"
                                           " glows",
                              "thermal-cycle": "every strong heating weakens the resin a little more until the"
                                                " fibres let go",
                              "cheap": "it is the most expensive material on the shelf by a wide margin",
                              "clear": "it is black, and the weave shows",
                              "gas-tight": "wound fibre and resin does not seal on its own — composite gas"
                                            " cylinders have a liner inside them",
                          },
             },
             {
                 "id": "concrete",
                 "name": "Reinforced concrete",
                 "cls": "composite",
                 "meets": [
                              "red-heat",
                              "stiff",
                              "cheap",
                              "no-shatter",
                          ],
                 "fails": {
                              "thermal-cycle": "water trapped inside turns to steam and blows flakes off the"
                                                " surface",
                              "light": "it is the heaviest thing on the shelf",
                              "clear": "it is opaque",
                              "gas-tight": "concrete is porous — gas works its way through it",
                              "flex-tough": "it cracks instead of flexing; the steel inside stops the crack"
                                             " running, which is not the same as bending",
                          },
             },
         ],
         "jobs": [
             {
                 "id": "oven",
                 "name": "Lining for a pizza oven floor",
                 "setup": "A wood-fired oven, lit every evening, left to go cold overnight."
                           " The floor glows dull red at the hottest part of the night.",
                 "reqs": [
                             "red-heat",
                             "thermal-cycle",
                             "stiff",
                             "cheap",
                         ],
                 "praise": "A firebrick was made for exactly this. It takes the heat, it"
                            " does not mind being heated and cooled every day, it holds the"
                            " weight of the fire, and it is cheap enough to lay a whole floor."
                            " That it is heavy and would shatter if you dropped it does not"
                            " matter — nobody is going to drop the oven floor.",
             },
             {
                 "id": "bottle",
                 "name": "A bottle for a fizzy drink",
                 "setup": "Two litres, pressurised, thrown into a bag, dropped on"
                           " pavements, and the label has to be readable through the"
                           " contents.",
                 "reqs": [
                             "light",
                             "gas-tight",
                             "no-shatter",
                             "clear",
                         ],
                 "praise": "PET holds the gas in, weighs almost nothing, bounces when it is"
                            " dropped, and you can see the drink through it. It softens in an"
                            " oven, and no fizzy drink has ever needed to go in one.",
             },
             {
                 "id": "bike",
                 "name": "A racing bike frame",
                 "setup": "Ridden hard, out of the saddle up hills, over potholes, and"
                           " every gram is argued about.",
                 "reqs": [
                             "light",
                             "stiff",
                             "flex-tough",
                         ],
                 "praise": "Carbon fibre is the one that gets all three at once: stiff so"
                            " the pedalling is not wasted, light enough to argue about grams,"
                            " and tough enough to take years of flexing. It costs a great"
                            " deal, and on a racing frame that is the trade being made"
                            " deliberately.",
             },
             {
                 "id": "stove",
                 "name": "The window in a stove door",
                 "setup": "A wood burner in a living room. The fire is a metre from a sofa,"
                           " the door is opened and shut while it is alight, and people want"
                           " to watch the flames.",
                 "reqs": [
                             "clear",
                             "red-heat",
                             "thermal-cycle",
                             "stiff",
                         ],
                 "praise": "Heat-proof glass-ceramic is the only material here that is"
                            " transparent and unbothered by the heat. It is expensive and"
                            " heavy, and a stove door is small — so those are the right costs"
                            " to accept for the one property nothing else offers.",
             },
         ],
         "close_id": "bench-close",
         "close_title": "Four jobs, and the winners came from three different "
                        "families.",
         "close": [
             "Two of the winners were ceramics and they lost each other's "
             "jobs — one is opaque and cheap, the other clear and expensive. "
             "<strong>The family tells you what to expect. The particular "
             "material has to be checked against the particular job.</strong>",
             "Notice what never decided a job: how STRONG a material is on "
             "its own. Every rejection above named a specific thing the "
             "material could not do — passes gas, cracks when cycled, will "
             "not stand red heat. <strong>Strong and tough are two "
             "properties, and neither of them is a score out of ten.</strong>",
         ]},

        {"type": "key-fact", "ref": "what-a-composite-is"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Six words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Ceramic", "Polymer", "Composite", "Brittle", "Tough",
                   "Strong"]},

        {"type": "misconception", "id": "think-commit-plastic",
         "anchor": "s-think", "targets": "MATL-12"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    # ⊖ NO FIGURE. Design offers a composite cross-section as the unit's one
    # candidate; declined for now and recorded in the docstring rather than
    # dropped silently.
    "figures": [],

    "activities": [
        {"id": "think-commit-plastic",
         "kind": "predict",
         "demand": "explain",
         "targets": "MATL-12",
         "prompt": "One word covering a great many substances. Commit before "
                   "you read on.",
         # ⚑ MRB-177 — 14, 15, 14, 14 words.
         "options": [
             "Right — if one plastic cannot do a job then no plastic will "
             "manage it",
             "Wrong — “plastic” is a family of very different "
             "substances, like “metal”",
             "Right, because every plastic is made from crude oil in the same "
             "way",
             "Wrong — all plastics behave the same and the job must be "
             "impossible",
         ],
         "reveal": [
             "“Plastic” is a family, not a substance — like "
             "“metal”. A carrier bag goes soft in hot water. A "
             "kettle body holds boiling water all day and stays rigid. A "
             "saucepan handle sits above a gas flame for years. A "
             "bulletproof vest is woven from polymer fibre. Those are four "
             "polymers with almost nothing in common except the long chains "
             "they are built from.",
             "Some polymers soften whenever they are heated, and can be "
             "melted and reshaped over and over. Others are set hard as they "
             "are made and will char rather than melt. <strong>Asking "
             "“will plastic do?” is like asking “will "
             "metal do?” — the answer depends entirely on which one."
             "</strong>",
         ]},
    ],

    "key_facts": [
        {"id": "what-a-composite-is", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "A composite is two materials built into one, so that the "
                 "result does something neither could do alone: strong fibres "
                 "take the pull, and the material around them holds the "
                 "fibres in place and spreads the load."},
    ],

    "ladder": {
        # index 3 — moved from Design's 0.
        "recall": {
            # ⊕ MRB-279, 21 Aug 2026 — FIXED AT THE DISTRACTOR, per MRB-177's
            # standing ruling. The correct answer was the only two-word option
            # against three one-word distractors, so a student could score it
            # by picking the longest without reading a word — and this rung
            # shipped that way in PR #9.
            #
            # MRB-177 rules that a length tell is fixed at the DISTRACTOR and
            # never by shortening the correct answer, and that reaching for
            # `KNOWN_TELLS` is the regression. So `Reinforced concrete` stays:
            # it is the flagship KS3 composite and the one this unit's own
            # bench runs. Each distractor takes the form the unit already uses
            # for it — the tile and the sheet are c9-04's own load test, the
            # wire is c9-02's — which makes all four options two words and the
            # parity a property of how the question is built.
            #
            # Each distractor still names one material from one of the three
            # families the lesson contrasts (ceramic, polymer, metal), so the
            # taxonomy the rung tests is unchanged. Answer stays at index 3:
            # MRB-278 measured the fourth option correct 0 times in 174 rungs.
            "q": "Which of these is a composite?",
            # ⊕ MRB-281, 23 Aug 2026 — CONVERGENT FIX, resolved to main's
            # wording. The content-chem lane fixed this same length tell
            # independently and reached the same three two-word distractors
            # bar one: `Fired porcelain` where main wrote `Porcelain tile`.
            # Main's is kept because it is the complete edit — it also
            # rewrote the three corrections below to open on the two-word
            # option, and `Porcelain tile` is the form c9-04's own load test
            # already uses. The lane's `Fired porcelain` would have left
            # "A porcelain tile is a ceramic" answering an option that never
            # says tile. Nothing about the ruling differs between the two.
            "options": ["Porcelain tile", "Polythene sheet", "Copper wire",
                        "Reinforced concrete"],
            "answer": 3,
            "feedback": {
                0: "A porcelain tile is a ceramic — one material, fired hard.",
                1: "A polythene sheet is a polymer — long chains, and nothing "
                   "else built into it.",
                2: "Copper wire is a metal and an element. There is only one "
                   "kind of atom in it.",
            }},

        # index 2 — moved from Design's 0. `MATL-13` at the ladder.
        "apply": {
            "q": "A ceramic tile and a polythene sheet are each pressed with "
                 "a rising load. The tile takes far more force and then "
                 "breaks suddenly. The sheet bends early and never quite "
                 "breaks. Which statement describes them?",
            "options": [
                "The tile is both stronger and tougher; the sheet is weaker "
                "in every way",
                "The sheet is stronger, because it survived the test and the "
                "tile did not",
                "The tile is stronger but brittle; the sheet is weaker but "
                "tough",
                "They are equally strong, because each one failed in its own "
                "way",
            ],
            "answer": 2,
            "feedback": {
                0: "The tile is stronger and it is NOT tougher — breaking "
                   "suddenly is exactly what brittle means.",
                1: "Surviving is toughness, not strength. The sheet gave way "
                   "under far less force.",
                3: "The tile took far more force before it failed. That is "
                   "what being stronger is.",
            }},

        "explain": {
            "q": "Explain why reinforced concrete is used for bridges when "
                 "neither concrete nor steel alone would do, using the word "
                 "composite in your answer.",
            "field_label": "Your explanation",
            "placeholder": "Concrete on its own is…",
            "success": [
                "Says concrete is strong when squashed but weak when "
                "stretched.",
                "Says steel is strong when stretched.",
                "Says the steel bars are placed where the bridge is being "
                "pulled apart.",
                "Says the concrete holds the steel in place and spreads the "
                "load.",
                "Says the combination is a composite, doing what neither "
                "material does alone.",
            ]},

        "produce": {
            "q": "Choose a material for the see-through door of a wood-fired "
                 "oven that is lit every evening and left to go cold "
                 "overnight. Justify your choice and say why an ordinary "
                 "glass pane would fail.",
            "field_label": "Your answer",
            "placeholder": "The door needs a material that…",
            "success": [
                "Says the material must be see-through.",
                "Says it must stand high temperatures.",
                "Says it must survive being heated and cooled every day "
                "without cracking.",
                "Chooses a heat-proof glass-ceramic, or a ceramic that is "
                "transparent.",
                "Says ordinary glass would crack from the repeated heating "
                "and cooling, not from the heat alone.",
            ]},
    },

    "key_note": "Ceramics are made by firing clay or other minerals. They are "
                "hard, stiff and stand high temperatures, they do not conduct "
                "electricity, and they are brittle — strong under a steady "
                "load, but they crack rather than bend. Polymers are built "
                "from very long chains of atoms. They are light, easily "
                "shaped, usually flexible and tough, and they soften or burn "
                "when heated. A composite is two or more materials combined "
                "so the result has properties neither had alone: fibres for "
                "strength, and a surrounding material to hold them and spread "
                "the load.",

    "stretch": [
        {"type": "explainer", "id": "why-concrete-spalls",
         "text": "Concrete does not fail in a fire the way people expect. It "
                 "holds water in tiny pores, and when the surface is heated "
                 "hard that water turns to steam faster than it can escape. "
                 "The pressure blows flakes off the face — spalling — and "
                 "each flake exposes fresh concrete to the heat. That is why "
                 "reinforced concrete lost the pizza-oven job above: the "
                 "problem is not the temperature, it is the same surface "
                 "being taken up and down through it every day."},
        {"type": "explainer", "id": "composites-at-the-end",
         "text": "A composite is hard to take apart again, which is the price "
                 "of being two materials in one. A cracked carbon-fibre "
                 "bicycle frame is currently shredded, burned for its energy, "
                 "or buried; a steel one goes back into a furnace and comes "
                 "out as steel. Separating fibres from the resin around them "
                 "is an active engineering problem rather than a settled one, "
                 "and it is the strongest argument anyone makes for building "
                 "things out of one material where one will do."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Ceramic",
         "definition": "A material made by firing clay or minerals hard. "
                       "Stiff, heat-resistant and brittle.",
         "note": "Brick, porcelain, glass, the tile on a bathroom floor."},
        {"term": "Polymer",
         "definition": "A material built from very long chains of atoms. "
                       "Light, easily shaped, and it softens or burns when "
                       "heated.",
         "note": "A family of substances, not one substance."},
        {"term": "Composite",
         "definition": "Two materials built into one so the result does what "
                       "neither could alone.",
         "note": "Fibres take the pull; the surround holds them and spreads "
                 "the load."},
        {"term": "Brittle",
         "definition": "Breaks all at once rather than bending first.",
         "note": "Not the same as weak — the plate is brittle AND strong."},
        {"term": "Tough",
         "definition": "Absorbs a knock and keeps going, usually by giving a "
                       "little.",
         "note": "The beaker is tough and weak. Both words are needed."},
        {"term": "Strong",
         "definition": "Takes a large force before it fails.",
         "note": "Says nothing at all about HOW it fails."},
    ],

    "safety_note": "",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure how something can be strong and "
                      "break easily?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Polymer chains and cross-linking, thermosoftening against "
                   "thermosetting, and choosing materials against a full "
                   "specification including cost and life cycle.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
