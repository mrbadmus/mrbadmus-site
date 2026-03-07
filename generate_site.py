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
                "triple_only": [],
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
                "triple_only": [],
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
                "triple_only": [],
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
                "triple_only": ["Radio wave production and detection", "X-rays in medicine", "Lenses and magnification"],
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
                "triple_only": [],
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
                "triple_only": ["Intermolecular forces — van der Waals, dipole-dipole, hydrogen bonds"],
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
                "triple_only": ["Respiratory system — gas exchange details", "Blood clotting"],
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

# ─────────────────────────────────────────────
#  SHARED CSS — full design system
# ─────────────────────────────────────────────

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
  background: rgba(0,0,0,0.7);
  z-index: 200;
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
  padding: 16px;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.25s;
}
.chat-overlay.open { pointer-events: all; opacity: 1; }
.chat-modal {
  width: 420px;
  max-width: calc(100vw - 32px);
  height: min(580px, calc(100vh - 100px));
  background: var(--dark);
  border-radius: 20px;
  border: 1px solid rgba(255,255,255,0.1);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  box-shadow: 0 20px 80px rgba(0,0,0,0.8);
  transform: translateY(20px);
  transition: transform 0.25s;
}
.chat-overlay.open .chat-modal { transform: translateY(0); }
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
10. Format responses clearly with line breaks — never write a wall of text
11. If a student seems confused, offer to break it down further
12. Never give a one-word answer — always explain the physics/chemistry/biology`;

  const SUBJECT_PROMPTS = {
    physics: `${BASE_PROMPT}

CURRENT SUBJECT: AQA GCSE Physics (8463)

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

CURRENT SUBJECT: AQA GCSE Chemistry (8462)

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

