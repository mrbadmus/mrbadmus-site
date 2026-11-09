/* ═══════════════════════════════════════════════════════════════════════
   ask-tutor.js — "Ask the tutor" beside a practice question (8 Nov 2026).

   Design's parent-side delivery draws it on the child's question page. That
   page is student/assignment.html, the GENERATED page every Rainford pupil
   uses, so nothing here is in its template: shared/student-live.js loads this
   file for a family/organisation CHILD session and for nobody else, and the
   button and sheet live on <body>, outside the mount host the compiled
   runtime empties on every setState (the reason set-work.js does the same).

   The engine is the lesson tutor's own: mrbadmus.v2.js is loaded the first
   time the sheet opens, for its system prompt and formatReply, so a reply here
   renders and a question is logged (child_tutor_questions, through the same
   POST /api/chat) exactly as on a lesson. `context.path` carries the
   assignment, which is how GET /api/consumer/child/tutor-talk brings the
   conversation back on another device.

   Reads the question off the page: [data-mrb-qw] attributes (student_rulings,
   C9). No attribute on screen means no question on screen, so no button.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var c = window.MrBadmusConfig;
  if (!c || !c.BACKEND_URL || !c.AUTH_STORAGE_KEY || typeof c.isChildSession !== 'function') { return; }
  var session = null;
  try { session = JSON.parse(window.localStorage.getItem(c.AUTH_STORAGE_KEY) || 'null'); } catch (e) { return; }
  if (!session || !session.access_token || !c.isChildSession(session)) { return; }

  var assignment = new URLSearchParams(window.location.search).get('assignment') || '';
  var PATH = '/student/assignment.html' + (assignment ? '?assignment=' + encodeURIComponent(assignment) : '');

  var root = null, btn = null, sheet = null, list = null, input = null, send = null, closeBtn = null;
  var talk = [];            // {role, content} sent to the model, oldest first
  var loaded = null;        // the engine, once
  var restored = null;      // the past talk, once
  var busy = false;

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (x) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[x];
    });
  }
  function txt(el) { return el ? String(el.textContent || '').replace(/\s+/g, ' ').trim() : ''; }
  function shown(el) { return !!(el && el.getClientRects && el.getClientRects().length); }
  function practice() { return window.__MRB_PRACTICE__ || {}; }

  function question() {
    var stem = document.querySelector('[data-mrb-qw="stem"]');
    if (!shown(stem)) { return null; }
    var opts = Array.prototype.map.call(document.querySelectorAll('[data-mrb-qw="opt"]'), function (o) {
      return { key: txt(o.querySelector('[data-mrb-qw="key"]')), text: txt(o.querySelector('[data-mrb-qw="text"]')) || txt(o) };
    });
    /* The mark (RIGHT, NOT THIS ONE, THE ANSWER), not the feedback note: a bank
       row with no `why` has no note, so a note says nothing about whether the
       question has been answered. */
    return { stem: txt(stem), options: opts, answered: shown(document.querySelector('[data-mrb-qw="status"]')) };
  }

  function assetUrl(src) {
    var map = window.__MRB_ASSET_V__, v = map && map[src.replace(/^\/shared\//, '')];
    return v ? src + '?v=' + v : src;
  }
  function engine() {
    if (loaded) { return loaded; }
    loaded = new Promise(function (resolve, reject) {
      if (window.MrBadmus) { resolve(window.MrBadmus); return; }
      var s = document.createElement('script');
      s.src = assetUrl('/shared/mrbadmus.v2.js');
      s.onload = function () { window.MrBadmus ? resolve(window.MrBadmus) : reject(new Error('no engine')); };
      s.onerror = function () { reject(new Error('no engine')); };
      document.head.appendChild(s);
    }).then(function (M) {
      var p = practice();
      return Promise.resolve(M.init({ subject: p.subject || 'physics', topic: p.title || '', keyStage: p.keyStage === 'KS3' ? 'ks3' : '' }))
        .then(function () { return M; });
    });
    return loaded;
  }

  function systemFor(M, q) {
    var base = M.systemPrompt();
    if (!q) { return base; }
    var said = 'The student has this practice question on screen.\nQuestion: ' + q.stem;
    if (q.options.length) {
      said += '\nOptions:\n' + q.options.map(function (o) { return (o.key ? o.key + '. ' : '') + o.text; }).join('\n');
    }
    said += q.answered
      ? '\nThey have answered it and can see the feedback, so explain it fully.'
      : '\nThey have not answered it yet. Help them work it out with hints and questions. Do not say which option is right, and do not rule options out until one is left.';
    return base + '\n\n' + said;
  }

  function token(M, fresh) {
    var auth = M.childAuth;
    return auth ? (fresh ? auth.refresh(c) : auth.token(c)) : Promise.resolve(session.access_token);
  }

  function drawEmpty() {
    if (list.children.length) { return; }
    var li = document.createElement('li');
    li.className = 'mrb-at-empty';
    li.textContent = 'Ask anything about this question. The tutor helps you work it out.';
    list.appendChild(li);
  }
  function bubble(who, html, mine) {
    var empty = list.querySelector('.mrb-at-empty');
    if (empty) { empty.remove(); }
    var li = document.createElement('li');
    li.className = 'mrb-at-msg' + (mine ? ' is-mine' : '');
    li.innerHTML = '<span class="mrb-at-who">' + esc(who) + '</span><div class="mrb-at-body">' + html + '</div>';
    list.appendChild(li);
    list.scrollTop = list.scrollHeight;
    return li;
  }

  function restore(M) {
    return token(M).then(function (tok) {
      return fetch(c.BACKEND_URL + '/api/consumer/child/tutor-talk?path=' + encodeURIComponent(PATH), {
        headers: { Authorization: 'Bearer ' + tok }
      });
    }).then(function (r) { return r.ok ? r.json() : null; }).then(function (b) {
      /* Above anything asked while this read was out, so the talk stays in order. */
      var first = list.querySelector('.mrb-at-msg'), past = [];
      var put = function (li) { if (first) { list.insertBefore(li, first); } };
      (b && b.tutor || []).forEach(function (r) {
        if (!r.answered || !r.reply) { return; }
        put(bubble('You', esc(r.question), true));
        put(bubble('Tutor', M.formatReply(r.reply), false));
        past.push({ role: 'user', content: r.question }, { role: 'assistant', content: r.reply });
      });
      talk = past.concat(talk);
      while (talk.length > 20) { talk.splice(0, 2); }
      list.scrollTop = list.scrollHeight;
    }).catch(function () { /* the sheet still works without the past */ });
  }

  function ask() {
    var q = input.value.trim();
    if (!q || busy) { return; }
    busy = true; send.disabled = true; input.value = '';
    bubble('You', esc(q), true);
    var wait = bubble('Tutor', '…', false);
    wait.setAttribute('aria-busy', 'true');
    talk.push({ role: 'user', content: q });
    var fail = function () {
      talk.pop();
      wait.querySelector('.mrb-at-body').textContent = "The tutor isn't available just now. Try again in a minute.";
      wait.removeAttribute('aria-busy');
    };
    (restored || Promise.resolve()).then(engine).then(function (M) {
      var p = practice(), onScreen = question();
      var body = JSON.stringify({
        system: systemFor(M, onScreen), messages: talk,
        context: { path: PATH, title: p.title || document.title || '' }
      });
      var once = function (tok) {
        return fetch(c.BACKEND_URL + '/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + tok },
          body: body
        });
      };
      return token(M).then(once).then(function (r) {
        return r.status === 401 ? token(M, true).then(once) : r;
      }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
        var reply = d && d.content ? d.content.map(function (x) { return x.text || ''; }).filter(Boolean).join('') : '';
        if (!reply) { fail(); return; }
        wait.querySelector('.mrb-at-body').innerHTML = M.formatReply(reply);
        wait.removeAttribute('aria-busy');
        list.scrollTop = list.scrollHeight;
        talk.push({ role: 'assistant', content: reply });
        while (talk.length > 20) { talk.splice(0, 2); }
      });
    }).catch(fail).then(function () {
      busy = false;
      send.disabled = !input.value.trim();
      input.focus();
    });
  }

  function open() {
    root.classList.add('is-open');
    sheet.removeAttribute('hidden');
    document.documentElement.style.overflow = 'hidden';
    list.scrollTop = list.scrollHeight;   // hiding the sheet forgets its scroll
    input.focus();
    if (!restored) {
      drawEmpty();
      restored = engine().then(restore).catch(function () {});
    }
  }
  function close() {
    root.classList.remove('is-open');
    sheet.setAttribute('hidden', '');
    document.documentElement.style.overflow = '';
    btn.focus();
  }

  /* Above the action bar, and only while a question is on screen. */
  function place() {
    var on = !!question();
    btn.hidden = !on;
    document.documentElement.classList.toggle('mrb-at-room', on);
    if (!on) { return; }
    var bar = document.querySelector('[data-mrb-qw="actionbar"]');
    var r = shown(bar) ? bar.getBoundingClientRect() : null;
    var over = r ? Math.max(0, window.innerHeight - r.top) : 0;
    btn.style.bottom = (over + 12) + 'px';
  }

  function mount() {
    root = document.createElement('div');
    root.className = 'rd mrb-at';
    root.setAttribute('data-mode', 'ks3');
    root.innerHTML =
      '<button type="button" class="mrb-at-open" hidden>Ask the tutor</button>' +
      '<div class="mrb-at-scrim" data-at-close></div>' +
      '<aside class="mrb-at-sheet" role="dialog" aria-modal="true" aria-labelledby="mrb-at-h" hidden>' +
        '<header class="mrb-at-head"><div><h2 id="mrb-at-h">Ask the tutor</h2>' +
          '<p>About this question · your parent or tutor can read this</p></div>' +
          '<button type="button" class="mrb-at-x" data-at-close aria-label="Close">' +
            '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"></path></svg>' +
          '</button></header>' +
        '<ol class="mrb-at-list" aria-live="polite"></ol>' +
        '<form class="mrb-at-form"><input type="text" placeholder="Type your question" aria-label="Question for the tutor" maxlength="1000">' +
          '<button type="submit" disabled>Send</button></form>' +
      '</aside>';
    document.body.appendChild(root);
    btn = root.querySelector('.mrb-at-open');
    sheet = root.querySelector('.mrb-at-sheet');
    list = root.querySelector('.mrb-at-list');
    input = root.querySelector('input');
    send = root.querySelector('.mrb-at-form button');
    closeBtn = root.querySelector('.mrb-at-x');
    btn.addEventListener('click', open);
    root.addEventListener('click', function (e) { if (e.target.closest('[data-at-close]')) { close(); } });
    input.addEventListener('input', function () { send.disabled = busy || !input.value.trim(); });
    root.querySelector('form').addEventListener('submit', function (e) { e.preventDefault(); ask(); });
    document.addEventListener('keydown', function (e) {
      if (!root.classList.contains('is-open')) { return; }
      if (e.key === 'Escape') { e.preventDefault(); close(); return; }
      if (e.key === 'Tab') {
        var first = closeBtn, last = send.disabled ? input : send;
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
      /* No stopPropagation: this page has no key that picks an option, and its
         clock listens for keydown on window, so swallowing keys here paused the
         clock after 60 seconds of typing. */
    }, true);
    var queued = false;
    var soon = function () {
      if (queued) { return; }
      queued = true;
      window.requestAnimationFrame(function () { queued = false; place(); });
    };
    new MutationObserver(soon).observe(document.body, { childList: true, subtree: true });
    window.addEventListener('resize', soon, { passive: true });
    place();
  }

  var link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = assetUrl('/shared/ask-tutor.css');
  document.head.appendChild(link);
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', mount); } else { mount(); }
})();
