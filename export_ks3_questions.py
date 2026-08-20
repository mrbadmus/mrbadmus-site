#!/usr/bin/env python3
"""export_ks3_questions.py — mirror the KS3 question pools into Postgres.

    python3 export_ks3_questions.py            # write SQL under build/ks3-questions/
    python3 export_ks3_questions.py --stdout   # one statement per line, to stdout
    python3 export_ks3_questions.py --check    # counts only, write nothing

── Why this exists ──────────────────────────────────────────────────────

`compose_assignment()` and the 70 question modules are Python, in this repo.
The thing that has to CALL them — the on-demand assignment producer — lives in
the Node backend, in a different repo. There are three ways to bridge that and
only one of them keeps a question written in exactly one place:

  1. Re-implement the bank in Node.          70 files of content, duplicated.
  2. Vendor a JSON copy into the backend.    Still a copy. Still drifts.
  3. Mirror it into the database. ← this.

The tables are a BUILD ARTEFACT, the way `mrbadmus_site/` is. Python is the
source; this script is the only writer; the export is idempotent, so running it
twice changes nothing and running it after an edit changes exactly what was
edited. Nothing here authors a question and nothing here may be hand-edited in
the database.

It also buys something the wiring needed anyway: with the pools in Postgres the
assignment page can read a question's text, its four options, their letters and
the per-distractor `why` in one query — instead of fetching the lesson's built
HTML page and scraping `.ks3-option[data-correct]` out of the DOM, which is what
`student/assignment.html:96` has had to do, and which breaks the moment the
lesson template changes a class name.

── The two pools are not the same shape ─────────────────────────────────

**The bank** (`ks3_data/<unit>/questions_*.py`) is twelve questions per lesson,
four per band, each option carrying a `why` for every wrong answer. It is what a
weekly assignment is drawn from.

**The ladder** (`LESSON["ladder"]`) is the four rungs at the foot of each lesson
page. Only `recall` and `apply` are exported: they are multiple choice and have
a right answer. `explain` and `produce` are marked BY THE STUDENT against
success criteria — nothing can score them, so nothing can put them in a recall
round.

⚠️ **The right-answer feedback slot is left CLOSED.** A ladder authors three
feedback strings, one for each wrong option. The correct option has none, and
this exporter writes `why: null` for it rather than inventing a fourth. That is
the standing ruling and it is what `student_parity.py` layer H is watching for:
a generic "Correct!" is not teaching, and a reused string is worse than silence.
"""

import argparse
import importlib
import json
import os
import pkgutil
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

OUT_DIR = os.path.join("build", "ks3-questions")

# ⚠️ SMALL ON PURPOSE. Each row is a question, four options and four feedback
# strings — around a kilobyte of JSON — so 40 rows is roughly 38 kB per
# statement. A first attempt used 120 and the load stalled part-way through;
# whatever the ceiling is, it is not worth finding by binary search on a
# production table. 28 small statements apply in well under a minute and any
# one of them can be re-run on its own, because they are upserts.
ROWS_PER_STATEMENT = 120

LETTERS = ("A", "B", "C", "D")

# Ladder keys that are not rungs. `retry_note` and `sub` are authoring notes
# that live alongside the rungs in the same dict.
NOT_A_RUNG = {"retry_note", "sub"}
MARKED_RUNGS = ("recall", "apply")


def sql_str(v):
    """A Postgres string literal, or NULL."""
    if v is None:
        return "null"
    return "'" + str(v).replace("'", "''") + "'"


def sql_json(v):
    return sql_str(json.dumps(v, ensure_ascii=False, separators=(",", ":"))) + "::jsonb"


# ── the bank ─────────────────────────────────────────────────────────────

def bank_rows():
    """Every bank question, in bank order.

    `bank_position` is the question's index inside its own module. That
    ordering is what makes `compose_assignment` deterministic — it takes
    questions in bank order — so it has to survive the trip into the database
    or the producer would compose a different assignment from the same inputs.
    """
    import ks3_data.question_bank as qb

    rows = []
    by_lesson = qb.bank_by_lesson()
    for (unit_code, lesson_slug) in sorted(by_lesson):
        for pos, q in enumerate(by_lesson[(unit_code, lesson_slug)]):
            opts = q.get("options") or []
            if len(opts) != 4:
                raise SystemExit(
                    "export_ks3_questions: %s has %d option(s), expected 4"
                    % (q.get("id"), len(opts)))
            if sum(1 for o in opts if o.get("correct")) != 1:
                raise SystemExit(
                    "export_ks3_questions: %s does not have exactly one "
                    "correct option" % q.get("id"))
            rows.append(dict(
                id=q["id"],
                unit_code=unit_code,
                lesson_slug=lesson_slug,
                band=q["band"],
                bank_position=pos,
                text=q["text"],
                figure=q.get("figure"),
                options=[
                    dict(text=o["text"],
                         correct=bool(o.get("correct")),
                         # The correct option carries no `why` in the bank
                         # either — the field is the misconception behind a
                         # DISTRACTOR. Kept null rather than absent so the
                         # shape is the same for all four.
                         why=o.get("why"))
                    for o in opts
                ],
            ))
    return rows


# ── the ladder ───────────────────────────────────────────────────────────

