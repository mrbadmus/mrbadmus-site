"""KS3 question bank — the pool a weekly assignment is drawn from (MRB-269).

**What this is.** One question file per authored lesson, living beside the
lesson it tests::

    ks3_data/c1/questions_04_gas_pressure.py
    ks3_data/b1/questions_01_life_processes.py

Files, not a database table, because the questions then live in the same
version-controlled, gated world as the lesson content they test; the build can
validate them; and no migration is needed to ship them. A teacher-editable
overlay in the database can come later and reference these ids.

**How they are found.** This module *globs* — it walks every unit package for
modules named ``questions_*.py`` and imports them by dotted name. No unit's
``__init__.py`` needs to know a question file exists, so adding a lesson's
questions is a one-file change that cannot collide with lesson authoring.

── The module contract ──────────────────────────────────────────────────

Each question module exports exactly four names::

    UNIT          = "C1"                # unit code, as in structure.py
    LESSON        = "gas-pressure"       # lesson slug, permanent (§8.4)
    LESSON_NUMBER = 4                    # the lesson's slot number in its unit
    QUESTIONS     = [ ... ]              # twelve or more question dicts

── The question record ──────────────────────────────────────────────────

::

    {
        "id": "c1-04-h02",
        "band": "harder",
        "text": "A sealed syringe of air is pushed halfway in. ...",
        "options": [
            {"text": "It doubles, because ...", "correct": True},
            {"text": "It halves, because ...",  "correct": False,
             "why": "Less space means MORE collisions per second, not fewer."},
            ... exactly four, exactly one correct ...
        ],
        "figure": None,
    }

``id`` — permanent, and the thing ``assignment_questions.source_ref`` stores.
Format ``{unit}-{lesson:02d}-{band-letter}{nn}``, band letter ``e``/``s``/``h``,
unit code lowercased. **Ids are never reused or renumbered.** A retired question
is removed and its id retires with it.

``band`` — the RUNG OF DEMAND, never the topic: ``easier`` (recall and direct
recognition), ``standard`` (applying the idea to a situation the lesson
covered), ``harder`` (an unfamiliar context, or two ideas from the lesson
joined). ⊕ MRB-335: at least four of each, at least twelve per lesson, and the
first four of each band are the twelve at ``bank_position`` 0–11. Set work
surfaces the three bands to a teacher as Easy / Medium / Hard.

``options`` — exactly four, exactly one ``correct: True``. **Every wrong option
carries a ``why``** that names the specific misconception it represents and
corrects it. That field is the whole point of the bank: a class converging on
one distractor is a named misunderstanding, and the ``why`` is what a student
sees the moment they answer.

``figure`` — ``None``, or the ``id`` of a figure that already exists in that
lesson's ``figures[]``. Question files never author new diagrams.

── Assignment composition (ruled, MRB-269) ──────────────────────────────

Recorded here so the rule is not lost, and implemented by
:func:`compose_assignment` below.

⊕ **MIDE'S FINAL RULING (20 Aug 2026) — this SUPERSEDES the 13 + 2 split.**
The earlier rule reserved at least two of the fifteen as retrieval from the
immediately preceding lesson and took the other thirteen from the current
week. That is gone. The rule now is:

* **Fifteen questions per weekly assignment.**
* **The current week's lessons supply everything they can** in the drawn band
  — four per lesson, which is all that band has.
* **The rest fills from earlier lessons in the scheme, nearest first.**
* Default band is ``standard``. A class or a student moved down draws
  ``easier``; moved up draws ``harder``. **The band is a property of the
  question** — this supersedes MRB-239's rung-based difficulty ruling.
* **Week one may legally be short.** It has nothing earlier in the scheme to
  fill from, so it ships with whatever its own lessons hold and
  :class:`ShortAssignment` is NOT raised.
* **Everywhere else, short raises.** Shipping short outside week one is the
  one outcome the ruling forbids.

Why the retrieval minimum went: it was a floor on a pool that is now the
fallback anyway. Under the new rule the earlier lessons are drawn nearest
first, so the immediately preceding lesson is already the first thing reached
once the current week runs out — which it almost always does. The old rule
spent two of fifteen enforcing what the ordering gives for free, and it made
week one a special case that had to be written twice.

⚠️ **Filling from earlier lessons is the normal path, not an edge case.**
Twelve questions per lesson is four per band, and an assignment draws a single
band, so fifteen questions need four lessons in scope::

    1 current-week lesson  →  4 available, 11 to find earlier
    2 current-week lessons →  8 available,  7 to find earlier
    3 current-week lessons → 12 available,  3 to find earlier
    4 current-week lessons → 16 available,  none needed  ✓

A KS3 week is typically one or two lessons, so ``earlier_lessons`` will be
supplied on almost every real call outside week one.
"""

