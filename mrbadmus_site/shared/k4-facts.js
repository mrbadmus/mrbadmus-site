/* ═══════════════════════════════════════════════════════════════════════
   k4-facts.js — the science-fact card on the landing hero
   (MRB-342.2 Part 4; stilled and quietened 12 Oct 2026, front-door run)

   Reads shared/science-facts.js's window.MRB_SCIENCE_FACTS and fills the
   panel generate_site_v5.k4_facts_panel() emits (#k4-facts / #k4-facts-stage
   / #k4-facts-sr). Both files load `defer`, in that order. If the data
   failed to load, the panel removes itself rather than sit on the page
   empty.

   ── ONE FACT PER PAGE LOAD, THEN STILL ──────────────────────────────────

   A fact is picked at random when the page loads and stays. No rotation,
   no timer, no animation: Mide asked for the card to go back to the quiet
   version it was before the 25 Sep redesign. The visible card and the
   screen-reader paragraph carry the SAME fact.

   ── ACCESSIBILITY ────────────────────────────────────────────────────

   The visible stage is `aria-hidden="true"` (set in the emitted HTML);
   `#k4-facts-sr` is a visually-hidden paragraph with the same fact, which
   is the only copy assistive tech reaches, so it is never read twice.
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // The same three hexes generate_site_v5.py's PHYSICS_COLOR / CHEMISTRY_COLOR /
  // BIOLOGY_COLOR constants hold — what every other dot on this chrome page
  // (the door cards, the subject picker) renders.
  var SUBJECTS = {
    physics:   { label: 'Physics',   color: '#1D6FB8' },
    chemistry: { label: 'Chemistry', color: '#B02342' },
    biology:   { label: 'Biology',   color: '#237A3B' }
  };

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s == null ? '' : String(s);
    return d.innerHTML;
  }

  function subjectOf(fact) {
    return SUBJECTS[fact.subject] || SUBJECTS.biology;
  }

  function boot() {
    var root = document.getElementById('k4-facts');
    var stage = document.getElementById('k4-facts-stage');
    var srNode = document.getElementById('k4-facts-sr');
    if (!root || !stage || !srNode) return;

    var facts = window.MRB_SCIENCE_FACTS;
    if (!facts || !facts.length) {
      // shared/science-facts.js failed to load (blocked script, cold CDN,
      // offline). An empty panel reads as a bug; no panel reads as nothing
      // happened here, which is the honest state.
      if (root.parentNode) root.parentNode.removeChild(root);
      return;
    }

    var fact = facts[Math.floor(Math.random() * facts.length)];
    var subj = subjectOf(fact);

    stage.innerHTML =
      '<p class="k4-fact">' +
        '<span class="k4-fact-kicker">' +
          '<span class="k4-dot k4-dot-sm" style="background:' + subj.color + '"></span>' +
          esc(subj.label) +
        '</span>' +
        '<span class="k4-fact-text">' + esc(fact.text) + '</span>' +
      '</p>';
    srNode.textContent = subj.label + ': ' + fact.text;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
