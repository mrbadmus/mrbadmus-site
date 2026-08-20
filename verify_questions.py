#!/usr/bin/env python3
"""verify_questions.py — the gate on the KS3 question bank (MRB-269).

A gate that has never been seen to fail is not a gate. Every check below has
been demonstrated failing by deliberate mutation. Run it as part of the build:

    python3 verify_questions.py

Exit 0 = clean. Exit 1 = at least one finding, printed with the id and file that
carries it. It never "warns" — a question bank that a teacher sets as homework
is either valid or it is not.

── The nine checks ──────────────────────────────────────────────────────

1. A lesson with fewer than twelve questions, or a band with fewer than four.
2. A question with other than exactly four options, or other than exactly one
   correct.
3. A wrong option with no ``why``, or an empty one.
4. A duplicate ``id`` anywhere in the bank.
5. A ``figure`` naming something that does not exist in that lesson, **or that exists
   but cannot render** — a figure at ``status: "needed"`` has no artwork drawn and one
   at ``status: "retired"`` has been removed, so pointing a question at either shows the
   student an empty slot. Membership in ``figures[]`` is not enough; the figure has to be
   a picture a student can actually look at.
6. A question whose ``text`` matches a ladder rung's question text.
7. A question attached to a lesson slug not in ``structure.py``.
8. The composition ruling itself, exercised against the real bank: a full week
   fills from its own lessons, a thin week fills from earlier ones nearest
   first, week one is allowed to be short, a thin week that is NOT week one
   raises, and the same inputs always give the same fifteen.

9. **A recorded attempt that cannot be resolved back to the question it came
   from.** Every row `shared/ks3.js` writes to `quiz_question_attempts` claims
   to be about a question. This check is the proof that the claim can be
   redeemed — offline, against the authored content and the built page, before
   a single student generates a row.

   ⚠️ THE PROMPT FOR THIS CHECK SAID "back to a BANK question" AND THAT IS THE
   WRONG TARGET. Checked rather than assumed: check 6 immediately above exists
   to guarantee the bank NEVER restates a ladder rung, so the two sets are
   disjoint BY GATE. A ladder attempt can no more resolve to a bank question
   than a bank question can appear on a ladder. Two capture paths, two homes:

     ladder rungs  → /api/quiz-score → quiz_question_attempts
     bank questions → /api/assignment-submit → assignment_question_attempts

   So the resolvable target for a `quiz_question_attempts` row is the LADDER,
   and the identity is (subtopic, rung) — subtopic on the quiz_scores row, rung
   in its own column since 20260819122539. What check 9 gates is that this pair
   round-trips, and that the page can still emit the parts it needs to.

Checks 1–3 and 5–6 are per-lesson; 4 is global; 7 gates the file's own identity;
8 gates :func:`ks3_data.question_bank.compose_assignment`; 9 gates the ladder
attempt round trip against the BUILT tree.
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


# A figure a student can actually see. `needed` means commissioned but not drawn;
# `retired` means removed (e.g. MRB-257 decision 5, where the dial replaced the
# timeline). Both are still declared in `figures[]`, which is why membership alone is
# not the test.
RENDERABLE_FIGURE_STATUS = {"final", "drawn", "drafted"}


def _ladder_texts(lesson):
    """Every rung question in a lesson's ladder, normalised."""
    out = set()
    for rung in (lesson.get("ladder") or {}).values():
        if isinstance(rung, dict) and rung.get("q"):
            out.add(_normalise(rung["q"]))
    return out



# ── check 9 · the ladder attempt round trip ────────────────────────────────
#
# The served tree, not ./ks3 — Cloudflare serves from mrbadmus_site/, so this is
# the markup a student's browser actually runs against.
KS3_OUT = os.path.join("mrbadmus_site", "ks3")

