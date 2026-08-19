#!/usr/bin/env python3
"""verify_questions.py — the gate on the KS3 question bank (MRB-269).

A gate that has never been seen to fail is not a gate. Every check below has
been demonstrated failing by deliberate mutation. Run it as part of the build:

    python3 verify_questions.py

Exit 0 = clean. Exit 1 = at least one finding, printed with the id and file that
carries it. It never "warns" — a question bank that a teacher sets as homework
is either valid or it is not.

── The seven checks ─────────────────────────────────────────────────────

1. A lesson with fewer than twelve questions, or a band with fewer than four.
2. A question with other than exactly four options, or other than exactly one
   correct.
3. A wrong option with no ``why``, or an empty one.
4. A duplicate ``id`` anywhere in the bank.
5. A ``figure`` naming something that does not exist in that lesson.
6. A question whose ``text`` matches a ladder rung's question text.
7. A question attached to a lesson slug not in ``structure.py``.

Checks 1–3 and 5–6 are per-lesson; 4 is global; 7 gates the file's own identity.
A few structural preconditions (a band that is not one of the three, an id that
does not match its own lesson and band) are folded into the checks they belong
to, because a question that fails them cannot be selected correctly either.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ks3_data
from ks3_data import question_bank as qb


def _normalise(text):
    """Loose text identity: case, punctuation and whitespace do not count.

    Check 6 exists to stop the bank restating a ladder rung. Restating it with
    a comma moved is the same duplication, so the comparison ignores anything
    that is not a letter or a digit.
    """
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def _ladder_texts(lesson):
    """Every rung question in a lesson's ladder, normalised."""
    out = set()
    for rung in (lesson.get("ladder") or {}).values():
        if isinstance(rung, dict) and rung.get("q"):
            out.add(_normalise(rung["q"]))
    return out


def verify():
    findings = []

    def fail(check, where, message):
        findings.append((check, where, message))

    # The authored lessons, keyed the way the bank keys them.
    lessons = {}
    known_slugs = set()
    for unit in ks3_data.build_units():
        for lesson in unit["lessons"]:
            known_slugs.add(lesson["slug"])
            if lesson.get("authored"):
                lessons[(unit["code"], lesson["slug"])] = lesson

    seen_ids = {}

    for record in qb.load_bank():
        unit = record["unit"]
        slug = record["lesson"]
        number = record["number"]
        where = record["module"]
        questions = record["questions"]

        # ── check 7 — the file's own identity ───────────────────────────
        if slug not in known_slugs:
            fail(7, where,
                 "lesson slug %r is not in structure.py — the topic map is the "
                 "single record of scope (§7)" % slug)
            continue
        lesson = lessons.get((unit, slug))
        if lesson is None:
            fail(7, where,
                 "no authored lesson %r in unit %r — a question must be "
                 "answerable from the lesson it belongs to" % (slug, unit))
            continue

        figure_ids = {f.get("id") for f in (lesson.get("figures") or [])}
        ladder = _ladder_texts(lesson)

        # ── check 1 — twelve per lesson, four per band ──────────────────
        if len(questions) != qb.QUESTIONS_PER_LESSON:
            fail(1, where, "%d questions, expected %d"
                 % (len(questions), qb.QUESTIONS_PER_LESSON))
        for band in qb.BANDS:
            n = sum(1 for q in questions if q.get("band") == band)
            if n != qb.PER_BAND:
                fail(1, where, "band %r has %d questions, expected %d"
                     % (band, n, qb.PER_BAND))

        for q in questions:
            qid = q.get("id", "<no id>")
            at = "%s [%s]" % (where, qid)

            band = q.get("band")
            if band not in qb.BANDS:
                fail(1, at, "band %r is not one of %s" % (band, list(qb.BANDS)))

            # ── check 4 — duplicate ids anywhere in the bank ────────────
            if qid in seen_ids:
                fail(4, at, "duplicate id — already used by %s" % seen_ids[qid])
            else:
                seen_ids[qid] = where

            # id must name its own lesson and band, or selection and
            # `assignment_questions.source_ref` disagree about what was set.
            if band in qb.BANDS and number is not None:
                expected = "%s-%02d-%s" % (unit.lower(), number,
                                           qb.BAND_LETTER[band])
                if not str(qid).startswith(expected):
                    fail(4, at, "id does not match its lesson and band — "
                                "expected the form %s%s" % (expected, "NN"))

            if not (q.get("text") or "").strip():
                fail(2, at, "empty question text")

            # ── check 2 — exactly four options, exactly one correct ─────
            options = q.get("options") or []
            if len(options) != 4:
                fail(2, at, "%d options, expected exactly 4" % len(options))
            correct = [o for o in options if o.get("correct")]
            if len(correct) != 1:
                fail(2, at, "%d options marked correct, expected exactly 1"
                     % len(correct))

            # ── check 3 — every wrong option carries a real `why` ───────
            for i, opt in enumerate(options):
                if not (opt.get("text") or "").strip():
                    fail(2, at, "option %d has empty text" % i)
                if opt.get("correct"):
                    continue
                if not (opt.get("why") or "").strip():
                    fail(3, at, "wrong option %d has no `why` — a distractor "
                                "without a correction teaches nothing" % i)

            # ── check 5 — figure must already exist in the lesson ───────
            figure = q.get("figure")
            if figure is not None and figure not in figure_ids:
                fail(5, at, "figure %r is not in lesson %r (has: %s)"
                     % (figure, slug, sorted(figure_ids) or "none"))

            # ── check 6 — must not restate a ladder rung ────────────────
            if _normalise(q.get("text")) in ladder:
                fail(6, at, "question text restates a ladder rung — the bank "
                            "is additional depth, not a copy")

    return findings


def main():
    findings = verify()
    n_lessons = len(qb.load_bank())
    n_questions = len(qb.all_questions())

    if not findings:
        print("verify_questions: OK — %d lessons, %d questions, all seven "
              "checks clean." % (n_lessons, n_questions))
        return 0

    print("verify_questions: %d FINDING(S) across %d lessons, %d questions\n"
          % (len(findings), n_lessons, n_questions))
    for check, where, message in sorted(findings, key=lambda f: (f[0], f[1])):
        print("  [check %d] %s\n             %s" % (check, where, message))
    print("\nA red gate means no commit and no push for that unit.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
