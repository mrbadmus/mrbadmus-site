"""set_work_drive.py — MRB-335. A teacher picks a TOPIC, and the right child
gets the right questions.

    MRB_SET_WORK_PASSWORD=<pw> python3 set_work_drive.py
    MRB_SET_WORK_PASSWORD=<pw> python3 set_work_drive.py --keep    # leave the world
    MRB_SET_WORK_PASSWORD=<pw> python3 set_work_drive.py --api-only # no browser
    MRB_SET_WORK_PASSWORD=<pw> python3 set_work_drive.py --shots DIR

⚠️ EVERY CHECK HERE RUNS ON A REAL USER'S JWT AGAINST THE REAL TEST PROJECT,
through a locally-run backend and, for the sheet, a real headless browser.
Nothing is stubbed, and nothing is proved on a service-role key: service role
bypasses RLS entirely, so a proof carried on one proves nothing about what a
teacher or a child can actually do. The service key appears in exactly one
place — `mrb331_fixture.py`, to build and tear down the world — and never
inside a check.

── ⊕ MRB-335 REWROTE THIS FILE, AND EVERY v1 SCHEME ASSERTION IS RETIRED ──

v1 (MRB-331) asked a teacher to pick a SCHEME OF WORK ROW, and this drive was
written around that: `sow_entry_id`, `/api/teacher/set-work/topics`,
`pick_lesson()` choosing "a lesson with enough scheme BEHIND it to fill from",
`released_now`, `held_until`. All of it described a contract that MRB-335
DELETED. Keeping any of it would not have produced a red — it would have
produced a drive that 404s in a corner and reports on a product nobody ships.

What replaced it is a different question, so these are different checks:

    v1: "is this scheme row's lesson allowed, and can the pool fill it"
    v2: "is this NODE OF THE CURRICULUM in THIS CLASS'S TREE, at a tier the
         teacher chose, from a pool scoped by the class's own pathway"

⚠️ THE TIER MOVED SIDES, AND IT IS THE SINGLE MOST IMPORTANT THING IN HERE.
Under v1 the class's tier governed what Set work served. Under v2:

    Set work's TIER    = the REQUEST's, chosen per set. A Foundation class
                         being set Higher extension, and a Higher class being
                         set Foundation revision, are both ordinary teaching.
    Set work's PATHWAY = the CLASS's, always, and cannot be asked for. It is
                         what makes a `triple_only` question unreachable on a
                         combined class.
    AUTO composition   = unchanged. Its tier IS the class's tier, and it reads
                         only `bank_position < 12` (RISKS D7).

── WHY A DRIVE AND NOT A UNIT TEST ────────────────────────────────────

Every property MRB-335 has to establish is a seam between things that are
individually fine, and none of them is visible from either side alone:

  · a tree filtered correctly and a POOL query that forgets the same filter
    look identical from the outside;
  · a sheet that offers only what a class may have proves nothing about what
    the WRITE accepts, and the write is the only thing a crafted request meets;
  · the scroll-jump that made v1's sheet unusable is a property of the RENDERER,
    not of any string in the file — it can only be measured by scrolling;
  · "the release instant round-trips through the BST boundary" needs a real
    `Intl` in a real browser at one end and a real timestamptz at the other.

Every check name below is a row in `docs/mrb335/RISKS.md`.
"""

import argparse
import json
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)
sys.path.insert(0, REPO)

import mrb331_fixture as FX          # noqa: E402  (after chdir, deliberately)
import ks3_browser as cdp            # noqa: E402
import ks4_data                      # noqa: E402

# ⚠️ THE CHECKOUT THIS DRIVE LAUNCHES `node server.js` FROM (⊕ MRB-331,
# 7 Sep 2026). `Server` below already insists it must be "THIS REPO'S BACKEND
# AND THIS RUN'S CODE" — and then hardwired the MAIN checkout, which is a
# shared working copy that any session can leave on any branch. On 7 September
# it was on a colleague's feat/mrb332-ks4-pool, so the drive would have started
# THEIR server and reported fifty-four green checks about code this branch does
# not contain. Set MRB_BACKEND (or pass a path) to name the worktree actually
# being shipped; the sibling repo stays the default.
BACKEND = (
    (sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None)
    or os.environ.get("MRB_BACKEND")
    or "/Users/midebadmus/Documents/GitHub/mrbadmus---backend"
)
PORT = 5531
SITE_PORT = 5533
API = "http://127.0.0.1:%d" % PORT
# ⚠️ THE PAGE MUST REACH THE BACKEND ON `localhost`, NOT `127.0.0.1`, AND THE
# TWO ARE NOT INTERCHANGEABLE HERE. `shared/config.js` only honours `?api=` when
# `location.hostname` is `localhost` or `127.0.0.1`, and the backend's CORS
# allowlist names ORIGINS — `http://localhost:5500` is on it and
# `http://127.0.0.1:5500` is not. A mismatch fails in the worst possible way:
# the request goes out, the browser drops the RESPONSE, and the sheet reports
# the same "Unavailable" it would show for a backend that was down.
PAGE_API = "http://localhost:%d" % PORT
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

# ⚠️ ONE CLOCK, READ ONCE, USED EVERYWHERE. The drive sets work, then asks
# whether it released; both questions are about the same instant. Reading
# `now()` twice a few hundred milliseconds apart is how a check that is about
# "before or after the hold" starts failing once a month at a boundary.
NOW = datetime.now(timezone.utc)
DUE = NOW + timedelta(days=7)

# ⚠️ THE HELD SCHOOL NEEDS A LATER DUE DATE THAN THE OPEN ONE, and the reason
# is a property worth keeping rather than a wrinkle to work around: the hold
# pushes RELEASE forward, and the backend refuses `due_at` that falls before
# release. The fixture's hold is 8 days out, so a due date of NOW + 7 is
# legitimately refused there. `check_hold` asserts that refusal deliberately
# and then uses a date that clears the hold.
DUE_HELD = NOW + timedelta(days=21)

TITLE = "MRB-335 drive"          # every title this drive writes starts here
checks = []
made_assignments = []            # every assignment id this drive creates


def record(ok, label, detail=""):
    checks.append((bool(ok), label, detail))
    print("   %s  %s%s" % ("✅" if ok else "❌", label,
                           ("\n        " + str(detail)[:400]) if detail else ""))
    return bool(ok)


def anon_key():
    """The TEST project's anon key, read out of the page config rather than
    typed — the same source `teacher_admin_real_drive.py` uses."""
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def sign_in(email, pw, tries=4):
    """A real GoTrue password grant. Returns the whole session.

    ⚠️ IT RETRIES, AND THAT IS NOT PADDING. Four accounts sign in back to back
    at the top of this drive, and GoTrue answered the third with a bare TLS
    `UNEXPECTED_EOF_WHILE_READING` — no status, no body, just a dropped
    handshake. A gate that goes red on somebody else's transient network is a
    gate people learn to re-run rather than read, and a gate people re-run
    without reading is not a gate. A real refusal (a 400 for bad credentials)
    still fails immediately; only a transport-level failure is retried.
    """
    key = anon_key()
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(
            FX.env("SUPABASE_URL") + "/auth/v1/token?grant_type=password",
            method="POST",
            headers={"apikey": key, "Content-Type": "application/json"},
            data=json.dumps({"email": email, "password": pw}).encode())
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            raise SystemExit("sign-in refused for %s: %s %s"
                             % (email, e.code, e.read().decode()[:200]))
        except (urllib.error.URLError, ssl.SSLError, OSError) as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise SystemExit("sign-in for %s failed after %d tries: %s"
                     % (email, tries, last))


def call(method, path, token, body=None):
    """One call to the locally-run backend, as a signed-in person."""
    req = urllib.request.Request(
        API + path, method=method,
        headers={"Authorization": "Bearer " + token,
                 "Content-Type": "application/json"},
        data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw.strip() else {})
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, raw[:400]


def rest(method, path, token, body=None, prefer=None):
    """PostgREST as a signed-in person, under real RLS."""
    key = anon_key()
    headers = {"apikey": key, "Authorization": "Bearer " + token,
               "Content-Type": "application/json"}
    if prefer:
        headers["Prefer"] = prefer
    req = urllib.request.Request(
        FX.env("SUPABASE_URL") + path, method=method, headers=headers,
        data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw.strip() else {})
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:300]


class Server:
    """The backend, run locally against TEST, for the life of the drive.

    ⚠️ IT MUST BE THIS REPO'S BACKEND AND THIS RUN'S CODE. Pointing the drive
    at the deployed Render instance would test whatever is on main, which is
    precisely not what is being changed here.

    ⚠️ KILLED BY PID, NEVER BY NAME. Three lanes run `node server.js` on this
    machine at once; `pkill -f node` takes down two colleagues' work and leaves
    no trace of having done it.
    """

    def __init__(self, extra_origin=None):
        self.extra_origin = extra_origin
        self.p = None

    def __enter__(self):
        # ⚠️ SUPPLY THE ANON KEY. The standing check (`callerStanding`) runs the
        # caller's own JWT through `auth_user_has_scope`, so the DATABASE
        # decides who is a school admin rather than the backend guessing. Without
        # it the admin path answers 500 `scope_check_failed` — honest, but it
        # means the drive would never exercise the 403 it is there to prove.
        env = dict(os.environ, PORT=str(PORT), SUPABASE_ANON_KEY=anon_key())
        # ⚠️ AND THE PAGE'S ORIGIN. The allowlist is a literal list in server.js
        # naming `http://localhost:5500`; this drive serves the site on a port of
        # its own so that it cannot collide with a colleague's static server, and
        # `EXTRA_CORS_ORIGINS` is exactly the escape hatch that exists so a dev
        # port never has to be added to production's list.
        if self.extra_origin:
            env["EXTRA_CORS_ORIGINS"] = self.extra_origin
        self.p = subprocess.Popen(
            ["node", "server.js"], cwd=BACKEND, env=env,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        deadline = time.time() + 45
        while time.time() < deadline:
            if self.p.poll() is not None:
                out = self.p.stdout.read()[:2000]
                raise SystemExit("backend exited on boot:\n" + out)
            try:
                with urllib.request.urlopen(API + "/api/health", timeout=3):
                    print("   backend up on :%d (pid %d) from %s"
                          % (PORT, self.p.pid, BACKEND))
                    return self
            except Exception:                                  # noqa: BLE001
                time.sleep(0.4)
        raise SystemExit("backend did not come up on :%d" % PORT)

    def __exit__(self, *exc):
        if not self.p:
            return
        self.p.terminate()
        try:
            self.p.wait(timeout=10)
        except subprocess.TimeoutExpired:
            self.p.kill()


# ════════════════════════════════════════════════════════════════════════
# THE POOL, AS PYTHON SEES IT — the independent reading every purity check
# is measured against.
# ════════════════════════════════════════════════════════════════════════
#
# ⚠️ RE-DERIVED FROM PLAN §1, NOT READ OUT OF THE BACKEND. Asserting that the
# backend's payload agrees with the backend's own filter is a tautology. What
# makes "every served question is one this class may have" a real claim is that
# the entitlement is computed HERE, from `ks4_data.classify()` and the authored
# rows, and the payload is compared against it.
_KS4_BY_ID = None
_KS4_CLASSIFY = None


def ks4_pool():
    global _KS4_BY_ID, _KS4_CLASSIFY
    if _KS4_BY_ID is None:
        _KS4_BY_ID = {r["id"]: r for r in ks4_data.load_pool()}
        _KS4_CLASSIFY = ks4_data.classify()
    return _KS4_BY_ID, _KS4_CLASSIFY


def ks4_permitted(row, tier, pathway):
    """PLAN §1's pool spec, stated independently.

    ⚠️ THE HIGHER POOL IS NOT SIMPLY THE HIGHER ROWS. It is `tier='higher'`
    (all bands) ∪ `tier='foundation'` in `standard|harder`. A Higher class is
    not a class that skips the foundation material; it is a class that meets it
    at the harder end — only 30 of 264 subtopics are classified `higher`, so
    "higher rows only" would leave Higher unable to set most of the spec, and
    including their `easier` band would hand a Higher group the four gentlest
    questions in the topic. An audit that assumed otherwise would fail on
    correct data, which is the worst kind of check.
    """
    if pathway != "triple" and row["triple_only"]:
        return False
    if tier == "foundation":
        return row["tier"] == "foundation"
    if row["tier"] == "higher":
        return True
    return row["tier"] == "foundation" and row["band"] in ("standard", "harder")


KS3_BAND_BY_TIER = {"easy": "easier", "medium": "standard", "hard": "harder"}


def scope_of(token, class_id):
    st, body = call("GET", "/api/teacher/set-work/scope?class_id=" + class_id, token)
    return st, (body if isinstance(body, dict) else {})


def preview(token, class_id, tier, kind, ref, count=10, exclude=None,
            subject=None):
    q = ("/api/teacher/set-work/preview?class_id=%s&tier=%s&scope_kind=%s"
         "&scope_ref=%s&count=%d" % (class_id, tier, kind, ref, count))
    if exclude:
        q += "&exclude=" + ",".join(exclude)
    # ⊕ `subject` DISAMBIGUATES, AND IS OPTIONAL BECAUSE ALMOST NOTHING NEEDS
    # IT. `atomic-structure` is a topic id in BOTH chemistry and physics, so on
    # a combined class the tree holds two nodes under one ref. Every other id in
    # the curriculum is unique.
    if subject:
        q += "&subject=" + subject
    return call("GET", q, token)


def flatten(tree):
    """(kind, ref, name, topic_id, subject, paper, counts) for every node."""
    out = []
    for t in tree:
        out.append(("topic", t["id"], t["name"], t["id"], t.get("subject"),
                    t.get("paper"), t.get("counts") or {}))
        for c in t.get("children") or []:
            out.append(("subtopic", c["id"], c["name"], t["id"], t.get("subject"),
                        t.get("paper"), c.get("counts") or {}))
    return out


# ════════════════════════════════════════════════════════════════════════
# 1 · THE TREE — what each cohort is offered, and at what tiers
# ════════════════════════════════════════════════════════════════════════
def check_scope(t_teacher):
    print("\n1 · the tree each class is offered")
    out = {}
    for key, cid in (("ks3", FX.C_KS3_A), ("comb", FX.C_KS4_COMB),
                     ("bi", FX.C_KS4_TRIPLE), ("ph", FX.C_KS4_SEPS)):
        st, body = scope_of(t_teacher, cid)
        if st != 200:
            record(False, "/scope answers for %s" % key, "status %s %s"
                   % (st, json.dumps(body)[:200]))
            return None
        out[key] = body
    record(True, "/scope answers 200 for all four classes")

    _by_id, cls = ks4_pool()

    # ── C5 · seps_sees_own_subject_only ───────────────────────────────
    #
    # ⚠️ TWO SEPARATE-SCIENCE CLASSES, AND THAT IS WHY THIS CAN FAIL. With one
    # seps class in the world, "sees its OWN subject" and "sees the FIRST
    # subject" are the same answer, and a route that had hardcoded biology
    # would pass. 10c/Ph1 exists so the two claims come apart.
    # ⊕ MRB-336, 8 Sep 2026 — `and body.get("papers") is None` USED TO BE
    # PART OF THIS CONJUNCTION, and it is the only clause that changed. It
    # said a separate-sciences class is offered no paper chips. See the
    # dedicated papers check below for why that was wrong; the SUBJECT half of
    # this assertion is untouched and is what the check is actually named for.
    for label, key, want in (("10a/Bi1", "bi", "biology"),
                             ("10c/Ph1", "ph", "physics")):
        body = out[key]
        subs = {t.get("subject") for t in body.get("tree") or []}
        record(subs == {want} and body.get("subjects") == [want]
               and (body.get("class") or {}).get("subject") == want,
               "seps_sees_own_subject_only — %s sees %s and nothing else"
               % (label, want),
               "tree subjects %s · subjects %s · papers %s"
               % (sorted(s or "-" for s in subs), body.get("subjects"),
                  body.get("papers")))

    comb = out["comb"]
    record(sorted(comb.get("subjects") or []) ==
           ["biology", "chemistry", "physics"] and comb.get("papers") == [1, 2],
           "the combined class gets all three subjects and both paper chips",
           "subjects %s papers %s" % (comb.get("subjects"), comb.get("papers")))

    # ── ⊕ MRB-336 · PAPERS ARE A KEY-STAGE FACT, NOT A PATHWAY FACT ───────
    #
    # ⛔ THE OLD ASSERTION LIVED IN THE LOOP ABOVE AND READ
    # `body.get("papers") is None` FOR BOTH SEPARATE-SCIENCE CLASSES, under
    # ks4_pool_drive's comment "papers are a combined-only chip". It passed
    # every run, and what it was pinning was a defect: AQA examines Triple
    # Biology on Biology Paper 1 and Biology Paper 2, exactly as it examines
    # Trilogy on two papers per science. So the cohort whose teachers most
    # often revise BY PAPER — "everything on paper 1 before the mock" — was
    # the one cohort the sheet would not let filter by it.
    #
    # It is superseded here rather than deleted so that a reader meeting
    # `papers == [1, 2]` on a triple class cannot mistake it for the drift.
    #
    # ⚠️ THE OFFER AND THE TREE ARE TWO FACTS AND THIS SPLITS THEM.
    # `treeForClass` has stamped `paper` on every KS4 topic from `KS4_PAPER`
    # since it was written, with no pathway branch near it — so the triple
    # tree ALREADY carried the right paper on every topic and only the OFFER
    # (`papersFor`) withheld the chips. Asserting only the class-level list
    # would therefore pass on a build where the per-topic stamp had been lost,
    # and asserting only the stamp would pass on today's defect. Both, or
    # neither is a real claim.
    record(out["bi"].get("papers") == [1, 2]
           and out["ph"].get("papers") == [1, 2],
           "⊕ MRB-336: papers_offered_on_triple — a separate-sciences class "
           "is offered BOTH paper chips, because AQA examines it on two "
           "papers per science",
           "10a/Bi1 %s · 10c/Ph1 %s"
           % (out["bi"].get("papers"), out["ph"].get("papers")))
    record(out["ks3"].get("papers") is None,
           "…and KS3 still has none, so the change is keyed on the KEY STAGE "
           "and not on 'everybody gets papers now'",
           "8a/Sc1 papers %r" % out["ks3"].get("papers"))

    # ── ⊕ MRB-336 · `space`, THE ONE TOPIC THAT PROVES BOTH DIRECTIONS ────
    #
    # All five of `space`'s subtopics are `triple_only`, which makes it the
    # only topic in the curriculum where the two halves of this change pull
    # opposite ways at once:
    #
    #   · on TRIPLE PHYSICS it is in the tree and must carry a paper 2 chip —
    #     it IS examined on physics paper 2, and until today a Triple Physics
    #     teacher revising by paper could not reach it by paper at all;
    #   · on COMBINED it is not in the tree, so there is nothing there to
    #     carry a chip (C7 above asserts the absence).
    #
    # Neither is a special case in `papersFor`; both fall out of the tree it
    # is stamped onto. That is exactly why they need asserting separately —
    # a one-line change cannot tell them apart, and a regression in either
    # direction would leave the other passing.
    ph_topics = {t["id"]: t for t in out["ph"].get("tree") or []}
    sp = ph_topics.get("space")
    record(sp is not None and sp.get("paper") == 2,
           "⊕ MRB-336: space_is_paper_two_on_triple — the topic a combined "
           "class cannot see carries paper 2 on the triple physics tree",
           "paper %r, %d subtopic(s)"
           % ((sp or {}).get("paper"), len((sp or {}).get("children") or []))
           if sp else "⚠️ `space` is absent from the triple physics tree")

    # …and the rail PARTITIONS the tree rather than sampling it. One topic
    # with `paper: null` is a topic that disappears from both filters, and a
    # teacher who tapped Paper 1 and then Paper 2 would never see it.
    unpapered = []
    for label, key in (("combined", "comb"), ("triple bio", "bi"),
                       ("triple phys", "ph")):
        for t in out[key].get("tree") or []:
            if t.get("paper") not in (1, 2):
                unpapered.append("%s/%s=%r" % (label, t.get("id"), t.get("paper")))
    record(not unpapered,
           "⊕ MRB-336: paper_partitions_the_tree — every KS4 topic on every "
           "cohort's tree carries paper 1 or paper 2",
           "%d topic(s) across three cohorts, all papered"
           % sum(len(out[k].get("tree") or []) for k in ("comb", "bi", "ph"))
           if not unpapered else "UNPAPERED: %s" % unpapered[:6])

    # ── C6 · combined_no_triple_only ──────────────────────────────────
    leaked = [ref for kind, ref, _n, _t, _s, _p, _c in flatten(comb.get("tree") or [])
              if kind == "subtopic" and cls.get(ref, {}).get("triple_only")]
    record(not leaked,
           "combined_no_triple_only — no triple-only subtopic is on the "
           "combined tree",
           "%d subtopic(s) offered, none triple-only"
           % sum(1 for k, *_r in flatten(comb.get("tree") or []) if k == "subtopic")
           if not leaked else "LEAKED: %s" % sorted(leaked)[:6])
    # …and the mirror, or "offers nothing unusual" would pass this.
    trip_only = [ref for kind, ref, _n, _t, _s, _p, _c
                 in flatten(out["bi"].get("tree") or [])
                 if kind == "subtopic" and cls.get(ref, {}).get("triple_only")]
    record(bool(trip_only),
           "…and the triple class IS offered triple-only subtopics",
           "%d, e.g. %s" % (len(trip_only), sorted(trip_only)[:3]))

    # ── C7 · space_absent_on_combined ─────────────────────────────────
    #
    # A topic ALL of whose subtopics are triple-only is omitted from a combined
    # tree entirely rather than rendered empty. Today that is exactly `space`.
    comb_topics = {t["id"] for t in comb.get("tree") or []}
    record("space" not in comb_topics,
           "space_absent_on_combined — the topic is not on the tree at all, "
           "not merely empty",
           "%d topics offered" % len(comb_topics))

    # ── C9 · ks3_three_tiers, and Medium is the default ───────────────
    ks3 = out["ks3"]
    record(ks3.get("tiers") == ["easy", "medium", "hard"]
           and (ks3.get("class") or {}).get("default_tier") == "medium",
           "ks3_three_tiers — Easy / Medium / Hard, defaulting to Medium",
           "tiers %s default %s"
           % (ks3.get("tiers"), (ks3.get("class") or {}).get("default_tier")))
    record(ks3.get("subjects") == ["biology", "chemistry", "physics"]
           and ks3.get("papers") is None,
           "…all three sciences, and no paper chips at KS3",
           "subjects %s papers %s" % (ks3.get("subjects"), ks3.get("papers")))

    # ── C11 · tier_default_matches_rule ───────────────────────────────
    #
    # RISKS D15. The fixture's KS4 rows carry no tier in their INSERT payload —
    # `classes_apply_tier_rule` derives it from the name — so what this reads is
    # the database's reading of `10b/Sc5` and `10a/Bi1`, not a value this drive
    # or its fixture typed in.
    for label, key, want in (("10b/Sc5", "comb", "foundation"),
                             ("10a/Bi1", "bi", "higher"),
                             ("10c/Ph1", "ph", "higher")):
        k = out[key].get("class") or {}
        record(k.get("default_tier") == want and out[key].get("tiers") ==
               ["foundation", "higher"],
               "tier_default_matches_rule — %s lands on %s" % (label, want),
               "default_tier %s · source %s · tiers %s"
               % (k.get("default_tier"), k.get("tier_pathway_source"),
                  out[key].get("tiers")))

    # ── C4 · sheet_offers_same_cohort_only ────────────────────────────
    #
    # ⚠️ 10a/Bi1 AND 10c/Ph1 ARE BOTH TRIPLE HIGHER AND ARE STILL TWO COHORTS,
    # because a cohort carries the SCIENCE. That pair is the only way to prove
    # the subject conjunct at KS4 without also changing the pathway, which
    # would leave a passing check that never tested it.
    for label, key, forbid in (("10a/Bi1", "bi", FX.C_KS4_SEPS),
                               ("10c/Ph1", "ph", FX.C_KS4_TRIPLE),
                               ("10b/Sc5", "comb", FX.C_KS4_TRIPLE),
                               ("8a/Sc1", "ks3", FX.C_KS4_COMB)):
        ids = {c["id"] for c in out[key].get("cohort_classes") or []}
        record(forbid not in ids,
               "sheet_offers_same_cohort_only — %s is not offered a class of "
               "another cohort" % label,
               "offered: %s" % sorted(c["name"] for c in
                                      out[key].get("cohort_classes") or []))
    ks3_ids = {c["id"] for c in ks3.get("cohort_classes") or []}
    record(FX.C_KS3_B in ks3_ids,
           "…and IS offered the KS3 class beside it, or the list would pass "
           "by being empty",
           "offered: %s" % sorted(c["name"] for c in
                                  ks3.get("cohort_classes") or []))
    record(FX.C_FOREIGN not in ks3_ids,
           "…and never a class in the same cohort the teacher does not teach")

    # ── C12 · every node carries a count for EVERY tier ───────────────
    #
    # The tier chip re-renders counts IN PLACE from what /scope already sent
    # (the browser half proves that). It can only do so if the counts are all
    # there, so a node missing a tier key would be a spinner the teacher never
    # asked for — or a silent zero.
    missing = []
    for key, tiers in (("ks3", ["easy", "medium", "hard"]),
                       ("comb", ["foundation", "higher"])):
        for kind, ref, _n, _t, _s, _p, counts in flatten(out[key].get("tree") or []):
            for t in tiers:
                if not isinstance(counts.get(t), int):
                    missing.append("%s %s@%s" % (kind, ref, t))
    record(not missing,
           "tier_change_recounts (data half) — every node carries a count for "
           "every tier of its key stage, in one /scope answer",
           "no re-fetch is possible on a chip tap" if not missing
           else "%d missing: %s" % (len(missing), missing[:5]))
    return out


# ════════════════════════════════════════════════════════════════════════
# 2 · THE PREVIEW — every question belongs to scope, tier and pathway
# ════════════════════════════════════════════════════════════════════════
def pick_topic(scope, want_children=2, tier="foundation"):
    """A topic with several stocked subtopics, for the round-robin check."""
    best = None
    for t in scope.get("tree") or []:
        stocked = [c for c in t.get("children") or []
                   if (c.get("counts") or {}).get(tier, 0) > 0]
        if len(stocked) >= want_children:
            n = sum((c.get("counts") or {})[tier] for c in stocked)
            if best is None or n > best[0]:
                best = (n, t, stocked)
    return best


def check_preview(t_teacher, scopes):
    print("\n2 · what a preview actually hands over")
    by_id, cls = ks4_pool()

    # ── every question is in scope, at the tier, in the pathway ───────
    #
    # ⚠️ THE PATHWAY IS THE CLASS'S AND THE TIER IS THE REQUEST'S, which is the
    # v2 semantic in one line. So the SAME class is asked at BOTH tiers, and
    # each answer is audited against that request's entitlement.
    for label, cid, pathway in (("10b/Sc5 combined", FX.C_KS4_COMB, "combined"),
                                ("10a/Bi1 triple", FX.C_KS4_TRIPLE, "triple")):
        scope = scopes["comb" if pathway == "combined" else "bi"]
        for tier in ("foundation", "higher"):
            got = pick_topic(scope, 2, tier)
            if not got:
                record(False, "%s @ %s: a stocked topic exists" % (label, tier))
                continue
            _n, topic, _stocked = got
            st, body = preview(t_teacher, cid, tier, "topic", topic["id"], 10)
            qs = (body or {}).get("picked") or []
            if st != 200 or not qs:
                record(False, "%s @ %s: preview on %s" % (label, tier, topic["id"]),
                       "status %s %s" % (st, json.dumps(body)[:200]))
                continue
            slugs = {c["id"] for c in topic.get("children") or []}
            bad = []
            for q in qs:
                row = by_id.get(q["id"])
                if row is None:
                    bad.append("%s is in no authored pool" % q["id"])
                    continue
                if row["subtopic_slug"] not in slugs:
                    bad.append("%s is %s, outside %s"
                               % (q["id"], row["subtopic_slug"], topic["id"]))
                elif not ks4_permitted(row, tier, pathway):
                    bad.append("%s is tier=%s band=%s triple_only=%s — not "
                               "permitted at %s %s" % (q["id"], row["tier"],
                                                       row["band"],
                                                       row["triple_only"],
                                                       pathway, tier))
                if len(q.get("options") or []) != 4 or q.get("correct_index") is None:
                    bad.append("%s has %d option(s), answer %s"
                               % (q["id"], len(q.get("options") or []),
                                  q.get("correct_index")))
            record(not bad,
                   "preview_in_scope — %s @ %s: every question is in %s, at "
                   "this tier, in this pathway" % (label, tier, topic["id"]),
                   "%d question(s), all permitted" % len(qs) if not bad
                   else "; ".join(bad[:4]))

            # ── C14 · spread_across_subtopics ─────────────────────────
            if tier == "foundation":
                spread = {by_id[q["id"]]["subtopic_slug"] for q in qs
                          if q["id"] in by_id}
                stocked_n = len([c for c in topic["children"]
                                 if (c.get("counts") or {}).get(tier, 0) > 0])
                record(len(spread) >= min(stocked_n, 2),
                       "spread_across_subtopics — a topic-level set of ten is "
                       "not ten questions about one subtopic",
                       "%d subtopic(s) across %d question(s), from %d stocked"
                       % (len(spread), len(qs), stocked_n))

                # ── A7 · no_duplicate_stems_in_preview ────────────────
                stems = [re.sub(r"[.?!\s]+$", "",
                                re.sub(r"\s+", " ", (q.get("stem") or "").lower()))
                         for q in qs]
                record(len(set(stems)) == len(stems),
                       "no_duplicate_stems_in_preview — %s @ %s" % (label, tier),
                       "%d question(s), %d distinct stems"
                       % (len(stems), len(set(stems))))

    # ── the KS3 side: the band IS the tier ────────────────────────────
    import ks3_data.question_bank as qb
    ks3_by_id = {}
    for entry in qb.load_bank():
        for q in entry["questions"]:
            ks3_by_id[q["id"]] = (entry["lesson"], q["band"])
    ks3 = scopes["ks3"]
    got = pick_topic(ks3, 2, "medium")
    if got:
        _n, unit, _s = got
        for tier in ("easy", "medium", "hard"):
            st, body = preview(t_teacher, FX.C_KS3_A, tier, "topic", unit["id"], 10)
            qs = (body or {}).get("picked") or []
            slugs = {c["id"] for c in unit.get("children") or []}
            bad = [q["id"] for q in qs
                   if q["id"] not in ks3_by_id
                   or ks3_by_id[q["id"]][0] not in slugs
                   or ks3_by_id[q["id"]][1] != KS3_BAND_BY_TIER[tier]]
            record(st == 200 and qs and not bad,
                   "preview_in_scope — KS3 %s @ %s draws only band %s from "
                   "this unit" % (unit["id"], tier, KS3_BAND_BY_TIER[tier]),
                   "%d question(s), all in band" % len(qs) if not bad
                   else "wrong: %s" % bad[:4])

    # ── the count chips' ceiling is a real number ─────────────────────
    #
    # `available` is what the chips cap against (RISKS A4). It must be the whole
    # pool for the scope and NOT what is left after `exclude`, or a ceiling
    # would shrink every time a teacher swapped a row and disable the chip they
    # were already on.
    got = pick_topic(scopes["comb"], 2, "foundation")
    if got:
        _n, topic, _s = got
        st, a = preview(t_teacher, FX.C_KS4_COMB, "foundation", "topic",
                        topic["id"], 5)
        first = [q["id"] for q in (a.get("picked") or [])]
        st2, b = preview(t_teacher, FX.C_KS4_COMB, "foundation", "topic",
                         topic["id"], 5, exclude=first)
        record(a.get("available") == b.get("available") and a.get("available", 0) > 0,
               "available is the WHOLE pool, not what is left after exclude",
               "available %s then %s with %d excluded"
               % (a.get("available"), b.get("available"), len(first)))
        record(not (set(first) & {q["id"] for q in (b.get("picked") or [])}),
               "…and exclude is honoured — none of the excluded ids come back")


# ════════════════════════════════════════════════════════════════════════
# 3 · SWAP — never a repeat, and it runs out honestly
# ════════════════════════════════════════════════════════════════════════
def check_swap(t_teacher, scopes):
    print("\n3 · swap")

    # ⚠️ A SMALL SCOPE ON PURPOSE. Exhaustion is only reachable on a pool a
    # drive can actually drain, and a KS3 LESSON at one tier holds four to
    # sixteen rows. On a KS4 topic it would take hundreds of requests.
    small = None
    for t in scopes["ks3"].get("tree") or []:
        for c in t.get("children") or []:
            n = (c.get("counts") or {}).get("easy", 0)
            if 0 < n <= 8 and (small is None or n < small[1]):
                small = (c["id"], n)
    if not small:
        record(False, "a small KS3 lesson exists to drain")
        return
    slug, n = small
    record(True, "chose a lesson small enough to exhaust",
           "%s holds %d at Easy" % (slug, n))

    seen, rounds = [], 0
    st, body = preview(t_teacher, FX.C_KS3_A, "easy", "subtopic", slug, 1)
    if st != 200 or not body.get("picked"):
        record(False, "the small lesson previews", "status %s" % st)
        return
    seen.append(body["picked"][0]["id"])

    # ── A6 · swap_never_repeats, and then swap_exhausts_disables ──────
    while rounds < n + 4:
        rounds += 1
        st, one = call("GET", "/api/teacher/set-work/swap?class_id=%s&tier=easy"
                       "&scope_kind=subtopic&scope_ref=%s&exclude=%s"
                       % (FX.C_KS3_A, slug, ",".join(seen)), t_teacher)
        if st == 204:
            break
        if st != 200 or not (one or {}).get("id"):
            record(False, "swap answered %s" % st, json.dumps(one)[:160])
            return
        if one["id"] in seen:
            record(False, "swap_never_repeats — swap handed back %s, already "
                          "shown" % one["id"], "after %d swap(s)" % rounds)
            return
        seen.append(one["id"])
    record(True, "swap_never_repeats — %d consecutive swaps, never a repeat"
           % (len(seen) - 1), "ids: %s" % ", ".join(seen[:6]))
    record(st == 204 and len(seen) == n,
           "swap_exhausts_disables — the pool runs out at exactly its size, "
           "and says so with 204 rather than an empty 200",
           "%d shown of %d available, final status %s" % (len(seen), n, st))

    # A 204 is what the sheet turns into a dead Swap button. An empty 200 would
    # be a control that looked alive and did nothing — the dead-control shape.
    record(st == 204, "…and 204 is a status the sheet can act on")


# ════════════════════════════════════════════════════════════════════════
# 4 · THE WRITE, AND EVERY WAY IT MUST REFUSE
# ════════════════════════════════════════════════════════════════════════
#
# ⚠️ THESE ARE CRAFTED REQUESTS, NOT SHEET PRESSES, AND THAT IS THE POINT. The
# sheet only ever OFFERS what a class may have, so a teacher working through
# the UI can never trip any of them. A sheet is a browser, and a browser can be
# asked to post anything; these go straight at the route with a real teacher's
# JWT, which is exactly what an inspector-tab request would be.
def post_set(token, **kw):
    body = {
        "class_ids": kw.get("class_ids"),
        "tier": kw.get("tier"),
        "scope_kind": kw.get("scope_kind", "topic"),
        "scope_ref": kw.get("scope_ref"),
        "question_ids": kw.get("question_ids"),
        "title": kw.get("title", TITLE + " · scratch"),
        "release_at": kw.get("release_at", None),
        "due_at": kw.get("due_at", DUE.isoformat()),
        # ⊕ `client_ref` IS REQUIRED, and a FRESH one per call by default.
        # It is the idempotency key: the same body twice with the same ref
        # sets the work once. So every ordinary check here must carry its OWN,
        # or the second write in a run would be answered as a replay of the
        # first and the check would pass having written nothing.
        # `check_idempotent_submit` is the one place a ref is reused on
        # purpose.
        "client_ref": kw.get("client_ref") or str(uuid.uuid4()),
    }
    if kw.get("subject") is not None:
        body["subject"] = kw["subject"]
    st, out = call("POST", "/api/teacher/set-work", token, body)
    if st == 200 and isinstance(out, dict):
        made_assignments.extend(out.get("assignment_ids") or [])
    return st, out


def check_write(t_teacher, scopes):
    print("\n4 · setting the work, and every way the route must refuse")
    by_id, cls = ks4_pool()

    got = pick_topic(scopes["comb"], 2, "foundation")
    if not got:
        record(False, "a combined topic to set")
        return None
    _n, topic, _s = got
    st, prev = preview(t_teacher, FX.C_KS4_COMB, "foundation", "topic",
                       topic["id"], 5)
    ids = [q["id"] for q in (prev.get("picked") or [])]
    if len(ids) < 5:
        record(False, "five questions to set", "got %d" % len(ids))
        return None

    # ── the ordinary set ──────────────────────────────────────────────
    st, made = post_set(t_teacher, class_ids=[FX.C_KS4_COMB], tier="foundation",
                        scope_ref=topic["id"], question_ids=ids,
                        title=TITLE + " · one class")
    # ⊕ MRB-336, 8 Sep 2026 — `and made.get("clamped") is False` WAS THE THIRD
    # CONJUNCT HERE. The field is gone from the response, so the old clause
    # would now compare `None is False` and fail — but the more useful reading
    # is that it has nothing left to say: with no clamp anywhere in the route,
    # "was this set clamped" is not a question the answer needs to carry.
    # ⚠️ `is None` is asserted rather than merely dropped. A `clamped` key
    # reappearing would mean a clamp had come back, and a silently-tolerated
    # extra key is how a removed behaviour returns unnoticed.
    ok = record(st == 200 and len(made.get("assignment_ids") or []) == 1
                and made.get("clamped") is None,
                "a teacher sets work on one class, and the answer carries no "
                "`clamped` field because nothing clamps any more",
                "status %s ids %s clamped %r keys %s"
                % (st, made.get("assignment_ids"), made.get("clamped"),
                   sorted(made.keys()) if isinstance(made, dict) else made))
    if not ok:
        return None
    aid = made["assignment_ids"][0]

    # Read it back THROUGH THE API, as the teacher, not out of the database.
    st, back = call("GET", "/api/class/current-assignment?class_id=%s"
                    "&assignment_id=%s" % (FX.C_KS4_COMB, aid), t_teacher)
    got_ids = [q.get("question_ref") for q in back.get("questions") or []]
    record(got_ids == ids,
           "the stored questions are the ones chosen, in the order chosen",
           "wanted %s\n        got    %s" % (ids, got_ids))
    a = back.get("assignment") or {}
    record(a.get("title") == TITLE + " · one class",
           "the teacher's title is stored verbatim", a.get("title"))

    # ── D2 · the NOT NULL columns are filled from the SCOPE ───────────
    #
    # `topic` and `subject_id` are NOT NULL and v1 wrote them from the scheme
    # row, which no longer exists. A v2 row that left `topic` as the slug, or
    # as null, would be a row every downstream consumer renders as a blank
    # heading — the reteach panel, the digest and the print sheet all display it.
    st, cols = rest("GET", "/rest/v1/assignments?id=eq.%s&select=topic,subtopic,"
                           "quiz_type,set_tier,scope_kind,scope_ref,subject,paper,"
                           "source,auto_generated,set_by,source_sow_entry_id,"
                           "academic_week,subject_id" % aid, t_teacher)
    row = cols[0] if isinstance(cols, list) and cols else {}
    record(row.get("topic") == topic["name"]
           and row.get("subtopic") is None
           and row.get("quiz_type") == "topic_quiz"
           and row.get("set_tier") == "foundation"
           and row.get("scope_kind") == "topic"
           and row.get("scope_ref") == topic["id"]
           and row.get("subject") == topic.get("subject")
           and row.get("source") == "teacher"
           and row.get("auto_generated") is False
           and row.get("source_sow_entry_id") is None
           and row.get("subject_id"),
           "consumers_render_null_sow (data half) — the row carries the "
           "TOPIC TITLE, the scope, the tier and a subject_id, and no scheme "
           "entry at all",
           json.dumps(row)[:300])
    record(row.get("paper") in (1, 2),
           "…and the paper the topic sits on, for the combined chips",
           "paper %s" % row.get("paper"))

    # ── C1 · spoofed_tier_rejected ────────────────────────────────────
    for bad_tier in ("medium", "HIGHER", "", "super"):
        st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB], tier=bad_tier,
                           scope_ref=topic["id"], question_ids=ids)
        if not record(st == 400 and (out or {}).get("error") == "bad_tier",
                      "spoofed_tier_rejected — a KS4 class refuses tier %r"
                      % bad_tier, "status %s %s" % (st, json.dumps(out)[:120])):
            break
    st, out = post_set(t_teacher, class_ids=[FX.C_KS3_A], tier="foundation",
                       scope_ref="B1", question_ids=ids)
    record(st == 400 and (out or {}).get("error") == "bad_tier",
           "spoofed_tier_rejected — and a KS3 class refuses 'foundation'",
           "status %s %s" % (st, json.dumps(out)[:120]))

    # ── C2 · scope_spoof_rejected ─────────────────────────────────────
    #
    # ⚠️ THE REFUSAL IS AT THE SCOPE, NOT AT THE POOL, AND THAT IS STRONGER.
    # The tree is RE-DERIVED from the class on every request, so `meiosis` is
    # not "found and then rejected" for a combined class — it is not in the
    # tree that gets walked, so there is nothing to find. A filter applied
    # after a lookup is a filter a caller can forget.
    for label, ref, kind in (("a triple-only subtopic", "meiosis", "subtopic"),
                             ("the space topic", "space", "topic"),
                             ("a KS3 unit code", "B1", "topic"),
                             ("something invented", "not-a-real-topic", "topic")):
        st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB],
                           tier="foundation", scope_kind=kind, scope_ref=ref,
                           question_ids=ids)
        record(st == 400 and (out or {}).get("error") == "scope_not_for_class",
               "scope_spoof_rejected — a combined class refuses %s (%s)"
               % (label, ref), "status %s %s" % (st, json.dumps(out)[:120]))

    # ── C3 · foreign_question_rejected — the meiosis-in-Energy-Changes case ─
    #
    # Two ids from `meiosis` (triple-only BIOLOGY) posted under `energy-changes`
    # (CHEMISTRY) at the combined class. It is wrong three ways at once — wrong
    # topic, wrong subject, wrong pathway — and the route must not distinguish
    # them: a missing id and an out-of-scope id are ONE refusal, because telling
    # them apart would confirm the existence of a question the caller was never
    # offered.
    meiosis = [i for i, r in by_id.items() if r["subtopic_slug"] == "meiosis"][:2]
    ec = [c["id"] for t in scopes["comb"]["tree"]
          for c in t.get("children") or [] if t["id"] == "energy-changes"]
    if meiosis and ec:
        st, ec_prev = preview(t_teacher, FX.C_KS4_COMB, "foundation", "topic",
                              "energy-changes", 3)
        good = [q["id"] for q in (ec_prev.get("picked") or [])]
        st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB],
                           tier="foundation", scope_ref="energy-changes",
                           question_ids=good[:1] + meiosis)
        record(st == 400 and (out or {}).get("error") == "questions_not_in_scope",
               "foreign_question_rejected — two meiosis ids posted under "
               "energy-changes are refused, even beside a legitimate one",
               "status %s %s" % (st, json.dumps(out)[:160]))
        record(good and "meiosis" not in json.dumps(out),
               "…and the refusal does not name the questions it refused",
               json.dumps(out)[:160])
    else:
        record(False, "the meiosis / energy-changes case is constructible",
               "meiosis ids %s, energy-changes children %s" % (meiosis, ec))

    # ── C4 · cohort_mismatch_rejected ─────────────────────────────────
    #
    # 10a/Bi1 and 10c/Ph1 are BOTH KS4 triple higher. They are still two
    # cohorts, because a cohort carries the separate science — and this pair is
    # the only way to prove that conjunct without also moving the pathway.
    st, bi_prev = preview(t_teacher, FX.C_KS4_TRIPLE, "higher", "topic",
                          "cell-biology", 3)
    bi_ids = [q["id"] for q in (bi_prev.get("picked") or [])]
    for label, pair in (("two triple classes of different sciences",
                         [FX.C_KS4_TRIPLE, FX.C_KS4_SEPS]),
                        ("a triple and a combined class",
                         [FX.C_KS4_TRIPLE, FX.C_KS4_COMB]),
                        ("a KS4 and a KS3 class",
                         [FX.C_KS4_TRIPLE, FX.C_KS3_A])):
        st, out = post_set(t_teacher, class_ids=pair, tier="higher",
                           scope_ref="cell-biology", question_ids=bi_ids)
        record(st == 400 and (out or {}).get("error") == "cohort_mismatch",
               "cohort_mismatch_rejected — %s cannot be set together" % label,
               "status %s %s" % (st, json.dumps(out)[:160]))

    # ── A11 · title_bounds ────────────────────────────────────────────
    for label, title in (("empty", ""), ("whitespace", "   "),
                         ("81 characters", "x" * 81)):
        st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB],
                           tier="foundation", scope_ref=topic["id"],
                           question_ids=ids, title=title)
        record(st == 400 and (out or {}).get("error") == "bad_title",
               "title_bounds — a %s title is refused" % label,
               "status %s %s" % (st, json.dumps(out)[:120]))
    st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB], tier="foundation",
                       scope_ref=topic["id"], question_ids=ids, title="x" * 80)
    record(st == 200, "…and exactly 80 is accepted, so the bound is not off "
                      "by one", "status %s" % st)

    # ── the count bounds ──────────────────────────────────────────────
    st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB], tier="foundation",
                       scope_ref=topic["id"], question_ids=[])
    record(st == 400 and (out or {}).get("error") == "no_questions",
           "a set of nothing is refused", "status %s %s" % (st, json.dumps(out)[:100]))
    st, big = preview(t_teacher, FX.C_KS4_COMB, "foundation", "topic",
                      topic["id"], 20)
    big_ids = [q["id"] for q in (big.get("picked") or [])]
    if len(big_ids) >= 20:
        st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB],
                           tier="foundation", scope_ref=topic["id"],
                           question_ids=big_ids[:20],
                           title=TITLE + " · twenty")
        record(st == 200, "twenty questions is accepted — the maximum",
               "status %s" % st)
        st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB],
                           tier="foundation", scope_ref=topic["id"],
                           question_ids=big_ids[:20] + big_ids[:1])
        record(st == 400 and (out or {}).get("error") in
               ("too_many_questions", "duplicate_questions"),
               "twenty-one is refused", "status %s %s" % (st, json.dumps(out)[:120]))
        st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB],
                           tier="foundation", scope_ref=topic["id"],
                           question_ids=big_ids[:3] + big_ids[:1])
        record(st == 400 and (out or {}).get("error") == "duplicate_questions",
               "the same question twice in one set is refused",
               "status %s %s" % (st, json.dumps(out)[:120]))
    else:
        record(False, "a topic with twenty available at Foundation exists",
               "%s has %d" % (topic["id"], len(big_ids)))

    # ── B3/B4/B5 · the dates ──────────────────────────────────────────
    later = (NOW + timedelta(days=3)).isoformat()
    st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB], tier="foundation",
                       scope_ref=topic["id"], question_ids=ids,
                       release_at=later, due_at=(NOW + timedelta(days=1)).isoformat())
    record(st == 400 and (out or {}).get("error") == "bad_due_at",
           "due_before_release_rejected — work due before it appears is "
           "overdue the instant a child first sees it",
           "status %s %s" % (st, json.dumps(out)[:160]))
    st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB], tier="foundation",
                       scope_ref=topic["id"], question_ids=ids,
                       release_at=(NOW - timedelta(hours=2)).isoformat())
    record(st == 400 and (out or {}).get("error") == "release_in_past",
           "release_in_past_rejected — two hours ago is not a slow form "
           "submission", "status %s %s" % (st, json.dumps(out)[:160]))
    st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB], tier="foundation",
                       scope_ref=topic["id"], question_ids=ids,
                       release_at=(NOW + timedelta(minutes=2)).isoformat(),
                       due_at=(NOW + timedelta(days=8)).isoformat())
    record(st == 200,
           "…but two minutes from now is accepted, so the five-minute grace "
           "is a grace and not a ban", "status %s" % st)
    st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB], tier="foundation",
                       scope_ref=topic["id"], question_ids=ids,
                       due_at=(NOW + timedelta(days=400)).isoformat())
    record(st == 400 and (out or {}).get("error") == "due_too_far",
           "due_too_far_rejected — a due date in 2031 is a mistyped year, "
           "every time", "status %s %s" % (st, json.dumps(out)[:160]))

    # ── multi-class, and its atomicity ────────────────────────────────
    print("\n   multi-class")
    st, ks3_prev = preview(t_teacher, FX.C_KS3_A, "medium", "topic", "B1", 4)
    ks3_ids = [q["id"] for q in (ks3_prev.get("picked") or [])]
    st, made2 = post_set(t_teacher, class_ids=[FX.C_KS3_A, FX.C_KS3_B],
                         tier="medium", scope_ref="B1", question_ids=ks3_ids,
                         title=TITLE + " · two classes")
    created = (made2 or {}).get("created") or []
    record(st == 200 and len(created) == 2
           and len({c["assignment_id"] for c in created}) == 2,
           "one press sets the work on both classes, each getting an "
           "assignment of its OWN — marking and completion are per class",
           "status %s, %d created" % (st, len(created)))

    # ⚠️ A PARTIAL SET IS WORSE THAN A REFUSAL. A teacher who sees an error and
    # cannot tell which half landed will retry, and `assignments_class_week_uniq`
    # is partial on `source='auto'` — nothing dedupes teacher rows, so the
    # child's week lists the same homework twice. No transient failure is
    # needed for this; it happened on MRB-331 with a hold on one school.
    before = set(week_titles(t_teacher, FX.C_KS3_A))
    ghost = TITLE + " · should never exist"
    st, out = post_set(t_teacher, class_ids=[FX.C_KS3_A, FX.C_FOREIGN],
                       tier="medium", scope_ref="B1", question_ids=ks3_ids,
                       title=ghost)
    record(st == 403 and (out or {}).get("error") == "not_authorised_for_class",
           "multi_class_atomic — a class the teacher does not teach refuses "
           "the WHOLE request", "status %s %s" % (st, json.dumps(out)[:160]))
    after = set(week_titles(t_teacher, FX.C_KS3_A))
    record(ghost not in after and after == before,
           "…and wrote NOTHING to the class that WAS the teacher's",
           "titles unchanged: %s" % sorted(after)[:6])

    # The same shape, refused for a DIFFERENT reason, to prove the rollback is
    # not specific to the 403 path: a bad question id inside a two-class set.
    st, out = post_set(t_teacher, class_ids=[FX.C_KS3_A, FX.C_KS3_B],
                       tier="medium", scope_ref="B1",
                       question_ids=ks3_ids[:2] + ["ks4-meiosis-e01"],
                       title=ghost + " 2")
    after2 = set(week_titles(t_teacher, FX.C_KS3_A))
    record(st == 400 and after2 == before,
           "multi_class_atomic — and a bad question id refuses both classes "
           "before either is written",
           "status %s, titles unchanged" % st)
    return aid, topic


