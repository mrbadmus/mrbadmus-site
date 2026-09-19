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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-07-e05",
        "band": "easier",
        "text": "A surface that gives a strong echo is…",
        "options": [
            {"text": "soft and open, like a heavy curtain", "correct": False,
             "why": "Soft open materials absorb sound, which is why a "
                    "curtained room is quiet."},
            {"text": "hard, flat and heavy", "correct": True},
            {"text": "warm rather than cold", "correct": False,
             "why": "Temperature is not what decides how much a surface "
                    "reflects."},
            {"text": "rough and full of small holes", "correct": False,
             "why": "That is what acoustic foam is like, and it is designed "
                    "to absorb rather than reflect."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e06",
        "band": "easier",
        "text": "A shout reflects from a wall and comes back. The total "
                "distance the sound travels is…",
        "options": [
            {"text": "the distance to the wall", "correct": False,
             "why": "That is only the outward leg; the sound has to come back "
                    "before it is heard."},
            {"text": "half the distance to the wall", "correct": False,
             "why": "The path is longer than the distance to the wall, not "
                    "shorter."},
            {"text": "twice the distance to the wall", "correct": True},
            {"text": "four times the distance to the wall", "correct": False,
             "why": "There are two journeys, out and back, not four."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-07-s05",
        "band": "standard",
        "text": "An echo returns from a cliff 2.0 s after the shout. Sound "
                "travels at about 340 m/s. How far away is the cliff?",
        "options": [
            {"text": "680 m", "correct": False,
             "why": "That is the whole path, out and back. The cliff is half "
                    "of it away."},
            {"text": "340 m", "correct": True},
            {"text": "170 m", "correct": False,
             "why": "That halves it twice — once for the two journeys and "
                    "once too often."},
            {"text": "1360 m", "correct": False,
             "why": "That doubles the total path instead of halving it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s06",
        "band": "standard",
        "text": "Why does hanging a heavy curtain across a bare wall reduce "
                "the echo in a room?",
        "options": [            {"text": "Because sound cannot travel through fabric at all",
             "correct": False,
             "why": "Some passes through and some is absorbed — an echo needs "
                    "sound sent BACK."},
            {"text": "Because the curtain makes the room smaller, so there is "
                     "no time for an echo",
             "correct": False,
             "why": "A curtain hardly changes the distance; what changes is "
                    "how much comes back."},
            {"text": "Because the curtain stops the sound being made in the "
                     "first place",
             "correct": False,
             "why": "The source is unaffected; the curtain acts on the sound "
                    "after it arrives."},
            {"text": "Because the curtain absorbs sound instead of reflecting "
                     "it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-07-h05",
        "band": "harder",
        "text": "A ship's pulse returns after 0.60 s through sea water at "
                "about 1500 m/s. How deep is the water?",
        "options": [
            {"text": "900 m", "correct": False,
             "why": "That is the whole path. The pulse went down and came "
                    "back, so the depth is half of it."},
            {"text": "450 m", "correct": True},
            {"text": "2500 m", "correct": False,
             "why": "That is 1500 ÷ 0.60, dividing where the calculation "
                    "multiplies."},
            {"text": "225 m", "correct": False,
             "why": "That halves the answer a second time; only one halving "
                    "is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h06",
        "band": "harder",
        "text": "A student forgets that an echo makes two journeys. What "
                "happens to their answer?",
        "options": [
            {"text": "It comes out half the true distance", "correct": False,
             "why": "Forgetting to halve leaves the answer too big, not too "
                    "small."},
            {"text": "It comes out twice the true distance", "correct": True},
            {"text": "It comes out four times the true distance",
             "correct": False,
             "why": "The path is doubled, not quadrupled, so the error is a "
                    "factor of two."},
            {"text": "It is unaffected, because the speed cancels out",
             "correct": False,
             "why": "The speed appears once either way; it is the path length "
                    "that has been got wrong."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p6-07-e07",
        "band": "easier",
        "text": "A tiled bathroom has hard walls, a hard floor and a hard "
                "ceiling. Shouting in it usually sounds…",
        "options": [
            {"text": "echoey, because the hard tiled surfaces reflect most "
                     "of the sound", "correct": True},
            {"text": "quieter than shouting outside, because tiles muffle "
                     "every note", "correct": False,
             "why": "Hard tiles reflect sound rather than muffling it, "
                    "which is why a tiled room sounds louder and more "
                    "echoey, not quieter."},
            {"text": "muffled, because tiles absorb the higher notes in a "
                     "voice well", "correct": False,
             "why": "Tiles are hard and reflect sound; absorbing is what "
                    "soft, open-textured materials do instead."},
            {"text": "silent in there, because tiles are said to block "
                     "sound completely", "correct": False,
             "why": "Tiles reflect sound back into the room rather than "
                    "blocking it, which is exactly why the room sounds "
                    "echoey."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e08",
        "band": "easier",
        "text": "A car has fabric seats, a carpeted floor and a padded "
                "roof lining. Talking inside it sounds…",
        "options": [
            {"text": "louder than in a bare room, because fabric and "
                     "carpet reflect sound well", "correct": False,
             "why": "Fabric and carpet are soft and open-textured, so "
                    "they absorb sound rather than sending it back."},
            {"text": "close and dead, because the soft linings absorb "
                     "most of what reaches them", "correct": True},
            {"text": "unchanged from a tiled room, because a car is too "
                     "small for its surfaces to matter", "correct": False,
             "why": "A tiled room of the same size would sound sharply "
                    "echoey; the soft linings are what make the "
                    "difference."},
            {"text": "higher-pitched, because soft materials raise the "
                     "frequency of a voice", "correct": False,
             "why": "Nothing in the car changes the frequency of a "
                    "sound; what changes is how much of it survives as a "
                    "reflection."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e09",
        "band": "easier",
        "text": "A person talks in a room with a closed glass window. "
                "Someone standing just outside can faintly hear them. The "
                "sound reaching that person outside has mostly been…",
        "options": [
            {"text": "reflected back into the room by the window",
             "correct": False,
             "why": "Reflected sound goes back the way it came, so it "
                    "would return into the room, not reach a listener "
                    "outside."},
            {"text": "absorbed by the glass and turned into a little "
                     "heating", "correct": False,
             "why": "Absorbed sound is gone rather than heard outside — "
                    "none of it would reach the listener that way."},
            {"text": "transmitted through the glass to the outside",
             "correct": True},
            {"text": "frozen in the glass until the window opens",
             "correct": False,
             "why": "Sound is not a substance and cannot be frozen or "
                    "stored inside a material."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e10",
        "band": "easier",
        "text": "Thick loft insulation is fitted in the ceiling between a "
                "noisy workshop and a quiet room above it. The insulation "
                "works mainly by…",
        "options": [
            {"text": "reflecting the sound back into the noisy room it "
                     "came from", "correct": False,
             "why": "Reflecting sends it back rather than reducing what "
                    "continues upward — the insulation instead takes up "
                    "the sound's energy."},
            {"text": "transmitting the sound through unchanged, at full "
                     "strength", "correct": False,
             "why": "That would mean the insulation is doing nothing at "
                    "all, which is the opposite of what is observed."},
            {"text": "amplifying the sound before it reaches the quiet "
                     "room next door", "correct": False,
             "why": "Nothing adds energy to the sound; less of it "
                    "survives, not more."},
            {"text": "absorbing the sound, so far less of it reaches the "
                     "quiet room", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e11",
        "band": "easier",
        "text": "For a returning reflection to be heard as a separate echo, "
                "roughly what fraction of the original sound has to come "
                "back?",
        "options": [
            {"text": "at least about 15%", "correct": True},
            {"text": "at least about 90%", "correct": False,
             "why": "90% is closer to what a very reflective surface like "
                    "bare rock sends back; the minimum needed for a "
                    "separate echo is far lower."},
            {"text": "any small amount, however little", "correct": False,
             "why": "A surface such as foam sends back only about 3%, and "
                    "that is too little to be heard as a separate echo."},
            {"text": "exactly 50%", "correct": False,
             "why": "There is no such exact halfway requirement; the rough "
                    "threshold is much lower than this."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e12",
        "band": "easier",
        "text": "Roughly how far away does a hard surface usually need to "
                "be before a shout returns as a separate, distinct echo "
                "rather than one slightly fuller sound?",
        "options": [
            {"text": "about 1.7 m or more", "correct": False,
             "why": "At that distance the reflection would return in well "
                    "under a tenth of a second, too soon to be heard "
                    "separately."},
            {"text": "about 17 m or more", "correct": True},
            {"text": "about 170 m or more", "correct": False,
             "why": "A separate echo is heard well before this distance; "
                    "17 m is closer to the real threshold."},
            {"text": "any short distance", "correct": False,
             "why": "At a very short distance the reflection arrives too "
                    "soon and simply thickens the original sound rather "
                    "than separating from it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e13",
        "band": "easier",
        "text": "A flat wall stands 60 m from where a shout is made. What is "
                "the total distance the sound travels before the echo is "
                "heard?",
        "options": [
            {"text": "60 m", "correct": False,
             "why": "That is only the distance to the wall, the outward "
                    "leg — the sound still has to travel back."},
            {"text": "30 m", "correct": False,
             "why": "That halves the distance to the wall instead of "
                    "doubling it."},
            {"text": "120 m", "correct": True},
            {"text": "240 m", "correct": False,
             "why": "That is four times the distance to the wall; the "
                    "journey has two equal legs, not four."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e14",
        "band": "easier",
        "text": "An echo returns after the sound has covered a total of "
                "500 m. How far away is the reflecting wall?",
        "options": [
            {"text": "500 m", "correct": False,
             "why": "500 m is the whole out-and-back path; the wall is "
                    "halfway along it."},
            {"text": "1000 m", "correct": False,
             "why": "That doubles a total that has already been doubled "
                    "once."},
            {"text": "125 m", "correct": False,
             "why": "That halves the correct answer again; only one "
                    "halving is needed."},
            {"text": "250 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e15",
        "band": "easier",
        "text": "A canyon wall reflects a shout, and the total path the "
                "sound covers, out and back, is 0.6 km. How far away is the "
                "wall, in metres?",
        "options": [
            {"text": "300 m", "correct": True},
            {"text": "600 m", "correct": False,
             "why": "0.6 km converts to 600 m, which is the whole path, "
                    "not the distance to the wall."},
            {"text": "60 m", "correct": False,
             "why": "That divides the total path by ten rather than by "
                    "two."},
            {"text": "1200 m", "correct": False,
             "why": "That doubles the total path instead of halving it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e16",
        "band": "easier",
        "text": "Which of these would give the strongest echo if a shout "
                "were made towards it?",
        "options": [
            {"text": "a pillow, because it sits close to the sound source",
             "correct": False,
             "why": "Distance is not the deciding factor here, and a "
                    "pillow is soft, so it absorbs rather than reflects "
                    "sound."},
            {"text": "a steel shutter, because it is hard, flat and heavy",
             "correct": True},
            {"text": "a pile of dry leaves, because leaves rustle easily "
                     "in wind", "correct": False,
             "why": "Rustling shows the leaves move readily, which is "
                    "exactly why they absorb sound rather than reflecting "
                    "it strongly."},
            {"text": "an open window, because sound passes through any "
                     "opening", "correct": False,
             "why": "An opening lets sound transmit through rather than "
                    "reflecting it back as an echo."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e17",
        "band": "easier",
        "text": "Which of these is built specifically to give almost no "
                "echo at all?",
        "options": [
            {"text": "a sheet of plywood, because wood is a solid "
                     "material", "correct": False,
             "why": "Plywood is fairly hard and reflects a good deal of "
                    "sound rather than absorbing it."},
            {"text": "a pane of glass, because it is smooth", "correct": False,
             "why": "A smooth hard surface like glass reflects sound "
                    "well; smoothness does not make it absorbent."},
            {"text": "a wall of foam wedges, purpose-built to absorb "
                     "sound", "correct": True},
            {"text": "a brick wall, because bricks are heavy building "
                     "blocks", "correct": False,
             "why": "A heavy, hard surface like brick reflects strongly — "
                    "the opposite of what is wanted here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e18",
        "band": "easier",
        "text": "A cyclist rings a bell near a stone bridge and, a moment "
                "later, hears the same ring again, a little fainter. What "
                "is that returning sound called?",
        "options": [
            {"text": "a resonance", "correct": False,
             "why": "Resonance is a different effect, in which an object "
                    "vibrates strongly at its own natural frequency; "
                    "nothing here is being driven to vibrate."},
            {"text": "a vibration", "correct": False,
             "why": "A vibration is what makes the sound in the first "
                    "place, not the reflected sound heard afterwards."},
            {"text": "an oscillation", "correct": False,
             "why": "An oscillation is a general back-and-forth motion; "
                    "the specific reflected, delayed sound has its own "
                    "name."},
            {"text": "an echo", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e19",
        "band": "easier",
        "text": "The time a sound takes to die away inside a room, after "
                "the source has stopped, is called…",
        "options": [
            {"text": "the reverberation time", "correct": True},
            {"text": "the amplitude", "correct": False,
             "why": "Amplitude measures how big a vibration is, not how "
                    "long sound lingers in a room."},
            {"text": "the wavelength", "correct": False,
             "why": "Wavelength is a property of the wave itself, "
                    "unrelated to how long a room's sound persists."},
            {"text": "the frequency", "correct": False,
             "why": "Frequency counts vibrations per second; it says "
                    "nothing about how long sound takes to fade in a "
                    "room."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e20",
        "band": "easier",
        "text": "Architects designing a concert hall for an orchestra "
                "generally aim for a reverberation time of roughly…",
        "options": [
            {"text": "about two minutes", "correct": False,
             "why": "A room where sound lingered for whole minutes would "
                    "be unusable — instruments would blur into one "
                    "continuous noise."},
            {"text": "about two seconds", "correct": True},
            {"text": "about two hundredths of a second", "correct": False,
             "why": "A room that dead would sound lifeless, which "
                    "orchestral halls specifically avoid."},
            {"text": "exactly zero seconds", "correct": False,
             "why": "A room with no reverberation at all would sound "
                    "completely dead, which is not the aim."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e21",
        "band": "easier",
        "text": "For clear speech, such as in a lecture theatre, architects "
                "usually aim for a shorter reverberation time than for "
                "music — roughly…",
        "options": [
            {"text": "about ten seconds", "correct": False,
             "why": "A reverberation time that long would badly blur "
                    "spoken words together."},
            {"text": "about one minute", "correct": False,
             "why": "Far too long for intelligible speech; words would "
                    "run into one another."},
            {"text": "about one second", "correct": True},
            {"text": "about one hundredth of a second", "correct": False,
             "why": "This is closer to a dead recording booth, built for "
                    "a different purpose than a lecture theatre."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e22",
        "band": "easier",
        "text": "When a soft, absorbent material takes in sound, where does "
                "the sound's energy mostly end up?",
        "options": [
            {"text": "a brighter patch of light on the surface",
             "correct": False,
             "why": "Sound energy does not become light; the material "
                    "simply warms very slightly."},
            {"text": "a small electric current inside the material",
             "correct": False,
             "why": "An ordinary absorbing material like foam or curtain "
                    "generates no electric current."},
            {"text": "a new sound at a noticeably lower pitch",
             "correct": False,
             "why": "Absorbed sound is not re-emitted at any pitch; its "
                    "energy is used up as heating."},
            {"text": "a very small amount of heat", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e23",
        "band": "easier",
        "text": "When sound meets a surface and is reflected, what happens "
                "to it?",
        "options": [
            {"text": "it is sent back the way it came", "correct": True},
            {"text": "it carries on through the material and out the "
                     "other side", "correct": False,
             "why": "Carrying on through is what happens to transmitted "
                    "sound, not reflected sound."},
            {"text": "it is turned into a small amount of heating inside "
                     "the material", "correct": False,
             "why": "Turning into heating is what happens to absorbed "
                    "sound; reflected sound is not absorbed."},
            {"text": "it is stopped from existing, the instant it "
                     "arrives", "correct": False,
             "why": "Nothing about reflection destroys the sound — it "
                    "continues on, travelling back the way it came."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e24",
        "band": "easier",
        "text": "A bare rock face reflects sound strongly mainly because it "
                "is…",
        "options": [
            {"text": "soft, thin and light", "correct": False,
             "why": "Soft, light materials absorb sound rather than "
                    "reflecting it strongly."},
            {"text": "hard, flat and heavy", "correct": True},
            {"text": "warm and dry", "correct": False,
             "why": "Temperature and dryness are not what decides how "
                    "much a surface reflects."},
            {"text": "rough and full of small holes", "correct": False,
             "why": "A rough, holed surface, like foam, is built to "
                    "absorb sound rather than send it back."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e25",
        "band": "easier",
        "text": "Which of these, added to a bare classroom wall, would most "
                "reduce echo in the room?",
        "options": [
            {"text": "a sheet of glass fixed flat over the wall",
             "correct": False,
             "why": "Glass is hard and reflects sound well, so it would "
                    "do nothing to reduce echo."},
            {"text": "a fresh layer of gloss paint", "correct": False,
             "why": "A thin layer of paint barely changes how hard or "
                    "soft the wall's surface is to sound."},
            {"text": "a heavy curtain or a thick fabric hanging",
             "correct": True},
            {"text": "a metal noticeboard screwed to the wall",
             "correct": False,
             "why": "Metal is hard and reflects strongly, adding to the "
                    "echo rather than reducing it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e26",
        "band": "easier",
        "text": "A shout reflects off a cliff 220 m away. What is the total "
                "distance the sound travels before the echo returns?",
        "options": [
            {"text": "220 m", "correct": False,
             "why": "That is only the outward leg to the cliff; the sound "
                    "still has to return."},
            {"text": "110 m", "correct": False,
             "why": "That halves the one-way distance instead of doubling "
                    "the round trip."},
            {"text": "880 m", "correct": False,
             "why": "That is four times the distance to the cliff, not "
                    "twice."},
            {"text": "440 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e27",
        "band": "easier",
        "text": "A reflecting cliff is 900 m from where a shout is made. "
                "What is the total distance the sound travels, out and "
                "back?",
        "options": [
            {"text": "1800 m", "correct": True},
            {"text": "900 m", "correct": False,
             "why": "That is only the outward leg; the total path also "
                    "includes the return journey."},
            {"text": "3600 m", "correct": False,
             "why": "That is four times the one-way distance, not twice."},
            {"text": "450 m", "correct": False,
             "why": "That halves the one-way distance instead of doubling "
                    "the round trip."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e28",
        "band": "easier",
        "text": "Why do architects deliberately avoid making every surface "
                "of a concert hall completely hard?",
        "options": [
            {"text": "so that every seat in the hall ends up exactly the "
                     "same distance from the stage as every other seat "
                     "in the room", "correct": False,
             "why": "Seat distances are a matter of the hall's shape and "
                    "size, not of how hard or soft its surfaces are."},
            {"text": "so that the sound dies away over about the right "
                     "time — not instantly and not forever either",
             "correct": True},
            {"text": "so that the building costs as little as possible "
                     "to put up", "correct": False,
             "why": "Cost is not the reason acoustic materials are "
                    "chosen; the aim is how the sound behaves once the "
                    "hall is built."},
            {"text": "so that no reflected sound ever reaches the "
                     "audience", "correct": False,
             "why": "Some reflected sound is wanted — a hall with none at "
                    "all sounds dead, which musicians dislike."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e29",
        "band": "easier",
        "text": "Ancient open-air theatres were often built with hard stone "
                "seating rather than soft materials. Why?",
        "options": [
            {"text": "because stone was simply the only building "
                     "material ever available anywhere at that time",
             "correct": False,
             "why": "Wood, clay and other softer materials were "
                    "certainly available; stone was chosen for how it "
                    "behaves acoustically."},
            {"text": "because stone seating absorbs a performer's voice "
                     "fairly evenly", "correct": False,
             "why": "Stone is hard and reflects sound rather than "
                    "absorbing it, which is exactly why it helps a voice "
                    "carry."},
            {"text": "because hard stone reflects sound out towards the "
                     "audience at the back", "correct": True},
            {"text": "because stone seating keeps the audience cool in "
                     "hot weather", "correct": False,
             "why": "Keeping cool is not why stone was chosen here; the "
                    "reason is how well it reflects sound towards the "
                    "back rows."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-e30",
        "band": "easier",
        "text": "A school library is carpeted and lined with shelves of "
                "books, and sounds made in it barely echo at all. Why?",
        "options": [
            {"text": "the room is far too small for any sound to travel "
                     "across it", "correct": False,
             "why": "Sound crosses a room that size easily; the "
                    "difference is in how much comes back, not whether it "
                    "can travel there."},
            {"text": "the books physically block sound waves from ever "
                     "being made, anywhere near them", "correct": False,
             "why": "Books do not stop sound being made; they absorb "
                    "some of the sound after it exists."},
            {"text": "the carpets reflect sound away from a reader's "
                     "ears on purpose", "correct": False,
             "why": "Carpets absorb sound rather than reflecting it; that "
                    "absorption is exactly why the room is so quiet."},
            {"text": "carpets, soft furniture and shelves of books absorb "
                     "most of the sound made in the room", "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p6-07-s07",
        "band": "standard",
        "text": "A hard wall stands only 3 m away in a narrow corridor, and "
                "a hand clap there gives no separate echo. Why not?",
        "options": [
            {"text": "the sound has been absorbed by the wall's surface "
                     "rather than reflected back towards the listener at "
                     "all", "correct": False,
             "why": "A hard wall reflects strongly rather than absorbing; "
                    "plenty of sound is coming back."},
            {"text": "the returning pulse is not truly a reflection at "
                     "all, and it is in any case far too quiet for a "
                     "person to hear it as anything separate",
             "correct": False,
             "why": "It is an ordinary reflection, and at 3 m it returns "
                    "loudly — the problem is timing, not loudness."},
            {"text": "the surface is directly overhead rather than in "
                     "front", "correct": False,
             "why": "Direction is not stated as the issue here; the "
                    "distance is what matters."},
            {"text": "the reflection arrives too soon after the original "
                     "sound to be heard separately", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s08",
        "band": "standard",
        "text": "A village hall with a bare wooden floor and painted brick walls sounds very echoey when it is empty, but much less so once it is full of people for a meeting. Explain why.",
        "options": [
            {"text": "the people themselves, their clothing and their "
                     "hair, absorb a good deal of the sound the bare "
                     "floor and walls would otherwise send back",
             "correct": True},
            {"text": "a hall packed with people is physically smaller inside, leaving too little distance for a reflection to arrive late enough to be heard separately",
             "correct": False,
             "why": "The hall's walls have not moved, so the distances "
                    "are unchanged; what has changed is how much sound "
                    "comes back off what is now in the way."},
            {"text": "sound travels more slowly through the warmer air "
                     "of a crowded hall, so the reflections never manage "
                     "to reach a listener at all", "correct": False,
             "why": "A warmer hall changes the speed of sound only "
                    "slightly, and the reflections still arrive; what "
                    "changes is how much of the sound survives."},
            {"text": "the quiet talking of a full hall cancels out the "
                     "reflected sound, leaving the room sounding flat "
                     "and dead instead", "correct": False,
             "why": "Extra voices add sound to the hall rather than "
                    "cancelling reflections; the fall in echo comes from "
                    "the people absorbing it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s09",
        "band": "standard",
        "text": "Using a stopwatch, a hiker times the echo from a quarry "
                "face at 0.60 s after clapping once, with sound travelling "
                "at roughly 340 m/s. What distance does that put the "
                "quarry face at?",
        "options": [
            {"text": "204 m", "correct": False,
             "why": "That is the whole path, out and back. The wall is "
                    "halfway along it."},
            {"text": "102 m", "correct": True},
            {"text": "51 m", "correct": False,
             "why": "That halves the correct answer a second time; only "
                    "one halving is needed."},
            {"text": "340 m", "correct": False,
             "why": "That is just the speed of sound; it has not been "
                    "combined with the 0.60 s at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s10",
        "band": "standard",
        "text": "A probe fires a click down a straight mine shaft and the "
                "echo returns 0.80 s later, with sound at about 340 m/s in "
                "air. How long is the shaft?",
        "options": [
            {"text": "272 m", "correct": False,
             "why": "That is the whole path, down and back. The shaft's "
                    "length is half of it."},
            {"text": "68 m", "correct": False,
             "why": "That halves the correct answer a second time."},
            {"text": "136 m", "correct": True},
            {"text": "408 m", "correct": False,
             "why": "That comes from the wrong time altogether — check "
                    "0.80 s, not a different figure."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s11",
        "band": "standard",
        "text": "On a graph of the time before an echo returns, plotted "
                "against the distance to the wall, what shape would the "
                "line take?",
        "options": [
            {"text": "It shows the depth reached by the sound so far",
             "correct": False,
             "why": "The graph plots time against distance to the wall, "
                    "not depth reached — those are different quantities "
                    "here."},
            {"text": "It doubles for every extra 340 m of distance to the "
                     "wall", "correct": False,
             "why": "The relationship is a steady straight-line "
                    "proportion, not a doubling at fixed steps."},
            {"text": "It increases in proportion to the distance to the "
                     "wall", "correct": True},
            {"text": "It stays fixed at one second whatever the "
                     "distance", "correct": False,
             "why": "A fixed time would mean distance made no difference "
                    "at all, which is not how an echo behaves."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s12",
        "band": "standard",
        "text": "A ship's horn sounds once, 255 m from a rocky headland, "
                "with sound moving through the air at roughly 340 m/s. How "
                "many seconds pass before the horn's echo returns?",
        "options": [
            {"text": "3.0 s", "correct": False,
             "why": "That doubles the correct time; the path has been "
                    "doubled once too often."},
            {"text": "6.0 s", "correct": False,
             "why": "That is four times the correct answer, not twice."},
            {"text": "1.5 s", "correct": True},
            {"text": "0.75 s", "correct": False,
             "why": "That halves the correct answer; the total path has "
                    "not been used."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s13",
        "band": "standard",
        "text": "A single loud bang is made 6 m from a hard wall — too "
                "close for a separate echo. What would a listener actually "
                "hear?",
        "options": [
            {"text": "The bang would sound duller and fuller, but still "
                     "like one sound", "correct": True},
            {"text": "A single loud bang would be heard as several "
                     "separate, later bangs", "correct": False,
             "why": "Several separate bangs would need several separate "
                    "reflections arriving late enough to tell apart, not "
                    "one reflection arriving too soon."},
            {"text": "Nothing would change about how the bang sounds",
             "correct": False,
             "why": "The reflection still reaches the ear and combines "
                    "with the original — it just cannot be told apart "
                    "from it."},
            {"text": "The bang would arrive before it was actually made",
             "correct": False,
             "why": "Nothing can arrive before it is made; the reflection "
                    "is simply too close behind the original to separate "
                    "from it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s14",
        "band": "standard",
        "text": "Why is roughly 17 m taken as the shortest distance at "
                "which a hard surface gives a separate echo?",
        "options": [
            {"text": "Because reflections closer than about 17 m arrive "
                     "too soon to separate from the original",
             "correct": True},
            {"text": "Because the ear can only ever hear one sound "
                     "during any one second", "correct": False,
             "why": "The ear can hear many separate sounds within a "
                    "second; the limit here is about two sounds arriving "
                    "close together."},
            {"text": "Because sound gets quieter the further it travels, "
                     "so a near echo is inaudible", "correct": False,
             "why": "A near echo is not too quiet — a hard surface close "
                    "by reflects strongly. The problem is timing, not "
                    "loudness."},
            {"text": "Because it takes longer than a tenth of a second "
                     "for the ear to register any sound",
             "correct": False,
             "why": "The ear registers sound almost instantly; the "
                    "tenth-of-a-second figure is about telling two "
                    "arrivals apart, not about hearing at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s15",
        "band": "standard",
        "text": "Which of these, at the same distance from a shout, is "
                "most likely to give a clear echo?",
        "options": [
            {"text": "A brick garage wall, because it is hard, flat and "
                     "heavy enough to reflect strongly", "correct": True},
            {"text": "A wooden fence, because wood is a natural "
                     "material", "correct": False,
             "why": "A thin, gapped wooden fence is neither especially "
                    "flat nor heavy, so it reflects far less strongly "
                    "than a solid wall."},
            {"text": "A hedge, because plants absorb carbon dioxide as "
                     "well as sound", "correct": False,
             "why": "A hedge's leaves and gaps absorb and scatter sound "
                    "rather than reflecting it strongly."},
            {"text": "A steel girder, because metal always gives the "
                     "loudest possible echo", "correct": False,
             "why": "Metal is a strong reflector, but a solid brick wall "
                    "is just as flat, hard and heavy and reflects "
                    "similarly well."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s16",
        "band": "standard",
        "text": "A long, straight, hard-walled corridor gives a noticeable "
                "echo; a corridor half as long, with the same walls, gives "
                "none. Why?",
        "options": [
            {"text": "Because a longer corridor changes the speed sound "
                     "travels at", "correct": False,
             "why": "Sound travels at the same speed in the same air "
                    "regardless of the corridor's length."},
            {"text": "Because the extra distance gives the reflection "
                     "time enough to separate from the original shout",
             "correct": True},
            {"text": "Because a longer corridor is always narrower, "
                     "which reflects sound more strongly", "correct": False,
             "why": "Width is not stated to change here; it is the "
                    "extra length, and so the extra delay, that matters."},
            {"text": "Because sound needs to travel at least ten metres "
                     "before it can reflect off a surface", "correct": False,
             "why": "Sound reflects off a hard surface at any distance; "
                    "what changes with distance is whether the reflection "
                    "can be heard separately."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s17",
        "band": "standard",
        "text": "A reflecting cliff is 300 m away. Sound travels at about "
                "340 m/s in air. What is the total distance the sound "
                "travels, out and back?",
        "options": [
            {"text": "600 m", "correct": True},
            {"text": "2400 m", "correct": False,
             "why": "That is eight times the one-way distance."},
            {"text": "300 m", "correct": False,
             "why": "That is only the outward leg; the sound still has "
                    "to return."},
            {"text": "1200 m", "correct": False,
             "why": "That is four times the one-way distance, not "
                    "twice."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s18",
        "band": "standard",
        "text": "A padded gym mat store and an empty tiled sports hall are "
                "the same size. Shouting in the tiled hall produces a much "
                "stronger echo. Why?",
        "options": [
            {"text": "Sound is well known to travel a good deal faster "
                     "through a tiled floor than it ever does through "
                     "padded mats", "correct": False,
             "why": "Sound in this room travels through the air, at the "
                    "same speed regardless of what the floor is made of."},
            {"text": "The tile is far more reflective than the padded "
                     "mats, so much more of the sound comes back",
             "correct": True},
            {"text": "The mats make the room feel a good deal smaller "
                     "than it really is, leaving no time at all for any "
                     "reflection to separate into an echo", "correct": False,
             "why": "The two rooms are the same size, so the distance "
                    "available for an echo has not changed — what has "
                    "changed is how much sound comes back."},
            {"text": "The tiled hall is warmer, and warm air reflects "
                     "sound more strongly", "correct": False,
             "why": "Temperature of the air is not what decides how much "
                    "sound a surface reflects."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s19",
        "band": "standard",
        "text": "Why does an echo-timing device need to know which "
                "material — air, water or a particular metal — the sound "
                "is travelling through before it can report a distance?",
        "options": [
            {"text": "Because different materials produce different "
                     "frequencies of echo", "correct": False,
             "why": "Frequency is set by the source, not changed by the "
                    "material the sound is passing through."},
            {"text": "Because the timing has to be converted into a "
                     "distance using the speed of sound in that material, "
                     "and different materials have different speeds",
             "correct": True},
            {"text": "Because the material only ever changes how loud "
                     "the returning echo eventually sounds to a listener, "
                     "and has no bearing whatsoever on how far away the "
                     "reflecting surface actually is", "correct": False,
             "why": "The material's speed of sound is exactly what links "
                    "the measured time to a distance, so it has everything "
                    "to do with the reported distance."},
            {"text": "Because sound cannot enter some materials without "
                     "knowing this", "correct": False,
             "why": "Sound enters ordinary materials whether or not the "
                    "material is known; the issue is turning a time into "
                    "a distance correctly."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s20",
        "band": "standard",
        "text": "A hard playground wall and a hedge stand at the same "
                "distance from a shout. Which is more likely to produce a "
                "noticeable echo, and why?",
        "options": [
            {"text": "The hedge, because plants are well known to "
                     "naturally amplify and strengthen any sound that "
                     "happens to pass through their leaves and branches",
             "correct": False,
             "why": "Leaves and gaps scatter and absorb sound; they do "
                    "not amplify it."},
            {"text": "Both would be equally likely, because the distance "
                     "to a surface is honestly the only thing that ever "
                     "decides whether an echo happens", "correct": False,
             "why": "Distance decides the timing condition, but the "
                    "surface's material decides how much sound comes "
                    "back at all — both matter."},
            {"text": "Neither, because open-air settings never produce "
                     "an echo", "correct": False,
             "why": "An echo needs only a reflecting surface and enough "
                    "distance; open-air settings such as a playground "
                    "wall can and do produce one."},
            {"text": "The playground wall, because a hard flat surface "
                     "reflects far more sound than a hedge's leaves and "
                     "gaps", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s21",
        "band": "standard",
        "text": "A recording engineer claps once in an untreated room and "
                "hears a harsh, ringing effect; after fitting foam panels, "
                "the same clap sounds flat and short. What has changed?",
        "options": [
            {"text": "The foam has made the room physically smaller",
             "correct": False,
             "why": "Foam panels are thin; they do not meaningfully "
                    "shrink the room's dimensions."},
            {"text": "The foam has changed the frequency of the "
                     "handclap", "correct": False,
             "why": "Nothing changes the frequency of the original "
                    "sound; what changes is how much of it survives as a "
                    "reflection."},
            {"text": "The foam has made the clap itself quieter to begin "
                     "with", "correct": False,
             "why": "The clap is made the same way either time; it is "
                    "the reflected sound that has changed, not the "
                    "original."},
            {"text": "Far less of the clap's sound is now being "
                     "reflected back into the room", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s22",
        "band": "standard",
        "text": "Why is a swimming pool hall, with its hard tiled walls "
                "and water surface, one of the echoey-est rooms in a "
                "typical school?",
        "options": [
            {"text": "Water is well known to make sound travel a great "
                     "deal further before it ever properly fades away to "
                     "nothing", "correct": False,
             "why": "It is the hard tiled surfaces, not the water, that "
                    "make the hall so echoey — a pool hall with soft "
                    "acoustic surfaces would be much quieter."},
            {"text": "The chlorine in the air changes how sound "
                     "reflects", "correct": False,
             "why": "Chlorine in the air has no meaningful effect on how "
                    "a surface reflects sound."},
            {"text": "The room is unusually small compared with a normal "
                     "hall", "correct": False,
             "why": "A pool hall is not usually smaller than an ordinary "
                    "hall; the echo comes from what its surfaces are made "
                    "of."},
            {"text": "Almost every surface in it is hard and reflects "
                     "sound strongly, with almost nothing to absorb it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s23",
        "band": "standard",
        "text": "A bell rings near a cliff and its echo is heard 4.0 s "
                "later, with sound at about 340 m/s. How far away is the "
                "cliff?",
        "options": [
            {"text": "1360 m", "correct": False,
             "why": "That is the whole path, out and back. The cliff is "
                    "halfway along it."},
            {"text": "340 m", "correct": False,
             "why": "That is just the speed of sound on its own; it has "
                    "not been combined with the 4.0 s."},
            {"text": "680 m", "correct": True},
            {"text": "2720 m", "correct": False,
             "why": "That is four times the correct distance, not "
                    "twice."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s24",
        "band": "standard",
        "text": "A single shout near two identical rock walls, one twice "
                "as far away as the other, gives two separate echoes "
                "rather than one. Why?",
        "options": [
            {"text": "The nearer wall absorbs almost all of the sound "
                     "completely, while the further wall simply reflects "
                     "the whole of it straight back again", "correct": False,
             "why": "Both walls are the same hard rock, so both reflect "
                    "strongly — the difference between them is distance, "
                    "not material."},
            {"text": "The two walls just happen to be built from two "
                     "entirely different kinds of building material "
                     "altogether, inside and out", "correct": False,
             "why": "The walls are described as identical; only their "
                    "distances differ."},
            {"text": "Sound only reflects off the second wall it "
                     "reaches", "correct": False,
             "why": "Sound reflects off every hard surface it meets, the "
                    "nearer wall included."},
            {"text": "The two reflections arrive at different times, far "
                     "enough apart for the ear to hear them as two "
                     "separate sounds", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s25",
        "band": "standard",
        "text": "A window is opened in a previously echoey room, and the "
                "room's echo becomes noticeably weaker. Why might that be?",
        "options": [
            {"text": "Opening a window of any kind always makes an "
                     "entire room noticeably quieter overall, whatever "
                     "else is going on inside it", "correct": False,
             "why": "A room can stay just as loud once a window is open; "
                    "what has changed here is how much sound reflects "
                    "back, not the overall level."},
            {"text": "Some of the sound that used to reflect off the "
                     "window can now transmit out through the opening "
                     "instead", "correct": True},
            {"text": "The open window absorbs sound the way foam does",
             "correct": False,
             "why": "An opening does not absorb sound; it lets sound "
                    "transmit straight through instead of reflecting."},
            {"text": "Air escaping steadily through the open window is "
                     "what actually slows the returning sound down on its "
                     "way back", "correct": False,
             "why": "The speed of sound in the room's air is unchanged; "
                    "what has changed is how much sound leaves through "
                    "the opening rather than reflecting."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s26",
        "band": "standard",
        "text": "A steel shutter 6 m away gives no separate echo; a thick "
                "hedge 250 m away also gives none. What is different about "
                "the two failures?",
        "options": [
            {"text": "Both fail for exactly the same reason — neither "
                     "surface reflects any sound", "correct": False,
             "why": "The shutter reflects strongly; its problem is "
                    "timing, not a lack of reflection."},
            {"text": "The shutter fails because it absorbs sound; the "
                     "hedge fails because it is too far away",
             "correct": False,
             "why": "The shutter reflects rather than absorbs; and the "
                    "hedge's problem is how little it sends back, not the "
                    "distance."},
            {"text": "Both surfaces would succeed perfectly well if "
                     "their distances from the shout were simply swapped "
                     "around, since distance is what matters here",
             "correct": False,
             "why": "Swapping distances would fix the shutter's timing "
                    "problem, but the hedge would still send back too "
                    "little sound at any distance."},
            {"text": "The shutter fails because it is too close for the "
                     "reflection to separate in time; the hedge fails "
                     "because too little sound comes back at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s27",
        "band": "standard",
        "text": "Two claps are made near a wall 51 m away. How long after "
                "each clap does its echo return, given sound travels at "
                "about 340 m/s?",
        "options": [
            {"text": "0.15 s", "correct": False,
             "why": "That halves the correct answer; the round trip has "
                    "not been used."},
            {"text": "0.60 s", "correct": False,
             "why": "That doubles the correct answer."},
            {"text": "0.30 s", "correct": True},
            {"text": "3.0 s", "correct": False,
             "why": "That is ten times too large — check the decimal "
                    "point."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s28",
        "band": "standard",
        "text": "A hunter's rifle shot echoes off a distant cliff face and "
                "returns 2.4 s later, with sound at about 340 m/s. How far "
                "away is the cliff?",
        "options": [
            {"text": "816 m", "correct": False,
             "why": "That is the whole path, out and back. The cliff is "
                    "halfway along it."},
            {"text": "204 m", "correct": False,
             "why": "That halves the correct answer a second time."},
            {"text": "408 m", "correct": True},
            {"text": "1632 m", "correct": False,
             "why": "That doubles the whole path instead of halving it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s29",
        "band": "standard",
        "text": "A drummer plays a single loud beat in an empty warehouse "
                "with bare brick walls, and clearly hears the beat repeat "
                "two or three times, fading each time. What causes the "
                "fading repeats, rather than just one echo?",
        "options": [
            {"text": "The drum itself keeps making the sound after it is "
                     "hit", "correct": False,
             "why": "A drum beat is brief; the repeats heard afterwards "
                    "are reflections, not the drum sounding again."},
            {"text": "Each repeat is a brand new sound created by the "
                     "walls", "correct": False,
             "why": "The walls make nothing; each repeat is the same "
                    "beat, reflected again."},
            {"text": "The warehouse itself somehow amplifies the beat a "
                     "little more loudly and clearly each and every time "
                     "that it repeats around the room", "correct": False,
             "why": "Each repeat is described as fading, not growing "
                    "louder; nothing adds energy to the sound."},
            {"text": "The beat reflects back and forth between different "
                     "hard walls, each reflection weaker than the last as "
                     "some sound is lost", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-s30",
        "band": "standard",
        "text": "Two identical foam panels are placed the same distance "
                "from a shout, one facing the listener squarely and one "
                "turned to face partly away. Which would give the fainter "
                "returning sound, and why?",
        "options": [
            {"text": "The squarely facing panel, because facing a "
                     "listener directly always absorbs more sound than "
                     "facing away", "correct": False,
             "why": "Facing direction affects where reflected sound "
                    "goes, not how much a panel absorbs — both panels "
                    "absorb the same fraction."},
            {"text": "Neither — both would return exactly the same "
                     "amount of sound to the listener, whichever way "
                     "they face", "correct": False,
             "why": "Angling a surface changes the direction reflected "
                    "sound travels in, so it changes how much reaches a "
                    "particular listener."},
            {"text": "The turned panel, because whatever little it "
                     "reflects is directed away from the listener rather "
                     "than straight back at them", "correct": True},
            {"text": "The squarely facing panel, because facing away "
                     "somehow makes a surface absorb less sound than it "
                     "otherwise would", "correct": False,
             "why": "Absorption depends on the material, not the angle; "
                    "angling the panel changes where the reflected part "
                    "goes, not how much is absorbed."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p6-07-h07",
        "band": "harder",
        "text": "A canyon wall lies 85 m from a point where someone "
                "shouts, and sound moves through the air at roughly "
                "340 m/s. Calculate how many seconds pass before the echo "
                "is heard.",
        "options": [
            {"text": "0.50 s", "correct": True},
            {"text": "1.0 s", "correct": False,
             "why": "That doubles the correct answer; the distance has "
                    "already been doubled to get the total path."},
            {"text": "0.25 s", "correct": False,
             "why": "That halves the correct answer; the total path has "
                    "not yet been divided by the speed."},
            {"text": "170 s", "correct": False,
             "why": "That treats the path in metres as if it were "
                    "already the time in seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h08",
        "band": "harder",
        "text": "Standing 42.5 m from a warehouse's steel shutter, a "
                "worker bangs a metal pipe once. Taking the speed of "
                "sound as about 340 m/s, work out the delay before the "
                "bang's echo returns.",
        "options": [
            {"text": "0.50 s", "correct": False,
             "why": "That is the time for a wall twice as far away; check "
                    "the working for this distance."},
            {"text": "0.25 s", "correct": True},
            {"text": "0.125 s", "correct": False,
             "why": "That halves the correct answer once too often."},
            {"text": "85 s", "correct": False,
             "why": "That treats the path in metres as if it were "
                    "already the time in seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h09",
        "band": "harder",
        "text": "A shout is made exactly between two hard parallel walls. "
                "Rather than one echo, a rapid series of fading echoes is "
                "heard. Explain why.",
        "options": [
            {"text": "Each wall makes its own brand new sound the instant "
                     "the shout reaches it", "correct": False,
             "why": "Neither wall makes any sound of its own; each one "
                    "only reflects what already reaches it."},
            {"text": "The two walls swap the sound between them until it "
                     "is finally absorbed by the floor alone", "correct": False,
             "why": "The walls do not pass sound to each other directly; "
                    "each reflection travels back across the gap and is "
                    "heard by the listener before the next bounce."},
            {"text": "The shout keeps bouncing back and forth between the "
                     "two hard walls, each bounce arriving slightly later "
                     "and a little weaker than the last", "correct": True},
            {"text": "Only the nearer wall ever reflects; the far wall "
                     "simply stops the sound completely", "correct": False,
             "why": "A hard wall reflects sound whichever side of the "
                    "shout it is on; nothing here singles out only one "
                    "wall to stop reflecting entirely."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h10",
        "band": "harder",
        "text": "The same heavy curtain seems to kill the echo made by a "
                "shout almost completely, but does far less to reduce the "
                "boom of a bass drum played in the same room. Explain why.",
        "options": [
            {"text": "The curtain has simply worn thin in the middle "
                     "from years of use", "correct": False,
             "why": "Wear is not stated and would not explain a "
                    "consistent difference between a shout and a bass "
                    "note in particular."},
            {"text": "A bass drum's note is far too loud and too "
                     "powerful for any curtain in an ordinary room to "
                     "have a noticeable effect on it",
             "correct": False,
             "why": "Loudness is not the deciding factor here; a soft "
                    "curtain absorbs some of any sound reaching it, "
                    "whatever its volume."},
            {"text": "Curtains only ever affect how loud a sound seems "
                     "to a listener in the room, and have no effect "
                     "whatsoever on how much of any sound is actually "
                     "reflected back", "correct": False,
             "why": "A curtain's whole effect on an echo is by changing "
                    "how much sound reflects back — that is exactly what "
                    "absorption does."},
            {"text": "How well a material absorbs sound depends on "
                     "frequency, and a curtain that absorbs high notes "
                     "well may do far less to a low, booming note",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h11",
        "band": "harder",
        "text": "A simple echo rule assumes a surface reflects the same "
                "fraction of sound whatever the distance. Explain what "
                "that simple rule leaves out for a very hard mountainside "
                "several kilometres away, and what effect that has.",
        "options": [
            {"text": "Over a much longer distance the sound also spreads "
                     "out and is absorbed by the air itself, so even a "
                     "hard mountainside may send back less than the "
                     "simple rule assumes", "correct": True},
            {"text": "Nothing changes over any distance, because a rule "
                     "this simple is meant to hold exactly true no "
                     "matter how far away the surface is",
             "correct": False,
             "why": "The model itself says it is a simplification; real "
                    "sound loses energy to spreading and to the air over "
                    "long distances, which the model does not include."},
            {"text": "The mountain would have to reflect more than 100% "
                     "of the sound reaching it at that range, returning "
                     "even more energy than the original shout actually "
                     "carried", "correct": False,
             "why": "A surface can reflect at most all of the sound that "
                    "reaches it, never more than it received."},
            {"text": "The speed of sound itself becomes noticeably "
                     "greater over very long distances, which is why a "
                     "distant echo can sometimes seem to arrive sooner "
                     "than expected", "correct": False,
             "why": "The speed of sound in a given air is not changed by "
                    "how far the sound has already travelled."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h12",
        "band": "harder",
        "text": "A designer wants a single hall that suits both spoken "
                "announcements and orchestral concerts equally well. "
                "Explain why this is difficult using a single fixed choice "
                "of surfaces.",
        "options": [
            {"text": "Because a hall can only ever be built for speech "
                     "or for music, never both", "correct": False,
             "why": "Some real halls do serve both purposes reasonably "
                    "well; the difficulty is in the choice of surfaces, "
                    "not an absolute impossibility."},
            {"text": "Because speech is clearest with a short "
                     "reverberation time while music benefits from a "
                     "longer one, and no single fixed mix of hard and "
                     "soft surfaces suits both at once", "correct": True},
            {"text": "Because music and speech both need exactly the "
                     "same reverberation time anyway", "correct": False,
             "why": "The two aims are different: a shorter time suits "
                    "clear speech, a longer one suits richer music."},
            {"text": "Because the size of the audience alone decides how "
                     "clear speech or music will sound in any hall, "
                     "whatever choices are made about which surfaces are "
                     "hard and which are soft", "correct": False,
             "why": "Audience size affects some absorption, but the "
                    "surfaces chosen for the hall are what mainly set its "
                    "reverberation time."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h13",
        "band": "harder",
        "text": "A reflecting wall starts 34 m from a shout and is then "
                "moved to 68 m away, with sound at about 340 m/s both "
                "times. What happens to the time before the echo returns?",
        "options": [
            {"text": "0.2 s", "correct": False,
             "why": "That is the time for the original 34 m distance, "
                    "not the doubled one."},
            {"text": "0.8 s", "correct": False,
             "why": "That is four times the original time; doubling the "
                    "distance doubles the time, it does not quadruple it."},
            {"text": "0.4 s", "correct": True},
            {"text": "0.1 s", "correct": False,
             "why": "That halves the original time instead of doubling "
                    "it — the distance has increased, not decreased."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h14",
        "band": "harder",
        "text": "A bare rock face stands 60 m away and a bank of foam "
                "wedges stands 200 m away from the same shout. Evaluate "
                "which, if either, would give an audible separate echo.",
        "options": [
            {"text": "The foam wedges, because they are a good deal "
                     "further away than the rock face, and distance on its "
                     "own decides whether an echo is heard, whatever the "
                     "surface is made of",
             "correct": False,
             "why": "Distance alone is not enough — the foam sends back "
                    "far too little sound to be heard as an echo, however "
                    "far away it is."},
            {"text": "Both equally, because any hard, flat and heavy "
                     "surface always beats any soft one at giving an "
                     "echo, regardless of how far away either one happens "
                     "to be from the person shouting", "correct": False,
             "why": "The foam is soft, not hard, flat and heavy, so it "
                    "does not behave like the rock at any distance."},
            {"text": "Neither, because 200 m is beyond the range at "
                     "which any echo can ever be heard", "correct": False,
             "why": "200 m is well within range for a good reflector; "
                    "the rock face at 60 m clears both conditions "
                    "comfortably."},
            {"text": "The rock face, because it clears both conditions "
                     "— enough returns, and it is far enough away — "
                     "while the foam fails the amount-returned condition "
                     "however far away it is", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h15",
        "band": "harder",
        "text": "An echo returns after the sound has covered a total of "
                "850 m in 2.5 s. What speed of sound does this measurement "
                "imply, and is it a reasonable value for air?",
        "options": [
            {"text": "About 340 m/s, which is a perfectly reasonable "
                     "value for the speed of sound in air", "correct": True},
            {"text": "About 2125 m/s, which is far too fast to be a real "
                     "measurement of air", "correct": False,
             "why": "That multiplies the distance by the time instead of "
                    "dividing the distance by the time."},
            {"text": "About 3.4 m/s, which is far too slow to be a real "
                     "measurement of air", "correct": False,
             "why": "That misplaces a decimal point; 850 m in 2.5 s is a "
                    "great deal faster than 3.4 m/s."},
            {"text": "About 850 m/s, roughly the speed of sound in a "
                     "light gas rather than air", "correct": False,
             "why": "That uses the distance on its own without dividing "
                    "by the time at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h16",
        "band": "harder",
        "text": "A miniature echo-timing model is tested and the total "
                "path recorded is 8000 cm. What is the distance to the "
                "reflecting surface, in metres?",
        "options": [
            {"text": "80 m", "correct": False,
             "why": "8000 cm converts to 80 m, which is the whole path, "
                    "not the distance to the surface."},
            {"text": "40 m", "correct": True},
            {"text": "20 m", "correct": False,
             "why": "That halves the correct answer a second time."},
            {"text": "800 m", "correct": False,
             "why": "That treats 8000 cm as if it were 800 m; a metre is "
                    "100 cm, not 10 cm."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h17",
        "band": "harder",
        "text": "A recording engineer wants an entirely echo-free vocal "
                "booth, with no returning sound whatsoever. Evaluate "
                "whether this is achievable.",
        "options": [
            {"text": "Yes — properly designed foam wedges absorb "
                     "precisely 100% of every sound that reaches them, "
                     "which is why professional booths are described as "
                     "completely echo-free", "correct": False,
             "why": "Even foam wedges typically send back a small "
                    "fraction, around 3%, of the sound reaching them — "
                    "not none at all."},
            {"text": "Yes — echo can always be eliminated completely by "
                     "adding enough foam", "correct": False,
             "why": "Adding more foam reduces the returning fraction "
                    "further but does not take it all the way to zero."},
            {"text": "No — some sound always returns from any real "
                     "surface, even one built to absorb, so a completely "
                     "echo-free booth is not achievable, only a very "
                     "quiet one", "correct": True},
            {"text": "No — but only because microphones always add some "
                     "echo of their own", "correct": False,
             "why": "A microphone does not add an echo; the returning "
                    "sound comes from the room's own surfaces, foam "
                    "included."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h18",
        "band": "harder",
        "text": "A 15 m school corridor, with hard walls at both ends, "
                "occasionally seems to produce a very faint, barely "
                "separate echo — right at the edge of what the roughly "
                "17 m rule would predict. Evaluate this observation.",
        "options": [
            {"text": "A 15 m corridor could never possibly produce any "
                     "separate echo at all", "correct": False,
             "why": "The 17 m figure is only a rough threshold, so "
                    "results right around that distance can vary rather "
                    "than switching sharply at an exact point."},
            {"text": "A 15 m corridor is certain to produce a loud, "
                     "completely unmistakable echo every single time "
                     "somebody claps or shouts anywhere inside it, "
                     "whatever it is used for", "correct": False,
             "why": "15 m is slightly under the rough threshold, so a "
                    "loud, certain echo every time is not what the "
                    "approximate rule would predict."},
            {"text": "The 17 m threshold applies only to shouting and "
                     "not to any other sound", "correct": False,
             "why": "The threshold comes from how the ear separates two "
                    "arrivals in time, which applies to claps and other "
                    "sounds just as much as shouting."},
            {"text": "The 17 m figure is only a rough threshold, so "
                     "right around that distance results vary and a "
                     "faint separate echo may sometimes just be "
                     "noticeable", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h19",
        "band": "harder",
        "text": "One reflection returns 0.11 s after the original sound, "
                "and another returns 0.5 s after it. Compare how each "
                "would actually sound to a listener.",
        "options": [
            {"text": "The 0.11 s case would sound like a faint, only "
                     "just separate echo, while the 0.5 s case would "
                     "sound clearly like two distinct sounds",
             "correct": True},
            {"text": "Both would sound exactly like one single, slightly "
                     "fuller sound", "correct": False,
             "why": "0.5 s is well past the roughly 0.1 s point at which "
                    "the ear starts to hear two sounds separately."},
            {"text": "Both would sound like two completely distinct, "
                     "equally clear sounds", "correct": False,
             "why": "0.11 s is right at the edge of the threshold, so "
                    "that case would sound only faintly separate, not as "
                    "clearly distinct as the 0.5 s case."},
            {"text": "The 0.11 s case would sound clearer than the 0.5 s "
                     "case, not less clear", "correct": False,
             "why": "A longer delay gives the ear more time to tell the "
                    "two sounds apart, so the 0.5 s case is the clearer "
                    "one, not the 0.11 s case."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h20",
        "band": "harder",
        "text": "A student measures a wall as 100 m away and times an "
                "echo returning 0.50 s later. Using the total path and the "
                "time, evaluate what speed of sound this would imply, and "
                "whether the measurement seems trustworthy.",
        "options": [
            {"text": "About 400 m/s, which matches the accepted, "
                     "commonly quoted speed of sound in air just as "
                     "closely as any textbook figure would, so no error "
                     "need be suspected here", "correct": False,
             "why": "400 m/s is noticeably higher than the accepted "
                    "figure of about 340 m/s for air, so it does not "
                    "match a textbook value closely."},
            {"text": "About 400 m/s, which is higher than the real speed "
                     "of sound in air — suggesting an error somewhere in "
                     "the measurement rather than a true reading",
             "correct": True},
            {"text": "About 200 m/s, which is a perfectly normal value "
                     "for air", "correct": False,
             "why": "200 m/s is well below the accepted figure for air "
                    "and does not match the working from the given "
                    "numbers either."},
            {"text": "The implied speed cannot be worked out from this "
                     "information", "correct": False,
             "why": "The distance and the time given are exactly what is "
                    "needed to work out an implied speed for the total "
                    "path."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h21",
        "band": "harder",
        "text": "An architect makes the alcove behind a concert-hall "
                "stage noticeably deeper than before. Predict, with "
                "reasoning, whether this is likely to make speech from "
                "the stage clearer or less clear for the audience, "
                "everything else the same.",
        "options": [
            {"text": "Clearer, because making a stage alcove noticeably "
                     "deeper always increases how loud a speaker's voice "
                     "ends up sounding by the time it reaches the back "
                     "of the hall", "correct": False,
             "why": "A deeper alcove does not reliably make a voice "
                    "louder by the time it reaches the back; what changes "
                    "is how late the alcove's own reflection arrives."},
            {"text": "Unaffected, because the exact depth chosen for an "
                     "alcove behind the stage has no effect whatsoever "
                     "on any of the sound reflected from its surfaces, "
                     "however far back it is built", "correct": False,
             "why": "Depth changes the distance the sound travels to "
                    "the back of the alcove and back, which changes how "
                    "late that reflection arrives."},
            {"text": "Less clear, because sound reflecting off the back "
                     "of a deeper alcove takes noticeably longer to "
                     "return and can arrive late enough to blur with the "
                     "original speech", "correct": True},
            {"text": "Clearer, because reflections arriving from further "
                     "away are always heard as sharper and more distinct "
                     "than the original sound that produced them in the "
                     "first place", "correct": False,
             "why": "A later-arriving reflection tends to blur with "
                    "speech rather than sharpen it, once the delay grows "
                    "large enough."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h22",
        "band": "harder",
        "text": "A probe fires a click down a straight mine shaft "
                "recorded as 0.204 km deep, with sound at about 340 m/s. "
                "How long after the click does the echo return?",
        "options": [
            {"text": "0.6 s", "correct": False,
             "why": "That is the time for the 204 m one-way trip alone, "
                    "not the full there-and-back path of 408 m."},
            {"text": "2.4 s", "correct": False,
             "why": "That is far too long for a path of only about "
                    "408 m at 340 m/s."},
            {"text": "0.3 s", "correct": False,
             "why": "That halves the one-way time as well; the echo has "
                    "the whole 408 m path to cover, not a quarter of it."},
            {"text": "1.2 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h23",
        "band": "harder",
        "text": "An echo returns 0.60 s after a click, with sound at about "
                "340 m/s. What is the distance to the reflecting surface, "
                "in kilometres?",
        "options": [
            {"text": "0.102 km", "correct": True},
            {"text": "0.204 km", "correct": False,
             "why": "That is the whole path in kilometres, out and back "
                    "— the distance to the surface is half of it."},
            {"text": "0.051 km", "correct": False,
             "why": "That halves the correct answer a second time."},
            {"text": "1.02 km", "correct": False,
             "why": "That is ten times too large — check the conversion "
                    "from metres to kilometres."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h24",
        "band": "harder",
        "text": "A flat surface is angled to face partly away from a "
                "listener, while staying the same distance from them. "
                "Predict what happens to the echo they hear.",
        "options": [
            {"text": "The echo would return exactly as loud as it did "
                     "before the surface was angled away, since only the "
                     "distance between the listener and a surface ever "
                     "affects how loud any returning echo can possibly "
                     "be", "correct": False,
             "why": "Direction matters too: reflected sound leaves a "
                    "surface at a matching angle, so much of it can miss "
                    "the listener once the surface is turned away."},
            {"text": "Much of the reflected sound would be directed off "
                     "to one side rather than straight back, so the "
                     "returning echo would be fainter even though the "
                     "distance is unchanged", "correct": True},
            {"text": "The echo would arrive back noticeably sooner than "
                     "before, since turning a surface to face even "
                     "slightly away somehow shortens the total path the "
                     "sound has to travel there and back again",
             "correct": False,
             "why": "The distance to the surface has not changed, so the "
                    "total path length, and therefore the timing, stays "
                    "the same."},
            {"text": "No sound could reflect back once the surface is "
                     "angled away", "correct": False,
             "why": "Some sound still reflects towards the listener even "
                    "at an angle; only the amount reaching them changes, "
                    "not whether any does at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h25",
        "band": "harder",
        "text": "A quiet handclap and a much louder shout are both made "
                "the same distance from a hard wall. Compare how the "
                "fraction of each sound that reflects back compares.",
        "options": [
            {"text": "A louder shout always has a considerably larger "
                     "fraction of its sound reflected straight back off "
                     "a hard surface than a quiet one could ever hope to "
                     "manage under the same conditions", "correct": False,
             "why": "The fraction reflected depends on the surface, not "
                    "on how loud the original sound was."},
            {"text": "A louder shout is reflected noticeably less well "
                     "than a much quieter one, because unusually loud "
                     "sound is absorbed a good deal more easily by any "
                     "ordinary surface it happens to meet", "correct": False,
             "why": "Ordinary surfaces do not absorb loud sound more "
                    "easily than quiet sound; the fraction reflected "
                    "stays about the same either way."},
            {"text": "The fraction of the shout that returns stays "
                     "about the same whatever the loudness, so a louder "
                     "shout gives a louder echo but proportionally no "
                     "more of it comes back", "correct": True},
            {"text": "Loudness makes no real difference to an echo in "
                     "either direction, and changing how loudly someone "
                     "shouts should make no noticeable difference to "
                     "what returns", "correct": False,
             "why": "Loudness does make a difference to how loud the "
                    "echo itself sounds — a louder original sound gives "
                    "a louder echo, even though the reflected fraction "
                    "is unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h26",
        "band": "harder",
        "text": "A device records the total echo path as 152000 mm. What "
                "is the distance to the reflecting surface, in metres?",
        "options": [
            {"text": "152 m", "correct": False,
             "why": "152000 mm converts to 152 m, which is the whole "
                    "path, not the distance to the surface."},
            {"text": "38 m", "correct": False,
             "why": "That halves the correct answer a second time."},
            {"text": "7600 m", "correct": False,
             "why": "That treats 152000 mm as if a metre were only "
                    "20 mm; a metre is 1000 mm."},
            {"text": "76 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h27",
        "band": "harder",
        "text": "A very loud firework explodes 200 m from a hillside, and "
                "later a much quieter handclap is made 200 m from the "
                "same hillside. Compare how long each takes to produce an "
                "echo.",
        "options": [
            {"text": "The two would take exactly the same time, because "
                     "the distance and the speed of sound are the same "
                     "for both; only how easily each is heard differs",
             "correct": True},
            {"text": "The firework's echo would return sooner, because a "
                     "louder sound always travels faster", "correct": False,
             "why": "Sound in the same air travels at the same speed "
                    "whatever its loudness; loudness does not affect "
                    "speed."},
            {"text": "The handclap's echo would return sooner, because "
                     "quieter sounds always travel faster", "correct": False,
             "why": "Sound in the same air travels at the same speed "
                    "whatever its loudness; loudness does not affect "
                    "speed."},
            {"text": "Neither would ever produce a measurable echo, "
                     "because both events are too brief", "correct": False,
             "why": "Both a firework and a handclap are brief sounds "
                    "that reflect and can be timed just as any other "
                    "sound can."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h28",
        "band": "harder",
        "text": "A reflecting cliff is recorded as 0.075 km from a shout. "
                "What is the total distance the sound travels, out and "
                "back, in metres?",
        "options": [
            {"text": "75 m", "correct": False,
             "why": "That is only the one-way distance to the cliff, "
                    "converted from 0.075 km; the sound still has to "
                    "return."},
            {"text": "150 m", "correct": True},
            {"text": "300 m", "correct": False,
             "why": "That doubles the correct total path once too "
                    "often."},
            {"text": "37.5 m", "correct": False,
             "why": "That halves the one-way distance instead of "
                    "doubling the round trip."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h29",
        "band": "harder",
        "text": "A gorge produces such a strong effect that a single "
                "shout is heard reflecting back and forth many times, "
                "each time fainter, before fading to silence. Explain, in "
                "terms of reflection and absorption together, why the "
                "echoes eventually stop being heard at all.",
        "options": [
            {"text": "Each bounce off the gorge walls is reflected "
                     "essentially perfectly, with nothing lost along the "
                     "way, so in theory the very same echoes should "
                     "carry on repeating for an extremely long time",
             "correct": False,
             "why": "The echoes are described as getting fainter each "
                    "time, which shows some sound is lost to absorption "
                    "at every bounce, not none at all."},
            {"text": "The gorge simply runs out of sound to reflect "
                     "after some fixed, countable number of bounces, in "
                     "much the same way a battery eventually runs out of "
                     "stored charge after enough use", "correct": False,
             "why": "There is no fixed store of sound being used up; "
                    "each bounce simply carries a smaller fraction of the "
                    "energy than the one before."},
            {"text": "Each bounce loses some of its sound to absorption, "
                     "so the returning fraction gets smaller every time "
                     "until it eventually falls below what the ear can "
                     "pick out from silence", "correct": True},
            {"text": "The listener's own ear simply stops responding for "
                     "a short while after hearing several loud echoes "
                     "arrive one after another in quick succession",
             "correct": False,
             "why": "The ear keeps working throughout; what changes is "
                    "how much sound is actually arriving, not the ear's "
                    "ability to detect it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-07-h30",
        "band": "harder",
        "text": "An echo sounder gives a noticeably longer delay when "
                "tested against a soft muddy lake bed than against a hard "
                "rocky one at the exact same true depth, using the same "
                "speed of sound in the water both times. Evaluate what "
                "this suggests.",
        "options": [
            {"text": "The soft mud lining the lake bed must be slowing "
                     "the speed of sound down noticeably as the pulse "
                     "passes close to it, which would neatly explain why "
                     "the timing comes out differently", "correct": False,
             "why": "The speed of sound is set by the water the pulse "
                    "travels through, not by what the bed at the far end "
                    "happens to be made of."},
            {"text": "The hard rock lining the other lake bed must "
                     "instead be speeding the returning pulse up as it "
                     "gets close, which would also explain why the "
                     "timing comes out differently between the two beds",
             "correct": False,
             "why": "The bed material affects how much of the pulse "
                    "reflects, not the speed the pulse travels at "
                    "through the water."},
            {"text": "A softer lake bed always means a shorter, "
                     "quicker-arriving echo", "correct": False,
             "why": "At the same depth and the same water speed, the "
                    "timing should not depend on how soft or hard the "
                    "bed is."},
            {"text": "The timing ought to be the same either way, since "
                     "both the depth and the speed of sound in water are "
                     "unchanged; mud and rock differ in how much comes "
                     "back, not in how long the journey takes",
             "correct": True},
        ],
        "figure": None,
    },
]

