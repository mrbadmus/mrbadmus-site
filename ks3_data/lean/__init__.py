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
    big_question  kept on the lesson; left off the lean page itself (build_ks3.lesson_page)
    misconceptions  elicited_by / confronted_by point at the Easy mistakes card
    figures     the record's own figures are added
    ladder      options' feedback and stems overlaid from the record. The ladder's
                questions, options and answers are never touched.
    ks4_becomes, safety_note   replaced by the record's own wording when it gives one
                (None drops the line), so a lean page's endmatter meets the standard too.

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
    # exact-text edits to a self-marked rung's success list (render only; the authored list is
    # untouched). Every [old, new] pair must find its old text exactly once, or the build stops.
    for old, new in rec.get("ladder_ticks") or []:
        hits = [(rung, i) for rung, q in lad.items() for i, t in enumerate(q.get("success") or []) if t == old]
        if len(hits) != 1:
            raise ValueError("lean[%s]: ladder_ticks old text %r found %d times in the ladder's success lists"
                             % (rec["slug"], old[:70], len(hits)))
        rung, i = hits[0]
        lad[rung]["success"][i] = new
    for rung, stem in (rec.get("ladder_stem") or {}).items():
        if rung not in lad:
            raise ValueError("lean[%s]: ladder_stem names unknown rung %r" % (rec["slug"], rung))
        lad[rung]["q"] = stem
    return lad


def _misconceptions(lesson, rec):
    """The misconceptions as the lean page can honour them: a COPY whose `elicited_by`
    and `confronted_by` name a real element on the lean page (the Easy mistakes card, or
    the Key knowledge section when a lesson has none). Ids and statements are kept."""
    import lean_blocks
    has_card = any(lean_blocks.card_id(c) == lean_blocks.EASY_MISTAKES_ID
                   for c in rec["knowledge"] + rec["deeper"] if c.get("kind") == "card")
    target = lean_blocks.EASY_MISTAKES_ID if has_card else "s-knowledge"
    out = []
    for m in lesson.get("misconceptions") or []:
        m = dict(m)
        if m.get("confronted_by"):
            m["confronted_by"] = target
        if m.get("elicited_by"):
            m["elicited_by"] = target
        out.append(m)
    return out


def apply(lesson):
    rec = records().get(lesson.get("slug"))
    if rec is None:
        return lesson
    lesson = dict(lesson)
    # `big_question` stays on the lesson (the browse pages print it as a card blurb);
    # build_ks3.lesson_page leaves it off a lean lesson's own page.
    lesson["core"] = copy.deepcopy(CORE)
    if rec.get("try"):          # `lean-try` is in core only when a record names a simulation
        at = next(i for i, b in enumerate(lesson["core"]) if b["type"] == "lean-fact") + 1
        lesson["core"].insert(at, {"type": "lean-try"})
    lesson["rail"] = copy.deepcopy(RAIL)
    lesson["stretch"] = []
    lesson["ladder"] = _ladder(lesson, rec)
    lesson["misconceptions"] = _misconceptions(lesson, rec)
    # render-only rewording of two endmatter lines; a None value drops the line
    for key in ("ks4_becomes", "safety_note"):
        if key in rec:
            if rec[key]:
                lesson[key] = rec[key]
            else:
                lesson.pop(key, None)
    # the lean page carries a convention note only when its record sets one
    if rec.get("convention_note"):
        lesson["convention_note"] = rec["convention_note"]
    else:
        lesson.pop("convention_note", None)
    # the record's own figures join the lesson's (a drawn figure needs its art registered)
    have = {f["id"] for f in lesson.get("figures") or []}
    lesson["figures"] = list(lesson.get("figures") or []) + [
        copy.deepcopy(f) for f in rec.get("figures") or [] if f["id"] not in have]
    lesson["lean"] = rec
    return lesson
