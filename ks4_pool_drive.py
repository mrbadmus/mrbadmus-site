"""ks4_pool_drive.py — MRB-332, ported to Set work v2 (MRB-335). A KS4 teacher
sets work, and the right child gets the right questions.

    MRB_SET_WORK_PASSWORD=<pw> python3 ks4_pool_drive.py --keep
    MRB_SET_WORK_PASSWORD=<pw> MRB_BACKEND=<path> python3 ks4_pool_drive.py --keep

⚠️ REQUIRES THE INTEGRATED BRANCH. It imports `mrb331_fixture`, which arrives
with MRB-331 (`feat/set-work`), and it drives a backend carrying MRB-335's
`/api/teacher/set-work/scope` and `/preview` (`feat/set-work-v2`). Run it after
the rebase, not before; on its own branch it will fail at the import, loudly,
which is the correct behaviour.

⚠️ EVERY CHECK RUNS ON A REAL USER'S JWT against the real TEST project through
a locally-run backend, exactly as `set_work_drive.py` does. Nothing is stubbed.
The service key builds the world and never appears inside a check — a proof
carried on a service-role key proves nothing about what a teacher or a child
can actually do, because service role bypasses RLS.

── WHAT THIS DRIVE EXISTS TO PROVE ─────────────────────────────────────

One property, and it is the one that matters to a child:

    **A Combined class is never served a Triple-only question, whatever tier
    it is set at. A class is served the tier its TEACHER asked for, which is
    not necessarily its own.**

`ks4_pool_check.py` proves the content rule about the DATA. This proves it
about the SERVING PATH — the class row, the tree, the scope seal, the pool
query, RLS and the payload, end to end — because a correct rule and a query
that forgets to apply it look identical from the outside.

── ⊕ MRB-335: THE ONE SEMANTIC CHANGE, AND IT IS THE POINT OF THE PORT ──

This file used to say, and MRB-332's checks used to assume:

    "A Foundation Combined class is never served a Higher or a Triple-only
    question. A Triple Higher class is served everything."

Half of that sentence is still true and half of it is now WRONG, and the wrong
half is kept here rather than deleted because following it would re-open the
hole from the other side — a reader who "fixed" a check back to it would be
asserting that a teacher may not set Foundation revision to a Higher class,
which is ordinary teaching that v1 could not express and v2 exists to allow.

What actually holds under v2 (RISKS E1, C1):

  · **Set work's tier is the REQUEST's tier.** A teacher chooses it per set.
    A Foundation class may legitimately be set Higher extension work; a Higher
    class may legitimately be set Foundation revision. So "this class is
    Foundation, therefore it may not see a Higher row" is no longer a true
    statement about Set work, and every assertion in the old file that said it
    has been retired.
  · **Set work's PATHWAY is always the CLASS's, and cannot be asked for.**
    There is no pathway parameter on any route. That asymmetry is what makes
    `triple_only` unreachable on a combined class no matter what a browser
    posts — the tree is re-derived from the class row and the scope must be a
    node OF THAT TREE, so the refusal happens before the pool is consulted.
  · **The class tier still governs the AUTOMATIC producer** (`ks4BankScope`),
    which is a different question with a different answer, and which reads
    only `bank_position < 12` (RISKS D7). Set work reads every position.

── ⊕ MRB-335: v1's ROUTE AND ITS `sow_entry_id` CONTRACT ARE DELETED ────

Kept, because it names the route this file used to call and a reader who
restored it would be calling a 404. The old text read:

    "This drive was written against `POST …/preview {lesson_slug}`. MRB-331
    shipped `GET /api/teacher/set-work/preview?class_id=&sow_entry_id=`…
    it keys on the SCHEME ENTRY, not the slug, and deliberately 404s
    `sow_entry_not_found` for a row outside the class's own cohort."

`GET /api/teacher/set-work/topics` is GONE, `sow_entry_id` is GONE, and the
scheme of work no longer scopes Set work at all. The refusal that replaces
`sow_entry_not_found` is `400 scope_not_for_class`, and it is a STRONGER
refusal, not a renamed one: the scheme was a list somebody had authored, so a
gap in it refused by accident; the tree is derived from the class's cohort, so
it refuses by construction.

⚠️ The old helper's THIRD state (`not_on_scheme`) is gone with it, and the
lesson that produced it is not. An earlier revision of this drive treated a
404 and an empty payload alike, and two checks went green while every preview
in the run was 404ing. `preview()` below therefore returns the HTTP status and
the parsed body, and every check asserts on the status explicitly — there is
no state in which "the route refused me" can be read as "the rule protected
me".

── ⚠️ MRB-331'S THREE CHECKS: WHAT BECAME OF EACH ──────────────────────

`set_work_drive.py` asserted, correctly for its own branch:

    · `has_bank is False` for a KS4 class
    · every KS4 lesson reports `available == 0`
    · the eight colliding slugs report `available == 0`

⊕ MRB-335: the first two are gone rather than inverted. `has_bank` and the
per-lesson `available` were fields of `/set-work/topics`, and that route no
longer exists; what replaced them is `/scope`, whose tree carries a `counts`
object PER TIER on every node (RISKS C12) because the tier chip must re-count
in place. The property those two checks were reaching for — "the KS4 pool is
real and reachable" — is now proved by the previews actually returning `ks4-`
rows, which is a stronger statement than a non-zero count.

**The third did NOT invert and still has not — it changes shape, and getting
that wrong would re-open the exact hole MRB-331 closed.** The eight colliding
slugs hold twelve KS3 rows each. They now also hold KS4 rows each. So a count
is true whether the route is reading the right table or the wrong one, and a
check on the number proves nothing at all.

What separates them is the IDENTITY of the rows: a KS4 pool id begins `ks4-`
and a KS3 bank id looks like `c1-04-h02`. So the collision check here asserts
that every question served for a colliding slug is a `ks4-` id, and that no
KS3 id appears anywhere in a KS4 payload. That is a property no amount of
counting can fake, and it is the most important assertion in this file.
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
from urllib.parse import quote

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)
sys.path.insert(0, REPO)

try:
    import mrb331_fixture as FX          # noqa: E402  (after chdir)
except ModuleNotFoundError:
    raise SystemExit(
        "ks4_pool_drive: mrb331_fixture is missing.\n"
        "This drive runs on the INTEGRATED branch — MRB-331 (feat/set-work)\n"
        "provides the fixture and the three KS4 classes it needs. Rebase this\n"
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

# The bands, in the order the pool authors them. `standard|harder` is the half
# of the Foundation rows a Higher set may draw — see `permits()`.
HARDER_BANDS = ("standard", "harder")

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


# ── the two v2 routes ────────────────────────────────────────────────────

_SCOPE = {}


def scope(token, class_id, fresh=False):
    """(status, body) for `/scope`. Cached: it is the same answer every time
    for a class and it reads the whole tree's counts, which is 189 slugs on a
    combined class."""
    if fresh or class_id not in _SCOPE:
        _SCOPE[class_id] = call(
            "GET", "/api/teacher/set-work/scope?class_id=" + class_id, token)
    return _SCOPE[class_id]


def preview(token, class_id, tier, kind, ref, count=10, exclude=None):
    """(status, body) for `/preview`.

    ⚠️ RETURNS THE STATUS, ALWAYS, AND NEVER COLLAPSES IT INTO 'no questions'.
    See the docstring: an earlier revision of this file treated a refusal and
    an empty payload alike and went green while every request was 404ing.
    """
    path = ("/api/teacher/set-work/preview?class_id=%s&tier=%s"
            "&scope_kind=%s&scope_ref=%s&count=%d"
            % (class_id, quote(tier), quote(kind), quote(ref), count))
    if exclude:
        path += "&exclude=" + quote(",".join(exclude))
    return call("GET", path, token)


def picked_ids(body):
    return [str(q.get("id") or "") for q in (body.get("picked") or [])]


# ── the pool, as Python knows it ─────────────────────────────────────────

def pool_index():
    """id → row, from the authored source.

    The drive checks what the SERVER served against what the AUTHOR wrote, not
    against a second copy of the server's own logic. If the two disagree the
    export or the query is wrong, and either way a child is affected.
    """
    return {r["id"]: r for r in ks4_data.load_pool(strict=False)}


def pool_slugs(pool):
    return {r["subtopic_slug"] for r in pool.values()}


def permits(row, tier, pathway):
    """PLAN §1's pool spec, as a predicate, applied from first principles.

    ⊕ MRB-335 REWROTE THE TIER HALF OF THIS, and the old one would have failed
    on correct data. It read:

        if tier == "foundation" and row["tier"] == "higher": forbidden

    — i.e. it treated a Higher set as "the higher rows, plus anything". PLAN §1
    is narrower on one side and wider on the other:

        Foundation → `tier='foundation'` rows, ALL THREE BANDS.
        Higher     → `tier='higher'` rows (all bands)
                     ∪ `tier='foundation'` rows in `standard|harder`.

    The second clause is the part worth reading twice, and it is why an audit
    that assumed "Higher = the higher rows" would go red against a correct
    server. A Higher class is not a class that skips the foundation material;
    it is a class that meets it at the harder end. Only 30 of 264 subtopics are
    classified `higher` at all, so excluding foundation rows would leave Higher
    unable to set most of the specification — and including their `easier` band
    would hand a Higher group the four gentlest questions in the topic.

    The PATHWAY half is unchanged and is an INCLUSION, never an exclusion
    (RISKS C6): the day a third content flag appears, an exclusion would admit
    it silently to every class in the school.
    """
    if pathway == "combined" and row["triple_only"]:
        return False, "triple-only"
    if tier == "foundation":
        if row["tier"] != "foundation":
            return False, "higher-tier row in a foundation set"
    else:
        if row["tier"] == "foundation" and row["band"] not in HARDER_BANDS:
            return False, "foundation/%s row in a higher set" % row["band"]
    return True, ""


def audit_payload(label, questions, pool, tier, pathway):
    """Every question in one payload, against the content rule.

    Returns (ok, detail). The rule is applied here from first principles —
    the REQUEST's tier and the CLASS's pathway in, permitted flag combinations
    out — rather than by calling the backend's own scope function, so that a
    wrong scope function cannot agree with itself.

    ⊕ MRB-335: `tier` is now the tier the request ASKED FOR, not the class's
    own. Under v1 the two were the same number and this argument could be read
    either way; under v2 they are independent and reading it as the class's
    would make every legitimate cross-tier set look like a leak.
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
        ok, why = permits(row, tier, pathway)
        if not ok:
            problems.append("%s is %s" % (qid, why))

    if ks3:
        return False, ("⚠️ %d KS3 BANK id(s) served to a KS4 class: %s"
                       % (len(ks3), ", ".join(ks3[:5])))
    if problems:
        return False, ("⚠️ %d FORBIDDEN question(s) served to %s at tier=%s: %s"
                       % (len(problems), pathway, tier, "; ".join(problems[:5])))
    if unknown:
        return False, ("%d served id(s) are in no pool at all: %s"
                       % (len(unknown), ", ".join(unknown[:5])))
    return True, "%d question(s), every one permitted for %s at tier=%s" % (
        len(questions), pathway, tier)


