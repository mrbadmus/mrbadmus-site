/* ⊕ MRB-351 — THE FLASHCARD HOMEWORK ENGINE.
 *
 * The state machine behind a teacher-set deck in the class page's flashcard
 * overlay. It owns NO markup: the overlay is Design's one flashcard component
 * (student_rulings.py, "PHASE 2 — THE FLASHCARDS"), and in homework mode its
 * `cardVals()` reads this engine instead of the practice deck. One component,
 * two decks.
 *
 * WHAT IT DOES
 *   · make phase (mode = make): each unmade card in order — question, the
 *     pupil writes, Check locks it and turns the card to the model answer,
 *     Got it / Nearly / Not yet, next. Leaving mid-way is fine; reopening
 *     continues at the next unmade card (the server's state says which).
 *   · review phase: a queue built at the start of each pass — Not yet →
 *     Nearly → never rated → Got it. Got it leaves the pass; Nearly and Not yet
 *     go to the back. The pass ends when the queue is empty or the pupil
 *     taps Finish for now.
 *   · events: card_shown, answer_submitted, revealed, rated, session_finish,
 *     visibility — each with a client-generated id, the device clock and
 *     whether the tab was visible. They are queued on the DEVICE (so a flaky
 *     connection or a closed tab loses nothing), sent in batches, and are
 *     idempotent on the server by id. The SERVER computes every duration.
 *
 * WHAT IT DOES NOT DO: decide completion. `flashcard_record()` does, from the
 * events, and says so in the state it returns.
 *
 * Transport is injected (`MRBHomework.transport`) so the fixture page and the
 * Node tests run it with no network at all.
 */
