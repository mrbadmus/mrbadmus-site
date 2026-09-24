"""Physics · Space — `red-shift-big-bang`, the MRB-338 expansion.

The twenty rows already here take the headline facts twice over: what
red-shift is, what it shows, the age of the universe, the temperature of the
background radiation, the hydrogen-to-helium split, one forward Hubble
calculation and the no-centre misconception. So these 34 go to the parts of
the lesson nobody has examined.

The mechanism: the Doppler effect itself, on sound as well as light, and why
a measured spectral line rather than a galaxy's apparent colour is what
astronomers actually read. The law: what Hubble's Law states, the units and
value of the constant, and the two rearrangements — distance from speed, and
the constant from a speed and a distance, plus a shift read straight off a
spectral line as an absolute change, as a percentage and as a ratio between
two galaxies. The timeline: the opaque first few hundred thousand years, the
moment the universe turned transparent and let the background radiation out,
and the first stars.

And the honest edges of the model: what it does not explain, why 67 and 73
km/s/Mpc disagreeing is a live question rather than a scandal, and what a
sky full of blue-shifted galaxies would have meant.

10 / 12 / 12: the easier band was already eight deep on what red-shift shows,
so it takes the stated quantities and definitions it was missing, and the
reasoning and the arithmetic carry the weight at `standard` and `harder`.
"""

