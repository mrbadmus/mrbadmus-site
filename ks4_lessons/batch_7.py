"""ks4_lessons.batch_7 - Batch 7 (Prompt AC). Design's own delivery, placed
VERBATIM in docs/ks4/design-reference/batch-7/ (MD5SUMS beside it), ported by
the named rulings in ks4_batch_rulings.py exactly as batches 4, 5 and 6 were.

Her shared blocks are byte-identical to batch 6's EXCEPT Ks4Triangle (the top
item may now be a `fixed: true` cell, for the 1 in 1/d^2). Batch 7 registers
its OWN block set, read from its own copy, so batch 4, 5 and 6 pages are
untouched. Same display-time subscript asset as batch 6 (SVG tspan inside figure
labels, added <svg> nodes scanned).
"""
import os

B = "batch-7"
ALL = ["CF", "CH", "TF", "TH"]
TRIPLE = ["TF", "TH"]

_REF = os.path.join("docs", "ks4", "design-reference", "batch-7", "lessons")
AUTHORED_DIR = _REF
BLOCKS_DIR = _REF
EXT_SRC = os.path.join("ks4_lessons", "batch7_ext.js")  # display-time subscripts (MRB-302); the quiz text carries \u208x escapes

# Same placeholder fix as batches 4 and 5 (line inputs inside two nested cards).
EXTRA_CSS = """
/* batch-7: the line inputs' placeholders must fit at phone width (same fix as batch 4). */
@media (max-width: 520px) {
  #ks4-mount div[data-arrive][style*="align-items: flex-start; padding: 14px 16px"] { gap: 8px !important; padding: 12px 10px !important; }
  #ks4-mount div[data-arrive][style*="align-items: flex-start; padding: 14px 16px"] > span[aria-hidden="true"] { flex-basis: 28px !important; width: 28px !important; height: 28px !important; font-size: 16px !important; }
  #ks4-mount input[type="text"]::placeholder { font-size: 11px; letter-spacing: -.03em; }
}
@media (max-width: 380px) {
  #ks4-mount input[type="text"]::placeholder { font-size: 10px; }
}
"""
BLOCK_NAMES = ["Ks4Chrome", "Ks4Choice", "Ks4Sort", "Ks4Chain", "Ks4Write",
               "Ks4Cfifa", "Ks4Triangle", "Ks4Guess", "Ks4Steps", "Ks4Practice",
               "Ks4KeyNote", "Ks4QuizBank", "Ks4End", "Ks4Video"]
OWN_CSS_BLOCKS = ["Ks4Triangle", "Ks4Guess", "Ks4Steps", "Ks4Practice"]


def L(slug, f, subject, topic, title, spec, family, routes=ALL, **kw):
    d = dict(slug=slug, source_file="ks4-%s-%s.dc.html" % (subject, f),
             subject=subject, topic_id=topic, title=title, spec=spec,
             family=family, routes=routes, review_state="examiner-reviewed", batch=B,
             port_rulings=True, staged=False)
    d.update(kw)
    return d


LESSONS = [
    L("communicable-diseases-defence", "4.3.1.1-communicable-diseases-defence", "biology", "infection-response", "Communicable diseases and defences", "4.3.1.1", "Classify", block_map={'s-spread': 'explainer'}),
    L("viral-diseases", "4.3.1.2-viral-diseases", "biology", "infection-response", "Viral diseases", "4.3.1.2", "Classify"),
    L("bacterial-diseases", "4.3.1.3-bacterial-diseases", "biology", "infection-response", "Bacterial diseases", "4.3.1.3", "Classify"),
    L("fungal-protist-diseases", "4.3.1.4-fungal-protist-diseases", "biology", "infection-response", "Fungal and protist diseases", "4.3.1.4", "Classify"),
    L("vaccination", "4.3.1.7-vaccination", "biology", "infection-response", "Vaccination", "4.3.1.7", "Process"),
    L("antibiotics-painkillers", "4.3.1.8-antibiotics-painkillers", "biology", "infection-response", "Antibiotics and painkillers", "4.3.1.8", "Classify", block_map={'s-slow': 'explainer'}),
    L("drug-discovery-development", "4.3.1.9-drug-discovery-development", "biology", "infection-response", "Drug discovery and development", "4.3.1.9", "Process", block_map={'s-source': 'explainer'}),
    L("monoclonal-antibodies", "4.3.2.1-monoclonal-antibodies", "biology", "infection-response", "Monoclonal antibodies", "4.3.2.1", "Process", routes=["TH"], block_map={'s-uses': 'explainer'}),
    L("plant-disease-detection-defence", "4.3.3.1-plant-disease-detection-defence", "biology", "infection-response", "Plant disease and defences", "4.3.3.1", "Classify", routes=TRIPLE, block_map={'s-defence': 'explainer'}),
    L("photosynthesis", "4.4.1.1-photosynthesis", "biology", "bioenergetics", "Photosynthesis", "4.4.1.1", "Process"),
    L("rate-of-photosynthesis", "4.4.1.2-rate-of-photosynthesis", "biology", "bioenergetics", "Rate of photosynthesis", "4.4.1.2", "Quantitative", block_map={'s-calc': 'explainer'}),
    L("uses-of-glucose", "4.4.1.3-uses-of-glucose", "biology", "bioenergetics", "Uses of glucose", "4.4.1.3", "Classify"),
    L("aerobic-respiration", "4.4.2.1-aerobic-respiration", "biology", "bioenergetics", "Aerobic respiration", "4.4.2.1", "Process"),
    L("anaerobic-respiration", "4.4.2.1-anaerobic-respiration", "biology", "bioenergetics", "Anaerobic respiration", "4.4.2.1", "Process"),
    L("response-to-exercise", "4.4.2.2-response-to-exercise", "biology", "bioenergetics", "Response to exercise", "4.4.2.2", "Model"),
    L("metabolism", "4.4.2.3-metabolism", "biology", "bioenergetics", "Metabolism", "4.4.2.3", "Model", block_map={'s-urea': 'explainer'}),
]