def week_titles(token, class_id):
    st, body = call("GET", "/api/class/current-assignment?class_id=" + class_id,
                    token)
    return [w.get("title") for w in ((body or {}).get("week_work") or [])]


# ════════════════════════════════════════════════════════════════════════
# 5 · THE GO-LIVE HOLD, AND THE CHILD ON THE OTHER SIDE OF IT
# ════════════════════════════════════════════════════════════════════════
def check_hold(t_teacher, t_pupil_b):
    """⊕ MRB-336, 8 Sep 2026 — MIDE'S RULING, AND BOTH HALVES OF IT AT ONCE.

    ⛔ THIS CHECK USED TO ASSERT THE DEFECT. Three of its assertions are
    reversed here, and they are named so a reader can find what they used to
    say (the whole prior body is at `docs/mrb336/` in the report, and in git
    at 44dadd96c):

      1. `record(made.get("clamped") is True, "hold_clamp_single_line — the
         answer says `clamped`, which is the ONLY thing that makes the sheet
         show its one line", …)`
      2. `record(st == 400 and early.get("error") == "bad_due_at", "a due date
         falling before the hold releases the work is refused", …)`
      3. `record(TITLE + " · held" not in titles, "student_404_before_release
         — the child cannot see it in the week", …)` and its companion
         asserting a 404 on the id.

    Every one of those was a correct description of the code, and the code was
    wrong. `schools.assignments_open_from` was written as Mide's dial for
    delaying the day a school starts COMPOSING; it had grown a second job,
    silently, by being read inside the teacher's own write path. A teacher who
    set work in the week before term and chose Release Now had the release
    shoved to the school's open date, which also re-filed the row under a
    LATER academic week — so the work was invisible twice over, and the sheet
    told them it had been set. That is what Mide's three rows on production
    were, and his sentence is the definition rather than an exception to it:

        "the point of setting work is so that students can do assignments
         even though the automatic assignments hasn't gone live yet"

    ⚠️ THE RULING HAS TWO HALVES AND ONLY ONE OF THEM IS THE CHANGE. The hold
    keeps its ENTIRE meaning for automatic composition. A gate that proved
    only the new half would pass just as happily on a build that had deleted
    the hold outright, which would silently start composing for every school
    Mide is holding back — including on the morning of a live dry run.

    ⚠️ SO BOTH HALVES ARE PROVED IN ONE SCENARIO, FROM ONE RESPONSE, ON ONE
    CLASS, AT ONE INSTANT. `/api/class/current-assignment` answers both
    questions at once: `reason` and `assignment` describe the AUTOMATIC
    producer, and `week_work` lists what the child can actually open. Read
    separately — a held school here and a released row there — the two could
    disagree about the clock, the week, or the class and still both be green.
    Read from one payload they cannot.

    The seam that makes that possible is `.eq('source', 'auto')` on the
    "already composed?" branch (server.js:1636): a teacher's row never
    satisfies it, so the hold branch at 1d is genuinely reached even on a
    class that has teacher-set work sitting on it.

    ⚠️ AND THIS VERSION NEVER LIFTS THE HOLD. The old one PATCHed
    `schools.assignments_open_from` into the past to show the child the work,
    then PATCHed it back. That was the only way to make the point when release
    was clamped, and it left a window in which a crash between the two writes
    would leave the fixture's held school permanently open — every later run
    of this drive would then pass while testing nothing. Nothing here writes
    to `schools` at all.
    """
    print("\n5 · the school's go-live hold, and the child on the other side")
    st, scope = scope_of(t_teacher, FX.C_KS3_HELD)
    open_from = ((scope or {}).get("class") or {}).get("open_from")
    record(bool(open_from),
           "/scope still reports the school's open date on the class — it is "
           "the fact the AUTOMATIC producer acts on, and what "
           "teacher/admin.html renders",
           "open_from %s" % open_from)
    # ⚠️ NOTHING IN THE SHEET READS IT ANY MORE, and that is asserted on the
    # other side rather than here: `hold_line_gone` in `check_toast_and_swap`
    # proves the overlay carries no hold node and none of the words. A field
    # that is served and unread is only safe while something says so.

    got = pick_topic(scope, 1, "medium")
    if not got:
        return record(False, "the held school's class offers a stocked unit")
    _n, unit, _s = got
    st, prev = preview(t_teacher, FX.C_KS3_HELD, "medium", "topic", unit["id"], 3)
    ids = [q["id"] for q in (prev.get("picked") or [])]
    if len(ids) < 3:
        return record(False, "three questions to set on the held class",
                      "got %d" % len(ids))

    # ── (1) THE REFUSAL THAT USED TO FIRE, AND MUST NOT ───────────────
    #
    # ⊕ REVERSED. `DUE` is seven days out and the fixture's hold is EIGHT, so
    # this is precisely the request the old code answered 400 `bad_due_at` on:
    # the server moved release to the open date, the due date then fell before
    # it, and the work would have arrived already overdue. With no clamp there
    # is no such conflict — the teacher's release is now, the due date is a
    # week away, and the two are in the order the teacher chose them in.
    #
    # ⚠️ THE ASSERTION IS ON THE STATUS *AND* ON THE ERROR BEING ABSENT. A 200
    # alone would also be returned by a route that had stopped validating
    # `due_at` at all, and the refusal that remains (below) is what keeps that
    # honest.
    st, made = post_set(t_teacher, class_ids=[FX.C_KS3_HELD], tier="medium",
                        scope_ref=unit["id"], question_ids=ids,
                        title=TITLE + " · released into the hold",
                        due_at=DUE.isoformat())
    if not record(st == 200 and made.get("assignment_ids"),
                  "hold_does_not_refuse_the_due_date — Release Now with a due "
                  "date INSIDE the school's hold window is accepted; it used "
                  "to be 400 `bad_due_at`, because the clamp had moved release "
                  "past it",
                  "status %s %s" % (st, json.dumps(made)[:200])):
        return False
    aid = made["assignment_ids"][0]
    record(made.get("clamped") is None,
           "…and the answer carries no `clamped` field, on the one class in "
           "the world where it used to be True",
           "keys %s" % (sorted(made.keys()) if isinstance(made, dict) else made))

    # ── (2) `release_at` IS STORED EXACTLY AS ASKED ───────────────────
    #
    # ⊕ REVERSED. This used to assert the stored instant was LONDON MIDNIGHT
    # ON THE SCHOOL'S OPEN DATE — computed here in `Europe/London` precisely
    # because comparing the date strings read the correct clamp as an
    # off-by-one-day bug. The arithmetic was right and the behaviour it
    # measured is gone.
    #
    # ⚠️ READ OFF THE ROW THROUGH THE ROUTE, NOT OUT OF THE POST'S OWN REPORT.
    # A route that answered `release_at: <now>` and stored something else
    # would pass a check on its own payload. And read through the route rather
    # than PostgREST for a reason that is a property of the fixture: this
    # teacher's profile is in the OPEN school while this class is in the HELD
    # one — deliberately, so one sign-in drives both sides — and `assignments`'
    # SELECT policy is sealed on `school_id = auth_user_school_id()`, so
    # PostgREST correctly hands her an empty list here.
    st, back_h = call("GET", "/api/class/current-assignment?class_id=%s"
                      "&assignment_id=%s" % (FX.C_KS3_HELD, aid), t_teacher)
    stored = ((back_h or {}).get("assignment") or {}).get("release_at")
    got_at = (datetime.fromisoformat(str(stored).replace("Z", "+00:00"))
              if stored else None)
    # Release Now sends `release_at: null` and the server stamps its own
    # `now`, so this is a window rather than an equality. Five minutes is the
    # route's own past-grace and is wide enough for a slow sign-in and narrow
    # enough that a clamp to a date EIGHT DAYS away could never fit inside it.
    drift = abs((got_at - NOW).total_seconds()) if got_at else None
    record(got_at is not None and drift is not None and drift < 300,
           "release_at_stored_as_asked — Release Now on a held school stores "
           "an instant that IS now, not the school's open date",
           "stored %s · %s from the drive's clock"
           % (stored, ("%.0fs" % drift) if drift is not None else "—"))

    # …and the negative, stated as the thing it used to be. The two are not
    # the same assertion: a route that stored `now + 3 days` would satisfy
    # neither, but a route that stored midnight tonight would satisfy the
    # first at a certain hour and never this one.
    from zoneinfo import ZoneInfo
    y, m, d = (int(x) for x in str(open_from)[:10].split("-"))
    was = datetime(y, m, d, 0, 0, tzinfo=ZoneInfo("Europe/London")).astimezone(
        timezone.utc)
    record(got_at is not None and got_at != was,
           "…and specifically NOT London midnight on the school's open date, "
           "which is exactly what it used to be",
           "stored %s · the old clamp would have stored %s"
           % (stored, was.isoformat()))

    # ── (3) BOTH HALVES OF THE RULING, FROM ONE PUPIL'S ONE READ ──────
    #
    # ⊕ REVERSED, and this is the assertion Mide's ticket is actually about.
    # It used to read `student_404_before_release — the child cannot see it in
    # the week`, with a companion demanding 404 on the id. Both passed. Both
    # described work a teacher had set, been told was set, and no child could
    # open.
    #
    # ⚠️ ONE REQUEST, TWO CLAIMS, AND THEY ARE ABOUT DIFFERENT THINGS.
    #   `week_work`             → what the child can open        (must CONTAIN it)
    #   `reason` + `assignment` → the AUTOMATIC producer          (must be HELD)
    # Split across two requests these could disagree about the clock, the
    # teaching week or the class and both still be green.
    st, seen = call("GET", "/api/class/current-assignment?class_id=" +
                    FX.C_KS3_HELD, t_pupil_b)
    titles = [w.get("title") for w in ((seen or {}).get("week_work") or [])]
    record(st == 200 and (TITLE + " · released into the hold") in titles,
           "student_sees_teacher_work_during_the_hold — the child in the HELD "
           "school sees the work IMMEDIATELY, with no clock moved and the "
           "hold still standing",
           "status %s · week_work: %s" % (st, titles))

    record((seen or {}).get("reason") == "assignments_not_open_yet"
           and (seen or {}).get("assignment") is None,
           "auto_still_held_in_the_same_breath — and in the SAME response the "
           "AUTOMATIC producer is still refusing to compose for that school",
           "reason %r · assignment %r"
           % ((seen or {}).get("reason"),
              ((seen or {}).get("assignment") or {}).get("id")))
    record(((seen or {}).get("detail") or {}).get("opens_on") == open_from,
           "…and it names the same open date /scope reported, so the two "
           "halves are talking about one hold rather than two",
           "opens_on %r · open_from %r"
           % (((seen or {}).get("detail") or {}).get("opens_on"), open_from))

    # ⚠️ AND THE CHILD CAN ACTUALLY OPEN IT, not merely see the title. A route
    # can list work in a week and still 404 the questions — which is exactly
    # what the old behaviour did, and listing without opening would be a
    # crueller version of the same bug.
    st, direct = call("GET", "/api/class/current-assignment?class_id=%s"
                      "&assignment_id=%s" % (FX.C_KS3_HELD, aid), t_pupil_b)
    record(st == 200 and (direct.get("assignment") or {}).get("id") == aid
           and len(direct.get("questions") or []) == len(ids),
           "…and can OPEN it by its id, with its questions, while the school "
           "is still held",
           "status %s · %d question(s)"
           % (st, len(direct.get("questions") or [])))

    # ── (4) THE REFUSAL THAT REMAINS, AND WHY IT IS ASSERTED HERE ─────
    #
    # ⚠️ REMOVING THE CLAMP REMOVES THE ONLY REASON `bad_due_at` EVER FIRED IN
    # PRACTICE, and a validator with nothing left to refuse is a validator
    # nobody notices losing. Due BEFORE the release the TEACHER typed is still
    # impossible and still 400s — nothing to do with any school.
    st, bad = post_set(t_teacher, class_ids=[FX.C_KS3_HELD], tier="medium",
                       scope_ref=unit["id"], question_ids=ids,
                       title=TITLE + " · due before its own release",
                       release_at=(NOW + timedelta(days=7)).isoformat(),
                       due_at=(NOW + timedelta(days=1)).isoformat())
    record(st == 400 and (bad or {}).get("error") == "bad_due_at",
           "due_before_release_still_refused — release next week, due "
           "tomorrow: 400 `bad_due_at`, so the validator did not leave with "
           "the clamp",
           "status %s %s" % (st, json.dumps(bad)[:160]))

    return aid


# ════════════════════════════════════════════════════════════════════════
# 6 · AUTO COMPOSITION IS UNCHANGED (RISKS D7)
# ════════════════════════════════════════════════════════════════════════
def compose_ids(t_pupil, class_id):
    """The ids the AUTOMATIC producer composes for this class, right now."""
    st, body = call("GET", "/api/class/current-assignment?class_id=" + class_id,
                    t_pupil)
    a = (body or {}).get("assignment") or {}
    if a.get("source") not in (None, "auto") and a.get("source") != "auto":
        pass
    return st, a, [q.get("question_ref") for q in (body or {}).get("questions") or []]


