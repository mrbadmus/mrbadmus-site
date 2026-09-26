/* ═══════════════════════════════════════════════════════════════════════
   k4-facts.js — the rotating science-fact card on the landing hero
   (MRB-342.2 Part 4; card redesign 25 Sep 2026)

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
   even though the bags are technically satisfied. `advance()` swaps the
   new bag's first two entries when that happens.

   ── THE CARD (Claude Design's "Science Fact Card" delivery) ────────────

   Unlike the old crossfade, only one fact's card exists in the DOM at a
   time. Advancing REBUILDS the card from scratch so it replays Design's
   deal animation (`k4FactsDeal`) and the fact text's word-by-word reveal
   (`k4FactsWord`) exactly as drawn, rather than trying to fade one card
   into the next. The subject dot, the mono kicker (coloured, not grey —
   Design's call) and the footer progress fill are rebuilt with it.

   Design's own component shows a fixed 6 facts with one footer segment
   per fact. This site's deck is ~80 facts, so the footer here is ONE
   track that fills over the hold time and resets on each advance, rather
   than 80 illegible slivers — the one deliberate departure from the
   delivery (see the CSS comment in shared/ks4-chrome.css).

   ── prefers-reduced-motion: ONE fact, static, no timer ──────────────────

   Not a slower rotation — no rotation. The deck still runs once to pick
   which single fact shows, but no interval or animation is ever started.

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
  // `soft` is a low-alpha tint of the same hex, for the card's corner glow —
  // Design's delivery used its own slightly different hexes for this; the
  // brand colours themselves did not change, so these are derived from ours.
  var SUBJECTS = {
    physics:   { label: 'Physics',   color: '#1D6FB8', soft: 'rgba(29,111,184,0.07)' },
    chemistry: { label: 'Chemistry', color: '#B02342', soft: 'rgba(176,35,66,0.06)' },
    biology:   { label: 'Biology',   color: '#237A3B', soft: 'rgba(35,122,59,0.07)' }
  };

  var HOLD_MS = 6000;   // time a fact holds before advancing

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

    // The static fact for assistive tech: chosen once, independent of the
    // sighted rotation, and never touched again.
    var srIdx = Math.floor(Math.random() * facts.length);
    srNode.textContent = subjectOf(facts[srIdx]).label + ': ' + facts[srIdx].text;

    var paused = false;
    var tick = 0;

    function buildCard(idx) {
      var f = facts[idx];
      var subj = subjectOf(f);
      var words = String(f.text).split(' ');

      var card = document.createElement('div');
      card.className = 'k4-fact-card';
      card.style.setProperty('--k4-fact-color', subj.color);
      card.style.setProperty('--k4-fact-soft', subj.soft);
      card.style.setProperty('--k4-fact-hold', HOLD_MS + 'ms');

      var glow = document.createElement('div');
      glow.className = 'k4-fact-glow';
      card.appendChild(glow);

      var kickerRow = document.createElement('div');
      kickerRow.className = 'k4-fact-kicker-row';
      var dot = document.createElement('span');
      dot.className = 'k4-fact-dot';
      var kicker = document.createElement('span');
      kicker.className = 'k4-fact-kicker';
      kicker.textContent = subj.label;
      kickerRow.appendChild(dot);
      kickerRow.appendChild(kicker);
      card.appendChild(kickerRow);

      var text = document.createElement('p');
      text.className = 'k4-fact-text';
      text.innerHTML = words.map(function (w, k) {
        var delay = reduce ? 0 : (120 + k * 38);
        return '<span class="k4-fact-word" style="animation-delay:' + delay + 'ms">' + esc(w) + '</span>';
      }).join('');
      card.appendChild(text);

      var barWrap = document.createElement('div');
      barWrap.className = 'k4-fact-bar';
      var track = document.createElement('div');
      track.className = 'k4-fact-bar-track';
      var fill = document.createElement('div');
      fill.className = 'k4-fact-bar-fill' + (paused ? ' k4-paused' : '');
      track.appendChild(fill);
      barWrap.appendChild(track);
      card.appendChild(barWrap);

      return card;
    }

    var current = -1;
    function render(idx) {
      current = idx;
      tick++;
      stage.innerHTML = '';
      stage.appendChild(buildCard(idx));
    }

    var deck = makeDeck(facts.length);
    render(deck.next(-1));

    // A debug/test hook — read by the verification harness to prove the
    // deck does not repeat before it is exhausted, and to advance the
    // rotation on demand rather than wait 6s x 80 facts in real time.
    // Harmless in production: nothing else on the page reads or writes it.
    var shown = [current];
    function advance() {
      render(deck.next(current));
      shown.push(current);
    }
    window.__MRB_FACTS_DEBUG = {
      total: facts.length,
      get shown() { return shown.slice(); },
      advance: advance
    };

    if (reduce || facts.length < 2) return; // one fact, static, no timer

    root.addEventListener('mouseenter', function () { setPaused(true); });
    root.addEventListener('mouseleave', function () { setPaused(false); });
    root.addEventListener('focusin', function () { setPaused(true); });
    root.addEventListener('focusout', function () { setPaused(false); });

    function setPaused(v) {
      paused = v;
      var fill = stage.querySelector('.k4-fact-bar-fill');
      if (fill) fill.classList.toggle('k4-paused', paused);
    }

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
