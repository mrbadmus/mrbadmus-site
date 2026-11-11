# -*- coding: utf-8 -*-
"""KS3 lean records: one module per lesson, merged over the lesson by build_units().

    ks3_data/lean/<slug with underscores>.py   exports LESSON (docs/lessons/LEAN-RECORD.md)

`apply(lesson)` runs AFTER start_here.apply() in ks3_data.build_units(). A lesson
with no record is returned untouched, so it is byte-identical.

What a record changes (all at build time, on a COPY: nothing here mutates the
authored LESSON, which export_ks3_questions.py reads for the database mirror):

    core        replaced by the lean blocks (start, words, knowledge, fact, try,
                the existing ladder, deeper)
    rail        three stops: Start here, Key knowledge, Practice
    stretch     emptied (Dive deeper replaces it)
    big_question  removed from the page; kept as meta_description for search
    ladder      options' feedback and stems overlaid from the record. The ladder's
                questions, options and answers are never touched.

Every other field stays (vocabulary, covers, misconceptions, figures, activities,
key_note...) so the data-reading gates and the flashcards are unaffected.
"""
import copy
import importlib
import pkgutil

_RECORDS = None


def records():
    """{slug: LESSON}. Discovered by module, keyed by the record's own slug."""
    global _RECORDS
    if _RECORDS is None:
        found = {}
        for m in sorted(m.name for m in pkgutil.iter_modules(__path__)):
            if m.startswith("_"):
                continue
            mod = importlib.import_module("%s.%s" % (__name__, m))
            rec = getattr(mod, "LESSON", None)
            if rec is None:
                continue
            if rec["slug"] in found:
                raise ValueError("ks3_data.lean: two records for %r" % rec["slug"])
            if m != rec["slug"].replace("-", "_"):
                raise ValueError("ks3_data.lean: %s.py holds the record for %r; the file "
                                 "must be named %s.py" % (m, rec["slug"],
                                                          rec["slug"].replace("-", "_")))
            validate(rec)
            found[rec["slug"]] = rec
        _RECORDS = found
    return _RECORDS


def validate(rec):
    where = "ks3_data.lean[%r]" % rec.get("slug")
    st = rec.get("start") or {}
    if len(st.get("options") or []) != 2 or st.get("answer") not in (0, 1):
        raise ValueError("%s: start needs exactly two options and answer 0 or 1" % where)
    if not str(st.get("question", "")).endswith("?"):
        raise ValueError("%s: start.question must be a question" % where)
    for key in ("words", "knowledge", "key_fact", "deeper"):
        if not rec.get(key):
            raise ValueError("%s: %s is missing" % (where, key))
    for c in rec["knowledge"] + rec["deeper"]:
        if c.get("kind") not in ("card", "reveal"):
            raise ValueError("%s: unknown item kind %r" % (where, c.get("kind")))


RAIL = [
    {"anchor": "s-hook", "short": "START", "label": "Start here", "done_when": "committed"},
    {"anchor": "s-knowledge", "short": "KNOW", "label": "Key knowledge",
     "done_when": "lean_opened"},
    {"anchor": "s-ladder", "short": "PRACTICE", "label": "Practice",
     "done_when": "ladder_complete"},
]

CORE = [
    {"type": "lean-start", "anchor": "s-hook"},
    {"type": "lean-words", "anchor": "s-words"},
    {"type": "lean-knowledge", "anchor": "s-knowledge"},
    {"type": "lean-fact", "anchor": "s-fact"},
    {"type": "lean-try"},
    {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
    {"type": "lean-deeper", "anchor": "s-deeper"},
]


def _ladder(lesson, rec):
    """The ladder as the lean page shows it: a COPY with feedback and stems
    overlaid. The authored ladder (and so the database mirror) is untouched."""
    lad = copy.deepcopy(lesson.get("ladder") or {})
    for rung, fb in (rec.get("ladder_feedback") or {}).items():
        q = lad.get(rung)
        if not q or not q.get("options"):
            raise ValueError("lean[%s]: ladder_feedback names rung %r, which has no options"
                             % (rec["slug"], rung))
        q["feedback"] = dict(fb)
    for rung, stem in (rec.get("ladder_stem") or {}).items():
        if rung not in lad:
            raise ValueError("lean[%s]: ladder_stem names unknown rung %r" % (rec["slug"], rung))
        lad[rung]["q"] = stem
    return lad


def apply(lesson):
    rec = records().get(lesson.get("slug"))
    if rec is None:
        return lesson
    lesson = dict(lesson)
    if lesson.get("big_question") and not lesson.get("meta_description"):
        lesson["meta_description"] = lesson["big_question"]
    lesson.pop("big_question", None)
    lesson["core"] = copy.deepcopy(CORE)
    lesson["rail"] = copy.deepcopy(RAIL)
    lesson["stretch"] = []
    lesson["ladder"] = _ladder(lesson, rec)
    lesson["lean"] = rec
    return lesson
