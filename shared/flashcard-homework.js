/* ⊕ MRB-351 — THE FLASHCARD HOMEWORK ENGINE.
 *
 * The state machine behind a teacher-set deck in the class page's flashcard
 * overlay. It owns NO markup: the overlay is Design's one flashcard component
 * (student_rulings.py, "PHASE 2 — THE FLASHCARDS"), and in homework mode its
 * `cardVals()` reads this engine instead of the practice deck. One component,
 * two decks.
 *
 * ⊕ PUPIL FLOW (Stage A, 28 Sep 2026 — docs/mrb351/PUPIL-FLOW.md, §11 wins).
 *
 *   A PASS is one run through the deck. Every card in the pass is answered
 *   once — typed, or "I don't know" — then rated. Wrong cards do NOT loop
 *   round inside a pass; a pass always ends.
 *
 *   Each card goes through four states:
 *     A  question + answer box                 (revealed = false)
 *     B  checking: model answer showing, the three ratings showing,
 *        none filled, chip "Checking…"         (verdict = "pending")
 *     C  verdict: chip Right / Nearly / Wrong / No answer, the suggested
 *        rating filled; no verdict → no chip, nothing filled
 *     D  rated: the next card in state A, or the end screen
 *
 *   The headline counts THIS PASS: "2 of 10 right" — a card is right when its
 *   rating in this pass is Got it. `‹ Back` re-opens the previous card in
 *   state A; answering and rating it again REPLACES its rating in this pass
 *   (the server keeps every event; its latest `rated` wins).
 *
 *   Make mode = two passes in the first sitting: the writing pass, its end
 *   screen, then the review pass of the SAME sitting. Every other pass ends
 *   its sitting with `session_finish`.
 *
 *   events: card_shown, answer_submitted, revealed, rated, session_finish,
 *   visibility — each with a client-generated id, the device clock and
 *   whether the tab was visible. They are queued on the DEVICE (so a flaky
 *   connection or a closed tab loses nothing), sent in batches, and are
 *   idempotent on the server by id. The SERVER computes every duration.
 *
 * WHAT IT DOES NOT DO: decide completion. `flashcard_record()` does, from the
 * events, and says so in the state it returns.
 *
 * Transport, the model check and the resume read are injected
 * (`MRBHomework.transport` / `.modelCheck` / `.resumeRead`) so the fixture
 * page and the Node tests run it with no network at all.
 */
