"""ks4_lessons.batch_5 — Batch 5 (Prompt AB). Design's own delivery, placed
VERBATIM in docs/ks4/design-reference/batch-5/ (MD5SUMS beside it), ported by
the named rulings in ks4_batch_rulings.py exactly as batch 4 was.

Her shared blocks are byte-identical to batch 4's (checked by md5 and recorded
in docs/ks4/BATCH5-PORT-REPORT.md), so this batch registers the same block set,
reading them from its own copy of her delivery. Batch 5 carries the same
display-time subscript asset as batch 4 (its quiz text has \\u208x escapes).
"""
import os

B = "batch-5"
ALL = ["CF", "CH", "TF", "TH"]
TRIPLE = ["TF", "TH"]

_REF = os.path.join("docs", "ks4", "design-reference", "batch-5", "lessons")
AUTHORED_DIR = _REF
BLOCKS_DIR = _REF
EXT_SRC = os.path.join("ks4_lessons", "batch5_ext.js")  # display-time subscripts (MRB-302); the quiz text carries \u208x escapes

# Same placeholder fix as batch 4 (line inputs inside two nested cards).
EXTRA_CSS = """
/* batch-5: the line inputs' placeholders must fit at phone width (same fix as batch 4). */
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
    L("land-use", "4.7.3.3-land-use", "biology", "ecology", "Land use and peat bogs", "4.7.3.3", "Classify", block_map={'s-conflict': 'explainer'}),
    L("metals-non-metals", "5.1.2.3-metals-non-metals", "chemistry", "atomic-structure", "Metals and non-metals", "5.1.2.3", "Classify", block_map={'s-bench': 'explainer'}),
    L("reactivity-series", "5.4.1.1-reactivity-series", "chemistry", "chemical-changes", "Reactivity of metals", "5.4.1.1", "Model", block_map={'s-oxygen': 'explainer'}),
    L("energy-resources", "6.1.3-energy-resources", "physics", "energy", "Energy resources", "6.1.3", "Classify"),
    L("structure-of-atom", "6.4.1.1-structure-of-atom", "physics", "atomic-structure", "The structure of an atom", "6.4.1.1", "Model"),
    L("plant-tissues", "4.2.3.1-plant-tissues", "biology", "organisation", "Plant tissues and organs", "4.2.3.1", "Model", block_map={'s-tubes': 'explainer'}),
    L("waste-management", "4.7.3.2-waste-management", "biology", "ecology", "Waste management and pollution", "4.7.3.2", "Classify"),
    L("earths-resources", "5.10.1.1-earths-resources", "chemistry", "resources", "Using the Earth’s resources", "5.10.1.1", "Quantitative", block_map={'s-sort1': 'explainer'}),
    L("development-atomic-model", "6.4.1.3-development-atomic-model", "physics", "atomic-structure", "Development of the model of the atom", "6.4.1.3", "Process", block_map={'s-timeline': 'explainer'}),
    L("global-warming", "4.7.3.5-global-warming", "biology", "ecology", "Global warming and ecosystems", "4.7.3.5", "Process", block_map={'s-cause': 'explainer', 's-evidence': 'explainer'}),
    L("group-0", "5.1.2.4-group-0", "chemistry", "atomic-structure", "Group 0", "5.1.2.4", "Model"),
    L("extraction-of-metals", "5.4.1.3-extraction-of-metals", "chemistry", "chemical-changes", "Extraction of metals", "5.4.1.3", "Process", block_map={'s-redox': 'explainer'}),
    L("potable-water", "5.10.1.2-potable-water", "chemistry", "resources", "Potable water", "5.10.1.2", "Quantitative", block_map={'s-potable': 'explainer'}),
    L("radioactive-decay", "6.4.2.1-radioactive-decay", "physics", "atomic-structure", "Radioactive decay", "6.4.2.1", "Model", block_map={'s-decay': 'explainer', 's-uses': 'explainer'}),
    L("red-shift-big-bang", "4.8.2-red-shift-big-bang", "physics", "space", "Red-shift and the Big Bang", "4.8.2", "Process", routes=TRIPLE, block_map={'s-1998': 'explainer'}),
]
