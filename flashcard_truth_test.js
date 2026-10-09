#!/usr/bin/env node
/* Flashcards round 3 (teacher) — shared/flashcard-truth.js, in Node, no
 * browser and no network. Effort is not understanding: a Done pupil who
 * pressed "I don't know" must read as unsure, a Done pupil with nothing to
 * flag reads "all confident", and a read that did not work reads as nothing.
 *
 *   node flashcard_truth_test.js
 */
"use strict";
const path = require("path");
const T = require(path.join(__dirname, "shared", "flashcard-truth.js"));

let fails = 0;
function check(ok, what, detail) {
  console.log("   " + (ok ? "PASS" : "FAIL") + "  " + what + (ok ? "" : "  - " + JSON.stringify(detail)));
  if (!ok) { fails++; }
}
const eq = (a, b) => JSON.stringify(a) === JSON.stringify(b);

const IDK = "I don't know";
const cards = [];
for (let i = 0; i < 10; i++) { cards.push({ id: "c" + (i + 1), position: i, question: "Q" + (i + 1) }); }
const pupils = [
  { pupil_id: "A", status: "done" }, { pupil_id: "B", status: "done" },
  { pupil_id: "C", status: "not_started" }];

/* A finished, got_it on all ten, but: IDK on c1 c2 c3 c4 (c4 twice), a
   Nearly typed answer on c5, a Wrong one on c6 → 6 of 10 unsure; c7 typed
   answer checked Right (not weak); c8 typed "I don't know" as a review answer
   without an event row (still idk-ish text → counts as idk too, so 7). To keep
   the headline 6 of 10, c8 is just Right. */
const idk = [
  { pupil_id: "A", card_id: "c1", type: "answer_submitted", answer: IDK },
  { pupil_id: "A", card_id: "c2", type: "answer_submitted", answer: IDK },
  { pupil_id: "A", card_id: "c3", type: "answer_submitted", answer: IDK },
  { pupil_id: "A", card_id: "c4", type: "answer_submitted", answer: IDK },
  { pupil_id: "A", card_id: "c4", type: "answer_submitted", answer: IDK },
  { pupil_id: "B", card_id: "c9", type: "answer_submitted", answer: IDK }   // B: idk on c9 only
];
const reviews = [];
cards.forEach((c) => {
  reviews.push({ pupil_id: "A", card_id: c.id, rating: "got_it", answer: "own words", answer_check: "match" });
  reviews.push({ pupil_id: "B", card_id: c.id, rating: "got_it", answer: "right answer", answer_check: "match" });
});
// A: c1-c4 re-typed after IDK and checked Right (still unsure through idk)
// A: c5 Nearly, c6 Wrong on top of the Right rows above
reviews.push({ pupil_id: "A", card_id: "c5", rating: "nearly", answer: "sort of", answer_check: "partial" });
reviews.push({ pupil_id: "A", card_id: "c6", rating: "not_yet", answer: "no idea really", answer_check: "no" });
// an unchecked and a blank answer are NOT weak
reviews.push({ pupil_id: "A", card_id: "c7", rating: "nearly", answer: "x", answer_check: "pending" });
reviews.push({ pupil_id: "A", card_id: "c8", rating: "nearly", answer: "", answer_check: "blank" });
// the IDK text itself with a "no" verdict is idk, never weak
reviews.push({ pupil_id: "B", card_id: "c10", rating: "not_yet", answer: IDK, answer_check: "no" });
// C: a row for a pupil who is not in the class, and one for a card not in the deck
reviews.push({ pupil_id: "Z", card_id: "c1", rating: "got_it", answer: "x", answer_check: "no" });
reviews.push({ pupil_id: "A", card_id: "gone", rating: "got_it", answer: "x", answer_check: "no" });

const t = T.build({ pupils, cards, idk, reviews, pupilCards: [], expectActivity: true });

check(!t.failed, "build succeeds");
check(T.unsure(t, "A") === 6, "pupil A: 6 unsure (4 idk + Nearly + Wrong)", T.unsure(t, "A"));
check(T.unsure(t, "B") === 2, "pupil B: idk on c9 and the IDK text on c10", T.unsure(t, "B"));
check(T.unsure(t, "C") === 0, "pupil C: none");
check(T.pupilLine(t, pupils[0], 10) === "· 6 of 10 unsure", "A's line", T.pupilLine(t, pupils[0], 10));
check(T.pupilLine(t, pupils[1], 10) === "· 2 of 10 unsure", "B's line", T.pupilLine(t, pupils[1], 10));
check(T.pupilLine(t, pupils[2], 10) === "", "C (not started): nothing extra");

// per-card counts, order
const rt = t.reteach;
// c1-c4 idk by A; c9 and c10 idk by B; c5 c6 weak by A. c4 counted once per pupil.
check(rt.length === 8, "8 cards have an unsure pupil (c7, c8 are not weak)", rt.map(r => r.id));
check(eq(rt.map(r => r.id), ["c1", "c2", "c3", "c4", "c9", "c10", "c5", "c6"]),
  "sort: unsure desc (all 1), idk desc, then position", rt.map(r => r.id));
