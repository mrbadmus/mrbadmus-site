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
    {
        "id": "p6-08-e01",
        "band": "easier",
        "text": "The auditory range of a healthy young human is about…",
        "options": [
            {"text": "0 Hz to 1000 Hz",
                         "correct": False,
                         "why": "The top of the human range is far higher than 1000 Hz — most music lives "
                    "above it."},
            {"text": "20 Hz to 2000 Hz",
                         "correct": False,
                         "why": "The bottom is right and the top is ten times too low."},
            {"text": "200 Hz to 20 000 Hz",
                         "correct": False,
                         "why": "The top is right and the bottom is ten times too high; people hear well "
                    "below 200 Hz."},
            {"text": "20 Hz to 20 000 Hz",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e02",
        "band": "easier",
        "text": "Sound above the top of the human range is called…",
        "options": [
            {"text": "infrasound",
                         "correct": False,
                         "why": "Infrasound is below the bottom of the range, not above the top."},
            {"text": "supersound",
                         "correct": False,
                         "why": "Not a term used in physics."},
            {"text": "ultrasound",
                         "correct": True},
            {"text": "silence",
                         "correct": False,
                         "why": "It is a real sound and a microphone records it. Only our ears are missing "
                    "out."},
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
                         "why": "16 Hz is below about 20 Hz, so it is under the bottom of the human range."},
            {"text": "infrasound, as far as human ears are concerned",
                         "correct": True},
            {"text": "ultrasound, well above the top of the human range",
                         "correct": False,
                         "why": "Ultrasound is above the top of our range. 16 Hz is at the other end "
                    "entirely."},
            {"text": "not sound at all, just a vibration too low to count",
                         "correct": False,
                         "why": "It is an ordinary pressure wave in air, made and carried in exactly the same "
                    "way."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e04",
        "band": "easier",
        "text": "As people get older, the usual change to their auditory range is that…",
        "options": [
            {"text": "the top of it comes down",
                         "correct": True},
            {"text": "the bottom of it rises a long way",
                         "correct": False,
                         "why": "The bottom hardly moves. It is the top that is lost."},
            {"text": "the whole range shifts upwards",
                         "correct": False,
                         "why": "Nothing shifts. The band gets narrower at the top."},
            {"text": "it stays the same and everything just gets quieter",
                         "correct": False,
                         "why": "Frequencies above the new top are gone altogether, however loud they are "
                    "made."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s01",
        "band": "standard",
        "text": "Why are auditory ranges usually drawn on an axis where each mark is ten "
                "times the one before?",
        "options": [
            {"text": "Because a straight scale is harder for a reader to take in at a glance, and "
                     "a stepped one is always the easier of the two to read off",
                         "correct": False,
                         "why": "A straight scale is easy to read. The trouble is what it would show."},
            {"text": "Because the numbers run from a few hertz to over a hundred thousand, and on "
                     "a straight scale every band would pile into one end",
                         "correct": True},
            {"text": "Because frequency can only be measured in powers of ten, so those are the "
                     "only marks that could honestly be put along the axis at all",
                         "correct": False,
                         "why": "Frequency can be any value at all — 440 Hz, for instance."},
            {"text": "Because the ear can only hear frequencies that are powers of ten, and the "
                     "marks along the axis are exactly where hearing actually happens",
                         "correct": False,
                         "why": "The ear responds across the whole band continuously."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s02",
        "band": "standard",
        "text": "A cat's range runs to about 64 000 Hz and a mouse does most of its calling "
                "near 60 000 Hz. What does that suggest?",
        "options": [
            {"text": "That a cat can hear mice talking to each other",
                         "correct": True},
            {"text": "That mice can hear cats coming",
                         "correct": False,
                         "why": "That may be true, but it is not what the two numbers given here line up to "
                    "show."},
            {"text": "That mice and cats use the same calls",
                         "correct": False,
                         "why": "The mouse is calling and the cat is listening. Nothing says the cat calls at "
                    "that frequency."},
            {"text": "That both are using ultrasound to see in the dark",
                         "correct": False,
                         "why": "Neither echolocates. They are simply hearing and calling."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s03",
        "band": "standard",
        "text": "A tone at 15 Hz is played very loudly to a person and a dog. Who hears it?",
        "options": [
            {"text": "Both, because it is loud",
                         "correct": False,
                         "why": "Loudness cannot rescue a frequency outside a range. 15 Hz is below both "
                    "bottoms."},
            {"text": "The dog only, because dogs hear better",
                         "correct": False,
                         "why": "The dog's range starts at about 67 Hz — higher than ours, not lower."},
            {"text": "Neither — 15 Hz is below the bottom of both ranges",
                         "correct": True},
            {"text": "The person only, because human ears reach lower than a dog's",
                         "correct": False,
                         "why": "Human ears do reach lower than a dog's, but not as low as 15 Hz."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s04",
        "band": "standard",
        "text": "Which statement about ultrasound is correct?",
        "options": [
            {"text": "It travels faster than audible sound in the same material, which is why an "
                     "echo from it comes back sooner",
                         "correct": False,
                         "why": "Every frequency travels at the same speed in the same material."},
            {"text": "It cannot be reflected or absorbed",
                         "correct": False,
                         "why": "It reflects and is absorbed by exactly the same rules, which is what makes "
                    "scanning possible."},
            {"text": "It does not need a material to travel through",
                         "correct": False,
                         "why": "It needs a medium like any other sound, which is why a scanner needs gel."},
            {"text": "It is ordinary sound whose frequency happens to be above the top of the "
                     "human range",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h01",
        "band": "harder",
        "text": "A bat's range starts at about 2000 Hz — far higher than ours — and reaches "
                "about 110 000 Hz. What does giving up the bottom of the range cost a bat, "
                "and why is it worth it?",
        "options": [
            {"text": "It loses low sounds it has little use for, and gains the very short "
                     "wavelengths that reflect off insects",
                         "correct": True},
            {"text": "It loses nothing, because 2000 Hz is the lowest sound there is",
                         "correct": False,
                         "why": "Sounds far below 2000 Hz exist everywhere — an elephant's rumble at 16 Hz, "
                    "for one."},
            {"text": "It loses the ability to hear other bats, which is why bats hunt alone and "
                     "never call to one another",
                         "correct": False,
                         "why": "Bat calls are high, well inside the bat's own range, and bats are often "
                    "highly social."},
            {"text": "It gains loudness, because a narrower range concentrates the hearing",
                         "correct": False,
                         "why": "A range says which frequencies an ear responds to, not how loud they seem."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h02",
        "band": "harder",
        "text": "Someone with age-related hearing loss says speech sounds mumbled rather than "
                "quiet, and shouting does not help. Why?",
        "options": [
            {"text": "Because shouting lowers the pitch of a voice, making it harder still",
                         "correct": False,
                         "why": "Shouting raises the volume; it does not systematically lower the pitch "
                    "enough to matter here."},
            {"text": "Because the frequencies that separate consonants sit high, and those are the "
                     "ones that have gone — turning up what is left does not restore them",
                         "correct": True},
            {"text": "Because loud sound is absorbed more strongly by a damaged ear",
                         "correct": False,
                         "why": "The loss is a missing band, not extra absorption of loud sound."},
            {"text": "Because mumbling is a habit of the speaker rather than anything about the "
                     "listener, and speaking more clearly would fix it whoever was in the room",
                         "correct": False,
                         "why": "The same speaker is perfectly clear to someone else in the room, so the "
                    "difference is in the listening."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h03",
        "band": "harder",
        "text": "On a chart where each mark is ten times the one before, a bat's bar reaches "
                "roughly one mark further right than a dog's. What does that gap mean?",
        "options": [
            {"text": "The bat hears about ten hertz higher than the dog",
                         "correct": False,
                         "why": "On a multiplying scale a step is a factor, not an addition."},
            {"text": "The bat hears about ten times louder than the dog",
                         "correct": False,
                         "why": "The axis is frequency, and says nothing about loudness."},
            {"text": "The bat hears ten times as many different frequencies",
                         "correct": False,
                         "why": "Both hear a continuous band. The chart compares where the tops of the bands "
                    "are."},
            {"text": "The bat's top frequency is roughly ten times the dog's",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h04",
        "band": "harder",
        "text": "Why is it misleading to say simply that animals hear better than people?",
        "options": [
            {"text": "Because animals actually hear a good deal worse than people do, and the "
                     "ranges shown on the chart have been exaggerated",
                         "correct": False,
                         "why": "The ranges are real. Reversing the claim keeps the same one-dimensional "
                    "thinking."},
            {"text": "Because a range only says what an ear responds to at all, and it says "
                     "nothing whatever about how well it does any of it",
                         "correct": False,
                         "why": "True, and worth saying — but it is not the main thing wrong with the "
                    "sentence, which is about direction."},
            {"text": "Because ranges sit in different places rather than being simply wider: an "
                     "elephant reaches lower than us and stops lower too",
                         "correct": True},
            {"text": "Because only mammals have auditory ranges at all, and the chart leaves out "
                     "every other kind of animal there is",
                         "correct": False,
                         "why": "Birds, fish and insects all detect sound, and many have measured ranges."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e05",
        "band": "easier",
        "text": "Sound below the bottom of the human range is called…",
        "options": [
            {"text": "ultrasound",
                         "correct": False,
                         "why": "Ultrasound is ABOVE the top of our range, not below the bottom of it."},
            {"text": "infrasound",
                         "correct": True},
            {"text": "silence",
                         "correct": False,
                         "why": "It is a real sound that other animals hear; it is only silent to us."},
            {"text": "a rarefaction",
                         "correct": False,
                         "why": "A rarefaction is a stretched-out patch within any sound wave, at any "
                    "frequency."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s05",
        "band": "standard",
        "text": "A whistle sounds steadily at 25 000 Hz in a room holding a person and a dog. "
                "Who hears it?",
        "options": [
            {"text": "Both of them, because it is a real sound",
                         "correct": False,
                         "why": "It is real, but 25 000 Hz is above the top of a human range of about 20 000 "
                    "Hz."},
            {"text": "Neither, because nothing is really being made",
                         "correct": False,
                         "why": "The whistle is vibrating and sending out a wave like any other."},
            {"text": "The dog only, whose range reaches higher",
                         "correct": True},
            {"text": "The person only, because dogs hear lower notes",
                         "correct": False,
                         "why": "A dog's range reaches far higher than ours, not lower."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h05",
        "band": "harder",
        "text": "A bat calls at 80 000 Hz. Why is that not a different KIND of sound from a "
                "human shout?",
        "options": [
            {"text": "Because both are made by vibrations and obey the same rules; only our ears "
                     "differ",
                         "correct": True},
            {"text": "Because a bat's call is much quieter, so it is only a faint version",
                         "correct": False,
                         "why": "Loudness is amplitude and is a separate matter; some bat calls are extremely "
                    "loud."},
            {"text": "Because it becomes an ordinary sound once it reflects off something",
                         "correct": False,
                         "why": "Reflecting does not change a sound's frequency, so it comes back just as "
                    "inaudible."},
            {"text": "Because all sound above 20 000 Hz travels faster than audible sound",
                         "correct": False,
                         "why": "Every frequency travels at the same speed through the same material."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e06",
        "band": "easier",
        "text": "A dog whistle and a smoke alarm's chirp are both genuine, physical sounds, "
                "yet most adults hear only one of them clearly. Which property of a sound "
                "mainly decides whether a particular listener can hear it?",
        "options": [
            {"text": "its frequency, compared with that listener's auditory range",
                         "correct": True},
            {"text": "its colour, since higher-pitched sounds are always a different colour to the "
                     "ear",
                         "correct": False,
                         "why": "Sound has no colour; colour is a property of light, an entirely different "
                    "kind of wave."},
            {"text": "how far the sound has travelled before reaching the listener",
                         "correct": False,
                         "why": "Distance mainly affects how loud a sound arrives, not whether its frequency "
                    "falls inside a listener's range at all."},
            {"text": "how many people are listening to it at once",
                         "correct": False,
                         "why": "The number of listeners present has no effect on whether any one of them can "
                    "hear a given sound."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e07",
        "band": "easier",
        "text": "Which of these three is a genuine, physical sound wave: a bat's ultrasonic "
                "call, a burst of radio static, or a beam of infrared light?",
        "options": [
            {"text": "the beam of infrared light, since light and sound are simply two names for "
                     "the same kind of wave",
                         "correct": False,
                         "why": "Light and sound are different kinds of wave entirely; infrared light is "
                    "electromagnetic, not a vibration passing through a material."},
            {"text": "the bat's ultrasonic call",
                         "correct": True},
            {"text": "the burst of radio static, since static is simply a very high-pitched sound",
                         "correct": False,
                         "why": "Radio static is an electromagnetic signal, not a sound wave, however it "
                    "might be described informally."},
            {"text": "none of the three — all three are electromagnetic signals of one kind or "
                     "another",
                         "correct": False,
                         "why": "A bat's call is an ordinary mechanical sound wave, made by vibration and "
                    "needing air or another material to travel through, unlike the other two."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e08",
        "band": "easier",
        "text": "A rumbling sound sits at 10 Hz, below the bottom of the human range. This "
                "kind of sound is called…",
        "options": [
            {"text": "ultrasound",
                         "correct": False,
                         "why": "Ultrasound is above the top of the human range, not below the bottom of it."},
            {"text": "a rarefaction",
                         "correct": False,
                         "why": "A rarefaction is a stretched-out patch found within any sound wave, at any "
                    "frequency, not a name for a frequency band."},
            {"text": "infrasound",
                         "correct": True},
            {"text": "an echo",
                         "correct": False,
                         "why": "An echo is reflected sound heard as a separate sound; it has nothing to do "
                    "with a sound's frequency being high or low."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e09",
        "band": "easier",
        "text": "The words infrasound and ultrasound are defined relative to which animal's "
                "hearing?",
        "options": [
            {"text": "a dog's",
                         "correct": False,
                         "why": "A dog's range is wider than a human's at the top, so the boundary is not set "
                    "by dogs."},
            {"text": "a bat's",
                         "correct": False,
                         "why": "A bat's range reaches far higher than the 20 000 Hz boundary the two terms "
                    "use."},
            {"text": "no particular animal's — the terms describe the sound itself",
                         "correct": False,
                         "why": "Ultrasound and infrasound are ordinary sound in every physical respect; the "
                    "terms describe a listener's hearing, not the sound."},
            {"text": "a human's",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e10",
        "band": "easier",
        "text": "A dog's auditory range runs from about…",
        "options": [
            {"text": "67 Hz to 45 000 Hz",
                         "correct": True},
            {"text": "20 Hz to 20 000 Hz",
                         "correct": False,
                         "why": "That is the human range; a dog's range starts higher and reaches further."},
            {"text": "2 Hz to 4500 Hz",
                         "correct": False,
                         "why": "That places both ends far too low for a dog."},
            {"text": "670 Hz to 450 000 Hz",
                         "correct": False,
                         "why": "Both figures here are ten times too high for a dog's real range."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e11",
        "band": "easier",
        "text": "A cat's auditory range reaches up to about…",
        "options": [
            {"text": "6400 Hz",
                         "correct": False,
                         "why": "That is ten times too low for a cat's real top frequency."},
            {"text": "640 000 Hz",
                         "correct": False,
                         "why": "That is ten times too high for a cat's real top frequency."},
            {"text": "64 000 Hz",
                         "correct": True},
            {"text": "6400 000 Hz",
                         "correct": False,
                         "why": "That is a hundred times too high for a cat's real top frequency."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e12",
        "band": "easier",
        "text": "An elephant's auditory range reaches up to about…",
        "options": [
            {"text": "1200 Hz",
                         "correct": False,
                         "why": "That is ten times too low for an elephant's real top frequency."},
            {"text": "120 000 Hz",
                         "correct": False,
                         "why": "That is ten times too high, closer to a bat's top frequency than an "
                    "elephant's."},
            {"text": "12 Hz",
                         "correct": False,
                         "why": "That is far too low, and it is close to the bottom of an elephant's range "
                    "rather than its top."},
            {"text": "12 000 Hz",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e13",
        "band": "easier",
        "text": "A bat's auditory range starts at about…",
        "options": [
            {"text": "200 Hz",
                         "correct": False,
                         "why": "That is ten times too low for a bat's real bottom frequency."},
            {"text": "20 000 Hz",
                         "correct": False,
                         "why": "That is ten times too high for a bat's real bottom frequency — 20 000 Hz is "
                    "close to the top of the human range instead."},
            {"text": "2000 Hz",
                         "correct": True},
            {"text": "2 Hz",
                         "correct": False,
                         "why": "That is a thousand times too low for a bat's real bottom frequency."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e14",
        "band": "easier",
        "text": "A mouse's auditory range runs from about…",
        "options": [
            {"text": "1000 Hz to 91 000 Hz",
                         "correct": True},
            {"text": "100 Hz to 9100 Hz",
                         "correct": False,
                         "why": "Both figures here are ten times too low for a mouse's real range."},
            {"text": "10 000 Hz to 910 000 Hz",
                         "correct": False,
                         "why": "Both figures here are ten times too high for a mouse's real range."},
            {"text": "20 Hz to 20 000 Hz",
                         "correct": False,
                         "why": "That is the human range; a mouse hears almost nothing near the bottom of "
                    "that range."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e15",
        "band": "easier",
        "text": "Which hears higher-pitched sounds, a dog or a cat?",
        "options": [
            {"text": "The dog, because its range reaches about 64 000 Hz at the top",
                         "correct": False,
                         "why": "64 000 Hz is the cat's top frequency, not the dog's; a dog's range reaches "
                    "lower, to about 45 000 Hz."},
            {"text": "Neither — dogs and cats share exactly the same auditory range",
                         "correct": False,
                         "why": "The two ranges differ: a dog reaches about 45 000 Hz and a cat reaches about "
                    "64 000 Hz."},
            {"text": "The cat, because its range reaches higher, to about 64 000 Hz at the top",
                         "correct": True},
            {"text": "The dog, because dogs are generally the larger animal of the two",
                         "correct": False,
                         "why": "Body size is not what decides the top of an animal's auditory range; the "
                    "cat's range simply reaches higher."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e16",
        "band": "easier",
        "text": "Whose range reaches lower, a mouse's or a young human's?",
        "options": [
            {"text": "The mouse's, since its range starts at about 1000 Hz and a human's starts at "
                     "about 20 Hz",
                         "correct": False,
                         "why": "1000 Hz is higher than 20 Hz, so the mouse's range starts higher, not lower."},
            {"text": "Neither reaches especially low compared with other animals in general",
                         "correct": False,
                         "why": "A young human's 20 Hz is in fact one of the lower starting points among the "
                    "animals in this lesson."},
            {"text": "They are the same, since both start close to the bottom of what any mammal "
                     "can hear",
                         "correct": False,
                         "why": "The two starting points are quite different: about 20 Hz for a human against "
                    "about 1000 Hz for a mouse."},
            {"text": "The human's, since its range starts at about 20 Hz and a mouse's starts at "
                     "about 1000 Hz",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e17",
        "band": "easier",
        "text": "As a person gets older, by around what age has the top of their hearing "
                "range typically fallen to about 12 000 Hz?",
        "options": [
            {"text": "about ten",
                         "correct": False,
                         "why": "The fall described in this lesson is a change over adult life, not something "
                    "typically seen by age ten."},
            {"text": "there is no such typical age — hearing range does not change with age",
                         "correct": False,
                         "why": "The top of the human range does fall with age; around fifty is the typical "
                    "figure given for reaching about 12 000 Hz."},
            {"text": "about ninety",
                         "correct": False,
                         "why": "By about fifty, not ninety, a typical person has already lost the band above "
                    "roughly 12 000 Hz."},
            {"text": "about fifty",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e18",
        "band": "easier",
        "text": "Hearing damage caused by exposure to loud sound is best described as…",
        "options": [
            {"text": "a physical injury to the ear that does not repair itself",
                         "correct": True},
            {"text": "a kind of tiredness that clears up with a good night's sleep",
                         "correct": False,
                         "why": "The damage is permanent rather than something that clears up with rest, "
                    "unlike ordinary tiredness."},
            {"text": "a short-term dip in hearing that returns to normal within a few days",
                         "correct": False,
                         "why": "The hair cells involved do not grow back in humans, so the loss is lasting "
                    "rather than a short-term dip."},
            {"text": "a reaction some people have to dust or pollen in the air",
                         "correct": False,
                         "why": "The damage described here comes from loud sound itself, not from an allergic "
                    "reaction to something in the air."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e19",
        "band": "easier",
        "text": "Once the hair cells in the inner ear that respond to the highest frequencies "
                "are damaged by loud sound, do they grow back in humans?",
        "options": [
            {"text": "Yes, within a few weeks of rest",
                         "correct": False,
                         "why": "These hair cells do not regrow in humans, however long a person rests their "
                    "hearing."},
            {"text": "Yes, but only very slowly, over several years",
                         "correct": False,
                         "why": "There is no slow regrowth either — once damaged, these particular hair cells "
                    "are gone for good in humans."},
            {"text": "No, they do not grow back in humans",
                         "correct": True},
            {"text": "No, because humans never had working hair cells there in the first place",
                         "correct": False,
                         "why": "The hair cells are present and working before the damage; it is the damage "
                    "itself that removes them permanently."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e20",
        "band": "easier",
        "text": "Compared with high-frequency sound, low-frequency sound travels further "
                "through open air mainly because it is…",
        "options": [
            {"text": "absorbed less by the air and by ground cover as it travels",
                         "correct": True},
            {"text": "made up of bigger, heavier particles that carry it further",
                         "correct": False,
                         "why": "Sound is a disturbance passing through the same air particles at every "
                    "frequency; it does not carry its own heavier particles."},
            {"text": "reflected back and forth between the ground and the sky many times over",
                         "correct": False,
                         "why": "Low frequencies travel further because less of them is absorbed on the way, not because of repeated reflection off the sky."},
            {"text": "converted partway into light, which then travels the rest of the distance",
                         "correct": False,
                         "why": "Sound energy is not converted into light on its journey through the air."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e21",
        "band": "easier",
        "text": "Elephant herds keep in touch over several kilometres using very low rumbles "
                "partly because…",
        "options": [
            {"text": "low frequencies are absorbed less by open ground and so carry further",
                         "correct": True},
            {"text": "low frequencies travel faster than high ones over long distances",
                         "correct": False,
                         "why": "Every frequency of sound travels at the same speed through the same air; "
                    "speed is not what lets the rumble carry further."},
            {"text": "elephants are simply louder than most other land animals",
                         "correct": False,
                         "why": "The advantage described in the lesson comes from the frequency being low, "
                    "not from the animal being louder overall."},
            {"text": "high frequencies cannot travel through open air at all",
                         "correct": False,
                         "why": "High frequencies do travel through open air; they are simply absorbed more "
                    "over the same distance than low frequencies are."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e22",
        "band": "easier",
        "text": "The loudest calls in the ocean, made by blue whales, are pitched…",
        "options": [
            {"text": "above 20 000 Hz, well into ultrasound",
                         "correct": False,
                         "why": "Blue whale calls sit at the opposite end of the scale, below the human "
                    "range, not above it."},
            {"text": "right in the middle of the human range, around 1000 Hz",
                         "correct": False,
                         "why": "Blue whale calls are described as being below 20 Hz, not in the middle of "
                    "the human range."},
            {"text": "at exactly the same pitch as a dog whistle",
                         "correct": False,
                         "why": "A dog whistle is tuned to a high ultrasonic frequency; a blue whale's call "
                    "sits at the very opposite, infrasonic end of the scale."},
            {"text": "below 20 Hz, into infrasound",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e23",
        "band": "easier",
        "text": "The band of frequencies a particular animal's ear can respond to is called "
                "its…",
        "options": [
            {"text": "hearing threshold",
                         "correct": False,
                         "why": "A threshold usually names a single boundary value, not the whole band an ear "
                    "responds to."},
            {"text": "sound spectrum",
                         "correct": False,
                         "why": "A spectrum is a general spread of frequencies in a sound or a signal, not a "
                    "term for what one particular ear can respond to."},
            {"text": "pitch scale",
                         "correct": False,
                         "why": "Pitch describes how high or low a single note sounds, not the whole band an "
                    "ear can respond to."},
            {"text": "auditory range",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e24",
        "band": "easier",
        "text": "Does ultrasound travel faster through air than an audible sound of the same "
                "loudness?",
        "options": [
            {"text": "Yes, ultrasound is faster",
                         "correct": False,
                         "why": "Every frequency of sound travels at the same speed through the same air; "
                    "frequency does not change the speed."},
            {"text": "No — both travel at the same speed through the same air",
                         "correct": True},
            {"text": "No, ultrasound is slower, because it is a heavier kind of wave",
                         "correct": False,
                         "why": "Ultrasound is not a heavier wave of any kind; it travels at exactly the same "
                    "speed as audible sound in the same air."},
            {"text": "It depends on how loud each sound is",
                         "correct": False,
                         "why": "Loudness does not affect the speed of sound; speed depends on the material "
                    "the sound travels through."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e25",
        "band": "easier",
        "text": "On a chart of auditory ranges, each mark along the axis represents…",
        "options": [
            {"text": "ten times the value of the mark before it",
                         "correct": True},
            {"text": "one more than the value of the mark before it",
                         "correct": False,
                         "why": "The marks multiply rather than simply add one each time — that is why the "
                    "chart can fit numbers spanning a few hertz up to a few hundred thousand."},
            {"text": "exactly the same value as every other mark on the chart",
                         "correct": False,
                         "why": "If every mark were the same value the chart could show no range of "
                    "frequencies at all."},
            {"text": "half the value of the mark before it",
                         "correct": False,
                         "why": "The chart's marks multiply upward by ten each time, not halve."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e26",
        "band": "easier",
        "text": "A cinema installs speakers built to reproduce audible sound faithfully. What "
                "range of frequencies would they mainly need to cover?",
        "options": [
            {"text": "roughly 20 Hz to 20 000 Hz",
                         "correct": True},
            {"text": "roughly 20 000 Hz to 200 000 Hz",
                         "correct": False,
                         "why": "That whole band lies above the human range, in ultrasound, so it would be "
                    "wasted on a listener's ears."},
            {"text": "roughly 2 Hz to 20 Hz",
                         "correct": False,
                         "why": "That band lies below the human range, in infrasound, and would mostly go "
                    "unheard."},
            {"text": "exactly one single frequency, since all sounds share the same pitch",
                         "correct": False,
                         "why": "Real sounds cover a wide spread of frequencies, not a single pitch, which is "
                    "why speakers need to reproduce a whole band."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e27",
        "band": "easier",
        "text": "A vet measures a rabbit's auditory range and finds it reaches well above 20 "
                "000 Hz at the top. Compared with a person's range, the rabbit's top is…",
        "options": [
            {"text": "lower than a person's",
                         "correct": False,
                         "why": "A top above 20 000 Hz is higher than the human top of about 20 000 Hz, not "
                    "lower."},
            {"text": "higher than a person's",
                         "correct": True},
            {"text": "exactly the same as a person's",
                         "correct": False,
                         "why": "A top above 20 000 Hz is higher than the human figure of about 20 000 Hz, so "
                    "the two are not the same."},
            {"text": "impossible to compare without knowing the rabbit's loudness",
                         "correct": False,
                         "why": "Comparing the top of two ranges only needs the two frequency values; "
                    "loudness does not come into it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e28",
        "band": "easier",
        "text": "Which of these best describes what infrasound and ultrasound have in common?",
        "options": [
            {"text": "Both are silent even to a microphone",
                         "correct": False,
                         "why": "A microphone registers both perfectly well; they are ordinary sound, only "
                    "outside the human range."},
            {"text": "Both obey the ordinary rules of sound, and are simply outside the human "
                     "range",
                         "correct": True},
            {"text": "Both travel without needing any material to move through",
                         "correct": False,
                         "why": "Like any other sound, both need a material such as air, water or a solid to "
                    "travel through."},
            {"text": "Both are exclusively made by animals rather than by machines",
                         "correct": False,
                         "why": "Machines readily produce both — a dog whistle makes ultrasound and some "
                    "industrial equipment makes infrasound."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e29",
        "band": "easier",
        "text": "A young child and their grandparent both stand next to a device making a "
                "steady 15 000 Hz tone. Based on how hearing ranges typically change with "
                "age, who is more likely to hear it clearly?",
        "options": [
            {"text": "The grandparent, since older ears are generally more sensitive overall",
                         "correct": False,
                         "why": "Age-related loss typically removes the TOP of the range first, which makes a "
                    "high tone like this one harder, not easier, for an older ear to hear."},
            {"text": "The child, since the top of the range typically falls with age",
                         "correct": True},
            {"text": "Neither, since 15 000 Hz is above the top of every human's range at any age",
                         "correct": False,
                         "why": "15 000 Hz sits below the usual young-adult top of about 20 000 Hz, so a "
                    "young ear can typically hear it."},
            {"text": "Both equally, since age has no effect on hearing range at all",
                         "correct": False,
                         "why": "The top of the human range typically falls with age, so the two are not "
                    "equally likely to hear a high tone like this."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-e30",
        "band": "easier",
        "text": "Which pair correctly matches an animal with roughly where the TOP of its "
                "auditory range sits?",
        "options": [
            {"text": "Bat — about 110 000 Hz",
                         "correct": True},
            {"text": "Elephant — about 110 000 Hz",
                         "correct": False,
                         "why": "110 000 Hz is close to the bat's top frequency; an elephant's range tops out "
                    "far lower, around 12 000 Hz."},
            {"text": "Dog — about 110 000 Hz",
                         "correct": False,
                         "why": "A dog's range tops out at about 45 000 Hz, well below 110 000 Hz."},
            {"text": "Human — about 110 000 Hz",
                         "correct": False,
                         "why": "A healthy young human's range tops out at about 20 000 Hz, nowhere near 110 "
                    "000 Hz."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s06",
        "band": "standard",
        "text": "A vet says a rabbit's range tops out somewhat higher than a human's. On the "
                "usual multiplying chart, would that show as a small step to the right or a "
                "very large one?",
        "options": [
            {"text": "A very large step, because any difference at all between two animals always "
                     "shows as a huge jump on this kind of chart",
                         "correct": False,
                         "why": "How big the step looks depends on how many times higher the second value is, "
                    "not simply on whether there is a difference."},
            {"text": "A small step, since the chart shrinks large differences down until they "
                     "barely show at all",
                         "correct": False,
                         "why": "The chart does the opposite — it stretches out a huge range of values, so "
                    "even a modest multiple shows as a visible step."},
            {"text": "A small step, because a top only somewhat higher represents a fairly small "
                     "multiple of the human figure",
                         "correct": True},
            {"text": "There is no way to tell without measuring the rabbit's range in millimetres "
                     "of chart width",
                         "correct": False,
                         "why": "The size of the step is decided by the ratio between the two frequencies, "
                    "which can be reasoned out without a ruler."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s07",
        "band": "standard",
        "text": "A dog's range starts at about 67 Hz and a cat's starts at about 45 Hz. What "
                "does that difference suggest about the bottom of the two ranges?",
        "options": [
            {"text": "The dog's range reaches slightly lower at the bottom than the cat's does",
                         "correct": False,
                         "why": "67 Hz is a higher starting point than 45 Hz, so the dog's bottom is higher, "
                    "not lower, than the cat's."},
            {"text": "The cat's range reaches slightly lower at the bottom than the dog's does",
                         "correct": True},
            {"text": "The two bottoms are effectively identical, since both are well under 100 Hz",
                         "correct": False,
                         "why": "45 Hz and 67 Hz are two distinctly different starting points, even though "
                    "both happen to be under 100 Hz."},
            {"text": "Neither figure tells us anything about the bottom of a range, only about its "
                     "top",
                         "correct": False,
                         "why": "Both 67 Hz and 45 Hz are given as the lowest frequency each animal can hear "
                    "— that is exactly the bottom of the range."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s08",
        "band": "standard",
        "text": "A device is built to emit a steady tone at 50 Hz. Explain why a young human "
                "and an elephant nearby would both hear it, while a dog standing just as "
                "close would not.",
        "options": [
            {"text": "Dogs simply cannot hear tones from mechanical devices of any kind, only "
                     "tones actually made by other living, breathing animals, never from a machine "
                     "of any sort",
                         "correct": False,
                         "why": "A dog's hearing responds to any sound wave within its range, whether it "
                    "comes from a device or an animal; the source is not the issue here."},
            {"text": "50 Hz falls inside the human and elephant ranges, but it is below the bottom "
                     "of a dog's range, which starts higher, at about 67 Hz",
                         "correct": True},
            {"text": "50 Hz is far too quiet a tone for any animal in the room to hear, the human and the elephant included, whatever their ranges happen to be",
                         "correct": False,
                         "why": "The question is about whether the frequency falls within a range, not about "
                    "loudness, and the human and elephant are both said to hear it."},
            {"text": "A dog's range simply does not include any frequency below 200 Hz",
                         "correct": False,
                         "why": "A dog's range starts at about 67 Hz, not 200 Hz, though 50 Hz still falls "
                    "below that lower figure."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s09",
        "band": "standard",
        "text": "A tone at 95 000 Hz is sounded near a bat and a mouse. Explain who, if "
                "anyone, would hear it.",
        "options": [
            {"text": "Neither — 95 000 Hz is above the top of both the bat's range, at about 110 "
                     "000 Hz, and the mouse's, at about 91 000 Hz",
                         "correct": False,
                         "why": "95 000 Hz is below the bat's top of about 110 000 Hz, so the bat's range "
                    "does include it."},
            {"text": "The bat only, since 95 000 Hz sits below its top of about 110 000 Hz but "
                     "above the mouse's top of about 91 000 Hz",
                         "correct": True},
            {"text": "The mouse only, since a mouse is more sensitive to very high frequencies than a bat is, and a bat's own range stops short of 95 000 Hz",
                         "correct": False,
                         "why": "The mouse's range is described as topping out at about 91 000 Hz, below the "
                    "95 000 Hz tone; the bat's higher top does include it."},
            {"text": "Both, since 95 000 Hz is comfortably inside both of their ranges",
                         "correct": False,
                         "why": "95 000 Hz is above the mouse's top of about 91 000 Hz, so it falls outside "
                    "the mouse's range."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s10",
        "band": "standard",
        "text": "An elephant and a bat both give up part of the ordinary human range compared "
                "with a young person. Compare what each one gives up.",
        "options": [
            {"text": "Both give up exactly the same part of the human range, the very top above 20 000 Hz, and neither of them reaches any lower at the bottom than a person does",
                         "correct": False,
                         "why": "The elephant's range does not reach anywhere near 20 000 Hz at all; it is "
                    "the bat, not the elephant, that reaches well past that figure."},
            {"text": "The elephant gives up the top, reaching only about 12 000 Hz, while the bat "
                     "gives up the bottom, starting at about 2000 Hz",
                         "correct": True},
            {"text": "The elephant gives up the bottom, while the bat gives up the top",
                         "correct": False,
                         "why": "It is the other way round: the elephant reaches lower than a human at the "
                    "bottom but not higher at the top, and the bat reaches higher at the top but "
                    "not lower at the bottom."},
            {"text": "Neither animal gives up any part of the human range at all — both of them "
                     "simply add a stretch of extra range on top of what a human already has",
                         "correct": False,
                         "why": "The elephant's top, at about 12 000 Hz, is lower than a human's top of about "
                    "20 000 Hz, so it has given up part of the range rather than only adding to "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s11",
        "band": "standard",
        "text": "A chart of animal auditory ranges shades the human band behind "
                "every row. Why is that more useful than just listing the numbers "
                "in a table?",
        "options": [
            {"text": "Because a plain table of numbers cannot represent a frequency at all, and only a shaded chart is able to carry frequency values in the first place",
                         "correct": False,
                         "why": "A table could list every figure perfectly well; the shading is there to make "
                    "comparisons easier to see, not because numbers alone are impossible."},
            {"text": "Because the shaded band shows exactly how loud each animal's calls are",
                         "correct": False,
                         "why": "The shading marks a range of frequencies, the human band, not a measure of "
                    "loudness."},
            {"text": "So a reader can see at a glance which parts of each animal's range fall "
                     "inside, above or below the human band",
                         "correct": True},
            {"text": "So that infrasound and ultrasound can be coloured in completely different "
                     "colours from each other",
                         "correct": False,
                         "why": "The chart's purpose is to mark the human band for comparison; colouring "
                    "infrasound and ultrasound differently is not what the shading is for."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s12",
        "band": "standard",
        "text": "A hearing specialist says a patient's top frequency has "
                "fallen from about 18 000 Hz to about 9000 Hz over "
                "several years. Explain roughly what has happened on a "
                "multiplying chart, where each mark means ten times the "
                "one before it.",
        "options": [
            {"text": "The whole band has shifted left by exactly one full decade mark, since every measurable fall in a person's hearing works out at a factor of ten on a chart of this kind",
                         "correct": False,
                         "why": "A factor of ten would take 18 000 Hz down to 1800 Hz, not to 9000 Hz; the "
                    "real fall here is roughly a factor of two."},
            {"text": "The bottom of the patient's band has also fallen by the same amount as the "
                     "top",
                         "correct": False,
                         "why": "Age-related loss typically leaves the bottom of the range almost unchanged; "
                    "it is the top that moves."},
            {"text": "The top of the patient's band has moved left by well under one whole mark, "
                     "since 9000 Hz is about half of 18 000 Hz rather than a tenth of it",
                         "correct": True},
            {"text": "Nothing meaningful has changed on the chart at all, since both of those figures still sit comfortably above the bottom of the human range and inside it",
                         "correct": False,
                         "why": "Losing half of the top frequency is a real and noticeable narrowing of the "
                    "range, even though both figures remain above the bottom."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s13",
        "band": "standard",
        "text": "Why might a teenager and their grandparent disagree about whether a "
                "particular high-pitched device noise is annoying?",
        "options": [
            {"text": "Older people always find high-pitched sounds more annoying than younger "
                     "people do",
                         "correct": False,
                         "why": "The lesson describes the TOP of the range falling with age, which would make "
                    "a high sound LESS noticeable to an older listener, not more annoying."},
            {"text": "Teenagers cannot hear low-pitched sounds, which is why the disagreement "
                     "happens",
                         "correct": False,
                         "why": "The bottom of the range barely changes with age; the disagreement described "
                    "here is about a high-pitched sound, not a low one."},
            {"text": "The grandparent may simply not be able to hear it, since the top of the "
                     "hearing range typically falls with age",
                         "correct": True},
            {"text": "Hearing range has nothing to do with it — the disagreement must be about "
                     "personal taste alone",
                         "correct": False,
                         "why": "A real physical difference in what each person can hear is a reasonable "
                    "explanation here, given how the top of the range changes with age."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s14",
        "band": "standard",
        "text": "Someone claims that turning up the volume on a pair of headphones can never "
                "cause permanent hearing damage. Evaluate this claim.",
        "options": [
            {"text": "The claim is right, since any damage caused by loud sound always heals "
                     "itself completely within just a few days of quiet rest, without any lasting "
                     "effect",
                         "correct": False,
                         "why": "The relevant hair cells do not grow back in humans, so damage from loud "
                    "sound is lasting, not something that heals within days."},
            {"text": "The claim is right, since headphones are too quiet to ever reach a damaging "
                     "volume",
                         "correct": False,
                         "why": "Headphones are perfectly capable of reaching volumes loud enough to damage "
                    "hearing, which is exactly why a volume limit is recommended."},
            {"text": "The claim is wrong — loud sound can permanently damage the hair cells that "
                     "respond to high frequencies, and they do not regrow in humans",
                         "correct": True},
            {"text": "The claim cannot possibly be evaluated without knowing the exact make and "
                     "model of headphones being used in each individual case, and the volume "
                     "setting too",
                         "correct": False,
                         "why": "The underlying science — that loud sound can permanently damage hair cells "
                    "that do not regrow — does not depend on which particular headphones are "
                    "used."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s15",
        "band": "standard",
        "text": "Explain why the hair cells that respond to the HIGHEST frequencies are "
                "usually the first to be damaged by loud sound.",
        "options": [
            {"text": "They are simply more fragile than the ear's other hair cells, for reasons "
                     "that have nothing to do with where in the ear they happen to sit",
                         "correct": False,
                         "why": "There is a structural reason — their position nearest the entrance — rather than any unexplained fragility."},
            {"text": "High frequencies are always a good deal louder than low frequencies of the same kind, so they do far more damage to a hair cell on arrival",
                         "correct": False,
                         "why": "Loudness is a separate property from frequency; a high note is not "
                    "automatically louder than a low one."},
            {"text": "They are located deepest inside the ear, furthest from where sound enters",
                         "correct": False,
                         "why": "It is the opposite — the cells that respond to the highest frequencies sit "
                    "nearest the entrance, which is why they take the most punishment."},
            {"text": "They sit nearest the entrance of the inner ear, so they take the most "
                     "punishment from sound arriving from outside",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s16",
        "band": "standard",
        "text": "Explain why elephants communicating over several kilometres use very low "
                "rumbles rather than higher-pitched calls.",
        "options": [
            {"text": "Low frequencies always sound louder to a distant listener than high "
                     "frequencies of the same original loudness",
                         "correct": False,
                         "why": "The advantage described is about how much of the signal survives the journey "
                    "through absorption, not about the pitch itself sounding louder."},
            {"text": "Higher-pitched calls would be heard by predators, while low rumbles are "
                     "silent to other animals",
                         "correct": False,
                         "why": "Low rumbles are still real, audible sound to any ear within range; they are "
                    "not silent to other animals."},
            {"text": "An elephant's vocal organs are physically unable to produce any frequency "
                     "above about 100 Hz",
                         "correct": False,
                         "why": "The lesson describes elephants choosing low rumbles for how far they carry, "
                    "not because elephants are incapable of any higher sound."},
            {"text": "Low frequencies are absorbed less by open ground as they travel, so more of "
                     "the signal survives over a long distance",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s17",
        "band": "standard",
        "text": "A student says that because a blue whale's calls are below 20 Hz, they must "
                "be silent and undetectable. Evaluate this claim.",
        "options": [
            {"text": "The claim is right, since nothing below 20 Hz can ever be detected by any "
                     "instrument built by humans, however sensitive it is",
                         "correct": False,
                         "why": "Instruments built to detect infrasound can and do record these calls; the 20 "
                    "Hz figure is a limit of human hearing, not of detection in general."},
            {"text": "The claim is right, since infrasound carries no energy at all",
                         "correct": False,
                         "why": "Infrasound is ordinary sound in every physical respect and does carry "
                    "energy; it is simply below the human hearing range."},
            {"text": "The claim cannot be judged at all without first knowing exactly how far away "
                     "from the whale the listener happens to be standing",
                         "correct": False,
                         "why": "Whether the sound is detectable at all does not depend on distance; the "
                    "calls are real and recordable, only inaudible to human ears."},
            {"text": "The claim is wrong — the calls are real sound, recordable with the right "
                     "equipment; they are only silent to human ears",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s18",
        "band": "standard",
        "text": "A manufacturer claims their new ultrasonic pest deterrent produces \"a "
                "completely different kind of sound wave\" from ordinary noise. Evaluate this "
                "claim.",
        "options": [
            {"text": "The claim is accurate, since ultrasound needs no material at all to travel "
                     "through, quite unlike an ordinary sound wave in air",
                         "correct": False,
                         "why": "Ultrasound needs a material to travel through, exactly like any other sound; "
                    "that is not a difference between the two."},
            {"text": "The claim is accurate, since ultrasound travels far faster than ordinary "
                     "sound in the same air",
                         "correct": False,
                         "why": "Every frequency of sound travels at the same speed through the same air; "
                    "ultrasound is not faster."},
            {"text": "The claim cannot be checked without testing the device directly",
                         "correct": False,
                         "why": "The underlying physics — that ultrasound is ordinary sound above the human "
                    "range — applies regardless of which particular device is being sold."},
            {"text": "The claim is misleading — ultrasound is ordinary sound above the top of the "
                     "human range, not a different kind of wave",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s19",
        "band": "standard",
        "text": "A 40 000 Hz tone is sounded in a room holding a cat and a mouse. Who hears "
                "it?",
        "options": [
            {"text": "Neither, since 40 000 Hz is above the top of both the cat's and the mouse's "
                     "ranges",
                         "correct": False,
                         "why": "40 000 Hz sits below the cat's top of about 64 000 Hz, so the cat's range "
                    "does include it."},
            {"text": "The cat only, since a mouse's hearing is usually said to stop well short of "
                     "40 000 Hz",
                         "correct": False,
                         "why": "A mouse's range runs up to about 91 000 Hz, well past 40 000 Hz, so the "
                    "mouse's range does include it too."},
            {"text": "The mouse only, since a mouse is a good deal more sensitive than a cat to very high frequencies, and 40 000 Hz sits above where a cat stops hearing",
                         "correct": False,
                         "why": "The cat's top of about 64 000 Hz also comfortably includes 40 000 Hz, so the "
                    "cat hears it as well."},
            {"text": "Both, since 40 000 Hz falls inside the cat's range of about 45 to 64 000 Hz "
                     "and the mouse's range of about 1000 to 91 000 Hz",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s20",
        "band": "standard",
        "text": "A student argues that since a dog's range starts higher than a human's, a "
                "dog must be worse at hearing low sounds in general. Evaluate this argument.",
        "options": [
            {"text": "The argument is right, and it also means a dog's overall range must be "
                     "narrower than a human's, once both ends are properly compared",
                         "correct": False,
                         "why": "A dog's range is not narrower overall — it reaches far higher at the top "
                    "than a human's does, even though it starts higher at the bottom."},
            {"text": "The argument is reasonable for the bottom of the range, but says nothing "
                     "about the top, where a dog actually hears higher than a human",
                         "correct": True},
            {"text": "The argument is wrong, since a dog's range starts lower than a human's, not "
                     "higher",
                         "correct": False,
                         "why": "A dog's range starts at about 67 Hz, higher than the human figure of about "
                    "20 Hz, so the starting comparison in the argument is correct."},
            {"text": "The argument cannot really be judged, since loudness and auditory range are "
                     "exactly the same physical property under two different names",
                         "correct": False,
                         "why": "Loudness and auditory range are different properties — one is about how big "
                    "a vibration is, the other about which frequencies an ear can respond to at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s21",
        "band": "standard",
        "text": "Explain why a chart of auditory ranges drawn on a straight, evenly-spaced "
                "axis (rather than a multiplying one) would make the human, elephant and dog "
                "ranges hard to tell apart.",
        "options": [
            {"text": "Because a straight, evenly-spaced axis cannot represent frequency at all in "
                     "any form, and only a multiplying axis of the kind normally drawn for hearing ranges can show frequency values correctly",
                         "correct": False,
                         "why": "A straight axis can represent frequency perfectly well; the trouble is only "
                    "that it spreads the huge range of values unevenly across the page."},
            {"text": "Because those three particular animals — the human, the elephant and the dog "
                     "— all happen to hear at exactly the same single frequency as one another, "
                     "which is why their bars would overlap completely",
                         "correct": False,
                         "why": "The three ranges differ meaningfully from one another; the problem with a "
                    "straight axis is how it displays a wide spread of values, not that the "
                    "values are identical."},
            {"text": "Because a straight, evenly-spaced axis always reverses the left-to-right "
                     "order of the animals compared with how a multiplying axis would normally arrange them",
                         "correct": False,
                         "why": "The order of the animals along the axis would stay the same either way; what "
                    "changes is how much space each one takes up."},
            {"text": "Because those three ranges sit relatively close together compared with the "
                     "full span up to a bat's, so they would be squeezed into a small part of a "
                     "straight axis stretching to over 100 000 Hz",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s22",
        "band": "standard",
        "text": "A hearing-aid maker builds a device that only amplifies frequencies above "
                "4000 Hz. Suggest why this might help someone whose top range has fallen with "
                "age, more than simply making everything louder would.",
        "options": [
            {"text": "Because the frequencies that make consonants distinct sit mostly above 4000 "
                     "Hz, and those are the ones typically lost first",
                         "correct": True},
            {"text": "Because amplifying only high frequencies always makes speech quieter "
                     "overall, which is more comfortable to listen to",
                         "correct": False,
                         "why": "The aim of a hearing aid is to make relevant sounds more audible, not "
                    "quieter; the reasoning here is about which frequencies carry the missing "
                    "information."},
            {"text": "Because low frequencies below 4000 Hz have already completely disappeared "
                     "for everyone over a certain age",
                         "correct": False,
                         "why": "Low frequencies are typically the ones that survive best with age; it is the "
                    "high frequencies that are usually lost first."},
            {"text": "Because amplifying any single narrow band works equally well whichever "
                     "frequencies happen to be chosen",
                         "correct": False,
                         "why": "The choice of band matters here — frequencies above 4000 Hz specifically "
                    "carry the information that makes consonants distinct."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s23",
        "band": "standard",
        "text": "A wildlife recordist wants to capture both an elephant's rumble and a bat's "
                "call on the same microphone. Explain the challenge this presents.",
        "options": [
            {"text": "The two sounds sit at opposite extremes of the frequency scale, so the "
                     "microphone needs to respond well right across an unusually wide band",
                         "correct": True},
            {"text": "Elephants and bats never make sound at the same time of day, so a single "
                     "recording is impossible regardless of the microphone",
                         "correct": False,
                         "why": "The challenge described is about frequency range, not about the animals' "
                    "timing."},
            {"text": "The two sounds are actually at very similar frequencies, so an ordinary "
                     "microphone would manage perfectly well",
                         "correct": False,
                         "why": "An elephant's rumble and a bat's call sit at opposite ends of the frequency "
                    "scale, nowhere near similar."},
            {"text": "Only one of the two sounds is real sound; the other is simply too quiet to "
                     "exist",
                         "correct": False,
                         "why": "Both an elephant's rumble and a bat's call are real sound; the challenge is "
                    "the wide spread of frequencies, not one of them not existing."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s24",
        "band": "standard",
        "text": "A class finds the top of each person's hearing by playing a tone "
                "through a speaker and slowly raising its frequency until each "
                "person stops hearing it. Suggest why the volume must be held "
                "steady all the way through the test.",
        "options": [
            {"text": "So that frequency is the only thing being changed — a tone growing "
                     "louder as it rose could still be noticed past the frequency that is "
                     "really that person's limit",
                         "correct": True},
            {"text": "So that the loudspeaker sends out exactly the same frequency to every person in the room at once, which a volume changing part-way through the test would otherwise pull out of step",
                         "correct": False,
                         "why": "The frequency is deliberately being changed during the test; it is the "
                    "volume that has to be held steady, and volume does not alter it."},
            {"text": "So that the tone travels through the air at the same speed for every "
                     "person in the room, rather than reaching some of them sooner",
                         "correct": False,
                         "why": "Sound travels at the same speed through the same air whatever its "
                    "volume, so holding the volume steady has nothing to do with speed."},
            {"text": "Because a loudspeaker is physically unable to change its volume and "
                     "its frequency at the same moment as one another",
                         "correct": False,
                         "why": "A loudspeaker can change both at once perfectly well; the volume is held "
                    "steady on purpose, to leave frequency as the only variable."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s25",
        "band": "standard",
        "text": "A dolphin's clicks reach well above 100 000 Hz, similar to a bat's calls. "
                "Suggest what this similarity is most likely to be for, given what a very high frequency is generally useful for.",
        "options": [
            {"text": "Detecting small objects or prey, since both animals rely on echoes from very "
                     "high-frequency calls to sense their surroundings",
                         "correct": True},
            {"text": "Making the loudest possible sound, since higher frequencies are always "
                     "louder than lower ones",
                         "correct": False,
                         "why": "Frequency and loudness are separate properties; a high-pitched click is not "
                    "automatically the loudest kind of sound."},
            {"text": "Communicating over the longest possible distance, since higher frequencies "
                     "always carry furthest",
                         "correct": False,
                         "why": "It is LOW frequencies, not high ones, that carry furthest through open air or water, because less of them is absorbed on the way."},
            {"text": "Avoiding detection by other animals, since sound above 100 000 Hz cannot "
                     "possibly be heard by any creature at all, however good its hearing is",
                         "correct": False,
                         "why": "Other animals with very high ranges, such as bats, mice and dolphins "
                    "themselves, can and do hear well above 100 000 Hz."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s26",
        "band": "standard",
        "text": "A cat hears from about 45 Hz up to about 64 000 Hz, and a bat from "
                "about 2000 Hz up to about 110 000 Hz. Which tone would BOTH "
                "definitely hear: one at 1000 Hz, or one at 40 000 Hz?",
        "options": [
            {"text": "The 1000 Hz tone, since the lower of two tones is the easier one for "
                     "any animal to pick up",
                         "correct": False,
                         "why": "A bat's hearing starts at about 2000 Hz, above 1000 Hz, so a bat would "
                    "not pick up that tone at all."},
            {"text": "The 40 000 Hz tone, since it sits inside the cat's hearing and inside "
                     "the bat's",
                         "correct": True},
            {"text": "Both tones equally, since frequency does not affect which animal can hear a "
                     "sound",
                         "correct": False,
                         "why": "Frequency is exactly what decides whether a tone falls inside or outside an "
                    "animal's range."},
            {"text": "Neither tone, since each one falls outside at least one of the two "
                     "animals' hearing",
                         "correct": False,
                         "why": "40 000 Hz sits comfortably inside the cat's hearing and inside the bat's, "
                    "so both animals pick that one up."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s27",
        "band": "standard",
        "text": "A student says infrasound and ultrasound are exact opposites of each other, "
                "like hot and cold. Evaluate this claim.",
        "options": [
            {"text": "The claim overstates it — both are simply ordinary sound outside the human "
                     "range, one below and one above, not a special opposite pair of waves",
                         "correct": True},
            {"text": "The claim is exactly right, since ultrasound always travels through solids "
                     "while infrasound can only travel through air",
                         "correct": False,
                         "why": "Both kinds of sound can travel through air, water or solids, just like any "
                    "audible sound; neither is restricted to one kind of material."},
            {"text": "The claim is exactly right, since ultrasound genuinely carries real energy "
                     "while infrasound carries none whatsoever, in any situation at all, indoors "
                     "or outdoors",
                         "correct": False,
                         "why": "Both ultrasound and infrasound carry energy, exactly as any ordinary sound "
                    "does."},
            {"text": "The claim cannot be judged at all, since infrasound and ultrasound have "
                     "never once both been measured together in the very same experiment, under "
                     "laboratory conditions",
                         "correct": False,
                         "why": "Both have been measured many times over, in animals and with instruments, "
                    "and can be compared directly."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s28",
        "band": "standard",
        "text": "On a multiplying chart, where each mark means ten times the one before it, "
                "which shifts a bar's end further to the right: doubling a frequency of 1000 "
                "Hz, or doubling a frequency of 50 000 Hz?",
        "options": [
            {"text": "Doubling the 50 000 Hz frequency, since it starts from a much bigger number "
                     "to begin with, and bigger starting numbers always move further on a chart "
                     "like this one",
                         "correct": False,
                         "why": "On a multiplying scale, the size of the shift depends on the ratio, "
                    "doubling, not on the starting number itself."},
            {"text": "Doubling the 1000 Hz frequency, since smaller starting numbers are always "
                     "the ones that move further along on this particular kind of multiplying "
                     "chart",
                         "correct": False,
                         "why": "It is the ratio between the two values, not which one is smaller, that "
                    "decides how far a bar moves on a multiplying chart."},
            {"text": "Both shifts move the bar's end the same distance to the right, since "
                     "doubling is the same ratio whichever frequency you start from",
                         "correct": True},
            {"text": "Neither shift moves the bar at all in either direction, since doubling a "
                     "frequency apparently does not change where it sits on this kind of "
                     "multiplying chart",
                         "correct": False,
                         "why": "Doubling a frequency does move its position on the chart; what stays the "
                    "same between the two cases is how far it moves, not whether it moves."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s29",
        "band": "standard",
        "text": "A warehouse fits an ultrasonic mouse repeller at 40 000 Hz and the "
                "staff report hearing nothing at all from it. Explain how the device "
                "can be reaching the mice while adding no noise for the staff.",
        "options": [
            {"text": "It sends out a real sound wave above the top of the human range but "
                     "well inside a mouse's, so the mice are exposed to a genuine tone",
                         "correct": True},
            {"text": "It sends out no sound wave at all; the mice are disturbed by the "
                     "moving air the device pushes out instead",
                         "correct": False,
                         "why": "A microphone set up beside the device records a genuine steady tone; it "
                    "is a real sound wave, not simply moving air."},
            {"text": "It sends out a beam of light invisible to human eyes, and it is this "
                     "light that the mice are able to see in the dark of the warehouse",
                         "correct": False,
                         "why": "The device is described as ultrasonic, so it makes sound; there is no "
                    "light involved in how it reaches the mice."},
            {"text": "It is not silent at all — the tone is simply far too faint for any "
                     "instrument in the warehouse to record, however close it is held",
                         "correct": False,
                         "why": "A microphone records the tone readily; it is a normal-strength sound "
                    "wave that happens to sit above the human hearing range."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-s30",
        "band": "standard",
        "text": "Both elephants and blue whales rely on very low, infrasonic calls for "
                "long-distance communication, one through open ground and the other through "
                "open ocean. What do the two situations have in common?",
        "options": [
            {"text": "In both, low frequencies are absorbed less than high ones over a long "
                     "distance, letting the signal carry further",
                         "correct": True},
            {"text": "In both cases, the animals involved are simply far louder overall than any "
                     "other animal found anywhere on the whole of Earth",
                         "correct": False,
                         "why": "The advantage described here comes from how well low frequencies travel, not "
                    "from either animal being the loudest overall."},
            {"text": "In both cases, sound is simply unable to travel at all through open ground "
                     "or open ocean once its frequency rises above about 20 Hz",
                         "correct": False,
                         "why": "Higher frequencies still travel through both ground and ocean; they are "
                    "simply absorbed more over the same distance than low frequencies are."},
            {"text": "In both cases, the low frequency itself changes into an entirely different "
                     "kind of wave altogether once it actually leaves the animal making it",
                         "correct": False,
                         "why": "The call remains an ordinary sound wave throughout its journey; nothing "
                    "about it changes into a different kind of wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h06",
        "band": "harder",
        "text": "A student notices a bat's bar ends about halfway between the left edge of "
                "the chart and where a mouse's bar ends, and concludes the bat's top "
                "frequency must be about half the mouse's. Evaluate this reasoning.",
        "options": [
            {"text": "The reasoning is wrong — equal distances along a multiplying axis represent "
                     "equal ratios, not equal fractions of the values themselves, so sitting "
                     "halfway along does not mean half the value",
                         "correct": True},
            {"text": "The reasoning is right, since halfway along any axis means half of the value "
                     "that sits at the far end",
                         "correct": False,
                         "why": "That rule holds on a straight, evenly-spaced axis, but this chart multiplies "
                    "along its length instead of adding, so halfway along means something "
                    "different."},
            {"text": "The reasoning is right, but only because bats and mice happen to be "
                     "similar-sized animals",
                         "correct": False,
                         "why": "The size of the two animals has no bearing on how positions along a "
                    "multiplying chart relate to actual frequency values."},
            {"text": "The reasoning cannot be judged without first measuring the chart with a "
                     "ruler in millimetres",
                         "correct": False,
                         "why": "The flaw here is about what kind of axis is being read, a multiplying one "
                    "rather than a straight one, which can be reasoned about without measuring "
                    "anything."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h07",
        "band": "harder",
        "text": "A hearing-aid designer boosts every frequency below 500 Hz for a patient "
                "whose top range has fallen from 18 000 Hz to 8000 Hz with age. Evaluate "
                "whether this choice is likely to restore the missing consonant sounds in "
                "speech.",
        "options": [
            {"text": "Very likely to help, since boosting any part of the frequency range restores "
                     "what has been lost elsewhere in that range",
                         "correct": False,
                         "why": "Boosting one band of frequencies does not restore information carried in a "
                    "completely different, higher band that the patient can no longer hear at "
                    "all."},
            {"text": "Unlikely to help much, since the frequencies that carry the consonants sit well above 500 Hz, closer to 4000 Hz and beyond",
                         "correct": True},
            {"text": "Very likely to help, since the missing information in speech is mostly "
                     "carried below 500 Hz in any speaker's voice",
                         "correct": False,
                         "why": "The frequencies that separate one consonant from another sit mostly above 4000 Hz, not below 500 Hz."},
            {"text": "Impossible to judge without knowing the exact brand of hearing aid being "
                     "fitted",
                         "correct": False,
                         "why": "The relevant fact is which BAND of frequencies is being boosted, and whether "
                    "that matches where the missing information actually sits — the brand of aid "
                    "does not change that."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h08",
        "band": "harder",
        "text": "An elephant's range runs from about 16 Hz to 12 000 Hz, and a bat's from "
                "about 2000 Hz to 110 000 Hz. Working roughly in powers of ten, which "
                "animal's range actually spans MORE decades of frequency, top to bottom?",
        "options": [
            {"text": "The bat's — its top frequency of 110 000 Hz is far higher than the "
                     "elephant's 12 000 Hz, so its span must cover more decades too",
                         "correct": False,
                         "why": "A higher top on its own does not decide the number of decades spanned — the "
                    "bat's range also starts far higher, at 2000 Hz rather than 16 Hz, which "
                    "narrows its span considerably."},
            {"text": "They span exactly the same number of decades, since both ranges are "
                     "described using the same kind of multiplying chart",
                         "correct": False,
                         "why": "Using the same kind of chart to display two ranges does not make their "
                    "actual spans equal; the two spans here work out noticeably different."},
            {"text": "The elephant's — 16 to 12 000 Hz is close to three decades, while 2000 to "
                     "110 000 Hz for the bat is under two",
                         "correct": True},
            {"text": "Neither spans a whole number of decades, so the comparison cannot really be "
                     "made at all",
                         "correct": False,
                         "why": "A span does not need to be a whole number of decades for two spans to be "
                    "compared — one can still be bigger or smaller than the other."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h09",
        "band": "harder",
        "text": "A mouse's range starts at about 1000 Hz, and a bat's starts at about 2000 "
                "Hz. Is it possible for a mouse to hear a genuine sound that a nearby bat "
                "cannot, using these figures?",
        "options": [
            {"text": "No — a bat's range includes everything a mouse's range includes, since a "
                     "bat's top frequency is so much higher",
                         "correct": False,
                         "why": "A higher top does not guarantee a lower bottom — the bat's range actually "
                    "starts higher than the mouse's, leaving a gap the mouse alone can hear."},
            {"text": "No — mice and bats share exactly the same range of frequencies, regardless "
                     "of the figures given",
                         "correct": False,
                         "why": "The two ranges given here are clearly different, both at the bottom and at "
                    "the top, so they are not the same range."},
            {"text": "It is impossible to say without first measuring how loud the tone is",
                         "correct": False,
                         "why": "Whether a frequency falls inside a range does not depend on loudness; it "
                    "depends only on the frequency itself compared with the range's limits."},
            {"text": "Yes — a tone at, say, 1500 Hz falls inside the mouse's range but below the "
                     "bottom of the bat's",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h10",
        "band": "harder",
        "text": "Explain why sending a very low-frequency SOUND signal would be a poor way to "
                "communicate instantly with someone on the other side of the world, even "
                "though low frequencies travel unusually far.",
        "options": [
            {"text": "Sound of any frequency travels at only a few hundred metres per second and "
                     "needs a continuous material to carry it, so it would take far too long and "
                     "could not cross open space",
                         "correct": True},
            {"text": "Low frequencies cannot travel through air at all over such enormous "
                     "distances",
                         "correct": False,
                         "why": "Low frequencies are described as travelling further than high ones precisely "
                    "because they are absorbed less; the real limit here is their speed and their "
                    "need for a material, not an inability to travel through air."},
            {"text": "Low-frequency sound instantly turns into ultrasound once it has travelled "
                     "far enough, but instead arrives as something else entirely different from a "
                     "rumble",
                         "correct": False,
                         "why": "A sound's frequency does not change as it travels; a low rumble stays a low "
                    "rumble however far it goes."},
            {"text": "Low frequencies are always too quiet to be detected once they leave the "
                     "source",
                         "correct": False,
                         "why": "Loudness on arrival depends on how the signal is produced and how much is "
                    "absorbed, not on some fixed rule that low frequencies always end up too "
                    "quiet."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h11",
        "band": "harder",
        "text": "Someone argues that because a bat's range covers fewer decades than an "
                "elephant's, an elephant must have 'better' hearing overall. Evaluate this "
                "argument.",
        "options": [
            {"text": "The argument is sound, since a wider span in decades means more sensitive "
                     "hearing throughout it, not merely at some of it",
                         "correct": False,
                         "why": "A range only says which frequencies an ear responds to; sensitivity within "
                    "that range is a separate matter this lesson does not measure at all."},
            {"text": "The argument is flawed — a wider span in decades says nothing about how well "
                     "an ear performs, only which frequencies it can respond to at all",
                         "correct": True},
            {"text": "The argument is sound, since bats are widely known to have poor hearing "
                     "compared with most other ordinary mammals, especially when it comes to "
                     "detecting quiet sounds",
                         "correct": False,
                         "why": "Bats are in fact known for unusually capable hearing, used for detailed "
                    "echolocation; a narrower span in decades does not make their hearing worse."},
            {"text": "The argument cannot be evaluated without first measuring both animals' "
                     "hearing in a laboratory",
                         "correct": False,
                         "why": "The flaw here is a logical one — span in decades and quality of hearing are "
                    "simply different properties — and it can be identified without new "
                    "measurements."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h12",
        "band": "harder",
        "text": "A factory worker is exposed to loud machinery for years and gradually loses "
                "hearing above 6000 Hz. A different worker is exposed to one extremely loud "
                "explosion and instantly loses hearing across a wide band. Compare what each "
                "event tells us about how hair-cell damage can happen.",
        "options": [
            {"text": "Both cases must be exactly the same underlying injury, since hearing damage "
                     "always develops in precisely the same way regardless of what caused it, "
                     "whether suddenly or gradually over time",
                         "correct": False,
                         "why": "The two cases differ in how the damage develops — gradually from repeated "
                    "exposure, or suddenly from one intense event — even though both are real "
                    "hearing damage."},
            {"text": "Only the factory worker has suffered real damage; a single loud event is too "
                     "brief to injure the ear at all",
                         "correct": False,
                         "why": "A single sufficiently loud event can and does damage hair cells immediately; "
                    "brevity does not protect the ear if the sound is intense enough."},
            {"text": "The first shows gradual damage building up over years at the vulnerable "
                     "high-frequency end, while the second shows that a single intense event can "
                     "damage a much wider band at once",
                         "correct": True},
            {"text": "Neither worker has suffered any permanent damage at all, since hearing loss "
                     "from noise always recovers fully given enough time to rest, even if that "
                     "rest only lasts for one single quiet night at home",
                         "correct": False,
                         "why": "Damage to these hair cells is described as permanent in humans, whether it "
                    "builds up gradually or happens all at once."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h13",
        "band": "harder",
        "text": "A 30 000 Hz tone is measured with an energy meter and found to carry just as "
                "much power as an audible tone a person finds moderately loud. Use this "
                "measurement to evaluate whether \"inaudible\" is a property of the sound "
                "itself or of the listener.",
        "options": [
            {"text": "Of the sound itself — the measurement shows the wave is carrying no real "
                     "energy at that frequency",
                         "correct": False,
                         "why": "The measurement described shows the opposite: the wave carries ordinary, "
                    "comparable energy to an audible tone."},
            {"text": "Of neither — the meter itself must simply be faulty, since nothing above the "
                     "human range can ever carry any measurable energy at all, however sensitive "
                     "or expensive that meter happens to be",
                         "correct": False,
                         "why": "Ultrasound behaves like any other sound and does carry measurable energy; "
                    "there is no reason to assume the meter is faulty here."},
            {"text": "Of both equally, since sound and listener always contribute exactly the same "
                     "amount to whether or not something ends up being heard, in every single case "
                     "without any exception whatsoever",
                         "correct": False,
                         "why": "This particular measurement isolates the sound's own energy from the "
                    "listener's response, and shows the energy is ordinary — the missing piece is "
                    "specifically about the listener."},
            {"text": "Of the listener — the measurement shows the wave carries ordinary energy, so "
                     "what is missing is an ear able to respond to that frequency, not anything "
                     "about the sound",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h14",
        "band": "harder",
        "text": "A cat's range (about 45 to 64 000 Hz) and a human's (about 20 to 20 000 Hz) "
                "overlap for most of the human range. Explain what a cat gains and loses "
                "compared with a human, rather than simply saying it hears \"better\".",
        "options": [
            {"text": "A cat loses almost nothing at the bottom, since 45 Hz is close to 20 Hz, but "
                     "gains a considerable stretch of extra range at the top, up to 64 000 Hz",
                         "correct": True},
            {"text": "A cat gains at the bottom of its range and loses at the top compared with a "
                     "human",
                         "correct": False,
                         "why": "It is the other way round here: the cat's bottom is slightly higher than a "
                    "human's, and its top reaches considerably further."},
            {"text": "A cat's range is simply a scaled-up copy of a human's, twice as wide at "
                     "every point",
                         "correct": False,
                         "why": "The two ranges are not a simple scaled copy of one another; the bottom "
                    "hardly changes while the top changes a great deal."},
            {"text": "A cat gains and loses exactly the same amount at both ends, leaving its "
                     "overall range the same width as a human's, just shifted along the scale, "
                     "with nothing changing overall between the two species",
                         "correct": False,
                         "why": "The cat's range is considerably wider overall than a human's, mostly because "
                    "of how much further its top reaches."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h15",
        "band": "harder",
        "text": "A device advertised as producing \"pure infrasound with zero audible "
                "component\" is tested and found to also emit a faint audible hum at 200 Hz "
                "alongside its main 15 Hz signal. Evaluate the advertising claim.",
        "options": [
            {"text": "The claim is still true, since 200 Hz is itself a form of infrasound and "
                     "therefore does not count against the claim",
                         "correct": False,
                         "why": "200 Hz sits well inside the ordinary human audible range, above the roughly "
                    "20 Hz boundary; it is not infrasound."},
            {"text": "The claim is false as tested — a genuinely pure 15 Hz signal would have no "
                     "component inside the audible range at all, yet one has been measured",
                         "correct": True},
            {"text": "The claim cannot be judged, since infrasound devices are never tested for "
                     "any other frequencies",
                         "correct": False,
                         "why": "This device clearly has been tested for other frequencies, which is exactly "
                    "how the extra 200 Hz hum was found."},
            {"text": "The claim is true, because a small hum at 200 Hz is too quiet to ever count "
                     "as a real audible component",
                         "correct": False,
                         "why": "The claim promised zero audible component, not merely a quiet one; a "
                    "measurable audible hum contradicts a claim of zero."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h16",
        "band": "harder",
        "text": "A student says that because ultrasound has a shorter wavelength than audible "
                "sound, it must also have a smaller amplitude. Evaluate this claim.",
        "options": [
            {"text": "The claim is right, since a shorter wavelength leaves physically less room for a large amplitude, so a high-frequency wave is squeezed into a smaller movement",
                         "correct": False,
                         "why": "Wavelength describes the spacing of a wave's pattern, while amplitude "
                    "describes how far each particle moves — the two do not constrain each other "
                    "in this way."},
            {"text": "The claim is right, since amplitude is simply another name for wavelength",
                         "correct": False,
                         "why": "Amplitude and wavelength are two separate properties of a wave, not two "
                    "names for the same thing."},
            {"text": "The claim is wrong — wavelength and amplitude are independent properties; a "
                     "high-frequency wave can have a large or small amplitude",
                         "correct": True},
            {"text": "The claim cannot be judged without knowing the exact material the ultrasound "
                     "is travelling through",
                         "correct": False,
                         "why": "Wavelength and amplitude are independent properties of a wave in any "
                    "material; the particular material does not change that relationship."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h17",
        "band": "harder",
        "text": "Explain why a chart showing only the TOP frequency of each animal's range, "
                "without the bottom, would give a misleading picture of how the ranges "
                "compare.",
        "options": [
            {"text": "It would hide nothing important, since the top frequency alone always "
                     "determines the full width of a range",
                         "correct": False,
                         "why": "The width of a range depends on both ends; two animals can share a similar "
                    "top while differing considerably at the bottom, or the reverse."},
            {"text": "It would make every animal's range look identical, since tops are always "
                     "roughly the same across species",
                         "correct": False,
                         "why": "The tops given in this lesson vary hugely between species, from about 12 000 "
                    "Hz for an elephant to about 110 000 Hz for a bat."},
            {"text": "It would only matter for animals that can hear ultrasound, and not for any "
                     "others",
                         "correct": False,
                         "why": "Missing the bottom of a range loses real information whether or not the "
                    "animal's top reaches into ultrasound."},
            {"text": "It would hide real differences at the bottom, such as an elephant reaching "
                     "far lower than a human despite a similar-looking top",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h18",
        "band": "harder",
        "text": "A smoke alarm signals a flat battery with a short chirp at about "
                "3000 Hz rather than a much higher tone. Evaluate why a far higher "
                "chirp would be a poor choice in a home with older occupants.",
        "options": [
            {"text": "A far higher chirp could sit above an older listener's top, which falls "
                     "with age, so the warning might go unnoticed, while 3000 Hz sits well "
                     "inside almost every adult's range",
                         "correct": True},
            {"text": "A far higher chirp would carry much less well through the walls of a house, since the pitch of a chirp is the one thing that decides how loudly it arrives in the room next door",
                         "correct": False,
                         "why": "How loudly a chirp arrives depends mainly on how much is absorbed on the "
                    "way; the trouble with a very high chirp is whose range it falls inside."},
            {"text": "A far higher chirp would reach the ear more slowly, arriving too late "
                     "to give a useful warning to anybody in the house",
                         "correct": False,
                         "why": "Every frequency travels through the same air at the same speed, so a "
                    "higher chirp arrives no later than a lower one."},
            {"text": "It would make no difference at all, since the top of a person's hearing "
                     "stays exactly where it was throughout adult life",
                         "correct": False,
                         "why": "The top of the human range falls steadily through adult life, which is "
                    "precisely why a very high warning tone is a risk."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h19",
        "band": "harder",
        "text": "A recording studio wants a single microphone that can faithfully capture "
                "both a bass guitar's lowest note, around 40 Hz, and a bat detector's "
                "downshifted output, around 15 000 Hz. Explain whether one ordinary "
                "microphone built for human hearing is likely to manage both.",
        "options": [
            {"text": "No, because 40 Hz is infrasound and no ordinary microphone can register it "
                     "at all",
                         "correct": False,
                         "why": "40 Hz is above the roughly 20 Hz boundary of infrasound, so it lies inside "
                    "the ordinary audible band, not below it."},
            {"text": "Yes, in principle — both frequencies sit inside the ordinary audible band a "
                     "human-hearing microphone is built to capture",
                         "correct": True},
            {"text": "No, because 15 000 Hz is ultrasound and no ordinary microphone built for "
                     "human hearing can register it at all, whatever its quality",
                         "correct": False,
                         "why": "15 000 Hz sits below the roughly 20 000 Hz boundary of ultrasound, so it is "
                    "still inside the ordinary audible band."},
            {"text": "No, because a microphone can only ever register one single frequency at a "
                     "time",
                         "correct": False,
                         "why": "An ordinary microphone responds to a whole band of frequencies at once, not "
                    "just one, which is exactly how it can capture real music and speech."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h20",
        "band": "harder",
        "text": "Explain why the safe listening advice \"keep the volume low enough that you "
                "could still hold a conversation\" does not fully protect against noise-induced hearing damage.",
        "options": [
            {"text": "The advice is completely sufficient on its own, since damage only ever "
                     "happens at volumes far too loud for any conversation to be possible in the "
                     "first place, so nothing below that level could ever cause harm",
                         "correct": False,
                         "why": "Damage accumulates over years of exposure, which can happen even at volumes that do not prevent normal conversation."},
            {"text": "The advice fails because conversation always happens at a completely silent "
                     "volume",
                         "correct": False,
                         "why": "Ordinary conversation is a real, audible sound with a definite volume; the "
                    "advice is comparing listening volume against that level, not against "
                    "silence."},
            {"text": "Damage builds up with cumulative exposure over time as well as with peak "
                     "loudness, so even a moderate volume kept up for very long periods can still "
                     "gradually damage high-frequency hair cells",
                         "correct": True},
            {"text": "The advice fails only for people who already have some hearing loss, and "
                     "works perfectly for everyone else",
                         "correct": False,
                         "why": "This kind of damage can happen to anyone with healthy hearing exposed to enough loud sound over time, not only to those already affected."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h21",
        "band": "harder",
        "text": "A bat, a dog and a human are all exposed to a steady 40 000 Hz tone. Taking the top of a human's hearing as about 20 000 Hz, a dog's as about 45 000 Hz and a bat's as about 110 000 Hz, which of the three, if any, would hear nothing at all?",
        "options": [
            {"text": "The bat only, since its range is described as reaching far higher than "
                     "either the human's or the dog's, which the question implies means it hears "
                     "differently from both of them",
                         "correct": False,
                         "why": "Reaching higher at the top does not mean the bat hears NOTHING at a lower "
                    "ultrasonic frequency like 40 000 Hz — its range comfortably includes it, "
                    "just as the dog's does."},
            {"text": "The dog only, since its range is described as narrower overall than either "
                     "the human's or the bat's",
                         "correct": False,
                         "why": "A dog's range reaches to about 45 000 Hz, which comfortably includes 40 000 "
                    "Hz; describing its overall span as narrower does not change that."},
            {"text": "All three would hear nothing, since 40 000 Hz is ultrasound and ultrasound "
                     "is inaudible to every animal without exception",
                         "correct": False,
                         "why": "Ultrasound is inaudible only relative to a particular ear's range; both the "
                    "bat's and the dog's ranges reach well past 40 000 Hz."},
            {"text": "The human only, since 40 000 Hz sits above the human range but inside both "
                     "the bat's range, up to 110 000 Hz, and the dog's, up to 45 000 Hz",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h22",
        "band": "harder",
        "text": "A museum exhibit lets visitors turn a dial from 20 Hz up to 20 000 Hz and "
                "hear the tone fade in and out of audibility near each end. Explain why the "
                "fading is gradual near the edges rather than the tone simply switching off "
                "at an exact number.",
        "options": [
            {"text": "Real hearing thresholds are approximate and vary between individuals, so the "
                     "edges of the quoted 20 Hz to 20 000 Hz range are not exact cut-offs for any "
                     "one person",
                         "correct": True},
            {"text": "The dial itself is faulty, since a genuine boundary should always switch off "
                     "instantly with no fading at all",
                         "correct": False,
                         "why": "This lesson describes the human range's limits as round, approximate figures "
                    "rather than exact cut-offs, so gradual fading near the edges is expected "
                    "rather than a fault."},
            {"text": "The tone is not actually changing frequency at all near the edges, only its "
                     "loudness, which is unrelated to the exhibit's real purpose in any case, and "
                     "has nothing to do with hearing ranges at all",
                         "correct": False,
                         "why": "The exhibit is specifically demonstrating the edges of the audible frequency "
                    "range, and the fading described is about audibility as frequency changes."},
            {"text": "Every visitor would experience the exact same fading at the exact same "
                     "numbers on the dial",
                         "correct": False,
                         "why": "Individual hearing varies, so different visitors are likely to notice the "
                    "fade starting at somewhat different points on the dial."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h23",
        "band": "harder",
        "text": "A sound engineer claims that halving a signal's frequency always halves how "
                "far it can be heard outdoors. Evaluate this claim against how low-frequency sound behaves over distance.",
        "options": [
            {"text": "The claim is right, since any change at all to a signal's frequency always "
                     "changes its carrying distance by exactly the same fixed factor, whatever "
                     "that frequency happens to be",
                         "correct": False,
                         "why": "There is no fixed, exact factor relating a frequency change to a carrying distance; what there is is a general trend, lower frequencies carrying further."},
            {"text": "The claim is wrong in direction — LOWER frequencies carry further, not less far, because they are absorbed less by air and by ground",
                         "correct": True},
            {"text": "The claim is right, since higher frequencies are always absorbed a good deal "
                     "less by open air than lower ones ever manage to be, which is well known "
                     "among sound engineers",
                         "correct": False,
                         "why": "The trend runs the other way: LOWER frequencies are absorbed less, which is why elephant and whale calls carry so far."},
            {"text": "The claim cannot be evaluated without knowing the loudness of the original "
                     "signal",
                         "correct": False,
                         "why": "The trend that lower frequencies carry further is about frequency and absorption, and applies whatever the original loudness happens to be."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h24",
        "band": "harder",
        "text": "Explain why a single number, such as \"20 000 Hz\", is only ever an "
                "approximate boundary for the top of human hearing, rather than a precise "
                "line every person shares.",
        "options": [
            {"text": "Because 20 000 Hz is not really a frequency at all, only a rough description "
                     "of loudness",
                         "correct": False,
                         "why": "20 000 Hz is a genuine frequency, measured in hertz, describing how fast a "
                    "sound vibrates, not a measure of loudness."},
            {"text": "Because every person's hearing changes to exactly 20 000 Hz once they reach "
                     "full adulthood, whatever it happened to be before that point, and this "
                     "single figure never changes again for the rest of that person's life",
                         "correct": False,
                         "why": "Hearing ranges do not converge on one exact shared number in adulthood; the "
                    "figure given is a rough average, and individuals vary around it."},
            {"text": "Because individual hearing varies, because published studies disagree over how quiet a sound must be before it counts as heard, and because very few adults reach 20 000 Hz in practice",
                         "correct": True},
            {"text": "Because 20 000 Hz is simply wrong, and the real boundary of human hearing "
                     "has never been measured",
                         "correct": False,
                         "why": "20 000 Hz is a widely used and reasonably accurate round figure for the top "
                    "of a young, healthy human range; the point is that it is a round convention, "
                    "not that it is wrong."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h25",
        "band": "harder",
        "text": "An elephant hears down to about 16 Hz, well below a dog's lowest of "
                "about 67 Hz, yet a dog's highest of about 45 000 Hz is far above an "
                "elephant's highest of about 12 000 Hz. Explain what this shows about "
                "comparing two animals' hearing using a single word like \"better\".",
        "options": [
            {"text": "It shows that the figures given for elephants and dogs must contain an "
                     "error, since one range cannot be both lower and higher than another",
                         "correct": False,
                         "why": "A range can perfectly well be lower at the bottom and higher at the top than "
                    "another range at the same time — there is no contradiction here."},
            {"text": "It shows that elephants hear better than dogs in every possible sense",
                         "correct": False,
                         "why": "The dog reaches far higher at the top, so the elephant wins at one end and "
                    "loses at the other; neither is simply \"better\" from these figures."},
            {"text": "It shows that dogs and elephants must actually share identical ranges, and "
                     "the differences given are just measurement error",
                         "correct": False,
                         "why": "The two ranges given differ at both ends by a clear, meaningful amount, not "
                    "by a small amount that measurement error would explain."},
            {"text": "It shows that one range can sit lower at one end and higher at the "
                     "other, so a single word like \"better\" hides which end is actually "
                     "being compared",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h26",
        "band": "harder",
        "text": "A listener plays extremely loud, bass-heavy music through earbuds for years. "
                "Given where the most vulnerable hair cells sit in the ear, predict which part of their OWN hearing is most likely to be damaged first — even though the music itself is mostly low-pitched.",
        "options": [
            {"text": "The highest frequencies they can hear, since the hair cells responding to "
                     "those sit nearest the ear's entrance and take the most punishment from loud "
                     "sound passing through, whatever its own pitch",
                         "correct": True},
            {"text": "The lowest frequencies they can hear, since damage always happens first at "
                     "whichever frequency the loud sound itself is pitched at, regardless of the "
                     "ear's structure, not at any other frequency the ear might otherwise detect",
                         "correct": False,
                         "why": "What puts the vulnerable cells at risk is their POSITION in the ear, nearest the entrance, not a match between a cell and the sound's own pitch."},
            {"text": "The middle of their hearing range, since damage always spreads outward "
                     "evenly from wherever sound enters the ear",
                         "correct": False,
                         "why": "It is the cells nearest the entrance, which respond to the highest frequencies, that take the most punishment first, not those in the middle of the range."},
            {"text": "No particular part, since bass-heavy music cannot damage any frequency other "
                     "than the bass notes it actually contains",
                         "correct": False,
                         "why": "Position in the ear, not the pitch of the music itself, is what decides which cells take the most punishment from loud sound."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h27",
        "band": "harder",
        "text": "Explain why a doctor might take \"ringing in the ears after a loud concert\" "
                "seriously as a warning sign, rather than dismissing it as ordinary and "
                "always short-lived.",
        "options": [
            {"text": "Ringing after a concert always means permanent, total deafness has already "
                     "occurred",
                         "correct": False,
                         "why": "This lesson describes damage that shows up first at the top of the range, "
                    "not immediate total deafness; ringing is a warning sign, not proof of total "
                    "loss."},
            {"text": "It can be a sign that the hair cells responding to high frequencies have "
                     "been stressed or damaged, and that damage does not repair itself in humans "
                     "even once the ringing fades",
                         "correct": True},
            {"text": "Ringing is caused by something entirely unrelated to hearing, such as "
                     "changes in blood pressure during a concert or a change in room temperature, "
                     "neither of which has anything to do with the ears themselves",
                         "correct": False,
                         "why": "The ringing described here follows exposure to loud sound and points to the "
                    "ear itself, in keeping with this lesson's account of noise damage."},
            {"text": "A doctor cannot draw any conclusion from ringing alone without an expensive "
                     "laboratory hearing test first",
                         "correct": False,
                         "why": "Ringing after loud exposure is, on its own, already a meaningful warning "
                    "sign worth taking seriously, even before any formal test is done."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h28",
        "band": "harder",
        "text": "A patient's top hearing frequency is measured at 14 000 Hz, compared with "
                "the usual young-adult figure of about 20 000 Hz. On a multiplying chart, "
                "where one mark means ten times, roughly how big a step is this fall?",
        "options": [
            {"text": "Exactly one whole mark, since any noticeable fall in hearing always "
                     "corresponds to a full factor of ten on this kind of chart",
                         "correct": False,
                         "why": "A full mark represents a factor of ten; 20 000 Hz falling to 14 000 Hz is a "
                    "much smaller change than that."},
            {"text": "More than two whole marks, since any hearing loss serious enough to measure "
                     "must be a huge change on this chart",
                         "correct": False,
                         "why": "Two marks would mean a hundred-fold fall, which would take 20 000 Hz down to "
                    "about 200 Hz — far more than the fall described here."},
            {"text": "A good deal less than one whole mark, since 20 000 divided by 14 000 is only "
                     "a little over one, nowhere near a factor of ten",
                         "correct": True},
            {"text": "The chart cannot show this change at all, since it only has marks for round "
                     "multiples of ten",
                         "correct": False,
                         "why": "A change does not need to land exactly on a mark to be shown on the chart; "
                    "it can sit at any point between two marks, including a small step like this "
                    "one."},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h29",
        "band": "harder",
        "text": "An app claims it can \"cure\" noise-induced high-frequency hearing loss by "
                "playing specially designed corrective tones through headphones. Evaluate this claim using what is known about damaged hair cells.",
        "options": [
            {"text": "The claim is very likely true, since any sound played through headphones for "
                     "long enough can gradually retrain damaged hair cells to work again, however "
                     "badly damaged they originally were",
                         "correct": False,
                         "why": "These particular hair cells do not regrow in humans once they are damaged; no amount of retraining sound changes that."},
            {"text": "The claim is very likely true, provided the corrective tones are played "
                     "loudly enough for long enough",
                         "correct": False,
                         "why": "Playing sound louder or longer does not regrow hair cells that have already "
                    "been damaged; if anything, loud sound is what causes this kind of damage in "
                    "the first place."},
            {"text": "The claim cannot be evaluated without first knowing the exact price of the "
                     "app",
                         "correct": False,
                         "why": "Whether the underlying science is plausible does not depend on the app's "
                    "price; it depends on whether damaged hair cells can regrow, and in humans they cannot."},
            {"text": "The claim is very unlikely to be true — the relevant hair cells do not "
                     "regrow in humans once damaged, so no sound played afterwards can restore "
                     "them",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-08-h30",
        "band": "harder",
        "text": "A young human's hearing spans roughly three decades of frequency, yet most of the energy in ordinary speech sits between about 100 Hz and 4000 Hz. Explain why a hearing aid does not need to amplify the whole "
                "three-decade range equally to help someone follow speech.",
        "options": [
            {"text": "Because the frequencies that actually carry most of speech's useful "
                     "information are concentrated in a much narrower band than the full range a "
                     "young ear can respond to",
                         "correct": True},
            {"text": "Because speech contains no sound at all outside the 100 Hz to 4000 Hz band, "
                     "so amplifying anywhere else would be entirely pointless for a listener, "
                     "whatever the hearing aid is designed to do",
                         "correct": False,
                         "why": "Speech does contain some energy outside that band; the point is that most of "
                    "the USEFUL information for understanding words is concentrated within it."},
            {"text": "Because a hearing aid physically cannot amplify more than one single narrow "
                     "band of frequencies at any one time, no matter how advanced or expensive its "
                     "electronics might be",
                         "correct": False,
                         "why": "A hearing aid can be built to amplify a wide band if that were useful; the "
                    "reason a narrower band often suffices is where speech's information actually "
                    "sits, not a physical limit of the device."},
            {"text": "Because the full three-decade range only applies to music, and speech uses "
                     "an entirely separate range of its own",
                         "correct": False,
                         "why": "Speech and music both fall within the same overall human auditory range; "
                    "speech's energy happens to be concentrated in a narrower band within it."},
        ],
        "figure": None,
    },
]
