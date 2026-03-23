#!/usr/bin/env python3
"""
MrBadmusAI — Full Site Generator
Run: python3 generate_site.py
Output: ./mrbadmus_site/ (ready to deploy on Netlify)
"""

import os, shutil, json

# ─────────────────────────────────────────────
#  SITE DATA — all topics, subtopics, equations,
#  required practicals, flags
# ─────────────────────────────────────────────

SITE_DATA = {
    "physics": {
        "label": "Physics",
        "emoji": "⚡",
        "color": "#4ECDC4",
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
        "color": "#FF6B6B",
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
        "color": "#6BCB77",
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

# v5 structural additions below
SHARED_CSS = r"""/* MrBadmusAI — Global Design System */
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@400;600;700;800&display=swap');

:root {
  --physics: #4ECDC4;
  --chemistry: #FF6B6B;
  --biology: #6BCB77;
  --yellow: #FFD93D;
  --orange: #FF6B35;
  --dark: #1A1A2E;
  --darker: #0F0F1A;
  --card: #16213E;
  --card2: #1A2545;
  --text: #E8F4FD;
  --muted: #8892A4;
  --radius: 12px;
  --shadow: 0 4px 20px rgba(0,0,0,0.4);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  font-family: 'Nunito', sans-serif;
  background: var(--darker);
  color: var(--text);
  min-height: 100vh;
  line-height: 1.6;
}

h1, h2, h3, .brand { font-family: 'Fredoka One', cursive; }

a { color: inherit; text-decoration: none; }

/* ── NAV ── */
.nav {
  background: var(--dark);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  padding: 0 24px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
}
.nav-brand {
  font-family: 'Fredoka One', cursive;
  font-size: 1.4rem;
  background: linear-gradient(135deg, var(--yellow), var(--orange));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.nav-links { display: flex; gap: 20px; align-items: center; }
.nav-links a {
  font-size: 0.85rem;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: 20px;
  transition: background 0.2s;
  opacity: 0.8;
}
.nav-links a:hover { background: rgba(255,255,255,0.1); opacity: 1; }
.nav-links a.active { background: rgba(255,255,255,0.15); opacity: 1; }
.nav-links a.phy { color: var(--physics); }
.nav-links a.che { color: var(--chemistry); }
.nav-links a.bio { color: var(--biology); }

/* ── HERO ── */
.hero {
  padding: 80px 24px;
  text-align: center;
  background: radial-gradient(ellipse at center, #1e2a4a 0%, var(--darker) 70%);
}
.hero h1 { font-size: clamp(2.2rem, 5vw, 4rem); margin-bottom: 16px; }
.hero p { font-size: 1.15rem; color: var(--muted); max-width: 600px; margin: 0 auto 40px; }
.hero-gradient { background: linear-gradient(135deg, var(--yellow), var(--orange)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }

/* ── SUBJECT CARDS (landing) ── */
.subject-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 28px;
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 24px 80px;
}
.subject-card {
  background: var(--card);
  border-radius: 20px;
  padding: 36px 28px;
  text-align: center;
  border: 2px solid transparent;
  transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
  cursor: pointer;
  display: block;
}
.subject-card:hover { transform: translateY(-6px); box-shadow: 0 12px 40px rgba(0,0,0,0.5); }
.subject-card.phy { border-color: var(--physics); }
.subject-card.che { border-color: var(--chemistry); }
.subject-card.bio { border-color: var(--biology); }
.subject-card:hover.phy { box-shadow: 0 12px 40px rgba(78,205,196,0.25); }
.subject-card:hover.che { box-shadow: 0 12px 40px rgba(255,107,107,0.25); }
.subject-card:hover.bio { box-shadow: 0 12px 40px rgba(107,203,119,0.25); }
.subject-icon { font-size: 3.5rem; margin-bottom: 16px; display: block; }
.subject-card h2 { font-size: 1.8rem; margin-bottom: 8px; }
.subject-card p { color: var(--muted); font-size: 0.95rem; margin-bottom: 20px; }
.subject-card .btn {
  display: inline-block;
  padding: 10px 28px;
  border-radius: 50px;
  font-weight: 800;
  font-size: 0.95rem;
  color: var(--darker);
  transition: opacity 0.2s;
}
.subject-card .btn:hover { opacity: 0.85; }
.phy .btn { background: var(--physics); }
.che .btn { background: var(--chemistry); }
.bio .btn { background: var(--biology); }

/* ── TOPIC HUB ── */
.hub-header {
  padding: 50px 24px 30px;
  text-align: center;
}
.hub-header h1 { font-size: 2.5rem; margin-bottom: 8px; }
.hub-header p { color: var(--muted); font-size: 1rem; }

.topic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px 80px;
}
.topic-card {
  background: var(--card);
  border-radius: var(--radius);
  padding: 24px;
  border-left: 4px solid transparent;
  transition: transform 0.2s, box-shadow 0.2s;
  display: block;
}
.topic-card:hover { transform: translateY(-4px); box-shadow: var(--shadow); }
.topic-card-head { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 12px; }
.topic-card h3 { font-size: 1.1rem; flex: 1; }
.topic-card-meta { color: var(--muted); font-size: 0.8rem; margin-bottom: 12px; }
.badge {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 20px;
  display: inline-block;
  margin: 2px;
  background: rgba(255,255,255,0.1);
}
.badge-rp { background: rgba(255,217,61,0.2); color: var(--yellow); }
.badge-h { background: rgba(78,205,196,0.2); color: var(--physics); }
.badge-t { background: rgba(255,107,107,0.15); color: #ff9999; }
.topic-card-footer { margin-top: 14px; }
.topic-card-footer .go-btn {
  font-size: 0.82rem;
  font-weight: 700;
  padding: 7px 18px;
  border-radius: 20px;
  color: var(--darker);
  display: inline-block;
}

/* ── TOPIC PAGE ── */
.topic-header {
  padding: 50px 24px 30px;
  max-width: 900px;
  margin: 0 auto;
}
.topic-header .back-link {
  font-size: 0.85rem;
  color: var(--muted);
  margin-bottom: 16px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: color 0.2s;
}
.topic-header .back-link:hover { color: var(--text); }
.topic-header h1 { font-size: 2.2rem; margin-bottom: 8px; }
.spec-pill {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 20px;
  background: rgba(255,255,255,0.1);
  color: var(--muted);
  margin-right: 8px;
}
.paper-pill {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 20px;
  background: rgba(255,217,61,0.15);
  color: var(--yellow);
}

.content-area {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 24px 120px;
}

.section { margin-bottom: 40px; }
.section-title {
  font-family: 'Fredoka One', cursive;
  font-size: 1.3rem;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.section-title::after {
  content: '';
  flex: 1;
  height: 2px;
  background: rgba(255,255,255,0.08);
  border-radius: 2px;
}

/* ── CARDS ── */
.card {
  background: var(--card);
  border-radius: var(--radius);
  padding: 24px;
  margin-bottom: 16px;
  border: 1px solid rgba(255,255,255,0.06);
}
.card h4 { font-size: 1rem; margin-bottom: 10px; font-weight: 800; }

/* ── FORMULA PILLS ── */
.formula-grid { display: flex; flex-wrap: wrap; gap: 10px; }
.formula-pill {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 8px;
  padding: 10px 18px;
  font-family: 'Courier New', monospace;
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 0.5px;
}

/* ── FIFA BOX ── */
.fifa-box {
  background: linear-gradient(135deg, #1a2a1a, #1e2e1e);
  border: 2px solid #4CAF50;
  border-radius: var(--radius);
  padding: 20px 24px;
  margin-bottom: 16px;
}
.fifa-box .fifa-title {
  font-family: 'Fredoka One', cursive;
  font-size: 1rem;
  color: #4CAF50;
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.fifa-step { display: flex; gap: 14px; margin-bottom: 10px; align-items: flex-start; }
.fifa-letter {
  font-family: 'Fredoka One', cursive;
  font-size: 1.1rem;
  width: 28px;
  height: 28px;
  border-radius: 6px;
  background: #4CAF50;
  color: #0F1A0F;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-top: 2px;
}
.fifa-step p { font-size: 0.95rem; }
.fifa-answer { font-size: 1.1rem; font-weight: 800; color: #80FF80; }

/* ── HIGHER / TRIPLE BOXES ── */
.higher-box {
  background: rgba(78,205,196,0.07);
  border: 2px solid rgba(78,205,196,0.4);
  border-radius: var(--radius);
  padding: 18px 22px;
  margin-bottom: 14px;
  position: relative;
}
.higher-box::before {
  content: '⭐ HIGHER TIER';
  font-size: 0.72rem;
  font-weight: 800;
  color: var(--physics);
  letter-spacing: 0.5px;
  display: block;
  margin-bottom: 8px;
}
.triple-box {
  background: rgba(255,107,107,0.07);
  border: 2px solid rgba(255,107,107,0.3);
  border-radius: var(--radius);
  padding: 18px 22px;
  margin-bottom: 14px;
  position: relative;
}
.triple-box::before {
  content: '🔬 TRIPLE ONLY';
  font-size: 0.72rem;
  font-weight: 800;
  color: var(--chemistry);
  letter-spacing: 0.5px;
  display: block;
  margin-bottom: 8px;
}

/* ── SUBTOPIC LIST ── */
.subtopic-list { list-style: none; display: flex; flex-direction: column; gap: 8px; }
.subtopic-list li {
  padding: 12px 16px;
  background: var(--card2);
  border-radius: 8px;
  font-size: 0.95rem;
  display: flex;
  align-items: center;
  gap: 10px;
  border-left: 3px solid rgba(255,255,255,0.1);
  transition: border-color 0.2s, background 0.2s;
}
.subtopic-list li:hover { background: rgba(255,255,255,0.05); }

/* ── RP SECTION ── */
.rp-card {
  background: rgba(255,217,61,0.06);
  border: 2px solid rgba(255,217,61,0.3);
  border-radius: var(--radius);
  padding: 20px 24px;
  margin-bottom: 12px;
}
.rp-card h4 { color: var(--yellow); font-size: 0.95rem; margin-bottom: 8px; }

/* ── QUIZ ── */
.quiz-card { background: var(--card); border-radius: var(--radius); padding: 24px; margin-bottom: 16px; }
.quiz-card .q-text { font-size: 1rem; font-weight: 700; margin-bottom: 14px; }
.quiz-options { display: flex; flex-direction: column; gap: 8px; }
.quiz-opt {
  padding: 11px 16px;
  background: var(--card2);
  border: 2px solid transparent;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 600;
  transition: border-color 0.15s, background 0.15s;
  text-align: left;
  color: var(--text);
}
.quiz-opt:hover { border-color: rgba(255,255,255,0.2); background: rgba(255,255,255,0.05); }
.quiz-opt.correct { border-color: #4CAF50; background: rgba(76,175,80,0.15); }
.quiz-opt.wrong { border-color: #f44336; background: rgba(244,67,54,0.15); }
.quiz-feedback { margin-top: 12px; font-size: 0.9rem; display: none; padding: 10px 14px; border-radius: 8px; }
.quiz-feedback.show { display: block; }
.quiz-feedback.correct-fb { background: rgba(76,175,80,0.15); color: #80FF80; }
.quiz-feedback.wrong-fb { background: rgba(244,67,54,0.15); color: #FF8080; }

/* ── CHAT FAB ── */
.chat-fab {
  position: fixed;
  bottom: 28px;
  right: 28px;
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--yellow), var(--orange));
  border: none;
  cursor: pointer;
  font-size: 1.8rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 28px rgba(255,107,53,0.5);
  transition: transform 0.2s, box-shadow 0.2s;
  z-index: 90;
}
.chat-fab:hover { transform: scale(1.08); box-shadow: 0 10px 40px rgba(255,107,53,0.7); }

/* ── CHAT OVERLAY ── */
.chat-overlay {
  position: fixed;
  inset: 0;
  background: var(--darker);
  z-index: 200;
  display: flex;
  flex-direction: column;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s;
}
.chat-overlay.open { pointer-events: all; opacity: 1; }
.chat-modal {
  width: 100%;
  height: 100%;
  background: var(--darker);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.chat-overlay.open .chat-modal { transform: none; }
.chat-head {
  padding: 16px 18px;
  background: linear-gradient(135deg, var(--yellow), var(--orange));
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.chat-head-info h3 { font-family: 'Fredoka One', cursive; font-size: 1.1rem; color: var(--darker); }
.chat-head-info p { font-size: 0.75rem; color: rgba(15,15,26,0.7); }
.close-btn { background: none; border: none; cursor: pointer; font-size: 1.4rem; color: var(--darker); line-height: 1; padding: 4px; }
.chat-msgs {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.chat-msg { display: flex; gap: 10px; align-items: flex-start; }
.chat-msg--user { flex-direction: row-reverse; }
.chat-msg__avatar {
  width: 32px; height: 32px;
  border-radius: 50%;
  background: rgba(255,255,255,0.1);
  display: flex; align-items: center; justify-content: center;
  font-size: 1rem; flex-shrink: 0;
}
.chat-msg__bubble {
  background: var(--card);
  padding: 12px 16px;
  border-radius: 14px;
  font-size: 0.88rem;
  line-height: 1.6;
  max-width: 80%;
}
.chat-msg--user .chat-msg__bubble { background: rgba(255,217,61,0.15); border-bottom-right-radius: 4px; }
.chat-msg--bot .chat-msg__bubble { border-bottom-left-radius: 4px; }
.typing span {
  display: inline-block;
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--muted);
  margin: 0 2px;
  animation: bounce 1.2s infinite;
}
.typing span:nth-child(2) { animation-delay: 0.2s; }
.typing span:nth-child(3) { animation-delay: 0.4s; }
@keyframes bounce { 0%,60%,100%{transform:translateY(0)} 30%{transform:translateY(-8px)} }

.img-preview-row { display: none; align-items: center; gap: 8px; padding: 8px 16px; background: var(--card); }
.img-preview-row img { height: 60px; border-radius: 8px; }
.img-preview-row button { background: none; border: none; color: var(--muted); cursor: pointer; font-size: 1.1rem; }

.chat-input-row {
  padding: 12px 16px;
  border-top: 1px solid rgba(255,255,255,0.08);
  display: flex;
  gap: 8px;
  align-items: center;
}
.chat-input-row input {
  flex: 1;
  background: var(--card);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 10px;
  padding: 10px 14px;
  color: var(--text);
  font-family: 'Nunito', sans-serif;
  font-size: 0.9rem;
  outline: none;
  transition: border-color 0.2s;
}
.chat-input-row input:focus { border-color: var(--yellow); }
.chat-input-row .img-btn, .chat-send-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.4rem;
  padding: 6px;
  border-radius: 8px;
  transition: background 0.2s;
}
.chat-send-btn {
  background: linear-gradient(135deg, var(--yellow), var(--orange));
  border-radius: 10px;
  font-size: 1.1rem;
  padding: 8px 14px;
}
.chat-send-btn:hover { opacity: 0.85; }

/* ── RESPONSIVE ── */
@media (max-width: 600px) {
  .nav-links a { padding: 5px 10px; font-size: 0.8rem; }
  .topic-grid { grid-template-columns: 1fr; }
  .subject-grid { grid-template-columns: 1fr; }
}
"""

# ─────────────────────────────────────────────
#  SHARED JS — from existing mrbadmus.js
# ─────────────────────────────────────────────

SHARED_JS = r"""/**
 * mrbadmus.js — Shared AI chat engine
 * Works across Physics, Chemistry, Biology
 */
window.MrBadmus = (function() {
  let chatInited = false, pendingImg = null, chatHistory = [], currentSubject = 'physics', currentTopic = '', systemPrompt = '';
  let studentName = null, studentProfile = null;

  // Load student name + profile from Supabase session (if logged in)
  function loadStudentSession() {
    try {
      const raw = localStorage.getItem('sb-urklkrwevjtlfbwnipjn-auth-token');
      if (!raw) return;
      const session = JSON.parse(raw);
      const user = session?.user;
      if (!user) return;
      studentName = user.user_metadata?.first_name || null;
      // Update chat header subtitle with name
      const subtitle = document.getElementById('chat-head-subtitle');
      if (subtitle && studentName) subtitle.textContent = 'Hey ' + studentName + '! 👋';
    } catch(e) {}
  }

  const BASE_PROMPT = `You are Mr. Badmus AI — an expert AQA GCSE Science teacher covering Physics, Chemistry and Biology (AQA 8463 / 8462 / 8461). You are warm, encouraging, and deeply knowledgeable.

CORE TEACHING RULES — ALWAYS FOLLOW:
1. Use the FIFA method for ALL calculations without exception:
   F = Formula (write it out)
   I = Insert values (substitute numbers + units)
   F = Fix (show any conversions or rearrangements)
   A = Answer (include the unit — always)
2. Always say "potential difference" not "voltage" in physics contexts
3. Always include units in every final answer
4. Show all working — never skip steps
5. Be encouraging and warm — students may be struggling
6. When a concept is tricky, use a real-life analogy first
7. Always state the AQA spec point if relevant (e.g. "AQA 4.2.1.3")
8. For higher tier content, label it clearly: ⭐ HIGHER TIER
9. For triple science only content, label it: 🔬 TRIPLE ONLY
10. Keep responses SHORT and punchy — 3 to 6 lines max unless doing a full FIFA example
11. Never start with a long introduction — get straight to the point
12. If a student just says hello or greets you, respond with ONE friendly line only — e.g. "Hey! What are we working on today? 🔥"
13. Never list topics unprompted — only show a list if the student asks "what can you help with"
14. Format clearly with line breaks — never write a wall of text
15. If a student is confused, offer to break it down — but keep the offer to one sentence
16. CRITICAL — You are a FULL GCSE Science tutor covering ALL THREE sciences. You MUST answer questions about Biology, Chemistry AND Physics regardless of which subject page the student is on. NEVER say "I'm only the Physics tutor" or refuse to answer Chemistry or Biology questions. If a student on a Physics page asks about photosynthesis, answer it fully. Always help with any AQA GCSE Science topic.`;

  const SUBJECT_PROMPTS = {
    physics: `${BASE_PROMPT}

CURRENT PAGE CONTEXT: AQA GCSE Physics (8463) — but answer ALL science subjects if asked

FULL PHYSICS SPECIFICATION TOPICS:
4.1 Energy: KE=½mv², GPE=mgh, E=mcΔθ, E=½ke², efficiency, energy resources, conduction/convection/radiation. RP1 specific heat capacity, RP2 insulation.
4.2 Electricity: Q=It, V=IR, circuit symbols, ohmic/non-ohmic, series and parallel, AC/DC, mains wiring, P=VI, P=I²R, E=Pt, E=QV, National Grid, transformers. RP3 resistance of wire, RP4 I-V characteristics. Higher: potential dividers. Triple: static electricity, electric fields.
4.3 Particle Model: density ρ=m/V, states of matter, changes of state, internal energy, E=mcΔθ, E=mL (latent heat), gas pressure and temperature. Higher: Boyle's law, absolute zero. RP5 density.
4.4 Atomic Structure: protons/neutrons/electrons, isotopes, atomic model history, radioactive decay (alpha/beta/gamma), nuclear equations, half-life, background radiation, fission/fusion. RP6 half-life sim.
4.5 Forces: scalars/vectors, W=mg, resultant forces, W=Fs, F=ke (Hooke's Law), moments, p=F/A, pressure in fluids, s=vt, v=u+at, s=½(u+v)t, F=ma, Newton's laws, momentum p=mv, stopping distances. Higher: impulse=FΔt, terminal velocity. RP7 acceleration, RP8 spring extension.
4.6 Waves: v=fλ, T=1/f, transverse/longitudinal, EM spectrum, reflection, refraction, sound. Higher: n=sin(i)/sin(r). Triple: lenses, X-rays, radio waves. RP9 waves, RP10 light.
4.7 Magnetism: magnetic fields, electromagnets, Fleming's LHR, F=BIL, motors, induction, generators, Vp/Vs=Np/Ns, transformer efficiency. Higher: induced EMF. RP11 motor effect.
4.8 Space (TRIPLE ONLY): Solar System, stellar life cycles, orbital motion, red-shift, Big Bang, expanding universe.

REQUIRED PRACTICALS: RP1-RP11 as listed above.
KEY EQUATIONS: All equation sheet equations apply.`,

    chemistry: `${BASE_PROMPT}

CURRENT PAGE CONTEXT: AQA GCSE Chemistry (8462) — but answer ALL science subjects if asked

FULL CHEMISTRY SPECIFICATION TOPICS:
4.1 Atomic Structure & Periodic Table: protons/neutrons/electrons, Ar, Mr, isotopes, electronic structure, periodic table groups/periods, Group 1 (alkali metals), Group 7 (halogens), Group 0 (noble gases), transition metals.
4.2 Bonding: ionic (electron transfer, giant lattice), covalent (electron sharing, simple molecular vs giant), metallic (delocalised electrons), alloys, polymers. Higher: dot-cross diagrams. Triple: intermolecular forces.
4.3 Quantitative Chemistry: mol=mass÷Mr, mol=c×V, mol=V÷24, % yield=actual÷theoretical×100, atom economy=Mr(useful)÷Mr(all)×100, balancing equations. Higher: limiting reactants, titration calcs.
4.4 Chemical Changes: reactivity series, displacement, metal extraction, pH scale, neutralisation, acid+metal→salt+H₂, acid+base→salt+H₂O, acid+carbonate→salt+H₂O+CO₂, making salts, electrolysis (molten and solutions). Higher: half equations. RP1 making salts, RP2 electrolysis.
4.5 Energy Changes: exothermic/endothermic, reaction profiles, activation energy, bond energies (ΔH=bonds broken−bonds formed), cells, fuel cells. Higher: bond energy calcs. RP3 temperature changes.
4.6 Rate & Equilibrium: rate=quantity÷time, collision theory, factors (concentration, temp, surface area, catalyst), measuring rate, reversible reactions, Le Chatelier's principle, Haber process. Higher: equilibrium position calculations. RP4 thiosulfate, RP5 marble chips.
4.7 Organic Chemistry: crude oil, fractional distillation, alkanes (CₙH₂ₙ₊₂), cracking, alkenes (CₙH₂ₙ), addition reactions, polymerisation, alcohols, carboxylic acids, esters. Higher: mechanisms. Triple: amino acids, condensation polymers. 
4.8 Chemical Analysis: pure substances, chromatography (Rf=spot÷solvent), flame tests, testing gases, ion tests, mass spectrometry, IR spectroscopy. Higher: interpreting spectra. RP6 chromatography, RP7 ion tests.
4.9 Atmosphere: composition, evolution of atmosphere, greenhouse effect, climate change, carbon footprint, pollutants (CO, NOₓ, SO₂, particulates).
4.10 Using Resources: finite/renewable, water treatment, LCA, corrosion, alloys, ceramics, polymers, composites, Haber process (N₂+3H₂⇌2NH₃), NPK fertilisers. Higher: fertiliser calculations. RP8 water purification.`,

    biology: `${BASE_PROMPT}

CURRENT PAGE CONTEXT: AQA GCSE Biology (8461) — but answer ALL science subjects if asked

FULL BIOLOGY SPECIFICATION TOPICS:
4.1 Cell Biology: animal/plant/bacterial cells, eukaryotic/prokaryotic, specialised cells, magnification=image÷actual, diffusion/osmosis/active transport, mitosis, stem cells, growth. Higher: meiosis, stem cell ethics. RP1 microscopy, RP2 osmosis.
4.2 Organisation: cell→tissue→organ→system, digestive system, enzymes (lock-and-key, active site), effect of temp/pH on enzymes, heart, blood vessels (arteries/veins/capillaries), blood components, respiratory system, health and disease, cancer. Higher: CHD treatments, plant transport. RP3 enzyme pH, RP4 food tests.
4.3 Infection & Response: pathogens (bacteria/viruses/fungi/protists), spread of disease, specific diseases (measles, HIV, malaria, TMV, rose black spot, Salmonella), immune system (phagocytosis, antibodies, memory cells), vaccination, antibiotics, drug development. Higher: monoclonal antibodies, plant defences.
4.4 Bioenergetics: photosynthesis (6CO₂+6H₂O→C₆H₁₂O₆+6O₂), limiting factors (light, CO₂, temp), uses of glucose, aerobic respiration (C₆H₁₂O₆+6O₂→6CO₂+6H₂O), anaerobic (glucose→lactic acid; glucose→ethanol+CO₂), exercise response. Higher: rate graphs, metabolism. RP5 photosynthesis, RP6 fermentation.
4.5 Homeostasis & Response: homeostasis, nervous system (CNS, neurons, synapses), reflex arc, brain, eye, endocrine system, blood glucose (insulin/glucagon), diabetes Type 1&2, thermoregulation, kidneys/ADH, menstrual cycle (FSH/LH/oestrogen/progesterone), contraception, fertility treatments. Higher: negative feedback, IVF ethics. Triple: kidney detail. RP7 reaction time.
4.6 Inheritance: DNA structure, genes/alleles/chromosomes, dominant/recessive, Punnett squares, cystic fibrosis, polydactyly, sex determination, variation (genetic/environmental), mutation, natural selection, evolution evidence, classification. Higher: codominance, genetic engineering. Triple: protein synthesis.
4.7 Ecology: populations/communities/ecosystems, abiotic/biotic factors, interdependence, food webs, competition, adaptations, quadrats/transects, water/carbon/nitrogen cycles, biodiversity, deforestation, climate change, conservation, mark-recapture formula. Higher: biodiversity index, predator-prey. RP8 habitat sampling.`
  };

  const FALLBACKS = {
    physics: [
      { k: ['potential difference','pd','voltage'], r: '<strong>Potential Difference (p.d.) — AQA 4.2.1.3</strong><br><br>P.d. is the energy transferred per unit charge. It\'s the "push" that drives current around the circuit.<br><br><strong>FIFA Example</strong> (find p.d. across 4Ω with 3A):<br>F — V = I × R<br>I — V = 3 × 4<br>F — No conversion needed<br>A — V = <strong>12 V</strong><br><br>Measured with a voltmeter connected <strong>in parallel</strong>.' },
      { k: ['ohm','v=ir','resistance','calculate'], r: '<strong>Ohm\'s Law — V = IR (AQA 4.2.1.3)</strong><br><br>FIFA Example (find current, V=12V, R=4Ω):<br>F — I = V ÷ R<br>I — I = 12 ÷ 4<br>F — No conversion<br>A — I = <strong>3 A</strong>' },
      { k: ['series'], r: '<strong>Series Circuit (AQA 4.2.2)</strong><br>• Current: same everywhere<br>• P.D.: splits between components<br>• Resistance: R_total = R₁ + R₂ + ...' },
      { k: ['parallel'], r: '<strong>Parallel Circuit (AQA 4.2.2)</strong><br>• P.D.: same across every branch<br>• Current: splits — I = I₁ + I₂<br>• Resistance: less than smallest branch' },
    ],
    chemistry: [
      { k: ['mole','mol','mr','mass'], r: '<strong>Moles (AQA Chem)</strong><br>mol = mass ÷ Mr<br><br>FIFA (2 mol CO₂, Mr=44):<br>F — mass = mol × Mr<br>I — mass = 2 × 44<br>F — None<br>A — mass = <strong>88 g</strong>' },
      { k: ['atom','proton','electron','neutron'], r: '<strong>Atomic Structure</strong><br>• Protons: +1, in nucleus<br>• Neutrons: 0, in nucleus<br>• Electrons: −1, in shells<br>Atomic number = protons. Mass number = protons + neutrons.' },
    ],
    biology: [
      { k: ['cell','nucleus','mitochondria'], r: '<strong>Cell Types</strong><br>Animal: nucleus, cytoplasm, membrane, mitochondria, ribosomes<br>Plant: all above + cell wall, chloroplasts, vacuole<br>Bacterial: cell wall, membrane, cytoplasm, ribosomes, plasmid, DNA loop (no nucleus)' },
      { k: ['photosynthesis'], r: '<strong>Photosynthesis</strong><br>6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂<br>Limiting factors: light intensity, CO₂, temperature' },
    ]
  };

  function getFallback(q, subject) {
    const lq = q.toLowerCase();
    const items = FALLBACKS[subject] || FALLBACKS.physics;
    for (const item of items) {
      if (item.k.some(k => lq.includes(k))) return item.r;
    }
    return `Great question! 😊 Ask me about a specific topic and I\'ll help. For unlimited live AI answers, the teacher can add the API key in server settings.`;
  }

  function addMsg(role, html) {
    const box = document.getElementById('chatMsgs');
    if (!box) return null;
    const d = document.createElement('div');
    d.className = `chat-msg chat-msg--${role}`;
    d.innerHTML = `<div class="chat-msg__avatar">${role==='user'?'🧑':'⚡'}</div><div class="chat-msg__bubble">${html}</div>`;
    box.appendChild(d);
    box.scrollTop = box.scrollHeight;
    return d;
  }

  function formatReply(text) {
    return text.replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/\*(.*?)\*/g,'<em>$1</em>').replace(/`(.*?)`/g,'<code>$1</code>').replace(/\n\n/g,'<br><br>').replace(/\n/g,'<br>');
  }

  function init(config) {
    currentSubject = config.subject || 'physics';
    currentTopic = config.topic || '';
    systemPrompt = SUBJECT_PROMPTS[currentSubject] || SUBJECT_PROMPTS.physics;
    if (currentTopic) systemPrompt += `\n\nThe student is currently studying: ${currentTopic}. Focus on this topic when possible.`;

    document.getElementById('chatOverlay')?.addEventListener('click', e => { if(e.target===document.getElementById('chatOverlay')) close(); });
    document.querySelector('.close-btn')?.addEventListener('click', close);
    document.querySelector('.chat-send-btn')?.addEventListener('click', () => ask());
    document.getElementById('ci')?.addEventListener('keydown', e => { if(e.key==='Enter') ask(); });
    document.getElementById('imgInput')?.addEventListener('change', () => handleImg(document.getElementById('imgInput')));
    document.querySelectorAll('.quick-q').forEach(btn => btn.addEventListener('click', () => ask(btn.dataset.q)));
    document.querySelectorAll('[data-open-chat]').forEach(el => el.addEventListener('click', open));
  }

  function open() {
    loadStudentSession();
    document.getElementById('chatOverlay')?.classList.add('open');
    if (!chatInited) {
      chatInited = true;
      const sn = {physics:'Physics ⚡',chemistry:'Chemistry 🧪',biology:'Biology 🌿'}[currentSubject];
      const greet = studentName
        ? "Hey " + studentName + "! 👋 I'm Mr Badmus — here to help you smash your GCSE Science. What are we stuck on?"
        : "Hey! 👋 I'm Mr Badmus — here to help you smash your GCSE Science. What are we stuck on?";
      addMsg('bot', greet);
    }
    setTimeout(() => document.getElementById('ci')?.focus(), 100);
  }

  function close() { document.getElementById('chatOverlay')?.classList.remove('open'); }

  function handleImg(input) {
    const file = input.files[0]; if (!file) return;
    const reader = new FileReader();
    reader.onload = e => {
      pendingImg = e.target.result;
      const row = document.getElementById('imgPreviewRow');
      const prev = document.getElementById('imgPreview');
      if (prev) prev.src = pendingImg;
      if (row) row.style.display = 'flex';
    };
    reader.readAsDataURL(file); input.value='';
  }

  function clearImg() {
    pendingImg = null;
    const prev = document.getElementById('imgPreview'), row = document.getElementById('imgPreviewRow');
    if (prev) prev.src=''; if (row) row.style.display='none';
  }

  async function ask(preset) {
    if (!chatInited) open();
    const input = document.getElementById('ci');
    const q = preset || (input ? input.value.trim() : '');
    const hasImg = !!pendingImg;
    if (!q && !hasImg) return;
    if (input) input.value = '';
    addMsg('user', (q||'Please answer this question:') + (hasImg ? `<br><img src="${pendingImg}" style="max-width:100%;border-radius:6px;margin-top:6px;display:block;" alt="question"/>` : ''));
    const imgData = pendingImg; clearImg();
    const t = addMsg('bot', '<div class="typing"><span></span><span></span><span></span></div>');
    let userContent = hasImg ? [{ type:'image', source:{ type:'base64', media_type:imgData.split(';')[0].split(':')[1], data:imgData.split(',')[1] }}, { type:'text', text:q||'Answer this GCSE Science question fully using FIFA for any calculations.' }] : q;
    chatHistory.push({ role:'user', content:userContent });
    try {
      const res = await fetch('/api/chat', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({ system:systemPrompt, messages:chatHistory }) });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      if (data.error) throw new Error(data.error.message);
      const reply = data.content?.map(c=>c.text||'').filter(Boolean).join('') || 'Sorry, no response.';
      if (t) t.querySelector('.chat-msg__bubble').innerHTML = formatReply(reply);
      chatHistory.push({ role:'assistant', content:reply });
      if (chatHistory.length > 20) chatHistory.splice(0,2);
    } catch(err) {
      chatHistory.pop();
      if (t) t.querySelector('.chat-msg__bubble').innerHTML = hasImg ? '⚠️ Image analysis needs a live connection. Type your question instead!' : getFallback(q, currentSubject);
    }
    document.getElementById('chatMsgs').scrollTop = 99999;
  }

  return { init, open, close, ask };
})();
"""

# ─────────────────────────────────────────────
#  NETLIFY FUNCTION
# ─────────────────────────────────────────────

NETLIFY_FUNCTION = """exports.handler = async function(event) {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
  };
  try {
    const body = JSON.parse(event.body || '{}');
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': process.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1000,
        system: body.system || '',
        messages: body.messages || [],
      }),
    });
    const data = await response.json();
    return { statusCode: 200, headers, body: JSON.stringify(data) };
  } catch (err) {
    return { statusCode: 500, headers, body: JSON.stringify({ error: { message: err.message } }) };
  }
};
"""

NETLIFY_TOML = """[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/:splat"
  status = 200
"""


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
    "combined": "#4ECDC4",   # teal
    "triple":   "#FF6B6B",   # red/pink
}

TIER_COLORS = {
    "foundation": "#6BCB77",  # green
    "higher":     "#FFD93D",  # yellow
}

PHYSICS_COLOR   = "#4ECDC4"
CHEMISTRY_COLOR = "#FF6B6B"
BIOLOGY_COLOR   = "#6BCB77"


# ─────────────────────────────────────────────
#  UPDATED NAV — includes pathway context
# ─────────────────────────────────────────────

def nav_html(active_subject="", pathway="", tier=""):
    """Nav bar — shows home, search icon, and optionally pathway breadcrumb."""
    pathway_links = ""
    if pathway and tier:
        pc = PATHWAY_COLORS.get(pathway, "#4ECDC4")
        tc = TIER_COLORS.get(tier, "#FFD93D")
        pathway_links = f"""
    <span style="color:var(--muted)">›</span>
    <a href="/{pathway}/index.html" style="color:{pc};font-weight:700;">{pathway.title()} Science</a>
    <span style="color:var(--muted)">›</span>
    <a href="/{pathway}/{tier}/index.html" style="color:{tc};font-weight:700;">{tier.title()}</a>"""
        if active_subject:
            sc = SITE_DATA[active_subject]["color"]
            sl = SITE_DATA[active_subject]["label"]
            se = SITE_DATA[active_subject]["emoji"]
            pathway_links += f"""
    <span style="color:var(--muted)">›</span>
    <a href="/{pathway}/{tier}/{active_subject}/index.html" style="color:{sc};font-weight:700;">{se} {sl}</a>"""
    elif pathway:
        pc = PATHWAY_COLORS.get(pathway, "#4ECDC4")
        pathway_links = f"""
    <span style="color:var(--muted)">›</span>
    <a href="/{pathway}/index.html" style="color:{pc};font-weight:700;">{pathway.title()} Science</a>"""

    return f"""<nav class="nav">
  <a class="nav-brand" href="/index.html">⚗️ MrBadmusAI</a>
  <div class="nav-links" style="display:flex;align-items:center;gap:8px;font-size:0.88rem;">
    <a href="/index.html" style="color:var(--muted);">Home</a>
    <a href="/index.html#siteSearch" title="Search topics" onclick="setTimeout(()=>document.getElementById('siteSearch')?.focus(),100)" style="color:var(--muted);font-size:1.1rem;text-decoration:none;">🔍</a>
    {pathway_links}
    <span id="nav-auth-area" style="margin-left:4px;display:flex;gap:6px;align-items:center;">
      <a href="/auth.html?tab=signup" style="border:2px solid #4ECDC4;color:#4ECDC4;padding:5px 12px;border-radius:20px;font-weight:800;font-size:0.82rem;text-decoration:none;white-space:nowrap;">Sign Up</a>
      <a href="/auth.html?tab=signin" style="background:linear-gradient(135deg,#4ECDC4,#38a89d);color:#0F0F1A;padding:6px 14px;border-radius:20px;font-weight:800;font-size:0.82rem;text-decoration:none;white-space:nowrap;">Sign In</a>
    </span>
  </div>
</nav>
<script>
(function(){{
  const SUPA_URL = 'https://urklkrwevjtlfbwnipjn.supabase.co';
  const SUPA_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVya2xrcndldmp0bGZid25pcGpuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQxOTQyNzksImV4cCI6MjA4OTc3MDI3OX0.pW9AP6TPlKC_XHDTbrEKrEGmGXglN0z5b0KGXD2oHvg';
  // Lightweight session check using localStorage (Supabase stores session here)
  try {{
    const raw = localStorage.getItem('sb-urklkrwevjtlfbwnipjn-auth-token');
    if (raw) {{
      const session = JSON.parse(raw);
      const user = session?.user;
      if (user) {{
        const firstName = user.user_metadata?.first_name || user.email?.split('@')[0] || 'You';
        const area = document.getElementById('nav-auth-area');
        if (area) area.innerHTML = '<a href="/profile-setup.html" style="color:#4ECDC4;font-weight:800;font-size:0.82rem;text-decoration:none;white-space:nowrap;">👤 ' + firstName + '</a>';
      }}
    }}
  }} catch(e) {{}}
}})();
</script>"""


# ─────────────────────────────────────────────
#  UPDATED CHAT — with Talk feature (voice in + TTS)
# ─────────────────────────────────────────────

def chat_html():
    return """<button class="chat-fab" onclick="MrBadmus.open()" title="Ask Mr Badmus AI">🤖</button>

<div class="chat-overlay" id="chatOverlay">
  <div class="chat-modal">
    <div class="chat-head">
      <div class="chat-head-left">
        <button class="chat-head-back" onclick="MrBadmus.close()">← Back</button>
        <div class="chat-head-info">
          <h3>Mr. Badmus AI</h3>
          <p id="chat-head-subtitle">GCSE Science Tutor</p>
        </div>
      </div>
      <button class="close-btn" onclick="MrBadmus.close()">✕</button>
    </div>
    <div class="chat-msgs" id="chatMsgs"></div>
    <div class="img-preview-row" id="imgPreviewRow">
      <img id="imgPreview" src="" alt="preview"/>
      <button onclick="document.getElementById(\'imgPreview\').src=\'\';document.getElementById(\'imgPreviewRow\').style.display=\'none\';">✕</button>
    </div>
    <div class="chat-input-row" style="max-width:860px;width:100%;margin:0 auto;padding:0 24px 20px;">
      <label for="imgInput" class="img-btn" title="Upload image">📷</label>
      <input type="file" id="imgInput" accept="image/*" style="display:none"/>
      <input type="text" id="ci" placeholder="Ask Mr Badmus anything..."/>
      <button class="chat-send-btn">➤</button>
    </div>
  </div>
</div>"""



# ─────────────────────────────────────────────
#  UPDATED SHARED JS — adds TTS + Voice Input
# ─────────────────────────────────────────────

# Extract original SHARED_JS and patch it — we inject TTS/voice at the end of the module
# The patched JS is appended to the SHARED_JS string already defined above.

SHARED_JS_PATCHED = SHARED_JS  # no voice patch



# Also add voice button CSS to SHARED_CSS
SHARED_CSS_PATCHED = SHARED_CSS + """


/* ── PATHWAY CARDS (landing) ── */
.pathway-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  max-width: 900px;
  margin: 40px auto;
  padding: 0 24px;
}
@media (max-width: 600px) { .pathway-grid { grid-template-columns: 1fr; } }

.pathway-card {
  background: var(--card);
  border-radius: 18px;
  padding: 36px 28px;
  text-align: center;
  text-decoration: none;
  border: 2px solid rgba(255,255,255,0.08);
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
  display: block;
}
.pathway-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}
.pathway-card.combined { border-color: rgba(78,205,196,0.4); }
.pathway-card.combined:hover { border-color: #4ECDC4; box-shadow: 0 12px 40px rgba(78,205,196,0.2); }
.pathway-card.triple { border-color: rgba(255,107,107,0.4); }
.pathway-card.triple:hover { border-color: #FF6B6B; box-shadow: 0 12px 40px rgba(255,107,107,0.2); }

.pathway-icon { font-size: 3rem; margin-bottom: 12px; }
.pathway-card h2 { font-size: 1.6rem; margin-bottom: 10px; }
.pathway-card p { font-size: 0.9rem; color: var(--muted); line-height: 1.6; margin-bottom: 20px; }
.pathway-badge-row { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
.pathway-badge { padding: 4px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 700; }

/* ── TIER CARDS ── */
.tier-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  max-width: 700px;
  margin: 40px auto;
  padding: 0 24px;
}
@media (max-width: 500px) { .tier-grid { grid-template-columns: 1fr; } }

.tier-card {
  background: var(--card);
  border-radius: 16px;
  padding: 32px 24px;
  text-align: center;
  text-decoration: none;
  border: 2px solid rgba(255,255,255,0.08);
  transition: transform 0.2s, box-shadow 0.2s;
  display: block;
}
.tier-card:hover { transform: translateY(-3px); }
.tier-card.foundation { border-color: rgba(107,203,119,0.4); }
.tier-card.foundation:hover { border-color: #6BCB77; box-shadow: 0 8px 30px rgba(107,203,119,0.2); }
.tier-card.higher { border-color: rgba(255,217,61,0.4); }
.tier-card.higher:hover { border-color: #FFD93D; box-shadow: 0 8px 30px rgba(255,217,61,0.2); }

/* ── SUBJECT CARDS inside pathway ── */
.subject-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  max-width: 900px;
  margin: 32px auto;
  padding: 0 24px;
}
@media (max-width: 700px) { .subject-row { grid-template-columns: 1fr; } }

/* ── NEXT/PREV NAVIGATION ── */
.subtopic-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 32px 0 16px;
  gap: 12px;
  flex-wrap: wrap;
}
.nav-arrow {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: var(--card);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 10px;
  text-decoration: none;
  color: var(--text);
  font-size: 0.88rem;
  font-weight: 700;
  transition: all 0.2s;
  max-width: 45%;
}
.nav-arrow:hover { border-color: var(--subject); color: var(--subject); background: rgba(255,255,255,0.04); }
.nav-arrow.prev::before { content: '←'; }
.nav-arrow.next::after  { content: '→'; }
.nav-arrow-label { font-size: 0.75rem; color: var(--muted); font-weight: 400; }
.nav-arrow-title { font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 180px; }
.subtopic-nav-spacer { flex: 1; }

/* ── BREADCRUMB BAR ── */
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.8rem;
  color: var(--muted);
  padding: 8px 0 4px;
  flex-wrap: wrap;
}
.breadcrumb a { color: var(--muted); text-decoration: none; }
.breadcrumb a:hover { color: var(--text); }
.breadcrumb .sep { opacity: 0.4; }
"""


# ─────────────────────────────────────────────
#  PAGE SHELL — uses SHARED_CSS_PATCHED
# ─────────────────────────────────────────────

def page_shell(title, subject, body_html, topic_id="", topic_title="", pathway="", tier=""):
    color = SITE_DATA[subject]["color"] if subject else "#4ECDC4"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} | MrBadmusAI</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
  <style>
    :root {{ --subject: {color}; }}
    .topic-card {{ border-left-color: var(--subject); }}
    .section-title {{ color: var(--subject); }}
    .go-btn {{ background: var(--subject); }}
    .spec-pill {{ border-color: var(--subject); }}
  </style>
