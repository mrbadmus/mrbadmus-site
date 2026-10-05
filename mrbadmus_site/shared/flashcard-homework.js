/* ⊕ MRB-351 — THE FLASHCARD HOMEWORK ENGINE.
 *
 * ⊕ THE PUPIL DECIDES (Mide, 5 Oct 2026) — THE RULE THAT STANDS NOW. This is
 * revision: the pupil is the judge, not the machine (the Anki / Brainscape /
 * Quizlet model). Top-set Year 11s typed right answers worded differently,
 * the check said "Nearly", and would not let them pick Secured.
 *
 *   · The pupil may still type an answer and the answer check still runs,
 *     but its verdict is only a HINT: the chip beside their answer (Right /
 *     Nearly / Wrong / No answer / Checking…). It never gates anything.
 *   · After every reveal Secured, Nearly and Not yet are ALL available —
 *     whatever the verdict, while it is still "Checking…", when the check is
 *     slow, failed or down, and after "I don't know". The pupil never waits
 *     for the check. Nothing is pre-filled.
 *   · The teacher still sees the truth: the typed answer, the verdict and the
 *     pupil's rating are all recorded exactly as before, side by side.
 *   · The revealed answer is always the deck's model answer; what the pupil
 *     typed only ever appears as "your answer" beside it.
 *   SUPERSEDES: the 29 Sep "THE VERDICT CAPS THE RATING" bullet below, the
 *   2 Oct line that a card nothing could check "may never be Secured", the
 *   4 Oct "Secured means checked" (option B) rule, and the cap at Nearly
 *   after "I don't know". They are kept below as history, not as behaviour.
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
 *     C  verdict: chip Right / Nearly / Wrong / No answer as a hint only;
 *        all three ratings stay open, nothing filled (5 Oct)
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
 *   · [SUPERSEDED 5 Oct 2026 — the pupil decides] THE VERDICT CAPS THE RATING. Right → up to Got it, Nearly → up to
 *     Nearly, Wrong / No answer → Not yet only. Enforced here, in `rate()`,
 *     so the buttons, keys 1·2·3 and the swipe all obey it. While the check
 *     is out ("Checking…") nothing can be rated; no verdict → no cap.
 *   · "I DON'T KNOW" IS A LEARNING STEP. The card stays on its question,
 *     the model answer shows under it, and the pupil writes it in their own
 *     words; that answer is checked (hint only, no cap since 5 Oct). The card comes round
 *     once more at the end of the pass as a plain card.
 *   · A PASS THAT IS NOT ALL RIGHT ENDS ON "Try again", which replays only
 *     the cards that are not Got it, in the pass's own order, in the SAME
 *     server sitting (no `session_finish`). On that retry the bar becomes
 *     numbered chips; a green one can be tapped to redo that card (a
 *     "detour") without leaving the queue.
 *   · A PASS THAT IS ALL RIGHT ends the sitting (`session_finish`) and
 *     offers one button, Done. × still ends the sitting (A13).
 *
 * ⊕ STAGE D (29 Sep 2026 — docs/mrb351/STAGE-D-PLAN.md §1 decision 5 wins
 *   over everything above about where a reopened deck lands).
 *
 *   PROGRESS IS NEVER LOST. Every answer and every rating is sent the
 *   moment it happens, and kept on the device until the server has it. When
 *   the pupil comes back — after ×, a reload, a phone that died, or on
 *   another device — they land on the next card they have not done, with
 *   the count they had. What "the pass they were on" means is worked out
 *   from their own ratings on the server (`reconstruct`), not from the
 *   server's sitting, which still closes on × and after ten quiet minutes
 *   exactly as before (the teacher's numbers do not move).
 *
 *   A pass ENDS when every card is Got it, or when its round is finished
 *   and nothing more happens for an hour. A finished round that is not all
 *   right shows Try again when they come back inside that hour, and starts
 *   a fresh pass after it. Half-typed answers are kept on the device.
 *
 *   events: card_shown, answer_submitted, revealed, rated, session_finish,
 *   visibility — each with a client-generated id, the device clock and
 *   whether the tab was visible. They are queued on the DEVICE (so a flaky
 *   connection or a closed tab loses nothing), sent in batches, and are
 *   idempotent on the server by id. The SERVER computes every duration.
 *
 * ⊕ MRB-354 (Mide, 2 Oct 2026 — "Students need to be able to do flashcards
 *   and move on … probably has that knowledge secured already"). SECURED,
 *   DONE AND FINISH ARE REWRITTEN, and the ENGINE now decides all three
 *   itself — it no longer waits on the server for any of them.
 *
 *   secured(card) = exists a rating of it, latest per (card, session, phase)
 *   — the SAME grouping ‹ Back already used within one sitting — that is
 *   got_it. Make phase or review phase, any sitting, no pairing, no hour
 *   gap, completion_rule ignored. ⊕ Mide, 4 Oct 2026: once secured, stays
 *   secured — no later rating (‹ Back, a redo, a Revise pass, another tab)
 *   ever un-secures a card; it is kept as history ("Later tries").
 *   done = the deck has ≥1 card and every card is secured. finish = for
 *   each card, the earliest counting got_it row; the deck's finish is the
 *   MAX of those (the moment the LAST card secured) — `finishedAt()` below.
 *
 *   `securedMap()`/`securedCount()`/`allSecured()` compute this from TWO
 *   layers: `historicalSecured` (this pupil's own `flashcard_reviews`, read
 *   once per resume/reopen — see `resumeFor()`) plus `liveSecured` (cards
 *   rated got_it since then). A deck already
 *   fully secured when opened goes straight to the Done screen — see the
 *   short-circuit at the top of `start()` — never a fresh pass. A pass that
 *   is not all secured ends on Try again, replaying the cards still not
 *   secured (never merely "not Got it in this pass"): a card secured
 *   earlier stays secured and is never replayed. `finishedAt()` no longer
 *   shares `walkReview`'s round-aware walk — that walk still decides WHERE
 *   a reopened pass lands (`reconstruct()`, unchanged) — because there is
 *   no round or pass to reconstruct for "is every card secured"; it is a
 *   flat fact over the pupil's whole history.
 *
 *   NEVER READ `state.secured`/`state.known`/`state.n` FOR PUPIL DISPLAY —
 *   those are the server's, and the server still computes the OLD
 *   two-sitting rule until the parked SQL lands. This file's own secured/
 *   finishedAt are the pupil-facing truth either way.
 *
 * Transport, the keepalive transport, the model check and the resume read
 * are injected (`MRBHomework.transport` / `.transportKeepalive` /
 * `.modelCheck` / `.resumeRead`) so the fixture
 * page and the Node tests run it with no network at all.
 */
