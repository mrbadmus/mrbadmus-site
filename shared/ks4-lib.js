/* KS4 lesson helpers — business logic only, no styling.
   Reads the frozen source in ks4-source.js (window.KS4SRC) and hands lessons
   verbatim quiz items, tips, key notes and FIFA steps. Nothing here rewrites a
   frozen string: options are only re-ordered (deterministically), because in the
   source the correct option is always first and almost always the longest. */
window.KS4 = (function () {
  var RK = { 'Combined Foundation': 'CF', 'Combined Higher': 'CH', 'Triple Foundation': 'TF', 'Triple Higher': 'TH' };
  /* Equation sheets: one entry per exam year. Each summer add the new year's two AQA PDFs and move EQ_YEAR. */
  var EQ_BY_YEAR = {
    2026: { combined: 'https://www.aqa.org.uk/files/resources.science.AQA-8464-8465-FS-INS-2025_PDF/c4fac749855e8fefcd6ff58bd7b9cb701309df9b.pdf',
            triple: 'https://www.aqa.org.uk/files/resources.physics.AQA-8463-FS-INS-2025_PDF/6b5358e1159b1b6cc2d622fc5eb894320d6fb763.pdf' }
  };
  var EQ_YEAR = 2026;
  var EQ = EQ_BY_YEAR[EQ_YEAR];
  /* Lesson videos: slug -> { src, poster, captions (.vtt), title, duration, transcript: [paragraphs] }. Empty = no slot shown. */
  var VIDEOS = {};
  function video(slug) { var v = VIDEOS[slug]; return v && v.src ? v : null; }
  var ROUTES = ['Combined Foundation', 'Combined Higher', 'Triple Foundation', 'Triple Higher'];
  function src(slug) { return (window.KS4SRC || {})[slug] || {}; }
  function routeKey(r) { return RK[r] || 'TH'; }
  function flags(r) {
    var k = routeKey(r);
    return { key: k, higher: k === 'CH' || k === 'TH', triple: k === 'TF' || k === 'TH', label: r || 'Triple Higher' };
  }
  function hash(str) {
    var h = 2166136261;
    for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }
  var RIGHT = 'This is the answer the mark scheme credits.';
  function item(q) {
    if (!q) return null;
    var we = q.wrong_explanations || {};
    var opts = q.opts.map(function (o, i) {
      return { text: o[0], correct: !!o[1], reply: o[1] ? RIGHT : (we[String(i)] || ''), k: hash(q.q + '|' + o[0]) };
    });
    opts.sort(function (a, b) { return a.k - b.k; });
    return { prompt: q.q, options: opts.map(function (o) { return { text: o.text, correct: o.correct, reply: o.reply }; }) };
  }
  function quiz(slug, r) {
    var s = src(slug).quiz || {};
    return s[routeKey(r)] || s.TH || [];
  }
  function find(slug, r, needle) {
    var list = quiz(slug, r);
    var q = list.filter(function (x) { return x.q.indexOf(needle) >= 0; })[0];
    if (!q) q = (src(slug).quiz && src(slug).quiz.TH || []).filter(function (x) { return x.q.indexOf(needle) >= 0; })[0];
    return item(q);
  }
  function bank(slug, r) { return quiz(slug, r).map(item); }
  function tip(slug) { return src(slug).examiner_tip || ''; }
  function keyLines(slug) {
    var t = src(slug).key_note || '';
    return t.split(/(?<=\.)\s+/).map(function (s) { return s.trim(); }).filter(Boolean);
  }
  function commonMistake(slug) { return src(slug).common_mistake || ''; }
  var LABELS = ['Formula', 'Insert', 'Fine-tune', 'Answer'];
  /* The four FIFA steps stay word for word; CFIFA puts a Convert step in front. */
  function cfifa(fifa, convertLine, convertNote) {
    var steps = [{ letter: 'C', label: 'Convert', line: convertLine, note: convertNote || '' }];
    (fifa.steps || []).forEach(function (s, i) { steps.push({ letter: s[0], label: LABELS[i] || '', line: s[1], note: '' }); });
    return steps;
  }
  function fifas(slug) { return src(slug).fifas || []; }
  function load(key, fallback) { try { var v = localStorage.getItem(key); return v === null ? fallback : JSON.parse(v); } catch (e) { return fallback; } }
  function save(key, v) { try { localStorage.setItem(key, JSON.stringify(v)); } catch (e) {} }
  /* Progress rail. A node ticks only when its activity is complete (KS3 convention). */
  function rail(list, done, active) {
    var a = Math.max(0, Math.min(list.length - 1, active || 0));
    var nDone = done.filter(Boolean).length;
    return {
      rail: list.map(function (r, i) {
        var d = !!done[i], cur = i === a;
        return { href: '#' + r.id, label: r.short, num: String(i + 1), done: d, showNum: !d, hasLine: i < list.length - 1,
          linkStyle: 'display:flex;flex-direction:column;align-items:center;gap:7px;text-decoration:none;color:inherit;padding:2px 0;',
          chipStyle: 'display:grid;place-items:center;width:32px;height:32px;border-radius:10px;font-family:var(--ks3-font-display);font-weight:800;font-size:16px;background:' +
            (d ? 'var(--ks3-accent-text)' : 'var(--ks3-card)') + ';border:2px solid ' + (d || cur ? 'var(--ks3-ink)' : 'var(--ks3-rule-strong)') + ';color:' +
            (d ? 'var(--ks3-ground)' : cur ? 'var(--ks3-ink)' : 'var(--ks3-ink-muted)') + ';box-shadow:' + (cur ? '0 0 0 4px var(--ks3-accent-tint)' : 'none') + ';',
          textStyle: 'font-family:var(--ks3-font-mono);font-size:11px;font-weight:500;letter-spacing:.09em;text-transform:uppercase;text-align:center;line-height:1.2;color:' +
            (cur ? 'var(--ks3-ink)' : 'var(--ks3-ink-muted)') + ';',
          lineStyle: 'display:block;width:2px;height:18px;margin:6px 0;background:' + (d ? 'var(--ks3-accent-text)' : 'var(--ks3-rule)') + ';' };
      }),
      railCountLabel: nDone + ' of ' + list.length + ' done',
      railCurrentLabel: list[a] ? list[a].label : '', railCurrentHref: list[a] ? '#' + list[a].id : '#',
      railBarStyle: 'display:block;height:100%;width:' + Math.round(nDone / list.length * 100) + '%;background:var(--ks3-accent-text);'
    };
  }
  function observe(cmp, list) {
    if (!('IntersectionObserver' in window)) return null;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var i = list.findIndex(function (r) { return r.id === e.target.id; });
        if (i >= 0) cmp.setState({ active: i });
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    var tries = 0;
    (function hook() {
      var found = 0;
      list.forEach(function (r) { var el = document.getElementById(r.id); if (el) { io.observe(el); found++; } });
      if (found < list.length && tries++ < 40) setTimeout(hook, 150);
    })();
    return io;
  }
  /* Route plumbing: the page reads one record and renders one route. */
  function route(cmp) {
    var r = (cmp.state && cmp.state.route) || cmp.props.route || 'Triple Higher';
    var f = flags(r);
    return { route: r, isHigher: f.higher, isTriple: f.triple, isTH: f.higher && f.triple, notHigher: !f.higher, notTriple: !f.triple,
      routeOptions: ROUTES.map(function (x) { return { value: x, label: x }; }),
      eqSheetHref: f.triple ? EQ.triple : EQ.combined, eqSheetLabel: (f.triple ? 'GCSE Physics (8463)' : 'Combined Science: Trilogy and Synergy (8464/8465)') + ' · June ' + EQ_YEAR,
      onRoute: function (e) { cmp.setState({ route: e.target.value }); } };
  }
  function ready(cmp) {
    var t = setInterval(function () { if (window.KS4SRC && window.KS4D) { clearInterval(t); cmp.setState({ libReady: true }); } }, 40);
  }
  function fig(svgStr, alt, max) {
    if (!svgStr) return null;
    // ⊕ R2 (ks4_rulings.py): React.createElement(...) -> the runtime's figure marker.
    return { __mrbFig: true, __html: svgStr, alt: alt || '', max: max || '100%' };
  }

  /* ⊕ ENGINE ADDITION — not in Design's delivery. Her page never needed a
     real href (Route was a review selector, and her prev/next/connects
     hrefs were sibling .dc.html filenames for local review). NAV is
     generated from ks4_lessons.LESSONS by build_ks4.py.
     ⊕ D2 fix (26 Sep 2026, docs/ks4/pilot-live-audit.md): this used to
     fall back to the Triple pathway at the same tier when the target did
     not ship on the current pathway (nanoparticles is Triple-only), which
     sent a Combined pupil into chemistry-only content. It now returns
     null instead — ks4_rulings.py's R-CONNECTS wraps every endConnects
     array with a .filter() that drops a null-href entry, so the link is
     simply absent on a route where the target has no page. */
  var NAV = {"chemical-bonds": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "covalent-bonding": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "giant-covalent-structures": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "ionic-bonding": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "ionic-compounds": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "metallic-bonding": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "metals-alloys": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "nanoparticles": {"routes": ["TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "polymers": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "properties-ionic-compounds": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "properties-small-molecules": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}, "resistors": {"routes": ["CF", "CH", "TF", "TH"], "subject": "physics", "topic": "electricity"}, "series-parallel-circuits": {"routes": ["CF", "CH", "TF", "TH"], "subject": "physics", "topic": "electricity"}, "states-of-matter": {"routes": ["CF", "CH", "TF", "TH"], "subject": "chemistry", "topic": "bonding"}};
  function hrefFor(slug, R) {
    var n = NAV[slug];
    if (!n) { return null; }
    var pathway = (R && R.isTriple) ? 'triple' : 'combined';
    var tier = (R && R.isHigher) ? 'higher' : 'foundation';
    var code = (pathway === 'triple' ? 'T' : 'C') + (tier === 'higher' ? 'H' : 'F');
    if (n.routes.indexOf(code) === -1) { return null; }
    return '/' + pathway + '/' + tier + '/' + n.subject + '/' + n.topic + '/' + slug + '.html';
  }
  return { rail: rail, observe: observe, route: route, ready: ready, fig: fig, ROUTES: ROUTES, EQ: EQ, EQ_BY_YEAR: EQ_BY_YEAR, EQ_YEAR: EQ_YEAR, video: video, VIDEOS: VIDEOS, src: src, routeKey: routeKey, flags: flags, item: item, quiz: quiz, find: find, bank: bank,
    tip: tip, keyLines: keyLines, commonMistake: commonMistake, cfifa: cfifa, fifas: fifas, load: load, save: save, hash: hash, hrefFor: hrefFor };
})();
