"""ks4_lessons.batch_2 — Batch 2 (docs/ks4/BATCH-PLAN.md), the first lessons
Code authored after Mide's ruling of 1 Oct 2026. Sources:
ks4_lessons/authored/batch-2/<slug>.dc.html. Per-lesson notes and the source
examination: docs/ks4/packs/batch-2/. `withhold` entries name frozen quiz items
the batch examination found wrong (or wrong for a route), so the page does not
serve them — each needs a DEPARTURES row (docs/ks4/packs/batch-2/DEPARTURES.md).
The ten B2-W1…B2-W10 entries were removed on feat/ks4-frozen-corrections: Mide
approved correcting those items in all_subtopics_*.py itself (2 Oct 2026,
docs/ks4/FROZEN-CORRECTIONS.md), so they are served again."""

B = "batch-2"
ALL = ["CF", "CH", "TF", "TH"]
TRIPLE = ["TF", "TH"]


def W(needle, dep, routes=None):
    return {"needle": needle, "dep": dep, "routes": routes}


LESSONS = [
    dict(slug="chromosomes-mitosis", source_file="chromosomes-mitosis.dc.html",
         subject="biology", topic_id="cell-biology",
         title="Chromosomes, the cell cycle and mitosis", spec="4.1.2.1–4.1.2.2",
         family="Process", routes=ALL, review_state="examiner-reviewed", batch=B,
         block_map={"s-cycle": "worked-example"}),
    dict(slug="enzymes", source_file="enzymes.dc.html",
         subject="biology", topic_id="organisation", title="Enzymes",
         spec="4.2.2.1", family="Required practical", routes=ALL,
         review_state="examiner-reviewed", batch=B),
    dict(slug="carbon-cycle", source_file="carbon-cycle.dc.html",
         subject="biology", topic_id="ecology", title="The carbon cycle",
         spec="4.7.2.2", family="Process", routes=ALL, review_state="examiner-reviewed",
         batch=B, block_map={"s-trace": "worked-example", "s-label": "check"}),
    dict(slug="atoms-elements-compounds", source_file="atoms-elements-compounds.dc.html",
         subject="chemistry", topic_id="atomic-structure",
         title="Atoms, elements and compounds", spec="5.1.1.1",
         family="Classify", routes=ALL, review_state="examiner-reviewed", batch=B,
         block_map={"s-balance": "worked-example"}),
    dict(slug="using-moles-calculations", source_file="using-moles-calculations.dc.html",
         subject="chemistry", topic_id="quantitative",
         title="Using moles — calculations and limiting reactants",
         spec="5.3.2.3–5.3.2.4", family="Quantitative", routes=["CH", "TH"],
         review_state="examiner-reviewed", batch=B,
         block_map={"s-bench": "figure", "s-solution": "check"}),
    dict(slug="concentration-of-solutions", source_file="concentration-of-solutions.dc.html",
         subject="chemistry", topic_id="quantitative",
         title="Concentration of solutions", spec="5.3.2.5",
         family="Quantitative", routes=ALL, review_state="examiner-reviewed", batch=B,
         block_map={"s-bench": "figure", "s-mol": "check"}),
    dict(slug="metal-hydroxides", source_file="metal-hydroxides.dc.html",
         subject="chemistry", topic_id="analysis", title="Metal hydroxides",
         spec="8462 4.8.3.2", family="Classify", routes=TRIPLE,
         review_state="examiner-reviewed", batch=B,
         block_map={"s-bench": "practical", "s-forge": "worked-example", "s-ionic": "check"}),
    dict(slug="changes-in-energy", source_file="changes-in-energy.dc.html",
         subject="physics", topic_id="energy", title="Changes in energy",
         spec="6.1.1.2", family="Quantitative", routes=ALL,
         review_state="examiner-reviewed", batch=B),
    dict(slug="internal-energy", source_file="internal-energy.dc.html",
         subject="physics", topic_id="particle-model", title="Internal energy",
         spec="6.3.2.1", family="Model", routes=ALL, review_state="examiner-reviewed", batch=B),
    dict(slug="lenses", source_file="lenses.dc.html",
         subject="physics", topic_id="waves", title="Lenses",
         spec="8463 4.6.2.5", family="Model", routes=TRIPLE,
         review_state="examiner-reviewed", batch=B,
         block_map={"s-bench": "practical", "s-build": "worked-example", "s-eye": "check"}),
    dict(slug="eukaryotes-prokaryotes", source_file="eukaryotes-prokaryotes.dc.html",
         subject="biology", topic_id="cell-biology",
         title="Eukaryotes and prokaryotes", spec="4.1.1.1",
         family="Contrast", routes=ALL, review_state="examiner-reviewed", batch=B,
         block_map={"s-build": "comparison", "s-scale": "check"}),
    dict(slug="decomposition", source_file="decomposition.dc.html",
         subject="biology", topic_id="ecology", title="Decomposition",
         spec="4.7.2.2 (+ 8461 4.7.2.3, RP10)", family="Required practical",
         routes=ALL, review_state="examiner-reviewed", batch=B,
         block_map={"s-sim": "required-practical", "s-return": "check"}),
    dict(slug="relative-formula-mass", source_file="relative-formula-mass.dc.html",
         subject="chemistry", topic_id="quantitative",
         title="Relative formula mass", spec="5.3.1.2", family="Quantitative",
         routes=ALL, review_state="examiner-reviewed", batch=B,
         block_map={"s-pans": "check"}),
    dict(slug="percentage-yield", source_file="percentage-yield.dc.html",
         subject="chemistry", topic_id="quantitative", title="Percentage yield",
         spec="8462 4.3.3.1", family="Quantitative", routes=TRIPLE,
         review_state="examiner-reviewed", batch=B,
         block_map={"s-which": "check", "s-bench": "practical",
                    "s-reasons": "check", "s-theory": "worked-example"}),
    dict(slug="titrations", source_file="titrations.dc.html",
         subject="chemistry", topic_id="chemical-changes", title="Titrations",
         spec="8462 4.4.2.5", family="Required practical", routes=TRIPLE,
         review_state="examiner-reviewed", batch=B,
         block_map={"s-indicator": "check", "s-bench": "required-practical",
                    "s-rp": "required-practical", "s-conc": "worked-example",
                    "s-errors": "check"}),
    dict(slug="carbonates-halides-sulfates", source_file="carbonates-halides-sulfates.dc.html",
         subject="chemistry", topic_id="analysis",
         title="Tests for carbonates, halides and sulfates",
         spec="8462 4.8.3.3–4.8.3.5", family="Required practical", routes=TRIPLE,
         review_state="examiner-reviewed", batch=B,
         block_map={"s-rack": "practical", "s-ionic": "check"}),
]