# ── tree helpers ─────────────────────────────────────────────────────────

def tree_slugs(body):
    """slug → topic id, for every child in a `/scope` tree."""
    out = {}
    for topic in body.get("tree") or []:
        for child in topic.get("children") or []:
            out[child["id"]] = topic["id"]
    return out


def tree_topics(body):
    return {t["id"]: t for t in (body.get("tree") or [])}


# ── the checks ───────────────────────────────────────────────────────────

def check_scope(token):
    """`/scope` answers for all three KS4 classes, and its tree is the class's.

    ⊕ MRB-335 REPLACES `check_topics`. That function called
    `GET /api/teacher/set-work/topics`, which no longer exists, and asserted
    `has_bank is True` and `available == 4` per lesson. Both fields are gone
    with the route; see the docstring for what replaced them and why the
    replacement is stronger.
    """
    print("\n── /scope answers, and the tree is the CLASS's ──")
    bodies = {}
    for label, cid in (("Triple Higher biology 10a/Bi1", FX.C_KS4_TRIPLE),
                       ("Combined Foundation 10b/Sc5", FX.C_KS4_COMB),
                       ("Triple Higher physics 10c/Ph1", FX.C_KS4_SEPS)):
        st, body = scope(token, cid)
        record(st == 200 and bool(body.get("tree")),
               "/scope 200 for %s" % label,
               "%d topic(s), %d subtopic(s)"
               % (len(body.get("tree") or []), len(tree_slugs(body)))
               if st == 200 else "HTTP %s %s" % (st, str(body)[:120]))
        bodies[cid] = body if st == 200 else {}

    cls = ks4_data.classify()
    comb = bodies.get(FX.C_KS4_COMB) or {}
    trip = bodies.get(FX.C_KS4_TRIPLE) or {}
    seps = bodies.get(FX.C_KS4_SEPS) or {}

    # ── RISKS C6 — the Combined tree holds no triple-only subtopic ────────
    #
    # Measured against `ks4_data.classify()`, the AUTHORED classification, not
    # against the backend's mirrored tree — the mirror is the thing under test.
    comb_slugs = tree_slugs(comb)
    leaked = sorted(s for s in comb_slugs
                    if cls.get(s) and cls[s]["triple_only"])
    record(comb_slugs and not leaked,
           "RISKS C6: the Combined tree contains NO triple_only subtopic",
           "%d subtopic(s), none triple-only" % len(comb_slugs)
           if not leaked else "⚠️ leaked: %s" % ", ".join(leaked[:6]))

    # ── RISKS C7 — `space` is absent from the Combined tree entirely ──────
    #
    # Not "space has no children" — ABSENT. All five of its subtopics are
    # triple-only, so a tree that pruned children but kept the topic would show
    # a teacher a topic they can never set anything on.
    record("space" not in tree_topics(comb),
           "RISKS C7: the topic `space` is absent from the Combined tree",
           "not present at all"
           if "space" not in tree_topics(comb)
           else "⚠️ present with %d child(ren)"
                % len(tree_topics(comb)["space"].get("children") or []))

    # And the mirror: the Triple class DOES see triple-only content, or the
    # filter is simply "serve nothing unusual" and Triple pupils are short-
    # changed by a check that would pass either way.
    trip_slugs = tree_slugs(trip)
    trip_only = sorted(s for s in trip_slugs
                       if cls.get(s) and cls[s]["triple_only"])
    record(bool(trip_only),
           "the Triple tree DOES contain triple_only subtopics",
           "%d of %d, e.g. %s" % (len(trip_only), len(trip_slugs),
                                  ", ".join(trip_only[:3])))

    # ── RISKS C5 — a separate-sciences class sees ONE science ─────────────
    for label, body, want in (("10a/Bi1", trip, "biology"),
                              ("10c/Ph1", seps, "physics")):
        subs = {t.get("subject") for t in (body.get("tree") or [])}
        record(subs == {want} and body.get("subjects") == [want],
               "RISKS C5: %s sees %s and nothing else" % (label, want),
               "tree subjects=%s, subjects=%s"
               % (sorted(subs), body.get("subjects")))

    comb_subs = {t.get("subject") for t in (comb.get("tree") or [])}
    record(comb_subs == {"biology", "chemistry", "physics"}
           and sorted(comb.get("subjects") or []) ==
           ["biology", "chemistry", "physics"],
           "the Combined class sees all three sciences",
           "tree subjects=%s, subjects=%s"
           % (sorted(comb_subs), comb.get("subjects")))

    # ── ⊕ MRB-336, 8 Sep 2026 — PAPERS ARE NOT A COMBINED-ONLY CHIP ──────
    #
    # ⛔ This check used to read:
    #
    #     # Papers are a combined-only chip (RISKS C8 / PLAN §4).
    #     record(comb.get("papers") == [1, 2] and trip.get("papers") is None
    #            and seps.get("papers") is None,
    #            "papers: [1,2] on Combined, null on both Triple classes", …)
    #
    # It is kept, rather than deleted, because it is a check that PASSED while
    # describing a defect, and a reader meeting the new assertion cold would
    # otherwise have no way to tell which of the two readings is the mistake.
    #
    # The old comment carried the whole error in four words. AQA examines the
    # separate sciences on two papers per science, exactly as Trilogy is
    # examined on two per science — Biology Paper 1 and Biology Paper 2 are
    # real papers with real dates. Withholding the chip from Triple meant the
    # one cohort whose teachers most often revise BY PAPER ("everything on
    # paper 1 before the mock") was the only cohort that could not filter by
    # it. Mide called it "a simple fix" and it is: `papersFor` returns [1, 2]
    # for every KS4 class and null only at KS3.
    #
    # ⚠️ THE TREE NEVER HAD THIS BUG — only the OFFER did. `treeForClass` has
    # stamped `paper` on every KS4 topic from `KS4_PAPER` since it was written,
    # with no pathway branch anywhere near it, so a triple class's tree already
    # carried the paper on every topic it could see and the chips were simply
    # not offered. That is why the fix is one line and why the assertion below
    # tests the OFFER (`papers`) and the TREE (`paper` per topic) separately:
    # they were never the same fact, and a future regression could break either
    # one without the other.
    record(comb.get("papers") == [1, 2] and trip.get("papers") == [1, 2]
           and seps.get("papers") == [1, 2],
           "papers: [1,2] on Combined AND on both Triple classes — AQA "
           "examines the separate sciences on two papers per science too",
           "combined=%s triple=%s seps=%s"
           % (comb.get("papers"), trip.get("papers"), seps.get("papers")))

    # ── ⊕ MRB-336 · `space` IS THE CASE THAT COMES OUT RIGHT BOTH WAYS ────
    #
    # All five of `space`'s subtopics are `triple_only`, which makes it the
    # only topic in the curriculum that exercises both halves of the change at
    # once, and the two halves pull in opposite directions:
    #
    #   · on TRIPLE PHYSICS it is in the tree and must now carry a paper 2
    #     chip — it is examined on physics paper 2, and before today a Triple
    #     Physics teacher revising by paper could not reach it by paper;
    #   · on COMBINED it is dropped from the tree entirely (RISKS C7, asserted
    #     above), so there is no topic there to carry a chip at all.
    #
    # A one-line `papersFor` change cannot distinguish those, and neither can
    # a check that only reads the class-level `papers` list. This reads the
    # PER-TOPIC stamp on the node itself.
    seps_topics = tree_topics(seps)
    space = seps_topics.get("space")
    record(space is not None and space.get("paper") == 2,
           "⊕ MRB-336: `space` is on the Triple Physics tree AND carries "
           "paper 2 — the topic the combined tree cannot see is examined on "
           "physics paper 2, and now says so",
           "paper=%r, %d subtopic(s)"
           % ((space or {}).get("paper"), len((space or {}).get("children") or []))
           if space else "⚠️ `space` is not on the Triple Physics tree at all")

    # …and every KS4 topic a teacher is offered carries a paper, on every
    # cohort. A chip rail is only usable if the partition is total: one topic
    # with `paper: null` is a topic that vanishes from both filters.
    unpapered = []
    for label, body in (("combined", comb), ("triple bio", trip),
                        ("triple phys", seps)):
        for tid, topic in tree_topics(body).items():
            if topic.get("paper") not in (1, 2):
                unpapered.append("%s/%s=%r" % (label, tid, topic.get("paper")))
    record(not unpapered,
           "⊕ MRB-336: every KS4 topic on every cohort's tree carries paper 1 "
           "or paper 2 — the chip rail partitions the tree, it does not "
           "sample it",
           "%d topic(s) across three cohorts, all papered"
           % sum(len(tree_topics(b)) for b in (comb, trip, seps))
           if not unpapered else "UNPAPERED: %s" % unpapered[:6])

    # ── RISKS C11 — the default tier is the class-NAME rule's answer ──────
    #
    # ⚠️ THIS IS THE ONE PLACE THE CLASS'S OWN TIER STILL SHOWS UP IN SET WORK,
    # and it is a DEFAULT, not a constraint. `defaultTierFor()` lands the sheet
    # on the tier the teacher usually wants; every check below then proves that
    # the teacher can move off it. Confusing the two is exactly the error this
    # port exists to remove.
    want = {FX.C_KS4_COMB: ("10b/Sc5", "foundation"),
            FX.C_KS4_TRIPLE: ("10a/Bi1", "higher"),
            FX.C_KS4_SEPS: ("10c/Ph1", "higher")}
    bad = []
    for cid, (name, tier) in want.items():
        got = ((bodies.get(cid) or {}).get("class") or {}).get("default_tier")
        if got != tier:
            bad.append("%s wanted %s got %s" % (name, tier, got))
    record(not bad,
           "RISKS C11: default_tier matches the class-name rule on all three",
           "10b/Sc5=foundation, 10a/Bi1=higher, 10c/Ph1=higher"
           if not bad else "; ".join(bad))

    return bodies


