#!/usr/bin/env python3
"""sharpen_pupil_live.py — Sharpen lane P's LIVE proof on TEST (C3 + C5).

A throwaway KS3 class on TEST, a throwaway teacher and pupil, and three sets
written through the REAL backend (`POST /api/teacher/set-work`, run locally
from the backend worktree against TEST):

  done    — every question answered (2 right, the rest wrong), completed
  partly  — half answered, completed               → "Finish it"
  older   — a completed set moved to an earlier teaching week (C3's picker)

Then, in headless Chrome, as the pupil, on the real `student/class.html` and
`student/assignment.html` served from this worktree (config → TEST, backend →
localhost:3000):

  C3  the week select opens on THIS week (it holds work), lists the weeks that
      hold work, filters the list, and All weeks shows everything
  C5  the completed rows' ONE button is "See your answers" / "Finish it"
      (no Close); See your answers opens the results: every question with its
      mark; "Look at it" → "Change my answer" → a new answer is CONFIRMED and
      the server answers `revised: true`, same attempt, score changed,
      completed_at / is_late untouched; "Finish it" opens on the first
      unanswered question, which is simply answerable
  C5  degrade: with the backend's `revised` stripped from the payloads (an
      old backend), the set is read-only with no error; and a revision
      refused 409 puts the old answer back, read-only, no error
  C5  teacher: the student screen's history row says "revised after marking"
      and the Breakdown panel's HANDED IN tile carries "Revised after marking …"

    MRB_SHOTS=~/tmp/ks3-gates python3 tools/sharpen_pupil_live.py

Shots: $MRB_SHOTS/sharpen-C-pupil/ at 390 and 1440, light and dark.
TEST ONLY: the service key's own `ref` claim is checked before any write.
Throwaway rows are torn down by a SNAPSHOTTED ID LIST, never a predicate.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
import mrb351_acceptance as acc  # noqa: E402
import mrb351_pupil_flow_live as pf  # noqa: E402  (teardown, session_js)
import ks3_browser as cdp  # noqa: E402

DEFAULT_ENV = "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/sharpen/.env"
BACKEND = "http://localhost:3000"
PORT = 5614
FAILS: list[str] = []


def check(ok, what, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + what + (("  — " + detail) if detail and not ok else ""))
    if not ok:
        FAILS.append(what + (" — " + detail if detail else ""))
    return ok


def api(method, path, token, body=None, timeout=60):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BACKEND + path, data=data, method=method,
                                 headers={"Authorization": "Bearer " + token,
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            return r.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw.decode(errors="replace")[:300]


# ── the world ─────────────────────────────────────────────────────────────
def build(c, manifest, label):
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year],
                     "assignments": [], "users": []})
    people = {}
    for key in ("t", "p"):
        email = f"sharpenp-{key}-{label}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
        manifest["users"].append(uid)
        people[key] = {"id": uid, "email": email}
    manifest["people"] = people
    json.dump(manifest, open(manifest["_path"], "w"), indent=1)
    acc._ok("school", *c.write("schools", "POST", {
        "id": school, "name": f"Sharpen P {ts}", "code": f"SHARPP{ts}", "kind": "school",
        "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {
        "id": year, "school_id": school, "name": "sharpen-p", "start_date": start,
        "end_date": end, "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {
        "id": klass, "school_id": school, "academic_year_id": year,
        "name": f"8p/Sc{ts % 10}", "key_stage": "KS3", "year_group": 8}))
    # No automatic weekly work in this class: only the three sets below.
    st, body = c.write("classes", "PATCH", {"__match__": f"id=eq.{klass}", "auto_assignments": False})
    if st not in (200, 204):
        print(f"  (auto_assignments not set: {st} {str(body)[:120]})")
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['t']['id']}",
        "role": "teacher", "school_id": school, "first_name": "Tia", "last_name": "Sharpen",
        "display_name": "Tia Sharpen", "username": f"sharpt{ts:x}"}))
    acc._ok("p", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{people['p']['id']}",
        "role": "student", "school_id": school, "first_name": "Pip", "last_name": "Sharpen",
        "display_name": "Pip Sharpen", "username": f"sharpp{ts:x}",
        "science_pathway": "combined", "tier": "higher"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Biology"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": people["t"]["id"], "role": "subject_teacher",
        "subject_id": subj[0]["id"]}))
    acc._ok("class_members", *c.write("class_members", "POST", {
        "class_id": klass, "student_id": people["p"]["id"], "joined_via": "admin_added"}))
    return {"school": school, "class": klass, "people": people}


def pick_scope(tok_t, klass):
    st, sc = api("GET", f"/api/teacher/set-work/scope?class_id={klass}", tok_t)
    if st != 200:
        acc.die(f"scope {st} {sc}")
    tiers = sc.get("tiers") or []
    tier = None
    for t in tiers:
        tid = t.get("id") if isinstance(t, dict) else t
        if tid in ("standard", "medium", "higher"):
            tier = tid
    if tier is None and tiers:
        tier = tiers[0].get("id") if isinstance(tiers[0], dict) else tiers[0]
    # every lesson (a subtopic of a unit), with its unit's subject
    lessons = []
    for topic in sc.get("tree") or []:
        for child in topic.get("children") or []:
            lessons.append((child, topic.get("subject")))
    return sc, tier, lessons


def make_set(tok_t, klass, tier, lesson, subject, title, n, due_days=4):
    q = f"/api/teacher/set-work/preview?class_id={klass}&tier={tier}&scope_kind=subtopic&scope_ref={lesson}&count={n}"
    if subject:
        q += f"&subject={subject}"
    st, pv = api("GET", q, tok_t)
    if st != 200:
        acc.die(f"preview {st} {pv}")
    ids = [x["id"] for x in (pv.get("picked") or [])][:n]
    if len(ids) < n:
        acc.die(f"preview gave {len(ids)} ids for {lesson}")
    now = datetime.now(timezone.utc)
    body = {"class_ids": [klass], "tier": tier, "title": title,
            "release_at": None, "due_at": (now + timedelta(days=due_days)).isoformat(),
            "client_ref": str(uuid.uuid4()),
            "scopes": [{"scope_kind": "subtopic", "scope_ref": lesson,
                        "subject": subject, "question_ids": ids}]}
    st, out = api("POST", "/api/teacher/set-work", tok_t, body)
    if st != 200:
        acc.die(f"set-work {st} {out}")
    aid = (out.get("assignment_ids") or [None])[0] or (out.get("assignments") or [{}])[0].get("id")
    if not aid:
        acc.die(f"set-work returned no id: {out}")
    return aid


def serve_questions(tok_p, klass, aid):
    st, cur = api("GET", f"/api/class/current-assignment?class_id={klass}&assignment_id={aid}", tok_p)
    if st != 200:
        acc.die(f"current-assignment {st} {cur}")
    return cur


def answer_body(q, index, pick_right):
    opts = q.get("options") or []
    right = next((o for o in opts if o.get("correct")), None)
    wrong = next((o for o in opts if not o.get("correct")), None)
    chosen = right if pick_right else wrong
    return {"question_index": index, "question_ref": q.get("question_ref"),
            "question_text": q.get("text"), "rung": q.get("rung"),
            "selected_answer": chosen.get("text"), "correct_answer": right.get("text") if right else None,
            "selected_option_letter": chosen.get("letter"),
            "correct_option_letter": right.get("letter") if right else None,
            "is_correct": chosen is right, "time_spent_seconds": 5}


def sub_row(c, aid, pid):
    st, rows = c.select(None, "assignment_submissions", {
        "assignment_id": f"eq.{aid}", "student_id": f"eq.{pid}",
        "select": "id,attempt_no,status,score,max_score,completed_at,submitted_at,updated_at,is_late",
        "order": "attempt_no.asc"}, as_service=True)
    return rows or []


# ── the browser ───────────────────────────────────────────────────────────
class P:
    def __init__(self, page, shots):
        self.page, self.shots = page, shots

    def q(self, js):
        return self.page.eval(js)

    def wait(self, js, what, timeout=25):
        t0 = time.time()
        while time.time() - t0 < timeout:
            try:
                v = self.q(js)
            except Exception:
                v = None
            if v:
                return v
            time.sleep(0.4)
        print(f"  [wait] {what} not reached; text: "
              f"{(self.q('document.body.innerText') or '')[:300]!r}")
        return None

    def shot(self, name, sel=None, w=390, h=844, above=100):
        y = 0
        if sel:
            r = self.q("(function(){var e=document.querySelector(%s);if(!e)return null;"
                       "var b=e.getBoundingClientRect();return b.top+window.scrollY})()" % json.dumps(sel))
            if r is not None:
                y = max(0, float(r) - above)
        res = self.page.send("Page.captureScreenshot", {
            "format": "png", "captureBeyondViewport": True, "fromSurface": True,
            "clip": {"x": 0, "y": y, "width": w, "height": h, "scale": 1}})
        path = os.path.join(self.shots, name + ".png")
        open(path, "wb").write(base64.b64decode(res["data"]))
        return path


def viewport(page, w, h, mobile):
    page.send("Emulation.setDeviceMetricsOverride",
              {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": mobile})


CLICK_TEXT = r"""(function (txt, scope) {
  var root = scope ? document.querySelector(scope) : document;
  if (!root) return null;
  var els = root.querySelectorAll('button,a');
  for (var i = 0; i < els.length; i++) {
    var t = (els[i].innerText || '').replace(/\s+/g, ' ').trim();
    if (t === txt) { els[i].click(); return t; }
  }
  return null;
})(%s, %s)"""

HAS_TEXT = r"""(function (txt) {
  return (document.body.innerText || '').indexOf(txt) >= 0;
})(%s)"""

ROW_OPEN = r"""(function (title) {
  var bs = document.querySelectorAll('#work button');
  for (var i = 0; i < bs.length; i++) {
    if ((bs[i].innerText || '').indexOf(title) >= 0) { bs[i].click(); return bs[i].innerText; }
  }
  return null;
})(%s)"""

# the expanded row's buttons, in order (the row header is excluded)
ROW_BUTTONS = r"""(function (title) {
  var bs = [].slice.call(document.querySelectorAll('#work button'));
  var i = bs.findIndex(function (b) { return (b.innerText || '').indexOf(title) >= 0; });
  if (i < 0) return null;
  var out = [];
  for (var j = i + 1; j < bs.length; j++) {
    var t = (bs[j].innerText || '').replace(/\s+/g, ' ').trim();
    if (/^W\d\d /.test(t) || bs[j].getAttribute('aria-expanded') !== null) break;
    out.push(t);
  }
  return JSON.stringify(out);
})(%s)"""

WEEK = r"""(function (v) {
  var s = document.querySelector('[data-mrb-week-select]');
  if (!s) return null;
  if (v !== null) { s.value = v; s.dispatchEvent(new Event('change', {bubbles: true})); }
  return JSON.stringify({value: s.value,
    options: [].map.call(s.options, function (o) { return o.text; }),
    rows: [].map.call(document.querySelectorAll('#work button[aria-expanded]'),
      function (b) { return (b.innerText || '').replace(/\s+/g, ' ').trim(); })});
})(%s)"""

ASG = r"""(function () {
  var r = document.querySelector('.rd[data-mode="ks3"]');
  var t = r ? (r.innerText || '') : '';
  var opts = [].slice.call(document.querySelectorAll('button')).filter(function (e) {
    var s = (e.innerText || '').trim(); return /^[ABCD]\n/.test(s) && s.split('\n').length <= 3;
  });
  return JSON.stringify({
    text: t.replace(/\s+/g, ' ').slice(0, 4000),
    change: !!document.querySelector('[data-mrb-change-answer]'),
    confirm: [].some.call(document.querySelectorAll('button'), function (b) { return (b.innerText||'').trim() === 'Confirm answer'; }),
    marks: [].map.call(document.querySelectorAll('[data-mrb-done-mark]'), function (m) { return m.innerText; }),
    optCursor: opts.map(function (o) { return getComputedStyle(o).cursor; }),
    nOpts: opts.length,
    err: /could not|went wrong|try again later/i.test(t)
  });
})()"""

PICK_OPT = r"""(function (letter) {
  var opts = [].slice.call(document.querySelectorAll('button')).filter(function (e) {
    var s = (e.innerText || '').trim(); return /^[ABCD]\n/.test(s) && s.split('\n').length <= 3;
  });
  var o = opts.find(function (e) { return (e.innerText || '').trim().charAt(0) === letter; });
  if (!o) return null; o.click(); return letter;
})(%s)"""

# watch the answer POSTs the page makes (body + response), and optionally
# rewrite them: `strip` removes `revised` from progress payloads (an old
# backend), `refuse` answers a revise 409 as an old backend would.
NET = r"""(function () {
  if (window.__netWrapped) return; window.__netWrapped = true;
  window.__answers = [];
  var mode = (function () { try { return sessionStorage.getItem('sharpenNet') || ''; } catch (e) { return ''; } })();
  var of = window.fetch;
  window.fetch = function (url, init) {
    var u = String(url || '');
    var isAns = /\/api\/assignment\/answer/.test(u);
    var body = null;
    try { body = init && init.body ? JSON.parse(init.body) : null; } catch (e) {}
    if (isAns && mode === 'offline') {
      window.__answers.push({ body: body, status: 0, res: null });
      return Promise.reject(new TypeError('Failed to fetch'));
    }
    if (isAns && mode === 'refuse' && body && body.revise === true) {
      window.__answers.push({ body: body, status: 409, res: null });
      return Promise.resolve(new Response(JSON.stringify({ error: 'attempt_already_complete' }),
        { status: 409, headers: { 'Content-Type': 'application/json' } }));
    }
    return of.apply(this, arguments).then(function (res) {
      if (isAns) {
        return res.clone().json().then(function (j) {
          window.__answers.push({ body: body, status: res.status, res: j }); return res;
        }, function () { return res; });
      }
      if (mode === 'strip' && /current-assignment|assignment\/progress/.test(u)) {
        return res.clone().json().then(function (j) {
          if (j && typeof j === 'object') {
            delete j.revised; if (j.resume) delete j.resume.revised;
          }
          return new Response(JSON.stringify(j), { status: res.status, headers: res.headers });
        }, function () { return res; });
      }
      return res;
    });
  };
})();"""


def open_page(page, url, ready_js, timeout=40):
    page.goto("about:blank")
    page.goto(url)
    t0 = time.time()
    while time.time() - t0 < timeout:
        try:
            if page.eval(ready_js):
                time.sleep(0.8)
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="run")
    ap.add_argument("--env-file", default=DEFAULT_ENV)
    ap.add_argument("--keep", action="store_true")
    a = ap.parse_args()

    env = acc.read_env(a.env_file)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")
    c = acc.Client(url, acc.anon_key(), service)
    shots = os.path.join(os.environ.get("MRB_SHOTS") or cdp.gate_tmp(), "sharpen-C-pupil")
    os.makedirs(shots, exist_ok=True)
    manifest = {"_path": os.path.join(shots, "manifest.json")}
    result = {}
    try:
        w = build(c, manifest, a.label)
        klass, pupil, teacher = w["class"], w["people"]["p"], w["people"]["t"]
        tok_t = c.sign_in(teacher["email"], acc.THROWAWAY_PASSWORD)
        tok_p = c.sign_in(pupil["email"], acc.THROWAWAY_PASSWORD)
        sc, tier, lessons = pick_scope(tok_t, klass)
        # a lesson with a pool of at least 6 at this tier
        chosen = None
        for n, subj in lessons:
            cnt = n.get("counts") or n.get("count") or {}
            k = cnt.get(tier) if isinstance(cnt, dict) else cnt
            if (k or 0) >= 12:
                chosen = (n["id"], subj)
                break
        if not chosen:
            acc.die(f"no lesson with 12+ questions at {tier}: {[(x[0].get('id'), x[0].get('counts')) for x in lessons[:5]]}")
        lesson, subject = chosen
        print(f"  scope: tier={tier} lesson={lesson} subject={subject}")
        a_done = make_set(tok_t, klass, tier, lesson, subject, "Done set", 4)
        a_part = make_set(tok_t, klass, tier, lesson, subject, "Partly set", 4)
        a_old = make_set(tok_t, klass, tier, lesson, subject, "Older set", 3)
        manifest["assignments"] += [a_done, a_part, a_old]
        json.dump(manifest, open(manifest["_path"], "w"), indent=1)
        # the older set moves to an earlier teaching week
        st, rows = c.select(None, "assignments", {"id": f"eq.{a_done}", "select": "academic_week"}, as_service=True)
        wk_now = rows[0]["academic_week"]
        wk_old = max(1, (wk_now or 2) - 2)
        acc._ok("older week", *c.write("assignments", "PATCH", {"__match__": f"id=eq.{a_old}",
                                                                "academic_week": wk_old}))
        result["weeks"] = {"now": wk_now, "old": wk_old}

        # the pupil's answers, through the real routes
        plan = {a_done: [True, True, False, False], a_part: [True, False, None, None],
                a_old: [True, True, True]}
        served = {}
        for aid, picks in plan.items():
            cur = serve_questions(tok_p, klass, aid)
            qs = cur.get("questions") or []
            served[aid] = qs
            for i, p in enumerate(picks):
                if p is None:
                    continue
                st, out = api("POST", "/api/assignment/answer", tok_p,
                              {"assignment_id": aid, "answer": answer_body(qs[i], i, p)})
                if st != 200:
                    acc.die(f"answer {aid} {i}: {st} {out}")
            st, out = api("POST", "/api/assignment/complete", tok_p, {"assignment_id": aid, "total_time_seconds": 60})
            if st != 200:
                acc.die(f"complete {aid}: {st} {out}")
        before = sub_row(c, a_done, pupil["id"])[0]
        result["done_before"] = before
        check(before["status"] == "complete" and before["score"] == 2,
              "setup: the done set is complete at 2 right (%s/%s)" % (before["score"], before["max_score"]))
        # contract: an answer WITHOUT revise on a complete set is still 409
        st, out = api("POST", "/api/assignment/answer", tok_p,
                      {"assignment_id": a_done, "answer": answer_body(served[a_done][2], 2, True)})
        check(st == 409, "contract: answering a completed set without revise is still 409 (%s)" % st)
        time.sleep(3.0)     # so a revision lands well past the 2 s slack

        server, port = cdp.serve(REPO, PORT)
        try:
            with cdp.Browser() as br:
                page = br.attach()
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": NET})
                st, sess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                                  {"apikey": c.anon, "Content-Type": "application/json"},
                                  {"email": pupil["email"], "password": acc.THROWAWAY_PASSWORD})
                sess_id = page.send("Page.addScriptToEvaluateOnNewDocument",
                                    {"source": pf.session_js(ref, sess)})["identifier"]
                B = P(page, shots)
                cls_url = f"http://127.0.0.1:{port}/student/class.html?class={klass}"
                ready_cls = "!!document.querySelector('[data-mrb-week-select]')"

                def theme_js(t):
                    return ("(function(){try{localStorage.setItem('mrb-theme',%s)}catch(e){}})()"
                            % json.dumps(t))

                # ══ C3 — the week select, at 390 and 1440, light and dark ══
                for theme in ("light", "dark"):
                    for (vw, vh, mob) in ((390, 844, True), (1440, 900, False)):
                        viewport(page, vw, vh, mob)
                        open_page(page, "about:blank", "true")
                        page.goto(f"http://127.0.0.1:{port}/student/settings.html")
                        time.sleep(0.5)
                        B.q(theme_js(theme))
                        ok = open_page(page, cls_url, ready_cls)
                        check(ok, f"C3 {theme} {vw}: the class page mounts with the week select")
                        s = json.loads(B.q(WEEK % "null") or "{}")
                        tag = f"{vw}-{theme}"
                        if theme == "light" and vw == 390:
                            result["select_default"] = s
                            check(s.get("value") == str(wk_now),
                                  "C3: the select opens on THIS week (it holds work)",
                                  "value=%r want %r" % (s.get("value"), wk_now))
                            check(any("this week" in o for o in s.get("options", []))
                                  and s.get("options", [None])[0] == "All weeks"
                                  and any(o.startswith("Week %d" % wk_old) for o in s.get("options", [])),
                                  "C3: options are All weeks + the weeks holding work, this week marked",
                                  str(s.get("options")))
                            titles = " | ".join(s.get("rows", []))
                            check("Done set" in titles and "Partly set" in titles and "Older set" not in titles,
                                  "C3: this week's list holds this week's sets only", titles)
                        B.shot(f"c3-{tag}-01-this-week", "#work", vw, vh)
                        B.q(WEEK % json.dumps(str(wk_old)))
                        time.sleep(0.6)
                        s = json.loads(B.q(WEEK % "null") or "{}")
                        if theme == "light" and vw == 390:
                            titles = " | ".join(s.get("rows", []))
                            check(s.get("value") == str(wk_old) and "Older set" in titles and "Done set" not in titles,
                                  "C3: choosing week %d filters to that week" % wk_old, titles)
                        B.shot(f"c3-{tag}-02-other-week", "#work", vw, vh)
                        B.q(WEEK % json.dumps(""))
                        time.sleep(0.6)
                        s = json.loads(B.q(WEEK % "null") or "{}")
                        if theme == "light" and vw == 390:
                            titles = " | ".join(s.get("rows", []))
                            check(all(t in titles for t in ("Done set", "Partly set", "Older set")),
                                  "C3: All weeks shows everything", titles)

                        # ══ C5 — the rows' one button ═══════════════════════
                        B.q(WEEK % json.dumps(str(wk_now)))
                        time.sleep(0.4)
                        B.q(ROW_OPEN % json.dumps("Done set"))
                        time.sleep(0.6)
                        btns = json.loads(B.q(ROW_BUTTONS % json.dumps("Done set")) or "[]")
                        if theme == "light" and vw == 390:
                            result["done_row_buttons"] = btns
                            check(btns[:1] == ["See your answers"] and "Close" not in btns,
                                  "C5: the done set's expanded row has ONE button, See your answers", str(btns))
                        B.shot(f"c5-{tag}-01-done-row", "#work", vw, vh)
                        B.q(ROW_OPEN % json.dumps("Done set"))
                        time.sleep(0.3)
                        B.q(ROW_OPEN % json.dumps("Partly set"))
                        time.sleep(0.6)
                        btns = json.loads(B.q(ROW_BUTTONS % json.dumps("Partly set")) or "[]")
                        if theme == "light" and vw == 390:
                            result["part_row_buttons"] = btns
                            check(btns[:1] == ["Finish it"] and "Close" not in btns,
                                  "C5: the partly-done set's row has ONE button, Finish it", str(btns))
                        B.shot(f"c5-{tag}-02-partly-row", "#work", vw, vh)
                        bench = B.q("(function(){var b=document.querySelector('[data-port-region=\"bench-done\"]');"
                                    "return b?b.innerText.replace(/\\s+/g,' '):null})()")
                        if bench:
                            B.shot(f"c5-{tag}-03-done-bench", "[data-port-region=\"bench-done\"]", vw, vh)
                            if theme == "light" and vw == 390:
                                result["done_bench"] = bench
                                check("Read the feedback" not in bench and
                                      ("See your answers" in bench or "Finish it" in bench),
                                      "C5: the done bench's one button is See your answers / Finish it", bench[:200])

                # ══ C5 — See your answers → change an answer ═══════════════
                viewport(page, 390, 844, True)
                page.goto(f"http://127.0.0.1:{port}/student/settings.html")
                time.sleep(0.4)
                B.q(theme_js("light"))
                open_page(page, cls_url, ready_cls)
                B.q(WEEK % json.dumps(str(wk_now)))
                time.sleep(0.3)
                B.q(ROW_OPEN % json.dumps("Done set"))
                time.sleep(0.5)
                B.q(CLICK_TEXT % (json.dumps("See your answers"), json.dumps("#work")))
                ok = B.wait("location.pathname.indexOf('assignment') >= 0 && "
                            "document.querySelectorAll('[data-mrb-done-mark]').length > 0", "results")
                s = json.loads(B.q(ASG))
                result["results_before"] = s
                check(ok and s["marks"] == ["✓", "✓", "✗", "✗"],
                      "C5: See your answers opens the results — every question, with its mark", str(s["marks"]))
                check("YOUR ANSWERS" in s["text"].upper() and "2 / 4" in s["text"],
                      "C5: the results are headed Your answers and score 2 / 4", s["text"][:300])
                B.shot("c5-390-light-04-results", ".rd", 390, 844, above=0)
                # Look at it on question 3 (wrong)
                B.q(r"""(function(){var b=[].slice.call(document.querySelectorAll('button')).filter(function(x){return /Look at it/.test(x.innerText)});b[2].click();})()""")
                time.sleep(0.8)
                s = json.loads(B.q(ASG))
                check(s["change"] and not s["confirm"],
                      "C5: an answered question on a completed set shows Change my answer (and no Confirm)")
                B.shot("c5-390-light-05-look-at-it", ".rd", 390, 844, above=0)
                B.q("document.querySelector('[data-mrb-change-answer]').click()")
                time.sleep(0.5)
                q3 = served[a_done][2]
                right_letter = next(o["letter"] for o in q3["options"] if o.get("correct"))
                B.q(PICK_OPT % json.dumps(right_letter))
                time.sleep(0.4)
                B.q(CLICK_TEXT % (json.dumps("Confirm answer"), "null"))
                ans = B.wait("(window.__answers||[]).filter(function(a){return a.body&&a.body.revise===true&&a.status})"
                             ".length ? JSON.stringify(window.__answers) : null", "the revise POST")
                got = json.loads(ans or "[]")
                rv = [x for x in got if (x.get("body") or {}).get("revise") is True]
                result["revise_post"] = rv
                res = (rv[0].get("res") if rv else None) or {}
                check(bool(rv) and rv[0]["status"] == 200 and res.get("revised") is True
                      and res.get("status") == "complete" and res.get("attempt_no") == before["attempt_no"]
                      and res.get("submission_id") == before["id"] and res.get("score") == 3,
                      "C5: the page sends revise:true and the server revises THE SAME attempt (score 3)",
                      json.dumps(res)[:300])
                s = json.loads(B.q(ASG))
                B.shot("c5-390-light-06-changed-answer", ".rd", 390, 844, above=0)
                B.q(CLICK_TEXT % (json.dumps("Summary"), "null"))
                time.sleep(0.8)
                s = json.loads(B.q(ASG))
                result["results_after"] = s
                check(s["marks"] == ["✓", "✓", "✓", "✗"] and "3 / 4" in s["text"]
                      and "REVISED AFTER MARKING" in s["text"].upper(),
                      "C5: the results now read 3 / 4, question 3 ticked, revised after marking",
                      "%s %s" % (s["marks"], s["text"][:200]))
                B.shot("c5-390-light-07-results-revised", ".rd", 390, 844, above=0)
                after = sub_row(c, a_done, pupil["id"])
                result["done_after"] = after
                a1 = after[0] if after else {}
                check(len(after) == 1 and a1["id"] == before["id"] and a1["status"] == "complete"
                      and a1["score"] == 3 and a1["completed_at"] == before["completed_at"]
                      and a1["is_late"] == before["is_late"],
                      "DB: one attempt, same row, complete, score 3; completed_at and is_late untouched",
                      json.dumps(after)[:300])
                st, prog = api("GET", f"/api/assignment/progress?assignment_id={a_done}", tok_p)
                check(st == 200 and prog.get("revised") is True, "API: /progress says revised: true")
                # dark + 1440 of the results
                for (vw, vh, mob, theme) in ((1440, 900, False, "light"), (390, 844, True, "dark"),
                                             (1440, 900, False, "dark")):
                    viewport(page, vw, vh, mob)
                    page.goto(f"http://127.0.0.1:{port}/student/settings.html")
                    time.sleep(0.4)
                    B.q(theme_js(theme))
                    open_page(page, f"http://127.0.0.1:{port}/student/assignment.html?class={klass}&assignment={a_done}",
                              "document.querySelectorAll('[data-mrb-done-mark]').length > 0")
                    B.shot(f"c5-{vw}-{theme}-07-results-revised", ".rd", vw, vh, above=0)

                # ══ C5 — Finish it → the first unanswered question ═══════
                viewport(page, 390, 844, True)
                page.goto(f"http://127.0.0.1:{port}/student/settings.html")
                time.sleep(0.4)
                B.q(theme_js("light"))
                open_page(page, cls_url, ready_cls)
                B.q(WEEK % json.dumps(str(wk_now)))
                time.sleep(0.3)
                B.q(ROW_OPEN % json.dumps("Partly set"))
                time.sleep(0.5)
                B.q(CLICK_TEXT % (json.dumps("Finish it"), json.dumps("#work")))
                ok = B.wait("location.pathname.indexOf('assignment') >= 0 && /Question 03/i.test(document.body.innerText)",
                            "the first unanswered question")
                s = json.loads(B.q(ASG))
                check(ok and not s["change"] and s["nOpts"] >= 2 and all(cu == "pointer" for cu in s["optCursor"]),
                      "C5: Finish it opens on question 3, the first unanswered, and it is answerable",
                      "%s %s" % (s["optCursor"], s["text"][:160]))
                B.shot("c5-390-light-08-finish-it", ".rd", 390, 844, above=0)
                q = served[a_part][2]
                B.q(PICK_OPT % json.dumps(next(o["letter"] for o in q["options"] if o.get("correct"))))
                time.sleep(0.3)
                B.q(CLICK_TEXT % (json.dumps("Confirm answer"), "null"))
                ans = B.wait("(window.__answers||[]).filter(function(a){return a.body&&a.body.revise===true&&a.status})"
                             ".length ? JSON.stringify(window.__answers) : null", "the finish POST")
                rv = [x for x in json.loads(ans or "[]") if (x.get("body") or {}).get("revise") is True]
                check(bool(rv) and rv[0]["status"] == 200 and (rv[0].get("res") or {}).get("answered") == 3,
                      "C5: answering an unanswered question on a completed set saves (3 of 4 answered)",
                      json.dumps(rv)[:200])
                B.shot("c5-390-light-09-finish-answered", ".rd", 390, 844, above=0)

                # ══ C5 — a revision queued offline survives a reload ════════
                page.goto(f"http://127.0.0.1:{port}/student/settings.html")
                B.q("sessionStorage.setItem('sharpenNet','offline')")
                open_page(page, f"http://127.0.0.1:{port}/student/assignment.html?class={klass}&assignment={a_done}",
                          "document.querySelectorAll('[data-mrb-done-mark]').length > 0")
                B.q(r"""(function(){var b=[].slice.call(document.querySelectorAll('button')).filter(function(x){return /Look at it/.test(x.innerText)});b[3].click();})()""")
                time.sleep(0.6)
                B.q("document.querySelector('[data-mrb-change-answer]').click()")
                time.sleep(0.4)
                q4 = served[a_done][3]
                B.q(PICK_OPT % json.dumps(next(o["letter"] for o in q4["options"] if o.get("correct"))))
                time.sleep(0.3)
                B.q(CLICK_TEXT % (json.dumps("Confirm answer"), "null"))
                time.sleep(1.5)
                queued = B.q("(function(){for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);"
                             "if(k.indexOf('mrbadmusai.answerqueue.v1.')===0){var d=JSON.parse(localStorage.getItem(k));"
                             "var e=d&&d.e&&d.e['3'];if(e)return JSON.stringify({revise:e.revise});}}return null})()")
                check(bool(queued) and json.loads(queued).get("revise") is True,
                      "C5 offline: the change is queued on the device, marked as a revision", str(queued))
                mid = sub_row(c, a_done, pupil["id"])[0]
                page.goto(f"http://127.0.0.1:{port}/student/settings.html")
                B.q("sessionStorage.removeItem('sharpenNet')")
                open_page(page, f"http://127.0.0.1:{port}/student/assignment.html?class={klass}&assignment={a_done}",
                          "document.querySelectorAll('[data-mrb-done-mark]').length > 0")
                ans = B.wait("(window.__answers||[]).filter(function(a){return a.body&&a.body.revise===true&&a.status===200})"
                             ".length ? JSON.stringify(window.__answers) : null", "the queued revision, sent on reload")
                after_q = sub_row(c, a_done, pupil["id"])[0]
                result["offline_queue"] = {"before": mid, "after": after_q}
                check(bool(ans) and mid["score"] == 3 and after_q["score"] == 4 and after_q["id"] == mid["id"],
                      "C5 offline: on reload the queued revision is sent with revise:true — score 3 → 4, same row",
                      "%s → %s" % (mid.get("score"), after_q.get("score")))
                B.shot("c5-390-light-09b-offline-revision-sent", ".rd", 390, 844, above=0)

                # ══ C5 — degrade: an old backend (no `revised`) ═════════════
                page.goto(f"http://127.0.0.1:{port}/student/settings.html")
                B.q("sessionStorage.setItem('sharpenNet','strip')")
                open_page(page, f"http://127.0.0.1:{port}/student/assignment.html?class={klass}&assignment={a_old}",
                          "document.querySelectorAll('[data-mrb-done-mark]').length > 0 || "
                          "/Your answers|Where it went wrong/i.test(document.body.innerText)")
                B.q(r"""(function(){var b=[].slice.call(document.querySelectorAll('button')).filter(function(x){return /Look at it/.test(x.innerText)});if(b[0])b[0].click();})()""")
                time.sleep(0.8)
                s = json.loads(B.q(ASG))
                check(not s["change"] and not s["err"] and all(cu == "default" for cu in s["optCursor"]),
                      "C5 degrade: with no `revised` (old backend) the set is read-only, no error",
                      "%s %s" % (s["change"], s["optCursor"]))
                B.shot("c5-390-light-10-degrade-readonly", ".rd", 390, 844, above=0)
                # ══ C5 — degrade: a revision refused 409 ════════════════════
                page.goto(f"http://127.0.0.1:{port}/student/settings.html")
                B.q("sessionStorage.setItem('sharpenNet','refuse')")
                open_page(page, f"http://127.0.0.1:{port}/student/assignment.html?class={klass}&assignment={a_old}",
                          "document.querySelectorAll('[data-mrb-done-mark]').length > 0")
                B.q(r"""(function(){var b=[].slice.call(document.querySelectorAll('button')).filter(function(x){return /Look at it/.test(x.innerText)});if(b[0])b[0].click();})()""")
                time.sleep(0.6)
                B.q("document.querySelector('[data-mrb-change-answer]').click()")
                time.sleep(0.4)
                q = served[a_old][0]
                B.q(PICK_OPT % json.dumps(next(o["letter"] for o in q["options"] if not o.get("correct"))))
                time.sleep(0.3)
                B.q(CLICK_TEXT % (json.dumps("Confirm answer"), "null"))
                time.sleep(2.5)
                s = json.loads(B.q(ASG))
                check(not s["change"] and not s["err"] and "RIGHT" in s["text"] and "NOT THIS ONE" not in s["text"],
                      "C5 degrade: a revision refused 409 puts the old (right) answer back, read-only, no error",
                      s["text"][:300])
                B.shot("c5-390-light-11-degrade-refused", ".rd", 390, 844, above=0)
                B.q("sessionStorage.removeItem('sharpenNet')")
                after_old = sub_row(c, a_old, pupil["id"])
                check(after_old and after_old[0]["score"] == 3, "DB: the refused revision changed nothing (3/3)")

                # ══ C6 — a named set the server cannot serve says so ═══════
                open_page(page, f"http://127.0.0.1:{port}/student/assignment.html?class={klass}"
                                f"&assignment={uuid.uuid4()}",
                          "/No work has been set|could not load/i.test(document.body.innerText)")
                txt = B.q("document.body.innerText") or ""
                check("No work has been set for this week yet." in txt,
                      "C6: an assignment the server cannot serve says there is no such work", txt[:160])
                # ══ C6 — settings and claim-confirm, as the pupil ═══════════
                for (vw, vh, mob, theme) in ((390, 844, True, "light"), (1440, 900, False, "light"),
                                             (390, 844, True, "dark"), (1440, 900, False, "dark")):
                    viewport(page, vw, vh, mob)
                    page.goto(f"http://127.0.0.1:{port}/student/settings.html")
                    time.sleep(0.4)
                    B.q(theme_js(theme))
                    open_page(page, f"http://127.0.0.1:{port}/student/settings.html",
                              "/Account settings/.test(document.body.innerText)")
                    B.shot(f"c6-{vw}-{theme}-settings", None, vw, vh)
                    open_page(page, f"http://127.0.0.1:{port}/student/claim-confirm.html",
                              "/can.t be used/.test(document.body.innerText)")
                    time.sleep(1.0)
                    if vw == 390 and theme == "light":
                        t = B.q("document.body.innerText") or ""
                        check("Ask for a new one in Account settings, or ask your teacher." in t
                              and "Account settings" in (B.q("document.getElementById('problem-auth-link').innerText") or ""),
                              "C6: claim-confirm says the one thing, and sends a signed-in pupil to Account settings",
                              t[:200])
                        st_txt = ""
                    B.shot(f"c6-{vw}-{theme}-claim-confirm", None, vw, vh)
                viewport(page, 390, 844, True)

                # ══ the teacher's screens ═══════════════════════════════════
                page.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": sess_id})
                st, tsess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                                   {"apikey": c.anon, "Content-Type": "application/json"},
                                   {"email": teacher["email"], "password": acc.THROWAWAY_PASSWORD})
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, tsess)})
                sd_url = (f"http://127.0.0.1:{port}/teacher/student-detail.html?class={klass}"
                          f"&student={pupil['id']}")
                for (vw, vh, mob, theme) in ((1440, 900, False, "light"), (390, 844, True, "light"),
                                             (1440, 900, False, "dark"), (390, 844, True, "dark")):
                    viewport(page, vw, vh, mob)
                    page.goto(f"http://127.0.0.1:{port}/teacher/today.html")
                    time.sleep(0.6)
                    B.q(theme_js(theme))
                    ok = open_page(page, sd_url, "!!document.querySelector('[data-mrb-revised]')", timeout=50)
                    tag = f"{vw}-{theme}"
                    if theme == "light" and vw == 1440:
                        rows = B.q("(function(){return [].map.call(document.querySelectorAll('[data-mrb-revised]'),"
                                   "function(e){var r=e.closest('[data-dc-tpl=\"361\"]');return r?r.innerText.replace(/\\s+/g,' '):e.innerText})})()")
                        result["teacher_rows"] = rows
                        joined = " || ".join(rows or [])
                        check(ok and rows and len(rows) == 2 and "Done set" in joined and "4/4" in joined
                              and "Partly set" in joined and "Older set" not in joined,
                              "teacher: 'revised after marking' on the two revised sets (Done 4/4, Partly), "
                              "not on the Older set whose revision was refused", str(rows))
                    B.shot(f"c5-{tag}-12-teacher-row", "[data-mrb-revised]", vw, vh, above=260)
                    B.q(r"""(function(){var e=document.querySelector('[data-mrb-revised]');var r=e&&e.closest('[data-dc-tpl="361"]');if(!r)return;var b=[].slice.call(r.querySelectorAll('button')).find(function(x){return /Breakdown/.test(x.innerText)});if(b)b.click();})()""")
                    ok = B.wait("!!document.querySelector('[data-bd-revised]')", "breakdown revised line", timeout=20)
                    if theme == "light" and vw == 1440:
                        line = B.q("(function(){var e=document.querySelector('[data-bd-revised]');return e?e.innerText:null})()")
                        result["breakdown_line"] = line
                        check(bool(ok) and (line or "").startswith("Revised after marking"),
                              "teacher: the Breakdown's HANDED IN tile says 'Revised after marking <when>'", str(line))
                    B.shot(f"c5-{tag}-13-teacher-breakdown", "[data-bd-revised]", vw, vh, above=300)
        finally:
            server.shutdown()
            server.server_close()
        json.dump(result, open(os.path.join(shots, "result.json"), "w"), indent=1, default=str)
    finally:
        if not a.keep:
            st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest.get('classes', []))})",
                                                      "select": "id"}, as_service=True) \
                if manifest.get("classes") else (200, [])
            manifest["auto_assignments"] = [x["id"] for x in (extra or [])
                                            if x["id"] not in manifest.get("assignments", [])]
            # question rows and attempts under OUR assignments, by id list
            aids = manifest.get("assignments", [])
            if aids:
                st, subs = c.select(None, "assignment_submissions",
                                    {"assignment_id": f"in.({','.join(aids)})", "select": "id"}, as_service=True)
                sub_ids = [x["id"] for x in subs or []]
                if sub_ids:
                    c.write("assignment_question_attempts", "DELETE",
                            {"__match__": f"submission_id=in.({','.join(sub_ids)})"})
                c.write("assignment_questions", "DELETE", {"__match__": f"assignment_id=in.({','.join(aids)})"})
            json.dump(manifest, open(manifest["_path"], "w"), indent=1)
            pf.teardown(c, manifest)
            residue = {}
            for table, ids in (("schools", manifest.get("schools", [])), ("classes", manifest.get("classes", [])),
                               ("assignments", manifest.get("assignments", []))):
                if ids:
                    st, rows = c.select(None, table, {"id": f"in.({','.join(ids)})", "select": "id"}, as_service=True)
                    if rows:
                        residue[table] = len(rows)
            check(not residue, "teardown by snapshotted id list left nothing behind (%s)" % residue)
    print("\n  screenshots: %s" % shots)
    if FAILS:
        print("\n  FAIL — %d check(s)" % len(FAILS))
        for f in FAILS:
            print("    · " + f)
        sys.exit(1)
    print("\n  PASS — sharpen lane P, live on TEST")


if __name__ == "__main__":
    main()
