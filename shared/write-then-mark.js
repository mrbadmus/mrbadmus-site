/* ============================================================
   MrBadmus — WRITE-THEN-MARK  (Bonding v2 Phase 2B · MRB-136)

   Two registrations into the exam-ladder kernel, one core:

     'write'     WriteThenMark   — you write it, then you mark it
                                   against the real scheme.
     'examiner'  BeTheExaminer   — you mark someone ELSE's answer,
                                   and you are scored on how close
                                   your marking was to the examiner's.

   BeTheExaminer is deliberately NOT a fourth engine. It is a thin
   framing layer over the same marking-point tick list, because the
   skill is identical: hold a real answer against a real scheme and
   decide, line by line, what it earned. Only the ownership of the
   answer changes.

   ── THE ONE RULE THAT MUST NEVER BE RELAXED ──────────────────
   The free text is NEVER auto-graded. No fuzzy matching, no
   keyword scoring, no similarity heuristic, no model call. The
   textarea is inspected for exactly one thing: is it non-empty
   enough to count as an attempt. The learning event IS the student
   reading the mark scheme against their own words and deciding
   "did I say that?" — grading it away deletes the lesson and
   replaces it with a number. Anyone tempted to add scoring here
   should add a better mark scheme instead.
   ─────────────────────────────────────────────────────────────

   Self-award is capped at item.tariff. Seven marking points on a
   6-marker is normal AQA indicative content; the cap is what makes
   an honest self-mark possible.

   Slugs (doNotAccept[].slug, doNotAccept[].altSlugs[],
   misconceptionsShown[], misconceptionsAvoided[]) are verbatim join
   keys into the MRB-135 MCQ banks. They render character-for-
   character into .mrb-slug via text nodes. Never reformat one.

   Nothing here mutates the item or anything under ctx.content — the
   authored content is shared and is read-only.
============================================================ */
(function () {
  'use strict';
  if (!window.MrbExamLadder) return;

  var LADDER = window.MrbExamLadder;
  var U = LADDER.util;          /* el, shuffle, dequote, stripTariff, plural */
  var el = U.el;

  var MIN_CHARS = 20;           /* attempt gate — a token amount, not a quality bar */

  /* ---------- styles ---------- */
  var STYLE_ID = 'mrb-wtm-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '.mrb-wtm,.mrb-wtm *{box-sizing:border-box}',
      '.mrb-wtm{font-family:var(--font-body,system-ui,sans-serif);color:var(--ink-body,#2A241E)}',

      /* framing */
      '.mrb-wtm__eyebrow{font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#716A60;margin:0 0 8px}',
      '.mrb-wtm__frame{font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.55;color:var(--ink-body,#2A241E);background:var(--surface-inset,#F7F2E8);border-left:4px solid var(--accent-deep,#B5341A);border-radius:12px;padding:11px 15px;margin:0 0 14px;max-width:68ch}',
      '.mrb-wtm__q-lbl{font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#716A60;margin:0 0 6px}',

      /* the write surface */
      '.mrb-wtm__lbl{display:block;font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(13.5px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);margin:14px 0 7px}',
      '.mrb-wtm__ta{display:block;width:100%;min-height:150px;resize:vertical;font-family:var(--font-body,system-ui,sans-serif);font-size:calc(14.5px * var(--rd-fs-scale,1));line-height:1.6;color:var(--ink-body,#2A241E);background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);border-radius:14px;padding:13px 15px}',
      '.mrb-wtm__ta:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-wtm__gate{font-size:calc(12.5px * var(--rd-fs-scale,1));line-height:1.5;color:#716A60;margin:8px 0 0}',
      '.mrb-wtm__link{font-family:var(--font-body,system-ui,sans-serif);font-size:calc(12.5px * var(--rd-fs-scale,1));color:#6B635A;background:none;border:none;padding:6px 2px;cursor:pointer;text-decoration:underline}',
      '.mrb-wtm__link:hover{color:var(--accent-deep,#B5341A)}',
      '.mrb-wtm__link:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px;border-radius:6px}',
      '.mrb-wtm__prev{font-family:var(--font-mono,monospace);font-size:calc(11.5px * var(--rd-fs-scale,1));color:#716A60;margin:0 0 12px}',

      /* the student answer under examination */
      '.mrb-wtm__answer{margin:0 0 4px;background:var(--surface-inset,#F7F2E8);border:1px solid var(--border,#E4DCCB);border-left:4px solid var(--accent-tint-border,#F0BBA9);border-radius:14px;padding:14px 18px;font-size:calc(14.5px * var(--rd-fs-scale,1));line-height:1.62;color:var(--ink-body,#2A241E);max-width:70ch}',
      '.mrb-wtm__answer-by{display:block;font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#716A60;margin-bottom:7px}',

      /* scheme sections */
      '.mrb-wtm__scheme{margin-top:20px;border-top:1px solid var(--surface-inset,#EFE7D8);padding-top:18px}',
      '.mrb-wtm__sec{margin-top:18px}',
      '.mrb-wtm__sec-h{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(14px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);margin:0 0 9px}',
      '.mrb-wtm__strand{font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent-deep,#B5341A);margin:14px 0 7px}',
      '.mrb-wtm__strand:first-child{margin-top:0}',

      /* marking points */
      '.mrb-wtm__pts{display:flex;flex-direction:column;gap:7px}',
      '.mrb-wtm__pt{display:flex;align-items:flex-start;gap:11px;border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);border-radius:12px;padding:11px 13px;cursor:pointer}',
      '.mrb-wtm__pt:focus-within{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-wtm__cb{flex:none;width:18px;height:18px;margin:2px 0 0;accent-color:var(--accent-deep,#B5341A);cursor:pointer}',
      '.mrb-wtm__pt-b{flex:1 1 auto;min-width:0}',
      '.mrb-wtm__pt-t{display:block;font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.5;color:var(--ink-body,#2A241E)}',
      '.mrb-wtm__tag{display:inline-block;margin-top:5px;font-family:var(--font-mono,monospace);font-size:calc(10px * var(--rd-fs-scale,1));letter-spacing:.05em;color:#716A60;border:1px dashed var(--border,#E4DCCB);border-radius:999px;padding:2px 9px}',
      '.mrb-wtm__mk{flex:none;font-family:var(--font-mono,monospace);font-weight:700;font-size:calc(14px * var(--rd-fs-scale,1));line-height:1.4;color:#8A8074}',
      '.mrb-wtm__pt.is-hit{border-color:var(--ok-border,#7FB98A);background:var(--ok-bg,#E7F3EA)}',
      '.mrb-wtm__pt.is-hit .mrb-wtm__mk{color:var(--ok,#2E6B3A)}',
      '.mrb-wtm__pt.is-wrong{border-color:var(--err-border,#E0897B);background:var(--err-bg,#FBE4DE)}',
      '.mrb-wtm__pt.is-wrong .mrb-wtm__mk{color:var(--err,#A83824)}',
      '.mrb-wtm__pt.is-open{border-color:#E0A21A;background:#FEF6E0}',
      '.mrb-wtm__pt.is-open .mrb-wtm__mk{color:#8A5E0A}',
      '.mrb-wtm__pt.is-quiet{opacity:.72}',
      '.mrb-wtm__pt.is-locked{cursor:default}',
      '.mrb-wtm__key{font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));line-height:1.7;color:#716A60;margin:9px 0 0}',

      /* the running self-award */
      '.mrb-wtm__count{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(15px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);background:var(--surface-inset,#F7F2E8);border:1px solid var(--border,#E4DCCB);border-radius:12px;padding:12px 16px;margin-top:14px}',
      '.mrb-wtm__count small{display:block;font-family:var(--font-body,system-ui,sans-serif);font-weight:400;font-size:calc(12px * var(--rd-fs-scale,1));line-height:1.5;color:#716A60;margin-top:4px}',

      /* levels */
      '.mrb-wtm__level{margin-top:14px;border:1px solid var(--accent-tint-border,#F0BBA9);background:var(--accent-wash,#FBEEE9);border-radius:14px;padding:14px 17px}',
      '.mrb-wtm__level-n{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(14.5px * var(--rd-fs-scale,1));color:var(--accent-deep,#B5341A);margin:0 0 6px}',
      '.mrb-wtm__level-d{font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.55;color:var(--ink-body,#2A241E);margin:0;max-width:68ch}',
      '.mrb-wtm__bands{margin:10px 0 0;padding:0;list-style:none;display:flex;flex-direction:column;gap:8px}',
      '.mrb-wtm__band{font-size:calc(13px * var(--rd-fs-scale,1));line-height:1.5;border-left:3px solid var(--border,#E4DCCB);padding-left:11px}',
      '.mrb-wtm__band b{font-family:var(--font-display,sans-serif);color:var(--ink,#1A1714)}',

      /* plain content lists (allow / do-not-accept / cap failures / misconceptions) */
      '.mrb-wtm__list{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:8px}',
      '.mrb-wtm__li{font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.55;padding-left:15px;position:relative;max-width:68ch}',
      '.mrb-wtm__li::before{content:"";position:absolute;left:0;top:.62em;width:5px;height:5px;border-radius:50%;background:var(--border,#E4DCCB)}',
      '.mrb-wtm__li--ok::before{background:var(--ok,#2E6B3A)}',
      '.mrb-wtm__li--no::before{background:var(--err,#A83824)}',
      '.mrb-wtm__li-note{color:#716A60;font-style:italic}',
      '.mrb-wtm__slugs{display:block;margin-top:3px}',

      /* examiner verdict furniture */
      '.mrb-wtm__nums{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}',
      '.mrb-wtm__num{font-family:var(--font-mono,monospace);font-weight:700;font-size:calc(14px * var(--rd-fs-scale,1));min-width:46px;padding:10px 14px;border-radius:12px;border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);color:var(--ink,#1A1714);cursor:pointer}',
      '.mrb-wtm__num[aria-pressed="true"]{border-color:var(--accent-deep,#B5341A);background:var(--accent-wash,#FBEEE9);color:var(--accent-deep,#B5341A);box-shadow:0 0 0 2px var(--accent-tint,#FBE0D6)}',
      '.mrb-wtm__num:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-wtm__num[disabled]{opacity:.5;cursor:default}',
      '.mrb-wtm__quote{margin:14px 0 0;border-left:4px solid var(--accent-deep,#B5341A);background:var(--surface-inset,#F7F2E8);border-radius:0 14px 14px 0;padding:13px 17px;font-size:calc(14px * var(--rd-fs-scale,1));line-height:1.6;color:var(--ink-body,#2A241E);max-width:68ch}',
      '.mrb-wtm__quote-by{display:block;font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#716A60;margin-bottom:6px}',
      '.mrb-wtm__verdict{font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));letter-spacing:.05em;color:#716A60;margin:14px 0 0}',
      '.mrb-wtm__mis-s{display:block;margin-top:3px;color:var(--ink-body,#2A241E)}'
    ].join('');
    document.head.appendChild(s);
  }

  /* ---------- small read-only helpers ---------- */

  function txt(s) { return document.createTextNode(String(s)); }

  /* A slug is a join key into the MCQ banks. It goes to the DOM as a raw
     text node inside .mrb-slug so it survives byte-for-byte. */
  function slugEl(slug) {
    return el('span', { className: 'mrb-slug' }, String(slug));
  }

  /* Both field shapes ship in the authored data: tierNote is a plain
     string (ionic-bonding, giant-covalent, metals-alloys) and tierNotes
     is a {foundation, higher} object (properties-*). Handle both; for the
     object form show only the note matching the build tier. */
  function tierNoteFor(item, tier) {
    if (typeof item.tierNote === 'string' && item.tierNote) return item.tierNote;
    var tn = item.tierNotes;
    if (!tn) return null;
    if (typeof tn === 'string') return tn;
    return tn[tier] || null;
  }

  /* Levels rows carry marks:[lo,hi] and are authored high-to-low, including
     a level-0 row at [0,0]. First containing band wins. */
  function bandFor(item, award) {
    var bands = item.levels || [], found = null;
    bands.forEach(function (b) {
      if (found) return;
      var m = b.marks || [];
      if (typeof m[0] === 'number' && typeof m[1] === 'number' && award >= m[0] && award <= m[1]) found = b;
    });
    return found;
  }

  function bandName(b) {
    if (!b) return '';
    return b.levelLabel ? String(b.levelLabel) : ('Level ' + b.level);
  }

  /* Misconceptions resolve by slug, or by membership of a slugs[] alias
     list (ionic-bonding folds several MCQ slugs onto one statement). */
  function findMisconception(ctx, slug) {
    var list = (ctx.content && ctx.content.misconceptions) || [], found = null;
    list.forEach(function (m) {
      if (found) return;
      if (m.slug === slug) found = m;
      else if (m.slugs && m.slugs.indexOf(slug) !== -1) found = m;
    });
    return found;
  }

  function section(heading, node) {
    if (!node) return null;
    return el('div', { className: 'mrb-wtm__sec' }, [
      el('h5', { className: 'mrb-wtm__sec-h' }, heading),
      node
    ]);
  }

  function plainList(items, modifier) {
    if (!items || !items.length) return null;
    var ul = el('ul', { className: 'mrb-wtm__list' });
    items.forEach(function (s) {
      ul.appendChild(el('li', { className: 'mrb-wtm__li' + (modifier ? ' ' + modifier : '') }, String(s)));
    });
    return ul;
  }

  /* doNotAccept rows: {text}, {text,slug}, {text,slug,note}, {text,slug,altSlugs[]}.
     Every slug present on the row reaches the DOM verbatim. */
  function doNotAcceptList(items) {
    if (!items || !items.length) return null;
    var ul = el('ul', { className: 'mrb-wtm__list' });
    items.forEach(function (d) {
      var row = el('li', { className: 'mrb-wtm__li mrb-wtm__li--no' });
      row.appendChild(txt(typeof d === 'string' ? d : d.text));
      if (d && d.note) {
        row.appendChild(txt(' '));
        row.appendChild(el('span', { className: 'mrb-wtm__li-note' }, '(' + d.note + ')'));
      }
      var slugs = [];
      if (d && d.slug) slugs.push(d.slug);
      if (d && d.altSlugs) d.altSlugs.forEach(function (s) { slugs.push(s); });
      if (slugs.length) {
        var holder = el('span', { className: 'mrb-wtm__slugs' });
        slugs.forEach(function (s, i) {
          if (i) holder.appendChild(txt(' · '));
          holder.appendChild(slugEl(s));
        });
        row.appendChild(holder);
      }
      ul.appendChild(row);
    });
    return ul;
  }

  function misconceptionList(ctx, slugs, framing) {
    if (!slugs || !slugs.length) return null;
    var ul = el('ul', { className: 'mrb-wtm__list' });
    slugs.forEach(function (s) {
      var m = findMisconception(ctx, s);
      var row = el('li', { className: 'mrb-wtm__li mrb-wtm__li--no' }, [slugEl(s)]);
      /* statements are authored with their own internal quote marks and are
         NOT dequoted — stripping the wrapper would mangle the "A" / "B" form. */
      if (m && m.statement) row.appendChild(el('span', { className: 'mrb-wtm__mis-s' }, m.statement));
      if (framing) row.appendChild(el('span', { className: 'mrb-wtm__mis-s mrb-wtm__li-note' }, framing));
      ul.appendChild(row);
    });
    return ul;
  }

  /* ---------- the shared core: the marking-point tick list ----------
     Used unchanged by both engines. In 'write' the student ticks what
     their own answer said; in 'examiner' they tick what someone else's
     answer earned. Same control, same marks, different owner. */
  function tickList(points, onChange) {
    var wrap = el('div', { className: 'mrb-wtm__pts' });
    var rows = [];
    var lastStrand = null;

    points.forEach(function (p) {
      var strand = p.strand || null;
      if (strand && strand !== lastStrand) wrap.appendChild(el('h6', { className: 'mrb-wtm__strand' }, strand));
      lastStrand = strand;

      var cb = el('input', { className: 'mrb-wtm__cb', attrs: { type: 'checkbox' } });
      var mk = el('span', { className: 'mrb-wtm__mk', attrs: { 'aria-hidden': 'true' } }, '');
      var sr = el('span', { className: 'mrb-sr' }, '');

      var tags = [];
      if (p.essential === false) tags.push('creditworthy elaboration');
      if (p.tag) tags.push(String(p.tag));

      /* implicit label association: the checkbox lives inside its <label>,
         so the whole row is a hit target and no generated ids are needed
         (ids would have to be unique across re-renders). */
      var row = el('label', { className: 'mrb-wtm__pt' }, [
        cb,
        el('span', { className: 'mrb-wtm__pt-b' }, [
          el('span', { className: 'mrb-wtm__pt-t' }, p.text),
          tags.length ? el('span', { className: 'mrb-wtm__tag' }, tags.join(' · ')) : null
        ]),
        mk, sr
      ]);
      if (onChange) cb.addEventListener('change', onChange);
      rows.push({ p: p, cb: cb, mk: mk, sr: sr, row: row });
      wrap.appendChild(row);
    });

    return {
      node: wrap,
      rows: rows,
      count: function () {
        var n = 0;
        rows.forEach(function (r) { if (r.cb.checked) n++; });
        return n;
      },
      lock: function () {
        rows.forEach(function (r) {
          r.cb.disabled = true;
          r.row.className += ' is-locked';
        });
      }
    };
  }

  /* ---------- 'write' — WriteThenMark ---------- */
  function buildWrite(item, ctx) {
    ensureStyles();

    var tariff = item.tariff || 1;
    var root = el('div', { className: 'mrb-wtm' });

    if (item.heading) {
      root.appendChild(el('p', { className: 'mrb-wtm__eyebrow' },
        item.heading + (item.headingNote ? ' · ' + item.headingNote : '')));
    }
    root.appendChild(el('p', { className: 'mrb-lc__stem' }, ctx.util.stripTariff(ctx.util.dequote(item.stem))));
    if (item.note) root.appendChild(el('p', { className: 'mrb-lc__meta' }, ctx.util.dequote(item.note)));

    var prior = ctx.store.readItem(item.id);
    if (prior) {
      root.appendChild(el('p', { className: 'mrb-wtm__prev' },
        'Recorded earlier: ' + prior.a + ' / ' + prior.o + ' — marking it again replaces that.'));
    }

    /* --- the write surface --- */
    var ta = el('textarea', {
      className: 'mrb-wtm__ta',
      attrs: {
        rows: '7',
        placeholder: 'Write your full answer here, in exam conditions, before you look at the scheme.'
      }
    });
    root.appendChild(el('label', null, [
      el('span', { className: 'mrb-wtm__lbl' }, 'Your answer'),
      ta
    ]));

    var gate = el('p', { className: 'mrb-wtm__gate', attrs: { 'aria-live': 'polite' } },
      'Write at least ' + MIN_CHARS + ' characters to unlock the mark scheme.');
    root.appendChild(gate);

    var revealBtn = el('button', { className: 'mrb-btn', attrs: { type: 'button' } }, 'Reveal the mark scheme');
    revealBtn.disabled = true;
    var skipBtn = el('button', { className: 'mrb-wtm__link', attrs: { type: 'button' } },
      'I would rather just see the scheme');
    var actions = el('div', { className: 'mrb-lc__actions' }, [revealBtn, skipBtn]);
    root.appendChild(actions);

    var slot = el('div');
    root.appendChild(slot);

    /* The ONLY inspection of the free text anywhere in this file: length.
       Never read it for meaning. See the header rule. */
    function gateCheck() {
      var n = String(ta.value || '').replace(/\s+/g, ' ').trim().length;
      var ok = n >= MIN_CHARS;
      revealBtn.disabled = !ok;
      gate.textContent = ok
        ? 'Attempt logged. Reveal the scheme and mark yourself honestly — nobody sees this but you.'
        : 'Write at least ' + MIN_CHARS + ' characters to unlock the mark scheme (' + (MIN_CHARS - n) + ' to go).';
    }
    ta.addEventListener('input', gateCheck);

    revealBtn.addEventListener('click', function () { reveal(true); });
    skipBtn.addEventListener('click', function () { reveal(false); });

    /* --- the scheme --- */
    function reveal(attempted) {
      revealBtn.disabled = true;
      skipBtn.disabled = true;
      actions.style.display = 'none';
      ta.readOnly = true;
      slot.innerHTML = '';

      var scheme = el('div', { className: 'mrb-wtm__scheme' });
      slot.appendChild(scheme);

      scheme.appendChild(el('h4', { className: 'mrb-wtm__sec-h' },
        attempted
          ? 'The mark scheme — tick every point your answer actually made'
          : 'The mark scheme'));

      if (!attempted) {
        scheme.appendChild(el('div', { className: 'mrb-note mrb-note--plain' },
          'You have not attempted this one, so there is nothing to mark and nothing is recorded. ' +
          'Read it through, then come back and write it cold — the marks live in the writing, not the reading.'));
      }

      var points = item.markingPoints || [];
      var list = null;

      if (attempted) {
        list = tickList(points, function () { sync(); });
        scheme.appendChild(list.node);
      } else {
        /* read-only rendering: no controls, no award, no report */
        var ro = el('ul', { className: 'mrb-wtm__list' });
        var seen = null;
        points.forEach(function (p) {
          if (p.strand && p.strand !== seen) ro.appendChild(el('h6', { className: 'mrb-wtm__strand' }, p.strand));
          if (p.strand) seen = p.strand;
          var li = el('li', { className: 'mrb-wtm__li mrb-wtm__li--ok' }, [txt(p.text)]);
          var tags = [];
          if (p.essential === false) tags.push('creditworthy elaboration');
          if (p.tag) tags.push(String(p.tag));
          if (tags.length) li.appendChild(el('span', { className: 'mrb-wtm__tag mrb-wtm__slugs' }, tags.join(' · ')));
          ro.appendChild(li);
        });
        scheme.appendChild(ro);
      }

      var countEl = null, levelSlot = null, recordBtn = null;

      if (attempted) {
        countEl = el('div', { className: 'mrb-wtm__count', attrs: { 'aria-live': 'polite' } });
        scheme.appendChild(countEl);
      }

      var allowNode = plainList(item.allow, 'mrb-wtm__li--ok');
      if (allowNode) scheme.appendChild(section('An examiner would also accept…', allowNode));

      var noNode = doNotAcceptList(item.doNotAccept);
      if (noNode) scheme.appendChild(section('An examiner would NOT credit…', noNode));

      if (item.levels && item.levels.length) {
        if (attempted) {
          levelSlot = el('div');
          scheme.appendChild(section('Where that puts you', levelSlot));
        } else {
          var bands = el('ul', { className: 'mrb-wtm__bands' });
          item.levels.forEach(function (b) {
            bands.appendChild(el('li', { className: 'mrb-wtm__band' }, [
              el('b', null, bandName(b) + ' · ' + b.marks[0] + '–' + b.marks[1] + ' marks'),
              txt(' ' + b.descriptor)
            ]));
          });
          scheme.appendChild(section('The level bands for this question', bands));
        }

        var capNode = plainList(item.capFailures, 'mrb-wtm__li--no');
        if (capNode) {
          scheme.appendChild(section(
            item.capFailuresHeading || 'What would have stopped you reaching the top band',
            capNode));
        }
      }

      if (attempted) {
        recordBtn = el('button', { className: 'mrb-btn', attrs: { type: 'button' } }, 'Record this mark');
        var done = el('p', { className: 'mrb-wtm__gate', attrs: { 'aria-live': 'polite' } }, '');
        recordBtn.addEventListener('click', function () {
          var award = Math.min(list.count(), tariff);
          ctx.report(item.id, award, tariff);
          recordBtn.textContent = 'Update this mark';
          done.textContent = 'Recorded ' + award + ' / ' + tariff +
            '. Change a tick and press again if you want to revise it.';
        });
        scheme.appendChild(el('div', { className: 'mrb-lc__actions' }, [recordBtn]));
        scheme.appendChild(done);
      }

      /* tier notes, transfer notes and authoring checks close the card */
      var tn = tierNoteFor(item, ctx.tier);
      if (tn) {
        scheme.appendChild(el('div', { className: 'mrb-note mrb-note--plain' }, [
          el('b', null, (ctx.tier === 'higher' ? 'Higher tier' : 'Foundation tier') + ' · '),
          txt(tn)
        ]));
      }
      if (item.transferNote) {
        scheme.appendChild(el('div', { className: 'mrb-note mrb-note--plain' }, [
          el('b', null, 'Transfers to · '),
          txt(item.transferNote)
        ]));
      }
      if (item.check === true && item.checkNote) {
        scheme.appendChild(el('div', { className: 'mrb-note mrb-note--tip' }, [
          el('b', null, 'Authoring note, flagged for examiner check · '),
          txt(item.checkNote)
        ]));
      }

      function sync() {
        var raw = list.count();
        var award = Math.min(raw, tariff);
        countEl.innerHTML = '';
        countEl.appendChild(txt('You have awarded yourself ' + award + ' / ' + tariff));
        countEl.appendChild(el('small', null,
          raw > tariff
            ? 'You ticked ' + raw + ' points. This question has ' + points.length +
              ' marking points but only ' + tariff + ' marks, so it caps at ' + tariff + '.'
            : 'Tick a point only if your own words actually said it. Nothing here reads your answer — this mark is yours to set honestly.'));

        if (levelSlot) {
          levelSlot.innerHTML = '';
          var b = bandFor(item, award);
          if (b) {
            levelSlot.appendChild(el('div', { className: 'mrb-wtm__level' }, [
              el('p', { className: 'mrb-wtm__level-n' }, bandName(b) + ' · ' + award + ' / ' + tariff),
              el('p', { className: 'mrb-wtm__level-d' }, b.descriptor)
            ]));
          }
        }
      }

      if (attempted) sync();
    }

    gateCheck();
    return root;
  }

  /* ---------- 'examiner' — BeTheExaminer ----------
     Same tick list, different chair. The score is marking accuracy. */
  function buildExaminer(item, ctx) {
    ensureStyles();

    var outOf = item.outOf || 1;
    var official = typeof item.officialMark === 'number' ? item.officialMark : 0;

    /* resolve the question this answer was written for */
    var target = null;
    if (item.targetItemId) {
      ((ctx.content && ctx.content.writeThenMark) || []).forEach(function (w) {
        if (w.id === item.targetItemId) target = w;
      });
    }
    var points = (target && target.markingPoints) || null;

    var root = el('div', { className: 'mrb-wtm' });

    root.appendChild(el('p', { className: 'mrb-wtm__frame' },
      'You are the examiner. Below is another student’s answer. Decide what it earned, ' +
      'then see what the real examiner gave it. Your score is how close your marking was — ' +
      'not the mark the answer got.'));

    root.appendChild(el('p', { className: 'mrb-wtm__q-lbl' }, 'The question this answer was given to'));
    if (target) {
      root.appendChild(el('p', { className: 'mrb-lc__stem' }, ctx.util.stripTariff(ctx.util.dequote(target.stem))));
    } else if (item.targetPrompt) {
      /* ionic-bonding ib-be2 has no sibling WriteThenMark item — it marks a
         formula deduction, so the prompt is carried inline and there are no
         marking points to tick. */
      root.appendChild(el('p', { className: 'mrb-lc__stem' }, ctx.util.stripTariff(ctx.util.dequote(item.targetPrompt))));
    } else {
      root.appendChild(el('p', { className: 'mrb-lc__stem' }, 'Question worth ' + outOf + ' ' + ctx.util.plural(outOf, 'mark', 'marks') + '.'));
    }
    /* ib-be2's note restates its targetPrompt word for word; printing both
       reads as a rendering fault. Show the note only when it adds something. */
    var meta = item.note ? ctx.util.dequote(item.note) : null;
    if (meta && item.targetPrompt && meta.indexOf(item.targetPrompt) !== -1) meta = null;
    if (meta) root.appendChild(el('p', { className: 'mrb-lc__meta' }, meta));

    root.appendChild(el('blockquote', { className: 'mrb-wtm__answer' }, [
      el('span', { className: 'mrb-wtm__answer-by' }, 'The answer you are marking'),
      txt(ctx.util.dequote(item.studentAnswer))
    ]));

    var list = null;
    var chosen = null;          /* the mark the student commits to */
    var auto = true;            /* it tracks the ticks until the student overrides it */
    var numBtns = [];

    var countEl = el('div', { className: 'mrb-wtm__count', attrs: { 'aria-live': 'polite' } });
    var submitBtn = el('button', { className: 'mrb-btn', attrs: { type: 'button' } }, 'Submit my marking');
    var slot = el('div');

    if (points && points.length) {
      list = tickList(points, function () {
        if (auto) chosen = Math.min(list.count(), outOf);
        paintNums();
        sync();
      });
      root.appendChild(section('Which marking points did this answer actually earn?', list.node));
    }

    /* The committed mark is a separate control from the ticks, always.
       Indicative content is not reliably one point / one mark — psm-be1 is
       credited 3 marks off 2 listed points ("2–3 marks" in its own note) —
       so a student who ticks exactly what the examiner credited must still
       be able to commit the mark the examiner actually gave. The ticks
       suggest; the student decides. That is also how examining works. */
    var nums = el('div', { className: 'mrb-wtm__nums' });
    for (var i = 0; i <= outOf; i++) {
      (function (v) {
        var b = el('button', {
          className: 'mrb-wtm__num',
          attrs: { type: 'button', 'aria-pressed': 'false', 'aria-label': v + ' out of ' + outOf }
        }, String(v));
        b.addEventListener('click', function () {
          chosen = v;
          auto = false;
          paintNums();
          sync();
        });
        numBtns.push({ b: b, v: v });
        nums.appendChild(b);
      })(i);
    }

    var markBlock = el('div', null, [nums]);
    if (list) {
      markBlock.appendChild(el('p', { className: 'mrb-wtm__gate' },
        'Ticking sets this for you. Nudge it if you think the answer earned more or less than the ticks ' +
        'suggest — a marking point is not always worth exactly one mark.'));
    }
    root.appendChild(section(
      list ? 'And the mark you would give it, out of ' + outOf
           : 'What mark out of ' + outOf + ' would you give this answer?',
      markBlock));

    root.appendChild(countEl);
    root.appendChild(el('div', { className: 'mrb-lc__actions' }, [submitBtn]));
    root.appendChild(slot);

    function paintNums() {
      numBtns.forEach(function (x) {
        x.b.setAttribute('aria-pressed', x.v === chosen ? 'true' : 'false');
      });
    }

    function proposed() { return chosen; }

    function sync() {
      var p = proposed();
      countEl.innerHTML = '';
      if (p == null) {
        countEl.appendChild(txt(list
          ? 'Tick the points this answer earned, then commit a mark out of ' + outOf + '.'
          : 'Choose a mark out of ' + outOf + '.'));
        submitBtn.disabled = true;
        return;
      }
      submitBtn.disabled = false;
      countEl.appendChild(txt('You would give this answer ' + p + ' / ' + outOf));
      countEl.appendChild(el('small', null,
        'Your own score is ' + outOf + ' minus how far your mark is from the examiner’s, floored at 0. ' +
        'Marking it accurately is the skill being tested here.'));
    }

    submitBtn.addEventListener('click', function () {
      var p = proposed();
      if (p == null) return;
      var gap = Math.abs(p - official);
      var award = Math.max(0, outOf - gap);

      submitBtn.disabled = true;
      submitBtn.style.display = 'none';
      if (list) list.lock();
      numBtns.forEach(function (x) { x.b.disabled = true; });

      /* mark up the tick list against what the examiner actually awarded */
      if (list) {
        var hit = item.pointsHit || [];
        var miss = item.pointsMissed || [];
        list.rows.forEach(function (r) {
          var ticked = r.cb.checked;
          var wasHit = hit.indexOf(r.p.id) !== -1;
          var wasMiss = miss.indexOf(r.p.id) !== -1;
          var cls = '', sym = '', say = '';
          if (wasHit && ticked) { cls = ' is-hit'; sym = '✓'; say = 'Correctly awarded.'; }
          else if (wasHit && !ticked) { cls = ' is-open'; sym = '○'; say = 'There was a mark here and you did not award it.'; }
          else if (ticked && wasMiss) { cls = ' is-wrong'; sym = '✕'; say = 'You awarded this, but the answer did not earn it.'; }
          else if (ticked) { cls = ' is-wrong'; sym = '✕'; say = 'You awarded this; the examiner’s notes do not list it as earned.'; }
          else { cls = ' is-quiet'; sym = '·'; say = 'Correctly withheld.'; }
          r.row.className = 'mrb-wtm__pt is-locked' + cls;
          r.mk.textContent = sym;
          r.sr.textContent = ' ' + say;
        });
        list.node.appendChild(el('p', { className: 'mrb-wtm__key' },
          '✓ correctly awarded  ·  ✕ awarded but not earned  ·  ○ a mark you missed  ·  · correctly withheld'));
      }

      var res = el('div', { className: 'mrb-wtm__scheme' });
      slot.appendChild(res);

      res.appendChild(el('div', { className: 'mrb-note ' + (gap === 0 ? 'mrb-note--ok' : gap <= 1 ? 'mrb-note--tip' : 'mrb-note--err') }, [
        el('b', null, 'The examiner gave it ' + official + ' / ' + outOf + '. '),
        txt(item.markNote ? item.markNote + ' ' : ''),
        txt('You gave it ' + p + ' — ' +
          (gap === 0 ? 'exactly right.' : 'out by ' + gap + ' ' + ctx.util.plural(gap, 'mark', 'marks') + '.') +
          ' Your score: ' + award + ' / ' + outOf + '.')
      ]));

      if (item.pointsHitNote) {
        res.appendChild(section('What it earned', el('p', { className: 'mrb-wtm__level-d' }, item.pointsHitNote)));
      }
      if (item.pointsMissedNote) {
        res.appendChild(section('What it missed', el('p', { className: 'mrb-wtm__level-d' }, item.pointsMissedNote)));
      }

      if (item.examinerLine) {
        res.appendChild(el('blockquote', { className: 'mrb-wtm__quote' }, [
          el('span', { className: 'mrb-wtm__quote-by' }, 'What the examiner would write'),
          txt(ctx.util.dequote(item.examinerLine))
        ]));
      }

      var shown = misconceptionList(ctx, item.misconceptionsShown);
      if (shown) res.appendChild(section('The misconceptions behind the lost marks', shown));

      var avoided = misconceptionList(ctx, item.misconceptionsAvoided,
        'Avoided here, but not resolved — the answer sidesteps it rather than showing it is understood.');
      if (avoided) res.appendChild(section('Avoided, but not resolved', avoided));

      var verdict = item.headingFull || item.heading;
      if (verdict) {
        res.appendChild(el('p', { className: 'mrb-wtm__verdict' },
          'Examiner’s filing: ' + verdict + (item.headingNote ? ' · ' + item.headingNote : '')));
      }

      ctx.report(item.id, award, outOf);
    });

    sync();
    return root;
  }

  /* ---------- registration ---------- */
  LADDER.register('write', {
    label: 'Write & self-mark',
    build: buildWrite
  });

  LADDER.register('examiner', {
    label: 'Be the examiner',
    build: buildExaminer,
    tariff: function (item) { return item.outOf; }
  });
})();