</head>
<body>
  {nav_html(subject, pathway, tier)}
  {body_html}
  {chat_html()}
  <script src="/shared/mrbadmus.js"></script>
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
#  LANDING PAGE — new structure
# ─────────────────────────────────────────────

def make_landing():
    body = """
<section class="hero">
  <h1>Welcome to <span class="hero-gradient">MrBadmusAI</span></h1>
  <p>Your GCSE Science revision hub — Physics, Chemistry &amp; Biology. Choose your course below.</p>
  <div class="hero-search">
    <input type="text" id="siteSearch" placeholder="🔍 Search topics e.g. 'photosynthesis', 'forces'..." autocomplete="off"/>
    <div id="searchResults" class="search-results"></div>
  </div>
</section>

<div class="pathway-grid">

  <a class="pathway-card combined" href="/combined/index.html">
    <div class="pathway-icon">🔬</div>
    <h2 style="color:#4ECDC4">Combined Science</h2>
    <p>Covers Biology, Chemistry and Physics for the Combined Science qualification. Includes Foundation and Higher tiers.</p>
    <div class="pathway-badge-row">
      <span class="pathway-badge" style="background:rgba(107,203,119,0.2);color:#6BCB77;">Foundation</span>
      <span class="pathway-badge" style="background:rgba(255,217,61,0.2);color:#FFD93D;">Higher</span>
    </div>
    <div style="margin-top:20px;">
      <span style="background:#4ECDC4;color:#0F0F1A;padding:8px 20px;border-radius:20px;font-size:0.85rem;font-weight:800;">Start Combined Science →</span>
    </div>
  </a>

  <a class="pathway-card triple" href="/triple/index.html">
    <div class="pathway-icon">⚗️</div>
    <h2 style="color:#FF6B6B">Triple Science</h2>
    <p>Separate Biology, Chemistry and Physics qualifications with extended content. Foundation and Higher tiers.</p>
    <div class="pathway-badge-row">
      <span class="pathway-badge" style="background:rgba(107,203,119,0.2);color:#6BCB77;">Foundation</span>
      <span class="pathway-badge" style="background:rgba(255,217,61,0.2);color:#FFD93D;">Higher</span>
    </div>
    <div style="margin-top:20px;">
      <span style="background:#FF6B6B;color:#0F0F1A;padding:8px 20px;border-radius:20px;font-size:0.85rem;font-weight:800;">Start Triple Science →</span>
    </div>
  </a>

</div>

<style>
.hero-search { max-width:560px;margin:24px auto 0;position:relative; }
.hero-search input { width:100%;padding:14px 20px;border-radius:50px;border:2px solid rgba(255,255,255,0.15);background:rgba(255,255,255,0.07);color:var(--text);font-family:'Nunito',sans-serif;font-size:1rem;outline:none;transition:border-color 0.2s; }
.hero-search input:focus { border-color:#4ECDC4; }
.search-results { position:absolute;top:calc(100% + 8px);left:0;right:0;background:var(--card);border:1px solid rgba(255,255,255,0.12);border-radius:14px;max-height:320px;overflow-y:auto;z-index:200;display:none; }
.search-results.open { display:block; }
.search-result-item { padding:12px 18px;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.06);font-size:0.9rem;display:flex;align-items:center;gap:10px; }
.search-result-item:last-child { border-bottom:none; }
.search-result-item:hover { background:rgba(255,255,255,0.05); }
.search-result-subject { font-size:0.72rem;padding:2px 8px;border-radius:10px;font-weight:700;flex-shrink:0; }
</style>

<script>
(function() {
  // Quick search index — pathway links for Combined Higher as default deep link
  const INDEX = [

    {t:'Atoms, Elements and Compounds',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/atoms-elements-compounds.html',c:'#FF6B6B'},
    {t:'Mixtures and Separation Techniques',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/mixtures.html',c:'#FF6B6B'},
    {t:'Development of the Model of the Atom',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/model-of-the-atom.html',c:'#FF6B6B'},
    {t:'Subatomic Particles',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/subatomic-particles.html',c:'#FF6B6B'},
    {t:'Relative Atomic Mass and Isotopes',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/relative-atomic-mass.html',c:'#FF6B6B'},
    {t:'Electronic Structure',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/electronic-structure.html',c:'#FF6B6B'},
    {t:'The Periodic Table',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/periodic-table.html',c:'#FF6B6B'},
    {t:'Development of the Periodic Table',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/development-periodic-table.html',c:'#FF6B6B'},
    {t:'Metals and Non-metals',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/metals-non-metals.html',c:'#FF6B6B'},
    {t:'Group 0 — Noble Gases',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/group-0.html',c:'#FF6B6B'},
    {t:'Group 1 — Alkali Metals',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/group-1.html',c:'#FF6B6B'},
    {t:'Group 7 — Halogens',s:'Chemistry',url:'/combined/higher/chemistry/atomic-structure/group-7.html',c:'#FF6B6B'},
    {t:'Chemical Bonds',s:'Chemistry',url:'/combined/higher/chemistry/bonding/chemical-bonds.html',c:'#FF6B6B'},
    {t:'Ionic Bonding',s:'Chemistry',url:'/combined/higher/chemistry/bonding/ionic-bonding.html',c:'#FF6B6B'},
    {t:'Ionic Compounds',s:'Chemistry',url:'/combined/higher/chemistry/bonding/ionic-compounds.html',c:'#FF6B6B'},
    {t:'Covalent Bonding',s:'Chemistry',url:'/combined/higher/chemistry/bonding/covalent-bonding.html',c:'#FF6B6B'},
    {t:'Metallic Bonding',s:'Chemistry',url:'/combined/higher/chemistry/bonding/metallic-bonding.html',c:'#FF6B6B'},
    {t:'States of Matter and State Symbols',s:'Chemistry',url:'/combined/higher/chemistry/bonding/states-of-matter.html',c:'#FF6B6B'},
    {t:'Properties of Ionic Compounds',s:'Chemistry',url:'/combined/higher/chemistry/bonding/properties-ionic-compounds.html',c:'#FF6B6B'},
    {t:'Properties of Small Molecules',s:'Chemistry',url:'/combined/higher/chemistry/bonding/properties-small-molecules.html',c:'#FF6B6B'},
    {t:'Polymers',s:'Chemistry',url:'/combined/higher/chemistry/bonding/polymers.html',c:'#FF6B6B'},
    {t:'Giant Covalent Structures',s:'Chemistry',url:'/combined/higher/chemistry/bonding/giant-covalent-structures.html',c:'#FF6B6B'},
    {t:'Properties of Metals and Alloys',s:'Chemistry',url:'/combined/higher/chemistry/bonding/metals-alloys.html',c:'#FF6B6B'},
    {t:'Nanoparticles',s:'Chemistry',url:'/combined/higher/chemistry/bonding/nanoparticles.html',c:'#FF6B6B'},
    {t:'Conservation of Mass and Balanced Equations',s:'Chemistry',url:'/combined/higher/chemistry/quantitative/conservation-of-mass.html',c:'#FF6B6B'},
    {t:'Relative Formula Mass',s:'Chemistry',url:'/combined/higher/chemistry/quantitative/relative-formula-mass.html',c:'#FF6B6B'},
    {t:'Mass Changes in Reactions',s:'Chemistry',url:'/combined/higher/chemistry/quantitative/mass-changes-reactions.html',c:'#FF6B6B'},
    {t:'Chemical Measurements',s:'Chemistry',url:'/combined/higher/chemistry/quantitative/chemical-measurements.html',c:'#FF6B6B'},
    {t:'Concentration of Solutions',s:'Chemistry',url:'/combined/higher/chemistry/quantitative/concentration-of-solutions.html',c:'#FF6B6B'},
    {t:'Reactivity of Metals and Metal Oxides',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/reactivity-series.html',c:'#FF6B6B'},
    {t:'Extraction of Metals and Reduction',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/extraction-of-metals.html',c:'#FF6B6B'},
    {t:'Oxidation and Reduction',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/oxidation-reduction.html',c:'#FF6B6B'},
    {t:'Reactions of Acids with Metals and Bases',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/reactions-of-acids.html',c:'#FF6B6B'},
    {t:'Making Salts and Neutralisation',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/salts-neutralisation.html',c:'#FF6B6B'},
    {t:'The pH Scale',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/ph-scale.html',c:'#FF6B6B'},
    {t:'The Process of Electrolysis',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/electrolysis-principles.html',c:'#FF6B6B'},
    {t:'Electrolysis of Molten Ionic Compounds',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/electrolysis-molten.html',c:'#FF6B6B'},
    {t:'Using Electrolysis to Extract Metals',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/electrolysis-extraction.html',c:'#FF6B6B'},
    {t:'Electrolysis of Aqueous Solutions',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/electrolysis-aqueous.html',c:'#FF6B6B'},
    {t:'Exothermic and Endothermic Reactions',s:'Chemistry',url:'/combined/higher/chemistry/energy-changes/exothermic-endothermic.html',c:'#FF6B6B'},
    {t:'Reaction Profiles',s:'Chemistry',url:'/combined/higher/chemistry/energy-changes/reaction-profiles.html',c:'#FF6B6B'},
    {t:'Rate of Reaction and Calculations',s:'Chemistry',url:'/combined/higher/chemistry/rates-equilibrium/calculating-rates.html',c:'#FF6B6B'},
    {t:'Factors Affecting Rate of Reaction',s:'Chemistry',url:'/combined/higher/chemistry/rates-equilibrium/factors-affecting-rate.html',c:'#FF6B6B'},
    {t:'Collision Theory and Activation Energy',s:'Chemistry',url:'/combined/higher/chemistry/rates-equilibrium/collision-theory.html',c:'#FF6B6B'},
    {t:'Catalysts',s:'Chemistry',url:'/combined/higher/chemistry/rates-equilibrium/catalysts.html',c:'#FF6B6B'},
    {t:'Reversible Reactions and Equilibrium',s:'Chemistry',url:'/combined/higher/chemistry/rates-equilibrium/reversible-reactions-equilibrium.html',c:'#FF6B6B'},
    {t:'Crude Oil, Hydrocarbons and Alkanes',s:'Chemistry',url:'/combined/higher/chemistry/organic/crude-oil-hydrocarbons.html',c:'#FF6B6B'},
    {t:'Fractional Distillation of Crude Oil',s:'Chemistry',url:'/combined/higher/chemistry/organic/fractional-distillation.html',c:'#FF6B6B'},
    {t:'Properties of Hydrocarbons',s:'Chemistry',url:'/combined/higher/chemistry/organic/properties-of-hydrocarbons.html',c:'#FF6B6B'},
    {t:'Cracking and Alkenes',s:'Chemistry',url:'/combined/higher/chemistry/organic/cracking-alkenes.html',c:'#FF6B6B'},
    {t:'Pure Substances',s:'Chemistry',url:'/combined/higher/chemistry/analysis/pure-substances.html',c:'#FF6B6B'},
    {t:'Formulations',s:'Chemistry',url:'/combined/higher/chemistry/analysis/formulations.html',c:'#FF6B6B'},
    {t:'Chromatography',s:'Chemistry',url:'/combined/higher/chemistry/analysis/chromatography.html',c:'#FF6B6B'},
    {t:'Testing for Gases',s:'Chemistry',url:'/combined/higher/chemistry/analysis/testing-for-gases.html',c:'#FF6B6B'},
    {t:'Composition of the Atmosphere',s:'Chemistry',url:'/combined/higher/chemistry/atmosphere/composition-of-atmosphere.html',c:'#FF6B6B'},
    {t:'The Earth\'s Early Atmosphere',s:'Chemistry',url:'/combined/higher/chemistry/atmosphere/early-atmosphere.html',c:'#FF6B6B'},
    {t:'Greenhouse Gases and Climate Change',s:'Chemistry',url:'/combined/higher/chemistry/atmosphere/greenhouse-gases.html',c:'#FF6B6B'},
    {t:'Atmospheric Pollutants from Fuels',s:'Chemistry',url:'/combined/higher/chemistry/atmosphere/atmospheric-pollutants.html',c:'#FF6B6B'},
    {t:'Using the Earth\'s Resources',s:'Chemistry',url:'/combined/higher/chemistry/using-resources/earths-resources.html',c:'#FF6B6B'},
    {t:'Potable Water and Water Treatment',s:'Chemistry',url:'/combined/higher/chemistry/using-resources/potable-water.html',c:'#FF6B6B'},
    {t:'Life Cycle Assessment',s:'Chemistry',url:'/combined/higher/chemistry/using-resources/life-cycle-assessment.html',c:'#FF6B6B'},
    {t:'Reducing Use of Resources',s:'Chemistry',url:'/combined/higher/chemistry/using-resources/reducing-use-of-resources.html',c:'#FF6B6B'},
    {t:'Moles',s:'Chemistry',url:'/combined/higher/chemistry/quantitative/moles.html',c:'#FF6B6B'},
    {t:'Amounts of Substances in Equations',s:'Chemistry',url:'/combined/higher/chemistry/quantitative/amounts-in-equations.html',c:'#FF6B6B'},
    {t:'Using Moles — Limiting Reactants',s:'Chemistry',url:'/combined/higher/chemistry/quantitative/using-moles-calculations.html',c:'#FF6B6B'},
    {t:'Strong and Weak Acids',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/strong-weak-acids.html',c:'#FF6B6B'},
    {t:'Half Equations for Electrode Reactions',s:'Chemistry',url:'/combined/higher/chemistry/chemical-changes/half-equations.html',c:'#FF6B6B'},
    {t:'Bond Energy Calculations',s:'Chemistry',url:'/combined/higher/chemistry/energy-changes/bond-energy-calculations.html',c:'#FF6B6B'},
    {t:'Effect of Conditions on Equilibrium',s:'Chemistry',url:'/combined/higher/chemistry/rates-equilibrium/effect-of-conditions-equilibrium.html',c:'#FF6B6B'},
    // Triple Chemistry Foundation
    {t:'Atoms, Elements and Compounds',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/atoms-elements-compounds.html',c:'#FF6B6B'},
    {t:'Mixtures and Separation Techniques',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/mixtures.html',c:'#FF6B6B'},
    {t:'Development of the Model of the Atom',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/model-of-the-atom.html',c:'#FF6B6B'},
    {t:'Subatomic Particles',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/subatomic-particles.html',c:'#FF6B6B'},
    {t:'Relative Atomic Mass, Atomic Number and Isotopes',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/relative-atomic-mass.html',c:'#FF6B6B'},
    {t:'Electronic Structure',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/electronic-structure.html',c:'#FF6B6B'},
    {t:'The Periodic Table',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/periodic-table.html',c:'#FF6B6B'},
    {t:'Development of the Periodic Table',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/development-periodic-table.html',c:'#FF6B6B'},
    {t:'Metals and Non-metals',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/metals-non-metals.html',c:'#FF6B6B'},
    {t:'Group 0 — Noble Gases',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/group-0.html',c:'#FF6B6B'},
    {t:'Group 1 — Alkali Metals',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/group-1.html',c:'#FF6B6B'},
    {t:'Group 7 — Halogens',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/group-7.html',c:'#FF6B6B'},
    {t:'Properties of Transition Metals',s:'Chemistry',url:'/triple/foundation/chemistry/atomic-structure/transition-metals.html',c:'#FF6B6B'},
    {t:'Chemical Bonds',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/chemical-bonds.html',c:'#FF6B6B'},
    {t:'Ionic Bonding',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/ionic-bonding.html',c:'#FF6B6B'},
    {t:'Ionic Compounds',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/ionic-compounds.html',c:'#FF6B6B'},
    {t:'Covalent Bonding',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/covalent-bonding.html',c:'#FF6B6B'},
    {t:'Metallic Bonding',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/metallic-bonding.html',c:'#FF6B6B'},
    {t:'States of Matter and State Symbols',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/states-of-matter.html',c:'#FF6B6B'},
    {t:'Structure and Properties of Ionic Compounds',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/properties-ionic-compounds.html',c:'#FF6B6B'},
    {t:'Structure and Properties of Small Molecules',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/properties-small-molecules.html',c:'#FF6B6B'},
    {t:'Polymers',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/polymers.html',c:'#FF6B6B'},
    {t:'Giant Covalent Structures',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/giant-covalent-structures.html',c:'#FF6B6B'},
    {t:'Properties of Metals and Alloys',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/metals-alloys.html',c:'#FF6B6B'},
    {t:'Nanoparticles',s:'Chemistry',url:'/triple/foundation/chemistry/bonding/nanoparticles.html',c:'#FF6B6B'},
    {t:'Conservation of Mass and Balanced Equations',s:'Chemistry',url:'/triple/foundation/chemistry/quantitative/conservation-of-mass.html',c:'#FF6B6B'},
    {t:'Relative Formula Mass',s:'Chemistry',url:'/triple/foundation/chemistry/quantitative/relative-formula-mass.html',c:'#FF6B6B'},
    {t:'Mass Changes in Reactions',s:'Chemistry',url:'/triple/foundation/chemistry/quantitative/mass-changes-reactions.html',c:'#FF6B6B'},
    {t:'Chemical Measurements',s:'Chemistry',url:'/triple/foundation/chemistry/quantitative/chemical-measurements.html',c:'#FF6B6B'},
    {t:'Percentage Yield',s:'Chemistry',url:'/triple/foundation/chemistry/quantitative/percentage-yield.html',c:'#FF6B6B'},
    {t:'Atom Economy',s:'Chemistry',url:'/triple/foundation/chemistry/quantitative/atom-economy.html',c:'#FF6B6B'},
    {t:'Concentration of Solutions',s:'Chemistry',url:'/triple/foundation/chemistry/quantitative/concentration-of-solutions.html',c:'#FF6B6B'},
    {t:'Reactivity of Metals and Metal Oxides',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/reactivity-series.html',c:'#FF6B6B'},
    {t:'Extraction of Metals and Reduction',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/extraction-of-metals.html',c:'#FF6B6B'},
    {t:'Oxidation and Reduction',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/oxidation-reduction.html',c:'#FF6B6B'},
    {t:'Reactions of Acids with Metals and Bases',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/reactions-of-acids.html',c:'#FF6B6B'},
    {t:'Making Salts and Neutralisation',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/salts-neutralisation.html',c:'#FF6B6B'},
    {t:'The pH Scale and Neutralisation',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/ph-scale.html',c:'#FF6B6B'},
    {t:'Titrations',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/titrations.html',c:'#FF6B6B'},
    {t:'The Process of Electrolysis',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/electrolysis-principles.html',c:'#FF6B6B'},
    {t:'Electrolysis of Molten Ionic Compounds',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/electrolysis-molten.html',c:'#FF6B6B'},
    {t:'Using Electrolysis to Extract Metals',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/electrolysis-extraction.html',c:'#FF6B6B'},
    {t:'Electrolysis of Aqueous Solutions',s:'Chemistry',url:'/triple/foundation/chemistry/chemical-changes/electrolysis-aqueous.html',c:'#FF6B6B'},
    {t:'Exothermic and Endothermic Reactions',s:'Chemistry',url:'/triple/foundation/chemistry/energy-changes/exothermic-endothermic.html',c:'#FF6B6B'},
    {t:'Reaction Profiles',s:'Chemistry',url:'/triple/foundation/chemistry/energy-changes/reaction-profiles.html',c:'#FF6B6B'},
    {t:'Cells and Batteries',s:'Chemistry',url:'/triple/foundation/chemistry/energy-changes/cells-and-batteries.html',c:'#FF6B6B'},
    {t:'Fuel Cells',s:'Chemistry',url:'/triple/foundation/chemistry/energy-changes/fuel-cells.html',c:'#FF6B6B'},
    {t:'Rate of Reaction and Calculations',s:'Chemistry',url:'/triple/foundation/chemistry/rates-equilibrium/calculating-rates.html',c:'#FF6B6B'},
    {t:'Factors Affecting the Rate of Reaction',s:'Chemistry',url:'/triple/foundation/chemistry/rates-equilibrium/factors-affecting-rate.html',c:'#FF6B6B'},
    {t:'Collision Theory and Activation Energy',s:'Chemistry',url:'/triple/foundation/chemistry/rates-equilibrium/collision-theory.html',c:'#FF6B6B'},
    {t:'Catalysts',s:'Chemistry',url:'/triple/foundation/chemistry/rates-equilibrium/catalysts.html',c:'#FF6B6B'},
    {t:'Reversible Reactions and Equilibrium',s:'Chemistry',url:'/triple/foundation/chemistry/rates-equilibrium/reversible-reactions-equilibrium.html',c:'#FF6B6B'},
    {t:'Crude Oil, Hydrocarbons and Alkanes',s:'Chemistry',url:'/triple/foundation/chemistry/organic/crude-oil-hydrocarbons.html',c:'#FF6B6B'},
    {t:'Fractional Distillation of Crude Oil',s:'Chemistry',url:'/triple/foundation/chemistry/organic/fractional-distillation.html',c:'#FF6B6B'},
    {t:'Properties of Hydrocarbons',s:'Chemistry',url:'/triple/foundation/chemistry/organic/properties-of-hydrocarbons.html',c:'#FF6B6B'},
    {t:'Cracking and Alkenes',s:'Chemistry',url:'/triple/foundation/chemistry/organic/cracking-alkenes.html',c:'#FF6B6B'},
    {t:'Structure and Formulae of Alkenes',s:'Chemistry',url:'/triple/foundation/chemistry/organic/structure-of-alkenes.html',c:'#FF6B6B'},
    {t:'Reactions of Alkenes',s:'Chemistry',url:'/triple/foundation/chemistry/organic/reactions-of-alkenes.html',c:'#FF6B6B'},
    {t:'Alcohols',s:'Chemistry',url:'/triple/foundation/chemistry/organic/alcohols.html',c:'#FF6B6B'},
    {t:'Carboxylic Acids',s:'Chemistry',url:'/triple/foundation/chemistry/organic/carboxylic-acids.html',c:'#FF6B6B'},
    {t:'Addition Polymerisation',s:'Chemistry',url:'/triple/foundation/chemistry/organic/addition-polymerisation.html',c:'#FF6B6B'},
    {t:'DNA and Other Naturally Occurring Polymers',s:'Chemistry',url:'/triple/foundation/chemistry/organic/dna-naturally-occurring-polymers.html',c:'#FF6B6B'},
    {t:'Pure Substances',s:'Chemistry',url:'/triple/foundation/chemistry/analysis/pure-substances.html',c:'#FF6B6B'},
    {t:'Formulations',s:'Chemistry',url:'/triple/foundation/chemistry/analysis/formulations.html',c:'#FF6B6B'},
    {t:'Chromatography',s:'Chemistry',url:'/triple/foundation/chemistry/analysis/chromatography.html',c:'#FF6B6B'},
    {t:'Testing for Gases',s:'Chemistry',url:'/triple/foundation/chemistry/analysis/testing-for-gases.html',c:'#FF6B6B'},
    {t:'Flame Tests',s:'Chemistry',url:'/triple/foundation/chemistry/analysis/flame-tests.html',c:'#FF6B6B'},
    {t:'Metal Hydroxides',s:'Chemistry',url:'/triple/foundation/chemistry/analysis/metal-hydroxides.html',c:'#FF6B6B'},
    {t:'Tests for Carbonates, Halides and Sulfates',s:'Chemistry',url:'/triple/foundation/chemistry/analysis/carbonates-halides-sulfates.html',c:'#FF6B6B'},
    {t:'Instrumental Methods and Flame Emission Spectroscopy',s:'Chemistry',url:'/triple/foundation/chemistry/analysis/instrumental-methods.html',c:'#FF6B6B'},
    {t:'The Composition of the Atmosphere',s:'Chemistry',url:'/triple/foundation/chemistry/atmosphere/composition-of-atmosphere.html',c:'#FF6B6B'},
    {t:'The Earth's Early Atmosphere and How It Changed',s:'Chemistry',url:'/triple/foundation/chemistry/atmosphere/early-atmosphere.html',c:'#FF6B6B'},
    {t:'Greenhouse Gases and Climate Change',s:'Chemistry',url:'/triple/foundation/chemistry/atmosphere/greenhouse-gases.html',c:'#FF6B6B'},
    {t:'Atmospheric Pollutants from Fuels',s:'Chemistry',url:'/triple/foundation/chemistry/atmosphere/atmospheric-pollutants.html',c:'#FF6B6B'},
    {t:'Using the Earth's Resources and Sustainable Development',s:'Chemistry',url:'/triple/foundation/chemistry/resources/earths-resources.html',c:'#FF6B6B'},
    {t:'Potable Water and Water Treatment',s:'Chemistry',url:'/triple/foundation/chemistry/resources/potable-water.html',c:'#FF6B6B'},
    {t:'Life Cycle Assessment',s:'Chemistry',url:'/triple/foundation/chemistry/resources/life-cycle-assessment.html',c:'#FF6B6B'},
    {t:'Ways of Reducing the Use of Resources',s:'Chemistry',url:'/triple/foundation/chemistry/resources/reducing-use-of-resources.html',c:'#FF6B6B'},
    {t:'Corrosion and Its Prevention',s:'Chemistry',url:'/triple/foundation/chemistry/resources/corrosion-prevention.html',c:'#FF6B6B'},
    {t:'Alloys as Useful Materials',s:'Chemistry',url:'/triple/foundation/chemistry/resources/alloys-useful-materials.html',c:'#FF6B6B'},
    {t:'Ceramics, Polymers and Composites',s:'Chemistry',url:'/triple/foundation/chemistry/resources/ceramics-polymers-composites.html',c:'#FF6B6B'},
    {t:'The Haber Process',s:'Chemistry',url:'/triple/foundation/chemistry/resources/haber-process.html',c:'#FF6B6B'},
    {t:'Production and Uses of NPK Fertilisers',s:'Chemistry',url:'/triple/foundation/chemistry/resources/npk-fertilisers.html',c:'#FF6B6B'},
    // Triple Chemistry Higher
    {t:'Atoms, Elements and Compounds',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/atoms-elements-compounds.html',c:'#FF6B6B'},
    {t:'Mixtures and Separation Techniques',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/mixtures.html',c:'#FF6B6B'},
    {t:'Development of the Model of the Atom',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/model-of-the-atom.html',c:'#FF6B6B'},
    {t:'Subatomic Particles',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/subatomic-particles.html',c:'#FF6B6B'},
    {t:'Relative Atomic Mass, Atomic Number and Isotopes',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/relative-atomic-mass.html',c:'#FF6B6B'},
    {t:'Electronic Structure',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/electronic-structure.html',c:'#FF6B6B'},
    {t:'The Periodic Table',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/periodic-table.html',c:'#FF6B6B'},
    {t:'Development of the Periodic Table',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/development-periodic-table.html',c:'#FF6B6B'},
    {t:'Metals and Non-metals',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/metals-non-metals.html',c:'#FF6B6B'},
    {t:'Group 0 — Noble Gases',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/group-0.html',c:'#FF6B6B'},
    {t:'Group 1 — Alkali Metals',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/group-1.html',c:'#FF6B6B'},
    {t:'Group 7 — Halogens',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/group-7.html',c:'#FF6B6B'},
    {t:'Properties of Transition Metals',s:'Chemistry',url:'/triple/higher/chemistry/atomic-structure/transition-metals.html',c:'#FF6B6B'},
    {t:'Chemical Bonds',s:'Chemistry',url:'/triple/higher/chemistry/bonding/chemical-bonds.html',c:'#FF6B6B'},
    {t:'Ionic Bonding',s:'Chemistry',url:'/triple/higher/chemistry/bonding/ionic-bonding.html',c:'#FF6B6B'},
    {t:'Ionic Compounds',s:'Chemistry',url:'/triple/higher/chemistry/bonding/ionic-compounds.html',c:'#FF6B6B'},
    {t:'Covalent Bonding',s:'Chemistry',url:'/triple/higher/chemistry/bonding/covalent-bonding.html',c:'#FF6B6B'},
    {t:'Metallic Bonding',s:'Chemistry',url:'/triple/higher/chemistry/bonding/metallic-bonding.html',c:'#FF6B6B'},
    {t:'States of Matter and State Symbols',s:'Chemistry',url:'/triple/higher/chemistry/bonding/states-of-matter.html',c:'#FF6B6B'},
    {t:'Structure and Properties of Ionic Compounds',s:'Chemistry',url:'/triple/higher/chemistry/bonding/properties-ionic-compounds.html',c:'#FF6B6B'},
    {t:'Structure and Properties of Small Molecules',s:'Chemistry',url:'/triple/higher/chemistry/bonding/properties-small-molecules.html',c:'#FF6B6B'},
    {t:'Polymers',s:'Chemistry',url:'/triple/higher/chemistry/bonding/polymers.html',c:'#FF6B6B'},
    {t:'Giant Covalent Structures',s:'Chemistry',url:'/triple/higher/chemistry/bonding/giant-covalent-structures.html',c:'#FF6B6B'},
    {t:'Properties of Metals and Alloys',s:'Chemistry',url:'/triple/higher/chemistry/bonding/metals-alloys.html',c:'#FF6B6B'},
    {t:'Nanoparticles',s:'Chemistry',url:'/triple/higher/chemistry/bonding/nanoparticles.html',c:'#FF6B6B'},
    {t:'Conservation of Mass and Balanced Equations',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/conservation-of-mass.html',c:'#FF6B6B'},
    {t:'Relative Formula Mass',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/relative-formula-mass.html',c:'#FF6B6B'},
    {t:'Mass Changes in Reactions',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/mass-changes-reactions.html',c:'#FF6B6B'},
    {t:'Chemical Measurements',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/chemical-measurements.html',c:'#FF6B6B'},
    {t:'Percentage Yield',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/percentage-yield.html',c:'#FF6B6B'},
    {t:'Atom Economy',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/atom-economy.html',c:'#FF6B6B'},
    {t:'Concentration of Solutions',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/concentration-of-solutions.html',c:'#FF6B6B'},
    {t:'Moles',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/moles.html',c:'#FF6B6B'},
    {t:'Amounts of Substances in Equations',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/amounts-in-equations.html',c:'#FF6B6B'},
    {t:'Using Moles — Calculations and Limiting Reactants',s:'Chemistry',url:'/triple/higher/chemistry/quantitative/using-moles-calculations.html',c:'#FF6B6B'},
    {t:'Reactivity of Metals and Metal Oxides',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/reactivity-series.html',c:'#FF6B6B'},
    {t:'Extraction of Metals and Reduction',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/extraction-of-metals.html',c:'#FF6B6B'},
    {t:'Oxidation and Reduction',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/oxidation-reduction.html',c:'#FF6B6B'},
    {t:'Reactions of Acids with Metals and Bases',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/reactions-of-acids.html',c:'#FF6B6B'},
    {t:'Making Salts and Neutralisation',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/salts-neutralisation.html',c:'#FF6B6B'},
    {t:'The pH Scale and Neutralisation',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/ph-scale.html',c:'#FF6B6B'},
    {t:'Titrations',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/titrations.html',c:'#FF6B6B'},
    {t:'The Process of Electrolysis',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/electrolysis-principles.html',c:'#FF6B6B'},
    {t:'Electrolysis of Molten Ionic Compounds',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/electrolysis-molten.html',c:'#FF6B6B'},
    {t:'Using Electrolysis to Extract Metals',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/electrolysis-extraction.html',c:'#FF6B6B'},
    {t:'Electrolysis of Aqueous Solutions',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/electrolysis-aqueous.html',c:'#FF6B6B'},
    {t:'Strong and Weak Acids',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/strong-weak-acids.html',c:'#FF6B6B'},
    {t:'Half Equations for Electrode Reactions',s:'Chemistry',url:'/triple/higher/chemistry/chemical-changes/half-equations.html',c:'#FF6B6B'},
    {t:'Exothermic and Endothermic Reactions',s:'Chemistry',url:'/triple/higher/chemistry/energy-changes/exothermic-endothermic.html',c:'#FF6B6B'},
    {t:'Reaction Profiles',s:'Chemistry',url:'/triple/higher/chemistry/energy-changes/reaction-profiles.html',c:'#FF6B6B'},
    {t:'Cells and Batteries',s:'Chemistry',url:'/triple/higher/chemistry/energy-changes/cells-and-batteries.html',c:'#FF6B6B'},
    {t:'Fuel Cells',s:'Chemistry',url:'/triple/higher/chemistry/energy-changes/fuel-cells.html',c:'#FF6B6B'},
    {t:'Bond Energy Calculations',s:'Chemistry',url:'/triple/higher/chemistry/energy-changes/bond-energy-calculations.html',c:'#FF6B6B'},
    {t:'Rate of Reaction and Calculations',s:'Chemistry',url:'/triple/higher/chemistry/rates-equilibrium/calculating-rates.html',c:'#FF6B6B'},
    {t:'Factors Affecting the Rate of Reaction',s:'Chemistry',url:'/triple/higher/chemistry/rates-equilibrium/factors-affecting-rate.html',c:'#FF6B6B'},
    {t:'Collision Theory and Activation Energy',s:'Chemistry',url:'/triple/higher/chemistry/rates-equilibrium/collision-theory.html',c:'#FF6B6B'},
    {t:'Catalysts',s:'Chemistry',url:'/triple/higher/chemistry/rates-equilibrium/catalysts.html',c:'#FF6B6B'},
    {t:'Reversible Reactions and Equilibrium',s:'Chemistry',url:'/triple/higher/chemistry/rates-equilibrium/reversible-reactions-equilibrium.html',c:'#FF6B6B'},
    {t:'Effect of Changing Conditions on Equilibrium',s:'Chemistry',url:'/triple/higher/chemistry/rates-equilibrium/effect-of-conditions-equilibrium.html',c:'#FF6B6B'},
    {t:'Crude Oil, Hydrocarbons and Alkanes',s:'Chemistry',url:'/triple/higher/chemistry/organic/crude-oil-hydrocarbons.html',c:'#FF6B6B'},
    {t:'Fractional Distillation of Crude Oil',s:'Chemistry',url:'/triple/higher/chemistry/organic/fractional-distillation.html',c:'#FF6B6B'},
    {t:'Properties of Hydrocarbons',s:'Chemistry',url:'/triple/higher/chemistry/organic/properties-of-hydrocarbons.html',c:'#FF6B6B'},
    {t:'Cracking and Alkenes',s:'Chemistry',url:'/triple/higher/chemistry/organic/cracking-alkenes.html',c:'#FF6B6B'},
    {t:'Structure and Formulae of Alkenes',s:'Chemistry',url:'/triple/higher/chemistry/organic/structure-of-alkenes.html',c:'#FF6B6B'},
    {t:'Reactions of Alkenes',s:'Chemistry',url:'/triple/higher/chemistry/organic/reactions-of-alkenes.html',c:'#FF6B6B'},
    {t:'Alcohols',s:'Chemistry',url:'/triple/higher/chemistry/organic/alcohols.html',c:'#FF6B6B'},
    {t:'Carboxylic Acids',s:'Chemistry',url:'/triple/higher/chemistry/organic/carboxylic-acids.html',c:'#FF6B6B'},
    {t:'Addition Polymerisation',s:'Chemistry',url:'/triple/higher/chemistry/organic/addition-polymerisation.html',c:'#FF6B6B'},
    {t:'Condensation Polymerisation',s:'Chemistry',url:'/triple/higher/chemistry/organic/condensation-polymerisation.html',c:'#FF6B6B'},
    {t:'Amino Acids',s:'Chemistry',url:'/triple/higher/chemistry/organic/amino-acids.html',c:'#FF6B6B'},
    {t:'DNA and Other Naturally Occurring Polymers',s:'Chemistry',url:'/triple/higher/chemistry/organic/dna-naturally-occurring-polymers.html',c:'#FF6B6B'},
    {t:'Pure Substances',s:'Chemistry',url:'/triple/higher/chemistry/analysis/pure-substances.html',c:'#FF6B6B'},
    {t:'Formulations',s:'Chemistry',url:'/triple/higher/chemistry/analysis/formulations.html',c:'#FF6B6B'},
    {t:'Chromatography',s:'Chemistry',url:'/triple/higher/chemistry/analysis/chromatography.html',c:'#FF6B6B'},
    {t:'Testing for Gases',s:'Chemistry',url:'/triple/higher/chemistry/analysis/testing-for-gases.html',c:'#FF6B6B'},
    {t:'Flame Tests',s:'Chemistry',url:'/triple/higher/chemistry/analysis/flame-tests.html',c:'#FF6B6B'},
    {t:'Metal Hydroxides',s:'Chemistry',url:'/triple/higher/chemistry/analysis/metal-hydroxides.html',c:'#FF6B6B'},
    {t:'Tests for Carbonates, Halides and Sulfates',s:'Chemistry',url:'/triple/higher/chemistry/analysis/carbonates-halides-sulfates.html',c:'#FF6B6B'},
    {t:'Instrumental Methods and Flame Emission Spectroscopy',s:'Chemistry',url:'/triple/higher/chemistry/analysis/instrumental-methods.html',c:'#FF6B6B'},
    {t:'The Composition of the Atmosphere',s:'Chemistry',url:'/triple/higher/chemistry/atmosphere/composition-of-atmosphere.html',c:'#FF6B6B'},
    {t:'The Earth\'s Early Atmosphere and How It Changed',s:'Chemistry',url:'/triple/higher/chemistry/atmosphere/early-atmosphere.html',c:'#FF6B6B'},
    {t:'Greenhouse Gases and Climate Change',s:'Chemistry',url:'/triple/higher/chemistry/atmosphere/greenhouse-gases.html',c:'#FF6B6B'},
    {t:'Atmospheric Pollutants from Fuels',s:'Chemistry',url:'/triple/higher/chemistry/atmosphere/atmospheric-pollutants.html',c:'#FF6B6B'},
    {t:'Using the Earth\'s Resources and Sustainable Development',s:'Chemistry',url:'/triple/higher/chemistry/resources/earths-resources.html',c:'#FF6B6B'},
    {t:'Potable Water and Water Treatment',s:'Chemistry',url:'/triple/higher/chemistry/resources/potable-water.html',c:'#FF6B6B'},
    {t:'Life Cycle Assessment',s:'Chemistry',url:'/triple/higher/chemistry/resources/life-cycle-assessment.html',c:'#FF6B6B'},
    {t:'Ways of Reducing the Use of Resources',s:'Chemistry',url:'/triple/higher/chemistry/resources/reducing-use-of-resources.html',c:'#FF6B6B'},
    {t:'Corrosion and Its Prevention',s:'Chemistry',url:'/triple/higher/chemistry/resources/corrosion-prevention.html',c:'#FF6B6B'},
    {t:'Alloys as Useful Materials',s:'Chemistry',url:'/triple/higher/chemistry/resources/alloys-useful-materials.html',c:'#FF6B6B'},
    {t:'Ceramics, Polymers and Composites',s:'Chemistry',url:'/triple/higher/chemistry/resources/ceramics-polymers-composites.html',c:'#FF6B6B'},
    {t:'The Haber Process',s:'Chemistry',url:'/triple/higher/chemistry/resources/haber-process.html',c:'#FF6B6B'},
    {t:'Production and Uses of NPK Fertilisers',s:'Chemistry',url:'/triple/higher/chemistry/resources/npk-fertilisers.html',c:'#FF6B6B'},
    {t:'Alternative Methods of Extracting Metals',s:'Chemistry',url:'/triple/higher/chemistry/resources/alternative-metal-extraction.html',c:'#FF6B6B'},
    {t:'Alternative Methods of Extracting Metals',s:'Chemistry',url:'/combined/higher/chemistry/using-resources/alternative-metal-extraction.html',c:'#FF6B6B'},
    {t:'Energy Stores and Systems',s:'Physics',url:'/combined/higher/physics/energy/energy-stores-systems.html',c:'#4ECDC4'},
    {t:'Changes in Energy',s:'Physics',url:'/combined/higher/physics/energy/changes-in-energy.html',c:'#4ECDC4'},
    {t:'Energy Changes in Systems',s:'Physics',url:'/combined/higher/physics/energy/energy-changes-in-systems.html',c:'#4ECDC4'},
    {t:'Power',s:'Physics',url:'/combined/higher/physics/energy/power.html',c:'#4ECDC4'},
    {t:'Energy Transfers in a System',s:'Physics',url:'/combined/higher/physics/energy/energy-transfers-in-a-system.html',c:'#4ECDC4'},
    {t:'Efficiency',s:'Physics',url:'/combined/higher/physics/energy/efficiency.html',c:'#4ECDC4'},
    {t:'Energy Resources',s:'Physics',url:'/combined/higher/physics/energy/energy-resources.html',c:'#4ECDC4'},
    {t:'Standard Circuit Diagram Symbols',s:'Physics',url:'/combined/higher/physics/electricity/circuit-symbols.html',c:'#4ECDC4'},
    {t:'Electrical Charge and Current',s:'Physics',url:'/combined/higher/physics/electricity/electrical-charge-current.html',c:'#4ECDC4'},
    {t:'Current, Resistance and Potential Difference',s:'Physics',url:'/combined/higher/physics/electricity/current-resistance-pd.html',c:'#4ECDC4'},
    {t:'Resistors',s:'Physics',url:'/combined/higher/physics/electricity/resistors.html',c:'#4ECDC4'},
    {t:'Series and Parallel Circuits',s:'Physics',url:'/combined/higher/physics/electricity/series-parallel-circuits.html',c:'#4ECDC4'},
    {t:'Direct and Alternating Potential Difference',s:'Physics',url:'/combined/higher/physics/electricity/direct-alternating-pd.html',c:'#4ECDC4'},
    {t:'Mains Electricity',s:'Physics',url:'/combined/higher/physics/electricity/mains-electricity.html',c:'#4ECDC4'},
    {t:'Power',s:'Physics',url:'/combined/higher/physics/electricity/power-electricity.html',c:'#4ECDC4'},
    {t:'Energy Transfers in Everyday Appliances',s:'Physics',url:'/combined/higher/physics/electricity/energy-transfers-appliances.html',c:'#4ECDC4'},
    {t:'The National Grid',s:'Physics',url:'/combined/higher/physics/electricity/national-grid.html',c:'#4ECDC4'},
    {t:'Density of Materials',s:'Physics',url:'/combined/higher/physics/particle-model/density-of-materials.html',c:'#4ECDC4'},
    {t:'Changes of State',s:'Physics',url:'/combined/higher/physics/particle-model/changes-of-state.html',c:'#4ECDC4'},
    {t:'Internal Energy',s:'Physics',url:'/combined/higher/physics/particle-model/internal-energy.html',c:'#4ECDC4'},
    {t:'Temperature Changes and Specific Heat Capacity',s:'Physics',url:'/combined/higher/physics/particle-model/temperature-changes-shc.html',c:'#4ECDC4'},
    {t:'Changes of State and Specific Latent Heat',s:'Physics',url:'/combined/higher/physics/particle-model/specific-latent-heat.html',c:'#4ECDC4'},
    {t:'Particle Motion in Gases',s:'Physics',url:'/combined/higher/physics/particle-model/particle-motion-pressure.html',c:'#4ECDC4'},
    {t:'The Structure of an Atom',s:'Physics',url:'/combined/higher/physics/atomic-structure/structure-of-atom.html',c:'#4ECDC4'},
    {t:'Mass Number, Atomic Number and Isotopes',s:'Physics',url:'/combined/higher/physics/atomic-structure/mass-number-isotopes.html',c:'#4ECDC4'},
    {t:'Development of the Model of the Atom',s:'Physics',url:'/combined/higher/physics/atomic-structure/development-atomic-model.html',c:'#4ECDC4'},
    {t:'Radioactive Decay and Nuclear Radiation',s:'Physics',url:'/combined/higher/physics/atomic-structure/radioactive-decay.html',c:'#4ECDC4'},
    {t:'Nuclear Equations',s:'Physics',url:'/combined/higher/physics/atomic-structure/nuclear-equations.html',c:'#4ECDC4'},
    {t:'Half-Lives and Radioactive Decay',s:'Physics',url:'/combined/higher/physics/atomic-structure/half-lives.html',c:'#4ECDC4'},
    {t:'Radioactive Contamination',s:'Physics',url:'/combined/higher/physics/atomic-structure/radioactive-contamination.html',c:'#4ECDC4'},
    {t:'Scalar and Vector Quantities',s:'Physics',url:'/combined/higher/physics/forces/scalar-vector-quantities.html',c:'#4ECDC4'},
    {t:'Contact and Non-Contact Forces',s:'Physics',url:'/combined/higher/physics/forces/contact-noncontact-forces.html',c:'#4ECDC4'},
    {t:'Gravity',s:'Physics',url:'/combined/higher/physics/forces/gravity.html',c:'#4ECDC4'},
    {t:'Resultant Forces',s:'Physics',url:'/combined/higher/physics/forces/resultant-forces.html',c:'#4ECDC4'},
    {t:'Work Done and Energy Transfer',s:'Physics',url:'/combined/higher/physics/forces/work-done-energy-transfer.html',c:'#4ECDC4'},
    {t:'Forces and Elasticity',s:'Physics',url:'/combined/higher/physics/forces/forces-elasticity.html',c:'#4ECDC4'},
    {t:'Distance, Speed and Velocity',s:'Physics',url:'/combined/higher/physics/forces/distance-speed-velocity.html',c:'#4ECDC4'},
    {t:'Distance–Time Graphs',s:'Physics',url:'/combined/higher/physics/forces/distance-time-graphs.html',c:'#4ECDC4'},
    {t:'Acceleration',s:'Physics',url:'/combined/higher/physics/forces/acceleration.html',c:'#4ECDC4'},
    {t:'Newton's Laws of Motion',s:'Physics',url:'/combined/higher/physics/forces/newtons-laws.html',c:'#4ECDC4'},
    {t:'Stopping Distance and Braking',s:'Physics',url:'/combined/higher/physics/forces/stopping-distance-braking.html',c:'#4ECDC4'},
    {t:'Transverse and Longitudinal Waves',s:'Physics',url:'/combined/higher/physics/waves/transverse-longitudinal-waves.html',c:'#4ECDC4'},
    {t:'Properties of Waves',s:'Physics',url:'/combined/higher/physics/waves/properties-of-waves.html',c:'#4ECDC4'},
    {t:'Types of Electromagnetic Waves',s:'Physics',url:'/combined/higher/physics/waves/types-of-em-waves.html',c:'#4ECDC4'},
    {t:'Properties of Electromagnetic Waves 1',s:'Physics',url:'/combined/higher/physics/waves/properties-em-waves-1.html',c:'#4ECDC4'},
    {t:'Properties of Electromagnetic Waves 2 and Hazards',s:'Physics',url:'/combined/higher/physics/waves/properties-em-waves-2.html',c:'#4ECDC4'},
    {t:'Uses and Applications of Electromagnetic Waves',s:'Physics',url:'/combined/higher/physics/waves/uses-em-waves.html',c:'#4ECDC4'},
    {t:'Poles of a Magnet and Permanent Magnetism',s:'Physics',url:'/combined/higher/physics/magnetism/poles-of-a-magnet.html',c:'#4ECDC4'},
    {t:'Magnetic Fields',s:'Physics',url:'/combined/higher/physics/magnetism/magnetic-fields.html',c:'#4ECDC4'},
    {t:'Electromagnetism',s:'Physics',url:'/combined/higher/physics/magnetism/electromagnetism.html',c:'#4ECDC4'},
    {t:'Momentum',s:'Physics',url:'/combined/higher/physics/forces/momentum.html',c:'#4ECDC4'},
    {t:"Fleming's Left-Hand Rule and the Motor Effect",s:'Physics',url:'/combined/higher/physics/magnetism/flemings-left-hand-rule.html',c:'#4ECDC4'},
    {t:'Electric Motors',s:'Physics',url:'/combined/higher/physics/magnetism/electric-motors.html',c:'#4ECDC4'},
    // Triple Physics Foundation
    {t:'Energy Stores and Systems',s:'Physics',url:'/triple/foundation/physics/energy/energy-stores-systems.html',c:'#4ECDC4'},
    {t:'Changes in Energy',s:'Physics',url:'/triple/foundation/physics/energy/changes-in-energy.html',c:'#4ECDC4'},
    {t:'Energy Changes in Systems',s:'Physics',url:'/triple/foundation/physics/energy/energy-changes-in-systems.html',c:'#4ECDC4'},
    {t:'Power',s:'Physics',url:'/triple/foundation/physics/energy/power.html',c:'#4ECDC4'},
    {t:'Energy Transfers in a System',s:'Physics',url:'/triple/foundation/physics/energy/energy-transfers-in-a-system.html',c:'#4ECDC4'},
    {t:'Efficiency',s:'Physics',url:'/triple/foundation/physics/energy/efficiency.html',c:'#4ECDC4'},
    {t:'Energy Resources',s:'Physics',url:'/triple/foundation/physics/energy/energy-resources.html',c:'#4ECDC4'},
    {t:'Thermal Conductivity and Reducing Unwanted Energy Transfers',s:'Physics',url:'/triple/foundation/physics/energy/thermal-conductivity.html',c:'#4ECDC4'},
    {t:'Standard Circuit Diagram Symbols',s:'Physics',url:'/triple/foundation/physics/electricity/circuit-symbols.html',c:'#4ECDC4'},
    {t:'Electrical Charge and Current',s:'Physics',url:'/triple/foundation/physics/electricity/electrical-charge-current.html',c:'#4ECDC4'},
    {t:'Current, Resistance and Potential Difference',s:'Physics',url:'/triple/foundation/physics/electricity/current-resistance-pd.html',c:'#4ECDC4'},
    {t:'Resistors',s:'Physics',url:'/triple/foundation/physics/electricity/resistors.html',c:'#4ECDC4'},
    {t:'Series and Parallel Circuits',s:'Physics',url:'/triple/foundation/physics/electricity/series-parallel-circuits.html',c:'#4ECDC4'},
    {t:'Direct and Alternating Potential Difference',s:'Physics',url:'/triple/foundation/physics/electricity/direct-alternating-pd.html',c:'#4ECDC4'},
    {t:'Mains Electricity',s:'Physics',url:'/triple/foundation/physics/electricity/mains-electricity.html',c:'#4ECDC4'},
    {t:'Power',s:'Physics',url:'/triple/foundation/physics/electricity/power-electricity.html',c:'#4ECDC4'},
    {t:'Energy Transfers in Everyday Appliances',s:'Physics',url:'/triple/foundation/physics/electricity/energy-transfers-appliances.html',c:'#4ECDC4'},
    {t:'The National Grid',s:'Physics',url:'/triple/foundation/physics/electricity/national-grid.html',c:'#4ECDC4'},
    {t:'Static Charge',s:'Physics',url:'/triple/foundation/physics/electricity/static-charge.html',c:'#4ECDC4'},
    {t:'Electric Fields',s:'Physics',url:'/triple/foundation/physics/electricity/electric-fields.html',c:'#4ECDC4'},
    {t:'Density of Materials',s:'Physics',url:'/triple/foundation/physics/particle-model/density-of-materials.html',c:'#4ECDC4'},
    {t:'Changes of State',s:'Physics',url:'/triple/foundation/physics/particle-model/changes-of-state.html',c:'#4ECDC4'},
    {t:'Internal Energy',s:'Physics',url:'/triple/foundation/physics/particle-model/internal-energy.html',c:'#4ECDC4'},
    {t:'Temperature Changes and Specific Heat Capacity',s:'Physics',url:'/triple/foundation/physics/particle-model/temperature-changes-shc.html',c:'#4ECDC4'},
    {t:'Changes of State and Specific Latent Heat',s:'Physics',url:'/triple/foundation/physics/particle-model/specific-latent-heat.html',c:'#4ECDC4'},
    {t:'Particle Motion in Gases',s:'Physics',url:'/triple/foundation/physics/particle-model/particle-motion-pressure.html',c:'#4ECDC4'},
    {t:'The Structure of an Atom',s:'Physics',url:'/triple/foundation/physics/atomic-structure/structure-of-atom.html',c:'#4ECDC4'},
    {t:'Mass Number, Atomic Number and Isotopes',s:'Physics',url:'/triple/foundation/physics/atomic-structure/mass-number-isotopes.html',c:'#4ECDC4'},
    {t:'Development of the Model of the Atom',s:'Physics',url:'/triple/foundation/physics/atomic-structure/development-atomic-model.html',c:'#4ECDC4'},
    {t:'Radioactive Decay and Nuclear Radiation',s:'Physics',url:'/triple/foundation/physics/atomic-structure/radioactive-decay.html',c:'#4ECDC4'},
    {t:'Nuclear Equations',s:'Physics',url:'/triple/foundation/physics/atomic-structure/nuclear-equations.html',c:'#4ECDC4'},
    {t:'Half-Lives and Radioactive Decay',s:'Physics',url:'/triple/foundation/physics/atomic-structure/half-lives.html',c:'#4ECDC4'},
    {t:'Radioactive Contamination',s:'Physics',url:'/triple/foundation/physics/atomic-structure/radioactive-contamination.html',c:'#4ECDC4'},
    {t:'Background Radiation',s:'Physics',url:'/triple/foundation/physics/atomic-structure/background-radiation.html',c:'#4ECDC4'},
    {t:'Uses of Nuclear Radiation',s:'Physics',url:'/triple/foundation/physics/atomic-structure/uses-of-nuclear-radiation.html',c:'#4ECDC4'},
    {t:'Nuclear Fission',s:'Physics',url:'/triple/foundation/physics/atomic-structure/nuclear-fission.html',c:'#4ECDC4'},
    {t:'Nuclear Fusion',s:'Physics',url:'/triple/foundation/physics/atomic-structure/nuclear-fusion.html',c:'#4ECDC4'},
    {t:'Scalar and Vector Quantities',s:'Physics',url:'/triple/foundation/physics/forces/scalar-vector-quantities.html',c:'#4ECDC4'},
    {t:'Contact and Non-Contact Forces',s:'Physics',url:'/triple/foundation/physics/forces/contact-noncontact-forces.html',c:'#4ECDC4'},
    {t:'Gravity',s:'Physics',url:'/triple/foundation/physics/forces/gravity.html',c:'#4ECDC4'},
    {t:'Resultant Forces',s:'Physics',url:'/triple/foundation/physics/forces/resultant-forces.html',c:'#4ECDC4'},
    {t:'Work Done and Energy Transfer',s:'Physics',url:'/triple/foundation/physics/forces/work-done-energy-transfer.html',c:'#4ECDC4'},
    {t:'Forces and Elasticity',s:'Physics',url:'/triple/foundation/physics/forces/forces-elasticity.html',c:'#4ECDC4'},
    {t:'Moments, Levers and Gears',s:'Physics',url:'/triple/foundation/physics/forces/moments-levers-gears.html',c:'#4ECDC4'},
    {t:'Pressure in a Fluid',s:'Physics',url:'/triple/foundation/physics/forces/pressure-in-a-fluid.html',c:'#4ECDC4'},
    {t:'Distance, Speed and Velocity',s:'Physics',url:'/triple/foundation/physics/forces/distance-speed-velocity.html',c:'#4ECDC4'},
    {t:'Distance–Time Graphs',s:'Physics',url:'/triple/foundation/physics/forces/distance-time-graphs.html',c:'#4ECDC4'},
    {t:'Acceleration',s:'Physics',url:'/triple/foundation/physics/forces/acceleration.html',c:'#4ECDC4'},
    {t:'Newton\'s Laws of Motion',s:'Physics',url:'/triple/foundation/physics/forces/newtons-laws.html',c:'#4ECDC4'},
    {t:'Stopping Distance and Braking',s:'Physics',url:'/triple/foundation/physics/forces/stopping-distance-braking.html',c:'#4ECDC4'},
    {t:'Transverse and Longitudinal Waves',s:'Physics',url:'/triple/foundation/physics/waves/transverse-longitudinal-waves.html',c:'#4ECDC4'},
    {t:'Properties of Waves',s:'Physics',url:'/triple/foundation/physics/waves/properties-of-waves.html',c:'#4ECDC4'},
    {t:'Types of Electromagnetic Waves',s:'Physics',url:'/triple/foundation/physics/waves/types-of-em-waves.html',c:'#4ECDC4'},
    {t:'Properties of Electromagnetic Waves 1',s:'Physics',url:'/triple/foundation/physics/waves/properties-em-waves-1.html',c:'#4ECDC4'},
    {t:'Properties of Electromagnetic Waves 2 and Hazards',s:'Physics',url:'/triple/foundation/physics/waves/properties-em-waves-2.html',c:'#4ECDC4'},
    {t:'Uses and Applications of Electromagnetic Waves',s:'Physics',url:'/triple/foundation/physics/waves/uses-em-waves.html',c:'#4ECDC4'},
    {t:'Lenses',s:'Physics',url:'/triple/foundation/physics/waves/lenses.html',c:'#4ECDC4'},
    {t:'Infrared Emission, Absorption and Black Bodies',s:'Physics',url:'/triple/foundation/physics/waves/infrared-black-bodies.html',c:'#4ECDC4'},
    {t:'Poles of a Magnet and Permanent Magnetism',s:'Physics',url:'/triple/foundation/physics/magnetism/poles-of-a-magnet.html',c:'#4ECDC4'},
    {t:'Magnetic Fields',s:'Physics',url:'/triple/foundation/physics/magnetism/magnetic-fields.html',c:'#4ECDC4'},
    {t:'Electromagnetism',s:'Physics',url:'/triple/foundation/physics/magnetism/electromagnetism.html',c:'#4ECDC4'},
    {t:'Our Solar System and Gravity',s:'Physics',url:'/triple/foundation/physics/space/solar-system-gravity.html',c:'#4ECDC4'},
    {t:'The Life Cycle of a Star',s:'Physics',url:'/triple/foundation/physics/space/stellar-evolution.html',c:'#4ECDC4'},
    {t:'Red-shift and the Big Bang',s:'Physics',url:'/triple/foundation/physics/space/red-shift-big-bang.html',c:'#4ECDC4'},
    // Triple Physics Higher
    {t:'Energy Stores and Systems',s:'Physics',url:'/triple/higher/physics/energy/energy-stores-systems.html',c:'#4ECDC4'},
    {t:'Changes in Energy',s:'Physics',url:'/triple/higher/physics/energy/changes-in-energy.html',c:'#4ECDC4'},
    {t:'Energy Changes in Systems',s:'Physics',url:'/triple/higher/physics/energy/energy-changes-in-systems.html',c:'#4ECDC4'},
    {t:'Power',s:'Physics',url:'/triple/higher/physics/energy/power.html',c:'#4ECDC4'},
    {t:'Energy Transfers in a System',s:'Physics',url:'/triple/higher/physics/energy/energy-transfers-in-a-system.html',c:'#4ECDC4'},
    {t:'Efficiency',s:'Physics',url:'/triple/higher/physics/energy/efficiency.html',c:'#4ECDC4'},
    {t:'Energy Resources',s:'Physics',url:'/triple/higher/physics/energy/energy-resources.html',c:'#4ECDC4'},
    {t:'Thermal Conductivity and Reducing Unwanted Energy Transfers',s:'Physics',url:'/triple/higher/physics/energy/thermal-conductivity.html',c:'#4ECDC4'},
    {t:'Standard Circuit Diagram Symbols',s:'Physics',url:'/triple/higher/physics/electricity/circuit-symbols.html',c:'#4ECDC4'},
    {t:'Electrical Charge and Current',s:'Physics',url:'/triple/higher/physics/electricity/electrical-charge-current.html',c:'#4ECDC4'},
    {t:'Current, Resistance and Potential Difference',s:'Physics',url:'/triple/higher/physics/electricity/current-resistance-pd.html',c:'#4ECDC4'},
    {t:'Resistors',s:'Physics',url:'/triple/higher/physics/electricity/resistors.html',c:'#4ECDC4'},
    {t:'Series and Parallel Circuits',s:'Physics',url:'/triple/higher/physics/electricity/series-parallel-circuits.html',c:'#4ECDC4'},
    {t:'Direct and Alternating Potential Difference',s:'Physics',url:'/triple/higher/physics/electricity/direct-alternating-pd.html',c:'#4ECDC4'},
    {t:'Mains Electricity',s:'Physics',url:'/triple/higher/physics/electricity/mains-electricity.html',c:'#4ECDC4'},
    {t:'Power',s:'Physics',url:'/triple/higher/physics/electricity/power-electricity.html',c:'#4ECDC4'},
    {t:'Energy Transfers in Everyday Appliances',s:'Physics',url:'/triple/higher/physics/electricity/energy-transfers-appliances.html',c:'#4ECDC4'},
    {t:'The National Grid',s:'Physics',url:'/triple/higher/physics/electricity/national-grid.html',c:'#4ECDC4'},
    {t:'Static Charge',s:'Physics',url:'/triple/higher/physics/electricity/static-charge.html',c:'#4ECDC4'},
    {t:'Electric Fields',s:'Physics',url:'/triple/higher/physics/electricity/electric-fields.html',c:'#4ECDC4'},
    {t:'Density of Materials',s:'Physics',url:'/triple/higher/physics/particle-model/density-of-materials.html',c:'#4ECDC4'},
    {t:'Changes of State',s:'Physics',url:'/triple/higher/physics/particle-model/changes-of-state.html',c:'#4ECDC4'},
    {t:'Internal Energy',s:'Physics',url:'/triple/higher/physics/particle-model/internal-energy.html',c:'#4ECDC4'},
    {t:'Temperature Changes and Specific Heat Capacity',s:'Physics',url:'/triple/higher/physics/particle-model/temperature-changes-shc.html',c:'#4ECDC4'},
    {t:'Changes of State and Specific Latent Heat',s:'Physics',url:'/triple/higher/physics/particle-model/specific-latent-heat.html',c:'#4ECDC4'},
    {t:'Particle Motion in Gases',s:'Physics',url:'/triple/higher/physics/particle-model/particle-motion-pressure.html',c:'#4ECDC4'},
    {t:'The Structure of an Atom',s:'Physics',url:'/triple/higher/physics/atomic-structure/structure-of-atom.html',c:'#4ECDC4'},
    {t:'Mass Number, Atomic Number and Isotopes',s:'Physics',url:'/triple/higher/physics/atomic-structure/mass-number-isotopes.html',c:'#4ECDC4'},
    {t:'Development of the Model of the Atom',s:'Physics',url:'/triple/higher/physics/atomic-structure/development-atomic-model.html',c:'#4ECDC4'},
    {t:'Radioactive Decay and Nuclear Radiation',s:'Physics',url:'/triple/higher/physics/atomic-structure/radioactive-decay.html',c:'#4ECDC4'},
    {t:'Nuclear Equations',s:'Physics',url:'/triple/higher/physics/atomic-structure/nuclear-equations.html',c:'#4ECDC4'},
    {t:'Half-Lives and Radioactive Decay',s:'Physics',url:'/triple/higher/physics/atomic-structure/half-lives.html',c:'#4ECDC4'},
    {t:'Radioactive Contamination',s:'Physics',url:'/triple/higher/physics/atomic-structure/radioactive-contamination.html',c:'#4ECDC4'},
    {t:'Background Radiation',s:'Physics',url:'/triple/higher/physics/atomic-structure/background-radiation.html',c:'#4ECDC4'},
    {t:'Uses of Nuclear Radiation',s:'Physics',url:'/triple/higher/physics/atomic-structure/uses-of-nuclear-radiation.html',c:'#4ECDC4'},
    {t:'Nuclear Fission',s:'Physics',url:'/triple/higher/physics/atomic-structure/nuclear-fission.html',c:'#4ECDC4'},
    {t:'Nuclear Fusion',s:'Physics',url:'/triple/higher/physics/atomic-structure/nuclear-fusion.html',c:'#4ECDC4'},
    {t:'Scalar and Vector Quantities',s:'Physics',url:'/triple/higher/physics/forces/scalar-vector-quantities.html',c:'#4ECDC4'},
    {t:'Contact and Non-Contact Forces',s:'Physics',url:'/triple/higher/physics/forces/contact-noncontact-forces.html',c:'#4ECDC4'},
    {t:'Gravity',s:'Physics',url:'/triple/higher/physics/forces/gravity.html',c:'#4ECDC4'},
    {t:'Resultant Forces',s:'Physics',url:'/triple/higher/physics/forces/resultant-forces.html',c:'#4ECDC4'},
    {t:'Resolving Forces and Vector Diagrams',s:'Physics',url:'/triple/higher/physics/forces/resolving-forces.html',c:'#4ECDC4'},
    {t:'Free Body Diagrams',s:'Physics',url:'/triple/higher/physics/forces/free-body-diagrams.html',c:'#4ECDC4'},
    {t:'Work Done and Energy Transfer',s:'Physics',url:'/triple/higher/physics/forces/work-done-energy-transfer.html',c:'#4ECDC4'},
    {t:'Forces and Elasticity',s:'Physics',url:'/triple/higher/physics/forces/forces-elasticity.html',c:'#4ECDC4'},
    {t:'Moments, Levers and Gears',s:'Physics',url:'/triple/higher/physics/forces/moments-levers-gears.html',c:'#4ECDC4'},
    {t:'Pressure in a Fluid',s:'Physics',url:'/triple/higher/physics/forces/pressure-in-a-fluid.html',c:'#4ECDC4'},
    {t:'Upthrust and Floating',s:'Physics',url:'/triple/higher/physics/forces/upthrust-floating.html',c:'#4ECDC4'},
    {t:'Distance, Speed and Velocity',s:'Physics',url:'/triple/higher/physics/forces/distance-speed-velocity.html',c:'#4ECDC4'},
    {t:'Distance–Time Graphs',s:'Physics',url:'/triple/higher/physics/forces/distance-time-graphs.html',c:'#4ECDC4'},
    {t:'Acceleration',s:'Physics',url:'/triple/higher/physics/forces/acceleration.html',c:'#4ECDC4'},
    {t:'Newton\'s Laws of Motion',s:'Physics',url:'/triple/higher/physics/forces/newtons-laws.html',c:'#4ECDC4'},
    {t:'Stopping Distance and Braking',s:'Physics',url:'/triple/higher/physics/forces/stopping-distance-braking.html',c:'#4ECDC4'},
    {t:'Motion in a Circle',s:'Physics',url:'/triple/higher/physics/forces/motion-in-a-circle.html',c:'#4ECDC4'},
    {t:'Momentum',s:'Physics',url:'/triple/higher/physics/forces/momentum.html',c:'#4ECDC4'},
    {t:'Transverse and Longitudinal Waves',s:'Physics',url:'/triple/higher/physics/waves/transverse-longitudinal-waves.html',c:'#4ECDC4'},
    {t:'Sound Waves and Hearing',s:'Physics',url:'/triple/higher/physics/waves/sound-waves-hearing.html',c:'#4ECDC4'},
    {t:'Waves for Detection and Exploration',s:'Physics',url:'/triple/higher/physics/waves/waves-detection-exploration.html',c:'#4ECDC4'},
    {t:'Properties of Waves',s:'Physics',url:'/triple/higher/physics/waves/properties-of-waves.html',c:'#4ECDC4'},
    {t:'Types of Electromagnetic Waves',s:'Physics',url:'/triple/higher/physics/waves/types-of-em-waves.html',c:'#4ECDC4'},
    {t:'Properties of Electromagnetic Waves 1',s:'Physics',url:'/triple/higher/physics/waves/properties-em-waves-1.html',c:'#4ECDC4'},
    {t:'Properties of Electromagnetic Waves 2 and Hazards',s:'Physics',url:'/triple/higher/physics/waves/properties-em-waves-2.html',c:'#4ECDC4'},
    {t:'Uses and Applications of Electromagnetic Waves',s:'Physics',url:'/triple/higher/physics/waves/uses-em-waves.html',c:'#4ECDC4'},
    {t:'Wave Front Diagrams and Refraction',s:'Physics',url:'/triple/higher/physics/waves/wave-front-refraction.html',c:'#4ECDC4'},
    {t:'Lenses',s:'Physics',url:'/triple/higher/physics/waves/lenses.html',c:'#4ECDC4'},
    {t:'Infrared Emission, Absorption and Black Bodies',s:'Physics',url:'/triple/higher/physics/waves/infrared-black-bodies.html',c:'#4ECDC4'},
    {t:'Radiation Balance and Earth\'s Temperature',s:'Physics',url:'/triple/higher/physics/waves/radiation-balance-temperature.html',c:'#4ECDC4'},
    {t:'Poles of a Magnet and Permanent Magnetism',s:'Physics',url:'/triple/higher/physics/magnetism/poles-of-a-magnet.html',c:'#4ECDC4'},
    {t:'Magnetic Fields',s:'Physics',url:'/triple/higher/physics/magnetism/magnetic-fields.html',c:'#4ECDC4'},
    {t:'Electromagnetism',s:'Physics',url:'/triple/higher/physics/magnetism/electromagnetism.html',c:'#4ECDC4'},
    {t:'Fleming\'s Left-Hand Rule and the Motor Effect',s:'Physics',url:'/triple/higher/physics/magnetism/flemings-left-hand-rule.html',c:'#4ECDC4'},
    {t:'Electric Motors',s:'Physics',url:'/triple/higher/physics/magnetism/electric-motors.html',c:'#4ECDC4'},
    {t:'Loudspeakers and Headphones',s:'Physics',url:'/triple/higher/physics/magnetism/loudspeakers-headphones.html',c:'#4ECDC4'},
    {t:'Induced Potential and the Generator Effect',s:'Physics',url:'/triple/higher/physics/magnetism/induced-potential.html',c:'#4ECDC4'},
    {t:'Uses of the Generator Effect',s:'Physics',url:'/triple/higher/physics/magnetism/uses-generator-effect.html',c:'#4ECDC4'},
    {t:'Microphones',s:'Physics',url:'/triple/higher/physics/magnetism/microphones.html',c:'#4ECDC4'},
    {t:'Transformers',s:'Physics',url:'/triple/higher/physics/magnetism/transformers.html',c:'#4ECDC4'},
    {t:'Our Solar System and Gravity',s:'Physics',url:'/triple/higher/physics/space/solar-system-gravity.html',c:'#4ECDC4'},
    {t:'Gravity, Stable Orbits and Orbital Speed',s:'Physics',url:'/triple/higher/physics/space/gravity-stable-orbits.html',c:'#4ECDC4'},
    {t:'The Life Cycle of a Star',s:'Physics',url:'/triple/higher/physics/space/stellar-evolution.html',c:'#4ECDC4'},
    {t:'Red-shift and the Big Bang',s:'Physics',url:'/triple/higher/physics/space/red-shift-big-bang.html',c:'#4ECDC4'},
    {t:'Dark Matter and Dark Energy',s:'Physics',url:'/triple/higher/physics/space/dark-matter-dark-energy.html',c:'#4ECDC4'},
    {t:'Cell Structure',s:'Biology',url:'/combined/higher/biology/cell-biology/cell-structure.html',c:'#6BCB77'},
    {t:'Transport in Cells (Diffusion, Osmosis)',s:'Biology',url:'/combined/higher/biology/cell-biology/transport-in-cells.html',c:'#6BCB77'},
    {t:'Cell Division (Mitosis)',s:'Biology',url:'/combined/higher/biology/cell-biology/cell-division.html',c:'#6BCB77'},
    {t:'Principles of Organisation',s:'Biology',url:'/combined/higher/biology/organisation/principles-of-organisation.html',c:'#6BCB77'},
    {t:'The Digestive System',s:'Biology',url:'/combined/higher/biology/organisation/digestive-system.html',c:'#6BCB77'},
    {t:'Enzymes',s:'Biology',url:'/combined/higher/biology/organisation/enzymes.html',c:'#6BCB77'},
    {t:'The Heart and Blood Vessels',s:'Biology',url:'/combined/higher/biology/organisation/heart-blood-vessels.html',c:'#6BCB77'},
    {t:'Blood',s:'Biology',url:'/combined/higher/biology/organisation/blood.html',c:'#6BCB77'},
    {t:'Coronary Heart Disease',s:'Biology',url:'/combined/higher/biology/organisation/coronary-heart-disease.html',c:'#6BCB77'},
    {t:'Health, Disease and Risk Factors',s:'Biology',url:'/combined/higher/biology/organisation/health-disease.html',c:'#6BCB77'},
    {t:'Cancer',s:'Biology',url:'/combined/higher/biology/organisation/cancer.html',c:'#6BCB77'},
    {t:'Plant Tissues and Organs',s:'Biology',url:'/combined/higher/biology/organisation/plant-tissues.html',c:'#6BCB77'},
    {t:'Transpiration',s:'Biology',url:'/combined/higher/biology/organisation/transpiration.html',c:'#6BCB77'},
    {t:'Translocation',s:'Biology',url:'/combined/higher/biology/organisation/translocation.html',c:'#6BCB77'},
    {t:'Communicable Diseases and Defence',s:'Biology',url:'/combined/higher/biology/infection-response/communicable-diseases-defence.html',c:'#6BCB77'},
    {t:'Viral Diseases',s:'Biology',url:'/combined/higher/biology/infection-response/viral-diseases.html',c:'#6BCB77'},
    {t:'Bacterial Diseases',s:'Biology',url:'/combined/higher/biology/infection-response/bacterial-diseases.html',c:'#6BCB77'},
    {t:'Fungal and Protist Diseases',s:'Biology',url:'/combined/higher/biology/infection-response/fungal-protist-diseases.html',c:'#6BCB77'},
    {t:'Vaccination',s:'Biology',url:'/combined/higher/biology/infection-response/vaccination.html',c:'#6BCB77'},
    {t:'Antibiotics and Painkillers',s:'Biology',url:'/combined/higher/biology/infection-response/antibiotics-painkillers.html',c:'#6BCB77'},
    {t:'Drug Discovery and Development',s:'Biology',url:'/combined/higher/biology/infection-response/drug-discovery-development.html',c:'#6BCB77'},
    {t:'Plant Disease Detection and Defence',s:'Biology',url:'/combined/higher/biology/infection-response/plant-disease-detection-defence.html',c:'#6BCB77'},
    {t:'Photosynthesis',s:'Biology',url:'/combined/higher/biology/bioenergetics/photosynthesis.html',c:'#6BCB77'},
    {t:'Rate of Photosynthesis',s:'Biology',url:'/combined/higher/biology/bioenergetics/rate-of-photosynthesis.html',c:'#6BCB77'},
    {t:'Uses of Glucose from Photosynthesis',s:'Biology',url:'/combined/higher/biology/bioenergetics/uses-of-glucose.html',c:'#6BCB77'},
    {t:'Aerobic Respiration',s:'Biology',url:'/combined/higher/biology/bioenergetics/aerobic-respiration.html',c:'#6BCB77'},
    {t:'Anaerobic Respiration',s:'Biology',url:'/combined/higher/biology/bioenergetics/anaerobic-respiration.html',c:'#6BCB77'},
    {t:'Response to Exercise',s:'Biology',url:'/combined/higher/biology/bioenergetics/response-to-exercise.html',c:'#6BCB77'},
    {t:'Metabolism',s:'Biology',url:'/combined/higher/biology/bioenergetics/metabolism.html',c:'#6BCB77'},
    {t:'Homeostasis',s:'Biology',url:'/combined/higher/biology/homeostasis/homeostasis.html',c:'#6BCB77'},
    {t:'The Human Nervous System',s:'Biology',url:'/combined/higher/biology/homeostasis/nervous-system.html',c:'#6BCB77'},
    {t:'Reflex Actions',s:'Biology',url:'/combined/higher/biology/homeostasis/reflex-actions.html',c:'#6BCB77'},
    {t:'Thermoregulation',s:'Biology',url:'/combined/higher/biology/homeostasis/thermoregulation.html',c:'#6BCB77'},
    {t:'The Endocrine System',s:'Biology',url:'/combined/higher/biology/homeostasis/endocrine-system.html',c:'#6BCB77'},
    {t:'Blood Glucose Control and Diabetes',s:'Biology',url:'/combined/higher/biology/homeostasis/blood-glucose-diabetes.html',c:'#6BCB77'},
    {t:'Human Reproduction and Hormones',s:'Biology',url:'/combined/higher/biology/homeostasis/human-reproduction-hormones.html',c:'#6BCB77'},
    {t:'Contraception and Fertility',s:'Biology',url:'/combined/higher/biology/homeostasis/contraception-fertility.html',c:'#6BCB77'},
    {t:'Sexual and Asexual Reproduction',s:'Biology',url:'/combined/higher/biology/inheritance/sexual-asexual-reproduction.html',c:'#6BCB77'},
    {t:'DNA and the Genome',s:'Biology',url:'/combined/higher/biology/inheritance/dna-genome.html',c:'#6BCB77'},
    {t:'Genetic Inheritance',s:'Biology',url:'/combined/higher/biology/inheritance/genetic-inheritance.html',c:'#6BCB77'},
    {t:'Inherited Disorders',s:'Biology',url:'/combined/higher/biology/inheritance/inherited-disorders.html',c:'#6BCB77'},
    {t:'Sex Determination',s:'Biology',url:'/combined/higher/biology/inheritance/sex-determination.html',c:'#6BCB77'},
    {t:'Variation',s:'Biology',url:'/combined/higher/biology/inheritance/variation.html',c:'#6BCB77'},
    {t:'Evolution and Natural Selection',s:'Biology',url:'/combined/higher/biology/inheritance/evolution-natural-selection.html',c:'#6BCB77'},
    {t:'Selective Breeding',s:'Biology',url:'/combined/higher/biology/inheritance/selective-breeding.html',c:'#6BCB77'},
    {t:'Genetic Engineering',s:'Biology',url:'/combined/higher/biology/inheritance/genetic-engineering.html',c:'#6BCB77'},
    {t:'Evidence for Evolution',s:'Biology',url:'/combined/higher/biology/inheritance/evidence-for-evolution.html',c:'#6BCB77'},
    {t:'Fossils and Extinction',s:'Biology',url:'/combined/higher/biology/inheritance/fossils-extinction.html',c:'#6BCB77'},
    {t:'Resistant Bacteria',s:'Biology',url:'/combined/higher/biology/inheritance/resistant-bacteria.html',c:'#6BCB77'},
    {t:'Ecosystems',s:'Biology',url:'/combined/higher/biology/ecology/ecosystems.html',c:'#6BCB77'},
    {t:'Abiotic and Biotic Factors',s:'Biology',url:'/combined/higher/biology/ecology/abiotic-biotic-factors.html',c:'#6BCB77'},
    {t:'Adaptations',s:'Biology',url:'/combined/higher/biology/ecology/adaptations.html',c:'#6BCB77'},
    {t:'Food Chains and Food Webs',s:'Biology',url:'/combined/higher/biology/ecology/food-chains-webs.html',c:'#6BCB77'},
    {t:'Population and Competition',s:'Biology',url:'/combined/higher/biology/ecology/population-competition.html',c:'#6BCB77'},
    {t:'Biodiversity',s:'Biology',url:'/combined/higher/biology/ecology/biodiversity.html',c:'#6BCB77'},
    {t:'The Carbon Cycle',s:'Biology',url:'/combined/higher/biology/ecology/carbon-cycle.html',c:'#6BCB77'},
    {t:'The Water Cycle',s:'Biology',url:'/combined/higher/biology/ecology/water-cycle.html',c:'#6BCB77'},
    {t:'The Nitrogen Cycle',s:'Biology',url:'/combined/higher/biology/ecology/nitrogen-cycle.html',c:'#6BCB77'},
    {t:'Decomposition',s:'Biology',url:'/combined/higher/biology/ecology/decomposition.html',c:'#6BCB77'},
    {t:'Sampling Techniques',s:'Biology',url:'/combined/higher/biology/ecology/sampling-techniques.html',c:'#6BCB77'},
    {t:'Culturing Microorganisms',s:'Biology',url:'/combined/higher/biology/cell-biology/culturing-microorganisms.html',c:'#6BCB77'},
    {t:'Monoclonal Antibodies',s:'Biology',url:'/combined/higher/biology/infection-response/monoclonal-antibodies.html',c:'#6BCB77'},
    {t:'Reaction Time',s:'Biology',url:'/combined/higher/biology/homeostasis/reaction-time.html',c:'#6BCB77'},
    {t:'The Brain',s:'Biology',url:'/combined/higher/biology/homeostasis/the-brain.html',c:'#6BCB77'},
    {t:'The Eye',s:'Biology',url:'/combined/higher/biology/homeostasis/the-eye.html',c:'#6BCB77'},
    {t:'Defects of the Eye',s:'Biology',url:'/combined/higher/biology/homeostasis/defects-of-the-eye.html',c:'#6BCB77'},
    {t:'Trophic Levels and Biomass',s:'Biology',url:'/combined/higher/biology/ecology/trophic-levels-biomass.html',c:'#6BCB77'},
    {t:'Food Production and Sustainable Fishing',s:'Biology',url:'/combined/higher/biology/ecology/food-production.html',c:'#6BCB77'},
    {t:'Impact of Environmental Change',s:'Biology',url:'/combined/higher/biology/ecology/environmental-change.html',c:'#6BCB77'},
    {t:'Role of Biotechnology',s:'Biology',url:'/combined/higher/biology/ecology/role-of-biotechnology.html',c:'#6BCB77'},
    // Triple Biology Foundation
    {t:'Eukaryotes and Prokaryotes',s:'Biology',url:'/triple/foundation/biology/cell-biology/eukaryotes-prokaryotes.html',c:'#6BCB77'},
    {t:'Animal and Plant Cells',s:'Biology',url:'/triple/foundation/biology/cell-biology/animal-plant-cells.html',c:'#6BCB77'},
    {t:'Cell Specialisation and Differentiation',s:'Biology',url:'/triple/foundation/biology/cell-biology/cell-specialisation.html',c:'#6BCB77'},
    {t:'Microscopy',s:'Biology',url:'/triple/foundation/biology/cell-biology/microscopy.html',c:'#6BCB77'},
    {t:'Chromosomes, the Cell Cycle and Mitosis',s:'Biology',url:'/triple/foundation/biology/cell-biology/chromosomes-mitosis.html',c:'#6BCB77'},
    {t:'Stem Cells',s:'Biology',url:'/triple/foundation/biology/cell-biology/stem-cells.html',c:'#6BCB77'},
    {t:'Diffusion, Osmosis and Active Transport',s:'Biology',url:'/triple/foundation/biology/cell-biology/transport-in-cells.html',c:'#6BCB77'},
    {t:'Culturing Microorganisms',s:'Biology',url:'/triple/foundation/biology/cell-biology/culturing-microorganisms.html',c:'#6BCB77'},
    {t:'Principles of Organisation',s:'Biology',url:'/triple/foundation/biology/organisation/principles-of-organisation.html',c:'#6BCB77'},
    {t:'The Digestive System',s:'Biology',url:'/triple/foundation/biology/organisation/digestive-system.html',c:'#6BCB77'},
    {t:'Enzymes',s:'Biology',url:'/triple/foundation/biology/organisation/enzymes.html',c:'#6BCB77'},
    {t:'The Heart and Blood Vessels',s:'Biology',url:'/triple/foundation/biology/organisation/heart-blood-vessels.html',c:'#6BCB77'},
    {t:'Blood',s:'Biology',url:'/triple/foundation/biology/organisation/blood.html',c:'#6BCB77'},
    {t:'Coronary Heart Disease',s:'Biology',url:'/triple/foundation/biology/organisation/coronary-heart-disease.html',c:'#6BCB77'},
    {t:'Health, Disease and Risk Factors',s:'Biology',url:'/triple/foundation/biology/organisation/health-disease.html',c:'#6BCB77'},
    {t:'Cancer',s:'Biology',url:'/triple/foundation/biology/organisation/cancer.html',c:'#6BCB77'},
    {t:'Plant Tissues and Organs',s:'Biology',url:'/triple/foundation/biology/organisation/plant-tissues.html',c:'#6BCB77'},
    {t:'Transpiration',s:'Biology',url:'/triple/foundation/biology/organisation/transpiration.html',c:'#6BCB77'},
    {t:'Translocation',s:'Biology',url:'/triple/foundation/biology/organisation/translocation.html',c:'#6BCB77'},
    {t:'Communicable Diseases and Human Defence Systems',s:'Biology',url:'/triple/foundation/biology/infection-response/communicable-diseases-defence.html',c:'#6BCB77'},
    {t:'Viral Diseases',s:'Biology',url:'/triple/foundation/biology/infection-response/viral-diseases.html',c:'#6BCB77'},
    {t:'Bacterial Diseases',s:'Biology',url:'/triple/foundation/biology/infection-response/bacterial-diseases.html',c:'#6BCB77'},
    {t:'Fungal and Protist Diseases',s:'Biology',url:'/triple/foundation/biology/infection-response/fungal-protist-diseases.html',c:'#6BCB77'},
    {t:'Vaccination',s:'Biology',url:'/triple/foundation/biology/infection-response/vaccination.html',c:'#6BCB77'},
    {t:'Antibiotics and Painkillers',s:'Biology',url:'/triple/foundation/biology/infection-response/antibiotics-painkillers.html',c:'#6BCB77'},
    {t:'Drug Discovery and Development',s:'Biology',url:'/triple/foundation/biology/infection-response/drug-discovery-development.html',c:'#6BCB77'},
    {t:'Plant Disease Detection and Defence',s:'Biology',url:'/triple/foundation/biology/infection-response/plant-disease-detection-defence.html',c:'#6BCB77'},
    {t:'Photosynthesis',s:'Biology',url:'/triple/foundation/biology/bioenergetics/photosynthesis.html',c:'#6BCB77'},
    {t:'Rate of Photosynthesis',s:'Biology',url:'/triple/foundation/biology/bioenergetics/rate-of-photosynthesis.html',c:'#6BCB77'},
    {t:'Uses of Glucose from Photosynthesis',s:'Biology',url:'/triple/foundation/biology/bioenergetics/uses-of-glucose.html',c:'#6BCB77'},
    {t:'Aerobic Respiration',s:'Biology',url:'/triple/foundation/biology/bioenergetics/aerobic-respiration.html',c:'#6BCB77'},
    {t:'Anaerobic Respiration',s:'Biology',url:'/triple/foundation/biology/bioenergetics/anaerobic-respiration.html',c:'#6BCB77'},
    {t:'Response to Exercise',s:'Biology',url:'/triple/foundation/biology/bioenergetics/response-to-exercise.html',c:'#6BCB77'},
    {t:'Metabolism',s:'Biology',url:'/triple/foundation/biology/bioenergetics/metabolism.html',c:'#6BCB77'},
    {t:'Homeostasis',s:'Biology',url:'/triple/foundation/biology/homeostasis/homeostasis.html',c:'#6BCB77'},
    {t:'The Human Nervous System',s:'Biology',url:'/triple/foundation/biology/homeostasis/nervous-system.html',c:'#6BCB77'},
    {t:'Reflex Actions',s:'Biology',url:'/triple/foundation/biology/homeostasis/reflex-actions.html',c:'#6BCB77'},
    {t:'Thermoregulation',s:'Biology',url:'/triple/foundation/biology/homeostasis/thermoregulation.html',c:'#6BCB77'},
    {t:'The Endocrine System',s:'Biology',url:'/triple/foundation/biology/homeostasis/endocrine-system.html',c:'#6BCB77'},
    {t:'Blood Glucose Control and Diabetes',s:'Biology',url:'/triple/foundation/biology/homeostasis/blood-glucose-diabetes.html',c:'#6BCB77'},
    {t:'Human Reproduction and Hormones',s:'Biology',url:'/triple/foundation/biology/homeostasis/human-reproduction-hormones.html',c:'#6BCB77'},
    {t:'Contraception and Fertility Treatment',s:'Biology',url:'/triple/foundation/biology/homeostasis/contraception-fertility.html',c:'#6BCB77'},
    {t:'Reaction Time',s:'Biology',url:'/triple/foundation/biology/homeostasis/reaction-time.html',c:'#6BCB77'},
    {t:'The Brain',s:'Biology',url:'/triple/foundation/biology/homeostasis/the-brain.html',c:'#6BCB77'},
    {t:'The Eye',s:'Biology',url:'/triple/foundation/biology/homeostasis/the-eye.html',c:'#6BCB77'},
    {t:'Defects of the Eye',s:'Biology',url:'/triple/foundation/biology/homeostasis/defects-of-the-eye.html',c:'#6BCB77'},
    {t:'Sexual and Asexual Reproduction',s:'Biology',url:'/triple/foundation/biology/inheritance/sexual-asexual-reproduction.html',c:'#6BCB77'},
    {t:'Meiosis',s:'Biology',url:'/triple/foundation/biology/inheritance/meiosis.html',c:'#6BCB77'},
    {t:'Advantages and Disadvantages of Sexual and Asexual Reproduction',s:'Biology',url:'/triple/foundation/biology/inheritance/advantages-sexual-asexual.html',c:'#6BCB77'},
    {t:'DNA and the Genome',s:'Biology',url:'/triple/foundation/biology/inheritance/dna-genome.html',c:'#6BCB77'},
    {t:'DNA Structure',s:'Biology',url:'/triple/foundation/biology/inheritance/dna-structure.html',c:'#6BCB77'},
    {t:'Genetic Inheritance',s:'Biology',url:'/triple/foundation/biology/inheritance/genetic-inheritance.html',c:'#6BCB77'},
    {t:'Inherited Disorders',s:'Biology',url:'/triple/foundation/biology/inheritance/inherited-disorders.html',c:'#6BCB77'},
    {t:'Sex Determination',s:'Biology',url:'/triple/foundation/biology/inheritance/sex-determination.html',c:'#6BCB77'},
    {t:'Variation',s:'Biology',url:'/triple/foundation/biology/inheritance/variation.html',c:'#6BCB77'},
    {t:'Evolution and Natural Selection',s:'Biology',url:'/triple/foundation/biology/inheritance/evolution-natural-selection.html',c:'#6BCB77'},
    {t:'Theory of Evolution',s:'Biology',url:'/triple/foundation/biology/inheritance/theory-of-evolution.html',c:'#6BCB77'},
    {t:'Selective Breeding',s:'Biology',url:'/triple/foundation/biology/inheritance/selective-breeding.html',c:'#6BCB77'},
    {t:'Genetic Engineering',s:'Biology',url:'/triple/foundation/biology/inheritance/genetic-engineering.html',c:'#6BCB77'},
    {t:'Cloning',s:'Biology',url:'/triple/foundation/biology/inheritance/cloning.html',c:'#6BCB77'},
    {t:'Evidence for Evolution',s:'Biology',url:'/triple/foundation/biology/inheritance/evidence-for-evolution.html',c:'#6BCB77'},
    {t:'Mendel and the Development of Genetics',s:'Biology',url:'/triple/foundation/biology/inheritance/understanding-genetics.html',c:'#6BCB77'},
    {t:'Fossils and Extinction',s:'Biology',url:'/triple/foundation/biology/inheritance/fossils-extinction.html',c:'#6BCB77'},
    {t:'Resistant Bacteria',s:'Biology',url:'/triple/foundation/biology/inheritance/resistant-bacteria.html',c:'#6BCB77'},
    {t:'Classification of Living Organisms',s:'Biology',url:'/triple/foundation/biology/inheritance/classification-living-organisms.html',c:'#6BCB77'},
    {t:'Ecosystems',s:'Biology',url:'/triple/foundation/biology/ecology/ecosystems.html',c:'#6BCB77'},
    {t:'Abiotic and Biotic Factors',s:'Biology',url:'/triple/foundation/biology/ecology/abiotic-biotic-factors.html',c:'#6BCB77'},
    {t:'Adaptations',s:'Biology',url:'/triple/foundation/biology/ecology/adaptations.html',c:'#6BCB77'},
    {t:'Food Chains and Food Webs',s:'Biology',url:'/triple/foundation/biology/ecology/food-chains-webs.html',c:'#6BCB77'},
    {t:'Population and Competition',s:'Biology',url:'/triple/foundation/biology/ecology/population-competition.html',c:'#6BCB77'},
    {t:'Biodiversity',s:'Biology',url:'/triple/foundation/biology/ecology/biodiversity.html',c:'#6BCB77'},
    {t:'The Carbon Cycle',s:'Biology',url:'/triple/foundation/biology/ecology/carbon-cycle.html',c:'#6BCB77'},
    {t:'The Water Cycle',s:'Biology',url:'/triple/foundation/biology/ecology/water-cycle.html',c:'#6BCB77'},
    {t:'The Nitrogen Cycle',s:'Biology',url:'/triple/foundation/biology/ecology/nitrogen-cycle.html',c:'#6BCB77'},
    {t:'Decomposition',s:'Biology',url:'/triple/foundation/biology/ecology/decomposition.html',c:'#6BCB77'},
    {t:'Trophic Levels',s:'Biology',url:'/triple/foundation/biology/ecology/trophic-levels.html',c:'#6BCB77'},
    {t:'Pyramids of Biomass',s:'Biology',url:'/triple/foundation/biology/ecology/pyramids-of-biomass.html',c:'#6BCB77'},
    {t:'Transfer of Biomass',s:'Biology',url:'/triple/foundation/biology/ecology/transfer-of-biomass.html',c:'#6BCB77'},
    {t:'Sampling Techniques',s:'Biology',url:'/triple/foundation/biology/ecology/sampling-techniques.html',c:'#6BCB77'},
    {t:'Factors Affecting Food Security',s:'Biology',url:'/triple/foundation/biology/ecology/factors-affecting-food-security.html',c:'#6BCB77'},
    {t:'Farming Techniques',s:'Biology',url:'/triple/foundation/biology/ecology/farming-techniques.html',c:'#6BCB77'},
    {t:'Sustainable Fisheries',s:'Biology',url:'/triple/foundation/biology/ecology/sustainable-fisheries.html',c:'#6BCB77'},
    {t:'The Role of Biotechnology',s:'Biology',url:'/triple/foundation/biology/ecology/role-of-biotechnology.html',c:'#6BCB77'},
    // Triple Biology Higher
    {t:'Eukaryotes and Prokaryotes',s:'Biology',url:'/triple/higher/biology/cell-biology/eukaryotes-prokaryotes.html',c:'#6BCB77'},
    {t:'Animal and Plant Cells',s:'Biology',url:'/triple/higher/biology/cell-biology/animal-plant-cells.html',c:'#6BCB77'},
    {t:'Cell Specialisation and Differentiation',s:'Biology',url:'/triple/higher/biology/cell-biology/cell-specialisation.html',c:'#6BCB77'},
    {t:'Microscopy',s:'Biology',url:'/triple/higher/biology/cell-biology/microscopy.html',c:'#6BCB77'},
    {t:'Chromosomes, the Cell Cycle and Mitosis',s:'Biology',url:'/triple/higher/biology/cell-biology/chromosomes-mitosis.html',c:'#6BCB77'},
    {t:'Stem Cells',s:'Biology',url:'/triple/higher/biology/cell-biology/stem-cells.html',c:'#6BCB77'},
    {t:'Diffusion, Osmosis and Active Transport',s:'Biology',url:'/triple/higher/biology/cell-biology/transport-in-cells.html',c:'#6BCB77'},
    {t:'Culturing Microorganisms',s:'Biology',url:'/triple/higher/biology/cell-biology/culturing-microorganisms.html',c:'#6BCB77'},
    {t:'Principles of Organisation',s:'Biology',url:'/triple/higher/biology/organisation/principles-of-organisation.html',c:'#6BCB77'},
    {t:'The Digestive System',s:'Biology',url:'/triple/higher/biology/organisation/digestive-system.html',c:'#6BCB77'},
    {t:'Enzymes',s:'Biology',url:'/triple/higher/biology/organisation/enzymes.html',c:'#6BCB77'},
    {t:'The Heart and Blood Vessels',s:'Biology',url:'/triple/higher/biology/organisation/heart-blood-vessels.html',c:'#6BCB77'},
    {t:'Blood',s:'Biology',url:'/triple/higher/biology/organisation/blood.html',c:'#6BCB77'},
    {t:'Coronary Heart Disease',s:'Biology',url:'/triple/higher/biology/organisation/coronary-heart-disease.html',c:'#6BCB77'},
    {t:'Health, Disease and Risk Factors',s:'Biology',url:'/triple/higher/biology/organisation/health-disease.html',c:'#6BCB77'},
    {t:'Cancer',s:'Biology',url:'/triple/higher/biology/organisation/cancer.html',c:'#6BCB77'},
    {t:'Plant Tissues and Organs',s:'Biology',url:'/triple/higher/biology/organisation/plant-tissues.html',c:'#6BCB77'},
    {t:'Transpiration',s:'Biology',url:'/triple/higher/biology/organisation/transpiration.html',c:'#6BCB77'},
    {t:'Translocation',s:'Biology',url:'/triple/higher/biology/organisation/translocation.html',c:'#6BCB77'},
    {t:'Communicable Diseases and Human Defence Systems',s:'Biology',url:'/triple/higher/biology/infection-response/communicable-diseases-defence.html',c:'#6BCB77'},
    {t:'Viral Diseases',s:'Biology',url:'/triple/higher/biology/infection-response/viral-diseases.html',c:'#6BCB77'},
    {t:'Bacterial Diseases',s:'Biology',url:'/triple/higher/biology/infection-response/bacterial-diseases.html',c:'#6BCB77'},
    {t:'Fungal and Protist Diseases',s:'Biology',url:'/triple/higher/biology/infection-response/fungal-protist-diseases.html',c:'#6BCB77'},
    {t:'Vaccination',s:'Biology',url:'/triple/higher/biology/infection-response/vaccination.html',c:'#6BCB77'},
    {t:'Antibiotics and Painkillers',s:'Biology',url:'/triple/higher/biology/infection-response/antibiotics-painkillers.html',c:'#6BCB77'},
    {t:'Drug Discovery and Development',s:'Biology',url:'/triple/higher/biology/infection-response/drug-discovery-development.html',c:'#6BCB77'},
    {t:'Plant Disease Detection and Defence',s:'Biology',url:'/triple/higher/biology/infection-response/plant-disease-detection-defence.html',c:'#6BCB77'},
    {t:'Monoclonal Antibodies',s:'Biology',url:'/triple/higher/biology/infection-response/monoclonal-antibodies.html',c:'#6BCB77'},
    {t:'Photosynthesis',s:'Biology',url:'/triple/higher/biology/bioenergetics/photosynthesis.html',c:'#6BCB77'},
    {t:'Rate of Photosynthesis',s:'Biology',url:'/triple/higher/biology/bioenergetics/rate-of-photosynthesis.html',c:'#6BCB77'},
    {t:'Uses of Glucose from Photosynthesis',s:'Biology',url:'/triple/higher/biology/bioenergetics/uses-of-glucose.html',c:'#6BCB77'},
    {t:'Aerobic Respiration',s:'Biology',url:'/triple/higher/biology/bioenergetics/aerobic-respiration.html',c:'#6BCB77'},
    {t:'Anaerobic Respiration',s:'Biology',url:'/triple/higher/biology/bioenergetics/anaerobic-respiration.html',c:'#6BCB77'},
    {t:'Response to Exercise',s:'Biology',url:'/triple/higher/biology/bioenergetics/response-to-exercise.html',c:'#6BCB77'},
    {t:'Metabolism',s:'Biology',url:'/triple/higher/biology/bioenergetics/metabolism.html',c:'#6BCB77'},
    {t:'Homeostasis',s:'Biology',url:'/triple/higher/biology/homeostasis/homeostasis.html',c:'#6BCB77'},
    {t:'The Human Nervous System',s:'Biology',url:'/triple/higher/biology/homeostasis/nervous-system.html',c:'#6BCB77'},
    {t:'Reflex Actions',s:'Biology',url:'/triple/higher/biology/homeostasis/reflex-actions.html',c:'#6BCB77'},
    {t:'Thermoregulation',s:'Biology',url:'/triple/higher/biology/homeostasis/thermoregulation.html',c:'#6BCB77'},
    {t:'The Endocrine System',s:'Biology',url:'/triple/higher/biology/homeostasis/endocrine-system.html',c:'#6BCB77'},
    {t:'Blood Glucose Control and Diabetes',s:'Biology',url:'/triple/higher/biology/homeostasis/blood-glucose-diabetes.html',c:'#6BCB77'},
    {t:'Human Reproduction and Hormones',s:'Biology',url:'/triple/higher/biology/homeostasis/human-reproduction-hormones.html',c:'#6BCB77'},
    {t:'Contraception and Fertility Treatment',s:'Biology',url:'/triple/higher/biology/homeostasis/contraception-fertility.html',c:'#6BCB77'},
    {t:'Reaction Time',s:'Biology',url:'/triple/higher/biology/homeostasis/reaction-time.html',c:'#6BCB77'},
    {t:'The Brain',s:'Biology',url:'/triple/higher/biology/homeostasis/the-brain.html',c:'#6BCB77'},
    {t:'The Eye',s:'Biology',url:'/triple/higher/biology/homeostasis/the-eye.html',c:'#6BCB77'},
    {t:'Defects of the Eye',s:'Biology',url:'/triple/higher/biology/homeostasis/defects-of-the-eye.html',c:'#6BCB77'},
    {t:'Sexual and Asexual Reproduction',s:'Biology',url:'/triple/higher/biology/inheritance/sexual-asexual-reproduction.html',c:'#6BCB77'},
    {t:'Meiosis',s:'Biology',url:'/triple/higher/biology/inheritance/meiosis.html',c:'#6BCB77'},
    {t:'Advantages and Disadvantages of Sexual and Asexual Reproduction',s:'Biology',url:'/triple/higher/biology/inheritance/advantages-sexual-asexual.html',c:'#6BCB77'},
    {t:'DNA and the Genome',s:'Biology',url:'/triple/higher/biology/inheritance/dna-genome.html',c:'#6BCB77'},
    {t:'DNA Structure',s:'Biology',url:'/triple/higher/biology/inheritance/dna-structure.html',c:'#6BCB77'},
    {t:'Genetic Inheritance',s:'Biology',url:'/triple/higher/biology/inheritance/genetic-inheritance.html',c:'#6BCB77'},
    {t:'Inherited Disorders',s:'Biology',url:'/triple/higher/biology/inheritance/inherited-disorders.html',c:'#6BCB77'},
    {t:'Sex Determination',s:'Biology',url:'/triple/higher/biology/inheritance/sex-determination.html',c:'#6BCB77'},
    {t:'Variation',s:'Biology',url:'/triple/higher/biology/inheritance/variation.html',c:'#6BCB77'},
    {t:'Evolution and Natural Selection',s:'Biology',url:'/triple/higher/biology/inheritance/evolution-natural-selection.html',c:'#6BCB77'},
    {t:'Theory of Evolution',s:'Biology',url:'/triple/higher/biology/inheritance/theory-of-evolution.html',c:'#6BCB77'},
    {t:'Selective Breeding',s:'Biology',url:'/triple/higher/biology/inheritance/selective-breeding.html',c:'#6BCB77'},
    {t:'Genetic Engineering',s:'Biology',url:'/triple/higher/biology/inheritance/genetic-engineering.html',c:'#6BCB77'},
    {t:'Cloning',s:'Biology',url:'/triple/higher/biology/inheritance/cloning.html',c:'#6BCB77'},
    {t:'Evidence for Evolution',s:'Biology',url:'/triple/higher/biology/inheritance/evidence-for-evolution.html',c:'#6BCB77'},
    {t:'Mendel and the Development of Genetics',s:'Biology',url:'/triple/higher/biology/inheritance/understanding-genetics.html',c:'#6BCB77'},
    {t:'Fossils and Extinction',s:'Biology',url:'/triple/higher/biology/inheritance/fossils-extinction.html',c:'#6BCB77'},
    {t:'Resistant Bacteria',s:'Biology',url:'/triple/higher/biology/inheritance/resistant-bacteria.html',c:'#6BCB77'},
    {t:'Classification of Living Organisms',s:'Biology',url:'/triple/higher/biology/inheritance/classification-living-organisms.html',c:'#6BCB77'},
    {t:'Ecosystems',s:'Biology',url:'/triple/higher/biology/ecology/ecosystems.html',c:'#6BCB77'},
    {t:'Abiotic and Biotic Factors',s:'Biology',url:'/triple/higher/biology/ecology/abiotic-biotic-factors.html',c:'#6BCB77'},
    {t:'Adaptations',s:'Biology',url:'/triple/higher/biology/ecology/adaptations.html',c:'#6BCB77'},
    {t:'Food Chains and Food Webs',s:'Biology',url:'/triple/higher/biology/ecology/food-chains-webs.html',c:'#6BCB77'},
    {t:'Population and Competition',s:'Biology',url:'/triple/higher/biology/ecology/population-competition.html',c:'#6BCB77'},
    {t:'Biodiversity',s:'Biology',url:'/triple/higher/biology/ecology/biodiversity.html',c:'#6BCB77'},
    {t:'The Carbon Cycle',s:'Biology',url:'/triple/higher/biology/ecology/carbon-cycle.html',c:'#6BCB77'},
    {t:'The Water Cycle',s:'Biology',url:'/triple/higher/biology/ecology/water-cycle.html',c:'#6BCB77'},
    {t:'The Nitrogen Cycle',s:'Biology',url:'/triple/higher/biology/ecology/nitrogen-cycle.html',c:'#6BCB77'},
    {t:'Decomposition',s:'Biology',url:'/triple/higher/biology/ecology/decomposition.html',c:'#6BCB77'},
    {t:'Trophic Levels',s:'Biology',url:'/triple/higher/biology/ecology/trophic-levels.html',c:'#6BCB77'},
    {t:'Pyramids of Biomass',s:'Biology',url:'/triple/higher/biology/ecology/pyramids-of-biomass.html',c:'#6BCB77'},
    {t:'Transfer of Biomass',s:'Biology',url:'/triple/higher/biology/ecology/transfer-of-biomass.html',c:'#6BCB77'},
    {t:'Sampling Techniques',s:'Biology',url:'/triple/higher/biology/ecology/sampling-techniques.html',c:'#6BCB77'},
    {t:'The Impact of Environmental Change',s:'Biology',url:'/triple/higher/biology/ecology/environmental-change.html',c:'#6BCB77'},
    {t:'Factors Affecting Food Security',s:'Biology',url:'/triple/higher/biology/ecology/factors-affecting-food-security.html',c:'#6BCB77'},
    {t:'Farming Techniques',s:'Biology',url:'/triple/higher/biology/ecology/farming-techniques.html',c:'#6BCB77'},
    {t:'Sustainable Fisheries',s:'Biology',url:'/triple/higher/biology/ecology/sustainable-fisheries.html',c:'#6BCB77'},
    {t:'The Role of Biotechnology',s:'Biology',url:'/triple/higher/biology/ecology/role-of-biotechnology.html',c:'#6BCB77'},
  ];
  const input = document.getElementById('siteSearch');
  const results = document.getElementById('searchResults');
  if (!input) return;
  input.addEventListener('input', function() {
    const q = this.value.trim().toLowerCase();
    if (q.length < 2) { results.classList.remove('open'); return; }
    const matches = INDEX.filter(item => item.t.toLowerCase().includes(q) || item.s.toLowerCase().includes(q)).slice(0,8);
    if (!matches.length) { results.classList.remove('open'); return; }
    results.innerHTML = matches.map(m =>
      '<a class="search-result-item" href="' + m.url + '">' +
      '<span class="search-result-subject" style="background:' + m.c + '22;color:' + m.c + '">' + m.s + '</span>' +
      '<span>' + m.t + '</span></a>'
    ).join('');
    results.classList.add('open');
  });
  document.addEventListener('click', e => { if (!e.target.closest('.hero-search')) results.classList.remove('open'); });
})();
</script>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>MrBadmusAI — GCSE Science Revision</title>
  <meta name="description" content="Free GCSE Science revision with AI tutor, FIFA worked examples, quizzes and full topic notes. Physics, Chemistry, Biology."/>
  <link rel="stylesheet" href="/shared/styles.css"/>
</head>
<body>
  {nav_html()}
  {body}
  {chat_html()}
  <script src="/shared/mrbadmus.js"></script>
  <script>MrBadmus.init({{ subject: 'physics' }});</script>
</body>
</html>"""


