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

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p6-03-e13",
        "band": "easier",
        "text": "Four things are involved whenever a sound is heard: a "
                "detector responding, air being pushed and released, a "
                "disturbance travelling outward, and something vibrating. Which "
                "of these four is the ONLY one that is not itself sound?",
        "options": [
            {"text": "the detector responding", "correct": True},
            {"text": "the air being pushed and released", "correct": False,
             "why": "This is the sound itself leaving the source — "
                    "without it there would be nothing to carry onward."},
            {"text": "the disturbance travelling outward", "correct": False,
             "why": "The travelling disturbance is still sound, moving "
                    "through the air from source to detector."},
            {"text": "something vibrating", "correct": False,
             "why": "The vibrating source is exactly where the sound "
                    "begins; it is very much part of the sound, not the "
                    "exception."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e14",
        "band": "easier",
        "text": "A plucked guitar string moves about 3 mm with each "
                "vibration; a struck tuning fork moves about 0.5 mm. "
                "Which one moves further with each vibration?",
        "options": [
            {"text": "the tuning fork", "correct": False,
             "why": "0.5 mm is smaller than 3 mm, so the fork's prongs "
                    "are moving less far, not more."},
            {"text": "the guitar string", "correct": True},
            {"text": "neither — both move exactly the same distance",
             "correct": False,
             "why": "3 mm and 0.5 mm are different distances; the "
                    "string's amplitude is clearly the bigger of the "
                    "two."},
            {"text": "it cannot be told without knowing how many times a "
                     "second each one vibrates", "correct": False,
             "why": "How far each one moves is given directly as an "
                    "amplitude; how often it vibrates is a separate "
                    "measurement."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e15",
        "band": "easier",
        "text": "A concert tuning fork vibrates 440 times each second; a "
                "large drum skin vibrates about 80 times each second. "
                "Which one is moving to and fro more times each second?",
        "options": [
            {"text": "both move to and fro the same number of times each "
                     "second", "correct": False,
             "why": "440 and 80 are different numbers — the fork is "
                    "moving to and fro far more often."},
            {"text": "the drum skin", "correct": False,
             "why": "80 is smaller than 440, so the drum skin is moving "
                    "to and fro fewer times each second, not more."},
            {"text": "the tuning fork", "correct": True},
            {"text": "it cannot be told without knowing how far each one "
                     "moves", "correct": False,
             "why": "How many times a second each one vibrates is given "
                    "directly; how far each one moves is a separate "
                    "measurement."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e16",
        "band": "easier",
        "text": "A tuning fork is struck once and left alone; a "
                "loudspeaker cone is driven continuously by an "
                "electrical signal. Which one needs a continuing supply "
                "of something to keep vibrating?",
        "options": [
            {"text": "neither needs anything supplied once it starts "
                     "vibrating", "correct": False,
             "why": "The cone stops moving the moment its driving signal "
                    "stops arriving, so it clearly does depend on a "
                    "continuing supply."},
            {"text": "the tuning fork", "correct": False,
             "why": "A struck fork is set going by a single strike, then "
                    "simply left to ring on its own — it needs nothing "
                    "more supplied to it."},
            {"text": "both need a continuing supply of something",
             "correct": False,
             "why": "The fork rings on its own once struck; only the "
                    "cone depends on a signal that keeps arriving."},
            {"text": "the loudspeaker cone", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e17",
        "band": "easier",
        "text": "A singer is holding a long note and runs out of breath "
                "partway through it. What happens to the note?",
        "options": [
            {"text": "The note stops, since the folds can no longer be "
                     "blown open and snapped shut", "correct": True},
            {"text": "The note carries on unchanged, since the folds "
                     "keep vibrating on their own once started", "correct": False,
             "why": "Unlike a struck fork, the folds need a continuing "
                    "supply of air — without it, they stop being driven and "
                    "the note ends."},
            {"text": "The note gets louder, since less air pressure "
                     "means the folds vibrate more freely", "correct": False,
             "why": "Running out of breath removes the air that drives "
                    "the folds at all; it does not make them vibrate more "
                    "freely."},
            {"text": "Nothing changes, since the folds store enough "
                     "vibration to keep going regardless", "correct": False,
             "why": "Nothing about a sound is stored up in the folds; "
                    "the note exists only while they are actually being "
                    "driven."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e18",
        "band": "easier",
        "text": "A guitar string is plucked and released, with nothing "
                "driving it any further. What happens to it over the next few "
                "seconds?",
        "options": [
            {"text": "It keeps vibrating at exactly the same amplitude "
                     "forever, since nothing is stopping it", "correct": False,
             "why": "The string loses a little energy to the air with "
                    "every push it gives, so its own vibration gradually "
                    "shrinks rather than staying constant."},
            {"text": "It fades, since every push it gives the air "
                     "always takes a little energy from the string itself", "correct": True},
            {"text": "It stops instantly the moment the plucking finger "
                     "is released", "correct": False,
             "why": "A plucked string carries on ringing for a while "
                    "after release — it fades gradually rather than stopping "
                    "at once."},
            {"text": "It vibrates faster and faster as it fades", "correct": False,
             "why": "Fading is about the string moving a smaller "
                    "distance each time, not about vibrating faster."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e19",
        "band": "easier",
        "text": "Which of these is struck once and then simply left to "
                "ring, rather than needing something continuously supplied to "
                "keep going?",
        "options": [
            {"text": "a set of vocal folds", "correct": False,
             "why": "Vocal folds need a continuing supply of air from "
                    "the lungs to keep being driven open and shut."},
            {"text": "a loudspeaker cone", "correct": False,
             "why": "A cone is driven continuously by an electrical "
                    "signal — remove the signal and it stops."},
            {"text": "a tuning fork", "correct": True},
            {"text": "an eardrum", "correct": False,
             "why": "An eardrum is a detector in this lesson, not one "
                    "of the sources that is struck, plucked or driven."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e20",
        "band": "easier",
        "text": "A large drum skin can be loud without moving very far "
                "— only about 0.5 mm. Why can it still push a lot of air?",
        "options": [
            {"text": "Because the drum is always struck harder than "
                     "other sources", "correct": False,
             "why": "How hard something is struck is not what this "
                    "lesson uses to explain the drum's loudness; its large "
                    "surface area is."},
            {"text": "Because a small amplitude always pushes more air "
                     "than a large one", "correct": False,
             "why": "A small amplitude on its own pushes less air, not "
                    "more — it is the drum skin's large surface area that "
                    "makes up for it."},
            {"text": "Because the drum skin is simply heavier than a "
                     "fork, a string or a loudspeaker cone", "correct": False,
             "why": "Weight is not the reason given in this lesson — "
                    "the explanation is about how much surface is pushing the "
                    "air."},
            {"text": "Because its amplitude is small but its surface "
                     "area is large, so it still moves a lot of air even without "
                     "moving far", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e21",
        "band": "easier",
        "text": "A struck tuning fork's prongs move only about 0.5 mm, "
                "yet the fork is clearly making a sound. Why is the movement "
                "hard to see by eye?",
        "options": [
            {"text": "The prongs move a very short distance, and they "
                     "move to and fro far too quickly for the eye to follow", "correct": True},
            {"text": "The prongs stay still — the sound comes from the "
                     "air around them instead, which starts moving on its own as "
                     "soon as the metal is struck", "correct": False,
             "why": "The prongs genuinely are moving: a struck fork "
                    "dipped into water splashes it, which is direct evidence "
                    "of the movement."},
            {"text": "The movement begins after the sound has already "
                     "faded away to nothing", "correct": False,
             "why": "The movement and the sound happen together — the "
                    "sound lasts exactly as long as the prongs keep vibrating."},
            {"text": "Metal objects can never be seen to move, whatever "
                     "the size of the movement", "correct": False,
             "why": "A large enough movement in metal is perfectly "
                    "visible; it is this movement's small size and high speed "
                    "that hide it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e22",
        "band": "easier",
        "text": "A struck drum skin has finished ringing and gone "
                "completely silent. Is it still vibrating?",
        "options": [
            {"text": "Yes, but too quietly to disturb the air any "
                     "further", "correct": False,
             "why": "If it were still vibrating it would still be "
                    "disturbing the air, however slightly — silence "
                    "means the vibration itself has stopped."},
            {"text": "No — sound only exists while the source is "
                     "actually vibrating, and a silent skin has stopped",
             "correct": True},
            {"text": "Yes — the sound is simply being stored quietly "
                     "inside the drum skin, ready to be released again "
                     "later on", "correct": False,
             "why": "Nothing about a sound is stored up inside a "
                    "vibrating object; the sound exists only while the "
                    "vibration is actually happening."},
            {"text": "It cannot be known without touching the skin",
             "correct": False,
             "why": "A skin making no sound at all is exactly the "
                    "evidence that its vibration has stopped — nothing "
                    "further needs to be touched."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e23",
        "band": "easier",
        "text": "A guitar string is plucked and starts loud, then gets "
                "quieter and quieter until it falls silent. What is "
                "happening to the string's own vibration over this time?",
        "options": [
            {"text": "It is vibrating faster and faster as it gets "
                     "quieter", "correct": False,
             "why": "Getting quieter is about the string moving a "
                    "smaller distance each time, not about vibrating "
                    "faster."},
            {"text": "It is swinging the same distance the whole time, "
                     "right up until it suddenly stops", "correct": False,
             "why": "A fading note comes from the vibration itself "
                    "shrinking gradually, not from a constant swing that "
                    "stops all at once."},
            {"text": "It is swinging less and less far each time, until "
                     "it stops moving altogether", "correct": True},
            {"text": "Nothing is changing about the string itself — the "
                     "air around it is simply absorbing the sound",
             "correct": False,
             "why": "The string's own vibration is genuinely shrinking "
                    "over time; that is what makes the note fade."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e24",
        "band": "easier",
        "text": "An eardrum and a microphone's diaphragm do the same "
                "kind of job in the chain from a source to a listener. What is "
                "that job?",
        "options": [
            {"text": "Both are sources: they make the sound in the "
                     "first place", "correct": False,
             "why": "A source is what vibrates to start a sound off. "
                    "These two are set moving BY a sound that has already been "
                    "made somewhere else."},
            {"text": "Both store the arriving sound until it is needed", "correct": False,
             "why": "Nothing about a sound is stored anywhere. Both "
                    "move only while the sound is actually arriving at them."},
            {"text": "Both push the air outward to carry the sound "
                     "further", "correct": False,
             "why": "Pushing the air outward is a source's job. These "
                    "two sit at the far end of the chain, being pushed by air "
                    "that is already moving."},
            {"text": "Both are detectors: they are set moving by "
                     "arriving sound", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e25",
        "band": "easier",
        "text": "In the four-stage description of a sound, which stage "
                "comes immediately before 'the disturbance travels "
                "outward'?",
        "options": [
            {"text": "the air is pushed and released", "correct": True},
            {"text": "something vibrates", "correct": False,
             "why": "That is the very first stage of all, two stages "
                    "before the disturbance travels outward."},
            {"text": "a detector at the far end finally picks it up",
             "correct": False,
             "why": "Detecting is the LAST of the four stages, coming "
                    "after the disturbance has already travelled "
                    "outward."},
            {"text": "the sound is stored", "correct": False,
             "why": "Sound is never stored at any stage — this is not "
                    "one of the four stages at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e26",
        "band": "easier",
        "text": "In the four-stage description of a sound, which stage "
                "comes first of all?",
        "options": [
            {"text": "the disturbance travels outward", "correct": False,
             "why": "Nothing can travel outward until something has "
                    "started vibrating in the first place."},
            {"text": "something vibrates", "correct": True},
            {"text": "a detector picks it up", "correct": False,
             "why": "Detecting is the last of the four stages, not the "
                    "first."},
            {"text": "the air is pushed and released", "correct": False,
             "why": "The air can only be pushed and released once "
                    "something is already vibrating to push it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e27",
        "band": "easier",
        "text": "A microphone's diaphragm moves in time with arriving "
                "air. What is its job?",
        "options": [
            {"text": "To store the sound until it is needed later",
             "correct": False,
             "why": "Nothing about a sound is stored — the diaphragm's "
                    "movement is converted into a signal as it happens."},
            {"text": "To push the air back outward, making the sound "
                     "louder", "correct": False,
             "why": "That is a loudspeaker's job, at the other end of "
                    "the chain — a microphone's diaphragm detects, it "
                    "does not push sound out."},
            {"text": "To turn that movement into a changing electrical "
                     "signal", "correct": True},
            {"text": "To block unwanted vibrations from reaching the "
                     "microphone", "correct": False,
             "why": "The diaphragm's job is to move WITH arriving air, "
                    "not to block it out."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e28",
        "band": "easier",
        "text": "A loudspeaker cone is driven back and forth by a signal "
                "that keeps arriving continuously. What would happen to "
                "the cone if that signal suddenly stopped?",
        "options": [
            {"text": "It cannot be known without measuring the cone's "
                     "amplitude first", "correct": False,
             "why": "A cone with no driving signal has nothing left "
                    "pushing it — this holds whatever its amplitude "
                    "happened to be beforehand."},
            {"text": "It would carry on vibrating at the same amplitude "
                     "indefinitely", "correct": False,
             "why": "Unlike a struck fork, the cone depends on a "
                    "continuing signal — without one, it has nothing "
                    "left driving it."},
            {"text": "It would vibrate even harder, to make up for the "
                     "missing signal", "correct": False,
             "why": "Nothing about a missing signal makes a cone move "
                    "further — with no signal driving it, it simply "
                    "stops."},
            {"text": "It would stop vibrating too, since nothing is "
                     "driving it any more", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e29",
        "band": "easier",
        "text": "A loudspeaker cone needs a continuous electrical signal "
                "to keep vibrating. What does a set of vocal folds need "
                "to keep vibrating in a similar, continuing way?",
        "options": [
            {"text": "A continuous supply of air from the lungs",
             "correct": True},
            {"text": "A continuous electrical signal, exactly like the "
                     "cone", "correct": False,
             "why": "Vocal folds are driven by moving air, not by "
                    "electricity — that is the cone's own supply, not "
                    "theirs."},
            {"text": "Nothing at all, once the singer has taken a first "
                     "breath", "correct": False,
             "why": "The folds stop the moment the air supply stops — "
                    "one breath at the very start is not enough to keep "
                    "them going."},
            {"text": "A continuous supply of sound arriving from "
                     "elsewhere", "correct": False,
             "why": "The folds are the SOURCE of the note, not "
                    "something driven by sound arriving from somewhere "
                    "else."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-e30",
        "band": "easier",
        "text": "A tuning fork, a guitar string and a drum skin are all "
                "set going by a single strike or pluck, then left alone. What "
                "happens to each one's vibration after that?",
        "options": [
            {"text": "It stays at the same amplitude forever, since "
                     "nothing is acting on any of them", "correct": False,
             "why": "Each push against the air takes a little of the "
                    "vibration's own energy, so all three fade rather than "
                    "staying constant."},
            {"text": "It gradually dies away, since each push against "
                     "the air takes a little energy and nothing tops it back up "
                     "at all", "correct": True},
            {"text": "It stops completely instantly, the very moment "
                     "the strike or pluck itself ends, for all three sources "
                     "alike", "correct": False,
             "why": "All three carry on ringing for a while afterwards "
                    "— they fade gradually rather than stopping at once."},
            {"text": "It grows louder for a moment before fading", "correct": False,
             "why": "None of the three gains extra energy after being "
                    "set going — each one's vibration only ever shrinks from "
                    "that point on."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p6-03-s12",
        "band": "standard",
        "text": "A tuning fork vibrates 440 times each second; a large "
                "drum skin vibrates about 80 times each second. Roughly "
                "how many times more often does the fork vibrate than "
                "the drum, for every one time the drum does?",
        "options": [
            {"text": "about 20 times as often", "correct": False,
             "why": "440 divided by 80 comes to about 5.5, well short "
                    "of 20."},
            {"text": "about 2 times as often", "correct": False,
             "why": "440 divided by 80 comes to about 5.5, not 2."},
            {"text": "about 5 or 6 times as often", "correct": True},
            {"text": "exactly the same number of times", "correct": False,
             "why": "440 and 80 are very different numbers — the fork "
                    "is vibrating far more often than the drum."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s13",
        "band": "standard",
        "text": "A guitar string moves about 3 mm with each vibration; a "
                "tuning fork moves about 0.5 mm. Roughly how many times "
                "further does the string move than the fork?",
        "options": [
            {"text": "about 3 times further", "correct": False,
             "why": "3 mm divided by 0.5 mm comes to 6, not 3."},
            {"text": "It cannot be told without knowing how often each "
                     "one vibrates", "correct": False,
             "why": "Comparing the two amplitudes only needs the two "
                    "distances given; how often each vibrates is a "
                    "separate measurement."},
            {"text": "about 15 times further", "correct": False,
             "why": "That divides 3 by 0.2, not by the fork's actual "
                    "0.5 mm amplitude."},
            {"text": "about 6 times further", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s14",
        "band": "standard",
        "text": "A vocal fold vibrates about 120 times a second for a "
                "low voice. A concert tuning fork vibrates 440 times a "
                "second. Which is vibrating faster, and by roughly what "
                "factor?",
        "options": [
            {"text": "The tuning fork, by roughly 3 to 4 times",
             "correct": True},
            {"text": "The vocal fold, by roughly 3 to 4 times",
             "correct": False,
             "why": "440 is bigger than 120, so the fork is the faster "
                    "of the two, not the vocal fold."},
            {"text": "The tuning fork, but only by about 10%",
             "correct": False,
             "why": "440 divided by 120 comes to well over 3, not "
                    "close to 1.1."},
            {"text": "Neither — the two numbers are close enough to "
                     "count as the same", "correct": False,
             "why": "120 and 440 are far apart; the fork is vibrating "
                    "several times faster, not about the same rate."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s15",
        "band": "standard",
        "text": "A loudspeaker cone moves about 1 mm on a loud bass "
                "note. If the same cone were driven at only a quarter of "
                "that amplitude, roughly how far would it move?",
        "options": [
            {"text": "4 mm", "correct": False,
             "why": "That multiplies by 4 rather than dividing by 4."},
            {"text": "0.25 mm", "correct": True},
            {"text": "0.75 mm", "correct": False,
             "why": "That subtracts a quarter of a millimetre from 1 mm "
                    "instead of taking a quarter OF the 1 mm."},
            {"text": "1 mm, unchanged", "correct": False,
             "why": "Driving the cone at a smaller amplitude setting "
                    "does change how far it moves — it does not stay "
                    "at 1 mm."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s16",
        "band": "standard",
        "text": "A struck drum skin fades to silence after a couple of "
                "seconds, while a struck tuning fork can be heard ringing for "
                "much longer. Suggest, using an idea from this lesson, why the "
                "fork might ring for longer.",
        "options": [
            {"text": "The drum skin is simply thinner than a tuning "
                     "fork's prongs, and a thinner object always fades away "
                     "faster", "correct": False,
             "why": "Thinness is not the property this lesson links to "
                    "fading — how much surface is pushing the air is."},
            {"text": "The fork simply starts with far more energy than "
                     "the drum, however it is struck", "correct": False,
             "why": "Nothing in this lesson says a fork is struck with "
                    "more energy — the difference described is about how much "
                    "air each one pushes, not how hard it is hit."},
            {"text": "Its thin prongs push far less air with each swing "
                     "than the drum's large skin, so it hands over its energy "
                     "more slowly", "correct": True},
            {"text": "A drum skin cannot ring at all, since it is flat "
                     "rather than curved like a fork", "correct": False,
             "why": "A drum skin clearly does ring, just for a shorter "
                    "time than the fork — being flat rather than curved is not "
                    "the reason given."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s17",
        "band": "standard",
        "text": "A phone's tiny loudspeaker sounds much louder when the "
                "phone is laid flat on a hard tabletop than when held "
                "up in the air. Using the tuning-fork idea from this "
                "lesson, suggest why.",
        "options": [
            {"text": "The phone's own electronics automatically turn "
                     "the volume up whenever they detect a hard surface "
                     "underneath the phone", "correct": False,
             "why": "Nothing electronic is detecting the tabletop — the "
                    "extra loudness comes from the table itself being "
                    "made to push more air."},
            {"text": "The table absorbs the sound and produces a "
                     "louder echo of its own", "correct": False,
             "why": "The table is not producing an echo — it is being "
                    "driven directly by the phone and pushing the air "
                    "itself, the same way as the fork on a table."},
            {"text": "Laying the phone flat always increases the "
                     "amplitude of the speaker's own vibration",
             "correct": False,
             "why": "The speaker's own vibration is not changed by "
                    "lying flat — it is the much larger table surface "
                    "that ends up pushing more air."},
            {"text": "The tabletop, driven by the phone's vibration, "
                     "pushes far more air than the tiny speaker alone",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s18",
        "band": "standard",
        "text": "A microphone changes air movement into an electrical "
                "signal; a loudspeaker changes an electrical signal "
                "into air movement. An engineer wires a microphone's "
                "output directly into a loudspeaker's input. What "
                "should happen when someone speaks near the microphone?",
        "options": [
            {"text": "The loudspeaker should reproduce something like "
                     "the sound, since the microphone's signal can "
                     "drive the speaker as intended", "correct": True},
            {"text": "Nothing should happen, since a microphone's "
                     "signal is not strong enough to drive any "
                     "loudspeaker at all", "correct": False,
             "why": "The whole point of the chain is that the "
                    "microphone's signal is exactly the kind of signal "
                    "a loudspeaker is built to be driven by."},
            {"text": "The loudspeaker should instead start acting as a "
                     "microphone itself", "correct": False,
             "why": "Wiring a signal INTO a loudspeaker drives its cone "
                    "as a source — it does not turn the loudspeaker "
                    "into a detector."},
            {"text": "The microphone itself should stop working "
                     "altogether, since its own signal has nowhere left "
                     "to go once it reaches the loudspeaker's input",
             "correct": False,
             "why": "The loudspeaker is exactly where the microphone's "
                    "signal is meant to go — reaching it does not stop "
                    "the microphone working."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s19",
        "band": "standard",
        "text": "A struck cymbal is ringing steadily. A player rests a "
                "hand lightly on its edge and the note becomes much quieter but "
                "does not stop. What has the light touch done?",
        "options": [
            {"text": "Blocked most of the sound from leaving the "
                     "cymbal, while letting the rest escape past the hand, so "
                     "the note that is left is simply the part that got past it", "correct": False,
             "why": "A hand on the edge does not block a path out. It "
                    "acts on the cymbal's own swing, which is what was making "
                    "the sound."},
            {"text": "Taken some energy out of the cymbal's swing, so "
                     "it now moves a smaller distance and disturbs the air less", "correct": True},
            {"text": "Slowed the cymbal down, so that it now vibrates "
                     "fewer times each second", "correct": False,
             "why": "A light touch takes energy out of the swing rather "
                    "than changing how often the cymbal vibrates; the note "
                    "goes quieter, not lower."},
            {"text": "Nothing at all to the cymbal — the hand simply "
                     "absorbs sound out of the air nearby", "correct": False,
             "why": "The hand is in contact with the cymbal itself, and "
                    "it is the cymbal's own swing that has shrunk, not the air "
                    "around it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s20",
        "band": "standard",
        "text": "A recording of a violin is played back through a "
                "loudspeaker in a completely different room, long after the "
                "original violin has stopped playing. Using the idea that sound "
                "is not stored, explain what the loudspeaker is actually doing.",
        "options": [
            {"text": "It is pulling the violin's own vibration back "
                     "from wherever it went after the recording", "correct": False,
             "why": "The original vibration is long gone; the "
                    "loudspeaker never recovers it — it makes a new one of its "
                    "own, following the stored pattern."},
            {"text": "It is releasing the original violin's sound, "
                     "which has been kept somewhere since it was recorded", "correct": False,
             "why": "No sound has been kept anywhere — only a pattern "
                    "has, and the loudspeaker makes a brand new vibration from "
                    "that pattern."},
            {"text": "It is converting a stored electrical pattern back "
                     "into a fresh vibration of its own cone, making new sound "
                     "rather than releasing old sound", "correct": True},
            {"text": "It is simply amplifying whatever faint trace of "
                     "sound remains in the room from the original violin", "correct": False,
             "why": "No trace of the original sound remains in a "
                    "different room; the loudspeaker's cone is making an "
                    "entirely fresh vibration of its own."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s21",
        "band": "standard",
        "text": "A phone's tiny loudspeaker and a large concert hall "
                "speaker are both driven by the same electrical signal, "
                "producing the same note. Which is more likely to sound louder, "
                "and why, using ideas about pushing air from this lesson?",
        "options": [
            {"text": "It cannot be judged without knowing the exact "
                     "colour of each loudspeaker's casing", "correct": False,
             "why": "The casing's colour has nothing to do with how "
                    "much air a cone pushes — its surface area does."},
            {"text": "The phone's speaker, since smaller cones always "
                     "move a greater distance for the same signal", "correct": False,
             "why": "Cone size is not linked to how far it moves in "
                    "this lesson — a larger cone simply has more surface area "
                    "pushing the air."},
            {"text": "Neither — an identical electrical signal produces "
                     "exactly the same loudness for every size of cone", "correct": False,
             "why": "The size of the vibrating surface matters, just as "
                    "it does for a tuning fork pressed onto a table — a bigger "
                    "cone pushes more air."},
            {"text": "The concert hall speaker, since its much larger "
                     "cone pushes far more air with the same movement", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s22",
        "band": "standard",
        "text": "A phone earpiece speaker is extremely small, yet "
                "produces a clearly audible note when held right against your "
                "ear. Using ideas about pushing air from this lesson, suggest "
                "why a speaker this close to the ear doesn't need to push "
                "nearly as much air as a large speaker across a room.",
        "options": [
            {"text": "It only has to disturb a small volume of air "
                     "right next to the ear, rather than fill a whole room", "correct": True},
            {"text": "It is exempt from needing to push air, unlike "
                     "every other vibrating source", "correct": False,
             "why": "Every source in this lesson works by pushing the "
                    "air — the earpiece is no exception, it simply has far "
                    "less air to disturb."},
            {"text": "The ear itself pushes the air back towards the "
                     "speaker, doing half the work", "correct": False,
             "why": "The ear is a detector in this lesson, not a source "
                    "— it does not push air back towards anything."},
            {"text": "The speaker converts electricity straight into a "
                     "nerve signal without needing to disturb any air at all", "correct": False,
             "why": "A loudspeaker still works by moving a cone and "
                    "disturbing air, even at very close range — it does not "
                    "skip straight to a nerve signal."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s23",
        "band": "standard",
        "text": "A struck drum skin and a struck cymbal are both left "
                "alone after being hit. The drum's sound dies away "
                "within a couple of seconds; the cymbal can still be "
                "faintly heard many seconds later. What does this "
                "suggest about how quickly each is handing its "
                "vibration energy to the air?",
        "options": [
            {"text": "The cymbal is handing its energy to the air much "
                     "faster than the drum is", "correct": False,
             "why": "The cymbal lasts LONGER, which points to it "
                    "losing its energy more slowly, not faster."},
            {"text": "The drum is handing its energy to the air much "
                     "faster than the cymbal is", "correct": True},
            {"text": "Both are handing their energy to the air at "
                     "exactly the same rate", "correct": False,
             "why": "If the rates were the same, the two sounds would "
                    "fade away over similar times — they clearly do "
                    "not here."},
            {"text": "Neither is really losing energy at all — the "
                     "drum's sound is simply too quiet to hear sooner",
             "correct": False,
             "why": "A fading sound is exactly the sign that a source "
                    "is losing its vibration energy to the air over "
                    "time."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s24",
        "band": "standard",
        "text": "A guitarist plucks a string gently, then plucks the "
                "same string much harder. Both notes fade at roughly the same "
                "rate, but one lasts noticeably longer before becoming "
                "inaudible. Which pluck was harder, and why does it last longer "
                "despite fading at the same rate?",
        "options": [
            {"text": "Neither pluck lasts any longer than the other — "
                     "fading at the same rate means both become inaudible at "
                     "exactly the same moment", "correct": False,
             "why": "Fading at the same RATE still leaves more total "
                    "vibration to get through if you start from a bigger "
                    "amplitude."},
            {"text": "The gentler pluck: a smaller starting amplitude "
                     "always takes longer to disappear completely", "correct": False,
             "why": "A smaller starting amplitude has LESS distance to "
                    "fade through before reaching silence, not more."},
            {"text": "The harder pluck: starting with a bigger "
                     "amplitude means there is more vibration to lose before it "
                     "fades down to nothing", "correct": True},
            {"text": "The harder pluck, but only because harder plucks "
                     "always change the string's rate of vibration", "correct": False,
             "why": "Nothing here changes how often the string vibrates "
                    "each second — only how far it moves, its amplitude, is "
                    "affected by how hard it is plucked."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s25",
        "band": "standard",
        "text": "A tuning fork is struck and its base pressed either "
                "onto a large flat board or a small thin coin, one at a time. "
                "Which is more likely to make the note louder, and why?",
        "options": [
            {"text": "It cannot be judged without knowing the exact "
                     "rate the fork is vibrating at", "correct": False,
             "why": "How often the fork vibrates is not what decides "
                    "this comparison — how much surface area is pushing the "
                    "air is."},
            {"text": "The small thin coin, since smaller objects always "
                     "vibrate more freely", "correct": False,
             "why": "Freedom to vibrate is not the property linked to "
                    "loudness here — surface area pushing the air is."},
            {"text": "Neither would change the loudness at all, since "
                     "only the fork's own prongs make the sound", "correct": False,
             "why": "This lesson's own table example shows the "
                    "opposite: whatever the fork is pressed onto joins in "
                    "pushing the air, changing the loudness."},
            {"text": "The large flat board, since it has more surface "
                     "in contact with the air to push", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s26",
        "band": "standard",
        "text": "A loudspeaker cone reproduces the sound of a drum "
                "being struck. Is the cone itself being physically struck by a "
                "drumstick, or is something else making it vibrate?",
        "options": [
            {"text": "Something else — an electrical signal, never a "
                     "drumstick, drives the cone back and forth to copy the "
                     "pattern the drum originally made", "correct": True},
            {"text": "Yes — a tiny hidden striker built into the "
                     "loudspeaker itself physically taps the cone each time, to "
                     "copy the drum", "correct": False,
             "why": "No striker is involved — the cone is driven "
                    "directly by an electrical signal, not tapped by anything "
                    "mechanical."},
            {"text": "Yes, but just for very loud drum sounds", "correct": False,
             "why": "Whatever the loudness, the cone is always driven "
                    "by the electrical signal, never by a physical strike."},
            {"text": "Neither — a loudspeaker cannot reproduce a drum "
                     "sound at all, only continuous notes", "correct": False,
             "why": "A loudspeaker can reproduce a drum's pattern "
                    "perfectly well, by moving its cone to copy the electrical "
                    "signal made from that pattern."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s27",
        "band": "standard",
        "text": "A vocal fold's amplitude is roughly 1 mm; a tuning "
                "fork's is roughly 0.5 mm. If both vibrated the exact same "
                "number of times each second, which would push more air with "
                "each vibration, all else being equal?",
        "options": [
            {"text": "The tuning fork, since a smaller amplitude always "
                     "pushes more air per vibration", "correct": False,
             "why": "A smaller amplitude moves the surrounding air a "
                    "smaller distance, so it pushes less air, not more."},
            {"text": "The vocal folds, since a bigger amplitude "
                     "displaces more air", "correct": True},
            {"text": "Both would push exactly the same amount of air, "
                     "since they vibrate the same number of times each second", "correct": False,
             "why": "How OFTEN each one vibrates is the same here, but "
                    "how FAR each one moves — the amplitude — is different, "
                    "and that changes how much air is pushed."},
            {"text": "It cannot be judged without knowing the surface "
                     "area of each source", "correct": False,
             "why": "'All else being equal' fixes the two surfaces as "
                    "the same, so the two amplitudes on their own settle the "
                    "comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s28",
        "band": "standard",
        "text": "A microphone's diaphragm is moving in time with "
                "arriving sound. A student says the diaphragm is 'making its "
                "own new sound to match what it hears.' What is wrong with this "
                "description?",
        "options": [
            {"text": "The description is right, but only for very loud "
                     "sounds reaching the diaphragm", "correct": False,
             "why": "Loudness makes no difference here — a diaphragm "
                    "always converts arriving sound into a signal, never makes "
                    "sound of its own."},
            {"text": "Nothing is wrong — the diaphragm makes a fresh "
                     "sound each time, matching what arrives", "correct": False,
             "why": "The diaphragm is a detector: it turns arriving "
                    "sound into an electrical signal, rather than producing "
                    "sound of its own."},
            {"text": "The diaphragm isn't making sound at all — it is "
                     "converting the arriving vibration directly into an "
                     "electrical signal", "correct": True},
            {"text": "The description is right about the diaphragm "
                     "itself, but wrong about which particular part of the whole "
                     "microphone is actually doing it", "correct": False,
             "why": "The diaphragm IS the part doing the converting; "
                    "the error is calling that conversion 'making sound' at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s29",
        "band": "standard",
        "text": "A guitar string set vibrating pushes the air next to "
                "it about 3 mm each way. Would doubling this to 6 mm make the "
                "resulting sound louder, quieter, or unaffected?",
        "options": [
            {"text": "It cannot be judged without knowing the exact "
                     "shape of the guitar's body", "correct": False,
             "why": "The amplitude of the string's own vibration is "
                    "enough on its own to reason about loudness here."},
            {"text": "Quieter, since a bigger movement always takes "
                     "longer to complete, giving the air less of a shove each "
                     "time", "correct": False,
             "why": "A bigger swing does not weaken the shove it gives "
                    "the air — it disturbs the air more, not less."},
            {"text": "Unaffected, since loudness depends on how many "
                     "times a second something vibrates, not on how far it moves", "correct": False,
             "why": "This lesson links loudness to how far something "
                    "moves, its amplitude, not only to how often it vibrates."},
            {"text": "Louder, since a bigger vibration always disturbs "
                     "the air more", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-s30",
        "band": "standard",
        "text": "A struck drum skin, amplitude about 0.5 mm, is "
                "compared with a plucked string, amplitude about 3 mm, "
                "both at the very first instant after being set going. "
                "Which starts by disturbing the air more strongly, all "
                "else being equal?",
        "options": [
            {"text": "The string, given its bigger starting amplitude",
             "correct": True},
            {"text": "The drum skin, given its smaller starting "
                     "amplitude", "correct": False,
             "why": "A smaller amplitude disturbs the air less at that "
                    "first instant, not more — the string's bigger "
                    "swing does more at the start."},
            {"text": "Both disturb the air equally strongly, since both "
                     "are described as vibrating sources",
             "correct": False,
             "why": "Being a vibrating source does not make two "
                    "different amplitudes equal — 3 mm and 0.5 mm "
                    "disturb the air by different amounts."},
            {"text": "It cannot be judged without knowing how long each "
                     "one goes on vibrating for", "correct": False,
             "why": "Comparing the very first instant only needs the "
                    "two starting amplitudes, which are already given."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p6-03-h10",
        "band": "harder",
        "text": "A tuning fork vibrates 440 times a second and keeps "
                "ringing for 3 seconds before fading to silence. "
                "Roughly how many total vibrations has it made in that "
                "time?",
        "options": [
            {"text": "147", "correct": False,
             "why": "That divides 440 by 3 instead of multiplying it "
                    "by 3."},
            {"text": "1320", "correct": True},
            {"text": "443", "correct": False,
             "why": "That adds 440 and 3 together instead of "
                    "multiplying them."},
            {"text": "It cannot be found without knowing the fork's "
                     "amplitude", "correct": False,
             "why": "Total vibrations over a time only needs the rate "
                    "and the time; amplitude plays no part in this "
                    "calculation."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h11",
        "band": "harder",
        "text": "A guitar string plucked gently has amplitude 1.5 mm; "
                "the same string plucked hard has amplitude 4.5 mm. "
                "Roughly how many times more air would you expect the "
                "hard pluck to disturb with each swing, all else being "
                "equal?",
        "options": [
            {"text": "about 6 times as much", "correct": False,
             "why": "4.5 divided by 1.5 comes to 3, not 6."},
            {"text": "about 1.5 times as much", "correct": False,
             "why": "4.5 divided by 1.5 comes to 3, not 1.5."},
            {"text": "about 3 times as much", "correct": True},
            {"text": "exactly the same amount, since it is still the "
                     "same string", "correct": False,
             "why": "1.5 mm and 4.5 mm are very different amplitudes — "
                    "the harder pluck genuinely moves further and "
                    "disturbs more air."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h12",
        "band": "harder",
        "text": "A struck drum skin, amplitude about 0.5 mm, is "
                "compared with a loudspeaker cone playing a quiet note, also "
                "about 0.5 mm in amplitude. A student says the two must sound "
                "equally loud, since a similar-sized loudspeaker cone and a "
                "drum skin are 'roughly the same kind of vibrating surface.' "
                "Assess this claim, using the surface-area idea from this "
                "lesson.",
        "options": [
            {"text": "It cannot be judged, because loudness depends "
                     "only on how many times a second something vibrates", "correct": False,
             "why": "This lesson links loudness to amplitude and "
                    "surface area, not only to how often something vibrates "
                    "each second."},
            {"text": "The claim is right — amplitude alone always "
                     "settles loudness, whatever the size of the vibrating "
                     "surface involved", "correct": False,
             "why": "This lesson's own table example shows surface area "
                    "matters too — amplitude on its own is not the whole "
                    "story."},
            {"text": "The claim is right, since a cone and a drum skin "
                     "are built from identical materials in every case", "correct": False,
             "why": "Nothing in this lesson claims cones and drum skins "
                    "share a material — and even if they did, size would still "
                    "matter for loudness."},
            {"text": "The claim overreaches: loudness also depends on "
                     "how much surface area is pushing the air, and a drum skin "
                     "is typically far larger in area than a cone, so equal "
                     "amplitude does not guarantee equal loudness", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h13",
        "band": "harder",
        "text": "A recording of a full orchestra is played back through "
                "a single small earbud speaker. A student says: 'this must "
                "really be several different sounds all being made by the "
                "earbud's cone at once, since so many instruments can be "
                "heard.' Using the idea of a single cone from this lesson, "
                "assess this claim.",
        "options": [
            {"text": "The claim is wrong: the single cone reproduces "
                     "one combined, ever-changing vibration pattern — the "
                     "recorded pattern of the whole orchestra together — rather "
                     "than making several separate sounds at once", "correct": True},
            {"text": "The claim is right: one cone cannot reproduce "
                     "more than one instrument, so several hidden cones must be "
                     "inside the earbud, one for each group of instruments that "
                     "has to be heard at the same time", "correct": False,
             "why": "A single cone can follow one combined pattern that "
                    "represents every instrument together — no extra hidden "
                    "cones are needed."},
            {"text": "The claim is right, but only because earbuds are "
                     "a special exception to how ordinary loudspeakers work", "correct": False,
             "why": "Earbuds work the same way as any other loudspeaker "
                    "cone in this lesson — nothing about them is a special "
                    "exception."},
            {"text": "It cannot be judged without knowing exactly how "
                     "many instruments are in the orchestra", "correct": False,
             "why": "However many instruments are playing, the cone is "
                    "still following one single combined pattern, however "
                    "complicated that pattern is."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h14",
        "band": "harder",
        "text": "A student claims: 'every one of these five sources — a "
                "plucked string, a loudspeaker cone, a struck tuning fork, a "
                "struck drum skin and a set of vocal folds — needs something "
                "continuously supplied to keep it vibrating, or it would stop "
                "instantly.' Assess this claim.",
        "options": [
            {"text": "The claim is right — remove the driving supply "
                     "from any of the five and every one of them stops vibrating "
                     "within a fraction of a second", "correct": False,
             "why": "A struck fork, string or drum skin has no "
                    "continuing supply to remove — they carry on ringing for "
                    "some time on their own once struck."},
            {"text": "The claim is wrong: the string, the fork and the "
                     "drum skin are all set going by a single strike or pluck "
                     "and simply left to ring, fading gradually — only the cone "
                     "and the vocal folds genuinely need a continuing supply", "correct": True},
            {"text": "The claim is right for the cone and the vocal "
                     "folds, but wrong for the fork, and nothing can be said "
                     "either way about the string or the drum skin's own "
                     "behaviour once struck", "correct": False,
             "why": "This lesson does describe the string and the drum "
                    "skin too — both are struck or plucked once and then left "
                    "alone, fading over time, just like the fork."},
            {"text": "The claim is wrong for all five — none of them "
                     "needs anything continuously supplied to keep vibrating, "
                     "ever", "correct": False,
             "why": "The cone genuinely does stop the instant its "
                    "driving signal is removed, and the vocal folds stop the "
                    "instant the air supply runs out."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h15",
        "band": "harder",
        "text": "A tuning fork's prongs move about 0.5 mm and a guitar "
                "string moves about 3 mm, yet both can produce sounds of "
                "similar loudness under the right conditions. Using ideas from "
                "this lesson, suggest one way the fork could compensate for its "
                "much smaller amplitude.",
        "options": [
            {"text": "There is no way for the fork to compensate — its "
                     "amplitude is fixed for good once it is made", "correct": False,
             "why": "This lesson's own table example shows a clear way "
                    "to make the fork louder without changing its amplitude at "
                    "all."},
            {"text": "By vibrating many more times each second, since "
                     "that always makes up for a smaller amplitude, however "
                     "little the prongs themselves happen to move on each swing "
                     "of the vibration", "correct": False,
             "why": "This lesson links loudness to amplitude and "
                    "surface area, not to how often something vibrates each "
                    "second."},
            {"text": "By increasing the surface area pushing the air — "
                     "for example, pressing its base onto a table, so a much "
                     "larger area pushes the air even though the prongs still "
                     "move only a little", "correct": True},
            {"text": "By being struck with a much heavier hammer, which "
                     "always increases the fork's own surface area", "correct": False,
             "why": "Striking harder does not change the fork's own "
                    "surface area — pressing it onto something larger does."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h16",
        "band": "harder",
        "text": "A loudspeaker cone driven by a strong electrical "
                "signal moves further each vibration than the same cone driven "
                "by a weak signal, but both vibrate the same number of times "
                "each second. Which produces the louder sound, and why?",
        "options": [
            {"text": "It cannot be judged without knowing the exact "
                     "voltage used to drive the cone", "correct": False,
             "why": "The amplitude each signal produces is already "
                    "given directly, which is enough to compare the two cases."},
            {"text": "The weak-signal case, because a smaller amplitude "
                     "always gives a cleaner, louder-sounding push", "correct": False,
             "why": "A smaller amplitude means the cone moves less far, "
                    "disturbing the air less, not more."},
            {"text": "Neither — loudness depends only on how often the "
                     "cone vibrates each second, never on how far it moves", "correct": False,
             "why": "This lesson links loudness to amplitude as well as "
                    "rate; with the rate fixed here, amplitude is what makes "
                    "the difference."},
            {"text": "The strong-signal case, because a bigger "
                     "amplitude of vibration always disturbs the air more", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h17",
        "band": "harder",
        "text": "A struck drum skin, amplitude about 0.5 mm, is placed "
                "so its edge just touches a small suspended ball. "
                "Predict what you would expect to observe about the "
                "ball while the drum is ringing, and explain why, using "
                "an idea from this lesson about invisible vibrations.",
        "options": [
            {"text": "The ball should visibly jump or vibrate, since "
                     "the movement — though too small to see directly "
                     "on the skin — is still large enough to disturb "
                     "something touching it", "correct": True},
            {"text": "The ball should stay perfectly still, since a "
                     "movement too small to see on the skin cannot "
                     "possibly affect anything else either",
             "correct": False,
             "why": "This lesson's tuning-fork-in-water example shows "
                    "exactly the opposite: a movement too small to see "
                    "directly can still visibly disturb something it "
                    "touches."},
            {"text": "The ball should gradually heat up over time, "
                     "since the drum's own vibration energy is being "
                     "steadily converted into warmth at the exact point "
                     "of contact between them", "correct": False,
             "why": "Nothing in this lesson describes vibration energy "
                    "turning into noticeable heat — the expected effect "
                    "is movement, not warming."},
            {"text": "Nothing can be predicted at all without first "
                     "measuring the exact size of the ball",
             "correct": False,
             "why": "The size of the ball is not needed to predict "
                    "whether it will move at all — a genuinely "
                    "vibrating surface touching it should disturb it "
                    "visibly."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h18",
        "band": "harder",
        "text": "A phone's loudspeaker plays a recording of a plucked "
                "guitar string. A student says: 'somewhere inside the phone, a "
                "tiny string must be vibrating to make this sound.' Assess this "
                "claim, using the idea of the chain from vibration to signal "
                "and back again.",
        "options": [
            {"text": "The claim is right — every recorded instrument "
                     "must have a matching miniature version of itself built "
                     "into the phone's speaker", "correct": False,
             "why": "A single cone reproduces the PATTERN of the "
                    "recorded vibration; it does not need a miniature copy of "
                    "the original instrument inside it."},
            {"text": "The claim is wrong: no string is present inside "
                     "the phone at all — the original vibration was converted to "
                     "an electrical signal long ago, and is now driving a fresh "
                     "vibration of the phone's own cone instead", "correct": True},
            {"text": "The claim is right, but only for string "
                     "instruments — other recordings really do use a matching "
                     "source inside the phone", "correct": False,
             "why": "The same cone reproduces every recorded pattern, "
                    "whatever instrument it came from — none of them need a "
                    "matching source built in."},
            {"text": "It cannot be judged without opening up the phone "
                     "to look inside its speaker", "correct": False,
             "why": "The chain described in this lesson — vibration to "
                    "signal, and signal back to a fresh vibration — already "
                    "settles this without needing to look inside."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h19",
        "band": "harder",
        "text": "A tuning fork is struck and dipped briefly into a bowl "
                "of water, then removed, dried, and struck again — this "
                "time held motionless just above the water's surface "
                "without touching it. In which case, if any, would you "
                "expect to see the water visibly disturbed?",
        "options": [
            {"text": "Only the second case, since holding the fork "
                     "still above the water lets it disturb a wider "
                     "area", "correct": False,
             "why": "Without touching the water at all, there is "
                    "nothing pushing it directly — the visible splash "
                    "in this lesson comes from actual contact."},
            {"text": "Both cases equally, since the fork is vibrating "
                     "just as much either way", "correct": False,
             "why": "Direct contact lets the prongs push the water "
                    "itself; air alone moving past, without contact, is "
                    "far too gentle to visibly disturb the surface."},
            {"text": "Only the first case, when the fork actually "
                     "touches the water directly", "correct": True},
            {"text": "Neither case, since a struck fork's movement is "
                     "always too small to disturb water at all",
             "correct": False,
             "why": "Dipping the fork directly into water is exactly "
                    "how this lesson shows the vibration IS large "
                    "enough to disturb it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h20",
        "band": "harder",
        "text": "Two identical strings are compared under different "
                "tension: a loose one and a tight one, both plucked with the "
                "same force. The tight string vibrates back and forth many more "
                "times each second than the loose one. A student assumes this "
                "also means the tight string must have the bigger amplitude. "
                "Assess this assumption, treating amplitude and rate as two "
                "separate measurements.",
        "options": [
            {"text": "It cannot be assessed at all without measuring "
                     "the exact tension of each string", "correct": False,
             "why": "The lesson's treatment of amplitude and rate as "
                    "independent measurements is enough to assess the "
                    "assumption, without needing the exact tensions."},
            {"text": "The assumption is safe — a source that vibrates "
                     "more often always moves further with each vibration too", "correct": False,
             "why": "This lesson describes rate and amplitude as two "
                    "separate measurements for a source; one changing does not "
                    "force the other to change with it."},
            {"text": "The assumption is safe, but only because both "
                     "strings are described as being plucked with the same "
                     "force, which fixes both the rate and the amplitude at the "
                     "same value for each of the two strings", "correct": False,
             "why": "Being plucked with the same force does not settle "
                    "how the two strings' amplitudes compare — the two "
                    "measurements remain independent of one another."},
            {"text": "The assumption is not safe: amplitude and "
                     "how-many-times-a-second are two separate readouts for a "
                     "source, so a bigger rate never by itself means a bigger "
                     "amplitude", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h21",
        "band": "harder",
        "text": "A struck cymbal vibrates about 300 times each second, "
                "and makes roughly 1800 vibrations in total before it becomes "
                "too quiet to hear. For roughly how long was it audible?",
        "options": [
            {"text": "6 seconds", "correct": True},
            {"text": "540 000 seconds", "correct": False,
             "why": "That multiplies 1800 by 300 instead of dividing "
                    "1800 by it."},
            {"text": "1500 seconds", "correct": False,
             "why": "That subtracts 300 from 1800 instead of dividing "
                    "1800 by it."},
            {"text": "It cannot be found without knowing the cymbal's "
                     "amplitude", "correct": False,
             "why": "A time comes from the total number of vibrations "
                    "and the rate; amplitude plays no part in this "
                    "calculation."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h22",
        "band": "harder",
        "text": "A loudspeaker cone vibrates 150 times a second at one "
                "setting. A different setting drives the same cone at 450 times "
                "a second, with the same amplitude each time. A student says "
                "the second setting is disturbing the air 3 times as often. Is "
                "this reasoning about the RATE correct, even without knowing "
                "anything about how loud each one sounds?",
        "options": [
            {"text": "No — 450 is only about 1.5 times 150, not 3 times", "correct": False,
             "why": "450 divided by 150 comes to exactly 3, not 1.5."},
            {"text": "Yes — 450 is exactly 3 times 150, so the cone is "
                     "genuinely vibrating, and so disturbing the air, three "
                     "times as often in the second case", "correct": True},
            {"text": "No — comparing how often two sources vibrate each "
                     "second always needs both amplitudes to be measured and "
                     "known first", "correct": False,
             "why": "Comparing two RATES only needs the two rate "
                    "figures given, both of which are stated directly here."},
            {"text": "It cannot be judged, since the amplitudes given "
                     "for the two settings are different", "correct": False,
             "why": "The question states the amplitude is the same each "
                    "time — only the rate differs between the two settings."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h23",
        "band": "harder",
        "text": "A tuning fork's prongs move a certain amplitude when "
                "struck gently, and about three times that amplitude when "
                "struck hard. A student argues: 'since the fork vibrates the "
                "same number of times each second in both cases, the two "
                "strikes must be handing energy to the air at exactly the same "
                "rate.' Assess this argument using the amplitude idea from this "
                "lesson.",
        "options": [
            {"text": "The argument is right, but only because tuning "
                     "forks are a special case among the five sources named "
                     "here, which behave differently from every other vibrating "
                     "object of their kind", "correct": False,
             "why": "Nothing marks tuning forks out as an exception — "
                    "amplitude affects how much air is disturbed for every "
                    "source in this lesson."},
            {"text": "The argument is right — only the rate of "
                     "vibration decides how fast energy is handed to the air, "
                     "whatever the amplitude, since each swing hands over the "
                     "same fixed parcel of energy however far it travels", "correct": False,
             "why": "This lesson links loudness, and so how much air is "
                    "disturbed, to amplitude as well as to rate — amplitude is "
                    "not irrelevant here."},
            {"text": "The argument is wrong: a bigger amplitude "
                     "disturbs the air more with each swing, so the harder "
                     "strike hands over more energy each second even though the "
                     "rate is unchanged", "correct": True},
            {"text": "It cannot be assessed without knowing the "
                     "material the fork is made from", "correct": False,
             "why": "The material of the fork is not needed here — the "
                    "amplitude comparison given is already enough to assess "
                    "the argument."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h24",
        "band": "harder",
        "text": "A vocal fold vibrates about 120 times a second and "
                "moves about 1 mm each vibration; a tuning fork vibrates 440 "
                "times a second and moves about 0.5 mm each vibration. A "
                "student says the fork must be pushing more total air each "
                "second, since it vibrates so much more often despite its "
                "smaller movement. Assess this claim as far as the numbers "
                "given allow.",
        "options": [
            {"text": "Neither source pushes air unless its surface area "
                     "is given first", "correct": False,
             "why": "Both sources clearly do push air, as this lesson "
                    "describes for every source — what is missing here is "
                    "enough information to compare the TOTAL amount each "
                    "pushes."},
            {"text": "The claim is definitely right — vibrating more "
                     "often always outweighs moving a smaller distance, whatever "
                     "else is going on", "correct": False,
             "why": "This lesson gives no rule that rate always "
                    "outweighs amplitude — both matter, along with surface "
                    "area, which is not given here."},
            {"text": "The claim is definitely wrong — moving further "
                     "each vibration always outweighs vibrating more often, "
                     "whatever else is going on", "correct": False,
             "why": "This lesson gives no rule that amplitude always "
                    "outweighs rate either — with surface area unknown, "
                    "neither claim can be settled outright."},
            {"text": "This cannot be fully settled just from these "
                     "numbers: total air pushed depends on the size of each push "
                     "AND how often it happens, together with the surface area "
                     "involved, which is not given here for either source", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h25",
        "band": "harder",
        "text": "A struck drum skin produces a certain loudness. Which "
                "of the following would most reliably make it louder, "
                "based on ideas from this lesson?",
        "options": [
            {"text": "Using a larger drum skin, so more surface area "
                     "pushes the air", "correct": True},
            {"text": "Striking it more gently, since gentler strikes "
                     "are always louder", "correct": False,
             "why": "A gentler strike gives the skin a smaller "
                    "amplitude, which disturbs the air less, not more."},
            {"text": "Using a smaller drum skin, since less material "
                     "vibrating is always louder", "correct": False,
             "why": "This lesson links a LARGER surface area to more "
                    "air being pushed, not a smaller one."},
            {"text": "Playing it somewhere with as little air present "
                     "as possible, since air just gets in the way of "
                     "the vibration", "correct": False,
             "why": "Air is essential in this lesson's chain — it is "
                    "what carries the disturbance onward at all, not "
                    "something in the way of it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h26",
        "band": "harder",
        "text": "A struck tuning fork rings audibly for several seconds "
                "even though its own prongs push very little air directly. A "
                "student says: 'since the prongs push so little air, almost "
                "none of the fork's vibration energy can be reaching your ear "
                "at all.' Assess this claim.",
        "options": [
            {"text": "The claim is right — a fork's thin prongs push so "
                     "little air that essentially none of its vibration energy "
                     "can ever possibly reach a listener's ear at all, however "
                     "quiet the room happens to be", "correct": False,
             "why": "The fork is stated to ring audibly for several "
                    "seconds, which is direct evidence that enough energy is "
                    "reaching the ear to be heard."},
            {"text": "The claim overstates the case: a small amount of "
                     "air being pushed can still carry enough energy over a few "
                     "metres to be clearly heard, especially in a quiet room", "correct": True},
            {"text": "The claim is right, but only in rooms with the "
                     "windows open", "correct": False,
             "why": "Nothing about open windows is relevant here — the "
                    "fork's small push of air is simply enough to be heard, in "
                    "an ordinary quiet room."},
            {"text": "It cannot be judged, because sound cannot travel "
                     "through air at all unless the source pushes it very hard", "correct": False,
             "why": "This lesson describes even small movements — a "
                    "tuning fork's thin prongs among them — as capable of "
                    "producing an audible sound through the air."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h27",
        "band": "harder",
        "text": "A guitar string set vibrating produces sound for "
                "several seconds before fading to silence. A tuning fork set "
                "vibrating with the same starting amplitude produces sound for "
                "much longer before fading. A student concludes the fork must "
                "be losing its energy to the air more slowly than the string "
                "does. Assess this conclusion using surface-area ideas from "
                "this lesson.",
        "options": [
            {"text": "The conclusion is wrong, because the string's "
                     "greater length always means it must ring for longer, not "
                     "the fork", "correct": False,
             "why": "Length on its own is not what this lesson links to "
                    "how quickly a source fades — how much surface is pushing "
                    "the air is."},
            {"text": "The conclusion is wrong — a fork and a string "
                     "always lose their vibration energy at exactly the same "
                     "rate, whatever their shape", "correct": False,
             "why": "This lesson links how quickly a source fades to "
                    "how much air it pushes, which depends on its surface area "
                    "— a fork and a string differ there."},
            {"text": "The conclusion is reasonable: the fork's thin "
                     "prongs present much less surface to the air than the "
                     "string's length, so with a similar starting amplitude it "
                     "is likely losing energy more slowly", "correct": True},
            {"text": "It cannot be assessed without measuring the "
                     "temperature of both the fork and the string", "correct": False,
             "why": "Temperature plays no part in this lesson's "
                    "explanation of why some sources fade faster than others."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h28",
        "band": "harder",
        "text": "A struck cymbal and a struck tuning fork are compared. "
                "The cymbal, despite being struck with similar force, produces "
                "a noticeably louder sound. A student attributes this entirely "
                "to the cymbal being made of a 'louder metal.' Assess this "
                "explanation using surface-area ideas.",
        "options": [
            {"text": "It cannot be assessed, because no example "
                     "involving more than one metal source has been given", "correct": False,
             "why": "Surface area, already established in this lesson "
                    "with the tuning-fork-and-table example, is enough to "
                    "assess the explanation without needing further metal "
                    "examples."},
            {"text": "The explanation is convincing — some metals are "
                     "simply louder than others, whatever their size, and bronze "
                     "is known to be the loudest of all the metals a cymbal "
                     "might be cast from", "correct": False,
             "why": "This lesson makes no such claim about metals being "
                    "inherently louder — its explanations for loudness are "
                    "about amplitude and surface area."},
            {"text": "The explanation is convincing, since both the "
                     "cymbal and the fork are struck with a similar amount of "
                     "force in this comparison, which rules out anything other "
                     "than the metal itself as the cause", "correct": False,
             "why": "Similar force being used does not support a "
                    "'louder metal' explanation — it actually points toward "
                    "some OTHER factor, such as surface area, making the "
                    "difference."},
            {"text": "The explanation is unconvincing on its own: a "
                     "material on its own is not what decides loudness — the "
                     "cymbal's much larger surface area pushing more air is a "
                     "far more likely factor", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h29",
        "band": "harder",
        "text": "A struck tuning fork, dipped briefly in water to show "
                "it is vibrating, is dried off and struck again — this time its "
                "ring is timed and found to last only half as long as before "
                "dipping. A student suggests the fork should be kept wet "
                "permanently, since water must somehow make it ring longer. "
                "Assess this suggestion.",
        "options": [
            {"text": "The suggestion is not well supported: dipping the "
                     "fork in water actually dampens it, losing some of its "
                     "vibration energy pushing the water aside, so the timing "
                     "difference more likely reflects the dipping itself rather "
                     "than water helping it ring", "correct": True},
            {"text": "The suggestion is well supported — water clearly "
                     "adds extra vibration energy to a fork every time it is "
                     "dipped in", "correct": False,
             "why": "Dipping a fork in water takes energy OUT of its "
                    "vibration to disturb the water — it does not add energy "
                    "to the fork."},
            {"text": "The suggestion is well supported, but only for "
                     "forks that ring for less than five seconds when dry", "correct": False,
             "why": "There is no such time threshold in this lesson — "
                    "dipping a fork in water dampens it regardless of how long "
                    "it would otherwise have rung for."},
            {"text": "It cannot be assessed, because a struck tuning "
                     "fork never loses any of its vibration energy once it has "
                     "started ringing", "correct": False,
             "why": "A struck fork continually hands its vibration "
                    "energy to whatever it disturbs, air or water alike, which "
                    "is exactly why it eventually falls silent."},
        ],
        "figure": None,
    },
    {
        "id": "p6-03-h30",
        "band": "harder",
        "text": "A concert tuning fork's rate — 440 times a second — is "
                "fixed and reliable, which is exactly why it is used for tuning "
                "instruments. A student asks why a guitar string or a drum skin "
                "would not work as well for this exact purpose. Suggest an "
                "answer, considering how consistent each source's vibration is.",
        "options": [
            {"text": "A guitar string and a drum skin are just as "
                     "reliable as a tuning fork for this purpose", "correct": False,
             "why": "Only the tuning fork is described in this lesson "
                    "as being built to vibrate at one rate and almost nothing "
                    "else — the string and drum are not described that way."},
            {"text": "A guitar string and a drum skin are not built to "
                     "hold one single, dependable rate the way a tuning fork is", "correct": True},
            {"text": "A guitar string and a drum skin cannot vibrate "
                     "unless they are struck again and again continuously, quite "
                     "unlike a tuning fork", "correct": False,
             "why": "This lesson describes the string and the drum skin "
                    "as being struck or plucked ONCE and left to ring, just "
                    "like the fork — continuous striking is not what is "
                    "described."},
            {"text": "It cannot be answered, because nothing given here "
                     "says how a tuning fork vibrates", "correct": False,
             "why": "This lesson describes the fork in detail, "
                    "including its being built to vibrate at one dependable "
                    "rate — that description is exactly what answers the "
                    "question."},
        ],
        "figure": None,
    },
]
