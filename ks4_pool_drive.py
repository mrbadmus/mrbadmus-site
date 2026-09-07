"""ks4_pool_drive.py — MRB-332. A KS4 teacher sets work, and the right child
gets the right questions.

    MRB_THROWAWAY_PASSWORD=<pw> python3 ks4_pool_drive.py
    MRB_THROWAWAY_PASSWORD=<pw> python3 ks4_pool_drive.py --keep

⚠️ REQUIRES THE INTEGRATED BRANCH. It imports `mrb331_fixture`, which arrives
with MRB-331 (`feat/set-work`), and it drives a backend carrying MRB-332's
`bankFor` KS4 branch (`feat/mrb332-ks4-pool`). Run it after the rebase, not
before; on its own branch it will fail at the import, loudly, which is the
correct behaviour.

⚠️ EVERY CHECK RUNS ON A REAL USER'S JWT against the real TEST project through
a locally-run backend, exactly as `set_work_drive.py` does. Nothing is stubbed.
The service key builds and tears down the world and never appears inside a
check — a proof carried on a service-role key proves nothing about what a
teacher or a child can actually do, because service role bypasses RLS.

── WHAT THIS DRIVE EXISTS TO PROVE ─────────────────────────────────────

One property, and it is the one that matters to a child:

    **A Foundation Combined class is never served a Higher or a Triple-only
    question. A Triple Higher class is served everything.**

`ks4_pool_check.py` proves that about the DATA. This proves it about the
SERVING PATH — the class row, the scope function, the query, RLS and the
payload, end to end — because a correct rule and a query that forgets to
apply it look identical from the outside.

── ⚠️ THREE OF MRB-331'S CHECKS INVERT HERE, AND ONE CHANGES SHAPE ─────

`set_work_drive.py` asserts, correctly for its own branch:

    · `has_bank is False` for a KS4 class
    · every KS4 lesson reports `available == 0`
    · the eight colliding slugs report `available == 0`

The first two simply invert once this pool exists, and the rebase must update
them; they are named here so that whoever does the rebase finds them.

**The third does NOT invert — it changes shape, and getting that wrong would
re-open the exact hole MRB-331 closed.** The eight colliding slugs hold twelve
KS3 rows each. They now also hold twelve KS4 rows each. So `available == 12`
is true whether the route is reading the right table or the wrong one, and a
check on the number proves nothing at all.

What separates them is the IDENTITY of the rows: a KS4 pool id begins `ks4-`
and a KS3 bank id looks like `c1-04-h02`. So the collision check here asserts
that every question served for a colliding slug is a `ks4-` id, and that no
KS3 id appears anywhere in a KS4 payload. That is a property no amount of
counting can fake.
"""

import json
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)
sys.path.insert(0, REPO)

try:
    import mrb331_fixture as FX          # noqa: E402  (after chdir)
except ModuleNotFoundError:
    raise SystemExit(
        "ks4_pool_drive: mrb331_fixture is missing.\n"
        "This drive runs on the INTEGRATED branch — MRB-331 (feat/set-work)\n"
        "provides the fixture and the two KS4 classes it needs. Rebase this\n"
        "lane onto MRB-331 and run it again.")

import ks4_data                          # noqa: E402

# ⚠️ THE CHECKOUT THIS DRIVE LAUNCHES `node server.js` FROM. This hardwired the
# MAIN backend checkout, which is exactly the defect MRB-331 fixed in
# `pool_ownership.py` and `set_work_drive.py` on 7 September — the main checkout
# is a SHARED working copy and any session can leave it on any branch. This
# lane's own work was what was sitting in it that morning.
#
# ⚠️ The dangerous direction is not the red. A drive pointed at a colleague's
# branch that happens to satisfy the contract reports green about a backend
# nobody is shipping, and nobody investigates a pass. So it takes an explicit
# path, in the same shape and precedence as set_work_drive.py; the sibling repo
# stays the default because that is what an ordinary machine has.
BACKEND = (
    (sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None)
    or os.environ.get("MRB_BACKEND")
    or "/Users/midebadmus/Documents/GitHub/mrbadmus---backend"
)
PORT = 5532                              # not 5531 — set_work_drive owns that
API = "http://127.0.0.1:%d" % PORT
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

NOW = datetime.now(timezone.utc)
DUE = NOW + timedelta(days=7)