# ─────────────────────────────────────────────
#  PATHWAY PAGE — /combined/index.html etc
# ─────────────────────────────────────────────

def make_pathway_page(pathway):
    """Combined Science or Triple Science landing — choose Foundation or Higher."""
    pc = PATHWAY_COLORS[pathway]
    label = "Combined Science" if pathway == "combined" else "Triple Science"
    emoji = "🔬" if pathway == "combined" else "⚗️"
    description = {
        "combined": "The Combined Science qualification covers all three sciences in one course. Choose your tier below.",
        "triple":   "Triple Science covers separate Biology, Chemistry and Physics qualifications with extended content. Choose your tier below.",
    }[pathway]

    body = f"""
<div class="hub-header">
  <a class="back-link" href="/index.html">← Back to Home</a>
  <h1 style="color:{pc}">{emoji} {label}</h1>
  <p>{description}</p>
</div>

<div class="tier-grid">
  <a class="tier-card foundation" href="/{pathway}/foundation/index.html">
    <div style="font-size:2.5rem;margin-bottom:12px;">📗</div>
    <h2 style="color:#6BCB77;margin-bottom:10px;">Foundation Tier</h2>
    <p style="color:var(--muted);font-size:0.88rem;line-height:1.6;">Core content for grades 1–5. All the key facts, equations and required practicals you need.</p>
    <div style="margin-top:20px;">
      <span style="background:#6BCB77;color:#0F0F1A;padding:7px 18px;border-radius:20px;font-size:0.82rem;font-weight:800;">Foundation →</span>
    </div>
  </a>

  <a class="tier-card higher" href="/{pathway}/higher/index.html">
    <div style="font-size:2.5rem;margin-bottom:12px;">📙</div>
    <h2 style="color:#FFD93D;margin-bottom:10px;">Higher Tier</h2>
    <p style="color:var(--muted);font-size:0.88rem;line-height:1.6;">Foundation content plus Higher-only material for grades 4–9. More equations, more depth.</p>
    <div style="margin-top:20px;">
      <span style="background:#FFD93D;color:#0F0F1A;padding:7px 18px;border-radius:20px;font-size:0.82rem;font-weight:800;">Higher →</span>
    </div>
  </a>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{label} | MrBadmusAI</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
</head>
<body>
  {nav_html(pathway=pathway)}
  {body}
  {chat_html()}
  <script src="/shared/mrbadmus.js"></script>
  <script>MrBadmus.init({{ subject: 'physics' }});</script>
</body>
</html>"""


