"""ks4_lessons.batch_lean: the lean lesson pilot (docs/lessons/LEAN-STANDARD.md).

One record per lesson (ks4_lessons/lean/<slug>.py) builds a lean page on all four
routes. The eight Energy lessons below are the pilot. Five were live Design
lessons in batches 2 to 5; their legacy page still supplies the chrome, the
route switch, the ladder, the quiz bank and the logic class (rungs, bank and every
quiz item stay verbatim). Three were old generate_site_v5 pages and are rebuilt
from their record alone.

THE LEAN BATCH OWNS ITS SLUGS. The legacy batches keep their LESSONS lists, so their
shared per-batch assets (ks4-source-*.js, ks4-lesson-*.css, ks4-ext-*.js) stay
byte-identical. They simply do not WRITE a page, or list one in their manifest, for a
slug the lean batch owns (ks4_lessons.lean_owned_slugs()), in either build order.

Only slugs whose record file exists are registered, so the slice builds as records
arrive.
"""
import importlib
import os

from . import lean as _lean

B = "batch-lean"
ALL = ["CF", "CH", "TF", "TH"]
LEAN = True   # ks4_lessons.all_lessons() skips this module: NAV in ks4-lib.js must not move

SLUGS = ["efficiency", "changes-in-energy", "power", "thermal-conductivity",
         "energy-resources", "energy-stores-systems", "energy-changes-in-systems",
         "energy-transfers-in-a-system"]

# Lessons that have no legacy page: identity comes from here (the subtopic data's own
# title and spec, 6.1.1.1 / 6.1.1.3 / 6.1.2.1).
_OLD_FORMAT = {
    "energy-stores-systems": ("Energy stores and systems", "6.1.1.1", "Model"),
    "energy-changes-in-systems": ("Energy changes in systems", "6.1.1.3", "Quantitative"),
    "energy-transfers-in-a-system": ("Energy transfers in a system", "6.1.2.1", "Model"),
}

BLOCKS_DIR = os.path.join("ks4_lessons", "lean", "blocks")
BLOCK_NAMES = ["Ks4Chrome", "Ks4Choice", "Ks4Sort", "Ks4Chain", "Ks4Write",
               "Ks4Cfifa", "Ks4Triangle", "Ks4Guess", "Ks4Steps", "Ks4Practice",
               "Ks4Ladder", "Ks4QuizBank", "Ks4End", "Ks4Video"]
# Blocks whose <style> is not already in the pilot's shared ks4-lesson.css.
OWN_CSS_BLOCKS = ["Ks4Triangle", "Ks4Guess", "Ks4Steps", "Ks4Practice"]
EXT_SRC = os.path.join("ks4_lessons", "batch5_ext.js")   # display-time subscripts (MRB-302)

# What a lean page's sections are, for ks4_lessons.blocks.classify_section().
_BLOCK_MAP = {"s-words": "keyword", "s-knowledge": "explainer", "s-fact": "key-fact",
              "s-deeper": "explainer"}


def _extra_css():
    from . import batch_4
    return batch_4.EXTRA_CSS   # the line-input placeholder rule the Steps and Cfifa blocks need


EXTRA_CSS = _extra_css()


def _legacy(slug, batch):
    mod = importlib.import_module("ks4_lessons.%s" % batch.replace("-", "_"))
    for L in mod.LESSONS:
        if L["slug"] == slug:
            return L
    raise ValueError("batch_lean: %r is not in %s" % (slug, batch))


def _lesson(slug, rec):
    legacy = (rec.get("legacy") or {}).get("batch")
    if legacy:
        d = dict(_legacy(slug, legacy))
        d["legacy_batch"] = legacy
    else:
        title, spec, family = _OLD_FORMAT[slug]
        d = dict(slug=slug, subject="physics", topic_id="energy", title=title, spec=spec,
                 family=family, routes=ALL, review_state="examiner-reviewed",
                 legacy_batch=None)
    d.update(batch=B, staged=False, lean=rec, unit="Energy",
             block_map=dict(_BLOCK_MAP))
    return d


LESSONS = [_lesson(s, _lean.records()[s]) for s in SLUGS if s in _lean.records()]
