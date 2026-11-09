/* ═══════════════════════════════════════════════════════════════════════
   consumer/parent-side.js — what the parent-side pages share
   (25 Oct 2026, docs/b2c/parent-side-plan.md).

   Loaded by consumer/family.html (a parent: Home, a child, Past work) and
   consumer/done.html (a child: "Everything you've done"), after
   consumer-common.js. Exposes window.MrBadmusParentSide.

   It turns the API's records into words, and words only from records:
     · an answer's marking state is one of three — SCORED, SELF-CHECKED or
       NOT MARKED — and an answer nobody marked is never "Right";
     · a score counts marked answers only ("7/11 marked · 1 answer not
       marked");
     · a time is shown only where it was measured, and never as a total
       when part of the item went untimed;
     · a work item that saves no answers says "This activity isn't
       tracked yet." — never a blank or a zero;
     · every chip carries a glyph AND a word (colour is never the only
       signal; and no marking state is green — see parent-side.css).

   Nothing here invents a number: every figure is read from a field.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var C = window.MrBadmusConsumer;
  var esc = C.escapeHtml;

  /* Design's glyphs (her `glyph()`), plus `self` for self-checked. */
  var GLYPH = {
    tick: '<path d="M5 12.5l4.5 4.5L19 7"/>',
    cross: '<path d="M6 6l12 12M18 6L6 18"/>',
    tilde: '<path d="M4 13c2.5-4 5.5-4 8 0s5.5 4 8 0"/>',
    dot: '<circle cx="12" cy="12" r="4"/>',
    half: '<circle cx="12" cy="12" r="8"/><path d="M12 4a8 8 0 0 1 0 16z" fill="currentColor" stroke="none"/>',
    dash: '<path d="M7 12h10"/>',
    self: '<circle cx="12" cy="12" r="8" stroke-dasharray="3 3"/><path d="M8.5 12.2l2.4 2.4 4.6-4.8"/>',
    warn: '<path d="M12 3l10 18H2z" stroke-width="2"/><path d="M12 10v5M12 18v.5" stroke-width="2"/>',
    go: '<path d="M9 5l7 7-7 7" stroke-width="2"/>',
    back: '<path d="M15 5l-7 7 7 7" stroke-width="2"/>',
    close: '<path d="M6 6l12 12M18 6L6 18" stroke-width="2"/>'
  };
  function glyph(k, size) {
    if (!GLYPH[k]) { return ''; }
    var s = size || 14;
    return '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" aria-hidden="true" fill="none" ' +
      'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">' + GLYPH[k] + '</svg>';
  }

  /* ── dates (civil YYYY-MM-DD in, British words out) ─────────────────── */
  var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                'September', 'October', 'November', 'December'];
  var MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var WD = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  function civil(ymd) {
    var m = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(ymd || ''));
    return m ? { y: +m[1], m: +m[2], d: +m[3], wd: new Date(Date.UTC(+m[1], +m[2] - 1, +m[3])).getUTCDay() } : null;
  }
  function thisYear() { var t = civil(C.londonYMD()); return t ? t.y : null; }
  /* "28 September" ("28 September 2025" when it is not this year). */
  function weekLabel(ymd) {
    var c = civil(ymd);
    if (!c) { return ''; }
    return c.d + ' ' + MONTHS[c.m - 1] + (c.y !== thisYear() ? ' ' + c.y : '');
  }
  function dayShort(ymd) { var c = civil(ymd); return c ? WD[c.wd] : ''; }
  function dateShort(ymd) { var c = civil(ymd); return c ? (c.d + ' ' + MON[c.m - 1]) : ''; }
  /* The London civil day an instant fell on. */
  function dayOf(iso) { return iso ? C.londonYMD(iso) : null; }

  /* A measured duration. Whole seconds in; "45 s", "6 min 5 s", "1 h 4 min". */
  function fmtSecs(n) {
    if (n == null || isNaN(Number(n))) { return null; }
    n = Math.round(Number(n));
    var h = Math.floor(n / 3600), m = Math.floor((n % 3600) / 60), s = n % 60;
    if (h) { return h + ' h' + (m ? ' ' + m + ' min' : ''); }
    if (m) { return m + ' min' + (s ? ' ' + s + ' s' : ''); }
    return s + ' s';
  }

  var KIND = { lesson: 'Lesson', practice: 'Practice', unit_check: 'Unit check', exam: 'Exam question',
               flashcards: 'Flashcards', challenge: 'Weekly challenge' };
  function kindLabel(k) { return KIND[k] || (k ? String(k).charAt(0).toUpperCase() + String(k).slice(1).replace(/_/g, ' ') : 'Work'); }
  function subjKey(s) {
    var k = String(s || '').toLowerCase();
    return (k === 'biology' || k === 'chemistry' || k === 'physics') ? k : 'none';
  }
  function subjHtml(s) {
    if (!s) { return ''; }
    return '<span class="ps-subj ps-s-' + subjKey(s) + '">' + esc(s) + '</span>';
  }
  function plural(n, one, many) { return n + ' ' + (n === 1 ? one : (many || one + 's')); }

  /* ── what the child saw ─────────────────────────────────────────────── */
  /* ⊕ 9 Nov 2026 (blind run 2): a lesson's quiz option is stored with its reason
     ("180 Pa — multiply the force by the area"), which is its answer key, and
     stays as stored. The page shows it without the reason, by option_labels.py's
     rule. Only the renderers that apply that rule are in QUIZ_ID: a KS3 ladder's
     marked rungs and KS4's practice questions. A lesson's other options were shown
     whole, and a practice set shows its bank's text. The panel holds two of a
     question's options, not all of them, so the rule runs on those two. */
  var QUIZ_ID = /(^ks4q:|#(recall|apply)$|^ks4:.*#(choice-\d+|r1(-\d+)?)$)/;
  function shownOption(a, text) {
    if (text == null || !a || a.surface !== 'lesson' || a.kind !== 'choice' || !QUIZ_ID.test(String(a.question_id || ''))) { return text; }
    var plan = window.MrBadmusOptionPlan;
    if (!plan) { return text; }
    var opts = [[a.answer, false]];
    if (a.correct_answer != null && a.correct_answer !== a.answer) { opts.push([a.correct_answer, true]); }
    opts = opts.filter(function (o) { return o[0] != null; });
    var p = plan(a.question_text || '', opts, null);
    for (var i = 0; i < opts.length; i += 1) { if (opts[i][0] === text) { return p.labels[i]; } }
    return text;
  }

  /* ── one answer ─────────────────────────────────────────────────────── */
  /* scored | self_checked | unmarked. The contract's answer carries
     `outcome` ('unmarked' for anything nobody marked); a self-check is an
     unmarked row whose reason says so. `marking_state` wins if the backend
     sends it. */
  function markState(a) {
    if (!a) { return 'unmarked'; }
    var ms = a.mark_state || a.marking_state;
    if (ms === 'scored' || ms === 'self_checked' || ms === 'unmarked') { return ms; }
    if (a.outcome === 'unmarked' || a.marked_by === 'unmarked') {
      /* Only a written or ordered answer can have been checked by the child
         (consumer/answers.js markState): an older row said so of a tapped choice. */
      return ((a.unmarked_reason === 'self_checked' || a.self_checked === true) && (a.kind === 'written' || a.kind === 'order'))
        ? 'self_checked' : 'unmarked';
    }
    return 'scored';
  }
  function multiMark(a) { return a && Number(a.marks_available) > 1; }
  /* {cls, glyph, word} for one answer. */
  function verdict(a) {
    var st = markState(a);
    if (st === 'unmarked') { return { cls: 'unmarked', glyph: 'dash', word: 'Not marked' }; }
    if (st === 'self_checked') { return { cls: 'self', glyph: 'self', word: 'Self-checked' }; }
    if (multiMark(a) && a.marks_scored != null) {
      var w = a.marks_scored + '/' + a.marks_available;
      if (a.outcome === 'correct') { return { cls: 'right', glyph: 'tick', word: w }; }
      if (a.outcome === 'wrong') { return { cls: 'wrong', glyph: 'cross', word: w }; }
      return { cls: 'part', glyph: 'half', word: w };
    }
    if (a.outcome === 'correct') { return { cls: 'right', glyph: 'tick', word: 'Right' }; }
    if (a.outcome === 'wrong') { return { cls: 'wrong', glyph: 'cross', word: 'Wrong' }; }
    if (a.outcome === 'partial') { return { cls: 'part', glyph: 'half', word: 'Part marks' }; }
    return { cls: 'unmarked', glyph: 'dash', word: 'Not marked' };
  }
  function chip(v, small, extraLabel) {
    return '<span class="ps-chip ps-c-' + v.cls + (small ? ' is-sm' : '') + '"' +
      (extraLabel ? ' aria-label="' + esc(extraLabel) + '"' : '') + '>' + glyph(v.glyph) + esc(v.word) + '</span>';
  }
  function markedBy(a) {
    if (markState(a) !== 'scored') { return ''; }
    if (a.marked_by === 'key') { return 'Marked automatically'; }
    if (a.marked_by === 'ai') { return 'Marked by AI'; }
    /* ⊕ 9 Nov 2026 (F2): 'stub' is the keyword-count fallback, written only
       when the backend has no marking model (no key). A failed model call is
       never a stub. The child's page calls it a practice mark; so does this. */
    if (a.marked_by === 'stub') { return 'Practice mark, the AI marker didn’t check'; }
    return '';
  }

  /* ── one work item ──────────────────────────────────────────────────── */
  function answersOf(it) { return (it && Array.isArray(it.answers)) ? it.answers : []; }
  function isTracked(it) { return !(it && it.tracked === false); }
  /* ⊕ 9 Nov 2026 (F1): answers in no work item, as pieces (`own_work`). They
     are listed and opened like any other and said plainly not to be set work;
     "N of M done" and the week strip never count them. */
  var NOT_SET = 'Not set work';
  function isOwn(it) { return !!(it && it.own_work); }
  /* Everything an activity read holds: set work, then own work. */
  function allItems(act) {
    return ((act && act.work_items) || []).concat((act && act.own_work) || []);
  }
  /* Has this piece saved anything? On a past-work row the answers themselves
     are not sent; the summary says. */
  function hasAnswers(it) {
    return answersOf(it).length > 0 || Number(((it && it.summary) || {}).answered) > 0;
  }
  /* The numbers a row and the panel say, from `summary` (the backend's
     count over every answer row) with the self-check split counted from the
     answers themselves. */
  function itemScore(it) {
    var s = (it && it.summary) || {};
    var ans = answersOf(it);
    var self = s.self_checked != null ? Number(s.self_checked)
      : ans.filter(function (a) { return markState(a) === 'self_checked'; }).length;
    var unmarkedAll = s.unmarked != null ? Number(s.unmarked)
      : ans.filter(function (a) { return markState(a) !== 'scored'; }).length;
    var plain = Math.max(0, unmarkedAll - self);
    var avail = Number(s.marks_available) || 0;
    var scored = Number(s.marks_scored) || 0;
    var parts = [];
    if (avail > 0) { parts.push(scored + '/' + avail + ' marked'); }
    if (plain) { parts.push(plural(plain, 'answer') + ' not marked'); }
    if (self) { parts.push(self + ' self-checked'); }
    return {
      avail: avail, scored: scored, plain: plain, self: self,
      answers: ans.length || Number(s.answered) || 0,
      questions: s.questions != null ? Number(s.questions) : distinctQuestions(ans),
      frac: avail > 0 ? scored / avail : null,
      text: avail > 0 ? (scored + '/' + avail) : '',
      line: parts.join(' · ')
    };
  }
  function distinctQuestions(ans) {
    var seen = {}, n = 0;
    ans.forEach(function (a) { var k = a.question_id || a.id; if (!seen[k]) { seen[k] = 1; n++; } });
    return n;
  }
  /* A measured time, only when every answer in it was measured. */
  function itemTime(it) {
    var s = (it && it.summary) || {};
    if (s.time_seconds == null || s.time_complete === false) { return null; }
    return fmtSecs(s.time_seconds);
  }
  /* The chip for a DONE item. */
  function doneChip(it) {
    if (!isTracked(it)) { return { cls: 'right', glyph: 'tick', word: 'Done' }; }
    var sc = itemScore(it);
    if (sc.avail > 0) {
      var cls = sc.scored >= sc.avail ? 'right' : (sc.scored <= 0 ? 'wrong' : 'part');
      return { cls: cls, glyph: cls === 'right' ? 'tick' : cls === 'wrong' ? 'cross' : 'half', word: sc.text };
    }
    if (sc.self && !sc.plain) { return { cls: 'self', glyph: 'self', word: 'Self-checked' }; }
    if (sc.plain || sc.self) { return { cls: 'unmarked', glyph: 'dash', word: 'Not marked' }; }
    return { cls: 'right', glyph: 'tick', word: 'Done' };
  }
  /* {done, chip, dim} for any item, against `today` (a civil date). Work
     OPENS on its day (B2C unit 7, ruling 1) — nothing is "due". */
  /* Done: the activity's `status`, or — on a past-work row, which carries
     no status because every row there IS done — a done_at / done_day. */
  function isDone(it) {
    return !!it && !it.removed && (it.status === 'done' || (!it.status && !!(it.done_at || it.done_day)));
  }
  function itemState(it, today) {
    if (isDone(it)) { return { done: true, chip: doneChip(it), dim: false }; }
    /* ⊕ 9 Nov 2026 (F8): part-way through, with saved answers. It opens. */
    if (hasAnswers(it)) { return { done: false, dim: false, started: true, chip: { cls: 'ahead', glyph: 'half', word: 'Started' } }; }
    var d = String(it.scheduled_for || '').slice(0, 10);
    if (d && today && d < today) { return { done: false, dim: true, chip: { cls: 'notdone', glyph: 'dash', word: 'Not done' } }; }
    if (d && d === today) { return { done: false, dim: false, chip: { cls: 'today', glyph: 'dot', word: 'Today' } }; }
    return { done: false, dim: false, chip: { cls: 'ahead', glyph: '', word: d ? ('Opens ' + dayShort(d)) : 'Set' } };
  }
  function itemDate(it) { return it.done_day || dayOf(it.done_at) || String(it.scheduled_for || '').slice(0, 10); }
  /* The Monday of a civil date's Mon–Sun week. */
  function mondayOf(ymd) {
    var c = civil(ymd);
    if (!c) { return null; }
    return C.ymdPlusDays(String(ymd).slice(0, 10), -((c.wd + 6) % 7));
  }

  /* ── the work panel: every question ─────────────────────────────────── */
  function groupByQuestion(ans) {
    var order = [], by = {};
    ans.slice().sort(function (a, b) {
      return String(a.answered_at || '').localeCompare(String(b.answered_at || '')) ||
        (a.attempt_no || 0) - (b.attempt_no || 0);
    }).forEach(function (a) {
      var k = a.question_id || a.id;
      if (!by[k]) { by[k] = []; order.push(k); }
      by[k].push(a);
    });
    return order.map(function (k) { return by[k]; });
  }
  function questionHtml(rows, n, who) {
    var last = rows[rows.length - 1];
    var v = verdict(last);
    var kp = last.knowledge_point && last.knowledge_point.label;
    var qtext = last.question_text || rows[0].question_text;
    var body = '<div class="ps-qa">';
    if (rows.length === 1) {
      body += '<span class="k">' + esc(who) + ' answered</span>' +
        '<span class="v said' + (v.cls === 'wrong' ? ' is-wrong' : '') + '">' +
        (last.answer != null && last.answer !== '' ? esc(shownOption(last, last.answer)) : '<span class="ps-muted">No answer given</span>') + '</span>';
    } else {
      body += '<span class="k">' + esc(who) + ' answered</span><ol class="ps-attempts v">' +
        rows.map(function (a, i) {
          var av = verdict(a);
          var t = fmtSecs(a.time_spent_seconds);
          return '<li><span class="ps-mono ps-muted">Attempt ' + (a.attempt_no || (i + 1)) + '</span>' +
            '<span class="said' + (av.cls === 'wrong' ? ' is-wrong' : '') + '" style="font-weight:600">' +
            (a.answer != null && a.answer !== '' ? esc(shownOption(a, a.answer)) : '<span class="ps-muted">No answer given</span>') + '</span>' +
            chip(av, true) + (t ? '<span class="ps-mono ps-muted">' + esc(t) + '</span>' : '') + '</li>';
        }).join('') + '</ol>';
    }
    if (last.correct_answer) {
      body += '<span class="k">Correct answer</span><span class="v">' + esc(shownOption(last, last.correct_answer)) + '</span>';
    } else if (v.cls === 'wrong' || v.cls === 'part') {
      /* ⊕ 9 Nov 2026 (F10): the lesson judged this and saved no right answer
         to show (a typed formula, the concordant titres). Said, not left for
         a parent to go looking. */
      body += '<span class="k">Correct answer</span><span class="v ps-muted">Not tracked yet</span>';
    }
    /* ⊕ 9 Nov 2026 (F4): the child's own self-marking, in their words. It is
       stored apart from the mark and is never a mark. */
    var yourself = who === 'You' ? 'yourself' : 'themselves';
    if (last.self_level != null) {
      body += '<span class="k">Own pick</span><span class="v">Picked Level ' + esc(String(last.self_level)) +
        ' for ' + yourself + ', not marked</span>';
    }
    /* The points ticked, beside any pick. The backend counts them; the array also
       holds the level's own position. */
    var ticked = last.self_points != null ? Number(last.self_points)
      : (Array.isArray(last.self_ticks) ? last.self_ticks.length : 0);
    if (last.kind === 'written' && ticked > 0) {
      body += '<span class="k">Own ticks</span><span class="v">Ticked ' + ticked +
        (last.points_total ? ' of ' + esc(String(last.points_total)) : '') + ' for ' + yourself + ', not marked</span>';
    }
    if (last.mark_level != null && last.mark_level !== '' && markState(last) === 'scored') {
      /* The backend sends the AQA level as a number (0–3); older rows may
         carry the words. Either reads "Level 2". */
      var lv = typeof last.mark_level === 'number' || /^\d+$/.test(String(last.mark_level))
        ? 'Level ' + last.mark_level : String(last.mark_level);
      /* A keyword count's level is not an examiner's (markedBy). */
      body += '<span class="k">' + (last.marked_by === 'stub' ? 'Practice level' : 'AQA level') +
        '</span><span class="v"><strong>' + esc(lv) + '</strong></span>';
    }
    if (last.mark_next_step) {
      body += '<span class="k">Next step</span><span class="v">' + esc(last.mark_next_step) + '</span>';
    }
    if (last.feedback) {
      body += '<span class="k">Feedback</span><span class="v body">' + esc(last.feedback) + '</span>';
    }
    body += '</div>';
    var meta = [];
    meta.push(rows.length === 1 ? ('Attempt ' + (last.attempt_no || 1)) : plural(rows.length, 'attempt'));
    if (rows.length === 1) {
      var t1 = fmtSecs(last.time_spent_seconds);
      if (t1) { meta.push(t1); }
    }
    var mb = markedBy(last);
    if (mb) { meta.push(mb); }
    return '<li class="ps-q">' +
      '<div class="ps-q-top"><span class="ps-q-n" aria-hidden="true">' + n + '</span>' +
        '<div style="flex:1;min-width:0"><p class="ps-q-text"><span class="ps-sr">Question ' + n + ': </span>' +
          (qtext ? esc(qtext) : '<span class="ps-muted">The question text wasn’t saved.</span>') + '</p>' +
          (kp ? '<p class="ps-q-topic">' + esc(kp) + '</p>' : '') + '</div>' +
        chip(v, true) + '</div>' +
      '<div class="ps-q-body">' + body +
        '<p class="ps-q-meta">' + meta.map(function (m) { return '<span>' + esc(m) + '</span>'; }).join('') + '</p>' +
      '</div></li>';
  }
  function panelHtml(it, who) {
    var sc = itemScore(it);
    var t = itemTime(it);
    var date = itemDate(it);
    var tracked = isTracked(it);
    var groups = groupByQuestion(answersOf(it));
    var stats = '';
    if (tracked && groups.length) {
      stats = '<div class="ps-panel-stats">' +
        (sc.line ? '<span><span class="k">' + (sc.avail > 0 ? 'Score' : 'Marking') + '</span> <strong>' + esc(sc.line) + '</strong></span>' : '') +
        (t ? '<span><span class="k">Time</span> <strong>' + esc(t) + '</strong></span>' : '') +
        '<span><span class="k">Questions</span> <strong>' + groups.length + '</strong></span></div>';
    }
    var body;
    if (!tracked) {
      body = '<div class="ps-dashed" style="padding:14px 16px;font-size:15px;color:var(--ks3-ink-body)">' +
        '<strong style="color:var(--ks3-ink)">This activity isn’t tracked yet.</strong></div>';
    } else if (!groups.length) {
      body = '<div class="ps-dashed" style="padding:14px 16px;font-size:15px;color:var(--ks3-ink-body)">' +
        'No answers were given in this one.</div>';
    } else {
      body = '<ol class="ps-qs">' + groups.map(function (rows, i) { return questionHtml(rows, i + 1, who); }).join('') + '</ol>';
    }
    return '<div class="ps-panel-h"><div style="flex:1;min-width:0">' +
        '<p class="ps-eyebrow">' + esc(kindLabel(it.kind)) + (it.subject ? ' · ' + subjHtml(it.subject) : '') +
          (date ? ' · ' + esc(dayShort(date) + ' ' + dateShort(date)) : '') +
          (isOwn(it) ? ' · ' + NOT_SET : '') + '</p>' +
        '<h2 id="ps-panel-title">' + esc(it.title || kindLabel(it.kind)) + '</h2>' + stats + '</div>' +
        '<button type="button" class="ps-iconbtn" data-ps-close aria-label="Close">' + glyph('close', 20) + '</button></div>' +
      '<div class="ps-panel-b">' + body + '</div>';
  }

  /* Opens the panel over the page (side sheet ≥700px, full screen below).
     Escape, the veil and the close button all shut it; focus is held inside
     it and returned to the opener. `onClose` is told. */
  var openNow = null;
  function openPanel(it, who, onClose) {
    closePanel(true);
    var opener = document.activeElement;
    var host = document.querySelector('.ps-root') || document.body;
    var veil = document.createElement('div');
    veil.className = 'ps-veil';
    veil.setAttribute('aria-hidden', 'true');
    var aside = document.createElement('aside');
    aside.className = 'ps-panel';
    aside.setAttribute('role', 'dialog');
    aside.setAttribute('aria-modal', 'true');
    aside.setAttribute('aria-labelledby', 'ps-panel-title');
    aside.innerHTML = panelHtml(it, who);
    host.appendChild(veil);
    host.appendChild(aside);
    var prevOverflow = document.documentElement.style.overflow;
    document.documentElement.style.overflow = 'hidden';
    function onKey(e) {
      if (e.key === 'Escape') { e.preventDefault(); close(); return; }
      if (e.key !== 'Tab') { return; }
      var f = aside.querySelectorAll('button, a[href], [tabindex]:not([tabindex="-1"])');
      if (!f.length) { return; }
      var first = f[0], lastEl = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); lastEl.focus(); }
      else if (!e.shiftKey && document.activeElement === lastEl) { e.preventDefault(); first.focus(); }
    }
    function close(silent) {
      if (!aside.parentNode) { return; }
      document.removeEventListener('keydown', onKey, true);
      veil.parentNode && veil.parentNode.removeChild(veil);
      aside.parentNode.removeChild(aside);
      document.documentElement.style.overflow = prevOverflow;
      openNow = null;
      if (opener && opener.focus && document.contains(opener)) { try { opener.focus(); } catch (e) {} }
      if (!silent && onClose) { onClose(); }
    }
    veil.addEventListener('click', function () { close(); });
    aside.querySelector('[data-ps-close]').addEventListener('click', function () { close(); });
    document.addEventListener('keydown', onKey, true);
    aside.querySelector('[data-ps-close]').focus();
    openNow = close;
    return close;
  }
  function closePanel(silent) { if (openNow) { openNow(silent); } }

  /* ── past work, grouped by week ─────────────────────────────────────── */
  /* The server groups and sorts for a parent (/past-work); the child's
     page, and a backend without that route, group the activity's DONE items
     here by the same rule: weeks newest first (or oldest); highest/lowest by
     the week's marked fraction, weeks with nothing marked last. */
  function groupWeeks(items, sort, subject) {
    /* The backend's buildPastWork rule: DONE items, grouped by the Mon–Sun
       week of the day each was done (London). */
    var by = {}, order = [];
    (items || []).forEach(function (it) {
      if (!isDone(it)) { return; }
      /* A piece whose subject nothing records is under every subject, not none. */
      if (subject && it.subject && it.subject !== subject) { return; }
      var ws = mondayOf(itemDate(it)) || String(it.week_start || '').slice(0, 10);
      if (!by[ws]) { by[ws] = []; order.push(ws); }
      by[ws].push(it);
    });
    var groups = order.map(function (ws) {
      var its = by[ws].slice().sort(itemOrder(sort));
      var s = 0, a = 0, un = 0;
      its.forEach(function (it) {
        var sm = it.summary || {};
        s += Number(sm.marks_scored) || 0; a += Number(sm.marks_available) || 0; un += Number(sm.unmarked) || 0;
      });
      var own = its.filter(isOwn).length;
      return { week_start: ws, label: weekLabel(ws), items: its, done: its.length - own, own_work: own,
               score: { marked_scored: s, marked_available: a, unmarked: un, fraction: a > 0 ? s / a : null } };
    });
    return sortGroups(groups, sort);
  }
  /* Items inside a week: newest done first, or by their own marked
     fraction for highest/lowest (nothing marked last) — the backend's
     buildPastWork rule. */
  function itemFrac(it) {
    var s = (it && it.summary) || {};
    var a = Number(s.marks_available) || 0;
    return a > 0 ? (Number(s.marks_scored) || 0) / a : null;
  }
  function itemOrder(sort) {
    var byDone = function (a, b) { return String(b.done_at || '').localeCompare(String(a.done_at || '')); };
    if (sort === 'oldest') { return function (a, b) { return byDone(b, a); }; }
    if (sort !== 'highest' && sort !== 'lowest') { return byDone; }
    var dir = sort === 'lowest' ? -1 : 1;
    return function (a, b) {
      var fa = itemFrac(a), fb = itemFrac(b);
      if (fa == null && fb == null) { return byDone(a, b); }
      if (fa == null) { return 1; }
      if (fb == null) { return -1; }
      return (dir * (fb - fa)) || byDone(a, b);
    };
  }
  function frac(g) { return g && g.score && g.score.fraction != null ? g.score.fraction : null; }
  function sortGroups(groups, sort) {
    var g = groups.slice();
    if (sort === 'highest' || sort === 'lowest') {
      var scored = g.filter(function (x) { return frac(x) != null; });
      var rest = g.filter(function (x) { return frac(x) == null; });
      scored.sort(function (x, y) { return sort === 'highest' ? frac(y) - frac(x) : frac(x) - frac(y); });
      rest.sort(function (x, y) { return String(y.week_start).localeCompare(String(x.week_start)); });
      return scored.concat(rest);
    }
    g.sort(function (x, y) {
      return sort === 'oldest' ? String(x.week_start).localeCompare(String(y.week_start))
                               : String(y.week_start).localeCompare(String(x.week_start));
    });
    return g;
  }
  function weekSummary(g) {
    var sc = g.score || {};
    var n = g.done != null ? g.done : (g.items || []).length;
    var own = Number(g.own_work) || 0, started = Number(g.started) || 0;
    var bits = [];
    if (n || !(own || started)) { bits.push(n + ' done'); }
    if (started) { bits.push(started + ' started'); }
    if (own) { bits.push(own + ' not set work'); }
    if (sc.marked_available > 0) { bits.push(sc.marked_scored + '/' + sc.marked_available + ' marked'); }
    return bits.join(' · ');
  }

  window.MrBadmusParentSide = {
    glyph: glyph, weekLabel: weekLabel, dayShort: dayShort, dateShort: dateShort, dayOf: dayOf,
    fmtSecs: fmtSecs, kindLabel: kindLabel, subjKey: subjKey, subjHtml: subjHtml, plural: plural,
    markState: markState, verdict: verdict, chip: chip, itemScore: itemScore, itemTime: itemTime,
    itemState: itemState, itemDate: itemDate, mondayOf: mondayOf, isDone: isDone, doneChip: doneChip, isTracked: isTracked,
    isOwn: isOwn, allItems: allItems, hasAnswers: hasAnswers, NOT_SET: NOT_SET, shownOption: shownOption,
    panelHtml: panelHtml, openPanel: openPanel, closePanel: closePanel,
    groupWeeks: groupWeeks, sortGroups: sortGroups, weekSummary: weekSummary
  };
})();