def check_auto_unchanged(t_teacher, t_pupil, scopes):
    print("\n6 · the automatic weekly work does not move when Set work runs")

    # ⚠️ COMPOSED BEFORE AND AFTER, ON THE SAME CLASS, AROUND A REAL SET WORK
    # WRITE. The danger D7 names is not that Set work overwrites an assignment
    # — it is that the CONTENT LANES' new rows, at bank_position 12 and up,
    # change what `composeFromBank` draws. The ceiling that stops it is
    # `bank_position < 12` inside `bankFor`, and a ceiling is invisible until
    # something reads past it.
    st, a_before, before = compose_ids(t_pupil, FX.C_KS3_A)
    if st != 200 or not before:
        record(False, "an automatic assignment composes for 8a/Sc1",
               "status %s, %d question(s), reason %r"
               % (st, len(before), (a_before or {}).get("id")))
        return
    record(True, "an automatic assignment composed", "%d question(s)" % len(before))

    st, prev = preview(t_teacher, FX.C_KS3_A, "hard", "topic", "B1", 6)
    ids = [q["id"] for q in (prev.get("picked") or [])]
    post_set(t_teacher, class_ids=[FX.C_KS3_A], tier="hard", scope_ref="B1",
             question_ids=ids, title=TITLE + " · auto neighbour")

    st, a_after, after = compose_ids(t_pupil, FX.C_KS3_A)
    record(after == before,
           "auto_composition_unchanged — the automatic set is byte-identical "
           "before and after a teacher sets work on the same class in the "
           "same week", "%d ids, unchanged" % len(before) if after == before
           else "before %s\n        after  %s" % (before[:6], after[:6]))

    # ── the ceiling, measured through the API ─────────────────────────
    #
    # ⚠️ THE ONLY HONEST WAY TO SAY "bankFor IGNORES POSITION ≥ 12" FROM OUT
    # HERE. Take the ids the auto producer actually served and look up every
    # one's `bank_position` in the authored bank. A lesson topped up to 40 rows
    # would hand back a position ≥ 12 the moment the ceiling was dropped —
    # which is exactly the change that would silently recompose every automatic
    # assignment in the school.
    import ks3_data.question_bank as qb
    pos = {}
    grown = set()
    for entry in qb.load_bank():
        if len(entry["questions"]) > 12:
            grown.add(entry["lesson"])
        for i, q in enumerate(entry["questions"]):
            pos[q["id"]] = i
    over = [(i, pos[i]) for i in after if i in pos and pos[i] >= 12]
    record(not over,
           "auto_ignores_positions_ge_12 (through the API) — every id the "
           "producer served sits in the frozen window 0..11",
           "%d id(s), max position %d; %d lesson(s) in the bank now hold more "
           "than twelve" % (len(after), max([pos[i] for i in after if i in pos]
                                            or [-1]), len(grown))
           if not over else "SERVED FROM ABOVE THE CEILING: %s" % over[:5])
    record(bool(grown),
           "…and the window is a real window: lessons above twelve rows exist, "
           "so a dropped ceiling would show", "%d topped-up lesson(s)" % len(grown))


# ════════════════════════════════════════════════════════════════════════
# 7 · THE ADMIN CORRECTION (RISKS D12) AND THE 'LAST SET' TAG (C13)
# ════════════════════════════════════════════════════════════════════════
def check_admin_and_lastset(t_teacher, t_admin, admin_id):
    print("\n7 · an admin corrects a class's cohort, and it is audited")

    st, before = rest("GET", "/rest/v1/classes?id=eq.%s&select=tier,"
                             "science_pathway,science_subject,tier_pathway_source"
                      % FX.C_KS4_COMB, t_admin)
    was = before[0] if isinstance(before, list) and before else {}

    # A plain teacher must NOT be able to do this: a class's tier decides which
    # questions a child is served, which is a teaching decision.
    st, out = call("POST", "/api/admin/class-tier", t_teacher,
                   {"class_id": FX.C_KS4_COMB, "tier": "higher",
                    "pathway": "combined", "subject": None})
    record(st == 403 and (out or {}).get("error") == "admin_required",
           "a plain teacher cannot change a class's tier",
           "status %s %s" % (st, json.dumps(out)[:120]))

    st, out = call("POST", "/api/admin/class-tier", t_admin,
                   {"class_id": FX.C_KS4_COMB, "tier": "higher",
                    "pathway": "combined", "subject": None})
    ok = record(st == 200 and (out.get("class") or {}).get("tier") == "higher",
                "admin_edit_audited — the school admin can correct it",
                "status %s %s" % (st, json.dumps(out)[:200]))
    if ok:
        record((out.get("class") or {}).get("tier_pathway_source") == "admin",
               "…and the row now records that a PERSON decided, not the name "
               "rule — which is what stops a re-import overwriting it",
               "source %s (was %s)" % ((out.get("class") or {}).get(
                   "tier_pathway_source"), was.get("tier_pathway_source")))
        st, aud = rest("GET", "/rest/v1/audit_log?target_id=eq.%s&"
                              "action=eq.class.tier_pathway.set&"
                              "select=action,payload&order=created_at.desc&limit=1"
                       % FX.C_KS4_COMB, t_admin)
        row = aud[0] if isinstance(aud, list) and aud else {}
        p = row.get("payload") or {}
        record(row.get("action") == "class.tier_pathway.set"
               and p.get("acting_as_admin") is True
               and (p.get("from") or {}).get("tier") == was.get("tier")
               and (p.get("to") or {}).get("tier") == "higher",
               "admin_edit_audited — an audit_log row names who, what from "
               "and what to", json.dumps(p)[:240])

    # The incoherent triple is refused: a combined class has no separate
    # science, and a triple one must say which.
    st, out = call("POST", "/api/admin/class-tier", t_admin,
                   {"class_id": FX.C_KS4_COMB, "tier": "higher",
                    "pathway": "combined", "subject": "biology"})
    record(st == 400 and (out or {}).get("error") == "bad_triple",
           "a combined class with a separate science is refused as incoherent",
           "status %s %s" % (st, json.dumps(out)[:140]))
    st, out = call("POST", "/api/admin/class-tier", t_admin,
                   {"class_id": FX.C_KS3_A, "tier": "higher",
                    "pathway": "combined", "subject": None})
    record(st == 400 and (out or {}).get("error") == "not_ks4",
           "a KS3 class has no tier to set", "status %s %s"
           % (st, json.dumps(out)[:140]))

    # Put it back where the name rule says, so the world is idempotent.
    call("POST", "/api/admin/class-tier", t_admin,
         {"class_id": FX.C_KS4_COMB, "tier": "foundation",
          "pathway": "combined", "subject": None})

    # ── C13 · last_set_tag ────────────────────────────────────────────
    print("\n   the 'last set' tag")
    st, scope = scope_of(t_teacher, FX.C_KS3_A)
    tags = {t["id"]: t.get("last_set_at") for t in (scope or {}).get("tree") or []}
    record(tags.get("B1"),
           "last_set_tag — the unit this drive set work on carries a date",
           "B1 last_set_at %s" % tags.get("B1"))
    untouched = [k for k, v in tags.items() if v is None]
    record(bool(untouched),
           "…and a unit nobody has set carries none, so the tag is a fact "
           "about THIS class and not a constant",
           "%d unit(s) untagged, e.g. %s" % (len(untouched), untouched[:3]))


# ════════════════════════════════════════════════════════════════════════
# 8 · THE SHEET, IN A REAL BROWSER, AT 390px
# ════════════════════════════════════════════════════════════════════════
#
# ⚠️ ONE BROWSER PER PERSONA, RUN SEQUENTIALLY. Two Chromes and two node
# servers on one laptop is how a gate starts failing for reasons that have
# nothing to do with the code — and a drive that fails for the machine's
# reasons is one people re-run rather than read.
#
# ⚠️ DEVICE METRICS BEFORE NAVIGATING. Headless Chrome floors its WINDOW width
# at about 500px, so `--window-size=390` silently produces a 500px layout and
# then crops the image: a screenshot 390 pixels across showing the wrong
# layout. `set_viewport` overrides device metrics, which reflows at the true
# CSS width so a 390px media query fires as it does on a phone.

# ⚠️ THE CLICK AND THE WAIT ARE TWO SEPARATE EVALUATIONS, AND THEY HAVE TO BE.
#
# `signIn()` ends in `redirectAfterAuth()`, which NAVIGATES. An in-page async
# helper that clicked the button and then awaited the token for twenty seconds
# was therefore awaiting inside an execution context the sign-in it had just
# triggered was busy destroying — and CDP answered `Inspected target navigated
# or closed (-32000)`, as an exception, out of the middle of a check whose
# subject was a teacher signing in successfully. It killed a run that had
# ninety-two green checks behind it, and the message pointed at the browser
# rather than at the sign-in.
#
# So the click returns immediately, and the token is polled for from HERE, one
# short evaluation at a time, with a destroyed context treated as "the redirect
# is happening, ask again" rather than as a failure. `localStorage` is
# same-origin and survives the navigation, which is what makes it the right
# thing to watch.
CLICK_SIGN_IN_JS = """
(function () {
  var e = document.getElementById('signin-email');
  var p = document.getElementById('signin-password');
  var b = document.getElementById('btn-signin');
  if (!e || !p || !b) { return 'no sign-in form'; }
  e.value = %s; p.value = %s;
  b.click();
  return 'clicked';
})()
"""

TOKEN_JS = ("(Object.keys(localStorage).filter(function(k){"
            "return k.indexOf('-auth-token') > -1;})[0] || '')")


# Every string the sheet is allowed to say in its CHROME — RISKS A9's list,
# asserted rather than described. Topic names, subtopic names, counts, question
# stems and option texts are DATA and are not in here; the sweep below reads
# only labels, chips, buttons, tags and the two status lines.
FAFF_EXACT = {
    "Classes", "Topic", "Detail", "Next", "Set work", "Back", "Cancel",
    "Close", "Swap", "Tier", "Subject", "Paper", "Topics", "Questions",
    "Title", "Release", "Due",
    "Foundation", "Higher", "Easy", "Medium", "Hard",
    "Biology", "Chemistry", "Physics", "All",
    "Paper 1", "Paper 2", "Both",
    "5", "10", "15", "20",
    "A.", "B.", "C.", "D.",
    "Now", "Later",
    "Not set yet", "Set this week", "Unavailable", "Not set",
    # ⊕ MRB-336 §6 — EDIT. `Save` is the primary's verb on a row that
    # already exists; `Not saved` is the refusal toast beside `Not set`, and
    # is a second failure WORD rather than a third sentence — a teacher who
    # pressed Save has to be told that nothing was saved, and "Not set"
    # would be a lie about a set that is already out.
    "Save", "Not saved",
}
# ⚠️ A SECOND SET, AND SPLITTING THEM IS THE POINT RATHER THAN A CONCESSION.
# These four are `aria-label`s on the date and time inputs and are never
# rendered. The visible label above each PAIR is one word — "Release", "Due" —
# so a screen reader meeting the two boxes under it would announce two
# identical unlabelled edit boxes; these are what make them "Release date" and
# "Release time". A9 bans SENTENCES on the screen, not accessible names, and
# deleting them to make a string list shorter would trade a real
# accessibility fact for a cosmetic one.
#
# So the drive asserts three things instead of one: every string in SAY is in
# one of the two sets; none of THESE four appears in the sheet's visible text;
# and each is actually carried by an input, so the exemption is paying for
# itself rather than being a hole four strings wide.
FAFF_ARIA = {"Release date", "Release time", "Due date", "Due time"}
# The four composed strings, each a label plus a number.
#
# ⊕ MRB-336 — `Assignments open <date>` WAS THE FIFTH, and it is deleted
# rather than merely unused. The school hold no longer governs work a teacher
# sets by hand, so the sheet has nothing to disclose about it and emits no
# `.sw-hold` node at all. Left in this list it would be a permission for a
# string the sheet can no longer produce — which is how a faff sweep quietly
# stops sweeping.
FAFF_PATTERNS = [
    re.compile(r"^Set \d+ weeks? ago$"),
    re.compile(r"^\d+ students?$"),
    re.compile(r"^\d+\.$"),                      # the question number, "1."
    re.compile(r"^.{1,80} · .+$"),               # the toast: title · class(es)
]

READ_CHROME_JS = r"""
(function () {
  var o = document.querySelector('[data-sw="overlay"]');
  if (!o) { return JSON.stringify({err: 'no overlay'}); }
  var sel = '.sw-label,.sw-chip,.sw-btn,.sw-step,.sw-row-tag,.sw-swap,' +
            '.sw-hold,.sw-opt-k,.sw-q-n';
  var out = [];
  var nodes = o.querySelectorAll(sel);
  for (var i = 0; i < nodes.length; i++) {
    var n = nodes[i];
    if (n.offsetParent === null && n.tagName !== 'BODY') { continue; }
    var t = (n.textContent || '').trim();
    if (t) { out.push(t); }
  }
  var toast = document.querySelector('[data-sw="toast"]');
  if (toast && !toast.hidden) { out.push((toast.textContent || '').trim()); }
  return JSON.stringify(out);
})()
"""


# ⚠️ ONE HARNESS ARTEFACT, NAMED, BECAUSE IT LOOKS EXACTLY LIKE A DEFECT.
# `shared/teacher-live.js:3368` fires a hardcoded, fire-and-forget
# `fetch('https://mrbadmus-backend.onrender.com/api/health')` on every teacher
# page — a deliberate warm-up of PRODUCTION's Render dyno, `.catch(){}` so it
# can never affect the page. It ignores `?api=` by design, because warming the
# local backend is not what it is for. Under a drive it is cross-origin to a
# host that does not allow-list `localhost:5533`, so the browser logs a CORS
# error for a request whose failure is already handled. Filtering it by its
# URL rather than by a generic "ignore CORS" rule keeps every OTHER blocked
# request visible — and a page silently talking to production instead of the
# local backend is exactly the failure this drive must not hide.
#
# ⚠️ AND ONE PRE-EXISTING DEFECT, WHICH IS A DIFFERENT THING FROM AN ARTEFACT
# AND IS FILTERED ONLY BECAUSE IT IS PROVED TO PREDATE THIS TICKET.
# `shared/teacher-ds.css` and `shared/student-ds.css` each declare the SAME
# font face twice: once as `url('../fonts/…')`, which from `/shared/` resolves
# to `/fonts/…` and 404s, and then again as `url('/shared/fonts/…')`, which is
# where the file actually is. The second rule wins, so the font renders and the
# 404 is a console line and nothing else. MEASURED: `shared/teacher-ds.css` is
# md5-identical at 7f03fc8ce (the merge-base) and today — fba5f719… both sides
# — and it last changed at MRB-287. It is reported as a finding on the teacher
# surface; deleting the broken first rule is a one-line fix for whoever next
# owns those files, and is not MRB-335's to make.
CONSOLE_NOISE = (
    "favicon",
    "mrbadmus-backend.onrender.com/api/health",
    "/fonts/instrument-sans-var",
)


def real_errors(errs):
    return [e for e in errs if not any(n in e for n in CONSOLE_NOISE)]


def record_console(p, when):
    errs = real_errors(p.console_errors())
    return record(not errs,
                  "the browser logged no console error %s" % when,
                  "clean (the prod dyno warm-up ping is filtered by URL and "
                  "named in CONSOLE_NOISE)" if not errs
                  else "; ".join(errs[:3]))


def js(p, expr):
    return p.eval(expr)


def goto_ready(p, url, ready, settle=2.5, tries=4):
    """Navigate, then wait for the page to be the one we asked for.

    ⚠️ `Inspected target navigated or closed` IS NOT A PRODUCT FAILURE AND
    MUST NOT BE ALLOWED TO LOOK LIKE ONE. `auth.html` decides late what to
    render — it checks for an existing session and may navigate — and
    `page(url, settle=N)` returns after a fixed wait, so an `eval` issued on
    the far side of that wait can land while the target is mid-navigation and
    dies with CDP -32000. It killed a whole run at the first sign-in, with a
    stack trace, after ninety-two green API checks.

    So the wait is on a FACT about the page (`ready`) rather than on a clock,
    and a navigation during the probe is retried rather than raised. A page
    that genuinely never arrives still fails — this returns False and the
    caller records it — which is the difference between tolerating a flake
    and hiding a failure.
    """
    for attempt in range(tries):
        try:
            p.goto(url, settle=settle)
        except Exception:                                       # noqa: BLE001
            time.sleep(1.0)
            continue
        for _ in range(50):
            try:
                if p.eval(ready):
                    return True
            except Exception:                                   # noqa: BLE001
                pass
            time.sleep(0.3)
    return False


def sign_in_page(p, base, email, pw):
    """Sign in the way a teacher does: through auth.html's own form."""
    if not goto_ready(p, "%s/auth.html?env=test&api=%s" % (base, PAGE_API),
                      "!!document.getElementById('btn-signin')"):
        return "auth.html never rendered its sign-in form"
    try:
        clicked = p.eval(CLICK_SIGN_IN_JS % (json.dumps(email), json.dumps(pw)))
    except Exception as e:                                      # noqa: BLE001
        return "could not press Sign In: %s" % e
    if clicked != "clicked":
        return str(clicked)
    for _ in range(80):
        time.sleep(0.3)
        try:
            key = p.eval(TOKEN_JS)
        except Exception:                                       # noqa: BLE001
            continue          # mid-redirect; the context is being replaced
        if key:
            return "ok " + key
    return "no session in localStorage 24s after pressing Sign In"


def wait_for(p, expr, tries=60, gap=0.25):
    for _ in range(tries):
        try:
            if p.eval(expr):
                return True
        except Exception:                                       # noqa: BLE001
            pass
        time.sleep(gap)
    return False


# The page the sheet lives on, remembered once so `open_sheet` can put itself
# back there. Set by `check_sheet`.
SHEET_PAGE = {"base": None}


def ensure_sheet_page(p, class_id=None):
    """Make sure the tab is on a page that actually carries the sheet module.

    ⚠️ NOT EVERY TEACHER PAGE LOADS `shared/set-work.js`. `teacher/admin.html`
    is one of the four HAND-WRITTEN teacher pages and carries no sheet at all,
    so a check that drove the admin screen left the tab somewhere
    `window.MRBSetWork` does not exist — and the next check to call
    `MRBSetWork.open` died with `Cannot read properties of undefined`, out of
    the middle of a check about a swap race.

    Making the sheet checks depend on the ORDER they are called in is the kind
    of coupling that survives exactly until somebody inserts a check between
    two others. So the dependency is stated instead: anything that opens the
    sheet says so, and gets put back if it needs to be.
    """
    try:
        if p.eval("!!(window.MRBSetWork && window.MRBSetWork.open)"):
            return True
    except Exception:                                           # noqa: BLE001
        pass
    base = SHEET_PAGE.get("base")
    if not base:
        return False
    p.set_viewport(390, 844)
    return goto_ready(p, "%s/teacher/class-detail.html?class=%s&env=test&api=%s"
                      % (base, class_id or FX.C_KS4_COMB, PAGE_API),
                      "!!(window.MRBSetWork && window.MRBSetWork.open)",
                      settle=6.0)


def open_sheet(p, class_id, wait_tree=True):
    ensure_sheet_page(p, class_id)
    p.eval("window.MRBSetWork.open({classId: %s})" % json.dumps(class_id))
    if wait_tree:
        return wait_for(p, "document.querySelectorAll('[data-sw=\"topic\"]')"
                           ".length > 0")
    return True


def sw_click(p, sel, index=0):
    return p.eval("(function(){var n=document.querySelectorAll(%s)[%d];"
                  "if(!n){return false;} n.click(); return true;})()"
                  % (json.dumps(sel), index))


def check_sheet(b, base, sess, class_ids, shots):
    """The sheet itself, as a teacher on a phone."""
    print("\n8 · the sheet, at 390px, as the teacher")
    key = anon_key()
    url = FX.env("SUPABASE_URL")

    p = b.attach()
    # ⚠️ METRICS FIRST. See the note above this section.
    p.set_viewport(390, 844)
    signed = sign_in_page(p, base, FX.TEACHER_EMAIL, os.environ[FX.ENV_SWITCH])
    if not record(str(signed).startswith("ok"),
                  "the teacher signs in through auth.html, for real", signed):
        return

    p.set_viewport(390, 844)
    SHEET_PAGE["base"] = base
    if not goto_ready(p, "%s/teacher/class-detail.html?class=%s&env=test&api=%s"
                      % (base, FX.C_KS4_COMB, PAGE_API),
                      "!!(window.MRBSetWork && window.MRBSetWork.open)",
                      settle=6.0):
        record(False, "the teacher's class screen loads with the sheet module")
        return

    # ── the trigger the generated page actually carries ───────────────
    pressed = p.eval(r"""(function(){
      var bs = document.querySelectorAll('button, a');
      for (var i = 0; i < bs.length; i++) {
        if ((bs[i].textContent || '').trim() === 'Set work'
            && bs[i].offsetParent !== null) { bs[i].click(); return true; }
      }
      return false;})()""")
    opened = wait_for(p, "(function(){var o=document.querySelector("
                         "'[data-sw=\"overlay\"]');return o && !o.hidden;})()")
    record(pressed and opened,
           "the generated page's own 'Set work' button opens the sheet",
           "pressed %s, overlay visible %s" % (pressed, opened))
    record(p.eval("document.querySelector('[data-sw=\"overlay\"]')"
                  ".getAttribute('data-sw-class')") == FX.C_KS4_COMB,
           "…and it opens on THIS class — the counter and the class id are "
           "on the overlay so a sweep reads a number instead of inferring "
           "from a screenshot",
           p.eval("document.querySelector('[data-sw=\"overlay\"]')"
                  ".getAttribute('data-sw-opens')"))

    # ── the sheet, driven directly from here on ───────────────────────
    if not open_sheet(p, FX.C_KS4_COMB):
        record(False, "the combined class's tree loads in the sheet")
        return
    record(True, "the tree loads",
           "%s topic row(s)" % p.eval("document.querySelectorAll("
                                      "'[data-sw=\"topic\"]').length"))

    # ── C11 (rendered) · the tier chip lands on the class's tier ──────
    on = p.eval("(function(){var c=document.querySelector("
                "'[data-sw=\"tier-chips\"] .is-on');return c?c.textContent:'';})()")
    record(on == "Foundation",
           "tier_default_matches_rule (rendered) — 10b/Sc5 opens on Foundation",
           "chip on: %r" % on)

    # ── C5 (rendered) · no subject chips on a separate-science class ──
    p.eval("window.MRBSetWork.close()")
    open_sheet(p, FX.C_KS4_SEPS)
    hidden = p.eval("(function(){var c=document.querySelector("
                    "'[data-sw=\"subject-chips\"]');return !!(c && c.hidden);})()")
    ph_on = p.eval("(function(){var c=document.querySelector("
                   "'[data-sw=\"tier-chips\"] .is-on');return c?c.textContent:'';})()")
    record(hidden and ph_on == "Higher",
           "seps_sees_own_subject_only (rendered) — 10c/Ph1 gets NO subject "
           "chips at all, and opens on Higher",
           "subject rail hidden %s, tier chip %r" % (hidden, ph_on))
    # ── ⊕ MRB-336, 8 Sep 2026 · THE PAPER CHIPS COME TO TRIPLE ───────
    #
    # ⛔ This read the other way round and passed:
    #
    #     papers_hidden = p.eval(… "[data-sw=\"paper-chips\"]" … ".hidden")
    #     record(papers_hidden,
    #            "…and no paper chips either — papers are a combined idea")
    #
    # Papers are not a combined idea. AQA examines Triple Physics on Physics
    # Paper 1 and Physics Paper 2, with their own dates, and "everything on
    # paper 1 before the mock" is the single most common thing a separate-
    # sciences teacher wants to set. The rail was withheld from the one cohort
    # that most needed it.
    #
    # ⚠️ THE RAIL IS DATA-DRIVEN AND THAT IS WHY THIS IS A SEPARATE CHECK FROM
    # THE `/scope` ONE. `syncPapers` renders whatever `S.scope.papers` holds
    # (`shared/set-work.js`: `show = !!(papers && papers.length)`), so the
    # data check above and this one could in principle come apart — a build
    # that served the list and left the rail `hidden` would pass the first and
    # fail here, which is exactly the failure a data-only gate would miss.
    ph_papers = p.eval("""(function(){
        var c = document.querySelector('[data-sw="paper-chips"]');
        return {hidden: !!(c && c.hidden), present: !!c,
                chips: c ? Array.prototype.map.call(
                  c.querySelectorAll('.sw-chip'),
                  function(n){return n.textContent;}) : []};})()""")
    record(ph_papers["present"] and not ph_papers["hidden"]
           and ph_papers["chips"] == ["Paper 1", "Paper 2", "Both"],
           "⊕ MRB-336: paper_chips_on_triple — 10c/Ph1 DOES get the paper "
           "rail, with both papers and Both, even though it gets no subject "
           "chips at all", json.dumps(ph_papers))

    # ⚠️ AND THE RAIL FILTERS. A chip that renders and does nothing is worse
    # than no chip: the teacher taps Paper 1, the list does not change, and
    # they set the whole subject believing they narrowed it. `space` is the
    # row to watch — physics paper 2, triple-only, and the topic the combined
    # tree cannot see at all.
    # ⚠️ VISIBILITY IS ASKED OF THE LAYOUT, NOT OF THE ELEMENT'S OWN
    # `hidden` PROPERTY, and the difference cost a red on the first run.
    # `syncTree` hides the topic's WRAPPER (`r.wrap.hidden = …`, set-work.js
    # :1078), not the `[data-sw="topic"]` row inside it — so `row.hidden` is
    # `false` on every row whatever the filter is doing, because `.hidden`
    # reflects the attribute on THAT element and says nothing about an
    # ancestor. Reading it made a working filter look broken.
    #
    # ⚠️ AND THE FAILURE DIRECTION WOULD HAVE BEEN THE OTHER WAY ROUND
    # ANYWHERE ELSE. Here the mistake produced a red on correct code, which is
    # the safe kind; a check written the same way but asserting something IS
    # hidden would have gone GREEN on a filter that had stopped filtering.
    # `getClientRects()` is empty for anything not laid out, for any reason.
    def _rows():
        return p.eval("""(function(){
            var out = [];
            var rs = document.querySelectorAll('[data-sw="topic"]');
            for (var i = 0; i < rs.length; i++) {
              if (rs[i].getClientRects().length) {
                out.push(rs[i].getAttribute('data-sw-ref')
                         || rs[i].textContent.trim()); }}
            return out;})()""")

    def _tap(label):
        p.eval("""(function(){var cs=document.querySelectorAll(
            '[data-sw="paper-chips"] .sw-chip');
            for(var i=0;i<cs.length;i++){
              if(cs[i].textContent===%s){cs[i].click();return true;}}
            return false;})()""" % json.dumps(label))
        time.sleep(0.4)

    # ⚠️ ADVANCE TO THE TOPIC STEP FIRST. The sheet opens on the CLASSES
    # step and the topic panel is `display:none` until Next is pressed — so
    # the rows exist, carry their refs, and are laid out nowhere. Measuring
    # there returns zero rows under every chip, which reads as "the filter
    # hides everything" rather than as "nothing is on screen yet".
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    time.sleep(0.6)
    wait_for(p, "(function(){var r=document.querySelector('[data-sw=\"topic\"]');"
                "return !!r && r.getClientRects().length > 0;})()")
    _tap("Both")
    both = _rows()
    _tap("Paper 1")
    p1 = _rows()
    _tap("Paper 2")
    p2 = _rows()
    _tap("Both")
    joined = sorted(set(p1) | set(p2))
    record(both and p1 and p2 and set(p1) & set(p2) == set()
           and joined == sorted(set(both)),
           "⊕ MRB-336: paper_chips_partition_the_triple_tree — Paper 1 and "
           "Paper 2 are disjoint and together are exactly the whole tree, so "
           "no topic is unreachable by paper",
           "both %d · p1 %d · p2 %d · overlap %s"
           % (len(both), len(p1), len(p2), sorted(set(p1) & set(p2))[:3]))
    record(any("space" in str(r).lower() for r in p2)
           and not any("space" in str(r).lower() for r in p1),
           "…and `space` — triple-only, and invisible to a combined class — "
           "is reachable under Paper 2 and only under Paper 2",
           "paper 2 rows: %s" % [r for r in p2 if "space" in str(r).lower()])

    p.eval("window.MRBSetWork.close()")
    open_sheet(p, FX.C_KS4_COMB)
    record(p.eval("(function(){var c=document.querySelector("
                  "'[data-sw=\"subject-chips\"]');return !!(c && !c.hidden);})()")
           and p.eval("document.querySelectorAll("
                      "'[data-sw=\"paper-chips\"] .sw-chip').length") == 3,
           "…while the combined class DOES get subject and paper chips, "
           "or 'hidden' would pass by being hidden everywhere",
           "paper chips: %s"
           % p.eval("Array.from(document.querySelectorAll("
                    "'[data-sw=\"paper-chips\"] .sw-chip')).map("
                    "function(n){return n.textContent;})"))
    return p


# ── A1 · scroll_unchanged_on_select ─────────────────────────────────────
#
# THE ROOT CAUSE, and why it can only be measured by scrolling. v1's sheet was
# Design's compiled node, rendered by `student-runtime.js`, whose `draw()`
# EMPTIES the entire mount host and rebuilds it (`host.textContent = ""` at
# :497). It restores focus, form values and the DOCUMENT's scroll — and no
# element's `scrollTop`, because it holds no record of one. Design's sheet is
# its own inner scroller, so every tap of a topic destroyed the node holding
# the teacher's place and replaced it with one at zero.
#
# Nothing about that is visible in a string, a class name or a payload. It is
# visible in exactly one number.
SCROLL_JS = """(function(){var s=document.querySelector('[data-sw="sheet"]');
  return s ? {top: s.scrollTop, h: s.scrollHeight, c: s.clientHeight} : null;})()"""


