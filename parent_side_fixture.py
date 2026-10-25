"""parent_side_fixture.py — offline payloads for the parent-side rebuild
(25 Oct 2026, docs/b2c/parent-side-plan.md).

The shapes are the API CONTRACT in that plan (§ "API contract"), built so
consumer_dash_fixture.py's stub can answer the five reads the new pages make:

  GET /api/consumer/family/home
  GET /api/consumer/children/:id/activity      (topics, keeps_wrong, work_items[].answers)
  GET /api/consumer/children/:id/past-work
  GET /api/consumer/family/past-work
  GET /api/consumer/child/activity             (the signed-in child's own)

Every state the pages must word is here on purpose, so the drive and the
contrast sweep reach it: a right / wrong / two-attempt multiple choice, a
partly-marked calculation, a written answer at 1/4, a 6-mark answer with an
AQA level and a next step, an UNMARKED written answer and a SELF-CHECKED one,
measured and unmeasured times, a work item that saves no answers
(`tracked: false`), a not-done item from earlier in the week, today's item and
one that opens later, a repeatedly-wrong question and topic, tutor questions
with the safe HTML the backend makes (a <sub>, bold, a list).

Fixture data only — nothing here ships to a page.
"""
from __future__ import annotations

import copy

WEEK = "2026-09-28"          # consumer_dash_fixture KIDS[0].week_strip.from
TODAY = "2026-09-30"         # …and its `today` index 2 (Wednesday)
PREV1 = "2026-09-21"
PREV2 = "2026-09-14"

KP = {
    "cells": ("kp-cells", "Cell structure"),
    "mag": ("kp-mag", "Calculating magnification"),
    "diff": ("kp-diff", "Diffusion"),
    "org": ("kp-org", "Levels of organisation"),
    "melt": ("kp-melt", "Changes of state"),
    "part": ("kp-part", "The particle model"),
}

_n = [0]


def _id(prefix):
    _n[0] += 1
    return "%s-%03d" % (prefix, _n[0])


def mcq(item, kp, q, said, correct, ok, at, attempt=1, secs=None, qid=None):
    return {
        "id": _id("ans"), "work_item_id": item, "surface": "lesson",
        "question_id": qid or ("q:" + q[:24].lower().replace(" ", "-")),
        "knowledge_point": {"id": KP[kp][0], "label": KP[kp][1]},
        "question_text": q, "answer": said, "correct_answer": correct, "kind": "choice",
        "outcome": "correct" if ok else "wrong", "is_correct": ok,
        "marks_scored": 1 if ok else 0, "marks_available": 1,
        "points_hit": None, "points_total": None, "feedback": None,
        "mark_level": None, "mark_next_step": None, "marked_by": "key",
        "mark_state": "scored", "unmarked_reason": None, "attempt_no": attempt,
        "time_spent_seconds": secs, "answered_at": at,
    }


def written(item, kp, q, said, correct, got, of, at, level=None, nxt=None, feedback=None,
            secs=None, marked_by="ai", reason=None, kind="written"):
    unmarked = marked_by == "unmarked"
    if unmarked:
        outcome = "unmarked"
    elif got >= of:
        outcome = "correct"
    elif got <= 0:
        outcome = "wrong"
    else:
        outcome = "partial"
    return {
        "id": _id("ans"), "work_item_id": item, "surface": "lesson",
        "question_id": "q:" + q[:24].lower().replace(" ", "-"),
        "knowledge_point": {"id": KP[kp][0], "label": KP[kp][1]},
        "question_text": q, "answer": said, "correct_answer": correct, "kind": kind,
        "outcome": outcome, "is_correct": None,
        "marks_scored": None if unmarked else got, "marks_available": of,
        "points_hit": None, "points_total": None,
        "feedback": None if unmarked else feedback,
        "mark_level": None if unmarked else level,
        "mark_next_step": None if unmarked else nxt,
        "marked_by": marked_by, "unmarked_reason": reason if unmarked else None,
        "mark_state": ("self_checked" if reason == "self_checked" else "unmarked") if unmarked else "scored",
        "attempt_no": 1, "time_spent_seconds": secs, "answered_at": at,
    }


