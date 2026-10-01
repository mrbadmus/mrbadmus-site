#!/usr/bin/env python3
"""ks4_batch_plan.py — the KS4 lesson-batch plan (docs/ks4/BATCH-PLAN.md).

    python3 tools/ks4_batch_plan.py            # print the plan to stdout
    python3 tools/ks4_batch_plan.py --write    # (re)write docs/ks4/BATCH-PLAN.md
    python3 tools/ks4_batch_plan.py --check    # exit 1 if the committed file differs

Deterministic, stdlib only, reads repo files only (no database, no network).

Inputs
  * the 264 KS4 subtopics and their audience — `ks4_data.classify()`, which is
    derived from `generate_site_v5.PATHWAY_TOPIC_MAP` + `all_subtopics_*.py`
  * the 14 pilot lessons — `ks4_lessons.LESSONS` (Batch 1, already live)
  * Rainford's KS4 sequence — the generated seed
    `supabase/seeds/20260906234500_rainford_ks4_overrides.sql`

The ordering rule, the calendar assumptions and the batching rule are stated in
the generated file's header; the constants below are the only knobs.
"""

import datetime as dt
import importlib
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

OUT = os.path.join(REPO, "docs", "ks4", "BATCH-PLAN.md")
SEED = os.path.join(REPO, "supabase", "seeds",
                    "20260906234500_rainford_ks4_overrides.sql")

# ── the calendar ─────────────────────────────────────────────────────────
# Rainford's 2026-27 academic_years row starts 2026-09-01 (docs/mrb336/RISKS.md
# A2, read from production). The backend's currentTeachingWeek()
# (assignment-compose.js) puts week 1 on the Sunday on or before start_date and
# rolls the number every Sunday 00:00 UK (MRB-330). Holidays are NOT skipped.
TODAY = dt.date(2026, 10, 1)
YEAR_START = dt.date(2026, 9, 1)
# No school calendar exists in either repo or in `Rainford SOW/`. Assumed
# (standard England / St Helens pattern, unverified): autumn half-term
# Mon 26 Oct – Fri 30 Oct 2026; autumn term ends Fri 18 Dec 2026.
HALF_TERM_HOLIDAY = dt.date(2026, 10, 26)
LAST_DAY_BEFORE_CHRISTMAS = dt.date(2026, 12, 18)

BATCH_MIN, BATCH_MAX = 12, 16
ROUTES = ("CF", "CH", "TF", "TH")
SUBJECTS = ("biology", "chemistry", "physics")
SUBJ_ABBR = {"biology": "Bi", "chemistry": "Ch", "physics": "Ph",
             "Biology": "Bi", "Chemistry": "Ch", "Physics": "Ph"}


def week0():
    d = YEAR_START
    return d - dt.timedelta(days=(d.weekday() + 1) % 7)   # Sunday on/before


def teaching_week(day):
    sunday = day - dt.timedelta(days=(day.weekday() + 1) % 7)
    return (sunday - week0()).days // 7 + 1


def week_monday(week):
    return week0() + dt.timedelta(days=7 * (week - 1) + 1)


NOW_WEEK = teaching_week(TODAY)
HALF_TERM_WEEK = teaching_week(HALF_TERM_HOLIDAY)
XMAS_LAST_WEEK = teaching_week(LAST_DAY_BEFORE_CHRISTMAS)