def check_scroll(p, shots):
    print("\n   scroll, sticky and sideways at 390px")
    open_sheet(p, FX.C_KS4_COMB)

    # Step 0 is the class list and is short; the tree on step 1 is the long one.
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    time.sleep(0.4)
    geom = p.eval(SCROLL_JS)
    if not geom or geom["h"] <= geom["c"] + 40:
        record(False, "the topic list is long enough to scroll at 390px",
               "scrollHeight %s clientHeight %s" % (geom and geom["h"],
                                                    geom and geom["c"]))
        return
    record(True, "the topic list scrolls at 390px",
           "%dpx of content in a %dpx scroller" % (geom["h"], geom["c"]))

    # Scroll a long way down, then tap things. Nothing may move the scroller.
    target = int((geom["h"] - geom["c"]) * 0.6)
    p.eval("document.querySelector('[data-sw=\"sheet\"]').scrollTop = %d" % target)
    time.sleep(0.3)
    start = p.eval(SCROLL_JS)["top"]

    moves = []

    def tap(label, expr):
        before = p.eval(SCROLL_JS)["top"]
        did = p.eval(expr)
        time.sleep(0.35)
        after = p.eval(SCROLL_JS)["top"]
        moves.append((label, did, before, after))
        return did, before, after

    # A topic in view, its chevron, a subtopic under it, and a tier chip.
    tap("a topic row", """(function(){var s=document.querySelector(
        '[data-sw="sheet"]'), rs=document.querySelectorAll('[data-sw="topic"]');
        for(var i=0;i<rs.length;i++){var r=rs[i].getBoundingClientRect();
          if(r.top>60 && r.bottom<s.getBoundingClientRect().bottom
             && rs[i].getAttribute('aria-disabled')!=='true'){
            rs[i].click(); return rs[i].getAttribute('data-sw-ref');}}
        return false;})()""")
    tap("a chevron", """(function(){var s=document.querySelector(
        '[data-sw="sheet"]'), cs=document.querySelectorAll('[data-sw="chevron"]');
        for(var i=0;i<cs.length;i++){var r=cs[i].getBoundingClientRect();
          if(r.top>60 && r.bottom<s.getBoundingClientRect().bottom && !cs[i].hidden){
            cs[i].click(); return true;}}
        return false;})()""")
    tap("a subtopic row", """(function(){var s=document.querySelector(
        '[data-sw="sheet"]'), rs=document.querySelectorAll('[data-sw="subtopic"]');
        for(var i=0;i<rs.length;i++){var r=rs[i].getBoundingClientRect();
          if(r.top>60 && r.bottom<s.getBoundingClientRect().bottom
             && rs[i].getAttribute('aria-disabled')!=='true'){
            rs[i].click(); return rs[i].getAttribute('data-sw-ref');}}
        return false;})()""")
    tap("a tier chip", """(function(){var cs=document.querySelectorAll(
        '[data-sw="tier-chips"] .sw-chip');
        for(var i=0;i<cs.length;i++){if(!cs[i].classList.contains('is-on')){
          cs[i].click(); return cs[i].textContent;}} return false;})()""")

    reached = [m for m in moves if m[1]]
    jumped = [m for m in reached if m[2] != m[3]]
    record(len(reached) >= 4 and not jumped,
           "scroll_unchanged_on_select — %d control(s) tapped %dpx down a "
           "scrolled list, and the scroller did not move" % (len(reached), start),
           "; ".join("%s %s→%s" % (m[0], m[2], m[3]) for m in reached)
           if not jumped else
           "JUMPED: %s" % "; ".join("%s %s→%s" % (m[0], m[2], m[3])
                                    for m in jumped))
    # ⚠️ AND THE CONTROLS MUST HAVE DONE SOMETHING. A sheet whose taps were all
    # no-ops would keep its scroll perfectly. The tier chip is the cheapest
    # proof: it re-counts in place.
    record(len(reached) >= 4,
           "…and every one of those taps landed on a live control, so the "
           "check is not passing on a dead sheet",
           "%d of %d reachable" % (len(reached), len(moves)))

    # ── the subject chip is a FILTER, and is measured differently ──────
    #
    # ⚠️ IT IS NOT ALLOWED TO RESET, BUT IT IS ALLOWED TO CLAMP, and reading
    # the first as the second is how this check goes red on correct code.
    # Filtering to one science hides two thirds of the rows, so the list
    # genuinely gets shorter and the browser pins `scrollTop` to the new
    # maximum. Measured: 949 → 184, where 184 was exactly
    # `scrollHeight - clientHeight` afterwards. A re-render jump goes to 0;
    # a clamp goes to the end of the shorter list. So the property is "the
    # scroller did not move UNLESS it had nowhere left to be, and then it
    # sits at the new end" — which is also the check that would catch a
    # filter that silently reset to the top.
    before = p.eval(SCROLL_JS)
    picked = p.eval("""(function(){var cs=document.querySelectorAll(
        '[data-sw="subject-chips"] .sw-chip');
        for(var i=0;i<cs.length;i++){if(!cs[i].classList.contains('is-on')
          && cs[i].textContent!=='All'){cs[i].click(); return cs[i].textContent;}}
        return false;})()""")
    time.sleep(0.4)
    after = p.eval(SCROLL_JS)
    new_max = max(0, after["h"] - after["c"])
    record(bool(picked) and after["top"] == min(before["top"], new_max),
           "scroll_unchanged_on_select — a SUBJECT filter keeps the "
           "teacher's place, or pins it to the end of the shorter list; it "
           "never resets to the top",
           "%s: %d → %d, and the new maximum is %d"
           % (picked, before["top"], after["top"], new_max))
    p.eval("""(function(){var cs=document.querySelectorAll(
        '[data-sw="subject-chips"] .sw-chip');
        for(var i=0;i<cs.length;i++){if(cs[i].textContent==='All'){
          cs[i].click();}} return true;})()""")

    # ── A2/A3 · sticky_header_three_positions ─────────────────────────
    #
    # `position: sticky` inside an `overflow:auto` container is fragile on iOS
    # ≤16 when the scroller is transformed or has an `overflow:hidden`
    # ancestor. The primary action lives in that header (v1's footer scrolled
    # away with the content), so if it unsticks, "Next" leaves the viewport.
    tops = []
    for frac in (0.0, 0.45, 1.0):
        p.eval("(function(){var s=document.querySelector('[data-sw=\"sheet\"]');"
               "s.scrollTop = Math.round((s.scrollHeight - s.clientHeight) * %s);"
               "})()" % frac)
        time.sleep(0.3)
        tops.append(p.eval("""(function(){
          var s = document.querySelector('[data-sw="sheet"]');
          var h = s.querySelector('.sw-head');
          return {head: Math.round(h.getBoundingClientRect().top),
                  sheet: Math.round(s.getBoundingClientRect().top),
                  st: Math.round(s.scrollTop)};})()"""))
    off = [t for t in tops if abs(t["head"] - t["sheet"]) > 1]
    record(not off and len({t["st"] for t in tops}) == 3,
           "sticky_header_three_positions — the header's top equals the "
           "scroller's top at the top, the middle and the bottom of the list",
           "; ".join("scrollTop %d → head %d / sheet %d"
                     % (t["st"], t["head"], t["sheet"]) for t in tops))
    record(p.eval("""(function(){
        var s = document.querySelector('[data-sw="sheet"]');
        var b = s.querySelector('[data-sw="primary"]').getBoundingClientRect();
        return b.top >= 0 && b.bottom <= (window.innerHeight + 1);})()"""),
           "…and the primary action is inside the viewport at the bottom of "
           "the list, which is what v1's footer was not")

    if shots:
        p.screenshot(os.path.join(shots, "A2-sticky-header-390.png"), width=390)


def check_sideways(p, label, shots=None):
    """RISKS A8 / E11, at both widths, on whatever step the sheet is on."""
    out = []
    for w in (390, 1280):
        p.set_viewport(w, 900)
        time.sleep(0.35)
        r = p.eval("""(function(){
          var d = document.documentElement, b = document.body;
          var wide = [];
          var o = document.querySelector('[data-sw="overlay"]');
          if (o && !o.hidden) {
            var ns = o.querySelectorAll('*');
            for (var i = 0; i < ns.length; i++) {
              var n = ns[i];
              if (n.offsetParent === null) { continue; }
              if (n.scrollWidth > n.clientWidth + 1
                  && getComputedStyle(n).overflowX === 'visible') {
                wide.push((n.getAttribute('data-sw') || n.className || n.tagName)
                          + ' ' + n.scrollWidth + '>' + n.clientWidth);
              }
            }
          }
          return {doc: d.scrollWidth, cli: d.clientWidth,
                  body: b.scrollWidth, wide: wide.slice(0, 5)};})()""")
        ok = r["doc"] <= r["cli"] + 1 and not r["wide"]
        out.append((w, ok, r))
        if shots and w == 390:
            p.screenshot(os.path.join(shots, "A8-no-sideways-%s-390.png" % label),
                         width=390)
    p.set_viewport(390, 844)
    bad = [o for o in out if not o[1]]
    return record(not bad,
                  "no_sideways_scroll_390 — %s, at 390 and 1280" % label,
                  "; ".join("%dpx doc %d ≤ %d" % (w, r["doc"], r["cli"])
                            for w, _ok, r in out) if not bad
                  else "; ".join("%dpx doc %d > %d, overflowing: %s"
                                 % (w, r["doc"], r["cli"], r["wide"])
                                 for w, _ok, r in bad))


# ── ⊕ THE STALE-RESPONSE GUARD (found by this drive, 8 Sep 2026) ───────
#
# ⚠️ THE DEFECT THIS PINS WAS NOT REPRODUCIBLE BY WATCHING. It reproduced as
# an unexplained red in `seps_sees_own_subject_only (rendered)` — the sheet
# opened on 10c/Ph1 and drew 10b/Sc5's tree — and re-running made it go away,
# which is the shape of a race rather than a bug in either class's scoping.
#
# So this makes the race deterministic instead of hoping for it: the FIRST
# /scope response is held back two seconds by wrapping `fetch`, so it lands
# AFTER the second one. Nothing about the sheet or the server is stubbed —
# this is ordinary slow-network behaviour, arranged to happen on purpose.
def check_stale_guard(p):
    print("\n   the sheet shows the class it was opened for")

    p.eval("""(function(){
      if (window.__mrbHeld) { return true; }
      window.__mrbHeld = true;
      var real = window.fetch, n = 0;
      window.__mrbRealFetch = real;
      window.fetch = function (u, o) {
        var mine = String(u).indexOf('set-work/scope') > -1 ? ++n : 0;
        return real(u, o).then(function (r) {
          if (mine === 1) {
            return new Promise(function (res) {
              setTimeout(function () { res(r); }, 2000); });
          }
          return r; });
      };
      return true;})()""")

    # 10a/Bi1 is Triple Higher BIOLOGY (7 topics, no subject rail, Higher).
    # 10b/Sc5 is Combined FOUNDATION (24 topics, subject rail, Foundation).
    # Nothing about the two is alike, so a mix-up cannot look like a pass.
    p.eval("window.MRBSetWork.open({classId: %s})" % json.dumps(FX.C_KS4_TRIPLE))
    time.sleep(0.15)
    p.eval("window.MRBSetWork.open({classId: %s})" % json.dumps(FX.C_KS4_COMB))
    time.sleep(4.0)

    got = p.eval("""(function(){
      var o = document.querySelector('[data-sw="overlay"]');
      return {isFor: o.getAttribute('data-sw-class'),
              topics: document.querySelectorAll('[data-sw="topic"]').length,
              tier: (document.querySelector(
                '[data-sw="tier-chips"] .is-on')||{}).textContent,
              subjHidden: document.querySelector(
                '[data-sw="subject-chips"]').hidden};})()""")

    # ⚠️ THE TIER IS THE HALF THAT MATTERS. `S.classId` was always right, so
    # the write went to the right class — at the OTHER class's tier. Most base
    # subtopics are in both trees, so the request is accepted, and a Foundation
    # group is set Higher questions with the chip agreeing they should be.
    record(got["isFor"] == FX.C_KS4_COMB and got["topics"] > 20
           and got["tier"] == "Foundation" and got["subjHidden"] is False,
           "sheet_shows_the_class_it_was_opened_for — a /scope answer for the "
           "class the sheet WAS on cannot paint over the class it is on now, "
           "however late it arrives",
           "flagged %s · %d topics · tier %s · subject rail hidden %s "
           "(10a/Bi1 would be 7 / Higher / True)"
           % (got["isFor"][-3:], got["topics"], got["tier"], got["subjHidden"]))

    # …and the same for a response that lands after the sheet has CLOSED.
    p.eval("window.MRBSetWork.close()")
    p.eval("window.MRBSetWork.open({classId: %s})" % json.dumps(FX.C_KS4_SEPS))
    time.sleep(0.15)
    p.eval("window.MRBSetWork.close()")
    time.sleep(2.5)
    record(p.eval("(function(){var o=document.querySelector("
                  "'[data-sw=\"overlay\"]');return !!(o && o.hidden);})()"),
           "…and an answer arriving after Close does not reopen the sheet "
           "behind the teacher")

    p.eval("""(function(){ if (window.__mrbHeld && window.__mrbRealFetch) {
        window.fetch = window.__mrbRealFetch; } return true;})()""")


# ── the Detail step: chips, formulae, dates, the hold line, the toast ───
def goto_detail(p, class_id, tier, kind, ref):
    """Open the sheet and walk it to Detail on a named node, by pressing."""
    open_sheet(p, class_id)
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")   # Classes → Topic
    time.sleep(0.3)
    p.eval("""(function(){var cs=document.querySelectorAll(
        '[data-sw="tier-chips"] .sw-chip');
        for(var i=0;i<cs.length;i++){
          if(cs[i].textContent.toLowerCase()===%s){cs[i].click();return true;}}
        return false;})()""" % json.dumps(tier.lower()))
    time.sleep(0.3)
    if kind == "subtopic":
        # Its parent's chevron has to be open before the row is clickable.
        p.eval("""(function(){var cs=document.querySelectorAll('[data-sw="chevron"]');
            for(var i=0;i<cs.length;i++){if(cs[i].getAttribute('aria-expanded')
              ==='false'){cs[i].click();}} return true;})()""")
        time.sleep(0.4)
    hit = p.eval("""(function(){var rs=document.querySelectorAll('[data-sw=%s]');
        for(var i=0;i<rs.length;i++){
          if(rs[i].getAttribute('data-sw-ref')===%s){rs[i].click();return true;}}
        return false;})()""" % (json.dumps(kind), json.dumps(ref)))
    if not hit:
        return False
    time.sleep(0.3)
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")   # Topic → Detail
    return wait_for(p, "document.querySelectorAll('[data-sw=\"question\"]')"
                       ".length > 0")


def chip_state(p, rail):
    return p.eval("""(function(){var out=[];var cs=document.querySelectorAll(
        '[data-sw=%s] .sw-chip');
        for(var i=0;i<cs.length;i++){out.push({t:cs[i].textContent,
          on:cs[i].classList.contains('is-on'), off:!!cs[i].disabled});}
        return out;})()""" % json.dumps(rail))


def find_node_with(scope, lo, hi, tier):
    """A node whose pool at `tier` sits in [lo, hi] — for the chip cap."""
    for t in scope.get("tree") or []:
        for c in t.get("children") or []:
            n = (c.get("counts") or {}).get(tier, 0)
            if lo <= n <= hi:
                return ("subtopic", c["id"], n, t["id"])
        n = (t.get("counts") or {}).get(tier, 0)
        if lo <= n <= hi:
            return ("topic", t["id"], n, t["id"])
    return None


def check_detail(p, scopes, shots):
    print("\n   the Detail step")

    # ── A4 · chips_cap_at_availability ────────────────────────────────
    #
    # ⚠️ TWO SCOPES, BECAUSE THE RULE HAS TWO HALVES. A scope of 5–9 proves the
    # DEFAULT DROPS (10 is above the ceiling, so the sheet lands on 5); a scope
    # of 10–14 proves the CAP without the drop (10 is still reachable, 15 and
    # 20 are not). One scope can only ever show one of them, and a check that
    # showed only the cap would pass on a sheet that never re-defaulted.
    # ⚠️ THE CLASS AND THE TIER TRAVEL WITH THE NODE. An earlier version
    # searched three (tree, tier) pairs with `or`, then tried to work out
    # afterwards which one had answered by comparing the result with a FRESH
    # call to the same function — and `find_node_with` builds a new tuple every
    # time, so the identity test was always false and every node was driven at
    # the combined class. It only showed once the content lanes topped up KS3
    # and the first branch started answering: the drive then tried to reach the
    # KS3 lesson `life-processes` in a KS4 tree. Which class a node belongs to
    # is not something to re-derive; it is something to carry.
    CANDIDATES = ((FX.C_KS3_A, "ks3", "easy"),
                  (FX.C_KS4_COMB, "comb", "higher"),
                  (FX.C_KS4_COMB, "comb", "foundation"))
    small = mid = None
    for cid, key, tier in CANDIDATES:
        if small is None:
            hit = find_node_with(scopes[key], 5, 9, tier)
            if hit:
                small = (cid, tier) + hit
        if mid is None:
            hit = find_node_with(scopes[key], 10, 14, tier)
            if hit:
                mid = (cid, tier) + hit

    if small:
        cid, tier, kind, ref, n, _t = small
        if goto_detail(p, cid, tier, kind, ref):
            chips = chip_state(p, "count-chips")
            by = {c["t"]: c for c in chips}
            rows = p.eval("document.querySelectorAll('[data-sw=\"question\"]').length")
            record(by.get("5", {}).get("off") is False
                   and all(by.get(k, {}).get("off") is True for k in ("10", "15", "20"))
                   and by.get("5", {}).get("on") is True,
                   "chips_cap_at_availability — a scope holding %d disables "
                   "10 / 15 / 20 and the default DROPS from 10 to 5" % n,
                   "%s · %d row(s) rendered" % (chips, rows))
            record(rows == 5,
                   "…and the sheet actually renders the dropped count",
                   "%d question row(s)" % rows)
        else:
            record(False, "reach the small scope %s in the sheet" % ref)
    else:
        record(False, "a scope of 5–9 questions exists to cap against")

    if mid:
        mcid, mtier, kind, ref, n, _t = mid
        if goto_detail(p, mcid, mtier, kind, ref):
            by = {c["t"]: c for c in chip_state(p, "count-chips")}
            record(by.get("5", {}).get("off") is False
                   and by.get("10", {}).get("off") is False
                   and by.get("15", {}).get("off") is True
                   and by.get("20", {}).get("off") is True
                   and by.get("10", {}).get("on") is True,
                   "chips_cap_at_availability — a scope holding %d keeps 10 "
                   "live and disables 15 and 20, so the cap is a ceiling and "
                   "not a blanket" % n, json.dumps(by)[:220])
        else:
            record(False, "reach the mid scope %s" % ref)
    else:
        record(False, "a scope of 10–14 questions exists")

    # ── 20 is reachable where the pool allows it ──────────────────────
    big = None
    for t in scopes["comb"].get("tree") or []:
        if (t.get("counts") or {}).get("foundation", 0) >= 20:
            big = t["id"]
            break
    if big and goto_detail(p, FX.C_KS4_COMB, "foundation", "topic", big):
        by = {c["t"]: c for c in chip_state(p, "count-chips")}
        record(all(by.get(k, {}).get("off") is False for k in ("5", "10", "15", "20")),
               "…and on a topic with twenty or more, every chip is live — "
               "twenty is the ceiling, not a chip that is always dead",
               json.dumps(by)[:200])
        p.eval("""(function(){var cs=document.querySelectorAll(
            '[data-sw="count-chips"] .sw-chip');
            for(var i=0;i<cs.length;i++){if(cs[i].textContent==='20'){
              cs[i].click();return true;}} return false;})()""")
        wait_for(p, "document.querySelectorAll('[data-sw=\"question\"]')"
                    ".length === 20")
        record(p.eval("document.querySelectorAll('[data-sw=\"question\"]').length")
               == 20, "…and pressing 20 renders twenty rows")
        check_sideways(p, "Detail with twenty questions", shots)

    # ── A1 · the COUNT CHIP is a selection too, and it rebuilds the list ──
    #
    # ⚠️ THE HARDEST OF THE FIVE, AND THE ONE MOST LIKELY TO JUMP. A count chip
    # is the only control that calls `/preview` and then `buildQuestions()`,
    # which empties `els.qlist` and builds it again — the exact shape of the
    # v1 defect, one container down. It is legitimate there: the LIST is new
    # data. What must not move is the SHEET's scroller, which is a different
    # node and is not rebuilt.
    if big and goto_detail(p, FX.C_KS4_COMB, "foundation", "topic", big):
        p.eval("""(function(){var cs=document.querySelectorAll(
            '[data-sw="count-chips"] .sw-chip');
            for(var i=0;i<cs.length;i++){if(cs[i].textContent==='20'){
              cs[i].click();}} return true;})()""")
        wait_for(p, "document.querySelectorAll('[data-sw=\"question\"]')"
                    ".length === 20")
        g = p.eval(SCROLL_JS)
        if g and g["h"] > g["c"] + 40:
            p.eval("document.querySelector('[data-sw=\"sheet\"]').scrollTop"
                   " = %d" % int((g["h"] - g["c"]) * 0.5))
            time.sleep(0.3)
            before = p.eval(SCROLL_JS)["top"]
            p.eval("""(function(){var cs=document.querySelectorAll(
                '[data-sw="count-chips"] .sw-chip');
                for(var i=0;i<cs.length;i++){if(cs[i].textContent==='15'){
                  cs[i].click();}} return true;})()""")
            wait_for(p, "document.querySelectorAll('[data-sw=\"question\"]')"
                        ".length === 15")
            time.sleep(0.4)
            after = p.eval(SCROLL_JS)
            new_max = max(0, after["h"] - after["c"])
            record(after["top"] == min(before, new_max),
                   "scroll_unchanged_on_select — a COUNT chip rebuilds the "
                   "question list and does NOT move the sheet's scroller",
                   "%d → %d (new maximum %d), 20 rows became %s"
                   % (before, after["top"], new_max,
                      p.eval("document.querySelectorAll("
                             "'[data-sw=\"question\"]').length")))
        else:
            record(False, "the Detail list is long enough to scroll",
                   "scrollHeight %s" % (g and g["h"]))

    # ── MRB-302 · a formula row renders a real subscript ──────────────
    #
    # STORE FLAT, RENDER SUBSCRIPT. `conservation-of-mass` holds twelve
    # foundation rows, six of which carry CO2 / H2O / O2, so a set of twelve
    # contains all six — the check cannot fail for want of a formula in the
    # draw. ⚠️ The stored string is never touched: what goes to the route is
    # the question ID, and every answer comparison in the estate runs on
    # option indices, so a display-time pass cannot reach marking.
    if goto_detail(p, FX.C_KS4_COMB, "foundation", "subtopic",
                   "conservation-of-mass"):
        p.eval("""(function(){var ss=document.querySelectorAll('[data-sw="stem"]');
            for(var i=0;i<ss.length;i++){ss[i].click();} return true;})()""")
        time.sleep(0.5)
        got = p.eval(r"""(function(){
          var rows = document.querySelectorAll('[data-sw="question"]');
          var withFormula = 0, withSub = 0, flat = [];
          for (var i = 0; i < rows.length; i++) {
            var t = rows[i].textContent || '';
            if (/\b(CO2|H2O|O2|CH4|N2|H2)\b/.test(t.replace(/₂|₃|₄/g,
                function (c) { return {'₂':'2','₃':'3','₄':'4'}[c]; }))) {
              withFormula++;
              if (rows[i].querySelector('sub')) { withSub++; }
              else { flat.push(t.slice(0, 60)); }
            }
          }
          return {rows: rows.length, withFormula: withFormula,
                  withSub: withSub, flat: flat.slice(0, 3),
                  subs: document.querySelectorAll(
                    '[data-sw="overlay"] sub').length};})()""")
        record(got["withFormula"] > 0 and got["withSub"] == got["withFormula"],
               "an expanded row renders a real <sub> for every formula it "
               "shows — CO2 displays as CO₂ (MRB-302)",
               "%d of %d rows carry a formula; %d <sub> element(s) in the sheet"
               % (got["withFormula"], got["rows"], got["subs"])
               if got["withSub"] == got["withFormula"]
               else "flat: %s" % got["flat"])
        record(got["subs"] >= got["withFormula"],
               "…and the subscripts are in the options as well as the stems",
               "%d <sub> across %d formula row(s)" % (got["subs"],
                                                      got["withFormula"]))
        if shots:
            p.screenshot(os.path.join(shots, "MRB302-subscripts-390.png"),
                         width=390)
    else:
        record(False, "reach conservation-of-mass in the sheet")


# ── B1/B8 · the dates, across the BST boundary ─────────────────────────
#
# The teacher types a WALL CLOCK — "Sunday the 25th at 01:30" — and the server
# stores an INSTANT. Between those two is the hour that happens twice on
# 25 Oct 2026. `Intl.DateTimeFormat` with `timeZone:'Europe/London'` is the only
# authority available on a page with no build step, and the server must NOT use
# `toLocaleString` at all — Render runs a small-ICU Node where a `timeZone`
# option is silently ignored (RISKS B2).
BST_CASES = [
    # (date, time, expected UTC ISO, why)
    ("2026-10-24", "23:30", "2026-10-24T22:30:00.000Z", "the night before, in BST"),
    ("2026-10-25", "00:30", "2026-10-24T23:30:00.000Z", "still BST, +1"),
    ("2026-10-25", "01:30", "2026-10-25T00:30:00.000Z",
     "AMBIGUOUS — 01:30 happens twice; the EARLIER instant wins, so work "
     "opens at the first moment the clock reads what was typed"),
    ("2026-10-25", "02:30", "2026-10-25T02:30:00.000Z", "GMT now, +0"),
    ("2026-10-26", "07:00", "2026-10-26T07:00:00.000Z", "the Monday, GMT"),
    ("2027-03-28", "01:30", "2027-03-28T01:30:00.000Z",
     "NONEXISTENT — 01:30 never happens; shifted forward to 02:30 BST"),
]


def check_dates(p, t_teacher, scopes, shots):
    print("\n   dates, and the hour that happens twice")

    wrong = []
    for d, t, want, why in BST_CASES:
        got = p.eval("window.MRBSetWork.londonToUtcIso(%s, %s)"
                     % (json.dumps(d), json.dumps(t)))
        if got != want:
            wrong.append("%s %s → %s, wanted %s (%s)" % (d, t, got, want, why))
    record(not wrong,
           "bst_boundary_roundtrip (client) — six London wall clocks across "
           "both 2026 transitions convert to the right instant",
           "; ".join("%s %s → %s" % (d, t, w) for d, t, w, _y in BST_CASES)
           if not wrong else "; ".join(wrong))

    back = []
    for d, t, want, _why in BST_CASES:
        r = p.eval("window.MRBSetWork.utcToLondonParts(%s)" % json.dumps(want))
        if not r or r["date"] != d or r["time"] != t:
            # The ambiguous and nonexistent cases do not round-trip to the
            # same wall clock, and must not be asserted to.
            if (d, t) not in (("2027-03-28", "01:30"),):
                back.append("%s → %s" % (want, r))
    record(not back,
           "…and the instant reads back as the wall clock the teacher typed",
           "every ordinary case round-trips" if not back else "; ".join(back))

    # ── the same instants, THROUGH THE ROUTE, into a timestamptz ──────
    #
    # ⚠️ THE CLIENT CONVERTING CORRECTLY IS HALF THE CLAIM. What is stored is a
    # `timestamptz`, and what a teacher later reads is the server's London
    # formatting of it. Both ends, one instant.
    got = pick_topic(scopes["comb"], 1, "foundation")
    if not got:
        return
    _n, topic, _s = got
    st, prev = preview(t_teacher, FX.C_KS4_COMB, "foundation", "topic",
                       topic["id"], 3)
    ids = [q["id"] for q in (prev.get("picked") or [])]
    for d, t, want, why in BST_CASES[1:3]:
        rel = p.eval("window.MRBSetWork.londonToUtcIso(%s, %s)"
                     % (json.dumps(d), json.dumps(t)))
        due = p.eval("window.MRBSetWork.londonToUtcIso('2026-10-26','07:00')")
        st, out = post_set(t_teacher, class_ids=[FX.C_KS4_COMB],
                           tier="foundation", scope_ref=topic["id"],
                           question_ids=ids, release_at=rel, due_at=due,
                           title=TITLE + " · bst " + t)
        if st != 200:
            record(False, "bst_boundary_roundtrip (server) — release %s %s "
                          "is accepted" % (d, t),
                   "status %s %s" % (st, json.dumps(out)[:160]))
            continue
        aid = out["assignment_ids"][0]
        st, row = rest("GET", "/rest/v1/assignments?id=eq.%s&select=release_at,"
                              "due_at" % aid, t_teacher)
        stored = (row[0] if isinstance(row, list) and row else {})
        rel_ms = p.eval("Date.parse(%s)" % json.dumps(stored.get("release_at") or ""))
        want_ms = p.eval("Date.parse(%s)" % json.dumps(rel))
        shown = p.eval("window.MRBSetWork.utcToLondonParts(%s)"
                       % json.dumps(stored.get("release_at") or ""))
        record(rel_ms == want_ms and shown and shown["date"] == d
               and shown["time"] == t,
               "bst_boundary_roundtrip (server) — %s %s survives the round "
               "trip: %s" % (d, t, why),
               "sent %s · stored %s · reads back %s %s"
               % (rel, stored.get("release_at"),
                  (shown or {}).get("date"), (shown or {}).get("time")))

    # ── B8 · defaults_london ──────────────────────────────────────────
    if goto_detail(p, FX.C_KS4_COMB, "foundation", "topic", topic["id"]):
        vals = p.eval("""(function(){var q=function(s){var n=
            document.querySelector('[data-sw="'+s+'"]');return n?n.value:null;};
            return {rd:q('release-date'), rt:q('release-time'),
                    dd:q('due-date'), dt:q('due-time'),
                    relFields: !!document.querySelector(
                      '[data-sw="release-fields"]').hidden,
                    on: (document.querySelector(
                      '[data-sw="release-chips"] .is-on')||{}).textContent};})()""")
        want_due = p.eval("""(function(){
            var f=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/London',
              year:'numeric',month:'2-digit',day:'2-digit'});
            var p=f.formatToParts(new Date());var o={};
            p.forEach(function(x){o[x.type]=x.value;});
            var d=new Date(Date.UTC(+o.year,+o.month-1,+o.day)+7*86400000);
            return d.toISOString().slice(0,10);})()""")
        record(vals["dt"] == "18:00" and vals["dd"] == want_due
               and vals["rt"] == "07:00" and vals["on"] == "Now"
               and vals["relFields"] is True,
               "defaults_london — Due defaults to +7 days at 18:00 London, "
               "Release defaults to Now with its fields hidden and 07:00 ready",
               json.dumps(vals))
        record(p.eval("""(function(){var n=document.querySelector(
            '[data-sw="title"]');return {v:n.value, max:n.maxLength};})()""")
               ["max"] == 80,
               "title_bounds (rendered) — the field cannot hold 81 characters",
               "maxlength %s"
               % p.eval("document.querySelector('[data-sw=\"title\"]').maxLength"))


# ── A9 · faff_sweep ────────────────────────────────────────────────────
def check_faff(p, scopes):
    print("\n   the words the sheet is allowed to say")

    # ⚠️ THE TABLE FIRST, THEN THE RENDER. `SAY` is the complete set the module
    # can emit; sweeping only the DOM would miss a string added but not yet
    # reached by this drive's path, which is exactly the string that ships.
    say = p.eval("JSON.parse(JSON.stringify(Object.keys("
                 "window.MRBSetWork.SAY)))")
    flat = p.eval("""(function(){var S=window.MRBSetWork.SAY, out=[];
        var walk=function(v){ if(typeof v==='string'){out.push(v);}
          else if(Array.isArray(v)){v.forEach(walk);}
          else if(v && typeof v==='object'){Object.keys(v).forEach(function(k){
            walk(v[k]);});}};
        Object.keys(S).forEach(function(k){ if(typeof S[k]!=='function'){
          walk(S[k]);}});
        return out;})()""")
    extra = sorted(set(flat) - FAFF_EXACT - FAFF_ARIA - {"student", "students"})
    record(not extra,
           "faff_sweep (the table) — every literal string in SAY is on RISKS "
           "A9's list, or is one of the four accessible names",
           "%d string(s), all allowed" % len(flat)
           if not extra else "NOT ON THE LIST: %s" % extra)

    # The four aria-labels are exempt from the VISIBLE list because they are
    # not visible. Both halves of that sentence are checked.
    labelled = p.eval("""(function(){var out=[];var ns=document.querySelectorAll(
        '[data-sw="overlay"] input[aria-label]');
        for(var i=0;i<ns.length;i++){out.push(ns[i].getAttribute('aria-label'));}
        return out;})()""")
    body_text = p.eval("(document.querySelector('[data-sw=\"overlay\"]')"
                       "||{}).innerText || ''")
    leaked = sorted(a for a in FAFF_ARIA if a in body_text)
    # ⚠️ NOT AN EQUALITY. `Title` is an aria-label too, and it is also the
    # VISIBLE label above that field — so it is legitimately in both sets, and
    # demanding `labelled == FAFF_ARIA` failed on a string that was already
    # allowed. Three separate claims instead: every accessible name is allowed
    # somewhere; the four that are allowed ONLY as accessible names are all
    # actually carried by an input, so the exemption is paying for itself; and
    # none of those four is ever drawn.
    stray = sorted(set(labelled) - FAFF_EXACT - FAFF_ARIA)
    record(not stray and FAFF_ARIA <= set(labelled) and not leaked,
           "faff_sweep — every accessible name is on one of the two lists, "
           "the four exempt ones are all really carried by an input, and none "
           "of them is ever drawn on the screen",
           "aria-labels: %s; none in the visible text" % sorted(labelled)
           if not (stray or leaked)
           else "unlisted: %s · visible: %s" % (stray, leaked))
    # And the composed ones, evaluated rather than read.
    #
    # ⊕ MRB-336, 8 Sep 2026 — `S.hold('14 Sep 2026')` WAS THE FIFTH AND THIS
    # CALL CRASHED THE DRIVE. `SAY.hold` went with the hold line, and its
    # `FAFF_PATTERNS` entry went with it — but the call stayed, so the sweep
    # died on `TypeError: S.hold is not a function` and took every check after
    # it down. That is worth a line rather than a silent edit: a gate that
    # THROWS is not a gate that fails, it is a gate that stops, and the eleven
    # sections behind this one reported nothing at all.
    #
    # ⚠️ SO THE ABSENCE IS ASSERTED RATHER THAN JUST NOT CALLED. `SAY` is the
    # complete set of strings this module can emit; a `hold` key coming back
    # would mean the sentence had returned, and deleting the call without
    # saying so would leave nothing watching for that.
    record(p.eval("typeof window.MRBSetWork.SAY.hold") == "undefined",
           "⊕ MRB-336: hold_string_is_gone — `SAY` has no `hold` at all, so "
           "the sheet cannot compose a sentence about a school hold that no "
           "longer governs anything a teacher does",
           "typeof SAY.hold is %r"
           % p.eval("typeof window.MRBSetWork.SAY.hold"))
    composed = p.eval("""(function(){var S=window.MRBSetWork.SAY;
        return [S.weeksAgo(1), S.weeksAgo(3), S.pupils(1), S.pupils(24)];})()""")
    bad = [c for c in composed
           if c not in FAFF_EXACT
           and not any(r.match(c) for r in FAFF_PATTERNS)]
    record(not bad,
           "faff_sweep — the four composed strings are each a label plus a "
           "number", "; ".join(composed) if not bad else str(bad))

    # ⚠️ AND THE THREE v1 SENTENCES MUST BE GONE BY NAME. A general "no long
    # strings" rule would pass a NEW sentence; naming the ones that were there
    # is what makes the check about this ticket.
    # ⚠️ TESTED AGAINST `SAY`, NOT AGAINST THE SOURCE, and both earlier
    # attempts are why. Grepping the whole FILE matched `"Only "` inside a
    # comment. Extracting string literals with a regex matched most of the
    # file, because a hand-rolled JS literal parser treats the apostrophe in
    # "the teacher's" as an opening quote and swallows everything after it.
    #
    # `SAY` is the complete set of strings this module can emit — the file
    # says so and `faff_sweep (the table)` above has just proved every one of
    # them is on the allowed list — so it is the right thing to search, it is
    # read out of the running page rather than parsed, and prose cannot reach
    # it. `flat` is that list.
    # ⚠️ NOT the bare word `available`: it is a substring of `Unavailable`,
    # which IS allowed and IS in SAY, so the phrase list was reporting the
    # permitted string as the forbidden one. v1's sentence was "Only N
    # available" and `Only ` catches it on its own.
    V1_FAFF = ("can't be opened", "Only ", "Step 1 of", "You need to",
               "Sorry", "Please ")
    v1 = sorted({f for f in V1_FAFF
                 for lit in flat if f.lower() in lit.lower()})
    record(not v1,
           "faff_sweep — none of v1's sentences survives as a string the "
           "sheet can SAY (the prose is free to discuss them)",
           "%d emittable string(s), none of the seven phrases" % len(flat)
           if not v1 else "still sayable: %s" % v1)

    # The two that cannot appear in honest prose either, so the source is
    # still worth one look for them.
    src = open("shared/set-work.js", encoding="utf-8").read()
    gone = [f for f in ("This work can't be opened until", "Step 1 of 3")
            if f in src]
    record(not gone,
           "…and v1's two named sentences are nowhere in the file at all",
           "neither of them" if not gone else "present: %s" % gone)

    # ── the render sweep, on all three steps ──────────────────────────
    seen, unknown = set(), []
    open_sheet(p, FX.C_KS4_COMB)
    for step in range(3):
        raw = json.loads(p.eval(READ_CHROME_JS))
        if isinstance(raw, dict):
            record(False, "the sheet is open for the faff sweep", str(raw))
            return
        for s in raw:
            seen.add(s)
            if s in FAFF_EXACT or any(r.match(s) for r in FAFF_PATTERNS):
                continue
            unknown.append(s)
        if step == 0:
            p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
            time.sleep(0.3)
            p.eval("""(function(){var rs=document.querySelectorAll(
                '[data-sw="topic"]');
                for(var i=0;i<rs.length;i++){
                  if(rs[i].getAttribute('aria-disabled')!=='true'){
                    rs[i].click();return true;}} return false;})()""")
            time.sleep(0.3)
        elif step == 1:
            p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
            wait_for(p, "document.querySelectorAll('[data-sw=\"question\"]')"
                        ".length > 0")
    record(not unknown,
           "faff_sweep (rendered) — every label, chip, button, tag and status "
           "line across all three steps is on the list",
           "%d distinct chrome string(s), all allowed" % len(seen)
           if not unknown else "NOT ON THE LIST: %s" % sorted(set(unknown))[:10])