# What `shared/ks3.js` reads out of a rung, named here so a rename on either
# side is a FAILURE rather than a silent null column. Every one of these is
# load-bearing for a field in quiz_question_attempts.
# ⚠️ `ks3-rung[^"]*` and NOT `ks3-rung`. A SELF-marked rung ships
# `class="ks3-rung ks3-rung-self"`, so an exact-class match finds the two
# marked rungs and silently misses the two written ones — which are precisely
# the rungs MRB-269 phase 4a is about. Caught by this check reporting `explain`
# and `produce` missing on all 70 lessons at once: a finding that uniform is a
# finding about the checker.
# `ks3-rung` then a QUOTE or a SPACE — never `ks3-rung[^"]*`, which also
# matches the `ks3-rungs` CONTAINER the four rungs sit inside.
_RUNG_OPEN = r'<div class="ks3-rung(?: [^"]*)?"'
_RUNG_RE = re.compile(
    _RUNG_OPEN + r'([^>]*)>(.*?)(?=' + _RUNG_OPEN + r'|</div></div></section>|\Z)',
    re.S)
_ATTR_RE = re.compile(r'data-rung="([^"]*)"')
_MODE_RE = re.compile(r'data-mode="([^"]*)"')
_Q_RE = re.compile(r'<p class="ks3-rung-q">(.*?)</p>', re.S)
_OPT_RE = re.compile(r'<button type="button" class="ks3-option"(.*?)</button>', re.S)
_MARK_RE = re.compile(r'<span class="ks3-opt-mark"[^>]*>([^<]*)</span>')
_LABEL_RE = re.compile(r'<span class="ks3-opt-label">(.*?)</span>', re.S)


def _text(html):
    """Visible text of a fragment: tags out, entities in, whitespace collapsed."""
    import html as _h
    return re.sub(r"\s+", " ", _h.unescape(re.sub(r"<[^>]+>", "", html or ""))).strip()


def _built_page(unit_code, lesson):
    """The built HTML for a lesson, or None if the page is not on disk."""
    for root, _dirs, files in os.walk(KS3_OUT):
        if (lesson["slug"] + ".html") in files:
            return open(os.path.join(root, lesson["slug"] + ".html"),
                        encoding="utf-8").read()
    return None


