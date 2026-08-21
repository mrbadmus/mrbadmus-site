"""C9 lesson 04 — Ceramics, polymers and composites: twelve questions.

The lesson's argument is one shape: "strong" is not one word, a family tells
you what to expect and a job has to be checked against the particular material,
and a composite is two materials doing what neither could alone. The page
teaches it with four jobs, six materials, and exactly one match each.

These twelve probe the angles the mastery ladder leaves alone: separating
strong from tough in a case where they point opposite ways, what a family
predicts and what it does not, and why a composite is not simply a mixture.

The distractors are built from the lesson's declared misconceptions.

`MATL-11` (if a material shatters it must be weak) drives the wrong options in
e01, s01 and h01.

`MATL-12` (plastic is one material) drives e03, s02 and h03. s02 is the one
that matters: it offers two polymers whose behaviour is opposite, so the belief
has to explain how one word covers both.

`MATL-13` (strong and tough are the same property) drives e02, s03, h02 and
h04, where a single ranking is assumed. h04 is the register's own case put as a
purchasing decision, which is where a student meets it.

⚠️ MRB-278 · ANSWER POSITION. Cycles 0, 1, 2, 3 through each band.

⚠️ BAND VALUES ARE FULL WORDS.
"""

UNIT = "C9"
LESSON = "ceramics-polymers-and-composites"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c9-04-e01",
        "band": "easier",
        "text": "Which set of properties describes a typical ceramic?",
        "options": [
            {"text": "Hard, stiff, stands high temperatures, brittle",
             "correct": True},
            {"text": "Light, flexible, tough, softens when heated",
             "correct": False,
             "why": "That is the polymer list, and every item is the opposite "
                    "of the ceramic one."},
            {"text": "Shiny, malleable, conducts electricity well",
             "correct": False,
             "why": "That is a metal. Ceramics do not conduct."},
            {"text": "Two materials combined, fibres taking the pull",
             "correct": False,
             "why": "That is a composite, which is a way of building rather "
                    "than a set of properties."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e02",
        "band": "easier",
        "text": "A china plate shatters when dropped. A plastic beaker "
                "bounces. Which is the stronger material?",
        "options": [
            {"text": "The beaker, because it survived the fall",
             "correct": False,
             "why": "Surviving a knock is toughness. Strength is how much "
                    "force it takes to break something."},
            {"text": "The plate, because it takes far more force to break",
             "correct": True},
            {"text": "Neither — they are equally strong in different ways",
             "correct": False,
             "why": "They differ on both properties, and the plate is clearly "
                    "the stronger."},
            {"text": "The beaker, because it can be bent without damage",
             "correct": False,
             "why": "Bending without damage is toughness again, and it comes "
                    "with being WEAKER here."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e03",
        "band": "easier",
        "text": "A carrier bag goes soft in hot water but a kettle body holds "
                "boiling water and stays rigid. Both are polymers. What does "
                "that show?",
        "options": [
            {"text": "One of them cannot really be a polymer",
             "correct": False,
             "why": "Both are. Long chains of atoms is what makes a polymer, "
                    "and both have them."},
            {"text": "The kettle must have a metal layer hidden inside it",
             "correct": False,
             "why": "Plenty of kettle bodies are polymer throughout and still "
                    "hold boiling water."},
            {"text": "“Polymer” is a family, and its members "
                     "differ widely",
             "correct": True},
            {"text": "The bag was faulty and should have held the heat too",
             "correct": False,
             "why": "It behaved exactly as that polymer is supposed to. It is "
                    "a different polymer."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e04",
        "band": "easier",
        "text": "What makes reinforced concrete a composite?",
        "options": [
            {"text": "It is heavier than either concrete or steel on their "
                     "own",
             "correct": False,
             "why": "Weight is not what the word means, and it is not even "
                    "true of the steel."},
            {"text": "It is made in a factory rather than mixed on site",
             "correct": False,
             "why": "Where it is made has nothing to do with it."},
            {"text": "It contains more than one chemical element in it",
             "correct": False,
             "why": "So does plain concrete, and so does almost everything."},
            {"text": "Steel bars and concrete together do what neither does "
                     "alone",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c9-04-s01",
        "band": "standard",
        "text": "What does brittle mean?",
        "options": [
            {"text": "It breaks all at once rather than bending first",
             "correct": True},
            {"text": "It breaks under a small force, unlike a strong material",
             "correct": False,
             "why": "That is being weak. A ceramic tile is brittle and takes "
                    "an enormous force."},
            {"text": "It wears away gradually when it is rubbed",
             "correct": False,
             "why": "That is abrasion, and most ceramics resist it very "
                    "well."},
            {"text": "It becomes weaker each time it is loaded and unloaded",
             "correct": False,
             "why": "That is fatigue, and it happens to metals rather more "
                    "than to ceramics."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s02",
        "band": "standard",
        "text": "A fizzy drink kept in a polyethene bottle goes flat within "
                "days; the same drink in a PET bottle does not. Why?",
        "options": [
            {"text": "Polyethene dissolves slowly into the drink and spoils "
                     "it",
             "correct": False,
             "why": "Nothing dissolves in. The gas leaves, which is a "
                    "different problem."},
            {"text": "Polyethene lets carbon dioxide pass through it and PET "
                     "does not",
             "correct": True},
            {"text": "Polyethene bottles are always made with a looser cap",
             "correct": False,
             "why": "The cap is not the route. The wall of the bottle is."},
            {"text": "PET is a much thicker plastic, so it simply holds more",
             "correct": False,
             "why": "PET bottles are thin. It is what the material does, not "
                    "how much of it there is."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s03",
        "band": "standard",
        "text": "A bicycle frame has to be light, stiff, and survive repeated "
                "knocks. Why does a ceramic fail that job?",
        "options": [
            {"text": "Because ceramics are too heavy for a bicycle frame",
             "correct": False,
             "why": "Some ceramics are light. The knocks are the problem."},
            {"text": "Because ceramics are not stiff enough to hold a frame's "
                     "shape",
             "correct": False,
             "why": "Ceramics are extremely stiff. That part of the job they "
                    "pass."},
            {"text": "Because a ceramic is brittle and a knock would crack it "
                     "outright",
             "correct": True},
            {"text": "Because ceramics cannot be made in the shape of a tube",
             "correct": False,
             "why": "They can be. The shape is not what rules them out."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s04",
        "band": "standard",
        "text": "Two of the four jobs on the bench are won by ceramics, and "
                "neither ceramic could do the other's job. What does that "
                "show?",
        "options": [
            {"text": "That one of the two is not really a ceramic at all",
             "correct": False,
             "why": "Both are, and both behave like ceramics — hard, stiff "
                    "and heat-resistant."},
            {"text": "That the families are not a useful way to sort "
                     "materials",
             "correct": False,
             "why": "The families predicted both of them well. They just do "
                    "not predict everything."},
            {"text": "That a job can only ever be done by one family of "
                     "material",
             "correct": False,
             "why": "The four jobs were won from three different families, "
                    "which is the opposite."},
            {"text": "That the family tells you what to expect and the "
                     "particular material still has to be checked",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c9-04-h01",
        "band": "harder",
        "text": "Why is “which material is better?” not a "
                "question that can be answered on its own?",
        "options": [
            {"text": "Because better depends entirely on what the material "
                     "has to survive",
             "correct": True},
            {"text": "Because every material is better than every other at "
                     "something",
             "correct": False,
             "why": "Close and not quite the point: the job comes first, not "
                    "the material's list of talents."},
            {"text": "Because no two materials can be compared without "
                     "measuring them",
             "correct": False,
             "why": "They can be measured. The measurements still do not "
                    "produce a single ranking."},
            {"text": "Because new materials are invented faster than they can "
                     "be ranked",
             "correct": False,
             "why": "True of engineering and irrelevant to whether one "
                    "ranking could exist."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h02",
        "band": "harder",
        "text": "Reinforced concrete is used for bridges. What is each of the "
                "two materials contributing?",
        "options": [
            {"text": "The steel resists being squashed and the concrete "
                     "resists being pulled",
             "correct": False,
             "why": "It is the other way round. Concrete is strong in "
                    "compression and weak in tension."},
            {"text": "The concrete takes the pull and the steel spreads the "
                     "load across it",
             "correct": True},
            {"text": "Both take the same loads, so the pair is simply twice "
                     "as strong",
             "correct": False,
             "why": "A composite is not a doubling. Each material does the "
                    "job the other cannot."},
            {"text": "The steel keeps the concrete dry and stops it cracking "
                     "in frost",
             "correct": False,
             "why": "Steel in concrete does the opposite — it has to be kept "
                    "dry itself, or it rusts."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h03",
        "band": "harder",
        "text": "A designer needs a see-through door for a wood-fired oven "
                "lit every evening and left cold overnight. Why is ordinary "
                "window glass the wrong choice?",
        "options": [
            {"text": "Because glass is not see-through enough once it is "
                     "warm",
             "correct": False,
             "why": "It stays transparent. Transparency is not what fails."},
            {"text": "Because glass is a polymer and polymers soften when "
                     "heated",
             "correct": False,
             "why": "Glass is treated as a ceramic here, and it does not "
                    "soften at oven temperatures."},
            {"text": "Because it would crack from being heated and cooled "
                     "every day",
             "correct": True},
            {"text": "Because glass conducts heat too well and would burn "
                     "somebody",
             "correct": False,
             "why": "Ceramics are poor conductors. That is one of the "
                    "properties the job wants."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h04",
        "band": "harder",
        "text": "A cracked carbon-fibre bicycle frame is currently shredded, "
                "burned or buried, while a cracked steel one is melted down "
                "and reused. What is the trade-off a composite makes?",
        "options": [
            {"text": "It costs more to buy, so fewer of them are made in the "
                     "first place",
             "correct": False,
             "why": "Price is a consequence. The difficulty is physical."},
            {"text": "It is weaker than steel, so it cracks more often and "
                     "sooner",
             "correct": False,
             "why": "Carbon fibre is stiffer and lighter than steel for the "
                    "same job. Failure rate is not the issue."},
            {"text": "It cannot be repaired, so a crack ends the frame's life "
                     "immediately",
             "correct": False,
             "why": "Composite frames are repaired. What is hard is "
                    "separating them at the end."},
            {"text": "Being two materials in one is what makes it good, and "
                     "what makes it hard to take apart again",
             "correct": True},
        ],
        "figure": None,
    },
]
