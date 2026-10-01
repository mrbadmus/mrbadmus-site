"""ks4_lessons.batch_3 — Batch 3 (docs/ks4/BATCH-PLAN.md). Sources:
ks4_lessons/authored/batch-3/<slug>.dc.html; notes and source examination in
docs/ks4/packs/batch-3/. `withhold` = frozen quiz items the batch examination
found wrong (or wrong for a route); verbatim in all_subtopics_*.py, not served,
each with a DEPARTURES row (docs/ks4/packs/batch-3/DEPARTURES.md)."""

B = "batch-3"
ALL = ["CF", "CH", "TF", "TH"]
TRIPLE = ["TF", "TH"]
RS = "draft"


def W(needle, dep, routes=None):
    return {"needle": needle, "dep": dep, "routes": routes}


LESSONS = [
    dict(slug="temperature-changes-shc", source_file="temperature-changes-shc.dc.html",
         subject="physics", topic_id="particle-model",
         title="Temperature changes and specific heat capacity", spec="6.3.2.2",
         family="Quantitative", routes=ALL, review_state=RS, batch=B,
         block_map={"s-race": "check", "s-rp": "required-practical", "s-sim": "required-practical"},
         withhold=[W("A 2 kg iron block (c = 450 J/kg°C) cools from 200°C to 50°C", "B3-W1")]),
    dict(slug="sound-waves-hearing", source_file="sound-waves-hearing.dc.html",
         subject="physics", topic_id="waves", title="Sound waves and hearing",
         spec="8463 4.6.1.4", family="Process", routes=["TH"], review_state=RS, batch=B,
         block_map={"s-path": "worked-example"},
         withhold=[W("used for foetal scanning rather than X-rays", "B3-W2")]),
    dict(slug="microscopy", source_file="microscopy.dc.html",
         subject="biology", topic_id="cell-biology", title="Microscopy",
         spec="4.1.1.5", family="Quantitative", routes=ALL, review_state=RS, batch=B,
         block_map={"s-resolve": "check", "s-bench": "required-practical", "s-draw": "check"},
         withhold=[W("What is the maximum magnification of a light microscope?", "B3-W3"),
                   W("An image is 45 mm wide. The actual size is 0.009 mm", "B3-W4")]),
    dict(slug="conservation-of-mass", source_file="conservation-of-mass.dc.html",
         subject="chemistry", topic_id="quantitative",
         title="Conservation of mass and balanced equations", spec="5.3.1.1",
         family="Quantitative", routes=ALL, review_state=RS, batch=B,
         block_map={"s-flask": "figure", "s-write": "check"},
         withhold=[W("24 g of magnesium reacts completely with oxygen", "B3-W5")]),
    dict(slug="atom-economy", source_file="atom-economy.dc.html",
         subject="chemistry", topic_id="quantitative", title="Atom economy",
         spec="8462 4.3.3.2", family="Quantitative", routes=TRIPLE, review_state=RS, batch=B,
         block_map={"s-strip": "figure", "s-brine": "check", "s-route": "comparison"},
         withhold=[W("Why do addition reactions always have an atom economy of 100%?", "B3-W6")]),
    dict(slug="waves-detection-exploration", source_file="waves-detection-exploration.dc.html",
         subject="physics", topic_id="waves", title="Waves for detection and exploration",
         spec="8463 4.6.1.5", family="Investigation", routes=["TH"], review_state=RS, batch=B,
         block_map={"s-quake": "practical", "s-scan": "practical"}),
    dict(slug="mixtures", source_file="mixtures.dc.html",
         subject="chemistry", topic_id="atomic-structure",
         title="Mixtures and separation techniques", spec="5.1.1.2",
         family="Classify", routes=ALL, review_state=RS, batch=B,
         block_map={"s-desk": "check", "s-kit": "practical"}),
    dict(slug="early-atmosphere", source_file="early-atmosphere.dc.html",
         subject="chemistry", topic_id="atmosphere",
         title="The Earth's early atmosphere and how it changed",
         spec="5.9.1.2–5.9.1.4", family="Process", routes=ALL, review_state=RS, batch=B,
         block_map={"s-clock": "worked-example"}),
    dict(slug="specific-latent-heat", source_file="specific-latent-heat.dc.html",
         subject="physics", topic_id="particle-model",
         title="Changes of state and specific latent heat", spec="6.3.2.3",
         family="Quantitative", routes=ALL, review_state=RS, batch=B,
         block_map={"s-ledger": "worked-example", "s-logger": "check"}),
    dict(slug="greenhouse-gases", source_file="greenhouse-gases.dc.html",
         subject="chemistry", topic_id="atmosphere",
         title="Greenhouse gases and climate change", spec="5.9.2.1–5.9.2.4",
         family="Model", routes=ALL, review_state=RS, batch=B,
         block_map={"s-bench": "figure", "s-effects": "check",
                    "s-reports": "check", "s-limits": "check"}),
    dict(slug="types-of-em-waves", source_file="types-of-em-waves.dc.html",
         subject="physics", topic_id="waves", title="Types of electromagnetic waves",
         spec="6.6.2.1", family="Model", routes=ALL, review_state=RS, batch=B,
         block_map={"s-spectrum": "figure"},
         withhold=[W("Which EM wave has the highest frequency?", "B3-W7")]),
    dict(slug="particle-motion-pressure", source_file="particle-motion-pressure.dc.html",
         subject="physics", topic_id="particle-model", title="Particle motion in gases",
         spec="6.3.3.1 (+ 8463 4.3.3.2–4.3.3.3)", family="Model", routes=ALL,
         review_state=RS, batch=B,
         withhold=[W("A gas is at 27°C and 100 kPa", "B3-W8")]),
    dict(slug="power", source_file="power.dc.html",
         subject="physics", topic_id="energy", title="Power", spec="6.1.1.4",
         family="Quantitative", routes=ALL, review_state=RS, batch=B),
]