# ── AQA spec refs, authored ─────────────────────────────────────────────
# slug → (separate-science ref, 8464 Trilogy ref or None).
# The separate ref (8461 Bi / 8462 Ch / 8463 Ph, all "4.x") is also the SORT
# key: the separate specs are the superset, so their numbering orders every
# subtopic, and Trilogy's numbering preserves that order. A trailing "?" marks
# a ref this plan is not sure of. The data's own `spec` field is mixed
# (8464 for most, 846x for some Triple pages, coarse or wrong for others —
# e.g. static-charge '6.2.5', motion-in-a-circle '6.5.6'), so it is shown
# nowhere and only informed these.
SPEC = {
    # biology — 8461 / 8464
    "eukaryotes-prokaryotes": ("4.1.1.1", "4.1.1.1"),
    "animal-plant-cells": ("4.1.1.2", "4.1.1.2"),
    "cell-specialisation": ("4.1.1.3–4.1.1.4", "4.1.1.3–4.1.1.4"),
    "microscopy": ("4.1.1.5", "4.1.1.5"),
    "culturing-microorganisms": ("4.1.1.6", None),
    "chromosomes-mitosis": ("4.1.2.1–4.1.2.2", "4.1.2.1–4.1.2.2"),
    "stem-cells": ("4.1.2.3", "4.1.2.3"),
    "transport-in-cells": ("4.1.3.1–4.1.3.3", "4.1.3.1–4.1.3.3"),
    "principles-of-organisation": ("4.2.1", "4.2.1"),
    "digestive-system": ("4.2.2.1", "4.2.2.1"),
    "enzymes": ("4.2.2.1", "4.2.2.1"),
    "heart-blood-vessels": ("4.2.2.2", "4.2.2.2"),
    "blood": ("4.2.2.3", "4.2.2.3"),
    "coronary-heart-disease": ("4.2.2.4", "4.2.2.4"),
    "health-disease": ("4.2.2.5–4.2.2.6", "4.2.2.5–4.2.2.6"),
    "cancer": ("4.2.2.7", "4.2.2.7"),
    "plant-tissues": ("4.2.3.1", "4.2.3.1"),
    "transpiration": ("4.2.3.2", "4.2.3.2"),
    "translocation": ("4.2.3.2", "4.2.3.2"),
    "communicable-diseases-defence": ("4.3.1.1", "4.3.1.1"),
    "viral-diseases": ("4.3.1.2", "4.3.1.2"),
    "bacterial-diseases": ("4.3.1.3", "4.3.1.3"),
    "fungal-protist-diseases": ("4.3.1.4–4.3.1.5", "4.3.1.4–4.3.1.5"),
    "vaccination": ("4.3.1.7", "4.3.1.7"),
    "antibiotics-painkillers": ("4.3.1.8", "4.3.1.8"),
    "drug-discovery-development": ("4.3.1.9", "4.3.1.9"),
    "monoclonal-antibodies": ("4.3.2.1–4.3.2.2", None),
    "plant-disease-detection-defence": ("4.3.3.1–4.3.3.2", None),
    "photosynthesis": ("4.4.1.1", "4.4.1.1"),
    "rate-of-photosynthesis": ("4.4.1.2", "4.4.1.2"),
    "uses-of-glucose": ("4.4.1.3", "4.4.1.3"),
    "aerobic-respiration": ("4.4.2.1", "4.4.2.1"),
    "anaerobic-respiration": ("4.4.2.1", "4.4.2.1"),
    "response-to-exercise": ("4.4.2.2", "4.4.2.2"),
    "metabolism": ("4.4.2.3", "4.4.2.3"),
    "homeostasis": ("4.5.1", "4.5.1"),
    "nervous-system": ("4.5.2.1", "4.5.2.1"),
    "reflex-actions": ("4.5.2.1", "4.5.2.1"),
    "reaction-time": ("4.5.2.1", "4.5.2.1"),
    "the-brain": ("4.5.2.2", None),
    "the-eye": ("4.5.2.3", None),
    "defects-of-the-eye": ("4.5.2.3", None),
    "thermoregulation": ("4.5.2.4", None),
    "endocrine-system": ("4.5.3.1", "4.5.3.1"),
    "blood-glucose-diabetes": ("4.5.3.2", "4.5.3.2"),
    "human-reproduction-hormones": ("4.5.3.4", "4.5.3.3"),
    "contraception-fertility": ("4.5.3.5–4.5.3.6", "4.5.3.4–4.5.3.5"),
    "sexual-asexual-reproduction": ("4.6.1.1", "4.6.1.1"),
    "meiosis": ("4.6.1.2", "4.6.1.2"),
    "advantages-sexual-asexual": ("4.6.1.3", None),
    "dna-genome": ("4.6.1.4", "4.6.1.3"),
    "dna-structure": ("4.6.1.5", None),
    "genetic-inheritance": ("4.6.1.6", "4.6.1.4"),
    "inherited-disorders": ("4.6.1.7", "4.6.1.5"),
    "sex-determination": ("4.6.1.8", "4.6.1.6"),
    "variation": ("4.6.2.1", "4.6.2.1"),
    "evolution-natural-selection": ("4.6.2.2", "4.6.2.2"),
    "selective-breeding": ("4.6.2.3", "4.6.2.3"),
    "genetic-engineering": ("4.6.2.4", "4.6.2.4"),
    "cloning": ("4.6.2.5", None),
    "theory-of-evolution": ("4.6.3.1–4.6.3.2", None),
    "understanding-genetics": ("4.6.3.3", None),
    "evidence-for-evolution": ("4.6.3.4", "4.6.3.1"),
    "fossils-extinction": ("4.6.3.5–4.6.3.6", "4.6.3.2–4.6.3.3"),
    "resistant-bacteria": ("4.6.3.7", "4.6.3.4"),
    "classification-living-organisms": ("4.6.4", "4.6.4"),
    "ecosystems": ("4.7.1.1", "4.7.1.1"),
    "population-competition": ("4.7.1.1", "4.7.1.1"),
    "abiotic-biotic-factors": ("4.7.1.2–4.7.1.3", "4.7.1.2–4.7.1.3"),
    "adaptations": ("4.7.1.4", "4.7.1.4"),
    "food-chains-webs": ("4.7.2.1", "4.7.2.1"),
    "sampling-techniques": ("4.7.2.1", "4.7.2.1"),
    "carbon-cycle": ("4.7.2.2", "4.7.2.2"),
    "water-cycle": ("4.7.2.2", "4.7.2.2"),
    "decomposition": ("4.7.2.3", "4.7.2.2?"),
    "environmental-change": ("4.7.2.4", None),
    "biodiversity": ("4.7.3.1", "4.7.3.1"),
    "waste-management": ("4.7.3.2", "4.7.3.2"),
    "land-use": ("4.7.3.3", "4.7.3.3"),
    "deforestation": ("4.7.3.4", "4.7.3.4"),
    "global-warming": ("4.7.3.5", "4.7.3.5"),
    "maintaining-biodiversity": ("4.7.3.6", "4.7.3.6"),
    "trophic-levels": ("4.7.4.1", None),
    "pyramids-of-biomass": ("4.7.4.2", None),
    "transfer-of-biomass": ("4.7.4.3", None),
    "factors-affecting-food-security": ("4.7.5.1", None),
    "farming-techniques": ("4.7.5.2", None),
    "sustainable-fisheries": ("4.7.5.3", None),
    "role-of-biotechnology": ("4.7.5.4", None),
    # chemistry — 8462 / 8464
    "atoms-elements-compounds": ("4.1.1.1", "5.1.1.1"),
    "mixtures": ("4.1.1.2", "5.1.1.2"),
    "model-of-the-atom": ("4.1.1.3", "5.1.1.3"),
    "subatomic-particles": ("4.1.1.4–4.1.1.5", "5.1.1.4–5.1.1.5"),
    "relative-atomic-mass": ("4.1.1.6", "5.1.1.6"),
    "electronic-structure": ("4.1.1.7", "5.1.1.7"),
    "periodic-table": ("4.1.2.1", "5.1.2.1"),
    "development-periodic-table": ("4.1.2.2", "5.1.2.2"),
    "metals-non-metals": ("4.1.2.3", "5.1.2.3"),
    "group-0": ("4.1.2.4", "5.1.2.4"),
    "group-1": ("4.1.2.5", "5.1.2.5"),
    "group-7": ("4.1.2.6", "5.1.2.6"),
    "transition-metals": ("4.1.3.1–4.1.3.2", None),
    "chemical-bonds": ("4.2.1.1", "5.2.1.1"),
    "ionic-bonding": ("4.2.1.2", "5.2.1.2"),
    "ionic-compounds": ("4.2.1.3", "5.2.1.3"),
    "covalent-bonding": ("4.2.1.4", "5.2.1.4"),
    "metallic-bonding": ("4.2.1.5", "5.2.1.5"),
    "states-of-matter": ("4.2.2.1–4.2.2.2", "5.2.2.1–5.2.2.2"),
    "properties-ionic-compounds": ("4.2.2.3", "5.2.2.3"),
    "properties-small-molecules": ("4.2.2.4", "5.2.2.4"),
    "polymers": ("4.2.2.5", "5.2.2.5"),
    "giant-covalent-structures": ("4.2.2.6", "5.2.2.6"),
    "metals-alloys": ("4.2.2.7–4.2.2.8", "5.2.2.7–5.2.2.8"),
    "nanoparticles": ("4.2.4", None),
    "conservation-of-mass": ("4.3.1.1", "5.3.1.1"),
    "relative-formula-mass": ("4.3.1.2", "5.3.1.2"),
    "mass-changes-reactions": ("4.3.1.3", "5.3.1.3"),
    "chemical-measurements": ("4.3.1.4", "5.3.1.4"),
    "moles": ("4.3.2.1", "5.3.2.1"),
    "amounts-in-equations": ("4.3.2.2", "5.3.2.2"),
    "using-moles-calculations": ("4.3.2.3–4.3.2.4", "5.3.2.3–5.3.2.4"),
    "concentration-of-solutions": ("4.3.2.5", "5.3.2.5"),
    "percentage-yield": ("4.3.3.1", None),
    "atom-economy": ("4.3.3.2", None),
    "reactivity-series": ("4.4.1.1–4.4.1.2", "5.4.1.1–5.4.1.2"),
    "extraction-of-metals": ("4.4.1.3", "5.4.1.3"),
    "oxidation-reduction": ("4.4.1.4", "5.4.1.4"),
    "reactions-of-acids": ("4.4.2.1–4.4.2.2", "5.4.2.1–5.4.2.2"),
    "salts-neutralisation": ("4.4.2.3", "5.4.2.3"),
    "ph-scale": ("4.4.2.4", "5.4.2.4"),
    "titrations": ("4.4.2.5", None),
    "strong-weak-acids": ("4.4.2.6", "5.4.2.5"),
    "electrolysis-principles": ("4.4.3.1", "5.4.3.1"),
    "electrolysis-molten": ("4.4.3.2", "5.4.3.2"),
    "electrolysis-extraction": ("4.4.3.3", "5.4.3.3"),
    "electrolysis-aqueous": ("4.4.3.4", "5.4.3.4"),
    "half-equations": ("4.4.3.5", "5.4.3.5"),
    "exothermic-endothermic": ("4.5.1.1", "5.5.1.1"),
    "reaction-profiles": ("4.5.1.2", "5.5.1.2"),
    "bond-energy-calculations": ("4.5.1.3", "5.5.1.3"),
    "cells-and-batteries": ("4.5.2.1", None),
    "fuel-cells": ("4.5.2.2", None),
    "calculating-rates": ("4.6.1.1", "5.6.1.1"),
    "factors-affecting-rate": ("4.6.1.2", "5.6.1.2"),
    "collision-theory": ("4.6.1.3", "5.6.1.3"),
    "catalysts": ("4.6.1.4", "5.6.1.4"),
    "reversible-reactions-equilibrium": ("4.6.2.1–4.6.2.3", "5.6.2.1–5.6.2.3"),
    "effect-of-conditions-equilibrium": ("4.6.2.4–4.6.2.7", "5.6.2.4–5.6.2.7"),
    "crude-oil-hydrocarbons": ("4.7.1.1", "5.7.1.1"),
    "fractional-distillation": ("4.7.1.2", "5.7.1.2"),
    "properties-of-hydrocarbons": ("4.7.1.3", "5.7.1.3"),
    "cracking-alkenes": ("4.7.1.4", "5.7.1.4"),
    "structure-of-alkenes": ("4.7.2.1", None),
    "reactions-of-alkenes": ("4.7.2.2", None),
    "alcohols": ("4.7.2.3", None),
    "carboxylic-acids": ("4.7.2.4", None),
    "addition-polymerisation": ("4.7.3.1", None),
    "condensation-polymerisation": ("4.7.3.2", None),
    "amino-acids": ("4.7.3.3", None),
    "dna-naturally-occurring-polymers": ("4.7.3.4", None),
    "pure-substances": ("4.8.1.1", "5.8.1.1"),
    "formulations": ("4.8.1.2", "5.8.1.2"),
    "chromatography": ("4.8.1.3", "5.8.1.3"),
    "testing-for-gases": ("4.8.2.1–4.8.2.4", "5.8.2.1–5.8.2.4"),
    "flame-tests": ("4.8.3.1", None),
    "metal-hydroxides": ("4.8.3.2", None),
    "carbonates-halides-sulfates": ("4.8.3.3–4.8.3.5", None),
    "instrumental-methods": ("4.8.3.6–4.8.3.7", None),
    "composition-of-atmosphere": ("4.9.1.1", "5.9.1.1"),
    "early-atmosphere": ("4.9.1.2–4.9.1.4", "5.9.1.2–5.9.1.4"),
    "greenhouse-gases": ("4.9.2.1–4.9.2.4", "5.9.2.1–5.9.2.4"),
    "atmospheric-pollutants": ("4.9.3.1–4.9.3.2", "5.9.3.1–5.9.3.2"),
    "earths-resources": ("4.10.1.1", "5.10.1.1"),
    "potable-water": ("4.10.1.2–4.10.1.3", "5.10.1.2–5.10.1.3"),
    "alternative-metal-extraction": ("4.10.1.4", "5.10.1.4"),
    "life-cycle-assessment": ("4.10.2.1", "5.10.2.1"),
    "reducing-use-of-resources": ("4.10.2.2", "5.10.2.2"),
    "corrosion-prevention": ("4.10.3.1", None),
    "alloys-useful-materials": ("4.10.3.2", None),
    "ceramics-polymers-composites": ("4.10.3.3", None),
    "haber-process": ("4.10.4.1", None),
    "npk-fertilisers": ("4.10.4.2", None),
    # physics — 8463 / 8464
    "energy-stores-systems": ("4.1.1.1", "6.1.1.1"),
    "changes-in-energy": ("4.1.1.2", "6.1.1.2"),
    "energy-changes-in-systems": ("4.1.1.3", "6.1.1.3"),
    "power": ("4.1.1.4", "6.1.1.4"),
    "energy-transfers-in-a-system": ("4.1.2.1", "6.1.2.1"),
    "thermal-conductivity": ("4.1.2.1", "6.1.2.1?"),
    "efficiency": ("4.1.2.2", "6.1.2.2"),
    "energy-resources": ("4.1.3", "6.1.3"),
    "circuit-symbols": ("4.2.1.1", "6.2.1.1"),
    "electrical-charge-current": ("4.2.1.2", "6.2.1.2"),
    "current-resistance-pd": ("4.2.1.3", "6.2.1.3"),
    "resistors": ("4.2.1.4", "6.2.1.4"),
    "series-parallel-circuits": ("4.2.2", "6.2.2"),
    "direct-alternating-pd": ("4.2.3.1", "6.2.3.1"),
    "mains-electricity": ("4.2.3.2", "6.2.3.2"),
    "power-electricity": ("4.2.4.1", "6.2.4.1"),
    "energy-transfers-appliances": ("4.2.4.2", "6.2.4.2"),
    "national-grid": ("4.2.4.3", "6.2.4.3"),
    "static-charge": ("4.2.5.1", None),
    "electric-fields": ("4.2.5.2", None),
    "density-of-materials": ("4.3.1.1", "6.3.1.1"),
    "changes-of-state": ("4.3.1.2", "6.3.1.2"),
    "internal-energy": ("4.3.2.1", "6.3.2.1"),
    "temperature-changes-shc": ("4.3.2.2", "6.3.2.2"),
    "specific-latent-heat": ("4.3.2.3", "6.3.2.3"),
    "particle-motion-pressure": ("4.3.3.1–4.3.3.3", "6.3.3.1"),
    "structure-of-atom": ("4.4.1.1", "6.4.1.1"),
    "mass-number-isotopes": ("4.4.1.2", "6.4.1.2"),
    "development-atomic-model": ("4.4.1.3", "6.4.1.3"),
    "radioactive-decay": ("4.4.2.1", "6.4.2.1"),
    "nuclear-equations": ("4.4.2.2", "6.4.2.2"),
    "half-lives": ("4.4.2.3", "6.4.2.3"),
    "radioactive-contamination": ("4.4.2.4", "6.4.2.4"),
    "background-radiation": ("4.4.3.1", None),
    "uses-of-nuclear-radiation": ("4.4.3.2–4.4.3.3", None),
    "nuclear-fission": ("4.4.4.1", None),
    "nuclear-fusion": ("4.4.4.2", None),
    "scalar-vector-quantities": ("4.5.1.1", "6.5.1.1"),
    "contact-noncontact-forces": ("4.5.1.2", "6.5.1.2"),
    "gravity": ("4.5.1.3", "6.5.1.3"),
    "resultant-forces": ("4.5.1.4", "6.5.1.4"),
    "resolving-forces": ("4.5.1.4", "6.5.1.4?"),
    "free-body-diagrams": ("4.5.1.4", "6.5.1.4?"),
    "work-done-energy-transfer": ("4.5.2", "6.5.2"),
    "forces-elasticity": ("4.5.3", "6.5.3"),
    "moments-levers-gears": ("4.5.4", None),
    "pressure-in-a-fluid": ("4.5.5.1.1, 4.5.5.2", None),
    "upthrust-floating": ("4.5.5.1.2", None),
    "distance-speed-velocity": ("4.5.6.1.1–4.5.6.1.3", "6.5.4.1.1–6.5.4.1.3"),
    "motion-in-a-circle": ("4.5.6.1.3", "6.5.4.1.3?"),
    "distance-time-graphs": ("4.5.6.1.4", "6.5.4.1.4"),
    "acceleration": ("4.5.6.1.5", "6.5.4.1.5"),
    "newtons-laws": ("4.5.6.2.1–4.5.6.2.3", "6.5.4.2.1–6.5.4.2.3"),
    "stopping-distance-braking": ("4.5.6.3.1–4.5.6.3.4", "6.5.4.3.1–6.5.4.3.4"),
    "momentum": ("4.5.7.1–4.5.7.3", "6.5.5.1–6.5.5.2"),
    "transverse-longitudinal-waves": ("4.6.1.1", "6.6.1.1"),
    "properties-of-waves": ("4.6.1.2", "6.6.1.2"),
    "sound-waves-hearing": ("4.6.1.4", None),
    "waves-detection-exploration": ("4.6.1.5", None),
    "types-of-em-waves": ("4.6.2.1", "6.6.2.1"),
    "properties-em-waves-1": ("4.6.2.2", "6.6.2.2"),
    "wave-front-refraction": ("4.6.2.2", "6.6.2.2?"),
    "properties-em-waves-2": ("4.6.2.3", "6.6.2.3"),
    "uses-em-waves": ("4.6.2.4", "6.6.2.4"),
    "lenses": ("4.6.2.5", None),
    "infrared-black-bodies": ("4.6.3.1–4.6.3.2?", None),
    "radiation-balance-temperature": ("4.6.3.2", None),
    "poles-of-a-magnet": ("4.7.1.1", "6.7.1.1"),
    "magnetic-fields": ("4.7.1.2", "6.7.1.2"),
    "electromagnetism": ("4.7.2.1", "6.7.2.1"),
    "flemings-left-hand-rule": ("4.7.2.2", "6.7.2.2"),
    "electric-motors": ("4.7.2.3", "6.7.2.3"),
    "loudspeakers-headphones": ("4.7.2.4", None),
    "induced-potential": ("4.7.3.1", None),
    "uses-generator-effect": ("4.7.3.2", None),
    "microphones": ("4.7.3.3", None),
    "transformers": ("4.7.3.4", None),
    "solar-system-gravity": ("4.8.1.1", None),
    "stellar-evolution": ("4.8.1.2", None),
    "gravity-stable-orbits": ("4.8.1.3", None),
    "red-shift-big-bang": ("4.8.2", None),
    "dark-matter-dark-energy": ("4.8.2?", None),
}

