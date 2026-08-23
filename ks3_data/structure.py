"""KS3 structure — all 33 units, all 185 lesson slots.

**Structure-first** (architecture.md §11 decision 8, ruled FULL BUILD 2026-07-26):

    "Every unit and lesson slot exists from the start, unauthored lessons
     present honestly as coming soon, never as broken links."

So this module is the *skeleton*: it declares every unit and every lesson slot
in the §7 topic map, with its slug, title and family. It carries no teaching
content at all.

Authored units live in their own modules (``chemistry_c1_particles.py`` and so
on) and are merged over this skeleton by ``__init__.py``. A lesson present here
but not in an authored module renders as a **coming soon** placeholder — a real,
routable page, never a 404 and never a dead link.

Transcribed from architecture.md §7.1–§7.3. Lesson titles and families are
copied from those tables; ``Y`` values are the §7 advisory fallback (§11
decision 5 demoted them — the published default is ``default_sequence.py``).

Slugs are **permanent** (§8.4): renaming a lesson changes its title, never its
slug, because scheme-of-work rows, progress records and ``requires`` edges all
point at slugs.
"""

# Each unit: (code, slug, title, discipline, statutory_area, typical_year,
#             [(lesson_slug, lesson_title, family), ...])
#
# A lesson slot may carry a FOURTH element: the code of the unit that **owns**
# the lesson. That marks the slot as a **reference**, not a copy — §4.6's
# single-source rule:
#
#     "One owning lesson, referenced from elsewhere. Never two copies."
#
# A referenced slot generates no page of its own. It renders in the unit index
# as a cross-link to the owner's page. Ownership for the contested ideas is
# fixed in §7.4 and is not re-argued per unit.
#
# `split_rationale` is carried for units split from one statutory heading (§4.3).

