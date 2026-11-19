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
# Wave 1 (docs/lessons/LEAN-PLAN.md): Physics Magnetism (ten old-format lessons), then Biology
# Ecology (eight old-format lessons derived below, fifteen legacy batch-10 lessons), Chemistry
# Quantitative, then Physics Waves (six old-format lessons, three new ones, six legacy lessons
# from batches 2, 3 and 4), then Biology Organisation (eleven legacy lessons from batches 2, 4, 5
# and 6; see BIO_EYEBROW below), then Chemistry Chemical analysis (six old-format lessons and
# two legacy batch-2 lessons).

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
    ("biology", "ecology"): "Ecology",
    ("chemistry", "quantitative"): "Quantitative chemistry",
    ("physics", "waves"): "Waves",
    ("biology", "organisation"): "Organisation",
    ("chemistry", "analysis"): "Chemical analysis",
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
    "gas-volumes": "Quantitative",
    # Ecology's eight old-format lessons (the fifteen legacy ones keep batch 10's own family)
    "biodiversity": "Model",
    "waste-management": "Process",
    "land-use": "Process",
    "global-warming": "Process",
    "carbon-cycle": "Model",
    "water-cycle": "Model",
    "decomposition": "Process",
    "factors-affecting-food-security": "Classify",
    # Waves: six old-format lessons rebuilt, and three new physics-only lessons (8463 4.6.1.3,
    # Required practical activity 9, 4.6.2.6). The six legacy ones keep their batch's own family.
    "transverse-longitudinal-waves": "Model",
    "properties-of-waves": "Quantitative",
    "properties-em-waves-1": "Model",
    "properties-em-waves-2": "Classify",
    "wave-front-refraction": "Model",
    "radiation-balance-temperature": "Process",
    "reflection-of-waves": "Model",
    "required-practical-light": "Required practical",
    "visible-light": "Model",
    # Chemical analysis: six old-format lessons rebuilt (the two legacy ones keep batch 2's family)
    "pure-substances": "Contrast",
    "formulations": "Classify",
    "chromatography": "Required practical",
    "testing-for-gases": "Classify",
    "flame-tests": "Classify",
    "instrumental-methods": "Process",
}
# Ecology lessons whose record has no `legacy` but which were live Design lessons in an earlier
# batch: the lean page is built from the record alone and replaces that page. slug -> the one
# batch it replaces (ks4_lessons.verify_no_slug_collisions refuses any other collision).
SUPERSEDES = {
    "biodiversity": "batch-4", "water-cycle": "batch-4",
    "carbon-cycle": "batch-2", "decomposition": "batch-2",
    "global-warming": "batch-5", "land-use": "batch-5", "waste-management": "batch-5",
    "factors-affecting-food-security": "batch-6",
}
# The AQA section number of each old-format Biology lesson, taken from the lesson's curriculum
# table (docs/lessons/wave1/ks4-<slug>.md, its Sources line) and NOT from the subtopic data, whose
# `spec` is sometimes only the section (carbon-cycle, water-cycle and decomposition say 4.7.3).
# Biology numbers the same in 8464 and 8461, so one number serves both specs, except
# decomposition: 8464 has no Decomposition section, so on CF/CH it is the 4.7.2.2 line on
# microorganisms; 8461 teaches it as 4.7.2.3 (TF/TH). A (combined, triple) pair says so.
_SPEC = {
    "biodiversity": "4.7.3.1",
    "waste-management": "4.7.3.2",
    "land-use": "4.7.3.3",
    "global-warming": "4.7.3.5",
    "carbon-cycle": "4.7.2.2",
    "water-cycle": "4.7.2.2",
    "decomposition": ("4.7.2.2", "4.7.2.3"),
    "factors-affecting-food-security": "4.7.5.1",
}
# The AQA section number of each Biology Organisation lesson (8464 and 8461 number section 4.2 the
# same, word for word), from the lesson's curriculum table (docs/lessons/wave1/ks4-<slug>.md). All
# eleven are legacy Design pages, so the number on the page comes from the legacy header's literal
# ("AQA Biology 4.2.x", rebuilt per route by lean_ks4) or, for enzymes, from its own logic. The
# subtopic data's `spec` is wrong on nine of the eleven (enzymes "4.2.2.2", blood "4.2.3.2", ...)
# and is never read for them; this table is what the build checks the page's number against
# (lean_ks4 stops on a mismatch, and on a self-bound eyebrow that does not name it on both routes).
BIO_EYEBROW = {
    "principles-of-organisation": "4.2.1",
    "digestive-system": "4.2.2.1",
    "enzymes": "4.2.2.1",
    "heart-blood-vessels": "4.2.2.2",
    "blood": "4.2.2.3",
    "coronary-heart-disease": "4.2.2.4",
    "health-disease": "4.2.2.5\u20134.2.2.6",
    "cancer": "4.2.2.7",
    "plant-tissues": "4.2.3.1",
    "transpiration": "4.2.3.2",
    "translocation": "4.2.3.2",
}
# The 8464 section number of an old-format PHYSICS lesson whose subtopic data has it wrong, so
# the eyebrow is not derived from that data (docs/lessons/wave1/ks4-<slug>.md, its Sources line).
# The physics eyebrow rule turns 6.x into 8463's 4.x. wave-front-refraction's data says
# "6.6.2 (HT only)": it is 6.6.2.2 / 4.6.2.2. radiation-balance-temperature's data says
# "6.6.5.4": it is 8463 4.6.3.2, and 8464 has no such point; "6.6.3.2" is written so the rule
# gives "AQA Physics (8463) 4.6.3.2" on TH, its only route (its Combined form is never shown, as
# for transformers, TH only, 6.7.3.4).
_PHYS_SPEC = {
    "wave-front-refraction": "6.6.2.2",
    "radiation-balance-temperature": "6.6.3.2",
}
# Chemistry numbers its sections differently in the two specs: AQA Combined Science (8464)
# writes 5.3.x.y, AQA Chemistry (8462) writes 4.3.x.y (the sub-numbers happen to agree in this
# unit, but are written out per lesson, never derived). slug -> (8464 number, 8462 number), each
# taken from the lesson's curriculum table (docs/lessons/wave1/ks4-<slug>.md, its Sources line).
# percentage-yield and atom-economy exist on TF/TH only (8462 4.3.3.x, "chemistry only"), so
# their Combined slot is None. The lean page's eyebrow is built from this table when the legacy
# header writes a literal "AQA Chemistry 5.3.x.y" (moles, amounts-in-equations,
# chemical-measurements, mass-changes-reactions); the other six legacy pages bind eyebrowLine /
# specRef per route themselves, and lean_pilot_drive checks every route's number against this table.
CHEM_EYEBROW = {
    "conservation-of-mass": ("5.3.1.1", "4.3.1.1"),
    "relative-formula-mass": ("5.3.1.2", "4.3.1.2"),
    "mass-changes-reactions": ("5.3.1.3", "4.3.1.3"),
    "chemical-measurements": ("5.3.1.4", "4.3.1.4"),
    "moles": ("5.3.2.1", "4.3.2.1"),
    "amounts-in-equations": ("5.3.2.2", "4.3.2.2"),
    "using-moles-calculations": ("5.3.2.3\u20135.3.2.4", "4.3.2.3\u20134.3.2.4"),
    "concentration-of-solutions": ("5.3.2.5", "4.3.2.5"),
    "percentage-yield": (None, "4.3.3.1"),
    "atom-economy": (None, "4.3.3.2"),
    "gas-volumes": (None, "4.3.5"),
    # Chemical analysis (8464 5.8 / 8462 4.8); the Triple-only lessons have no Combined slot
    "pure-substances": ("5.8.1.1", "4.8.1.1"),
    "formulations": ("5.8.1.2", "4.8.1.2"),
    "chromatography": ("5.8.1.3", "4.8.1.3"),
    "testing-for-gases": ("5.8.2.1\u20135.8.2.4", "4.8.2.1\u20134.8.2.4"),
    "flame-tests": (None, "4.8.3.1"),
    "instrumental-methods": (None, "4.8.3.6\u20134.8.3.7"),
    "metal-hydroxides": (None, "4.8.3.2"),
    "carbonates-halides-sulfates": (None, "4.8.3.3\u20134.8.3.5"),
}
# Words kept capitalised by sentence_case() beyond the first word.
_KEEP_CAPS = {"Fleming's"}