# Site pages flagged triple_only whose content AQA 8464 also teaches (as this
# plan reads the spec). Routes still follow the site; Mide rules on science.
TRILOGY_ALSO = {"meiosis", "classification-living-organisms",
                "resolving-forces", "free-body-diagrams", "motion-in-a-circle",
                "wave-front-refraction", "thermal-conductivity"}

# ── provisional families ────────────────────────────────────────────────
# Definitions: Design Pack - Pilot/01-architecture/00-KS4-Lessons-Rebuild-
# Architecture.md, "The architecture families". REQUIRED PRACTICAL is used
# only where the practical is the page's centre; elsewhere an RP is carried
# by the concept family and shows in the RP column.
FAMILY = {
    # biology
    "eukaryotes-prokaryotes": ("CONTRAST", "nucleus or not; orders of magnitude"),
    "animal-plant-cells": ("CLASSIFY", "organelle → function → which cell"),
    "cell-specialisation": ("MODEL", "structure-fits-function explains every specialised cell"),
    "microscopy": ("QUANTITATIVE", "magnification carries it (architecture's own example)"),
    "culturing-microorganisms": ("REQUIRED PRACTICAL", "antiseptic/antibiotic zones RP is the page"),
    "chromosomes-mitosis": ("PROCESS", "cell cycle in stages (architecture's example)"),
    "stem-cells": ("CONTRAST", "embryonic vs adult vs meristem"),
    "transport-in-cells": ("CLASSIFY", "diffusion / osmosis / active transport — which and why"),
    "principles-of-organisation": ("CLASSIFY", "cell → tissue → organ → system levels"),
    "digestive-system": ("SYSTEM", "organs and enzymes in sequence; break one"),
    "enzymes": ("MODEL", "lock-and-key explains specificity and denaturing"),
    "heart-blood-vessels": ("SYSTEM", "double circulation (architecture's example)"),
    "blood": ("CLASSIFY", "component → job"),
    "coronary-heart-disease": ("PROCESS", "plaque → blocked flow → treatment options"),
    "health-disease": ("INVESTIGATION", "risk factors: correlation vs cause in data"),
    "cancer": ("CONTRAST", "benign vs malignant"),
    "plant-tissues": ("SYSTEM", "leaf tissues working as one organ"),
    "transpiration": ("INVESTIGATION", "potometer: variables and rate data"),
    "translocation": ("CONTRAST", "xylem vs phloem"),
    "communicable-diseases-defence": ("SYSTEM", "lines of defence; breach one"),
    "viral-diseases": ("CLASSIFY", "disease → pathogen → spread → control"),
    "bacterial-diseases": ("CONTRAST", "bacteria vs viruses: toxins, antibiotics"),
    "fungal-protist-diseases": ("CLASSIFY", "pathogen type from symptoms/vector"),
    "vaccination": ("PROCESS", "primary → secondary response"),
    "antibiotics-painkillers": ("CONTRAST", "kills bacteria vs treats symptoms"),
    "drug-discovery-development": ("PROCESS", "trial stages in order"),
    "monoclonal-antibodies": ("PROCESS", "hybridoma production steps"),
    "plant-disease-detection-defence": ("CLASSIFY", "symptom → cause; defence type"),
    "photosynthesis": ("PROCESS", "inputs → chloroplast → glucose"),
    "rate-of-photosynthesis": ("REQUIRED PRACTICAL", "light-intensity RP; limiting factors"),
    "uses-of-glucose": ("CLASSIFY", "fate of glucose → use"),
    "aerobic-respiration": ("PROCESS", "reaction and where it runs"),
    "anaerobic-respiration": ("CONTRAST", "aerobic vs anaerobic (architecture's example)"),
    "response-to-exercise": ("SYSTEM", "heart, lungs, oxygen debt respond together"),
    "metabolism": ("CLASSIFY", "reaction → build-up or breakdown"),
    "homeostasis": ("SYSTEM", "receptor → coordinator → effector"),
    "nervous-system": ("SYSTEM", "CNS and neurones; cut one link"),
    "reflex-actions": ("PROCESS", "reflex arc step by step"),
    "reaction-time": ("REQUIRED PRACTICAL", "ruler-drop RP and its data"),
    "the-brain": ("CLASSIFY", "region → function"),
    "the-eye": ("SYSTEM", "the eye (architecture's example)"),
    "defects-of-the-eye": ("CONTRAST", "short- vs long-sight and their lenses"),
    "thermoregulation": ("SYSTEM", "too hot / too cold feedback"),
    "endocrine-system": ("CONTRAST", "hormonal vs nervous"),
    "blood-glucose-diabetes": ("SYSTEM", "insulin/glucagon feedback; type 1 vs 2"),
    "human-reproduction-hormones": ("PROCESS", "menstrual cycle hormone sequence"),
    "contraception-fertility": ("CLASSIFY", "method → hormonal or barrier, how it works"),
    "sexual-asexual-reproduction": ("CONTRAST", "gametes vs no gametes"),
    "meiosis": ("PROCESS", "two divisions to four haploid cells"),
    "advantages-sexual-asexual": ("CONTRAST", "variation vs speed"),
    "dna-genome": ("MODEL", "gene → protein → characteristic"),
    "dna-structure": ("PROCESS", "protein synthesis (architecture's example)"),
    "genetic-inheritance": ("QUANTITATIVE", "Punnett squares and ratios"),
    "inherited-disorders": ("CONTRAST", "dominant vs recessive disorder; screening"),
    "sex-determination": ("QUANTITATIVE", "XX/XY cross and probability"),
    "variation": ("CLASSIFY", "genetic vs environmental"),
    "evolution-natural-selection": ("PROCESS", "variation → selection → change"),
    "selective-breeding": ("PROCESS", "breeding steps over generations"),
    "genetic-engineering": ("PROCESS", "cut, insert, vector"),
    "cloning": ("CLASSIFY", "cloning technique → plant or animal"),
    "theory-of-evolution": ("CONTRAST", "Darwin vs Lamarck; speciation"),
    "understanding-genetics": ("INVESTIGATION", "Mendel's evidence and its reception"),
    "evidence-for-evolution": ("INVESTIGATION", "weighing the evidence"),
    "fossils-extinction": ("PROCESS", "how fossils form; causes of extinction"),
    "resistant-bacteria": ("PROCESS", "resistance evolving step by step"),
    "classification-living-organisms": ("CLASSIFY", "Linnaean ranks and domains"),
    "ecosystems": ("SYSTEM", "interdependence; remove one species"),
    "population-competition": ("MODEL", "competition explains population change"),
    "abiotic-biotic-factors": ("CLASSIFY", "factor → abiotic or biotic"),
    "adaptations": ("CLASSIFY", "structural / behavioural / functional"),
    "food-chains-webs": ("SYSTEM", "food web knock-on; predator–prey"),
    "sampling-techniques": ("INVESTIGATION", "sampling (architecture's example); quadrat RP"),
    "carbon-cycle": ("PROCESS", "the carbon cycle (architecture's example)"),
    "water-cycle": ("PROCESS", "evaporation → condensation → precipitation"),
    "decomposition": ("REQUIRED PRACTICAL", "rate-of-decay RP; Rainford gives it 4 lessons"),
    "environmental-change": ("INVESTIGATION", "distribution data under change"),
    "biodiversity": ("SYSTEM", "lose species, predict knock-on"),
    "waste-management": ("CLASSIFY", "pollutant → source → effect"),
    "land-use": ("CONTRAST", "peat: burn/use vs conserve"),
    "deforestation": ("PROCESS", "clearing → CO₂ and biodiversity chain"),
    "global-warming": ("SYSTEM", "warming's effects through ecosystems"),
    "maintaining-biodiversity": ("INVESTIGATION", "evaluate conservation programmes"),
    "trophic-levels": ("CLASSIFY", "organism → trophic level"),
    "pyramids-of-biomass": ("QUANTITATIVE", "construct pyramids from data"),
    "transfer-of-biomass": ("QUANTITATIVE", "efficiency calculation"),
    "factors-affecting-food-security": ("CLASSIFY", "threat → category"),
    "farming-techniques": ("CONTRAST", "intensive vs free-range"),
    "sustainable-fisheries": ("SYSTEM", "quota/net size; overfish one stock"),
    "role-of-biotechnology": ("PROCESS", "mycoprotein / GM production"),
    # chemistry
    "atoms-elements-compounds": ("CLASSIFY", "element / compound / mixture"),
    "mixtures": ("CLASSIFY", "mixture → separation technique"),
    "model-of-the-atom": ("MODEL", "nuclear model and its predecessors"),
    "subatomic-particles": ("MODEL", "p/n/e charges and masses"),
    "relative-atomic-mass": ("QUANTITATIVE", "weighted mean of isotopes"),
    "electronic-structure": ("MODEL", "shell filling explains the table"),
    "periodic-table": ("MODEL", "position from electron structure"),
    "development-periodic-table": ("INVESTIGATION", "Mendeleev's evidence and gaps"),
    "metals-non-metals": ("CONTRAST", "lose vs gain electrons"),
    "group-0": ("MODEL", "full shell explains inertness and trend"),
    "group-1": ("MODEL", "distance of outer electron explains the trend"),
    "group-7": ("CLASSIFY", "will it displace?"),
    "transition-metals": ("CONTRAST", "vs Group 1"),
    "conservation-of-mass": ("QUANTITATIVE", "balancing equations"),
    "relative-formula-mass": ("QUANTITATIVE", "Mr sums"),
    "mass-changes-reactions": ("CONTRAST", "gas escapes vs gas gained"),
    "chemical-measurements": ("INVESTIGATION", "uncertainty and range"),
    "moles": ("QUANTITATIVE", "moles (architecture's example)"),
    "amounts-in-equations": ("QUANTITATIVE", "reacting masses"),
    "using-moles-calculations": ("QUANTITATIVE", "balancing from masses; limiting reactant"),
    "concentration-of-solutions": ("QUANTITATIVE", "g/dm³ (mol/dm³ triple HT)"),
    "percentage-yield": ("QUANTITATIVE", "yield calculation"),
    "atom-economy": ("QUANTITATIVE", "atom economy calculation"),
    "reactivity-series": ("CLASSIFY", "rank metals from observations"),
    "extraction-of-metals": ("CONTRAST", "carbon reduction vs electrolysis"),
    "oxidation-reduction": ("CLASSIFY", "oxidised or reduced?"),
    "reactions-of-acids": ("CLASSIFY", "acid + X → which salt and products"),
    "salts-neutralisation": ("REQUIRED PRACTICAL", "making a soluble salt RP"),
    "ph-scale": ("MODEL", "H⁺ concentration explains pH"),
    "titrations": ("REQUIRED PRACTICAL", "titration RP and its calculation"),
    "strong-weak-acids": ("CONTRAST", "full vs partial ionisation"),
    "electrolysis-principles": ("PROCESS", "electrolysis (architecture's example)"),
    "electrolysis-molten": ("CLASSIFY", "which ion to which electrode"),
    "electrolysis-extraction": ("SYSTEM", "aluminium cell; change cryolite/anode"),
    "electrolysis-aqueous": ("REQUIRED PRACTICAL", "electrolysis of solutions RP"),
    "half-equations": ("PROCESS", "build a half equation step by step"),
    "exothermic-endothermic": ("CONTRAST", "exo vs endo; temperature-change RP"),
    "reaction-profiles": ("MODEL", "profile diagram explains activation energy"),
    "bond-energy-calculations": ("QUANTITATIVE", "bonds broken − made"),
    "cells-and-batteries": ("MODEL", "reactivity difference sets voltage"),
    "fuel-cells": ("CONTRAST", "fuel cell vs battery"),
    "calculating-rates": ("QUANTITATIVE", "rates (architecture's example)"),
    "factors-affecting-rate": ("REQUIRED PRACTICAL", "rate RP (concentration)"),
    "collision-theory": ("MODEL", "collision frequency and energy"),
    "catalysts": ("CONTRAST", "with vs without catalyst"),
    "reversible-reactions-equilibrium": ("MODEL", "dynamic equilibrium"),
    "effect-of-conditions-equilibrium": ("CLASSIFY", "which way does it shift?"),
    "crude-oil-hydrocarbons": ("CLASSIFY", "alkane or not; CₙH₂ₙ₊₂"),
    "fractional-distillation": ("PROCESS", "column steps by boiling point"),
    "properties-of-hydrocarbons": ("MODEL", "chain length explains the properties"),
    "cracking-alkenes": ("PROCESS", "cracking conditions → products"),
    "structure-of-alkenes": ("CONTRAST", "alkane vs alkene"),
    "reactions-of-alkenes": ("CLASSIFY", "reagent → addition product"),
    "alcohols": ("CLASSIFY", "alcohol reactions and uses"),
    "carboxylic-acids": ("CONTRAST", "weak acid vs strong; esters"),
    "addition-polymerisation": ("PROCESS", "monomer → repeat unit"),
    "condensation-polymerisation": ("CONTRAST", "condensation vs addition"),
    "amino-acids": ("PROCESS", "amino acids → polypeptide"),
    "dna-naturally-occurring-polymers": ("CLASSIFY", "polymer → monomer"),
    "pure-substances": ("CONTRAST", "pure vs impure melting point"),
    "formulations": ("CLASSIFY", "formulation or not"),
    "chromatography": ("REQUIRED PRACTICAL", "chromatography RP and Rf"),
    "testing-for-gases": ("CLASSIFY", "test result → gas"),
    "flame-tests": ("CLASSIFY", "colour → ion"),
    "metal-hydroxides": ("CLASSIFY", "precipitate colour → ion"),
    "carbonates-halides-sulfates": ("REQUIRED PRACTICAL", "identify-the-ions RP lands here"),
    "instrumental-methods": ("CONTRAST", "instrumental vs chemical tests"),
    "composition-of-atmosphere": ("CLASSIFY", "gas → proportion"),
    "early-atmosphere": ("PROCESS", "how the atmosphere changed"),
    "greenhouse-gases": ("MODEL", "greenhouse effect mechanism"),
    "atmospheric-pollutants": ("CLASSIFY", "pollutant → source → effect"),
    "earths-resources": ("CLASSIFY", "finite/renewable, natural/synthetic"),
    "potable-water": ("REQUIRED PRACTICAL", "water purification RP"),
    "alternative-metal-extraction": ("CONTRAST", "phytomining vs bioleaching"),
    "life-cycle-assessment": ("INVESTIGATION", "evaluate LCA data"),
    "reducing-use-of-resources": ("CLASSIFY", "reduce/reuse/recycle"),
    "corrosion-prevention": ("CONTRAST", "barrier vs sacrificial"),
    "alloys-useful-materials": ("CLASSIFY", "alloy → use"),
    "ceramics-polymers-composites": ("CONTRAST", "thermosetting vs thermosoftening"),
    "haber-process": ("SYSTEM", "conditions compromise; change one"),
    "npk-fertilisers": ("PROCESS", "producing NPK"),
    # physics
    "energy-stores-systems": ("CLASSIFY", "store vs pathway"),
    "changes-in-energy": ("QUANTITATIVE", "KE, GPE, EPE equations"),
    "energy-changes-in-systems": ("REQUIRED PRACTICAL", "SHC RP sits at this spec point"),
    "power": ("QUANTITATIVE", "power (architecture's example)"),
    "energy-transfers-in-a-system": ("MODEL", "conservation + dissipation"),
    "thermal-conductivity": ("REQUIRED PRACTICAL", "thermal-insulation RP"),
    "efficiency": ("QUANTITATIVE", "efficiency calculation"),
    "energy-resources": ("CONTRAST", "renewable vs non-renewable"),
    "circuit-symbols": ("CLASSIFY", "symbol → component"),
    "electrical-charge-current": ("QUANTITATIVE", "Q = It"),
    "current-resistance-pd": ("QUANTITATIVE", "V = IR; wire-resistance RP"),
    "direct-alternating-pd": ("CONTRAST", "AC vs DC (architecture's example)"),
    "mains-electricity": ("SYSTEM", "three-core cable; break the earth"),
    "power-electricity": ("QUANTITATIVE", "P = VI, P = I²R"),
    "energy-transfers-appliances": ("QUANTITATIVE", "E = Pt, E = QV"),
    "national-grid": ("SYSTEM", "the National Grid (architecture's example)"),
    "static-charge": ("PROCESS", "rubbing → electron transfer → force/spark"),
    "electric-fields": ("MODEL", "field explains force at a distance"),
    "density-of-materials": ("REQUIRED PRACTICAL", "density RP (ρ = m/V)"),
    "changes-of-state": ("MODEL", "particle model (architecture's example)"),
    "internal-energy": ("MODEL", "KE + PE of particles"),
    "temperature-changes-shc": ("QUANTITATIVE", "SHC (architecture's example)"),
    "specific-latent-heat": ("QUANTITATIVE", "E = mL"),
    "particle-motion-pressure": ("MODEL", "collisions explain gas pressure"),
    "structure-of-atom": ("MODEL", "the nuclear model (architecture's example)"),
    "mass-number-isotopes": ("CLASSIFY", "isotope or not"),
    "development-atomic-model": ("INVESTIGATION", "scattering evidence → new model"),
    "radioactive-decay": ("CLASSIFY", "alpha/beta/gamma (architecture's example)"),
    "nuclear-equations": ("QUANTITATIVE", "balance mass and atomic numbers"),
    "half-lives": ("QUANTITATIVE", "half-life from graphs"),
    "radioactive-contamination": ("CONTRAST", "contamination vs irradiation"),
    "background-radiation": ("QUANTITATIVE", "corrected count rate, dose"),
    "uses-of-nuclear-radiation": ("CLASSIFY", "choose isotope by type/half-life"),
    "nuclear-fission": ("PROCESS", "chain reaction"),
    "nuclear-fusion": ("CONTRAST", "fusion vs fission"),
    "scalar-vector-quantities": ("CLASSIFY", "scalar or vector"),
    "contact-noncontact-forces": ("CONTRAST", "contact vs non-contact"),
    "gravity": ("QUANTITATIVE", "W = mg"),
    "resultant-forces": ("MODEL", "balanced/unbalanced explains motion"),
    "resolving-forces": ("QUANTITATIVE", "scale drawings and components"),
    "free-body-diagrams": ("MODEL", "one diagram predicts the motion"),
    "work-done-energy-transfer": ("QUANTITATIVE", "W = Fs"),
    "forces-elasticity": ("QUANTITATIVE", "Hooke's law (architecture's example); spring RP"),
    "moments-levers-gears": ("QUANTITATIVE", "M = Fd"),
    "pressure-in-a-fluid": ("QUANTITATIVE", "p = hρg"),
    "upthrust-floating": ("MODEL", "pressure difference explains upthrust"),
    "distance-speed-velocity": ("CONTRAST", "speed vs velocity"),
    "motion-in-a-circle": ("MODEL", "constant speed, changing velocity"),
    "distance-time-graphs": ("QUANTITATIVE", "gradient = speed"),
    "acceleration": ("QUANTITATIVE", "a = Δv/t, v² − u² = 2as"),
    "newtons-laws": ("MODEL", "three laws explain motion"),
    "stopping-distance-braking": ("SYSTEM", "thinking + braking; change one factor"),
    "momentum": ("QUANTITATIVE", "p = mv, conservation"),
    "transverse-longitudinal-waves": ("CONTRAST", "transverse vs longitudinal"),
    "properties-of-waves": ("REQUIRED PRACTICAL", "ripple-tank RP; v = fλ"),
    "sound-waves-hearing": ("PROCESS", "vibration → ear → hearing range"),
    "waves-detection-exploration": ("INVESTIGATION", "infer hidden structure from wave data"),
    "types-of-em-waves": ("MODEL", "one spectrum ordered by λ and f"),
    "properties-em-waves-1": ("MODEL", "material/λ explain refraction and absorption"),
    "wave-front-refraction": ("MODEL", "wavefront speed change explains bending"),
    "properties-em-waves-2": ("CONTRAST", "ionising vs non-ionising"),
    "uses-em-waves": ("CLASSIFY", "use → wave, and why"),
    "lenses": ("MODEL", "ray model predicts the image"),
    "infrared-black-bodies": ("CONTRAST", "matt black vs shiny; Rainford's IR RP"),
    "radiation-balance-temperature": ("SYSTEM", "Earth's energy balance; change one input"),
    "poles-of-a-magnet": ("CONTRAST", "permanent vs induced"),
    "magnetic-fields": ("MODEL", "magnetic fields (architecture's example)"),
    "electromagnetism": ("SYSTEM", "solenoid: change current/turns/core"),
    "flemings-left-hand-rule": ("QUANTITATIVE", "F = BIl"),
    "electric-motors": ("SYSTEM", "coil, field, commutator together"),
    "loudspeakers-headphones": ("PROCESS", "signal → force → vibration"),
    "induced-potential": ("MODEL", "changing field induces pd"),
    "uses-generator-effect": ("CONTRAST", "alternator vs dynamo"),
    "microphones": ("PROCESS", "sound → coil → signal"),
    "transformers": ("QUANTITATIVE", "turns ratio"),
    "solar-system-gravity": ("CLASSIFY", "body → type; formation"),
    "stellar-evolution": ("PROCESS", "stellar life cycle (architecture's example)"),
    "gravity-stable-orbits": ("MODEL", "gravity explains orbital speed"),
    "red-shift-big-bang": ("INVESTIGATION", "evidence for the Big Bang"),
    "dark-matter-dark-energy": ("CONTRAST", "dark matter vs dark energy"),
}


