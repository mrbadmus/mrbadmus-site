#!/usr/bin/env python3
"""
MrBadmusAI — Full Site Generator
Run: python3 generate_site.py
Output: ./mrbadmus_site/ (ready to deploy on Cloudflare)
"""

import os, shutil, json, glob, sys, re

# Bonding redesign (MRB-113 Phase B) — theory-block decomposition for the
# redesigned bonding pages. Frozen source fields are never edited; blocks are
# authored presentation. See bonding_redesign.py and the port map.
from bonding_redesign import (
    BONDING_REDESIGN, BLOCK_CSS as BONDING_BLOCK_CSS,
    render_theory_blocks, interactive_init_js, render_examiner_tip,
    build_fifa_config,
)

# ─────────────────────────────────────────────
#  EXAM LADDER (Phase 2B · MRB-136 · architecture_v2 Law 6)
# ─────────────────────────────────────────────
# The bonding pages carrying the authored production layer: marking-point
# decompositions, causal chains, be-the-examiner items and the formula
# deducer bank. Content lives in shared/exam-content/<slug>.js, joined to
# the page by slug and rendered by shared/exam-ladder.js — deliberately
# OUTSIDE the eight frozen content fields (quiz, matching, common_mistake,
# key_note, theory, fifas, higher, triple_only), which stay byte-identical.
EXAM_LADDER_PAGES = {
    "properties-ionic-compounds",
    "giant-covalent-structures",
    "metals-alloys",
    "properties-small-molecules",
    "ionic-bonding",
}

# ─────────────────────────────────────────────
#  SITE DATA — all topics, subtopics, equations,
#  required practicals, flags
# ─────────────────────────────────────────────

SITE_DATA = {
    "physics": {
        "label": "Physics",
        "emoji": "⚡",
        "color": "#1D6FB8",
        "code": "8463",
        "topics": [
            {
                "id": "energy",
                "title": "Energy",
                "spec": "4.1",
                "paper": 1,
                "subtopics": [
                    "Energy stores and systems",
                    "Changes in energy — kinetic, gravitational potential, elastic potential",
                    "Conservation of energy",
                    "Energy transfer — conduction, convection, radiation",
                    "Efficiency",
                    "Renewable and non-renewable energy resources",
                ],
                "equations": ["KE = ½mv²", "GPE = mgh", "E = QΔθ", "Efficiency = useful output ÷ total input"],
                "rp": ["RP1 — Specific heat capacity", "RP2 — Thermal insulation"],
                "higher": ["Elastic potential energy: E = ½ke²", "Derivation of KE formula"],
                "triple_only": ["Thermal conductivity and insulation (RP2)"],
            },
            {
                "id": "electricity",
                "title": "Electricity",
                "spec": "4.2",
                "paper": 1,
                "subtopics": [
                    "Circuit symbols and diagrams",
                    "Charge, current and time — Q = It",
                    "Potential difference, current and resistance — V = IR",
                    "Resistance — ohmic conductors, filament lamp, diode, thermistor, LDR",
                    "Series and parallel circuits",
                    "Mains electricity — AC, DC, live/neutral/earth",
                    "Power — P = VI, P = I²R",
                    "Energy — E = Pt, E = QV",
                    "National Grid",
                ],
                "equations": ["Q = It", "V = IR", "P = VI", "P = I²R", "E = Pt", "E = QV"],
                "rp": ["RP3 — Resistance of a wire (length)", "RP4 — I–V characteristics"],
                "higher": ["Potential divider circuits", "Vout = Vin × R2/(R1+R2)"],
                "triple_only": ["Static electricity", "Electric fields"],
            },
            {
                "id": "particle-model",
                "title": "Particle Model of Matter",
                "spec": "4.3",
                "paper": 1,
                "subtopics": [
                    "States of matter — solid, liquid, gas",
                    "Changes of state",
                    "Density — ρ = m/V",
                    "Internal energy",
                    "Specific heat capacity — E = mcΔθ",
                    "Specific latent heat — E = mL",
                    "Gas pressure and temperature",
                ],
                "equations": ["ρ = m/V", "E = mcΔθ", "E = mL", "pV = constant (Boyle's law)", "p/T = constant"],
                "rp": ["RP5 — Density of regular/irregular objects"],
                "higher": ["Gas pressure and volume relationships", "Absolute zero"],
                "triple_only": [],
            },
            {
                "id": "atomic-structure",
                "title": "Atomic Structure",
                "spec": "4.4",
                "paper": 1,
                "subtopics": [
                    "Structure of the atom",
                    "Mass number, atomic number, isotopes",
                    "Development of the atomic model",
                    "Radioactive decay — alpha, beta, gamma",
                    "Nuclear equations",
                    "Half-life",
                    "Background radiation",
                    "Nuclear fission and fusion",
                ],
                "equations": ["A = N/t (activity)", "Count rate ÷ 2 per half-life"],
                "rp": ["RP6 — Radioactive decay simulation (dice)"],
                "higher": ["Nuclear equations with correct notation", "Uses and hazards of radiation"],
                "triple_only": ["Background radiation", "Uses of nuclear radiation", "Nuclear fission", "Nuclear fusion"],
            },
            {
                "id": "forces",
                "title": "Forces",
                "spec": "4.5",
                "paper": 2,
                "subtopics": [
                    "Scalar and vector quantities",
                    "Contact and non-contact forces",
                    "Weight, mass and gravity — W = mg",
                    "Resultant forces",
                    "Work done — W = Fs",
                    "Forces and elasticity — F = ke",
                    "Moments and levers",
                    "Pressure — p = F/A",
                    "Speed, distance, time — s = vt",
                    "Acceleration — a = Δv/t",
                    "Newton's laws of motion",
                    "Stopping distances",
                    "Momentum — p = mv",
                ],
                "equations": ["W = mg", "W = Fs", "F = ke", "Moment = Fd", "p = F/A", "s = vt", "a = Δv/t", "F = ma", "p = mv"],
                "rp": ["RP7 — Acceleration on a ramp", "RP8 — Force and extension (spring)"],
                "higher": ["p = F/A for fluids", "Terminal velocity", "Impulse = FΔt"],
                "triple_only": ["Moments, levers and gears", "Pressure in fluids and upthrust"],
            },
            {
                "id": "waves",
                "title": "Waves",
                "spec": "4.6",
                "paper": 2,
                "subtopics": [
                    "Transverse and longitudinal waves",
                    "Wave speed — v = fλ",
                    "Reflection and refraction",
                    "Sound waves",
                    "Electromagnetic spectrum",
                    "Visible light",
                    "Radio waves to gamma rays — uses and hazards",
                    "Infrared — temperature and radiation",
                ],
                "equations": ["v = fλ", "T = 1/f"],
                "rp": ["RP9 — Investigating waves — ripple tank / slinky", "RP10 — Light — reflection and refraction"],
                "higher": ["Reflection angle = incidence angle", "Refractive index n = sin i / sin r"],
                "triple_only": ["Sound waves, hearing and ultrasound", "Seismic waves and SONAR", "Lenses and vision correction", "Infrared emission and black bodies"],
            },
            {
                "id": "magnetism",
                "title": "Magnetism and Electromagnetism",
                "spec": "4.7",
                "paper": 2,
                "subtopics": [
                    "Permanent and induced magnets",
                    "Magnetic fields",
                    "Electromagnets",
                    "Fleming's left hand rule",
                    "The motor effect — F = BIL",
                    "Electric motors",
                    "Electromagnetic induction",
                    "Generators and alternators",
                    "Transformers — Vp/Vs = Np/Ns",
                ],
                "equations": ["F = BIL", "Vp/Vs = Np/Ns", "Vp × Ip = Vs × Is (100% efficiency)"],
                "rp": ["RP11 — Investigate the factors affecting the force on a conductor"],
                "higher": ["Induced EMF and flux", "Transformer efficiency calculations"],
                "triple_only": ["Loudspeakers", "Induced potential", "Generator effect", "Microphones", "Transformers"],
            },
            {
                "id": "space",
                "title": "Space Physics",
                "spec": "4.8",
                "paper": 2,
                "subtopics": [
                    "The Solar System",
                    "Life cycle of stars",
                    "Orbital motion",
                    "Red-shift and the Big Bang",
                    "The expanding universe",
                    "Dark matter and dark energy",
                ],
                "equations": ["Orbital speed ∝ 1/√r"],
                "rp": [],
                "higher": ["Red-shift calculations", "Evidence for the Big Bang"],
                "triple_only": ["Space Physics is TRIPLE ONLY (Physics 8463)"],
            },
        ],
    },
    "chemistry": {
        "label": "Chemistry",
        "emoji": "🧪",
        "color": "#B02342",
        "code": "8462",
        "topics": [
            {
                "id": "atomic-structure",
                "title": "Atomic Structure and the Periodic Table",
                "spec": "4.1",
                "paper": 1,
                "subtopics": [
                    "Structure of the atom — protons, neutrons, electrons",
                    "Mass number and atomic number",
                    "Isotopes",
                    "Electronic structure and shells",
                    "Development of the atomic model",
                    "The periodic table — periods and groups",
                    "Metals and non-metals",
                    "Group 1 — alkali metals",
                    "Group 7 — halogens",
                    "Group 0 — noble gases",
                    "Transition metals",
                ],
                "equations": ["Mass number = protons + neutrons", "Atomic number = number of protons"],
                "rp": [],
                "higher": ["Electronic structure of first 20 elements", "Predicting properties from group trends"],
                "triple_only": [],
            },
            {
                "id": "bonding",
                "title": "Bonding, Structure and Properties of Matter",
                "spec": "4.2",
                "paper": 1,
                "subtopics": [
                    "Ionic bonding — electron transfer, lattice structure",
                    "Covalent bonding — electron sharing",
                    "Metallic bonding — delocalised electrons",
                    "Simple molecular structures — low melting point",
                    "Giant covalent structures — diamond, graphite, silica",
                    "Giant ionic lattices",
                    "Alloys",
                    "Polymers",
                ],
                "equations": [],
                "rp": [],
                "higher": ["Dot and cross diagrams for covalent molecules", "Graphene and nanotubes"],
                "triple_only": [],
            },
            {
                "id": "quantitative",
                "title": "Quantitative Chemistry",
                "spec": "4.3",
                "paper": 1,
                "subtopics": [
                    "Relative atomic mass (Ar) and relative formula mass (Mr)",
                    "Moles — mol = mass ÷ Mr",
                    "Concentration — mol = concentration × volume",
                    "Gas volumes — mol = volume ÷ 24 (at RTP)",
                    "Percentage yield",
                    "Atom economy",
                    "Balancing equations",
                ],
                "equations": ["mol = mass ÷ Mr", "mol = c × V", "mol = V ÷ 24", "% yield = actual ÷ theoretical × 100", "Atom economy = Mr useful ÷ Mr all × 100"],
                "rp": [],
                "higher": ["Limiting reactant calculations", "Titration calculations — moles from burette readings"],
                "triple_only": [],
            },
            {
                "id": "chemical-changes",
                "title": "Chemical Changes",
                "spec": "4.4",
                "paper": 1,
                "subtopics": [
                    "Reactivity series of metals",
                    "Displacement reactions",
                    "Extraction of metals — reduction, electrolysis",
                    "Acids and bases — pH scale",
                    "Neutralisation — acid + alkali",
                    "Reactions of acids with metals, oxides, carbonates",
                    "Making salts",
                    "Electrolysis — principles",
                    "Electrolysis of molten ionic compounds",
                    "Electrolysis of solutions",
                ],
                "equations": ["acid + metal → salt + hydrogen", "acid + base → salt + water", "acid + carbonate → salt + water + CO₂"],
                "rp": ["RP1 — Making salts (titration)", "RP2 — Electrolysis of aqueous solutions"],
                "higher": ["Half equations for electrolysis", "Predicting products at electrodes"],
                "triple_only": [],
            },
            {
                "id": "energy-changes",
                "title": "Energy Changes",
                "spec": "4.5",
                "paper": 1,
                "subtopics": [
                    "Exothermic and endothermic reactions",
                    "Reaction profiles — activation energy",
                    "Bond energies — breaking bonds (endothermic) vs forming bonds (exothermic)",
                    "Cells and batteries",
                    "Fuel cells — hydrogen fuel cell",
                ],
                "equations": ["ΔH = energy in (breaking) − energy out (forming)"],
                "rp": ["RP3 — Temperature changes in reactions"],
                "higher": ["Bond energy calculations", "Comparing fuel cells vs batteries"],
                "triple_only": [],
            },
            {
                "id": "rates-equilibrium",
                "title": "Rate and Extent of Chemical Change",
                "spec": "4.6",
                "paper": 2,
                "subtopics": [
                    "Rate of reaction — definition",
                    "Factors affecting rate: concentration, temperature, surface area, catalyst",
                    "Collision theory",
                    "Measuring rate of reaction",
                    "Reversible reactions",
                    "Equilibrium — Le Chatelier's principle",
                    "Effect of changing conditions on equilibrium",
                ],
                "equations": ["Rate = quantity ÷ time"],
                "rp": ["RP4 — Rate of reaction (sodium thiosulfate + HCl)", "RP5 — Rate of reaction (marble chips + HCl)"],
                "higher": ["Le Chatelier's principle — temperature, pressure, concentration effects", "Haber process conditions"],
                "triple_only": [],
            },
            {
                "id": "organic",
                "title": "Organic Chemistry",
                "spec": "4.7",
                "paper": 2,
                "subtopics": [
                    "Crude oil and hydrocarbons",
                    "Fractional distillation",
                    "Alkanes — naming, properties, combustion",
                    "Cracking — thermal and catalytic",
                    "Alkenes — double bond, addition reactions",
                    "Addition polymerisation",
                    "Alcohols — ethanol, fermentation, combustion",
                    "Carboxylic acids",
                    "Condensation polymerisation",
                ],
                "equations": ["CₙH₂ₙ₊₂ (alkanes)", "CₙH₂ₙ (alkenes)"],
                "rp": [],
                "higher": ["Mechanisms — addition reactions of alkenes", "Ester formation"],
                "triple_only": ["Amino acids and proteins", "DNA — condensation polymerisation"],
            },
            {
                "id": "analysis",
                "title": "Chemical Analysis",
                "spec": "4.8",
                "paper": 2,
                "subtopics": [
                    "Pure substances vs mixtures",
                    "Chromatography — Rf values",
                    "Flame tests — identifying metal ions",
                    "Testing for gases — hydrogen, oxygen, CO₂, chlorine",
                    "Testing for ions — precipitation reactions",
                    "Instrumental analysis — mass spectrometry, IR spectroscopy",
                ],
                "equations": ["Rf = distance by spot ÷ distance by solvent"],
                "rp": ["RP6 — Paper chromatography", "RP7 — Identify ions using chemical tests"],
                "higher": ["Interpreting mass spectra", "IR spectroscopy — functional groups"],
                "triple_only": [],
            },
            {
                "id": "atmosphere",
                "title": "Chemistry of the Atmosphere",
                "spec": "4.9",
                "paper": 2,
                "subtopics": [
                    "Composition of the atmosphere",
                    "Evolution of the atmosphere",
                    "Greenhouse gases — CO₂, methane, water vapour",
                    "Human causes of climate change",
                    "Carbon footprint",
                    "Atmospheric pollutants — CO, NOₓ, SO₂, particulates",
                ],
                "equations": [],
                "rp": [],
                "higher": ["Evidence for climate change", "Evaluating methods to reduce carbon footprint"],
                "triple_only": [],
            },
            {
                "id": "resources",
                "title": "Using Resources",
                "spec": "4.10",
                "paper": 2,
                "subtopics": [
                    "Finite and renewable resources",
                    "Water treatment",
                    "Life cycle assessment (LCA)",
                    "Reduce, reuse, recycle",
                    "Corrosion — rusting of iron",
                    "Alloys",
                    "Ceramics, polymers, composites",
                    "The Haber process — making ammonia",
                    "Fertilisers",
                ],
                "equations": ["N₂ + 3H₂ ⇌ 2NH₃"],
                "rp": ["RP8 — Water purification"],
                "higher": ["NPK fertiliser calculations", "LCA evaluation"],
                "triple_only": [],
            },
        ],
    },
    "biology": {
        "label": "Biology",
        "emoji": "🌿",
        "color": "#237A3B",
        "code": "8461",
        "topics": [
            {
                "id": "cell-biology",
                "title": "Cell Biology",
                "spec": "4.1",
                "paper": 1,
                "subtopics": [
                    "Animal and plant cells — structure and function",
                    "Prokaryotic and eukaryotic cells",
                    "Cell specialisation",
                    "Microscopy — magnification = image ÷ actual",
                    "Diffusion, osmosis, active transport",
                    "Cell division — mitosis",
                    "Growth and differentiation",
                    "Stem cells",
                ],
                "equations": ["Magnification = image size ÷ actual size"],
                "rp": ["RP1 — Microscopy (plant or animal cells)", "RP2 — Osmosis in plant tissue"],
                "higher": ["Meiosis and genetic variation", "Stem cell ethics and uses"],
                "triple_only": [],
            },
            {
                "id": "organisation",
                "title": "Organisation",
                "spec": "4.2",
                "paper": 1,
                "subtopics": [
                    "Cell → tissue → organ → organ system",
                    "Digestive system — enzymes and digestion",
                    "Enzymes — lock and key model, active site",
                    "Effect of temperature and pH on enzymes",
                    "Heart and circulatory system",
                    "Blood vessels — arteries, veins, capillaries",
                    "Blood components",
                    "Respiratory system",
                    "Health and disease — communicable and non-communicable",
                    "Cancer",
                ],
                "equations": [],
                "rp": ["RP3 — Effect of pH on enzyme activity", "RP4 — Food tests (starch, glucose, protein, fat)"],
                "higher": ["Coronary heart disease — treatments", "Plant transport — xylem and phloem"],
                "triple_only": [],
            },
            {
                "id": "infection-response",
                "title": "Infection and Response",
                "spec": "4.3",
                "paper": 1,
                "subtopics": [
                    "Pathogens — bacteria, viruses, fungi, protists",
                    "How pathogens spread",
                    "Specific diseases — measles, HIV, malaria, tobacco mosaic virus, rose black spot, Salmonella",
                    "The immune system — phagocytosis, antibodies, memory cells",
                    "Vaccination — herd immunity",
                    "Antibiotics and painkillers",
                    "Drug development and testing",
                ],
                "equations": [],
                "rp": [],
                "higher": ["Monoclonal antibodies — production and uses", "Plant defence responses"],
                "triple_only": [],
            },
            {
                "id": "bioenergetics",
                "title": "Bioenergetics",
                "spec": "4.4",
                "paper": 1,
                "subtopics": [
                    "Photosynthesis equation — 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
                    "Limiting factors of photosynthesis — light, CO₂, temperature",
                    "Uses of glucose",
                    "Aerobic respiration — C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O",
                    "Anaerobic respiration — humans and yeast",
                    "Response to exercise — heart rate, breathing rate",
                ],
                "equations": ["6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂", "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O (aerobic)", "glucose → lactic acid (anaerobic, humans)", "glucose → ethanol + CO₂ (fermentation)"],
                "rp": ["RP5 — Rate of photosynthesis (pondweed)", "RP6 — Anaerobic fermentation (yeast)"],
                "higher": ["Light intensity vs rate of photosynthesis graphs", "Metabolism and metabolic rate"],
                "triple_only": [],
            },
            {
                "id": "homeostasis",
                "title": "Homeostasis and Response",
                "spec": "4.5",
                "paper": 2,
                "subtopics": [
                    "Homeostasis — maintaining internal conditions",
                    "The nervous system — CNS, neurons, synapses",
                    "Reflex arc",
                    "The brain — cerebrum, cerebellum, medulla",
                    "The eye — structure and function",
                    "The endocrine system — hormones and glands",
                    "Blood glucose regulation — insulin and glucagon",
                    "Diabetes — Type 1 and Type 2",
                    "Controlling body temperature",
                    "Controlling water balance — kidneys and ADH",
                    "Reproductive hormones — menstrual cycle, FSH, LH, oestrogen, progesterone",
                    "Contraception and fertility treatments",
                ],
                "equations": [],
                "rp": ["RP7 — Investigating reaction time"],
                "higher": ["Negative feedback loops", "IVF treatment and ethical considerations"],
                "triple_only": ["Thermoregulation detail", "Kidney — ultrafiltration and reabsorption"],
            },
            {
                "id": "inheritance",
                "title": "Inheritance, Variation and Evolution",
                "spec": "4.6",
                "paper": 2,
                "subtopics": [
                    "DNA structure — double helix, bases, base pairing",
                    "Genes, alleles, chromosomes",
                    "Dominant and recessive alleles",
                    "Monohybrid crosses — Punnett squares",
                    "Inherited conditions — cystic fibrosis, polydactyly",
                    "Sex determination — XX and XY",
                    "Variation — environmental and genetic",
                    "Mutation",
                    "Natural selection",
                    "Evidence for evolution — fossils, antibiotic resistance",
                    "Classification",
                ],
                "equations": [],
                "rp": [],
                "higher": ["Codominance and blood groups", "Genetic engineering — insulin production"],
                "triple_only": ["Protein synthesis — transcription and translation", "Selective breeding"],
            },
            {
                "id": "ecology",
                "title": "Ecology",
                "spec": "4.7",
                "paper": 2,
                "subtopics": [
                    "Levels of organisation — population, community, ecosystem",
                    "Abiotic and biotic factors",
                    "Interdependence — food webs, competition",
                    "Adaptations",
                    "Sampling — quadrats and transects",
                    "Cycling of materials — water cycle, carbon cycle, nitrogen cycle",
                    "Biodiversity and its importance",
                    "Human impacts — deforestation, global warming, pollution",
                    "Conservation",
                ],
                "equations": ["Population size = (n1 × n2) ÷ m (mark-recapture)"],
                "rp": ["RP8 — Sampling organisms in a habitat"],
                "higher": ["Calculating biodiversity index", "Interactions in food webs — predator-prey cycles"],
                "triple_only": [],
            },
        ],
    },
}

# ── Shared CSS — read from source file ──
_css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shared", "styles.css")
with open(_css_path, "r", encoding="utf-8") as f:
    SHARED_CSS_PATCHED = f.read()

# ─────────────────────────────────────────────
#  SHARED JS — read from source file
# ─────────────────────────────────────────────

# ── Shared JS — read from source file ──
_js_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shared", "mrbadmus.v2.js")
with open(_js_path, "r", encoding="utf-8") as f:
    SHARED_JS = f.read()



# ─────────────────────────────────────────────
#  NEW SITE STRUCTURE DATA
#  Combined Science: Foundation / Higher
#  Triple Science:   Foundation / Higher
#  Each has Physics / Chemistry / Biology
# ─────────────────────────────────────────────

# Subtopic lists from your curriculum maps (images)
# These drive which topics appear in each pathway

COMBINED_FOUNDATION_TOPICS = {
    "physics": ["energy", "electricity", "particle-model", "atomic-structure", "forces", "waves", "magnetism"],
    "chemistry": ["atomic-structure", "bonding", "quantitative", "chemical-changes", "energy-changes", "rates-equilibrium", "organic", "analysis", "atmosphere", "resources"],
    "biology": ["cell-biology", "organisation", "infection-response", "bioenergetics", "homeostasis", "inheritance", "ecology"],
}

COMBINED_HIGHER_TOPICS = {
    "physics": ["energy", "electricity", "particle-model", "atomic-structure", "forces", "waves", "magnetism"],
    "chemistry": ["atomic-structure", "bonding", "quantitative", "chemical-changes", "energy-changes", "rates-equilibrium", "organic", "analysis", "atmosphere", "resources"],
    "biology": ["cell-biology", "organisation", "infection-response", "bioenergetics", "homeostasis", "inheritance", "ecology"],
}

TRIPLE_FOUNDATION_TOPICS = {
    "physics": ["energy", "electricity", "particle-model", "atomic-structure", "forces", "waves", "magnetism", "space"],
    "chemistry": ["atomic-structure", "bonding", "quantitative", "chemical-changes", "energy-changes", "rates-equilibrium", "organic", "analysis", "atmosphere", "resources"],
    "biology": ["cell-biology", "organisation", "infection-response", "bioenergetics", "homeostasis", "inheritance", "ecology"],
}

TRIPLE_HIGHER_TOPICS = {
    "physics": ["energy", "electricity", "particle-model", "atomic-structure", "forces", "waves", "magnetism", "space"],
    "chemistry": ["atomic-structure", "bonding", "quantitative", "chemical-changes", "energy-changes", "rates-equilibrium", "organic", "analysis", "atmosphere", "resources"],
    "biology": ["cell-biology", "organisation", "infection-response", "bioenergetics", "homeostasis", "inheritance", "ecology"],
}

PATHWAY_TOPIC_MAP = {
    ("combined", "foundation"): COMBINED_FOUNDATION_TOPICS,
    ("combined", "higher"):     COMBINED_HIGHER_TOPICS,
    ("triple",   "foundation"): TRIPLE_FOUNDATION_TOPICS,
    ("triple",   "higher"):     TRIPLE_HIGHER_TOPICS,
}

PATHWAY_COLORS = {
    "combined": "#1D6FB8",   # combined = physics blue
    "triple":   "#B02342",   # triple = chemistry crimson
}

TIER_COLORS = {
    "foundation": "#237A3B",  # green
    "higher":     "#7A5F00",  # deep gold (light-theme readable)
}

PHYSICS_COLOR   = "#1D6FB8"
CHEMISTRY_COLOR = "#B02342"
BIOLOGY_COLOR   = "#237A3B"

# ── Shared <head> assets — every generated page loads the token
#    sheet first (with font preloads), then the consuming stylesheet ──
HEAD_ASSETS = """<link rel="preload" href="/shared/fonts/fraunces-var-latin.woff2" as="font" type="font/woff2" crossorigin/>
  <link rel="preload" href="/shared/fonts/plus-jakarta-sans-var-latin.woff2" as="font" type="font/woff2" crossorigin/>
  <link rel="stylesheet" href="/shared/tokens.css"/>
  <link rel="stylesheet" href="/shared/styles.css"/>
  <link rel="stylesheet" href="/shared/nav.css"/>
  <script src="/shared/search-index.js" defer></script>
  <script src="/shared/search.js" defer></script>
  <script src="/shared/nav.js" defer></script>
  <script src="/shared/class-entry.js" defer></script>"""

THEME_COLOR = "#F7F1E5"  # pre-paint browser chrome tint — matches --bg (light default)


# ─────────────────────────────────────────────
#  UPDATED NAV — includes pathway context
# ─────────────────────────────────────────────


def nav_html(active_subject="", pathway="", tier="", chrome=False):
    """Canonical public top-nav (MRB-109). Styling lives in shared/nav.css;
    behaviour — the auth chip and the accessible hamburger drawer — lives in
    shared/nav.js. This returns markup only.

    ⊕ MRB-301 · `chrome=True` returns Claude Design's header instead.

    The default (`chrome=False`) branch is UNCHANGED and must stay so: it is
    what every one of the ~1,000 KS4 LESSON pages renders, and MRB-301's scope
    wall is that a lesson page comes out of this run byte-for-byte identical.
    Only the seven chrome makers pass `chrome=True`.

    The chrome branch keeps the two hooks shared/nav.js binds to —
    `.nav-burger` and `#nav-auth-area` — so the sign-in chip, the "My class"
    chip and the whole drawer keep working with no change to nav.js at all.
    What changes is the drawing: Design replaced the emoji (⚡🏆🔍) with drawn
    marks, which is why this is new markup rather than new CSS over the old.

    The header crumbs are deliberately absent here: Design moved the trail
    into the page body (`k4_crumbs`), and `.nav-crumbs` is display:none in
    ks4-chrome.css so the two cannot double up."""
    if chrome:
        return f"""<nav class="nav">
  <div class="k4-navbar">
    <a class="nav-brand" href="/index.html">{K4_BRANDMARK} MrBadmusAI</a>
    <div class="nav-cluster">
      <a href="/3d/" class="nav-text-link">3D Studio</a>
      <a href="/weekly-challenge.html" class="challenge-chip"><svg viewBox="0 0 12 16" width="12" height="15" fill="currentColor" aria-hidden="true"><path d="M7.4 0L1 9.2h3.6L3.4 16 11 6.1H6.6L7.4 0z"/></svg> <span class="nav-chip-label">Challenge</span></a>
      <a href="/leaderboard.html" class="nav-icon-link" title="Leaderboard" aria-label="Leaderboard"><svg viewBox="0 0 20 20" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6.5 3h7v4.5a3.5 3.5 0 01-7 0V3zM6.5 4.2H4v1.3a2.4 2.4 0 002.4 2.4M13.5 4.2H16v1.3a2.4 2.4 0 01-2.4 2.4M10 11v3M7 17h6l-.7-2.4h-4.6L7 17z"/></svg></a>
      <a href="#" class="nav-icon-link" title="Search topics" aria-label="Search topics" onclick="if(window.MRBSearch){{MRBSearch.open();}}return false;"><svg viewBox="0 0 20 20" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true"><circle cx="9" cy="9" r="5.6"/><path d="M13.2 13.2L17 17"/></svg></a>
      <span id="nav-auth-area"></span>
      <button class="nav-burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav-drawer"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>"""

    crumbs = ""
    if pathway and tier:
        pc = PATHWAY_COLORS.get(pathway, "#1D6FB8")
        tc = TIER_COLORS.get(tier, "#7A5F00")
        crumbs = f"""
    <span class="crumb-sep">›</span>
    <a href="/{pathway}/index.html" class="crumb" style="color:{pc};">{pathway.title()} Science</a>
    <span class="crumb-sep">›</span>
    <a href="/{pathway}/{tier}/index.html" class="crumb" style="color:{tc};">{tier.title()}</a>"""
        if active_subject:
            sc = SITE_DATA[active_subject]["color"]
            sl = SITE_DATA[active_subject]["label"]
            se = SITE_DATA[active_subject]["emoji"]
            crumbs += f"""
    <span class="crumb-sep">›</span>
    <a href="/{pathway}/{tier}/{active_subject}/index.html" class="crumb" style="color:{sc};">{se} {sl}</a>"""
    elif pathway:
        pc = PATHWAY_COLORS.get(pathway, "#1D6FB8")
        crumbs = f"""
    <span class="crumb-sep">›</span>
    <a href="/{pathway}/index.html" class="crumb" style="color:{pc};">{pathway.title()} Science</a>"""

    crumbs_block = f'<div class="nav-crumbs">{crumbs}</div>' if crumbs else ""

    return f"""<nav class="nav">
  <a class="nav-brand" href="/index.html"><svg class="brand-logo" width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M4 6l4-4 4 4" stroke="url(#navGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M4 6l4-4 4 4" stroke="url(#navGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" transform="translate(4,6)"/><defs><linearGradient id="navGrad" x1="4" y1="2" x2="16" y2="12" gradientUnits="userSpaceOnUse"><stop style="stop-color:var(--brand-grad-a)"/><stop offset="1" style="stop-color:var(--brand-grad-b)"/></linearGradient></defs></svg> MrBadmusAI</a>
  {crumbs_block}
  <div class="nav-cluster">
    <a href="/3d/" class="nav-text-link">3D Studio</a>
    <a href="/weekly-challenge.html" class="challenge-chip">⚡ <span class="nav-chip-label">Challenge</span></a>
    <a href="/leaderboard.html" class="nav-icon-link" title="Leaderboard" aria-label="Leaderboard">🏆</a>
    <a href="#" class="nav-icon-link" title="Search topics" aria-label="Search topics" onclick="if(window.MRBSearch){{MRBSearch.open();}}return false;">🔍</a>
    <span id="nav-auth-area"></span>
    <button class="nav-burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav-drawer"><span></span><span></span><span></span></button>
  </div>
</nav>"""


# ─────────────────────────────────────────────────────────────────────────
#  MRB-301 · THE KS4 CHROME — Claude Design's 23 Aug 2026 delivery
# ─────────────────────────────────────────────────────────────────────────
#
# Source of truth: docs/ks3/design-reference/chrome/. Seven screens were
# delivered; SIX of them are ported below (landing, GCSE hub, tier choice,
# science picker, topic list, topic page). The seventh — Design's KS3 hub,
# with its year picker and subject picker — is VENDORED AND PARKED, not
# applied: MRB-301's scope wall puts every KS3 page out of reach, and that
# wall does not bend for a view Design happened to draw.
#
# ── THE DELIVERY IS A SAMPLE, AND WHAT THAT COST ────────────────────────
#
# Design's file is a click-through with placeholder links ("#"), directive
# attributes ({{ goHome }}, {{ isKs3 }}, {{ subjectName }}) and INVENTED
# numbers — 68%, 80%, 76%, "7 topics", "10 topics", "14th of 212",
# "3 of 7 done", "CoralTrail56". Every one of those is plausible, which is
# what makes them dangerous: nobody can tell a made-up percentage from a
# real one by looking at it. `ks4_chrome_tells.py` derives its corpus from
# the vendored delivery on every run and fails the build if any of them
# reaches a built page.
#
# So: LIVE LOGIC WINS, DESIGN'S PRESENTATION WINS. Every count below is
# computed from SITE_DATA / PATHWAY_TOPIC_MAP / the subtopic modules, or it
# is not rendered at all.
#
# ── THE PROGRESS SURFACES ARE NOT HERE, AND THAT IS THE HONEST PORT ─────
#
# Design drew a per-student progress system across five of the six screens:
# a "Jump back in" card, "6 of 24 topics", "3 of 7 done", per-topic
# Done/In progress/Not started, "Last opened: Physics · Energy". She wired
# it to a `showProgress` prop, so the switch is hers.
#
# THERE IS NO KS4 PROGRESS MODEL. Not a table, not an endpoint, not a
# client store — checked, not assumed: the backend serves
# /api/assignment/progress and /api/class/progress, both KS3, and nothing
# records that a KS4 student opened a subtopic. So `showProgress` is FALSE
# on every page here, and none of those surfaces is emitted.
#
# Faking them was the one thing that could not happen. A signed-out
# visitor showing "3 of 7 done" is a lie about a student's own work, and it
# is the exact failure `ks4_chrome_tells` exists to make impossible.
# Building the model instead is a schema change, which MRB-301 does not
# authorise. It is written up in the report as the largest thing Design
# drew that the data cannot power.
#
# What IS live: the weekly challenge and the leaderboard, both of which
# have real endpoints, both wired below.

