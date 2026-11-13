#!/usr/bin/env python3
"""activity_save_drive.py — every lesson activity a family child does is
SAVED and comes back on ANOTHER device; a school pupil's page is untouched.

Mide's item 1 (25 Oct 2026). Headless Chrome against the BUILT pages, served
from this checkout, and a FAKE backend in this process that keeps answer
rows the way `child_answers` does and hands them back through
`GET /api/consumer/child/saved` — the same request and response shapes as
consumer/answers.js (POST /api/consumer/child/answer, POST
/api/consumer/child/self-ticks, GET /api/consumer/child/saved). No account,
no database, no network beyond 127.0.0.1 (everything else is blocked).

For each case:
  device A — a family child's session; the drive answers through the page's
             own controls; the answers the page POSTs are recorded.
  device B — a FRESH browser profile (another device: no outbox, no
             localStorage); the page reads /saved and must show the work back,
             and must POST nothing while restoring.
And once per page type, a SCHOOL PUPIL's session with the same presses:
  no POST to /api/consumer/child/*, no capture globals, and the page's DOM
  after the presses byte-identical to the same run with the PREVIOUS
  shared/mrbadmus.v2.js (origin/main c3a30aebd, read from git).

Every recorded body is also checked against the backend's own
validateAnswerBody (MRB_BACKEND_DIR, else the sibling backend checkout) —
so a body the real server would refuse fails here.

    python3 activity_save_drive.py [--only NAME] [--width 1280]
"""
import config_env  # the production hosts, read from shared/config.js
import argparse
import http.server
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.parse

# Every request off this machine is refused; the backend platform is named by config, never here.
OFF_BOX = ["*supabase.co*", "*%s*" % config_env.PROD_BACKEND_PLATFORM, "*mrbadmus.com*", "*googleapis*", "*gstatic*", "*unpkg*", "*jsdelivr*", "*cdnjs*"]

import datetime as _dt
import ks3_browser as KB

REPO = os.path.dirname(os.path.abspath(__file__))
BACKEND = os.environ.get("MRB_BACKEND_DIR") or os.path.join(os.path.dirname(REPO), "mrbadmus---backend")
LEGACY_REF = "c3a30aebd"
AUTH_KEY = "sb-qeppkiswvclkkwbxmlok-auth-token"     # TEST project (127.0.0.1 is TEST in config.js)

# ── the fake backend: child_answers in memory ────────────────────────────
class Ledger:
    def __init__(self):
        self.rows, self.bodies, self.ticks, self.lock = [], [], [], threading.Lock()

    def reset(self):
        with self.lock:
            self.rows, self.bodies, self.ticks = [], [], []


LEDGER = Ledger()
KS3_CFA_PAGE = "/ks3/physics/pressure/pressure-force-over-area.html"
THROTTLE = {"ticks": 0}                 # refuse this many self-tick posts with a 429


def quiz_id(slug, text):
    import hashlib
    import unicodedata
    t = unicodedata.normalize("NFKC", str(text or ""))
    t = re.sub(r"^\s*\d+[.)]\s+", "", t)
    t = re.sub(r"\s+", " ", t).strip().lower()
    return "ks4q:%s:%s" % (slug, hashlib.sha1(t.encode("utf-8")).hexdigest()[:10])


def slug_of(path):
    return (path.rsplit("/", 1)[-1] or "").replace(".html", "")