# ── loaders ─────────────────────────────────────────────────────────────

def load_subtopics():
    """slug → record, from the site data. Audience from ks4_data.classify()."""
    import ks4_data
    cls = ks4_data.classify()
    content = {}
    for subj in SUBJECTS:
        for suffix in ("", "_higher", "_triple_foundation", "_triple_higher"):
            mod = importlib.import_module("all_subtopics_%s%s" % (subj, suffix))
            pages = getattr(mod, "%s_SUBTOPICS_ALL" % subj.upper())
            for topic, sts in pages.items():
                for st in sts:
                    c = content.setdefault(st["id"], dict(
                        title=st["title"], rp=False, fifas=0, eqs=0,
                        topics=set()))
                    c["topics"].add(topic)
                    c["rp"] = c["rp"] or bool(st.get("rp"))
                    c["fifas"] = max(c["fifas"], len(st.get("fifas") or []))
                    c["eqs"] = max(c["eqs"], len(st.get("equations") or []))
    out = {}
    for slug, a in cls.items():
        routes = {(False, "foundation"): ROUTES,
                  (False, "higher"): ("CH", "TH"),
                  (True, "foundation"): ("TF", "TH"),
                  (True, "higher"): ("TH",)}[(a["triple_only"], a["tier"])]
        rec = dict(slug=slug, subject=a["subject"], topic=a["topic"],
                   site_order=a["order"], tier=a["tier"],
                   triple_only=a["triple_only"], routes=routes)
        rec.update(content[slug])
        out[slug] = rec
    return out


