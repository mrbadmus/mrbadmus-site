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
 *   · ⊕ Sharpen (§13.7): "I don't know" → own words, replayed once; the leftovers screen (Try again, no session_finish); Try again
 *     replays only the leftovers with a redo of a green card; ONE
 *     session_finish across a pass and its retries; a deleted set → gone.
 *   · ⊕ Stage D (STAGE-D-PLAN.md §2.9, cases 17–27): `reconstruct` builds the
 *     pass from the pupil's own ratings; × / a dead phone / another device /
 *     offline-then-reload land on the next card not done; Try again lasts an
 *     hour; answers are sent at once; the keepalive leaves the queue; half-
 *     typed words survive a reload.
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
  const S = { events: [], sittings: 0, open: null, fail: false, gapOk: false, sittingRatings: {}, history: [],
              rows: [], seen: {} };
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
      if (e.id && S.seen[e.id]) { return; }          // on conflict (id) do nothing
      if (e.id) { S.seen[e.id] = true; }
      S.events.push(e);
      if (!S.open) { S.sittings++; S.open = "s" + S.sittings; S.sittingRatings = {}; }
      const c = cards.find((k) => k.id === e.card);
      if (e.type === "answer_submitted" && c && e.phase === "make" && !c.made) { c.made = true; c.mine = e.answer; }
      if (e.type === "rated" && c) {
        c.last = e.rating; S.sittingRatings[c.id + e.phase] = { rating: e.rating, phase: e.phase };
        // flashcard_reviews: one row per rating; a make rating only once the card is made
        if (e.phase !== "make" || c.made) {
          // ⊕ MRB-354 — `session_id` is the real grouping key for secured
          // now; `S.open` already IS this stand-in's sitting id.
          S.rows.push({ id: e.id, card_id: c.id, rating: e.rating, phase: e.phase, rated_at: e.at, session_id: S.open });
        }
      }
      if (e.type === "session_finish") { S.history.push(S.sittingRatings); S.open = null; }
    });
    recompute();
    return Promise.resolve(state());
  };
  S.cards = cards;
  // ⊕ Stage D — the pupil's own flashcard_reviews, oldest first (RLS: own rows).
  S.reviews = () => JSON.parse(JSON.stringify(S.rows));
  S.shift = (ms) => { S.rows.forEach((r) => { r.rated_at -= ms; }); };
  return S;
}

const FIVE = [
  { question: "Unit of force?", answer: "The newton (N)" },
  { question: "Formula of water?", answer: "H2O" },
  { question: "What is weight?", answer: "The force acting on an object due to gravity" },
  { question: "Spring equation?", answer: "F = ke" },
  { question: "Velocity: scalar or vector?", answer: "A vector" },
];

// A real-shaped 10-card deck (the "Organic Chemistry Quiz" shape: AQA organic
// wording, one long sentence-style model answer per card). The crude-oil card
// is word for word the one in docs/experience/Y-REPORT.md; the rest are
// written in the same register.
const TEN = [
  { question: "Describe how crude oil is formed.", answer: "Plankton died, were buried under sediment and compressed via heat and pressure over millions of years" },
  { question: "What is a hydrocarbon?", answer: "A compound made of hydrogen and carbon atoms only" },
  { question: "What is the general formula of the alkanes?", answer: "CnH2n+2" },
  { question: "What is the general formula of the alkenes?", answer: "CnH2n" },
  { question: "How does fractional distillation separate crude oil?", answer: "It separates the hydrocarbons by boiling point as vapour rises up the fractionating column" },
  { question: "What happens to viscosity as chain length increases?", answer: "Viscosity increases as the chains get longer" },
  { question: "What is cracking?", answer: "Breaking down long chain hydrocarbons into shorter, more useful molecules" },
  { question: "What is the test for an alkene?", answer: "Bromine water turns from orange to colourless" },
  { question: "What is formed when an alkane burns completely?", answer: "Carbon dioxide and water" },
  { question: "What is a functional group?", answer: "The atom or group of atoms that gives a compound its characteristic reactions" },
];

