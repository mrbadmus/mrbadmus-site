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
    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-06-e08",
        "band": "easier",
        "text": "What makes the solvent travel up the chromatography paper?",
        "options": [
            {"text": "It soaks up through the tiny gaps between the fibres",
             "correct": True},
            {"text": "It is pushed up by the weight of the liquid in the tank",
             "correct": False,
             "why": "The liquid in the tank pushes nothing upwards. A strip "
                    "dipped into an open dish climbs just the same"},
            {"text": "It is pulled up the paper by the dyes on the baseline",
             "correct": False,
             "why": "A blank strip with nothing spotted on it climbs exactly "
                    "as far, so the dyes cannot be doing the pulling"},
            {"text": "It evaporates from the tank and lands higher up",
             "correct": False,
             "why": "That would dampen the whole sheet at once. What you see "
                    "is a wet front creeping steadily up from the bottom"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e09",
        "band": "easier",
        "text": "In paper chromatography, which part stays still and which "
                "part moves?",
        "options": [
            {"text": "The solvent stays still and the paper is drawn up "
                     "through it",
             "correct": False,
             "why": "The paper is clipped in place and never moves. What you "
                    "watch climbing is the wet front"},
            {"text": "The paper stays still and the solvent moves up through "
                     "it",
             "correct": True},
            {"text": "Both move — the paper sinks as the solvent climbs",
             "correct": False,
             "why": "The paper does not sink or shift at all during a run. "
                    "Only the solvent travels"},
            {"text": "The dyes move on their own and the solvent stays put",
             "correct": False,
             "why": "A dye cannot travel by itself. It moves only while "
                    "solvent is soaking past it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e10",
        "band": "easier",
        "text": "Which contest decides how far a substance travels up the paper?",
        "options": [
            {
             "text": "Its pull upwards against gravity",
             "correct": False,
             "why": "Gravity is not one side of the contest. It acts on the whole paper and everything on it, and decides nothing about which dye goes furthest.",
            },
            {
             "text": "Its grip on the paper against how well it dissolves",
             "correct": True,
            },
            {
             "text": "Its attraction to the other dyes in the mixture",
             "correct": False,
             "why": "Dyes in a mixture take no notice of one another. Each one has its own contest with the paper and the solvent",
            },
            {
             "text": "The solvent's pull against the substance's weight",
             "correct": False,
             "why": "Weight plays no part. A heavy substance travels as far as a light one if the solvent dissolves it as readily",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e11",
        "band": "easier",
        "text": "Why is a lid put on the chromatography tank while the paper "
                "runs?",
        "options": [
            {"text": "To keep the paper pressed flat against the glass",
             "correct": False,
             "why": "The paper has to hang free. Pressing it against the "
                    "glass is a fault, not something the lid is there for"},
            {"text": "To stop light fading the coloured spots as they climb",
             "correct": False,
             "why": "A run takes minutes and the dyes do not fade in that "
                    "time. Light is not what the lid keeps out"},
            {"text": "To keep the tank warm so the solvent climbs faster",
             "correct": False,
             "why": "A lid heats nothing, and the speed of the climb is not "
                    "what is being protected"},
            {"text": "To stop the solvent evaporating from the paper",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e12",
        "band": "easier",
        "text": "What goes wrong if the chromatography paper is allowed to "
                "touch the side of the beaker?",
        "options": [
            {"text": "The wet paper tears along the line where it touches",
             "correct": False,
             "why": "Wet paper does not tear against smooth glass, and a "
                    "tear is not what spoils these runs"},
            {"text": "Solvent creeps along the glass and the front goes "
                     "crooked",
             "correct": True},
            {"text": "The spots transfer onto the glass and are lost",
             "correct": False,
             "why": "Dyes travel in solvent inside the paper. They do not "
                    "jump across onto the beaker"},
            {"text": "The glass cools the solvent so that it stops climbing",
             "correct": False,
             "why": "The beaker is at room temperature, and so is the "
                    "solvent. Nothing is cooled by the contact"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e13",
        "band": "easier",
        "text": "A sample is put on the baseline as several small drops, with "
                "the paper left to dry between each one. Why dry it in "
                "between?",
        "options": [
            {"text": "So that nothing from the spot can drip down and spoil "
                     "the solvent",
             "correct": False,
             "why": "The solvent in the tank sits below the baseline and "
                    "never touches the sample, wet or dry"},
            {"text": "So that the pencil baseline does not smudge",
             "correct": False,
             "why": "Graphite does not smudge when it gets wet, and the line "
                    "is not what the drying protects"},
            {"text": "So that the spot stays small instead of spreading wide",
             "correct": True},
            {"text": "So that the dyes have time to soak deep into the "
                     "fibres and hold on",
             "correct": False,
             "why": "Soaking deeper would hold the dyes back, which is the "
                    "opposite of what is wanted"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e14",
        "band": "easier",
        "text": "When a finished chromatogram is measured, where are the distances measured from?",
        "options": [
            {
             "text": "The pencil baseline",
             "correct": True,
            },
            {
             "text": "The bottom edge",
             "correct": False,
             "why": "The paper usually dips a centimetre or two below the baseline, so every reading taken this way is too big",
            },
            {
             "text": "The solvent level",
             "correct": False,
             "why": "That level is below the paper's spots and is not marked anywhere on the paper",
            },
            {
             "text": "The top edge",
             "correct": False,
             "why": "Nothing starts at the top. Every substance begins its journey at the baseline",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e15",
        "band": "easier",
        "text": "A spot on a finished chromatogram is nearly a centimetre "
                "across. Which part of it is the distance measured to?",
        "options": [
            {"text": "The lower edge, nearest the baseline",
             "correct": False,
             "why": "Using the near edge makes every reading too small, and "
                    "it is not the agreed way of doing it"},
            {"text": "The upper edge, nearest the solvent front",
             "correct": False,
             "why": "Using the far edge makes every reading too large, and "
                    "it is not the agreed way of doing it"},
            {"text": "Whichever edge is easier to see",
             "correct": False,
             "why": "A measurement has to be taken the same way every time, "
                    "or two chromatograms cannot be compared at all"},
            {"text": "The centre of the spot",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e16",
        "band": "easier",
        "text": "A chemist divides the distance a spot travelled by the "
                "distance the solvent travelled. What unit does the answer "
                "carry?",
        "options": [
            {"text": "Centimetres",
             "correct": False,
             "why": "Dividing centimetres by centimetres cancels the unit "
                    "rather than keeping it"},
            {"text": "No unit at all",
             "correct": True},
            {"text": "Centimetres squared",
             "correct": False,
             "why": "Multiplying two lengths gives a squared unit. This is a "
                    "division, and a division cancels"},
            {"text": "Per centimetre",
             "correct": False,
             "why": "Dividing a length by a length leaves nothing behind, "
                    "not a per-centimetre unit"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e17",
        "band": "easier",
        "text": "Can the ratio of a spot's distance to the solvent's distance "
                "ever come out greater than 1?",
        "options": [
            {"text": "Yes, if the paper is left in the tank long enough",
             "correct": False,
             "why": "However long the run goes on, the spot is still being "
                    "carried by the solvent and cannot get ahead of it"},
            {"text": "Yes, if a great deal of that dye was spotted onto the "
                     "baseline to begin with",
             "correct": False,
             "why": "Amount changes how dark a spot is, never how far it "
                    "climbs compared with the front"},
            {"text": "No — the spot cannot travel further than the solvent "
                     "carrying it",
             "correct": True},
            {"text": "Yes, if the solvent is swapped for a faster one",
             "correct": False,
             "why": "A faster solvent carries the spot further as well, so "
                    "the spot still finishes below the front"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e18",
        "band": "easier",
        "text": "Two laboratories want to compare their ratio values for the "
                "same dye. What has to be the same in both runs?",
        "options": [
            {"text": "The solvent and the type of paper",
             "correct": True},
            {"text": "The temperature of the room, and nothing else",
             "correct": False,
             "why": "Temperature makes a small difference, but it is the "
                    "solvent and the paper that decide how far a dye goes"},
            {"text": "The size of the spot put onto the baseline",
             "correct": False,
             "why": "Spot size changes how dark and how wide a spot is, not "
                    "the ratio that comes out of it"},
            {"text": "The number of other spots on the paper",
             "correct": False,
             "why": "The two laboratories are comparing one dye. How many "
                    "other substances are present changes nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e19",
        "band": "easier",
        "text": "An unknown dye travels exactly as far as a known dye on the "
                "same paper. Does that prove they are the same substance?",
        "options": [
            {"text": "Yes — no two substances ever travel the same distance "
                     "on one paper",
             "correct": False,
             "why": "Plenty of different substances happen to travel the "
                    "same distance, which is why a match settles nothing"},
            {"text": "Yes, as long as the two spots are the same colour",
             "correct": False,
             "why": "Two different dyes of the same colour can easily travel "
                    "the same distance as each other"},
            {"text": "No — a match in distance means nothing at all",
             "correct": False,
             "why": "A match is real evidence and a mismatch rules a "
                    "substance out. It simply is not proof on its own"},
            {"text": "No — it is good evidence, but other substances could "
                     "travel that far too",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e20",
        "band": "easier",
        "text": "What is a reference sample in chromatography?",
        "options": [
            {"text": "A sample whose identity is already known",
             "correct": True},
            {"text": "The sample somebody wants identifying",
             "correct": False,
             "why": "That is the unknown. A reference is the one you can "
                    "already put a name to"},
            {"text": "The solvent chosen for the run",
             "correct": False,
             "why": "The solvent is the liquid that does the carrying. It is "
                    "not a sample at all"},
            {"text": "A second run of the same unknown",
             "correct": False,
             "why": "Repeating the unknown gives nothing new to compare it "
                    "against, which is the whole point of a reference"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e21",
        "band": "easier",
        "text": "A student wants to run the colouring from a boiled sweet on "
                "chromatography paper. What has to be done to the sweet "
                "first?",
        "options": [
            {"text": "Grind it up and spread the powder along the baseline",
             "correct": False,
             "why": "A solid cannot travel up the paper. The colouring has "
                    "to be in solution before anything can carry it"},
            {"text": "Warm it until the colouring melts onto the paper",
             "correct": False,
             "why": "Melted colouring is still not dissolved, so it would "
                    "sit exactly where it was put"},
            {"text": "Dissolve its colouring in a few drops of water",
             "correct": True},
            {"text": "Press it against the paper until a mark is left",
             "correct": False,
             "why": "A smear of solid is not a solution, so the solvent has "
                    "nothing it can pick up and carry"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e22",
        "band": "easier",
        "text": "A felt-tip pen's dye does not move at all when water is used "
                "as the solvent. What should be tried next?",
        "options": [
            {"text": "Leaving the paper standing in the water for a good "
                     "deal longer than usual",
             "correct": False,
             "why": "A dye that will not dissolve in water has not started "
                    "dissolving in it an hour later either"},
            {"text": "Using a much bigger spot of the same ink",
             "correct": False,
             "why": "More of a dye that cannot dissolve is still a dye that "
                    "cannot dissolve"},
            {"text": "Drawing the baseline closer to the top of the paper, "
                     "to shorten the climb",
             "correct": False,
             "why": "Where the baseline sits has no bearing on whether a dye "
                    "will dissolve in the solvent"},
            {"text": "Running it again with a different solvent, such as "
                     "ethanol",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e23",
        "band": "easier",
        "text": "Which of these finished chromatograms is the most useful one to read?",
        "options": [
            {
             "text": "One with its spots spread well apart up the paper",
             "correct": True,
            },
            {
             "text": "One with all its spots bunched together near the top",
             "correct": False,
             "why": "Spots crowded into one band cannot be told apart, which defeats the point of separating them",
            },
            {
             "text": "One with all its spots still sitting on the baseline",
             "correct": False,
             "why": "Spots that have not moved have not been separated from one another at all",
            },
            {
             "text": "One with a single wide streak from baseline to front",
             "correct": False,
             "why": "A streak is the worst of the four: nothing in it can be counted or measured",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e24",
        "band": "easier",
        "text": "What is a locating agent used for in chromatography?",
        "options": [
            {"text": "Marking where the solvent front reached",
             "correct": False,
             "why": "The front is marked in pencil by hand as the paper "
                    "comes out, not by a chemical"},
            {"text": "Making colourless spots visible after the run",
             "correct": True},
            {"text": "Holding the spots on the baseline while the run starts",
             "correct": False,
             "why": "Nothing holds the spots down. They stay put only until "
                    "the climbing solvent reaches them"},
            {"text": "Dissolving a sample that will not dissolve in water",
             "correct": False,
             "why": "That job belongs to choosing a different solvent, not "
                    "to a spray used at the end of a run"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e25",
        "band": "easier",
        "text": "Two identical papers are spotted with the same ink. One is "
                "taken out after five minutes and one after ten. What is "
                "true of the spots on the second paper?",
        "options": [
            {"text": "They are in the same places as on the first paper",
             "correct": False,
             "why": "The solvent went on climbing for another five minutes, "
                    "and the spots went on climbing with it"},
            {"text": "They are darker than the spots on the first paper",
             "correct": False,
             "why": "Extra time adds no dye. The same amount was spotted "
                    "onto each of the two papers"},
            {"text": "They are further from the baseline than on the first",
             "correct": True},
            {"text": "They are closer together than on the first paper",
             "correct": False,
             "why": "As the front moves on, the fast spots pull away from "
                    "the slow ones rather than closing up on them"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e26",
        "band": "easier",
        "text": "After a chromatogram has been run, are the separated dyes "
                "still the same substances that were spotted on?",
        "options": [
            {"text": "No — each one has reacted with the paper it travelled "
                     "through",
             "correct": False,
             "why": "The paper holds a dye back but does not react with it. "
                    "The dye can be washed off again unchanged"},
            {"text": "No — the solvent has combined with each of them",
             "correct": False,
             "why": "The solvent dissolves a dye and carries it. The two do "
                    "not join up into anything new"},
            {"text": "Only the ones that reached the solvent front are "
                     "unchanged",
             "correct": False,
             "why": "How far a dye climbed makes no difference to what it "
                    "is. All of them come off the paper unchanged"},
            {"text": "Yes — separating a mixture makes no new substances",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e27",
        "band": "easier",
        "text": "Black ink is separated and gives a yellow spot, a magenta "
                "spot and a cyan spot. Why is there no black spot anywhere "
                "on the paper?",
        "options": [
            {"text": "Black was the colour of the three dyes mixed together, "
                     "not a dye of its own",
             "correct": True},
            {"text": "The black dye is the heaviest of them all, so it stayed "
                     "down on the baseline",
             "correct": False,
             "why": "Nothing here turns on weight, and there was no black "
                    "dye to be left behind in the first place"},
            {"text": "The black dye dissolved into the solvent in the tank "
                     "and was lost",
             "correct": False,
             "why": "The solvent in the tank never reaches the baseline, so "
                    "nothing can be lost into it"},
            {"text": "The black dye travelled past the solvent front and off "
                     "the paper",
             "correct": False,
             "why": "Nothing travels past the front. The front is as far as "
                    "any solvent, and so any dye, has got"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e28",
        "band": "easier",
        "text": "One ink gives two red spots at different heights on the "
                "paper. What does that tell you?",
        "options": [
            {"text": "One of the red spots came from the paper's own fibres",
             "correct": False,
             "why": "The paper contributes no colour of its own. Both spots "
                    "came out of the ink"},
            {"text": "The ink contains two different red substances",
             "correct": True},
            {"text": "The same red dye was spotted on twice by mistake",
             "correct": False,
             "why": "One dye travels one distance. Two heights means two "
                    "substances, however alike they look"},
            {"text": "The red dye split in half as it climbed the paper",
             "correct": False,
             "why": "The run splits nothing. It only moves apart substances "
                    "that were separate to begin with"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e29",
        "band": "easier",
        "text": "Three dyes from one ink finish at 2 cm, 5 cm and 8 cm above "
                "the baseline. Which one was held most strongly by the "
                "paper?",
        "options": [
            {"text": "The one at 8 cm",
             "correct": False,
             "why": "That dye got the furthest of the three, which means the "
                    "paper held it the least"},
            {"text": "The one at 5 cm",
             "correct": False,
             "why": "The middle dye was held more tightly than the fastest "
                    "one but less tightly than the slowest"},
            {"text": "The one at 2 cm",
             "correct": True},
            {"text": "All three equally, or they would not be in one ink",
             "correct": False,
             "why": "Dyes sharing an ink are still separate substances, and "
                    "each is held by its own amount"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e30",
        "band": "easier",
        "text": "Which two distances have to be measured on a finished "
                "chromatogram to work out a spot's ratio?",
        "options": [
            {"text": "The width of the spot and the width of the paper",
             "correct": False,
             "why": "Widths play no part in it. The ratio is built out of "
                    "how far things travelled up the paper"},
            {"text": "The height of the paper and the depth of solvent in "
                     "the tank",
             "correct": False,
             "why": "Neither of those is a distance anything travelled, and "
                    "neither is marked on the paper"},
            {"text": "The gap between two neighbouring spots and the total "
                     "length of the paper strip",
             "correct": False,
             "why": "The gap between spots is never used. Each spot's own "
                    "travel is what counts"},
            {"text": "The distance the spot travelled and the distance the "
                     "solvent travelled",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e31",
        "band": "easier",
        "text": "A student measures both distances in millimetres instead of "
                "centimetres. What happens to the ratio that comes out?",
        "options": [
            {"text": "It is exactly the same number",
             "correct": True},
            {"text": "It comes out ten times bigger",
             "correct": False,
             "why": "Both measurements grow by the same factor of ten, and "
                    "the division cancels that out"},
            {"text": "It comes out ten times smaller",
             "correct": False,
             "why": "Neither measurement shrinks, and dividing one by the "
                    "other removes the unit altogether"},
            {"text": "It cannot be worked out in millimetres",
             "correct": False,
             "why": "Any unit of length works, as long as the same one is "
                    "used for both of the distances"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-e32",
        "band": "easier",
        "text": "Why is the solvent front marked in pencil the moment the "
                "paper is lifted out of the tank?",
        "options": [
            {"text": "Because the front keeps on climbing for a while after "
                     "the paper is out",
             "correct": False,
             "why": "The front stops as soon as the paper leaves the "
                    "solvent. The trouble is that it then vanishes"},
            {"text": "Because the paper dries and the front can no longer be "
                     "seen",
             "correct": True},
            {"text": "Because the spots keep moving while the paper dries",
             "correct": False,
             "why": "The spots stop where they are. Drying does not shift "
                    "them any further up the paper"},
            {"text": "Because the pencil mark stops the solvent evaporating",
             "correct": False,
             "why": "A pencil line does nothing to the solvent. It only "
                    "records where the front had got to"},
        ],
        "figure": None,
    },
    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c3-06-s08",
        "band": "standard",
        "text": "A student lifts the paper out of the tank halfway through a "
                "run and stands it on the bench. What happens to the spots "
                "from that moment on?",
        "options": [
            {"text": "They carry on climbing, because the paper is already "
                     "wet",
             "correct": False,
             "why": "The paper is wet only as far as the front. Above that it "
                    "is dry, and a dye travels only in moving solvent"},
            {"text": "They stop moving, because no more solvent is soaking "
                     "past them",
             "correct": True},
            {"text": "They slide back towards the baseline as the paper "
                     "dries",
             "correct": False,
             "why": "Solvent dries where it is. It does not drain back down "
                    "the paper taking the dyes with it"},
            {"text": "They spread sideways and merge into one another",
             "correct": False,
             "why": "Sideways spreading comes from a spot that was too large "
                    "at the start, not from taking the paper out early"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s09",
        "band": "standard",
        "text": "Explain why a dye spot cannot move any further once the "
                "finished paper has dried out.",
        "options": [
            {"text": "The dye has stuck permanently to the paper fibres by "
                     "then",
             "correct": False,
             "why": "It is not stuck permanently. The spot can be cut out, "
                    "redissolved and run again"},
            {"text": "The dried dye is a solid now, and too heavy to climb",
             "correct": False,
             "why": "Weight is not what moves a dye up a paper. It travels "
                    "only because solvent carries it"},
            {"text": "There is no moving solvent left to dissolve it and "
                     "carry it",
             "correct": True},
            {"text": "The paper's fibres close up as they dry and block the "
                     "gaps",
             "correct": False,
             "why": "The gaps are still open. Wet the paper again and the "
                    "spot starts moving again"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s10",
        "band": "standard",
        "text": "The same dye is run again in the same solvent, this time on a paper that grips it more tightly than before. What happens to its spot?",
        "options": [
            {
             "text": "It finishes nearer the baseline than it did before",
             "correct": True,
            },
            {
             "text": "It finishes nearer the solvent front than before",
             "correct": False,
             "why": "Clinging to the paper harder loses the dye the contest, so it gets less far up rather than further",
            },
            {
             "text": "It finishes in exactly the same place as before",
             "correct": False,
             "why": "The distance is settled by the contest between paper and solvent, and one side of that contest has changed",
            },
            {
             "text": "It stays put but comes out a darker colour",
             "correct": False,
             "why": "Darkness comes from how much was spotted onto the baseline, and that has not been changed here",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s11",
        "band": "standard",
        "text": "The lid is left off the tank during a long run. What does "
                "that do to the run?",
        "options": [
            {"text": "The spots fade, because the open air bleaches the dyes "
                     "as they climb the paper",
             "correct": False,
             "why": "Air does not bleach these dyes, and nothing fades in "
                    "the few minutes a run takes"},
            {"text": "The tank cools, so nothing will dissolve any more",
             "correct": False,
             "why": "An open tank sits at room temperature, and the dyes "
                    "dissolve at room temperature perfectly well"},
            {"text": "Solvent evaporates off the paper, so the front climbs "
                     "slowly and unevenly",
             "correct": True},
            {"text": "The paper curls and the spots run back down it",
             "correct": False,
             "why": "The spots do not run backwards. Solvent dries where it "
                    "is rather than draining away downwards"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s12",
        "band": "standard",
        "text": "A finished paper's wet front is not level: it ends 2 cm further up the paper on the left-hand side than on the right. Suggest what caused that.",
        "options": [
            {
             "text": "The baseline was drawn higher on one side than the other",
             "correct": False,
             "why": "A sloping baseline would tilt the spots, but the wet front would still climb level across the paper",
            },
            {
             "text": "The spots were put on before the pencil line was drawn",
             "correct": False,
             "why": "The order of ruling and spotting makes no difference at all to how the solvent climbs",
            },
            {
             "text": "Too much sample was spotted onto one of the lanes",
             "correct": False,
             "why": "A heavy spot spreads sideways in its own lane. It does not tilt the front across the whole paper",
            },
            {
             "text": "The paper was resting against the side of the beaker",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s13",
        "band": "standard",
        "text": "A run works properly but every spot comes out faint and hard "
                "to see. What should be done differently next time?",
        "options": [
            {"text": "Put on one much larger drop of the sample instead",
             "correct": False,
             "why": "A larger drop makes a wide spot that spreads into its "
                    "neighbours, which is worse rather than better"},
            {"text": "Spot the sample on several times, drying in between",
             "correct": True},
            {"text": "Leave the paper in the tank for longer",
             "correct": False,
             "why": "Extra time moves the spots further up the paper. It "
                    "does not put any more dye into them"},
            {"text": "Use a more dilute solution of the same sample",
             "correct": False,
             "why": "Diluting it puts even less dye on the paper, so the "
                    "spots come out fainter still"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s14",
        "band": "standard",
        "text": "A student measures a spot's distance from the bottom edge of "
                "the paper rather than from the pencil baseline. Why is that "
                "reading wrong?",
        "options": [
            {"text": "The spot did not start there — it started at the "
                     "baseline",
             "correct": True},
            {"text": "The bottom edge was under the solvent, so it is wet",
             "correct": False,
             "why": "The trouble is not that the edge was wet. It is that "
                    "the spot never began its journey from there"},
            {"text": "The bottom edge is not straight enough to measure from",
             "correct": False,
             "why": "The cut edge is straight enough to measure from. It is "
                    "simply the wrong starting point"},
            {"text": "Distances are measured downwards from the solvent "
                     "front",
             "correct": False,
             "why": "They are measured upwards from the baseline, which is "
                    "where every substance on the paper started"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s15",
        "band": "standard",
        "text": "A student measures to the top edge of each spot instead of to its centre. What does that do to the ratio she works out for each spot?",
        "options": [
            {
             "text": "Every value comes out slightly too small",
             "correct": False,
             "why": "The top edge is further from the baseline than the centre is, so the reading is bigger, not smaller",
            },
            {
             "text": "The values are unchanged, as every spot is treated the same way",
             "correct": False,
             "why": "The solvent front is a line rather than a spot, so only one of the two distances is inflated",
            },
            {
             "text": "Every value comes out slightly too large",
             "correct": True,
            },
            {
             "text": "The values become impossible to compare with each other",
             "correct": False,
             "why": "They can still be compared with one another. It is comparison with anybody else's values that breaks",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s16",
        "band": "standard",
        "text": "Both distances were measured in centimetres. Explain why the "
                "ratio worked out from them carries no unit.",
        "options": [
            {"text": "A length divided by a length leaves a plain number",
             "correct": True},
            {"text": "Any value below 1 is a plain number and carries no unit",
             "correct": False,
             "why": "Plenty of quantities below 1 carry units, such as 0.5 "
                    "metres. It is the division that removes this one"},
            {"text": "The two distances were measured with the same ruler",
             "correct": False,
             "why": "Using one ruler is good practice, but it is dividing "
                    "one distance by the other that cancels the unit"},
            {"text": "The length of the paper itself was never measured",
             "correct": False,
             "why": "The paper's own length is no part of the calculation, "
                    "and leaving it out is not what removes the unit"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s17",
        "band": "standard",
        "text": "A student works out a dye's ratio of spot distance to solvent distance and gets 1.6. Which mistake would produce that?",
        "options": [
            {
             "text": "The solvent front was marked after the paper had dried",
             "correct": False,
             "why": "A front marked late is hard to place accurately, but it could not push the answer above 1",
            },
            {
             "text": "The spot was measured to its centre, not its top edge",
             "correct": False,
             "why": "The centre is the right place to measure to, and either choice still gives an answer below 1",
            },
            {
             "text": "The paper was left in the tank for far too long",
             "correct": False,
             "why": "Even a paper run right to the top has its spots below the front, so the answer stays under 1",
            },
            {
             "text": "The two distances were divided the wrong way round",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s18",
        "band": "standard",
        "text": "A student's ratio of spot distance to solvent distance for a dye is 0.38. A book gives 0.52 for that dye, measured in a different solvent. What does the disagreement show?",
        "options": [
            {
             "text": "That her substance is definitely not the one the book was describing at all",
             "correct": False,
             "why": "A different solvent moves every spot, so the two would be expected to disagree whatever the substance was",
            },
            {
             "text": "Nothing — different solvents were used, so the two cannot be compared",
             "correct": True,
            },
            {
             "text": "That her measurements must have been taken carelessly",
             "correct": False,
             "why": "Measuring more carefully would not bring the two together, because the runs were never comparable",
            },
            {
             "text": "That the value printed in the book must be wrong",
             "correct": False,
             "why": "The book's value is right for the solvent it was measured in. The comparison is what is at fault",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s19",
        "band": "standard",
        "text": "An unknown substance and a known one give spots at the same "
                "height. What would be the best way to test whether they "
                "really are the same substance?",
        "options": [
            {"text": "Run the unknown again in the same solvent and check it "
                     "repeats",
             "correct": False,
             "why": "Repeating the same run only shows the first was done "
                    "properly. It puts no new evidence on the table"},
            {"text": "Put a bigger spot of the unknown on and see if it goes "
                     "further",
             "correct": False,
             "why": "A bigger spot does not travel further, so this test "
                    "would show nothing either way"},
            {"text": "Run them side by side again in a different solvent",
             "correct": True},
            {"text": "Leave the paper in longer so the spots move further "
                     "apart",
             "correct": False,
             "why": "A longer run carries both spots on together and gives "
                    "no comparison that was not there already"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s20",
        "band": "standard",
        "text": "A sports drink's colouring is run beside pure samples of three permitted dyes. The drink gives one spot, level with the second dye and nowhere near the other two. What is the best conclusion?",
        "options": [
            {
             "text": "The drink contains all three of those dyes, in different amounts",
             "correct": False,
             "why": "The drink gave a single spot. Three dyes in it would have given three spots",
            },
            {
             "text": "The drink is definitely coloured with the second dye, and no further test is needed",
             "correct": False,
             "why": "One match is strong evidence, but two different substances can travel the same distance as each other",
            },
            {
             "text": "The drink contains a dye that is none of the three",
             "correct": False,
             "why": "Its spot finished level with the second dye, which is strong evidence that it is that dye rather than one outside the list.",
            },
            {
             "text": "The drink's colouring behaves like the second dye and may well be it",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s21",
        "band": "standard",
        "text": "Leaf pigments are ground up with a little ethanol before "
                "anything is spotted onto the paper. Explain why the "
                "grinding step is needed.",
        "options": [
            {"text": "Grinding breaks the pigments into smaller, faster ones",
             "correct": False,
             "why": "Grinding breaks open leaf cells, not pigment "
                    "substances. Each pigment stays exactly what it was"},
            {"text": "It gets the pigments into solution so they can be "
                     "carried",
             "correct": True},
            {"text": "The green would otherwise hide the other pigments",
             "correct": False,
             "why": "The pigments separate on the paper whatever colour the "
                    "extract happens to look like to start with"},
            {"text": "A whole leaf is too heavy to be lifted up the paper",
             "correct": False,
             "why": "Weight is not the obstacle. Once a pigment is dissolved "
                    "it is carried however heavy the leaf was"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s22",
        "band": "standard",
        "text": "A marker pen's ink stays on the baseline when water is the "
                "solvent, but separates into four spots when ethanol is used. "
                "Explain the difference.",
        "options": [
            {"text": "Ethanol is thinner, so it slips past the dyes more "
                     "easily",
             "correct": False,
             "why": "How runny a solvent is does not decide this. What "
                    "matters is whether the dyes dissolve in it at all"},
            {"text": "Ethanol evaporates faster and pulls the dyes up behind "
                     "it",
             "correct": False,
             "why": "Evaporating solvent is a nuisance rather than a lifting "
                    "force. The dyes move because they dissolve"},
            {"text": "The dyes dissolve in ethanol but hardly at all in "
                     "water",
             "correct": True},
            {"text": "Ethanol reacts with the dyes and makes soluble ones",
             "correct": False,
             "why": "No reaction takes place. The dyes that come off the "
                    "baseline are the dyes that went onto it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s23",
        "band": "standard",
        "text": "Every spot on a finished paper is bunched together just below the solvent front. What should be changed to get a better separation?",
        "options": [
            {
             "text": "Take the paper out sooner, before the spots bunch up",
             "correct": False,
             "why": "Stopping earlier shrinks every distance in the same proportion, so the spots end up closer together still",
            },
            {
             "text": "Spot less of the sample onto the baseline",
             "correct": False,
             "why": "The amount decides how dark a spot is, not where on the paper it finishes",
            },
            {
             "text": "Use a wider strip of paper and the same solvent",
             "correct": False,
             "why": "Width gives a spot more room sideways. Every spot still climbs the same fraction of the way to the front, so they finish just as bunched.",
            },
            {
             "text": "Try a solvent the dyes dissolve in less readily",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s24",
        "band": "standard",
        "text": "Amino acids are separated and the paper is sprayed with a "
                "locating agent afterwards. Why is it sprayed on at the end "
                "rather than mixed into the sample at the start?",
        "options": [
            {"text": "Mixed in at the start, it would stop the amino acids "
                     "dissolving in the solvent at all",
             "correct": False,
             "why": "It does not stop anything dissolving. The objection is "
                    "that it would travel up the paper as well"},
            {"text": "At the end it shows where each one stopped, without "
                     "changing how they travelled",
             "correct": True},
            {"text": "Mixed in first it would react with the paper instead",
             "correct": False,
             "why": "It reacts with the amino acids wherever they happen to "
                    "be, on the paper or off it"},
            {"text": "Sprayed at the start it would wash off into the tank",
             "correct": False,
             "why": "The solvent sits below the baseline, so nothing on the "
                    "paper is washed down into the tank"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s25",
        "band": "standard",
        "text": "The same ink is run twice in the same solvent, once for five "
                "minutes and once for twelve. Comparing the two papers, what "
                "is the same and what is different?",
        "options": [
            {"text": "Both the distances and the ratios come out the same",
             "correct": False,
             "why": "The longer run carried the spot and the front further "
                    "up, so the distances are not the same"},
            {"text": "The distances match but the ratios come out different",
             "correct": False,
             "why": "It is the other way round. Distances grow with time, "
                    "and the ratio is what survives that"},
            {"text": "Both the distances and the ratios come out different",
             "correct": False,
             "why": "The spot and the front grow together, so dividing one "
                    "by the other gives the same answer twice"},
            {"text": "The distances differ but the ratios come out the same",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s26",
        "band": "standard",
        "text": "A separated dye can be cut out of the paper, redissolved and "
                "used again. Explain why that is possible.",
        "options": [
            {"text": "Nothing was altered chemically — it is the same "
                     "substance it was",
             "correct": True},
            {"text": "The solvent dried out of it and left it pure",
             "correct": False,
             "why": "Drying removes solvent, but that is not why the dye "
                    "still works. It was never altered in the first place"},
            {"text": "The paper shielded it from the solvent as it travelled",
             "correct": False,
             "why": "The dye was dissolved in the solvent the whole way up, "
                    "and came through it completely unchanged"},
            {"text": "Only the strongest dyes survive being separated",
             "correct": False,
             "why": "Every dye on the paper comes through the run unchanged, "
                    "whether its spot is dark or faint"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s27",
        "band": "standard",
        "text": "A black ink separates into a yellow spot, a magenta spot and a cyan spot, and nothing black appears anywhere on the paper. A student says the ink must hold a black dye as well, which simply did not show up. Why is that wrong?",
        "options": [
            {
             "text": "A black dye would have been destroyed by the solvent",
             "correct": False,
             "why": "The solvent destroys nothing on its way up. It only dissolves substances and carries them",
            },
            {
             "text": "A black dye would have been left down on the baseline, out of sight",
             "correct": False,
             "why": "A spot sitting on the baseline is perfectly visible, and there was no spot there to see",
            },
            {
             "text": "Coloured dyes mixed together look black; no black dye is needed",
             "correct": True,
            },
            {
             "text": "Black dyes do exist, so the student is right after all",
             "correct": False,
             "why": "Black dyes do exist, but this ink had none: every spot the paper produced was a coloured one",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s28",
        "band": "standard",
        "text": "A blue ink and a green ink are run side by side. Each gives "
                "one spot, both exactly 4.5 cm above the baseline, and the "
                "two spots are different colours. What can you say?",
        "options": [
            {"text": "They hold the same dye, which changed colour in one of "
                     "the two lanes",
             "correct": False,
             "why": "A dye does not change colour on its way up the paper. "
                    "Its colour belongs to the substance itself"},
            {"text": "One of the two lanes must have been measured wrongly",
             "correct": False,
             "why": "Two spots really can finish level with each other. The "
                    "measurement is not what is at fault here"},
            {"text": "They hold different dyes that happen to travel the same "
                     "distance",
             "correct": True},
            {"text": "They hold the same dye, since distance decides identity",
             "correct": False,
             "why": "Distance is evidence, not identity. Two different "
                    "substances can travel exactly as far as each other"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s29",
        "band": "standard",
        "text": "Three dyes in one ink travel 1.5 cm, 4.0 cm and 7.5 cm on "
                "one paper. Put them in order of how readily the solvent "
                "dissolved them, least readily first.",
        "options": [
            {"text": "1.5 cm, then 4.0 cm, then 7.5 cm",
             "correct": True},
            {"text": "7.5 cm, then 4.0 cm, then 1.5 cm",
             "correct": False,
             "why": "The dye that got furthest is the one the solvent "
                    "dissolved best, so it belongs at the end of this order"},
            {"text": "4.0 cm, then 1.5 cm, then 7.5 cm",
             "correct": False,
             "why": "The middle dye is not the least willing of the three. "
                    "The order follows the distances straight through"},
            {"text": "They cannot be ordered without knowing the amounts",
             "correct": False,
             "why": "How much of each dye was spotted on has no bearing on "
                    "how far up the paper it travels"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s30",
        "band": "standard",
        "text": "A student measured how far a spot travelled and now wants "
                "its ratio. What else must be measured, and why?",
        "options": [
            {"text": "The width of the paper, so the ratio allows for its "
                     "size",
             "correct": False,
             "why": "The ratio has nothing to do with the paper's size. It "
                    "compares two distances travelled up it"},
            {"text": "How far the solvent went, because the ratio compares "
                     "the two",
             "correct": True},
            {"text": "Nothing else — the spot's distance is the ratio",
             "correct": False,
             "why": "A distance in centimetres is not a ratio. It becomes "
                    "one only when it is divided by the solvent's distance"},
            {"text": "The time the run took, because faster runs give more",
             "correct": False,
             "why": "Time is no part of this calculation. Only the two "
                    "distances go into it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s31",
        "band": "standard",
        "text": "A student measures a spot at 45 mm and the solvent front at 9.0 cm, divides one by the other and writes down 5. What has gone wrong?",
        "options": [
            {
             "text": "The spot was measured to the wrong part of itself",
             "correct": False,
             "why": "Measuring to the centre or to an edge shifts the answer a little; it could never turn it into 5",
            },
            {
             "text": "The solvent front was marked too low on the paper",
             "correct": False,
             "why": "A front marked slightly low changes the answer slightly. It does not multiply it by ten",
            },
            {
             "text": "The solvent front was measured to the top edge of the paper instead of to the pencil mark",
             "correct": False,
             "why": "Taking the front too high makes the number she divided by bigger, so the answer comes out smaller rather than ten times too big.",
            },
            {
             "text": "The two distances were in different units",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-s32",
        "band": "standard",
        "text": "A student forgets to mark the solvent front, and by the time "
                "she comes back the paper has dried. What can still be done "
                "with the chromatogram?",
        "options": [
            {"text": "The spots can still be compared, but no ratio can be "
                     "worked out",
             "correct": True},
            {"text": "Nothing at all — the whole chromatogram is now useless",
             "correct": False,
             "why": "The spots are still on the paper and can still be "
                    "compared against the other lanes of the same run"},
            {"text": "Everything, since the front always ends at the paper's "
                     "top edge",
             "correct": False,
             "why": "A good run is stopped short of the top edge, which is "
                    "exactly why the front has to be marked"},
            {"text": "The paper can go back in the tank until the front shows",
             "correct": False,
             "why": "A second run carries every spot further on, so the "
                    "chromatogram no longer shows what it first showed"},
        ],
        "figure": None,
    },
    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-06-h08",
        "band": "harder",
        "text": "Water climbs several centimetres up a strip of "
                "chromatography paper even though gravity pulls it down. "
                "Suggest how that is possible.",
        "options": [
            {"text": "Air pressing down on the liquid in the tank squeezes "
                     "the water up the strip",
             "correct": False,
             "why": "Air presses on the paper just as hard as on the tank, so "
                    "pressure alone would push the liquid down as readily"},
            {"text": "Water touching paper is warmed, and warm liquids rise",
             "correct": False,
             "why": "Nothing is heated here, and a cold tank behaves in "
                    "exactly the same way as a warm one"},
            {"text": "The fibres attract water strongly across very narrow "
                     "gaps, and lift it",
             "correct": True},
            {"text": "The dyes on the baseline draw the water up towards "
                     "them",
             "correct": False,
             "why": "A blank strip with nothing spotted on it climbs exactly "
                    "as far, so the dyes cannot be lifting anything"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h09",
        "band": "harder",
        "text": "A student writes that the paper carries the dyes upwards "
                "while the solvent holds them back. How much of that is "
                "right?",
        "options": [
            {"text": "All of it — that is the contest, in the right order",
             "correct": False,
             "why": "The two jobs have been swapped over. It is the paper "
                    "that holds a dye back and the solvent that carries it"},
            {"text": "Neither job is right: the solvent carries and the "
                     "paper holds back",
             "correct": True},
            {"text": "Half right: the paper carries them, but the solvent "
                     "does not hold them",
             "correct": False,
             "why": "The paper carries nothing at all. It is fixed in place, "
                    "and its only effect is to hold a dye back"},
            {"text": "None of it — a dye's own weight decides where it "
                     "stops",
             "correct": False,
             "why": "Weight has no say in it at all. Where a dye stops is "
                    "settled by the paper and the solvent between them"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h10",
        "band": "harder",
        "text": "In solvent X, dye P travels further than dye Q. In solvent "
                "Y, dye Q travels further than dye P. Which statement is "
                "right?",
        "options": [
            {"text": "How far a dye goes depends on the solvent as much as "
                     "on the dye",
             "correct": True},
            {"text": "One of the two runs must have had its lanes labelled "
                     "the wrong way round",
             "correct": False,
             "why": "Both results are perfectly possible. Changing the "
                    "solvent can genuinely reverse which dye leads"},
            {"text": "Dye P and dye Q must really be the same substance",
             "correct": False,
             "why": "One substance behaves the same way in both solvents, "
                    "which is precisely what these two did not do"},
            {"text": "Solvent Y is simply the faster of the two solvents",
             "correct": False,
             "why": "A faster solvent carries both dyes further. It does not "
                    "reverse which of the two is in front"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h11",
        "band": "harder",
        "text": "Two identical papers are run at once, one in a covered tank "
                "and one in an open one. The open tank's spots finish lower "
                "down. A student says that proves the two inks hold "
                "different dyes. Evaluate that.",
        "options": [
            {"text": "Correct — spots at different heights always mean "
                     "different dyes",
             "correct": False,
             "why": "That holds only when both runs were done under the same "
                    "conditions, and these two plainly were not"},
            {"text": "Correct, as long as both papers came out at the same "
                     "moment",
             "correct": False,
             "why": "Coming out together does not help. The open tank was "
                    "losing solvent to the air the whole time"},
            {"text": "Wrong — the open tank's front climbed further, not "
                     "less far",
             "correct": False,
             "why": "An open tank loses solvent to the air, so its front "
                    "climbs less far. That is why its spots sit lower"},
            {"text": "Wrong — the two runs were not comparable, so the "
                     "heights prove nothing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h12",
        "band": "harder",
        "text": "On a run where the paper touched the glass, the solvent "
                "front in one lane finished 1.5 cm lower than in the next "
                "lane. Why is a single ratio for the whole paper now unsafe?",
        "options": [
            {"text": "The spots have been carried sideways into the wrong "
                     "lanes",
             "correct": False,
             "why": "Lanes do not swap over. Each sample stays in the column "
                    "it was spotted onto"},
            {"text": "No ratio at all can be worked out once the front is "
                     "crooked",
             "correct": False,
             "why": "It can be worked out lane by lane. It is one shared "
                    "front distance for the whole paper that is unsafe"},
            {"text": "The dyes dissolved differently on the two sides of the "
                     "paper",
             "correct": False,
             "why": "The dyes are the same substances everywhere. What "
                    "differed is how far the solvent got in each lane"},
            {"text": "Each lane's spots must be measured against the front "
                     "in that lane",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h13",
        "band": "harder",
        "text": "A finished paper shows each lane as one long vertical streak "
                "rather than a set of round spots. Which explanation fits "
                "best?",
        "options": [
            {"text": "Far too much sample was put on, so each substance "
                     "smeared as it moved",
             "correct": True},
            {"text": "The paper was left in the tank until the solvent had "
                     "run off the top edge",
             "correct": False,
             "why": "Running off the top crushes the spots into a band at "
                    "the edge; it does not stretch a lane into a streak"},
            {"text": "The tank had no lid, so solvent evaporated as it "
                     "climbed",
             "correct": False,
             "why": "A missing lid makes the front slow and uneven. It does "
                    "not turn every spot into a streak"},
            {"text": "The baseline was ruled far too near the bottom edge of "
                     "the paper strip itself",
             "correct": False,
             "why": "A baseline too low lets the spots dip into the solvent, "
                    "which washes them away rather than streaking them"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h14",
        "band": "harder",
        "text": "A spot sits 9.0 cm above the bottom edge of the paper and the solvent front sits 12.0 cm above that same edge. The baseline was ruled 2.0 cm above the bottom edge. What is the correct ratio for that spot?",
        "options": [
            {
             "text": "0.75",
             "correct": False,
             "why": "This is 9.0 divided by 12.0 — both distances taken from the bottom edge instead of from the baseline",
            },
            {
             "text": "0.70",
             "correct": True,
            },
            {
             "text": "0.58",
             "correct": False,
             "why": "This is 7.0 divided by 12.0 — the spot corrected to the baseline but the front left uncorrected",
            },
            {
             "text": "0.90",
             "correct": False,
             "why": "This is 9.0 divided by 10.0 — the front corrected to the baseline but the spot left uncorrected",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h15",
        "band": "harder",
        "text": "Two students work out a dye's ratio of spot distance to solvent distance from the same chromatogram. One measures to the centre of the spot and gets 0.62; the other measures to its top edge and gets 0.68. Which value should be recorded?",
        "options": [
            {
             "text": "0.68, because the far edge shows how far the substance reached",
             "correct": False,
             "why": "The leading edge is the furthest few particles, not the substance as a whole, and it is not the agreed point",
            },
            {
             "text": "The mean of the two, 0.65, since both measured carefully",
             "correct": False,
             "why": "Averaging a correct method with an incorrect one does not rescue the incorrect one",
            },
            {
             "text": "Neither — two values this far apart mean the run must be repeated",
             "correct": False,
             "why": "The run itself is sound. The two differ only because one of the two measuring methods was wrong",
            },
            {
             "text": "0.62, because the centre of a spot is the agreed measuring point",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h16",
        "band": "harder",
        "text": "A student writes down a dye's ratio of spot distance to solvent distance as 0.62 cm. What is wrong with that, and what should it say?",
        "options": [
            {
             "text": "Nothing is wrong, as both distances were in centimetres",
             "correct": False,
             "why": "Dividing centimetres by centimetres leaves no centimetres behind in the answer",
            },
            {
             "text": "The unit should not be there at all: it should read 0.62",
             "correct": True,
            },
            {
             "text": "The unit should be centimetres squared, as two lengths were used",
             "correct": False,
             "why": "A squared unit comes from multiplying two lengths. Dividing them cancels the unit instead",
            },
            {
             "text": "It should read 62 cm, since it is a percentage of the run",
             "correct": False,
             "why": "It is a ratio between 0 and 1 rather than a percentage, and it still carries no unit",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h17",
        "band": "harder",
        "text": "A dye's ratio of spot distance to solvent distance is 0.95. What does that tell you about how its spot finished, and why is it awkward to work with?",
        "options": [
            {
             "text": "It finished almost down at the baseline, so the dye had hardly moved at all",
             "correct": False,
             "why": "A value near 1 means the spot travelled almost as far as the solvent, which puts it near the top",
            },
            {
             "text": "It travelled 0.95 cm, which is barely clear of the baseline",
             "correct": False,
             "why": "The result is a ratio and carries no unit. It is not a distance in centimetres",
            },
            {
             "text": "It is impossible, because a result has to be below 0.5",
             "correct": False,
             "why": "Any value between 0 and 1 can happen. Only a value greater than 1 is impossible.",
            },
            {
             "text": "It finished right up by the front, where fast dyes are hard to tell apart",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h18",
        "band": "harder",
        "text": "Two laboratories run the same substance in the same solvent "
                "and get 0.42 and 0.56. Both measured carefully. Suggest the "
                "most likely reason for the difference.",
        "options": [
            {"text": "They used different papers, which hold a substance "
                     "back by different amounts",
             "correct": True},
            {"text": "One left its paper in the tank longer than the other "
                     "did",
             "correct": False,
             "why": "Time is not what decides the result. A longer run "
                    "carries the spot and the front on together"},
            {"text": "One of the two laboratories spotted on far more of the "
                     "substance than the other",
             "correct": False,
             "why": "The amount decides how dark and how wide a spot is. It "
                    "has no effect on the result at all"},
            {"text": "One measured in millimetres and the other in "
                     "centimetres",
             "correct": False,
             "why": "The units cancel in the division, so both would arrive "
                    "at exactly the same number"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h19",
        "band": "harder",
        "text": "An unknown and a known dye finish level in one solvent, and "
                "level again in a second, quite different solvent. How strong "
                "is the evidence now?",
        "options": [
            {"text": "Proof — matching twice can only happen for one "
                     "substance",
             "correct": False,
             "why": "It is very strong evidence, but two substances matching "
                    "twice by chance has not been ruled out"},
            {"text": "Much stronger than one match, though still short of "
                     "proof",
             "correct": True},
            {"text": "No stronger, since the same two substances were used "
                     "again",
             "correct": False,
             "why": "The second solvent is a fresh test, and passing two "
                    "independent tests is worth more than passing one"},
            {"text": "Weaker, since two different solvents cannot be "
                     "compared",
             "correct": False,
             "why": "Each pair was run together in its own solvent, so each "
                    "of the two comparisons is fair in itself"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h20",
        "band": "harder",
        "text": "An unknown food colouring gives two spots. One finishes "
                "level with dye X, the other level with dye Z, and neither is "
                "level with dye Y. What is the best conclusion?",
        "options": [
            {"text": "It is dye X, and the other spot came out of the paper "
                     "itself",
             "correct": False,
             "why": "The paper adds nothing of its own. Both spots came out "
                    "of the colouring that was spotted on"},
            {"text": "It is one dye that split into two on its way up the "
                     "paper",
             "correct": False,
             "why": "A run splits nothing. Two spots means two substances "
                    "were in the sample to begin with"},
            {"text": "It is probably a mixture behaving like X and Z, and "
                     "holds no Y",
             "correct": True},
            {"text": "It holds X, Y and Z, but the Y was too faint to show "
                     "up",
             "correct": False,
             "why": "Nothing appeared at Y's height, and a spot too faint to "
                    "see cannot be offered as evidence that it is there"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h21",
        "band": "harder",
        "text": "A mixture holds two dyes: one dissolves in water only, the "
                "other in ethanol only. A run in water gives one spot. What "
                "has become of the second dye?",
        "options": [
            {"text": "It was carried off the paper into the water in the "
                     "tank",
             "correct": False,
             "why": "The solvent in the tank never reaches the baseline, so "
                    "nothing on the paper can be lost into it"},
            {"text": "It went to the very top of the paper, as water could "
                     "not hold it back",
             "correct": False,
             "why": "A dye water cannot dissolve is a dye water cannot "
                    "carry. It does not race ahead of the others"},
            {"text": "It joined onto the first dye, and the two of them came "
                     "up as a single spot",
             "correct": False,
             "why": "Two substances do not merge into one. Each keeps its "
                    "own contest with the paper"},
            {"text": "It stayed on the baseline, because water could not "
                     "dissolve it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h22",
        "band": "harder",
        "text": "Two dyes in one ink both dissolve very well in ethanol. "
                "Explain why running the ink in ethanol might still fail to "
                "separate them.",
        "options": [
            {"text": "If ethanol carries both equally well they finish level "
                     "and look like one spot",
             "correct": True},
            {"text": "Because ethanol dissolves the paper as well as the two "
                     "dyes",
             "correct": False,
             "why": "Ethanol does not dissolve chromatography paper, which "
                    "is why it can be used as a solvent at all"},
            {"text": "Because two dyes that both dissolve well can never be "
                     "separated",
             "correct": False,
             "why": "They can be, in a solvent that suits one better than "
                    "the other. It is this solvent that fails, not the "
                    "method"},
            {"text": "Because the ethanol evaporates away before it can "
                     "carry either of them very far",
             "correct": False,
             "why": "With the lid on the tank, the solvent climbs the paper "
                    "perfectly well before any of it evaporates"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h23",
        "band": "harder",
        "text": "One ink is run in three solvents. In A all four spots stay "
                "on the baseline; in B they are spread from 2 cm to 8 cm; in "
                "C all four sit within half a centimetre of the front. Which "
                "solvent should be used?",
        "options": [
            {"text": "A, because spots that stay put are the easiest to "
                     "measure",
             "correct": False,
             "why": "Spots that have not moved have not been separated, so "
                    "there is nothing worth measuring"},
            {"text": "C, because the dyes travelled furthest and so "
                     "separated most",
             "correct": False,
             "why": "All four travelled about as far as each other, so they "
                    "finished crowded together rather than separated"},
            {"text": "B, because its spots are spread out and can be told "
                     "apart",
             "correct": True},
            {"text": "Any of the three, since the same four dyes are there "
                     "in each",
             "correct": False,
             "why": "The same dyes are present in all three, but only one of "
                    "the runs lets you tell them apart"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h24",
        "band": "harder",
        "text": "After spraying, a paper that had looked blank shows three "
                "spots. A student says the spray must have made three new "
                "substances. Evaluate that.",
        "options": [
            {"text": "Wrong — the three were there all along, and the spray "
                     "only made them visible",
             "correct": True},
            {"text": "Right — the spray reacted with the paper and made "
                     "three marks",
             "correct": False,
             "why": "The paper is the same all the way up. Marks appear only "
                    "where a substance from the sample stopped"},
            {"text": "Right, because colourless substances cannot be "
                     "separated at all",
             "correct": False,
             "why": "Colourless substances separate exactly as coloured ones "
                    "do. Only the seeing of them is harder"},
            {"text": "Wrong — the spray removed three coloured substances "
                     "and left gaps",
             "correct": False,
             "why": "What appeared were marks, not gaps, and nothing was "
                    "taken off the paper by the spray"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h25",
        "band": "harder",
        "text": "In one run a spot travels 3.0 cm and the solvent 6.0 cm. In "
                "a second run of the same ink in the same solvent, stopped "
                "later, the spot travels 5.0 cm and the solvent 10.0 cm. What "
                "do the two runs show?",
        "options": [
            {"text": "Two different dyes, since the spots travelled "
                     "different distances",
             "correct": False,
             "why": "The two results work out the same, which is exactly "
                    "what one dye run twice looks like"},
            {"text": "One dye that travels faster the longer it is left in "
                     "the tank",
             "correct": False,
             "why": "The dye is carried at its own rate throughout. The "
                    "extra distance came from the extra time, as did the "
                    "front's"},
            {"text": "Nothing, since runs stopped at different times cannot "
                     "be compared",
             "correct": False,
             "why": "This is what dividing by the front's distance is for. "
                    "Stopping at different moments does not change it"},
            {"text": "One dye, because both runs work out to the same 0.50",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h26",
        "band": "harder",
        "text": "A student writes that chromatography is a chemical change, "
                "because black ink turns into three different colours. "
                "Evaluate that.",
        "options": [
            {"text": "Right — three substances came out where one went in",
             "correct": False,
             "why": "Three substances went in. Black was only what they "
                    "looked like while they were mixed together"},
            {"text": "Right, because a solvent was needed to bring the "
                     "change about",
             "correct": False,
             "why": "The solvent carries substances about. Needing one does "
                    "not make a process a chemical change"},
            {"text": "Wrong — no new substance is made, so it is a physical "
                     "separation",
             "correct": True},
            {"text": "Wrong — it is a chemical change, but a very slow one",
             "correct": False,
             "why": "Speed does not come into it. No new substance is made "
                    "at any rate at all"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h27",
        "band": "harder",
        "text": "A green ink is run and gives one blue spot and one yellow "
                "spot, with nothing green anywhere on the paper. What does "
                "that show about the ink?",
        "options": [
            {"text": "Its green dye broke down into a blue one and a yellow "
                     "one",
             "correct": False,
             "why": "The run breaks nothing down. The blue and the yellow "
                    "were separate substances in the ink already"},
            {"text": "It holds three dyes, and the green has not left the "
                     "baseline",
             "correct": False,
             "why": "There is no green spot anywhere on the paper, on the "
                    "baseline or above it"},
            {"text": "The paper turned its green dye into two different "
                     "colours",
             "correct": False,
             "why": "The paper changes nothing. Its only effect is to hold "
                    "different substances back by different amounts"},
            {"text": "Its green was a blue dye and a yellow dye seen "
                     "together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h28",
        "band": "harder",
        "text": "Run on one paper at the same time, ink 1 gives spots at "
                "3 cm and 6 cm, and ink 2 gives spots at 6 cm and 9 cm. What "
                "is the most that can be said?",
        "options": [
            {"text": "They are the same ink, since both have a spot at 6 cm",
             "correct": False,
             "why": "Each ink has a spot the other one lacks, so they cannot "
                    "be the same mixture"},
            {"text": "They have nothing whatever in common",
             "correct": False,
             "why": "Both produced a spot at 6 cm, which is real evidence of "
                    "a substance they share"},
            {"text": "They may share the 6 cm substance, but each holds one "
                     "the other lacks",
             "correct": True},
            {"text": "Ink 2 is the stronger of the two, since both of its "
                     "spots travelled further",
             "correct": False,
             "why": "How far a spot travels says nothing about how "
                    "concentrated the ink it came from was"},
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h29",
        "band": "harder",
        "text": "Dye A travels 4.0 cm on a paper whose solvent travelled 8.0 cm. Dye B travels 6.0 cm on a second run, in the same solvent and on the same type of paper, whose solvent travelled 15.0 cm. Which dye is held more strongly by the paper?",
        "options": [
            {
             "text": "Dye A, because 0.50 is the larger of the two results",
             "correct": False,
             "why": "A larger result means the dye went further for the solvent it had, so the paper held it less tightly",
            },
            {
             "text": "Dye B, because its result of 0.40 is the smaller",
             "correct": True,
            },
            {
             "text": "Dye A, because it travelled the shorter distance in centimetres",
             "correct": False,
             "why": "Centimetres cannot be compared across two runs whose solvents travelled different distances",
            },
            {
             "text": "Neither — two separate papers cannot be compared at all",
             "correct": False,
             "why": "Dividing by the front's distance exists precisely so that two such runs can be compared",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h30",
        "band": "harder",
        "text": "A spot finished 3.0 cm above the pencil baseline. Dividing that height by the solvent front's climb gives 0.25. How far had the front climbed?",
        "options": [
            {
             "text": "0.75 cm",
             "correct": False,
             "why": "This multiplies 3.0 by 0.25. The spot's distance has to be divided by the result, not multiplied by it",
            },
            {
             "text": "3.25 cm",
             "correct": False,
             "why": "This adds the two numbers together. The result is a ratio, not something that can be added on",
            },
            {
             "text": "12.0 cm",
             "correct": True,
            },
            {
             "text": "4.0 cm",
             "correct": False,
             "why": "This divides 3.0 by 0.75, treating the ratio as the share of the paper left above the spot rather than the share of the front's travel that the spot made.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h31",
        "band": "harder",
        "text": "A spot travels 36 mm and the solvent front travels 8.0 cm. What is the ratio of spot distance to solvent distance, to two decimal places?",
        "options": [
            {
             "text": "0.45",
             "correct": True,
            },
            {
             "text": "4.50",
             "correct": False,
             "why": "This divides 36 by 8.0 without converting first, so the answer comes out ten times too big",
            },
            {
             "text": "0.22",
             "correct": False,
             "why": "This divides 8.0 by 36, which is both the wrong way round and in unconverted units",
            },
            {
             "text": "2.22",
             "correct": False,
             "why": "This divides 8.0 cm by 3.6 cm — the conversion done, but the division the wrong way round",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-06-h32",
        "band": "harder",
        "text": "A student who forgot to mark the solvent front suggests "
                "measuring to the top edge of the paper instead, saying it "
                "will be nearly right. Evaluate that suggestion.",
        "options": [
            {"text": "Sound — the front always stops a millimetre or two "
                     "below the top",
             "correct": False,
             "why": "The paper is taken out well before the front nears the "
                    "top, so the gap can easily be centimetres"},
            {"text": "Unsound — the front stopped short, so every result "
                     "comes out too small",
             "correct": True},
            {"text": "Unsound — every result would come out too large "
                     "instead",
             "correct": False,
             "why": "Dividing by a distance larger than the true one makes "
                    "the answer smaller, not larger"},
            {"text": "Sound, so long as every spot on the paper is measured "
                     "in exactly the same way",
             "correct": False,
             "why": "Treating them alike keeps them comparable with one "
                    "another, but leaves every one of the results wrong"},
        ],
        "figure": None,
    },
]
