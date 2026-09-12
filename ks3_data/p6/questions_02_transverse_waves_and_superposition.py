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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-02-e05",
        "band": "easier",
        "text": "Two waves overlap and then pass each other. What happens to "
                "each wave afterwards?",
        "options": [            {"text": "Both stop where they met", "correct": False,
             "why": "Meeting does not stop a wave — it keeps travelling in "
                    "the direction it was going."},
            {"text": "The larger one carries on and the smaller one is gone",
             "correct": False,
             "why": "Neither is destroyed; both emerge from the overlap "
                    "unchanged."},
            {"text": "They join into one wave of the average size",
             "correct": False,
             "why": "Averaging never happens. They add while they overlap and "
                    "then separate again."},
            {"text": "Each carries on exactly as it was", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e06",
        "band": "easier",
        "text": "Adding the two displacements at every point where waves "
                "overlap is called…",
        "options": [
            {"text": "reflection", "correct": False,
             "why": "Reflection is a wave bouncing off a barrier, which is a "
                    "different behaviour."},
            {"text": "absorption", "correct": False,
             "why": "Absorption is a surface taking energy from a wave, not "
                    "two waves meeting."},
            {"text": "superposition", "correct": True},
            {"text": "refraction", "correct": False,
             "why": "Refraction is a wave changing direction as it enters a "
                    "different material."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-02-s05",
        "band": "standard",
        "text": "A crest of amplitude 5 cm meets a trough of amplitude 2 cm. "
                "What is the displacement there at that instant?",
        "options": [            {"text": "3 cm upwards", "correct": True},
            {"text": "7 cm upwards", "correct": False,
             "why": "That adds them as though both were crests; a trough "
                    "counts the other way."},
            {"text": "3 cm downwards", "correct": False,
             "why": "The size is right but the direction is not: the crest is "
                    "the larger of the two."},
            {"text": "0 cm — they cancel", "correct": False,
             "why": "They only cancel completely when the two are the same "
                    "size, and these are not."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s06",
        "band": "standard",
        "text": "A ripple reflects off the wall of a tank. What can then "
                "happen to it?",
        "options": [            {"text": "It travels back and can overlap with the waves still "
                     "arriving",
             "correct": True},
            {"text": "It stops at the wall, having given up its energy",
             "correct": False,
             "why": "Some is absorbed, but a reflected ripple travels back "
                    "across the tank."},
            {"text": "It travels back at half the speed it arrived with",
             "correct": False,
             "why": "The speed is set by the water, and reflecting does not "
                    "change it."},
            {"text": "It carries on through the wall into the bench",
             "correct": False,
             "why": "The wall is what it reflects from; that is what makes "
                    "the returning ripple."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-02-h05",
        "band": "harder",
        "text": "A crest of amplitude 3 mm meets a trough of amplitude 5 mm. "
                "What is seen where they overlap?",
        "options": [
            {"text": "A displacement of 8 mm downwards", "correct": False,
             "why": "That adds their sizes; a crest and a trough count "
                    "against each other."},
            {"text": "Flat water, because a crest and a trough always cancel",
             "correct": False,
             "why": "They cancel completely only when the two amplitudes "
                    "match, and these differ by 2 mm."},
            {"text": "A displacement of 2 mm downwards", "correct": True},
            {"text": "A displacement of 2 mm upwards", "correct": False,
             "why": "The size is right but the trough is the larger, so what "
                    "is left over points downwards."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h06",
        "band": "harder",
        "text": "In a crossing pattern some patches heave twice as far and "
                "others stay flat. What is true at every flat patch?",
        "options": [
            {"text": "The two waves arrive there crest on trough",
             "correct": True},
            {"text": "Only one of the two waves ever reaches there",
             "correct": False,
             "why": "Both reach every patch; it is how they line up that "
                    "differs from place to place."},
            {"text": "The water there is deeper, so the waves are damped",
             "correct": False,
             "why": "The pattern appears in a tank of even depth, so depth is "
                    "not what makes it."},
            {"text": "The energy of both waves has been absorbed there",
             "correct": False,
             "why": "Nothing absorbs it — the waves carry on past the flat "
                    "patch unchanged."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-02-e07",
        "band": "easier",
        "text": "A rope is shaken from side to side so that a wave travels "
                "along it. This is a transverse wave because the rope "
                "itself moves…",
        "options": [
            {"text": "at right angles to the direction the wave travels "
                     "along the rope", "correct": True},
            {"text": "along the rope, moving the same way the wave itself "
                     "is travelling along its length",
             "correct": False,
             "why": "That describes a longitudinal wave, not a transverse "
                    "one."},
            {"text": "in a full circle around the rope's own length",
             "correct": False,
             "why": "A shaken rope moves side to side, not in circles "
                    "around its own length."},
            {"text": "only at the two ends where the rope is held",
             "correct": False,
             "why": "Every point the wave reaches moves, not just the "
                    "ends."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e08",
        "band": "easier",
        "text": "A wave reflects straight back off a barrier. Which two "
                "properties of the wave stay the same after reflecting?",
        "options": [
            {"text": "Its amplitude and its direction of travel",
             "correct": False,
             "why": "Direction is exactly what reflection changes — the "
                    "wave now travels the other way."},
            {"text": "Its energy and its direction of travel",
             "correct": False,
             "why": "Direction changes on reflection; it is wavelength and "
                    "frequency that stay the same."},
            {"text": "Nothing stays the same — a reflected wave is a "
                     "completely new wave", "correct": False,
             "why": "It is still the same wave, just travelling the other "
                    "way with its wavelength and frequency unchanged."},
            {"text": "Its wavelength and its frequency", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e09",
        "band": "easier",
        "text": "Superposition is the rule that, wherever two waves "
                "overlap, the surface…",
        "options": [
            {"text": "takes the average of the two displacements at that "
                     "point", "correct": False,
             "why": "It takes the total, not a halfway compromise between "
                    "the two."},
            {"text": "always moves to whichever displacement is bigger, "
                     "ignoring the smaller one", "correct": False,
             "why": "Both displacements count; the smaller one is not "
                    "ignored."},
            {"text": "takes the sum of the two displacements at that point",
             "correct": True},
            {"text": "stops moving altogether until the two waves have "
                     "passed each other", "correct": False,
             "why": "The surface keeps moving throughout — it just moves "
                    "by the combined amount."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e10",
        "band": "easier",
        "text": "A ripple-tank paddle is switched off, leaving the water "
                "completely flat where a wave used to be. What has "
                "happened here?",
        "options": [
            {"text": "Two waves have cancelled each other out exactly",
             "correct": False,
             "why": "Cancelling needs two waves overlapping; here there is "
                    "simply no wave at all."},
            {"text": "A single wave has lost all its energy on the spot",
             "correct": False,
             "why": "Nothing about switching a paddle off destroys energy; "
                    "it simply stops making a new wave."},
            {"text": "Its amplitude and wavelength have become zero",
             "correct": False,
             "why": "Wavelength describes the spacing of a wave that "
                    "exists; with no wave present, that idea does not "
                    "apply here at all."},
            {"text": "There is no wave there any more, rather than two "
                     "waves cancelling", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e11",
        "band": "easier",
        "text": "Using the usual sign convention for displacement, a point "
                "on the water sitting below the still level counts as…",
        "options": [
            {"text": "positive", "correct": False,
             "why": "Positive is used for a point above the still level, "
                    "not below it."},
            {"text": "negative", "correct": True},
            {"text": "zero, because only points above the still level are "
                     "measured", "correct": False,
             "why": "Points below the still level are measured too — as "
                    "negative displacements, not as zero."},
            {"text": "it depends on the wavelength of the wave",
             "correct": False,
             "why": "The sign only depends on which side of the still "
                    "level the point sits, not on the wavelength."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e12",
        "band": "easier",
        "text": "When a crest from one wave meets a crest from another wave "
                "of the same size, superposition gives…",
        "options": [
            {"text": "a smaller crest than either wave had alone",
             "correct": False,
             "why": "Two crests ADD; the result is bigger, not smaller."},
            {"text": "flat water, because the two waves cancel",
             "correct": False,
             "why": "Cancelling happens when a crest meets a trough, not "
                    "when two crests meet."},
            {"text": "a bigger crest than either wave had alone",
             "correct": True},
            {"text": "exactly the same crest as either wave had alone, "
                     "unchanged", "correct": False,
             "why": "Adding two crests together gives a taller crest, not "
                    "an unchanged one."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e13",
        "band": "easier",
        "text": "After two overlapping waves have passed through each "
                "other and moved apart again, what has happened to each "
                "one?",
        "options": [
            {"text": "Each one carries on afterwards exactly as it was "
                     "before the overlap", "correct": True},
            {"text": "The bigger wave has absorbed the smaller one, so only "
                     "one wave remains afterwards", "correct": False,
             "why": "Neither wave absorbs the other; both continue on "
                    "their own, unchanged."},
            {"text": "Both waves are permanently changed by the overlap and "
                     "never return to their original size", "correct": False,
             "why": "The change to each wave's shape only lasts while they "
                    "are overlapping; afterwards each returns to normal."},
            {"text": "Both waves stop travelling once they have overlapped "
                     "once", "correct": False,
             "why": "Overlapping does not stop either wave; both carry on "
                    "travelling afterwards."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e14",
        "band": "easier",
        "text": "What word names a wave bouncing back off a barrier, still "
                "travelling as the same wave with the same wavelength?",
        "options": [
            {"text": "superposition", "correct": False,
             "why": "Superposition is what happens when two waves "
                    "overlap, not a wave bouncing off a barrier."},
            {"text": "displacement", "correct": False,
             "why": "Displacement is how far the surface is from the still "
                    "level, not the bouncing of a wave off a barrier."},
            {"text": "reflection", "correct": True},
            {"text": "amplitude", "correct": False,
             "why": "Amplitude is a height measurement, not the name for a "
                    "wave bouncing off a barrier."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-02-s07",
        "band": "standard",
        "text": "A wave train of amplitude 8 mm meets a second wave train "
                "of amplitude 3 mm exactly crest on trough, at a point "
                "where they overlap. What is the displacement of the "
                "surface at that point?",
        "options": [
            {"text": "11 mm", "correct": False,
             "why": "Adding both amplitudes is right for crest on crest, "
                    "not for crest on trough, which works the other way."},
            {"text": "0 mm, because crest on trough always cancels "
                     "completely", "correct": False,
             "why": "Exact cancelling only happens when the two amplitudes "
                    "are equal. Here 8 mm and 3 mm are different sizes."},
            {"text": "2.5 mm, taking the average of the two amplitudes",
             "correct": False,
             "why": "Superposition adds the two displacements; it does not "
                    "average them."},
            {"text": "5 mm, in the direction of the larger wave's crest",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s08",
        "band": "standard",
        "text": "Two identical wave trains meet exactly crest on crest, "
                "giving a wave with twice the amplitude of either one "
                "alone, for as long as they overlap. Does this create any "
                "new energy?",
        "options": [
            {"text": "Yes — a wave with twice the amplitude must contain "
                     "twice the total energy of the whole system",
             "correct": False,
             "why": "No energy is added; the taller wave only exists while "
                    "the two are overlapping, and both return to normal "
                    "afterwards."},
            {"text": "No — once the two waves have passed through each "
                     "other, each is back to its own original amplitude",
             "correct": True},
            {"text": "Yes, but only while the two waves are overlapping, "
                     "and the extra energy then simply disappears",
             "correct": False,
             "why": "Energy cannot appear and then disappear; nothing new "
                    "was ever created in the first place."},
            {"text": "It cannot be answered without knowing the wavelength "
                     "of each wave", "correct": False,
             "why": "Wavelength isn't needed here — both waves keep their "
                    "own amplitude afterwards, which already answers the "
                    "question."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s09",
        "band": "standard",
        "text": "A point on the water sits 4 mm below the still level. "
                "Using the usual sign convention, what is its "
                "displacement?",
        "options": [
            {"text": "+4 mm", "correct": False,
             "why": "Positive is for a point above the still level; this "
                    "point is below it."},
            {"text": "4 mm, with no sign needed at all", "correct": False,
             "why": "The sign convention specifically needs a sign to show "
                    "which side of the still level the point is on."},
            {"text": "It cannot be given a displacement, because it is "
                     "below the still level rather than above it",
             "correct": False,
             "why": "Points below the still level get a displacement too — "
                    "a negative one — just as points above get a positive "
                    "one."},
            {"text": "−4 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s10",
        "band": "standard",
        "text": "A wave of wavelength 40 cm travels down a channel and "
                "reflects straight back off a wall at the far end. What is "
                "the wavelength of the reflected wave?",
        "options": [
            {"text": "20 cm, since reflecting off a wall halves the "
                     "wavelength", "correct": False,
             "why": "Reflection does not change the wavelength at all; it "
                    "only changes the direction of travel."},
            {"text": "40 cm", "correct": True},
            {"text": "80 cm, since reflecting off a wall doubles the "
                     "wavelength", "correct": False,
             "why": "There is no doubling on reflection — the wavelength "
                    "stays exactly as it was."},
            {"text": "It cannot be found without knowing how far away the "
                     "wall is", "correct": False,
             "why": "The distance to the wall plays no part in what the "
                    "reflected wave's wavelength turns out to be."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s11",
        "band": "standard",
        "text": "Two loudspeakers, wired to play exactly the same single "
                "note, are set up a short distance apart. Walking along in "
                "front of them, a listener passes through spots where the "
                "note sounds much quieter. What is happening at those "
                "quiet spots?",
        "options": [
            {"text": "Only one of the two speakers is reaching that spot "
                     "at all", "correct": False,
             "why": "Both speakers are playing into the same room; sound "
                    "from both reaches every spot."},
            {"text": "The sound waves from the two speakers are arriving "
                     "out of step and partly cancelling by superposition",
             "correct": True},
            {"text": "The air simply absorbs more sound at certain "
                     "distances from the speakers", "correct": False,
             "why": "Nothing about the air itself changes from spot to "
                    "spot here; the quiet patches come from how the two "
                    "waves combine."},
            {"text": "The two speakers turn down automatically",
             "correct": False,
             "why": "Ordinary loudspeakers do no such thing; the quiet "
                    "patches are a property of the sound waves combining, "
                    "not of the speakers themselves."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s12",
        "band": "standard",
        "text": "Noise-cancelling headphones remove an unwanted sound by "
                "generating another sound wave. For this to cancel the "
                "unwanted sound, how must the generated wave arrive?",
        "options": [
            {"text": "Crest on crest with the unwanted sound wave",
             "correct": False,
             "why": "Crest on crest would ADD to the unwanted sound and "
                    "make it louder, not cancel it."},
            {"text": "At a completely different frequency from the "
                     "unwanted sound", "correct": False,
             "why": "A different frequency would not consistently line up "
                    "to cancel the unwanted sound at all."},
            {"text": "Crest on trough with the unwanted sound wave",
             "correct": True},
            {"text": "Travelling in the same direction as the unwanted "
                     "sound wave, at a lower amplitude", "correct": False,
             "why": "Direction and amplitude alone do not cancel a wave; "
                    "arriving crest on trough is what is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s13",
        "band": "standard",
        "text": "One wave gives a displacement of +9 mm at a point, at the "
                "same moment a second wave gives a displacement of −4 mm "
                "at that same point. What is the resulting displacement?",
        "options": [
            {"text": "+13 mm", "correct": False,
             "why": "That adds the two sizes without using the negative "
                    "sign on the second wave."},
            {"text": "−5 mm", "correct": False,
             "why": "Adding +9 and −4 gives a positive result, since the "
                    "positive displacement is the larger of the two."},
            {"text": "+4.5 mm, the average of the two displacements",
             "correct": False,
             "why": "Superposition adds the two displacements together; it "
                    "does not average them."},
            {"text": "+5 mm", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-02-h07",
        "band": "harder",
        "text": "A wave train travels down a channel toward a barrier and "
                "reflects, running back through the wave train still "
                "arriving. Some fixed points in the channel never move at "
                "all, however long they are watched, while points half a "
                "wavelength away heave up and down strongly and "
                "continuously. Explain why this pattern forms.",
        "options": [
            {"text": "The reflected wave is weaker than the incoming wave, "
                     "so it can only partly cancel it at certain points",
             "correct": False,
             "why": "Nothing here suggests the reflected wave lost "
                    "strength; the explanation is about matching "
                    "wavelengths, not weakening."},
            {"text": "Because the two waves share the same wavelength, a "
                     "crest from one always meets a trough from the other "
                     "at some fixed points, and a crest always meets a "
                     "crest at others — and neither relationship ever "
                     "changes over time", "correct": True},
            {"text": "The barrier absorbs the wave unevenly along its "
                     "length, letting more through in some places than "
                     "others", "correct": False,
             "why": "Uneven absorption at the barrier is not part of what "
                    "is described; the still and heaving points come from "
                    "how the two waves combine, not from the barrier."},
            {"text": 'Superposition works only between waves travelling in the '
                     'same direction, so the still points mark where the rule '
                     'has stopped applying, since two waves running at each '
                     'other cancel everywhere at once rather than at fixed '
                     'places along the channel', "correct": False,
             "why": "Superposition adds displacements whichever way each "
                    "wave is travelling; there is no such restriction."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h08",
        "band": "harder",
        "text": "A student claims superposition can only really happen "
                "with waves on water, since that is the only place two "
                "waves can properly overlap. Assess this using the "
                "noise-cancelling headphone example.",
        "options": [
            {"text": "The claim is correct, since sound cannot overlap the "
                     "way water waves can", "correct": False,
             "why": "Noise-cancelling headphones rely on exactly that kind "
                    "of overlap happening with sound."},
            {"text": "The claim is correct, because headphones use "
                     "electronics rather than genuine wave overlap to "
                     "remove sound", "correct": False,
             "why": "The cancelling itself comes from the generated sound "
                    "wave genuinely overlapping the unwanted one, not from "
                    "electronics alone."},
            {"text": 'The claim is wrong, but only because sound is a special '
                     'exception, rather than following the same rule water '
                     'waves do', "correct": False,
             "why": "Sound is not a special exception — the very same "
                    "adding-displacements rule is what makes the "
                    "cancelling happen."},
            {"text": "The claim is wrong — the same rule of adding "
                     "displacements applies to sound waves too, which is "
                     "how a headphone can generate a wave that cancels an "
                     "unwanted sound", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h09",
        "band": "harder",
        "text": "At one particular fixed point in a channel, an incoming "
                "wave and its reflection are found to be permanently "
                "cancelling however long the point is watched, given that "
                "both waves share the same wavelength. What can be said "
                "about that point?",
        "options": [
            {"text": "It must sit exactly halfway between the barrier and "
                     "the wave source", "correct": False,
             "why": "Where a still point falls depends on the wavelength "
                    "and the distance to the barrier, not simply on being "
                    "halfway along."},
            {"text": "A crest from one wave always arrives there together "
                     "with a trough from the other, and — because the "
                     "wavelength never changes — that relationship holds "
                     "at every later moment too", "correct": True},
            {"text": 'The two waves must have slightly different wavelengths at '
                     'that point, which is why they fail to add up to zero '
                     'every time', "correct": False,
             "why": "The two waves are stated to share the same "
                    "wavelength; that is exactly what keeps the "
                    "cancelling permanent."},
            {"text": "That point is slowly drifting along the channel over "
                     "time, following the incoming wave as it travels",
             "correct": False,
             "why": "A permanently still point stays fixed in place; it "
                    "does not drift along with either wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h10",
        "band": "harder",
        "text": "Two wave trains of different wavelengths overlap along "
                "the same stretch of channel. A student expects to see the "
                "same kind of permanent still-and-heaving pattern seen "
                "when a wave reflects off a barrier. Explain why this "
                "expectation is probably wrong.",
        "options": [
            {"text": "It is wrong because waves of different wavelengths "
                     "cannot superpose at all — only identical waves can "
                     "add together", "correct": False,
             "why": "The surface adds whatever displacements are present "
                    "at a point, whatever the wavelengths involved; "
                    "superposition still happens."},
            {"text": "It is wrong because superposition needs both waves "
                     "to be travelling in exactly the same direction",
             "correct": False,
             "why": "Direction of travel is not the reason a permanent "
                    "pattern needs matching wavelengths."},
            {"text": 'The expectation is correct — any two overlapping waves, '
                     'whatever their wavelengths, settle into a fixed '
                     'still-and-heaving pattern given enough time, because the '
                     'longer wave eventually falls into step with the shorter '
                     'one and the pattern then stops moving', "correct": False,
             "why": "A permanent pattern specifically needs matching "
                    "wavelengths; without that, the pattern of adding and "
                    "cancelling positions keeps shifting rather than "
                    "settling."},
            {"text": "A permanent pattern needs the crest-meets-trough (or "
                     "crest-meets-crest) relationship at each fixed point "
                     "to stay the same over time, which relies on the two "
                     "waves sharing a wavelength — with different "
                     "wavelengths that relationship keeps shifting instead",
             "correct": True},
        ],
        "figure": None,
    },
]
