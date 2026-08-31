"""P6 lesson 03 — How sound is made: twelve questions (MRB-223).

Written against Design's page. The tuning fork in the water, the four-stage
strip and the vibration chain are hers.

The discriminations, in the order the lesson builds them:

  · the OBJECT vibrates and the air passes it on (`WAVE-09`);
  · too small and too fast to see is still vibrating (`WAVE-10`);
  · a microphone and a loudspeaker run the same chain in opposite
    directions (`WAVE-11`);
  · nothing is stored and released: the sound exists only while something
    is vibrating (`WAVE-12`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — 0,2,3,1 · 3,1,0,2 · 1,3,2,0, three of each.

⚠️ EVERY DISTRACTOR STATES A COMPLETE WRONG RULE. Six sets here had the
correct answer as the longest option by MRB-177's own threshold; the
correct answers are untouched and the short distractors were finished.

⚠️ The ladder's own two marked rungs are NOT restated.
"""

UNIT = "P6"
LESSON = "how-sound-is-made"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p6-03-e01",
        "band": "easier",
        "text": "Every sound starts with…",
        "options": [
            {"text": "something vibrating", "correct": True},
            {"text": "moving air", "correct": False,
             "why": "Air moves in a breeze without making a note. Something "
                    "has to vibrate to start a sound off."},
            {"text": "a loud noise nearby", "correct": False,
             "why": "That only pushes the question back a step: the loud "
                    "noise had to start somewhere too."},
            {"text": "electricity", "correct": False,
             "why": "A drum and a violin use no electricity at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e02",
        "band": "easier",
        "text": "A loudspeaker makes a sound. What is the part that "
                "vibrates?",
        "options": [
            {"text": "the wire carrying the signal", "correct": False,
             "why": "The wire carries the signal to the speaker. It is not "
                    "what pushes the air."},
            {"text": "the air inside the box", "correct": False,
             "why": "The air is pushed by something. The question is what "
                    "pushes it."},
            {"text": "the cone", "correct": True},
            {"text": "the magnet, which stays still", "correct": False,
             "why": "The magnet is deliberately fixed. It is what the moving "
                    "coil pushes against."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e03",
        "band": "easier",
        "text": "A struck tuning fork looks completely still. Which "
                "observation shows it is vibrating?",
        "options": [
            {"text": "It feels cold to the touch when you hold it",
             "correct": False,
             "why": "Metal feels cold whether it has been struck or not."},
            {"text": "It is heavier after it has been struck",
             "correct": False,
             "why": "Nothing has been added to it. Its mass is unchanged."},
            {"text": "It rings on for several seconds afterwards",
             "correct": False,
             "why": "The ringing is the sound itself, which is what is being "
                    "explained. It is not independent evidence."},
            {"text": "Dipping its tip into water throws a spray",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e04",
        "band": "easier",
        "text": "The part of the ear that a sound wave sets vibrating first "
                "is the…",
        "options": [
            {"text": "brain", "correct": False,
             "why": "The brain receives signals from the ear. Nothing "
                    "vibrates it."},
            {"text": "eardrum", "correct": True},
            {"text": "outer flap of the ear", "correct": False,
             "why": "The flap gathers sound and guides it inwards, but it is "
                    "not the membrane that is set vibrating."},
            {"text": "throat", "correct": False,
             "why": "The throat is used for making sound, not for detecting "
                    "it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p6-03-s01",
        "band": "standard",
        "text": "A microphone and a loudspeaker are built from very similar "
                "parts. What is the relationship between them?",
        "options": [
            {"text": "A microphone is a small, quiet loudspeaker, and the "
                     "size of the parts inside is the whole of the "
                     "difference between them", "correct": False,
             "why": "Size and loudness are not the difference. A microphone "
                    "the size of a speaker would still be a microphone."},
            {"text": "A microphone works on electricity and a loudspeaker "
                     "does not, which is why only one of the two ever has "
                     "to be plugged in",
             "correct": False,
             "why": "Both involve electricity. The difference is which way "
                    "it flows through the chain."},
            {"text": "They are quite unrelated devices that happen to look "
                     "alike, and nothing useful at all follows from the "
                     "resemblance between them",
             "correct": False,
             "why": "The resemblance is not a coincidence — a loudspeaker "
                    "can genuinely be used as a rough microphone."},
            {"text": "They run the same chain in opposite directions: one "
                     "turns electricity into vibration, the other turns "
                     "vibration into electricity", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s02",
        "band": "standard",
        "text": "A guitar string is plucked and then a finger is laid gently "
                "on it. The sound stops at once. Why?",
        "options": [
            {"text": "The finger absorbs the sound that is already out in "
                     "the air around the string", "correct": False,
             "why": "The sound already in the air carries on to your ear "
                    "regardless. What stops is the making of new sound."},
            {"text": "The finger stops the string vibrating, so nothing is "
                     "left to disturb the air", "correct": True},
            {"text": "The finger blocks off the path that the sound was "
                     "taking out to your ear", "correct": False,
             "why": "Sound spreads in every direction. One finger cannot "
                    "block all of them."},
            {"text": "The finger cools the string down, and a cold string "
                     "does not make any sound", "correct": False,
             "why": "Temperature is not what decides it. A cold string "
                    "plucked hard sounds perfectly well."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s03",
        "band": "standard",
        "text": "Put the stages in order for someone hearing a drum: "
                "(1) the eardrum vibrates, (2) the skin of the drum "
                "vibrates, (3) the air is squeezed and released in turn, "
                "(4) signals go to the brain.",
        "options": [
            {"text": "2, 3, 1, 4", "correct": True},
            {"text": "3, 2, 1, 4", "correct": False,
             "why": "The air cannot be squeezed until something squeezes it, "
                    "and that something is the drum skin."},
            {"text": "2, 1, 3, 4", "correct": False,
             "why": "The eardrum cannot move before the disturbance has "
                    "crossed the air to reach it."},
            {"text": "1, 2, 3, 4", "correct": False,
             "why": "This starts at the listener. The chain starts at the "
                    "thing that vibrates."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s04",
        "band": "standard",
        "text": "Someone says the air makes the sound and the object just "
                "gets it going. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong at all — the air really is the "
                     "source of the sound, and the object only ever starts "
                     "it off", "correct": False,
             "why": "Still air makes no sound at all, and the note stops the "
                    "instant the object is stopped."},
            {"text": "The air does nothing at all — the sound reaches you "
                     "on its own, and would cross a room with all the air "
                     "pumped out", "correct": False,
             "why": "This overcorrects. The air is essential: it is what "
                    "carries the disturbance to you."},
            {"text": "The object is the source and the air is the carrier: "
                     "stop the object and the sound stops, and the air is "
                     "still there", "correct": True},
            {"text": "The air only matters for the loud sounds, and a "
                     "quiet one reaches your ear without needing any air "
                     "to carry it", "correct": False,
             "why": "The air carries quiet sounds in exactly the same way. "
                    "Loudness is not what decides it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p6-03-h01",
        "band": "harder",
        "text": "A wine glass is tapped and rings. A student says the sound "
                "was stored in the glass and the tap let it out. What is the "
                "best correction?",
        "options": [
            {"text": "The sound was stored in the air around the glass "
                     "instead, and the tap is what shook it loose from "
                     "there", "correct": False,
             "why": "This moves the storage rather than removing it. Nothing "
                    "anywhere holds a stock of sound."},
            {"text": "Nothing was stored — the tap set the glass vibrating, "
                     "and the sound exists only while the vibration lasts",
             "correct": True},
            {"text": "The sound was stored, but only briefly, so most of "
                     "it had already leaked away before the tap arrived",
             "correct": False,
             "why": "Briefly stored is still stored. Damp the glass with a "
                    "hand and the sound stops instantly, with nothing left "
                    "to come out later."},
            {"text": "The glass makes new sound each time it is looked at, "
                     "and it goes on for as long as anyone is watching",
             "correct": False,
             "why": "Looking has nothing to do with it. The vibration is "
                    "what makes the sound."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h02",
        "band": "harder",
        "text": "A recording is played back through a speaker and sounds like "
                "the original. Trace what has happened to the pattern of the "
                "sound.",
        "options": [
            {"text": "The sound itself was captured, kept and released "
                     "again, completely unchanged from the moment it was "
                     "first made in the room", "correct": False,
             "why": "Nothing of the original sound survives. Only a record "
                    "of its pattern does."},
            {"text": "The recording holds air from the original room and "
                     "releases it when the speaker is switched on, which is "
                     "why a room can be recorded at all",
             "correct": False,
             "why": "No air is stored. A recording is a pattern, not a "
                    "sample of anything physical."},
            {"text": "The speaker guesses at the pattern from the "
                     "instructions it is given, filling in for itself "
                     "whatever the recording lost on the way in",
             "correct": False,
             "why": "There is no guessing. The pattern is copied faithfully "
                    "from what the microphone measured."},
            {"text": "The pattern moved from air, to a diaphragm, to "
                     "electricity, to storage, and then back out through a "
                     "cone into the air again", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h03",
        "band": "harder",
        "text": "A mosquito's wings beat about 600 times a second and you "
                "hear a whine. Your hand waves about twice a second and you "
                "hear nothing. Both are moving air. What is the difference?",
        "options": [
            {"text": "The mosquito is closer to your ear than your hand "
                     "ever gets to it, and closeness is what decides "
                     "whether a moving thing can be heard at all",
             "correct": False,
             "why": "Move the mosquito across the room and you still hear "
                    "it; wave your hand next to your ear and you still hear "
                    "nothing."},
            {"text": "The hand is too big to make a sound, because a large "
                     "surface moves the air too gently to be heard, and "
                     "only something small and light can disturb it enough",
             "correct": False,
             "why": "Large things make sound perfectly well — a drum skin is "
                    "much bigger than a mosquito's wing."},
            {"text": "The mosquito squeezes and releases the air hundreds of "
                     "times a second, which is fast enough for the ear to "
                     "respond to; twice a second is far too slow",
             "correct": True},
            {"text": "The hand moves the air smoothly, and only rough "
                     "movement makes a sound, which is why a tuning fork "
                     "running smoothly of its own accord stays quite "
                     "silent", "correct": False,
             "why": "Smooth and rough is not the distinction. A smoothly "
                    "vibrating tuning fork makes a very clean note."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h04",
        "band": "harder",
        "text": "Why does a loudspeaker cone have to move BOTH outwards and "
                "back, rather than just pushing outwards?",
        "options": [
            {"text": "Because a sound is a repeated squeezing and releasing "
                     "of the air, and a cone that only pushed would give one "
                     "shove and then stop", "correct": True},
            {"text": "Because the cone would fall off its mounting if it "
                     "only ever travelled the one way, and no speaker "
                     "would last a whole evening of use", "correct": False,
             "why": "The mounting is not the reason. The physics of what "
                    "sound is decides it."},
            {"text": "Because moving back is what makes the sound loud, "
                     "and pushing forwards only sets the pitch of the note "
                     "that comes out of it", "correct": False,
             "why": "Loudness comes from how far it moves, not from which "
                    "direction it is going."},
            {"text": "Because the air has to be given time to get out of the "
                     "way before the cone can push it again, and pulling "
                     "back is how that time is made", "correct": False,
             "why": "The air is not being cleared out. It is being squeezed "
                    "and released where it already is."},
        ],
        "figure": None,
    },
]