ROW_HDR = re.compile(r"^-- ── Year (\d+) · (\w+) · (\w+) — (\d+) lessons")
ROW = re.compile(r"^\s*\((\d+)(?:::smallint)?, '(?:[^']|'')*'(?:::text)?, "
                 r"(?:null|'([a-z0-9-]+)'(?:::text)?), ")


def load_rainford():
    """[(year, Subject, tier, academic_week, slug-or-None)], plus block sizes."""
    rows, sizes, cur = [], {}, None
    with open(SEED, encoding="utf-8") as f:
        for line in f:
            m = ROW_HDR.match(line)
            if m:
                cur = (int(m[1]), m[2], m[3])
                sizes[cur] = int(m[4])
                continue
            m = ROW.match(line)
            if m and cur:
                rows.append((*cur, int(m[1]), m[2]))
    return rows, sizes


# ── ordering ────────────────────────────────────────────────────────────

def spec_key(rec):
    sep = SPEC[rec["slug"]][0].rstrip("?")
    first = re.split(r"[–,]", sep)[0].strip()
    return (SUBJECTS.index(rec["subject"]),
            tuple(int(x) for x in first.split(".")), rec["site_order"])


def fmt_weeks(rows_for_slug):
    """'Y10 Ch w5–8 (H,F); Y11 Ch w9 (H)' — whole year, compressed."""
    by = {}
    for y, s, t, w, _ in rows_for_slug:
        by.setdefault((y, s, w), set()).add(t[0].upper())
    grp = {}
    for (y, s, w), tiers in by.items():
        grp.setdefault((y, s, "".join(sorted(tiers, key="HF".index))), []).append(w)
    parts = []
    for (y, s, tiers), ws in sorted(grp.items(),
                                    key=lambda kv: (min(kv[1]), kv[0])):
        ws = sorted(set(ws))
        runs, start = [], ws[0]
        for a, b in zip(ws, ws[1:] + [None]):
            if b != a + 1:
                runs.append(str(start) if start == a else "%d–%d" % (start, a))
                start = b
        parts.append("Y%d %s w%s (%s)" % (y, SUBJ_ABBR[s], ",".join(runs),
                                          ",".join(tiers)))
    return "; ".join(parts)