def lesson_modules():
    """Every authored lesson module, as (unit_code, module)."""
    import ks3_data

    found = []
    for unit in sorted(m.name for m in pkgutil.iter_modules(ks3_data.__path__)
                       if m.ispkg):
        pkg_dir = os.path.join(REPO, "ks3_data", unit)
        for fname in sorted(os.listdir(pkg_dir)):
            if not (fname.startswith("lesson_") and fname.endswith(".py")):
                continue
            mod = importlib.import_module("ks3_data.%s.%s" % (unit, fname[:-3]))
            if getattr(mod, "LESSON", None) is not None:
                found.append((unit.upper(), mod))
    return found


def ladder_rows():
    rows = []
    for unit_code, mod in lesson_modules():
        lesson = mod.LESSON
        slug = lesson.get("slug")
        ladder = lesson.get("ladder") or {}
        if not slug:
            raise SystemExit(
                "export_ks3_questions: %s has a ladder but no slug" % mod.__name__)
        for rung in MARKED_RUNGS:
            r = ladder.get(rung)
            if r is None:
                continue
            opts = r.get("options") or []
            if len(opts) != 4:
                raise SystemExit(
                    "export_ks3_questions: %s#%s has %d option(s), expected 4"
                    % (slug, rung, len(opts)))
            answer = r.get("answer")
            if not isinstance(answer, int) or not (0 <= answer < 4):
                raise SystemExit(
                    "export_ks3_questions: %s#%s has answer=%r, expected an "
                    "index 0-3" % (slug, rung, answer))
            # `feedback` is keyed by the index of the WRONG option it corrects.
            # Authored files use int keys; be tolerant of str keys too.
            fb = r.get("feedback") or {}
            fb = {int(k): v for k, v in fb.items()}
            missing = [i for i in range(4) if i != answer and i not in fb]
            if missing:
                raise SystemExit(
                    "export_ks3_questions: %s#%s has no feedback for wrong "
                    "option(s) %s — every distractor must name the "
                    "misconception it represents"
                    % (slug, rung, ", ".join(LETTERS[i] for i in missing)))
            rows.append(dict(
                question_ref="%s#%s" % (slug, rung),
                unit_code=unit_code,
                lesson_slug=slug,
                rung=rung,
                text=r["q"],
                answer_letter=LETTERS[answer],
                options=[
                    dict(letter=LETTERS[i],
                         text=opts[i],
                         correct=(i == answer),
                         # ⚠️ THE RIGHT-ANSWER SLOT IS CLOSED. Null, not a
                         # generic line. See the module docstring.
                         why=(None if i == answer else fb[i]))
                    for i in range(4)
                ],
            ))
    return rows


# ── emitting ─────────────────────────────────────────────────────────────

def upsert_statements(table, columns, rows, conflict_key):
    """Idempotent multi-row upserts, chunked."""
    out = []
    for start in range(0, len(rows), ROWS_PER_STATEMENT):
        chunk = rows[start:start + ROWS_PER_STATEMENT]
        values = []
        for r in chunk:
            cells = []
            for col in columns:
                v = r[col]
                if isinstance(v, (list, dict)):
                    cells.append(sql_json(v))
                elif isinstance(v, int) and not isinstance(v, bool):
                    cells.append(str(v))
                else:
                    cells.append(sql_str(v))
            values.append("(" + ", ".join(cells) + ")")
        updates = ", ".join(
            "%s = excluded.%s" % (c, c) for c in columns if c != conflict_key)
        out.append(
            "insert into public.%s (%s) values\n%s\non conflict (%s) do update "
            "set %s, updated_at = now();"
            % (table, ", ".join(columns), ",\n".join(values), conflict_key,
               updates))
    return out


BANK_COLUMNS = ["id", "unit_code", "lesson_slug", "band", "bank_position",
                "text", "figure", "options"]
LADDER_COLUMNS = ["question_ref", "unit_code", "lesson_slug", "rung", "text",
                  "answer_letter", "options"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true",
                    help="print the statements instead of writing files")
    ap.add_argument("--check", action="store_true",
                    help="validate and count; write nothing")
    args = ap.parse_args()

    bank = bank_rows()
    ladder = ladder_rows()

    lessons_banked = len({(r["unit_code"], r["lesson_slug"]) for r in bank})
    lessons_laddered = len({r["lesson_slug"] for r in ladder})

    print("\n📚  export_ks3_questions — the pools, out of Python\n")
    print("     bank    %4d question(s) across %d lesson(s)"
          % (len(bank), lessons_banked))
    print("     ladder  %4d question(s) across %d lesson(s)  (recall + apply "
          "only)" % (len(ladder), lessons_laddered))

    if args.check:
        print("\n     --check: nothing written.\n")
        return

    stmts = (upsert_statements("ks3_bank_questions", BANK_COLUMNS, bank, "id")
             + upsert_statements("ks3_ladder_questions", LADDER_COLUMNS,
                                 ladder, "question_ref"))

    if args.stdout:
        for s in stmts:
            print(s)
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    for old in os.listdir(OUT_DIR):
        if old.endswith(".sql"):
            os.remove(os.path.join(OUT_DIR, old))
    for i, s in enumerate(stmts):
        path = os.path.join(OUT_DIR, "%02d.sql" % i)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(s + "\n")
    print("\n     ✅ %d statement(s) → %s/" % (len(stmts), OUT_DIR))
    print("\n     These are upserts. Applying them twice is applying them "
          "once.\n")


if __name__ == "__main__":
    main()
