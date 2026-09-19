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
            {"text": "The steel takes the pull and the concrete takes the "
                     "squashing load",
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

    # ── easier · MRB-338 night 3 top-up ─────────────────────────────────
    {
        "id": "c9-04-e14",
        "band": "easier",
        "text": "Why does firebrick fail the “see-through” requirement in "
                "the bench?",
        "options": [
            {"text": "It is opaque", "correct": True},
            {"text": "It is coloured bright red, which blocks light",
             "correct": False,
             "why": "Colour is not the reason given. Being opaque is."},
            {"text": "It is too thick to see through", "correct": False,
             "why": "Thickness is not the reason given. The material "
                    "itself does not let light through."},
            {"text": "It has not been polished smooth", "correct": False,
             "why": "Polishing changes shine, not whether light passes "
                    "through the material at all."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e15",
        "band": "easier",
        "text": "Firebrick and heat-proof glass-ceramic are the two "
                "materials on the bench that both fail “does not shatter "
                "when dropped”. What do they have in common?",
        "options": [
            {"text": "They are both composites", "correct": False,
             "why": "Both are ceramics, not composites."},
            {"text": "They are both ceramics", "correct": True},
            {"text": "They are both polymers", "correct": False,
             "why": "Neither is a polymer. Polymers on the bench meet this "
                    "requirement rather than fail it."},
            {"text": "They are both made from crude oil", "correct": False,
             "why": "Neither comes from crude oil. That describes "
                    "polymers, a different family."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e16",
        "band": "easier",
        "text": "Why does firebrick fail “holds pressurised gas in”?",
        "options": [
            {"text": "It reacts with the gas chemically", "correct": False,
             "why": "Nothing here is a chemical reaction. The gas simply "
                    "escapes through the material."},
            {"text": "It is too heavy to hold gas", "correct": False,
             "why": "Weight has nothing to do with whether gas can escape "
                    "through a material."},
            {"text": "Fired clay is full of tiny holes", "correct": True},
            {"text": "It cracks the moment gas is added", "correct": False,
             "why": "Nothing about adding gas cracks a firebrick. The "
                    "porosity is the reason given."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e17",
        "band": "easier",
        "text": "Why does polythene fail “holds pressurised gas in”?",
        "options": [
            {"text": "It melts as soon as gas is added", "correct": False,
             "why": "Nothing about adding gas melts polythene. The gas "
                    "simply passes through the material."},
            {"text": "It dissolves in the gas", "correct": False,
             "why": "Polythene does not dissolve in carbon dioxide."},
            {"text": "It is too thin to hold anything", "correct": False,
             "why": "Thinness is not the reason given — the material "
                    "itself lets the gas seep through."},
            {"text": "Carbon dioxide seeps through it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e18",
        "band": "easier",
        "text": "An empty PET bottle crumples easily in one hand. What keeps "
                "a full, sealed one rigid?",
        "options": [
            {"text": "The pressure of the gas inside", "correct": True},
            {"text": "The label wrapped around it", "correct": False,
             "why": "A label adds no strength to the bottle wall."},
            {"text": "The drink freezing solid inside it", "correct": False,
             "why": "The drink stays liquid. Freezing plays no part in "
                    "this."},
            {"text": "The cap being screwed on tightly", "correct": False,
             "why": "The cap seals the bottle. It is the sealed gas "
                    "pressure that firms up the wall."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e19",
        "band": "easier",
        "text": "Why does carbon-fibre composite fail “stands red heat”?",
        "options": [
            {"text": "The carbon fibres themselves melt at a low "
                     "temperature", "correct": False,
             "why": "It is the resin that fails first, not the fibres "
                    "themselves."},
            {"text": "The resin holding the fibres together chars first",
             "correct": True},
            {"text": "It reacts explosively with hot air", "correct": False,
             "why": "Nothing here explodes. The resin simply chars under "
                    "strong heat."},
            {"text": "It is too light in weight to hold its own shape "
                     "once the furnace gets very hot", "correct": False,
             "why": "Weight is not the reason given for this failure."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e20",
        "band": "easier",
        "text": "Which single material on the bench is described as “the "
                "heaviest thing on the shelf”?",
        "options": [
            {"text": "Firebrick", "correct": False,
             "why": "Firebrick is heavy too, and it is not the one "
                    "described this way."},
            {"text": "Carbon-fibre composite", "correct": False,
             "why": "Carbon-fibre composite is one of the lightest "
                    "materials on the shelf."},
            {"text": "Reinforced concrete", "correct": True},
            {"text": "Heat-proof glass-ceramic", "correct": False,
             "why": "A safe pane of it is heavy, and it is not the one "
                    "singled out as heaviest."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e21",
        "band": "easier",
        "text": "Why does heat-proof glass-ceramic fail “cheap by the "
                "square metre”?",
        "options": [
            {"text": "It has to be imported from abroad", "correct": False,
             "why": "Where it comes from is not the reason given."},
            {"text": "It needs a licence to buy", "correct": False,
             "why": "Nothing about a licence is mentioned. The cost "
                    "itself is the reason."},
            {"text": "It is taxed more heavily than other materials",
             "correct": False,
             "why": "Tax is not the reason given for its cost."},
            {"text": "A sheet of it costs many times what firebrick "
                     "does", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e22",
        "band": "easier",
        "text": "What do we call the property that measures how hard a "
                "material is to scratch?",
        "options": [
            {"text": "Hardness", "correct": True},
            {"text": "Toughness", "correct": False,
             "why": "Toughness is about surviving a knock, not resisting "
                    "a scratch."},
            {"text": "Strength", "correct": False,
             "why": "Strength is about the force needed to break a "
                    "material, not to scratch it."},
            {"text": "Stiffness", "correct": False,
             "why": "Stiffness is about resisting bending, not resisting "
                    "a scratch."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e23",
        "band": "easier",
        "text": "Why does carbon-fibre composite fail “see-through”?",
        "options": [
            {"text": "It is coated in a dark paint", "correct": False,
             "why": "Nothing here is painted. The material's own colour "
                    "and weave block light."},
            {"text": "It is black, and the weave of the fibres shows",
             "correct": True},
            {"text": "It is wrapped in an opaque plastic film",
             "correct": False,
             "why": "No film is mentioned. The composite itself is not "
                    "see-through."},
            {"text": "The resin used sets cloudy", "correct": False,
             "why": "Cloudiness is not the reason given — the material's "
                    "colour and weave are."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e24",
        "band": "easier",
        "text": "Why does reinforced concrete fail “see-through”?",
        "options": [
            {"text": "It is deliberately tinted grey during mixing",
             "correct": False,
             "why": "Tinting is not the reason. Concrete is simply "
                    "opaque."},
            {"text": "The steel bars inside block the light",
             "correct": False,
             "why": "The concrete itself is opaque, quite apart from the "
                    "steel bars inside it."},
            {"text": "It is opaque", "correct": True},
            {"text": "It is coated with a reflective layer", "correct": False,
             "why": "No coating is mentioned. The material is opaque on "
                    "its own."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e25",
        "band": "easier",
        "text": "Why does firebrick fail “takes repeated flexing and "
                "knocks”?",
        "options": [
            {"text": "It flexes too easily and never springs back",
             "correct": False,
             "why": "Firebrick does not flex easily at all. It cracks "
                    "instead."},
            {"text": "It is too slippery to grip", "correct": False,
             "why": "Grip is not what this requirement is about."},
            {"text": "It wears away when rubbed", "correct": False,
             "why": "Wearing away is a different property from flexing "
                    "and taking knocks."},
            {"text": "It does not flex at all — the first bend is a "
                     "crack", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e26",
        "band": "easier",
        "text": "Why does heat-proof glass-ceramic fail “does not shatter "
                "when dropped”?",
        "options": [
            {"text": "A sharp knock on a corner and it goes",
             "correct": True},
            {"text": "It is too slippery to hold onto safely",
             "correct": False,
             "why": "Grip is not the reason given for this failure."},
            {"text": "It reacts with the air and weakens over time",
             "correct": False,
             "why": "Nothing here is a chemical reaction with the air."},
            {"text": "It is too heavy to carry without dropping it",
             "correct": False,
             "why": "Weight is a separate property from what happens once "
                    "it is dropped."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e27",
        "band": "easier",
        "text": "Why does PET fail “stands red heat”?",
        "options": [
            {"text": "It catches fire the moment it is warmed even "
                     "slightly", "correct": False,
             "why": "PET does not catch fire at these temperatures. It "
                    "buckles and softens instead."},
            {"text": "It buckles in an oven and softens in boiling water",
             "correct": True},
            {"text": "It turns black under heat", "correct": False,
             "why": "Colour change is not the reason given for this "
                    "failure."},
            {"text": "It becomes strongly magnetic once it is heated in "
                     "the furnace", "correct": False,
             "why": "PET does not become magnetic. It softens under "
                    "heat."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e28",
        "band": "easier",
        "text": "Why does polythene fail “stiff under load”?",
        "options": [
            {"text": "It shatters under the smallest load", "correct": False,
             "why": "Polythene does not shatter. It bends easily instead."},
            {"text": "It dissolves under a steady load", "correct": False,
             "why": "Nothing about a load makes polythene dissolve."},
            {"text": "A sheet of it bends between your fingers",
             "correct": True},
            {"text": "It cracks along straight lines", "correct": False,
             "why": "Cracking along lines is not how polythene fails "
                    "this requirement — bending easily is."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e29",
        "band": "easier",
        "text": "Which material is described as “the most expensive "
                "material on the shelf by a wide margin”?",
        "options": [
            {"text": "Heat-proof glass-ceramic", "correct": False,
             "why": "It is expensive too, and it is not the one singled "
                    "out this way."},
            {"text": "Reinforced concrete", "correct": False,
             "why": "Concrete is one of the cheaper materials on the "
                    "shelf."},
            {"text": "PET", "correct": False,
             "why": "PET is one of the cheaper materials on the shelf."},
            {"text": "Carbon-fibre composite", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-e30",
        "band": "easier",
        "text": "Which requirement do PET and polythene both MEET, that "
                "firebrick and heat-proof glass-ceramic both FAIL?",
        "options": [
            {"text": "Stiff under load", "correct": False,
             "why": "Neither PET nor polythene meets this — both bend or "
                    "crumple under a load."},
            {"text": "Stands red heat", "correct": False,
             "why": "Neither PET nor polythene meets this — both are "
                    "polymers that soften under heat."},
            {"text": "Light", "correct": True},
            {"text": "See-through", "correct": False,
             "why": "Polythene fails this one — it comes out milky "
                    "rather than clear."},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night 3 top-up ─────────────────────────────
    {
        "id": "c9-04-s14",
        "band": "standard",
        "text": "The racing bike job needs a material that is light AND "
                "stiff at once, but the pizza-oven job's requirements do "
                "not mention “light” at all. Why not?",
        "options": [
            {"text": "An oven floor is fixed in place, so its weight is "
                     "not part of doing the job well", "correct": True},
            {"text": "No material heavy enough for an oven floor exists",
             "correct": False,
             "why": "Heavy materials are exactly what oven floors are "
                    "made from."},
            {"text": "An oven does not need to be stiff, unlike a bike",
             "correct": False,
             "why": "The oven floor does need to be stiff — it is one of "
                    "its four requirements."},
            {"text": "Heavier materials cost less than lighter ones",
             "correct": False,
             "why": "That is not a rule this lesson states."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s15",
        "band": "standard",
        "text": "Heat-proof glass-ceramic meets “stands red heat” easily, "
                "yet it still fails “does not shatter when dropped”. Why "
                "does resisting heat not also mean resisting a knock?",
        "options": [
            {"text": "The knock test was carried out while it was still "
                     "hot", "correct": False,
             "why": "The bench does not say the knock test was done hot."},
            {"text": "Standing heat and surviving a knock are different "
                     "properties", "correct": True},
            {"text": "The failure is a formality rather than a real one",
             "correct": False,
             "why": "The failure is genuine: a sharp knock on a corner "
                    "and it goes."},
            {"text": "Resisting heat and resisting a knock are one "
                     "property seen two ways", "correct": False,
             "why": "They are not one property, which is why a material "
                    "can have one and not the other."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s16",
        "band": "standard",
        "text": "Firebrick and heat-proof glass-ceramic can both stand red "
                "heat and survive daily heating and cooling, yet only "
                "glass-ceramic wins the stove-window job. Why?",
        "options": [
            {"text": "Firebrick's low price rules it out of a window job",
             "correct": False,
             "why": "Being cheap is not a disqualification anywhere in "
                    "this lesson."},
            {"text": "Firebrick has not been tested against heat",
             "correct": False,
             "why": "Firebrick meets both the heat and cycling "
                    "requirements. It is simply not transparent."},
            {"text": "The window also needs to be see-through",
             "correct": True},
            {"text": "Glass-ceramic is stiffer than firebrick",
             "correct": False,
             "why": "Both materials meet the stiffness requirement."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s17",
        "band": "standard",
        "text": "Carbon-fibre composite fails “cheap by the square metre” "
                "by a wide margin, yet it still wins the racing bike job. "
                "Why does failing one requirement not rule it out?",
        "options": [
            {"text": "The bike job ignores its own rules as an exception",
             "correct": False,
             "why": "The bike job is not treated as an exception."},
            {"text": "Expense on its own makes a material the best choice",
             "correct": False,
             "why": "Expense is not a merit by itself."},
            {"text": "The bike job has a bigger budget than the others",
             "correct": False,
             "why": "Budget is not mentioned anywhere on the bench."},
            {"text": "Cost was never one of the bike job's requirements",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s18",
        "band": "standard",
        "text": "The pizza-oven job's requirements do not include "
                "“see-through” or “holds pressurised gas in”. Why would "
                "adding those two make less sense for an oven floor?",
        "options": [
            {"text": "A requirement should describe something the job "
                     "genuinely needs", "correct": True},
            {"text": "Every job on the bench is fixed at four "
                     "requirements", "correct": False,
             "why": "The number of requirements is not fixed at four for "
                    "every job."},
            {"text": "“See-through” is not a genuine requirement anywhere "
                     "on the bench", "correct": False,
             "why": "It decides the bottle and stove jobs."},
            {"text": "Extra requirements make a job impossible for any "
                     "material to satisfy", "correct": False,
             "why": "Firebrick would still meet the original four even "
                    "with extra requirements listed."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s19",
        "band": "standard",
        "text": "PET meets “gas-tight” and “see-through”, which the bottle "
                "job needs, and it also meets “takes repeated flexing and "
                "knocks”, which the job's list does not mention. Does that "
                "extra toughness count against PET?",
        "options": [
            {"text": "It cannot be judged, since toughness is never "
                     "mentioned for this job", "correct": False,
             "why": "A requirement list is a floor to clear, not a "
                    "ceiling to match exactly."},
            {"text": "No — meeting a property beyond what a job needs "
                     "does not disqualify it", "correct": True},
            {"text": "Yes — a material must match a job's list exactly, "
                     "with nothing extra", "correct": False,
             "why": "Nothing here disqualifies a useful extra property."},
            {"text": "Yes — extra toughness makes PET too expensive",
             "correct": False,
             "why": "Toughness and cost are different properties."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s20",
        "band": "standard",
        "text": "Firebrick's low cost matters far more for the oven job "
                "than heat-proof glass-ceramic's high cost matters for the "
                "stove job. Why?",
        "options": [
            {"text": "Outdoor materials are always cheaper than indoor "
                     "ones", "correct": False,
             "why": "Nothing here is about indoors or outdoors."},
            {"text": "Stove windows are subsidised by manufacturers",
             "correct": False,
             "why": "Subsidies are not mentioned anywhere in this "
                    "lesson."},
            {"text": "An oven floor covers a much larger area than a "
                     "stove window", "correct": True},
            {"text": "An oven floor is replaced more often than a window",
             "correct": False,
             "why": "Replacement frequency is not the reason given."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s21",
        "band": "standard",
        "text": "Two of the shelf's materials both meet “stands red "
                "heat”, “stiff under load” and “cheap”. What single "
                "requirement decides the oven job in firebrick's favour "
                "over the other one?",
        "options": [
            {"text": "Light, which concrete meets and firebrick fails",
             "correct": False,
             "why": "Neither material meets “light” — both are heavy."},
            {"text": "See-through, which decides every job on the bench",
             "correct": False,
             "why": "This job does not require “see-through” at all."},
            {"text": "Survives daily heating and cooling, which concrete "
                     "fails", "correct": True},
            {"text": "Does not shatter when dropped, which firebrick "
                     "fails", "correct": False,
             "why": "The oven job does not ask for this — nobody drops "
                    "an oven floor."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s22",
        "band": "standard",
        "text": "Why can a material that is very cheap and very strong "
                "still be the wrong choice for a job?",
        "options": [
            {"text": "A job's requirements must all be met together",
             "correct": True},
            {"text": "Cheap materials are never actually strong",
             "correct": False,
             "why": "Firebrick is both cheap and strong under a steady "
                    "load."},
            {"text": "Strength is not a real property materials have",
             "correct": False,
             "why": "Strength is central to this whole lesson."},
            {"text": "Every job on the bench cares only about price in "
                     "the end", "correct": False,
             "why": "Price is only one of several possible requirements, "
                    "and some jobs list it not at all."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s23",
        "band": "standard",
        "text": "Which TWO materials on the shelf both meet “stiff under "
                "load” AND “cheap by the square metre”?",
        "options": [
            {"text": "PET and polythene", "correct": False,
             "why": "Both are cheap, and neither is stiff — both bend or "
                    "crumple easily."},
            {"text": "Firebrick and reinforced concrete", "correct": True},
            {"text": "Carbon-fibre composite and heat-proof glass-ceramic",
             "correct": False,
             "why": "Both are stiff, and neither is cheap."},
            {"text": "Firebrick and PET", "correct": False,
             "why": "PET fails “stiff under load” — a bottle crumples in "
                    "one hand."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s24",
        "band": "standard",
        "text": "PET meets more of the bench's nine requirements than any "
                "other single material. Why does it not win every job?",
        "options": [
            {"text": "PET is disqualified from winning more than one job "
                     "by a rule on the bench", "correct": False,
             "why": "No such rule is described."},
            {"text": "Meeting more requirements always matters less than "
                     "meeting fewer, harder ones", "correct": False,
             "why": "It is not about MORE or FEWER requirements met."},
            {"text": "Each job weighs a different, specific set of "
                     "requirements", "correct": True},
            {"text": "PET is too familiar as a bottle material to be "
                     "considered for anything else", "correct": False,
             "why": "Familiarity is not a reason given in this lesson."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s25",
        "band": "standard",
        "text": "Carbon-fibre composite and reinforced concrete both fail "
                "“holds pressurised gas in”. Do they fail it for the SAME "
                "reason?",
        "options": [
            {"text": "Yes — both are far too heavy for a gas container",
             "correct": False,
             "why": "Weight is not the reason given for either failure."},
            {"text": "Yes — neither can be shaped into a bottle",
             "correct": False,
             "why": "Shape is not the issue named for either material."},
            {"text": "No — carbon fibre is opaque, concrete is porous",
             "correct": False,
             "why": "Opacity is a separate failure of carbon fibre's, not "
                    "why it fails “holds gas in”."},
            {"text": "No — the fibre and resin do not seal on their own, "
                     "while concrete is porous throughout", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s26",
        "band": "standard",
        "text": "Reinforced concrete meets “does not shatter when "
                "dropped”, while firebrick and heat-proof glass-ceramic — "
                "both ceramics — do not. What is different about concrete?",
        "options": [
            {"text": "It has steel embedded in it", "correct": True},
            {"text": "It is not brittle in any way, unlike a ceramic",
             "correct": False,
             "why": "Concrete's own matrix is brittle. The steel changes "
                    "how it fails."},
            {"text": "It is much softer than firebrick or glass-ceramic",
             "correct": False,
             "why": "Softness is not what stops concrete shattering."},
            {"text": "It contains no ceramic material of any kind",
             "correct": False,
             "why": "Cement is fired from minerals much like a ceramic; "
                    "concrete is that plus steel."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s27",
        "band": "standard",
        "text": "Firebrick and heat-proof glass-ceramic both meet “stands "
                "red heat”. What do these two share that neither polymer "
                "on the shelf does?",
        "options": [
            {"text": "Both are fired from clay or minerals",
             "correct": True},
            {"text": "Both were invented more recently than the others",
             "correct": False,
             "why": "Invention date has nothing to do with heat "
                    "resistance."},
            {"text": "Both are composites reinforced with a metal",
             "correct": False,
             "why": "Neither is a composite. Both are plain ceramics."},
            {"text": "Both are the two cheapest materials on the shelf",
             "correct": False,
             "why": "Glass-ceramic is one of the most expensive materials "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s28",
        "band": "standard",
        "text": "Polythene meets “takes repeated flexing and knocks” but "
                "fails “stiff under load”. Could it still be chosen for the "
                "racing bike job, which needs both?",
        "options": [
            {"text": "Yes — meeting any one requirement is enough to be "
                     "considered", "correct": False,
             "why": "A job's requirements have to be met together."},
            {"text": "No — meeting only one of the two needed properties "
                     "is not enough", "correct": True},
            {"text": "Yes — toughness matters more than stiffness for any "
                     "bicycle frame", "correct": False,
             "why": "Both properties are needed for this job."},
            {"text": "No — only composites are ever used for a bike "
                     "frame", "correct": False,
             "why": "Family membership does not disqualify a material."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s29",
        "band": "standard",
        "text": "Carbon-fibre composite meets “stiff under load” but fails "
                "the oven job's other three requirements. Why is meeting "
                "one requirement out of four not enough to win the oven "
                "job?",
        "options": [
            {"text": "“Stiff under load” is the least important "
                     "requirement on any job", "correct": False,
             "why": "No requirement is ranked as least important."},
            {"text": "Carbon-fibre composite is banned from ovens",
             "correct": False,
             "why": "No such ban is described."},
            {"text": "A material can meet exactly one requirement per "
                     "job", "correct": False,
             "why": "Firebrick meets four requirements for the oven job "
                    "alone."},
            {"text": "A job's requirement list works as an ALL condition",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-s30",
        "band": "standard",
        "text": "Suppose firebrick costs £20 per square metre and "
                "heat-proof glass-ceramic costs eight times as much per "
                "square metre. What would 5 square metres of glass-ceramic "
                "cost?",
        "options": [
            {"text": "£100", "correct": False,
             "why": "That is five times £20, ignoring the eightfold "
                    "price difference."},
            {"text": "£160", "correct": False,
             "why": "That is the cost of only one square metre, not "
                    "five."},
            {"text": "£1,000", "correct": False,
             "why": "That comes from multiplying £20 by 50 rather than "
                    "by the correct price per square metre."},
            {"text": "£800", "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night 3 top-up ───────────────────────────────
    {
        "id": "c9-04-h14",
        "band": "harder",
        "text": "A new job needs a material that is stiff, cheap AND "
                "see-through, all at once. Is there one on the shelf?",
        "options": [
            {"text": "No — the stiff, cheap materials are opaque, and the "
                     "see-through stiff one is expensive", "correct": True},
            {"text": "Yes — PET meets all three at once", "correct": False,
             "why": "PET is cheap and clear, and fails “stiff under "
                    "load” — a bottle crumples in one hand."},
            {"text": "Yes — firebrick meets all three at once",
             "correct": False,
             "why": "Firebrick is stiff and cheap, and it is opaque."},
            {"text": "No — none of the six materials is see-through in "
                     "the way this job would need for its window",
             "correct": False,
             "why": "PET and glass-ceramic are both see-through — "
                    "neither is stiff and cheap too."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h15",
        "band": "harder",
        "text": "A new job needs a material that both “stands red heat” "
                "and “takes repeated flexing and knocks” at the same time. "
                "Can any material on the shelf do this job?",
        "options": [
            {"text": "Yes — reinforced concrete meets both", "correct": False,
             "why": "Concrete meets “stands red heat” and fails "
                    "“flexing and knocks”."},
            {"text": "No — every heat-resistant material here is "
                     "brittle, and every flexible one fails at red heat",
             "correct": True},
            {"text": "Yes — carbon-fibre composite meets both",
             "correct": False,
             "why": "Carbon fibre meets “flexing and knocks” and fails "
                    "“stands red heat” outright."},
            {"text": "No — none of the six materials meets either "
                     "requirement", "correct": False,
             "why": "Firebrick meets heat, polythene meets flexing. "
                    "Some meet one; none meets both."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h16",
        "band": "harder",
        "text": "Firebrick costs £20/m² and covers a 15 m² oven floor. "
                "Heat-proof glass-ceramic costs eight times as much per "
                "m² and would cover a 0.5 m² stove window. Which "
                "installation costs more in total, and by how much?",
        "options": [
            {"text": "The stove window costs more, by £60", "correct": False,
             "why": "The window costs £80 in total, less than the "
                    "floor's £300."},
            {"text": "They cost exactly the same amount in total",
             "correct": False,
             "why": "£300 and £80 are not equal."},
            {"text": "The oven floor costs more, by £220", "correct": True},
            {"text": "The oven floor costs more, by £300",
             "correct": False,
             "why": "£300 is the floor's own total, not the difference "
                    "between the two totals."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h17",
        "band": "harder",
        "text": "A designer proposes a foam plastic instead of carbon "
                "fibre for the racing bike frame, arguing it would be "
                "lighter still. Evaluate this against the frame's three "
                "requirements: light, stiff, flex-tough.",
        "options": [
            {"text": "It would win the job outright, since improving on "
                     "one required property settles the choice",
             "correct": False,
             "why": "All three requirements have to be met together, "
                    "not just the one being improved."},
            {"text": "It is not a real material family, so the proposal "
                     "cannot be evaluated at all", "correct": False,
             "why": "Foam is a real polymer form. The objection is about "
                    "stiffness, not existence."},
            {"text": "Anything lighter than carbon fibre must also be "
                     "stiffer", "correct": False,
             "why": "Lightness says nothing about stiffness. The two "
                    "properties are not linked that way."},
            {"text": "It would likely fail on stiffness even if it wins "
                     "on weight", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h18",
        "band": "harder",
        "text": "A pizza restaurant wants an oven floor that is ALSO "
                "see-through, so customers can watch the pizza cook from "
                "below. Is this achievable with the shelf's materials, and "
                "what would it cost?",
        "options": [
            {"text": "Achievable with glass-ceramic, at a far higher cost "
                     "than firebrick over a whole floor's area",
             "correct": True},
            {"text": "Not achievable at any price, since heat-resistance "
                     "and clarity cannot occur in one material here",
             "correct": False,
             "why": "Glass-ceramic is both heat-resistant and clear — "
                    "the problem is cost over a large area."},
            {"text": "Achievable with PET, which is both cheap and "
                     "see-through", "correct": False,
             "why": "PET fails “stands red heat” outright and would "
                    "soften before the oven reached temperature."},
            {"text": "Achievable with firebrick, since it covers oven "
                     "floors successfully already", "correct": False,
             "why": "Firebrick is opaque, whatever else it does well."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h19",
        "band": "harder",
        "text": "Explain why no material on the shelf satisfies all of: "
                "cheap, light, AND stands red heat.",
        "options": [
            {"text": "No material on the shelf manages to be both cheap "
                     "and light at the same time, whatever else it "
                     "offers", "correct": False,
             "why": "PET and polythene are both cheap and light — "
                    "neither stands red heat."},
            {"text": "The cheap, light materials on the shelf are "
                     "polymers, and none of them stands red heat",
             "correct": True},
            {"text": "No material on the shelf stands red heat",
             "correct": False,
             "why": "Firebrick and glass-ceramic both stand red heat. "
                    "Neither is light."},
            {"text": "The requirement is too vague to test clearly",
             "correct": False,
             "why": "Each requirement is tested against each material "
                    "individually and clearly on the bench."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h20",
        "band": "harder",
        "text": "A composite gas cylinder without a liner leaks gas at 40 "
                "ml per hour. Fitting a liner cuts the leak rate to a "
                "twentieth of that. What is the leak rate WITH the liner?",
        "options": [
            {"text": "20 ml per hour", "correct": False,
             "why": "That halves the rate rather than dividing by "
                    "twenty."},
            {"text": "0.2 ml per hour", "correct": False,
             "why": "That divides by two hundred rather than by "
                    "twenty."},
            {"text": "2 ml per hour", "correct": True},
            {"text": "38 ml per hour", "correct": False,
             "why": "That subtracts twenty from the rate rather than "
                    "dividing by twenty."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h21",
        "band": "harder",
        "text": "A manufacturer claims “any ceramic” would work for the "
                "stove window because “ceramics stand heat well”. Evaluate "
                "this claim using the shelf's own two ceramics.",
        "options": [
            {"text": "True — both firebrick and glass-ceramic would work "
                     "equally well as a window in a wood-burning stove",
             "correct": False,
             "why": "Firebrick is opaque and cannot serve as a window, "
                    "whatever it does for heat."},
            {"text": "False — neither ceramic stands red heat at all",
             "correct": False,
             "why": "Both ceramics genuinely meet “stands red heat”. The "
                    "flaw concerns clarity, not heat."},
            {"text": "True, but glass-ceramic is not really a ceramic",
             "correct": False,
             "why": "This lesson treats glass-ceramic as a ceramic "
                    "throughout."},
            {"text": "False — firebrick stands heat but is opaque, so "
                     "clarity varies within the ceramic family",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h22",
        "band": "harder",
        "text": "A rival firm invents a ceramic just as heat-resistant as "
                "glass-ceramic but much cheaper. Would that make it the "
                "better choice for the stove window?",
        "options": [
            {"text": "Not necessarily — it still has to meet clarity and "
                     "stiffness too, or the saving does not matter",
             "correct": True},
            {"text": "Yes — a cheaper material wins the job once it "
                     "matches an existing one on heat resistance, "
                     "regardless of anything else", "correct": False,
             "why": "Cost is one of several requirements. The others "
                    "still have to be met."},
            {"text": "No — glass-ceramic cannot be replaced, whatever the "
                     "rival's properties", "correct": False,
             "why": "A material meeting every requirement equally well "
                    "for less money would be a genuine improvement."},
            {"text": "Yes, since heat resistance is the stove window's "
                     "one and only requirement", "correct": False,
             "why": "The window's list also names clarity, stiffness "
                    "and surviving daily cycling."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h23",
        "band": "harder",
        "text": "A student claims carbon-fibre composite, which meets four "
                "requirements, must be the most generally useful material "
                "on the shelf. Evaluate this claim.",
        "options": [
            {"text": "Sound — the material meeting the most requirements "
                     "overall is the most useful one", "correct": False,
             "why": "Carbon fibre fails three of the four requirements "
                    "the oven job needs, despite its high count overall."},
            {"text": "Flawed — usefulness depends on which job is being "
                     "done, not on a raw count of boxes ticked",
             "correct": True},
            {"text": "Sound, since carbon fibre wins the racing bike job "
                     "outright", "correct": False,
             "why": "Winning one job does not establish general "
                    "usefulness across every job."},
            {"text": "Flawed, but only because reinforced concrete meets "
                     "more requirements than carbon fibre does",
             "correct": False,
             "why": "Both of them meet four of the nine. And the count "
                    "was never the real problem — usefulness depends on "
                    "the specific job."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h24",
        "band": "harder",
        "text": "Reinforced concrete is the one material on the shelf with "
                "a brittle base that still meets “does not shatter when "
                "dropped”. Would a hypothetical steel-reinforced "
                "glass-ceramic be expected to meet it too?",
        "options": [
            {"text": "No — glass-ceramic cannot be combined with steel",
             "correct": False,
             "why": "Nothing rules this combination out. The reasoning "
                    "should follow from what stops concrete shattering."},
            {"text": "No — concrete resists shattering because it is a "
                     "ceramic, and glass-ceramic already is one",
             "correct": False,
             "why": "Concrete's ceramic matrix is brittle on its own — "
                    "the resistance comes from the steel."},
            {"text": "Plausibly yes — the steel, not the ceramic base, is "
                     "what stops concrete shattering", "correct": True},
            {"text": "Yes, but glass-ceramic is already unbreakable "
                     "without any reinforcement, entirely on its own",
             "correct": False,
             "why": "Glass-ceramic is not unbreakable — it fails “does "
                    "not shatter when dropped” on its own."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h25",
        "band": "harder",
        "text": "Explain why “a composite beats a single material” is not "
                "something the bench actually shows.",
        "options": [
            {"text": "Composites generally cost more than single "
                     "materials on this shelf, which counts against "
                     "them here", "correct": False,
             "why": "Cost is not the reasoning this lesson uses to judge "
                    "a material against a job."},
            {"text": "No composite on the shelf wins a job outright",
             "correct": False,
             "why": "Carbon-fibre composite wins the racing bike job "
                    "outright."},
            {"text": "Single materials cost less than composites do, and "
                     "the cheaper material wins the job", "correct": False,
             "why": "The bike job is won by the most expensive material "
                    "on the shelf, not the cheapest — and reinforced "
                    "concrete is a cheap composite."},
            {"text": "Firebrick, a single ceramic, beats both composites "
                     "on the shelf for the oven job", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h26",
        "band": "harder",
        "text": "A hypothetical material meets the same four requirements "
                "as firebrick for the oven job, and ALSO meets “light”, "
                "unlike firebrick. Does this change the oven choice?",
        "options": [
            {"text": "No — the oven job never asks for “light”, so "
                     "meeting it changes nothing here", "correct": True},
            {"text": "Yes — meeting an extra requirement makes a "
                     "material the new winner", "correct": False,
             "why": "A job is decided by its own requirement list, not "
                    "by extra properties a rival happens to add."},
            {"text": "Yes — the oven job does care about weight, "
                     "quietly", "correct": False,
             "why": "The oven job's requirements are red-heat, "
                    "thermal-cycle, stiff and cheap — weight is not "
                    "among them."},
            {"text": "No — firebrick cannot be replaced by another "
                     "material, however it compares", "correct": False,
             "why": "A genuinely better material would not be ruled "
                    "out. The point is that THIS extra property does not "
                    "matter for THIS job."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h27",
        "band": "harder",
        "text": "Both carbon-fibre composite and reinforced concrete are "
                "“composites”, yet carbon fibre meets “light” and concrete "
                "fails it badly. Why does calling both “composites” not "
                "predict this difference?",
        "options": [
            {"text": "Concrete is not really a composite at all",
             "correct": False,
             "why": "Concrete is treated as a composite of cement and "
                    "steel throughout this lesson."},
            {"text": "Carbon-fibre composite is not really a composite "
                     "either, despite being built from two combined "
                     "materials", "correct": False,
             "why": "It is a composite of fibres and resin, exactly as "
                    "the family is defined."},
            {"text": "“Light” is a property no composite can ever have",
             "correct": False,
             "why": "Carbon-fibre composite meets “light” directly, so "
                    "the family clearly can have it."},
            {"text": "“Composite” means two materials were combined, not "
                     "which specific properties resulted", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h28",
        "band": "harder",
        "text": "A builder mistakenly orders enough glass-ceramic, at its "
                "own price of £160/m², to cover a 15 m² oven floor instead "
                "of firebrick at £20/m². How much MORE does this mistake "
                "cost than the correct material would have?",
        "options": [
            {"text": "£2,400", "correct": False,
             "why": "That is the full glass-ceramic cost, before "
                    "subtracting what firebrick would have cost."},
            {"text": "£140", "correct": False,
             "why": "That is the per-square-metre price difference, not "
                    "the total extra cost over 15 m²."},
            {"text": "£2,100", "correct": True},
            {"text": "£300", "correct": False,
             "why": "That is what firebrick alone would have cost, not "
                    "the size of the overspend."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h29",
        "band": "harder",
        "text": "A material is discovered that flexes twice as far as "
                "carbon fibre before failing. Would this make it better "
                "for the racing bike job?",
        "options": [
            {"text": "Yes — flexing further before failing is exactly "
                     "what this job's three requirements are measuring",
             "correct": False,
             "why": "The bike job also needs “stiff under load” and "
                    "“light”, not flex-tough alone."},
            {"text": "Not necessarily — extra flex can come with less "
                     "stiffness, which the job needs just as much",
             "correct": True},
            {"text": "No — carbon fibre cannot be beaten on any "
                     "property by another material", "correct": False,
             "why": "A genuine improvement is not ruled out. The "
                    "question is whether it improves on all three "
                    "requirements, not just one."},
            {"text": "Yes, because a material that flexes further before "
                     "failing always ends up being lighter too",
             "correct": False,
             "why": "Flexing distance and weight are different "
                    "properties. One does not guarantee the other."},
        ],
        "figure": None,
    },
    {
        "id": "c9-04-h30",
        "band": "harder",
        "text": "A manufacturer tries embedding continuous glass fibres, "
                "instead of carbon fibres, in the same resin used for the "
                "bike frame. Based on what fibres and resin each "
                "contribute, what would you expect to change, and what "
                "would stay the same?",
        "options": [
            {"text": "Everything stays the same, since any fibre in any "
                     "resin behaves identically", "correct": False,
             "why": "Different fibres have different properties — that "
                    "is why carbon and glass fibre give a different "
                    "result."},
            {"text": "The result would no longer count as a composite",
             "correct": False,
             "why": "Two materials combined so the result does what "
                    "neither can alone is still a composite, whichever "
                    "fibre is used."},
            {"text": "The resin would switch to taking the pull instead "
                     "of the fibres", "correct": False,
             "why": "Fibres for pull, resin for holding and spreading — "
                    "that division defines this kind of composite "
                    "regardless of fibre."},
            {"text": "Cost would likely fall, while the fibres still "
                     "take the pull and the resin still holds and "
                     "spreads the load", "correct": True},
        ],
        "figure": None,
    },
]