# ─────────────────────────────────────────────
#  TIER PAGE — /combined/foundation/index.html
# ─────────────────────────────────────────────

def make_tier_page(pathway, tier):
    """Choose Physics / Chemistry / Biology within a pathway+tier."""
    pc = PATHWAY_COLORS[pathway]
    tc = TIER_COLORS[tier]
    pathway_label = "Combined Science" if pathway == "combined" else "Triple Science"

    subject_cards = ""
    for subj in ["physics", "chemistry", "biology"]:
        data = SITE_DATA[subj]
        topic_ids = PATHWAY_TOPIC_MAP[(pathway, tier)][subj]
        topic_count = len(topic_ids)
        sc = data["color"]
        subject_cards += f"""
<a class="subject-card {subj[:3]}" href="/{pathway}/{tier}/{subj}/index.html" style="border-color:rgba({','.join(str(int(sc.lstrip('#')[i:i+2],16)) for i in (0,2,4))},0.4);">
  <span class="subject-icon">{data['emoji']}</span>
  <h2 style="color:{sc}">{data['label']}</h2>
  <p>{tier.title()} tier — {topic_count} topic{'s' if topic_count!=1 else ''}</p>
  <span class="btn" style="background:{sc};">Explore {data['label']} →</span>
</a>"""

    body = f"""
<div class="hub-header">
  <a class="back-link" href="/{pathway}/index.html">← Back to {pathway_label}</a>
  <h1 style="color:{tc}">{'📗' if tier=='foundation' else '📙'} {tier.title()} Tier</h1>
  <p style="color:var(--muted);">{pathway_label} — select a subject</p>
</div>
<div class="subject-grid">
  {subject_cards}
</div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{pathway_label} {tier.title()} | MrBadmusAI</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
</head>
<body>
  {nav_html(pathway=pathway, tier=tier)}
  {body}
  {chat_html()}
  <script src="/shared/mrbadmus.js"></script>
  <script>MrBadmus.init({{ subject: 'physics' }});</script>
</body>
</html>"""