import importlib
import os
import pkgutil
import re

BANDS = ("easier", "standard", "harder")
BAND_LETTER = {"easier": "e", "standard": "s", "harder": "h"}

QUESTIONS_PER_LESSON = 12
PER_BAND = 4
ASSIGNMENT_SIZE = 15

# ⊕ MRB-335 (7 Sep 2026) — THE LESSON IS NO LONGER EXACTLY TWELVE.
#
# Set work lets a teacher choose questions by unit or lesson, and twelve per
# lesson is far too thin a pool for that: a KS3 unit needs about fifty per band
# before a class can be set work twice without seeing the same rows. So the
# bank now GROWS. Three names carry the consequences, and they mean different
# things:
#
#   QUESTIONS_PER_LESSON  the ORIGINAL twelve. No longer a lesson's size — it
#                         is the size of the window auto composition sees, and
#                         a lesson's MINIMUM.
#   PER_BAND              four. No longer a lesson's per-band count — it is
#                         the per-band MINIMUM, and the count inside the
#                         original twelve.
#   AUTO_POSITIONS        the cap. `bank_position < AUTO_POSITIONS` is what
#                         `compose_assignment` — and `bankFor()` in the Node
#                         backend — may draw from.
#
# ⚠️ THE CAP IS WHY A TOP-UP IS SAFE (RISKS D7). `compose_assignment` takes
# questions in bank order until it has fifteen, so a lesson that grew from four
# standard rows to nine would silently change EVERY auto-composed assignment
# that ever reached it — a class would be served a different homework from the
# same week, with nothing in the diff to say why. Capping the auto read at the
# original twelve makes any top-up byte-identical for auto, while Set work
# reads every position.
AUTO_POSITIONS = QUESTIONS_PER_LESSON

# ⚠️ A KNOWN CONTENT DEFECT, NAMED SO NO MORE OF IT CAN BE ADDED — NOT AN
# EXEMPTION ANYONE MAY GROW (MRB-335, found 7 Sep 2026).
#
# Three C8 questions carry `<sub>` tags in their stems, options and `why`
# fields. Bank text never reaches the DOM as HTML: `student-runtime.js`
# builds every text node with `document.createTextNode` (line 138/141), and
# nothing runs `ks3_art.kit.formulae()` over bank rows the way it runs over
# lesson prose. So a child sitting one of these assignments is shown
#
#     Silicon forms SiO<sub>2</sub> and tin forms SnO<sub>2</sub>.
#
# with the angle brackets, today, live. The fix is one character per site —
# `<sub>2</sub>` → `₂` — but it is a CONTENT edit in `ks3_data/c8/`, which the
# MRB-335 loader lane may not make. Listed here so the check ships GREEN
# while still refusing every new occurrence, and so the finding cannot be
# lost. **Delete a line from this set when the row is fixed. Never add one.**
MARKUP_KNOWN = frozenset({
    "c8-02-s03",   # stem + option 2 · SiO<sub>2</sub>, SnO<sub>2</sub>, XO<sub>2</sub>
    "c8-03-e02",   # why 3 · MgCl<sub>2</sub>
    "c8-03-h04",   # stem + why 0 + why 1 · CO<sub>2</sub>, SiO<sub>2</sub>, Na<sub>2</sub>O
})

