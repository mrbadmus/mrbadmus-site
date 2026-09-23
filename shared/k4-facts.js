/* ═══════════════════════════════════════════════════════════════════════
   k4-facts.js — the rotating science-fact panel on the landing hero
   (MRB-342.2 Part 4)

   Reads shared/science-facts.js's window.MRB_SCIENCE_FACTS and drives the
   panel generate_site_v5.make_landing()'s k4_facts_panel() emits (#k4-facts
   / #k4-facts-stage / #k4-facts-sr). Both files are loaded `defer`, in that
   order, so by the time this runs the data is already on window — but a
   failed or blocked fetch of science-facts.js is handled too: the panel
   removes itself rather than sit on the page empty.

   ── ONE FACT AT A TIME, NO REPEAT UNTIL THE DECK IS EXHAUSTED ───────────

   `makeDeck()` shuffles every fact's index once, walks the shuffled order,
   and reshuffles only once it runs out — the classic "shuffle bag" a card
   game uses so a full pass never repeats a card. The one edge a naive
   "shuffle, then walk" misses: a fresh shuffle's own first card can equal
   the last card of the PREVIOUS bag, which reads as a repeat to a visitor
   even though the bags are technically satisfied. `next()` swaps the new
   bag's first two entries when that happens.

   ── ZERO LAYOUT SHIFT ─────────────────────────────────────────────────

   Every fact is rendered into the stage up front, stacked with CSS
   `grid-area: 1 / 1` (shared/ks4-chrome.css) — the same technique the GCSE
   hub's Top Stars rail already uses for its tier crossfade. Because every
   fact is present in the DOM, not just the current one, the grid track's
   height is set by the browser from the TALLEST fact and never changes
   again as `.k4-on` moves between them. That is what makes the headline
   beside this panel immovable — nothing here is measured or capped by
   this script; it falls out of the stacking.

   ── prefers-reduced-motion: ONE fact, static, no timer ──────────────────

   Not a slower rotation — no rotation. The deck still runs once to pick
   which single fact shows, but no interval is ever started.

   ── ACCESSIBILITY ────────────────────────────────────────────────────

   The whole stage is `aria-hidden="true"` (set in the emitted HTML) and
   carries no `aria-live` region, so a screen-reader user is never
   interrupted by a fact changing. `#k4-facts-sr` is a single, static,
   visually-hidden paragraph naming one fact chosen once at load — set
   here, never rewritten — which is the only copy assistive tech reaches.
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // The same three hexes generate_site_v5.py's PHYSICS_COLOR / CHEMISTRY_COLOR /
  // BIOLOGY_COLOR constants hold — not the older teal/pink/green named in
  // CLAUDE.md's subject-colour note, which predates the MRB-46 Phase 3 swap.
  // These are what every other dot on this chrome page (the door cards,
  // the subject picker) actually renders today.
  var SUBJECTS = {
    physics:   { label: 'Physics',   color: '#1D6FB8' },
    chemistry: { label: 'Chemistry', color: '#B02342' },
    biology:   { label: 'Biology',   color: '#237A3B' }
  };

  var HOLD_MS = 6000;   // time a fact holds, once fully faded in
  var FADE_MS = 600;    // must match the CSS `.k4-fact` transition duration

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s == null ? '' : String(s);
    return d.innerHTML;
  }

  function subjectOf(fact) {
    return SUBJECTS[fact.subject] || SUBJECTS.biology;
  }

  function shuffled(n) {
    var a = [];
    for (var i = 0; i < n; i++) a.push(i);
    for (i = n - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  // A "shuffle bag": walks one shuffled pass over every index, reshuffles
  // when exhausted, and refuses to let the new bag's first draw repeat the
  // fact that was just showing.
  function makeDeck(n) {
    var order = shuffled(n);
    var pos = 0;
    return {
      next: function (justShownIdx) {
        if (pos >= order.length) {
          order = shuffled(n);
          if (order.length > 1 && order[0] === justShownIdx) {
            var tmp = order[0]; order[0] = order[1]; order[1] = tmp;
          }
          pos = 0;
        }
        return order[pos++];
      }
    };
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

    var reduce = window.matchMedia &&
                 window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    var nodes = facts.map(function (f, i) {
      var subj = subjectOf(f);
      var p = document.createElement('p');
      p.className = 'k4-fact';
      p.setAttribute('data-idx', String(i));
      p.innerHTML =
        '<span class="k4-fact-kicker">' +
          '<span class="k4-dot k4-dot-sm" style="background:' + subj.color + '"></span>' +
          esc(subj.label) +
        '</span>' +
        '<span class="k4-fact-text">' + esc(f.text) + '</span>';
      stage.appendChild(p);
      return p;
    });

    // The static fact for assistive tech: chosen once, independent of the
    // sighted rotation, and never touched again.
    var srIdx = Math.floor(Math.random() * facts.length);
    srNode.textContent = subjectOf(facts[srIdx]).label + ': ' + facts[srIdx].text;

    var deck = makeDeck(facts.length);
    var current = deck.next(-1);
    nodes[current].classList.add('k4-on');

    // A debug/test hook — read by the verification harness to prove the
    // deck does not repeat before it is exhausted, and to advance the
    // rotation on demand rather than wait 6s x 80 facts in real time.
    // Harmless in production: nothing else on the page reads or writes it.
    var shown = [current];
    function advance() {
      nodes[current].classList.remove('k4-on');
      current = deck.next(current);
      nodes[current].classList.add('k4-on');
      shown.push(current);
    }
    window.__MRB_FACTS_DEBUG = {
      total: facts.length,
      get shown() { return shown.slice(); },
      advance: advance
    };

    if (reduce || facts.length < 2) return; // one fact, static, no timer

    var paused = false;
    root.addEventListener('mouseenter', function () { paused = true; });
    root.addEventListener('mouseleave', function () { paused = false; });
    root.addEventListener('focusin', function () { paused = true; });
    root.addEventListener('focusout', function () { paused = false; });

    setInterval(function () {
      if (paused) return;
      advance();
    }, HOLD_MS);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