# ─────────────────────────────────────────────
#  SUBJECT HUB — /combined/foundation/physics/index.html
# ─────────────────────────────────────────────

def make_pathway_hub(pathway, tier, subject):
    """Subject topic list within a pathway/tier."""
    data = SITE_DATA[subject]
    color = data["color"]
    emoji = data["emoji"]
    label = data["label"]
    pathway_label = "Combined Science" if pathway == "combined" else "Triple Science"

    topic_ids = PATHWAY_TOPIC_MAP[(pathway, tier)][subject]
    topics = [t for t in data["topics"] if t["id"] in topic_ids]

    cards = ""
    for t in topics:
        badges = ""
        if t.get("rp"): badges += f'<span class="badge badge-rp">📋 {len(t["rp"])} RP</span>'
        if t.get("higher") and tier == "higher": badges += f'<span class="badge badge-h">⭐ Higher</span>'
        if t.get("triple_only") and pathway == "triple": badges += f'<span class="badge badge-t">🔬 Triple</span>'

        cards += f"""
<a class="topic-card" href="/{pathway}/{tier}/{subject}/{t['id']}.html">
  <div class="topic-card-head">
    <h3>{t['title']}</h3>
  </div>
  <div class="topic-card-meta">Spec {t['spec']} &nbsp;·&nbsp; Paper {t['paper']}</div>
  <div>{badges}</div>
  <div class="topic-card-footer">
    <span class="go-btn" style="background:{color};color:#0F0F1A;padding:7px 18px;border-radius:20px;font-size:0.82rem;font-weight:800;">Study this topic →</span>
  </div>
</a>"""

    body = f"""
<div class="hub-header">
  <a class="back-link" href="/{pathway}/{tier}/index.html">← Back to {tier.title()} Tier</a>
  <h1 style="color:{color}">{emoji} {label}</h1>
  <p>{pathway_label} — {tier.title()} Tier — {len(topics)} topics</p>
</div>
<div class="topic-grid">
  {cards}
</div>"""

    return page_shell(f"{label} | {tier.title()} | {pathway_label} | MrBadmusAI",
                      subject, body, pathway=pathway, tier=tier)


