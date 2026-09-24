#!/usr/bin/env python3
"""flashcard_decks_drive.py — MRB-351, the teacher's half of flashcard homework,
DRIVEN in a real headless Chrome against a stubbed data layer.

What it proves, each as a named check (exit 1 on any FAIL):

  SHEET (shared/set-work.js + shared/flashcard-decks.js)
  · the type chips sit at the top of the Classes step; Questions is the
    default and its flow still reaches Topic and Detail with the tree and the
    questions it always drew (the MCQ branch is not disturbed);
  · Flashcards lifts the cohort — a class outside the MCQ cohort is pickable;
  · Upload → progress ("Reading… 35%") → the review table, with the flagged,
    low-confidence and empty-sided rows SORTED TO THE TOP and the live count
    "5 cards · 1 needs an answer";
  · Save deck is DISABLED while a side is empty and enabled once filled;
    swap / delete / add / up-down / drag all do what they say;
  · Save posts `flashcard_deck_save` with p_finalise true, moves the sheet to
    Detail, and Set work posts `flashcard_set_work` with the EXACT payload —
    classes, deck, mode 'make', rule 'secure', release null, due as
    `londonToUtcIso(date, time)`, the note, a client_ref;
  · a server refusal (`due_before_release`) outlines the due fields, and the
    retry reuses the same client_ref;
  · a cached reply offers the two buttons and "Read it again" resends with
    force=1; Paste posts {paste,title}; Type opens three blank rows;
  · My decks → pick → Next → Ready-made + Quick + a later release post those;
  · MRBSetWork.edit({kind:'flashcards'}) reads the row and saves through
    `flashcard_edit_assignment`, keeping the stored note.

  LIBRARY (teacher/decks.html)
  · lists own decks with N cards / author / date / "Used in N assignments";
    a deleted deck in use stays, greyed "Deleted · used in 2 assignments";
    a deleted unused deck is absent; the Shared tab shows colleagues' ready
    shared decks only; search filters;
  · Duplicate calls the RPC and opens the copy in the review table;
    Share/Unshare and Delete (two presses) write the right rows.

  EVERYWHERE
  · no horizontal scroll at 360 and 390 (document AND sheet);
  · no visible text node is an explanatory sentence;
  · no console errors beyond the CDN script the container cannot reach.

⚠️ THE STUB MODELS WHAT RLS WOULD RETURN; IT DOES NOT PROVE RLS. The SQL half
is on TEST. This proves the page given those rows.

Screenshots: $MRB_SHOTS/mrb351-decks/ (default ~/tmp/ks3-gates/...).
"""
import json
import os
import sys
import time

import ks3_browser as cdp

T = "11111111-1111-4111-8111-111111111111"          # the teacher
COL = "22222222-2222-4222-8222-222222222222"        # a colleague
C1 = "c1c1c1c1-0000-4000-8000-000000000001"
C2 = "c2c2c2c2-0000-4000-8000-000000000002"
C3 = "c3c3c3c3-0000-4000-8000-000000000003"
D1 = "d1d1d1d1-0000-4000-8000-000000000001"
D2 = "d2d2d2d2-0000-4000-8000-000000000002"
D3 = "d3d3d3d3-0000-4000-8000-000000000003"
D4 = "d4d4d4d4-0000-4000-8000-000000000004"
D5 = "d5d5d5d5-0000-4000-8000-000000000005"
D6 = "d6d6d6d6-0000-4000-8000-000000000006"
DN = "dededede-0000-4000-8000-00000000000e"
J1 = "a0a0a0a0-0000-4000-8000-0000000000j1".replace("j", "a")
A1 = "a1a1a1a1-0000-4000-8000-000000000001"


def deck(id_, title, n, by, shared=True, status="ready", deleted=None, kind="typed",
         updated="2026-09-12T10:00:00Z", subject=None):
    return {"id": id_, "title": title, "card_count": n, "created_by": by,
            "shared_with_school": shared, "status": status, "source_kind": kind,
            "source_file_name": None, "subject": subject, "updated_at": updated,
            "deleted_at": deleted}


def card(id_, deck_id, pos, q, a, conf=None, flagged=False, ref=None):
    return {"id": id_, "deck_id": deck_id, "position": pos, "question": q, "answer": a,
            "source_ref": ref, "confidence": conf, "flagged": flagged}


def cid(n):
    return "cccccccc-0000-4000-8000-%012d" % n


TABLES = {
    "profiles": [
        {"id": T, "first_name": "Ada", "last_name": "Nwosu", "display_name": "Ms Nwosu",
         "role": "teacher", "school_id": "s1"},
        {"id": COL, "first_name": "Ben", "last_name": "Okoro", "display_name": "Mr Okoro",
         "role": "teacher", "school_id": "s1"},
    ],
    "staff_scopes": [],
    "flashcard_decks": [
        deck(D1, "Cell biology", 3, T, updated="2026-09-20T09:00:00Z", subject="biology"),
        deck(D2, "Making CO2", 2, T, shared=True),
        deck(D3, "Old ecology", 4, T, deleted="2026-09-18T09:00:00Z"),
        deck(D4, "Scratch deck", 1, T, deleted="2026-09-18T09:00:00Z"),
        deck(D5, "Bonding", 2, COL, shared=True),
        deck(D6, "Colleague draft", 0, COL, shared=True, status="draft"),
        deck(DN, "cells", 5, T, status="draft", kind="upload",
             updated="2026-09-24T09:00:00Z"),
    ],
    "flashcard_cards": [
        card(cid(1), D1, 0, "What is a cell?", "The unit of life"),
        card(cid(2), D1, 1, "Nucleus holds?", "DNA"),
        card(cid(3), D1, 2, "Mitochondria do?", "Respiration"),
        card(cid(11), D5, 0, "Ionic bond?", "Transfer of electrons"),
        card(cid(12), D5, 1, "Covalent bond?", "Shared pair of electrons"),
        card(cid(21), DN, 0, "Q-one", "A-one", conf=0.95, ref="Slide 1"),
        card(cid(22), DN, 1, "Q-two", "A-two", conf=0.9, ref="Slide 2"),
        card(cid(23), DN, 2, "Q-flag", "A-flag", conf=0.9, flagged=True, ref="Slide 3"),
        card(cid(24), DN, 3, "Q-empty", "", conf=0.9, ref="Slide 4"),
        card(cid(25), DN, 4, "Formula of water is H2O?", "A-low", conf=0.4, ref="Slide 5"),
    ],
    "assignments": [
        {"id": "u1", "deck_id": D1, "deleted_at": None},
        {"id": "u2", "deck_id": D3, "deleted_at": None},
        {"id": "u3", "deck_id": D3, "deleted_at": None},
        {"id": A1, "deck_id": D1, "deleted_at": None, "title": "Cells homework",
         "due_at": "2026-10-01T17:00:00Z", "release_at": "2026-09-20T06:00:00Z",
         "teacher_note": "Old note", "flashcard_mode": "review",
         "completion_rule": "quick", "class_id": C1},
    ],
    "flashcard_extractions": [],
}

CLASSES = [{"id": C1, "code": "10a/Bi1", "n": 28},
           {"id": C2, "code": "10b/Bi2", "n": 27},
           {"id": C3, "code": "8r/Sc1", "n": 30}]

SCOPE = {
    "class": {"key_stage": "KS4", "default_tier": "higher"},
    "tiers": ["foundation", "higher"],
    "subjects": ["biology"],
    "papers": None,
    "cohort_classes": [{"id": C1, "name": "10a/Bi1", "pupils": 28},
                       {"id": C2, "name": "10b/Bi2", "pupils": 27}],
    "tree": [{"id": "cell-biology", "name": "Cell biology", "subject": "biology",
              "counts": {"foundation": 30, "higher": 40}, "last_set_at": None,
              "children": [{"id": "cell-structure", "name": "Cell structure",
                            "counts": {"foundation": 10, "higher": 12}}]}],
    "max_per_scope": 500,
    "assignment_note": True,
}
PREVIEW = {"available": 40, "picked": [
    {"id": "q%d" % i, "stem": "Question %d about CO2" % i,
     "options": ["A", "B", "C", "D"], "correct_index": 0} for i in range(1, 11)]}