# ── A10 · toast_after_set, and A6's dead Swap in the DOM ───────────────
def check_toast_and_swap(p, scopes, shots):
    print("\n   the toast, and the Swap that runs out")

    # A small KS3 lesson: small enough that Swap can be drained inside a drive.
    small = find_node_with(scopes["ks3"], 4, 8, "easy")
    if small and goto_detail(p, FX.C_KS3_A, "easy", small[0], small[1]):
        n = small[2]
        rows = p.eval("document.querySelectorAll('[data-sw=\"question\"]').length")
        pressed = 0
        for _ in range(n + 3):
            alive = p.eval("""(function(){var b=document.querySelector(
                '[data-sw="swap"]:not([disabled])'); if(!b){return false;}
                b.click(); return true;})()""")
            if not alive:
                break
            pressed += 1
            time.sleep(0.9)
        dead = p.eval("document.querySelectorAll('[data-sw=\"swap\"][disabled]')"
                      ".length")
        total = p.eval("document.querySelectorAll('[data-sw=\"swap\"]').length")
        record(pressed > 0 and dead > 0,
               "swap_exhausts_disables (rendered) — a scope holding %d runs "
               "out after %d swap(s) and the row's Swap goes DEAD rather than "
               "offering a control that does nothing" % (n, pressed),
               "%d of %d Swap buttons disabled, %d row(s)" % (dead, total, rows))
        if shots:
            p.screenshot(os.path.join(shots, "A6-swap-exhausted-390.png"),
                         width=390)

    # ── the toast, on a real set ──────────────────────────────────────
    got = pick_topic(scopes["ks3"], 2, "medium")
    if not got:
        return
    _n, unit, _s = got
    if not goto_detail(p, FX.C_KS3_A, "medium", "topic", unit["id"]):
        record(False, "reach Detail for the toast check")
        return
    title = TITLE + " · from the sheet"
    p.eval("""(function(){var t=document.querySelector('[data-sw="title"]');
        t.value=%s; t.dispatchEvent(new Event('input',{bubbles:true}));
        return t.value;})()""" % json.dumps(title))
    time.sleep(0.3)
    record(p.eval("!document.querySelector('[data-sw=\"primary\"]').disabled"),
           "the primary is live once the sheet is valid",
           "label %r" % p.eval("document.querySelector("
                               "'[data-sw=\"primary\"]').textContent"))
    record(p.eval("document.querySelector('[data-sw=\"primary\"]').textContent")
           == "Set work",
           "…and it says 'Set work' on the last step, 'Next' before it")

    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    ok = wait_for(p, "(function(){var t=document.querySelector("
                     "'[data-sw=\"toast\"]');return t && !t.hidden;})()")
    toast = p.eval("(document.querySelector('[data-sw=\"toast\"]')||{})"
                   ".textContent")
    record(ok and toast == title + " · 8a/Sc1",
           "toast_after_set — one class: '<title> · <class>'", repr(toast))
    record(p.eval("(function(){var o=document.querySelector("
                  "'[data-sw=\"overlay\"]');return !!(o && o.hidden);})()"),
           "…and the sheet closes behind it")
    if shots:
        p.screenshot(os.path.join(shots, "A10-toast-390.png"), width=390)

    # Two classes: the plural form, and the count rather than the names.
    open_sheet(p, FX.C_KS3_A)
    p.eval("""(function(){var rs=document.querySelectorAll('[data-sw="class"]');
        for(var i=0;i<rs.length;i++){ if(rs[i].getAttribute('aria-pressed')
          ==='false'){rs[i].click(); return true;}} return false;})()""")
    time.sleep(0.3)
    n_on = p.eval("document.querySelectorAll('[data-sw=\"class\"][aria-pressed"
                  "=\"true\"]').length")
    if n_on >= 2:
        p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
        time.sleep(0.3)
        p.eval("""(function(){var rs=document.querySelectorAll('[data-sw="topic"]');
            for(var i=0;i<rs.length;i++){
              if(rs[i].getAttribute('aria-disabled')!=='true'){
                rs[i].click();return true;}} return false;})()""")
        time.sleep(0.3)
        p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
        wait_for(p, "document.querySelectorAll('[data-sw=\"question\"]')"
                    ".length > 0")
        t2 = TITLE + " · two from the sheet"
        p.eval("""(function(){var t=document.querySelector('[data-sw="title"]');
            t.value=%s; t.dispatchEvent(new Event('input',{bubbles:true}));})()"""
               % json.dumps(t2))
        time.sleep(0.3)
        # ⚠️ HIDE THE PREVIOUS TOAST FIRST, AND WAIT FOR THE NEW TEXT RATHER
        # THAN FOR VISIBILITY. The toast lives 3.2 seconds and the single-class
        # set was well inside that, so `wait_for(not hidden)` returned
        # instantly on the OLD toast and this check read the OLD string. It
        # went red reporting the one-class wording — a drive artefact wearing
        # the clothes of a product defect, which is the expensive kind.
        p.eval("""(function(){var t=document.querySelector('[data-sw="toast"]');
            t.hidden = true; t.textContent = ''; return true;})()""")
        p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
        wait_for(p, "(function(){var t=document.querySelector("
                    "'[data-sw=\"toast\"]');return t && !t.hidden "
                    "&& t.textContent.indexOf('Set for') > -1;})()")
        toast2 = p.eval("(document.querySelector('[data-sw=\"toast\"]')||{})"
                        ".textContent")
        record(toast2 == "%s · Set for %d classes" % (t2, n_on),
               "toast_after_set — several classes: '<title> · Set for N "
               "classes'", repr(toast2))

    # ── ⊕ MRB-336 · THE HELD SCHOOL'S SHEET SAYS NOTHING ──────────────
    #
    # v1 said "This work can't be opened until…"; MRB-335 cut that to one
    # factual date. MRB-336 cuts the date too, because the fact stopped being
    # true: the hold governs AUTOMATIC composition and no longer touches work
    # a teacher sets, so `release_at` is stored exactly as asked.
    #
    # ⚠️ THE ASSERTION IS ON THE NODE, NOT ON THE TEXT. A hidden node still
    # carrying "Assignments open 14 Sep 2026" would pass a text check and
    # would be one CSS change away from being visible again.
    open_sheet(p, FX.C_KS3_HELD)
    time.sleep(0.5)
    st_scope = p.eval("document.querySelectorAll('[data-sw=\"topic\"]').length")
    if st_scope:
        p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
        time.sleep(0.3)
        p.eval("""(function(){var rs=document.querySelectorAll('[data-sw="topic"]');
            for(var i=0;i<rs.length;i++){
              if(rs[i].getAttribute('aria-disabled')!=='true'){
                rs[i].click();return true;}} return false;})()""")
        time.sleep(0.3)
        p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
        wait_for(p, "document.querySelectorAll('[data-sw=\"question\"]')"
                    ".length > 0")
        held = p.eval("""(function(){
            var o = document.querySelector('[data-sw="overlay"]');
            return {node: !!document.querySelector('[data-sw="hold"]'),
                    cls: o.querySelectorAll('.sw-hold').length,
                    open: (o.textContent||'').indexOf('Assignments open')};})()""")
        record(held["node"] is False and held["cls"] == 0
               and held["open"] == -1,
               "hold_line_gone — the held school's sheet carries no hold node, "
               "no `.sw-hold`, and the words nowhere in the overlay",
               json.dumps(held))
        if shots:
            p.screenshot(os.path.join(shots, "B6-no-hold-line-390.png"),
                         width=390)


# ── C12/A5 rendered · the tier chip re-counts, and a zero refuses ──────
def check_tier_and_zero(p, scopes):
    print("\n   the tier chip, and a node with nothing at that tier")
    open_sheet(p, FX.C_KS4_COMB)
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    time.sleep(0.4)

    def counts():
        return p.eval("""(function(){var out={};var rs=document.querySelectorAll(
            '[data-sw="topic"]');
            for(var i=0;i<rs.length;i++){out[rs[i].getAttribute('data-sw-ref')]=
              rs[i].querySelector('.sw-count').textContent;} return out;})()""")

    found = counts()
    reqs_before = p.eval("performance.getEntriesByType('resource').filter("
                         "function(r){return r.name.indexOf('set-work/scope')"
                         ">-1;}).length")
    p.eval("""(function(){var cs=document.querySelectorAll(
        '[data-sw="tier-chips"] .sw-chip');
        for(var i=0;i<cs.length;i++){if(cs[i].textContent==='Higher'){
          cs[i].click();return true;}} return false;})()""")
    time.sleep(0.5)
    higher = counts()
    reqs_after = p.eval("performance.getEntriesByType('resource').filter("
                        "function(r){return r.name.indexOf('set-work/scope')"
                        ">-1;}).length")
    moved = [k for k in found if found[k] != higher.get(k)]
    record(bool(moved),
           "tier_change_recounts — the counts move when the tier chip moves",
           "%d of %d topic counts changed, e.g. %s"
           % (len(moved), len(found),
              ["%s %s→%s" % (k, found[k], higher[k]) for k in moved[:3]]))
    record(reqs_after == reqs_before,
           "…IN PLACE, with no second /scope request — a spinner between a "
           "teacher and a number they are comparing is the thing this avoids",
           "%d /scope request(s) before, %d after" % (reqs_before, reqs_after))

    # ── A5 · zero_count_not_selectable ────────────────────────────────
    #
    # A Higher-only subtopic renders `0` at Foundation and refuses to be
    # picked. It is NOT removed: the tree is filtered by pathway and never by
    # tier, because a tree that changed shape when the chip moved would be a
    # different tree and the teacher would lose their place in it.
    p.eval("""(function(){var cs=document.querySelectorAll(
        '[data-sw="tier-chips"] .sw-chip');
        for(var i=0;i<cs.length;i++){if(cs[i].textContent==='Foundation'){
          cs[i].click();}} return true;})()""")
    time.sleep(0.3)
    p.eval("""(function(){var cs=document.querySelectorAll('[data-sw="chevron"]');
        for(var i=0;i<cs.length;i++){if(cs[i].getAttribute('aria-expanded')
          ==='false'){cs[i].click();}} return true;})()""")
    time.sleep(0.6)
    zeros = p.eval("""(function(){var out=[];var rs=document.querySelectorAll(
        '[data-sw="subtopic"]');
        for(var i=0;i<rs.length;i++){
          if(rs[i].querySelector('.sw-count').textContent==='0'){
            out.push({ref:rs[i].getAttribute('data-sw-ref'),
                      dis:rs[i].getAttribute('aria-disabled')});}}
        return out;})()""")
    record(zeros and all(z["dis"] == "true" for z in zeros),
           "zero_count_not_selectable — every subtopic showing 0 at "
           "Foundation is rendered, visible, and aria-disabled",
           "%d zero row(s), all disabled, e.g. %s"
           % (len(zeros), [z["ref"] for z in zeros[:3]]) if zeros
           else "no zero rows found — the check measured nothing")
    if zeros:
        clicked = p.eval("""(function(){var rs=document.querySelectorAll(
            '[data-sw="subtopic"]');
            for(var i=0;i<rs.length;i++){
              if(rs[i].querySelector('.sw-count').textContent==='0'){
                rs[i].click();
                return rs[i].classList.contains('is-on');}} return null;})()""")
        time.sleep(0.3)
        record(clicked is False
               and p.eval("!!document.querySelector('[data-sw=\"primary\"]')"
                          ".disabled"),
               "…and clicking one selects nothing and leaves Next disabled",
               "row is-on after click: %s" % clicked)


# ── D1–D4 · every downstream consumer renders a v2 row ─────────────────
#
# ⚠️ NOT "the columns are non-null" — that is already asserted in check_write.
# This is the other half: the SCREENS. Every one of them was written when an
# assignment came from a scheme row, and every one reads `title`, `topic`,
# `academic_week` and `due_at`. A v2 row has `source_sow_entry_id = null` and a
# `topic` that is a display title rather than a slug, and the failure mode is
# not an error — it is the word `null` on a teacher's screen, or `Week null`.
CONSUMERS = [
    ("teacher class-detail", "/teacher/class-detail.html?class=%(ks3a)s"),
    ("teacher assignment",   "/teacher/assignment.html?class=%(ks3a)s"),
    ("teacher digest",       "/teacher/digest.html?class=%(ks3a)s"),
    ("teacher insights",     "/teacher/insights.html?class=%(ks3a)s"),
]
STUDENT_PAGES = [
    ("student class",      "/student/class.html?class=%(ks3a)s"),
    ("student assignment", "/student/assignment.html?class=%(ks3a)s"),
]

BAD_TEXT = re.compile(r"\bnull\b|\bundefined\b|\bNaN\b|Week null|\[object Object\]")


def check_consumers(p, base, pages, who, title, shots):
    print("\n   %s: every screen with a v2 assignment on it" % who)
    for label, path in pages:
        url = (base + path % {"ks3a": FX.C_KS3_A}) + "&env=test&api=" + PAGE_API
        p.set_viewport(390, 900)
        goto_ready(p, url, "document.body && document.body.innerText.length > 0",
                   settle=6.5, tries=2)
        got = p.eval("""(function(){
          var t = (document.body.innerText || '');
          return {text: t, len: t.length,
                  sw: document.documentElement.scrollWidth,
                  cw: document.documentElement.clientWidth};})()""")
        bad = BAD_TEXT.findall(got["text"] or "")
        drew = (got["len"] or 0) > 200
        record(drew and not bad,
               "consumers_render_null_sow — %s draws with a v2 assignment on "
               "it, and says no null" % label,
               "%d characters of visible text, no null/undefined"
               % got["len"] if drew and not bad
               else ("drew only %d characters" % got["len"] if not drew
                     else "SAYS: %s" % sorted(set(bad))))
        # ⚠️ ONE NAMED, PROVED PRE-EXISTING OVERFLOW, AND IT IS ASSERTED
        # RATHER THAN SKIPPED. `teacher/insights.html` overflows by 19px at
        # 390 — a 209px "Find a student" header control whose right edge sits
        # at 583. It is nothing to do with assignments, Set work or a v2 row.
        # MEASURED ON BOTH SIDES: the same page built from 7f03fc8ce, the
        # merge-base with origin/main, gives byte-identical numbers (docW 409,
        # cliW 390, the same 209px button at 583). So it is reported as a
        # finding on the teacher surface and not as an MRB-335 red — and it is
        # asserted at its known size, so the day it gets WORSE this goes red
        # instead of staying quietly excused.
        known = 409 if label == "teacher insights" else None
        if known:
            record(got["sw"] == known,
                   "…%s still overflows by exactly the %dpx it overflowed by "
                   "before MRB-335 — a pre-existing header control, proved on "
                   "the merge-base build, not a regression"
                   % (label, known - got["cw"]),
                   "scrollWidth %d (pre-MRB-335: %d), clientWidth %d"
                   % (got["sw"], known, got["cw"]))
        else:
            record(got["sw"] <= got["cw"] + 1,
                   "…and %s does not scroll sideways at 390px" % label,
                   "scrollWidth %d ≤ clientWidth %d" % (got["sw"], got["cw"]))
        if shots:
            p.screenshot(os.path.join(
                shots, "D3-%s-390.png" % label.replace(" ", "-")), width=390)
        # The title this drive set must actually be ON the page somewhere, or
        # "no nulls" is a claim about a screen that is not showing the row.
        if label in ("teacher class-detail", "student class"):
            record(title in (got["text"] or ""),
                   "…and %s actually shows the work this drive set" % label,
                   "looked for %r" % title)


# ════════════════════════════════════════════════════════════════════════
# 9 · CLEANUP, AND THE PROOF THAT IT HAPPENED
# ════════════════════════════════════════════════════════════════════════
#
# ⚠️ EVERY DELETE'S STATUS IS CHECKED AND THE WORLD IS RE-QUERIED. A teardown
# that reports success without looking is worse than one that crashes: the
# litter becomes somebody else's problem, discovered later, by someone who does
# not know what it is. `mrb331_fixture.teardown()` learned this the hard way and
# the same discipline applies to the rows a drive CAUSES rather than seeds.
def cleanup(teacher_id, admin_id):
    print("\n9 · clearing up after the drive")
    ids = ",".join(c[0] for c in FX.CLASSES)

    st, before = FX.api("GET", "/rest/v1/assignments?class_id=in.(%s)"
                               "&select=id,title" % ids)
    n_before = len(before) if isinstance(before, list) else 0
    n_aq = 0
    if isinstance(before, list) and before:
        aids = ",".join(a["id"] for a in before)
        st, qs = FX.api("GET", "/rest/v1/assignment_questions"
                               "?assignment_id=in.(%s)&select=id" % aids)
        n_aq = len(qs) if isinstance(qs, list) else 0

    n_aud = 0
    for uid in (teacher_id, admin_id):
        if not uid:
            continue
        st, rows = FX.api("GET", "/rest/v1/audit_log?actor_id=eq.%s&select=id"
                          % uid)
        n_aud += len(rows) if isinstance(rows, list) else 0

    gone = FX.clear_work()
    for uid in (teacher_id, admin_id):
        if uid:
            FX.api("DELETE", "/rest/v1/audit_log?actor_id=eq." + uid)

    # ── the proof ─────────────────────────────────────────────────────
    st, left_a = FX.api("GET", "/rest/v1/assignments?class_id=in.(%s)"
                               "&select=id" % ids)
    left_aud = 0
    for uid in (teacher_id, admin_id):
        if uid:
            st, rows = FX.api("GET", "/rest/v1/audit_log?actor_id=eq.%s"
                                     "&select=id" % uid)
            left_aud += len(rows) if isinstance(rows, list) else 0
    n_left = len(left_a) if isinstance(left_a, list) else -1
    record(n_left == 0 and left_aud == 0,
           "every row this drive wrote is gone, and the world was re-queried "
           "to say so rather than assumed",
           "removed %d assignment(s) (%d question rows) and %d audit row(s); "
           "%d assignment(s) and %d audit row(s) remain"
           % (gone, n_aq, n_aud, n_left, left_aud))
    print("        this drive created %d assignment(s) by id" % len(set(made_assignments)))
    return n_left == 0


# ════════════════════════════════════════════════════════════════════════
def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("backend", nargs="?", default=None)
    ap.add_argument("--keep", action="store_true",
                    help="leave the throwaway world and this run's rows standing")
    ap.add_argument("--api-only", action="store_true",
                    help="skip the browser half (no Chrome)")
    ap.add_argument("--shots", default="docs/mrb335/shots",
                    help="where the 390px screenshots go")
    args = ap.parse_args()

    pw = os.environ.get(FX.ENV_SWITCH, "")
    if not pw:
        print("Set %s. This drive signs throwaway accounts in for real."
              % FX.ENV_SWITCH)
        return 2
    if args.shots:
        os.makedirs(args.shots, exist_ok=True)

    print("\n🧾  MRB-335 — a teacher picks a topic, and the right child gets "
          "the right questions\n")
    FX.seed()
    gone = FX.clear_work()
    if gone:
        print("  cleared %d assignment(s) from a previous run" % gone)

    t_teacher = sign_in(FX.TEACHER_EMAIL, pw)["access_token"]
    t_admin = sign_in(FX.ADMIN_EMAIL, pw)["access_token"]
    sess_teacher = sign_in(FX.TEACHER_EMAIL, pw)
    sess_pupil = sign_in(FX.PUPIL_EMAIL, pw)
    t_pupil = sess_pupil["access_token"]
    t_pupil_b = sign_in(FX.PUPIL_B_EMAIL, pw)["access_token"]
    teacher_id = FX.find_user(FX.TEACHER_EMAIL)
    admin_id = FX.find_user(FX.ADMIN_EMAIL)

    server = None
    site = None
    twenty_title = None
    deleted_title = None          # ⊕ MRB-336, set by check_delete_surfaces
    try:
        site, site_port = cdp.serve("mrbadmus_site", port=SITE_PORT)
        base = "http://localhost:%d" % site_port
        print("   site on %s" % base)
        server = Server(extra_origin=base)
        server.__enter__()

        scopes = check_scope(t_teacher)
        if not scopes:
            return 1
        check_preview(t_teacher, scopes)
        check_swap(t_teacher, scopes)
        check_write(t_teacher, scopes)
        check_hold(t_teacher, t_pupil_b)
        check_auto_unchanged(t_teacher, t_pupil, scopes)
        check_admin_and_lastset(t_teacher, t_admin, admin_id)
        check_ambiguous_topic(t_teacher, scopes)
        check_idempotent_submit(t_teacher, scopes)
        check_tier_write_seal(t_teacher, t_admin)
        check_figures_and_counts(t_teacher, scopes)
        # ⊕ MRB-336 — the API half of Delete and Edit, and their audit.
        deleted_id = check_delete(t_teacher, t_pupil, t_admin, scopes)
        edited = check_edit(t_teacher, scopes)
        check_delete_edit_audited(t_admin, deleted_id,
                                  edited[0] if isinstance(edited, tuple) else None)
        twenty_title = set_twenty(t_teacher, scopes)

        if not args.api_only:
            # ⚠️ ONE BROWSER PER PERSONA, SEQUENTIALLY. The teacher's browser
            # is closed before the pupil's opens.
            with cdp.Browser() as b:
                p = check_sheet(b, base, sess_teacher, None, args.shots)
                if p:
                    check_sideways(p, "the Classes step", args.shots)
                    check_scroll(p, args.shots)
                    check_sideways(p, "the Topic step", args.shots)
                    check_tier_and_zero(p, scopes)
                    check_detail(p, scopes, args.shots)
                    check_sideways(p, "the Detail step", args.shots)
                    check_dates(p, t_teacher, scopes, args.shots)
                    check_faff(p, scopes)
                    check_toast_and_swap(p, scopes, args.shots)
                    check_hold_validation(p, scopes)
                    check_classes_screen_open(p, base)
                    # LAST of the sheet checks, both of them: each wraps
                    # `fetch` to make a race deterministic, so nothing that
                    # needs an unhindered network runs behind them.
                    race_stems = check_swap_count_race(p, scopes)
                    check_swap_race_stored(t_teacher, race_stems)
                    check_stale_guard(p)
                    p.eval("window.MRBSetWork.close()")
                    # ⚠️ READ BEFORE THE CONSUMER NAVIGATIONS, or this check
                    # is about four other pages rather than about the sheet.
                    record_console(p, "while the sheet was driven")
                    check_consumers(p, base, CONSUMERS, "the teacher",
                                    TITLE + " · from the sheet", args.shots)

            # ⊕ MRB-336 §4/§6 — THE CARDS, THE STATUS PILL, THE SET COLUMN
            # AND THE ROW CONTROLS, IN A BROWSER OF THEIR OWN.
            #
            # ⚠️ THEY CANNOT SHARE THE SHEET'S TAB, and the reason is written
            # three lines above this in the sheet block: `check_swap_count_race`
            # and `check_stale_guard` each REPLACE `window.fetch` to make a
            # race deterministic, and the restore at the end of the second one
            # puts back what it found — which is the FIRST one's wrapper, not
            # the native function. That tab's network is deliberately
            # instrumented for the rest of its life, and the existing comment
            # already says nothing needing an unhindered network may run behind
            # them.
            #
            # Everything below needs a completely ordinary network: it sets
            # work, reloads a generated page, presses a control that writes,
            # and reads the result back. Run in that tab, `open_class_page`
            # timed out five times waiting for a table that was correct in
            # every other context — a red about a wrapper, wearing the name of
            # a product defect.
            with cdp.Browser() as bc:
                pc = bc.attach()
                pc.set_viewport(390, 900)
                signed = sign_in_page(pc, base, FX.TEACHER_EMAIL, pw)
                record(str(signed).startswith("ok"),
                       "the teacher signs in again, in a clean tab, for the "
                       "class-page checks", signed)
                cards_made = check_cards(pc, base, t_teacher, scopes,
                                         args.shots)
                check_remind_names_its_own_card(pc, base, cards_made)
                check_card_counts_are_per_card(pc, base, cards_made)
                check_status_and_set_column(pc, base, t_teacher, scopes,
                                            args.shots)
                check_edit_sheet(pc, base, args.shots)
                check_row_controls(pc, base, t_teacher, scopes, args.shots,
                                   None)
                surf = check_delete_surfaces(pc, base, t_teacher, scopes)
                deleted_title = surf[1] if isinstance(surf, tuple) else None
                check_wide(pc, base, [("8a/Sc1", FX.C_KS3_A),
                                      ("9a/Sc1", FX.C_KS3_NOAUTO)])

            with cdp.Browser() as b2:
                p2 = b2.attach()
                p2.set_viewport(390, 900)
                signed = sign_in_page(p2, base, FX.PUPIL_EMAIL, pw)
                record(str(signed).startswith("ok"),
                       "the pupil signs in through auth.html, for real", signed)
                check_consumers(p2, base, STUDENT_PAGES, "the pupil",
                                TITLE + " · from the sheet", args.shots)
                check_student_twenty(p2, base, twenty_title)
                # ⊕ MRB-336 — the child's half of the delete sweep. It needs
                # the PUPIL's browser, which is why it is here and not beside
                # the teacher's four screens.
                check_delete_student_surfaces(p2, base, deleted_title)

            # ⚠️ THE ADMIN IS A THIRD PERSONA AND NEEDS A THIRD BROWSER.
            # `teacher/admin.html` is a school-operations screen and refuses a
            # plain teacher — correctly. Driving it in the teacher's tab left
            # a page with 47 characters on it and a red that said "the admin
            # screen loads", which is a true sentence about the wrong account.
            with cdp.Browser() as b3:
                p3 = b3.attach()
                p3.set_viewport(390, 900)
                signed = sign_in_page(p3, base, FX.ADMIN_EMAIL, pw)
                record(str(signed).startswith("ok"),
                       "the school admin signs in through auth.html, for real",
                       signed)
                check_admin_repaint(p3, base, t_admin)
    finally:
        if server:
            server.__exit__(None, None, None)
        if site:
            site.shutdown()

    if not args.keep:
        cleanup(teacher_id, admin_id)
        print("\nclearing the throwaway world")
        FX.teardown()
    else:
        print("\n--keep: the throwaway world and this run's rows are left standing")

    bad = [c for c in checks if not c[0]]
    print("\n%s  %d checks, %d failed\n"
          % ("❌" if bad else "✅", len(checks), len(bad)))
    for ok, label, detail in bad:
        print("   · %s" % label)
    return 1 if bad else 0




# ════════════════════════════════════════════════════════════════════════
# 10 · THE CONTRACT ADDITIONS (⊕ 8 Sep 2026, after the cold audit)
# ════════════════════════════════════════════════════════════════════════

# ── (a) `atomic-structure` IS TWO TOPICS, AND ONLY THE SUBJECT SEPARATES THEM ─
#
# ⚠️ THE ONLY AMBIGUOUS ID IN THE CURRICULUM, AND IT FAILS SILENTLY. AQA has a
# topic called Atomic structure in chemistry (paper 1) and another in physics
# (paper 1), and the slug is byte-identical. On a combined class the tree holds
# BOTH, one after the other, so a `findScope` that walked the tree and returned
# the first match handed every teacher who tapped the PHYSICS row a set of
# CHEMISTRY questions — with a plausible title, a plausible paper, and nothing
# anywhere saying so. `subject` is what tells them apart; it is optional
# because every other id in the curriculum is unique.
def check_ambiguous_topic(t_teacher, scopes):
    print("\n10 · Atomic structure is two topics, in two sciences")

    comb = scopes["comb"]
    both = [t for t in comb.get("tree") or [] if t["id"] == "atomic-structure"]
    record(len(both) == 2
           and sorted(t.get("subject") for t in both) == ["chemistry", "physics"],
           "the combined tree really does carry TWO `atomic-structure` topics, "
           "so the ambiguity is present and not hypothetical",
           "subjects: %s" % sorted(t.get("subject") for t in both))
    if len(both) != 2:
        return

    by_subject = {t["subject"]: t for t in both}
    for subject, other in (("physics", "chemistry"), ("chemistry", "physics")):
        want = {c["id"] for c in by_subject[subject]["children"]}
        wrong = {c["id"] for c in by_subject[other]["children"]}
        st, body = preview(t_teacher, FX.C_KS4_COMB, "foundation", "topic",
                           "atomic-structure", 10, subject=subject)
        got = {q.get("slug") or q.get("subtopic") for q in (body or {}).get("picked") or []}
        record(st == 200 and got and got <= want and not (got & wrong),
               "the %s Atomic structure previews %s subtopics and none of "
               "%s's" % (subject, subject, other),
               "status %s · %d question(s) from %s"
               % (st, len(got), sorted(got)[:3]) if st == 200
               else "status %s %s" % (st, json.dumps(body)[:160]))
        record((body or {}).get("scope", {}).get("subject") == subject,
               "…and the answer says which science it answered for, so the "
               "sheet can show the right chip",
               "scope.subject = %r, paper %s"
               % ((body or {}).get("scope", {}).get("subject"),
                  (body or {}).get("scope", {}).get("paper")))

    # ── and the WRITE stores it, which is what a consumer reads ───────
    st, prev = preview(t_teacher, FX.C_KS4_COMB, "foundation", "topic",
                       "atomic-structure", 5, subject="physics")
    ids = [q["id"] for q in (prev.get("picked") or [])]
    st, made = post_set(t_teacher, class_ids=[FX.C_KS4_COMB], tier="foundation",
                        scope_ref="atomic-structure", subject="physics",
                        question_ids=ids, title=TITLE + " · physics atoms")
    if record(st == 200 and made.get("assignment_ids"),
              "a physics Atomic structure set is accepted",
              "status %s %s" % (st, json.dumps(made)[:160])):
        aid = made["assignment_ids"][0]
        st, row = rest("GET", "/rest/v1/assignments?id=eq.%s&select=subject,"
                              "paper,topic,scope_ref" % aid, t_teacher)
        r = row[0] if isinstance(row, list) and row else {}
        record(r.get("subject") == "physics" and r.get("paper") == 1,
               "…and the row records subject=physics, paper=1 — not "
               "chemistry's, which shares the slug",
               json.dumps(r)[:220])

    # An unknown science is a refusal rather than a silent fallback to the
    # first match, which is the behaviour this whole check exists to end.
    st, out = preview(t_teacher, FX.C_KS4_COMB, "foundation", "topic",
                      "atomic-structure", 5, subject="geography")
    record(st == 400, "an unknown science is refused, not quietly ignored",
           "status %s %s" % (st, json.dumps(out)[:120]))


