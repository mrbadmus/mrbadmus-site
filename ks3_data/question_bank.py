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
    QUESTIONS     = [ ... ]              # twelve question dicts

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

``band`` — ``easier`` (recall and direct recognition), ``standard`` (applying
the idea to a situation the lesson covered), ``harder`` (an unfamiliar context,
or two ideas from the lesson joined). Four of each, twelve per lesson.

``options`` — exactly four, exactly one ``correct: True``. **Every wrong option
carries a ``why``** that names the specific misconception it represents and
corrects it. That field is the whole point of the bank: a class converging on
one distractor is a named misunderstanding, and the ``why`` is what a student
sees the moment they answer.

``figure`` — ``None``, or the ``id`` of a figure that already exists in that
lesson's ``figures[]``. Question files never author new diagrams.

── Assignment composition (ruled, MRB-269) ──────────────────────────────

Recorded here so the rule is not lost, and implemented by
:func:`compose_assignment` below:

* **Fifteen questions per weekly assignment.**
* **At least two are retrieval** from the immediately preceding lesson in that
  class's scheme of work.
* The remaining thirteen come from the current week's lessons.
* Default band is ``standard``. A class or a student moved down draws
  ``easier``; moved up draws ``harder``. **The band is a property of the
  question** — this supersedes MRB-239's rung-based difficulty ruling.
* Week one of a scheme has no preceding lesson: it takes all fifteen from its
  own lessons.
* A lesson that cannot supply its share falls back to the nearest earlier
  lesson in the same subject rather than shipping a short assignment.
"""

import importlib
import os
import pkgutil

BANDS = ("easier", "standard", "harder")
BAND_LETTER = {"easier": "e", "standard": "s", "harder": "h"}

QUESTIONS_PER_LESSON = 12
PER_BAND = 4
ASSIGNMENT_SIZE = 15
RETRIEVAL_MINIMUM = 2

_HERE = os.path.dirname(os.path.abspath(__file__))


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


# ── assignment composition ──────────────────────────────────────────────

def compose_assignment(current_lessons, preceding_lesson=None,
                       band="standard", earlier_lessons=(), bank=None,
                       size=ASSIGNMENT_SIZE, retrieval=RETRIEVAL_MINIMUM):
    """Pick the fifteen questions for one weekly assignment.

    ``current_lessons``   — [(unit_code, slug), ...] this week's lessons, in
                            teaching order.
    ``preceding_lesson``  — (unit_code, slug) of the immediately preceding
                            lesson in the class's scheme of work, or ``None``
                            in week one.
    ``band``              — ``standard`` by default; ``easier`` for a class or
                            student moved down, ``harder`` for one moved up.
    ``earlier_lessons``   — [(unit_code, slug), ...] earlier lessons in the same
                            subject, **nearest first**, used only as fallback
                            when a lesson cannot supply its share.

    Returns a list of question dicts, ``size`` long. Selection is deterministic
    — it takes questions in bank order, so the same inputs always give the same
    assignment and a teacher previewing one sees what the class will get.
    """
    bank = bank if bank is not None else bank_by_lesson()

    def pool(key):
        return [q for q in bank.get(key, []) if q.get("band") == band]

    chosen, seen = [], set()

    def take(key, n):
        """Take up to ``n`` unused questions from one lesson. Returns count."""
        got = 0
        for q in pool(key):
            if got >= n:
                break
            if q["id"] in seen:
                continue
            seen.add(q["id"])
            chosen.append(q)
            got += 1
        return got

    # 1. Retrieval first — at least two from the immediately preceding lesson.
    #    Week one has no preceding lesson and takes all fifteen from its own.
    if preceding_lesson is not None:
        take(preceding_lesson, retrieval)

    # 2. The rest, spread as evenly as the current week's lessons allow.
    remaining = size - len(chosen)
    if current_lessons and remaining > 0:
        share, extra = divmod(remaining, len(current_lessons))
        for i, key in enumerate(current_lessons):
            take(key, share + (1 if i < extra else 0))

    # 3. Shortfall — a lesson that could not supply its share falls back to the
    #    nearest earlier lesson in the same subject, rather than shipping a
    #    short assignment. Current lessons are revisited first (a lesson may
    #    have questions left over once its own share was capped), then earlier
    #    ones nearest-first, and finally the preceding lesson.
    if len(chosen) < size:
        fallbacks = list(current_lessons) + list(earlier_lessons)
        if preceding_lesson is not None:
            fallbacks.append(preceding_lesson)
        for key in fallbacks:
            if len(chosen) >= size:
                break
            take(key, size - len(chosen))

    return chosen[:size]
