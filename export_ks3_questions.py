#!/usr/bin/env python3
"""export_ks3_questions.py — mirror the KS3 question pools into Postgres.

    python3 export_ks3_questions.py            # write SQL under build/ks3-questions/
    python3 export_ks3_questions.py --json     # write bank.json / ladder.json for the RPC
    python3 export_ks3_questions.py --stdout   # one statement per line, to stdout
    python3 export_ks3_questions.py --check    # counts only, write nothing
    python3 export_ks3_questions.py --verify   # ⭐ THE GATE: does the database still
                                               #   match Python, row for row?

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
ROWS_PER_STATEMENT = 250

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
    ap.add_argument("--json", action="store_true",
                    help="write bank.json / ladder.json for ks3_pools_ingest")
    ap.add_argument("--verify", action="store_true",
                    help="compare the live tables against Python, row for row")
    args = ap.parse_args()

    bank = bank_rows()
    ladder = ladder_rows()

    # ⚠️ THE LESSON SLUG MUST BE GLOBALLY UNIQUE, and this is where that is
    # enforced rather than hoped for.
    #
    # Python keys the bank by (unit_code, lesson_slug). The producer in the Node
    # backend cannot: it reads `ks3_bank_questions` filtered by `lesson_slug`
    # alone, because the scheme of work stores a subtopic SLUG and no unit code.
    # The two agree only while no slug appears in two units. If one ever does,
    # the producer silently merges both lessons' questions into one pool and
    # composes an assignment Python would never compose — and nothing about the
    # page would look wrong.
    #
    # It is true today across all 77 lessons. It is not guaranteed by anything
    # else, so it is asserted here, on the way out, where a new unit will trip
    # it the first time it is exported.
    by_slug = {}
    for r in bank:
        by_slug.setdefault(r["lesson_slug"], set()).add(r["unit_code"])
    collisions = {s: sorted(u) for s, u in by_slug.items() if len(u) > 1}
    if collisions:
        raise SystemExit(
            "export_ks3_questions: lesson slug(s) used by more than one unit — "
            "%s. The backend's producer looks a lesson up by slug alone (the "
            "scheme of work has no unit code), so it would merge them. Rename "
            "one of them before exporting."
            % "; ".join("%r in %s" % (s, u) for s, u in sorted(collisions.items())))

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

    if args.verify:
        sys.exit(verify(bank, ladder))

    if args.json:
        os.makedirs(OUT_DIR, exist_ok=True)
        for name, rows in (("bank", bank), ("ladder", ladder)):
            path = os.path.join(OUT_DIR, name + ".json")
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(rows, fh, ensure_ascii=False)
            print("     ✅ %-12s %8d bytes  → %s"
                  % (name + ".json", os.path.getsize(path), path))
        print("\n     Apply with ks3_pools_ingest(pool, payload). See the "
              "migration for the guard.\n")
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


# ── the gate ─────────────────────────────────────────────────────────────

def verify(bank, ladder):
    """Does the database still match Python, row for row?

    The tables are a mirror. A mirror nobody checks is just a second copy, and
    the failure it hides is the quiet one: a question edited in Python, the
    export not re-run, and every class served the old wording for a term while
    the repo says otherwise.

    Reads over PostgREST with a real session rather than a service key, because
    the pools are readable by any signed-in user and this only needs to READ.
    SKIPS LOUDLY when there are no credentials — a gate that passes because it
    could not run is worse than no gate.
    """
    import ssl
    import urllib.error
    import urllib.request

    pw = os.environ.get("MRB_TEST_STUDENT_PASSWORD")
    if not pw:
        print("\n     ⏭️  --verify SKIPPED: MRB_TEST_STUDENT_PASSWORD is not set,")
        print("        so the live tables cannot be read. This is the only check")
        print("        that the database still matches these files.\n")
        return 0

    url = "https://urklkrwevjtlfbwnipjn.supabase.co"
    src = open(os.path.join(REPO, "leaderboard.html"), encoding="utf-8").read()
    import re
    key = re.search(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}",
                    src).group(0)
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

    def api(path, headers, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(
            url + path, data=data, method=("POST" if data else "GET"),
            headers=dict({"Content-Type": "application/json"}, **headers))
        with urllib.request.urlopen(req, timeout=90, context=ctx) as r:
            return json.loads(r.read().decode())

    tok = api("/auth/v1/token?grant_type=password", {"apikey": key},
              {"email": "midebolabadmus@gmail.com", "password": pw})
    del pw
    auth = {"apikey": key, "Authorization": "Bearer " + tok["access_token"]}

    def fetch(table, cols):
        out, step = [], 1000
        while True:
            page = api("/rest/v1/%s?select=%s&order=%s&limit=%d&offset=%d"
                       % (table, cols, cols.split(",")[0], step, len(out)), auth)
            out.extend(page)
            if len(page) < step:
                return out

    problems = []

    def compare(name, want, got, keyfield, fields):
        w = {r[keyfield]: r for r in want}
        g = {r[keyfield]: r for r in got}
        missing = sorted(set(w) - set(g))
        extra = sorted(set(g) - set(w))
        if missing:
            problems.append("%s: %d row(s) in Python and NOT in the database — "
                            "the export has not been applied: %s"
                            % (name, len(missing), ", ".join(missing[:5])))
        if extra:
            problems.append("%s: %d row(s) in the database that Python does not "
                            "have — a retired question is still being served: %s"
                            % (name, len(extra), ", ".join(extra[:5])))
        differing = []
        for k in sorted(set(w) & set(g)):
            for f in fields:
                a, b_ = w[k][f], g[k][f]
                if f == "options":
                    a = json.dumps(a, sort_keys=True, ensure_ascii=False)
                    b_ = json.dumps(b_, sort_keys=True, ensure_ascii=False)
                if a != b_:
                    differing.append("%s.%s" % (k, f))
                    break
        if differing:
            problems.append("%s: %d row(s) differ between Python and the "
                            "database: %s" % (name, len(differing),
                                              ", ".join(differing[:5])))
        print("     %s %-8s %4d in Python, %4d live, %d missing, %d extra, %d differing"
              % ("❌" if (missing or extra or differing) else "✅", name,
                 len(w), len(g), len(missing), len(extra), len(differing)))

    print("\n     comparing the live tables against Python\n")
    compare("bank",
            bank,
            fetch("ks3_bank_questions",
                  "id,unit_code,lesson_slug,band,bank_position,text,figure,options"),
            "id",
            ["unit_code", "lesson_slug", "band", "bank_position", "text",
             "figure", "options"])
    compare("ladder",
            ladder,
            fetch("ks3_ladder_questions",
                  "question_ref,unit_code,lesson_slug,rung,text,answer_letter,options"),
            "question_ref",
            ["unit_code", "lesson_slug", "rung", "text", "answer_letter",
             "options"])

    print()
    if problems:
        for p in problems:
            print("        · " + p)
        print("\n     Re-run:  python3 export_ks3_questions.py --json  and apply "
              "it.\n")
        return 1
    print("     ✅ the database is exactly what these files say it is.\n")
    return 0


if __name__ == "__main__":
    main()