class Api(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type, Accept")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")

    def _json(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if u.path == "/api/consumer/child/saved":
            path = (urllib.parse.parse_qs(u.query).get("path") or [""])[0]
            ks = "KS3" if path.startswith("/ks3/") else "KS4"
            slug = slug_of(path)
            with LEDGER.lock:
                rows = [dict(r) for r in LEDGER.rows if r["key_stage"] == ks and r["lesson_slug"] == slug]
            return self._json(200, {"ok": True, "ready": True, "key_stage": ks, "lesson_slug": slug, "answers": rows, "tutor": []})
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except ValueError:
            body = {}
        u = urllib.parse.urlparse(self.path)
        if u.path == "/api/consumer/child/answer":
            with LEDGER.lock:
                LEDGER.bodies.append(body)
                if any(r.get("client_event_id") == body.get("client_event_id") for r in LEDGER.rows):
                    return self._json(200, {"ok": True, "duplicate": True})
                slug = body.get("lesson_slug") or slug_of(body.get("path") or "")
                qid = body.get("question_id") or quiz_id(slug, body.get("question_text"))
                att = 1 + sum(1 for r in LEDGER.rows if r["question_id"] == qid)
                self_checked = body.get("self_checked") is True
                LEDGER.rows.append({
                    "question_id": qid, "rung": body.get("rung"), "answer_kind": body.get("kind"),
                    "question_text": body.get("question_text"), "answer": body.get("answer"),
                    "correct_answer": body.get("correct_answer"),
                    "is_correct": None if self_checked else body.get("is_correct"),
                    "marks_scored": body.get("marks_scored"), "marks_available": body.get("marks") or 1,
                    "points_hit": None, "points_total": None, "feedback": None, "mark_level": None,
                    "mark_next_step": None, "marked_by": "key" if (not self_checked and body.get("is_correct") is not None) else "unmarked",
                    "self_ticks": None, "attempt_no": att, "answered_at": body.get("answered_at"),
                    "surface": "lesson", "work_item_id": None,
                    "key_stage": body.get("key_stage"), "lesson_slug": slug, "client_event_id": body.get("client_event_id"),
                })
            return self._json(200, {"ok": True})
        if u.path == "/api/consumer/child/self-ticks":
            if THROTTLE["ticks"] > 0:
                THROTTLE["ticks"] -= 1
                return self._json(429, {"error": "too_many", "retry_after_s": 1})
            with LEDGER.lock:
                LEDGER.ticks.append(body)
                hit = [r for r in LEDGER.rows if r["question_id"] == body.get("question_id")]
                if not hit:
                    return self._json(404, {"error": "no_answer"})
                hit[-1]["self_ticks"] = sorted(set((body.get("ticks") or []) + ([100 + body["level"]] if isinstance(body.get("level"), int) else [])))
            return self._json(200, {"ok": True, "ticks": hit[-1]["self_ticks"]})
        self.send_response(204)
        self._cors()
        self.end_headers()


# ── the site, with the previous capture code on demand ──────────────────
LEGACY = {"on": False}
SLOW = {"path": None, "secs": 2.0}       # one script held back, as a slow line would
_LEGACY_JS = None


def legacy_js():
    global _LEGACY_JS
    if _LEGACY_JS is None:
        _LEGACY_JS = subprocess.run(["git", "-C", REPO, "show", LEGACY_REF + ":shared/mrbadmus.v2.js"],
                                    capture_output=True, check=True).stdout
    return _LEGACY_JS


class Site(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=REPO, **kw)

    def log_message(self, *a):
        pass

    def do_GET(self):
        if SLOW["path"] and urllib.parse.urlparse(self.path).path == SLOW["path"]:
            time.sleep(SLOW["secs"])
        if LEGACY["on"] and urllib.parse.urlparse(self.path).path == "/shared/mrbadmus.v2.js":
            b = legacy_js()
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript")
            self.send_header("Content-Length", str(len(b)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(b)
            return
        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def start(handler):
    s = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    s.daemon_threads = True
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s, s.server_address[1]


# ── the cases ────────────────────────────────────────────────────────────
# `act`: JS run on device A (returns anything; may be a promise).
# `want`: ids that must be POSTed (prefix match with '*').
# `back`: JS run on device B once restored; must return true.
# A helper library is injected first (H.*).
HELPERS = r"""
window.H = {
  sleep: function (ms) { return new Promise(function (r) { setTimeout(r, ms); }); },
  rootBtn: function (label, nth) {
    var host = document.getElementById('ks4-mount');
    var owned = function (el) { for (var u = el.parentNode; u; u = u.parentNode) { if (u.__mrbKs4) { return u === host; } } return false; };
    var list = Array.prototype.filter.call(host.querySelectorAll('button, [tabindex]'), function (b) {
      return owned(b) && (b.textContent || '').replace(/\s+/g, ' ').indexOf(label) >= 0;
    });
    return list[nth || 0] || null;
  },
  click: function (el) { if (!el) { throw new Error('nothing to click'); } el.scrollIntoView({ block: 'center' }); el.click(); return true; },
  sec: function (act) { return document.querySelector('[data-activity="' + act + '"]'); },
  btnIn: function (root, sel, label) {
    var list = Array.prototype.filter.call(root.querySelectorAll(sel), function (b) { return !label || (b.textContent || '').replace(/\s+/g, ' ').indexOf(label) >= 0; });
    return list[0] || null;
  },
  pressed: function (el) { return !!el && el.getAttribute('aria-pressed') === 'true'; },
  write: function () {
    var out = null;
    Array.prototype.forEach.call(document.querySelectorAll('[data-dc-tpl]'), function (el) {
      var a = el.__mrbKs4;
      if (!out && a && a.comp === 'Ks4Write' && (a.logic.props.levels || []).length && el.querySelector('textarea')) { out = a; }
    });
    return out;
  },
  rootState: function () { return document.getElementById('ks4-mount').__mrbKs4.logic.state; },
  L: function () { return document.getElementById('ks4-mount').__mrbKs4.logic; },
  v: function () { return H.L().renderVals(); },
  // A lesson's own handler, as its control calls it, then a draw so the tap sees the step.
  call: async function (get, arg) { var f = typeof get === 'string' ? H.v()[get] : get(H.v()); if (typeof f !== 'function') { throw new Error('no handler ' + get); } f(arg === undefined ? { target: { value: '' } } : arg); await H.sleep(90); },
  val: function (v) { return { target: { value: v } }; },
  set: async function (p) { H.L().setState(p); await H.sleep(90); },
  // Real controls, for the cases that prove the DOM path.
  exact: function (label) {
    var host = document.getElementById('ks4-mount');
    var list = Array.prototype.filter.call(host.querySelectorAll('button'), function (b) { return (b.textContent || '').replace(/\s+/g, ' ').trim() === label; });
    return list[0] || null;
  },
  // An option by its own label, whatever letter is drawn in front of it: a short label
  // like "1" is inside other buttons' words, and which ones differs by width.
  opt: function (label) {
    var host = document.getElementById('ks4-mount');
    return Array.prototype.filter.call(host.querySelectorAll('button'), function (b) { return (b.textContent || '').replace(/\\s+/g, ' ').trim().replace(/^[A-E] ?(?=.)/, '') === label; })[0] || null;
  },
  type: async function (el, v) { el.scrollIntoView({ block: 'center' }); el.value = v; el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); await H.sleep(90); },
  block: function (name) {
    var host = document.getElementById('ks4-mount'), out = null;
    Array.prototype.forEach.call(host.querySelectorAll('[data-dc-tpl]'), function (el) {
      var a = el.__mrbKs4;
      if (out || !a || a.comp !== name) { return; }
      for (var u = el.parentNode; u; u = u.parentNode) { if (u.__mrbKs4) { if (u === host) { out = a; } return; } }
    });
    return out;
  }
};
"""

KS4 = "/combined/higher/biology/ecology/"
CASES = [
    # ── KS4: a lesson's own activities ──
    dict(name="ks4-flag-pick", page=KS4 + "abiotic-biotic-factors.html",
         act="H.click(H.rootBtn('A new predator')); await H.sleep(400); H.click(H.rootBtn('A new pathogen')); await H.sleep(400);",
         want=["ks4:abiotic-biotic-factors:ch#bq", "ks4:abiotic-biotic-factors:ch#bq"],
         check=lambda b: [x for x in b if x["question_id"] == "ks4:abiotic-biotic-factors:ch#bq"][0]["is_correct"] is False
                         and [x for x in b if x["question_id"] == "ks4:abiotic-biotic-factors:ch#bq"][1]["is_correct"] is True,
         back="H.rootState().bq === 0 && H.rootState().bqOk === true"),
    dict(name="ks4-words-pick", page="/combined/higher/biology/cell-biology/animal-plant-cells.html",
         act="H.click(H.rootBtn('Most of it, about three quarters')); await H.sleep(400);",
         want=["ks4:animal-plant-cells:ch#est"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#est")][0]["is_correct"] is True,
         back="H.rootState().est === 2"),
    dict(name="ks4-gate", page=KS4 + "ecosystems.html",
         act="H.click(H.rootBtn('community')); await H.sleep(400); H.click(H.rootBtn('population')); await H.sleep(400);",
         want=["ks4:ecosystems:ch#lv-1", "ks4:ecosystems:ch#lv-1"],
         check=lambda b: [x["is_correct"] for x in b if x["question_id"] == "ks4:ecosystems:ch#lv-1"] == [False, True],
         back="H.rootState().lv === 1"),
    dict(name="ks4-prediction-map", page="/combined/higher/biology/cell-biology/chromosomes-mitosis.html",
         act="""H.click(H.rootBtn('It grows, makes more ribosomes')); await H.sleep(300);
                var q = H.v().cyQs; for (var i = 1; i < q.length; i += 1) { H.click(H.rootBtn(H.v().cyQs[i].opts[0].label, 0)); await H.sleep(200); }
                await H.call('onCyRun'); await H.sleep(300);""",
         want=["ks4:chromosomes-mitosis:ch#preds-1-1"],
         check=lambda b: isinstance([x for x in b if x["question_id"].endswith("#preds-1-1")][0]["is_correct"], bool)
                         and bool([x for x in b if x["question_id"].endswith("#preds-1-1")][0]["correct_answer"]),
         back="H.rootState().preds[0][0] === 0 && H.rootState().revealed[0] === true"),
    dict(name="ks4-level-pick", page="/triple/higher/biology/inheritance/advantages-sexual-asexual.html",
         act="""var w = H.write(); if (!w) { throw new Error('no level-marked write'); }
                var ta = w.host.querySelector('textarea'); ta.scrollIntoView({block:'center'});
                ta.value = 'Sexual reproduction gives variation so some offspring may survive a change, while asexual reproduction is faster and needs only one parent.';
                ta.dispatchEvent(new Event('input', {bubbles: true})); await H.sleep(300);
                H.click(H.btnIn(w.host, 'button', 'Show the mark scheme')); await H.sleep(500);
                var lv = Array.prototype.filter.call(w.host.querySelectorAll('button'), function (b) { return /Level 1/.test(b.textContent); })[0];
                H.click(lv); await H.sleep(1500); window.__lv = (w.logic.props.levels || []).length;""",
         want=["ks4:advantages-sexual-asexual:th#*"],
         ticks=True,
         back="(function(){ var w = H.write(); return !!w && w.logic.state.open === true && typeof w.logic.state.level === 'number' && /Level 1/.test(w.logic.props.levels[w.logic.state.level].label); })()"),
    # ── item 5: "Your turn" reopens where the child was; the practice set keeps an answered Q5 open ──
    dict(name="ks4-yourturn-tab", page="/combined/higher/biology/cell-biology/eukaryotes-prokaryotes.html",
         act="""var cf = H.block('Ks4Cfifa'); var ins = cf.host.querySelectorAll('input');
                var vals = ['Nothing to convert before substituting', 'Actual size = Image size ÷ Magnification', 'A = 36 ÷ 600', 'A = 0.06 mm; × 1000 = 60', 'Actual size = 60 µm'];
                for (var i = 0; i < ins.length && i < 5; i += 1) { ins[i].value = vals[i]; ins[i].dispatchEvent(new Event('input', {bubbles: true})); await H.sleep(60); }
                await H.sleep(200); H.click(H.btnIn(cf.host, 'button', 'Check your working')); await H.sleep(800);""",
         want=["ks4:eukaryotes-prokaryotes:ch#cfifa-1-1"],
         back="(function(){ var cf = H.block('Ks4Cfifa'); var s = cf.logic.state; return s.qEx === 1 && !!s.q[0] && s.q[0].open === true; })()"),
    dict(name="ks4-quizbank-fold", page="/combined/higher/biology/cell-biology/eukaryotes-prokaryotes.html",
         act="""var qb = H.block('Ks4QuizBank'); H.click(H.btnIn(qb.host, 'button', 'Show 1 more')); await H.sleep(500);
                var lis = qb.host.querySelectorAll('li'); H.click(lis[4].querySelector('button')); await H.sleep(300);
                H.click(qb.host.querySelectorAll('li')[0].querySelector('button')); await H.sleep(500);""",
         want=[],
         check=lambda b: sum(1 for x in b if x.get("question_id") is None and x.get("kind") == "choice") == 2,
         back="(function(){ var qb = H.block('Ks4QuizBank'); var s = qb.logic.state; return s.picks[4] !== undefined && s.picks[0] !== undefined && s.shown >= 5 && qb.host.querySelectorAll('li').length >= 5; })()"),
    # ── ⊕ 8 Nov 2026: what the option-group classifier cannot see (ROOT_FORMS) ──
    # Typed, through the page's real input and real button.
    dict(name="ks4-typed-rate", page="/triple/higher/biology/ecology/decomposition.html", forms=True,
         act="""H.click(document.querySelector('#ks4-mount [aria-label^="Graph A"]')); await H.sleep(200);
                await H.set({ own: { 20: 300, 30: 180, 40: 100, 50: 150, 60: null } });
                await H.type(document.getElementById('dec-rate'), '0.01');
                H.click(H.exact('Check')); await H.sleep(300);""",
         want=["ks4:decomposition:th#rate", "ks4:decomposition:th#own-40", "ks4:decomposition:th#own-60"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#rate")][0]["kind"] == "numeric"
                         and [x for x in b if x["question_id"].endswith("#rate")][0]["is_correct"] is True
                         and [x for x in b if x["question_id"].endswith("#own-60")][0]["answer"] == "Over 600 s",
         back="(function(){ var s = H.rootState(), el = document.getElementById('dec-rate'); return s.rate === '0.01' && s.rateChecked && s.own[40] === 100 && s.own[60] === null && !!el && el.value === '0.01'; })()"),
    # Selected and judged at once, then typed.
    dict(name="ks4-select-anom", page="/triple/higher/biology/organisation/enzymes.html", forms=True,
         act="""H.click(document.querySelector('#ks4-mount [aria-label^="Graph A"]')); await H.sleep(200);
                var own = {}; H.v().phTabs.forEach(function (t) { own[+t.label.replace('pH ', '')] = 120; }); await H.set({ own: own });
                var L = H.L(), right = null; H.v().anomOpts.forEach(function (o) { L.state.anom = o.value; if (o.value && /^Yes/.test(L.renderVals().anomWord)) { right = o.value; } }); L.state.anom = '';
                await H.type(document.getElementById('enz-anom'), right);
                await H.call('onMean', H.val('105')); await H.call('onMeanCheck'); await H.sleep(200);""",
         want=["ks4:enzymes:th#anom", "ks4:enzymes:th#mean"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#anom")][0]["is_correct"] is True
                         and bool([x for x in b if x["question_id"].endswith("#anom")][0]["correct_answer"])
                         and [x for x in b if x["question_id"].endswith("#mean")][0]["is_correct"] is True,
         back="(function(){ var s = H.rootState(), el = document.getElementById('enz-anom'); return s.anom !== '' && s.mean === '105' && s.meanChecked && s.own[6] === 120 && /^Yes/.test(H.v().anomWord) && !!el && el.value === s.anom; })()"),
    dict(name="ks4-states-lab", page="/triple/higher/chemistry/bonding/states-of-matter.html", forms=True,
         act="""await H.set({ n: 21 }); await H.type(document.getElementById('anom'), '4');
                await H.type(document.getElementById('mp'), '69'); H.click(H.exact('Check')); await H.sleep(300);""",
         want=["ks4:states-of-matter:th#anom", "ks4:states-of-matter:th#mp"],
         check=lambda b: all(x["is_correct"] is True for x in b),
         back="(function(){ var s = H.rootState(); return s.n >= 21 && String(s.anom) === '4' && s.mp === '69' && s.mpChecked === true; })()"),
    dict(name="ks4-typed-formula", page="/triple/higher/chemistry/bonding/ionic-compounds.html", forms=True,
         act="""H.click(H.exact('6')); await H.sleep(200); await H.call('onDx', H.val('wrong')); await H.call('onDxCheck');
                await H.call(function (v) { return v.dxTabs[1].onClick; }); await H.call('onDx', H.val('X2Y')); await H.call('onDxCheck'); await H.sleep(200);""",
         want=["ks4:ionic-compounds:th#lenspick", "ks4:ionic-compounds:th#dxval-1", "ks4:ionic-compounds:th#dxval-2"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#dxval-1")][0]["is_correct"] is False
                         and [x for x in b if x["question_id"].endswith("#lenspick")][0]["correct_answer"] == "6",
         back="(function(){ var s = H.rootState(); return s.lensPick === 6 && s.dxVal[0] === 'wrong' && s.dxVal[1] === 'X2Y' && s.dx === 1 && s.dxChecked === true; })()"),
    # A list of picks, a form, and a builder, all in one lesson.
    dict(name="ks4-list-of-picks", page="/triple/higher/chemistry/bonding/ionic-bonding.html", forms=True,
         act="""await H.call(function (v) { return v.wOptions[0].onClick; }); await H.call(function (v) { return v.wOptions[1].onClick; }); await H.call(function (v) { return v.wOptions[0].onClick; });
                await H.call('onMore'); await H.call('onMq', H.val('1')); await H.call('onXq', H.val('-1')); await H.call('onDCheck');
                await H.call('onNextF'); await H.call('onAddM'); await H.call('onAddX'); await H.call('onAddX'); await H.sleep(200);""",
         want=["ks4:ionic-bonding:th#wa-1-1", "ks4:ionic-bonding:th#wa-1-2", "ks4:ionic-bonding:th#wa-1-3", "ks4:ionic-bonding:th#draw-1"],
         # The three steps' right answers are not all first: pressing A, B, A is right, wrong, wrong.
         check=lambda b: [[x for x in b if x["question_id"].endswith("#wa-1-%d" % n)][0]["is_correct"] for n in (1, 2, 3)] == [True, False, False],
         back="(function(){ var s = H.rootState(); return s.wa[0].length === 3 && s.wa[0][1] === 1 && s.moved === 1 && s.mq === '1' && s.xq === '-1' && s.dChecked === true; })()"),
    dict(name="ks4-builder-formula", page="/triple/higher/chemistry/bonding/ionic-bonding.html", forms=True,
         act="""await H.call('onNextF');
                var ok = function () { return /^Formula:/.test(String(H.v().fDone)); };
                for (var m = 1; m <= 6 && !ok(); m += 1) { for (var x = 1; x <= 6 && !ok(); x += 1) { await H.set({ fm: m, fx: x }); } }
                await H.sleep(200);""",
         want=["ks4:ionic-bonding:th#formula-2"],
         check=lambda b: [x for x in b if "#formula-" in x["question_id"]][-1]["is_correct"] is True,
         back="(function(){ var s = H.rootState(); return s.f === 1 && s.fm > 0 && s.fx > 0 && /^Formula:/.test(String(H.v().fDone)); })()"),
    dict(name="ks4-select-labels", page="/triple/higher/biology/ecology/carbon-cycle.html", forms=True,
         act="""var rows = H.v().lRows; for (var i = 0; i < rows.length; i += 1) { var el = document.getElementById(rows[i].id); await H.type(el, el.options[1].value); }
                await H.call('onLCheck'); await H.sleep(200);""",
         want=["ks4:carbon-cycle:th#labels-a", "ks4:carbon-cycle:th#labels-i"],
         back="(function(){ var s = H.rootState(); return s.lChecked === true && Object.keys(s.labels).length === 9 && document.getElementById(H.v().lRows[0].id).value === s.labels[H.v().lRows[0].letter]; })()"),
    dict(name="ks4-form-pan", page="/triple/higher/chemistry/quantitative/relative-formula-mass.html", forms=True,
         act="""await H.call(function (v) { return v.panOpts[0].onClick; }); await H.call('onPanL', H.val('10')); await H.call('onPanR', H.val('20')); await H.call('onLoad'); await H.sleep(200);""",
         want=["ks4:relative-formula-mass:th#pan-1"],
         check=lambda b: b[-1]["is_correct"] is False and b[-1]["answer"].count("\n") == 2,
         back="(function(){ var s = H.rootState(); return s.pp[0] === 0 && s.pv[0].l === '10' && s.pv[0].r === '20' && s.pd[0] === true; })()"),
    dict(name="ks4-form-latent", page="/triple/higher/physics/particle-model/specific-latent-heat.html", forms=True,
         act="""await H.set({ gate: 0 }); await H.call(function (v) { return v.stageOpts[0].onClick; }); await H.set({ done: { 0: true } }); await H.sleep(100);
                await H.set({ logDone: true, ans: { 0: 0, 1: 0 } }); await H.call('onLText', H.val('123')); await H.call(function (v) { return v.lUnits[0].onClick; }); await H.call('onLCheck'); await H.sleep(200);""",
         want=["ks4:specific-latent-heat:th#picks-1", "ks4:specific-latent-heat:th#ltext"],
         back="(function(){ var s = H.rootState(); return s.picks[0] === 0 && s.done[0] === true && s.lText === '123' && s.lUnit === 0 && s.lCode !== null && s.lTries === 1 && s.logDone === true; })()"),
    dict(name="ks4-form-shc", page="/triple/higher/physics/particle-model/temperature-changes-shc.html", forms=True,
         act="""var c = H.v().raceCards; for (var i = 0; i < 4; i += 1) { await H.call((function (j) { return function (v) { return v.raceCards[j].onClick; }; })(i)); }
                await H.set({ raceDone: true, raceP: 1 }); await H.set({ gate: 0, phase: 'off', simT: 60 }); await H.call(function (v) { return v.offOpts[0].onClick; }); await H.sleep(120);
                await H.set({ phase: 'done', cText: '500' }); await H.call('onCCheck'); await H.sleep(200);""",
         want=["ks4:temperature-changes-shc:th#order", "ks4:temperature-changes-shc:th#offpick", "ks4:temperature-changes-shc:th#ctext"],
         back="(function(){ var s = H.rootState(); return s.order.length === 4 && s.raceDone === true && s.offPick === 0 && s.phase === 'done' && s.cText === '500' && s.cCode !== null; })()"),
    dict(name="ks4-form-round", page="/triple/higher/physics/energy/changes-in-energy.html", forms=True,
         retired="the lean rebuild (Wave 0) took the practice round off the page",
         absent=['"e": "roundOpts"'],
         act="await H.call(function (v) { return v.roundOpts[1].onClick; }); await H.call('onReveal'); await H.sleep(200);",
         want=["ks4:changes-in-energy:th#picks-1"],
         back="(function(){ var s = H.rootState(); return s.picks[0] === 1 && s.revealed[0] === true; })()"),
    dict(name="ks4-form-power", page="/triple/higher/physics/energy/power.html", forms=True,
         retired="the lean rebuild (Wave 0) took the practice round off the page",
         absent=['"e": "roundOpts"'],
         act="await H.call(function (v) { return v.roundOpts[0].onClick; }); await H.set({ revealed: { 0: true } }); await H.sleep(200);",
         want=["ks4:power:th#picks-1"],
         back="(function(){ var s = H.rootState(); return s.picks[0] === 0 && s.revealed[0] === true; })()"),
    dict(name="ks4-form-internal", page="/triple/higher/physics/particle-model/internal-energy.html", forms=True,
         act="await H.call(function (v) { return v.stageOpts[0].onClick; }); await H.set({ done: { 0: true } }); await H.sleep(200);",
         want=["ks4:internal-energy:th#picks-1"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool),
         back="(function(){ var s = H.rootState(); return s.picks[0] === 0 && s.done[0] === true; })()"),
    dict(name="ks4-form-piston", page="/triple/higher/physics/particle-model/particle-motion-pressure.html", forms=True,
         act="""await H.call(function (v) { return v.bOpts[0].onClick; }); await H.set({ bDone: { 0: true } });
                await H.call(function (v) { return v.p3Opts[0].onClick; }); await H.set({ p3Done: true }); await H.sleep(200);""",
         want=["ks4:particle-motion-pressure:th#bpick-1", "ks4:particle-motion-pressure:th#p3"],
         back="(function(){ var s = H.rootState(); return s.bPick[0] === 0 && s.bDone[0] === true && s.p3Pick === 0 && s.p3Done === true; })()"),
    dict(name="ks4-form-reports", page="/triple/higher/chemistry/atmosphere/greenhouse-gases.html", forms=True,
         act="""var q = H.v().repQs; for (var i = 0; i < q.length; i += 1) { await H.call((function (k) { return function (v) { return v.repQs[k].options[0].onClick; }; })(i)); }
                await H.call('onRepCheck'); await H.sleep(200);""",
         want=["ks4:greenhouse-gases:th#rep-1", "ks4:greenhouse-gases:th#rep-2"],
         check=lambda b: all(isinstance(x["is_correct"], bool) for x in b),
         back="(function(){ var s = H.rootState(); return Object.keys(s.rep).length === H.v().repQs.length && s.repChecked === true; })()"),
    dict(name="ks4-form-tubes", page="/triple/higher/chemistry/analysis/metal-hydroxides.html", forms=True,
         act="""await H.call(function (v) { return v.askOptions[0].onClick; }); await H.sleep(2100);
                var ip = H.v().ionParts; for (var i = 0; i < ip.length; i += 1) { await H.call((function (k) { return function (v) { return v.ionParts[k].options[0].onClick; }; })(i)); }
                await H.call('onIonCheck');
                var fp = H.v().forgeItems[0].parts; for (var j = 0; j < fp.length; j += 1) { await H.call((function (k) { return function (v) { return v.forgeItems[0].parts[k].options[0].onClick; }; })(j)); }
                await H.call(function (v) { return v.forgeItems[0].onCheck; }); await H.sleep(200);""",
         want=["ks4:metal-hydroxides:th#rec-cu-p1", "ks4:metal-hydroxides:th#ion", "ks4:metal-hydroxides:th#forge-1"],
         check=lambda b: all(isinstance(x["is_correct"], bool) for x in b),
         back="(function(){ var s = H.rootState(); return s.rec.cu && s.rec.cu.p1 === 'blue' && s.rec.cu.s1 === 'done' && s.ion.checked === true && Object.keys(s.ion.picks).length > 0 && Object.keys(s.forge).length === 1; })()"),
    dict(name="ks4-form-tube-id", page="/triple/higher/chemistry/analysis/metal-hydroxides.html", forms=True,
         act="""await H.set({ cur: 'al' }); await H.call(function (v) { return v.askOptions[3].onClick; }); await H.sleep(2000);
                await H.call(function (v) { return v.askOptions[0].onClick; }); await H.sleep(2000);
                await H.set({ cur: 'X' }); await H.call(function (v) { return v.actions[0].onClick; }); await H.sleep(2000);
                await H.call(function (v) { return v.askOptions[0].onClick; }); await H.sleep(300);""",
         want=["ks4:metal-hydroxides:th#rec-al-p1", "ks4:metal-hydroxides:th#rec-al-p2", "ks4:metal-hydroxides:th#rec-x-id"],
         check=lambda b: all(isinstance(x["is_correct"], bool) for x in b),
         back="(function(){ var s = H.rootState(); return s.rec.al && s.rec.al.p1 === 'white' && s.rec.al.s2 === 'done' && !!s.rec.al.p2 && s.rec.X && !!s.rec.X.last && s.cur === 'X'; })()"),
    dict(name="ks4-form-piston-push", page="/triple/higher/physics/particle-model/particle-motion-pressure.html", forms=True,
         act="""await H.call(function (v) { return v.p3Opts[0].onClick; }); await H.set({ p3Done: true }); await H.call(function (v) { return v.p4Opts[1].onClick; }); await H.set({ p4Done: true, p4Started: true }); await H.sleep(200);""",
         want=["ks4:particle-motion-pressure:th#p4"],
         back="(function(){ var s = H.rootState(); return s.p3Done === true && s.p4Pick === 1 && s.p4Done === true; })()"),
    dict(name="ks4-form-products", page="/triple/higher/chemistry/atmosphere/atmospheric-pollutants.html", forms=True,
         act="await H.call(function (v) { return v.products[0].onClick; }); await H.call(function (v) { return v.products[1].onClick; }); await H.call('onCheck'); await H.sleep(200);",
         want=["ks4:atmospheric-pollutants:th#products-1"],
         check=lambda b: b[-1]["answer"].count("\n") == 1 and isinstance(b[-1]["is_correct"], bool),
         back="(function(){ var s = H.rootState(); return Object.keys(s.picks).length === 2 && s.checked === true; })()"),
    # Builders: steppers read at their Check.
    dict(name="ks4-builder-balance", page="/triple/higher/chemistry/atomic-structure/atoms-elements-compounds.html", forms=True,
         act="""await H.call(function (v) { return v.balTerms.filter(function (t) { return t.isSpecies; })[0].onUp || v.balTerms.filter(function (t) { return t.isSpecies; })[0].up; }); await H.call('onBalCheck'); await H.sleep(200);""",
         want=["ks4:atoms-elements-compounds:th#bv-1"],
         back="(function(){ var s = H.rootState(); return !!s.bc[0] && s.bc[0][0] === 2 && !!s.bv[0]; })()"),
    dict(name="ks4-builder-chips", page="/triple/higher/chemistry/analysis/carbonates-halides-sulfates.html", forms=True,
         act="await H.call(function (v) { return v.specItems[0].chips[0].onClick; }); await H.call(function (v) { return v.specItems[0].onCheck; }); await H.sleep(200);",
         want=["ks4:carbonates-halides-sulfates:th#spec-1"],
         back="(function(){ var s = H.rootState(); return !!s.spec[0] && s.spec[0].checked === true && s.spec[0].marks[0] === true; })()"),
    dict(name="ks4-builder-bonds", page="/triple/higher/chemistry/bonding/covalent-bonding.html", forms=True,
         act="await H.call(function (v) { return v.bBonds[0].onMore; }); await H.call('onBCheck'); await H.sleep(200);",
         want=["ks4:covalent-bonding:th#orders-5"],
         back="(function(){ return H.rootState().bChecked === true && /^1 /.test(H.v().bBonds[0].value); })()"),
    dict(name="ks4-builder-atom", page="/triple/higher/physics/atomic-structure/structure-of-atom.html", forms=True,
         act="await H.set({ p: 5, e: 6 }); await H.call(function (v) { return v.counters[0].inc; }); await H.sleep(200);",
         want=["ks4:structure-of-atom:th#built"],
         back="(function(){ var s = H.rootState(); return s.built === true && s.p === 6 && s.e === 6; })()"),
    # Choices the classifier could not tie to one place.
    dict(name="ks4-choice-verdict", page="/triple/higher/chemistry/atomic-structure/metals-non-metals.html", forms=True,
         act="await H.call(function (v) { return v.verdicts[1].onClick; }); await H.sleep(200);",
         want=["ks4:metals-non-metals:th#verdict-1"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool),
         back="(function(){ return H.rootState().verdict[0] === false; })()"),
    dict(name="ks4-choice-predict", page="/triple/higher/chemistry/chemical-changes/reactivity-series.html", forms=True,
         act="await H.call(function (v) { return v.predicts[0].onClick; }); await H.sleep(200);",
         want=["ks4:reactivity-series:th#pred-*"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool),
         back="(function(){ var s = H.rootState(); return s.pred === true && s.swaps === 1; })()"),
    dict(name="ks4-rank", page="/triple/higher/chemistry/bonding/properties-small-molecules.html", forms=True,
         act="""await H.call(function (v) { return v.gateOpts[0].onClick; });
                var n = H.v().rankPool.length; for (var i = 0; i < n; i += 1) { await H.call((function (j) { return function (v) { return v.rankPool[j].onClick; }; })(i)); }
                await H.call('onRankCheck'); await H.sleep(200);""",
         want=["ks4:properties-small-molecules:th#gate", "ks4:properties-small-molecules:th#rank"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#gate")][0]["is_correct"] is True,
         back="(function(){ var s = H.rootState(); return s.gate === 0 && s.order.length === 4 && s.rankChecked === true; })()"),
    dict(name="ks4-predict-wall", page="/triple/higher/physics/energy/thermal-conductivity.html", forms=True,
         retired="the lean rebuild (Wave 0) took the wall prediction off the page",
         absent=['"e": "changes"', '"e": "predictions"'],
         act="await H.call(function (v) { return v.changes[0].onClick; }); await H.call(function (v) { return v.predictions[0].onClick; }); await H.sleep(200);",
         want=["ks4:thermal-conductivity:th#tries-1-1"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool),
         back="(function(){ var s = H.rootState(); return s.tries === 1 && !!s.pred && s.pred.pick === 'Faster'; })()"),
    dict(name="ks4-order-spectrum", page="/triple/higher/physics/waves/types-of-em-waves.html", forms=True,
         act="""var n = H.v().tray.length; for (var i = 0; i < n; i += 1) { await H.call(function (v) { return v.tray[0].onClick; }); } await H.call('onP1'); await H.sleep(200);""",
         want=["ks4:types-of-em-waves:th#placed"],
         back="(function(){ var s = H.rootState(); return s.p1 === true && s.placed.length === 7; })()"),
    dict(name="ks4-predict-rough", page="/triple/higher/chemistry/chemical-changes/titrations.html", forms=True,
         act="await H.call(function (v) { return v.gateOpts[0].onClick; }); await H.sleep(200);",
         want=["ks4:titrations:th#gate"],
         back="(function(){ return H.rootState().gate === 0; })()"),
    dict(name="ks4-predict-atoms", page="/triple/higher/chemistry/bonding/polymers.html", forms=True,
         act="await H.call(function (v) { return v.apOpts[0].onClick; }); await H.sleep(200);",
         want=["ks4:polymers:th#appick"],
         check=lambda b: b[-1]["is_correct"] is True,
         back="(function(){ return H.rootState().apPick === 0; })()"),
    dict(name="ks4-pair-bond", page="/triple/higher/chemistry/bonding/chemical-bonds.html", forms=True,
         act="""await H.call(function (v) { return v.cells[0].onClick; }); await H.call(function (v) { return v.cells[1].onClick; });
                H.click(H.exact('Covalent') || H.exact(H.v().predictButtons[1].label)); await H.sleep(1300);""",
         want=["ks4:chemical-bonds:th#pair-*"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool) and b[-1]["answer"],
         back="(function(){ var s = H.rootState(); return s.pick.length === 2 && s.pred !== null; })()"),
    # ── ⊕ 8 Nov 2026: the titration bench, and verdicts that must come back without a press ──
    dict(name="ks4-bench-titration", page="/triple/higher/chemistry/chemical-changes/titrations.html", forms=True,
         act="""await H.call(function (v) { return v.gateOpts[0].onClick; });
                var runs = [2500, 2475, 2510, 2470];
                for (var i = 0; i < runs.length; i += 1) {
                  await H.set({ added: runs[i], shown: runs[i] }); await H.call('onRecord');
                  if (i < runs.length - 1) { await H.call('onNextRun'); }
                }
                await H.call(function (v) { return v.rowBtns[1].onClick; }); await H.call(function (v) { return v.rowBtns[3].onClick; });
                await H.call('onPickCheck'); await H.sleep(200);""",
         want=["ks4:titrations:th#gate", "ks4:titrations:th#rows-1", "ks4:titrations:th#rows-2", "ks4:titrations:th#rows-4", "ks4:titrations:th#concord"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#concord")][0]["is_correct"] is True
                         and [x for x in b if x["question_id"].endswith("#rows-2")][0]["kind"] == "numeric"
                         and "24.75" in [x for x in b if x["question_id"].endswith("#rows-2")][0]["answer"],
         back="""(function(){ var s = H.rootState(); return s.rows.length === 4 && s.rows[1].titre === 2475 && s.rows[1].run === 1 && s.rows[3].titre === 2470 && !s.rows[1].over && !!s.sel[1] && !!s.sel[3] && !!s.pick && s.pick.ok === true; })()"""),
    dict(name="ks4-reveal-check", page="/triple/higher/chemistry/quantitative/conservation-of-mass.html", forms=True,
         act="""H.click(H.rootBtn(H.v().w1Options[0].label)); await H.sleep(400); H.click(H.opt(H.v().w2Options[0].label)); await H.sleep(400);
                var n = H.v().w3Rows.length; for (var i = 0; i < n; i += 1) { H.click(document.querySelector('#ks4-mount button[aria-label="' + H.v().w3Rows[i].options[0].aria + '"]')); await H.sleep(120); }
                await H.call('onW3Check'); await H.sleep(200);""",
         want=["ks4:conservation-of-mass:th#w3-1"],
         back="""(function(){ var s = H.rootState(); return s.w3Checked === true && Object.keys(s.w3).length === H.v().w3Rows.length && H.v().w3Checked === true; })()"""),
    dict(name="ks4-reveal-circuit", page="/triple/higher/physics/electricity/series-parallel-circuits.html", forms=True,
         act="""H.click(H.rootBtn(H.v().qs[0].opts[0].label, 0)); await H.sleep(150); H.click(H.rootBtn(H.v().qs[1].opts[1].label, 1)); await H.sleep(150); await H.call('onReveal'); await H.sleep(200);""",
         want=["ks4:series-parallel-circuits:th#preds-*"],
         check=lambda b: all(isinstance(x["is_correct"], bool) and x["correct_answer"] and x["self_checked"] is False for x in b if "#preds-" in x["question_id"]),
         back="""(function(){ var s = H.rootState(); return s.revealed[s.step] === true && H.v().revealed === true && s.preds[s.step][1] === 1; })()"""),
    dict(name="ks4-reveal-waves", page="/triple/higher/physics/waves/waves-detection-exploration.html", forms=True,
         act="""H.click(H.rootBtn(H.v().qOpts[0].text)); await H.sleep(150); await H.call('onQReveal'); H.click(H.rootBtn(H.v().uOpts[1].text)); await H.sleep(150); await H.call('onUReveal'); await H.sleep(200);""",
         want=["ks4:waves-detection-exploration:th#qpred-*", "ks4:waves-detection-exploration:th#upred-*"],
         check=lambda b: all(isinstance(x["is_correct"], bool) and x["correct_answer"] for x in b if "pred-" in x["question_id"]),
         back="""(function(){ var v = H.v(), s = H.rootState(); return v.qShown === true && v.uShown === true && s.qPred[s.qStage] === 0 && s.uPred[s.uStage] === 1; })()"""),
    dict(name="ks4-reveal-sound", page="/triple/higher/physics/waves/sound-waves-hearing.html", forms=True,
         act="""H.click(H.rootBtn(H.v().pOpts[0].text)); await H.sleep(150); await H.call('onPReveal');
                var st = 1; for (var k = 1; k <= 4 && !H.v().pTones.length; k += 1) { await H.set({ pStage: k }); st = k; }
                var n = H.v().pTones.length; for (var i = 0; i < n; i += 1) { await H.call((function (j) { return function (v) { return v.pTones[j].opts[0].onClick; }; })(i)); }
                await H.call('onPReveal'); await H.sleep(200); window.__st = st;""",
         want=["ks4:sound-waves-hearing:th#ppred-*", "ks4:sound-waves-hearing:th#tpred-*-1"],
         check=lambda b: all(isinstance(x["is_correct"], bool) and x["correct_answer"] for x in b if "#ppred-" in x["question_id"]),
         back="""(function(){ var s = H.rootState(), n = H.v().pTones.length; return s.pShown[1] === true && n > 0 && s.pShown[s.pStage] === true && Object.keys(s.tPred).length === n; })()"""),
    # ── Answers found by reading the groups the classifier filed as not-an-answer ──
    dict(name="ks4-read-threats", page="/triple/higher/biology/ecology/factors-affecting-food-security.html", forms=True,
         act="""H.click(H.exact(H.v().threatBtns[0].label)); await H.sleep(300);""",
         want=["ks4:factors-affecting-food-security:th#picks-1"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool) and b[-1]["answer"],
         back="""(function(){ var s = H.rootState(); return s.picks[0] !== undefined && s.picks[0] !== null && H.v().headDone === true; })()"""),
    dict(name="ks4-read-levels", page="/triple/higher/biology/organisation/principles-of-organisation.html", forms=True,
         act="""H.click(H.exact(H.v().levelBtns[0].label)); await H.sleep(300);""",
         want=["ks4:principles-of-organisation:th#picks-1"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool) and b[-1]["answer"],
         back="""(function(){ return H.v().exDone === true; })()"""),
    dict(name="ks4-read-methods", page="/triple/higher/chemistry/chemical-changes/extraction-of-metals.html", forms=True,
         act="""H.click(H.exact(H.v().methods[0].label)); await H.sleep(300);""",
         want=["ks4:extraction-of-metals:th#pick-*"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool) and b[-1]["answer"],
         back="""(function(){ return H.rootState().pick !== null && H.v().hasChooseNote === true; })()"""),
    dict(name="ks4-read-clue", page="/triple/higher/biology/infection-response/viral-diseases.html", forms=True,
         act="""H.click(H.exact(H.v().clueBtns[0].label)); await H.sleep(300);""",
         want=["ks4:viral-diseases:th#clue-1"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool) and b[-1]["answer"],
         back="""(function(){ return H.rootState().pick === 0; })()"""),
    dict(name="ks4-read-meiosis", page="/triple/higher/biology/inheritance/meiosis.html", forms=True,
         act="""for (var k = 0; k < 6 && H.v().stepBtns.length < 2; k += 1) { await H.set({ step: k }); }
                var b = H.v().stepBtns; window.__at = H.rootState().step; H.click(H.exact(b[0].label)); await H.sleep(200); if (H.rootState().step === window.__at) { H.click(H.exact(b[1].label)); await H.sleep(200); }""",
         want=["ks4:meiosis:th#gate-*"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool) and b[-1]["answer"],
         back="""(function(){ return H.rootState().step > 0; })()"""),
    dict(name="ks4-read-microscope", page="/triple/higher/biology/cell-biology/microscopy.html", forms=True,
         act="""await H.set({ pending: 0 }); H.click(H.exact(H.v().gateOpts[0].label)); await H.sleep(300);""",
         want=["ks4:microscopy:th#gate-1"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool) and b[-1]["answer"] and b[-1]["question_text"],
         back="""(function(){ var s = H.rootState(); return s.gate[0] === 0 && s.pending === null; })()"""),
    dict(name="ks4-read-zones", page="/triple/higher/physics/energy/energy-resources.html", forms=True,
         retired="the lean rebuild (Wave 0) took the resource cards off the page",
         absent=['"e": "zones"'],
         act="""var z = H.v().zones; for (var i = 0; i < z.length && !H.rootState().flip; i += 1) { H.click(H.exact(z[i].label)); await H.sleep(200); }""",
         want=["ks4:energy-resources:th#placed-1"],
         check=lambda b: b[-1]["is_correct"] is True,
         back="""(function(){ var s = H.rootState(); return s.flip === true && Object.keys(s.placed).length === 1; })()"""),
    dict(name="ks4-read-logger", page="/triple/higher/physics/particle-model/specific-latent-heat.html", forms=True,
         act="""await H.set({ logDone: true }); await H.call(function (v) { return v.logSteps[0].opts[0].onClick; }); await H.sleep(200);""",
         want=["ks4:specific-latent-heat:th#ans-1"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool),
         back="""(function(){ var s = H.rootState(); return s.logDone === true && s.ans[0] === 0; })()"""),
    # Real presses: these two read the words on the control the child pressed.
    dict(name="ks4-name-cell", page="/triple/higher/biology/organisation/blood.html", forms=True,
         act="""var c = H.v().choices; var byT = function (t) { return Array.prototype.filter.call(document.querySelectorAll('#ks4-mount button'), function (b) { return (b.textContent || '').trim() === t; })[0]; };
                for (var i = 0; i < c.length; i += 1) { H.click(byT(H.v().choices[i].text)); await H.sleep(120); if (H.rootState().stage !== 'name') { break; } } await H.sleep(200);""",
         want=["ks4:blood:th#cell-1-name"],
         back="(function(){ return H.rootState().stage === 'job' && H.rootState().sel === 0; })()"),
    dict(name="ks4-order-links", page="/triple/higher/physics/space/red-shift-big-bang.html", forms=True,
         act="""var t = H.v().links; var byText = function (x) { return Array.prototype.filter.call(document.querySelectorAll('#ks4-mount button'), function (b) { return (b.textContent || '').indexOf(x) >= 0; })[0]; };
                H.click(byText(t[0].text)); await H.sleep(200); H.click(byText(t[1].text)); await H.sleep(200);""",
         want=["ks4:red-shift-big-bang:th#order-1"],
         check=lambda b: [x["is_correct"] for x in b if "#order-" in x["question_id"]] == [False, True],
         back="(function(){ return H.rootState().order.length === 1 && H.rootState().order[0] === 0; })()"),
    dict(name="ks4-choice-star", page="/triple/higher/physics/space/stellar-evolution.html", forms=True,
         act="H.click(H.exact(H.v().nextBtns[0].label)); await H.sleep(300);",
         want=["ks4:stellar-evolution:th#step-sun-3"],
         check=lambda b: isinstance(b[-1]["is_correct"], bool) and b[-1]["answer"],
         back="(function(){ return H.rootState().step.sun === 3; })()"),
    dict(name="ks4-list-features", page="/triple/higher/biology/cell-biology/cell-specialisation.html", forms=True,
         act="await H.call(function (v) { return v.featBtns[0].onClick; }); await H.call(function (v) { return v.featBtns[1].onClick; }); await H.call('onCompare'); await H.sleep(200);",
         want=["ks4:cell-specialisation:th#compared-1"],
         check=lambda b: b[-1]["answer"].count("\n") == 1,
         back="(function(){ var s = H.rootState(); var k = Object.keys(s.compared)[0]; return !!k && s.picks[k].length === 2; })()"),
    # ── ⊕ 9 Nov 2026: a blind run's findings ──
    dict(name="ks3-five-rulings", page="/ks3/chemistry/energy-changes-in-reactions/measuring-a-temperature-change.html",
         act="""var c = document.querySelectorAll('.ks3-rplan-step'); for (var i = 0; i < c.length; i += 1) { H.click(c[i].querySelectorAll('.ks3-rplan-opt')[0]); await H.sleep(120); }""",
         want=["measuring-a-temperature-change#plan-judge-%d" % n for n in range(1, 6)],
         check=lambda b: all(isinstance(x["is_correct"], bool) and x.get("correct_answer") for x in b if "#plan-judge-" in x["question_id"])
                         and [x for x in b if x["question_id"].endswith("-1")][0]["is_correct"] is False,
         back="""(function(){ var c = document.querySelectorAll('.ks3-rplan-step'); return Array.prototype.every.call(c, function (s) { return H.pressed(s.querySelectorAll('.ks3-rplan-opt')[0]) && s.getAttribute('data-open') === '1'; }) && /^5 of 5|all/.test(document.querySelector('.ks3-rplan-block [data-count]').textContent); })()"""),
    dict(name="ks3-bench-count", page="/ks3/chemistry/particles-and-their-behaviour/solids-liquids-and-gases.html",
         act="""var s = document.querySelector('.ks3-sbench-block'); H.click(s.querySelector('[data-benchgate] .ks3-option')); await H.sleep(200);
                var st = s.querySelectorAll('[data-sbench-state]'); for (var i = 0; i < st.length; i += 1) { H.click(st[i]); await H.sleep(150); } await H.sleep(1000);""",
         want=["solids-liquids-and-gases#state-bench-1"],
         ticks=True, settle=1.5,
         back="""/all three seen|^3 of 3/.test(document.querySelector('.ks3-sbench-block [data-count]').textContent)"""),
    dict(name="ks3-rig-runs", page="/ks3/chemistry/energy-changes-in-reactions/measuring-a-temperature-change.html",
         act="""var s = document.querySelector('.ks3-rigb-block'); var run = s.querySelector('[data-rigb-run]'); H.click(run); await H.sleep(150);
                var d = s.querySelectorAll('.ks3-rigb-dial'); for (var i = 0; i < 2; i += 1) { var o = d[i].querySelectorAll('[data-rigb-for]'); H.click(o[o.length - 1]); await H.sleep(100); H.click(s.querySelector('[data-rigb-run]')); await H.sleep(150); }""",
         want=["measuring-a-temperature-change#rig-build-1"],
         check=lambda b: sum(1 for x in b if x["question_id"].endswith("#rig-build-1")) == 3,
         back="""(function(){ var s = document.querySelector('.ks3-rigb-block'); return s.getAttribute('data-stage-done') === '1'; })()"""),
    dict(name="ks4-indicative-ticks", page="/triple/higher/biology/inheritance/advantages-sexual-asexual.html", ticks429=1, settle=2,
         act="""var w = H.write(); var ta = w.host.querySelector('textarea'); ta.scrollIntoView({block:'center'});
                ta.value = 'Sexual reproduction gives variation so some offspring may survive a change, while asexual reproduction is faster and needs only one parent.';
                ta.dispatchEvent(new Event('input', {bubbles: true})); await H.sleep(300);
                H.click(H.btnIn(w.host, 'button', 'Show the mark scheme')); await H.sleep(500);
                var lv = Array.prototype.filter.call(w.host.querySelectorAll('button'), function (b) { return /Level 1/.test(b.textContent); })[0]; H.click(lv); await H.sleep(200);
                var boxes = w.host.querySelectorAll('input[type=checkbox]'); H.click(boxes[0]); await H.sleep(100); H.click(boxes[2]); await H.sleep(2500);""",
         want=["ks4:advantages-sexual-asexual:th#*"],
         ticks=True,
         tickcheck=lambda t: t[-1]["ticks"] == [3, 5, 7] and t[-1].get("level") == 1,
         back="""(function(){ var w = H.write(); var s = w.logic.state; return s.open === true && typeof s.level === 'number' && /Level 1/.test(w.logic.props.levels[s.level].label) && !!s.ticks[0] && !s.ticks[1] && !!s.ticks[2]; })()"""),
    # Every unit of a multi-unit kind gets its own id, and every one comes back.
    dict(name="ks3-units-fault", page="/ks3/biology/breathing-and-gas-exchange/exercise-asthma-and-smoking.html",
         retired="the lean rebuild (Wave 0) took the locate-the-fault bench off the page",
         absent=["ks3-fault-block", "data-fault"],
         act="""var s = document.querySelector('.ks3-fault-block'); var t = s.querySelectorAll('.ks3-fault-tab');
                for (var i = 0; i < 2; i += 1) { H.click(t[i]); await H.sleep(100); H.click(s.querySelectorAll('[data-fault] .ks3-option')[i]); await H.sleep(100); H.click(s.querySelector('[data-fault-open]')); await H.sleep(150); }""",
         want=["exercise-asthma-and-smoking#locate-the-fault-1", "exercise-asthma-and-smoking#locate-the-fault-2"],
         check=lambda b: all(isinstance(x["is_correct"], bool) for x in b if "#locate-the-fault" in x["question_id"]),
         back="""/^2 of 3/.test(document.querySelector('.ks3-fault-block [data-count]').textContent)"""),
    dict(name="ks3-units-route", page="/ks3/biology/respiration/aerobic-vs-anaerobic.html",
         retired="the lean rebuild (Wave 1) took the which-route bench off the page",
         absent=["ks3-rd-block", "data-rd-case"],
         act="""var s = document.querySelector('.ks3-rd-block'); var t = s.querySelectorAll('[data-rd-case]');
                for (var i = 0; i < 2; i += 1) { H.click(t[i]); await H.sleep(100); H.click(s.querySelectorAll('[data-rd-route]')[0]); await H.sleep(100); H.click(s.querySelector('[data-rd-run]')); await H.sleep(150); }""",
         want=["aerobic-vs-anaerobic#which-route-is-running-1", "aerobic-vs-anaerobic#which-route-is-running-2"],
         check=lambda b: all(isinstance(x["is_correct"], bool) for x in b if "#which-route" in x["question_id"]),
         back="""/^2 of/.test(document.querySelector('.ks3-rd-block [data-rd-progress]').textContent)"""),
    dict(name="ks3-units-grid", page="/ks3/chemistry/types-of-reaction/displacement.html",
         act="""var s = document.querySelector('.ks3-rgrid-block'); var c = s.querySelectorAll('[data-rgrid-cell]');
                for (var i = 0; i < 2; i += 1) { H.click(c[i + 1]); await H.sleep(100); H.click(s.querySelector('[data-rgrid-opt="yes"]')); await H.sleep(200); }""",
         want=["displacement#grid-sixteen-2", "displacement#grid-sixteen-3"],
         check=lambda b: all(isinstance(x["is_correct"], bool) for x in b if "#grid-sixteen" in x["question_id"]),
         back="""document.querySelectorAll('.ks3-rgrid-block [data-rgrid-state]').length >= 2"""),
    dict(name="ks3-units-halogens", page="/ks3/chemistry/the-periodic-table/group-7-the-halogens.html",
         act="""var s = document.querySelector('.ks3-hgrid-block'); var c = s.querySelectorAll('[data-hgrid-cell]');
                H.click(s.querySelector('[data-hgrid-opt="no"]')); await H.sleep(80); H.click(c[0]); await H.sleep(150); H.click(c[1]); await H.sleep(150);""",
         want=["group-7-the-halogens#grid-nine-1", "group-7-the-halogens#grid-nine-2"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#grid-nine-1")][0]["is_correct"] is True
                         and [x for x in b if x["question_id"].endswith("#grid-nine-2")][0]["is_correct"] is None
                         and [x for x in b if x["question_id"].endswith("#grid-nine-2")][0]["self_checked"] is False,
         back="""H.pressed(document.querySelectorAll('.ks3-hgrid-block [data-hgrid-cell]')[1])"""),
    dict(name="ks3-units-combinations", page="/ks3/biology/nutrition-and-digestion/food-tests.html",
         act="""var s = document.querySelector('.ks3-tbench-block'); H.click(s.querySelectorAll('[data-predict] .ks3-option')[0]); await H.sleep(200);
                H.click(s.querySelectorAll('.ks3-tbench-tab[data-food]')[1]); await H.sleep(120); H.click(s.querySelectorAll('[data-predict] .ks3-option')[1]); await H.sleep(200);""",
         want=["food-tests#twenty-combinations-1", "food-tests#twenty-combinations-5"],
         check=lambda b: all(isinstance(x["is_correct"], bool) for x in b if "#twenty" in x["question_id"]),
         back="""/^2 of/.test(document.querySelector('.ks3-tbench-block [data-count]').textContent)"""),
    dict(name="ks3-units-sentence", page="/ks3/chemistry/chemical-reactions/chemical-vs-physical-change.html",
         act="""var s = document.querySelector('.ks3-chain-block'); var u = s.querySelectorAll('[data-chain-slot]'); H.click(u[0].querySelector('.ks3-option')); await H.sleep(120); H.click(u[1].querySelector('.ks3-option')); await H.sleep(150);""",
         want=["chemical-vs-physical-change#chain-wax-1", "chemical-vs-physical-change#chain-wax-2"],
         check=lambda b: all(isinstance(x["is_correct"], bool) for x in b),
         back="""(function(){ var u = document.querySelectorAll('.ks3-chain-block [data-chain-slot]'); return H.pressed(u[0].querySelector('.ks3-option')) && H.pressed(u[1].querySelector('.ks3-option')); })()"""),
    dict(name="ks3-units-order", page="/ks3/chemistry/the-earth-and-its-atmosphere/the-rock-cycle.html",
         act="""var p = document.querySelectorAll('.ks3-grain-block [data-grain-pick]'); for (var i = 0; i < p.length; i += 1) { H.click(p[i]); await H.sleep(50); } await H.sleep(200);""",
         want=["the-rock-cycle#grain-order-1"],
         check=lambda b: len(b) == 1 and b[0]["kind"] == "order" and isinstance(b[0]["is_correct"], bool) and b[0]["correct_answer"].count("\n") >= 3,
         back="""(function(){ var p = document.querySelectorAll('.ks3-grain-block [data-grain-pick]'); return Array.prototype.every.call(p, function (x) { return H.pressed(x); }); })()"""),
    dict(name="ks3-units-sort", page="/ks3/biology/cells-and-organisation/life-processes.html",
         act="""var r = document.querySelectorAll('.ks3-sort .ks3-sortrow'); for (var i = 0; i < r.length; i += 1) { H.click(r[i].querySelector('.ks3-sort-chip')); await H.sleep(40); }
                H.click(r[1].querySelectorAll('.ks3-sort-chip')[1]); await H.sleep(120);
                H.click(document.querySelector('.ks3-sort [data-sort-reveal]')); await H.sleep(300);
                H.click(document.querySelector('.ks3-sort [data-selfcheck] .ks3-option')); await H.sleep(200);""",
         want=["life-processes#living-once-never-*"],
         check=lambda b: len(set(x["question_id"] for x in b)) == len(b) and len(b) >= 8 and all(x["correct_answer"] for x in b if x["is_correct"] is False),
         back="""(function(){ var r = document.querySelectorAll('.ks3-sort .ks3-sortrow'); return H.pressed(r[0].querySelector('.ks3-sort-chip')) && H.pressed(r[1].querySelectorAll('.ks3-sort-chip')[1]) && !r[0].querySelector('.ks3-sort-answer').closest('[hidden]') && H.pressed(document.querySelector('.ks3-sort [data-selfcheck] .ks3-option')); })()"""),
    # ── ⊕ 9 Nov 2026: a second blind run ──
    dict(name="ks4-all-right", page="/combined/higher/chemistry/quantitative/conservation-of-mass.html",
         act="""await H.set({ w1: 0, w2: 2 }); var R = [0, 3, 3, 1, 2];
                for (var i = 0; i < 5; i += 1) { var o = H.v().w3Rows[i].options[R[i]]; H.click(document.querySelector('#ks4-mount button[aria-label="' + o.aria + '"]')); await H.sleep(200); }
                await H.call('onW3Check'); await H.sleep(200);""",
         want=["ks4:conservation-of-mass:ch#w3-%d" % n for n in range(1, 6)],
         check=lambda b: all(x["is_correct"] is True for x in b if "#w3-" in x["question_id"]),
         back="""(function(){ var s = H.rootState(); return s.w3Checked === true && Object.keys(s.w3).length === 5 && /^All five right/.test(H.v().w3Word); })()"""),
    dict(name="ks4-chain-retry", page="/combined/higher/biology/organisation/heart-blood-vessels.html",
         act="""var P = H.block('Ks4Practice'), R = P.logic.props.rungs, keys = [], ck = null, n = 0;
                [R.r1, R.r2, R.r3, R.r4].forEach(function (items, ri) { items.forEach(function (it, i) { keys.push(ri + '-' + i); if ((it.kind || 'mcq') === 'chain' && !ck) { ck = [ri, i, it]; } }); });
                var kid = function () { var o = null; Array.prototype.forEach.call(P.host.querySelectorAll('[data-dc-tpl]'), function (el) { var a = el.__mrbKs4; if (!o && a && a.comp === 'Ks4Chain') { o = a; } }); return o; };
                var links = ck[2].links.map(function (t, k) { return 'L' + k; });
                var check = async function (order) { var c = kid(); c.logic.setState({ chain: order, checked: false }); await H.sleep(90); c.logic.renderVals().onCheck(); await H.sleep(250); };
                await check(links.slice().reverse());
                var q = {}; keys.forEach(function (k) { q[k] = { res: k === ck[0] + '-' + ck[1] ? false : true, pick: 0, conv: null, num: '', unit: '' }; }); P.logic.setState({ q: q }); await H.sleep(120);
                P.logic.renderVals().onRetry(); await H.sleep(300);
                await check(links); await H.sleep(200); window.__ck = ck[0] + '-' + ck[1];""",
         want=["ks4:heart-blood-vessels:ch#r*"],
         # ⊕ 10 Nov 2026: the check after Retry is the rung's again, so it names the rung, once.
         check=lambda b: (lambda ch: len(ch) == 2 and all(x["rung"] for x in ch) and ch[1]["is_correct"] is True)([x for x in b if x["question_id"].endswith("#r3-1")]),
         back="""(function(){ var P = H.block('Ks4Practice'), R = P.logic.props.rungs, ck = null; [R.r1, R.r2, R.r3, R.r4].forEach(function (items, ri) { items.forEach(function (it, i) { if ((it.kind || 'mcq') === 'chain' && !ck) { ck = ri + '-' + i; } }); }); return P.logic.state.q[ck].res === true; })()"""),
    dict(name="ks4-chain-recheck", page="/combined/higher/biology/organisation/heart-blood-vessels.html",
         act="""var P = H.block('Ks4Practice'), R = P.logic.props.rungs, ck = null;
                [R.r1, R.r2, R.r3, R.r4].forEach(function (items) { items.forEach(function (it) { if ((it.kind || 'mcq') === 'chain' && !ck) { ck = it; } }); });
                var c = null; Array.prototype.forEach.call(P.host.querySelectorAll('[data-dc-tpl]'), function (el) { var a = el.__mrbKs4; if (!c && a && a.comp === 'Ks4Chain') { c = a; } });
                var links = ck.links.map(function (t, k) { return 'L' + k; });
                c.logic.setState({ chain: links.slice().reverse(), checked: false }); await H.sleep(90); c.logic.renderVals().onCheck(); await H.sleep(250);
                c.logic.setState({ chain: links, checked: false }); await H.sleep(90); c.logic.renderVals().onCheck(); await H.sleep(250);""",
         want=["ks4:heart-blood-vessels:ch#r*"],
         check=lambda b: (lambda ch: len(ch) == 2 and ch[0]["rung"] and not ch[1]["rung"])([x for x in b if x["question_id"].endswith("#r3-1")]),
         back="""(function(){ var P = H.block('Ks4Practice'), R = P.logic.props.rungs, ck = null; [R.r1, R.r2, R.r3, R.r4].forEach(function (items, ri) { items.forEach(function (it, i) { if ((it.kind || 'mcq') === 'chain' && !ck) { ck = ri + '-' + i; } }); }); return P.logic.state.q[ck].res === false; })()"""),
    dict(name="ks4-concord-none", page="/triple/higher/chemistry/chemical-changes/titrations.html",
         act="""var runs = [2500, 2520, 2510, 2470];
                for (var i = 0; i < runs.length; i += 1) { await H.set({ gate: 0, added: runs[i], shown: runs[i] }); await H.call('onRecord'); if (i < 3) { await H.call('onNextRun'); } }
                await H.call(function (v) { return v.rowBtns[2].onClick; }); await H.call(function (v) { return v.rowBtns[3].onClick; }); await H.call('onPickCheck'); await H.sleep(200);""",
         want=["ks4:titrations:th#concord"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#concord")][0]["is_correct"] is False
                         and "oncordant" in ([x for x in b if x["question_id"].endswith("#concord")][0]["correct_answer"] or ""),
         back="(function(){ var s = H.rootState(); return !!s.pick && s.pick.ok === false; })()"),
    # ── ⊕ 10 Nov 2026: a fourth blind run ──
    dict(name="ks4-group1-predict", page="/combined/higher/chemistry/atomic-structure/group-1.html",
         act="""H.click(H.exact('Drop it in')); await H.sleep(300); await H.call(function (v) { return v.metals[1].onClick; }); await H.sleep(200);
                H.click(H.exact('More gently')); await H.sleep(400);""",
         want=["ks4:group-1:ch#preds-2"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#preds-2")][0]["is_correct"] is False
                         and [x for x in b if x["question_id"].endswith("#preds-2")][0]["correct_answer"] == "More vigorously"
                         and not any(x.get("answer") == "Drop it in" for x in b),
         back="H.rootState().shown[1] === true && H.rootState().preds[1] === 'less'"),
    dict(name="ks4-last-compound", page="/combined/higher/chemistry/bonding/ionic-compounds.html",
         act="""var vals = ['MgO', 'CaF2', 'Na2O'];
                for (var i = 0; i < 3; i += 1) { var a = H.rootState().dxVal.slice(); a[i] = vals[i]; await H.set({ dx: i, dxVal: a, dxChecked: false }); await H.call('onDxCheck'); await H.sleep(150); }""",
         want=["ks4:ionic-compounds:ch#dxval-3"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#dxval-3")][0]["is_correct"] is False,
         same="H.rootState().dx === 2 && H.rootState().dxChecked === true && /^Count again/.test(H.v().dxWord)",
         back="H.rootState().dx === 2 && H.rootState().dxChecked === true && /^Count again/.test(H.v().dxWord)"),
    dict(name="ks3-live-calc", page="/ks3/physics/forces/moments.html",
         act="""var g = document.querySelector('.ks3-span-block [data-span-gopt="0"]'); H.click(g); await H.sleep(200);
                H.click(document.querySelector('[data-span-arm="0.05"]')); await H.sleep(120);
                var f = document.querySelector('[data-span-force]'); f.value = '40'; f.dispatchEvent(new Event('input', {bubbles: true})); await H.sleep(150);
                var q = document.querySelector('[data-p4cfa-q="0"]'), ins = q.querySelectorAll('[data-p4cfa-input]'), L = ['nothing', 'M = F x d', 'M = 40 x 0.05', '40 x 0.05 = 2', 'M = 2 N m'];
                for (var i = 0; i < ins.length; i += 1) { ins[i].value = L[i]; ins[i].dispatchEvent(new Event('input', {bubbles: true})); }
                await H.sleep(100); H.click(q.querySelector('[data-p4cfa-check]')); await H.sleep(400);""",
         then="""var f = document.querySelector('[data-span-force]'); f.value = '100'; f.dispatchEvent(new Event('input', {bubbles: true})); await H.sleep(500);""",
         want=["moments#your-turn-moment-1"],
         check=lambda b: [x for x in b if x["question_id"] == "moments#your-turn-moment-1"][0]["question_text"].startswith("Your spanner: 40 N at 0.05 m"),
         same="""(function(){ var q = document.querySelector('[data-p4cfa-q="0"]'); return q.querySelector('[data-p4cfa-head]').textContent.trim() === 'Your spanner: 40 N at 0.05 m from the pivot.' && !q.querySelector('[data-p4cfa-reveal]').hasAttribute('hidden') && document.querySelector('[data-span-force]').value === '40'; })()""",
         back="""(function(){ var q = document.querySelector('[data-p4cfa-q="0"]'); return q.querySelector('[data-p4cfa-head]').textContent.trim() === 'Your spanner: 40 N at 0.05 m from the pivot.' && !q.querySelector('[data-p4cfa-reveal]').hasAttribute('hidden'); })()"""),
    dict(name="ks3-bench-runs", page="/ks3/physics/energy-at-home/energy-in-food.html", settle=0, settle_b=7,
         act="""var s = document.querySelector('.ks3-calor-block'); H.click(s.querySelector('[data-calor-gopt]')); await H.sleep(200);
                for (var k = 0; k < 2; k += 1) {
                  H.click(s.querySelectorAll('[data-calor-food]')[k]); await H.sleep(100);
                  var b = s.querySelector('[data-calor-burn]'); H.click(b);
                  for (var t = 0; t < 80 && !b.disabled; t += 1) { await H.sleep(100); }
                  H.click(s.querySelector('[data-calor-record]')); await H.sleep(200);
                }""",
         want=["energy-in-food#food-calorimeter-run-1", "energy-in-food#food-calorimeter-run-2"],
         check=lambda b: all(x["kind"] == "numeric" and x["is_correct"] is None and x["answer"].count(" · ") == 3 for x in b if "-run-" in x["question_id"]),
         back="""(function(){ var r = document.querySelectorAll('.ks3-calor-block [data-calor-rows] tr'); return r.length === 2 && r[1].children[1].textContent.trim() === document.querySelectorAll('.ks3-calor-block [data-calor-food]')[1].textContent.trim(); })()"""),
    # ⊕ 10 Nov 2026, fifth blind run: a run recorded part-way through a burn burned less
    # than the slider's smallest mass, so it can't be made again with the same numbers.
    # It stays saved; the page's table starts empty rather than showing other numbers.
    dict(name="ks3-bench-part-run", page="/ks3/physics/energy-at-home/energy-in-food.html", settle=0, settle_b=7,
         act="""var s = document.querySelector('.ks3-calor-block'); H.click(s.querySelector('[data-calor-gopt]')); await H.sleep(200);
                var m = s.querySelector('[data-calor-mass]'); m.value = m.min; m.dispatchEvent(new Event('input', {bubbles: true})); await H.sleep(100);
                H.click(s.querySelectorAll('[data-calor-food]')[0]); await H.sleep(100);
                H.click(s.querySelector('[data-calor-burn]')); await H.sleep(600);
                H.click(s.querySelector('[data-calor-record]')); await H.sleep(300);""",
         want=["energy-in-food#food-calorimeter-run-1"],
         check=lambda b: [x for x in b if x["question_id"].endswith("-run-1")][0]["answer"].split(" · ")[0].strip() not in ("0.1 g", "0.10 g"),
         back="""(function(){ return document.querySelectorAll('.ks3-calor-block [data-calor-rows] tr').length === 0; })()"""),
    # ── ⊕ 9 Nov 2026: a third blind run ──
    dict(name="ks4-typed-rate", page="/triple/higher/biology/ecology/decomposition.html",
         act="""var L = document.getElementById('ks4-mount').__mrbKs4.logic; L.setState({ own: { 40: 120 } }); await H.sleep(150); L.setState({ rate: '1' }); await H.sleep(100); await H.call('onRateCheck'); await H.sleep(250);""",
         want=["ks4:decomposition:th#rate"],
         check=lambda b: [x for x in b if x["question_id"].endswith("#rate")][0]["correct_answer"] == "0.0083",
         back="true"),
    dict(name="ks3-commit-run", page="/ks3/chemistry/chemical-reactions/mass-in-a-reaction.html",
         act="""var s = document.querySelector('.ks3-bbench-block'), o = s.querySelectorAll('[data-bbench-predict] .ks3-option'); H.click(o[0]); await H.sleep(120); H.click(o[1]); await H.sleep(120); H.click(s.querySelector('[data-bbench-run]')); await H.sleep(500);""",
         want=["mass-in-a-reaction#*-1"],
         check=lambda b: len(b) == 1,
         back="""H.pressed(document.querySelectorAll('.ks3-bbench-block [data-bbench-predict] .ks3-option')[1])"""),
    dict(name="ks3-commit-run-2", page="/ks3/chemistry/mixtures-and-separation/evaporation-and-crystallisation.html",
         act="""var s = document.querySelector('.ks3-cryst-block'), o = s.querySelectorAll('[data-cryst-gate-opts] .ks3-option'); H.click(o[0]); await H.sleep(120); H.click(o[1]); await H.sleep(120); H.click(s.querySelector('[data-cryst-run]')); await H.sleep(500);""",
         want=["evaporation-and-crystallisation#*-1"],
         check=lambda b: len(b) == 1,
         back="""H.pressed(document.querySelectorAll('.ks3-cryst-block [data-cryst-gate-opts] .ks3-option')[1])"""),
    dict(name="ks3-commit-panel", page="/ks3/biology/movement-skeleton-and-muscles/what-the-skeleton-does.html",
         act="""var s = document.querySelector('.ks3-switch-block'), o = s.querySelectorAll('.ks3-switch-panel:not([hidden]) .ks3-option'); H.click(o[0]); await H.sleep(120); H.click(o[1]); await H.sleep(120); H.click(s.querySelector('.ks3-switch-panel:not([hidden]) [data-switch]')); await H.sleep(300);""",
         want=["what-the-skeleton-does#switch-off-chains-1"],
         check=lambda b: len(b) == 1,
         back="""H.pressed(document.querySelectorAll('.ks3-switch-block .ks3-switch-panel .ks3-option')[1])"""),
    dict(name="ks3-commit-whole", page="/ks3/biology/photosynthesis/testing-a-leaf-for-starch.html",
         retired="the lean rebuild (Wave 1) took the run-it-badly bench off the page",
         absent=["ks3-mb-block", "data-mb-run"],
         act="""var s = document.querySelector('.ks3-mb-block'), o = s.querySelectorAll('.ks3-mb-opt[data-step="boil"]'); H.click(o[1]); await H.sleep(120); H.click(s.querySelector('[data-mb-run]')); await H.sleep(400);""",
         want=["testing-a-leaf-for-starch#run-it-badly-1"],
         check=lambda b: len(b) == 1 and b[0]["answer"].count("\n") >= 4,
         back="""H.pressed(document.querySelectorAll('.ks3-mb-block .ks3-mb-opt[data-step="boil"]')[1])"""),
    dict(name="ks3-commit-check", page="/ks3/biology/inheritance-and-dna/what-makes-a-species.html",
         act="""var s = document.querySelector('.ks3-sc-block'), p = s.querySelector('[data-sc-panel="dogs"]'), o = p.querySelectorAll('.ks3-sc-verdict'); H.click(o[1]); await H.sleep(120); H.click(o[2]); await H.sleep(120); H.click(s.querySelector('[data-sc-check]')); await H.sleep(300);""",
         want=["what-makes-a-species#same-species-or-not-1"],
         check=lambda b: len(b) == 1 and b[0]["is_correct"] is False and b[0]["correct_answer"] == "Same species",
         back="""H.pressed(document.querySelector('.ks3-sc-block [data-sc-panel="dogs"]').querySelectorAll('.ks3-sc-verdict')[2])"""),
    dict(name="ks3-commit-plot", page="/ks3/biology/inheritance-and-dna/variation-continuous-and-discontinuous.html",
         act="""var s = document.querySelector('.ks3-vp-block'), o = s.querySelectorAll('[data-vp-pred]'); H.click(o[0]); await H.sleep(120); H.click(o[1]); await H.sleep(120); H.click(s.querySelector('[data-vp-plot]')); await H.sleep(300);""",
         want=["variation-continuous-and-discontinuous#*-1"],
         check=lambda b: len(b) == 1 and isinstance(b[0]["is_correct"], bool) and b[0]["correct_answer"],
         back="""H.pressed(document.querySelectorAll('.ks3-vp-block [data-vp-pred]')[1])"""),
    dict(name="ks4-readings", page="/combined/higher/physics/electricity/resistors.html",
         act="""H.click(document.querySelector('[aria-label^="Graph A"]')); await H.sleep(200);
                for (var i = 0; i < 3; i += 1) { await H.call('onRecord'); await H.sleep(120); }
                await H.call('onClear'); await H.sleep(120);
                for (var j = 0; j < 2; j += 1) { await H.call('onRecord'); await H.sleep(120); }""",
         want=["ks4:resistors:ch#data-resistor-1", "ks4:resistors:ch#data-resistor-5", "ks4:resistors:ch#data-resistor-cleared"],
         check=lambda b: all(x["kind"] == "numeric" and x["is_correct"] is None and re.match(r"^[-\u2212]?\d+\.\d\d V, \d+\.\d\d A$", x["answer"]) for x in b if "#data-" in x["question_id"] and "cleared" not in x["question_id"]) and [x for x in b if x["question_id"].endswith("gate-resistor")][0]["correct_answer"] == "A",
         back="H.rootState().data.resistor.length === 2 && H.rootState().gate.resistor === 0"),
    dict(name="ks3-rig-build", page="/ks3/chemistry/energy-changes-in-reactions/measuring-a-temperature-change.html",
         act="""var s = document.querySelector('.ks3-rigb-block'); H.click(s.querySelector('[data-rigb-run]')); await H.sleep(400);""",
         want=["measuring-a-temperature-change#rig-build-1"],
         back="true"),
    dict(name="ks3-curve-run", page="/ks3/chemistry/energy-changes-in-reactions/energy-and-changes-of-state.html",
         act="""var s = document.querySelector('.ks3-hcurve-block'); var b = s.querySelector('[data-hcurve-step]'); for (var i = 0; i < 8 && !b.disabled; i += 1) { H.click(b); await H.sleep(120); }""",
         want=[],
         back="(function(){ var s = document.querySelector('.ks3-hcurve-block'); return !!s; })()"),
    dict(name="ks4-steps-wrong", page="/combined/higher/biology/ecology/decomposition.html",
         act="""var settle = async function () { for (var t = 0; t < 40 && H.rootState().cycAnim; t += 1) { await H.sleep(200); } };
                for (var i = 0; i < 3; i += 1) { var o = H.v().cycOptions; H.click(H.rootBtn(o[i === 1 ? 1 : 0].text)); await H.sleep(150); await settle(); if (i < 2) { await H.call('onCycNext'); } }""",
         want=["ks4:decomposition:ch#cycpick-1", "ks4:decomposition:ch#cycpick-2", "ks4:decomposition:ch#cycpick-3"],
         check=lambda b: all(isinstance(x["is_correct"], bool) and x["correct_answer"] for x in b if "#cycpick-" in x["question_id"]),
         back="""(function(){ var s = H.rootState(); return s.cycPick.every(function (x) { return x !== null; }) && !s.cycAnim && s.cyc === 2; })()"""),
    dict(name="ks4-commit-only", page="/combined/higher/physics/electricity/series-parallel-circuits.html",
         act="""var q = H.v().qs; H.click(H.rootBtn(q[0].opts[0].label, 0)); await H.sleep(120); H.click(H.rootBtn(H.v().qs[0].opts[1].label, 0)); await H.sleep(120); H.click(H.rootBtn(H.v().qs[1].opts[1].label, 1)); await H.sleep(120);
                window.__before = 1; await H.sleep(200); await H.call('onReveal'); await H.sleep(250);""",
         want=["ks4:series-parallel-circuits:ch#preds-2-1", "ks4:series-parallel-circuits:ch#preds-2-2"],
         check=lambda b: len([x for x in b if "#preds-" in x["question_id"]]) == 2 and all(x.get("correct_answer") and isinstance(x["is_correct"], bool) for x in b if "#preds-" in x["question_id"]),
         back="""(function(){ var s = H.rootState(); return s.revealed[s.step] === true && s.preds[s.step][0] === 1; })()"""),
    dict(name="ks4-commit-lens", page="/triple/higher/physics/waves/lenses.html",
         act="""var q = H.v().bQs; for (var i = 0; i < q.length; i += 1) { await H.call((function (j) { return function (v) { return v.bQs[j] && v.bQs[j].opts[0].onClick; }; })(i)); }
                await H.call('onDraw'); await H.sleep(200);
                document.getElementById('ks4-mount').__mrbKs4.logic.setState({ pos: 1 }); await H.sleep(200);
                q = H.v().bQs; for (var j = 0; j < q.length; j += 1) { await H.call((function (n) { return function (v) { return v.bQs[n].opts[0].onClick; }; })(j)); }
                await H.call('onDraw'); await H.sleep(200);""",
         want=["ks4:lenses:th#preds-*"],
         check=lambda b: all(isinstance(x["is_correct"], bool) and x["correct_answer"] and x["is_correct"] == (x["answer"] == x["correct_answer"]) for x in b if "#preds-" in x["question_id"]) and any("cx20" in x["question_id"] for x in b),
         back="""(function(){ var s = H.rootState(); return Object.keys(s.shown).length === 2 && H.v().bVerdicts.length > 0; })()"""),
    dict(name="ks4-commit-pair", page="/triple/higher/physics/waves/types-of-em-waves.html",
         act="""var q = H.v().pairQs; for (var i = 0; i < q.length; i += 1) { await H.call((function (j) { return function (v) { return v.pairQs[j].opts[0].onClick; }; })(i)); }
                await H.call('onSend'); await H.sleep(200);""",
         want=["ks4:types-of-em-waves:th#preds-1-1"],
         back="""(function(){ return H.rootState().shown[0] === true; })()"""),
    dict(name="ks4-control-label", page="/combined/higher/chemistry/atomic-structure/group-1.html",
         act="H.click(H.exact('Drop it in')); await H.sleep(400);",
         want=[],
         check=lambda b: not any(x.get("answer") == "Drop it in" for x in b),
         back="true"),
    # ── KS3: the rest of the instruments ──
    dict(name="ks3-gate", page="/ks3/physics/energy-transfers/energy-transfers-before-and-after.html",
         act="var s = document.querySelector('.ks3-btally-block'); H.click(s.querySelector('[data-btally-gopt]')); await H.sleep(300);",
         want=["energy-transfers-before-and-after#*-1"],
         back="(function(){ var s = document.querySelector('.ks3-btally-block'); return H.pressed(s.querySelector('[data-btally-gopt]')) && s.querySelector('[data-btally-gate]').hidden; })()"),
    dict(name="ks3-unit-judged", page="/ks3/chemistry/particles-and-their-behaviour/testing-the-model.html",
         act="var s = document.querySelector('.ks3-ebench-block'); var c = s.querySelectorAll('.ks3-ebench-case'); H.click(c[0].querySelector('[data-call=\"1\"]')); H.click(c[2].querySelector('[data-call=\"1\"]')); await H.sleep(300);",
         want=["testing-the-model#seven-observations-1", "testing-the-model#seven-observations-3"],
         check=lambda b: {x["question_id"]: x["is_correct"] for x in b}.get("testing-the-model#seven-observations-1") is True
                         and {x["question_id"]: x["is_correct"] for x in b}.get("testing-the-model#seven-observations-3") is False,
         back="(function(){ var c = document.querySelectorAll('.ks3-ebench-block .ks3-ebench-case'); return H.pressed(c[0].querySelector('[data-call=\"1\"]')) && H.pressed(c[2].querySelector('[data-call=\"1\"]')); })()"),
    # ⊕ 8 Nov 2026: the saved work arrives before shared/ks3.js has run (a phone on
    # a slow line, a fast read). The replay must wait: pressing buttons nothing is
    # listening to yet loses the restore for good, with state 'done'.
    dict(name="ks3-slow-script", page="/ks3/chemistry/particles-and-their-behaviour/testing-the-model.html",
         slow_on_b="/shared/ks3.js",
         act="var s = document.querySelector('.ks3-ebench-block'); var c = s.querySelectorAll('.ks3-ebench-case'); H.click(c[0].querySelector('[data-call=\"1\"]')); await H.sleep(300);",
         want=["testing-the-model#seven-observations-1"],
         back="(function(){ var c = document.querySelectorAll('.ks3-ebench-block .ks3-ebench-case'); return H.pressed(c[0].querySelector('[data-call=\"1\"]')) && c[0].getAttribute('data-open') === '1'; })()"),
    dict(name="ks3-tab-unit", page="/ks3/physics/forces/non-contact-forces.html",
         act="var s = document.querySelector('.ks3-fsort-block'); H.click(s.querySelector('[data-fsort-tab=\"2\"]')); await H.sleep(200); H.click(s.querySelector('.ks3-fsort-label')); await H.sleep(300);",
         want=["non-contact-forces#*-3"],
         check=lambda b: any(x["question_id"].endswith("-3") and isinstance(x.get("is_correct"), bool) for x in b),
         back="(function(){ var s = document.querySelector('.ks3-fsort-block'); return H.pressed(s.querySelector('[data-fsort-tab=\"2\"]')) && H.pressed(s.querySelector('.ks3-fsort-label')); })()"),
    dict(name="ks3-parts-check", page="/ks3/biology/cells-and-organisation/levels-of-organisation.html",
         act="""var s = document.querySelector('.ks3-hard'); var rows = s.querySelectorAll('.ks3-hardrow');
                Array.prototype.forEach.call(rows, function (r) { H.click(r.querySelector('.ks3-rung-chip[data-rung=\"Tissue\"]') || r.querySelector('.ks3-rung-chip')); });
                await H.sleep(200); H.click(s.querySelector('[data-hard-reveal]')); await H.sleep(400);""",
         want=["levels-of-organisation#s-hard-1", "levels-of-organisation#s-hard-2"],
         check=lambda b: all(isinstance(x.get("is_correct"), bool) for x in b if "#s-hard-" in x["question_id"]),
         back="(function(){ var r = document.querySelectorAll('.ks3-hard .ks3-hardrow'); return r.length > 1 && r[0].getAttribute('data-open') === '1' && !!r[0].querySelector('.ks3-rung-chip[aria-pressed=\"true\"]'); })()"),
    dict(name="ks3-whole-check", page="/ks3/physics/describing-motion/distance-time-graphs.html",
         act="""var s = document.querySelector('.ks3-jwalk-block'); var segs = s.querySelectorAll('[data-jwalk-seg]');
                var want = ['walk','still','jog','back']; Array.prototype.forEach.call(segs, function (g, i) { H.click(g.querySelector('[data-jwalk-mode=\"' + want[i] + '\"]')); });
                await H.sleep(200); H.click(s.querySelector('[data-jwalk-send]')); await H.sleep(500);""",
         want=["distance-time-graphs#journey-match-1"],
         check=lambda b: [x for x in b if x["question_id"] == "distance-time-graphs#journey-match-1"][0]["is_correct"] is True,
         back="(function(){ var g = document.querySelectorAll('.ks3-jwalk-block [data-jwalk-seg]'); return g.length === 4 && H.pressed(g[2].querySelector('[data-jwalk-mode=\"jog\"]')); })()"),
    dict(name="ks3-typed", page="/ks3/chemistry/types-of-reaction/which-reaction-is-this.html",
         act="""var s = document.querySelector('.ks3-rwrite-block'); var f = s.querySelector('[data-rwrite-field]');
                f.value = 'If a substance gains oxygen it is oxidised, and if a fuel burns in oxygen that is combustion.';
                f.dispatchEvent(new Event('input', {bubbles: true})); await H.sleep(200); H.click(s.querySelector('[data-rwrite-show]')); await H.sleep(400);""",
         want=["which-reaction-is-this#*-1"],
         check=lambda b: [x for x in b if x["kind"] == "written"][0].get("self_checked") is False and [x for x in b if x["kind"] == "written"][0].get("is_correct") is None
                         and [x for x in b if x["kind"] == "written"][0]["answer"].startswith("If a substance gains oxygen"),
         back="(function(){ var s = document.querySelector('.ks3-rwrite-block'); return /gains oxygen/.test(s.querySelector('[data-rwrite-field]').value) && s.querySelector('[data-rwrite-show]').disabled; })()"),
    dict(name="ks3-order", page="/ks3/chemistry/acids-and-alkalis/making-a-pure-dry-salt.html",
         act="""var s = document.querySelector('.ks3-morder-block'); var st = s.querySelectorAll('[data-morder-step]');
                for (var i = 0; i < st.length; i += 1) { H.click(st[i]); await H.sleep(60); } await H.sleep(400);""",
         want=["making-a-pure-dry-salt#*-1"],
         check=lambda b: [x for x in b if x["kind"] == "order"][0]["answer"].count("\n") >= 3 and bool([x for x in b if x["kind"] == "order"][0]["correct_answer"]),
         back="(function(){ var s = document.querySelector('.ks3-morder-block'); return !!s.querySelector('[data-morder-answer]') && !s.querySelector('[data-morder-answer]').hidden; })()"),
    # ⊕ 8 Nov 2026: the two live puzzles (no Check; the page judges every press).
    dict(name="ks3-live-model", page="/ks3/biology/inheritance-and-dna/how-we-worked-out-dna.html",
         act="""var s = document.querySelector('.ks3-dh-block');
                H.click(s.querySelector('.ks3-dh-opt[data-dh-dial="strands"][data-dh-opt="2"]')); await H.sleep(200);
                var want = JSON.parse(s.querySelector('[data-dh]').getAttribute('data-target'));
                Object.keys(want).forEach(function (k) { var b = s.querySelector('.ks3-dh-opt[data-dh-dial="' + k + '"][data-dh-opt="' + want[k] + '"]'); if (b.getAttribute('aria-pressed') !== 'true') { H.click(b); } });
                await H.sleep(400);""",
         want=["how-we-worked-out-dna#build-a-model-that-fits-all-of-it-1"],
         check=lambda b: b[0]["is_correct"] is False and b[-1]["is_correct"] is True and b[-1]["answer"].count("\n") == 2,
         back="""(function(){ var s = document.querySelector('.ks3-dh-block'); var want = JSON.parse(s.querySelector('[data-dh]').getAttribute('data-target'));
                return Object.keys(want).every(function (k) { return H.pressed(s.querySelector('.ks3-dh-opt[data-dh-dial="' + k + '"][data-dh-opt="' + want[k] + '"]')); }); })()"""),
    dict(name="ks3-live-balance", page="/ks3/chemistry/chemical-reactions/symbol-equations-and-balancing.html",
         act="""var s = document.querySelector('.ks3-cbal-block'); var eq = s.querySelector('[data-cbal-eq="water"]');
                var up = function (i) { H.click(eq.querySelector('[data-cbal-for="' + i + '"][data-cbal-delta="1"]')); };
                up(0); await H.sleep(150); up(2); await H.sleep(400);""",
         want=["symbol-equations-and-balancing#balance-four-1"],
         check=lambda b: len(b) == 1 and b[0]["answer"] == "2, 1, 2" and b[0]["is_correct"] is True,
         back="""(function(){ var s = document.querySelector('.ks3-cbal-block'); var eq = s.querySelector('[data-cbal-eq="water"]');
                return eq.querySelector('[data-cbal-coeff="0"]').textContent === '2' && !eq.querySelector('[data-cbal-balanced]').hidden && !s.querySelector('[data-cbal-tick="water"]').hidden; })()"""),
    dict(name="ks3-commit-no-reveal", page="/ks3/biology/cells-and-organisation/unicellular-organisms.html",
         act="var s = H.sec('microscope-bench'); H.click(s.querySelectorAll('.ks3-option')[1]); await H.sleep(300);",
         want=["unicellular-organisms#microscope-bench"],
         back="H.pressed(H.sec('microscope-bench').querySelectorAll('.ks3-option')[1])"),
]
# One school-pupil (non-child) run per page type: the same presses.
# ⊕ 11 Nov 2026: ks4-form-internal stands in for ks4-form-round (the same stepPick form kind),
# because the lean rebuild retired the round on changes-in-energy.
PUPIL = ["ks4-flag-pick", "ks4-level-pick", "ks4-form-internal", "ks4-list-features", "ks3-gate", "ks3-parts-check", "ks3-typed"]


def retired_proof(c):
    """A case whose activity a lesson rebuild removed: prove the controls are gone from the
    built page and every id it used to send is retired (null) in docs/b2c/id-maps, so a
    child's saved rows are listed, not lost (docs/b2c/LESSON-DEPENDENCIES.md section 5)."""
    import glob
    html = open(os.path.join(REPO, "mrbadmus_site", c["page"].lstrip("/")), encoding="utf-8").read()
    still = [s for s in c["absent"] if s in html]
    maps = {}
    for p in sorted(glob.glob(os.path.join(REPO, "docs", "b2c", "id-maps", "*.json"))):
        maps.update(json.load(open(p, encoding="utf-8")))
    unmapped = [w for w in c["want"]
                if not any(k in maps and maps[k] is None for k in (w, re.sub(r"(-\d+)+$", "", w)))]
    return (not still and not unmapped), {"still drawn": still, "not retired in the id map": unmapped}


# Typed and not sent: back on the same device, nowhere else, and gone once sent.
DRAFTS = [
    dict(name="write", page="/triple/higher/biology/inheritance/advantages-sexual-asexual.html",
         type="""var w = H.write(), ta = w.host.querySelector('textarea'); ta.value = 'A half written answer about variation.'; ta.dispatchEvent(new Event('input', {bubbles: true}));""",
         back="H.write().logic.state.text === 'A half written answer about variation.' && H.write().host.querySelector('textarea').value === 'A half written answer about variation.'",
         blank="H.write().logic.state.text === ''"),
    dict(name="five lines, KS4", page="/combined/higher/biology/cell-biology/eukaryotes-prokaryotes.html",
         type="""var cf = H.block('Ks4Cfifa'), ins = cf.host.querySelectorAll('input'); ins[0].value = 'none yet'; ins[0].dispatchEvent(new Event('input', {bubbles: true})); await H.sleep(100); ins[1].value = 'Actual size'; ins[1].dispatchEvent(new Event('input', {bubbles: true}));""",
         back="(function(){ var ins = H.block('Ks4Cfifa').host.querySelectorAll('input'); return ins[0].value === 'none yet' && ins[1].value === 'Actual size'; })()",
         blank="H.block('Ks4Cfifa').host.querySelectorAll('input')[0].value === ''"),
    dict(name="five lines, KS3", page=KS3_CFA_PAGE,
         type="""var i = document.querySelectorAll('[data-instrument] input'), ins = Array.prototype.filter.call(i, function (x) { return Array.prototype.some.call(x.attributes, function (a) { return /^data-p\\d+cfa-input$/.test(a.name); }); }); window.__n = ins.length; ins[0].value = 'keep this line'; ins[0].dispatchEvent(new Event('input', {bubbles: true}));""",
         back="Array.prototype.some.call(document.querySelectorAll('[data-instrument] input'), function (x) { return x.value === 'keep this line'; })",
         blank="!Array.prototype.some.call(document.querySelectorAll('[data-instrument] input'), function (x) { return x.value === 'keep this line'; })"),
    # ⊕ 9 Nov 2026, a third blind run. Each `send` then presses the commit after the
    # reload and `sent` reads the time on the answer: it must include the typing.
    dict(name="typed, a KS3 rule of your own", page="/ks3/chemistry/types-of-reaction/which-reaction-is-this.html",
         type="""await H.sleep(3000); var f = document.querySelector('[data-rwrite-field]'); f.value = 'If a substance gains oxygen it is oxidised, which is a longer rule than the page asks for.'; f.dispatchEvent(new Event('input', {bubbles: true}));""",
         back="/gains oxygen/.test(document.querySelector('[data-rwrite-field]').value) && !document.querySelector('[data-rwrite-show]').disabled",
         blank="document.querySelector('[data-rwrite-field]').value === ''",
         send="H.click(document.querySelector('[data-rwrite-show]')); await H.sleep(400);",
         sent=lambda b: b and b[0]["time_spent_seconds"] is not None and b[0]["time_spent_seconds"] >= 3),
    dict(name="typed, KS3 Question 2", page="/ks3/physics/space/mass-vs-weight.html",
         type="""var s = document.querySelector('[data-activity="your-turn-mass"]'); H.click(s.querySelector('[data-p12cfa-tab="1"]')); await H.sleep(150);
                 var i = s.querySelector('[data-p12cfa-q="1"] [data-p12cfa-input="1"]'); i.value = 'second question line'; i.dispatchEvent(new Event('input', {bubbles: true}));""",
         back="""(function(){ var q = document.querySelector('[data-activity="your-turn-mass"] [data-p12cfa-q="1"]'); return !q.hasAttribute('hidden') && q.querySelector('[data-p12cfa-input="1"]').value === 'second question line'; })()""",
         blank="""document.querySelector('[data-activity="your-turn-mass"] [data-p12cfa-q="1"] [data-p12cfa-input="1"]').value === ''"""),
    dict(name="typed, KS3 Question 2 beside a live bench", page="/ks3/physics/forces/moments.html",
         type="""var s = document.querySelector('[data-activity="your-turn-moment"]'); H.click(s.querySelector('[data-p4cfa-tab="1"]')); await H.sleep(150);
                 var q = s.querySelector('[data-p4cfa-q="1"]'), i = q.querySelectorAll('[data-p4cfa-input]'); i[0].focus(); i[0].value = 'nothing to convert'; i[0].dispatchEvent(new Event('input', {bubbles: true})); i[1].value = 'M = F x d'; i[1].dispatchEvent(new Event('input', {bubbles: true}));""",
         back="""(function(){ var q = document.querySelector('[data-activity="your-turn-moment"] [data-p4cfa-q="1"]'); return !q.hasAttribute('hidden') && q.querySelectorAll('[data-p4cfa-input]')[1].value === 'M = F x d'; })()""",
         blank="""document.querySelector('[data-activity="your-turn-moment"] [data-p4cfa-q="1"] [data-p4cfa-input]').value === ''"""),
    dict(name="a slider", page="/ks3/physics/energy-at-home/reading-a-fuel-bill.html",
         type="""var r = document.querySelector('[data-bill-slider="shower"]'); r.value = '45'; r.dispatchEvent(new Event('input', {bubbles: true}));""",
         back="""document.querySelector('[data-bill-slider="shower"]').value === '45'""",
         blank="""document.querySelector('[data-bill-slider="shower"]').value === '20'"""),
    dict(name="a count on a block that takes no answer", page="/ks3/chemistry/the-earth-and-its-atmosphere/the-rock-cycle.html",
         type="""var s = document.querySelector('.ks3-parrow-block'), p = s.querySelectorAll('[data-parrow-pick]'); H.click(p[1]); await H.sleep(120); H.click(p[2]); await H.sleep(120);""",
         back="/^3 of 6/.test(document.querySelector('.ks3-parrow-block [data-count]').textContent.trim())",
         blank="/^1 of 6/.test(document.querySelector('.ks3-parrow-block [data-count]').textContent.trim())"),
    dict(name="picks on a KS3 block, not yet opened", page="/ks3/biology/cells-and-organisation/levels-of-organisation.html",
         type="""await H.sleep(2500); var r = document.querySelector('.ks3-hard .ks3-hardrow'); H.click(r.querySelectorAll('.ks3-rung-chip')[1]); await H.sleep(150);""",
         back="H.pressed(document.querySelector('.ks3-hard .ks3-hardrow').querySelectorAll('.ks3-rung-chip')[1])",
         blank="!H.pressed(document.querySelector('.ks3-hard .ks3-hardrow').querySelectorAll('.ks3-rung-chip')[1])"),
    dict(name="a pick behind its own Check", page="/ks3/biology/reproduction/seed-dispersal.html",
         type="""var o = document.querySelectorAll('.ks3-dsort-block .ks3-b5c-opt[data-owner="dandelion"]'); H.click(o[1]); await H.sleep(150);""",
         back="""H.pressed(document.querySelectorAll('.ks3-dsort-block .ks3-b5c-opt[data-owner="dandelion"]')[1])""",
         blank="""!H.pressed(document.querySelectorAll('.ks3-dsort-block .ks3-b5c-opt[data-owner="dandelion"]')[1])"""),
    dict(name="picks not yet closed", page="/combined/higher/physics/electricity/series-parallel-circuits.html",
         type="""await H.sleep(2500); var q = H.v().qs; H.click(H.rootBtn(q[0].opts[0].label, 0)); await H.sleep(150);""",
         back="(function(){ var s = H.rootState(); return s.preds[s.step][0] === 0 && !s.revealed[s.step]; })()",
         blank="(function(){ var s = H.rootState(); return !(s.preds[s.step] || []).length; })()",
         send="""var q = H.v().qs; for (var i = 1; i < q.length; i += 1) { H.click(H.rootBtn(H.v().qs[i].opts[0].label, i)); await H.sleep(100); } await H.call('onReveal'); await H.sleep(250);""",
         sent=lambda b: b and b[0]["time_spent_seconds"] is not None and b[0]["time_spent_seconds"] >= 2),
]


def run_drafts(sport, aport, width, ok, only=None):
    base = "http://127.0.0.1:%d" % sport
    def one(d):
        print("\n── draft: %s" % d["name"])
        LEDGER.reset()
        with KB.Browser() as br:
            pg = open_page(br, sport, aport, d["page"], session(True), width)
            wait_saved(pg)
            run_act(pg, d["type"])
            time.sleep(0.9)
            pg.goto("%s%s?api=http://127.0.0.1:%d" % (base, d["page"], aport), settle=1.0)
            pg.eval(HELPERS)
            wait_saved(pg)
            time.sleep(0.5)
            try:
                came = pg.eval("!!(%s)" % d["back"]) is True
            except KB.JSError:
                came = False
            ok(came, "a draft comes back on the same device", pg.eval("JSON.stringify(Object.keys(localStorage).filter(function (k) { return /draft/.test(k); }).map(function (k) { return [k, localStorage.getItem(k).slice(0, 200)]; }))"))
            ok(not LEDGER.bodies, "a draft posts nothing", LEDGER.bodies)
            if d.get("send"):
                run_act(pg, d["send"])
                time.sleep(0.5)
                ok(bool(d["sent"](LEDGER.bodies)), "the answer's time includes the draft", [(x.get("question_id"), x.get("time_spent_seconds")) for x in LEDGER.bodies])
                LEDGER.reset()
        with KB.Browser() as br:
            pg = open_page(br, sport, aport, d["page"], session(True), width)
            wait_saved(pg)
            time.sleep(0.4)
            ok(pg.eval("!!(%s)" % d["blank"]) is True, "a draft never reaches another device")

    # A Chrome that stops answering is not a finding: once more, then it counts.
    for d in DRAFTS:
        if only and not re.search(only, "draft " + d["name"]):
            continue
        try:
            one(d)
        except KB.CDPError as e:
            print("  ⟳ Chrome stopped answering (%s), once more" % str(e)[:80], flush=True)
            one(d)


def run_best(sport, aport, width, ok):
    """⊕ 9 Nov 2026: "Best before today" reads the saved rows: same on every device, and
    today's own answers are never before today."""
    page = "/combined/higher/biology/organisation/heart-blood-vessels.html"
    items_js = """JSON.stringify((function () { var R = H.block('Ks4Practice').logic.props.rungs, out = [];
        ['r1', 'r2', 'r3', 'r4'].forEach(function (k, ri) { (R[k] || []).forEach(function (it, n) {
          var good = (it.options || []).filter(function (o) { return o && o.correct; })[0];
          out.push({ id: 'ks4:heart-blood-vessels:ch#r' + (ri + 1) + '-' + (n + 1), answer: good ? (good.text || good.label || '') : 'x', kind: it.kind || 'mcq' });
        }); });
        return out; })())"""
    def row(it, when):
        return {"question_id": it["id"], "rung": it["id"].split("#")[1].split("-")[0], "answer_kind": "choice" if it["kind"] == "mcq" else "written",
                "question_text": "q", "answer": it["answer"], "correct_answer": it["answer"], "is_correct": True, "marks_scored": 1, "marks_available": 1,
                "points_hit": None, "points_total": None, "feedback": None, "mark_level": None, "mark_next_step": None, "marked_by": "key",
                "self_ticks": None, "attempt_no": 1, "answered_at": when, "surface": "lesson", "work_item_id": None,
                "key_stage": "KS4", "lesson_slug": "heart-blood-vessels", "client_event_id": it["id"]}
    now = _dt.datetime.now(_dt.timezone.utc)
    today, yesterday = now.isoformat(), (now - _dt.timedelta(days=2)).isoformat()
    print("\n── best before today")
    LEDGER.reset()
    with KB.Browser() as br:
        pg = open_page(br, sport, aport, page, session(True), width)
        wait_saved(pg)
        time.sleep(0.4)
        items = json.loads(pg.eval(items_js))
        ok(len(items) == 7, "the practice block has its seven questions", items)
        pg.eval("localStorage.setItem('ks4-best-heart-blood-vessels', '4')")
        pg.goto("http://127.0.0.1:%d%s?api=http://127.0.0.1:%d" % (sport, page, aport), settle=1.0)
        pg.eval(HELPERS)
        wait_saved(pg)
        time.sleep(0.4)
        ok(pg.eval("H.block('Ks4Practice').logic.state.best") is None, "no saved rows: this device's old number is not used")
    for name, rows, want in (("answered today", [row(i, today) for i in items], None),
                             ("answered on an earlier day", [row(i, yesterday) for i in items], 4),
                             ("an earlier day, one question missing", [row(i, yesterday) for i in items[:-1]], None)):
        LEDGER.reset()
        LEDGER.rows.extend(rows)
        with KB.Browser() as br:
            pg = open_page(br, sport, aport, page, session(True), width)
            wait_saved(pg)
            time.sleep(0.6)
            ok(pg.eval("H.block('Ks4Practice').logic.state.best") == want, "%s: best is %s" % (name, want), pg.eval("H.block('Ks4Practice').logic.state.best"))
            shown = pg.eval("/Best before today/.test(document.body.innerText)")
            ok(shown is (want is not None), "%s: the page says so" % name)
    LEDGER.reset()


def session(child):
    email = ("11111111-2222-4333-8444-555555555555@children.mrbadmus.internal" if child else "pupil@rainford.example")
    return {"access_token": "fake-token", "refresh_token": "fake-refresh", "token_type": "bearer",
            "expires_in": 3600, "expires_at": int(time.time()) + 24 * 3600,
            "user": {"id": "11111111-2222-4333-8444-555555555555", "email": email}}


# The pupil comparison holds Math.random still: the Start-here guess shuffles its
# options per page load (KS4 R20, KS3 shuffleGuess), so without this two runs of
# the SAME code differ. Nothing else is pinned, and the comparison is untouched.
PIN_RANDOM = """(function () {
  var s = 0x2F6E2B1;
  Math.random = function () {
    s = (s + 0x6D2B79F5) | 0;
    var t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
})();"""


def open_page(br, site, api, page, sess, width, pin_random=False):
    pg = br.attach()
    pg.set_viewport(width, 900)
    if pin_random:
        pg.send("Page.enable")
        pg.send("Page.addScriptToEvaluateOnNewDocument", {"source": PIN_RANDOM})
    pg.send("Network.enable")
    pg.send("Network.setBlockedURLs", {"urls": OFF_BOX})
    base = "http://127.0.0.1:%d" % site
    pg.goto(base + "/404.html")
    pg.eval("localStorage.clear(); %s" % ("localStorage.setItem(%s, %s)" % (json.dumps(AUTH_KEY), json.dumps(json.dumps(sess))) if sess else ""))
    pg.goto("%s%s?api=http://127.0.0.1:%d" % (base, page, api), settle=1.2)
    pg.eval(HELPERS)
    return pg


def wait_saved(pg, timeout=15):
    t0 = time.time()
    while time.time() - t0 < timeout:
        st = pg.eval("window.MrBadmusSaved ? window.MrBadmusSaved.state : 'none'")
        if st in ("done", "none"):
            return st
        time.sleep(0.2)
    return "timeout"


def run_act(pg, js):
    return pg.eval("(async function(){ %s; return true; })()" % js, timeout=60)


def id_ok(want, got):
    if want.endswith("*"):
        return any(g.startswith(want[:-1]) for g in got)
    if "*" in want:
        a, b = want.split("*", 1)
        return any(g.startswith(a) and g.endswith(b) for g in got)
    return want in got


def validate(bodies):
    """Every body through the backend's own validateAnswerBody."""
    js = ("const A=require(%s);let bad=[];for(const b of JSON.parse(require('fs').readFileSync(0,'utf8'))){"
          "const v=A.validateAnswerBody(b);if(v.error)bad.push([b.question_id,v.error]);}"
          "process.stdout.write(JSON.stringify(bad));") % json.dumps(os.path.join(BACKEND, "consumer", "answers.js"))
    r = subprocess.run(["node", "-e", js], input=json.dumps(bodies), capture_output=True, text=True, cwd=BACKEND)
    if r.returncode != 0:
        return [["(validator did not run)", r.stderr[-300:]]]
    return json.loads(r.stdout or "[]")


# ── --sweep: every KS3 kind in <ks3-specs>, one page each, its first control ──
SWEEP_JS = r"""
window.SW = {
  sec: function (k) { if (k === 'ks4') { return document.getElementById('ks4-mount'); } return Array.prototype.filter.call(document.querySelectorAll('[data-instrument]'), function (s) { return s.classList.contains(k); })[0]; },
  sig: function (sec) {
    return JSON.stringify({
      p: Array.prototype.map.call(sec.querySelectorAll('[aria-pressed]'), function (b) { return b.getAttribute('aria-pressed'); }).join(''),
      v: Array.prototype.map.call(sec.querySelectorAll('input, select, textarea'), function (i) { return i.type === 'range' ? '' : String(i.value); }).join('|')
    });
  },
  go: async function (k) {
    var sleep = function (ms) { return new Promise(function (r) { setTimeout(r, ms); }); };
    var sp = window.MrBadmusAnswerCapture.ks3Specs[k], sec = SW.sec(k);
    if (!sec || !sp) { throw new Error('no block or no spec'); }
    var all = function (root, sel) {
      return Array.prototype.filter.call(root.querySelectorAll(typeof sel === 'function' ? 'button' : sel), function (b) { return typeof sel === 'function' ? sel(b) : true; });
    };
    var live = function (b) { return !b.disabled && b.getAttribute('aria-disabled') !== 'true'; };
    var shown = function (b) { return !b.closest('[hidden]') && b.getClientRects().length > 0; };
    var firstOf = function (list) { return list.filter(function (b) { return live(b) && shown(b) && b.getAttribute('aria-pressed') !== 'true'; })[0] || list.filter(live)[0]; };
    var press = function (b) { if (!b) { throw new Error('no control to press'); } b.scrollIntoView({ block: 'center' }); b.click(); };
    if (sp.t === 'u') {
      if (sp.tab) { var tb = all(sec, sp.tab).filter(shown)[0]; if (tb && tb.getAttribute('aria-pressed') !== 'true') { press(tb); await sleep(60); } }
      if (sp.first) { press(sec.querySelector(sp.first)); await sleep(60); }
      press(firstOf(all(sec, sp.opt)));
      await sleep(80);
      if (sp.commit) { press(firstOf(all(sec, sp.commit))); }
    } else if (sp.t === 'c') {
      Array.prototype.filter.call(sec.querySelectorAll(sp.part), shown).forEach(function (part) {
        var opts = part.matches(sp.opt) ? [part] : Array.prototype.slice.call(part.querySelectorAll(sp.opt));
        var b = opts.filter(function (o) { return live(o) && shown(o); })[0];
        if (b && b.getAttribute('aria-pressed') !== 'true') { press(b); }
        if (sp.whole && !sp.toggle) { return; }
      });
      await sleep(80);
      press(all(sec, sp.check).filter(shown)[0] || all(sec, sp.check)[0]);
    } else if (sp.t === 't') {
      if (sp.opt) {
        // Every step's own group: the page's Check waits for all of them.
        var seen = {};
        all(sec, sp.opt).forEach(function (o) { var g = o.getAttribute('data-group') || ''; if (!seen[g]) { seen[g] = 1; press(o); } });
        await sleep(40);
      }
      Array.prototype.forEach.call(sec.querySelectorAll(sp.inputs), function (i) {
        if (i.tagName === 'SELECT') { i.selectedIndex = i.options.length > 1 ? 1 : 0; }
        else { i.value = '12.5 because the reading stays the same when it is repeated'; }
        i.dispatchEvent(new Event('input', { bubbles: true })); i.dispatchEvent(new Event('change', { bubbles: true }));
      });
      await sleep(60);
      press(all(sec, sp.check).filter(shown)[0] || all(sec, sp.check)[0]);
    } else if (sp.t === 'o') {
      var steps = all(sec, sp.step);
      for (var n = 0; n < steps.length; n += 1) { if (live(steps[n])) { press(steps[n]); await sleep(30); } }
    } else if (sp.t === 'l') {
      if (k === 'ks3-cbal-block') {
        var eq = sec.querySelector('[data-cbal-eq]:not([hidden])') || sec.querySelector('[data-cbal-eq]');
        press(eq.querySelector('[data-cbal-for="0"][data-cbal-delta="1"]')); await sleep(40);
        press(eq.querySelector('[data-cbal-for="2"][data-cbal-delta="1"]'));
      } else { press(firstOf(all(sec, sp.press))); }
    }
    await sleep(400);
    return SW.sig(sec);
  }
};
"""


# ── --units: every unit of one page of every kind ─────────────────────────
# The sweep presses a block's FIRST control, so it cannot see several separately
# judged items sharing an id. This presses the first free button of EVERY group of
# sibling buttons in the block, in turn, as new groups appear, and watches what was
# posted: two groups under one id is a finding; a self-checked row beside words the
# press revealed is listed to be read.
CONTROL_WORD = re.compile(r"^(drop|run|start|next|check|go(?= *$)|send|play|add|test|show|reveal|close|press|try again|reset)\b", re.I)
# "Run step 2" moves a lesson on after its verdict; it commits nothing.
COMMIT_WORD = re.compile(r"^(run(?! step)|check|close|send|reveal|test|show|mark|start(?! again)|submit|light|fire|switch|see)\b", re.I)
# A pick that unlocks the next step of a lesson rather than committing an answer.
COMMIT_NAMED = ["giant-covalent-structures qOpts"]
# Form rows whose answer the lesson does not hold in a sentence: named, see SAVE-COVERAGE.
FORM_NO_KEY = set()
SPEC_NO_KEY = set()
UNITS_JS = r"""
window.UN = {
  // What must come back: every pressed control. A tab on screen is allowed to differ.
  sig: function (sec) {
    return Array.prototype.filter.call(sec.querySelectorAll('[aria-pressed]'), function (b) {
      return !/tab|seg-btn/.test(b.className || '') && !b.closest('[role="tablist"]');
    }).map(function (b) { return b.getAttribute('aria-pressed') === 'true' ? '1' : '0'; }).join('');
  },
  sec: function (k) { if (k === 'ks4') { return document.getElementById('ks4-mount'); } return Array.prototype.filter.call(document.querySelectorAll('[data-instrument]'), function (s) { return s.classList.contains(k); })[0]; },
  lines: function (sec) {
    var out = {};
    Array.prototype.forEach.call(sec.querySelectorAll('p, li, strong, dd, td, h3, h4'), function (el) {
      if (el.closest('button') || el.closest('[hidden]') || !el.getClientRects().length) { return; }
      var t = (el.textContent || '').replace(/\s+/g, ' ').trim();
      if (t) { out[t] = 1; }
    });
    return out;
  },
  go: async function (k) {
    var sleep = function (ms) { return new Promise(function (r) { setTimeout(r, ms); }); };
    var sec = UN.sec(k);
    if (!sec) { throw new Error('no block'); }
    // A group is the buttons of one question: a list's <li>s are one group.
    var groupOf = function (x) { return (x.parentElement && x.parentElement.tagName === 'LI' && x.parentElement.parentElement) || x.parentElement; };
    var live = function (x) { return !x.disabled && x.getAttribute('aria-disabled') !== 'true' && !x.closest('[hidden]') && x.getClientRects().length > 0; };
    var clicked = [], used = [], steps = [];
    // Answers sent, counted per press: the difference between a post at the press and one at its commit.
    window.__unSent = 0;
    if (!window.__unFetch) {
      window.__unFetch = window.fetch;
      window.fetch = function (u, o) {
        if (o && o.method === 'POST' && /answer/.test(String(u))) { window.__unSent += 1; }
        return window.__unFetch.apply(this, arguments);
      };
    }
    var press = async function (b) {
      var sentAt = window.__unSent;
      clicked.push(b);
      var before = UN.lines(sec), liveBefore = Array.prototype.filter.call(sec.querySelectorAll('button'), live);
      b.scrollIntoView({ block: 'center' }); b.click();
      await sleep(90);
      var after = UN.lines(sec), added = Object.keys(after).filter(function (t) { return !before[t]; });
      // A button this press has just made pressable: what a per-tap post would come before.
      var opened = Array.prototype.filter.call(sec.querySelectorAll('button'), live).filter(function (x) { return liveBefore.indexOf(x) < 0; })
        .map(function (x) { return (x.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40); });
      steps.push({ label: (b.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 50), added: added.join(' / ').slice(0, 200), opened: opened, posted: window.__unSent > sentAt });
    };
    var filled = [];
    for (var n = 0; n < (k === 'ks4' ? 110 : 70); n += 1) {
      // A KS4 lesson's own typed boxes and dropdowns: something in each, once, so its Check can be pressed.
      if (k === 'ks4') {
        Array.prototype.forEach.call(sec.querySelectorAll('input:not([type=checkbox]):not([type=radio]):not([type=range]), select'), function (f) {
          if (filled.indexOf(f) >= 0 || f.disabled || f.closest('[hidden]') || !f.getClientRects().length) { return; }
          filled.push(f);
          if (f.tagName === 'SELECT') { if (f.options.length > 1) { f.selectedIndex = 1; } } else { f.value = '1'; }
          f.dispatchEvent(new Event('input', { bubbles: true })); f.dispatchEvent(new Event('change', { bubbles: true }));
        });
        await sleep(30);
      }
      var all = Array.prototype.filter.call(sec.querySelectorAll('button'), live);
      // First the first free button of a group not yet answered; a group that has
      // been reset (nothing pressed in it) counts as free again.
      var b = all.filter(function (x) {
        var g = groupOf(x);
        if (used.indexOf(g) < 0) { return clicked.indexOf(x) < 0; }
        return false;
      })[0];
      if (b) { used.push(groupOf(b)); await press(b); continue; }
      // Then a button never pressed: a tab that may bring a new question up.
      b = all.filter(function (x) { return clicked.indexOf(x) < 0; })[0];
      if (!b) { break; }
      var g2 = groupOf(b);
      await press(b);
      // Whatever it brought up can be answered again.
      used = used.filter(function (g) { return g === g2 || !g.querySelector('[aria-pressed="false"]') || g.querySelector('[aria-pressed="true"]'); });
    }
    return JSON.stringify({ groups: used.length, steps: steps, sig: UN.sig(sec) });
  }
};
"""


def run_units(sport, aport, width, only):
    js = open(os.path.join(REPO, "shared", "mrbadmus.v2.js"), encoding="utf-8").read()
    block = js[js.find("/* <ks3-specs> */"):js.find("/* </ks3-specs> */")]
    kinds = set(re.findall(r"'(ks3-[a-z0-9-]+)'\s*:", block))
    for name in ("KIND_A", "KIND_B5C"):
        m = re.search(r"var %s = (\{.*?\});" % name, js)
        kinds |= set(json.loads(m.group(1)))
    kinds = sorted(kinds)
    import glob
    found = {}
    for p in sorted(glob.glob(os.path.join(REPO, "ks3", "**", "*.html"), recursive=True)):
        with open(p, encoding="utf-8") as f:
            h = f.read()
        for k in kinds:
            if k not in found and re.search(r'<section[^>]*class="[^"]*\b%s(?![\w-])[^"]*"[^>]*data-instrument' % re.escape(k), h):
                found[k] = "/" + os.path.relpath(p, REPO)
    base = "http://127.0.0.1:%d" % sport
    shared, listed, differs, n_ok, t0 = [], [], [], 0, time.time()
    swept = {"wrong without an answer": [], "self-checked": [], "a control's label as the answer": [], "posted per tap, with a commit it opened": []}
    with KB.Browser() as br:
        pg = br.attach()
        pg.set_viewport(width, 900)
        pg.send("Network.enable")
        pg.send("Network.setBlockedURLs", {"urls": OFF_BOX})
        fresh = "localStorage.clear(); sessionStorage.clear(); localStorage.setItem(%s, %s)" % (json.dumps(AUTH_KEY), json.dumps(json.dumps(session(True))))
        for k in kinds:
            if only and not re.search(only, k):
                continue
            if k not in found:
                print("  -- %s: no page carries it" % k, flush=True)
                continue
            LEDGER.reset()
            try:
                pg.goto(base + "/404.html")
                pg.eval(fresh)
                pg.goto("%s%s?api=http://127.0.0.1:%d" % (base, found[k], aport), settle=0.4)
                wait_saved(pg)
                pg.eval(UNITS_JS)
                r = json.loads(pg.eval("UN.go(%s)" % json.dumps(k), timeout=60))
                time.sleep(0.4)
            except Exception as e:  # noqa: BLE001
                print("  !! %s: %s" % (k, str(e)[:120]), flush=True)
                continue
            act_prefix = found[k].rsplit("/", 1)[-1].replace(".html", "") + "#"
            bodies = [b for b in LEDGER.bodies if (b.get("question_id") or "").startswith(act_prefix)]
            import collections
            n_id = collections.Counter(b["question_id"] for b in bodies)
            # One id asked about different things: the question words differ between its rows.
            words = collections.defaultdict(set)
            for b in bodies:
                words[b["question_id"]].add(b.get("question_text") or "")
            dup = {i: len(t) for i, t in words.items() if len(t) > 1}
            self_c = [b for b in bodies if b.get("is_correct") is None]
            # ⊕ 9 Nov 2026: the shapes the blind runs keep finding, listed for every kind.
            for b in bodies:
                if b.get("is_correct") is False and not b.get("correct_answer"):
                    swept["wrong without an answer"].append((k, b["question_id"]))
                if b.get("self_checked") is True:
                    swept["self-checked"].append((k, b["question_id"]))
                if CONTROL_WORD.match(str(b.get("answer") or "")):
                    swept["a control's label as the answer"].append((k, b["question_id"], b["answer"]))
            for st in r["steps"]:
                commit = [x for x in st.get("opened") or [] if COMMIT_WORD.match(x)]
                if commit and st.get("posted"):
                    swept["posted per tap, with a commit it opened"].append((k, st["label"], commit[:2]))
            line = "%s groups=%d posts=%d ids=%d selfchecked=%d" % (k, r["groups"], len(bodies), len(n_id), len(self_c))
            if dup:
                shared.append((k, found[k], dup))
                line += " SHARED=%s Q=%s" % (json.dumps(dup), json.dumps(sorted(list(words.values())[0])[:2], ensure_ascii=False)[:200])
            if self_c:
                reveal = [s2["added"] for s2 in r["steps"] if s2["added"]][:2]
                listed.append((k, found[k], reveal))
                line += " SAW=%s" % json.dumps(reveal, ensure_ascii=False)[:260]
            # Device B: every row back, nothing posted.
            if bodies:
                n_b = len(LEDGER.bodies)
                try:
                    pg.goto(base + "/404.html")
                    pg.eval(fresh)
                    pg.goto("%s%s?api=http://127.0.0.1:%d" % (base, found[k], aport), settle=0.4)
                    wait_saved(pg)
                    pg.eval(UNITS_JS)
                    time.sleep(0.4)
                    back = pg.eval("UN.sig(UN.sec(%s))" % json.dumps(k))
                    if back != r["sig"]:
                        differs.append(k)
                        line += " B-DIFFERS A=%s B=%s" % (r["sig"][:40], back[:40])
                    if len(LEDGER.bodies) != n_b:
                        differs.append(k)
                        line += " B-POSTED=%d" % (len(LEDGER.bodies) - n_b)
                except Exception as e:  # noqa: BLE001
                    line += " B-ERROR %s" % str(e)[:60]
            print("  " + line, flush=True)
            n_ok += 1
    print("\nunits: %d kinds pressed in full, %d with an id shared by different questions, %d with self-checked rows to read, %d whose presses did not all come back, %.0f s" % (n_ok, len(shared), len(listed), len(differs), time.time() - t0))
    for name, rows in swept.items():
        print("\n%s: %d" % (name, len(rows)))
        for row in rows:
            print("   ", row)
    return shared


# ── --commits: what can be read without a browser ─────────────────────────
def run_commits():
    """Lists every instance of a shape from the source, so a new lesson cannot bring one in unseen:
    a group that posts per tap before its own commit; a ROOT_FORMS row that judges and gives no
    right answer; a draft key the lesson does not have; a count that would drop on reload."""
    import glob, subprocess
    js = open(os.path.join(REPO, "shared", "mrbadmus.v2.js"), encoding="utf-8").read()
    bad = 0
    pages = {}
    for p in sorted(glob.glob(os.path.join(REPO, "combined", "higher", "*", "*", "*.html")) + glob.glob(os.path.join(REPO, "triple", "higher", "*", "*", "*.html"))):
        with open(p, encoding="utf-8") as f:
            if "MrBadmusKS4Runtime.mount" in f.read():
                pages.setdefault(os.path.basename(p)[:-5], os.path.relpath(p, REPO))
    out = subprocess.run(["node", "tools/kp_commit_scan.js"], input="\n".join(pages.values()), cwd=REPO, capture_output=True, text=True, timeout=300)
    named = {tuple(x.split()[:2]) for x in COMMIT_NAMED}
    rows = [ln for ln in out.stdout.splitlines() if ln.strip()]
    loose = [ln for ln in rows if tuple(ln.split()[:2]) not in named]
    print("commit scan: %d lessons, %d groups a pick unlocks, %d named as not a commit, %d posting before a commit" % (len(pages), len(rows), len(rows) - len(loose), len(loose)))
    for ln in loose:
        print("   per tap:", ln)
    bad += len(loose)
    if out.returncode:
        print(out.stderr[:400])
        bad += 1
    # A draft key must be a key of the lesson's own state.
    m = re.search(r"var ROOT_DRAFT = (\{.*?\});", js, re.S)
    for slug, keys in re.findall(r"'([a-z0-9-]+)': \[([^\]]*)\]", m.group(1)):
        if slug not in pages:
            print("   draft: no lesson called", slug)
            bad += 1
            continue
        with open(os.path.join(REPO, pages[slug]), encoding="utf-8") as f:
            h = f.read()
        j = h.rfind("class Component extends DCLogic")
        head = h[j:h.find("renderVals", j)]
        for k in re.findall(r"'(\w+)'", keys):
            if not re.search(r"\b%s\s*:" % k, head):
                print("   draft: %s has no %s in its state" % (slug, k))
                bad += 1
    # A count on a block that takes no answer must be on the local list.
    kinds = json.load(open(os.path.join(REPO, "tools", "ks3_instrument_shapes.json"), encoding="utf-8"))["kinds"]
    want = set()
    for p in glob.glob(os.path.join(REPO, "ks3", "*", "*", "*.html")):
        with open(p, encoding="utf-8") as f:
            h = f.read()
        for mm in re.finditer(r'<section[^>]*class="[^"]*\b(ks3-[a-z0-9-]+-block)\b[^"]*"[^>]*data-instrument', h):
            end = h.find("</section>", mm.end())
            if (kinds.get(mm.group(1)) or {}).get("shape") == "X" and "data-count" in h[mm.end():end]:
                want.add(mm.group(1)[4:-6])
    have = set(re.search(r"<ks3-count-local> \*/ /\\bks3-\(([^)]*)\)", js).group(1).split("|"))
    print("local counts: %d kinds on the list, %d in the pages" % (len(have), len(want)))
    for k in sorted(want - have):
        print("   count: ks3-%s-block is not on the list" % k)
        bad += 1
    for k in sorted(have - want):
        print("   count: ks3-%s-block is listed and no page has one" % k)
    # A form row that judges and names no right answer.
    block = js[js.find("/* <ks4-root-forms> */"):js.find("/* </ks4-root-forms> */")]
    slug, loose_rows = None, []
    for ln in block.splitlines():
        h2 = re.match(r"\s{8}'([a-z0-9-]+)':", ln)
        if h2:
            slug = h2.group(1)
        if re.search(r"\bok: (?!null|true,)", ln) and "good:" not in ln and slug:
            loose_rows.append((slug, ln.strip()[:90]))
    print("form rows that judge and name no right answer: %d (TYPED_NO_KEY names the ones the lesson cannot answer)" % len(loose_rows))
    for row in loose_rows:
        if row[0] not in FORM_NO_KEY:
            print("   no answer:", row)
            bad += 1
    # A KS3 spec that judges and names no right answer.
    specs = js[js.find("/* <ks3-specs> */"):js.find("/* </ks3-specs> */")]
    chunks = re.split(r"(?m)^(?=\s{8}'ks3-[a-z0-9-]+':)", specs)
    no_key = []
    for ch in chunks:
        m2 = re.match(r"\s{8}'(ks3-[a-z0-9-]+)':", ch)
        if m2 and "right:" in ch and "key:" not in ch and not re.search(r"good: (?!null)", ch):
            no_key.append(m2.group(1))
    print("KS3 specs that judge and name no right answer: %d" % len(no_key))
    for k in no_key:
        if k not in SPEC_NO_KEY:
            print("   no answer:", k)
            bad += 1
    print("commits: %s" % ("clean" if not bad else "%d to read" % bad))
    return bad


# ── --units-ks4: every rebuilt lesson, every control pressed ──────────────
def run_units_ks4(sport, aport, width, only):
    import glob, collections
    pages = {}
    for p in sorted(glob.glob(os.path.join(REPO, "combined", "higher", "*", "*", "*.html")) + glob.glob(os.path.join(REPO, "triple", "higher", "*", "*", "*.html"))):
        with open(p, encoding="utf-8") as f:
            if "MrBadmusKS4Runtime.mount" in f.read():
                pages.setdefault(os.path.basename(p)[:-5], "/" + os.path.relpath(p, REPO))
    base = "http://127.0.0.1:%d" % sport
    swept = {"wrong without an answer": [], "self-checked": [], "a control's label as the answer": [], "same id posted again": [], "posted per tap, with a commit it opened": []}
    n_ok, posts = 0, 0
    fresh = "localStorage.clear(); sessionStorage.clear(); localStorage.setItem(%s, %s)" % (json.dumps(AUTH_KEY), json.dumps(json.dumps(session(True))))
    items = [(s2, pg2) for s2, pg2 in sorted(pages.items()) if not only or re.search(only, s2)]
    if os.environ.get("MRB_SLICE"):
        lo, hi = os.environ["MRB_SLICE"].split(":")
        items = items[int(lo):int(hi)]
    while items:
        try:
            with KB.Browser() as br:
                pg = br.attach()
                pg.set_viewport(width, 900)
                pg.send("Network.enable")
                pg.send("Network.setBlockedURLs", {"urls": OFF_BOX})
                while items:
                    slug, page = items.pop(0)
                    LEDGER.reset()
                    pg.goto(base + "/404.html")
                    pg.eval(fresh)
                    pg.goto("%s%s?api=http://127.0.0.1:%d" % (base, page, aport), settle=0.5)
                    wait_saved(pg)
                    pg.eval(UNITS_JS)
                    r = json.loads(pg.eval("UN.go('ks4')", timeout=90))
                    time.sleep(0.3)
                    n_ok += 1
                    bodies = list(LEDGER.bodies)
                    posts += len(bodies)
                    for b in bodies:
                        q = b.get("question_id") or ""
                        if b.get("is_correct") is False and not b.get("correct_answer"):
                            swept["wrong without an answer"].append((q, b.get("kind")))
                        if b.get("self_checked") is True:
                            swept["self-checked"].append((q,))
                        if CONTROL_WORD.match(str(b.get("answer") or "")):
                            swept["a control's label as the answer"].append((q, b.get("answer")))
                    for st in r["steps"]:
                        commit = [x for x in st.get("opened") or [] if COMMIT_WORD.match(x)]
                        if commit and st.get("posted"):
                            swept["posted per tap, with a commit it opened"].append((slug, st["label"], commit[:2]))
                    again = collections.Counter(b["question_id"] for b in bodies if b.get("question_id"))
                    for q, c in again.items():
                        if c > 1:
                            swept["same id posted again"].append((q, c))
                    print("  %s posts=%d" % (slug, len(bodies)), flush=True)
        except Exception as e:  # noqa: BLE001
            print("  !! %s: %s" % (slug, str(e)[:100]), flush=True)
    print("\nunits-ks4: %d lessons pressed, %d answers" % (n_ok, posts))
    for name, rows in swept.items():
        print("\n%s: %d" % (name, len(rows)))
        for row in rows:
            print("   ", row)
    return 0


def sweep_pages():
    js = open(os.path.join(REPO, "shared", "mrbadmus.v2.js"), encoding="utf-8").read()
    block = js[js.find("/* <ks3-specs> */"):js.find("/* </ks3-specs> */")]
    kinds = sorted(set(re.findall(r"'(ks3-[a-z0-9-]+)'\s*:", block)))
    found = {}
    import glob
    for p in sorted(glob.glob(os.path.join(REPO, "ks3", "**", "*.html"), recursive=True)):
        with open(p, encoding="utf-8") as f:
            h = f.read()
        for k in kinds:
            if k not in found and re.search(r'<section[^>]*class="[^"]*\b%s(?![\w-])[^"]*"[^>]*data-instrument' % re.escape(k), h):
                found[k] = "/" + os.path.relpath(p, REPO)
    return kinds, found


def run_sweep(sport, aport, width, only):
    kinds, found = sweep_pages()
    base = "http://127.0.0.1:%d" % sport
    fails, ok_n, bodies = [], 0, []
    t0 = time.time()
    with KB.Browser() as br:
        pg = br.attach()
        pg.set_viewport(width, 900)
        pg.send("Network.enable")
        pg.send("Network.setBlockedURLs", {"urls": OFF_BOX})
        fresh = "localStorage.clear(); sessionStorage.clear(); localStorage.setItem(%s, %s)" % (json.dumps(AUTH_KEY), json.dumps(json.dumps(session(True))))
        def load(page):
            pg.goto(base + "/404.html")
            pg.eval(fresh)
            pg.goto("%s%s?api=http://127.0.0.1:%d" % (base, page, aport), settle=0.5)
            st = wait_saved(pg)
            pg.eval(SWEEP_JS)
            return st
        for k in kinds:
            if only and not re.search(only, k):
                continue
            if k not in found:
                fails.append((k, "no page carries it"))
                continue
            page = found[k]
            LEDGER.reset()
            why = None
            try:
                load(page)
                a = pg.eval("SW.go(%s)" % json.dumps(k), timeout=30)
                time.sleep(0.5)
                got = list(LEDGER.bodies)
                if not got:
                    why = "the first control posted nothing"
                elif got[-1].get("question_id", "").split("#")[0] != page.rsplit("/", 1)[-1].replace(".html", ""):
                    why = "posted a foreign id " + str(got[-1].get("question_id"))
                else:
                    bodies.extend(got)
                    n = len(LEDGER.bodies)
                    st = load(page)
                    time.sleep(0.4)
                    b = pg.eval("SW.sig(SW.sec(%s))" % json.dumps(k))
                    if st != "done":
                        why = "device B state " + st
                    elif a != b:
                        why = "device B differs\n   A " + a[:300] + "\n   B " + b[:300]
                    elif len(LEDGER.bodies) != n:
                        why = "device B posted while restoring"
            except Exception as e:  # noqa: BLE001 — a drive error is a finding
                why = "drive error: %s" % str(e)[:200]
            if why:
                fails.append((k, why))
                print("  ❌ %s  %s\n     %s" % (k, page, why), flush=True)
            else:
                ok_n += 1
    bad = validate(bodies)
    print("\nsweep: %d kinds of %d went A → valid body → B identical, %d failed, %d bodies, %d refused by the server's validator, %.0f s"
          % (ok_n, len(kinds), len(fails), len(bodies), len(bad), time.time() - t0))
    for b in bad[:10]:
        print("  validator:", b)
    return fails, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--units", action="store_true", help="every unit of one page of every KS3 kind: flags an id several separately judged items share")
    ap.add_argument("--sweep", action="store_true", help="every KS3 kind in <ks3-specs>: first control, valid body, back on device B")
    ap.add_argument("--only")
    ap.add_argument("--units-ks4", action="store_true", help="every rebuilt KS4 lesson, every control pressed: lists wrong-without-answer, control labels, self-checked, repeated ids")
    ap.add_argument("--commits", action="store_true", help="no browser: every group posting before its commit, every judged form row with no right answer, draft keys, local counts")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--no-pupil", action="store_true")
    ap.add_argument("--pupil-only", action="store_true", help="only the school-pupil comparisons")
    a = ap.parse_args()
    if a.commits:
        return 1 if run_commits() else 0
    site, sport = start(Site)
    api, aport = start(Api)
    if a.units_ks4:
        return run_units_ks4(sport, aport, a.width, a.only)
    if a.units:
        return 1 if run_units(sport, aport, a.width, a.only) else 0
    if a.sweep:
        f, b = run_sweep(sport, aport, a.width, a.only)
        return 1 if f or b else 0
    fails, passes, all_bodies = [], 0, []

    def ok(cond, what, detail=""):
        nonlocal passes
        if cond:
            passes += 1
            print("  ✅ " + what)
        else:
            fails.append(what)
            print("  ❌ " + what + (("\n       " + str(detail)[:600]) if detail != "" else ""))

    cases = [c for c in CASES if not a.only or re.search(a.only, c["name"])]

    def one_case(c):
        print("\n── %s  (%s, %dpx)" % (c["name"], c["page"], a.width))
        if c.get("retired"):
            good, why = retired_proof(c)
            ok(good, "retired: %s; its controls are gone and its ids are retired in docs/b2c/id-maps" % c["retired"], why)
            return
        LEDGER.reset()
        LEGACY["on"] = False
        THROTTLE["ticks"] = c.get("ticks429", 0)
        with KB.Browser() as br:
            pg = open_page(br, sport, aport, c["page"], session(True), a.width)
            wait_saved(pg)
            try:
                run_act(pg, c["act"])
            except Exception as e:  # noqa: BLE001 — a drive error is a finding
                ok(False, "device A: the presses ran", e)
                return
            time.sleep(1.5 + c.get("settle", 0))
            errs = [e for e in pg.console_errors() if "net::ERR_BLOCKED" not in e and "ERR_BLOCKED_BY_CLIENT" not in e and "429" not in e]
            # ⊕ 10 Nov 2026: the same device, reloaded: what was saved, not what was left on screen.
            if c.get("same"):
                if c.get("then"):
                    run_act(pg, c["then"])
                    time.sleep(0.8)
                n_same = len(LEDGER.bodies)
                pg.goto("http://127.0.0.1:%d%s?api=http://127.0.0.1:%d" % (sport, c["page"], aport), settle=1.0)
                pg.eval(HELPERS)
                wait_saved(pg)
                time.sleep(0.8 + c.get("settle_b", 0))
                same = pg.eval("(function(){ try { return !!(%s); } catch (e) { return 'ERR ' + e.message; } })()" % c["same"])
                ok(same is True, "same device, reloaded: what was saved", same)
                ok(len(LEDGER.bodies) == n_same, "same device: restoring sent nothing", LEDGER.bodies[n_same:])
        bodies = [b for b in LEDGER.bodies if not c.get("then") or b in LEDGER.bodies[:n_same]] if c.get("same") else list(LEDGER.bodies)
        all_bodies.extend(bodies)
        ids = [b.get("question_id") or "" for b in bodies]
        for w in c["want"]:
            ok(id_ok(w, ids), "device A saved %s" % w, ids)
        if c.get("check"):
            try:
                good = c["check"](bodies)
            except Exception as e:  # noqa: BLE001
                good, ids = False, "%s: %s" % (e, bodies)
            ok(good, "device A: right/wrong as the lesson judged it", [(b.get("question_id"), b.get("is_correct"), b.get("self_checked"), b.get("answer")) for b in bodies])
        if c.get("ticks"):
            ok(any(t.get("ticks") for t in LEDGER.ticks), "device A sent the level pick as the child's own tick", LEDGER.ticks)
            if c.get("tickcheck"):
                ok(c["tickcheck"](LEDGER.ticks), "the ticks reached the ledger in the shape the page keeps them", LEDGER.ticks)
        ok(all(isinstance(b.get("time_spent_seconds"), int) or b.get("time_spent_seconds") is None for b in bodies), "every body carries a measured time (or null)")
        ok(not errs, "device A: no page errors", errs)
        n_before = len(LEDGER.bodies)
        SLOW["path"] = c.get("slow_on_b")
        with KB.Browser() as br:
            pg = open_page(br, sport, aport, c["page"], session(True), a.width)
            st = wait_saved(pg)
            time.sleep(0.8 + c.get("settle_b", 0))
            SLOW["path"] = None
            back = pg.eval("(function(){ try { return !!(%s); } catch (e) { return 'ERR ' + e.message; } })()" % c["back"])
            ok(st == "done" and back is True, "device B (fresh profile): restored from /saved", "state=%s back=%s" % (st, back))
            time.sleep(1.0)
        ok(len(LEDGER.bodies) == n_before, "device B: restoring sent nothing", LEDGER.bodies[n_before:])


    # A Chrome that stops answering is not a finding about the page: once more, then it counts.
    for c in ([] if a.pupil_only else cases):
        p0, f0, b0 = passes, len(fails), len(all_bodies)
        try:
            one_case(c)
        except KB.CDPError as e:
            print("  ⟳ Chrome stopped answering (%s), once more" % str(e)[:80], flush=True)
            passes, fails[f0:], all_bodies[b0:] = p0, [], []
            SLOW["path"] = None
            try:
                one_case(c)
            except KB.CDPError as e2:
                ok(False, "%s: Chrome stopped answering twice" % c["name"], e2)

    if not a.pupil_only and (not a.only or any(re.search(a.only, "draft " + d["name"]) for d in DRAFTS)):
        run_drafts(sport, aport, a.width, ok, a.only)
    if not a.pupil_only and (not a.only or re.search(a.only, "best")):
        run_best(sport, aport, a.width, ok)

    if not a.no_pupil:
        for c in [c for c in cases if c["name"] in PUPIL]:
            print("\n── school pupil: %s" % c["name"])
            doms = []
            for legacy in (True, False):
                LEDGER.reset()
                LEGACY["on"] = legacy
                # A Chrome that stops answering is not a finding: once more, then it counts.
                for attempt in (1, 2):
                    try:
                        with KB.Browser() as br:
                            pg = open_page(br, sport, aport, c["page"], session(False), a.width, pin_random=True)
                            time.sleep(0.5)
                            glob_ = pg.eval("[typeof window.MrBadmusAnswerCapture, typeof window.MrBadmusKS4Tap, typeof window.MrBadmusSaved].join(',')")
                            try:
                                run_act(pg, c["act"])
                            except KB.CDPError:
                                raise
                            except Exception as e:  # noqa: BLE001
                                ok(False, "pupil presses ran (%s)" % ("old code" if legacy else "new code"), e)
                            time.sleep(1.2)
                            doms.append(pg.eval("document.documentElement.outerHTML"))
                        break
                    except KB.CDPError as e:
                        print("  ⟳ Chrome stopped answering (%s), once more" % str(e)[:80], flush=True)
                        if attempt == 2:
                            raise
                if not legacy:
                    ok(glob_ == "undefined,undefined,undefined", "pupil: no capture installed", glob_)
                    ok(not LEDGER.bodies and not LEDGER.ticks, "pupil: nothing posted", LEDGER.bodies)
            # A page that animates can land a frame either side between two runs
            # of the SAME code (changes-in-energy: 32, 33, 32). So the new page is
            # compared with what the old code produces, not with one sample of it.
            same = doms[0] == doms[1]
            for _ in range(3):
                if same:
                    break
                LEDGER.reset()
                LEGACY["on"] = True
                with KB.Browser() as br:
                    pg = open_page(br, sport, aport, c["page"], session(False), a.width, pin_random=True)
                    time.sleep(0.5)
                    run_act(pg, c["act"])
                    time.sleep(1.2)
                    same = pg.eval("document.documentElement.outerHTML") == doms[1]
            LEGACY["on"] = False
            if not same:
                import difflib
                d = list(difflib.unified_diff(doms[0].split(">"), doms[1].split(">"), lineterm="", n=0))[:12]
            ok(same, "pupil: the page DOM after the presses is identical to the previous code's", "" if same else "\n".join(d))

    bad = validate(all_bodies)
    print("\n── every recorded body through the backend's validateAnswerBody (%d bodies)" % len(all_bodies))
    ok(not bad, "the real server would accept every body", bad)
    print("\n%d passed, %d failed" % (passes, len(fails)))
    for f in fails:
        print("  ✗ " + f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
