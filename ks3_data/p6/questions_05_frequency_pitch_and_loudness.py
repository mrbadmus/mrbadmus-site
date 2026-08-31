"""P6 lesson 05 — Frequency, pitch and loudness: twelve questions.

Written against Design's page. The two guitar strings, the signal
generator and both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · a hertz counts vibrations each SECOND;
  · frequency sets pitch and amplitude sets loudness, independently
    (`WAVE-17`, `WAVE-19`);
  · a hertz says nothing about loudness (`WAVE-20`);
  · every frequency travels at the same speed in the same air
    (`WAVE-18`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — 1,0,3,2 · 2,3,1,0 · 3,2,0,1, three of each.

⚠️ The ladder's own two marked rungs are NOT restated. Nor are the two
worked examples, whose numbers (1500 in 5.0 s, 15 000 in 0.50 min) do not
appear here.
"""

UNIT = "P6"
LESSON = "frequency-pitch-and-loudness"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p6-05-e01",
        "band": "easier",
        "text": "A frequency of 1 hertz means…",
        "options": [
            {"text": "one vibration every minute", "correct": False,
             "why": "The hertz is counted per second, not per minute."},
            {"text": "one complete vibration every second", "correct": True},
            {"text": "one metre travelled every second", "correct": False,
             "why": "That is a speed. A hertz counts vibrations, not "
                    "distance."},
            {"text": "one unit of loudness", "correct": False,
             "why": "Loudness is set by amplitude and is nothing to do with "
                    "the hertz."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e02",
        "band": "easier",
        "text": "Which measurement decides how HIGH a note sounds?",
        "options": [
            {"text": "the frequency", "correct": True},
            {"text": "the amplitude", "correct": False,
             "why": "Amplitude decides loudness. A quiet note and a loud one "
                    "can be at exactly the same pitch."},
            {"text": "the speed of the sound", "correct": False,
             "why": "The speed is the same for every note in the same air, "
                    "so it cannot be what makes one higher."},
            {"text": "the distance from the source", "correct": False,
             "why": "Walking away makes a note quieter, not lower."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e03",
        "band": "easier",
        "text": "A speaker cone is made to move further from its rest place "
                "each time, at the same rate as before. The note…",
        "options": [
            {"text": "gets higher, because moving further each time means "
                     "the cone gets round its journey more often", "correct": False,
             "why": "Higher would need more vibrations each second, and the "
                    "rate has not changed."},
            {"text": "gets lower, because a longer journey each time "
                     "leaves the cone fewer trips to make each second",
             "correct": False,
             "why": "Lower would need fewer vibrations each second. Again, "
                    "the rate is unchanged."},
            {"text": "stops altogether, because a cone pushed that far can "
                     "no longer settle back to its rest place",
             "correct": False,
             "why": "The cone is still vibrating, so it is still making "
                    "sound."},
            {"text": "gets louder and stays at the same pitch, because "
                     "only the distance moved has changed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e04",
        "band": "easier",
        "text": "A string vibrates at 400 Hz for 3.0 seconds. How many "
                "complete vibrations is that?",
        "options": [
            {"text": "About 133", "correct": False,
             "why": "That is 400 divided by 3. Each second brings another "
                    "400, so you multiply."},
            {"text": "403", "correct": False,
             "why": "Adding a time to a frequency adds two different "
                    "quantities together."},
            {"text": "1200", "correct": True},
            {"text": "1200 Hz", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: this is "
                    "a plain count of vibrations over a stated three "
                    "seconds."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p6-05-s01",
        "band": "standard",
        "text": "An oscilloscope shows a 20 ms window. The volume is turned "
                "up and nothing else changes. What happens to the trace?",
        "options": [
            {"text": "More vibrations fit in the window, at the same "
                     "height as before", "correct": False,
             "why": "That is what raising the frequency would do. The volume "
                    "dial does not change the rate."},
            {"text": "Fewer vibrations fit in the window, and they are "
                     "taller than before", "correct": False,
             "why": "The number in the window is set by the frequency, which "
                    "has not been touched."},
            {"text": "The same number of vibrations as before, drawn "
                     "taller on the screen", "correct": True},
            {"text": "Nothing changes at all, because the width of the "
                     "window is fixed", "correct": False,
             "why": "The window being fixed is exactly why the change shows "
                    "up as height rather than as spacing."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s02",
        "band": "standard",
        "text": "How many complete vibrations fit into a 20 ms window at "
                "500 Hz?",
        "options": [
            {"text": "500", "correct": False,
             "why": "That is how many fit into a whole second. The window is "
                    "a fiftieth of one."},
            {"text": "20", "correct": False,
             "why": "That is the window in milliseconds, not a count of "
                    "vibrations."},
            {"text": "25", "correct": False,
             "why": "That would be 500 divided by 20, which mixes hertz with "
                    "milliseconds. The time has to be in seconds."},
            {"text": "10", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s03",
        "band": "standard",
        "text": "A tuning fork makes 6000 complete vibrations in 0.25 "
                "minutes. What is its frequency?",
        "options": [
            {"text": "400 Hz", "correct": True},
            {"text": "24 000 Hz", "correct": False,
             "why": "That divides by 0.25 without converting the minutes. A "
                    "hertz is counted per second."},
            {"text": "1500 Hz", "correct": False,
             "why": "That multiplies rather than divides, and skips the "
                    "conversion as well."},
            {"text": "15 Hz", "correct": False,
             "why": "That divides the converted time by the count instead of "
                    "the other way round."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s04",
        "band": "standard",
        "text": "Two notes are played, one loud and low, one quiet and high. "
                "Which comparison is correct?",
        "options": [
            {"text": "The loud one has both the bigger amplitude and the "
                     "higher frequency", "correct": False,
             "why": "It has the bigger amplitude, but the quiet one is the "
                    "high note, so it has the higher frequency."},
            {"text": "The quiet one has both the smaller amplitude and the "
                     "lower frequency", "correct": False,
             "why": "It does have the smaller amplitude, but it was "
                    "described as the HIGH note."},
            {"text": "The loud one has the bigger amplitude; the quiet one "
                     "has the higher frequency", "correct": True},
            {"text": "Nothing can be said, because loudness and pitch are "
                     "the same measurement", "correct": False,
             "why": "They are two separate measurements, which is exactly "
                    "why the two notes can differ in opposite directions."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p6-05-h01",
        "band": "harder",
        "text": "Concert A is 440 Hz and the A an octave above is 880 Hz. "
                "What does that tell you about how the ear judges pitch?",
        "options": [
            {"text": "The ear adds: an octave is always 440 Hz more",
             "correct": False,
             "why": "If that were so, the octave above 880 would be 1320. It "
                    "is 1760."},
            {"text": "The ear responds to ratios: the same musical step is "
                     "the same multiplication, not the same difference",
             "correct": True},
            {"text": "The ear cannot judge pitch above 440 Hz",
             "correct": False,
             "why": "People hear pitch clearly far above 440 Hz — most of a "
                    "piano lives up there."},
            {"text": "The ear responds only to the loudness, and pitch is "
                     "learned later from music lessons rather than heard "
                     "directly", "correct": False,
             "why": "Pitch is heard directly, and the octave relationship "
                    "holds for people who have never learned any music."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h02",
        "band": "harder",
        "text": "A piccolo and a tuba play together in a band a hundred "
                "metres away. Why does the music arrive as music?",
        "options": [
            {"text": "Because the piccolo is the quieter of the two, which "
                     "slows it down until it matches the pace the tuba is "
                     "setting", "correct": False,
             "why": "Loudness does not change the speed either, and a loud "
                    "piccolo would still arrive with the tuba."},
            {"text": "Because the tuba's low notes travel faster through "
                     "the air than the piccolo's high ones and catch them "
                     "up on the way", "correct": False,
             "why": "No frequency catches any other up. All of them travel "
                    "at the same speed."},
            {"text": "Because your brain reassembles the notes into the "
                     "right order after they arrive, putting back the "
                     "timing the journey lost", "correct": False,
             "why": "The brain does not have to. They genuinely arrive "
                    "together, which is why a recording made a hundred "
                    "metres away is in time too."},
            {"text": "Because every frequency travels through the same air "
                     "at the same speed, so all the notes arrive together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h03",
        "band": "harder",
        "text": "A student says that turning the volume up must add extra "
                "vibrations each second. What is the best correction?",
        "options": [
            {"text": "Turning the volume up makes each vibration take the "
                     "cone further, and the number each second is exactly "
                     "as it was", "correct": True},
            {"text": "Turning the volume up removes vibrations rather than "
                     "adding them", "correct": False,
             "why": "It neither adds nor removes any. The count each second "
                    "is untouched."},
            {"text": "Turning the volume up does add vibrations, but too "
                     "few to hear, so the pitch shifts by an amount nobody "
                     "notices", "correct": False,
             "why": "It adds none at all, and the pitch is unchanged by any "
                    "amount you can measure."},
            {"text": "Turning the volume up changes both the pitch and the "
                     "loudness together", "correct": False,
             "why": "The pitch does not change, which is why you can turn "
                    "music up without it going out of tune."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h04",
        "band": "harder",
        "text": "Why is a trace at 800 Hz more crowded than one at 200 Hz, "
                "when the oscilloscope window is the same either way?",
        "options": [
            {"text": "Because a higher note travels faster through the "
                     "air, so more of it gets past in the same time",
             "correct": False,
             "why": "Both travel at the same speed. Speed is not what fills "
                    "the window."},
            {"text": "Because at 800 Hz the source completes four times as "
                     "many vibrations in the same fixed window",
             "correct": True},
            {"text": "Because a higher note is quieter, so a great deal "
                     "more of it fits into the same fixed window",
             "correct": False,
             "why": "Loudness sets the height of the trace, not how many "
                    "vibrations there are."},
            {"text": "Because the oscilloscope shortens the window that it "
                     "shows for the higher notes", "correct": False,
             "why": "The window is fixed at 20 ms whatever the frequency, "
                    "which is what makes the comparison fair."},
        ],
        "figure": None,
    },
]