# ─────────────────────────────────────────────
#  TOPIC PAGE — /combined/foundation/physics/energy.html
# ─────────────────────────────────────────────

def make_pathway_topic_page(pathway, tier, subject, topic):
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
  <h1 style="color:{color}">{emoji} {topic['title']}</h1>
  <span class="spec-pill">Spec {topic['spec']}</span>
  <span class="paper-pill">Paper {topic['paper']}</span>
  <span class="badge" style="background:rgba(255,255,255,0.08);margin-left:6px;font-size:0.75rem;">{'📗 Foundation' if tier=='foundation' else '📙 Higher'}</span>
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
    <div class="card" style="text-align:center;padding:32px;">
      <p style="font-size:1.1rem;margin-bottom:8px;">Stuck on <strong>{topic['title']}</strong>? Ask me anything!</p>
      <p style="color:var(--muted);font-size:0.9rem;margin-bottom:20px;">I'll use FIFA for calculations and flag Higher/Triple content clearly.</p>
      <button data-open-chat style="background:{color};color:#0F0F1A;border:none;padding:14px 32px;border-radius:50px;font-size:1rem;font-weight:800;cursor:pointer;font-family:'Nunito',sans-serif;">💬 Ask Mr Badmus AI</button>
    </div>
  </div>

  {subtopic_nav_html}

