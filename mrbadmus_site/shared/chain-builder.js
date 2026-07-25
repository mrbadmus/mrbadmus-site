/* ============================================================
   MrBadmus — CHAIN BUILDER  (Bonding v2 Phase 2B · MRB-136)
   Rung ③ of the exam ladder: assemble the causal chain in the
   order an examiner reads it.

   INPUT MODEL — copied from shared/tap-match.js, for the same
   reason: HTML5 drag-and-drop is dead on iOS/Android touch (drag
   events never fire) and is keyboard-inaccessible. So:
     · tap a pool link  → it is appended to the end of the chain
     · tap a chain link → it goes back to the pool
     · ↑ / ↓ on each placed link reorder it
   Every control is a real <button>: Enter/Space work natively and
   the tab order is the visual order. No drag anywhere.

   ANTI-GIVE-AWAY GUARANTEE:
     the pool is item.links[] AND item.redHerrings[] combined and
     Fisher–Yates shuffled IN THE BROWSER on every build(), never
     baked into the DOM in answer order. The chain starts empty.

   MARKING — deliberately NOT strict string order. The whole point
   of the authored orderingRules is that a valid alternative order
   must not be marked wrong:
     canonical[]       reference order of link ids (also the reveal)
     optional[]        may be omitted with no penalty (scene-setters)
     interchangeable[] members of a group are free relative to each
                       other, in both directions
     mustPrecede[]     a must appear before b
   Constraint set actually graded:
     · if mustPrecede is authored, THOSE pairs are the law (plus
       their transitive closure) and canonical order is NOT imposed
       on top. This is what makes ib-chainB's "two parallel blocks,
       either block may come first" score full marks — the author
       signalled the block boundary by leaving that one adjacency
       out of mustPrecede.
     · if mustPrecede is absent, canonical IS the law: every earlier
       id must precede every later one (pic-chainB).
     · either way, any pair inside one interchangeable group is
       struck out — before AND after closure — so an internal swap
       can never cost a mark.
     · a rule only bites when BOTH of its links are in the chain, so
       omitting an optional link cannot break the rules around it.
   One mark per essential link that is present and rule-clean; an
   essential link that is also flagged optional keeps its mark when
   omitted (authored intent: "do not mark a chain wrong if 1 is
   omitted"). A violated precedence costs the mark on the LATER link
   only. Any red herring in the chain caps the award at
   (essential count − 1) and its slug is surfaced verbatim.

   ES5 only — this site has no build step.
============================================================ */
(function () {
  'use strict';
  if (!window.MrbExamLadder) return;

  /* ---------- styles ---------- */
  var STYLE_ID = 'mrb-chain-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '.mrb-chain,.mrb-chain *{box-sizing:border-box}',
      '.mrb-chain{font-family:var(--font-body,system-ui,sans-serif);color:var(--ink-body,#2A241E)}',
      '.mrb-chain__grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;align-items:start}',
      '@media (max-width:700px){.mrb-chain__grid{grid-template-columns:1fr}}',
      '.mrb-chain__lbl{font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-muted,#6B635A);margin-bottom:10px}',

      /* chain column */
      '.mrb-chain__list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}',
      '.mrb-chain__row{display:flex;align-items:flex-start;gap:8px;border:1px solid var(--border,#E4DCCB);border-radius:12px;padding:8px 10px;background:var(--surface-inset,#F7F2E8)}',
      '.mrb-chain__row.is-ok{border-color:var(--ok-border,#7FB98A);background:var(--ok-bg,#E7F3EA)}',
      '.mrb-chain__row.is-bad{border-color:var(--err-border,#E0897B);background:var(--err-bg,#FBE4DE)}',
      '.mrb-chain__num{flex:none;width:22px;height:22px;margin-top:2px;border-radius:999px;display:flex;align-items:center;justify-content:center;font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));font-weight:700;color:var(--surface-panel,#FFFDF8);background:var(--accent-deep,#B5341A)}',
      '.mrb-chain__txt{flex:1 1 auto;min-width:0;text-align:left;font-family:var(--font-body,system-ui,sans-serif);font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.45;color:var(--ink-body,#2A241E);background:transparent;border:none;padding:2px 0;cursor:pointer;border-radius:8px;overflow-wrap:anywhere}',
      '.mrb-chain__txt[disabled]{cursor:default;opacity:1;color:var(--ink-body,#2A241E)}',
      '.mrb-chain__static{flex:1 1 auto;min-width:0;font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.45;overflow-wrap:anywhere}',
      '.mrb-chain__moves{flex:none;display:flex;gap:4px}',
      '.mrb-chain__move{flex:none;width:28px;height:28px;border-radius:8px;border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);color:var(--ink,#1A1714);font-size:calc(13px * var(--rd-fs-scale,1));line-height:1;cursor:pointer}',
      '.mrb-chain__move[disabled]{opacity:.35;cursor:default}',
      '.mrb-chain__mark{flex:none;font-weight:700;margin-left:2px}',
      '.mrb-chain__empty{border:2px dashed var(--border,#E4DCCB);border-radius:12px;padding:14px 14px;font-size:calc(13px * var(--rd-fs-scale,1));line-height:1.5;color:var(--ink-muted,#6B635A);background:var(--surface-inset,#F7F2E8)}',

      /* pool column */
      '.mrb-chain__pool{display:flex;flex-direction:column;gap:8px}',
      '.mrb-chain__pick{font-family:var(--font-body,system-ui,sans-serif);font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.45;text-align:left;cursor:pointer;border-radius:10px;padding:10px 13px;border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);color:var(--ink-body,#2A241E);transition:background .15s,border-color .15s;overflow-wrap:anywhere}',
      '.mrb-chain__pick:hover{border-color:var(--accent-tint-border,#F0BBA9);background:var(--accent-wash,#FBEEE9)}',
      '.mrb-chain__pick[disabled]{cursor:default;opacity:.55}',
      '.mrb-chain__pool-empty{font-size:calc(13px * var(--rd-fs-scale,1));color:var(--ink-faint,#8A8074);padding:4px 2px}',

      /* focus rings on every control */
      '.mrb-chain__txt:focus-visible,.mrb-chain__move:focus-visible,.mrb-chain__pick:focus-visible,.mrb-chain__toggle:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',

      /* status + feedback */
      '.mrb-chain__status{margin-top:14px;font-family:var(--font-mono,monospace);font-size:calc(12px * var(--rd-fs-scale,1));color:var(--ink-muted,#6B635A);min-height:1.2em}',
      '.mrb-chain__prev{margin:0 0 14px;font-family:var(--font-mono,monospace);font-size:calc(12px * var(--rd-fs-scale,1));color:var(--ink-muted,#6B635A)}',
      '.mrb-chain__fb-h{font-family:var(--font-display,sans-serif);font-weight:700;display:block;margin-bottom:6px}',
      '.mrb-chain__fb-list{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-direction:column;gap:6px}',
      '.mrb-chain__fb-list li{padding-left:14px;position:relative}',
      '.mrb-chain__fb-list li::before{content:"·";position:absolute;left:2px}',
      '.mrb-chain__herring{margin-top:8px;padding-top:8px;border-top:1px solid var(--err-border,#E0897B)}',

      /* reveal */
      '.mrb-chain__reveal{margin-top:14px;border:1px solid var(--border,#E4DCCB);border-radius:14px;background:var(--surface-inset,#F7F2E8);padding:14px 17px}',
      '.mrb-chain__reveal[hidden]{display:none}',
      '.mrb-chain__reveal h4{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(14px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);margin:0 0 10px}',
      '.mrb-chain__steps{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px;counter-reset:mrbchain}',
      '.mrb-chain__step{display:flex;align-items:flex-start;gap:8px;font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.5}',
      '.mrb-chain__step-n{flex:none;font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));font-weight:700;color:var(--accent-deep,#B5341A);margin-top:2px}',
      '.mrb-chain__role{display:inline-block;margin-left:6px;font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));letter-spacing:.04em;color:var(--ink-muted,#6B635A);border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);border-radius:999px;padding:2px 8px;white-space:nowrap}',
      '.mrb-chain__ann{display:block;font-size:calc(12px * var(--rd-fs-scale,1));color:var(--ink-muted,#6B635A);margin-top:2px}',
      '.mrb-chain__ordering{margin-top:12px;padding-top:10px;border-top:1px solid var(--border,#E4DCCB);font-size:calc(12.5px * var(--rd-fs-scale,1));line-height:1.55;color:var(--ink-body,#2A241E)}',
      '.mrb-chain__ordering b{font-family:var(--font-display,sans-serif)}',
      '.mrb-chain__toggle{margin-top:12px;font-family:var(--font-display,sans-serif);font-weight:600;font-size:calc(13px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB);border-radius:10px;padding:8px 14px;cursor:pointer}'
    ].join('');
    document.head.appendChild(s);
  }

  /* ---------- tiny helpers (ES5 only: no ES6 array or spread syntax) ---------- */
  function isArr(x) { return Object.prototype.toString.call(x) === '[object Array]'; }
  function list(x) { return isArr(x) ? x : []; }
  function has(a, v) { return a.indexOf(v) !== -1; }

  /* A link is essential unless the author marked it creditworthy.
     Written this way (rather than role === 'essential') so a link
     that ships with no role field still counts, and so tariff and
     marking always read the same set. */
  function isEssential(link) { return link.role !== 'creditworthy'; }

  function essentialIds(item) {
    var out = [];
    list(item.links).forEach(function (lk) { if (isEssential(lk)) out.push(lk.id); });
    return out;
  }

  function tariffOf(item) { return essentialIds(item).length; }

  /* ---------- the rule set ---------- */
  function ruleSet(item) {
    var rules = item.orderingRules || {};
    var links = list(item.links);
    var i, j;

    /* canonical always lists every link id in printed order; fall back
       to printed order, and append anything the rules forgot. */
    var canonical = list(rules.canonical).slice();
    links.forEach(function (lk) { if (!has(canonical, lk.id)) canonical.push(lk.id); });

    var optional = {};
    list(rules.optional).forEach(function (id) { optional[id] = true; });

    /* group number per id; 0/undefined means "in no group" */
    var group = {};
    list(rules.interchangeable).forEach(function (g, gi) {
      list(g).forEach(function (id) { group[id] = gi + 1; });
    });
    function swappable(a, b) { return !!group[a] && group[a] === group[b]; }

    var before = {};   /* before[a][b] === true  →  a must come before b */
    function addEdge(a, b) {
      if (!a || !b || a === b || swappable(a, b)) return;
      if (!before[a]) before[a] = {};
      before[a][b] = true;
    }

    var must = [];
    list(rules.mustPrecede).forEach(function (p) { if (isArr(p) && p.length >= 2) must.push(p); });

    if (must.length) {
      /* Authored pairs are the law. Canonical order is NOT imposed on
         top of them — an adjacency the author left out is a deliberate
         block boundary (parallel blocks may be written in either order). */
      must.forEach(function (p) { addEdge(p[0], p[1]); });
      /* transitive closure, so a rule still bites across an omitted link */
      for (i = 0; i < canonical.length; i++) {
        var via = canonical[i];
        for (j = 0; j < canonical.length; j++) {
          var a = canonical[j];
          if (!before[a] || !before[a][via] || !before[via]) continue;
          for (var k = 0; k < canonical.length; k++) {
            var b = canonical[k];
            if (b === a || !before[via][b]) continue;
            addEdge(a, b);
          }
        }
      }
      /* strike out any pair the closure re-created inside one
         interchangeable group — an internal swap must never cost a mark */
      canonical.forEach(function (a) {
        canonical.forEach(function (b) {
          if (before[a] && before[a][b] && swappable(a, b)) delete before[a][b];
        });
      });
    } else {
      /* no mustPrecede authored → canonical order is the law, minus any
         interchangeable pair. Full pairwise, so it is already transitive
         and survives an omitted link in the middle. */
      for (i = 0; i < canonical.length; i++) {
        for (j = i + 1; j < canonical.length; j++) addEdge(canonical[i], canonical[j]);
      }
    }

    return { canonical: canonical, optional: optional, group: group, before: before };
  }

  /* ---------- marking ---------- */
  function grade(item, chain) {
    var rs = ruleSet(item);
    var links = list(item.links);
    var herrings = list(item.redHerrings);

    var linkById = {}, herringById = {}, pos = {}, i;
    links.forEach(function (lk) { linkById[lk.id] = lk; });
    herrings.forEach(function (h) { herringById[h.id] = h; });
    for (i = 0; i < chain.length; i++) pos[chain[i]] = i;

    var tariff = tariffOf(item);
    var award = 0;
    var state = {};          /* id → ok | bad | missing | forgiven | herring */
    var missing = [], misplaced = [], forgiven = [], creditOk = [], creditBad = [], placedHerrings = [];

    links.forEach(function (lk) {
      var here = pos[lk.id];
      var core = isEssential(lk);

      if (here == null) {
        if (!core) { state[lk.id] = 'forgiven'; return; }
        if (rs.optional[lk.id]) {
          /* authored as omittable: no penalty, so the mark stands */
          award++; state[lk.id] = 'forgiven'; forgiven.push(lk);
        } else {
          state[lk.id] = 'missing'; missing.push(lk);
        }
        return;
      }

      /* present — a rule only bites when both of its links are placed */
      var blocker = null;
      rs.canonical.forEach(function (other) {
        if (blocker || other === lk.id) return;
        if (!rs.before[other] || !rs.before[other][lk.id]) return;
        if (pos[other] == null) return;
        if (pos[other] > here) blocker = other;
      });

      if (blocker) {
        state[lk.id] = 'bad';
        if (core) misplaced.push({ link: lk, blocker: linkById[blocker] });
        else creditBad.push(lk);
      } else {
        state[lk.id] = 'ok';
        if (core) award++; else creditOk.push(lk);
      }
    });

    chain.forEach(function (id) {
      if (herringById[id]) { state[id] = 'herring'; placedHerrings.push(herringById[id]); }
    });

    /* a wrong-model link is a lost level, not a lost mark */
    var capped = false;
    if (placedHerrings.length) {
      var cap = tariff > 0 ? tariff - 1 : 0;
      if (award > cap) { award = cap; }
      capped = true;
    }

    return {
      rules: rs, tariff: tariff, award: award, state: state,
      missing: missing, misplaced: misplaced, forgiven: forgiven,
      creditOk: creditOk, creditBad: creditBad,
      herrings: placedHerrings, capped: capped
    };
  }

  /* ---------- the engine ---------- */
  window.MrbExamLadder.register('chain', {
    label: 'Build the chain',
    rung: 3,
    tariff: function (item) { return tariffOf(item); },

    build: function (item, ctx) {
      ensureStyles();

      var el = ctx.util.el;
      var plural = ctx.util.plural;
      var links = list(item.links);
      var herrings = list(item.redHerrings);
      var tariff = tariffOf(item);

      /* text lookup covers links AND herrings; never mutates the source */
      var textOf = {}, isHerring = {};
      links.forEach(function (lk) { textOf[lk.id] = lk.text; });
      herrings.forEach(function (h) { textOf[h.id] = h.text; isHerring[h.id] = true; });

      /* --- per-build state: nothing lives at module level --- */
      var chain = [];
      var locked = false;
      var revealOpen = true;
      var poolOrder = [];
      links.forEach(function (lk) { poolOrder.push(lk.id); });
      herrings.forEach(function (h) { poolOrder.push(h.id); });
      poolOrder = ctx.util.shuffle(poolOrder);   /* Fisher–Yates, every build */

      /* --- chrome --- */
      var root = el('div', { className: 'mrb-chain' });

      root.appendChild(el('p', { className: 'mrb-lc__stem' },
        'Order the reasoning — ' + ctx.util.dequote(item.title || '')));
      root.appendChild(el('p', { className: 'mrb-lc__meta' },
        'Tap a link to add it to the end of your chain. Tap a placed link to send it back. Use ↑ and ↓ to reorder. ' +
        'Some of these links are wrong-model distractors — leaving one out is part of the skill. ' +
        tariff + ' ' + plural(tariff, 'mark', 'marks') + ' available.'));

      var previous = ctx.store.readItem(item.id);
      if (previous) {
        root.appendChild(el('p', { className: 'mrb-chain__prev' },
          'Last time: ' + previous.a + ' / ' + previous.o + '. Build it again to re-check.'));
      }

      var chainWrap = el('div');
      var poolWrap = el('div', { className: 'mrb-chain__pool' });
      var poolEmpty = el('div', { className: 'mrb-chain__pool-empty' }, 'Every link is in the chain.');

      root.appendChild(el('div', { className: 'mrb-chain__grid' }, [
        el('div', null, [el('div', { className: 'mrb-chain__lbl' }, 'Your chain · tap a link to send it back'), chainWrap]),
        el('div', null, [el('div', { className: 'mrb-chain__lbl' }, 'Links · tap one to add it'), poolEmpty, poolWrap])
      ]));

      var checkBtn = el('button', {
        className: 'mrb-btn', attrs: { type: 'button' },
        on: { click: function () { check(); } }
      }, '✓ Check my chain');
      var clearBtn = el('button', {
        className: 'mrb-btn mrb-btn--quiet', attrs: { type: 'button' },
        on: { click: function () {
          chain = [];
          say('Chain cleared. Every link is back in the pool.');
          render();
        } }
      }, '↻ Clear chain');

      root.appendChild(el('div', { className: 'mrb-lc__actions' }, [checkBtn, clearBtn]));

      var status = el('div', { className: 'mrb-chain__status', attrs: { 'aria-live': 'polite' } });
      var feedback = el('div');
      var revealSlot = el('div');
      root.appendChild(status);
      root.appendChild(feedback);
      root.appendChild(revealSlot);

      function say(msg) { status.textContent = msg; }

      /* --- rows --- */
      function liveRow(id, i) {
        var row = el('li', { className: 'mrb-chain__row' });
        row.appendChild(el('span', { className: 'mrb-chain__num', attrs: { 'aria-hidden': 'true' } }, String(i + 1)));
        row.appendChild(el('button', {
          className: 'mrb-chain__txt',
          attrs: { type: 'button', 'aria-label': 'Position ' + (i + 1) + '. Remove from the chain: ' + textOf[id] },
          on: { click: function () {
            chain.splice(i, 1);
            say('Removed from the chain: ' + textOf[id] + '. ' + chain.length + ' ' + plural(chain.length, 'link', 'links') + ' placed.');
            render();
          } }
        }, textOf[id]));

        var up = el('button', {
          className: 'mrb-chain__move',
          attrs: { type: 'button', 'aria-label': 'Move up: ' + textOf[id] },
          on: { click: function () {
            if (i === 0) return;
            chain[i] = chain[i - 1]; chain[i - 1] = id;
            say('Moved to position ' + i + ': ' + textOf[id]);
            render();
          } }
        }, '↑');
        var down = el('button', {
          className: 'mrb-chain__move',
          attrs: { type: 'button', 'aria-label': 'Move down: ' + textOf[id] },
          on: { click: function () {
            if (i >= chain.length - 1) return;
            chain[i] = chain[i + 1]; chain[i + 1] = id;
            say('Moved to position ' + (i + 2) + ': ' + textOf[id]);
            render();
          } }
        }, '↓');
        if (i === 0) up.setAttribute('disabled', 'disabled');
        if (i >= chain.length - 1) down.setAttribute('disabled', 'disabled');

        row.appendChild(el('span', { className: 'mrb-chain__moves' }, [up, down]));
        return row;
      }

      function markedRow(id, i, state) {
        var good = state === 'ok' || state === 'forgiven';
        var row = el('li', { className: 'mrb-chain__row ' + (good ? 'is-ok' : 'is-bad') });
        row.appendChild(el('span', { className: 'mrb-chain__num', attrs: { 'aria-hidden': 'true' } }, String(i + 1)));
        row.appendChild(el('span', { className: 'mrb-chain__static' }, [
          document.createTextNode(textOf[id]),
          el('span', { className: 'mrb-sr' }, good ? ' — credited' : (state === 'herring' ? ' — wrong model, not credited' : ' — not credited here'))
        ]));
        row.appendChild(el('span', { className: 'mrb-chain__mark', attrs: { 'aria-hidden': 'true' } }, good ? '✓' : '✕'));
        return row;
      }

      /* --- render (no reshuffle: pool order is fixed for this build) --- */
      function render(marked) {
        chainWrap.innerHTML = '';
        if (!chain.length) {
          chainWrap.appendChild(el('div', { className: 'mrb-chain__empty' },
            'Empty. Tap the link you would write first.'));
        } else {
          var ol = el('ol', { className: 'mrb-chain__list' });
          chain.forEach(function (id, i) {
            ol.appendChild(marked ? markedRow(id, i, marked.state[id]) : liveRow(id, i));
          });
          chainWrap.appendChild(ol);
        }

        poolWrap.innerHTML = '';
        var left = 0;
        poolOrder.forEach(function (id) {
          if (has(chain, id)) return;
          left++;
          var btn = el('button', {
            className: 'mrb-chain__pick',
            attrs: { type: 'button', 'aria-label': 'Add to the end of the chain: ' + textOf[id] },
            on: { click: function () {
              chain.push(id);
              say('Added at position ' + chain.length + ': ' + textOf[id]);
              render();
            } }
          }, textOf[id]);
          if (locked) btn.setAttribute('disabled', 'disabled');
          poolWrap.appendChild(btn);
        });
        poolEmpty.style.display = left ? 'none' : 'block';

        if (locked || !chain.length) checkBtn.setAttribute('disabled', 'disabled');
        else checkBtn.removeAttribute('disabled');
        if (locked) clearBtn.setAttribute('disabled', 'disabled');
        else clearBtn.removeAttribute('disabled');
      }

      /* --- reveal: canonical order + the verbatim ordering note --- */
      function buildReveal(res) {
        var linkById = {};
        links.forEach(function (lk) { linkById[lk.id] = lk; });

        var steps = el('ol', { className: 'mrb-chain__steps' });
        res.rules.canonical.forEach(function (id, i) {
          var lk = linkById[id];
          if (!lk) return;
          var chip = lk.roleLabel || lk.roleNote || lk.role || '';
          if (res.rules.optional[id]) chip = chip ? chip + ' · may be omitted' : 'may be omitted';
          var body = el('span', null, [document.createTextNode(lk.text)]);
          if (chip) body.appendChild(el('span', { className: 'mrb-chain__role' }, chip));
          if (lk.note) body.appendChild(el('span', { className: 'mrb-chain__ann' }, lk.note));
          steps.appendChild(el('li', { className: 'mrb-chain__step' }, [
            el('span', { className: 'mrb-chain__step-n', attrs: { 'aria-hidden': 'true' } }, String(i + 1) + '.'),
            body
          ]));
        });

        var panel = el('section', { className: 'mrb-chain__reveal', attrs: { id: 'mrb-chain-reveal-' + item.id } }, [
          el('h4', null, 'The chain in order'),
          steps
        ]);
        if (item.orderingNote) {
          panel.appendChild(el('p', { className: 'mrb-chain__ordering' }, [
            el('b', null, 'More than one order scores. '),
            document.createTextNode(item.orderingNote)
          ]));
        }

        var toggle = el('button', {
          className: 'mrb-chain__toggle',
          attrs: { type: 'button', 'aria-pressed': 'true', 'aria-controls': 'mrb-chain-reveal-' + item.id },
          on: { click: function () {
            revealOpen = !revealOpen;
            toggle.setAttribute('aria-pressed', revealOpen ? 'true' : 'false');
            toggle.textContent = revealOpen ? 'Hide the chain in order' : 'Show the chain in order';
            if (revealOpen) panel.removeAttribute('hidden');
            else panel.setAttribute('hidden', 'hidden');
          } }
        }, 'Hide the chain in order');

        revealSlot.innerHTML = '';
        revealSlot.appendChild(panel);
        revealSlot.appendChild(toggle);
      }

      /* --- feedback --- */
      function buildFeedback(res) {
        var perfect = !res.herrings.length && !res.missing.length && !res.misplaced.length && res.award >= res.tariff;
        var tone = perfect ? 'mrb-note--ok' : (res.herrings.length ? 'mrb-note--err' : 'mrb-note--tip');
        var note = el('div', { className: 'mrb-note ' + tone });

        var head;
        if (perfect) {
          head = res.award + ' / ' + res.tariff + ' — top level. Every essential link is there, in an order an examiner can follow.';
        } else if (res.herrings.length) {
          head = res.award + ' / ' + res.tariff + ' — capped at Level 1. There is a wrong-model link in your chain.';
        } else {
          head = res.award + ' / ' + res.tariff + ' — capped below the top level: the chain is not complete and in order yet.';
        }
        note.appendChild(el('b', { className: 'mrb-chain__fb-h' }, head));

        var pts = el('ul', { className: 'mrb-chain__fb-list' });

        res.missing.forEach(function (lk) {
          pts.appendChild(el('li', null, 'Missing an essential link: ' + lk.text + ' Without it the reasoning has a gap, so that mark is not there to award.'));
        });
        res.misplaced.forEach(function (m) {
          pts.appendChild(el('li', null,
            'Out of order: ' + m.link.text + ' It has to come after ' + (m.blocker ? m.blocker.text : 'the link it depends on') +
            ' — the mark goes on the later link, so this one scores nothing.'));
        });
        res.creditBad.forEach(function (lk) {
          pts.appendChild(el('li', null,
            'Out of order (no mark lost, this link is a bonus): ' + lk.text));
        });
        res.forgiven.forEach(function (lk) {
          pts.appendChild(el('li', null,
            'You left this out and that is fine — it is scene-setting, not a required link: ' + lk.text));
        });
        res.creditOk.forEach(function (lk) {
          pts.appendChild(el('li', null,
            'Credited as a bonus, not required for the chain: ' + lk.text));
        });
        if (pts.childNodes.length) note.appendChild(pts);

        if (res.herrings.length) {
          var box = el('div', { className: 'mrb-chain__herring' });
          box.appendChild(el('b', { className: 'mrb-chain__fb-h' },
            res.herrings.length === 1 ? 'The wrong-model link:' : 'The wrong-model links:'));
          var hl = el('ul', { className: 'mrb-chain__fb-list' });
          res.herrings.forEach(function (h) {
            /* The slug is the join key to the MRB-135 MCQ banks. It goes into
               .mrb-slug on its own, byte-for-byte — the brackets sit outside
               the span so a scan of .mrb-slug text yields the exact key, the
               same contract write-then-mark.js and formula-deducer.js keep. */
            hl.appendChild(el('li', null, [
              document.createTextNode(h.text + ' ['),
              el('span', { className: 'mrb-slug' }, String(h.slug)),
              document.createTextNode(']')
            ]));
          });
          box.appendChild(hl);
          box.appendChild(el('p', { className: 'mrb-chain__ordering' },
            'This is not one dropped mark — it is a dropped level. Conflating two models tells the examiner the model itself is not understood, ' +
            'so a real exam answer containing it caps at Level 1 however many other marking points it makes. ' +
            'For the same reason a chain holding it cannot score more than ' +
            (res.tariff > 0 ? res.tariff - 1 : 0) + ' out of ' + res.tariff + ' here.'));
          note.appendChild(box);
        }

        feedback.innerHTML = '';
        feedback.appendChild(note);
      }

      /* --- check --- */
      function check() {
        if (locked || !chain.length) return;
        var res = grade(item, chain);
        locked = true;
        render(res);
        buildFeedback(res);
        buildReveal(res);
        say('Marked: ' + res.award + ' out of ' + res.tariff + '. The chain in order is shown below.');
        ctx.report(item.id, res.award, res.tariff);
      }

      render();
      return root;
    }
  });
})();