# ── (b) THE SAME SUBMIT TWICE SETS THE WORK ONCE ───────────────────────
#
# ⚠️ NOTHING DEDUPES TEACHER ROWS. `assignments_class_week_uniq` is PARTIAL on
# `source = 'auto'`, so two identical teacher sets are two rows and the child's
# week lists the same homework twice. A teacher whose phone drops the response
# and who presses Set work again is the ordinary way to get there — no
# transient failure and no double-tap is needed, just a slow train.
def check_idempotent_submit(t_teacher, scopes):
    print("\n   the same submit, twice")

    got = pick_topic(scopes["ks3"], 2, "medium")
    if not got:
        return record(False, "a KS3 unit to set twice")
    _n, unit, _s = got
    st, prev = preview(t_teacher, FX.C_KS3_A, "medium", "topic", unit["id"], 4)
    ids = [q["id"] for q in (prev.get("picked") or [])]
    ref = str(uuid.uuid4())
    title = TITLE + " · pressed twice"

    kw = dict(class_ids=[FX.C_KS3_A], tier="medium", scope_ref=unit["id"],
              question_ids=ids, title=title, client_ref=ref)
    st1, first = post_set(t_teacher, **kw)
    st2, second = post_set(t_teacher, **kw)

    record(st1 == 200 and first.get("replayed") is False,
           "the first press sets the work and says it was not a replay",
           "status %s replayed=%s ids=%s"
           % (st1, first.get("replayed"), first.get("assignment_ids")))
    record(st2 == 200 and second.get("replayed") is True,
           "the second press with the SAME client_ref answers 200 "
           "`replayed: true` — a retry is told it succeeded, because it did",
           "status %s replayed=%s" % (st2, second.get("replayed")))
    record(sorted(second.get("assignment_ids") or []) ==
           sorted(first.get("assignment_ids") or []),
           "…and hands back the SAME assignment ids, so a sheet that retried "
           "can still refresh the right card",
           "%s vs %s" % (first.get("assignment_ids"),
                         second.get("assignment_ids")))

    # ⚠️ THE ROW COUNT IS THE PROOF, NOT THE FLAG. A route could answer
    # `replayed: true` and insert anyway.
    st, rows = rest("GET", "/rest/v1/assignments?class_id=eq.%s&title=eq.%s"
                           "&select=id" % (FX.C_KS3_A, urllib.parse.quote(title)),
                    t_teacher)
    n = len(rows) if isinstance(rows, list) else -1
    record(n == 1,
           "…and the class holds exactly ONE assignment with that title, not "
           "two — the week does not list the same homework twice",
           "%d row(s) titled %r" % (n, title))

    # A DIFFERENT ref is a different set, or the guard would make a teacher
    # unable to set the same topic twice on purpose.
    st3, third = post_set(t_teacher, **dict(kw, client_ref=str(uuid.uuid4()),
                                            title=title + " again"))
    record(st3 == 200 and third.get("replayed") is False
           and sorted(third.get("assignment_ids") or []) !=
           sorted(first.get("assignment_ids") or []),
           "a NEW client_ref sets a new piece of work — the guard is an "
           "idempotency key, not a lock on the topic",
           "status %s replayed=%s" % (st3, third.get("replayed")))

    for bad in (None, "", "not-a-uuid", 42):
        st, out = call("POST", "/api/teacher/set-work", t_teacher, {
            "class_ids": [FX.C_KS3_A], "tier": "medium", "scope_kind": "topic",
            "scope_ref": unit["id"], "question_ids": ids,
            "title": TITLE + " · no ref", "due_at": DUE.isoformat(),
            "release_at": None, "client_ref": bad})
        if not record(st == 400 and (out or {}).get("error") == "bad_client_ref",
                      "a submit with client_ref %r is refused — without one "
                      "there is no way to make a retry safe" % (bad,),
                      "status %s %s" % (st, json.dumps(out)[:110])):
            break


# ── (c) THE TIER IS NOT A COLUMN A TEACHER MAY WRITE ───────────────────
#
# ⚠️ THE ROUTE BEING ADMIN-ONLY IS NOT THE SAME CLAIM AS THE COLUMN BEING
# PROTECTED. `POST /api/admin/class-tier` checks `standing.schoolAdmin` in the
# backend — but `classes` is a table a signed-in teacher can already UPDATE
# through PostgREST for the things a teacher legitimately changes, and a
# class's tier decides WHICH QUESTIONS A CHILD IS SERVED. A teacher who can
# PATCH it can move their whole class onto Higher content from the browser
# console, and every check that goes through the route would still be green.
#
# So the seal is in the DATABASE, and this asks the database directly, with a
# real teacher's JWT and no backend in the way.
def check_tier_write_seal(t_teacher, t_admin):
    print("\n   who may move a class's tier")

    st, before = rest("GET", "/rest/v1/classes?id=eq.%s&select=tier,"
                             "tier_pathway_source" % FX.C_KS4_COMB, t_admin)
    was = (before[0] if isinstance(before, list) and before else {})

    st, out = rest("PATCH", "/rest/v1/classes?id=eq." + FX.C_KS4_COMB,
                   t_teacher, {"tier": "higher"}, prefer="return=representation")
    st2, after = rest("GET", "/rest/v1/classes?id=eq.%s&select=tier,"
                             "tier_pathway_source" % FX.C_KS4_COMB, t_admin)
    now = (after[0] if isinstance(after, list) and after else {})

    # ⚠️ THE ROW IS THE PROOF, NOT THE STATUS. PostgREST answers an UPDATE that
    # matched no row with a cheerful 200 and an empty array, and a policy that
    # merely hides the row would give the same 200 — so "it was refused" and
    # "it silently did nothing" and "it worked" are three different things that
    # can all look alike from the status line alone. Read the tier back.
    record(now.get("tier") == was.get("tier"),
           "a teacher's own JWT cannot move `classes.tier` through PostgREST "
           "— the seal is in the database, not only in the route",
           "tier %r before, %r after, PATCH answered %s"
           % (was.get("tier"), now.get("tier"), st))
    record(now.get("tier_pathway_source") == was.get("tier_pathway_source"),
           "…and nothing was stamped `admin` by an edit that did not happen",
           "source %r → %r" % (was.get("tier_pathway_source"),
                               now.get("tier_pathway_source")))

    # ⚠️ AND THE ADMIN ROUTE MUST STILL WORK, or "nobody can change it" would
    # pass this pair and break the one screen that repairs a mis-imported class.
    st, ok = call("POST", "/api/admin/class-tier", t_admin,
                  {"class_id": FX.C_KS4_COMB, "tier": "higher",
                   "pathway": "combined", "subject": None})
    record(st == 200 and (ok.get("class") or {}).get("tier") == "higher",
           "…while the admin route still moves it, so the seal is a seal and "
           "not a wall", "status %s %s" % (st, json.dumps(ok)[:160]))
    call("POST", "/api/admin/class-tier", t_admin,
         {"class_id": FX.C_KS4_COMB, "tier": "foundation",
          "pathway": "combined", "subject": None})


# ── (d) A FIGURE CANNOT BE SET, AND THE COUNTS MUST BE HONEST ──────────
#
# ⚠️ A KS3 QUESTION MAY CARRY A `figure`, AND THE SHEET CANNOT DRAW ONE. The
# sheet renders a stem and four options; a question whose stem says "look at
# the diagram" with no diagram is unanswerable, and it is unanswerable for the
# CHILD, in the assignment, after a teacher has set it in good faith.
def check_figures_and_counts(t_teacher, scopes):
    print("\n   figures, and counts that mean what they say")

    import ks3_data.question_bank as qb
    with_figure = set()
    for entry in qb.load_bank():
        for q in entry["questions"]:
            if q.get("figure"):
                with_figure.add(q["id"])

    seen, offered = 0, []
    for topic in (scopes["ks3"].get("tree") or [])[:8]:
        for tier in ("easy", "medium", "hard"):
            st, body = preview(t_teacher, FX.C_KS3_A, tier, "topic",
                               topic["id"], 20)
            for q in (body or {}).get("picked") or []:
                seen += 1
                if q.get("figure") is not None or q["id"] in with_figure:
                    offered.append("%s (%s @ %s)" % (q["id"], topic["id"], tier))
    record(not offered,
           "preview_no_figures — no KS3 question carrying a figure is ever "
           "offered; the sheet draws a stem and four options and cannot draw "
           "a diagram",
           "%d question(s) sampled across 8 units × 3 tiers; %d figure-bearing "
           "rows exist in the bank and none was served"
           % (seen, len(with_figure)) if not offered
           else "OFFERED: %s" % offered[:5])

    # ── /scope's count is what the chips cap against; preview is what
    #    arrives. They must agree, or a chip promises a question the pool
    #    cannot deliver.
    disagreed = []
    for key, cid, tier in (("ks3", FX.C_KS3_A, "medium"),
                           ("comb", FX.C_KS4_COMB, "foundation"),
                           ("bi", FX.C_KS4_TRIPLE, "higher")):
        for topic in (scopes[key].get("tree") or [])[:6]:
            n = (topic.get("counts") or {}).get(tier, 0)
            if not n:
                continue
            st, body = preview(t_teacher, cid, tier, "topic", topic["id"], 20)
            avail = (body or {}).get("available")
            picked = len((body or {}).get("picked") or [])
            # `available` de-duplicates by normalised stem, so it may be
            # SMALLER than the count — never larger, and the number picked
            # must be exactly what was asked for or exactly what exists.
            if avail is None or avail > n or picked != min(20, avail):
                disagreed.append("%s @ %s: scope %s, available %s, picked %s"
                                 % (topic["id"], tier, n, avail, picked))
    record(not disagreed,
           "scope_counts_agree_with_preview — every count the chips cap "
           "against is at least what preview can serve, and a request for "
           "twenty returns exactly what exists",
           "18 topic(s) across three cohorts agree" if not disagreed
           else "; ".join(disagreed[:4]))


# ── (g) SWAP IN FLIGHT, THEN A COUNT CHIP ──────────────────────────────
#
# ⚠️ TWO ASYNC WRITES INTO ONE LIST, AND THE SECOND REBUILDS IT. Swap replaces
# `S.picked[i]` when its answer lands; a count chip calls `/preview` and
# replaces `S.picked` ENTIRELY. Press Swap and tap a chip before it returns and
# the swap's answer can be written into a list that no longer exists — leaving
# `S.picked` holding a question that is NOT on the screen. The teacher reads ten
# rows, presses Set work, and the class is set something the teacher never saw.
#
# It is invisible in every other way: the DOM is consistent, the count is right,
# and only the ids disagree.
def check_swap_count_race(p, scopes):
    print("\n   Swap in flight, then a count chip")

    big = None
    for t in scopes["comb"].get("tree") or []:
        if (t.get("counts") or {}).get("foundation", 0) >= 20:
            big = t["id"]
            break
    if not big or not goto_detail(p, FX.C_KS4_COMB, "foundation", "topic", big):
        return record(False, "reach a twenty-deep topic for the swap race")

    # Hold the swap two seconds so the race is arranged rather than hoped for.
    p.eval("""(function(){
      if (window.__mrbSwapHeld) { return true; }
      window.__mrbSwapHeld = true;
      var real = window.fetch;
      window.fetch = function (u, o) {
        var slow = String(u).indexOf('set-work/swap') > -1;
        return real(u, o).then(function (r) {
          if (!slow) { return r; }
          return new Promise(function (res) {
            setTimeout(function () { res(r); }, 2000); });
        });
      };
      return true;})()""")

    p.eval("""(function(){var b=document.querySelector(
        '[data-sw="swap"]:not([disabled])'); if(b){b.click();} return !!b;})()""")
    time.sleep(0.2)
    p.eval("""(function(){var cs=document.querySelectorAll(
        '[data-sw="count-chips"] .sw-chip');
        for(var i=0;i<cs.length;i++){if(cs[i].textContent==='5'){cs[i].click();}}
        return true;})()""")
    wait_for(p, "document.querySelectorAll('[data-sw=\"question\"]').length === 5")
    time.sleep(3.0)          # the held swap lands here, into the new list

    # ⚠️ THE SUBMITTED IDS ARE READ FROM THE SHEET'S OWN PAYLOAD, and the rows
    # from the DOM. Comparing the DOM with itself would prove nothing.
    got = p.eval(r"""(function(){
      var rows = document.querySelectorAll('[data-sw="question"]');
      var onScreen = [];
      for (var i = 0; i < rows.length; i++) {
        onScreen.push((rows[i].querySelector('[data-sw="stem"]').textContent
                       || '').trim());
      }
      return {rows: onScreen.length, stems: onScreen};})()""")

    # Set it, and read back what actually reached the database.
    p.eval("""(function(){var t=document.querySelector('[data-sw="title"]');
        t.value=%s; t.dispatchEvent(new Event('input',{bubbles:true}));})()"""
           % json.dumps(TITLE + " · swap race"))
    time.sleep(0.3)
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    ok = wait_for(p, "(function(){var t=document.querySelector("
                     "'[data-sw=\"toast\"]');return t && !t.hidden;})()")
    record(ok and got["rows"] == 5,
           "the sheet shows five rows after the chip, with a swap still in "
           "flight behind it", "%d row(s) on screen" % got["rows"])
    return got["stems"]


def check_swap_race_stored(t_teacher, stems):
    """The other half of (g): what was STORED must be what was on screen."""
    if not stems:
        return
    st, rows = rest("GET", "/rest/v1/assignments?class_id=eq.%s&title=eq.%s"
                           "&select=id&order=created_at.desc&limit=1"
                    % (FX.C_KS4_COMB,
                       urllib.parse.quote(TITLE + " · swap race")), t_teacher)
    if not (isinstance(rows, list) and rows):
        return record(False, "the swap-race set reached the database")
    aid = rows[0]["id"]
    st, body = call("GET", "/api/class/current-assignment?class_id=%s"
                    "&assignment_id=%s" % (FX.C_KS4_COMB, aid), t_teacher)
    stored = [(q.get("text") or "").strip()
              for q in (body or {}).get("questions") or []]

    def norm(x):
        return re.sub(r"\s+", " ", str(x or "")).strip()

    on = [norm(x) for x in stems]
    db = [norm(x) for x in stored]
    record(len(db) == len(on) and set(db) == set(on),
           "swap_count_race — the questions STORED are exactly the questions "
           "that were on the screen; a swap landing after a count chip cannot "
           "smuggle a row the teacher never read into the set",
           "%d on screen, %d stored, identical" % (len(on), len(db))
           if set(db) == set(on)
           else "on screen but not stored: %s\n        stored but not shown: %s"
                % (sorted(set(on) - set(db))[:2], sorted(set(db) - set(on))[:2]))


# ── (h) ⊕ MRB-336 · THE HELD SCHOOL SETS WORK FOR TODAY ────────────────
#
# ⛔ THIS CHECK USED TO ASSERT THE OPPOSITE, and the thing it asserted was the
# defect. The held school opens in eight days; a teacher choosing Release Now
# and a due date inside that window was refused (`bad_due_at`), because the
# server moved the release to the open date and the work was then overdue on
# the day it appeared. The sheet disabled the primary to say so a second
# earlier. Both halves were correct implementations of a rule Mide has now
# deleted: "the point of setting work is so that students can do assignments
# even though the automatic assignments hasn't gone live yet."
#
# So the same two taps are now the ORDINARY case, and this check proves it —
# no hold node, a live primary, a clean Due field.
#
# ⚠️ AND THE SECOND HALF IS WHY THIS CHECK STAYS RATHER THAN BEING DELETED.
# Removing the clamp removes the sheet's only reason to refuse a date, and a
# validator with nothing left to refuse is a validator nobody notices losing.
# Due BEFORE the release the teacher typed is still impossible, still stops
# the primary, still outlines the field, and still sends nothing.
def check_hold_validation(p, scopes):
    print("\n   the held school: Release Now, due inside the hold window")

    got = pick_topic(scopes["ks3"], 1, "medium")
    if not got:
        return record(False, "a unit to try in the held school")
    _n, unit, _s = got
    if not goto_detail(p, FX.C_KS3_HELD, "medium", "topic", unit["id"]):
        return record(False, "reach Detail on the held school's class")

    p.eval("""(function(){var t=document.querySelector('[data-sw="title"]');
        t.value=%s; t.dispatchEvent(new Event('input',{bubbles:true}));})()"""
           % json.dumps(TITLE + " · inside the hold"))
    # Release Now, and a due date two days out — inside the eight-day hold.
    p.eval("""(function(){var cs=document.querySelectorAll(
        '[data-sw="release-chips"] .sw-chip');
        for(var i=0;i<cs.length;i++){if(cs[i].textContent==='Now'){
          cs[i].click();}} return true;})()""")
    soon = p.eval("""(function(){
        var f=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/London',
          year:'numeric',month:'2-digit',day:'2-digit'});
        var o={}; f.formatToParts(new Date()).forEach(function(x){o[x.type]=x.value;});
        var d=new Date(Date.UTC(+o.year,+o.month-1,+o.day)+2*86400000);
        return d.toISOString().slice(0,10);})()""")
    p.eval("""(function(){var d=document.querySelector('[data-sw="due-date"]');
        d.value=%s; d.dispatchEvent(new Event('input',{bubbles:true}));
        d.dispatchEvent(new Event('change',{bubbles:true}));})()""" % json.dumps(soon))
    time.sleep(0.5)

    state = p.eval("""(function(){
      var o = document.querySelector('[data-sw="overlay"]');
      var pri = document.querySelector('[data-sw="primary"]');
      var dd = document.querySelector('[data-sw="due-date"]');
      var dt = document.querySelector('[data-sw="due-time"]');
      return {disabled: !!pri.disabled,
              dueOutlined: dd.classList.contains('sw-bad')
                        || dt.classList.contains('sw-bad'),
              holdNode: !!document.querySelector('[data-sw="hold"]'),
              open: (o.textContent||'').indexOf('Assignments open'),
              due: dd.value};})()""")
    record(state["disabled"] is False and state["dueOutlined"] is False,
           "hold_does_not_stop_the_teacher — Release Now with a due date "
           "inside the school's hold window: the primary is LIVE and the Due "
           "field is clean", json.dumps(state))
    record(state["holdNode"] is False and state["open"] == -1,
           "…and the sheet says nothing about the hold, because the hold no "
           "longer decides anything the teacher can see", json.dumps(state))

    # ── the refusal that REMAINS: due before the release itself ───────
    #
    # Release Later, next week; Due tomorrow. Nothing to do with the school.
    later = p.eval("""(function(){
        var f=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/London',
          year:'numeric',month:'2-digit',day:'2-digit'});
        var o={}; f.formatToParts(new Date()).forEach(function(x){o[x.type]=x.value;});
        var base=Date.UTC(+o.year,+o.month-1,+o.day);
        return {rel: new Date(base+7*86400000).toISOString().slice(0,10),
                due: new Date(base+1*86400000).toISOString().slice(0,10)};})()""")
    p.eval("""(function(){var cs=document.querySelectorAll(
        '[data-sw="release-chips"] .sw-chip');
        for(var i=0;i<cs.length;i++){if(cs[i].textContent==='Later'){
          cs[i].click();}} return true;})()""")
    time.sleep(0.3)
    p.eval("""(function(){var v=%s;
        var r=document.querySelector('[data-sw="release-date"]');
        var d=document.querySelector('[data-sw="due-date"]');
        r.value=v.rel; d.value=v.due;
        [r,d].forEach(function(n){
          n.dispatchEvent(new Event('input',{bubbles:true}));
          n.dispatchEvent(new Event('change',{bubbles:true}));});})()"""
           % json.dumps(later))
    time.sleep(0.5)
    bad = p.eval("""(function(){
      var pri = document.querySelector('[data-sw="primary"]');
      var dd = document.querySelector('[data-sw="due-date"]');
      var dt = document.querySelector('[data-sw="due-time"]');
      return {disabled: !!pri.disabled,
              dueOutlined: dd.classList.contains('sw-bad')
                        || dt.classList.contains('sw-bad')};})()""")
    record(bad["disabled"] and bad["dueOutlined"],
           "due_before_release_still_refused — Release next week with Due "
           "tomorrow: the primary is DISABLED and the Due field is outlined",
           json.dumps(bad))

    # ⚠️ AND NOTHING WAS SENT. A disabled button that still fires would look
    # identical from the screen.
    n = p.eval("performance.getEntriesByType('resource').filter(function(r){"
               "return r.name.indexOf('/api/teacher/set-work') > -1 "
               "&& r.name.indexOf('set-work/') < 0;}).length")
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    time.sleep(1.0)
    n2 = p.eval("performance.getEntriesByType('resource').filter(function(r){"
                "return r.name.indexOf('/api/teacher/set-work') > -1 "
                "&& r.name.indexOf('set-work/') < 0;}).length")
    record(n2 == n,
           "…and pressing the disabled primary sends NOTHING — a POST count "
           "of %d before and after" % n, "%d → %d" % (n, n2))


# ── (i) OPENED FROM THE CLASSES SCREEN, NOTHING IS PRESELECTED ─────────
#
# ⚠️ `classes.html` HAS NO CLASS IN ITS URL, so the sheet's opening class is
# `this.CLASSES[0]` — whichever class happens to sort first. Preselecting it is
# a sheet that has quietly decided, on a screen showing twenty classes, which
# one the teacher meant. The press that follows sets real work on a real class
# the teacher did not choose.
#
# And once a class IS chosen, the rest of the list is no longer all selectable:
# cohort is what makes two classes safe to set the same work on, so a class of
# another cohort must go dead rather than be offered and then refused by the
# server with `cohort_mismatch`.
def check_classes_screen_open(p, base):
    print("\n   the sheet opened from the classes screen")

    if not goto_ready(p, "%s/teacher/classes.html?env=test&api=%s"
                      % (base, PAGE_API),
                      "!!(window.MRBSetWork && window.MRBSetWork.open)",
                      settle=6.0):
        return record(False, "the classes screen loads with the sheet module")

    # ⚠️ THERE ARE TWO "SET WORK" BUTTONS ON THIS SCREEN AND THEY MEAN
    # DIFFERENT THINGS. The one on a CLASS CARD carries that card's id and is
    # SUPPOSED to preselect it — the teacher has already said which class. The
    # one in the header carries none, because the header is not about a class.
    # Pressing the first match in document order found a card, saw its class
    # correctly preselected, and reported the header's behaviour as broken.
    #
    # So every visible one is pressed in turn and identified by what the sheet
    # says it opened on (`data-sw-class`), which is the only thing that tells
    # them apart from out here.
    opened = p.eval(r"""(async function(){
      var bs = document.querySelectorAll('button, a'), out = [];
      for (var i = 0; i < bs.length; i++) {
        var b = bs[i];
        if ((b.textContent || '').trim() !== 'Set work') { continue; }
        if (b.offsetParent === null) { continue; }
        b.click();
        await new Promise(function (r) { setTimeout(r, 400); });
        var o = document.querySelector('[data-sw="overlay"]');
        out.push({i: i, cls: o ? (o.getAttribute('data-sw-class') || '') : null});
        if (window.MRBSetWork) { window.MRBSetWork.close(); }
        await new Promise(function (r) { setTimeout(r, 150); });
      }
      return out;})()""")
    # ⚠️ EVERY REACHABLE "Set work" ON THIS SCREEN IS A CLASS CARD'S, and a
    # card's SHOULD preselect: the teacher has already said which class by
    # tapping that card. Measured — three cards, each opening on its own id —
    # so the card behaviour is asserted here and the no-class case is driven
    # through the page's own seam below.
    cards = [o for o in (opened or []) if o["cls"]]
    record(bool(cards) and all(o["cls"] for o in (opened or [])),
           "every Set work control reachable on the classes screen is a class "
           "CARD's, and each opens on its own class — a card has already been "
           "chosen, so preselecting it is right",
           "%d control(s): %s" % (len(opened or []),
                                  [o["cls"][-3:] for o in (opened or [])]))

    # ⚠️ THE NO-CLASS CASE IS DRIVEN THROUGH `MRB_SET_WORK_OPEN('')`, WHICH IS
    # THE PAGE'S OWN SEAM AND NOT A STUB. It is exactly what node 165 — the
    # header control — is bound to (`openSetWork: () => MRB_SET_WORK_OPEN(
    # s.classId || '')`), and MRB-335 changed it from `return false` to
    # passing the empty string through. That control is present in the
    # compiled page and was NOT reachable in this sweep at 390px; whether it
    # should be is a question for the site lane. What is measurable from here
    # is the behaviour it invokes, and that is what this drives.
    if p.eval("typeof MRB_SET_WORK_OPEN === 'function'"):
        record(p.eval("MRB_SET_WORK_OPEN('')") is True,
               "MRB_SET_WORK_OPEN('') opens the sheet rather than refusing — "
               "an empty class is the classes screen, not an error (it used "
               "to `return false`, which made that control dead)")
    else:
        return record(False, "the page exposes MRB_SET_WORK_OPEN")
    if not wait_for(p, "document.querySelectorAll('[data-sw=\"class\"]')"
                       ".length > 0"):
        return record(False, "the sheet opened on no class lists the classes")

    state = p.eval("""(function(){
      var rs = document.querySelectorAll('[data-sw="class"]'), on = [];
      for (var i = 0; i < rs.length; i++) {
        if (rs[i].getAttribute('aria-pressed') === 'true') {
          on.push(rs[i].getAttribute('data-sw-ref')); } }
      return {rows: rs.length, selected: on,
              primary: !!document.querySelector('[data-sw="primary"]').disabled,
              step: document.querySelector(
                '[data-sw="overlay"]').getAttribute('data-sw-step')};})()""")
    record(state["rows"] > 0 and not state["selected"] and state["primary"],
           "classes_screen_no_preselect — the sheet opens on the Classes step "
           "with NOTHING chosen and Next disabled, rather than deciding for "
           "the teacher which of %d classes they meant" % state["rows"],
           json.dumps(state))

    # ── THE FIRST TAP IS THE ANCHOR, AND IT IS WHAT ASKS FOR THE SCOPE ──
    #
    # ⚠️ DRIVEN ON THE LIVE TEST PAGE, NOT ON A FIXTURE, AND THE DIFFERENCE
    # DECIDES WHAT THIS CHECK CAN SEE. A fixture page carries no
    # `MrBadmusTeacherGuard`, so `token()` rejects before `fetch` is ever
    # called and `/scope` can never SUCCEED there — a fixture can only ever
    # exercise the failure path. The success path needs a real session, which
    # is why this runs on `teacher/classes.html` as the signed-in teacher.
    def scope_calls():
        return p.eval("performance.getEntriesByType('resource').filter("
                      "function(r){return r.name.indexOf('set-work/scope')"
                      ">-1;}).map(function(r){return r.name.split("
                      "'class_id=')[1].split('&')[0];})") or []

    before_calls = scope_calls()
    picked = p.eval("""(function(){var rs=document.querySelectorAll(
        '[data-sw="class"]');
        for(var i=0;i<rs.length;i++){
          if(rs[i].getAttribute('aria-pressed')!=='true'){
            rs[i].click(); return rs[i].getAttribute('data-sw-ref');}}
        return null;})()""")
    got = wait_for(p, "!document.querySelector('[data-sw=\"primary\"]').disabled")
    after_calls = scope_calls()
    new_calls = after_calls[len(before_calls):]

    record(bool(picked) and picked in new_calls,
           "classes_screen_anchors_on_first_tap — the first tap is what asks "
           "for the scope: a /scope request goes out FOR THAT CLASS, and none "
           "went before it",
           "%d call(s) before, %d after; the new one is for %s"
           % (len(before_calls), len(after_calls),
              (new_calls[0][-3:] if new_calls else "nothing")))
    record(got, "…and Next comes alive once that scope has RESOLVED — the "
                "dead end is gone",
           "primary disabled = %s"
           % p.eval("document.querySelector('[data-sw=\"primary\"]').disabled"))

    # ⚠️ NEXT BEING ENABLED IS NOT THE SAME CLAIM AS THE NEXT STEP WORKING.
    # A primary that lights and then lands on an empty topic list is the
    # defect one step further along.
    p.eval("document.querySelector('[data-sw=\"primary\"]').click()")
    loaded = wait_for(p, "document.querySelectorAll('[data-sw=\"topic\"]')"
                         ".length > 0")
    record(loaded,
           "classes_screen_topic_step_loads — pressing Next reaches the Topic "
           "step with that class's own tree on it",
           "%s topic row(s), step %s"
           % (p.eval("document.querySelectorAll('[data-sw=\"topic\"]').length"),
              p.eval("document.querySelector('[data-sw=\"overlay\"]')"
                     ".getAttribute('data-sw-step')")))

    # ── UNTICKING THE LAST CLASS UN-ANCHORS ────────────────────────────
    #
    # A sheet that stayed anchored to a class the teacher had just unticked
    # would offer the rest of the list as though the cohort were still
    # settled — and would then be refused by the server with `cohort_mismatch`
    # for a choice the teacher had explicitly undone.
    p.eval("document.querySelector('[data-sw=\"back\"]').click()")
    time.sleep(0.4)
    p.eval("""(function(){var rs=document.querySelectorAll(
        '[data-sw="class"][aria-pressed="true"]');
        for(var i=0;i<rs.length;i++){rs[i].click();} return true;})()""")
    time.sleep(0.6)
    un = p.eval("""(function(){
      var rs = document.querySelectorAll('[data-sw="class"]');
      var on = 0, dead = 0;
      for (var i = 0; i < rs.length; i++) {
        if (rs[i].getAttribute('aria-pressed') === 'true') { on++; }
        if (rs[i].getAttribute('aria-disabled') === 'true' || rs[i].disabled) {
          dead++; } }
      return {rows: rs.length, on: on, dead: dead,
              primary: !!document.querySelector('[data-sw="primary"]').disabled,
              step: document.querySelector(
                '[data-sw="overlay"]').getAttribute('data-sw-step')};})()""")
    record(un["on"] == 0 and un["dead"] == 0 and un["primary"] is True,
           "classes_screen_unanchors — unticking the last class un-anchors "
           "the sheet: every row is selectable again and Next goes back to "
           "disabled", json.dumps(un))

    # …and a DIFFERENT first pick re-anchors, or "un-anchored" would be a
    # sheet that had simply stopped working.
    before2 = scope_calls()
    second = p.eval("""(function(){var rs=document.querySelectorAll(
        '[data-sw="class"]');
        for(var i=rs.length-1;i>=0;i--){
          if(rs[i].getAttribute('aria-pressed')!=='true'){
            rs[i].click(); return rs[i].getAttribute('data-sw-ref');}}
        return null;})()""")
    alive = wait_for(p, "!document.querySelector('[data-sw=\"primary\"]')"
                        ".disabled")
    after2 = scope_calls()
    record(bool(second) and second != picked and alive
           and second in after2[len(before2):],
           "classes_screen_reanchors — a different first pick anchors on THAT "
           "class and fetches its scope, so un-anchoring is a reset and not a "
           "breakage",
           "first %s, then %s; %d new /scope call(s)"
           % (str(picked)[-3:], str(second)[-3:],
              len(after2) - len(before2)))

    # ── THE ONE WORD A FAILED SCOPE IS ALLOWED TO SAY, ON STEP 0 ───────
    #
    # The tree carries the same word one step further in, and a teacher who
    # cannot get past step 0 was never going to read that one.
    note = p.eval("""(function(){var n=document.querySelector(
        '[data-sw="class-note"]');
        return n ? {hidden: !!n.hidden, text: (n.textContent||'').trim(),
                    cls: n.className} : null;})()""")
    record(note is not None and note["text"] == "Unavailable"
           and note["hidden"] is True,
           "the class panel carries the one-word failure note, hidden while "
           "the scope is fine — one word, on the step the teacher is standing "
           "on", json.dumps(note))
    p.eval("window.MRBSetWork.close()")


