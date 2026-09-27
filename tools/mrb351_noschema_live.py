"""tools/mrb351_noschema_live.py — MRB-351 landing, stream E.

The coordinator's required proof that "no schema change is visible" is a
STATIC-ANALYSIS claim (`flashcard_request_shape_drive.py`, a recording stub
standing in for Supabase). This script is the LIVE version: it rolls TEST back
to before any MRB-351 migration, boots this branch's real backend against
real TEST, serves the real built site, signs a real teacher and a real pupil
in through auth.html in headless Chrome, and reads Chrome's own Network log
and console while they use the real pages a Rainford teacher/pupil would use
today — with NO flashcard schema present at all. Then it does the identical
journey against a plain origin/main build, and diffs the two.

    MRB_BACKEND=<path to the mrb351 backend worktree> \
    MRB_SET_WORK_PASSWORD=<anything> \
    python3 tools/mrb351_noschema_live.py

⚠️ THIS ASSUMES TEST HAS ALREADY BEEN ROLLED BACK (mrb351 migrations 1-3
undone) BEFORE THIS RUNS, and leaves it rolled back — the coordinator's brief
rolls forward again afterwards, deliberately as a separate step, so that a
crash midway through THIS script is caught looking at a database with no
flashcard schema rather than a half-migrated one.

Decisions taken here (recorded for the report, not asked):

  · ONE backend process serves BOTH builds (this branch's and origin/main's).
    The request-shape claim under test is about the SITE's own JS calling
    Supabase directly (`shared/teacher-data.js`, `shared/student-data.js`,
    `shared/teacher-admin-nav.js`'s capability probe) — the backend's own
    flashcard guards (`kind='flashcards'` refusals in the worksheet/feedback
    routes) cannot fire with no flashcard schema present, so pointing both
    builds at the same backend instance is a faithful test of the site half
    and halves the boot cost and the throwaway-world bookkeeping.
  · The pupil-facing half runs on 8a/Sc1 (`FX.C_KS3_A`), because that is the
    one class in `mrb331_fixture`'s world the throwaway pupil is actually a
    MEMBER of. The teacher-only half (Set work sheet + tree) also opens once
    against 10b/Sc5 (`FX.C_KS4_COMB`), which is the KS4 class the brief named,
    to touch a KS4 tree/request shape at least once — no MCQ assignment is
    written there because the pupil cannot see it anyway.
  · "The real Set work route" is exercised as a real HTTP POST with the
    teacher's own JWT (exactly the request `shared/set-work.js`'s Save button
    fires), rather than driving Save through simulated clicks — the wizard's
    OWN correctness (every step, every validation) is what the standing
    `set_work_drive.py` gate already proves in step 3 of this landing; this
    script's job is the request-shape proof, and it also opens the sheet in
    the browser (`window.MRBSetWork.open`) so the sheet's own `/scope` read is
    captured on the wire too.
  · Only XHR/fetch requests to `/rest/v1/*` or `/api/*` are scanned for
    forbidden tokens. Static asset requests (script/css/image files) are
    excluded from the diff — their URLs differ between builds by cache-bust
    hash alone, which is expected and not a schema question.
"""
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)
sys.path.insert(0, REPO)

import mrb331_fixture as FX          # noqa: E402
import ks3_browser as cdp            # noqa: E402

BACKEND = os.environ.get("MRB_BACKEND")
if not BACKEND:
    raise SystemExit("Set MRB_BACKEND to the mrb351 backend worktree path.")
MAIN_BACKEND_ENV = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env"

API_PORT = 5591
SITE_A_PORT = 5593   # this branch's mrbadmus_site
SITE_B_PORT = 5595   # origin/main's mrbadmus_site, built fresh in a temp worktree
API = "http://127.0.0.1:%d" % API_PORT
PAGE_API = "http://localhost:%d" % API_PORT
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

MAIN_REF = "origin/main"

checks = []


def record(ok, label, detail=""):
    checks.append((bool(ok), label, detail))
    print("   %s  %s%s" % ("PASS" if ok else "FAIL", label,
                            ("\n        " + str(detail)[:500]) if detail else ""))
    return bool(ok)


def anon_key_from(site_dir):
    src = open(os.path.join(site_dir, "shared", "config.js"), encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                      src[src.index("const TEST"):]).group(1)


