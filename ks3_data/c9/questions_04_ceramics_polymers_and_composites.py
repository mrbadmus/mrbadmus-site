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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c9-04-e05",
        "band": "easier",
        "text": "What is a polymer?",
        "options": [
            {"text": "A material made by firing clay or minerals hard, so "
                     "that it becomes stiff enough to stand a high "
                     "temperature without softening",
             "correct": False,
             "why": "That is a ceramic. A polymer softens or burns when it is "
                    "heated"},
            {"text": "Two materials built into one",
             "correct": False,
             "why": "That is a composite"},
            {"text": "Another word for plastic",
             "correct": False,
             "why": "Close, and plastic is one family of polymers. Wool and "
                    "DNA are polymers too"},
            {"text": "A material built from very long chains of atoms",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e06",
        "band": "easier",
        "text": "What does TOUGH mean, as this lesson uses it?",
        "options": [
            {"text": "Absorbs a knock and keeps going, usually by giving a "
                     "little",
             "correct": True},
            {"text": "Takes a large force before it fails, however it then "
                     "gives way",
             "correct": False,
             "why": "That is STRONG. Tough is about surviving a knock, "
                    "usually by giving a little"},
            {"text": "Breaks all at once rather than bending",
             "correct": False,
             "why": "That is brittle, which is the opposite of tough"},
            {"text": "Hard to scratch",
             "correct": False,
             "why": "That is hardness. A hard material can still shatter"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e07",
        "band": "easier",
        "text": "Which of these is a ceramic?",
        "options": [
            {"text": "Polythene",
             "correct": False,
             "why": "A polymer — long chains, and it softens in hot water"},
            {"text": "Brick",
             "correct": True},
            {"text": "Reinforced concrete, which is used for the whole of a "
                     "bridge and is fired hard in the same way that a brick "
                     "or a floor tile is",
             "correct": False,
             "why": "It is a composite of concrete and steel, and it is not "
                    "fired at all"},
            {"text": "Copper wire",
             "correct": False,
             "why": "A metal, and an element"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e08",
        "band": "easier",
        "text": "What happens to a polymer when it is heated?",
        "options": [
            {"text": "It becomes harder and stiffer, which is why plastics "
                     "are fired in ovens in the same way that clay is before "
                     "they can be used for anything demanding",
             "correct": False,
             "why": "Firing is what a CERAMIC needs. A polymer goes the other "
                    "way"},
            {"text": "Nothing at all",
             "correct": False,
             "why": "A carrier bag in hot water goes soft within seconds"},
            {"text": "It softens or burns",
             "correct": True},
            {"text": "It conducts electricity",
             "correct": False,
             "why": "Polymers are insulators hot or cold. That is much of "
                    "what they are used for"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e09",
        "band": "easier",
        "text": "In a composite, what do the FIBRES do?",
        "options": [
            {"text": "Hold everything in place and spread the load out across "
                     "the whole of the material, so that no one part of it "
                     "has to carry more than its share",
             "correct": False,
             "why": "That is what the surrounding material does. The fibres "
                    "take the pull"},
            {"text": "Make the material lighter",
             "correct": False,
             "why": "They often do, and it is a side effect. Their job is to "
                    "carry a pulling force"},
            {"text": "Keep water out",
             "correct": False,
             "why": "The surround does that where it matters. The fibres are "
                    "structural"},
            {"text": "Take the pull",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e10",
        "band": "easier",
        "text": "Which property does a ceramic NOT have?",
        "options": [
            {"text": "Toughness",
             "correct": True},
            {"text": "Stiffness",
             "correct": False,
             "why": "Ceramics are very stiff, which is part of why they are "
                    "used for floors"},
            {"text": "Heat resistance",
             "correct": False,
             "why": "Standing heat is one of a ceramic's best properties"},
            {"text": "Hardness",
             "correct": False,
             "why": "Ceramics are hard — a tile is difficult to scratch"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e11",
        "band": "easier",
        "text": "Do ceramics conduct electricity?",
        "options": [
            {"text": "Yes, once they have been fired, because firing drives "
                     "out the water in the clay and leaves a path through the "
                     "material for a current to follow",
             "correct": False,
             "why": "Firing does drive off water and does not make a "
                    "conductor. Ceramics insulate"},
            {"text": "No",
             "correct": True},
            {"text": "Only when they are hot",
             "correct": False,
             "why": "A hot tile is still an insulator. That is why they are "
                    "used around heating elements"},
            {"text": "Only if they contain metal",
             "correct": False,
             "why": "A ceramic with metal in it would be a composite. A "
                    "ceramic on its own does not conduct"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e12",
        "band": "easier",
        "text": "What does STRONG mean, in this lesson's careful sense?",
        "options": [
            {"text": "Survives being dropped, knocked and bent without "
                     "cracking, which is what people usually mean when they "
                     "call a material a strong one",
             "correct": False,
             "why": "That is toughness. The plate is strong AND shatters"},
            {"text": "Is heavy for its size",
             "correct": False,
             "why": "That is density. Carbon fibre is light and very strong"},
            {"text": "Takes a large force before it fails",
             "correct": True},
            {"text": "Lasts a long time outdoors",
             "correct": False,
             "why": "That is durability, and it is a different question "
                    "again"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e13",
        "band": "easier",
        "text": "Why is a floor tile a good example of a ceramic?",
        "options": [
            {"text": "It is light, easily shaped and flexible enough to be "
                     "laid over a floor that is not perfectly level before it "
                     "is grouted into place",
             "correct": False,
             "why": "Every one of those is a POLYMER's properties. A tile is "
                    "none of them"},
            {"text": "It conducts heat away from the room",
             "correct": False,
             "why": "It feels cold underfoot and is a poor conductor "
                    "compared with a metal"},
            {"text": "It can be melted and reshaped",
             "correct": False,
             "why": "A fired ceramic cannot be reshaped. That is a polymer's "
                    "property"},
            {"text": "It is hard, stiff, stands heat, and cracks rather than "
                     "bending",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c9-04-s05",
        "band": "standard",
        "text": "Why does calling something STRONG say nothing about how it "
                "will fail?",
        "options": [
            {"text": "Because strength is measured in a laboratory and "
                     "failure happens in the real world, so the two are never "
                     "compared directly with each other",
             "correct": False,
             "why": "Both are measured in the same test. They are simply "
                    "different things about it"},
            {"text": "Because a strong material never fails",
             "correct": False,
             "why": "Everything fails at some load. Strength says at what "
                    "load"},
            {"text": "Because strong and tough mean the same thing",
             "correct": False,
             "why": "They are different properties, which is the whole point "
                    "of the plate and the beaker"},
            {"text": "Because strength is the force it takes before failure, "
                     "and failure can be a crack or a bend",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s06",
        "band": "standard",
        "text": "A kitchen worktop has to resist scratches, stand a hot pan, "
                "and not crack when something heavy is dropped on it. Which "
                "property is hardest to get?",
        "options": [
            {"text": "Not cracking, because the materials that are hard and "
                     "heat-proof are usually brittle",
             "correct": True},
            {"text": "Standing a hot pan, because almost no material used "
                     "indoors can take a temperature that high without "
                     "softening or burning where the pan has touched it",
             "correct": False,
             "why": "Ceramics and stone stand a hot pan easily. It is the "
                    "toughness that pulls against the rest"},
            {"text": "Resisting scratches",
             "correct": False,
             "why": "Plenty of hard materials resist scratches. The conflict "
                    "is between hardness and toughness"},
            {"text": "None — one material does all three easily",
             "correct": False,
             "why": "The three pull against each other, which is why worktops "
                    "are a compromise"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s07",
        "band": "standard",
        "text": "Why is a composite better for a bridge than either of its "
                "materials alone?",
        "options": [
            {"text": "Because two materials together are twice as strong as "
                     "one, so a bridge built out of a composite can carry "
                     "twice the weight of a bridge built out of either",
             "correct": False,
             "why": "A composite is not a doubling. Each material does the "
                    "job the other cannot"},
            {"text": "Because the fibres carry the pull and the surround "
                     "holds them and spreads the load",
             "correct": True},
            {"text": "Because a composite is cheaper",
             "correct": False,
             "why": "Composites are often more expensive. They are used for "
                    "what they do"},
            {"text": "Because the two materials react together",
             "correct": False,
             "why": "Nothing reacts. They are combined physically"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s08",
        "band": "standard",
        "text": "Glass and porcelain are both ceramics, and one is "
                "see-through. What does that tell you about the family?",
        "options": [
            {"text": "That glass is not really a ceramic, since a material "
                     "that lets light through it cannot be in the same family "
                     "as one that does not",
             "correct": False,
             "why": "Glass is a ceramic. Being see-through is not part of the "
                    "definition"},
            {"text": "That ceramics vary in every property",
             "correct": False,
             "why": "They share hardness, stiffness, heat resistance and "
                    "brittleness. Appearance varies"},
            {"text": "That a family sets what to expect, and each material "
                     "still has to be checked",
             "correct": True},
            {"text": "That porcelain is stronger",
             "correct": False,
             "why": "Their strengths are comparable, and it is not what the "
                    "pair is showing"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s09",
        "band": "standard",
        "text": "A crash helmet has a hard outer shell and a crushable "
                "lining. What is each part doing?",
        "options": [
            {"text": "The shell absorbs the blow by cracking, and the lining "
                     "holds the pieces of it together so that none of them "
                     "reaches the head underneath",
             "correct": False,
             "why": "The shell is there to spread the force over a wide area. "
                    "The crushing is the lining's job"},
            {"text": "Both spread the blow equally",
             "correct": False,
             "why": "They do different jobs, which is why the helmet has "
                    "two layers"},
            {"text": "The lining keeps the shell dry",
             "correct": False,
             "why": "Nothing here is about water. Both layers are "
                    "structural"},
            {"text": "The shell spreads the blow; the lining absorbs it by "
                     "giving way",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s10",
        "band": "standard",
        "text": "A ceramic mug and a polymer mug are both filled with boiling "
                "water. What is the practical difference?",
        "options": [
            {"text": "The ceramic one stands the heat easily; the polymer one "
                     "may soften",
             "correct": True},
            {"text": "The ceramic one conducts the heat straight through to "
                     "your hand, and the polymer one keeps it in, which is "
                     "why hot drinks are served in plastic cups",
             "correct": False,
             "why": "A ceramic mug is a poor conductor too — that is why it "
                    "can be held. The difference is the softening"},
            {"text": "Neither is affected",
             "correct": False,
             "why": "Boiling water softens many polymers noticeably"},
            {"text": "The polymer one cracks",
             "correct": False,
             "why": "Cracking is what a ceramic does. A polymer gives way by "
                    "softening"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s11",
        "band": "standard",
        "text": "Carbon fibre is used for a racing bicycle frame and steel "
                "for a delivery bike. What is being traded?",
        "options": [
            {"text": "Strength against toughness, since carbon fibre is far "
                     "stronger than steel and steel is by far the tougher of "
                     "the two materials in every use",
             "correct": False,
             "why": "That names two real properties in the wrong shape. What "
                    "decides a delivery bike is cost and repairability"},
            {"text": "Weight and stiffness against cost and ease of repair",
             "correct": True},
            {"text": "Nothing — carbon fibre is better in every way",
             "correct": False,
             "why": "It costs far more and a cracked frame cannot be welded"},
            {"text": "Conductivity against insulation",
             "correct": False,
             "why": "Neither property matters for a bicycle frame"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s12",
        "band": "standard",
        "text": "Why is BRITTLE not the same as WEAK?",
        "options": [
            {"text": "Because a weak material fails slowly and a brittle one "
                     "fails quickly, so the two words describe how long the "
                     "failure takes rather than how much force it needs",
             "correct": False,
             "why": "Speed is not the difference. One word is about the force "
                    "and the other about the manner"},
            {"text": "Because brittle materials are always harder",
             "correct": False,
             "why": "Often true and not the definition. A hard material can "
                    "be tough"},
            {"text": "Because a brittle material can take a very large force "
                     "before it fails — it just fails all at once",
             "correct": True},
            {"text": "Because weak materials never break",
             "correct": False,
             "why": "They break easily, which is what weak means"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s13",
        "band": "standard",
        "text": "A drinks bottle has to be light, unbreakable when dropped, "
                "and hold gas in. Which family, and why?",
        "options": [
            {"text": "A ceramic, because a ceramic is completely airtight and "
                     "gas is exactly the thing that a fizzy drink has to be "
                     "stopped from losing",
             "correct": False,
             "why": "Airtight is true and a ceramic bottle shatters when "
                    "dropped. Toughness rules it out"},
            {"text": "A metal, because metals are tough",
             "correct": False,
             "why": "A metal can is used and it is heavier and cannot be "
                    "resealed. For a bottle a polymer wins"},
            {"text": "A composite, because two materials always beat one",
             "correct": False,
             "why": "Two materials are used where one cannot do the job. Here "
                    "one can"},
            {"text": "A polymer, because it is light and tough, and the right "
                     "one keeps carbon dioxide in",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c9-04-h05",
        "band": "harder",
        "text": "Concrete spalls in a fire — flakes blow off the face. What "
                "causes that?",
        "options": [
            {"text": "The steel bars inside expand faster than the concrete "
                     "around them, and push the surface off from the inside "
                     "as the whole beam is heated through",
             "correct": False,
             "why": "The bars do expand, and spalling happens on plain "
                    "concrete with no steel in it at all"},
            {"text": "The concrete burns",
             "correct": False,
             "why": "Concrete does not burn. It is steam pressure that does "
                    "the damage"},
            {"text": "The concrete melts at the surface",
             "correct": False,
             "why": "It does not reach anything like its melting point in an "
                    "ordinary fire"},
            {"text": "Water in tiny pores turns to steam faster than it can "
                     "escape, and the pressure lifts flakes off",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h06",
        "band": "harder",
        "text": "Why is a composite harder to RECYCLE than either of the "
                "materials in it?",
        "options": [
            {"text": "Because being two materials in one is what makes it "
                     "good, and separating them again is the difficulty",
             "correct": True},
            {"text": "Because the two materials react together over time, so "
                     "that what comes back at the end of a frame's life is "
                     "neither of the two things that went into it",
             "correct": False,
             "why": "Nothing reacts. The materials are still there, and they "
                    "are bonded together physically"},
            {"text": "Because composites are always contaminated",
             "correct": False,
             "why": "A clean composite is just as hard to separate. The "
                    "combination itself is the problem"},
            {"text": "Because there is no demand for the materials",
             "correct": False,
             "why": "There is demand for both. Getting them apart is what "
                    "stops it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h07",
        "band": "harder",
        "text": "A material is described as strong, stiff, light AND brittle. "
                "Which job would suit it worst?",
        "options": [
            {"text": "A bridge deck, since a deck has to carry an enormous "
                     "steady load and anything brittle would give way under "
                     "the weight of the traffic on it",
             "correct": False,
             "why": "A steady load is what a brittle material is BEST at. It "
                    "is the sudden blow that kills it"},
            {"text": "A hammer head",
             "correct": True},
            {"text": "A window pane",
             "correct": False,
             "why": "Glass is exactly this description and does the job "
                    "perfectly well"},
            {"text": "A floor tile",
             "correct": False,
             "why": "A steady load spread across a tile is what a ceramic "
                    "handles best"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h08",
        "band": "harder",
        "text": "The lesson says a see-through oven door must survive being "
                "heated and cooled EVERY DAY, not just being hot. Why is that "
                "the harder requirement?",
        "options": [
            {"text": "Because a material heated and cooled many times becomes "
                     "weaker",
             "correct": False,
             "why": "That is a fair description of fatigue and it is not what "
                    "cracks glass. Uneven expansion does it in one cycle"},
            {"text": "Because the oven gets hotter each time it is lit",
             "correct": False,
             "why": "It reaches about the same temperature each evening. The "
                    "cycling is the problem"},
            {"text": "Because repeated expanding and contracting cracks a "
                     "brittle material even when the temperature is never too "
                     "high for it",
             "correct": True},
            {"text": "Because the glass gets dirty",
             "correct": False,
             "why": "Cleaning is a nuisance rather than a failure of the "
                    "material"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h09",
        "band": "harder",
        "text": "Which pair of properties makes ceramics good for the inside "
                "of a furnace and bad for a hammer?",
        "options": [
            {"text": "Hardness and stiffness, since a furnace lining has to "
                     "be hard enough to resist the flame and a hammer head "
                     "has to be able to give slightly as it strikes",
             "correct": False,
             "why": "Hardness suits both jobs. What rules out the hammer is "
                    "that a ceramic shatters under a blow"},
            {"text": "Lightness and stiffness",
             "correct": False,
             "why": "Ceramics are not especially light, and lightness is not "
                    "what decides either job"},
            {"text": "Conductivity and hardness",
             "correct": False,
             "why": "Ceramics do not conduct, and that is useful for a "
                    "furnace rather than relevant to a hammer"},
            {"text": "Heat resistance and brittleness",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h10",
        "band": "harder",
        "text": "Two polymers behave completely differently in hot water. "
                "What does that mean for the word POLYMER on a data sheet?",
        "options": [
            {"text": "It names a family, so the particular polymer still has "
                     "to be identified",
             "correct": True},
            {"text": "It is a useless word, since a name that covers "
                     "materials as different as a carrier bag and a kettle "
                     "body tells an engineer nothing they can use",
             "correct": False,
             "why": "It tells you a great deal — light, shapeable, "
                    "insulating, softens with heat. It just does not tell you "
                    "which one"},
            {"text": "One of the two has been labelled wrongly",
             "correct": False,
             "why": "Both are polymers. The family is genuinely wide"},
            {"text": "The word means the same as plastic",
             "correct": False,
             "why": "Plastics are one part of it, and the point here is about "
                    "how wide the family is"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h11",
        "band": "harder",
        "text": "Why does a composite depend on its two materials STAYING "
                "joined to each other?",
        "options": [
            {"text": "Because the two materials protect each other from the "
                     "weather, and a gap between them would let water in and "
                     "start the steel rusting from the inside",
             "correct": False,
             "why": "Water getting in is a real long-term problem and it is "
                    "not the structural point. The load has to cross the "
                    "join"},
            {"text": "Because the load is passed between them — separate "
                     "them and each is back to its own weakness",
             "correct": True},
            {"text": "Because they would otherwise react with each other",
             "correct": False,
             "why": "They do not react at all. What they do is share a "
                    "load"},
            {"text": "Because a composite is only counted as one material "
                     "while the two parts are touching",
             "correct": False,
             "why": "That is a point about naming. The engineering reason is "
                    "that the load is passed across"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h12",
        "band": "harder",
        "text": "A designer wants one material for a bicycle frame that is "
                "light, stiff, tough and cheap. Why is that specification hard "
                "to meet?",
        "options": [
            {"text": "Because no material is both light and stiff at the same "
                     "time",
             "correct": False,
             "why": "Carbon fibre is both, and it is expensive. Cost is where "
                    "the specification breaks"},
            {"text": "Because toughness and stiffness cannot go together",
             "correct": False,
             "why": "Steel is both, which is why it is used for so many "
                    "frames"},
            {"text": "Because the materials that are light and stiff are "
                     "expensive, and the cheap ones are heavier",
             "correct": True},
            {"text": "Because a frame has to be made from a composite",
             "correct": False,
             "why": "Steel and aluminium frames are single materials and work "
                    "perfectly well"},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h13",
        "band": "harder",
        "text": "Reinforced concrete lost the pizza-oven job in this lesson. "
                "What exactly ruled it out?",
        "options": [
            {"text": "The temperature itself, since a wood fire burns far "
                     "hotter than concrete can stand and the oven would fail "
                     "on the first evening it was lit",
             "correct": False,
             "why": "Concrete stands the temperature. It is the CYCLING that "
                    "spalls the face off"},
            {"text": "The steel inside rusting",
             "correct": False,
             "why": "A real long-term problem for concrete and not what ruled "
                    "it out here"},
            {"text": "Its weight",
             "correct": False,
             "why": "An oven is not carried about. Weight was never the "
                    "objection"},
            {"text": "The same surface being taken up and down through a high "
                     "temperature every day",
             "correct": True},
        ],
        "figure": None,
    },
]