(function (root) {
  "use strict";

  var STORE = "mrbadmusai.fchw.v1.";
  var FLUSH_MS = 2500;
  var MODEL_WAIT_MS = 4000;
  var HOUR = 60 * 60 * 1000;          // a finished round, then this long quiet → a new pass
  var IDK_SLACK = 5 * 60 * 1000;      // device clock vs the first rating of the pass
  var DRAFT_MS = 300;
  var BEACON_MAX = 60;                // events per keepalive request (64 KB budget)
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
  // ⊕ Sharpen review (Fable, S-c) — which cards met "I don't know" in this
  // pass, and which have had their replay: kept on the device, so a reload
  // keeps the replay. ⊕ Stage D: honoured beside any
  // reconstructed pass (decision 8), for the round it was written in (`n`)
  // and not from before the pass began (`at` vs the pass's first rating).
  function loadIdk(key) {
    try {
      var v = JSON.parse(root.localStorage.getItem(STORE + "idk." + key) || "null");
      return v && v.seen ? v : null;
    } catch (e) { return null; }
  }
  function saveIdk(key, seen, done, n) {
    try {
      root.localStorage.setItem(STORE + "idk." + key,
        JSON.stringify({ at: Date.now(), n: n || 1, seen: seen || {}, done: done || {} }));
    } catch (e) { /* private mode */ }
  }
  // ⊕ Stage D (decision 4) — half-typed answers, per card, on the device, so
  // a reload mid-sentence keeps the words. A card's entry goes when it is
  // rated.
  function loadDrafts(key) {
    try {
      var v = JSON.parse(root.localStorage.getItem(STORE + "draft." + key) || "null");
      return v && typeof v === "object" ? v : {};
    } catch (e) { return {}; }
  }
  function saveDrafts(key, map) {
    try {
      if (Object.keys(map).length) { root.localStorage.setItem(STORE + "draft." + key, JSON.stringify(map)); }
      else { root.localStorage.removeItem(STORE + "draft." + key); }
    } catch (e) { /* private mode */ }
  }

  // ── the no-model answer check: an EXACT port of SQL flashcard_quick_check
  // (supabase/migrations/20260924180100_mrb351_flashcards_functions.sql; the
  // one-word rule below is Prompt Y's, 20261004120000_y_quick_check_key_word
  // .sql, parked on feat/y-migrations until it is applied to production).
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
    // ⊕ Prompt Y (4 Oct 2026) — ONE WORD is Right here only when it IS the
    // model answer's one key word (function words and one- or two-character
    // symbols like "J", "N", "kg" aside): "joules" for "Joules (J)". It used
    // to be Right when it was ANY word of the model answer, so "energy"
    // secured "The minimum amount of energy needed for particles to react".
    // Every other one-word answer goes to the answer check, which judges it.
    if (pa.indexOf(" ") < 0) {
      var key = ma.split(" ").filter(function (w) { return w.length > 2 && FUNCTION_WORDS.indexOf(w) < 0; });
      return key.length && key.join(" ") === pa ? "match" : null;
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

  // ── ⊕ STAGE D: where a reopened deck lands (decision 5) ──────────────
  //
  // `rows`  the pupil's own flashcard_reviews for this assignment, oldest
  //         first: {card_id, rating, phase, rated_at}. Kept in the order
  //         given (the read orders by rated_at, id).
  // `cards` the deck (state.cards: id, position, last, secured).
  // `idk`   optional: this device's "I don't know" record ({seen: {id}}) —
  //         a replay's rating straight after its round finished belongs to
  //         that round, not to a new one.
  // Returns null for "start a fresh pass", or
  //   { stage, pass: {id: {rating, phase}}, order: [id], since: ms|null,
  //     round: {n, targets: [id], done: [id]}, ended: null|"retry" }.
  function ms(v) {
    if (typeof v === "number") { return v; }
    var n = Date.parse(v);
    return isNaN(n) ? 0 : n;
  }
  // ── THE ROUND-AWARE WALK (⊕ MUST-FIX, review 1 Oct 2026) ─────────────
  //
  // ONE walker behind both `reconstruct()` (what pass the pupil is in NOW)
  // and `finishedAt()` (the first time any pass they were in ended all
  // Right — the Done screen moment). Mirroring this by hand in two places
  // is exactly how the two drifted: a first `finishedAt`, written as a
  // simple cumulative "every card's latest rating is Got it" check with no
  // reset, agreed with `reconstruct` on every scenario this file's own
  // tests tried — until a pupil left a leftovers round stale for an hour,
  // came back to a FRESH pass (the engine re-asks the whole deck; see
  // `rankedIds`), and got the weak card right FIRST. `reconstruct` rightly
  // shows them 1 of 5 rated; the old `finishedAt`, never resetting, still
  // saw every card's all-time-latest rating as Got it and called it
  // finished. That is wrong in the direction that matters: it stamps a
  // pupil done, permanently, while they are mid-pass.
  //
  // `list` is already filtered to the rows this walk should see (review-
  // phase ratings for this deck, in order — see each caller for how make
  // mode's writing pass is excluded first). Returns the walk's ending
  // state (`latest`/`first`/`targets`/`done`/`count`/`n`/`complete`/
  // `since`/`lastAt` — exactly what `reconstruct`'s step 3 used to read off
  // its own locals) PLUS `firstFinish`: `{at, card, event_id}` | `null`,
  // the FIRST row anywhere in the walk at which `allRight()` held — i.e.
  // the pass showing at that instant reached the Done screen. Once set it
  // is never replaced: finishing stays finished, whatever happens later
  // (`finishedAt`'s own contract — a later rating or a stale gap can move
  // `reconstruct` on to a new pass without ever un-finishing the pupil).
  function walkReview(list, deck, idk) {
    var seen = (idk && idk.seen) || {};
    // The record is this device's, for ONE round of ONE pass (`n`, `at`) —
    // start() applies the same two tests before honouring it. Without them a
    // record left by an earlier pass on this device would fold another
    // device's round-2 rating of that card back into round 1.
    var idkN = (idk && idk.n) || 1, idkAt = (idk && idk.at) || 0;
    var latest, first, targets, done, count, n, complete, since, lastAt = 0, firstFinish = null;
    function reset() {
      latest = {}; first = []; targets = deck.slice(); done = {}; count = {}; n = 1; complete = false; since = null;
    }
    function allRight() {
      return deck.every(function (id) { return latest[id] && latest[id].rating === "got_it"; });
    }
    function finish(r) {
      if (!firstFinish) { firstFinish = { at: r.at, card: r.card, event_id: r.event_id }; }
      reset();
    }
    reset();
    list.forEach(function (r) {
      if (complete) {
        if (r.at - lastAt >= HOUR) {
          reset();
        } else if (seen[r.card] && count[r.card] === 1 && targets.indexOf(r.card) >= 0 &&
                   idkN === n && (!idkAt || since === null || idkAt >= since - IDK_SLACK)) {
          // an "I don't know" replay: the last showing of the round it
          // belongs to. The round stays finished.
          latest[r.card] = { rating: r.rating, phase: "review" };
          count[r.card] += 1;
          lastAt = r.at;
          if (allRight()) { finish(r); }
          return;
        } else {
          targets = deck.filter(function (id) { return !latest[id] || latest[id].rating !== "got_it"; });
          done = {}; count = {}; n += 1; complete = false;
        }
      }
      if (since === null) { since = r.at; }
      if (!latest[r.card]) { first.push(r.card); }
      latest[r.card] = { rating: r.rating, phase: "review" };
      count[r.card] = (count[r.card] || 0) + 1;
      if (targets.indexOf(r.card) >= 0) { done[r.card] = true; }
      lastAt = r.at;
      if (allRight()) { finish(r); return; }
      if (targets.every(function (id) { return done[id]; })) { complete = true; }
    });
    return { latest: latest, first: first, targets: targets, done: done, count: count,
             n: n, complete: complete, since: since, lastAt: lastAt, firstFinish: firstFinish };
  }

  function reconstruct(rows, cards, mode, now, idk) {
    if (!rows || !cards || !cards.length) { return null; }
    var deck = cards.slice().sort(function (a, b) { return a.position - b.position; })
      .map(function (c) { return c.id; });
    var inDeck = {};
    deck.forEach(function (id) { inDeck[id] = true; });
    var list = [];
    rows.forEach(function (r) {
      if (!r || !inDeck[r.card_id] || !(r.rating in RANK)) { return; }
      list.push({ card: r.card_id, rating: r.rating, phase: r.phase === "make" ? "make" : "review", at: ms(r.rated_at) });
    });

    // 1 · make mode's writing pass: every card rated once in the make phase.
    if (mode === "make") {
      var mk = {}, mkSince = null;
      list.forEach(function (r) {
        if (r.phase !== "make") { return; }
        if (mkSince === null) { mkSince = r.at; }
        mk[r.card] = { rating: r.rating, phase: "make" };
      });
      if (deck.some(function (id) { return !mk[id]; })) {
        return { stage: "make", pass: mk, order: deck.slice(), since: mkSince, ended: null,
                 round: { n: 1, targets: deck.slice(), done: deck.filter(function (id) { return mk[id]; }) } };
      }
    }

    // 2 · walk the review ratings — the shared walker, above.
    var w = walkReview(list.filter(function (r) { return r.phase === "review"; }), deck, idk);
    var latest = w.latest, first = w.first, targets = w.targets, done = w.done,
        n = w.n, complete = w.complete, since = w.since, lastAt = w.lastAt;

    // 3 · what is left open.
    var ended = null;
    if (!first.length) {
      if (mode !== "make") { return null; }
      var fresh = rankedIds(cards);
      return { stage: "review", pass: {}, order: fresh, since: null, ended: null,
               round: { n: 1, targets: fresh.slice(), done: [] } };
    }
    if (complete) {
      if ((now || Date.now()) - lastAt >= HOUR) { return null; }
      ended = "retry";
    }
    var order = first.concat(rankedIds(cards).filter(function (id) { return first.indexOf(id) < 0; }));
    var pass = {};
    Object.keys(latest).forEach(function (id) {
      // mid-retry, a card still to be redone in this round is "to come",
      // not "answered" — exactly as retry() leaves it.
      if (n > 1 && !ended && targets.indexOf(id) >= 0 && !done[id]) { return; }
      pass[id] = latest[id];
    });
    return {
      stage: "review", pass: pass, order: order, since: since, ended: ended,
      round: { n: n,
               targets: order.filter(function (id) { return targets.indexOf(id) >= 0; }),
               done: order.filter(function (id) { return done[id]; }) }
    };
  }

  // ── SECURED — once secured, stays secured (Mide, 4 Oct 2026) ──────────
  //
  // "Once secured, stays secured. It also helps with students not losing
  // motivation." secured(card) = the card has EVER been rated got_it, in any
  // sitting, any phase. A later lower rating — ‹ Back onto a secured card, a
  // Revise pass after Done, another tab — is kept as history ("Later tries")
  // and never takes the card back. (MRB-354, 2 Oct, had let the latest rating
  // in the SAME sitting win, so ‹ Back and a wrong answer un-secured it.)
  // The same rule as `flashcard_card_state`'s `known`
  // (supabase/migrations/20261004180000_y2_secured_stays_secured.sql).
  //
  // `rows`: the pupil's own flashcard_reviews, any order —
  // {card_id, rating, rated_at, event_id|id}. Returns
  // {secured: {card_id: true}, finishAt: {card_id: {at, event_id}}} —
  // `finishAt[card]` is that card's EARLIEST got_it, which is what
  // `finishedAt()` below needs: the deck's finish is the MAX of these, the
  // moment the LAST card secured.
  function securedInfo(rows, cards) {
    var inDeck = {};
    (cards || []).forEach(function (c) { inDeck[c.id] = true; });
    var secured = {}, finishAt = {};
    (rows || []).forEach(function (r) {
      if (!r || !inDeck[r.card_id] || r.rating !== "got_it") { return; }
      var at = ms(r.rated_at), best = finishAt[r.card_id];
      secured[r.card_id] = true;
      if (!best || at < best.at) { finishAt[r.card_id] = { at: at, event_id: r.event_id || r.id || null }; }
    });
    return { secured: secured, finishAt: finishAt };
  }

  // ⊕ MRB-354 (2 Oct 2026; superseded the 1 Oct round-aware-walk version) —
  // "finished the homework" = done = every card secured (above), read from
  // data with no live Engine. finish = the MAX over cards of each card's
  // EARLIEST counting got_it row — the moment the LAST card became secured.
  // No round, no hour gap, no make-phase gating: a card secured during the
  // WRITING pass alone is already secured, so a deck can finish without a
  // review pass ever running. This is now a FLAT fact over the pupil's whole
  // history, not a replay of `reconstruct()`'s pass-shaped walk — `mode`/
  // `idk` are no longer needed and are accepted-but-ignored so existing call
  // sites (`student-live.js`'s `recordFinish`/heal) need no change.
  // `rows`: oldest first, {card_id, rating, phase, session_id, rated_at,
  // event_id|id}. Returns {at, event_id} | null.
  function finishedAt(rows, cards /* , mode, idk — ignored, kept for callers */) {
    if (!rows || !cards || !cards.length) { return null; }
    var info = securedInfo(rows, cards);
    var best = null;
    for (var i = 0; i < cards.length; i++) {
      var f = info.finishAt[cards[i].id];
      if (!f) { return null; }   // not every card secured yet
      if (!best || f.at > best.at) { best = f; }
    }
    return best;
  }

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
    // SECURED, built once from the pupil's own rows at the last resume /
    // reopen (`historicalSecured`, frozen — see `resumeFor()`), plus every
    // card rated got_it since (`liveSecured`). Both only ever grow: once
    // secured, stays secured (Mide, 4 Oct 2026).
    this.historicalSecured = {};
    if (this.opts.secured) {
      var self0 = this;
      Object.keys(this.opts.secured).forEach(function (id) {
        if (self0.opts.secured[id]) { self0.historicalSecured[id] = true; }
      });
    }
    this.liveSecured = {};    // cards rated got_it since the last read — once secured, stays
    this.liveSessionN = 0;
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

  // THE DISPLAY TRUTH FOR SECURED: secured at the last read of the pupil's
  // own rows (`historicalSecured`), or rated got_it since (`liveSecured`).
  // Never lowered.
  Engine.prototype.securedMap = function () {
    var self = this;
    var out = {};
    this.cards.forEach(function (c) {
      out[c.id] = !!(self.historicalSecured[c.id] || self.liveSecured[c.id]);
    });
    return out;
  };
  Engine.prototype.securedCount = function () {
    var m = this.securedMap(), n = 0;
    this.cards.forEach(function (c) { if (m[c.id]) { n += 1; } });
    return n;
  };
  Engine.prototype.allSecured = function () {
    return this.cards.length > 0 && this.securedCount() === this.cards.length;
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
  function rankedIds(cards) {
    var cs = (cards || []).slice();
    cs.sort(function (a, b) {
      var oa = rank(a), ob = rank(b);
      return oa !== ob ? oa - ob : a.position - b.position;
    });
    return cs.map(function (c) { return c.id; });
  }
  Engine.prototype.ranked = function () { return rankedIds(this.cards); };
  Engine.prototype.byPosition = function (ids) {
    var self = this;
    return ids.filter(function (id) { return self.byId[id]; })
      .sort(function (a, b) { return self.byId[a].position - self.byId[b].position; });
  };

  // A pass. `resume` is `reconstruct()`'s answer (null = a fresh pass): the
  // stage, the pass's ratings and order, and the round it is on.
  // `freshSecured`, when given (a reused engine re-resuming — `Api.open()`),
  // is secured-per-card computed from a fresh server read; it can only ADD
  // to `historicalSecured`, never remove (secured never un-secures). ⊕
  // MRB-354 — if, taking that into account, the WHOLE deck is already
  // secured, this is the Done screen, full stop — never a fresh pass, and
  // never the `resume` a stale per-pass reconstruction might otherwise ask
  // for. The one way PAST this shortcut is `again()`'s own "Revise flashcards
  // one more time", which sets `forceRevise` for the one `start()` call it
  // makes.
  Engine.prototype.start = function (resume, freshSecured) {
    var self = this;
    if (freshSecured) {
      Object.keys(freshSecured).forEach(function (id) {
        if (freshSecured[id]) { self.historicalSecured[id] = true; }
      });
    }
    if (!this.forceRevise && this.cards.length && this.allSecured()) {
      this.pass = {}; this.retries = 0; this.replayed = {}; this.idkSeen = {}; this.replayDone = {};
      this.detour = null; this.learn = false; this.idkNow = false;
      this.saved = {}; this.drafts = {};
      this.stage = "review";
      this.order = this.ranked();
      this.passIds = []; this.baseLen = 0; this.idx = 0; this.frontier = 0;
      this.endAllSecured();
      return;
    }
    var R = resume || null;
    this.ended = false;
    this.end = null;
    this.pass = {};
    this.retries = 0;          // Try again rounds in this pass
    this.replayed = {};        // cards an "I don't know" sent round again
    this.idkSeen = {};         // cards met with "I don't know" this round
    this.replayDone = {};      // …whose replay has been rated
    this.detour = null;        // a green card being redone on a retry
    this.learn = false;        // "I don't know": the own-words step
    this.idkNow = false;       // this showing of the card began with it
    // Half-typed text from the device (decision 4).
    this.saved = {};
    var kept0 = loadDrafts(this.id);
    Object.keys(kept0).forEach(function (id) {
      if (self.byId[id] && typeof kept0[id] === "string" && kept0[id]) { self.saved[id] = kept0[id].slice(0, 500); }
    });
    this.drafts = {};
    Object.keys(this.saved).forEach(function (id) { self.drafts[id] = self.saved[id]; });
    var mode = this.state && this.state.mode;
    var done = [];
    if (R) {
      this.stage = R.stage === "make" ? "make" : "review";
      var order = (R.order || []).filter(function (id) { return self.byId[id]; });
      var tset = {}, dset = {};
      (R.round.targets || []).forEach(function (id) { tset[id] = true; });
      (R.round.done || []).forEach(function (id) { dset[id] = true; });
      Object.keys(R.pass || {}).forEach(function (id) {
        if (self.byId[id]) { self.pass[id] = { rating: R.pass[id].rating, mine: null, verdict: null, cap: null }; }
      });
      if (R.round.n > 1) {
        // a Try again round: the chips view, on the cards still to redo.
        this.retries = R.round.n - 1;
        this.passIds = order.filter(function (id) { return tset[id] && !dset[id]; });
      } else {
        done = order.filter(function (id) { return dset[id]; });
        this.passIds = done.concat(order.filter(function (id) { return !dset[id]; }));
      }
      this.order = order;
      // decision 7 — a card MADE but not rated (the phone died between the
      // two) reopens with its stored answer in the box.
      if (this.stage === "make") {
        this.cards.forEach(function (c) {
          if (c.made && !self.pass[c.id] && c.mine && c.mine !== IDK_TEXT && !self.drafts[c.id]) {
            self.drafts[c.id] = c.mine;
          }
        });
      }
    } else if (mode === "make" && this.unmade().length) {
      this.stage = "make";
      this.passIds = this.unmade().map(function (c) { return c.id; });
      this.order = this.passIds.slice();
    } else {
      this.stage = "review";
      this.passIds = this.ranked();
      this.order = this.passIds.slice();
    }
    this.baseLen = this.passIds.length;
    // "I don't know" cards of this round, kept on the device: an unrated
    // one opens in the learn state again (show()), a rated one still gets
    // its replay.
    var kept = R ? loadIdk(this.id) : null;
    if (kept && (kept.n || 1) === R.round.n &&
        (R.since == null || (kept.at || 0) >= R.since - IDK_SLACK)) {
      this.idkSeen = kept.seen || {};
      this.replayDone = kept.done || {};
      Object.keys(this.idkSeen).forEach(function (id) {
        if (self.pass[id] && !self.replayDone[id] && self.byId[id] && self.passIds.indexOf(id, done.length) < 0) {
          self.replayed[id] = true;
          self.passIds.push(id);
        }
      });
    }
    this.keepIdk();
    this.idx = R && R.round.n > 1 ? 0 : done.length;
    this.frontier = this.idx;   // ⊕ MRB-354 — Forward never goes past this
    if (this.idx >= this.passIds.length && (this.passIds.length || (R && R.ended))) { this.endPass(); return; }
    this.show();
  };

  // ⊕ MRB-354 — the short-circuit path from `start()`: every card already
  // secured, so there is no pass to show at all. No `sessionFinish()` (there
  // is nothing new to close out), but `flush()` below still settles the end
  // screen and fires `Api.onFinish` if nothing is pending — the heal path
  // for a pupil whose finish the server has not yet caught up to.
  Engine.prototype.endAllSecured = function () {
    this.ended = true;
    this.revealed = false;
    this.learn = false;
    this.detour = null;
    this.tok += 1;
    var total = this.cards.length;
    this.end = { securedCount: total, total: total, writing: false, all: true, settled: false, finished: true };
    this.changed();
    this.flush();
  };

  Engine.prototype.keepIdk = function () {
    saveIdk(this.id, this.idkSeen, this.replayDone, this.retries + 1);
  };

  // The device copy of the half-typed answers: soon after typing, at once
  // when a card is rated or the page is going away.
  Engine.prototype.keepDrafts = function (now) {
    var self = this;
    if (this.draftTimer) { clearTimeout(this.draftTimer); this.draftTimer = null; }
    if (now) { saveDrafts(this.id, this.saved); return; }
    this.draftTimer = setTimeout(function () { self.draftTimer = null; saveDrafts(self.id, self.saved); }, DRAFT_MS);
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
    // ⊕ Sharpen review (Fable, M-1) — a card met with "I don't know" and not
    // yet rated in this pass (‹ Back then forward again, or a reload) opens
    // in the learn state again: the replay still applies.
    if (c && !this.detour && this.idkSeen[c.id] && !this.pass[c.id]) {
      this.learn = true;
      this.idkNow = true;
    }
    if (c) {
      this.event({ type: "card_shown", card: c.id, phase: this.stage });
    }
    this.changed();
  };

  // ── pupil actions ────────────────────────────────────────────────────
  Engine.prototype.setDraft = function (text) {
    this.draft = String(text == null ? "" : text).slice(0, 500);
    var c = this.current();
    if (c && !this.revealed) {
      this.drafts[c.id] = this.draft;
      if (/\S/.test(this.draft)) { this.saved[c.id] = this.draft; } else { delete this.saved[c.id]; }
      this.keepDrafts(false);
    }
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
    // Answered, not yet rated: a reopen puts this answer back in the box.
    if (extra && extra.idk) { delete this.saved[c.id]; } else { this.saved[c.id] = answer; }
    this.keepDrafts(true);
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
    this.flush();                          // ⊕ Stage D: sent now, not in 400 ms
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
    this.idkSeen[c.id] = true;
    this.keepIdk();
    this.mine = IDK_TEXT;
    this.draft = "";
    this.drafts[c.id] = "";
    delete this.saved[c.id];
    this.keepDrafts(true);
    this.changed();
    this.flush();                          // ⊕ Stage D: sent now
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
    // ⊕ Mide, 4 Oct 2026 (option B) — ONE quiet retry before giving up, so a
    // single slow or failed reply doesn't cost the pupil: a second attempt,
    // the pupil still seeing "Checking…". A late reply to EITHER attempt
    // still lands (the edge function answers a repeat of the same text from
    // the verdict it stored for the first, without asking the model again).
    // Only when both come back empty does the card go unchecked (no chip).
    // ⊕ 5 Oct 2026: the pupil never waits for any of this to rate.
    var tries = 0;
    function attempt() {
      tries += 1;
      var mine = tries, done = false;
      function fail() {
        if (done || settled) { return; }
        done = true;
        if (mine < 2) { attempt(); } else { land(null); }
      }
      setTimeout(fail, Api.modelWaitMs || MODEL_WAIT_MS);
      Promise.resolve().then(function () { return Api.modelCheck(self.id, c.id, answer, self); })
        .then(function (v) {
          if (VERDICTS.indexOf(v) >= 0) { done = true; land(v); } else { fail(); }
        }, fail);
    }
    attempt();
  };

  // ⊕ Mide, 5 Oct 2026 — THE PUPIL DECIDES. Once the answer is showing, ALL
  // THREE ratings are allowed, always: whatever the verdict, while it is
  // still "Checking…", when the check was slow, failed or is down, and after
  // "I don't know". The verdict is a HINT (the chip), never a gate. Nothing
  // is pre-filled either: a filled button would be a verdict-shaped nudge,
  // and the least surprising screen is three equal buttons the pupil picks
  // from. (`cap()` is kept as the one place that says so; it is no longer a
  // ceiling. It replaces the 29 Sep verdict cap and the 4 Oct "no verdict
  // caps at Nearly" rule, and the old after-"I don't know" cap at Nearly.)
  Engine.prototype.cap = function () {
    return this.revealed ? "got_it" : null;
  };
  Engine.prototype.allowed = function (rating) {
    return !!this.revealed && RATINGS.indexOf(rating) >= 0;
  };

  // Nothing is filled for the pupil (see above).
  Engine.prototype.suggestion = function () { return null; };

  Engine.prototype.rate = function (rating) {
    var c = this.current();
    if (!c || !this.allowed(rating)) { return; }
    var id = c.id;
    this.acted += 1;
    this.event({ type: "rated", card: id, phase: this.stage, rating: rating, via: "tap" });
    c.last = rating; c.lastLocal = rating;
    if (rating === "got_it") { c.known = true; }
    this.pass[id] = { rating: rating, mine: this.mine, verdict: this.verdict === "pending" ? null : this.verdict, cap: null };
    // Once secured, stays secured (Mide, 4 Oct 2026): a got_it here secures
    // the card for good; a later lower rating is history, never a downgrade.
    if (rating === "got_it") { this.liveSecured[id] = true; }
    delete this.saved[id];
    this.keepDrafts(true);
    if (!this.detour && this.idx >= this.baseLen && this.idkSeen[id]) {
      this.replayDone[id] = true;       // this rating IS the replay's
      this.keepIdk();
    }
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
        this.keepIdk();
      }
      this.idx += 1;
      if (this.idx > this.frontier) { this.frontier = this.idx; }   // ⊕ MRB-354
      if (this.idx < this.passIds.length) { this.show(); } else { this.endPass(); }
    }
    this.flush();                          // ⊕ Stage D: durable the moment it happens
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

  // ⊕ MRB-354 — Forward ›: beside ‹ Back. Walks back UP toward the card the
  // pupil was on (`frontier`, the furthest this pass has reached), one card
  // per press, changing no rating — it is a pure cursor move, never a
  // re-rate. Hidden once already at the frontier (the newest card). Never
  // offered during a retry's redo detour (there is no "forward" from a side
  // trip; ‹ Back already exits it).
  Engine.prototype.canForward = function () {
    return !this.ended && !this.detour && this.idx < this.frontier;
  };
  Engine.prototype.forward = function () {
    if (!this.canForward()) { return; }
    this.idx += 1;
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

  // The end of a pass (⊕ MRB-354 rewrite of §13.1.6–8: ONE rule now, for
  // BOTH the writing pass and the review pass — "Make mode's writing pass
  // end screen follows the SAME rule").
  //   every card secured   ends the sitting; Done (+ the quieter "Revise
  //                         flashcards one more time" secondary — see
  //                         `again()`).
  //   anything else         Try again, in the SAME sitting, on the cards
  //                         still not secured (never merely "not Got it in
  //                         this pass": a card secured earlier is never
  //                         replayed — see `retry()`).
  Engine.prototype.endPass = function () {
    var writing = this.stage === "make";
    var securedCount = this.securedCount(), total = this.cards.length;
    var all = total > 0 && securedCount === total;
    this.ended = true;
    this.revealed = false;
    this.learn = false;
    this.detour = null;
    this.tok += 1;
    this.end = { securedCount: securedCount, total: total, writing: writing, all: all, settled: false, finished: all };
    if (all) { this.sessionFinish(); }
    this.changed();
    this.flush();
  };

  Engine.prototype.sessionFinish = function () {
    this.event({ type: "session_finish" });
    this.liveSessionN += 1;   // ⊕ MRB-354 — the NEXT rating starts a fresh sitting's group
  };

  // ⊕ 1 Oct 2026 — the end screen settles once the server has the pass
  // (flush has nothing left queued). The FIRST time it settles for a
  // finished pass, tell the page so it can write the submission at once
  // (`student-live.js`'s `recordFinish`, the same write the heal makes on
  // every class-page load). Fires once per pass: `settled` guards it, and a
  // new pass gets a new `this.end` object.
  Engine.prototype.settleEnd = function () {
    if (!this.end || this.end.settled) { return; }
    if (this.end.finished && typeof Api.onFinish === "function") {
      try { Api.onFinish(this.id); } catch (e) { /* fire and forget; the heal covers it */ }
    }
    this.end.settled = true;
  };

  // Try again (⊕ MRB-354): only the cards that are NOT SECURED — never
  // merely "not Got it in this pass". A card secured earlier (this sitting
  // or an older one) stays out of the queue even if it happens to sit in
  // `this.pass` with a lower rating from a stage this engine re-asked it at.
  Engine.prototype.retry = function () {
    if (!this.ended || !this.end || this.end.all) { return; }
    var self = this;
    this.retries += 1;
    var secured = this.securedMap();
    Object.keys(this.pass).forEach(function (id) {
      if (!secured[id]) { delete self.pass[id]; }
    });
    this.replayed = {};
    this.idkSeen = {};
    this.replayDone = {};
    this.keepIdk();
    this.detour = null;
    this.passIds = this.order.filter(function (id) { return !secured[id]; });
    // A leftover is answered afresh: its wrong answer is not put back in
    // the box for the pupil to send again. (A green card's redo keeps its
    // earlier answer — §13.1.11.)
    this.passIds.forEach(function (id) { delete self.drafts[id]; delete self.saved[id]; });
    this.keepDrafts(true);
    this.baseLen = this.passIds.length;
    this.idx = 0;
    this.frontier = 0;   // ⊕ MRB-354
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

  // ⊕ MRB-354 — the quieter secondary offered beside Done once everything is
  // secured: "Revise flashcards one more time". It never un-secures anything
  // and never un-does the homework (secured is a one-way OR over every
  // sitting a card has ever had a got_it rating in — nothing this fresh pass
  // rates can remove that). `forceRevise` is the one way past `start()`'s
  // own all-secured shortcut, which would otherwise re-show the same Done
  // screen the pupil just asked to get past.
  Engine.prototype.again = function () {
    this.forceRevise = true;
    this.start(null);
    this.forceRevise = false;
  };

  Engine.prototype.visibility = function () {
    this.event({ type: "visibility" });
    if (!visibleNow()) { this.flushBeacon(); }
  };

  // ⊕ Stage D (decision 4) — the page is going away (pagehide, or hidden:
  // a phone locked or switched away from, which may be the last thing it
  // ever does). A plain fetch may be cancelled on unload; a `keepalive`
  // one is not. The events STAY queued — the reply is never awaited — and
  // the next send repeats them; the server keeps one row per event id.
  Engine.prototype.flushBeacon = function () {
    this.keepDrafts(true);
    var k = Api.transportKeepalive;
    if (this.pending.length && typeof k === "function") {
      try { k(this.id, this.pending.slice(0, BEACON_MAX)); } catch (e) { /* the queue is still on the device */ }
      return;
    }
    this.flush();
  };

  // ── what the overlay draws ───────────────────────────────────────────
  Engine.prototype.view = function () {
    var self = this;
    var s = this.state || {};
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
    var end = null;
    if (this.end) {
      var E = this.end;
      // ⊕ MRB-354 — ONE line, "N of M secured", computed by this engine from
      // the pupil's own rows plus this sitting's live ratings; it never
      // waits on the server (no `ready` gate: `securedCount`/`total` are
      // already the display truth the instant the pass ends). Not all
      // secured → ONE button, Try again. All secured → Done, plus the
      // quieter "Revise flashcards one more time" secondary (`end.secondary`
      // — the template shows it alongside Done, never on its own).
      var button = E.all ? "done" : "retry";
      end = {
        line1: E.securedCount + " of " + E.total + " secured",
        offline: this.error === "offline",
        secondary: E.all,
        button: button,
        buttonLabel: { done: "Done", retry: "Try again" }[button]
      };
    }
    var chip = this.revealed && this.verdict ? CHIP[this.verdict] : "";
    var allowed = {};
    RATINGS.forEach(function (r) { allowed[r] = self.allowed(r); });
    return {
      phase: p, n: this.cards.length, m: m, right: right, secured: this.securedCount(),
      headline: right + " of " + m + " right",
      // ⊕ Sharpen review (Fable, M-2) — mid-pass the strip is the headline
      // and the bar/chips only; the secured count belongs to the end
      // screen, which keeps it.
      securedLine: "",
      helper: "",
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
      canForward: this.canForward(),   // ⊕ MRB-354
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
        this.settleEnd(); this.changed();
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
      if (self.pending.length) { self.flushSoon(0); }
      else if (self.end) { self.settleEnd(); }
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

  // The pupil's own ratings for the deck → where the pass stands, AND
  // (⊕ MRB-354) which cards are already secured. A read that fails (RLS,
  // network, no reader) → a fresh pass and nothing secured yet, today's
  // behaviour. Returns {R, secured}: `R` is `reconstruct()`'s answer (null =
  // a fresh pass, for `Engine.start()`'s `resume`); `secured` is
  // `securedInfo()`'s per-card map (for `historicalSecured`).
  function resumeFor(assignmentId, state) {
    var cards = (state && state.cards) || [];
    var read = typeof Api.resumeRead === "function"
      ? Promise.resolve().then(function () { return Api.resumeRead(assignmentId); }).catch(function () { return null; })
      : Promise.resolve(null);
    return read.then(function (rows) {
      var secured;
      try { secured = securedInfo(rows, cards).secured; } catch (e) { secured = {}; }
      var R;
      try { R = reconstruct(rows, cards, state && state.mode, Date.now(), loadIdk(assignmentId)); } catch (e) { R = null; }
      return { R: R, secured: secured };
    });
  }

  // Send what this device still holds, until it is all sent or sending fails.
  function drain(e, tries) {
    return Promise.resolve(e.flush()).then(function () {
      if (e.pending.length && !e.error && tries > 0) { return drain(e, tries - 1); }
      return null;
    });
  }

  var Api = {
    transport: null,          // (assignmentId, events[]) → Promise<state>
    transportKeepalive: null, // (assignmentId, events[]) → void; survives the page going away
    onSessionEnd: null,       // (assignmentId) → void
    onFinish: null,           // ⊕ 1 Oct 2026: (assignmentId) → void, once the Done screen's pass has settled
    modelCheck: null,         // (assignmentId, cardId, answer, engine) → Promise<verdict|null>
    resumeRead: null,         // (assignmentId) → Promise<[{card_id, rating, phase, rated_at, id}]>, oldest first
    modelWaitMs: MODEL_WAIT_MS,
    active: null,
    quickCheck: quickCheck,
    reconstruct: reconstruct,
    finishedAt: finishedAt,
    securedInfo: securedInfo,   // ⊕ MRB-354 — exposed for tests/drives
    open: function (assignmentId) {
      var t = Api.transport;
      var known = engines[assignmentId];
      if (known) {
        if (typeof t !== "function") { Api.active = known; return Promise.resolve(known); }
        // ⊕ Stage D — what this device did goes first; then, if the server
        // has all of it, the pass is rebuilt from the server exactly as a
        // first open would (another device may have moved it on). Still
        // holding events (offline): carry on with the pass in memory.
        // ⊕ Sharpen §13.6 — the server is asked either way: the teacher may
        // have deleted the set since.
        known.keepDrafts(true);
        return drain(known, 3).then(function () { return t(assignmentId, []); }).then(function (state) {
          if (state) { known.merge(state); }
          if (known.pending.length && !(known.end && known.end.all)) { Api.active = known; return known; }
          return resumeFor(assignmentId, known.state).then(function (r) {
            known.start(r.R, r.secured);
            Api.active = known;
            return known;
          });
        }, function (err) {
          if (err && err.message === "not_your_homework") { delete engines[assignmentId]; throw err; }
          if (known.end && known.end.all) { known.start(null); }
          Api.active = known;
          return known;
        });
      }
      if (typeof t !== "function") { return Promise.reject(new Error("no_transport")); }
      // Anything still queued on this device from a previous visit goes
      // first, so the ratings we read back already include it.
      var queued = load(assignmentId);
      return Promise.resolve(t(assignmentId, queued)).then(function (state) {
        save(assignmentId, []);
        return resumeFor(assignmentId, state).then(function (r) {
          var e = new Engine(assignmentId, state, { resume: r.R, secured: r.secured });
          engines[assignmentId] = e;
          Api.active = e;
          return e;
        });
      });
    },
    close: function () {
      var e = Api.active;
      Api.active = null;
      if (e) { e.keepDrafts(true); e.flush(); }
    },
    flushAll: function () {
      Object.keys(engines).forEach(function (k) { engines[k].flush(); });
    },
    beaconAll: function () {
      Object.keys(engines).forEach(function (k) { engines[k].flushBeacon(); });
    },
    _Engine: Engine,
    // (tests: a page reload — this page's engines are gone, the device's
    // storage is not)
    _reset: function () {
      Object.keys(engines).forEach(function (k) {
        var e = engines[k];
        if (e.timer) { clearTimeout(e.timer); e.timer = null; }
        if (e.draftTimer) { e.keepDrafts(true); }   // as pagehide would
      });
      engines = {}; Api.active = null;
    }
  };

  // ⊕ Prompt Y (4 Oct 2026) — TWO TABS ON ONE HOMEWORK. The server keeps one
  // open sitting per pupil per homework, so two tabs write into the SAME
  // sitting, and within a sitting the latest rating of a card is the one
  // that counts (the ‹ Back rule). A tab left open on card 1 while the pupil
  // secured it in another tab would offer card 1 again, and a Not yet typed
  // there un-secured it on the server while this tab's own screen still
  // counted it. The stale tab is the fault, so it is never allowed to take
  // an answer: another tab's progress on this homework (see
  // `progressElsewhere`) marks it stale, and the moment
  // this tab is in front again — visible and focused — it is rebuilt from
  // the server through the same reopen path a second device uses
  // (`Api.open`: this tab's own unsent events first, then the pass the
  // server holds), and redrawn.
  var stale = {};
  // Only PROGRESS elsewhere counts: an answer, a rating, or a sitting's end
  // queued or delivered (the queue going from holding them to empty is the
  // other tab's send landing — the moment the server has them). An "I don't
  // know" is itself an answer in that queue. Drafts, visibility pings and the
  // "I don't know" record move nothing on the server, and every rebuild
  // rewrites them, so counting them made two tabs that both thought they
  // were in front rebuild each other for ever, dropping taps on the way.
  function hasWork(v) {
    try {
      return (JSON.parse(v || "[]") || []).some(function (x) {
        return !!x && (x.type === "rated" || x.type === "answer_submitted" || x.type === "session_finish");
      });
    } catch (e) { return false; }
  }
  function progressElsewhere(ev, id) {
    return ev.key === STORE + id && (hasWork(ev.newValue) || hasWork(ev.oldValue));
  }
  function inFront() {
    var d = root.document;
    return !!d && d.visibilityState !== "hidden" && (typeof d.hasFocus !== "function" || d.hasFocus());
  }
  // One rebuild at a time. The other tab's last rating can still be in
  // flight when this one comes forward, so the first rebuild may read the
  // server a moment too early; that tab's send then lands, writes storage,
  // and asks again. Two `Api.open`s racing would let the EARLIER read finish
  // last and win, so a request that arrives mid-rebuild waits for it and
  // runs once after.
  var resyncing = false, resyncAgain = false;
  function resync() {
    var e = Api.active;
    if (!e || !stale[e.id] || !inFront()) { return; }
    if (resyncing) { resyncAgain = true; return; }
    var id = e.id;
    stale[id] = false;
    resyncing = true;
    Api.open(id).then(function (k) { if (k) { k.changed(); } }, function () { e.changed(); })
      .then(function () {
        resyncing = false;
        if (resyncAgain) { resyncAgain = false; stale[id] = true; resync(); }
      });
  }
  Api._resync = resync;   // tests

  if (root.document && root.addEventListener) {
    root.document.addEventListener("visibilitychange", function () {
      if (Api.active) { Api.active.visibility(); }
      resync();
    });
    root.addEventListener("focus", resync);
    root.addEventListener("storage", function (ev) {
      if (!ev || !ev.key || ev.key.indexOf(STORE) !== 0) { return; }
      Object.keys(engines).forEach(function (id) { if (progressElsewhere(ev, id)) { stale[id] = true; } });
      resync();
    });
    root.addEventListener("pagehide", function () { Api.beaconAll(); });
  }

  if (typeof module !== "undefined" && module.exports) { module.exports = Api; }
  root.MRBHomework = Api;
})(typeof window !== "undefined" ? window : globalThis);
