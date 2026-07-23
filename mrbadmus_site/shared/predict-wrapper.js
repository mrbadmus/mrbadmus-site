/* ============================================================
   MrBadmus — PREDICT WRAPPER  (Bonding v2 · MRB-133 Phase 1a)
   Predict-before-reveal (architecture_v2 Law 4): a commit-chip
   row that gates a hero's first reveal/state change. The student
   must wager before the model answers; after the gated action
   fires, the wrapper shows right/wrong against their chip using
   the tone tokens. No verdict is ever shown un-wagered.

   PUBLIC API (consumed by the hero modules):
     var gate = MrbPredictWrapper.create(config.predict);
     someContainer.appendChild(gate.el);
     // in an action handler:
     if (!gate.allow(actionKey)) return;   // nudges if uncommitted
     ...perform the action...
     gate.resolveIf(actionKey);            // reveals right/wrong once

   CONFIG SCHEMA (config.predict):
   {
     question     : string,
     options      : [string, ...],   // 2–3 commit chips
     correctIndex : int,
     revealsOn    : string           // action key, e.g. 'state:graphite',
                                     // 'force', 'step:2'
   }
   Action keys are namespaced by each hero: 'state:<key>' for a
   state/toggle button, 'force' for a force button, 'step:<n>' for
   reaching stepper step index ≥ n.
============================================================ */
(function () {
  'use strict';
  if (window.MrbPredictWrapper) return;

  var STYLE_ID = 'mrb-predict-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '.mrb-pw{padding:14px 24px;border-bottom:1px solid var(--surface-inset,#EFE7D8);background:var(--surface-panel,#FFFDF8)}',
      '.mrb-pw__q{display:flex;align-items:baseline;gap:8px;font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(14.5px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);margin-bottom:10px}',
      '.mrb-pw__tag{font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.1em;color:var(--accent-deep,#B5341A);text-transform:uppercase;flex:none}',
      '.mrb-pw__chips{display:flex;gap:8px;flex-wrap:wrap}',
      '.mrb-pw__chip{font-family:var(--font-display,sans-serif);font-weight:600;font-size:calc(13.5px * var(--rd-fs-scale,1));cursor:pointer;border-radius:999px;padding:8px 16px;color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1.5px solid var(--border,#E4DCCB);transition:all .15s}',
      '.mrb-pw__chip:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-pw__chip.is-committed{color:#fff;background:var(--surface-dark,#1A1714);border-color:var(--surface-dark,#1A1714)}',
      '.mrb-pw__chip.is-right{color:var(--ok,#2E6B3A);background:var(--ok-bg,#E7F3EA);border-color:var(--ok-border,#7FB98A)}',
      '.mrb-pw__chip.is-wrong{color:var(--err,#A83824);background:var(--err-bg,#FBE4DE);border-color:var(--err-border,#E0897B)}',
      '.mrb-pw__chip:disabled{cursor:default}',
      '.mrb-pw__verdict{margin-top:10px;font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(13.5px * var(--rd-fs-scale,1));display:none}',
      '.mrb-pw__verdict.is-right{display:block;color:var(--ok,#2E6B3A)}',
      '.mrb-pw__verdict.is-wrong{display:block;color:var(--err,#A83824)}',
      '.mrb-pw__nudge{margin-top:10px;font-family:var(--font-mono,monospace);font-size:calc(12px * var(--rd-fs-scale,1));color:var(--accent-deep,#B5341A);display:none}',
      '.mrb-pw.is-nudging .mrb-pw__nudge{display:block}',
      '@media (prefers-reduced-motion: no-preference){.mrb-pw.is-nudging .mrb-pw__chips{animation:mrbPwNudge .3s ease-in-out 2}}',
      '@keyframes mrbPwNudge{0%,100%{transform:translateX(0)}50%{transform:translateX(5px)}}',
    ].join('');
    document.head.appendChild(s);
  }

  function create(cfg) {
    if (!cfg || !cfg.options || !cfg.options.length) return null;
    ensureStyles();

    var committed = null;   // chosen index
    var resolved = false;

    var root = document.createElement('div');
    root.className = 'mrb-pw';

    var q = document.createElement('div');
    q.className = 'mrb-pw__q';
    var tag = document.createElement('span');
    tag.className = 'mrb-pw__tag';
    tag.textContent = 'Predict';
    q.appendChild(tag);
    q.appendChild(document.createTextNode(cfg.question || ''));
    root.appendChild(q);

    var chipsWrap = document.createElement('div');
    chipsWrap.className = 'mrb-pw__chips';
    var chips = cfg.options.map(function (label, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'mrb-pw__chip';
      b.textContent = label;
      b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function () {
        if (resolved) return;
        committed = committed === i ? null : i;
        chips.forEach(function (c, k) {
          c.classList.toggle('is-committed', committed === k);
          c.setAttribute('aria-pressed', committed === k ? 'true' : 'false');
        });
        root.classList.remove('is-nudging');
      });
      chipsWrap.appendChild(b);
      return b;
    });
    root.appendChild(chipsWrap);

    var verdict = document.createElement('div');
    verdict.className = 'mrb-pw__verdict';
    verdict.setAttribute('aria-live', 'polite');
    root.appendChild(verdict);

    var nudge = document.createElement('div');
    nudge.className = 'mrb-pw__nudge';
    nudge.textContent = '☝ commit a prediction first — then reveal';
    root.appendChild(nudge);

    function isGated(actionKey) {
      if (resolved) return false;
      var on = cfg.revealsOn || '';
      if (on.indexOf('step:') === 0 && actionKey && actionKey.indexOf('step:') === 0) {
        // step gates trigger on reaching index >= n
        return parseInt(actionKey.slice(5), 10) >= parseInt(on.slice(5), 10);
      }
      return actionKey === on;
    }

    return {
      el: root,
      committed: function () { return committed !== null; },
      allow: function (actionKey) {
        if (!isGated(actionKey)) return true;
        if (committed !== null) return true;
        root.classList.add('is-nudging');
        if (root.scrollIntoView) root.scrollIntoView({ block: 'nearest' });
        return false;
      },
      resolveIf: function (actionKey) {
        if (resolved || !isGated(actionKey) || committed === null) return;
        resolved = true;
        root.classList.remove('is-nudging');
        var right = committed === cfg.correctIndex;
        chips.forEach(function (c, k) {
          c.disabled = true;
          if (k === committed) c.classList.add(right ? 'is-right' : 'is-wrong');
          if (!right && k === cfg.correctIndex) c.classList.add('is-right');
          c.classList.remove('is-committed');
        });
        verdict.className = 'mrb-pw__verdict ' + (right ? 'is-right' : 'is-wrong');
        verdict.textContent = right
          ? 'Your prediction was right — watch it play out.'
          : 'Not what you predicted — the model shows why: ' + cfg.options[cfg.correctIndex];
      },
    };
  }

  window.MrbPredictWrapper = { create: create };
})();
