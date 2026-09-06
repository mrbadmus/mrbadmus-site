#!/usr/bin/env python3
"""export_ks4_questions.py — mirror the KS4 assignment pool into Postgres.

    python3 export_ks4_questions.py                    # SQL under build/ks4-questions/
    python3 export_ks4_questions.py --subject physics  # one subject only
    python3 export_ks4_questions.py --check            # counts only, write nothing
    python3 export_ks4_questions.py --stdout           # statements to stdout
    python3 export_ks4_questions.py --verify           # ⭐ THE GATE: does the
                                                       #   database match Python?
    python3 export_ks4_questions.py --partial          # allow a part-authored pool
    python3 export_ks4_questions.py --delete-orphans   # retire withdrawn ids too

── Why this exists ──────────────────────────────────────────────────────

`ks4_data/questions/**.py` is where a KS4 assignment question is written, and
it is Python, in this repo. The thing that has to COMPOSE an assignment from
those questions is the Node backend, in a different repo. That is the same
bridge `export_ks3_questions.py` crosses, and it has the same three possible
answers — re-implement in Node, vendor a JSON copy, or mirror into the
database — of which only the third keeps a question written in exactly one
place. So: mirror.

`public.ks4_assignment_bank` is therefore a BUILD ARTEFACT, the way
`mrbadmus_site/` is. Python is the source. This script is the ONLY writer.
The export is idempotent, so running it twice changes nothing and running it
after an edit changes exactly what was edited. Nothing here authors a
question, and nothing in that table may be hand-edited — the next export
would silently revert the correction, which is the worst way to lose one.

── Why this is a separate script from the KS3 exporter ──────────────────

Not because KS4 is special, but because the two pools are DIFFERENT SHAPES
and one script serving both would have to branch on key stage in every
function it has.

KS3 stores `options` as jsonb: `[{text, correct, why}]`, one `why` per
distractor, the answer identified by a flag on an option. KS4 stores
`options` as a Postgres `text[]` of four plain strings, with the answer as a
`correct_index` smallint and a single `why` explaining the CORRECT answer.
That was ruled for MRB-332, `verify_answer_positions.py` measures
`correct_index` directly, and the database's own four-option CHECK constraint
only exists because the column is an array rather than a blob.

The two tables are separate for a harder reason still, spelled out in the
migration: eight KS4 subtopic slugs are byte-identical to KS3 lesson slugs,
`ks3_assignment_bank` is joined on `lesson_slug` alone, and a KS4 lookup
against it returns twelve KS3 questions — real science, correct, three years
too easy, and nothing anywhere saying so. Two tables end that structurally.
Two exporters keep it that way.

── Ship per subject, on purpose ─────────────────────────────────────────

The pool is authored by several people at once, one subject at a time, and
the plan is to SHIP EACH SUBJECT AS IT LANDS rather than wait for all three.

`ks4_data.load_pool()` defaults to `strict=True`, which insists on twelve
questions per subtopic across four-per-band. That is the right default: an
export is what children are served from, and a subtopic with nine questions
composes a short assignment nobody asked for.

`--partial` drops to `strict=False`, which skips ONLY the completeness check.
Everything else still holds — ids unique and `ks4-` prefixed, four distinct
non-empty options, `correct_index` in range, `tier`/`triple_only` agreeing
with the curriculum's own classification. A malformed question never loads,
with or without the flag. `--partial` means "some are missing", never "some
are wrong".

⚠️ Use `--partial` with `--subject` for an overnight ship, so that what you
are calling partial is one named subject rather than the whole estate.

── The two flags that decide who sees a question ────────────────────────

    tier='foundation', triple_only=False → BASE. Every class.
    tier='higher',     triple_only=False → Higher tier only.
    triple_only=True                     → Triple Science only.

A Foundation Combined class must NEVER be served a higher or a triple_only
question. This exporter does not compute those flags and does not check them
— `ks4_data.classify()` derives them from the site's own curriculum data and
`load_pool()` refuses any authored file that disagrees. The mirror's job is
to carry them across unchanged, which is why they are in the column list and
in the `--verify` comparison: a flag that drifted in transit is a Foundation
child sitting a Higher question.
"""

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

OUT_DIR = os.path.join("build", "ks4-questions")

