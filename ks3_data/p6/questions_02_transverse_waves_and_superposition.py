"""P6 lesson 02 — Transverse waves and superposition: twelve questions.

Written against Design's page. The two stones in the pond, the reflection
strip and the superposition lanes are hers.

The discriminations, in the order the lesson builds them:

  · superposition ADDS the two displacements at every point (`WAVE-07`);
  · cancelling is a MOMENT, not a destruction — both waves carry on
    (`WAVE-05`);
  · flat water at an instant still holds the energy (`WAVE-06`);
  · neither wave wins: the pattern is the sum, and it comes apart again
    (`WAVE-08`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — 2,0,1,3 · 0,3,2,1 · 1,2,3,0, three of each.

⚠️ EVERY DISTRACTOR STATES A COMPLETE WRONG RULE. Six sets here had the
correct answer as the longest option by MRB-177's own threshold; the
correct answers are untouched and the short distractors were finished.

⚠️ The ladder's own two marked rungs are NOT restated.
"""

UNIT = "P6"
LESSON = "transverse-waves-and-superposition"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p6-02-e01",
        "band": "easier",
        "text": "When two waves meet at a point, superposition says the "
                "displacement there is…",
        "options": [
            {"text": "whichever of the two is bigger", "correct": False,
             "why": "Nothing is discarded. Both waves contribute at every "
                    "point."},
            {"text": "the average of the two", "correct": False,
             "why": "Averaging halves everything. Two equal crests meeting "
                    "make a crest twice as high, not one the same height."},
            {"text": "the two added together", "correct": True},
            {"text": "always zero, because they cancel", "correct": False,
             "why": "Cancelling happens only when a crest meets a trough of "
                    "the same size. Two crests meeting add up."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e02",
        "band": "easier",
        "text": "A crest of amplitude 3 cm meets a crest of amplitude 2 cm. "
                "How far is the water displaced at that moment?",
        "options": [
            {"text": "5 cm", "correct": True},
            {"text": "1 cm", "correct": False,
             "why": "Subtracting is what happens when a crest meets a "
                    "trough. Two crests both push the water the same way."},
            {"text": "2.5 cm", "correct": False,
             "why": "That is the average. Superposition adds rather than "
                    "averages."},
            {"text": "6 cm", "correct": False,
             "why": "The displacements are added, not multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e03",
        "band": "easier",
        "text": "A crest of amplitude 4 cm meets a trough of amplitude 4 cm. "
                "What is seen at that point at that instant?",
        "options": [
            {"text": "A crest of 8 cm", "correct": False,
             "why": "Adding 8 cm would need two crests. A trough displaces "
                    "the water the opposite way."},
            {"text": "Flat water", "correct": True},
            {"text": "A trough of 8 cm", "correct": False,
             "why": "Again, the two displacements are opposite, so they take "
                    "each other away rather than piling up."},
            {"text": "A crest of 4 cm", "correct": False,
             "why": "That would be one wave on its own. The other one has "
                    "not gone anywhere."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e04",
        "band": "easier",
        "text": "A ripple reaches the straight wall of a tank. What happens?",
        "options": [
            {"text": "It stops dead at the wall and goes no further",
             "correct": False,
             "why": "The energy has to go somewhere, and the water in front "
                    "of the wall keeps moving after the ripple arrives."},
            {"text": "It carries on through the wall and out the other "
                     "side", "correct": False,
             "why": "The wall is not water; the ripple cannot continue "
                    "through it as a water wave."},
            {"text": "It sinks and disappears into the deeper water",
             "correct": False,
             "why": "Ripples do not sink. The disturbance is on the "
                    "surface, and it is still there after it meets the wall."},
            {"text": "It is reflected and travels back across the tank",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p6-02-s01",
        "band": "standard",
        "text": "Two identical pulses travel towards each other along a "
                "rope, one an upward hump and one a downward hump. At the "
                "instant they exactly overlap the rope looks straight. What "
                "happens next?",
        "options": [
            {"text": "The two pulses carry on past each other, each exactly "
                     "as it was before", "correct": True},
            {"text": "The rope stays straight — both pulses have been "
                     "destroyed", "correct": False,
             "why": "The rope is straight for an instant only. The energy is "
                    "in the rope's movement at that moment, and the pulses "
                    "reappear."},
            {"text": "One larger pulse continues in the direction the first "
                     "one was going", "correct": False,
             "why": "Nothing has merged. Two pulses went in and two pulses "
                    "come out, going opposite ways."},
            {"text": "The rope snaps back and the pulses reverse direction",
             "correct": False,
             "why": "Neither pulse turns round. Each keeps going the way it "
                    "was already going."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s02",
        "band": "standard",
        "text": "Two speakers play the same steady note and a listener finds "
                "a spot where the sound is very quiet. What is happening "
                "there?",
        "options": [
            {"text": "One speaker is faulty and producing nothing at that "
                     "moment", "correct": False,
             "why": "Cover one speaker and the quiet spot fills with sound "
                    "again, which shows both were working."},
            {"text": "The sound from the two speakers is being absorbed by "
                     "the air at that point", "correct": False,
             "why": "Air does not absorb sound at one spot and not the next. "
                    "Move a step and the sound is loud again."},
            {"text": "The two speakers are cancelling each other out for "
                     "good, so no energy leaves them and the room is quiet "
                     "everywhere", "correct": False,
             "why": "Energy is leaving them all the time — a step to one "
                    "side and it is loud. Cancelling redistributes it, it "
                    "does not remove it."},
            {"text": "A compression from one speaker is arriving with a "
                     "rarefaction from the other, and the two take each "
                     "other away", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s03",
        "band": "standard",
        "text": "At an instant when two waves cancel completely across a "
                "whole stretch of water, where has the energy gone?",
        "options": [
            {"text": "It has been turned into heat by the collision",
             "correct": False,
             "why": "Waves do not collide in that sense. Nothing is warmed, "
                    "and both waves emerge unchanged a moment later."},
            {"text": "It has been used up making the water flat",
             "correct": False,
             "why": "Making water flat is what water does on its own. It "
                    "costs nothing."},
            {"text": "Nowhere — the water is flat but moving, so the energy "
                     "is in its motion", "correct": True},
            {"text": "It was never there, because two waves that cancel "
                     "carry no energy", "correct": False,
             "why": "Each wave carries energy on its own, and each is still "
                    "carrying it. The flat moment does not undo that."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s04",
        "band": "standard",
        "text": "Two stones are dropped into a pond at the same moment a "
                "little way apart. What pattern appears where the two sets "
                "of ripples overlap?",
        "options": [
            {"text": "A single set of ripples spreading out from one point "
                     "midway between the two stones", "correct": False,
             "why": "The two sources stay separate, and their circles keep "
                    "spreading from where each stone landed."},
            {"text": "A criss-cross pattern with places of unusually big "
                     "movement and places of almost none", "correct": True},
            {"text": "Flat water everywhere that the two sets of ripples "
                     "meet and cancel one another out", "correct": False,
             "why": "That happens only where a crest meets a trough. "
                    "Elsewhere the crests reinforce each other."},
            {"text": "The stronger set of ripples carrying on and the "
                     "weaker set vanishing away altogether",
             "correct": False,
             "why": "Neither set vanishes. Both keep spreading and both keep "
                    "contributing everywhere they overlap."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p6-02-h01",
        "band": "harder",
        "text": "Noise-cancelling headphones work by playing a second sound. "
                "Why does the wearer hear quiet rather than more noise?",
        "options": [
            {"text": "The headphones play a very loud sound that drowns "
                     "out the noise, so the wearer simply stops noticing "
                     "what was there before", "correct": False,
             "why": "That would be louder, not quieter, and the wearer would "
                    "hear the drowning sound instead."},
            {"text": "The second sound is timed so its compressions arrive "
                     "where the noise has rarefactions, and the two add to "
                     "almost nothing at the eardrum", "correct": True},
            {"text": "The headphones absorb the noise in their padding "
                     "before it reaches the ear, so nothing at all is left "
                     "of it by the time the eardrum is reached",
             "correct": False,
             "why": "Some padding does absorb, but that is not what the "
                    "electronics are doing. Switch the electronics off and "
                    "the padding is still there."},
            {"text": "The second sound is at a frequency too high to hear, "
                     "so it removes the noise silently — a sound nobody can "
                     "hear can still take away one they can",
             "correct": False,
             "why": "A sound the ear cannot respond to cannot cancel one it "
                    "can. The cancelling sound is at the same frequency as "
                    "the noise."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h02",
        "band": "harder",
        "text": "Why is it wrong to say that when two waves cancel they "
                "destroy each other?",
        "options": [
            {"text": "Because they never really cancel — there is always a "
                     "little left over, and that leftover is what carries "
                     "both waves on past each other", "correct": False,
             "why": "Two equal and opposite displacements do cancel exactly. "
                    "The trouble with the word is what happens afterwards."},
            {"text": "Because only one of them is destroyed and the other "
                     "carries on through the water on its own, entirely "
                     "unchanged by the meeting", "correct": False,
             "why": "Neither is destroyed. Both emerge, and both are "
                    "unchanged."},
            {"text": "Because cancelling is what the WATER does at one "
                     "place at one instant, while both waves travel on "
                     "through each other unchanged", "correct": True},
            {"text": "Because waves cannot be destroyed by anything at "
                     "all, so nothing that happens where two of them meet "
                     "could ever count as destruction", "correct": False,
             "why": "Waves are absorbed and die away all the time. What "
                    "cancelling is not, is one of the ways that happens."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h03",
        "band": "harder",
        "text": "A student says that where two waves meet, the bigger one "
                "wins. What is the best correction?",
        "options": [
            {"text": "The smaller one wins, because it is easier for the "
                     "water to follow a small movement than it is to "
                     "follow a larger one instead", "correct": False,
             "why": "Reversing the claim keeps the mistake. Neither wave "
                    "wins anything."},
            {"text": "The bigger one wins only if it has the longer "
                     "wavelength as well, so length decides it whenever the "
                     "two heights are close together", "correct": False,
             "why": "Wavelength does not decide it either. Both waves "
                    "contribute whatever their length."},
            {"text": "They take it in turns, one after the other, so the "
                     "water follows first the one wave and then the other "
                     "one after it", "correct": False,
             "why": "They arrive together, not in turn, and the water "
                    "responds to both at once."},
            {"text": "Neither wins — the water is displaced by the sum of "
                     "the two, and each wave carries on afterwards exactly "
                     "as it was before", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h04",
        "band": "harder",
        "text": "A wave is reflected from a wall and meets the wave still "
                "arriving. In some places the water hardly moves at all, and "
                "those places stay put. What does that tell you?",
        "options": [
            {"text": "The two waves are adding to nothing at those points "
                     "every cycle, because the arriving and reflected waves "
                     "have a fixed timing relationship", "correct": True},
            {"text": "The reflected wave is weaker, so it can only cancel in "
                     "a few places, and those places are wherever the two "
                     "happen to be passing at the time", "correct": False,
             "why": "The still places would drift about rather than stay "
                    "put, and there would be no clear pattern."},
            {"text": "The water is deeper at those points, so it cannot "
                     "move", "correct": False,
             "why": "Depth is a property of the tank and would not produce "
                    "a repeating pattern of still and moving places."},
            {"text": "The wall has absorbed the wave at those points",
             "correct": False,
             "why": "The wall is one surface and cannot absorb at some "
                    "points in the tank and not others."},
        ],
        "figure": None,
    },
]