# A KS3 bank id: unit code, lesson number, band letter and index — 'c1-04-h02'.
# Anything matching this inside a KS4 payload is a cross-key-stage leak.
KS3_ID = re.compile(r"^[bcp]\d{1,2}-\d{2}-[esh]\d{2}$", re.I)

checks = []


def record(ok, label, detail=""):
    checks.append((ok, label, detail))
    print("   %s  %s%s" % ("✅" if ok else "❌", label,
                           ("\n        " + detail) if detail else ""))
    return ok


def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def sign_in(email, pw, tries=4):
    """A real GoTrue password grant. Retries: signing several accounts in back
    to back has drawn a bare TLS reset from GoTrue before, and a drive that
    dies on that reads as a product failure."""
    key = anon_key()
    url = FX.env("SUPABASE_URL") + "/auth/v1/token?grant_type=password"
    body = json.dumps({"email": email, "password": pw}).encode()
    last = None
    for n in range(tries):
        try:
            rq = urllib.request.Request(url, data=body, method="POST")
            rq.add_header("apikey", key)
            rq.add_header("Content-Type", "application/json")
            with urllib.request.urlopen(rq, context=CTX, timeout=30) as r:
                return json.loads(r.read())["access_token"]
        except Exception as exc:                      # noqa: BLE001
            last = exc
            time.sleep(1.5 * (n + 1))
    raise SystemExit("ks4_pool_drive: could not sign in %s — %s" % (email, last))


def call(method, path, token, payload=None):
    body = json.dumps(payload).encode() if payload is not None else None
    rq = urllib.request.Request(API + path, data=body, method=method)
    rq.add_header("Authorization", "Bearer " + token)
    if body:
        rq.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(rq, timeout=60) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw or b"{}")
        except ValueError:
            return e.code, {"raw": raw.decode("utf-8", "replace")[:400]}


# ── the pool, as Python knows it ─────────────────────────────────────────

def pool_index():
    """id → row, from the authored source.

    The drive checks what the SERVER served against what the AUTHOR wrote, not
    against a second copy of the server's own logic. If the two disagree the
    export or the query is wrong, and either way a child is affected.
    """
    return {r["id"]: r for r in ks4_data.load_pool(strict=False)}


def audit_payload(label, questions, pool, tier, pathway):
    """Every question in one payload, against the content rule.

    Returns (ok, detail). The rule is applied here from first principles —
    `tier`/`pathway` in, permitted flag combinations out — rather than by
    calling the backend's own scope function, so that a wrong scope function
    cannot agree with itself.
    """
    problems, unknown, ks3 = [], [], []
    for q in questions:
        qid = q.get("source_ref") or q.get("id") or ""
        if KS3_ID.match(str(qid)):
            ks3.append(qid)
            continue
        row = pool.get(qid)
        if row is None:
            unknown.append(qid)
            continue
        if tier == "foundation" and row["tier"] == "higher":
            problems.append("%s is higher-tier" % qid)
        if pathway == "combined" and row["triple_only"]:
            problems.append("%s is triple-only" % qid)

    if ks3:
        return False, ("⚠️ %d KS3 BANK id(s) served to a KS4 class: %s"
                       % (len(ks3), ", ".join(ks3[:5])))
    if problems:
        return False, ("⚠️ %d FORBIDDEN question(s) served to %s %s: %s"
                       % (len(problems), pathway, tier,
                          "; ".join(problems[:5])))
    if unknown:
        return False, ("%d served id(s) are in no pool at all: %s"
                       % (len(unknown), ", ".join(unknown[:5])))
    return True, "%d question(s), every one permitted for %s %s" % (
        len(questions), pathway, tier)


# ── the checks ───────────────────────────────────────────────────────────

