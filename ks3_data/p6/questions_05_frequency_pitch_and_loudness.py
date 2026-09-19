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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-05-e05",
        "band": "easier",
        "text": "Frequency is measured in…",
        "options": [            {"text": "seconds (s)", "correct": False,
             "why": "Seconds measure time; frequency counts how many "
                    "vibrations fit into each one."},
            {"text": "decibels (dB)", "correct": False,
             "why": "Decibels describe how loud a sound is, which is set by "
                    "the amplitude instead."},
            {"text": "metres per second (m/s)", "correct": False,
             "why": "That is a speed. Every frequency of sound travels at the "
                    "same speed in one material."},
            {"text": "hertz (Hz)", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e06",
        "band": "easier",
        "text": "Which measurement decides how LOUD a note sounds?",
        "options": [
            {"text": "The frequency", "correct": False,
             "why": "Frequency sets the pitch — how high the note is, not how "
                    "loud."},
            {"text": "The amplitude", "correct": True},
            {"text": "The speed of the sound", "correct": False,
             "why": "Every sound travels at the same speed through the same "
                    "air, loud or quiet."},
            {"text": "The wavelength", "correct": False,
             "why": "Wavelength goes with frequency, so it is tied to pitch "
                    "rather than loudness."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-05-s05",
        "band": "standard",
        "text": "A string makes 1500 complete vibrations in 5.0 seconds. What "
                "is its frequency?",
        "options": [
            {"text": "7500 Hz", "correct": False,
             "why": "That is 1500 × 5. Frequency is vibrations DIVIDED by the "
                    "time."},
            {"text": "300 Hz", "correct": True},
            {"text": "0.0033 Hz", "correct": False,
             "why": "That is 5 ÷ 1500, the division upside down."},
            {"text": "1495 Hz", "correct": False,
             "why": "That subtracts, and a count cannot have a time taken "
                    "from it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s06",
        "band": "standard",
        "text": "A 200 Hz note and an 800 Hz note are played together across "
                "the same room. Which reaches the listener first?",
        "options": [
            {"text": "The 800 Hz note, because higher notes travel faster",
             "correct": False,
             "why": "Pitch has no effect on speed; if it did, music would "
                    "arrive scrambled."},
            {"text": "The 200 Hz note, because longer waves cover ground "
                     "faster",
             "correct": False,
             "why": "Wavelength does not change the speed either — all of it "
                    "arrives together."},
            {"text": "They arrive together, at the same speed", "correct": True},
            {"text": "The louder of the two, whichever that is",
             "correct": False,
             "why": "Loudness is amplitude, and it does not change the speed "
                    "of sound at all."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-05-h05",
        "band": "harder",
        "text": "A tuning fork of frequency 512 Hz rings for 2.5 s. How many "
                "complete vibrations does it make?",
        "options": [
            {"text": "1280", "correct": True},
            {"text": "205", "correct": False,
             "why": "That is 512 ÷ 2.5. The count is the frequency MULTIPLIED "
                    "by the time."},
            {"text": "514.5", "correct": False,
             "why": "That adds the time to the frequency, which cannot be "
                    "done."},
            {"text": "0.0049", "correct": False,
             "why": "That is 2.5 ÷ 512, the division the wrong way round."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h06",
        "band": "harder",
        "text": "A guitar string is plucked harder than before, and nothing "
                "else is changed. What happens to the note?",
        "options": [
            {"text": "It becomes higher, because the string moves faster",
             "correct": False,
             "why": "It does move faster, but it still completes the same "
                    "number of vibrations each second."},
            {"text": "It becomes louder and lower at the same time",
             "correct": False,
             "why": "Nothing lowers the pitch: the string's rate of vibration "
                    "is unchanged."},
            {"text": "It becomes louder: the amplitude is bigger but the rate "
                     "is not",
             "correct": True},
            {"text": "Nothing changes, because it is the same string",
             "correct": False,
             "why": "The amplitude has changed, and that is what the ear "
                    "hears as loudness."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p6-05-e07",
        "band": "easier",
        "text": "A frequency of 50 Hz means the source completes…",
        "options": [
            {"text": "50 complete vibrations every second", "correct": True},
            {"text": "50 vibrations every minute", "correct": False,
             "why": "The hertz counts vibrations each second, not each "
             "minute."},
            {"text": "half a vibration every second", "correct": False,
             "why": "50 Hz means fifty whole vibrations a second, not a "
             "fraction of one."},
            {"text": "50 metres every second", "correct": False,
             "why": "That is a speed. A hertz counts vibrations, not "
             "distance."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e08",
        "band": "easier",
        "text": "Doubling the frequency of a note, with nothing else "
                "changed, makes the note…",
        "options": [
            {"text": "louder", "correct": False,
             "why": "Loudness comes from amplitude, which has not been "
             "changed here."},
            {"text": "higher", "correct": True},
            {"text": "quieter", "correct": False,
             "why": "Loudness comes from amplitude, which has not been "
             "changed here."},
            {"text": "exactly the same as before", "correct": False,
             "why": "Doubling how often the source vibrates each second "
             "changes the pitch."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e09",
        "band": "easier",
        "text": "A source is made to swing further each time it moves, "
                "but at exactly the same rate as before. What happens to "
                "the note it makes?",
        "options": [
            {"text": "higher-pitched", "correct": False,
             "why": "Pitch comes from frequency, which has not been changed "
             "here."},
            {"text": "lower-pitched", "correct": False,
             "why": "Pitch comes from frequency, which has not been changed "
             "here."},
            {"text": "louder", "correct": True},
            {"text": "unchanged in every way", "correct": False,
             "why": "A bigger amplitude is heard as a real difference: the "
             "note gets louder."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e10",
        "band": "easier",
        "text": "A drum skin beats steadily 20 times every second. Over "
                "a 10-second drum roll, how many beats does it complete?",
        "options": [
            {"text": "2", "correct": False,
             "why": "That divides instead of multiplying. Each second brings "
             "another 20 vibrations."},
            {"text": "30", "correct": False,
             "why": "Adding a time to a frequency adds two different "
             "quantities together."},
            {"text": "200 Hz", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: this is "
             "a plain count of vibrations."},
            {"text": "200", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e11",
        "band": "easier",
        "text": "Which of these is a unit of frequency?",
        "options": [
            {"text": "The hertz", "correct": True},
            {"text": "The decibel", "correct": False,
             "why": "The decibel is a unit used for loudness, not frequency."},
            {"text": "The metre", "correct": False,
             "why": "The metre is a unit of distance."},
            {"text": "The second", "correct": False,
             "why": "The second is a unit of time, not of frequency itself."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e12",
        "band": "easier",
        "text": "A quiet note and a loud note played at exactly the "
                "same pitch have the same…",
        "options": [
            {"text": "amplitude", "correct": False,
             "why": "Amplitude is what differs between a quiet and a loud "
             "note."},
            {"text": "frequency", "correct": True},
            {"text": "decibel level", "correct": False,
             "why": "The decibel level is what differs here, since one is "
             "quieter than the other."},
            {"text": "loudness", "correct": False,
             "why": "Loudness is exactly what differs between the two notes."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e13",
        "band": "easier",
        "text": "A bass drum thump and a piccolo note are played "
                "equally loudly as each other. Which measurement of the "
                "two sounds is the same?",
        "options": [
            {"text": "frequency", "correct": False,
             "why": "Frequency is what differs here, since one note is "
             "higher than the other."},
            {"text": "pitch", "correct": False,
             "why": "Pitch is what differs here, since one note is higher "
             "than the other."},
            {"text": "amplitude", "correct": True},
            {"text": "wavelength", "correct": False,
             "why": "Their wavelengths differ along with their pitch."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e14",
        "band": "easier",
        "text": "A small bird's wings beat much faster than a "
                "swan's. Which measurement is bigger for the bird's wingbeat "
                "sound?",
        "options": [
            {"text": "Its amplitude", "correct": False,
             "why": "Beating faster changes how often the wings move, which "
             "is frequency, not how far each wing swings."},
            {"text": "Its loudness", "correct": False,
             "why": "A faster wingbeat does not by itself mean a louder "
             "sound."},
            {"text": "The speed of sound around it", "correct": False,
             "why": "The speed of sound depends on the air, not on how fast "
             "the wings beat."},
            {"text": "Its frequency", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e15",
        "band": "easier",
        "text": "An oscilloscope window is fixed at 20 ms. Raising "
                "the frequency of the note being shown makes the trace…",
        "options": [
            {"text": "show more complete vibrations in the same window", "correct": True},
            {"text": "show fewer complete vibrations in the same window", "correct": False,
             "why": "A higher frequency packs MORE vibrations into the same "
             "window, not fewer."},
            {"text": "grow taller, with no change to how crowded it is", "correct": False,
             "why": "Height changes with amplitude. Raising the frequency "
             "changes how crowded the trace is."},
            {"text": "shrink to a smaller trace overall", "correct": False,
             "why": "Raising the frequency does not shrink the trace; it "
             "crowds more vibrations into the same space."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e16",
        "band": "easier",
        "text": "The number of complete vibrations a source makes in "
                "one second is called its…",
        "options": [
            {"text": "amplitude", "correct": False,
             "why": "Amplitude is how far the source moves each time, not "
             "how often."},
            {"text": "frequency", "correct": True},
            {"text": "wavelength", "correct": False,
             "why": "Wavelength is a distance along a wave, not a count of "
             "vibrations."},
            {"text": "loudness", "correct": False,
             "why": "Loudness is how loud the note sounds, which comes from "
             "amplitude instead."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e17",
        "band": "easier",
        "text": "A tuning fork vibrates at 100 Hz for 2 seconds. How "
                "many vibrations does it make?",
        "options": [
            {"text": "50", "correct": False,
             "why": "That divides instead of multiplying the frequency by "
             "the time."},
            {"text": "102", "correct": False,
             "why": "Adding the time onto the frequency mixes up two "
             "different quantities."},
            {"text": "200", "correct": True},
            {"text": "98", "correct": False,
             "why": "Subtracting the time from the frequency mixes up two "
             "different quantities."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e18",
        "band": "easier",
        "text": "A whistle is blown harder than before, with nothing "
                "else changed about it. What happens to the note it makes?",
        "options": [
            {"text": "It gets higher and louder at the same time", "correct": False,
             "why": "Blowing harder changes only how far the air inside "
             "moves, which is loudness, not pitch."},
            {"text": "It gets lower and louder at the same time", "correct": False,
             "why": "Blowing harder changes only how far the air inside "
             "moves, which is loudness, not pitch."},
            {"text": "It gets higher only, with no change to how loud it "
            "sounds", "correct": False,
             "why": "Blowing harder makes the whistle louder; the pitch is "
             "set by the whistle's own shape."},
            {"text": "It gets louder and stays at the same pitch", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e19",
        "band": "easier",
        "text": "A vibration repeats 3 times each second. How many "
                "times does it repeat in one whole minute?",
        "options": [
            {"text": "180", "correct": True},
            {"text": "3", "correct": False,
             "why": "That gives the rate for one second, not the total "
             "across a whole minute."},
            {"text": "63", "correct": False,
             "why": "Adding 60 onto the rate mixes up two different "
             "quantities."},
            {"text": "18", "correct": False,
             "why": "That multiplies by 6 rather than by the 60 seconds in a "
             "minute."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e20",
        "band": "easier",
        "text": "For a vibrating source, amplitude describes how far…",
        "options": [
            {"text": "sound travels through the air in one second", "correct": False,
             "why": "That describes a speed, a different quantity from "
             "amplitude."},
            {"text": "the source moves from its rest place each time it "
            "vibrates", "correct": True},
            {"text": "the source repeats its own motion each second", "correct": False,
             "why": "How often it repeats is the frequency, not the "
             "amplitude."},
            {"text": "a note travels before it fades away completely", "correct": False,
             "why": "How far a note carries is not what amplitude measures "
             "on this bench."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e21",
        "band": "easier",
        "text": "An oscilloscope window lasts exactly 1 second and "
                "shows 60 complete vibrations. What is the frequency?",
        "options": [
            {"text": "1 Hz", "correct": False,
             "why": "That reads off the length of the window rather than the "
             "count of vibrations inside it."},
            {"text": "6 Hz", "correct": False,
             "why": "That divides the count by 10 for no reason; the window "
             "is exactly 1 second long."},
            {"text": "60 Hz", "correct": True},
            {"text": "600 Hz", "correct": False,
             "why": "That multiplies the count by 10 for no reason; the "
             "window is exactly 1 second long."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e22",
        "band": "easier",
        "text": "Which pair of measurements are independent of each "
                "other for a vibrating source?",
        "options": [
            {"text": "Frequency and pitch", "correct": False,
             "why": "These two are directly linked: the frequency is exactly "
             "what decides the pitch."},
            {"text": "Amplitude and loudness", "correct": False,
             "why": "These two are directly linked: the amplitude is exactly "
             "what decides the loudness."},
            {"text": "Frequency and hertz", "correct": False,
             "why": "These are not two separate measurements at all; hertz "
             "is simply the unit frequency is measured in."},
            {"text": "Frequency and amplitude", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e23",
        "band": "easier",
        "text": "A car horn sounds much louder than a doorbell "
                "chime, at the same pitch as each other. Which measurement "
                "differs between the two sounds?",
        "options": [
            {"text": "Their amplitude", "correct": True},
            {"text": "Their frequency", "correct": False,
             "why": "The two sounds are stated to share the same pitch, so "
             "their frequency is the same."},
            {"text": "Their wavelength", "correct": False,
             "why": "Sharing the same pitch means sharing the same "
             "frequency, and so the same wavelength too."},
            {"text": "The speed of sound around each one", "correct": False,
             "why": "Both sounds travel through the same air at the same "
             "speed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e24",
        "band": "easier",
        "text": "A vibration happens 120 times in one minute, at a "
                "steady rate. What is its frequency in Hz?",
        "options": [
            {"text": "120 Hz", "correct": False,
             "why": "That reads off the count for a whole minute as if it "
             "were the count for one second."},
            {"text": "2 Hz", "correct": True},
            {"text": "60 Hz", "correct": False,
             "why": "That divides by 2 rather than by the 60 seconds in a "
             "minute."},
            {"text": "7200 Hz", "correct": False,
             "why": "That multiplies the count by 60 rather than dividing by "
             "it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e25",
        "band": "easier",
        "text": "Whistle A makes 300 vibrations each second; Whistle "
                "B makes 500. Which one sounds higher?",
        "options": [
            {"text": "Whistle A", "correct": False,
             "why": "The higher frequency, not the lower one, gives the "
             "higher-sounding note."},
            {"text": "They sound exactly the same pitch", "correct": False,
             "why": "Different frequencies give different pitches; 300 Hz "
             "and 500 Hz are not the same."},
            {"text": "Whistle B", "correct": True},
            {"text": "It depends on how hard each one is blown", "correct": False,
             "why": "How hard each is blown changes the loudness, not which "
             "one sounds higher."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e26",
        "band": "easier",
        "text": "A note is recorded twice, once quietly and once "
                "loudly, with nothing else changed. What differs between the "
                "two oscilloscope traces?",
        "options": [
            {"text": "The loud one is more crowded with vibrations", "correct": False,
             "why": "Crowding comes from frequency, which is unchanged "
             "between the two recordings."},
            {"text": "The loud one's trace lasts twice as long on the screen", "correct": False,
             "why": "The window length is fixed; loudness changes the height "
             "of the trace, not how long it runs."},
            {"text": "Nothing at all differs between the two traces", "correct": False,
             "why": "A louder note genuinely draws a taller trace on the "
             "screen."},
            {"text": "The loud one is drawn taller", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e27",
        "band": "easier",
        "text": "How should '40 Hz' be read aloud?",
        "options": [
            {"text": "Forty hertz", "correct": True},
            {"text": "Forty metres", "correct": False,
             "why": "The hertz is not a unit of distance."},
            {"text": "Forty decibels", "correct": False,
             "why": "The decibel is a different unit, used for loudness."},
            {"text": "Forty seconds", "correct": False,
             "why": "The hertz is not a unit of time."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e28",
        "band": "easier",
        "text": "Which of these correctly pairs a measurement with "
                "its unit?",
        "options": [
            {"text": "Amplitude — hertz", "correct": False,
             "why": "Amplitude is a distance, and is not measured in hertz."},
            {"text": "Frequency — hertz", "correct": True},
            {"text": "Loudness — metres", "correct": False,
             "why": "Metres measure distance, not how loud something sounds."},
            {"text": "Pitch — seconds", "correct": False,
             "why": "Seconds measure time, not how high or low a note "
             "sounds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e29",
        "band": "easier",
        "text": "A bell strikes 45 times in 9 seconds, at a steady "
                "rate. What is its frequency?",
        "options": [
            {"text": "54 Hz", "correct": False,
             "why": "That adds the time to the count rather than dividing "
             "one by the other."},
            {"text": "36 Hz", "correct": False,
             "why": "That subtracts the time from the count rather than "
             "dividing one by the other."},
            {"text": "5 Hz", "correct": True},
            {"text": "405 Hz", "correct": False,
             "why": "That multiplies the two values rather than dividing the "
             "count by the time."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-e30",
        "band": "easier",
        "text": "Which word describes how HIGH or LOW a note sounds?",
        "options": [
            {"text": "Hertz", "correct": False,
             "why": "Hertz is the unit frequency is measured in, not the "
             "word for the sensation itself."},
            {"text": "Amplitude", "correct": False,
             "why": "Amplitude is about how far the source moves, which sets "
             "loudness rather than pitch."},
            {"text": "Loudness", "correct": False,
             "why": "Loudness describes how loud a note sounds, a separate "
             "quality from pitch."},
            {"text": "Pitch", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p6-05-s07",
        "band": "standard",
        "text": "A guitar string vibrates 900 times in 0.5 minutes. "
                "What is its frequency?",
        "options": [
            {"text": "30 Hz", "correct": True},
            {"text": "1800 Hz", "correct": False,
             "why": "That treats 0.5 as if it were the number of seconds "
             "rather than converting it to 30 seconds first."},
            {"text": "450 Hz", "correct": False,
             "why": "That divides by 2 rather than converting the 0.5 "
             "minutes into 30 seconds."},
            {"text": "30", "correct": False,
             "why": "The arithmetic is right and the unit is missing: this "
             "needs to be given in hertz."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s08",
        "band": "standard",
        "text": "An oscilloscope window is 50 ms long. How many "
                "complete vibrations of a 200 Hz note fit in it?",
        "options": [
            {"text": "4", "correct": False,
             "why": "That divides the frequency by the window length in "
             "milliseconds without converting units."},
            {"text": "10", "correct": True},
            {"text": "250", "correct": False,
             "why": "That adds the window length onto the frequency rather "
             "than multiplying them."},
            {"text": "10000", "correct": False,
             "why": "That treats the window as 50 seconds rather than 50 "
             "milliseconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s09",
        "band": "standard",
        "text": "A student increases the amplitude on a signal "
                "generator but leaves the frequency dial untouched. What "
                "happens on the oscilloscope screen?",
        "options": [
            {"text": "More vibrations fit in the window than before", "correct": False,
             "why": "How many vibrations fit in the window is set by the "
             "frequency, which has not been touched."},
            {"text": "Fewer vibrations fit in the window than before", "correct": False,
             "why": "How many vibrations fit in the window is set by the "
             "frequency, which has not been touched."},
            {"text": "The same number of vibrations fit in the window, drawn "
            "taller than before", "correct": True},
            {"text": "The trace disappears from the screen completely", "correct": False,
             "why": "A bigger amplitude makes a bigger, more visible trace, "
             "not a vanishing one."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s10",
        "band": "standard",
        "text": "Two whistles are blown with exactly the same force. "
                "Whistle A makes 400 vibrations each second; Whistle B makes "
                "800. Which statement is correct?",
        "options": [
            {"text": "Whistle B is louder and higher-pitched than Whistle A", "correct": False,
             "why": "Blowing with the same force keeps the loudness the "
             "same; only the pitch differs here."},
            {"text": "Whistle A is the higher-pitched of the two", "correct": False,
             "why": "The higher frequency, 800 Hz, belongs to Whistle B, "
             "which is the higher-pitched one."},
            {"text": "They sound identical in every way", "correct": False,
             "why": "Their different frequencies mean they sound different "
             "in pitch, even played with equal force."},
            {"text": "They are equally loud, but Whistle B is higher-pitched", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s11",
        "band": "standard",
        "text": "A note is played for a quarter of a second at 800 "
                "Hz. How many complete vibrations occur?",
        "options": [
            {"text": "200", "correct": True},
            {"text": "3200", "correct": False,
             "why": "That multiplies by 4 rather than by the quarter-second "
             "actually given."},
            {"text": "800", "correct": False,
             "why": "That forgets to scale the frequency down for the "
             "shorter quarter-second duration."},
            {"text": "3.2", "correct": False,
             "why": "That divides the frequency by 250, the quarter-second "
             "written out in milliseconds, instead of multiplying by the "
             "0.25 s given."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s12",
        "band": "standard",
        "text": "Why does turning up the volume on a stereo not "
                "change the pitch of the music?",
        "options": [
            {"text": "Because pitch is fixed by the material of the speaker "
            "cone and cannot be altered by any dial", "correct": False,
             "why": "The same speaker plays many different pitches, all "
             "depending on the signal fed into it, not on its material."},
            {"text": "Because the volume control changes the amplitude only, "
            "leaving the frequency of each note unchanged", "correct": True},
            {"text": "Because the ear stops being able to detect pitch once "
            "a sound passes a certain volume", "correct": False,
             "why": "Pitch stays clearly audible at high volumes; turning "
             "music up does not switch pitch perception off."},
            {"text": "Because loudness and pitch are actually the same "
            "physical measurement under two different names", "correct": False,
             "why": "They are two separate measurements: one comes from "
             "amplitude, the other from frequency."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s13",
        "band": "standard",
        "text": "Two oscilloscope traces use the same 20 ms window. "
                "Trace A shows 4 complete vibrations; Trace B shows 12. "
                "Which note has the higher frequency, and what are the two "
                "frequencies?",
        "options": [
            {"text": "Trace A, at 600 Hz, against Trace B's 200 Hz", "correct": False,
             "why": "This swaps which trace is higher and swaps the two "
             "calculated values as well."},
            {"text": "Trace B, but both traces are actually at 400 Hz", "correct": False,
             "why": "The two traces show different numbers of vibrations in "
             "the same window, so their frequencies cannot be equal."},
            {"text": "Trace B, at 600 Hz, against Trace A's 200 Hz", "correct": True},
            {"text": "It cannot be told without knowing the amplitude of "
            "each trace", "correct": False,
             "why": "Frequency is read from how crowded the trace is, which "
             "needs no information about amplitude."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s14",
        "band": "standard",
        "text": "A recorder player uncovers more finger holes, which "
                "shortens the effective length of vibrating air inside and "
                "raises the pitch. If the player also blows harder at the "
                "same time, what happens to the loudness?",
        "options": [
            {"text": "It must decrease, since raising the pitch quietens a "
            "note", "correct": False,
             "why": "Pitch and loudness are separate measurements; raising "
             "the pitch does not by itself quieten anything."},
            {"text": "It stays exactly the same, since only pitch can change "
            "on this instrument", "correct": False,
             "why": "Blowing harder changes how far the air inside moves, "
             "which changes the loudness too."},
            {"text": "It cannot be predicted from the information given", "correct": False,
             "why": "Blowing harder is stated directly, and that alone is "
             "enough to say the loudness increases."},
            {"text": "It also increases, independently of the pitch change", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s15",
        "band": "standard",
        "text": "A signal generator's frequency is halved and its "
                "amplitude is doubled at the same time. What happens to the "
                "trace on a fixed-width oscilloscope window?",
        "options": [
            {"text": "Half as many vibrations fit in the window, each one "
            "drawn taller than before", "correct": True},
            {"text": "Twice as many vibrations fit in the window, each one "
            "drawn shorter than before", "correct": False,
             "why": "Halving the frequency fits FEWER vibrations in the "
             "window, not more, and doubling the amplitude makes them "
             "taller, not shorter."},
            {"text": "The same number of vibrations fit in the window, all "
            "drawn taller than before", "correct": False,
             "why": "Halving the frequency does change how many vibrations "
             "fit in a fixed window."},
            {"text": "The trace disappears, since the two changes cancel "
            "each other out", "correct": False,
             "why": "The two changes affect different features of the trace "
             "and do not cancel one another."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s16",
        "band": "standard",
        "text": "A machine vibrates 7200 times in 3 minutes at a "
                "steady rate. What is its frequency?",
        "options": [
            {"text": "2400 Hz", "correct": False,
             "why": "That divides by 3 rather than converting the 3 minutes "
             "into 180 seconds first."},
            {"text": "40 Hz", "correct": True},
            {"text": "24 Hz", "correct": False,
             "why": "That divides by 300 rather than by the 180 seconds "
             "actually in 3 minutes."},
            {"text": "21600 Hz", "correct": False,
             "why": "That multiplies the two values rather than dividing the "
             "count by the time."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s17",
        "band": "standard",
        "text": "A loudspeaker cone is driven to move exactly twice "
                "as far each time, at exactly the same rate as before. Why "
                "does the pitch of the note not change?",
        "options": [
            {"text": "Because pitch is set by the size of the speaker "
            "cabinet, not by how the cone itself moves", "correct": False,
             "why": "The same cabinet plays many different pitches, all set "
             "by the frequency it is driven at."},
            {"text": "Because doubling a distance halves a frequency, which "
            "cancels the change out", "correct": False,
             "why": "Distance and frequency are separate measurements; "
             "changing one does not automatically change the other."},
            {"text": "Because the rate the cone goes to and fro, its "
            "frequency, has not been changed, only how far it moves each "
            "time", "correct": True},
            {"text": "Because the ear cannot detect a change in amplitude on "
            "its own", "correct": False,
             "why": "The ear detects amplitude changes readily, which is "
             "exactly why the note is heard to get louder."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s18",
        "band": "standard",
        "text": "A drone rotor produces 3000 complete vibrations of "
                "sound in 0.5 minutes. What is the frequency of the sound it "
                "makes?",
        "options": [
            {"text": "6000 Hz", "correct": False,
             "why": "That divides by 0.5 directly rather than converting the "
             "0.5 minutes into 30 seconds first."},
            {"text": "100", "correct": False,
             "why": "The arithmetic is right and the unit is missing: this "
             "needs to be given in hertz."},
            {"text": "1500 Hz", "correct": False,
             "why": "That multiplies by 0.5 rather than converting the time "
             "and dividing by it."},
            {"text": "100 Hz", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s19",
        "band": "standard",
        "text": "Note A is 300 Hz at a small amplitude; Note B is "
                "also 300 Hz but at a large amplitude. Which of these is "
                "true?",
        "options": [
            {"text": "They have the same pitch, but Note B is louder", "correct": True},
            {"text": "They have the same pitch and the same loudness", "correct": False,
             "why": "Their amplitudes differ, so their loudness differs too, "
             "even with matching frequencies."},
            {"text": "Note A is the higher-pitched of the two", "correct": False,
             "why": "Both notes share the same frequency, so neither is "
             "higher-pitched than the other."},
            {"text": "Note B is the higher-pitched of the two", "correct": False,
             "why": "Both notes share the same frequency, so neither is "
             "higher-pitched than the other."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s20",
        "band": "standard",
        "text": "A wasp's wings beat 4600 times in 2.0 seconds. What "
                "is the frequency of the buzzing sound?",
        "options": [
            {"text": "9200 Hz", "correct": False,
             "why": "That multiplies the two values rather than dividing the "
             "count by the time."},
            {"text": "2300 Hz", "correct": True},
            {"text": "2300", "correct": False,
             "why": "The arithmetic is right and the unit is missing: this "
             "needs to be given in hertz."},
            {"text": "4598 Hz", "correct": False,
             "why": "That subtracts the time from the count rather than "
             "dividing one by the other."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s21",
        "band": "standard",
        "text": "A speaker plays a steady 200 Hz note. A listener "
                "walks from 2 m away to 10 m away, and nothing about the "
                "speaker is changed. What happens to the note they hear?",
        "options": [
            {"text": "It sounds lower-pitched, because a longer journey "
            "stretches each vibration out on the way", "correct": False,
             "why": "The journey does not stretch the vibrations out. The "
             "speaker still sends 200 of them every second, so the pitch is "
             "unchanged."},
            {"text": "It sounds higher-pitched, because the low parts of a "
            "note fade first over a long distance", "correct": False,
             "why": "A note of one steady frequency has no separate low part "
             "to lose, and the pitch a listener hears does not shift with "
             "distance."},
            {"text": "It sounds exactly the same, because the speaker is "
            "still producing an identical 200 Hz note", "correct": False,
             "why": "The frequency is indeed unchanged, but the vibrations "
             "reaching the ear are smaller further away, so the note is not "
             "heard the same."},
            {"text": "It stays at the same pitch, but sounds quieter, since "
            "less of the vibration reaches the ear", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s22",
        "band": "standard",
        "text": "Machine A ticks 50 times in 2 seconds. Machine B "
                "ticks 30 times in 1 second. Which has the higher frequency?",
        "options": [
            {"text": "Machine A, at 50 Hz against Machine B's 30 Hz", "correct": False,
             "why": "That reads A's raw count over 2 seconds as if it were "
             "its frequency, without dividing by the time."},
            {"text": "They share exactly the same frequency", "correct": False,
             "why": "25 Hz and 30 Hz are two different frequencies, so the "
             "two machines do not match."},
            {"text": "Machine A, at 25 Hz against Machine B's 20 Hz", "correct": False,
             "why": "Machine B's frequency is 30 Hz, from 30 ticks in "
             "exactly 1 second, not 20 Hz."},
            {"text": "Machine B, at 30 Hz against Machine A's 25 Hz", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s23",
        "band": "standard",
        "text": "A loud handclap and a quiet metronome tick can "
                "still have the same frequency if…",
        "options": [
            {"text": "they both repeat the same number of times each second", "correct": True},
            {"text": "they are both exactly the same loudness", "correct": False,
             "why": "The question already states one is loud and the other "
             "quiet, so their loudness differs."},
            {"text": "they are both made by hitting two solid objects "
            "together", "correct": False,
             "why": "How a sound is produced does not by itself fix its "
             "frequency."},
            {"text": "the clap happens much closer to the listener than the "
            "tick", "correct": False,
             "why": "Distance from the listener changes loudness, not the "
             "source's own frequency."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s24",
        "band": "standard",
        "text": "A fan produces a steady buzzing sound of 5400 "
                "complete vibrations in 1.5 minutes. What is the frequency, "
                "in Hz?",
        "options": [
            {"text": "3600 Hz", "correct": False,
             "why": "That divides by 1.5 directly rather than converting the "
             "1.5 minutes into 90 seconds first."},
            {"text": "60 Hz", "correct": True},
            {"text": "90 Hz", "correct": False,
             "why": "That divides by 60 rather than by the 90 seconds "
             "actually in 1.5 minutes."},
            {"text": "8100 Hz", "correct": False,
             "why": "That multiplies the two values rather than dividing the "
             "count by the time."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s25",
        "band": "standard",
        "text": "A note's amplitude is increased while its frequency "
                "is decreased, both at the same time. Which statement is "
                "definitely true?",
        "options": [
            {"text": "The note becomes louder and higher-pitched", "correct": False,
             "why": "A decreasing frequency lowers the pitch, not raises it."},
            {"text": "The note becomes quieter and lower-pitched", "correct": False,
             "why": "An increasing amplitude makes the note louder, not "
             "quieter."},
            {"text": "The note becomes louder and lower-pitched", "correct": True},
            {"text": "Nothing about the note can be predicted, since the two "
            "changes cancel each other out", "correct": False,
             "why": "The two changes affect separate qualities and do not "
             "cancel one another; both effects happen together."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s26",
        "band": "standard",
        "text": "A double bass makes lower-pitched notes than a "
                "violin, but can be played more loudly. What does this tell "
                "you about the relationship between frequency and amplitude?",
        "options": [
            {"text": "It shows lower-pitched instruments are naturally "
            "quieter", "correct": False,
             "why": "The double bass is the lower-pitched instrument here "
             "and is described as being able to play more loudly."},
            {"text": "It shows amplitude is what actually decides pitch on "
            "stringed instruments", "correct": False,
             "why": "Pitch on a stringed instrument comes from frequency, "
             "set by the string's tension, thickness and length."},
            {"text": "It shows every instrument has one fixed loudness set "
            "by its size", "correct": False,
             "why": "The same double bass can be played both quietly and "
             "loudly; loudness is not fixed by size alone."},
            {"text": "Nothing links them — either instrument could in "
            "principle be tuned to any combination of the two", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s27",
        "band": "standard",
        "text": "A generator buzzes 850 times in 2.5 seconds. What "
                "is its frequency?",
        "options": [
            {"text": "340 Hz", "correct": True},
            {"text": "2125 Hz", "correct": False,
             "why": "That multiplies the two values rather than dividing the "
             "count by the time."},
            {"text": "340", "correct": False,
             "why": "The arithmetic is right and the unit is missing: this "
             "needs to be given in hertz."},
            {"text": "212.5 Hz", "correct": False,
             "why": "That divides by 4 rather than by the 2.5 seconds "
             "actually given."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s28",
        "band": "standard",
        "text": "Two oscilloscope traces use the same window. Trace "
                "P is twice as crowded with vibrations as Trace Q. What can "
                "you say about their frequencies?",
        "options": [
            {"text": "Trace P's frequency is half Trace Q's", "correct": False,
             "why": "Being more crowded means MORE vibrations fit in the "
             "same window, which means a higher frequency, not a lower one."},
            {"text": "Trace P's frequency is twice Trace Q's", "correct": True},
            {"text": "Both traces have the same frequency", "correct": False,
             "why": "One trace being twice as crowded as the other means "
             "their frequencies must differ."},
            {"text": "It cannot be told without knowing the amplitude of "
            "each trace", "correct": False,
             "why": "Crowding in the window is read from frequency alone; "
             "amplitude is not needed for this comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s29",
        "band": "standard",
        "text": "A trace shows 8 complete vibrations in a fixed "
                "window. The amplitude is then increased, with nothing else "
                "changed. How many complete vibrations show in the window "
                "now?",
        "options": [
            {"text": "16", "correct": False,
             "why": "How many vibrations fit in the window is set by the "
             "frequency, which has not been touched."},
            {"text": "4", "correct": False,
             "why": "How many vibrations fit in the window is set by the "
             "frequency, which has not been touched."},
            {"text": "Still 8", "correct": True},
            {"text": "It cannot be told without knowing the new amplitude", "correct": False,
             "why": "The count of vibrations in the window depends on the "
             "frequency, not on the amplitude."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-s30",
        "band": "standard",
        "text": "A guitarist tunes a string by tightening it, which "
                "raises its vibration rate. Explain, in terms of frequency "
                "and pitch, why this changes the note.",
        "options": [
            {"text": "Tightening raises the amplitude of vibration, which is "
            "heard as a louder note", "correct": False,
             "why": "The question states the rate of vibration rises, which "
             "is a change in frequency, not amplitude."},
            {"text": "Tightening changes the wavelength of the string but "
            "leaves the frequency and pitch unchanged", "correct": False,
             "why": "A change in the vibration rate is exactly a change in "
             "frequency, which is what raises the pitch."},
            {"text": "Tightening has no effect on the frequency, only on how "
            "the string feels to pluck", "correct": False,
             "why": "The question states directly that tightening raises the "
             "vibration rate, which is the frequency."},
            {"text": "Tightening raises the frequency of vibration, and a "
            "higher frequency is heard as a higher pitch", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p6-05-h07",
        "band": "harder",
        "text": "A student claims: 'A signal generator set to 1000 "
                "Hz makes a sound wave that travels twice as fast as one set "
                "to 500 Hz.' Evaluate this claim.",
        "options": [
            {"text": "Wrong — every frequency of sound travels at the same "
            "speed through the same air", "correct": True},
            {"text": "Correct — doubling the frequency doubles the speed of "
            "the resulting sound wave", "correct": False,
             "why": "Speed in a given material stays the same whatever the "
             "frequency; only the pitch changes."},
            {"text": "Correct, but this holds for frequencies above 500 Hz "
            "specifically", "correct": False,
             "why": "There is no frequency threshold at which speed starts "
             "to change; it is fixed by the material at every frequency."},
            {"text": "It cannot be judged without knowing the amplitude of "
            "each signal", "correct": False,
             "why": "Amplitude plays no part in the speed of sound; the "
             "claim is wrong regardless of amplitude."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h08",
        "band": "harder",
        "text": "A pendulum-driven chime buzzes at 4 Hz continuously "
                "for exactly half an hour. How many complete vibrations does "
                "it make?",
        "options": [
            {"text": "120", "correct": False,
             "why": "That uses the number of minutes in half an hour rather "
             "than the number of seconds."},
            {"text": "7200", "correct": True},
            {"text": "14400", "correct": False,
             "why": "That uses the 3600 seconds in a whole hour rather than "
             "the 1800 seconds in half an hour."},
            {"text": "1800", "correct": False,
             "why": "That gives the number of seconds in half an hour, "
             "forgetting to multiply by the frequency at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h09",
        "band": "harder",
        "text": "A student says: 'If a source keeps the same "
                "frequency and the same amplitude but is left vibrating for "
                "twice as long, the note it makes will be twice as loud.' "
                "Evaluate this reasoning.",
        "options": [
            {"text": "Correct — the ear adds up every vibration it receives, "
            "so a note that lasts twice as long is heard at twice the "
            "loudness", "correct": False,
             "why": "The ear does not total a note up as it goes; how loud "
             "each moment sounds is set by how far the source swings, not by "
             "how many swings have gone before."},
            {"text": "Correct, though the doubling only holds for notes that "
            "last under a second or so", "correct": False,
             "why": "There is no such time threshold: a longer note is not "
             "louder at any duration, short or long."},
            {"text": "Wrong — how long a note lasts is separate from how "
            "loud it is; loudness is set by the amplitude, which has not "
            "changed", "correct": True},
            {"text": "It cannot be evaluated without knowing the frequency "
            "the source has been set to", "correct": False,
             "why": "The frequency sets the pitch, not the loudness, so no "
             "particular value of it is needed to judge the claim."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h10",
        "band": "harder",
        "text": "A tuning fork is timed making 27 000 complete "
                "vibrations in exactly 45 seconds. What is its frequency?",
        "options": [
            {"text": "1 215 000 Hz", "correct": False,
             "why": "That multiplies the count by the time rather than "
             "dividing the count by the time."},
            {"text": "0.0017 Hz", "correct": False,
             "why": "That divides the time by the count, the calculation the "
             "wrong way round."},
            {"text": "26 955 Hz", "correct": False,
             "why": "That subtracts the time from the count rather than "
             "dividing one by the other."},
            {"text": "600 Hz", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h11",
        "band": "harder",
        "text": "A student says: 'A car horn is loud, so it must "
                "have a high frequency; a whisper is quiet, so it must have "
                "a low frequency.' Evaluate this reasoning.",
        "options": [
            {"text": "Wrong — loudness comes from amplitude and pitch comes "
            "from frequency, and either can be high or low independently of "
            "the other", "correct": True},
            {"text": "Correct, since loud sounds tend to be high-pitched "
            "instruments and quiet sounds tend to be low-pitched ones in "
            "most everyday situations people encounter", "correct": False,
             "why": "There is no such general pattern: a loud, low foghorn "
             "and a quiet, high whistle both exist."},
            {"text": "Correct for a car horn specifically, but not "
            "necessarily for other sources", "correct": False,
             "why": "A car horn is simply loud and happens to be fairly "
             "high-pitched; neither property causes the other."},
            {"text": "It cannot be judged without measuring the decibel "
            "level of each sound", "correct": False,
             "why": "Knowing the exact loudness in decibels would not tell "
             "you anything about the frequency either way."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h12",
        "band": "harder",
        "text": "Note X has frequency 250 Hz and amplitude 2 mm. "
                "Note Y has frequency 600 Hz and amplitude 5 mm. Which "
                "comparison is correct?",
        "options": [
            {"text": "Note X is higher-pitched, but Note Y is louder", "correct": False,
             "why": "Note Y has the bigger frequency, 600 Hz against 250 Hz, "
             "so Y is the higher-pitched one, not X."},
            {"text": "Note Y is both higher-pitched and louder than Note X", "correct": True},
            {"text": "Note Y is higher-pitched, but Note X is louder", "correct": False,
             "why": "Note Y has the bigger amplitude, 5 mm against 2 mm, so "
             "Y is the louder one, not X."},
            {"text": "They are equally loud, but Note Y is higher-pitched", "correct": False,
             "why": "Their amplitudes differ, 2 mm against 5 mm, so their "
             "loudness differs too."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h13",
        "band": "harder",
        "text": "Trace A shows a 300 Hz note across a 20 ms window. "
                "Trace B shows a 600 Hz note across a 10 ms window, half as "
                "wide. How do the numbers of complete vibrations shown in "
                "the two traces compare?",
        "options": [
            {"text": "Trace B shows twice as many complete vibrations as "
            "Trace A", "correct": False,
             "why": "Halving the window exactly cancels doubling the "
             "frequency, so the two counts come out equal, not doubled."},
            {"text": "Trace A shows twice as many complete vibrations as "
            "Trace B", "correct": False,
             "why": "Doubling the frequency exactly cancels halving the "
             "window, so the two counts come out equal, not doubled."},
            {"text": "They show exactly the same number of complete "
            "vibrations, 6 each", "correct": True},
            {"text": "It cannot be told without knowing the amplitude of "
            "each trace", "correct": False,
             "why": "The count of vibrations shown depends on frequency and "
             "window length alone, not on amplitude."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h14",
        "band": "harder",
        "text": "A generator is set to 250 Hz and left running for "
                "an unknown time, producing 11 250 complete vibrations. For "
                "how long was it running?",
        "options": [
            {"text": "2 812 500 s", "correct": False,
             "why": "That multiplies the two values together rather than "
             "dividing the count by the frequency."},
            {"text": "0.022 s", "correct": False,
             "why": "That divides the frequency by the count, the "
             "calculation the wrong way round."},
            {"text": "11 000 s", "correct": False,
             "why": "That subtracts the frequency from the count rather than "
             "dividing one by the other."},
            {"text": "45 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h15",
        "band": "harder",
        "text": "An orchestra tunes every instrument to the same "
                "note before a concert. A student says this means every "
                "instrument must also be equally loud once tuned. Evaluate.",
        "options": [
            {"text": "Wrong — tuning fixes the frequency, and so the pitch, "
            "each instrument plays for that note, but says nothing about how "
            "loud each one can be played", "correct": True},
            {"text": "Correct — once instruments share a tuned frequency, "
            "they automatically end up sharing the same amplitude and so the "
            "same loudness as each other", "correct": False,
             "why": "Frequency and amplitude are independent; sharing one "
             "does not fix the other."},
            {"text": "Correct, for string instruments specifically", "correct": False,
             "why": "There is nothing about string instruments in particular "
             "that links their tuned frequency to their loudness."},
            {"text": "It cannot be judged without knowing the size of the "
            "concert hall", "correct": False,
             "why": "The size of the hall changes how the sound is heard by "
             "an audience, not the relationship between an instrument's own "
             "frequency and amplitude."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h16",
        "band": "harder",
        "text": "A designer wants a doorbell that sounds both "
                "higher-pitched and quieter than the current model, changing "
                "nothing else about how it is built. Which two properties of "
                "its vibration must change, and in which directions?",
        "options": [
            {"text": "Frequency must increase and amplitude must also "
            "increase", "correct": False,
             "why": "A quieter doorbell needs a smaller amplitude, not a "
             "bigger one."},
            {"text": "Frequency must increase and amplitude must decrease", "correct": True},
            {"text": "The amplitude alone needs to change, since pitch "
            "cannot be redesigned", "correct": False,
             "why": "Pitch is set by frequency and can be changed by "
             "redesigning how often the doorbell vibrates."},
            {"text": "Frequency alone needs to change, since loudness is "
            "fixed by the doorbell's size", "correct": False,
             "why": "Loudness comes from amplitude, which can be changed by "
             "redesigning how far the doorbell vibrates."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h17",
        "band": "harder",
        "text": "A machine buzzes at a steady rate and completes 1 "
                "vibration every 0.004 seconds. What is its frequency?",
        "options": [
            {"text": "0.004 Hz", "correct": False,
             "why": "That gives back the time between vibrations rather than "
             "the frequency itself."},
            {"text": "400 Hz", "correct": False,
             "why": "That comes from dividing 1 by 0.0025 rather than by the "
             "0.004 seconds actually given."},
            {"text": "250 Hz", "correct": True},
            {"text": "4 Hz", "correct": False,
             "why": "That confuses the 0.004 seconds with a count of "
             "vibrations rather than a time."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h18",
        "band": "harder",
        "text": "A drone motor buzzes at 3000 Hz. How long, in "
                "minutes, does it take to complete 540 000 vibrations?",
        "options": [
            {"text": "180 minutes", "correct": False,
             "why": "That gives the correct number of seconds, 180, without "
             "converting it into minutes."},
            {"text": "0.3 minutes", "correct": False,
             "why": "That reaches the correct 180 seconds and then divides "
             "by 600 instead of by the 60 seconds in a minute."},
            {"text": "9 minutes", "correct": False,
             "why": "That divides the correct 180 seconds by 20 rather than "
             "by the 60 seconds in a minute."},
            {"text": "3 minutes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h19",
        "band": "harder",
        "text": "A student looks at two oscilloscope traces in the "
                "same window: one crowded with many small vibrations, one "
                "sparse with a few large ones. They conclude the crowded "
                "trace must be quieter, because its vibrations look smaller. "
                "Evaluate.",
        "options": [
            {"text": "This cannot be judged from crowding alone — height, "
            "not crowding, is what shows loudness, and the crowded trace's "
            "height has not been given", "correct": True},
            {"text": "Correct — more crowded traces read as quieter on this "
            "kind of screen", "correct": False,
             "why": "Crowding shows frequency; nothing about how crowded a "
             "trace is says anything about how tall, and so how loud, it is."},
            {"text": "Correct, since crowding is set by the amplitude in "
            "this type of diagram", "correct": False,
             "why": "Crowding is set by frequency, not amplitude; amplitude "
             "shows up as the height of the trace instead."},
            {"text": "Wrong — the crowded trace must be louder overall, "
            "since packing more vibrations into the same window carries more "
            "total energy than a sparser one would", "correct": False,
             "why": "How much energy each vibration carries depends on its "
             "own amplitude, which is not stated here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h20",
        "band": "harder",
        "text": "Source A is 150 Hz. Source B's frequency is 3 times "
                "Source A's. Source C's frequency is half of Source B's. "
                "Rank the three sources from lowest to highest pitch.",
        "options": [
            {"text": "A, then B, then C", "correct": False,
             "why": "Source C, at 225 Hz, sits between Source A's 150 Hz and "
             "Source B's 450 Hz, not above both."},
            {"text": "A, then C, then B", "correct": True},
            {"text": "C, then A, then B", "correct": False,
             "why": "Source A's 150 Hz is lower than Source C's 225 Hz, so A "
             "comes first, not second."},
            {"text": "B, then C, then A", "correct": False,
             "why": "This puts the highest frequency, Source B's 450 Hz, "
             "first instead of last."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h21",
        "band": "harder",
        "text": "A guitarist says: 'Plucking a string harder makes "
                "it swing through a wider arc, and a wider arc must mean "
                "more vibrations each second, since there is more distance "
                "to cover.' What is wrong with this reasoning?",
        "options": [
            {"text": "Nothing is wrong — a wider swing does need more "
            "vibrations to happen every second in order to keep up with the "
            "extra distance being covered each time", "correct": False,
             "why": "The string's own stiffness and length fix how often it "
             "swings, regardless of how wide each swing is."},
            {"text": "The reasoning is wrong simply because guitar strings "
            "cannot be plucked harder in a controlled way", "correct": False,
             "why": "A string can genuinely be plucked with more or less "
             "force; the flaw is in what that is assumed to change."},
            {"text": "It wrongly assumes a bigger swing must be completed "
            "more often; the string still completes the same number of full "
            "swings each second, just larger ones", "correct": True},
            {"text": "It is impossible to say without measuring the string's "
            "tension first", "correct": False,
             "why": "Tension is not needed here; the flaw in the reasoning "
             "can be seen without it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h22",
        "band": "harder",
        "text": "A machine's frequency is exactly 4 times a "
                "reference tone of 55 Hz. How many complete vibrations does "
                "the machine make in 1.5 seconds?",
        "options": [
            {"text": "82.5", "correct": False,
             "why": "That uses the reference tone's own frequency, 55 Hz, "
             "instead of the machine's 220 Hz."},
            {"text": "330 Hz", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: this is "
             "a plain count of vibrations."},
            {"text": "1320", "correct": False,
             "why": "That multiplies by 4 a second time, on top of already "
             "using the machine's correct frequency."},
            {"text": "330", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h23",
        "band": "harder",
        "text": "A student claims: 'Bigger instruments always make "
                "lower-pitched notes, so pitch is decided by the size of the "
                "instrument, not by its frequency.' Evaluate.",
        "options": [
            {"text": "Wrong — pitch is decided by frequency; a bigger "
            "instrument often vibrates more slowly, giving it a lower "
            "frequency, but it is the frequency, not the size directly, that "
            "fixes the pitch", "correct": True},
            {"text": "Correct — size alone decides pitch, and frequency is "
            "really just another name given to the same physical property "
            "that the size of an instrument already fixes on its own", "correct": False,
             "why": "Size and frequency are different things; size can "
             "influence frequency, but pitch itself is set by frequency."},
            {"text": "Correct, though this mainly applies to string "
            "instruments", "correct": False,
             "why": "The link between size and frequency is not confined to "
             "string instruments, and it is still frequency, not size, that "
             "fixes pitch."},
            {"text": "It cannot be evaluated without knowing the material "
            "each instrument is made from", "correct": False,
             "why": "The material affects how well an instrument sounds, not "
             "the basic link between frequency and pitch being tested here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h24",
        "band": "harder",
        "text": "A slow industrial vibration completes 10 800 cycles "
                "over exactly 2 hours. What is its frequency, in Hz?",
        "options": [
            {"text": "5400 Hz", "correct": False,
             "why": "That divides by 2 directly rather than converting the 2 "
             "hours into 7200 seconds first."},
            {"text": "1.5 Hz", "correct": True},
            {"text": "0.67 Hz", "correct": False,
             "why": "That divides the time by the count, the calculation the "
             "wrong way round."},
            {"text": "90 Hz", "correct": False,
             "why": "That converts the 2 hours into 120 minutes but stops "
             "there, without converting on to seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h25",
        "band": "harder",
        "text": "A sound engineer raises a signal's frequency and "
                "lowers its amplitude at the same time, by carefully chosen "
                "amounts. A student claims the two changes must cancel out, "
                "leaving the note completely unchanged. Evaluate.",
        "options": [
            {"text": "Correct — since one change goes up while the other "
            "goes down at the same time, the two effects on the note must "
            "balance out and leave it sounding completely unchanged overall", "correct": False,
             "why": "Pitch and loudness are separate qualities; a rise in "
             "one and a fall in the other does not undo either effect."},
            {"text": "Correct, provided the two changes are exactly "
            "proportional to each other", "correct": False,
             "why": "Even matched changes still raise the pitch and lower "
             "the loudness; the two effects happen on different qualities "
             "and cannot offset one another."},
            {"text": "Wrong — frequency and amplitude affect different "
            "qualities, pitch and loudness, so changing both changes both; "
            "neither change can cancel the other's separate effect", "correct": True},
            {"text": "It cannot be evaluated without knowing which dial was "
            "moved first", "correct": False,
             "why": "The order the dials are moved in makes no difference to "
             "the final pitch and loudness reached."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h26",
        "band": "harder",
        "text": "A note's frequency is 480 Hz. A second note has "
                "half that frequency, and lasts for 2.5 seconds. How many "
                "complete vibrations does the SECOND note make?",
        "options": [
            {"text": "1200", "correct": False,
             "why": "That uses the first note's frequency, 480 Hz, rather "
             "than the second note's 240 Hz."},
            {"text": "96", "correct": False,
             "why": "That divides the second note's frequency by the time "
             "rather than multiplying them together."},
            {"text": "240", "correct": False,
             "why": "That gives only the second note's frequency, forgetting "
             "to multiply by the 2.5 seconds it lasts."},
            {"text": "600", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h27",
        "band": "harder",
        "text": "A signal generator is set to 400 Hz, but its "
                "amplitude is turned all the way down to zero. What note is "
                "heard?",
        "options": [
            {"text": "None — with zero amplitude there is no vibration left "
            "to make a sound, whatever the frequency dial says", "correct": True},
            {"text": "A very quiet 400 Hz note, since the frequency dial "
            "still reads 400", "correct": False,
             "why": "With no amplitude at all there is nothing left to "
             "vibrate the air; a frequency reading alone makes no sound."},
            {"text": "A note at 0 Hz, since the amplitude and frequency "
            "readings have merged into one", "correct": False,
             "why": "The two dials remain separate; turning one down to zero "
             "does not change what the other one reads."},
            {"text": "A 400 Hz note at completely normal loudness, since "
            "frequency alone decides whether a note is heard", "correct": False,
             "why": "Amplitude, not frequency, decides whether there is any "
             "vibration at all to be heard."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h28",
        "band": "harder",
        "text": "A note's frequency is increased by 20%, from 500 Hz "
                "to 600 Hz, with the amplitude left unchanged. Which "
                "statement is correct?",
        "options": [
            {"text": "The note becomes higher-pitched and louder, since "
            "raising the frequency by that much also raises the amplitude", "correct": False,
             "why": "The amplitude is stated to be unchanged, so the "
             "loudness cannot have changed alongside the pitch."},
            {"text": "The note becomes higher-pitched only; its loudness is "
            "unaffected", "correct": True},
            {"text": "The note becomes quieter, since a higher frequency "
            "needs less energy in each vibration", "correct": False,
             "why": "With the amplitude unchanged, the loudness stays the "
             "same; it does not fall just because the frequency has risen."},
            {"text": "The note's pitch is unaffected, since a 20% change is "
            "too small to notice", "correct": False,
             "why": "A 20% rise in frequency, from 500 Hz to 600 Hz, is a "
             "clearly noticeable change in pitch."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h29",
        "band": "harder",
        "text": "An oscilloscope, window fixed at 25 ms, shows a "
                "trace with 5 complete vibrations, each one twice as tall as "
                "a reference trace of the same frequency. What is this "
                "trace's frequency, and how does its loudness compare with "
                "the reference?",
        "options": [
            {"text": "125 Hz, and it is quieter than the reference", "correct": False,
             "why": "5 vibrations across a 25 ms window gives 200 Hz, not "
             "125 Hz, and a taller trace is louder, not quieter."},
            {"text": "200 Hz, but exactly as loud as the reference", "correct": False,
             "why": "A taller trace shows a bigger amplitude, which makes "
             "the note louder than the reference, not equally loud."},
            {"text": "200 Hz, and it is louder than the reference", "correct": True},
            {"text": "25 Hz, and it is louder than the reference", "correct": False,
             "why": "That lifts the 25 straight out of the window's length "
             "in milliseconds and offers it as a frequency, instead of "
             "dividing the 5 vibrations by the 0.025 s window."},
        ],
        "figure": None,
    },
    {
        "id": "p6-05-h30",
        "band": "harder",
        "text": "A student writes this summary: 'Frequency and "
                "amplitude are just two different names for the same "
                "underlying vibration, so you can't really have one without "
                "changing the other.' Give the best correction.",
        "options": [
            {"text": "The summary is correct, and the whole point of the two "
            "words is that they describe one single thing", "correct": False,
             "why": "The truth is the opposite: frequency and amplitude are "
             "separate and independent of one another."},
            {"text": "The summary is correct for quiet sounds, but not for "
            "loud ones", "correct": False,
             "why": "There is no such split by loudness; frequency and "
             "amplitude are independent at every loudness."},
            {"text": "The summary is wrong mainly in the choice of words "
            "used, since in most ordinary instruments the two measurements "
            "do tend to rise and fall together in practice anyway", "correct": False,
             "why": "The two measurements do not rise and fall together; a "
             "note can get louder, quieter, higher or lower in any "
             "combination."},
            {"text": "They are two separate, independent measurements of the "
            "same vibration, how often it repeats and how far it swings, and "
            "either can change while the other stays fixed", "correct": True},
        ],
        "figure": None,
    },
]