def batches(items, key):
    """Partition `items` into consecutive runs of BATCH_MIN..BATCH_MAX,
    minimising the number of cuts that fall INSIDE a group (same key either
    side). Ties → the larger earlier batch (soonest work pulled forward)."""
    n = len(items)
    best = {n: (0, ())}
    for i in range(n - 1, -1, -1):
        cand = None
        for size in range(BATCH_MAX, BATCH_MIN - 1, -1):
            j = i + size
            if j > n or j not in best:
                continue
            cut = 1 if j < n and key(items[j - 1]) == key(items[j]) else 0
            score = (best[j][0] + cut, (size,) + best[j][1])
            if cand is None or score[0] < cand[0] or (
                    score[0] == cand[0] and
                    tuple(-x for x in score[1]) < tuple(-x for x in cand[1])):
                cand = score
        if cand is not None:
            best[i] = cand
    if 0 not in best:
        raise SystemExit("cannot partition %d items into %d–%d" %
                         (n, BATCH_MIN, BATCH_MAX))
    out, i = [], 0
    for size in best[0][1]:
        out.append(items[i:i + size])
        i += size
    return out


# ── build ───────────────────────────────────────────────────────────────

def build():
    from ks4_lessons import LESSONS
    subs = load_subtopics()
    rows, sizes = load_rainford()

    pilot = [l["slug"] for l in LESSONS]
    missing = (sorted(set(subs) - set(SPEC)) +
               sorted(set(subs) - set(FAMILY) - set(pilot)))
    extra = sorted((set(SPEC) | set(FAMILY)) - set(subs))
    if missing or extra:
        raise SystemExit("SPEC/FAMILY out of step with the data: missing %s, "
                         "extra %s" % (missing, extra))

    by_slug = {}
    for r in rows:
        if r[4]:
            by_slug.setdefault(r[4], []).append(r)
    for slug, rs in by_slug.items():
        rec = subs.get(slug)
        if rec is None:
            continue
        rec["rainford"] = fmt_weeks(rs)
        upcoming = [w for _, _, _, w, _ in rs if NOW_WEEK <= w <= XMAS_LAST_WEEK]
        rec["next_week"] = min(upcoming) if upcoming else None

    todo = [r for s, r in subs.items() if s not in set(pilot)]
    soon = sorted((r for r in todo if r.get("next_week")),
                  key=lambda r: (r["next_week"], spec_key(r)))
    rest = sorted((r for r in todo if not r.get("next_week")), key=spec_key)
    ordered = soon + rest

    def group(r):
        if r.get("next_week"):
            return ("week", r["next_week"])
        return ("topic", r["subject"], r["topic"])

    plan = batches(ordered, group)

    oddities = find_oddities(subs, rows, sizes)
    return subs, pilot, plan, rows, sizes, oddities


