"""P6 L8 — Hearing and auditory range (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p6/p6-08-hearing-and-auditory-range.dc.html`.

Her page wins outright. The dog whistle, the seven listeners, the decade
chart, all four rungs and the Childline block are hers.

── ⚖️ NO FORMULA BLOCK, AND THAT IS DESIGN'S CALL ───────────────────

Nothing on this page is quantitative in the CFIFA sense — a range is read,
not computed — and the 23 Aug audit does not list `p6-08` among the
lessons rebuilt onto CFIFA. Adding a worked example here would be
inventing a calculation to fill a block, which is exactly what the audit
rules against. Logged as considered-not-changed.

── ⚖️ RULED · THE AXIS MULTIPLIES, AND THE PAGE SAYS SO ON ITS FACE ──

1 Hz to 110 000 Hz is five powers of ten. On a straight ruler scale the
whole human range would be the first fifth of the axis and every animal
band would pile into one end. `r_log_range` refuses a payload spanning
under three decades, and the lead, the axis caption and the figure's
closing line all tell the student what the marks mean.

── ⚖️ RULED · EVERY BRANCH NAMES A SECOND LISTENER ──────────────────

"The dog can hear it" is a reading. "The dog can hear it and you cannot"
is the lesson. `r_log_range` refuses a branch with no comparison.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-range · s-chart · s-ladder

⚖️ **THE CHART STOP IS TICKED BY THE BENCH.** Design's own `s-chart`
ticks on the gate alone, EARLIER than `s-range`, which also wants a
control touched. `mirrors` would tick it late, so `log-range` marks its
sibling directly at the gate.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    WAVE-29  a dog whistle makes no sound
    WAVE-30  ultrasound is a different kind of sound from ordinary sound
    WAVE-31  losing the top of your range just makes everything quieter
    WAVE-32  animals hear better than people do
"""