async function fresh(opts) {
  // ⊕ MRB-354 test-harness hardening — a straggling microtask/short-timer
  // chain from the PREVIOUS test's flush() can still be in flight (it
  // captured the OLD Api.transport, which is harmless to IT, but its own
  // requeue (flushSoon(0)/(8000)) reads Api.transport FRESH when it later
  // fires). Give any such chain a moment to settle against the transport
  // that is still live for it, before `_reset()` swaps in a new one.
  await tick(20);
  H._reset();
  localStorage.clear();
  const S = server(Object.assign({ mode: "review", rule: "secure", cards: FIVE }, opts || {}));
  H.transport = S.transport;
  H.transportKeepalive = null;
  H.modelCheck = null;
  H.resumeRead = () => Promise.resolve(S.reviews());
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
    check(v.revealed && v.chip === "Right" && v.suggest === null && v.allowed.got_it, "a matching answer: chip Right, nothing filled, Secured allowed");
    check(v.mine === "newton", "the pupil's answer is kept for the back of the card");
    e.rate("got_it");
    v = e.view();
    check(v.headline === "1 of 5 right" && v.segments[0].state === "right" && v.segments[1].current, "Got it → '1 of 5 right', segment 1 green, segment 2 current");
    answer(e, "the");                     // a lone function word → Wrong, Not yet filled
    v = e.view();
    check(v.chip === "Wrong" && v.suggest === null, "a lone function word: chip Wrong, nothing filled");
    e.rate("not_yet");
    check(e.view().segments[1].state === "answered", "Not yet → segment grey (answered, not right)");
    answer(e, "force of gravity on it");  // multi-word, no model → no chip, nothing filled
    v = e.view();
    // ⊕ Mide, 5 Oct 2026 (the pupil decides): no verdict at all, and every
    // rating is still open — Secured included.
    check(v.revealed && v.chip === "" && v.suggest === null, "undecided and no model check: no chip, nothing filled");
    check(v.allowed.got_it && v.allowed.nearly && v.allowed.not_yet, "no verdict → all three ratings allowed");
    e.rate("got_it");
    answer(e, "f = ke"); e.rate("not_yet");
    answer(e, "vector"); e.rate("not_yet");
    v = e.view();
    // ⊕ MRB-354 — the end screen is "N of M secured" (not "right"): c0 and
    // c2 are got_it, nothing was ever secured before this pass, so 2 of 5.
    check(v.phase === "end" && v.end && v.end.line1 === "2 of 5 secured", "end screen line 1 '2 of 5 secured' (" + (v.end && v.end.line1) + ")");
    check(v.end.button === "retry" && v.end.buttonLabel === "Try again" && !v.end.secondary,
          "not all secured: ONE button 'Try again', no secondary, nothing waits on the server");
    await e.flush(); await tick(5); await e.flush(); await tick(5);
    v = e.view();
    check(v.end.line1 === "2 of 5 secured" && v.end.button === "retry", "the server's reply adds nothing to the leftovers screen");
    check(!S.events.some((x) => x.type === "session_finish"), "a pass that is not all right does NOT end the sitting");
    const rated = S.events.filter((x) => x.type === "rated");
    check(rated.length === 5 && rated.every((x) => x.via === "auto" || x.via === "tap"), "every rating says how it was chosen (via)");
    check(rated.every((x) => x.via === "tap"), "nothing is pre-filled, so every rating is a tap");
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
    await e.flush(); await tick(5); await e.flush();
    const c0 = S.events.filter((x) => x.type === "rated" && x.card === "c0").map((x) => x.rating);
    check(c0.join() === "got_it,not_yet", "both ratings are events; the latest wins (" + c0 + ")");
    e.back(); answer(e, "newton"); e.rate("got_it");
    check(e.view().right === 1, "and back up again → 1 of 5");
  }

  // ── 4. model verdicts: in time, late, and nothing rates while checking ─
  {
    const { e } = await fresh();
    H.modelCheck = () => Promise.resolve("partial");
    answer(e, "force in newtons");
    check(e.view().chip === "Checking…" && e.view().suggest === null, "state B: 'Checking…', none filled");
    await tick(5);
    check(e.view().chip === "Nearly" && e.view().suggest === null && e.view().allowed.got_it, "the model's 'partial' → chip Nearly, nothing filled, Secured allowed");
    e.rate("nearly");
    H.modelWaitMs = 60;
    H.modelCheck = () => new Promise((r) => setTimeout(() => r("match"), 100));
    answer(e, "made of water");
    await tick(80);
    // ⊕ option B: the first wait ran out at 60 ms, so a quiet retry is out —
    // still "Checking…" — and the first reply, landing at 100 ms (inside the
    // retry's own wait, which ends at 120), is used.
    check(e.view().chip === "Checking…" && e.view().allowed.got_it, "first wait over: a quiet retry, still 'Checking…', Secured allowed");
    await tick(60);
    check(e.view().chip === "Right" && e.view().suggest === null, "a slow first reply landing during the retry still counts as the hint");
    e.rate("got_it");
    H.modelCheck = () => new Promise((r) => setTimeout(() => r("match"), 400));
    answer(e, "a force");
    await tick(160);
    check(e.view().chip === "" && e.view().allowed.got_it, "both waits over: no chip, Secured still allowed");
    check(e.view().allowed.nearly && e.view().allowed.not_yet, "an unchecked answer can be rated anything");
    await tick(300);
    check(e.view().chip === "", "a verdict landing after both waits is ignored");
    e.rate("nearly");
    H.modelWaitMs = 4000;
    H.modelCheck = () => Promise.resolve({ weird: true });
    answer(e, "ke");
    await tick(5);
    check(e.view().chip === "" && e.view().allowed.got_it, "a reply without a verdict string (twice) → no chip, Secured allowed");
  }

  // ── 5. a failed resume read starts a fresh pass (§2.7) ───────────────
  {
    const { S, e } = await fresh();
    answer(e, "newton"); e.rate("got_it");
    await e.flush(); await tick(5);
    H._reset();
    H.resumeRead = () => Promise.reject(new Error("rls"));
    const e3 = await H.open("A");
    check(e3.view().pos === 1 && e3.view().headline === "0 of 5 right", "a failed resume read starts a fresh pass");
    H._reset();
    H.resumeRead = null;
    const e4 = await H.open("A");
    check(e4.view().pos === 1, "no resume reader → a fresh pass");
    check(S.rows.length === 1, "the stand-in kept the one rating as a flashcard_reviews row");
  }

  // ── 6. ⊕ MRB-354 — make mode: the writing pass follows the SAME rule as
  //      review (all secured → Done; else Try again on the leftovers,
  //      which stays in the WRITING stage — retyping, not reviewing). A
  //      card secured during the writing pass alone needs no review pass
  //      at all; "Revise flashcards one more time" afterward is the only
  //      way into one, voluntarily, over the whole deck. ──────────────────
  {
    const { S, e } = await fresh({ mode: "make", cards: FIVE.slice(0, 3) });
    let v = e.view();
    check(v.phase === "make" && v.headline === "0 of 3 right", "make mode opens on the writing pass");
    answer(e, "newton"); e.rate("got_it");                 // c0 secures in the writing pass
    answer(e, "water"); e.rate("not_yet");                 // c1 (model "H2O") is wrong
    answer(e, "the force acting on an object due to gravity"); e.rate("got_it");   // c2 secures too
    v = e.view();
    check(v.phase === "end" && v.end.line1 === "2 of 3 secured", "writing pass end screen: '2 of 3 secured' (2 cards got it)");
    check(v.end.button === "retry" && !v.end.secondary,
          "writing pass, not all secured: Try again, no secondary (MRB-354 — no forced review pass)");
    check(!S.events.concat(e.pending).some((x) => x.type === "session_finish"), "the leftovers screen does NOT end the sitting");
    await e.flush(); await tick(5);
    check(S.cards.every((c) => c.made), "every card made, even the one left not secured");
    e.retry();
    v = e.view();
    check(v.phase === "make" && e.passIds.join() === "c1" && v.card.id === "c1",
          "Try again on a writing pass RETYPES the leftover (stage stays make), not a review of it");
    answer(e, "h2o"); e.rate("got_it");                    // now every card has a got_it rating
    await e.flush(); await tick(5); await e.flush(); await tick(5);
    v = e.view();
    check(S.events.filter((x) => x.type === "session_finish").length === 1,
          "securing the last card ends the sitting, once — no review pass was ever needed");
    check(v.end.line1 === "3 of 3 secured" && v.end.button === "done" && v.end.secondary,
          "all three secured from the writing pass alone → Done + the Revise secondary");
    // the voluntary "Revise flashcards one more time": a FULL pass of the
    // whole deck, in review stage — it never un-secures anything.
    e.again();
    v = e.view();
    check(v.phase === "review" && v.headline === "0 of 3 right" && v.secured === 3,
          "Revise: a fresh review pass of the whole deck; still 3 of 3 secured throughout");
    answer(e, "no idea at all really"); e.rate("not_yet");  // a deliberately wrong rating this time
    v = e.view();
    check(v.secured === 3, "rating a card badly on a voluntary revise does not un-secure it (different sitting's group)");
    await e.flush(); await tick(5); await e.flush(); await tick(5);
  }

  // ── 7. ⊕ MRB-354 — end screen: ONE rating secures a card at once (no
  //      second sitting); all secured → Done + the quieter secondary;
  //      reopening an already-fully-secured deck skips straight to Done,
  //      never a fresh pass; the rule (secure/quick) changes nothing. ────
  {
    const { e } = await fresh({ rule: "quick", cards: FIVE.slice(0, 2) });
    answer(e, "newton"); e.rate("got_it");
    answer(e, "h2o"); e.rate("got_it");
    let v = e.view();
    check(v.end.line1 === "2 of 2 secured" && v.end.button === "done" && v.end.secondary,
          "both right, this is the FIRST sitting ever → Done at once (no second sitting needed, rule ignored)");
    // drain fully before the next fresh() reassigns Api.transport — a
    // flush() queued behind an in-flight one re-sends via flushSoon(0),
    // which would otherwise land on the NEXT test's stub.
    await e.flush(); await tick(5); await e.flush(); await tick(5);

    const r = await fresh({ cards: FIVE.slice(0, 2) });
    answer(r.e, "newton"); r.e.rate("got_it");
    r.S.fail = true;
    answer(r.e, "h2o"); r.e.rate("got_it");
    await r.e.flush(); await tick(5);
    v = r.e.view();
    check(v.end.line1 === "2 of 2 secured" && v.end.offline,
          "offline at the end: still shows the secured count the device already knows, never waits on the server");

    // ⊕ MRB-354 — reopening a deck that is ALREADY all secured (every card
    // got_it in an earlier, closed sitting) lands straight on Done — never
    // a fresh pass — and the secondary is still offered.
    r.S.fail = false;
    await r.e.flush(); await tick(5);
    const again = await H.open("A");
    v = again.view();
    check(v.phase === "end" && v.end.button === "done" && v.end.secondary && v.end.line1 === "2 of 2 secured",
          "reopening an already-fully-secured deck: straight to Done, no fresh pass");
    check(!again.passIds.length, "…with no pass ever built (the shortcut in start())");
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

  // ── 10. the verdict is a hint, never a gate (Mide, 5 Oct 2026) ───────
  const ALL3 = (v) => v.allowed.got_it && v.allowed.nearly && v.allowed.not_yet;
  {
    const { e } = await fresh();
    answer(e, "newton");
    let v = e.view();
    check(ALL3(v) && v.suggest === null, "match: all three allowed, nothing filled");
    e.rate("got_it");
    // (a) a right-but-different answer, verdict partial: Secured is allowed and secures the card
    H.modelCheck = () => Promise.resolve("partial");
    answer(e, "water");
    await tick(5);
    v = e.view();
    check(v.chip === "Nearly" && ALL3(v) && v.suggest === null, "(a) partial: chip Nearly, all three allowed, nothing filled");
    const was = v.card.id;
    e.rate("got_it");
    check(e.view().card.id !== was && e.securedMap()[was] === true, "(a) Secured on a 'Nearly' verdict is taken and secures the card");
    H.modelCheck = null;
    answer(e, "the");                     // a lone function word → Wrong
    v = e.view();
    // ⊕ 8 Oct 2026 — the floor: Nearly and Not yet stay open, Secured does not.
    check(v.chip === "Wrong" && v.allowed.nearly && v.allowed.not_yet && !v.allowed.got_it,
          "wrong verdict on a non-attempt: chip Wrong, Nearly / Not yet open, Secured greyed");
    e.rate("got_it");
    check(e.view().card.id === v.card.id && e.view().revealed, "Secured is refused on a lone function word");
    e.rate("nearly");
    check(e.view().card.id !== v.card.id, "Nearly is taken on a Wrong verdict");
    answer(e, "dunno");
    v = e.view();
    check(v.chip === "No answer" && v.allowed.nearly && v.allowed.not_yet && !v.allowed.got_it,
          "(b) typed blank-ish: chip No answer, Secured greyed");
    e.rate("not_yet");
    check(e.view().card.id !== v.card.id, "(b) Not yet is taken after a No answer verdict");
  }

  // ── 10b. THE REVEALED ANSWER IS ALWAYS THE DECK'S MODEL ANSWER ────────
  // (Mide, 5 Oct 2026.) What the overlay draws on the back of a card is
  // `card.answer` (and `learnAnswer` in the learn step) — both read straight
  // from the deck. What the pupil typed only ever reaches the screen as
  // `view().mine`, "your answer" beside it. Proved on the 10-card deck, on
  // every path, in review mode and in make mode.
  {
    const MODEL = (id) => TEN[Number(id.slice(1))].answer;
    const WRONG = "it is the stuff that comes out of the ground";
    let shown = 0;
    function proves(e, typed, what) {
      const v = e.view();
      const back = v.learn ? v.learnAnswer : v.card.answer;
      check(back === MODEL(v.card.id), what + ": the answer shown is the deck's model answer");
      check(typed === null || back !== typed, what + ": it is not what the pupil typed");
      if (v.revealed && typed !== null) { check(v.mine === typed, what + ": the typed text appears only as 'your answer'"); }
      shown++;
    }
    for (const mode of ["review", "make"]) {
      const { e } = await fresh({ mode, cards: TEN });
      // path 1 — first go: type a wrong answer, Not yet
      e.setDraft(WRONG); e.check();
      proves(e, WRONG, mode + " first go (typed wrong)");
      e.rate("not_yet");
      // path 2 — "I don't know": the model answer shows first, then own words
      e.idk();
      proves(e, null, mode + " I don't know (before typing)");
      check(e.view().mine === null && !e.view().revealed, mode + " I don't know: nothing the pupil typed is on the card");
      e.setDraft("made of hydrogen and carbon"); e.check();
      proves(e, "made of hydrogen and carbon", mode + " I don't know (own words typed)");
      e.rate("got_it");
      // finish the pass: c2.. wrong and Not yet, except the replay of c1
      for (let i = 2; i < 10; i++) { e.setDraft(WRONG + " " + i); e.check(); proves(e, WRONG + " " + i, mode + " card " + i); e.rate("not_yet"); }
      // the replay of the I-don't-know card comes round last
      check(e.view().card && e.view().card.id === "c1", mode + ": the I-don't-know card comes round again");
      e.setDraft(WRONG + " again"); e.check();
      proves(e, WRONG + " again", mode + " replay");
      e.rate("not_yet");
      // path 3 — Try again: the wrong answer is not carried in, and the model answer is still the deck's
      check(e.view().phase === "end" && e.view().end.button === "retry", mode + ": the pass ends on Try again");
      e.retry();
      proves(e, null, mode + " Try again (before typing)");
      check(e.view().draft === "" && e.view().mine === null, mode + " Try again: the earlier wrong answer is not put back");
      e.setDraft("second wrong try"); e.check();
      proves(e, "second wrong try", mode + " Try again (typed)");
      e.rate("not_yet");
    }
    // path 4 — "Revise flashcards one more time", after every card is secured
    {
      const { e } = await fresh({ cards: TEN });
      for (let i = 0; i < 10; i++) { e.setDraft(TEN[i].answer.slice(0, 12) + " my way"); e.check(); e.rate("got_it"); }
      check(e.view().end.button === "done" && e.view().end.secondary, "revise: ten secured, Done and the quiet secondary");
      e.again();
      proves(e, null, "Revise one more time (before typing)");
      e.setDraft("a wrong revise answer"); e.check();
      proves(e, "a wrong revise answer", "Revise one more time (typed wrong)");
      e.rate("not_yet");
      check(e.securedCount() === 10, "Revise: a wrong answer rated Not yet leaves the card secured");
      e.idk();
      proves(e, null, "Revise one more time (I don't know)");
    }
    console.log(`  model answer: ${shown} on-screen checks over review + make, first go / I don't know / Try again / Revise`);
  }

  // ── 11. nothing waits on the check (c) ──────────────────────────────
  {
    const { e } = await fresh();
    H.modelWaitMs = 60;
    H.modelCheck = () => new Promise(() => {});      // never answers
    answer(e, "some newton thing");
    let v = e.view();
    check(v.checking && ALL3(v), "(c) Checking…: all three ratings allowed at once");
    await tick(150);   // the first wait AND the quiet retry's
    v = e.view();
    check(!v.checking && ALL3(v) && v.suggest === null, "(c) both waits expire with no verdict: all three still allowed");
    H.modelWaitMs = 4000;
    // a check that fails outright
    H.modelCheck = () => Promise.reject(new Error("down"));
    answer(e, "another newton thing");
    check(ALL3(e.view()), "(c) a failing check: all three allowed straight away");
    await tick(5);
    check(!e.view().checking && ALL3(e.view()) && e.view().chip === "", "(c) a failing check: no chip, all three still allowed");
    e.rate("got_it");
    check(e.view().card.id !== "c0" || e.view().pos > 1, "(c) a tap while 'Checking…' is taken and moves on");
    await tick(5);
    H.modelCheck = null;
    // rate during Checking…, the verdict lands late: the rating stands
    const e2o = await fresh();
    const e2 = e2o.e;
    H.modelWaitMs = 4000;
    H.modelCheck = () => new Promise((r) => setTimeout(() => r("no"), 30));
    answer(e2, "a long newton answer here");
    e2.rate("got_it");
    await tick(60);
    check(e2.securedMap().c0 === true, "(c) rated Secured during Checking…; the late 'Wrong' changes nothing");
    const ev2 = e2o.S.events.concat(e2.pending).filter((x) => x.card === "c0" && x.type === "rated");
    check(ev2.length === 1 && ev2[0].rating === "got_it", "(c) exactly one rating event, got_it");
    H.modelCheck = null;
  }

  // (d) ten cards, all Secured in ONE pass → Done, with ratings and verdicts side by side (e)
  {
    const { S, e } = await fresh({ cards: TEN });
    H.modelCheck = () => Promise.resolve("partial");
    for (let i = 0; i < 10; i++) {
      answer(e, TEN[i].answer.slice(0, 12) + " my wording " + i);       // not the model answer: verdict comes back partial
      await tick(5);
      e.rate("got_it");
    }
    const v = e.view();
    check(v.phase === "end" && v.end.line1 === "10 of 10 secured" && v.end.button === "done" && v.end.secondary === true,
          "(d) ten cards secured in one pass, every verdict 'Nearly': 10 of 10 secured, Done");
    await e.flush(); await tick(5); await e.flush();
    const evs = S.events;
    const verdicts = evs.filter((x) => x.type === "answer_submitted");
    const rated = evs.filter((x) => x.type === "rated");
    check(rated.length === 10 && rated.every((x) => x.rating === "got_it"), "(e) ten rated events, all got_it");
    check(verdicts.length === 10 && verdicts.every((x, i) => x.answer === TEN[i].answer.slice(0, 12) + " my wording " + i),
          "(e) the typed answers are recorded exactly (answer_submitted)");
    check(evs.some((x) => x.type === "session_finish"), "(d) an all-secured pass ends the sitting");
    H.modelCheck = null;
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
    check(v.revealed && !v.learn && v.chip === "Right" && ALL3(v) && v.suggest === null,
          "own words Right: chip Right, all three allowed, nothing filled (no cap after 'I don't know')");
    e.rate("nearly");
    check(e.passIds.length === 6 && e.view().segments.length === 5 && e.view().chips.length === 5,
          "the card is appended once: 6 showings, still 5 segments");
    answer(e, "the force acting on an object due to gravity"); e.rate("got_it");
    answer(e, "f = ke"); e.rate("got_it");
    answer(e, "vector"); e.rate("got_it");
    v = e.view();
    check(v.card && v.card.id === "c1" && !e.idkNow && v.segments[1].current, "it comes round last as a plain card");
    check(v.draft === "", "…with an empty box: answered from memory, not from the own-words step");
    answer(e, "h2o");
    v = e.view();
    check(ALL3(v) && v.suggest === null, "on the replay all three are allowed");
    e.rate("got_it");
    v = e.view();
    check(v.phase === "end" && v.end.line1 === "5 of 5 secured" && v.headline === "5 of 5 right",
          "the headline counts THIS pass (5, not 6 — the replay); the end screen counts secured (also 5)");
    const subs = evs().filter((x) => x.type === "answer_submitted" && x.card === "c1");
    check(subs.length === 3 && subs[0].idk && subs[0].answer === "I don't know" && subs[1].own_words && subs[1].answer === "h2o",
          "events: answer_submitted 'I don't know' (idk), then the own words (own_words)");
    check(evs().filter((x) => x.type === "revealed" && x.card === "c1").length === 3, "each answer is revealed once");
  }

  // ── 12b. I don't know → ‹ Back → forward: still the learn state (M-1) ─
  {
    const { e } = await fresh();
    answer(e, "newton"); e.rate("got_it");
    e.idk();
    e.back();
    check(e.view().card.id === "c0" && !e.view().learn, "‹ Back from the learn state: the previous card, plain");
    answer(e, "newton"); e.rate("got_it");
    let v = e.view();
    check(v.card.id === "c1" && v.learn && v.learnAnswer === "H2O" && !e.canCheck(),
          "forward again: the I-don't-know card reopens in the learn state");
    e.setDraft("h2o"); e.check();
    v = e.view();
    check(v.suggest === null && ALL3(v), "…and its own words may be rated anything");
    e.rate("nearly");
    check(e.passIds.length === 6 && e.passIds[5] === "c1", "…and it is still replayed at the end of the pass");
    answer(e, "the force acting on an object due to gravity"); e.rate("got_it");
    answer(e, "f = ke"); e.rate("got_it");
    answer(e, "vector"); e.rate("got_it");
    v = e.view();
    check(v.card.id === "c1" && !v.learn, "the replay is a plain card");
  }

  // ── 12c. a reload keeps the I-don't-know card (S-c, now beside any pass) ─
  {
    const { S, e } = await fresh();
    answer(e, "newton"); e.rate("got_it");
    e.idk();
    await e.flush(); await tick(5);
    H._reset();                                   // the page reloads; localStorage survives
    const e2 = await H.open("A");
    let v = e2.view();
    check(v.card.id === "c1" && v.learn, "reload mid-learn: the card reopens in the learn state");
    e2.setDraft("h2o"); e2.check();
    check(ALL3(e2.view()), "reload mid-learn: all three allowed");
    e2.rate("nearly");
    check(e2.passIds[e2.passIds.length - 1] === "c1", "reload mid-learn: still replayed");
    await e2.flush(); await tick(5);
    H._reset();
    const e3 = await H.open("A");
    check(e3.passIds[e3.passIds.length - 1] === "c1" && e3.passIds.length === 6 && e3.view().pos === 3,
          "reload after the own-words rating: its replay is still to come, the pass carries on at card 3");
    H._reset(); localStorage.clear();              // another device: no I-don't-know record
    const e4 = await H.open("A");
    check(!e4.view().learn && e4.passIds.length === 5 && e4.view().pos === 3,
          "another device: the same place in the pass, no replay (decision 8)");
  }

  // ── 13. "I don't know" twice on one card → no third showing ─────────
  {
    const { e } = await fresh({ cards: FIVE.slice(0, 2) });
    e.idk(); e.setDraft("newton"); e.check(); e.rate("nearly");
    answer(e, "h2o"); e.rate("got_it");
    check(e.view().card.id === "c0", "c0 comes round");
    e.idk(); e.setDraft("newton"); e.check(); e.rate("nearly");
    const v = e.view();
    check(v.phase === "end" && e.passIds.length === 3 && v.end.line1 === "1 of 2 secured", "second I don't know: no third showing, the pass ends");
  }

  // ── 14 + 15. Try again: only the leftovers, the chips, a redo ────────
  {
    const { S, e } = await fresh();
    const evs = () => S.events.concat(e.pending);
    answer(e, "newton"); e.rate("got_it");            // c0 green
    answer(e, "water"); e.rate("not_yet");            // c1 grey
    answer(e, "the force acting on an object due to gravity"); e.rate("got_it");           // c2 green
    answer(e, "stretch"); e.rate("not_yet");          // c3 grey
    answer(e, "vector"); e.rate("got_it");            // c4 green
    let v = e.view();
    check(v.end.line1 === "3 of 5 secured" && v.end.button === "retry" && !v.end.secondary, "leftovers: '3 of 5 secured', Try again, no secondary");
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
    check(v.detour && v.card.id === "c2" && !v.revealed && v.draft === "the force acting on an object due to gravity" && v.chips[2].current,
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
    // ⊕ Mide, 4 Oct 2026 — "once secured, stays secured": c2 was Secured,
    // then re-rated Not yet through a redo. The rating is kept (history),
    // but c2 stays secured, so securing c1 and c3 finishes the deck.
    await e.flush(); await tick(5); await e.flush(); await tick(5);
    check(v.end.line1 === "5 of 5 secured" && v.end.button === "done" && v.end.secondary,
          "c2 stays secured after the redo's Not yet: 5 of 5 secured, Done + the Revise secondary");
    check(S.events.filter((x) => x.type === "session_finish").length === 1, "exactly ONE session_finish across the pass and the retry");
    const c2 = S.events.filter((x) => x.type === "rated" && x.card === "c2").map((x) => x.rating);
    check(c2.join() === "got_it,not_yet", "the later Not yet is still recorded as an event (" + c2 + ")");
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

  // ══ ⊕ STAGE D — progress is never lost (STAGE-D-PLAN.md §2.9) ═════════
  const MIN = 60 * 1000;
  const STORE = "mrbadmusai.fchw.v1.";
  const deck5 = () => FIVE.map((c, i) => ({ id: "c" + i, position: i, last: null, secured: false }));
  // ⊕ MRB-354 — `session` defaults to one shared sitting ("s"): most of
  // these rows don't care about the grouping key at all. Tests that DO
  // (secured's own session+phase grouping) pass distinct session ids.
  const row = (card, rating, at, phase, session) =>
    ({ card_id: card, rating, phase: phase || "review", rated_at: at, session_id: session == null ? "s" : session });
  const rightOf = (r) => Object.keys(r.pass).filter((k) => r.pass[k].rating === "got_it").length;

  // ── 17. reconstruct, pure ───────────────────────────────────────────
  {
    const now = Date.now();
    const R = (rows, mode, idk) => H.reconstruct(rows, deck5(), mode || "review", now, idk);
    // (a) 3 of 5 rated
    let r = R([row("c0", "got_it", now - 3 * MIN), row("c1", "not_yet", now - 2 * MIN), row("c2", "got_it", now - MIN)]);
    check(r && r.stage === "review" && r.round.n === 1 && r.round.done.join() === "c0,c1,c2" && rightOf(r) === 2 &&
          r.ended === null && r.order.join() === "c0,c1,c2,c3,c4", "17a: 3 of 5 → round 1, done in rated order, 2 right, not ended");
    // (b) all 5, 2 not right, last 5 min ago
    const five = [row("c0", "got_it", now - 9 * MIN), row("c1", "not_yet", now - 8 * MIN), row("c2", "got_it", now - 7 * MIN),
                  row("c3", "not_yet", now - 6 * MIN), row("c4", "got_it", now - 5 * MIN)];
    r = R(five);
    check(r && r.ended === "retry" && r.round.n === 1 && r.round.done.length === 5 && rightOf(r) === 3,
          "17b: round 1 complete, not all right, 5 min ago → the Try again screen");
    // (c) the same an hour on
    const old = five.map((x) => Object.assign({}, x, { rated_at: x.rated_at - 56 * MIN }));
    check(R(old) === null, "17c: the same, last rating 61 min ago → a new pass (null)");
    // (d) round 2 begun 5 min after round 1 finished
    r = R(five.concat([row("c1", "got_it", now)]));
    check(r && r.round.n === 2 && r.round.targets.join() === "c1,c3" && r.round.done.join() === "c1" &&
          rightOf(r) === 4 && !r.pass.c3 && r.ended === null, "17d: round 2 — targets the 2 leftovers, 1 done, 4 right, c3 to come");
    // (e) a green-chip redo inside round 2
    r = R(five.concat([row("c1", "got_it", now - MIN), row("c0", "not_yet", now)]));
    check(r && r.round.n === 2 && r.round.done.join() === "c1" && r.round.targets.join() === "c1,c3" &&
          r.pass.c0.rating === "not_yet" && rightOf(r) === 3, "17e: a redo of a green card changes the pass, not the round");
    // (f) all right, then one later rating
    const all = ["c0", "c1", "c2", "c3", "c4"].map((c, i) => row(c, "got_it", now - (20 - i) * MIN));
    r = R(all.concat([row("c2", "nearly", now - MIN)]));
    check(r && r.round.n === 1 && r.round.done.join() === "c2" && Object.keys(r.pass).join() === "c2" && r.order[0] === "c2",
          "17f: all Got it ends the pass; the open pass is the one later rating");
    check(R(all) === null, "17f: all Got it and nothing since → a new pass");
    // (g) make mode
    r = R([row("c0", "got_it", now - 3 * MIN, "make"), row("c1", "not_yet", now - 2 * MIN, "make"), row("c2", "got_it", now - MIN, "make")], "make");
    check(r && r.stage === "make" && r.round.done.join() === "c0,c1,c2" && r.order.join() === "c0,c1,c2,c3,c4",
          "17g: make, 3 of 5 written → the writing pass, 3 done");
    r = R(["c0", "c1", "c2", "c3", "c4"].map((c, i) => row(c, "got_it", now - (9 - i) * MIN, "make")), "make");
    check(r && r.stage === "review" && r.round.n === 1 && r.round.done.length === 0 && Object.keys(r.pass).length === 0,
          "17g: make, all written, no review yet → review round 1, nothing done");
    // (h) a card rated twice inside round 1
    r = R([row("c0", "got_it", now - 3 * MIN), row("c1", "not_yet", now - 2 * MIN), row("c0", "not_yet", now - MIN)]);
    check(r && r.round.n === 1 && r.round.done.join() === "c0,c1" && r.pass.c0.rating === "not_yet" && r.ended === null,
          "17h: a card rated twice in round 1 counts once toward cover; the latest rating stands");
    // (h') an "I don't know" replay after the round finished stays in round 1 (on the device that knows)
    const idkRun = [row("c0", "got_it", now - 9 * MIN), row("c1", "nearly", now - 8 * MIN), row("c2", "got_it", now - 7 * MIN),
                    row("c3", "not_yet", now - 6 * MIN), row("c4", "got_it", now - 5 * MIN), row("c1", "got_it", now - 4 * MIN)];
    r = R(idkRun, "review", { seen: { c1: true } });
    check(r && r.ended === "retry" && r.round.n === 1 && rightOf(r) === 4, "17h': the I-don't-know replay belongs to round 1 → Try again screen, 4 right");
    r = R(idkRun);
    check(r && r.round.n === 2 && r.round.done.join() === "c1", "17h': without the device's record it reads as round 2 begun");
    // (h'') a record from another round or an earlier pass is not this replay
    r = R(idkRun, "review", { seen: { c1: true }, n: 2, at: now - 4 * MIN });
    check(r && r.round.n === 2 && r.round.done.join() === "c1", "17h'': a record written in round 2 does not fold a rating into round 1");
    r = R(idkRun, "review", { seen: { c1: true }, n: 1, at: now - 3 * 60 * MIN });
    check(r && r.round.n === 2 && r.round.done.join() === "c1", "17h'': a record from before this pass began does not either");
    r = R(idkRun, "review", { seen: { c1: true }, n: 1, at: now - 9 * MIN - 30 * 1000 });
    check(r && r.ended === "retry" && r.round.n === 1, "17h'': one written just before the pass's first rating (the first card was the I-don't-know) still counts");
    // (i) nothing
    check(R([]) === null && H.reconstruct(null, deck5(), "review", now) === null, "17i: no rows / no read → null");
  }

  // ── 18. × mid-pass, then reopen: the same place (reverses S-b) ───────
  {
    const { S, e } = await fresh();
    answer(e, "newton"); e.rate("got_it");
    answer(e, "water"); e.rate("not_yet");
    e.finish();
    H.close();
    await tick(5); await e.flush(); await tick(5);
    check(S.events.some((x) => x.type === "session_finish"), "18: × still sends session_finish (A13)");
    const again = await H.open("A");
    const v = again.view();
    check(v.headline === "1 of 5 right" && v.pos === 3 && v.canBack &&
          v.segments.map((g) => g.state).join() === "right,answered,todo,todo,todo" && v.segments[2].current,
          "18: reopening after × lands on card 3 at '1 of 5 right' (" + v.headline + ", pos " + v.pos + ")");

    // ── 19. the phone dies: another device, nothing on it ──────────────
    again.setDraft("typed on the dead phone");
    H._reset(); localStorage.clear();
    const e2 = await H.open("A");
    const v2 = e2.view();
    check(v2.headline === "1 of 5 right" && v2.pos === 3 && v2.draft === "",
          "19: a new device lands on card 3 at '1 of 5 right'; the other phone's half-typed words are not here");

    // ── 20. offline, then a reload on the same device ──────────────────
    S.fail = true;
    answer(e2, "the force acting on an object due to gravity"); e2.rate("got_it");
    await tick(5);
    check(e2.pending.length > 0 && S.rows.length === 2, "20: offline — the rating waits on the device");
    S.fail = false;
    H._reset();                                   // reload; localStorage kept
    const e3 = await H.open("A");
    const v3 = e3.view();
    check(S.rows.length === 3 && v3.pos === 4 && v3.headline === "2 of 5 right" && v3.segments[2].state === "right",
          "20: the queue is sent first, then the pass lands on card 4 with card 3 counted (" + v3.headline + ")");
  }

  // ── 21. the Try again screen survives a reopen, for an hour ─────────
  {
    const { S, e } = await fresh();
    const script = { c0: ["newton", "got_it"], c1: ["water", "not_yet"], c2: ["the force acting on an object due to gravity", "got_it"],
                     c3: ["stretch", "not_yet"], c4: ["vector", "got_it"] };
    for (let k = 0; k < 5; k++) { const id = e.view().card.id; answer(e, script[id][0]); e.rate(script[id][1]); }
    await tick(5); await e.flush(); await tick(5);
    H.close();
    let a = await H.open("A");
    let v = a.view();
    check(v.phase === "end" && v.end.button === "retry" && v.end.line1 === "3 of 5 secured",
          "21: reopened inside the hour → the same Try again screen, '3 of 5 secured'");
    a.retry();
    v = a.view();
    check(a.passIds.join() === "c1,c3" && v.chips.filter((g) => g.state === "right").length === 3 && v.card.id === "c1",
          "21: Try again → a queue of 2 in first-pass order, 3 green chips");
    H._reset(); localStorage.clear();
    a = await H.open("A");
    check(a.view().phase === "end" && a.view().end.line1 === "3 of 5 secured", "21: …and on another device too (secured is read from the server's rows, not a local record)");
    S.shift(61 * MIN);
    H.close();
    a = await H.open("A");
    v = a.view();
    check(v.headline === "0 of 5 right" && v.pos === 1 && v.segments.every((g) => g.state === "todo"),
          "21: an hour on → a new pass, '0 of 5 right', 5 to do (" + v.headline + ")");
  }

  // ── 22. reopened mid-retry: the chips view, on what is left ─────────
  {
    const { S, e } = await fresh();
    const script = { c0: ["newton", "got_it"], c1: ["water", "not_yet"], c2: ["the force acting on an object due to gravity", "got_it"],
                     c3: ["stretch", "not_yet"], c4: ["vector", "got_it"] };
    for (let k = 0; k < 5; k++) { const id = e.view().card.id; answer(e, script[id][0]); e.rate(script[id][1]); }
    e.retry();
    answer(e, "h2o"); e.rate("got_it");
    await tick(5); await e.flush(); await tick(5);
    for (const other of [false, true]) {
      H.close();
      if (other) { H._reset(); localStorage.clear(); }
      const a = await H.open("A");
      const v = a.view();
      check(v.retry && a.retries === 1 && a.passIds.join() === "c3" && v.card.id === "c3" && v.headline === "4 of 5 right" &&
            v.chips.length === 5 && v.chips[1].state === "right" && v.chips[3].state === "todo",
            "22: mid-retry reopen" + (other ? " (another device)" : "") + " → chips, retries 1, queue [c3], '4 of 5 right' (" + v.headline + ")");
    }
    check(S.sittings >= 1, "22: sittings " + S.sittings);
  }

  // ── 23. ⊕ MRB-354 — all secured → Done → reopen: STRAIGHT BACK TO DONE,
  //        never a fresh pass (secured never un-secures, so there is
  //        nothing left for a fresh pass to ask). "Revise flashcards one
  //        more time" is the only way into one, voluntarily. ────────────
  {
    const { S, e } = await fresh();
    const good = { c0: "newton", c1: "h2o", c2: "the force acting on an object due to gravity", c3: "f = ke", c4: "vector" };
    for (let k = 0; k < 5; k++) { const id = e.view().card.id; answer(e, good[id]); e.rate("got_it"); }
    await tick(5); await e.flush(); await tick(5);
    check(e.view().end.button === "done" && e.view().end.secondary, "23: all secured → Done + the Revise secondary");
    e.finish(); H.close();
    await tick(5);
    const a = await H.open("A");
    check(a.view().phase === "end" && a.view().end.button === "done" && a.view().end.line1 === "5 of 5 secured" && !a.passIds.length,
          "23: reopening an already-fully-secured deck → straight to Done, no fresh pass");
    check(S.events.filter((x) => x.type === "session_finish").length === 1, "23: session_finish sent once");
    a.again();
    check(a.view().phase === "review" && a.view().headline === "0 of 5 right" && a.view().secured === 5,
          "23: 'Revise flashcards one more time' is the only way into a fresh pass — still 5 of 5 secured throughout");
  }

  // ── 24. make mode: a card written but not rated when the phone died ──
  {
    const { S, e } = await fresh({ mode: "make" });
    answer(e, "newton"); e.rate("got_it");
    answer(e, "h2o"); e.rate("got_it");
    answer(e, "the force acting on an object due to gravity");   // made (answer_submitted), not rated
    await tick(5); await e.flush(); await tick(5);
    check(S.cards[2].made && S.cards[2].mine === "the force acting on an object due to gravity", "24: the server has card 3's answer");
    H._reset(); localStorage.clear();              // the phone died; another device
    const a = await H.open("A");
    let v = a.view();
    check(v.phase === "make" && v.card.id === "c2" && !v.revealed && v.draft === "the force acting on an object due to gravity" && v.pos === 3 && v.headline === "2 of 5 right",
          "24: card 3 reopens in state A with its stored answer in the box (" + v.draft + ", pos " + v.pos + ")");
    a.check(); a.rate("got_it");
    check(a.view().card.id === "c3", "24: Check → rate → card 4");
    answer(a, "f = ke"); a.rate("got_it");
    answer(a, "vector"); a.rate("got_it");
    v = a.view();
    // ⊕ MRB-354 — every card got_it from the writing pass alone → Done at
    // once, no forced review pass (the OLD "again" bucket is gone).
    check(v.phase === "end" && v.end.button === "done" && v.end.secondary && v.end.line1 === "5 of 5 secured",
          "24: the writing pass secures every card → Done + Revise, straight away");
    await tick(5); await a.flush(); await tick(5);
    H._reset();
    const b = await H.open("A");
    check(b.view().phase === "end" && b.view().end.button === "done", "24: reopened after Done → straight back to Done, no fresh pass");
    b.again();
    check(b.view().phase === "review" && b.view().headline === "0 of 5 right" && b.view().secured === 5,
          "24: 'Revise flashcards one more time' is the only way into a review pass — still 5 of 5 secured");
  }

  // ── 25. every answer is sent at once; the keepalive leaves the queue ──
  {
    const { S, e } = await fresh();
    answer(e, "newton");
    await tick(5);
    e.rate("got_it");
    await Promise.resolve(); await Promise.resolve(); await Promise.resolve();
    check(S.events.some((x) => x.type === "rated" && x.card === "c0"), "25: a rating reaches the transport before the next macrotask");
    const ka = [];
    H.transportKeepalive = (id, evs) => { ka.push.apply(ka, evs); };
    S.fail = true;
    answer(e, "water"); e.rate("not_yet");
    await tick(5);
    const held = e.pending.map((x) => x.id).join();
    globalThis.document = { visibilityState: "hidden" };
    e.visibility();
    delete globalThis.document;
    check(ka.length > 0 && ka.some((x) => x.type === "rated" && x.card === "c1") && e.pending.map((x) => x.id).slice(0, -1).join() === held,
          "25: hidden → the keepalive gets the pending batch; the queue is unchanged");
    S.fail = false;
    await S.transport("A", ka);                   // the keepalive landed
    const before = S.events.length;
    await e.flush(); await tick(5);
    const ids = S.events.map((x) => x.id);
    check(new Set(ids).size === ids.length && S.rows.length === 2 && e.pending.length === 0,
          "25: the next flush resends the same ids and the server keeps one of each (" + (S.events.length - before) + " new)");
    const many = [];
    H.transportKeepalive = (id, evs) => { many.push(evs.length); };
    S.fail = true;
    for (let k = 0; k < 40; k++) { e.visibility(); }
    e.flushBeacon();
    check(many.length === 1 && many[0] <= 60, "25: a keepalive batch is at most 60 events (" + many + ")");
    S.fail = false;
    H.transportKeepalive = null;
  }

  // ── 26. half-typed words survive a reload ───────────────────────────
  {
    const { e } = await fresh();
    e.setDraft("half");
    H._reset();
    const a = await H.open("A");
    check(a.view().card.id === "c0" && a.view().draft === "half", "26: a reload keeps the half-typed answer (" + a.view().draft + ")");
    a.setDraft("newton"); a.check(); a.rate("got_it");
    check(localStorage.getItem(STORE + "draft.A") === null, "26: rated → the card's saved draft is gone");
  }

  // ── 27. retired things stay retired ─────────────────────────────────
  {
    const raw = fs.readFileSync(path.join(ROOT, "shared/flashcard-homework.js"), "utf8");
    ["afterWriting", "RESUME_MS", "newSitting"].forEach((w) =>
      check(raw.indexOf(w) < 0, "27: absent from the engine source: " + w));
  }

  // ══ ⊕ 1 Oct 2026 — "finished the homework" (Mide's ruling: reaching the
  //    engine's own Done screen = done, on both the pupil and teacher
  //    side). `finishedAt()` reads that fact from the pupil's own ratings,
  //    with no live Engine; `onFinish` fires once the settled Done screen
  //    has told the page. See docs/experience/DESIGN-PORT-REPORT.md,
  //    "Follow-up 1 Oct", for the rule and the write it feeds. ═══════════

  // ── 28. ⊕ MRB-354 — finishedAt agrees with endPass().all: every card
  //        secured (across the leftovers screen AND its retry, the SAME
  //        sitting) is what finishes the deck, not a round or a pass. ────
  {
    const { S, e } = await fresh();
    answer(e, "newton"); e.rate("got_it");
    answer(e, "water"); e.rate("not_yet");
    check(H.finishedAt(S.reviews(), S.cards) === null,
          "28: finishedAt null before every card is secured (1 of 5)");
    answer(e, "the force acting on an object due to gravity"); e.rate("got_it");
    answer(e, "f = ke"); e.rate("got_it");
    answer(e, "vector"); e.rate("got_it");
    let v = e.view();
    check(v.end.button === "retry" && H.finishedAt(S.reviews(), S.cards) === null,
          "28: the leftovers screen (endPass().all === false): finishedAt agrees, null (4 of 5)");
    e.retry();
    answer(e, "h2o"); e.rate("got_it");                 // secures the last card
    await e.flush(); await tick(5);
    v = e.view();
    check(v.end.button === "done", "28: securing the last card completes the pass (endPass().all === true)");
    const hit = H.finishedAt(S.reviews(), S.cards);
    const lastRow = S.rows[S.rows.length - 1];
    check(!!hit && hit.at === lastRow.rated_at && lastRow.card_id === "c1",
          "28: finishedAt agrees — the moment c1 (the last unsecured card) got got_it");
  }

  // ── 29. ⊕ MRB-354 — secured needs ONE got_it rating, in EITHER phase, in
  //        ANY sitting — no pairing with the other phase, no second sitting.
  //        A card secured in the make (writing) phase alone is enough; the
  //        whole deck can finish without a review pass ever running. ─────
  {
    const now = Date.now();
    const makeOnly = ["c0", "c1", "c2", "c3", "c4"]
      .map((c, i) => row(c, "got_it", now - (5 - i) * MIN, "make"));
    check(H.finishedAt(makeOnly, deck5()) !== null,
          "29: every card got_it in the WRITING phase alone → finished, no review pass needed");
    const mixedPhases = ["c0", "c1"].map((c, i) => row(c, "got_it", now - (5 - i) * MIN, "make"))
      .concat(["c2", "c3", "c4"].map((c, i) => row(c, "got_it", now - (3 - i) * MIN, "review")));
    check(H.finishedAt(mixedPhases, deck5()) !== null,
          "29: a mix of make-phase and review-phase got_it rows, one each, still finishes");
    const fourOfFive = ["c0", "c1", "c2", "c3"].map((c, i) => row(c, "got_it", now - (4 - i) * MIN));
    check(H.finishedAt(fourOfFive, deck5()) === null, "29: 4 of 5 secured → not finished");
  }

  // ── 30. ⊕ MRB-354 — a LATER rating, in a DIFFERENT sitting, can only ADD
  //        a new group; it never removes an existing one, so it cannot
  //        un-finish a pupil. finishedAt has no round or hour-gap logic at
  //        all any more — this is just "every card has a counting row". ──
  {
    const now = Date.now();
    const allRight = ["c0", "c1", "c2", "c3", "c4"]
      .map((c, i) => row(c, "got_it", now - (20 - i) * MIN, "review", "sA"));
    const firstHit = H.finishedAt(allRight, deck5());
    check(!!firstHit && firstHit.at === allRight[4].rated_at,
          "30: finishedAt fires at the last card's own got_it row");
    const later = allRight.concat([row("c2", "nearly", now, "review", "sB")]);   // a DIFFERENT sitting
    check(H.reconstruct(later, deck5(), "review", now) !== null,
          "30: sanity — reconstruct opens a fresh pass after the later rating");
    const stillHit = H.finishedAt(later, deck5());
    check(!!stillHit && stillHit.at === firstHit.at,
          "30: finishedAt is unchanged — a new sitting's rating forms its OWN group and cannot remove an earlier one");
  }

  // ── 31. ⊕ Mide, 4 Oct 2026 — once secured, stays secured: a ‹ Back to a
  //        secured card and a lower rating in the SAME sitting never takes
  //        it back; the deck's finish is the moment the LAST card was first
  //        secured. ─────────────────────────────────────────────────────
  {
    const now = Date.now();
    const sameSitting = ["c0", "c1", "c2", "c3"].map((c, i) => row(c, "got_it", now - (10 - i) * MIN, "review", "s1"))
      .concat([row("c4", "got_it", now - 5 * MIN, "review", "s1"),
               row("c4", "not_yet", now - 4 * MIN, "review", "s1")]);   // ‹ Back, answered wrong
    const hit = H.finishedAt(sameSitting, deck5());
    check(!!hit && hit.at === now - 5 * MIN, "31: c4 stays secured — finished when c4 was first secured");
    check(!!H.securedInfo(sameSitting, deck5()).secured.c4, "31: securedInfo agrees — c4 is in the secured set");
    const later = sameSitting.concat([row("c4", "got_it", now, "review", "s2")]);
    check(H.finishedAt(later, deck5()).at === now - 5 * MIN, "31: a later got_it does not move the finish");
  }

  // ── 31b. ⊕ Mide, 4 Oct 2026 — revising after Done and getting a card
  //        wrong never un-secures it; the wrong answer is still recorded. ─
  {
    const { S, e } = await fresh();
    const good = { c0: "newton", c1: "h2o", c2: "the force acting on an object due to gravity", c3: "f = ke", c4: "vector" };
    for (let k = 0; k < 5; k++) { const id = e.view().card.id; answer(e, good[id]); e.rate("got_it"); }
    await tick(5); await e.flush(); await tick(5);
    check(e.view().end.line1 === "5 of 5 secured", "31b: all secured");
    e.again();
    const first = e.view().card.id;
    answer(e, "the"); e.rate("not_yet");          // wrong this time
    check(e.securedCount() === 5 && e.securedMap()[first], "31b: a wrong answer in a Revise pass leaves the card secured");
    for (let k = 0; k < 4; k++) { const id = e.view().card.id; answer(e, good[id]); e.rate("got_it"); }
    await tick(5); await e.flush(); await tick(5);
    check(e.view().end.line1 === "5 of 5 secured" && e.view().end.button === "done", "31b: the Revise pass still ends 5 of 5 secured, Done");
    const rs = S.events.filter((x) => x.type === "rated" && x.card === first).map((x) => x.rating);
    check(rs.join() === "got_it,not_yet", "31b: the later Not yet is recorded (" + rs + ")");
  }

  // ── 32. Api.onFinish fires once the Done screen settles, and only then ─
  {
    const { e } = await fresh();
    let fired = [];
    H.onFinish = (id) => { fired.push(id); };
    const good = { c0: "newton", c1: "h2o", c2: "the force acting on an object due to gravity", c3: "f = ke", c4: "vector" };
    for (let k = 0; k < 5; k++) { const id = e.view().card.id; answer(e, good[id]); e.rate("got_it"); }
    await e.flush(); await tick(5); await e.flush(); await tick(5);
    check(e.view().end.button === "done", "32: all right → Done");
    check(fired.length === 1 && fired[0] === "A", "32: onFinish fired exactly once, with the assignment id (" + fired.length + ")");
    await e.flush(); await tick(5); e.view();
    check(fired.length === 1, "32: a later flush with nothing left to settle does not refire onFinish");
    H.onFinish = null;
  }
  {
    const { e } = await fresh();
    let fired = 0;
    H.onFinish = () => { fired++; };
    answer(e, "newton"); e.rate("not_yet");
    answer(e, "water"); e.rate("not_yet");
    answer(e, "gravity"); e.rate("not_yet");
    answer(e, "stretch"); e.rate("not_yet");
    answer(e, "vector"); e.rate("not_yet");
    await e.flush(); await tick(5);
    check(e.view().end.button === "retry" && fired === 0, "32b: the leftovers (Try again) screen never fires onFinish");
    H.onFinish = null;
  }

  // ── 33. ⊕ MRB-354 (superseded the old MUST-FIX) — finishedAt is a FLAT
  //        fact with no round or hour-gap logic at all any more: an old
  //        got_it row from an ABANDONED round (one reconstruct() itself
  //        would start a fresh pass over — see 17c) still counts, because
  //        under the new rule it was never un-secured. Securing just the
  //        leftover card, however much later, finishes the deck — this is
  //        the INTENDED behaviour (Mide: "probably has that knowledge
  //        secured already"), not the bug the old round-walk had to guard
  //        against. ──────────────────────────────────────────────────────
  {
    const now = Date.now();
    const deck = deck5();
    // Sitting 1: c0-c3 Got it, c4 Not yet → the leftovers ("Try again")
    // screen. Walks away for over an hour — reconstruct would start a
    // fresh pass (test 17c's own rule, unchanged).
    const sitting1 = [row("c0", "got_it", now - 100 * MIN), row("c1", "got_it", now - 99 * MIN),
                      row("c2", "got_it", now - 98 * MIN), row("c3", "got_it", now - 97 * MIN),
                      row("c4", "not_yet", now - 96 * MIN)];
    check(H.finishedAt(sitting1, deck) === null, "33: c4 is the only unsecured card → not finished");
    check(H.reconstruct(sitting1, deck, "review", now) === null,
          "33: sanity — reconstruct starts a fresh pass (stale, unaffected by MRB-354)");
    // The pupil gets c4 right, later, in what reconstruct() considers a
    // brand-new pass. The deck finishes anyway — c0-c3's old got_it rows
    // are still good.
    const finished = sitting1.concat([row("c4", "got_it", now)]);
    const hit = H.finishedAt(finished, deck);
    check(!!hit && hit.at === now, "33: securing the leftover card (even in a 'fresh' pass) finishes the deck, at its own time");
    const rc = H.reconstruct(finished, deck, "review", now + MIN);
    check(rc && rc.stage === "review" && Object.keys(rc.pass).length === 1 && rc.ended === null,
          "33: reconstruct still sees its own fresh pass, 1 of 5 rated so far, not ended — the two never need to agree "
          + "on ROUNDS for finishedAt to agree with them on DONE");
  }

  // ── 34. ⊕ 8 Oct 2026 (round 3) — SECURED HAS A FLOOR: realAttempt ────
  //        Real production-deck model answers; every "opens" row is a
  //        correct-or-honest attempt in the pupil's own words, every
  //        "greyed" row is keyboard mash, a blank, "idk" or filler.
  {
    const RA = H.realAttempt;
    check(typeof RA === "function", "34: realAttempt is exposed on the module's test surface");
    const OPEN = [
      ["Plankton died, were buried under sediment and compressed via heat and pressure over millions of years",
        ["plants died, got buried, heat and pressure"]],
      ["Joules (J)", ["J", "j", "joules", "joule"]],
      ["One", ["1", "one"]],
      ["Its resistance decreases.", ["it goes down", "decreases", "gets lower"]],
      ["Use limewater, it turns cloudy", ["milky", "goes cloudy"]],
      ["Lack of oxygen", ["not enough O2", "oxygen"]],
      ["It increases by a factor of 4", ["quadruples", "x4", "4 times bigger"]],
      ["F GPE = mgh\nI 14700 = m x 9.8 x 25\nF 14700/(9.8 x 25) = m\nA m = 60 kg", ["60kg", "60 kg", "60"]],
      ["F P = E/t\nI 2000 = E/5\nF 2000 x (5 x 60) = E\nA E = 600000 J", ["600,000", "600 000 J", "600000"]],
      ["58 500 J", ["58500", "J", "joules"]],
      ["Melt or boil it, the substance will melt or boil at a specific temperature", ["boiling point"]],
      ["A shared pair of electrons", ["electrons are shared"]],
      ["Contains at least one carbon-carbon double bond (C=C)", ["C=C", "double bond"]],
      ["Calculate the gradient (change in y/change in x)", ["gradient", "work out the slope change in y"]],
    ];
    let opened = 0, total = 0;
    OPEN.forEach(([model, pupils]) => pupils.forEach((p) => {
      total++;
      if (RA(p, model)) { opened++; } else { check(false, `34: ${JSON.stringify(p)} must OPEN against ${JSON.stringify(model.slice(0, 40))}`); }
    }));
    check(opened === total, `34: all ${total} real attempts open Secured (${opened})`);
    const MASH = ["xxgpdt", "asdf", "hjkl qwerty", "idk", "I don't know", "dunno", "x", "the", "a of the", "?", "...",
                  "kkkkkk", "", "   ", "no idea", "zzz", "fgfgfg hhh", "qwertyuiop", "it is a thing", "yes", "lol"];
    const MODELS = OPEN.map((o) => o[0]);
    let greyed = 0, gtotal = 0;
    MASH.forEach((p) => MODELS.forEach((m) => {
      gtotal++;
      if (!RA(p, m)) { greyed++; } else { check(false, `34: ${JSON.stringify(p)} must stay GREYED against ${JSON.stringify(m.slice(0, 40))}`); }
    }));
    check(greyed === gtotal, `34: all ${gtotal} mash/blank/filler pairs stay greyed (${greyed})`);
    check(!RA(null, "Joules (J)") && !RA(undefined, "x"), "34: null / undefined pupil text never opens it");
    check(RA("a joule", "Joules (J)") && RA("Newtons", "The newton (N)"), "34: unit words match across singular / plural");
    console.log(`  realAttempt: ${total} real attempts open, ${gtotal} mash pairs stay greyed`);
  }

  // ── 35. the floor in the engine: mash, a real word, "I don't know" ──
  {
    const { e } = await fresh({ cards: TEN });
    answer(e, "asdf kkkk");                       // mash
    let v = e.view();
    check(v.revealed && !v.allowed.got_it && v.allowed.nearly && v.allowed.not_yet,
          "35: after a mash Check Secured is greyed, Nearly / Not yet are open");
    const id0 = v.card.id;
    e.rate("got_it");
    check(e.view().card.id === id0 && e.view().revealed && !e.securedMap()[id0],
          "35: rate('got_it') (the 3 key, the swipe) does nothing while floored");
    e.rate("not_yet");                            // the mash goes Not yet
    answer(e, "hydrocarbon");                     // card 2 (a hydrocarbon): one real word
    check(e.view().allowed.got_it, "35: one real word from the model answer opens Secured");
    e.rate("got_it");
    check(e.securedMap().c1 === true, "35: and it secures the card");
    // "I don't know" → model answer → own words: the same floor, on the own-words text
    e.idk();
    check(!e.view().revealed && !e.view().allowed.got_it, "35: nothing to rate before the own-words Check");
    e.setDraft("zzzz qqqq"); e.check();
    check(e.view().revealed && !e.view().allowed.got_it && e.view().allowed.nearly,
          "35: after idk, mashed own words keep Secured greyed");
    e.rate("nearly");
    e.idk();
    e.setDraft("CnH2n"); e.check();
    check(e.view().allowed.got_it, "35: after idk, own words from the model answer open Secured");
    // the crude-oil card in the pupil's own words (Mide's test)
    const { e: e2 } = await fresh({ cards: TEN });
    e2.idk();
    e2.setDraft("plants died, got buried, heat and pressure"); e2.check();
    check(e2.view().allowed.got_it, "35: crude oil, own words after 'I don't know' → Secured opens");
    // the verdict chip is untouched: Wrong verdict + a real attempt still opens it
    const { e: e3 } = await fresh({ cards: TEN });
    H.modelCheck = () => Promise.resolve("no");
    answer(e3, "plankton, I think");
    await tick(5);
    check(e3.view().chip === "Wrong" && e3.view().allowed.got_it, "35: the chip is still only a hint — Wrong chip, real attempt, Secured open");
    H.modelCheck = null;
  }

  // ── 36. ⊕ the Mr Badmus nudge ───────────────────────────────────────
  {
    // run a 10-card deck to Done. `shaky[i]` → "idk" | "partial" | "late-partial" | undefined.
    async function runDeck(shaky) {
      const o = await fresh({ cards: TEN });
      const e = o.e;
      H.modelWaitMs = 4000;
      const kinds = {};
      H.modelCheck = (aid, cid, ans) => new Promise((r) => {
        const kind = kinds[ans] || "match";
        setTimeout(() => r(kind === "match" ? "match" : "partial"), kind === "late-partial" ? 40 : 1);
      });
      let guard = 0;
      const seen = {};
      while (e.view().card && guard++ < 60) {
        const i = Number(e.view().card.id.slice(1));
        const kind = shaky[i];
        const word = TEN[i].answer.slice(0, 12) + " ok";
        if (kind === "idk" && !seen[i]) { seen[i] = true; e.idk(); }
        const typed = kind === "partial" || kind === "late-partial" ? word + " partly" : word;
        if (kind === "partial" || kind === "late-partial") { kinds[typed] = kind; }
        e.setDraft(typed); e.check();
        if (kind === "partial") { await tick(10); }
        e.rate("got_it");
      }
      return o;
    }
    let o = await runDeck({ 0: "idk", 3: "idk", 6: "idk" });
    check(o.e.view().end && o.e.view().end.button === "done" && o.e.view().end.nudge === true,
          "36: 10 cards, 3 'idk then secured' → end.nudge true");
    check(o.e.view().end.line1 === "10 of 10 secured", "36: the nudge never changes the score or blocks Done");
    o = await runDeck({ 0: "idk", 3: "idk" });
    check(o.e.view().end.line1 === "10 of 10 secured" && o.e.view().end.nudge === false, "36: only 2 idk-secured → no nudge");
    o = await runDeck({ 0: "idk", 3: "idk", 5: "partial" });
    check(o.e.view().end.nudge === true, "36: 2 idk + 1 secured with a Nearly verdict → nudge");
    o = await runDeck({});
    check(o.e.view().end.nudge === false, "36: a clean run → no nudge");
    // a late verdict landing AFTER the card was rated still counts, and redraws the end screen
    o = await runDeck({ 0: "idk", 3: "idk", 9: "late-partial" });
    check(o.e.view().end && o.e.view().end.nudge === false, "36: the verdict has not landed yet → not counted yet");
    let ticks = 0; o.e.onChange = () => { ticks++; };
    await tick(80);
    check(o.e.view().end.nudge === true && ticks > 0, "36: a late verdict landing after rating counts, and redraws the end screen");
    // persistence: a reopen of the finished deck keeps the run
    await o.e.flush(); await tick(5); await o.e.flush();
    H._reset();
    H.transport = o.S.transport; H.resumeRead = () => Promise.resolve(o.S.reviews()); H.modelCheck = null;
    const e2 = await H.open("A");
    const v2 = e2.view();
    check(v2.end && v2.end.button === "done" && v2.end.nudge === true,
          "36: reopening the finished deck (all secured, stored shaky run) shows the nudge");
    // again() starts a new run and clears the record
    e2.again();
    check(e2.shakyCount() === 0 && !/"c0":true/.test(localStorage.getItem("mrbadmusai.fchw.v1.run.A") || ""),
          "36: again() clears the run record (in memory and on the device)");
    // a fresh run after again() with 0 shaky shows none
    let g = 0;
    while (e2.view().card && g++ < 40) {
      const i = Number(e2.view().card.id.slice(1));
      e2.setDraft(TEN[i].answer.slice(0, 12) + " ok"); e2.check(); e2.rate("got_it");
    }
    check(e2.view().end && e2.view().end.button === "done" && e2.view().end.nudge === false,
          "36: a fresh run after again() with 0 shaky shows no nudge");
    // storage that throws: the run lives in memory only and nothing breaks
    const realLS = globalThis.localStorage;
    const { e: e5 } = await fresh({ cards: TEN });
    Object.defineProperty(globalThis, "localStorage", { configurable: true, value: {
      getItem: () => { throw new Error("blocked"); }, setItem: () => { throw new Error("blocked"); },
      removeItem: () => { throw new Error("blocked"); }, clear: () => {} } });
    e5.idk(); e5.setDraft("plankton ok"); e5.check(); e5.rate("got_it");
    check(e5.shakyCount() === 1, "36: with storage blocked the run record still works in memory");
    Object.defineProperty(globalThis, "localStorage", { configurable: true, value: realLS });
    H.modelCheck = null;
  }

  console.log(`\n  ${passes} passed, ${fails} failed`);
  if (fails) { console.log("  FAIL — flashcard engine"); process.exit(1); }
  console.log("  PASS — flashcard engine (pupil flow)");
  process.exit(0);
})().catch((err) => { console.error(err); process.exit(1); });