def summary(answers, session_secs=None):
    t = {"answered": 0, "questions": 0, "correct": 0, "partial": 0, "wrong": 0,
         "unmarked": 0, "self_checked": 0}
    seen = set()
    ms = ma = 0
    timed = untimed = 0
    secs = 0
    for a in answers:
        t["answered"] += 1
        seen.add(a["question_id"])
        t[a["outcome"]] += 1
        if a.get("unmarked_reason") == "self_checked":
            t["self_checked"] += 1
        if a["marked_by"] != "unmarked" and a["marks_scored"] is not None:
            ms += a["marks_scored"]
            ma += a["marks_available"]
        if a["time_spent_seconds"] is not None:
            timed += 1
            secs += a["time_spent_seconds"]
        else:
            untimed += 1
    t["questions"] = len(seen)
    if session_secs is not None:
        secs, timed, untimed = session_secs, len(answers), 0
    t.update({"marks_scored": ms, "marks_available": ma, "marked": t["answered"] - t["unmarked"],
              "time_seconds": (secs if timed else None),
              "time_complete": bool(answers) and untimed == 0,
              "answers_timed": timed, "answers_untimed": untimed,
              "sessions_timed": 1 if session_secs is not None else 0})
    return t


def item(iid, kind, title, subject, week, day, status, answers=None, done_at=None,
         tracked=True, reason=None, session=None, sub=None):
    answers = answers or []
    return {
        "id": iid, "kind": kind, "title": title, "sub": sub, "subject": subject,
        "week_start": week, "scheduled_for": day, "status": status,
        "done_at": done_at, "removed": False,
        "tracked": tracked, "untracked_reason": reason,
        "summary": summary(answers, session), "answers": answers,
    }


