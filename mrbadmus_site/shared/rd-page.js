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
      btn.addEventListener('click', function () {
        var covered = card.classList.toggle('is-covered');
        btn.setAttribute('aria-pressed', covered ? 'true' : 'false');
        btn.textContent = covered ? '👁 Reveal' : 'Cover & recall';
      });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