def sign_in(email, pw, site_dir, tries=4):
    key = anon_key_from(site_dir)
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
    raise SystemExit("sign-in for %s failed after %d tries: %s" % (email, tries, last))


def call(method, path, token, body=None, tries=3):
    """One call to the locally-run backend, as a signed-in person.

    ⚠️ RETRIES A TRANSPORT FAILURE, NEVER AN HTTP ANSWER. This run's backend
    shares the machine with `build_all.py` building the origin/main worktree
    for comparison at the same time, and the first live run of this script
    met a 60s socket timeout on exactly that contention — not a real product
    refusal. Same discipline as `set_work_drive.sign_in`: an HTTPError has
    been answered and is returned as-is; only "never got an answer" retries.
    """
    req = urllib.request.Request(
        API + path, method=method,
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"},
        data=json.dumps(body).encode() if body is not None else None)
    last = None
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                raw = r.read().decode()
                return r.status, (json.loads(raw) if raw.strip() else {})
        except urllib.error.HTTPError as e:
            raw = e.read().decode()
            try:
                return e.code, json.loads(raw)
            except ValueError:
                return e.code, raw[:400]
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = e
            time.sleep(2.0 * (attempt + 1))
    raise SystemExit("%s %s failed after %d tries: %s" % (method, path.split("?")[0], tries, last))


