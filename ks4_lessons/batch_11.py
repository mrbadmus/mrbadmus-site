"""ks4_lessons.batch_11 - Batch 11. Design's own delivery, placed
VERBATIM in docs/ks4/design-reference/batch-11/ (MD5SUMS beside it), ported by
the named rulings in ks4_batch_rulings.py exactly as batches 4-8 were.

Her shared blocks are byte-identical to batches 8 and 10. Batch 11 registers its OWN
block set, read from its own copy, so earlier batches are untouched. Same
display-time subscript asset as batches 5-8.
"""
import os

B = "batch-11"
ALL = ["CF", "CH", "TF", "TH"]
TRIPLE = ["TF", "TH"]
HIGHER = ["CH", "TH"]

_REF = os.path.join("docs", "ks4", "design-reference", "batch-11", "lessons")
AUTHORED_DIR = _REF
BLOCKS_DIR = _REF
EXT_SRC = os.path.join("ks4_lessons", "batch11_ext.js")  # display-time subscripts (MRB-302); the quiz text carries \u208x escapes

# Same placeholder fix as batches 4 and 5 (line inputs inside two nested cards).
EXTRA_CSS = """
/* batch-11: the line inputs' placeholders must fit at phone width (same fix as batch 4). */
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
    L('model-of-the-atom', '5.1.1.3-model-of-the-atom', "chemistry", 'atomic-structure', 'Development of the model of the atom', '5.1.1.3', 'Process', block_map={'s-chain': 'explainer', 's-scatter': 'explainer'}),
    L('subatomic-particles', '5.1.1.4-subatomic-particles', "chemistry", 'atomic-structure', 'Subatomic particles', '5.1.1.4', 'Classify', block_map={'s-half': 'explainer'}),
    L('relative-atomic-mass', '5.1.1.6-relative-atomic-mass', "chemistry", 'atomic-structure', 'Relative atomic mass, atomic number and isotopes', '5.1.1.6', 'Quantitative'),
    L('electronic-structure', '5.1.1.7-electronic-structure', "chemistry", 'atomic-structure', 'Electronic structure', '5.1.1.7', 'Model'),
    L('group-7', '5.1.2.6-group-7', "chemistry", 'atomic-structure', 'Group 7: the halogens', '5.1.2.6', 'Classify', block_map={'s-grid': 'explainer', 's-ionic': 'explainer'}),
    L('transition-metals', '4.1.3.1-transition-metals', "chemistry", 'atomic-structure', 'Properties of transition metals', '4.1.3.1', 'Classify', routes=TRIPLE),
    L('mass-changes-reactions', '5.3.1.3-mass-changes-reactions', "chemistry", 'quantitative', 'Mass changes in reactions', '5.3.1.3', 'Quantitative'),
    L('chemical-measurements', '5.3.1.4-chemical-measurements', "chemistry", 'quantitative', 'Chemical measurements', '5.3.1.4', 'Quantitative', block_map={'s-words': 'explainer'}),
    L('moles', '5.3.2.1-moles', "chemistry", 'quantitative', 'Moles', '5.3.2.1', 'Quantitative', routes=HIGHER, block_map={'9': 'explainer'}),
    L('amounts-in-equations', '5.3.2.2-amounts-in-equations', "chemistry", 'quantitative', 'Amounts of substances in equations', '5.3.2.2', 'Quantitative', routes=HIGHER, block_map={'8': 'explainer', 's-masses': 'explainer'}),
    L('oxidation-reduction', '5.4.1.4-oxidation-reduction', "chemistry", 'chemical-changes', 'Oxidation and reduction', '5.4.1.4', 'Process'),
    L('salts-neutralisation', '5.4.2.2-salts-neutralisation', "chemistry", 'chemical-changes', 'Making salts and neutralisation', '5.4.2.2', 'Process', block_map={'s-name': 'explainer', 's-ionic': 'explainer', 's-titr': 'explainer'}),
    L('ph-scale', '5.4.2.4-ph-scale', "chemistry", 'chemical-changes', 'The pH scale and neutralisation', '5.4.2.4', 'Model', block_map={'s-ten': 'explainer'}),
    L('strong-weak-acids', '5.4.2.5-strong-weak-acids', "chemistry", 'chemical-changes', 'Strong and weak acids', '5.4.2.5', 'Quantitative', routes=HIGHER, block_map={'s-grid': 'explainer'}),
    L('electrolysis-principles', '5.4.3.1-electrolysis-principles', "chemistry", 'chemical-changes', 'The process of electrolysis', '5.4.3.1', 'Model', block_map={'s-terms': 'explainer', 's-ht': 'explainer'}),
    L('electrolysis-molten', '5.4.3.2-electrolysis-molten', "chemistry", 'chemical-changes', 'Electrolysis of molten ionic compounds', '5.4.3.2', 'Process', block_map={'s-demo': 'explainer', 's-half': 'explainer'}),
]