const c4 = rt.find(r => r.id === "c4");
check(c4.unsure === 1 && c4.idk === 1 && c4.weak === 0 && c4.securedAnyway === 1,
  "c4: a pupil counts once however many times IDK was pressed; secured anyway", c4);
const c5 = rt.find(r => r.id === "c5");
check(c5.unsure === 1 && c5.idk === 0 && c5.weak === 1 && c5.securedAnyway === 1, "c5: Nearly/Wrong", c5);
const c10 = rt.find(r => r.id === "c10");
check(c10.idk === 1 && c10.weak === 0 && c10.securedAnyway === 1, "c10: IDK text with a verdict is idk, not weak", c10);
check(!rt.some(r => r.id === "gone") && rt.every(r => r.unsure > 0), "foreign pupil/card rows ignored");

// "all confident" needs Done AND zero unsure AND a successful read
const B2 = T.build({ pupils, cards, idk: [], reviews: reviews.filter(r => r.pupil_id === "B" && r.card_id !== "c10"),
  pupilCards: [], expectActivity: true });
check(T.pupilLine(B2, pupils[1], 10) === "· all confident", "B with nothing flagged: all confident", T.pupilLine(B2, pupils[1], 10));
check(T.pupilLine(B2, { pupil_id: "B", status: "in_progress" }, 10) === "", "in progress and no flags: nothing");
check(T.pupilLine(B2, { pupil_id: "B", status: "done_late" }, 10) === "· all confident", "Done late counts");
check(B2.reteach.length === 0, "no unsure → no reteach rows");

// the reads did not work → never a claim
const F = T.build({ pupils, cards, idk: [], reviews: [], pupilCards: [], expectActivity: true });
check(F.failed === true, "work done but every read empty → failed");
check(T.pupilLine(F, pupils[1], 10) === "", "failed read: no 'all confident'");
check(T.pupilLine({ failed: true }, pupils[1], 10) === "" && T.pupilLine(null, pupils[1], 10) === "",
  "failed / not loaded: nothing");

// make mode: the make-pass answer
const M = T.build({ pupils, cards, idk: [], reviews: [{ pupil_id: "A", card_id: "c1", rating: "got_it", answer: null, answer_check: null }],
  pupilCards: [
    { pupil_id: "A", card_id: "c1", pupil_answer: "kinda", answer_check: "partial" },
    { pupil_id: "A", card_id: "c2", pupil_answer: IDK, answer_check: "no" },
    { pupil_id: "A", card_id: "c3", pupil_answer: "", answer_check: "blank" },
    { pupil_id: "A", card_id: "c4", pupil_answer: "fine", answer_check: "match" }],
  expectActivity: true });
check(M.byPupil.A.weak.c1 === 1 && M.byPupil.A.idk.c2 === 1 && !M.byPupil.A.weak.c2 && !M.byPupil.A.weak.c3 && !M.byPupil.A.weak.c4,
  "make-pass answers: partial/no typed = weak, IDK text = idk, blank/match = neither", M.byPupil.A);
check(M.reteach.find(r => r.id === "c1").securedAnyway === 1, "make mode: secured by a got_it yet weak → secured anyway");

// sort tie-breaks: more unsure first, then more idk, then position
const S = T.build({ pupils: [{ pupil_id: "A" }, { pupil_id: "B" }, { pupil_id: "C" }],
  cards: [{ id: "x1", position: 0, question: "1" }, { id: "x2", position: 1, question: "2" }, { id: "x3", position: 2, question: "3" }],
  idk: [{ pupil_id: "A", card_id: "x3", answer: IDK }, { pupil_id: "B", card_id: "x3", answer: IDK },
        { pupil_id: "A", card_id: "x2", answer: IDK }],
  reviews: [{ pupil_id: "B", card_id: "x1", rating: "nearly", answer: "meh", answer_check: "partial" },
            { pupil_id: "C", card_id: "x1", rating: "nearly", answer: "meh", answer_check: "no" },
            { pupil_id: "C", card_id: "x2", rating: "not_yet", answer: "meh", answer_check: "no" }],
  pupilCards: [], expectActivity: true });
// x1: unsure 2 (weak 2), x2: unsure 2 (idk 1, weak 1), x3: unsure 2 (idk 2) → idk desc: x3, x2, x1
check(eq(S.reteach.map(r => r.id), ["x3", "x2", "x1"]), "equal unsure → more idk first", S.reteach.map(r => [r.id, r.unsure, r.idk]));

console.log(fails ? "\nFAIL flashcard_truth_test: " + fails + " failure(s)" : "\nOK flashcard_truth_test: all checks passed");
process.exit(fails ? 1 : 0);
