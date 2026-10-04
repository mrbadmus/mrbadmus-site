/* ═══════════════════════════════════════════════════════════════════════
   consumer/topic-picker.js — ONE topic picker for every parent screen that
   asks "which topic?". B2C onboarding repair, 3 Oct 2026 (Mide's ruling,
   option a).

   Used by: the signup "Where is X up to?" step (consumer/signup.html) and
   the dashboard's Set work screen (consumer/overview.html).

   WHAT IT OFFERS
   ──────────────
   Every KS3 unit and lesson and every GCSE topic and subtopic, from
   /consumer/curriculum-index.json (written by
   tools/export_curriculum_tree.py from the same Python the site is built
   from; `curriculum_tree_mirror` fails if it drifts).

   Two ways in, working on ONE list and ONE selection:
     · type in the search box — it filters;
     · the Subject and Topic dropdowns — they narrow.
   Typing inside a narrowed topic filters that topic's lessons.

   WHAT A PARENT MAY CHOOSE
   ────────────────────────
   Only what is in the child's own scheme of work — the units and lessons
   GET /api/consumer/children/:id/picker returns. Everything else is shown,
   greyed and not selectable, with the year it is taught in:
     · a KS3 unit (and its lessons): the unit's typical year;
     · a GCSE topic or subtopic: the year the child's (pathway, tier) block
       puts it in — "taught at GCSE" when the child is not at GCSE yet.
   When that year cannot be worked out, or it IS the child's own year (the
   plan simply does not hold it), the label says "not in Year N's plan".
   No year is ever hard-coded here.

   The selection handed to `onChange`:
     { level: 'unit'|'lesson', ks: 'ks3'|'ks4',
       subject: the scheme's own subject name (the key its cursors use),
       name, unitName, unitCode (KS3 only), slug (lessons only),
       week (lessons only — the scheme's teaching-order week) }

   ACCESSIBILITY
   ─────────────
   The search box is a WAI-ARIA 1.2 combobox (aria-controls, aria-expanded,
   aria-activedescendant) over an always-visible listbox. Arrow keys move,
   Enter chooses, Escape clears the search. Greyed options are reachable and
   announced (aria-disabled) but cannot be chosen.

   STATE SURVIVES A RE-RENDER
   ──────────────────────────
   Both host pages rebuild their whole screen on every change. `mount()`
   takes a plain `state` object and keeps everything in it, so the host can
   re-mount after its own render and the parent loses nothing.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var SUBJECTS = ['biology', 'chemistry', 'physics'];
  var MAX_ROWS = 60;
  var indexPromise = null;

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function cap(s) { s = String(s || ''); return s.charAt(0).toUpperCase() + s.slice(1); }
  function norm(s) { return String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim(); }

  function loadIndex() {
    if (indexPromise) { return indexPromise; }
    indexPromise = fetch('/consumer/curriculum-index.json', { credentials: 'same-origin' })
      .then(function (r) {
        if (!r.ok) { throw new Error('index ' + r.status); }
        return r.json();
      })
      .catch(function (e) { indexPromise = null; throw e; });
    return indexPromise;
  }

  /* ── years ─────────────────────────────────────────────────────────── */
  function blockKeys(child) {
    var p = (child.pathway || '').toLowerCase();
    var t = (child.tier || '').toLowerCase();
    var keys = [];
    ['c', 't'].forEach(function (pi) {
      ['f', 'h'].forEach(function (ti) {
        if ((!p || p.charAt(0) === pi) && (!t || t.charAt(0) === ti)) { keys.push(pi + ti); }
      });
    });
    return keys;
  }
  function yearsOfSub(map, keys) {
    var out = {};
    keys.forEach(function (k) { if (map && map[k] != null) { out[map[k]] = true; } });
    return Object.keys(out).map(Number).sort();
  }
  function whyText(years, childYear) {
    if (!years.length || years.indexOf(childYear) !== -1) {
      return 'not in Year ' + childYear + '’s plan';
    }
    if (years.length === 1) { return 'taught in Year ' + years[0]; }
    return 'taught in Years ' + years.slice(0, -1).join(', ') + ' and ' + years[years.length - 1];
  }

  /* ⊕ B2C polish (4 Oct 2026). A GCSE item shown to a Years 7–9 child used
     to union every pathway/tier block's year — "taught in Years 10 and 11"
     for Homeostasis, while a Year 10 child on one block read "taught in
     Year 11" for the same topic. Both were true of something, and together
     they read as a contradiction. A child below GCSE has no block yet, so
     the only true thing to say is the stage; a GCSE child keeps the year
     their own block teaches it in. */
  function ks4Why(years, childYear, childKs) {
    return childKs === 'ks3' ? 'taught at GCSE' : whyText(years, childYear);
  }

  /* ── the flat list, built once per (index, child) ──────────────────── */
  function build(index, child, units) {
    var year = Number(child.year) || 0;
    var childKs = year >= 10 ? 'ks4' : 'ks3';
    var keys = childKs === 'ks4' ? blockKeys(child) : ['cf', 'ch', 'tf', 'th'];

    // What the child's scheme holds — only ever their own key stage.
    var schemeUnit = {}, schemeLesson = {};
    (units || []).forEach(function (u) {
      var k = u.unit_code ? ('c:' + String(u.unit_code).toLowerCase()) : ('n:' + norm(u.name));
      schemeUnit[k] = u;
      (u.lessons || []).forEach(function (l) {
        schemeLesson[l.slug] = { week: l.week, unit: u };
      });
    });

    var items = [], topics = [];
    function add(t) { t.idx = items.length; items.push(t); return t; }

    (index.ks3 || []).forEach(function (u) {
      var own = childKs === 'ks3';
      var su = own ? schemeUnit['c:' + String(u.c).toLowerCase()] : null;
      var why = own && su ? '' : whyText([u.y], year);
      var topic = add({
        id: 'ks3-' + u.c, level: 'unit', ks: 'ks3', subject: u.s, name: u.n,
        unitName: su ? su.name : u.n, unitCode: u.c, ok: !!su, why: why,
        schemeSubject: su ? su.subject : null,
        hay: norm(u.n + ' ' + u.c), kids: []
      });
      topics.push(topic);
      (u.l || []).forEach(function (l) {
        var sl = own ? schemeLesson[l[0]] : null;
        // The scheme decides — a lesson the scheme lists under this unit is
        // choosable even when the unit row above is not, and vice versa.
        var ok = !!(sl && sl.unit && String(sl.unit.unit_code || '').toLowerCase() === String(u.c).toLowerCase());
        topic.kids.push(add({
          id: 'ks3-' + u.c + '-' + l[0], level: 'lesson', ks: 'ks3', subject: u.s, name: l[1],
          unitName: topic.unitName, unitCode: u.c, slug: l[0], week: ok ? sl.week : null,
          schemeSubject: ok ? sl.unit.subject : null,
          ok: ok, why: ok ? '' : whyText([u.y], year), parent: topic,
          hay: norm(l[1] + ' ' + u.n)
        }));
      });
    });

    (index.ks4 || []).forEach(function (t) {
      var own = childKs === 'ks4';
      var su = own ? schemeUnit['n:' + norm(t.n)] : null;
      var all = {};
      (t.l || []).forEach(function (l) { yearsOfSub(l[2], keys).forEach(function (y) { all[y] = true; }); });
      var tYears = Object.keys(all).map(Number).sort();
      var topic = add({
        id: 'ks4-' + t.s + '-' + t.id, level: 'unit', ks: 'ks4', subject: t.s, name: t.n,
        unitName: su ? su.name : t.n, unitCode: null, ok: !!su,
        schemeSubject: su ? su.subject : null,
        why: su ? '' : ks4Why(tYears, year, childKs), hay: norm(t.n), kids: []
      });
      topics.push(topic);
      (t.l || []).forEach(function (l) {
        var sl = own ? schemeLesson[l[0]] : null;
        var ok = !!(sl && sl.unit && !sl.unit.unit_code && norm(sl.unit.name) === norm(t.n));
        topic.kids.push(add({
          id: 'ks4-' + t.s + '-' + t.id + '-' + l[0], level: 'lesson', ks: 'ks4', subject: t.s,
          name: l[1], unitName: topic.unitName, unitCode: null, slug: l[0],
          week: ok ? sl.week : null, ok: ok, schemeSubject: ok ? sl.unit.subject : null,
          why: ok ? '' : ks4Why(yearsOfSub(l[2], keys), year, childKs), parent: topic,
          hay: norm(l[1] + ' ' + t.n)
        }));
      });
    });

    return { items: items, topics: topics, childKs: childKs, year: year };
  }

  function selectionOf(it) {
    return {
      level: it.level, ks: it.ks, subject: it.schemeSubject || cap(it.subject), name: it.name,
      unitName: it.unitName, unitCode: it.unitCode || null,
      slug: it.slug || null, week: it.week == null ? null : it.week
    };
  }

  /* ── what to list ──────────────────────────────────────────────────── */
  function visible(model, st) {
    var q = norm(st.q);
    var sel = st.selected ? model.items.filter(function (i) { return i.id === st.selected; })[0] : null;
    // The box shows the chosen item's name after a pick; that is not a search.
    if (sel && q === norm(sel.name)) { q = ''; }
    var words = q ? q.split(' ') : [];
    var inSubject = function (i) { return !st.subject || i.subject === st.subject; };
    var match = function (i) {
      for (var w = 0; w < words.length; w++) { if (i.hay.indexOf(words[w]) === -1) { return false; } }
      return true;
    };

    var topic = st.topic ? model.topics.filter(function (t) { return t.id === st.topic; })[0] : null;
    if (!topic && sel && !q) { topic = sel.level === 'unit' ? sel : sel.parent; }

    var rows;
    if (topic) {
      rows = [topic].concat(topic.kids).filter(function (i) { return !words.length || match(i); });
    } else if (words.length) {
      rows = model.items.filter(function (i) { return inSubject(i) && match(i); });
      rows.sort(function (a, b) {
        var ra = (a.ok ? 0 : 2) + (a.level === 'unit' ? 0 : 1);
        var rb = (b.ok ? 0 : 2) + (b.level === 'unit' ? 0 : 1);
        if (ra !== rb) { return ra - rb; }
        var sa = a.hay.indexOf(words[0]) === 0 ? 0 : 1, sb = b.hay.indexOf(words[0]) === 0 ? 0 : 1;
        return sa - sb || a.idx - b.idx;
      });
    } else {
      // Nothing typed, nothing browsed: this child's own units. If their
      // plan holds none (it can be empty), their key stage's topics, greyed.
      rows = model.topics.filter(function (t) { return inSubject(t) && t.ok; });
      if (!rows.length) {
        rows = model.topics.filter(function (t) { return inSubject(t) && t.ks === model.childKs; });
      }
    }
    return { rows: rows.slice(0, MAX_ROWS), more: Math.max(0, rows.length - MAX_ROWS), topic: topic };
  }

  /* ── mount ─────────────────────────────────────────────────────────── */
  var uid = 0;
  function mount(host, opts) {
    opts = opts || {};
    var st = opts.state || {};
    if (st.q == null) { st.q = ''; }
    var child = opts.child || {};
    var model = build(opts.index, child, opts.units);
    var base = 'tp' + (++uid);
    var lessons = opts.allowLessons !== false;

    if (!lessons) {
      model.items.forEach(function (i) {
        if (i.level === 'lesson') { i.pick = i.parent; }
      });
    }

    var subjOpts = '<option value="">All subjects</option>' + SUBJECTS.map(function (s) {
      return '<option value="' + s + '"' + (st.subject === s ? ' selected' : '') + '>' + cap(s) + '</option>';
    }).join('');

    host.innerHTML =
      '<div class="tp">' +
        '<div class="tp-browse">' +
          '<label class="tp-lab">Subject<select class="tp-sel" id="' + base + '-subj">' + subjOpts + '</select></label>' +
          '<label class="tp-lab">Topic<select class="tp-sel" id="' + base + '-topic"></select></label>' +
        '</div>' +
        '<label class="tp-lab" for="' + base + '-q">Search</label>' +
        '<input class="tp-q" id="' + base + '-q" type="text" role="combobox" autocomplete="off" ' +
          'autocapitalize="none" spellcheck="false" aria-autocomplete="list" aria-expanded="true" ' +
          'aria-controls="' + base + '-list" placeholder="' + esc(opts.placeholder || 'e.g. food tests, bonding') + '"/>' +
        '<ul class="tp-list" id="' + base + '-list" role="listbox" aria-label="' +
          esc(opts.listLabel || 'Topics') + '"></ul>' +
        '<p class="tp-more" id="' + base + '-more" aria-live="polite"></p>' +
      '</div>';

    var subjEl = document.getElementById(base + '-subj');
    var topicEl = document.getElementById(base + '-topic');
    var qEl = document.getElementById(base + '-q');
    var listEl = document.getElementById(base + '-list');
    var moreEl = document.getElementById(base + '-more');
    var rows = [], active = -1;

    var sel0 = st.selected && model.items.filter(function (i) { return i.id === st.selected; })[0];
    qEl.value = st.q || (sel0 ? sel0.name : '');

    function fillTopics() {
      var groups = { ks3: [], ks4: [] };
      model.topics.forEach(function (t) {
        if (st.subject && t.subject !== st.subject) { return; }
        groups[t.ks].push('<option value="' + esc(t.id) + '"' + (st.topic === t.id ? ' selected' : '') + '>' +
          esc(t.name + (t.ok ? '' : ' (' + t.why + ')')) + '</option>');
      });
      var order = model.childKs === 'ks4' ? ['ks4', 'ks3'] : ['ks3', 'ks4'];
      topicEl.innerHTML = '<option value="">All topics</option>' + order.map(function (k) {
        if (!groups[k].length) { return ''; }
        return '<optgroup label="' + (k === 'ks3' ? 'Years 7 to 9' : 'GCSE') + '">' + groups[k].join('') + '</optgroup>';
      }).join('');
    }

    function draw() {
      var v = visible(model, st);
      rows = v.rows;
      if (active >= rows.length) { active = rows.length - 1; }
      listEl.innerHTML = rows.length ? rows.map(function (it, n) {
        var on = st.selected === it.id;
        var meta = it.level === 'lesson'
          ? ('Lesson in ' + it.unitName)
          : (it.ks === 'ks3' ? ('Unit ' + it.unitCode) : 'GCSE topic');
        return '<li role="option" id="' + base + '-o' + n + '" data-n="' + n + '" class="tp-opt' +
          (it.level === 'lesson' ? ' tp-lesson' : '') + (it.ok ? '' : ' tp-off') +
          (n === active ? ' tp-active' : '') + '" aria-selected="' + (on ? 'true' : 'false') + '"' +
          (it.ok ? '' : ' aria-disabled="true"') + '>' +
          '<span class="tp-name">' + esc(it.name) + '</span>' +
          '<span class="tp-meta">' + esc(cap(it.subject) + ' · ' + meta) +
          (it.ok ? '' : ' · <span class="tp-why">' + esc(it.why) + '</span>') + '</span>' +
          '</li>';
      }).join('') : '<li class="tp-empty" role="presentation">Nothing matches that.</li>';
      moreEl.textContent = v.more ? (v.more + ' more — keep typing to narrow it down.') : '';
      if (active >= 0) {
        qEl.setAttribute('aria-activedescendant', base + '-o' + active);
        var a = document.getElementById(base + '-o' + active);
        if (a && a.scrollIntoView) { a.scrollIntoView({ block: 'nearest' }); }
      } else {
        qEl.removeAttribute('aria-activedescendant');
      }
    }

    function choose(n) {
      var it = rows[n];
      if (!it || !it.ok) { return; }
      var target = it.pick || it;
      if (!target.ok) { return; }
      st.selected = target.id;
      st.q = '';
      qEl.value = target.name;
      active = -1;
      draw();
      if (typeof opts.onChange === 'function') { opts.onChange(selectionOf(target)); }
    }

    subjEl.addEventListener('change', function () {
      st.subject = subjEl.value;
      var t = st.topic && model.topics.filter(function (x) { return x.id === st.topic; })[0];
      if (t && st.subject && t.subject !== st.subject) { st.topic = ''; }
      active = -1;
      fillTopics(); draw();
    });
    topicEl.addEventListener('change', function () {
      st.topic = topicEl.value;
      var t = st.topic && model.topics.filter(function (x) { return x.id === st.topic; })[0];
      if (t && !st.subject) { st.subject = t.subject; subjEl.value = t.subject; fillTopics(); }
      st.q = ''; qEl.value = '';
      active = -1; draw();
    });
    qEl.addEventListener('input', function () {
      st.q = qEl.value;
      active = -1; draw();
    });
    qEl.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        if (!rows.length) { return; }
        active = e.key === 'ArrowDown' ? Math.min(rows.length - 1, active + 1) : Math.max(0, active - 1);
        draw();
      } else if (e.key === 'Enter') {
        if (active >= 0) { e.preventDefault(); choose(active); }
      } else if (e.key === 'Escape') {
        if (qEl.value) { e.preventDefault(); st.q = ''; qEl.value = ''; active = -1; draw(); }
      } else if (e.key === 'Home' && rows.length && active >= 0) {
        e.preventDefault(); active = 0; draw();
      } else if (e.key === 'End' && rows.length && active >= 0) {
        e.preventDefault(); active = rows.length - 1; draw();
      }
    });
    listEl.addEventListener('mousedown', function (e) { e.preventDefault(); });
    listEl.addEventListener('click', function (e) {
      var li = e.target.closest ? e.target.closest('li[data-n]') : null;
      if (!li) { return; }
      choose(Number(li.getAttribute('data-n')));
    });

    fillTopics();
    draw();

    return {
      selection: function () {
        var it = st.selected && model.items.filter(function (i) { return i.id === st.selected; })[0];
        return it ? selectionOf(it) : null;
      },
      focus: function () { qEl.focus(); }
    };
  }

  window.MrBadmusTopicPicker = { loadIndex: loadIndex, mount: mount, _build: build, _whyText: whyText };
})();