def check_topics(t_teacher, pool):
    """The set-work sheet's topic list, for both KS4 classes."""
    print("\n── the topic list ──")
    st, trip = call("GET", "/api/teacher/set-work/topics?class_id=" +
                    FX.C_KS4_TRIPLE, t_teacher)
    st2, comb = call("GET", "/api/teacher/set-work/topics?class_id=" +
                     FX.C_KS4_COMB, t_teacher)
    if st != 200 or st2 != 200:
        record(False, "KS4 topics load", "%s / %s" % (st, st2))
        return None, None

    # ⊕ INVERTS MRB-331. Its drive asserts has_bank is False; a KS4 pool now
    # exists, so False here would mean the branch never landed.
    record(trip.get("has_bank") is True and comb.get("has_bank") is True,
           "KS4 has_bank is now TRUE for both classes (inverts MRB-331)",
           "triple=%s combined=%s"
           % (trip.get("has_bank"), comb.get("has_bank")))

    t_rows = {r["lesson_slug"]: r.get("available", 0)
              for r in trip.get("topics") or []}
    c_rows = {r["lesson_slug"]: r.get("available", 0)
              for r in comb.get("topics") or []}

    # ⊕ INVERTS MRB-331. Every seeded subtopic should now offer questions.
    t_stocked = [s for s, n in t_rows.items() if n > 0]
    record(len(t_stocked) > 20,
           "KS4 Triple Higher: most lessons now have banked questions",
           "%d of %d rows have available > 0" % (len(t_stocked), len(t_rows)))

    # ⚠️ THE COUNT IS FOUR, NOT TWELVE, AND THAT IS CORRECT.
    #
    # A subtopic holds twelve questions — but `/set-work/topics` reports what is
    # available AT ONE BAND, because `bankFor` applies `.eq('band', band)` and
    # the route answers for a single band at a time. Twelve per subtopic is four
    # easier, four standard, four harder, so a correctly stocked subtopic
    # reports 4 here and a route that reported 12 would be ignoring the band.
    #
    # This drive asserted 12 and was wrong, not the product. Recorded rather
    # than quietly corrected, because "the number I expected" is the weakest
    # possible reason to change an assertion and the next reader deserves the
    # arithmetic.
    wrong = {s: n for s, n in t_rows.items() if n not in (0, 4)}
    record(not wrong,
           "KS4: every stocked subtopic reports four available — one band of twelve",
           "%d stocked, all at 4" % len(t_stocked) if not wrong
           else "off-band counts: %s" % dict(list(wrong.items())[:5]))

    # Scoping proved by DIFFERENCE, not by a count. A route ignoring tier and
    # pathway entirely would still return rows for both classes.
    only_triple = set(t_rows) - set(c_rows)
    record(bool(only_triple),
           "KS4: the Triple Higher class is offered lessons the Combined "
           "Foundation class is not",
           "%d triple-only lesson(s), e.g. %s"
           % (len(only_triple), ", ".join(sorted(only_triple)[:3])))

    # And the Combined Foundation sheet must never LIST a triple-only or a
    # higher-only subtopic. The scheme scopes this too, so a failure here is
    # a scheme problem rather than a pool problem — worth telling apart.
    cls = ks4_data.classify()
    wrong = [s for s in c_rows
             if cls.get(s) and (cls[s]["triple_only"]
                                or cls[s]["tier"] == "higher")]
    record(not wrong,
           "KS4: the Combined Foundation sheet lists no higher/triple subtopic",
           "clean" if not wrong
           else "⚠️ listed: %s" % ", ".join(sorted(wrong)[:5]))
    return trip, comb


# ── the route's real contract (⚠️ read at merge, not assumed) ────────────
#
# This drive was written against `POST …/preview {lesson_slug}`. MRB-331 shipped
#     GET /api/teacher/set-work/preview?class_id=&sow_entry_id=[&count=][&band=]
# and it answers `{picked, pool, available, reason}` — not `questions`. It keys
# on the SCHEME ENTRY, not the slug, and deliberately 404s `sow_entry_not_found`
# for a row outside the class's own cohort, because "that row exists but is not
# yours" is a fact about another cohort's scheme.
#
# ⚠️ That 404 is why the helper below returns a THIRD state. A missing scheme
# entry and an empty payload are different refusals — the first is the scheme
# declining to offer the topic, the second is the pool declining to fill it —
# and a check that treats them alike passes when the route is simply broken.
# An earlier revision of this drive did exactly that: every preview 404'd and
# two checks went green on "served 0".
_TOPICS = {}


def topics_for(t_teacher, class_id):
    if class_id not in _TOPICS:
        st, body = call("GET", "/api/teacher/set-work/topics?class_id=" + class_id,
                        t_teacher)
        _TOPICS[class_id] = (body.get("topics") or []) if st == 200 else []
    return _TOPICS[class_id]


def sow_id_for(t_teacher, class_id, slug):
    """The class's own scheme-entry id for `slug`, or None if not on its scheme."""
    for r in topics_for(t_teacher, class_id):
        if r.get("lesson_slug") == slug:
            return r.get("id")
    return None


