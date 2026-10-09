/* ═══════════════════════════════════════════════════════════════════════
   flashcard-truth.js — Flashcards round 3, the teacher's half: EFFORT is not
   UNDERSTANDING.

   The progress table's status chip (Done / In progress …) says what a pupil
   DID. It cannot say whether they understood: a pupil who presses "I don't
   know" on every card and is then shown the answer still finishes, and a
   card secures on any got_it rating. This module turns the raw rows the page
   reads into the second fact — which cards each pupil is UNSURE of — and into
   one class-wide "reteach" list.

   PURE. No DOM, no network: the page (flashcard-progress.js) does the reads
   and hands the rows in, so flashcard_truth_test.js can prove every rule in
   Node. Exported on `window.MRBFlashcardTruth` and, for Node, `module.exports`.

   THE RULES (Mide, 6 Oct 2026 — "you can't punish a student because the
   system said they did the flashcard"):
     · idk     the pupil pressed "I don't know" on the card at least once.
               (A flashcard_events answer_submitted row whose answer is the
               exact IDK text; or any stored answer that IS that text.)
     · weak    the pupil TYPED an answer (not the IDK text, not blank) that the
               check called Nearly (partial) or Wrong (no) — on a review rating
               (flashcard_reviews.answer_check) or the make-pass answer
               (flashcard_pupil_cards.answer_check). ANY such answer counts.
     · unsure  idk || weak.
     · secured any got_it rating (the MRB-354 rule — once secured, always).
   A card can be both secured and unsure: that is the point. "Secured anyway"
   is how many pupils got a card to green while still guessing at it.

   A pupil with NO rows at all has unsure = 0, which is also what a failed
   read would look like — so the page never calls `pupilLine` unless the read
   SUCCEEDED (see `ok`). A read that errored or returned nothing must never be
   presented as "all confident".
   ═══════════════════════════════════════════════════════════════════════ */