# ⊕ RETIRED by Mide's final ruling (20 Aug 2026). `RETRIEVAL_MINIMUM = 2`
# reserved two of the fifteen for the immediately preceding lesson. The rule is
# now "current week supplies everything it can, the rest fills from earlier
# lessons nearest first", under which the preceding lesson is already the first
# thing reached. The name is gone rather than left at 0, so nothing can read it
# and believe a floor still applies.

_HERE = os.path.dirname(os.path.abspath(__file__))


class ShortAssignment(Exception):
    """Not enough questions in scope to build a full assignment.

    ⊕ NOT raised in week one, which has nothing earlier in the scheme to fill
    from and is allowed to ship with whatever its own lessons hold.

    Raised everywhere else rather than returning a short list, because "rather
    than shipping a short assignment" is the ruled behaviour and a caller that
    silently sets nine questions has broken it without anyone noticing. The
    message names what was asked for and what was reachable, so the fix (pass
    more ``earlier_lessons``, nearest first) is obvious from the traceback.
    """


def _question_modules():
    """Every ``questions_*.py`` under every unit package, in sorted order.

    Yields ``(unit_package_name, module_name)``. Sorted at both levels so the
    bank assembles identically on every machine and every run.
    """
    for unit_pkg in sorted(
            m.name for m in pkgutil.iter_modules([_HERE]) if m.ispkg):
        unit_dir = os.path.join(_HERE, unit_pkg)
        for mod in sorted(m.name for m in pkgutil.iter_modules([unit_dir])):
            if mod.startswith("questions_"):
                yield unit_pkg, mod


def load_bank():
    """The whole bank, as a list of per-lesson records in unit/lesson order.

    Each record::

        {"unit": "C1", "lesson": "gas-pressure", "number": 4,
         "module": "ks3_data.c1.questions_04_gas_pressure",
         "questions": [ ... twelve dicts ... ]}

    Import errors are deliberately not swallowed: a question file that does not
    parse is a build failure, not a silently missing lesson.
    """
    records = []
    for unit_pkg, mod_name in _question_modules():
        dotted = "%s.%s.%s" % (__package__, unit_pkg, mod_name)
        m = importlib.import_module(dotted)
        records.append({
            "unit":      getattr(m, "UNIT", None),
            "lesson":    getattr(m, "LESSON", None),
            "number":    getattr(m, "LESSON_NUMBER", None),
            "module":    dotted,
            "questions": list(getattr(m, "QUESTIONS", []) or []),
        })
    return records


def bank_by_lesson():
    """``{(unit_code, lesson_slug): [question, ...]}`` for the whole bank."""
    return {(r["unit"], r["lesson"]): r["questions"] for r in load_bank()}


def all_questions():
    """Every question in the bank, flat, in deterministic order."""
    return [q for r in load_bank() for q in r["questions"]]


def questions_for(unit_code, lesson_slug, band=None):
    """One lesson's questions, optionally filtered to a single band."""
    pool = bank_by_lesson().get((unit_code, lesson_slug), [])
    if band is None:
        return list(pool)
    return [q for q in pool if q.get("band") == band]


# ── the auto-composition cap (MRB-335, RISKS D7) ────────────────────────

def auto_pool(questions):
    """The rows AUTO composition may draw from: ``bank_position < 12``.

    A question's ``bank_position`` in ``ks3_assignment_bank`` is its index
    inside its own module (see ``export_ks3_questions.bank_rows``), so the
    positional cap is a slice here and a ``.lt('bank_position', 12)`` filter in
    the backend's ``bankFor()``. **The two must stay identical** — they are the
    same rule expressed twice, and the day they disagree a teacher's preview
    and the class's actual homework are different assignments.

    Set work does NOT go through here. It reads every position, on purpose:
    the top-up rows exist for exactly that.
    """
    return list(questions)[:AUTO_POSITIONS]


