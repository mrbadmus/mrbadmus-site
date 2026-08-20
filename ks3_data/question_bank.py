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

BANDS = ("easier", "standard", "harder")
BAND_LETTER = {"easier": "e", "standard": "s", "harder": "h"}

QUESTIONS_PER_LESSON = 12
PER_BAND = 4
ASSIGNMENT_SIZE = 15

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
        for q in bank.get(key, []):
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