def check_attempt_round_trip(lessons, fail):
    """Every attempt the page can write must resolve back to an authored rung.

    A row in `quiz_question_attempts` says "this student answered this
    question". Its identity is (subtopic, rung): the lesson slug on the
    quiz_scores row, and the rung column. This check proves, offline and before
    any student generates a row, that the pair redeems — and that the page can
    still emit the parts the row is made of.

    Four ways it can fail, and all four have been demonstrated:

      a. the built page emits a `data-rung` the authored ladder does not have,
         so the row names a question nobody can find;
      b. the authored ladder has a rung the built page never emits, so a rung
         is unanswerable and its column would never be written;
      c. the question text on the page is not the authored question, so
         `question_text` is a snapshot of something the content does not
         contain — the resolver's own cross-check;
      d. a lettered option no longer exposes its letter and its label as
         SEPARATE elements, which is the exact shape MRB-270 phase 5 needs to
         fill selected_option_letter without guessing a prefix length.
    """
    for (unit_code, slug), lesson in sorted(lessons.items()):
        ladder = lesson.get("ladder") or {}
        authored = {k: v for k, v in ladder.items()
                    if isinstance(v, dict) and v.get("q")}
        if not authored:
            continue
        where = "%s/%s" % (unit_code, slug)

        html = _built_page(unit_code, lesson)
        if html is None:
            fail(9, where,
                 "authored lesson with a ladder and NO BUILT PAGE in %s — "
                 "run build_ks3.py; a check that skips a missing page is a "
                 "check that passes when the build is broken" % KS3_OUT)
            continue

        emitted = {}
        for attrs, body in _RUNG_RE.findall(html):
            m = _ATTR_RE.search(attrs)
            if not m:
                fail(9, where,
                     "a .ks3-rung on the built page carries no `data-rung`. "
                     "That attribute IS the rung column; without it the row "
                     "cannot say which question it is about")
                continue
            emitted[m.group(1)] = (attrs, body)

        # (a) every emitted rung resolves to an authored one
        for key in sorted(set(emitted) - set(authored)):
            fail(9, "%s [%s]" % (where, key),
                 "the page emits rung %r and the authored ladder has no such "
                 "rung. An attempt row carrying it could never be resolved "
                 "back to a question — authored rungs are %s"
                 % (key, sorted(authored)))

        # (b) every authored rung is actually emitted
        for key in sorted(set(authored) - set(emitted)):
            fail(9, "%s [%s]" % (where, key),
                 "the authored ladder declares rung %r and the built page "
                 "never emits it, so it can be answered by nobody and its "
                 "column would never be written" % key)

        for key in sorted(set(authored) & set(emitted)):
            attrs, body = emitted[key]
            at = "%s [%s]" % (where, key)

            # (c) the page's question IS the authored question
            qm = _Q_RE.search(body)
            if not qm:
                fail(9, at,
                     "the rung has no `.ks3-rung-q` on the built page. That "
                     "element is where shared/ks3.js reads `question_text`; "
                     "without it the row records an empty question")
                continue
            if _normalise(_text(qm.group(1))) != _normalise(authored[key]["q"]):
                fail(9, at,
                     "the question on the page is not the authored question, "
                     "so `question_text` would snapshot text the content does "
                     "not contain.\n               page:     %r\n"
                     "               authored: %r"
                     % (_text(qm.group(1))[:90], authored[key]["q"][:90]))

            # (d) letter and label are separate elements on a lettered rung
            mm = _MODE_RE.search(attrs)
            mode = mm.group(1) if mm else ""
            options = _OPT_RE.findall(body)
            if mode == "self" or not options:
                continue
            for n, opt in enumerate(options):
                if not _MARK_RE.search(opt):
                    fail(9, at,
                         "option %d has no `.ks3-opt-mark`, so its LETTER "
                         "cannot be read separately and "
                         "selected_option_letter would be null. This is the "
                         "shape MRB-270 phase 5 opened the column for" % n)
                if not _LABEL_RE.search(opt):
                    fail(9, at,
                         "option %d has no `.ks3-opt-label`, so the option "
                         "TEXT can only be read off the button as a whole — "
                         "which is how \"ANothing at all\" reached the column "
                         "in the first place (MRB-239)" % n)


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

        figures = {f.get("id"): f.get("status")
                   for f in (lesson.get("figures") or [])}
        figure_ids = set(figures)
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
            if figure is not None:
                if figure not in figure_ids:
                    fail(5, at, "figure %r is not in lesson %r (has: %s)"
                         % (figure, slug, sorted(figure_ids) or "none"))
                elif figures[figure] not in RENDERABLE_FIGURE_STATUS:
                    fail(5, at, "figure %r is %r — there is no artwork to show, so the "
                                "question would point the student at an empty slot"
                         % (figure, figures[figure]))

            # ── check 6 — must not restate a ladder rung ────────────────
            if _normalise(q.get("text")) in ladder:
                fail(6, at, "question text restates a ladder rung — the bank "
                            "is additional depth, not a copy")

    # ── check 9 — the ladder attempt round trip ─────────────────────────
    check_attempt_round_trip(lessons, fail)

    findings.extend(_check_composition())
    return findings