</div>"""

    return page_shell(f"{topic['title']} | {data['label']} | {tier.title()} | MrBadmusAI",
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
  <p style="margin-bottom:14px;font-size:0.95rem;font-style:italic;color:#ccc;">{ex['q']}</p>
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

PHYSICS_COLOR = "#4ECDC4"

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

    # Shuffle the definitions (right-hand side) so they don't appear in order
    indexed_pairs = list(enumerate(pairs))
    shuffled_defs = list(indexed_pairs)
    random.shuffle(shuffled_defs)

    items_html = ""
    for i, pair in shuffled_defs:
        term, content_item = pair
        items_html += f'<div class="match-def{" match-def-svg" if use_svg else ""}" data-index="{i}" draggable="true">{content_item}</div>\n'

    terms_html = ""
    for i, pair in enumerate(pairs):
        term, _ = pair
        terms_html += f'''<div class="match-target" data-index="{i}">
  <div class="match-term">{term}</div>
  <div class="match-drop" data-accepts="{i}">Drop here</div>
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
  <p style="margin-bottom:14px;font-size:0.95rem;font-style:italic;color:#ccc;">{fifa['question']}</p>
  {steps_html}
</div>"""
    return f"""<div class="section">
  <div class="section-title">⚽ FIFA Worked Examples</div>
  {boxes}
</div>"""