TOPIC = "space"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-red-shift-big-bang-e09",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by the Doppler effect.",
        "options": [
            "A change in the observed wavelength and frequency of a wave "
            "caused by motion of its source",
            "A change in the speed of a wave caused by motion of its source, "
            "so that the wave arrives late",
            "A change in the brightness of a wave caused by how far it has "
            "travelled",
            "A change in the direction of a wave caused by it crossing into "
            "a different material",
        ],
        "correct_index": 0,
        "why": "Relative motion between a source and an observer changes the "
               "wavelength and frequency the observer measures; the speed of "
               "the wave through space is unchanged.",
    },
    {
        "id": "ks4-red-shift-big-bang-e10",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what Hubble's Law says about the recession speed of a "
                "galaxy.",
        "options": [
            "It is inversely proportional to the galaxy's distance",
            "It is proportional to the galaxy's distance from Earth",
            "It depends on the galaxy's mass, because a heavier galaxy was "
            "given a bigger push to start with",
            "It is the same for every galaxy, however far away it is",
        ],
        "correct_index": 1,
        "why": "Hubble's Law is v = H₀d: recession speed is proportional to "
               "distance, so a galaxy twice as far away recedes twice as "
               "fast.",
    },
    {
        "id": "ks4-red-shift-big-bang-e11",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the units in which the Hubble constant is given.",
        "options": [
            "km/s",
            "Mpc/s",
            "km/s/Mpc",
            "km/Mpc",
        ],
        "correct_index": 2,
        "why": "H₀ is a speed per unit distance, so it is quoted in km/s per "
               "megaparsec — km/s/Mpc.",
    },
    {
        "id": "ks4-red-shift-big-bang-e12",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the approximate value of the Hubble constant.",
        "options": [
            "0.7 km/s/Mpc",
            "7 km/s/Mpc",
            "7000 km/s/Mpc",
            "70 km/s/Mpc",
        ],
        "correct_index": 3,
        "why": "The current best estimate is about 70 km/s/Mpc, so a galaxy "
               "1 Mpc away recedes at roughly 70 km/s.",
    },
    {
        "id": "ks4-red-shift-big-bang-e13",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the part of the electromagnetic spectrum in which the "
                "background radiation left over from the early universe is "
                "now found.",
        "options": [
            "Microwaves",
            "Radio waves",
            "Infrared",
            "Visible light",
        ],
        "correct_index": 0,
        "why": "It is detected as microwaves, which is why it is called the "
               "cosmic microwave background radiation.",
    },
    {
        "id": "ks4-red-shift-big-bang-e14",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State roughly how long after the Big Bang the universe "
                "cooled enough to become transparent.",
        "options": [
            "About one second",
            "About 380 000 years",
            "About 380 million years",
            "About 9 billion years",
        ],
        "correct_index": 1,
        "why": "After about 380 000 years the universe was cool enough for "
               "atoms to form, so light could travel freely for the first "
               "time.",
    },
    {
        "id": "ks4-red-shift-big-bang-e15",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the Big Bang theory says the universe was like at "
                "the very beginning.",
        "options": [
            "Cold and thin, and already its present size",
            "Empty, with matter appearing later to fill it",
            "Extremely hot, extremely dense and very small",
            "Made of the same stars and galaxies that we can see today",
        ],
        "correct_index": 2,
        "why": "The model begins with all the matter and energy of the "
               "universe in an extremely hot, extremely dense state about "
               "13.8 billion years ago.",
    },
    {
        "id": "ks4-red-shift-big-bang-e16",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the wavelengths of the sound waves "
                "reaching a listener as a siren moves away from them.",
        "options": [
            "They are squashed, so the note sounds higher",
            "They are unchanged, so the note sounds the same",
            "They are absorbed, so the note simply sounds quieter",
            "They are stretched, so the note sounds lower",
        ],
        "correct_index": 3,
        "why": "A receding source stretches the waves that reach the "
               "listener, lowering the pitch — the same Doppler effect that "
               "red-shifts light.",
    },
    {
        "id": "ks4-red-shift-big-bang-e17",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State roughly how long after the Big Bang the first stars "
                "and galaxies formed.",
        "options": [
            "Hundreds of millions of years",
            "Within the first year",
            "About 9 billion years",
            "About 13 billion years",
        ],
        "correct_index": 0,
        "why": "Gravity needed hundreds of millions of years to pull the gas "
               "into the first stars and galaxies.",
    },
    {
        "id": "ks4-red-shift-big-bang-e18",
        "subtopic_slug": "red-shift-big-bang",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State whether the Big Bang theory explains what caused the "
                "Big Bang.",
        "options": [
            "Yes — it shows that an earlier universe collapsed",
            "No — the original cause of the Big Bang is still unknown",
            "Yes — it shows that an explosion took place in space that was "
            "already there",
            "No — the microwave background has shown the whole theory to be "
            "wrong",
        ],
        "correct_index": 1,
        "why": "The model describes how the universe developed from an "
               "extremely hot, dense state onwards; what caused that state "
               "remains an open question.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-red-shift-big-bang-s07",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A galaxy recedes from Earth at 13 600 km/s. Taking the "
                "Hubble constant as 68 km/s/Mpc, determine its distance.",
        "options": [
            "0.005 Mpc",
            "20 Mpc",
            "200 Mpc",
            "920 000 Mpc",
        ],
        "correct_index": 2,
        "why": "Rearranging v = H₀d gives d = v ÷ H₀ = 13 600 ÷ 68 = 200 Mpc.",
    },
    {
        "id": "ks4-red-shift-big-bang-s08",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A spectral line emitted at 500 nm is observed from a galaxy "
                "at 550 nm. Determine the change in wavelength and state "
                "what it shows.",
        "options": [
            "A decrease of 50 nm, showing the galaxy is moving towards Earth",
            "An increase of 50 nm, showing the galaxy is moving towards Earth",
            "An increase of 1.1 nm, showing the galaxy is moving away from "
            "Earth",
            "An increase of 50 nm, showing the galaxy is moving away from "
            "Earth",
        ],
        "correct_index": 3,
        "why": "550 − 500 = 50 nm longer, which is a red-shift, so the galaxy "
               "is receding from Earth.",
    },
    {
        "id": "ks4-red-shift-big-bang-s09",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the radiation released by the hot early universe "
                "now reaches us as microwaves rather than as far more "
                "energetic radiation.",
        "options": [
            "The expansion of space has stretched its wavelength enormously "
            "while it travelled",
            "It has passed through so much cold gas that the gas took its "
            "energy",
            "Microwaves travel faster than other waves, so they are the first "
            "to arrive from that time",
            "The radiation has spread out through a far larger volume, which "
            "lowers the frequency of every wave in it",
        ],
        "correct_index": 0,
        "why": "Expansion stretches the wavelength of the radiation as it "
               "travels, so radiation that began extremely energetic is now "
               "cold microwaves at about 2.7 K.",
    },
    {
        "id": "ks4-red-shift-big-bang-s10",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the amounts of hydrogen and helium found in the "
                "oldest stars are treated as evidence for the Big Bang.",
        "options": [
            "They show that the oldest stars are still fusing hydrogen, which "
            "no other model allows",
            "The model predicted those amounts before they were measured, and "
            "the measurements agree",
            "They show that hydrogen is the lightest element, which is what "
            "the model rests on",
            "The amounts differ from star to star, matching the ages the "
            "model gives them",
        ],
        "correct_index": 1,
        "why": "Big Bang nucleosynthesis predicted roughly 75% hydrogen and "
               "25% helium by mass, and observations of the oldest stars "
               "match that prediction.",
    },
    {
        "id": "ks4-red-shift-big-bang-s11",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why astronomers treat the Big Bang model as well "
                "supported rather than as resting on red-shift alone.",
        "options": [
            "Red-shift is the least reliable measurement in astronomy, so it "
            "has to be propped up by other work",
            "Red-shift can be measured only for the galaxies nearest to "
            "Earth, so it cannot describe the universe",
            "Several independent observations all agree with the model, so "
            "they are unlikely to agree by chance",
            "The model was accepted long before red-shift was discovered, so "
            "red-shift plays no part in supporting it",
        ],
        "correct_index": 2,
        "why": "Red-shift, the microwave background and the hydrogen-helium "
               "abundance are separate lines of evidence that point the same "
               "way, which is far stronger than any one of them alone.",
    },
    {
        "id": "ks4-red-shift-big-bang-s12",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why light from the universe's first few hundred "
                "thousand years cannot reach Earth today.",
        "options": [
            "All the light from that time passed the Earth long ago, so none "
            "of it is left for us to detect",
            "Light had not yet been created then, because the first stars had "
            "not started to shine",
            "The light from that time has been stretched so far that it has "
            "turned into ordinary matter",
            "The universe was an opaque plasma then, so light could not "
            "travel freely through it",
        ],
        "correct_index": 3,
        "why": "Until atoms formed, the universe was a hot plasma that "
               "scattered light constantly, so no light from before that "
               "moment can reach us.",
    },
    {
        "id": "ks4-red-shift-big-bang-s13",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The light from a galaxy shows no red-shift and no "
                "blue-shift. Deduce what this tells you about its motion "
                "relative to Earth.",
        "options": [
            "It is neither approaching nor receding from Earth",
            "It is receding from Earth very quickly indeed",
            "It must lie at the exact centre of the universe, where nothing "
            "moves",
            "It is so far away that its light has lost all of its energy on "
            "the long journey",
        ],
        "correct_index": 0,
        "why": "A shift appears only when a source and an observer move "
               "apart or together, so no shift means no motion along the "
               "line of sight.",
    },
    {
        "id": "ks4-red-shift-big-bang-s14",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A spectral line emitted at 600 nm is observed from a galaxy "
                "at 618 nm. Calculate the percentage increase in the "
                "wavelength.",
        "options": [
            "18%",
            "3%",
            "0.03%",
            "30%",
        ],
        "correct_index": 1,
        "why": "The increase is 618 − 600 = 18 nm, and 18 ÷ 600 = 0.03, which "
               "is a 3% increase.",
    },
    {
        "id": "ks4-red-shift-big-bang-s15",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why astronomers measure red-shift from the lines in "
                "a galaxy's spectrum rather than from how red the galaxy "
                "looks.",
        "options": [
            "A galaxy's colour is set by how hot its stars are, so a "
            "red-shifted galaxy looks blue",
            "Spectral lines travel faster than the rest of a galaxy's light, "
            "so they show the shift first",
            "The lines come from known elements, so the change in their "
            "wavelength can be measured exactly",
            "Only the lines in a spectrum are red-shifted, and the rest of "
            "its light is unchanged",
        ],
        "correct_index": 2,
        "why": "Each element gives lines at known wavelengths, so comparing "
               "the observed wavelength with the laboratory one gives the "
               "shift as a measured number.",
    },
    {
        "id": "ks4-red-shift-big-bang-s16",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what the Big Bang model says happened to the "
                "temperature of the universe after the Big Bang.",
        "options": [
            "It stayed almost constant throughout",
            "It rose steadily as the first stars began to shine",
            "It fell at first and then rose again once galaxies began to "
            "collide with one another",
            "It fell steadily as the universe expanded, and is very low today",
        ],
        "correct_index": 3,
        "why": "The universe has cooled continuously as it expanded, which is "
               "why the radiation left from its hot early stage now arrives "
               "as cold microwaves.",
    },
    {
        "id": "ks4-red-shift-big-bang-s17",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the Big Bang model is described as a theory that "
                "new evidence could still change.",
        "options": [
            "Because a scientific model is kept only while it fits the "
            "observations, and new observations keep arriving",
            "Because scientists have already found evidence against it and "
            "have set that evidence aside",
            "Because a theory stays no more than a guess until it has been "
            "proved beyond any possibility of doubt",
            "Because the model was worked out from mathematics and has never "
            "been compared with any observation",
        ],
        "correct_index": 0,
        "why": "Scientific models are provisional: the Big Bang is accepted "
               "because it fits the evidence we have, and better evidence "
               "could force it to be changed.",
    },
    {
        "id": "ks4-red-shift-big-bang-s18",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A galaxy 250 Mpc from Earth recedes at 17 500 km/s. "
                "Determine the value of the Hubble constant from these data.",
        "options": [
            "0.014 km/s/Mpc",
            "70 km/s/Mpc",
            "4 375 000 km/s/Mpc",
            "7 km/s/Mpc",
        ],
        "correct_index": 1,
        "why": "Rearranging v = H₀d gives H₀ = v ÷ d = 17 500 ÷ 250 = 70 "
               "km/s/Mpc.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-red-shift-big-bang-h07",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The observable universe is about 93 billion light-years "
                "across, yet light has not had time to cross even a sixth "
                "of that. Suggest how this is possible.",
        "options": [
            "Light from the most distant galaxies travels much faster than "
            "light from the nearer ones",
            "Distances in space are measured outwards from a centre, so a "
            "diameter counts each side twice",
            "Space itself expanded while the light was travelling, carrying "
            "its source further away",
            "The universe must be about 93 billion years old, and its "
            "accepted age is an error",
        ],
        "correct_index": 2,
        "why": "Expansion keeps adding distance between us and a galaxy while "
               "its light is in flight, so the galaxy is now much further "
               "away than the light has travelled.",
    },
    {
        "id": "ks4-red-shift-big-bang-h08",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Big Bang model predicts that the universe should be "
                "about 25% helium by mass. Suggest what astronomers would "
                "have had to do if the oldest stars had been found to be 60% "
                "helium.",
        "options": [
            "Leave the model unchanged, because a prediction about helium is "
            "no part of the model",
            "Leave the model unchanged, and conclude that the measurement "
            "must be wrong",
            "Change the definition of helium, so that the prediction and the "
            "measurement then agreed",
            "Change or replace the model, because a prediction that fails "
            "counts as evidence against it",
        ],
        "correct_index": 3,
        "why": "A model is tested by its predictions: one that does not match "
               "measurement has to be modified or given up, which is exactly "
               "why the matching 25% carries weight.",
    },
    {
        "id": "ks4-red-shift-big-bang-h09",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A spectral line emitted at 400 nm arrives from galaxy X at "
                "404 nm and from galaxy Y at 416 nm. Determine which galaxy "
                "is further from Earth, and by roughly what factor.",
        "options": [
            "Y, by a factor of about 4, because recession speed is "
            "proportional to distance",
            "X, by a factor of about 4, because a smaller shift means a "
            "greater distance",
            "Y, by a factor of about 1.03, because the ratio of the observed "
            "wavelengths gives the ratio of distances",
            "Neither — they are the same distance away, because the emitted "
            "wavelength is the same for both",
        ],
        "correct_index": 0,
        "why": "The shifts are 4 nm and 16 nm, so Y recedes about four times "
               "as fast, and by Hubble's Law it is about four times as far "
               "away.",
    },
    {
        "id": "ks4-red-shift-big-bang-h10",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate this claim: 'Because the universe is expanding, the "
                "distance from the Earth to the Sun must be growing each "
                "year.'",
        "options": [
            "Correct — every distance in the universe grows at exactly the "
            "same rate as the universe expands",
            "Incorrect — the Earth and Sun are held together by gravity, and "
            "expansion is seen between distant galaxies",
            "Incorrect — the universe expands only where a red-shift has "
            "been measured",
            "Correct — though the growth is small, because the Sun's gravity "
            "halves the rate of the expansion",
        ],
        "correct_index": 1,
        "why": "Expansion shows itself between galaxies that are far apart; "
               "systems bound by gravity, such as the Solar System, hold "
               "together and do not expand with it.",
    },
    {
        "id": "ks4-red-shift-big-bang-h11",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Hubble constant is measured as about 67 km/s/Mpc by one "
                "method and about 73 km/s/Mpc by another. Suggest what "
                "scientists should conclude from this.",
        "options": [
            "One of the two teams must have falsified its data, since honest "
            "results would agree exactly",
            "The Hubble constant must be changing rapidly, since two "
            "measurements of it give different answers",
            "The value is not yet settled, and better measurements are needed "
            "to resolve the difference",
            "The average of the two, 70 km/s/Mpc, is certainly the true value "
            "and the difference can be ignored",
        ],
        "correct_index": 2,
        "why": "Two careful methods that disagree by more than their stated "
               "uncertainties mark an unfinished measurement — a question to "
               "work on, not a result to average away.",
    },
    {
        "id": "ks4-red-shift-big-bang-h12",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the Big Bang cannot be tested by repeating it in "
                "a laboratory, and describe how astronomers test it instead.",
        "options": [
            "It could be repeated in a laboratory, but only inside a particle "
            "accelerator large enough to hold it",
            "It cannot be tested, so the Big Bang is a matter of belief "
            "rather than of evidence",
            "It happened before time began, so astronomers test the model by "
            "working out what came before it",
            "It happened once only, so the model is tested by checking "
            "predictions it makes about what we observe",
        ],
        "correct_index": 3,
        "why": "A one-off event cannot be repeated, so the model earns its "
               "standing by predicting things that can then be looked for — "
               "the microwave background being the clearest case.",
    },
    {
        "id": "ks4-red-shift-big-bang-h13",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deduce what astronomers would conclude if most distant "
                "galaxies were found to be blue-shifted rather than "
                "red-shifted.",
        "options": [
            "That the universe is contracting, which the model in its present "
            "form does not describe",
            "That the Earth lies at the centre of the universe, with all the "
            "galaxies falling towards it",
            "That the light from those galaxies has travelled so far that it "
            "has gradually turned blue",
            "That the expansion has speeded up, because a faster expansion "
            "shifts light the other way",
        ],
        "correct_index": 0,
        "why": "Blue-shift means approach, so a sky of blue-shifted galaxies "
               "would mean the universe is shrinking rather than expanding, "
               "and the model would need rebuilding.",
    },
    {
        "id": "ks4-red-shift-big-bang-h14",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Light from a quasar set out 12 billion years ago and the "
                "universe is about 13.8 billion years old. Determine how long "
                "after the Big Bang that light was given out, and state what "
                "astronomers learn from it.",
        "options": [
            "1.8 billion years, and it shows them the quasar exactly as it "
            "stands at this moment",
            "1.8 billion years, and it shows them the universe as it was when "
            "it was young",
            "12 billion years, and it shows the universe when it was young",
            "25.8 billion years, and it shows a time before the Big Bang",
        ],
        "correct_index": 1,
        "why": "13.8 − 12 = 1.8 billion years, so the light carries a picture "
               "of the universe as it was very early in its history.",
    },
    {
        "id": "ks4-red-shift-big-bang-h15",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the cosmic microwave background is described as "
                "the oldest light that can be observed.",
        "options": [
            "It is the light of the very first stars, which were the first "
            "objects able to give out any light",
            "It has the longest wavelength of any radiation, and the longest "
            "waves take the longest to arrive",
            "It was released when the universe first became transparent, so "
            "nothing earlier can reach us",
            "It has been travelling since before the Big Bang, so it comes "
            "from earlier than anything else",
        ],
        "correct_index": 2,
        "why": "Before atoms formed the universe was opaque, so this "
               "radiation is the earliest light able to travel freely and "
               "reach a telescope.",
    },
    {
        "id": "ks4-red-shift-big-bang-h16",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why the Big Bang model does not describe what "
                "happened before the Big Bang.",
        "options": [
            "It was written to cover only the years since the Big Bang, and a "
            "longer version is being prepared",
            "Astronomers have chosen not to look further back, because those "
            "results would be too hard to publish",
            "Light from before the Big Bang has already passed the Earth, so "
            "that evidence is no longer available",
            "It describes the beginning of space and time, so there is no "
            "'before' for it to reach back into",
        ],
        "correct_index": 3,
        "why": "In the model space and time begin with the Big Bang, so the "
               "question of what came before falls outside what it can "
               "describe.",
    },
    {
        "id": "ks4-red-shift-big-bang-h17",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare what the red-shift of galaxies and the cosmic "
                "microwave background each tell astronomers about the "
                "universe.",
        "options": [
            "Red-shift shows the universe is expanding now; the background "
            "shows it was once hot and dense",
            "Red-shift shows the universe was once hot and dense; the "
            "background shows it is expanding now",
            "Both show only that the universe is expanding, so the "
            "background adds nothing to red-shift",
            "Red-shift shows how old the universe is; the background shows "
            "where its centre lies",
        ],
        "correct_index": 0,
        "why": "Red-shift is evidence about the universe now — it is getting "
               "bigger; the background radiation is evidence about its past — "
               "it was once hot and dense.",
    },
    {
        "id": "ks4-red-shift-big-bang-h18",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Galaxy R recedes at 10 200 km/s and galaxy S lies 400 Mpc "
                "from Earth. Taking the Hubble constant as 68 km/s/Mpc, "
                "determine which of the two is further from Earth.",
        "options": [
            "R, because a galaxy quoted by its speed is the more distant of "
            "a pair",
            "S, because R's distance works out as 150 Mpc",
            "R, because R's distance is 690 000 Mpc",
            "Neither — they are the same distance, because R's distance works "
            "out as 400 Mpc",
        ],
        "correct_index": 1,
        "why": "d = v ÷ H₀ = 10 200 ÷ 68 = 150 Mpc for R, which is well "
               "inside S's 400 Mpc, so S is the more distant galaxy.",
    },

    # ── standard, continued: the CMB's own temperature and cooling, the
    # steady-state rival, the Hubble constant as a graph gradient, why many
    # galaxies are needed, two fresh calculations, and Lemaître's priority ──
    {
        "id": "ks4-red-shift-big-bang-s19",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The cosmic microwave background radiation is measured "
                "today at about 2.7 K, yet it was released when the "
                "universe was around 3000 K. Explain why it has cooled "
                "so dramatically on its journey to us.",
        "options": [
            "The expansion of space has stretched its wavelength "
            "enormously since it was released, and a longer "
            "wavelength corresponds to a lower temperature",
            "The radiation has been steadily absorbed and re-emitted "
            "by the gas and dust of billions of galaxies it has "
            "passed through since it began travelling",
            "The radiation was measured incorrectly at the time it "
            "was released, and the true early temperature is now "
            "known to be much closer to 2.7 K",
            "Radiation naturally loses energy the further it travels "
            "through space, in the same way that sound gradually "
            "fades over a long enough distance",
        ],
        "correct_index": 0,
        "why": "Cosmic expansion stretches the wavelength of the "
               "radiation as it travels, and a longer wavelength means "
               "lower energy and so a lower equivalent temperature.",
    },
    {
        "id": "ks4-red-shift-big-bang-s20",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Before the 1960s, some astronomers supported a rival "
                "'steady-state' theory, in which the universe is "
                "expanding but has always looked the same on average, "
                "with new matter continuously created to fill the "
                "growing space. Explain why this theory lost support "
                "once the cosmic microwave background was discovered.",
        "options": [
            "The steady-state theory had in fact already predicted the "
            "exact temperature of the background radiation years "
            "before, so its discovery only strengthened that older "
            "model further",
            "A universe that has always looked the same has no hot, "
            "dense early phase to have left behind a leftover glow, "
            "so the background radiation had no natural explanation "
            "within it",
            "The steady-state theory was abandoned purely because more "
            "astronomers personally preferred the Big Bang model, "
            "rather than because of any new evidence",
            "The background radiation was found to come from a single "
            "nearby galaxy rather than from the whole sky, which "
            "neither theory had predicted at all",
        ],
        "correct_index": 1,
        "why": "The Big Bang model explains the background radiation "
               "directly, as the leftover glow of a hot early "
               "universe; a steady-state universe has no such episode "
               "to leave one behind.",
    },
    {
        "id": "ks4-red-shift-big-bang-s21",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Astronomers measure the distance and the recession "
                "speed of many different galaxies and plot recession "
                "speed against distance on a graph. Explain how the "
                "Hubble constant is obtained from this graph.",
        "options": [
            "It is read directly from the single highest speed plotted "
            "anywhere on the graph, ignoring every other galaxy with "
            "a lower recession speed than that one alone",
            "It is calculated by averaging the distances of every "
            "galaxy plotted, without using their recession speeds in "
            "the calculation at all",
            "It is the gradient of the straight line that best fits "
            "the plotted points, since Hubble's Law states that speed "
            "is proportional to distance",
            "It is found from the point where the line crosses the "
            "speed axis, which shows the recession speed at zero "
            "distance from Earth",
        ],
        "correct_index": 2,
        "why": "Since v = H₀d is a straight-line relationship through "
               "the origin, plotting v against d for many galaxies "
               "gives a line whose gradient is H₀ itself.",
    },
    {
        "id": "ks4-red-shift-big-bang-s22",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A nearby galaxy's own motion through space, caused by "
                "the pull of nearby galaxy clusters, can add several "
                "hundred km/s to or take several hundred km/s from "
                "its measured recession speed. Explain why astronomers "
                "use many galaxies rather than just one to find the "
                "Hubble constant.",
        "options": [
            "Using many galaxies allows astronomers to measure each "
            "one with a much less powerful, and therefore far "
            "cheaper, telescope than any single galaxy on its own "
            "would ever need",
            "A single galaxy can only ever be red-shifted, so several "
            "are needed before a genuine blue-shifted galaxy can be "
            "included in the data as well",
            "Every individual galaxy in the universe recedes at a "
            "completely different rate, so no pattern could ever "
            "emerge from studying only one of them",
            "One galaxy's own local motion can distort its measured "
            "speed, but averaging over many galaxies lets that random "
            "local motion cancel out, leaving the true underlying "
            "trend",
        ],
        "correct_index": 3,
        "why": "Local motion adds noise to any one galaxy's reading, "
               "but with many galaxies that noise tends to cancel out, "
               "revealing the genuine Hubble relationship underneath.",
    },
    {
        "id": "ks4-red-shift-big-bang-s23",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An absorption line with a rest wavelength of 500 nm is "
                "measured at 512 nm in the light from a quasar. "
                "Calculate the size of the wavelength shift caused by "
                "the redshift.",
        "options": [
            "12 nm",
            "500 nm",
            "512 nm",
            "1012 nm",
        ],
        "correct_index": 0,
        "why": "The shift is the observed wavelength minus the rest "
               "wavelength: 512 − 500 = 12 nm.",
    },
    {
        "id": "ks4-red-shift-big-bang-s24",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A quasar lies 150 Mpc from Earth. Using a Hubble constant "
                "of 70 km/s/Mpc, calculate its expected recession "
                "velocity.",
        "options": [
            "10 500 km/s",
            "2.1 km/s",
            "150 km/s",
            "1050 km/s",
        ],
        "correct_index": 0,
        "why": "v = H₀d = 70 × 150 = 10 500 km/s.",
    },
    {
        "id": "ks4-red-shift-big-bang-s25",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Georges Lemaître proposed an expanding universe "
                "originating from a single point, based on Einstein's "
                "equations, several years before Edwin Hubble's "
                "observations of galaxy red-shift were published. "
                "Explain what this tells you about how the Big Bang "
                "model developed.",
        "options": [
            "It tells you the model was accepted purely on Lemaître's "
            "mathematics alone, since observational evidence played "
            "no real part in establishing it",
            "It tells you Hubble's later observations were entirely "
            "unnecessary, since the theoretical prediction on its own "
            "was already more than enough to convince the whole "
            "scientific community",
            "It tells you the theoretical idea came first, and it was "
            "observational evidence — Hubble's red-shift measurements "
            "— that later gave it strong scientific support",
            "It tells you the two scientists worked on completely "
            "unrelated ideas, and it is only in modern textbooks that "
            "their separate work has been linked together",
        ],
        "correct_index": 2,
        "why": "Lemaître's mathematics proposed the expanding-universe "
               "idea; Hubble's later observations of red-shift then "
               "provided the evidence that idea needed to become "
               "widely accepted.",
    },
    {
        "id": "ks4-red-shift-big-bang-s26",
        "subtopic_slug": "red-shift-big-bang",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The cosmic microwave background radiation was "
                "discovered by chance in 1965. Explain why this "
                "discovery was treated as a turning point in the "
                "debate between the Big Bang model and the rival "
                "steady-state model.",
        "options": [
            "It proved that galaxies were red-shifted for the very "
            "first time, which neither model had previously been "
            "able to explain at all",
            "It showed that the universe contained far more hydrogen "
            "than either rival model had ever predicted, forcing both "
            "of them to be reworked completely from scratch",
            "It was immediately shown to have come from a single "
            "nearby star, which neither model could explain and both "
            "were abandoned as a result",
            "It supplied direct evidence of the hot, dense early "
            "universe the Big Bang model required, which the "
            "steady-state model had no way to account for",
        ],
        "correct_index": 3,
        "why": "The steady-state model had no hot early phase to leave "
               "behind such radiation, so its discovery counted "
               "heavily in the Big Bang model's favour.",
    },

    # ── harder, continued: the constant as a gradient, evaluating the
    # steady-state holdout, a single nearby galaxy's unreliable distance,
    # two quasars compared, Lemaître and Hubble's real roles, scatter in
    # real data, the stretch-factor honesty check, and what a rival theory
    # would still need to explain ─────────────────────────────────────────
    {
        "id": "ks4-red-shift-big-bang-h19",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "figure": "ks4-fig-graph-hubble-two-galaxies",
        "text": "The graph shows the recession speed of two galaxies against their distance from Earth, and the straight line through the origin that both lie on. Calculate the gradient of the line.",
        "options": [
            "70 km/s/Mpc",
            "35 km/s/Mpc",
            "7 km/s/Mpc",
            "700 km/s/Mpc",
        ],
        "correct_index": 0,
        "why": "Reading the two galaxies: (50 Mpc, 3500 km/s) and (150 Mpc, 10 500 km/s). Gradient = change in speed ÷ change in distance = (10 500 − 3500) ÷ (150 − 50) = 7000 ÷ 100 = 70 km/s/Mpc.",
    },
    {
        "id": "ks4-red-shift-big-bang-h20",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A scientist in 1966 argues that the steady-state model "
                "should be kept, since it can still explain galaxy "
                "red-shift just as well as the Big Bang model can. "
                "Evaluate this argument in light of the cosmic "
                "microwave background's discovery the previous year.",
        "options": [
            "The argument is sound, because red-shift is the only "
            "observation either model is ever required to explain, "
            "so both remain equally supported by the evidence",
            "The argument is weak: matching red-shift alone is no "
            "longer enough once one model also accounts for the "
            "background radiation and the other model does not",
            "The argument is sound, because the background radiation "
            "was later shown to be unrelated to either model and so "
            "should be set aside entirely from the debate",
            "The argument is weak, but only because steady-state "
            "theory had already been formally disproved decades "
            "earlier for a completely unconnected reason",
        ],
        "correct_index": 1,
        "why": "A model earns support by explaining everything "
               "observed, not just one line of evidence; once the "
               "background radiation favoured only one model, matching "
               "red-shift alone stopped being a sufficient defence.",
    },
    {
        "id": "ks4-red-shift-big-bang-h21",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A nearby galaxy is measured receding at only "
                "200 km/s. Using the Hubble constant of 70 km/s/Mpc, "
                "a student calculates its distance as under 3 Mpc, "
                "and treats this as an exact, reliable value. Evaluate "
                "the student's confidence in that figure.",
        "options": [
            "The confidence is justified, because Hubble's Law gives "
            "an exact distance for absolutely any galaxy, regardless "
            "of how nearby it happens to be",
            "The confidence is justified, because a low recession "
            "speed always means the measurement taken is inherently "
            "more accurate than a high recession speed measurement "
            "would ever turn out to be",
            "The confidence is misplaced: for a nearby, slow-moving "
            "galaxy, its own local motion can be a large fraction of "
            "the total measured speed, making the Hubble-Law distance "
            "unreliable",
            "The confidence is misplaced, because the Hubble constant "
            "does not apply to any galaxy inside our own galaxy "
            "cluster, however its speed is measured",
        ],
        "correct_index": 2,
        "why": "A small recession speed is easily distorted by a "
               "galaxy's own local motion, so the distance calculated "
               "from it alone carries much more uncertainty than the "
               "same calculation would for a fast-receding, distant "
               "galaxy.",
    },
    {
        "id": "ks4-red-shift-big-bang-h22",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Quasar P's light set out 10.5 billion years ago and "
                "quasar Q's light set out 13.2 billion years ago, in a "
                "universe now about 13.8 billion years old. Compare "
                "what each quasar's light shows astronomers, and state "
                "which shows the younger universe.",
        "options": [
            "Quasar P's light shows the younger universe, because it "
            "has had less total time to travel and so has changed "
            "less along the whole way on its very long journey to "
            "reach Earth",
            "Both quasars show the universe at exactly the same age, "
            "because both are being observed today, at the same "
            "moment in time",
            "Neither quasar's light can show anything about the age "
            "of the universe, because a quasar's own age can never be "
            "measured or estimated at all",
            "Quasar P's light shows the universe about 3.3 billion "
            "years after the Big Bang, and quasar Q's light shows it "
            "just 0.6 billion years after the Big Bang, so Q shows "
            "the younger universe",
        ],
        "correct_index": 3,
        "why": "13.8 − 10.5 = 3.3 billion years after the Big Bang for "
               "P, and 13.8 − 13.2 = 0.6 billion years after it for Q, "
               "so Q's light captures by far the younger universe.",
    },
    {
        "id": "ks4-red-shift-big-bang-h23",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A textbook states that 'Edwin Hubble alone discovered "
                "the expanding universe.' Evaluate this statement.",
        "options": [
            "The statement overstates Hubble's role: Georges Lemaître "
            "had already proposed an expanding universe from theory "
            "several years earlier, and Hubble's contribution was the "
            "crucial observational confirmation of it",
            "The statement is accurate, because Lemaître's work was "
            "published only after Hubble's observations and simply "
            "repeated what Hubble had already found",
            "The statement is accurate, because Hubble worked in "
            "complete isolation from every other astronomer and "
            "physicist working at the time",
            "The statement understates Hubble's role: in actual fact "
            "no theoretical prediction of any expanding universe at "
            "all existed anywhere before Hubble's own observations "
            "were first published",
        ],
        "correct_index": 0,
        "why": "Lemaître's theoretical proposal came first; Hubble's "
               "later observations of galaxy red-shift supplied the "
               "evidence that turned the idea into a strongly "
               "supported scientific model.",
    },
    {
        "id": "ks4-red-shift-big-bang-h24",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "figure": "ks4-fig-graph-hubble-forty-galaxies",
        "text": "The graph shows the recession speed of forty galaxies against their distance, with a straight line of best fit through the origin. Evaluate whether the scatter of the points about the line means Hubble's Law should be rejected.",
        "options": [
            "It should be rejected, because a genuine physical law would never, under any circumstances, allow a single point to lie above or below the line that it predicts",
            "It should not be rejected: some scatter is expected from each galaxy's own local motion adding to or subtracting from its recession speed, while the overall trend still supports the law",
            "It should be rejected, because forty galaxies is far too small a sample for any pattern in the data to be considered meaningful at all",
            "It should not be rejected, but only because the scatter proves that every galaxy's local motion is identical in size and always adds to its recession speed",
        ],
        "correct_index": 1,
        "why": "The points follow a clear straight-line trend, and they sit both above and below the line. Scatter like this is expected, because each galaxy's own local motion adds to or subtracts from its recession speed. What matters is the trend across many galaxies, so the law is supported, not rejected.",
    },
    {
        "id": "ks4-red-shift-big-bang-h25",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The cosmic microwave background's wavelength has been "
                "stretched by a factor of about 1100 since it was "
                "released, when the universe was about 380 000 years "
                "old; the universe is now about 13.8 billion years "
                "old. Evaluate the claim that this stretch factor "
                "should simply equal the ratio of the two ages, "
                "13.8 billion ÷ 380 000 ≈ 36 000.",
        "options": [
            "The claim is sound, and the mismatch between 1100 and "
            "36 000 shows that the accepted age of the universe must "
            "in fact be wrong",
            "The claim is sound, because wavelength stretching and "
            "time elapsed are always directly proportional to one "
            "another in any expanding system",
            "The claim is unsound: the rate at which space has "
            "expanded has not stayed constant throughout the "
            "universe's history, so a simple ratio of ages does not "
            "predict the stretch factor correctly",
            "The claim is unsound, because the stretch factor of "
            "1100 was in fact measured incorrectly, and its true "
            "value is now believed to be much closer to 36 000 than "
            "originally thought",
        ],
        "correct_index": 2,
        "why": "Expansion has sped up and slowed down at different "
               "points in cosmic history, so stretching cannot be "
               "read off as a simple ratio of two ages — a genuinely "
               "honest gap in the simplest version of the model.",
    },
    {
        "id": "ks4-red-shift-big-bang-h26",
        "subtopic_slug": "red-shift-big-bang",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A new theory claims to explain galaxy red-shift exactly "
                "as well as the Big Bang model does. Evaluate what "
                "else that theory would need to achieve before "
                "scientists would seriously consider it as a "
                "replacement for the Big Bang model.",
        "options": [
            "Nothing further would be needed, because matching the "
            "red-shift evidence alone is sufficient to replace any "
            "existing scientific model, however well supported",
            "It would need to disprove the existence of red-shift "
            "altogether, since that is the only evidence the Big Bang "
            "model actually depends on",
            "It would need the formal support of a clear majority of "
            "working astronomers voting in its favour, regardless of "
            "what evidence it did or did not actually go on to "
            "explain",
            "It would also need to account for the cosmic microwave "
            "background and the observed hydrogen-to-helium ratio, "
            "since the Big Bang model is supported by all three lines "
            "of evidence together",
        ],
        "correct_index": 3,
        "why": "The Big Bang model's strength comes from several "
               "independent lines of evidence agreeing at once; a "
               "rival matching only one of them, red-shift, has not "
               "yet matched the case for the model it hopes to "
               "replace.",
    },
]
