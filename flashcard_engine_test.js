#!/usr/bin/env node
/* MRB-351 pupil flow — the flashcard homework ENGINE, driven directly in
 * Node with no browser and no network (docs/mrb351/PUPIL-FLOW.md §9.1, §11).
 *
 *   node flashcard_engine_test.js          # run every check
 *   node flashcard_engine_test.js --sql    # print the SQL that re-derives
 *                                          # the parity table's `sql` column
 *
 * WHAT IT PROVES
 *   · quickCheck === SQL flashcard_quick_check, case for case (A12). The
 *     `sql` column of tests/fixtures/quickcheck_cases.json was produced by
 *     the real function on TEST (whose body is byte-identical to
 *     production's); --sql prints the query that regenerates it.
 *   · "N of M right" counts THIS pass; ‹ Back re-answers and REPLACES the
 *     card's rating for this pass; "I don't know"; the chip and the filled
 *     rating from a verdict; a late verdict is ignored; resume from
 *     {card: rating}; make mode's two passes; the end screen's words and
 *     button in every case A8 names; × after one Check ends the sitting
 *     (A13); none of the retired strings survive.
 *   · ⊕ Sharpen (§13.7): the verdict caps the rating; nothing rates while
 *     checking; "I don't know" → own words, capped at Nearly, replayed
 *     once; the leftovers screen (Try again, no session_finish); Try again
 *     replays only the leftovers with a redo of a green card; ONE
 *     session_finish across a pass and its retries; a deleted set → gone.
 *
 * WHAT IT DOES NOT PROVE: the server's arithmetic (TEST, under real roles),
 * or the page (flashcard_homework_drive.py).
 */
"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = __dirname;
const CASES = JSON.parse(fs.readFileSync(path.join(ROOT, "tests/fixtures/quickcheck_cases.json"), "utf8"));

if (process.argv.includes("--sql")) {
  const lit = (v) => (v === null ? "null::text" : "$q$" + v + "$q$");
  console.log("select json_agg(json_build_object('i',i,'v',public.flashcard_quick_check(p,m)) order by i) from (values\n" +
    CASES.cases.map((c, i) => `(${i},${lit(c.pupil)},${lit(c.model)})`).join(",\n") + "\n) t(i,p,m);");
  process.exit(0);
}

// A device store the engine can write to.
const store = {};
Object.defineProperty(globalThis, "localStorage", {
  configurable: true,
  value: {
    getItem: (k) => (k in store ? store[k] : null),
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: (k) => { delete store[k]; },
    clear: () => { for (const k of Object.keys(store)) delete store[k]; },
  },
});

const H = require("./shared/flashcard-homework.js");

let fails = 0, passes = 0;
function check(ok, what) {
  if (ok) { passes++; } else { fails++; console.log("  FAIL " + what); }
}
const tick = (ms = 0) => new Promise((r) => setTimeout(r, ms));

// ── 1. quickCheck = SQL ────────────────────────────────────────────────
let parity = 0;
CASES.cases.forEach((c, i) => {
  const js = H.quickCheck(c.pupil, c.model);
  if (js === c.sql) { parity++; }
  else { check(false, `quickCheck case ${i} ${JSON.stringify(c.pupil)} vs ${JSON.stringify(c.model)}: JS ${js} SQL ${c.sql}`); }
});
check(parity === CASES.cases.length, `quickCheck agrees with SQL on all ${CASES.cases.length} cases (${parity})`);
console.log(`  quickCheck: ${parity}/${CASES.cases.length} cases agree with public.flashcard_quick_check`);

