"""P6 lesson 07 — Echoes, reflection and absorption: twelve questions.

Written against Design's page. The cliff, the five surfaces, the bar and
both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · reflected, absorbed and transmitted are three separate fates;
  · an echo needs BOTH enough sound back AND enough delay;
  · the sound goes out and back, so the path is twice the distance
    (`WAVE-27`);
  · absorbing is not blocking, and a wall makes nothing of its own
    (`WAVE-25`, `WAVE-26`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — 0,1,2,3 · 3,2,1,0 · 2,0,3,1, three of each.

⚠️ The ladder's own two marked rungs are NOT restated, nor are the worked
examples' figures (680 m in 2.0 s, 1.02 km).
"""

UNIT = "P6"
LESSON = "echoes-reflection-and-absorption"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p6-07-e01",
        "band": "easier",
        "text": "An echo is…",
        "options": [
            {"text": "reflected sound heard as a separate sound",
             "correct": True},
            {"text": "a new sound made by the wall", "correct": False,
             "why": "The wall makes nothing. An echo is your own voice, "
                    "coming back."},
            {"text": "sound that has been absorbed and released again",
             "correct": False,
             "why": "Absorbed sound is gone for good, ending as a tiny "
                    "amount of heating. Nothing is released."},
            {"text": "sound that has travelled right through a wall",
             "correct": False,
             "why": "That is transmitted sound, and it carries on away from "
                    "you rather than back to you."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e02",
        "band": "easier",
        "text": "Which surface would give the strongest echo?",
        "options": [
            {"text": "a heavy curtain", "correct": False,
             "why": "Soft and folded, so it absorbs most of what reaches "
                    "it."},
            {"text": "a bare rock face", "correct": True},
            {"text": "a bank of foam wedges", "correct": False,
             "why": "Foam wedges are built to absorb almost everything — "
                    "about 3% comes back."},
            {"text": "long mown grass", "correct": False,
             "why": "Grass is soft and open-textured, so most of the sound "
                    "is absorbed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e03",
        "band": "easier",
        "text": "Sound arriving at a surface can be reflected, absorbed or…",
        "options": [
            {"text": "destroyed", "correct": False,
             "why": "Nothing is destroyed. Absorbed sound has become a very "
                    "small amount of heating."},
            {"text": "frozen", "correct": False,
             "why": "Sound is not a substance and cannot be frozen."},
            {"text": "transmitted", "correct": True},
            {"text": "amplified", "correct": False,
             "why": "A plain surface adds no energy, so nothing gets louder "
                    "on arrival."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e04",
        "band": "easier",
        "text": "An echo comes back after the sound has travelled 900 m in "
                "total. How far away is the wall?",
        "options": [
            {"text": "1800 m", "correct": False,
             "why": "That doubles a total that has already been doubled."},
            {"text": "900 m", "correct": False,
             "why": "The 900 m is the whole journey, out and back. The wall "
                    "is halfway along it."},
            {"text": "300 m", "correct": False,
             "why": "That divides by three. The journey has two equal parts, "
                    "not three."},
            {"text": "450 m", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p6-07-s01",
        "band": "standard",
        "text": "A hard wall is only 5 m away and there is no separate echo. "
                "Why not?",
        "options": [
            {"text": "The wall is too hard, and hard surfaces absorb sound "
                     "rather than sending it back, so nothing returns to be "
                     "heard",
             "correct": False,
             "why": "Hard surfaces reflect strongly. Plenty is coming back."},
            {"text": "Sound cannot travel as short a distance as 5 m",
             "correct": False,
             "why": "Sound crosses 5 m easily — you can hear someone talking "
                    "at that range."},
            {"text": "The wall is too small to reflect sound", "correct": False,
             "why": "Size is not stated and is not the reason. The problem "
                    "is in the timing."},
            {"text": "The reflection gets back in far less than a tenth of a "
                     "second, so the ear runs it together with the original",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s02",
        "band": "standard",
        "text": "Why do the two conditions for an echo have to be checked "
                "separately?",
        "options": [
            {"text": "Because they are really the same condition written "
                     "twice", "correct": False,
             "why": "They are independent: distance and material can be "
                    "varied one at a time, and each can fail on its own."},
            {"text": "Because a surface can fail one and pass the other — "
                     "foam at 300 m is far enough and too absorbent, and "
                     "rock at 5 m is reflective enough and too close",
             "correct": True},
            {"text": "Because the second one only applies indoors",
             "correct": False,
             "why": "The tenth-of-a-second rule is about your ear, and it "
                    "applies wherever you are."},
            {"text": "Because one is about sound and the other is about "
                     "light, and the two travel by such different rules "
                     "that each needs a condition written for it alone "
                     "rather than one that covers both", "correct": False,
             "why": "Both are about sound. No light is involved."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s03",
        "band": "standard",
        "text": "A shout is heard back from a wall 1.0 s after it is made. "
                "Sound travels at about 340 m/s. How far away is the wall?",
        "options": [
            {"text": "340 m", "correct": False,
             "why": "That is the whole path, out and back, in one second. "
                    "The wall is halfway along it."},
            {"text": "680 m", "correct": False,
             "why": "That doubles when it should halve."},
            {"text": "170 m", "correct": True},
            {"text": "170 m/s", "correct": False,
             "why": "The number is right and the unit is wrong. The question "
                    "asks how far, which is a distance."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s04",
        "band": "standard",
        "text": "A recording booth is lined with foam wedges. What is the "
                "foam doing?",
        "options": [
            {"text": "Absorbing almost all the sound that reaches it, so "
                     "very little comes back into the room", "correct": True},
            {"text": "Stopping sound from outside getting in, so that the "
                     "room stays quiet the whole time a take is running",
             "correct": False,
             "why": "Blocking is done by mass, not by softness. Thin foam "
                    "does almost nothing to keep noise out."},
            {"text": "Reflecting the sound evenly in all directions, so "
                     "that no one corner of the room sounds odd",
             "correct": False,
             "why": "It is doing the opposite of reflecting — the wedges "
                    "exist to stop reflections."},
            {"text": "Making the room quieter by lowering the frequency of "
                     "the sound until it falls below what anyone can hear", "correct": False,
             "why": "Nothing changes the frequency of the sound. What "
                    "changes is how much of it survives."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p6-07-h01",
        "band": "harder",
        "text": "A neighbour's television is clearly audible through a wall. "
                "Someone suggests fixing thin acoustic foam to your side of "
                "the wall. Will it help?",
        "options": [
            {"text": "Yes — foam absorbs sound, so a good deal less of the "
                     "television's noise will manage to get through to "
                     "your side", "correct": False,
             "why": "The foam absorbs sound that is already in your room. "
                    "The television's sound arrives through the wall itself."},
            {"text": "Yes, but only if it is fixed to the neighbour's side, "
                     "because foam has to be between the source and the "
                     "wall to work",
             "correct": False,
             "why": "The side does not rescue it. Thin foam is a poor "
                    "blocker either way."},
            {"text": "Hardly at all — blocking needs mass, and thin foam "
                     "has almost none; what it fixes is echo inside a room",
             "correct": True},
            {"text": "No, because sound cannot pass through a solid wall "
                     "at all, so the foam would have nothing to stop",
             "correct": False,
             "why": "Sound clearly does pass through, which is the whole "
                    "problem being described."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h02",
        "band": "harder",
        "text": "Why is an echo recognisably your own voice rather than "
                "something the wall produced?",
        "options": [
            {"text": "Because the sound that comes back is the same sound, "
                     "sent back the way it came, just quieter", "correct": True},
            {"text": "Because the wall copies whatever sound it hears and "
                     "then sends its own version of it straight back to "
                     "you", "correct": False,
             "why": "Copying would need the wall to make sound, and it makes "
                    "none."},
            {"text": "Because your brain fills in what it expects to hear "
                     "and quietly supplies your own voice for you",
             "correct": False,
             "why": "A microphone records the echo just as faithfully, with "
                    "no brain involved."},
            {"text": "Because the wall vibrates at the same frequency and "
                     "so produces the same note, copying whatever arrives "
                     "at it", "correct": False,
             "why": "This would predict a single note, not your words and "
                    "your accent coming back."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h03",
        "band": "harder",
        "text": "A concert hall designer says the aim is not silence. What "
                "is the aim?",
        "options": [
            {"text": "To remove every reflection, so only the direct sound "
                     "arrives", "correct": False,
             "why": "A hall with no reflections at all sounds dead, and "
                    "musicians dislike playing in one."},
            {"text": "To make every surface as hard as possible, so nothing "
                     "is lost", "correct": False,
             "why": "That is the swimming-pool problem: far too much arrives "
                    "late and the sound is a mess."},
            {"text": "To make the hall as small as possible so no "
                     "reflection is late, because a late reflection is "
                     "always the problem", "correct": False,
             "why": "A hall has to hold an audience, and shortening every "
                    "path is not how the balance is struck."},
            {"text": "To choose how much of each surface is hard and how "
                     "much soft, so sound dies away over about the right "
                     "time", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h04",
        "band": "harder",
        "text": "A ship's echo sounder is calibrated for sea water at about "
                "1500 m/s and is used by mistake over a very warm, very "
                "salty patch where sound travels faster. What happens to its "
                "readings?",
        "options": [
            {"text": "Nothing at all changes — the timing is what matters "
                     "and not the speed, and the timing itself has not "
                     "changed here", "correct": False,
             "why": "The timing has to be turned into a distance, and the "
                    "speed is what does the turning."},
            {"text": "Every depth is reported too shallow, because the real "
                     "pulse covered more distance in the time than the "
                     "sounder assumes", "correct": True},
            {"text": "Every depth is reported too deep, because faster "
                     "sound takes longer to return and the sounder simply "
                     "waits for it", "correct": False,
             "why": "Faster sound returns sooner, not later."},
            {"text": "The sounder stops working altogether, because the "
                     "speed of sound it meets is outside the range it was "
                     "built for", "correct": False,
             "why": "It goes on reporting perfectly confident numbers, which "
                    "is exactly what makes the error dangerous."},
        ],
        "figure": None,
    },
]