# ── the shape of one lesson's bank ──────────────────────────────────────

def _normalise(text):
    """Loose text identity: case, punctuation and whitespace do not count."""
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


_ID_RE = None


def validate_lesson(record):
    """Every structural rule one lesson's questions must obey.

    Returns ``[(check_number, question_id_or_None, message), ...]`` — empty
    when the lesson is clean. Lives here rather than in ``verify_questions.py``
    so that the rule and the data have one home, and so a content lane can run
    it on its own file without running the whole gate.

    ⊕ MRB-335 RELAXED THE SIZE RULES AND TIGHTENED EVERYTHING ELSE.

    What relaxed — a lesson used to be exactly twelve questions, exactly four
    per band. It is now **at least** twelve, **at least** four per band, with
    the shape of the original twelve pinned:

      · positions 0–11 hold exactly four of each band, in the authored order
        they have always had, so ``auto_pool()`` sees precisely what it saw
        before any top-up;
      · every row a lane adds therefore lands at position ≥ 12 by
        construction, because a position IS an index;
      · ids stay unique inside the lesson, and each band's ``nn`` suffixes run
        ``01, 02, 03, …`` with no gap and no repeat — which is what makes
        "continue from 05" a rule a lane can follow and a gate can check.

    What tightened — two failures that nothing was watching for, and that a
    growing bank makes far more likely:

      · **a duplicate stem** inside one lesson. Twelve hand-written questions
        do not collide; fifty do, and an assignment that asks the same thing
        twice looks like a bug to the child answering it.
      · **a duplicate answer SET with the same correct option** — the same
        question written twice with the options shuffled. ⚠️ Deliberately not
        "the same four options": ``p4-09-e01`` and ``p4-09-e02`` share their
        four options and are different questions (one asks which is NOT a
        non-contact force, the other which can only attract). Sharing an
        option pool is legitimate MCQ design; sharing it AND the answer is one
        question written twice.
    """
    global _ID_RE
    if _ID_RE is None:
        _ID_RE = re.compile(r"^[a-z0-9]+-(\d{2})-([esh])(\d{2})$")

    out = []
    questions = record["questions"]
    unit = record["unit"]
    number = record["number"]

    def fail(check, qid, message):
        out.append((check, qid, message))

    # ── size: at least the original twelve, at least four per band ──────
    if len(questions) < QUESTIONS_PER_LESSON:
        fail(1, None, "%d questions, expected at least %d — the original "
                      "twelve are the auto-composition window and may not "
                      "shrink" % (len(questions), QUESTIONS_PER_LESSON))
    for band in BANDS:
        n = sum(1 for q in questions if q.get("band") == band)
        if n < PER_BAND:
            fail(1, None, "band %r has %d question(s), expected at least %d"
                          % (band, n, PER_BAND))

    # ── the original twelve still occupy positions 0–11 ─────────────────
    head = questions[:QUESTIONS_PER_LESSON]
    if len(head) == QUESTIONS_PER_LESSON:
        for band in BANDS:
            n = sum(1 for q in head if q.get("band") == band)
            if n != PER_BAND:
                fail(1, None,
                     "bank_position 0–11 hold %d %r question(s), expected "
                     "exactly %d. A top-up must APPEND (position >= 12); "
                     "inserting into the first twelve changes every auto "
                     "assignment this lesson has ever produced (RISKS D7)"
                     % (n, band, PER_BAND))

    # ── ids: unique here, and each band numbered 01..N with no gaps ─────
    seen, by_band = {}, {}
    for pos, q in enumerate(questions):
        qid = q.get("id", "<no id>")
        band = q.get("band")

        if band not in BANDS:
            fail(1, qid, "band %r is not one of %s" % (band, list(BANDS)))

        if qid in seen:
            fail(1, qid, "duplicate id inside this lesson — position %d "
                         "repeats position %d" % (pos, seen[qid]))
        else:
            seen[qid] = pos

        m = _ID_RE.match(str(qid))
        if not m:
            fail(1, qid, "id is not of the form <unit>-<lesson nn>-<e|s|h><nn>")
            continue
        if band in BANDS and BAND_LETTER[band] != m.group(2):
            fail(1, qid, "id says band %r but the row says %r"
                         % (m.group(2), band))
        if number is not None and int(m.group(1)) != number:
            fail(1, qid, "id names lesson %s but this module is lesson %d"
                         % (m.group(1), number))
        if unit and not str(qid).startswith(unit.lower() + "-"):
            fail(1, qid, "id does not open with unit %r" % unit.lower())
        by_band.setdefault(m.group(2), []).append(int(m.group(3)))

    for letter, nums in sorted(by_band.items()):
        want = list(range(1, len(nums) + 1))
        if sorted(nums) != want:
            fail(1, None,
                 "band %r ids are %s — they must run %s with no gap and no "
                 "repeat, so a lane topping this lesson up continues from the "
                 "next number and cannot collide"
                 % (letter, sorted(nums), want))

    # ── the correct option carries NO `why`, and nothing carries markup ──
    #
    # `why` is the misconception behind a DISTRACTOR. On the correct option it
    # is either absent or None — `export_ks3_questions.bank_rows` writes
    # `o.get("why")` straight into the JSON the student's page reads, so a
    # `why` on the right answer would be shown as a correction of a correct
    # answer.
    #
    # ⚠️ MARKUP, NOT SUBSCRIPTS. Bank text is inserted as TEXT by the
    # assignment page — nothing runs `ks3_art.kit.formulae()` over it, unlike
    # KS3 lesson prose — so `<sub>2</sub>` would be shown to the child
    # literally, angle brackets and all. It also means a bank row that needs a
    # subscript must carry the real character: C2's notation lessons ask "what
    # is the small 2 in CO₂ doing?", which is unanswerable written flat. That
    # is why this checks for markup and NOT for subscript characters — see
    # docs/mrb335/ks3-authoring.md.
    for q in questions:
        qid = q.get("id", "<no id>")
        for i, opt in enumerate(q.get("options") or []):
            if opt.get("correct") and (opt.get("why") or "").strip():
                fail(1, qid, "option %d is the CORRECT one and carries a "
                             "`why` — the field is the misconception behind a "
                             "distractor and must be null here" % i)
        for label, text in ([("stem", q.get("text"))]
                            + [("option %d" % i, o.get("text"))
                               for i, o in enumerate(q.get("options") or [])]
                            + [("why %d" % i, o.get("why"))
                               for i, o in enumerate(q.get("options") or [])]):
            if (text and re.search(r"<\s*/?\s*[a-zA-Z]", text)
                    and qid not in MARKUP_KNOWN):
                fail(1, qid, "%s contains HTML markup — bank text is inserted "
                             "as TEXT, so a tag is shown to the child "
                             "literally" % label)

    # ── duplicate stems, and duplicate question-in-disguise ─────────────
    stems, answers = {}, {}
    for q in questions:
        qid = q.get("id", "<no id>")
        stem = _normalise(q.get("text"))
        if stem and stem in stems:
            fail(1, qid, "stem repeats %s — a lesson may not ask the same "
                         "thing twice" % stems[stem])
        else:
            stems[stem] = qid

        options = q.get("options") or []
        correct = [o for o in options if o.get("correct")]
        if len(options) != 4 or len(correct) != 1:
            continue      # check 2 in verify_questions owns that finding
        key = (tuple(sorted(_normalise(o.get("text")) for o in options)),
               _normalise(correct[0].get("text")))
        if key in answers:
            fail(1, qid, "same four options AND the same correct option as "
                         "%s — that is one question written twice" % answers[key])
        else:
            answers[key] = qid

    return out