TABLE = "ks4_assignment_bank"

# ⚠️ SMALL ON PURPOSE, and the same 250 the KS3 exporter uses for the same
# reason. Each row is a stem, four options and a `why` — around a kilobyte —
# so 250 rows is a statement of a few hundred kB. A first attempt at KS3 used
# a much larger chunk and the load stalled part-way through; whatever the real
# ceiling is, it is not worth finding by binary search against a table
# students are served from. Small statements apply in seconds, and any ONE of
# them can be re-run on its own, because they are upserts.
ROWS_PER_STATEMENT = 250

# The migration's column order, deliberately, so a reader can hold the file
# and the table side by side. `id` is the conflict key.
COLUMNS = ["id", "subtopic_slug", "subject", "band", "tier", "triple_only",
           "text", "options", "correct_index", "why", "bank_position"]
CONFLICT_KEY = "id"

# The subset compared by --verify: everything except the key itself.
COMPARED = [c for c in COLUMNS if c != CONFLICT_KEY]


# ── SQL literals ─────────────────────────────────────────────────────────

def sql_str(v):
    """A Postgres string literal, or NULL."""
    if v is None:
        return "null"
    return "'" + str(v).replace("'", "''") + "'"


def sql_text_array(items):
    """A Postgres `text[]` literal: array['a','b','c','d']::text[].

    ⚠️ THIS IS THE ONE PLACE THE TWO POOLS' SHAPES GENUINELY DIFFER, so it is
    worth being explicit about why it is written this way.

    The obvious alternative is Postgres's own array-literal syntax,
    `'{"a","b"}'::text[]`, and it is a trap: that form is a STRING that
    Postgres re-parses, so a comma, a brace, a backslash or a double quote
    inside an option changes how many elements come out the other side. Real
    options in this corpus contain commas constantly ("2.5 m/s, to the right")
    and quotes occasionally.

    `array[...]` is not a string. Each element is its own literal, escaped
    once by `sql_str`, and nothing re-parses it — so an option containing
    `","` arrives as one element with a comma in it, which is what was
    written. The `::text[]` cast is not decoration either: an empty or
    all-NULL `array[]` would otherwise be typed `unknown[]` and the insert
    would fail with a type error rather than with the four-option CHECK that
    actually describes the problem.
    """
    if items is None:
        return "null"
    return "array[" + ", ".join(sql_str(o) for o in items) + "]::text[]"


def sql_cell(column, value):
    """One value, rendered for its column's type. Types are named, not sniffed.

    The KS3 exporter dispatches on the Python type of the value — list/dict →
    jsonb, int → bare, everything else → quoted string. That works there
    because no column is boolean. Here `triple_only` is, and `isinstance(True,
    int)` is True in Python, so a type sniff would emit `1` for a boolean
    column: accepted by Postgres, and accepted for the WRONG reason. Dispatch
    on the column instead — the schema is known, so there is no reason to
    guess.
    """
    if column == "options":
        return sql_text_array(value)
    if column == "triple_only":
        if value is None:
            return "null"
        return "true" if value else "false"
    if column in ("correct_index", "bank_position"):
        if value is None:
            return "null"
        if isinstance(value, bool) or not isinstance(value, int):
            raise SystemExit(
                "export_ks4_questions: %s is %r, expected an integer. The "
                "column is a smallint and a quoted value would either fail or "
                "be silently coerced." % (column, value))
        return str(value)
    return sql_str(value)


# ── emitting ─────────────────────────────────────────────────────────────

def upsert_statements(rows):
    """Idempotent multi-row upserts, chunked at ROWS_PER_STATEMENT."""
    out = []
    updates = ", ".join("%s = excluded.%s" % (c, c) for c in COMPARED)
    for start in range(0, len(rows), ROWS_PER_STATEMENT):
        chunk = rows[start:start + ROWS_PER_STATEMENT]
        values = []
        for r in chunk:
            values.append("(" + ", ".join(
                sql_cell(col, r[col]) for col in COLUMNS) + ")")
        out.append(
            "insert into public.%s (%s) values\n%s\non conflict (%s) do update "
            "set %s, updated_at = now();"
            % (TABLE, ", ".join(COLUMNS), ",\n".join(values), CONFLICT_KEY,
               updates))
    return out


