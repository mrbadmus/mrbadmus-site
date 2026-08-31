"""P6 lesson 08 — Hearing and auditory range: twelve questions (MRB-223).

Written against Design's page. The dog whistle, the seven listeners and
the decade chart are hers.

The discriminations, in the order the lesson builds them:

  · a range has a BOTTOM as well as a top;
  · infrasound and ultrasound are statements about OUR ears (`WAVE-30`);
  · inaudible is about the listener, not about the sound (`WAVE-29`);
  · animals are not simply better — their ranges sit elsewhere, and the
    top of ours falls with age (`WAVE-32`, `WAVE-31`) — the harder band
    sits here.

⚠️ POSITION IS AUTHORED — 3,2,1,0 · 1,0,2,3 · 0,1,3,2, three of each.

⚠️ The ladder's own two marked rungs are NOT restated; in particular the
30 000 Hz three-listener question and the dog-whistle statement question
do not appear again here.
"""

UNIT = "P6"
LESSON = "hearing-and-auditory-range"
LESSON_NUMBER = 8

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p6-08-e01",
        "band": "easier",
        "text": "The auditory range of a healthy young human is about…",
        "options": [
            {"text": "0 Hz to 1000 Hz", "correct": False,
             "why": "The top of the human range is far higher than 1000 Hz — "
                    "most music lives above it."},
            {"text": "20 Hz to 2000 Hz", "correct": False,
             "why": "The bottom is right and the top is ten times too low."},
            {"text": "200 Hz to 20 000 Hz", "correct": False,
             "why": "The top is right and the bottom is ten times too high; "
                    "people hear well below 200 Hz."},
            {"text": "20 Hz to 20 000 Hz", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e02",
        "band": "easier",
        "text": "Sound above the top of the human range is called…",
        "options": [
            {"text": "infrasound", "correct": False,
             "why": "Infrasound is below the bottom of the range, not above "
                    "the top."},
            {"text": "supersound", "correct": False,
             "why": "Not a term used in physics."},
            {"text": "ultrasound", "correct": True},
            {"text": "silence", "correct": False,
             "why": "It is a real sound and a microphone records it. Only "
                    "our ears are missing out."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e03",
        "band": "easier",
        "text": "An elephant can hear down to about 16 Hz. That sound is…",
        "options": [
            {"text": "ordinary audible sound for a person to hear too",
             "correct": False,
             "why": "16 Hz is below about 20 Hz, so it is under the bottom of "
                    "the human range."},
            {"text": "infrasound, as far as human ears are concerned",
             "correct": True},
            {"text": "ultrasound, well above the top of the human range",
             "correct": False,
             "why": "Ultrasound is above the top of our range. 16 Hz is at "
                    "the other end entirely."},
            {"text": "not sound at all, just a vibration too low to count",
             "correct": False,
             "why": "It is an ordinary pressure wave in air, made and "
                    "carried in exactly the same way."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e04",
        "band": "easier",
        "text": "As people get older, the usual change to their auditory "
                "range is that…",
        "options": [
            {"text": "the top of it comes down", "correct": True},
            {"text": "the bottom of it rises a long way", "correct": False,
             "why": "The bottom hardly moves. It is the top that is lost."},
            {"text": "the whole range shifts upwards", "correct": False,
             "why": "Nothing shifts. The band gets narrower at the top."},
            {"text": "it stays the same and everything just gets quieter",
             "correct": False,
             "why": "Frequencies above the new top are gone altogether, "
                    "however loud they are made."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p6-08-s01",
        "band": "standard",
        "text": "Why are auditory ranges usually drawn on an axis where each "
                "mark is ten times the one before?",
        "options": [
            {"text": "Because a straight scale is harder for a reader to "
                     "take in at a glance, and a stepped one is always the "
                     "easier of the two to read off", "correct": False,
             "why": "A straight scale is easy to read. The trouble is what "
                    "it would show."},
            {"text": "Because the numbers run from a few hertz to over a "
                     "hundred thousand, and on a straight scale every band "
                     "would pile into one end", "correct": True},
            {"text": "Because frequency can only be measured in powers of "
                     "ten, so those are the only marks that could honestly "
                     "be put along the axis at all", "correct": False,
             "why": "Frequency can be any value at all — 440 Hz, for "
                    "instance."},
            {"text": "Because the ear can only hear frequencies that are "
                     "powers of ten, and the marks along the axis are "
                     "exactly where hearing actually happens", "correct": False,
             "why": "The ear responds across the whole band continuously."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s02",
        "band": "standard",
        "text": "A cat's range runs to about 64 000 Hz and a mouse does most "
                "of its calling near 60 000 Hz. What does that suggest?",
        "options": [
            {"text": "That a cat can hear mice talking to each other",
             "correct": True},
            {"text": "That mice can hear cats coming", "correct": False,
             "why": "That may be true, but it is not what the two numbers "
                    "given here line up to show."},
            {"text": "That mice and cats use the same calls", "correct": False,
             "why": "The mouse is calling and the cat is listening. Nothing "
                    "says the cat calls at that frequency."},
            {"text": "That both are using ultrasound to see in the dark",
             "correct": False,
             "why": "Neither echolocates. They are simply hearing and "
                    "calling."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s03",
        "band": "standard",
        "text": "A tone at 15 Hz is played very loudly to a person and a "
                "dog. Who hears it?",
        "options": [
            {"text": "Both, because it is loud", "correct": False,
             "why": "Loudness cannot rescue a frequency outside a range. 15 "
                    "Hz is below both bottoms."},
            {"text": "The dog only, because dogs hear better", "correct": False,
             "why": "The dog's range starts at about 67 Hz — higher than "
                    "ours, not lower."},
            {"text": "Neither — 15 Hz is below the bottom of both ranges",
             "correct": True},
            {"text": "The person only, because human ears reach lower than a "
                     "dog's", "correct": False,
             "why": "Human ears do reach lower than a dog's, but not as low "
                    "as 15 Hz."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s04",
        "band": "standard",
        "text": "Which statement about ultrasound is correct?",
        "options": [
            {"text": "It travels faster than audible sound in the same "
                     "material, which is why an echo from it comes back "
                     "sooner", "correct": False,
             "why": "Every frequency travels at the same speed in the same "
                    "material."},
            {"text": "It cannot be reflected or absorbed", "correct": False,
             "why": "It reflects and is absorbed by exactly the same rules, "
                    "which is what makes scanning possible."},
            {"text": "It does not need a material to travel through",
             "correct": False,
             "why": "It needs a medium like any other sound, which is why a "
                    "scanner needs gel."},
            {"text": "It is ordinary sound whose frequency happens to be "
                     "above the top of the human range", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p6-08-h01",
        "band": "harder",
        "text": "A bat's range starts at about 2000 Hz — far higher than "
                "ours — and reaches about 110 000 Hz. What does giving up "
                "the bottom of the range cost a bat, and why is it worth it?",
        "options": [
            {"text": "It loses low sounds it has little use for, and gains "
                     "the very short wavelengths that reflect off insects",
             "correct": True},
            {"text": "It loses nothing, because 2000 Hz is the lowest sound "
                     "there is", "correct": False,
             "why": "Sounds far below 2000 Hz exist everywhere — an "
                    "elephant's rumble at 16 Hz, for one."},
            {"text": "It loses the ability to hear other bats, which is why "
                     "bats hunt alone and never call to one another", "correct": False,
             "why": "Bat calls are high, well inside the bat's own range, "
                    "and bats are often highly social."},
            {"text": "It gains loudness, because a narrower range "
                     "concentrates the hearing", "correct": False,
             "why": "A range says which frequencies an ear responds to, not "
                    "how loud they seem."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h02",
        "band": "harder",
        "text": "Someone with age-related hearing loss says speech sounds "
                "mumbled rather than quiet, and shouting does not help. Why?",
        "options": [
            {"text": "Because shouting lowers the pitch of a voice, making "
                     "it harder still", "correct": False,
             "why": "Shouting raises the volume; it does not systematically "
                    "lower the pitch enough to matter here."},
            {"text": "Because the frequencies that separate consonants sit "
                     "high, and those are the ones that have gone — turning "
                     "up what is left does not restore them", "correct": True},
            {"text": "Because loud sound is absorbed more strongly by a "
                     "damaged ear", "correct": False,
             "why": "The loss is a missing band, not extra absorption of "
                    "loud sound."},
            {"text": "Because mumbling is a habit of the speaker rather "
                     "than anything about the listener, and speaking more "
                     "clearly would fix it whoever was in the room", "correct": False,
             "why": "The same speaker is perfectly clear to someone else in "
                    "the room, so the difference is in the listening."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h03",
        "band": "harder",
        "text": "On a chart where each mark is ten times the one before, a "
                "bat's bar reaches roughly one mark further right than a "
                "dog's. What does that gap mean?",
        "options": [
            {"text": "The bat hears about ten hertz higher than the dog",
             "correct": False,
             "why": "On a multiplying scale a step is a factor, not an "
                    "addition."},
            {"text": "The bat hears about ten times louder than the dog",
             "correct": False,
             "why": "The axis is frequency, and says nothing about loudness."},
            {"text": "The bat hears ten times as many different frequencies",
             "correct": False,
             "why": "Both hear a continuous band. The chart compares where "
                    "the tops of the bands are."},
            {"text": "The bat's top frequency is roughly ten times the "
                     "dog's", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h04",
        "band": "harder",
        "text": "Why is it misleading to say simply that animals hear better "
                "than people?",
        "options": [
            {"text": "Because animals actually hear a good deal worse than "
                     "people do, and the ranges shown on the chart have "
                     "been exaggerated", "correct": False,
             "why": "The ranges are real. Reversing the claim keeps the same "
                    "one-dimensional thinking."},
            {"text": "Because a range only says what an ear responds to at "
                     "all, and it says nothing whatever about how well it "
                     "does any of it",
             "correct": False,
             "why": "True, and worth saying — but it is not the main thing "
                    "wrong with the sentence, which is about direction."},
            {"text": "Because ranges sit in different places rather than "
                     "being simply wider: an elephant reaches lower than us "
                     "and stops lower too", "correct": True},
            {"text": "Because only mammals have auditory ranges at all, "
                     "and the chart leaves out every other kind of animal "
                     "there is", "correct": False,
             "why": "Birds, fish and insects all detect sound, and many have "
                    "measured ranges."},
        ],
        "figure": None,
    },
]