def check_request_tier(token, pool, bodies):
    """⊕ MRB-335, RISKS E1/C1. THE TIER IS THE REQUEST'S, NOT THE CLASS'S.

    This check replaces MRB-332's `check_serving` half that read the class row
    to decide what was allowed. Under v1 that was right; under v2 it is the
    defect. A teacher chooses the tier per set, so a Foundation class being
    asked for Higher extension and a Higher class being asked for Foundation
    revision are both ORDINARY, and a drive that refused either would be
    asserting v1's contract against v2's product.
    """
    print("\n── the tier is the REQUEST's, not the class's ──")
    cls = ks4_data.classify()
    comb = bodies.get(FX.C_KS4_COMB) or {}
    comb_slugs = tree_slugs(comb)
    have = pool_slugs(pool)

    # A subtopic the COMBINED FOUNDATION class can reach that is classified
    # `higher` — 11 of them exist and none is triple-only. It is the sharpest
    # possible instrument: at tier=foundation its pool is empty, at tier=higher
    # it is full, and the only thing that moved is the query parameter.
    higher_slugs = sorted(s for s in comb_slugs
                          if s in have and cls[s]["tier"] == "higher")
    if not higher_slugs:
        record(False, "no higher-tier subtopic on the Combined tree — "
                      "the request-tier property is not measurable")
        return
    slug = higher_slugs[0]

    st_f, b_f = preview(token, FX.C_KS4_COMB, "foundation", "subtopic", slug)
    st_h, b_h = preview(token, FX.C_KS4_COMB, "higher", "subtopic", slug)

    record(st_f == 200 and st_h == 200,
           "a FOUNDATION class may be asked for HIGHER work — both 200 on %s"
           % slug,
           "foundation=%s (%d served), higher=%s (%d served)"
           % (st_f, len(b_f.get("picked") or []),
              st_h, len(b_h.get("picked") or [])))

    # The two requests draw from DIFFERENT pools, proved by a row the
    # foundation pool cannot contain: PLAN §1's Foundation clause is
    # `tier='foundation'` rows only, so any `tier='higher'` row served here is
    # outside it by construction.
    extra = [i for i in picked_ids(b_h)
             if pool.get(i) and pool[i]["tier"] == "higher"]
    record(bool(extra),
           "the higher request serves rows the foundation pool cannot hold",
           "%d of %d served row(s) are tier='higher', e.g. %s"
           % (len(extra), len(picked_ids(b_h)), ", ".join(extra[:3]))
           if extra else "⚠️ nothing outside the foundation pool was served")

    # And the foundation request on that same subtopic serves nothing, because
    # every row it has is higher-tier. `short` says so rather than an error:
    # a tier with an empty pool is a legitimate answer, not a refusal.
    record(st_f == 200 and not (b_f.get("picked") or []),
           "…and the same subtopic at tier=foundation serves nothing at all",
           "available=%s short=%s — the request tier, not the class, emptied it"
           % (b_f.get("available"), b_f.get("short")))

    # ── the mirror: a HIGHER class asked for FOUNDATION revision ──────────
    trip = bodies.get(FX.C_KS4_TRIPLE) or {}
    base = sorted(s for s in tree_slugs(trip)
                  if s in have and cls[s]["tier"] == "foundation")
    if base:
        st, body = preview(token, FX.C_KS4_TRIPLE, "foundation",
                           "subtopic", base[0])
        ids = picked_ids(body)
        wrong = [i for i in ids
                 if not (pool.get(i) and pool[i]["tier"] == "foundation")]
        record(st == 200 and ids and not wrong,
               "a HIGHER class may be asked for FOUNDATION revision (10a/Bi1)",
               "HTTP %s, %d served on %s, every one a tier='foundation' row"
               % (st, len(ids), base[0]) if not wrong
               else "⚠️ %s served: %s" % (st, ", ".join(wrong[:4])))
    else:
        record(False, "no foundation-tier subtopic on 10a/Bi1's tree")

    # ── RISKS C1 — a tier that is not this key stage's is refused ─────────
    #
    # `easy|medium|hard` are the KS3 difficulties. They are real tier values
    # SOMEWHERE, which is what makes them the right thing to post: a validator
    # that merely checked the string against a global list would accept them.
    bad = []
    for t in ("easy", "medium", "hard"):
        st, body = preview(token, FX.C_KS4_COMB, t, "subtopic", slug)
        if st != 400 or body.get("error") != "bad_tier":
            bad.append("%s → %s %s" % (t, st, body.get("error")))
    record(not bad,
           "RISKS C1: a KS3 tier on a KS4 class is 400 bad_tier",
           "easy/medium/hard all refused" if not bad else "; ".join(bad))