def find_oddities(subs, rows, sizes):
    odd = []
    unknown = sorted({r[4] for r in rows if r[4] and r[4] not in subs})
    odd.append("Seed slugs not in the site data: %s." %
               (", ".join(unknown) if unknown else "none"))
    multi = sorted(s for s, r in subs.items() if len(r["topics"]) > 1)
    odd.append("Subtopics filed under two topics: %s." %
               (", ".join(multi) if multi else "none (classify() asserts it)"))
    never = sorted(s for s in subs if not subs[s].get("rainford"))
    odd.append("Subtopics Rainford never references: %d (ordered by spec "
               "only)." % len(never))
    found_ht = sorted({(r[4], r[0], r[1]) for r in rows
                       if r[4] and r[2] == "foundation"
                       and subs[r[4]]["tier"] == "higher"})
    if found_ht:
        odd.append("Rainford Foundation rows on a page the site ships Higher-"
                   "only (no CF/TF route exists): " + "; ".join(
                       "%s (Y%d %s)" % x for x in found_ht) + ".")
    over = sorted("Y%d %s %s %d" % (k[0], SUBJ_ABBR[k[1]], k[2][0].upper(), v)
                  for k, v in sizes.items() if v > 39)
    if over:
        odd.append("Blocks longer than the 39-week ceiling of "
                   "currentTeachingWeek(), so academic_week is a lesson index, "
                   "not a calendar week (several lessons a week in practice): "
                   + ", ".join(over) + ". Read literally, as this plan does, "
                   "later lessons look later than they are; relative order "
                   "within a block is unaffected.")
    odd.append("Week %d is the half-term holiday, but the platform's week "
               "count does not skip holidays, so academic_week %d rows are "
               "still 'taught' that week. They are kept in the window."
               % (HALF_TERM_WEEK, HALF_TERM_WEEK))
    odd.append("Nothing in the backend reads scheme_of_work_overrides "
               "(schemeLessons() reads scheme_of_work_entries only), and the "
               "Rainford rows are on TEST only. The sequence is used here as "
               "ordering evidence, as briefed.")
    tri = sorted(TRILOGY_ALSO)
    odd.append("Site flags these triple_only, but AQA 8464 also teaches the "
               "content (as this plan reads the spec; Mide's call, routes "
               "follow the site): " + ", ".join(tri) + ". meiosis and "
               "classification-living-organisms were already flagged in "
               "docs/ks4/rainford-sow-mapping.md §3.")
    odd.append("The data's `spec` field mixes 8464 and 846x numbering and is "
               "wrong in places (static-charge '6.2.5', electric-fields "
               "'6.2.6', motion-in-a-circle '6.5.6', theory-of-evolution "
               "'4.6.3.3', culturing-microorganisms '4.1.2'); the refs here "
               "are authored in tools/ks4_batch_plan.py SPEC.")
    odd.append("The data's `rp` field names some non-AQA practicals as RPs "
               "(circuit-symbols, electrical-charge-current, "
               "transverse-longitudinal-waves 'slinky', magnetic-fields "
               "'plotting compass'); the RP column reports the data as-is.")
    return odd


