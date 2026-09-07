"""C3 lesson 06 — Chromatography: twelve questions (MRB-269).

The lesson's argument is a tug of war: every dissolved substance is pulled two
ways at once, sticking to the paper against dissolving in the moving solvent,
and how far it travels is decided by nothing else. Three method decisions can
ruin the whole run, each in its own way, and a readable chromatogram then
convicts one pen out of four. These twelve probe that argument from the angles
the ladder leaves alone: the ladder asks what chromatography separates and why
the baseline is pencil, so nothing here asks either of those again. They ask
instead where the colours came from, what a count of spots means, why the
solvent has to start low and why the paper comes out early, what a missing spot
proves, and what changes and what does not when you change the solvent.

The distractors are built from the lesson's two declared misconceptions.
MIX-11 (the dye or colour is made by the paper or the solvent) drives the wrong
options in e01, e02, e04, s02 and s04 — every one of them has the paper or the
solvent adding, removing or creating colour rather than doing the one thing it
does, which is pull. MIX-12 (the spot that travels furthest is the one there is
most of) drives e04, s03, h01 and h03, where height is read as a statement
about quantity, or quantity is read as a push. A third strand, everywhere in
the lesson and not in the register, is that a spot's height is a fixed property
of the dye rather than the outcome of a contest that has two sides: e03, s01,
h02 and h04 each carry a distractor that treats it that way.

⚑ A ruling, and it is a deviation from Design's NOTES §4 flag 13. Flag 13 sets
`<sub>` — not a Unicode subscript — as the way the R_f symbol is written, and
the lesson record follows it exactly, in three strings. This file does not use
the symbol at all. Question files are plain text by settled convention across
the key stage (every existing bank writes CaCO₃ and H₂O with Unicode and
carries no HTML anywhere), and nothing renders a question yet, so there is no
read site that could prove `<sub>` survives here. h02 therefore names the
quantity in words — "divide the distance the spot travelled by the distance
the solvent travelled" — which is what a student has to be able to do anyway,
and needs no markup to say. Flag 13 is untouched where it was ruled: on the
page.
"""

