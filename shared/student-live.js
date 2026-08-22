/* ═══════════════════════════════════════════════════════════════════════
   student-live.js — the live data source for the ported student pages.

   `student/class-ported.html` and `student/assignment-ported.html` define
   `window.__MRB_MOUNT__` and do not call it, and they carry no data of their
   own. This file is what decides what a student sees: it works out which of
   the two pages it is on, reads that student's real class from Supabase and
   the real backend, puts it on `window.__MRB_DATA__` under exactly the keys
   the fixtures list, and calls `window.__MRB_MOUNT__()`.

   ⛔ THERE IS NO FALLBACK TO THE FIXTURE. The fixtures are one real class's
   homework with one real child's name on it. If anything here fails, the page
   says so in plain words and does not mount.

   ⚠️ NOTHING IN THIS FILE MAY INVENT STUDENT-VISIBLE CONTENT. Where the
   product does not record something — a teacher's name, a per-week points
   history, teacher feedback on a piece of work — the key is left empty and
   the gap is written down in the handover, never filled with a plausible
   value. An empty state is honest. An invented one is not.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var HOST_ID = "mrb-student";
  var SDK_URL =
    "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js";

  /* The four helpers, in the ONE order that works. `student-data.js` delegates
     `workingAcademicYear()` to `class-entry.js` and throws a named error if it
     is not already on the page (CLAUDE.md, MRB-267), and `student-guard.js`
     owns the Supabase client that `student-data.js` asks for. */
  var DEPS = [
    "/shared/config.js",
    "/shared/class-entry.js",
    "/shared/student-guard.js",
    "/shared/student-data.js",
    /* ⊕ RULED 22 Aug 2026 — P3. Where each KS3 lesson lives, so a lesson slug
       out of the database can become the URL of the lesson itself. Generated
       by `build_student_port.py`; see `lesson_index()` there for why the map
       has to be shipped rather than derived. Last in the list because nothing
       above it needs it and it is the only one a page can survive without. */
    "/shared/ks3-lesson-urls.js"
  ];

  /* ── plain words, for when the page cannot render ───────────────────────
     No platform self-explanation (CLAUDE.md §8.10): a student is told what is
     true about their class, never about the software. */
  var SAY = {
    generic:    "We could not load your class just now. Try again in a moment.",
    /* True both for a student who has never been added to a class and for one
       whose only class finished in July — the working-year scope hides the
       second, and "this year" keeps the sentence honest for both. */
    noClass:    "You are not in a class this year yet. Your teacher will add you to one.",
    pastYear:   "That class finished at the end of last year.",
    notMine:    "That class is not one of yours.",
    noRecall:   "There is nothing to look back over yet. Check again after your next lesson.",
    noWork:     "No work has been set for this week yet.",
    workNotSet: "This week’s work is not ready yet. Check again later today."
  };

  function host() { return document.getElementById(HOST_ID); }

  function say(line) {
    var el = host();
    if (!el) { return; }
    el.textContent = "";
    var wrap = document.createElement("div");
    wrap.setAttribute("data-mrb-state", "unavailable");
    wrap.style.cssText =
      "min-height:60vh;display:flex;align-items:center;justify-content:center;" +
      "padding:32px;box-sizing:border-box;";
    var p = document.createElement("p");
    p.style.cssText =
      "margin:0;max-width:34ch;text-align:center;font:400 17px/1.55 " +
      "'IBM Plex Sans',system-ui,-apple-system,'Segoe UI',sans-serif;" +
      "color:var(--ks3-ink,#2A2018);";
    p.textContent = line;
    wrap.appendChild(p);
    el.appendChild(wrap);
  }

  /* ── which page am I on? ────────────────────────────────────────────────
     From the page's OWN compiled binding table, `window.__MRB_BIND__`, which
     the porter emits and which lists the identity strings each page binds.
     `backToClass` exists only on the assignment; `welcomeLine` only on the
     class view. That is structural — it comes out of the same build step as
     the template — so it survives the file being renamed or moved, which a
     pathname test would not. The pathname is kept as a last resort only. */
  function whichPage() {
    var keys = {};
    (window.__MRB_BIND__ || []).forEach(function (b) { keys[b.k] = true; });
    if (keys.backToClass) { return "assignment"; }
    if (keys.welcomeLine) { return "class"; }
    return /assignment/i.test(window.location.pathname) ? "assignment" : "class";
  }

  // ── loading the helpers ───────────────────────────────────────────────

  /* ⚑ THE CACHE-BUST STAMP, FOR THE FILES THIS ONE LOADS ITSELF.

     Every asset under /shared/ is served `max-age=14400, must-revalidate` —
     four hours — while the pages themselves are `max-age=0`. So a page and the
     scripts it pulls in can be four hours apart, and the failure is silent:
     `student-data.js` is where `saveBenchTheme` and the academic-year scoping
     live, and an old copy of it does not error, it just behaves like
     yesterday.

     The stamps cannot live in the DEPS list above, because this file is
     hand-written source and the hashes are only knowable at build time. So
     `build_student_port.py` publishes them onto the page as
     `window.__MRB_ASSET_V__`, keyed on the BARE FILENAME — keyed on the full
     path they would be rewritten by generate_site_v5.py's own cache-bust
     regex, which matches `/shared/<name>"` wherever it occurs, including
     inside a JSON key.

     No map, no stamp, current behaviour: this file stays loadable by a page
     that does not carry one. */
  function stamped(src) {
    var map = window.__MRB_ASSET_V__;
    if (!map) { return src; }
    var v = map[src.replace(/^\/shared\//, "")];
    return v ? src + "?v=" + v : src;
  }

  function loadScript(rawSrc) {
    var src = stamped(rawSrc);
    return new Promise(function (resolve, reject) {
      var existing = document.querySelector('script[src="' + src + '"]');
      if (existing && existing.getAttribute("data-mrb-loaded") === "1") {
        return resolve();
      }
      var s = document.createElement("script");
      s.src = src;
      s.onload = function () { s.setAttribute("data-mrb-loaded", "1"); resolve(); };
      s.onerror = function () { reject(new Error("could not load " + src)); };
      document.head.appendChild(s);
    });
  }

  async function loadDeps() {
    if (!window.supabase || !window.supabase.createClient) {
      await loadScript(SDK_URL);
    }
    for (var i = 0; i < DEPS.length; i++) {
      await loadScript(DEPS[i]);   // strictly in order — see DEPS
    }
  }

  // ── small shared helpers ──────────────────────────────────────────────
  var LONDON = "Europe/London";

  function pad2(n) { return n < 10 ? "0" + n : String(n); }

  function fmtDay(iso) {            // 'THU 18 SEP'
    if (!iso) { return ""; }
    return new Intl.DateTimeFormat("en-GB", {
      timeZone: LONDON, weekday: "short", day: "numeric", month: "short"
    }).format(new Date(iso)).replace(/,/g, "").toUpperCase();
  }

  function fmtTime(iso) {           // '18:00'
    if (!iso) { return ""; }
    return new Intl.DateTimeFormat("en-GB", {
      timeZone: LONDON, hour: "2-digit", minute: "2-digit", hour12: false
    }).format(new Date(iso));
  }

  /* 'Mon 15 Sep' and 'Thu 18 Sep, 18:00' — the docket's own two shapes, mixed
     case, which is why they cannot reuse fmtDay's upper-cased one. */
  function fmtSet(iso) {
    if (!iso) { return ""; }
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return ""; }
    var D = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    var M = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    return D[d.getDay()] + " " + d.getDate() + " " + M[d.getMonth()];
  }

  /* 'Thursday' — the day a deadline falls on, spelled out, for the bench
     blurb's closing clause. Design named Thursday for every class. */
  function weekdayName(iso) {
    if (!iso) { return ""; }
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return ""; }
    return ["Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"][d.getDay()];
  }

  function fmtDueMixed(iso) {
    if (!iso) { return ""; }
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return ""; }
    return fmtSet(iso) + ", " + pad2(d.getHours()) + ":" + pad2(d.getMinutes());
  }

  /* '13 days left', 'Due today', 'Overdue'. Against the SERVER's clock, and
     rounded the way a student counts: tomorrow is one day left, not 0.7. */
  function daysLeft(dueIso, now) {
    if (!dueIso || !now) { return ""; }
    var ms = Date.parse(dueIso) - now;
    if (isNaN(ms)) { return ""; }
    if (ms <= 0) { return "Overdue"; }
    var days = Math.ceil(ms / 86400000);
    if (days <= 1) { return "Due today"; }
    return days + " days left";
  }

  function fmtDue(iso) {
    if (!iso) { return "NO DEADLINE SET"; }
    return "DUE " + fmtDay(iso) + ", " + fmtTime(iso);
  }

  /* 'the-gas-exchange-system' → 'The gas exchange system'. A faithful reading
     of the real slug, not a new name for the lesson: the slug is the only
     lesson title these two endpoints carry. */
  function deslug(slug) {
    if (!slug) { return ""; }
    var words = String(slug).split("-").filter(Boolean).join(" ");
    return words.charAt(0).toUpperCase() + words.slice(1);
  }

  /* ── where things are, as URLs ─────────────────────────────────────────
     ⊕ RULED 22 Aug 2026 — P1 and P3. Both buttons went nowhere, and neither
     could have gone anywhere: the page had no URL for either destination.

     `?class=` and `?env=` travel with every internal link. Dropping `class`
     would land a student in whichever class `pickClass` chooses by default,
     which for a student in two classes is a coin toss; dropping `env` would
     move a tester from the test project to production mid-journey. */
  function carryParams(path) {
    var q = new URLSearchParams(window.location.search);
    var keep = new URLSearchParams();
    ["class", "env"].forEach(function (k) {
      if (q.get(k)) { keep.set(k, q.get(k)); }
    });
    var qs = keep.toString();
    return qs ? path + "?" + qs : path;
  }

  function assignmentHref() { return carryParams("/student/assignment.html"); }

  /* A KS3 lesson slug → the lesson's own page, or "" if this build does not
     know that slug. Empty rather than a guessed path: a link that 404s is
     worse than a button that is not offered, and the caller checks. */
  function lessonHref(slug) {
    if (!slug) { return ""; }
    var where = window.MRB_KS3_LESSONS && window.MRB_KS3_LESSONS[slug];
    return where ? "/ks3/" + where + "/" + slug + ".html" : "";
  }

  /* `source_ref` comes in TWO shapes and both are real.

       b4-01-s01                                        a bank/ladder id
       chemistry/particles-and-their-behaviour/particle-model   a path

     The second is how the hand-seeded May demo assignment was written, and it
     is still the only marked work on the platform — so the shape that looks
     like a legacy accident is the one a student actually has feedback on.
     Its last segment is the lesson slug, which is checked against the index
     like any other rather than trusted as a path. */
  function slugFromRef(ref) {
    if (!ref) { return ""; }
    var str = String(ref);
    return str.indexOf("/") >= 0 ? str.split("/").pop() : "";
  }

  function initials(first, last) {
    var f = (first || "").trim(), l = (last || "").trim();
    if (f && l) { return (f[0] + l[0]).toUpperCase(); }
    if (f) { return f.slice(0, 2).toUpperCase(); }
    return "";
  }

  /* '2 DAYS AGO', from the SERVER's clock against the row's own timestamp. */
  function agoText(iso, now) {
    if (!iso || !now) { return ""; }
    var days = Math.floor((now - Date.parse(iso)) / 86400000);
    if (days <= 0) { return "TODAY"; }
    if (days === 1) { return "YESTERDAY"; }
    if (days < 7) { return days + " DAYS AGO"; }
    var weeks = Math.floor(days / 7);
    return weeks === 1 ? "1 WEEK AGO" : weeks + " WEEKS AGO";
  }

  /* The school-local calendar date of an instant, as `YYYY-MM-DD`, so it can
     be compared against an academic year's own `start_date` / `end_date` —
     which are plain dates and carry no timezone at all. */
  function londonYmd(when) {
    var parts = new Intl.DateTimeFormat("en-CA", {
      timeZone: LONDON, year: "numeric", month: "2-digit", day: "2-digit"
    }).format(new Date(when));
    return parts;
  }

  /* AUTUMN / SPRING / SUMMER TERM, from the SERVER's clock (the `Date` header
     of the backend response) read in school-local time, AGAINST THE CLASS'S
     OWN ACADEMIC YEAR.

     ⊕ RULED 22 Aug 2026 — P8. THE YEAR IS THE POINT, AND LEAVING IT OUT IS
     WHAT PUT "SUMMER TERM" OVER WEEK 1.

     This used to read the calendar MONTH and nothing else: 9-12 Autumn, 1-3
     Spring, everything else Summer. That is right for eleven months of the
     year and wrong for the one that matters most — the run-up to September.
     On 21 August 2026 the month is 8, so it said SUMMER TERM, while the class
     it was labelling belongs to 2026-27, a year that has not started, whose
     first week is AUTUMN WEEK 1. A student opening the page in the holidays
     was told they were in a term that finished in July.

     The fix is not a fourth month range. It is to ask the academic year, which
     is the thing that actually knows:

       before the year starts   AUTUMN  — the pre-year window, per the standing
                                ruling that it reads as Autumn Week 1. It is
                                the term the student is about to be in, and it
                                is the term their week 1 belongs to.
       start_date .. 31 Dec     AUTUMN
       1 Jan .. 31 Mar          SPRING
       1 Apr .. end_date        SUMMER

     Anchored on the year's OWN start rather than on a hardcoded September, so
     a school whose year opens in August is labelled from its own dates. The
     Spring/Summer boundary is the English school convention; the database
     records no half-term or Easter dates for anything finer to read, and
     Easter moves, so a fixed 31 March is the honest approximation and is named
     as one rather than being presented as a lookup.

     With no academic year to read — the query failed, or a class has none —
     it falls back to the month rule it replaced. A wrong-but-plausible term
     name is a poor answer, but a page that will not draw its own breadcrumb
     is a worse one, and the year is only ever missing when something else has
     already gone wrong. */
  /* ── the environment badge ─────────────────────────────────────────────
     ⊕ RULED 22 Aug 2026 — P6. The badge renders only when this is NOT the
     product. On mrbadmus.com, nothing at all.

     "Production" is BOTH halves — the real domain AND the real project — and
     it has to be, because the dangerous case is the one where only one of
     them is true. A developer on localhost pointed at the production database
     with `?env=prod` is looking at 135 real children's homework, and that is
     exactly when a badge earns its place. So:

       mrbadmus.com + prod project     ""       the product. Nothing.
       localhost    + prod project     "PROD"   ⚠️ real data, off the real site
       anywhere     + test project     "TEST"
       anything else                   the environment's name, or LOCAL

     ⚠️ THIS CANNOT BE PROVED ON localhost, and that is the design rather than
     a gap. Every local drive runs on `localhost?env=prod`, which is the second
     row: the badge SHOWS, and showing is correct there. The empty case is only
     reachable from the real domain, so it is verified on mrbadmus.com after
     the push and nowhere else. */
  /* ── how many, in words ────────────────────────────────────────────────
     ⊕ RULED 22 Aug 2026 — P2. Design writes the round size as a WORD — "Six a
     round", "SIX QUESTIONS", "OF SIX" — which is exactly why no grep for a
     digit ever found any of the three, and why the header announced six over
     a counter reading 01/02. Keeping the word keeps Design's voice; the
     number inside it is now the real one.

     Beyond twelve it falls back to digits rather than growing a dictionary. A
     round is capped at six, so the tail is unreachable today and exists so
     that raising the cap cannot produce "undefined a round". */
  var NUM_WORDS = ["no", "one", "two", "three", "four", "five", "six",
                   "seven", "eight", "nine", "ten", "eleven", "twelve"];

  function numWord(n) {
    n = Number(n) || 0;
    return (n >= 0 && n < NUM_WORDS.length) ? NUM_WORDS[n] : String(n);
  }

  function capitalise(w) { return w.charAt(0).toUpperCase() + w.slice(1); }

  function envBadgeText() {
    var cfg = window.MrBadmusConfig || {};
    var env = String(cfg.environment || "");
    var host = String(window.location.hostname || "");
    var live = (host === "mrbadmus.com" || host === "www.mrbadmus.com");
    if (live && env === "prod") { return ""; }
    return env ? env.toUpperCase() : "LOCAL";
  }

  function termLabelFrom(serverNow, year) {
    var today = londonYmd(serverNow);

    if (year && year.start_date) {
      if (today < year.start_date) { return "AUTUMN TERM"; }
      var startYear = Number(String(year.start_date).slice(0, 4));
      if (today <= startYear + "-12-31")     { return "AUTUMN TERM"; }
      if (today <= (startYear + 1) + "-03-31") { return "SPRING TERM"; }
      return "SUMMER TERM";
    }

    var month = Number(new Intl.DateTimeFormat("en-GB", {
      timeZone: LONDON, month: "numeric"
    }).format(new Date(serverNow)));
    if (month >= 9 && month <= 12) { return "AUTUMN TERM"; }
    if (month >= 1 && month <= 3)  { return "SPRING TERM"; }
    return "SUMMER TERM";
  }

  /* "AUTUMN TERM" → "Autumn". ⊕ 23 Aug 2026 — PHASE 1b, for the account
     sheet's TERM row, which Design sets in sentence case and beside a week
     count rather than as the shouted crumb-rail label. Derived from the one
     term label this file already computes rather than computed a second time:
     two derivations of the same term is how the crumb rail and the sheet come
     to disagree in March. */
  function seasonOf(termLabel) {
    var word = String(termLabel || "").split(" ")[0];
    if (!word) { return ""; }
    return word.charAt(0) + word.slice(1).toLowerCase();
  }

  /* ── the backend ───────────────────────────────────────────────────────
     Bearer token from the live session. The response's `Date` header is the
     SERVER clock, and it is the only "now" this file trusts for deciding what
     is due — never `new Date()`, which is the device's opinion. The device
     clock is used for nothing but choosing how to print a timestamp. */
  var serverNow = null;

  /* The sink for the page about to mount. Module-level rather than threaded
     through the return value, because `__MRB_DATA__` is a DATA object and the
     sink is not data — putting a live object with a network connection inside
     the thing the page renders from would blur exactly the line this file
     exists to keep sharp. */
  var pendingSink = null;

  async function api(path, token) {
    var cfg = window.MrBadmusConfig || {};
    var base = cfg.BACKEND_URL || "https://mrbadmus-backend.onrender.com";
    var res = await fetch(base + path, {
      headers: { Authorization: "Bearer " + token }
    });
    var stamp = res.headers.get("date");
    if (stamp) {
      var t = Date.parse(stamp);
      if (!isNaN(t)) { serverNow = t; }
    }
    if (!res.ok) {
      throw new Error("backend " + res.status + " on " + path);
    }
    return res.json();
  }

  /* ── the four options of one question ──────────────────────────────────
     Both endpoints return `[{letter, text, correct, why}]` — the ladder rows
     carry the letter themselves, the bank rows have it added by the route.

     ⚠️ THE RIGHT ANSWER'S FEEDBACK SLOT IS EMPTY STRING, ALWAYS. A lesson
     authors three feedback strings, one per distractor; the API returns
     `why: null` for the correct option deliberately. Writing "Correct!" into
     that slot is exactly what Mide's ruling 1a and `student_parity.py` layer H
     forbid, so the slot closes rather than fills. */
  function normalise(options, answerLetter) {
    var opts = (options || []).slice(0, 4);
    if (opts.length !== 4) { return null; }
    var letters = ["A", "B", "C", "D"];
    var ai = -1;
    if (answerLetter) {
      ai = opts.findIndex(function (o, i) {
        return (o.letter || letters[i]) === answerLetter;
      });
    }
    if (ai < 0) { ai = opts.findIndex(function (o) { return o.correct === true; }); }
    if (ai < 0) { return null; }        // nothing can mark it — leave it out
    return {
      a: ai,
      o: opts.map(function (o) { return o.text == null ? "" : String(o.text); }),
      f: opts.map(function (o, i) {
        if (i === ai) { return ""; }    // ← the closed slot. Do not fill it.
        return typeof o.why === "string" ? o.why : "";
      })
    };
  }

  // ── which class ───────────────────────────────────────────────────────
  /* A student sees only their own current-year class; there is no picker.
     `loadStudentClasses` is already scoped to the working academic year and
     already ordered by name, so "the working-year one, and if several still,
     the first by name" is simply its first row. A `?class=<uuid>` in the URL
     is honoured only when it names one of those same classes — a bookmark to
     last year's class resolves to the same honest message either way. */
  function pickClass(classes) {
    if (!classes || !classes.length) { return null; }
    var wanted = new URLSearchParams(window.location.search).get("class");
    if (wanted) {
      var match = classes.filter(function (k) { return k.id === wanted; })[0];
      if (match) { return match; }
    }
    return classes[0];
  }


  /* ═══════════════════════════════════════════════════════════════════════
     THE SINK — where a student's answers actually go
     ═══════════════════════════════════════════════════════════════════════

     Ruled 22 Aug 2026. `window.__MRB_SINK__` is set immediately before mount
     and read lazily by the ported page. It is a WRITER and a RESUME SOURCE;
     everything the page RENDERS still comes through `MRB_DATA`.

     ⛔ THE OLD PAGE POSTED NOWHERE. `handIn` wrote '17 SEP, 20:41' into local
     state and stopped. This is the other end of that wire.

     ⚠️ `resume()` IS SYNCHRONOUS BY CONSTRUCTION. The page calls it from
     `loadLive()`, which cannot await. So the progress is fetched BEFORE the
     mount and handed over already resolved — an empty first paint followed by
     a late repaint is how a student sees their own answers appear and then
     jump, and it is avoidable by ordering rather than by cleverness.
     ═══════════════════════════════════════════════════════════════════════ */

  var LETTERS = "ABCD";

  /* '17 SEP, 20:41' — Design's own shape, from the SERVER's timestamp. The
     device clock chooses nothing here but how to print what the server said. */
  function fmtStamp(iso) {
    if (!iso) { return ""; }
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return ""; }
    var M = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
             "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"];
    return d.getDate() + " " + M[d.getMonth()] + ", " +
           pad2(d.getHours()) + ":" + pad2(d.getMinutes());
  }

  /* "2 days late" — the real number of days, or nothing. Design welded a
     fixed "2 DAYS LATE" over whatever the true overdue period happened to be.
     Rounded UP, because four hours past the deadline is a day late to a
     teacher and "0 days late" is not a sentence anybody says. */
  function lateTextFor(dueIso, doneIso) {
    if (!dueIso || !doneIso) { return "late"; }
    var ms = Date.parse(doneIso) - Date.parse(dueIso);
    if (isNaN(ms) || ms <= 0) { return "late"; }
    var days = Math.ceil(ms / 86400000);
    return days + (days === 1 ? " day late" : " days late");
  }

  function makeSink(assignment, questions, progress, token) {
    /* The page speaks in (question index, option index). The route speaks in
       question_ref and option letters. This is the whole of the translation,
       kept in one place so neither side has to know the other's vocabulary. */
    function payloadFor(index, option, secs) {
      var q = questions[index];
      if (!q) { return null; }
      var src = q.__src || {};
      var opts = src.options || [];
      var chosen = opts[option] || {};
      var right = null;
      for (var i = 0; i < opts.length; i += 1) { if (opts[i].correct) { right = opts[i]; } }
      return {
        question_index: index,
        question_ref: src.question_ref || null,
        question_text: src.text || q.q || null,
        rung: src.rung || null,
        selected_answer: chosen.text == null ? null : String(chosen.text),
        correct_answer: right && right.text != null ? String(right.text) : null,
        selected_option_letter: chosen.letter || LETTERS[option] || null,
        correct_option_letter: right ? right.letter : null,
        is_correct: right ? (chosen.letter === right.letter) : null,
        time_spent_seconds: secs == null ? null : secs
      };
    }

    /* Answers given while the browser is offline. The page shows them as held
       — that is Design's `held` map and its reconnect animation, untouched —
       and this re-sends them in order when the browser says it is back. */
    var queue = [];
    var flushing = false;

    async function post(path, body) {
      var cfg = window.MrBadmusConfig || {};
      var base = cfg.BACKEND_URL || "https://mrbadmus-backend.onrender.com";
      var res = await fetch(base + path, {
        method: "POST",
        headers: {
          Authorization: "Bearer " + token,
          "Content-Type": "application/json"
        },
        body: JSON.stringify(body),
        /* ⚠️ `keepalive` IS LOAD-BEARING, AND ITS ABSENCE COST AN ANSWER.
           Found by driving: the page answered a question, navigated away a
           moment later, and the row never reached the database — the browser
           CANCELS in-flight requests when the document unloads, silently, with
           no error anywhere. The page had already shown the tick.

           That is the exact shape of the defect this whole unit exists to
           remove. It is not a test artefact: a student who taps Confirm and
           then immediately taps "Back to 8r/Sc1", or closes the tab, or locks
           their phone, is doing the same thing on a slower connection.

           `keepalive` lets the request outlive the document. The 64 KB body
           limit it comes with is not a constraint here — one answer is a few
           hundred bytes. */
        keepalive: true
      });
      var stamp = res.headers.get("date");
      if (stamp) {
        var t = Date.parse(stamp);
        if (!isNaN(t)) { serverNow = t; }
      }
      if (!res.ok) { throw new Error("backend " + res.status + " on " + path); }
      return res.json();
    }

    async function flush() {
      if (flushing) { return; }
      flushing = true;
      try {
        while (queue.length) {
          var next = queue[0];
          await post("/api/assignment/answer",
                     { assignment_id: assignment.id, answer: next });
          queue.shift();          // ← only on success, so a failure retries
        }
      } catch (err) {
        console.error("[student-live] answer not saved yet", err);
      } finally {
        flushing = false;
      }
    }

    if (typeof window.addEventListener === "function") {
      window.addEventListener("online", function () { flush(); });
    }

    return {
      /* Called from `loadLive()`. Already resolved — see the note above. */
      resume: function () {
        var p = progress || {};
        var sub = p.submission;
        var answers = {};
        var count = 0;
        (p.answers || []).forEach(function (a) {
          var li = LETTERS.indexOf(a.selected_option_letter || "");
          if (li < 0) { return; }        // self-marked, or a rung with no letter
          answers[a.question_index] = li;
          count += 1;
        });
        /* Where to put them: the first question they have NOT answered, so
           returning on Thursday opens where they stopped rather than at the
           beginning. If everything is answered, at the start of the review. */
        var idx = 0;
        for (var i = 0; i < questions.length; i += 1) {
          if (answers[i] == null) { idx = i; break; }
          idx = 0;
        }
        var done = !!(sub && sub.status === "complete");
        return {
          answers: answers,
          sels: {},
          held: {},
          idx: done ? 0 : idx,
          elapsed: (sub && sub.total_time_seconds) || 0,
          view: done ? "done" : "q",
          handedAt: done ? fmtStamp(sub.completed_at) : null,
          late: !!(sub && sub.is_late),
          resumed: count > 0 && !done,
          live: true
        };
      },

      saveAnswer: function (ev) {
        var body = payloadFor(ev.index, ev.option, null);
        if (!body) { return null; }
        queue.push(body);
        flush();
        return null;
      },

      complete: function (elapsed) {
        /* Answers first. A completion that overtook the last answer would mark
           the work finished without the answer that finished it. */
        return flush().then(function () {
          return post("/api/assignment/complete", {
            assignment_id: assignment.id,
            total_time_seconds: elapsed == null ? null : elapsed
          });
        }).then(function (r) {
          var sub = (r && r.submission) || {};
          return {
            stamp: fmtStamp(sub.completed_at),
            late: !!(r && r.is_late)
          };
        });
      }
    };
  }

  // ── the class view ────────────────────────────────────────────────────
  async function buildClass(sb, user, klass, token) {
    var D = window.MrBadmusStudentData;

    var detail = await D.loadStudentClass(klass.id, user.id);
    var recall  = await api("/api/class/recall?class_id=" + klass.id, token);
    var current = await api("/api/class/current-assignment?class_id=" + klass.id, token);

    /* Whether a piece of work is still open or has been missed is decided
       against the SERVER's clock and nothing else. Without one, this page does
       not guess with the device's — it says it could not load. */
    if (!serverNow) { throw new Error("no server clock on the response"); }

    /* The teaching week each piece of work belongs to. `assignments` records
       it (`academic_week`), so read it rather than recomputing it; the fall
       back derives it from `due_at` against the academic year's start_date,
       which is the same arithmetic the producer used to set that due_at. */
    var weeks = {};
    var aw = await sb.from("assignments")
      .select("id, academic_week").eq("class_id", klass.id).is("deleted_at", null);
    (aw.data || []).forEach(function (r) { weeks[r.id] = r.academic_week; });

    /* ── which lesson each piece of work draws on ───────────────────────
       ⊕ RULED 22 Aug 2026 — P3. "Open the lesson" needs a lesson, and the
       work rows carried none: `lessonDefs` is built from the CURRENT
       assignment's questions and says nothing about the marked work from
       three weeks ago, which is the only work that button appears on.

       The chain is `assignment_questions.source_ref` → the bank or the
       ladder → `lesson_slug`, and a student is allowed to walk all of it
       (`aq_student_read`; both question tables are readable by any
       authenticated user). A failure anywhere in it costs the button and
       nothing else — the work list still renders, so this is caught and
       logged rather than thrown. */
    var lessonsFor = {};
    try {
      var ids = (aw.data || []).map(function (r) { return r.id; });
      if (ids.length) {
        var aq = await sb.from("assignment_questions")
          .select("assignment_id, position, source_ref")
          .in("assignment_id", ids).order("position");

        var refs = [], bySlug = {};
        (aq.data || []).forEach(function (r) {
          if (r.source_ref && String(r.source_ref).indexOf("/") < 0) {
            refs.push(r.source_ref);
          }
        });
        if (refs.length) {
          var bank = await sb.from("ks3_bank_questions")
            .select("id, lesson_slug").in("id", refs);
          (bank.data || []).forEach(function (r) { bySlug[r.id] = r.lesson_slug; });
          var lad = await sb.from("ks3_ladder_questions")
            .select("question_ref, lesson_slug").in("question_ref", refs);
          (lad.data || []).forEach(function (r) {
            bySlug[r.question_ref] = r.lesson_slug;
          });
        }

        (aq.data || []).forEach(function (r) {
          var slug = bySlug[r.source_ref] || slugFromRef(r.source_ref);
          var href = lessonHref(slug);
          if (!href) { return; }              // not a lesson this build knows
          var list = lessonsFor[r.assignment_id] ||
                     (lessonsFor[r.assignment_id] = []);
          for (var i = 0; i < list.length; i++) {
            if (list[i].slug === slug) { return; }   // distinct, in position order
          }
          list.push({ slug: slug, href: href, name: deslug(slug) });
        });
      }
    } catch (err) {
      console.error("[student-live] could not resolve the lessons behind "
                    + "this class's work", err);
    }

    var year = null;
    var yrs = await sb.from("academic_years")
      .select("id, name, start_date, end_date").is("deleted_at", null);
    if (!yrs.error) { year = window.MRBClassEntry.workingAcademicYear(yrs.data); }

    function weekOf(card) {
      if (weeks[card.id] != null) { return weeks[card.id]; }
      if (!card.due_at || !year || !year.start_date) { return 1; }
      var days = Math.floor(
        (Date.parse(card.due_at) - Date.parse(year.start_date + "T00:00:00Z")) / 86400000);
      return Math.max(1, Math.min(39, Math.floor(days / 7) + 1));
    }

    var currentId = current && current.assignment ? current.assignment.id : null;
    var currentCount = current && current.questions ? current.questions.length : 0;

    /* ── work[] ──────────────────────────────────────────────────────────
       Every assignment this class has, in the three buckets the data layer
       returns, with the status derived from the real rows and the SERVER
       clock: scored → marked, handed in but unscored → pending, still open →
       open, past its deadline and not handed in → missed.

       `notes` and `items` are OMITTED, not emptied and not invented. Nothing
       in `assignment_submissions` records a teacher's written feedback, and
       the per-question breakdown lives in `assignment_question_attempts`,
       which this page does not read. A row simply has no feedback to show. */
    var cards = detail.assignmentsDueNow
      .concat(detail.assignmentsComingUp, detail.assignmentsDone);

    var work = cards.map(function (c) {
      var status;
      if (c.is_submitted) {
        status = (c.score != null && c.max_score != null) ? "marked" : "pending";
      } else if (c.due_at && Date.parse(c.due_at) < serverNow) {
        status = "missed";
      } else {
        status = "open";
      }

      var brief;
      if (c.id === currentId && currentCount) { brief = currentCount + " questions"; }
      else if (c.max_score != null)           { brief = c.max_score + " marks"; }
      else                                    { brief = c.subject_name || ""; }

      var detailLine;
      if (status === "marked") {
        /* ⊕ RULED 22 Aug 2026 — W5. "Complete" replaces "Hand it in"
           everywhere it appears, and the work rows are one of the places it
           appears. The words change; nothing else does. */
        detailLine = "COMPLETED " + fmtDay(c.submitted_at) +
                     " · " + c.score + " OF " + c.max_score + " MARKS";
      } else if (status === "pending") {
        detailLine = "COMPLETED " + fmtDay(c.submitted_at) + " · NOT MARKED YET";
      } else if (status === "missed") {
        detailLine = fmtDue(c.due_at) + " · NOT COMPLETED";
      } else {
        detailLine = fmtDue(c.due_at);
      }

      /* ⊕ RULED 22 Aug 2026 — P3. Where this row's primary button goes.
         Design's label is singular — "Open the lesson" — and every real
         assignment on the platform draws on exactly one lesson, so the first
         IS the lesson. `lessons` carries the whole distinct list anyway, in
         the order the questions ask them, so a future multi-lesson row has
         somewhere honest to grow into rather than needing this re-derived. */
      var rowLessons = lessonsFor[c.id] || [];

      var row = {
        id: c.id,
        week: weekOf(c),
        title: c.title || "",
        brief: brief,
        status: status,
        detail: detailLine,
        lessons: rowLessons,
        lessonHref: rowLessons.length ? rowLessons[0].href : "",
        assignmentHref: c.id === currentId ? assignmentHref() : ""
      };
      if (status === "marked" && c.max_score > 0) {
        row.score = Math.round((c.score / c.max_score) * 100);
      }
      if (c.is_submitted && c.due_at && !c.on_time) { row.late = true; }
      return row;
    });

    /* ── ⊕ RULED 22 Aug 2026 — P4. IS THIS WEEK'S WORK DONE? ─────────────
       The bench shows THIS WEEK'S assignment, so its state is that one card's
       state — and the work list below the bench was already reading it
       correctly, which is precisely why the two contradicted each other.
       Same field, same card, one answer now. */
    var benchCard = null;
    cards.forEach(function (c) { if (c.id === currentId) { benchCard = c; } });
    var benchDone = !!(benchCard && benchCard.is_submitted);
    var benchMarked = !!(benchDone && benchCard.score != null
                         && benchCard.max_score != null);
    var benchLessons = (currentId && lessonsFor[currentId]) || [];
    var benchLate = !!(benchDone && benchCard.due_at && !benchCard.on_time);

    /* ── the leaderboard: roster[] and weekPts{} ──────────────────────────
       ⛔ BOTH ARE EMPTY, AND THAT IS THE HONEST ANSWER TODAY.

       The page's board is a FOUR-WEEK history: `boardWeeks` offers W01–W04
       and TERM, the leader's "N WEEKS AT THE TOP" walks `weekPts[w]` down
       from the selected week to week 1, and the up/down arrows compare
       against the previous week. Filling any of that needs a points series
       per student per week.

       What exists is `class_stars_leaderboard_for_member`, and it answers a
       different question: THIS week only, ELIGIBLE students only (every piece
       in on time, 75%+), as a percentage rather than points. There is no
       per-week history anywhere — a student cannot read another student's
       submissions (`submissions_self_all`), so the client cannot compute one
       either, and no table stores one.

       Repeating this week's numbers under W01–W03, or zeroing them, would put
       a fabricated result next to a real child's name on a leaderboard their
       class can see. That is the same fault the 21 Aug ruling removed from
       the ON TIME / SCORE / RECALL split bar, and it is not reintroduced here.

       Empty is also SAFE: every read of `weekPts` on the page is inside a map
       over `roster`, so an empty roster never indexes a missing week. The
       board renders with no leader and no chasers until there is a real
       series to show. See the handover — this needs Mide's ruling, not a
       workaround in this file. */
    var roster = [];
    var weekPts = {};

    /* ── lessonDefs[] ────────────────────────────────────────────────────
       This week's lessons, in the order the assignment draws on them. The
       fixture's meta line is lesson PROGRESS ("READ · 4 RUNGS DONE", "NOT
       OPENED") and nothing records whether a lesson has been opened, so the
       meta says the one thing that is true of all of them. */
    var lessonDefs = [];
    var seen = {};
    (current && current.questions ? current.questions : []).forEach(function (q) {
      if (!q.lesson_slug || seen[q.lesson_slug]) { return; }
      seen[q.lesson_slug] = true;
      lessonDefs.push({
        num: pad2(lessonDefs.length + 1),
        name: deslug(q.lesson_slug),
        meta: "SET IN THIS WEEK’S ASSIGNMENT",
        on: true,
        /* ⊕ RULED 22 Aug 2026 — found by the control sweep, not by the brief.
           Each card in "Lessons in this topic" is an `<a href="#top">`, so
           tapping the lesson a student was just told to revise SCROLLED THE
           PAGE TO THE TOP. Same defect as P1/P3/P5/P7 and the fifth of its
           family tonight; it is only here rather than on the punch list
           because nobody had pressed it either. Empty when this build has no
           page for the slug, and the card then keeps Design's inert anchor
           rather than pointing at a 404. */
        href: lessonHref(q.lesson_slug)
      });
    });

    /* ── questions[] — the recall round ──────────────────────────────────
       The lesson ladder's recall and apply rungs for the lessons this class
       has been taught, nearest lesson first. The page's round is six long, so
       six is what it is given. */
    var questions = [];
    (recall && recall.questions ? recall.questions : []).forEach(function (q) {
      if (questions.length >= 6) { return; }
      var n = normalise(q.options, q.answer_letter);
      if (!n) { return; }
      questions.push({
        topic: String(q.topic || deslug(q.lesson_slug)).toUpperCase(),
        a: ["A", "B", "C", "D"][n.a],
        q: q.text || "",
        o: n.o,
        f: n.f
      });
    });
    if (!questions.length) {
      /* The page reads `questions[0]` on its first render, so with nothing to
         recall it cannot draw at all. Say the true thing instead. */
      var e = new Error("no recall questions");
      e.mrbSay = SAY.noRecall;
      throw e;
    }

    /* ── shoutouts[] ─────────────────────────────────────────────────────
       The class's real shout-out feed, narrowed to the ones written TO this
       student (and the ones written to the class as a whole). The card does
       not name a recipient, so a shout-out about somebody else would read on
       this page as if it were about the reader.

       A failure here is not fatal to the page: the shout-out box is one panel
       and the work is the page, so it empties rather than taking the class
       view down with it. */
    var shoutouts = [];
    try {
      var feed = await window.MrBadmusStudentData.loadStudentClassShoutouts(
        klass.id, { limit: 20 });
      shoutouts = (feed.shoutouts || []).filter(function (s) {
        return s.recipient_id == null || s.recipient_id === user.id;
      }).map(function (s) {
        var au = s.author || {};
        var who = ((au.first_name || "") + " " + (au.last_name || "")).trim();
        return {
          who: initials(au.first_name, au.last_name),
          text: s.message || "",
          meta: [who.toUpperCase(), agoText(s.created_at, serverNow)]
            .filter(Boolean).join(" · ")
        };
      });
    } catch (shoutErr) {
      console.error("[student-live] shoutouts", shoutErr);
    }

    /* The teaching week, from the SERVER (both class endpoints compute it
       against the academic year's own dates, never a device clock). The
       denominator is the scheme's own ceiling of 39 weeks, which is what the
       numerator counts against. */
    var weekNo = (current && current.week != null)
      ? current.week
      : (recall && recall.week != null ? recall.week : null);

    var v = detail.viewer || {};

    /* ⊕ 22 Aug 2026 — PHASE 2a. The student's bench theme, onto the page root,
       BEFORE the mount. It is set on `document.documentElement` rather than on
       the `.rd` root because the `.rd` root does not exist yet — the runtime
       draws it — and Design's six `[data-bench-theme="…"]` rules are written
       against whatever ancestor carries the attribute.

       ⚠️ NULL IS A REAL VALUE AND IT MEANS HARBOUR, so a student with no
       preference gets NO ATTRIBUTE. Design's contract is that the attribute
       being ABSENT is harbour, and `:root` in the grafted block already carries
       harbour's values; writing `data-bench-theme="harbour"` here would say the
       same thing in a second place, and the two would disagree the first time
       somebody changed the default in one of them. "No row, no preference, no
       attribute" is ONE state — the same wording the column's own comment
       uses. */
    if (v.bench_theme) {
      document.documentElement.setAttribute("data-bench-theme", v.bench_theme);
    }

    var first = (v.first_name || "").trim();
    var name = klass.name || "";

    /* ⊕ 23 Aug 2026 — PHASE 1b. THE CLASS PAGE GETS A SINK, and until now it
       had none: `makeSink` is built inside `buildAssignment`, so on this page
       `window.__MRB_SINK__` was never set and `_sinkCall` was a permanent
       no-op. The theme picker is the first control on the class view that
       WRITES anything, so it is the first thing that needed one.

       One method, and deliberately not more. A sink is a writer; adding the
       class page's reads to it would put a network object inside the thing the
       page renders from, which is the line this file exists to keep sharp. */
    pendingSink = {
      saveBenchTheme: function (t) {
        return D.saveBenchTheme(user.id, t);
      }
    };

    return {
      work: work,
      roster: roster,
      weekPts: weekPts,
      lessonDefs: lessonDefs,
      questions: questions,

      /* Nothing records a recall streak — no table carries a class, a teaching
         week and a rung together — so the round opens at zero rather than at
         a number that would be made up. */
      streak: 0,

      /* The leaderboard opens on THIS week, not on the week Design drew.
         A number, matching the `wk === MRB_DATA('currentWeek')` comparison the
         scope note makes with `===`. */
      boardWeek: weekNo == null ? 1 : weekNo,

      shoutouts: shoutouts,

      currentWeek: weekNo == null ? 0 : weekNo,
      weekNumber: weekNo == null ? "—" : pad2(weekNo),
      weekTotal: "39",

      className: name,
      /* The template's third occurrence keeps its own indentation; binding it
         to `className` would silently eat the whitespace. */
      classNamePadded: name + "\n        ",
      studentFirstName: first,
      studentInitials: initials(v.first_name, v.last_name),
      welcomeLine: first
        ? "Welcome back, " + first + " · your class"
        : "Welcome back · your class",

      /* COULD NOT SOURCE — a student can read `class_teachers` but has no
         read policy on a TEACHER's `profiles` row (MRB-265, half delivered),
         so the teacher's name is genuinely unreadable from here. "Your
         teacher" is true; a name would be invented. */
      teacherName: "Your teacher",
      teacherInitials: "",

      /* COULD NOT SOURCE — `class_members_self_read` shows a student their own
         membership row and no one else's, so the size of the class cannot be
         counted from the client. Empty, rather than a guess. */
      classSize: "",

      /* ── the docket, and the rest of Design's welded figures ───────────
         ⊕ 22 Aug 2026. Every one of these was a constant in Design's logic —
         "8 questions", "Using a microscope", "Mon 15 Sep", "Thu 18 Sep,
         18:00", "2 days left", "40 POINTS AT STAKE", "58%" — sitting above a
         real assignment of a different length, on a different topic, due on a
         different day. A screenshot caught them; a text check had not,
         because the check held names and no numbers.

         ⛔ WHERE THE PRODUCT DOES NOT RECORD SOMETHING, THE KEY IS EMPTY.
         An empty docket row is honest. "40 POINTS AT STAKE" over an
         assignment with no points is not. */
      docketQuestions: currentCount ? String(currentCount) : "",
      docketDrawsOn: lessonDefs.map(function (l) { return l.name; }).join(" · "),
      docketSet: current && current.assignment
        ? fmtSet(current.assignment.created_at) : "",
      docketDue: current && current.assignment
        ? fmtDueMixed(current.assignment.due_at) : "",
      /* ⊕ RULED 22 Aug 2026 — P4. The docket agrees with the bench.
         `OPEN` was welded, so a finished piece of work still wore it — and
         the countdown beside it went on counting down to a deadline the
         student had already beaten. Once it is done the deadline is not the
         story, so that slot is empty rather than technically-true. */
      docketFlag: benchDone
        ? (benchMarked ? "MARKED" : "COMPLETE")
        : ((benchCard && benchCard.due_at
            && Date.parse(benchCard.due_at) < serverNow) ? "MISSED" : "OPEN"),
      /* Once the work is done the deadline is not the story, and the slot is
         directly above the answered-progress bar — so it LABELS that bar
         instead, which is the other half of the 22 Aug progress ruling
         ("'5 of 15 answered' and the same as a percentage"). An unlabelled
         full bar was what emptying it left behind, and a graphic with no
         words is not an honest blank. */
      docketLeft: benchDone
        ? ((current && current.progress)
            ? current.progress.answered + " of " + current.progress.total
              + " answered" : "")
        : (current && current.assignment
            ? daysLeft(current.assignment.due_at, serverNow) : ""),

      /* ⊕ 22 Aug 2026 — the bench checklist. Design's middle item spelled the
         assignment's length out IN WORDS — "Answer the eight questions" — which
         is why no grep for a digit ever found it, and it sits on the same
         screen as the docket, so once the docket became real the two
         contradicted each other in front of the student. Its last item said
         "Hand it in", which W5 retires along with the button it names. */
      /* ⊕ 22 Aug 2026 — the bench panel's two sentences. Design's read
         "On the bench now · due Thu 18:00" and "Eight questions, set from this
         week's lessons. Open it, answer them, hand it in before Thursday." —
         a fixed day, a fixed time, a count spelled out in words, and a verb
         W5 retires. Both are sentence-case in the markup and upper-cased by
         CSS, which is why every grep for the rendered form found nothing. */
      /* ⊕ RULED 22 Aug 2026 — P4. The eyebrow carries the congratulation,
         because it is the one line of the three that shows at EVERY width —
         Design puts the paragraph below it inside `sc-if wide`, so a phone
         would otherwise get the score and no acknowledgement at all. */
      benchLead: benchDone
        ? ((first ? "Good week, " + first : "Good week")
           + " · completed " + fmtDay(benchCard.submitted_at)
           + (benchLate ? " · late" : ""))
        : (current && current.assignment && current.assignment.due_at
            ? "On the bench now · due " + fmtDueMixed(current.assignment.due_at)
            : "On the bench now"),
      benchBlurb: benchDone
        ? ((benchMarked
             ? "You scored " + benchCard.score + " out of "
               + benchCard.max_score + ". "
             : "It is with your teacher to mark. ")
           + (benchLessons.length
               ? "Go back over the lesson whenever you want, or practise your "
                 + "recall."
               : "Practise your recall whenever you want."))
        : ((currentCount && current && current.assignment
            && current.assignment.due_at)
            ? (currentCount + " questions, set from this week's lessons. " +
               "Open it, answer them, and complete it before " +
               weekdayName(current.assignment.due_at) + ".")
            : "Set from this week's lessons. Open it, answer the questions, "
              + "and complete it."),

      /* W5, in the readings strip. */
      handedLabel: "Completed",
      handedCaption: "OF COMPLETED",

      /* ⊕ RULED 22 Aug 2026 — P4. THE CHECKLIST DOES NOT RENDER when the
         week is done. It is an `sc-for`, and the runtime returns without
         drawing anything for an empty list, so an empty array IS the ruling —
         there is no state flag and nothing to keep in step. */
      benchTasks: benchDone ? [] : [
        { key: "t1", label: "Open it" },
        { key: "t2", label: currentCount
            ? "Answer the " + currentCount + " questions"
            : "Answer the questions" },
        { key: "t3", label: "Complete it" }
      ],

      /* ── ⊕ RULED 22 Aug 2026 — P4, the rest of the done state ──────────
         Two actions: the primary revisits the lesson, and "Practise recall"
         is Design's own second button, already sitting beside it.

         The meter stops counting a three-item checklist that is no longer on
         screen and shows the MARK instead — which is the only percentage a
         finished piece of work has. Unmarked, it is full and says so in
         words: the student's part is complete even though the score is not
         in yet. */
      benchDone: benchDone,
      benchPrimaryLabel: benchDone
        ? (benchLessons.length ? "Revisit the lesson" : "Practise recall")
        : "Open the assignment",
      benchPrimaryHref: benchDone
        ? (benchLessons.length ? benchLessons[0].href : "")
        : ((current && current.assignment) ? assignmentHref() : ""),
      benchPct: benchMarked && benchCard.max_score > 0
        ? Math.round((benchCard.score / benchCard.max_score) * 100) + "%"
        : "100%",
      benchDoneText: benchMarked
        ? (benchCard.score + " / " + benchCard.max_score + " MARKS")
        : "NOT MARKED YET",

      /* COULD NOT SOURCE — nothing anywhere assigns a points value to an
         assignment. `40 POINTS AT STAKE` was a number Design chose for a
         drawing, and there is no column it could be read from. */
      docketWorth: "",

      /* ⊕ This one CAN be real, and the 22 Aug ruling requires it to be:
         "progress is visible all week, to the student and to the teacher —
         '5 of 15 answered' and the same as a percentage". That is exactly
         what the new `progress` block on the payload carries. */
      docketElapsed: current && current.progress
        ? current.progress.percent + "%" : "",

      /* COULD NOT SOURCE — the recall round writes nowhere. `/api/class/recall`
         only reads, and no table carries a class, a teaching week and a rung
         together, so how many a student has answered this week and what
         fraction they got right are both genuinely unrecorded. Design's '46'
         and '77%' were a drawing. Empty until the round has somewhere to
         write; see the handover. */
      recallAnswered: "",
      recallPct: "",
      recallRounds: "",

      /* ⛔ THE FLOOR OF NINE. Design wrote `pad(Math.max(9, st.streak))`, so a
         child whose best streak is three was shown nine. Zero makes the
         Math.max a no-op and the real streak shows through — which today is
         0, because nothing records a streak either. */
      bestStreakFloor: 0,

      /* COULD NOT SOURCE, and deliberately not approximated. Design's sentence
         states an apportionment — "Recall is worth 20 of the 100 points on the
         leaderboard" — that the platform cannot compute, which is the same
         fault the 21 Aug ruling took out of the split bar and its static
         40/40/20 legend. It is also platform self-explanation on a student
         page. Empty rather than restated. */
      roundNote: "",

      /* The status word on an OPEN piece of work. Design wrote 'DUE THU 18:00'
         — one class's one deadline, printed on every open row of every class.
         The precise deadline is already on the line directly below (`detail`
         reads "DUE THU 18 SEP, 18:00"), so the word carries only what is true
         of every open row rather than borrowing one row's time for all of
         them. That matters when a class has two things open at once. */
      dueWordLong: "DUE",
      dueWordShort: "DUE",

      subjectLabel: klass.pill_label || "",
      termLabel: termLabelFrom(serverNow, year),

      /* ── ⊕ 23 Aug 2026 — PHASE 1b. The account sheet's two real rows ────
         Design typed `8r/Sc1 · SCIENCE` and `Summer · Week 01 / 39` into the
         markup of the sheet, one text node each. Both are composed here from
         values this function already holds, so neither is a second source of
         truth for the class, the subject or the week.

         ⚠️ THE SEPARATOR IS DESIGN'S TYPOGRAPHY AND IS CARRIED VERBATIM —
         space, NON-BREAKING space, middle dot, NON-BREAKING space, space. It
         is what stops the subject wrapping onto its own line under a class
         name on a 360px phone. It is not data and it is not decoration to be
         tidied into a plain " · ".

         Each half drops out cleanly when the platform does not have it: no
         subject pill (`class_teachers` carries no subject) leaves the class
         name alone rather than a class name with a dangling dot, and no week
         leaves the term alone. An honest half-row beats a full one with a
         placeholder in it — the same rule the docket rows already follow. */
      accountClassLine: klass.pill_label
        ? name + " \u00a0\u00b7\u00a0 " + String(klass.pill_label).toUpperCase()
        : name,
      accountTerm: (function () {
        var season = seasonOf(termLabelFrom(serverNow, year));
        if (weekNo == null) { return season; }
        return season + " \u00a0\u00b7\u00a0 Week " + pad2(weekNo) + " / 39";
      })(),

      /* ⊕ RULED 22 Aug 2026 — P6. Empty on the live site, and the binding is
         marked `drop`, so the chip's element goes with its text rather than
         leaving an empty bordered box in the header. */
      envBadge: envBadgeText(),

      /* ── ⊕ RULED 22 Aug 2026 — P2. The round is min(6, pool), and every
         count on the page says the size it is going to show ──────────────
         `questions` is already capped at six where it is built, so this IS
         min(6, pool) and needs no arithmetic of its own. When the Physics and
         C4+ banks land the pool passes six, the cap does its job, and all
         four of these say six again with nothing changed. */
      recallBlurb: questions.length
        ? "Questions from the lessons this class has covered. "
          + capitalise(numWord(questions.length))
          + (questions.length === 1 ? " question a round" : " a round")
          + ", unlimited rounds."
        : SAY.noRecall,
      recallEyebrow: questions.length
        ? (numWord(questions.length).toUpperCase() + " QUESTION"
           + (questions.length === 1 ? "" : "S") + " \u00B7 UNLIMITED ROUNDS")
        : "",
      recallOutOf: "OF " + numWord(questions.length).toUpperCase(),
      /* ⊕ RULED 22 Aug 2026. The count is the length of the list it counts. */
      lessonCount: pad2(lessonDefs.length),

      recallCrumb: questions.length
        ? (numWord(questions.length).toUpperCase() + " A ROUND") : "RECALL",
      topicTitle: current && current.assignment
        ? (current.assignment.topic || current.assignment.title || "")
        : ""
    };
  }

  // ── the assignment ────────────────────────────────────────────────────
  async function buildAssignment(klass, token) {
    var current = await api("/api/class/current-assignment?class_id=" + klass.id, token);
    var progress = null;

    /* `assignment: null` with a reason is a NORMAL state — no current week, no
       scheme row, nothing banked yet. It means no work is set, not an error. */
    if (!current || !current.assignment) {
      var none = new Error(current && current.reason ? current.reason : "no assignment");
      none.mrbSay = SAY.noWork;
      throw none;
    }

    var a = current.assignment;

    /* ⊕ 22 Aug 2026 — W2. What this student has already answered, FROM THE
       SERVER, read BEFORE the mount so `resume()` can answer synchronously.
       A failure here is not fatal: an unresumed page shows an empty assignment
       whose answers still save, which is a bad morning rather than a lost
       week. It is logged rather than swallowed. */
    try {
      progress = await api("/api/assignment/progress?assignment_id=" + a.id, token);
    } catch (err) {
      console.error("[student-live] could not read progress", err);
    }

    var questions = [];
    (current.questions || []).forEach(function (q) {
      if (q.retired) { return; }        // the bank no longer has it; do not draw a blank
      var n = normalise(q.options, null);
      if (!n) { return; }
      questions.push({
        /* The row this was built from, kept alongside rather than re-derived:
           the sink needs `question_ref`, the option letters and which one is
           right, and reconstructing those from what the page renders would be
           guessing at data we already have in our hand. Not read by the page —
           `MRB_DATA` never sees it — only by the sink. */
        __src: q,
        t: deslug(q.lesson_slug).toUpperCase(),
        /* ⚠️ ALWAYS null. The page can draw seven figures and seven only, all
           of them Design's own examples keyed `micro` / `bubbles` / `fov` /
           `plant` / `cells` / `scale` / `slot`. A real question's `figure` is
           the id of a figure in its KS3 lesson and never one of those, so
           pointing at it would caption a drawing that is not there. */
        g: null,
        q: q.text || "",
        o: n.o,
        f: n.f,
        a: n.a
      });
    });

    /* ⊕ 22 Aug 2026 — THE FLOOR OF SIX IS GONE, at both ends.
       Design's `count()` returned `Math.max(6, …)` and then indexed that far,
       so a four-question assignment ran off the end of the array and this
       refused to open rather than let it. The refusal was honest and the floor
       was wrong; `count()` now reads the assignment's actual length (see
       student_rulings.py) and this only has to refuse an EMPTY one. */
    if (!questions.length) {
      var short = new Error("assignment has no usable questions");
      short.mrbSay = SAY.workNotSet;
      throw short;
    }

    var name = klass.name || "";
    pendingSink = makeSink(a, questions, progress, token);

    return {
      questions: questions,

      /* Empty on purpose. `wrongPlan` seeds Design's demo scenarios with a
         student's wrong answers; there are none to seed, and inventing three
         would put wrong answers this child never gave in front of them. */
      wrongPlan: {},

      /* Empty on purpose — see `g` above. No figure is drawn, so no figure is
         captioned, and an unmatched key would print nothing anyway. */
      figCaptions: {},

      /* Where this student's own in-progress answers are kept in their
         browser, per assignment. Real ids, so two assignments never collide
         and a new one never resumes the last one's answers. */
      KEY: "mrbadmusai.assignment." +
           name.replace(/[^A-Za-z0-9]/g, "") + "." + a.id + ".v1",
      DUE: fmtDue(a.due_at),

      /* ⊕ 22 Aug 2026 — two values Design welded into one line of `renderVals`.
         `WEEK 04` was every class in every week of every year; a real week is
         the assignment's own `academic_week`, and where there isn't one the
         key is EMPTY and the header simply drops the clause. An empty label is
         honest; "WEEK 04" over week 1 is not. */
      weekLabel: a.academic_week ? "WEEK " + pad2(a.academic_week) : "",
      lateText: lateTextFor(a.due_at, progress && progress.submission
                                      ? progress.submission.completed_at : null),

      className: name,
      backToClass: "Back to " + name,
      topicTitle: a.topic || a.title || "",

      /* ⊕ RULED 22 Aug 2026 — W5. The three words that live in Design's
         MARKUP rather than in its logic, bound by path like every other
         template literal. The padding is Design's own indentation and travels
         with the word; see the note in build_student_port.py's BINDINGS. */
      completeLabel: "Complete\n          ",
      completeChip: "COMPLETE\n          ",
      completeHeading: "Complete"
    };
  }

  // ── go ────────────────────────────────────────────────────────────────
  async function run() {
    var page = whichPage();
    await loadDeps();

    window.MrBadmusStudentGuard.requireStudentRole({
      onAllowed: async function (ctx) {
        try {
          var sb = window.MrBadmusStudentGuard.getClient();
          var session = await sb.auth.getSession();
          var token = session && session.data && session.data.session
            ? session.data.session.access_token : null;
          if (!token) { throw new Error("no access token on the session"); }

          var classes = await window.MrBadmusStudentData.loadStudentClasses(ctx.user.id);
          var klass = pickClass(classes);
          if (!klass) { return say(SAY.noClass); }

          var data = page === "assignment"
            ? await buildAssignment(klass, token)
            : await buildClass(sb, ctx.user, klass, token);

          window.__MRB_DATA__ = data;

          /* ⊕ 22 Aug 2026 — the `#live` history rewrite that used to sit here
             is GONE. It was a workaround, from outside, for the page falling
             back to a demo scenario; the page now refuses every scenario but
             the student's own whenever a sink is present, which is a property
             rather than a nudge. A student typing `#handedin` gets their own
             work, not a fabricated completion.

             The sink goes on the window BEFORE the mount and never after: the
             page reads it lazily but `loadLive()` runs during the very first
             render, and a sink that arrived a tick later would resume nothing
             on the one paint that matters. */
          if (pendingSink) { window.__MRB_SINK__ = pendingSink; }

          window.__MRB_MOUNT__();
        } catch (err) {
          console.error("[student-live]", err);
          if (err && err.mrbSay) { return say(err.mrbSay); }
          if (err && err.code === "class_not_current") { return say(SAY.pastYear); }
          if (err && (err.code === "not_authorised" ||
                      err.code === "class_not_found" ||
                      err.code === "invalid_class_id")) {
            return say(SAY.notMine);
          }
          say(SAY.generic);
        }
      }
      /* No `onDenied`: the guard's own behaviour is the right one. No session
         sends the student to /auth.html with a return path, and a signed-in
         non-student goes home. */
    });
  }

  run().catch(function (err) {
    console.error("[student-live]", err);
    say(SAY.generic);
  });
})();