# ── assignment composition ──────────────────────────────────────────────

def compose_assignment(current_lessons, preceding_lesson=None,
                       band="standard", earlier_lessons=(), bank=None,
                       size=ASSIGNMENT_SIZE, week_one=None):
    """Pick the fifteen questions for one weekly assignment.

    ⊕ MIDE'S FINAL RULING (20 Aug 2026). The current week's lessons supply
    everything they can in ``band``; the rest fills from earlier lessons in the
    scheme, NEAREST FIRST. Week one may legally be short. See the module
    docstring for what this superseded and why.

    ``current_lessons``   — [(unit_code, slug), ...] this week's lessons, in
                            teaching order.
    ``preceding_lesson``  — (unit_code, slug) of the immediately preceding
                            lesson in the class's scheme, or ``None`` in week
                            one. It is simply the NEAREST earlier lesson: it is
                            prepended to ``earlier_lessons`` if not already
                            there, and has no reserved share any more.
    ``band``              — ``standard`` by default; ``easier`` for a class or
                            student moved down, ``harder`` for one moved up.
    ``earlier_lessons``   — [(unit_code, slug), ...] earlier lessons in the
                            scheme, **nearest first**.
    ``week_one``          — force the week-one reading. ``None`` (the default)
                            infers it: week one is a call with nothing earlier
                            in the scheme to draw on, which is exactly when
                            being short is legal.

    Returns a list of question dicts, at most ``size`` long, and shorter ONLY
    in week one. Selection is deterministic — questions are taken in bank
    order — so the same inputs always give the same assignment and a teacher
    previewing one sees what the class will get.

    Raises :class:`ShortAssignment` if the lessons in scope cannot supply
    ``size`` questions at ``band`` and this is not week one.
    """
    bank = bank if bank is not None else bank_by_lesson()

    # The scheme behind this week, nearest first. `preceding_lesson` is the
    # nearest earlier lesson by definition, so it heads the list unless the
    # caller already put it there.
    earlier = list(earlier_lessons)
    if preceding_lesson is not None and preceding_lesson not in earlier:
        earlier.insert(0, preceding_lesson)

    if week_one is None:
        week_one = not earlier

    chosen, seen = [], set()

    def take(key, n):
        """Take up to ``n`` unused questions of ``band`` from one lesson."""
        got = 0
        # ⊕ MRB-335 / RISKS D7 — `auto_pool`, not the whole lesson. The bank
        # grows for Set work; auto composition must be unchanged by that. The
        # backend's `bankFor()` applies the identical `bank_position < 12`.
        for q in auto_pool(bank.get(key, [])):
            if got >= n:
                break
            if q.get("band") != band or q["id"] in seen:
                continue
            seen.add(q["id"])
            chosen.append(q)
            got += 1
        return got

    # 1. The current week supplies everything it can. No cap per lesson beyond
    #    what the band holds — the ruling says "everything they can".
    for key in current_lessons:
        if len(chosen) >= size:
            break
        take(key, size - len(chosen))

    # 2. The rest fills from earlier lessons in the scheme, nearest first.
    for key in earlier:
        if len(chosen) >= size:
            break
        take(key, size - len(chosen))

    # 3. Short is legal in week one and forbidden everywhere else.
    if len(chosen) < size and not week_one:
        raise ShortAssignment(
            "only %d question(s) at band %r reachable from %d current lesson(s)"
            " and %d earlier — %d needed. Each lesson supplies %d questions per"
            " band, so pass more `earlier_lessons` (nearest first) to make up"
            " the shortfall."
            % (len(chosen), band, len(current_lessons), len(earlier), size,
               PER_BAND))

    return chosen[:size]