CURRENT SUBJECT: AQA GCSE Biology (8461)

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
    document.getElementById('chatOverlay')?.classList.add('open');
    if (!chatInited) {
      chatInited = true;
      const sn = {physics:'Physics ⚡',chemistry:'Chemistry 🧪',biology:'Biology 🌿'}[currentSubject];
      addMsg('bot', `Hello! I\'m <strong>Mr. Badmus AI</strong> — your ${sn} tutor! 👋<br><br>I know the full AQA GCSE ${currentSubject} spec. Ask me anything — concepts, calculations, exam questions, or upload a photo of a question!<br><br>I always use <strong>FIFA</strong> for calculations and label Higher Tier and Triple content clearly.`);
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
#  HTML GENERATORS
# ─────────────────────────────────────────────

def nav_html(active=""):
    return f"""<nav class="nav">
  <a class="nav-brand" href="/index.html">⚗️ MrBadmusAI</a>
  <div class="nav-links">
    <a class="phy{' active' if active=='physics' else ''}" href="/physics/index.html">⚡ Physics</a>
    <a class="che{' active' if active=='chemistry' else ''}" href="/chemistry/index.html">🧪 Chemistry</a>
    <a class="bio{' active' if active=='biology' else ''}" href="/biology/index.html">🌿 Biology</a>
  </div>
</nav>"""

def chat_html():
    return """<button class="chat-fab" onclick="MrBadmus.open()" title="Ask Mr Badmus AI">🤖</button>

<div class="chat-overlay" id="chatOverlay">
  <div class="chat-modal">
    <div class="chat-head">
      <div class="chat-head-info">
        <h3>Mr. Badmus AI</h3>
        <p>AQA GCSE Science Tutor</p>
      </div>
      <button class="close-btn">✕</button>
    </div>
    <div class="chat-msgs" id="chatMsgs"></div>
    <div class="img-preview-row" id="imgPreviewRow">
      <img id="imgPreview" src="" alt="preview"/>
      <button onclick="document.getElementById('imgPreview').src='';document.getElementById('imgPreviewRow').style.display='none';">✕</button>
    </div>
    <div class="chat-input-row">
      <label for="imgInput" class="img-btn" title="Upload image">📷</label>
      <input type="file" id="imgInput" accept="image/*" style="display:none"/>
      <input type="text" id="ci" placeholder="Ask anything about this topic..."/>
      <button class="chat-send-btn">➤</button>
    </div>
  </div>
</div>"""

def page_shell(title, subject, body_html, topic_id="", topic_title=""):
    color = SITE_DATA[subject]["color"]
    label = SITE_DATA[subject]["label"]
    emoji = SITE_DATA[subject]["emoji"]
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
    .subject-tag {{ color: var(--subject); }}
  </style>
</head>
<body>
  {nav_html(subject)}
  {body_html}
  {chat_html()}
  <script src="/shared/mrbadmus.js"></script>
  <script>
    MrBadmus.init({{
      subject: '{subject}',
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

def make_landing():
    cards = ""
    for subj, data in SITE_DATA.items():
        count = len(data["topics"])
        cards += f"""
  <a class="subject-card {subj[:3]}" href="/{subj}/index.html">
    <span class="subject-icon">{data['emoji']}</span>
    <h2 style="color:{data['color']}">{data['label']}</h2>
    <p>AQA GCSE {data['label']} (AQA {data['code']}) — {count} topic{'s' if count!=1 else ''} covered</p>
    <span class="btn">Explore {data['label']} →</span>
  </a>"""

    body = f"""
<section class="hero">
  <h1>Welcome to <span class="hero-gradient">MrBadmusAI</span></h1>
  <p>Your AQA GCSE Science revision hub — Physics, Chemistry &amp; Biology covered with AI-powered help, FIFA worked examples and exam-ready content.</p>
</section>
<div class="subject-grid">
  {cards}
</div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>MrBadmusAI — AQA GCSE Science Revision</title>
  <link rel="stylesheet" href="/shared/styles.css"/>
</head>
<body>
  {nav_html()}
  {body}
  <script src="/shared/mrbadmus.js"></script>
  <script>MrBadmus.init({{ subject: 'physics' }});</script>
</body>
</html>"""

def make_hub(subject):
    data = SITE_DATA[subject]
    color = data["color"]
    topics = data["topics"]

    cards = ""
    for t in topics:
        badges = ""
        if t["rp"]: badges += f'<span class="badge badge-rp">📋 {len(t["rp"])} RP</span>'
        if t["higher"]: badges += f'<span class="badge badge-h">⭐ Higher</span>'
        if t["triple_only"]: badges += f'<span class="badge badge-t">🔬 Triple</span>'

        cards += f"""
<a class="topic-card" href="/{ subject}/{t['id']}.html">
  <div class="topic-card-head">
    <h3>{t['title']}</h3>
  </div>
  <div class="topic-card-meta">Spec {t['spec']} &nbsp;·&nbsp; Paper {t['paper']}</div>
  <div>{badges}</div>
  <div class="topic-card-footer">
    <span class="go-btn" style="background:{color};color:#0F0F1A;padding:7px 18px;border-radius:20px;font-size:0.82rem;font-weight:700;">Study this topic →</span>
  </div>
</a>"""

    body = f"""
<div class="hub-header">
  <h1 style="color:{color}">{data['emoji']} {data['label']}</h1>
  <p>AQA GCSE {data['label']} ({data['code']}) — select a topic to start studying</p>
</div>
<div class="topic-grid">
  {cards}
</div>"""

    return page_shell(f"{data['label']} Topics | MrBadmusAI", subject, body)

def make_topic_page(subject, topic):
    data = SITE_DATA[subject]
    color = data["color"]
    emoji = data["emoji"]

    # Build subtopics list
    subtopic_items = "\n".join(
        f'<li><span style="color:{color}">●</span> {s}</li>'
        for s in topic["subtopics"]
    )

    # Build formula pills
    formula_pills = "\n".join(
        f'<div class="formula-pill">{eq}</div>'
        for eq in topic["equations"]
    ) if topic["equations"] else '<p style="color:var(--muted);font-size:0.9rem;">No specific equations for this topic — see the formula sheet.</p>'

    # Build FIFA example (generic, topic-specific)
    fifa_example = make_fifa_example(subject, topic)

    # Build Higher boxes
    higher_html = ""
    for h in topic["higher"]:
        higher_html += f'<div class="higher-box"><p>{h}</p></div>'
    if not higher_html:
        higher_html = '<p style="color:var(--muted);font-size:0.9rem;">No Higher Tier extensions for this topic.</p>'

    # Build Triple boxes
    triple_html = ""
    for tr in topic["triple_only"]:
        triple_html += f'<div class="triple-box"><p>{tr}</p></div>'
    if not triple_html:
        triple_html = '<p style="color:var(--muted);font-size:0.9rem;">No Triple Science-only content for this topic.</p>'

    # Build RP section
    rp_html = ""
    for rp in topic["rp"]:
        rp_num = rp.split("—")[0].strip()
        rp_name = rp.split("—")[1].strip() if "—" in rp else rp
        rp_html += f"""
<div class="rp-card">
  <h4>🔬 {rp}</h4>
  <p style="font-size:0.88rem;color:var(--muted);">Required Practical — you need to know the method, variables, equipment and how to analyse results.</p>
  <p style="margin-top:8px;font-size:0.85rem;">
    <a href="https://www.youtube.com/results?search_query=AQA+GCSE+{rp_name.replace(' ','+')}" target="_blank" 
       style="color:{color};font-weight:700;">▶ Find tutorial videos on YouTube →</a>
  </p>
</div>"""
    if not rp_html:
        rp_html = '<p style="color:var(--muted);font-size:0.9rem;">No required practicals for this topic.</p>'

    # Build quiz
    quiz_html = make_quiz(subject, topic, color)

    body = f"""
<div class="topic-header">
  <a class="back-link" href="/{subject}/index.html">← Back to {data['label']}</a>
  <h1 style="color:{color}">{emoji} {topic['title']}</h1>
  <span class="spec-pill">Spec {topic['spec']}</span>
  <span class="paper-pill">Paper {topic['paper']}</span>
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
    {fifa_example}
  </div>

  <div class="section">
    <div class="section-title">⭐ Higher Tier Content</div>
    {higher_html}
  </div>

  <div class="section">
    <div class="section-title">🔬 Triple Science Extensions</div>
    {triple_html}
  </div>

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
      <p style="font-size:1.1rem;margin-bottom:16px;">Stuck on something? Ask me anything about <strong>{topic['title']}</strong>!</p>
      <p style="color:var(--muted);font-size:0.9rem;margin-bottom:20px;">I'll use FIFA for all calculations and label Higher Tier content clearly.</p>
      <button data-open-chat style="background:{color};color:#0F0F1A;border:none;padding:14px 32px;border-radius:50px;font-size:1rem;font-weight:800;cursor:pointer;font-family:'Nunito',sans-serif;">
        💬 Ask Mr Badmus AI
      </button>
    </div>
  </div>

</div>"""

    return page_shell(f"{topic['title']} | {data['label']} | MrBadmusAI", subject, body, topic["id"], topic["title"])


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

def build_site(output_dir="mrbadmus_site"):
    print(f"\n🏗️  Building MrBadmusAI site → {output_dir}/\n")

    # Clean and create dirs
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    dirs = [
        output_dir,
        f"{output_dir}/shared",
        f"{output_dir}/physics",
        f"{output_dir}/chemistry",
        f"{output_dir}/biology",
        f"{output_dir}/netlify/functions",
    ]
    for d in dirs:
        os.makedirs(d)

    # Write shared files
    with open(f"{output_dir}/shared/styles.css", "w") as f:
        f.write(SHARED_CSS)
    print("  ✅ shared/styles.css")

    with open(f"{output_dir}/shared/mrbadmus.js", "w") as f:
        f.write(SHARED_JS)
    print("  ✅ shared/mrbadmus.js")

    # Netlify
    with open(f"{output_dir}/netlify/functions/chat.js", "w") as f:
        f.write(NETLIFY_FUNCTION)
    print("  ✅ netlify/functions/chat.js")

    with open(f"{output_dir}/netlify.toml", "w") as f:
        f.write(NETLIFY_TOML)
    print("  ✅ netlify.toml")

    # Landing page
    with open(f"{output_dir}/index.html", "w") as f:
        f.write(make_landing())
    print("  ✅ index.html")

    # Subject hubs + topic pages
    total_pages = 0
    for subject in ["physics", "chemistry", "biology"]:
        with open(f"{output_dir}/{subject}/index.html", "w") as f:
            f.write(make_hub(subject))
        print(f"  ✅ {subject}/index.html")
        total_pages += 1

        for topic in SITE_DATA[subject]["topics"]:
            path = f"{output_dir}/{subject}/{topic['id']}.html"
            with open(path, "w") as f:
                f.write(make_topic_page(subject, topic))
            print(f"     ✅ {subject}/{topic['id']}.html")
            total_pages += 1

    # Copy all generated files to current directory for GitHub
    import shutil as _sh
    for item in os.listdir(output_dir):
        s = os.path.join(output_dir, item)
        d = os.path.join(".", item)
        if item in ['.git', 'generate_site.py', 'subtopic_generator.py']:
            continue
        if os.path.isdir(s):
            if os.path.exists(d):
                _sh.rmtree(d)
            _sh.copytree(s, d)
        else:
            _sh.copy2(s, d)

    print(f"\n🎉 Done! {total_pages} pages generated and copied to repo root")
    print(f"\nTotal structure:")
    print(f"  1 landing page")
    print(f"  3 subject hubs")
    print(f"  {total_pages - 4} topic pages")
    print(f"\nNext steps:")
    print(f"  1. cd {output_dir}")
    print(f"  2. Upload to GitHub")
    print(f"  3. Connect to Netlify")
    print(f"  4. Add ANTHROPIC_API_KEY to Netlify environment variables")
    print(f"  See DEPLOY.md for full instructions\n")

    # Count files
    file_count = sum(len(files) for _, _, files in os.walk(output_dir))
    print(f"  Total files: {file_count}")

if __name__ == "__main__":
    build_site()