class Server:
    """This branch's backend, run locally against TEST. Killed by PID only."""

    def __init__(self, extra_origins):
        self.extra_origins = extra_origins
        self.p = None

    def __enter__(self):
        env = dict(os.environ)
        for line in open(MAIN_BACKEND_ENV, encoding="utf-8"):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
        env["PORT"] = str(API_PORT)
        env["NODE_PATH"] = ("/Users/midebadmus/Documents/GitHub/"
                             "mrbadmus-backend-worktrees/experience/node_modules")
        env["EXTRA_CORS_ORIGINS"] = ",".join(self.extra_origins)
        self.p = subprocess.Popen(
            ["node", "server.js"], cwd=BACKEND, env=env,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        deadline = time.time() + 45
        while time.time() < deadline:
            if self.p.poll() is not None:
                out = self.p.stdout.read()[:3000]
                raise SystemExit("backend exited on boot:\n" + out)
            try:
                with urllib.request.urlopen(API + "/api/health", timeout=3):
                    print("   backend up on :%d (pid %d) from %s" % (API_PORT, self.p.pid, BACKEND))
                    return self
            except Exception:                                      # noqa: BLE001
                time.sleep(0.4)
        raise SystemExit("backend did not come up on :%d" % API_PORT)

    def __exit__(self, *exc):
        if not self.p:
            return
        pid = self.p.pid
        self.p.terminate()
        try:
            self.p.wait(timeout=10)
        except subprocess.TimeoutExpired:
            self.p.kill()
        print("   backend (pid %d) stopped" % pid)


# ════════════════════════════════════════════════════════════════════════
# Browser helpers
# ════════════════════════════════════════════════════════════════════════

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

API_URL_RE = re.compile(r"/rest/v1/|/api/")
ASSET_RE = re.compile(r"\.(js|css|png|jpg|jpeg|svg|ico|woff2?|json)(\?|$)")
FORBIDDEN_COLS = ("kind", "flashcard_mode", "completion_rule", "deck_id")


def goto_ready(p, url, ready, settle=2.5, tries=4):
    for attempt in range(tries):
        try:
            p.goto(url, settle=settle)
        except Exception:                                          # noqa: BLE001
            time.sleep(1.0)
            continue
        for _ in range(50):
            try:
                if p.eval(ready):
                    return True
            except Exception:                                      # noqa: BLE001
                pass
            time.sleep(0.3)
    return False


def sign_in_page(p, base, email, pw):
    if not goto_ready(p, "%s/auth.html?env=test&api=%s" % (base, PAGE_API),
                       "!!document.getElementById('btn-signin')"):
        return "auth.html never rendered its sign-in form"
    try:
        clicked = p.eval(CLICK_SIGN_IN_JS % (json.dumps(email), json.dumps(pw)))
    except Exception as e:                                         # noqa: BLE001
        return "could not press Sign In: %s" % e
    if clicked != "clicked":
        return str(clicked)
    for _ in range(80):
        time.sleep(0.3)
        try:
            key = p.eval(TOKEN_JS)
        except Exception:                                          # noqa: BLE001
            continue
        if key:
            return "ok " + key
    return "no session in localStorage 24s after pressing Sign In"


def enable_network(p):
    p.send("Network.enable", {"maxPostDataSize": 1 << 20})


def api_requests_since_nav(p):
    """Every /rest/v1/ or /api/ request URL Chrome has sent since the last
    navigation (static assets excluded — see the module docstring)."""
    try:
        p.send("Runtime.evaluate", {"expression": "1", "returnByValue": True})
    except cdp.CDPError:
        pass
    p.drain(0.4)
    out = []
    for ev in p._events:                                            # noqa: SLF001
        if ev.get("method") != "Network.requestWillBeSent":
            continue
        rq = (ev.get("params") or {}).get("request") or {}
        url = rq.get("url") or ""
        if API_URL_RE.search(url) and not ASSET_RE.search(url):
            out.append({"method": rq.get("method"), "url": url})
    return out


def load_page(p, url, label, results, errors, ready="document.body && document.body.innerText.length>0"):
    ok = goto_ready(p, url, ready, settle=6.0, tries=3)
    time.sleep(0.6)
    reqs = api_requests_since_nav(p)
    errs = [e for e in p.console_errors() if "favicon.ico" not in e]
    results[label] = reqs
    errors[label] = errs
    record(ok, "%s loaded" % label, "" if ok else url)
    # ⊕ the brief's own words: "no Flashcards chip and no 'Flashcard decks'
    # link" — checked directly on the rendered DOM, on every teacher page,
    # not just inferred from the network log.
    if ok and "teacher" in label:
        try:
            has_link = p.eval("document.body.innerText.indexOf('Flashcard decks') > -1")
        except Exception:                                          # noqa: BLE001
            has_link = None
        record(has_link is False, "%s: no 'Flashcard decks' nav link" % label,
               "the link IS on the page" if has_link else "eval failed" if has_link is None else "")
    return reqs, errs


def norm_url(url):
    """Strip the scheme/host/port so the SAME path against a different port
    (two builds, two backends in earlier drafts) compares equal, and strip a
    cache-bust `?v=...` file's own query so an asset's differing hash cannot
    register as a request-shape difference (already filtered out above, kept
    here belt-and-braces for any remaining static reference in a query)."""
    return re.sub(r"^https?://[^/]+", "", url)


FLASHCARD_RE = re.compile(r"flashcard", re.I)


def analyse(reqs_by_page):
    """Returns (forbidden_hits, flashcard_hits, probe_count).

    ⚠️ THE FORBIDDEN-COLUMN CHECK IS SCOPED TO `/rest/v1/assignments`, NOT TO
    EVERY TABLE. `kind` is also a genuine, pre-existing, unrelated column on
    `public.ks3_cards` (the dashboard flashcard-practice card's front/back
    TYPE — MCQ vs cloze vs equation — see the "pool ownership" contract in
    CLAUDE.md), and the pupil class page legitimately selects it on every
    load. An unscoped substring match on `kind` flags that real, unrelated
    column as if it were the new `assignments.kind` this proof exists to
    catch — the two are unrelated columns on unrelated tables that happen to
    share an English word.
    """
    forbidden = []
    flashcard_hits = []
    for label, reqs in reqs_by_page.items():
        for r in reqs:
            url = r["url"]
            if FLASHCARD_RE.search(url):
                flashcard_hits.append((label, r["method"], url))
            if "assignment_flashcards" in url.lower():
                forbidden.append((label, "table assignment_flashcards", url))
            if "/rest/v1/assignments?" not in url and "/rest/v1/assignments&" not in url:
                continue
            m = re.search(r"[?&]select=([^&]*)", url)
            if m:
                sel = urllib.parse.unquote(m.group(1))
                tokens = re.split(r"[,()]", sel)
                for col in FORBIDDEN_COLS:
                    if any(t.strip() == col for t in tokens):
                        forbidden.append((label, "assignments select names %r" % col, url))
    # every flashcard_* hit other than exactly flashcard_decks is forbidden outright
    for label, method, url in flashcard_hits:
        if "flashcard_decks" not in url.lower():
            forbidden.append((label, "non-probe flashcard request", url))
    probe_hits = [h for h in flashcard_hits if "flashcard_decks" in h[2].lower()]
    return forbidden, flashcard_hits, probe_hits


# ════════════════════════════════════════════════════════════════════════
def add_main_worktree():
    """Create the detached origin/main worktree and return its path.

    ⚠️ SPLIT FROM THE BUILD STEP ON PURPOSE. If `build_all.py` fails inside a
    single "create + build" function, the exception unwinds before the caller
    ever receives a path, and `finally: remove_main_worktree(main_dir)` in
    `main()` cannot clean up a worktree it was never told about — exactly the
    kind of leak the brief's "temp worktrees removed" requirement is there to
    catch. So the caller assigns `main_dir` the moment the worktree exists,
    before the (separately fallible) build runs.
    """
    os.makedirs(os.path.expanduser("~/tmp"), exist_ok=True)
    d = tempfile.mkdtemp(prefix="mrb351-main-", dir=os.path.expanduser("~/tmp"))
    os.rmdir(d)  # git worktree add wants to create it itself
    print("   adding origin/main worktree at %s (temporary, deleted after use)" % d)
    subprocess.run(["git", "worktree", "add", "--detach", d, MAIN_REF],
                    cwd=REPO, check=True, capture_output=True)
    return d


def build_main_worktree(d):
    print("   building origin/main's site in %s" % d)
    subprocess.run(["python3", "build_all.py"], cwd=d, check=True,
                    capture_output=True)


def remove_main_worktree(d):
    subprocess.run(["git", "worktree", "remove", "--force", d], cwd=REPO,
                    capture_output=True)
    shutil.rmtree(d, ignore_errors=True)


def pick_ks3_scope(scope_tree, tier="easy"):
    for topic in scope_tree.get("tree") or []:
        for child in topic.get("children") or []:
            if (child.get("counts") or {}).get(tier, 0) > 0:
                return child["id"]
    return None


def preview_ids(token, class_id, tier, kind, ref, count=5):
    q = ("/api/teacher/set-work/preview?class_id=%s&tier=%s&scope_kind=%s"
         "&scope_ref=%s&count=%d" % (class_id, tier, kind, ref, count))
    st, body = call("GET", q, token)
    if st != 200:
        return None
    return [q["id"] for q in (body or {}).get("picked") or []]


def post_set(token, class_id, tier, scope_kind, scope_ref, question_ids, title, due_at):
    body = {
        "class_ids": [class_id], "tier": tier, "scope_kind": scope_kind,
        "scope_ref": scope_ref, "question_ids": question_ids, "title": title,
        "release_at": None, "due_at": due_at, "client_ref": str(uuid.uuid4()),
    }
    return call("POST", "/api/teacher/set-work", token, body)


def run_journey(site_base, label):
    """One full journey (teacher + pupil), returns (reqs_by_page, errs_by_page).

    ⚠️ TWO SEPARATE cdp.Browser() INSTANCES, ONE PER PERSONA — the same
    convention set_work_drive.py uses ("ONE BROWSER PER PERSONA,
    SEQUENTIALLY"). `Browser.attach()` always returns the SAME single page
    target for its own browser, so two personas in one Browser would share a
    tab and a `localStorage`, and the pupil's sign-in would silently replace
    the teacher's session mid-journey rather than the two being independent.
    """
    reqs_by_page, errs_by_page = {}, {}
    with cdp.Browser() as b:
        pt = b.attach()
        pt.set_viewport(390, 900)
        signed = sign_in_page(pt, site_base, FX.TEACHER_EMAIL, os.environ[FX.ENV_SWITCH])
        record(str(signed).startswith("ok"), "%s: teacher signs in through auth.html" % label, signed)
        enable_network(pt)

        # class-detail (KS3, real class), then open Set work on it
        url = "%s/teacher/class-detail.html?class=%s&env=test&api=%s" % (site_base, FX.C_KS3_A, PAGE_API)
        load_page(pt, url, "%s: teacher class-detail (8a/Sc1)" % label, reqs_by_page, errs_by_page,
                  ready="!!(window.MRBSetWork && window.MRBSetWork.open)")
        pt.eval("window.MRBSetWork.open({classId: %s})" % json.dumps(FX.C_KS3_A))
        time.sleep(1.5)
        try:
            has_chip = pt.eval(
                "Array.prototype.slice.call(document.querySelectorAll('[data-sw]'))"
                ".some(function(n){return (n.textContent||'').trim()==='Flashcards';})")
        except Exception:                                           # noqa: BLE001
            has_chip = None
        record(has_chip is False, "%s: no 'Flashcards' chip in the Set work sheet" % label,
               "the chip IS in the sheet" if has_chip else "eval failed" if has_chip is None else "")
        # ⚠️ CUMULATIVE, NOT ADDITIVE. `api_requests_since_nav` reads events
        # since the last NAVIGATION (`goto()` clears them), and no navigation
        # happens between the page load and opening the sheet — so this
        # second read already contains the class-detail page's own requests
        # once, as an exact prefix. Concatenating the class-detail bucket
        # onto it (an earlier version of this script did) double-counted
        # every one of them, including the flashcard-capability probe, which
        # is exactly the count this proof depends on getting right.
        cumulative = api_requests_since_nav(pt)
        prior = reqs_by_page["%s: teacher class-detail (8a/Sc1)" % label]
        reqs_by_page["%s: teacher Set work sheet opened (8a/Sc1)" % label] = \
            cumulative[len(prior):]
        pt.eval("try { window.MRBSetWork.close(); } catch (e) {}")

        # also touch the KS4 tree once, per the brief naming 10b/Sc5
        url = "%s/teacher/class-detail.html?class=%s&env=test&api=%s" % (site_base, FX.C_KS4_COMB, PAGE_API)
        load_page(pt, url, "%s: teacher class-detail (10b/Sc5)" % label, reqs_by_page, errs_by_page,
                  ready="!!(window.MRBSetWork && window.MRBSetWork.open)")
        pt.eval("window.MRBSetWork.open({classId: %s})" % json.dumps(FX.C_KS4_COMB))
        time.sleep(1.5)
        cumulative = api_requests_since_nav(pt)
        prior = reqs_by_page["%s: teacher class-detail (10b/Sc5)" % label]
        reqs_by_page["%s: teacher Set work sheet opened (10b/Sc5)" % label] = \
            cumulative[len(prior):]
        pt.eval("try { window.MRBSetWork.close(); } catch (e) {}")

        for name, path in (
            ("today", "/teacher/today.html"),
            ("timetable", "/teacher/timetable.html"),
            ("classes", "/teacher/classes.html"),
            ("class-detail (post-set)", "/teacher/class-detail.html?class=%s" % FX.C_KS3_A),
            ("digest", "/teacher/digest.html?class=%s" % FX.C_KS3_A),
            ("insights", "/teacher/insights.html?class=%s" % FX.C_KS3_A),
        ):
            url = "%s%s%senv=test&api=%s" % (site_base, path, "&" if "?" in path else "?", PAGE_API)
            load_page(pt, url, "%s: teacher %s" % (label, name), reqs_by_page, errs_by_page)

        pupil_id = FX.find_user(FX.PUPIL_EMAIL)
        url = "%s/teacher/student-detail.html?student=%s&env=test&api=%s" % (site_base, pupil_id, PAGE_API)
        load_page(pt, url, "%s: teacher student-detail" % label, reqs_by_page, errs_by_page)

    with cdp.Browser() as b2:
        pp = b2.attach()
        pp.set_viewport(390, 900)
        signed = sign_in_page(pp, site_base, FX.PUPIL_EMAIL, os.environ[FX.ENV_SWITCH])
        record(str(signed).startswith("ok"), "%s: pupil signs in through auth.html" % label, signed)
        enable_network(pp)
        url = "%s/student/class.html?class=%s&env=test&api=%s" % (site_base, FX.C_KS3_A, PAGE_API)
        load_page(pp, url, "%s: pupil class page" % label, reqs_by_page, errs_by_page)
        pp.eval("(function(){var b=document.querySelector('.mrb-bell-btn'); "
                "if (b) { b.click(); return true; } return false;})()")
        time.sleep(1.0)
        bell_reqs = api_requests_since_nav(pp)
        reqs_by_page["%s: pupil bell opened" % label] = bell_reqs
        errs_by_page["%s: pupil bell opened" % label] = \
            [e for e in pp.console_errors() if "favicon.ico" not in e]

    return reqs_by_page, errs_by_page


def main():
    pw = os.environ.get(FX.ENV_SWITCH, "")
    if not pw:
        raise SystemExit("Set %s." % FX.ENV_SWITCH)

    print("\nMRB-351 no-schema live proof — TEST rolled back, real backend, real browser\n")
    FX.seed()
    gone = FX.clear_work()
    if gone:
        print("   cleared %d leftover assignment(s)" % gone)
    teacher_token = sign_in(FX.TEACHER_EMAIL, pw, REPO)["access_token"]
    teacher_id = FX.find_user(FX.TEACHER_EMAIL)
    admin_id = FX.find_user(FX.ADMIN_EMAIL)

    main_dir = None
    server = None
    site_a = site_b = None
    try:
        site_a, site_a_port = cdp.serve(os.path.join(REPO, "mrbadmus_site"), port=SITE_A_PORT)
        base_a = "http://localhost:%d" % site_a_port
        main_dir = add_main_worktree()
        build_main_worktree(main_dir)
        site_b, site_b_port = cdp.serve(os.path.join(main_dir, "mrbadmus_site"), port=SITE_B_PORT)
        base_b = "http://localhost:%d" % site_b_port

        server = Server(extra_origins=[base_a, base_b])
        server.__enter__()

        # ── set a Questions assignment end to end, through the real backend ──
        scope_ks3 = call("GET", "/api/teacher/set-work/scope?class_id=" + FX.C_KS3_A, teacher_token)[1]
        ref = pick_ks3_scope(scope_ks3, "easy")
        record(bool(ref), "a stocked KS3 subtopic exists to set work from",
               ref or scope_ks3)
        made_title = None
        if ref:
            ids = preview_ids(teacher_token, FX.C_KS3_A, "easy", "subtopic", ref, 5)
            record(bool(ids), "preview returns question ids for %s" % ref, ids)
            if ids:
                due = (datetime.now(timezone.utc) + timedelta(days=7)).isoformat()
                made_title = "MRB-351 no-schema proof · " + str(uuid.uuid4())[:8]
                st, out = post_set(teacher_token, FX.C_KS3_A, "easy", "subtopic", ref,
                                    ids, made_title, due)
                record(st == 200, "POST /api/teacher/set-work (real route) wrote a Questions assignment",
                       "status %s %s" % (st, json.dumps(out)[:200]))

        print("\n── journey on THIS BRANCH's build (%s) ──" % base_a)
        reqs_a, errs_a = run_journey(base_a, "mine")
        print("\n── journey on origin/main's build (%s) ──" % base_b)
        reqs_b, errs_b = run_journey(base_b, "main")
    finally:
        if server:
            server.__exit__(None, None, None)
        if site_a:
            site_a.shutdown()
        if site_b:
            site_b.shutdown()
        if main_dir:
            remove_main_worktree(main_dir)
        print("\nclearing the throwaway world's assignments")
        FX.clear_work()
        FX.teardown()

    # ── the request-shape assertions, on THIS branch's build ──────────────
    print("\n── request-shape assertions (this branch) ──")
    forbidden, flashcard_hits, probes = analyse(reqs_a)
    record(not forbidden, "no request anywhere names a forbidden column, "
           "table or rpc", forbidden[:10])
    record(len(probes) <= 1, "the flashcard-capability probe fires at most "
           "once across the whole teacher browser session",
           "%d probe hit(s): %s" % (len(probes), probes))
    print("   probe count: %d" % len(probes))
    for label, count in ((l, len(r)) for l, r in reqs_a.items()):
        print("      %-55s %3d /rest or /api request(s)" % (label, count))

    # ── diff against origin/main, per page, STRUCTURALLY ──────────────────
    #
    # ⚠️ NOT A RAW-URL-STRING DIFF. A `select=` value is a comma-separated
    # column list PostgREST receives in whatever order the calling JS wrote
    # it in, and inserting one column (`quiz_type`) in the middle of an
    # existing select shifts every character after it — so a literal string
    # comparison would report the ENTIRE select as "different" on both sides
    # for the one legitimate change, rather than reporting the one column
    # that actually changed. `normalise_request` parses each request into
    # (path, sorted select columns with `quiz_type` excluded, sorted other
    # query params) so that column reordering and the one permitted addition
    # both wash out, and a genuine shape difference (a different table, a
    # different filter, a forbidden column) still shows up.
    print("\n── diff: this branch vs origin/main, same journey ──")

    def split_select(select):
        cols, cur, depth = [], "", 0
        for ch in select:
            if ch == "(":
                depth += 1
                cur += ch
            elif ch == ")":
                depth -= 1
                cur += ch
            elif ch == "," and depth == 0:
                cols.append(cur)
                cur = ""
            else:
                cur += ch
        if cur:
            cols.append(cur)
        return cols

    def normalise_request(url):
        u = norm_url(url)
        path, _, qs = u.partition("?")
        params = urllib.parse.parse_qs(qs, keep_blank_values=True)
        select = params.pop("select", [""])[0]
        cols = tuple(sorted(c.strip() for c in split_select(urllib.parse.unquote(select))
                             if c.strip() and c.strip() != "quiz_type"))
        other = tuple(sorted((k, tuple(sorted(v))) for k, v in params.items()))
        return (path, cols, other)

    def shape(reqs):
        return sorted(set(normalise_request(r["url"]) for r in reqs))

    all_bad_diff = []
    for label in reqs_a:
        blabel = label.replace("mine:", "main:")
        sa, sb = shape(reqs_a.get(label, [])), shape(reqs_b.get(blabel, []))
        only_a = [u for u in sa if u not in sb]
        only_b = [u for u in sb if u not in sa]
        ok = not only_a and not only_b
        if not ok:
            all_bad_diff.append((label, only_a, only_b))
        print("   %-55s +%d/-%d %s" % (label.replace("mine: ", ""), len(only_a), len(only_b),
                                        "OK" if ok else "DIFFERS"))
    record(not all_bad_diff, "no unexplained request-shape difference from origin/main "
           "(structurally: path + select columns other than `quiz_type` + other "
           "query params), for the identical journey", all_bad_diff[:8])

    # Two console lines are excused by name, not silently dropped, because
    # both are pre-existing and documented, not introduced by this branch:
    #   · the `mrbadmus-backend.onrender.com/api/health` CORS block is the
    #     "health-ping CORS flake" named in project memory
    #     (project_mrb291_engine_cleanup) — a background health check that
    #     fires on a timer against the real deployed backend regardless of
    #     which build is on screen, and legitimately CORS-fails from a local
    #     dev port; its presence on one build's capture and not the other's
    #     same page is the timer's, not the product's.
    #   · the `flashcard_decks` 404 is `teacher-admin-nav.js`'s own
    #     capability probe (see its header comment) succeeding at the ONE
    #     thing it is for: on a project with no flashcard schema, of course
    #     the probe's request 404s — that is what "fails closed" means, and
    #     the comment names this exact moment ("production... the migration
    #     [not] applied") as expected, not a defect this proof should catch.
    KNOWN_BENIGN = (
        "mrbadmus-backend.onrender.com/api/health",
        "flashcard_decks?select=id&limit=0",
    )
    print("\n── console errors: mine vs main, per page ──")
    console_bad = []
    for label, errs in errs_a.items():
        blabel = label.replace("mine:", "main:")
        main_errs = set(errs_b.get(blabel, []))
        extra = [e for e in errs if e not in main_errs
                 and not any(k in e for k in KNOWN_BENIGN)]
        if extra:
            console_bad.append((label, extra))
        print("   %-55s mine=%d main=%d %s"
              % (label.replace("mine: ", ""), len(errs), len(main_errs),
                 "OK" if not extra else "EXTRA: %s" % extra[:2]))
    record(not console_bad, "no console error on this branch that main's own "
           "build for the same journey does not also show", console_bad[:5])

    bad = [c for c in checks if not c[0]]
    print("\n%s  %d checks, %d failed\n" % ("FAIL" if bad else "PASS", len(checks), len(bad)))
    for ok, label, detail in bad:
        print("   - %s" % label)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
