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
]