UNITS = [
    # ── Biology — 11 units, 58 lessons ──────────────────────────────────
    ("B1", "cells-and-organisation", "Cells and organisation", "biology",
     "Structure and function of living organisms", 7, [
        ("life-processes", "Life processes and what living things are made of", "CLASSIFY"),
        ("using-a-microscope", "Using a microscope", "INVESTIGATION"),
        ("animal-and-plant-cells", "Animal and plant cells", "MODEL"),
        ("specialised-cells", "Specialised cells", "SYSTEM"),
        ("levels-of-organisation", "Levels of organisation", "SYSTEM"),
        ("unicellular-organisms", "Unicellular organisms", "CONTRAST"),
        # ⊖ `stem-cells-and-meristems` and `enzymes-and-rate` were declared here
        #   at Phase 1 and removed on 2026-08-12 (MRB-199), ruled by Mide as
        #   examiner. Neither had a statutory statement to own: the CELLS strand
        #   is six statements and B1 was carrying eight lessons, so the two
        #   surplus slots were beyond-statutory by accident rather than by
        #   declaration. §7.6's exemption is built for the Year 9 GCSE bridge,
        #   not for a Year 7 statutory unit, so exempting them here would have
        #   opened a register that has no unit to hold it yet.
        #
        #   Stem cells becomes a Year 9 bridge candidate when §7.6's units
        #   exist. Enzymes has a statutory home already and it is not in B1 —
        #   `KS3.B.NUT.04` covers "enzymes simply as biological catalysts"
        #   under Nutrition and digestion, and B3 already declares
        #   `enzymes-in-digestion` to own it. No slot was moved across, because
        #   moving one would have given B3 two enzyme lessons and put the
        #   statutory one back into competition for its own statement.
        #   B1 is now six lessons for six statements — exactly 1:1.
     ]),
    ("B2", "movement-skeleton-and-muscles", "Movement: skeleton and muscles", "biology",
     "Structure and function of living organisms", 7, [
        ("what-the-skeleton-does", "What the skeleton does", "SYSTEM"),
        ("joints", "Joints", "MODEL"),
        ("antagonistic-muscle-pairs", "Antagonistic muscle pairs", "SYSTEM"),
        ("biomechanics-forces-in-the-body", "Biomechanics: forces in the body", "QUANTITATIVE"),
     ]),
    ("B3", "nutrition-and-digestion", "Nutrition and digestion", "biology",
     "Structure and function of living organisms", 7, [
        ("a-balanced-diet", "A balanced diet", "CLASSIFY"),
        ("food-tests", "Food tests", "INVESTIGATION"),
        # ⊕ OWNED BY B3. Ruled by Mide, 16 Aug 2026 (MRB-232).
        #
        # `KS3.B.NUT.02` was claimed by both B3 and Physics P2, and §7.4 gave
        # the whole of it to P2 — "Energy in food, energy calculations → owner
        # Physics P2, referenced by Biology B3" — so this slot was a reference
        # that generated no page. The statement splits instead, because it is
        # two different lessons wearing one bullet:
        #
        #   B3 owns WHAT YOU NEED AND WHY — requirements, imbalance, and what
        #      follows from getting it wrong. That is a nutrition lesson and it
        #      belongs beside the other seven.
        #   P2 keeps COMPARING ENERGY VALUES FROM LABELS IN kJ — the arithmetic
        #      and the units, which is a physics lesson about energy.
        #
        # P2's link back here is a `references` EDGE, never prose, so neither
        # page repeats the other and §4.6's single-source rule still holds.
        #
        # ⚠️ THE SLUG MOVES, and that is the exception rather than the rule.
        # §8.4 says renaming a lesson changes its title and never its slug —
        # but this slot has never generated a page, so there is no URL to
        # break, no `requires` edge pointing at it and no scheme-of-work row to
        # move. The slug is aligned to what Design delivered
        # (`energy-in-food-and-what-you-need`) rather than Design's file being
        # renamed to match a slug that never shipped.
        ("energy-in-food-and-what-you-need",
         "Energy in food and what you need", "QUANTITATIVE"),
        ("when-diet-goes-wrong", "When diet goes wrong", "CONTRAST"),
        ("the-digestive-system", "The digestive system", "SYSTEM"),
        ("enzymes-in-digestion", "Enzymes in digestion", "PROCESS"),
        ("absorption-and-the-small-intestine", "Absorption and the small intestine", "MODEL"),
        ("bacteria-in-the-gut", "Bacteria in the gut", "SYSTEM"),
     ]),
    ("B4", "breathing-and-gas-exchange", "Breathing and gas exchange", "biology",
     "Structure and function of living organisms", 8, [
        ("the-gas-exchange-system", "The gas exchange system", "SYSTEM"),
        ("how-breathing-works", "How breathing works", "MODEL"),
        ("alveoli-built-for-exchange", "Alveoli: built for exchange", "MODEL"),
        ("exercise-asthma-and-smoking", "Exercise, asthma and smoking", "SYSTEM"),
        ("stomata-and-gas-exchange-in-plants", "Stomata and gas exchange in plants", "CONTRAST"),
     ]),
    ("B5", "reproduction", "Reproduction", "biology",
     "Structure and function of living organisms", 8, [
        ("human-reproductive-systems", "Human reproductive systems", "SYSTEM"),
        ("gametes-and-fertilisation", "Gametes and fertilisation", "PROCESS"),
        ("the-menstrual-cycle", "The menstrual cycle", "PROCESS"),
        ("gestation-placenta-and-birth", "Gestation, the placenta and birth", "PROCESS"),
        ("lifestyle-and-the-developing-foetus", "Lifestyle and the developing foetus", "SYSTEM"),
        ("flowers-and-pollination", "Flowers and pollination", "SYSTEM"),
        ("fertilisation-seeds-and-fruit", "Fertilisation, seeds and fruit", "PROCESS"),
        ("seed-dispersal", "Seed dispersal", "CLASSIFY"),
     ]),
    ("B6", "health-and-drugs", "Health and drugs", "biology",
     "Structure and function of living organisms", 9, [
        ("what-drugs-do-to-the-body", "What drugs do to the body", "SYSTEM"),
        ("alcohol-and-smoking", "Alcohol and smoking", "SYSTEM"),
        ("substance-misuse-and-decisions", "Substance misuse and decisions", "INVESTIGATION"),
     ]),
    ("B7", "photosynthesis", "Photosynthesis", "biology",
     "Material cycles and energy", 8, [
        ("the-photosynthesis-reaction", "The photosynthesis reaction", "PROCESS"),
        ("leaves-built-for-the-job", "Leaves built for the job", "MODEL"),
        ("testing-a-leaf-for-starch", "Testing a leaf for starch", "INVESTIGATION"),
        ("why-almost-all-life-depends-on-it", "Why almost all life depends on it", "SYSTEM"),
     ]),
    ("B8", "respiration", "Respiration", "biology",
     "Material cycles and energy", 8, [
        ("aerobic-respiration", "Aerobic respiration", "PROCESS"),
        ("why-every-cell-respires", "Why every cell respires", "SYSTEM"),
        ("anaerobic-respiration-in-humans", "Anaerobic respiration in humans", "PROCESS"),
        ("fermentation", "Fermentation and what we use it for", "PROCESS"),
        ("aerobic-vs-anaerobic", "Aerobic vs anaerobic", "CONTRAST"),
     ]),
    ("B9", "ecosystems-and-interdependence", "Ecosystems and interdependence", "biology",
     "Interactions and interdependencies", 9, [
        ("food-chains-and-food-webs", "Food chains and food webs", "SYSTEM"),
        ("predator-and-prey", "Predator and prey", "MODEL"),
        ("disturbing-a-food-web", "Disturbing a food web", "SYSTEM"),
        ("pollinators-and-food-security", "Pollinators and food security", "SYSTEM"),
        ("toxic-build-up-in-a-food-chain", "Toxic build-up in a food chain", "PROCESS"),
        ("sampling-an-ecosystem", "Sampling an ecosystem", "INVESTIGATION"),
     ]),
    ("B10", "inheritance-and-dna", "Inheritance and DNA", "biology",
     "Genetics and evolution", 9, [
        ("variation-continuous-and-discontinuous", "Variation: continuous and discontinuous", "INVESTIGATION"),
        ("chromosomes-genes-and-dna", "Chromosomes, genes and DNA", "MODEL"),
        ("how-we-worked-out-dna", "How we worked out DNA's structure", "INVESTIGATION"),
        ("passing-it-on-heredity", "Passing it on: heredity", "PROCESS"),
        ("what-makes-a-species", "What makes a species", "CLASSIFY"),
     ]),
    ("B11", "evolution-extinction-and-biodiversity", "Evolution, extinction and biodiversity", "biology",
     "Genetics and evolution", 9, [
        ("variation-and-competitive-success", "Variation and competitive success", "SYSTEM"),
        ("natural-selection", "Natural selection", "PROCESS"),
        ("when-the-environment-changes-extinction", "When the environment changes: extinction", "SYSTEM"),
        ("biodiversity-and-gene-banks", "Biodiversity and gene banks", "SYSTEM"),
     ]),

    # ── Chemistry — 10 units, 55 lessons ────────────────────────────────
    ("C1", "particles-and-their-behaviour", "Particles and their behaviour", "chemistry",
     "The particulate nature of matter", 7, [
        ("particle-model", "The particle model", "MODEL"),
        ("solids-liquids-and-gases", "Solids, liquids and gases", "CONTRAST"),
        ("changes-of-state", "Changes of state", "PROCESS"),
        ("gas-pressure", "Gas pressure", "MODEL"),
        ("diffusion", "Diffusion", "MODEL"),
        ("testing-the-model", "Testing the model: does it explain everything?", "INVESTIGATION"),
     ]),
    ("C2", "atoms-elements-and-compounds", "Atoms, elements and compounds", "chemistry",
     "Atoms, elements and compounds", 7, [
        ("the-atom-daltons-model", "The atom: Dalton's model", "MODEL"),
        ("elements", "Elements", "CLASSIFY"),
        ("compounds", "Compounds", "CONTRAST"),
        ("chemical-symbols", "Chemical symbols", "CLASSIFY"),
        ("formulae", "Formulae", "MODEL"),
        ("conservation-of-mass", "Conservation of mass", "QUANTITATIVE"),
     ]),
    ("C3", "mixtures-and-separation", "Mixtures and separation", "chemistry",
     "Pure and impure substances", 7, [
        ("pure-or-mixture", "Pure or mixture?", "CLASSIFY"),
        ("dissolving-and-solutions", "Dissolving and solutions", "MODEL"),
        ("filtration", "Filtration", "PROCESS"),
        ("evaporation-and-crystallisation", "Evaporation and crystallisation", "PROCESS"),
        ("distillation", "Distillation", "PROCESS"),
        ("chromatography", "Chromatography", "PROCESS"),
        ("proving-something-is-pure", "Proving something is pure", "INVESTIGATION"),
     ]),
    ("C4", "chemical-reactions", "Chemical reactions", "chemistry",
     "Chemical reactions", 8, [
        ("chemical-vs-physical-change", "Chemical change vs physical change", "CONTRAST"),
        ("reactions-rearrange-atoms", "Reactions rearrange atoms", "MODEL"),
        ("word-equations", "Word equations", "MODEL"),
        ("mass-in-a-reaction", "Mass in a reaction", "QUANTITATIVE"),
        ("symbol-equations-and-balancing", "Symbol equations and balancing", "MODEL"),
     ]),
    ("C5", "types-of-reaction", "Types of reaction", "chemistry",
     "Chemical reactions", 8, [
        ("combustion", "Combustion", "PROCESS"),
        ("thermal-decomposition", "Thermal decomposition", "PROCESS"),
        ("oxidation", "Oxidation", "PROCESS"),
        ("displacement", "Displacement", "PROCESS"),
        ("which-reaction-is-this", "Which reaction is this?", "CLASSIFY"),
     ]),
    ("C6", "acids-and-alkalis", "Acids and alkalis", "chemistry",
     "Chemical reactions", 8, [
        ("acids-and-alkalis", "Acids and alkalis", "CLASSIFY"),
        ("the-ph-scale-and-indicators", "The pH scale and indicators", "MODEL"),
        ("neutralisation", "Neutralisation", "PROCESS"),
        ("acid-plus-metal", "Acid + metal", "PROCESS"),
        # ⊕ MRB-281, 23 Aug 2026 — RENAMED IN PLACE from `acid-plus-alkali`
        # ("Acid + alkali: making a salt"). That slot was never authored and
        # never could be: its topic is owned twice over by `neutralisation`
        # (CR.07a) and `making-a-pure-dry-salt` (CR.07b), so a lesson under
        # that name would double-own CR.07 and fail rule 4. Design drew
        # `c6-05-acids-and-carbonates` at this position instead; the earlier
        # ruling left the slot dead, and Mide has now overridden it. Renaming
        # rather than inserting keeps the key stage at 185 slots and leaves
        # positions 6 and 7 — and therefore every slug and URL below — exactly
        # where they already were.
        ("acids-and-carbonates", "Acids and carbonates", "PROCESS"),
        ("making-a-pure-dry-salt", "Making a pure dry salt", "INVESTIGATION"),
        ("catalysts", "Catalysts", "MODEL"),
     ]),
    ("C7", "energy-changes-in-reactions", "Energy changes in reactions", "chemistry",
     "Energetics", 9, [
        ("energy-and-changes-of-state", "Energy and changes of state", "MODEL"),
        ("exothermic-reactions", "Exothermic reactions", "PROCESS"),
        ("endothermic-reactions", "Endothermic reactions", "CONTRAST"),
        ("measuring-a-temperature-change", "Measuring a temperature change", "INVESTIGATION"),
     ]),
    ("C8", "the-periodic-table", "The periodic table", "chemistry",
     "The periodic table", 8, [
        ("metals-and-non-metals", "Metals and non-metals", "CONTRAST"),
        ("mendeleev", "Mendeleev and the table that predicted", "MODEL"),
        ("groups-and-periods", "Groups and periods", "MODEL"),
        ("group-1-the-alkali-metals", "Group 1 \u2014 the alkali metals", "MODEL"),
        ("group-7-the-halogens", "Group 7 \u2014 the halogens", "CONTRAST"),
        ("group-0-and-why-groups-exist", "Group 0 and why groups exist", "MODEL"),
        ("metal-and-non-metal-oxides", "Metal and non-metal oxides", "CONTRAST"),
     ]),
    ("C9", "metals-and-materials", "Metals and materials", "chemistry",
     "Materials", 9, [
        ("the-reactivity-series", "The reactivity series", "CLASSIFY"),
        ("predicting-displacement", "Predicting displacement", "MODEL"),
        ("getting-metals-out-of-rocks", "Getting metals out of rocks", "PROCESS"),
        ("ceramics-polymers-and-composites", "Ceramics, polymers and composites", "CONTRAST"),
     ]),
    ("C10", "the-earth-and-its-atmosphere", "The Earth and its atmosphere", "chemistry",
     "Earth and atmosphere", 9, [
        ("inside-the-earth", "Inside the Earth", "MODEL"),
        ("three-ways-to-make-a-rock", "Three ways to make a rock", "CLASSIFY"),
        ("the-rock-cycle", "The rock cycle", "PROCESS"),
        ("a-planet-with-limits", "A planet with limits: resources and recycling", "SYSTEM"),
        ("whats-in-the-air", "What's in the air", "MODEL"),
        ("carbon-dioxide-humans-and-climate", "Carbon dioxide, humans and climate", "SYSTEM"),
     ]),

    # ── Physics — 12 units, 70 lessons ──────────────────────────────────
    ("P1", "energy-transfers", "Energy transfers", "physics",
     "Energy", 8, [
        ("energy-stores", "Energy stores", "CLASSIFY"),
        ("energy-transfers-before-and-after", "Energy transfers: before and after", "MODEL"),
        ("conservation-of-energy", "Conservation of energy", "MODEL"),
        ("heating-and-thermal-equilibrium", "Heating and thermal equilibrium", "MODEL"),
        ("conduction", "Conduction", "PROCESS"),
        ("radiation", "Radiation", "PROCESS"),
        ("insulation", "Keeping energy in: insulation", "INVESTIGATION"),
        ("simple-machines", "Simple machines: force for distance", "QUANTITATIVE"),
     ]),
    ("P2", "energy-at-home", "Energy at home", "physics",
     "Energy", 9, [
        ("energy-in-food", "Energy in food", "QUANTITATIVE"),
        ("power-ratings-in-watts", "Power ratings in watts", "QUANTITATIVE"),
        ("calculating-energy-transferred", "Calculating energy transferred", "QUANTITATIVE"),
        ("reading-a-fuel-bill", "Reading a fuel bill", "QUANTITATIVE"),
        ("fuels-and-energy-resources", "Fuels and energy resources", "CLASSIFY"),
     ]),
    ("P3", "describing-motion", "Describing motion", "physics",
     "Motion and forces", 7, [
        ("speed", "Speed", "QUANTITATIVE"),
        ("distance-time-graphs", "Distance–time graphs", "INVESTIGATION"),
        ("relative-motion", "Relative motion", "MODEL"),
     ]),
    ("P4", "forces", "Forces", "physics",
     "Motion and forces", 7, [
        ("what-a-force-is", "What a force is", "MODEL"),
        ("drawing-and-adding-forces", "Drawing and adding forces", "MODEL"),
        ("balanced-and-unbalanced", "Balanced and unbalanced", "CONTRAST"),
        ("what-forces-do-to-motion", "What forces do to motion", "MODEL"),
        ("friction", "Friction", "PROCESS"),
        ("air-and-water-resistance", "Air and water resistance", "SYSTEM"),
        ("moments", "Moments: the turning effect", "QUANTITATIVE"),
        ("springs-and-hookes-law", "Springs and Hooke's law", "INVESTIGATION"),
        ("non-contact-forces", "Non-contact forces", "CLASSIFY"),
     ]),
    ("P5", "pressure", "Pressure", "physics",
     "Motion and forces", 8, [
        ("pressure-force-over-area", "Pressure = force ÷ area", "QUANTITATIVE"),
        ("pressure-in-liquids", "Pressure in liquids", "MODEL"),
        ("upthrust-floating-and-sinking", "Upthrust, floating and sinking", "MODEL"),
        ("atmospheric-pressure", "Atmospheric pressure", "SYSTEM"),
     ]),
    ("P6", "waves-and-sound", "Waves and sound", "physics",
     "Waves", 8, [
        ("waves-on-water", "Waves on water: what a wave is", "MODEL"),
        ("transverse-waves-and-superposition", "Transverse waves, reflection and superposition", "MODEL"),
        ("how-sound-is-made", "How sound is made", "PROCESS"),
        ("sound-is-longitudinal", "Sound is longitudinal", "CONTRAST"),
        ("frequency-pitch-and-loudness", "Frequency, pitch and loudness", "QUANTITATIVE"),
        ("sound-needs-a-medium", "Sound needs a medium", "INVESTIGATION"),
        ("echoes-reflection-and-absorption", "Echoes, reflection and absorption", "PROCESS"),
        ("hearing-and-auditory-range", "Hearing and auditory range", "SYSTEM"),
        ("ultrasound-at-work", "Ultrasound at work", "SYSTEM"),
     ]),
    ("P7", "light", "Light", "physics",
     "Waves", 8, [
        ("light-travels", "Light travels", "MODEL"),
        ("reflection-mirrors-and-scattering", "Reflection: mirrors and scattering", "MODEL"),
        ("refraction", "Refraction", "PROCESS"),
        ("lenses-and-images", "Lenses and images", "MODEL"),
        ("the-eye-and-the-camera", "The eye and the camera", "SYSTEM"),
        ("colour-and-the-spectrum", "Colour and the spectrum", "MODEL"),
        ("why-things-look-coloured", "Why things look coloured", "CONTRAST"),
     ]),
    ("P8", "electric-circuits", "Electric circuits", "physics",
     "Electricity and electromagnetism", 8, [
        ("current-and-circuits", "Current and circuits", "MODEL"),
        ("series-and-parallel", "Series and parallel", "CONTRAST"),
        ("current-at-a-junction", "Current at a junction", "SYSTEM"),
        ("potential-difference", "Potential difference", "MODEL"),
        ("resistance", "Resistance", "QUANTITATIVE"),
        ("conductors-and-insulators", "Conductors and insulators", "CLASSIFY"),
        ("building-and-measuring-a-circuit", "Building and measuring a circuit", "INVESTIGATION"),
     ]),
    ("P9", "static-electricity", "Static electricity", "physics",
     "Electricity and electromagnetism", 9, [
        ("charging-by-rubbing", "Charging by rubbing", "PROCESS"),
        ("forces-between-charges", "Forces between charges", "MODEL"),
        ("electric-fields", "Electric fields", "MODEL"),
     ]),
    ("P10", "magnetism-and-electromagnetism", "Magnetism and electromagnetism", "physics",
     "Electricity and electromagnetism", 9, [
        ("magnets-and-poles", "Magnets and poles", "CONTRAST"),
        ("magnetic-fields", "Magnetic fields", "INVESTIGATION"),
        ("the-earth-is-a-magnet", "The Earth is a magnet", "SYSTEM"),
        ("electromagnets", "Electromagnets", "MODEL"),
        ("how-a-motor-works", "How a motor works", "SYSTEM"),
     ]),
    ("P11", "matter-and-the-particle-model", "Matter and the particle model", "physics",
     "Matter", 7, [
        ("density", "Density", "QUANTITATIVE"),
        ("brownian-motion", "Brownian motion", "MODEL"),
        ("temperature-and-internal-energy", "Temperature, particle motion and internal energy", "MODEL"),
        ("why-ice-floats", "Why ice floats", "CONTRAST"),
     ]),
    ("P12", "space", "Space", "physics",
     "Space physics", 9, [
        ("gravity-and-weight", "Gravity and weight", "QUANTITATIVE"),
        ("mass-vs-weight", "Mass vs weight", "CONTRAST"),
        ("gravity-earth-moon-and-sun", "Gravity between Earth, Moon and Sun", "MODEL"),
        ("the-sun-stars-and-galaxies", "The Sun, stars and galaxies", "SYSTEM"),
        ("seasons-and-the-tilt", "Seasons and the tilt", "MODEL"),
        ("how-far-is-a-light-year", "How far is a light year?", "QUANTITATIVE"),
     ]),
]

