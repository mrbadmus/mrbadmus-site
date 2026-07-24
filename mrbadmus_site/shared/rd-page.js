/* ============================================================
   MrBadmus — RD PAGE CHROME  (Bonding v2 · MRB-133 Phase 1d)
   Small page-level behaviours for redesigned (.rd) pages.
   Currently: the Key Note revision card's cover-and-recall
   toggle — cover the note, recall it out loud, reveal to check.
   Frozen key_note text is untouched; this is presentation only.
============================================================ */
(function () {
  'use strict';
  function boot() {
    document.querySelectorAll('.rd-keycard').forEach(function (card) {
      var btn = card.querySelector('.rd-keycard__cover');
      if (!btn) return;
      var steps = Array.prototype.slice.call(card.querySelectorAll('.rd-keycard__step'));
      // Legacy single-block card (no split steps): plain cover / uncover.
      if (!steps.length) {
        btn.addEventListener('click', function () {
          var covered = card.classList.toggle('is-covered');
          btn.setAttribute('aria-pressed', covered ? 'true' : 'false');
          btn.textContent = covered ? '👁 Reveal' : 'Cover & recall';
        });
        return;
      }
      // Stepped cover-and-recall (MRB-134 Fix 5): the card shows all steps by
      // default (photographable); the button walks all-shown -> cover all ->
      // reveal step 1 -> step 2 -> ... -> all shown. `revealed` = steps shown.
      var n = steps.length, revealed = n;
      function render() {
        for (var i = 0; i < n; i++) steps[i].classList.toggle('is-covered', i >= revealed);
        var covered = revealed < n;
        btn.setAttribute('aria-pressed', covered ? 'true' : 'false');
        btn.textContent = (revealed >= n) ? 'Cover & recall' : ('👁 Reveal step ' + (revealed + 1));
      }
      btn.addEventListener('click', function () {
        revealed = (revealed >= n) ? 0 : revealed + 1;   // all-shown -> cover all; else reveal next
        render();
      });
      render();
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