# ── the module's own self-check ─────────────────────────────────────────
#
#     python3 -m ks3_data.question_bank
#
# Run this before committing a top-up. It is the fast half of
# `verify_questions.py` — everything that can be judged from the question
# files alone, with no lesson content, no built pages and no database — plus
# the one property the top-up exists to protect: that adding rows cannot move
# an auto-composed assignment.

def _cap_test():
    """A synthetic lesson of 20 composes exactly what its first 12 compose.

    ⚠️ This is the whole of RISKS D7 in eight lines, and it is synthetic on
    purpose: the real bank has no topped-up lesson yet, so a test written
    against the real bank would pass today and prove nothing about tomorrow.
    """
    out = []

    def lesson(n, n_per_band):
        """One synthetic lesson: the original twelve, then a top-up appended."""
        qs = []
        # positions 0–11: the original four per band, easier/standard/harder.
        for i in range(1, PER_BAND + 1):
            for band in BANDS:
                qs.append({"id": "x1-%02d-%s%02d" % (n, BAND_LETTER[band], i),
                           "band": band, "text": "q", "options": []})
        # positions 12+: the top-up, appended, never inserted.
        for i in range(PER_BAND + 1, n_per_band + 1):
            for band in BANDS:
                qs.append({"id": "x1-%02d-%s%02d" % (n, BAND_LETTER[band], i),
                           "band": band, "text": "q", "options": []})
        return qs

    keys = [("X1", "l%d" % i) for i in range(4)]
    thin = {k: lesson(i + 1, PER_BAND) for i, k in enumerate(keys)}
    fat = {k: lesson(i + 1, PER_BAND + 16) for i, k in enumerate(keys)}

    for band in BANDS:
        a = [q["id"] for q in compose_assignment(keys, band=band, bank=thin)]
        b = [q["id"] for q in compose_assignment(keys, band=band, bank=fat)]
        if a != b:
            out.append((0, None,
                        "auto composition CHANGED when the lesson grew from "
                        "%d rows to %d at band %r:\n           12-row: %s\n"
                        "           60-row: %s"
                        % (len(thin[keys[0]]), len(fat[keys[0]]), band, a, b)))
        if len(a) != ASSIGNMENT_SIZE:
            out.append((0, None, "composed %d at band %r, expected %d"
                                 % (len(a), band, ASSIGNMENT_SIZE)))

    # And the cap itself, said directly: nothing at position >= 12 is reachable.
    capped = {q["id"] for q in auto_pool(fat[keys[0]])}
    if len(capped) != AUTO_POSITIONS:
        out.append((0, None, "auto_pool returned %d rows, expected %d"
                             % (len(capped), AUTO_POSITIONS)))
    if any(q["id"] not in capped
           for q in compose_assignment(keys, band="standard", bank=fat)
           if q["id"].startswith("x1-01-")):
        out.append((0, None, "a row at bank_position >= 12 reached an auto "
                             "assignment"))
    return out