def make_new_quiz(quiz, color):
    import random
    if not quiz:
        return ""
    cards_html = ""
    for i, q in enumerate(quiz):
        # Shuffle options so correct answer isn't always option A
        opts = list(enumerate(q["opts"]))  # [(original_idx, (text, is_correct)), ...]
        random.shuffle(opts)

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

    score_messages = [
        "Keep going — re-read the theory and try again. You'll get there! 📖",
        "Not bad — review the sections you missed and have another go. 💪",
        "Decent effort! A bit more revision and you'll nail it. 🔄",
        "Good work! Just a couple of gaps to fill. Nearly there! 🌟",
        "Excellent! You've really got this topic down. 🏆",
    ]
    score_msgs_json = str(score_messages).replace("'", '"')

    return f"""<div class="section">
  <div class="section-title">🎯 Test Yourself</div>
  <div class="quiz-progress" id="quizProgress">Question 1 of {len(quiz)}</div>
  {cards_html}
  <div class="quiz-end-msg" id="quizEndMsg" style="display:none;margin-top:16px;padding:16px 20px;border-radius:12px;font-size:0.95rem;font-weight:700;text-align:center;"></div>
</div>
<script>
(function(){{
  const scoreMessages = {score_msgs_json};
  document.querySelectorAll('#qcard-0, #qcard-1, #qcard-2, #qcard-3, #qcard-4').forEach(():{{}});
  // handled by global quiz JS below
}})();
</script>"""


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
                lines_html += f"<div style='background:rgba(255,255,255,0.04);border-left:3px solid rgba(107,203,119,0.35);border-radius:6px;padding:9px 14px;margin:0 0 7px 0;font-size:0.93rem;line-height:1.75;color:var(--text);'>{line}</div>"
            else:
                lines_html += "<div style='height:4px;'></div>"
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
    <button data-open-chat style="background:{color};color:#0F0F1A;border:none;padding:14px 32px;border-radius:50px;font-size:1rem;font-weight:800;cursor:pointer;font-family:'Nunito',sans-serif;">💬 Ask Mr Badmus AI</button>
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
  {keynote_html}
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
.match-check-btn,.match-reset-btn {{ border:none;padding:10px 20px;border-radius:8px;cursor:pointer;font-weight:700;font-size:0.88rem;font-family:'Nunito',sans-serif; }}
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
  <title>{st['title']} | Electricity | Physics | MrBadmusAI</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
  {extra_css}
</head>
<body>
  {nav}
  {body}
  {chat}
  <script src="/shared/mrbadmus.js"></script>
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
      <button data-open-chat style="background:{color};color:#0F0F1A;border:none;padding:14px 32px;border-radius:50px;font-size:1rem;font-weight:800;cursor:pointer;font-family:'Nunito',sans-serif;">💬 Ask Mr Badmus AI</button>
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
  <title>Electricity | Physics | MrBadmusAI</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
  {extra_css}
</head>
<body>
  {nav}
  {body}
  {chat}
  <script src="/shared/mrbadmus.js"></script>
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
                lines_html += f"<div style='background:rgba(255,255,255,0.04);border-left:3px solid rgba(107,203,119,0.35);border-radius:6px;padding:9px 14px;margin:0 0 7px 0;font-size:0.93rem;line-height:1.75;color:var(--text);'>{line}</div>"
            else:
                lines_html += "<div style='height:4px;'></div>"
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
  <div class="card" style="text-align:center;padding:32px;">
    <p style="font-size:1.1rem;margin-bottom:8px;font-weight:700;">Stuck? Just ask! 💬</p>
    <p style="color:var(--muted);font-size:0.9rem;margin-bottom:20px;">I'll use FIFA for calculations and flag Higher/Triple content clearly.</p>
    <button data-open-chat style="background:{color};color:#0F0F1A;border:none;padding:14px 32px;border-radius:50px;font-size:1rem;font-weight:800;cursor:pointer;font-family:'Nunito',sans-serif;">💬 Ask Mr Badmus AI</button>
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
        endMsg.style.background = ratio === 1 ? 'rgba(107,203,119,0.15)' : ratio >= 0.6 ? 'rgba(255,217,61,0.12)' : 'rgba(255,107,107,0.12)';
        endMsg.style.color = ratio === 1 ? '#6BCB77' : ratio >= 0.6 ? '#FFD93D' : '#FF8888';
        endMsg.style.border = '1px solid ' + (ratio === 1 ? 'rgba(107,203,119,0.3)' : ratio >= 0.6 ? 'rgba(255,217,61,0.3)' : 'rgba(255,107,107,0.3)');
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
    const accepts = parseInt(drop.dataset.accepts);
    const placed = drop.querySelector('.match-def');
    if (placed && parseInt(placed.dataset.index) === accepts) {{
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

    body = f"""
<div class="topic-header">
  <a class="back-link" href="/{pathway}/{tier}/{subject}/{topic_id}.html">← Back to {topic_title}</a>
  <h1 style="color:{color}">{subject_emoji} {st['title']}</h1>
  <span class="spec-pill">Spec {st['spec']}</span>
  <span class="badge" style="background:rgba(255,255,255,0.08);margin-left:6px;font-size:0.75rem;">{tier_badge}</span>
</div>

<div class="content-area">

  <div class="section">
    <div class="section-title">📖 In-Depth Theory</div>
    {theory_html}
    {mistake_html}
  </div>

  {var_html}
  {eq_html}
  {keynote_html}
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
:root {{ --subject: {color}; }}
.section-title {{ color: var(--subject); }}
.var-table {{ display:flex;flex-direction:column;gap:8px; }}
.var-row {{ display:flex;align-items:center;gap:16px;padding:10px 16px;background:rgba(255,255,255,0.03);border-radius:8px;border-left:3px solid {color}; }}
.var-sym {{ font-family:'Courier New',monospace;font-size:1.1rem;font-weight:700;color:{color};min-width:28px; }}
.var-desc {{ font-size:0.9rem;color:var(--text); }}
.keynote-box {{ background:rgba(255,217,61,0.08);border:1px solid rgba(255,217,61,0.3);border-radius:10px;padding:16px 20px; }}
.mistake-box {{ background:rgba(255,107,107,0.08);border:1px solid rgba(255,107,107,0.3);border-radius:10px;padding:16px 20px;margin:16px 0; }}
.mistake-title {{ font-weight:800;color:#FF6B6B;margin-bottom:8px; }}
.higher-box {{ background:rgba(255,217,61,0.08);border-left:4px solid #FFD93D;padding:14px 18px;border-radius:8px;margin-bottom:10px; }}
.triple-box {{ background:rgba(78,205,196,0.08);border-left:4px solid #4ECDC4;padding:14px 18px;border-radius:8px;margin-bottom:10px; }}
.star-rating-card {{ padding:24px; }}
.stars-row {{ display:flex;gap:8px;margin:12px 0; }}
.star-btn {{ background:none;border:none;font-size:1.5rem;cursor:pointer;opacity:0.4;transition:opacity 0.2s,transform 0.1s; }}
.star-btn:hover,.star-btn.star-active {{ opacity:1; }}
.star-btn.star-active {{ transform:scale(1.15); }}
.star-labels {{ display:flex;justify-content:space-between;font-size:0.75rem;color:var(--muted);margin-bottom:8px; }}
.star-feedback {{ display:none;margin-top:10px;padding:10px 14px;background:rgba(255,255,255,0.05);border-radius:8px;font-size:0.88rem; }}
.quiz-progress {{ background:rgba(255,255,255,0.05);border-radius:8px;padding:8px 14px;font-size:0.82rem;color:var(--muted);margin-bottom:16px; }}
.quiz-card {{ background:var(--card);border-radius:12px;padding:20px;margin-bottom:16px;border:1px solid rgba(255,255,255,0.06); }}
.q-text {{ font-weight:700;margin-bottom:14px;line-height:1.5; }}
.quiz-options {{ display:flex;flex-direction:column;gap:8px; }}
.quiz-opt {{ background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:var(--text);padding:10px 16px;border-radius:8px;cursor:pointer;text-align:left;font-family:'Nunito',sans-serif;font-size:0.9rem;transition:all 0.15s; }}
.quiz-opt:hover {{ background:rgba(255,255,255,0.1); }}
.quiz-opt.correct {{ background:rgba(107,203,119,0.2);border-color:#6BCB77;color:#6BCB77; }}
.quiz-opt.wrong {{ background:rgba(255,107,107,0.2);border-color:#FF6B6B;color:#FF6B6B; }}
.quiz-fb {{ display:none;margin-top:12px;padding:10px 14px;border-radius:8px;font-size:0.88rem;line-height:1.6; }}
.quiz-fb.show {{ display:block; }}
.quiz-fb.correct-fb {{ background:rgba(107,203,119,0.15);border:1px solid rgba(107,203,119,0.3);color:#6BCB77; }}
.quiz-fb.wrong-fb {{ background:rgba(255,107,107,0.12);border:1px solid rgba(255,107,107,0.3);color:#FF8888; }}
.match-layout {{ display:flex;gap:20px;flex-wrap:wrap; }}
.match-targets {{ display:flex;flex-direction:column;gap:10px;flex:1;min-width:200px; }}
.match-target {{ display:flex;flex-direction:column;gap:6px; }}
.match-term {{ font-weight:700;font-size:0.9rem; }}
.match-drop {{ border:2px dashed rgba(255,255,255,0.2);border-radius:8px;padding:8px 12px;min-height:40px;font-size:0.82rem;color:var(--muted);cursor:pointer;transition:all 0.15s; }}
.match-drop.drag-over {{ border-color:{color};background:rgba(78,205,196,0.08); }}
.match-drop.has-item {{ color:var(--text);border-style:solid;border-color:rgba(255,255,255,0.2); }}
.match-drop.match-correct {{ border-color:#6BCB77;background:rgba(107,203,119,0.1); }}
.match-drop.match-wrong {{ border-color:#FF6B6B;background:rgba(255,107,107,0.1); }}
.match-defs {{ display:flex;flex-direction:column;gap:8px;flex:1;min-width:180px; }}
.match-def {{ background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);border-radius:8px;padding:8px 12px;cursor:grab;font-size:0.85rem;user-select:none;transition:opacity 0.15s; }}
.match-def:hover {{ background:rgba(255,255,255,0.12); }}
.match-def.dragging {{ opacity:0.5; }}
.match-check-btn,.match-reset-btn {{ padding:8px 18px;border-radius:8px;border:none;cursor:pointer;font-family:'Nunito',sans-serif;font-weight:700;font-size:0.85rem; }}
.match-check-btn {{ background:{color};color:#0F0F1A; }}
.match-reset-btn {{ background:rgba(255,255,255,0.08);color:var(--text); }}
.match-result {{ margin-top:12px;padding:10px 14px;border-radius:8px;font-size:0.88rem; }}
.match-result-win {{ background:rgba(107,203,119,0.15);color:#6BCB77; }}
.match-result-partial {{ background:rgba(255,107,107,0.12);color:#FF8888; }}
.fifa-label {{ font-size:0.75rem;font-weight:800;color:{color};text-transform:uppercase;letter-spacing:0.05em;margin-bottom:8px; }}
</style>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{st['title']} | {subject_label} | MrBadmusAI</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
  {extra_css}
</head>
<body>
  {nav_html(subject, pathway, tier)}
  {body}
  {chat_html()}
  <script src="/shared/mrbadmus.js"></script>
  <script>MrBadmus.init({{subject:'{subject}',topic:'{st["title"]} ({st["spec"]})'}});</script>
  <script>{quiz_js}</script>
  <script>{matching_js}</script>
  <script>{star_js}</script>
</body>
</html>"""



# ─────────────────────────────────────────────
#  UPDATED TOPIC PAGE — + button links to full subtopic page
#  Used for topics that have detailed subtopic data
# ─────────────────────────────────────────────

def make_pathway_topic_page_with_subtopics(pathway, tier, subject, topic, subtopics_list):
    """
    Topic page where each subtopic row has a + button that LINKS to the full subtopic page
    (rather than expanding inline). Used when subtopic detail pages exist.
    """
    data = SITE_DATA[subject]
    color = data["color"]
    emoji = data["emoji"]
    pathway_label = "Combined Science" if pathway == "combined" else "Triple Science"

    # Build subtopic rows with direct links
    subtopic_rows = ""
    for st in subtopics_list:
        st_url = f"/{pathway}/{tier}/{subject}/{topic['id']}/{st['id']}.html"
        subtopic_rows += f"""
<div class="subtopic-row" id="row-{st['id']}">
  <div class="subtopic-main">
    <a class="subtopic-link" href="{st_url}">
      <span class="subtopic-title">{st['title']}</span>
      <span style="font-size:0.78rem;color:var(--muted);">Spec {st['spec']}</span>
    </a>
    <a href="{st_url}" class="expand-btn" title="Open full notes" style="text-decoration:none;">+</a>
  </div>
</div>"""

    # Equations
    formula_pills = ""
    if topic.get("equations"):
        for eq in topic["equations"]:
            if "(Higher)" in eq and tier == "foundation":
                continue
            formula_pills += f'<div class="formula-pill">{eq}</div>\n'
    if not formula_pills:
        formula_pills = '<p style="color:var(--muted);font-size:0.9rem;">See individual subtopic pages for equations.</p>'

    # Next/Prev topic navigation
    topic_ids = PATHWAY_TOPIC_MAP[(pathway, tier)][subject]
    topics_in_path = [t for t in data["topics"] if t["id"] in topic_ids]
    curr_idx = next((i for i, t in enumerate(topics_in_path) if t["id"] == topic["id"]), None)

    nav_prev = nav_next = ""
    if curr_idx is not None:
        if curr_idx > 0:
            prev_t = topics_in_path[curr_idx - 1]
            nav_prev = f'<a class="nav-arrow prev" href="/{pathway}/{tier}/{subject}/{prev_t["id"]}.html"><span><div class="nav-arrow-label">Previous Topic</div><div class="nav-arrow-title">{prev_t["title"]}</div></span></a>'
        else:
            nav_prev = '<span></span>'
        if curr_idx < len(topics_in_path) - 1:
            next_t = topics_in_path[curr_idx + 1]
            nav_next = f'<a class="nav-arrow next" href="/{pathway}/{tier}/{subject}/{next_t["id"]}.html"><span><div class="nav-arrow-label">Next Topic</div><div class="nav-arrow-title">{next_t["title"]}</div></span></a>'
        else:
            nav_next = '<span></span>'

    topic_nav_html = f"""<div class="subtopic-nav" style="margin-top:32px;">
  {nav_prev}
  <a href="/{pathway}/{tier}/{subject}/index.html" style="font-size:0.8rem;color:var(--muted);text-decoration:none;">📋 All {data['label']} Topics</a>
  {nav_next}
</div>"""

    # Higher and triple sections
    higher_html = ""
    if tier == "higher" and topic.get("higher"):
        items = "".join(f'<div class="higher-box"><p>{h}</p></div>' for h in topic["higher"])
        higher_html = f'<div class="section"><div class="section-title">⭐ Higher Tier Content</div>{items}</div>'

    triple_html = ""
    if pathway == "triple" and topic.get("triple_only"):
        items = "".join(f'<div class="triple-box"><p>{tr}</p></div>' for tr in topic["triple_only"])
        triple_html = f'<div class="section"><div class="section-title">🔬 Triple Science Extensions</div>{items}</div>'

    tier_badge = '📗 Foundation' if tier == 'foundation' else '📙 Higher'

    extra_css = f"""<style>
:root {{ --subject: {color}; }}
.section-title {{ color: var(--subject); }}
.subtopic-list-new {{ display:flex;flex-direction:column; }}
.subtopic-row {{ border-bottom:1px solid rgba(255,255,255,0.06); }}
.subtopic-row:last-child {{ border-bottom:none; }}
.subtopic-main {{ display:flex;align-items:center;justify-content:space-between;padding:14px 20px;transition:background 0.15s; }}
.subtopic-main:hover {{ background:rgba(255,255,255,0.03); }}
.subtopic-link {{ display:flex;align-items:center;gap:12px;flex:1;text-decoration:none;color:var(--text);font-size:0.95rem;font-weight:600;transition:color 0.15s; }}
.subtopic-link:hover .subtopic-title {{ color:{color};text-decoration:underline; }}
.expand-btn {{ background:rgba(78,205,196,0.15);border:1px solid rgba(78,205,196,0.3);color:{color};width:28px;height:28px;border-radius:6px;font-size:1.2rem;font-weight:700;display:flex;align-items:center;justify-content:center;transition:all 0.2s;flex-shrink:0;margin-left:12px; }}
.expand-btn:hover {{ background:{color};color:#0F0F1A; }}
</style>"""

    body = f"""
<div class="topic-header">
  <a class="back-link" href="/{pathway}/{tier}/{subject}/index.html">← Back to {data['label']}</a>
  <h1 style="color:{color}">{emoji} {topic['title']}</h1>
  <span class="spec-pill">Spec {topic['spec']}</span>
  <span class="paper-pill">Paper {topic['paper']}</span>
  <span class="badge" style="background:rgba(255,255,255,0.08);margin-left:6px;font-size:0.75rem;">{tier_badge}</span>
</div>

<div class="content-area">

  <div class="section">
    <div class="section-title">📋 Subtopics — click any to open full notes</div>
    <div class="card" style="padding:0;overflow:hidden;">
      <div class="subtopic-list-new">{subtopic_rows}</div>
    </div>
    <p style="font-size:0.82rem;color:var(--muted);margin-top:10px;">💡 Click a subtopic title or the <strong>+</strong> button to open the full notes, quiz and examples.</p>
  </div>

  <div class="section">
    <div class="section-title">📐 Key Equations</div>
    <div class="formula-grid">{formula_pills}</div>
  </div>

  {higher_html}
  {triple_html}

  <div class="section">
    <div class="section-title">🤖 Ask Mr Badmus AI</div>
    <div class="card" style="text-align:center;padding:32px;">
      <p style="font-size:1.1rem;margin-bottom:16px;font-weight:700;">Got a question about {topic['title']}? 💬</p>
      <button data-open-chat style="background:{color};color:#0F0F1A;border:none;padding:14px 32px;border-radius:50px;font-size:1rem;font-weight:800;cursor:pointer;font-family:'Nunito',sans-serif;">💬 Ask Mr Badmus AI</button>
    </div>
  </div>

  {topic_nav_html}

</div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{topic['title']} | {data['label']} | MrBadmusAI</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
  {extra_css}
</head>
<body>
  {nav_html(subject, pathway, tier)}
  {body}
  {chat_html()}
  <script src="/shared/mrbadmus.js"></script>
  <script>MrBadmus.init({{subject:'{subject}',topic:'{topic["title"]} ({topic["spec"]})'}});</script>
</body>
</html>"""



# ─────────────────────────────────────────────
#  BUILD FUNCTION — v5 new structure
# ─────────────────────────────────────────────

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

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Directory structure
    dirs = [
        output_dir,
        f"{output_dir}/shared",
        f"{output_dir}/netlify/functions",
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

    with open(f"{output_dir}/shared/mrbadmus.js", "w") as f:
        f.write(SHARED_JS_PATCHED)
    print("  ✅ shared/mrbadmus.js")

    # ── Netlify ──
    with open(f"{output_dir}/netlify/functions/chat.js", "w") as f:
        f.write(NETLIFY_FUNCTION)
    with open(f"{output_dir}/netlify.toml", "w") as f:
        f.write(NETLIFY_TOML)
    print("  ✅ netlify config")

    # ── Auth pages — copy into output if they exist in repo root ──
    import shutil as _shutil, os as _os
    for _auth_file in ["auth.html", "profile-setup.html"]:
        _src = _auth_file
        _dst = f"{output_dir}/{_auth_file}"
        if _os.path.exists(_src):
            _shutil.copy2(_src, _dst)
            print(f"  ✅ {_auth_file}")
        else:
            print(f"  ⚠️  {_auth_file} not found — skipping")

    # ── Landing page ──
    with open(f"{output_dir}/index.html", "w") as f:
        f.write(make_landing())
    print("  ✅ index.html")
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

    # ── Copy to repo root ──
    for item in os.listdir(output_dir):
        s = os.path.join(output_dir, item)
        d = os.path.join(".", item)
        if item in ['.git', 'generate_site_v5.py', 'generate_site.py',
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
    print(f"  3. Push to GitHub → Netlify auto-deploys")


if __name__ == "__main__":
    build_site()