# Design's BrandMark — a right-pointing DOUBLE chevron, the second at 0.34
# opacity. Lifted from her _ds bundle (components/general/BrandMark), not
# redrawn. ⚠️ This is NOT the KS3 lessons' mark (a single UPWARD chevron at
# stroke-width 4.6) and the two are not interchangeable; see CLAUDE.md's
# four brand presentations.
K4_BRANDMARK = ('<svg width="21" height="21" viewBox="0 0 22 22" aria-hidden="true">'
                '<path d="M3.5 3.5 L11 11 L3.5 18.5" stroke="#E4572E" stroke-width="3.4" '
                'fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                '<path d="M12 3.5 L19.5 11 L12 18.5" stroke="#E4572E" stroke-opacity="0.34" '
                'stroke-width="3.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                '</svg>')

# The one arrow in the delivery, used on every forward affordance.
K4_ARROW = ('<svg viewBox="0 0 20 12" width="19" height="12" fill="none" stroke="currentColor" '
            'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M1 6h16M12.5 1l5 5-5 5"/></svg>')

K4_ARROW_ACCENT = K4_ARROW.replace('stroke="currentColor"', 'stroke="#A93411"').replace(
    'aria-hidden="true">', 'aria-hidden="true" class="k4-row-arrow">')

# AQA's official equation sheets (follow-up to MRB-301). Combined Science
# shares one sheet across all three subjects; Triple Physics gets its own,
# larger sheet — the split AQA itself publishes, not one this site invented.
AQA_EQUATION_SHEET_COMBINED = "https://www.aqa.org.uk/files/fHDU1dLPgDwvQhfFoL805J/83b24f0c972f309cb452cdc82e3800aef7a0b2b8.pdf"
AQA_EQUATION_SHEET_TRIPLE = "https://www.aqa.org.uk/files/fHDU1dLPgDwvQhfFoL5D2R/1c3e60b181036bcbc2e37485aaaf446ba5f34d9f.pdf"

# Design's drawn subject marks, replacing the ⚡🧪🌿 emoji the live pages use.
K4_SUBJECT_MARK = {
    "physics": '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13.5 2.5L5 13.5h5.5L9.5 21.5 18 10.5h-5.5l1-8z"/></svg>',
    "chemistry": '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9.5 3h5M10.5 3v6.2L5.8 18a2.6 2.6 0 002.3 3.8h7.8a2.6 2.6 0 002.3-3.8L13.5 9.2V3M7.4 15h9.2"/></svg>',
    "biology": '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 20c0-8 5.5-14 14-14 0 8-5.5 14-14 14zM5 20c2.4-3.6 5.4-6.2 9-8"/></svg>',
}

# Design's per-subject soft grounds for the mark tile.
K4_SUBJECT_SOFT = {"physics": "#EAF2FA", "chemistry": "#FAEDF0", "biology": "#EAF3EC"}

# Design writes small counts as words ("Seven topics, four on Paper 1").
# Keeping her voice costs three lines; everything above twenty falls back
# to the digit, which no count on these pages reaches.
_K4_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
             "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]


def k4_word(n, cap=False):
    w = _K4_WORDS[n] if 0 <= n < len(_K4_WORDS) else str(n)
    return w[:1].upper() + w[1:] if cap else w


def k4_topics_for(pathway, tier, subject):
    """The topics this pathway+tier actually serves, in spec order."""
    ids = PATHWAY_TOPIC_MAP[(pathway, tier)][subject]
    return [t for t in SITE_DATA[subject]["topics"] if t["id"] in ids]


def k4_subject_counts(pathway, tier, subject):
    """Every number the science picker and topic list render, derived.

    Nothing here is authored. `total` is how many topics this pathway+tier
    serves (Combined physics 7, Triple physics 8 — the Space topic is the
    difference, and it appears because the map says so, not because a
    number was typed twice)."""
    topics = k4_topics_for(pathway, tier, subject)
    p1 = [t for t in topics if t.get("paper") == 1]
    p2 = [t for t in topics if t.get("paper") == 2]
    rp = sum(len(t.get("rp") or []) for t in topics)
    return dict(topics=topics, total=len(topics), p1=p1, p2=p2, rp=rp)


def k4_crumbs(items):
    """Design's uppercase mono trail. `items` is [(label, href_or_None)];
    the last entry is the current page and never a link."""
    parts = []
    for i, (label, href) in enumerate(items):
        if i:
            parts.append('<span class="k4-sep">›</span>')
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
    return '<div class="k4-crumbs">' + "".join(parts) + "</div>"


def k4_footer():
    """Design's footer. Every link is a real route — the delivery's were
    all `href="#"`, which is precisely the kind of placeholder that ships
    if nobody looks."""
    return f"""
<footer class="k4-footer">
  <div class="k4-footer-inner">
    <span class="k4-footer-mark">MrBadmusAI · Science revision for Years 7 to 11</span>
    <span class="k4-footer-links">
      <a href="/leaderboard.html">Leaderboard</a>
      <a href="/past-papers.html">Past papers</a>
      <a href="/3d/">3D Studio</a>
    </span>
  </div>
</footer>"""


def k4_page(title, body, description="", subject="physics", pathway="", tier="",
            topic_title="", extra_head=""):
    """The chrome shell. `data-chrome="ks4"` is the ONLY thing that lets
    shared/ks4-chrome.css apply, and no lesson page sets it."""
    desc = f'\n  <meta name="description" content="{description}"/>' if description else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="theme-color" content="#FBF3E6"/>
  <title>{title}</title>{desc}
  {HEAD_ASSETS}
  <link rel="stylesheet" href="/shared/ks4-chrome.css"/>{extra_head}
</head>
<body data-chrome="ks4">
  {nav_html(subject, pathway, tier, chrome=True)}
  {body}
  {k4_footer()}
  {chat_html()}
  <script src="/shared/mrbadmus.v2.js"></script>
  <script>MrBadmus.init({{ subject: '{subject}', topic: '{topic_title}' }});</script>
</body>
</html>"""


def chat_html():
    return """<button class="chat-fab" onclick="MrBadmus.open()" title="Ask MrBadmus AI"><span class="fab-logo"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M4 6l4-4 4 4" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M8 6l4-4 4 4" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" transform="translate(4,6)"/></svg></span><span class="fab-text">Ask MrBadmusAI</span></button>

<div class="chat-overlay" id="chatOverlay">
  <div class="chat-modal">
    <div class="chat-head">
      <div class="chat-head-info">
        <h3>Mr. Badmus AI</h3>
        <p id="chat-head-subtitle">GCSE Science Tutor</p>
      </div>
      <button class="close-btn" onclick="MrBadmus.close()">✕</button>
    </div>
    <div class="chat-msgs" id="chatMsgs"></div>
    <div class="img-preview-row" id="imgPreviewRow">
      <img id="imgPreview" src="" alt="preview"/>
      <button onclick="document.getElementById(\'imgPreview\').src=\'\';document.getElementById(\'imgPreviewRow\').style.display=\'none\';">✕</button>
    </div>
    <div class="chat-input-row" style="max-width:860px;width:100%;margin:0 auto;padding:0 24px 20px;">
      <label for="imgInput" class="img-btn" title="Upload image or paste screenshot (Ctrl+V / Cmd+V)">📷</label>
      <input type="file" id="imgInput" accept="image/*" style="display:none"/>
      <input type="text" id="ci" placeholder="Ask Mr Badmus anything... (paste screenshots with Ctrl+V)"/>
      <button class="chat-send-btn">➤</button>
    </div>
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>"""



# ─────────────────────────────────────────────
#  UPDATED SHARED JS — adds TTS + Voice Input
# ─────────────────────────────────────────────

# Extract original SHARED_JS and patch it — we inject TTS/voice at the end of the module
# The patched JS is appended to the SHARED_JS string already defined above.

SHARED_JS_PATCHED = SHARED_JS  # no voice patch





# ─────────────────────────────────────────────
#  PAGE SHELL — uses SHARED_CSS_PATCHED
# ─────────────────────────────────────────────

# ⊕ MRB-301 — UNREACHED AS OF 29 Aug 2026, and left standing on purpose.
#
# `page_shell` had exactly two callers: `make_pathway_hub` and
# `make_pathway_topic_page`. The hub moved to `k4_page` in the chrome port,
# and `make_pathway_topic_page` builds ZERO pages — measured, not assumed:
# every one of the 98 (pathway, tier, subject, topic) combinations the
# PATHWAY_TOPIC_MAP serves has subtopic data, so build_site() always takes
# the `make_pathway_topic_page_with_subtopics` branch.
#
# Neither is deleted here. `make_pathway_topic_page` is the only thing that
# still wires `make_fifa_example` and `make_quiz` into a topic page, and
# removing 200 lines of working code in a run whose whole discipline is
# "touch the chrome and nothing else" would be exactly the kind of tidying
# that turns a scoped diff into an unreviewable one. If the lesson-page run
# decides they are dead, that run can bury them.
def page_shell(title, subject, body_html, topic_id="", topic_title="", pathway="", tier=""):
    color = SITE_DATA[subject]["color"] if subject else "#1D6FB8"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="theme-color" content="{THEME_COLOR}"/>
  <title>{title} | MrBadmusAI</title>
  {HEAD_ASSETS}
  <style>
    html {{ background: var(--bg); }}
    :root {{ --subject: {color}; }}
    .go-btn {{ background: var(--subject); }}
  </style>
</head>
<body>
  {nav_html(subject, pathway, tier)}
  {body_html}
  {chat_html()}
  <script src="/shared/mrbadmus.v2.js"></script>
  <script>
    MrBadmus.init({{
      subject: '{subject or "physics"}',
      topic: '{topic_title}'
    }});
  </script>
  <script>
  // Quiz logic
  document.querySelectorAll('.quiz-opt').forEach(btn => {{
    btn.addEventListener('click', function() {{
      const card = this.closest('.quiz-card');
      if (card.dataset.answered) return;
      card.dataset.answered = '1';
      const correct = card.dataset.answer;
      const allOpts = card.querySelectorAll('.quiz-opt');
      allOpts.forEach(o => {{
        if (o.dataset.val === correct) o.classList.add('correct');
        else if (o === this) o.classList.add('wrong');
      }});
      const fb = card.querySelector('.quiz-feedback');
      if (fb) {{
        fb.classList.add('show');
        if (this.dataset.val === correct) fb.classList.add('correct-fb');
        else fb.classList.add('wrong-fb');
      }}
    }});
  }});
  </script>
</body>
</html>"""


# ─────────────────────────────────────────────
#  ROOT LANDING — the key-stage chooser  (/index.html)
# ─────────────────────────────────────────────
#
# MRB-176 ruling 1. The site now serves two key stages, so the first thing a
# visitor sees is which one they are in — not a GCSE pathway picker that a Year
# 7 has no way to answer.
#
# `/index.html` stays the site's home and the nav-brand target (CLAUDE.md's
# brand rule is unchanged); what MOVED is the GCSE landing experience, which now
# lives at `/ks4.html` behind the GCSE card. MRB-137's landing redesign — the
# `landing-band` two-column layout with the Top Stars rail — is carried across
# verbatim by `make_ks4_landing()` below. It is In Review and is reconciled
# behind the card, not re-implemented.


def make_landing():
    """The key-stage chooser — Claude Design's landing (MRB-301).

    Two doors and one live strip. The chooser itself is unchanged in
    FUNCTION from MRB-176: a Year 7 still cannot be asked a GCSE pathway
    question, so the first decision is still KS3 or GCSE.

    ⚠️ The KS3 door routes into the EXISTING, UNTOUCHED KS3 estate at
    /ks3/index.html. MRB-301 restyles the door, never what is behind it."""
    body = f"""
<main class="k4-main k4-home">

  <section class="k4-band">
    <div class="k4-band-copy" style="flex:1 1 480px;animation:k4-rise .5s both">
      <h1 class="k4-h1 k4-h1-hero">Revision that<br>keeps score.</h1>
      <p class="k4-lede">Free science for Years 7 to 11 — biology, chemistry and physics,
      with an AI tutor that never tires of the same question.</p>
    </div>
  </section>

  <section class="k4-doors">
    <a class="k4-door" href="/ks3/index.html" style="--k4-door-hue:#E4572E">
      <div class="k4-eyebrow"><span class="k4-dot" style="background:#E4572E"></span>Years 7 to 9</div>
      <h2>KS3 Science</h2>
      <p>The whole national curriculum programme of study, across all three sciences — the science everything at GCSE is built on.</p>
      <div class="k4-pills">
        <span class="k4-pill">Year 7</span>
        <span class="k4-pill">Year 8</span>
        <span class="k4-pill">Year 9</span>
      </div>
      <span class="k4-door-foot">Start KS3 {K4_ARROW}</span>
    </a>

    <a class="k4-door" href="/ks4.html" style="--k4-door-hue:#1D6FB8;animation-delay:.06s">
      <div class="k4-eyebrow"><span class="k4-dot" style="background:#1D6FB8"></span>Years 10 and 11</div>
      <h2>GCSE Science</h2>
      <p>Combined and Triple Science, Foundation and Higher — full topic notes, worked examples, quizzes, past papers and the weekly challenge.</p>
      <div class="k4-pills">
        <span class="k4-pill">Combined</span>
        <span class="k4-pill">Triple</span>
        <span class="k4-pill">Foundation</span>
        <span class="k4-pill">Higher</span>
      </div>
      <span class="k4-door-foot">Start GCSE {K4_ARROW}</span>
    </a>
  </section>

  {k4_challenge_strip()}
</main>"""

    return k4_page(
        "MrBadmusAI — Free KS3 &amp; GCSE Science Revision",
        body,
        description="Free science revision for Years 7 to 11. KS3 Science for Years 7–9 and GCSE Combined and Triple Science for Years 10–11, with an AI tutor, quizzes and full topic notes.",
        extra_head='\n  <script src="/shared/ks4-chrome.js" defer></script>')


def k4_challenge_strip():
    """Design's "This week's challenge" strip, with nothing invented in it.

    Server-rendered: the kicker, the true copy, and the call to action —
    all three are facts about the product, not about a student.

    Client-filled (shared/ks4-chrome.js, one public GET): the two tier
    leaders. Each cell ships `hidden` and is REMOVED if its tier has no
    entrant this week, so an empty week renders as an empty week.

    ⚠️ Design's drawn cells were "Your best 68%", "Beat it and you move up
    4 places" and "Your rank 14th of 212". All three are per-student
    numbers behind an authenticated read, and all three were invented in
    the delivery. They are not here; /leaderboard.html is where a student's
    own position lives."""
    return f"""
  <section class="k4-challenge" id="k4-challenge">
    <div class="k4-challenge-cell">
      <div class="k4-kicker k4-kicker-accent">This week's challenge</div>
      <p class="k4-challenge-head">Ten minutes, one science</p>
      <p class="k4-challenge-sub">New questions every Friday — biology, chemistry and physics, at your own tier.</p>
    </div>
    <div class="k4-challenge-cell" id="k4-lead-foundation" hidden>
      <div class="k4-kicker">Leading · Foundation</div>
      <p class="k4-challenge-head" data-k4-name></p>
      <p class="k4-challenge-sub"><span data-k4-pct></span> so far this week</p>
    </div>
    <div class="k4-challenge-cell" id="k4-lead-higher" hidden>
      <div class="k4-kicker">Leading · Higher</div>
      <p class="k4-challenge-head" data-k4-name></p>
      <p class="k4-challenge-sub"><span data-k4-pct></span> so far this week</p>
    </div>
    <div class="k4-challenge-cell k4-challenge-go">
      <a class="k4-cta-solid" href="/weekly-challenge.html">Take the challenge {K4_ARROW}</a>
    </div>
  </section>"""



def make_ks4_landing():
    """The GCSE hub at /ks4.html — Claude Design's "GCSE hub" (MRB-301).

    Two pathway doors and the Top Stars rail. MRB-137's rail is not
    re-implemented: it is the SAME endpoint, the same percentage rule, the
    same Foundation/Higher crossfade and the same both-tiers-iterated fix,
    moved into shared/ks4-chrome.js and dressed in Design's dark card."""
    body = f"""
<main class="k4-main">
  {k4_crumbs([("All courses", "/index.html"), ("GCSE Science", None)])}

  <section class="k4-band" style="margin-bottom:34px">
    <div class="k4-band-copy">
      <div class="k4-eyebrow">Key Stage 4 · Years 10 and 11</div>
      <h1 class="k4-h1">GCSE Science</h1>
    </div>
    <div class="k4-band-side k4-note">
      <div class="k4-kicker">Not sure which?</div>
      <p>Combined gives you two GCSEs in science. Triple gives you three separate ones. Your timetable will say which.</p>
    </div>
  </section>

  <section class="k4-split">
    <div class="k4-split-main" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;align-items:start">
      <a class="k4-door k4-door-sm" href="/combined/index.html" style="--k4-door-hue:#1D6FB8">
        <div class="k4-eyebrow"><span class="k4-dot k4-dot-sm" style="background:#1D6FB8"></span>Two GCSEs</div>
        <h2>Combined Science</h2>
        <p>Biology, chemistry and physics in one course. Six exams, two grades.</p>
        <div class="k4-pills">
          <span class="k4-pill k4-pill-foundation">Foundation</span>
          <span class="k4-pill k4-pill-higher">Higher</span>
        </div>
        <span class="k4-door-foot">Open Combined {K4_ARROW}</span>
      </a>

      <a class="k4-door k4-door-sm" href="/triple/index.html" style="--k4-door-hue:#B02342">
        <div class="k4-eyebrow"><span class="k4-dot k4-dot-sm" style="background:#B02342"></span>Three GCSEs</div>
        <h2>Triple Science</h2>
        <p>Each science graded on its own. More content, six exams, three grades.</p>
        <div class="k4-pills">
          <span class="k4-pill k4-pill-foundation">Foundation</span>
          <span class="k4-pill k4-pill-higher">Higher</span>
        </div>
        <span class="k4-door-foot">Open Triple {K4_ARROW}</span>
      </a>
    </div>

    {k4_stars_rail()}
  </section>
</main>"""

    return k4_page(
        "MrBadmusAI — GCSE Science Revision",
        body,
        description="Free GCSE Science revision with AI tutor, FIFA worked examples, quizzes and full topic notes. Physics, Chemistry, Biology.",
        extra_head='\n  <script src="/shared/ks4-chrome.js" defer></script>')


def k4_stars_rail():
    """Design's "Top stars" aside. Every row is filled by
    shared/ks4-chrome.js from /api/weekly-leaderboard/landing.

    Ships EMPTY on purpose. The server has no idea who is on the board, so
    rendering a placeholder row would mean a real name replacing a fake one
    after paint — and if the fetch failed, the fake one would simply stay.
    The no-data state is the honest first frame: "No stars yet".

    ⚠️ Design drew a third row reading "14 · You · 68%". A viewer's own
    position needs an authenticated /board read with their tier; it is not
    rendered here and is not invented. /leaderboard.html has it."""
    return f"""
    <aside class="k4-stars" id="k4-stars" aria-label="Top stars of the week">
      <div>
        <div class="k4-kicker k4-kicker-ondark">Top stars</div>
        <p class="k4-stars-title">This week's leaders</p>
      </div>

      <div class="k4-champ" id="k4-champ" hidden>
        <div class="k4-champ-kicker">Champion of the week</div>
        <div class="k4-champ-row">
          <span class="k4-champ-name" data-k4-champ-name></span>
          <span class="k4-champ-pct" data-k4-champ-pct></span>
        </div>
      </div>

      <div class="k4-stars-slides" id="k4-stars-slides">
        <div class="k4-stars-slide" data-k4-slide="foundation" role="tabpanel" aria-label="Foundation top stars" aria-hidden="true">
          <div class="k4-stars-slide-head">Foundation</div>
          <div data-k4-rows="foundation"><p class="k4-stars-empty">No stars yet — be the first.</p></div>
        </div>
        <div class="k4-stars-slide" data-k4-slide="higher" role="tabpanel" aria-label="Higher top stars" aria-hidden="true">
          <div class="k4-stars-slide-head">Higher</div>
          <div data-k4-rows="higher"><p class="k4-stars-empty">No stars yet — be the first.</p></div>
        </div>
      </div>

      <div class="k4-stars-foot">
        <div class="k4-stars-dots" id="k4-stars-dots" role="tablist" aria-label="Choose tier" hidden>
          <button class="k4-stars-dot" type="button" role="tab" data-tier="foundation" aria-selected="false" aria-label="Show Foundation stars"></button>
          <button class="k4-stars-dot" type="button" role="tab" data-tier="higher" aria-selected="false" aria-label="Show Higher stars"></button>
        </div>
        <a class="k4-cta-light" href="/leaderboard.html">Full leaderboard {K4_ARROW}</a>
      </div>
    </aside>"""



def make_pathway_page(pathway):
    """Combined or Triple → choose a tier. Design's "Tier choice" screen.

    ⚠️ In the delivery BOTH tier cards called `goFoundation` — a
    click-through convenience that would have shipped as a Higher card
    that opens Foundation. Each card routes to its own tier here.

    "Two GCSEs · N topics" is derived across the three sciences for THIS
    pathway, so Combined reads 24 and Triple reads 25 (the Space topic).
    Design's drawing said 24 for both."""
    label = "Combined Science" if pathway == "combined" else "Triple Science"
    hue = PATHWAY_COLORS[pathway]

    # The topic count is identical at both tiers (the tier changes the
    # depth, not which topics are served), so Foundation's map answers for
    # the pathway. Asserted rather than assumed — see below.
    total = sum(len(PATHWAY_TOPIC_MAP[(pathway, "foundation")][s])
                for s in ["physics", "chemistry", "biology"])
    total_h = sum(len(PATHWAY_TOPIC_MAP[(pathway, "higher")][s])
                  for s in ["physics", "chemistry", "biology"])
    if total != total_h:
        # If the two tiers ever diverge, the single headline number stops
        # being true and a silent wrong count is worse than a loud build.
        raise SystemExit(
            f"generate_site_v5: {pathway} serves {total} topics at Foundation "
            f"and {total_h} at Higher — the tier-choice headline can no longer "
            f"be one number. Split it before shipping.")

    eyebrow = (f"Two GCSEs · {total} topics" if pathway == "combined"
               else f"Three GCSEs · {total} topics · extended content")
    blurb = ("Biology, chemistry and physics in one course. Six exams, two grades."
             if pathway == "combined"
             else "Each science graded on its own. More content, six exams, three grades.")

    tiers = ""
    for tier, tier_hue, grades, note in [
        ("foundation", "#237A3B", "Grades 1 to 5",
         "Every idea on the specification, at the depth Foundation papers ask for."),
        ("higher", "#7A5F00", "Grades 4 to 9",
         "Everything at Foundation plus the Higher-only material — more equations, more depth."),
    ]:
        tiers += f"""
    <a class="k4-door" href="/{pathway}/{tier}/index.html" style="--k4-door-hue:{tier_hue}">
      <div class="k4-eyebrow"><span class="k4-dot k4-dot-sm" style="background:{tier_hue}"></span>{grades}</div>
      <h2>{tier.title()}</h2>
      <p>{note}</p>
      <span class="k4-door-foot">Open {tier.title()} {K4_ARROW}</span>
    </a>"""

    body = f"""
<main class="k4-main">
  {k4_crumbs([("All courses", "/index.html"), ("GCSE Science", "/ks4.html"), (label.split()[0], None)])}

  <section class="k4-band" style="margin-bottom:34px">
    <div class="k4-band-copy">
      <div class="k4-eyebrow"><span class="k4-dot" style="background:{hue}"></span>{eyebrow}</div>
      <h1 class="k4-h1">{label}</h1>
      <p class="k4-lede">{blurb}</p>
    </div>
    <div class="k4-band-side k4-note">
      <div class="k4-kicker">Which tier am I?</div>
      <p>Your school enters you for one of them. If nobody has told you yet, ask your teacher.</p>
    </div>
  </section>

  <section class="k4-grid-2">{tiers}
  </section>
</main>"""

    return k4_page(f"{label} | MrBadmusAI", body, pathway=pathway)



def make_tier_page(pathway, tier):
    """The science picker — Design's "Foundation subjects" screen, at both
    tiers and both pathways.

    Every number on the three cards is derived: how many topics this
    pathway+tier serves, how they split across the two papers, and how
    many required practicals sit inside them. Design's drawing said
    "7 topics / Paper 1 · 4 / Paper 2 · 3 / 11 RP" for physics; those
    happen to be right for Combined, and wrong the moment you look at
    Triple — which is exactly why they are computed here.

    ⚠️ Design's "Your tier so far — 6 of 24 topics" card is absent. There
    is no KS4 progress model to fill it (see the MRB-301 banner above
    K4_BRANDMARK), and a signed-out visitor being shown someone's progress
    is the failure this port is built to avoid."""
    pathway_label = "Combined Science" if pathway == "combined" else "Triple Science"
    tier_hue = TIER_COLORS[tier]

    cards = ""
    for subj in ["physics", "chemistry", "biology"]:
        data = SITE_DATA[subj]
        c = k4_subject_counts(pathway, tier, subj)
        hue = data["color"]
        first = c["topics"][0]["title"] if c["topics"] else ""
        last = c["topics"][-1]["title"] if c["topics"] else ""
        # Design's own blurbs are first-topic-through-to-last-topic
        # summaries ("Atoms and bonding through to the atmosphere and
        # using resources"), so this keeps her sentence shape and lets the
        # spec write it.
        blurb = f"{first} through to {last}." if first and last else ""
        rp_tag = (f'<span class="k4-tag">{c["rp"]} RP</span>' if c["rp"] else "")
        cards += f"""
    <a class="k4-door k4-door-sm k4-subject" href="/{pathway}/{tier}/{subj}/index.html" style="--k4-door-hue:{hue}">
      <div class="k4-subject-top">
        <span class="k4-subject-mark" style="background:{K4_SUBJECT_SOFT[subj]};color:{hue}">{K4_SUBJECT_MARK[subj]}</span>
        <span class="k4-count">{c["total"]} topic{"s" if c["total"] != 1 else ""}</span>
      </div>
      <h2>{data["label"]}</h2>
      <p>{blurb}</p>
      <div class="k4-pills">
        <span class="k4-tag">Paper 1 · {len(c["p1"])}</span>
        <span class="k4-tag">Paper 2 · {len(c["p2"])}</span>
        {rp_tag}
      </div>
      <span class="k4-door-foot">Open {data["label"]} {K4_ARROW}</span>
    </a>"""

    body = f"""
<main class="k4-main">
  {k4_crumbs([("All courses", "/index.html"),
              ("GCSE Science", "/ks4.html"),
              (pathway.title(), f"/{pathway}/index.html"),
              (tier.title(), None)])}

  <section class="k4-band" style="margin-bottom:34px">
    <div class="k4-band-copy">
      <div class="k4-eyebrow"><span class="k4-dot" style="background:{tier_hue}"></span>{pathway_label} · {tier.title()}</div>
      <h1 class="k4-h1">Pick a science</h1>
    </div>
  </section>

  <section class="k4-grid-3">{cards}
  </section>
</main>"""

    return k4_page(f"{pathway_label} {tier.title()} | MrBadmusAI", body,
                   pathway=pathway, tier=tier)



def make_pathway_hub(pathway, tier, subject):
    """The topic list — Design's "Topic list" screen, the one she shipped
    as a template ({{ subjectName }}, {{ paper1 }}, {{ paper2 }}).

    This is the LAST page MRB-301 touches. Every row opens a topic page;
    the lesson pages behind those are the next run and are untouched.

    ⚠️ Design's rows each carried a `state` — DONE / IN PROGRESS / NOT
    STARTED — and a "This subject · 2 of 7 done" card. Both need a KS4
    progress model that does not exist, so neither is emitted."""
    data = SITE_DATA[subject]
    hue = data["color"]
    label = data["label"]
    pathway_label = "Combined Science" if pathway == "combined" else "Triple Science"
    c = k4_subject_counts(pathway, tier, subject)

    # Design's lede is a sentence made entirely of counts. Written from the
    # spec rather than typed, so Triple's eighth physics topic changes it.
    rp_sentence = (f" {k4_word(c['rp'], cap=True)} required practical"
                   f"{'s' if c['rp'] != 1 else ''} across them."
                   if c["rp"] else "")
    lede = (f"{k4_word(c['total'], cap=True)} topic{'s' if c['total'] != 1 else ''}, "
            f"{k4_word(len(c['p1']))} on Paper 1 and {k4_word(len(c['p2']))} on Paper 2."
            f"{rp_sentence}")

    def rows(topic_list, offset):
        if not topic_list:
            return ""
        out = ""
        for i, t in enumerate(topic_list):
            n_rp = len(t.get("rp") or [])
            meta = f"Spec {t['spec']}"
            if n_rp:
                meta += f" &nbsp;·&nbsp; {n_rp} required practical{'s' if n_rp > 1 else ''}"
            badges = ""
            if t.get("higher") and tier == "higher":
                badges += '<span class="k4-tag">Higher</span>'
            if t.get("triple_only") and pathway == "triple":
                badges += '<span class="k4-tag">Triple</span>'
            out += f"""
        <a class="k4-row" href="/{pathway}/{tier}/{subject}/{t['id']}.html">
          <span class="k4-row-num">{str(offset + i + 1).zfill(2)}</span>
          <span class="k4-row-body">
            <span class="k4-row-title">{t['title']}</span>
            <span class="k4-row-meta">{meta}</span>
          </span>
          {badges}
          {K4_ARROW_ACCENT}
        </a>"""
        return out

    sections = ""
    n = 0
    for paper_label, group in [("Paper 1", c["p1"]), ("Paper 2", c["p2"])]:
        if not group:
            continue
        sections += f"""
      <div class="k4-section-head"{' style="margin-top:36px"' if sections else ''}>
        <span class="k4-section-label">{paper_label}</span>
        <span class="k4-rule"></span>
      </div>
      <div class="k4-list">{rows(group, n)}
      </div>"""
        n += len(group)

    # A topic that names neither paper would otherwise vanish from the only
    # page that lists it. Nothing in the spec data does today; if that ever
    # changes, it shows up here rather than disappearing.
    stray = [t for t in c["topics"] if t.get("paper") not in (1, 2)]
    if stray:
        sections += f"""
      <div class="k4-section-head" style="margin-top:36px">
        <span class="k4-section-label">Also on this course</span>
        <span class="k4-rule"></span>
      </div>
      <div class="k4-list">{rows(stray, n)}
      </div>"""

    body = f"""
<main class="k4-main">
  {k4_crumbs([("GCSE Science", "/ks4.html"),
              (pathway.title(), f"/{pathway}/index.html"),
              (tier.title(), f"/{pathway}/{tier}/index.html"),
              (label, None)])}

  <section class="k4-band" style="margin-bottom:36px">
    <div class="k4-band-copy">
      <div class="k4-eyebrow"><span class="k4-dot" style="background:{hue}"></span>{pathway_label} · {tier.title()}</div>
      <h1 class="k4-h1">{label}</h1>
      <p class="k4-lede">{lede}</p>
    </div>
  </section>

  <section>{sections}
  </section>
</main>"""

    return k4_page(f"{label} | {tier.title()} | {pathway_label} | MrBadmusAI",
                   body, subject=subject, pathway=pathway, tier=tier)


def make_pathway_topic_page(pathway, tier, subject, topic):
    # ⊕ MRB-301 — UNREACHED. See the note above `page_shell`. Deliberately
    # NOT ported to the new chrome: it builds no pages, and porting a page
    # nobody can reach would have been untestable work inside a scope wall.
    data = SITE_DATA[subject]
    color = data["color"]
    emoji = data["emoji"]
    pathway_label = "Combined Science" if pathway == "combined" else "Triple Science"

    # Filter subtopics: Foundation hides Higher-only bullets if tier==foundation
    subtopic_items = ""
    for s in topic["subtopics"]:
        is_higher_only = "(Higher only)" in s or "(Higher Only)" in s
        if is_higher_only and tier == "foundation":
            continue  # hide Higher-only subtopics from Foundation
        subtopic_items += f'<li><span style="color:{color}">●</span> {s}</li>\n'

    # Filter equations (show all for higher, filter for foundation)
    formula_pills = ""
    if topic.get("equations"):
        for eq in topic["equations"]:
            is_higher = "(Higher)" in eq or "(higher)" in eq
            if is_higher and tier == "foundation":
                continue
            formula_pills += f'<div class="formula-pill">{eq}</div>\n'
    if not formula_pills:
        formula_pills = '<p style="color:var(--muted);font-size:0.9rem;">No specific equations for this topic.</p>'

    # FIFA example
    fifa_html = make_fifa_example(subject, topic)

    # Higher tier box — only show on Higher pages
    higher_html = ""
    if tier == "higher" and topic.get("higher"):
        for h in topic["higher"]:
            higher_html += f'<div class="higher-box"><p>{h}</p></div>'
        higher_html = f"""<div class="section">
  <div class="section-title">⭐ Higher Tier Content</div>
  {higher_html}
</div>"""

    # Triple only box — only show on Triple pages
    triple_html = ""
    if pathway == "triple" and topic.get("triple_only"):
        for tr in topic["triple_only"]:
            triple_html += f'<div class="triple-box"><p>{tr}</p></div>'
        triple_html = f"""<div class="section">
  <div class="section-title">🔬 Triple Science Extensions</div>
  {triple_html}
</div>"""

    # RP section
    rp_html = ""
    for rp in topic.get("rp", []):
        rp_name = rp.split("—")[1].strip() if "—" in rp else rp
        rp_html += f"""<div class="rp-card">
  <h4>🔬 {rp}</h4>
  <p style="font-size:0.88rem;color:var(--muted);">Required Practical — know the method, variables and analysis.</p>
</div>"""
    if not rp_html:
        rp_html = '<p style="color:var(--muted);font-size:0.9rem;">No required practicals for this topic.</p>'

    # Quiz
    quiz_html = make_quiz(subject, topic, color)

    # Next/Prev navigation
    topic_ids = PATHWAY_TOPIC_MAP[(pathway, tier)][subject]
    topics_in_path = [t for t in data["topics"] if t["id"] in topic_ids]
    curr_idx = next((i for i, t in enumerate(topics_in_path) if t["id"] == topic["id"]), None)

    nav_prev = nav_next = ""
    if curr_idx is not None:
        if curr_idx > 0:
            prev_t = topics_in_path[curr_idx - 1]
            nav_prev = f'<a class="nav-arrow prev" href="/{pathway}/{tier}/{subject}/{prev_t["id"]}.html"><span><div class="nav-arrow-label">Previous</div><div class="nav-arrow-title">{prev_t["title"]}</div></span></a>'
        else:
            nav_prev = '<span></span>'
        if curr_idx < len(topics_in_path) - 1:
            next_t = topics_in_path[curr_idx + 1]
            nav_next = f'<a class="nav-arrow next" href="/{pathway}/{tier}/{subject}/{next_t["id"]}.html"><span><div class="nav-arrow-label">Next</div><div class="nav-arrow-title">{next_t["title"]}</div></span></a>'
        else:
            nav_next = '<span></span>'

    subtopic_nav_html = f"""<div class="subtopic-nav">
  {nav_prev}
  <a href="/{pathway}/{tier}/{subject}/index.html" style="font-size:0.8rem;color:var(--muted);text-decoration:none;">📋 All {data['label']} Topics</a>
  {nav_next}
</div>"""

    body = f"""
<div class="topic-header">
  <a class="back-link" href="/{pathway}/{tier}/{subject}/index.html">← Back to {data['label']}</a>
  <div class="topic-kicker">{data['label']} · {pathway_label}</div>
  <h1>{topic['title']}</h1>
  <div class="meta-row">
    <span class="spec-pill">Spec {topic['spec']}</span>
    <span class="paper-pill">Paper {topic['paper']}</span>
    <span class="tier-pill">{'📗 Foundation' if tier=='foundation' else '📙 Higher'}</span>
  </div>
</div>

<div class="content-area">

  <div class="section">
    <div class="section-title">📋 What You Need to Know</div>
    <div class="card">
      <ul class="subtopic-list">
        {subtopic_items}
      </ul>
    </div>
  </div>

  <div class="section">
    <div class="section-title">📐 Key Equations</div>
    <div class="formula-grid">
      {formula_pills}
    </div>
  </div>

  <div class="section">
    <div class="section-title">⚽ FIFA Worked Example</div>
    {fifa_html}
  </div>

  {higher_html}
  {triple_html}

  <div class="section">
    <div class="section-title">🧪 Required Practicals</div>
    {rp_html}
  </div>

  <div class="section">
    <div class="section-title">🎯 Quick Quiz</div>
    {quiz_html}
  </div>

  <div class="section">
    <div class="section-title">🤖 Ask Mr Badmus AI</div>
    <div class="card ask-card">
      <p class="ask-lede">Stuck on {topic['title']}? Ask me anything!</p>
      <p class="ask-sub">I'll use FIFA for calculations and flag Higher/Triple content clearly.</p>
      <button data-open-chat class="btn-primary">💬 Ask Mr Badmus AI</button>
    </div>
  </div>

  {subtopic_nav_html}

</div>"""

    return page_shell(f"{topic['title']} | {data['label']} | {tier.title()}",
                      subject, body, topic["id"], topic["title"], pathway, tier)

def make_fifa_example(subject, topic):
    """Generate a relevant FIFA worked example per topic."""
    examples = {
        ("physics", "energy"): {
            "q": "A 2 kg ball falls 5 m. Calculate its gain in gravitational potential energy. (g = 10 N/kg)",
            "steps": [
                ("F", "GPE = m × g × h"),
                ("I", "GPE = 2 × 10 × 5"),
                ("F", "No unit conversion needed"),
                ("A", "GPE = <strong>100 J</strong>"),
            ]
        },
        ("physics", "electricity"): {
            "q": "A resistor has a potential difference of 12 V across it and a current of 3 A flowing through it. Calculate its resistance.",
            "steps": [
                ("F", "R = V ÷ I"),
                ("I", "R = 12 ÷ 3"),
                ("F", "No conversion needed"),
                ("A", "R = <strong>4 Ω</strong>"),
            ]
        },
        ("physics", "particle-model"): {
            "q": "Calculate the density of an object with mass 200 g and volume 50 cm³.",
            "steps": [
                ("F", "ρ = m ÷ V"),
                ("I", "ρ = 200 ÷ 50"),
                ("F", "Convert: 200 g = 0.2 kg, 50 cm³ = 0.00005 m³ → ρ = 0.2 ÷ 0.00005"),
                ("A", "ρ = <strong>4000 kg/m³</strong>"),
            ]
        },
        ("physics", "atomic-structure"): {
            "q": "A radioactive sample has an initial count rate of 800 counts/min. Its half-life is 20 minutes. What is the count rate after 60 minutes?",
            "steps": [
                ("F", "Each half-life → count rate halves"),
                ("I", "60 min ÷ 20 min = 3 half-lives"),
                ("F", "800 → 400 → 200 → 100"),
                ("A", "Count rate = <strong>100 counts/min</strong>"),
            ]
        },
        ("physics", "forces"): {
            "q": "A car of mass 1200 kg accelerates at 3 m/s². Calculate the resultant force.",
            "steps": [
                ("F", "F = m × a"),
                ("I", "F = 1200 × 3"),
                ("F", "No conversion needed"),
                ("A", "F = <strong>3600 N</strong>"),
            ]
        },
        ("physics", "waves"): {
            "q": "A wave has a frequency of 200 Hz and a wavelength of 1.5 m. Calculate the wave speed.",
            "steps": [
                ("F", "v = f × λ"),
                ("I", "v = 200 × 1.5"),
                ("F", "No conversion needed"),
                ("A", "v = <strong>300 m/s</strong>"),
            ]
        },
        ("physics", "magnetism"): {
            "q": "A transformer has 200 turns on the primary and 1000 turns on the secondary. The primary voltage is 230 V. Find the secondary voltage.",
            "steps": [
                ("F", "Vp/Vs = Np/Ns → Vs = Vp × (Ns/Np)"),
                ("I", "Vs = 230 × (1000/200)"),
                ("F", "Vs = 230 × 5"),
                ("A", "Vs = <strong>1150 V</strong>"),
            ]
        },
        ("physics", "space"): {
            "q": "As a star runs out of hydrogen fuel, it expands into a red giant. Explain what happens next for a star similar in mass to our Sun.",
            "steps": [
                ("F", "Identify the stellar life cycle stage"),
                ("I", "Sun-like mass → red giant → outer layers shed"),
                ("F", "Core remains as dense remnant"),
                ("A", "<strong>Planetary nebula</strong> forms, core becomes a <strong>white dwarf</strong>"),
            ]
        },
        ("chemistry", "atomic-structure"): {
            "q": "An atom has 11 protons and 12 neutrons. State its atomic number, mass number and symbol.",
            "steps": [
                ("F", "Atomic number = protons. Mass number = protons + neutrons"),
                ("I", "Atomic number = 11 (this is Sodium, Na). Mass number = 11 + 12 = 23"),
                ("F", "No calculation needed"),
                ("A", "Atomic number = <strong>11</strong>, mass number = <strong>23</strong>, symbol = <strong>²³₁₁Na</strong>"),
            ]
        },
        ("chemistry", "quantitative"): {
            "q": "Calculate the number of moles in 44 g of CO₂. (Ar: C=12, O=16)",
            "steps": [
                ("F", "mol = mass ÷ Mr"),
                ("I", "Mr of CO₂ = 12 + (16×2) = 44. mol = 44 ÷ 44"),
                ("F", "No conversion needed"),
                ("A", "mol = <strong>1 mol</strong>"),
            ]
        },
        ("chemistry", "bonding"): {
            "q": "Explain why sodium chloride (NaCl) has a high melting point.",
            "steps": [
                ("F", "Identify the bonding type and structure"),
                ("I", "NaCl is ionic — Na⁺ and Cl⁻ ions in a giant lattice"),
                ("F", "Many strong electrostatic forces of attraction between oppositely charged ions"),
                ("A", "Requires <strong>lots of energy</strong> to break the lattice → <strong>high melting point</strong>"),
            ]
        },
        ("chemistry", "chemical-changes"): {
            "q": "Zinc reacts with sulfuric acid. Write the word equation and state the type of reaction.",
            "steps": [
                ("F", "Acid + metal → salt + hydrogen"),
                ("I", "Zinc + sulfuric acid → zinc sulfate + hydrogen"),
                ("F", "Zinc is above hydrogen in the reactivity series — it displaces H₂"),
                ("A", "Zinc + sulfuric acid → zinc sulfate + <strong>hydrogen</strong>. Type: <strong>displacement/acid-metal reaction</strong>"),
            ]
        },
        ("chemistry", "energy-changes"): {
            "q": "In a reaction, 800 kJ/mol of energy is needed to break bonds and 950 kJ/mol is released when bonds form. Is the reaction exothermic or endothermic? Calculate ΔH.",
            "steps": [
                ("F", "ΔH = energy in (breaking bonds) − energy out (forming bonds)"),
                ("I", "ΔH = 800 − 950"),
                ("F", "Negative ΔH = exothermic"),
                ("A", "ΔH = <strong>−150 kJ/mol</strong> → <strong>Exothermic</strong> reaction"),
            ]
        },
        ("chemistry", "rates-equilibrium"): {
            "q": "A student times how long it takes for a cross to disappear in the sodium thiosulfate + HCl experiment. The result is 25 seconds. Calculate the rate of reaction.",
            "steps": [
                ("F", "Rate = 1 ÷ time"),
                ("I", "Rate = 1 ÷ 25"),
                ("F", "No conversion needed"),
                ("A", "Rate = <strong>0.04 s⁻¹</strong>"),
            ]
        },
        ("chemistry", "organic"): {
            "q": "Name the alkane with 4 carbon atoms and state its molecular formula.",
            "steps": [
                ("F", "Alkanes follow CₙH₂ₙ₊₂"),
                ("I", "n = 4 → H = 2(4)+2 = 10"),
                ("F", "4 carbons = but- prefix"),
                ("A", "Name: <strong>Butane</strong>, Formula: <strong>C₄H₁₀</strong>"),
            ]
        },
        ("chemistry", "analysis"): {
            "q": "In a chromatography experiment, a spot travels 4.5 cm and the solvent front travels 9 cm. Calculate the Rf value.",
            "steps": [
                ("F", "Rf = distance moved by spot ÷ distance moved by solvent"),
                ("I", "Rf = 4.5 ÷ 9"),
                ("F", "No units — Rf has no units"),
                ("A", "Rf = <strong>0.5</strong>"),
            ]
        },
        ("chemistry", "atmosphere"): {
            "q": "State the approximate percentages of nitrogen and oxygen in the Earth's atmosphere.",
            "steps": [
                ("F", "Recall atmospheric composition"),
                ("I", "Nitrogen ≈ 78%, Oxygen ≈ 21%, other gases ≈ 1%"),
                ("F", "Nitrogen is most abundant, oxygen second"),
                ("A", "Nitrogen ≈ <strong>78%</strong>, Oxygen ≈ <strong>21%</strong>"),
            ]
        },
        ("chemistry", "resources"): {
            "q": "The Haber process makes ammonia. State the conditions used and explain why a moderate temperature is chosen.",
            "steps": [
                ("F", "N₂ + 3H₂ ⇌ 2NH₃ (reversible reaction)"),
                ("I", "Conditions: 450°C, 200 atm, iron catalyst"),
                ("F", "High temp: faster rate but lower yield (forward reaction is exothermic). Compromise at 450°C"),
                ("A", "450°C gives a <strong>reasonable rate</strong> and <strong>acceptable yield</strong> — economic balance"),
            ]
        },
        ("biology", "cell-biology"): {
            "q": "A cell has an image size of 30 mm on a slide. The actual size of the cell is 0.03 mm. Calculate the magnification.",
            "steps": [
                ("F", "Magnification = image size ÷ actual size"),
                ("I", "M = 30 ÷ 0.03"),
                ("F", "No unit conversion — both in mm"),
                ("A", "Magnification = <strong>×1000</strong>"),
            ]
        },
        ("biology", "organisation"): {
            "q": "An enzyme works at its optimum pH of 7. Explain what happens to the rate of reaction if the pH drops to 2.",
            "steps": [
                ("F", "pH affects the shape of the active site"),
                ("I", "pH 2 is acidic — far from optimum pH 7"),
                ("F", "H⁺ ions denature the enzyme — active site shape changes"),
                ("A", "Substrate can no longer bind → <strong>rate of reaction decreases to zero</strong> — enzyme is <strong>denatured</strong>"),
            ]
        },
        ("biology", "infection-response"): {
            "q": "Explain how vaccination prevents the spread of a disease through a population.",
            "steps": [
                ("F", "Vaccination introduces a weakened/dead pathogen or antigen"),
                ("I", "Immune system produces antibodies and memory cells"),
                ("F", "If enough people are vaccinated → herd immunity"),
                ("A", "Memory cells allow a <strong>faster, stronger response</strong> if real pathogen is encountered. Herd immunity <strong>protects vulnerable individuals</strong> who cannot be vaccinated"),
            ]
        },
        ("biology", "bioenergetics"): {
            "q": "Light intensity is doubled in a photosynthesis experiment. Explain the effect on the rate of photosynthesis.",
            "steps": [
                ("F", "Identify limiting factors"),
                ("I", "If light is the limiting factor, doubling intensity increases rate"),
                ("F", "But if CO₂ or temperature is the limiting factor, increasing light has no effect"),
                ("A", "Rate <strong>increases</strong> if light is the limiting factor, until <strong>another factor</strong> becomes limiting"),
            ]
        },
        ("biology", "homeostasis"): {
            "q": "A person's blood glucose level rises after eating. Describe how the body returns it to normal.",
            "steps": [
                ("F", "Blood glucose rises → pancreas detects this"),
                ("I", "Beta cells in pancreas secrete insulin"),
                ("F", "Insulin causes liver/muscle cells to absorb glucose and convert to glycogen"),
                ("A", "Blood glucose <strong>returns to normal</strong> — this is <strong>negative feedback</strong>"),
            ]
        },
        ("biology", "inheritance"): {
            "q": "Two parents are both carriers for cystic fibrosis (Ff). Calculate the probability of their child having cystic fibrosis.",
            "steps": [
                ("F", "Draw a Punnett square. Cystic fibrosis allele = f (recessive). Carrier = Ff"),
                ("I", "Ff × Ff → FF, Ff, Ff, ff"),
                ("F", "Only ff shows cystic fibrosis"),
                ("A", "Probability = <strong>1 in 4 (25%)</strong>"),
            ]
        },
        ("biology", "ecology"): {
            "q": "In a mark-recapture experiment, 60 fish were caught and marked. Later, 50 fish were caught and 10 were marked. Estimate the total population.",
            "steps": [
                ("F", "Population = (n1 × n2) ÷ m"),
                ("I", "Population = (60 × 50) ÷ 10"),
                ("F", "Population = 3000 ÷ 10"),
                ("A", "Estimated population = <strong>300 fish</strong>"),
            ]
        },
    }

    key = (subject, topic["id"])
    ex = examples.get(key)
    if not ex:
        return f'<div class="card"><p style="color:var(--muted);">Ask Mr Badmus AI below for a worked FIFA example on {topic["title"]}!</p></div>'

    steps_html = ""
    for letter, text in ex["steps"]:
        steps_html += f"""
<div class="fifa-step">
  <div class="fifa-letter">{letter}</div>
  <p>{text}</p>
</div>"""

    return f"""<div class="fifa-box">
  <div class="fifa-title">⚽ FIFA Example</div>
  <p class="fifa-question">{ex['q']}</p>
  {steps_html}
</div>"""


def make_quiz(subject, topic, color):
    """Generate 3-question quizzes per topic."""
    quizzes = {
        ("physics", "electricity"): [
            {
                "q": "A charge of 30 C flows past a point in 6 seconds. What is the current?",
                "opts": [("5 A", True), ("180 A", False), ("0.2 A", False), ("36 A", False)],
                "fb_correct": "Correct! I = Q ÷ t = 30 ÷ 6 = 5 A ✅",
                "fb_wrong": "Not quite. Use I = Q ÷ t → I = 30 ÷ 6 = 5 A"
            },
            {
                "q": "Which component has a resistance that DECREASES as temperature increases?",
                "opts": [("Thermistor", True), ("Filament lamp", False), ("Diode", False), ("Fixed resistor", False)],
                "fb_correct": "Correct! A thermistor (NTC) has lower resistance at higher temperatures ✅",
                "fb_wrong": "Not quite. A thermistor decreases in resistance as temperature rises — used in thermostats."
            },
            {
                "q": "In a parallel circuit, what is the same across every branch?",
                "opts": [("Potential difference", True), ("Current", False), ("Resistance", False), ("Charge", False)],
                "fb_correct": "Correct! P.D. is the same across all parallel branches ✅",
                "fb_wrong": "Not quite. In a parallel circuit, the potential difference (p.d.) is the same across every branch."
            },
        ],
        ("physics", "energy"): [
            {
                "q": "A 5 kg object moves at 4 m/s. Calculate its kinetic energy.",
                "opts": [("40 J", True), ("20 J", False), ("80 J", False), ("100 J", False)],
                "fb_correct": "Correct! KE = ½mv² = ½ × 5 × 16 = 40 J ✅",
                "fb_wrong": "Not quite. KE = ½mv² = ½ × 5 × 4² = ½ × 5 × 16 = 40 J"
            },
            {
                "q": "What is the unit of energy?",
                "opts": [("Joule (J)", True), ("Watt (W)", False), ("Newton (N)", False), ("Pascal (Pa)", False)],
                "fb_correct": "Correct! Energy is measured in Joules (J) ✅",
                "fb_wrong": "Not quite. Energy is measured in Joules (J). Watts = power, Newtons = force."
            },
            {
                "q": "Which statement about energy is always true?",
                "opts": [("Energy is conserved — it cannot be created or destroyed", True), ("Energy is always lost as heat", False), ("Useful energy output can exceed total input", False), ("Efficiency can be greater than 100%", False)],
                "fb_correct": "Correct! The law of conservation of energy — energy is never created or destroyed, only transferred ✅",
                "fb_wrong": "Not quite. Energy is always conserved — it cannot be created or destroyed, only transferred between stores."
            },
        ],
        ("chemistry", "quantitative"): [
            {
                "q": "Calculate the Mr of H₂O. (Ar: H=1, O=16)",
                "opts": [("18", True), ("17", False), ("16", False), ("20", False)],
                "fb_correct": "Correct! Mr = 2(1) + 16 = 18 ✅",
                "fb_wrong": "Not quite. Mr of H₂O = 2×1 + 16 = 18"
            },
            {
                "q": "How many moles are in 56 g of iron? (Ar of Fe = 56)",
                "opts": [("1 mol", True), ("56 mol", False), ("0.5 mol", False), ("2 mol", False)],
                "fb_correct": "Correct! mol = 56 ÷ 56 = 1 mol ✅",
                "fb_wrong": "Not quite. mol = mass ÷ Mr = 56 ÷ 56 = 1 mol"
            },
            {
                "q": "A reaction produces 8 g of product but the theoretical yield is 10 g. What is the percentage yield?",
                "opts": [("80%", True), ("125%", False), ("20%", False), ("18%", False)],
                "fb_correct": "Correct! % yield = (8 ÷ 10) × 100 = 80% ✅",
                "fb_wrong": "Not quite. % yield = (actual ÷ theoretical) × 100 = (8 ÷ 10) × 100 = 80%"
            },
        ],
        ("biology", "cell-biology"): [
            {
                "q": "Which organelle is found in plant cells but NOT animal cells?",
                "opts": [("Chloroplast", True), ("Nucleus", False), ("Mitochondria", False), ("Ribosomes", False)],
                "fb_correct": "Correct! Chloroplasts are only found in plant cells — they carry out photosynthesis ✅",
                "fb_wrong": "Not quite. Chloroplasts are found only in plant cells. Nucleus, mitochondria and ribosomes are in both."
            },
            {
                "q": "A cell image measures 5 mm. The actual cell is 0.05 mm. What is the magnification?",
                "opts": [("×100", True), ("×10", False), ("×1000", False), ("×0.01", False)],
                "fb_correct": "Correct! M = 5 ÷ 0.05 = ×100 ✅",
                "fb_wrong": "Not quite. Magnification = image size ÷ actual size = 5 ÷ 0.05 = ×100"
            },
            {
                "q": "Which process moves substances from HIGH to LOW concentration without using energy?",
                "opts": [("Diffusion", True), ("Active transport", False), ("Osmosis (water only)", False), ("Endocytosis", False)],
                "fb_correct": "Correct! Diffusion moves substances down a concentration gradient — no energy needed ✅",
                "fb_wrong": "Not quite. Diffusion is the passive movement from high to low concentration. Active transport uses energy and goes against the gradient."
            },
        ],
        ("biology", "bioenergetics"): [
            {
                "q": "What are the products of aerobic respiration?",
                "opts": [("Carbon dioxide and water", True), ("Glucose and oxygen", False), ("Lactic acid", False), ("Ethanol and CO₂", False)],
                "fb_correct": "Correct! Aerobic respiration: glucose + oxygen → carbon dioxide + water (+ energy) ✅",
                "fb_wrong": "Not quite. Aerobic respiration produces carbon dioxide and water. Lactic acid is from anaerobic respiration in animals."
            },
            {
                "q": "Which factor is NOT a limiting factor of photosynthesis?",
                "opts": [("Soil pH", True), ("Light intensity", False), ("CO₂ concentration", False), ("Temperature", False)],
                "fb_correct": "Correct! Soil pH is not a direct limiting factor. The three main limiting factors are light, CO₂ and temperature ✅",
                "fb_wrong": "Not quite. Soil pH doesn't directly limit photosynthesis. Light intensity, CO₂ concentration and temperature are the three main limiting factors."
            },
            {
                "q": "In anaerobic respiration in yeast, what are the products?",
                "opts": [("Ethanol and carbon dioxide", True), ("Lactic acid", False), ("Carbon dioxide and water", False), ("Glucose and oxygen", False)],
                "fb_correct": "Correct! Yeast fermentation: glucose → ethanol + carbon dioxide ✅",
                "fb_wrong": "Not quite. Yeast produces ethanol and CO₂ in anaerobic respiration. Lactic acid is produced in human muscle cells."
            },
        ],
    }

    # Default quiz for topics without specific questions
    default_quiz = [
        {
            "q": f"Which specification section covers {topic['title']}?",
            "opts": [(f"AQA Spec {topic['spec']}", True), ("AQA Spec 1.1", False), ("AQA Spec 9.9", False), ("Not in the spec", False)],
            "fb_correct": f"Correct! {topic['title']} is covered in AQA spec section {topic['spec']} ✅",
            "fb_wrong": f"Not quite. This topic is in AQA spec section {topic['spec']}."
        },
        {
            "q": f"Which exam paper is {topic['title']} assessed in?",
            "opts": [(f"Paper {topic['paper']}", True), (f"Paper {3 - topic['paper']}", False), ("Both papers equally", False), ("Not assessed", False)],
            "fb_correct": f"Correct! {topic['title']} is assessed in Paper {topic['paper']} ✅",
            "fb_wrong": f"Not quite. {topic['title']} is examined in Paper {topic['paper']}."
        },
    ]

    questions = quizzes.get((subject, topic["id"]), default_quiz)

    html = ""
    for i, q in enumerate(questions):
        opts_html = ""
        correct_val = ""
        for j, (opt_text, is_correct) in enumerate(q["opts"]):
            val = f"opt{i}_{j}"
            if is_correct:
                correct_val = val
            opts_html += f'<button class="quiz-opt" data-val="{val}">{opt_text}</button>\n'

        html += f"""
<div class="quiz-card" data-answer="{correct_val}">
  <div class="q-text">{i+1}. {q['q']}</div>
  <div class="quiz-options">
    {opts_html}
  </div>
  <div class="quiz-feedback correct-fb">{q.get('fb_correct','✅ Correct!')}</div>
  <div class="quiz-feedback wrong-fb">{q.get('fb_wrong','Not quite — try again!')}</div>
</div>"""

    return html


# ─────────────────────────────────────────────
#  BUILD FUNCTION
# ─────────────────────────────────────────────

PHYSICS_COLOR = "#1D6FB8"

ELECTRICITY_SUBTOPICS = [
    # ─────────────────────────────────────────────
    # 1. CIRCUIT SYMBOLS
    # ─────────────────────────────────────────────
    {
        "id": "circuit-symbols",
        "title": "Circuit Symbols and Diagrams",
        "spec": "4.2.1.1",
        "summary": "Draw and interpret circuit diagrams using standard AQA symbols.",
        "theory": [
            {
                "heading": "What is a circuit diagram?",
                "content": "A circuit diagram is a map of an electrical circuit.\nInstead of drawing real components, we use standard symbols.\nEvery physicist in the world uses the same symbols — so anyone can read your diagram."
            },
            {
                "heading": "How to draw a good circuit diagram",
                "content": "Always use a ruler — no freehand wiggly lines!\nComponents sit on straight horizontal or vertical lines.\nCorners are right angles — like a rectangle.\nLabel components with their values where given (e.g. '6 Ω')."
            },
            {
                "heading": "Series vs Parallel — spot the difference",
                "content": "Series: one single loop — like a one-way street with no junctions.\nParallel: the wire splits into branches — like a road that forks then rejoins."
            },
            {
                "heading": "Ammeter and Voltmeter — where do they go?",
                "content": "Ammeter — measures current. Goes IN SERIES (in the main loop).\nVoltmeter — measures potential difference. Goes IN PARALLEL (branching across the component).\nSwap these and you'll get zero readings or blow the meter!"
            }
        ],
        "common_mistake": "Students often draw voltmeters in series and ammeters in parallel — the wrong way round! Remember: Ammeter = in the main line (series). Voltmeter = branching across (parallel).",
        "key_note": None,
        "higher": None,
        "triple_only": None,
        "equations": [],
        "variables": [],
        "rp": None,
        "matching": {
            "title": "Match the Component to its Symbol",
            "instruction": "Drag each description to the correct component name.",
            "svg_pairs": [
                ("Cell", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="30" y2="15" stroke="white" stroke-width="2"/><line x1="30" y1="5" x2="30" y2="25" stroke="white" stroke-width="3"/><line x1="38" y1="10" x2="38" y2="20" stroke="white" stroke-width="1.5"/><line x1="38" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/></svg>'),
                ("Battery", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="15" y2="15" stroke="white" stroke-width="2"/><line x1="15" y1="5" x2="15" y2="25" stroke="white" stroke-width="3"/><line x1="22" y1="10" x2="22" y2="20" stroke="white" stroke-width="1.5"/><line x1="29" y1="5" x2="29" y2="25" stroke="white" stroke-width="3"/><line x1="36" y1="10" x2="36" y2="20" stroke="white" stroke-width="1.5"/><line x1="36" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/></svg>'),
                ("Open Switch", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="25" y2="15" stroke="white" stroke-width="2"/><circle cx="25" cy="15" r="3" fill="white"/><line x1="28" y1="15" x2="52" y2="5" stroke="white" stroke-width="2"/><circle cx="55" cy="15" r="3" fill="white"/><line x1="55" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/></svg>'),
                ("Closed Switch", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="25" y2="15" stroke="white" stroke-width="2"/><circle cx="25" cy="15" r="3" fill="white"/><line x1="28" y1="15" x2="52" y2="15" stroke="white" stroke-width="2"/><circle cx="55" cy="15" r="3" fill="white"/><line x1="55" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/></svg>'),
                ("Resistor", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="18" y2="15" stroke="white" stroke-width="2"/><rect x="18" y="8" width="44" height="14" fill="none" stroke="white" stroke-width="2"/><line x1="62" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/></svg>'),
                ("Variable Resistor", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="18" y2="15" stroke="white" stroke-width="2"/><rect x="18" y="8" width="44" height="14" fill="none" stroke="white" stroke-width="2"/><line x1="62" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/><line x1="55" y1="25" x2="28" y2="5" stroke="white" stroke-width="2"/><polygon points="25,4 32,2 30,9" fill="white"/></svg>'),
                ("Lamp / Bulb", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="22" y2="15" stroke="white" stroke-width="2"/><circle cx="40" cy="15" r="12" fill="none" stroke="white" stroke-width="2"/><line x1="30" y1="7" x2="50" y2="23" stroke="white" stroke-width="2"/><line x1="50" y1="7" x2="30" y2="23" stroke="white" stroke-width="2"/><line x1="52" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/></svg>'),
                ("Voltmeter", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="22" y2="15" stroke="white" stroke-width="2"/><circle cx="40" cy="15" r="12" fill="none" stroke="white" stroke-width="2"/><text x="40" y="20" text-anchor="middle" fill="white" font-size="12" font-family="Arial">V</text><line x1="52" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/></svg>'),
                ("Ammeter", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="22" y2="15" stroke="white" stroke-width="2"/><circle cx="40" cy="15" r="12" fill="none" stroke="white" stroke-width="2"/><text x="40" y="20" text-anchor="middle" fill="white" font-size="12" font-family="Arial">A</text><line x1="52" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/></svg>'),
                ("Diode", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="28" y2="15" stroke="white" stroke-width="2"/><polygon points="28,6 28,24 52,15" fill="white"/><line x1="52" y1="6" x2="52" y2="24" stroke="white" stroke-width="2.5"/><line x1="52" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/></svg>'),
                ("LED", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="28" y2="15" stroke="white" stroke-width="2"/><polygon points="28,6 28,24 52,15" fill="white"/><line x1="52" y1="6" x2="52" y2="24" stroke="white" stroke-width="2.5"/><line x1="52" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/><line x1="44" y1="4" x2="54" y2="-2" stroke="white" stroke-width="1.5"/><polygon points="54,-2 50,0 52,-4" fill="white"/><line x1="48" y1="7" x2="58" y2="1" stroke="white" stroke-width="1.5"/><polygon points="58,1 54,3 56,-1" fill="white"/></svg>'),
                ("Thermistor", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="18" y2="15" stroke="white" stroke-width="2"/><rect x="18" y="8" width="44" height="14" fill="none" stroke="white" stroke-width="2"/><line x1="62" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/><line x1="22" y1="22" x2="38" y2="8" stroke="white" stroke-width="2"/><text x="44" y="20" fill="white" font-size="9" font-family="Arial" font-style="italic">T</text></svg>'),
                ("LDR", '<svg width="80" height="30" viewBox="0 0 80 30"><line x1="0" y1="15" x2="18" y2="15" stroke="white" stroke-width="2"/><rect x="18" y="8" width="44" height="14" fill="none" stroke="white" stroke-width="2"/><line x1="62" y1="15" x2="80" y2="15" stroke="white" stroke-width="2"/><line x1="20" y1="4" x2="28" y2="10" stroke="white" stroke-width="1.5" stroke-dasharray="2"/><line x1="28" y1="2" x2="36" y2="8" stroke="white" stroke-width="1.5" stroke-dasharray="2"/><polygon points="20,4 24,5 22,1" fill="white"/><polygon points="28,2 32,3 30,-1" fill="white"/></svg>'),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "An ammeter must always be connected — how?",
                "opts": [
                    ("In series — in the main current path", True),
                    ("In parallel — branching across the component", False),
                    ("Across the battery terminals only", False),
                    ("Outside the circuit, nearby", False)
                ],
                "wrong_explanations": {
                    1: "That's where a VOLTMETER goes — not an ammeter. If you put an ammeter in parallel, it has almost zero resistance and would short-circuit the component.",
                    2: "The battery terminals are where the voltmeter goes to measure the supply p.d. The ammeter must be in the main loop.",
                    3: "Electrical components only work when they're physically connected in the circuit."
                }
            },
            {
                "q": "A voltmeter is connected across a lamp. What does this tell you about the connection?",
                "opts": [
                    ("It is in parallel with the lamp", True),
                    ("It is in series with the lamp", False),
                    ("It is outside the circuit", False),
                    ("It replaces the lamp in the circuit", False)
                ],
                "wrong_explanations": {
                    1: "Series connection means the voltmeter is in the main loop — but a voltmeter in series would block current and give a wrong reading.",
                    2: "Outside the circuit means no connection at all — the voltmeter would read zero.",
                    3: "The voltmeter measures the lamp — it doesn't replace it. Both must be in the circuit."
                }
            },
            {
                "q": "Which component only allows current to flow in one direction?",
                "opts": [
                    ("Diode", True),
                    ("Resistor", False),
                    ("LDR", False),
                    ("Thermistor", False)
                ],
                "wrong_explanations": {
                    1: "A resistor slows current in both directions — it doesn't block it in one direction.",
                    2: "An LDR changes resistance with light, but current can flow both ways through it.",
                    3: "A thermistor changes resistance with temperature, but current can flow both ways."
                }
            },
            {
                "q": "What does an LDR do when light intensity increases?",
                "opts": [
                    ("Its resistance decreases", True),
                    ("Its resistance increases", False),
                    ("It stops working", False),
                    ("Its resistance stays the same", False)
                ],
                "wrong_explanations": {
                    1: "This is a very common mix-up! More light → LOWER resistance in an LDR. Think: light 'frees up' the electrons to flow more easily.",
                    2: "An LDR doesn't stop working — it just changes resistance depending on light level.",
                    3: "LDR stands for Light-DEPENDENT Resistor — its whole purpose is to change resistance with light."
                }
            },
            {
                "q": "In a circuit diagram, what shape represents a resistor?",
                "opts": [
                    ("A rectangle", True),
                    ("A circle with an X", False),
                    ("A triangle pointing to a line", False),
                    ("Two parallel lines of different lengths", False)
                ],
                "wrong_explanations": {
                    1: "Circle with X = a lamp/bulb. Don't mix these up!",
                    2: "Triangle pointing to a line = a diode. That's the one-way component.",
                    3: "Two parallel lines of different lengths = a cell (single) or battery (multiple)."
                }
            }
        ]
    },

    # ─────────────────────────────────────────────
    # 2. CHARGE, CURRENT AND TIME
    # ─────────────────────────────────────────────
    {
        "id": "charge-current-time",
        "title": "Charge, Current and Time",
        "spec": "4.2.1.2",
        "summary": "Use Q = It to calculate charge, current and time in electrical circuits.",
        "theory": [
            {
                "heading": "Think of it like a water pipe — but cooler",
                "content": "Imagine Mr Badmus has a burger van.\nThe burgers being delivered are the CHARGE — each burger is a tiny electron.\nThe number of burgers delivered every second is the CURRENT.\nMore burgers per second = bigger current.\nThe total number of burgers delivered over the whole shift = total charge."
            },
            {
                "heading": "What is electric current?",
                "content": "Current is the rate of flow of charge — how much charge passes a point every second.\nIn metal conductors, electrons are the charge carriers.\nCurrent is measured in Amperes (A) using an ammeter in series."
            },
            {
                "heading": "What is electric charge?",
                "content": "Charge is the 'stuff' that flows — it's carried by electrons.\nOne electron carries a tiny charge of 1.6 × 10⁻¹⁹ C.\nCharge is measured in Coulombs (C)."
            }
        ],
        "variables": [
            ("Q", "Charge", "Coulombs", "C"),
            ("I", "Current", "Amperes", "A"),
            ("t", "Time", "Seconds", "s"),
        ],
        "common_mistake": "Time MUST be in seconds before you use Q = It. If the question gives minutes, multiply by 60 first. Forgetting to convert is the single most common error in this topic — examiners know it and test it deliberately!",
        "key_note": None,
        "higher": None,
        "triple_only": None,
        "equations": ["Q = It"],
        "rp": None,
        "matching": None,
        "fifas": [
            {
                "label": "Example 1 — Find charge (Q)",
                "question": "A current of 2 A flows through a wire for 3 minutes. Calculate the total charge that flows.",
                "steps": [
                    ("F", "Q = I × t"),
                    ("I", "I = 2 A, t = 3 minutes → MUST convert: 3 × 60 = 180 s"),
                    ("F", "Q = 2 × 180"),
                    ("A", "Q = 360 C")
                ]
            },
            {
                "label": "Example 2 — Find current (I)",
                "question": "A total charge of 450 C flows through a circuit in 1.5 minutes. Calculate the current.",
                "steps": [
                    ("F", "I = Q ÷ t"),
                    ("I", "Q = 450 C, t = 1.5 min → convert: 1.5 × 60 = 90 s"),
                    ("F", "I = 450 ÷ 90"),
                    ("A", "I = 5 A")
                ]
            },
            {
                "label": "Example 3 — Find time (t)",
                "question": "A current of 0.5 A delivers a charge of 180 C. How long does this take? Give your answer in minutes.",
                "steps": [
                    ("F", "t = Q ÷ I"),
                    ("I", "t = 180 ÷ 0.5"),
                    ("F", "t = 360 s → convert to minutes: 360 ÷ 60"),
                    ("A", "t = 6 minutes")
                ]
            }
        ],
        "quiz": [
            {
                "q": "A charge of 120 C flows past a point in 60 seconds. What is the current?",
                "opts": [
                    ("2 A", True),
                    ("7200 A", False),
                    ("0.5 A", False),
                    ("120 A", False)
                ],
                "wrong_explanations": {
                    1: "You multiplied Q × t instead of dividing! That gives 7200, which would mean a current bigger than a lightning bolt. Always use I = Q ÷ t.",
                    2: "You divided the wrong way — that's t ÷ Q, not Q ÷ t. Remember: I = Q ÷ t = 120 ÷ 60 = 2 A.",
                    3: "You might have used Q ÷ I instead of Q ÷ t. Be careful which quantity is which."
                }
            },
            {
                "q": "A 4 A current flows for 5 minutes. What is the total charge that flows?",
                "opts": [
                    ("1200 C", True),
                    ("20 C", False),
                    ("0.8 C", False),
                    ("300 C", False)
                ],
                "wrong_explanations": {
                    1: "You forgot to convert minutes to seconds! Q = 4 × 5 = 20 C only works if time is in seconds. 5 minutes = 300 s, so Q = 4 × 300 = 1200 C.",
                    2: "You divided instead of multiplied, and forgot the time conversion. Q = I × t = 4 × 300 = 1200 C.",
                    3: "You converted time correctly (300 s) but then divided instead of multiplying. Q = I × t."
                }
            },
            {
                "q": "What is the unit of electric charge?",
                "opts": [
                    ("Coulomb (C)", True),
                    ("Ampere (A)", False),
                    ("Volt (V)", False),
                    ("Joule (J)", False)
                ],
                "wrong_explanations": {
                    1: "Ampere is the unit of CURRENT (I), not charge. Don't confuse the quantity with its unit.",
                    2: "Volt is the unit of potential difference (V) — the 'push' in a circuit. Charge is measured in Coulombs.",
                    3: "Joule is the unit of energy. Charge and energy are different quantities — don't mix them up."
                }
            },
            {
                "q": "A current of 3 A flows for 2 minutes. How much charge flows?",
                "opts": [
                    ("360 C", True),
                    ("6 C", False),
                    ("90 C", False),
                    ("1.5 C", False)
                ],
                "wrong_explanations": {
                    1: "Classic time conversion error! Q = 3 × 2 = 6 only if time is in seconds. 2 minutes = 120 s, so Q = 3 × 120 = 360 C.",
                    2: "You divided Q by I somewhere. Remember the formula is Q = I × t, not Q = I ÷ t.",
                    3: "You may have divided I by t. Q = I × t = 3 × 120 = 360 C."
                }
            },
            {
                "q": "How long does it take a 6 A current to deliver 900 C of charge?",
                "opts": [
                    ("150 seconds", True),
                    ("5400 seconds", False),
                    ("0.0067 seconds", False),
                    ("906 seconds", False)
                ],
                "wrong_explanations": {
                    1: "You multiplied instead of dividing — that gives Q, not t. Use t = Q ÷ I = 900 ÷ 6 = 150 s.",
                    2: "You divided I by Q instead of Q by I. t = Q ÷ I = 900 ÷ 6 = 150 s.",
                    3: "You added Q and I, which doesn't make physical sense. t = Q ÷ I = 900 ÷ 6 = 150 s."
                }
            }
        ]
    },

    # ─────────────────────────────────────────────
    # 3. POTENTIAL DIFFERENCE, CURRENT, RESISTANCE
    # ─────────────────────────────────────────────
    {
        "id": "potential-difference-resistance",
        "title": "Potential Difference, Current and Resistance",
        "spec": "4.2.1.3",
        "summary": "Apply V = IR to calculate potential difference, current and resistance.",
        "theory": [
            {
                "heading": "The Burger Van — Mr Badmus' Circuit",
                "content": "Mr Badmus runs a burger van.\nThe number of burgers he MAKES per minute is the Potential Difference (p.d.) — the driving force.\nThe waiters and waitresses DELIVERING burgers are the charge carriers (electrons).\nHow many burgers get delivered per second is the Current.\nA congested street, a broken-down van blocking the road, a queue of people — that's Resistance.\nMore congestion = fewer burgers delivered = lower current."
            },
            {
                "heading": "What is Potential Difference?",
                "content": "Potential difference (p.d.) is the energy given to each unit of charge by the power supply.\nDon't call it 'voltage' in your exam — call it potential difference!\nMeasured in Volts (V) using a voltmeter in PARALLEL."
            },
            {
                "heading": "What is Resistance?",
                "content": "Resistance is anything that opposes the flow of current.\nThe higher the resistance, the less current flows for the same p.d.\nThink: a narrow road vs a wide road — fewer cars get through the narrow one.\nMeasured in Ohms (Ω)."
            },
            {
                "heading": "Ohm's Law",
                "content": "A component is ohmic if its resistance stays constant when temperature stays constant.\nOn an I-V graph, an ohmic conductor gives a straight line through the origin.\nA curved I-V graph means resistance is changing — non-ohmic."
            }
        ],
        "variables": [
            ("V", "Potential Difference", "Volts", "V"),
            ("I", "Current", "Amperes", "A"),
            ("R", "Resistance", "Ohms", "Ω"),
        ],
        "common_mistake": "Students write 'voltage' instead of 'potential difference' and lose marks. Also — never put a voltmeter in series or an ammeter in parallel. The voltmeter goes ACROSS (parallel), the ammeter goes IN THE LINE (series).",
        "key_note": None,
        "higher": None,
        "triple_only": None,
        "equations": ["V = IR"],
        "rp": "RP4 — I-V characteristics: plot I-V graphs for a resistor, filament lamp and diode",
        "matching": None,
        "fifas": [
            {
                "label": "Example 1 — Find current (I)",
                "question": "A resistor has a potential difference of 9 V across it and a resistance of 3 Ω. Calculate the current.",
                "steps": [
                    ("F", "I = V ÷ R"),
                    ("I", "I = 9 ÷ 3"),
                    ("F", "No unit conversion needed"),
                    ("A", "I = 3 A")
                ]
            },
            {
                "label": "Example 2 — Find resistance (R)",
                "question": "A current of 0.5 A flows through a component when a p.d. of 6 V is applied. Calculate the resistance.",
                "steps": [
                    ("F", "R = V ÷ I"),
                    ("I", "R = 6 ÷ 0.5"),
                    ("F", "No unit conversion needed"),
                    ("A", "R = 12 Ω")
                ]
            },
            {
                "label": "Example 3 — Find potential difference (V)",
                "question": "A 15 Ω resistor carries a current of 0.4 A. Calculate the potential difference across it.",
                "steps": [
                    ("F", "V = I × R"),
                    ("I", "V = 0.4 × 15"),
                    ("F", "No unit conversion needed"),
                    ("A", "V = 6 V")
                ]
            }
        ],
        "quiz": [
            {
                "q": "A 12 V supply drives current through a 4 Ω resistor. What is the current?",
                "opts": [
                    ("3 A", True),
                    ("48 A", False),
                    ("0.33 A", False),
                    ("8 A", False)
                ],
                "wrong_explanations": {
                    1: "You multiplied V × R instead of dividing. That gives power, not current. Use I = V ÷ R = 12 ÷ 4 = 3 A.",
                    2: "You divided R by V instead of V by R. I = V ÷ R = 12 ÷ 4 = 3 A.",
                    3: "You subtracted R from V. Equations don't work with subtraction here — use I = V ÷ R."
                }
            },
            {
                "q": "What does Ohm's Law tell us about a resistor at constant temperature?",
                "opts": [
                    ("Current is proportional to potential difference — resistance stays constant", True),
                    ("Resistance increases as current increases", False),
                    ("Current decreases as potential difference increases", False),
                    ("Resistance is zero at constant temperature", False)
                ],
                "wrong_explanations": {
                    1: "This describes a filament lamp, not an ohmic conductor. In a lamp, resistance increases as it heats up.",
                    2: "This is the opposite! V = IR means increasing V increases I — they go up together when R is constant.",
                    3: "Zero resistance would mean a superconductor — not what Ohm's Law describes."
                }
            },
            {
                "q": "A current of 2 A flows through a 10 Ω resistor. What is the potential difference?",
                "opts": [
                    ("20 V", True),
                    ("5 V", False),
                    ("0.2 V", False),
                    ("12 V", False)
                ],
                "wrong_explanations": {
                    1: "You divided instead of multiplying. V = I × R = 2 × 10 = 20 V.",
                    2: "You divided both numbers in the wrong way. V = I × R = 2 × 10 = 20 V.",
                    3: "There's no subtraction in Ohm's Law. V = I × R = 2 × 10 = 20 V."
                }
            },
            {
                "q": "On an I-V graph, what does a straight line through the origin tell you?",
                "opts": [
                    ("The component is ohmic — resistance is constant", True),
                    ("The component has zero resistance", False),
                    ("The component only works in one direction", False),
                    ("The component is heating up as current increases", False)
                ],
                "wrong_explanations": {
                    1: "Zero resistance would mean no p.d. at all — the line would be vertical, not diagonal.",
                    2: "One-direction only = a diode. Its I-V graph is NOT a straight line.",
                    3: "Heating up as current increases = filament lamp. Its I-V graph CURVES — not a straight line."
                }
            },
            {
                "q": "The p.d. across a component is 8 V and the current through it is 0.4 A. What is the resistance?",
                "opts": [
                    ("20 Ω", True),
                    ("3.2 Ω", False),
                    ("0.05 Ω", False),
                    ("8.4 Ω", False)
                ],
                "wrong_explanations": {
                    1: "You multiplied V × I instead of dividing. That gives power (in watts), not resistance.",
                    2: "You divided I by V instead of V by I. R = V ÷ I = 8 ÷ 0.4 = 20 Ω.",
                    3: "You added V and I — that's not a valid electrical equation. R = V ÷ I = 8 ÷ 0.4 = 20 Ω."
                }
            }
        ]
    },

    # ─────────────────────────────────────────────
    # 4. RESISTANCE — COMPONENTS
    # ─────────────────────────────────────────────
    {
        "id": "resistance-components",
        "title": "Resistance — How Components Behave",
        "spec": "4.2.1.4",
        "summary": "Describe how resistance varies in different components and interpret I-V graphs.",
        "theory": [
            {
                "heading": "The Ohmic Conductor — Mr Consistent",
                "content": "An ohmic conductor is like a well-trained waiter — no matter how busy the burger van gets, he always delivers at the same rate per burger.\nResistance stays constant at constant temperature.\nI-V graph: a perfectly straight line through the origin.\nExample: a fixed resistor."
            },
            {
                "heading": "The Filament Lamp — Slows Down When Tired",
                "content": "As current increases, the filament wire gets hotter.\nHotter wire = electrons collide more with the vibrating ions = more resistance.\nSo the lamp gets harder to push current through as it heats up.\nI-V graph: starts steep (easy to push current through when cold), then curves and flattens (harder when hot).\nShape = a gentle S-curve."
            },
            {
                "heading": "The Diode — One-Way Street",
                "content": "A diode is like a turnstile — current can only go one way.\nForward direction: almost no resistance once p.d. exceeds about 0.7 V.\nReverse direction: almost infinite resistance — no current flows at all.\nI-V graph: flat line in reverse, then shoots up steeply in the forward direction.\nUsed to convert AC to DC."
            },
            {
                "heading": "The Thermistor — Hot and Helpful",
                "content": "NTC = Negative Temperature Coefficient.\nAs temperature INCREASES → resistance DECREASES.\nThink: when the burger van heats up, the congestion mysteriously clears!\nUsed in: thermostats, temperature sensors, phone overheating protection."
            },
            {
                "heading": "The LDR — Lights Up When Needed",
                "content": "LDR = Light-Dependent Resistor.\nAs light intensity INCREASES → resistance DECREASES.\nThink: when the sun comes out, more electrons get 'excited' and the current flows more easily.\nUsed in: automatic street lights (come on in the dark), phone screen brightness sensors."
            }
        ],
        "variables": [],
        "common_mistake": "Students mix up thermistors and LDRs with normal resistors. Remember: BOTH thermistors and LDRs DECREASE in resistance when their trigger (heat/light) INCREASES. This feels backwards — but it's NTC (Negative Temperature Coefficient) for a reason!",
        "key_note": None,
        "higher": "In a potential divider with an LDR: as light increases, LDR resistance drops, so the voltage across the LDR drops. If LDR is in position R2: Vout = Vin × R2 ÷ (R1 + R2).",
        "triple_only": None,
        "equations": ["V = IR (applies to each component individually)"],
        "rp": "RP4 — Investigate I-V characteristics: plot current vs p.d. graphs for a resistor, filament lamp and diode.",
        "matching": {
            "title": "Match the Component to its I-V Graph Shape",
            "instruction": "Match each component to how its I-V graph looks.",
            "pairs": [
                ("Ohmic resistor", "Straight line through the origin"),
                ("Filament lamp", "S-shaped curve — starts steep, then flattens"),
                ("Diode (forward)", "Flat near zero, then shoots up steeply"),
                ("Diode (reverse)", "Completely flat — no current flows"),
                ("Thermistor (heated)", "Steeper line — resistance has dropped"),
                ("LDR (in bright light)", "Steeper line — resistance has dropped"),
            ]
        },
        "fifas": [
            {
                "label": "Example 1 — Thermistor current at two temperatures",
                "question": "A thermistor has resistance 2000 Ω at 20°C and 200 Ω at 80°C. The supply p.d. is 6 V. Calculate the current at each temperature.",
                "steps": [
                    ("F", "I = V ÷ R (apply separately at each temperature)"),
                    ("I", "At 20°C: I = 6 ÷ 2000 = 0.003 A. At 80°C: I = 6 ÷ 200 = 0.03 A"),
                    ("F", "No unit conversion needed"),
                    ("A", "At 20°C: I = 0.003 A (3 mA). At 80°C: I = 0.03 A (30 mA). Higher temp = lower R = more current ✅")
                ]
            },
            {
                "label": "Example 2 — Find resistance from I-V graph data",
                "question": "From an I-V graph, a resistor shows a current of 0.6 A when the p.d. is 3 V. Calculate its resistance and state whether it is ohmic.",
                "steps": [
                    ("F", "R = V ÷ I"),
                    ("I", "R = 3 ÷ 0.6"),
                    ("F", "No unit conversion needed"),
                    ("A", "R = 5 Ω. If the I-V graph is a straight line through the origin, it is ohmic.")
                ]
            }
        ],
        "quiz": [
            {
                "q": "As temperature increases, what happens to an NTC thermistor's resistance?",
                "opts": [
                    ("It decreases", True),
                    ("It increases", False),
                    ("It stays the same", False),
                    ("It becomes infinite", False)
                ],
                "wrong_explanations": {
                    1: "This is the most common mistake in this topic! NTC = Negative Temperature Coefficient. NEGATIVE means resistance goes DOWN as temperature goes UP.",
                    2: "Only a fixed resistor stays constant. A thermistor is specifically designed to change with temperature.",
                    3: "Infinite resistance would mean no current at all — that describes a diode in reverse, not a thermistor."
                }
            },
            {
                "q": "What shape is the I-V graph for a filament lamp?",
                "opts": [
                    ("A curve — starts steep then flattens (S-shape)", True),
                    ("A straight line through the origin", False),
                    ("Flat in one direction, steep in the other", False),
                    ("A horizontal straight line", False)
                ],
                "wrong_explanations": {
                    1: "Straight line = ohmic conductor. A filament lamp HEATS UP as current increases, so its resistance changes — giving a curve.",
                    2: "Flat one direction, steep the other = a diode. The lamp allows current both ways.",
                    3: "A horizontal line would mean zero current regardless of p.d. — that's not how a lamp works."
                }
            },
            {
                "q": "An LDR is placed in a dark room. What happens to its resistance?",
                "opts": [
                    ("Resistance increases", True),
                    ("Resistance decreases", False),
                    ("Resistance stays the same", False),
                    ("Resistance becomes zero", False)
                ],
                "wrong_explanations": {
                    1: "Less light = LOWER resistance? No! Less light means fewer free electrons = HIGHER resistance. Dark = high R in an LDR.",
                    2: "LDR means Light-DEPENDENT — it changes with light. In the dark it doesn't stay the same.",
                    3: "Zero resistance would mean a perfect conductor — an LDR in the dark has very HIGH resistance, not zero."
                }
            },
            {
                "q": "Which component has almost infinite resistance in one direction?",
                "opts": [
                    ("Diode", True),
                    ("Thermistor", False),
                    ("LDR", False),
                    ("Fixed resistor", False)
                ],
                "wrong_explanations": {
                    1: "Thermistors change resistance with temperature, but current can flow both ways through them.",
                    2: "LDRs change resistance with light, but current can flow both ways through them.",
                    3: "A fixed resistor has the same resistance in both directions — it doesn't block current in reverse."
                }
            },
            {
                "q": "A component at 20°C shows a straight I-V graph. At 200°C, the graph curves. What is it?",
                "opts": [
                    ("A filament lamp or wire — resistance increases with temperature", True),
                    ("A diode — it only works at high temperatures", False),
                    ("An LDR — it changes with temperature as well as light", False),
                    ("An ohmic conductor — it always gives a straight line", False)
                ],
                "wrong_explanations": {
                    1: "A diode's behaviour is about direction, not temperature. And it works at all temperatures, not just high ones.",
                    2: "LDRs respond to LIGHT, not temperature. And their graph doesn't curve at high temperatures.",
                    3: "An ohmic conductor maintains a straight I-V graph as long as temperature stays constant. Change the temperature and it stops being ohmic."
                }
            }
        ]
    },

    # ─────────────────────────────────────────────
    # 5. SERIES AND PARALLEL CIRCUITS
    # ─────────────────────────────────────────────
    {
        "id": "series-parallel-circuits",
        "title": "Series and Parallel Circuits",
        "spec": "4.2.2",
        "summary": "Apply the rules for current, p.d. and resistance in series and parallel circuits.",
        "theory": [
            {
                "heading": "Series — The One-Way Motorway",
                "content": "Imagine a single motorway with no exits.\nEvery car (electron) passes through every junction.\nSo the flow (current) is the same at every point — no car gets lost.\nThe motorway has toll booths (resistors) — each one slows the traffic down a little.\nAll the tolls add up to the total journey cost (total p.d.)."
            },
            {
                "heading": "Series Circuit Rules",
                "content": "Current (I): the same at every point in the circuit.\nPotential difference (V): shared — V_total = V₁ + V₂ + V₃.\nResistance (R): adds up — R_total = R₁ + R₂ + R₃.\nAdding more resistors in series → total resistance increases → current decreases."
            },
            {
                "heading": "Parallel — The Multi-Lane Bypass",
                "content": "Now imagine the motorway splits into three lanes.\nTraffic (charge) can choose any lane.\nEach lane has its own toll booth — but each driver only pays ONE toll.\nSo every lane has the SAME journey cost (same p.d.).\nBut more lanes = more total traffic = more current overall."
            },
            {
                "heading": "Parallel Circuit Rules",
                "content": "Potential difference (V): the same across every parallel branch.\nCurrent (I): splits — I_total = I₁ + I₂ + I₃.\nResistance (R): total is LESS than any individual branch.\nAdding more branches in parallel → total resistance decreases → total current increases."
            },
            {
                "heading": "Why your home is wired in parallel",
                "content": "Every appliance in your home gets the full 230 V mains.\nTurning one appliance off doesn't affect the others.\nEach device has its own switch — independent control.\nIf it were series, one broken bulb would cut off everything!"
            }
        ],
        "variables": [],
        "common_mistake": "Students often say 'p.d. is the same in series' — it's NOT! P.d. SPLITS in series and stays the SAME in parallel. Current is the same in series, and SPLITS in parallel. These are always swapped in exams — be very careful!",
        "key_note": None,
        "higher": "Total resistance in parallel: 1/R_total = 1/R₁ + 1/R₂. For two resistors: R_total = (R₁ × R₂) ÷ (R₁ + R₂). The total is always LESS than the smallest individual resistor.",
        "triple_only": None,
        "equations": ["R_total = R₁ + R₂ (series)", "V_total = V₁ + V₂ (series)", "I_total = I₁ + I₂ (parallel)"],
        "rp": None,
        "matching": {
            "title": "Series or Parallel?",
            "instruction": "Sort each statement into Series or Parallel.",
            "pairs": [
                ("Series", "Current is the same at every point"),
                ("Series", "Potential difference is shared between components"),
                ("Series", "Total resistance = sum of all resistances"),
                ("Parallel", "Potential difference is the same across every branch"),
                ("Parallel", "Current splits between branches"),
                ("Parallel", "Total resistance is less than the smallest branch"),
                ("Parallel", "Used in household wiring"),
                ("Series", "One broken component stops the whole circuit"),
            ]
        },
        "fifas": [
            {
                "label": "Example 1 — Series circuit",
                "question": "Two resistors of 4 Ω and 8 Ω are connected in series to a 24 V battery. Calculate (a) total resistance, (b) current, (c) p.d. across each resistor.",
                "steps": [
                    ("F", "(a) R_total = R₁ + R₂. (b) I = V ÷ R_total. (c) V = I × R for each resistor"),
                    ("I", "(a) R_total = 4 + 8 = 12 Ω. (b) I = 24 ÷ 12 = 2 A. (c) V₁ = 2×4 = 8 V, V₂ = 2×8 = 16 V"),
                    ("F", "Check: V₁ + V₂ = 8 + 16 = 24 V ✅ (must equal battery p.d.)"),
                    ("A", "R_total = 12 Ω, I = 2 A, V₁ = 8 V, V₂ = 16 V")
                ]
            },
            {
                "label": "Example 2 — Parallel circuit (branch currents)",
                "question": "Two resistors of 6 Ω and 12 Ω are connected in parallel across a 12 V supply. Calculate the current in each branch and the total current.",
                "steps": [
                    ("F", "Each branch: I = V ÷ R (same V = 12 V across both branches)"),
                    ("I", "I₁ = 12 ÷ 6 = 2 A. I₂ = 12 ÷ 12 = 1 A"),
                    ("F", "I_total = I₁ + I₂"),
                    ("A", "I₁ = 2 A, I₂ = 1 A, I_total = 3 A")
                ]
            }
        ],
        "quiz": [
            {
                "q": "In a series circuit, what is the same at every point?",
                "opts": [
                    ("Current", True),
                    ("Potential difference", False),
                    ("Resistance", False),
                    ("Power", False)
                ],
                "wrong_explanations": {
                    1: "P.d. is SHARED in series — it splits across each component. Only current stays the same throughout a series circuit.",
                    2: "Resistance is different for each component — it doesn't stay the same throughout the circuit.",
                    3: "Power = VI — since both V and I vary by component, power varies too."
                }
            },
            {
                "q": "Two 6 Ω resistors are in series with a 12 V battery. What is the current?",
                "opts": [
                    ("1 A", True),
                    ("2 A", False),
                    ("4 A", False),
                    ("0.5 A", False)
                ],
                "wrong_explanations": {
                    1: "You forgot to add the resistors first! In series, R_total = 6 + 6 = 12 Ω. Then I = V ÷ R = 12 ÷ 12 = 1 A.",
                    2: "You divided V by one resistor only. In series you must add them: R_total = 12 Ω, I = 12 ÷ 12 = 1 A.",
                    3: "You multiplied instead of dividing somewhere. I = V ÷ R_total = 12 ÷ 12 = 1 A."
                }
            },
            {
                "q": "In a parallel circuit, what is the same across every branch?",
                "opts": [
                    ("Potential difference", True),
                    ("Current", False),
                    ("Resistance", False),
                    ("Charge", False)
                ],
                "wrong_explanations": {
                    1: "Current SPLITS in parallel — branches with lower resistance carry more current.",
                    2: "Resistance is different for each branch — that's why current splits unevenly.",
                    3: "Charge splits between branches just like current does."
                }
            },
            {
                "q": "Why are household appliances connected in parallel?",
                "opts": [
                    ("Each appliance gets full mains p.d. and can be switched independently", True),
                    ("It reduces the current through each appliance", False),
                    ("It means the total resistance is higher", False),
                    ("It prevents any current from flowing until all appliances are on", False)
                ],
                "wrong_explanations": {
                    1: "Parallel actually allows MORE total current from the supply — not less. Each branch carries its own current.",
                    2: "Adding more parallel branches DECREASES total resistance, it doesn't increase it.",
                    3: "In parallel, each branch works independently — you don't need all appliances on for any to work."
                }
            },
            {
                "q": "A series circuit has a 3 Ω and a 7 Ω resistor. The current is 2 A. What is the supply p.d.?",
                "opts": [
                    ("20 V", True),
                    ("5 V", False),
                    ("0.2 V", False),
                    ("8 V", False)
                ],
                "wrong_explanations": {
                    1: "You only used one resistor. In series, R_total = 3 + 7 = 10 Ω. V = I × R = 2 × 10 = 20 V.",
                    2: "You divided instead of multiplying. V = I × R_total = 2 × 10 = 20 V.",
                    3: "You may have just added the resistor values without multiplying by current. V = I × R = 2 × 10 = 20 V."
                }
            }
        ]
    },

    # ─────────────────────────────────────────────
    # 6. MAINS ELECTRICITY
    # ─────────────────────────────────────────────
    {
        "id": "mains-electricity",
        "title": "Mains Electricity — AC, DC and Safe Wiring",
        "spec": "4.2.3",
        "summary": "Describe AC and DC, the UK mains supply, and the role of each wire in a plug.",
        "theory": [
            {
                "heading": "DC — The Loyal Soldier",
                "content": "DC (Direct Current) always flows in the same direction — like a loyal soldier marching in one direction.\nSource: batteries, cells, solar panels.\nExample: the current from a phone battery is DC."
            },
            {
                "heading": "AC — The Indecisive One",
                "content": "AC (Alternating Current) repeatedly reverses direction — like someone who can't decide which way to walk.\nIn the UK: 50 times per second (50 Hz).\nSource: mains supply, generators.\nYour phone charger converts AC mains into DC for the battery."
            },
            {
                "heading": "The Three Wires — Know Them Cold",
                "content": "LIVE (brown): carries the 230 V alternating p.d. This is the dangerous wire.\nNEUTRAL (blue): completes the circuit, held at 0 V.\nEARTH (green and yellow): safety wire — only carries current if there's a fault."
            },
            {
                "heading": "Why the Earth Wire Saves Lives",
                "content": "If a fault occurs and the live wire touches the metal case of an appliance:\nWithout earth wire: you touch the case → current flows through YOU to earth → electric shock.\nWith earth wire: current flows through earth wire instead → fuse blows → circuit breaks → you're safe.\nThe earth wire is always connected to the metal casing of appliances."
            },
            {
                "heading": "Fuses vs Circuit Breakers",
                "content": "Fuse: a thin wire that melts if current gets too high, breaking the circuit. Always in the LIVE wire. Must be replaced after blowing.\nCircuit breaker: electromagnetic switch that trips if current exceeds the rated value. Can be reset.\nRCD (Residual Current Device): detects tiny imbalances between live and neutral. Trips in milliseconds — faster than a fuse. Used in bathrooms and outdoors."
            }
        ],
        "variables": [],
        "common_mistake": "Students say the live wire is safe when the switch is off — it is NOT. The live wire is ALWAYS at 230 V, even when the switch is open. The switch only breaks the circuit between the switch and the appliance — the wire from the mains to the switch is still live!",
        "key_note": "UK mains electricity: 230 V, 50 Hz (alternating current)",
        "higher": None,
        "triple_only": None,
        "equations": [],
        "rp": None,
        "matching": {
            "title": "Match the Wire to its Description",
            "instruction": "Match each wire to its colour and role.",
            "pairs": [
                ("Live wire", "Brown — carries the 230 V alternating p.d."),
                ("Neutral wire", "Blue — completes the circuit, held at 0 V"),
                ("Earth wire", "Green and yellow — safety wire, connected to metal casing"),
                ("Fuse", "Always in the live wire — melts to break circuit if current too high"),
                ("RCD", "Detects imbalance between live and neutral — trips in milliseconds"),
            ]
        },
        "fifas": [],
        "quiz": [
            {
                "q": "What colour is the live wire in a UK plug?",
                "opts": [
                    ("Brown", True),
                    ("Blue", False),
                    ("Green and yellow", False),
                    ("Red", False)
                ],
                "wrong_explanations": {
                    1: "Blue is the NEUTRAL wire — it completes the circuit but is held at 0 V, not 230 V.",
                    2: "Green and yellow is the EARTH wire — the safety wire. It's the one that saves you from electric shock.",
                    3: "Red was the old colour for live in UK wiring before 2006. Modern wiring uses BROWN for live."
                }
            },
            {
                "q": "What is the frequency of UK mains electricity?",
                "opts": [
                    ("50 Hz", True),
                    ("60 Hz", False),
                    ("230 Hz", False),
                    ("100 Hz", False)
                ],
                "wrong_explanations": {
                    1: "60 Hz is used in the USA and Canada — not in the UK.",
                    2: "230 is the VOLTAGE of UK mains, not the frequency.",
                    3: "100 Hz is double the mains frequency — this is actually the flicker rate you sometimes see in fluorescent lights."
                }
            },
            {
                "q": "Why is the live wire dangerous even when the switch is turned off?",
                "opts": [
                    ("The live wire is always at 230 V — the switch only breaks the circuit after itself", True),
                    ("Because the switch stores electricity", False),
                    ("The neutral wire passes charge to the live wire when the switch is off", False),
                    ("It is not dangerous when the switch is off", False)
                ],
                "wrong_explanations": {
                    1: "Switches don't store electricity! The danger is that the wire from the supply to the switch is still live.",
                    2: "The neutral wire is held at 0 V — it doesn't pass charge to the live wire.",
                    3: "This is dangerously wrong! The live wire between the mains supply and the switch is always at 230 V — never touch it."
                }
            },
            {
                "q": "What is the purpose of the earth wire?",
                "opts": [
                    ("Safety — it carries fault current to earth, preventing electric shock and blowing the fuse", True),
                    ("It carries the main 230 V supply to the appliance", False),
                    ("It completes the normal circuit when the appliance is on", False),
                    ("It reduces the current through the appliance", False)
                ],
                "wrong_explanations": {
                    1: "The LIVE wire carries the 230 V supply. The earth wire only carries current during a fault.",
                    2: "The NEUTRAL wire completes the normal circuit. The earth wire is purely a safety backup.",
                    3: "The earth wire doesn't limit current during normal operation. That's what fuses and resistors are for."
                }
            },
            {
                "q": "Which safety device trips the fastest in a fault?",
                "opts": [
                    ("RCD (Residual Current Device)", True),
                    ("Fuse", False),
                    ("Circuit breaker", False),
                    ("Earth wire", False)
                ],
                "wrong_explanations": {
                    1: "A fuse melts when current gets too high — but melting takes time. An RCD detects tiny imbalances and trips in milliseconds.",
                    2: "Circuit breakers are faster than fuses but slower than RCDs. RCDs detect faults that wouldn't even blow a fuse.",
                    3: "The earth wire isn't a switching device — it just provides a safe path for fault current."
                }
            }
        ]
    },

    # ─────────────────────────────────────────────
    # 7. ELECTRICAL POWER
    # ─────────────────────────────────────────────
    {
        "id": "electrical-power",
        "title": "Electrical Power",
        "spec": "4.2.4",
        "summary": "Calculate power using P = VI and P = I²R.",
        "theory": [
            {
                "heading": "What is Power?",
                "content": "Power is how quickly energy is transferred.\nA 2000 W kettle transfers 2000 J every single second.\nA 100 W bulb transfers 100 J every second.\nHigher wattage = more energy per second = 'more powerful'."
            },
            {
                "heading": "P = VI — The Main Power Equation",
                "content": "Use this when you know voltage and current.\nA higher p.d. means each charge carries more energy.\nA higher current means more charge passes every second.\nSo power goes up when EITHER p.d. or current increases."
            },
            {
                "heading": "P = I²R — When You Don't Know Voltage",
                "content": "Use this when you know current and resistance but not p.d.\nNotice the I² — this means doubling the current QUADRUPLES the power.\nThis is why cables heat up — even a small increase in current causes a BIG increase in power lost as heat.\nThis is also why the National Grid uses HIGH voltage and LOW current — to reduce I²R losses in the cables."
            },
            {
                "heading": "The National Grid",
                "content": "Electricity travels across the UK at 400,000 V — step-up transformers boost the voltage.\nHigh voltage = low current for the same power.\nLow current = less power wasted as heat in the cables (P_loss = I²R).\nBefore it reaches your home, step-down transformers bring it back to 230 V."
            }
        ],
        "variables": [
            ("P", "Power", "Watts", "W"),
            ("V", "Potential Difference", "Volts", "V"),
            ("I", "Current", "Amperes", "A"),
            ("R", "Resistance", "Ohms", "Ω"),
        ],
        "common_mistake": "In P = I²R, students forget to square the current first. Write it out as P = (I × I) × R if it helps. Also — don't mix up P = VI with E = QV. Power (P) is energy per second. Energy (E) is power × time.",
        "key_note": None,
        "higher": "National Grid power loss: P_loss = I²R. Doubling transmission voltage halves current, reducing power loss to ONE QUARTER (because I² is quartered). This is why the grid uses 400 kV.",
        "triple_only": None,
        "equations": ["P = VI", "P = I²R"],
        "rp": None,
        "matching": None,
        "fifas": [
            {
                "label": "Example 1 — Using P = VI",
                "question": "A hairdryer operates at 230 V and draws a current of 5 A. Calculate its power rating.",
                "steps": [
                    ("F", "P = V × I"),
                    ("I", "P = 230 × 5"),
                    ("F", "No unit conversion needed"),
                    ("A", "P = 1150 W")
                ]
            },
            {
                "label": "Example 2 — Using P = I²R",
                "question": "A resistor of 6 Ω carries a current of 3 A. Calculate the power dissipated.",
                "steps": [
                    ("F", "P = I² × R"),
                    ("I", "P = 3² × 6 = 9 × 6"),
                    ("F", "Square the current FIRST — don't multiply 3 × 6 then square!"),
                    ("A", "P = 54 W")
                ]
            },
            {
                "label": "Example 3 — National Grid power loss",
                "question": "A transmission cable has resistance 5 Ω and carries a current of 200 A. Calculate the power wasted as heat.",
                "steps": [
                    ("F", "P_loss = I² × R"),
                    ("I", "P_loss = 200² × 5 = 40,000 × 5"),
                    ("F", "Square the current first: 200² = 40,000"),
                    ("A", "P_loss = 200,000 W = 200 kW — this is why high voltage (low current) matters!")
                ]
            }
        ],
        "quiz": [
            {
                "q": "A 6 Ω resistor carries a current of 3 A. What is its power output?",
                "opts": [
                    ("54 W", True),
                    ("18 W", False),
                    ("2 W", False),
                    ("162 W", False)
                ],
                "wrong_explanations": {
                    1: "You forgot to square the current! P = I²R = 3 × 6 = 18 only if you don't square. P = (3²) × 6 = 9 × 6 = 54 W.",
                    2: "You divided R by I. P = I²R = 9 × 6 = 54 W — always multiply.",
                    3: "You squared the whole of (I × R) instead of just I. Square I first: P = I² × R = 9 × 6 = 54 W."
                }
            },
            {
                "q": "Why does the National Grid transmit electricity at high voltage?",
                "opts": [
                    ("High voltage means low current, which reduces I²R power losses", True),
                    ("High voltage means high current, giving more power", False),
                    ("It makes the electricity safer for homes", False),
                    ("It increases the total power generated", False)
                ],
                "wrong_explanations": {
                    1: "High voltage means HIGH current for the same power — but that would massively increase heating losses. It's the opposite!",
                    2: "400,000 V would kill you instantly — it's not safe for homes. That's why step-down transformers bring it to 230 V.",
                    3: "The grid doesn't generate more power — it just transmits the same power more efficiently."
                }
            },
            {
                "q": "A kettle is rated 2 kW. It runs for 3 minutes. How much energy does it transfer?",
                "opts": [
                    ("360,000 J", True),
                    ("6000 J", False),
                    ("360 J", False),
                    ("6 J", False)
                ],
                "wrong_explanations": {
                    1: "You forgot to convert time to seconds! E = P × t = 2000 × 3 = 6000 J only if t is in seconds. 3 minutes = 180 s → E = 2000 × 180 = 360,000 J.",
                    2: "You divided energy by time somewhere. E = P × t — always multiply power by time (in seconds).",
                    3: "You used minutes directly AND divided. Always convert to seconds: 3 min = 180 s."
                }
            },
            {
                "q": "An appliance is rated 230 V, 2 A. What is its power?",
                "opts": [
                    ("460 W", True),
                    ("115 W", False),
                    ("232 W", False),
                    ("4 W", False)
                ],
                "wrong_explanations": {
                    1: "You divided V by I. P = V × I = 230 × 2 = 460 W — always multiply.",
                    2: "You added V and I instead of multiplying. P = V × I = 230 × 2 = 460 W.",
                    3: "You subtracted V and I. There's no subtraction in P = VI."
                }
            },
            {
                "q": "The current in a cable doubles. What happens to the power lost as heat (P = I²R)?",
                "opts": [
                    ("It quadruples (×4)", True),
                    ("It doubles (×2)", False),
                    ("It stays the same", False),
                    ("It halves (÷2)", False)
                ],
                "wrong_explanations": {
                    1: "Doubling I means power DOUBLES — but remember P = I²R. If I doubles, I² becomes 4 times bigger. So power quadruples.",
                    2: "If resistance R stayed constant but current changed, it would have no effect — but R is multiplied by I², not I.",
                    3: "If I doubles, P = I²R means P = (2I)²R = 4I²R — the power halves only if current halves."
                }
            }
        ]
    },

    # ─────────────────────────────────────────────
    # 8. ENERGY TRANSFER
    # ─────────────────────────────────────────────
    {
        "id": "energy-transfer",
        "title": "Energy Transfers in Electrical Circuits",
        "spec": "4.2.4",
        "summary": "Calculate energy transferred using E = Pt and E = QV.",
        "theory": [
            {
                "heading": "E = Pt — Energy from Power and Time",
                "content": "Energy = Power × Time.\nThink: a powerful appliance running for a long time transfers a LOT of energy.\nTime MUST be in seconds for the answer to be in Joules.\nIf you want the answer in kWh (for electricity bills), keep power in kW and time in hours."
            },
            {
                "heading": "E = QV — Energy from Charge and P.D.",
                "content": "Each unit of charge carries energy equal to the p.d. it moves through.\nSo total energy = total charge × potential difference.\nThis links nicely with Q = It — substituting gives E = I × t × V = P × t. All connected!"
            },
            {
                "heading": "Paying for Electricity — kWh",
                "content": "Your electricity meter counts energy in kilowatt-hours (kWh).\n1 kWh = the energy used by a 1 kW appliance in 1 hour.\n1 kWh = 1000 × 3600 = 3,600,000 J = 3.6 MJ.\nCost = power (kW) × time (hours) × price per kWh."
            },
            {
                "heading": "Transformers in the National Grid",
                "content": "Step-UP transformer: increases p.d., decreases current — used to send electricity across the country.\nStep-DOWN transformer: decreases p.d., increases current — used before electricity enters homes.\nFor a 100% efficient transformer: power in = power out, so Vp × Ip = Vs × Is."
            }
        ],
        "variables": [
            ("E", "Energy", "Joules", "J"),
            ("P", "Power", "Watts", "W"),
            ("t", "Time", "Seconds", "s"),
            ("Q", "Charge", "Coulombs", "C"),
            ("V", "Potential Difference", "Volts", "V"),
        ],
        "common_mistake": "Mixing up E = Pt (energy from power) with P = VI (power from voltage and current). They're related but different! Also — when using kWh for electricity bills, keep power in kW and time in HOURS. Switch to seconds only when you need Joules.",
        "key_note": "1 kilowatt-hour (kWh) = 3,600,000 J = 3.6 MJ",
        "higher": "For a 100% efficient transformer: Vp/Vs = Np/Ns and Vp × Ip = Vs × Is. Real transformers are close to 100% efficient — energy losses are mainly heating in the coils.",
        "triple_only": None,
        "equations": ["E = Pt", "E = QV"],
        "rp": None,
        "matching": None,
        "fifas": [
            {
                "label": "Example 1 — Using E = QV",
                "question": "A charge of 500 C flows through a device with a p.d. of 12 V across it. Calculate the energy transferred.",
                "steps": [
                    ("F", "E = Q × V"),
                    ("I", "E = 500 × 12"),
                    ("F", "No unit conversion needed"),
                    ("A", "E = 6000 J")
                ]
            },
            {
                "label": "Example 2 — Using E = Pt (with time conversion)",
                "question": "A 1500 W electric heater runs for 2 hours. Calculate the energy transferred in Joules and in kWh.",
                "steps": [
                    ("F", "In Joules: E = P × t (t in seconds). In kWh: E = P(kW) × t(hours)"),
                    ("I", "In Joules: t = 2 × 3600 = 7200 s → E = 1500 × 7200. In kWh: P = 1.5 kW, t = 2 h → E = 1.5 × 2"),
                    ("F", "Two different approaches — both valid"),
                    ("A", "E = 10,800,000 J = 10.8 MJ. In kWh: E = 3 kWh")
                ]
            },
            {
                "label": "Example 3 — Electricity bill calculation",
                "question": "A 2.5 kW tumble dryer runs for 90 minutes. Electricity costs 28p per kWh. Calculate the cost.",
                "steps": [
                    ("F", "Energy (kWh) = P(kW) × t(hours). Cost = energy × price per kWh"),
                    ("I", "t = 90 min = 1.5 hours. Energy = 2.5 × 1.5 = 3.75 kWh"),
                    ("F", "Cost = 3.75 × 28p"),
                    ("A", "Cost = 105p = £1.05")
                ]
            }
        ],
        "quiz": [
            {
                "q": "A 2 kW heater runs for 3 hours. How much energy does it use in kWh?",
                "opts": [
                    ("6 kWh", True),
                    ("0.67 kWh", False),
                    ("7200 kWh", False),
                    ("2 kWh", False)
                ],
                "wrong_explanations": {
                    1: "You divided instead of multiplying. Energy (kWh) = P(kW) × t(hours) = 2 × 3 = 6 kWh.",
                    2: "You converted hours to seconds (×3600) when using kWh — you don't need to! For kWh, keep time in hours: 2 × 3 = 6 kWh.",
                    3: "You used just the power without multiplying by time. E = P × t = 2 × 3 = 6 kWh."
                }
            },
            {
                "q": "How many joules are in 1 kWh?",
                "opts": [
                    ("3,600,000 J", True),
                    ("1000 J", False),
                    ("3600 J", False),
                    ("1,000,000 J", False)
                ],
                "wrong_explanations": {
                    1: "1000 J = 1 kJ, not 1 kWh. A kilowatt-hour is much bigger than a kilojoule.",
                    2: "3600 J = 1 Wh (watt-hour), not 1 kWh. You need to multiply by 1000: 1 kWh = 3,600,000 J.",
                    3: "A megajoule (MJ) = 1,000,000 J. 1 kWh = 3.6 MJ = 3,600,000 J — close but not 1 MJ."
                }
            },
            {
                "q": "A charge of 200 C moves through a p.d. of 9 V. How much energy is transferred?",
                "opts": [
                    ("1800 J", True),
                    ("22.2 J", False),
                    ("191 J", False),
                    ("209 J", False)
                ],
                "wrong_explanations": {
                    1: "You divided Q by V. E = Q × V = 200 × 9 = 1800 J — always multiply.",
                    2: "You subtracted V from Q instead of multiplying. E = Q × V = 200 × 9 = 1800 J.",
                    3: "You added Q and V instead of multiplying. E = Q × V = 200 × 9 = 1800 J."
                }
            },
            {
                "q": "What does a step-up transformer do?",
                "opts": [
                    ("Increases voltage and decreases current", True),
                    ("Increases both voltage and current", False),
                    ("Decreases voltage and increases current", False),
                    ("Keeps voltage the same but increases current", False)
                ],
                "wrong_explanations": {
                    1: "If both increased, power would increase — a transformer can't create energy! Power in = Power out, so V up means I down.",
                    2: "A step-DOWN transformer decreases voltage and increases current — used before electricity enters your home.",
                    3: "A transformer that keeps voltage the same is not a transformer — it's just a wire!"
                }
            },
            {
                "q": "Electricity costs 30p per kWh. A 3 kW appliance runs for 2 hours. What is the cost?",
                "opts": [
                    ("£1.80", True),
                    ("90p", False),
                    ("£18.00", False),
                    ("60p", False)
                ],
                "wrong_explanations": {
                    1: "You only used power without multiplying by time. Energy = 3 × 2 = 6 kWh. Cost = 6 × 30p = 180p = £1.80.",
                    2: "You moved the decimal point wrong. 6 kWh × 30p = 180p = £1.80, not £18.",
                    3: "You used watts instead of kilowatts. P = 3 kW (not 3000 kW). Energy = 3 × 2 = 6 kWh. Cost = 6 × 30 = 180p = £1.80."
                }
            }
        ]
    },

    # ─────────────────────────────────────────────
    # 9. STATIC ELECTRICITY (Triple only)
    # ─────────────────────────────────────────────
    {
        "id": "static-electricity",
        "title": "Static Electricity",
        "spec": "4.2.5",
        "summary": "Explain static charge build-up, electric fields, and real-world applications.",
        "theory": [
            {
                "heading": "How Static Charge Builds Up",
                "content": "When two insulators are rubbed together, electrons transfer from one to the other.\nThe object that GAINS electrons becomes negatively charged.\nThe object that LOSES electrons becomes positively charged.\nOnly electrons move — protons are locked in the nucleus and never transfer."
            },
            {
                "heading": "Attraction and Repulsion",
                "content": "Like charges REPEL — two negative objects push away from each other.\nUnlike charges ATTRACT — positive and negative pull towards each other.\nThink: North poles of two magnets pushing apart — same idea with same charges."
            },
            {
                "heading": "Electric Fields",
                "content": "An electric field is the region around a charged object where another charge experiences a force.\nField lines point FROM positive TO negative — like an arrow showing the direction a positive charge would move.\nCloser field lines = stronger field.\nBetween two parallel plates: uniform field — evenly spaced parallel lines."
            },
            {
                "heading": "Real-World Uses",
                "content": "Inkjet printers: charged ink droplets are deflected by electric fields to land in the right place.\nElectrostatic paint sprayers: paint droplets are charged, car body is earthed — paint is attracted evenly.\nElectrostatic precipitators: remove dust and soot from factory chimneys using charged plates.\nDefibrillators: deliver a controlled electric shock to restart the heart."
            },
            {
                "heading": "Dangers of Static",
                "content": "Fuel tankers are earthed before refuelling — a spark from static could ignite fuel vapour.\nAircraft build up charge during flight — earthing strips discharge them safely on landing.\nElectronic components can be destroyed by static discharge — handled with anti-static mats and wristbands."
            }
        ],
        "variables": [],
        "common_mistake": "Students say 'protons transfer during charging by friction' — they DON'T. Only electrons move. Protons are in the nucleus and can't transfer. Always say 'electrons are transferred from X to Y'.",
        "key_note": None,
        "higher": "Electric field strength: E = V ÷ d (p.d. between plates ÷ distance apart). Force on a charge: F = EQ. Stronger field or larger charge = larger force.",
        "triple_only": "This entire subtopic (4.2.5) is TRIPLE SCIENCE ONLY — it does not appear in Combined Science Trilogy.",
        "equations": ["F = EQ (Higher)", "E = V/d (Higher)"],
        "rp": None,
        "matching": {
            "title": "Match the Application to How Static is Used",
            "instruction": "Match each device or situation to how it uses static electricity.",
            "pairs": [
                ("Inkjet printer", "Charged ink droplets are deflected by electric fields to land precisely"),
                ("Electrostatic paint sprayer", "Charged paint droplets are attracted to an earthed car body"),
                ("Electrostatic precipitator", "Charged plates attract soot and dust particles from chimney smoke"),
                ("Fuel tanker earthing", "Prevents sparks from static charge that could ignite fuel vapour"),
                ("Anti-static wristband", "Safely conducts static charge away from sensitive electronics"),
            ]
        },
        "fifas": [
            {
                "label": "Example 1 — Explaining charge transfer",
                "question": "A plastic rod is rubbed with a cloth. Explain why the rod becomes negatively charged.",
                "steps": [
                    ("F", "Identify what transfers during friction charging"),
                    ("I", "Electrons (negatively charged) transfer from the cloth to the plastic rod"),
                    ("F", "Protons cannot move — they are fixed in the nucleus"),
                    ("A", "The rod gains electrons → gains negative charge. The cloth loses electrons → becomes positively charged")
                ]
            },
            {
                "label": "Example 2 — Electric field strength (Higher)",
                "question": "Two parallel plates are 0.02 m apart. The p.d. between them is 500 V. Calculate the electric field strength.",
                "steps": [
                    ("F", "E = V ÷ d"),
                    ("I", "E = 500 ÷ 0.02"),
                    ("F", "No unit conversion needed"),
                    ("A", "E = 25,000 V/m = 25 kV/m")
                ]
            }
        ],
        "quiz": [
            {
                "q": "A plastic rod is rubbed with a cloth and becomes negatively charged. What happened?",
                "opts": [
                    ("Electrons transferred from the cloth to the rod", True),
                    ("Protons transferred from the rod to the cloth", False),
                    ("Neutrons transferred from the cloth to the rod", False),
                    ("Electrons transferred from the rod to the cloth", False)
                ],
                "wrong_explanations": {
                    1: "Protons are locked in the nucleus and NEVER transfer. Only electrons move during friction charging.",
                    2: "Neutrons are uncharged — they play no role in static electricity.",
                    3: "If electrons transferred FROM the rod, it would lose negative charge and become POSITIVE. The rod is negative, so it must have GAINED electrons."
                }
            },
            {
                "q": "Two positively charged spheres are brought close together. What happens?",
                "opts": [
                    ("They repel each other", True),
                    ("They attract each other", False),
                    ("Nothing happens", False),
                    ("One becomes neutral", False)
                ],
                "wrong_explanations": {
                    1: "Unlike charges (+ and −) attract. LIKE charges (both + or both −) always REPEL.",
                    2: "If nothing happened, there would be no electric field — but charged objects always create fields and exert forces.",
                    3: "Charges don't neutralise just by being near each other — they need to physically touch and share charge."
                }
            },
            {
                "q": "In which direction do electric field lines point?",
                "opts": [
                    ("From positive to negative", True),
                    ("From negative to positive", False),
                    ("In circles around the charge", False),
                    ("Randomly in all directions", False)
                ],
                "wrong_explanations": {
                    1: "Field lines point FROM positive TO negative — the direction a positive test charge would move.",
                    2: "Circular field lines are for magnetic fields around a wire — not electric fields.",
                    3: "Electric field lines are not random — they follow specific patterns from + to −."
                }
            },
            {
                "q": "Why are fuel tankers earthed before refuelling?",
                "opts": [
                    ("To safely discharge any built-up static charge and prevent sparks near fuel vapour", True),
                    ("To increase the flow rate of the fuel", False),
                    ("To measure how much fuel is in the tanker", False),
                    ("To prevent the fuel from evaporating", False)
                ],
                "wrong_explanations": {
                    1: "Earthing has nothing to do with fuel flow rate — it's purely an electrical safety measure.",
                    2: "Earthing is a safety measure against static sparks, not a measuring device.",
                    3: "Earthing removes electrical charge — it has no effect on fuel vapour pressure."
                }
            },
            {
                "q": "How does an electrostatic paint sprayer work?",
                "opts": [
                    ("Charged paint droplets are attracted to the earthed metal body of the car", True),
                    ("Paint is heated and sprayed at high pressure", False),
                    ("The car body is charged positively and repels the paint away evenly", False),
                    ("Magnets in the sprayer attract the paint to the surface", False)
                ],
                "wrong_explanations": {
                    1: "Pressure spraying is used in conventional sprayers — it doesn't use static electricity.",
                    2: "If the car body repelled the paint, none would stick! Unlike charges attract — earthed body (neutral) attracts charged paint.",
                    3: "Electrostatic paint sprayers use electric charge, not magnetism. Paint isn't magnetic."
                }
            }
        ]
    }
]

# ─────────────────────────────────────────────
# PAGE RENDERER — all corrections applied
# ─────────────────────────────────────────────

def make_variable_rows(variables):
    if not variables:
        return ""
    rows = ""
    for sym, name, unit_name, unit_sym in variables:
        rows += f'<div class="var-row"><span class="var-sym">{sym}</span><span class="var-desc">{name} ({sym}) is measured in {unit_name} ({unit_sym})</span></div>\n'
    return f'<div class="var-table">{rows}</div>'


def make_matching_widget(matching, st_id, color):
    if not matching:
        return ""
    import json as _json
    import random

    # Support both svg_pairs and regular pairs
    pairs = matching.get("svg_pairs") or matching.get("pairs", [])
    use_svg = "svg_pairs" in matching

    pairs_len = len(pairs)

    # Grade by CATEGORY GROUP, not by row index (MRB-104).
    # A "term" is the left-hand label; many matchings are category sorts where
    # several rows share the same term (e.g. three rows labelled "Energy store").
    # The old grader compared each def's original row-index to the slot index,
    # so a correctly-categorised item dropped into a same-labelled sibling slot
    # scored WRONG. We instead give every distinct term a group id: a slot is
    # correct when the item dropped in it belongs to a row with the same term.
    # For one-to-one matchings each term is unique, so group id == row identity
    # and behaviour is unchanged. Handles both variants with no schema change.
    term_group = {}
    for t, _ in pairs:
        if t not in term_group:
            term_group[t] = len(term_group)

    # Shuffle the definitions (right-hand side) so they don't appear in order.
    # Seeded per subtopic so regeneration is deterministic — same content in,
    # byte-identical page out. Unseeded shuffling made every generator run
    # rewrite ~1,000 unchanged pages (the "shuffle churn").
    indexed_pairs = list(enumerate(pairs))
    shuffled_defs = list(indexed_pairs)
    random.Random("match:%s:%d" % (st_id, pairs_len)).shuffle(shuffled_defs)

    items_html = ""
    for i, pair in shuffled_defs:
        term, content_item = pair
        g = term_group[term]
        items_html += f'<div class="match-def{" match-def-svg" if use_svg else ""}" data-index="{i}" data-group="{g}" draggable="true">{content_item}</div>\n'

    terms_html = ""
    for i, pair in enumerate(pairs):
        term, _ = pair
        g = term_group[term]
        terms_html += f'''<div class="match-target" data-index="{i}">
  <div class="match-term">{term}</div>
  <div class="match-drop" data-accepts="{i}" data-accepts-group="{g}">Drop here</div>
</div>\n'''

    return f"""<div class="section">
  <div class="section-title">🎯 Matching Activity — {matching['title']}</div>
  <div class="card">
    <p style="font-size:0.88rem;color:var(--muted);margin-bottom:16px;">{matching['instruction']} — drag the symbols on the right to match the component names on the left.</p>
    <div class="match-layout">
      <div class="match-targets">{terms_html}</div>
      <div class="match-defs" id="defPool-{st_id}">{items_html}</div>
    </div>
    <div style="display:flex;gap:12px;margin-top:16px;flex-wrap:wrap;">
      <button class="match-check-btn" onclick="checkMatching('{st_id}', {pairs_len})">✅ Check Answers</button>
      <button class="match-reset-btn" onclick="resetMatching('{st_id}', {pairs_len})">🔄 Reset</button>
    </div>
    <div class="match-result" id="matchResult-{st_id}"></div>
  </div>
</div>"""


def make_fifa_boxes(fifas):
    if not fifas:
        return ""
    boxes = ""
    for fifa in fifas:
        steps_html = ""
        for letter, text in fifa["steps"]:
            steps_html += f"""<div class="fifa-step">
  <div class="fifa-letter">{letter}</div>
  <p>{text}</p>
</div>"""
        boxes += f"""<div class="fifa-box" style="margin-bottom:20px;">
  <div class="fifa-label">{fifa['label']}</div>
  <p class="fifa-question">{fifa['question']}</p>
  {steps_html}
</div>"""
    return f"""<div class="section">
  <div class="section-title">⚽ FIFA Worked Examples</div>
  {boxes}
</div>"""


def _esc_attr(s):
    """Escape a string for safe use inside a double-quoted HTML attribute."""
    return (str(s).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def make_pilot_quiz(quiz):
    """
    Reveal-at-end quiz (MRB-121) — pilot page only.

    Differs from the standard make_new_quiz in three ways:
      1. Options are emitted in CANONICAL order (no build-time shuffle) — the
         browser shuffles them on load, exactly like the Categorise Bins hero.
         This kills the build-time shuffle churn on this page.
      2. Each option carries its own correctness (`data-correct`) and, for a
         wrong option, its misconception text (`data-wrong-exp`). Grading is by
         attribute, so it is independent of the display order.
      3. No feedback markup is pre-shown. The PILOT_QUIZ_JS controller withholds
         all correct/incorrect feedback until "Check answers" is pressed.

    Question text, options, correct answers and misconception text are frozen —
    this is behaviour only.
    """
    cards_html = ""
    for i, q in enumerate(quiz):
        orig_wrong_exp = q.get("wrong_explanations", {})
        opts_html = ""
        for orig_j, (opt_text, is_correct) in enumerate(q["opts"]):
            attrs = f' data-qi="{i}"'
            if is_correct:
                attrs += ' data-correct="1"'
            else:
                exp = orig_wrong_exp.get(orig_j)
                if exp:
                    attrs += f' data-wrong-exp="{_esc_attr(exp)}"'
            opts_html += f'<button class="quiz-opt"{attrs}>{opt_text}</button>\n'
        cards_html += f"""<div class="quiz-card" id="qcard-{i}">
  <div class="q-text">{i+1}. {q['q']}</div>
  <div class="quiz-options">{opts_html}</div>
  <div class="quiz-fb" id="qfb-{i}"></div>
</div>"""

    return f"""<div class="section">
  <div class="section-title">🎯 Test Yourself</div>
  <div class="quiz-progress" id="quizProgress">Answer all {len(quiz)} questions, then check your answers.</div>
  {cards_html}
  <div class="quiz-actions">
    <button class="quiz-check-btn" id="quizCheckBtn" type="button">✓ Check answers</button>
    <button class="quiz-again-btn" id="quizAgainBtn" type="button" style="display:none;">↻ Try again</button>
  </div>
  <div class="quiz-end-msg" id="quizEndMsg" style="display:none;margin-top:16px;padding:16px 20px;border-radius:12px;font-size:0.95rem;font-weight:700;text-align:center;"></div>
</div>"""


# Reveal-at-end quiz controller (MRB-121, pilot page only). Emitted in place of
# the standard instant-mark quiz_js. Selecting an option only records the
# choice; no green/red until "Check answers". Grading reads data-correct, so it
# is independent of the browser-shuffled option order. "Try again" clears and
# reshuffles (same approach as the bins hero).
PILOT_QUIZ_JS = """
(function(){
  const SCORE_MESSAGES = [
    "Keep going — re-read the theory and try again. You'll get there! 📖",
    "Not bad — review the sections you missed and have another go. 💪",
    "Decent effort! A bit more revision and you'll nail it. 🔄",
    "Good work! Just a couple of gaps to fill. Nearly there! 🌟",
    "Excellent! You've really got this topic down. 🏆"
  ];
  const cards = Array.from(document.querySelectorAll('.quiz-card'));
  const total = cards.length;
  if (!total) return;
  const checkBtn = document.getElementById('quizCheckBtn');
  const againBtn = document.getElementById('quizAgainBtn');
  const endMsg = document.getElementById('quizEndMsg');
  const prog = document.getElementById('quizProgress');
  let checked = false;

  // Browser-side option shuffle (Fisher–Yates), consistent with the bins hero.
  function shuffleOptions(){
    document.querySelectorAll('.quiz-options').forEach(function(box){
      const opts = Array.from(box.querySelectorAll('.quiz-opt'));
      for (let k = opts.length - 1; k > 0; k--){
        const j = Math.floor(Math.random() * (k + 1));
        const t = opts[k]; opts[k] = opts[j]; opts[j] = t;
      }
      opts.forEach(function(o){ box.appendChild(o); });
    });
  }

  function updateProgress(){
    if (checked || !prog) return;
    const answered = cards.filter(function(c){ return c.querySelector('.quiz-opt.selected'); }).length;
    prog.textContent = answered === total
      ? 'All ' + total + ' answered — hit Check answers below ↓'
      : answered + ' of ' + total + ' answered';
  }

  function onSelect(){
    if (checked) return;
    const box = this.closest('.quiz-options');
    box.querySelectorAll('.quiz-opt').forEach(function(o){ o.classList.remove('selected'); });
    this.classList.add('selected');
    updateProgress();
  }

  function reveal(){
    checked = true;
    let correctCount = 0;
    cards.forEach(function(card, i){
      const opts = Array.from(card.querySelectorAll('.quiz-opt'));
      const chosen = card.querySelector('.quiz-opt.selected');
      const fb = document.getElementById('qfb-' + i);
      opts.forEach(function(o){ o.disabled = true; o.classList.remove('selected'); });
      const correctOpt = opts.filter(function(o){ return o.dataset.correct === '1'; })[0];
      if (correctOpt) correctOpt.classList.add('correct');
      const isRight = !!(chosen && chosen.dataset.correct === '1');
      if (isRight) correctCount++;
      if (chosen && !isRight) chosen.classList.add('wrong');
      if (!fb) return;
      if (!chosen){
        fb.className = 'quiz-fb wrong-fb show';
        fb.textContent = '⚠️ Not answered — the correct answer is highlighted above.';
      } else if (isRight){
        fb.className = 'quiz-fb correct-fb show';
        fb.textContent = '✅ Correct! Well done!';
      } else {
        const exp = chosen.dataset.wrongExp;
        fb.className = 'quiz-fb wrong-fb show';
        fb.textContent = exp ? ('❌ Not quite. ' + exp) : '❌ Not quite — the correct answer is highlighted above.';
      }
    });
    if (prog) prog.textContent = '🎉 Finished! ' + correctCount + '/' + total + ' correct';
    if (endMsg){
      const ratio = correctCount / total;
      const msgIdx = ratio === 1 ? 4 : ratio >= 0.8 ? 3 : ratio >= 0.6 ? 2 : ratio >= 0.4 ? 1 : 0;
      endMsg.textContent = correctCount + '/' + total + ' — ' + SCORE_MESSAGES[msgIdx];
      endMsg.style.display = 'block';
      endMsg.style.background = ratio === 1 ? 'rgba(35,122,59,0.10)' : ratio >= 0.6 ? 'rgba(122,95,0,0.10)' : 'rgba(179,38,30,0.09)';
      endMsg.style.color = ratio === 1 ? '#237A3B' : ratio >= 0.6 ? '#7A5F00' : '#B3261E';
      endMsg.style.border = '1px solid ' + (ratio === 1 ? 'rgba(35,122,59,0.3)' : ratio >= 0.6 ? 'rgba(122,95,0,0.3)' : 'rgba(179,38,30,0.3)');
    }
    if (checkBtn) checkBtn.style.display = 'none';
    if (againBtn) againBtn.style.display = '';
  }

  function tryAgain(){
    checked = false;
    cards.forEach(function(card, i){
      card.querySelectorAll('.quiz-opt').forEach(function(o){
        o.disabled = false;
        o.classList.remove('selected', 'correct', 'wrong');
      });
      const fb = document.getElementById('qfb-' + i);
      if (fb){ fb.className = 'quiz-fb'; fb.textContent = ''; }
    });
    if (endMsg){ endMsg.style.display = 'none'; endMsg.textContent = ''; }
    if (checkBtn) checkBtn.style.display = '';
    if (againBtn) againBtn.style.display = 'none';
    shuffleOptions();
    updateProgress();
  }

  cards.forEach(function(card){
    card.querySelectorAll('.quiz-opt').forEach(function(btn){ btn.addEventListener('click', onSelect); });
  });
  if (checkBtn) checkBtn.addEventListener('click', reveal);
  if (againBtn) againBtn.addEventListener('click', tryAgain);
  shuffleOptions();
  updateProgress();
})();
"""


def _rd_quiz_options(q):
    """Canonical-order options with data-correct / data-wrong-exp attributes.
    The browser shuffles per load (shared/quiz.js); grading is by attribute,
    so display order can never leak or affect marks. Question text, options
    and misconception text are frozen — behaviour only."""
    orig_wrong_exp = q.get("wrong_explanations", {})
    opts_html = ""
    for orig_j, (opt_text, is_correct) in enumerate(q["opts"]):
        attrs = ""
        if is_correct:
            attrs += ' data-correct="1"'
        else:
            exp = orig_wrong_exp.get(orig_j)
            if exp:
                attrs += f' data-wrong-exp="{_esc_attr(exp)}"'
        opts_html += f'<button class="quiz-opt" type="button"{attrs}>{opt_text}</button>\n'
    return opts_html


def _esc_html(s):
    """Escape plain text for HTML element content."""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def split_key_note(text):
    """Split a frozen Key Note into mark-scheme-ordered steps at sentence
    boundaries — SPLIT ONLY, never edit (MRB-134 Fix 5, law 10). Guarantees the
    steps rejoin to the exact original (whitespace-normalised); on ANY mismatch
    the whole note is returned as one step, so the splitter can never alter
    frozen text. Abbreviations (e.g./i.e.) are shielded from the boundary rule."""
    t = (text or "").strip()
    if not t:
        return []
    SH = "\uE000"
    guard = (t.replace("e.g. ", "e" + SH + "g" + SH + " ")
              .replace("i.e. ", "i" + SH + "e" + SH + " "))
    pieces = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", guard)
    steps = [p.replace(SH, ".").strip() for p in pieces if p.strip()]
    # lossless check: rejoining with single spaces must reconstruct the note
    if " ".join(steps) != re.sub(r"\s+", " ", t):
        return [t]
    return steps


def make_rd_keycard(key_note, subtopic_title=""):
    """Key Note as a photographable revision card with STEPPED cover-and-recall
    (MRB-134 Fix 5): the frozen note is split into numbered steps; the card shows
    all steps by default and the button walks cover -> reveal step 1 -> ... ->
    all shown (rd-page.js). Steps numbered in mono. Frozen text is split, not
    edited.

    Phase 2B revision #4/5: the card carries its subtopic as a title INSIDE the
    card. It is meant to be photographed and revised from later, so a card that
    does not say what it is about is a card you cannot use out of context."""
    steps = split_key_note(key_note)
    n = len(steps)
    lbl = "Revision card" + (" · %d steps" % n if n > 1 else "")
    title_html = ('\n      <span class="rd-keycard__title">%s</span>'
                  % _esc_html(subtopic_title) if subtopic_title else "")
    items = "".join(
        '<li class="rd-keycard__step">'
        '<span class="rd-keycard__step-n">%02d</span>'
        '<span class="rd-keycard__step-text">%s</span></li>'
        % (i + 1, _esc_html(s)) for i, s in enumerate(steps))
    return f"""
<div class="section">
  <div class="rd-sec-kicker">Key note · cover it, say it, check it</div>
  <div class="rd-keycard" data-steps="{n}">
    <div class="rd-keycard__hd">
      <div class="rd-keycard__id">
        <span class="rd-keycard__lbl">{lbl}</span>{title_html}
      </div>
      <button class="rd-keycard__cover" type="button" aria-pressed="false">Cover &amp; recall</button>
    </div>
    <ol class="rd-keycard__steps">{items}</ol>
  </div>
</div>"""


def make_rd_checkpoint(q, st_id, n):
    """One checkpoint micro-quiz (MRB-133 Phase 1c): a frozen quiz question
    RELOCATED inline after the theory block it tests. Immediate feedback on
    selection — the frozen wrong-option explanations do the teaching."""
    return f"""<div class="rd-checkpoint" id="cp-{st_id}-{n}">
  <div class="rd-checkpoint__kicker">Checkpoint · quick check</div>
  <div class="q-text">{q['q']}</div>
  <div class="quiz-options">{_rd_quiz_options(q)}</div>
  <div class="quiz-fb"></div>
</div>"""


def make_rd_quiz(quiz, st_id, checkpoint_qidxs, pre_html=""):
    """Exam-paper quiz (MRB-133 Phase 1c, council §5.7): one continuous panel,
    hanging mono numbers (CSS counters), hairline rules, compact lettered
    options, chunked Warm-up / Exam standard / Stretch with later chunks in
    <details>, a sticky progress chip and per-chunk check buttons.
    Questions listed in checkpoint_qidxs render inline as checkpoints instead
    (relocated, not duplicated). pre_html sits above the panel (e.g. the
    relocated Examiner Tip, Phase 1f)."""
    if not quiz:
        return ""
    cp = set(checkpoint_qidxs or [])
    remaining = [(i, q) for i, q in enumerate(quiz) if i not in cp]
    total = len(remaining)
    chunk_defs = [("Warm-up", 0, 4), ("Exam standard", 4, 8), ("Stretch", 8, len(quiz))]
    parts = []
    first_emitted = False
    for name, lo, hi in chunk_defs:
        qs = [(i, q) for i, q in remaining if lo <= i < hi]
        if not qs:
            continue
        cards = ""
        for i, q in qs:
            cards += f"""<div class="quiz-card">
  <div class="q-text">{q['q']}</div>
  <div class="quiz-options">{_rd_quiz_options(q)}</div>
  <div class="quiz-fb"></div>
</div>"""
        n_lbl = f"{name} · {len(qs)} question{'s' if len(qs) != 1 else ''}"
        check = '<div class="rd-exam__check-row"><button class="quiz-check-btn" type="button" data-chunk-check>✓ Check this set</button></div>'
        if not first_emitted:
            # first chunk open, with its own heading
            parts.append(f"""<section class="rd-exam__chunk" data-chunk="{name}">
      <div class="rd-exam__chunk-hd">{n_lbl}</div>
      {cards}
      {check}
    </section>""")
            first_emitted = True
        else:
            # later chunks behind <details> (summary carries the heading)
            parts.append(f"""<details class="rd-exam__details"><summary>{n_lbl}</summary>
      <section class="rd-exam__chunk" data-chunk="{name}">
      {cards}
      {check}
      </section>
    </details>""")
    chunks_html = "\n    ".join(parts)
    return f"""<div class="section" id="rd-test">
  <div class="rd-sec-kicker">Test yourself · {total} questions, exam order</div>{pre_html}
  <div class="rd-exam" data-st="{st_id}">
    <div class="rd-exam__chip">0 of {total} answered</div>
    {chunks_html}
    <div class="rd-exam__end" style="display:none;"></div>
    <div class="rd-exam__actions">
      <button class="quiz-check-btn" type="button" data-retry-misses style="display:none;">↻ Retry my misses</button>
      <button class="quiz-again-btn" type="button" data-start-over style="display:none;">Start over</button>
    </div>
  </div>
</div>"""


# Star-rating feedback for redesigned pages (MRB-133 Phase 1g): every rating
# answers with a ROUTE, not a congratulation. No exclamation stacking, no
# emoji. Non-redesigned pages keep STAR_MESSAGES unchanged.
RD_STAR_MESSAGES = [
    "Start with Teach me above — one block at a time, checkpoint after each. The AI chat can explain anything from scratch.",
    "Re-read the theory blocks that felt hardest, then run the matching activity to lock in the basics.",
    "Halfway there. Run the interactive again, then take the quiz — the misses will show you exactly what to revise.",
    "Nearly solid. Take the quiz and retry your misses — the last gap is usually one idea.",
    "If the quiz agrees — near full marks below — you're done here. Move on to the next page.",
]


def make_new_quiz(quiz, color, pilot=False):
    import random
    if not quiz:
        return ""
    if pilot:
        return make_pilot_quiz(quiz)
    cards_html = ""
    for i, q in enumerate(quiz):
        # Shuffle options so correct answer isn't always option A.
        # Seeded from the question content so regeneration is deterministic
        # (kills the shuffle churn); editing a question naturally reshuffles it.
        opts = list(enumerate(q["opts"]))  # [(original_idx, (text, is_correct)), ...]
        random.Random("quiz:%d:%r" % (i, q["opts"])).shuffle(opts)

        opts_html = ""
        correct_display_idx = None  # position after shuffle
        wrong_exp_map = {}          # display_idx → explanation
        orig_wrong_exp = q.get("wrong_explanations", {})

        for display_j, (orig_j, (opt_text, is_correct)) in enumerate(opts):
            if is_correct:
                correct_display_idx = display_j
            else:
                # Map original wrong explanation index to new display position
                if orig_j in orig_wrong_exp:
                    wrong_exp_map[display_j] = orig_wrong_exp[orig_j]
            opts_html += f'<button class="quiz-opt" data-qi="{i}" data-oi="{display_j}">{opt_text}</button>\n'

        wrong_exp_js = "{"
        for idx, explanation in wrong_exp_map.items():
            safe = explanation.replace("\\", "\\\\").replace('"', '\\"').replace("'", "\\'")
            wrong_exp_js += f'{idx}: "{safe}",'
        wrong_exp_js += "}"

        cards_html += f"""<div class="quiz-card" id="qcard-{i}" data-answer="{correct_display_idx}" data-wrong-exp='{wrong_exp_js}'>
  <div class="q-text">{i+1}. {q['q']}</div>
  <div class="quiz-options">{opts_html}</div>
  <div class="quiz-fb" id="qfb-{i}"></div>
</div>"""

    return f"""<div class="section">
  <div class="section-title">🎯 Test Yourself</div>
  <div class="quiz-progress" id="quizProgress">Question 1 of {len(quiz)}</div>
  {cards_html}
  <div class="quiz-end-msg" id="quizEndMsg" style="display:none;margin-top:16px;padding:16px 20px;border-radius:12px;font-size:0.95rem;font-weight:700;text-align:center;"></div>
</div>"""


def make_star_rating(st_id):
    return f"""<div class="section">
  <div class="section-title">⭐ How Well Do You Understand This Topic?</div>
  <div class="card star-rating-card">
    <p style="font-size:0.95rem;color:var(--muted);margin-bottom:16px;">Be honest with yourself — this helps you know what to revise!</p>
    <div class="stars-row" id="stars-{st_id}">
      <button class="star-btn" data-rating="1" onclick="rateTopic('{st_id}', 1)" title="I don't understand this at all">⭐</button>
      <button class="star-btn" data-rating="2" onclick="rateTopic('{st_id}', 2)" title="I understand a little">⭐</button>
      <button class="star-btn" data-rating="3" onclick="rateTopic('{st_id}', 3)" title="I understand about half of it">⭐</button>
      <button class="star-btn" data-rating="4" onclick="rateTopic('{st_id}', 4)" title="I mostly understand it">⭐</button>
      <button class="star-btn" data-rating="5" onclick="rateTopic('{st_id}', 5)" title="I understand it perfectly">⭐</button>
    </div>
    <div class="star-labels">
      <span>Don't get it</span>
      <span>Getting there</span>
      <span>Nailed it!</span>
    </div>
    <div class="star-feedback" id="starfb-{st_id}"></div>
  </div>
</div>"""


STAR_MESSAGES = [
    "No worries — that's what Mr Badmus AI is here for! Hit the chat button below and ask me to explain it from scratch. 💬",
    "Good start! Read through the theory again, then try the quiz once more. You'll get there! 📖",
    "Solid — you're getting there! Try explaining it out loud to yourself. If you can say it, you know it. 🗣️",
    "Great work! Just review the parts you found tricky and you'll be flying. 🚀",
    "PERFECT! You've nailed this topic. Move on — you're ready! 🏆"
]


def make_new_subtopic_page(st, color):
    """Generate a full dedicated subtopic page with all corrections applied."""
    st_id = st["id"]

    # Theory sections — short paragraphs
    theory_html = ""
    for section in st["theory"]:
        # Split content by \n for short lines
        lines = section["content"].split("\n")
        lines_html = ""
        for line in lines:
            if line.strip():
                lines_html += f"<div class='theory-line'>{line}</div>"
            else:
                lines_html += "<div class='theory-gap'></div>"
        theory_html += f"""<div class="card" style="margin-bottom:14px;">
  <h4 style="margin-bottom:10px;font-size:1rem;">{section['heading']}</h4>
  {lines_html}
</div>"""

    # Variables
    var_html = ""
    if st.get("variables"):
        var_html = f"""<div class="section">
  <div class="section-title">📐 Variables</div>
  <div class="card">{make_variable_rows(st['variables'])}</div>
</div>"""

    # Equations
    eq_html = ""
    if st.get("equations"):
        pills = "".join(f'<div class="formula-pill">{eq}</div>' for eq in st["equations"])
        eq_html = f"""<div class="section">
  <div class="section-title">📐 Key Equations</div>
  <div class="formula-grid">{pills}</div>
</div>"""

    # Key note
    keynote_html = ""
    if st.get("key_note"):
        keynote_html = f"""<div class="section">
  <div class="section-title">📌 Key Note</div>
  <div class="keynote-box"><p>{st['key_note']}</p></div>
</div>"""

    # Common mistake
    mistake_html = ""
    if st.get("common_mistake"):
        mistake_html = f"""<div class="mistake-box">
  <div class="mistake-title">⚠️ Common Mistake</div>
  <p style="font-size:0.9rem;line-height:1.7;">{st['common_mistake']}</p>
</div>"""

    # Examiner tip — one exam-technique pointer per page (site-wide field).
    # Leading newline lets it piggyback onto the keynote line (see body) so pages
    # without a tip stay byte-identical.
    examiner_html = ""
    if st.get("examiner_tip"):
        examiner_html = f"""
  <div class="section">
  <div class="section-title">⭐ Examiner Tip</div>
  <div class="examiner-box"><p>{st['examiner_tip']}</p></div>
</div>"""

    # Higher box
    higher_html = ""
    if st.get("higher"):
        higher_html = f"""<div class="section">
  <div class="section-title">⭐ Higher Tier Only</div>
  <div class="higher-box"><p>{st['higher']}</p></div>
</div>"""

    # Triple only
    triple_html = ""
    if st.get("triple_only"):
        triple_html = f"""<div class="section">
  <div class="section-title">🔬 Triple Science Only</div>
  <div class="triple-box"><p>{st['triple_only']}</p></div>
</div>"""

    # RP box
    rp_html = ""
    if st.get("rp"):
        rp_html = f"""<div class="section">
  <div class="section-title">🧪 Required Practical</div>
  <div class="rp-card"><h4>🔬 {st['rp']}</h4>
  <p style="font-size:0.88rem;color:var(--muted);margin-top:6px;">Know the method, variables, equipment and how to analyse results.</p>
  </div>
</div>"""

    # Matching widget
    matching_html = make_matching_widget(st.get("matching"), st_id, color)

    # FIFA boxes
    fifa_html = make_fifa_boxes(st.get("fifas", []))

    # Quiz
    quiz_html = make_new_quiz(st.get("quiz", []), color)

    # Star rating
    star_html = make_star_rating(st_id)

    # AI chat section
    chat_section = f"""<div class="section">
  <div class="section-title">🤖 Ask Mr Badmus AI</div>
  <div class="card" style="text-align:center;padding:32px;">
    <p style="font-size:1.1rem;margin-bottom:8px;font-weight:700;">Stuck? Just ask! 💬</p>
    <p style="color:var(--muted);font-size:0.9rem;margin-bottom:20px;">I'll use FIFA for all calculations and flag Higher Tier and Triple content clearly.</p>
    <button data-open-chat style="background:{color};color:#0F0F1A;border:none;padding:14px 32px;border-radius:50px;font-size:1rem;font-weight:800;cursor:pointer;font-family:'Plus Jakarta Sans',sans-serif;">💬 Ask Mr Badmus AI</button>
  </div>
</div>"""

    import json as _json
    star_msgs_js = _json.dumps(STAR_MESSAGES)

    quiz_js = """
document.querySelectorAll('.quiz-opt').forEach(btn => {
  btn.addEventListener('click', function() {
    const card = this.closest('.quiz-card');
    if (card.dataset.answered) return;
    card.dataset.answered = '1';
    const correctIdx = parseInt(card.dataset.answer);
    const clickedIdx = parseInt(this.dataset.oi);
    const isCorrect = clickedIdx === correctIdx;
    const fb = document.getElementById('qfb-' + this.dataset.qi);

    // Mark options
    card.querySelectorAll('.quiz-opt').forEach((o, idx) => {
      if (idx === correctIdx) o.classList.add('correct');
      else if (o === this && !isCorrect) o.classList.add('wrong');
    });

    // Feedback
    if (isCorrect) {
      fb.className = 'quiz-fb correct-fb show';
      fb.innerHTML = '✅ Correct! Well done!';
    } else {
      const wrongExp = card.dataset.wrongExp ? JSON.parse(card.dataset.wrongExp.replace(/'/g, '"')) : {};
      const explanation = wrongExp[clickedIdx] || 'Look at the correct answer highlighted above.';
      fb.className = 'quiz-fb wrong-fb show';
      fb.innerHTML = '❌ Incorrect. ' + explanation;
    }

    // Update progress
    const answered = document.querySelectorAll('.quiz-card[data-answered]').length;
    const total = document.querySelectorAll('.quiz-card').length;
    const prog = document.getElementById('quizProgress');
    if (prog) {
      if (answered === total) {
        const correct = document.querySelectorAll('.quiz-opt.correct').length;
        prog.innerHTML = '🎉 Finished! You got ' + answered + '/' + total + ' questions answered.';
        prog.style.background = 'rgba(78,205,196,0.15)';
      } else {
        prog.innerHTML = 'Question ' + (answered + 1) + ' of ' + total;
      }
    }
  });
});
"""

    matching_js = f"""
function checkMatching(stId, pairs) {{
  const targets = document.querySelectorAll('.match-target');
  let correct = 0;
  targets.forEach(target => {{
    const drop = target.querySelector('.match-drop');
    const accepts = parseInt(target.querySelector('.match-drop').dataset.accepts);
    const placed = drop.querySelector('.match-def');
    if (placed && parseInt(placed.dataset.index) === accepts) {{
      drop.classList.add('match-correct');
      drop.classList.remove('match-wrong');
      correct++;
    }} else if (placed) {{
      drop.classList.add('match-wrong');
      drop.classList.remove('match-correct');
    }}
  }});
  const result = document.getElementById('matchResult-' + stId);
  const total = pairs.length;
  if (correct === total) {{
    result.innerHTML = '🎉 Perfect! All ' + total + ' matched correctly!';
    result.className = 'match-result match-result-win';
  }} else {{
    result.innerHTML = correct + '/' + total + ' correct — keep trying! Wrong answers are highlighted in red.';
    result.className = 'match-result match-result-partial';
  }}
}}

function resetMatching(stId, pairs) {{
  const pool = document.getElementById('defPool-' + stId);
  const drops = document.querySelectorAll('.match-drop');
  drops.forEach(drop => {{
    const placed = drop.querySelector('.match-def');
    if (placed) {{
      pool.appendChild(placed);
    }}
    drop.innerHTML = 'Drop here';
    drop.classList.remove('match-correct', 'match-wrong', 'has-item');
  }});
  const result = document.getElementById('matchResult-' + stId);
  if (result) {{ result.innerHTML = ''; result.className = 'match-result'; }}
}}

// Drag and drop
document.querySelectorAll('.match-def').forEach(def => {{
  def.addEventListener('dragstart', e => {{
    e.dataTransfer.setData('text/plain', def.dataset.index);
    def.classList.add('dragging');
  }});
  def.addEventListener('dragend', () => def.classList.remove('dragging'));
}});

document.querySelectorAll('.match-drop').forEach(drop => {{
  drop.addEventListener('dragover', e => {{ e.preventDefault(); drop.classList.add('drag-over'); }});
  drop.addEventListener('dragleave', () => drop.classList.remove('drag-over'));
  drop.addEventListener('drop', e => {{
    e.preventDefault();
    drop.classList.remove('drag-over');
    const idx = e.dataTransfer.getData('text/plain');
    const def = document.querySelector('.match-def[data-index="' + idx + '"]');
    if (!def) return;
    // Return existing item to pool if occupied
    const existing = drop.querySelector('.match-def');
    if (existing) {{
      const pool = document.getElementById('defPool-{st_id}');
      pool.appendChild(existing);
    }}
    drop.innerHTML = '';
    drop.appendChild(def);
    drop.classList.add('has-item');
    drop.classList.remove('match-correct', 'match-wrong');
  }});
}});
"""

    star_js = f"""
const STAR_MESSAGES_{st_id.replace('-','_')} = {star_msgs_js};
function rateTopic(stId, rating) {{
  const stars = document.querySelectorAll('#stars-' + stId + ' .star-btn');
  stars.forEach((s, i) => {{
    s.classList.toggle('star-active', i < rating);
  }});
  const fb = document.getElementById('starfb-' + stId);
  fb.innerHTML = STAR_MESSAGES_{st_id.replace('-','_')}[rating - 1];
  fb.style.display = 'block';
  // Save to localStorage
  try {{ localStorage.setItem('star_' + stId, rating); }} catch(e) {{}}
}}
// Load saved rating
try {{
  const saved = localStorage.getItem('star_{st_id}');
  if (saved) rateTopic('{st_id}', parseInt(saved));
}} catch(e) {{}}
"""

    body = f"""
<div class="topic-header">
  <a class="back-link" href="/physics/electricity.html">← Back to Electricity</a>
  <h1 style="color:{color}">⚡ {st['title']}</h1>
  <span class="spec-pill">Spec {st['spec']}</span>
  <span class="paper-pill">Paper 1</span>
</div>

<div class="content-area">

  <div class="section">
    <div class="section-title">📖 In-Depth Theory</div>
    {theory_html}
    {mistake_html}
  </div>

  {var_html}
  {eq_html}
  {keynote_html}{examiner_html}
  {matching_html}
  {fifa_html}
  {higher_html}
  {triple_html}
  {rp_html}
  {quiz_html}
  {star_html}
  {chat_section}

</div>"""

    extra_css = f"""
<style>
html {{ background: #0F0F1A; }}
:root {{ --subject: {color}; }}
.section-title {{ color: var(--subject); }}

/* Variables */
.var-table {{ display:flex;flex-direction:column;gap:8px; }}
.var-row {{ display:flex;align-items:center;gap:16px;padding:10px 16px;background:rgba(255,255,255,0.03);border-radius:8px;border-left:3px solid {color}; }}
.var-sym {{ font-family:'Courier New',monospace;font-size:1.1rem;font-weight:700;color:{color};min-width:28px; }}
.var-desc {{ font-size:0.9rem;color:var(--text); }}

/* Common mistake */
.mistake-box {{ background:rgba(255,100,50,0.08);border:1px solid rgba(255,100,50,0.3);border-left:4px solid #FF6435;border-radius:10px;padding:16px 20px;margin-top:16px; }}
.mistake-title {{ color:#FF6435;font-weight:800;font-size:0.95rem;margin-bottom:8px; }}

/* Key note */
.keynote-box {{ background:rgba(255,217,61,0.08);border:1px solid rgba(255,217,61,0.3);border-left:4px solid #FFD93D;border-radius:10px;padding:16px 20px; }}
.keynote-box p {{ font-size:0.9rem;color:#FFD93D;font-weight:600; }}

/* FIFA label */
.fifa-label {{ font-size:0.8rem;font-weight:700;color:{color};text-transform:uppercase;letter-spacing:1px;margin-bottom:8px; }}

/* Matching */
.match-layout {{ display:flex;gap:16px;flex-wrap:wrap; }}
.match-targets {{ flex:1;min-width:220px;display:flex;flex-direction:column;gap:8px; }}
.match-defs {{ flex:1;min-width:220px;display:flex;flex-direction:column;gap:8px; }}
.match-target {{ display:flex;flex-direction:column;gap:4px; }}
.match-term {{ font-weight:700;font-size:0.88rem;color:{color};padding:4px 0; }}
.match-drop {{ background:rgba(255,255,255,0.04);border:2px dashed rgba(255,255,255,0.15);border-radius:8px;padding:10px 14px;font-size:0.85rem;color:var(--muted);min-height:42px;transition:all 0.15s; }}
.match-drop.drag-over {{ border-color:{color};background:rgba(78,205,196,0.1); }}
.match-drop.has-item {{ border-style:solid;border-color:rgba(255,255,255,0.2);color:var(--text); }}
.match-drop.match-correct {{ border-color:#6BCB77;background:rgba(107,203,119,0.1); }}
.match-drop.match-wrong {{ border-color:#FF6B6B;background:rgba(255,107,107,0.1); }}
.match-def {{ background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:10px 14px;font-size:0.85rem;cursor:grab;transition:all 0.15s; }}
.match-def:hover {{ background:rgba(255,255,255,0.1);border-color:{color}; }}
.match-def.dragging {{ opacity:0.5; }}
.match-check-btn,.match-reset-btn {{ border:none;padding:10px 20px;border-radius:8px;cursor:pointer;font-weight:700;font-size:0.88rem;font-family:'Plus Jakarta Sans',sans-serif; }}
.match-check-btn {{ background:{color};color:#0F0F1A; }}
.match-reset-btn {{ background:rgba(255,255,255,0.08);color:var(--text); }}
.match-result {{ margin-top:12px;font-weight:700;font-size:0.9rem;padding:10px 16px;border-radius:8px;display:none; }}
.match-result-win {{ background:rgba(107,203,119,0.15);color:#6BCB77;display:block; }}
.match-result-partial {{ background:rgba(255,107,107,0.1);color:#FF6B6B;display:block; }}

/* Quiz */
.quiz-progress {{ background:rgba(78,205,196,0.08);border:1px solid rgba(78,205,196,0.2);border-radius:8px;padding:10px 16px;font-size:0.88rem;color:{color};font-weight:700;margin-bottom:16px; }}
.quiz-fb {{ display:none;padding:12px 16px;border-radius:8px;font-size:0.88rem;font-weight:600;margin-top:10px;line-height:1.6; }}
.quiz-fb.show {{ display:block; }}
.quiz-fb.correct-fb {{ background:rgba(107,203,119,0.12);color:#6BCB77;border:1px solid rgba(107,203,119,0.3); }}
.quiz-fb.wrong-fb {{ background:rgba(255,107,107,0.1);color:#FF8080;border:1px solid rgba(255,107,107,0.3); }}

/* Stars */
.star-rating-card {{ text-align:center;padding:28px; }}
.stars-row {{ display:flex;justify-content:center;gap:8px;margin-bottom:8px; }}
.star-btn {{ background:none;border:none;font-size:2rem;cursor:pointer;transition:transform 0.15s;filter:grayscale(1);opacity:0.4; }}
.star-btn:hover,.star-btn.star-active {{ filter:grayscale(0);opacity:1;transform:scale(1.2); }}
.star-labels {{ display:flex;justify-content:space-between;font-size:0.75rem;color:var(--muted);margin-bottom:12px;padding:0 8px; }}
.star-feedback {{ display:none;margin-top:12px;padding:12px 16px;background:rgba(255,217,61,0.08);border:1px solid rgba(255,217,61,0.2);border-radius:8px;font-size:0.9rem;color:#FFD93D;font-weight:600; }}
</style>"""

    nav = nav_html("physics")
    chat = chat_html()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="theme-color" content="#0F0F1A"/>
  <title>{st['title']} | Electricity | Physics | MrBadmusAI</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
  <link rel="stylesheet" href="/shared/nav.css"/>
  <script src="/shared/nav.js" defer></script>
  <script src="/shared/class-entry.js" defer></script>
  {extra_css}
</head>
<body>
  {nav}
  {body}
  {chat}
  <script src="/shared/mrbadmus.v2.js"></script>
  <script>
    MrBadmus.init({{ subject: 'physics', topic: '{st['title']} (AQA {st['spec']})' }});
  </script>
  <script>
  {quiz_js}
  {matching_js}
  {star_js}
  </script>
</body>
</html>"""

def make_updated_electricity_page():
    """Electricity topic hub with expand/link subtopic rows."""
    color = PHYSICS_COLOR
    subtopic_rows = ""
    for st in ELECTRICITY_SUBTOPICS:
        theory_preview = st["theory"][0]["content"].split("\n")[0] if st["theory"] else ""
        eq_pills = "".join(f'<span class="formula-pill" style="font-size:0.8rem;padding:6px 12px;">{eq}</span>' for eq in st.get("equations", [])) if st.get("equations") else ""
        badges = ""
        if st.get("higher"): badges += '<span class="badge badge-h">⭐ Higher</span>'
        if st.get("triple_only"): badges += '<span class="badge badge-t">🔬 Triple</span>'
        if st.get("rp"): badges += '<span class="badge badge-rp">📋 RP</span>'
        if st.get("matching"): badges += '<span class="badge" style="background:rgba(255,217,61,0.15);color:#FFD93D;border-color:rgba(255,217,61,0.3);">🎯 Matching</span>'

        subtopic_rows += f"""
<div class="subtopic-row" id="row-{st['id']}">
  <div class="subtopic-main">
    <a href="/physics/electricity/{st['id']}.html" class="subtopic-link">
      <span style="color:{color};margin-right:8px;">●</span>
      <span class="subtopic-title">{st['title']}</span>
      <span style="font-size:0.75rem;color:var(--muted);margin-left:8px;">{st['spec']}</span>
      {badges}
    </a>
    <button class="expand-btn" onclick="toggleExpand('{st['id']}')" title="Preview">+</button>
  </div>
  <div class="subtopic-expand" id="expand-{st['id']}">
    <p style="font-size:0.88rem;line-height:1.7;margin-bottom:12px;">{theory_preview}</p>
    {"<div class='formula-grid' style='margin-bottom:12px;'>" + eq_pills + "</div>" if eq_pills else ""}
    <a href="/physics/electricity/{st['id']}.html" class="expand-full-link" style="color:{color};font-weight:700;font-size:0.88rem;">📖 Full notes, examples &amp; quiz →</a>
  </div>
</div>"""

    extra_css = f"""<style>
html {{ background: #0F0F1A; }}
:root {{ --subject: {color}; }}
.section-title {{ color: var(--subject); }}
.subtopic-list-new {{ display:flex;flex-direction:column; }}
.subtopic-row {{ border-bottom:1px solid rgba(255,255,255,0.06); }}
.subtopic-row:last-child {{ border-bottom:none; }}
.subtopic-main {{ display:flex;align-items:center;justify-content:space-between;padding:14px 20px;transition:background 0.15s; }}
.subtopic-main:hover {{ background:rgba(255,255,255,0.03); }}
.subtopic-link {{ display:flex;align-items:center;gap:6px;flex:1;text-decoration:none;color:var(--text);font-size:0.95rem;font-weight:600;transition:color 0.15s; }}
.subtopic-link:hover .subtopic-title {{ color:{color};text-decoration:underline; }}
.expand-btn {{ background:rgba(78,205,196,0.15);border:1px solid rgba(78,205,196,0.3);color:{color};width:28px;height:28px;border-radius:6px;cursor:pointer;font-size:1.2rem;font-weight:700;display:flex;align-items:center;justify-content:center;transition:all 0.2s;flex-shrink:0;margin-left:12px; }}
.expand-btn.open {{ transform:rotate(45deg); }}
.subtopic-expand {{ display:none;padding:0 20px 16px 36px;border-top:1px solid rgba(255,255,255,0.05);background:rgba(0,0,0,0.15); }}
.subtopic-expand.open {{ display:block; }}
.expand-full-link {{ display:inline-block;margin-top:10px;padding:8px 18px;background:rgba(78,205,196,0.1);border:1px solid rgba(78,205,196,0.3);border-radius:8px; }}
</style>"""

    body = f"""
<div class="topic-header">
  <a class="back-link" href="/physics/index.html">← Back to Physics</a>
  <h1 style="color:{color}">⚡ Electricity</h1>
  <span class="spec-pill">Spec 4.2</span><span class="paper-pill">Paper 1</span>
</div>
<div class="content-area">
  <div class="section">
    <div class="section-title">📋 What You Need to Know</div>
    <div class="card" style="padding:0;overflow:hidden;">
      <div class="subtopic-list-new">{subtopic_rows}</div>
    </div>
    <p style="font-size:0.82rem;color:var(--muted);margin-top:10px;">💡 Click a topic title to open the full notes page, or press <strong>+</strong> to preview it here.</p>
  </div>
  <div class="section">
    <div class="section-title">📐 Key Equations</div>
    <div class="formula-grid">
      <div class="formula-pill">Q = It</div><div class="formula-pill">V = IR</div>
      <div class="formula-pill">P = VI</div><div class="formula-pill">P = I²R</div>
      <div class="formula-pill">E = Pt</div><div class="formula-pill">E = QV</div>
    </div>
  </div>
  <div class="section">
    <div class="section-title">🤖 Ask Mr Badmus AI</div>
    <div class="card" style="text-align:center;padding:32px;">
      <p style="font-size:1.1rem;margin-bottom:16px;font-weight:700;">Got a question about Electricity? 💬</p>
      <button data-open-chat style="background:{color};color:#0F0F1A;border:none;padding:14px 32px;border-radius:50px;font-size:1rem;font-weight:800;cursor:pointer;font-family:'Plus Jakarta Sans',sans-serif;">💬 Ask Mr Badmus AI</button>
    </div>
  </div>
</div>"""

    nav = nav_html("physics")
    chat = chat_html()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <meta name="theme-color" content="#0F0F1A"/>
  <title>Electricity | Physics | MrBadmusAI</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
  <link rel="stylesheet" href="/shared/nav.css"/>
  <script src="/shared/nav.js" defer></script>
  <script src="/shared/class-entry.js" defer></script>
  {extra_css}
</head>
<body>
  {nav}
  {body}
  {chat}
  <script src="/shared/mrbadmus.v2.js"></script>
  <script>MrBadmus.init({{subject:'physics',topic:'Electricity (AQA 4.2)'}});</script>
  <script>
  function toggleExpand(id) {{
    const expand = document.getElementById('expand-' + id);
    const btn = document.getElementById('row-' + id).querySelector('.expand-btn');
    const isOpen = expand.classList.contains('open');
    document.querySelectorAll('.subtopic-expand.open').forEach(el => el.classList.remove('open'));
    document.querySelectorAll('.expand-btn.open').forEach(el => el.classList.remove('open'));
    if (!isOpen) {{ expand.classList.add('open'); btn.classList.add('open'); }}
  }}
  </script>
</body>
</html>"""



# ─────────────────────────────────────────────
#  PATHWAY-AWARE SUBTOPIC PAGE
#  Wraps make_new_subtopic_page with correct
#  back links and next/prev navigation
# ─────────────────────────────────────────────

def make_pathway_subtopic_page(st, color, subject, pathway, tier, all_subtopics_for_topic, topic_id, topic_title):
    """
    Generates a full subtopic page with:
    - Correct back link → /{pathway}/{tier}/{subject}/{topic_id}.html
    - Next/Prev navigation across subtopics in this topic
    - All existing content (theory, quiz, FIFA, matching, star rating)
    """
    import json as _json
    st_id = st["id"]

    # Find prev/next within this topic's subtopic list
    st_idx = next((i for i, s in enumerate(all_subtopics_for_topic) if s["id"] == st_id), None)
    nav_prev = nav_next = ""
    if st_idx is not None:
        if st_idx > 0:
            prev_s = all_subtopics_for_topic[st_idx - 1]
            nav_prev = f'<a class="nav-arrow prev" href="/{pathway}/{tier}/{subject}/{topic_id}/{prev_s["id"]}.html"><span><div class="nav-arrow-label">Previous</div><div class="nav-arrow-title">{prev_s["title"]}</div></span></a>'
        else:
            nav_prev = '<span></span>'
        if st_idx < len(all_subtopics_for_topic) - 1:
            next_s = all_subtopics_for_topic[st_idx + 1]
            nav_next = f'<a class="nav-arrow next" href="/{pathway}/{tier}/{subject}/{topic_id}/{next_s["id"]}.html"><span><div class="nav-arrow-label">Next</div><div class="nav-arrow-title">{next_s["title"]}</div></span></a>'
        else:
            nav_next = '<span></span>'

    subtopic_nav_html = f"""<div class="subtopic-nav">
  {nav_prev}
  <a href="/{pathway}/{tier}/{subject}/{topic_id}.html" style="font-size:0.8rem;color:var(--muted);text-decoration:none;">📋 All {topic_title} subtopics</a>
  {nav_next}
</div>"""

    # Theory sections
    theory_html = ""
    for section in st["theory"]:
        lines = section["content"].split("\n")
        lines_html = ""
        for line in lines:
            if line.strip():
                lines_html += f"<div class='theory-line'>{line}</div>"
            else:
                lines_html += "<div class='theory-gap'></div>"
        theory_html += f"""<div class="card" style="margin-bottom:14px;">
  <h4 style="margin-bottom:10px;font-size:1rem;">{section['heading']}</h4>
  {lines_html}
</div>"""

    # Variables
    var_html = ""
    if st.get("variables"):
        var_html = f"""<div class="section">
  <div class="section-title">📐 Variables</div>
  <div class="card">{make_variable_rows(st['variables'])}</div>
</div>"""

    # Equations
    eq_html = ""
    if st.get("equations"):
        # Filter Higher equations for Foundation
        eqs = st["equations"]
        if tier == "foundation":
            eqs = [e for e in eqs if "(Higher)" not in e and "(higher)" not in e]
        if eqs:
            pills = "".join(f'<div class="formula-pill">{eq}</div>' for eq in eqs)
            eq_html = f"""<div class="section">
  <div class="section-title">📐 Key Equations</div>
  <div class="formula-grid">{pills}</div>
</div>"""

    # Key note
    keynote_html = ""
    if st.get("key_note"):
        keynote_html = f"""<div class="section">
  <div class="section-title">📌 Key Note</div>
  <div class="keynote-box"><p>{st['key_note']}</p></div>
</div>"""

    # Common mistake
    mistake_html = ""
    if st.get("common_mistake"):
        mistake_html = f"""<div class="mistake-box">
  <div class="mistake-title">⚠️ Common Mistake</div>
  <p style="font-size:0.9rem;line-height:1.7;">{st['common_mistake']}</p>
</div>"""

    # Examiner tip — one exam-technique pointer per page (site-wide field).
    # Non-redesigned pages render it as a flat amber callout; .rd pages override
    # this below with the canonical examiner-tip block. The leading newline lets
    # it piggyback onto the keynote line in the body, so pages WITHOUT a tip stay
    # byte-identical (an empty examiner_html appends nothing).
    examiner_html = ""
    if st.get("examiner_tip"):
        examiner_html = f"""
  <div class="section">
  <div class="section-title">⭐ Examiner Tip</div>
  <div class="examiner-box"><p>{st['examiner_tip']}</p></div>
</div>"""

    # 3D Studio link — an optional way into /3d/ from the pages whose specimen
    # the studio holds. Scoped by DATA, not by slug: a page gets the link when
    # its subtopic entry carries `studio_url`, and nothing at all when it does
    # not, so there is no page list in the template to keep in sync. Optional
    # `studio_label` carries the copy that names the specimen (the default is
    # deliberately specimen-neutral). Same leading-newline trick as the
    # examiner tip above — it piggybacks onto the keynote line in the body, so
    # every page without the field stays byte-identical.
    studio_html = ""
    if st.get("studio_url"):
        studio_html = f"""
  <div class="section">
  <div class="section-title">🧊 3D Studio</div>
  <div class="card">
    <a class="btn-primary" href="{st['studio_url']}">{st.get('studio_label', 'Explore in 3D')}</a>
  </div>
</div>"""

    # Higher box — only on higher tier
    higher_html = ""
    if tier == "higher" and st.get("higher"):
        higher_html = f"""<div class="section">
  <div class="section-title">⭐ Higher Tier Only</div>
  <div class="higher-box"><p>{st['higher']}</p></div>
</div>"""

    # Triple only box — only on triple pathway
    triple_html = ""
    if pathway == "triple" and st.get("triple_only"):
        triple_html = f"""<div class="section">
  <div class="section-title">🔬 Triple Science Only</div>
  <div class="triple-box"><p>{st['triple_only']}</p></div>
</div>"""

    # RP box
    rp_html = ""
    if st.get("rp"):
        rp_html = f"""<div class="section">
  <div class="section-title">🧪 Required Practical</div>
  <div class="rp-card"><h4>🔬 {st['rp']}</h4>
  <p style="font-size:0.88rem;color:var(--muted);margin-top:6px;">Know the method, variables, equipment and how to analyse results.</p>
  </div>
</div>"""

    matching_html = make_matching_widget(st.get("matching"), st_id, color)
    fifa_html_content = make_fifa_boxes(st.get("fifas", []))
    quiz_html = make_new_quiz(st.get("quiz", []), color)
    star_html = make_star_rating(st_id)

    chat_section = f"""<div class="section">
  <div class="section-title">🤖 Ask Mr Badmus AI</div>
  <div class="card ask-card">
    <p class="ask-lede">Stuck? Just ask! 💬</p>
    <p class="ask-sub">I'll use FIFA for calculations and flag Higher/Triple content clearly.</p>
    <button data-open-chat class="btn-primary">💬 Ask Mr Badmus AI</button>
  </div>
</div>"""

    star_msgs_js = _json.dumps(STAR_MESSAGES)

    quiz_js = """
const SCORE_MESSAGES = [
  "Keep going — re-read the theory and try again. You'll get there! 📖",
  "Not bad — review the sections you missed and have another go. 💪",
  "Decent effort! A bit more revision and you'll nail it. 🔄",
  "Good work! Just a couple of gaps to fill. Nearly there! 🌟",
  "Excellent! You've really got this topic down. 🏆",
];

document.querySelectorAll('.quiz-opt').forEach(btn => {
  btn.addEventListener('click', function() {
    const card = this.closest('.quiz-card');
    if (card.dataset.answered) return;
    const correctIdx = parseInt(card.dataset.answer);
    const clickedIdx = parseInt(this.dataset.oi);
    const isCorrect = clickedIdx === correctIdx;

    // Store whether student got THIS card right
    card.dataset.answered = isCorrect ? 'correct' : 'wrong';

    const fb = document.getElementById('qfb-' + this.dataset.qi);

    card.querySelectorAll('.quiz-opt').forEach((o, idx) => {
      if (idx === correctIdx) o.classList.add('correct');
      else if (o === this && !isCorrect) o.classList.add('wrong');
      o.disabled = true;
    });

    let wrongExp = {};
    try { wrongExp = JSON.parse(card.dataset.wrongExp || '{}'); } catch(e) {}

    if (isCorrect) {
      fb.className = 'quiz-fb correct-fb show';
      fb.innerHTML = '✅ Correct! Well done!';
    } else {
      const explanation = wrongExp[clickedIdx] || 'Look at the correct answer highlighted above.';
      fb.className = 'quiz-fb wrong-fb show';
      fb.innerHTML = '❌ Incorrect. ' + explanation;
    }

    const allCards = document.querySelectorAll('.quiz-card');
    const answeredCards = document.querySelectorAll('.quiz-card[data-answered]');
    const total = allCards.length;
    const answered = answeredCards.length;
    const prog = document.getElementById('quizProgress');

    if (answered === total) {
      // Count only cards where student clicked correct
      const correctCount = document.querySelectorAll('.quiz-card[data-answered="correct"]').length;
      if (prog) prog.innerHTML = '🎉 Finished! ' + correctCount + '/' + total + ' correct';

      const endMsg = document.getElementById('quizEndMsg');
      if (endMsg) {
        const ratio = correctCount / total;
        const msgIdx = ratio === 1 ? 4 : ratio >= 0.8 ? 3 : ratio >= 0.6 ? 2 : ratio >= 0.4 ? 1 : 0;
        endMsg.innerHTML = correctCount + '/' + total + ' — ' + SCORE_MESSAGES[msgIdx];
        endMsg.style.display = 'block';
        endMsg.style.background = ratio === 1 ? 'rgba(35,122,59,0.10)' : ratio >= 0.6 ? 'rgba(122,95,0,0.10)' : 'rgba(179,38,30,0.09)';
        endMsg.style.color = ratio === 1 ? '#237A3B' : ratio >= 0.6 ? '#7A5F00' : '#B3261E';
        endMsg.style.border = '1px solid ' + (ratio === 1 ? 'rgba(35,122,59,0.3)' : ratio >= 0.6 ? 'rgba(122,95,0,0.3)' : 'rgba(179,38,30,0.3)');
      }
    } else {
      if (prog) prog.innerHTML = 'Question ' + (answered + 1) + ' of ' + total;
    }
  });
});
"""

    matching_js = f"""
function checkMatching(stId, pairs) {{
  const targets = document.querySelectorAll('.match-target');
  let correct = 0;
  targets.forEach(target => {{
    const drop = target.querySelector('.match-drop');
    // Grade by category group (MRB-104): a slot is correct when the item in it
    // belongs to a row sharing this slot's term. For one-to-one matchings each
    // group holds exactly one item, so this is identical to an exact match.
    const acceptsGroup = drop.dataset.acceptsGroup;
    const placed = drop.querySelector('.match-def');
    if (placed && placed.dataset.group === acceptsGroup) {{
      drop.classList.add('match-correct'); drop.classList.remove('match-wrong'); correct++;
    }} else if (placed) {{
      drop.classList.add('match-wrong'); drop.classList.remove('match-correct');
    }}
  }});
  const result = document.getElementById('matchResult-' + stId);
  const total = pairs;
  if (correct === total) {{
    result.innerHTML = '🎉 Perfect! All ' + total + ' matched correctly!';
    result.className = 'match-result match-result-win';
  }} else {{
    result.innerHTML = correct + '/' + total + ' correct — keep trying!';
    result.className = 'match-result match-result-partial';
  }}
}}
function resetMatching(stId, pairs) {{
  const pool = document.getElementById('defPool-' + stId);
  document.querySelectorAll('.match-drop').forEach(drop => {{
    const placed = drop.querySelector('.match-def');
    if (placed) pool.appendChild(placed);
    drop.innerHTML = 'Drop here';
    drop.classList.remove('match-correct', 'match-wrong', 'has-item');
  }});
  const result = document.getElementById('matchResult-' + stId);
  if (result) {{ result.innerHTML = ''; result.className = 'match-result'; }}
}}
document.querySelectorAll('.match-def').forEach(def => {{
  def.addEventListener('dragstart', e => {{ e.dataTransfer.setData('text/plain', def.dataset.index); def.classList.add('dragging'); }});
  def.addEventListener('dragend', () => def.classList.remove('dragging'));
}});
document.querySelectorAll('.match-drop').forEach(drop => {{
  drop.addEventListener('dragover', e => {{ e.preventDefault(); drop.classList.add('drag-over'); }});
  drop.addEventListener('dragleave', () => drop.classList.remove('drag-over'));
  drop.addEventListener('drop', e => {{
    e.preventDefault(); drop.classList.remove('drag-over');
    const idx = e.dataTransfer.getData('text/plain');
    const def = document.querySelector('.match-def[data-index="' + idx + '"]');
    if (!def) return;
    const existing = drop.querySelector('.match-def');
    if (existing) document.getElementById('defPool-{st_id}').appendChild(existing);
    drop.innerHTML = ''; drop.appendChild(def);
    drop.classList.add('has-item'); drop.classList.remove('match-correct', 'match-wrong');
  }});
}});
"""

    star_js = f"""
const STAR_MESSAGES_{st_id.replace('-','_')} = {star_msgs_js};
function rateTopic(stId, rating) {{
  document.querySelectorAll('#stars-' + stId + ' .star-btn').forEach((s, i) => s.classList.toggle('star-active', i < rating));
  const fb = document.getElementById('starfb-' + stId);
  fb.innerHTML = STAR_MESSAGES_{st_id.replace('-','_')}[rating - 1];
  fb.style.display = 'block';
  try {{ localStorage.setItem('star_' + stId, rating); }} catch(e) {{}}
}}
try {{
  const saved = localStorage.getItem('star_{st_id}');
  if (saved) rateTopic('{st_id}', parseInt(saved));
}} catch(e) {{}}
"""

    tier_badge = '📗 Foundation' if tier == 'foundation' else '📙 Higher'
    subject_label = SITE_DATA[subject]["label"]
    subject_emoji = SITE_DATA[subject]["emoji"]
    paper_num = "1"  # default; could be looked up from topic data

    # ── Redesign hero slot (MRB-113 Phase B pilot) ──
    # Gated to the single sign-off page: giant-covalent-structures in the
    # bonding topic. `rd` on <body> opts the page into the Locked Tokens
    # (see shared/tokens.css). Every OTHER page keeps body_class="" and is
    # byte-identical to before — nothing else on the site is touched.
    body_class = ""
    hero_html = ""
    hero_scripts = ""
    redesign_css = ""
    # ── Exemplar (giant-covalent-structures) retrofitted onto the block system:
    #    it is now a normal BONDING_REDESIGN entry (Two-State hero + bins + block
    #    theory), so it flows through the single data-driven branch below. Its
    #    In-Depth Theory moves from old `.theory-line` prose to the block library;
    #    hero, bins, quiz, tip and Common Mistake are unchanged (MRB-113 Phase D2).
    if topic_id == "bonding" and st_id in BONDING_REDESIGN:
        # ── Bonding redesign — data-driven (MRB-113 Phase B, Path B) ──
        # One branch for every ported bonding page. The rcfg declares:
        #   hero     : None | {module, ns, config_key[, kicker]} | {module, ns, build:'fifa'}
        #   activity : {type:'bins', config_key} | {type:'match'}
        #   theory_blocks : the Theory Block Library decomposition.
        # Same `.rd` opt-in + reveal-quiz as the exemplar. The In-Depth Theory is
        # rebuilt from blocks (bonding_redesign.py); the static Common-Mistake box
        # is suppressed ONLY when a mistake-check block carries the misconception
        # (hero pages + compare-reveal pages keep the static box). Frozen source
        # fields are untouched — block content is authored presentation. Every
        # non-listed page keeps body_class="" and is byte-identical to before.
        rcfg = BONDING_REDESIGN[st_id]
        body_class = "rd"
        # Phase 0d (MRB-132): the quiz engine is no longer inlined per page —
        # it ships once as /shared/quiz.js and the generator emits a script tag.
        quiz_js = ""

        # ── Phase 1f (MRB-133): Examiner Tip placement split. Text is frozen
        # (approved tips); only WHERE it renders changes. 'quiz' → directly
        # above the quiz panel; 'activity' → the retrieval activity's success
        # state (successTip in the TapMatch/bins config).
        _tip_text = st.get("examiner_tip")
        _tip_mode = rcfg.get("tip_placement", "quiz")

        # ── Phase 1c (MRB-133): checkpoint micro-quizzes — 2–3 frozen recall
        # questions RELOCATED inline after the theory block they test. The
        # exam panel renders the remaining questions.
        _cps = rcfg.get("checkpoints", [])
        _cp_idxs = [c["q"] for c in _cps]
        _quiz = st.get("quiz", [])
        _theory_inserts = {}
        for _n, _c in enumerate(_cps):
            if _c["q"] < len(_quiz):
                _theory_inserts.setdefault(_c["after"], []).append(
                    make_rd_checkpoint(_quiz[_c["q"]], st_id, _n))

        # ── Phase 1f: Common Mistake moves to the moment the error is born.
        # mistake_after: 'hero' → directly under the hero slot; int → after
        # that theory block; None → end of the theory section (unchanged).
        # Pages whose misconception lives in a mistake-check block suppress
        # the static box entirely (as before).
        _mistake_target = rcfg.get("mistake_after")
        if any(b.get("type") == "mistake-check" for b in rcfg["theory_blocks"]):
            mistake_html = ""
            _mistake_target = None
        elif isinstance(_mistake_target, int):
            _theory_inserts.setdefault(_mistake_target, []).append(mistake_html)
            mistake_html = ""

        theory_html, _rd_interactive = render_theory_blocks(
            rcfg["theory_blocks"], st_id, inserts=_theory_inserts)

        # Exam-paper quiz (Phase 1c) with the technique tip above it (Phase 1f)
        _pre_quiz = ""
        if _tip_text and _tip_mode == "quiz":
            _pre_quiz = f"\n  {render_examiner_tip(_tip_text)}"
        quiz_html = make_rd_quiz(_quiz, st_id, _cp_idxs, pre_html=_pre_quiz)

        # Phase 1f: drop static blocks an interactive already teaches
        if rcfg.get("suppress_fifa_boxes"):
            fifa_html_content = ""

        _scripts = []          # hero module src paths (/shared/heroes/), in load order
        # shared root scripts (/shared/): quiz engine (0d), page chrome (1d);
        # predict-wrapper (1a) is appended on hero pages below.
        _shared_scripts = ["quiz.js", "rd-page.js"]

        # ── Exam ladder (Phase 2B, MRB-136) — architecture_v2 Law 6 ──
        # The five pages where AQA's production marks actually sit. The
        # kernel must load BEFORE the engines (they register into it) and
        # the authored content module is joined by slug. The authored items
        # are net-new: they live only in shared/exam-content/, never in the
        # eight frozen fields.
        # periodic-table.js first: the kernel calls MrbPeriodicTable.button()
        # while rendering a card, so the component must already be defined.
        _has_ladder = st_id in EXAM_LADDER_PAGES
        if _has_ladder:
            _shared_scripts += ["periodic-table.js", "exam-ladder.js",
                                "write-then-mark.js", "chain-builder.js",
                                "formula-deducer.js",
                                "exam-content/%s.js" % st_id]
        _inits = []     # inline init snippets (each wrapped in an IIFE)
        _needs_configs = False   # any hero/activity reading MrbHeroConfigs

        # ── Activity: Categorise Bins, or TapMatch (Phase 0a, MRB-132) ──
        # (kickers use the mono voice, no emoji — Phase 1g §5.9)
        act = rcfg["activity"]
        _act_id_attr = "" if rcfg.get("hero") else ' id="rd-labs"'   # Labs anchor (1e)
        _succ_tip_js = ""
        if _tip_text and _tip_mode == "activity":
            _succ_tip_js = "if(binCfg)binCfg.successTip=%s;" % _json.dumps(_tip_text, ensure_ascii=False)
        if act["type"] == "bins":
            matching_js = ""   # no drag-match widget on a bins page
            _bins_kicker = act.get("kicker", "sort the cards")
            matching_html = f"""<div class="section"{_act_id_attr}>
    <div class="rd-hero-kicker">Retrieval · {_bins_kicker}</div>
    <div id="bins-{st_id}"></div>
  </div>"""
            _scripts.append("categorise-bins.js")
            _needs_configs = True
            _inits.append(
                "var binCfg=window.MrbHeroConfigs&&MrbHeroConfigs.bonding&&MrbHeroConfigs.bonding['%s'];"
                "var binHost=document.getElementById('bins-%s');" % (act["config_key"], st_id)
                + _succ_tip_js
                + "if(binCfg&&binHost&&window.MrbHeroes&&MrbHeroes.categoriseBins)MrbHeroes.categoriseBins.init(binHost,binCfg);")
        else:
            # 'match' — Phase 0a: the old HTML5 drag-and-drop matching is DEAD on
            # touch devices and keyboard-inaccessible, so .rd pages ship TapMatch
            # (tap-select / tap-place, real buttons, browser shuffle of BOTH
            # columns, grading by mapping). The frozen `matching` field is passed
            # through UNCHANGED as the card/term texts. Group ids follow the
            # MRB-104 rule: rows sharing a term share a group.
            matching_js = ""   # retire the DnD runtime from bonding output
            _m = st.get("matching")
            if _m and _m.get("pairs"):
                _pairs = _m["pairs"]
                _tg = {}
                for _t, _d in _pairs:
                    if _t not in _tg:
                        _tg[_t] = len(_tg)
                _tm_cfg = {
                    "stId": st_id, "title": _m.get("title", "Matching"),
                    "instruction": _m.get("instruction", ""),
                    "pairs": [{"t": _t, "d": _d, "g": _tg[_t]} for _t, _d in _pairs],
                }
                if _tip_text and _tip_mode == "activity":
                    _tm_cfg["successTip"] = _tip_text
                matching_html = f"""<div class="section"{_act_id_attr}>
    <div class="rd-hero-kicker">Retrieval · {_m.get('title', 'Matching')}</div>
    <div id="match-{st_id}"></div>
  </div>"""
                _shared_scripts.append("tap-match.js")
                _inits.append(
                    "var tmHost=document.getElementById('match-%s');"
                    "if(tmHost&&window.MrbTapMatch)MrbTapMatch.init(tmHost,%s);"
                    % (st_id, _json.dumps(_tm_cfg, ensure_ascii=False)))
            else:
                matching_html = ""

        # ── Hero: structural interactive, or none ──
        hero = rcfg.get("hero")
        if hero:
            _kicker = hero.get("kicker", "explore the model")
            # Phase 1f: mistake_after == 'hero' renders the frozen Common
            # Mistake box inside the hero slot, at the moment the error is born.
            _hero_mistake = ""
            if _mistake_target == "hero" and mistake_html:
                _hero_mistake = f"\n    {mistake_html}"
                mistake_html = ""
            hero_html = f"""
  <div class="rd-hero-slot" id="rd-labs">
    <div class="rd-hero-kicker">Interactive · {_kicker}</div>
    <div id="hero-{st_id}"></div>{_hero_mistake}
  </div>
"""
            _shared_scripts.append("predict-wrapper.js")   # Phase 1a (Law 4)
            # MRB-134 Phase 1.6 (Law 9): the visible-motion engines reconcile
            # their viz through the shared keyed renderer — load it first.
            if hero["module"] in ("dot-cross-stepper", "two-state-compare", "state-toggle-lab"):
                _scripts.append("keyed-render.js")
            _scripts.append(hero["module"] + ".js")
            if hero.get("build") == "fifa":
                # FIFA config = frozen `fifas` worked spine (per variant) zipped
                # with authored per-tier practice; serialised inline.
                _fifa_cfg = build_fifa_config(st.get("fifas"), tier)
                if _fifa_cfg:
                    _cfg_json = _json.dumps(_fifa_cfg, ensure_ascii=False)
                    _inits.append(
                        "var host=document.getElementById('hero-%s');"
                        "if(host&&window.MrbHeroes&&MrbHeroes.%s)MrbHeroes.%s.init(host,%s);"
                        % (st_id, hero["ns"], hero["ns"], _cfg_json))
                else:
                    hero_html = ""   # defensive: no config → no hero slot
            else:
                _needs_configs = True
                _inits.append(
                    "var cfg=window.MrbHeroConfigs&&MrbHeroConfigs.bonding&&MrbHeroConfigs.bonding['%s'];"
                    "var host=document.getElementById('hero-%s');"
                    "if(cfg&&host&&window.MrbHeroes&&MrbHeroes.%s)MrbHeroes.%s.init(host,cfg);"
                    % (hero["config_key"], st_id, hero["ns"], hero["ns"]))
        else:
            hero_html = ""

        # theory-blocks.js only when an interactive block (mistake-check / compare-reveal) is present
        if _rd_interactive:
            _scripts.append("theory-blocks.js")
        if _needs_configs:
            _scripts.append("bonding-configs.js")

        _tb_init = interactive_init_js(_rd_interactive)
        _script_tags = "\n".join(
            ['  <script src="/shared/%s"></script>' % s for s in _shared_scripts]
            + ['  <script src="/shared/heroes/%s"></script>' % s for s in _scripts])
        _init_body = "\n".join("    (function(){%s})();" % s for s in _inits)
        hero_scripts = f"""
{_script_tags}
  <script>
{_init_body}
{_tb_init}
  </script>"""
        redesign_css = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap">
<style>
/* Redesign — page-scoped chrome (bonding · block page) */
html { background: var(--surface-page); }
.rd .rd-hero-slot { max-width: var(--content-max); margin: var(--sp-5) auto 0; padding: 0 var(--sp-5); }
.rd .rd-hero-kicker { font-family: var(--font-mono); font-size: calc(0.72rem * var(--rd-fs-scale, 1)); font-weight: 600; letter-spacing: .14em; text-transform: uppercase; color: var(--accent-deep); margin-bottom: var(--sp-3); }  /* MRB-128: kicker text uses --accent-deep #B5341A = 4.64:1 on cream; --accent-strong #C0392B was 4.17:1 (fails AA). Brand token --accent-strong unchanged. */
.rd .topic-kicker { color: var(--accent-deep); }  /* MRB-128 sweep: topic kicker inherits --subject=--accent-strong on .rd (15px on cream = 4.17:1, fails AA); lift to --accent-deep = 4.64:1. */
.rd .mistake-box { background: linear-gradient(180deg,#FBE7E2,#F8E0DA); border: 1px solid #EBBCB1; border-left: 5px solid var(--accent-strong); border-radius: var(--r-callout); }
.rd .mistake-title { color: var(--accent-deep); font-family: var(--font-display); }
.rd .keynote-box { background: linear-gradient(90deg,#FBE7E0,#F6EFE2); border: 1px solid var(--border); border-left: 5px solid var(--accent-strong); }
/* MRB-123 — old-prose elements (exemplar) whose size is a site-wide literal, not a --fs token: scale them on .rd pages too. !important beats the inline font-size on the Common Mistake <p>. */
.rd .mistake-box p { font-size: calc(0.9rem * var(--rd-fs-scale, 1)) !important; }
.rd .quiz-opt.selected { border-color: var(--accent-strong,#E0531F); background: #FBEAE1; color: var(--accent-deep,#B5341A); box-shadow: 0 6px 16px -8px rgba(224,83,31,.5); }
.rd .quiz-opt:disabled { pointer-events: none; }
.rd .quiz-opt { font-size: calc(0.9rem * var(--rd-fs-scale, 1)); }
.rd .quiz-actions { display: flex; gap: 12px; margin-top: 8px; flex-wrap: wrap; }
.rd .quiz-check-btn { font-family: var(--font-display,sans-serif); font-weight: 700; font-size: calc(0.95rem * var(--rd-fs-scale, 1)); color: #fff; background: var(--accent-deep,#B5341A); border: none; padding: 12px 22px; border-radius: 12px; cursor: pointer; box-shadow: 0 8px 20px -8px rgba(181,52,26,.7); }
.rd .quiz-again-btn { font-family: var(--font-display,sans-serif); font-weight: 600; font-size: calc(0.95rem * var(--rd-fs-scale, 1)); color: #4A4238; background: var(--surface-inset,#EFE7D8); border: 1px solid var(--border,#E4DCCB); padding: 12px 22px; border-radius: 12px; cursor: pointer; }
""" + BONDING_BLOCK_CSS + """
</style>"""

    # ── Redesigned (.rd) page overrides (MRB-133 Phase 1) — every default
    # below is byte-identical for non-rd pages. ──
    mode_chooser_html = ""
    theory_sec_open = '<div class="section">'
    theory_title_html = '<div class="section-title">📖 In-Depth Theory</div>'
    if body_class == "rd":
        # Phase 1f: the keynote-adjacent Examiner Tip section is retired — the
        # tip now renders above the quiz or inside the activity success state.
        examiner_html = ""
        # Phase 1d: Key Note becomes the photographable revision card with a
        # cover-and-recall toggle, and moves to LAST (council §3.2 rule 8) —
        # appended after the quiz, before the end-matter ritual. Frozen text.
        keynote_html = ""
        if st.get("key_note"):
            # Fix 5 (MRB-134): stepped cover-and-recall revision card. Frozen
            # note is SPLIT into mark-scheme steps (never edited); rd-page.js
            # walks cover -> reveal step 1 -> ... -> all shown.
            quiz_html += make_rd_keycard(st['key_note'], st.get('title', ''))
        # Phase 2B (MRB-136): the page ENDS in the four-rung ladder (Law 6).
        # Recognition — the quiz above — is rung ①; the module builds rungs
        # ②–④ from the authored content module. Empty mount by design: the
        # engines render everything, so nothing authored is baked into HTML.
        # Revision #4/5: the section names its subject before its content.
        if st_id in EXAM_LADDER_PAGES:
            quiz_html += f"""
  <div class="section" id="rd-ladder">
    <div class="rd-sec-kicker">Exam ladder · {_esc_html(st['title'])}</div>
    <div class="mrb-ladder" data-page="{st_id}" data-tier="{tier}" data-pathway="{pathway}"></div>
  </div>"""
        # Phase 1e: mode chooser — three anchors under the page kicker, serving
        # the 10-minute bus session and the 40-minute desk session alike.
        # Phase 2B adds a fourth on ladder pages: production is where the
        # marks are, so it gets its own way in.
        _ladder_mode = ('\n    <a href="#rd-ladder">✍️ Write it</a>'
                        if st_id in EXAM_LADDER_PAGES else '')
        mode_chooser_html = f"""
  <nav class="rd-modes" aria-label="Choose how to use this page">
    <a href="#rd-teach">📖 Teach me</a>
    <a href="#rd-labs">🎮 Labs</a>
    <a href="#rd-test">🎯 Test me</a>{_ladder_mode}
  </nav>"""
        # Phase 1g: mono kickers replace emoji section titles
        theory_sec_open = '<div class="section" id="rd-teach">'
        theory_title_html = '<div class="rd-sec-kicker">Theory · read, then commit</div>'
        star_html = f"""<div class="section">
  <div class="rd-sec-kicker">Rate your confidence · then let the quiz check it</div>
  <div class="card star-rating-card">
    <p style="font-size:0.95rem;color:var(--muted);margin-bottom:16px;">Be honest — this only has to convince you.</p>
    <div class="stars-row" id="stars-{st_id}">
      <button class="star-btn" data-rating="1" onclick="rateTopic('{st_id}', 1)" title="I don't understand this at all">⭐</button>
      <button class="star-btn" data-rating="2" onclick="rateTopic('{st_id}', 2)" title="I understand a little">⭐</button>
      <button class="star-btn" data-rating="3" onclick="rateTopic('{st_id}', 3)" title="I understand about half of it">⭐</button>
      <button class="star-btn" data-rating="4" onclick="rateTopic('{st_id}', 4)" title="I mostly understand it">⭐</button>
      <button class="star-btn" data-rating="5" onclick="rateTopic('{st_id}', 5)" title="I understand it perfectly">⭐</button>
    </div>
    <div class="star-labels">
      <span>Don't get it</span>
      <span>Getting there</span>
      <span>Nailed it</span>
    </div>
    <div class="star-feedback" id="starfb-{st_id}"></div>
  </div>
</div>"""
        _rd_star_msgs = _json.dumps(RD_STAR_MESSAGES, ensure_ascii=False)
        star_js = f"""
const STAR_MESSAGES_{st_id.replace('-','_')} = {_rd_star_msgs};
function rateTopic(stId, rating) {{
  document.querySelectorAll('#stars-' + stId + ' .star-btn').forEach((s, i) => s.classList.toggle('star-active', i < rating));
  const fb = document.getElementById('starfb-' + stId);
  fb.innerHTML = STAR_MESSAGES_{st_id.replace('-','_')}[rating - 1];
  fb.style.display = 'block';
  try {{ localStorage.setItem('star_' + stId, rating); }} catch(e) {{}}
}}
try {{
  const saved = localStorage.getItem('star_{st_id}');
  if (saved) rateTopic('{st_id}', parseInt(saved));
}} catch(e) {{}}
"""
        chat_section = f"""<div class="section">
  <div class="rd-sec-kicker">Stuck · ask Mr Badmus AI</div>
  <div class="card ask-card">
    <p class="ask-lede">Ask about anything on this page.</p>
    <p class="ask-sub">FIFA for calculations; Higher (⭐) and Triple (🔬) content flagged clearly.</p>
    <button data-open-chat class="btn-primary">💬 Ask Mr Badmus AI</button>
  </div>
</div>"""

    body = f"""
<div class="topic-header">
  <a class="back-link" href="/{pathway}/{tier}/{subject}/{topic_id}.html">← Back to {topic_title}</a>
  <div class="topic-kicker">{subject_label} · {topic_title}</div>
  <h1>{st['title']}</h1>
  <div class="meta-row">
    <span class="spec-pill">Spec {st['spec']}</span>
    <span class="tier-pill">{tier_badge}</span>
  </div>{mode_chooser_html}
</div>

<div class="content-area">
{hero_html}
  {theory_sec_open}
    {theory_title_html}
    {theory_html}
    {mistake_html}
  </div>

  {var_html}
  {eq_html}
  {keynote_html}{examiner_html}{studio_html}
  {matching_html}
  {fifa_html_content}
  {higher_html}
  {triple_html}
  {rp_html}
  {quiz_html}
  {star_html}
  {chat_section}
  {subtopic_nav_html}

</div>"""

    extra_css = f"""
<style>
html {{ background: var(--bg); }}
:root {{ --subject: {color}; }}
</style>"""

    # Emit the matching <script> only when there is matching JS to run. On the
    # pilot page matching_js is nulled (JOB 1), so no empty/dead tag appears.
    # For every other page matching_js is non-empty, so this is byte-identical
    # to the previous unconditional `<script>{matching_js}</script>`.
    matching_script = f"<script>{matching_js}</script>" if matching_js else ""
    # Same guard for the quiz engine: .rd pages null quiz_js (the engine ships
    # as /shared/quiz.js, Phase 0d); every other page keeps the inline blob and
    # stays byte-identical.
    quiz_script = f"<script>{quiz_js}</script>" if quiz_js else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <meta name="theme-color" content="{THEME_COLOR}"/>
  <title>{st['title']} | {subject_label} | MrBadmusAI</title>
  {HEAD_ASSETS}
  {extra_css}
  {redesign_css}
</head>
<body class="{body_class}">
  {nav_html(subject, pathway, tier)}
  {body}
  {chat_html()}
  <script src="/shared/mrbadmus.v2.js"></script>
  <script>MrBadmus.init({{subject:'{subject}',topic:'{st["title"]} ({st["spec"]})'}});</script>
  {quiz_script}
  {matching_script}
  <script>{star_js}</script>
  {hero_scripts}
</body>
</html>"""



# ─────────────────────────────────────────────
#  UPDATED TOPIC PAGE — + button links to full subtopic page
#  Used for topics that have detailed subtopic data
# ─────────────────────────────────────────────


def make_pathway_topic_page_with_subtopics(pathway, tier, subject, topic, subtopics_list):
    """The topic page — Design's "Energy topic" screen (MRB-301).

    THE LAST PAGE OF THE JOURNEY. Every subtopic row here opens a LESSON
    page, and lesson pages are the next run: nothing below writes one, and
    `make_pathway_subtopic_page` is not touched by MRB-301 at all.

    ── WHAT DESIGN DREW, AND WHAT LIVE LOGIC KEPT ─────────────────────────

    Kept from Design: the hero with its derived tag row, the bordered
    subtopic list, the equations panel, the "Ask about X" card and the
    required-practicals panel.

    Kept from the LIVE page because Design did not draw them and dropping
    them would lose real content or real navigation:

      · the ⭐ Higher and 🔬 Triple sections — teaching that only appears
        on this page, and only at the tier/pathway that gets it;
      · the PREVIOUS topic link. Design drew "Next topic" alone; a
        one-way spine is a navigation regression, so both ends render;
      · the "GCSE Science" rung of the trail. Design's deepest screen
        starts at "Combined", which leaves no route back to /ks4.html
        from here other than the brand.

    Dropped from Design, and reported: the per-subtopic DONE / HALF
    FINISHED / NOT STARTED states, the tick glyphs that encode them, and
    the "Your progress here — 3 of 7 done" card. No KS4 progress model
    exists to fill any of it."""
    data = SITE_DATA[subject]
    hue = data["color"]
    label = data["label"]
    pathway_label = "Combined Science" if pathway == "combined" else "Triple Science"

    n_rp = len(topic.get("rp") or [])
    n_st = len(subtopics_list)

    tags = f'<span class="k4-tag k4-tag-lg">Spec {topic["spec"]}</span>'
    tags += f'<span class="k4-tag k4-tag-lg">Paper {topic["paper"]}</span>'
    if n_rp:
        tags += (f'<span class="k4-tag k4-tag-lg k4-tag-rp">{n_rp} required '
                 f'practical{"s" if n_rp > 1 else ""}</span>')
    tags += (f'<span class="k4-tag k4-tag-lg">{n_st} subtopic'
             f'{"s" if n_st != 1 else ""}</span>')

    # ── Subtopic rows. Each opens a lesson page; none is restyled. ──
    rows = ""
    for i, st in enumerate(subtopics_list):
        st_url = f"/{pathway}/{tier}/{subject}/{topic['id']}/{st['id']}.html"
        desc = (f'<span class="k4-row-desc">{st["summary"]}</span>'
                if st.get("summary") else "")
        rows += f"""
          <a class="k4-row k4-row-st" id="row-{st['id']}" href="{st_url}">
            <span class="k4-row-num">{i + 1}</span>
            <span class="k4-row-body">
              <span class="k4-row-title">{st['title']}</span>
              {desc}
              <span class="k4-row-meta">Spec {st['spec']}</span>
            </span>
            {K4_ARROW_ACCENT}
          </a>"""

    # ── Equations. The Foundation filter is the live rule, unchanged. ──
    formulae = ""
    for eq in topic.get("equations") or []:
        if "(Higher)" in eq and tier == "foundation":
            continue
        long_cls = " k4-formula-long" if len(eq) > 26 else ""
        formulae += f'<span class="k4-formula{long_cls}">{eq}</span>'
    equations_panel = ""
    if formulae:
        equations_panel = f"""
        <div class="k4-panel">
          <div class="k4-kicker">Equations you need</div>
          <div class="k4-formulae">{formulae}</div>
          <div class="k4-formulae-footer">
            <p class="k4-formulae-footer-label">View the full equation sheet:</p>
            <a class="k4-formulae-footer-link" href="{AQA_EQUATION_SHEET_COMBINED}" target="_blank" rel="noopener">Combined Science {K4_ARROW}</a>
            <a class="k4-formulae-footer-link" href="{AQA_EQUATION_SHEET_TRIPLE}" target="_blank" rel="noopener">Triple Science (Physics) {K4_ARROW}</a>
          </div>
        </div>"""

    # ── Required practicals. Design wrote hers as a sentence naming the
    #    two in Energy; the names come out of the spec data instead, so a
    #    topic with three, or none, says so by itself. ──
    rp_panel = ""
    if n_rp:
        items = "".join(f'<span class="k4-formula k4-formula-long">{rp}</span>'
                        for rp in topic["rp"])
        rp_panel = f"""
        <div class="k4-panel k4-panel-soft">
          <div class="k4-kicker">Required practicals</div>
          <p>{k4_word(n_rp, cap=True)} sit{"s" if n_rp == 1 else ""} inside this topic, and {"it is" if n_rp == 1 else "they are"} fair game in Paper {topic["paper"]}.</p>
          <div class="k4-formulae">{items}</div>
        </div>"""

    # ── Higher / Triple content — live only, Design drew neither. ──
    extra = ""
    if tier == "higher" and topic.get("higher"):
        items = "".join(f"<p>{h}</p>" for h in topic["higher"])
        extra += f"""
        <div class="k4-panel k4-panel-soft" style="margin-top:24px">
          <div class="k4-kicker">Higher tier only</div>
          {items}
        </div>"""
    if pathway == "triple" and topic.get("triple_only"):
        items = "".join(f"<p>{tr}</p>" for tr in topic["triple_only"])
        extra += f"""
        <div class="k4-panel k4-panel-soft" style="margin-top:24px">
          <div class="k4-kicker">Triple science extension</div>
          {items}
        </div>"""

    # ── Previous / next along the spec spine. ──
    topics_in_path = k4_topics_for(pathway, tier, subject)
    curr = next((i for i, t in enumerate(topics_in_path) if t["id"] == topic["id"]), None)
    prev_t = topics_in_path[curr - 1] if curr not in (None, 0) else None
    next_t = (topics_in_path[curr + 1]
              if curr is not None and curr < len(topics_in_path) - 1 else None)

    spine = ""
    for kicker, t in [("Previous topic", prev_t), ("Next topic", next_t)]:
        if not t:
            continue
        spine += f"""
        <div class="k4-nextrow">
          <div>
            <div class="k4-kicker">{kicker}</div>
            <p class="k4-nextrow-title">{t['title']}</p>
          </div>
          <a class="k4-cta-quiet" href="/{pathway}/{tier}/{subject}/{t['id']}.html">Spec {t['spec']} · Paper {t['paper']} {K4_ARROW}</a>
        </div>"""

    body = f"""
<main class="k4-main">
  {k4_crumbs([("GCSE Science", "/ks4.html"),
              (pathway.title(), f"/{pathway}/index.html"),
              (tier.title(), f"/{pathway}/{tier}/index.html"),
              (label, f"/{pathway}/{tier}/{subject}/index.html"),
              (topic["title"], None)])}

  <section class="k4-band" style="margin-bottom:36px">
    <div class="k4-band-copy">
      <div class="k4-eyebrow"><span class="k4-dot" style="background:{hue}"></span>{label} · {pathway_label} {tier.title()}</div>
      <h1 class="k4-h1 k4-h1-topic">{topic['title']}</h1>
      <div class="k4-pills" style="margin-top:20px;gap:9px">{tags}</div>
    </div>
  </section>

  <section class="k4-split">
    <div class="k4-split-main">
      <div class="k4-section-head">
        <span class="k4-section-label">Subtopics</span>
        <span class="k4-rule"></span>
      </div>
      <div class="k4-list">{rows}
      </div>
      {extra}
      {spine}
      <p style="margin-top:24px"><a href="/{pathway}/{tier}/{subject}/index.html">All {label} topics</a></p>
    </div>

    <aside class="k4-split-side">{equations_panel}

      <div class="k4-dark">
        <div class="k4-kicker k4-kicker-ondark">Stuck on something</div>
        <p class="k4-dark-title">Ask about {topic['title']}</p>
        <p>Calculations get worked through with FIFA, and anything Higher or Triple is flagged before you learn it by mistake.</p>
        <button type="button" data-open-chat class="k4-cta">Ask MrBadmusAI {K4_ARROW}</button>
      </div>
{rp_panel}
    </aside>
  </section>
</main>"""

    return k4_page(f"{topic['title']} | {label} | MrBadmusAI", body,
                   subject=subject, pathway=pathway, tier=tier,
                   topic_title=f"{topic['title']} ({topic['spec']})")


def build_site(output_dir="mrbadmus_site"):
    import sys, os, shutil
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    # Import subtopic data
    try:
        from all_subtopics_physics           import PHYSICS_SUBTOPICS_ALL
        from all_subtopics_physics_higher                     import PHYSICS_SUBTOPICS_ALL as PHYSICS_SUBTOPICS_HIGHER
        from all_subtopics_physics_triple_foundation import PHYSICS_SUBTOPICS_ALL as PHYSICS_SUBTOPICS_TRIPLE_FOUNDATION
        from all_subtopics_physics_triple_higher    import PHYSICS_SUBTOPICS_ALL as PHYSICS_SUBTOPICS_TRIPLE_HIGHER
        from all_subtopics_chemistry         import CHEMISTRY_SUBTOPICS_ALL
        from all_subtopics_chemistry_higher              import CHEMISTRY_SUBTOPICS_ALL as CHEMISTRY_SUBTOPICS_HIGHER
        from all_subtopics_chemistry_triple_foundation import CHEMISTRY_SUBTOPICS_ALL as CHEMISTRY_SUBTOPICS_TRIPLE_FOUNDATION
        from all_subtopics_chemistry_triple_higher    import CHEMISTRY_SUBTOPICS_ALL as CHEMISTRY_SUBTOPICS_TRIPLE_HIGHER
        from all_subtopics_biology                     import BIOLOGY_SUBTOPICS_ALL
        from all_subtopics_biology_higher            import BIOLOGY_SUBTOPICS_ALL as BIOLOGY_SUBTOPICS_HIGHER
        from all_subtopics_biology_triple_foundation import BIOLOGY_SUBTOPICS_ALL as BIOLOGY_SUBTOPICS_TRIPLE_FOUNDATION
        from all_subtopics_biology_triple_higher    import BIOLOGY_SUBTOPICS_ALL as BIOLOGY_SUBTOPICS_TRIPLE_HIGHER
        print("  ✅ Loaded subtopic modules")
    except ImportError as e:
        print(f"  ⚠️  Could not load subtopics: {e}")
        PHYSICS_SUBTOPICS_ALL        = {}
        PHYSICS_SUBTOPICS_HIGHER     = {}
        PHYSICS_SUBTOPICS_TRIPLE_FOUNDATION   = {}
        PHYSICS_SUBTOPICS_TRIPLE_HIGHER       = {}
        CHEMISTRY_SUBTOPICS_ALL      = {}
        CHEMISTRY_SUBTOPICS_HIGHER                 = {}
        CHEMISTRY_SUBTOPICS_TRIPLE_FOUNDATION    = {}
        CHEMISTRY_SUBTOPICS_TRIPLE_HIGHER        = {}
        BIOLOGY_SUBTOPICS_ALL                     = {}
        BIOLOGY_SUBTOPICS_HIGHER                 = {}
        BIOLOGY_SUBTOPICS_TRIPLE_FOUNDATION      = {}
        BIOLOGY_SUBTOPICS_TRIPLE_HIGHER          = {}

    SUBTOPICS_ALL = {
        "physics":   PHYSICS_SUBTOPICS_ALL,
        "chemistry": CHEMISTRY_SUBTOPICS_ALL,
        "biology":   BIOLOGY_SUBTOPICS_ALL,
    }

    print(f"\n🏗️  Building MrBadmusAI v5 → {output_dir}/\n")

    # ── Wipe the deploy tree — except output this generator does not own ───
    # build_site() rebuilds output_dir from scratch. That is correct for
    # everything it generates and destructive for everything it does not.
    # `mrbadmus_site/ks3/` is written by build_ks3.py, a deliberately separate
    # generator (see its module docstring), so the plain rmtree that used to be
    # here deleted every KS3 page whenever this generator ran second —
    # demonstrated, not inferred: 221 KS3 pages before, 0 after. Nothing
    # complained. The KS4 build succeeded, exit 0, and KS3 simply vanished from
    # the tree Cloudflare serves until build_ks3.py next ran, so whether KS3
    # existed in production depended purely on which generator ran last.
    #
    # The repo-root round-trip disguised it rather than catching it: that loop
    # only rmtree's top-level dirs it finds in output_dir, so with ks3/ already
    # gone the stale ./ks3/ mirror survived untouched — deployed output and
    # source disagreeing silently, which is the state hardest to notice.
    #
    # Deleting entry-by-entry and skipping the foreign trees is deliberate: an
    # earlier fix moved them aside and restored them afterwards, which works but
    # strands the KS3 output in a temp dir if the build raises in between. This
    # never moves them at all, so there is no window in which they are anywhere
    # but where they belong. Either generator order is safe.
    #
    # Add a name here whenever another standalone generator starts writing into
    # mrbadmus_site/. Anything NOT listed is still wiped, which is the point:
    # one tree, one writer.
    FOREIGN_OUTPUT_DIRS = ["ks3", "3d"]

    if os.path.exists(output_dir):
        for _entry in os.listdir(output_dir):
            if _entry in FOREIGN_OUTPUT_DIRS:
                continue
            _p = os.path.join(output_dir, _entry)
            shutil.rmtree(_p) if os.path.isdir(_p) else os.remove(_p)

    # Directory structure
    dirs = [
        output_dir,
        f"{output_dir}/shared",
        f"{output_dir}/combined",
        f"{output_dir}/combined/foundation",
        f"{output_dir}/combined/higher",
        f"{output_dir}/triple",
        f"{output_dir}/triple/foundation",
        f"{output_dir}/triple/higher",
    ]
    for pathway in ["combined", "triple"]:
        for tier in ["foundation", "higher"]:
            for subject in ["physics", "chemistry", "biology"]:
                dirs.append(f"{output_dir}/{pathway}/{tier}/{subject}")
                # Create subdirs for each topic (for subtopic pages)
                topic_ids = PATHWAY_TOPIC_MAP[(pathway, tier)][subject]
                for tid in topic_ids:
                    dirs.append(f"{output_dir}/{pathway}/{tier}/{subject}/{tid}")

    for d in dirs:
        os.makedirs(d, exist_ok=True)

    total_pages = 0

    # ── Shared files ──
    with open(f"{output_dir}/shared/styles.css", "w") as f:
        f.write(SHARED_CSS_PATCHED)
    print("  ✅ shared/styles.css")

    with open(f"{output_dir}/shared/mrbadmus.v2.js", "w") as f:
        f.write(SHARED_JS_PATCHED)
    print("  ✅ shared/mrbadmus.v2.js")


    # ── Auth pages — copy into output if they exist in repo root ──
    import shutil as _shutil, os as _os
    # ⊕ MRB-257 · KS3 Biology audit 6.1 — `404.html` JOINS THIS LIST.
    #
    # Cloudflare Pages looks for `404.html` in the nearest ancestor directory of
    # a request it cannot resolve, and — this is the part that bit us — when it
    # finds none ANYWHERE it falls back to serving the root `index.html` with a
    # **200**. Measured on the live site: three bogus paths plus `/favicon.ico`
    # all returned 200 text/html, 7,396 bytes, byte-identical (md5 b676e202…),
    # titled "MrBadmusAI — Free KS3 & GCSE Science Revision". A stale bookmark
    # dumped a student on the marketing homepage with no sign anything had gone
    # wrong, and every wrong URL was a candidate for indexing as the homepage.
    #
    # It has to be copied from here rather than written by build_ks3.py: that
    # generator writes only under `mrbadmus_site/ks3/` on purpose, and anything
    # it left at the output root would be deleted by the wipe loop above the
    # next time this generator ran.
    for _auth_file in ["404.html", "auth.html", "reset-password.html", "profile-setup.html", "teacher-profile.html", "weekly-challenge.html", "leaderboard.html", "past-papers.html", "my-challenges.html", "revision.html"]:
        _src = _auth_file
        _dst = f"{output_dir}/{_auth_file}"
        if _os.path.exists(_src):
            _shutil.copy2(_src, _dst)
            print(f"  ✅ {_auth_file}")
        else:
            print(f"  ⚠️  {_auth_file} not found — skipping")

    # ── Auto-copy any non-patched file in shared/ ──
    # Glob-based instead of hardcoded list so future additions to shared/
    # don't require generator edits. styles.css and mrbadmus.v2.js are
    # excluded — those are written above via templated open() and would
    # be overwritten by a plain copy.
    _shared_explicit_writes = {"styles.css", "mrbadmus.v2.js"}
    for _src in sorted(glob.glob("shared/*")):
        _filename = os.path.basename(_src)
        if _filename in _shared_explicit_writes:
            continue
        _dst = f"{output_dir}/shared/{_filename}"
        try:
            if os.path.isdir(_src):
                # Subdirectories (e.g. shared/fonts/) copied whole —
                # the flat glob alone would skip them and trip the
                # round-trip safety net below.
                if _os.path.exists(_dst):
                    _shutil.rmtree(_dst)
                _shutil.copytree(_src, _dst)
                print(f"  ✅ shared/{_filename}/ (directory)")
            else:
                _shutil.copy2(_src, _dst)
                print(f"  ✅ shared/{_filename}")
        except Exception as e:
            print(f"  ⚠️  shared/{_filename}: {e}")

    # ── Stage 2A teacher pages tree ──
    # Whole teacher/ directory copied so /teacher/classes.html (and future
    # /teacher/* pages from MRB-20 onwards) get emitted into mrbadmus_site/.
    _teacher_src = "teacher"
    _teacher_dst = f"{output_dir}/teacher"
    if _os.path.exists(_teacher_src):
        if _os.path.exists(_teacher_dst):
            _shutil.rmtree(_teacher_dst)
        _shutil.copytree(_teacher_src, _teacher_dst)
        print(f"  ✅ teacher/ (directory tree)")
    else:
        print(f"  ⚠️  teacher/ directory not found — skipping")

    # ── Stage 2C student pages tree ──
    # Mirror of the teacher/ block above. Whole student/ directory copied
    # into output. Added in MRB-46 Phase 3 (Stage 2C) for /student/class.html.
    _student_src = "student"
    _student_dst = f"{output_dir}/student"
    if _os.path.isdir(_student_src):
        if _os.path.exists(_student_dst):
            _shutil.rmtree(_student_dst)
        _shutil.copytree(_student_src, _student_dst)
        print(f"  ✅ student/ (directory tree)")
    else:
        print(f"  ⚠️  student/ directory not found — skipping")

    # ── MRB-308 consumer pages tree ──
    # Mirror of the teacher/ and student/ blocks above. WITHOUT THIS BLOCK
    # THE WHOLE DIRECTORY IS DEAD: Cloudflare serves mrbadmus_site/, not the
    # repo root, so a /consumer/* page that is never copied here is a page
    # that returns 404 in every deployed environment while looking perfectly
    # correct in the repo — the failure mode that reads as "the flag must
    # still be off" rather than as "the file was never published".
    #
    # ⚠️ Adding the tree here is also what puts it under the round-trip's
    # rmtree, which is why "consumer" joins the safety-net list below in the
    # same change. The two lines are one decision; do not keep one without
    # the other.
    _consumer_src = "consumer"
    _consumer_dst = f"{output_dir}/consumer"
    if _os.path.isdir(_consumer_src):
        if _os.path.exists(_consumer_dst):
            _shutil.rmtree(_consumer_dst)
        _shutil.copytree(_consumer_src, _consumer_dst)
        print(f"  ✅ consumer/ (directory tree)")
    else:
        print(f"  ⚠️  consumer/ directory not found — skipping")

    # ⊕ MRB-317/318 Night 3 — three MORE consumer trees, same rule as above.
    #   parents/  the public front door (home, how it works, pricing, home
    #             education, sign-in chooser) — the address a parent is given
    #   go/       the child's login, at the shortest URL a child can type:
    #             mrbadmus.com/go — the address printed in the E2 email
    #   org/      the organisation (council / tutoring centre) staff surface
    # Every page in all three is behind CONSUMER_SIGNUP_ENABLED exactly as
    # consumer/ is, and every one joins the safety-net list below for the
    # same reason consumer/ did.
    for _tree in ("parents", "go", "org"):
        _t_src = _tree
        _t_dst = f"{output_dir}/{_tree}"
        if _os.path.isdir(_t_src):
            if _os.path.exists(_t_dst):
                _shutil.rmtree(_t_dst)
            _shutil.copytree(_t_src, _t_dst)
            print(f"  ✅ {_tree}/ (directory tree)")
        else:
            print(f"  ⚠️  {_tree}/ directory not found — skipping")

    # ── 3D Studio built artifact (MRB-185 recon, MRB-194 integration) ──
    # 3d-studio/ is a Vite app at repo root; its build output (3d-studio/dist/)
    # is the single source of truth for mrbadmus_site/3d/. This block is the
    # ONLY writer of that path: "3d" is in FOREIGN_OUTPUT_DIRS, so the wipe
    # loop and the cache-bust stamping both leave it alone, and it is opted out
    # of the repo-root round-trip below (no ./3d/ mirror — Cloudflare serves
    # mrbadmus_site/ only, and a mirror would be a third copy of every
    # multi-MB GLB in git with no reader). One tree, one writer.
    #
    # No `npm run build` is invoked from here, deliberately. A Node failure
    # must never be able to fail a KS3 or KS4 build. The Vite build is a manual
    # pre-step documented in CLAUDE.md, and the staleness check below is its
    # safety net.
    #
    # Two failure modes, both LOUD, neither fatal, neither destructive:
    #   dist/ missing → the deployed studio is left exactly as it is, never
    #                   deleted. A machine without a Node toolchain (or a fresh
    #                   clone) must not be able to wipe live output — that is
    #                   the MRB-88 lesson.
    #   dist/ stale   → the studio is still published (dist IS the source of
    #                   truth, and republishing it changes nothing), but the
    #                   run shouts, because otherwise Mide's normal workflow —
    #                   generator, then GitHub Desktop, with no npm step in it
    #                   — ships an old build silently every single time.
    # Both warnings are re-printed after the "Done" line, because a warning
    # 2,000 green ticks above the end of the output has not been delivered.
    _studio_root = "3d-studio"
    _studio_dist = _os.path.join(_studio_root, "dist")
    _studio_dst = f"{output_dir}/3d"
    _studio_src_dirs = [_os.path.join(_studio_root, _d)
                        for _d in ("src", "content", "public")]
    _studio_alarm = None

    def _newest_file_mtime(_top):
        """Newest mtime of any file under _top, or None if it holds no files.

        Directory mtimes are deliberately ignored: a directory's mtime only
        moves when an entry is added or removed, so editing a file in place
        would not register. Files are what Vite reads.
        """
        _newest = None
        for _r, _subdirs, _files in _os.walk(_top):
            _subdirs[:] = [_d for _d in _subdirs if _d != "node_modules"]
            for _f in _files:
                if _f == ".DS_Store":
                    continue
                try:
                    _m = _os.path.getmtime(_os.path.join(_r, _f))
                except OSError:
                    continue
                if _newest is None or _m > _newest:
                    _newest = _m
        return _newest

    def _shout(_lines):
        """A warning sized to survive a wall of green ticks."""
        _w = 78
        print()
        print("!" * _w)
        for _l in _lines:
            print("!! " + _l.ljust(_w - 6) + " !!")
        print("!" * _w)
        print()

    if _os.path.isdir(_studio_dist):
        _dist_mtime = _newest_file_mtime(_studio_dist)
        _src_mtime = None
        for _sd in _studio_src_dirs:
            if not _os.path.isdir(_sd):
                continue
            _m = _newest_file_mtime(_sd)
            if _m is not None and (_src_mtime is None or _m > _src_mtime):
                _src_mtime = _m

        if _os.path.exists(_studio_dst):
            _shutil.rmtree(_studio_dst)
        _shutil.copytree(_studio_dist, _studio_dst)
        _studio_files = sum(len(_f) for _, _, _f in _os.walk(_studio_dst))
        print(f"  ✅ 3d/ ({_studio_files} files, from {_studio_dist})")

        if _dist_mtime is not None and _src_mtime is not None and _dist_mtime < _src_mtime:
            import datetime as _dt
            _fmt = "%d %b %H:%M:%S"
            _studio_alarm = [
                "",
                "STALE 3D STUDIO BUILD — the studio you just published is OLD.",
                "",
                f"  3d-studio/dist/  last built  {_dt.datetime.fromtimestamp(_dist_mtime).strftime(_fmt)}",
                f"  3d-studio source last edited {_dt.datetime.fromtimestamp(_src_mtime).strftime(_fmt)}",
                "",
                "  Source has changed since the last Vite build, so mrbadmus_site/3d/",
                "  does NOT contain your latest 3D Studio work. Everything else in",
                "  this build is fine — KS3 and KS4 are unaffected.",
                "",
                "  Fix, then run this generator again:",
                "",
                "      cd 3d-studio && npm run build && cd ..",
                "",
            ]
            _shout(_studio_alarm)
    else:
        _studio_alarm = [
            "",
            "NO 3D STUDIO BUILD FOUND — 3d-studio/dist/ does not exist.",
            "",
            f"  {_studio_dst} has been LEFT UNTOUCHED (not deleted), so whatever",
            "  was last deployed is still there. But nothing was published from",
            "  source in this run. Everything else in this build is fine — KS3 and",
            "  KS4 are unaffected.",
            "",
            "  If you meant to publish the studio, run:",
            "",
            "      cd 3d-studio && npm install && npm run build && cd ..",
            "",
        ]
        _shout(_studio_alarm)

    # ── Landing pages ──
    # /index.html is the key-stage chooser; /ks4.html is the GCSE landing that
    # used to be at /. Both are written here and both round-trip to the repo
    # root via the copy loop at the end of this function (MRB-176 ruling 1).
    with open(f"{output_dir}/index.html", "w") as f:
        f.write(make_landing())
    print("  ✅ index.html (key-stage chooser)")
    total_pages += 1

    with open(f"{output_dir}/ks4.html", "w") as f:
        f.write(make_ks4_landing())
    print("  ✅ ks4.html (GCSE landing)")
    total_pages += 1

    # ── Pathway pages ──
    for pathway in ["combined", "triple"]:
        with open(f"{output_dir}/{pathway}/index.html", "w") as f:
            f.write(make_pathway_page(pathway))
        print(f"  ✅ {pathway}/index.html")
        total_pages += 1

        # ── Tier pages ──
        for tier in ["foundation", "higher"]:
            with open(f"{output_dir}/{pathway}/{tier}/index.html", "w") as f:
                f.write(make_tier_page(pathway, tier))
            print(f"  ✅ {pathway}/{tier}/index.html")
            total_pages += 1

            # ── Subject hubs ──
            for subject in ["physics", "chemistry", "biology"]:
                with open(f"{output_dir}/{pathway}/{tier}/{subject}/index.html", "w") as f:
                    f.write(make_pathway_hub(pathway, tier, subject))
                print(f"  ✅ {pathway}/{tier}/{subject}/index.html")
                total_pages += 1

                # ── Topic pages ──
                topic_ids = PATHWAY_TOPIC_MAP[(pathway, tier)][subject]
                subj_data = SITE_DATA[subject]
                # Use correct data for pathway/tier — Triple must come before generic Higher
                if subject == "biology" and tier == "higher" and pathway == "triple":
                    subj_subtopics = BIOLOGY_SUBTOPICS_TRIPLE_HIGHER
                elif subject == "biology" and tier == "foundation" and pathway == "triple":
                    subj_subtopics = BIOLOGY_SUBTOPICS_TRIPLE_FOUNDATION
                elif subject == "biology" and tier == "higher":
                    subj_subtopics = BIOLOGY_SUBTOPICS_HIGHER
                elif subject == "chemistry" and tier == "higher" and pathway == "triple":
                    subj_subtopics = CHEMISTRY_SUBTOPICS_TRIPLE_HIGHER
                elif subject == "chemistry" and tier == "foundation" and pathway == "triple":
                    subj_subtopics = CHEMISTRY_SUBTOPICS_TRIPLE_FOUNDATION
                elif subject == "chemistry" and tier == "higher":
                    subj_subtopics = CHEMISTRY_SUBTOPICS_HIGHER
                elif subject == "physics" and tier == "higher" and pathway == "triple":
                    subj_subtopics = PHYSICS_SUBTOPICS_TRIPLE_HIGHER
                elif subject == "physics" and tier == "foundation" and pathway == "triple":
                    subj_subtopics = PHYSICS_SUBTOPICS_TRIPLE_FOUNDATION
                elif subject == "physics" and tier == "higher":
                    subj_subtopics = PHYSICS_SUBTOPICS_HIGHER
                else:
                    subj_subtopics = SUBTOPICS_ALL[subject]
                color = subj_data["color"]

                for topic in subj_data["topics"]:
                    if topic["id"] not in topic_ids:
                        continue

                    topic_subtopics = subj_subtopics.get(topic["id"], [])

                    if topic_subtopics:
                        # Has subtopic detail pages → use + link version
                        page_html = make_pathway_topic_page_with_subtopics(
                            pathway, tier, subject, topic, topic_subtopics)
                    else:
                        # No subtopic data → use plain topic page
                        page_html = make_pathway_topic_page(pathway, tier, subject, topic)

                    path = f"{output_dir}/{pathway}/{tier}/{subject}/{topic['id']}.html"
                    with open(path, "w") as f:
                        f.write(page_html)
                    print(f"     ✅ {pathway}/{tier}/{subject}/{topic['id']}.html")
                    total_pages += 1

                    # ── Subtopic pages ──
                    for i, st in enumerate(topic_subtopics):
                        st_html = make_pathway_subtopic_page(
                            st, color, subject, pathway, tier,
                            topic_subtopics, topic["id"], topic["title"]
                        )
                        st_path = f"{output_dir}/{pathway}/{tier}/{subject}/{topic['id']}/{st['id']}.html"
                        with open(st_path, "w") as f:
                            f.write(st_html)
                        print(f"        ✅ .../{topic['id']}/{st['id']}.html")
                        total_pages += 1

    # No "put the foreign trees back" step here any more: nothing was moved.
    # The wipe above skips FOREIGN_OUTPUT_DIRS in place, so ks3/ never leaves
    # output_dir and the copy-to-repo-root round-trip below finds it exactly
    # where it belongs — the root ks3/ mirror stays faithful without help.

    # ── Safety net — fail loudly if the round-trip would delete source files ──
    # The "Copy to repo root" round-trip below does shutil.rmtree(./<dir>) for
    # each top-level dir in mrbadmus_site/ before copytree-ing it back. If a
    # source dir has files not represented in mrbadmus_site/, those files get
    # destroyed. This check catches the bug class permanently — any future
    # addition to shared/, teacher/, or student/ that the generator doesn't
    # know about will fail here instead of silently destroying files.
    # Discovered in MRB-46 Phase 3 / MRB-35 bundle merge when three shared/*
    # JS files added by the bundle were silently deleted from the source tree
    # by the round-trip. See MRB-88 for the architectural follow-up
    # (auto-discovery across all top-level dirs, not just these three).
    # ⊕ MRB-308 — "consumer" joins the list the moment consumer/ becomes a
    # round-tripped tree. See the copy block above: a tree that is copied to
    # the root is a tree that can be DELETED from source by the round-trip,
    # and this net is the only thing that catches a file the generator has
    # not been told about.
    for _dir in ["shared", "teacher", "student", "consumer", "parents", "go", "org"]:
        if not os.path.isdir(_dir):
            continue
        _source_files = set(os.listdir(_dir))
        _deploy_dir = os.path.join(output_dir, _dir)
        _deploy_files = set(os.listdir(_deploy_dir)) if os.path.isdir(_deploy_dir) else set()
        _missing = _source_files - _deploy_files
        if _missing:
            print(f"\n❌ ABORT: {_dir}/ has files not in {output_dir}/{_dir}/:")
            for _f in sorted(_missing):
                print(f"     {_f}")
            print(f"   The round-trip would delete these from source.")
            print(f"   Either copy them to {output_dir}/{_dir}/ explicitly, or add them to the generator's copy logic.")
            sys.exit(1)

    # ── Cache-bust shared stylesheets ──
    # Stamp a content-hash version query (?v=<hash>) onto every <link> to a
    # shared stylesheet, so browsers, network proxies, and Cloudflare's edge
    # refetch the CSS when — and only when — its content changes. Without this,
    # a device can keep serving an old cached styles.css/tokens.css indefinitely
    # (survives hard-refresh and incognito when the stale copy is upstream),
    # which is exactly how a font-size fix goes live everywhere except one
    # laptop. Runs before the round-trip so both mrbadmus_site/ and the repo
    # root get the same stamped links. Idempotent: the regex matches whether or
    # not a stale ?v= is already present, so a previously-stamped copied file
    # (auth.html, teacher/*, etc.) is re-stamped to the current hash, never
    # frozen at an old one.
    import hashlib as _hashlib, re as _re
    # nav.js is on this list for the same reason nav.css is, and the omission
    # was a real hole rather than a decision: the nav's BEHAVIOUR — the drawer's
    # menu rows — lives in the JS, so a device holding a cached nav.js keeps an
    # old menu however many times the CSS is rebusted. Found when the 3D Studio
    # drawer row was added (MRB-214) and the row would have reached nobody who
    # had already loaded the site. The regex below is written against a bare
    # `/shared/<name>"`, which is the shape of both the <link> and the <script>
    # tag, so extending the list is the whole change.
    # ⊕ MRB-260, 19 Aug 2026 — mrbadmus.v2.js joins the list, and its absence
    # was the more expensive of the two holes on it.
    #
    # Every page includes the chat engine as a BARE `<script
    # src="/shared/mrbadmus.v2.js">` — 1,966 tags, all identical, none
    # versioned — while the KS3 tree has carried per-build stamps on its shared
    # assets since §8.5. So MRB-234's auth-header fix shipped to new visitors
    # only: a returning student keeps whatever copy their browser cached, for
    # as long as the cache lives, and no amount of redeploying changes that.
    # `chat_logs` sitting at zero after MRB-234 shipped is exactly what that
    # looks like from the outside, and it is indistinguishable from the fix not
    # working — which is the real cost. Without this line every future
    # chat-engine fix would be debugged the same way again.
    #
    # The regex below is written against a bare `/shared/<name>"`, which is the
    # shape of this tag as much as of the <link>s, so the list is the change.
    #
    # ⊕ MRB-261, 19 Aug 2026 — the two dashboard data layers join the list.
    # The year-scoping fix (a student must be shown this year's class, not the
    # one they left in July) lives entirely inside student-data.js and
    # teacher-data.js, and both were loaded as bare unversioned <script> tags.
    # Shipping it unbusted would have reached new visitors only — the same
    # failure mode as mrbadmus.v2.js above, and just as invisible from the
    # outside.
    #
    # ⊕ AND THE REST OF THE HOLE IS CLOSED, same day. The paragraph above
    # used to end by naming what it had NOT fixed — "config.js, the two
    # guards, shoutouts.js, search*.js still carry it; that is a known hole,
    # not a decision". Adding only the two files a change happened to touch
    # is how this list has grown every time, and it guarantees the next fix
    # to any other shared module ships silently broken for returning
    # visitors and is then debugged from scratch. So EVERY shared asset the
    # built tree loads is stamped now, not the ones this run needed:
    #
    #   · the six that were named as outstanding — config.js, the student
    #     and teacher guards, shoutouts.js, search-index.js, search.js
    #     (search* is on 1,000 pages);
    #   · and the ten instrument engines the KS4 bonding-redesign pages load
    #     — rd-page.js, quiz.js and the eight exam engines — which were
    #     never named but carry the identical defect on 46 pages. Leaving
    #     them would have been the same decision that produced this
    #     paragraph's first draft.
    #
    # KS3 loads none of these (checked: zero references in the built ks3/
    # tree), so build_ks3.py's VERSIONED_ASSETS is unchanged.
    #
    # ⊕ MRB-290 (25 Aug 2026) — the hand-maintained list is GONE. It had
    # grown by exactly the mechanism the paragraph above describes twice
    # over, and it was still one file short: `student-breakpoints.js`,
    # loaded by the two student preview pages, was never added, so those
    # two pages shipped it bare. The list is now every top-level .css/.js
    # in the published shared/ tree, so "add the file we happened to
    # touch" is structurally impossible. A file in shared/ that no page
    # links costs nothing here — the alternation simply never matches it.
    #
    # Longest-first, because the alternation below is ordered and a name
    # that prefixes another would otherwise mask it.
    _versioned_assets = sorted(
        [_fn for _fn in os.listdir(os.path.join(output_dir, "shared"))
         if _fn.endswith((".css", ".js"))
         and os.path.isfile(os.path.join(output_dir, "shared", _fn))],
        key=lambda _n: (-len(_n), _n))
    _asset_ver = {}
    for _name in _versioned_assets:
        _p = os.path.join(output_dir, "shared", _name)
        if os.path.exists(_p):
            with open(_p, "rb") as _fh:
                _asset_ver[_name] = _hashlib.md5(_fh.read()).hexdigest()[:8]
    if _asset_ver:
        _ver_pat = _re.compile(
            r'/shared/(' + '|'.join(_re.escape(n) for n in _asset_ver) + r')(?:\?v=[a-f0-9]+)?"'
        )
        def _stamp_versions(_html):
            return _ver_pat.sub(
                lambda m: f'/shared/{m.group(1)}?v={_asset_ver[m.group(1)]}"', _html
            )
        _stamped = 0
        for _root, _subdirs, _files in os.walk(output_dir):
            # Skip the foreign trees, for the same reason they are not wiped.
            # build_ks3.py owns its pages and stamps them itself at write time,
            # from the same source files by the same md5[:8] scheme, so the two
            # trees agree. Stamping them here as well would mean whichever
            # generator ran last decided the bytes of a KS3 page — and
            # build_ks3.py's determinism and reorder proofs compare KS3 output
            # byte for byte, so a foreign writer makes both unreliable.
            # One tree, one writer.
            #
            # Pruning _subdirs is what stops os.walk descending at all, rather
            # than testing every directory it reaches on the way down.
            if os.path.abspath(_root) == os.path.abspath(output_dir):
                for _d in FOREIGN_OUTPUT_DIRS:
                    if _d in _subdirs:
                        _subdirs.remove(_d)
            for _fn in _files:
                if not _fn.endswith(".html"):
                    continue
                _fp = os.path.join(_root, _fn)
                with open(_fp, "r", encoding="utf-8") as _fh:
                    _content = _fh.read()
                _new = _stamp_versions(_content)
                if _new != _content:
                    with open(_fp, "w", encoding="utf-8") as _fh:
                        _fh.write(_new)
                    _stamped += 1
        print(f"  ✅ cache-bust: stamped {_stamped} pages — {_asset_ver}")

        # ⊕ MRB-290 (25 Aug 2026) — the stamps are VERIFIED, not trusted.
        # Ported from build_student_port._verify_stamps, which explains why
        # each check exists. Three assertions, and a failure is a dead build,
        # not a warning — a stamp naming bytes that are not what will be
        # served is worse than no stamp at all:
        #
        #   1. every stamp equals md5[:8] of the published shared/ copy,
        #      re-read from disk after everything that writes it has run;
        #   2. where a repo-root shared/ source exists, it agrees — the two
        #      trees are round-tripped and must not diverge;
        #   3. no quote-terminated `/shared/…"` reference survives in any
        #      built page without a stamp. Anchored on the trailing quote,
        #      exactly like the stamping regex above, so this verifies
        #      precisely what that pass could have stamped — and prose
        #      mentions of /shared/ paths inside comments (revision.html,
        #      auth.html and friends carry several) cannot false-positive.
        #      The stamp group is OPTIONAL-and-tested, never a negative
        #      lookahead — see build_student_port.py for the twelve-page
        #      false alarm the lookahead produced.
        #
        # Runs BEFORE the repo-root round-trip below, so an unstamped page
        # can never reach the mirror.
        _bad_stamps = []
        for _name, _want in sorted(_asset_ver.items()):
            for _tree in (os.path.join(output_dir, "shared"), "shared"):
                _p = os.path.join(_tree, _name)
                if not os.path.exists(_p):
                    continue  # only files present in a tree are checked
                with open(_p, "rb") as _fh:
                    _got = _hashlib.md5(_fh.read()).hexdigest()[:8]
                if _got != _want:
                    _bad_stamps.append(
                        "%s hashes %s but pages shipped ?v=%s" % (_p, _got, _want))
        _linked = _re.compile(r'/shared/[A-Za-z0-9._/-]+(\?v=[0-9a-f]+)?"')
        for _root, _subdirs, _files in os.walk(output_dir):
            if os.path.abspath(_root) == os.path.abspath(output_dir):
                for _d in FOREIGN_OUTPUT_DIRS:
                    if _d in _subdirs:
                        _subdirs.remove(_d)
            for _fn in _files:
                if not _fn.endswith(".html"):
                    continue
                _fp = os.path.join(_root, _fn)
                with open(_fp, "r", encoding="utf-8") as _fh:
                    _content = _fh.read()
                for _m in _linked.finditer(_content):
                    if _m.group(1):
                        continue
                    _ref = _m.group(0).rstrip('"')[len("/shared/"):]
                    # Only top-level .css/.js are versioned: the stamping
                    # regex alternates over BASENAMES, so a subdirectory ref
                    # (/shared/fonts/…) could never be stamped by it and a
                    # non-css/js asset (woff2 preloads) is not versioned.
                    # Verify exactly what the pass could have stamped.
                    if "/" in _ref or not _ref.endswith((".css", ".js")):
                        continue
                    _bad_stamps.append(
                        "%s links %s with no cache-bust stamp" % (_fp, _m.group(0)))
        if _bad_stamps:
            raise SystemExit(
                "generate_site_v5.py: the cache-bust stamps are not honest.\n  "
                + "\n  ".join(_bad_stamps))
        print(f"  ✅ cache-bust: verified — every stamped asset re-hashed from "
              f"disk, no bare /shared/ link in {output_dir}")

    # ── Copy to repo root ──
    for item in os.listdir(output_dir):
        s = os.path.join(output_dir, item)
        d = os.path.join(".", item)
        if item in ['3d', '.git', 'generate_site_v5.py', 'generate_site.py',
                    'all_subtopics_physics.py', 'all_subtopics_chemistry.py',
                    'all_subtopics_biology.py']:
            continue
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    print(f"\n🎉 Done! {total_pages} pages generated")
    print(f"\nStructure:")
    print(f"  Landing → Combined/Triple → Foundation/Higher → Subject → Topics → Subtopics")
    print(f"\nNext steps:")
    print(f"  1. python3 generate_site_v5.py")
    print(f"  2. Check output in {output_dir}/")
    print(f"  3. Push to GitHub → Cloudflare auto-deploys")

    # A 3D Studio warning raised hundreds of lines ago has scrolled off the
    # screen by now. Say it again, last, where it is the thing still on screen
    # when the run finishes. Still not fatal: KS3 and KS4 are unaffected, and a
    # Node problem must never be able to fail this build.
    if _studio_alarm:
        _shout(_studio_alarm)


if __name__ == "__main__":
    # ⊕ MRB-271 — BUILD YOUR OWN TREE, NEVER SOMEBODY ELSE'S.
    #
    # Every path in this file is relative, and a relative path resolves against
    # the CURRENT DIRECTORY, not against this script. So
    # `python3 /elsewhere/generate_site_v5.py` run from inside a worktree imported
    # /elsewhere's modules and wrote the output into the WORKTREE — one tree's
    # source, another tree's deploy directory, and `generate_site_v5.build_site()`
    # opens by deleting most of what it finds there.
    #
    # With four worktrees live (see docs/ks3/worktrees.md) that stopped being
    # hypothetical. Anchoring to the script's own directory makes the invocation
    # path irrelevant: this file always builds the checkout it is part of.
    #
    # `__main__` only. Importing this module must NOT move the caller's cwd —
    # verify_ks3.py imports it and builds into its own scratch directories.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    build_site()