def delete_orphans_statement(rows, subject):
    """Remove rows the database still serves and Python no longer has.

    ── ⚠️ WHY THIS IS NOT THE DEFAULT ───────────────────────────────────

    Because the export ships one subject at a time, and a delete that runs by
    default would eventually run at the wrong moment.

    Picture the overnight run: physics is authored and shipped, chemistry is
    half written, an executor exports chemistry with `--partial`. If orphan
    deletion were part of a normal export, that run's row set — chemistry
    only, and not all of it — would be the definition of "everything Python
    has", and every physics row shipped hours earlier would be an orphan.
    Three thousand live questions deleted by a script that exited 0 and said
    it had exported chemistry. Nothing in the output would look wrong; the
    next class to be set physics homework would find out.

    So retiring a question is a SEPARATE, DELIBERATE act. It is asked for by
    name, it is scoped to the subject being exported when one is named, and it
    refuses to run at all under `--partial` — see `main()`, which will not let
    the two flags combine, because "the pool is incomplete" and "these rows
    are withdrawn" are contradictory claims about the same absence.

    Emitted AFTER the upserts, never before: that way there is no instant at
    which a question a student could be mid-assignment on has been deleted but
    its replacement not yet inserted.

    It is deliberately ONE statement rather than chunked. A NOT-IN list cannot
    be split — each chunk's list would be missing the other chunks' ids, so
    chunk one would delete exactly the rows chunk two exists to keep.
    """
    keep = sorted(r["id"] for r in rows)
    scope = ("subject = %s and " % sql_str(subject)) if subject else ""
    if not keep:
        # Refusing rather than emitting `delete from … where subject = 'x'`.
        # An unqualified wipe is never what somebody meant by "remove the
        # questions that are no longer in Python".
        raise SystemExit(
            "export_ks4_questions --delete-orphans: Python has no rows in "
            "scope, so the generated delete would empty %s%s. Nothing has "
            "been written. If a subject really is being withdrawn wholesale, "
            "do it by hand and mean it."
            % (TABLE, (" for subject %r" % subject) if subject else ""))
    return ("-- Retire withdrawn questions. Runs AFTER the upserts above.\n"
            "delete from public.%s\n where %sid <> all (%s);"
            % (TABLE, scope, sql_text_array(keep)))


# ── counting ─────────────────────────────────────────────────────────────

def report(rows, subject, partial):
    """What was loaded, broken down the way a reviewer needs to see it."""
    subjects = sorted({r["subject"] for r in rows})
    subtopics = {r["subtopic_slug"] for r in rows}

    print("\n📚  export_ks4_questions — the KS4 assignment pool, out of Python\n")
    if subject:
        print("     --subject %s" % subject)
    if partial:
        print("     --partial: the 12-per-subtopic completeness check is OFF. "
              "Everything else still holds.")
    print("     %4d question(s) across %d subtopic(s)"
          % (len(rows), len(subtopics)))

    for subj in subjects:
        srows = [r for r in rows if r["subject"] == subj]
        stops = {r["subtopic_slug"] for r in srows}
        bands = {b: sum(1 for r in srows if r["band"] == b)
                 for b in ("easier", "standard", "harder")}
        # The audience split is printed on every run because it is the thing
        # that must never quietly change: a question moving from BASE to
        # HIGHER changes who is allowed to be asked it.
        base = sum(1 for r in srows
                   if r["tier"] == "foundation" and not r["triple_only"])
        higher = sum(1 for r in srows
                     if r["tier"] == "higher" and not r["triple_only"])
        triple = sum(1 for r in srows if r["triple_only"])
        print("       %-10s %4d q  %3d subtopic(s)   "
              "easier %d / standard %d / harder %d   "
              "base %d / higher %d / triple %d"
              % (subj, len(srows), len(stops), bands["easier"],
                 bands["standard"], bands["harder"], base, higher, triple))

    if not rows:
        print("       (nothing authored in scope yet)")


