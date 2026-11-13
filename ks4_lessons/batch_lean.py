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
import re

from . import lean as _lean

B = "batch-lean"
ALL = ["CF", "CH", "TF", "TH"]
LEAN = True   # ks4_lessons.all_lessons() skips this module: NAV in ks4-lib.js must not move

SLUGS = ["efficiency", "changes-in-energy", "power", "thermal-conductivity",
         "energy-resources", "energy-stores-systems", "energy-changes-in-systems",
         "energy-transfers-in-a-system"]

# Slugs the lean batch registers when their record exists: the eight above first (their order
# is part of the Energy pages' bytes), then every other record in ks4_lessons/lean/, by slug.
# Wave 1 (docs/lessons/LEAN-PLAN.md): Physics Magnetism, ten old-format lessons.

# Lessons that have no legacy page: identity comes from here (the subtopic data's own
# title and spec, 6.1.1.1 / 6.1.1.3 / 6.1.2.1). The three Energy ones are written out so
# their pages stay byte-identical; every OTHER old-format lesson is derived from the subtopic
# data by _derive() below.
_OLD_FORMAT = {
    "energy-stores-systems": ("Energy stores and systems", "6.1.1.1", "Model"),
    "energy-changes-in-systems": ("Energy changes in systems", "6.1.1.3", "Quantitative"),
    "energy-transfers-in-a-system": ("Energy transfers in a system", "6.1.2.1", "Model"),
}

# ── old-format lessons beyond Energy: identity derived from all_subtopics_<subject>*.py ──
# Subject and topic of each unit whose old-format lessons are derived, and the unit name the
# header chrome shows. A unit is added here when its first record lands.
_UNITS = {
    ("physics", "magnetism"): "Magnetism and electromagnetism",
}
# The family label (the eyebrow's last word) is a ruled choice per lesson, drawn from the
# labels the existing batches use: Model, Quantitative, Process, Classify, Contrast,
# Investigation, Required practical. Magnetism: poles are sorted (Classify), the two field
# lessons and electromagnetism are about drawing the field (Model), the motor effect, motors,
# loudspeakers, the generator effect and microphones are cause-and-effect chains (Process),
# transformers is the one with a calculation (Quantitative).
_FAMILY = {
    "poles-of-a-magnet": "Classify",
    "magnetic-fields": "Model",
    "electromagnetism": "Model",
    "flemings-left-hand-rule": "Process",
    "electric-motors": "Process",
    "loudspeakers-headphones": "Process",
    "induced-potential": "Process",
    "uses-generator-effect": "Process",
    "microphones": "Process",
    "transformers": "Quantitative",
}
# Words kept capitalised by sentence_case() beyond the first word.
_KEEP_CAPS = {"Fleming's"}

_SUBTOPIC_MODULES = {
    "physics": {"CF": "all_subtopics_physics", "CH": "all_subtopics_physics_higher",
                "TF": "all_subtopics_physics_triple_foundation",
                "TH": "all_subtopics_physics_triple_higher"},
}
_SUBTOPIC_ATTR = {"physics": "PHYSICS_SUBTOPICS_ALL"}
_DATA = {}


def _subtopics(subject):
    """{route: {topic_id: [subtopic dict]}} for one subject (cached)."""
    if subject not in _DATA:
        _DATA[subject] = {r: getattr(importlib.import_module(m), _SUBTOPIC_ATTR[subject])
                          for r, m in _SUBTOPIC_MODULES[subject].items()}
    return _DATA[subject]


def sentence_case(title):
    """'Magnetic Fields' -> 'Magnetic fields', as the pilot titled its lessons."""
    words = title.split()
    return " ".join([words[0]] + [w if w in _KEEP_CAPS else w.lower() for w in words[1:]])


def clean_spec(spec):
    """'6.7.2.4 (HT only, physics only)' -> '6.7.2.4'."""
    return re.sub(r"\s*\([^)]*\)", "", str(spec)).strip()


def _derive(slug):
    """Identity of an old-format lesson (no legacy page, not one of the Energy three) from the
    subtopic data: subject, topic, unit, sentence-case title, clean spec, and ROUTES = only
    the routes the subtopic exists on. Fails loudly if the slug is not in a known unit."""
    for (subject, topic), unit in _UNITS.items():
        found = {}
        for route, tree in _subtopics(subject).items():
            for st in tree.get(topic, []):
                if st["id"] == slug:
                    found[route] = st
        if not found:
            continue
        if slug not in _FAMILY:
            raise ValueError("batch_lean: %r has no family label in _FAMILY" % slug)
        canon = found.get("TH") or next(iter(found.values()))   # TH is the 'everything' tier
        return dict(slug=slug, subject=subject, topic_id=topic,
                    title=sentence_case(canon["title"]), spec=clean_spec(canon["spec"]),
                    family=_FAMILY[slug], routes=[r for r in ALL if r in found],
                    review_state="examiner-reviewed", legacy_batch=None, source_file=None,
                    unit=unit)
    raise ValueError("batch_lean: %r is not a subtopic of any unit in _UNITS (%s)"
                     % (slug, ", ".join("%s/%s" % k for k in _UNITS)))


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
        unit = "Energy"
    elif slug in _OLD_FORMAT:
        title, spec, family = _OLD_FORMAT[slug]
        unit = "Energy"
        d = dict(slug=slug, subject="physics", topic_id="energy", title=title, spec=spec,
                 family=family, routes=ALL, review_state="examiner-reviewed",
                 legacy_batch=None,
                 # no Design file: the key exists (as None) because tools that walk every
                 # registered batch index lessons by `source_file`
                 source_file=None)
    else:
        d = _derive(slug)
        unit = d.pop("unit")
    d.update(batch=B, staged=False, lean=rec, unit=unit,
             block_map=dict(_BLOCK_MAP))
    return d


def _slugs():
    recs = _lean.records()
    return [s for s in SLUGS if s in recs] + sorted(s for s in recs if s not in SLUGS)


LESSONS = [_lesson(s, _lean.records()[s]) for s in _slugs()]