// ── a stand-in flashcard_record ─────────────────────────────────────────
// Latest rating per card per sitting PER PHASE (the parked migration's rule,
// §8 as built — a make-phase Got it must survive its own sitting's review);
// secure = a make got_it + a later review got_it, or review got_its in two
// sittings the test marks as an hour apart.
function server(opts) {
  const cards = opts.cards.map((c, i) => Object.assign({ id: "c" + i, position: i, made: false, known: false,
    secured: false, last: null, mine: null }, c));
  const S = { events: [], sittings: 0, open: null, fail: false, gapOk: false, sittingRatings: {}, history: [] };
  function recompute() {
    cards.forEach((c) => {
      const per = [];
      S.history.concat(S.open ? [S.sittingRatings] : []).forEach((m) => {
        ["make", "review"].forEach((ph) => { if (m[c.id + ph]) { per.push(m[c.id + ph]); } });
      });
      c.known = per.some((r) => r.rating === "got_it");
      const make = per.some((r) => r.rating === "got_it" && r.phase === "make");
      const rev = per.filter((r) => r.rating === "got_it" && r.phase === "review").length;
      c.secured = opts.rule === "quick" ? c.known : ((make && rev >= 1) || (rev >= 2 && S.gapOk));
    });
  }
  function state() {
    return JSON.parse(JSON.stringify({
      assignment_id: "A", title: "Forces", mode: opts.mode, rule: opts.rule, n: cards.length,
      note: "Do these", made: cards.filter((c) => c.made).length, known: cards.filter((c) => c.known).length,
      secured: cards.filter((c) => c.secured).length, complete: cards.every((c) => c.secured),
      session_id: S.open, sittings: S.sittings, cards,
    }));
  }
  S.transport = (id, events) => {
    if (S.fail) { return Promise.reject(new Error("offline")); }
    (events || []).forEach((e) => {
      S.events.push(e);
      if (!S.open) { S.sittings++; S.open = "s" + S.sittings; S.sittingRatings = {}; }
      const c = cards.find((k) => k.id === e.card);
      if (e.type === "answer_submitted" && c && e.phase === "make" && !c.made) { c.made = true; c.mine = e.answer; }
      if (e.type === "rated" && c) { c.last = e.rating; S.sittingRatings[c.id + e.phase] = { rating: e.rating, phase: e.phase }; }
      if (e.type === "session_finish") { S.history.push(S.sittingRatings); S.open = null; }
    });
    recompute();
    return Promise.resolve(state());
  };
  S.cards = cards;
  return S;
}

const FIVE = [
  { question: "Unit of force?", answer: "The newton (N)" },
  { question: "Formula of water?", answer: "H2O" },
  { question: "What is weight?", answer: "The force acting on an object due to gravity" },
  { question: "Spring equation?", answer: "F = ke" },
  { question: "Velocity: scalar or vector?", answer: "A vector" },
];

async function fresh(opts) {
  H._reset();
  localStorage.clear();
  const S = server(Object.assign({ mode: "review", rule: "secure", cards: FIVE }, opts || {}));
  H.transport = S.transport;
  H.modelCheck = null;
  H.resumeRead = null;
  H.modelWaitMs = 4000;
  const e = await H.open("A");
  return { S, e };
}

function answer(e, text) { e.setDraft(text); e.check(); }