def ada_items():
    _n[0] = 0
    T = "T17:%02d:00Z"
    w1 = "ada-w1"   # Mon: lesson, done, every marking state
    l1 = [
        mcq(w1, "cells", "Which part of a cell controls what enters and leaves?",
            "Cell membrane", "Cell membrane", True, "2026-09-28" + T % 2, secs=21),
        mcq(w1, "cells", "Where does aerobic respiration happen?",
            "Nucleus", "Mitochondria", False, "2026-09-28" + T % 3, secs=34,
            qid="q:resp-site"),
        mcq(w1, "cells", "Where does aerobic respiration happen?",
            "Mitochondria", "Mitochondria", True, "2026-09-28" + T % 4, attempt=2, secs=12,
            qid="q:resp-site"),
        written(w1, "mag", "A cell is 0.02 mm wide. Its image is 4 mm wide. Calculate the magnification.",
                "4 ÷ 0.02 = 20", "× 200 (4 ÷ 0.02)", 2, 3, "2026-09-28" + T % 6,
                feedback="Right method; the division slipped by a factor of ten.", secs=142,
                kind="numeric"),
        written(w1, "org", "Explain why a muscle cell has many mitochondria. (4 marks)",
                "It needs lots of energy.", "Muscle cells contract, which needs energy from respiration; "
                "mitochondria are where aerobic respiration happens, so more mitochondria release more energy.",
                1, 4, "2026-09-28" + T % 9,
                feedback="One mark for 'needs energy'. Link it to respiration happening in mitochondria.",
                secs=None),
        written(w1, "org", "Describe how you would prepare a slide of onion cells and view them. (6 marks)",
                "Peel the skin, put it on a slide with iodine, cover slip, look at it on low power then high power.",
                "Thin layer of epidermis; drop of water or iodine stain; lower the cover slip at an angle to "
                "avoid bubbles; start on the lowest power objective, focus with the coarse then fine knob.",
                0, 6, "2026-09-28" + T % 14, marked_by="unmarked", reason="marker_unavailable"),
    ]
    w2 = "ada-w2"   # Tue: practice, done, measured as one session
    p2 = []
    qs = [("What is the function of the nucleus?", "Controls the cell", "Controls the cell", True),
          ("Which structure is found in plant cells only?", "Cell wall", "Cell wall", True),
          ("What do ribosomes make?", "Protein", "Protein", True),
          ("What is the unit of magnification?", "mm", "It has no unit", False),
          ("Which cells have no nucleus?", "Prokaryotic cells", "Prokaryotic cells", True),
          ("What does a specialised cell do?", "A particular job", "A particular job", True),
          ("How is a sperm cell adapted?", "Has a tail", "Has a tail", True),
          ("What is magnification?", "How big the cell is", "Image size ÷ real size", False)]
    for i, (q, s, c, ok) in enumerate(qs):
        p2.append(mcq(w2, "mag" if "magnif" in q else "cells", q, s, c, ok,
                      "2026-09-29T16:%02d:00Z" % (10 + i)))
    w3 = "ada-w3"   # Wed: exam question, 6 marks, level 2
    e3 = [written(w3, "part",
                  "Explain why the temperature of ice stays the same while it melts. (6 marks)",
                  "The energy goes into the ice but it does not get hotter because the particles are "
                  "breaking away from each other. When it is all water the temperature goes up again.",
                  "Energy is transferred to the ice; it is used to break the bonds between particles, "
                  "not to raise their kinetic energy, so the temperature stays at 0 °C until all is melted.",
                  3, 6, "2026-09-30T07:40:00Z", level="Level 2",
                  nxt="To reach Level 3: say the energy breaks the bonds between particles rather than "
                      "speeding them up.",
                  feedback="A clear idea that the energy does something other than heat the ice. Name the "
                           "bonds and the kinetic energy to reach the top level.", secs=552)]
    w7 = "ada-w7"   # Mon: done, saves no answers
    w8 = "ada-w8"   # Wed: self-checked written answer only
    s8 = [written(w8, "diff", "Describe what happens to a drop of ink in still water.",
                  "It spreads out slowly until the colour is the same everywhere.",
                  "The particles spread from high to low concentration by diffusion until evenly mixed.",
                  0, 2, "2026-09-30T06:55:00Z", marked_by="unmarked", reason="self_checked", secs=95)]
    this_week = [
        item(w1, "lesson", "Cells and organisation", "Biology", WEEK, "2026-09-28", "done", l1,
             done_at="2026-09-28T17:20:00Z"),
        item(w7, "lesson", "Using a microscope", "Biology", WEEK, "2026-09-28", "done",
             done_at="2026-09-28T18:05:00Z", tracked=False, reason="custom_layout"),
        item("ada-w6", "lesson", "Specialised cells", "Biology", WEEK, "2026-09-28", "set"),
        item(w2, "practice", "Quick questions: cells", "Biology", WEEK, "2026-09-29", "done", p2,
             done_at="2026-09-29T16:20:00Z", session=365, sub="8 questions"),
        item(w3, "exam", "Exam question: Changes of state", "Chemistry", WEEK, "2026-09-30", "done", e3,
             done_at="2026-09-30T07:50:00Z", sub="6 marks"),
        item(w8, "lesson", "Diffusion", "Biology", WEEK, "2026-09-30", "done", s8,
             done_at="2026-09-30T07:00:00Z"),
        item("ada-w4", "lesson", "Osmosis", "Biology", WEEK, "2026-09-30", "set"),
        item("ada-w5", "unit_check", "Unit check: Cells", "Biology", WEEK, "2026-10-04", "set"),
    ]
    v1 = "ada-v1"
    pv1 = [mcq(v1, "melt", "Why does the temperature stay the same while ice melts?",
               "The ice is still cold inside", "The energy is breaking the bonds between particles",
               False, "2026-09-22T16:31:00Z", qid="q:ice-melt"),
           mcq(v1, "part", "In which state are the particles furthest apart?", "Gas", "Gas", True,
               "2026-09-22T16:32:00Z"),
           mcq(v1, "part", "Which state keeps its volume but takes its container's shape?",
               "Liquid", "Liquid", True, "2026-09-22T16:33:00Z")]
    v2 = "ada-v2"
    pv2 = [written(v2, "cells", "Compare a plant cell with an animal cell. (6 marks)",
                   "Both have a nucleus, cytoplasm and membrane and mitochondria. Plant cells also have a "
                   "cell wall, chloroplasts and a permanent vacuole, animal cells do not.",
                   "Shared: nucleus, cytoplasm, membrane, mitochondria, ribosomes. Plant only: cellulose wall, "
                   "chloroplasts, permanent vacuole.", 5, 6, "2026-09-24T17:05:00Z", level="Level 3",
                   feedback="Level 3: every structure named and sorted correctly. Ribosomes would complete it.",
                   secs=410)]
    u1 = "ada-u1"
    pu1 = [mcq(u1, "melt", "Why does the temperature stay the same while ice melts?",
               "The ice is still cold inside", "The energy is breaking the bonds between particles",
               False, "2026-09-15T16:10:00Z", qid="q:ice-melt"),
           mcq(u1, "part", "What happens to particles when a solid is heated?",
               "They vibrate more", "They vibrate more", True, "2026-09-15T16:11:00Z")]
    earlier = [
        item(v1, "practice", "Particle model", "Chemistry", PREV1, "2026-09-22", "done", pv1,
             done_at="2026-09-22T16:35:00Z", session=180, sub="3 questions"),
        item(v2, "exam", "Exam question: Plant and animal cells", "Biology", PREV1, "2026-09-24", "done", pv2,
             done_at="2026-09-24T17:10:00Z", sub="6 marks"),
        item(u1, "practice", "States of matter", "Chemistry", PREV2, "2026-09-15", "done", pu1,
             done_at="2026-09-15T16:12:00Z"),
    ]
    return this_week + earlier


