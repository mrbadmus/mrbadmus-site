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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-03-e05",
        "band": "easier",
        "text": "A drum is struck and a sound is heard. What is making the "
                "sound?",
        "options": [            {"text": "The drummer's hand", "correct": False,
             "why": "The hand supplies the energy; the vibrating surface is "
                    "what produces the sound."},
            {"text": "The air inside the drum, on its own", "correct": False,
             "why": "The air carries the sound onwards, but the skin is what "
                    "starts it vibrating."},
            {"text": "The stick, which stores the sound and lets it out",
             "correct": False,
             "why": "Nothing stores sound. The stick sets the skin moving and "
                    "the skin does the rest."},
            {"text": "The vibrating drum skin", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e06",
        "band": "easier",
        "text": "What does a microphone turn a vibration into?",
        "options": [            {"text": "A changing electrical signal", "correct": True},
            {"text": "A louder sound", "correct": False,
             "why": "Making a sound louder is a loudspeaker's job, at the "
                    "other end of the chain."},
            {"text": "A beam of light carrying the note", "correct": False,
             "why": "Nothing in a microphone produces light; it produces an "
                    "electrical signal."},
            {"text": "A store of sound to be released later", "correct": False,
             "why": "Sound is never stored; the pattern is passed on as it "
                    "arrives."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-03-s05",
        "band": "standard",
        "text": "A struck tuning fork is dipped into a beaker of water. What "
                "happens, and what does it show?",
        "options": [
            {"text": "The water is thrown about, showing the prongs are "
                     "moving",
             "correct": True},
            {"text": "The water stays still, showing the fork is not "
                     "vibrating",
             "correct": False,
             "why": "The splashing is easy to see, and it is exactly the "
                    "evidence the eye could not get from the fork alone."},
            {"text": "The water heats up, showing sound is a kind of warmth",
             "correct": False,
             "why": "Sound is a disturbance passed between particles, not a "
                    "thermal store."},
            {"text": "The fork stops ringing at once, showing water blocks "
                     "sound",
             "correct": False,
             "why": "It does damp quickly, but what the test shows is the "
                    "movement, not a blocking effect."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s06",
        "band": "standard",
        "text": "A loudspeaker is playing, and a hand is pressed firmly on "
                "the cone. What happens?",
        "options": [            {"text": "The sound gets louder, because the hand adds to the "
                     "push",
             "correct": False,
             "why": "The hand stops the cone rather than helping it; there is "
                    "nothing left to disturb the air."},
            {"text": "The note gets lower, because the cone is now heavier",
             "correct": False,
             "why": "The cone is held still, not merely loaded, so there is "
                    "no note at all."},
            {"text": "The sound carries on, because the signal is still "
                     "arriving",
             "correct": False,
             "why": "The signal arrives, but nothing turns it into a "
                    "disturbance in the air."},
            {"text": "The sound stops, because the cone can no longer "
                     "vibrate",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-03-h05",
        "band": "harder",
        "text": "Why does a note stop the instant a ringing object is "
                "gripped, rather than fading away over seconds?",
        "options": [
            {"text": "Because the hand absorbs the sound already in the room",
             "correct": False,
             "why": "A hand cannot mop up sound that has already left; what "
                    "it stops is the source."},
            {"text": "Because gripping it makes the note too low to hear",
             "correct": False,
             "why": "The note does not drop in pitch — it ceases to be "
                    "produced at all."},
            {"text": "Because the source stops vibrating, so no new "
                     "disturbance is sent out",
             "correct": True},
            {"text": "Because the sound stored inside the object has been "
                     "sealed in",
             "correct": False,
             "why": "Nothing is stored inside it; the sound existed only "
                    "while the surface moved."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h06",
        "band": "harder",
        "text": "A ringing bell is put inside a sealed box lined with thick "
                "foam and almost nothing is heard. Is the bell still "
                "vibrating?",
        "options": [            {"text": "Yes, and the foam is absorbing the disturbance before "
                     "it gets out",
             "correct": True},
            {"text": "No — the foam stops it moving", "correct": False,
             "why": "The foam never touches the bell; it absorbs the "
                    "disturbance travelling through the air."},
            {"text": "No — sound cannot be made inside a closed box",
             "correct": False,
             "why": "The box is full of air, so the bell makes sound "
                    "perfectly well inside it."},
            {"text": "Yes, but the sound has been stored in the foam",
             "correct": False,
             "why": "The foam takes the energy into thermal stores; nothing "
                    "keeps the sound for later."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-03-e07",
        "band": "easier",
        "text": "Every sound, whatever makes it, begins with something…",
        "options": [
            {"text": "heating up", "correct": False,
             "why": "Temperature has nothing to do with starting a sound; "
                    "vibration does."},
            {"text": "glowing", "correct": False,
             "why": "Sound has nothing to do with light or glowing; it "
                    "starts with something moving to and fro."},
            {"text": "cooling down", "correct": False,
             "why": "Temperature has nothing to do with starting a sound; "
                    "vibration does."},
            {"text": "vibrating", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e08",
        "band": "easier",
        "text": "In a microphone, the thin stretched sheet that is set "
                "moving by arriving air is called the…",
        "options": [
            {"text": "diaphragm", "correct": True},
            {"text": "amplitude", "correct": False,
             "why": "Amplitude is a measurement of a wave, not a part "
                    "inside a microphone."},
            {"text": "cone", "correct": False,
             "why": "A cone is the moving part of a loudspeaker, not the "
                    "sheet inside a microphone."},
            {"text": "wavelength", "correct": False,
             "why": "Wavelength is a measurement of a wave, not a part "
                    "inside a microphone."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e09",
        "band": "easier",
        "text": "The stretched sheet inside your ear that vibrates when "
                "sound arrives, doing the same job as a microphone's "
                "diaphragm, is the…",
        "options": [
            {"text": "eardrum", "correct": True},
            {"text": "eyelid", "correct": False,
             "why": "The eyelid has nothing to do with hearing; it is part "
                    "of the eye."},
            {"text": "vocal folds", "correct": False,
             "why": "Vocal folds are in the throat and are used to make "
                    "sound, not to detect it arriving."},
            {"text": "elbow", "correct": False,
             "why": "The elbow plays no part in hearing at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e10",
        "band": "easier",
        "text": "A plucked ruler, resting over the edge of a desk, is "
                "buzzing loudly. A hand presses down firmly on the free "
                "end. What happens to the sound?",
        "options": [
            {"text": "It stops at once, because the ruler can no longer "
                     "vibrate", "correct": True},
            {"text": "It carries on for a while, because the sound was "
                     "already released into the room", "correct": False,
             "why": "Sound is not released and then left drifting; it "
                    "exists only while the source keeps vibrating."},
            {"text": "It gets louder, because the hand pushes more air",
             "correct": False,
             "why": "The hand stops the ruler moving; it does not push "
                    "air the way the vibrating ruler was doing."},
            {"text": "It changes to a completely different sound, made now "
                     "by the hand instead of the ruler", "correct": False,
             "why": "The hand is not vibrating and making a new sound; it "
                    "is simply stopping the ruler's own vibration."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e11",
        "band": "easier",
        "text": "A drum is struck once and its skin buzzes for a short "
                "time before falling silent. While the skin is buzzing, "
                "where is the sound coming from?",
        "options": [
            {"text": "It was stored inside the drum from an earlier hit, "
                     "and this strike simply released it", "correct": False,
             "why": "Nothing is stored up inside a drum; the sound exists "
                    "only while the skin is actually vibrating."},
            {"text": "From the drummer's hand, which somehow keeps on "
                     "making the sound long after the strike itself",
             "correct": False,
             "why": "The hand only delivers the strike; the drum skin is "
                    "what carries on vibrating afterwards."},
            {"text": "From the air trapped inside the drum, which starts "
                     "making sound on its own once disturbed",
             "correct": False,
             "why": "The air only carries the disturbance; it is the "
                    "vibrating skin that is making the sound happen."},
            {"text": "From the skin, vibrating and disturbing the air next "
                     "to it, fresh each moment", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e12",
        "band": "easier",
        "text": "A struck tuning fork sounds much quieter held in the air "
                "than when its base is pressed onto a table top. What has "
                "been added to the fork to make it louder on the table?",
        "options": [
            {"text": "Extra energy from the table", "correct": False,
             "why": "The table does not add energy to the fork; the fork "
                    "still only has the energy it was struck with."},
            {"text": "A bigger vibration", "correct": False,
             "why": "The fork's own vibration is not made bigger by "
                    "touching the table."},
            {"text": "Nothing has been added to the fork itself",
             "correct": True},
            {"text": "A higher frequency of vibration overall", "correct": False,
             "why": "Touching the table does not change how fast the fork "
                    "is vibrating."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-03-s07",
        "band": "standard",
        "text": "A struck tuning fork is quiet held in the air but loud "
                "once its base is pressed onto a table top, and nothing "
                "about the fork's own vibration has changed. Why does it "
                "sound louder on the table?",
        "options": [
            {"text": "The table top is being driven by the fork and pushes "
                     "far more air than the fork's own thin prongs could "
                     "on their own", "correct": True},
            {"text": "The table absorbs the vibration and makes its own "
                     "fresh, louder sound", "correct": False,
             "why": "The table does not make its own sound; it simply "
                    "transmits the fork's vibration to a much larger area "
                    "of air."},
            {"text": "The table reflects the fork's sound back directly "
                     "towards the listener, which is what doubles how "
                     "loud it seems to be", "correct": False,
             "why": "Nothing here is being reflected back towards a "
                    "listener; the whole table top is itself being made to "
                    "push the air."},
            {"text": "Pressing the fork onto the table increases the "
                     "fork's own frequency of vibration", "correct": False,
             "why": "The fork's frequency is unchanged by touching the "
                    "table; only how much air gets pushed changes."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s08",
        "band": "standard",
        "text": "The louder, table-driven version of a struck tuning "
                "fork's note also dies away faster than the quiet, "
                "held-in-air version. Explain why, in terms of energy.",
        "options": [
            {"text": "The table version uses up the fork's fixed store of "
                     "vibration energy more quickly, because it is being "
                     "handed to a much larger amount of air each moment",
             "correct": True},
            {"text": "The table version has more total energy to begin "
                     "with, so naturally there is more of it to use up",
             "correct": False,
             "why": "Both versions start with exactly the same energy from "
                    "the same strike; nothing extra was given to either "
                    "one."},
            {"text": "The table absorbs energy from the surrounding room "
                     "as well as from the fork itself, and this combined "
                     "absorption is what somehow speeds up the fading",
             "correct": False,
             "why": "The room does not feed extra energy into the system; "
                    "the fading is about how fast the fork's own energy is "
                    "given up, not about energy coming in from elsewhere."},
            {"text": "Louder sounds always fade faster than quiet ones, "
                     "regardless of what is making either of them",
             "correct": False,
             "why": "That is not a general rule; it is specifically about "
                    "how quickly a particular source is handing its energy "
                    "to the air, not about loudness on its own."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s09",
        "band": "standard",
        "text": "A loudspeaker cone is playing a very high, quiet note, "
                "vibrating so fast and by such a tiny distance that its "
                "movement cannot be seen at all by eye. Is the cone "
                "actually vibrating?",
        "options": [
            {"text": "No — if the movement cannot be seen, there is no "
                     "real vibration happening", "correct": False,
             "why": "Sound is coming out, and sound only exists while "
                    "something is genuinely vibrating; the movement is "
                    "simply too fast and small to see."},
            {"text": "It depends on whether the note is loud enough to "
                     "hear clearly", "correct": False,
             "why": "Loudness comes from the size of the vibration, not "
                    "from whether the cone is vibrating in the first "
                    "place."},
            {"text": 'No — a note this quiet and high is produced '
                     'electronically, without the cone having to move, since '
                     'the speaker only passes the signal onward to the room', "correct": False,
             "why": "A loudspeaker always makes sound by moving its cone; "
                    "there is no way for it to produce sound without any "
                    "movement."},
            {"text": "Yes — the sound coming out is only possible because "
                     "the cone really is vibrating, whether or not that "
                     "movement is visible", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s10",
        "band": "standard",
        "text": "A cheap intercom uses a single small loudspeaker at each "
                "end, wired so either one can act as the microphone while "
                "the other plays the sound. What makes it possible for one "
                "loudspeaker to work as a microphone at all?",
        "options": [
            {"text": "The two loudspeakers are secretly connected by radio "
                     "as well as by wire, and the radio link carries the "
                     "sound", "correct": False,
             "why": "No radio link is needed or used; the ordinary wire "
                    "connection is doing the whole job."},
            {"text": "A speaker's cone moving in response to arriving "
                     "sound can generate an electrical signal, the same "
                     "way a microphone diaphragm does", "correct": True},
            {"text": 'Loudspeakers and microphones are built from identical '
                     'parts, with no difference between them anywhere', "correct": False,
             "why": "They are built for different jobs, even though the "
                    "underlying moving-coil idea can run in either "
                    "direction."},
            {"text": "The intercom's electronics fake the microphone function "
                     "on their own, reading the tiny currents in the wire "
                     "without the loudspeaker's cone moving at all",
             "correct": False,
             "why": "It is the loudspeaker's own cone and coil, moved by "
                    "the arriving sound, that genuinely generates the "
                    "signal — nothing is faked."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s11",
        "band": "standard",
        "text": "A large table top and a small tuning fork are both made "
                "to vibrate by the same struck fork, at the very same "
                "frequency. Which pushes more air, and why?",
        "options": [
            {"text": "The tuning fork, because it is vibrating fastest",
             "correct": False,
             "why": "Both are vibrating at the same frequency here; "
                    "speed of vibration is not what is different between "
                    "them."},
            {"text": "The table top, because it has a much larger surface "
                     "in contact with the air", "correct": True},
            {"text": "Neither one, since both push exactly the same air",
             "correct": False,
             "why": "Frequency being equal does not make the amount of air "
                    "pushed equal; surface area in contact with the air "
                    "matters too."},
            {"text": 'The tuning fork, because metal pushes air more easily '
                     'than wood does, whatever the size of the surface doing '
                     'the pushing', "correct": False,
             "why": "The material of the surface is not what decides this "
                    "here; how much surface area is moving the air is."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-03-h07",
        "band": "harder",
        "text": "A struck tuning fork sounds louder pressed onto a table, "
                "and a student concludes the fork itself must be "
                "vibrating with a bigger amplitude while touching the "
                "table. Assess this conclusion.",
        "options": [
            {"text": "The conclusion is right, since a louder sound "
                     "always means a bigger amplitude of vibration "
                     "somewhere within the whole system", "correct": False,
             "why": "The extra loudness comes from the table pushing more "
                    "air, not from the fork's own amplitude growing."},
            {"text": "The conclusion is wrong — the fork's own vibration is "
                     "unchanged; the table simply pushes far more air with "
                     "the same movement", "correct": True},
            {"text": "The conclusion is right, but only because the table "
                     "physically presses the prongs further apart",
             "correct": False,
             "why": "Nothing about resting the base on a table changes how "
                    "far apart the prongs swing."},
            {"text": "The conclusion cannot be judged without measuring "
                     "the fork's frequency as well as its loudness",
             "correct": False,
             "why": "Frequency is not in question here; the fork's "
                    "amplitude — not its frequency — is what the "
                    "conclusion is actually about."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h08",
        "band": "harder",
        "text": "Old headphones plugged into a microphone socket and "
                "shouted into will pick up a faint, poor-quality signal, "
                "even though they were built only to turn a signal into "
                "sound. Explain why this works at all.",
        "options": [
            {"text": 'It does not work — any faint signal picked up this way is '
                     'random electrical noise from the socket, and it only '
                     'seems to follow the shouting because the socket is being '
                     'jogged', "correct": False,
             "why": "The headphones genuinely do generate a real, if poor, "
                    "signal from the sound arriving at them."},
            {"text": "A coil moving near a magnet generates a voltage "
                     "whether or not that was the intended use, so shouted "
                     "sound moving the headphone's own coil produces a "
                     "signal too", "correct": True},
            {"text": "Headphones secretly contain a hidden microphone "
                     "circuit built in alongside the speaker part",
             "correct": False,
             "why": "No separate microphone circuit is needed; it is the "
                    "very same coil-and-magnet part doing an unintended "
                    "second job."},
            {"text": "Shouting into headphones works only because modern "
                     "electronics automatically convert the sound for "
                     "them", "correct": False,
             "why": "No conversion electronics are involved; the physical "
                    "coil-and-magnet movement itself is what generates the "
                    "signal."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h09",
        "band": "harder",
        "text": "A student claims a struck tuning fork keeps sounding "
                "forever, because striking it started the vibration and "
                "nothing afterwards acts to stop it. Assess this claim.",
        "options": [
            {"text": "The claim is right — struck once, a tuning fork "
                     "genuinely never stops vibrating on its own",
             "correct": False,
             "why": "A struck fork's note is heard to fade away and "
                    "eventually stop; it does not vibrate forever."},
            {"text": 'The claim is right, but only because sound is inaudible '
                     'once too quiet, while the fork still vibrates as hard as '
                     'at the start, with nothing touching it to slow it', "correct": False,
             "why": "The fork's vibration itself genuinely weakens over "
                    "time; it is not simply becoming too quiet to hear "
                    "while staying just as strong."},
            {"text": "The claim is wrong, but only because friction "
                     "between the prongs eventually welds them together",
             "correct": False,
             "why": "Nothing about the prongs welding together is "
                    "involved; the fading comes from energy being handed "
                    "to the air, not from the prongs sticking."},
            {"text": "The claim is wrong — the fork continually hands its "
                     "vibration energy to the surrounding air, so the "
                     "vibration and the sound both gradually die away",
             "correct": True},
        ],
        "figure": None,
    },
]