STUB_JS = r"""
(function () {
  var F = window.__FD__;
  F.calls = []; F.fetches = []; F.done = [];
  var seq = 0;
  function newId() {
    seq += 1;
    var h = ("000000000000" + seq.toString(16)).slice(-12);
    return "eeeeeeee-0000-4000-8000-" + h;
  }
  function rows(t) { return F.tables[t] || (F.tables[t] = []); }
  function match(r, f) {
    var v = r[f.col];
    if (f.op === 'eq') { return v === f.val; }
    if (f.op === 'is') { return f.val === null ? (v === null || v === undefined) : v === f.val; }
    if (f.op === 'in') { return f.val.indexOf(v) !== -1; }
    return true;
  }
  function Q(table) {
    var fs = [], one = false, upd = null, head = false, countMode = false, ord = null;
    var api = {
      select: function (c, o) { if (o && o.head) { head = true; } if (o && o.count) { countMode = true; } return api; },
      order: function (c, o) { ord = {col: c, asc: !(o && o.ascending === false)}; return api; },
      limit: function () { return api; },
      eq: function (c, v) { fs.push({op:'eq', col:c, val:v}); return api; },
      is: function (c, v) { fs.push({op:'is', col:c, val:v}); return api; },
      in: function (c, v) { fs.push({op:'in', col:c, val:v}); return api; },
      update: function (v) { upd = v; return api; },
      single: function () { one = true; return api; },
      maybeSingle: function () { one = true; return api; },
      then: function (res, rej) {
        var out = rows(table).filter(function (r) {
          for (var i = 0; i < fs.length; i++) { if (!match(r, fs[i])) { return false; } }
          return true;
        });
        if (table === 'flashcard_extractions' && fs.length) {
          var job = F.jobs[fs[0].val] || [];
          var step = job.length > 1 ? job.shift() : job[0];
          F.calls.push({kind: 'poll', job: fs[0].val});
          return Promise.resolve({data: step || null, error: null}).then(res, rej);
        }
        if (upd) {
          out.forEach(function (r) { for (var k in upd) { r[k] = upd[k]; } });
          F.calls.push({kind: 'update', table: table, values: upd, filters: fs});
          return Promise.resolve({data: null, error: null}).then(res, rej);
        }
        if (ord) {
          out.sort(function (a, b) {
            var x = a[ord.col], y = b[ord.col];
            return (x < y ? -1 : x > y ? 1 : 0) * (ord.asc ? 1 : -1);
          });
        }
        var payload;
        if (head) { payload = {data: null, count: out.length, error: null}; }
        else if (one) { payload = {data: out[0] ? JSON.parse(JSON.stringify(out[0])) : null, error: null}; }
        else { payload = {data: JSON.parse(JSON.stringify(out)), error: null}; }
        return Promise.resolve(payload).then(res, rej);
      }
    };
    return api;
  }
  function rpc(name, args) {
    F.calls.push({kind: 'rpc', name: name, args: JSON.parse(JSON.stringify(args))});
    var fail = F.failNext && F.failNext[name];
    if (fail) { delete F.failNext[name]; return Promise.resolve({data: null, error: {message: fail}}); }
    if (name === 'flashcard_deck_save') {
      var id = args.p_deck || newId();
      var d = rows('flashcard_decks').filter(function (x) { return x.id === id; })[0];
      if (!d) {
        d = {id: id, created_by: F.uid, shared_with_school: true, source_kind: (args.p_meta || {}).source_kind || 'typed',
             updated_at: new Date().toISOString(), deleted_at: null};
        rows('flashcard_decks').push(d);
      }
      d.title = args.p_title; d.card_count = args.p_cards.length;
      d.status = args.p_finalise ? 'ready' : 'draft';
      F.tables.flashcard_cards = rows('flashcard_cards').filter(function (c) { return c.deck_id !== id; });
      args.p_cards.forEach(function (c, i) {
        rows('flashcard_cards').push({id: c.id || newId(), deck_id: id, position: i, question: c.question,
          answer: c.answer, source_ref: c.source_ref || null, confidence: c.confidence == null ? null : c.confidence,
          flagged: !!c.flagged});
      });
      return Promise.resolve({data: {deck_id: id, card_count: args.p_cards.length, status: d.status}, error: null});
    }
    if (name === 'flashcard_deck_duplicate') {
      var src = rows('flashcard_decks').filter(function (x) { return x.id === args.p_deck; })[0];
      var nid = newId();
      rows('flashcard_decks').push({id: nid, title: src.title + ' (copy)', card_count: src.card_count,
        created_by: F.uid, shared_with_school: true, status: src.status, source_kind: src.source_kind,
        source_file_name: null, subject: src.subject, updated_at: new Date().toISOString(), deleted_at: null});
      rows('flashcard_cards').filter(function (c) { return c.deck_id === src.id; }).forEach(function (c) {
        rows('flashcard_cards').push({id: newId(), deck_id: nid, position: c.position, question: c.question,
          answer: c.answer, source_ref: c.source_ref, confidence: c.confidence, flagged: c.flagged});
      });
      return Promise.resolve({data: nid, error: null});
    }
    if (name === 'flashcard_set_work') {
      return Promise.resolve({data: {success: true, assignment_ids: args.p_class_ids.map(function () { return newId(); }),
        release_at: args.p_release_at || new Date().toISOString(), cards: 4}, error: null});
    }
    if (name === 'flashcard_edit_assignment') {
      return Promise.resolve({data: {ok: true}, error: null});
    }
    return Promise.resolve({data: null, error: null});
  }
  var user = {id: F.uid, aud: 'authenticated', role: 'authenticated', email: 'stub@drive.invalid',
              app_metadata: {}, user_metadata: {}};
  var client = {
    from: Q, rpc: rpc,
    auth: {
      getUser: function () { return Promise.resolve({data: {user: user}, error: null}); },
      getSession: function () { return Promise.resolve({data: {session: {user: user, access_token: 'stub'}}, error: null}); },
      signOut: function () { return Promise.resolve({error: null}); },
      onAuthStateChange: function () { return {data: {subscription: {unsubscribe: function () {}}}}; }
    }
  };
  var sdk = {createClient: function () { return client; }};
  Object.defineProperty(window, 'supabase', {
    configurable: true, get: function () { return sdk; }, set: function () {}
  });

  /* The two network seams that are not supabase-js: the extraction edge
     function and the Set work backend. Everything else is the real server. */
  var realFetch = window.fetch.bind(window);
  function reply(status, body) {
    return Promise.resolve(new Response(JSON.stringify(body), {status: status,
      headers: {'Content-Type': 'application/json'}}));
  }
  window.fetch = function (url, init) {
    var u = String(url && url.url ? url.url : url);
    if (u.indexOf('/functions/v1/flashcard-extract') > -1) {
      var rec = {url: u, headers: (init && init.headers) || {}};
      var b = init && init.body;
      if (b instanceof FormData) {
        rec.form = {};
        b.forEach(function (v, k) { rec.form[k] = (v && v.name !== undefined) ? ('file:' + v.name) : String(v); });
      } else { try { rec.json = JSON.parse(b); } catch (e) { rec.json = null; } }
      F.fetches.push(rec);
      var r = F.extractQueue.shift() || {status: 500, body: {error: 'none'}};
      return reply(r.status, r.body);
    }
    if (u.indexOf('/api/teacher/set-work/scope') > -1) { F.fetches.push({url: u}); return reply(200, F.scope); }
    if (u.indexOf('/api/teacher/set-work/preview') > -1) { F.fetches.push({url: u}); return reply(200, F.preview); }
    return realFetch(url, init);
  };
  window.MRB_SET_WORK_DONE = function (d) { F.done.push(d); };
  window.__MRB_DATA__ = {SET_WORK_CLASSES: F.classes};
})();
"""

