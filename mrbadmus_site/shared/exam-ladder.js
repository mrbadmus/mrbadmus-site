/* ============================================================
   MrBadmus — EXAM LADDER  (Bonding v2 Phase 2B · MRB-136)

   architecture_v2 Law 6: every page ends in the four-rung ladder
     ① recall check  → the existing .rd-exam MCQ set (recognition)
     ② apply         → deduce / calculate (FormulaDeducer, short-tariff writes)
     ③ explain       → chain assembly (ChainBuilder)
     ④ extended      → write-then-self-mark (WriteThenMark, BeTheExaminer)
   Recognition feeds the ladder; production tops it, because AQA
   pays for production.

   This file is the SPINE, not an engine. It:
     · reads the authored content module for the page
       (window.MrbExamContent[<page>], loaded from shared/exam-content/)
     · filters by build tier, sorts items into rungs
     · lays out the rung chrome and the per-item card shell
     · owns persistence and "retry my misses" (Law 8)
   The three engines register themselves into it and render only
   the inside of a card.

   MOUNT (generator emits this, the module builds the rest):
     <div class="mrb-ladder" data-page="ionic-bonding"
          data-tier="higher" data-pathway="triple"></div>

   ENGINE CONTRACT:
     MrbExamLadder.register('chain', {
       label : 'Build the chain',       // kind chip on the card
       rung  : 3,                       // default rung for this kind
       build : function (item, ctx) { ... return DOM node ... }
     });
   ctx gives the engine: page, tier, pathway, content, util, store,
   and report(itemId, award, outOf) — the single way a result is
   recorded. Engines never touch localStorage themselves.

   PERSISTENCE (Law 8 — never punish: no streaks, no timers, no XP):
     mrb_ladder_<page>    per-item awards, survives reload, drives
                          "retry my misses"
     writemark_best_<page> / chain_best_<page> / formula_best_<page>
                          best marks per engine, for the score + delta
============================================================ */
(function () {
  'use strict';
  if (window.MrbExamLadder) return;

  /* ---------- helpers (house style: shared/tap-match.js) ---------- */
  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) {
      if (attrs.className) n.className = attrs.className;
      if (attrs.html) n.innerHTML = attrs.html;
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

  function shuffle(a) {
    var arr = a.slice();
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr;
  }

  /* The authored files quote some strings ("…") as their own device and
     leave others bare. Both are verbatim source; strip the wrapper only
     for display so the five pages read alike. Never mutate the data. */
  function dequote(s) {
    if (typeof s !== 'string') return s;
    var t = s.trim();
    if (t.length > 1 && /^["“]/.test(t) && /["”]$/.test(t)) return t.slice(1, -1);
    return s;
  }

  /* Stems are transcribed with AQA's printed "[6 marks]" tail. The card
     already shows a tariff chip, so drop the duplicate at render time. */
  function stripTariff(s) {
    if (typeof s !== 'string') return s;
    return s.replace(/\s*\[\s*\d+\s*marks?\s*\]\s*$/i, '');
  }

  function plural(n, one, many) { return n === 1 ? one : many; }

  /* ---------- author-facing note suppression ----------
     The authored files are working documents as well as content. Their note
     fields mix two audiences: teaching the student is meant to read, and
     filing the AUTHOR needs — where an item came from, which grade it
     discriminates, what it cross-refers to in the source file. The second
     kind must never render. This is the same class as the "[HIGHER]" leak
     that cleanHeading() already fixes in write-then-mark.js; the rule is
     generalised here so every engine gets it from one place.

     Three passes, coarsest first, and all of them at RENDER time only — the
     authored data keeps every word, because that filing is how Mide
     navigates his own source files.

       1. Whole-note provenance. A note that is nothing but a parenthesised
          source tag — "(frozen Q1)", "(frozen Higher Q — bridges to
          FormulaDeducer §5)", "(to 1D, [3 marks])" — is dropped entirely.
          "(to: <the question> [4 marks])" goes too: buildExaminer already
          prints the target question above it, so the note only ever
          restates it and adds the author's mark split.

       2. Inline cross-references. "(see §2)", "(see §2 levels)", "(see 1D)",
          "(MP3)", "(frozen Triple-Higher)" point at places in the source
          file or at mark-point numbers the student is never shown. Cut the
          reference, keep the sentence around it.

       3. Author-register sentences. A sentence that talks ABOUT the student
          in the third person ("Tests whether the student can hold two force
          types apart"), grades the item ("Grade 8/9 discriminator"), files
          it ("Cross-page: this is also frozen Q on…", "Transfer variants:
          …", "Directly examinable"), or cites a ticket (MRB-135) is
          addressed to the author. Dropped at sentence granularity so a
          mixed note keeps its teaching half.

     If nothing substantive survives, the caller renders no box at all — an
     empty panel saying nothing is worse than no panel. */

  var PROVENANCE_NOTE = /^\s*\(\s*(?:frozen\b|to[\s:]|all three are the frozen\b|complements\s+MRB-|starter item\b)[\s\S]*\)\s*$/i;

  var CROSS_REF = new RegExp([
    '\\s*\\(\\s*see\\s+[^)]*\\)',                 /* (see §2) (see §2 levels) (see 1D) */
    '\\s*[—–,;-]?\\s*see\\s+(?:§\\s*)?\\d+[A-Za-z]?\\b',  /* "— see 1D", "see §2" mid-sentence */
    '\\s*\\(\\s*MP\\s*\\d+[^)]*\\)',              /* (MP3) (MP4) */
    '\\s*\\(\\s*frozen[^)]*\\)',                  /* (frozen Triple-Higher) */
    '\\s*\\(\\s*MRB-\\d+[^)]*\\)'                 /* (MRB-135 exemplar PIC-11) */
  ].join('|'), 'ig');

  /* One match anywhere in the sentence makes it author register. Deliberately
     narrow: "the student" in the third person is the giveaway, whereas "you"
     or an imperative is teaching. "Award any 6" and "Indicative content" are
     NOT here — a student marking their own answer is doing exactly the job
     that mark-scheme vocabulary is for. */
  var AUTHOR_REGISTER = [
    /\b(?:a|the)\s+student\b/i,                     /* "Tests whether the student…" */
    /\bgrade[\s-]?\d(?:\s*[/-]\s*\d)?\b/i,          /* "Grade 8/9 discriminator" */
    /\bcross-page\b/i,
    /\btransfer variants\b/i,
    /\bdirectly examinable\b/i,
    /\bMRB-\d+/,
    /\bfrozen\s+(?:q\d*|higher|triple|foundation|examiner|set)\b/i,
    /\bthe council\b/i,                             /* the authoring review panel */
    /\bmarquee\b/i,

    /* Bare filing labels: a shorthand tag with no teaching in it, left where
       a sentence would go. Observed in the authored set; extend this list
       when a new one shows up rather than widening the rules above. */
    /^\s*two-structure contrast\b/i
  ];

  function isAuthorSentence(s) {
    for (var i = 0; i < AUTHOR_REGISTER.length; i++) {
      if (AUTHOR_REGISTER[i].test(s)) return true;
    }
    return false;
  }

  /* Split on sentence ends, keeping the delimiter so a surviving sentence
     keeps its full stop. A stop that closes a quotation ends the sentence
     too — 'hide behind "covalent = strong = high MP." Award any 6.' is two
     sentences with two different audiences, and splitting it is what lets
     the second one survive. A stop mid-token (a decimal, "e.g.") is not a
     boundary, because the next character is not space or a closing quote. */
  function sentences(s) {
    var out = [], buf = '', i, next;
    for (i = 0; i < s.length; i++) {
      buf += s.charAt(i);
      if (!/[.!?;]/.test(s.charAt(i))) continue;
      next = s.charAt(i + 1);
      if (/["”'’]/.test(next)) { buf += next; i++; next = s.charAt(i + 1); }
      if (next === '' || /\s/.test(next)) { out.push(buf); buf = ''; }
    }
    if (buf.trim()) out.push(buf);
    return out;
  }

  /* studentNote(raw) -> a string safe to show, or null for "render nothing". */
  function studentNote(raw) {
    if (typeof raw !== 'string' || !raw.trim()) return null;
    if (PROVENANCE_NOTE.test(raw.trim())) return null;

    var kept = [];
    sentences(raw.replace(CROSS_REF, '')).forEach(function (s) {
      if (!isAuthorSentence(s)) kept.push(s.trim());
    });

    var out = kept.join(' ')
      .replace(/\s{2,}/g, ' ')
      .replace(/\(\s*\)/g, '')            /* a parenthetical emptied by pass 2 */
      .replace(/\s+([.,;:!?])/g, '$1')
      .replace(/^[\s;:,.—-]+/, '')
      .trim();

    /* Nothing but punctuation or a bare connective left is not a note. */
    if (!/[a-z0-9]/i.test(out)) return null;
    return out;
  }

  /* ---------- progressive disclosure (revision #7) ----------
     One collapsed row: tap the label to open the body. Deliberately the same
     shape and language as the compare-reveal theory block so the ladder reads
     as part of the page, not a bolted-on widget. Reference material collapses;
     the thing the student is actively doing never does. */
  function reveal(label, body, openCue, shutCue) {
    var open = false;
    var cue = el('span', { className: 'mrb-reveal__cue' }, (shutCue || 'show') + ' ▼');
    var wrap = el('div', { className: 'mrb-reveal__body' }, body);
    var row = el('div', { className: 'mrb-reveal__row' });
    var btn = el('button', {
      className: 'mrb-reveal__btn',
      attrs: { type: 'button', 'aria-expanded': 'false' },
      on: {
        click: function () {
          open = !open;
          btn.setAttribute('aria-expanded', open ? 'true' : 'false');
          cue.textContent = (open ? (openCue || 'hide') : (shutCue || 'show')) + (open ? ' ▲' : ' ▼');
          row.classList.toggle('is-open', open);
          if (open) row.appendChild(wrap); else if (wrap.parentNode) row.removeChild(wrap);
        }
      }
    }, [el('span', null, label), cue]);
    row.appendChild(btn);
    return row;
  }

  function revealGroup(rows) {
    return el('div', { className: 'mrb-reveal' }, rows);
  }

  /* ---------- persistence ---------- */
  /* v2 (revision round): FormulaDeducer changed from "check as many times as
     you like" to "the first reveal is the one that counts", so a v1 formula
     mark no longer means what it used to. Rather than migrate a score whose
     meaning changed, v1 is invalidated cleanly — read returns {} and the next
     write stamps v2. This is device-local practice data, not a graded record,
     so a silent fresh start costs the student nothing and cannot crash the
     new UI on stale keys. */
  var STORE_V = 2;
  function ladderKey(page) { return 'mrb_ladder_' + page; }

  function readAll(page) {
    try {
      var raw = localStorage.getItem(ladderKey(page));
      if (!raw) return {};
      var o = JSON.parse(raw);
      if (!o || o.v !== STORE_V || !o.items) return {};
      return o.items;
    } catch (e) { return {}; }
  }

  /* Drop a stale or unparseable key outright at boot rather than leaving it to
     rot until the next write. readAll() already refuses to trust it, so this
     is tidiness, not safety — but a key that says v1 forever is a key someone
     will one day misread as live data. */
  function purgeStale(page) {
    try {
      var raw = localStorage.getItem(ladderKey(page));
      if (!raw) return;
      var o = null;
      try { o = JSON.parse(raw); } catch (e) { o = null; }
      if (!o || o.v !== STORE_V || !o.items) localStorage.removeItem(ladderKey(page));
    } catch (e) {}
  }

  function writeAll(page, items) {
    try { localStorage.setItem(ladderKey(page), JSON.stringify({ v: STORE_V, items: items })); } catch (e) {}
  }

  function readItem(page, id) {
    var all = readAll(page);
    return all[id] || null;
  }

  function writeItem(page, id, award, outOf) {
    var all = readAll(page);
    all[id] = { a: award, o: outOf };
    writeAll(page, all);
  }

  function clearItem(page, id) {
    var all = readAll(page);
    delete all[id];
    writeAll(page, all);
  }

  function bestKey(prefix, page) { return prefix + '_best_' + page; }

  function readBest(prefix, page) {
    try { var v = parseInt(localStorage.getItem(bestKey(prefix, page)), 10); return isNaN(v) ? null : v; } catch (e) { return null; }
  }

  function writeBest(prefix, page, v) {
    try {
      var prev = readBest(prefix, page);
      if (prev == null || v > prev) { localStorage.setItem(bestKey(prefix, page), String(v)); return true; }
    } catch (e) {}
    return false;
  }

  /* ---------- engine registry ---------- */
  var ENGINES = {};
  function register(name, def) { ENGINES[name] = def; }

  /* ---------- rung definitions (Law 6) ---------- */
  var RUNGS = [
    { n: 1, numeral: '①', title: 'Recall check',
      blurb: 'Recognition — the question set above. It feeds the ladder; it is not the top of it.' },
    { n: 2, numeral: '②', title: 'Apply',
      blurb: 'Deduce and construct. Short-tariff answers and formula building.' },
    { n: 3, numeral: '③', title: 'Explain',
      blurb: 'Assemble the causal chain in the order an examiner reads it.' },
    { n: 4, numeral: '④', title: 'Extended response',
      blurb: 'Write it out, then mark it against the real scheme. Reading the scheme against your own words is the learning.' }
  ];

  /* Which rung an authored item sits on. Demand, not engine:
     an item can carry an explicit `rung` and that always wins. */
  function rungFor(kind, item) {
    if (item && item.rung) return item.rung;
    if (kind === 'formula') return 2;
    if (kind === 'chain') return 3;
    if (kind === 'examiner') return 4;
    if (kind === 'write') return (item.tariff || 0) >= 4 ? 4 : 2;
    return 2;
  }

  /* ---------- styles ---------- */
  var STYLE_ID = 'mrb-exam-ladder-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '.mrb-ladder,.mrb-ladder *{box-sizing:border-box}',
      '.mrb-ladder{font-family:var(--font-body,system-ui,sans-serif);color:var(--ink-body,#2A241E)}',
      '.mrb-ladder__intro{margin:0 0 18px;font-size:calc(14.5px * var(--rd-fs-scale,1));line-height:1.55;color:var(--ink-body,#2A241E);max-width:70ch}',

      /* progress strip */
      '.mrb-ladder__strip{display:flex;gap:8px;flex-wrap:wrap;list-style:none;margin:0 0 22px;padding:0}',
      '.mrb-ladder__step{display:flex;align-items:center;gap:7px;font-family:var(--font-mono,monospace);font-size:calc(11.5px * var(--rd-fs-scale,1));font-weight:600;letter-spacing:.04em;padding:7px 13px;border-radius:999px;border:1px solid var(--border,#E4DCCB);background:var(--surface-inset,#F7F2E8);color:#716A60}',
      '.mrb-ladder__step.is-live{border-color:var(--accent-tint-border,#F0BBA9);background:var(--accent-wash,#FBEEE9);color:var(--accent-deep,#B5341A)}',
      '.mrb-ladder__step.is-done{border-color:var(--ok-border,#7FB98A);background:var(--ok-bg,#E7F3EA);color:var(--ok,#2E6B3A)}',
      '.mrb-ladder__step-n{font-size:calc(13px * var(--rd-fs-scale,1))}',

      /* rung block — revision #7: more air between rungs and between cards */
      '.mrb-ladder__rung{margin:0 0 52px}',
      '.mrb-ladder__rung:last-of-type{margin-bottom:34px}',
      '.mrb-ladder__rung-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-bottom:4px}',
      '.mrb-ladder__rung-n{font-family:var(--font-display,sans-serif);font-size:calc(20px * var(--rd-fs-scale,1));color:var(--accent-deep,#B5341A);line-height:1}',
      '.mrb-ladder__rung-t{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(17px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);margin:0}',
      '.mrb-ladder__rung-count{font-family:var(--font-mono,monospace);font-size:calc(11.5px * var(--rd-fs-scale,1));color:#716A60;margin-left:auto}',
      '.mrb-ladder__rung-blurb{margin:0 0 22px;font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.5;color:#6B635A;max-width:66ch}',
      '.mrb-ladder__items{display:flex;flex-direction:column;gap:28px}',

      /* recall rung is a pointer back to the question set, not a duplicate bank */
      '.mrb-ladder__recall{border:1px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);background:var(--surface-inset,#F7F2E8);padding:18px 22px;font-size:calc(14px * var(--rd-fs-scale,1));line-height:1.55}',
      '.mrb-ladder__recall a{color:var(--accent-deep,#B5341A);font-weight:600}',

      /* item card shell */
      '.mrb-lc{border:1px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);background:var(--surface-panel,#FFFDF8);box-shadow:var(--shadow-panel,0 22px 50px -35px rgba(60,30,20,.5));overflow:hidden}',
      '.mrb-lc[data-state="done"]{border-color:var(--ok-border,#7FB98A)}',
      '.mrb-lc[data-state="miss"]{border-color:var(--err-border,#E0897B)}',
      '.mrb-lc__head{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding:14px 22px;border-bottom:1px solid var(--surface-inset,#EFE7D8);background:var(--surface-card,#F5F1E8)}',
      '.mrb-lc__kind{font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--accent-deep,#B5341A)}',
      '.mrb-lc__chip{font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:600;letter-spacing:.06em;color:#6B635A;border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);border-radius:999px;padding:3px 10px}',
      /* revision #6: the Higher tier chip is gone. Tier FILTERING is unchanged
         and lives in visible() — students are already inside their tier, so
         the badge was noise. Do not reintroduce a tier label here. */
      '.mrb-lc__score{margin-left:auto;font-family:var(--font-mono,monospace);font-size:calc(12px * var(--rd-fs-scale,1));font-weight:700;padding:5px 12px;border-radius:999px;white-space:nowrap;background:var(--surface-inset,#EFE7D8);color:#6B635A}',
      '.mrb-lc__score.is-done{background:var(--ok-bg,#E7F3EA);color:var(--ok,#2E6B3A)}',
      '.mrb-lc__score.is-miss{background:var(--err-bg,#FBE4DE);color:var(--err,#A83824)}',
      '.mrb-lc__body{padding:24px 24px 26px}',

      /* revision #4/5: every card says what it is about before its content */
      '.mrb-lc__subject{font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--accent-deep,#B5341A);margin:0 0 12px;padding-bottom:11px;border-bottom:1px solid var(--surface-inset,#EFE7D8)}',

      /* revision #3: the task is the loudest thing on the card */
      '.mrb-lc__task{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(19px * var(--rd-fs-scale,1));line-height:1.35;color:var(--ink,#1A1714);margin:0 0 10px;max-width:44ch}',

      /* shared inner furniture the engines reuse */
      '.mrb-lc__stem{font-size:calc(15px * var(--rd-fs-scale,1));line-height:1.6;color:var(--ink,#1A1714);margin:0 0 6px;max-width:68ch}',
      '.mrb-lc__meta{font-size:calc(12.5px * var(--rd-fs-scale,1));line-height:1.5;color:#716A60;margin:0 0 20px;max-width:68ch}',
      '.mrb-lc__actions{display:flex;gap:10px;margin-top:22px;flex-wrap:wrap}',

      /* periodic-table toggle sits above everything the engine renders */
      '.mrb-lc__tools{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 18px}',

      /* revision #7: progressive disclosure, matching the compare-reveal
         theory block (.mrb-tb-reveal__* in shared/heroes/theory-blocks.js) */
      '.mrb-reveal{display:flex;flex-direction:column;gap:9px;margin:16px 0}',
      '.mrb-reveal__row{border:1px solid var(--border,#E4DCCB);border-radius:12px;overflow:hidden;background:var(--surface-panel,#FFFDF8)}',
      '.mrb-reveal__btn{display:flex;align-items:center;justify-content:space-between;gap:12px;width:100%;text-align:left;cursor:pointer;border:none;background:var(--surface-panel,#FFFDF8);padding:13px 16px;font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(14px * var(--rd-fs-scale,1));color:var(--ink,#1A1714)}',
      '.mrb-reveal__row.is-open .mrb-reveal__btn{background:var(--surface-inset,#F7F2E8)}',
      '.mrb-reveal__btn:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:-2px}',
      '.mrb-reveal__cue{font-family:var(--font-mono,monospace);font-size:calc(11.5px * var(--rd-fs-scale,1));font-weight:600;color:var(--accent-deep,#B5341A);flex:none}',
      '.mrb-reveal__body{padding:4px 16px 15px;font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.55;color:var(--ink-body,#2A241E)}',
      '.mrb-btn{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(14.5px * var(--rd-fs-scale,1));color:#fff;background:var(--accent-deep,#B5341A);border:none;padding:12px 22px;border-radius:12px;cursor:pointer;box-shadow:0 8px 20px -8px rgba(181,52,26,.7)}',
      '.mrb-btn[disabled]{opacity:.45;cursor:default;box-shadow:none}',
      '.mrb-btn--quiet{color:#4A4238;background:var(--surface-inset,#EFE7D8);border:1px solid var(--border,#E4DCCB);box-shadow:none;font-weight:600}',
      '.mrb-btn:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-note{border-radius:14px;padding:13px 17px;font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.55;margin-top:14px}',
      '.mrb-note--ok{background:var(--ok-bg,#E7F3EA);border-left:4px solid var(--ok,#2E6B3A);color:#20522B}',
      '.mrb-note--err{background:var(--err-bg,#FBE4DE);border-left:4px solid var(--err,#A83824);color:#7C2A19}',
      '.mrb-note--tip{background:#FEF6E0;border-left:4px solid #E0A21A;color:#4A3A12}',
      '.mrb-note--plain{background:var(--surface-inset,#F7F2E8);border-left:4px solid var(--border,#E4DCCB);color:var(--ink-body,#2A241E)}',
      '.mrb-note b{font-family:var(--font-display,sans-serif)}',
      '.mrb-slug{font-family:var(--font-mono,monospace);font-size:.85em;color:#8A8074}',
      '.mrb-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}',

      /* end panel */
      '.mrb-ladder__end{display:none;border-radius:var(--r-panel,22px);padding:20px 24px;font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(15px * var(--rd-fs-scale,1));line-height:1.55;margin-top:8px}',
      '.mrb-ladder__end.is-win{background:var(--ok-bg,#E7F3EA);color:#20522B}',
      '.mrb-ladder__end.is-mid{background:#FEF6E0;color:#4A3A12}',
      '.mrb-ladder__end.is-low{background:var(--err-bg,#FBE4DE);color:#7C2A19}',
      '.mrb-ladder__actions{display:flex;gap:12px;margin-top:18px;flex-wrap:wrap}',
      /* The optional group carries no horizontal padding: its cards must line
         up with the core cards above it, or the ladder reads as two columns.
         Revision #7 asked for one consistent card width down the page. */
      '.mrb-ladder__optional{margin-top:28px;border-top:1px dashed var(--border,#E4DCCB);padding:0;background:none}',
      '.mrb-ladder__optional > summary{cursor:pointer;font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(14.5px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);padding:18px 0 4px}',
      '.mrb-ladder__optional > summary::marker{color:var(--accent-deep,#B5341A)}',
      '.mrb-ladder__optional .mrb-ladder__items{margin:18px 0 6px}'
    ].join('');
    document.head.appendChild(s);
  }

  /* ---------- card shell ---------- */
  function makeCard(opts) {
    /* opts: kind, label, tariff, command, ao, subject, periodicTable, itemId.
       No tier option — revision #6 removed the badge; tier still decides
       WHICH items reach this function, via visible(). */
    var score = el('span', { className: 'mrb-lc__score' }, opts.tariff ? ('0 / ' + opts.tariff) : 'not started');
    var head = el('div', { className: 'mrb-lc__head' }, [
      el('span', { className: 'mrb-lc__kind' }, opts.kind),
      opts.label ? el('span', { className: 'mrb-lc__chip' }, opts.label) : null,
      opts.tariff ? el('span', { className: 'mrb-lc__chip' }, opts.tariff + ' ' + plural(opts.tariff, 'mark', 'marks')) : null,
      opts.command ? el('span', { className: 'mrb-lc__chip' }, opts.command + (opts.ao ? ' · ' + opts.ao : '')) : null,
      score
    ]);
    var body = el('div', { className: 'mrb-lc__body' });
    var root = el('article', { className: 'mrb-lc', attrs: { 'data-item': opts.itemId } }, [head, body]);
    return {
      subject: opts.subject,
      periodicTable: !!opts.periodicTable,
      root: root,
      body: body,
      setScore: function (award, outOf) {
        score.textContent = award + ' / ' + outOf;
        score.className = 'mrb-lc__score ' + (award >= outOf ? 'is-done' : 'is-miss');
        root.setAttribute('data-state', award >= outOf ? 'done' : 'miss');
      },
      reset: function () {
        score.textContent = opts.tariff ? ('0 / ' + opts.tariff) : 'not started';
        score.className = 'mrb-lc__score';
        root.removeAttribute('data-state');
      }
    };
  }

  /* ---------- content selection ---------- */
  function visible(item, tier) {
    /* Higher-tagged items render on Higher builds only; everything else
       renders everywhere. Foundation-accessible items are tagged 'any'
       in the authored data (see the graphene/fullerene caveat). */
    return item.tier !== 'higher' || tier === 'higher';
  }

  function collect(content, tier) {
    var out = [];
    function push(kind, list) {
      (list || []).forEach(function (item) {
        if (!visible(item, tier)) return;
        out.push({ kind: kind, item: item, rung: rungFor(kind, item), optional: !!item.optional });
      });
    }
    push('write', content.writeThenMark);
    push('examiner', content.beTheExaminer);
    push('chain', content.chains);
    push('formula', content.formula);
    return out;
  }

  function bestPrefix(kind) {
    if (kind === 'chain') return 'chain';
    if (kind === 'formula') return 'formula';
    return 'writemark';
  }

  /* ---------- init ---------- */
  function init(root) {
    var page = root.dataset.page || '';
    var tier = root.dataset.tier || 'foundation';
    var pathway = root.dataset.pathway || 'combined';
    var content = (window.MrbExamContent || {})[page];
    if (!content) return;

    purgeStale(page);
    ensureStyles();

    var entries = collect(content, tier);
    if (!entries.length) return;

    var cards = {};       // itemId -> { card, entry, rebuild }
    var order = [];       // itemId in render order

    var endPanel = el('div', { className: 'mrb-ladder__end' });
    var retryBtn = el('button', {
      className: 'mrb-btn', attrs: { type: 'button' },
      style: { display: 'none' },
      on: { click: function () { retryMisses(); } }
    }, '↻ Retry my misses');
    var resetBtn = el('button', {
      className: 'mrb-btn mrb-btn--quiet', attrs: { type: 'button' },
      style: { display: 'none' },
      on: { click: function () { startOver(); } }
    }, 'Start over');
    var strip = el('ol', { className: 'mrb-ladder__strip' });
    var stepEls = {};

    var ctx = {
      page: page,
      tier: tier,
      pathway: pathway,
      content: content,
      util: {
        el: el, shuffle: shuffle, dequote: dequote, stripTariff: stripTariff,
        studentNote: studentNote,
        plural: plural, reveal: reveal, revealGroup: revealGroup
      },
      store: {
        readItem: function (id) { return readItem(page, id); },
        readBest: function (prefix) { return readBest(prefix, page); }
      },
      report: function (itemId, award, outOf) {
        writeItem(page, itemId, award, outOf);
        var c = cards[itemId];
        if (c) c.card.setScore(award, outOf);
        refresh();
      }
    };

    /* --- build one card --- */
    function buildCard(entry) {
      var engine = ENGINES[entry.kind];
      if (!engine) return null;
      var item = entry.item;
      var card = makeCard({
        kind: engine.label,
        label: item.label || item.id,
        tariff: engine.tariff ? engine.tariff(item) : item.tariff,
        command: item.command,
        ao: item.ao,
        /* engines declare these as functions, matching the tariff() shape */
        subject: engine.subject ? engine.subject(item, ctx) : null,
        periodicTable: engine.needsTable ? !!engine.needsTable(item, ctx) : false,
        itemId: item.id
      });
      cards[item.id] = { card: card, entry: entry, engine: engine };
      if (order.indexOf(item.id) === -1) order.push(item.id);
      renderInto(item.id);
      return card.root;
    }

    function renderInto(itemId) {
      var c = cards[itemId];
      if (!c) return;
      c.card.body.innerHTML = '';
      c.card.reset();
      /* revision #4/5: the card names its subject before anything else.
         revision #2: the periodic table sits above the task, so it is there
         when the student needs it rather than found after they are stuck. */
      if (c.card.subject) {
        c.card.body.appendChild(el('p', { className: 'mrb-lc__subject' }, String(c.card.subject)));
      }
      if (c.card.periodicTable && window.MrbPeriodicTable) {
        c.card.body.appendChild(el('div', { className: 'mrb-lc__tools' },
          window.MrbPeriodicTable.button()));
      }
      var node = c.engine.build(c.entry.item, ctx);
      if (node) c.card.body.appendChild(node);
      var saved = readItem(page, itemId);
      if (saved) c.card.setScore(saved.a, saved.o);
    }

    /* --- rungs --- */
    var wrap = el('div');

    wrap.appendChild(el('p', { className: 'mrb-ladder__intro' },
      'Recognition got you here. These four rungs are where the marks actually live: ' +
      'deduce it, order it, then write it and mark it against the real scheme.'));
    wrap.appendChild(strip);

    RUNGS.forEach(function (rung) {
      var mine = entries.filter(function (e) { return e.rung === rung.n; });
      var core = mine.filter(function (e) { return !e.optional; });
      var extra = mine.filter(function (e) { return e.optional; });
      if (rung.n !== 1 && !mine.length) return;

      var countEl = el('span', { className: 'mrb-ladder__rung-count' });
      var sec = el('section', { className: 'mrb-ladder__rung', attrs: { 'data-rung': String(rung.n) } }, [
        el('div', { className: 'mrb-ladder__rung-head' }, [
          el('span', { className: 'mrb-ladder__rung-n' }, rung.numeral),
          el('h3', { className: 'mrb-ladder__rung-t' }, rung.title),
          countEl
        ]),
        el('p', { className: 'mrb-ladder__rung-blurb' }, rung.blurb)
      ]);

      if (rung.n === 1) {
        var best = readBest('quiz', page);
        var recall = el('div', { className: 'mrb-ladder__recall' });
        recall.appendChild(document.createTextNode(
          best == null
            ? 'Do the question set above first — it is rung ① of this ladder. '
            : 'Question set above: best so far ' + best + ' marks. '
        ));
        recall.appendChild(el('a', { attrs: { href: '#rd-test' } }, 'Back to the questions ↑'));
        sec.appendChild(recall);
        countEl.textContent = 'recognition';
      } else {
        var list = el('div', { className: 'mrb-ladder__items' });
        core.forEach(function (e) {
          var node = buildCard(e);
          if (node) list.appendChild(node);
        });
        sec.appendChild(list);

        if (extra.length) {
          /* Mide's ruling: the polyatomic set ships as a Higher-weighted
             OPTIONAL group — not core, not cut. */
          var optList = el('div', { className: 'mrb-ladder__items' });
          extra.forEach(function (e) {
            var node = buildCard(e);
            if (node) optList.appendChild(node);
          });
          sec.appendChild(el('details', { className: 'mrb-ladder__optional' }, [
            el('summary', null, 'Optional stretch · ' + extra.length + ' more (' +
              (extra[0].item.set === 'polyatomic' ? 'ions that travel as a group — brackets matter' : 'beyond the core set') + ')'),
            optList
          ]));
        }
        countEl.textContent = mine.length + ' ' + plural(mine.length, 'item', 'items');
      }

      wrap.appendChild(sec);
    });

    wrap.appendChild(endPanel);
    wrap.appendChild(el('div', { className: 'mrb-ladder__actions' }, [retryBtn, resetBtn]));
    root.appendChild(wrap);

    /* --- progress strip --- */
    RUNGS.forEach(function (rung) {
      if (rung.n !== 1 && !entries.some(function (e) { return e.rung === rung.n; })) return;
      var step = el('li', { className: 'mrb-ladder__step' }, [
        el('span', { className: 'mrb-ladder__step-n' }, rung.numeral),
        el('span', null, rung.title),
        el('span', { className: 'mrb-ladder__step-state' }, '')
      ]);
      stepEls[rung.n] = step;
      strip.appendChild(step);
    });

    /* --- state roll-up --- */
    function totals() {
      var done = 0, award = 0, outOf = 0, missed = [];
      order.forEach(function (id) {
        var saved = readItem(page, id);
        var c = cards[id];
        var max = c && c.engine.tariff ? c.engine.tariff(c.entry.item) : (c && c.entry.item.tariff) || 1;
        outOf += max;
        if (saved) {
          done++;
          award += saved.a;
          if (saved.a < saved.o) missed.push(id);
        }
      });
      return { done: done, total: order.length, award: award, outOf: outOf, missed: missed };
    }

    function refresh() {
      var t = totals();

      RUNGS.forEach(function (rung) {
        var step = stepEls[rung.n];
        if (!step) return;
        var state = step.querySelector('.mrb-ladder__step-state');
        if (rung.n === 1) {
          var qb = readBest('quiz', page);
          step.className = 'mrb-ladder__step' + (qb != null ? ' is-done' : '');
          state.textContent = qb != null ? ' ✓' : '';
          return;
        }
        var mine = order.filter(function (id) { return cards[id].entry.rung === rung.n; });
        var attempted = mine.filter(function (id) { return !!readItem(page, id); });
        step.className = 'mrb-ladder__step' +
          (mine.length && attempted.length === mine.length ? ' is-done' : attempted.length ? ' is-live' : '');
        state.textContent = mine.length ? ' ' + attempted.length + '/' + mine.length : '';
      });

      /* per-engine bests (Law 8 / spec §5) */
      ['write', 'examiner', 'chain', 'formula'].forEach(function (kind) {
        var ids = order.filter(function (id) { return cards[id].entry.kind === kind; });
        if (!ids.length) return;
        var all = ids.every(function (id) { return !!readItem(page, id); });
        if (!all) return;
        var sum = 0;
        ids.forEach(function (id) { sum += readItem(page, id).a; });
        writeBest(bestPrefix(kind), page, sum);
      });

      if (t.done < t.total) {
        endPanel.style.display = 'none';
        retryBtn.style.display = t.missed.length ? '' : 'none';
        resetBtn.style.display = t.done ? '' : 'none';
        return;
      }

      var ratio = t.outOf ? t.award / t.outOf : 0;
      var msg = t.award + '/' + t.outOf + ' across the ladder';
      if (ratio === 1) {
        msg += ' — every mark, including the production ones. That is the hard half of this page done.';
      } else if (ratio >= 0.75) {
        msg += ' — strong. Retry your ' + t.missed.length + ' ' + plural(t.missed.length, 'miss', 'misses') +
               ' and read each scheme line you did not award yourself.';
      } else if (ratio >= 0.5) {
        msg += ' — the ideas are there; the marks are in the wording. Retry your misses with the marking points open.';
      } else {
        msg += ' — go back through the theory blocks, then retry your misses. Writing is a separate skill from recognising.';
      }
      endPanel.textContent = msg;
      endPanel.className = 'mrb-ladder__end ' + (ratio === 1 ? 'is-win' : ratio >= 0.6 ? 'is-mid' : 'is-low');
      endPanel.style.display = 'block';
      retryBtn.style.display = t.missed.length ? '' : 'none';
      resetBtn.style.display = '';
    }

    function retryMisses() {
      var t = totals();
      if (!t.missed.length) return;
      t.missed.forEach(function (id) {
        clearItem(page, id);
        renderInto(id);
      });
      endPanel.style.display = 'none';
      refresh();
      var first = cards[t.missed[0]];
      if (first && first.card.root.scrollIntoView) first.card.root.scrollIntoView({ block: 'center' });
    }

    function startOver() {
      order.forEach(function (id) { clearItem(page, id); renderInto(id); });
      endPanel.style.display = 'none';
      refresh();
    }

    refresh();
  }

  /* ---------- boot ---------- */
  function boot() {
    Array.prototype.slice.call(document.querySelectorAll('.mrb-ladder')).forEach(init);
  }

  window.MrbExamLadder = {
    register: register,
    init: init,
    util: { el: el, shuffle: shuffle, dequote: dequote, stripTariff: stripTariff,
            studentNote: studentNote, plural: plural }
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
