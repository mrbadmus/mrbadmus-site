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
 *   screen, then the review pass of the SAME sitting.
 *
 * ⊕ SHARPEN (29 Sep 2026 — PUPIL-FLOW.md §13 wins over everything above).
 *
 *   · THE VERDICT CAPS THE RATING. Right → up to Got it, Nearly → up to
 *     Nearly, Wrong / No answer → Not yet only. Enforced here, in `rate()`,
 *     so the buttons, keys 1·2·3 and the swipe all obey it. While the check
 *     is out ("Checking…") nothing can be rated; no verdict → no cap.
 *   · "I DON'T KNOW" IS A LEARNING STEP. The card stays on its question,
 *     the model answer shows under it, and the pupil writes it in their own
 *     words; that answer is checked, capped at Nearly. The card comes round
 *     once more at the end of the pass as a plain card.
 *   · A PASS THAT IS NOT ALL RIGHT ENDS ON "Try again", which replays only
 *     the cards that are not Got it, in the pass's own order, in the SAME
 *     server sitting (no `session_finish`). On that retry the bar becomes
 *     numbered chips; a green one can be tapped to redo that card (a
 *     "detour") without leaving the queue.
 *   · A PASS THAT IS ALL RIGHT ends the sitting (`session_finish`) and
 *     offers one button, Done. × still ends the sitting (A13).
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
  // §13.1 — how high a rating may go.
  var RANK = { not_yet: 0, nearly: 1, got_it: 2 };
  var RATINGS = ["not_yet", "nearly", "got_it"];

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
    this.retries = 0;          // Try again passes in this sitting
    this.replayed = {};        // cards an "I don't know" sent round again
    this.detour = null;        // a green card being redone on a retry
    this.learn = false;        // "I don't know": the own-words step
    this.idkNow = false;       // this showing of the card began with it
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
    done.forEach(function (id) { self.pass[id] = { rating: r[id].rating, mine: null, verdict: null, cap: null }; });
    // The pass's own order, fixed for the whole sitting: the bar, the chips
    // and a Try again all read it.
    this.order = this.passIds.slice();
    this.idx = done.length;
    if (this.idx >= this.passIds.length && this.passIds.length) { this.endPass(); return; }
    this.show();
  };

  Engine.prototype.current = function () {
    if (this.ended) { return null; }
    if (this.detour) { return this.byId[this.detour] || null; }
    return this.byId[this.passIds[this.idx]] || null;
  };

  Engine.prototype.show = function () {
    var c = this.current();
    this.tok += 1;
    this.revealed = false;
    this.learn = false;
    this.idkNow = false;
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
    this.learn = false;
    this.acted += 1;
    this.verdict = local;
  };

  Engine.prototype.check = function () {
    var c = this.current();
    if (!c || !this.canCheck()) { return; }
    var answer = this.draft;
    var local = quickCheck(answer, c.answer);
    var waiting = !local && typeof Api.modelCheck === "function";
    // After "I don't know", this is the pupil's answer in their own words.
    this.reveal(answer, local || (waiting ? "pending" : null), this.learn ? { own_words: true } : null);
    this.changed();
    this.flushSoon(400);
    if (waiting) { this.askModel(c, answer); }
  };

  // §13.1.4: "I don't know" is a learning step. The card stays on its
  // question, the model answer shows under it, and the pupil writes it in
  // their own words (the next Check). The press itself is recorded as it
  // always was — `answer_submitted` "I don't know" (idk) + `revealed` — so a
  // make-mode card is made, and the teacher sees what was pressed.
  Engine.prototype.idk = function () {
    var c = this.current();
    if (!c || this.revealed || this.learn) { return; }
    this.event({ type: "answer_submitted", card: c.id, phase: this.stage, answer: IDK_TEXT, idk: true });
    this.event({ type: "revealed", card: c.id, phase: this.stage });
    if (this.stage === "make" && !c.made) { c.made = true; c.mine = IDK_TEXT; }
    this.acted += 1;
    this.learn = true;
    this.idkNow = true;
    this.mine = IDK_TEXT;
    this.draft = "";
    this.drafts[c.id] = "";
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

  // §13.1.1–3 — the highest rating this answer may have.
  //   null    no cap (no verdict: a timeout, no key, an old function)
  //   "none"  nothing may be rated yet (the check is still out)
  //   else    the highest allowed rating; after "I don't know", Nearly.
  Engine.prototype.cap = function () {
    if (!this.revealed) { return null; }
    if (this.verdict === "pending") { return "none"; }
    if (VERDICTS.indexOf(this.verdict) >= 0) {
      var s = SUGGEST[this.verdict];
      return this.idkNow && RANK[s] > RANK.nearly ? "nearly" : s;
    }
    return this.idkNow ? "nearly" : null;
  };
  Engine.prototype.allowed = function (rating) {
    if (!this.revealed || RATINGS.indexOf(rating) < 0) { return false; }
    var cap = this.cap();
    return cap === null || (cap !== "none" && RANK[rating] <= RANK[cap]);
  };

  // The filled rating: the cap, and only when there is a verdict (after
  // "I don't know" with no verdict, Got it is greyed and nothing is filled).
  Engine.prototype.suggestion = function () {
    if (!this.revealed || VERDICTS.indexOf(this.verdict) < 0) { return null; }
    return this.cap();
  };

  Engine.prototype.rate = function (rating) {
    var c = this.current();
    if (!c || !this.allowed(rating)) { return; }
    var id = c.id;
    var suggested = this.suggestion();
    var cap = this.cap();
    this.acted += 1;
    this.event({ type: "rated", card: id, phase: this.stage, rating: rating,
                 via: suggested === rating ? "auto" : "tap" });
    c.last = rating; c.lastLocal = rating;
    if (rating === "got_it") { c.known = true; }
    this.pass[id] = { rating: rating, mine: this.mine, verdict: this.verdict === "pending" ? null : this.verdict, cap: cap };
    if (this.detour) {
      // A redo on a retry replaces that card's rating and goes back to the
      // card the queue was on. Rated below Got it it turns grey, but does
      // not join this pass's queue: a pass always ends.
      this.detour = null;
      this.show();
    } else {
      // A card met with "I don't know" comes round once more, at the end.
      if (this.idkNow && !this.replayed[id] && this.passIds.indexOf(id, this.idx + 1) < 0) {
        this.replayed[id] = true;
        this.passIds.push(id);
        // It comes round to be answered from memory: an empty box.
        delete this.drafts[id];
      }
      this.idx += 1;
      if (this.idx < this.passIds.length) { this.show(); } else { this.endPass(); }
    }
    this.flushSoon(600);
  };

  // ‹ Back: the previous card of this pass, in state A, with what the pupil
  // wrote last time already in the box. During a redo, back to the queue's
  // card with the green rating untouched. No event of its own.
  Engine.prototype.canBack = function () { return !this.ended && (!!this.detour || this.idx > 0); };
  Engine.prototype.back = function () {
    if (!this.canBack()) { return; }
    if (this.detour) { this.detour = null; this.show(); return; }
    this.idx -= 1;
    this.show();
  };

  // §13.1.11 — redo a green card on a retry pass, from state A of the
  // queue's card only.
  Engine.prototype.canRedo = function (id) {
    return !this.ended && !this.revealed && !this.learn && !this.detour &&
      !!this.pass[id] && this.pass[id].rating === "got_it";
  };
  Engine.prototype.redo = function (id) {
    if (!this.canRedo(id)) { return; }
    this.detour = id;
    this.show();
  };

  // Right in this pass, over the whole deck of the pass (`order`): green
  // cards carried into a Try again still count.
  Engine.prototype.right = function () {
    var self = this;
    return (this.order || []).filter(function (id) { return self.pass[id] && self.pass[id].rating === "got_it"; }).length;
  };

  // The end of a pass (§13.1.6–8).
  //   writing pass (make mode)  keeps the sitting open; its review follows.
  //   all right                 ends the sitting; Done.
  //   anything else             Try again, in the SAME sitting.
  Engine.prototype.endPass = function () {
    var writing = this.stage === "make";
    var right = this.right();
    var m = this.order.length;
    var all = !writing && right === m;
    this.ended = true;
    this.revealed = false;
    this.learn = false;
    this.detour = null;
    this.tok += 1;
    this.end = { right: right, m: m, writing: writing, all: all, settled: false };
    if (all) { this.sessionFinish(); }
    this.changed();
    this.flush();
  };

  Engine.prototype.sessionFinish = function () {
    this.event({ type: "session_finish" });
  };

  // Try again: only the cards that are not Got it, in the pass's own order.
  Engine.prototype.retry = function () {
    if (!this.ended || !this.end || this.end.all || this.end.writing) { return; }
    var self = this;
    this.retries += 1;
    Object.keys(this.pass).forEach(function (id) {
      if (self.pass[id].rating !== "got_it") { delete self.pass[id]; }
    });
    this.replayed = {};
    this.detour = null;
    this.passIds = this.order.filter(function (id) { return !self.pass[id]; });
    // A leftover is answered afresh: its wrong answer is not put back in
    // the box for the pupil to send again. (A green card's redo keeps its
    // earlier answer — §13.1.11.)
    this.passIds.forEach(function (id) { delete self.drafts[id]; });
    this.idx = 0;
    this.ended = false;
    this.end = null;
    this.tok += 1;
    this.show();
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
    var order = this.order || [];
    var m = order.length;
    var right = this.right();
    var here = this.ended ? null : (this.detour || (this.passIds || [])[this.idx]);
    var segs = order.map(function (id) {
      var e = self.pass[id];
      return { id: id, state: e ? (e.rating === "got_it" ? "right" : "answered") : "todo",
               current: id === here };
    });
    var chips = segs.map(function (g, i) {
      return { id: g.id, num: i + 1, state: g.state, current: g.current,
               redo: g.state === "right" && self.canRedo(g.id) };
    });
    var review = p === "review";
    var end = null;
    if (this.end) {
      var E = this.end;
      var ready = E.settled && !this.pending.length;
      var offline = E.all && !ready && this.error === "offline";
      var button = E.writing ? "again" : E.all ? "done" : "retry";
      end = {
        line1: E.right + " of " + E.m + " right",
        // Line 2 and the helper only on the all-right screen, and only once
        // the server has the pass (A8a); nothing else waits on the server.
        line2: E.all && ready ? (secured + " of " + n + " secured so far") : "",
        offline: offline,
        helper: E.all && ready && secured < n ? "Revise flashcards one more time" : "",
        button: button,
        buttonLabel: { done: "Done", again: "Revise flashcards one more time", retry: "Try again" }[button]
      };
    }
    var chip = this.revealed && this.verdict ? CHIP[this.verdict] : "";
    var allowed = {};
    RATINGS.forEach(function (r) { allowed[r] = self.allowed(r); });
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
      cap: this.cap(),
      allowed: allowed,
      learn: !!c && !!this.learn,
      learnAnswer: c && this.learn ? c.answer : "",
      retry: this.retries > 0,
      chips: chips,
      detour: !!this.detour,
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
    }, function (err) {
      self.sending = false;
      // §13.6 — the teacher deleted this set while it was open. Nothing
      // sent now can land, so stop trying and say so.
      if (err && err.message === "not_your_homework") {
        self.error = "gone";
        self.pending = [];
        save(self.id, []);
        self.changed();
        return;
      }
      // Kept on the device; retried with a longer wait. Idempotent ids mean a
      // batch that DID land but whose reply was lost is harmless to resend.
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
      var t = Api.transport;
      var known = engines[assignmentId];
      if (known) {
        // A pass that has ended starts afresh on reopening; one left
        // mid-way carries on where it was.
        var resume = function () {
          Api.active = known;
          if (known.ended) { known.opts.newSitting = true; known.start(null); }
          return known;
        };
        if (typeof t !== "function") { return Promise.resolve(resume()); }
        // ⊕ Sharpen §13.6 — ask the server first, even though the deck is
        // already on the device: the teacher may have deleted it since.
        // Offline, the device carries on as before.
        return Promise.resolve().then(function () { return t(assignmentId, []); }).then(function (state) {
          if (state) { known.merge(state); }
          return resume();
        }, function (err) {
          if (err && err.message === "not_your_homework") { delete engines[assignmentId]; throw err; }
          return resume();
        });
      }
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