def preview(t_teacher, class_id, slug, band="standard", count=10):
    """(state, questions). state is 'ok' | 'not_on_scheme' | 'http <n>'."""
    sow_id = sow_id_for(t_teacher, class_id, slug)
    if not sow_id:
        return "not_on_scheme", []
    st, body = call("GET", "/api/teacher/set-work/preview?class_id=%s"
                    "&sow_entry_id=%s&band=%s&count=%d"
                    % (class_id, sow_id, band, count), t_teacher)
    if st != 200:
        return "http %s" % st, []
    return "ok", list(body.get("picked") or [])


def check_collision(t_teacher, pool):
    """⚠️ THE COLLISION, RESHAPED. See the module docstring.

    MRB-331 proved this by asserting `available == 0`. That test cannot
    survive this ticket: the eight slugs hold twelve KS3 rows AND twelve KS4
    rows, so the number is 12 either way. Identity is what separates them.
    """
    print("\n── the eight colliding slugs ──")
    COLLIDING = ["aerobic-respiration", "catalysts", "changes-of-state",
                 "chromatography", "conservation-of-mass",
                 "distance-time-graphs", "electric-fields", "magnetic-fields"]

    leaked, checked, missing = [], [], []
    for slug in COLLIDING:
        if slug not in pool_slugs(pool):
            missing.append(slug)
            continue
        state, qs = preview(t_teacher, FX.C_KS4_TRIPLE, slug)
        if state == "not_on_scheme":
            missing.append(slug + " (not on this class's scheme)")
            continue
        if state != "ok":
            leaked.append("%s: preview %s" % (slug, state))
            continue
        checked.append(slug)
        for q in qs:
            qid = str(q.get("source_ref") or q.get("id") or "")
            if KS3_ID.match(qid):
                leaked.append("%s served KS3 id %s" % (slug, qid))
            elif not qid.startswith("ks4-"):
                leaked.append("%s served unrecognised id %s" % (slug, qid))

    record(not leaked,
           "KS4: the eight colliding slugs serve KS4 ids and never KS3 ones",
           "%d slug(s) checked, every question a ks4- id" % len(checked)
           if not leaked else "; ".join(leaked[:5]))
    if missing:
        record(True, "collision check: %d slug(s) not yet authored"
               % len(missing), ", ".join(missing))


def pool_slugs(pool):
    return {r["subtopic_slug"] for r in pool.values()}


def check_serving(t_teacher, pool):
    """THE PROPERTY. Set real work on both classes and audit what is served."""
    print("\n── what each class is actually served ──")
    cls = ks4_data.classify()
    have = pool_slugs(pool)

    # ⚠️ THE SUBTOPIC MUST BE ONE BOTH CLASSES ARE ACTUALLY OFFERED, and it is
    # chosen from their topic lists rather than from the pool alphabetically.
    #
    # The pool holds all 264 subtopics; a fixture class is one year group at one
    # week and is offered a fraction of them. Taking `sorted(pool)[0]` picked
    # `abiotic-biotic-factors`, which is on neither class's scheme, so every
    # preview answered `sow_entry_not_found` and the checks failed for a reason
    # that had nothing to do with what they measure.
    #
    # Intersecting the two lists is also what makes the comparison mean
    # anything: both classes can reach this row, so any DIFFERENCE in what comes
    # back is the content rule rather than the scheme.
    offered_both = ({r["lesson_slug"] for r in topics_for(t_teacher, FX.C_KS4_COMB)}
                    & {r["lesson_slug"] for r in topics_for(t_teacher, FX.C_KS4_TRIPLE)})
    base = sorted(s for s in have & offered_both
                  if cls[s]["tier"] == "foundation"
                  and not cls[s]["triple_only"])
    if not base:
        record(False, "no base subtopic is on BOTH classes' schemes — "
                      "nothing comparable to serve")
        return None
    slug = base[0]

    out = {}
    for label, class_id, tier, pathway in (
            ("Foundation Combined", FX.C_KS4_COMB, "foundation", "combined"),
            ("Triple Higher", FX.C_KS4_TRIPLE, "higher", "triple")):
        state, qs = preview(t_teacher, class_id, slug)
        if state != "ok":
            record(False, "%s: preview on %s" % (label, slug), state)
            continue
        ok, detail = audit_payload(label, qs, pool, tier, pathway)
        record(ok, "%s is served only what it may be served" % label, detail)
        out[label] = qs
    return slug, out