INJECT_SHEET = r"""
new Promise(function (resolve) {
  var l = document.createElement('link'); l.rel = 'stylesheet'; l.href = '/shared/set-work.css';
  document.head.appendChild(l);
  var s = document.createElement('script'); s.src = '/shared/set-work.js';
  s.onload = function () { resolve(!!window.MRBSetWork); };
  s.onerror = function () { resolve(false); };
  document.head.appendChild(s);
})
"""

# Visible text nodes in the overlay(s) and the page body, as one list.
TEXTS_JS = r"""
(function () {
  var out = [];
  var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  var n;
  while ((n = w.nextNode())) {
    var t = (n.nodeValue || '').replace(/\s+/g, ' ').trim();
    if (!t) { continue; }
    var p = n.parentElement;
    if (!p || p.closest('script,style,noscript')) { continue; }
    var r = p.getBoundingClientRect();
    var cs = getComputedStyle(p);
    if (!r.width || !r.height || cs.visibility === 'hidden') { continue; }
    out.push(t);
  }
  return out;
})()
"""

OVERFLOW_JS = r"""
(function () {
  var d = document.documentElement;
  var bad = [];
  if (d.scrollWidth > d.clientWidth + 1) { bad.push('document ' + d.scrollWidth + '>' + d.clientWidth); }
  document.querySelectorAll('.sw-sheet').forEach(function (s) {
    if (s.offsetParent === null && getComputedStyle(s).position !== 'fixed') {}
    var o = s.closest('.sw-overlay');
    if (o && o.hidden) { return; }
    if (s.scrollWidth > s.clientWidth + 1) { bad.push('sheet ' + s.scrollWidth + '>' + s.clientWidth); }
  });
  return bad;
})()
"""

FORBIDDEN = ["you ", "your ", "will ", "click", "tap here", "how this works",
             "this deck", "upload a", "pupils will", "students will", "drag ",
             "choose a", "select a", "to get started"]


