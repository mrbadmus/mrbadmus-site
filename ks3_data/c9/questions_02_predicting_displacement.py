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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c9-02-e05",
        "band": "easier",
        "text": "In copper sulfate solution, what is the sulfate part doing "
                "during a displacement?",
        "options": [
            {"text": "Reacting with the metal that is added, which is what "
                     "releases the copper and lets it settle out onto the "
                     "surface of the solid",
             "correct": False,
             "why": "The sulfate takes no part. What changes is which metal "
                    "it is joined to"},
            {"text": "Staying put while the metals swap around it",
             "correct": True},
            {"text": "Being given off as a gas",
             "correct": False,
             "why": "No gas is produced in a displacement between two metals"},
            {"text": "Turning into a different compound while the metals swap",
             "correct": False,
             "why": "It ends up joined to a different metal and is the same "
                    "sulfate throughout"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e06",
        "band": "easier",
        "text": "Magnesium is added to zinc sulfate solution. What happens?",
        "options": [
            {"text": "Nothing, because magnesium and zinc are both metals and "
                     "two metals of the same kind cannot take each other's "
                     "place in a compound",
             "correct": False,
             "why": "Two DIFFERENT metals is exactly the case displacement "
                    "covers. Magnesium is above zinc"},
            {"text": "The zinc displaces the magnesium, which then settles out "
                     "as a grey solid",
             "correct": False,
             "why": "Zinc is below magnesium, so it cannot take its place"},
            {"text": "The magnesium displaces the zinc, which appears as a "
                     "solid",
             "correct": True},
            {"text": "A gas is given off",
             "correct": False,
             "why": "A metal and another metal's salt give a solid and a "
                    "solution, not a gas"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e07",
        "band": "easier",
        "text": "The lesson calls IMPOSSIBLE the most useful word on the "
                "page. What does it mean here?",
        "options": [
            {"text": "The reaction is so slow that no experiment a school "
                     "could run would ever be left going for long enough to "
                     "detect it",
             "correct": False,
             "why": "That would be SLOW. Impossible means there is nothing "
                    "going on to detect"},
            {"text": "The reaction needs equipment that no ordinary school "
                     "laboratory is likely to have",
             "correct": False,
             "why": "No equipment would help. The series rules the reaction "
                    "out entirely"},
            {"text": "Nobody has managed it yet",
             "correct": False,
             "why": "It is not an open question. The order says it cannot "
                    "happen"},
            {"text": "The reaction does not happen at any speed, so waiting "
                     "changes nothing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e08",
        "band": "easier",
        "text": "Which of these pairs would give NO reaction?",
        "options": [
            {"text": "Silver added to zinc sulfate solution",
             "correct": True},
            {"text": "Zinc added to copper sulfate solution",
             "correct": False,
             "why": "Zinc is above copper, so it displaces it readily"},
            {"text": "Copper added to silver nitrate solution",
             "correct": False,
             "why": "Copper is above silver, so grey needles of silver grow "
                    "on the wire"},
            {"text": "Magnesium added to iron sulfate solution",
             "correct": False,
             "why": "Magnesium is well above iron and displaces it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e09",
        "band": "easier",
        "text": "What is a compound, in the sense this lesson uses it?",
        "options": [
            {"text": "Two or more elements in the same container, mixed "
                     "thoroughly enough that no part of the mixture can be "
                     "told apart from any other part of it",
             "correct": False,
             "why": "That is a mixture. Nothing in it is joined"},
            {"text": "Two or more elements chemically joined, so neither "
                     "behaves as it did on its own",
             "correct": True},
            {"text": "A metal that has been stirred into water until none of "
                     "the solid can be seen any more at all",
             "correct": False,
             "why": "Dissolving spreads something out. A compound is atoms "
                    "joined"},
            {"text": "Any blue solution",
             "correct": False,
             "why": "The blue is a clue that copper is present, and colour is "
                    "not what makes something a compound"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e10",
        "band": "easier",
        "text": "What is a prediction, in this lesson?",
        "options": [
            {"text": "Saying what happened after you have watched it, in "
                     "words that anybody reading your notes afterwards can "
                     "check against the tube",
             "correct": False,
             "why": "That is a record of an observation. A prediction comes "
                    "FIRST"},
            {"text": "Guessing which tube will react, without using any of the "
                     "evidence you have been given",
             "correct": False,
             "why": "A guess uses nothing. A prediction uses the series"},
            {"text": "Saying what will happen before it happens, from "
                     "something you already know",
             "correct": True},
            {"text": "The result the teacher expects",
             "correct": False,
             "why": "Who expects it is not the point. It is worked out from "
                    "the order"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e11",
        "band": "easier",
        "text": "An iron nail in copper sulfate comes out brown. Where did "
                "the brown coating come from?",
        "options": [
            {"text": "Out of the nail, where the iron has changed into copper",
             "correct": False,
             "why": "No atom changes kind in a chemical reaction. The iron is "
                    "still iron"},
            {"text": "Out of the air",
             "correct": False,
             "why": "There is no copper in air. The blue fading is the "
                    "copper leaving the liquid"},
            {"text": "It is rust",
             "correct": False,
             "why": "Rust is orange-brown iron oxide and needs air and water. "
                    "This coating is copper"},
            {"text": "Out of the solution, where the copper was dissolved",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e12",
        "band": "easier",
        "text": "Iron filings are added to lead nitrate solution. Which metal "
                "ends up as a solid?",
        "options": [
            {"text": "Lead",
             "correct": True},
            {"text": "Iron, because the iron was a solid when it went in and "
                     "a displacement swaps the partners around it without "
                     "changing what state it is in",
             "correct": False,
             "why": "The iron dissolves as it displaces. The metal that comes "
                    "OUT is the less reactive one"},
            {"text": "Both, in two layers",
             "correct": False,
             "why": "The iron goes into solution as the lead comes out. Only "
                    "one of them ends up solid"},
            {"text": "Neither — no reaction happens",
             "correct": False,
             "why": "Iron is above lead in the series, so the reaction runs"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e13",
        "band": "easier",
        "text": "Which way round does a displacement run?",
        "options": [
            {"text": "Whichever metal is present in the larger amount takes "
                     "the place of the other, which is why the concentration "
                     "of the solution decides the outcome",
             "correct": False,
             "why": "Amount changes how much product, never which way the "
                    "reaction goes"},
            {"text": "Higher displaces lower, and never the other way round",
             "correct": True},
            {"text": "Lower displaces higher, so the weaker metal takes the "
                     "other's place",
             "correct": False,
             "why": "Exactly backwards, and it is the misconception the "
                    "half-empty grid exists to kill"},
            {"text": "Either way, given time",
             "correct": False,
             "why": "One direction is impossible rather than slow. Time "
                    "changes nothing"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c9-02-s05",
        "band": "standard",
        "text": "Copper wire in silver nitrate grows grey needles and the "
                "solution turns faintly blue. What are the two observations "
                "telling you?",
        "options": [
            {"text": "Silver is coming out of the solution and the blue is "
                     "silver nitrate becoming more concentrated as the water "
                     "around it is used up by the reaction",
             "correct": False,
             "why": "Silver nitrate is colourless. The blue is dissolved "
                    "copper, which was not there before"},
            {"text": "Silver is coming out of the solution and copper is "
                     "going into it",
             "correct": True},
            {"text": "The copper is coming out of the wire and the silver is "
                     "going into the solution",
             "correct": False,
             "why": "The needles are silver, and copper is above silver so it "
                    "is the one that dissolves"},
            {"text": "The wire is corroding in the nitrate",
             "correct": False,
             "why": "It is displacing rather than corroding, and something is "
                    "being deposited on it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s06",
        "band": "standard",
        "text": "A magnesium strip in copper sulfate is over in seconds; a "
                "zinc strip in iron sulfate takes days. Both are possible. What "
                "sets the difference?",
        "options": [
            {"text": "Whether the solution is a sulfate, since some "
                     "compounds give up their metal far more readily than "
                     "others do whatever metals are involved",
             "correct": False,
             "why": "Both are sulfates here, which is exactly why they are "
                    "comparable"},
            {"text": "How much solution is in the tube",
             "correct": False,
             "why": "Volume changes how much product. It does not make one "
                    "reaction seconds and the other days"},
            {"text": "How far apart the two metals are in the series",
             "correct": True},
            {"text": "Nothing — one of them must be impossible",
             "correct": False,
             "why": "Both are possible. Zinc is above iron, so the slow one "
                    "is genuinely running"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s07",
        "band": "standard",
        "text": "A student predicts NO reaction for a tube, and after an hour "
                "nothing has happened. Has the prediction been confirmed?",
        "options": [
            {"text": "No — nothing happening is not a result, so an hour of "
                     "watching an unchanged tube has told nobody anything at "
                     "all about the prediction",
             "correct": False,
             "why": "A predicted absence that turns out to be absent is a "
                    "successful test. The tube could have reacted"},
            {"text": "Yes, and no further evidence could ever be needed to "
                     "settle the question once and for all",
             "correct": False,
             "why": "Surviving one test is not proof for ever. It is "
                    "supporting evidence"},
            {"text": "No, because you cannot prove a negative",
             "correct": False,
             "why": "You can test one. The prediction said the tube would not "
                    "change, and it did not"},
            {"text": "It has survived a test it could have failed, which is "
                     "what confirming means",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s08",
        "band": "standard",
        "text": "A student heats a tube of copper in zinc sulfate solution to "
                "get the reaction going. What happens?",
        "options": [
            {"text": "Still nothing, because copper is below zinc and the "
                     "reaction is impossible rather than slow",
             "correct": True},
            {"text": "The reaction begins, because heating supplies the "
                     "energy that a reaction between two metals this close "
                     "together in the series needs before it can start",
             "correct": False,
             "why": "They are not close, and heating cannot start a reaction "
                    "the order rules out"},
            {"text": "The zinc sulfate decomposes instead, breaking apart into "
                     "simpler substances as soon as the tube is warmed",
             "correct": False,
             "why": "Nothing decomposes at the temperature of a warmed test "
                    "tube"},
            {"text": "The copper dissolves",
             "correct": False,
             "why": "Copper does not dissolve in zinc sulfate at any "
                    "temperature"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s09",
        "band": "standard",
        "text": "Which observation would show a displacement had happened, in "
                "a case where both solutions are colourless?",
        "options": [
            {"text": "The solution becoming warmer, since a displacement "
                     "gives out energy and a temperature rise is therefore "
                     "proof that one has taken place",
             "correct": False,
             "why": "A rise is good evidence and not proof on its own — "
                    "dissolving warms some solutions too. The deposit is "
                    "decisive"},
            {"text": "A solid appearing on the metal that was added",
             "correct": True},
            {"text": "Bubbles rising through the liquid from the metal that "
                     "was added",
             "correct": False,
             "why": "Bubbles would suggest a metal reacting with acid rather "
                    "than a displacement"},
            {"text": "The metal getting smaller",
             "correct": False,
             "why": "It does, and slowly enough to be hard to see. The "
                    "deposit shows first"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s10",
        "band": "standard",
        "text": "Zinc is added to a solution and a dark deposit forms. What "
                "can you say about the metal that was dissolved in it?",
        "options": [
            {"text": "It is above zinc in the series, because a metal has to "
                     "be more reactive than the one added before it will come "
                     "out of solution as a solid",
             "correct": False,
             "why": "Exactly backwards. The metal that comes OUT is the less "
                    "reactive one"},
            {"text": "It is copper",
             "correct": False,
             "why": "It might be. Several metals below zinc would give a dark "
                    "deposit"},
            {"text": "It is below zinc in the reactivity series",
             "correct": True},
            {"text": "Nothing can be said without knowing the colour",
             "correct": False,
             "why": "A deposit forming at all places it below zinc, whatever "
                    "colour it is"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s11",
        "band": "standard",
        "text": "Four metals are each tested against the other three's "
                "sulfates. Why is HALF the grid blank?",
        "options": [
            {"text": "Because half of the tubes pair a metal with its own "
                     "sulfate, and a metal cannot displace itself from a "
                     "compound it is already part of",
             "correct": False,
             "why": "Only four of the sixteen do that. The half-empty shape "
                    "comes from the order running one way"},
            {"text": "Because half of the solutions were made up far too "
                     "dilute to react at all",
             "correct": False,
             "why": "All were made the same way. Concentration is not what "
                    "makes the pattern"},
            {"text": "Because half of them were not run",
             "correct": False,
             "why": "Every tube was run, and the blanks are results"},
            {"text": "Because every pair works one way round and not the "
                     "other",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s12",
        "band": "standard",
        "text": "Why does the copper leaving the solution and the copper "
                "arriving on the nail count as ONE event rather than two?",
        "options": [
            {"text": "Because it is the same copper — it has moved from being "
                     "dissolved to being a solid on the nail",
             "correct": True},
            {"text": "Because the two happen at the same time, in the same "
                     "tube",
             "correct": False,
             "why": "Simultaneity is not the reason. It is one event because "
                    "it is one lot of copper"},
            {"text": "Because the blue fading is only an appearance",
             "correct": False,
             "why": "The fading is real and measurable. It is the same copper "
                    "as the coating"},
            {"text": "Because the nail is not really changing",
             "correct": False,
             "why": "The nail changes a great deal — it is being coated and "
                    "some iron is dissolving"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s13",
        "band": "standard",
        "text": "Which of these would a displacement prediction NEVER depend "
                "on?",
        "options": [
            {"text": "The two metals' positions in the series",
             "correct": False,
             "why": "That is the only thing it does depend on"},
            {"text": "How much of the solution is in the tube",
             "correct": True},
            {"text": "Which metal is in the solution and which is the solid",
             "correct": False,
             "why": "It matters a great deal. The same pair reacts one way "
                    "round and not the other"},
            {"text": "Whether the metal added is above the one dissolved",
             "correct": False,
             "why": "That is the prediction, put in other words"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c9-02-h05",
        "band": "harder",
        "text": "Aluminium powder and iron oxide react hot enough to weld "
                "railway track. Which fact about the series is doing the "
                "work?",
        "options": [
            {"text": "Aluminium melts at a far lower temperature than iron, "
                     "so it liquefies first and carries the heat through the "
                     "mixture to where the weld is needed",
             "correct": False,
             "why": "Melting points are not what drives it. The reaction "
                    "happens because aluminium wants the oxygen more"},
            {"text": "Aluminium is above iron, so it takes the oxygen and "
                     "leaves the iron as the element",
             "correct": True},
            {"text": "Iron is above aluminium, so the iron takes the oxygen "
                     "and leaves the aluminium as the element",
             "correct": False,
             "why": "The wrong way round, and it would leave aluminium as the "
                    "product rather than iron"},
            {"text": "Powdered metals always react violently",
             "correct": False,
             "why": "Powdered copper with iron oxide does nothing at all. The "
                    "positions decide it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h06",
        "band": "harder",
        "text": "An unknown metal M displaces copper from copper sulfate, and "
                "zinc displaces M from M sulfate. Where is M?",
        "options": [
            {"text": "Above zinc and above copper, because a metal that can "
                     "displace one of them has shown itself to be more "
                     "reactive than the others in the group",
             "correct": False,
             "why": "Zinc displaced M, which puts M below zinc. Only the "
                    "copper result went M's way"},
            {"text": "Below copper",
             "correct": False,
             "why": "Then it could not have displaced copper at all"},
            {"text": "Below zinc and above copper",
             "correct": True},
            {"text": "It cannot be placed from two results",
             "correct": False,
             "why": "One win and one loss brackets it exactly, which is how "
                    "the whole series was built"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h07",
        "band": "harder",
        "text": "A displacement is run in a sealed tube. The solid gets "
                "heavier and the solution lighter. Does that break "
                "conservation of mass?",
        "options": [
            {"text": "No, because the extra mass on the solid was created by "
                     "the reaction and the loss from the solution was "
                     "destroyed by it, and the two happen to match",
             "correct": False,
             "why": "Nothing is created or destroyed. The same atoms have "
                    "changed place"},
            {"text": "Yes, because two masses changed",
             "correct": False,
             "why": "Two PARTS changed and the total did not. That is what "
                    "conservation means"},
            {"text": "It cannot be told without also weighing the gas that "
                     "comes off during the reaction",
             "correct": False,
             "why": "No gas is produced in a displacement between two "
                    "metals"},
            {"text": "No — the total is unchanged, and only where the metal "
                     "sits has moved",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h08",
        "band": "harder",
        "text": "Why is a metal BELOW iron no use as a sacrificial block on a "
                "steel hull?",
        "options": [
            {"text": "Because it would not react in preference to the iron, "
                     "so the hull would corrode as before",
             "correct": True},
            {"text": "Because it would be eaten away far too quickly to be "
                     "worth bolting on, and the ship would have to be brought "
                     "into dock every few months to have it replaced",
             "correct": False,
             "why": "A metal below iron is eaten away more slowly, not "
                    "faster — which is exactly the problem"},
            {"text": "Because it would react with the seawater rather than "
                     "with the hull, and would be used up in doing so",
             "correct": False,
             "why": "That is what a metal ABOVE iron does, and it is the "
                    "whole point of the block"},
            {"text": "Because it would be too expensive",
             "correct": False,
             "why": "Cost matters and is not the objection. Such a block "
                    "simply would not work"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h09",
        "band": "harder",
        "text": "A student says the series predicts eight reactions out of "
                "eight, so it must be right. What is the careful version of "
                "that?",
        "options": [
            {"text": "Eight out of eight proves it, since nothing has ever "
                     "counted against it",
             "correct": False,
             "why": "No number of successes proves a general rule. It is well "
                    "supported rather than proved"},
            {"text": "Eight successful predictions are strong support, and "
                     "the ninth could still fail",
             "correct": True},
            {"text": "Eight results are too few to say anything",
             "correct": False,
             "why": "Eight predictions that could each have failed are "
                    "substantial evidence"},
            {"text": "The predictions were not really tested, because the "
                     "series was used to make them",
             "correct": False,
             "why": "The series made them and the TUBES tested them. That is "
                    "how a prediction works"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h10",
        "band": "harder",
        "text": "Why does the same order predict displacement, the water "
                "test, the acid test AND extraction with carbon?",
        "options": [
            {"text": "Because chemists arranged the order so that it would "
                     "fit all four, adjusting it whenever a new kind of "
                     "reaction was investigated",
             "correct": False,
             "why": "The order came from water and acid. That it then fitted "
                    "the others is a finding rather than an adjustment"},
            {"text": "Because all four of them are really the same reaction "
                     "underneath it all",
             "correct": False,
             "why": "They have different reactants and different products. "
                    "What they share is what drives them"},
            {"text": "Because all four depend on the same property of the "
                     "element",
             "correct": True},
            {"text": "It is a coincidence",
             "correct": False,
             "why": "Four independent kinds of evidence agreeing is what a "
                    "real property looks like"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h11",
        "band": "harder",
        "text": "A student leaves copper in magnesium sulfate for a month "
                "because “everything reacts eventually”. What is the "
                "strongest thing to say?",
        "options": [
            {"text": "That a month is not long enough, and that the tube "
                     "would have to be left for a year or more before any "
                     "conclusion could safely be drawn from it",
             "correct": False,
             "why": "That accepts the student's assumption. The reaction is "
                    "impossible rather than slow"},
            {"text": "That the tube should have been warmed",
             "correct": False,
             "why": "Warming speeds up a possible reaction. It cannot start "
                    "an impossible one"},
            {"text": "That the copper and the magnesium sulfate never come "
                     "into proper contact anywhere inside the tube",
             "correct": False,
             "why": "They are in contact throughout. Contact is not what is "
                    "missing"},
            {"text": "That the series rules this reaction out, so a month "
                     "gives exactly what an hour gave",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h12",
        "band": "harder",
        "text": "Carbon is placed in a series of METALS. Which piece of "
                "evidence puts it where it is?",
        "options": [
            {"text": "Which metal oxides it can and cannot take the oxygen "
                     "from",
             "correct": True},
            {"text": "How vigorously it reacts with cold water and with "
                     "dilute acid, tested in exactly the same way as each of "
                     "the metals on the bench was",
             "correct": False,
             "why": "Carbon does neither, which is why a different kind of "
                    "evidence had to be used"},
            {"text": "How hard it is",
             "correct": False,
             "why": "Diamond is the hardest substance known and graphite "
                    "rubs off on paper. Hardness places nothing"},
            {"text": "Its position on the periodic table",
             "correct": False,
             "why": "The reactivity series cuts across the table. Position "
                    "there does not fix position here"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h13",
        "band": "harder",
        "text": "A tube shows no change after an hour. What would have to be "
                "true for that to be a FAILED prediction rather than a "
                "successful one?",
        "options": [
            {"text": "The tube would have to have been set up wrongly, since "
                     "a prediction can only fail if the experiment testing it "
                     "was carried out properly in the first place",
             "correct": False,
             "why": "A badly set-up tube tests nothing either way. The "
                    "question is what the series said"},
            {"text": "The series would have to have said a reaction should "
                     "happen there",
             "correct": True},
            {"text": "The metals would have to be close together in the "
                     "series",
             "correct": False,
             "why": "Closeness makes a reaction slow. It does not decide "
                    "whether a prediction failed"},
            {"text": "Nothing — no reaction always means a failure",
             "correct": False,
             "why": "When the series predicts no reaction, no reaction is the "
                    "prediction coming true"},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · easier e14–e30 ─────────────────────────────────
    {
        "id": "c9-02-e14",
        "band": "easier",
        "text": "Magnesium ribbon is stood in copper sulfate solution. "
                "Complete the word equation: magnesium + copper sulfate →",
        "options": [
            {"text": "copper sulfate + magnesium", "correct": False,
             "why": "Those are the two starting substances written out again"},
            {"text": "magnesium copper + sulfate", "correct": False,
             "why": "The sulfate stays joined to a metal; it does not come "
                    "away on its own"},
            {"text": "magnesium sulfate + copper", "correct": True},
            {"text": "magnesium oxide + copper sulfide", "correct": False,
             "why": "There is no free oxygen or sulfur here — the sulfate "
                    "moves across as one whole part"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e15",
        "band": "easier",
        "text": "What has to be true of the metal being added for a "
                "displacement to happen?",
        "options": [
            {"text": "It must be below the metal in the compound",
             "correct": False,
             "why": "That is the direction that does not run; a lower metal "
                    "has nothing to offer"},
            {"text": "It must be above the metal in the compound",
             "correct": True},
            {"text": "It must be a different colour from it", "correct": False,
             "why": "Colour plays no part in the prediction"},
            {"text": "It must be heavier than it", "correct": False,
             "why": "Density plays no part in the prediction"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e16",
        "band": "easier",
        "text": "Zinc granules are dropped into blue copper sulfate solution. "
                "What happens to the colour of the solution?",
        "options": [
            {"text": "The blue fades", "correct": True},
            {"text": "It turns bright red", "correct": False,
             "why": "The copper appears as a brown-pink solid on the zinc, "
                    "not as a colour in the liquid"},
            {"text": "It turns a deeper blue", "correct": False,
             "why": "Copper is leaving the solution, so the blue gets weaker "
                    "rather than stronger"},
            {"text": "It stays exactly as blue", "correct": False,
             "why": "Zinc is above copper, so the copper comes out and the "
                    "blue drains away"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e17",
        "band": "easier",
        "text": "A coil of clean copper wire is left standing in silver "
                "nitrate solution. What grows on the wire?",
        "options": [
            {"text": "Nothing at all", "correct": False,
             "why": "Copper is above silver, so this is a pair that reacts"},
            {"text": "Brown-pink specks of copper", "correct": False,
             "why": "The copper is the metal going into the solution. The "
                    "silver is what comes out"},
            {"text": "A blue crust of copper sulfate", "correct": False,
             "why": "There is no sulfate here, and the copper dissolves "
                    "rather than coating the wire"},
            {"text": "Grey needles of silver", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e18",
        "band": "easier",
        "text": "In a displacement reaction, what does DISPLACED mean?",
        "options": [
            {"text": "Dissolved into the solution as a compound",
             "correct": False,
             "why": "That is what happens to the more reactive metal, not to "
                    "the one displaced"},
            {"text": "Heated until it melts and runs out", "correct": False,
             "why": "No melting is involved. The metal is released by a "
                    "chemical change"},
            {"text": "Pushed out of its compound, as the element",
             "correct": True},
            {"text": "Broken into smaller pieces", "correct": False,
             "why": "Breaking a solid up is a physical change and makes no "
                    "new substance"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e19",
        "band": "easier",
        "text": "Iron filings are tipped into colourless zinc sulfate "
                "solution. What happens?",
        "options": [
            {"text": "The zinc comes out as a grey solid", "correct": False,
             "why": "Iron is below zinc, so it cannot push the zinc out"},
            {"text": "Nothing", "correct": True},
            {"text": "The solution turns blue", "correct": False,
             "why": "Blue is a copper solution, and nothing reacts here in "
                    "any case"},
            {"text": "The filings dissolve away", "correct": False,
             "why": "Iron is below zinc, so the iron is not taken into the "
                    "solution"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e20",
        "band": "easier",
        "text": "Carbon powder is heated strongly with copper oxide. Which "
                "gas is given off?",
        "options": [
            {"text": "Hydrogen", "correct": False,
             "why": "There is no hydrogen in either of the substances being "
                    "heated"},
            {"text": "Oxygen", "correct": False,
             "why": "The oxygen is taken by the carbon rather than released "
                    "on its own"},
            {"text": "Carbon monoxide", "correct": False,
             "why": "The gas collected turns limewater cloudy, which is "
                    "carbon dioxide"},
            {"text": "Carbon dioxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e21",
        "band": "easier",
        "text": "To predict whether a displacement will happen, which two "
                "things do you compare?",
        "options": [
            {"text": "The metal being added and the metal inside the "
                     "compound", "correct": True},
            {"text": "The colour of the solution and the colour of the metal",
             "correct": False,
             "why": "Colour is a clue that a reaction has run, not a way of "
                    "predicting one"},
            {"text": "The mass of the metal and the volume of the solution",
             "correct": False,
             "why": "Amounts change how much product forms, not whether a "
                    "reaction can happen"},
            {"text": "The price of the two metals", "correct": False,
             "why": "Price is a fact about people. The series is a fact about "
                    "the metals"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e22",
        "band": "easier",
        "text": "Copper wire reacts with silver nitrate solution. Complete "
                "the word equation: copper + silver nitrate →",
        "options": [
            {"text": "silver nitrate + copper", "correct": False,
             "why": "Those are the two starting substances again, so nothing "
                    "has been displaced"},
            {"text": "copper nitrate + silver", "correct": True},
            {"text": "copper silver + nitrate", "correct": False,
             "why": "The nitrate stays joined to a metal rather than coming "
                    "away on its own"},
            {"text": "copper oxide + silver nitride", "correct": False,
             "why": "There is no free oxygen here, and the nitrate moves "
                    "across as one whole part"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e23",
        "band": "easier",
        "text": "A magnesium ribbon is stood in copper sulfate solution. What "
                "happens to the temperature of the tube?",
        "options": [
            {"text": "It falls sharply", "correct": False,
             "why": "This reaction gives heat out rather than taking it in"},
            {"text": "It does not change", "correct": False,
             "why": "The tube becomes hot enough to notice, which is a sign "
                    "the reaction has run"},
            {"text": "It rises enough to notice", "correct": True},
            {"text": "It rises only after the colour has gone",
             "correct": False,
             "why": "The warming happens while the reaction is running, not "
                    "afterwards"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e24",
        "band": "easier",
        "text": "Zinc granules are dropped into pale green iron sulfate "
                "solution and a reaction runs. What happens to the colour?",
        "options": [
            {"text": "It turns deep blue", "correct": False,
             "why": "Blue is copper in solution, and no copper is present "
                    "here"},
            {"text": "It turns pale green from colourless", "correct": False,
             "why": "The green is there at the start and fades as the iron "
                    "leaves the solution"},
            {"text": "It stays exactly the same", "correct": False,
             "why": "The iron is leaving the solution, so its colour drains "
                    "away"},
            {"text": "The pale green fades", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e25",
        "band": "easier",
        "text": "Which of these pairs WOULD react?",
        "options": [
            {"text": "Magnesium added to silver nitrate solution",
             "correct": True},
            {"text": "Silver added to magnesium sulfate solution",
             "correct": False,
             "why": "Silver is below magnesium, so it cannot displace it"},
            {"text": "Copper added to zinc sulfate solution", "correct": False,
             "why": "Copper is below zinc, so nothing happens"},
            {"text": "Silver added to copper sulfate solution",
             "correct": False,
             "why": "Silver is below copper, so nothing happens"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e26",
        "band": "easier",
        "text": "Zinc sulfate and copper are the two products of one of these "
                "reactions. Which one?",
        "options": [
            {"text": "Copper added to zinc sulfate solution", "correct": False,
             "why": "Copper is below zinc, so there is no reaction and no "
                    "products at all"},
            {"text": "Copper added to zinc oxide", "correct": False,
             "why": "Copper is below zinc, and there is no sulfate in either "
                    "substance"},
            {"text": "Zinc added to copper oxide", "correct": False,
             "why": "That would give copper and zinc oxide, and again there "
                    "is no sulfate involved"},
            {"text": "Zinc added to copper sulfate solution", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e27",
        "band": "easier",
        "text": "Magnesium, carbon, zinc, iron, copper, silver. Which of "
                "those is the least reactive?",
        "options": [
            {"text": "Copper", "correct": False,
             "why": "Copper is above silver, which is why copper displaces "
                    "silver and not the other way round"},
            {"text": "Iron", "correct": False,
             "why": "Iron is above copper, and copper is above silver"},
            {"text": "Silver", "correct": True},
            {"text": "Magnesium", "correct": False,
             "why": "Magnesium is the most reactive of those, not the least"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e28",
        "band": "easier",
        "text": "In a displacement, which of the two metals ends up as the "
                "solid element?",
        "options": [
            {"text": "The less reactive one", "correct": True},
            {"text": "The more reactive one", "correct": False,
             "why": "The more reactive metal takes the place in the compound, "
                    "so it goes into the solution"},
            {"text": "Whichever one was added", "correct": False,
             "why": "If the metal added is the less reactive one, nothing "
                    "happens at all"},
            {"text": "Whichever one is heavier", "correct": False,
             "why": "Density plays no part; position in the series decides "
                    "it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e29",
        "band": "easier",
        "text": "An iron nail is left in copper sulfate. Which colour does "
                "the solution move towards as the reaction runs?",
        "options": [
            {"text": "Deeper blue", "correct": False,
             "why": "The copper is leaving the solution, so the blue gets "
                    "weaker"},
            {"text": "Pale green", "correct": True},
            {"text": "Colourless", "correct": False,
             "why": "The iron going into the solution gives it a pale green "
                    "colour of its own"},
            {"text": "Bright red", "correct": False,
             "why": "The red-brown is the copper on the nail. The solution "
                    "goes pale green"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-e30",
        "band": "easier",
        "text": "Which of these would you NOT see in a tube where a "
                "displacement has run?",
        "options": [
            {"text": "Warming of the tube", "correct": False,
             "why": "These reactions give heat out, so a warm tube is "
                    "expected"},
            {"text": "A solid forming on the metal", "correct": False,
             "why": "The displaced metal appears as a solid, which is the "
                    "commonest sign of all"},
            {"text": "Bubbles of gas", "correct": True},
            {"text": "The colour of the solution changing", "correct": False,
             "why": "The colour changes as one metal leaves the solution and "
                    "the other goes into it"},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard s14–s30 ───────────────────────────────
    {
        "id": "c9-02-s14",
        "band": "standard",
        "text": "One piece of copper wire is left in zinc sulfate solution "
                "and another in silver nitrate solution. In which does the "
                "copper react?",
        "options": [
            {"text": "In both, because copper reacts with any dissolved "
                     "metal", "correct": False,
             "why": "Copper cannot displace zinc, which sits above it in the "
                    "series"},
            {"text": "In neither, because copper is the least reactive metal "
                     "there is", "correct": False,
             "why": "Silver sits below copper, so the silver nitrate tube "
                    "does react"},
            {"text": "Only in the silver nitrate, because copper is above "
                     "silver and below zinc", "correct": True},
            {"text": "Only in the zinc sulfate, because zinc is the easier of "
                     "the two to push out", "correct": False,
             "why": "Zinc is above copper, so that is the direction that "
                    "cannot run"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s15",
        "band": "standard",
        "text": "Of eight displacement proposals, five ran and three did "
                "nothing. What did the three have in common?",
        "options": [
            {"text": "The solutions used in them were too dilute to react",
             "correct": False,
             "why": "Concentration changes how fast a possible reaction goes, "
                    "not whether it can go"},
            {"text": "The added element was below the one in the compound",
             "correct": True},
            {"text": "The added element was above the one in the compound",
             "correct": False,
             "why": "That is the arrangement that does run. The three that "
                    "failed were the other way round"},
            {"text": "They were left standing for a shorter time than the "
                     "other five", "correct": False,
             "why": "Time changes how far a reaction gets, not whether it is "
                    "possible"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s16",
        "band": "standard",
        "text": "Two displacements both work, but one finishes in a minute "
                "and the other takes days. What is the same about them?",
        "options": [
            {"text": "In both, the two metals are next to each other in the "
                     "series", "correct": False,
             "why": "The quick one has metals far apart. Neighbouring metals "
                    "are what make a reaction slow"},
            {"text": "In both, the solution was the same strength",
             "correct": False,
             "why": "Nothing about strength follows from the two reactions "
                    "both working"},
            {"text": "In both, the same amount of solid is produced",
             "correct": False,
             "why": "How much solid forms depends on the amounts used, not on "
                    "the rule"},
            {"text": "In both, the added metal is above the one in the "
                     "compound", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s17",
        "band": "standard",
        "text": "Copper sulfate solution is blue and zinc sulfate solution is "
                "colourless. What does that colour difference tell you about "
                "which will react?",
        "options": [
            {"text": "Nothing at all — colour is not part of the prediction",
             "correct": True},
            {"text": "That the blue one reacts, because colour shows a "
                     "solution is active", "correct": False,
             "why": "Colour comes from the dissolved metal and says nothing "
                    "about reactivity"},
            {"text": "That the colourless one reacts, because it has nothing "
                     "in it to get in the way", "correct": False,
             "why": "Zinc sulfate is a solution of zinc, and the prediction "
                    "rests on positions"},
            {"text": "That neither reacts, because their colours are so "
                     "different", "correct": False,
             "why": "Colour is irrelevant. Zinc added to copper sulfate "
                    "reacts readily"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s18",
        "band": "standard",
        "text": "A displacement between a metal and a solution makes the tube "
                "noticeably warm. What does the warming tell you?",
        "options": [
            {"text": "That the metal was warm before it was added",
             "correct": False,
             "why": "The tube warms as the reaction runs, which is a sign of "
                    "the reaction itself"},
            {"text": "That the solution was too concentrated", "correct": False,
             "why": "Warming is a sign of a reaction, not of a fault in the "
                    "solution"},
            {"text": "That a chemical reaction has taken place",
             "correct": True},
            {"text": "That the reaction will run the other way as it cools",
             "correct": False,
             "why": "A displacement runs one way only, and cooling does not "
                    "reverse it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s19",
        "band": "standard",
        "text": "Why is testing BOTH directions of a pair a good check on the "
                "rule?",
        "options": [
            {"text": "Because repeating the same tube twice gives a more "
                     "reliable result", "correct": False,
             "why": "The reverse direction is not a repeat — it is a "
                    "different test, and that is the point"},
            {"text": "Because the rule says exactly one direction can run, so "
                     "a pair that reacted both ways would show it wrong",
             "correct": True},
            {"text": "Because the reverse direction runs more slowly and is "
                     "easier to watch", "correct": False,
             "why": "The reverse direction does not run, which is the whole "
                    "point of testing it"},
            {"text": "Because the two directions give the same products "
                     "either way", "correct": False,
             "why": "Only one direction gives products; the other gives "
                    "nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s20",
        "band": "standard",
        "text": "Blocks of magnesium are sometimes bolted to a steel hull "
                "instead of blocks of zinc. Would magnesium work?",
        "options": [
            {"text": "Yes, because magnesium is also above iron",
             "correct": True},
            {"text": "No, because only zinc can protect steel in seawater",
             "correct": False,
             "why": "Any metal above iron reacts in preference to it, and "
                    "zinc is not special"},
            {"text": "No, because magnesium is below iron in the series",
             "correct": False,
             "why": "Magnesium is well above iron, which is exactly why it "
                    "would work"},
            {"text": "Yes, but only because magnesium is heavier than zinc",
             "correct": False,
             "why": "Mass is not the reason. What matters is that magnesium "
                    "is above iron"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s21",
        "band": "standard",
        "text": "You have a solution of a metal's sulfate and want that metal "
                "as a solid, with no electricity available. What do you add?",
        "options": [
            {"text": "A metal below it in the reactivity series",
             "correct": False,
             "why": "A lower metal cannot push a higher one out of its "
                    "compound"},
            {"text": "More of the same sulfate solution", "correct": False,
             "why": "Adding more of the same substance changes nothing"},
            {"text": "A non-metal that dissolves easily in water",
             "correct": False,
             "why": "The metal has to be pushed out by something above it in "
                    "the order"},
            {"text": "A metal above it in the reactivity series",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s22",
        "band": "standard",
        "text": "Lead sits between iron and copper in the reactivity series. "
                "Predict what happens when lead is added to copper sulfate "
                "solution.",
        "options": [
            {"text": "The copper displaces the lead, which appears as a "
                     "solid", "correct": False,
             "why": "Copper is below lead, so it cannot push lead out of "
                    "anything"},
            {"text": "The lead displaces the copper, which appears as a "
                     "solid", "correct": True},
            {"text": "Nothing happens, because the two metals are close "
                     "together", "correct": False,
             "why": "Being close changes how obvious a reaction is, not "
                    "whether it can run"},
            {"text": "Nothing happens, because lead was not one of the six "
                     "metals in the strip", "correct": False,
             "why": "The rule works for any two metals whose positions are "
                    "known"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s23",
        "band": "standard",
        "text": "Iron filings and an iron nail of the same mass are each put "
                "into copper sulfate. What differs, and what does not?",
        "options": [
            {"text": "Both the speed and whether it happens differ",
             "correct": False,
             "why": "Shape changes the rate. It cannot make a possible "
                    "reaction impossible"},
            {"text": "Nothing differs, because the mass is the same",
             "correct": False,
             "why": "Filings have far more surface in contact, so they react "
                    "faster"},
            {"text": "The speed differs; whether it happens does not",
             "correct": True},
            {"text": "Whether it happens differs; the speed does not",
             "correct": False,
             "why": "It is the other way round — the rule fixes whether, and "
                    "shape fixes how fast"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s24",
        "band": "standard",
        "text": "A student predicts that zinc will displace magnesium from "
                "magnesium sulfate. What has gone wrong?",
        "options": [
            {"text": "Nothing at all; the prediction is right, but the "
                     "reaction is far too slow to see", "correct": False,
             "why": "It is not slow, it is impossible. Zinc sits below "
                    "magnesium"},
            {"text": "They have used a sulfate when an oxide was needed",
             "correct": False,
             "why": "The compound makes no difference. The positions do"},
            {"text": "They have forgotten that magnesium is a non-metal",
             "correct": False,
             "why": "Magnesium is a metal. Carbon is the non-metal in the "
                    "list"},
            {"text": "They have the order the wrong way round — magnesium is "
                     "above zinc", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s25",
        "band": "standard",
        "text": "Magnesium in copper sulfate, or copper in magnesium sulfate "
                "— which tube is easier to judge, and why?",
        "options": [
            {"text": "The first, because the blue draining away is easy to "
                     "see", "correct": True},
            {"text": "The second, because a colourless solution shows changes "
                     "more clearly", "correct": False,
             "why": "Nothing happens in the second tube, so there is no "
                    "change to see"},
            {"text": "Neither, because both tubes look the same throughout",
             "correct": False,
             "why": "The first tube loses its blue and grows a brown solid"},
            {"text": "The second, because copper is the more expensive metal",
             "correct": False,
             "why": "Price has nothing to do with what a tube shows"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s26",
        "band": "standard",
        "text": "A student says a displacement is just the two metals "
                "swapping places. Why is that a fair description?",
        "options": [
            {"text": "Because both metals end up dissolved in the solution "
                     "together", "correct": False,
             "why": "Only the more reactive metal dissolves; the other comes "
                    "out as a solid"},
            {"text": "Because the two metals combine to make a single new "
                     "metal", "correct": False,
             "why": "No new element is made. The two simply change places"},
            {"text": "Because the more reactive metal ends up joined to the "
                     "sulfate and the less reactive one ends up as the "
                     "element", "correct": True},
            {"text": "Because the sulfate is split between the two metals",
             "correct": False,
             "why": "The sulfate stays as one part and joins the more "
                    "reactive metal"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s27",
        "band": "standard",
        "text": "Which observation would tell you a displacement had "
                "FINISHED rather than merely started?",
        "options": [
            {"text": "The colour begins to change and a solid starts to form",
             "correct": False,
             "why": "That is the reaction starting, which is the opposite of "
                    "what was asked"},
            {"text": "The colour stops changing and no more solid forms",
             "correct": True},
            {"text": "The tube becomes warm to hold", "correct": False,
             "why": "Warming happens while the reaction is still running"},
            {"text": "Bubbles stop coming off the metal", "correct": False,
             "why": "No gas is given off in a displacement between a metal "
                    "and a solution"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s28",
        "band": "standard",
        "text": "You have iron, and solutions of zinc sulfate and copper "
                "sulfate. Which results would place iron between zinc and "
                "copper?",
        "options": [
            {"text": "A grey solid in the zinc sulfate, and nothing in the "
                     "copper sulfate", "correct": False,
             "why": "That would put iron above zinc and below copper, which "
                    "is the wrong way round"},
            {"text": "A solid in both tubes", "correct": False,
             "why": "Iron cannot displace zinc, so one of the tubes has to "
                    "show nothing"},
            {"text": "Nothing in either tube", "correct": False,
             "why": "Iron is above copper, so the copper sulfate tube must "
                    "react"},
            {"text": "Nothing in the zinc sulfate, and a brown solid in the "
                     "copper sulfate", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s29",
        "band": "standard",
        "text": "A displacement runs and the strip of added metal gets "
                "thinner. Where has that metal gone?",
        "options": [
            {"text": "Into the solution, as a compound", "correct": True},
            {"text": "Onto its own surface as a solid coat", "correct": False,
             "why": "The coat is the other metal, the one that came out of "
                    "the solution"},
            {"text": "Away as a gas", "correct": False,
             "why": "No gas is produced in a displacement between a metal and "
                    "a solution"},
            {"text": "Nowhere — the strip only looks thinner",
             "correct": False,
             "why": "The metal really is being used up, which is why the "
                    "strip thins"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-s30",
        "band": "standard",
        "text": "Copper, silver and gold each give the same result in cold "
                "water and in dilute acid. How does displacement help?",
        "options": [
            {"text": "It gives each of them a reaction with water at last",
             "correct": False,
             "why": "None of the three reacts with water, and displacement "
                    "does not change that"},
            {"text": "It shows all three are the same, so no order is needed",
             "correct": False,
             "why": "Copper displaces silver, so the three are not the same "
                    "as each other"},
            {"text": "It compares them against each other's compounds, which "
                     "separates them", "correct": True},
            {"text": "It cannot help, because a metal that does nothing in "
                     "acid does nothing anywhere else either", "correct": False,
             "why": "Copper does nothing in acid and still displaces silver "
                    "from its nitrate"},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder h14–h30 ─────────────────────────────────
    {
        "id": "c9-02-h14",
        "band": "harder",
        "text": "Zinc sulfate solution and copper sulfate solution are mixed "
                "by mistake, with no metal added at all. Predict what "
                "happens.",
        "options": [
            {"text": "Zinc comes out as a solid, because zinc is above "
                     "copper", "correct": False,
             "why": "The zinc here is already inside a compound, so it has "
                    "nothing left to give up"},
            {"text": "Nothing — a displacement needs a metal to be added",
             "correct": True},
            {"text": "Copper comes out as a solid, because copper is below "
                     "zinc", "correct": False,
             "why": "Both metals are already in compounds, and neither is a "
                    "metal that can displace"},
            {"text": "The two solutions react to make a new metal",
             "correct": False,
             "why": "No new element can be made by mixing two compounds"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h15",
        "band": "harder",
        "text": "Silver is recovered from used photographic solution by "
                "adding scrap iron. Explain why iron works, and whether "
                "copper would.",
        "options": [
            {"text": "Iron works only because it is magnetic, so the silver "
                     "can be pulled away from it afterwards", "correct": False,
             "why": "Magnetism plays no part. The silver is pushed out "
                    "chemically"},
            {"text": "Iron is above silver, so it displaces it; copper is "
                     "below silver, so copper would not work", "correct": False,
             "why": "Copper is above silver — the copper wire in silver "
                    "nitrate is the proof"},
            {"text": "Iron is above silver, so it displaces it; copper is "
                     "above silver too, so copper would work as well",
             "correct": True},
            {"text": "Iron works because it is the cheapest metal, and cost "
                     "is what decides whether a reaction runs", "correct": False,
             "why": "Cost decides which metal a works buys, not whether the "
                    "reaction is possible"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h16",
        "band": "harder",
        "text": "Predict what would be seen if a strip of magnesium were left "
                "in silver nitrate solution, and say which fact you used.",
        "options": [
            {"text": "Silver would build up on the magnesium, because "
                     "magnesium is above silver", "correct": True},
            {"text": "Nothing would happen, because silver nitrate is not a "
                     "sulfate", "correct": False,
             "why": "The rule compares the two metals; the part they are "
                    "joined to makes no difference"},
            {"text": "Magnesium would build up on the wire, leaving the "
                     "solution clear", "correct": False,
             "why": "Magnesium is the metal added, so it goes into the "
                    "solution rather than coming out"},
            {"text": "Nothing would happen, because magnesium and silver are "
                     "too far apart in the series to react", "correct": False,
             "why": "Being far apart makes a reaction quicker and more "
                    "obvious, not impossible"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h17",
        "band": "harder",
        "text": "Three unknown metals: X displaces Y from its sulfate, and Y "
                "displaces Z from its sulfate. What can you say about X and "
                "Z?",
        "options": [
            {"text": "Z is above X", "correct": False,
             "why": "X is above Y and Y is above Z, so X has to be above Z"},
            {"text": "X is above Z", "correct": True},
            {"text": "They are in the same place", "correct": False,
             "why": "Two steps of the order separate them, so they cannot be "
                    "level"},
            {"text": "Nothing, until X and Z are tested against each other",
             "correct": False,
             "why": "The order carries through: X above Y and Y above Z fixes "
                    "X above Z"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h18",
        "band": "harder",
        "text": "A student writes: 'copper is below zinc, therefore copper is "
                "unreactive.' Identify the error.",
        "options": [
            {"text": "There is no error; anything below zinc is unreactive",
             "correct": False,
             "why": "Copper displaces silver readily, so it is certainly not "
                    "unreactive"},
            {"text": "The error is that copper is above zinc, not below it",
             "correct": False,
             "why": "Copper really is below zinc. The error is in what "
                    "'below' is taken to mean"},
            {"text": "The error is that unreactive is not a word used about "
                     "metals", "correct": False,
             "why": "It is a fair word. The problem is using it for a metal "
                    "that does react"},
            {"text": "Below zinc only says less reactive than zinc, not "
                     "unreactive", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h19",
        "band": "harder",
        "text": "Two students disagree about why the nail reaction stops: one "
                "says the nail is fully coated, the other says the copper "
                "sulfate runs out. How would you decide?",
        "options": [
            {"text": "Weigh the nail before and after, and see whether it has "
                     "got heavier", "correct": False,
             "why": "It gets heavier on either explanation, so weighing "
                    "separates nothing"},
            {"text": "Use a bigger nail, since a bigger nail takes longer to "
                     "coat", "correct": False,
             "why": "A bigger nail changes both explanations at once, so "
                    "nothing is separated"},
            {"text": "Use a large excess of solution and see whether the "
                     "coated nail keeps reacting", "correct": True},
            {"text": "Warm the solution, since warming makes a reaction go "
                     "further than it otherwise would", "correct": False,
             "why": "Warming changes the rate, not how far the reaction can "
                    "go"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h20",
        "band": "harder",
        "text": "Two students both correctly predict that zinc will displace "
                "copper. One says it will take seconds, the other days. Which "
                "part does the series support?",
        "options": [
            {"text": "Only that it happens", "correct": True},
            {"text": "Only the timing, since that is what a prediction is "
                     "for", "correct": False,
             "why": "The series orders reactivity and gives no time for "
                    "anything"},
            {"text": "Both parts, since position fixes the speed exactly",
             "correct": False,
             "why": "Position suggests whether a reaction will be brisk, but "
                    "it fixes no time"},
            {"text": "Neither part, since the series applies to metals in "
                     "solution alone", "correct": False,
             "why": "The series applies wherever the two positions are known"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h21",
        "band": "harder",
        "text": "Metal M fizzes in dilute acid but does not react with zinc "
                "sulfate solution. Where is M?",
        "options": [
            {"text": "Above zinc, and below the metals that react with cold "
                     "water", "correct": False,
             "why": "If M were above zinc it would have displaced zinc from "
                    "its sulfate"},
            {"text": "Below zinc, and above the metals acid does not touch",
             "correct": True},
            {"text": "Below the metals acid does not touch", "correct": False,
             "why": "M fizzed in acid, so it is above the metals acid leaves "
                    "alone"},
            {"text": "Nowhere — the two results contradict each other",
             "correct": False,
             "why": "They fit together: M reacts with acid and sits below "
                    "zinc"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h22",
        "band": "harder",
        "text": "A works wants to recover copper from waste copper sulfate "
                "solution as cheaply as possible. Which metal, and what "
                "limits the choice?",
        "options": [
            {"text": "Silver, because it is a metal and the silver is easy to "
                     "get back afterwards", "correct": False,
             "why": "Silver is below copper, so it cannot displace copper at "
                    "all"},
            {"text": "Sodium, because the higher the metal the better the "
                     "reaction", "correct": False,
             "why": "Sodium reacts violently with the water itself, so it "
                    "never reaches the copper"},
            {"text": "Any metal, because every metal displaces every other "
                     "one", "correct": False,
             "why": "Only a metal above copper works, which rules most of "
                    "them out"},
            {"text": "Iron, because it is above copper and cheap; a metal too "
                     "high would react with the water as well", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h23",
        "band": "harder",
        "text": "Explain why a displacement can show that a metal is "
                "dissolved in a colourless solution, but cannot say which "
                "metal it is.",
        "options": [
            {"text": "A solid appearing only shows the dissolved metal is "
                     "below the one added", "correct": True},
            {"text": "A solid appearing shows exactly which metal it is, from "
                     "the colour of the solid", "correct": False,
             "why": "Several metals give a similar grey deposit, so its "
                    "colour cannot name one"},
            {"text": "A solid appearing shows nothing, because a colourless "
                     "solution holds no metal", "correct": False,
             "why": "Zinc sulfate solution is colourless and holds zinc"},
            {"text": "A solid appearing names the metal, because one metal "
                     "sits below any other", "correct": False,
             "why": "Many metals sit below a given one, so the result narrows "
                    "it rather than naming it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h24",
        "band": "harder",
        "text": "Two metals are close together in the series and a "
                "displacement between them is hard to see. Why is that a "
                "practical difficulty rather than a fault in the rule?",
        "options": [
            {"text": "The rule applies only to metals far apart in the "
                     "series", "correct": False,
             "why": "The rule is about the order, and neighbouring metals "
                    "obey it like any others"},
            {"text": "The rule is about solutions, and close metals make "
                     "solids instead", "correct": False,
             "why": "Every displacement of this kind makes a solid, however "
                    "far apart the metals are"},
            {"text": "The rule says which direction is possible, not how "
                     "obvious it will be", "correct": True},
            {"text": "It is a fault in the rule, which is why the series is "
                     "no more than a rough guide", "correct": False,
             "why": "The reaction does run. It is simply small and slow"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h25",
        "band": "harder",
        "text": "A gold ring is left in silver nitrate solution. Gold sits "
                "below silver in the series. Predict what happens.",
        "options": [
            {"text": "Silver is deposited on the gold", "correct": False,
             "why": "Gold is below silver, so it cannot displace silver from "
                    "anything"},
            {"text": "The gold dissolves and silver comes out",
             "correct": False,
             "why": "That would need gold to be above silver, and it is not"},
            {"text": "Nothing", "correct": True},
            {"text": "The ring turns from gold to silver", "correct": False,
             "why": "One element cannot change into another in a chemical "
                    "reaction"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h26",
        "band": "harder",
        "text": "Why does it make no difference whether the metal is joined "
                "to a sulfate, a nitrate or an oxide?",
        "options": [
            {"text": "Because all three of those parts are the same substance "
                     "under different names", "correct": False,
             "why": "They are three different substances. They simply behave "
                    "the same way here"},
            {"text": "Because all three break down on their own as soon as a "
                     "metal is added", "correct": False,
             "why": "Nothing breaks down on its own. The more reactive metal "
                    "takes the part"},
            {"text": "Because the sulfate, nitrate or oxide is removed first "
                     "by the water", "correct": False,
             "why": "Nothing is removed first, and the oxide reaction uses no "
                    "water at all"},
            {"text": "Because the prediction compares the two metals, and the "
                     "part they share joins whichever one wins",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h27",
        "band": "harder",
        "text": "Scrap iron is added to a tank of copper sulfate and the "
                "copper is collected. Why must the iron be in excess, and "
                "what is left in the tank?",
        "options": [
            {"text": "So that all the copper comes out; the tank ends with "
                     "iron sulfate solution and leftover iron", "correct": True},
            {"text": "So that the reaction goes faster; the tank ends with "
                     "copper sulfate solution and copper", "correct": False,
             "why": "Excess decides how completely the reaction runs, and the "
                    "copper sulfate is used up"},
            {"text": "So that the iron does not dissolve; the tank ends with "
                     "iron and copper sulfate", "correct": False,
             "why": "The iron dissolving is the reaction. It is the copper "
                    "that comes out"},
            {"text": "So that the solution stays blue; the tank ends with "
                     "blue solution and iron", "correct": False,
             "why": "The blue fading is the sign the reaction has run, so "
                    "keeping it blue is failure"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h28",
        "band": "harder",
        "text": "A student proposes placing an unknown metal in the series "
                "using ONE displacement test. What is the most that one test "
                "can establish?",
        "options": [
            {"text": "Its exact position, since a single reaction settles the "
                     "order", "correct": False,
             "why": "One comparison places it on one side of one metal, and "
                    "no more than that"},
            {"text": "A boundary — that the unknown is above or below one "
                     "particular metal", "correct": True},
            {"text": "Nothing, since a single test cannot be evidence",
             "correct": False,
             "why": "One result is real evidence. It simply does not fix a "
                    "whole position"},
            {"text": "Its position relative to every other metal in the "
                     "series at once", "correct": False,
             "why": "One test compares the unknown with one metal only"},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h29",
        "band": "harder",
        "text": "A student has copper, silver, and money for one solution: "
                "copper sulfate or silver nitrate. Which should they buy to "
                "demonstrate the rule?",
        "options": [
            {"text": "Copper sulfate, because it is blue and colour changes "
                     "show up best", "correct": False,
             "why": "Silver cannot displace copper, so the blue would not "
                    "change at all"},
            {"text": "Either, because both tubes would show a reaction",
             "correct": False,
             "why": "Only one of the two directions runs; the other shows "
                    "nothing"},
            {"text": "Copper sulfate, because silver is the more valuable "
                     "metal and should be kept", "correct": False,
             "why": "Value has nothing to do with which direction reacts"},
            {"text": "Silver nitrate, because copper is above silver and that "
                     "is the direction that reacts", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-02-h30",
        "band": "harder",
        "text": "The blue in a zinc-and-copper-sulfate tube stopped fading "
                "two days ago and the tube has stood untouched since. What "
                "has happened since then?",
        "options": [
            {"text": "The copper has slowly gone back into the solution as "
                     "the tube cooled", "correct": False,
             "why": "The reaction does not run backwards. Zinc stays above "
                    "copper"},
            {"text": "The zinc has begun to displace the sulfate itself",
             "correct": False,
             "why": "The sulfate is not displaced; it joins whichever metal "
                    "wins"},
            {"text": "Nothing more — all the copper that could come out has "
                     "come out", "correct": True},
            {"text": "The reaction has kept going, too slowly to see",
             "correct": False,
             "why": "The colour stopping is the sign there was nothing left "
                    "to react with"},
        ],
        "figure": None,
    },
]