def check_pathway_is_the_class(token, pool, bodies):
    """⊕ MRB-335, RISKS C6. THE PATHWAY IS THE CLASS'S AND CANNOT BE ASKED FOR.

    ⚠️ THE REFUSAL IS AT THE SCOPE, NOT AT THE POOL, AND THAT IS STRONGER.

    There is no pathway parameter on any Set work route. `swReadPreamble` calls
    `SW.findScope(cls, kind, ref)`, which walks a tree RE-DERIVED FROM THE
    CLASS ROW, so a triple-only slug is not a node of a combined class's tree
    and the request is refused before a single bank row is read.

    Why that is stronger than a pool filter that returns zero rows:

      · A pool filter has to be correct in every read path — count, preview,
        swap and the write — and the day one of them forgets it, the leak is
        silent. The scope seal is ONE function that all four go through.
      · A filter that returns zero looks identical to a filter that found
        nothing, so "0 served" is not evidence. `400 scope_not_for_class` is a
        statement the server made on purpose.
      · The refusal survives content changes. If someone later authored a
        foundation-band row against a triple-only slug, a tier filter would let
        it through and the scope seal still would not.

    This is the same reasoning MRB-332 wrote about the SCHEME refusing first —
    kept, because the shape of the argument survived even though the mechanism
    did not. The scheme refused by accident (a gap in what somebody had
    authored); the tree refuses by construction (a fact about the cohort).
    """
    print("\n── the pathway is the CLASS's, and cannot be asked for ──")
    cls = ks4_data.classify()
    have = pool_slugs(pool)
    trip_slugs = tree_slugs(bodies.get(FX.C_KS4_TRIPLE) or {})

    # A BIOLOGY triple-only subtopic — 10a/Bi1 is triple biology and sees only
    # biology, so a chemistry or physics slug would be refused for the wrong
    # reason (RISKS C5's subject rule) and prove nothing about the pathway.
    only = sorted(s for s in trip_slugs
                  if s in have and cls[s]["triple_only"])
    if not only:
        record(False, "no triple-only biology subtopic in the pool — "
                      "the pathway seal is not measurable")
        return
    slug = only[0]

    st, body = preview(token, FX.C_KS4_COMB, "higher", "subtopic", slug)
    record(st == 400 and body.get("error") == "scope_not_for_class",
           "a triple-only slug posted to the Combined class is refused",
           "HTTP %s %s on %s — refused at the SCOPE, not at the pool"
           % (st, body.get("error"), slug))

    # ⚠️ AND AT EVERY TIER. The seal must not be reachable by moving the one
    # parameter a teacher CAN choose: if `tier=foundation` let the slug
    # through, the pathway would be asked for by proxy.
    st2, body2 = preview(token, FX.C_KS4_COMB, "foundation", "subtopic", slug)
    record(st2 == 400 and body2.get("error") == "scope_not_for_class",
           "…and moving the tier chip does not unlock it",
           "tier=foundation → HTTP %s %s" % (st2, body2.get("error")))

    # The mirror. Without it, "refuse everything" would pass.
    st3, body3 = preview(token, FX.C_KS4_TRIPLE, "higher", "subtopic", slug)
    ids = picked_ids(body3)
    record(st3 == 200 and bool(ids),
           "the Triple class previews that same slug with questions",
           "HTTP %s, %d served on %s" % (st3, len(ids), slug))


