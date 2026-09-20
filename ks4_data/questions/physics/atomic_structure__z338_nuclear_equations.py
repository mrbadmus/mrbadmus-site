"""Physics · Atomic structure — the MRB-338 expansion of `nuclear-equations`.

One leaf only: AQA 8463 §6.4.2.2 — the symbols for the alpha and beta particles
and for a gamma ray, the rule that mass numbers and atomic numbers each balance
across a nuclear equation, the effect of each decay on the two numbers and on
the neutron count, and the reading of a chain of decays. The original twelve
rows in `atomic_structure__a.py` take caesium-137 by beta, an alpha from Z = 66,
the alpha symbol, a gamma from 60/27, polonium-210, strontium-90, the
nitrogen-to-oxygen identification, the neutron-to-proton mechanism, radon-220
followed by two betas, the two-step 214/83 chain, the stray-electron error and
the periodic-table comparison; this file takes what they leave — the beta
symbol's own two numbers, the three separate effects stated one at a time, the
change in the NEUTRON count (which the first twelve never ask), nine further
named nuclides, and the longer chains where the number of each decay has to be
recovered from the start and end nuclei alone.

⚠️ **Radium-226 and carbon-14 are deliberately absent.** Both are worked through
as examples in the lesson's own prose, so a row here asking for radon-222 from
radium-226, or nitrogen-14 from carbon-14, would hand back to a pupil the
arithmetic the page has already printed. The nuclides used instead — uranium-238,
thorium-234 and -232, americium-241, radon-222, plutonium-239, cobalt-60,
potassium-40, phosphorus-32, iodine-131, tritium, lead-214, bismuth-212,
sodium-24, technetium-99 — are all real, and every equation in the file balances
on both numbers.

The weight follows the CONTENT. `easier` stays at eight: recall here is two
symbols and the three rules, and a ninth way of asking "what happens to the mass
number" is the same question. The demand lives in `standard` and `harder`, where
a daughter has to be produced for a named parent, or a chain read backwards to
count the decays in it — so that is where the twenty-two-row bands sit.

Every wrong option carries its own FALSE reason at the key's level of detail
(brief §9.2/§9.9), and the wrong numbers are the errors a pupil actually makes:
dropping the mass number in beta decay, raising the atomic number in alpha
decay, subtracting 2 from the mass number instead of 4.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The beta symbol, the three rules one at a time, and what must balance.
    {
        "id": "ks4-nuclear-equations-e05",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A beta particle appears in a decay equation as a symbol "
                "carrying two small numbers. State the mass number and the "
                "atomic number written on it.",
        "options": [
            "Mass number 1 and atomic number −1",
            "Mass number 4 and atomic number 2",
            "Mass number 0 and atomic number −1",
            "Mass number 0 and atomic number +1",
        ],
        "correct_index": 2,
        "why": "A beta particle is an electron: its mass is negligible, so the "
               "mass number is 0, and its charge of −1 makes the atomic "
               "number −1.",
    },
    {
        "id": "ks4-nuclear-equations-e06",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the atomic number of a nucleus when it "
                "emits an alpha particle.",
        "options": [
            "It rises by 2",
            "It falls by 4",
            "It is unchanged",
            "It falls by 2",
        ],
        "correct_index": 3,
        "why": "An alpha particle carries away two protons, so the atomic "
               "number falls by 2.",
    },
    {
        "id": "ks4-nuclear-equations-e07",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "When alpha decay happens, state how the mass number of the "
                "nucleus changes.",
        "options": [
            "It falls by 4",
            "It falls by 2",
            "It is unchanged",
            "It rises by 4",
        ],
        "correct_index": 0,
        "why": "An alpha particle takes away two protons and two neutrons — "
               "four nucleons in all.",
    },
    {
        "id": "ks4-nuclear-equations-e08",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus emits a beta particle. State the effect of this on "
                "its mass number.",
        "options": [
            "It falls by 1",
            "It is unchanged",
            "It rises by 1",
            "It falls by 4",
        ],
        "correct_index": 1,
        "why": "A neutron becomes a proton, so the nucleon total stays the "
               "same and the mass number does not move.",
    },
    {
        "id": "ks4-nuclear-equations-e09",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which two quantities must balance on both sides of a "
                "nuclear equation.",
        "options": [
            "The number of electrons and the number of neutrons",
            "The mass numbers and the atomic numbers",
            "The number of protons and the number of electron shells",
            "The mass numbers and the number of neutrons",
        ],
        "correct_index": 1,
        "why": "The totals of the top numbers must match, and so must the "
               "totals of the bottom numbers.",
    },
    {
        "id": "ks4-nuclear-equations-e10",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which kind of emission leaves a nucleus as the same "
                "element it was before.",
        "options": [
            "Alpha emission, because the two protons lost are replaced from "
                "elsewhere in the nucleus",
            "Beta emission, because the electron emitted came from an outer "
                "shell and not from the nucleus",
            "Gamma emission",
            "All three of them leave the element unchanged",
        ],
        "correct_index": 2,
        "why": "A gamma ray carries away energy but no nucleons and no "
               "charge, so neither number changes and the element is the same.",
    },
    {
        "id": "ks4-nuclear-equations-e11",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus of mass number 24 and atomic number 11 emits a "
                "beta particle. State the atomic number of the nucleus left "
                "behind.",
        "options": [
            "10",
            "9",
            "11",
            "12",
        ],
        "correct_index": 3,
        "why": "Beta decay raises the atomic number by 1, so 11 becomes 12.",
    },
    {
        "id": "ks4-nuclear-equations-e12",
        "subtopic_slug": "nuclear-equations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the symbol used for a gamma ray in a nuclear equation.",
        "options": [
            "α",
            "γ",
            "β",
            "n",
        ],
        "correct_index": 1,
        "why": "Gamma radiation is written as the Greek letter gamma, γ, and "
               "carries no mass number or atomic number.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # A daughter produced for nine named parents, and the neutron count.
    {
        "id": "ks4-nuclear-equations-s05",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Complete this decay equation: 238/92 U → X + 4/2 He. State "
                "the mass number and the proton number of X.",
        "options": [
            "Mass number 234, atomic number 94",
            "Mass number 236, atomic number 90",
            "Mass number 234, atomic number 90",
            "Mass number 238, atomic number 90",
        ],
        "correct_index": 2,
        "why": "238 − 4 = 234 and 92 − 2 = 90, which is thorium-234.",
    },
    {
        "id": "ks4-nuclear-equations-s06",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thorium-234 nucleus contains 90 protons. It undergoes beta "
                "decay. State the mass number and atomic number of the "
                "daughter nuclide.",
        "options": [
            "Mass number 233, atomic number 91",
            "Mass number 234, atomic number 89",
            "Mass number 230, atomic number 88",
            "Mass number 234, atomic number 91",
        ],
        "correct_index": 3,
        "why": "Beta decay leaves the mass number at 234 and raises the "
               "atomic number to 91, which is protactinium-234.",
    },
    {
        "id": "ks4-nuclear-equations-s07",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alpha particle leaves an americium-241 nucleus that began "
                "with 95 protons. Calculate the mass number and atomic number "
                "of the nuclide remaining.",
        "options": [
            "Mass number 241, atomic number 93",
            "Mass number 237, atomic number 97",
            "Mass number 239, atomic number 93",
            "Mass number 237, atomic number 93",
        ],
        "correct_index": 3,
        "why": "241 − 4 = 237 and 95 − 2 = 93, which is neptunium-237.",
    },
    {
        "id": "ks4-nuclear-equations-s08",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Balance the nuclear equation 60/27 Co → X + 0/−1 e by "
                "determining the mass number and atomic number of X.",
        "options": [
            "Mass number 60, atomic number 26",
            "Mass number 60, atomic number 28",
            "Mass number 59, atomic number 28",
            "Mass number 56, atomic number 25",
        ],
        "correct_index": 1,
        "why": "The mass number stays at 60 and the atomic number rises to "
               "28, which is nickel-60.",
    },
    {
        "id": "ks4-nuclear-equations-s09",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the unknown nuclide X in this decay: 40/19 K → X + "
                "0/−1 e.",
        "options": [
            "Mass number 39, atomic number 20",
            "Mass number 40, atomic number 18",
            "Mass number 40, atomic number 20",
            "Mass number 36, atomic number 17",
        ],
        "correct_index": 2,
        "why": "Beta decay holds the mass number at 40 and takes the atomic "
               "number to 20, which is calcium-40.",
    },
    {
        "id": "ks4-nuclear-equations-s10",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Phosphorus-32 has 15 protons and is used as a medical "
                "tracer. Predict the mass number and atomic number of the "
                "nucleus formed when it emits a beta particle.",
        "options": [
            "Mass number 31, atomic number 16",
            "Mass number 32, atomic number 14",
            "Mass number 28, atomic number 13",
            "Mass number 32, atomic number 16",
        ],
        "correct_index": 3,
        "why": "32 stays, and 15 + 1 = 16, which is sulfur-32.",
    },
    {
        "id": "ks4-nuclear-equations-s11",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The equation 131/53 I → X + 0/−1 e represents the beta decay "
                "of iodine-131. State what the mass number and atomic number "
                "of X must be.",
        "options": [
            "Mass number 131, atomic number 52",
            "Mass number 130, atomic number 54",
            "Mass number 131, atomic number 54",
            "Mass number 127, atomic number 51",
        ],
        "correct_index": 2,
        "why": "The mass number is unchanged at 131 and the atomic number "
               "rises to 54, which is xenon-131.",
    },
    {
        "id": "ks4-nuclear-equations-s12",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Radon-222 gas has 86 protons in each nucleus. One such "
                "nucleus throws out an alpha particle. Calculate the mass "
                "number and atomic number of what is left.",
        "options": [
            "Mass number 220, atomic number 84",
            "Mass number 218, atomic number 88",
            "Mass number 222, atomic number 84",
            "Mass number 218, atomic number 84",
        ],
        "correct_index": 3,
        "why": "222 − 4 = 218 and 86 − 2 = 84, which is polonium-218.",
    },
    {
        "id": "ks4-nuclear-equations-s13",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plutonium-239 nucleus, atomic number 94, loses an alpha "
                "particle. Predict the mass number and atomic number of the "
                "nuclide produced.",
        "options": [
            "Mass number 235, atomic number 92",
            "Mass number 237, atomic number 92",
            "Mass number 239, atomic number 92",
            "Mass number 235, atomic number 96",
        ],
        "correct_index": 0,
        "why": "239 − 4 = 235 and 94 − 2 = 92, which is uranium-235.",
    },
    {
        "id": "ks4-nuclear-equations-s14",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the atomic number of a beta particle is written "
                "as −1 in a nuclear equation.",
        "options": [
            "Because the beta particle removes one nucleon from the nucleus "
                "as it leaves, so one has to be taken off the total",
            "Because the beta particle is emitted in the direction opposite "
                "to the one an alpha particle would take",
            "Because the beta particle has a mass slightly smaller than "
                "nothing, which the minus sign is there to record",
            "Because the beta particle is an electron carrying a charge of "
                "−1, and the lower number records charge",
        ],
        "correct_index": 3,
        "why": "The lower number in nuclear notation is the charge in units "
               "of the proton charge, and an electron's is −1.",
    },
    {
        "id": "ks4-nuclear-equations-s15",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how many neutrons a nucleus loses when it emits an "
                "alpha particle.",
        "options": [
            "4",
            "0",
            "2",
            "1",
        ],
        "correct_index": 2,
        "why": "An alpha particle is two protons and two neutrons, so two "
               "neutrons leave with it.",
    },
    {
        "id": "ks4-nuclear-equations-s16",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how the number of neutrons in a nucleus changes "
                "when it emits a beta particle.",
        "options": [
            "It rises by 1, since a proton has become a neutron inside the "
                "nucleus",
            "It falls by 1",
            "It does not change, because the mass number does not change "
                "either",
            "It falls by 2, in the same way as it does in alpha decay",
        ],
        "correct_index": 1,
        "why": "One neutron turns into a proton, so the neutron count drops "
               "by one while the nucleon total stays the same.",
    },
    {
        "id": "ks4-nuclear-equations-s17",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why gamma emission leaves a nucleus as the same "
                "element.",
        "options": [
            "Because a gamma ray takes away a proton and a neutron together, "
                "so the two changes cancel each other out",
            "Because a gamma ray is emitted from the electron shells of the "
                "atom rather than from the nucleus at all",
            "Because a gamma ray carries away energy but no nucleons and no "
                "charge, so the atomic number is unaltered",
            "Because a gamma ray is reabsorbed by the nucleus almost at once, "
                "which puts back whatever it had removed",
        ],
        "correct_index": 2,
        "why": "The element is fixed by the proton number, and a gamma ray "
               "changes neither the protons nor the neutrons.",
    },
    {
        "id": "ks4-nuclear-equations-s18",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus of mass number 212 and atomic number 83 changes "
                "into one of mass number 208 and atomic number 81. Determine "
                "which decay has taken place.",
        "options": [
            "Beta decay, because the atomic number has changed by one place "
                "in the periodic table",
            "Gamma emission, because the nucleus has kept the same number of "
                "particles throughout",
            "Two beta decays in succession, because the atomic number has "
                "fallen by two",
            "Alpha decay",
        ],
        "correct_index": 3,
        "why": "The mass number has fallen by 4 and the atomic number by 2, "
               "which is exactly alpha emission.",
    },
    {
        "id": "ks4-nuclear-equations-s19",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus containing 43 protons and 56 neutrons changes into "
                "one with 44 protons and 55 neutrons. State the type of "
                "emission responsible.",
        "options": [
            "Alpha decay, because the element has changed from one to "
                "another",
            "Gamma emission, because the mass number has stayed exactly as "
                "it was",
            "Alpha decay followed by two beta decays, because the atomic "
                "number has risen overall",
            "Beta decay",
        ],
        "correct_index": 3,
        "why": "An unchanged mass number with the atomic number up by one is "
               "the signature of beta emission.",
    },
    {
        "id": "ks4-nuclear-equations-s20",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how many places an element moves in the periodic "
                "table, and in which direction, when its nucleus emits an "
                "alpha particle.",
        "options": [
            "Four places to the left, one for each nucleon that the alpha "
                "particle has carried away with it",
            "Two places to the left",
            "Two places to the right, because the nucleus has become more "
                "stable than it was",
            "It does not move at all, because an alpha particle carries away "
                "no charge of its own",
        ],
        "correct_index": 1,
        "why": "The atomic number falls by 2 and the periodic table is "
               "ordered by atomic number, so the element moves two places "
               "left.",
    },
    {
        "id": "ks4-nuclear-equations-s21",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the atomic numbers on the two sides of a nuclear "
                "equation must add up to the same total.",
        "options": [
            "Because the total number of nucleons in the nucleus can never "
                "change during a decay of any kind",
            "Because the atomic number is always the smaller of the two "
                "figures and small numbers are easier to balance",
            "Because charge is conserved, and the lower number records the "
                "charge each particle carries",
            "Because the periodic table has a fixed number of places and "
                "none of them may be left empty",
        ],
        "correct_index": 2,
        "why": "The lower number is charge in units of the proton charge, and "
               "charge is conserved in every nuclear change.",
    },
    {
        "id": "ks4-nuclear-equations-s22",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Tritium is hydrogen-3 and has atomic number 1. It decays by "
                "beta emission. Determine the mass number and the atomic "
                "number of the daughter nucleus.",
        "options": [
            "Mass number 2, atomic number 2",
            "Mass number 3, atomic number 0",
            "Mass number 3, atomic number 2",
            "Mass number 1, atomic number 1",
        ],
        "correct_index": 2,
        "why": "The mass number stays at 3 and the atomic number rises to 2, "
               "giving helium-3.",
    },
    {
        "id": "ks4-nuclear-equations-s23",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Thorium-232 sits at the head of a decay series and has 90 "
                "protons. Its first step is alpha emission. State the mass "
                "number and atomic number of the product.",
        "options": [
            "Mass number 230, atomic number 88",
            "Mass number 228, atomic number 92",
            "Mass number 228, atomic number 88",
            "Mass number 232, atomic number 88",
        ],
        "correct_index": 2,
        "why": "232 − 4 = 228 and 90 − 2 = 88, which is radium-228.",
    },
    {
        "id": "ks4-nuclear-equations-s24",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what leaves the nucleus during alpha decay.",
        "options": [
            "A single proton, together with the electron that had been "
                "paired with it inside the nucleus",
            "Two protons and two neutrons, bound together as one particle",
            "Two protons on their own, the neutrons of the nucleus staying "
                "exactly where they were",
            "Four neutrons at once, which is why the mass number falls by as "
                "much as four",
        ],
        "correct_index": 1,
        "why": "An alpha particle is a helium-4 nucleus — two protons and two "
               "neutrons leaving together.",
    },
    {
        "id": "ks4-nuclear-equations-s25",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "When a lead-214 nucleus, which holds 82 protons, emits a "
                "beta particle, determine the mass number and atomic number "
                "of the nucleus that results.",
        "options": [
            "Mass number 214, atomic number 81",
            "Mass number 214, atomic number 83",
            "Mass number 213, atomic number 83",
            "Mass number 210, atomic number 80",
        ],
        "correct_index": 1,
        "why": "214 is unchanged and 82 + 1 = 83, which is bismuth-214.",
    },
    {
        "id": "ks4-nuclear-equations-s26",
        "subtopic_slug": "nuclear-equations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus of mass number 234 and atomic number 90 becomes "
                "one of mass number 230 and atomic number 88. Determine which "
                "particle was emitted.",
        "options": [
            "An alpha particle",
            "A beta particle, since the element has changed into another one",
            "A gamma ray, since no charged particle has left the nucleus at "
                "all",
            "A neutron, since the mass number has fallen while the atomic "
                "number stayed put",
        ],
        "correct_index": 0,
        "why": "A fall of 4 in the mass number and 2 in the atomic number is "
               "an alpha particle leaving.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Chains read forwards and backwards, and the errors that pass a
    # careless balance check.
    {
        "id": "ks4-nuclear-equations-h05",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Uranium-238, atomic number 92, begins a chain: first an "
                "alpha particle is released, then two beta particles one "
                "after the other. Determine the mass number and atomic number "
                "at the end of the chain.",
        "options": [
            "Mass number 234, atomic number 88",
            "Mass number 232, atomic number 92",
            "Mass number 238, atomic number 90",
            "Mass number 234, atomic number 92",
        ],
        "correct_index": 3,
        "why": "238/92 → 234/90 by alpha, then 234/91 and 234/92 as each beta "
               "raises the atomic number by one.",
    },
    {
        "id": "ks4-nuclear-equations-h06",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two alpha particles are released one after the other from an "
                "americium-241 nucleus that starts with 95 protons. Determine "
                "the mass number and atomic number of the nucleus left.",
        "options": [
            "Mass number 233, atomic number 95",
            "Mass number 237, atomic number 91",
            "Mass number 233, atomic number 91",
            "Mass number 239, atomic number 93",
        ],
        "correct_index": 2,
        "why": "Two alpha decays take 8 from the mass number and 4 from the "
               "atomic number: 241 − 8 = 233 and 95 − 4 = 91.",
    },
    {
        "id": "ks4-nuclear-equations-h07",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus of mass number 238 and atomic number 92 decays in "
                "several steps into one of mass number 226 and atomic number "
                "88. Determine how many alpha and how many beta decays this "
                "took.",
        "options": [
            "Three alpha decays and two beta decays",
            "Three alpha decays and no beta decays",
            "Twelve alpha decays and four beta decays",
            "Two alpha decays and four beta decays",
        ],
        "correct_index": 0,
        "why": "The mass number falls by 12, which needs three alphas; those "
               "would take the atomic number to 86, so two betas are needed "
               "to bring it back up to 88.",
    },
    {
        "id": "ks4-nuclear-equations-h08",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Starting from a nuclide with 92 protons and 235 nucleons, a "
                "decay series ends at a nuclide with 82 protons and 207 "
                "nucleons. Determine the number of alpha emissions and the "
                "number of beta emissions in the series.",
        "options": [
            "Seven alpha decays and no beta decays",
            "Four alpha decays and seven beta decays",
            "Twenty-eight alpha decays and ten beta decays",
            "Seven alpha decays and four beta decays",
        ],
        "correct_index": 3,
        "why": "28 ÷ 4 = 7 alpha decays, which would drop the atomic number "
               "by 14 to 78, so 4 beta decays are needed to raise it to 82.",
    },
    {
        "id": "ks4-nuclear-equations-h09",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why alpha decay reduces both the proton count and "
                "the neutron count of a nucleus by exactly two.",
        "options": [
            "Because two protons are emitted and two neutrons decay into "
                "protons at the same moment as they go",
            "Because the alpha particle emitted is itself made of two "
                "protons and two neutrons bound together",
            "Because the nucleus has to shed equal numbers of each kind of "
                "particle in order to stay electrically neutral",
            "Because four nucleons leave and the nucleus always divides them "
                "into equal halves as it does so",
        ],
        "correct_index": 1,
        "why": "The particle that leaves is a helium-4 nucleus, so exactly "
               "two protons and two neutrons go with it.",
    },
    {
        "id": "ks4-nuclear-equations-h10",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that a nucleus of mass number 238 and "
                "atomic number 92 decays into one of mass number 234 and "
                "atomic number 90, plus an alpha particle and a gamma ray. "
                "Determine whether the equation balances.",
        "options": [
            "No — a gamma ray has a mass number of 1, so the top line is out "
                "by one",
            "No — an alpha particle and a gamma ray cannot be emitted in the "
                "same decay as one another",
            "No — the gamma ray carries a charge of −1, so the bottom line "
                "does not add up",
            "Yes — 234 + 4 = 238 and 90 + 2 = 92, and a gamma ray adds "
                "nothing to either total",
        ],
        "correct_index": 3,
        "why": "The alpha accounts for the whole change and the gamma ray has "
               "a mass number and an atomic number of zero.",
    },
    {
        "id": "ks4-nuclear-equations-h11",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that sodium-24, atomic number 11, decays to "
                "magnesium-24, atomic number 12, by emitting a particle of "
                "mass number 0 and atomic number +1. Explain the error.",
        "options": [
            "The mass number of the emitted particle should be 4 rather than "
                "0, since every emitted particle carries nucleons",
            "The emitted particle should have atomic number −1, since 11 = "
                "12 + (−1) is what makes the bottom line balance",
            "The daughter's atomic number should be 10, because a beta "
                "particle lowers the atomic number by one",
            "There is no error at all — a beta particle is written with an "
                "atomic number of +1",
        ],
        "correct_index": 1,
        "why": "A beta particle is 0/−1, and 12 + (−1) = 11 balances the "
               "bottom line, whereas 12 + 1 = 13 does not.",
    },
    {
        "id": "ks4-nuclear-equations-h12",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bismuth-212 nucleus, which holds 83 protons, loses an "
                "alpha particle. The nuclide produced is itself unstable and "
                "gives out a beta particle. State the mass number and atomic "
                "number at the end.",
        "options": [
            "Mass number 208, atomic number 80",
            "Mass number 208, atomic number 82",
            "Mass number 212, atomic number 82",
            "Mass number 204, atomic number 82",
        ],
        "correct_index": 1,
        "why": "212/83 → 208/81 by alpha, and the beta then raises the atomic "
               "number to 82, giving 208/82.",
    },
    {
        "id": "ks4-nuclear-equations-h13",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two beta decays in succession raise the atomic "
                "number by two while leaving the mass number where it "
                "started.",
        "options": [
            "Because the two electrons emitted carry away a mass number of "
                "one each, and those two cancel out against each other",
            "Because each decay turns a neutron into a proton, adding one to "
                "the proton count and leaving the nucleon total alone",
            "Because the first decay raises the mass number by one and the "
                "second lowers it by one again",
            "Because the two electrons emitted come from an outer shell, so "
                "the nucleus itself is never involved at all",
        ],
        "correct_index": 1,
        "why": "A neutron becoming a proton keeps the nucleon count the same "
               "and adds one to the charge, and it happens twice.",
    },
    {
        "id": "ks4-nuclear-equations-h14",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus emits an alpha particle and then a gamma ray. "
                "Determine the total change in its mass number and in its "
                "atomic number.",
        "options": [
            "Mass number −4, atomic number −2",
            "Mass number −4, atomic number −3, the gamma ray carrying away "
                "one further unit of charge",
            "Mass number −5, atomic number −2, the gamma ray carrying away "
                "one further nucleon",
            "Mass number 0, atomic number 0, because the gamma ray restores "
                "what the alpha particle removed",
        ],
        "correct_index": 0,
        "why": "The alpha gives −4 and −2, and a gamma ray changes neither "
               "number, so the totals are −4 and −2.",
    },
    {
        "id": "ks4-nuclear-equations-h15",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the equation 234/90 → 234/91 + X, determine what particle "
                "X must be.",
        "options": [
            "An alpha particle, because an element has changed into another "
                "element",
            "A beta particle",
            "A neutron, because the nucleon total has been held constant "
                "across the change",
            "A gamma ray, because the mass number on each side is the same",
        ],
        "correct_index": 1,
        "why": "Balancing gives X a mass number of 0 and an atomic number of "
               "−1, which is a beta particle.",
    },
    {
        "id": "ks4-nuclear-equations-h16",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the equation 222/86 → X + 4/2, determine the mass number "
                "and atomic number of X.",
        "options": [
            "Mass number 226, atomic number 88, adding the alpha particle on "
                "instead of taking it away",
            "Mass number 218, atomic number 88",
            "Mass number 218, atomic number 84",
            "Mass number 222, atomic number 84",
        ],
        "correct_index": 2,
        "why": "222 − 4 = 218 and 86 − 2 = 84, so X is polonium-218.",
    },
    {
        "id": "ks4-nuclear-equations-h17",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Gamma emission is a decay that "
                "turns one element into another.'",
        "options": [
            "Sound — every kind of radioactive emission changes the element "
                "that the nucleus belongs to",
            "Sound — a gamma ray removes energy, and losing energy moves an "
                "element along the periodic table",
            "Unsound — a gamma ray changes neither the mass number nor the "
                "atomic number, so the element is the same afterwards",
            "Unsound — gamma emission changes the mass number but not the "
                "atomic number, so the element stays as it was",
        ],
        "correct_index": 2,
        "why": "Only a change in proton number changes the element, and gamma "
               "emission changes no nucleon count at all.",
    },
    {
        "id": "ks4-nuclear-equations-h18",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the electron emitted in beta decay cannot have "
                "come from one of the atom's electron shells.",
        "options": [
            "Because losing a shell electron would leave the mass number one "
                "unit lower than it is observed to be",
            "Because losing a shell electron would change neither the "
                "nucleus nor the element, whereas beta decay changes both",
            "Because the shells of an atom hold no electrons until after the "
                "decay has already happened",
            "Because a shell electron carries a charge of +1 while a beta "
                "particle carries −1",
        ],
        "correct_index": 1,
        "why": "Beta decay raises the atomic number, which only a change "
               "inside the nucleus can do, and losing a shell electron makes "
               "an ion of the same element.",
    },
    {
        "id": "ks4-nuclear-equations-h19",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nuclide of mass number 239 and atomic number 94 first "
                "releases an alpha particle; the product of that step then "
                "releases a beta particle. Determine the mass number and "
                "atomic number finally reached.",
        "options": [
            "Mass number 235, atomic number 93",
            "Mass number 235, atomic number 91",
            "Mass number 239, atomic number 93",
            "Mass number 231, atomic number 93",
        ],
        "correct_index": 0,
        "why": "239/94 → 235/92 by alpha, and the beta raises the atomic "
               "number to 93, giving 235/93.",
    },
    {
        "id": "ks4-nuclear-equations-h20",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus of mass number 40 and atomic number 19 emits a "
                "beta particle. Determine its neutron count before and after "
                "the decay.",
        "options": [
            "21 before and 22 after",
            "19 before and 20 after",
            "21 before and 20 after",
            "21 before and 21 after",
        ],
        "correct_index": 2,
        "why": "40 − 19 = 21 neutrons at the start, and one of them becomes a "
               "proton, leaving 40 − 20 = 20.",
    },
    {
        "id": "ks4-nuclear-equations-h21",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the mass number does not fall in beta decay even "
                "though a particle has left the nucleus.",
        "options": [
            "Because the particle that leaves is an electron, whose mass is "
                "negligible, and the nucleon it came from is still there as "
                "a proton",
            "Because a neutron enters the nucleus from outside at the same "
                "moment, replacing exactly what has gone",
            "Because the mass number of an element is fixed and cannot be "
                "altered by any decay at all",
            "Because the electron emitted is immediately recaptured into a "
                "shell, so the atom keeps all of its mass",
        ],
        "correct_index": 0,
        "why": "The nucleon is not lost — it changes from a neutron into a "
               "proton — and the electron that leaves carries almost no mass.",
    },
    {
        "id": "ks4-nuclear-equations-h22",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how many alpha decays are needed to take a nucleus "
                "from a mass number of 232 to a mass number of 208.",
        "options": [
            "12",
            "24",
            "4",
            "6",
        ],
        "correct_index": 3,
        "why": "232 − 208 = 24, and each alpha decay removes 4 nucleons, so "
               "24 ÷ 4 = 6.",
    },
    {
        "id": "ks4-nuclear-equations-h23",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that alpha decay moves an element two places "
                "to the right in the periodic table. Explain the error.",
        "options": [
            "Alpha decay moves it four places to the left, one for each "
                "nucleon that leaves the nucleus",
            "Alpha decay moves it two places to the left, because the atomic "
                "number falls by two",
            "Alpha decay leaves the position unchanged, since the element "
                "itself does not change",
            "Alpha decay moves it one place to the right, in the same "
                "direction as beta decay does",
        ],
        "correct_index": 1,
        "why": "Two protons are lost, so the atomic number falls by 2 and the "
               "element moves two places towards the start of the table.",
    },
    {
        "id": "ks4-nuclear-equations-h24",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iodine-131, atomic number 53, emits a beta particle and the "
                "daughter nucleus then emits a gamma ray. Determine the final "
                "mass number and atomic number.",
        "options": [
            "Mass number 131, atomic number 54",
            "Mass number 130, atomic number 54",
            "Mass number 127, atomic number 52",
            "Mass number 131, atomic number 55",
        ],
        "correct_index": 0,
        "why": "The beta takes the atomic number to 54 and leaves the mass "
               "number at 131; the gamma ray changes neither.",
    },
    {
        "id": "ks4-nuclear-equations-h25",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One alpha particle and then two beta particles are emitted "
                "by a nuclide that starts at mass number 230 and atomic "
                "number 90. Calculate the pair of values it ends on.",
        "options": [
            "Mass number 226, atomic number 88",
            "Mass number 222, atomic number 86",
            "Mass number 226, atomic number 90",
            "Mass number 230, atomic number 92",
        ],
        "correct_index": 2,
        "why": "230/90 → 226/88 by alpha, then 226/89 and 226/90 as each beta "
               "adds one to the atomic number.",
    },
    {
        "id": "ks4-nuclear-equations-h26",
        "subtopic_slug": "nuclear-equations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'A beta particle is an electron, so "
                "beta decay must lower the mass number by a small amount.'",
        "options": [
            "Sound — the electron's mass has to come off the total, however "
                "small that mass happens to be",
            "Unsound — an electron's mass is negligible, and the neutron it "
                "came from remains as a proton, so the mass number is "
                "unchanged",
            "Sound — the mass number falls by one, which is the mass number "
                "of the electron that leaves",
            "Unsound — beta decay in fact raises the mass number by one as "
                "the neutron changes into a proton",
        ],
        "correct_index": 1,
        "why": "Mass number counts nucleons, the nucleon count is unchanged, "
               "and the electron carries roughly 1/1836 of a nucleon's mass.",
    },
]