def _check_composition():
    """Check 8 — Mide's final composition ruling, against the real bank.

    ⊕ The ruling this gates (20 Aug 2026) SUPERSEDED the 13 + 2 retrieval
    split: the current week supplies everything it can, the rest fills from
    earlier lessons nearest first, and week one may legally be short.

    Lesson keys are read out of the bank rather than typed, so the check
    cannot rot when a lesson is renamed.
    """
    out = []

    def fail(where, message):
        out.append((8, where, message))

    bank = qb.bank_by_lesson()
    # Six real lessons from one unit, in lesson order — enough for a four-lesson
    # week plus two earlier ones.
    keys = [(r["unit"], r["lesson"]) for r in qb.load_bank()
            if r["unit"] == "B1"]
    if len(keys) < 6:
        fail("compose_assignment", "expected >= 6 B1 lessons to exercise the "
                                   "ruling, found %d" % len(keys))
        return out

    def ids(qs):
        return [q["id"] for q in qs]

    # (a) Four current-week lessons fill fifteen from the week alone.
    got = qb.compose_assignment(keys[2:6], earlier_lessons=keys[:2],
                                bank=bank)
    if len(got) != qb.ASSIGNMENT_SIZE:
        fail("compose_assignment/full-week",
             "four current lessons gave %d questions, expected %d"
             % (len(got), qb.ASSIGNMENT_SIZE))
    from_week = {q["id"] for q in got} & {
        q["id"] for k in keys[2:6] for q in bank.get(k, [])}
    if len(from_week) != len(got):
        fail("compose_assignment/full-week",
             "four current lessons hold 16 standard questions, so all %d "
             "should come from the week itself; %d did"
             % (len(got), len(from_week)))

    # (b) A one-lesson week fills the rest from earlier lessons, nearest first.
    got = qb.compose_assignment([keys[5]], earlier_lessons=list(reversed(keys[:5])),
                                bank=bank)
    if len(got) != qb.ASSIGNMENT_SIZE:
        fail("compose_assignment/thin-week",
             "one current lesson plus five earlier gave %d, expected %d"
             % (len(got), qb.ASSIGNMENT_SIZE))
    own = [q["id"] for q in bank.get(keys[5], []) if q.get("band") == "standard"]
    if ids(got)[:len(own)] != own:
        fail("compose_assignment/thin-week",
             "the current week's own questions must come first; got %s"
             % ids(got)[:len(own)])
    nearest = [q["id"] for q in bank.get(keys[4], []) if q.get("band") == "standard"]
    if ids(got)[len(own):len(own) + len(nearest)] != nearest:
        fail("compose_assignment/nearest-first",
             "the fill must take the NEAREST earlier lesson next; expected %s, "
             "got %s" % (nearest, ids(got)[len(own):len(own) + len(nearest)]))

    # (c) Week one — nothing earlier — is allowed to be short.
    try:
        short = qb.compose_assignment([keys[0]], bank=bank)
    except qb.ShortAssignment as exc:
        fail("compose_assignment/week-one",
             "week one must be allowed to ship short, but it raised: %s" % exc)
    else:
        if len(short) != qb.PER_BAND:
            fail("compose_assignment/week-one",
                 "one lesson holds %d standard questions; week one returned %d"
                 % (qb.PER_BAND, len(short)))

    # (d) The same thinness OUTSIDE week one must raise.
    try:
        qb.compose_assignment([keys[5]], earlier_lessons=[keys[4]], bank=bank)
    except qb.ShortAssignment:
        pass
    else:
        fail("compose_assignment/short-raises",
             "two lessons hold 8 standard questions and this is not week one, "
             "so it must raise ShortAssignment rather than ship short")

    # (e) Deterministic — a teacher previewing sees what the class will get.
    a = qb.compose_assignment(keys[2:6], earlier_lessons=keys[:2], bank=bank)
    b = qb.compose_assignment(keys[2:6], earlier_lessons=keys[:2], bank=bank)
    if ids(a) != ids(b):
        fail("compose_assignment/deterministic",
             "two identical calls gave different questions")
    if len(set(ids(a))) != len(ids(a)):
        fail("compose_assignment/duplicates",
             "an assignment repeated a question: %s" % ids(a))

    return out


def main():
    findings = verify()
    n_lessons = len(qb.load_bank())
    n_questions = len(qb.all_questions())

    if not findings:
        print("verify_questions: OK — %d lessons, %d questions, all nine "
              "checks clean." % (n_lessons, n_questions))
        return 0

    print("verify_questions: %d FINDING(S) across %d lessons, %d questions\n"
          % (len(findings), n_lessons, n_questions))
    # ⊕ MRB-270 — `str(f[0])`. Check 8 reports under a NAME ("compose_assignment/
    # deterministic") while checks 1–7 and 9 report under an int, and sorting a
    # list holding both raised TypeError: '<' not supported between 'str' and
    # 'int'. A red gate then printed a traceback instead of its findings —
    # still non-zero, so it never passed wrongly, but it told you nothing at
    # the moment you most needed telling. Only reachable when a numbered check
    # and check 8 fail in the same run, which is why it survived this long.
    for check, where, message in sorted(findings, key=lambda f: (str(f[0]), f[1])):
        print("  [check %s] %s\n             %s" % (check, where, message))
    print("\nA red gate means no commit and no push for that unit.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