def check_audience_audit(token, pool, bodies):
    """The audience audit: four (pathway, requested tier) audiences, on real
    payloads, against PLAN §1's pool spec.

    ⊕ MRB-335: v1 read the class's tier here and had one audience per class.
    v2 has one audience per (class pathway × requested tier), which is four —
    the same four `ks4_pool_check.py` measures on the data, now measured on the
    serving path.
    """
    print("\n── the four audiences, on what is actually served ──")
    cls = ks4_data.classify()
    have = pool_slugs(pool)

    for label, cid, pathway in (("Combined 10b/Sc5", FX.C_KS4_COMB, "combined"),
                                ("Triple 10a/Bi1", FX.C_KS4_TRIPLE, "triple")):
        slugs = tree_slugs(bodies.get(cid) or {})
        # A BASE subtopic — foundation-tier and not triple-only — because it is
        # the only kind both tiers can legitimately draw from, so a difference
        # between the two payloads is the tier rule and nothing else.
        base = sorted(s for s in slugs if s in have
                      and cls[s]["tier"] == "foundation"
                      and not cls[s]["triple_only"])
        if not base:
            record(False, "%s: no base subtopic on its tree" % label)
            continue
        slug = base[0]
        for tier in ("foundation", "higher"):
            st, body = preview(token, cid, tier, "subtopic", slug, count=20)
            if st != 200:
                record(False, "%s at tier=%s on %s" % (label, tier, slug),
                       "HTTP %s %s" % (st, str(body)[:120]))
                continue
            ok, detail = audit_payload(label, body.get("picked") or [],
                                       pool, tier, pathway)
            record(ok, "%s at tier=%s is served only what it may be served"
                   % (label, tier), detail)

        # ⚠️ AND THE TWO TIERS ARE NOT THE SAME SET. PLAN §1's Higher clause
        # excludes the `easier` band of the foundation rows, which is the whole
        # of the difference on a base subtopic — so a server that ignored the
        # tier entirely would pass both audits above and fail this one.
        st, b_h = preview(token, cid, "higher", "subtopic", slug, count=20)
        st2, b_f = preview(token, cid, "foundation", "subtopic", slug, count=20)
        h_bands = {q.get("band") for q in (b_h.get("picked") or [])}
        f_bands = {q.get("band") for q in (b_f.get("picked") or [])}
        record("easier" not in h_bands and "easier" in f_bands,
               "%s: a higher set draws no `easier` band, a foundation set does"
               % label,
               "higher bands=%s, foundation bands=%s, available %s vs %s"
               % (sorted(h_bands), sorted(f_bands),
                  b_h.get("available"), b_f.get("available")))