(function (root) {
  "use strict";

  var STORE = "mrbadmusai.fchw.v1.";
  var FLUSH_MS = 2500;

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

  var ORDER = { not_yet: 0, nearly: 1, none: 2, got_it: 3 };

  function Engine(assignmentId, state, opts) {
    this.id = assignmentId;
    this.opts = opts || {};
    this.pending = load(assignmentId);
    this.sending = false;
    this.timer = null;
    this.onChange = null;
    this.error = null;
    this.draft = "";
    this.revealed = false;
    this.mine = null;         // the pupil's answer to the current card, once written
    this.passRated = 0;       // ratings in this pass
    this.acted = 0;           // answers written + ratings, this visit
    this.fresh = false;       // "Your deck is ready" moment
    this.apply(state);
    this.start();
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

  // `stage` is set, never derived: the card being rated in the make phase
  // is already `made` by then, so "are there unmade cards?" would misfile
  // the LAST card's make-phase rating as a review.
  Engine.prototype.phase = function () {
    if (!this.state) { return "loading"; }
    if (this.betweenPasses) { return this.state.complete ? "done" : "pause"; }
    return this.stage;
  };

  // MRB-351 §4's order — Not yet → Nearly → never rated → Got it — with the
  // Got it cards that still need securing ahead of the ones already secured,
  // so a second sitting starts on the work that is left.
  function rank(c) {
    var r = ORDER[c.last || "none"];
    return r === 3 && c.secured ? 4 : r;
  }
  Engine.prototype.buildQueue = function () {
    var cs = this.cards.slice();
    cs.sort(function (a, b) {
      var oa = rank(a), ob = rank(b);
      return oa !== ob ? oa - ob : a.position - b.position;
    });
    this.queue = cs.map(function (c) { return c.id; });
    this.passRated = 0;
  };

  Engine.prototype.start = function () {
    this.betweenPasses = false;
    this.stage = (this.state && this.state.mode === "make" && this.unmade().length) ? "make" : "review";
    if (this.stage === "make") {
      this.current = this.unmade()[0];
    } else {
      this.buildQueue();
      this.current = this.byId[this.queue[0]];
    }
    this.show();
  };

  Engine.prototype.show = function () {
    this.revealed = false;
    this.draft = "";
    this.mine = null;
    if (this.current) {
      this.event({ type: "card_shown", card: this.current.id, phase: this.phase() === "make" ? "make" : "review" });
    }
    this.changed();
  };

  // ── pupil actions ────────────────────────────────────────────────────
  Engine.prototype.setDraft = function (text) {
    this.draft = String(text == null ? "" : text).slice(0, 500);
  };
  Engine.prototype.canCheck = function () { return /\S/.test(this.draft); };

  Engine.prototype.check = function () {
    if (this.phase() !== "make" || this.revealed || !this.canCheck() || !this.current) { return; }
    var c = this.current;
    this.event({ type: "answer_submitted", card: c.id, phase: "make", answer: this.draft });
    this.event({ type: "revealed", card: c.id, phase: "make" });
    c.made = true; c.mine = this.draft;
    this.mine = this.draft;
    this.revealed = true;
    this.changed();
    this.flushSoon(400);
  };

  Engine.prototype.flip = function () {
    var p = this.phase();
    if (p !== "review" || !this.current) { return; }
    if (!this.revealed) {
      this.revealed = true;
      this.event({ type: "revealed", card: this.current.id, phase: "review" });
      this.changed();
    }
  };

  Engine.prototype.rate = function (rating) {
    if (["got_it", "nearly", "not_yet"].indexOf(rating) < 0 || !this.current || !this.revealed) { return; }
    var p = this.phase();
    var c = this.current;
    this.acted += 1;
    this.event({ type: "rated", card: c.id, phase: p === "make" ? "make" : "review", rating: rating });
    c.last = rating; c.lastLocal = rating;
    if (rating === "got_it") { c.known = true; }
    if (p === "make") {
      var next = this.unmade()[0];
      if (next) { this.current = next; this.show(); }
      else {
        // "Your deck is ready" → straight into review.
        this.stage = "review";
        this.fresh = true;
        this.buildQueue();
        this.current = this.byId[this.queue[0]];
        this.show();
      }
    } else {
      this.passRated += 1;
      this.queue.shift();
      if (rating !== "got_it") { this.queue.push(c.id); }
      this.fresh = false;
      if (this.queue.length) { this.current = this.byId[this.queue[0]]; this.show(); }
      else { this.endPass(); }
    }
    this.flushSoon(600);
  };

  // "The session ends when the queue is empty or the pupil taps Finish for
  // now" (MRB-351 §4) — both end the sitting on the server.
  Engine.prototype.endPass = function () {
    this.betweenPasses = true;
    this.current = null;
    this.revealed = false;
    this.event({ type: "session_finish" });
    this.changed();
    this.flush();
  };

  Engine.prototype.finish = function () { if (!this.betweenPasses) { this.endPass(); } };

  Engine.prototype.again = function () {
    this.fresh = false;
    this.start();
  };

  Engine.prototype.visibility = function () {
    this.event({ type: "visibility" });
    if (!visibleNow()) { this.flush(); }
  };

  // ── what the overlay draws ───────────────────────────────────────────
  Engine.prototype.view = function () {
    var s = this.state || {};
    var n = s.n || this.cards.length;
    var made = this.cards.filter(function (c) { return c.made; }).length;
    var secured = s.secured || 0, known = s.known || 0;
    var p = this.phase();
    var word = s.rule === "quick" ? "known" : "secured";
    var count = s.rule === "quick" ? known : secured;
    var hint = "";
    if (p !== "make" && !s.complete) {
      if (s.rule === "quick") { hint = (n - known) + (n - known === 1 ? " card to get right" : " cards to get right"); }
      else if (known >= n) { hint = "Get every card right once more, later on"; }
      else { hint = (n - known) + (n - known === 1 ? " card still to get right" : " cards still to get right"); }
    }
    var pos = 0, total = n;
    if (p === "make" && this.current) { pos = made + (this.revealed ? 0 : 1); total = n; }
    else if (p === "make") { pos = made; }
    else if (this.current && this.queue) { pos = this.passRated + 1; total = this.passRated + this.queue.length; }
    return {
      phase: p, n: n, made: made, count: count, word: word, hint: hint,
      progressText: p === "make" ? ("Made " + made + " / " + n) : (count + " of " + n + " " + word),
      pct: n ? Math.round(((p === "make" ? made : count) / n) * 100) : 0,
      fresh: this.fresh,
      pos: pos, total: total,
      card: this.current,
      revealed: this.revealed,
      mine: this.mine || (this.current && this.current.mine) || null,
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
    if (this.sending || !this.pending.length || typeof t !== "function") { return Promise.resolve(); }
    this.sending = true;
    var batch = this.pending.slice(0, 200);
    return Promise.resolve().then(function () { return t(self.id, batch); }).then(function (state) {
      self.sending = false;
      var sent = {};
      batch.forEach(function (e) { sent[e.id] = true; });
      self.pending = self.pending.filter(function (e) { return !sent[e.id]; });
      save(self.id, self.pending);
      self.error = null;
      if (state) { self.merge(state); }
      if (self.pending.length) { self.flushSoon(200); }
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
    active: null,
    open: function (assignmentId) {
      if (engines[assignmentId]) {
        Api.active = engines[assignmentId];
        if (Api.active.betweenPasses) { Api.active.again(); }
        return Promise.resolve(Api.active);
      }
      var t = Api.transport;
      if (typeof t !== "function") { return Promise.reject(new Error("no_transport")); }
      // Anything still queued on this device from a previous visit goes
      // first, so the state we start from already includes it.
      var queued = load(assignmentId);
      return Promise.resolve(t(assignmentId, queued)).then(function (state) {
        save(assignmentId, []);
        var e = new Engine(assignmentId, state);
        engines[assignmentId] = e;
        Api.active = e;
        return e;
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

  if (root.document && root.addEventListener) {
    root.document.addEventListener("visibilitychange", function () {
      if (Api.active) { Api.active.visibility(); }
    });
    root.addEventListener("pagehide", function () { Api.flushAll(); });
  }

  if (typeof module !== "undefined" && module.exports) { module.exports = Api; }
  root.MRBHomework = Api;
})(typeof window !== "undefined" ? window : globalThis);