LESSON = {
    "slug":  "hearing-and-auditory-range",
    "title": "Hearing and auditory range",
    "discipline": "physics",
    "unit": "Waves and sound",
    "family": "SYSTEM",

    "covers": ["KS3.P.SND.04"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["echoes-reflection-and-absorption"],
    "assumes": [],
    "references": ["frequency-pitch-and-loudness", "how-sound-is-made",
                   "waves-on-water"],
    "ks4_links": [],

    "meta_description": "The words infrasound and ultrasound sound like two "
                        "different kinds of sound. They are not — they are "
                        "two statements about the ears of one particular "
                        "animal, and that animal is us.",

    "big_question": "The words infrasound and ultrasound sound like two "
                    "different kinds of sound. They are not. They are two "
                    "statements about the ears of one particular animal, and "
                    "that animal is us.",

    "rail": [
        {"anchor": "s-hook",   "short": "WHISTLE",
         "label": "The whistle nobody hears", "done_when": "committed"},
        {"anchor": "s-range",  "short": "RANGE",
         "label": "One tone, one listener",   "done_when": "gate_and_a_control"},
        {"anchor": "s-chart",  "short": "CHART",
         "label": "All seven side by side",   "done_when": "sibling_marked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",           "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The whistle nobody can hear.",
        "prompt": "A dog whistle is blown hard in a quiet room. Every person "
                  "there agrees it made no sound at all. The dog is already "
                  "on its feet and looking at the door.",
        "commit": "What is actually coming out of the whistle?",
        "options": [
            "A very quiet tone — too faint for a person to hear, but loud "
            "enough for a dog",
            "A loud tone at a frequency above the top of the human range, "
            "which the dog can respond to",
            "A tone travelling too fast for human ears to catch, but slow "
            "enough for a dog",
            "Nothing — the whistle makes no sound, and the dog reacts to the "
            "puff of air blown through it",
        ],
        "answer": 1,
        "reveal": "Put a microphone in front of it and it registers a strong, "
                  "steady tone at about 30 000 Hz. Nothing is missing from "
                  "the wave — the air is being squeezed and released just as "
                  "vigorously as by any audible note. <strong>What is "
                  "missing is a pair of ears able to respond that "
                  "fast.</strong> Turning it up would not help.",
    },

    "misconceptions": [
        {"id": "WAVE-29",
         "statement": "A dog whistle makes no sound.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        # ⚠️ THE ORDER HERE IS DESIGN'S, NOT MINE. `NOTES-P6-P7.md` §7
        # pre-allocates `WAVE-30` to *losing the top of your range just
        # makes things quieter* — her second Think-again quote on this
        # page. It had been minted onto 31, which would have put a minted
        # id on one of her authored numbers and her authored statement on a
        # spare. Both are back where she put them.
        {"id": "WAVE-30",
         "statement": "Losing the top of your hearing range just makes "
                      "everything a bit quieter.",
         "confronted_by": "s-think"},
        {"id": "WAVE-31",
         "statement": "Ultrasound is a different kind of sound from ordinary "
                      "sound.",
         "elicited_by": "range",
         "confronted_by": "range"},
        {"id": "WAVE-32",
         "statement": "Animals hear better than people do.",
         "elicited_by": "s-ladder",
         "confronted_by": "range"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every ear has a band of frequencies it can respond to, and "
                 "that band is called its <strong>auditory range</strong>. "
                 "Below the bottom of the range the vibrations are too slow "
                 "to set the ear working; above the top they are too fast. A "
                 "healthy young human ear runs from about 20 Hz up to about "
                 "20 000 Hz. Sound below the bottom of the human range is "
                 "called <strong>infrasound</strong>; sound above the top of "
                 "it is called <strong>ultrasound</strong>."},
        {"type": "explainer",
         "text": "Those names are about us, not about the sound. Ultrasound "
                 "is ordinary sound in every physical respect: it is made "
                 "the same way, it travels at the same speed through the "
                 "same material, and it reflects and is absorbed by the same "
                 "rules. <strong>The only thing that makes it ultra is that "
                 "our particular ears stop at 20 000 Hz.</strong> A bat "
                 "hearing a 60 000 Hz call is not hearing something exotic. "
                 "It is just hearing."},
        {"type": "explainer",
         "text": "Ranges are best drawn on a scale where every step "
                 "multiplies rather than adds, because the numbers involved "
                 "span five powers of ten. On the bench below, each mark "
                 "along the axis is ten times the one before it."},

        # ── #s-range · the tone generator ──────────────────────────────
        {"type": "log-range",
         "id": "range",
         "anchor": "s-range",
         "eyebrow": "At the bench · a tone generator and one listener at a "
                    "time",
         "heading": "Sound one tone. Ask one pair of ears.",
         "progress": "Change a control to begin",
         "lead": "A single steady tone at a frequency you choose, and one "
                 "listener in the room. The axis multiplies by ten at every "
                 "mark, because the numbers run from a few hertz to a few "
                 "hundred thousand.",
         "who_label": "Who is listening",
         "start_who": 0,
         "axis_note": "EACH MARK IS TEN TIMES THE ONE BEFORE IT",
         "band_label": "WHAT THIS LISTENER CAN HEAR",
         # ⚠️ `band_anchor` / `band_at` ARE THE KEYS `_sibling` READS.
         # These said `sibling` / `sibling_at`, which the drawer ignored in
         # silence — the wrapper shipped with no `data-sibling`, so nothing
         # ever ticked `#s-chart` and the rail carried a stop that could not
         # complete. MRB-208's gate cannot see it: the band section carries
         # `data-stage-done="0"`, which IS a signal `doneByDom()` reads, so
         # the stop looks reachable and never becomes true.
         # `band_at` is 1 because Design's own DONE gives this stop the
         # GATE alone, while the bench also wants a control touched.
         "band_anchor": "s-chart",
         "band_at": 1,
         "gate": {
             "prompt": "Commit first. A dog whistle sounds at about "
                       "30 000 Hz. A person hears nothing. Why?",
             "options": [
                 "Because 30 000 Hz travels too fast to reach a human ear",
                 "Because 30 000 Hz is above the top of the human range, so "
                 "human ears cannot respond to it",
                 "Because the sound is too quiet for a person and loud "
                 "enough for a dog, and turning it up would let everyone "
                 "hear it",
                 "Because the whistle is not making any sound",
             ],
             "answer": 1,
         },
         "freq": {"label": "The tone you are sounding", "min": 0, "max": 5000,
                  "step": 25, "start": 2400, "value": "251 Hz",
                  "decades": 5, "f_min": 1},
         # ⚠️ SLOWEST BOTTOM FIRST is NOT the order here — Design's tab row
         # runs young human first, because the human range is the reference
         # every other row is read against.
         "listeners": [
             {"id": "human-young", "label": "Human, young", "lo": 20,
              "hi": 20000,
              "note": "About 20 Hz to about 20 000 Hz is the usual figure "
                      "for a healthy young human ear, and it is where the "
                      "words infrasound and ultrasound get their "
                      "boundaries."},
             {"id": "human-50", "label": "Human, at 50", "lo": 20,
              "hi": 12000,
              "note": "The bottom of the range hardly moves with age; the "
                      "top comes down. By about fifty a typical person has "
                      "lost the band above roughly 12 000 Hz, and most never "
                      "notice, because very little of ordinary life lives up "
                      "there."},
             {"id": "dog", "label": "Dog", "lo": 67, "hi": 45000,
              "note": "A dog gives up a little at the bottom and gains a "
                      "great deal at the top, which is what a dog whistle at "
                      "about 30 000 Hz is built to exploit."},
             {"id": "cat", "label": "Cat", "lo": 45, "hi": 64000,
              "note": "A cat reaches higher than a dog, up to about "
                      "64 000 Hz — far enough to hear the ultrasonic squeaks "
                      "mice use to call each other, which is not a "
                      "coincidence."},
             {"id": "bat", "label": "Bat", "lo": 2000, "hi": 110000,
              "note": "A bat has given up the bottom of the range altogether "
                      "and reaches to about 110 000 Hz. Short wavelengths "
                      "reflect off small objects, so a very high call is "
                      "what lets a bat find a moth rather than just a wall."},
             {"id": "elephant", "label": "Elephant", "lo": 16, "hi": 12000,
              "note": "An elephant runs the other way, down to about 16 Hz. "
                      "Low frequencies travel a long way across open ground "
                      "without being absorbed, and elephant herds keep in "
                      "touch over several kilometres with calls people "
                      "nearby can feel more than hear."},
             {"id": "mouse", "label": "Mouse", "lo": 1000, "hi": 91000,
              "note": "A mouse hears almost nothing below about 1000 Hz and "
                      "reaches up to about 91 000 Hz, which is where mice do "
                      "most of their talking to each other."},
         ],
         # ⚖️ EVERY BRANCH NAMES A SECOND LISTENER at the same frequency.
         "branches": {
             # ⊕ PHASE 3, 25 Aug 2026 — HER three sentences, verbatim, with
             # this engine's tokens. The listener's OWN note is prepended by
             # the wiring, exactly as her `benchNote` does, so each state is
             # the material's sentence followed by the tone's.
             #
             # ⚠️ `{other}` NAMES A SPECIFIC SECOND LISTENER, BY HER RULE: an
             # elephant below the band, a bat above it, and inside the band a
             # bat if the young human is selected and a young person if not.
             # This had picked whichever listener happened to differ first,
             # which is a different lesson on some selections.
             "inside":
                 "Your {f} Hz tone falls inside that band, so this listener "
                 "hears it. {other}",
             "below":
                 "Your {f} Hz tone is below the bottom of that band, at "
                 "{lo} Hz, so this listener hears nothing. Nothing is wrong "
                 "with the tone: an elephant, which reaches down to about "
                 "16 Hz, {other}",
             "above":
                 "Your {f} Hz tone is above the top of that band, at {hi} "
                 "Hz, so this listener hears nothing. A bat, which reaches "
                 "to about 110 000 Hz, {other}",
         },
         "readouts": [
             {"id": "freq", "label": "The tone"},
             {"id": "lo", "label": "This listener hears from",
              "sub": "at the bottom of the range"},
             {"id": "hi", "label": "up to", "sub": "at the top of the range"},
             {"id": "verdict", "label": "Can this listener hear it?"},
         ]},

        # ── #s-chart · all seven on one decade axis ────────────────────
        {"type": "wave-band",
         "id": "range-chart",
         "anchor": "s-chart",
         "eyebrow": "The figure",
         "heading": "All seven on one multiplying scale",
         "chart": {
             "aria_label": "A chart of seven auditory ranges on an axis that "
                           "multiplies by ten at every mark, from 1 hertz to "
                           "100 000 hertz. The young human range, 20 to "
                           "20 000 hertz, is shaded behind every row; "
                           "everything left of it is labelled infrasound and "
                           "everything right of it ultrasound. From the "
                           "bottom up: elephant 16 to 12 000, young human 20 "
                           "to 20 000, human at 50 20 to 12 000, dog 67 to "
                           "45 000, cat 45 to 64 000, mouse 1000 to 91 000, "
                           "bat 2000 to 110 000 hertz.",
             "human": {"lo": 20, "hi": 20000},
             "infra_label": "INFRASOUND",
             "ultra_label": "ULTRASOUND",
             "rows": [
                 {"label": "Elephant",     "lo": 16,   "hi": 12000,
                  "value": "16 – 12 000 Hz"},
                 {"label": "Human, young", "lo": 20,   "hi": 20000,
                  "value": "20 – 20 000 Hz"},
                 {"label": "Human, at 50", "lo": 20,   "hi": 12000,
                  "value": "20 – 12 000 Hz"},
                 {"label": "Dog",          "lo": 67,   "hi": 45000,
                  "value": "67 – 45 000 Hz"},
                 {"label": "Cat",          "lo": 45,   "hi": 64000,
                  "value": "45 – 64 000 Hz"},
                 {"label": "Mouse",        "lo": 1000, "hi": 91000,
                  "value": "1 000 – 91 000 Hz"},
                 {"label": "Bat",          "lo": 2000, "hi": 110000,
                  "value": "2 000 – 110 000 Hz"},
             ],
         },
         "close": "Read the shaded strip as the human range. Everything to "
                  "the left of it is infrasound and everything to the right "
                  "is ultrasound, and both names are about us. On a scale "
                  "that multiplied by ten at every mark, a bar reaching one "
                  "mark further right is a range going ten times higher — "
                  "which is why a straight ruler scale would have squashed "
                  "every one of these bars into the same left-hand "
                  "centimetre."},

        {"type": "key-fact", "ref": "what-a-range-is"},

        {"type": "misconception", "id": "think-whistle-silent",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-whistle-silent",
         "kind": "predict",
         "demand": "explain",
         "targets": "WAVE-29",
         "statements": [
             {"quote": "A dog whistle makes no sound.",
              "targets": "WAVE-29",
              "body": [
                  "It makes a great deal of sound, and a microphone put in "
                  "front of it registers a loud steady tone at about 30 000 "
                  "Hz. Nothing is missing from the wave: the air is being "
                  "squeezed and released just as vigorously as it would be "
                  "by an audible note, and if you stood close enough with "
                  "the right instrument you could measure it. What is "
                  "missing is a pair of ears able to respond that fast. The "
                  "word inaudible is a statement about the listener.",
              ]},
             {"quote": "Losing the top of your hearing range just makes "
                      "everything a bit quieter.",
              "targets": "WAVE-31",
              "body": [
                  "It takes pieces out rather than turning a dial down. "
                  "High frequencies are what make consonants distinct — the "
                  "difference between s and f, or t and k, sits mostly "
                  "above 4000 Hz — so the first thing people notice when "
                  "the top of their range drops is not that speech is quiet "
                  "but that it is mumbled, especially in a noisy room where "
                  "the low frequencies are still arriving perfectly well. "
                  "That is also why simply shouting at someone with hearing "
                  "loss often does not help: the missing information was "
                  "never in the loud part.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "what-a-range-is",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "An auditory range is the band of frequencies an ear can "
                 "respond to, and a healthy young human ear covers about 20 "
                 "Hz to 20 000 Hz. Sound below that band is infrasound and "
                 "sound above it is ultrasound; both names describe our ears "
                 "rather than the sound, which behaves in exactly the same "
                 "way at every frequency. Many animals hear well outside our "
                 "band, and the top of the human range falls with age."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 1 and 2.
    "ladder": {
        "recall": {
            "q": "A tone of 30 000 Hz is sounded in a room holding a young "
                 "person, a dog and an elephant. Who can hear it?",
            "options": [
                "The dog only — 30 000 Hz is above the top of the human "
                "range and above the top of the elephant’s.",
                "Nobody — 30 000 Hz is ultrasound, and ultrasound is not "
                "really sound, so nothing in the room can respond to it "
                "however good its ears are",
                "The dog and the elephant — animals hear better than people "
                "do.",
                "All three — the tone is very high, and high sounds carry "
                "best.",
            ],
            "answer": 0,
            "feedback": {
                1: "Ultrasound is ordinary sound in every respect; the name "
                   "only means it is above the human range. The dog’s range "
                   "reaches about 45 000 Hz, so the dog hears it.",
                2: "Not all animals, and not in the same direction. The "
                   "elephant’s strength is at the bottom of the scale, "
                   "reaching down to about 16 Hz; its top is around 12 000 "
                   "Hz, lower than a young person’s.",
                3: "How well a sound carries is a different question from "
                   "whether an ear can respond to it. Above the top of a "
                   "range, nothing is heard at all, however well the sound "
                   "has travelled.",
            },
            "title": "Rung 1 · Read the ranges"},
        "apply": {
            "q": "A dog whistle is blown and no person in the room hears "
                 "anything. Which statement is right?",
            "options": [
                "The whistle produces a very quiet sound that only a dog’s "
                "more sensitive ears can pick up.",
                "The sound is there, but it travels too fast for human ears "
                "to catch it.",
                "The whistle produces no sound at all, and dogs are "
                "responding to the air being blown rather than to a sound, "
                "which is why a dog reacts and a microphone in the same "
                "room registers nothing",
                "The whistle is producing a loud tone at about 30 000 Hz, "
                "and human ears cannot respond to a vibration that fast — a "
                "microphone in the same room records it easily.",
            ],
            "answer": 3,
            "feedback": {
                0: "Loudness is not the issue. The tone is loud, and "
                   "turning it up would still not make a person hear it — "
                   "it is above the top of the human range.",
                1: "The verdict is right and the rule is wrong. Every "
                   "frequency travels through the same air at the same "
                   "speed; what changes is how many times a second the ear "
                   "is asked to respond.",
                2: "A microphone placed in front of it registers a strong "
                   "steady tone. There is a sound; there are no ears in the "
                   "room able to respond to it.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A bat hunts small insects in complete darkness by sending "
                 "out calls and listening for what comes back. Explain why "
                 "a range reaching up to about 110 000 Hz suits that job "
                 "better than a range like ours would.",
            "field_label": "Your explanation",
            "placeholder": "A very high frequency means…",
            "success": [
                "Says the bat sends out sound and listens for the "
                "reflection.",
                "Says a very high frequency has a very short wavelength.",
                "Says short wavelengths reflect well off small objects such "
                "as an insect.",
                "Says a lower-frequency call would give a reflection off "
                "large objects but tell the bat little about a moth.",
                "Says the bat can hear its own returning call because its "
                "range reaches that high, while ours does not.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Some shops have fitted a device that sounds a continuous "
                 "tone at about 17 000 Hz outside the door. Explain who is "
                 "likely to hear it and who is not, and give one reason "
                 "people have argued about whether such devices should be "
                 "allowed.",
            "field_label": "Your answer",
            "placeholder": "A tone at 17 000 Hz sits…",
            "success": [
                "Says 17 000 Hz sits near the top of the young human range.",
                "Says the top of the range falls with age, so many older "
                "adults cannot hear it.",
                "Says younger people are therefore the ones affected, which "
                "is what the device is designed to do.",
                "Says the tone reaches everyone in the street, not only the "
                "people it is aimed at — including babies and people who "
                "happen to be passing.",
                "Gives a reasoned objection or defence, for example that it "
                "targets people by age rather than by anything they have "
                "done, or that a shopkeeper has a real problem it is meant "
                "to solve.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "An auditory range is the band of frequencies an ear can "
                "respond to. A healthy young human ear runs from about 20 Hz "
                "to about 20 000 Hz; below that is infrasound and above it is "
                "ultrasound, and both names describe our ears rather than the "
                "sound itself. Other animals have their bands in different "
                "places: a bat reaches to about 110 000 Hz and an elephant "
                "down to about 16 Hz. The top of the human range falls with "
                "age and with exposure to loud sound, and that loss is "
                "permanent.",

    "stretch": [
        {"id": "where-a-range-sits-is-about-the-job",
         "type": "explainer",
         "text": "Where an animal's range sits is usually about the job it "
                 "has to do. Echolocation needs high frequencies, because a "
                 "short wavelength is what reflects off something small: a "
                 "bat calling at 100 000 Hz uses a wavelength of a few "
                 "millimetres and can pick a moth out of the air, while a "
                 "call at 1000 Hz would tell it only where the walls are. "
                 "Long-distance communication needs the opposite. Low "
                 "frequencies are absorbed far less by air and by ground "
                 "cover, so elephant rumbles near 16 Hz carry for "
                 "kilometres, and the loudest thing in the ocean is a blue "
                 "whale calling below 20 Hz."},
        {"id": "noise-damage-is-an-injury",
         "type": "explainer",
         "text": "Hearing loss from noise is a physical injury, not a "
                 "tiredness. The hair cells in the inner ear that respond to "
                 "the highest frequencies are the ones nearest the entrance, "
                 "they take the most punishment, and they do not grow back "
                 "in humans. That is why the damage shows up at the top of "
                 "the range first, why it accumulates over years, and why it "
                 "is one of the few injuries that is completely preventable "
                 "and completely permanent. Earplugs at a concert and a "
                 "volume limit on headphones are cheap; the hair cells are "
                 "not replaceable at any price."},
    ],

    "support": [],

    # ⊕ §8.10 · THE TREATMENT IS THE RULING. Design drew this as a small
    # block at the bottom edge above the legal line, which is exactly what
    # `safeguarding_note` renders: one quiet `.ks3-legal` foot line, NEVER a
    # callout. It goes here rather than in `support[]` — that layer is the
    # "Need a hand?" study scaffold and would print this as a panel.
    #
    # ⚠️ THE NUMBER IS NOT TAKEN UP. Childline, 0800 1111, is the same
    # service and the same digits the B5 lessons already carry; nothing new
    # is being introduced. The school routes stay as the daytime answer.
    "safeguarding_note": "Hearing damage from loud sound builds up quietly "
                         "and does not repair itself, so ringing ears after a "
                         "night out, or finding you keep turning the volume "
                         "up, are worth mentioning to someone rather than "
                         "ignoring. You can talk to a doctor, a school nurse "
                         "or any adult you trust. Childline is free, "
                         "confidential and open at any hour, on 0800 1111, "
                         "and you do not have to give your name.",

    "vocabulary": [
        {"term": "auditory range",
         "definition": "The band of frequencies a particular ear can respond "
                       "to, from the lowest it can hear to the highest."},
        {"term": "infrasound",
         "definition": "Sound below the bottom of the human range, under "
                       "about 20 Hz."},
        {"term": "ultrasound",
         "definition": "Sound above the top of the human range, over about "
                       "20 000 Hz. Ordinary sound in every other respect."},
    ],

    "tutor": {
        "anchor": "s-range",
        "prompt": "Ask Mr Badmus AI",
        "body": "Wondering which animals could hear a particular frequency?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The human audible range and how the ear converts pressure "
                   "changes to electrical impulses, ultrasound and infrasound "
                   "applications, and noise-induced hearing loss.",

    "convention_note": "Every range on this page is an approximate figure for "
                       "a typical healthy adult of that species, and "
                       "individuals vary widely; published values differ "
                       "between studies, partly because they disagree about "
                       "how quiet a sound has to be before an animal counts "
                       "as hearing it. The 20 Hz and 20 000 Hz limits of the "
                       "human range are round conventions rather than "
                       "measurements, and very few adults reach 20 000 Hz. "
                       "The human-at-50 figure is a typical outcome, not a "
                       "schedule: age-related loss varies enormously between "
                       "people and is made much worse by a lifetime of loud "
                       "sound. A range says only whether an ear can respond "
                       "to a frequency at all; it says nothing about how "
                       "well.",

    "ws": [],
}