def check_topic_scope(token, pool, bodies):
    """RISKS C14. A topic-level set spreads across its subtopics.

    Round-robin is the whole reason to offer a topic scope at all: a set drawn
    slug by slug puts the first eight questions on one subtopic, which is what
    a teacher gets if the code walks the children in order.
    """
    print("\n── a topic scope spreads across its subtopics ──")
    have = pool_slugs(pool)
    body = bodies.get(FX.C_KS4_COMB) or {}
    cand = [t for t in (body.get("tree") or [])
            if len([c for c in t.get("children") or [] if c["id"] in have]) > 1]
    if not cand:
        record(False, "no topic on the Combined tree has two stocked subtopics")
        return
    topic = cand[0]
    st, b = preview(token, FX.C_KS4_COMB, "foundation", "topic",
                    topic["id"], count=10)
    slugs = {q.get("subtopic") or q.get("slug")
             for q in (b.get("picked") or [])}
    stocked = len([c for c in topic["children"] if c["id"] in have])
    record(st == 200 and len(slugs) > 1,
           "RISKS C14: 10 questions on topic `%s` span more than one subtopic"
           % topic["id"],
           "HTTP %s, %d question(s) across %d of %d stocked subtopic(s): %s"
           % (st, len(b.get("picked") or []), len(slugs), stocked,
              ", ".join(sorted(s for s in slugs if s)[:4])))

    ok, detail = audit_payload("topic scope", b.get("picked") or [], pool,
                               "foundation", "combined")
    record(ok, "…and every one of them is permitted for combined/foundation",
           detail)


