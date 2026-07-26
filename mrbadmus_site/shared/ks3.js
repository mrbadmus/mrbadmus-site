/* ═══════════════════════════════════════════════════════════════
   KS3 — lesson interactions.  architecture.md §5.0, §5.8.

   Three jobs, and nothing else:

   Law 4 — predict before reveal. No stateful reveal is shown until
           the student has committed to a prediction. An unspoken
           wrong belief is invisible to its holder; committing is
           what drags it into the open.
   Law 8 — the mastery ladder persists, and "retry my misses" works.
   Law 9 — motion is animated, and reduced-motion users get the
           instant swap (handled in ks3.css, honoured here by not
           forcing any inline animation).

   Persistence uses localStorage on the same pattern as bonding v2
   (`quiz_best_<id>`), per §8.7. Server-side progress is Phase 5.

   Never punish: no streaks, no guilt copy, no XP, no timers.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var STORE_PREFIX = "ks3_best_";

  function readBest(id) {
    try {
      var v = window.localStorage.getItem(STORE_PREFIX + id);
      return v === null ? null : JSON.parse(v);
    } catch (e) { return null; }
  }

  function writeBest(id, value) {
    try {
      window.localStorage.setItem(STORE_PREFIX + id, JSON.stringify(value));
    } catch (e) { /* private mode — the lesson still works, just not saved */ }
  }

  /* ── Law 4: a reveal is gated behind a committed prediction ── */
  function wirePredictions(root) {
    var blocks = root.querySelectorAll("[data-activity]");
    Array.prototype.forEach.call(blocks, function (block) {
      var reveal = block.querySelector("[data-reveal]");
      var options = block.querySelectorAll(".ks3-option");
      if (!options.length) { return; }

      Array.prototype.forEach.call(options, function (btn) {
        btn.setAttribute("aria-pressed", "false");
        btn.addEventListener("click", function () {
          Array.prototype.forEach.call(options, function (b) {
            b.setAttribute("aria-pressed", "false");
          });
          btn.setAttribute("aria-pressed", "true");
          if (reveal && reveal.hasAttribute("hidden")) {
            reveal.removeAttribute("hidden");
            // Announce the reveal for screen-reader users, who would
            // otherwise get no signal that new content appeared.
            reveal.setAttribute("role", "status");
          }
        });
      });
    });
  }

  /* ── Law 8: the four-rung ladder ── */
  function wireLadder(ladder) {
    var lessonId = ladder.getAttribute("data-lesson") || "lesson";
    var rungs = ladder.querySelectorAll(".ks3-rung");
    var answered = {};
    var missed = {};

    function scoreLine() {
      var got = 0, total = 0;
      Object.keys(answered).forEach(function (k) {
        total += 1;
        if (answered[k]) { got += 1; }
      });
      return { got: got, total: total };
    }

    var summary = document.createElement("div");
    summary.className = "ks3-ladder-summary";
    summary.setAttribute("role", "status");
    ladder.appendChild(summary);

    var retry = document.createElement("button");
    retry.type = "button";
    retry.className = "ks3-retry";
    retry.textContent = "Retry my misses";
    retry.hidden = true;
    ladder.appendChild(retry);

    function refresh() {
      var s = scoreLine();
      if (!s.total) { summary.textContent = ""; return; }
      var best = readBest(lessonId);
      var txt = "You got " + s.got + " of " + s.total + ".";
      if (best && typeof best.got === "number") {
        if (s.got > best.got) {
          txt += " That's your best yet — up " + (s.got - best.got) + ".";
        } else {
          txt += " Your best so far is " + best.got + ".";
        }
      }
      summary.textContent = txt;
      if (!best || s.got > best.got) { writeBest(lessonId, s); }
      retry.hidden = Object.keys(missed).length === 0;
    }

    Array.prototype.forEach.call(rungs, function (rung) {
      var key = rung.getAttribute("data-rung");
      var options = rung.querySelectorAll(".ks3-option");
      if (!options.length) { return; }

      var fb = document.createElement("p");
      fb.className = "ks3-feedback";
      fb.setAttribute("role", "status");
      rung.appendChild(fb);

      Array.prototype.forEach.call(options, function (btn) {
        btn.addEventListener("click", function () {
          if (rung.getAttribute("data-locked") === "1") { return; }
          rung.setAttribute("data-locked", "1");

          var correct = btn.getAttribute("data-correct") === "1";
          answered[key] = correct;
          if (correct) { delete missed[key]; } else { missed[key] = true; }

          Array.prototype.forEach.call(options, function (b) {
            b.disabled = true;
            if (b.getAttribute("data-correct") === "1") {
              b.classList.add("is-correct");
            }
          });
          if (!correct) { btn.classList.add("is-wrong"); }

          // Law 10: the feedback corrects THIS misconception, not a
          // generic "wrong, try again".
          fb.textContent = correct
            ? "Correct."
            : (btn.getAttribute("data-feedback") || "Not quite.");
          refresh();
        });
      });
    });

    retry.addEventListener("click", function () {
      Array.prototype.forEach.call(rungs, function (rung) {
        var key = rung.getAttribute("data-rung");
        if (!missed[key]) { return; }
        rung.removeAttribute("data-locked");
        delete answered[key];
        var fb = rung.querySelector(".ks3-feedback");
        if (fb) { fb.textContent = ""; }
        Array.prototype.forEach.call(rung.querySelectorAll(".ks3-option"),
          function (b) {
            b.disabled = false;
            b.classList.remove("is-correct", "is-wrong");
            b.setAttribute("aria-pressed", "false");
          });
      });
      missed = {};
      retry.hidden = true;
      var first = ladder.querySelector(".ks3-rung:not([data-locked]) .ks3-option");
      if (first) { first.focus(); }
      refresh();
    });

    refresh();
  }

  function init() {
    wirePredictions(document);
    Array.prototype.forEach.call(
      document.querySelectorAll(".ks3-ladder"), wireLadder);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