_SUBTOPIC_MODULES = {
    "physics": {"CF": "all_subtopics_physics", "CH": "all_subtopics_physics_higher",
                "TF": "all_subtopics_physics_triple_foundation",
                "TH": "all_subtopics_physics_triple_higher"},
    "chemistry": {"CF": "all_subtopics_chemistry", "CH": "all_subtopics_chemistry_higher",
                  "TF": "all_subtopics_chemistry_triple_foundation",
                  "TH": "all_subtopics_chemistry_triple_higher"},
    "biology": {"CF": "all_subtopics_biology", "CH": "all_subtopics_biology_higher",
                "TF": "all_subtopics_biology_triple_foundation",
                "TH": "all_subtopics_biology_triple_higher"},
}
_SUBTOPIC_ATTR = {"physics": "PHYSICS_SUBTOPICS_ALL", "biology": "BIOLOGY_SUBTOPICS_ALL",
                  "chemistry": "CHEMISTRY_SUBTOPICS_ALL"}
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
        spec, spec_c = clean_spec(canon["spec"]), None
        if subject == "physics" and slug in _PHYS_SPEC:
            spec = _PHYS_SPEC[slug]
        if subject == "biology":
            if slug not in _SPEC:
                raise ValueError("batch_lean: %r has no section number in _SPEC" % slug)
            spec = _SPEC[slug]
            if isinstance(spec, tuple):
                spec_c, spec = spec
        d = dict(slug=slug, subject=subject, topic_id=topic,
                    title=sentence_case(canon["title"]), spec=spec,
                    family=_FAMILY[slug], routes=[r for r in ALL if r in found],
                    review_state="examiner-reviewed", legacy_batch=None, source_file=None,
                    unit=unit)
        if spec_c:
            d["spec_c"] = spec_c
        return d
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
    # ⊕ 18 Nov 2026 (Organisation pupil walk): at 390 px shared/lean.css's overflow-wrap:anywhere
    # split long words in reveal-table cells with no hyphen ("Carbohydra|tes"). On KS4 pages only
    # (lean.css is shared with KS3), hyphenate at a real break point first; a word with none
    # still wraps rather than overflowing.
    # (The comment re-stamps the file: the first stamp's URL was cached at the edge with the
    # previous bytes by a live check that ran before the deploy landed.)
    table = ("\n/* KS4 lean reveal tables: hyphenate long words (Organisation walk, 18 Nov 2026) */"
             "\nhtml .lean-table thead th, html .lean-table tbody th, html .lean-table .lean-cell "
             "{ overflow-wrap: break-word; -webkit-hyphens: auto; hyphens: auto; }\n")
    return batch_4.EXTRA_CSS + table   # + the line-input placeholder rule the Steps and Cfifa blocks need


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
        unit = _UNITS.get((d["subject"], d["topic_id"]), "Energy")
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
    if slug in CHEM_EYEBROW:
        d["eyebrow_spec"] = CHEM_EYEBROW[slug]
    if slug in BIO_EYEBROW:
        d["bio_spec"] = BIO_EYEBROW[slug]
    d.update(batch=B, staged=False, lean=rec, unit=unit,
             block_map=dict(_BLOCK_MAP))
    return d


def _slugs():
    recs = _lean.records()
    return [s for s in SLUGS if s in recs] + sorted(s for s in recs if s not in SLUGS)


LESSONS = [_lesson(s, _lean.records()[s]) for s in _slugs()]