(async function main() {
  // ── 2. right THIS pass, the bar, the leftovers end screen ───────────
  {
    const { S, e } = await fresh();
    let v = e.view();
    check(v.headline === "0 of 5 right", "a pass opens at '0 of 5 right' (" + v.headline + ")");
    check(v.segments.length === 5 && v.segments[0].current && v.segments[0].state === "todo", "five segments, the first is current");
    check(!v.canBack, "no ‹ Back on the first card");
    check(!e.canCheck(), "Check disabled before any text");
    e.setDraft("   ");
    check(!e.canCheck(), "Check disabled for spaces only");
    answer(e, "newton");                  // match → Right, Got it filled
    v = e.view();
    check(v.revealed && v.chip === "Right" && v.suggest === "got_it", "a matching answer: chip Right, Got it filled");
    check(v.mine === "newton", "the pupil's answer is kept for the back of the card");
    e.rate("got_it");
    v = e.view();
    check(v.headline === "1 of 5 right" && v.segments[0].state === "right" && v.segments[1].current, "Got it → '1 of 5 right', segment 1 green, segment 2 current");
    answer(e, "water");                   // no → Wrong, Not yet filled
    v = e.view();
    check(v.chip === "Wrong" && v.suggest === "not_yet", "a wrong one-word answer: chip Wrong, Not yet filled");
    e.rate("not_yet");
    check(e.view().segments[1].state === "answered", "Not yet → segment grey (answered, not right)");
    answer(e, "force of gravity on it");  // multi-word, no model → no chip, nothing filled
    v = e.view();
    check(v.revealed && v.chip === "" && v.suggest === null && v.cap === null, "undecided and no model check: no chip, no rating filled, no cap (A3)");
    check(v.allowed.got_it && v.allowed.nearly && v.allowed.not_yet, "no verdict → all three ratings allowed");
    e.rate("nearly");
    answer(e, "f = ke"); e.rate("not_yet");
    answer(e, "vector"); e.rate("got_it");
    v = e.view();
    check(v.phase === "end" && v.end && v.end.line1 === "2 of 5 right", "end screen line 1 '2 of 5 right' (" + (v.end && v.end.line1) + ")");
    check(v.end.button === "retry" && v.end.buttonLabel === "Try again" && v.end.line2 === "" && v.end.helper === "",
          "not all right: ONE button 'Try again', no line 2, no helper, nothing waits");
    await e.flush(); await tick(5); await e.flush(); await tick(5);
    v = e.view();
    check(v.end.line2 === "" && v.end.button === "retry", "the server's reply adds nothing to the leftovers screen");
    check(!S.events.some((x) => x.type === "session_finish"), "a pass that is not all right does NOT end the sitting");
    const rated = S.events.filter((x) => x.type === "rated");
    check(rated.length === 5 && rated.every((x) => x.via === "auto" || x.via === "tap"), "every rating says how it was chosen (via)");
    check(rated[0].via === "auto" && rated[2].via === "tap", "the filled rating tapped = auto; no suggestion = tap");
    check(!S.events.some((x) => "think_ms" in x || "active_ms" in x), "no event carries a duration");
  }

  // ── 3. ‹ Back re-answers and REPLACES the rating ────────────────────
  {
    const { S, e } = await fresh();
    answer(e, "newton"); e.rate("got_it");
    check(e.view().right === 1, "right = 1 after card 1");
    e.setDraft("some half typed");
    e.back();
    let v = e.view();
    check(v.card.id === "c0" && !v.revealed && v.draft === "newton", "‹ Back: card 1 again, in state A, the earlier text in the box");
    check(v.headline === "1 of 5 right", "going back does not change the count by itself");
    answer(e, "no idea"); e.rate("not_yet");
    v = e.view();
    check(v.right === 0 && v.headline === "0 of 5 right", "re-rated Not yet REPLACES Got it for this pass (" + v.headline + ")");
    check(v.card.id === "c1" && v.draft === "some half typed", "forward again: card 2 keeps what was typed before going back");
    await e.flush();
    const c0 = S.events.filter((x) => x.type === "rated" && x.card === "c0").map((x) => x.rating);
    check(c0.join() === "got_it,not_yet", "both ratings are events; the latest wins (" + c0 + ")");
    e.back(); answer(e, "newton"); e.rate("got_it");
    check(e.view().right === 1, "and back up again → 1 of 5");
  }

  // ── 4. model verdicts: in time, late, and nothing rates while checking ─
  {
    const { e } = await fresh();
    H.modelCheck = () => Promise.resolve("partial");
    answer(e, "force of gravity");
    check(e.view().chip === "Checking…" && e.view().suggest === null, "state B: 'Checking…', none filled");
    await tick(5);
    check(e.view().chip === "Nearly" && e.view().suggest === "nearly", "the model's 'partial' → chip Nearly, Nearly filled");
    e.rate("nearly");
    H.modelWaitMs = 60;
    H.modelCheck = () => new Promise((r) => setTimeout(() => r("match"), 150));
    answer(e, "made of hydrogen and oxygen");
    await tick(100);
    check(e.view().chip === "" && e.view().suggest === null, "no verdict inside the wait → no chip at all (A3)");
    await tick(100);
    check(e.view().chip === "", "a verdict landing after the wait is ignored");
    e.rate("not_yet");
    H.modelWaitMs = 4000;
    H.modelCheck = () => Promise.resolve({ weird: true });
    answer(e, "mass times gravity strength");
    await tick(5);
    check(e.view().chip === "" && e.view().cap === null, "a reply without a verdict string → no chip, no cap");
  }

  // ── 5. resume a sitting still open on the server ─────────────────────
  {
    H._reset(); localStorage.clear();
    const S = server({ mode: "review", rule: "secure", cards: FIVE });
    H.transport = S.transport;
    await S.transport("A", [{ id: "x", type: "card_shown", card: "c0", phase: "review", at: Date.now() }]);
    const now = Date.now();
    H.resumeRead = () => Promise.resolve({ c3: { rating: "got_it", phase: "review", at: now - 60000 },
                                            c1: { rating: "not_yet", phase: "review", at: now - 30000 } });
    const e = await H.open("A");
    const v = e.view();
    check(v.pos === 3 && v.headline === "1 of 5 right" && v.segments[0].state === "answered" && v.segments[1].state === "right",
          "resume: the two rated cards count as done, the pass carries on at card 3 (" + v.headline + ", pos " + v.pos + ")");
    check(v.canBack, "resume: ‹ Back reaches the cards already rated");
    H._reset(); localStorage.clear();
    H.resumeRead = () => Promise.resolve({ c3: { rating: "got_it", phase: "review", at: Date.now() - 11 * 60000 } });
    const e2 = await H.open("A");
    check(e2.view().pos === 1 && e2.view().headline === "0 of 5 right", "a sitting silent for over ten minutes is not resumed");
    H._reset(); localStorage.clear();
    H.resumeRead = () => Promise.reject(new Error("rls"));
    const e3 = await H.open("A");
    check(e3.view().pos === 1, "a failed resume read starts a fresh pass");
    H.resumeRead = null;
  }

  // ── 6. make mode: the writing pass, its end screen, the review pass ──
  {
    const { S, e } = await fresh({ mode: "make", cards: FIVE.slice(0, 3) });
    let v = e.view();
    check(v.phase === "make" && v.headline === "0 of 3 right", "make mode opens on the writing pass");
    answer(e, "newton"); e.rate("got_it");
    e.idk(); answer(e, "water"); e.rate("not_yet");     // I don't know → own words → Wrong
    answer(e, "gravity"); e.rate("got_it");
    v = e.view();
    check(v.phase === "make" && v.card.id === "c1", "the I-don't-know card comes round once more in the writing pass");
    answer(e, "water"); e.rate("not_yet");
    v = e.view();
    check(v.phase === "end" && v.end.line1 === "2 of 3 right", "writing pass end screen: '2 of 3 right'");
    check(v.end.button === "again" && v.end.buttonLabel === "Revise flashcards one more time" && v.end.helper === "" && v.end.line2 === "",
          "writing pass: the button is 'Revise flashcards one more time', straight away");
    check(!S.events.concat(e.pending).some((x) => x.type === "session_finish"), "the writing pass does NOT end the sitting");
    await e.flush(); await tick(5);
    check(S.cards.every((c) => c.made) && S.cards[1].mine === "I don't know", "every card made; I don't know is what the teacher sees");
    e.again();
    v = e.view();
    check(v.phase === "review" && v.headline === "0 of 3 right" && e.afterWriting, "the review pass opens at '0 of 3 right' (A7), same sitting");
    check(v.securedLine === "0 secured" && v.helper === "Revise flashcards one more time", "review pass strip: '0 secured' and the helper line");
    check(e.view().card.id === "c1", "the review pass starts on the Not yet card");
    for (let k = 0; k < 3; k++) {
      const id = e.view().card.id;
      answer(e, id === "c1" ? "water" : "no idea at all really");
      e.rate(id === "c1" ? "not_yet" : "got_it");
    }
    v = e.view();
    check(v.end.button === "retry" && !S.events.concat(e.pending).some((x) => x.type === "session_finish"),
          "make's review pass with a card left: Try again, sitting still open");
    e.retry();
    check(e.view().card.id === "c1" && e.view().headline === "2 of 3 right", "Try again replays only c1, opening at '2 of 3 right'");
    answer(e, "h2o"); e.rate("got_it");
    await e.flush(); await tick(5); await e.flush(); await tick(5);
    v = e.view();
    check(S.events.filter((x) => x.type === "session_finish").length === 1, "the all-right pass ends the sitting, once");
    check(v.end.line1 === "3 of 3 right" && v.end.line2 === "2 of 3 secured so far", "two cards secure (c1 had no make Got it): " + v.end.line2);
    check(v.end.button === "done" && v.end.helper === "Revise flashcards one more time", "all right, secured < n → Done with the helper line");
  }

  // ── 7. end screen: all secured → Done; offline; all right, not secured ─
  {
    const { e } = await fresh({ rule: "quick", cards: FIVE.slice(0, 2) });
    answer(e, "newton"); e.rate("got_it");
    answer(e, "h2o"); e.rate("got_it");
    let v = e.view();
    check(v.end.button === "done" && v.end.line2 === "", "all right: Done at once; line 2 waits for the server (A8a)");
    await e.flush(); await tick(5); await e.flush(); await tick(5);
    v = e.view();
    check(v.end.line2 === "2 of 2 secured so far" && v.end.button === "done" && v.end.helper === "",
          "everything secured → 'Done', no helper line");
    check(v.securedLine === "", "rule quick shows no 'secured' line in the strip");

    const r = await fresh({ cards: FIVE.slice(0, 2) });
    answer(r.e, "newton"); r.e.rate("got_it");
    r.S.fail = true;
    answer(r.e, "h2o"); r.e.rate("got_it");
    await r.e.flush(); await tick(5);
    v = r.e.view();
    check(v.end.offline && v.end.line2 === "", "offline at the end: SAVED ON THIS PHONE in place of line 2, never a stale number");

    const h = await fresh({ cards: FIVE.slice(0, 2) });
    answer(h.e, "newton"); h.e.rate("got_it");
    answer(h.e, "h2o"); h.e.rate("got_it");
    await h.e.flush(); await tick(5); await h.e.flush(); await tick(5);
    v = h.e.view();
    check(v.end.button === "done" && v.end.line2 === "0 of 2 secured so far" && v.end.helper === "Revise flashcards one more time",
          "all right, nothing secured yet → Done + 'Revise flashcards one more time' (later)");
    check(Object.keys(store).every((k) => k.indexOf(".end.") < 0), "no end time is kept on the device any more");
  }

  // ── 8. × after one Check ends the sitting (A13) ──────────────────────
  {
    const { S, e } = await fresh();
    answer(e, "newton");
    e.finish();
    await tick(5); await e.flush(); await tick(5);
    check(S.events.some((x) => x.type === "session_finish"), "× after one Check in review sends session_finish");
    const g = await fresh();
    g.e.finish();
    await tick(5);
    check(!g.S.events.some((x) => x.type === "session_finish"), "× before doing anything leaves the sitting to time out");
  }

  // ── 9. retired strings ──────────────────────────────────────────────
  {
    const src = fs.readFileSync(path.join(ROOT, "shared/flashcard-homework.js"), "utf8")
      .replace(/\/\*[\s\S]*?\*\//g, "").replace(/\/\/.*$/gm, "");
    ["FOR NOW", "Go again", "Made ", "later on", "Finish for now", "Compare it yourself", "Not quite", "Keep revising",
     "right this time", "tooSoon", "HOUR_MS"]
      .forEach((w) => check(src.indexOf(w) < 0, "retired string absent from the engine: " + JSON.stringify(w)));
  }

  // ── 10. the verdict caps the rating (§13.1.1) ────────────────────────
  {
    const { e } = await fresh();
    answer(e, "newton");
    let v = e.view();
    check(v.allowed.not_yet && v.allowed.nearly && v.allowed.got_it && v.suggest === "got_it", "match: all three allowed, Got it filled");
    e.rate("got_it");
    H.modelCheck = () => Promise.resolve("partial");
    answer(e, "hydrogen and oxygen");
    await tick(5);
    v = e.view();
    check(!v.allowed.got_it && v.allowed.nearly && v.allowed.not_yet && v.suggest === "nearly" && v.cap === "nearly",
          "partial: Got it refused, Nearly filled");
    const was = v.card.id;
    e.rate("got_it");
    check(e.view().card.id === was && e.view().revealed, "rate('got_it') above the cap is a no-op: the card is unchanged");
    e.rate("nearly");
    H.modelCheck = null;
    answer(e, "water");
    v = e.view();
    check(!v.allowed.got_it && !v.allowed.nearly && v.allowed.not_yet && v.chip === "Wrong", "no: only Not yet");
    e.rate("nearly");
    check(e.view().card.id === v.card.id, "Nearly refused on a Wrong answer");
    e.rate("not_yet");
    answer(e, "dunno");
    v = e.view();
    check(v.chip === "No answer" && !v.allowed.got_it && !v.allowed.nearly && v.allowed.not_yet, "blank: only Not yet");
  }

  // ── 11. nothing rates while the check is out ───────────────────────
  {
    const { e } = await fresh();
    H.modelWaitMs = 60;
    H.modelCheck = () => new Promise(() => {});      // never answers
    answer(e, "some force thing");
    let v = e.view();
    check(v.checking && v.cap === "none" && !v.allowed.got_it && !v.allowed.nearly && !v.allowed.not_yet,
          "Checking…: all three ratings refused");
    e.rate("not_yet");
    check(e.view().card.id === "c0" && e.view().revealed, "a tap while checking does nothing");
    await tick(100);
    v = e.view();
    check(!v.checking && v.allowed.got_it && v.allowed.nearly && v.allowed.not_yet && v.suggest === null,
          "the wait expires with no verdict: all three allowed, none filled");
    H.modelWaitMs = 4000;
  }

  // ── 12. "I don't know" is a learning step (§13.1.4) ──────────────────
  {
    const { S, e } = await fresh();
    answer(e, "newton"); e.rate("got_it");
    e.idk();
    let v = e.view();
    check(v.learn && !v.revealed && v.learnAnswer === "H2O" && v.canBack, "idk(): learn state, card not revealed, the answer showing, ‹ Back kept");
    check(v.suggest === null && v.chip === "", "learn state: no chip, nothing filled");
    const evs = () => S.events.concat(e.pending);
    const before = evs().length;
    e.idk();
    check(evs().length === before && e.view().learn, "a second 'I don't know' is ignored");
    check(!e.canCheck(), "the own-words box starts empty");
    e.setDraft("h2o"); e.check();
    v = e.view();
    check(v.revealed && !v.learn && v.chip === "Right" && !v.allowed.got_it && v.suggest === "nearly",
          "own words Right: chip Right, but capped at Nearly (Nearly filled, Got it off)");
    e.rate("nearly");
    check(e.passIds.length === 6 && e.view().segments.length === 5 && e.view().chips.length === 5,
          "the card is appended once: 6 showings, still 5 segments");
    answer(e, "gravity"); e.rate("got_it");
    answer(e, "f = ke"); e.rate("got_it");
    answer(e, "vector"); e.rate("got_it");
    v = e.view();
    check(v.card && v.card.id === "c1" && !e.idkNow && v.segments[1].current, "it comes round last as a plain card");
    check(v.draft === "", "…with an empty box: answered from memory, not from the own-words step");
    answer(e, "h2o");
    v = e.view();
    check(v.allowed.got_it && v.suggest === "got_it", "on the replay a Right answer may be Got it");
    e.rate("got_it");
    v = e.view();
    check(v.phase === "end" && v.end.line1 === "5 of 5 right" && v.headline === "5 of 5 right",
          "the replay's rating is the pass rating; headline counts 5, not 6");
    const subs = evs().filter((x) => x.type === "answer_submitted" && x.card === "c1");
    check(subs.length === 3 && subs[0].idk && subs[0].answer === "I don't know" && subs[1].own_words && subs[1].answer === "h2o",
          "events: answer_submitted 'I don't know' (idk), then the own words (own_words)");
    check(evs().filter((x) => x.type === "revealed" && x.card === "c1").length === 3, "each answer is revealed once");
  }

  // ── 13. "I don't know" twice on one card → no third showing ─────────
  {
    const { e } = await fresh({ cards: FIVE.slice(0, 2) });
    e.idk(); e.setDraft("newton"); e.check(); e.rate("nearly");
    answer(e, "h2o"); e.rate("got_it");
    check(e.view().card.id === "c0", "c0 comes round");
    e.idk(); e.setDraft("newton"); e.check(); e.rate("nearly");
    const v = e.view();
    check(v.phase === "end" && e.passIds.length === 3 && v.end.line1 === "1 of 2 right", "second I don't know: no third showing, the pass ends");
  }

  // ── 14 + 15. Try again: only the leftovers, the chips, a redo ────────
  {
    const { S, e } = await fresh();
    const evs = () => S.events.concat(e.pending);
    answer(e, "newton"); e.rate("got_it");            // c0 green
    answer(e, "water"); e.rate("not_yet");            // c1 grey
    answer(e, "gravity"); e.rate("got_it");           // c2 green
    answer(e, "stretch"); e.rate("not_yet");          // c3 grey
    answer(e, "vector"); e.rate("got_it");            // c4 green
    let v = e.view();
    check(v.end.line1 === "3 of 5 right" && v.end.button === "retry" && v.end.line2 === "", "leftovers: '3 of 5 right', Try again, no line 2");
    check(!evs().some((x) => x.type === "session_finish"), "no session_finish on the leftovers screen");
    e.retry();
    v = e.view();
    check(e.retries === 1 && v.retry && v.headline === "3 of 5 right", "Try again opens at '3 of 5 right' (" + v.headline + ")");
    check(e.passIds.join() === "c1,c3" && v.card.id === "c1", "the queue is the two leftovers, in the pass's order");
    check(v.draft === "", "a leftover opens with an empty box, not its wrong answer");
    check(Object.keys(e.pass).sort().join() === "c0,c2,c4", "only the green ratings are carried in");
    const greens = v.chips.filter((g) => g.state === "right");
    check(v.chips.length === 5 && greens.length === 3 && greens.every((g) => g.redo) &&
          v.chips.filter((g) => g.state === "todo").length === 2 && v.chips[1].current && v.chips[0].num === 1,
          "chips: 3 green (redo), 2 to come, the second is current");
    e.setDraft("half");
    e.redo("c2");
    v = e.view();
    check(v.detour && v.card.id === "c2" && !v.revealed && v.draft === "gravity" && v.chips[2].current,
          "redo: the green card in state A with its earlier answer");
    check(v.canBack && v.chips.every((g) => !g.redo), "‹ Back offered; no chip is a redo during a redo");
    e.back();
    v = e.view();
    check(!v.detour && v.card.id === "c1" && e.pass.c2.rating === "got_it" && v.draft === "half",
          "‹ Back during a redo: back on the queue's card, the green rating untouched");
    e.redo("c2");
    answer(e, "stretch"); e.rate("not_yet");
    v = e.view();
    check(!v.detour && v.card.id === "c1" && v.headline === "2 of 5 right" && v.chips[2].state === "answered",
          "rated Not yet: replaces (2 of 5), chip grey, back on c1");
    check(e.passIds.join() === "c1,c3", "the redone card does not join this pass's queue");
    answer(e, "h2o"); e.rate("got_it");
    answer(e, "f = ke"); e.rate("got_it");
    v = e.view();
    check(v.end.line1 === "4 of 5 right" && v.end.button === "retry", "c2 is left: Try again again");
    e.retry();
    check(e.passIds.join() === "c2" && e.view().headline === "4 of 5 right", "a second retry replays only the still-grey card");
    answer(e, "gravity"); e.rate("got_it");
    await e.flush(); await tick(5); await e.flush(); await tick(5);
    v = e.view();
    check(v.end.line1 === "5 of 5 right" && v.end.button === "done" && v.end.line2 === "0 of 5 secured so far",
          "finishing all right: Done, line 2 from the server");
    check(S.events.filter((x) => x.type === "session_finish").length === 1, "exactly ONE session_finish across the pass and both retries");
    const c2 = S.events.filter((x) => x.type === "rated" && x.card === "c2").map((x) => x.rating);
    check(c2.join() === "got_it,not_yet,got_it", "every rating of the redone card is an event (" + c2 + ")");
    check(S.sittings === 1, "one server sitting for the whole thing");
    e.retry();
    check(e.view().phase === "end", "no Try again after an all-right pass");
  }

  // ── 16. a set deleted while open ────────────────────────────────────
  {
    const { e } = await fresh();
    H.transport = () => Promise.reject(Object.assign(new Error("not_your_homework"), { code: "P0001" }));
    answer(e, "newton");
    await e.flush(); await tick(5);
    check(e.error === "gone" && e.pending.length === 0, "not_your_homework → the engine stops and says gone");
    H._reset();
    let rej = null;
    await H.open("A").catch((err) => { rej = err; });
    check(rej && rej.message === "not_your_homework", "opening a deleted set rejects with not_your_homework");
    // the deck is already on the device (the page was open before the delete)
    const g = await fresh({ cards: FIVE.slice(0, 1) });
    answer(g.e, "newton"); g.e.rate("got_it");
    await g.e.flush(); await tick(5);
    H.close();
    let rej2 = null;
    H.transport = () => Promise.reject(new Error("not_your_homework"));
    await H.open("A").catch((err) => { rej2 = err; });
    check(rej2 && rej2.message === "not_your_homework" && H.active === null,
          "reopening a deck already on the device asks the server first: deleted → rejects");
    H.transport = () => Promise.reject(new Error("offline"));
    const again = await fresh({ cards: FIVE.slice(0, 1) });
    H.close();
    H.transport = () => Promise.reject(new Error("Failed to fetch"));
    const back = await H.open("A");
    check(back === again.e && H.active === again.e, "offline, the deck on the device opens as before");
  }

  console.log(`\n  ${passes} passed, ${fails} failed`);
  if (fails) { console.log("  FAIL — flashcard engine"); process.exit(1); }
  console.log("  PASS — flashcard engine (pupil flow)");
  process.exit(0);
})().catch((err) => { console.error(err); process.exit(1); });
