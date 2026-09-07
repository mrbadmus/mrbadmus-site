/* ═══════════════════════════════════════════════════════════════════════
   set-work.js — the Set work sheet (MRB-335). Self-contained, patched in
   place, mounted on <body> where the compiled runtime cannot reach it.

   Surface:  window.MRBSetWork.open({classId})   .close()

   ── WHY IT IS NOT A COMPILED COMPONENT ────────────────────────────────

   THE SCROLL-JUMP ROOT CAUSE, named. v1's sheet was Design's compiled node
   581, rendered by `shared/student-runtime.js` inside the `#mrb-teacher`
   mount host. Every selection in the sheet called `this.setState(...)`, and:

     shared/student-runtime.js:62   setState -> this.__host.schedule(cb)
     shared/student-runtime.js:466  schedule -> api.draw()
     shared/student-runtime.js:496  var keepScroll = window.scrollY;
     shared/student-runtime.js:497  host.textContent = "";
     shared/student-runtime.js:498  host.appendChild(frag);
     shared/student-runtime.js:501  if (window.scrollY !== keepScroll) {
                                      window.scrollTo(0, keepScroll); }

   `draw()` empties the ENTIRE mount host and rebuilds the whole template
   from scratch — the runtime says so in its own header comment ("The
   re-render is a full rebuild, deliberately"). It restores focus
   (`refocus`, :381), form field values (`restoreFields`, :419) and the
   DOCUMENT's scroll (:496, :501). It restores no element's `scrollTop`,
   because it holds no record of one.

   Design's sheet is `width:720px; max-height:86vh; overflow:auto` — its own
   INNER scroll container. So on every tap of a topic, a count chip or a
   class, the DOM node holding the teacher's scroll position was destroyed at
   :497 and replaced at :498 by a brand-new node whose `scrollTop` is 0. The
   teacher was thrown back to the top of a fifty-row list, every time.

   Nothing about that is fixable inside the sheet: it is a property of the
   renderer the sheet was drawn by. Two ways out — teach the runtime to save
   and restore every descendant scroller, or take the sheet out of the
   runtime. The first changes the render path of every teacher AND student
   page in the estate to fix one overlay. This is the second.

   So: this module owns ONE overlay, appended to `document.body`, a SIBLING
   of the mount host. `draw()` cannot see it, and a page-level `setState`
   cannot disturb it.

   ── THE PATCHING RULE, which is the other half ────────────────────────

   Being outside the runtime is necessary and not sufficient — a module that
   rebuilt its own list on every tap would jump exactly as far. So:

     · the tree DOM and the question DOM are built ONCE PER DATA LOAD
       (`buildTree` after /scope, `buildQuestions` after /preview);
     · a SELECTION never builds anything. It toggles `classList`, an
       attribute, `hidden`, or `textContent` on nodes that already exist;
     · changing tier RE-COUNTS IN PLACE from the counts already in /scope —
       no request, no rebuild (RISKS C12);
     · filtering by subject or paper toggles `hidden` on existing rows;
     · Swap replaces one row's TEXT, never the row;
     · no `href="#"` anywhere — every control is a <button type="button">;
     · nothing calls `focus()` after a state change.

   RISKS A1. The drive check is `scroll_unchanged_on_select`.

   ── STRINGS ───────────────────────────────────────────────────────────

   RISKS A9. Every string in this file is a noun, a label, a number, a date
   or a button verb. There are no sentences. Validation is a disabled primary
   plus an outlined field, never a paragraph. The one factual line is the
   school's hold date, and it is a date.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  /* ═════════════════════════════════════════════════════════════════════
     1. FORMULAE — a faithful port of `formulae()` in ks3_art/kit.py.

     ⚠️ DISPLAY TIME ONLY. Nothing converted is ever stored, sent or
     compared. MRB-302's ruling is STORE FLAT, RENDER SUBSCRIPT, and every
     answer comparison in the estate runs on option indices, so this pass
     cannot reach marking. What goes to `/api/teacher/set-work` is the
     question ID; the stem is never round-tripped at all.

     ⚠️ NOT A LETTER-THEN-DIGIT REGEX. `C1`, `C6`, `P11`, `B2` are all a real
     element symbol followed by a number and are the unit codes this course
     is built on. A token converts only when every symbol is a real element,
     it carries a digit, and EITHER it has two or more element groups OR the
     whole token is one of the single-element species that genuinely take a
     subscript. `KS3`/`KS4` parse as formulae and are denied by name.

     The Python uses a lookbehind; this uses a captured prefix group instead,
     which is exactly equivalent and works on Safari below 16.4.
     ═════════════════════════════════════════════════════════════════════ */

  var ELEMENTS = {};
  ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co " +
   "Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb " +
   "Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re " +
   "Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm"
  ).split(" ").forEach(function (s) { ELEMENTS[s] = true; });

  /* `X` is Mendeleev's placeholder for an undiscovered element, not an
     element. It fills an element's slot typographically, so it subscripts
     like one — and it is kept out of ELEMENTS for the reason kit.py keeps it
     out: other code may reasonably assume ELEMENTS names real chemistry. */
  var PLACEHOLDERS = { X: true };

  var SINGLE_WITH_SUB = {
    H2: true, O2: true, N2: true, F2: true, Cl2: true,
    Br2: true, I2: true, O3: true, S8: true, P4: true
  };

  /* Tokens that parse as a formula and are not one. K + S + 3. Deliberately
     tiny and explicit: an entry here is something a human has SEEN
     mis-rendered, never something imagined. */
  var NOT_FORMULAE = { KS3: true, KS4: true };

  var FORMULA_RE = /(^|[^0-9A-Za-z<&/])(\d*)((?:[A-Z][a-z]?\d*)+)(?![0-9A-Za-z;])/g;
  var GROUP_RE = /([A-Z][a-z]?)(\d*)/g;
  var TAG_RE = /<[^>]*>/g;

  /* The parsed groups of a token, or null when it must be left alone.
     Mirrors `_formula_sub`'s five refusals in the same order. */
  function formulaGroups(body) {
    if (NOT_FORMULAE[body]) { return null; }
    var groups = [], m, seen = 0;
    GROUP_RE.lastIndex = 0;
    while ((m = GROUP_RE.exec(body)) !== null) {
      if (m[0] === "") { GROUP_RE.lastIndex += 1; continue; }
      groups.push([m[1], m[2]]);
      seen += m[0].length;
    }
    if (!groups.length || seen !== body.length) { return null; }
    for (var i = 0; i < groups.length; i++) {
      var sym = groups[i][0];
      if (!ELEMENTS[sym] && !PLACEHOLDERS[sym]) { return null; }
    }
    var anyDigit = false;
    for (var j = 0; j < groups.length; j++) {
      if (groups[j][1]) { anyDigit = true; }
    }
    if (!anyDigit) { return null; }              // no subscript to draw
    if (groups.length < 2 && !SINGLE_WITH_SUB[body]) {
      return null;                               // C1, P11, B2 — a code
    }
    return groups;
  }

  /* One run of plain text -> nodes. A leading coefficient is NOT a subscript:
     in `2CO2` the first 2 counts molecules and stays full size. That
     distinction is the entire point of the lesson this exists to serve. */
  function formulaRun(text, frag) {
    var last = 0, m;
    FORMULA_RE.lastIndex = 0;
    while ((m = FORMULA_RE.exec(text)) !== null) {
      var groups = formulaGroups(m[3]);
      if (!groups) { continue; }
      var start = m.index + m[1].length;
      if (start > last) {
        frag.appendChild(document.createTextNode(text.slice(last, start)));
      }
      if (m[2]) { frag.appendChild(document.createTextNode(m[2])); }
      for (var i = 0; i < groups.length; i++) {
        frag.appendChild(document.createTextNode(groups[i][0]));
        if (groups[i][1]) {
          var sub = document.createElement("sub");
          sub.textContent = groups[i][1];
          frag.appendChild(sub);
        }
      }
      last = m.index + m[0].length;
    }
    if (last < text.length) {
      frag.appendChild(document.createTextNode(text.slice(last)));
    }
  }

  /* Text already inside a tag is never touched — kit.py's rule. The pools are
     FLAT under MRB-302 so a stem should carry no markup at all; if one does,
     the tag run is emitted as literal TEXT (never as markup: this file has no
     `innerHTML` and a question stem is data). */
  function formulaFrag(text) {
    var s = String(text == null ? "" : text);
    var frag = document.createDocumentFragment();
    if (s.indexOf("<") < 0) { formulaRun(s, frag); return frag; }
    var last = 0, m;
    TAG_RE.lastIndex = 0;
    while ((m = TAG_RE.exec(s)) !== null) {
      formulaRun(s.slice(last, m.index), frag);
      frag.appendChild(document.createTextNode(m[0]));
      last = m.index + m[0].length;
    }
    formulaRun(s.slice(last), frag);
    return frag;
  }

  function setFormula(el, text) {
    el.textContent = "";
    el.appendChild(formulaFrag(text));
  }

  /* ═════════════════════════════════════════════════════════════════════
     2. LONDON ↔ UTC, by offset probing. No libraries.

     RISKS B1. The teacher types a WALL CLOCK — "Wednesday the 25th at 18:00"
     — and the server stores an instant. Between those two is the one hour
     that happens twice on 25 Oct 2026 and the one that never happens on
     28 Mar 2027, and a naive `new Date(dateStr + 'T' + timeStr)` reads the
     browser's own zone, which is the teacher's laptop's guess and not
     London.

     `Intl.DateTimeFormat` with `timeZone:'Europe/London'` is the only
     authority available on a page with no build step. It formats an INSTANT
     into London parts; running it on a candidate instant and comparing gives
     the offset, and two candidates one day either side of the wall clock
     cover both offsets around any transition.

     ⚠️ THE BACKEND MUST NOT DO THIS. Render runs a small-ICU Node where
     `toLocaleString` with a `timeZone` silently ignores it (RISKS B2). The
     server has `ukOffsetMsAt()` for the same job; this is the client's half.
     ═════════════════════════════════════════════════════════════════════ */

  var LDN = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Europe/London",
    year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit",
    hour12: false
  });

  function londonPartsAt(ms) {
    var parts = LDN.formatToParts(new Date(ms)), out = {}, i;
    for (i = 0; i < parts.length; i++) {
      if (parts[i].type !== "literal") { out[parts[i].type] = parts[i].value; }
    }
    /* `hour12:false` yields "24" for midnight on some ICU builds. */
    var h = Number(out.hour);
    if (h === 24) { h = 0; }
    return {
      y: Number(out.year), m: Number(out.month), d: Number(out.day),
      H: h, M: Number(out.minute), S: Number(out.second)
    };
  }

  /* Minutes EAST of UTC: 0 in GMT, 60 in BST. */
  function londonOffsetMinutesAt(ms) {
    var p = londonPartsAt(ms);
    return Math.round((Date.UTC(p.y, p.m - 1, p.d, p.H, p.M, p.S) - ms) / 60000);
  }

  function naiveUtcMs(dateStr, timeStr) {
    var d = String(dateStr || "").split("-");
    var t = String(timeStr || "").split(":");
    return Date.UTC(Number(d[0]), Number(d[1]) - 1, Number(d[2]),
                    Number(t[0]) || 0, Number(t[1]) || 0, 0, 0);
  }

  var DAY_MS = 86400000;

  /* A London wall clock -> the UTC instant, as an ISO string.

     AMBIGUOUS (25 Oct 2026 01:30 happens twice): the EARLIER instant wins —
     01:30 BST, 00:30 UTC. That is the "compatible" disambiguation every
     mainstream library defaults to, and it is the kinder one for a release
     time: work opens at the first moment the clock reads what was typed.

     NONEXISTENT (28 Mar 2027 01:30 never happens): shifted FORWARD by the
     gap, so it lands on 02:30 BST. Also the compatible rule. A due time
     inside the lost hour is a due time an hour later, never a silent
     failure. */
  function londonToUtcIso(dateStr, timeStr) {
    if (!dateStr || !timeStr) { return null; }
    var t0 = naiveUtcMs(dateStr, timeStr);
    if (isNaN(t0)) { return null; }
    var before = londonOffsetMinutesAt(t0 - DAY_MS);
    var after = londonOffsetMinutesAt(t0 + DAY_MS);
    var tried = (before === after) ? [before] : [before, after];
    var valid = [];
    for (var i = 0; i < tried.length; i++) {
      var cand = t0 - tried[i] * 60000;
      if (londonOffsetMinutesAt(cand) === tried[i]) { valid.push(cand); }
    }
    if (valid.length) {
      return new Date(Math.min.apply(null, valid)).toISOString();
    }
    /* The gap. Applying the offset in force BEFORE the transition moves the
       wall clock forward across it, which is the shift we want. */
    return new Date(t0 - before * 60000).toISOString();
  }

  /* The UTC instant -> the London wall clock the teacher would read. */
  function utcToLondonParts(iso) {
    var ms = (iso instanceof Date) ? iso.getTime() : Date.parse(iso);
    if (isNaN(ms)) { return null; }
    var p = londonPartsAt(ms);
    return {
      date: pad4(p.y) + "-" + pad2(p.m) + "-" + pad2(p.d),
      time: pad2(p.H) + ":" + pad2(p.M)
    };
  }

  function pad2(n) { return (n < 10 ? "0" : "") + n; }
  function pad4(n) { return ("000" + n).slice(-4); }

  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  /* "14 Sep 2026". The hold line's whole vocabulary. */
  function londonDateLabel(iso) {
    var ms = (iso instanceof Date) ? iso.getTime() : Date.parse(iso);
    if (isNaN(ms)) { return ""; }
    var p = londonPartsAt(ms);
    return p.d + " " + MONTHS[p.m - 1] + " " + p.y;
  }

  /* A London calendar date, n days from now, as YYYY-MM-DD.

     ⚠️ ADDED IN CALENDAR DAYS, NOT IN MILLISECONDS. `now + 7*864e5` crosses
     a DST boundary an hour out and lands on the 6th or the 8th day at the
     edges of the range. `Date.UTC` on the London PARTS increments the date
     itself, so "+7 days" is always the same weekday. */
  function londonDatePlus(days) {
    var p = londonPartsAt(Date.now());
    var d = new Date(Date.UTC(p.y, p.m - 1, p.d) + days * DAY_MS);
    return pad4(d.getUTCFullYear()) + "-" + pad2(d.getUTCMonth() + 1) +
           "-" + pad2(d.getUTCDate());
  }

  /* ═════════════════════════════════════════════════════════════════════
     3. THE BACKEND SEAM

     `window.MrBadmusConfig.BACKEND_URL` is the estate's one backend helper,
     and it IS the local override a drive needs: `shared/config.js` switches
     the whole config to the TEST project plus `http://localhost:3000` on
     `?env=test` or on localhost. Keeping it means a drive that already runs
     against a local backend keeps running against one, and production stays
     `https://mrbadmus-backend.onrender.com` with no branch here.
     ═════════════════════════════════════════════════════════════════════ */

  function apiBase() {
    var c = window.MrBadmusConfig || {};
    return c.BACKEND_URL || "https://mrbadmus-backend.onrender.com";
  }

  function token() {
    var g = window.MrBadmusTeacherGuard;
    var sb = (g && g.getClient) ? g.getClient() : null;
    if (!sb) { return Promise.reject(new Error("set-work: no data layer")); }
    return sb.auth.getSession().then(function (r) {
      var t = r && r.data && r.data.session && r.data.session.access_token;
      if (!t) { throw new Error("set-work: not signed in"); }
      return t;
    });
  }

  function apiGet(path) {
    return token().then(function (t) {
      return fetch(apiBase() + path, { headers: { Authorization: "Bearer " + t } });
    }).then(function (res) {
      if (res.status === 204) { return { status: 204, body: null }; }
      return res.json().then(
        function (d) { return { status: res.status, body: d, ok: res.ok }; },
        function () { return { status: res.status, body: null, ok: res.ok }; }
      );
    }).then(function (r) {
      if (r.status !== 204 && !r.ok) { throw new Error("set-work: " + r.status); }
      return r;
    });
  }

  function apiPost(path, payload) {
    return token().then(function (t) {
      return fetch(apiBase() + path, {
        method: "POST",
        headers: { Authorization: "Bearer " + t, "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
    }).then(function (res) {
      return res.json().then(
        function (d) { return { status: res.status, body: d, ok: res.ok }; },
        function () { return { status: res.status, body: null, ok: res.ok }; }
      );
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     4. STRINGS — the complete set. RISKS A9's list.
     Nouns, labels, numbers, dates and button verbs. No sentences.
     ═════════════════════════════════════════════════════════════════════ */

  var SAY = {
    steps: ["Classes", "Topic", "Detail"],
    next: "Next",
    set: "Set work",
    back: "Back",
    cancel: "Cancel",
    close: "Close",
    labelClasses: "Classes",
    labelTier: "Tier",
    labelSubject: "Subject",
    labelPaper: "Paper",
    labelTopics: "Topics",
    labelQuestions: "Questions",
    labelTitle: "Title",
    labelRelease: "Release",
    labelDue: "Due",
    tier: {
      foundation: "Foundation", higher: "Higher",
      easy: "Easy", medium: "Medium", hard: "Hard"
    },
    subject: { biology: "Biology", chemistry: "Chemistry", physics: "Physics" },
    subjectAll: "All",
    paper: ["Paper 1", "Paper 2"],
    paperBoth: "Both",
    notSet: "Not set yet",
    setThisWeek: "Set this week",
    swap: "Swap",
    now: "Now",
    later: "Later",
    releaseDate: "Release date",
    releaseTime: "Release time",
    dueDate: "Due date",
    dueTime: "Due time",
    student: "student",
    students: "students",
    /* The only composed strings. Each is a label plus a number or a date. */
    weeksAgo: function (n) { return "Set " + n + (n === 1 ? " week ago" : " weeks ago"); },
    pupils: function (n) { return n + " " + (n === 1 ? "student" : "students"); },
    hold: function (dateLabel) { return "Assignments open " + dateLabel; },
    setForClasses: function (title, n) { return title + " · Set for " + n + " classes"; },
    setForClass: function (title, name) { return title + " · " + name; },
    /* ⚠️ THE TWO REFUSAL LABELS, and they are the judgement call in this
       list. A9 bans sentences, not honesty: a sheet whose topic list failed
       to load and says NOTHING is a blank panel a teacher reads as "this
       class has no topics", which is a lie told by omission. These are noun
       phrases in the tag slot — the same two words a status chip carries —
       and there is no third. */
    unavailable: "Unavailable",
    notSetToast: "Not set"
  };

  /* ═════════════════════════════════════════════════════════════════════
     5. STATE
     ═════════════════════════════════════════════════════════════════════ */

  var S = null;          // the open sheet's state, or null
  var els = null;        // built DOM, kept between renders
  var toastTimer = null;

  function freshState(classId) {
    return {
      classId: classId,
      step: 0,                 // 0 Classes, 1 Topic, 2 Detail
      scope: null,             // the /scope answer
      scopeErr: false,
      classes: [classId],      // the opening class, preselected
      tier: "",
      subject: "all",
      paper: "both",
      scopeKind: "",           // 'topic' | 'subtopic'
      scopeRef: "",
      count: 10,
      available: 0,
      picked: [],
      shown: {},               // every question id shown this sheet SESSION
      expanded: {},
      swapDead: {},
      previewErr: false,
      busy: false,
      title: "",
      titleEdited: false,
      release: "now",          // 'now' | 'later'
      releaseDate: "",
      releaseTime: "07:00",
      dueDate: "",
      dueTime: "18:00",
      holdIso: "",
      showHold: false,
      badTitle: false,
      badDue: false,
      badRelease: false
    };
  }

  /* ═════════════════════════════════════════════════════════════════════
     6. DOM HELPERS — no innerHTML anywhere in this file.
     ═════════════════════════════════════════════════════════════════════ */

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) { n.className = cls; }
    if (text !== undefined && text !== null) { n.textContent = text; }
    return n;
  }

  function btn(cls, text) {
    var b = el("button", cls, text);
    b.type = "button";
    return b;
  }

  function svgChevron() {
    var ns = "http://www.w3.org/2000/svg";
    var s = document.createElementNS(ns, "svg");
    s.setAttribute("width", "10"); s.setAttribute("height", "10");
    s.setAttribute("viewBox", "0 0 10 10"); s.setAttribute("fill", "none");
    s.setAttribute("aria-hidden", "true");
    var p = document.createElementNS(ns, "path");
    p.setAttribute("d", "M3.5 1.5L7 5l-3.5 3.5");
    p.setAttribute("stroke", "currentColor");
    p.setAttribute("stroke-width", "1.6");
    p.setAttribute("stroke-linecap", "round");
    p.setAttribute("stroke-linejoin", "round");
    s.appendChild(p);
    return s;
  }

  function svgTick() {
    var ns = "http://www.w3.org/2000/svg";
    var s = document.createElementNS(ns, "svg");
    s.setAttribute("class", "sw-tick");
    s.setAttribute("width", "12"); s.setAttribute("height", "12");
    s.setAttribute("viewBox", "0 0 12 12"); s.setAttribute("fill", "none");
    s.setAttribute("aria-hidden", "true");
    var p = document.createElementNS(ns, "path");
    p.setAttribute("d", "M2 6.4L4.6 9 10 3.2");
    p.setAttribute("stroke", "currentColor");
    p.setAttribute("stroke-width", "1.8");
    p.setAttribute("stroke-linecap", "round");
    p.setAttribute("stroke-linejoin", "round");
    s.appendChild(p);
    return s;
  }

  /* ═════════════════════════════════════════════════════════════════════
     7. THE SHELL — built once for the life of the page, then reused.
     ═════════════════════════════════════════════════════════════════════ */

  function buildShell() {
    if (els) { return; }
    els = {};

    var overlay = el("div", "sw-overlay");
    overlay.hidden = true;
    overlay.setAttribute("data-sw", "overlay");

    var sheet = el("div", "sw-sheet");
    sheet.setAttribute("role", "dialog");
    sheet.setAttribute("aria-modal", "true");
    sheet.setAttribute("aria-label", SAY.set);
    sheet.tabIndex = -1;
    sheet.setAttribute("data-sw", "sheet");

    /* ── header: Back · step · primary ── */
    var head = el("div", "sw-head");
    var back = btn("sw-btn", SAY.cancel);
    back.setAttribute("data-sw", "back");
    var step = el("div", "sw-step", SAY.steps[0]);
    step.setAttribute("data-sw", "step");
    var primary = btn("sw-btn sw-btn-primary", SAY.next);
    primary.setAttribute("data-sw", "primary");
    head.appendChild(back); head.appendChild(step); head.appendChild(primary);

    var body = el("div", "sw-body");
    body.setAttribute("data-sw", "body");

    /* ── panel 0: Classes ── */
    var pClasses = el("div", "sw-panel");
    pClasses.setAttribute("data-sw", "panel-classes");
    pClasses.appendChild(el("div", "sw-label", SAY.labelClasses));
    var classList = el("div", "sw-tree");
    classList.setAttribute("data-sw", "class-list");
    pClasses.appendChild(classList);

    /* ── panel 1: Topic ── */
    var pTopic = el("div", "sw-panel");
    pTopic.setAttribute("data-sw", "panel-topic");
    pTopic.appendChild(el("div", "sw-label", SAY.labelTier));
    var tierChips = el("div", "sw-chips");
    tierChips.setAttribute("data-sw", "tier-chips");
    pTopic.appendChild(tierChips);

    var subjLabel = el("div", "sw-label", SAY.labelSubject);
    var subjChips = el("div", "sw-chips");
    subjChips.setAttribute("data-sw", "subject-chips");
    pTopic.appendChild(subjLabel); pTopic.appendChild(subjChips);

    var paperLabel = el("div", "sw-label", SAY.labelPaper);
    var paperChips = el("div", "sw-chips");
    paperChips.setAttribute("data-sw", "paper-chips");
    pTopic.appendChild(paperLabel); pTopic.appendChild(paperChips);

    pTopic.appendChild(el("div", "sw-label", SAY.labelTopics));
    var tree = el("div", "sw-tree");
    tree.setAttribute("data-sw", "tree");
    pTopic.appendChild(tree);

    /* ── panel 2: Detail ── */
    var pDetail = el("div", "sw-panel");
    pDetail.setAttribute("data-sw", "panel-detail");
    pDetail.appendChild(el("div", "sw-label", SAY.labelQuestions));
    var countChips = el("div", "sw-chips");
    countChips.setAttribute("data-sw", "count-chips");
    pDetail.appendChild(countChips);
    var qlist = el("div", "sw-qlist");
    qlist.setAttribute("data-sw", "qlist");
    pDetail.appendChild(qlist);

    pDetail.appendChild(el("div", "sw-label", SAY.labelTitle));
    var titleWrap = el("div", "sw-fields");
    var title = document.createElement("input");
    title.type = "text";
    title.className = "sw-input";
    title.maxLength = 80;
    title.setAttribute("aria-label", SAY.labelTitle);
    title.setAttribute("data-sw", "title");
    titleWrap.appendChild(title);
    pDetail.appendChild(titleWrap);

    pDetail.appendChild(el("div", "sw-label", SAY.labelRelease));
    var relChips = el("div", "sw-chips");
    relChips.setAttribute("data-sw", "release-chips");
    pDetail.appendChild(relChips);
    var relFields = el("div", "sw-fields");
    relFields.setAttribute("data-sw", "release-fields");
    var relDate = mkInput("date", SAY.releaseDate, "release-date");
    var relTime = mkInput("time", SAY.releaseTime, "release-time");
    relFields.appendChild(relDate); relFields.appendChild(relTime);
    pDetail.appendChild(relFields);

    pDetail.appendChild(el("div", "sw-label", SAY.labelDue));
    var dueFields = el("div", "sw-fields");
    var dueDate = mkInput("date", SAY.dueDate, "due-date");
    var dueTime = mkInput("time", SAY.dueTime, "due-time");
    dueFields.appendChild(dueDate); dueFields.appendChild(dueTime);
    pDetail.appendChild(dueFields);

    var hold = el("div", "sw-hold");
    hold.setAttribute("data-sw", "hold");
    hold.hidden = true;
    pDetail.appendChild(hold);

    body.appendChild(pClasses); body.appendChild(pTopic); body.appendChild(pDetail);
    sheet.appendChild(head); sheet.appendChild(body);
    overlay.appendChild(sheet);

    var toast = el("div", "sw-toast");
    toast.setAttribute("data-sw", "toast");
    toast.setAttribute("role", "status");
    toast.hidden = true;

    /* ⚠️ APPENDED TO <body>, NOT INTO `#mrb-teacher`. This is the fix. See
       the header: the runtime's `draw()` empties its own mount host on every
       page-level setState, so anything inside it is destroyed. A sibling of
       the host is not reachable from there. */
    document.body.appendChild(overlay);
    document.body.appendChild(toast);

    els = {
      overlay: overlay, sheet: sheet, head: head, back: back, step: step,
      primary: primary, body: body,
      pClasses: pClasses, classList: classList,
      pTopic: pTopic, tierChips: tierChips,
      subjLabel: subjLabel, subjChips: subjChips,
      paperLabel: paperLabel, paperChips: paperChips, tree: tree,
      pDetail: pDetail, countChips: countChips, qlist: qlist,
      title: title, relChips: relChips, relFields: relFields,
      relDate: relDate, relTime: relTime, dueDate: dueDate, dueTime: dueTime,
      hold: hold, toast: toast,
      treeRows: [], classRows: [], qRows: []
    };

    wireShell();
  }

  function mkInput(type, label, mark) {
    var i = document.createElement("input");
    i.type = type;
    i.className = "sw-input";
    i.setAttribute("aria-label", label);
    i.setAttribute("data-sw", mark);
    return i;
  }

  function wireShell() {
    els.overlay.addEventListener("click", function (e) {
      if (e.target === els.overlay) { close(); }
    });
    els.back.addEventListener("click", function () {
      if (!S) { return; }
      if (S.step === 0) { return close(); }
      S.step -= 1;
      syncStep();
    });
    els.primary.addEventListener("click", onPrimary);
    els.title.addEventListener("input", function () {
      if (!S) { return; }
      S.title = els.title.value;
      S.titleEdited = true;
      S.badTitle = false;
      syncValidity();
    });
    var dateTimeSync = function () {
      if (!S) { return; }
      S.releaseDate = els.relDate.value;
      S.releaseTime = els.relTime.value;
      S.dueDate = els.dueDate.value;
      S.dueTime = els.dueTime.value;
      S.badDue = false; S.badRelease = false;
      syncHold();
      syncValidity();
    };
    [els.relDate, els.relTime, els.dueDate, els.dueTime].forEach(function (i) {
      i.addEventListener("input", dateTimeSync);
      i.addEventListener("change", dateTimeSync);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && S) { close(); }
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     8. THE CHIP RAILS — built once per data load, toggled on selection.
     ═════════════════════════════════════════════════════════════════════ */

  /* `opts` = [{key, label, disabled}]. `onPick` gets the key. Returns the
     button list so a sync can toggle without rebuilding. */
  function buildChips(host, opts, onPick) {
    host.textContent = "";
    var out = [];
    opts.forEach(function (o) {
      var b = btn("sw-chip", o.label);
      b.setAttribute("data-sw-key", String(o.key));
      b.addEventListener("click", function () {
        if (b.disabled) { return; }
        onPick(o.key);
      });
      host.appendChild(b);
      out.push({ key: o.key, node: b });
    });
    return out;
  }

  function syncChips(list, active, isDisabled) {
    if (!list) { return; }
    list.forEach(function (c) {
      c.node.classList.toggle("is-on", String(c.key) === String(active));
      c.node.disabled = isDisabled ? !!isDisabled(c.key) : false;
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     9. THE TREE — built once per /scope, patched on every selection.
     ═════════════════════════════════════════════════════════════════════ */

  function countAt(node, tier) {
    var c = node && node.counts;
    var n = c ? c[tier] : 0;
    return (typeof n === "number" && n > 0) ? n : 0;
  }

  /* Design's own vocabulary over a real date. The question a teacher asks
     second is "have I already given them this?", so it is a fact about THIS
     class rather than about the topic. */
  function lastSetTag(iso) {
    if (!iso) { return SAY.notSet; }
    var t = Date.parse(iso);
    if (isNaN(t)) { return SAY.notSet; }
    var days = Math.floor((Date.now() - t) / DAY_MS);
    if (days < 7) { return SAY.setThisWeek; }
    return SAY.weeksAgo(Math.floor(days / 7));
  }

  function buildTree() {
    els.tree.textContent = "";
    els.treeRows = [];
    var tree = (S.scope && S.scope.tree) || [];

    tree.forEach(function (topic) {
      var wrap = el("div", "sw-node");
      var row = btn("sw-row", null);
      row.setAttribute("data-sw", "topic");
      row.setAttribute("data-sw-ref", String(topic.id));

      var kidsHost = el("div", "sw-kids");
      kidsHost.hidden = true;

      var chev = btn("sw-chev", null);
      chev.setAttribute("data-sw", "chevron");
      chev.setAttribute("aria-expanded", "false");
      chev.setAttribute("aria-label", String(topic.name || ""));
      chev.appendChild(svgChevron());

      var main = el("span", "sw-row-main");
      var name = el("span", "sw-row-name", String(topic.name || ""));
      var tag = el("span", "sw-row-tag", lastSetTag(topic.last_set_at));
      main.appendChild(name); main.appendChild(tag);

      var count = el("span", "sw-count", "0");

      row.appendChild(main); row.appendChild(count);

      /* The chevron sits OUTSIDE the selecting button so that expanding a
         topic is not the same press as selecting it. */
      var head = el("div", "sw-node-head");
      head.appendChild(row);
      if ((topic.children || []).length) { head.appendChild(chev); }
      else { chev.hidden = true; }

      wrap.appendChild(head);
      wrap.appendChild(kidsHost);
      els.tree.appendChild(wrap);

      var rec = {
        kind: "topic", ref: String(topic.id), data: topic,
        wrap: wrap, row: row, count: count, tag: tag, chev: chev,
        kidsHost: kidsHost, kids: []
      };
      els.treeRows.push(rec);

      row.addEventListener("click", function () {
        if (row.getAttribute("aria-disabled") === "true") { return; }
        pickScope("topic", rec.ref);
      });
      chev.addEventListener("click", function () {
        var open = chev.getAttribute("aria-expanded") === "true";
        chev.setAttribute("aria-expanded", open ? "false" : "true");
        kidsHost.hidden = open;
      });

      (topic.children || []).forEach(function (kid) {
        var krow = btn("sw-row", null);
        krow.setAttribute("data-sw", "subtopic");
        krow.setAttribute("data-sw-ref", String(kid.id));
        var kmain = el("span", "sw-row-main");
        kmain.appendChild(el("span", "sw-row-name", String(kid.name || "")));
        var kcount = el("span", "sw-count", "0");
        krow.appendChild(kmain); krow.appendChild(kcount);
        kidsHost.appendChild(krow);

        var krec = {
          kind: "subtopic", ref: String(kid.id), data: kid,
          parent: rec, row: krow, count: kcount
        };
        rec.kids.push(krec);
        els.treeRows.push(krec);

        krow.addEventListener("click", function () {
          if (krow.getAttribute("aria-disabled") === "true") { return; }
          pickScope("subtopic", krec.ref);
        });
      });
    });
  }

  /* ⚠️ THE PATCH. Called on every selection, every tier change and every
     filter change, and it BUILDS NOTHING. Counts, selection, availability
     and visibility are all attributes and text on nodes that already exist,
     so the scroller keeps its scrollTop and the teacher keeps their place. */
  function syncTree() {
    var tier = S.tier;
    els.treeRows.forEach(function (r) {
      var n = countAt(r.data, tier);
      r.count.textContent = String(n);
      var on = (S.scopeKind === r.kind && S.scopeRef === r.ref);
      r.row.classList.toggle("is-on", on);
      /* A zero-count row is shown with its `0` and refuses to be picked. */
      r.row.setAttribute("aria-disabled", n > 0 ? "false" : "true");
      if (r.kind === "topic") {
        r.wrap.hidden = !topicVisible(r.data);
      }
    });
    /* A filter that hides the chosen topic clears the choice rather than
       leaving Next live over a row nobody can see. */
    var sel = nodeFor(S.scopeKind, S.scopeRef);
    if (sel) {
      var top = (sel.kind === "topic") ? sel : sel.parent;
      if (top && top.wrap.hidden) { S.scopeKind = ""; S.scopeRef = ""; }
    }
    els.tree.classList.remove("sw-bad");
  }

  /* Subject and paper are FILTERS over the tree /scope already sent, applied
     by hiding rows. A separate-science class gets no subject chips at all
     (RISKS C5) and its tree only ever held one subject. */
  function topicVisible(topic) {
    if (S.subject !== "all" && topic.subject && topic.subject !== S.subject) {
      return false;
    }
    if (S.paper !== "both" && topic.paper && String(topic.paper) !== String(S.paper)) {
      return false;
    }
    return true;
  }

  function pickScope(kind, ref) {
    /* Selecting a subtopic deselects its topic and vice versa — one scope. */
    S.scopeKind = kind;
    S.scopeRef = ref;
    S.picked = [];
    S.expanded = {};
    S.swapDead = {};
    S.previewErr = false;
    if (!S.titleEdited) { S.title = autoTitle(); els.title.value = S.title; }
    syncTree();
    syncValidity();
  }

  function nodeFor(kind, ref) {
    for (var i = 0; i < els.treeRows.length; i++) {
      var r = els.treeRows[i];
      if (r.kind === kind && r.ref === ref) { return r; }
    }
    return null;
  }

  function autoTitle() {
    var r = nodeFor(S.scopeKind, S.scopeRef);
    if (!r) { return ""; }
    if (r.kind === "topic") { return String(r.data.name || "").slice(0, 80); }
    var parent = r.parent ? String(r.parent.data.name || "") : "";
    var own = String(r.data.name || "");
    return (parent ? parent + " · " + own : own).slice(0, 80);
  }

  /* ═════════════════════════════════════════════════════════════════════
     10. THE CLASS LIST — only cohort matches (RISKS C4).
     ═════════════════════════════════════════════════════════════════════ */

  function buildClasses() {
    els.classList.textContent = "";
    els.classRows = [];
    var list = (S.scope && S.scope.cohort_classes) || [];
    list.forEach(function (c) {
      var row = btn("sw-row", null);
      row.setAttribute("data-sw", "class");
      row.setAttribute("data-sw-ref", String(c.id));
      var box = el("span", null);
      box.style.cssText = "flex:none;width:16px;height:16px;border-radius:5px;" +
        "border:1.5px solid var(--st-rule-strong)";
      var main = el("span", "sw-row-main");
      main.appendChild(el("span", "sw-row-name", String(c.name || "")));
      main.appendChild(el("span", "sw-row-tag", SAY.pupils(c.pupils || 0)));
      row.appendChild(box); row.appendChild(main);
      els.classList.appendChild(row);
      var rec = { id: String(c.id), node: row, box: box };
      els.classRows.push(rec);
      row.addEventListener("click", function () {
        var i = S.classes.indexOf(rec.id);
        if (i > -1) { S.classes.splice(i, 1); } else { S.classes.push(rec.id); }
        syncClasses();
        syncValidity();
      });
    });
    syncClasses();
  }

  function syncClasses() {
    els.classRows.forEach(function (r) {
      var on = S.classes.indexOf(r.id) > -1;
      r.node.classList.toggle("is-on", on);
      r.node.setAttribute("aria-pressed", on ? "true" : "false");
      r.box.style.background = on ? "var(--st-accent-text)" : "transparent";
      r.box.style.borderColor = on ? "var(--st-accent-text)" : "var(--st-rule-strong)";
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     11. THE QUESTION LIST
     ═════════════════════════════════════════════════════════════════════ */

  var COUNTS = [5, 10, 15, 20];
  var LETTERS = ["A", "B", "C", "D"];

  function buildQuestions() {
    els.qlist.textContent = "";
    els.qRows = [];
    S.picked.forEach(function (q, i) {
      els.qlist.appendChild(buildQuestionRow(q, i));
    });
  }

  function buildQuestionRow(q, i) {
    var wrap = el("div", "sw-q");
    wrap.setAttribute("data-sw", "question");
    var head = el("div", "sw-q-head");
    var n = el("span", "sw-q-n", (i + 1) + ".");
    var stem = btn("sw-q-stem", null);
    stem.setAttribute("data-sw", "stem");
    setFormula(stem, q.stem);
    var swap = btn("sw-swap", SAY.swap);
    swap.setAttribute("data-sw", "swap");
    head.appendChild(n); head.appendChild(stem); head.appendChild(swap);

    var body = el("div", "sw-q-body");
    body.hidden = true;
    body.setAttribute("data-sw", "options");
    fillOptions(body, q);

    wrap.appendChild(head); wrap.appendChild(body);

    var rec = { i: i, wrap: wrap, stem: stem, body: body, swap: swap };
    els.qRows.push(rec);

    stem.addEventListener("click", function () { toggleQ(rec); });
    swap.addEventListener("click", function () { doSwap(rec); });
    return wrap;
  }

  function fillOptions(body, q) {
    body.textContent = "";
    var opts = q.options || [];
    for (var k = 0; k < opts.length; k++) {
      var row = el("div", "sw-opt");
      var key = el("span", "sw-opt-k", (LETTERS[k] || String(k + 1)) + ".");
      var text = el("span", null);
      text.style.minWidth = "0";
      setFormula(text, opts[k]);
      row.appendChild(key); row.appendChild(text);
      if (k === q.correct_index) {
        row.classList.add("is-right");
        row.appendChild(svgTick());
      }
      body.appendChild(row);
    }
  }

  /* Expanding toggles `hidden` on a node that already exists. Nothing is
     rebuilt, so the scroller does not move under the teacher's thumb. */
  function toggleQ(rec) {
    var open = !rec.body.hidden;
    rec.body.hidden = open;
    rec.wrap.classList.toggle("is-open", !open);
    S.expanded[rec.i] = !open;
  }

  /* ⚠️ SWAP REPLACES THE ROW'S TEXT, NEVER THE ROW. `exclude` is everything
     picked PLUS everything shown at any point this sheet session, so a swap
     can never hand back a question the teacher has already read and
     rejected (RISKS A6). A 204 means the pool is spent for this scope and
     tier, and that row's Swap goes dead rather than lying. */
  function doSwap(rec) {
    if (rec.swap.disabled || S.busy) { return; }
    var exclude = Object.keys(S.shown);
    S.picked.forEach(function (p) {
      if (exclude.indexOf(String(p.id)) < 0) { exclude.push(String(p.id)); }
    });
    rec.swap.disabled = true;
    apiGet("/api/teacher/set-work/swap?class_id=" + encodeURIComponent(S.classId) +
      "&tier=" + encodeURIComponent(S.tier) +
      "&scope_kind=" + encodeURIComponent(S.scopeKind) +
      "&scope_ref=" + encodeURIComponent(S.scopeRef) +
      "&exclude=" + encodeURIComponent(exclude.join(","))
    ).then(function (r) {
      if (r.status === 204 || !r.body || !r.body.id) {
        S.swapDead[rec.i] = true;
        return;                              // stays disabled
      }
      var q = r.body;
      S.shown[String(q.id)] = true;
      S.picked[rec.i] = q;
      setFormula(rec.stem, q.stem);
      fillOptions(rec.body, q);
      rec.swap.disabled = false;
    }, function () {
      rec.swap.disabled = false;
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     12. FETCHES
     ═════════════════════════════════════════════════════════════════════ */

  function loadScope() {
    S.scopeErr = false;
    return apiGet("/api/teacher/set-work/scope?class_id=" +
                  encodeURIComponent(S.classId)).then(function (r) {
      S.scope = r.body || {};
      var k = S.scope.class || {};
      S.holdIso = k.open_from || "";
      var tiers = S.scope.tiers || [];
      S.tier = k.default_tier ||
        (tiers.indexOf("medium") > -1 ? "medium" : (tiers[0] || ""));
      buildClasses();
      buildTierChips();
      buildSubjectChips();
      buildPaperChips();
      buildTree();
      syncTree();
      syncValidity();
      return true;
    }, function () {
      S.scope = null;
      S.scopeErr = true;
      els.tree.textContent = "";
      els.treeRows = [];
      var tag = el("div", "sw-row-tag", SAY.unavailable);
      els.tree.appendChild(tag);
      syncValidity();
      return false;
    });
  }

  /* The cap the count chips obey. Before /preview answers it is the count
     /scope already sent for this node at this tier — which IS the
     availability — so the normal path costs one request, not two. */
  function scopeAvailable() {
    var r = nodeFor(S.scopeKind, S.scopeRef);
    return r ? countAt(r.data, S.tier) : 0;
  }

  function loadPreview() {
    var cap = S.available || scopeAvailable();
    var want = Math.min(S.count, cap > 0 ? cap : S.count);
    S.busy = true;
    S.previewErr = false;
    syncValidity();
    /* ⚠️ NO `exclude` HERE, DELIBERATELY. `exclude` is /swap's contract: it
       stops a swap handing back a question the teacher has already read.
       Sending this session's shown-set to /preview instead would mean going
       BACK a step and forward again silently produced a different set of
       questions, and would eat the pool a scope has. */
    return apiGet("/api/teacher/set-work/preview?class_id=" +
      encodeURIComponent(S.classId) +
      "&tier=" + encodeURIComponent(S.tier) +
      "&scope_kind=" + encodeURIComponent(S.scopeKind) +
      "&scope_ref=" + encodeURIComponent(S.scopeRef) +
      "&count=" + encodeURIComponent(want)
    ).then(function (r) {
      var d = r.body || {};
      S.busy = false;
      S.picked = d.picked || [];
      S.available = (typeof d.available === "number") ? d.available : cap;
      S.picked.forEach(function (q) { S.shown[String(q.id)] = true; });
      S.swapDead = {};
      S.expanded = {};
      capCount();
      buildQuestions();
      syncCountChips();
      syncValidity();
      return true;
    }, function () {
      S.busy = false;
      S.previewErr = true;
      S.picked = [];
      els.qlist.textContent = "";
      els.qRows = [];
      els.qlist.appendChild(el("div", "sw-row-tag", SAY.unavailable));
      syncValidity();
      return false;
    });
  }

  /* Chips above availability are disabled, and a default that is now above
     it drops to the largest chip that is not (RISKS A4). */
  function capCount() {
    var cap = S.available;
    if (cap > 0 && S.count > cap) {
      var best = COUNTS[0];
      for (var i = 0; i < COUNTS.length; i++) {
        if (COUNTS[i] <= cap) { best = COUNTS[i]; }
      }
      S.count = best;
    }
  }

  /* ═════════════════════════════════════════════════════════════════════
     13. CHIP BUILDERS
     ═════════════════════════════════════════════════════════════════════ */

  function buildTierChips() {
    var tiers = (S.scope && S.scope.tiers) || [];
    els.tierList = buildChips(els.tierChips, tiers.map(function (t) {
      return { key: t, label: SAY.tier[t] || t };
    }), function (k) {
      S.tier = k;
      S.available = 0;
      S.picked = [];
      /* A selected node that has dropped to zero at the new tier deselects
         itself, which is what disables Next (RISKS A5). */
      var r = nodeFor(S.scopeKind, S.scopeRef);
      if (r && countAt(r.data, S.tier) === 0) { S.scopeKind = ""; S.scopeRef = ""; }
      syncTree();                        // re-counts IN PLACE, no request
      syncChips(els.tierList, S.tier);
      syncValidity();
    });
    syncChips(els.tierList, S.tier);
  }

  function buildSubjectChips() {
    var subs = (S.scope && S.scope.subjects) || [];
    /* No subject chips on a separate-science class: its tree holds one
       subject and a chip rail with one live option is a control that cannot
       do anything. */
    var show = subs.length > 1;
    els.subjLabel.hidden = !show;
    els.subjChips.hidden = !show;
    if (!show) { S.subject = "all"; els.subjList = []; return; }
    var opts = subs.map(function (s) {
      return { key: s, label: SAY.subject[s] || s };
    });
    opts.push({ key: "all", label: SAY.subjectAll });
    els.subjList = buildChips(els.subjChips, opts, function (k) {
      S.subject = k;
      syncTree();                        // hides rows, builds nothing
      syncChips(els.subjList, S.subject);
      syncValidity();
    });
    syncChips(els.subjList, S.subject);
  }

  function buildPaperChips() {
    var papers = (S.scope && S.scope.papers) || null;
    var show = !!(papers && papers.length);
    els.paperLabel.hidden = !show;
    els.paperChips.hidden = !show;
    if (!show) { S.paper = "both"; els.paperList = []; return; }
    var opts = papers.map(function (p) {
      return { key: String(p), label: SAY.paper[Number(p) - 1] || ("Paper " + p) };
    });
    opts.push({ key: "both", label: SAY.paperBoth });
    els.paperList = buildChips(els.paperChips, opts, function (k) {
      S.paper = k;
      syncTree();
      syncChips(els.paperList, S.paper);
      syncValidity();
    });
    syncChips(els.paperList, S.paper);
  }

  function buildCountChips() {
    els.countList = buildChips(els.countChips, COUNTS.map(function (n) {
      return { key: n, label: String(n) };
    }), function (k) {
      S.count = k;
      syncCountChips();
      loadPreview();
    });
    syncCountChips();
  }

  function syncCountChips() {
    var cap = S.available || scopeAvailable();
    syncChips(els.countList, S.count, function (k) {
      return cap > 0 && Number(k) > cap;
    });
  }

  function buildReleaseChips() {
    els.relList = buildChips(els.relChips, [
      { key: "now", label: SAY.now },
      { key: "later", label: SAY.later }
    ], function (k) {
      S.release = k;
      S.badRelease = false;
      syncRelease();
      syncHold();
      syncValidity();
    });
    syncRelease();
  }

  function syncRelease() {
    syncChips(els.relList, S.release);
    els.relFields.hidden = (S.release !== "later");
  }

  /* ═════════════════════════════════════════════════════════════════════
     14. THE HOLD LINE — one line, a date, only when it applies.
     ═════════════════════════════════════════════════════════════════════ */

  function syncHold() {
    var show = false;
    if (S.holdIso) {
      var open = Date.parse(S.holdIso);
      if (!isNaN(open)) {
        var chosen = (S.release === "later")
          ? Date.parse(londonToUtcIso(S.releaseDate, S.releaseTime) || "")
          : Date.now();
        if (!isNaN(chosen) && chosen < open) { show = true; }
      }
    }
    if (S.showHold) { show = true; }       // the server said `clamped`
    els.hold.hidden = !show;
    if (show) { els.hold.textContent = SAY.hold(londonDateLabel(S.holdIso)); }
  }

  /* ═════════════════════════════════════════════════════════════════════
     15. VALIDITY — a disabled primary and an outlined field. No sentences.
     ═════════════════════════════════════════════════════════════════════ */

  function releaseIso() {
    if (S.release === "now") { return null; }
    return londonToUtcIso(S.releaseDate, S.releaseTime);
  }
  function dueIso() { return londonToUtcIso(S.dueDate, S.dueTime); }

  function stepValid() {
    /* Nothing is valid before /scope answers. Without this the primary is
       live on step 0 the instant the sheet opens — the opening class is
       preselected — and a fast press lands on an empty topic list. */
    if (!S.scope) { return false; }
    if (S.step === 0) { return S.classes.length > 0; }
    if (S.step === 1) {
      if (!S.scopeKind || !S.scopeRef) { return false; }
      return scopeAvailable() > 0;
    }
    // Detail
    if (S.busy || S.previewErr) { return false; }
    if (!S.picked.length || S.picked.length > 20) { return false; }
    var t = String(S.title || "").trim();
    if (!t.length || t.length > 80) { return false; }
    var due = dueIso();
    if (!due) { return false; }
    var dueMs = Date.parse(due);
    var relMs = S.release === "later" ? Date.parse(releaseIso() || "") : Date.now();
    if (S.release === "later" && isNaN(relMs)) { return false; }
    if (isNaN(dueMs) || dueMs <= relMs) { return false; }
    if (dueMs > Date.now() + 365 * DAY_MS) { return false; }
    if (S.release === "later" && relMs < Date.now() - 5 * 60000) { return false; }
    return true;
  }

  function syncValidity() {
    els.primary.disabled = !stepValid();
    els.primary.textContent = (S.step === 2) ? SAY.set : SAY.next;
    els.back.textContent = (S.step === 0) ? SAY.cancel : SAY.back;
    /* The outline: only on a field the teacher has actually filled wrongly,
       never on one they have simply not reached yet. */
    if (S.step === 2) {
      var t = String(S.title || "").trim();
      els.title.classList.toggle("sw-bad", S.badTitle || (S.titleEdited && !t.length));
      var due = dueIso(), dueMs = due ? Date.parse(due) : NaN;
      var relMs = S.release === "later" ? Date.parse(releaseIso() || "") : Date.now();
      var dueBad = S.badDue || (!!S.dueDate && !!S.dueTime &&
        (isNaN(dueMs) || dueMs <= relMs || dueMs > Date.now() + 365 * DAY_MS));
      els.dueDate.classList.toggle("sw-bad", dueBad);
      els.dueTime.classList.toggle("sw-bad", dueBad);
      var relBad = S.badRelease || (S.release === "later" && !!S.releaseDate &&
        !!S.releaseTime && (isNaN(relMs) || relMs < Date.now() - 5 * 60000));
      els.relDate.classList.toggle("sw-bad", relBad);
      els.relTime.classList.toggle("sw-bad", relBad);
    }
  }

  /* ═════════════════════════════════════════════════════════════════════
     16. STEPS
     ═════════════════════════════════════════════════════════════════════ */

  function syncStep() {
    els.step.textContent = SAY.steps[S.step];
    els.pClasses.hidden = (S.step !== 0);
    els.pTopic.hidden = (S.step !== 1);
    els.pDetail.hidden = (S.step !== 2);
    /* A step change is a NEW SCREEN, so the scroller starts at the top —
       which is the one place a scroll reset is correct, and it is not a
       selection. */
    els.sheet.scrollTop = 0;
    syncValidity();
  }

  function onPrimary() {
    if (!S || els.primary.disabled) { return; }
    if (S.step === 0) { S.step = 1; syncStep(); syncTree(); return; }
    if (S.step === 1) {
      S.step = 2;
      S.available = 0;
      if (!S.titleEdited) { S.title = autoTitle(); els.title.value = S.title; }
      S.dueDate = S.dueDate || londonDatePlus(7);
      S.dueTime = S.dueTime || "18:00";
      S.releaseDate = S.releaseDate || londonDatePlus(1);
      els.dueDate.value = S.dueDate;
      els.dueTime.value = S.dueTime;
      els.relDate.value = S.releaseDate;
      els.relTime.value = S.releaseTime;
      syncStep();
      syncRelease();
      syncHold();
      loadPreview();
      return;
    }
    submit();
  }

  function submit() {
    if (S.busy) { return; }
    S.busy = true;
    syncValidity();
    var payload = {
      class_ids: S.classes.slice(),
      tier: S.tier,
      scope_kind: S.scopeKind,
      scope_ref: S.scopeRef,
      question_ids: S.picked.map(function (q) { return q.id; }),
      title: String(S.title || "").trim(),
      release_at: releaseIso(),
      due_at: dueIso()
    };
    var title = payload.title;
    var classCount = payload.class_ids.length;
    var only = classCount === 1 ? classNameOf(payload.class_ids[0]) : "";
    apiPost("/api/teacher/set-work", payload).then(function (r) {
      S.busy = false;
      if (!r.ok || !r.body || !r.body.success) {
        syncValidity();
        toast(SAY.notSetToast);
        return;
      }
      if (r.body.clamped) { S.showHold = true; syncHold(); }
      var done = { title: title, classIds: payload.class_ids,
                   assignmentIds: r.body.assignment_ids || [],
                   releaseAt: r.body.release_at || null,
                   clamped: !!r.body.clamped };
      close();
      toast(classCount === 1 && only
        ? SAY.setForClass(title, only)
        : SAY.setForClasses(title, classCount));
      /* ⚠️ THE REFRESH SEAM, and it is what v1 never had. v1's `swNext`
         ended in `this.ping(...)` and nothing else, so the class card a
         teacher had just set work to still read "no work set" until they
         reloaded the page. The generated page registers this hook in
         `teacher_rulings.py` and re-reads its own screen through
         `MrBadmusTeacherLive.load` — the same mechanism `MRB_REFRESH_FEED`
         and `MRB_REFRESH_FEEDBACK` already use. A page that has not
         registered one simply keeps its stale card, exactly as v1 did. */
      if (typeof window.MRB_SET_WORK_DONE === "function") {
        try { window.MRB_SET_WORK_DONE(done); }
        catch (e) { console.error("[set-work] refresh hook", e); }
      }
    }, function () {
      S.busy = false;
      syncValidity();
      toast(SAY.notSetToast);
    });
  }

  function classNameOf(id) {
    var list = (S.scope && S.scope.cohort_classes) || [];
    for (var i = 0; i < list.length; i++) {
      if (String(list[i].id) === String(id)) { return String(list[i].name || ""); }
    }
    return "";
  }

  function toast(msg) {
    buildShell();
    els.toast.textContent = msg;
    els.toast.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { els.toast.hidden = true; }, 3200);
  }

  /* ═════════════════════════════════════════════════════════════════════
     17. OPEN / CLOSE
     ═════════════════════════════════════════════════════════════════════ */

  function open(opts) {
    var o = opts || {};
    if (!o.classId) { return; }
    buildShell();
    S = freshState(String(o.classId));
    els.title.value = "";
    els.relTime.value = S.releaseTime;
    els.dueTime.value = S.dueTime;
    els.relDate.value = "";
    els.dueDate.value = "";
    els.qlist.textContent = "";
    els.qRows = [];
    els.tree.textContent = "";
    els.treeRows = [];
    els.classList.textContent = "";
    els.classRows = [];
    els.hold.hidden = true;
    buildCountChips();
    buildReleaseChips();
    syncStep();
    els.overlay.hidden = false;
    /* The one `focus()` in this file, and it is at OPEN — never after a
       state change. RISKS A1 bans the second, not the first: a dialog that
       does not take focus is unreachable from a keyboard. */
    els.sheet.focus({ preventScroll: true });
    loadScope();
  }

  function close() {
    if (!els) { return; }
    els.overlay.hidden = true;
    S = null;
  }

  /* ═════════════════════════════════════════════════════════════════════
     18. SURFACE
     ═════════════════════════════════════════════════════════════════════ */

  window.MRBSetWork = {
    open: open,
    close: close,
    /* Pure, tested by `tools/set_work_time_test.js`. Exported so the test can
       reach them without a browser, and so a drive can assert the conversion
       rather than infer it from a rendered date. */
    londonToUtcIso: londonToUtcIso,
    utcToLondonParts: utcToLondonParts,
    londonOffsetMinutesAt: londonOffsetMinutesAt,
    londonDateLabel: londonDateLabel,
    formulaFrag: formulaFrag,
    SAY: SAY
  };
})();
