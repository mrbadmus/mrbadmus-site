"""ks4_lessons.batch_6 — Batch 6 (Prompt AB). Design's own delivery, placed
VERBATIM in docs/ks4/design-reference/batch-6/ (MD5SUMS beside it), ported by
the named rulings in ks4_batch_rulings.py exactly as batches 4 and 5 were.

Her shared blocks are byte-identical to batch 5's EXCEPT Ks4Triangle (a new
`fixed: true` cell, for pi). So batch 6 registers its OWN block set, read from
its own copy of her delivery, and batch 4 and 5 pages are untouched. Batch 6
carries the same display-time subscript asset as batch 5 (its quiz text has
\\u208x escapes), in the form batch 5 ended with: an SVG tspan inside figure
labels, and added <svg> nodes scanned.
"""
import os

B = "batch-6"
ALL = ["CF", "CH", "TF", "TH"]
TRIPLE = ["TF", "TH"]

_REF = os.path.join("docs", "ks4", "design-reference", "batch-6", "lessons")
AUTHORED_DIR = _REF
BLOCKS_DIR = _REF
EXT_SRC = os.path.join("ks4_lessons", "batch6_ext.js")  # display-time subscripts (MRB-302); the quiz text carries \u208x escapes

# Same placeholder fix as batches 4 and 5 (line inputs inside two nested cards).
EXTRA_CSS = """
/* batch-6: the line inputs' placeholders must fit at phone width (same fix as batch 4). */
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
    L("factors-affecting-food-security", "4.7.5.1-factors-affecting-food-security", "biology", "ecology", "Factors affecting food security", "4.7.5.1", "Classify", routes=TRIPLE, block_map={'s-what': 'explainer'}),
    L("group-1", "5.1.2.5-group-1", "chemistry", "atomic-structure", "Group 1", "5.1.2.5", "Model", block_map={'s-air': 'explainer', 's-why': 'explainer'}),
    L("reactions-of-acids", "5.4.2.1-reactions-of-acids", "chemistry", "chemical-changes", "Reactions of acids", "5.4.2.1", "Process", block_map={'s-formula': 'explainer', 's-redox': 'explainer'}),
    L("stellar-evolution", "4.8.1.2-stellar-evolution", "physics", "space", "Life cycle of a star", "4.8.1.2", "Process", routes=TRIPLE, block_map={'s-elements': 'explainer'}),
    L("animal-plant-cells", "4.1.1.2-animal-plant-cells", "biology", "cell-biology", "Animal and plant cells", "4.1.1.2", "Quantitative"),
    L("cell-specialisation", "4.1.1.3-cell-specialisation", "biology", "cell-biology", "Cell specialisation", "4.1.1.3", "Classify", block_map={'s-diff': 'explainer'}),
    L("culturing-microorganisms", "4.1.1.6-culturing-microorganisms", "biology", "cell-biology", "Culturing microorganisms", "4.1.1.6", "Quantitative", routes=TRIPLE, block_map={'s-aseptic': 'explainer'}),
    L("stem-cells", "4.1.2.3-stem-cells", "biology", "cell-biology", "Stem cells", "4.1.2.3", "Classify", block_map={'s-clone': 'explainer'}),
    L("principles-of-organisation", "4.2.1-principles-of-organisation", "biology", "organisation", "Principles of organisation", "4.2.1", "Quantitative", block_map={'s-scale': 'explainer'}),
    L("digestive-system", "4.2.2.1-digestive-system", "biology", "organisation", "The digestive system", "4.2.2.1", "Model", block_map={'s-enz': 'explainer'}),
    L("health-disease", "4.2.2.5-health-disease", "biology", "organisation", "Health, disease and risk factors", "4.2.2.5", "Classify", block_map={'s-health': 'explainer', 's-risk': 'explainer'}),
    L("cancer", "4.2.2.7-cancer", "biology", "organisation", "Cancer", "4.2.2.7", "Model", block_map={'s-risk': 'explainer'}),
    L("transpiration", "4.2.3.2-transpiration", "biology", "organisation", "Transpiration", "4.2.3.2", "Process"),
    L("translocation", "4.2.3.2-translocation", "biology", "organisation", "Translocation", "4.2.3.2", "Process"),
]
