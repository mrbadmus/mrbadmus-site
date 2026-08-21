"""C9 lesson 02 — Predicting displacement: twelve questions (MRB-281).

The lesson's argument is one shape: higher displaces lower, lower never
displaces higher, and there is no third column. The page teaches it with eight
proposals, each committed to before it runs, and a sort at the end in which the
rule is the only thing left standing.

These twelve probe the angles the mastery ladder leaves alone: telling slow
from impossible, reading the same event from two directions, and what carbon is
doing in a set of metal reactions.

The distractors are built from the lesson's declared misconceptions.

`MATL-05` (any metal will displace any other if left long enough) drives the
wrong options in e03, s01, s04 and h01. Each treats an impossible reaction as a
slow one. s04 is the one that matters: it offers a real slow reaction — zinc in
iron sulfate — beside a real impossible one, so the belief has to tell them
apart and cannot.

`MATL-06` (a less reactive metal can push a more reactive one out) drives e02,
s02 and h03, where the rule is run backwards.

A third strand, in neither register entry, is that a displacement is ONE event
seen twice: the solution fading and the coating growing are not two things.
e04 and h02 are built on it.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS.
"""

UNIT = "C9"
LESSON = "predicting-displacement"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c9-02-e01",
        "band": "easier",
        "text": "What happens in a displacement reaction?",
        "options": [
            {"text": "A more reactive metal takes the place of a less "
                     "reactive one in its compound",
             "correct": True},
            {"text": "Two compounds swap their metals over so that both are "
                     "changed",
             "correct": False,
             "why": "One element is displaced from one compound. It is not a "
                    "trade between two compounds."},
            {"text": "A compound falls apart into the elements it was made "
                     "from",
             "correct": False,
             "why": "That is thermal decomposition, and no second metal is "
                    "involved."},
            {"text": "A metal joins with oxygen to make an oxide layer",
             "correct": False,
             "why": "That is oxidation. Nothing is being pushed out of a "
                    "compound."},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e02",
        "band": "easier",
        "text": "A silver wire is left in copper sulfate solution and nothing "
                "happens. Why?",
        "options": [
            {"text": "Silver is above copper, so it is too reactive to react "
                     "here",
             "correct": False,
             "why": "It is the other way round: silver is BELOW copper, which "
                    "is why it cannot displace it."},
            {"text": "Silver is below copper in the series, so it cannot "
                     "displace it",
             "correct": True},
            {"text": "Copper sulfate does not dissolve well enough to react",
             "correct": False,
             "why": "It dissolves readily — the blue colour is the dissolved "
                    "compound."},
            {"text": "Silver only reacts with acids and never with salts",
             "correct": False,
             "why": "Silver reacts with very little of anything. Its position "
                    "is the reason."},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e03",
        "band": "easier",
        "text": "A copper strip is left in magnesium sulfate solution for a "
                "week and nothing changes. What should you conclude?",
        "options": [
            {"text": "It needs longer — a week is not enough for a slow "
                     "reaction",
             "correct": False,
             "why": "Time cannot start a reaction the series rules out. A "
                    "year would look the same."},
            {"text": "The solution was too dilute for anything to be visible",
             "correct": False,
             "why": "Concentration changes the speed of a possible reaction, "
                    "not whether it is possible."},
            {"text": "The reaction cannot happen, because copper is below "
                     "magnesium",
             "correct": True},
            {"text": "The copper needs to be heated before it will react",
             "correct": False,
             "why": "Heat speeds up a possible reaction. It cannot make an "
                    "impossible one possible."},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e04",
        "band": "easier",
        "text": "An iron nail in copper sulfate goes brown while the blue of "
                "the solution fades. How many things are happening?",
        "options": [
            {"text": "Two — the nail rusts, and separately the solution "
                     "fades",
             "correct": False,
             "why": "The brown is copper, not rust, and it came out of the "
                    "solution that faded."},
            {"text": "Three — the nail changes, the solution changes and heat "
                     "is given off",
             "correct": False,
             "why": "Warming is part of the same event, not a third one."},
            {"text": "None — both are physical changes with no reaction at "
                     "all",
             "correct": False,
             "why": "A new substance appears on the nail. That is a chemical "
                    "change."},
            {"text": "One — the copper leaving the solution IS the copper "
                     "arriving on the nail",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c9-02-s01",
        "band": "standard",
        "text": "What is the difference between a reaction that is slow and "
                "one that is impossible?",
        "options": [
            {"text": "A slow one is going and will finish; an impossible one "
                     "is not going at all",
             "correct": True},
            {"text": "A slow one takes hours and an impossible one takes "
                     "years",
             "correct": False,
             "why": "An impossible one takes no length of time, because it "
                    "never starts."},
            {"text": "A slow one needs heating and an impossible one needs "
                     "electricity",
             "correct": False,
             "why": "Neither is about what is supplied. It is about whether "
                    "the series permits it."},
            {"text": "There is no real difference — everything reacts "
                     "eventually",
             "correct": False,
             "why": "Copper in magnesium sulfate never reacts. That is the "
                    "whole point of the lesson."},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s02",
        "band": "standard",
        "text": "Zinc is added to copper sulfate and copper is added to zinc "
                "sulfate. What happens in each?",
        "options": [
            {"text": "Both react, because the two metals are close together "
                     "in the series",
             "correct": False,
             "why": "Closeness affects speed, never direction. Only one of "
                    "the pair can work."},
            {"text": "The first reacts and the second does not, because zinc "
                     "is above copper",
             "correct": True},
            {"text": "Neither reacts, because both are metals of a similar "
                     "kind",
             "correct": False,
             "why": "Zinc in copper sulfate is one of the most reliable "
                    "displacements there is."},
            {"text": "The second reacts and the first does not, because "
                     "copper is the heavier",
             "correct": False,
             "why": "Mass has no part in it, and the direction is the other "
                    "way round."},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s03",
        "band": "standard",
        "text": "Carbon is heated with copper oxide and copper appears. Why "
                "is this called a displacement?",
        "options": [
            {"text": "Because carbon is a non-metal and non-metals always "
                     "take oxygen",
             "correct": False,
             "why": "Sulfur is a non-metal and does no such thing. It is "
                    "carbon's POSITION that matters."},
            {"text": "Because heating any oxide releases the metal inside it",
             "correct": False,
             "why": "Aluminium oxide heated with carbon gives nothing at all."},
            {"text": "Because carbon is above copper in the series and takes "
                     "its place",
             "correct": True},
            {"text": "Because the copper oxide melts and the copper runs out "
                     "of it",
             "correct": False,
             "why": "Melting separates nothing. A reaction is what frees the "
                    "copper."},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s04",
        "band": "standard",
        "text": "Zinc in iron sulfate changes very slowly. Copper in zinc "
                "sulfate does not change at all. How would you tell those two "
                "cases apart?",
        "options": [
            {"text": "Warm both — the one that is going will speed up and the "
                     "other will not",
             "correct": False,
             "why": "A reasonable practical move, and the series tells you "
                    "the answer without heating anything."},
            {"text": "Leave both for a month and see which one eventually "
                     "changes",
             "correct": False,
             "why": "It would work and it is the slow way of asking a "
                    "question already answered."},
            {"text": "Weigh both before and after, because only a reaction "
                     "changes mass",
             "correct": False,
             "why": "A displacement does not change the total mass. Nothing "
                    "leaves the tube."},
            {"text": "Compare the two positions in the series — zinc is above "
                     "iron, copper is below zinc",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c9-02-h01",
        "band": "harder",
        "text": "Why is “no reaction” a prediction rather than an "
                "absence of one?",
        "options": [
            {"text": "Because the series says it cannot happen, which is a "
                     "claim that could be wrong",
             "correct": True},
            {"text": "Because every experiment produces a result of some kind",
             "correct": False,
             "why": "True and trivial. The point is that this particular "
                    "result was SPECIFIED in advance."},
            {"text": "Because the student still has to write something in the "
                     "table",
             "correct": False,
             "why": "What gets written down is not what makes it a "
                    "prediction."},
            {"text": "Because a reaction might still be happening too slowly "
                     "to see",
             "correct": False,
             "why": "That is exactly what the lesson denies. The prediction "
                    "is that nothing is happening."},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h02",
        "band": "harder",
        "text": "A displacement is run in a sealed tube and the total mass is "
                "measured before and after. What happens to it?",
        "options": [
            {"text": "It rises, because a new solid has been created on the "
                     "metal",
             "correct": False,
             "why": "The solid came out of the solution. Nothing was "
                    "created."},
            {"text": "It stays the same, because the atoms have only "
                     "rearranged",
             "correct": True},
            {"text": "It falls, because the metal that dissolved has "
                     "disappeared",
             "correct": False,
             "why": "Dissolved is not gone. It is still in the tube and still "
                    "on the balance."},
            {"text": "It cannot be predicted without knowing which metals are "
                     "used",
             "correct": False,
             "why": "Conservation of mass holds for every displacement, "
                    "whichever pair it is."},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h03",
        "band": "harder",
        "text": "Zinc blocks are bolted to a steel ship's hull and replaced "
                "every few years. What are they for?",
        "options": [
            {"text": "They add weight low down and help keep the ship upright",
             "correct": False,
             "why": "Ballast is a real thing and is not what a small bolted "
                    "block of zinc is doing."},
            {"text": "They seal small holes in the steel as the zinc slowly "
                     "spreads",
             "correct": False,
             "why": "Zinc does not spread, and the blocks are on the outside "
                    "of an unholed hull."},
            {"text": "Zinc is above iron in the series, so the zinc reacts "
                     "instead of the hull",
             "correct": True},
            {"text": "Zinc is below iron, so it does not react and protects "
                     "the steel by covering it",
             "correct": False,
             "why": "It is above iron, and it works by BEING used up rather "
                    "than by surviving."},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h04",
        "band": "harder",
        "text": "A student proposes ordering four metals by dropping each "
                "into the other three's sulfate solutions. How many of the "
                "twelve tubes would be expected to react?",
        "options": [
            {"text": "All twelve, because every pair of different metals "
                     "reacts somehow",
             "correct": False,
             "why": "Half of every pair runs the wrong way and does nothing "
                    "at all."},
            {"text": "None, because a metal cannot displace another metal "
                     "from a sulfate",
             "correct": False,
             "why": "That is precisely what a displacement is, and six of "
                    "them work."},
            {"text": "Four, one for each metal, because each metal reacts "
                     "once",
             "correct": False,
             "why": "The most reactive metal displaces all three of the "
                    "others, not one."},
            {"text": "Six — every pair works one way round and not the other",
             "correct": True},
        ],
        "figure": None,
    },
]
