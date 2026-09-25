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

  /* "14 Sep 2026".

     ⊕ MRB-336 — EXPORT-ONLY NOW, and deliberately kept. It formatted the
     hold line, and the hold line is gone: the school hold no longer governs
     what a teacher sets, so the sheet no longer mentions it. The function
     stays because `tools/set_work_time_test.js` drives it as London-parts
     arithmetic — the same arithmetic the release and due fields run on —
     and those three cases are the only place that arithmetic is pinned. */
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

  /* ⊕ first-week fixes (22 Sep 2026) — EVERY READ SETTLES, AND A HUNG ONE IS A FAILURE RATHER THAN A
     FOREVER.

     ⛔ There was no timeout, and three controls were disabled for the life of
     a request that never answered: `Next` on the classes step (it waited for
     `/scope` to resolve), the primary on the Detail step (`sc.busy` is only
     cleared by a preview's own handlers) and one row's `Swap`. A fetch that
     never settles is not rare — a laptop lid closed on a school corridor, a
     Render instance paged out mid-response — and it left a sheet with nothing
     on screen saying why and no way to make it try again.

     Thirty seconds, and it is deliberately generous: `/scope` on a KS3 class
     pages five thousand bank rows, and a Render cold start is twenty seconds
     of honest waiting. This is the bound on "never", not a latency budget.

     ⚠️ GET ONLY. `apiPost` and `apiPatch` do NOT get one, and must not: a set
     whose POST is aborted may ALREADY HAVE BEEN WRITTEN, and a sheet that
     then let the teacher press again is the two-assignments-for-thirty-children
     defect `close()` was hardened against. A read is safe to abandon; a write
     is not. */
  var READ_TIMEOUT_MS = 30000;

  function apiGet(path) {
    var ctl = (typeof AbortController === "function") ? new AbortController() : null;
    var timer = null;
    var done = function () { if (timer) { clearTimeout(timer); timer = null; } };
    return token().then(function (t) {
      if (ctl) {
        timer = setTimeout(function () { try { ctl.abort(); } catch (e) { /* gone */ } },
                           READ_TIMEOUT_MS);
      }
      return fetch(apiBase() + path, {
        headers: { Authorization: "Bearer " + t },
        signal: ctl ? ctl.signal : undefined
      });
    }).then(function (res) {
      done();
      return res;
    }, function (e) {
      done();
      throw e;
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

  /* ⊕ MRB-336 — the same envelope as `apiPost`, with a method. A row that
     already exists is CHANGED, not set again: a second POST would be a
     second assignment for thirty children. */
  function apiPatch(path, payload) {
    return token().then(function (t) {
      return fetch(apiBase() + path, {
        method: "PATCH",
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
    setForClasses: function (title, n) { return title + " · Set for " + n + " classes"; },
    setForClass: function (title, name) { return title + " · " + name; },
    /* ⚠️ THE TWO REFUSAL LABELS, and they are the judgement call in this
       list. A9 bans sentences, not honesty: a sheet whose topic list failed
       to load and says NOTHING is a blank panel a teacher reads as "this
       class has no topics", which is a lie told by omission. These are noun
       phrases in the tag slot — the same two words a status chip carries —
       and there is no third. */
    /* ⊕ MRB-336 — EDIT. The primary's verb when the sheet was opened on a
       row that already exists: a set that is being CHANGED is saved, not
       set again. One word, and the only string this ticket adds to the
       sheet's visible vocabulary — the two labels above a released set's
       read-only values are `labelTier` and `steps[1]`, which are already
       here because the Topic step uses them. */
    save: "Save",
    /* ⊕ first-week fixes (22 Sep 2026) — TWO MORE, AND A9 STILL HOLDS. `Next` now enables the moment
       a class is ticked rather than waiting for `/scope`, so the Topic step is
       reachable before the tree exists. A panel that is empty because a
       request is in flight looks exactly like a panel that is empty because
       the class has no topics — which is the same lie by omission the two
       refusal labels above were added to stop. `Loading` is a status noun in
       the tag slot, exactly where `Unavailable` goes; `Retry` is a button
       verb, like `Save` and `Back`. Neither is a sentence. */
    loading: "Loading",
    retry: "Retry",
    unavailable: "Unavailable",
    notSetToast: "Not set",
    notSavedToast: "Not saved",
    savedFor: function (title) { return title + " \u00b7 Saved"; },
    /* \u2295 MRB-342 \u2014 SIX WORDS, AND NOT A SEVENTH. Multi-topic picking needs
       one verb (`Add topic`); the worksheet needs its own noun (`Worksheet`),
       its verb (`Download`), the two formats (`PDF`, `Word`) and the one
       thing a teacher chooses about the file (`Answers`). Every one is a
       noun or a button verb, so A9 holds without an exception.

       \u26a0\ufe0f THERE IS NO SEVENTH FOR "THE DOWNLOAD FAILED", deliberately. The
       refusal reuses `unavailable`, which is already the sheet's word for
       "this could not be got" and is already on the allowed list. A new
       failure string here would be a second way of saying the same thing.

       \u26a0\ufe0f AND THERE IS NO "REMOVE". A scope is taken back out by the gesture
       that put it in \u2014 tapping its row again on the Topic step, which is
       only a toggle once a second scope exists \u2014 and by Back, which drops a
       slot the teacher never filled. A control whose label is a word this
       list does not have is not a control this sheet can draw. */
    download: "Download",
    addTopic: "Add topic",
    worksheet: "Worksheet",
    pdf: "PDF",
    word: "Word",
    answers: "Answers",
    /* ⊕ MRB-342.1 — A SEVENTH, and it is a noun phrase like the six.
       `Multiple choice` names the one other property of the file a teacher
       chooses. Turned off, a question draws ruled answer lines instead of
       A/B/C/D — except where the stem points at its own options, which the
       SERVER decides; see `stemNeedsOptions` in the backend's worksheet.js.
       There is deliberately no word for that exception on this surface: a
       control that said "mostly" would be a control a teacher has to think
       about, and the sheet they get is right either way. */
    multipleChoice: "Multiple choice",
    /* ⊕ MRB-342.2 — FOUR MORE, AND EACH IS STILL A NOUN, A LABEL OR A
       COMPOSED NUMBER — never a sentence.

       `onePerTopic` names the ZIP choice beside `Multiple choice` and
       `Answers`; it is a checkbox in the same idiom, so it is a noun phrase
       like its two neighbours. `labelNote` is a field label, exactly like
       `labelTitle` above it. `charsLeft` and the two clamp notes are
       composed strings — a number plus fixed words — the same shape as
       `weeksAgo` and `pupils`.

       ⚠️ THE TWO CLAMP NOTES ARE RULED WORDING (contract §1.3), verbatim.
       The tier word is `SAY.tier[tier]` — already on this list — reused,
       never re-derived. */
    onePerTopic: "One file per topic",
    labelNote: "Note",
    charsLeft: function (n) { return n + " left"; },
    capNotePool: function (n, tierLabel) {
      return "Only " + n + " at " + tierLabel + ". All " + n + " added.";
    },
    capNoteCeiling: function (n) {
      return n + " is the most in one topic. " + n + " added.";
    },
    /* ⊕ MRB-342.2 §1.4 — the settled line a used-up Swap shows instead of
       nothing. Ruled wording, verbatim. */
    swapExhausted: "No more questions in this topic."
  };

  /* ═════════════════════════════════════════════════════════════════════
     5. STATE
     ═════════════════════════════════════════════════════════════════════ */

  var S = null;          // the open sheet's state, or null
  var els = null;        // built DOM, kept between renders
  var toastTimer = null;
  var opens = 0;         // how many times the sheet has been opened, ever

  /* ═══════════════════════════════════════════════════════════════════
     STALE-RESPONSE GUARDS. ⊕ MRB-335, added after a drive reproduced the
     failure deterministically.

     ⚠️ WITHOUT THESE, WHICH CLASS'S CURRICULUM THE TEACHER SEES IS DECIDED
     BY NETWORK ARRIVAL ORDER RATHER THAN BY WHICH CLASS THEY OPENED.

     FOUR buttons open this one sheet — the classes screen's primary, the
     class screen's primary, a class card and the empty state — and the
     header above already notes that a sweep can press a second one while
     the first is still open. What it did not account for is the REQUEST
     the first press left in flight. `loadScope`'s `.then` closes over no
     identity at all: it writes into whatever `S` happens to be when it
     resolves, and repaints the tree, the tier chip and the subject rail
     from it.

     Measured (set_work_drive, `sheet_shows_the_class_it_was_opened_for`):
     open 10a/Bi1 (Triple Higher Biology), then 10b/Sc5 (Combined
     Foundation) 150ms later with the first response held two seconds. The
     sheet ends up flagged `data-sw-class = 10b/Sc5` and drawn as
     10a/Bi1 — seven topics, the subject rail hidden, and the tier chip on
     HIGHER.

     ⚠️ THE TIER IS WHY THIS MATTERS RATHER THAN MERELY LOOKING WRONG.
     `S.classId` stays correct, so the write goes to the right class — at
     `S.tier`, which is now the OTHER class's default. Most base subtopics
     are in both trees, so the request is accepted, and a Foundation group
     is set Higher questions with the chip agreeing that they should be.

     Two counters rather than one, because there are two different
     staleness questions:

       `session`  — bumped by open() and close(). Any answer that arrives
                    after the sheet has been reopened or closed is for a
                    sheet that no longer exists.
       `fetchSeq` — bumped by every /scope and /preview request. Two count
                    chips tapped quickly are two legitimate requests within
                    ONE session, and the later one must win however they
                    arrive.
     ═══════════════════════════════════════════════════════════════════ */
  var session = 0;
  var fetchSeq = 0;
  /* True when the sheet was opened FROM a class — a card, the class screen,
     the empty state. False from the classes screen, where there is no class
     and the first tap chooses one. It decides one thing: whether unticking
     the last class un-anchors. Anchored, the anchor is the page's fact and
     is not the teacher's to clear by unticking. */
  var isAnchoredOpen = false;
  /* Restored on close, so a keyboard user is put back where they were. */
  var opener = null;

  /* ⊕ MRB-335 — AN IDEMPOTENCY KEY, because "it did not answer" and "it did
     not happen" are different facts and the network cannot tell them apart.

     A POST that times out after the server has written is indistinguishable
     here from one that never arrived. Without a key the honest options are
     both bad: retry and risk two identical assignments for thirty children,
     or refuse to retry and leave a teacher who pressed Set work unsure
     whether they did. With one, the server replays the first answer and the
     retry is free.

     `client_ref` identifies A COMPOSED SET, not a press — so it is minted
     when the Detail step is first reached, REUSED across retries of the same
     set, and regenerated whenever the questions change (every `/preview`)
     or the set lands. Reusing it across a genuinely different set would make
     the second set silently replay the first. */
  function uuid() {
    try {
      if (window.crypto && window.crypto.randomUUID) {
        return window.crypto.randomUUID();
      }
    } catch (e) { /* falls through */ }
    /* Not a v4 UUID and does not claim to be — it is a collision-resistant
       token for one browser tab, and the server treats it as opaque. */
    return "sw-" + Date.now().toString(36) + "-" +
           Math.random().toString(36).slice(2, 12) +
           Math.random().toString(36).slice(2, 12);
  }

  /* ⊕ MRB-342 — ONE SCOPE'S WHOLE STATE, AND WHY IT IS NOT ON `S`.

     A teacher setting Energy changes AND Rates picks a number for each, gets
     a list for each, and swaps rows inside each. Those are three facts per
     scope, not three facts per sheet: with `count`, `picked` and `swapDead`
     on `S`, adding a second topic would silently overwrite the first one's
     answers, and the teacher would press Set work over a list they had
     already replaced without seeing it happen.

     `seq` is the per-scope half of the staleness guard. The global `fetchSeq`
     is bumped by `/scope` only now, because two scopes' previews are two
     legitimate requests at once and a global bump would make the second kill
     the first — the same shape of bug the swap guard above was written for,
     one level out. A preview answer is kept when the session, the global
     `fetchSeq` AND its own scope's `seq` are all unchanged. */
  function freshScope() {
    return {
      kind: "",                // 'topic' | 'subtopic'
      ref: "",
      count: 10,
      available: 0,
      /* ⊕ MRB-342.2 — the server's own word for why `count` was not what was
         typed: "pool" | "ceiling" | null. Drives `capNote` below. */
      cappedBy: null,
      /* The inline line shown under this scope's count field, or null. Set
         from `cappedBy` after every `/preview` answer (`capNoteFor`), and
         cleared whenever the scope's node or tier changes
         (`resetScopeQuestions`). */
      capNote: null,
      picked: [],
      expanded: {},
      swapDead: {},
      /* ⊕ MRB-342.2 §1.4 — a settled line for a row whose Swap came back 204,
         keyed by the row's index, same shape as `swapDead`. */
      swapNote: {},
      previewErr: false,
      busy: false,
      seq: 0,
      els: null                // the section's nodes, built once per scope
    };
  }

  /* The slot the Topic step is answering for. Never null: `freshState` opens
     with one, and `Add topic` appends before it moves `si`. */
  function cur() { return S.scopes[S.si] || S.scopes[0]; }

  /* Every scope that has actually been given a node. A slot the teacher
     added and then walked away from is not part of the set.

     ⚠️ AN EDIT'S SLOT 0 ALWAYS COUNTS, WHATEVER IT HOLDS, AND THAT IS NOT A
     CONVENIENCE. `edit()` fills the scope from the ROW — `p.scope_kind` and
     `p.scope_ref` off the table — and a row written before MRB-335 added
     those columns carries neither. Under a strict filter such a row would
     have no scope at all, so `syncScopes` would draw no section for it,
     `loadStoredQuestions` would have nowhere to render the work the children
     were actually given, and `pickedTotal()` would be 0 — which disables
     Save on the one screen where a teacher is only trying to move a
     deadline. An edit is single-scope by construction (`Add topic` is hidden
     for the whole of one), so counting its only slot can never widen a set.

     ⚠️ IT DOES NOT LEAK INTO WHAT IS SENT. `submit()` maps over this list and
     is never reached in edit mode; `saveEdit()` reads `cur()` directly; and
     `download()` drops any scope with no `scope_kind`/`scope_ref` of its own
     before it builds a body. */
  function filledScopes() {
    return S.scopes.filter(function (sc, i) {
      return (!!sc.kind && !!sc.ref) || (!!S.editId && i === 0);
    });
  }

  function pickedTotal() {
    var n = 0;
    filledScopes().forEach(function (sc) { n += sc.picked.length; });
    return n;
  }

  /* ⊕ first-week fixes, ruled by Mide 22 Sep 2026 — THE COUNT IS PER TOPIC, AND
     `othersTotal()` IS GONE.

     ⛔ IT USED TO EXIST AND IT WAS THE BUG. It read:

         "The questions every OTHER scope is already spending, so a count chip
          that would push the set past the server's twenty is not offered."

     …and its answer was subtracted from `MAX_QUESTIONS` in four places —
     `syncCountChips`, `loadPreview` (twice), and the ceiling on `Add topic`.
     The result, in Mide's first real week of teaching with the sheet: with
     three topics on it, 15 and 20 were greyed on ALL THREE even though every
     one of them held thirty-odd questions in the bank, and with two topics the
     chips still stopped at 10. The number a teacher was allowed to give one
     class was being spent by the OTHER topics they had chosen, which is not a
     fact about anything — a pool belongs to a subtopic and so does the demand.

     Ruled: a teacher picks the count they want per topic — 5, 10, 15, 20 —
     limited only by THAT topic's own pool at the chosen tier. Nothing about
     the rest of the sheet reaches a count chip.

     What bounds a set instead is `MAX_SCOPES`: how many topics may be on one
     sheet. It is worn by `Add topic` — the control that actually adds one —
     and by nothing else. Both numbers are the backend's, and the names are
     its names: `SW.MAX_QUESTIONS_PER_SCOPE` and `SW.MAX_SCOPES` in
     `set-work-scope.js`.

     ⚠️ `pickedTotal()` SURVIVES and is still read — by `Download` (is there
     anything to print?) and by `stepValid` (has every scope got rows?). It is
     no longer a CEILING anywhere. */
  /* ⊕ MRB-342.2 — THE PER-SCOPE CEILING IS NO LONGER A NUMBER IN THIS FILE.
     It was 20 above, then a flat 500 while this ticket was being built — and
     both were wrong the same way: a real KS4 topic pool measured on TEST
     (`biology/ecology`, Foundation, triple) holds **1,450** rows, so any
     constant this file could pin would eventually BE the product cap for a
     big topic while calling itself a safety guard.

     `GET /api/teacher/set-work/scope` now answers a top-level
     `max_per_scope` — the server's own current ceiling, read fresh every
     time the sheet opens, never hand-copied. `maxPerScope()` is the one
     place that reads it; nothing else in this file may name a number for
     this. `MAX_QUESTIONS_FALLBACK` exists only for a `/scope` answer that
     predates the field — an older backend during the split-deploy window —
     and is a conservative guess rather than a real ceiling: large enough
     that it will essentially never bind against a real pool, so hitting it
     produces the ceiling NOTE rather than a request the server refuses. */
  var MAX_QUESTIONS_FALLBACK = 500;
  function maxPerScope() {
    var n = S && S.scope && S.scope.max_per_scope;
    return (typeof n === "number" && n > 0) ? n : MAX_QUESTIONS_FALLBACK;
  }
  var MAX_SCOPES = 10;         // topics on one sheet — `Add topic`'s ceiling

  function freshState(classId) {
    return {
      /* ⊕ MRB-335 — THE ANCHOR MAY BE EMPTY, and on the classes screen it
         always is. See `open()`. Everything scoped — the tree, the tier
         list, the cohort — comes from `/scope?class_id=`, so until a class
         is chosen there is nothing to ask for and step 0 is the only step
         that can be drawn. */
      classId: classId,
      step: 0,                 // 0 Classes, 1 Topic, 2 Detail
      scope: null,             // the /scope answer
      scopeErr: false,
      /* ⊕ first-week fixes (22 Sep 2026) — IN FLIGHT, and it is a THIRD state rather than the
         absence of the other two. `scope === null && !scopeErr` used to mean
         both "nothing has been asked for yet" and "an answer is on its way",
         and the Topic panel cannot tell a teacher which of those it is
         showing without being told. Owned by `loadScope` and cleared ONLY by
         the fetch whose `fetchSeq` is still current, so a superseded answer
         can never report the current request as finished. */
      scopeLoading: false,
      /* Anchored (a card, the class screen): that class, ticked. Unanchored
         (the classes screen): nothing, and the first tap anchors. */
      classes: classId ? [classId] : [],
      /* The rows step 0 draws: every class this teacher may set work to,
         from the page, before any request. `cohortIds` is null until
         `/scope` answers and then names the ones that may be set TOGETHER. */
      classPool: [],
      cohortIds: null,
      clientRef: "",
      submitting: false,
      tier: "",
      subject: "all",
      paper: "both",
      /* ⊕ MRB-342 — THE SCOPE IS NOW A LIST, AND EVERY SCOPE OWNS ITS OWN
         COUNT, ITS OWN ROWS AND ITS OWN SWAPS. See `freshScope` below for
         why none of that can live on `S`. `si` is the slot the Topic step
         is currently answering for; on the ordinary one-topic path it is 0
         from open to close and nothing about the sheet changes. */
      scopes: [freshScope()],
      si: 0,
      shown: {},               // every question id shown this sheet SESSION
      busy: false,             // the SUBMIT gate; a preview's busy is per scope
      title: "",
      titleEdited: false,
      release: "now",          // 'now' | 'later'
      releaseDate: "",
      releaseTime: "07:00",
      dueDate: "",
      dueTime: "18:00",
      badTitle: false,
      badDue: false,
      badRelease: false,
      /* ⊕ MRB-336 — EDIT. Empty on a new set, which is what every branch
         below tests. `locked` is "this work has already been released", and
         the server enforces the same narrowing: after release only `title`
         and `due_at` are accepted, anything else is `locked_after_release`.
         `keepPicked` stops arriving at the Detail step from re-rolling
         questions the teacher never asked to change. */
      editId: "",
      locked: false,
      keepPicked: false,
      roTier: "",
      roScope: "",
      /* ⊕ Stream L, 25 Sep 2026 (experience run, item N11 / data safety) —
         a snapshot of `cur().picked` taken the moment `loadStoredQuestions`
         first fills it, before this session's own count changes and swaps
         touch it. `[]` on a fresh set, which has nothing to preserve.
         See `otherScopesFor`. */
      originalPicked: []
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

  /* ⊕ MRB-342.2 — THE ONE NOTE CONTROL, SHARED BY TWO DIFFERENT FIELDS.

     A worksheet download carries an ephemeral `note` (contract §2.1, printed
     on the file and nowhere else); a Set-work assignment carries a durable
     `teacher_note` (§3, saved with the row, read back by the pupil). Two
     different facts, two different POST bodies — but the same 300-character,
     plain-text control: a label, a `<textarea>` and a live count. Built once
     here so the counting rule can never drift between the two places it is
     drawn.

     ⚠️ CODE POINTS, NOT `.length`. Postgres `char_length()` counts
     characters; JS `String.prototype.length` counts UTF-16 code units, and
     the two disagree outside the BMP — 300 🧪 is `char_length` 300 (accepted)
     and `.length` 600. `Array.from(s).length` iterates by code point, which
     is what both the live counter and the client-side guard use below, so
     the number a teacher watches and the bound the server enforces agree on
     the same string. */
  var NOTE_MAX = 300;
  function codePointLen(s) {
    try { return Array.from(String(s || "")).length; }
    catch (e) { return String(s || "").length; }
  }

  /* Trim, and collapse every run of whitespace (space, tab, CR, LF) to one
     space — the same normalisation the server applies before its own length
     check (contract §2.1), so the count shown here is the count that will
     actually be billed against the 300-character bound rather than a raw
     keystroke count that can disagree with it. */
  function normaliseNote(raw) {
    return String(raw || "").replace(/[ \t\r\n\f\v]+/g, " ").trim();
  }

  /* Returns `{wrap, textarea, sync, value}`. `value()` returns the
     NORMALISED string, ready to post; the field is never disabled at
     NOTE_MAX — a teacher may keep typing, the count goes negative-styled via
     `.sw-note-over`, and the server is the one true bound (`bad_note`). */
  function buildNoteField(mark) {
    var wrap = el("div", "sw-note-field");
    wrap.setAttribute("data-sw", mark + "-field");
    wrap.appendChild(el("div", "sw-label", SAY.labelNote));
    var ta = document.createElement("textarea");
    ta.className = "sw-input sw-note-input";
    ta.rows = 2;
    ta.setAttribute("data-sw", mark);
    ta.setAttribute("aria-label", SAY.labelNote);
    var count = el("div", "sw-note-count", SAY.charsLeft(NOTE_MAX));
    count.setAttribute("data-sw", mark + "-count");
    wrap.appendChild(ta);
    wrap.appendChild(count);
    function sync() {
      var n = codePointLen(normaliseNote(ta.value));
      var left = NOTE_MAX - n;
      count.textContent = SAY.charsLeft(left);
      count.classList.toggle("sw-note-over", left < 0);
    }
    ta.addEventListener("input", sync);
    sync();
    return {
      wrap: wrap, textarea: ta, sync: sync,
      value: function () { return normaliseNote(ta.value); }
    };
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
    /* ⊕ MRB-342 — DOWNLOAD SITS BESIDE THE PRIMARY AND IS NOT THE PRIMARY.
       A worksheet is a thing a teacher takes away; setting work is a thing
       thirty children receive. They are next to each other because they are
       about the same composed set, and they are different weights because
       only one of them writes anything. Nothing about a download reaches
       `assignments`. */
    var dl = makeDownload({
      mark: "download",
      request: function (format, answers, mc) {
        return sheetWorksheet(format, answers, mc);
      }
    });
    head.appendChild(back); head.appendChild(step);
    head.appendChild(dl.node); head.appendChild(primary);

    var body = el("div", "sw-body");
    body.setAttribute("data-sw", "body");

    /* ── panel 0: Classes ── */
    var pClasses = el("div", "sw-panel");
    pClasses.setAttribute("data-sw", "panel-classes");
    pClasses.appendChild(el("div", "sw-label", SAY.labelClasses));
    var classList = el("div", "sw-tree");
    classList.setAttribute("data-sw", "class-list");
    pClasses.appendChild(classList);
    /* ⊕ MRB-335 — the scope's failure, on the step the teacher is standing
       on. The tree carries the same word one step further in; a teacher who
       cannot get past step 0 was never going to read that one. */
    var classNote = el("div", "sw-row-tag", SAY.unavailable);
    classNote.setAttribute("data-sw", "class-note");
    classNote.hidden = true;
    pClasses.appendChild(classNote);

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
    /* ⊕ first-week fixes (22 Sep 2026) — THE TREE PANEL'S OWN STATUS, AND IT IS A SIBLING OF THE
       TREE RATHER THAN A CHILD OF IT.

       `Next` now enables the moment a class is ticked (see `stepValid`), so a
       teacher can stand on this step before `/scope` has answered. Three
       things can be true here — in flight, answered, failed — and the panel
       has to say which, because an empty `sw-tree` reads as "this class has
       no topics" in all three.

       ⚠️ NOT WRITTEN INTO `els.tree`. `buildTree()` opens by emptying that
       node, and `loadScope`'s failure path used to append the `Unavailable`
       tag into it — so the two fought over one container and the note's
       lifetime was whatever happened last. Kept outside, the status is
       patched (hidden / shown, one of two words) and the tree is built, and
       neither touches the other. */
    var treeNote = el("div", "sw-row-tag", SAY.loading);
    treeNote.setAttribute("data-sw", "tree-note");
    treeNote.hidden = true;
    pTopic.appendChild(treeNote);
    /* Its own control, because a failed read must be RETRYABLE without
       closing the sheet. Hidden unless the read actually failed: a Retry over
       a tree that loaded is a control that does nothing. */
    var treeRetry = btn("sw-btn sw-add", SAY.retry);
    treeRetry.setAttribute("data-sw", "tree-retry");
    treeRetry.hidden = true;
    pTopic.appendChild(treeRetry);

    /* ── panel 2: Detail ── */
    var pDetail = el("div", "sw-panel");
    pDetail.setAttribute("data-sw", "panel-detail");

    /* ⊕ MRB-336 — WHAT A RELEASED SET SHOWS INSTEAD OF ITS CONTROLS.
       Its tier and its topic, as values, at the head of the panel — where
       the teacher would otherwise be reading the answers they had just
       given on the Topic step. Children have already been given this work;
       changing either would change the questions underneath a pupil who
       has started, so the server refuses it (`locked_after_release`) and
       the sheet does not offer it.

       ⚠️ ABSENT, NOT DISABLED. A greyed-out chip rail with a sentence
       under it explaining why it is grey is two things this sheet does not
       do — a dead control and a sentence. A value with a label above it is
       what "read-only" looks like here. */
    var roTierLbl = el("div", "sw-label", SAY.labelTier);
    roTierLbl.setAttribute("data-sw", "ro-tier-label");
    roTierLbl.hidden = true;
    var roTier = el("div", "sw-ro");
    roTier.setAttribute("data-sw", "ro-tier");
    roTier.hidden = true;
    var roScopeLbl = el("div", "sw-label", SAY.steps[1]);
    roScopeLbl.setAttribute("data-sw", "ro-scope-label");
    roScopeLbl.hidden = true;
    var roScope = el("div", "sw-ro");
    roScope.setAttribute("data-sw", "ro-scope");
    roScope.hidden = true;
    pDetail.appendChild(roTierLbl); pDetail.appendChild(roTier);
    pDetail.appendChild(roScopeLbl); pDetail.appendChild(roScope);

    /* ⊕ MRB-342 — THE QUESTIONS EYEBROW IS DRAWN ONCE, OVER ALL THE SCOPES.
       One topic keeps exactly the DOM it had: this label, a `count-chips`
       rail and a `qlist`, in that order, with the same `data-sw` marks. What
       changed is that the last two now live inside a `.sw-scope` section, and
       a second topic adds a SECOND section rather than replacing the first. */
    var qLbl = el("div", "sw-label", SAY.labelQuestions);
    qLbl.setAttribute("data-sw", "questions-label");
    pDetail.appendChild(qLbl);
    var scopesHost = el("div", "sw-scopes");
    scopesHost.setAttribute("data-sw", "scopes");
    pDetail.appendChild(scopesHost);
    /* Back to the Topic step for a further scope. Disabled — not hidden —
       when the set is already at the server's twenty, because "there is no
       room for another topic" is a fact about the set the teacher has
       composed and a control that vanishes states it as an absence. */
    var addTopic = btn("sw-btn sw-add", SAY.addTopic);
    addTopic.setAttribute("data-sw", "add-topic");
    pDetail.appendChild(addTopic);

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

    /* ⊕ MRB-342.2 §3.3 — HIDDEN UNTIL `/scope` NAMES THE CAPABILITY, AND
       HIDDEN IS THE OPENING STATE. `syncNoteVisibility()` is the only place
       that ever un-hides it, and it un-hides on exactly one signal:
       `S.scope.assignment_note === true` — not "truthy", `=== true`. An
       older backend, or a request still in flight, answers with the key
       absent; `undefined` must read as unsupported, never as "unknown, so
       show it and let the save fail". */
    var note = buildNoteField("assignment-note");
    note.wrap.hidden = true;
    pDetail.appendChild(note.wrap);

    var relLbl = el("div", "sw-label", SAY.labelRelease);
    pDetail.appendChild(relLbl);
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
      pClasses: pClasses, classList: classList, classNote: classNote,
      pTopic: pTopic, tierChips: tierChips,
      subjLabel: subjLabel, subjChips: subjChips,
      paperLabel: paperLabel, paperChips: paperChips, tree: tree,
      treeNote: treeNote, treeRetry: treeRetry,
      pDetail: pDetail,
      qLbl: qLbl, scopesHost: scopesHost, addTopic: addTopic, dl: dl,
      relLbl: relLbl,
      roTierLbl: roTierLbl, roTier: roTier,
      roScopeLbl: roScopeLbl, roScope: roScope,
      title: title, noteWrap: note.wrap, noteInput: note.textarea,
      noteSync: note.sync, noteValue: note.value,
      relChips: relChips, relFields: relFields,
      relDate: relDate, relTime: relTime, dueDate: dueDate, dueTime: dueTime,
      toast: toast,
      treeRows: [], classRows: []
    };

    wireShell();
  }

  var FOCUSABLE = "button,[href],input,select,textarea,[tabindex]";

  /* Everything inside the sheet a Tab could legitimately land on, in DOM
     order: visible, enabled, and not inside a panel that is `hidden`. */
  function focusables() {
    var all = els.sheet.querySelectorAll(FOCUSABLE), out = [];
    for (var i = 0; i < all.length; i++) {
      var n = all[i];
      if (n.disabled) { continue; }
      if (n.getAttribute("tabindex") === "-1") { continue; }
      if (!n.offsetParent && n !== els.sheet) { continue; }  // hidden subtree
      out.push(n);
    }
    return out;
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
      /* ⊕ MRB-342 — BACK OUT OF A SLOT THE TEACHER NEVER FILLED, AND IT IS
         THE ONLY WAY TO UNDO `Add topic`. Pressing Add topic appends an
         empty scope and comes here; pressing Back with it still empty must
         drop it and return to the Detail step, not walk the teacher down to
         the Classes step of a set they are in the middle of composing. */
      if (S.step === 1 && S.scopes.length > 1 && !cur().kind) {
        dropScope(S.si);
        S.step = 2;
        syncStep();
        return;
      }
      S.step -= 1;
      syncStep();
    });
    els.addTopic.addEventListener("click", function () {
      if (!S || els.addTopic.disabled) { return; }
      S.scopes.push(freshScope());
      S.si = S.scopes.length - 1;
      S.step = 1;
      syncStep();
      syncTree();
      syncTierChips();
    });
    /* ⊕ first-week fixes (22 Sep 2026) — the one control that makes a failed `/scope` recoverable.
       Guarded on `S.classId` because there is nothing to ask about without an
       anchor, and on `scopeLoading` so a double-press cannot start a second
       request whose answer would race the first. */
    els.treeRetry.addEventListener("click", function () {
      if (!S || !S.classId || S.scopeLoading) { return; }
      loadScope();
    });
    els.primary.addEventListener("click", onPrimary);
    els.title.addEventListener("input", function () {
      if (!S) { return; }
      S.title = els.title.value;
      S.titleEdited = true;
      S.badTitle = false;
      syncValidity();
    });
    /* ⊕ MRB-342.2 §3 — the assignment note. Read on demand from `els.noteInput`
       at submit time (`els.noteValue()`, already trimmed and whitespace-
       collapsed); this listener clears the outline a refused save left
       behind, the same shape as the title's, AND marks the field dirty —
       see `S.noteEdited` in `saveEdit()`, and `edit()`'s comment on
       `S.noteLoaded`, for why a keystroke here is the thing that makes a
       PATCH allowed to touch this column at all. */
    els.noteInput.addEventListener("input", function () {
      if (!S) { return; }
      S.badNote = false;
      S.noteEdited = true;
      syncValidity();
    });
    var dateTimeSync = function () {
      if (!S) { return; }
      S.releaseDate = els.relDate.value;
      S.releaseTime = els.relTime.value;
      S.dueDate = els.dueDate.value;
      S.dueTime = els.dueTime.value;
      S.badDue = false; S.badRelease = false;
      syncValidity();
    };
    [els.relDate, els.relTime, els.dueDate, els.dueTime].forEach(function (i) {
      i.addEventListener("input", dateTimeSync);
      i.addEventListener("change", dateTimeSync);
    });
    document.addEventListener("keydown", function (e) {
      if (!S) { return; }
      if (e.key === "Escape") { close(); return; }
      /* ⊕ MRB-335 — TAB STAYS INSIDE THE SHEET.

         The overlay is `position:fixed; inset:0` and the page behind it is
         still in the tab order, so Tab walked out of a modal dialog and
         down a class list nobody could see or click — `aria-modal="true"`
         is a promise to assistive technology that the browser does not
         keep on its own.

         The list is read at the moment of the press rather than cached: the
         sheet's controls change with every step, and a cached ring would
         send Tab to a node that is now `hidden`. */
      if (e.key !== "Tab") { return; }
      var items = focusables();
      if (!items.length) { return; }
      var first = items[0], last = items[items.length - 1];
      var here = document.activeElement;
      if (e.shiftKey && (here === first || !els.sheet.contains(here))) {
        e.preventDefault(); last.focus();
      } else if (!e.shiftKey && (here === last || !els.sheet.contains(here))) {
        e.preventDefault(); first.focus();
      }
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
      // ⊕ Stream M, 25 Sep 2026 (experience run round 3, N8) — every chip
      // this sheet builds is a toggle (Now/Later, tier, subject, paper,
      // the count quick-picks…) and selection was shown by the `is-on`
      // CLASS alone, with nothing in the accessibility tree saying which
      // one — or that they are toggles at all. `aria-pressed` starts false
      // here and `syncChips` below keeps it in step with `is-on` on every
      // sync, the same call that already toggles the class.
      b.setAttribute("aria-pressed", "false");
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
      var on = String(c.key) === String(active);
      c.node.classList.toggle("is-on", on);
      c.node.setAttribute("aria-pressed", on ? "true" : "false");
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
      /* ⊕ MRB-342 — EVERY SCOPE IN THE SET IS TINTED, not only the slot the
         teacher is answering for. Coming back to the Topic step to add a
         third topic and seeing no mark on the two already chosen would be
         the sheet forgetting them on screen while still holding them. */
      var on = scopeHolding(r.kind, r.ref) !== null;
      r.row.classList.toggle("is-on", on);
      /* ⊕ MRB-335 — the class rows have carried this since they were drawn;
         the tree rows are the same kind of control (a toggle whose state is
         a tint) and were announcing nothing at all. Screen-reader users
         could not tell a chosen topic from an unchosen one. */
      r.row.setAttribute("aria-pressed", on ? "true" : "false");
      /* A zero-count row is shown with its `0` and refuses to be picked. */
      r.row.setAttribute("aria-disabled", n > 0 ? "false" : "true");
      if (r.kind === "topic") {
        r.wrap.hidden = !topicVisible(r.data);
      }
    });
    /* A filter that hides the chosen topic clears the choice rather than
       leaving Next live over a row nobody can see.

       ⚠️ THE CURRENT SLOT ONLY. A subject chip narrowing the tree says
       nothing about a topic the teacher already committed two steps ago;
       clearing those would delete part of the set as a side effect of a
       filter. */
    var sc = cur();
    var sel = nodeFor(sc.kind, sc.ref);
    if (sel) {
      var top = (sel.kind === "topic") ? sel : sel.parent;
      if (top && top.wrap.hidden) { sc.kind = ""; sc.ref = ""; }
    }
    els.tree.classList.remove("sw-bad");
  }

  /* The scope holding this node, or null. ⊕ MRB-342. */
  function scopeHolding(kind, ref) {
    for (var i = 0; i < S.scopes.length; i++) {
      var sc = S.scopes[i];
      if (sc.kind === kind && sc.ref === ref) { return sc; }
    }
    return null;
  }

  /* Drop a slot and leave `si` pointing at something real. */
  function dropScope(i) {
    if (S.scopes.length < 2) { return; }
    var sc = S.scopes[i];
    if (sc && sc.els && sc.els.wrap && sc.els.wrap.parentNode) {
      sc.els.wrap.parentNode.removeChild(sc.els.wrap);
    }
    S.scopes.splice(i, 1);
    if (S.si >= S.scopes.length) { S.si = S.scopes.length - 1; }
    syncScopes();
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
    var sc = cur();
    var held = scopeHolding(kind, ref);
    /* ⊕ MRB-342 — A NODE ALREADY IN THE SET IS NOT PICKED TWICE.

       If it belongs to ANOTHER slot the tap is ignored: the topic is already
       in the set, and moving it into this slot would leave the other one
       empty without saying so. If it belongs to THIS slot the tap is a
       deselect — which is how a scope is taken back out, and it is why there
       is no Remove button and no word for one.

       ⚠️ THE DESELECT ONLY EXISTS ONCE THERE ARE TWO SCOPES. On the ordinary
       one-topic path a second tap on the chosen row still re-picks it,
       byte for byte as before, so nothing that presses this sheet today
       meets a behaviour it has not met. */
    if (held && held !== sc) { return; }
    if (held === sc && S.scopes.length > 1) {
      sc.kind = ""; sc.ref = "";
      resetScopeQuestions(sc);
      syncTree();
      /* ⚠️ THE TIER RAIL FOLLOWS THE SELECTION, NOT THE STEP. Measured: the
         lock is a fact about how many scopes are FILLED, and filling one
         happens here — so syncing it only in `addTopic` left the other tier
         live on the step where a teacher would actually press it, and the
         lock appeared a step later, after the damage. */
      syncTierChips();
      syncValidity();
      return;
    }
    /* Selecting a subtopic deselects its topic and vice versa — one node per
       scope. */
    sc.kind = kind;
    sc.ref = ref;
    S.keepPicked = false;              // ⊕ MRB-336
    resetScopeQuestions(sc);
    if (!S.titleEdited) { S.title = autoTitle(); els.title.value = S.title; }
    syncTree();
    /* The lock is a fact about how many scopes are FILLED, and this is where
       one gets filled. Syncing the rail only in the `Add topic` handler left
       the other tier live on the step a teacher would actually press it on,
       and the lock appeared one step later — after the damage. */
    syncTierChips();
    syncValidity();
  }

  function resetScopeQuestions(sc) {
    sc.picked = [];
    sc.expanded = {};
    sc.swapDead = {};
    sc.swapNote = {};
    sc.previewErr = false;
    sc.available = 0;
    /* ⊕ MRB-342.2 — a clamp note is about the node/tier just left; it does
       not survive a topic or tier change (a stale "Only 8 at Higher" left
       showing under a freshly-picked topic that has never been asked about
       would be a lie about the wrong node). */
    sc.cappedBy = null;
    sc.capNote = null;
  }

  function nodeFor(kind, ref) {
    for (var i = 0; i < els.treeRows.length; i++) {
      var r = els.treeRows[i];
      if (r.kind === kind && r.ref === ref) { return r; }
    }
    return null;
  }

  /* ⊕ MRB-335 — THE SUBJECT OF THE CHOSEN SCOPE, and it is not decoration.
     `atomic-structure` is a topic id in BOTH chemistry and physics, so on a
     combined class the server cannot resolve a topic by id alone: it would
     have to guess, and half its guesses would hand a chemistry class the
     physics tree. The tree row already carries the answer.

     A subtopic takes its parent topic's subject — a subtopic id is unique
     today, but sending it costs nothing and means the server never has two
     resolution paths to keep in step. */
  function subjectParam(sc) {
    var subj = subjectOfScope(sc);
    return subj ? ("&subject=" + encodeURIComponent(subj)) : "";
  }

  function subjectOfScope(sc) {
    var s = sc || cur();
    var r = nodeFor(s.kind, s.ref);
    if (!r) { return ""; }
    var top = (r.kind === "topic") ? r : r.parent;
    return (top && top.data && top.data.subject) ? String(top.data.subject) : "";
  }

  /* The name of one scope's node, as the teacher reads it in the tree. It is
     DATA — a topic name — so it is drawn in `.sw-scope-name` and never in a
     `.sw-label`, which is chrome and is swept against the allowed words. */
  function scopeName(sc) {
    var r = nodeFor(sc.kind, sc.ref);
    if (!r) { return ""; }
    if (r.kind === "topic") { return String(r.data.name || ""); }
    var parent = r.parent ? String(r.parent.data.name || "") : "";
    var own = String(r.data.name || "");
    return parent ? parent + " · " + own : own;
  }

  /* ⊕ Stream L, 25 Sep 2026 (experience run, item N11 / data safety) — EVERY
     OTHER TOPIC A MULTI-SCOPE SET HOLDS, RECONSTRUCTED FROM ITS OWN
     QUESTIONS, TO BE SENT BACK UNCHANGED.

     ⛔ THE DEFECT THIS CLOSES. `edit()` gives an edit exactly ONE scope
     (`S.scopes[0]`, `Add topic` hidden throughout — MRB-342's own rule,
     because `assignments` stores one scope and `PATCH` used to accept one).
     `loadStoredQuestions` therefore poured EVERY question the set holds —
     Energy's and Forces', on a set made of both — into that one scope's
     `.picked`, under Energy's own heading. A teacher who changed the count
     or swapped a question redrew from ENERGY'S pool only; the payload
     `saveEdit` built then carried Energy's ids and nothing of Forces', and
     the PATCH route replaces `assignment_questions` with exactly the ids it
     is sent (see its own comment, "REPLACED WHENEVER THE BODY SENT
     QUESTIONS"). Forces was not merely hidden from the sheet — pressing
     Save deleted it from the database.

     ⚠️ THE BACKEND ALREADY TAKES THE FIX; ONLY THE SHEET DID NOT USE IT.
     `PATCH /api/teacher/set-work/:id` has accepted `scopes: [{scope_kind,
     scope_ref, subject?, question_ids}, …]` since MRB-342's follow-up
     (22 Sep 2026) — the honest mirror of the POST's own field, each scope
     sealed against its own pool, no union taken. Nothing here is a backend
     change; this is the sheet finally sending what the route has been able
     to read all along.

     ⚠️ A SUBTOPIC UNDER THE SAME TOPIC AS THE HEAD IS NOT "OTHER". A
     topic-level scope's own questions legitimately span several of that
     topic's subtopics — that is ordinary, single-scope behaviour, and
     splitting it into one manufactured scope per subtopic would change
     what the set is filed as without the teacher asking for that. Only a
     slug that does NOT belong under the head topic — or does not match
     the head's own ref, when the head IS a subtopic — is "other". Resolved
     against `els.treeRows`, the same tree `nodeFor`/`scopeName` read.

     ⚠️ AND NO ID IS EVER SENT TWICE. `headIds` — the head scope's CURRENT,
     possibly just-changed picks — wins any overlap; an "other" group is
     filtered down to whatever it has left and dropped if that empties it.
     This is what keeps a save correct even in the pathological case where
     the class's tree has not finished loading yet (`nodeFor` resolves
     nothing, so every slug reads as "other") — it can only ever result in
     a topic being filed as several small subtopic scopes instead of one,
     never in a duplicate id the server would refuse, and never in a
     dropped one. */
  function otherScopesFor(headScope, headIds) {
    var picked = S.originalPicked || [];
    if (!picked.length) { return []; }
    var byLesson = {}, order = [];
    picked.forEach(function (q) {
      if (!q.lesson) { return; }
      if (!byLesson[q.lesson]) { byLesson[q.lesson] = []; order.push(q.lesson); }
      byLesson[q.lesson].push(q.id);
    });
    var headSet = {};
    headIds.forEach(function (id) { headSet[id] = true; });
    var out = [];
    order.forEach(function (slug) {
      if (headScope.kind === "subtopic") {
        if (slug === headScope.ref) { return; }        // the head's own subtopic
      } else if (headScope.kind === "topic") {
        var r = nodeFor("subtopic", slug);
        var parentRef = r && r.parent ? r.parent.ref : null;
        if (parentRef === headScope.ref) { return; }    // a subtopic of the head topic
      }
      var ids = byLesson[slug].filter(function (id) { return !headSet[id]; });
      if (!ids.length) { return; }
      out.push({ scope_kind: "subtopic", scope_ref: slug,
                 subject: subjectOfScope({ kind: "subtopic", ref: slug }) || null,
                 question_ids: ids });
    });
    return out;
  }

  /* ⊕ Stream L, 25 Sep 2026 (experience run, item 25/8) — THE TITLE NAMES
     EVERY TOPIC, JOINED, NOT JUST THE FIRST.

     ⛔ WHAT THIS REPLACES. MRB-342 made the title the FIRST scope's name,
     unconditionally — reasoned as avoiding "a composed sentence in a sheet
     that does not write them", and worried about the 80-character field on
     a third topic. That reasoning held for a SENTENCE ("Energy, and also
     Forces, and also…"); it does not hold for a short join. A two-topic
     set titled "Energy" when it is Energy AND Forces is not a a sentence
     problem — it is the wrong noun, on the sheet's own default AND on
     every worksheet download that inherits it, which named its file
     "Energy.pdf" for a document that opens on a Forces question (the
     audit's item 25).

     Joining with " · " — is already Design's own separator for a
     topic-and-subtopic pair (`scopeName` uses it two lines below) — reads
     wrong for two DIFFERENT topics, so " + " is used instead, matching the
     wording the experience-run brief itself gives ("Energy + Forces"). The
     80-character cap is UNCHANGED and still the backstop for a teacher who
     picks several topics with long names; the teacher may still type
     whatever they like over any of this, exactly as before. */
  function autoTitle() {
    var scopes = filledScopes();
    if (!scopes.length) { scopes = [cur()]; }
    var names = scopes.map(scopeName).filter(function (n) { return !!n; });
    return names.join(" + ").slice(0, 80);
  }

  /* ═════════════════════════════════════════════════════════════════════
     10. THE CLASS LIST — only cohort matches (RISKS C4).
     ═════════════════════════════════════════════════════════════════════ */

  /* ⊕ MRB-335 — THE ROWS COME FROM THE PAGE FIRST AND THE SERVER SECOND.

     `/scope` needs a class before it can answer, so on the classes screen —
     where there is no class — the old code drew an empty step 0 and a dead
     Next. The list of classes a teacher may set work to is already on the
     page: `teacher-live.js` computes `SET_WORK_CLASSES` for exactly this,
     and its comment says why it is its own key rather than the render list
     ("which classes are on screen" and "which classes may be written to"
     are different questions).

     ⚠️ THE PAGE'S LIST IS NOT AUTHORITY ON THE COHORT and is never treated
     as one. It says which classes exist; `/scope` says which of them share
     this one's `(key_stage, science_pathway, science_subject)`, and the
     server refuses a mismatch with `cohort_mismatch` whatever this draws.
     What the page's copy buys is a step 0 that is drawn before the first
     request instead of after it. */
  function pagePool() {
    var d = window.__MRB_DATA__;
    var raw = (d && d.SET_WORK_CLASSES) || [];
    var out = [];
    for (var i = 0; i < raw.length; i++) {
      var c = raw[i];
      if (!c || !c.id) { continue; }
      out.push({ id: String(c.id), name: String(c.code || c.name || ""),
                 pupils: Number(c.n != null ? c.n : c.pupils) || 0 });
    }
    return out;
  }

  /* The cohort, when `/scope` has answered, else the page's list, else the
     anchor alone — so there is always something to draw. */
  function classPoolNow() {
    var coh = S.scope && S.scope.cohort_classes;
    var page = pagePool();
    if (page.length) { return page; }
    if (coh && coh.length) {
      return coh.map(function (c) {
        return { id: String(c.id), name: String(c.name || ""),
                 pupils: Number(c.pupils) || 0 };
      });
    }
    return S.classId ? [{ id: S.classId, name: "", pupils: 0 }] : [];
  }

  function buildClasses() {
    els.classList.textContent = "";
    els.classRows = [];
    S.classPool = classPoolNow();
    S.classPool.forEach(function (c) {
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
        if (row.getAttribute("aria-disabled") === "true") { return; }
        var i = S.classes.indexOf(rec.id);
        if (i > -1) { S.classes.splice(i, 1); } else { S.classes.push(rec.id); }
        /* ⊕ MRB-335 — THE FIRST TAP ANCHORS, and the anchor is what every
           later request is scoped by. Unanchored, `/scope` has not been
           asked for anything; this is the moment there is something to ask
           about. */
        if (!S.classId && S.classes.length) {
          S.classId = S.classes[0];
          els.overlay.setAttribute("data-sw-class", S.classId);
          syncClasses();
          syncValidity();
          loadScope();
          return;
        }
        /* Unticking the last one un-anchors: the cohort was a fact about a
           class nobody has chosen any more, and leaving the other rows
           disabled behind it would strand the teacher on a step with
           nothing selectable. */
        if (S.classId && !S.classes.length && !isAnchoredOpen) {
          S.classId = "";
          S.scope = null;
          S.cohortIds = null;
          /* Cleared, so the next tap is a real retry rather than a repaint
             of the last failure. */
          S.scopeErr = false;
          /* ⊕ first-week fixes (22 Sep 2026) — AND THE IN-FLIGHT FLAG, AND `fetchSeq` WITH IT.
             Un-anchoring while a `/scope` is still on the wire must not leave
             the panel saying `Loading` for a class nobody has chosen, and the
             answer that is still coming must not be allowed to paint a tree
             over it. Bumping `fetchSeq` makes that answer stale by
             construction — the same instrument `open()` uses on `session`. */
          S.scopeLoading = false;
          fetchSeq += 1;
          els.classNote.hidden = true;
          els.overlay.setAttribute("data-sw-class", "");
          els.tree.textContent = "";
          els.treeRows = [];
          syncClasses();
          syncScopePanel();
          syncValidity();
          return;
        }
        syncClasses();
        syncValidity();
      });
    });
    syncClasses();
  }

  /* ⊕ MRB-335 — REBUILT ONLY WHEN THE LIST ITSELF CHANGED.

     `/scope` lands AFTER the teacher has tapped a row — that tap is what
     asked for it — so an unconditional `buildClasses()` in its handler
     destroys every row including the one under their thumb, and replaces it
     with a fresh node. That is the replace-the-node-you-are-touching mistake
     this whole sheet exists to stop (see the header), one step earlier than
     where it was found the first time.

     The pool almost never changes: the page's `SET_WORK_CLASSES` and the
     cohort are drawn from the same classes, so the ordinary case is a patch
     and the rebuild is reserved for a list that is genuinely different. */
  function refreshClasses() {
    var want = classPoolNow().map(function (c) { return c.id; }).join(",");
    var have = els.classRows.map(function (r) { return r.id; }).join(",");
    if (want !== have) { buildClasses(); return; }
    S.classPool = classPoolNow();
    syncClasses();
  }

  function syncClasses() {
    els.classRows.forEach(function (r) {
      var on = S.classes.indexOf(r.id) > -1;
      /* Outside the anchor's cohort: shown, and not selectable. A teacher
         planning a term needs to see that 8r/Sc1 exists and cannot be set
         the same work as 10a/Bi1; hiding it would answer that with a
         silence. Same treatment, same reason, as a zero-count topic. */
      var out = !!(S.cohortIds && !S.cohortIds[r.id]);
      r.node.setAttribute("aria-disabled", out ? "true" : "false");
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

  /* ⊕ MRB-342 — A SCOPE'S SECTION, AND WHY EACH ONE IS ITS OWN SUBTREE.

     The patching rule in this file's header — "the question DOM is built
     ONCE PER DATA LOAD" — has to be read per SCOPE once there can be more
     than one. A preview landing for the second topic must not touch the
     first topic's rows: the teacher may be reading them, and rebuilding the
     list they are scrolled into is the exact defect this whole module was
     written to remove, one topic further along.

     So a scope owns a `.sw-scope` wrapper for its whole life and only the
     `qlist` inside it is refilled. The `data-sw` marks are Design's and the
     drive's existing ones — `count-chips`, `qlist`, `question`, `stem`,
     `swap` — so a single-topic sheet is the same DOM it was before, with one
     wrapper around the part that can now repeat. */
  function buildScopeSection(sc) {
    var wrap = el("div", "sw-scope");
    wrap.setAttribute("data-sw", "scope");
    var name = el("div", "sw-scope-name", "");
    name.setAttribute("data-sw", "scope-name");
    var chips = el("div", "sw-chips");
    chips.setAttribute("data-sw", "count-chips");
    /* ⊕ MRB-342.2 §1 — the number field beside the quick picks. `type=number,
       min=1` gives a phone a numeric keypad and a desktop the native
       steppers; `max` is set from `maxPerScope()` in `syncCountChips`, never
       hand-typed here, because the ceiling is the server's own answer and
       this file must not carry a second copy of it that could drift. */
    var countCustom = el("div", "sw-count-custom");
    countCustom.setAttribute("data-sw", "count-custom");
    var countInput = document.createElement("input");
    countInput.type = "number";
    countInput.min = "1";
    countInput.step = "1";
    countInput.className = "sw-input sw-count-input";
    countInput.setAttribute("data-sw", "count-input");
    countInput.setAttribute("aria-label", SAY.labelQuestions);
    countCustom.appendChild(countInput);
    /* The clamp note — RISKS A9's two ruled sentences (contract §1.3),
       hidden except while one of them applies to this scope. */
    var countNote = el("div", "sw-row-tag", "");
    countNote.setAttribute("data-sw", "count-note");
    countNote.hidden = true;
    var qlist = el("div", "sw-qlist");
    qlist.setAttribute("data-sw", "qlist");
    wrap.appendChild(name); wrap.appendChild(chips);
    wrap.appendChild(countCustom); wrap.appendChild(countNote);
    wrap.appendChild(qlist);
    els.scopesHost.appendChild(wrap);
    sc.els = { wrap: wrap, name: name, chips: chips, qlist: qlist,
               countList: null, countInput: countInput, countNote: countNote,
               qRows: [] };
    buildCountChips(sc);
    wireCountInput(sc);
    return sc.els;
  }

  /* Sections in, sections out, names and chips patched. BUILDS ONLY WHAT IS
     MISSING — an existing section is never replaced, for the reason above. */
  function syncScopes() {
    var list = filledScopes();
    /* An abandoned slot draws nothing: the teacher pressed Add topic, picked
       nothing, and came back. */
    S.scopes.forEach(function (sc) {
      if (sc.els && list.indexOf(sc) < 0) {
        if (sc.els.wrap.parentNode) {
          sc.els.wrap.parentNode.removeChild(sc.els.wrap);
        }
        sc.els = null;
      }
    });
    list.forEach(function (sc) {
      if (!sc.els) { buildScopeSection(sc); }
      sc.els.wrap.setAttribute("data-sw-ref", sc.ref);
      sc.els.name.textContent = scopeName(sc);
      /* One topic needs no heading — the Questions eyebrow above it and the
         Title field below it both already name it. Two topics need to say
         which rows belong to which. */
      sc.els.name.hidden = (list.length < 2);
      sc.els.chips.hidden = !!S.locked;
      sc.els.qlist.classList.toggle("is-ro", !!S.locked);
      syncCountChips(sc);
    });
    /* ⚠️ NOT OFFERED ON AN EDIT. A row in `assignments` carries ONE scope
       triple, and `PATCH /api/teacher/set-work/:id` takes one; a second
       topic added to an existing set would have nowhere to be written. */
    els.addTopic.hidden = !!S.editId;
    /* ⊕ first-week fixes (22 Sep 2026) — THE CEILING ON A SET IS ITS NUMBER OF TOPICS, and this is
       the control that wears it.

       ⛔ It read `pickedTotal() >= MAX_QUESTIONS`: once the teacher's topics
       added up to twenty questions there was no room for another topic. That
       was the whole-set ceiling in its last and most reasonable-looking
       place — and it was the same mistake, because a further topic does not
       take questions away from the ones already chosen. The set route accepts
       `MAX_SCOPES` scopes of twenty, so this is the number that is true. */
    els.addTopic.disabled = !S.scope || anyBusy() ||
      filledScopes().length >= MAX_SCOPES;
  }

  function anyBusy() {
    for (var i = 0; i < S.scopes.length; i++) {
      if (S.scopes[i].busy) { return true; }
    }
    return false;
  }

  function anyPreviewErr() {
    var list = filledScopes();
    for (var i = 0; i < list.length; i++) {
      if (list[i].previewErr) { return true; }
    }
    return false;
  }

  function buildQuestions(sc) {
    if (!sc.els) { return; }
    sc.els.qlist.textContent = "";
    sc.els.qRows = [];
    sc.picked.forEach(function (q, i) {
      sc.els.qlist.appendChild(buildQuestionRow(sc, q, i));
    });
  }

  /* ⊕ MRB-352 run 2 (landing) — THE SHEET DRAWS A QUESTION'S FIGURE.

     The backend's three Set work seals were lifted in run 2: a question
     carrying a `figure` id is now offerable, because the pupil's page and the
     worksheet both draw it. This sheet was the one surface still showing a
     teacher "Look at the diagram…" with no diagram (figure-contract §5 lists
     it: "same manifest, loaded by shared/set-work.js"), and
     set_work_drive's old `preview_no_figures` check was red on exactly that.

     ⚠️ THE ONLY innerHTML SINK IN THIS FILE, and it is fed EXCLUSIVELY from
     `window.MRBFigures` — build-time output of `build_figures.py`, the same
     manifest the pupil's page reads. A question's own stem and options stay
     on `setFormula`'s text path; nothing here ever looks at them.

     ⚠️ THE MANIFEST IS LOADED STAMPED OR NOT AT ALL. `/shared/*` is served
     `immutable` for a year, so the `?v=` comes from `window.__MRB_ASSET_V__`
     (build_teacher_port.STAMPED_DEPS names both manifests). With no stamp the
     sheet draws no figure — a worse preview, never a year-long pin.

     An id the manifest does not carry draws nothing and never throws, the
     same rule `shared/student-runtime.js`'s "fig" node keeps. */
  var figureLoads = {};
  function loadFigures(keyStage) {
    var name = (keyStage === "KS4") ? "figures-ks4.js" : "figures-ks3.js";
    if (figureLoads[name]) { return figureLoads[name]; }
    var map = window.__MRB_ASSET_V__;
    var v = map && map[name];
    if (!v) {
      figureLoads[name] = Promise.resolve(false);
      return figureLoads[name];
    }
    figureLoads[name] = new Promise(function (resolve) {
      var s = document.createElement("script");
      s.src = "/shared/" + name + "?v=" + v;
      s.onload = function () { resolve(true); };
      s.onerror = function () { resolve(false); };
      document.head.appendChild(s);
    });
    return figureLoads[name];
  }

  function drawFigure(body, q) {
    var id = q && q.figure;
    var figs = window.MRBFigures;
    var rec = (id && typeof id === "string" && figs) ? figs[id] : null;
    if (!rec || typeof rec.svg !== "string") { return; }
    var wrap = el("div", "sw-q-fig");
    wrap.setAttribute("data-sw", "figure");
    wrap.setAttribute("data-sw-figure", id);
    wrap.innerHTML = rec.svg;
    var svg = wrap.firstElementChild;
    if (svg && rec.w) { svg.style.maxWidth = rec.w + "px"; }
    body.appendChild(wrap);
  }

  /* The manifest can land after the rows are built (it is fetched alongside
     `/scope`, not before it). Redraw each row's body in place — the same
     nodes, so an expanded row stays expanded and the scroller does not move. */
  function redrawFigures() {
    if (!S || !S.scopes) { return; }
    S.scopes.forEach(function (sc) {
      ((sc.els && sc.els.qRows) || []).forEach(function (rec) {
        var q = sc.picked[rec.i];
        if (q && q.figure) { fillOptions(rec.body, q); }
      });
    });
  }

  function buildQuestionRow(sc, q, i) {
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

    /* ⊕ MRB-342.2 §1.4 — a used-up Swap goes to a SETTLED state, not a dead
       button with nothing said. Same `.sw-row-tag` idiom the tree and the
       topic panel already use for a status line; hidden until `doSwap`'s
       204 sets it. */
    var swapNote = el("div", "sw-row-tag", SAY.swapExhausted);
    swapNote.setAttribute("data-sw", "swap-note");
    swapNote.hidden = true;

    var body = el("div", "sw-q-body");
    body.hidden = true;
    body.setAttribute("data-sw", "options");
    fillOptions(body, q);

    wrap.appendChild(head); wrap.appendChild(swapNote); wrap.appendChild(body);

    var rec = { sc: sc, i: i, wrap: wrap, stem: stem, body: body, swap: swap,
                swapNote: swapNote };
    sc.els.qRows.push(rec);

    stem.addEventListener("click", function () { toggleQ(rec); });
    swap.addEventListener("click", function () { doSwap(rec); });
    return wrap;
  }

  function fillOptions(body, q) {
    body.textContent = "";
    drawFigure(body, q);
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
    rec.sc.expanded[rec.i] = !open;
  }

  /* ⚠️ SWAP REPLACES THE ROW'S TEXT, NEVER THE ROW. `exclude` is everything
     picked PLUS everything shown at any point this sheet session, so a swap
     can never hand back a question the teacher has already read and
     rejected (RISKS A6). A 204 means the pool is spent for this scope and
     tier, and that row's Swap goes dead rather than lying.

     ⊕ MRB-342 — `exclude` IS STILL THE WHOLE SHEET'S SHOWN-SET, ACROSS
     SCOPES. Two topics can hold the same subtopic's questions at KS4, and a
     worksheet with the same question twice under two headings is worse than
     one short of it. */
  function doSwap(rec) {
    var sc = rec.sc;
    if (rec.swap.disabled || S.busy) { return; }
    var exclude = Object.keys(S.shown);
    S.scopes.forEach(function (other) {
      other.picked.forEach(function (p) {
        if (exclude.indexOf(String(p.id)) < 0) { exclude.push(String(p.id)); }
      });
    });
    rec.swap.disabled = true;
    var mySession = session, mySeq = fetchSeq, myScopeSeq = sc.seq;
    apiGet("/api/teacher/set-work/swap?class_id=" + encodeURIComponent(S.classId) +
      "&tier=" + encodeURIComponent(S.tier) +
      "&scope_kind=" + encodeURIComponent(sc.kind) +
      "&scope_ref=" + encodeURIComponent(sc.ref) +
      subjectParam(sc) +
      "&exclude=" + encodeURIComponent(exclude.join(","))
    ).then(function (r) {
      /* ⊕ MRB-335 — `fetchSeq` IS CHECKED, AND THE COMMENT THAT SAID IT
         MUST NOT BE WAS WRONG ABOUT WHICH COUNTER SEPARATES THE TWO CASES.

         It read: "`fetchSeq` is deliberately NOT checked: two swaps on two
         rows are both legitimate at once." The first half of that is true
         and is PRESERVED — a swap READS the counters and never bumps one, so
         two swaps in flight on two rows still both land.

         What it missed is the other thing that can happen while a swap is
         in flight: a RE-PREVIEW. Tap a count chip, or go Back to the topic
         step, change tier and come forward again, and `loadPreview` replaces
         that scope's `picked` wholesale. The old swap then resolved into the
         NEW array at `rec.i` and wrote its stem into `rec.stem`, a node
         `buildQuestions` had already detached. So the teacher saw the row
         they were looking at unchanged, and `submit()` sent a question that
         had never been on their screen — which is the one thing this sheet
         exists to make impossible.

         ⊕ MRB-342 — AND IT IS THE SCOPE'S OWN `seq` THAT ANSWERS IT NOW.
         `fetchSeq` belongs to `/scope` alone, because two scopes' previews
         are two legitimate requests at once and a global bump would make
         the second one kill the first's rows. Both counters are captured,
         not incremented. */
      if (!S || mySession !== session || mySeq !== fetchSeq ||
          myScopeSeq !== sc.seq) { return; }
      if (r.status === 204 || !r.body || !r.body.id) {
        sc.swapDead[rec.i] = true;
        sc.swapNote[rec.i] = true;
        if (rec.swapNote) { rec.swapNote.hidden = false; }
        return;                              // stays disabled, and says why
      }
      var q = r.body;
      S.shown[String(q.id)] = true;
      sc.picked[rec.i] = q;
      setFormula(rec.stem, q.stem);
      fillOptions(rec.body, q);
      rec.swap.disabled = false;
    }, function () {
      if (!S || mySession !== session || mySeq !== fetchSeq ||
          myScopeSeq !== sc.seq) { return; }
      rec.swap.disabled = false;
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     12. FETCHES
     ═════════════════════════════════════════════════════════════════════ */

  /* ⊕ first-week fixes (22 Sep 2026) — THE TOPIC PANEL SAYS WHICH OF THE THREE THINGS IS TRUE, AND
     IT IS PATCHED IN PLACE.

     Reported by Mide after his first week: after selecting a class, `Next`
     stayed grey for a noticeable time and sometimes needed the class toggling
     off and on to wake up. `stepValid` for step 0 read
     `!!(S.scope || S.scopeErr)` — Next waited for `/scope` to SETTLE — and
     `loadScope` only called `syncValidity()` on its success and failure paths,
     never on the discarded-stale-response path and never at all if the request
     simply hung. Toggling the class off and on re-anchored and re-fetched, and
     the second answer arrived; that is the whole of why the workaround worked.

     Ruled: step 0 is valid when ≥1 class is selected, full stop. Which moves
     the problem here — the Topic step is now reachable before the tree exists,
     so this function is what makes that honest:

        loading  the chip rails and the tree are empty and `Loading` says so
        ready    the tree is built and the note and Retry are gone
        error    `Unavailable`, and a `Retry` that asks again in place

     `data-sw-scope-state` on the overlay carries the same word, counted onto
     the node the way `data-sw-opens` is, so a drive reads a state instead of
     inferring one from an empty container.

     ⚠️ IT REBUILDS NOTHING. Same reason as `syncTree` and `refreshClasses`:
     the teacher may be scrolled into this panel when `/scope` lands. */
  function syncScopePanel() {
    if (!S || !els) { return; }
    var state = S.scope ? "ready" : (S.scopeErr ? "error" : (S.scopeLoading ? "loading" : "idle"));
    els.overlay.setAttribute("data-sw-scope-state", state);
    var note = (state === "loading") ? SAY.loading
             : ((state === "error") ? SAY.unavailable : "");
    els.treeNote.textContent = note;
    els.treeNote.hidden = !note;
    els.treeRetry.hidden = (state !== "error");
    els.treeRetry.disabled = !!S.scopeLoading;
    /* ⚠️ THE CHIP RAILS ARE DELIBERATELY NOT TOUCHED. An unbuilt `.sw-chips`
       is an empty div and draws nothing, so hiding it would change no pixel
       and would add a fourth thing this function owns — and `buildSubjectChips`
       and `buildPaperChips` already own their own labels' visibility, for the
       different reason that a separate-sciences class HAS no subject chips.
       Two owners of one `hidden` is the bug this note exists to prevent. */
  }

  /* ⊕ MRB-342.2 §3.3 — the ONLY signal, and it is read strictly.
     `S.scope.assignment_note === true`, never a truthiness check: `undefined`
     (an older backend, or before `/scope` has answered) and `false` (a
     newer backend whose column is not on this database yet) both hide the
     field, and both are the CORRECT reading — "absent" is treated as FALSE,
     never as "unknown, so show it and let the save silently drop the note"
     (contract's own instruction, given the column is only present on TEST
     right now and the backend lane's half is not yet deployed here). */
  function syncNoteVisibility() {
    if (!els) { return; }
    var supported = !!(S && S.scope && S.scope.assignment_note === true);
    els.noteWrap.hidden = !supported;
  }

  function loadScope() {
    S.scopeErr = false;
    S.scopeLoading = true;
    els.classNote.hidden = true;
    syncScopePanel();
    var mySession = session, mySeq = ++fetchSeq;
    /* ⚠️ `syncValidity()` IS CALLED ON EVERY PATH OUT OF HERE, INCLUDING THE
       STALE ONE. The stale path does NOT clear `scopeLoading` — that flag
       belongs to the newer fetch, which is still in flight — but it does
       resync, because the state it is reading may have moved for other
       reasons while it was away. Under the new `stepValid` no path out of
       this function can leave `Next` grey on step 0 anyway: it no longer
       reads `S.scope` at all. */
    var stale = function () {
      if (!S) { return true; }
      if (mySession !== session || mySeq !== fetchSeq) {
        syncScopePanel();
        syncValidity();
        return true;
      }
      return false;
    };
    return apiGet("/api/teacher/set-work/scope?class_id=" +
                  encodeURIComponent(S.classId)).then(function (r) {
      if (stale()) { return false; }
      S.scopeLoading = false;
      S.scope = r.body || {};
      var k = S.scope.class || {};
      loadFigures(k.key_stage).then(function (ok) { if (ok) { redrawFigures(); } });
      var tiers = S.scope.tiers || [];
      /* ⊕ MRB-336 — AN EDIT KEEPS THE ROW'S OWN TIER. `/scope` answers with
         the CLASS's default, which is the right opening answer for a new
         set and the wrong one for a set that already exists: a teacher
         editing a Foundation revision set for a Higher class would have
         watched it become Higher a moment after the sheet opened, and
         `roTier` would then disagree with the chip rail. */
      if (!(S.editId && S.tier)) {
        S.tier = k.default_tier ||
          (tiers.indexOf("medium") > -1 ? "medium" : (tiers[0] || ""));
      }
      /* ⊕ MRB-335 — THE COHORT, and the pruning that goes with it. `/scope`
         is the only authority on which classes may be set the same work; a
         selection made before it answered can legitimately be outside. */
      S.cohortIds = {};
      ((S.scope.cohort_classes) || []).forEach(function (c) {
        S.cohortIds[String(c.id)] = true;
      });
      if (S.classId) { S.cohortIds[S.classId] = true; }
      S.classes = S.classes.filter(function (id) { return S.cohortIds[id]; });
      if (S.classId && S.classes.indexOf(S.classId) < 0) {
        S.classes.push(S.classId);
      }
      refreshClasses();
      buildTierChips();
      buildSubjectChips();
      buildPaperChips();
      buildTree();
      syncTree();
      syncScopes();
      /* ⊕ MRB-342.2 §3.3 — read once, per `/scope` answer, same as everything
         else this function resolves. */
      syncNoteVisibility();
      /* ⊕ first-week fixes (22 Sep 2026) — the panel resolves IN PLACE, so a teacher who already
         walked forward to the Topic step watches `Loading` become the tree
         without touching anything. No step change, no toggle, no re-open. */
      syncScopePanel();
      syncValidity();
      return true;
    }, function () {
      if (stale()) { return false; }
      S.scopeLoading = false;
      S.scope = null;
      S.scopeErr = true;
      els.classNote.hidden = false;
      els.tree.textContent = "";
      els.treeRows = [];
      /* ⊕ first-week fixes (22 Sep 2026) — the word is in `treeNote` now, not appended into the tree
         itself: `buildTree()` empties `els.tree`, so a tag written in here was
         a note whose lifetime depended on which function ran last. */
      syncScopePanel();
      syncValidity();
      return false;
    });
  }

  /* The cap the count chips obey. Before /preview answers it is the count
     /scope already sent for this node at this tier — which IS the
     availability — so the normal path costs one request, not two. */
  function scopeAvailable(sc) {
    var s = sc || cur();
    var r = nodeFor(s.kind, s.ref);
    return r ? countAt(r.data, S.tier) : 0;
  }

  /* ⊕ MRB-342.2 — the one line under a scope's count field, or null. Reads
     `sc.cappedBy`, set below, and `maxPerScope()` for the ceiling's own
     number — never a number typed into this file. */
  function capNoteFor(sc) {
    if (sc.cappedBy === "ceiling") { return SAY.capNoteCeiling(maxPerScope()); }
    if (sc.cappedBy === "pool") {
      return SAY.capNotePool(sc.available, SAY.tier[S.tier] || S.tier || "");
    }
    return null;
  }

  /* ⊕ MRB-342.2 — ONE PATH FOR A QUICK PICK AND A TYPED NUMBER, per the
     contract's own words: "there is one code path, not two." A chip tap and
     the number field's `commit` both end here with nothing but the number
     the teacher asked for — this function is the only place that decides
     what happens to a number bigger than this topic can give.

     ⚠️ THE CEILING IS CLAMPED HERE, CLIENT-SIDE, BEFORE THE REQUEST — and
     that is a deliberate difference from how the POOL clamp works (which is
     read back FROM `/preview`'s answer, in `loadPreview` below). The two
     ceilings answer different questions. The pool is a fact this file does
     not know until the server has looked, so it can only ever be read from
     the response. The ceiling (`maxPerScope()`) is known up front, from
     `/scope`, and pre-clamping it means the number this file remembers
     asking for and the number the network actually carries never disagree —
     and it means a request for 50,000 is never sent at all. The SERVER still
     re-validates independently and would refuse nothing: this is a courtesy
     to the network, not the security boundary (there is none needed here —
     nothing is written by a download or a preview). */
  function setScopeCount(sc, rawN) {
    var ceiling = maxPerScope();
    var overCeiling = rawN > ceiling;
    sc.count = overCeiling ? ceiling : rawN;
    /* Provisional — a rarer POOL clamp on top of this one, discovered only
       once `/preview` answers, wins the note that is actually shown
       (`loadPreview` below), because it is the truthful description of what
       was actually delivered. Set here so the note appears immediately for
       the ordinary case, without waiting on the network. */
    sc.cappedBy = overCeiling ? "ceiling" : null;
    sc.capNote = capNoteFor(sc);
    S.keepPicked = false;             // ⊕ MRB-336
    syncCountChips(sc);
    loadPreview(sc);
  }

  /* The cap the count chips obey. Before /preview answers it is the count
     /scope already sent for this node at this tier — which IS the
     availability — so the normal path costs one request, not two. */
  function scopeAvailable(sc) {
    var s = sc || cur();
    var r = nodeFor(s.kind, s.ref);
    return r ? countAt(r.data, S.tier) : 0;
  }

  /* ⊕ MRB-342 — ONE SCOPE'S PREVIEW, and every line of it is that scope's.
     Two of these can legitimately be in flight together, so the guard is
     `session` + `fetchSeq` (which only `/scope` moves) + this scope's own
     `seq`. A preview for the second topic can no longer discard the first
     topic's rows, and vice versa.

     ⊕ MRB-342.2 — AND THE COUNT SENT IS THE TEACHER'S OWN, UNCAPPED BY THE
     POOL. `setScopeCount` has already clamped to the ceiling above; nothing
     here clamps to `sc.available`, because the whole point of §1 is that a
     quick pick or a typed number bigger than the pool is not refused, not
     silently shrunk before it is even asked — it is asked for, the server
     says what it actually holds, and `sc.count` becomes THAT number
     (contract §1.1: "the server returns the whole pool and says so"). */
  function loadPreview(scope) {
    var sc = scope || cur();
    if (!sc.kind || !sc.ref) { return Promise.resolve(false); }
    if (!sc.els) { syncScopes(); }
    var want = sc.count;
    if (want < 1) {
      sc.picked = [];
      sc.available = 0;
      buildQuestions(sc);
      syncScopes();
      syncValidity();
      return Promise.resolve(false);
    }
    var mySession = session, mySeq = fetchSeq, myScopeSeq = ++sc.seq;
    sc.busy = true;
    sc.previewErr = false;
    syncValidity();
    /* ⚠️ NO `exclude` HERE, DELIBERATELY. `exclude` is /swap's contract: it
       stops a swap handing back a question the teacher has already read.
       Sending this session's shown-set to /preview instead would mean going
       BACK a step and forward again silently produced a different set of
       questions, and would eat the pool a scope has. */
    return apiGet("/api/teacher/set-work/preview?class_id=" +
      encodeURIComponent(S.classId) +
      "&tier=" + encodeURIComponent(S.tier) +
      "&scope_kind=" + encodeURIComponent(sc.kind) +
      "&scope_ref=" + encodeURIComponent(sc.ref) +
      subjectParam(sc) +
      "&count=" + encodeURIComponent(want)
    ).then(function (r) {
      if (!S || mySession !== session || mySeq !== fetchSeq ||
          myScopeSeq !== sc.seq) { return false; }
      var d = r.body || {};
      sc.busy = false;
      sc.picked = d.picked || [];
      sc.available = (typeof d.available === "number") ? d.available : sc.available;
      sc.picked.forEach(function (q) { S.shown[String(q.id)] = true; });
      sc.swapDead = {};
      sc.swapNote = {};
      sc.expanded = {};
      /* A different set of questions is a different thing to set, so it gets
         its own key. Without this, changing the count and pressing Set work
         would replay the FIRST set under the second set's chip. */
      S.clientRef = uuid();
      /* ⊕ MRB-342.2 — THE CHIP/FIELD IS NOW WHATEVER ACTUALLY ARRIVED, full
         stop. `capCount`'s old job — moving the selected number down to the
         largest thing that fits — is gone along with the idea that the
         number has to be one of the four quick picks: a typed 43 on a scope
         holding 43,504 duplicate-stem rows correctly ends up reading 43, not
         "the nearest chip below 43".

         A server-reported POOL clamp (`d.capped_by === "pool"`) always wins
         the note over a client-guessed ceiling clamp, because it is the
         description of what was actually delivered — see `setScopeCount`'s
         comment for why a stale "ceiling" note would otherwise say a bigger
         number was added than the rows on screen. */
      sc.cappedBy = (d.capped_by === "pool") ? "pool" :
        (sc.cappedBy === "ceiling" ? "ceiling" : null);
      sc.count = sc.picked.length;
      sc.capNote = capNoteFor(sc);
      buildQuestions(sc);
      syncScopes();
      syncValidity();
      return true;
    }, function () {
      if (!S || mySession !== session || mySeq !== fetchSeq ||
          myScopeSeq !== sc.seq) { return false; }
      sc.busy = false;
      sc.previewErr = true;
      sc.picked = [];
      if (sc.els) {
        sc.els.qlist.textContent = "";
        sc.els.qRows = [];
        sc.els.qlist.appendChild(el("div", "sw-row-tag", SAY.unavailable));
      }
      syncScopes();
      syncValidity();
      return false;
    });
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
      /* ⊕ MRB-336 — a different tier is a different set of questions, so an
         edit stops keeping the ones the row already holds. */
      S.keepPicked = false;
      /* ⊕ MRB-342 — THE TIER IS THE SET'S, NOT A SCOPE'S, so changing it
         throws away every scope's rows and not just the current one. A set
         holding Foundation questions from one topic and Higher from another
         is not a thing this sheet can write: the assignment carries ONE
         `set_tier`. */
      S.scopes.forEach(function (sc) {
        resetScopeQuestions(sc);
        /* A selected node that has dropped to zero at the new tier
           deselects itself, which is what disables Next (RISKS A5). */
        var r = nodeFor(sc.kind, sc.ref);
        if (r && countAt(r.data, S.tier) === 0) { sc.kind = ""; sc.ref = ""; }
      });
      syncTree();                        // re-counts IN PLACE, no request
      syncTierChips();
      syncScopes();
      syncValidity();
    });
    syncTierChips();
  }

  /* ⊕ MRB-342 — THE TIER LOCKS ONCE THERE IS MORE THAN ONE SCOPE.

     An assignment carries one `set_tier`, so a second topic is set at the
     first topic's tier or not at all. The rule is enforced by not OFFERING
     the other tiers rather than by refusing a press: a live chip that
     silently does nothing is the control this sheet does not draw, and a
     sentence explaining why is the sentence it does not write. */
  function syncTierChips() {
    var locked = filledScopes().length > 1;
    syncChips(els.tierList, S.tier, function (k) {
      return locked && String(k) !== String(S.tier);
    });
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

  /* ⊕ MRB-342 — ONE RAIL PER SCOPE, inside that scope's own section.

     ⊕ MRB-342.2 — AND THE RAIL NO LONGER DISABLES A CHIP ABOVE THE POOL.
     RISKS A4 and first-week fixes both disabled a chip once it read above
     `scopeAvailable()`, on the reasoning that offering a number the pool
     could not fill was a control that lies. Contract §1.1 overturns that
     reasoning for THIS ticket, in words: "A quick pick bigger than the pool
     gets exactly the same treatment as a typed number… it is never an error,
     and it never blocks." A pressable 20 on an eight-question topic is now
     correct — pressing it asks, the server says eight, and the inline note
     says so (`capNoteFor`). Nothing is disabled here any more. */
  function buildCountChips(sc) {
    sc.els.countList = buildChips(sc.els.chips, COUNTS.map(function (n) {
      return { key: n, label: String(n) };
    }), function (k) {
      setScopeCount(sc, Number(k));
    });
    syncCountChips(sc);
  }

  /* ⊕ MRB-342.2 — THE NUMBER FIELD'S OWN CODE PATH. `change` fires on blur
     and on the browser's native up/down steppers; Enter does not raise
     `change` on an input outside a `<form>`, so it is wired separately and
     forwarded into the same `commit`. A value that is not a whole number ≥ 1
     is silently ignored — not corrected, not toasted — because a teacher
     mid-keystroke ("1" on the way to "15") must not have their half-typed
     entry judged before they have finished typing; `change`/Enter only fire
     once they are done. */
  function wireCountInput(sc) {
    var input = sc.els.countInput;
    var commit = function () {
      var n = parseInt(input.value, 10);
      if (!(n >= 1)) { return; }
      setScopeCount(sc, n);
    };
    input.addEventListener("change", commit);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") { e.preventDefault(); commit(); input.blur(); }
    });
  }

  function syncCountChips(sc) {
    if (!sc || !sc.els || !sc.els.countList) { return; }
    /* Highlighted only when the count is exactly one of the four quick
       picks — the honest rendering of "the teacher typed 43" is that none of
       5/10/15/20 lights up. */
    syncChips(sc.els.countList, sc.count, null);
    /* The number field mirrors `sc.count` — EXCEPT while the teacher is
       actively typing in it, where overwriting `.value` mid-keystroke would
       fight their own fingers (the same reasoning `syncScopePanel` and every
       other "patched, not rebuilt" surface in this file already follows). */
    if (sc.els.countInput) {
      sc.els.countInput.max = String(maxPerScope());
      if (document.activeElement !== sc.els.countInput) {
        sc.els.countInput.value = sc.count > 0 ? String(sc.count) : "";
      }
    }
    if (sc.els.countNote) {
      sc.els.countNote.hidden = !sc.capNote;
      sc.els.countNote.textContent = sc.capNote || "";
    }
  }

  function buildReleaseChips() {
    els.relList = buildChips(els.relChips, [
      { key: "now", label: SAY.now },
      { key: "later", label: SAY.later }
    ], function (k) {
      S.release = k;
      S.badRelease = false;
      syncRelease();
      syncValidity();
    });
    syncRelease();
  }

  function syncRelease() {
    syncChips(els.relList, S.release);
    els.relFields.hidden = (S.release !== "later");
  }

  /* ⊕ MRB-336 — SECTION 14 WAS THE HOLD LINE, AND IT IS GONE.

     It drew one factual line — `Assignments open <date>` — whenever the
     release the teacher had chosen fell before `schools.assignments_open_from`,
     because the server then stored `max(requested, open_from)` and the work
     did not appear on the day they asked for it.

     The server no longer clamps. `schools.assignments_open_from` keeps its
     whole meaning for AUTOMATIC weekly composition and has none at all for
     work a teacher sets by hand, so `release_at` is now stored exactly as
     asked. There is nothing left for the sheet to disclose, and a line
     describing a rule that no longer applies would be worse than no line.

     Removed with it: `S.holdIso`, `S.showHold`, `holdMs()`, `syncHold()`,
     the `.sw-hold` node, the `clamped` field on the POST response, and the
     hold arm of `effReleaseMs()` — which was the whole of `effReleaseMs()`,
     so `stepValid` and `syncValidity` now compare Due against the release
     the teacher TYPED, which is again the release the server will use. */

  /* ═════════════════════════════════════════════════════════════════════
     15. VALIDITY — a disabled primary and an outlined field. No sentences.
     ═════════════════════════════════════════════════════════════════════ */

  function releaseIso() {
    if (S.release === "now") { return null; }
    return londonToUtcIso(S.releaseDate, S.releaseTime);
  }
  function dueIso() { return londonToUtcIso(S.dueDate, S.dueTime); }

  function stepValid() {
    /* ⊕ MRB-335 — STEP 0 IS VALID ONCE `/scope` HAS RESOLVED, WHICH IS NOT
       THE SAME AS ONCE IT HAS SUCCEEDED.

       ⛔ It used to read `if (!S.scope) return false` for every step, and on
       the classes screen that was a permanent dead end. There is no anchor
       until the first tap, so `/scope` is not requested until the first tap;
       if that request then FAILS — an expired session, a moment offline, a
       500 — `S.scope` stays null for the life of the sheet. The teacher is
       left looking at a class they have ticked and a Next that will not
       light, and nothing on the screen says why, because the failure is
       announced in the TREE, on the step they cannot reach.

       Measured on `teacher_fixtures/classes-fixture.html`, which has no
       `MrBadmusTeacherGuard` at all, so `token()` rejects before `fetch` is
       ever called: `{sel:1, pri:true, step:"0"}` with zero network requests
       — the anchor set, the tree already saying "Unavailable", and no way
       forward or back to it.

       Resolved-either-way is the honest gate. On the success path it is
       exactly "once the scope has loaded". On the failure path Next goes
       forward to the topic step, where the failure is ALREADY stated and
       where Next is already refused for want of a topic — a legible dead end
       instead of an illegible one. The class panel says it too now; see
       `loadScope`. */
    /* ⊕ first-week fixes, ruled by Mide 22 Sep 2026 — STEP 0 IS VALID WHEN A CLASS IS
       CHOSEN. FULL STOP.

       ⛔ It read `return !!(S.scope || S.scopeErr)` — resolved-either-way —
       and the note above explains why that was an improvement on what came
       before it. It is still wrong, and Mide met it in his first teaching
       week: after selecting a class, `Next` stayed grey for a noticeable time
       and SOMETIMES NEEDED THE CLASS TOGGLING OFF AND ON to wake up. Both
       halves of that follow from this line.

         · the wait is `/scope` — a round trip to Render, a KS3 tree with
           five thousand bank rows behind it — standing between a teacher's
           tap and a button that has nothing to do with the answer. Ticking a
           class is a complete statement of what step 0 asks.
         · the toggle-to-fix is the discarded-stale-response path in
           `loadScope`, which returned without calling `syncValidity()`, and a
           request that never settled, which called nothing at all. Either
           left `scope` null and `scopeErr` false forever — and toggling the
           class re-anchored and re-fetched, which is why it worked.

       Ruled: `Next` enables the moment a class is chosen; whatever it was
       waiting for happens in the background, and the toggle must become
       impossible. Both are now true by construction — this predicate cannot
       observe a fetch at all, so no state a fetch can be in can reach it. The
       Topic step carries the waiting instead, and says which of loading /
       ready / failed it is showing; see `syncScopePanel`. */
    if (S.step === 0) { return S.classes.length > 0; }
    if (!S.scope) { return false; }
    if (S.step === 1) {
      var sc = cur();
      if (!sc.kind || !sc.ref) { return false; }
      return scopeAvailable(sc) > 0;
    }
    // Detail
    if (S.busy || anyBusy() || anyPreviewErr()) { return false; }
    /* ⊕ MRB-336 — A RELEASED SET IS NOT SAVING ITS QUESTIONS, so an empty
       list is not a reason to refuse. The two fields it CAN change are the
       title and the deadline, both checked below; the questions are shown
       because a teacher changing a deadline should see what the deadline is
       on, and if that read failed the deadline is still theirs to move. */
    /* ⊕ MRB-342 — EVERY SCOPE MUST HAVE ROWS. A scope the teacher added and
       left empty would be a heading over nothing in the assignment and a
       section over nothing in the worksheet.

       ⊕ first-week fixes (22 Sep 2026) — AND THE TOTAL IS NO LONGER THE SERVER'S TWENTY. This read
       `total > MAX_QUESTIONS` on both branches, with the note "the count
       rails already refuse to compose past twenty, so this is the assertion
       behind them rather than a second rule". The rails no longer refuse
       that, because the server no longer does: the ceilings are twenty PER
       SCOPE and `MAX_SCOPES` scopes. So this is the same assertion, restated
       over the two things that are now true — and it is still the assertion
       BEHIND the controls rather than a rule of its own, because `Add topic`
       wears `MAX_SCOPES` and each count rail wears its own pool.

       ⚠️ `over` IS PER SCOPE. A single scope past twenty can only arrive from
       a stored set (an `edit()` of a row written under some other rule), and
       Save must be refused rather than sending a body the route will refuse. */
    var total = pickedTotal();
    var empty = filledScopes().some(function (sc) { return !sc.picked.length; });
    var over = filledScopes().some(function (sc) {
      return sc.picked.length > maxPerScope();
    });
    var many = filledScopes().length > MAX_SCOPES;
    if (!S.locked && (!total || empty || over || many)) { return false; }
    if (S.locked && (over || many)) { return false; }
    var t = String(S.title || "").trim();
    if (!t.length || t.length > 80) { return false; }
    var due = dueIso();
    if (!due) { return false; }
    var dueMs = Date.parse(due);
    var relMs = S.release === "later" ? Date.parse(releaseIso() || "") : Date.now();
    if (S.release === "later" && isNaN(relMs)) { return false; }
    if (isNaN(dueMs) || isNaN(relMs) || dueMs <= relMs) { return false; }
    if (dueMs > Date.now() + 365 * DAY_MS) { return false; }
    /* ⊕ MRB-342, 12 Sep 2026 — A FOUND DEFECT, AND IT DISABLED SAVE ON
       EVERY RELEASED SET.

       ⛔ This read `if (S.release === "later" && …)` with no `locked` guard.
       `edit()` sets `S.release = "later"` whenever the row carries a
       `release_at`, and a RELEASED row's release instant is in the past by
       definition — that is what "released" means. So the rule meant to stop
       a teacher SCHEDULING work into the past was being applied to a release
       nobody was changing, and `Save` was dead on exactly the screen
       MRB-336 §6 built it for: a released set, whose title and deadline are
       the only two things left to move.

       Measured on a stub, 12 Sep 2026: a set released 1 Sep, due 8 Sep, at
       the Detail step with eight questions drawn, a valid title and a valid
       deadline — `{t:"Save", off:true}`. Nothing on the screen said why,
       because the release fields are REMOVED on a released set (`syncStep`),
       so the field the rule was complaining about was not even drawn.

       The check is right for a set that is not out yet and wrong for one
       that is, so it is scoped to the first. `dueMs <= relMs` above still
       holds in both cases, which is the part that is genuinely about the
       teacher's new deadline. */
    if (!S.locked && S.release === "later" &&
        relMs < Date.now() - 5 * 60000) { return false; }
    return true;
  }

  function syncValidity() {
    els.primary.disabled = !stepValid();
    /* ⊕ MRB-336 — `Save` on a row that already exists, `Set work` on a new
       one. Only the LAST step's verb changes: the Topic step still goes
       Next, because there is still a Detail step after it. */
    els.primary.textContent = (S.step === 2)
      ? (S.editId ? SAY.save : SAY.set) : SAY.next;
    /* Edit has no Classes step — the row belongs to one class and that is
       not a thing being chosen — so its first step's Back is the way out. */
    els.back.textContent = (S.step === 0 || (S.editId && S.step === editFirst()))
      ? SAY.cancel : SAY.back;
    /* ⊕ MRB-342 — DOWNLOAD IS A DETAIL-STEP ACTION AND NOTHING ELSE. There
       is no worksheet to make before the questions have been drawn, and a
       control that is present on three steps and only works on one is a
       control that lies twice. It is enabled on the same fact the worksheet
       needs — at least one question on screen — and NOT on `stepValid`,
       because a missing deadline stops work being SET and has nothing to do
       with a file a teacher prints. */
    els.dl.node.hidden = (S.step !== 2);
    els.dl.setEnabled(!S.busy && !anyBusy() && pickedTotal() > 0);
    /* The outline: only on a field the teacher has actually filled wrongly,
       never on one they have simply not reached yet. */
    if (S.step === 2) {
      var t = String(S.title || "").trim();
      els.title.classList.toggle("sw-bad", S.badTitle || (S.titleEdited && !t.length));
      els.noteInput.classList.toggle("sw-bad", !!S.badNote);
      var due = dueIso(), dueMs = due ? Date.parse(due) : NaN;
      var relMs = S.release === "later" ? Date.parse(releaseIso() || "") : Date.now();
      var dueBad = S.badDue || (!!S.dueDate && !!S.dueTime &&
        (isNaN(dueMs) || (!isNaN(relMs) && dueMs <= relMs) ||
         dueMs > Date.now() + 365 * DAY_MS));
      els.dueDate.classList.toggle("sw-bad", dueBad);
      els.dueTime.classList.toggle("sw-bad", dueBad);
      /* ⊕ MRB-342 — `!S.locked`, for the reason given in `stepValid`: a
         released set is not changing its release, and outlining a field
         that is not on the screen is an outline nobody can act on. */
      var relBad = S.badRelease || (!S.locked && S.release === "later" &&
        !!S.releaseDate && !!S.releaseTime &&
        (isNaN(relMs) || relMs < Date.now() - 5 * 60000));
      els.relDate.classList.toggle("sw-bad", relBad);
      els.relTime.classList.toggle("sw-bad", relBad);
    }
  }

  /* ═════════════════════════════════════════════════════════════════════
     16. STEPS
     ═════════════════════════════════════════════════════════════════════ */

  function syncStep() {
    els.step.textContent = SAY.steps[S.step];
    els.overlay.setAttribute("data-sw-step", String(S.step));
    els.pClasses.hidden = (S.step !== 0);
    els.pTopic.hidden = (S.step !== 1);
    els.pDetail.hidden = (S.step !== 2);
    /* ⊕ MRB-336 — WHAT A RELEASED SET DOES NOT OFFER. The count chips
       choose how many questions; Swap changes which ones; Release decides
       when children see it. All three are decided the moment the work goes
       out, and the server refuses every one of them after that. They are
       REMOVED rather than disabled, and the tier and topic appear as values
       in their place — see the panel's head. */
    var ro = !!S.locked;
    /* The per-scope rails and lists take this in `syncScopes`. */
    syncScopes();
    /* ⊕ first-week fixes (22 Sep 2026) — the Topic panel's three states are re-stated on every step
       change, so arriving at it mid-fetch shows `Loading` rather than the
       blank tree a teacher would read as "no topics". */
    syncScopePanel();
    els.relLbl.hidden = ro;
    els.relChips.hidden = ro;
    if (ro) { els.relFields.hidden = true; }
    els.roTierLbl.hidden = !ro;
    els.roTier.hidden = !ro;
    els.roScopeLbl.hidden = !ro;
    els.roScope.hidden = !ro;
    if (ro) {
      els.roTier.textContent = S.roTier;
      els.roScope.textContent = S.roScope;
    }
    /* A step change is a NEW SCREEN, so the scroller starts at the top —
       which is the one place a scroll reset is correct, and it is not a
       selection. */
    els.sheet.scrollTop = 0;
    syncValidity();
  }

  /* ⊕ MRB-336 — WHICH STEP AN EDIT OPENS ON, and it is the one thing the
     teacher can still change. Before release nobody has seen the work, so
     everything is open and the sheet starts where the choosing starts.
     After release only the title and the deadline move, and both are on the
     Detail step. */
  function editFirst() { return S.locked ? 2 : 1; }

  function onPrimary() {
    if (!S || els.primary.disabled) { return; }
    if (S.step === 0) { S.step = 1; syncStep(); syncTree(); return; }
    if (S.step === 1) {
      S.step = 2;
      cur().available = 0;
      if (!S.titleEdited) { S.title = autoTitle(); els.title.value = S.title; }
      S.dueDate = S.dueDate || londonDatePlus(7);
      S.dueTime = S.dueTime || "18:00";
      S.releaseDate = S.releaseDate || londonDatePlus(1);
      els.dueDate.value = S.dueDate;
      els.dueTime.value = S.dueTime;
      els.relDate.value = S.releaseDate;
      els.relTime.value = S.releaseTime;
      /* Minted here — the first time the Detail step is reached — so that
         a retry of the SAME set reuses it. `loadPreview` replaces it
         whenever the questions themselves change. */
      S.clientRef = uuid();
      syncStep();
      syncRelease();
      /* ⊕ MRB-336 — AN EDIT DOES NOT RE-ROLL THE QUESTIONS ON THE WAY PAST.
         `loadPreview` picks a fresh set for the scope; arriving at the
         Detail step is not a request for different questions, and a teacher
         correcting a title must not find twenty new ones under it. Any
         change to tier, scope or count clears `keepPicked` and the preview
         runs as it always did. */
      if (S.keepPicked && cur().picked.length) {
        S.keepPicked = false;
        var k = cur();
        k.available = Math.max(k.available, k.picked.length);
        syncScopes();
        buildQuestions(k);
        syncCountChips(k);
        syncValidity();
        return;
      }
      /* ⊕ MRB-342 — ONLY THE SCOPES THAT HAVE NO ROWS ARE ASKED FOR.
         Arriving at the Detail step after adding a second topic must not
         re-roll the first one: the teacher has already read those questions
         and may have swapped two of them, and replacing the list they
         approved is the same defect as replacing the node they are
         scrolled into. */
      syncScopes();
      filledScopes().forEach(function (sc) {
        if (!sc.picked.length) { loadPreview(sc); }
      });
      return;
    }
    if (S.editId) { saveEdit(); return; }
    submit();
  }

  /* ⊕ MRB-335 — WHICH SERVER REFUSAL MARKS WHICH FIELD.

     The three `bad*` flags existed and nothing ever set them: a refusal
     produced "Not set" and left every field unmarked, so a teacher was told
     it had failed and not told where. These are the codes `server.js`
     actually returns from `POST /api/teacher/set-work` — read out of it,
     not invented — and each one names the field it is about.

     ⚠️ THE CODES WITH NO FIELD ARE DELIBERATELY ABSENT. `cohort_mismatch`,
     `scope_not_for_class`, `bad_tier`, `questions_not_in_scope` are not
     about anything on the Detail step; outlining an arbitrary control for
     them would be worse than the toast alone, which is what they get. */
  var BAD_FIELD = {
    bad_title: "badTitle",
    bad_due_at: "badDue",
    due_too_far: "badDue",
    bad_release_at: "badRelease",
    release_in_past: "badRelease",
    bad_note: "badNote"
  };

  function submit() {
    if (S.busy || S.submitting) { return; }
    /* One key per composed set. `loadPreview` mints a fresh one whenever the
       questions change; a RETRY after a network failure reuses this one,
       which is the entire point. */
    if (!S.clientRef) { S.clientRef = uuid(); }
    S.busy = true;
    S.submitting = true;
    syncValidity();
    /* ⊕ MRB-342 — ONE ASSIGNMENT PER CLASS, CARRYING EVERY SCOPE'S
       QUESTIONS, and the flat scope fields are the FIRST scope's.

       ⚠️ THE FLAT FIELDS ARE NOT REDUNDANT WITH `scopes[0]`. `assignments`
       has one `scope_kind`, one `scope_ref`, one `subject` and one `paper`,
       and the ruling is that they hold the first scope. Sending them is
       what makes a server that has not yet learned about `scopes` write the
       same row it wrote yesterday rather than a NULL one — the two halves
       of this ticket ship separately and the site half must not depend on
       arriving second.

       ⚠️ AND `question_ids` IS THE WHOLE SET, IN SCOPE ORDER. It is the
       column the assignment is actually made of; `scopes` exists so the
       audit payload can say which topic each block came from. Pathway is
       not here and never is — the server reads it from the class. */
    var scopes = filledScopes().map(function (sc) {
      return {
        scope_kind: sc.kind,
        scope_ref: sc.ref,
        subject: subjectOfScope(sc) || null,
        question_ids: sc.picked.map(function (q) { return q.id; })
      };
    });
    var allIds = [];
    scopes.forEach(function (s) { allIds = allIds.concat(s.question_ids); });
    var payload = {
      class_ids: S.classes.slice(),
      tier: S.tier,
      scope_kind: scopes.length ? scopes[0].scope_kind : "",
      scope_ref: scopes.length ? scopes[0].scope_ref : "",
      subject: scopes.length ? scopes[0].subject : null,
      scopes: scopes,
      question_ids: allIds,
      title: String(S.title || "").trim(),
      release_at: releaseIso(),
      due_at: dueIso(),
      client_ref: S.clientRef
    };
    /* ⊕ MRB-342.2 §3.4 — omitted on a NEW set when empty; there is nothing
       to clear yet, so `""` (which the server reads as "clear it") would be
       the wrong signal to send. Sent only when the field is actually on
       screen — `els.noteWrap.hidden` is the same capability gate
       `syncNoteVisibility` set, so a database with no column never receives
       a field it would have to silently drop. */
    if (!els.noteWrap.hidden) {
      var noteVal = els.noteValue();
      if (noteVal) { payload.note = noteVal; }
    }
    var title = payload.title;
    var classCount = payload.class_ids.length;
    var only = classCount === 1 ? classNameOf(payload.class_ids[0]) : "";
    /* ⚠️ CAPTURED, NOT READ BACK OFF `S`. A response can arrive after the
       sheet has closed — that is the whole reason `close()` now refuses
       mid-flight — and the toast and the refresh must still happen, because
       the WORK WAS SET whatever the sheet is doing. Everything the success
       path needs is in these locals. */
    var mySession = session;
    apiPost("/api/teacher/set-work", payload).then(function (r) {
      /* `replayed` is the idempotent path: the server recognised
         `client_ref` and is handing back what it created the first time.
         It is a success and is reported as one — a teacher who retried a
         timeout must not be told it failed, and must not get a second set. */
      var ok = !!(r.ok && r.body && (r.body.success || r.body.replayed));
      if (!ok) {
        if (S && mySession === session) {
          S.busy = false;
          S.submitting = false;
          var code = (r.body && r.body.error) || "";
          var field = BAD_FIELD[code];
          if (field) { S[field] = true; }
          syncValidity();
        }
        toast(SAY.notSetToast);
        return;
      }
      var done = { title: title, classIds: payload.class_ids,
                   assignmentIds: r.body.assignment_ids || [],
                   releaseAt: r.body.release_at || null,
                   replayed: !!r.body.replayed };
      if (S && mySession === session) {
        S.busy = false;
        S.submitting = false;
        S.clientRef = "";
        close();
      }
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
         registered one simply keeps its stale card, exactly as v1 did.

         ⚠️ FIRED EVEN WHEN THE SHEET HAS GONE. It is about the PAGE, not
         about the sheet, and a card left reading "no work set" over work
         that was set is the defect this closes. */
      if (typeof window.MRB_SET_WORK_DONE === "function") {
        try { window.MRB_SET_WORK_DONE(done); }
        catch (e) { console.error("[set-work] refresh hook", e); }
      }
    }, function () {
      /* A transport failure, so `client_ref` is KEPT: pressing Set work
         again sends the same key, and the server either does the work or
         replays what it already did. */
      if (S && mySession === session) {
        S.busy = false;
        S.submitting = false;
        syncValidity();
      }
      toast(SAY.notSetToast);
    });
  }

  function classNameOf(id) {
    var list = (S && S.classPool) || [];
    for (var i = 0; i < list.length; i++) {
      if (String(list[i].id) === String(id)) { return String(list[i].name || ""); }
    }
    var coh = (S && S.scope && S.scope.cohort_classes) || [];
    for (var j = 0; j < coh.length; j++) {
      if (String(coh[j].id) === String(id)) { return String(coh[j].name || ""); }
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
     16b. THE WORKSHEET — ⊕ MRB-342

     ⚠️ A DOWNLOAD WRITES NOTHING. `POST /api/teacher/worksheet` composes a
     file out of questions the teacher is already looking at and hands it
     back; no row reaches `assignments`, no child sees anything, and the
     sheet stays exactly where it was. That is the whole reason it is a
     SECOND action beside Set work rather than a step inside it: a teacher
     printing a cover lesson is not setting one.

     ⚠️ AND `pathway` IS NEVER IN THE BODY. Every Set-work route re-derives
     the class's pathway server-side and refuses to accept one; this route
     is the same contract and the same refusal. The body carries the class,
     the tier the teacher asked for, the scopes, and the ids — nothing that
     would let a browser widen what it may see.

     ⚠️ THE RESPONSE IS BYTES, NOT JSON. `apiPost` parses JSON and would
     swallow a PDF, so this has its own envelope. A non-2xx answer leaves the
     sheet untouched and says `Unavailable` — the word it already uses for
     "this could not be got" — rather than inventing a seventh string. */

  var DOWNLOAD_PATH = "/api/teacher/worksheet";

  /* A filename the operating system will accept, from a title a teacher
     typed. Not a security boundary — the file never leaves this browser —
     but a title with a slash in it produces a download nobody can find. */
  /* ⊕ MRB-342.2 §2.6 — `perTopic` GIVES THE FALLBACK A `.zip`, NEVER A
     `.pdf`/`.docx`. This fallback only ever runs when `Content-Disposition`
     could not be read (cross-origin, header not exposed) — see
     `nameFromHeaders` — so it is the ONLY place a client-guessed extension
     can disagree with what is actually inside the file. Handing a ZIP a
     `.pdf` name is exactly the defect this parameter exists to prevent. */
  function fileNameFor(title, format, perTopic) {
    var base = String(title || SAY.worksheet)
      .replace(/[^0-9A-Za-zÀ-ɏ ._-]+/g, " ")
      .replace(/\s+/g, " ")
      .trim()
      .slice(0, 80) || SAY.worksheet;
    if (perTopic) { return base + ".zip"; }
    return base + (format === "docx" ? ".docx" : ".pdf");
  }

  /* ⚠️ REVOKED ON A TIMER, NOT IMMEDIATELY. Safari starts the download
     asynchronously after the synthetic click, and revoking the object URL in
     the same tick cancels it. The anchor is detached straight away; only the
     URL waits. */
  function saveBlob(blob, name) {
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = name;
    a.rel = "noopener";
    a.style.cssText = "position:fixed;left:-9999px;top:0";
    document.body.appendChild(a);
    a.click();
    if (a.parentNode) { a.parentNode.removeChild(a); }
    setTimeout(function () {
      try { URL.revokeObjectURL(url); } catch (e) { /* already gone */ }
    }, 20000);
  }

  /* The server's own filename when it is readable, ours when it is not.
     `Content-Disposition` is not a CORS-safelisted response header, so on a
     cross-origin deploy this is empty and the fallback is what ships — which
     is why the fallback is a real name rather than "download". */
  function nameFromHeaders(res, title, format, perTopic) {
    var cd = "";
    try { cd = res.headers.get("Content-Disposition") || ""; }
    catch (e) { cd = ""; }
    var m = /filename\*?=(?:UTF-8'')?"?([^";]+)"?/i.exec(cd);
    if (m && m[1]) {
      try { return decodeURIComponent(m[1]); } catch (e) { return m[1]; }
    }
    return fileNameFor(title, format, perTopic);
  }

  /* ⊕ MRB-342.2 — `worksheet_busy` IS A "TRY AGAIN", NOT A FAILURE.
     The backend allows two concurrent LARGE renders (>200 questions,
     reachable now the per-scope cap is 2000 rather than 20) and 503s a
     third rather than risk an OOM that would take a child's own
     `/api/class/current-assignment` down along with it. An ordinary
     10–40-question worksheet can never reach this — the threshold is 200 —
     so it is a real state and a rare one, and it must read as "busy",
     never as "broken": no stack, no code, no `Unavailable`. The server's
     own `message` is shown verbatim rather than a word this file invents,
     because it is the one sentence on this whole surface that is DATA from
     the network rather than this module's own chrome — RISKS A9 governs
     what `SAY` can say, not a status line a server composed. */
  function postWorksheet(payload) {
    return token().then(function (t) {
      return fetch(apiBase() + DOWNLOAD_PATH, {
        method: "POST",
        headers: { Authorization: "Bearer " + t,
                   "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
    }).then(function (res) {
      if (res.status === 503) {
        return res.json().then(function (body) {
          var e = new Error("worksheet: busy");
          e.busy = true;
          e.busyMessage = (body && typeof body.message === "string" &&
                            body.message) || SAY.unavailable;
          throw e;
        }, function () {
          var e = new Error("worksheet: busy");
          e.busy = true;
          e.busyMessage = SAY.unavailable;
          throw e;
        });
      }
      if (!res.ok) { throw new Error("worksheet: " + res.status); }
      return res.blob().then(function (b) {
        return { blob: b, name: nameFromHeaders(res, payload.title,
                                                payload.format,
                                                !!payload.per_topic) };
      });
    });
  }

  /* The public one-shot: build the body, get the bytes, save them. Resolves
     true or false and NEVER rejects — every caller is a click listener, and
     a throw inside one is reported by the gates as a dead control.

     ⚠️ `opts.quiet` SUPPRESSES THE TOAST AND NOTHING ELSE, and it exists for
     exactly one caller: `downloadAssignment`, which has a SECOND thing to
     try when the first is refused (see its comment). A failure the caller is
     about to recover from must not put `Unavailable` on the screen for a
     second and then produce the file anyway — that is a control that says it
     failed and then succeeds, which is worse than either. Every other caller
     leaves it unset and is told. */
  function download(opts) {
    var o = opts || {};
    var scopes = (o.scopes || []).filter(function (s) {
      return s && s.scope_kind && s.scope_ref &&
             (s.question_ids || []).length;
    });
    if (!o.classId || !o.tier || !scopes.length) {
      return Promise.resolve(false);
    }
    var payload = {
      class_id: String(o.classId),
      tier: String(o.tier),
      scopes: scopes.map(function (s) {
        return { scope_kind: String(s.scope_kind),
                 scope_ref: String(s.scope_ref),
                 subject: s.subject || null,
                 question_ids: s.question_ids.map(String) };
      }),
      format: (o.format === "docx" || o.format === "word") ? "docx" : "pdf",
      answers: o.answers !== false,
      /* ⊕ MRB-342.1 — DEFAULTS TRUE ON THIS SIDE TOO, matching the route's
         own default. A caller that predates the flag — `downloadAssignment`
         from a class row, say — keeps the file it has always produced. */
      multiple_choice: o.multipleChoice !== false,
      /* ⊕ MRB-342.2 §2.6 — DEFAULTS FALSE, matching the route: an old caller
         that never learned this flag keeps getting one file, exactly as
         before. */
      per_topic: !!o.perTopic
    };
    if (o.title) { payload.title = String(o.title).slice(0, 80); }
    /* ⊕ MRB-342.2 §2.1 — omitted entirely when empty, never sent as `""`.
       `normaliseNote` (via `buildNoteField().value()`) has already trimmed
       and collapsed whitespace by the time it reaches here; an
       empty-after-that string is the same as never having typed one. */
    if (o.note) {
      var n = normaliseNote(o.note);
      if (n) { payload.note = n; }
    }
    return postWorksheet(payload).then(function (r) {
      /* ⚠️ EXACTLY ONE SAVE. `per_topic: true` answers with a ZIP, not
         several files — the server already does the bundling (contract
         §2.6) precisely so this line never has to loop over a list of blobs
         and call `saveBlob` more than once. Browsers block multiple
         automatic downloads; there is no path here that could trigger one. */
      saveBlob(r.blob, r.name);
      return true;
    }, function (e) {
      /* ⊕ MRB-342.2 — `busy` IS NOT LOGGED AS AN ERROR. It is the server
         correctly refusing to risk an OOM under real load — expected,
         self-recovering, and not a fact about anything broken here. The
         button is already re-enabled the moment this promise settles (the
         caller's own `finally`-equivalent below `go()`), so "try again in
         a moment" is true the instant it is shown. */
      if (e && e.busy) {
        if (!o.quiet) { toast(e.busyMessage || SAY.unavailable); }
        return false;
      }
      /* ⊕ Stream L, 25 Sep 2026 (experience run, item 25/8) — A QUIET
         REFUSAL IS EXPECTED, NOT AN ERROR. `downloadAssignment`'s
         multi-topic path (above) tries the assignment's own single stored
         scope FIRST, `quiet: true`, on the documented understanding that a
         two-topic set will refuse it (`questions_not_in_scope` — the ids
         of the topic that did not make it into `assignments`' one scope
         column) and fall back to a per-subtopic body that always resolves.
         `console.error`-ing that first, EXPECTED refusal was noise in front
         of a feature working exactly as designed — the audit's own words,
         "before the documented fallback". A caller that is NOT quiet still
         gets the log: this is the one signal that a REAL failure occurred
         on a request nothing is going to retry. */
      if (!o.quiet) { console.error("[set-work] worksheet", e); }
      if (!o.quiet) { toast(SAY.unavailable); }
      return false;
    });
  }

  /* The sheet's own body, out of the scopes the teacher has composed. */
  function sheetWorksheet(format, answers, multipleChoice) {
    if (!S) { return null; }
    return {
      classId: S.classId,
      tier: S.tier,
      title: String(S.title || "").trim(),
      format: format,
      answers: answers,
      multipleChoice: multipleChoice !== false,
      scopes: filledScopes().map(function (sc) {
        return { scope_kind: sc.kind, scope_ref: sc.ref,
                 subject: subjectOfScope(sc) || null,
                 question_ids: sc.picked.map(function (q) { return q.id; }) };
      })
    };
  }

  /* ⊕ MRB-342 — ONE DOWNLOAD CONTROL, USED IN THREE PLACES.

     The sheet's header, the class table's assignment row and the marking
     screen all offer the same thing, so they are the same component rather
     than three. `request(format, answers)` is the only thing that differs:
     the sheet has the questions in hand, and a row has to read them first,
     so it may return a payload OR a promise of one.

     ⚠️ IT IS A MENU, NOT TWO BUTTONS. `PDF` is the default and `Word` is the
     other one; a row with two download buttons side by side reads as two
     different downloads. `Answers` is a toggle inside the same menu because
     it is a property of the file, not a third format.

     ⚠️ AND IT CLOSES ON AN OUTSIDE PRESS. A menu left open over a table is
     a menu that will eventually be pressed by accident. */
  function makeDownload(opts) {
    var o = opts || {};
    var state = { answers: true, mc: true, perTopic: false, busy: false };

    var wrap = el("div", "sw-dl");
    var b = btn("sw-btn sw-dl-btn", SAY.download);
    b.setAttribute("data-sw", o.mark || "download");
    b.setAttribute("aria-haspopup", "true");
    b.setAttribute("aria-expanded", "false");

    var menu = el("div", "sw-dl-menu");
    menu.hidden = true;
    menu.setAttribute("data-sw", "download-menu");
    menu.setAttribute("aria-label", SAY.worksheet);

    var head = el("div", "sw-dl-title", SAY.worksheet);

    /* ⊕ MRB-342.1 — REAL CHECKBOXES, AND THAT IS THE WHOLE CHANGE.
       These two were `<button role="menuitemcheckbox">` carrying an inline
       SVG tick, which LOOKS like a checkbox and behaves like one only for as
       long as somebody keeps writing the behaviour by hand. An
       `<input type="checkbox">` inside its own `<label>` is checkable by
       Space, reachable by Tab, announced by a screen reader as a checkbox
       with a state, and focus-ringed by the browser — none of which the
       button ever was, and all of which had to be re-implemented to keep it.

       ⚠️ AND THE MENU ROLES CAME OFF WITH IT. A native checkbox inside
       `role="menu"` is a contradiction: ARIA's menu pattern owns the arrow
       keys and expects `menuitemcheckbox` children, so a real checkbox in
       one is announced as a menu item that is also not a menu item. The
       panel is now an ordinary labelled group, which is what it always
       was. */
    function checkRow(mark, label) {
      var row = el("label", "sw-dl-opt sw-dl-check");
      var box = document.createElement("input");
      box.type = "checkbox";
      box.className = "sw-dl-box";
      box.checked = true;
      box.setAttribute("data-sw", mark);
      /* The text is a `<span>` so the row's own `textContent` is exactly the
         label — RISKS A9's sweep reads the panel's direct children. */
      row.appendChild(box);
      row.appendChild(el("span", "sw-dl-word", label));
      return { row: row, box: box };
    }
    var mcC = checkRow("dl-multiple-choice", SAY.multipleChoice);
    var ansC = checkRow("dl-answers", SAY.answers);
    /* ⊕ MRB-342.2 §2.6 — "one file or one per topic", beside the other two.
       Same idiom: a real checkbox in its own label. Unchecked (the default)
       is "one file" — today's behaviour for a caller that never touches it. */
    var perTopicC = checkRow("dl-per-topic", SAY.onePerTopic);
    var checks = el("div", "sw-dl-checks");
    checks.appendChild(mcC.row);
    checks.appendChild(ansC.row);
    checks.appendChild(perTopicC.row);
    perTopicC.box.checked = false;

    /* ⊕ MRB-342.2 §2.1 — the note, shared with the Set-work sheet's own
       (see `buildNoteField`). This one is per DOWNLOAD, not persisted: it
       travels with the single `POST /api/teacher/worksheet` this menu is
       about to make, and is gone the moment the menu is reset. */
    var noteField = buildNoteField("dl-note");

    var pdf = btn("sw-dl-opt", SAY.pdf);
    pdf.setAttribute("data-sw", "dl-pdf");
    var word = btn("sw-dl-opt", SAY.word);
    word.setAttribute("data-sw", "dl-word");

    menu.appendChild(head); menu.appendChild(checks);
    menu.appendChild(noteField.wrap);
    menu.appendChild(pdf); menu.appendChild(word);
    wrap.appendChild(b); wrap.appendChild(menu);

    /* State → the boxes. Only `reset` needs it now: a person's own click is
       already reflected by the browser before `change` fires, and writing
       `checked` back inside the handler is how a checkbox comes to flicker. */
    function syncAnswers() {
      mcC.box.checked = state.mc;
      ansC.box.checked = state.answers;
      perTopicC.box.checked = state.perTopic;
    }

    function setOpen(on) {
      menu.hidden = !on;
      b.setAttribute("aria-expanded", on ? "true" : "false");
    }

    function go(format) {
      if (state.busy) { return; }
      var body;
      try { body = o.request ? o.request(format, state.answers, state.mc) : null; }
      catch (e) { body = null; }
      if (!body) { setOpen(false); toast(SAY.unavailable); return; }
      state.busy = true;
      b.disabled = true;
      setOpen(false);
      Promise.resolve(body).then(function (payload) {
        if (!payload) { toast(SAY.unavailable); return false; }
        payload.format = format;
        payload.answers = state.answers;
        payload.multipleChoice = state.mc;
        payload.perTopic = state.perTopic;
        payload.note = noteField.value();
        return download(payload);
      }, function () {
        toast(SAY.unavailable);
        return false;
      }).then(function () {
        state.busy = false;
        b.disabled = false;
      });
    }

    b.addEventListener("click", function (e) {
      e.stopPropagation();
      if (b.disabled) { return; }
      setOpen(menu.hidden);
    });
    /* ⚠️ `change`, NOT `click`, AND NOT ON THE LABEL. A click on a
       `<label>` is forwarded by the browser to its input, so a click listener
       here would run twice for one press — once for the label and once for
       the forwarded click — and the box would end up back where it started.
       `change` fires once, for a mouse press and for the Space key alike. */
    mcC.box.addEventListener("change", function () { state.mc = mcC.box.checked; });
    ansC.box.addEventListener("change", function () { state.answers = ansC.box.checked; });
    perTopicC.box.addEventListener("change", function () {
      state.perTopic = perTopicC.box.checked;
    });
    pdf.addEventListener("click", function (e) { e.stopPropagation(); go("pdf"); });
    word.addEventListener("click", function (e) { e.stopPropagation(); go("docx"); });
    menu.addEventListener("click", function (e) { e.stopPropagation(); });
    document.addEventListener("click", function () { setOpen(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { setOpen(false); }
    });

    syncAnswers();
    return {
      node: wrap,
      setEnabled: function (on) { b.disabled = !on || state.busy; },
      reset: function () {
        state.answers = true; state.mc = true; state.perTopic = false;
        noteField.textarea.value = ""; noteField.sync();
        syncAnswers(); setOpen(false);
      }
    };
  }

  /* ⊕ MRB-342 — A SET THAT ALREADY EXISTS, DOWNLOADED FROM ITS ROW.

     ⚠️ IT READS THE ROUTE THE CHILD'S OWN PAGE READS, for the reason `edit`
     does: `/api/class/current-assignment` is the one place the questions ON
     a set are served from, and a second read of the same rows would be a
     second answer to the same question.

     ⚠️ THE READ HAPPENS ON THE PRESS. A class table draws a dozen rows;
     pre-reading every set's questions on the chance one is downloaded would
     be twelve requests for no clicks.

     ⚠️ AND THERE IS NO MOUNTED COMPONENT HERE, DELIBERATELY. The generated
     teacher pages are drawn by `shared/student-runtime.js`, whose `draw()`
     empties the mount host and rebuilds the whole template on every
     `setState` — so a menu this module appended into a table row would be
     destroyed by the next redraw and its listeners with it. The row offers
     the two formats the way that page already offers a delete confirm:
     the same button, twice, in place, rendered by the template. This is the
     ACTION behind those presses and owns no DOM at all. */
  /* ⊕ D2, 25 Sep 2026 (experience follow-ups, item 2) — the by-subtopic
     fallback's own ids (`byLesson`, `order` — one array per `lesson_slug`),
     regrouped by the TOPIC each subtopic sits under. Nothing on
     `/api/class/current-assignment`'s question rows carries a topic id or a
     disambiguating subject — only `lesson_slug` — so the one place either is
     known is the class's own curriculum tree, read here the same way the
     composer sheet's `loadScope` already does. `MAX_SCOPES` is the same
     module-level constant `Add topic` is capped by; the backend's own cap is
     `SW.MAX_SCOPES` in set-work-scope.js and the two are asserted equal by
     `set_work_scope_check`.

     Answers `null` — never throws, never logs — when the tree cannot be
     read, or when grouping still leaves more topics than `MAX_SCOPES`. The
     second case is not reachable by anything the sheet can build today (a
     set would need eleven topics' worth of one science on it), so it is
     handled rather than asserted away: an honest "cannot do this" beats an
     assumption that quietly stops being true the day a limit changes
     elsewhere. */
  function groupByTopic(classId, byLesson, order) {
    return apiGet("/api/teacher/set-work/scope?class_id=" +
      encodeURIComponent(classId)).then(function (r) {
      var tree = (r.body && r.body.tree) || [];
      var infoBySlug = {};
      tree.forEach(function (topic) {
        (topic.children || []).forEach(function (child) {
          infoBySlug[child.id] = { topicId: topic.id,
                                    subject: topic.subject || null };
        });
      });
      var byTopic = {}, topicOrder = [];
      for (var i = 0; i < order.length; i++) {
        var ref = order[i];
        var info = infoBySlug[ref];
        // A subtopic this class's own tree does not know is not expected —
        // every id here came off a real assignment on this class — but a
        // half-built group is worse than none, so it stops the whole thing
        // rather than shipping a worksheet that is silently missing a
        // question the teacher assigned.
        if (!info) { return null; }
        var key = (info.subject || "") + "|" + info.topicId;
        if (!byTopic[key]) {
          byTopic[key] = { scope_kind: "topic", scope_ref: info.topicId,
                            subject: info.subject, question_ids: [] };
          topicOrder.push(key);
        }
        byTopic[key].question_ids =
          byTopic[key].question_ids.concat(byLesson[ref]);
      }
      if (!topicOrder.length || topicOrder.length > MAX_SCOPES) { return null; }
      return topicOrder.map(function (key) { return byTopic[key]; });
    }, function () { return null; });
  }

  function downloadAssignment(row) {
    var o = row || {};
    if (!o.assignmentId || !o.classId) { return Promise.resolve(false); }
    return apiGet("/api/class/current-assignment?class_id=" +
      encodeURIComponent(o.classId) +
      "&assignment_id=" + encodeURIComponent(o.assignmentId)
    ).then(function (r) {
      var body = r.body || {};
      var qs = body.questions || [];
      var a = body.assignment || {};
      if (!qs.length) { toast(SAY.unavailable); return false; }
      /* ⚠️ `question_ref`, NOT `id`, AND THIS WAS A REAL DEFECT (found by the
         real-bytes drive, 13 Sep 2026). `/api/class/current-assignment`
         builds each question as
         `{ position, question_ref, band, rung, lesson_slug, text, options }` —
         there is NO `id` on it, and there never was. `qs.map(q => q.id)`
         therefore produced `[undefined, undefined, …]`, which
         `JSON.stringify` writes as `[null, null, …]`, which the route's
         `isStrList` refuses with `bad_question_ids`. So EVERY download from
         an assignment row and from the marking screen answered 400 and
         toasted `Unavailable`.
         ⚠️ IT SURVIVED ITS OWN DRIVE BECAUSE THE DRIVE WAS A STUB: a stub
         accepts any body, so a body of nulls looked exactly like a body of
         ids. Nothing short of the real route could have told them apart.
         The falsy filter is not defensive padding — a RETIRED question comes
         back as `{ question_ref, retired: true }` with no text, and a body
         carrying an empty id would be refused for the wrong reason. */
      var ids = qs.map(function (q) { return q.question_ref || q.id; })
                  .filter(function (x) { return !!x; });
      if (!ids.length) { toast(SAY.unavailable); return false; }

      var common = {
        classId: o.classId,
        tier: o.tier || a.set_tier || "",
        title: o.title || a.title || "",
        format: o.format,
        answers: o.answers !== false,
        multipleChoice: o.multipleChoice !== false
      };
      /* ⚠️ A SUBJECT THAT IS NOT A STRING IS NOT A SUBJECT. The route's
         `validateBody` refuses a non-string `subject` with `bad_scope`, and
         a caller handing one over is a caller whose 400 says nothing about
         what it did wrong. `shared/teacher-data.js` really did hand this an
         object — a PostgREST embed shadowing the column of the same name —
         and the whole marking-screen Download was dead because of it. That
         is fixed at the source; this is the boundary refusing to pass on a
         shape it cannot use, so the next producer to get it wrong loses the
         subject rather than the download. */
      var subjIn = o.subject || a.subject;
      var subject = (typeof subjIn === "string" && subjIn && subjIn !== "all")
        ? subjIn : null;
      var stored = [{
        scope_kind: o.scopeKind || a.scope_kind || "",
        scope_ref: o.scopeRef || a.scope_ref || "",
        subject: subject,
        question_ids: ids
      }];

      /* ⛔ A SET MADE FROM SEVERAL TOPICS CANNOT BE PRINTED FROM ITS ROW
         UNDER ONE SCOPE, and that is a consequence of MRB-342's own
         multi-scope write rather than a bug in either half on its own.

         `assignments` has ONE scope triple. A two-topic set therefore
         records only the FIRST topic, by design (`docs/mrb342/REPORT.md`
         §3) — so posting all of its questions under that one scope asks the
         worksheet route for ids the first topic's pool does not contain, and
         the route correctly answers `questions_not_in_scope`. Found by the
         real-bytes drive, 13 Sep 2026; it cannot be reproduced against a
         stub, which has no pool to be outside of.

         ⚠️ THE STORED SCOPE IS TRIED FIRST, AND THAT IS THE POINT OF DOING
         IT THIS WAY ROUND. Every single-topic set — which is nearly all of
         them — still posts exactly the body it posted before, so its
         worksheet is unchanged: one scope means the renderer draws NO
         section heading, and splitting unconditionally would chop an
         ordinary topic-level set into one heading per subtopic.

         Only when that is refused does it fall back to the questions' OWN
         subtopics, which `/api/class/current-assignment` supplies as
         `lesson_slug` on every row (KS3 lesson, KS4 subtopic — the backend
         normalises both to that name). That body is always in scope, because
         a question is by definition inside its own subtopic. The cost of the
         fallback is one refused request, on the rarer path, and the teacher
         sees nothing of it. */
      var byLesson = {}, order = [];
      var splittable = true;
      for (var i = 0; i < qs.length; i++) {
        var ref = qs[i].lesson_slug;
        var qid = qs[i].question_ref || qs[i].id;
        if (!ref || !qid) { splittable = false; break; }
        if (!byLesson[ref]) { byLesson[ref] = []; order.push(ref); }
        byLesson[ref].push(String(qid));
      }
      /* ⚠️ AND THE FALLBACK CARRIES NO `subject`, WHICH IS NOT AN
         OVERSIGHT. `assignments` records ONE subject as well as one scope,
         so a two-topic set across two sciences — the ordinary KS3 case,
         where a unit of chemistry and a unit of biology sit in the same
         week — stamps the row `chemistry` and would then send `chemistry`
         with the BIOLOGY subtopic, which `findScope` cannot find:
         `scope_not_for_class`, on the body built to avoid a refusal. Found
         one refusal further in by the same drive.

         `subject` is only ever a DISAMBIGUATOR, and the one thing it
         disambiguates is `atomic-structure`, which is a TOPIC id in both
         chemistry and physics. Every SUBTOPIC ref in the curriculum is
         unique, and these are all subtopic refs, so omitting it can only
         resolve to the node the question actually came from.

         ⊕ D2, 25 Sep 2026 (experience follow-ups, item 2) — RETIRED IN FAVOUR OF
         `groupByTopic`, ABOVE. This grouped by subtopic — one scope per
         `lesson_slug` — which is what `too_many_scopes` (max `MAX_SCOPES`,
         10) meant a set spanning more than ten subtopics could not be
         downloaded at all: the stored scope refused (by design, above), the
         per-subtopic fallback ALSO refused, and nothing tried a third time —
         `console.error`, no file, no message. A topic-level set, or a
         multi-topic set of two broad topics, reaches eleven subtopics
         easily; a school reaching eleven TOPICS in one set is not a shape
         the product can make. (The subject rule above still holds for the
         regroup: a TOPIC ref is not unique across sciences, so there the
         tree's own subject is sent with it.) */
      var groupable = splittable && order.length > 1;

      var one = {}, k;
      for (k in common) { if (common.hasOwnProperty(k)) { one[k] = common[k]; } }
      one.scopes = stored;
      if (!groupable) { return download(one); }
      one.quiet = true;
      /* ⊕ D2, 25 Sep 2026 (experience follow-ups, item 2) — GROUPED BY TOPIC,
         NOT BY SUBTOPIC. `findScope`'s `topic` branch pools EVERY subtopic
         under that topic (`slugsForScope`, set-work-scope.js), so the same
         ids the subtopic split would have sent reach the route as far FEWER
         scopes when grouped by their topic instead — a set can span at most
         as many topics as it can subtopics, and nothing in the product can
         create a set spanning more than `MAX_SCOPES` topics. `groupByTopic`
         reads the class's own tree once (the same `/api/teacher/set-work/
         scope` the composer sheet already calls) to find each subtopic's
         topic id and disambiguating subject; it answers `null` only if that
         read fails or the ids still will not fit in `MAX_SCOPES` topics,
         which is the one shape this cannot express — reported to the
         teacher as `SAY.unavailable` rather than left silent, and never
         logged as an error: a set this big is a known, named limit, not a
         broken request. Proved end to end by `set_work_drive.py`'s
         `row_download_over_ten_subtopics` checks. */
      return download(one).then(function (ok) {
        if (ok) { return true; }
        return groupByTopic(o.classId, byLesson, order).then(function (byTopic) {
          if (!byTopic) {
            toast(SAY.unavailable);
            return false;
          }
          var two = {};
          for (var kk in common) {
            if (common.hasOwnProperty(kk)) { two[kk] = common[kk]; }
          }
          two.scopes = byTopic;
          return download(two);
        });
      });
    }, function () {
      toast(SAY.unavailable);
      return false;
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     17. OPEN / CLOSE
     ═════════════════════════════════════════════════════════════════════ */

  /* ⊕ MRB-335 — `classId` IS OPTIONAL, AND OMITTING IT IS THE CLASSES
     SCREEN'S CASE.

     ⛔ IT USED TO OPEN ON `CLASSES[0]`. Design's primary on the classes
     screen binds to `openSetWork`, and `openSetWork` handed it
     `klass().id` — and `klass()` on that page is
     `this.CLASSES[0] || MRB_NO_CLASS()`. So pressing "Set work" over a list
     of twelve classes silently anchored the whole sheet to whichever one
     sorted first: its tier, its cohort, its curriculum tree. A teacher who
     then ticked a different class got that class set work at the FIRST
     class's tier, and the chip agreed with the wrong answer.

     Ruled: from the classes screen the sheet opens on the Classes step with
     nothing preselected and every class the teacher has listed. The first
     tap picks the anchor, `/scope` is fetched for it, and the rows outside
     its cohort go `aria-disabled`. From a card or the class screen nothing
     changes — that class arrives ticked, as it always did. */
  function open(opts) {
    var o = opts || {};
    buildShell();
    isAnchoredOpen = !!o.classId;
    opener = (document.activeElement &&
              document.activeElement !== document.body)
      ? document.activeElement : null;
    /* ⚠️ EVERY IN-FLIGHT ANSWER IS ABANDONED HERE. See the guards above: an
       answer for the class the sheet was showing a moment ago must not paint
       over the class it is showing now. */
    session += 1;
    S = freshState(o.classId ? String(o.classId) : "");
    els.title.value = "";
    els.noteInput.value = "";
    els.noteSync();
    els.noteWrap.hidden = true;         // re-shown by `syncNoteVisibility`
    els.relTime.value = S.releaseTime;
    els.dueTime.value = S.dueTime;
    els.relDate.value = "";
    els.dueDate.value = "";
    els.scopesHost.textContent = "";
    els.dl.reset();
    els.tree.textContent = "";
    els.treeRows = [];
    els.classList.textContent = "";
    els.classRows = [];
    els.classNote.hidden = true;
    /* Drawn from the page before anything is asked for, so step 0 is never
       an empty panel with a dead Next. `/scope` refines it when it lands. */
    buildClasses();
    buildReleaseChips();
    syncStep();
    els.overlay.hidden = false;
    /* ⚠️ COUNTED ONTO THE OVERLAY, and it is the same instrument
       `student-runtime.js` puts on its mount host for the same reason
       ("counted onto the mount point so a gate reads a number instead of
       inferring from a screenshot").

       Four buttons open this one sheet — the classes screen's primary, the
       class screen's primary, a class card and the empty state — and the
       second of them pressed in a sweep finds the sheet ALREADY open, for a
       different class, with a tree that has not refetched yet. The DOM is
       momentarily identical, so a probe reading text and node counts
       concludes the control did nothing. It did: it re-opened the sheet, on
       another class. This says so, and `data-sw-class` says which. */
    opens += 1;
    els.overlay.setAttribute("data-sw-opens", String(opens));
    els.overlay.setAttribute("data-sw-class", S.classId);
    /* The one `focus()` in this file, and it is at OPEN — never after a
       state change. RISKS A1 bans the second, not the first: a dialog that
       does not take focus is unreachable from a keyboard. */
    els.sheet.focus({ preventScroll: true });
    /* Nothing to scope by yet on the classes screen; the first tap does it. */
    if (S.classId) { loadScope(); }
  }

  /* ⊕ MRB-335 — IT REFUSES WHILE A SET IS IN FLIGHT.

     ⛔ Escape, or a tap on the scrim, between pressing Set work and the
     server answering used to null `S` — and the response then landed in a
     handler whose every line reads `S`, threw, and produced no toast, no
     card refresh and no error. The work HAD been set. The teacher, seeing
     nothing happen, sets it again: two assignments for thirty children,
     from one deliberate press and one dismissal.

     The primary is already disabled for the same window, so this closes the
     other two ways out of the sheet and leaves the teacher exactly one
     thing to do, which is wait — for at most as long as the POST takes.
     `submit()` clears the flag on every path, including the failing ones. */
  function close() {
    if (!els) { return; }
    if (S && S.submitting) { return; }
    session += 1;
    els.overlay.hidden = true;
    S = null;
    isAnchoredOpen = false;
    if (opener && opener.focus) {
      try { opener.focus({ preventScroll: true }); } catch (e) { /* gone */ }
    }
    opener = null;
  }

  /* ═════════════════════════════════════════════════════════════════════
     17b. EDIT — the same sheet, opened on a row that already exists
     ═════════════════════════════════════════════════════════════════════ */

  /* ⊕ MRB-336 §6, 8 Sep 2026.

     ⚠️ IT IS `open()` WITH A ROW, NOT A SECOND SHEET. Everything a teacher
     changes about a set — the tier, the node, the questions, the title, the
     two instants — is already in this sheet, already validated here, and
     already sent from here. A separate edit dialog would be a second
     implementation of all of that, and the two would agree until the day
     they did not.

     ⚠️ THE CLASS IS THE ROW'S CLASS AND IS NOT A CHOICE. A multi-class set
     is N rows, one per class, and Edit acts on the ONE row the teacher is
     looking at. So the Classes step is not in the flow at all — see
     `editFirst()` — and the sheet says nothing about the other classes,
     because a teacher looking at one class's row is acting on one class's
     row.

     ⚠️ BEFORE RELEASE, EVERYTHING; AFTER RELEASE, THE TITLE AND THE
     DEADLINE. Nobody can have started work they cannot see, so before
     release there is nothing to protect. After it, a pupil may be halfway
     through: changing the questions underneath them is refused at the
     server (`locked_after_release`) and is not offered here.

     `row` carries what the class page already knows about the assignment —
     it comes off the same paper object the table row was drawn from, so no
     request is needed for any of it. Only the QUESTIONS have to be read,
     and only when they are being shown. */
  function edit(opts) {
    var o = opts || {};
    if (!o.assignmentId || !o.classId) { return false; }
    buildShell();
    isAnchoredOpen = true;
    opener = (document.activeElement &&
              document.activeElement !== document.body)
      ? document.activeElement : null;
    session += 1;
    S = freshState(String(o.classId));
    S.editId = String(o.assignmentId);
    S.locked = !!o.released;
    S.keepPicked = true;
    S.tier = o.tier || "";
    /* ⊕ MRB-342 — AN EDIT IS ONE SCOPE, and slot 0 is where it goes. The row
       in `assignments` carries one scope triple and `PATCH` takes one, so
       `Add topic` is hidden for the whole of an edit (see `syncScopes`). */
    S.scopes[0].kind = o.scopeKind || "";
    S.scopes[0].ref = o.scopeRef || "";
    S.si = 0;
    S.subject = o.subject || "all";
    S.paper = o.paper || "both";
    S.title = String(o.title || "");
    S.titleEdited = true;          // never overwritten by `autoTitle`
    S.roTier = (SAY.tier[S.tier] || S.tier || "");
    S.roScope = String(o.scopeTitle || o.title || "");
    /* ⊕ MRB-342.2 §3 — `o.note` is the generated page's own field name
       (`teacher_rulings.py`'s `MRB_SET_WORK_EDIT` call); `o.teacherNote` is
       accepted too, defensively, in case a caller ever names it after the
       column instead. Either way this is only ever a display default — a
       capability the row's own database answers `false` for hides the field
       regardless of what is in it.

       ⚠️ `S.noteLoaded` IS NOT THE SAME QUESTION AS "IS THERE TEXT". Until
       25 Sep 2026 `teacher_rulings.py` did not pass `note`/`teacherNote` at
       all (the open item this comment used to track), so `o.note` was
       always `undefined` and the field opened blank on every edit —
       indistinguishable, on screen, from a row whose note genuinely IS
       empty. ⊕ Stream J, 25 Sep 2026 (experience run, item 4) — CLOSED:
       `MRB_SET_WORK_EDIT`'s two call sites now pass `note: p.note || ''`
       (`p.note` carried from `assignments.teacher_note` by `buildPapers` in
       shared/teacher-live.js), so `o.note` arrives as a real string on every
       edit and this flips to `true` on its own. `saveEdit()`
       reads THIS flag, not the field's emptiness, to decide whether the
       PATCH may touch `teacher_note` at all: an edit that never learned
       what the stored note was must not be the edit that clears it. Once
       the generated page is wired to pass it, `o.note` starts arriving as
       a real string (possibly `""`) and this flips to `true` on its own —
       nothing here needs to change again. */
    S.noteLoaded = (o.note !== undefined && o.note !== null) ||
                   (o.teacherNote !== undefined && o.teacherNote !== null);
    S.noteEdited = false;
    S.note = String(o.note || o.teacherNote || "");

    /* The two instants, back into the fields the teacher set them from. */
    var rel = o.releaseAt ? utcToLondonParts(o.releaseAt) : null;
    if (rel) {
      S.release = "later"; S.releaseDate = rel.date; S.releaseTime = rel.time;
    }
    var due = o.dueAt ? utcToLondonParts(o.dueAt) : null;
    if (due) { S.dueDate = due.date; S.dueTime = due.time; }

    els.title.value = S.title;
    els.noteInput.value = S.note;
    els.noteSync();
    els.noteWrap.hidden = true;         // re-shown by `syncNoteVisibility`
    els.relDate.value = S.releaseDate;
    els.relTime.value = S.releaseTime;
    els.dueDate.value = S.dueDate;
    els.dueTime.value = S.dueTime;
    els.scopesHost.textContent = "";
    els.dl.reset();
    els.tree.textContent = "";
    els.treeRows = [];
    els.classList.textContent = "";
    els.classRows = [];
    els.classNote.hidden = true;

    S.step = editFirst();
    /* ⊕ MRB-336 — ONE KEY PER EDITING SESSION. `PATCH` is replay-guarded on
       (actor, assignment, client_ref) inside a thirty-minute window, exactly
       as `POST` is on (actor, client_ref): a retry after a dropped connection
       must be recognised as the same edit rather than applied twice. Minted
       HERE, when the sheet opens on a row, so that the retry inside
       `saveEdit` reuses it and a SECOND, deliberate edit — reopened from the
       row — gets its own. */
    S.clientRef = uuid();
    buildClasses();
    buildReleaseChips();
    syncStep();
    syncRelease();
    els.overlay.hidden = false;
    opens += 1;
    els.overlay.setAttribute("data-sw-opens", String(opens));
    els.overlay.setAttribute("data-sw-class", S.classId);
    els.overlay.setAttribute("data-sw-edit", S.editId);
    els.sheet.focus({ preventScroll: true });
    loadScope();
    loadStoredQuestions();
    return true;
  }

  /* The questions this set actually holds, so the sheet shows the work the
     children were given rather than a fresh draw for the same node.

     ⚠️ IT READS THE ROUTE THE CHILD'S OWN PAGE READS, and that is the point:
     `/api/class/current-assignment` is the one place the questions ON a set
     are served from, it is already reachable by this teacher, and adding a
     second read of the same rows would be a second answer to the same
     question. `bank_position`, tiers, pathway — none of it is re-derived
     here.

     ⚠️ AND A FAILURE IS NOT FATAL. Before release the teacher can simply
     step back and pick again; after release the title and the deadline are
     all that can move anyway, and both are already on screen. So a failed
     read leaves `Unavailable` where the rows would be and the Save that
     matters still works. */
  function loadStoredQuestions() {
    var mySession = session, want = S.editId;
    return apiGet("/api/class/current-assignment?class_id=" +
      encodeURIComponent(S.classId) +
      "&assignment_id=" + encodeURIComponent(want)
    ).then(function (r) {
      if (!S || mySession !== session || S.editId !== want) { return false; }
      var qs = (r.body && r.body.questions) || [];
      var sc = cur();
      /* ⛔ THE ROUTE'S SHAPE IS NOT THE SHEET'S SHAPE, AND READING IT AS IF
         IT WERE RENDERED FIVE BLANK ROWS. (Pre-existing — MRB-336 — found
         by MRB-342's real-bytes drive on 13 Sep 2026 and fixed here because
         it is the same root cause as `downloadAssignment`'s.)

         `/api/class/current-assignment` serves a question as

             { position, question_ref, band, rung, lesson_slug, unit_code,
               text, figure, options: [{ letter, text, correct, why }] }

         There is no `id`, no `stem` and no `correct_index` on it. So
         `q.stem || q.prompt || ""` was ALWAYS the empty string, `q.options`
         was an array of OBJECTS handed to a renderer that expects strings,
         and `q.correct_index` was always undefined — which is why pressing
         Edit on a set showed five numbered rows with no question in them
         and no tick against the answer. Measured in a browser before it was
         touched: `n: 5`, every `stem: ""`.

         ⚠️ THE ANSWER IS CARRIED PER OPTION, NOT AS AN INDEX. `correct` is a
         boolean on each option, so the index has to be found rather than
         read — and `-1` (nothing marked) must stay `-1` rather than becoming
         0, or the sheet would tick option A on a question whose key the
         bank no longer has. */
      sc.picked = qs.map(function (q) {
        var raw = q.options || [];
        var texts = raw.map(function (o) {
          return (o && typeof o === "object") ? (o.text || "") : String(o);
        });
        var ci = (typeof q.correct_index === "number") ? q.correct_index : -1;
        if (ci < 0) {
          for (var k = 0; k < raw.length; k++) {
            if (raw[k] && raw[k].correct) { ci = k; break; }
          }
        }
        return { id: q.question_ref || q.id,
                 stem: q.text || q.stem || q.prompt || "",
                 options: texts, correct_index: ci,
                 figure: q.figure || null,
                 lesson: q.lesson_slug || q.lesson || "" };
      });
      /* ⊕ Stream L, 25 Sep 2026 (experience run, item N11 / data safety) —
         A STABLE SNAPSHOT of what this set held BEFORE this editing
         session touches anything. `sc.picked` is about to be mutated by
         every count change and every swap the teacher makes; `otherScopesFor`
         (below, read at Save) needs to know what OTHER topics' questions
         existed at OPEN, not whatever `sc.picked` has been redrawn into by
         the time Save is pressed. */
      S.originalPicked = sc.picked.slice();
      sc.available = Math.max(sc.available, sc.picked.length);
      if (S.step === 2) { syncScopes(); buildQuestions(sc); syncCountChips(sc); }
      syncValidity();
      return true;
    }, function () {
      if (!S || mySession !== session || S.editId !== want) { return false; }
      S.keepPicked = false;
      var bad = cur();
      if (S.step === 2 && bad.els) {
        bad.els.qlist.textContent = "";
        bad.els.qRows = [];
        bad.els.qlist.appendChild(el("div", "sw-row-tag", SAY.unavailable));
      }
      syncValidity();
      return false;
    });
  }

  /* ⊕ MRB-336 — SAVE. The same payload as `submit()`, narrowed by what the
     row's own state allows, and sent to the row rather than to the
     collection: a second POST would be a second assignment.

     ⚠️ AFTER RELEASE IT SENDS TWO FIELDS AND NOT SEVEN. The server refuses
     the rest with `locked_after_release`; sending them anyway and relying on
     that refusal would turn every save into a coin toss about which field
     the server checked first. */
  function saveEdit() {
    if (S.busy || S.submitting) { return; }
    S.busy = true;
    S.submitting = true;
    syncValidity();
    /* ⚠️ AND `client_ref` IS REQUIRED — WITHOUT IT NOTHING SAVED AT ALL.
       `PATCH /api/teacher/set-work/:id` validates `client_ref` as a UUID and
       answers 400 `bad_client_ref` when it is missing, so every Save this
       sheet has ever sent was refused before it reached a single field. It
       failed in the quietest possible way: `BAD_FIELD` has no entry for
       `bad_client_ref`, so no field was outlined and no reason given — the
       teacher got `Not saved`, pressed again, and got it again.

       Same discipline as `submit()`: minted when the sheet opens on a row,
       reused by a retry after a transport failure, cleared on success. */
    if (!S.clientRef) { S.clientRef = uuid(); }
    var payload;
    if (S.locked) {
      payload = { title: String(S.title || "").trim(), due_at: dueIso(),
                  client_ref: S.clientRef };
    } else {
      var headScope = cur();
      var headIds = headScope.picked.map(function (q) { return q.id; });
      /* ⊕ Stream L, 25 Sep 2026 (experience run, item N11 / data safety) —
         every OTHER topic this set holds, unchanged. See `otherScopesFor`.
         Empty on the ordinary single-topic edit, which is nearly every
         edit — that case sends exactly the flat body it always sent. */
      var others = otherScopesFor(headScope, headIds);
      payload = { client_ref: S.clientRef,
                  tier: S.tier,
                  title: String(S.title || "").trim(),
                  release_at: releaseIso(),
                  due_at: dueIso() };
      if (others.length) {
        payload.scopes = [{ scope_kind: headScope.kind, scope_ref: headScope.ref,
                             subject: subjectOfScope(headScope) || null,
                             question_ids: headIds }].concat(others);
      } else {
        payload.scope_kind = headScope.kind;
        payload.scope_ref = headScope.ref;
        payload.subject = subjectOfScope(headScope) || null;
        payload.question_ids = headIds;
      }
    }
    /* ⊕ MRB-342.2 §3.4 — SENT WHEN THE FIELD WAS LOADED, OR WHEN THE
       TEACHER ACTUALLY TOUCHED IT — never on an untouched field that
       opened blank because nothing loaded it.

       ⛔ THE FIRST VERSION OF THIS READ `if (!els.noteWrap.hidden)`,
       UNCONDITIONALLY, and that was a defect this ticket would have
       shipped: before 25 Sep 2026 `teacher_rulings.py` did not pass the
       stored `teacher_note` into `edit()` (see `edit()`'s own comment,
       closed the same day), so `S.noteLoaded` was `false` on every edit and
       the field always opened blank. Sending the key regardless would have
       posted
       `note: ""` on EVERY save — including a save where the teacher only
       moved the deadline — and `note: ""` means "clear it" (contract
       §3.4). A teacher who had written a note, then edited the deadline a
       week later without ever looking at the note field, would have had
       it silently deleted. Found before it shipped, not after: this is a
       correction, not a report of a live incident.

       `S.noteEdited` is what makes a genuine edit still work: the
       teacher typed something (even into a field that opened blank
       because nothing was loaded into it), so a real intent exists and is
       sent. `S.noteLoaded || S.noteEdited` is therefore "there is
       something honest to say about this field" — never "the field
       exists on screen".

       Gated the same way as `submit()` on TOP of that: nothing is sent
       when the field itself is hidden (no capability). It is offered on a
       RELEASED set too — a note is the teacher's own annotation, not a
       fact about the questions a pupil is mid-way through. */
    if (!els.noteWrap.hidden && (S.noteLoaded || S.noteEdited)) {
      payload.note = els.noteValue();
    }
    var title = payload.title;
    var mySession = session;
    apiPatch("/api/teacher/set-work/" + encodeURIComponent(S.editId), payload)
      .then(function (r) {
        /* ⚠️ `ok`, NOT `success`, AND THE DIFFERENCE WAS A SILENT FAILURE IN
           THE WORST DIRECTION. This read `r.body.success`, copied from
           `submit()` — but `POST /api/teacher/set-work` answers
           `{ success: true, … }` and `PATCH /api/teacher/set-work/:id`
           answers `{ ok: true, replayed, assignment_id, changed, assignment }`.
           There is no `success` key on a PATCH reply at any of its three
           success branches (fresh, replay, no-op), so this was `undefined`
           every time and every SUCCESSFUL save took the failure arm: the
           sheet stayed open, `S.busy` was cleared, and the teacher was
           toasted `Not saved`.

           ⚠️ IT WAS THE SECOND OF TWO FAULTS ON THIS ONE PRESS, and only
           the other one was reachable at first: the payload carried no
           `client_ref`, so the route answered 400 `bad_client_ref` and this
           line never got the chance to misread a success. Both are fixed
           here, and both had to be — repairing either alone leaves Save
           still reporting failure.

           Both keys are accepted rather than just the right one, because the
           two routes genuinely disagree and this is the client to both.
           Unifying them on one flag is the backend's call, not a thing to
           guess at from here; it is written up as an open item. */
        var body = r.body || {};
        var ok = !!(r.ok && (body.ok === true || body.success === true));
        if (!ok) {
          if (S && mySession === session) {
            S.busy = false;
            S.submitting = false;
            var field = BAD_FIELD[(r.body && r.body.error) || ""];
            if (field) { S[field] = true; }
            syncValidity();
          }
          toast(SAY.notSavedToast);
          return;
        }
        if (S && mySession === session) {
          S.busy = false;
          S.submitting = false;
          S.clientRef = "";        /* ⊕ MRB-336 — as `submit()` does */
          close();
        }
        toast(SAY.savedFor(title));
        if (typeof window.MRB_SET_WORK_DONE === "function") {
          try { window.MRB_SET_WORK_DONE({ title: title, saved: true }); }
          catch (e) { /* the refresh seam is best-effort, as at POST */ }
        }
      }, function () {
        if (S && mySession === session) {
          S.busy = false; S.submitting = false; syncValidity();
        }
        toast(SAY.notSavedToast);
      });
  }

  /* ═════════════════════════════════════════════════════════════════════
     18. SURFACE
     ═════════════════════════════════════════════════════════════════════ */

  window.MRBSetWork = {
    open: open,
    edit: edit,
    close: close,
    /* ⊕ MRB-342 — the worksheet, for callers that are not the sheet.
       `download` takes a composed body; `downloadAssignment` takes a row
       that already exists and reads its questions first. */
    download: download,
    downloadAssignment: downloadAssignment,
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