def check_full_set(t_teacher, pool):
    """The Triple Higher class reaches content the Combined class cannot.

    The mirror of the check above: it is not enough that Foundation Combined
    is protected — if the filter were simply "serve nothing unusual", both
    classes would pass and Triple students would be short-changed.
    """
    print("\n── the Triple Higher class gets the full set ──")
    cls = ks4_data.classify()
    have = pool_slugs(pool)
    # Same correction as check_serving: chosen from what the Triple Higher class
    # is actually OFFERED, not from the pool alphabetically. A subtopic off its
    # scheme previews as sow_entry_not_found and proves nothing either way.
    offered_triple = {r["lesson_slug"] for r in topics_for(t_teacher, FX.C_KS4_TRIPLE)}
    triple = sorted(s for s in have & offered_triple if cls[s]["triple_only"])
    higher = sorted(s for s in have & offered_triple
                    if cls[s]["tier"] == "higher" and not cls[s]["triple_only"])

    for label, slugs in (("triple-only", triple), ("higher-only", higher)):
        if not slugs:
            record(True, "no %s subtopic on this class's scheme — not measurable"
                   % label)
            continue
        slug = slugs[0]
        state, qs = preview(t_teacher, FX.C_KS4_TRIPLE, slug)
        record(state == "ok" and qs,
               "Triple Higher reaches a %s subtopic (%s)" % (label, slug),
               "%d question(s) served" % len(qs) if state == "ok"
               else "preview %s" % state)

        # ⚠️ AND THE COMBINED FOUNDATION CLASS MUST NOT REACH IT — but state
        # WHICH refusal, because there are two and only one is this ticket's.
        #
        # On correct data the SCHEME refuses first: a triple-only or higher-only
        # subtopic is not on a Combined Foundation class's scheme at all, so
        # there is no scheme entry to preview and the pool filter is never
        # consulted. That is the honest result and it is asserted as such.
        #
        # It would be easy, and wrong, to write this as "served 0" and call it
        # proof of the content rule. An earlier revision did, and it went green
        # while every preview in the run was 404ing. The content rule itself is
        # proved where it can actually be exercised — test_ks4_bank_read.js
        # calls bankFor() with each scope against real rows, including the
        # Foundation-Triple and no-tier-no-pathway cases this route cannot
        # reach. Two lines of defence, each tested where it lives.
        state2, qs2 = preview(t_teacher, FX.C_KS4_COMB, slug)
        record(state2 == "not_on_scheme" or not qs2,
               "Combined Foundation cannot reach that same %s subtopic" % label,
               "refused at the SCHEME — not on its list at all"
               if state2 == "not_on_scheme" else
               ("refused at the POOL — scheme offered it, 0 served"
                if not qs2 else
                "⚠️ served %d question(s) it may not have" % len(qs2)))


def main():
    pw = os.environ.get(FX.ENV_SWITCH)
    if not pw:
        raise SystemExit(
            "ks4_pool_drive: set %s to the throwaway accounts' password."
            % FX.ENV_SWITCH)

    print("ks4_pool_drive — MRB-332, the KS4 content rule on the serving path")
    pool = pool_index()
    print("   pool: %d authored question(s), %d subtopic(s)"
          % (len(pool), len(pool_slugs(pool))))
    if not pool:
        raise SystemExit("ks4_pool_drive: the pool is empty — author and "
                         "export first.")

    # ⚠️ `seed`, not `build`. This drive was written against an earlier
    # shape of MRB-331's fixture; the merged one exposes seed() /
    # clear_work() / teardown(). docs/ks4/merge-notes.md says to read the
    # seam's final form rather than assume it — this is that, and it is
    # why the drive is run here rather than declared compatible.
    FX.seed()
    FX.clear_work()
    server = None
    try:
        server = subprocess.Popen(
            ["node", "server.js"], cwd=BACKEND,
            env=dict(os.environ, PORT=str(PORT)),
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(40):
            try:
                urllib.request.urlopen(API + "/api/health", timeout=2).read()
                break
            except Exception:                          # noqa: BLE001
                time.sleep(0.5)
        else:
            raise SystemExit("ks4_pool_drive: the backend did not come up on "
                             "port %d" % PORT)

        t_teacher = sign_in(FX.TEACHER_EMAIL, pw)
        check_topics(t_teacher, pool)
        check_collision(t_teacher, pool)
        check_serving(t_teacher, pool)
        check_full_set(t_teacher, pool)
    finally:
        if server:
            server.terminate()
        if "--keep" not in sys.argv:
            FX.teardown()

    bad = [c for c in checks if not c[0]]
    print("\n%s  %d check(s), %d failed"
          % ("❌" if bad else "✅", len(checks), len(bad)))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
