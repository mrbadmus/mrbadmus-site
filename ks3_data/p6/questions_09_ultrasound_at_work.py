"""P6 lesson 09 — Ultrasound at work: twelve questions (MRB-223).

Written against Design's page. The hidden weld, the three blocks and the
four-panel energy/information split are hers.

The discriminations, in the order the lesson builds them:

  · ultrasound obeys every ordinary rule of sound (`WAVE-33`);
  · the depth is HALF the path, and the speed belongs to the material;
  · a probe sends AND listens with the same face (`WAVE-34`);
  · the gel is there to remove the air, not to lubricate (`WAVE-36`), and
    the useful property is wavelength, not speed (`WAVE-35`) — the harder
    band sits here.

⚠️ POSITION IS AUTHORED — 1,2,3,0 · 2,1,0,3 · 3,0,1,2, three of each.

⚠️ The ladder's own two marked rungs are NOT restated: the 0.060 ms steel
calculation and the travels-through-solids statement do not appear again.
"""

UNIT = "P6"
LESSON = "ultrasound-at-work"
LESSON_NUMBER = 9

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p6-09-e01",
        "band": "easier",
        "text": "Ultrasound is sound with a frequency above about…",
        "options": [
            {"text": "20 Hz", "correct": False,
             "why": "20 Hz is the BOTTOM of the human range. Below it is "
                    "infrasound."},
            {"text": "20 000 Hz", "correct": True},
            {"text": "2000 Hz", "correct": False,
             "why": "2000 Hz is comfortably inside the human range — most "
                    "speech lives around there."},
            {"text": "200 000 Hz", "correct": False,
             "why": "Sound becomes ultrasound long before that. Even a dog "
                    "whistle at 30 000 Hz is already ultrasound to us."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e02",
        "band": "easier",
        "text": "Which of these uses ultrasound for the ENERGY it carries?",
        "options": [
            {"text": "a medical scan", "correct": False,
             "why": "A scan wants information back and deliberately uses as "
                    "little power as it can."},
            {"text": "a microphone", "correct": False,
             "why": "A microphone works at ordinary audible frequencies, and "
                    "it collects information."},
            {"text": "an ultrasonic cleaning bath", "correct": True},
            {"text": "an echo sounder on a ship", "correct": False,
             "why": "An echo sounder times what returns, so it is an "
                    "information use."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e03",
        "band": "easier",
        "text": "A pulse of ultrasound is sent into a block and reflects off "
                "something 40 mm down. What total distance does it travel "
                "before it gets back?",
        "options": [
            {"text": "20 mm", "correct": False,
             "why": "That halves when it should double. The 40 mm is already "
                    "the one-way depth."},
            {"text": "40 mm", "correct": False,
             "why": "That is only the trip down. The pulse has to come back "
                    "too."},
            {"text": "160 mm", "correct": False,
             "why": "That is four times the depth. The journey has two legs, "
                    "not four."},
            {"text": "80 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e04",
        "band": "easier",
        "text": "A gauge is used on an aluminium block but is still set up "
                "for steel. What goes wrong?",
        "options": [
            {"text": "Nothing — the timing is all that matters",
             "correct": False,
             "why": "The timing has to be turned into a depth, and the speed "
                    "of the material does that."},
            {"text": "It reports every depth as too shallow", "correct": False,
             "why": "Aluminium is FASTER than steel, so the pulse covers "
                    "more than the gauge assumes — the error runs the other "
                    "way."},
            {"text": "It reports every depth as too deep", "correct": True},
            {"text": "It refuses to give a reading at all", "correct": False,
             "why": "It gives a perfectly confident reading, which is what "
                    "makes the error easy to miss."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p6-09-s01",
        "band": "standard",
        "text": "The same reflector sits 60 mm down in water (about 1500 "
                "m/s) and in steel (about 5000 m/s). Where do the two pips "
                "on the screen sit closest together?",
        "options": [
            {"text": "In steel, because sound travels more than three times "
                     "faster there, so the echo is back much sooner",
             "correct": True},
            {"text": "In water, because the pulse has less material to get "
                     "through", "correct": False,
             "why": "The depth is the same in both. What differs is how fast "
                    "the pulse gets there and back."},
            {"text": "The same in both, because it is the same reflector at "
                     "the same depth and the screen shows depth rather than "
                     "time", "correct": False,
             "why": "The screen shows TIME, and the same distance takes very "
                    "different times in the two materials."},
            {"text": "In water, because water reflects more of the pulse",
             "correct": False,
             "why": "How much comes back changes the height of the pip, not "
                    "when it arrives."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s02",
        "band": "standard",
        "text": "Why does an ultrasound scan need a high frequency rather "
                "than an audible one?",
        "options": [
            {"text": "Because high frequencies travel faster and return "
                     "sooner", "correct": False,
             "why": "Every frequency travels at the same speed in the same "
                    "material."},
            {"text": "Because a high frequency has a very short wavelength, "
                     "and a short wavelength reflects off small features",
             "correct": True},
            {"text": "Because low frequencies cannot get into the body at "
                     "all, so only ultrasound is able to cross the skin", "correct": False,
             "why": "Low frequencies enter perfectly well. They simply sail "
                    "past small structures without noticing them."},
            {"text": "Because high frequencies are louder", "correct": False,
             "why": "Loudness is amplitude and has nothing to do with "
                    "frequency."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s03",
        "band": "standard",
        "text": "A probe on a water tank sends a pulse and the echo returns "
                "0.20 ms later. Sound travels at about 1500 m/s in water. "
                "How deep is the reflector?",
        "options": [
            {"text": "About 150 mm", "correct": True},
            {"text": "About 300 mm", "correct": False,
             "why": "That is the whole path, down and back. The reflector is "
                    "halfway along it."},
            {"text": "About 75 mm", "correct": False,
             "why": "That halves twice. Halve once only."},
            {"text": "About 7500 mm", "correct": False,
             "why": "The time is 0.20 thousandths of a second, not 0.20 "
                    "seconds. Check the milliseconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s04",
        "band": "standard",
        "text": "What do a medical scanner and a microphone have in common?",
        "options": [
            {"text": "Both deliver energy into whatever they are pointed "
                     "at, and both are run at as much power as they can "
                     "manage",
             "correct": False,
             "why": "Both are information devices, and both work at as low a "
                    "power as they can."},
            {"text": "Both work above 20 000 Hz", "correct": False,
             "why": "A microphone works at ordinary audible frequencies, "
                    "roughly 20 to 20 000 Hz."},
            {"text": "Both need a gel to work", "correct": False,
             "why": "A microphone needs no gel; it takes sound straight out "
                    "of the air."},
            {"text": "Both take information out of a sound wave and turn it "
                     "into an electrical signal", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p6-09-h01",
        "band": "harder",
        "text": "Why is the gel between the probe and the skin essential "
                "rather than merely comfortable?",
        "options": [
            {"text": "Because it lets the probe slide about more easily",
             "correct": False,
             "why": "It does help with that, but a dry probe pressed still "
                    "against the skin would still give no picture."},
            {"text": "Because it warms the skin so the tissue passes sound "
                     "more readily, and warm tissue carries a pulse further "
                     "than cold tissue does", "correct": False,
             "why": "The gel is usually cold, and a degree or two would make "
                    "no difference anyway."},
            {"text": "Because it is what makes the ultrasound audible to the "
                     "machine", "correct": False,
             "why": "The machine listens electronically and does not need "
                    "anything made audible."},
            {"text": "Because a thin layer of air would reflect almost the "
                     "whole pulse straight back off the surface, so hardly "
                     "any would get in", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h02",
        "band": "harder",
        "text": "A scanner looking deep into a body uses a lower frequency "
                "than one looking just under the skin. Why?",
        "options": [
            {"text": "Because high frequencies are absorbed faster and do "
                     "not reach as far, so depth is traded against detail",
             "correct": True},
            {"text": "Because deep structures are larger and move more "
                     "slowly", "correct": False,
             "why": "Size varies at every depth, and movement is not what "
                    "sets the choice of frequency."},
            {"text": "Because a low frequency travels faster and so gets "
                     "deeper before the echo is needed", "correct": False,
             "why": "All frequencies travel at the same speed in the same "
                    "tissue."},
            {"text": "Because a lower frequency is safer for deep tissue",
             "correct": False,
             "why": "Safety is managed by keeping the power low, not by the "
                    "frequency choice."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h03",
        "band": "harder",
        "text": "A bat hunting in the open uses a lower call, then switches "
                "to a higher one as it closes on a moth. What is it trading?",
        "options": [
            {"text": "Loudness for accuracy — the higher call is quieter "
                     "and more precise, so the bat gives up carrying power "
                     "for care", "correct": False,
             "why": "The switch is about wavelength, not about how loud the "
                    "call is."},
            {"text": "Range for detail — the lower call reaches further, the "
                     "higher one reflects off something as small as a moth",
             "correct": True},
            {"text": "Speed for range — the higher call gets back faster",
             "correct": False,
             "why": "Both calls travel at the same speed through the same "
                    "air."},
            {"text": "Nothing — it is simply excitement", "correct": False,
             "why": "The switch is consistent and well documented, and it "
                    "matches exactly the trade a scanner makes."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h04",
        "band": "harder",
        "text": "An engineer inspecting a weld sees a second pip appear "
                "before the one from the far face of the block. What does "
                "that suggest, and what is needed to turn it into a depth?",
        "options": [
            {"text": "The block is thinner than expected, and no further "
                     "information is needed", "correct": False,
             "why": "The far-face pip is still where it was; something new "
                    "has appeared in front of it."},
            {"text": "The probe is faulty, and it should be replaced before "
                     "any reading is taken, because a second pip is always "
                     "an instrument fault", "correct": False,
             "why": "A fault would not produce a pip at a consistent, "
                    "repeatable time."},
            {"text": "Something inside is reflecting the pulse, and the "
                     "speed of sound in that material is needed to convert "
                     "its timing into a depth", "correct": True},
            {"text": "The pulse has been absorbed partway through, and the "
                     "timing gives the depth directly", "correct": False,
             "why": "Absorbed sound sends nothing back. And the raw timing "
                    "gives the whole path, which still has to be halved."},
        ],
        "figure": None,
    },
]