# ── render ──────────────────────────────────────────────────────────────

def spec_cell(rec):
    sep, comb = SPEC[rec["slug"]]
    board = {"biology": "8461", "chemistry": "8462", "physics": "8463"}[
        rec["subject"]]
    if rec["triple_only"]:
        lead = comb if (comb and rec["slug"] in TRILOGY_ALSO) else "—"
        return "%s · %s %s" % (lead, board, sep)
    return comb


def lesson_row(n, rec, family=None):
    fam, why = family or FAMILY[rec["slug"]]
    return "| %d | `%s` | %s | %s | %s | %s | %s | %s — %s | %s | %s | %s | %s |" % (
        n, rec["slug"], rec["title"], rec["subject"][:4].title(),
        rec["topic"], spec_cell(rec), " ".join(rec["routes"]), fam, why,
        "Y" if rec["rp"] else "", rec["fifas"] or "", rec["eqs"] or "",
        rec.get("rainford", "—"))


TABLE_HEAD = ("| # | slug | title | subj | topic_id | 8464 · separate | routes "
              "| family — why | RP | FIFA | eq | Rainford (whole year) |\n"
              "|---|---|---|---|---|---|---|---|---|---|---|---|")


def render(subs, pilot, plan, oddities):
    L = []
    A = L.append
    A("# KS4 lesson batches")
    A("")
    A("Generated by `python3 tools/ks4_batch_plan.py --write`. Do not edit by "
      "hand — change the script.")
    A("")
    A("## Basis")
    A("")
    A("| | |")
    A("|---|---|")
    A("| Today | %s — **teaching week %d** |" % (TODAY.strftime("%a %d %b %Y"),
                                                   NOW_WEEK))
    A("| Week numbering | backend `currentTeachingWeek()`: week 1 starts "
      "Sun %s (the Sunday on or before the year's start_date, %s); the number "
      "rolls Sunday 00:00 UK; holidays are not skipped |" % (
          week0().strftime("%d %b"), YEAR_START.strftime("%d %b %Y")))
    A("| This half-term | weeks %d–%d (to Fri %s) |" % (
        NOW_WEEK, HALF_TERM_WEEK - 1,
        (week_monday(HALF_TERM_WEEK - 1) + dt.timedelta(days=4)).strftime("%d %b")))
    A("| Half-term holiday | week %d (w/c Mon %s) — **assumed**, no school "
      "calendar in either repo or `Rainford SOW/` |" % (
          HALF_TERM_WEEK, HALF_TERM_HOLIDAY.strftime("%d %b")))
    A("| Next half-term | weeks %d–%d (to Fri %s, **assumed**) |" % (
        HALF_TERM_WEEK + 1, XMAS_LAST_WEEK,
        LAST_DAY_BEFORE_CHRISTMAS.strftime("%d %b")))
    A("| Rainford week | a seed row's `academic_week` = the week it is taught "
      "(one lesson per week per block, read literally) |")
    A("| Window | academic_week %d–%d, all of Y9/Y10/Y11, both tiers |" % (
        NOW_WEEK, XMAS_LAST_WEEK))
    A("| Order | soonest window week across all blocks, then AQA spec order "
      "(separate-science numbering, Bi → Ch → Ph); everything not taught in "
      "the window, in spec order |")
    A("| Batches | %d–%d lessons; cuts placed to avoid splitting a week (before "
      "Christmas) or a topic (after); ties → larger earlier batch |" % (
          BATCH_MIN, BATCH_MAX))
    A("| Routes | from `ks4_data.classify()`: base → CF CH TF TH; Higher-only "
      "→ CH TH; Triple → TF TH; Triple Higher-only → TH. The per-subtopic "
      "`higher` field is inline higher content, never a whole-page flag |")
    A("| RP / FIFA / eq | from the site data (any module), as-is |")
    A("")

    A("## Summary")
    A("")
    A("| batch | lessons | Bi | Ch | Ph | soonest Rainford week | topics |")
    A("|---|---|---|---|---|---|---|")
    pil = [subs[s] for s in pilot]
    allb = [pil] + plan

    def summary(i, b):
        cnt = {s: sum(1 for r in b if r["subject"] == s) for s in SUBJECTS}
        wk = [r.get("next_week") for r in b if r.get("next_week")]
        topics = []
        for r in b:
            t = "%s/%s" % (r["subject"][:2].title(), r["topic"])
            if t not in topics:
                topics.append(t)
        A("| %s | %d | %s | %s | %s | %s | %s |" % (
            "1 (pilot, live)" if i == 1 else str(i), len(b),
            cnt["biology"] or "", cnt["chemistry"] or "", cnt["physics"] or "",
            ("w%d" % min(wk)) if wk else "—", ", ".join(topics)))

    for i, b in enumerate(allb, 1):
        summary(i, b)
    A("| **total** | **%d** | | | | | |" % sum(len(b) for b in allb))
    A("")

    A("## Batch 1 — pilot (live)")
    A("")
    A(TABLE_HEAD)
    from ks4_lessons import LESSONS
    fam = {l["slug"]: (l["family"].upper(), "pilot") for l in LESSONS}
    for n, s in enumerate(pilot, 1):
        A(lesson_row(n, subs[s], fam[s]))
    A("")
    for i, b in enumerate(plan, 2):
        A("## Batch %d" % i)
        A("")
        A(TABLE_HEAD)
        for n, r in enumerate(b, 1):
            A(lesson_row(n, r))
        A("")

    A("## Odd things")
    A("")
    for o in oddities:
        A("- " + o)
    A("")
    return "\n".join(L)


def main(argv):
    subs, pilot, plan, _rows, _sizes, odd = build()
    text = render(subs, pilot, plan, odd)
    if "--write" in argv:
        with open(OUT, "w", encoding="utf-8") as f:
            f.write(text)
        print("wrote %s (%d batches after the pilot)" % (
            os.path.relpath(OUT, REPO), len(plan)))
    elif "--check" in argv:
        try:
            with open(OUT, encoding="utf-8") as f:
                same = f.read() == text
        except FileNotFoundError:
            same = False
        print("BATCH-PLAN.md is %s" % ("current" if same else "STALE"))
        return 0 if same else 1
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