# ── (e) THE ADMIN SCREEN REPAINTS AFTER A SAVE ─────────────────────────
#
# ⚠️ DRIVING THE ROUTE IS NOT DRIVING THE SCREEN, and the gap between them is
# where `.select()` lives. `POST /api/admin/class-tier` is already proved to
# write and to audit. What that says nothing about is whether the PAGE then
# shows the new value — and a screen that saves correctly and repaints stale is
# the shape a head of department reads as "it didn't save", so they press it
# again, and again.
def check_admin_repaint(p, base, t_admin):
    print("\n   the admin screen after a save")

    if not goto_ready(p, "%s/teacher/admin.html?env=test&api=%s"
                      % (base, PAGE_API),
                      "document.body && document.body.innerText.length > 200",
                      settle=7.0):
        return record(False, "the admin screen loads")

    found = p.eval("""(function(){
      var sels = document.querySelectorAll('select');
      var out = [];
      for (var i = 0; i < sels.length; i++) {
        out.push({id: sels[i].id || sels[i].name || '',
                  n: sels[i].options.length,
                  v: sels[i].value,
                  label: (sels[i].getAttribute('aria-label') || '')});
      }
      return {selects: out, text: document.body.innerText.slice(0, 400)};})()""")
    record(bool(found["selects"]),
           "the admin screen renders its class-cohort selectors",
           "%d select(s): %s" % (len(found["selects"]),
                                 [s["id"] or s["label"] for s in
                                  found["selects"]][:6]))
    if not found["selects"]:
        return

    # Change the tier through the SCREEN and read the screen back.
    before = json.loads(json.dumps(found["selects"]))
    changed = p.eval("""(function(){
      var sels = document.querySelectorAll('select'), out = null;
      for (var i = 0; i < sels.length; i++) {
        var s = sels[i], opts = [];
        for (var j = 0; j < s.options.length; j++) { opts.push(s.options[j].value); }
        if (opts.indexOf('higher') > -1 && opts.indexOf('foundation') > -1) {
          s.value = (s.value === 'higher') ? 'foundation' : 'higher';
          s.dispatchEvent(new Event('change', {bubbles: true}));
          out = {idx: i, to: s.value};
          break; } }
      return out;})()""")
    if not changed:
        return record(False, "a tier selector with both tiers exists on the "
                             "admin screen", json.dumps(before)[:220])
    time.sleep(0.4)
    p.eval("""(function(){var bs=document.querySelectorAll('button');
        for(var i=0;i<bs.length;i++){var t=(bs[i].textContent||'').trim();
          if(/^(Save|Apply|Update)/i.test(t) && bs[i].offsetParent!==null){
            bs[i].click(); return t;}} return false;})()""")
    time.sleep(2.5)

    after = p.eval("""(function(){var sels=document.querySelectorAll('select');
        var s=sels[%d]; return s ? s.value : null;})()""" % changed["idx"])
    record(after == changed["to"],
           "admin_repaint_after_save — the selector still shows the value that "
           "was saved, rather than snapping back to the old one",
           "set to %r, screen shows %r" % (changed["to"], after))

    # ⚠️ AND THE DATABASE AGREES. A screen that keeps the new value locally and
    # saved nothing looks identical.
    st, rows = rest("GET", "/rest/v1/classes?id=in.(%s,%s,%s)&select=name,tier,"
                           "tier_pathway_source&order=name"
                    % (FX.C_KS4_COMB, FX.C_KS4_TRIPLE, FX.C_KS4_SEPS), t_admin)
    record(isinstance(rows, list) and any(r.get("tier") == changed["to"]
                                          for r in rows),
           "…and a class really does hold that tier in the database",
           json.dumps(rows)[:240])
    # Put every KS4 fixture class back where its name says.
    for cid in (FX.C_KS4_COMB, FX.C_KS4_TRIPLE, FX.C_KS4_SEPS):
        t, pth, sub = FX.rule_for(
            {FX.C_KS4_COMB: "10b/Sc5", FX.C_KS4_TRIPLE: "10a/Bi1",
             FX.C_KS4_SEPS: "10c/Ph1"}[cid])
        call("POST", "/api/admin/class-tier", t_admin,
             {"class_id": cid, "tier": t, "pathway": pth, "subject": sub})


# ── (f) TWENTY QUESTIONS, AS THE CHILD MEETS THEM ──────────────────────
#
# ⚠️ TWENTY IS THE NEW NUMBER AND NOTHING DOWNSTREAM WAS BUILT FOR IT. Every
# automatic assignment in the estate is TEN (`ASSIGNMENT_SIZE`), so the student
# page, its progress dots, its scroller and its submit have only ever been met
# by ten. Twenty is the ceiling Set work v2 offers a teacher, and the first
# time anybody finds out whether the page can carry it must not be a Year 8
# class on a Monday morning.
def set_twenty(t_teacher, scopes):
    """Set a twenty-question KS3 assignment on 8a/Sc1. Returns its title."""
    best = None
    for t in scopes["ks3"].get("tree") or []:
        n = (t.get("counts") or {}).get("medium", 0)
        if n >= 20 and (best is None or n > best[1]):
            best = (t["id"], n)
    if not best:
        record(False, "a KS3 unit deep enough for twenty at Medium")
        return None
    unit, n = best
    st, prev = preview(t_teacher, FX.C_KS3_A, "medium", "topic", unit, 20)
    ids = [q["id"] for q in (prev.get("picked") or [])]
    if len(ids) != 20:
        record(False, "twenty questions preview on %s" % unit,
               "got %d of 20 from a pool of %d" % (len(ids), n))
        return None
    title = TITLE + " · twenty"
    st, made = post_set(t_teacher, class_ids=[FX.C_KS3_A], tier="medium",
                        scope_ref=unit, question_ids=ids, title=title)
    if not record(st == 200, "a twenty-question set is written",
                  "status %s, unit %s" % (st, unit)):
        return None
    aid = made["assignment_ids"][0]
    st, back = rest("GET", "/rest/v1/assignment_questions?assignment_id=eq.%s"
                           "&select=position&order=position" % aid, t_teacher)
    pos = [r["position"] for r in back] if isinstance(back, list) else []
    record(pos == list(range(1, 21)),
           "…with twenty question rows at positions 1..20, none dropped",
           "%d row(s), positions %s…%s" % (len(pos), pos[:3], pos[-2:])
           if pos else "no rows")
    return title


def check_student_twenty(p, base, title):
    """The child's page, with twenty questions on it."""
    print("\n   the child opens a twenty-question set")
    if not title:
        return
    # ⚠️ ⊕ MRB-336, 8 Sep 2026 — SET THE VIEWPORT, DO NOT INHERIT IT. This
    # function asserts `scrollWidth <= clientWidth` twice and had no
    # `set_viewport` of its own: it was reading whatever width the previous
    # check happened to leave behind. That was 390 today and correct today,
    # for a reason nothing here states — and `ks3_browser.screenshot()`
    # (ks3_browser.py:572-577) takes `width=1280` as its DEFAULT and calls
    # `set_viewport(width, height)`, so ONE screenshot taken without an
    # explicit width, anywhere upstream, silently turns every "clean at
    # 390px" assertion below into a desktop measurement that passes because
    # a desktop has room. A width assertion has to name its own width.
    p.set_viewport(390, 900)
    if not goto_ready(p, "%s/student/class.html?class=%s&env=test&api=%s"
                      % (base, FX.C_KS3_A, PAGE_API),
                      "document.body && document.body.innerText.length > 200",
                      settle=7.0):
        return record(False, "the student class page loads")

    body = p.eval("document.body.innerText") or ""
    record(title in body,
           "student_sees_twenty — the twenty-question set is on the child's "
           "class page", "looked for %r" % title)

    got = p.eval("""(function(){
      var d = document.documentElement;
      return {sw: d.scrollWidth, cw: d.clientWidth,
              bad: /\\bnull\\b|\\bundefined\\b|\\bNaN\\b|Week null/.test(
                     document.body.innerText || ''),
              chars: (document.body.innerText||'').length};})()""")
    record(got["sw"] <= got["cw"] + 1 and not got["bad"],
           "…and the page does not scroll sideways at 390px or say null with "
           "twenty on it",
           "scrollWidth %d ≤ %d, %d characters" % (got["sw"], got["cw"],
                                                   got["chars"]))

    # Open the assignment itself and count what the child is actually given.
    p.set_viewport(390, 900)          # ⊕ MRB-336 — see above; never inherit
    if not goto_ready(p, "%s/student/assignment.html?class=%s&env=test&api=%s"
                      % (base, FX.C_KS3_A, PAGE_API),
                      "document.body && document.body.innerText.length > 100",
                      settle=7.0):
        return record(False, "the student assignment page loads")
    a = p.eval("""(function(){
      var d = document.documentElement;
      return {sw: d.scrollWidth, cw: d.clientWidth,
              chars: (document.body.innerText||'').length,
              bad: /\\bnull\\b|\\bundefined\\b|\\bNaN\\b/.test(
                     document.body.innerText || '')};})()""")
    record(a["sw"] <= a["cw"] + 1 and not a["bad"] and a["chars"] > 100,
           "…and the assignment page draws at 390px with no null",
           "scrollWidth %d ≤ %d, %d characters" % (a["sw"], a["cw"], a["chars"]))


# ════════════════════════════════════════════════════════════════════════
# 11 · ⊕ MRB-336 — DELETE AND EDIT, AND THE SURFACES THAT MUST FORGET
# ════════════════════════════════════════════════════════════════════════
#
# ⚠️ WHY THIS IS HERE AND NOT ONLY IN THE BACKEND'S OWN TESTS.
# `test_set_work_v2.js` drives both routes hard, and this does not repeat it
# for the sake of a second green tick. What the backend cannot see is the half
# that Mide actually asked for — "delete an assignment" is not a route, it is a
# row leaving SEVEN SCREENS. A route that answers 200 while the class page,
# the marking screen, the digest, the chase list and the child's own week all
# go on showing the work is a route that did nothing a teacher would call
# deleting. Only a browser, on the built pages, against a real row, can say so.
#
# So this section splits deliberately:
#   · the API half below proves the CONTRACT the pages are written against —
#     the shapes, the refusals, the idempotency and the audit;
#   · `check_delete_surfaces` and `check_row_controls` prove the CONSEQUENCE.

def api_delete(token, aid):
    return call("DELETE", "/api/teacher/set-work/" + str(aid), token)


def api_patch(token, aid, **fields):
    body = dict(fields)
    # ⚠️ A FRESH `client_ref` PER CALL, for `post_set`'s reason: PATCH is
    # replay-guarded on (actor, target, client_ref) inside a 30-minute window,
    # so a reused ref makes the SECOND edit a no-op that answers 200 and
    # writes nothing — and a check that asserted only the status would pass
    # having proved the opposite of what it says.
    body.setdefault("client_ref", str(uuid.uuid4()))
    return call("PATCH", "/api/teacher/set-work/" + str(aid), token, body)


def set_one(t_teacher, class_id, tier, scope_ref, title, n=4, **kw):
    """Set one piece of work and hand back (id, question_ids). None on failure."""
    st, prev = preview(t_teacher, class_id, tier, kw.get("scope_kind", "topic"),
                       scope_ref, n)
    ids = [q["id"] for q in (prev.get("picked") or [])]
    if len(ids) < n:
        record(False, "%d question(s) to set for %r" % (n, title),
               "got %d" % len(ids))
        return None, []
    st, made = post_set(t_teacher, class_ids=[class_id], tier=tier,
                        scope_ref=scope_ref, question_ids=ids, title=title,
                        **{k: v for k, v in kw.items() if k in
                           ("release_at", "due_at", "scope_kind", "subject")})
    if st != 200 or not (made or {}).get("assignment_ids"):
        record(False, "set %r" % title, "status %s %s" % (st, json.dumps(made)[:200]))
        return None, []
    return made["assignment_ids"][0], ids


# The keys a DELETE answer carries, first call and second. Written out rather
# than compared loosely, because "idempotent" here means the SAME SHAPE and not
# merely another 200 — a second call that dropped `assignment` would break the
# page's toast, which reads the title out of it.
DELETE_KEYS = {"ok", "already_deleted", "assignment", "question_count",
               "submission_count"}
DELETE_ASSIGNMENT_KEYS = {"id", "class_id", "title", "topic", "academic_week",
                          "source", "deleted_at"}


def check_delete(t_teacher, t_pupil, t_admin, scopes):
    print("\n11 · ⊕ MRB-336 · deleting a set")
    got = pick_topic(scopes["ks3"], 1, "medium")
    if not got:
        return record(False, "a KS3 unit to set work on")
    _n, unit, _s = got

    title = TITLE + " · to delete"
    aid, ids = set_one(t_teacher, FX.C_KS3_A, "medium", unit["id"], title, 4)
    if not aid:
        return False

    # The child can see it, or "it disappeared" is not a claim about anything.
    before = week_titles(t_pupil, FX.C_KS3_A)
    record(title in before,
           "the child can see the work BEFORE it is deleted, or the delete "
           "proves nothing", "week_work: %s" % before)

    # ── the delete ────────────────────────────────────────────────────
    st, out = api_delete(t_teacher, aid)
    a = (out or {}).get("assignment") or {}
    record(st == 200 and out.get("ok") is True
           and out.get("already_deleted") is False
           and a.get("id") == aid and a.get("deleted_at")
           and out.get("question_count") == len(ids),
           "delete_answers_the_row — 200, `already_deleted` false, and the "
           "deleted row is described back with its own question count",
           "status %s %s" % (st, json.dumps(out)[:220]))
    record(set(out.keys()) == DELETE_KEYS
           and set(a.keys()) == DELETE_ASSIGNMENT_KEYS,
           "…with exactly the keys the page's toast and refresh are written "
           "against, no more and no fewer",
           "top %s · assignment %s" % (sorted(out.keys()), sorted(a.keys())))

    # ── D4 · IDEMPOTENT, AND THAT MEANS THE SAME SHAPE ────────────────
    #
    # ⚠️ A DOUBLE TAP IS THE ORDINARY CASE, not an edge one: the control is a
    # two-tap arm-then-confirm on a row that disappears underneath the second
    # tap, and a phone that fires the confirm twice is a phone. The second
    # answer has to be a success the page can render, not a 404 it would show
    # as "that assignment is no longer there" about work the teacher HAS just
    # deleted.
    st2, out2 = api_delete(t_teacher, aid)
    a2 = (out2 or {}).get("assignment") or {}
    record(st2 == 200 and out2.get("ok") is True
           and out2.get("already_deleted") is True
           and set(out2.keys()) == DELETE_KEYS
           and set(a2.keys()) == DELETE_ASSIGNMENT_KEYS
           and a2.get("id") == aid and a2.get("title") == title,
           "delete_idempotent — the second call is 200 with the SAME shape "
           "and the same row, flagged `already_deleted`",
           "status %s %s" % (st2, json.dumps(out2)[:220]))
    record(a2.get("deleted_at") == a.get("deleted_at"),
           "…and it does not re-stamp `deleted_at`, so 'when was this "
           "deleted' survives a double tap",
           "first %s · second %s" % (a.get("deleted_at"), a2.get("deleted_at")))

    # ── the child ─────────────────────────────────────────────────────
    after = week_titles(t_pupil, FX.C_KS3_A)
    record(title not in after,
           "delete_leaves_the_childs_week — the work is gone from the child's "
           "week", "week_work: %s" % after)
    st, direct = call("GET", "/api/class/current-assignment?class_id=%s"
                      "&assignment_id=%s" % (FX.C_KS3_A, aid), t_pupil)
    record(st == 404,
           "…and cannot be reached by its id either — 404, not 403, so the "
           "refusal does not disclose that deleted work exists", "status %s" % st)

    # ⚠️ D2 · THE SUBMISSIONS AND THE MARKS ARE KEPT. Soft delete, not a
    # cascade. A teacher tidying a mis-set piece of work must not silently
    # retract points a child has already earned — the row leaves the screens,
    # the history stays in the table.
    st, qrows = FX.api("GET", "/rest/v1/assignment_questions?assignment_id=eq.%s"
                              "&select=id" % aid)
    record(isinstance(qrows, list) and len(qrows) == len(ids),
           "delete_is_soft — the question rows survive the delete; nothing "
           "cascades", "%d row(s) still there"
           % (len(qrows) if isinstance(qrows, list) else -1))

    # ── D4 · AN AUTOMATIC ROW IS NOT A TEACHER'S TO DELETE ────────────
    st, comp = call("GET", "/api/class/current-assignment?class_id=" +
                    FX.C_KS3_A, t_pupil)
    auto_id = ((comp or {}).get("assignment") or {}).get("id")
    if not auto_id:
        record(False, "an automatic assignment exists on 8a/Sc1 to refuse",
               "reason %r" % (comp or {}).get("reason"))
    else:
        st, refused = api_delete(t_teacher, auto_id)
        record(st == 409
               and (refused or {}).get("error") == "auto_assignment_not_editable"
               and ((refused or {}).get("detail") or {}).get("source") == "auto",
               "delete_refuses_an_auto_row — 409 "
               "`auto_assignment_not_editable`, and it names the source so the "
               "page can say WHICH rule it hit",
               "status %s %s" % (st, json.dumps(refused)[:180]))
        # …and the refusal did not delete it anyway.
        st, still = call("GET", "/api/class/current-assignment?class_id=%s"
                         "&assignment_id=%s" % (FX.C_KS3_A, auto_id), t_pupil)
        record(st == 200,
               "…and the automatic assignment is still there afterwards, so "
               "the 409 refused rather than merely reported", "status %s" % st)

    # ── D4 · WHO MAY NOT ──────────────────────────────────────────────
    live_title = TITLE + " · survives the refusals"
    live_id, _live_ids = set_one(t_teacher, FX.C_KS3_A, "medium", unit["id"],
                                 live_title, 3)
    if live_id:
        st, p403 = api_delete(t_pupil, live_id)
        record(st == 403 and (p403 or {}).get("error") == "not_authorised_for_class",
               "delete_refuses_a_pupil — a child enrolled in the class cannot "
               "delete its work", "status %s %s" % (st, json.dumps(p403)[:140]))

        # ⚠️ THE CROSS-SCHOOL CASE, AND THE FIXTURE MAKES IT REAL RATHER THAN
        # SYNTHETIC. `t_admin` is a school_admin — of the OPEN school — and a
        # school admin CAN delete work in their own school. So the refusal
        # below is not "an admin cannot delete", it is "not in THAT school":
        # the row is on the HELD school's class. A crafted uuid from another
        # tenant is exactly this shape, and this proves it on a real account
        # with real standing rather than on a random string.
        held_title = TITLE + " · in the other school"
        held_scope = scope_of(t_teacher, FX.C_KS3_HELD)[1]
        held_pick = pick_topic(held_scope, 1, "medium")
        held_id = None
        if held_pick:
            held_id, _h = set_one(t_teacher, FX.C_KS3_HELD, "medium",
                                  held_pick[1]["id"], held_title, 3,
                                  due_at=DUE.isoformat())
        if held_id:
            st, x403 = api_delete(t_admin, held_id)
            record(st == 403
                   and (x403 or {}).get("error") == "not_authorised_for_class",
                   "delete_refuses_another_school — a real school_admin, with "
                   "real standing in their OWN school, is refused a row in "
                   "another one", "status %s %s" % (st, json.dumps(x403)[:140]))
            st, ok_admin = api_delete(t_admin, live_id)
            record(st == 200 and (ok_admin or {}).get("ok") is True,
                   "…and the same admin CAN delete a row in the school they "
                   "actually administer, or the refusal above would pass by "
                   "the account being powerless",
                   "status %s" % st)

    st, n404 = api_delete(t_teacher, str(uuid.uuid4()))
    record(st == 404 and (n404 or {}).get("error") == "assignment_not_found",
           "delete_unknown_uuid — 404 `assignment_not_found`, which is the "
           "same answer a foreign row gives, so the 404 discloses nothing",
           "status %s %s" % (st, json.dumps(n404)[:140]))
    st, nbad = api_delete(t_teacher, "not-a-uuid")
    record(st == 404 and (nbad or {}).get("error") == "assignment_not_found",
           "…and a string that is not a uuid gets the same 404 rather than a "
           "500 from the database", "status %s %s" % (st, json.dumps(nbad)[:140]))
    return aid


def check_edit(t_teacher, scopes):
    print("\n12 · ⊕ MRB-336 · editing a set, before and after release")
    got = pick_topic(scopes["ks3"], 2, "medium")
    if not got:
        return record(False, "a KS3 unit with two stocked lessons")
    _n, unit, _s = got
    kids = [c["id"] for c in (unit.get("children") or [])
            if (c.get("counts") or {}).get("medium", 0) >= 3]
    if len(kids) < 1:
        return record(False, "a stocked lesson to move the scope to")

    # ── D3 · BEFORE RELEASE, EVERYTHING MOVES ─────────────────────────
    #
    # Nobody can have started, because nobody can see it. So the teacher who
    # picked the wrong topic at eleven at night can fix it rather than delete
    # it and set it again.
    later = (NOW + timedelta(days=3)).isoformat()
    title = TITLE + " · scheduled, then edited"
    aid, ids = set_one(t_teacher, FX.C_KS3_A, "medium", unit["id"], title, 4,
                       release_at=later)
    if not aid:
        return False

    st, prev2 = preview(t_teacher, FX.C_KS3_A, "hard", "subtopic", kids[0], 3)
    new_ids = [q["id"] for q in (prev2.get("picked") or [])]
    if len(new_ids) < 3:
        return record(False, "three replacement questions", "%d" % len(new_ids))
    st, ed = api_patch(t_teacher, aid, tier="hard", scope_kind="subtopic",
                       scope_ref=kids[0], question_ids=new_ids,
                       title=title + " (moved)")
    changed = set((ed or {}).get("changed") or [])
    record(st == 200 and (ed or {}).get("ok") is True
           and {"scope_ref", "scope_kind", "set_tier", "title"} <= changed,
           "edit_before_release_moves_everything — tier, scope kind, scope "
           "and title all change on an unreleased row",
           "status %s changed %s" % (st, sorted(changed)))

    # ⚠️ READ THE QUESTIONS BACK. `changed` is the server's own report; the
    # only proof that the child would meet different questions is the child's
    # own read path.
    st, back = call("GET", "/api/class/current-assignment?class_id=%s"
                    "&assignment_id=%s" % (FX.C_KS3_A, aid), t_teacher)
    got_ids = [q.get("question_ref") for q in (back or {}).get("questions") or []]
    record(got_ids == new_ids,
           "…and the STORED questions are the replacements, in the order "
           "chosen — not merely a `changed` list saying so",
           "wanted %s\n        got    %s" % (new_ids, got_ids))
    record(((back or {}).get("assignment") or {}).get("title")
           == title + " (moved)",
           "…and the new title is stored verbatim",
           ((back or {}).get("assignment") or {}).get("title"))

    # ── D3 · AFTER RELEASE, THE QUESTIONS ARE SEALED ──────────────────
    #
    # ⚠️ THIS IS THE HALF THAT PROTECTS THE CHILD, and it is the reason Edit
    # narrows rather than simply existing. A pupil halfway through eight
    # questions must not have them swapped underneath them: their answers are
    # already filed against ids, and the marking would be against a paper they
    # never sat.
    live_title = TITLE + " · already out"
    live_id, live_ids = set_one(t_teacher, FX.C_KS3_A, "medium", unit["id"],
                                live_title, 4)
    if not live_id:
        return False
    for field, value in (("question_ids", new_ids),
                         ("scope_ref", kids[0]),
                         ("tier", "hard"),
                         ("release_at", (NOW + timedelta(days=2)).isoformat())):
        st, ref = api_patch(t_teacher, live_id, **{field: value})
        ok = (st == 400 and (ref or {}).get("error") == "locked_after_release")
        det = (ref or {}).get("detail") or {}
        record(ok and det.get("fields") == [field]
               and det.get("editable") == ["title", "due_at"],
               "edit_locked_after_release — `%s` is refused 400 "
               "`locked_after_release`, and the refusal NAMES what is still "
               "editable" % field,
               "status %s %s" % (st, json.dumps(ref)[:200]))

    new_due = (NOW + timedelta(days=9)).isoformat()
    st, ok_ed = api_patch(t_teacher, live_id, title=live_title + " (retitled)",
                          due_at=new_due)
    record(st == 200 and (ok_ed or {}).get("ok") is True
           and set((ok_ed or {}).get("changed") or []) == {"title", "due_at"},
           "…while the title and the due date DO change on the same released "
           "row — a teacher can extend a deadline and fix a typo",
           "status %s changed %s" % (st, (ok_ed or {}).get("changed")))
    st, back2 = call("GET", "/api/class/current-assignment?class_id=%s"
                     "&assignment_id=%s" % (FX.C_KS3_A, live_id), t_teacher)
    a2 = (back2 or {}).get("assignment") or {}
    got2 = [q.get("question_ref") for q in (back2 or {}).get("questions") or []]
    record(a2.get("title") == live_title + " (retitled)" and got2 == live_ids,
           "…and the questions are UNTOUCHED by that edit, which is the whole "
           "of the rule",
           "title %r · %d question(s), unchanged %s"
           % (a2.get("title"), len(got2), got2 == live_ids))

    # A deleted row cannot be edited back into existence.
    api_delete(t_teacher, live_id)
    st, dead = api_patch(t_teacher, live_id, title=live_title + " (zombie)")
    record(st == 409 and (dead or {}).get("error") == "assignment_deleted",
           "edit_refuses_a_deleted_row — 409 `assignment_deleted`, so Edit "
           "cannot resurrect what Delete removed",
           "status %s %s" % (st, json.dumps(dead)[:140]))
    return aid, live_id


def check_delete_edit_audited(t_admin, aid, edited_id):
    """⚠️ AN AUDIT ROW IS THE ONLY THING THAT SURVIVES A SOFT DELETE.

    The row itself keeps `deleted_by`, but nothing on any screen shows it, and
    a school asking "who removed Tuesday's homework and when" has one place to
    look. Read as a REAL school_admin under RLS, not on the service key: an
    audit trail only the server can read is not an audit trail anybody has.
    """
    print("\n13 · ⊕ MRB-336 · the audit trail behind Delete and Edit")
    for action, target, want in (("assignment.deleted", aid,
                                  ("question_count", "submission_count")),
                                 ("assignment.edited", edited_id,
                                  ("changed", "from", "to"))):
        if not target:
            record(False, "an id to look %s up by" % action)
            continue
        st, rows = rest("GET", "/rest/v1/audit_log?target_id=eq.%s&action=eq.%s"
                               "&select=action,target_table,payload"
                               "&order=created_at.desc&limit=1"
                        % (target, action), t_admin)
        row = rows[0] if isinstance(rows, list) and rows else {}
        pay = row.get("payload") or {}
        record(row.get("action") == action
               and row.get("target_table") == "assignments"
               and all(k in pay for k in want),
               "%s is audited — the row names the table, the target and %s"
               % (action, " and ".join("`%s`" % k for k in want)),
               "status %s %s" % (st, json.dumps(pay)[:220]))


# ════════════════════════════════════════════════════════════════════════
# 14 · ⊕ MRB-336 §4 — THE CARDS, THE STATUS PILL AND THE ROW CONTROLS
# ════════════════════════════════════════════════════════════════════════
#
# ⚠️ 9a/Sc1 IS THE CLASS FOR THIS AND THE CHOICE IS LOAD-BEARING. It is the
# fixture's `auto_assignments = false` class, so nothing composes on it and
# `glance.cards` holds exactly the rows this check sets — one, then two, then
# three — with no automatic set silently occupying a slot. On 8a/Sc1 the auto
# row sorts LAST (it has no `release_at`) and would take slot B on the
# one-set case, so "two cards" there would be true for a reason that has
# nothing to do with what is being measured.
#
# ⚠️ AND IT HAS EXACTLY ONE PUPIL, which is what makes the chase chips and
# `Remind all N` countable rather than merely present.

CARDS_JS = """(function(){
  var g = document.querySelector('div[style*="minmax(330px,1fr)"]');
  if (!g) { return null; }
  return Array.prototype.map.call(g.children, function (card) {
    var c = card.children;
    var chaseBox = card.querySelector('div[style*="flex-wrap:wrap;gap:6px"]');
    var footer = card.querySelector('div[style*="margin-top:auto"]');
    var more = card.querySelector('[data-mrb-added="live-cards-more"]');
    return {
      eyebrow: ((c[0] && c[0].textContent) || '').trim(),
      title:   ((c[1] && c[1].textContent) || '').trim(),
      count:   ((c[2] && c[2].textContent) || '').trim(),
      chase: chaseBox ? Array.prototype.map.call(
        chaseBox.querySelectorAll('button'),
        function (b) { return (b.textContent || '').trim(); }) : [],
      remind: footer ? ((footer.textContent) || '').trim() : null,
      more: more ? ((more.textContent) || '').trim() : null
    };
  });
})()"""

# ⚠️ THE ROWS ARE FOUND BY THEIR OWN GRID, NOT BY DESCENDING FROM THE ANCHOR.
# `mrb-class-assignments` is on node 307 — the `<h2>Assignments</h2>` header
# row — because that is the FIRST REAL ELEMENT inside `<if klass.hasWork>` and
# the right thing for "+N more" to scroll to. The table itself (node 310) is
# its SIBLING, not its child, so `anchor.querySelectorAll(...)` searches inside
# a heading and returns nothing. It did, silently: eleven checks reported
# `row null` and `0 row(s)` about a table that was on the screen, and two of
# them PASSED vacuously ("the row leaves the table" is trivially true of a
# table you cannot see).
#
# The eight-column grid template is unique to this table on the page, so it
# identifies it without needing a hook the page does not have.
ROW_GRID = '2fr 100px 1fr 1fr 1fr 1fr 1.2fr auto'

ROWS_JS = """(function(){
  var all = document.querySelectorAll('div[style*=%s]');
  var out = [];
  for (var i = 0; i < all.length; i++) {
    var r = all[i];
    if ((r.getAttribute('style') || '').indexOf('cursor:pointer') === -1) {
      continue;                                  /* the header strip */
    }
    var c = r.children;
    out.push({
      title:  ((c[0] && c[0].textContent) || '').trim(),
      status: ((c[1] && c[1].textContent) || '').trim(),
      set:    ((c[2] && c[2].textContent) || '').trim(),
      due:    ((c[3] && c[3].textContent) || '').trim(),
      edit:   !!r.querySelector('[data-mrb-added="set-work-edit"]'),
      del:    !!r.querySelector('[data-mrb-added="set-work-delete"]'),
      cancel: !!r.querySelector('[data-mrb-added="set-work-delete-cancel"]')
    });
  }
  return out;
})()""" % json.dumps(ROW_GRID)


def press_row(p, title, kind):
    """Press one row's Edit / Delete / Cancel, found by its title."""
    return p.eval("""(function(){
      var all = document.querySelectorAll('div[style*=%s]');
      for (var i = 0; i < all.length; i++) {
        var r = all[i];
        if ((r.getAttribute('style')||'').indexOf('cursor:pointer') === -1) {
          continue; }
        if (((r.children[0]||{}).textContent||'').trim() !== %s) { continue; }
        var b = r.querySelector('[data-mrb-added="set-work-%s"]');
        if (!b) { return 'no control'; }
        b.click(); return 'clicked'; }
      return 'no row';})()"""
                  % (json.dumps(ROW_GRID), json.dumps(title), kind))


def ldn(dt):
    """The Set column's own format, computed independently in London.

    ⚠️ COMPUTED HERE RATHER THAN READ BACK. Asserting that the page's London
    string matches the page's own idea of London is a tautology; the point of
    the column is that a teacher in Rainford reads the instant in the time
    their school keeps.
    """
    from zoneinfo import ZoneInfo
    x = dt.astimezone(ZoneInfo("Europe/London"))
    return "%s %d %s %02d:%02d" % (
        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][x.weekday()],
        x.day, ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                "Sep", "Oct", "Nov", "Dec"][x.month - 1], x.hour, x.minute)


def clear_teacher_work(t_teacher, class_id):
    """Every teacher-set row on this class, removed THROUGH THE ROUTE.

    ⚠️ THROUGH THE ROUTE, NOT THROUGH THE SERVICE KEY, on purpose: the checks
    below are about how many cards a class has, so the drive's earlier
    sections must not be able to leave one behind — and doing the tidy-up with
    the very endpoint under test means a broken DELETE fails here loudly
    rather than by making a later count wrong for an unrelated-looking reason.
    """
    st, rows = FX.api("GET", "/rest/v1/assignments?class_id=eq.%s&source=eq."
                             "teacher&deleted_at=is.null&select=id" % class_id)
    n = 0
    for r in (rows if isinstance(rows, list) else []):
        st2, _ = api_delete(t_teacher, r["id"])
        n += 1 if st2 == 200 else 0
    return n


