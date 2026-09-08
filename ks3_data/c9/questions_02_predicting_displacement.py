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
]