def check_collision(token, pool, bodies):
    """⚠️ THE COLLISION, RESHAPED FOR v2. See the module docstring.

    MRB-331 proved this by asserting `available == 0`. That test cannot survive
    the KS4 pool existing: the eight slugs hold twelve KS3 rows AND a full set
    of KS4 rows, so the number is the same whichever table is read. IDENTITY is
    what separates them, and identity is what is asserted here.

    ⊕ MRB-335 — WHICH CLASS EACH SLUG IS DRIVEN AGAINST, AND WHY IT IS NOT
    ALWAYS THE TRIPLE ONE.

    v1 drove all eight against `10a/Bi1`, because v1's scope came from the
    scheme of work and the scheme carried whatever somebody had authored. v2's
    scope is the class's own tree, and `10a/Bi1` is triple BIOLOGY: seven of
    the eight slugs are chemistry or physics and are simply not nodes of its
    tree, so seven of the eight would answer `400 scope_not_for_class` and the
    check would go green having measured one slug.

    So each slug is driven against the class whose tree actually contains it —
    six non-triple-only slugs on the Combined class, `aerobic-respiration` on
    either, and `electric-fields` (triple-only physics) on `10c/Ph1`, which is
    the only class in the fixture that can reach it. The assertion is unchanged
    and the coverage is now eight of eight rather than one of eight.
    """
    print("\n── the eight colliding slugs ──")
    COLLIDING = ["aerobic-respiration", "catalysts", "changes-of-state",
                 "chromatography", "conservation-of-mass",
                 "distance-time-graphs", "electric-fields", "magnetic-fields"]

    cls = ks4_data.classify()
    have = pool_slugs(pool)
    trees = {cid: tree_slugs(bodies.get(cid) or {})
             for cid in (FX.C_KS4_COMB, FX.C_KS4_TRIPLE, FX.C_KS4_SEPS)}
    names = {FX.C_KS4_COMB: "10b/Sc5", FX.C_KS4_TRIPLE: "10a/Bi1",
             FX.C_KS4_SEPS: "10c/Ph1"}

    leaked, checked, missing = [], [], []
    for slug in COLLIDING:
        if slug not in have:
            missing.append(slug + " (not in the KS4 pool)")
            continue
        # The first class whose tree holds it. Combined first, because it is
        # the widest tree in the fixture — all three sciences, everything that
        # is not triple-only.
        cid = next((c for c in (FX.C_KS4_COMB, FX.C_KS4_TRIPLE, FX.C_KS4_SEPS)
                    if slug in trees[c]), None)
        if cid is None:
            missing.append(slug + " (on no fixture class's tree)")
            continue
        # The tier the slug's own rows are authored at, so the pool is not
        # empty for a reason that has nothing to do with the collision.
        tier = "higher" if cls[slug]["tier"] == "higher" else "foundation"
        st, body = preview(token, cid, tier, "subtopic", slug, count=20)
        if st != 200:
            leaked.append("%s on %s: preview HTTP %s %s"
                          % (slug, names[cid], st, body.get("error")))
            continue
        ids = picked_ids(body)
        if not ids:
            leaked.append("%s on %s: 200 but nothing served — a count check "
                          "would have passed here" % (slug, names[cid]))
            continue
        checked.append("%s/%s" % (slug, names[cid]))
        for qid in ids:
            if KS3_ID.match(qid):
                leaked.append("%s served KS3 id %s" % (slug, qid))
            elif not qid.startswith("ks4-"):
                leaked.append("%s served unrecognised id %s" % (slug, qid))

    record(not leaked,
           "KS4: the eight colliding slugs serve KS4 ids and never KS3 ones",
           "%d slug(s) checked, every question a ks4- id" % len(checked)
           if not leaked else "; ".join(leaked[:5]))
    if missing:
        record(True, "collision check: %d slug(s) not reachable"
               % len(missing), ", ".join(missing))


def main():
    pw = os.environ.get(FX.ENV_SWITCH)
    if not pw:
        raise SystemExit(
            "ks4_pool_drive: set %s to the throwaway accounts' password."
            % FX.ENV_SWITCH)

    print("ks4_pool_drive — MRB-335, the KS4 content rule on Set work v2's "
          "serving path")
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
    #
    # ⊕ MRB-335: `clear_work()` IS NO LONGER CALLED, deliberately. This drive
    # sets no work — every check is a GET — so it needs no empty slate, and
    # `clear_work()` deletes the assignments of every fixture class, which
    # during MRB-335 is a world three lanes share. Deleting a colleague's rows
    # out from under a running drive would make their red look like a product
    # failure. The only thing leftover history changes here is which questions
    # `pickRoundRobin` prefers, and every assertion below is about which
    # questions are PERMITTED, never about which were chosen.
    FX.seed()
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
        bodies = check_scope(t_teacher)
        check_request_tier(t_teacher, pool, bodies)
        check_pathway_is_the_class(t_teacher, pool, bodies)
        check_audience_audit(t_teacher, pool, bodies)
        check_topic_scope(t_teacher, pool, bodies)
        check_collision(t_teacher, pool, bodies)
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
