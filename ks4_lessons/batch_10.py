"""ks4_lessons.batch_10 - Batch 10. Design's own delivery, placed
VERBATIM in docs/ks4/design-reference/batch-10/ (MD5SUMS beside it), ported by
the named rulings in ks4_batch_rulings.py exactly as batches 4-8 were.

Her shared blocks are byte-identical to batch 8's. Batch 10 registers its OWN
block set, read from its own copy, so earlier batches are untouched. Same
display-time subscript asset as batches 5-8.
"""
import os

B = "batch-10"
ALL = ["CF", "CH", "TF", "TH"]
TRIPLE = ["TF", "TH"]

_REF = os.path.join("docs", "ks4", "design-reference", "batch-10", "lessons")
AUTHORED_DIR = _REF
BLOCKS_DIR = _REF
EXT_SRC = os.path.join("ks4_lessons", "batch10_ext.js")  # display-time subscripts (MRB-302); the quiz text carries \u208x escapes

# Same placeholder fix as batches 4 and 5 (line inputs inside two nested cards).
EXTRA_CSS = """
/* batch-10: the line inputs' placeholders must fit at phone width (same fix as batch 4). */
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
    L('ecosystems', '4.7.1.1-ecosystems', "biology", 'ecology', 'Ecosystems', '4.7.1.1', 'Model', block_map={'s-data': 'explainer'}),
    L('population-competition', '4.7.1.1-population-competition', "biology", 'ecology', 'Population and competition', '4.7.1.1', 'Model', block_map={'s-limits': 'explainer'}),
    L('abiotic-biotic-factors', '4.7.1.2-abiotic-biotic-factors', "biology", 'ecology', 'Abiotic and biotic factors', '4.7.1.2', 'Classify', block_map={'s-biotic': 'explainer', 's-data': 'explainer'}),
    L('adaptations', '4.7.1.4-adaptations', "biology", 'ecology', 'Adaptations', '4.7.1.4', 'Classify', block_map={'s-sav': 'explainer'}),
    L('food-chains-webs', '4.7.2.1-food-chains-webs', "biology", 'ecology', 'Food chains and food webs', '4.7.2.1', 'Model', block_map={'s-trophic': 'explainer'}),
    L('sampling-techniques', '4.7.2.1-sampling-techniques', "biology", 'ecology', 'Sampling techniques', '4.7.2.1', 'Quantitative', block_map={'s-stats': 'explainer'}),
    L('environmental-change', '4.7.2.4-environmental-change', "biology", 'ecology', 'The impact of environmental change', '4.7.2.4', 'Model', routes=['TH'], block_map={'s-three': 'explainer', 's-data': 'explainer'}),
    L('deforestation', '4.7.3.4-deforestation', "biology", 'ecology', 'Deforestation', '4.7.3.4', 'Process', block_map={'s-why': 'explainer', 's-weigh': 'explainer'}),
    L('maintaining-biodiversity', '4.7.3.6-maintaining-biodiversity', "biology", 'ecology', 'Maintaining biodiversity', '4.7.3.6', 'Classify', block_map={'s-impact': 'explainer', 's-weigh': 'explainer'}),
    L('trophic-levels', '4.7.4.1-trophic-levels', "biology", 'ecology', 'Trophic levels', '4.7.4.1', 'Model', routes=TRIPLE),
    L('pyramids-of-biomass', '4.7.4.2-pyramids-of-biomass', "biology", 'ecology', 'Pyramids of biomass', '4.7.4.2', 'Quantitative', routes=TRIPLE, block_map={'s-scale': 'explainer'}),
    L('transfer-of-biomass', '4.7.4.3-transfer-of-biomass', "biology", 'ecology', 'Transfer of biomass', '4.7.4.3', 'Quantitative', routes=TRIPLE),
    L('farming-techniques', '4.7.5.2-farming-techniques', "biology", 'ecology', 'Farming techniques', '4.7.5.2', 'Classify', routes=TRIPLE, block_map={'s-eval': 'explainer'}),
    L('sustainable-fisheries', '4.7.5.3-sustainable-fisheries', "biology", 'ecology', 'Sustainable fisheries', '4.7.5.3', 'Model', routes=TRIPLE, block_map={'s-problem': 'explainer', 's-graph': 'explainer'}),
    L('role-of-biotechnology', '4.7.5.4-role-of-biotechnology', "biology", 'ecology', 'The role of biotechnology', '4.7.5.4', 'Process', routes=TRIPLE, block_map={'s-gm': 'explainer'}),
]
