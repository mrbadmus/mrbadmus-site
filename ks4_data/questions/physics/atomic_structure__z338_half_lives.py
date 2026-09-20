"""Physics · Atomic structure — the MRB-338 expansion of `half-lives`.

One leaf only: AQA 8463 §6.4.2.3 — the definition of half-life, the (½)ⁿ rule
run forwards and backwards, the number of half-lives recovered from a ratio, the
percentage decayed as against the percentage remaining, the shape of a decay
curve, the fact that half-life is fixed for an isotope and cannot be altered by
heating, cooling, pressure or chemistry, and the background correction that has
to come first. The original twelve rows in `atomic_structure__a.py` take the
definition, the quarter after two half-lives, the randomness, iodine-131 over
one half-life, 2400 Bq over an hour, 8.0 × 10⁸ nuclei over three half-lives,
480 Bq to 60 Bq, the sixteenth, the midpoint of a twenty-hour fall, two sources
compared, a background-corrected half-life and the "decayed completely" error.

⚠️ **Every stem frame here is deliberately unlike the frames those twelve use.**
`set_work_scope_check` and `mrb338_leafcheck` fail a pair of stems at Jaccard
0.60 when both run to ten tokens or more, and "A source has an activity of X Bq
and a half-life of Y. Calculate its activity Z later" scores 0.67 against the
original `s01` on nothing but its frame — two different sums reading as one
question. So the calculations here are asked as count rates, as undecayed
nuclei, as masses, as percentages, as ratios and as "how many half-lives", and
the one existing number a row here might have wanted — iodine-131's eight days —
is left alone, because the original `e04` states it in its own stem (brief §9.6).

The weight follows the CONTENT. `easier` stays at eight: recall is one
definition, two named half-lives, the (½)ⁿ pattern and the one thing that cannot
change it. The demand lives in `standard` and `harder`, where the number of
half-lives has to be recovered from a ratio, or the background subtracted before
the halving can begin — so that is where the twenty-two-row bands sit.

Every value in the file is a power of two, so every answer comes out exactly.
The working lives in `why` and never in an option (brief §9.2).
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The one-step halving, the named half-lives, and the misconception that
    # heating a source changes it.
    {
        "id": "ks4-half-lives-e05",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether heating a radioactive source changes its "
                "half-life.",
        "options": [
            "Yes — heating shortens it, because warmer nuclei decay faster "
                "than cool ones do",
            "No — the half-life is fixed by the nucleus and nothing outside "
                "it alters the rate",
            "Yes — heating lengthens it, because the extra energy holds the "
                "nucleus together for longer",
            "Only for a gas, whose nuclei are free to move about as they are "
                "warmed",
        ],
        "correct_index": 1,
        "why": "Radioactive decay is spontaneous, so temperature, pressure "
               "and chemical state leave the half-life unchanged.",
    },
    {
        "id": "ks4-half-lives-e06",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how much of a radioactive sample is still undecayed "
                "once three half-lives have passed.",
        "options": [
            "One sixth of it, since three halvings take away three sixths",
            "One eighth of it",
            "Three eighths of it, one eighth surviving each half-life",
            "None of it, because three halvings use the whole sample up",
        ],
        "correct_index": 1,
        "why": "Each half-life halves what is left: ½ then ¼ then ⅛.",
    },
    {
        "id": "ks4-half-lives-e07",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate half-life of carbon-14.",
        "options": [
            "5730 days",
            "5730 hours",
            "573 years",
            "5730 years",
        ],
        "correct_index": 3,
        "why": "Carbon-14 has a half-life of about 5730 years, which is why it "
               "suits the dating of once-living material.",
    },
    {
        "id": "ks4-half-lives-e08",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample reads 800 Bq and its half-life is 4 hours. State "
                "the reading expected 4 hours later.",
        "options": [
            "0 Bq",
            "200 Bq",
            "400 Bq",
            "800 Bq",
        ],
        "correct_index": 2,
        "why": "One half-life has passed, so the activity has halved once: "
               "800 → 400 Bq.",
    },
    {
        "id": "ks4-half-lives-e09",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two quantities that fall to half their value during "
                "one half-life.",
        "options": [
            "The mass number and the atomic number of the nuclide",
            "The number of undecayed nuclei, and the activity",
            "The temperature of the sample, and its total mass",
            "The number of protons, and the number of electron shells",
        ],
        "correct_index": 1,
        "why": "Activity is proportional to the number of undecayed nuclei, so "
               "the two halve together.",
    },
    {
        "id": "ks4-half-lives-e10",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate half-life of technetium-99m.",
        "options": [
            "6 hours",
            "6 minutes",
            "6 days",
            "6 years",
        ],
        "correct_index": 0,
        "why": "Technetium-99m has a half-life of roughly 6 hours.",
    },
    {
        "id": "ks4-half-lives-e11",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two laboratories measure the half-life of the same isotope, "
                "one using a large sample and one a small sample. State what "
                "they should find.",
        "options": [
            "A shorter half-life for the large sample, since more nuclei "
                "means a faster rate of decay in it",
            "A longer half-life for the large sample, since it takes longer "
                "for so many more nuclei to decay away",
            "The same half-life, because it is a property of the isotope "
                "rather than of the amount present",
            "A different half-life each time, because decay is random and no "
                "two measurements can agree",
        ],
        "correct_index": 2,
        "why": "Half-life is fixed for a given isotope; a bigger sample has a "
               "higher activity but halves in the same time.",
    },
    {
        "id": "ks4-half-lives-e12",
        "subtopic_slug": "half-lives",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample holds 1000 undecayed nuclei of an isotope whose "
                "half-life is 2 days. State how many are left undecayed 2 "
                "days later.",
        "options": [
            "250",
            "500",
            "998",
            "0",
        ],
        "correct_index": 1,
        "why": "One half-life halves the number of undecayed nuclei: "
               "1000 → 500.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Half-lives counted out of a ratio, and the percentage-versus-fraction
    # pair that catches a pupil out.
    {
        "id": "ks4-half-lives-s05",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The activity of a sample is 6400 Bq and its half-life is 5 "
                "minutes. Determine the activity 20 minutes later.",
        "options": [
            "400 Bq",
            "800 Bq",
            "1600 Bq",
            "320 Bq",
        ],
        "correct_index": 0,
        "why": "20 ÷ 5 = 4 half-lives, and 6400 → 3200 → 1600 → 800 → 400 Bq.",
    },
    {
        "id": "ks4-half-lives-s06",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how many half-lives are needed to take an activity "
                "of 1600 Bq down to 200 Bq.",
        "options": [
            "8",
            "4",
            "3",
            "2",
        ],
        "correct_index": 2,
        "why": "1600 → 800 → 400 → 200 Bq, which is three halvings.",
    },
    {
        "id": "ks4-half-lives-s07",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source's half-life is 3 hours. Calculate the time needed "
                "for the number of undecayed nuclei to drop to one eighth of "
                "the number present at the start.",
        "options": [
            "24 hours",
            "6 hours",
            "12 hours",
            "9 hours",
        ],
        "correct_index": 3,
        "why": "One eighth is three halvings, and 3 × 3 hours = 9 hours.",
    },
    {
        "id": "ks4-half-lives-s08",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample contains 3.2 × 10⁶ undecayed nuclei of an isotope "
                "whose half-life is 10 years. Determine how many are left "
                "after 30 years.",
        "options": [
            "1.6 × 10⁶",
            "4.0 × 10⁵",
            "8.0 × 10⁵",
            "1.1 × 10⁶",
        ],
        "correct_index": 1,
        "why": "Three half-lives leave one eighth: 3.2 × 10⁶ ÷ 8 = "
               "4.0 × 10⁵.",
    },
    {
        "id": "ks4-half-lives-s09",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample's count rate drops from 960 counts per minute to 120 "
                "counts per minute over 12 hours. Determine its half-life.",
        "options": [
            "6 hours",
            "12 hours",
            "4 hours",
            "3 hours",
        ],
        "correct_index": 2,
        "why": "960 → 480 → 240 → 120 is three halvings, so 12 ÷ 3 = 4 hours.",
    },
    {
        "id": "ks4-half-lives-s10",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the half-life of an isotope cannot be shortened "
                "by any chemical or physical treatment.",
        "options": [
            "Because a chemical reaction can only reach the outer electrons "
                "of an atom and never the nucleus where decay happens",
            "Because the half-life of an isotope has been written into "
                "international tables and may not be altered afterwards",
            "Because chemical reactions release far too little energy to have "
                "any effect on the electrons of the atom at all",
            "Because any treatment that shortened the half-life would raise "
                "the activity, and activity is a fixed quantity",
        ],
        "correct_index": 0,
        "why": "Decay is a nuclear process and chemistry acts on electrons, so "
               "nothing a chemist or an oven can do reaches it.",
    },
    {
        "id": "ks4-half-lives-s11",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the percentage of the nuclei in a sample that have "
                "decayed by the end of two half-lives.",
        "options": [
            "50%",
            "25%",
            "75%",
            "100%",
        ],
        "correct_index": 2,
        "why": "A quarter is left undecayed, so three quarters — 75% — have "
               "decayed.",
    },
    {
        "id": "ks4-half-lives-s12",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the ratio of decayed nuclei to undecayed nuclei in "
                "a sample after three half-lives.",
        "options": [
            "3 : 1",
            "1 : 8",
            "7 : 1",
            "1 : 3",
        ],
        "correct_index": 2,
        "why": "One eighth is undecayed and seven eighths have decayed, so the "
               "ratio is 7 : 1.",
    },
    {
        "id": "ks4-half-lives-s13",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three half-lives after it was made, a source reads 500 Bq. "
                "Determine the activity it had when it was made.",
        "options": [
            "1500 Bq",
            "4000 Bq",
            "2000 Bq",
            "1000 Bq",
        ],
        "correct_index": 1,
        "why": "Working backwards, each half-life doubles the figure: "
               "500 → 1000 → 2000 → 4000 Bq.",
    },
    {
        "id": "ks4-half-lives-s14",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An isotope has a half-life of 20 minutes. Determine the "
                "fraction of a sample of it still undecayed 1 hour later.",
        "options": [
            "One third",
            "One eighth",
            "One quarter",
            "One twentieth",
        ],
        "correct_index": 1,
        "why": "60 ÷ 20 = 3 half-lives, and three halvings leave one eighth.",
    },
    {
        "id": "ks4-half-lives-s15",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a graph of activity against time for a "
                "radioactive source never quite reaches the time axis.",
        "options": [
            "Because the detector adds a small reading of its own that can "
                "never be taken away from the measurement",
            "Because each half-life removes only half of what is left, so "
                "some undecayed nuclei always remain",
            "Because the activity begins to rise again once it has fallen far "
                "enough towards the axis",
            "Because the axis of a graph is drawn at a value slightly above "
                "zero by convention",
        ],
        "correct_index": 1,
        "why": "Halving a quantity repeatedly makes it ever smaller without "
               "ever making it zero.",
    },
    {
        "id": "ks4-half-lives-s16",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source of half-life 6 days starts at 12 800 Bq. Determine "
                "its activity 24 days later.",
        "options": [
            "3200 Bq",
            "1600 Bq",
            "800 Bq",
            "400 Bq",
        ],
        "correct_index": 2,
        "why": "24 ÷ 6 = 4 half-lives: 12 800 → 6400 → 3200 → 1600 → 800 Bq.",
    },
    {
        "id": "ks4-half-lives-s17",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an isotope injected into a patient is chosen to "
                "have a half-life of only a few hours.",
        "options": [
            "So that its activity falls away quickly and the dose the "
                "patient receives stays small",
            "So that its activity climbs during the scan and the image "
                "becomes brighter as the minutes pass",
            "So that the hospital can buy it in bulk and keep it in store "
                "for as long as it is likely to be needed",
            "So that it decays into a second radioactive isotope, which then "
                "continues the measurement",
        ],
        "correct_index": 0,
        "why": "A short half-life means the source is soon inactive, so the "
               "patient is exposed for hours rather than for years.",
    },
    {
        "id": "ks4-half-lives-s18",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an isotope used to find the age of very old "
                "remains must have a half-life of thousands of years.",
        "options": [
            "Because a longer half-life makes the radiation emitted easier "
                "for a detector to pick up from a small sample",
            "Because an isotope with a short half-life would have decayed "
                "away almost completely and left nothing to measure",
            "Because the half-life of an isotope grows steadily longer as the "
                "sample containing it ages",
            "Because only an isotope of long half-life emits the gamma "
                "radiation that a dating measurement requires",
        ],
        "correct_index": 1,
        "why": "To measure an age the half-life has to be comparable with it, "
               "or too little of the isotope is left to compare.",
    },
    {
        "id": "ks4-half-lives-s19",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 100 g sample of an isotope has a half-life of 8 years. "
                "Determine the mass of the isotope left undecayed after 24 "
                "years.",
        "options": [
            "50 g",
            "25 g",
            "12.5 g",
            "33.3 g",
        ],
        "correct_index": 2,
        "why": "24 ÷ 8 = 3 half-lives, and 100 → 50 → 25 → 12.5 g.",
    },
    {
        "id": "ks4-half-lives-s20",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sixteen hours after it is measured at 640 Bq, a source reads "
                "40 Bq. Determine its half-life.",
        "options": [
            "8 hours",
            "2 hours",
            "16 hours",
            "4 hours",
        ],
        "correct_index": 3,
        "why": "640 → 320 → 160 → 80 → 40 Bq is four halvings, so "
               "16 ÷ 4 = 4 hours.",
    },
    {
        "id": "ks4-half-lives-s21",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate half-life of radon-222.",
        "options": [
            "3.8 days",
            "3.8 minutes",
            "3.8 years",
            "380 years",
        ],
        "correct_index": 0,
        "why": "Radon-222 has a half-life of about 3.8 days.",
    },
    {
        "id": "ks4-half-lives-s22",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what is meant by the undecayed nuclei in a sample.",
        "options": [
            "The nuclei that have already emitted radiation and become stable "
                "as a result of doing so",
            "The nuclei of the stable isotopes that happen to be mixed in "
                "with the radioactive material",
            "The nuclei that are still unstable and have yet to emit any "
                "radiation",
            "The nuclei that have lost their electrons and so carry an "
                "overall positive charge",
        ],
        "correct_index": 2,
        "why": "An undecayed nucleus is one that has not yet decayed, so it is "
               "still unstable and still contributes to the activity.",
    },
    {
        "id": "ks4-half-lives-s23",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two half-lives leave a quarter of the activity a source "
                "started with. Determine the percentage left after four "
                "half-lives.",
        "options": [
            "12.5%",
            "25%",
            "6.25%",
            "0%",
        ],
        "correct_index": 2,
        "why": "Four halvings leave one sixteenth, and 1 ÷ 16 × 100 = 6.25%.",
    },
    {
        "id": "ks4-half-lives-s24",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An isotope's half-life is 15 years. Determine the time its "
                "activity takes to drop to one thirty-second of the value it "
                "starts at.",
        "options": [
            "32 years",
            "480 years",
            "150 years",
            "75 years",
        ],
        "correct_index": 3,
        "why": "One thirty-second is five halvings, and 5 × 15 = 75 years.",
    },
    {
        "id": "ks4-half-lives-s25",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A detector reads 1280 counts per minute beside a source and "
                "160 counts per minute three hours later. Determine the "
                "half-life of the source.",
        "options": [
            "3 hours",
            "1 hour",
            "30 minutes",
            "90 minutes",
        ],
        "correct_index": 1,
        "why": "1280 → 640 → 320 → 160 is three halvings in 3 hours, so one "
               "half-life is 1 hour.",
    },
    {
        "id": "ks4-half-lives-s26",
        "subtopic_slug": "half-lives",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why scientists quote a half-life rather than the time "
                "a source takes to decay away entirely.",
        "options": [
            "Because the time to decay entirely is different for every "
                "sample of one isotope, while the half-life is the same",
            "Because the time to decay entirely can only be measured in a "
                "laboratory equipped to hold the source for years",
            "Because halving is easier arithmetic than dividing by any other "
                "number a scientist might have chosen",
            "Because halving always leaves some undecayed nuclei, so there is "
                "no definite time at which a source is finished",
        ],
        "correct_index": 3,
        "why": "Decay is exponential, so the activity approaches zero without "
               "reaching it and no finishing time exists to quote.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Backwards calculations, background subtracted first, and the hazard
    # comparison that turns on the length of the half-life.
    {
        "id": "ks4-half-lives-h05",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample whose half-life is 4 days shows a reading of 5000 "
                "Bq today. Calculate the reading 12 days from now.",
        "options": [
            "1250 Bq",
            "625 Bq",
            "2500 Bq",
            "417 Bq",
        ],
        "correct_index": 1,
        "why": "12 ÷ 4 = 3 half-lives: 5000 → 2500 → 1250 → 625 Bq.",
    },
    {
        "id": "ks4-half-lives-h06",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source of half-life 5 days now reads 90 Bq. Determine the "
                "reading it would have given 20 days ago.",
        "options": [
            "360 Bq",
            "1440 Bq",
            "450 Bq",
            "5.6 Bq",
        ],
        "correct_index": 1,
        "why": "20 ÷ 5 = 4 half-lives, and going back in time doubles four "
               "times: 90 → 180 → 360 → 720 → 1440 Bq.",
    },
    {
        "id": "ks4-half-lives-h07",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sources P and Q both begin at 4800 Bq. P has a half-life of "
                "2 hours and Q a half-life of 6 hours. Determine how much "
                "longer Q takes than P to fall to 600 Bq.",
        "options": [
            "12 hours",
            "4 hours",
            "18 hours",
            "6 hours",
        ],
        "correct_index": 0,
        "why": "600 Bq is three halvings for both, so P takes 6 hours and Q "
               "takes 18 hours — a difference of 12 hours.",
    },
    {
        "id": "ks4-half-lives-h08",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A detector beside a source reads 250 counts per minute, and "
                "30 minutes later it reads 130 counts per minute. The "
                "background in the room is 10 counts per minute. Determine the "
                "half-life of the source.",
        "options": [
            "15 minutes",
            "60 minutes",
            "45 minutes",
            "30 minutes",
        ],
        "correct_index": 3,
        "why": "Correcting first gives 240 and 120 counts per minute, one "
               "halving in 30 minutes, so the half-life is 30 minutes.",
    },
    {
        "id": "ks4-half-lives-h09",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A detector reads 420 counts per minute beside a source where "
                "the background is 20 counts per minute. Determine the reading "
                "it will give two half-lives later.",
        "options": [
            "105 counts per minute",
            "100 counts per minute",
            "125 counts per minute",
            "120 counts per minute",
        ],
        "correct_index": 3,
        "why": "The source alone is 400, which falls to 100 after two "
               "halvings, and the background of 20 is still there: "
               "100 + 20 = 120.",
    },
    {
        "id": "ks4-half-lives-h10",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'After ten half-lives a source has no "
                "activity left at all.'",
        "options": [
            "Sound — ten halvings is enough to use up every unstable nucleus "
                "a sample began with",
            "Unsound — after ten halvings about one thousandth of the "
                "activity remains, which is small but not nothing",
            "Sound — a source is defined as finished once ten half-lives have "
                "gone by, whatever the reading",
            "Unsound — after ten halvings the activity has in fact fallen to "
                "one tenth of where it started",
        ],
        "correct_index": 1,
        "why": "Ten halvings leave 1/1024 of the original activity — a very "
               "small fraction, but a measurable one.",
    },
    {
        "id": "ks4-half-lives-h11",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the smallest number of half-lives that takes the "
                "activity of a source below 1% of its starting value.",
        "options": [
            "4",
            "100",
            "7",
            "10",
        ],
        "correct_index": 2,
        "why": "Six halvings leave 1/64, which is 1.6%, and seven leave "
               "1/128, which is 0.78% — the first below 1%.",
    },
    {
        "id": "ks4-half-lives-h12",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the fraction of the original undecayed nuclei that "
                "is left once six half-lives have gone by.",
        "options": [
            "One twelfth",
            "One sixth",
            "One thirty-second",
            "One sixty-fourth",
        ],
        "correct_index": 3,
        "why": "Six halvings give (½)⁶, which is one sixty-fourth.",
    },
    {
        "id": "ks4-half-lives-h13",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample begins with 6.4 × 10¹⁰ undecayed nuclei. Determine "
                "how many are left after five half-lives.",
        "options": [
            "1.3 × 10¹⁰",
            "2.0 × 10⁹",
            "4.0 × 10⁹",
            "3.2 × 10⁹",
        ],
        "correct_index": 1,
        "why": "Five halvings leave one thirty-second: 6.4 × 10¹⁰ ÷ 32 = "
               "2.0 × 10⁹.",
    },
    {
        "id": "ks4-half-lives-h14",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a half-life read off a decay curve should be "
                "checked by taking a second pair of readings further along "
                "the curve.",
        "options": [
            "Because the half-life grows longer as a source ages, so the two "
                "values are expected to differ from one another",
            "Because a single pair could be misread, and a constant "
                "half-life means the second halving must take the same time",
            "Because the first halving of any source always takes longer "
                "than every halving that follows it",
            "Because the curve is a straight line at the start and only "
                "becomes a curve further along it",
        ],
        "correct_index": 1,
        "why": "Half-life is constant for an isotope, so two independent "
               "halvings must agree and disagreement means a reading error.",
    },
    {
        "id": "ks4-half-lives-h15",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An isotope's half-life is 25 minutes. Determine the fraction "
                "of it still undecayed after 2 hours and 5 minutes.",
        "options": [
            "One fifth",
            "One tenth",
            "One sixteenth",
            "One thirty-second",
        ],
        "correct_index": 3,
        "why": "2 hours 5 minutes is 125 minutes, and 125 ÷ 25 = 5 half-lives, "
               "leaving one thirty-second.",
    },
    {
        "id": "ks4-half-lives-h16",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 40 g sample of an isotope has a half-life of 12 hours. "
                "Determine the mass of it that has decayed after 36 hours.",
        "options": [
            "5 g",
            "20 g",
            "35 g",
            "30 g",
        ],
        "correct_index": 2,
        "why": "Three half-lives leave one eighth, which is 5 g, so "
               "40 − 5 = 35 g has decayed.",
    },
    {
        "id": "ks4-half-lives-h17",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two sources have equal activity today. One has a half-life "
                "of 1 hour and the other a half-life of 100 years. Compare "
                "the hazard each presents over the coming week.",
        "options": [
            "The one-hour source is the greater hazard for the week, having "
                "the shorter half-life of the two",
            "The hundred-year source is the greater hazard over the week, "
                "because its activity stays almost unchanged while the other "
                "falls away within a day",
            "The two present the same hazard all week, since their activities "
                "are equal at the start of it",
            "Neither presents any hazard after the first hour has passed, "
                "whatever half-life it happens to have",
        ],
        "correct_index": 1,
        "why": "The short-lived source is essentially gone within a day, while "
               "the long-lived one is still emitting at nearly its starting "
               "rate seven days later.",
    },
    {
        "id": "ks4-half-lives-h18",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'A source with a longer half-life "
                "is always the more dangerous of two sources.'",
        "options": [
            "Sound — a longer half-life means the source goes on emitting "
                "radiation for very much more time",
            "Unsound — it depends on the activity and the time considered: a "
                "long half-life means a low activity for a given number of "
                "nuclei",
            "Sound — half-life is the only property that decides how "
                "hazardous a radioactive source can be",
            "Unsound — a longer half-life in fact always makes a source the "
                "safer of the two, whatever else is true of it",
        ],
        "correct_index": 1,
        "why": "For the same number of nuclei a longer half-life means fewer "
               "decays each second, so hazard depends on activity, radiation "
               "type and exposure time together.",
    },
    {
        "id": "ks4-half-lives-h19",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In 18 days, 87.5% of the nuclei in a sample decay. Determine "
                "the half-life of the isotope.",
        "options": [
            "9 days",
            "6 days",
            "18 days",
            "3 days",
        ],
        "correct_index": 1,
        "why": "87.5% decayed leaves 12.5%, which is one eighth — three "
               "halvings — so 18 ÷ 3 = 6 days.",
    },
    {
        "id": "ks4-half-lives-h20",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An isotope's activity falls from 1.28 × 10⁴ Bq to 400 Bq in "
                "35 days. Determine its half-life.",
        "options": [
            "5 days",
            "35 days",
            "7 days",
            "12 days",
        ],
        "correct_index": 2,
        "why": "12 800 ÷ 400 = 32, which is five halvings, so "
               "35 ÷ 5 = 7 days.",
    },
    {
        "id": "ks4-half-lives-h21",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a half-life worked out from uncorrected count "
                "rates comes out longer than the true value.",
        "options": [
            "Because the background keeps the reading above zero, so the "
                "reading appears to halve more slowly than the source does",
            "Because background radiation decays alongside the source and so "
                "adds its own half-life to the measurement",
            "Because the detector counts each decay twice until the "
                "background has been subtracted from the total",
            "Because an uncorrected reading is always smaller than a "
                "corrected one, which makes the fall look slower",
        ],
        "correct_index": 0,
        "why": "The constant background is added to both readings, so the "
               "measured ratio is closer to 1 than the source's own, and the "
               "apparent halving takes longer.",
    },
    {
        "id": "ks4-half-lives-h22",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A waste isotope has a half-life of 24 000 years. Determine "
                "roughly how long its activity takes to fall to one sixteenth "
                "of its present value.",
        "options": [
            "96 000 years",
            "384 000 years",
            "48 000 years",
            "1500 years",
        ],
        "correct_index": 0,
        "why": "One sixteenth is four halvings, and 4 × 24 000 = 96 000 "
               "years.",
    },
    {
        "id": "ks4-half-lives-h23",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two samples of one isotope are prepared, the second "
                "containing twice as many nuclei as the first. Compare their "
                "activities and their half-lives.",
        "options": [
            "The second has twice the activity and twice the half-life, both "
                "scaling with the number of nuclei in it",
            "The second has twice the activity and the same half-life",
            "The second has the same activity and half the half-life, since "
                "the decays are shared among more nuclei",
            "Both the activity and the half-life are the same, because both "
                "samples are made of the same isotope",
        ],
        "correct_index": 1,
        "why": "Twice as many unstable nuclei give twice as many decays each "
               "second, but the fraction decaying — and so the half-life — is "
               "unchanged.",
    },
    {
        "id": "ks4-half-lives-h24",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source begins at 9.6 × 10⁵ Bq. Determine its activity after "
                "four half-lives.",
        "options": [
            "2.4 × 10⁵ Bq",
            "1.2 × 10⁵ Bq",
            "6.0 × 10⁴ Bq",
            "3.0 × 10⁴ Bq",
        ],
        "correct_index": 2,
        "why": "Four halvings divide by 16: 9.6 × 10⁵ ÷ 16 = 6.0 × 10⁴ Bq.",
    },
    {
        "id": "ks4-half-lives-h25",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures an isotope's half-life as 6 minutes, and "
                "gets 6 minutes again from a fresh sample a month later. "
                "Explain what this shows.",
        "options": [
            "That the sample used the second time was larger than the sample "
                "used the first time",
            "That the half-life of an isotope is a fixed property of it and "
                "does not change with time or with the sample",
            "That the detector has become steadily less sensitive over the "
                "month between the two measurements",
            "That the isotope stopped decaying between the two measurements "
                "and then began again",
        ],
        "correct_index": 1,
        "why": "Half-life is constant for a given isotope, so the same value "
               "is expected from any sample at any time.",
    },
    {
        "id": "ks4-half-lives-h26",
        "subtopic_slug": "half-lives",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample's activity falls from 6.4 × 10⁴ Bq to 2.0 × 10³ Bq. "
                "Determine how many half-lives have passed.",
        "options": [
            "32",
            "4",
            "5",
            "6",
        ],
        "correct_index": 2,
        "why": "64 000 ÷ 2000 = 32, and 32 is 2⁵, so five half-lives have "
               "passed.",
    },
]
