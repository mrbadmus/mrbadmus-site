/* ============================================================
   MrBadmus Hero — FIFA STEP REVEAL  (vanilla, net-new)
   Archetype 06. The calculation workhorse. FIFA = Formula ·
   Insert · Fine-tune · Answer. Two views of the SAME four-step
   method per example:
     • Worked   — reveal one step at a time on click.
     • Practice — the student does each step (choice or input) and
                  is marked one step at a time, feedback tied to
                  the failed step.
   An example picker steps between several escalating problems in
   one hero (content-standards §2: ≥3 worked examples + practice).

   Ported 1:1 from Design's `Bonding Hero 6 - FIFA Step Reveal
   .dc.html`. No React, no build step. The FIFA spine (F,I,F,A) is
   structural and comes from the FIFA constant, not the config.

   PUBLIC API:
     MrbHeroes.fifaStepReveal.init(container, config)

   CONFIG SCHEMA:
   {
     emoji, title, subtitle : string
     examples : [ {                 // ≥3; a picker shows when >1
       name    : string,            // picker tab label
       problem : string,            // question statement
       given   : [ { sym, val, note } ],   // known-quantity chips (optional)
       steps   : [ EXACTLY 4, mapped F,I,F,A × {
         title  : string,
         worked : string,           // line shown in the worked example
         note   : string,           // one-line explanation under the worked line
         practice : {
           prompt  : string,
           kind    : 'choice' | 'input',
           options : [ { text, ok } ],                 // kind:'choice'
           blanks  : [ { prefix, suffix, placeholder, accept:[..] } ],  // kind:'input'
           feedback: { wrong }
         }
       } ],
       success : { title, sub },
       hint    : string             // dark mono method-reminder bar
     } ]
   }
============================================================ */
(function () {
  'use strict';
  var NS = (window.MrbHeroes = window.MrbHeroes || {});
  if (NS.fifaStepReveal) return;

  var FIFA = [
    { letter: 'F', name: 'FORMULA' },
    { letter: 'I', name: 'INSERT' },
    { letter: 'F', name: 'FINE-TUNE' },
    { letter: 'A', name: 'ANSWER' },
  ];

  var STYLE_ID = 'mrb-hero-fifa-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '@keyframes mrbRevealUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}',
      '@keyframes mrbPopIn{from{opacity:0;transform:scale(.94)}to{opacity:1;transform:none}}',
      '.mrb-fifa,.mrb-fifa *{box-sizing:border-box}',
      '.mrb-fifa{font-family:var(--font-body,system-ui,sans-serif);background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);box-shadow:var(--shadow-panel,0 22px 50px -35px rgba(60,30,20,.5));overflow:hidden}',
      '.mrb-fifa__head{display:flex;align-items:center;gap:10px;padding:16px 24px;border-bottom:1px solid var(--surface-inset,#EFE7D8);flex-wrap:wrap}',
      '.mrb-fifa__head h3{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(18px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714);margin:0;min-width:0;overflow-wrap:anywhere}',
      '.mrb-fifa__sub{font-family:var(--font-mono,monospace);font-size: calc(12px * var(--rd-fs-scale, 1));font-weight:700;color:var(--ink-muted,#6B635A)}',
      '.mrb-fifa__picker{display:flex;gap:8px;flex-wrap:wrap;padding:12px 24px 0}',
      '.mrb-fifa__tab{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(13px * var(--rd-fs-scale, 1));cursor:pointer;border-radius:999px;padding:7px 14px;color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB)}',
      '.mrb-fifa__tab.is-active{color:#fff;background:var(--surface-dark,#1A1714);border-color:var(--surface-dark,#1A1714)}',
      '.mrb-fifa__body{padding:22px 24px}',
      '.mrb-fifa__prob{background:var(--surface-inset,#F7F2E8);border:1px solid var(--border,#E4DCCB);border-left:4px solid var(--accent-deep,#B5341A);border-radius:12px;padding:16px 18px}',
      '.mrb-fifa__prob-lbl{font-family:var(--font-mono,monospace);font-size: calc(11px * var(--rd-fs-scale, 1));font-weight:700;letter-spacing:.1em;color:var(--accent-deep,#B5341A);margin-bottom:8px}',
      '.mrb-fifa__prob-txt{margin:0 0 14px;font-size: calc(15px * var(--rd-fs-scale, 1));line-height:1.6;color:var(--ink-body,#2A241E)}',
      '.mrb-fifa__given{display:flex;flex-wrap:wrap;gap:8px}',
      '.mrb-fifa__chip{background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);border-radius:10px;padding:8px 12px;display:flex;flex-direction:column;gap:2px}',
      '.mrb-fifa__chip-sym{font-family:var(--font-mono,monospace);font-size: calc(11px * var(--rd-fs-scale, 1));font-weight:700;color:var(--ink-muted,#6B635A)}',
      '.mrb-fifa__chip-val{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(15px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714)}',
      '.mrb-fifa__chip-note{font-size: calc(11px * var(--rd-fs-scale, 1));color:var(--ink-muted,#6B635A)}',
      '.mrb-fifa__modes{display:flex;gap:8px;margin:20px 0 18px;flex-wrap:wrap}',
      '.mrb-fifa__seg{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(14px * var(--rd-fs-scale, 1));border:1px solid var(--border,#E4DCCB);padding:9px 16px;border-radius:10px;cursor:pointer;background:var(--surface-inset,#EFE7D8);color:#4A4238}',
      '.mrb-fifa__seg.is-on{background:var(--surface-dark,#1A1714);color:#fff;border-color:var(--surface-dark,#1A1714)}',
      '.mrb-fifa__steps{display:flex;flex-direction:column;gap:12px}',
      '.mrb-fifa__step{border:1px solid var(--surface-inset,#EFE7D8);border-radius:14px;padding:16px 18px;background:var(--surface-panel,#FFFDF8)}',
      '.mrb-fifa__step--reveal{animation:mrbRevealUp .4s both}',
      '.mrb-fifa__step-hd{display:flex;align-items:center;gap:12px}',
      '.mrb-fifa__badge{width:34px;height:34px;flex:0 0 34px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(17px * var(--rd-fs-scale, 1))}',
      '.mrb-fifa__badge--accent{color:#fff;background:radial-gradient(circle at 35% 30%,#E0745F,#C0392B);box-shadow:0 4px 10px -3px rgba(192,57,43,.5)}',
      '.mrb-fifa__badge--green{color:#2E6B3A;background:var(--ok-bg,#E7F3EA)}',
      '.mrb-fifa__badge--grey{color:#6B635A;background:#E4DCCB}',
      '.mrb-fifa__step-name{font-family:var(--font-mono,monospace);font-size: calc(10.5px * var(--rd-fs-scale, 1));font-weight:700;letter-spacing:.12em;color:var(--ink-muted,#6B635A)}',
      '.mrb-fifa__step-t{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(16px * var(--rd-fs-scale, 1));color:var(--ink,#1A1714)}',
      '.mrb-fifa__worked{margin-top:12px;background:var(--surface-dark,#1A1714);border-radius:10px;padding:14px 16px;font-family:var(--font-mono,monospace);font-size: calc(14.5px * var(--rd-fs-scale, 1));line-height:1.5;color:#EAE3D6;overflow-x:auto}',
      '.mrb-fifa__note{margin:10px 0 0;font-size: calc(13.5px * var(--rd-fs-scale, 1));line-height:1.55;color:var(--ink-muted,#6B635A)}',
      '.mrb-fifa__reveal-btn{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(14px * var(--rd-fs-scale, 1));padding:11px 22px;border-radius:10px;cursor:pointer;margin-top:14px;color:#fff;background:var(--accent-deep,#B5341A);border:none;box-shadow:0 8px 20px -8px rgba(181,52,26,.6)}',
      '.mrb-fifa__reveal-btn.is-done{color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB);box-shadow:none}',
      '.mrb-fifa__solved{margin-top:10px;background:var(--ok-bg,#E7F3EA);border:1px solid var(--ok-border,#7FB98A);border-radius:10px;padding:10px 14px;font-family:var(--font-mono,monospace);font-size: calc(13.5px * var(--rd-fs-scale, 1));color:#2E6B3A}',
      '.mrb-fifa__prompt{margin:12px 0 12px;font-size: calc(14px * var(--rd-fs-scale, 1));line-height:1.5;color:#4A4238}',
      '.mrb-fifa__opts{display:flex;flex-direction:column;gap:8px}',
      '.mrb-fifa__opt{font-family:var(--font-mono,monospace);font-size: calc(14px * var(--rd-fs-scale, 1));text-align:left;cursor:pointer;border-radius:10px;padding:11px 14px;background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);color:var(--ink-body,#2A241E);transition:all .15s}',
      '.mrb-fifa__opt.is-sel{background:#FBEAE1;border:2px solid var(--accent-strong,#E0531F);color:var(--ink-body,#2A241E);box-shadow:0 6px 16px -8px rgba(224,83,31,.5)}',
      '.mrb-fifa__blanks{display:flex;flex-wrap:wrap;align-items:center;gap:8px}',
      '.mrb-fifa__pre{font-family:var(--font-mono,monospace);font-size: calc(14.5px * var(--rd-fs-scale, 1));color:var(--ink-body,#2A241E)}',
      '.mrb-fifa__suf{font-family:var(--font-mono,monospace);font-size: calc(13px * var(--rd-fs-scale, 1));color:var(--ink-muted,#6B635A)}',
      '.mrb-fifa__in{width:92px;font-family:var(--font-mono,monospace);font-size: calc(15px * var(--rd-fs-scale, 1));font-weight:600;text-align:center;color:var(--ink,#1A1714);background:#fff;border:1.5px solid var(--border,#E4DCCB);border-radius:8px;padding:8px 6px;outline:none}',
      '.mrb-fifa__in:focus{border-color:var(--accent-strong,#C0392B)}',
      '.mrb-fifa__check-row{display:flex;align-items:center;gap:12px;margin-top:14px;flex-wrap:wrap}',
      '.mrb-fifa__check{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(14px * var(--rd-fs-scale, 1));color:#fff;background:var(--accent-deep,#B5341A);border:none;padding:10px 20px;border-radius:10px;cursor:pointer;box-shadow:0 8px 20px -8px rgba(181,52,26,.7)}',
      '.mrb-fifa__fb{animation:mrbPopIn .25s both;display:flex;align-items:center;gap:8px;font-size: calc(13.5px * var(--rd-fs-scale, 1));line-height:1.45;color:#A83824;background:var(--err-bg,#FBE4DE);border:1px solid var(--err-border,#E0897B);border-radius:10px;padding:9px 13px}',
      '.mrb-fifa__step--locked{background:var(--surface-inset,#F7F2E8)}',
      '.mrb-fifa__locked{margin-top:8px;font-size: calc(13px * var(--rd-fs-scale, 1));font-style:italic;color:var(--ink-muted,#6B635A)}',
      '.mrb-fifa__success{animation:mrbPopIn .35s both;margin-top:14px;display:flex;align-items:center;gap:12px;background:var(--ok-bg,#E7F3EA);border:1px solid var(--ok-border,#7FB98A);border-radius:14px;padding:16px 20px}',
      '.mrb-fifa__success-t{font-family:var(--font-display,sans-serif);font-weight:700;font-size: calc(16px * var(--rd-fs-scale, 1));color:#2E6B3A}',
      '.mrb-fifa__success-s{font-size: calc(13px * var(--rd-fs-scale, 1));color:#41663f}',
      '.mrb-fifa__restart{font-family:var(--font-display,sans-serif);font-weight:600;font-size: calc(14px * var(--rd-fs-scale, 1));color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB);padding:10px 20px;border-radius:10px;cursor:pointer;margin-top:14px}',
      '.mrb-fifa__strap{padding:13px 24px;background:var(--surface-dark,#1A1714);font-family:var(--font-mono,monospace);font-size: calc(12.5px * var(--rd-fs-scale, 1));line-height:1.5;color:#EAE3D6}',
    ].join('');
    document.head.appendChild(s);
  }

  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) {
      if (attrs.className) n.className = attrs.className;
      if (attrs.style) for (var k in attrs.style) n.style[k] = attrs.style[k];
      if (attrs.on) for (var ev in attrs.on) n.addEventListener(ev, attrs.on[ev]);
      if (attrs.attrs) for (var a in attrs.attrs) n.setAttribute(a, attrs.attrs[a]);
    }
    if (kids != null) {
      if (!Array.isArray(kids)) kids = [kids];
      kids.forEach(function (c) { if (c != null) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    }
    return n;
  }

  /* ---- pure answer marking ---- */
  function norm(s) {
    return String(s == null ? '' : s).trim().toLowerCase()
      .replace(/[−–—]/g, '-').replace(/×/g, 'x').replace(/÷/g, '/').replace(/\s+/g, '');
  }
  function matches(input, accept) {
    var n = norm(input);
    if (!n) return false;
    var iv = parseFloat(n.replace(/[^0-9.\-]/g, ''));
    return accept.some(function (a) {
      var an = norm(a);
      if (n === an) return true;
      var av = parseFloat(an.replace(/[^0-9.\-]/g, ''));
      if (!isNaN(av) && !isNaN(iv) && /[0-9]/.test(n) && Math.abs(av - iv) < 1e-9) return true;
      return false;
    });
  }

  function init(container, config) {
    if (!container || !config) return;
    ensureStyles();
    var examples = config.examples || [];
    if (!examples.length) return;

    // per-example UI state
    var ei = 0;
    var states = examples.map(function () { return { mode: 'worked', revealed: 1, cur: 0, vals: {}, status: {} }; });

    var root = el('div', { className: 'mrb-fifa' });
    root.appendChild(el('div', { className: 'mrb-fifa__head' }, [
      el('span', { style: { fontSize: 'calc(20px * var(--rd-fs-scale, 1))' } }, config.emoji || '⚽'),
      el('h3', null, config.title || 'FIFA Worked Examples'),
      config.subtitle ? el('span', { className: 'mrb-fifa__sub' }, '— ' + config.subtitle) : null,
    ]));

    var pickerWrap = null, tabEls = [];
    if (examples.length > 1) {
      pickerWrap = el('div', { className: 'mrb-fifa__picker' });
      tabEls = examples.map(function (ex, k) {
        var t = el('button', { className: 'mrb-fifa__tab', attrs: { type: 'button' },
          on: { click: function () { ei = k; render(); } } }, ex.name || ('Example ' + (k + 1)));
        pickerWrap.appendChild(t); return t;
      });
      root.appendChild(pickerWrap);
    }

    var body = el('div', { className: 'mrb-fifa__body' });
    var strap = el('div', { className: 'mrb-fifa__strap' });
    root.appendChild(body);
    root.appendChild(strap);
    container.appendChild(root);

    function stepCorrect(ex, st, si) {
      var p = ex.steps[si].practice;
      if (p.kind === 'choice') { var sel = st.vals[si + ':c']; return sel != null && p.options[sel] && !!p.options[sel].correct; }
      return p.blanks.every(function (b, bi) { return matches(st.vals[si + ':' + bi] || '', b.accept); });
    }

    function render() {
      var ex = examples[ei], st = states[ei];
      tabEls.forEach(function (t, k) { t.classList.toggle('is-active', k === ei); });
      body.innerHTML = '';
      strap.textContent = ex.hint || '';

      // problem
      var chips = (ex.given || []).map(function (g) {
        return el('div', { className: 'mrb-fifa__chip' }, [
          el('span', { className: 'mrb-fifa__chip-sym' }, g.sym),
          el('span', { className: 'mrb-fifa__chip-val' }, g.val),
          g.note ? el('span', { className: 'mrb-fifa__chip-note' }, g.note) : null,
        ]);
      });
      body.appendChild(el('div', { className: 'mrb-fifa__prob' }, [
        el('div', { className: 'mrb-fifa__prob-lbl' }, 'THE PROBLEM'),
        el('p', { className: 'mrb-fifa__prob-txt' }, ex.problem),
        chips.length ? el('div', { className: 'mrb-fifa__given' }, chips) : null,
      ]));

      // mode toggle
      var isWorked = st.mode === 'worked';
      body.appendChild(el('div', { className: 'mrb-fifa__modes' }, [
        el('button', { className: 'mrb-fifa__seg' + (isWorked ? ' is-on' : ''), attrs: { type: 'button' },
          on: { click: function () { st.mode = 'worked'; render(); } } }, '📖 Worked example'),
        el('button', { className: 'mrb-fifa__seg' + (!isWorked ? ' is-on' : ''), attrs: { type: 'button' },
          on: { click: function () { st.mode = 'practice'; render(); } } }, '✍️ Practice yourself'),
      ]));

      if (isWorked) {
        var stepEls = ex.steps.map(function (s, si) {
          if (si >= st.revealed) return null;
          return el('div', { className: 'mrb-fifa__step mrb-fifa__step--reveal' }, [
            el('div', { className: 'mrb-fifa__step-hd' }, [
              el('div', { className: 'mrb-fifa__badge mrb-fifa__badge--accent' }, FIFA[si].letter),
              el('div', null, [
                el('div', { className: 'mrb-fifa__step-name' }, FIFA[si].name),
                el('div', { className: 'mrb-fifa__step-t' }, s.title),
              ]),
            ]),
            el('div', { className: 'mrb-fifa__worked' }, s.worked),
            el('p', { className: 'mrb-fifa__note' }, s.note),
          ]);
        });
        body.appendChild(el('div', { className: 'mrb-fifa__steps' }, stepEls));
        var allRevealed = st.revealed >= ex.steps.length;
        body.appendChild(el('button', { className: 'mrb-fifa__reveal-btn' + (allRevealed ? ' is-done' : ''), attrs: { type: 'button' },
          on: { click: function () { st.revealed = allRevealed ? 1 : st.revealed + 1; render(); } } },
          allRevealed ? '↺ Collapse steps' : 'Reveal next step  →'));
      } else {
        // practice
        var stepCards = ex.steps.map(function (s, si) {
          var phase = si < st.cur ? 'solved' : (si === st.cur ? 'active' : 'locked');
          var p = s.practice;
          var badgeCls = phase === 'solved' ? 'mrb-fifa__badge--green' : (phase === 'active' ? 'mrb-fifa__badge--accent' : 'mrb-fifa__badge--grey');
          var kids = [
            el('div', { className: 'mrb-fifa__step-hd' }, [
              el('div', { className: 'mrb-fifa__badge ' + badgeCls }, phase === 'solved' ? '✓' : FIFA[si].letter),
              el('div', null, [
                el('div', { className: 'mrb-fifa__step-name' }, FIFA[si].name),
                el('div', { className: 'mrb-fifa__step-t' }, s.title),
              ]),
            ]),
          ];
          if (phase === 'solved') {
            kids.push(el('div', { className: 'mrb-fifa__solved' }, s.worked));
          } else if (phase === 'active') {
            kids.push(el('p', { className: 'mrb-fifa__prompt' }, p.prompt));
            if (p.kind === 'choice') {
              var opts = p.options.map(function (o, oi) {
                return el('button', { className: 'mrb-fifa__opt' + (st.vals[si + ':c'] === oi ? ' is-sel' : ''), attrs: { type: 'button' },
                  on: { click: function () { st.vals[si + ':c'] = oi; delete st.status[si]; render(); } } }, o.text);
              });
              kids.push(el('div', { className: 'mrb-fifa__opts' }, opts));
            } else {
              var blankEls = [];
              p.blanks.forEach(function (b, bi) {
                if (b.prefix) blankEls.push(el('span', { className: 'mrb-fifa__pre' }, b.prefix));
                var inp = el('input', { className: 'mrb-fifa__in', attrs: { type: 'text', placeholder: b.placeholder || '?', 'aria-label': (b.prefix || '') + ' answer' } });
                inp.value = st.vals[si + ':' + bi] || '';
                inp.addEventListener('input', function () { st.vals[si + ':' + bi] = inp.value; delete st.status[si]; });
                blankEls.push(inp);
                if (b.suffix) blankEls.push(el('span', { className: 'mrb-fifa__suf' }, b.suffix));
              });
              kids.push(el('div', { className: 'mrb-fifa__blanks' }, blankEls));
            }
            var checkRow = [el('button', { className: 'mrb-fifa__check', attrs: { type: 'button' },
              on: { click: function () {
                var ok = stepCorrect(ex, st, si);
                st.status[si] = ok ? 'right' : 'wrong';
                if (ok) st.cur = st.cur + 1;
                render();
              } } }, 'Check this step')];
            if (st.status[si] === 'wrong') {
              checkRow.push(el('div', { className: 'mrb-fifa__fb' }, [el('span', { style: { fontWeight: '700' } }, '✕'), el('span', null, p.feedback.wrong)]));
            }
            kids.push(el('div', { className: 'mrb-fifa__check-row' }, checkRow));
          } else {
            kids.push(el('div', { className: 'mrb-fifa__locked' }, 'Complete the step above first.'));
          }
          return el('div', { className: 'mrb-fifa__step' + (phase === 'locked' ? ' mrb-fifa__step--locked' : '') }, kids);
        });
        body.appendChild(el('div', { className: 'mrb-fifa__steps' }, stepCards));
        if (st.cur >= ex.steps.length) {
          body.appendChild(el('div', { className: 'mrb-fifa__success' }, [
            el('span', { style: { fontSize: 'calc(26px * var(--rd-fs-scale, 1))' } }, '🎉'),
            el('div', null, [
              el('div', { className: 'mrb-fifa__success-t' }, ex.success ? ex.success.title : 'Correct!'),
              ex.success && ex.success.sub ? el('div', { className: 'mrb-fifa__success-s' }, ex.success.sub) : null,
            ]),
          ]));
        }
        body.appendChild(el('button', { className: 'mrb-fifa__restart', attrs: { type: 'button' },
          on: { click: function () { st.cur = 0; st.vals = {}; st.status = {}; render(); } } }, '↻ Start over'));
      }
    }
    render();
    return { render: render };
  }

  NS.fifaStepReveal = { init: init };
})();