# ── main ─────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(
        description="Mirror the KS4 assignment question pool into Postgres.")
    ap.add_argument("--subject", choices=("biology", "chemistry", "physics"),
                    help="export one subject only (the per-subject ship)")
    ap.add_argument("--check", action="store_true",
                    help="validate and count; write nothing")
    ap.add_argument("--stdout", action="store_true",
                    help="print the statements instead of writing files")
    ap.add_argument("--verify", action="store_true",
                    help="compare the live table against Python, row for row")
    ap.add_argument("--partial", action="store_true",
                    help="allow a part-authored pool (load_pool strict=False) "
                         "— completeness only; malformed questions still fail")
    ap.add_argument("--project", choices=("test", "prod"), default="test",
                    help="which database --verify reads (default: test). "
                         "The KS4 pool reaches production only at merge, so "
                         "verifying prod before then compares against a table "
                         "that is not there yet.")
    ap.add_argument("--delete-orphans", action="store_true",
                    help="also emit a delete for ids the database has and "
                         "Python no longer does. NOT the default; see the "
                         "comment on delete_orphans_statement()")
    args = ap.parse_args()

    # "The pool is incomplete" and "these rows are withdrawn" are the same
    # absence with opposite meanings, and only the author knows which it is.
    # Refuse rather than pick.
    if args.delete_orphans and args.partial:
        raise SystemExit(
            "export_ks4_questions: --delete-orphans and --partial cannot be "
            "combined. --partial says questions are MISSING because they have "
            "not been written yet; --delete-orphans reads every absence as a "
            "question that has been WITHDRAWN, and would delete live rows for "
            "subtopics an author is still working on. Ship the subject "
            "complete first, then retire withdrawn ids in a separate run.")

    from ks4_data import load_pool

    # load_pool raises SystemExit with a numbered problem list when anything
    # is malformed. That is the right behaviour and it is left to propagate:
    # a pool that does not load must not produce a half-written export, and
    # the message it prints already names every file and question.
    rows = load_pool(args.subject, strict=not args.partial)

    report(rows, args.subject, args.partial)

    if args.check:
        print("\n     --check: nothing written.\n")
        return

    if args.verify:
        sys.exit(verify(rows, args.subject, args.partial))

    stmts = upsert_statements(rows)
    if args.delete_orphans:
        stmts.append(delete_orphans_statement(rows, args.subject))

    if not stmts:
        raise SystemExit(
            "export_ks4_questions: nothing to export%s. If that is a "
            "surprise, the authored modules are not where _modules() looks: "
            "ks4_data/questions/<subject>/<topic>.py, each with a QUESTIONS "
            "list." % (" for %s" % args.subject if args.subject else ""))

    if args.stdout:
        for s in stmts:
            print(s)
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    # Clearing first, so a run that produces fewer statements than the last
    # one cannot leave a stale tail behind for somebody to apply.
    for old in sorted(os.listdir(OUT_DIR)):
        if old.endswith(".sql"):
            os.remove(os.path.join(OUT_DIR, old))
    for i, s in enumerate(stmts):
        path = os.path.join(OUT_DIR, "%02d.sql" % i)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(s + "\n")
    print("\n     ✅ %d statement(s) → %s/" % (len(stmts), OUT_DIR))
    print("\n     These are upserts, applied in filename order. Applying them "
          "twice is applying them once.")
    if args.delete_orphans:
        print("     ⚠️ The LAST file is a DELETE. Apply it last, or not at "
              "all.")
    print()


# ── the gate ─────────────────────────────────────────────────────────────

