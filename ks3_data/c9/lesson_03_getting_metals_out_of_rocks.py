"""C9 L3 — Getting metals out of rocks (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c9/c9-03-getting-metals-out-of-rocks.dc.html`, and
her author's notes `NOTES-C9.md` §1, §3, §4 flags 10–15, §5.2, §6 (`MATL-08`,
`MATL-09`) and §10.

── ⚖️ THREE VERDICTS, NOT TWO, AND THE THIRD IS THE LESSON ──────────────

Every one of the twenty-four (ore, method) pairs carries an authored verdict,
and a method can WORK, NOT WORK, or **work and be the wrong tool**. Silver
oxide can be freed three ways and a works would pay for only one of them. A
two-state bench cannot say that, and saying it is the entire reason for asking
a student to choose a method rather than be told one.

⚖️ Each ore's declared `route` is checked against its OWN verdict for that
method, because the synthesis panel prints the route as the answer — and an
ore recommended a method its own bench has just refused is the page
contradicting itself.

⚖️ **AND AT LEAST ONE ORE MUST DEFEAT CARBON.** `MATL-09` is the belief that
any oxide gives up its oxygen to carbon if the furnace is hot enough. A bench
with no counter-example teaches it instead of confronting it, so the renderer
refuses one.

── SCIENCE FLAGS ────────────────────────────────────────────────────────

⚑ Flag 10 — SILVER OXIDE IS THE "HEAT ALONE" ROUTE, AND MERCURY OXIDE IS
AVOIDED DELIBERATELY. KEPT. Silver oxide does decompose on heating, so the
chemistry is honest; mercury oxide is the textbook example and is a
substantial hazard whose name in a lesson invites a search. The substitution
costs nothing and the textbook version gains nothing.

⚑ Flag 11 — the blast furnace stating that most of the oxygen is taken by
carbon monoxide formed from the coke, not by solid carbon. KEPT and correct,
and it is in the OPTIONAL layer for exactly that reason: it is above the
statutory line and it complicates a rule the core has just established.

⚑ Flag 12 — zinc leaving the furnace as a vapour and being condensed. KEPT and
correct, and it is why zinc's cell reads differently from iron's.

⚑ Flag 13 — aluminium costing more than gold in the 1850s. Attested; KEPT and
stated flatly, because hedging it would remove the only thing that makes the
carbon line feel like it cost somebody something.

⚑ Flag 14 — "roughly a twentieth of the electricity" for recycled aluminium.
The commonly quoted figure is about 5%. KEPT hedged: the exact number varies
with process and source, and a student who meets 5% elsewhere should find this
page compatible rather than contradicted.

⚑ Flag 15 — cryolite named only in the GCSE line, not in the lesson body.
KEPT.

── §5.2 · THE ONE PRACTICAL A CLASS IS LIKELY TO DO ─────────────────────

Copper oxide reduced by carbon is a standard school practical and the one
thing in this unit a class is most likely to actually run. It needs a written
risk assessment — strong heating, a reducing mixture, hot residues — and the
`safety_note` says so. The bench is a simulation and is not a method.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

This lesson holds **index 1** (recall, moved) and **index 0** (apply,
Design's own). ⚑ The apply rung's distractors are re-authored for length
(MRB-177): Design's answer runs 24 words against 15, 15 and 15 — longest by
nine and pickable on shape. Each distractor now states its wrong reason at the
answer's own length.
"""

