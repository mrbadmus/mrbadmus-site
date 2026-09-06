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

BACKEND = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend"
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
    url = FX.SUPABASE_URL + "/auth/v1/token?grant_type=password"
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

    # The count itself, where the pool is complete: twelve per subtopic.
    twelves = [s for s, n in t_rows.items() if n == 12]
    record(bool(twelves),
           "KS4: subtopics report twelve available",
           "%d subtopic(s) at exactly 12" % len(twelves))

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
        st, prev = call("POST", "/api/teacher/set-work/preview", t_teacher,
                        {"class_id": FX.C_KS4_TRIPLE, "lesson_slug": slug,
                         "band": "standard"})
        if st != 200:
            leaked.append("%s: preview %s" % (slug, st))
            continue
        qs = prev.get("questions") or []
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

    # A subtopic BOTH classes are taught, so the two payloads are comparable
    # and any difference is the content rule rather than the scheme.
    base = sorted(s for s in have
                  if cls[s]["tier"] == "foundation"
                  and not cls[s]["triple_only"])
    if not base:
        record(False, "no base subtopic is authored yet — nothing to serve")
        return None
    slug = base[0]

    out = {}
    for label, class_id, tier, pathway in (
            ("Foundation Combined", FX.C_KS4_COMB, "foundation", "combined"),
            ("Triple Higher", FX.C_KS4_TRIPLE, "higher", "triple")):
        st, prev = call("POST", "/api/teacher/set-work/preview", t_teacher,
                        {"class_id": class_id, "lesson_slug": slug,
                         "band": "standard"})
        if st != 200:
            record(False, "%s: preview on %s" % (label, slug),
                   "HTTP %s %s" % (st, prev))
            continue
        qs = prev.get("questions") or []
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
    triple = sorted(s for s in have if cls[s]["triple_only"])
    higher = sorted(s for s in have
                    if cls[s]["tier"] == "higher" and not cls[s]["triple_only"])

    for label, slugs in (("triple-only", triple), ("higher-only", higher)):
        if not slugs:
            record(True, "no %s subtopic authored yet — not measurable"
                   % label)
            continue
        slug = slugs[0]
        st, prev = call("POST", "/api/teacher/set-work/preview", t_teacher,
                        {"class_id": FX.C_KS4_TRIPLE, "lesson_slug": slug,
                         "band": "standard"})
        served = len(prev.get("questions") or []) if st == 200 else 0
        record(st == 200 and served > 0,
               "Triple Higher reaches a %s subtopic (%s)" % (label, slug),
               "%d question(s) served" % served if st == 200
               else "HTTP %s" % st)

        # And the Combined Foundation class must be REFUSED the same subtopic.
        st2, prev2 = call("POST", "/api/teacher/set-work/preview", t_teacher,
                          {"class_id": FX.C_KS4_COMB, "lesson_slug": slug,
                           "band": "standard"})
        served2 = len(prev2.get("questions") or []) if st2 == 200 else 0
        record(served2 == 0,
               "Combined Foundation is refused that same %s subtopic" % label,
               "served %d — refusal reason %r"
               % (served2, prev2.get("reason")) if served2 == 0
               else "⚠️ served %d question(s) it may not have" % served2)


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

    FX.build()
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
