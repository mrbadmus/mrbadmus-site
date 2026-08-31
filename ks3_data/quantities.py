"""The core quantities the estate defines in more than one place.

⊕ **XU-1, ruled 28 Aug 2026 (MRB-295/MRB-298).** This module exists because
the estate held FOUR definitions of temperature, across three units and two
subjects, and three of them were wrong.

    P11 `temperature-and-internal-energy`  (Y7 HT6)  average kinetic energy
                                                     — CORRECT
    C1  `changes-of-state`                 (Y7 HT1)  "how fast the particles
                                                     are moving" — WRONG, and
                                                     a MARKING CRITERION
    P1  `heating-and-thermal-equilibrium`  (Y8 HT2)  "the average speed of the
                                                     particles" — WRONG, and
                                                     a MARKING CRITERION
    C7  `energy-and-changes-of-state`      (Y9 HT1)  "how fast the particles
                                                     are moving" — WRONG, and
                                                     the latent-heat argument
                                                     rests on it

The correct definition was met SECOND and outnumbered three to one, and the
wrong one earned credit at the first opportunity a child is marked, in the
first half-term of Year 7. Found by the physics audit's cold double-checker,
28 Aug 2026; chemistry's own audit of 25 Aug caught neither chemistry site.

**Why it lives here and not in a unit module.** It crosses two subjects, so it
needs ONE owner rather than two. The ruling was "one definition, authored once,
applied at all four sites" — this file is the once.

⚠️ **Why the definition is not just "average speed".** Temperature tracks
average KINETIC energy, not average speed. For one substance the two rise and
fall together, which is why "average speed" survives so long unchallenged; but
two gases at the SAME temperature have the same average kinetic energy and
different average speeds, because their particles have different masses. The
distinction is the one KS4 needs and the one an examiner marks.

⚠️ **"Kinetic energy" is glossed inline, deliberately.** The earliest site is
Year 7 half-term 1, where a child has probably not met the term. The gloss is
part of the string so that it cannot be dropped at the one site that needs it
most.

⚠️ This module is NOT a unit module. It is registered in
`ks3_data/__init__.py`'s `_NON_UNIT_MODULES`, so the unit discovery pass skips
it. Adding a constant here does not create a unit.
"""

# The definition, written once. Everything below is a grammatical form of
# this same sentence, so the four sites cannot drift apart again.
TEMPERATURE_IS = ("a measure of the average kinetic energy of the particles "
                  "— the energy they have because they are moving")

# A full sentence, for prose, key facts and reveals.
TEMPERATURE_SENTENCE = "Temperature is %s." % TEMPERATURE_IS

# A self-marking criterion, for the two produce/explain rungs that mark it.
TEMPERATURE_CRITERION = "Says temperature is %s." % TEMPERATURE_IS

# A multiple-choice option, which has to be short enough to sit beside its
# distractors without being the longest by a mile (MRB-177 length parity).
TEMPERATURE_OPTION = "The average kinetic energy of the particles"

# A vocabulary-card definition: the sentence, plus what a card has to add.
TEMPERATURE_VOCAB = (
    "A measure of the average kinetic energy of the particles in a substance "
    "— the energy they have because they are moving. Measured in degrees "
    "Celsius (°C). It does not depend on how much there is.")
