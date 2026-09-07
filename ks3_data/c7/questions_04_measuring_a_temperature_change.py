"""C7 lesson 04 — Measuring a temperature change: twelve questions (MRB-272).

The lesson's argument is one shape: an energy change is measured as a
temperature change, and a temperature change is only as good as the apparatus
around it. The page teaches it by ruling on somebody else's plan and then
building eight rigs, none of which reaches the true value, so these twelve
probe the angles the mastery ladder leaves alone: which two readings are
needed, why the peak is the one to take, and what repeating an experiment can
and cannot fix.

The distractors are built from the lesson's two declared misconceptions.

`ENER-07` (repeating an experiment and averaging makes the result accurate)
drives the wrong options in e04, s02, h01 and h04. Each treats more data as a
cure for any error at all. h04 is the one that matters: it offers a group five
more repeats and asks what that would buy them, where the honest answer is
nothing.

`ENER-08` (results that agree closely with each other must be correct) drives
e03, s03 and h02, where precision is read as accuracy. h02 puts a set of five
readings that agree to a tenth of a degree in front of a student and asks
whether that settles anything.

A third strand, on the page and in neither register entry, is that the FINAL
temperature is the one to record. e01, e02 and s01 are built on it: the peak
arrives within seconds and everything after it is a measure of how long you
were away.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each and C7's four banks hold
twelve of each — level across the four indices by construction rather than by
a rebalancing pass.

Every question here is new prose, and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape, at the correct answer's own
length, and each is a mistake a real student actually makes.
"""

