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

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p6-02-e15",
        "band": "easier",
        "text": "A floating marker shows no rise and no dip at all — it "
                "sits exactly level with the undisturbed water surface. "
                "What value should be recorded for its displacement?",
        "options": [
            {"text": "0", "correct": True},
            {"text": "+1", "correct": False,
             "why": "A point exactly at the still level has not been "
                    "displaced at all, so its value is zero, not a small "
                    "positive number."},
            {"text": "It has no displacement value at all, since it "
                     "isn't above or below anything", "correct": False,
             "why": "Every point on the water has a displacement value; "
                    "for a point at the still level, that value is "
                    "simply zero."},
            {"text": "It depends on which way the nearest wave is "
                     "travelling", "correct": False,
             "why": "Displacement is measured from the still level, and "
                    "a point exactly on it is always zero, whichever way "
                    "any nearby wave is travelling."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e16",
        "band": "easier",
        "text": "Two crests arrive together at one point and lift the "
                "water 16 mm. One of the two crests is 7 mm on its own. How big "
                "is the other crest?",
        "options": [
            {"text": "23 mm", "correct": False,
             "why": "That adds 16 and 7 together. The 16 mm is already "
                    "the total of the two crests, so the second one is what is "
                    "left when the 7 mm is taken off."},
            {"text": "9 mm", "correct": True},
            {"text": "16 mm", "correct": False,
             "why": "16 mm is the combined rise of both crests "
                    "together, not the size of the second crest on its own."},
            {"text": "2.3 mm", "correct": False,
             "why": "That divides 16 by 7. The two crests add together, "
                    "so the second one is found by subtracting, not dividing."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e17",
        "band": "easier",
        "text": "A pulse is sent along a channel with a wavelength of "
                "25 cm. It bounces straight back off a wall at the far "
                "end. What is its wavelength on the way back?",
        "options": [
            {"text": "12.5 cm", "correct": False,
             "why": "Bouncing off a wall does not halve the wavelength; "
                    "it only changes which way the pulse is travelling."},
            {"text": "50 cm", "correct": False,
             "why": "Bouncing off a wall does not double the wavelength "
                    "either — the spacing between crests stays exactly "
                    "as it was."},
            {"text": "25 cm", "correct": True},
            {"text": "It cannot be found without knowing how far away "
                     "the wall is", "correct": False,
             "why": "Distance to the wall does not change the "
                    "wavelength of the reflected pulse; only the timing "
                    "of the bounce depends on that."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e18",
        "band": "easier",
        "text": "After a wave reflects off a barrier, which of its "
                "properties has changed?",
        "options": [
            {"text": "its wavelength, but nothing else", "correct": False,
             "why": "Reflecting off a barrier leaves the wavelength "
                    "exactly as it was — only the direction changes."},
            {"text": "its amplitude, but nothing else", "correct": False,
             "why": "Reflecting off a barrier does not, by itself, "
                    "change how far the surface rises — only the direction "
                    "changes."},
            {"text": "everything about it — it is really a brand new "
                     "wave afterwards", "correct": False,
             "why": "The reflected wave keeps its wavelength and "
                    "amplitude; only its direction of travel is new."},
            {"text": "only the direction it is travelling in", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e19",
        "band": "easier",
        "text": "A transverse water wave reflects off a wall. Is the "
                "reflected wave still transverse, or does reflecting "
                "change what kind of wave it is?",
        "options": [
            {"text": "Still transverse — reflecting only changes the "
                     "direction it travels in", "correct": True},
            {"text": "It becomes longitudinal, since it is now moving "
                     "the opposite way", "correct": False,
             "why": "Reflecting changes the DIRECTION of travel, not "
                    "the direction the water itself moves relative to "
                    "that — the wave stays transverse."},
            {"text": "It stops being a wave at all until it meets "
                     "another wave to overlap with", "correct": False,
             "why": "A reflected wave is still a travelling disturbance "
                    "on its own — it does not need a second wave to "
                    "count as a wave."},
            {"text": "It becomes a mixture of transverse and "
                     "longitudinal", "correct": False,
             "why": "Nothing about bouncing off a wall mixes in a "
                    "different kind of motion; the water still moves at "
                    "right angles to the new direction of travel."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e20",
        "band": "easier",
        "text": "Two ripples arrive at the same spot at the same "
                "instant: one lifts the surface 9 mm, the other pushes it down "
                "9 mm. What is the net effect at that spot?",
        "options": [
            {"text": "The surface rises 18 mm, since both ripples are "
                     "acting on it at once", "correct": False,
             "why": "Adding 9 mm up and 9 mm down cancels to zero; it "
                    "does not add up to a bigger rise."},
            {"text": "The two cancel exactly, and the water is flat "
                     "there", "correct": True},
            {"text": "The surface falls 18 mm", "correct": False,
             "why": "The two displacements are equal and opposite, so "
                    "they cancel to zero rather than adding to a bigger fall."},
            {"text": "Nothing can be said without knowing which ripple "
                     "arrived first", "correct": False,
             "why": "Both are stated to arrive at the same instant, so "
                    "their order does not come into it; the two simply add "
                    "together."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e21",
        "band": "easier",
        "text": "A crest of 5 mm overlaps with a trough of 8 mm. In "
                "which direction is the water displaced at the overlap, and "
                "why?",
        "options": [
            {"text": "Upwards, because a crest is always the one that "
                     "wins", "correct": False,
             "why": "Neither one \"wins\" — the two sizes are compared, "
                    "and here the trough is the larger of the two."},
            {"text": "There is no overall direction, since the two "
                     "cancel to exactly zero", "correct": False,
             "why": "Exact cancelling only happens when the two sizes "
                    "match. Here 5 mm and 8 mm are different, so they only "
                    "partly cancel."},
            {"text": "Downwards, because the trough is the larger of "
                     "the two", "correct": True},
            {"text": "Downwards, because troughs are always bigger than "
                     "crests", "correct": False,
             "why": "Troughs are not generally bigger than crests — "
                    "here the 8 mm trough is simply the larger of these two "
                    "particular waves."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e22",
        "band": "easier",
        "text": "At a certain instant, one wave is lifting a point 5 mm "
                "above the still level, while a second wave overlapping there "
                "at the very same moment is lifting it a further 3 mm. How high "
                "does the point reach in total?",
        "options": [
            {"text": "2 mm", "correct": False,
             "why": "That subtracts the two. Both displacements are "
                    "positive, so superposition adds them together."},
            {"text": "15 mm", "correct": False,
             "why": "That multiplies the two values. Superposition adds "
                    "displacements; it does not multiply them."},
            {"text": "0 mm, since two upward pushes always cancel out", "correct": False,
             "why": "Two displacements in the same direction do not "
                    "cancel each other — cancelling needs one pushing up and "
                    "one pushing down by the same amount."},
            {"text": "8 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e23",
        "band": "easier",
        "text": "A skipping rope is shaken at one end so a hump travels "
                "along it, hits the fixed far end, and bounces back. "
                "What word describes this bounce?",
        "options": [
            {"text": "reflection", "correct": True},
            {"text": "refraction", "correct": False,
             "why": "Refraction is a wave changing direction as it "
                    "enters a different material, not a hump bouncing "
                    "off a fixed end."},
            {"text": "wavelength", "correct": False,
             "why": "Wavelength is a distance measurement along the "
                    "rope, not the name for a hump bouncing back."},
            {"text": "absorption", "correct": False,
             "why": "Absorption would mean the far end soaking up the "
                    "hump rather than sending it back — the opposite of "
                    "what happens here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e24",
        "band": "easier",
        "text": "In a ripple tank, two paddle-generated crests of 4 mm "
                "and 6 mm happen to arrive together at exactly the same spot. "
                "How high does the water rise there?",
        "options": [
            {"text": "2 mm", "correct": False,
             "why": "That subtracts the two. Two crests both lift the "
                    "surface the same way, so they add rather than subtract."},
            {"text": "10 mm", "correct": True},
            {"text": "24 mm", "correct": False,
             "why": "That multiplies the two amplitudes together, which "
                    "is not what superposition does."},
            {"text": "6 mm", "correct": False,
             "why": "That only counts the larger crest — the smaller "
                    "one is still lifting the surface too."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e25",
        "band": "easier",
        "text": "A single wave train travels along a channel with no "
                "second wave present anywhere. Does superposition apply here?",
        "options": [
            {"text": "Yes — superposition applies to every wave, on its "
                     "own or not", "correct": False,
             "why": "Superposition is specifically about ADDING two or "
                    "more waves together; a lone wave has nothing to add to."},
            {"text": "It depends on the wave's amplitude", "correct": False,
             "why": "Whether superposition applies depends on whether "
                    "another wave is present to overlap with, not on how big "
                    "the one wave is."},
            {"text": "No — superposition only applies where two or more "
                     "waves overlap", "correct": True},
            {"text": "It depends on the wave's wavelength", "correct": False,
             "why": "Wavelength does not decide whether superposition "
                    "applies — the presence of a second wave to overlap with "
                    "does."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e26",
        "band": "easier",
        "text": "Two crests of the same height meet at a point. "
                "Compared with either crest alone, the water at that point is…",
        "options": [
            {"text": "the same height as either crest alone", "correct": False,
             "why": "Two equal crests add together; the result is "
                    "taller than either one on its own, not the same."},
            {"text": "flat, because the two crests cancel", "correct": False,
             "why": "Two crests both lift the surface the same way, so "
                    "they add — cancelling needs a crest and a trough."},
            {"text": "half as high", "correct": False,
             "why": "Adding two equal crests together gives a taller "
                    "result, not a shorter one."},
            {"text": "twice as high", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e27",
        "band": "easier",
        "text": "A crest and a trough of DIFFERENT sizes overlap. Which "
                "best describes what happens at that point?",
        "options": [
            {"text": "The two partly cancel, leaving a displacement in "
                     "the direction of the larger one", "correct": True},
            {"text": "The two add together to make an even bigger crest", "correct": False,
             "why": "A crest and a trough push the surface opposite "
                    "ways, so they partly cancel rather than adding to a "
                    "bigger crest."},
            {"text": "The two cancel completely, leaving flat water", "correct": False,
             "why": "Complete cancelling only happens when the crest "
                    "and trough are exactly the same size — here they are "
                    "different."},
            {"text": "Nothing happens, since a crest and a trough "
                     "cannot meet at the same point", "correct": False,
             "why": "A crest and a trough can perfectly well arrive at "
                    "the same point at the same moment — that is exactly when "
                    "superposition applies."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e28",
        "band": "easier",
        "text": "A wave is sent towards a wall and completely absorbed by "
                "padding on the wall, rather than bouncing back. Has this "
                "wave reflected?",
        "options": [
            {"text": "Yes — hitting a wall always counts as reflecting",
             "correct": False,
             "why": "Reflecting specifically means bouncing back. A wave "
                    "that is absorbed and does not bounce back has not "
                    "reflected."},
            {"text": "No — reflection means bouncing back, and this "
                     "wave has not bounced back at all", "correct": True},
            {"text": "Only partly, since some trace of the wave must "
                     "always survive at the wall", "correct": False,
             "why": "The wave is stated to be completely absorbed, so "
                    "there is no bounced-back wave at all, partial or "
                    "otherwise."},
            {"text": "It depends on the wave's amplitude", "correct": False,
             "why": "Whether a wave reflects or is absorbed depends on "
                    "the padding at the wall, not on the amplitude of "
                    "the wave itself."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e29",
        "band": "easier",
        "text": "Two wave trains overlap perfectly, crest on crest, "
                "both amplitude 4 mm. Immediately after they separate again, "
                "what is each wave's amplitude?",
        "options": [
            {"text": "8 mm each, since overlapping doubled them both", "correct": False,
             "why": "The 8 mm reading only exists while the two "
                    "overlap. Once apart, each wave is back to its own "
                    "original amplitude."},
            {"text": "0 mm each, since overlapping used up their "
                     "amplitude", "correct": False,
             "why": "Overlapping does not use anything up — both waves "
                    "carry on afterwards exactly as they were before."},
            {"text": "4 mm each, unchanged", "correct": True},
            {"text": "It cannot be told without knowing the wavelength", "correct": False,
             "why": "Each wave's amplitude after separating depends "
                    "only on what it was before; wavelength does not come into "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-e30",
        "band": "easier",
        "text": "A wave's crest is measured 6 mm above the still level "
                "after reflecting off a wall, matching its 6 mm before "
                "reflecting. What has this measurement confirmed?",
        "options": [
            {"text": "That the wall must be exactly 6 mm tall", "correct": False,
             "why": "The height of the wall has nothing to do with the "
                    "wave's own amplitude reading."},
            {"text": "That the wave has stopped travelling and is now "
                     "standing still", "correct": False,
             "why": "A matching amplitude before and after says nothing "
                    "about the wave stopping — it is still travelling, just in "
                    "a new direction."},
            {"text": "That the wave's wavelength must also have doubled", "correct": False,
             "why": "An unchanged amplitude reading says nothing about "
                    "the wavelength; reflection leaves that unchanged too, but "
                    "this measurement alone does not show that."},
            {"text": "That reflecting off the wall has not changed the "
                     "wave's amplitude", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p6-02-s14",
        "band": "standard",
        "text": "Two paddles generate crests of 12 mm and 7 mm, and by "
                "chance the two happen to arrive at exactly the same spot in "
                "the tank at the same instant. What is the water's displacement "
                "at that spot?",
        "options": [
            {"text": "5 mm", "correct": False,
             "why": "That subtracts the two. Two crests both lift the "
                    "surface the same way, so they add."},
            {"text": "84 mm", "correct": False,
             "why": "That multiplies 12 by 7. Superposition adds "
                    "displacements; it does not multiply them."},
            {"text": "12 mm, since the larger crest dominates the "
                     "smaller one", "correct": False,
             "why": "Neither crest is ignored — both contribute to the "
                    "total, which is why the two are added together."},
            {"text": "19 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s15",
        "band": "standard",
        "text": "At one spot in a channel, a 15 mm crest from one wave "
                "train overlaps with a 9 mm trough from another. What is the "
                "displacement at that spot?",
        "options": [
            {"text": "6 mm upwards", "correct": True},
            {"text": "24 mm upwards", "correct": False,
             "why": "That adds the two as though both were crests. A "
                    "crest and a trough work against each other instead."},
            {"text": "6 mm downwards", "correct": False,
             "why": "The size is right, but the crest is the larger of "
                    "the two, so the net displacement points upwards."},
            {"text": "0 mm, since a crest and a trough always cancel "
                     "completely", "correct": False,
             "why": "Complete cancelling only happens when the crest "
                    "and trough are the same size — here 15 mm and 9 mm are "
                    "different."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s16",
        "band": "standard",
        "text": "At one instant, a point's displacement due to one wave "
                "is 6 mm above the still level. A second, independent "
                "wave, overlapping at that same instant, contributes a "
                "further 10 mm below the still level. Taking upward as "
                "positive, what is the point's overall displacement?",
        "options": [
            {"text": "+16 mm", "correct": False,
             "why": "That adds the two sizes without using the negative "
                    "sign on the second wave."},
            {"text": "−4 mm", "correct": True},
            {"text": "+4 mm", "correct": False,
             "why": "The size is right, but the larger of the two "
                    "values is negative, so the total should be "
                    "negative too."},
            {"text": "−16 mm", "correct": False,
             "why": "That adds the two sizes as though both were "
                    "negative, ignoring the +6 mm's positive sign."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s17",
        "band": "standard",
        "text": "A canal lock gate briefly acts as a wall for a wave "
                "train inside the lock. A wave of amplitude 5 mm reflects off "
                "it and, further along, meets a second, separate wave of "
                "amplitude 5 mm arriving crest on crest. What is the peak "
                "displacement where they meet?",
        "options": [
            {"text": "5 mm", "correct": False,
             "why": "That only counts one of the two waves. Both are "
                    "present at the point and both contribute."},
            {"text": "25 mm", "correct": False,
             "why": "That multiplies the two amplitudes together, which "
                    "is not what superposition does."},
            {"text": "10 mm", "correct": True},
            {"text": "0 mm, since reflecting off the gate cancels the "
                     "wave", "correct": False,
             "why": "Reflecting off the gate does not cancel the wave — "
                    "it bounces back with the same amplitude, ready to add to "
                    "the second wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s18",
        "band": "standard",
        "text": "Two wave trains, both amplitude 4 mm, arrive at a "
                "point exactly crest on trough. What is the displacement there, "
                "and does this permanently use up either wave's energy?",
        "options": [
            {"text": "8 mm, and yes — the overlap permanently combines "
                     "their energy into one wave", "correct": False,
             "why": "Crest on trough with equal amplitudes cancels to 0 "
                    "mm, not 8 mm, and neither wave's energy is used up "
                    "permanently."},
            {"text": "0 mm, and yes — the cancelling uses up both "
                     "waves' energy for good", "correct": False,
             "why": "Cancelling only lasts while the two overlap; both "
                    "waves carry on afterwards with their own energy "
                    "unchanged."},
            {"text": "4 mm, and no — only half of one wave's energy is "
                     "used up", "correct": False,
             "why": "Equal crest and trough cancel completely, to 0 mm, "
                    "not to 4 mm."},
            {"text": "0 mm, and no — both waves keep their own energy "
                     "and carry on afterwards", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s19",
        "band": "standard",
        "text": "A pulse in a rope is sent towards a wall and reflects. "
                "It takes 2 seconds to reach the wall. Roughly how long does "
                "the return journey take, assuming nothing about its speed has "
                "changed?",
        "options": [
            {"text": "2 seconds", "correct": True},
            {"text": "1 second, since the return trip is always faster", "correct": False,
             "why": "Nothing about reflecting makes a pulse travel "
                    "faster on the way back; its speed is unchanged."},
            {"text": "4 seconds, since bouncing off the wall slows it "
                     "down", "correct": False,
             "why": "Reflecting off a wall does not slow a pulse down; "
                    "its speed stays the same in both directions."},
            {"text": "It cannot be estimated without knowing the "
                     "pulse's amplitude", "correct": False,
             "why": "Travel time depends on distance and speed, not on "
                    "amplitude, and both distance and speed are the same for "
                    "the return trip."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s20",
        "band": "standard",
        "text": "Two paddles at either end of a long tank both send "
                "identical wave trains toward the middle, timed to meet "
                "crest on crest. One paddle is then switched off. What "
                "happens to the wave pattern in the middle?",
        "options": [
            {"text": "It stays exactly the same as before, since one "
                     "wave travelling alone always carries the very "
                     "same pattern that two overlapping waves together "
                     "would have produced", "correct": False,
             "why": "With only one paddle running, there is no second "
                    "wave left to add to — the crest-on-crest addition "
                    "stops."},
            {"text": "Only the wave from the remaining paddle is left; "
                     "the crest-on-crest addition stops because there "
                     "is now only one wave", "correct": True},
            {"text": "The middle of the tank goes completely flat, "
                     "since half the source has been removed",
             "correct": False,
             "why": "The remaining paddle is still sending in a wave, "
                    "so the water is not flat — it simply shows that "
                    "one wave on its own."},
            {"text": "The remaining wave doubles in amplitude to make up "
                     "for the missing paddle", "correct": False,
             "why": "A wave's amplitude is set by its own paddle; "
                    "switching off a different paddle does not change "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s21",
        "band": "standard",
        "text": "A wave of amplitude 6 mm reflects off a wall and meets "
                "the still-incoming wave of amplitude 6 mm exactly crest on "
                "crest at one point, and exactly crest on trough at a second "
                "point further along the channel. What is the displacement at "
                "each of these two points?",
        "options": [
            {"text": "6 mm and 6 mm", "correct": False,
             "why": "Both points would only read 6 mm if just one wave "
                    "were present; at each point, both waves overlap."},
            {"text": "12 mm and 6 mm", "correct": False,
             "why": "Crest on trough with equal amplitudes cancels "
                    "completely, to 0 mm, not to 6 mm."},
            {"text": "12 mm and 0 mm", "correct": True},
            {"text": "36 mm and 0 mm", "correct": False,
             "why": "That multiplies the two amplitudes together for "
                    "the first point rather than adding them."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s22",
        "band": "standard",
        "text": "A wave gives a point a displacement of −7 mm. A "
                "second, independent wave gives that same point +7 mm at the "
                "same moment. What is the total displacement, and what does "
                "this show about the two waves' sizes at that instant?",
        "options": [
            {"text": "14 mm; it shows the two waves have very different "
                     "sizes", "correct": False,
             "why": "Adding −7 and +7 gives 0 mm, not 14 mm — the two "
                    "displacements are equal in size but opposite in sign, "
                    "which is why they cancel."},
            {"text": "−14 mm; it shows both waves are pushing the "
                     "surface downward at that point", "correct": False,
             "why": "One of the two displacements is positive, so they "
                    "are not both pushing the same way — they cancel instead."},
            {"text": "It cannot be found without knowing each wave's "
                     "wavelength", "correct": False,
             "why": "Adding the two displacements needs only the two "
                    "values given; wavelength plays no part in it."},
            {"text": "0 mm; it shows the two are contributing equally "
                     "sized, opposite displacements at that point", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s23",
        "band": "standard",
        "text": "Two wave trains, amplitude 8 mm and 3 mm, arrive at a "
                "point. A student calculates the displacement there as "
                "8 × 3 = 24 mm. What has gone wrong?",
        "options": [
            {"text": "Superposition adds the two displacements; it does "
                     "not multiply them. The correct total is 8 + 3 = "
                     "11 mm crest on crest, or 8 − 3 = 5 mm crest on "
                     "trough", "correct": True},
            {"text": "Nothing has gone wrong — multiplying is exactly "
                     "how superposition combines two waves",
             "correct": False,
             "why": "Superposition adds displacements together; "
                    "multiplying two amplitudes would give an area-like "
                    "quantity, not a height."},
            {"text": "The student should have multiplied and then "
                     "halved the result, giving 12 mm", "correct": False,
             "why": "Halving a multiplied result is still multiplying — "
                    "the correct operation is addition, not any form of "
                    "multiplication."},
            {"text": "The error is only in the units used, not in the "
                     "arithmetic itself — 24 mm should really have been "
                     "written down and reported instead as 24 square "
                     "millimetres", "correct": False,
             "why": "The problem is the operation used, not the units — "
                    "multiplying two amplitudes is the wrong step "
                    "regardless of how the answer is labelled."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s24",
        "band": "standard",
        "text": "A wave of amplitude 9 mm and a second wave of "
                "amplitude 9 mm meet, giving a displacement of 18 mm at a "
                "point. A student says this proves the two waves are arriving "
                "exactly crest on crest. Is this reasoning sound?",
        "options": [
            {"text": "No — 18 mm could just as easily happen with the "
                     "two waves crest on trough", "correct": False,
             "why": "Crest on trough with equal 9 mm amplitudes cancels "
                    "to 0 mm, nowhere near 18 mm."},
            {"text": "Yes — 18 mm is the maximum the two waves could "
                     "ever add up to, and that only happens when both crests "
                     "line up exactly", "correct": True},
            {"text": "No — the displacement says nothing at all about "
                     "how the two waves are lined up", "correct": False,
             "why": "The displacement is exactly what tells you how the "
                    "waves are lined up here, since 18 mm is only reachable "
                    "one way with these amplitudes."},
            {"text": "It cannot be judged without knowing the "
                     "wavelength of each wave", "correct": False,
             "why": "The two given amplitudes and the reading of 18 mm "
                    "are already enough to settle this, without needing the "
                    "wavelength."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s25",
        "band": "standard",
        "text": "A wave pulse travels 1.5 m along a channel to reach a "
                "wall, reflects, and travels back to its starting point. If its "
                "speed stays at 0.75 m/s throughout, how long does the whole "
                "round trip take?",
        "options": [
            {"text": "2.0 s", "correct": False,
             "why": "That only covers the outward 1.5 m leg. The pulse "
                    "also has to travel 1.5 m back again."},
            {"text": "1.125 s", "correct": False,
             "why": "That multiplies the outward 1.5 m by the speed "
                    "instead of dividing the total 3.0 m by it."},
            {"text": "4.0 s", "correct": True},
            {"text": "It cannot be found without knowing the pulse's "
                     "amplitude", "correct": False,
             "why": "Travel time comes from distance and speed alone; "
                    "amplitude plays no part in it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s26",
        "band": "standard",
        "text": "A ripple tank shows two wave trains overlapping. At a "
                "labelled point, one trace reads +12 mm and the total combined "
                "trace reads +7 mm. What must the second wave train's "
                "displacement be at that point?",
        "options": [
            {"text": "+19 mm", "correct": False,
             "why": "That adds the two readings together rather than "
                    "working out what the second wave must be adding to the "
                    "first."},
            {"text": "+5 mm", "correct": False,
             "why": "The size is right, but +12 and +5 would add to +17 "
                    "mm, not the +7 mm actually measured."},
            {"text": "+7 mm, the same as the combined reading", "correct": False,
             "why": "If the second wave alone gave +7 mm, the combined "
                    "reading with the first wave's +12 mm would be +19 mm, not "
                    "+7 mm."},
            {"text": "−5 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s27",
        "band": "standard",
        "text": "A crest of 10 mm and a trough of 6 mm overlap. A "
                "student says the result must be a trough of 4 mm, "
                "since a trough was one of the two waves involved. Is "
                "the student's conclusion right?",
        "options": [
            {"text": "The size is right (4 mm), but the direction is "
                     "wrong: the crest is the larger of the two, so the "
                     "net displacement points upward, not downward",
             "correct": True},
            {"text": "Yes, completely — both the size and the direction "
                     "are correct", "correct": False,
             "why": "The size, 4 mm, is right, but the direction is "
                    "not — the larger wave here is the crest, so the "
                    "result points upward."},
            {"text": "No — the size should be 16 mm, not 4 mm",
             "correct": False,
             "why": "16 mm would be crest on crest. A crest overlapping "
                    "a trough gives the DIFFERENCE of the two sizes, "
                    "which is 4 mm."},
            {"text": "No — a crest and a trough of genuinely different "
                     "sizes can never actually be combined at all, "
                     "whatever their two individual sizes happen to be "
                     "in a given case like this one", "correct": False,
             "why": "A crest and a trough of different sizes combine "
                    "perfectly well — superposition adds their two "
                    "displacements just as it would for any pair."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s28",
        "band": "standard",
        "text": "A wave train of amplitude 6 mm meets its own "
                "reflection, also 6 mm, and a gauge sitting in the overlap "
                "reads 12 mm. A second gauge further along the channel, past "
                "the overlap, reads the incoming train on its own. What does "
                "that second gauge read?",
        "options": [
            {"text": "12 mm, the same as the first gauge", "correct": False,
             "why": "The 12 mm reading exists only where the two trains "
                    "overlap and add. On its own the incoming train is still 6 "
                    "mm."},
            {"text": "6 mm", "correct": True},
            {"text": "0 mm, since the overlap used the wave up", "correct": False,
             "why": "Overlapping uses nothing up — each train leaves "
                    "the overlap carrying the amplitude it arrived with."},
            {"text": "It cannot be read without knowing the wavelength", "correct": False,
             "why": "The incoming train's own amplitude is 6 mm "
                    "whatever its wavelength; nothing more is needed to read "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s29",
        "band": "standard",
        "text": "A canal lock gate reflects a wave train of wavelength "
                "0.8 m straight back the way it came. What is the wavelength of "
                "the reflected wave, and has its speed changed?",
        "options": [
            {"text": "0.4 m, and yes, the speed has halved", "correct": False,
             "why": "Reflecting off a solid gate changes neither the "
                    "wavelength nor the speed — only the direction of travel."},
            {"text": "1.6 m, and no, the speed has not changed", "correct": False,
             "why": "The wavelength stays at 0.8 m; reflecting off a "
                    "gate does not double it."},
            {"text": "0.8 m, and no, the speed has not changed", "correct": True},
            {"text": "0.8 m, but the speed cannot be known without "
                     "measuring the gate", "correct": False,
             "why": "Reflecting off a solid gate leaves speed unchanged "
                    "regardless of the gate's own size — nothing about the "
                    "gate needs measuring for this."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-s30",
        "band": "standard",
        "text": "Two wave trains overlap. Where they overlap, the "
                "combined displacement is measured as −9 mm. One of the two "
                "waves alone gives −5 mm at that point. What must the other "
                "wave alone be giving at that point?",
        "options": [
            {"text": "−14 mm", "correct": False,
             "why": "That adds the two readings together rather than "
                    "working out what the missing wave must contribute."},
            {"text": "+4 mm", "correct": False,
             "why": "The size is right, but +4 and −5 would add to −1 "
                    "mm, not the −9 mm actually measured."},
            {"text": "−9 mm, the same as the combined reading", "correct": False,
             "why": "If the second wave alone gave −9 mm, the combined "
                    "reading with the first wave's −5 mm would be −14 mm, not "
                    "−9 mm."},
            {"text": "−4 mm", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p6-02-h11",
        "band": "harder",
        "text": "A wave train of amplitude 6 mm reflects off a wall and "
                "overlaps with the incoming wave train, also amplitude 6 mm "
                "with the same wavelength, at a fixed point where they always "
                "arrive crest on crest. The source amplitude is then increased "
                "so both the incoming and reflected waves become 9 mm each, "
                "without changing the wavelength. What is the new maximum "
                "displacement at this fixed point?",
        "options": [
            {"text": "18 mm", "correct": True},
            {"text": "12 mm, unchanged from before", "correct": False,
             "why": "12 mm was the OLD maximum, from 6 + 6. Increasing "
                    "each wave to 9 mm changes the total too."},
            {"text": "81 mm", "correct": False,
             "why": "That multiplies 9 by 9. Superposition adds "
                    "displacements; it does not multiply them."},
            {"text": "9 mm, since only one of the two waves is really "
                     "acting at the point", "correct": False,
             "why": "Both the incoming and reflected waves act on the "
                    "point at once, which is why their two displacements are "
                    "added together."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h12",
        "band": "harder",
        "text": "A student says: 'reflecting a wave off a wall must "
                "remove some of its energy, because the wave has to be "
                "turned right around.' Assess this claim.",
        "options": [
            {"text": "The claim is right — turning any wave around to "
                     "send it back the way it came always costs it a "
                     "noticeable share of its own energy, whatever kind "
                     "of barrier is doing the turning", "correct": False,
             "why": "A wave reflecting off a solid wall can bounce back "
                    "with its amplitude, and so its energy, unchanged."},
            {"text": "The claim is wrong: a wave reflecting off a solid "
                     "wall can bounce back with its amplitude — and so "
                     "its energy — unchanged; turning around does not, "
                     "by itself, remove energy", "correct": True},
            {"text": "The claim is right, but only for waves travelling "
                     "faster than about 1 m/s", "correct": False,
             "why": "There is no such speed threshold — reflecting off "
                    "a solid wall does not remove energy at any speed."},
            {"text": "It cannot be judged without knowing the wall's "
                     "own thickness", "correct": False,
             "why": "The wall's thickness is not what decides this — a "
                    "wave reflecting off a solid wall keeps its "
                    "amplitude regardless."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h13",
        "band": "harder",
        "text": "A wave of amplitude 14 mm meets its own reflection, "
                "also 14 mm and the same wavelength, exactly crest on crest at "
                "point P. At point Q, exactly a quarter of a wavelength further "
                "along the channel from P, what is the displacement, and why?",
        "options": [
            {"text": "28 mm, since both points share the same two waves", "correct": False,
             "why": "Sharing the same two waves does not mean sharing "
                    "the same result — a quarter of a wavelength along, the "
                    "crest-trough relationship between the two waves is "
                    "different from at P."},
            {"text": "14 mm, since only one of the two waves reaches Q", "correct": False,
             "why": "Both waves fill the whole channel, so both reach Q "
                    "just as they reach P."},
            {"text": "0 mm, because a quarter of a wavelength from a "
                     "crest-on-crest point puts the two waves crest on trough "
                     "instead", "correct": True},
            {"text": "It cannot be found without knowing the exact "
                     "distance from the wall to P", "correct": False,
             "why": "Knowing the OFFSET between P and Q — a quarter of "
                    "a wavelength — is enough on its own to work out the "
                    "displacement at Q."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h14",
        "band": "harder",
        "text": "A crest of 20 mm meets a trough of 8 mm at a point. A "
                "student says: 'the result must be 8 mm in the direction of the "
                "smaller wave, since the smaller one determines how much is "
                "left over.' Assess this claim.",
        "options": [
            {"text": "The claim is right about the stated size of 8 mm, "
                     "but it has got the direction of the net displacement "
                     "completely wrong", "correct": False,
             "why": "The size is also wrong — 20 minus 8 gives 12 mm, "
                    "not the 8 mm the claim states."},
            {"text": "The claim is right about the direction but wrong "
                     "about the size", "correct": False,
             "why": "The direction is also wrong — the net displacement "
                    "follows the larger wave, the 20 mm crest, not the smaller "
                    "trough."},
            {"text": "The claim is entirely correct", "correct": False,
             "why": "Both the stated size (8 mm) and the stated "
                    "direction (following the smaller wave) are wrong."},
            {"text": "The claim is wrong on both counts: the size is 12 "
                     "mm (20 minus 8), and the direction follows the LARGER "
                     "wave, not the smaller one", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h15",
        "band": "harder",
        "text": "A wave pulse travels at 0.6 m/s down a channel. It is "
                "sent 1.2 m to a wall, reflects instantly, and returns "
                "past its start point exactly 4.0 s after being sent. "
                "What does this timing show about the wave's speed on "
                "the return journey?",
        "options": [
            {"text": "It shows the return speed matches the outward "
                     "speed: 1.2 m + 1.2 m at 0.6 m/s takes exactly "
                     "4.0 s, with nothing left over to explain",
             "correct": True},
            {"text": "It shows the return journey home must have been "
                     "noticeably faster than the outward journey to the "
                     "wall, even though the pulse's speed was said to "
                     "stay the same throughout", "correct": False,
             "why": "4.0 s is exactly what 2.4 m at a steady 0.6 m/s "
                    "gives — there is no unexplained extra time pointing "
                    "to a faster return."},
            {"text": "It shows the wall must have delayed the pulse by "
                     "a full second", "correct": False,
             "why": "The whole 2.4 m round trip at 0.6 m/s takes exactly "
                    "4.0 s with no delay needed to explain the timing."},
            {"text": "Nothing can be concluded without knowing the "
                     "pulse's amplitude", "correct": False,
             "why": "Travel time depends on distance and speed alone; "
                    "amplitude plays no part in this calculation."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h16",
        "band": "harder",
        "text": "Wave A (amplitude 10 mm) meets Wave B (amplitude 10 "
                "mm) crest on crest at point P, giving 20 mm. At point Q, a "
                "different pair — Wave C (amplitude 15 mm) and Wave D "
                "(amplitude 5 mm) — meet crest on crest, also giving 20 mm. A "
                "student says the water is doing exactly the same thing at P "
                "and Q. Assess this.",
        "options": [
            {"text": "The claim is wrong — 20 mm from a 10-and-10 pair "
                     "is a fundamentally different height from 20 mm from a "
                     "15-and-5 pair", "correct": False,
             "why": "A displacement of 20 mm is a displacement of 20 "
                    "mm, whatever pair of waves produced it — the water's "
                    "height at that instant is identical."},
            {"text": "The claim is right: the peak displacement is the "
                     "same at both points, so at that instant the water surface "
                     "really is at the same height at P and Q, even though two "
                     "different pairs of waves produce it", "correct": True},
            {"text": "The claim is wrong, because Wave C and Wave D "
                     "must actually be arriving crest on trough, not crest on "
                     "crest", "correct": False,
             "why": "The question states both pairs meet crest on "
                    "crest; nothing suggests Wave C and Wave D are actually "
                    "out of step."},
            {"text": "It cannot be judged without knowing each wave's "
                     "wavelength", "correct": False,
             "why": "The peak displacement at each point is decided by "
                    "the amplitudes involved; wavelength is not needed to "
                    "compare the two readings."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h17",
        "band": "harder",
        "text": "A wave of amplitude 13 mm and wavelength 50 cm "
                "reflects off a wall, arriving back with its wavelength "
                "unchanged. A second wave of amplitude 13 mm and wavelength 25 "
                "cm is sent in from the opposite end, overlapping with the "
                "first. At the instant both happen to be at a crest at the same "
                "point, what is the maximum possible displacement there?",
        "options": [
            {"text": "13 mm, since only waves of matching wavelength "
                     "can really add together", "correct": False,
             "why": "Superposition adds whatever displacements are "
                    "present at a point, whether or not the two wavelengths "
                    "match."},
            {"text": "169 mm", "correct": False,
             "why": "That multiplies the two amplitudes together, which "
                    "is not what superposition does."},
            {"text": "26 mm", "correct": True},
            {"text": "It cannot be found, since the two different "
                     "wavelengths make the addition invalid", "correct": False,
             "why": "The two amplitudes are enough to answer this — "
                    "whether the wavelengths match affects whether a PERMANENT "
                    "pattern forms, not whether this single instant's addition "
                    "is valid."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h18",
        "band": "harder",
        "text": "A wave of amplitude 12 mm and a wave of amplitude 5 mm "
                "can combine to give a maximum of 17 mm (crest on crest) and a "
                "minimum of 7 mm (crest on trough). A student measures a "
                "displacement of 3 mm at one instant and says this must be a "
                "measurement error, since 3 mm falls outside both of these "
                "values. Assess this claim.",
        "options": [
            {"text": "The claim is wrong — 3 mm is a perfectly ordinary "
                     "and thoroughly unremarkable reading for these two "
                     "particular waves, sitting comfortably well within the "
                     "whole range they are able to produce together", "correct": False,
             "why": "3 mm is below the 7 mm lower limit these two "
                    "amplitudes can produce (12 minus 5), so it does sit "
                    "outside the expected range."},
            {"text": "The claim cannot be assessed without knowing "
                     "which instrument measured the 3 mm reading", "correct": False,
             "why": "The two given amplitudes alone are enough to work "
                    "out the expected range and compare the reading against "
                    "it."},
            {"text": "The claim is wrong, because a displacement can "
                     "take any value at all, however large or small, whatever "
                     "the two amplitudes happen to be", "correct": False,
             "why": "The two amplitudes fix a definite range, 7 mm to "
                    "17 mm here — the displacement cannot fall outside it."},
            {"text": "The claim is right to be suspicious: with these "
                     "two amplitudes, the displacement at any instant should lie "
                     "between 7 mm and 17 mm, so a reading of 3 mm does suggest "
                     "an error somewhere", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h19",
        "band": "harder",
        "text": "A student suggests that since two identical waves "
                "crest-on-crest give double the amplitude, three "
                "identical waves overlapping crest on crest at the same "
                "point must give TRIPLE the amplitude. Using the "
                "definition of superposition, assess this claim.",
        "options": [
            {"text": "The claim is right: superposition adds the "
                     "displacement of every wave present at a point, "
                     "so three identical crests of amplitude a add to "
                     "3a, following the same rule as for two",
             "correct": True},
            {"text": "The claim is wrong — superposition only ever "
                     "genuinely works for exactly two overlapping waves "
                     "at any one time, so a third wave simply cannot be "
                     "added into the very same calculation at all",
             "correct": False,
             "why": "Nothing limits superposition to two waves; the "
                    "surface simply takes the sum of however many "
                    "waves are present at that point."},
            {"text": "The claim is wrong, because adding a third "
                     "identical wave always cancels one of the "
                     "existing two out", "correct": False,
             "why": "Three crests arriving together all push the "
                    "surface the same way; nothing about a third crest "
                    "cancels an existing one."},
            {"text": "It cannot be judged without knowing the "
                     "wavelength shared by all three waves",
             "correct": False,
             "why": "Adding three equal displacements together needs "
                    "only their amplitude; wavelength plays no part in "
                    "this particular sum."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h20",
        "band": "harder",
        "text": "Two paddles at either end of a tank generate wave "
                "trains of amplitude 6 mm each, timed so they meet "
                "crest on crest at the exact centre. A third paddle is "
                "then added at the centre itself, injecting a further "
                "wave of amplitude 6 mm in step with the other two. "
                "What is the new maximum displacement at the centre?",
        "options": [
            {"text": "12 mm, unchanged, since the third paddle sits "
                     "exactly at the point being measured",
             "correct": False,
             "why": "A wave from a paddle AT the point being measured "
                    "still contributes its own displacement there, just "
                    "like the other two."},
            {"text": "18 mm", "correct": True},
            {"text": "216 mm", "correct": False,
             "why": "That multiplies 6 by 6 by 6, which is not how "
                    "superposition combines several waves."},
            {"text": "6 mm, since only the newest paddle's wave counts "
                     "at its own starting point", "correct": False,
             "why": "All three waves reach the centre and all three "
                    "contribute their own displacement there — none of "
                    "them is left out."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h21",
        "band": "harder",
        "text": "A wave of amplitude 10 mm reflects off a wall, and, "
                "further back down the channel, is found to have an amplitude "
                "of only 6 mm once it returns to the point it started from. A "
                "student says this must mean reflection has removed 4 mm worth "
                "of amplitude from the wave. Assess this claim.",
        "options": [
            {"text": "The claim is right — reflecting off any solid "
                     "wall, whatever it happens to be made of, always takes away "
                     "exactly the same fixed amount of amplitude from any wave "
                     "that bounces off it, every single time this happens", "correct": False,
             "why": "Reflecting off a solid wall does not, on its own, "
                    "reduce amplitude at all, let alone by a fixed fraction "
                    "each time."},
            {"text": "The claim is right, but only because 10 mm and 6 "
                     "mm are both even numbers", "correct": False,
             "why": "Whether the two numbers happen to be even has no "
                    "bearing on what caused the amplitude to drop."},
            {"text": "The claim overreaches: reflecting off a solid "
                     "wall does not, by itself, reduce a wave's amplitude — "
                     "something else, such as the channel absorbing some energy "
                     "along the way, is a more likely explanation for the drop", "correct": True},
            {"text": "It cannot be judged, because amplitude can never "
                     "change for any reason once a wave has been created", "correct": False,
             "why": "Amplitude certainly can change along a real "
                    "channel — through absorption, for instance — which is "
                    "exactly the kind of explanation worth considering here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h22",
        "band": "harder",
        "text": "A wave train partially overlaps with its own "
                "reflection along a stretch of channel 2.4 m long. The "
                "wavelength is 0.6 m. How many complete wavelengths fit into "
                "this stretch?",
        "options": [
            {"text": "3", "correct": False,
             "why": "3 wavelengths of 0.6 m would only span 1.8 m, "
                    "short of the 2.4 m stretch given."},
            {"text": "6", "correct": False,
             "why": "6 wavelengths of 0.6 m would span 3.6 m, more than "
                    "the 2.4 m stretch given."},
            {"text": "It cannot be found without knowing the amplitude", "correct": False,
             "why": "Fitting wavelengths into a length only needs the "
                    "wavelength and the length; amplitude plays no part in it."},
            {"text": "4", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h23",
        "band": "harder",
        "text": "A wave of amplitude 8 mm is at a crest at point P. A "
                "second wave overlaps it there, yet the combined displacement "
                "at P is measured as 8 mm — the SAME as the first wave's own "
                "amplitude. What must be true of the second wave at P at that "
                "instant?",
        "options": [
            {"text": "Its displacement there must be 0 mm at that "
                     "instant", "correct": True},
            {"text": "Its amplitude must also be exactly 8 mm", "correct": False,
             "why": "If the second wave were also contributing 8 mm "
                    "upward there, the total would be 16 mm, not the 8 mm "
                    "actually measured."},
            {"text": "It must be travelling in the opposite direction "
                     "to the first wave", "correct": False,
             "why": "Which direction the second wave travels in is not "
                    "what decides its displacement at this point; only its own "
                    "contribution being zero explains the reading."},
            {"text": "It cannot be a real wave at all, since it is "
                     "adding nothing to the total", "correct": False,
             "why": "A wave can be genuinely present and simply be "
                    "contributing zero displacement at this particular point "
                    "and instant."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h24",
        "band": "harder",
        "text": "A wave train's amplitude is doubled and its wavelength "
                "is halved before it reflects off a wall. Compared with before "
                "these changes, what is the reflected wave's new amplitude and "
                "wavelength?",
        "options": [
            {"text": "Amplitude and wavelength both back to their "
                     "original values, since reflecting always undoes any "
                     "earlier changes", "correct": False,
             "why": "Reflecting off a wall does not undo earlier "
                    "changes — it simply carries whatever amplitude and "
                    "wavelength the wave already has."},
            {"text": "Amplitude doubled, wavelength halved — reflecting "
                     "a wave changes its direction only, not its amplitude or "
                     "its wavelength", "correct": True},
            {"text": "Amplitude unchanged from before the doubling, "
                     "wavelength halved again", "correct": False,
             "why": "Reflecting does not touch amplitude or wavelength "
                    "at all — both stay exactly as they were set before "
                    "reaching the wall."},
            {"text": "It cannot be found without knowing the distance "
                     "to the wall", "correct": False,
             "why": "Distance to the wall affects only the timing of "
                    "the bounce, not the amplitude or wavelength of the "
                    "reflected wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h25",
        "band": "harder",
        "text": "A wave of amplitude 6 mm and a second wave, also "
                "amplitude 6 mm, are sent along a channel from opposite ends, "
                "timed to meet crest on crest at the centre. If the SECOND "
                "wave's amplitude is then increased to 10 mm, with nothing else "
                "changed, what is the new displacement at the centre?",
        "options": [
            {"text": "12 mm, unchanged", "correct": False,
             "why": "12 mm was the total before the second wave's "
                    "amplitude changed. Increasing it to 10 mm changes the "
                    "total too."},
            {"text": "60 mm", "correct": False,
             "why": "That multiplies 6 by 10, which is not how "
                    "superposition combines two waves."},
            {"text": "16 mm", "correct": True},
            {"text": "10 mm, since the larger wave now dominates "
                     "completely", "correct": False,
             "why": "Both waves still contribute at the point; the "
                    "smaller wave's 6 mm is not dropped from the total."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h26",
        "band": "harder",
        "text": "A wave of amplitude 8 mm meets its reflection, also 8 "
                "mm, crest on trough at point P, giving 0 mm. The source "
                "amplitude is then increased so both the incoming and reflected "
                "waves become 11 mm each. What is the new displacement at P?",
        "options": [
            {"text": "22 mm, since both amplitudes increased", "correct": False,
             "why": "22 mm would be crest on crest with two 11 mm "
                    "waves. At P the two waves are still crest on trough."},
            {"text": "3 mm", "correct": False,
             "why": "Equal amplitudes meeting crest on trough cancel "
                    "completely, to 0 mm, whatever that equal size happens to "
                    "be."},
            {"text": "It cannot be found without knowing the new "
                     "wavelength", "correct": False,
             "why": "Whether two equal-and-opposite displacements "
                    "cancel depends only on their sizes being equal, not on "
                    "the wavelength."},
            {"text": "Still 0 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h27",
        "band": "harder",
        "text": "A wave of amplitude 4 mm meets a wave of amplitude "
                "4 mm crest on crest at point P, and a wave of "
                "amplitude 4 mm meets a wave of amplitude 4 mm crest on "
                "trough at point Q. A student says P and Q must be "
                "experiencing the exact opposite of one another, since "
                "one is the maximum possible addition and the other is "
                "the maximum possible cancellation. Assess this claim.",
        "options": [
            {"text": "The claim is right: with equal amplitudes, crest "
                     "on crest gives the largest possible addition "
                     "(8 mm) and crest on trough gives the largest "
                     "possible cancellation (0 mm), the two true "
                     "extremes for this pair", "correct": True},
            {"text": "The claim is wrong — P and Q must actually always "
                     "be reading exactly the same displacement as one "
                     "another at every instant, since both points "
                     "involve the very same pair of 4 mm waves",
             "correct": False,
             "why": "Reading the same displacement would need the same "
                    "crest-trough relationship at both points, and P "
                    "and Q are stated to have different ones."},
            {"text": "The claim is wrong, because crest on trough "
                     "always gives a bigger displacement than crest on "
                     "crest", "correct": False,
             "why": "Crest on trough gives the smallest possible "
                    "displacement for a pair of equal waves, not the "
                    "biggest — that is crest on crest instead."},
            {"text": "It cannot be judged without knowing each wave's "
                     "wavelength", "correct": False,
             "why": "Comparing the two extremes only needs the "
                    "amplitudes; wavelength is not needed for this "
                    "particular comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h28",
        "band": "harder",
        "text": "A wave of amplitude 5 mm and a wave of amplitude 13 mm "
                "overlap. A student lists the possible displacements at any "
                "point as ranging continuously from 8 mm (crest on trough) up "
                "to 18 mm (crest on crest). Is this range correct?",
        "options": [
            {"text": "No — only the two end values, 8 mm and 18 mm, are "
                     "actually possible; nothing in between can occur", "correct": False,
             "why": "Values in between occur whenever the two waves are "
                    "only partly in or out of step — the two extremes are not "
                    "the only possible readings."},
            {"text": "Yes — with these two amplitudes, every value "
                     "between 8 mm and 18 mm is possible, depending on how "
                     "closely the two line up", "correct": True},
            {"text": "No — the range should run from 5 mm to 13 mm, "
                     "matching each wave's own amplitude", "correct": False,
             "why": "5 mm and 13 mm are the two amplitudes themselves, "
                    "not the range of their combined displacement, which runs "
                    "from 8 mm to 18 mm."},
            {"text": "It cannot be judged without knowing the "
                     "wavelength of each wave", "correct": False,
             "why": "The range of possible combined displacements comes "
                    "entirely from the two amplitudes; wavelength plays no "
                    "part in it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h29",
        "band": "harder",
        "text": "Wave X (amplitude 6 mm) and Wave Y (amplitude 6 mm) "
                "meet at point P, giving a combined displacement whose size is "
                "6 mm. A student claims this can only happen if the two waves "
                "are arriving partway out of step, neither fully crest on crest "
                "nor fully crest on trough, since 6 mm is neither the sum (12 "
                "mm) nor the difference (0 mm) of the two amplitudes. Assess "
                "this claim.",
        "options": [
            {"text": "The claim is wrong — a reading of 6 mm can only "
                     "ever happen when the two waves are lined up exactly crest "
                     "on crest, simply because 6 happens to be one of the two "
                     "amplitudes given here", "correct": False,
             "why": "Crest on crest with these two waves gives 12 mm, "
                    "not 6 mm — 6 mm sits between the two extremes instead."},
            {"text": "The claim is wrong — 6 mm can only happen crest "
                     "on trough, since a difference of some kind must always be "
                     "involved", "correct": False,
             "why": "Crest on trough with two equal 6 mm waves cancels "
                    "completely to 0 mm, not 6 mm."},
            {"text": "The claim is right: since 6 mm sits between the "
                     "two extremes of 0 mm and 12 mm, the two waves must be "
                     "arriving partway out of step with each other, not "
                     "perfectly in step or perfectly opposed", "correct": True},
            {"text": "It cannot be judged without knowing each wave's "
                     "wavelength", "correct": False,
             "why": "Judging where 6 mm sits between the two extremes "
                    "only needs the two amplitudes; wavelength is not needed "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-02-h30",
        "band": "harder",
        "text": "A wave train and its reflection, both amplitude 7 mm, "
                "overlap along a channel. At one point the combined reading is "
                "14 mm; at a second point, 0 mm; at a third point, 7 mm. Put "
                "these three points in order from where the two waves are most "
                "in step to where they are most out of step.",
        "options": [
            {"text": "0 mm, then 7 mm, then 14 mm", "correct": False,
             "why": "That runs the order backwards — 0 mm is where the "
                    "two waves are most out of step, not most in step."},
            {"text": "7 mm, then 14 mm, then 0 mm", "correct": False,
             "why": "14 mm, the largest reading, is where the two waves "
                    "are most in step and should come first, not second."},
            {"text": "All three points are equally in step, since the "
                     "same two 7 mm waves are involved at each one", "correct": False,
             "why": "Sharing the same two waves does not mean sharing "
                    "the same crest-trough relationship — the three readings "
                    "show three different degrees of overlap."},
            {"text": "14 mm, then 7 mm, then 0 mm", "correct": True},
        ],
        "figure": None,
    },
]