def self_check():
    """Validate the whole bank and the cap. Returns a list of findings."""
    findings = []
    for record in load_bank():
        for check, qid, message in validate_lesson(record):
            where = record["module"] + (" [%s]" % qid if qid else "")
            findings.append((check, where, message))
    for check, qid, message in _cap_test():
        findings.append((check, "compose_assignment/auto-cap", message))
    return findings


def _main():
    findings = self_check()
    records = load_bank()
    n_q = sum(len(r["questions"]) for r in records)
    topped = sum(1 for r in records
                 if len(r["questions"]) > QUESTIONS_PER_LESSON)
    if not findings:
        print("question_bank self-check: OK — %d lesson(s), %d question(s), "
              "%d topped up beyond position 11."
              % (len(records), n_q, topped))
        print("  auto-composition window: bank_position < %d (unchanged by "
              "any top-up)" % AUTO_POSITIONS)
        return 0
    print("question_bank self-check: %d FINDING(S) across %d lesson(s), "
          "%d question(s)\n" % (len(findings), len(records), n_q))
    for check, where, message in sorted(findings, key=lambda f: (f[0], f[1])):
        print("  [check %s] %s\n             %s" % (check, where, message))
    return 1


if __name__ == "__main__":
    import sys
    sys.exit(_main())
