"""ks4_lessons.batch_8 - Batch 8 (Prompt AD). Design's own delivery, placed
VERBATIM in docs/ks4/design-reference/batch-8/ (MD5SUMS beside it), ported by
the named rulings in ks4_batch_rulings.py exactly as batches 4, 5, 6 and 7 were.

Her shared blocks are byte-identical to batch 7's EXCEPT Ks4Steps (an optional
`eyebrow` prop, used by reaction time). Batch 8 registers
its OWN block set, read from its own copy, so batch 4, 5, 6 and 7 pages are
untouched. Same display-time subscript asset as batch 7 (SVG tspan inside figure
labels, added <svg> nodes scanned).
"""
import os

B = "batch-8"
ALL = ["CF", "CH", "TF", "TH"]
TRIPLE = ["TF", "TH"]

_REF = os.path.join("docs", "ks4", "design-reference", "batch-8", "lessons")
AUTHORED_DIR = _REF
BLOCKS_DIR = _REF
EXT_SRC = os.path.join("ks4_lessons", "batch8_ext.js")  # display-time subscripts (MRB-302); the quiz text carries \u208x escapes

# Same placeholder fix as batches 4 and 5 (line inputs inside two nested cards).
EXTRA_CSS = """
/* batch-8: the line inputs' placeholders must fit at phone width (same fix as batch 4). */
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
    L('homeostasis', '4.5.1-homeostasis', "biology", 'homeostasis', 'Homeostasis', '4.5.1', 'Model', block_map={'s-what': 'explainer'}),
    L('nervous-system', '4.5.2.1-nervous-system', "biology", 'homeostasis', 'The nervous system', '4.5.2.1', 'Model'),
    L('reflex-actions', '4.5.2.1-reflex-actions', "biology", 'homeostasis', 'Reflex actions', '4.5.2.1', 'Process'),
    L('reaction-time', '4.5.2.1-reaction-time', "biology", 'homeostasis', 'Reaction time', '4.5.2.1', 'Quantitative'),
    L('the-brain', '4.5.2.2-the-brain', "biology", 'homeostasis', 'The brain', '4.5.2.2', 'Model', routes=TRIPLE),
    L('the-eye', '4.5.2.3-the-eye', "biology", 'homeostasis', 'The eye', '4.5.2.3', 'Model', routes=TRIPLE),
    L('defects-of-the-eye', '4.5.2.3-defects-of-the-eye', "biology", 'homeostasis', 'Defects of the eye', '4.5.2.3', 'Model', routes=TRIPLE, block_map={'s-fix': 'explainer'}),
    L('thermoregulation', '4.5.2.4-thermoregulation', "biology", 'homeostasis', 'Thermoregulation', '4.5.2.4', 'Process', routes=TRIPLE, block_map={'s-centre': 'explainer'}),
    L('endocrine-system', '4.5.3.1-endocrine-system', "biology", 'homeostasis', 'The endocrine system', '4.5.3.1', 'Model'),
    L('blood-glucose-diabetes', '4.5.3.2-blood-glucose-diabetes', "biology", 'homeostasis', 'Blood glucose and diabetes', '4.5.3.2', 'Process'),
    L('human-reproduction-hormones', '4.5.3.4-human-reproduction-hormones', "biology", 'homeostasis', 'Hormones in human reproduction', '4.5.3.4', 'Model', block_map={'s-puberty': 'explainer'}),
    L('contraception-fertility', '4.5.3.5-contraception-fertility', "biology", 'homeostasis', 'Contraception and fertility', '4.5.3.5', 'Classify'),
    L('sexual-asexual-reproduction', '4.6.1.1-sexual-asexual-reproduction', "biology", 'inheritance', 'Sexual and asexual reproduction', '4.6.1.1', 'Classify', block_map={'s-ex': 'explainer'}),
    L('meiosis', '4.6.1.2-meiosis', "biology", 'inheritance', 'Meiosis', '4.6.1.2', 'Process', block_map={'s-why': 'explainer'}),
    L('advantages-sexual-asexual', '4.6.1.3-advantages-sexual-asexual', "biology", 'inheritance', 'Advantages of sexual and asexual reproduction', '4.6.1.3', 'Classify', routes=TRIPLE),
    L('dna-genome', '4.6.1.4-dna-genome', "biology", 'inheritance', 'DNA and the genome', '4.6.1.4', 'Model', block_map={'s-genome': 'explainer'}),
]