(function (root) {
  "use strict";

  /* Must equal IDK_TEXT in shared/flashcard-homework.js (what the pupil page
     records). Typed exactly, and compared exactly. */
  var IDK_TEXT = "I don't know";

  function isTyped(answer) {
    if (answer == null) { return false; }
    var s = String(answer).trim();
    return s !== "" && s !== IDK_TEXT;
  }
  function isIdkText(answer) {
    return answer != null && String(answer).trim() === IDK_TEXT;
  }
  function isWeakCheck(check) { return check === "partial" || check === "no"; }

  function slot(map, pid) {
    return map[pid] || (map[pid] = { idk: {}, weak: {}, secured: {} });
  }

  /* build({ pupils, cards, idk, reviews, pupilCards })

       pupils      [{pupil_id}]              the class, from flashcard_progress
       cards       [{id, position, question}] the deck
       idk         [{pupil_id, card_id}]     flashcard_events, answer = IDK text
       reviews     [{pupil_id, card_id, rating, answer, answer_check}]
       pupilCards  [{pupil_id, card_id, pupil_answer, answer_check}]  (make mode)
       expectActivity  true when some pupil has a sitting: all-empty rows then
                       mean the read failed, and the result is {failed:true}

     → { byPupil: {pid: {idk:{card:1}, weak:{card:1}, secured:{card:1}}},
         unsureCount(pid) via `unsure`, reteach: [...] }                       */
  function build(input) {
    input = input || {};
    var pupils = {}, deck = {}, byPupil = {}, i, r;
    (input.pupils || []).forEach(function (p) { pupils[p.pupil_id] = true; byPupil[p.pupil_id] = slot(byPupil, p.pupil_id); });
    (input.cards || []).forEach(function (c) { deck[c.id] = c; });

    function live(row) { return row && pupils[row.pupil_id] && deck[row.card_id]; }

    var idk = input.idk || [];
    /* ⚠️ A class that has done work but whose three reads all came back empty
       is a read that did not work (RLS answers an operator with nothing, not
       an error) — never "everyone is confident". */
    if (input.expectActivity && !idk.length && !(input.reviews || []).length &&
        !(input.pupilCards || []).length) {
      return { failed: true, byPupil: {}, reteach: [], n: 0 };
    }
    for (i = 0; i < idk.length; i++) {
      r = idk[i];
      /* Defensive: the page filters in SQL, but a row that is not an IDK
         answer is never counted as one. */
      if (!live(r) || (r.type != null && r.type !== "answer_submitted")) { continue; }
      if (r.answer != null && !isIdkText(r.answer)) { continue; }
      slot(byPupil, r.pupil_id).idk[r.card_id] = 1;
    }

    var reviews = input.reviews || [];
    for (i = 0; i < reviews.length; i++) {
      r = reviews[i];
      if (!live(r)) { continue; }
      var s = slot(byPupil, r.pupil_id);
      if (r.rating === "got_it") { s.secured[r.card_id] = 1; }
      if (isIdkText(r.answer)) { s.idk[r.card_id] = 1; }
      else if (isTyped(r.answer) && isWeakCheck(r.answer_check)) { s.weak[r.card_id] = 1; }
    }

    var pcs = input.pupilCards || [];
    for (i = 0; i < pcs.length; i++) {
      r = pcs[i];
      if (!live(r)) { continue; }
      var t = slot(byPupil, r.pupil_id);
      if (isIdkText(r.pupil_answer)) { t.idk[r.card_id] = 1; }
      else if (isTyped(r.pupil_answer) && isWeakCheck(r.answer_check)) { t.weak[r.card_id] = 1; }
    }

    /* per card, across the class */
    var rows = {};
    Object.keys(deck).forEach(function (id) {
      rows[id] = { id: id, position: deck[id].position, question: deck[id].question,
                   unsure: 0, idk: 0, weak: 0, securedAnyway: 0 };
    });
    Object.keys(byPupil).forEach(function (pid) {
      var s = byPupil[pid];
      Object.keys(deck).forEach(function (cid) {
        var a = !!s.idk[cid], w = !!s.weak[cid], u = a || w;
        if (a) { rows[cid].idk++; }
        if (w) { rows[cid].weak++; }
        if (u) { rows[cid].unsure++; }
        if (u && s.secured[cid]) { rows[cid].securedAnyway++; }
      });
    });
    var reteach = Object.keys(rows).map(function (k) { return rows[k]; })
      .filter(function (x) { return x.unsure > 0; })
      .sort(function (a, b) {
        return (b.unsure - a.unsure) || (b.idk - a.idk) ||
               ((a.position || 0) - (b.position || 0));
      });
    return { byPupil: byPupil, reteach: reteach, n: Object.keys(deck).length };
  }

  /* How many cards this pupil is unsure of (idk or weak). */
  function unsure(truth, pid) {
    var s = truth && truth.byPupil && truth.byPupil[pid];
    if (!s) { return 0; }
    var seen = {}, n = 0;
    Object.keys(s.idk).concat(Object.keys(s.weak)).forEach(function (c) {
      if (!seen[c]) { seen[c] = 1; n++; }
    });
    return n;
  }

  /* The understanding text that sits beside the status chip, or "".
       n unsure cards of m   → "· 6 of 10 unsure"
       Done/Done late and 0  → "· all confident"      (only when the read worked)
       anything else         → ""   (Not started, Missing with nothing, no data) */
  function pupilLine(truth, pupil, m) {
    if (!truth || truth.failed || !truth.byPupil || !pupil) { return ""; }
    var st = pupil.status;
    if (st === "not_started") { return ""; }
    var n = unsure(truth, pupil.pupil_id);
    if (n > 0) { return "· " + n + " of " + m + " unsure"; }
    if (st === "done" || st === "done_late") { return "· all confident"; }
    return "";
  }

  var api = { IDK_TEXT: IDK_TEXT, build: build, unsure: unsure, pupilLine: pupilLine };
  root.MRBFlashcardTruth = api;
  if (typeof module !== "undefined" && module.exports) { module.exports = api; }
})(typeof window !== "undefined" ? window : this);