def main():
    shots = os.path.join(cdp.gate_tmp(), "mrb351-decks")
    os.makedirs(shots, exist_ok=True)
    fails = []

    def check(ok, what, detail=""):
        print("   %s  %s%s" % ("PASS" if ok else "FAIL", what,
                               ("  - " + str(detail)) if detail and not ok else ""))
        if not ok:
            fails.append(what)

    root = os.path.dirname(os.path.abspath(__file__))
    server, port = cdp.serve(root)
    base = "http://127.0.0.1:%d" % port

    def fresh(b, jobs=None, queue=None, fail_next=None):
        state = {"uid": T, "tables": json.loads(json.dumps(TABLES)), "classes": CLASSES,
                 "scope": SCOPE, "preview": PREVIEW, "jobs": jobs or {},
                 "extractQueue": queue or [], "failNext": fail_next or {}}
        pre = "window.__FD__=%s;\n" % json.dumps(state) + STUB_JS
        p = b.page("about:blank", settle=0.1)
        p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pre})
        return p

    def wait(p, expr, timeout=8.0, step=0.1):
        end = time.time() + timeout
        while time.time() < end:
            try:
                v = p.eval(expr)
            except cdp.JSError:
                v = None
            if v:
                return v
            time.sleep(step)
        return None

    def click(p, sel):
        return p.eval("(function(){var n=document.querySelector(%s);"
                      "if(!n)return false;n.click();return true;})()" % json.dumps(sel))

    def errors(p):
        return [e for e in p.console_errors()
                if "favicon" not in e and "jsdelivr" not in e
                and "ERR_NAME_NOT_RESOLVED" not in e and "ERR_INTERNET_DISCONNECTED" not in e
                and "ERR_TUNNEL" not in e and "ERR_PROXY" not in e
                and "Failed to load resource" not in e
                and "config: TEST" not in e]

    def sentences(p, where):
        texts = p.eval(TEXTS_JS) or []
        bad = []
        for t in texts:
            low = " " + t.lower() + " "
            words = len(t.split())
            if any(f in low for f in FORBIDDEN):
                bad.append(t)
            elif words >= 5 and (t.endswith(".") or ". " in t):
                bad.append(t)
        check(not bad, "%s: no explanatory sentences on screen" % where, bad[:5])

    def overflow(p, where, widths=(360, 390)):
        for w in widths:
            p.set_viewport(w, 844, settle=0.3)
            bad = p.eval(OVERFLOW_JS)
            check(not bad, "%s: no horizontal scroll at %dpx" % (where, w), bad)

    def calls(p, name=None, kind="rpc"):
        cs = p.eval("window.__FD__.calls") or []
        return [c for c in cs if c.get("kind") == kind and (name is None or c.get("name") == name)]

    try:
        with cdp.Browser() as b:
            # ═══ 1. THE SHEET — Questions still works ═════════════════════
            print("\n── sheet: Questions branch ──")
            p = fresh(b)
            p.goto(base + "/teacher/decks.html", settle=1.5)
            check(bool(p.eval(INJECT_SHEET)), "sheet: set-work.js loads on the page")
            p.set_viewport(390, 844)
            p.eval("MRBSetWork.open({})")
            check(p.eval("document.querySelector('[data-sw=type-chips] .is-on').textContent")
                  == "Questions", "sheet: type chips at the top, Questions by default")
            first = p.eval("(function(){var pc=document.querySelector('[data-sw=panel-classes]');"
                           "return pc.firstElementChild.getAttribute('data-sw');})()")
            check(first == "type-label", "sheet: the type rail is the first thing on Classes", first)
            click(p, "[data-sw=class][data-sw-ref='%s']" % C1)
            wait(p, "document.querySelector('[data-sw=overlay]').getAttribute('data-sw-scope-state')==='ready'")
            check(p.eval("document.querySelector(\"[data-sw=class][data-sw-ref='%s']\")"
                         ".getAttribute('aria-disabled')" % C3) == "true",
                  "sheet (Questions): a class outside the cohort is not pickable")
            click(p, "[data-sw=primary]")
            check(p.eval("document.querySelector('[data-sw=step]').textContent") == "Topic",
                  "sheet (Questions): Next reaches the Topic step")
            check(bool(p.eval("!!document.querySelector('[data-sw=topic]')")),
                  "sheet (Questions): the tree is drawn")
            click(p, "[data-sw=topic]")
            click(p, "[data-sw=primary]")
            wait(p, "document.querySelectorAll('[data-sw=question]').length>0")
            check(p.eval("document.querySelector('[data-sw=step]').textContent") == "Detail"
                  and p.eval("document.querySelectorAll('[data-sw=question]').length") == 10,
                  "sheet (Questions): Detail step with ten questions")
            check(p.eval("document.querySelector('[data-sw=fc-top]').hidden") is True
                  and p.eval("document.querySelector('[data-sw=fc-summary]').hidden") is True,
                  "sheet (Questions): no flashcard controls on a question set")
            check(p.eval("!document.querySelector('[data-sw=download]').closest('.sw-dl').hidden"),
                  "sheet (Questions): Download still offered")
            p.eval("MRBSetWork.close()")

            # ═══ 2. FLASHCARDS — upload → review → save → set ════════════
            print("\n── sheet: Flashcards via Upload ──")
            jobs = {J1: [{"status": "reading", "progress": 10},
                         {"status": "asking", "progress": 35},
                         {"status": "asking", "progress": 35},
                         {"status": "done", "progress": 100, "pairs_found": 5,
                          "needs_answer": 1, "method": "model"}]}
            queue = [{"status": 202, "body": {"deck_id": DN, "job_id": J1}}]
            p = fresh(b, jobs=jobs, queue=queue,
                      fail_next={"flashcard_set_work": "due_before_release"})
            p.goto(base + "/teacher/decks.html", settle=1.5)
            p.eval(INJECT_SHEET)
            p.set_viewport(390, 844)
            p.eval("MRBSetWork.open({})")
            click(p, "[data-sw=type-chips] [data-sw-key=flashcards]")
            check(p.eval("document.querySelector('[data-sw=overlay]').getAttribute('data-sw-type')")
                  == "flashcards", "flash: the type chip switches the branch")
            click(p, "[data-sw=class][data-sw-ref='%s']" % C1)
            click(p, "[data-sw=class][data-sw-ref='%s']" % C3)
            check(p.eval("document.querySelector(\"[data-sw=class][data-sw-ref='%s']\")"
                         ".getAttribute('aria-pressed')" % C3) == "true",
                  "flash: any class the teacher teaches may be picked (no cohort)")
            check(not any("/scope" in (f.get("url") or "") for f in (p.eval("window.__FD__.fetches") or [])),
                  "flash: /scope is never asked for")
            click(p, "[data-sw=primary]")
            check(p.eval("document.querySelector('[data-sw=step]').textContent") == "Deck",
                  "flash: step 2 is named Deck")
            wait(p, "!!document.querySelector('[data-fd=source-chips]')")
            labels = p.eval("Array.from(document.querySelectorAll('[data-fd=source-chips] .sw-chip'))"
                            ".map(function(b){return b.textContent;})")
            check(labels == ["Upload", "Paste", "Type", "My decks", "Shared"],
                  "flash: source chips Upload · Paste · Type · My decks · Shared", labels)
            check(p.eval("document.querySelector('[data-fd=file]').accept")
                  == ".pptx,.docx,.pdf,.xlsx,.csv,.txt,.md,.png,.jpg,.jpeg,.heic",
                  "flash: the file input accepts the ruled types")
            check(p.eval("document.querySelector('[data-sw=primary]').disabled") is True,
                  "flash: Next is off until a deck is ready")
            p.eval("(function(){var i=document.querySelector('[data-fd=file]');"
                   "var dt=new DataTransfer();dt.items.add(new File(['x'],'cells.pptx'));"
                   "i.files=dt.files;i.dispatchEvent(new Event('change'));})()")
            seen35 = wait(p, "(function(){var l=document.querySelector('[data-fd=progress-label]');"
                             "return l&&l.textContent==='Reading\\u2026 35%';})()", timeout=6)
            check(bool(seen35), "flash: the progress label reads 'Reading… 35%'")
            p.screenshot(os.path.join(shots, "sheet-progress-390.png"), width=390, height=844,
                         full_page=False)
            f0 = (p.eval("window.__FD__.fetches") or [])[0]
            check(f0 and f0.get("form", {}).get("file") == "file:cells.pptx"
                  and f0.get("form", {}).get("title") == "cells"
                  and f0["headers"].get("Authorization") == "Bearer stub"
                  and bool(f0["headers"].get("apikey")),
                  "flash: upload is multipart file+title with the bearer and apikey", f0)
            wait(p, "!!document.querySelector('[data-fd=editor]')", timeout=8)
            order = p.eval("Array.from(document.querySelectorAll('[data-fd=card] [data-fd=q]'))"
                           ".map(function(t){return t.value;})")
            check(order[:3] == ["Q-flag", "Q-empty", "Formula of water is H2O?"],
                  "flash: flagged, empty-sided and low-confidence rows sorted to the top", order)
            check(p.eval("Array.from(document.querySelectorAll('[data-fd=card]')).slice(0,3)"
                         ".every(function(r){return r.classList.contains('is-flag');})"),
                  "flash: those rows are marked")
            check(p.eval("document.querySelector('[data-fd=count]').textContent")
                  == "5 cards · 1 needs an answer",
                  "flash: live count '5 cards · 1 needs an answer'",
                  p.eval("document.querySelector('[data-fd=count]').textContent"))
            check(p.eval("document.querySelector('[data-fd=save]').disabled") is True,
                  "flash: Save deck disabled with an empty answer")
            sub = p.eval("(function(){var r=document.querySelectorAll('[data-fd=card]')[2];"
                         "var q=r.querySelector('[data-fd=q-render]');"
                         "return !q.hidden && !!q.querySelector('sub') && q.textContent;})()")
            check(sub == "Formula of water is H2O?", "flash: a formula is drawn with <sub> read-only",
                  sub)
            check(p.eval("document.querySelectorAll('[data-fd=card] [data-fd=q]')[2].value")
                  == "Formula of water is H2O?", "flash: the editing field stays flat text")
            p.eval("(function(){var a=document.querySelectorAll('[data-fd=card] [data-fd=a]')[1];"
                   "a.value='A-filled';a.dispatchEvent(new Event('input'));})()")
            check(p.eval("document.querySelector('[data-fd=save]').disabled") is False
                  and p.eval("document.querySelector('[data-fd=count]').textContent") == "5 cards",
                  "flash: Save enabled once every side is filled; the count drops its tail")
            # swap one row
            p.eval("document.querySelectorAll('[data-fd=card] [data-fd=swap]')[3].click()")
            sw = p.eval("(function(){var r=document.querySelectorAll('[data-fd=card]')[3];"
                        "return [r.querySelector('[data-fd=q]').value,r.querySelector('[data-fd=a]').value];})()")
            check(sw == ["A-one", "Q-one"], "flash: Swap exchanges one row's question and answer", sw)
            # swap all twice = identity for that row, but proves the control
            p.eval("document.querySelector('[data-fd=swap-all]').click()")
            sa = p.eval("document.querySelectorAll('[data-fd=card] [data-fd=q]')[4].value")
            check(sa == "A-two", "flash: Swap all exchanges every row", sa)
            p.eval("document.querySelector('[data-fd=swap-all]').click()")
            # add a row → Save off → delete it
            p.eval("document.querySelector('[data-fd=add]').click()")
            check(p.eval("document.querySelectorAll('[data-fd=card]').length") == 6
                  and p.eval("document.querySelector('[data-fd=save]').disabled") is True
                  and "need an answer" in p.eval("document.querySelector('[data-fd=count]').textContent")
                  and "need a question" in p.eval("document.querySelector('[data-fd=count]').textContent")
                  or p.eval("document.querySelector('[data-fd=count]').textContent")
                  == "6 cards · 1 needs an answer · 1 needs a question",
                  "flash: Add card appends a blank row and Save goes off",
                  p.eval("document.querySelector('[data-fd=count]').textContent"))
            p.eval("(function(){var d=document.querySelectorAll('[data-fd=card] [data-fd=delete]');"
                   "d[d.length-1].click();})()")
            check(p.eval("document.querySelectorAll('[data-fd=card]').length") == 5
                  and p.eval("document.querySelector('[data-fd=save]').disabled") is False,
                  "flash: a row's Delete removes it")
            # delete the low-confidence row too → 4 cards
            p.eval("document.querySelectorAll('[data-fd=card] [data-fd=delete]')[2].click()")
            # up / down
            p.eval("document.querySelectorAll('[data-fd=card] [data-fd=down]')[0].click()")
            ud = p.eval("Array.from(document.querySelectorAll('[data-fd=card] [data-fd=q]')).map(function(t){return t.value;})")
            check(ud[:2] == ["Q-empty", "Q-flag"], "flash: Down moves a row one place", ud)
            check(p.eval("document.querySelectorAll('[data-fd=card] [data-fd=up]')[0].disabled") is True,
                  "flash: Up is off on the first row")
            p.eval("document.querySelectorAll('[data-fd=card] [data-fd=up]')[1].click()")
            # drag row 0 below row 1 with a real pointer, at desktop width
            p.set_viewport(1280, 800, settle=0.3)
            p.eval("(function(){var r=document.querySelectorAll('[data-fd=card]')[0];"
                   "var sh=r.closest('.sw-sheet');r.scrollIntoView({block:'start'});"
                   "sh.scrollTop=Math.max(0,sh.scrollTop-90);})()")
            time.sleep(0.2)
            g = p.eval("(function(){var h=document.querySelectorAll('[data-fd=card] [data-fd=handle]')[0]"
                       ".getBoundingClientRect();var r=document.querySelectorAll('[data-fd=card]')[1]"
                       ".getBoundingClientRect();return [h.x+h.width/2,h.y+h.height/2,r.y+r.height*0.8];})()")
            p.send("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": g[0], "y": g[1]})
            p.send("Input.dispatchMouseEvent", {"type": "mousePressed", "x": g[0], "y": g[1],
                                                "button": "left", "clickCount": 1})
            for k in range(1, 9):
                p.send("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": g[0],
                                                    "y": g[1] + (g[2] - g[1]) * k / 8,
                                                    "button": "left", "buttons": 1})
            p.send("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": g[0], "y": g[2],
                                                "button": "left", "clickCount": 1})
            time.sleep(0.2)
            dr = p.eval("Array.from(document.querySelectorAll('[data-fd=card] [data-fd=q]')).map(function(t){return t.value;})")
            check(dr[:2] == ["Q-empty", "Q-flag"], "flash: dragging the handle reorders rows", dr)
            p.set_viewport(390, 844, settle=0.3)
            p.eval("(function(){var t=document.querySelector('[data-fd=title]');t.value='Cells deck';"
                   "t.dispatchEvent(new Event('input'));})()")
            p.eval("document.querySelector('[data-fd=subject] [data-fd-key=biology]').click()")
            p.screenshot(os.path.join(shots, "sheet-review-390.png"), width=390, height=844,
                         full_page=False)
            overflow(p, "flash review table")
            sentences(p, "flash review table")
            p.set_viewport(1280, 800, settle=0.2)
            p.screenshot(os.path.join(shots, "sheet-review-1280.png"), width=1280, height=800,
                         full_page=False)
            p.set_viewport(390, 844, settle=0.2)
            click(p, "[data-fd=save]")
            wait(p, "document.querySelector('[data-sw=step]').textContent==='Detail'")
            sv = calls(p, "flashcard_deck_save")
            a = sv[-1]["args"] if sv else {}
            check(bool(sv) and a.get("p_deck") == DN and a.get("p_finalise") is True
                  and a.get("p_title") == "Cells deck"
                  and [c["question"] for c in a.get("p_cards", [])] == ["Q-empty", "Q-flag", "A-one", "Q-two"]
                  and a["p_cards"][0].get("answer") == "A-filled"
                  and all(c.get("id") for c in a["p_cards"])
                  and a.get("p_meta", {}).get("subject") == "biology"
                  and a.get("p_meta", {}).get("source_kind") == "upload",
                  "flash: Save posts flashcard_deck_save — order, ids, title, subject, finalise",
                  a)
            check(p.eval("document.querySelector('[data-sw=step]').textContent") == "Detail",
                  "flash: a saved deck moves the sheet to Detail")
            modes = p.eval("Array.from(document.querySelectorAll('[data-sw=fc-mode]')).map(function(b){"
                           "return [b.getAttribute('data-sw-key'),b.classList.contains('is-on'),b.textContent];})")
            check(modes and modes[0][0] == "make" and modes[0][1] and not modes[1][1]
                  and "Pupils write the answers" in modes[0][2] and "Ready-made cards" in modes[1][2],
                  "flash: two mode cards, 'Pupils write the answers' by default", modes)
            check(p.eval("document.querySelector('[data-sw=fc-rule] .is-on').textContent") == "Secure",
                  "flash: rule toggle defaults to Secure")
            check(p.eval("document.querySelector('[data-sw=download]').closest('.sw-dl').hidden") is True
                  and p.eval("document.querySelector('[data-sw=scopes]').offsetParent") is None,
                  "flash: no Download and no question list on a flashcard set")
            check(p.eval("!document.querySelector('[data-sw=assignment-note-field]').hidden"),
                  "flash: the note field is offered")
            summ = p.eval("document.querySelector('[data-sw=fc-summary]').innerText")
            check("Cells deck" in summ and "4 cards" in summ and "Pupils write the answers" in summ
                  and "Secure" in summ and "10a/Bi1" in summ and "8r/Sc1" in summ and "Due " in summ,
                  "flash: the summary card names deck · cards · mode · rule · classes · due", summ)
            check(p.eval("document.querySelector('[data-sw=title]').value") == "Cells deck",
                  "flash: the title defaults to the deck's")
            p.eval("(function(){var n=document.querySelector('[data-sw=assignment-note]');"
                   "n.value='Do ten a night';n.dispatchEvent(new Event('input'));})()")
            p.screenshot(os.path.join(shots, "sheet-detail-390.png"), width=390, height=844,
                         full_page=False)
            overflow(p, "flash detail")
            sentences(p, "flash detail")
            p.set_viewport(1280, 800, settle=0.2)
            p.screenshot(os.path.join(shots, "sheet-detail-1280.png"), width=1280, height=800,
                         full_page=False)
            p.set_viewport(390, 844, settle=0.2)
            click(p, "[data-sw=primary]")
            wait(p, "window.__FD__.calls.filter(function(c){return c.name==='flashcard_set_work';}).length>=1")
            time.sleep(0.2)
            check(p.eval("document.querySelector('[data-sw=due-date]').classList.contains('sw-bad')"),
                  "flash: a due_before_release refusal outlines the due fields")
            check(p.eval("!document.querySelector('[data-sw=overlay]').hidden"),
                  "flash: a refused set leaves the sheet open")
            # fix nothing, simply retry: the stub only refuses once
            p.eval("(function(){var d=document.querySelector('[data-sw=due-date]');"
                   "d.dispatchEvent(new Event('input'));})()")
            click(p, "[data-sw=primary]")
            wait(p, "document.querySelector('[data-sw=overlay]').hidden")
            sets = calls(p, "flashcard_set_work")
            want_due = p.eval("(function(){return MRBSetWork.londonToUtcIso("
                              "document.querySelector('[data-sw=due-date]').value,"
                              "document.querySelector('[data-sw=due-time]').value);})()")
            s2 = sets[-1]["args"] if sets else {}
            check(len(sets) == 2 and s2.get("p_class_ids") == [C1, C3] and s2.get("p_deck") == DN
                  and s2.get("p_mode") == "make" and s2.get("p_rule") == "secure"
                  and s2.get("p_release_at") is None and s2.get("p_due_at") == want_due
                  and s2.get("p_note") == "Do ten a night" and s2.get("p_title") == "Cells deck"
                  and bool(s2.get("p_client_ref")),
                  "flash: Set work posts the exact flashcard_set_work payload", s2)
            check(len(sets) == 2 and sets[0]["args"].get("p_client_ref") == s2.get("p_client_ref"),
                  "flash: the retry after a refusal reuses the client_ref")
            done = p.eval("window.__FD__.done") or []
            check(len(done) == 1 and done[0].get("kind") == "flashcards"
                  and len(done[0].get("assignmentIds") or []) == 2,
                  "flash: the page's MRB_SET_WORK_DONE hook fires once", done)
            errs = errors(p)
            check(not errs, "flash: no console errors", errs)

            # ═══ 3. cached · paste · type · My decks pick ══════════════════
            print("\n── sheet: cached, paste, type, pick ──")
            queue = [{"status": 200, "body": {"cached": {"deck_id": D1, "title": "Cell biology",
                                                         "card_count": 3, "mine": True}}},
                     {"status": 202, "body": {"deck_id": DN, "job_id": J1}},
                     {"status": 202, "body": {"deck_id": DN, "job_id": J1}}]
            jobs = {J1: [{"status": "asking", "progress": 35}]}
            p = fresh(b, jobs=jobs, queue=queue)
            p.goto(base + "/teacher/decks.html", settle=1.5)
            p.eval(INJECT_SHEET)
            p.set_viewport(390, 844)
            p.eval("MRBSetWork.open({classId: %s})" % json.dumps(C2))
            click(p, "[data-sw=type-chips] [data-sw-key=flashcards]")
            click(p, "[data-sw=primary]")
            wait(p, "!!document.querySelector('[data-fd=file]')")
            p.eval("(function(){var i=document.querySelector('[data-fd=file]');"
                   "var dt=new DataTransfer();dt.items.add(new File(['x'],'cells.pdf'));"
                   "i.files=dt.files;i.dispatchEvent(new Event('change'));})()")
            wait(p, "!document.querySelector('[data-fd=pane-cached]').hidden")
            bt = p.eval("[document.querySelector('[data-fd=use-before]').textContent,"
                        "document.querySelector('[data-fd=read-again]').textContent]")
            check(bt == ["Use the cards extracted before", "Read it again"],
                  "cached: the two buttons are offered", bt)
            click(p, "[data-fd=read-again]")
            EXT = ("window.__FD__.fetches.filter(function(f){"
                   "return f.url.indexOf('flashcard-extract')>-1;})")
            wait(p, EXT + ".length>=2")
            f1 = (p.eval(EXT) or [{}, {}])[1]
            check(f1.get("form", {}).get("force") == "1"
                  and f1.get("form", {}).get("file") == "file:cells.pdf",
                  "cached: 'Read it again' resends the file with force=1", f1)
            click(p, "[data-fd=source-chips] [data-fd-key=paste]")
            check(p.eval("document.querySelector('[data-fd=make]').disabled") is True,
                  "paste: Make cards is off on an empty box")
            p.eval("(function(){var t=document.querySelector('[data-fd=paste]');"
                   "t.value='Photosynthesis\\tMakes glucose\\nRespiration\\tReleases energy';"
                   "t.dispatchEvent(new Event('input'));})()")
            click(p, "[data-fd=make]")
            wait(p, EXT + ".length>=3")
            f2 = (p.eval(EXT) or [{}, {}, {}])[2]
            check((f2.get("json") or {}).get("paste", "").startswith("Photosynthesis")
                  and (f2.get("json") or {}).get("title") == "Photosynthesis\tMakes glucose",
                  "paste: Make cards posts {paste, title}", f2)
            click(p, "[data-fd=source-chips] [data-fd-key=type]")
            check(p.eval("document.querySelectorAll('[data-fd=card]').length") == 3
                  and p.eval("document.querySelector('[data-fd=save]').disabled") is True
                  and p.eval("document.querySelector('[data-fd=rerun]').hidden") is True,
                  "type: the review table opens with three blank rows, Save off, no re-run")
            sentences(p, "type table")
            click(p, "[data-fd=source-chips] [data-fd-key=mine]")
            wait(p, "document.querySelectorAll('[data-fd=deck]').length>0")
            mine = p.eval("Array.from(document.querySelectorAll('[data-fd=deck] .sw-row-name')).map(function(n){return n.textContent;})")
            check("Cell biology" in mine and "Old ecology" not in mine and "Bonding" not in mine,
                  "My decks: own live decks only", mine)
            check(p.eval("!!document.querySelector('[data-fd=deck-edit]')"),
                  "My decks: own decks show Edit")
            metas = p.eval("Array.from(document.querySelectorAll('[data-fd=deck] .sw-row-tag')).map(function(n){return n.textContent;})")
            check(any("3 cards" in m and "Ms Nwosu" in m for m in metas),
                  "My decks: rows carry N cards · author · date", metas)
            p.eval("document.querySelector('[data-fd=search]').value='co2';"
                   "document.querySelector('[data-fd=search]').dispatchEvent(new Event('input'))")
            wait(p, "document.querySelectorAll('[data-fd=deck]').length===1")
            got = p.eval("document.querySelector('[data-fd=deck] .sw-row-name').innerHTML")
            check(got == "Making CO<sub>2</sub>", "My decks: search filters, titles draw formulae", got)
            p.eval("document.querySelector('[data-fd=search]').value='';"
                   "document.querySelector('[data-fd=search]').dispatchEvent(new Event('input'))")
            click(p, "[data-fd=source-chips] [data-fd-key=shared]")
            wait(p, "document.querySelectorAll('[data-fd=deck]').length>0")
            shared = p.eval("Array.from(document.querySelectorAll('[data-fd=deck] .sw-row-name')).map(function(n){return n.textContent;})")
            check(shared == ["Bonding"], "Shared: colleagues' ready shared decks only", shared)
            check(not p.eval("!!document.querySelector('[data-fd=deck-edit]')"),
                  "Shared: a colleague's deck has no Edit")
            click(p, "[data-fd=source-chips] [data-fd-key=mine]")
            wait(p, "document.querySelectorAll('[data-fd=deck]').length>0")
            p.eval("(function(){var r=Array.from(document.querySelectorAll('[data-fd=deck]')).filter("
                   "function(n){return n.getAttribute('data-fd-id')===%s;})[0];r.click();})()" % json.dumps(D1))
            check(p.eval("document.querySelector('[data-sw=primary]').disabled") is False,
                  "pick: a ready deck enables Next")
            click(p, "[data-sw=primary]")
            click(p, "[data-sw=fc-mode][data-sw-key=review]")
            click(p, "[data-sw=fc-rule] [data-sw-key=quick]")
            click(p, "[data-sw=release-chips] [data-sw-key=later]")
            rel = p.eval("(function(){var d=new Date(Date.now()+3*864e5);"
                         "return d.toISOString().slice(0,10);})()")
            p.eval("(function(){var d=document.querySelector('[data-sw=release-date]');d.value=%s;"
                   "d.dispatchEvent(new Event('input'));var t=document.querySelector('[data-sw=release-time]');"
                   "t.value='08:30';t.dispatchEvent(new Event('input'));"
                   "var u=document.querySelector('[data-sw=due-date]');"
                   "u.value=new Date(Date.now()+9*864e5).toISOString().slice(0,10);"
                   "u.dispatchEvent(new Event('input'));})()" % json.dumps(rel))
            summ = p.eval("document.querySelector('[data-sw=fc-summary]').innerText")
            check("Ready-made cards" in summ and "Quick" in summ and "3 cards" in summ
                  and "10b/Bi2" in summ, "pick: the summary follows mode and rule", summ)
            click(p, "[data-sw=primary]")
            wait(p, "document.querySelector('[data-sw=overlay]').hidden")
            s3 = (calls(p, "flashcard_set_work") or [{}])[-1].get("args", {})
            want_rel = p.eval("MRBSetWork.londonToUtcIso(%s,'08:30')" % json.dumps(rel))
            check(s3.get("p_deck") == D1 and s3.get("p_mode") == "review"
                  and s3.get("p_rule") == "quick" and s3.get("p_release_at") == want_rel
                  and s3.get("p_class_ids") == [C2] and s3.get("p_note") is None,
                  "pick: Ready-made + Quick + a later release are what is posted", s3)

            # ═══ 3b. a failed extraction, and a re-run from the table ══════
            print("\n── sheet: failed extraction ──")
            J2 = J1.replace("a0a0", "b0b0")
            jobs = {J2: [{"status": "failed", "progress": 100, "error": "too_many_pages"}],
                    J1: [{"status": "done", "progress": 100}]}
            queue = [{"status": 202, "body": {"deck_id": DN, "job_id": J2}},
                     {"status": 202, "body": {"deck_id": DN, "job_id": J1}},
                     {"status": 202, "body": {"deck_id": DN, "job_id": J1}}]
            p = fresh(b, jobs=jobs, queue=queue)
            p.goto(base + "/teacher/decks.html", settle=1.5)
            p.eval(INJECT_SHEET)
            p.set_viewport(390, 844)
            p.eval("MRBSetWork.open({})")
            click(p, "[data-sw=type-chips] [data-sw-key=flashcards]")
            click(p, "[data-sw=class][data-sw-ref='%s']" % C1)
            click(p, "[data-sw=primary]")
            wait(p, "!!document.querySelector('[data-fd=file]')")
            p.eval("(function(){var i=document.querySelector('[data-fd=file]');"
                   "var dt=new DataTransfer();dt.items.add(new File(['x'],'big.pdf'));"
                   "i.files=dt.files;i.dispatchEvent(new Event('change'));})()")
            wait(p, "!document.querySelector('[data-fd=pane-failed]').hidden", timeout=6)
            check(p.eval("document.querySelector('[data-fd=fail-note]').textContent") == "Over 60 pages"
                  and not p.eval("document.querySelector('[data-fd=fail-rerun]').hidden")
                  and p.eval("document.querySelector('[data-fd=fail-rerun]').textContent") == "Try extraction again"
                  and p.eval("document.querySelector('[data-fd=fail-blank]').textContent") == "Start from blank",
                  "failed: the reason as a label, with 'Try extraction again' and 'Start from blank'")
            sentences(p, "failed extraction")
            click(p, "[data-fd=fail-rerun]")
            wait(p, "!!document.querySelector('[data-fd=editor]')", timeout=6)
            ext = p.eval("window.__FD__.fetches.filter(function(f){return f.url.indexOf('flashcard-extract')>-1;})")
            check(len(ext) == 2 and ext[1].get("json") == {"deck_id": DN, "rerun": True},
                  "failed: 'Try extraction again' posts {deck_id, rerun:true}", ext[-1:])
            check(not p.eval("document.querySelector('[data-fd=rerun]').hidden"),
                  "review table: an upload deck offers 'Try extraction again'")
            click(p, "[data-fd=rerun]")
            wait(p, "window.__FD__.fetches.filter(function(f){return f.url.indexOf('flashcard-extract')>-1;}).length>=3")
            ext = p.eval("window.__FD__.fetches.filter(function(f){return f.url.indexOf('flashcard-extract')>-1;})")
            check(ext[-1].get("json") == {"deck_id": DN, "rerun": True},
                  "review table: its re-run posts {deck_id, rerun:true}", ext[-1:])
            wait(p, "!!document.querySelector('[data-fd=editor]')", timeout=6)
            click(p, "[data-fd=blank]")
            check(p.eval("document.querySelectorAll('[data-fd=card]').length") == 3
                  and all(v == "" for v in p.eval("Array.from(document.querySelectorAll('[data-fd=q]')).map(function(t){return t.value;})")),
                  "review table: 'Start from blank' leaves three empty rows")
            errs = errors(p)
            check(not errs, "failed extraction: no console errors", errs)

            # ═══ 4. EDIT a flashcard row ══════════════════════════════════
            print("\n── sheet: edit a flashcard set ──")
            p.eval("MRBSetWork.edit({kind:'flashcards', assignmentId:%s, classId:%s,"
                   "title:'Cells homework', dueAt:'2026-10-01T17:00:00Z',"
                   "releaseAt:'2026-09-20T06:00:00Z', released:true})" % (json.dumps(A1), json.dumps(C1)))
            wait(p, "document.querySelector('[data-sw=assignment-note]').value==='Old note'")
            check(p.eval("document.querySelector('[data-sw=step]').textContent") == "Detail"
                  and p.eval("document.querySelector('[data-sw=back]').textContent") == "Cancel"
                  and p.eval("document.querySelector('[data-sw=primary]').textContent") == "Save",
                  "edit: opens on Detail with Cancel and Save")
            check(p.eval("document.querySelector('[data-sw=fc-top]').hidden") is True
                  and p.eval("document.querySelector('[data-sw=release-chips]').hidden") is True,
                  "edit: a released set offers no mode, rule or release")
            wait(p, "document.querySelector('[data-sw=fc-summary]').innerText.indexOf('Cell biology')>-1")
            summ = p.eval("document.querySelector('[data-sw=fc-summary]').innerText")
            check("Cell biology" in summ and "Ready-made cards" in summ and "Quick" in summ,
                  "edit: the summary carries the stored deck, mode and rule", summ)
            p.eval("(function(){var t=document.querySelector('[data-sw=title]');t.value='Cells HW';"
                   "t.dispatchEvent(new Event('input'));})()")
            click(p, "[data-sw=primary]")
            wait(p, "document.querySelector('[data-sw=overlay]').hidden")
            e = (calls(p, "flashcard_edit_assignment") or [{}])[-1].get("args", {})
            check(e.get("p_id") == A1 and e.get("p_title") == "Cells HW"
                  and e.get("p_due_at") == "2026-10-01T17:00:00.000Z"
                  and e.get("p_note") == "Old note" and e.get("p_release_at") is None,
                  "edit: saves through flashcard_edit_assignment, keeping the stored note", e)
            p.eval("MRBSetWork.edit({kind:'flashcards', assignmentId:%s, classId:%s,"
                   "title:'X', dueAt:'2026-10-01T17:00:00Z', releaseAt:'2026-09-20T06:00:00Z',"
                   "released:true})" % (json.dumps(A1), json.dumps(C1)))
            click(p, "[data-sw=back]")
            check(p.eval("document.querySelector('[data-sw=overlay]').hidden") is True,
                  "edit: Cancel closes the sheet")
            errs = errors(p)
            check(not errs, "sheet: no console errors", errs)

            # ═══ 5. THE LIBRARY ═══════════════════════════════════════════
            print("\n── library: teacher/decks.html ──")
            p = fresh(b)
            p.goto(base + "/teacher/decks.html", settle=1.5)
            wait(p, "document.querySelectorAll('[data-fd=lib-row]').length>0")
            rows = p.eval("Array.from(document.querySelectorAll('[data-fd=lib-row]')).map(function(r){"
                          "return [r.querySelector('.lib-title').textContent,r.querySelector('.lib-meta').textContent,"
                          "r.classList.contains('is-deleted')];})")
            titles = [r[0] for r in rows]
            check(titles[:1] == ["cells"] and "Cell biology" in titles and "Making CO2" in titles
                  and "Old ecology" in titles and "Scratch deck" not in titles and "Bonding" not in titles,
                  "library: My decks lists own decks; a deleted unused deck is gone", titles)
            cb = [r for r in rows if r[0] == "Cell biology"][0]
            check("3 cards" in cb[1] and "Ms Nwosu" in cb[1] and "20 Sep 2026" in cb[1]
                  and "Used in 2 assignments" in cb[1],
                  "library: a row carries N cards · author · date · used in N", cb[1])
            old = [r for r in rows if r[0] == "Old ecology"][0]
            check(old[2] and "Deleted · used in 2 assignments" in old[1],
                  "library: a deleted deck in use stays, greyed, 'Deleted · used in 2 assignments'",
                  old)
            check(p.eval("(function(){var r=Array.from(document.querySelectorAll('[data-fd=lib-row]')).filter("
                         "function(n){return n.getAttribute('data-fd-id')===%s;})[0];"
                         "return !r.querySelector('[data-fd=lib-edit]')&&!r.querySelector('[data-fd=lib-delete]');})()"
                         % json.dumps(D3)),
                  "library: a deleted deck offers no Edit and no Delete")
            n_nav = p.eval("Array.from(document.querySelectorAll('[data-port-region=topbar] a'))"
                           ".filter(function(a){return a.textContent.trim()==='Flashcard decks';}).length")
            check(n_nav == 1, "library: the bar carries 'Flashcard decks' once", n_nav)
            p.screenshot(os.path.join(shots, "library-1280.png"), width=1280, height=800)
            p.screenshot(os.path.join(shots, "library-390.png"), width=390, height=844)
            overflow(p, "library")
            sentences(p, "library")
            p.set_viewport(1280, 800)
            # share toggle on D2 (shared → Unshare)
            p.eval("(function(){var r=Array.from(document.querySelectorAll('[data-fd=lib-row]')).filter("
                   "function(n){return n.getAttribute('data-fd-id')===%s;})[0];"
                   "r.querySelector('[data-fd=lib-share]').click();})()" % json.dumps(D2))
            wait(p, "window.__FD__.calls.some(function(c){return c.kind==='update';})")
            up = calls(p, None, kind="update")
            check(up and up[-1]["table"] == "flashcard_decks"
                  and up[-1]["values"] == {"shared_with_school": False}
                  and up[-1]["filters"][0] == {"op": "eq", "col": "id", "val": D2},
                  "library: Unshare writes shared_with_school=false on that deck", up)
            wait(p, "(function(){var r=document.querySelector(\"[data-fd=lib-row][data-fd-id='%s'] [data-fd=lib-share]\");"
                    "return r&&r.textContent==='Share';})()" % D2)
            check(p.eval("document.querySelector(\"[data-fd=lib-row][data-fd-id='%s'] [data-fd=lib-share]\").textContent" % D2)
                  == "Share", "library: the row then offers Share")
            # delete D2: two presses
            p.eval("document.querySelector(\"[data-fd=lib-row][data-fd-id='%s'] [data-fd=lib-delete]\").click()" % D2)
            n_up = len(calls(p, None, kind="update"))
            check(p.eval("document.querySelector(\"[data-fd=lib-row][data-fd-id='%s'] [data-fd=lib-delete]\").textContent" % D2)
                  == "Confirm" and n_up == 1, "library: the first Delete press only arms it")
            p.eval("document.querySelector(\"[data-fd=lib-row][data-fd-id='%s'] [data-fd=lib-delete]\").click()" % D2)
            wait(p, "window.__FD__.calls.filter(function(c){return c.kind==='update';}).length>=2")
            up = calls(p, None, kind="update")
            check(len(up) == 2 and list(up[-1]["values"].keys()) == ["deleted_at"]
                  and up[-1]["filters"][0]["val"] == D2,
                  "library: the second press soft-deletes (deleted_at) that deck", up[-1] if up else None)
            wait(p, "!document.querySelector(\"[data-fd=lib-row][data-fd-id='%s']\")" % D2)
            check(not p.eval("!!document.querySelector(\"[data-fd=lib-row][data-fd-id='%s']\")" % D2),
                  "library: a deleted unused deck leaves the list")
            # shared tab + duplicate a colleague's deck
            click(p, "[data-fd=lib-tabs] [data-fd-key=shared]")
            srows = p.eval("Array.from(document.querySelectorAll('[data-fd=lib-row] .lib-title')).map(function(n){return n.textContent;})")
            check(srows == ["Bonding"], "library: Shared lists colleagues' ready shared decks", srows)
            check(p.eval("(function(){var r=document.querySelector('[data-fd=lib-row]');"
                         "return !r.querySelector('[data-fd=lib-edit]')&&!r.querySelector('[data-fd=lib-share]')"
                         "&&!r.querySelector('[data-fd=lib-delete]')&&!!r.querySelector('[data-fd=lib-duplicate]');})()"),
                  "library: a colleague's deck offers Duplicate only")
            click(p, "[data-fd=lib-row] [data-fd=lib-duplicate]")
            wait(p, "!!document.querySelector('[data-fd=panel]:not([hidden]) [data-fd=editor]')")
            dup = calls(p, "flashcard_deck_duplicate")
            check(dup and dup[-1]["args"] == {"p_deck": D5},
                  "library: Duplicate calls flashcard_deck_duplicate on that deck", dup)
            check(p.eval("document.querySelector('[data-fd=panel] [data-fd=title]').value") == "Bonding (copy)"
                  and p.eval("document.querySelectorAll('[data-fd=panel] [data-fd=card]').length") == 2,
                  "library: the copy opens in the review table")
            p.eval("(function(){var q=document.querySelector('[data-fd=panel] [data-fd=q]');"
                   "q.value='Ionic bonding?';q.dispatchEvent(new Event('input'));})()")
            p.screenshot(os.path.join(shots, "library-edit-390.png"), width=390, height=844,
                         full_page=False)
            overflow(p, "library editor")
            p.set_viewport(1280, 800)
            click(p, "[data-fd=panel] [data-fd=save]")
            wait(p, "document.querySelector('[data-fd=panel]').hidden")
            sv = calls(p, "flashcard_deck_save")
            check(sv and sv[-1]["args"]["p_deck"] not in (None, D5)
                  and sv[-1]["args"]["p_cards"][0]["question"] == "Ionic bonding?",
                  "library: the copy is saved as the teacher's own deck, not the colleague's",
                  sv[-1]["args"] if sv else None)
            click(p, "[data-fd=lib-tabs] [data-fd-key=mine]")
            wait(p, "Array.from(document.querySelectorAll('[data-fd=lib-row] .lib-title')).some(function(n){return n.textContent==='Bonding (copy)';})")
            check(p.eval("Array.from(document.querySelectorAll('[data-fd=lib-row] .lib-title')).some(function(n){return n.textContent==='Bonding (copy)';})"),
                  "library: the copy is listed under My decks")
            # search
            p.eval("(function(){var s=document.querySelector('[data-fd=lib-search]');s.value='cell';"
                   "s.dispatchEvent(new Event('input'));})()")
            st = p.eval("Array.from(document.querySelectorAll('[data-fd=lib-row] .lib-title')).map(function(n){return n.textContent;})")
            check(st == ["cells", "Cell biology"] or sorted(st) == sorted(["cells", "Cell biology"]),
                  "library: search filters by title", st)
            # New deck opens the deck step without a picker
            p.eval("(function(){var s=document.querySelector('[data-fd=lib-search]');s.value='';"
                   "s.dispatchEvent(new Event('input'));})()")
            click(p, "[data-fd=new-deck]")
            nl = p.eval("Array.from(document.querySelectorAll('[data-fd=panel] [data-fd=source-chips] .sw-chip')).map(function(b){return b.textContent;})")
            check(nl == ["Upload", "Paste", "Type"], "library: New deck offers Upload · Paste · Type", nl)
            click(p, "[data-fd=panel] [data-fd=source-chips] [data-fd-key=type]")
            p.screenshot(os.path.join(shots, "library-new-1280.png"), width=1280, height=800,
                         full_page=False)
            click(p, "[data-fd=panel-close]")
            errs = errors(p)
            check(not errs, "library: no console errors", errs)

            # ═══ 6. THE NAV LINK on another teacher page ══════════════════
            print("\n── nav: the link on a hand-written teacher page ──")
            for page in ("timetable.html", "today.html"):
                p = fresh(b)
                p.goto(base + "/teacher/" + page, settle=2.0)
                links = p.eval("Array.from(document.querySelectorAll('a')).filter(function(a){"
                               "return a.textContent.trim()==='Flashcard decks';}).map(function(a){"
                               "return a.getAttribute('href');})")
                check(links and len(links) == 1 and links[0].startswith("/teacher/decks.html"),
                      "nav: 'Flashcard decks' is injected once on teacher/%s" % page, links)
                # The bar's own width, not the page's: the link must not push
                # a phone-width bar sideways whatever the page below it does.
                for w in (360, 390):
                    p.set_viewport(w, 844, settle=0.3)
                    wide = p.eval("(function(){var n=document.querySelector('[data-port-region=topbar]');"
                                  "return n?[n.scrollWidth,n.clientWidth]:null;})()")
                    check(bool(wide) and wide[0] <= wide[1] + 1,
                          "nav: teacher/%s's bar does not scroll sideways at %dpx" % (page, w), wide)
    finally:
        server.shutdown()

    print("\nscreenshots: %s" % shots)
    if fails:
        print("\n❌ flashcard_decks_drive: %d FAIL" % len(fails))
        for f in fails:
            print("   · " + f)
        return 1
    print("\n✅ flashcard_decks_drive: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