(function (root) {
  "use strict";

  var STORE = "mrbadmusai.fchw.v1.";
  var FLUSH_MS = 2500;
  var MODEL_WAIT_MS = 4000;
  var HOUR_MS = 60 * 60 * 1000;
  var RESUME_MS = 10 * 60 * 1000;
  var IDK_TEXT = "I don't know";

  function uuid() {
    if (root.crypto && root.crypto.randomUUID) { return root.crypto.randomUUID(); }
    var b = new Uint8Array(16);
    (root.crypto || { getRandomValues: function (a) { for (var i = 0; i < a.length; i++) { a[i] = Math.floor(Math.random() * 256); } return a; } }).getRandomValues(b);
    b[6] = (b[6] & 0x0f) | 0x40; b[8] = (b[8] & 0x3f) | 0x80;
    var h = Array.prototype.map.call(b, function (x) { return (x + 256).toString(16).slice(1); }).join("");
    return h.slice(0, 8) + "-" + h.slice(8, 12) + "-" + h.slice(12, 16) + "-" + h.slice(16, 20) + "-" + h.slice(20);
  }

  function visibleNow() {
    return !(root.document && root.document.visibilityState === "hidden");
  }

  function load(key) {
    try { return JSON.parse(root.localStorage.getItem(STORE + key) || "[]"); } catch (e) { return []; }
  }
  function save(key, list) {
    try { root.localStorage.setItem(STORE + key, JSON.stringify(list)); } catch (e) { /* private mode */ }
  }
  // When this assignment's last sitting ended ON THIS DEVICE (A8b).
  function loadEnd(key) {
    try { var v = Number(root.localStorage.getItem(STORE + "end." + key)); return v > 0 ? v : null; } catch (e) { return null; }
  }
  function saveEnd(key, at) {
    try { root.localStorage.setItem(STORE + "end." + key, String(at)); } catch (e) { /* private mode */ }
  }

  // ── the no-model answer check: an EXACT port of SQL flashcard_quick_check
  // (supabase/migrations/20260924180100_mrb351_flashcards_functions.sql).
  // A12: SQL and JS must agree case for case, or the teacher sees `pending`
  // for an answer the pupil was told was Right. Both lists are copied
  // verbatim; `quickcheck_test` compares this against the database.
  var IDK = ["idk", "i dont know", "i don t know", "dont know", "don t know", "dunno",
             "no idea", "not sure", "no clue", "pass", "skip", "x", "xx", "xxx", "na", "n a",
             "unsure", "forgot", "i forgot", "i dunno", "idek", "not a clue",
             "no answer", "blank", "nk", "dk", "dno", "donno", "i dno", "hmm", "um", "erm"];
  var FUNCTION_WORDS = ["the", "a", "an", "it", "is", "in", "of", "and", "to", "on", "by"];
  function norm(s) {
    return String(s == null ? "" : s).toLowerCase()
      .replace(/[^a-z0-9 ]+/g, " ")
      .replace(/\s+/g, " ")
      .replace(/^ +| +$/g, "");
  }
  function quickCheck(pupil, model) {
    var pa = norm(pupil), ma = norm(model);
    if (pa === "") { return "blank"; }
    if (pa === ma) { return "match"; }
    if (IDK.indexOf(pa) >= 0) { return "blank"; }
    if (pa.indexOf(" ") < 0 && FUNCTION_WORDS.indexOf(pa) >= 0) { return "no"; }
    if (pa.indexOf(" ") < 0) {
      return (" " + ma + " ").indexOf(" " + pa + " ") >= 0 ? "match" : "no";
    }
    return null;
  }

  var VERDICTS = ["match", "partial", "no", "blank"];
  var CHIP = { pending: "Checking…", match: "Right", partial: "Nearly", no: "Wrong", blank: "No answer" };
  var SUGGEST = { match: "got_it", partial: "nearly", no: "not_yet", blank: "not_yet" };
  var ORDER = { not_yet: 0, nearly: 1, none: 2, got_it: 3 };

  function Engine(assignmentId, state, opts) {
    this.id = assignmentId;
    this.opts = opts || {};
    this.pending = load(assignmentId);
    this.sending = false;
    this.timer = null;
    this.onChange = null;
    this.error = null;
    this.acted = 0;           // answers + ratings, this visit (A13)
    this.sittingOpen = false; // events sent since the last session_finish
    this.tok = 0;             // bumps whenever the card in front changes
    this.apply(state);
    this.start(this.opts.resume || null);
  }

  Engine.prototype.apply = function (state) {
    this.state = state;
    this.cards = (state && state.cards) || [];
    this.byId = {};
    for (var i = 0; i < this.cards.length; i++) { this.byId[this.cards[i].id] = this.cards[i]; }
  };

  Engine.prototype.merge = function (state) {
    // A late server reply must not rewind what the pupil has just done on the
    // device: `made`/`last` are kept where the device is ahead.
    var local = this.byId;
    this.apply(state);
    for (var id in local) {
      var c = this.byId[id], l = local[id];
      if (!c) { continue; }
      if (l.made && !c.made) { c.made = true; c.mine = l.mine; }
      if (l.lastLocal) { c.last = l.lastLocal; c.lastLocal = l.lastLocal; }
    }
  };

  Engine.prototype.unmade = function () {
    return this.cards.filter(function (c) { return !c.made; });
  };

  Engine.prototype.phase = function () {
    if (!this.state) { return "loading"; }
    if (this.ended) { return "end"; }
    return this.stage;
  };

  // MRB-351 §4's order — Not yet → Nearly → never rated → Got it — with the
  // Got it cards that still need securing ahead of the ones already secured,
  // so a second sitting starts on the work that is left.
  function rank(c) {
    var r = ORDER[c.last || "none"];
    return r === 3 && c.secured ? 4 : r;
  }
  Engine.prototype.ranked = function () {
    var cs = this.cards.slice();
    cs.sort(function (a, b) {
      var oa = rank(a), ob = rank(b);
      return oa !== ob ? oa - ob : a.position - b.position;
    });
    return cs.map(function (c) { return c.id; });
  };
  Engine.prototype.byPosition = function (ids) {
    var self = this;
    return ids.filter(function (id) { return self.byId[id]; })
      .sort(function (a, b) { return self.byId[a].position - self.byId[b].position; });
  };

  // A new pass. `resume` = {card_id: {rating, phase}} for the sitting still
  // open on the server (a reload within ten minutes): those cards count as
  // done in this pass and it carries on from the first card without one.
  Engine.prototype.start = function (resume) {
    var self = this;
    this.ended = false;
    this.end = null;
    this.pass = {};
    this.drafts = {};
    this.afterWriting = false;
    var mode = this.state && this.state.mode;
    var done = [];
    var r = resume || {};
    var entries = Object.keys(r).filter(function (id) { return self.byId[id]; });
    var makeDone = entries.filter(function (id) { return r[id].phase === "make"; });
    var reviewDone = entries.filter(function (id) { return r[id].phase !== "make"; });
    if (mode === "make" && this.unmade().length) {
      this.stage = "make";
      done = this.byPosition(makeDone);
      var todo = this.unmade().map(function (c) { return c.id; })
        .filter(function (id) { return done.indexOf(id) < 0; });
      this.passIds = done.concat(todo);
    } else {
      this.stage = "review";
      // The writing pass happened in this very sitting: this is its review pass.
      this.afterWriting = mode === "make" && makeDone.length > 0 && !this.opts.newSitting;
      done = this.byPosition(reviewDone);
      this.passIds = done.concat(this.ranked().filter(function (id) { return done.indexOf(id) < 0; }));
    }
    done.forEach(function (id) { self.pass[id] = { rating: r[id].rating, mine: null, verdict: null }; });
    this.idx = done.length;
    if (this.idx >= this.passIds.length && this.passIds.length) { this.endPass(); return; }
    this.show();
  };

  Engine.prototype.current = function () {
    return this.ended ? null : (this.byId[this.passIds[this.idx]] || null);
  };

  Engine.prototype.show = function () {
    var c = this.current();
    this.tok += 1;
    this.revealed = false;
    this.verdict = null;
    this.mine = null;
    this.draft = c ? (this.drafts[c.id] || "") : "";
    if (c) {
      this.event({ type: "card_shown", card: c.id, phase: this.stage });
    }
    this.changed();
  };

  // ── pupil actions ────────────────────────────────────────────────────
  Engine.prototype.setDraft = function (text) {
    this.draft = String(text == null ? "" : text).slice(0, 500);
    var c = this.current();
    if (c && !this.revealed) { this.drafts[c.id] = this.draft; }
  };
  Engine.prototype.canCheck = function () { return !this.revealed && /\S/.test(this.draft || ""); };

  Engine.prototype.reveal = function (answer, local, extra) {
    var c = this.current();
    var ev = { type: "answer_submitted", card: c.id, phase: this.stage, answer: answer };
    for (var k in (extra || {})) { ev[k] = extra[k]; }
    this.event(ev);
    this.event({ type: "revealed", card: c.id, phase: this.stage });
    if (this.stage === "make" && !c.made) { c.made = true; c.mine = answer; }
    this.mine = answer;
    this.drafts[c.id] = extra && extra.idk ? "" : answer;
    this.revealed = true;
    this.acted += 1;
    this.verdict = local;
  };

  Engine.prototype.check = function () {
    var c = this.current();
    if (!c || !this.canCheck()) { return; }
    var answer = this.draft;
    var local = quickCheck(answer, c.answer);
    var waiting = !local && typeof Api.modelCheck === "function";
    this.reveal(answer, local || (waiting ? "pending" : null));
    this.changed();
    this.flushSoon(400);
    if (waiting) { this.askModel(c, answer); }
  };

  // A4: "I don't know" reveals the model answer and lands in state C with
  // chip "No answer" and Not yet filled; the pupil still taps to go on.
  Engine.prototype.idk = function () {
    var c = this.current();
    if (!c || this.revealed) { return; }
    this.reveal(IDK_TEXT, "blank", { idk: true });
    this.changed();
    this.flushSoon(400);
  };

  // §3.2–3.3: the model's verdict, if it lands inside four seconds and the
  // pupil has not already rated or moved on. Anything else → no chip.
  Engine.prototype.askModel = function (c, answer) {
    var self = this, tok = this.tok;
    var settled = false;
    function land(v) {
      if (settled) { return; }
      settled = true;
      var now = self.current();
      // (compared by id: a server reply rebuilds the card objects)
      if (self.tok !== tok || !now || now.id !== c.id || !self.revealed || self.verdict !== "pending") { return; }
      self.verdict = VERDICTS.indexOf(v) >= 0 ? v : null;
      self.changed();
    }
    setTimeout(function () { land(null); }, Api.modelWaitMs || MODEL_WAIT_MS);
    Promise.resolve().then(function () { return Api.modelCheck(self.id, c.id, answer, self); })
      .then(function (v) { land(typeof v === "string" ? v : null); }, function () { land(null); });
  };

  Engine.prototype.suggestion = function () {
    return (this.revealed && this.verdict && SUGGEST[this.verdict]) || null;
  };

  Engine.prototype.rate = function (rating) {
    var c = this.current();
    if (["got_it", "nearly", "not_yet"].indexOf(rating) < 0 || !c || !this.revealed) { return; }
    var suggested = this.suggestion();
    this.acted += 1;
    this.event({ type: "rated", card: c.id, phase: this.stage, rating: rating,
                 via: suggested === rating ? "auto" : "tap" });
    c.last = rating; c.lastLocal = rating;
    if (rating === "got_it") { c.known = true; }
    this.pass[c.id] = { rating: rating, mine: this.mine, verdict: this.verdict === "pending" ? null : this.verdict };
    this.idx += 1;
    if (this.idx < this.passIds.length) { this.show(); } else { this.endPass(); }
    this.flushSoon(600);
  };

  // ‹ Back: the previous card of this pass, in state A, with what the pupil
  // wrote last time already in the box. No event of its own.
  Engine.prototype.canBack = function () { return !this.ended && this.idx > 0; };
  Engine.prototype.back = function () {
    if (!this.canBack()) { return; }
    this.idx -= 1;
    this.show();
  };

  Engine.prototype.right = function () {
    var self = this;
    return this.passIds.filter(function (id) { return self.pass[id] && self.pass[id].rating === "got_it"; }).length;
  };

  // The end of a pass. The writing pass of make mode keeps its sitting open
  // (its review pass follows in the same sitting); every other pass ends it.
  Engine.prototype.endPass = function () {
    var s = this.state || {};
    var writing = this.stage === "make";
    var now = Date.now();
    var prev = loadEnd(this.id);
    // A8b: another pass now cannot secure anything when this was a review
    // sitting (not make's own review pass) and no earlier sitting ended an
    // hour or more ago. No record on this device → trust the server's count.
    var tooSoon = !writing && s.rule !== "quick" && !this.afterWriting &&
      (prev ? (now - prev) < HOUR_MS : (s.sittings || 0) <= 1);
    this.ended = true;
    this.revealed = false;
    this.tok += 1;
    this.end = { right: this.right(), m: this.passIds.length, writing: writing,
                 tooSoon: tooSoon, settled: false };
    if (!writing) { this.sessionFinish(now); }
    this.changed();
    this.flush();
  };

  Engine.prototype.sessionFinish = function (now) {
    this.event({ type: "session_finish" });
    saveEnd(this.id, now || Date.now());
  };

  // × — ends the sitting if the pupil did anything in it (A13).
  Engine.prototype.finish = function () {
    if (this.sittingOpen && this.acted) { this.sessionFinish(); }
    this.flush();
  };

  Engine.prototype.again = function () {
    var fromWriting = this.ended && this.end && this.end.writing;
    this.start(null);
    if (fromWriting) { this.afterWriting = true; }
  };

  Engine.prototype.visibility = function () {
    this.event({ type: "visibility" });
    if (!visibleNow()) { this.flush(); }
  };

  // ── what the overlay draws ───────────────────────────────────────────
  Engine.prototype.view = function () {
    var self = this;
    var s = this.state || {};
    var n = s.n || this.cards.length;
    var secured = s.secured || 0;
    var p = this.phase();
    var c = this.current();
    var m = (this.passIds || []).length;
    var right = this.right();
    var segs = (this.passIds || []).map(function (id, i) {
      var e = self.pass[id];
      return { state: e ? (e.rating === "got_it" ? "right" : "answered") : "todo",
               current: !self.ended && i === self.idx };
    });
    var review = p === "review";
    var end = null;
    if (this.end) {
      var E = this.end;
      var ready = E.settled && !this.pending.length;
      var offline = !ready && this.error === "offline";
      var known = ready || offline;
      var all = secured >= n && n > 0;
      var button = !known ? null : (all || E.tooSoon) ? "done" : "again";
      end = {
        line1: E.right + " of " + E.m + " right this time",
        line2: ready ? (secured + " of " + n + " secured so far") : "",
        offline: offline,
        helper: button === "done" && E.tooSoon && !all ? "Revise flashcards one more time" : "",
        button: button,
        buttonLabel: button === "done" ? "Done" : button === "again" ? "Revise flashcards one more time" : ""
      };
    }
    var chip = this.revealed && this.verdict ? CHIP[this.verdict] : "";
    return {
      phase: p, n: n, m: m, right: right, secured: secured,
      headline: right + " of " + m + " right",
      securedLine: review && s.rule !== "quick" ? secured + " secured" : "",
      helper: review && secured < n ? "Revise flashcards one more time" : "",
      segments: segs,
      pos: c ? this.idx + 1 : 0,
      card: c,
      revealed: !!this.revealed,
      checking: this.revealed && this.verdict === "pending",
      verdict: this.verdict,
      chip: chip,
      suggest: this.suggestion(),
      mine: this.revealed ? this.mine : null,
      draft: this.draft || "",
      canBack: this.canBack(),
      end: end,
      complete: !!s.complete,
      note: s.note || null,
      title: s.title || "",
      mode: s.mode, rule: s.rule
    };
  };

  // ── events ───────────────────────────────────────────────────────────
  Engine.prototype.event = function (e) {
    e.id = uuid();
    e.at = Date.now();
    e.visible = visibleNow();
    this.pending.push(e);
    save(this.id, this.pending);
    if (e.type === "session_finish") { this.sittingOpen = false; }
    else if (e.type !== "visibility") { this.sittingOpen = true; }
    this.flushSoon(FLUSH_MS);
  };

  Engine.prototype.flushSoon = function (ms) {
    var self = this;
    if (this.timer) { clearTimeout(this.timer); }
    this.timer = setTimeout(function () { self.timer = null; self.flush(); }, ms);
  };

  Engine.prototype.flush = function () {
    var self = this;
    var t = Api.transport;
    if (this.sending) { return this.sending; }
    if (!this.pending.length || typeof t !== "function") {
      if (this.end && !this.end.settled && !this.pending.length && typeof t === "function") {
        this.end.settled = true; this.changed();
      }
      return Promise.resolve();
    }
    var batch = this.pending.slice(0, 200);
    this.sending = Promise.resolve().then(function () { return t(self.id, batch); }).then(function (state) {
      self.sending = false;
      var sent = {};
      batch.forEach(function (e) { sent[e.id] = true; });
      self.pending = self.pending.filter(function (e) { return !sent[e.id]; });
      save(self.id, self.pending);
      self.error = null;
      if (state) { self.merge(state); }
      if (self.pending.length) { self.flushSoon(200); }
      else if (self.end) { self.end.settled = true; }
      if (batch.some(function (e) { return e.type === "session_finish"; }) && Api.onSessionEnd) {
        try { Api.onSessionEnd(self.id); } catch (e) { /* fire and forget */ }
      }
      self.changed();
    }, function () {
      // Kept on the device; retried with a longer wait. Idempotent ids mean a
      // batch that DID land but whose reply was lost is harmless to resend.
      self.sending = false;
      self.error = "offline";
      self.flushSoon(8000);
      self.changed();
    });
    return this.sending;
  };

  Engine.prototype.changed = function () {
    if (typeof this.onChange === "function") {
      try { this.onChange(); } catch (e) { /* the page must survive */ }
    }
  };

  // ── the module ───────────────────────────────────────────────────────
  var engines = {};
  var Api = {
    transport: null,          // (assignmentId, events[]) → Promise<state>
    onSessionEnd: null,       // (assignmentId) → void
    modelCheck: null,         // (assignmentId, cardId, answer, engine) → Promise<verdict|null>
    resumeRead: null,         // (sessionId) → Promise<{card_id: {rating, phase, at}}>
    modelWaitMs: MODEL_WAIT_MS,
    active: null,
    quickCheck: quickCheck,
    open: function (assignmentId) {
      if (engines[assignmentId]) {
        Api.active = engines[assignmentId];
        // A pass that has ended starts afresh on reopening; one left
        // mid-way carries on where it was.
        if (Api.active.ended) { Api.active.opts.newSitting = true; Api.active.start(null); }
        return Promise.resolve(Api.active);
      }
      var t = Api.transport;
      if (typeof t !== "function") { return Promise.reject(new Error("no_transport")); }
      // Anything still queued on this device from a previous visit goes
      // first, so the state we start from already includes it.
      var queued = load(assignmentId);
      return Promise.resolve(t(assignmentId, queued)).then(function (state) {
        save(assignmentId, []);
        var sid = state && state.session_id;
        var read = (sid && typeof Api.resumeRead === "function")
          ? Promise.resolve().then(function () { return Api.resumeRead(sid); }).catch(function () { return null; })
          : Promise.resolve(null);
        return read.then(function (map) {
          var e = new Engine(assignmentId, state, { resume: fresh(map) });
          engines[assignmentId] = e;
          Api.active = e;
          return e;
        });
      });
    },
    close: function () {
      var e = Api.active;
      Api.active = null;
      if (e) { e.flush(); }
    },
    flushAll: function () {
      Object.keys(engines).forEach(function (k) { engines[k].flush(); });
    },
    _Engine: Engine,
    _reset: function () { engines = {}; Api.active = null; }
  };

  // A resume map is only honoured while the sitting is still live on the
  // server: the last rating inside the last ten minutes.
  function fresh(map) {
    if (!map) { return null; }
    var last = 0, k;
    for (k in map) { last = Math.max(last, Number(map[k].at) || 0); }
    if (!last || Date.now() - last > RESUME_MS) { return null; }
    return map;
  }

  if (root.document && root.addEventListener) {
    root.document.addEventListener("visibilitychange", function () {
      if (Api.active) { Api.active.visibility(); }
    });
    root.addEventListener("pagehide", function () { Api.flushAll(); });
  }

  if (typeof module !== "undefined" && module.exports) { module.exports = Api; }
  root.MRBHomework = Api;
})(typeof window !== "undefined" ? window : globalThis);