def topics():
    def t(key, subject, status, marked, unmarked, right, wrong, partial, questions, seen):
        return {"id": KP[key][0], "label": KP[key][1], "subject": subject, "key_stage": "KS3",
                "status": status,
                "basis": {"answers": marked + unmarked, "marked": marked, "unmarked": unmarked,
                          "right": right, "wrong": wrong, "partial": partial, "questions": questions},
                "last_seen": seen}
    return [
        t("cells", "Biology", "secure", 12, 0, 11, 1, 0, 10, "2026-09-29T16:16:00Z"),
        t("part", "Chemistry", "shaky", 5, 0, 4, 0, 1, 5, "2026-09-30T07:40:00Z"),
        t("org", "Biology", "not_yet", 1, 1, 0, 0, 1, 2, "2026-09-28T17:14:00Z"),
        t("mag", "Biology", "not_yet", 3, 0, 0, 2, 1, 3, "2026-09-29T16:17:00Z"),
        t("melt", "Chemistry", "not_yet", 2, 0, 0, 2, 0, 1, "2026-09-22T16:31:00Z"),
        t("diff", "Biology", "shaky", 0, 1, 0, 0, 0, 1, "2026-09-30T06:55:00Z"),
    ]


def keeps_wrong(items):
    allans = [a for it in items for a in it["answers"]]
    ice = [a for a in allans if a["question_id"] == "q:ice-melt"]
    mag = [a for a in allans if a["knowledge_point"]["id"] == "kp-mag" and a["outcome"] == "wrong"]
    return [
        {"kind": "question", "id": "q:ice-melt",
         "label": "Why does the temperature stay the same while ice melts?",
         "subject": "Chemistry", "wrong_count": len(ice), "weeks_span": 2, "answers": ice},
        {"kind": "topic", "id": "kp-mag", "label": "Calculating magnification",
         "subject": "Biology", "wrong_count": len(mag), "weeks_span": 1, "answers": mag},
    ]