def verify(rows, subject, partial):
    """Does the database still match Python, row for row?

    The table is a mirror, and a mirror nobody checks is just a second copy.
    The failure it hides is the quiet one: a question corrected in Python, the
    export not re-run, and every class served the old wording — or worse, a
    `tier` flag fixed in the repo and still wrong in the table, which is a
    Foundation class being handed a Higher question by a system that believes
    it has been fixed.

    Reads over PostgREST with a real signed-in session rather than a service
    key, exactly as `export_ks3_questions.py --verify` does: the pool is
    readable by any authenticated user (`ks4_assignment_bank_read`), and this
    only ever READS.

    ⚠️ IT NEVER RETURNS 0 WITHOUT HAVING LOOKED. Three distinct exits:

        0  the mirror agrees
        1  measured drift — the counts or the fields differ
        3  could not look — no credential, or the network/API refused

    3 rather than 1 because a caller has to be able to tell "the mirror is
    wrong" from "nobody read it", and 3 rather than 0 because a gate that
    passes because it could not run is worse than no gate at all. `--verify`
    exiting 0 is a positive claim about the database, and it is only ever made
    after the rows have been compared.
    """
    import base64
    import re
    import ssl
    import urllib.error
    import urllib.request

    def cannot_see(reason, *hints):
        print("\n     ⛔ export_ks4_questions --verify COULD NOT LOOK: %s"
              % reason)
        for h in hints:
            print("        %s" % h)
        print("        Exit 3 — this is NOT a pass. The database has not been "
              "compared\n        against these files.\n")
        return 3

    pw = os.environ.get("MRB_TEST_STUDENT_PASSWORD")
    if not pw:
        return cannot_see(
            "MRB_TEST_STUDENT_PASSWORD is not set, so there is no session to "
            "read the table with.",
            "Set it and re-run. This is the only check that the questions a "
            "student",
            "is actually served still match the authored files.")

    # ⚠️ WHICH DATABASE --verify LOOKS AT (MRB-332).
    #
    # This defaults to TEST, and that is deliberate — it is the opposite of
    # the KS3 exporter it was modelled on, which hardcodes production.
    #
    # The KS3 default is right for KS3: that pool has been live for weeks, so
    # "does the database still match Python" is a question about production.
    # It is wrong for KS4, and dangerously so during the build: the KS4 pool
    # reaches production only at merge, so a --verify pointed at prod today
    # compares the authored files against a table that does not exist yet and
    # reports drift — a red that means "you are looking at the wrong place",
    # dressed as "your export is broken". The obvious response to that red is
    # to re-export, which would do nothing, twice.
    #
    # So: TEST by default, prod only when asked for by name. After the merge,
    # `--project prod` is the production gate.
    PROJECTS = {
        "test": "qeppkiswvclkkwbxmlok",
        "prod": "urklkrwevjtlfbwnipjn",
    }
    ref = PROJECTS[getattr(args, "project", None) or "test"]
    url = "https://%s.supabase.co" % ref
    print("     verifying against %s (%s)"
          % (("PRODUCTION" if ref == PROJECTS["prod"] else "TEST"), ref))

    # The anon key comes out of shared/config.js, which carries BOTH projects
    # — so take the one whose own `ref` claim matches the project this verify
    # points at, rather than the first JWT in the file. (The KS3 exporter used
    # to scrape this out of leaderboard.html and was left reaching for a key
    # that had moved; config.js is the durable home.)
    cfg = os.path.join(REPO, "shared", "config.js")
    try:
        src = open(cfg, encoding="utf-8").read()
    except OSError as exc:
        return cannot_see("shared/config.js is unreadable (%s)." % exc,
                          "It is where the anon key for project %r lives." % ref)
    key = None
    for tok in re.findall(
            r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}",
            src):
        payload = tok.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        try:
            claims = base64.urlsafe_b64decode(payload).decode()
        except Exception:
            continue
        if ('"ref":"%s"' % ref) in claims:
            key = tok
            break
    if key is None:
        return cannot_see(
            "shared/config.js carries no anon key for project %r." % ref,
            "Either the key was moved, or this verify is pointed at a project "
            "the site",
            "does not configure. Do not 'fix' it by taking whichever key is "
            "first in the file.")

    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

    def api(path, headers, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(
            url + path, data=data, method=("POST" if data else "GET"),
            headers=dict({"Content-Type": "application/json"}, **headers))
        with urllib.request.urlopen(req, timeout=90, context=ctx) as r:
            return json.loads(r.read().decode())

    # ⚠️ Every network failure below becomes an exit 3 with a name, never a
    # traceback and never a pass. A gate whose only failure mode is a stack
    # trace tends to get wrapped in a `|| true` by the third person who meets
    # it at midnight.
    try:
        tok = api("/auth/v1/token?grant_type=password", {"apikey": key},
                  {"email": "midebolabadmus@gmail.com", "password": pw})
    except urllib.error.HTTPError as exc:
        return cannot_see(
            "sign-in was refused (HTTP %s)." % exc.code,
            "MRB_TEST_STUDENT_PASSWORD is set but the credential did not work "
            "against %s." % ref)
    except Exception as exc:
        return cannot_see("sign-in could not reach %s (%s)." % (url, exc),
                          "No network, no comparison.")
    del pw
    auth = {"apikey": key, "Authorization": "Bearer " + tok["access_token"]}

    cols = ",".join(COLUMNS)
    # Scoped to the subject being verified when one is named. Without this a
    # `--verify --subject physics` would report every biology row in the table
    # as an extra, which is not drift — it is the other half of the pool.
    scope = ("&subject=eq.%s" % subject) if subject else ""

    def fetch():
        out, step = [], 1000
        while True:
            try:
                page = api("/rest/v1/%s?select=%s%s&order=id&limit=%d&offset=%d"
                           % (TABLE, cols, scope, step, len(out)), auth)
            except urllib.error.HTTPError as exc:
                detail = ""
                try:
                    detail = exc.read().decode()[:300]
                except Exception:
                    pass
                raise _Unreachable(
                    "reading public.%s failed (HTTP %s). %s"
                    % (TABLE, exc.code, detail))
            except Exception as exc:
                raise _Unreachable("reading public.%s failed (%s)"
                                   % (TABLE, exc))
            out.extend(page)
            if len(page) < step:
                return out

    try:
        live = fetch()
    except _Unreachable as exc:
        return cannot_see(
            str(exc),
            "If the table does not exist yet, apply "
            "supabase/migrations/20260906230000_mrb332_ks4_assignment_bank.sql",
            "first. An unapplied migration is not a green mirror.")

    print("\n     comparing public.%s against Python%s\n"
          % (TABLE, (" (subject=%s)" % subject) if subject else ""))

    want = {r["id"]: r for r in rows}
    got = {r["id"]: r for r in live}
    missing = sorted(set(want) - set(got))
    extra = sorted(set(got) - set(want))

    problems = []
    if missing:
        problems.append(
            "%d row(s) in Python and NOT in the database — the export has not "
            "been applied: %s" % (len(missing), ", ".join(missing[:5])))

    if extra:
        line = ("%d row(s) in the database that Python does not have — a "
                "retired question is still being served: %s"
                % (len(extra), ", ".join(extra[:5])))
        if partial:
            # Under --partial the pool is incomplete BY DECLARATION, so an id
            # the database has and this run does not may simply be a module
            # that was not loaded. Reported loudly, and deliberately not
            # counted as drift — claiming drift here would train whoever runs
            # the overnight ship to ignore the extras line, which is the line
            # that matters when the pool is complete.
            print("     ⚠️ --partial: %s" % line)
            print("        Not counted as drift: this run did not claim to "
                  "hold the whole pool.")
            print("        Re-run --verify WITHOUT --partial before believing "
                  "the mirror is clean.")
        else:
            problems.append(line)

    differing = []
    for k in sorted(set(want) & set(got)):
        for f in COMPARED:
            a, b = want[k][f], got[k][f]
            if f == "options":
                # PostgREST returns a text[] as a JSON array of strings, so
                # both sides are already lists. Compared IN ORDER and never
                # sorted: `correct_index` is an index into this exact
                # sequence, so a reordered options array is a different
                # question with a different answer.
                a, b = list(a or []), list(b or [])
            elif f == "triple_only":
                a, b = bool(a), bool(b)
            if a != b:
                differing.append("%s.%s" % (k, f))
                break
    if differing:
        problems.append("%d row(s) differ between Python and the database: %s"
                        % (len(differing), ", ".join(differing[:5])))

    ok = not problems
    print("     %s %-18s %5d in Python, %5d live, %d missing, %d extra, "
          "%d differing"
          % ("❌" if not ok else "✅", TABLE, len(want), len(got),
             len(missing), len(extra), len(differing)))
    print()

    if problems:
        for p in problems:
            print("        · " + p)
        print("\n     Re-run:  python3 export_ks4_questions.py%s   and apply "
              "build/ks4-questions/.\n"
              % (" --subject %s" % subject if subject else ""))
        return 1

    if partial:
        print("     ✅ everything Python loaded this run is live and identical."
              "\n        ⚠️ --partial: that is NOT a statement about the rest "
              "of the pool.\n")
    else:
        print("     ✅ the database is exactly what these files say it is.\n")
    return 0


class _Unreachable(Exception):
    """The database could not be read. Distinct from 'the database is wrong'."""


if __name__ == "__main__":
    main()