def open_class_page(p, base, class_id, width=390, settle=6.5):
    """⚠️ WAIT FOR THE TABLE ITSELF, NOT FOR 'SOME TEXT'.

    This read `getElementById('mrb-class-assignments') || innerText.length >
    400` and took the second branch every time: the page paints its header,
    roster and glance well before the assignments table exists, and
    `student-runtime.js` `draw()` empties and rebuilds the whole mount host on
    every `setState`, so there is a real window in which the class page is
    fully readable and the table is not on it. Four checks went red reporting
    `row null` about a table that was correct a second later.

    ⚠️ A DISJUNCTION IS THE WRONG SHAPE FOR A READINESS TEST when one branch
    is strictly weaker than the other. It cannot fail — which is the point of
    a readiness test — it can only be satisfied early.
    """
    p.set_viewport(width, 900)
    url = ("%s/teacher/class-detail.html?class=%s&env=test&api=%s"
           % (base, class_id, PAGE_API))
    if not goto_ready(p, url,
                      "!!document.getElementById('mrb-class-assignments')",
                      settle=settle, tries=3):
        return False
    # …and let the rebuild settle, so the node read is not the one about to
    # be thrown away.
    time.sleep(0.8)
    return wait_for(p, "!!document.getElementById('mrb-class-assignments')",
                    tries=40)


def check_cards(p, base, t_teacher, scopes, shots):
    print("\n14 · ⊕ MRB-336 §4.1 · a card is ONE live assignment")
    cid = FX.C_KS3_NOAUTO
    got = pick_topic(scopes["ks3"], 2, "medium")
    if not got:
        return record(False, "a KS3 unit for the card checks")
    _n, unit, _s = got
    kids = [c["id"] for c in (unit.get("children") or [])
            if (c.get("counts") or {}).get("medium", 0) >= 3]
    clear_teacher_work(t_teacher, cid)

    made = []
    # ⚠️ THREE DIFFERENT QUESTION COUNTS, and that is the per-card assertion.
    # The card that MRB-336 replaces summed the week: three sets of 3, 5 and 7
    # read "0 of 15 in" on one card, over a title reading "…· +2 more". If the
    # three cards below all said the same number, this check would pass on the
    # aggregate it exists to have removed.
    for label, n in (("A", 3), ("B", 5), ("C", 7)):
        title = "%s · card %s" % (TITLE, label)
        # ⚠️ RELEASE NOW, AND NOT A COMPUTED PAST INSTANT. The first version
        # of this passed `NOW - 8 minutes` so that "newest release first"
        # would have something to order by — and every set was refused
        # `release_in_past`. `NOW` is the drive's START clock, read once at
        # import (deliberately: half this file is about "before or after the
        # hold" and two clocks would make those checks flap), and by the time
        # section 14 runs the drive has been going for ten minutes. The
        # route's grace is five.
        #
        # Release Now is also the truer test: the server stamps its own
        # instant, the three sets land seconds apart in the order a teacher
        # made them, and slot A is the newest for the same reason it will be
        # in a classroom.
        aid, _ids = set_one(t_teacher, cid, "medium",
                            kids[len(made) % len(kids)] if kids else unit["id"],
                            title, n,
                            scope_kind="subtopic" if kids else "topic")
        time.sleep(1.2)     # distinct release instants, so the order is real
        if not aid:
            return False
        made.append((label, title, n, aid))

        if not open_class_page(p, base, cid):
            return record(False, "the class page loads with %d live set(s)"
                          % len(made))
        cards = p.eval(CARDS_JS)
        if cards is None:
            return record(False, "the live-card grid is on the class page")
        live = [c for c in cards if c["title"].startswith(TITLE)]

        want_n = min(len(made), 2)
        record(len(live) == want_n,
               "cards_are_slots_A_and_B — %d live set(s) on the class, %d "
               "card(s) drawn (never more than two)" % (len(made), want_n),
               "titles %s" % [c["title"] for c in cards])

        # ⚠️ NEWEST RELEASE FIRST. Slot A must be the set the teacher made
        # most recently, not the first one the read happened to return.
        newest = made[-1][1]
        record(live and live[0]["title"] == newest,
               "…and slot A is the NEWEST release, which is the set the "
               "teacher just made",
               "slot A %r · expected %r"
               % (live[0]["title"] if live else None, newest))

        # ⚠️ EACH CARD'S OWN DENOMINATOR. One pupil is enrolled, so every
        # card reads "0 of 1 in" — and the aggregate would have read
        # "0 of %d in" by now. The number that matters is the SECOND one.
        bad_count = [c["count"] for c in live if c["count"] != "0 of 1 in"]
        record(not bad_count,
               "…and every card counts its OWN column — '0 of 1 in' on each, "
               "not the week summed into one fraction",
               "counts %s" % [c["count"] for c in live])

        # No card's TITLE carries the retired aggregate suffix.
        record(not any(" · +" in c["title"] and "more" in c["title"]
                       for c in cards),
               "…and no card title carries the retired '· +N more' suffix — "
               "the overflow is a link, not a lie in the heading",
               "titles %s" % [c["title"] for c in cards])

        if len(made) <= 2:
            record(all(c["more"] is None for c in cards),
                   "…and with %d live set(s) there is no overflow link"
                   % len(made),
                   "more: %s" % [c["more"] for c in cards])
        else:
            rest_n = len(made) - 2
            record(live and live[-1]["more"] == "+%d more" % rest_n,
                   "…and the THIRD set becomes '+%d more' on the LAST card, "
                   "rather than a third card" % rest_n,
                   "more: %s" % [c["more"] for c in cards])

        # Per-card chase and per-card reminder button.
        record(all(len(c["chase"]) == 1 for c in live)
               and all(c["remind"] == "Remind all 1" for c in live),
               "…with its OWN chase chip and its OWN 'Remind all 1' — one "
               "pupil, one chip, per card",
               "chase %s · remind %s"
               % ([c["chase"] for c in live], [c["remind"] for c in live]))

        # ⚠️ THE ONLY SCREENSHOT IN THIS LOOP IS ON THE LAST PASS, AFTER
        # EVERY ASSERTION OF THAT PASS. `ks3_browser.screenshot()` sets the
        # viewport and leaves it set (ks3_browser.py:577, default 1280), and
        # `open_class_page` sets it again at the top of the next pass — but
        # a capture in the middle of a measured pass would be measuring one
        # width and photographing another.
        if shots and len(made) == 3:
            p.screenshot(os.path.join(shots, "MRB336-cards-three-390.png"),
                         width=390)
    # The next check reads this page; put the width back where the shot
    # found it rather than leaving 1280 behind for it.
    p.set_viewport(390, 900)
    time.sleep(0.4)

    # ── ⊕ MRB-336 · '+N more' HAS SOMEWHERE TO GO ─────────────────────
    #
    # ⚠️ THIS ASSERTS THE ANCHOR ELEMENT, NOT THE PRESS, AND THAT IS THE
    # POINT. `MRB_TO_ASSIGNMENTS()` answers `false` both when there is no
    # Assignments section to scroll to (legitimate — a class with no work)
    # and when the anchor simply is not in the DOM (a dead control), and from
    # outside the two are the same `false`. The id was first put on node 306,
    # which is the `<if>` — control flow, not an element — so it was dropped
    # by the runtime with no error, the generated HTML still contained the
    # string, and "+N more" did nothing at all on every class in the school.
    # It is the only route to the third and later live sets of a week.
    anchor = p.eval("""(function(){
      var el = document.getElementById('mrb-class-assignments');
      return {present: !!el, tag: el ? el.tagName : null,
              text: el ? (el.textContent||'').trim().slice(0, 40) : null,
              press: (typeof MRB_TO_ASSIGNMENTS === 'function')
                     ? MRB_TO_ASSIGNMENTS() : 'no helper'};})()""")
    record(anchor["present"] and anchor["press"] is True,
           "class_page_anchor — the Assignments section carries the id "
           "'+N more' scrolls to, and the press finds it",
           json.dumps(anchor))
    return made


def check_remind_names_its_own_card(p, base, made):
    """RISKS C4 — Remind on card A reminds about set A.

    ⚠️ THE ONLY PLACE THIS IS VISIBLE IS THE ROW IT WRITES. The button says
    'Remind all 1' on both cards, the toast says the same sentence on both,
    and the aggregate version — which nudged about every set in the week at
    once — was indistinguishable from the correct one on screen. The
    `assignment_id` on the `student_notifications` row is the whole claim.
    """
    print("\n   ⊕ MRB-336 · the reminder names the card it was pressed on")
    if not made or len(made) < 2:
        return record(False, "two cards to tell apart")
    cid = FX.C_KS3_NOAUTO
    FX.api("DELETE", "/rest/v1/student_notifications?class_id=eq." + cid)

    cards = p.eval(CARDS_JS) or []
    live = [c for c in cards if c["title"].startswith(TITLE)]
    if len(live) < 2:
        return record(False, "two live cards on the page",
                      "%d" % len(live))
    slot_a_title = live[0]["title"]
    slot_b_title = live[1]["title"]
    by_title = {t: aid for _l, t, _n, aid in made}

    # Press slot B's button, NOT slot A's. Pressing the first card would pass
    # against an implementation that always reminded about the first.
    pressed = p.eval("""(function(){
      var g = document.querySelector('div[style*="minmax(330px,1fr)"]');
      var cards = Array.prototype.filter.call(g.children, function (c) {
        var t = c.children[1];
        return t && (t.textContent || '').indexOf(%s) === 0; });
      var card = cards[1];
      if (!card) { return 'no second card'; }
      var f = card.querySelector('div[style*="margin-top:auto"] button');
      if (!f) { return 'no remind button'; }
      f.click();
      return 'clicked';})()""" % json.dumps(TITLE))
    if pressed != "clicked":
        return record(False, "the second card's Remind button is pressable",
                      pressed)
    time.sleep(3.0)

    st, rows = FX.api("GET", "/rest/v1/student_notifications?class_id=eq.%s"
                             "&select=assignment_id,student_id" % cid)
    got = sorted({r.get("assignment_id") for r in (rows or [])})
    want_b = by_title.get(slot_b_title)
    want_a = by_title.get(slot_a_title)
    record(got == [want_b],
           "remind_names_its_own_assignment — pressing slot B's 'Remind all' "
           "writes ONE reminder, and it names slot B's assignment",
           "wrote %s · slot B %s · slot A %s" % (got, want_b, want_a))
    record(want_a not in got,
           "…and specifically NOT slot A's, which is what the week-wide "
           "reminder used to do", "slot A id %s" % want_a)
    record(p.eval("(function(){var g=document.querySelector("
                  "'div[style*=\"minmax(330px,1fr)\"]');"
                  "return (g.textContent||'').indexOf('Reminded today')!==-1;})()"),
           "…and that card, and the teacher's screen, says 'Reminded today'")
    FX.api("DELETE", "/rest/v1/student_notifications?class_id=eq." + cid)


def check_card_counts_are_per_card(p, base, made):
    """C4's other half — the DENOMINATOR and the CHASE are per card too.

    ⚠️ WITHOUT THIS THE COUNT ASSERTION IN `check_cards` IS WEAK AND I WOULD
    RATHER SAY SO THAN LET IT LOOK STRONG. 9a/Sc1 has one pupil and nobody has
    submitted, so every card reads `0 of 1 in` — which is exactly what a
    surviving AGGREGATE card would read too. Three cards all saying the same
    true thing cannot distinguish "each card counted its own column" from
    "one number was copied onto three cards".
    """
    print("\n   ⊕ MRB-336 · the count and the chase are per card, not per week")
    if not made or len(made) < 2:
        return record(False, "two cards to tell apart")
    cards = p.eval(CARDS_JS) or []
    live = [c for c in cards if c["title"].startswith(TITLE)]
    if len(live) < 2:
        return record(False, "two live cards on the page", "%d" % len(live))
    by_title = {t: aid for _l, t, _n, aid in made}
    a_title, b_title = live[0]["title"], live[1]["title"]
    a_id = by_title.get(a_title)

    # ⚠️ THE SUBMISSION IS BUILT BY THE FIXTURE, NOT SUBMITTED BY A CHILD.
    # Driving a real pupil through a real assignment is `student_api_drive`'s
    # job and would take a browser, a sign-in and twenty answers to establish
    # one number here. `FX` is the service key and building the world is
    # exactly what it is for; nothing in the CHECK runs on it.
    pupil = FX.find_user(FX.PUPIL_EMAIL)
    sub_id = str(uuid.uuid4())
    st, _ = FX.api("POST", "/rest/v1/assignment_submissions",
                   {"id": sub_id, "assignment_id": a_id, "student_id": pupil,
                    "score": 3, "max_score": 3, "attempts": 1,
                    "submitted_at": datetime.now(timezone.utc).isoformat()})
    if st not in (200, 201, 204):
        return record(False, "a submission can be planted on slot A",
                      "status %s" % st)
    try:
        if not open_class_page(p, base, FX.C_KS3_NOAUTO):
            return record(False, "the class page reloads with a submission on it")
        cards = p.eval(CARDS_JS) or []
        live = [c for c in cards if c["title"].startswith(TITLE)]
        got = {c["title"]: c for c in live}
        a, b = got.get(a_title), got.get(b_title)
        record(a and b and a["count"] == "1 of 1 in" and b["count"] == "0 of 1 in",
               "card_counts_are_per_card — ONE pupil submits ONE of the two "
               "live sets, and the two cards now read DIFFERENT numbers; the "
               "aggregate card would have read '1 of 2 in' on both",
               "%r → %r · %r → %r"
               % (a_title[-12:], (a or {}).get("count"),
                  b_title[-12:], (b or {}).get("count")))
        record(a and b and a["chase"] == [] and b["chase"] == ["Pip T"],
               "…and the chase list follows the same column — the child who "
               "has done slot A is chased for slot B and not for slot A",
               "slot A chase %s · slot B chase %s"
               % ((a or {}).get("chase"), (b or {}).get("chase")))
        record(a and a["remind"] in (None, ""),
               "…and slot A offers no 'Remind all' at all, because there is "
               "nobody left on it to remind",
               "slot A footer %r" % (a or {}).get("remind"))
    finally:
        # ⚠️ REMOVED HERE RATHER THAN LEFT TO TEARDOWN. `--keep` exists so a
        # run can be inspected, and a planted submission left standing would
        # make the NEXT run's `0 of 1 in` assertions fail for a reason that
        # has nothing to do with the code.
        FX.api("DELETE", "/rest/v1/assignment_submissions?id=eq." + sub_id)


def check_status_and_set_column(p, base, t_teacher, scopes, shots):
    """§4.2 — Scheduled / Open / Closed, and the Set column in London.

    ⚠️ THIS IS THE SCREENSHOT MIDE SENT. A row released on the 14th and shown
    as OPEN on the 8th is the untruth the whole ticket started from: the table
    was grouping by DUE date and calling everything not yet due 'Open', so
    work no child could see was reported as work every child had.
    """
    print("\n15 · ⊕ MRB-336 §4.2 · Scheduled / Open / Closed, and the Set column")
    cid = FX.C_KS3_NOAUTO
    got = pick_topic(scopes["ks3"], 1, "medium")
    if not got:
        return record(False, "a KS3 unit for the status checks")
    _n, unit, _s = got
    clear_teacher_work(t_teacher, cid)

    # ── SCHEDULED, at a London boundary that is a DIFFERENT DAY in UTC ─
    #
    # ⚠️ 23:30 UTC IS THE NEXT DAY IN LONDON THROUGH BRITISH SUMMER TIME, and
    # that is the whole of this assertion. A Set column rendered in UTC — or
    # in whatever zone the teacher's laptop happens to be in — reads
    # "Mon 14 Sep 23:30" for an instant a Rainford teacher would call half
    # past midnight on Tuesday the 15th. One day out, on the column whose
    # only job is to say when the work appears.
    boundary = (NOW + timedelta(days=10)).replace(
        hour=23, minute=30, second=0, microsecond=0)
    sched_title = TITLE + " · scheduled"
    sched_id, _s1 = set_one(t_teacher, cid, "medium", unit["id"], sched_title, 3,
                            release_at=boundary.isoformat(),
                            due_at=(boundary + timedelta(days=5)).isoformat())

    open_title = TITLE + " · open now"
    open_id, _s2 = set_one(t_teacher, cid, "medium", unit["id"], open_title, 3)

    # ── CLOSED ────────────────────────────────────────────────────────
    #
    # ⚠️ AGED BY THE FIXTURE, NOT BY THE ROUTE, and the reason is that the
    # route is RIGHT to refuse: `release_in_past` and `bad_due_at` exist so a
    # teacher cannot set work that arrives already overdue. There is no
    # request that legitimately creates a closed row, so the world is built
    # rather than requested — the same posture `FX` takes everywhere else.
    closed_title = TITLE + " · closed"
    closed_id, _s3 = set_one(t_teacher, cid, "medium", unit["id"], closed_title, 3)
    if closed_id:
        FX.api("PATCH", "/rest/v1/assignments?id=eq." + closed_id,
               {"release_at": (NOW - timedelta(days=6)).isoformat(),
                "due_at": (NOW - timedelta(days=1)).isoformat()})

    if not open_class_page(p, base, cid):
        return record(False, "the class page loads for the status checks")
    rows = p.eval(ROWS_JS) or []
    by = {r["title"]: r for r in rows}

    for title, want, why in (
            (sched_title, "Scheduled",
             "released in the FUTURE — no child can see it, so it is not Open"),
            (open_title, "Open",
             "released and not yet due"),
            (closed_title, "Closed",
             "past its due date — 'Marked' was a claim about the teacher, not "
             "about the work")):
        r = by.get(title)
        record(r is not None and r["status"] == want,
               "status_is_release_and_due — %r reads %s (%s)"
               % (title.replace(TITLE + " · ", ""), want, why),
               "row %s" % json.dumps(r))

    r = by.get(sched_title)
    want_set = ldn(boundary)
    record(r is not None and r["set"] == want_set,
           "set_column_is_london — the Set column reads %r for an instant "
           "that is the day BEFORE in UTC" % want_set,
           "column %r · the UTC instant is %s"
           % ((r or {}).get("set"), boundary.isoformat()))

    # ⚠️ AND THE CARDS DISAGREE WITH THE TABLE ON PURPOSE. A Scheduled row is
    # in the table (it IS set) and is NOT a card (nobody has been shown it).
    # C5 — a card for scheduled work would be the same untruth one screen up.
    cards = p.eval(CARDS_JS) or []
    titles = [c["title"] for c in cards]
    record(open_title in titles and sched_title not in titles
           and closed_title not in titles,
           "scheduled_and_closed_are_not_cards — only the OPEN set has a "
           "card; the scheduled one is in the table and the closed one "
           "belongs to reteach", "cards %s" % titles)
    # ⚠️ THE SCREENSHOT IS LAST, AND THAT IS NOT TIDINESS.
    # `ks3_browser.screenshot()` sets the viewport as a side effect
    # (ks3_browser.py:577) and leaves it set, so a capture taken BEFORE a
    # read is a capture that changes the page the read then measures. Every
    # screenshot in this section goes after the last assertion that depends
    # on the width, and every one names its width explicitly.
    if shots:
        p.screenshot(os.path.join(shots, "MRB336-status-390.png"), width=390)
    return sched_id, open_id, closed_id


def check_row_controls(p, base, t_teacher, scopes, shots, ids):
    """§6 — Edit, Delete, the two-tap arm, and the toast."""
    print("\n16 · ⊕ MRB-336 §6 · the row controls")
    cid = FX.C_KS3_NOAUTO
    if not open_class_page(p, base, cid):
        return record(False, "the class page loads for the row controls")
    rows = p.eval(ROWS_JS) or []
    mine = [r for r in rows if r["title"].startswith(TITLE)]
    record(mine and all(r["edit"] and r["del"] for r in mine),
           "row_controls_present — every teacher-set row carries Edit and "
           "Delete", "%d row(s): %s"
           % (len(mine), [(r["title"][-16:], r["edit"], r["del"]) for r in mine]))
    record(all(not r["cancel"] for r in rows),
           "…and none is armed until it is pressed, so Cancel is nowhere yet")

    target = TITLE + " · closed"

    def press(kind):
        return press_row(p, target, kind)

    # ── THE TWO-TAP ARM. One tap must not delete. ─────────────────────
    #
    # ⚠️ THE ROW IS ITSELF A LINK — tapping it opens the marking screen — so
    # a Delete that fired on one press would sit a few pixels from a control a
    # teacher taps all day, with no dialogue in between. The arm IS the
    # confirmation, and `Cancel` appearing is how a teacher knows they are one
    # tap from losing the work.
    record(press("delete") == "clicked", "the first Delete tap lands")
    time.sleep(0.6)
    armed = [r for r in (p.eval(ROWS_JS) or []) if r["title"] == target]
    record(armed and armed[0]["cancel"] and not armed[0]["edit"],
           "delete_arms_before_it_deletes — one tap shows Cancel and hides "
           "Edit; it does not delete", "row %s" % json.dumps(armed[:1]))
    st, alive = FX.api("GET", "/rest/v1/assignments?title=eq.%s&deleted_at=is."
                              "null&select=id" % urllib.parse.quote(target))
    record(isinstance(alive, list) and len(alive) == 1,
           "…and the row is still there in the database after that first tap",
           "%d live row(s)" % (len(alive) if isinstance(alive, list) else -1))

    record(press("delete-cancel") == "clicked", "Cancel is pressable")
    time.sleep(0.5)
    back = [r for r in (p.eval(ROWS_JS) or []) if r["title"] == target]
    record(back and back[0]["edit"] and not back[0]["cancel"],
           "…and Cancel disarms it — Edit is back and Cancel is gone")

    # ── AND NOW, FOR REAL ─────────────────────────────────────────────
    press("delete")
    time.sleep(0.5)
    press("delete")
    time.sleep(3.5)
    after = p.eval(ROWS_JS) or []
    record(target not in [r["title"] for r in after],
           "delete_removes_the_row — the second tap deletes, and the row "
           "leaves the table WITHOUT a reload",
           "rows now: %s" % [r["title"][-18:] for r in after])
    st, gone = FX.api("GET", "/rest/v1/assignments?title=eq.%s&deleted_at=is."
                             "null&select=id" % urllib.parse.quote(target))
    record(isinstance(gone, list) and not gone,
           "…and it is soft-deleted in the database, not merely hidden",
           "%d live row(s)" % (len(gone) if isinstance(gone, list) else -1))
    if shots:
        p.screenshot(os.path.join(shots, "MRB336-after-delete-390.png"),
                     width=390)


def check_delete_surfaces(p, base, t_teacher, scopes):
    """A deleted set leaves EVERY screen, and that is what deleting means.

    ⚠️ RISKS A1 INVERTED THE DANGER HERE. `assignments.deleted_at` already
    existed and thirty-odd consumers already filtered it, so the risk is not
    "somebody forgot to exclude deleted rows" — it is that a reader assumes
    every consumer needs editing and edits one that was already right. So this
    check is a SWEEP rather than a list: it deletes one row and then reads
    every teacher screen and both student pages looking for its title.
    """
    print("\n17 · ⊕ MRB-336 · a deleted set leaves every screen")
    cid = FX.C_KS3_A
    got = pick_topic(scopes["ks3"], 1, "medium")
    if not got:
        return record(False, "a KS3 unit for the surface sweep")
    _n, unit, _s = got
    title = TITLE + " · vanishes everywhere"
    aid, _ids = set_one(t_teacher, cid, "medium", unit["id"], title, 4)
    if not aid:
        return False

    pages = [("class-detail", "/teacher/class-detail.html?class=%s"),
             ("assignment (marking)", "/teacher/assignment.html?class=%s"),
             ("digest", "/teacher/digest.html?class=%s"),
             ("insights", "/teacher/insights.html?class=%s")]

    def sweep(when):
        seen = {}
        for label, path in pages:
            p.set_viewport(390, 900)
            if not goto_ready(p, base + (path % cid) + "&env=test&api=" + PAGE_API,
                              "document.body && document.body.innerText.length > 300",
                              settle=6.5, tries=2):
                seen[label] = None
                continue
            seen[label] = title in (p.eval("document.body.innerText") or "")
        return seen

    before = sweep("before")
    record(any(v is True for v in before.values()),
           "the set is ON the teacher's screens before it is deleted, or the "
           "sweep below proves nothing", json.dumps(before))

    st, out = api_delete(t_teacher, aid)
    record(st == 200, "…and it is deleted", "status %s" % st)

    after = sweep("after")
    still = sorted(k for k, v in after.items() if v is True)
    record(not still,
           "delete_leaves_every_teacher_screen — the title is on none of "
           "class-detail, the marking screen, the digest or insights",
           json.dumps(after) if not still else "STILL SHOWING ON: %s" % still)
    # ⚠️ `None` MEANS A PAGE DID NOT LOAD, WHICH IS NOT A PASS. A page that
    # 404s or CORS-fails renders nothing, contains no title, and would satisfy
    # "the title is absent" while proving the opposite of what is claimed.
    dead = sorted(k for k, v in after.items() if v is None)
    record(not dead,
           "…and every one of those four pages actually LOADED, so 'absent' "
           "means absent rather than blank",
           "loaded: %s" % sorted(k for k, v in after.items() if v is not None)
           if not dead else "DID NOT LOAD: %s" % dead)
    return aid, title


def check_delete_student_surfaces(p, base, title):
    """The child's side of the same delete. One browser, the pupil's."""
    print("\n   …and the child's pages forget it too")
    if not title:
        return
    for label, path in (("student class", "/student/class.html?class=%s"),
                        ("student assignment", "/student/assignment.html?class=%s")):
        p.set_viewport(390, 900)
        ok = goto_ready(p, base + (path % FX.C_KS3_A) + "&env=test&api=" + PAGE_API,
                        "document.body && document.body.innerText.length > 200",
                        settle=7.0, tries=2)
        body = (p.eval("document.body.innerText") or "") if ok else ""
        record(ok and title not in body,
               "delete_leaves_the_childs_%s — the deleted set is not on it"
               % label.replace(" ", "_"),
               "%d characters, title absent" % len(body) if ok
               else "the page did not load, so absence proves nothing")


def check_wide(p, base, class_ids):
    """1280px. ⚠️ A DESKTOP WIDTH IS NOT 'THE PHONE BUT ROOMIER'.

    The Assignments table gained an EIGHTH column today and the card grid is
    `auto-fit minmax(330px, 1fr)` — at 390 it is one column and every failure
    mode of a wide grid is invisible. Both widths, or neither is measured.
    """
    print("\n18 · ⊕ MRB-336 · the teacher's screens at 1280px")
    for label, cid in class_ids:
        p.set_viewport(1280, 900)
        if not goto_ready(p, "%s/teacher/class-detail.html?class=%s&env=test&api=%s"
                          % (base, cid, PAGE_API),
                          "document.body && document.body.innerText.length > 300",
                          settle=6.5, tries=2):
            record(False, "class-detail loads at 1280px for %s" % label)
            continue
        got = p.eval("""(function(){
          var d = document.documentElement;
          var box = document.getElementById('mrb-class-assignments');
          var g = document.querySelector('div[style*="minmax(330px,1fr)"]');
          return {sw: d.scrollWidth, cw: d.clientWidth, iw: window.innerWidth,
                  boxOver: box ? (box.scrollWidth - box.clientWidth) : 0,
                  cards: g ? g.children.length : -1,
                  bad: /\\bnull\\b|\\bundefined\\b|\\bNaN\\b/.test(
                         document.body.innerText || '')};})()""")
        # ⚠️ ⊕ MRB-336 — THE WIDTH IS ASSERTED, NOT ASSUMED. A viewport
        # override can be undone by something else in the run —
        # `ks3_browser.screenshot()` resets it as a side effect
        # (ks3_browser.py:572-577, `width` defaulting to 1280) — and a
        # sideways-scroll check taken at the wrong width is the worst kind of
        # green: a desktop has the room, so it passes, and it passes hardest
        # on exactly the pages a phone cannot fit. `innerWidth` is the page's
        # own report of the width it was laid out at.
        record(got["iw"] == 1280,
               "…measured at 1280 — the page says so itself, so this is not a "
               "phone measurement wearing a desktop label",
               "window.innerWidth %s" % got["iw"])
        record(got["sw"] <= got["cw"] + 1 and not got["bad"],
               "wide_no_sideways — class-detail for %s does not scroll "
               "sideways at 1280px and says no null" % label,
               json.dumps(got))
        record(got["boxOver"] <= 1,
               "…and the eight-column Assignments table fits its own box "
               "rather than overflowing it",
               "%dpx over" % got["boxOver"])


def check_edit_sheet(p, base, shots):
    """§6 rendered — Edit opens the sheet on the row, and it NARROWS.

    ⚠️ THE API HALF PROVES THE SERVER REFUSES; THIS PROVES THE TEACHER IS NOT
    OFFERED IT. Those are different failures and only one of them is rude. A
    sheet that let a teacher restyle the questions on live work, take twenty
    seconds over it and then answer `locked_after_release` has told them the
    truth at the worst possible moment.
    """
    print("\n19 · ⊕ MRB-336 §6 · Edit, in the sheet")
    cid = FX.C_KS3_NOAUTO
    if not open_class_page(p, base, cid):
        return record(False, "the class page loads for the Edit check")
    target = TITLE + " · open now"
    clicked = press_row(p, target, "edit")
    if clicked != "clicked":
        return record(False, "Edit is pressable on the released row", clicked)
    if not wait_for(p, "!!document.querySelector('[data-sw=\"overlay\"]')"
                       "&& !document.querySelector('[data-sw=\"overlay\"]')"
                       ".hidden"):
        return record(False, "the sheet opens on Edit")
    time.sleep(1.2)

    st = p.eval("""(function(){
      var o = document.querySelector('[data-sw="overlay"]');
      var q = function(s){return o.querySelector(s);};
      var vis = function(n){return !!n && !n.hidden
        && getComputedStyle(n).display !== 'none';};
      return {edit: o.getAttribute('data-sw-edit') || '',
              primary: (q('[data-sw="primary"]')||{}).textContent || '',
              roTier: (q('[data-sw="ro-tier"]')||{}).textContent || null,
              roScope: (q('[data-sw="ro-scope"]')||{}).textContent || null,
              relChips: vis(q('[data-sw="release-chips"]')),
              qlistRo: !!q('[data-sw="qlist"].is-ro'),
              swaps: o.querySelectorAll('[data-sw="qlist"].is-ro .sw-swap')
                      .length,
              swapVisible: (function(){
                var s = o.querySelector('[data-sw="qlist"].is-ro .sw-swap');
                return s ? getComputedStyle(s).display !== 'none' : false;})(),
              title: (q('[data-sw="title"]')||{}).value || ''};})()""")
    record(bool(st["edit"]) and st["title"] == target,
           "edit_opens_on_the_row — the overlay is stamped with the "
           "assignment id and the title field holds THAT row's title",
           json.dumps({k: st[k] for k in ("edit", "title")}))
    record(st["primary"] == "Save",
           "…and the primary says Save, not Set — the verb for a row that "
           "already exists", repr(st["primary"]))
    record(st["roTier"] and st["roScope"],
           "edit_after_release_narrows — the tier and the topic are shown as "
           "FACTS rather than as controls",
           "tier %r · topic %r" % (st["roTier"], st["roScope"]))
    record(st["relChips"] is False,
           "…and the release chips are gone: an instant that has already "
           "passed is not a choice any more")
    record(st["qlistRo"] and st["swapVisible"] is False,
           "…and Swap is not offered on any question, so the pupil halfway "
           "through cannot have one changed underneath them",
           "%d swap control(s), none visible" % st["swaps"])
    # The title and the due date DO still move, or Edit would be a viewer.
    p.eval("""(function(){var t=document.querySelector('[data-sw="title"]');
        t.value=%s; t.dispatchEvent(new Event('input',{bubbles:true}));})()"""
           % json.dumps(target + " (renamed)"))
    time.sleep(0.3)
    record(p.eval("!document.querySelector('[data-sw=\"primary\"]').disabled"),
           "…while the title field is still live and Save is pressable, so "
           "the narrowing is a narrowing and not a lock")
    if shots:                          # ⊕ MRB-336 — last, and with a width
        p.screenshot(os.path.join(shots, "MRB336-edit-locked-390.png"),
                     width=390)
    p.eval("window.MRBSetWork.close()")


if __name__ == "__main__":
    sys.exit(main())