TUTOR = [
    {"question": "why does CO2 make the limewater cloudy",
     "question_html": "why does CO2 make the limewater cloudy",
     "reply": "Carbon dioxide reacts with limewater ...",
     "reply_html": "Carbon dioxide (CO<sub>2</sub>) reacts with the calcium hydroxide in limewater to make "
                   "<strong>calcium carbonate</strong>, which does not dissolve:<ul><li>the solid is tiny "
                   "white specks</li><li>the specks scatter light, so the liquid looks cloudy</li></ul>",
     "has_image": False, "page_path": "/ks3/biology/cells/cells-and-organisation.html",
     "page_title": "Cells and organisation", "lesson_slug": "cells-and-organisation", "key_stage": "KS3",
     "answered": True, "asked_at": "2026-09-28T16:42:00Z", "replied_at": "2026-09-28T16:42:09Z"},
    {"question": "so do plant cells respire too?", "question_html": "so do plant cells respire too?",
     "reply": "Yes ...", "reply_html": "Yes. Plant cells have mitochondria and respire all the time, day "
                                       "and night. Photosynthesis happens as well, in the light.",
     "has_image": False, "page_path": "/ks3/biology/cells/cells-and-organisation.html",
     "page_title": "Cells and organisation", "lesson_slug": "cells-and-organisation", "key_stage": "KS3",
     "answered": True, "asked_at": "2026-09-28T16:51:00Z", "replied_at": "2026-09-28T16:51:06Z"},
    {"question": "is melting a chemical change", "question_html": "is melting a chemical change",
     "reply": None, "reply_html": None,
     "has_image": False, "page_path": "/ks3/chemistry/particles/changes-of-state.html",
     "page_title": "Changes of state", "lesson_slug": "changes-of-state", "key_stage": "KS3",
     "answered": False, "asked_at": "2026-09-22T17:10:00Z", "replied_at": None},
]


def activity(child_id="kid-ada", first_name="Ada", year=8, child_view=False):
    if child_id != "kid-ada":
        return {"child": {"id": child_id, "first_name": first_name, "year_group": year,
                          "key_stage": "KS4" if year >= 10 else "KS3",
                          "username": "ben.saturn", "last_active_at": None},
                "range": {"from": None, "to": TODAY, "all_time": True},
                "work_items": [], "other_answers": [], "knowledge_points": [],
                "topics": [], "keeps_wrong": [], "tutor_questions": []}
    items = ada_items()
    out = {
        "child": {"id": child_id, "first_name": first_name, "year_group": year, "key_stage": "KS3",
                  "username": "ada.comet", "last_active_at": "2026-09-30T07:50:00Z"},
        "range": {"from": None, "to": TODAY, "all_time": True},
        "work_items": items, "other_answers": [], "knowledge_points": [],
        "topics": topics(), "keeps_wrong": keeps_wrong(items),
        "tutor_questions": copy.deepcopy(TUTOR),
    }
    return out


def _frac(items):
    s = a = 0
    for it in items:
        s += it["summary"]["marks_scored"]
        a += it["summary"]["marks_available"]
    return (s / a) if a else None


WEEK_LABELS = {WEEK: "28 September", PREV1: "21 September", PREV2: "14 September"}


def _monday(ymd):
    import datetime
    d = datetime.date.fromisoformat(ymd)
    return (d - datetime.timedelta(days=d.weekday())).isoformat()