# Units split from a single statutory heading carry a rationale (§4.3).
SPLIT_RATIONALE = {
    "B10": "Inheritance mechanism and evolutionary consequence are separately "
           "assessable ideas and are almost universally taught apart.",
    "B11": "Inheritance mechanism and evolutionary consequence are separately "
           "assessable ideas and are almost universally taught apart.",
    "C4":  "Eight statutory bullets spanning representation, reaction types and "
           "acid chemistry; universally taught as separate units and too large "
           "to schedule as one.",
    "C5":  "Eight statutory bullets spanning representation, reaction types and "
           "acid chemistry; universally taught as separate units and too large "
           "to schedule as one.",
    "C6":  "Eight statutory bullets spanning representation, reaction types and "
           "acid chemistry; universally taught as separate units and too large "
           "to schedule as one.",
}

# P11 is a referencing unit (§4.6, §7.3): it owns four lessons and pulls the
# rest of its statutory coverage from Chemistry C1.
REFERENCING_UNITS = {"P11": ["C1", "C4"]}

DISCIPLINES = ("biology", "chemistry", "physics")

DISCIPLINE_TITLES = {
    "biology":   "Biology",
    "chemistry": "Chemistry",
    "physics":   "Physics",
}


def unit_index():
    """All units as dicts, keyed by code, in declaration order."""
    out = {}
    for code, slug, title, disc, area, year, lessons in UNITS:
        out[code] = {
            "code": code, "slug": slug, "title": title, "discipline": disc,
            "statutory_area": area, "typical_year": year,
            "split_rationale": SPLIT_RATIONALE.get(code),
            "references": REFERENCING_UNITS.get(code, []),
            "lesson_slots": [
                {"slug": s[0], "title": s[1], "family": s[2],
                 "owned_by": s[3] if len(s) > 3 else None}
                for s in lessons
            ],
        }
    return out


def _owned(unit_lessons):
    """Slots this unit actually owns — referenced slots belong to another unit."""
    return [s for s in unit_lessons if len(s) <= 3]


def totals():
    """Counts. `lessons` counts SLOTS as §7 does; `owned` excludes references."""
    return {
        "units": len(UNITS),
        "lessons": sum(len(u[6]) for u in UNITS),
        "owned_lessons": sum(len(_owned(u[6])) for u in UNITS),
        "referenced_slots": sum(len(u[6]) - len(_owned(u[6])) for u in UNITS),
        "by_discipline": {
            d: {
                "units": sum(1 for u in UNITS if u[3] == d),
                "lessons": sum(len(u[6]) for u in UNITS if u[3] == d),
                "owned_lessons": sum(len(_owned(u[6])) for u in UNITS if u[3] == d),
            } for d in DISCIPLINES
        },
    }
