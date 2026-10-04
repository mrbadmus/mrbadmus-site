"""ks4_lessons.batch_4 — Batch 4 (Prompt AA). Design's own delivery, placed
VERBATIM in docs/ks4/design-reference/batch-4/ (MD5SUMS beside it). Unlike
batches 2/3 (authored in final form), these files still carry the review-tool
shape, so `port_rulings=True` routes each through ks4_batch_rulings.py — named
rulings, never hand edits.

Design's spec-numbered file names map to the LIVE slugs below (verified by
ks4_lessons.verify_batch_slugs against all_subtopics_*.py).

`staged=True` = registered but not yet built or shipped: lessons_for_batch()
hides it from every consumer (build, checks, nav) until the flag is removed
by the stage that has checked that lesson on every route.
"""
import os

B = "batch-4"
ALL = ["CF", "CH", "TF", "TH"]
TRIPLE = ["TF", "TH"]

_REF = os.path.join("docs", "ks4", "design-reference", "batch-4", "lessons")
AUTHORED_DIR = _REF       # the lessons (Design's file names) live here
BLOCKS_DIR = _REF         # and so do the shared blocks Design shipped with them

# Block set a batch-4 page registers. The pilot's Ks4Ladder is replaced by
# Ks4Practice; Ks4Triangle / Ks4Guess / Ks4Steps are the Part 1 blocks.
EXT_SRC = os.path.join("ks4_lessons", "batch4_ext.js")  # display-time subscripts (MRB-302)
BLOCK_NAMES = ["Ks4Chrome", "Ks4Choice", "Ks4Sort", "Ks4Chain", "Ks4Write",
               "Ks4Cfifa", "Ks4Triangle", "Ks4Guess", "Ks4Steps", "Ks4Practice",
               "Ks4KeyNote", "Ks4QuizBank", "Ks4End", "Ks4Video"]
# Blocks whose <style> is NOT already in the pilot's shared ks4-lesson.css
# (Cfifa/QuizBank changed only in markup and logic; no style differs).
OWN_CSS_BLOCKS = ["Ks4Triangle", "Ks4Guess", "Ks4Steps", "Ks4Practice"]


def L(slug, f, subject, topic, title, spec, family, routes=ALL, staged=True, **kw):
    d = dict(slug=slug, source_file="ks4-%s-%s.dc.html" % (subject, f),
             subject=subject, topic_id=topic, title=title, spec=spec,
             family=family, routes=routes, review_state="draft", batch=B,
             port_rulings=True, staged=staged)
    d.update(kw)
    return d


LESSONS = [
    L("efficiency", "6.1.2.2-efficiency", "physics", "energy", "Efficiency", "6.1.2.2",
      "Quantitative", staged=False, block_map={"s-waste": "explainer"}),
    L("heart-blood-vessels", "4.2.2.2-heart-blood-vessels", "biology", "organisation",
      "The heart and blood vessels", "4.2.2.2", "Model", staged=False, block_map={'s-heart': 'explainer', 's-vessels': 'explainer', 's-lungs': 'explainer'}),
    L("water-cycle", "4.7.2.2-water-cycle", "biology", "ecology", "The water cycle",
      "4.7.2.2", "Process", staged=False, block_map={'s-cycle': 'explainer', 's-fresh': 'explainer'}),
    L("atmospheric-pollutants", "5.9.3.1-atmospheric-pollutants", "chemistry", "atmosphere",
      "Atmospheric pollutants from fuels", "5.9.3.1", "Model", staged=False,
      block_map={'s-predict': 'explainer', 's-effects': 'explainer'}),
    L("infrared-black-bodies", "4.6.3-infrared-black-bodies", "physics", "waves",
      "Infrared, black bodies", "4.6.3", "Model", routes=TRIPLE, staged=False,
      block_map={'s-curve': 'explainer', 's-black': 'explainer', 's-balance': 'explainer'}),
    L("transport-in-cells", "4.1.3-transport-in-cells", "biology", "cell-biology",
      "Diffusion, osmosis and active transport", "4.1.3", "Classify", staged=False, block_map={'s-three': 'explainer', 's-osmosis': 'explainer', 's-exchange': 'explainer', 's-rp': 'required-practical'}),
    L("blood", "4.2.2.3-blood", "biology", "organisation", "Blood", "4.2.2.3", "Classify", staged=False, block_map={'s-smear': 'explainer', 's-parts': 'explainer'}),
    L("periodic-table", "5.1.2.1-periodic-table", "chemistry", "atomic-structure",
      "The periodic table", "5.1.2.1", "Classify", staged=False,
      block_map={'s-build': 'explainer', 's-trends': 'explainer'}),
    L("thermal-conductivity", "6.1.2.1-thermal-conductivity", "physics", "energy",
      "Thermal conductivity and reducing unwanted energy transfers", "6.1.2.1", "Model", staged=False,
      block_map={'s-conduct': 'explainer', 's-wall': 'explainer', 's-reduce': 'explainer', 's-rp': 'required-practical'}),
    L("coronary-heart-disease", "4.2.2.4-coronary-heart-disease", "biology", "organisation",
      "Coronary heart disease", "4.2.2.4", "Process", staged=False, block_map={'s-narrow': 'explainer', 's-treat': 'explainer', 's-patients': 'explainer'}),
    L("biodiversity", "4.7.3.1-biodiversity", "biology", "ecology", "Biodiversity",
      "4.7.3.1", "Classify", staged=False, block_map={'s-what': 'explainer', 's-webs': 'explainer', 's-people': 'explainer'}),
    L("development-periodic-table", "5.1.2.2-development-periodic-table", "chemistry",
      "atomic-structure", "Development of the periodic table", "5.1.2.2", "Process", staged=False,
      block_map={'s-moves': 'explainer', 's-story': 'explainer', 's-isotopes': 'explainer'}),
    L("uses-em-waves", "6.6.2.4-uses-em-waves", "physics", "waves",
      "Uses of electromagnetic waves", "6.6.2.4", "Classify", staged=False,
      block_map={'s-spectrum': 'explainer', 's-why': 'explainer'}),
]