def past_work(child_ids=("kid-ada",), names=None, sort="newest", subject=""):
    """GET /past-work's shape, as the backend's buildPastWork sends it:
    done items grouped by the Mon–Sun week of the day each was DONE, items
    carrying `score` and `done_day` but not their answers."""
    names = names or {"kid-ada": "Ada", "kid-ben": "Ben"}
    weeks = {}
    for cid in child_ids:
        if cid != "kid-ada":
            continue
        for it in ada_items():
            if it["status"] != "done" or (subject and it["subject"] != subject):
                continue
            day = it["done_at"][:10]
            sm = it["summary"]
            x = {k: it[k] for k in ("id", "kind", "title", "sub", "subject", "scheduled_for", "done_at",
                                    "summary", "tracked", "untracked_reason")}
            x["done_day"] = day
            x["score"] = {"marked_scored": sm["marks_scored"], "marked_available": sm["marks_available"],
                          "marked": sm["answered"] - sm["unmarked"], "unmarked": sm["unmarked"],
                          "fraction": (sm["marks_scored"] / sm["marks_available"]) if sm["marks_available"] else None}
            x["status"] = "done"
            x["child"] = {"id": cid, "first_name": names.get(cid, cid)}
            weeks.setdefault(_monday(day), []).append(x)
    groups = []
    for ws, its in weeks.items():
        its.sort(key=lambda i: i["done_at"], reverse=True)
        s = sum(i["score"]["marked_scored"] for i in its)
        a = sum(i["score"]["marked_available"] for i in its)
        groups.append({"week_start": ws, "label": WEEK_LABELS.get(ws, ws), "done": len(its),
                       "untracked": sum(1 for i in its if not i["tracked"]),
                       "score": {"marked_scored": s, "marked_available": a,
                                 "unmarked": sum(i["score"]["unmarked"] for i in its),
                                 "fraction": (s / a) if a else None},
                       "items": its})
    if sort in ("highest", "lowest"):
        scored = [g for g in groups if g["score"]["fraction"] is not None]
        rest = [g for g in groups if g["score"]["fraction"] is None]
        scored.sort(key=lambda g: g["score"]["fraction"], reverse=(sort == "highest"))
        groups = scored + rest
    else:
        groups.sort(key=lambda g: g["week_start"], reverse=(sort != "oldest"))
    return {"sort": sort, "subject": subject or None, "week": None,
            "total_items": sum(len(g["items"]) for g in groups), "weeks": groups}


def family_home(kids):
    """GET /family/home's shape for consumer_dash_fixture's KIDS."""
    children = []
    att_all = []
    for k in kids:
        cid = k["id"]
        if cid == "kid-ada":
            days = []
            states = ["done", "done", "due_today", "set", "none", "none", "set"]
            for i, d in enumerate(["2026-09-28", "2026-09-29", "2026-09-30", "2026-10-01",
                                   "2026-10-02", "2026-10-03", "2026-10-04"]):
                days.append({"date": d, "weekday": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][i],
                             "state": states[i]})
            att = [{"kind": "keeps_wrong", "topic": "Why does the temperature stay the same while ice melts?",
                    "wrong_count": 2, "weeks": 2}]
            ch = {"id": cid, "first_name": k["first_name"], "year_group": k["year_group"], "key_stage": "KS3",
                  "username": k["username"], "last_active_at": "2026-09-30T07:50:00Z",
                  "days_inactive": 0, "never_logged_in": False,
                  "week": {"week_start": WEEK, "label": "28 September", "done": 5, "total": 8, "days": days},
                  "most_recent": {"work_item_id": "ada-w3", "title": "Exam question: Changes of state",
                                  "kind": "exam", "subject": "Chemistry", "done_at": "2026-09-30T07:50:00Z",
                                  "score": {"marked_scored": 3, "marked_available": 6, "unmarked": 0}},
                  "attention": att}
        else:
            ch = {"id": cid, "first_name": k["first_name"], "year_group": k["year_group"],
                  "key_stage": "KS4" if k["year_group"] >= 10 else "KS3",
                  "username": k["username"], "last_active_at": None, "days_inactive": None,
                  "never_logged_in": True,
                  "week": {"week_start": WEEK, "label": "28 September", "done": 0, "total": 0,
                           "days": [{"date": d, "weekday": w, "state": "none"} for d, w in zip(
                               ["2026-09-28", "2026-09-29", "2026-09-30", "2026-10-01", "2026-10-02",
                                "2026-10-03", "2026-10-04"], ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])]},
                  "most_recent": None,
                  "attention": [{"kind": "never_logged_in", "set_count": 0, "first_due": None}]}
            att = ch["attention"]
        children.append(ch)
        for a in att:
            b = dict(a)
            b["child"] = {"id": cid, "first_name": k["first_name"]}
            att_all.append(b)
    return {"ok": True, "today": TODAY, "parent": {"first_name": "Sam"},
            "children": children, "attention_all": att_all, "plan": None}