UNIT = "C7"
LESSON = "measuring-a-temperature-change"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c7-04-e01",
        "band": "easier",
        "text": "Which two readings do you need in order to find the "
                "temperature change of a reaction?",
        "options": [
            {"text": "The starting temperature of the solution and the "
                     "highest temperature it reaches", "correct": True},
            {"text": "The temperature of the room and the temperature of the "
                     "mixture at the end", "correct": False,
             "why": "The room may not be at the same temperature as your "
                    "solution. Measure the solution itself before you start."},
            {"text": "The temperature at the start and the temperature ten "
                     "minutes afterwards", "correct": False,
             "why": "Ten minutes later the mixture has cooled back towards "
                    "the room. You need the peak."},
            {"text": "The highest temperature reached and the temperature of "
                     "the alkali you added", "correct": False,
             "why": "What you subtract from is the mixture's own starting "
                    "temperature, not one reactant's."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e02",
        "band": "easier",
        "text": "Why should the highest reading be recorded rather than the "
                "reading after five minutes?",
        "options": [
            {"text": "Because a thermometer becomes less accurate the longer "
                     "it is left in a liquid", "correct": False,
             "why": "A thermometer does not drift like that. What changes in "
                    "five minutes is the mixture, not the instrument."},
            {"text": "Because the peak is the closest the apparatus gets to "
                     "the true value, and heat loss wins after it",
             "correct": True},
            {"text": "Because the reaction is still going after five minutes "
                     "and the number is not final", "correct": False,
             "why": "The reaction has usually finished within seconds. What "
                    "happens in the next five minutes is cooling."},
            {"text": "Because the highest reading is easier to read off a "
                     "scale than a falling one", "correct": False,
             "why": "Both are equally readable. The peak is chosen because it "
                    "is the least spoiled by heat loss."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e03",
        "band": "easier",
        "text": "A group repeats a reaction five times and gets +6.7, +6.8, "
                "+6.8, +6.7 and +6.8 °C. What can they say?",
        "options": [
            {"text": "The result is correct, because five readings agree that "
                     "closely", "correct": False,
             "why": "Close agreement is precision, not accuracy. Five "
                    "readings can agree and all be wrong in the same way."},
            {"text": "The result must be wrong, because real measurements "
                     "always scatter more than that", "correct": False,
             "why": "Tight agreement is a good sign about the method. It is "
                    "just not a guarantee about the value."},
            {"text": "Their readings are precise, but that does not tell them "
                     "whether they are accurate", "correct": True},
            {"text": "Nothing at all, because five readings is too small a "
                     "sample to say anything", "correct": False,
             "why": "Five readings say plenty about how repeatable the method "
                    "is. What they cannot say is whether it is right."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e04",
        "band": "easier",
        "text": "Why is a polystyrene cup better than a glass beaker for this "
                "experiment?",
        "options": [
            {"text": "Because polystyrene reacts less with acids than glass "
                     "does", "correct": False,
             "why": "Glass is famously unreactive with dilute acids. That is "
                    "not the problem with it here."},
            {"text": "Because a cup is smaller, so the same energy warms it "
                     "more", "correct": False,
             "why": "The volume of solution is kept the same either way. The "
                    "difference is in the container itself."},
            {"text": "Because the cup can be thrown away, so there is less "
                     "washing up between runs", "correct": False,
             "why": "Convenience is not a measurement argument, and the "
                    "readings really do differ."},
            {"text": "Because it insulates better and absorbs less of the "
                     "energy warming itself up", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c7-04-s01",
        "band": "standard",
        "text": "Four groups run the same neutralisation and report +5, +7, "
                "+2 and +7 °C. Nobody made anything up. What is the most "
                "likely explanation?",
        "options": [
            {"text": "The reaction released different amounts of energy in "
                     "different beakers", "correct": False,
             "why": "The same reaction with the same amounts releases the "
                    "same energy. The reaction is not the variable."},
            {"text": "The groups lost different amounts of heat before they "
                     "read their thermometers", "correct": True},
            {"text": "Some groups must have used more concentrated acid than "
                     "the others", "correct": False,
             "why": "The question says same acid, same alkali, same volumes. "
                    "What differed was the measuring, not the chemistry."},
            {"text": "School thermometers are unreliable and disagree with "
                     "each other by several degrees", "correct": False,
             "why": "Thermometers are not that bad, and the +2 group's rig "
                    "explains their reading without blaming the instrument."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s02",
        "band": "standard",
        "text": "A group's rig loses heat, so every reading is too low. They "
                "repeat the experiment ten times and take the mean. What does "
                "that achieve?",
        "options": [
            {"text": "It removes the heat loss, because errors cancel out "
                     "over enough repeats", "correct": False,
             "why": "Only errors that fall on BOTH sides of the truth cancel. "
                    "Heat loss falls on one side every time."},
            {"text": "It makes no difference at all, so repeating is a waste "
                     "of time", "correct": False,
             "why": "Repeating genuinely reduces random scatter and shows how "
                    "repeatable the method is. It just cannot fix this."},
            {"text": "It reduces the scatter between their readings, but the "
                     "mean is still too low", "correct": True},
            {"text": "It doubles the accuracy, because ten readings are worth "
                     "twice as much as five", "correct": False,
             "why": "Accuracy is about closeness to the true value, and no "
                    "number of repeats moves a result that is always low."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s03",
        "band": "standard",
        "text": "Which of these is a SYSTEMATIC error in this experiment?",
        "options": [
            {"text": "Misreading the scale by a tenth of a degree, sometimes "
                     "high and sometimes low", "correct": False,
             "why": "That is a random error. It falls on both sides of the "
                    "truth and averaging reduces it."},
            {"text": "Stirring slightly harder on some runs than on others",
             "correct": False,
             "why": "Also random. It changes the reading a little in either "
                    "direction from run to run."},
            {"text": "Spilling a little of the alkali on one of the five "
                     "runs", "correct": False,
             "why": "That is a mistake affecting one run, which is why it "
                    "would show up as an anomalous result you could "
                    "identify."},
            {"text": "Heat escaping from an uninsulated beaker on every "
                     "single run", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s04",
        "band": "standard",
        "text": "A student fits a lid to the cup but leaves a small hole in "
                "it for the thermometer. Why not seal it completely?",
        "options": [
            {"text": "Because a sealed cup could build up pressure and the "
                     "thermometer has to go through somewhere",
             "correct": True},
            {"text": "Because a completely sealed cup would stop the reaction "
                     "happening at all", "correct": False,
             "why": "The reaction does not need air. Sealing it would not "
                    "stop the chemistry."},
            {"text": "Because the hole lets excess heat out and stops the "
                     "reading going too high", "correct": False,
             "why": "The whole point of the lid is to keep heat IN. The hole "
                    "is a cost of the method, not a feature."},
            {"text": "Because a sealed lid would make the reading too "
                     "accurate to compare with other groups", "correct": False,
             "why": "There is no such thing as too accurate, and no group is "
                    "trying to match anybody else's error."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c7-04-h01",
        "band": "harder",
        "text": "Two students compare methods. A uses a glass beaker and "
                "reads at the peak; B uses an insulated cup and reads two "
                "minutes later. Both get about +5 °C. What does that show?",
        "options": [
            {"text": "That the two methods are equally good, since they agree "
                     "with each other", "correct": False,
             "why": "Two methods with different faults can land on the same "
                    "wrong number. Agreement between them proves nothing."},
            {"text": "That the true value must be +5 °C, because two "
                     "different rigs found it", "correct": False,
             "why": "Both rigs lose heat, so both read low. Agreeing on a low "
                    "number does not make it the true one."},
            {"text": "That good apparatus and prompt reading are both needed, "
                     "and each one alone leaves a similar shortfall",
             "correct": True},
            {"text": "That the container makes no difference, since only the "
                     "timing changed the result", "correct": False,
             "why": "Both things changed between the two methods. Nothing "
                    "here isolates the container."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h02",
        "band": "harder",
        "text": "The best rig a school bench can build reads +6.8 °C when the "
                "true value is +7.0 °C. Where did the missing 0.2 °C go?",
        "options": [
            {"text": "Into a rounding error, because thermometers cannot read "
                     "to a tenth of a degree", "correct": False,
             "why": "A digital probe reads to a hundredth. The shortfall is "
                    "real energy, not a rounding artefact."},
            {"text": "Nowhere — it was never released, because the reaction "
                     "did not quite finish", "correct": False,
             "why": "The reaction finishes. What happens to the energy after "
                    "it is released is the question."},
            {"text": "Into the air, which is why the lid was fitted in the "
                     "first place", "correct": False,
             "why": "The lid has already stopped most of that. What is left "
                    "is the apparatus itself absorbing energy."},
            {"text": "Into warming the cup, the lid and the thermometer "
                     "themselves", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h03",
        "band": "harder",
        "text": "A class compares three fuels by heating a beaker of water "
                "with each in turn. Every value they get is far below the "
                "published figure. Is the comparison worthless?",
        "options": [
            {"text": "No, because the same loss applies to all three, so the "
                     "ranking between the fuels still holds", "correct": True},
            {"text": "Yes, because values that far from the published ones "
                     "cannot support any conclusion", "correct": False,
             "why": "They can support a comparison. Being wrong by a similar "
                    "amount each time is exactly what leaves the ranking "
                    "usable."},
            {"text": "Yes, unless they repeat it enough times for the mean to "
                     "approach the published figure", "correct": False,
             "why": "The mean will never approach it. Every reading is low "
                    "for the same reason, so the mean is low too."},
            {"text": "No, because the published figures are themselves only "
                     "estimates and no better than the class's",
             "correct": False,
             "why": "Published figures come from a bomb calorimeter and are "
                    "far better. The reason the comparison survives is that "
                    "the error is shared."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h04",
        "band": "harder",
        "text": "A group with a leaking rig asks whether five more repeats or "
                "a lid would improve their result more. What should you tell "
                "them?",
        "options": [
            {"text": "The repeats, because more data always improves a "
                     "measurement", "correct": False,
             "why": "More data improves precision. It does nothing to an "
                    "error that runs the same way every time."},
            {"text": "The lid, because it attacks the error that is actually "
                     "making every reading wrong", "correct": True},
            {"text": "Neither, because the true value cannot be reached with "
                     "school apparatus anyway", "correct": False,
             "why": "It cannot be reached exactly — but a lid gets them from "
                    "well below it to close to it, which is worth having."},
            {"text": "Both equally, since one reduces scatter and the other "
                     "reduces loss by the same amount", "correct": False,
             "why": "They are not equal here. The scatter is already small "
                    "and the loss is large."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-04-e05",
        "band": "easier",
        "text": "What is insulation?",
        "options": [
            {"text": "Material that stops heat escaping altogether, so that "
                     "an insulated cup loses none of the energy the reaction "
                     "inside it releases",
             "correct": False,
             "why": "Nothing stops it altogether. Even the best school rig "
                    "still reads low"},
            {"text": "Material that keeps electricity in a wire",
             "correct": False,
             "why": "The word is used that way too. Here it is about heat"},
            {"text": "The lid on top of the cup",
             "correct": False,
             "why": "A lid helps, and insulation is what the cup itself is "
                    "made of"},
            {"text": "Material that slows heat escaping",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e06",
        "band": "easier",
        "text": "What is a systematic error?",
        "options": [
            {"text": "An error that pushes every reading the same way",
             "correct": True},
            {"text": "An error made by following the method incorrectly, so "
                     "that the whole experiment has to be set up again from "
                     "the beginning",
             "correct": False,
             "why": "That is a mistake. A systematic error can happen in a "
                    "perfectly followed method"},
            {"text": "An error that scatters readings either side of the "
                     "truth",
             "correct": False,
             "why": "That is a random error, and it is the kind averaging "
                    "reduces"},
            {"text": "An error in the arithmetic",
             "correct": False,
             "why": "That is a mistake in the calculation rather than in the "
                    "measurement"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e07",
        "band": "easier",
        "text": "What is a random error?",
        "options": [
            {"text": "An error that happens without any cause at all, which "
                     "is why nothing can be done to reduce one however the "
                     "apparatus is improved",
             "correct": False,
             "why": "Random errors have causes — reading a scale slightly "
                    "differently each time. Averaging reduces them"},
            {"text": "An error that scatters readings on both sides of the "
                     "true value",
             "correct": True},
            {"text": "An error that makes every reading too low",
             "correct": False,
             "why": "That is systematic, and heat loss is the example in this "
                    "lesson"},
            {"text": "An error made by a careless student",
             "correct": False,
             "why": "Careful workers get random errors too. It is about the "
                    "measurement, not the person"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e08",
        "band": "easier",
        "text": "What is the peak temperature?",
        "options": [
            {"text": "The highest temperature the reaction is capable of "
                     "producing, which is worked out afterwards rather than "
                     "read off the thermometer during the run",
             "correct": False,
             "why": "It is a reading you take at the time. Nothing is worked "
                    "out"},
            {"text": "The reading five minutes after mixing",
             "correct": False,
             "why": "By then heat loss has been winning for some time and the "
                    "number has fallen"},
            {"text": "The highest reading the thermometer reaches",
             "correct": True},
            {"text": "The temperature of the room",
             "correct": False,
             "why": "The room is a separate thing, and it is not what the "
                    "peak measures"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e09",
        "band": "easier",
        "text": "What is meant by the true value?",
        "options": [
            {"text": "The mean of all the readings a group takes, which is "
                     "the closest anybody can get to a value with real "
                     "apparatus and is therefore treated as the true one",
             "correct": False,
             "why": "A mean can be wrong in the same direction every time. "
                    "The true value is what a perfect measurement would "
                    "give"},
            {"text": "The reading the teacher gets",
             "correct": False,
             "why": "A teacher's apparatus loses heat too"},
            {"text": "The largest reading anyone obtained",
             "correct": False,
             "why": "In this experiment the largest is likely to be the "
                    "closest, and that is not what the phrase means"},
            {"text": "The value a perfect measurement would give",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e10",
        "band": "easier",
        "text": "Why does polystyrene foam insulate so well?",
        "options": [
            {"text": "Because it is mostly trapped air, and air is a poor "
                     "conductor",
             "correct": True},
            {"text": "Because the plastic it is made of conducts heat "
                     "extremely badly, far worse than any other material a "
                     "school laboratory has on the shelf",
             "correct": False,
             "why": "Solid polystyrene is a fair insulator and nothing "
                    "special. It is the trapped air that does the work"},
            {"text": "Because it is white, so it reflects heat",
             "correct": False,
             "why": "Colour matters a little for radiation. The trapped air "
                    "is the reason"},
            {"text": "Because it is light",
             "correct": False,
             "why": "It is light BECAUSE it is mostly air. The air is the "
                    "insulator"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e11",
        "band": "easier",
        "text": "How is the temperature change worked out?",
        "options": [
            {"text": "The highest temperature reached, minus the temperature "
                     "of the room",
             "correct": False,
             "why": "The room may not be at the same temperature as the "
                    "solution. You measure the solution before you start"},
            {"text": "The highest or lowest temperature reached, minus the "
                     "starting temperature",
             "correct": True},
            {"text": "The highest temperature reached",
             "correct": False,
             "why": "One reading on its own says nothing. A change is a "
                    "difference"},
            {"text": "The mean of all the readings taken during the run",
             "correct": False,
             "why": "The mean would include readings from before the reaction "
                    "and after it had cooled"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e12",
        "band": "easier",
        "text": "Which way does heat loss push the measured temperature "
                "change?",
        "options": [
            {"text": "It makes it too large",
             "correct": False,
             "why": "Losing heat means the peak is lower than it should be, "
                    "so the change comes out smaller"},
            {"text": "It scatters it either side of the true value, so that "
                     "some runs come out too high and some too low",
             "correct": False,
             "why": "That would be a random error. Heat loss only ever runs "
                    "one way"},
            {"text": "It makes it too small",
             "correct": True},
            {"text": "It has no effect if the cup is insulated",
             "correct": False,
             "why": "Insulation reduces it and never removes it. Even the "
                    "best rig reads low"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c7-04-s05",
        "band": "standard",
        "text": "A group mixes the solutions, writes up their method, and "
                "then reads the thermometer five minutes later. What has that "
                "cost them?",
        "options": [
            {"text": "Nothing, provided they record what they see, since the "
                     "reading five minutes on is a perfectly honest "
                     "measurement of the temperature at that moment",
             "correct": False,
             "why": "It is honest and it is not the quantity wanted. The peak "
                    "has been and gone"},
            {"text": "The starting temperature",
             "correct": False,
             "why": "That was taken before mixing and is unaffected by the "
                    "delay"},
            {"text": "Nothing much, because the reaction is still going",
             "correct": False,
             "why": "A neutralisation finishes in seconds. Five minutes later "
                    "only cooling is happening"},
            {"text": "The peak — the mixture has been cooling towards room "
                     "temperature since it passed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s06",
        "band": "standard",
        "text": "Why is the STARTING temperature of the solution measured, "
                "rather than the temperature of the room?",
        "options": [
            {"text": "Because the solution may not be at room temperature "
                     "when you start",
             "correct": True},
            {"text": "Because a thermometer in a solution is more accurate "
                     "than one in air, and a reading taken in air can be out "
                     "by several degrees either way",
             "correct": False,
             "why": "The thermometer works fine in air. The problem is that "
                    "the solution may not be at room temperature"},
            {"text": "Because the room's temperature changes during the "
                     "lesson",
             "correct": False,
             "why": "It changes very slowly. The point is that the solution "
                    "and the room can differ from the outset"},
            {"text": "Because the room is always warmer than the solution",
             "correct": False,
             "why": "It may be either. That is exactly why you measure rather "
                    "than assume"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s07",
        "band": "standard",
        "text": "Two groups report +7 °C and +2 °C for the same reaction, and "
                "neither invented anything. Which is likely to be closer to "
                "the truth?",
        "options": [
            {"text": "The +2, because a smaller reading means less heat was "
                     "lost during the run and so less of the energy escaped "
                     "before the thermometer could register it",
             "correct": False,
             "why": "Exactly backwards. Losing heat is what makes a reading "
                    "SMALL"},
            {"text": "The +7, because every error in this experiment makes "
                     "the reading too small",
             "correct": True},
            {"text": "The mean of the two, at +4.5",
             "correct": False,
             "why": "Averaging a good result with a bad one gives a worse "
                    "one. These errors do not cancel"},
            {"text": "It cannot be said without knowing which group was more "
                     "careful",
             "correct": False,
             "why": "The direction of the error is known, and it points to "
                    "the larger reading whoever took it"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s08",
        "band": "standard",
        "text": "The same reaction in a glass beaker gives a smaller rise "
                "than in a polystyrene cup. Give BOTH reasons.",
        "options": [
            {"text": "Glass conducts heat away faster, and the reaction runs "
                     "more slowly in glass because the surface of the beaker "
                     "does not stir the mixture as a cup does",
             "correct": False,
             "why": "The container does not change the reaction. The second "
                    "reason is that glass warms itself"},
            {"text": "Glass is transparent, and glass is heavier",
             "correct": False,
             "why": "Neither affects the reading. Conduction and heat "
                    "capacity do"},
            {"text": "Glass conducts heat away faster, and glass absorbs more "
                     "energy warming itself up",
             "correct": True},
            {"text": "Glass reacts with the acid, and glass is colder",
             "correct": False,
             "why": "Glass does not react with dilute acid, and both "
                    "containers start at room temperature"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s09",
        "band": "standard",
        "text": "Why must the volumes and concentrations be kept the same "
                "between runs?",
        "options": [
            {"text": "So that the reaction finishes in the same time each "
                     "run, which is what makes the peak readings comparable "
                     "with one another",
             "correct": False,
             "why": "The timing is a side effect. The reason is that a "
                    "changed variable makes the comparison meaningless"},
            {"text": "So that the same amount of heat is lost each time",
             "correct": False,
             "why": "Heat loss depends on insulation and timing rather than "
                    "on the volumes. Fair comparison is the reason"},
            {"text": "Because the method says so",
             "correct": False,
             "why": "The method says so for a reason, and it is the reason "
                    "that is being asked for"},
            {"text": "So that the only thing being compared is the thing you "
                     "meant to compare",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s10",
        "band": "standard",
        "text": "What would a set of readings need in order to be both "
                "PRECISE and ACCURATE?",
        "options": [
            {"text": "To agree closely with each other AND with the true "
                     "value",
             "correct": True},
            {"text": "To agree closely with each other, taken enough times "
                     "that the mean can be trusted to have settled on the "
                     "right answer",
             "correct": False,
             "why": "That is precision alone. Five readings can agree closely "
                    "and all be low"},
            {"text": "To be taken by more than one person",
             "correct": False,
             "why": "Two people using the same leaking rig get the same low "
                    "answer"},
            {"text": "To be taken with a thermometer reading to two decimal "
                     "places",
             "correct": False,
             "why": "A finer scale improves precision and does nothing about "
                    "a heat loss that is already there"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s11",
        "band": "standard",
        "text": "A group records the peak at 27 °C but forgets to take a "
                "starting temperature. What can they report?",
        "options": [
            {"text": "A change of 27 °C, since the reading they have is the "
                     "one the reaction produced and the other would only have "
                     "been the temperature of the room anyway",
             "correct": False,
             "why": "The solution was already at some temperature before the "
                    "reaction. 27 is where it ended, not how far it moved"},
            {"text": "Nothing about the temperature change, because a change "
                     "needs two readings",
             "correct": True},
            {"text": "A change of about 7 °C, using room temperature as the "
                     "start",
             "correct": False,
             "why": "Room temperature is a guess at the missing reading. It "
                    "may not be what the solution was at"},
            {"text": "That the reaction was exothermic, and nothing else",
             "correct": False,
             "why": "Even that needs a comparison. One reading on its own "
                    "does not show a rise"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s12",
        "band": "standard",
        "text": "A group already has an insulated cup, a lid and a prompt "
                "reading, and their answer is still slightly low. What is "
                "left?",
        "options": [
            {"text": "Nothing at all — a rig with those three things is "
                     "perfect, so any remaining shortfall has to be a random "
                     "error rather than a systematic one",
             "correct": False,
             "why": "There is still a systematic shortfall, and it is the "
                    "apparatus absorbing energy"},
            {"text": "More repeats",
             "correct": False,
             "why": "Repeats do nothing about an error that runs one way "
                    "every time"},
            {"text": "The energy that goes into warming the cup, the lid and "
                     "the thermometer themselves",
             "correct": True},
            {"text": "A larger volume of solution",
             "correct": False,
             "why": "More solution changes the amounts rather than the "
                    "shortfall"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-04-h05",
        "band": "harder",
        "text": "A group with a visibly leaking rig reports a value exactly "
                "equal to the published one. What is the most honest thing to "
                "say?",
        "options": [
            {"text": "That the rig cannot have been leaking after all, since "
                     "a result that matches the published value is the best "
                     "evidence there is that the apparatus was working",
             "correct": False,
             "why": "Matching once is not evidence the rig was sound. It "
                    "invites the question of what else was wrong"},
            {"text": "That the published value must be wrong",
             "correct": False,
             "why": "One school reading is a poor reason to doubt a published "
                    "figure"},
            {"text": "That the result should be reported without comment",
             "correct": False,
             "why": "A result that disagrees with what the apparatus should "
                    "do is exactly the kind that needs a comment"},
            {"text": "That it is suspicious — a leaking rig should read low, "
                     "so something else has pushed it back up",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h06",
        "band": "harder",
        "text": "A bomb calorimeter is weighed and its own heat capacity "
                "measured before any reaction is run. Why go to that trouble?",
        "options": [
            {"text": "Because the vessel absorbs some of the energy itself, "
                     "and that share has to be known to be added back in",
             "correct": True},
            {"text": "Because the vessel has to be identical from one "
                     "laboratory to the next, and weighing it is how that is "
                     "checked before a measurement is published anywhere",
             "correct": False,
             "why": "Vessels differ, which is exactly why each one's own heat "
                    "capacity is measured"},
            {"text": "Because a heavier vessel loses heat faster",
             "correct": False,
             "why": "Heat loss depends on insulation. The mass matters "
                    "because of what the steel absorbs"},
            {"text": "To check nothing has been left inside it",
             "correct": False,
             "why": "Sensible practice and not the reason. The measurement is "
                    "used in the arithmetic afterwards"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h07",
        "band": "harder",
        "text": "Why is a polystyrene cup a genuine piece of scientific "
                "apparatus rather than a cheap substitute for something "
                "better?",
        "options": [
            {"text": "It insulates well enough that no heat escapes from it "
                     "at all, which is the property a container for this "
                     "measurement most needs to have",
             "correct": False,
             "why": "Heat still escapes — the best school rig reads low. Its "
                    "second virtue is its small heat capacity"},
            {"text": "It insulates well AND absorbs very little energy "
                     "warming itself up",
             "correct": True},
            {"text": "It is cheap, so a class can have one each",
             "correct": False,
             "why": "True and beside the point. The question is about the "
                    "physics"},
            {"text": "It cannot break",
             "correct": False,
             "why": "It can be crushed easily enough. Durability is not what "
                    "makes it suitable"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h08",
        "band": "harder",
        "text": "The calorie figures on a food packet come from burning a "
                "sample in a machine. Why is that measurement more trustworthy "
                "than a school one?",
        "options": [
            {"text": "The machine burns a far larger sample, so the "
                     "temperature rise is big enough for the losses to be too "
                     "small to matter beside it",
             "correct": False,
             "why": "The samples are small. What makes it trustworthy is that "
                    "the losses are controlled and accounted for"},
            {"text": "The people running it are more careful",
             "correct": False,
             "why": "Care helps and cannot remove a systematic error. Better "
                    "apparatus can"},
            {"text": "The vessel is sealed and insulated, and its own heat "
                     "capacity is measured and allowed for",
             "correct": True},
            {"text": "It uses electricity rather than a flame",
             "correct": False,
             "why": "Electric ignition is a detail. The insulation and the "
                    "known heat capacity are what matter"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h09",
        "band": "harder",
        "text": "A student proposes comparing three fuels by measuring the "
                "temperature of each FLAME rather than the water. Why is that "
                "no use?",
        "options": [
            {"text": "Because a thermometer put into a flame would break "
                     "before it could take a reading, so no measurement could "
                     "be made at all",
             "correct": False,
             "why": "There are thermometers that survive a flame. The "
                    "objection is that the reading answers the wrong "
                    "question"},
            {"text": "Because all three flames would be at the same "
                     "temperature",
             "correct": False,
             "why": "They would differ. And even different readings would not "
                    "measure energy released"},
            {"text": "Because a flame has no fixed temperature",
             "correct": False,
             "why": "A flame's temperature varies across it and can be "
                    "measured. It is still the wrong quantity"},
            {"text": "Because a flame's temperature says nothing about how "
                     "much energy the fuel released",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h10",
        "band": "harder",
        "text": "Why does averaging genuinely help with a RANDOM error, when "
                "it does nothing for a systematic one?",
        "options": [
            {"text": "Because random errors fall on both sides of the truth, "
                     "so they tend to cancel",
             "correct": True},
            {"text": "Because a random error is smaller than a systematic "
                     "one, so it takes fewer readings to average it away to "
                     "nothing at all",
             "correct": False,
             "why": "Size is not the difference. Direction is — a random "
                    "error can be large and still cancels"},
            {"text": "Because random errors happen less often",
             "correct": False,
             "why": "They happen on every reading. What matters is which way "
                    "they push"},
            {"text": "Because averaging removes the largest and smallest "
                     "readings",
             "correct": False,
             "why": "A mean uses every reading. Nothing is discarded"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h11",
        "band": "harder",
        "text": "A group improves its rig and the answer rises from +5.0 to "
                "+6.8 °C. Has the reaction changed?",
        "options": [
            {"text": "Yes — the better insulation keeps more of the energy in "
                     "the mixture, so the reaction releases more of it and "
                     "the temperature goes higher",
             "correct": False,
             "why": "The reaction releases the same energy whatever it is "
                    "sitting in. What changed is how much of it stayed"},
            {"text": "No — the reaction was always the same, and the "
                     "measurement has got closer to it",
             "correct": True},
            {"text": "Yes, because the conditions were changed",
             "correct": False,
             "why": "The apparatus changed rather than the chemistry. The "
                    "same substances reacted in the same amounts"},
            {"text": "It cannot be known without repeating both",
             "correct": False,
             "why": "Repeating is good practice and the question is settled "
                    "by reasoning: a reaction does not depend on its cup"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h12",
        "band": "harder",
        "text": "The lesson insists that one temperature reading on its own "
                "says nothing. Why is that a statement about the QUANTITY "
                "rather than about carelessness?",
        "options": [
            {"text": "Because a single reading might have been taken at the "
                     "wrong moment, and only a second one taken later shows "
                     "whether the first was at the peak",
             "correct": False,
             "why": "Timing is a separate worry. Even a perfectly timed peak "
                    "is useless without a start"},
            {"text": "Because thermometers are unreliable",
             "correct": False,
             "why": "A perfect thermometer would not help. The quantity "
                    "itself needs two readings"},
            {"text": "Because a temperature change is a difference, and a "
                     "difference cannot be got from one number",
             "correct": True},
            {"text": "Because the room temperature has to be recorded as "
                     "well",
             "correct": False,
             "why": "The room is not the second reading. The solution's "
                    "starting temperature is"},
        ],
        "figure": None,
    },
]
