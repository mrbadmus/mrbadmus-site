/* ============================================================
   MrBadmus — QUIZ ENGINE  (Bonding v2 · MRB-132 Phase 0d/0e + MRB-133 Phase 1c/1g)
   Phase 0d extracted the inlined reveal-at-end controller verbatim
   (verified by rendered-DOM comparison); this file is its Phase 1
   evolution. One engine, two card kinds:

   · MAIN QUIZ — `.rd-exam[data-st]`: exam-paper presentation.
     Questions sit in chunks (Warm-up / Exam standard / Stretch),
     each chunk with its own "Check this set" button; later chunks
     live inside <details>. A sticky progress chip tracks answered/
     checked counts. Grading reads data-correct, so it is
     independent of the browser-shuffled option order.
   · CHECKPOINTS — `.rd-checkpoint`: single relocated questions
     inline in the theory flow; immediate feedback on selection
     (the frozen wrong-option explanations do the teaching).

   PERSISTENCE (Phase 0e — never punish: no streaks, no guilt):
     quiz_best_<stId> — best main-quiz score on this device.
     End panel shows score + delta vs best, and "Retry my misses"
     rebuilds only the missed questions.
============================================================ */
(function () {
  'use strict';

  /* ---------- shared helpers ---------- */
  function shuffleOptionsIn(card) {
    var box = card.querySelector('.quiz-options');
    if (!box) return;
    var opts = Array.prototype.slice.call(box.querySelectorAll('.quiz-opt'));
    for (var k = opts.length - 1; k > 0; k--) {
      var j = Math.floor(Math.random() * (k + 1));
      var t = opts[k]; opts[k] = opts[j]; opts[j] = t;
    }
    opts.forEach(function (o) { box.appendChild(o); });
  }

  function fbEl(card) { return card.querySelector('.quiz-fb'); }

  function gradeCard(card) {
    /* reveal the verdict on one card; returns 'correct' | 'wrong' */
    var opts = Array.prototype.slice.call(card.querySelectorAll('.quiz-opt'));
    var chosen = card.querySelector('.quiz-opt.selected');
    var correctOpt = opts.filter(function (o) { return o.dataset.correct === '1'; })[0];
    opts.forEach(function (o) { o.disabled = true; o.classList.remove('selected'); });
    if (correctOpt) correctOpt.classList.add('correct');
    var isRight = !!(chosen && chosen.dataset.correct === '1');
    if (chosen && !isRight) chosen.classList.add('wrong');
    var fb = fbEl(card);
    if (fb) {
      if (!chosen) {
        fb.className = 'quiz-fb wrong-fb show';
        fb.textContent = 'Not answered — the correct answer is highlighted.';
      } else if (isRight) {
        fb.className = 'quiz-fb correct-fb show';
        fb.textContent = '✓ Correct.';
      } else {
        var exp = chosen.dataset.wrongExp;
        fb.className = 'quiz-fb wrong-fb show';
        fb.textContent = exp ? ('✕ Not quite. ' + exp) : '✕ Not quite — the correct answer is highlighted.';
      }
    }
    card.dataset.state = isRight ? 'correct' : 'wrong';
    return card.dataset.state;
  }

  function resetCard(card) {
    card.removeAttribute('data-state');
    card.querySelectorAll('.quiz-opt').forEach(function (o) {
      o.disabled = false;
      o.classList.remove('selected', 'correct', 'wrong');
    });
    var fb = fbEl(card);
    if (fb) { fb.className = 'quiz-fb'; fb.textContent = ''; }
    shuffleOptionsIn(card);
  }

  function bindSelect(card, onChange) {
    card.querySelectorAll('.quiz-opt').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (card.dataset.state) return;               // already graded
        var box = this.closest('.quiz-options');
        box.querySelectorAll('.quiz-opt').forEach(function (o) { o.classList.remove('selected'); });
        this.classList.add('selected');
        if (onChange) onChange();
      });
    });
  }

  /* ---------- persistence ---------- */
  function bestKey(st) { return 'quiz_best_' + st; }
  function readBest(st) {
    try { var v = parseInt(localStorage.getItem(bestKey(st)), 10); return isNaN(v) ? null : v; } catch (e) { return null; }
  }
  function writeBest(st, v) {
    try {
      var prev = readBest(st);
      if (prev == null || v > prev) { localStorage.setItem(bestKey(st), String(v)); return true; }
    } catch (e) {}
    return false;
  }

  /* ================= CHECKPOINTS ================= */
  function initCheckpoint(card) {
    shuffleOptionsIn(card);
    card.querySelectorAll('.quiz-opt').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (card.dataset.state) return;
        this.classList.add('selected');
        gradeCard(card);
        // low-ceremony one-more-go: a reset link, never a penalty
        var fb = fbEl(card);
        if (fb) {
          var again = document.createElement('button');
          again.type = 'button';
          again.className = 'rd-checkpoint__again';
          again.textContent = '↻ try this one again';
          again.addEventListener('click', function () { resetCard(card); });
          fb.appendChild(document.createTextNode(' '));
          fb.appendChild(again);
        }
      });
    });
  }

  /* ================= MAIN QUIZ ================= */
  function initExam(root) {
    var stId = root.dataset.st || '';
    var cards = Array.prototype.slice.call(root.querySelectorAll('.quiz-card'));
    var total = cards.length;
    if (!total) return;
    var chip = root.querySelector('.rd-exam__chip');
    var endMsg = root.querySelector('.rd-exam__end');
    var retryBtn = root.querySelector('[data-retry-misses]');
    var againBtn = root.querySelector('[data-start-over]');
    var chunks = Array.prototype.slice.call(root.querySelectorAll('.rd-exam__chunk'));

    function chunkCards(section) {
      return Array.prototype.slice.call(section.querySelectorAll('.quiz-card'));
    }
    function answeredCount() {
      return cards.filter(function (c) { return c.dataset.state || c.querySelector('.quiz-opt.selected'); }).length;
    }
    function gradedCount() {
      return cards.filter(function (c) { return c.dataset.state; }).length;
    }
    function score() {
      return cards.filter(function (c) { return c.dataset.state === 'correct'; }).length;
    }

    function updateChip() {
      if (!chip) return;
      var best = readBest(stId);
      var graded = gradedCount();
      var txt;
      if (graded === total) {
        txt = 'Checked: ' + score() + ' / ' + total;
      } else {
        txt = answeredCount() + ' of ' + total + ' answered';
        if (graded) txt += ' · ' + graded + ' checked';
      }
      if (best != null) txt += ' · best ' + best + '/' + total;
      chip.textContent = txt;
    }

    function chunkName(section) { return section.dataset.chunk || 'this set'; }

    function finishIfDone() {
      if (gradedCount() !== total) return;
      var sc = score();
      var prevBest = readBest(stId);
      writeBest(stId, sc);
      var misses = total - sc;
      var ratio = sc / total;

      // weakest chunk = most misses (diagnosis + route, MRB-133 Phase 1g)
      var weakest = null, weakestMisses = 0;
      chunks.forEach(function (sec) {
        var m = chunkCards(sec).filter(function (c) { return c.dataset.state === 'wrong'; }).length;
        if (m > weakestMisses) { weakestMisses = m; weakest = chunkName(sec); }
      });

      var msg = sc + '/' + total;
      if (ratio === 1) {
        msg += ' — full marks. If you can also explain each answer out loud, this page is done.';
      } else if (ratio >= 0.8) {
        msg += ' — close. Retry your ' + misses + (misses === 1 ? ' miss' : ' misses') + ' to finish the set.';
      } else if (ratio >= 0.5) {
        msg += ' — solid start.' + (weakest ? ' Most misses were in ' + weakest + ' — re-read the theory it tests, then retry your ' + misses + ' misses.' : '');
      } else {
        msg += (weakest ? ' — most misses were in ' + weakest + '. Two minutes back in the theory blocks, then retry your ' + misses + ' misses.'
                        : ' — head back to the theory blocks, then retry your ' + misses + ' misses.');
      }
      if (prevBest != null) {
        if (sc > prevBest) msg += ' New best — up from ' + prevBest + '.';
        else if (sc === prevBest) msg += ' Ties your best.';
        else msg += ' Best so far: ' + prevBest + '.';
      }

      if (endMsg) {
        endMsg.textContent = msg;
        endMsg.style.display = 'block';
        endMsg.className = 'rd-exam__end ' + (ratio === 1 ? 'is-win' : ratio >= 0.6 ? 'is-mid' : 'is-low');
      }
      if (retryBtn) retryBtn.style.display = misses ? '' : 'none';
      if (againBtn) againBtn.style.display = '';
      updateChip();
    }

    chunks.forEach(function (sec) {
      var btn = sec.querySelector('[data-chunk-check]');
      if (!btn) return;
      btn.addEventListener('click', function () {
        chunkCards(sec).forEach(function (c) { if (!c.dataset.state) gradeCard(c); });
        btn.disabled = true;
        updateChip();
        finishIfDone();
      });
    });

    if (retryBtn) retryBtn.addEventListener('click', function () {
      var missed = cards.filter(function (c) { return c.dataset.state === 'wrong'; });
      missed.forEach(resetCard);
      chunks.forEach(function (sec) {
        var hasReset = chunkCards(sec).some(function (c) { return !c.dataset.state; });
        var btn = sec.querySelector('[data-chunk-check]');
        if (btn && hasReset) btn.disabled = false;
        var det = sec.closest('details');
        if (det && hasReset) det.open = true;
      });
      if (endMsg) { endMsg.style.display = 'none'; endMsg.textContent = ''; }
      retryBtn.style.display = 'none';
      if (againBtn) againBtn.style.display = 'none';
      updateChip();
      var first = missed[0];
      if (first && first.scrollIntoView) first.scrollIntoView({ block: 'center' });
    });

    if (againBtn) againBtn.addEventListener('click', function () {
      cards.forEach(resetCard);
      chunks.forEach(function (sec) {
        var btn = sec.querySelector('[data-chunk-check]');
        if (btn) btn.disabled = false;
      });
      if (endMsg) { endMsg.style.display = 'none'; endMsg.textContent = ''; }
      retryBtn && (retryBtn.style.display = 'none');
      againBtn.style.display = 'none';
      updateChip();
    });

    cards.forEach(function (card) {
      shuffleOptionsIn(card);
      bindSelect(card, updateChip);
    });
    if (retryBtn) retryBtn.style.display = 'none';
    if (againBtn) againBtn.style.display = 'none';
    updateChip();
  }

  /* ---------- boot ---------- */
  function boot() {
    Array.prototype.slice.call(document.querySelectorAll('.rd-checkpoint')).forEach(initCheckpoint);
    Array.prototype.slice.call(document.querySelectorAll('.rd-exam')).forEach(initExam);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