LESSON = {
    "slug":  "getting-metals-out-of-rocks",
    "title": "Getting metals out of rocks",
    "discipline": "chemistry",
    "unit": "Metals and materials",
    "family": "PROCESS",

    "covers": ["KS3.C.MATS.02"],
    "touches": ["KS3.C.MATS.01", "KS3.WS.EXP.02"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3},
                {"id": "earth-and-resources", "level": 2}],
    "typical_year": 9,
    "typical_minutes": 55,

    "requires": ["predicting-displacement"],
    "assumes": [],
    "references": ["the-reactivity-series", "oxidation",
                   "thermal-decomposition"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "Half of a lump of malachite is copper, by mass, and no "
                    "amount of melting will pour any of it out. So how do you "
                    "get a metal out of a rock that is not letting go?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The green stone",   "done_when": "committed"},
        {"anchor": "s-line",   "short": "LINE",
         "label": "The carbon line",   "mirrors": "s-hook",
         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Six deliveries",    "done_when": "all_six_found"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Hotter does not help", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A lump of green-blue stone from a Cornish mine, and a "
                 "length of copper pipe.",
        "prompt": "The stone is malachite. Roughly half of it, by mass, is "
                  "copper. None of that copper looks like copper, behaves "
                  "like copper, or conducts like copper — and no amount of "
                  "melting the stone will pour any out.",
        "commit": "The copper is in there. Why can it not simply be melted "
                  "out?",
        "options": [
            "The furnace cannot get hot enough to melt that stone",
            "The copper is chemically joined to other elements",
            "The copper is in droplets too small to collect",
            "The stone would have to be crushed much finer first",
        ],
        "reveal": "Because the copper is <strong>chemically joined</strong> "
                  "to other elements — in this stone, to oxygen and carbon. "
                  "Melting changes a solid into a liquid and joins nothing "
                  "and separates nothing. Getting the copper out means taking "
                  "the oxygen off it, and that is a <strong>reaction</strong>, "
                  "not a temperature.",
    },

    "misconceptions": [
        # The hook block is emitted with `data-activity="hook"`, which is the
        # id both halves of this join resolve to.
        {"id": "MATL-08",
         "statement": "Metals are in the ground as metal, and extraction is "
                      "digging and melting.",
         "elicited_by": "hook",
         "confronted_by": "hook"},
        {"id": "MATL-09",
         "statement": "Any oxide gives up its oxygen to carbon if the furnace "
                      "is hot enough.",
         "elicited_by": "think-commit-hotter",
         "confronted_by": "think-commit-hotter"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook"},

        {"type": "explainer",
         "text": "A rock with enough of a metal compound in it to be worth "
                 "digging up is an <strong>ore</strong>. Most ores are, or "
                 "can be roasted into, the metal's <strong>oxide</strong>."},
        {"type": "explainer",
         "text": "So extraction is nearly always the same job: take the "
                 "oxygen away. Removing oxygen from a compound is called "
                 "<strong>reduction</strong>, and there are only a few ways "
                 "to do it. Which one works is decided by the reactivity "
                 "series."},

        # ── #s-line — the reference. No control; mirrors the hook.
        {"type": "rule", "anchor": "s-line",
         "eyebrow": "Reference · keep this one open",
         "statement": "The carbon line",
         "cards": [
             {"term": "Above carbon",
              "gloss": "Potassium, sodium, calcium, magnesium, aluminium. "
                       "These hold oxygen more tightly than carbon does, so "
                       "carbon cannot take it. They need electricity."},
             {"term": "Carbon",
              "gloss": "The line itself. Not a metal, and its place in the "
                       "series is what decides every row above and below."},
             {"term": "Below carbon",
              "gloss": "Zinc, iron, lead, copper. Carbon takes the oxygen "
                       "and the metal is left. This is a furnace, and it is "
                       "cheap."},
             {"term": "Far below carbon",
              "gloss": "Silver and gold. Their oxides fall apart on heating "
                       "alone, and gold is mostly found as the metal in the "
                       "first place."},
         ],
         "close": "Carbon is a non-metal with a place in the series, and this "
                  "is what the place is for. It can pull oxygen away from the "
                  "oxide of anything below it, and from nothing above it."},

        # ── #s-bench — six deliveries, four methods, 24 verdicts.
        {"type": "extraction-route", "id": "bench-six", "anchor": "s-bench",
         "eyebrow": "Your turn · six deliveries",
         "heading": "Six things arrive at the works. Find the method that "
                    "frees the metal.",
         "demand": "investigate",
         "resting": "Pick a delivery, then pick a method.",
         "head_counter": {"format": "{n} of {total} found", "start": 0,
                          "total": 6},
         # The method whose failure `MATL-09` turns on. The renderer refuses
         # a bench on which carbon frees everything.
         "carbon_method": "carbon",
         "methods": [
             {
                 "id": "crush",
                 "label": "Crush and wash",
             },
             {
                 "id": "alone",
                 "label": "Heat it alone",
             },
             {
                 "id": "carbon",
                 "label": "Heat it with carbon",
             },
             {
                 "id": "electric",
                 "label": "Pass electricity through it",
             },
         ],
         "route_groups": [
             {
                 "id": "crush",
                 "label": "Already the metal — just separate it",
                 "note": "The least reactive metals of all sit in the ground uncombined,"
                          " so the work is physical: crush, wash, pick out. No reaction is"
                          " needed and none is possible.",
             },
             {
                 "id": "alone",
                 "label": "Heat alone is enough",
                 "note": "Very unreactive metals hold oxygen so weakly that their oxides"
                          " fall apart when warmed. Nothing has to be added at all.",
             },
             {
                 "id": "carbon",
                 "label": "Heat with carbon",
                 "note": "For every metal below carbon in the series, carbon takes the"
                          " oxygen and the metal is left. This is the route for the metals"
                          " humanity has had for thousands of years.",
             },
             {
                 "id": "electric",
                 "label": "Electricity",
                 "note": "For every metal above carbon, nothing chemical on the shelf will"
                          " take the oxygen away, and electricity does the separating"
                          " instead. It is the expensive route, and for these metals it is"
                          " the only one.",
             },
         ],
         "ores": [
             {
                 "id": "gold",
                 "name": "Gold-bearing gravel",
                 "metal": "Gold",
                 "route": "crush",
                 "setup": "A tray of river gravel with dull yellow flecks in it, from a"
                           " claim in the Klondike.",
                 "line": "Gold sits at the very bottom of the series — and in the ground"
                          " it is the metal already",
                 "verdicts": {
                                 "crush": {
                                              "works": True,
                                              "title": "It works.",
                                              "why": "The gold is already gold. Crushing the rock and washing it away"
                                                      " leaves the flecks behind, because gold is much denser than the"
                                                      " sand. Nothing has reacted — this is separation, not chemistry.",
                                          },
                                 "alone": {
                                              "works": False,
                                              "title": "It does nothing.",
                                              "why": "There is no compound here to break up. Heating gold-bearing"
                                                      " gravel gives you hot gravel.",
                                          },
                                 "carbon": {
                                               "works": False,
                                               "title": "It does nothing.",
                                               "why": "Carbon takes oxygen out of oxides. This gold is not joined to"
                                                       " oxygen, so the carbon simply burns.",
                                           },
                                 "electric": {
                                                 "works": False,
                                                 "title": "It does nothing.",
                                                 "why": "Electricity splits compounds into their elements. Gold in gravel"
                                                         " is already an element, so there is nothing to split.",
                                             },
                             },
             },
             {
                 "id": "silver",
                 "name": "Silver oxide",
                 "metal": "Silver",
                 "route": "alone",
                 "setup": "A jar of dark powder, silver joined to oxygen.",
                 "line": "Silver sits below carbon, and very near the bottom",
                 "verdicts": {
                                 "crush": {
                                              "works": False,
                                              "title": "It does nothing.",
                                              "why": "Washing separates one solid from another. It cannot separate"
                                                      " silver from the oxygen it is chemically joined to — you end up"
                                                      " with finer silver oxide.",
                                          },
                                 "alone": {
                                              "works": True,
                                              "title": "It works.",
                                              "why": "Silver is so unreactive that it barely holds its oxygen at all:"
                                                      " heat the oxide and it comes apart on its own into silver and"
                                                      " oxygen gas. No second ingredient is needed.",
                                              "eq": [
                                                        "silver oxide",
                                                        "silver + oxygen",
                                                    ],
                                          },
                                 "carbon": {
                                               "works": True,
                                               "title": "It works — and it is the wrong tool.",
                                               "why": "Carbon does take the oxygen. But heat alone had already finished"
                                                       " the job, and now there is spare carbon to clean out of the"
                                                       " silver. Choosing this is not a mistake in chemistry; it is a"
                                                       " mistake in cost.",
                                           },
                                 "electric": {
                                                 "works": True,
                                                 "title": "It works — and nobody would pay for it.",
                                                 "why": "Electricity would split the oxide. It is the most expensive"
                                                         " method available, spent on the compound that needs the least.",
                                             },
                             },
             },
             {
                 "id": "copper",
                 "name": "Copper oxide",
                 "metal": "Copper",
                 "route": "carbon",
                 "setup": "A black powder, roasted from the green malachite in the hook.",
                 "line": "Copper sits below carbon",
                 "verdicts": {
                                 "crush": {
                                              "works": False,
                                              "title": "It does nothing.",
                                              "why": "You get finer black powder. The copper is joined to oxygen and"
                                                      " no amount of grinding parts them.",
                                          },
                                 "alone": {
                                              "works": False,
                                              "title": "It does not work.",
                                              "why": "Copper oxide is untroubled by a strong flame. It glows while it"
                                                      " is hot, and when it cools it is still black copper oxide.",
                                          },
                                 "carbon": {
                                               "works": True,
                                               "title": "It works.",
                                               "why": "Carbon is above copper in the series, so it takes the oxygen."
                                                       " Specks of pink-brown copper appear in the black mixture, and the"
                                                       " gas coming off turns limewater cloudy — carbon dioxide.",
                                               "eq": [
                                                         "copper oxide + carbon",
                                                         "copper + carbon dioxide",
                                                     ],
                                           },
                                 "electric": {
                                                 "works": True,
                                                 "title": "It works — and it is the wrong tool.",
                                                 "why": "Electricity would free the copper. Carbon does the same job with"
                                                         " a Bunsen burner and a test tube, and carbon is cheap.",
                                             },
                             },
             },
             {
                 "id": "iron",
                 "name": "Iron ore",
                 "metal": "Iron",
                 "route": "carbon",
                 "setup": "A truckload of rusty-red rock: iron joined to oxygen, with sand"
                           " and clay mixed in.",
                 "line": "Iron sits below carbon",
                 "verdicts": {
                                 "crush": {
                                              "works": False,
                                              "title": "It does nothing.",
                                              "why": "Crushing is done first at every ironworks — it makes the rock"
                                                      " easier to feed in. It frees no iron, because the iron is joined"
                                                      " to oxygen.",
                                          },
                                 "alone": {
                                              "works": False,
                                              "title": "It does not work.",
                                              "why": "Iron holds its oxygen far too well for heat alone. Furnaces"
                                                      " reached this temperature for centuries without producing iron"
                                                      " from ore.",
                                          },
                                 "carbon": {
                                               "works": True,
                                               "title": "It works.",
                                               "why": "Carbon takes the oxygen and molten iron collects at the bottom."
                                                       " On an industrial scale the carbon arrives as coke, and this"
                                                       " reaction is what a blast furnace is for.",
                                               "eq": [
                                                         "iron oxide + carbon",
                                                         "iron + carbon dioxide",
                                                     ],
                                           },
                                 "electric": {
                                                 "works": True,
                                                 "title": "It works — and it is the wrong tool.",
                                                 "why": "Electricity can free iron, and the world makes iron by the"
                                                         " hundred million tonnes. Paying for electricity instead of coke"
                                                         " would change the price of everything made of steel.",
                                             },
                             },
             },
             {
                 "id": "zinc",
                 "name": "Zinc oxide",
                 "metal": "Zinc",
                 "route": "carbon",
                 "setup": "A white powder, roasted from zinc blende ore.",
                 "line": "Zinc sits below carbon — but only just",
                 "verdicts": {
                                 "crush": {
                                              "works": False,
                                              "title": "It does nothing.",
                                              "why": "A finer white powder, still zinc oxide. The oxygen is chemically"
                                                      " joined on.",
                                          },
                                 "alone": {
                                              "works": False,
                                              "title": "It does not work.",
                                              "why": "Zinc oxide does not give up its oxygen to heat. It goes yellow"
                                                      " while hot and white again as it cools, and that is a change in"
                                                      " the crystals, not a reaction.",
                                          },
                                 "carbon": {
                                               "works": True,
                                               "title": "It works.",
                                               "why": "Carbon takes the oxygen. Zinc is unusual here: it boils at the"
                                                       " temperature the furnace runs at, so the metal leaves as a vapour"
                                                       " and is condensed somewhere cooler.",
                                               "eq": [
                                                         "zinc oxide + carbon",
                                                         "zinc + carbon dioxide",
                                                     ],
                                           },
                                 "electric": {
                                                 "works": True,
                                                 "title": "It works — and it is a judgement call.",
                                                 "why": "Zinc is close to carbon in the series, and both routes are used"
                                                         " in industry depending on the ore and the price of power. Carbon"
                                                         " is the one to know for the rule.",
                                             },
                             },
             },
             {
                 "id": "aluminium",
                 "name": "Aluminium oxide",
                 "metal": "Aluminium",
                 "route": "electric",
                 "setup": "A white powder purified from bauxite, the ore that most of"
                           " Australia and Guinea ship out by the boatload.",
                 "line": "Aluminium sits ABOVE carbon",
                 "verdicts": {
                                 "crush": {
                                              "works": False,
                                              "title": "It does nothing.",
                                              "why": "Bauxite is crushed and purified before anything else happens,"
                                                      " and at the end of it you have this white powder: aluminium still"
                                                      " joined to oxygen.",
                                          },
                                 "alone": {
                                              "works": False,
                                              "title": "It does not work.",
                                              "why": "Aluminium holds oxygen more tightly than almost anything. Heat"
                                                      " alone does not come close.",
                                          },
                                 "carbon": {
                                               "works": False,
                                               "title": "It does not work — and this is the important one.",
                                               "why": "Aluminium is above carbon in the reactivity series, so aluminium"
                                                       " holds the oxygen more strongly than carbon can pull. A hotter"
                                                       " furnace changes the speed of reactions that can happen, and this"
                                                       " one cannot.",
                                           },
                                 "electric": {
                                                 "works": True,
                                                 "title": "It works.",
                                                 "why": "A very large current passed through the molten oxide tears it"
                                                         " apart into aluminium and oxygen. Every aluminium object you have"
                                                         " ever held was made this way, and the works are built next to"
                                                         " power stations for a reason.",
                                                 "eq": [
                                                           "aluminium oxide",
                                                           "aluminium + oxygen",
                                                       ],
                                             },
                             },
             },
         ],
         "close_id": "bench-close",
         "close_title": "Six deliveries, four routes, one thing deciding.",
         "close": [
             "Nothing in that list is about how hard the rock is or how deep "
             "the mine is. It is the reactivity series, read against carbon, "
             "deciding how much energy it takes to break the metal free.",
         ]},

        {"type": "key-fact", "ref": "the-carbon-line"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Ore", "Oxide", "Reduction", "Extraction", "Electrolysis"]},

        {"type": "misconception", "id": "think-commit-hotter",
         "anchor": "s-think", "targets": "MATL-09"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "activities": [
        {"id": "think-commit-hotter",
         "kind": "predict",
         "demand": "explain",
         "targets": "MATL-09",
         "prompt": "Hotter fixes a great many things in chemistry. Commit "
                   "before you read on.",
         # ⚑ MRB-177 — 15, 16, 14, 15 words.
         "options": [
             "Right — a hot enough furnace will break any oxide apart in the "
             "end",
             "Wrong — aluminium is above carbon, so carbon has nothing to "
             "pull the oxygen with",
             "Right, because heat is what supplies the energy every reaction "
             "needs",
             "Wrong — no oxide gives up its oxygen to carbon at any "
             "temperature at all",
         ],
         "reveal": [
             "Aluminium oxide is the counter-example, and it is not a rare or "
             "awkward one — it is most of the world's aluminium. Aluminium is "
             "<strong>above</strong> carbon in the series, so it holds oxygen "
             "more tightly than carbon does. Carbon has nothing to pull with, "
             "and a hotter furnace does not change which of the two wants the "
             "oxygen more.",
             "Heat gets a possible reaction going faster. It cannot make an "
             "impossible one possible. <strong>That is why aluminium was a "
             "rarity for most of history and became ordinary within about "
             "thirty years of cheap electricity.</strong>",
         ]},
    ],

    "key_facts": [
        {"id": "the-carbon-line", "placement": "top-level", "ground": "card",
         "eyebrow": "Key fact",
         "text": "Heating a metal oxide with carbon takes the oxygen away and "
                 "leaves the metal — but only for metals below carbon in the "
                 "reactivity series. Metals above carbon have to be split out "
                 "with electricity."},
    ],

    "ladder": {
        # index 1 — moved from Design's 0.
        "recall": {
            "q": "Which of these metals can be obtained from its oxide by "
                 "heating with carbon?",
            "options": ["Aluminium", "Zinc", "Magnesium", "Potassium"],
            "answer": 1,
            "feedback": {
                0: "Aluminium is above carbon in the series, so carbon cannot "
                   "take its oxygen. It needs electricity.",
                2: "Magnesium is above carbon too — well above it.",
                3: "Potassium is at the very top of the series and is the "
                   "hardest of all to free.",
            }},

        # index 0 — Design's own. ⚑ Distractors re-authored for length.
        "apply": {
            "q": "Aluminium is one of the commonest metals in the Earth's "
                 "crust, and in the 1850s it cost more than gold. Which "
                 "statement explains why?",
            "options": [
                "Aluminium is above carbon in the series, so it could not be "
                "freed with carbon and no cheap way to use electricity "
                "existed yet",
                "Aluminium ore was extremely rare until new deposits were "
                "discovered, so for a long time there was very little of it "
                "to work with",
                "Aluminium melts at such a high temperature that no furnace "
                "built anywhere in the world at that time could get anywhere "
                "near it",
                "Aluminium reacts with the air the moment it is made, so "
                "nearly all of what was produced was lost again before it "
                "could be used",
            ],
            "answer": 0,
            "feedback": {
                1: "Aluminium ore is abundant — bauxite is common. Scarcity "
                   "was never the problem.",
                2: "Aluminium melts at 660 °C, which is LOW for a metal. "
                   "Melting was never the difficulty.",
                3: "It does grow an oxide layer, and that layer then protects "
                   "the metal underneath. It is not why it was expensive.",
            }},

        "explain": {
            "q": "Explain why iron can be obtained from its oxide in a "
                 "furnace with carbon, but aluminium cannot, using the "
                 "reactivity series in your answer.",
            "field_label": "Your explanation",
            "placeholder": "Iron is below carbon, so…",
            "success": [
                "Says iron is below carbon in the reactivity series.",
                "Says carbon can therefore take the oxygen from iron oxide.",
                "Says aluminium is above carbon in the series.",
                "Says aluminium holds its oxygen more tightly than carbon "
                "does.",
                "Says aluminium is obtained by passing electricity through "
                "its molten compound instead.",
            ]},

        "produce": {
            "q": "A new metal M is discovered. Its oxide is unchanged when "
                 "heated alone and unchanged when heated with carbon. "
                 "Describe where M sits in the reactivity series and how it "
                 "would have to be extracted.",
            "field_label": "Your answer",
            "placeholder": "M must be above…",
            "success": [
                "Says M is above carbon in the series.",
                "Says carbon cannot take the oxygen from M's oxide.",
                "Says heating alone is not enough either, so M is not near "
                "the bottom.",
                "Says M would have to be extracted using electricity.",
                "Says the extraction would be expensive because of the "
                "electricity it needs.",
            ]},
    },

    "key_note": "An ore is a rock containing enough of a metal compound to be "
                "worth extracting, and most ores are metal oxides. Removing "
                "the oxygen is reduction. A metal below carbon in the "
                "reactivity series can be reduced by heating its oxide with "
                "carbon, which takes the oxygen and leaves the metal — this "
                "is how iron, zinc, copper and lead are obtained. A metal "
                "above carbon holds oxygen too tightly for carbon to remove, "
                "and is obtained by passing electricity through its molten "
                "compound. The few metals below carbon that are least "
                "reactive of all, such as gold, are found in the ground as "
                "the metal itself.",

    "stretch": [
        {"type": "explainer", "id": "blast-furnace",
         "text": "A blast furnace does not mostly work the way the bench "
                 "above suggests. Coke burns to carbon dioxide, the carbon "
                 "dioxide meets more hot coke and becomes carbon monoxide, "
                 "and it is the carbon monoxide that does most of the work of "
                 "taking oxygen off the iron oxide as it falls through. Solid "
                 "carbon touching solid ore is a small part of it. The rule "
                 "you have learned is right about WHICH metals and slightly "
                 "simple about HOW."},
        {"type": "explainer", "id": "recycling-aluminium",
         "text": "Aluminium is expensive to win from its ore and cheap to use "
                 "again. Melting down cans and remaking them takes roughly a "
                 "twentieth of the electricity that extracting the same "
                 "aluminium from bauxite would need, because the hard part — "
                 "prising the oxygen off — has already been paid for once. "
                 "It is the clearest case in chemistry of recycling being an "
                 "energy decision rather than a tidiness one."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Ore",
         "definition": "A rock containing enough of a metal compound to be "
                       "worth digging up and extracting.",
         "note": "Malachite is an ore of copper; bauxite is one of "
                 "aluminium."},
        {"term": "Oxide",
         "definition": "A compound of a metal with oxygen. Most ores are "
                       "oxides, or can be roasted into one.",
         "note": "Which is why extraction is nearly always the same job."},
        {"term": "Reduction",
         "definition": "Removing oxygen from a compound.",
         "note": "The opposite of oxidation, which you met in C5."},
        {"term": "Extraction",
         "definition": "Getting a metal out of its ore as the metal itself.",
         "note": "A reaction, never a temperature."},
        {"term": "Electrolysis",
         "definition": "Splitting a compound apart by passing electricity "
                       "through it when molten or dissolved.",
         "note": "The only route for the metals above carbon."},
    ],

    "safety_note": "The bench is a simulation and is not a method. Reducing "
                   "copper oxide with carbon is a standard school practical "
                   "and the one thing in this unit a class is most likely to "
                   "run: it needs a written risk assessment covering strong "
                   "heating, a reducing mixture and hot residues that stay "
                   "dangerous long after the flame is out.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why a hotter furnace cannot help?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Reduction and oxidation defined by electron transfer, the "
                   "blast furnace equations, and electrolysis of aluminium "
                   "oxide dissolved in molten cryolite.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