UNIT = "C3"
LESSON = "chromatography"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c3-06-e01",
        "band": "easier",
        "text": "A single dot of black ink is put on chromatography paper and "
                "the solvent creeps up through it. The dot climbs and splits "
                "into three coloured spots. Where did those three colours "
                "come from?",
        "options": [
            {"text": "They were in the ink all along — its black was a "
                     "mixture of them", "correct": True},
            {"text": "The paper released them from its fibres as the wet "
                     "front passed over", "correct": False,
             "why": "The paper adds nothing to the run. Its only job is to "
                    "hold on to the dyes, and holding on is the opposite of "
                    "giving something out."},
            {"text": "The solvent reacted with the ink and made three new "
                     "colours out of it", "correct": False,
             "why": "Nothing reacts. The solvent dissolves the dyes and "
                    "carries them, and every dye that comes off the paper is "
                    "the same substance that went on it."},
            {"text": "The ink broke down into three simpler colours as it "
                     "climbed the paper", "correct": False,
             "why": "Nothing broke down either. The three dyes were separate "
                    "substances sitting in the same drop, and all the run did "
                    "was move them apart."},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e02",
        "band": "easier",
        "text": "One lane of a finished chromatogram shows three separate "
                "coloured spots at three different heights. What does the "
                "number three tell you about that ink?",
        "options": [
            {"text": "It was spotted onto the baseline three times",
             "correct": False,
             "why": "One dot was spotted. What the run counts is how many "
                    "different substances were in that dot, not how many "
                    "times you touched the paper."},
            {"text": "The solvent passed over the sample three times on its "
                     "way up", "correct": False,
             "why": "The solvent rises once and keeps going. Three spots "
                    "means three substances that each stopped in a different "
                    "place, not three passes."},
            {"text": "The paper has three layers, and each one held on to a "
                     "colour", "correct": False,
             "why": "The paper is one thing and it contributes no colour of "
                    "its own. It pulls on every dye, and the dyes differ in "
                    "how hard they are pulled."},
            {"text": "Three different substances were dissolved in it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e03",
        "band": "easier",
        "text": "The solvent in the tank has to start BELOW the pencil "
                "baseline. What goes wrong if it starts above it?",
        "options": [
            {"text": "The paper gets wet before the run begins, so the spots "
                     "spread sideways", "correct": False,
             "why": "The paper is wet all the way through a run — that is how "
                    "the solvent travels. What matters is whether the ink "
                    "starts in the liquid or above it."},
            {"text": "The ink dots sit in the liquid and dissolve straight "
                     "into the tank", "correct": True},
            {"text": "The solvent has less paper to climb, so the spots "
                     "cannot separate far enough", "correct": False,
             "why": "How far the spots separate is set by when you take the "
                    "paper out. Here they never separate at all, because "
                    "there is nothing left on the paper to separate."},
            {"text": "The pencil baseline dissolves and smears up the "
                     "paper", "correct": False,
             "why": "Pencil is graphite and does not dissolve, wherever the "
                    "solvent starts — that is exactly why the baseline is "
                    "drawn in it. It is the ink that is at risk here."},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e04",
        "band": "easier",
        "text": "One lane shows a faint spot near the top of the paper and a "
                "thick dark spot low down. Which statement is right?",
        "options": [
            {"text": "There is more of the top dye, because it travelled "
                     "further up the paper", "correct": False,
             "why": "How far a spot goes says nothing about how much of it "
                    "there is. One particle of a dye is pulled exactly as "
                    "hard as a million of them."},
            {"text": "The low spot is dark because the paper soaked colour "
                     "into it on the way", "correct": False,
             "why": "The paper puts no colour into anything. A spot is dark "
                    "because there is a lot of that dye in it, and that is "
                    "the only thing darkness reports."},
            {"text": "There is more of the low dye, and height is about the "
                     "tug of war alone", "correct": True},
            {"text": "The low spot is a heavier substance, which is why it "
                     "could not climb", "correct": False,
             "why": "Nothing in chromatography is about weight or size. The "
                    "low dye clings to the paper more strongly than it "
                    "dissolves in the solvent, and that is the whole reason."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c3-06-s01",
        "band": "standard",
        "text": "A student leaves the paper in the tank until the solvent "
                "reaches the top edge. Two things are now impossible. Which "
                "pair?",
        "options": [
            {"text": "Separating the fastest spots from each other, and "
                     "measuring how far the solvent went", "correct": True},
            {"text": "Separating the slowest spots from each other, and "
                     "telling which colours are there", "correct": False,
             "why": "The slow spots are the ones still spread out, and every "
                    "colour is still visible. The damage is at the fast end, "
                    "where the spots have piled up against the edge."},
            {"text": "Drawing the pencil baseline, and knowing where each "
                     "of the spots started", "correct": False,
             "why": "The baseline was drawn before the paper went in and has "
                    "not moved since. Nothing about it depends on when the "
                    "paper comes out."},
            {"text": "Dissolving the ink at all, and getting the solvent to "
                     "climb the paper", "correct": False,
             "why": "Both of those happened — the solvent reached the top, so "
                    "it certainly climbed. What is lost is the finish, not "
                    "the start."},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s02",
        "band": "standard",
        "text": "The note and all four suspect pens are run on ONE piece of "
                "paper, at the same time. Why does that matter?",
        "options": [
            {"text": "The paper adds a little colour of its own, so every "
                     "lane must get the same amount", "correct": False,
             "why": "The paper adds no colour to any lane. It is one side of "
                    "the tug of war and nothing else, and the dyes on the "
                    "paper are the dyes that went on it."},
            {"text": "Dyes only separate properly when several inks are run "
                     "side by side", "correct": False,
             "why": "A single lane separates perfectly well on its own. The "
                    "neighbouring lanes are there to be compared against, not "
                    "to make the separation work."},
            {"text": "A height only means something next to other heights "
                     "from the same run", "correct": True},
            {"text": "One sheet of paper uses far less solvent than five "
                     "separate runs would", "correct": False,
             "why": "It does, and that is not the reason. A warmer room, a "
                    "different paper or a different solvent moves every spot, "
                    "so two runs cannot be compared height for height."},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s03",
        "band": "standard",
        "text": "The same red dye is spotted twice on one baseline: a tiny "
                "dot in one lane, a thick blob in the other. After the run, "
                "what is different about the two spots?",
        "options": [
            {"text": "The blob has travelled further, because there was more "
                     "of it pushing upwards", "correct": False,
             "why": "Amount is not a push. Every particle of that dye meets "
                    "exactly the same tug of war, so having more of them "
                    "changes nothing about how far they go."},
            {"text": "The blob has travelled less far, because there was more "
                     "of it to drag along", "correct": False,
             "why": "Nothing is dragged and nothing is heavier. It is the "
                    "same dye in both lanes, so the paper and the solvent "
                    "pull on it identically in both."},
            {"text": "They are at different heights, because no two lanes "
                     "ever come out quite the same", "correct": False,
             "why": "The two lanes are on one sheet, in one solvent, for the "
                    "same time — which is exactly the arrangement that makes "
                    "heights comparable."},
            {"text": "They are at the same height, and only the size and "
                     "darkness differ", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s04",
        "band": "standard",
        "text": "A drug test is run properly — pencil baseline, solvent below "
                "the spots, paper taken out in time — and the finished paper "
                "looks blank. What has most likely happened?",
        "options": [
            {"text": "The sample was far too dilute for any of it to climb "
                     "the paper and be seen", "correct": False,
             "why": "How much you put on changes how dark a spot is, never "
                    "whether it moves. A dilute sample gives a faint spot, "
                    "not an empty lane."},
            {"text": "The substances separated, but they are colourless and "
                     "need a spray or ultraviolet light to show",
             "correct": True},
            {"text": "Nothing separated at all, because only coloured "
                     "substances can be separated this way", "correct": False,
             "why": "Colour has nothing to do with the tug of war. Amino "
                    "acids, sugars and drugs all separate perfectly well; "
                    "they simply arrive invisible."},
            {"text": "The solvent never climbed the paper properly, so the "
                     "run did not really happen", "correct": False,
             "why": "The method was followed and the paper came out in time, "
                    "so the front rose as it should. A blank paper after a "
                    "good run is about what you can see, not what moved."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c3-06-h01",
        "band": "harder",
        "text": "Two inks are run side by side on one paper. Ink 1 gives a "
                "faint spot 8 cm above the baseline. Ink 2 gives a very dark "
                "spot 8 cm above the baseline. What can you conclude?",
        "options": [
            {"text": "They are different dyes, because the two spots are "
                     "different darknesses", "correct": False,
             "why": "Darkness reports how much, not which. Two different "
                    "amounts of one dye look exactly like this, and the "
                    "matching height is the part that identifies."},
            {"text": "Ink 2 holds more dyes than ink 1, because its spot has "
                     "more colour in it", "correct": False,
             "why": "How many dyes an ink holds is how many spots it gives, "
                    "and each of these gave one. Extra darkness is extra of "
                    "the same thing."},
            {"text": "They may well be the same dye, with more of it in "
                     "ink 2", "correct": True},
            {"text": "Ink 1's dye is held by the paper more strongly, which "
                     "is why its spot is fainter", "correct": False,
             "why": "The paper's grip decides height, and both spots are at "
                    "the same height — so the grip is the same. Faintness is "
                    "a statement about amount."},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h02",
        "band": "harder",
        "text": "Chemists divide the distance a spot travelled by the "
                "distance the solvent travelled, so that one lab's result "
                "means something in another. On one chromatogram the solvent "
                "front travelled 10.0 cm from the baseline and a green spot "
                "travelled 6.5 cm. What is that value for the green dye?",
        "options": [
            {"text": "0.65", "correct": True},
            {"text": "1.54", "correct": False,
             "why": "That is the two distances divided the other way round. "
                    "The spot's distance goes on top, and it is always the "
                    "smaller of the two, so the value is always below 1."},
            {"text": "0.35", "correct": False,
             "why": "That is the 3.5 cm of paper ABOVE the spot divided by "
                    "10.0. What is measured is how far the spot travelled "
                    "from the baseline, not how far short of the front it "
                    "stopped."},
            {"text": "6.50", "correct": False,
             "why": "That is the spot's distance on its own, which is what "
                    "the dividing was meant to get rid of. A distance in "
                    "centimetres only means something in the run it came "
                    "from."},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h03",
        "band": "harder",
        "text": "A note gives four spots. A suspect's pen gives spots at the "
                "same heights as three of them, and gives nothing at the "
                "fourth height. Is it a match?",
        "options": [
            {"text": "Yes — three heights out of four agreeing is close "
                     "enough to say it is the same ink", "correct": False,
             "why": "A missing spot rules a sample out as firmly as a wrong "
                    "one. The note holds a substance this pen does not, so "
                    "the two inks are not the same."},
            {"text": "Yes, as long as the fourth spot was only a faint one on "
                     "the note", "correct": False,
             "why": "Faint means there was little of it, not that it does not "
                    "count. It is still a substance the note has and the "
                    "suspect's pen has not."},
            {"text": "No — the heights would all have to differ for the two "
                     "inks to be told apart", "correct": False,
             "why": "That is the wrong way round. Matching heights are what "
                    "agreement looks like; it is the height with nothing at "
                    "it that settles this one."},
            {"text": "No — the note holds a dye this pen does not have",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h04",
        "band": "harder",
        "text": "The same four inks are run again the next day in a different "
                "solvent, correctly in every other way. Every spot comes out "
                "at a different height from before. Has something gone wrong?",
        "options": [
            {"text": "Yes — a dye should climb the same distance every time, "
                     "so this paper must be faulty", "correct": False,
             "why": "A height is not a property of the dye by itself. It is "
                    "the result of a contest between the paper and whichever "
                    "solvent is moving, and one side of that contest has been "
                    "swapped."},
            {"text": "No — one side of the tug of war has changed, so every "
                     "height changes with it", "correct": True},
            {"text": "No — the lanes were spotted in a different order, so "
                     "the spots have swapped over", "correct": False,
             "why": "Changing the order of the lanes would move things "
                    "sideways. What has changed here is how high every spot "
                    "sits in every lane."},
            {"text": "Yes — the dyes have reacted with the new solvent and "
                     "become different substances", "correct": False,
             "why": "A solvent dissolves and carries; it does not react. The "
                    "same four inks are on the paper, pulled by a different "
                    "partner."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-06-e05",
        "band": "easier",
        "text": "What is the solvent front on a chromatogram?",
        "options": [
            {"text": "The lowest edge of the paper, the part that is standing "
                     "in the liquid in the bottom of the tank",
             "correct": False,
             "why": "That is where the solvent starts. The front is where it "
                    "has climbed TO"},
            {"text": "The highest point the solvent has climbed to",
             "correct": True},
            {"text": "The pencil line the spots are placed on",
             "correct": False,
             "why": "That is the baseline. The front is the solvent's "
                    "furthest point"},
            {"text": "The first spot to appear as the paper dries",
             "correct": False,
             "why": "The front is a line made by the solvent itself, not by "
                    "any of the dyes"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e06",
        "band": "easier",
        "text": "What is a chromatogram?",
        "options": [
            {"text": "The tank of solvent that the paper is stood in, "
                     "together with the lid that stops the solvent "
                     "evaporating out of it",
             "correct": False,
             "why": "That is the apparatus. The chromatogram is the result "
                    "you take out of it"},
            {"text": "The pencil line the spots are placed on",
             "correct": False,
             "why": "That is the baseline, which is one part of the finished "
                    "paper"},
            {"text": "The finished paper, with each substance separated into "
                     "a spot of its own",
             "correct": True},
            {"text": "The machine used to measure the heights",
             "correct": False,
             "why": "The heights are measured with a ruler. There is no "
                    "machine in this method"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e07",
        "band": "easier",
        "text": "Black ink from two different manufacturers is run on the "
                "same paper and gives two different sets of spots. What does "
                "that show?",
        "options": [
            {"text": "That one of the two inks has gone off, since a fresh "
                     "black ink always separates into the same standard set of "
                     "dyes",
             "correct": False,
             "why": "There is no standard set. Each maker chooses its own "
                    "recipe for black"},
            {"text": "That one of them was run in the wrong solvent",
             "correct": False,
             "why": "They were run on the same paper in the same solvent, "
                    "which is exactly what makes the comparison fair"},
            {"text": "That black is not really a colour",
             "correct": False,
             "why": "Nothing here is about colour theory. It is about what is "
                    "dissolved in each ink"},
            {"text": "That each maker mixes its black from a different set of "
                     "dyes",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c3-06-s05",
        "band": "standard",
        "text": "One dye travels almost to the solvent front. What does that "
                "say about it?",
        "options": [
            {"text": "That there is more of it in the ink than of any other "
                     "dye",
             "correct": False,
             "why": "How much there is changes how dark the spot is, never "
                    "how high it goes"},
            {"text": "That it dissolves in the moving solvent far more "
                     "readily than it sticks to the paper",
             "correct": True},
            {"text": "That its particles are the smallest in the ink",
             "correct": False,
             "why": "Nothing here is about size. It is a tug of war between "
                    "the paper and the solvent"},
            {"text": "That it was spotted on last",
             "correct": False,
             "why": "All the spots start on the same baseline at the same "
                    "time. The order of spotting changes nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s06",
        "band": "standard",
        "text": "One lane's spot never leaves the baseline at all, even "
                "though the solvent has climbed right past it. What does that "
                "mean?",
        "options": [
            {"text": "That the spot was drawn in pencil rather than being "
                     "made with ink, so there was never any dye there for the "
                     "solvent to pick up",
             "correct": False,
             "why": "A good point about pencil, and this lane holds a real "
                    "sample. It is a dye that will not move"},
            {"text": "That there was too little of that substance to move",
             "correct": False,
             "why": "Even a faint trace travels if the solvent can carry it. "
                    "Amount changes darkness, not height"},
            {"text": "That substance sticks to the paper so strongly that the "
                     "solvent cannot carry it",
             "correct": True},
            {"text": "That the solvent never reached that lane",
             "correct": False,
             "why": "The solvent rises across the whole width of the paper at "
                    "once, so every lane gets it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s07",
        "band": "standard",
        "text": "A student puts the ink on the baseline as one blob a "
                "centimetre across, instead of a small dot. What goes wrong?",
        "options": [
            {"text": "The blob is too heavy, so the paper sags into the "
                     "solvent and the run is drowned before it can start",
             "correct": False,
             "why": "A drop of ink weighs nothing. What it ruins is the "
                    "spots, not the paper"},
            {"text": "The dyes travel further, because there is more of them "
                     "to be carried",
             "correct": False,
             "why": "Height does not depend on amount. A big blob gives big "
                    "spots at the same heights"},
            {"text": "The blob dissolves the pencil line",
             "correct": False,
             "why": "Graphite is insoluble, which is exactly why the baseline "
                    "is drawn in pencil"},
            {"text": "The dyes spread sideways and their spots overlap, so "
                     "the separated colours cannot be told apart",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-06-h05",
        "band": "harder",
        "text": "A height in centimetres means nothing in another laboratory, "
                "but a spot's distance divided by the solvent's distance does. "
                "Why?",
        "options": [
            {"text": "Because dividing turns the measurement into a "
                     "percentage",
             "correct": False,
             "why": "It is a ratio with no units at all rather than a "
                    "percentage, and agreeing units is not what fixes the "
                    "problem"},
            {"text": "Because dividing removes the effect of how far the "
                     "solvent happened to run in that particular tank",
             "correct": True},
            {"text": "Because the number that comes out is always the same "
                     "for every dye",
             "correct": False,
             "why": "It differs from dye to dye — which is the whole point of "
                    "quoting it"},
            {"text": "Because the second laboratory can then use whichever "
                     "solvent it prefers",
             "correct": False,
             "why": "Change the solvent and the value changes too. What is "
                    "removed is the run's length, not the solvent's "
                    "identity"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h06",
        "band": "harder",
        "text": "A dye's ratio of spot distance to solvent distance is 0.40, "
                "and on this run the solvent front travelled 12.0 cm from the "
                "baseline. How far did the dye travel?",
        "options": [
            {"text": "30.0 cm",
             "correct": False,
             "why": "That is dividing 12.0 by 0.40. A spot can never travel "
                    "further than the solvent that carries it"},
            {"text": "12.4 cm",
             "correct": False,
             "why": "That is adding rather than multiplying, and it puts the "
                    "spot above the solvent front"},
            {"text": "4.8 cm",
             "correct": True},
            {"text": "It cannot be worked out without knowing how much dye "
                     "was spotted onto the baseline in the first place",
             "correct": False,
             "why": "The amount changes how dark the spot is, never how far "
                    "it goes. The two numbers given are enough"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h07",
        "band": "harder",
        "text": "Why would chromatography be useless for separating sand from "
                "water?",
        "options": [
            {"text": "Because sand is far too heavy to be carried up a piece "
                     "of paper against gravity, however long the run is left "
                     "to go on for",
             "correct": False,
             "why": "Weight is not the obstacle — the solvent climbs against "
                    "gravity carrying dissolved dyes quite happily. Sand is "
                    "not dissolved at all"},
            {"text": "Because sand has no colour, so the spots could not be "
                     "seen",
             "correct": False,
             "why": "Colourless substances separate perfectly well and are "
                    "then sprayed to show them. The problem here is earlier "
                    "than that"},
            {"text": "Because water cannot be used as the solvent",
             "correct": False,
             "why": "Water is a perfectly good chromatography solvent. The "
                    "trouble is that the sand is a solid in lumps"},
            {"text": "Because sand is not dissolved, so there is nothing for "
                     "the solvent to carry",
             "correct": True},
        ],
        "figure": None,
    },
]
