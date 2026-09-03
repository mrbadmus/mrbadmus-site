/* ═══════════════════════════════════════════════════════════════════════
   teacher-live.js — the live data source for the ported teacher dashboard.
   MRB-287.

   Claude Design's `Teacher Dashboard.dc.html` is a SAMPLE. Every class in it,
   every student, every mark and every date is invented, seeded from an FNV
   hash of a made-up class id. The prototype is right about SHAPE and wrong
   about everything else, and it is right about shape on purpose: its README
   pins "one number, one source" — one score matrix per class, from which the
   student averages, the paper means, the class mean, the digest mean and the
   question grid are all derived, so no two screens can disagree.

   This file keeps that property and replaces the source. It reads the real
   classes, rosters, assignments, submissions and per-question attempts out of
   Supabase, builds the same primitives Design's `renderVals` consumes, and
   hands them over under the keys the emitted page asks for. Design's
   derivation then runs on top of real numbers without knowing it changed.

   ⛔ NOTHING HERE MAY INVENT A NUMBER. Not an estimate, not an apportionment,
   not a hash, not a plausible default. Where the product does not record
   something, the key comes back EMPTY and the region renders empty, and the
   gap goes in the handover. A bar apportioning marks a student did not earn
   is a lie told in a graph, and it is worse than a blank because a blank
   cannot be quoted at a parents' evening.

   ⛔ AND NO COUNT MAY BE A LITERAL. Design's search box says "Search students
   across all 12 classes"; its crumb rail says "Autumn term · 2026–27"; its
   paper tile says "8 questions, 1 mark each". Twelve, the term, the year and
   the eight are all data. Every one of them is computed here and exported as
   its own key, and the porter's rulings put them where the literals were.

   ── the contract ───────────────────────────────────────────────────────
   `window.MrBadmusTeacherLive`:

     load(screen, params)  async → a plain object of DATA KEYS. The emitted
                           page's `MRB_DATA(k)` THROWS on a key it was not
                           given, deliberately — a missing key is a visible
                           failure, never a silent default — so `load` returns
                           the complete key set on every screen and varies
                           only in how much per-paper detail it fetches.
     grid(classId, idx)    async → one class × question grid, fetched on
                           demand for a paper `load` did not prefetch.
     run()                 the page entry point: load the DEPS, run the
                           teacher guard, build the data, call
                           `window.__MRB_MOUNT__()`. Called at the foot of
                           this file; the page does not call it.

   `screen` is one of: classes | class | student | marking | insights |
   digest | import. `params` carries { classId, studentId, paperIdx,
   chartKind, chartScope, digestScope }.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var HOST_ID = "mrb-teacher";
  var SDK_URL =
    "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js";

  /* The helpers, in the ONE order that works — the same constraint
     student-live.js documents at length, for the same two reasons.
     `teacher-data.js` delegates `workingAcademicYear()` to `class-entry.js`
     and throws a named error if it is not already on the page (CLAUDE.md,
     MRB-267), and `teacher-guard.js` owns the Supabase client that
     `teacher-data.js` asks for. `shoutouts.js` is last because it is the only
     one a screen can survive without. */
  var DEPS = [
    "/shared/config.js",
    "/shared/class-entry.js",
    "/shared/teacher-guard.js",
    "/shared/teacher-data.js",
    "/shared/shoutouts.js"
  ];

  /* ── plain words, for when the page cannot render ───────────────────────
     A teacher is an adult on a working instrument, so these say what is true
     about their classes without apologising and without explaining the
     software to them. Design's rule for the whole surface: "copy is terse and
     functional — no reassurance copy, no platform meta-text." */
  var SAY = {
    generic:    "Your classes could not be loaded. Try again in a moment.",
    slow:       "Your classes did not arrive. Try again in a minute or two.",
    noClasses:  "You are not teaching any classes this year.",
    notMine:    "That class is not one of yours."
  };

  function host() { return document.getElementById(HOST_ID); }

  /* One centred line in the host, in the page's own typeface. Both states
     this file can draw — the boot line and `say()` — are made of it, so they
     cannot drift apart in shape, only in colour.

     Every token carries a literal fallback and that is load-bearing rather
     than defensive: the `--st-*` studio tokens live in a `:root` block inside
     the compiled template and do not exist until the page mounts. */
  function panel(text, state, colour) {
    var wrap = document.createElement("div");
    wrap.setAttribute("data-mrb-state", state);
    wrap.style.cssText =
      "min-height:60vh;display:flex;align-items:center;justify-content:center;" +
      "padding:32px;box-sizing:border-box;";
    var p = document.createElement("p");
    p.style.cssText =
      "margin:0;max-width:38ch;text-align:center;font:400 17px/1.55 " +
      "'Instrument Sans',system-ui,-apple-system,'Segoe UI',sans-serif;" +
      "color:" + colour + ";";
    p.textContent = text;
    wrap.appendChild(p);
    return wrap;
  }

  function say(line) {
    var el = host();
    if (!el) { return; }
    el.textContent = "";
    el.appendChild(panel(line, "unavailable", "var(--st-ink,#2A2018)"));
  }

  /* ── the boot line ─────────────────────────────────────────────────────
     Nothing paints until every request has come back — `__MRB_MOUNT__()` is
     the first thing that draws anything — so without this a slow load is a
     white page indistinguishable from a broken one.

     Two words, and they are the only two that are true before any data has
     arrived. Not a class count, not a term, not a name: this file's own rule
     is that it invents nothing student- or teacher-visible, and at boot there
     is no value it could honestly show.

     It cannot survive the mount. It is a child of the host and both exits
     empty the host first — the runtime's draw opens with `textContent = ""`,
     and `say()` above does the same — so there is no path where a teacher
     sees this line beside real content, including a mount that throws
     half-way, which lands in the catch and calls `say()`. */
  /* ── the skeleton under it ─────────────────────────────────────────────
     ⊕ 27 Aug 2026, the load-performance pass.

     The boot line above solved "is this page broken?" and left "is anything
     still happening?" unanswered: two static words for four and a half seconds
     on a cold load look identical whether the read is in flight or dead. These
     blocks answer the second question the only honest way a page can before it
     has any data — by MOVING.

     ⚠️ IT IS VISUAL, AND IT SAYS NOTHING. Not one word is added. The teacher
     surface's own copy rule is Design's — "terse and functional, no
     reassurance copy, no platform meta-text" — and a skeleton captioned
     "Loading your classes…" would break it just as a spinner's caption would.
     What is drawn is the SHAPE of what is coming, which is true before the
     data arrives because it is a property of the screen and not of the rows.

     ⚠️ AND IT IS HONEST ABOUT BEING EMPTY. Every block is a neutral rule-ruled
     rectangle in the page's own ink at low opacity — no invented counts, no
     placeholder names, no ghost numbers. A teacher can tell at a glance that
     nothing has arrived yet. The instant something has, this is gone: it is a
     child of the same host the boot line is, and both exits (`__MRB_MOUNT__`'s
     `textContent = ""` and `say()`'s) empty the host before they write. There
     is no path on which a shimmer survives beside real content, and none on
     which it survives beside an error — which matters more, because a page
     that shimmers under a sentence saying it failed is worse than either.

     Every token carries a literal fallback for the same reason `panel()`'s do:
     the `--st-*` tokens live in the compiled template's `:root` and do not
     exist until the page mounts. */
  var SKEL_STYLE_ID = "mrb-skel-css";

  function skelStyle() {
    if (document.getElementById(SKEL_STYLE_ID)) { return; }
    var s = document.createElement("style");
    s.id = SKEL_STYLE_ID;
    /* A slow opacity breath rather than a travelling gradient sweep: it is one
       property, it cannot band on a low-colour projector, and it degrades to a
       plain static block when a teacher has asked for less motion — which the
       media query does explicitly rather than leaving to chance. */
    s.textContent =
      "@keyframes mrbSkelPulse{0%,100%{opacity:.34}50%{opacity:.13}}" +
      ".mrb-skel{background:var(--st-ink,#2A2018);border-radius:10px;" +
      "animation:mrbSkelPulse 1.5s ease-in-out infinite}" +
      "@media (prefers-reduced-motion:reduce){" +
      ".mrb-skel{animation:none;opacity:.18}}";
    document.head.appendChild(s);
  }

  function skelBar(h, w, mt) {
    var d = document.createElement("div");
    d.className = "mrb-skel";
    d.style.cssText = "height:" + h + "px;width:" + w + ";" +
                      (mt ? "margin-top:" + mt + "px;" : "");
    return d;
  }

  /* One class card's worth of blocks: the code, the subject pill's line, and
     the two-line footing every card carries. */
  function skelCard() {
    var c = document.createElement("div");
    c.style.cssText =
      "border:1px solid var(--st-rule,rgba(42,32,24,.14));border-radius:14px;" +
      "padding:18px;box-sizing:border-box;";
    c.appendChild(skelBar(15, "52%", 0));
    c.appendChild(skelBar(10, "34%", 12));
    c.appendChild(skelBar(8, "100%", 22));
    c.appendChild(skelBar(8, "72%", 8));
    return c;
  }

  function skeleton(screen) {
    var wrap = document.createElement("div");
    wrap.setAttribute("data-mrb-skeleton", "1");
    wrap.setAttribute("aria-hidden", "true");   // decorative; the heading above
                                                // is the only thing announced
    wrap.style.cssText = "width:100%;max-width:1180px;margin:0 auto;";

    if (screen === "classes") {
      // The landing grid. Six cards, not twelve: enough to read as a grid,
      // never so many that the count itself looks like a claim about how many
      // classes this teacher has.
      var grid = document.createElement("div");
      grid.style.cssText =
        "display:grid;gap:16px;" +
        "grid-template-columns:repeat(auto-fill,minmax(240px,1fr));";
      for (var i = 0; i < 6; i++) { grid.appendChild(skelCard()); }
      wrap.appendChild(grid);
      return wrap;
    }

    // Every other screen — class detail, marking, a student, the digest, the
    // charts — opens with a header band over a list of rows. One shape covers
    // them because that IS the shape they share.
    wrap.appendChild(skelBar(58, "100%", 0));
    var rows = document.createElement("div");
    rows.style.cssText = "margin-top:20px;display:flex;flex-direction:column;gap:10px;";
    var widths = ["100%", "94%", "97%", "88%", "92%", "85%"];
    widths.forEach(function (w) { rows.appendChild(skelBar(30, w, 0)); });
    wrap.appendChild(rows);
    return wrap;
  }

  function boot() {
    var el = host();
    if (!el || el.firstChild) { return; }   // never over the top of anything

    /* One wrapper, so the boot line and the skeleton are a single child of the
       host and cannot be separated. `data-mrb-state="boot"` stays on it — that
       is the attribute the state is read by, and it must keep naming the whole
       boot state rather than half of it. */
    var wrap = document.createElement("div");
    wrap.setAttribute("data-mrb-state", "boot");
    wrap.style.cssText = "padding:40px 32px;box-sizing:border-box;";

    var p = document.createElement("p");
    p.style.cssText =
      "margin:0 0 28px;text-align:center;font:400 17px/1.55 " +
      "'Instrument Sans',system-ui,-apple-system,'Segoe UI',sans-serif;" +
      "color:var(--st-caption,#7A6E63);";
    p.textContent = "My classes";
    wrap.appendChild(p);

    skelStyle();
    wrap.appendChild(skeleton(screenFromLocation()));
    el.appendChild(wrap);
  }

  // ── loading the helpers ───────────────────────────────────────────────

  /* ⚑ THE CACHE-BUST STAMP, FOR THE FILES THIS ONE LOADS ITSELF.

     Every asset under /shared/ is served `max-age=14400, must-revalidate`
     while the pages themselves are `max-age=0`, so a page and the scripts it
     pulls in can be four hours apart, and the failure is silent: an old
     `teacher-data.js` does not error, it just behaves like yesterday — which,
     the day `loadClassMatrices` shipped, means the dashboard asking for a
     function that is not there.

     The stamps cannot live in the DEPS list, because this file is
     hand-written source and the hashes are only knowable at build time. The
     porter publishes them onto the page as `window.__MRB_ASSET_V__`, keyed on
     the BARE FILENAME — keyed on the full path they would themselves be
     rewritten by generate_site_v5.py's cache-bust regex, which matches
     `/shared/<name>"` wherever it occurs, including inside a JSON key.

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

  /* TWO WAVES, NOT SIX — student-live.js's ruling of 23 Aug 2026, and the
     reasoning transfers exactly.

     ⚠️ ONLY PART OF THE ORDER IS REAL. Every cross-file reference in these is
     inside a function body: `teacher-data.js` looks `window.MRBClassEntry` up
     when `workingAcademicYear()` is CALLED and throws a named error if it is
     absent, and it reaches for the guard inside its own loaders. None of that
     runs at evaluation time, so those four can arrive in any order provided
     nothing CALLS them until all four are here — which is what awaiting the
     wave does.

     ⚠️ ONE OF THEM IS NOT LAZY, AND IT IS WHY THIS IS TWO WAVES. `class-entry.js`
     ends by MOUNTING ITSELF, and its `mount()` resolves through `cfg()`, which
     reads `window.MrBadmusConfig` and falls back to the PRODUCTION url and key
     when it is absent. Load it alongside `config.js` and a dashboard running
     against the test project would, intermittently and depending on which
     script won the network, point part of itself at production data. So
     `config.js` goes first, alone, and everything that could read it follows.

     The SDK keeps the first wave rather than taking one of its own: it is the
     slowest of the six, nothing reads `window.supabase` at evaluation time,
     and the one file with a load-time side effect is in the wave after it
     either way. */
  async function loadDeps() {
    var first = [loadScript(DEPS[0])];               // config.js
    if (!window.supabase || !window.supabase.createClient) {
      first.push(loadScript(SDK_URL));
    }
    await Promise.all(first);
    await Promise.all(DEPS.slice(1).map(function (src) {
      return loadScript(src);
    }));
  }

  /* ═════════════════════════════════════════════════════════════════════
     DATES
     ═════════════════════════════════════════════════════════════════════

     ⚠️ BROWSER-LOCAL, NOT London, and that is a decision rather than an
     oversight. `teacher-data.computeWeekWindow` computes the assignment week
     in the BROWSER'S timezone — deliberately, so a UK teacher's "Monday" is
     their local Monday — and every window boundary on this dashboard comes
     from it. Labelling those same windows in a different zone would let a
     range read "17–21 Aug" over a window that started on the 16th. One clock
     for the whole surface; the platform is UK-AQA-only, so the two agree
     anyway except for an hour either side of midnight.

     ⚠️ ONE MONTH ARRAY, AND Intl IS NEVER ASKED TO SPELL A MONTH. `en-GB`'s
     own short name for September is "Sept" — four letters, the only month
     that is not three — so asking Intl for the spelling is one September away
     from a ragged column. student-live.js learned this the hard way on
     24 Aug 2026 with three hand-rolled arrays that could disagree; there is
     one here and it is this one. */
  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  var DAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

  function asDate(iso) {
    if (!iso) { return null; }
    var d = new Date(iso);
    return isNaN(d.getTime()) ? null : d;
  }

  function dayMonth(d) { return d.getDate() + " " + MONTHS[d.getMonth()]; }
  function dowDayMonth(d) { return DAYS[d.getDay()] + " " + dayMonth(d); }
  function dayMonthYear(d) { return dayMonth(d) + " " + d.getFullYear(); }

  /* The Monday and the Friday of the teaching week an instant falls in.
     Sunday is the END of a week to JS (`getDay()` 0) and the START of nothing
     to a school, so it is pulled back to the Monday six days behind it. */
  function teachingWeek(d) {
    var mon = new Date(d);
    mon.setDate(d.getDate() - ((d.getDay() + 6) % 7));
    mon.setHours(0, 0, 0, 0);
    var fri = new Date(mon);
    fri.setDate(mon.getDate() + 4);
    return { mon: mon, fri: fri };
  }

  /* '17–21 Aug' within a month, '28 Aug–1 Sep' across one. Design's own
     format, kept because the week bar's columns are sized for it. */
  function weekRangeLabel(d) {
    if (!d) { return ""; }
    var w = teachingWeek(d);
    return w.mon.getMonth() === w.fri.getMonth()
      ? w.mon.getDate() + "–" + dayMonth(w.fri)
      : dayMonth(w.mon) + "–" + dayMonth(w.fri);
  }

  /* Design's relative-time vocabulary, against real timestamps. Its own list
     ran '9 min ago' … '9 days ago'; anything older than a fortnight is given
     in weeks, because "23 days ago" is a number a teacher has to convert. */
  function relativeTime(iso, now) {
    var d = asDate(iso);
    if (!d) { return ""; }
    var mins = Math.floor((now - d.getTime()) / 60000);
    // A negative gap is clock skew between the device and the server, not a
    // submission from the future. It reads as "just now", which it is.
    if (mins < 1) { return "just now"; }
    if (mins < 60) { return mins + " min ago"; }
    var hours = Math.floor(mins / 60);
    if (hours < 24) { return hours === 1 ? "1 hour ago" : hours + " hours ago"; }
    var days = Math.floor(hours / 24);
    if (days === 1) { return "yesterday"; }
    if (days < 14) { return days + " days ago"; }
    var weeks = Math.floor(days / 7);
    return weeks + " weeks ago";
  }

  function hoursSince(iso, now) {
    var d = asDate(iso);
    return d ? (now - d.getTime()) / 3600000 : null;
  }

  function initialsOf(first, last) {
    var f = (first || "").trim(), l = (last || "").trim();
    if (f && l) { return (f[0] + l[0]).toUpperCase(); }
    if (f) { return f.slice(0, 2).toUpperCase(); }
    if (l) { return l.slice(0, 2).toUpperCase(); }
    return "";
  }

  function fullName(first, last) {
    return [(first || "").trim(), (last || "").trim()].filter(Boolean).join(" ");
  }

  /* The local calendar date of an instant as `YYYY-MM-DD`, so it can be
     compared against an academic year's `start_date` / `end_date` — which are
     plain DATE columns and carry no timezone at all. */
  function ymd(when) {
    var d = new Date(when);
    var m = d.getMonth() + 1, day = d.getDate();
    return d.getFullYear() + "-" + (m < 10 ? "0" + m : m) + "-" +
           (day < 10 ? "0" + day : day);
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE TERM, AND THE YEAR — COMPUTED, NEVER TYPED
     ═════════════════════════════════════════════════════════════════════

     Design's crumb rail reads "Autumn term · 2026–27" as literal text and its
     footer reads "Viewing 2026–27". Both are data: the year is the working
     `academic_years` row's own name and the term falls out of its dates.

     ⚠️ A DATE BEFORE THE YEAR STARTS IS AUTUMN, WEEK 1. Through late August a
     teacher is looking at a year that has not begun — the working-year helper
     picks it precisely so they can set work before term does — and the honest
     answer for the term is the term that is about to start, not the summer
     that has finished. Getting this wrong is not cosmetic: "Summer term ·
     2026–27" over a September timetable is a dashboard that looks stale.

     ⚠️ THIS RULE IS WRITTEN TWICE ON THE PLATFORM. `shared/student-live.js`
     has `termLabelFrom()`, which is the same rule in a page-scoped IIFE with
     no exports, so it cannot be imported and is not going to be hand-synced
     — that is the MRB-267 mistake. Consolidating the two into a shared module
     is a REQUIREMENT recorded in this ticket's handover, not something this
     file can do without editing another. */
  function seasonFor(todayYmd, year) {
    if (year && year.start_date) {
      if (todayYmd < year.start_date) { return "Autumn"; }
      var startYear = Number(String(year.start_date).slice(0, 4));
      if (todayYmd <= startYear + "-12-31") { return "Autumn"; }
      if (todayYmd <= (startYear + 1) + "-03-31") { return "Spring"; }
      return "Summer";
    }
    var m = new Date().getMonth() + 1;
    if (m >= 9 && m <= 12) { return "Autumn"; }
    if (m >= 1 && m <= 3) { return "Spring"; }
    return "Summer";
  }

  /* '2026-27' / '2026/27' / '2026–27' all come back as '2026–27' with the en
     dash the design system sets. A name that is not a year pair is passed
     through untouched rather than reformatted into something the school did
     not call it. */
  function yearLabelOf(year) {
    var name = (year && year.name) || "";
    var m = /^(\d{4})\s*[-–\/]\s*(\d{2,4})$/.exec(String(name).trim());
    if (!m) { return String(name); }
    var b = m[2].length === 4 ? m[2].slice(2) : m[2];
    return m[1] + "–" + b;
  }

  /* Which teaching week of the academic year today is, 1-based, Monday
     aligned. Before the year starts, week 1 — see the ruling above.

     ⚠️ THIS IS A WEEK OF THE YEAR, NOT A WEEK OF THE TERM. "Autumn Week 1"
     reads as term-relative and through the autumn it IS, because the autumn
     term opens the year. From January it drifts: `academic_years` records a
     start and an end and nothing about half terms, so there is no data here
     from which a term-relative week could be derived. Recorded in the
     handover rather than approximated. */
  function academicWeekOf(now, year) {
    if (!year || !year.start_date) { return null; }
    var start = new Date(String(year.start_date) + "T00:00:00");
    if (isNaN(start.getTime())) { return null; }
    var startMon = teachingWeek(start).mon;
    var thisMon = teachingWeek(new Date(now)).mon;
    var weeks = Math.floor((thisMon - startMon) / (7 * 86400000));
    return weeks < 0 ? 1 : weeks + 1;
  }

  /* ⊕ MRB-287, 26 Aug 2026 — EMPTY ON LIVE PRODUCTION, on purpose. Design's
     v2 deleted the permanent PROD chip from the nav, and it was right to: a
     badge that is always there warns of nothing. The badge's real job is the
     other direction — TEST and LOCAL, where a teacher could be driving the
     wrong database — so those still return a word and the ported nav renders
     the chip behind an `if envBadge` that draws nothing on prod. */
  function envBadge() {
    var cfg = window.MrBadmusConfig || {};
    var env = String(cfg.environment || "");
    var h = String(window.location.hostname || "");
    var live = (h === "mrbadmus.com" || h === "www.mrbadmus.com");
    if (live && env === "prod") { return ""; }
    return env ? env.toUpperCase() : "LOCAL";
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE SUBJECT LABEL COMES OFF THE CLASS CODE
     ═════════════════════════════════════════════════════════════════════

     Design's README, and it is a product rule rather than a rendering
     convenience: KS3 `/Sc` → Science, KS4 `/Sc` → Combined Science, `/Ph` →
     Physics, `/Ch` → Chemistry, `/Bi` → Biology. Tier and pathway are
     DELIBERATELY ABSENT from the card — a teacher knows their own set, and
     "Foundation" on a card in front of a child is a label nobody asked for.

     ⚠️ THIS IS NOT `pill_label`. `teacher-data.derivePill` answers a different
     question — which subject the TEACHER is linked to the class for, off
     `class_teachers.subject_id` — and for a KS4 triple class it picks the
     smallest subject_id to stay deterministic. Both are right; they are not
     interchangeable, and the card wants this one.

     ⚠️ A NAME THAT DOES NOT MATCH GETS NO SUBJECT. The class naming convention
     (MRB-263) is year, band letter, slash, subject code, set number — but
     `classes.name` is free text and a school can type anything into it. An
     unparseable name returns "", which is a blank on the card, not a guess.
     Design's `dotsFor("")` falls through to the three-hue pip, so a blank
     currently READS as multi-subject; that is a gap and it is in the
     handover. */
  var SUBJECT_BY_CODE = {
    SC: { KS3: "Science", KS4: "Combined Science", KS5: "Combined Science" },
    PH: { KS3: "Physics", KS4: "Physics", KS5: "Physics" },
    CH: { KS3: "Chemistry", KS4: "Chemistry", KS5: "Chemistry" },
    BI: { KS3: "Biology", KS4: "Biology", KS5: "Biology" }
  };

  function subjectFromCode(name, keyStage) {
    var m = /\/\s*([A-Za-z]{2})/.exec(String(name || ""));
    if (!m) { return ""; }
    var row = SUBJECT_BY_CODE[m[1].toUpperCase()];
    if (!row) { return ""; }
    return row[keyStage] || row.KS4 || "";
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE MATRIX — ONE PER CLASS, AND EVERY NUMBER ON EVERY SCREEN COMES
     FROM IT
     ═════════════════════════════════════════════════════════════════════

     Design's own invariant, kept: a student's average is their row, a paper's
     mean is its column, the class mean is the mean of the marked columns, the
     digest mean is the mean of the class means, and the question grid is
     built from the same marks. Two derivations of one number is how a
     dashboard comes to contradict itself in front of a parent.

     Design's cells are marks out of a fixed 8. Real ones are not: `score` and
     `max_score` are per submission and a paper can be out of anything. So the
     matrix carries FOUR parallel arrays per student instead of one —

       scores[p]  the raw mark, or null where there is no submission
       max[p]     what that mark was out of, or null
       pct[p]     the mark as a percentage, or null
       late[p]    `is_late` as stamped at completion

     — and `pct` exists so nothing downstream has to divide by anything. Every
     `/ 8` in Design's derivation is a sample-data tell and every one of them
     is listed in the handover with the key that replaces it.

     ⚠️ COLUMN 0 IS NOT NECESSARILY THE ONLY OPEN PAPER. Design assumes exactly
     one — index 0 open, 1..n marked — and reaches for `.slice(1)` when it
     wants "the marked ones". Real classes have none open, or three. So the
     aggregates below are computed over `markedIdx`, the indices actually
     closed, and are handed over ready-made: `classMean`, `markedSub`,
     `markedOnTime`, `markedPct` and `studentAvg` are read straight off this
     object by Design's code and need no slicing.                          */
  function buildPapers(pack, now) {
    var roster = pack.members.length;

    /* Newest first — Design's week bar runs oldest-to-newest on screen but
       indexes newest-first, and index 0 is the week it opens parked on.
       due_at DESC with NULLS FIRST, because an assignment with no deadline
       never closes and so belongs at the open end. */
    var list = pack.assignments.slice().sort(function (a, b) {
      if (a.due_at == null && b.due_at == null) {
        return (b.created_at || "").localeCompare(a.created_at || "");
      }
      if (a.due_at == null) { return -1; }
      if (b.due_at == null) { return 1; }
      if (a.due_at !== b.due_at) { return a.due_at < b.due_at ? 1 : -1; }
      return (a.title || "").localeCompare(b.title || "");
    });

    var nowIso = new Date(now).toISOString();
    return list.map(function (a, i) {
      // Open until the deadline passes; an assignment with no deadline never
      // closes, which is what `upcoming` means in teacher-data's own grouping.
      var open = !a.due_at || a.due_at > nowIso;
      var dueD = asDate(a.due_at);
      /* ⊕ RULED 24 Aug 2026 — THE RAIL IS ANCHORED ON `due_at`, AND `set` IS
         DERIVED FROM IT AS due − 7 DAYS.

         The teaching week is still the one the work was SET in rather than the
         one its deadline falls in — that part is Design's rule and it is the
         right one, because a teacher stepping back through the bar is stepping
         back through lessons.

         ⛔ WHAT THIS REPLACES: `asDate(a.created_at) || dueD`. `created_at` is
         the row's insert stamp, not a teaching fact, and a term composed in one
         batch gives every assignment in it the SAME created_at — which
         collapses the whole twelve-week rail onto one range and makes every
         week read as the same week. It fails silently and it fails on exactly
         the data the platform actually has.

         `due_at` is per assignment and real. Design's own `weeks()` already
         worked this way round — it computes the set date FROM the due date
         (`setOn = due − 7`), never the reverse — so this is Design's model on
         real deadlines rather than a new one. `created_at` is still returned
         on the paper for anything that wants the insert stamp; nothing builds
         a week out of it.

         No deadline, no week: the rail entry is blank rather than invented. */
      var setD = null, fri = null;
      if (dueD) {
        setD = new Date(dueD);
        setD.setDate(dueD.getDate() - 7);
        fri = teachingWeek(setD).fri;
      }
      return {
        id: a.id,
        idx: i,
        title: a.title || "",
        // Design prefixes the open paper's date with "Due " and leaves the
        // closed ones bare; `renderVals` strips the prefix back off in three
        // places, so the shape has to be exactly this.
        due: dueD ? (open ? "Due " + dowDayMonth(dueD) : dowDayMonth(dueD)) : "",
        set: setD ? dowDayMonth(setD) : "",
        range: weekRangeLabel(setD),
        dueShort: dueD ? dayMonth(dueD) : "",
        lateShort: fri ? dayMonth(fri) : "",
        due_at: a.due_at,
        created_at: a.created_at,
        academic_week: a.academic_week,
        subject_name: a.subject_name,
        // The ACTIVE roster. NOT the denominator for "submitted" — see
        // `asked`, which decoratePapers fills in once the matrix is built.
        roster: roster,
        when: open ? "upcoming" : "marked"
      };
    });
  }

  function buildMatrix(pack, papers, now) {
    var idxOf = {};
    papers.forEach(function (p) { idxOf[p.id] = p.idx; });
    var cols = papers.length;

    // Who is still on the roll. A submission from anyone else is a DEPARTED
    // student's, and departed students are handled differently in the rows
    // and in the columns — see the ruling below.
    var isActive = {};
    pack.members.forEach(function (m) { isActive[m.student_id] = true; });

    // The current teaching week's papers, from the class's own anchor day.
    // `pack.week` is teacher-data's `computeWeekWindow`, so the dashboard and
    // the class-detail page agree on where the week starts.
    var inWeekPaper = {};
    papers.forEach(function (p) {
      if (p.due_at && p.due_at >= pack.week.start_at && p.due_at < pack.week.end_at) {
        inWeekPaper[p.idx] = true;
      }
    });

    /* ── ONE CELL, FOR ANY STUDENT ─────────────────────────────────────
       Written once and read twice — by the roster rows (active students) and
       by the column aggregates (everyone). Two readings of a submission is
       how a cell and its column come to disagree.

       ⊕ RULED 24 Aug 2026 — LATENESS IS THE STAMP FIRST, THE COMPARISON
       SECOND, AND UNKNOWN THIRD.

       `assignment_submissions.is_late` was added on 22 AUG 2026
       (20260821115131_assignment_submissions_progress_columns.sql) and nothing
       was backfilled, so EVERY row from before that date carries NULL. Reading
       that NULL as `false` — which is what `s.is_late === true` did — quietly
       marks the platform's entire history of late work as on time. It is a
       claim, it is unsupportable, and it is invisible.

       So where the stamp is absent we fall back to the platform's OTHER
       definition of on-time, the one `calcStudentStats` has always used:
       `submitted_at > due_at`. That is not a third rule —
       it is the first rule backfilled with the second, applied exactly where
       the stamp is missing and nowhere else.

       ⚠️ AND WHERE NEITHER IS AVAILABLE, LATE IS `null` — NOT `false`. A
       submission with no stamp and an assignment with no deadline cannot be
       judged either way, and "unknown" must never render as "on time". Every
       count below keeps unknown in its own bucket for that reason.

       String comparison on the two timestamps is deliberate and is the
       assumption the rest of this data layer already runs on: PostgREST hands
       back raw timestamptz strings, for which lexicographic order IS
       chronological order. `pickFirstAttempts` carries the same warning —
       parse these to Date objects and the comparison breaks silently. */
    function cellOf(s, paper) {
      if (!s) { return null; }
      var stamp = s.completed_at || s.submitted_at || null;
      // A row exists from the FIRST ANSWER, not from completion (the 22 Aug
      // 2026 model). An in-progress row is neither submitted nor late.
      var done = !!stamp || s.status === "complete";
      if (!done) { return null; }

      var score = null, max = null, pct = null;
      if (s.score != null && s.max_score != null && s.max_score > 0) {
        score = s.score;
        max = s.max_score;
        pct = Math.round((s.score / s.max_score) * 100);
      }

      var late = null;
      if (s.is_late != null) {
        late = s.is_late === true;
      } else if (stamp && paper && paper.due_at) {
        late = stamp > paper.due_at;
      }

      return {
        stamp: stamp, score: score, max: max, pct: pct,
        late: late, status: s.status || null
      };
    }

    // Every first-attempt submission, indexed by (student, paper). EVERYONE'S
    // — active and departed alike; which of the two a row belongs to is
    // decided at the point of use, not here.
    var byStudent = {};
    pack.submissions.forEach(function (s) {
      var i = idxOf[s.assignment_id];
      if (i == null) { return; }
      if (!byStudent[s.student_id]) { byStudent[s.student_id] = {}; }
      byStudent[s.student_id][i] = s;
    });

    var blank = function () { var a = []; for (var i = 0; i < cols; i++) { a.push(null); } return a; };

    /* ── THE ROWS: ACTIVE MEMBERS ONLY ─────────────────────────────────
       The roster is active-only under the locked rule (MRB-38, Mide,
       9 May 2026). A departed student's marks live in the COLUMNS, where
       they belong, and not in a roster row, where they do not. */
    var rows = pack.members.map(function (m) {
      var sid = m.student_id;
      var mine = byStudent[sid] || {};
      var scores = blank(), max = blank(), pct = blank(), stamp = blank(),
          stampShort = blank(), status = blank(), late = blank(),
          submitted = [];
      var inWeek = false;
      for (var p = 0; p < cols; p++) {
        var c = cellOf(mine[p], papers[p]);
        if (mine[p]) { status[p] = mine[p].status || null; }
        if (!c) { submitted.push(false); continue; }
        /* `submitted[p]` is the honest predicate for "did this student hand
           this in", and it is NOT `scores[p] != null`: a submission with no
           score is handed in and ungraded, which is a different thing from
           missing. Design conflates them because its sample has no ungraded
           work. */
        submitted.push(true);
        scores[p] = c.score;
        max[p] = c.max;
        pct[p] = c.pct;
        // Tri-state: true late, false on time, null not knowable.
        late[p] = c.late;
        status[p] = c.status;
        if (c.stamp) {
          stamp[p] = c.stamp;
          var when = asDate(c.stamp);
          if (when) { stampShort[p] = dayMonth(when); }
        }
        if (inWeekPaper[p]) { inWeek = true; }
      }
      return {
        sid: sid, scores: scores, max: max, pct: pct, late: late,
        stamp: stamp, stampShort: stampShort, status: status,
        inWeek: inWeek, submitted: submitted
      };
    });

    /* ── THE COLUMNS: EVERYONE WHO SAT THE PAPER ───────────────────────
       ⊕ RULED 24 Aug 2026 — DEPARTED STUDENTS COUNT IN THE COLUMNS.

       This is the locked rule from MRB-38 (Mide, 9 May 2026), the same one
       `calcAssignmentStats` implements: an assignment's historical mean must
       not move because a student left the class in February. Excluding them
       here — which is what an earlier draft of this file did, to keep the
       matrix internally tidy — would have given the class-detail page and
       this one two different means for the same assignment, and this one
       would have drifted a little further every time a pupil left.

       ⚠️ THE DENOMINATOR IS `colAsked`, NOT THE ROSTER. That is what made
       excluding them look necessary: `colSub / k.n` reads "31/29" once a
       departed student's submission is counted, and 31 out of 29 looks like a
       bug. The mean was never the problem — the denominator was. `asked` is
       how many students the paper actually went to: the active roster, plus
       any departed student who has a submission for THAT paper. It reads
       "31/31", both numbers are true, and the locked rule holds.

       A departed student with no submission is not counted: we cannot know
       from a `left_at` alone whether they were still in the class when the
       work was set, and adding them to the denominator would invent an
       absence. */
    var everyId = Object.keys(byStudent);
    var colSub = [], colMean = [], colOnTime = [], colLate = [],
        colLateUnknown = [], colMarkedN = [], colAsked = [];

    for (var p = 0; p < cols; p++) {
      /* eslint-disable no-loop-func */
      (function (pi) {
        var sub = 0, on = 0, lt = 0, unk = 0, tot = 0, totMax = 0,
            graded = 0, offRoster = 0;
        everyId.forEach(function (sid) {
          var c = cellOf(byStudent[sid][pi], papers[pi]);
          if (!c) { return; }
          sub += 1;
          if (!isActive[sid]) { offRoster += 1; }
          // Three buckets, never two. An unknown lateness is counted as
          // neither on time nor late, so it cannot be quietly absorbed into
          // whichever of the two the reader happens to be looking at.
          if (c.late === true) { lt += 1; }
          else if (c.late === false) { on += 1; }
          else { unk += 1; }
          if (c.score != null && c.max) { tot += c.score; totMax += c.max; graded += 1; }
        });
        colSub.push(sub);
        colOnTime.push(on);
        colLate.push(lt);
        colLateUnknown.push(unk);
        colMarkedN.push(graded);
        colAsked.push(pack.members.length + offRoster);
        // sum(score)/sum(max), the same definition `calcAssignmentStats` uses,
        // over the same population it uses, so a paper's mean here and on the
        // class-detail page are one number. null — never 0 — when nothing is
        // graded: 0% is a claim about how the class did, and "nothing marked"
        // is not that claim.
        colMean.push(totMax > 0 ? Math.round((tot / totMax) * 100) : null);
      }(p));
      /* eslint-enable no-loop-func */
    }

    var markedIdx = papers.filter(function (p) { return p.when === "marked"; })
                          .map(function (p) { return p.idx; });

    // Per STUDENT, so active rows only — a departed student has no row for an
    // average to sit in. sum(score)/sum(max) over the papers that have closed.
    var studentAvg = {};
    rows.forEach(function (r) {
      var tot = 0, totMax = 0;
      markedIdx.forEach(function (i) {
        if (r.scores[i] != null && r.max[i]) { tot += r.scores[i]; totMax += r.max[i]; }
      });
      studentAvg[r.sid] = totMax > 0 ? Math.round((tot / totMax) * 100) : null;
    });

    var markedSub = 0, markedOnTime = 0, markedLate = 0,
        markedLateUnknown = 0, markedAsked = 0;
    markedIdx.forEach(function (i) {
      markedSub += colSub[i];
      markedOnTime += colOnTime[i];
      markedLate += colLate[i];
      markedLateUnknown += colLateUnknown[i];
      markedAsked += colAsked[i];
    });
    var latenessKnown = markedOnTime + markedLate;

    var meansOfMarked = markedIdx.map(function (i) { return colMean[i]; })
                                 .filter(function (v) { return v != null; });

    var out = {
      rows: rows,
      cols: cols,
      colSub: colSub,
      colAsked: colAsked,
      colMean: colMean,
      colOnTime: colOnTime,
      colLate: colLate,
      colLateUnknown: colLateUnknown,
      colMarkedN: colMarkedN,
      markedIdx: markedIdx,
      studentAvg: studentAvg,
      markedSub: markedSub,
      markedAsked: markedAsked,
      markedOnTime: markedOnTime,
      markedLate: markedLate,
      markedLateUnknown: markedLateUnknown,
      // Out of the submissions whose lateness is KNOWN, not out of all of
      // them. Dividing by `markedSub` would let every un-stamped historic row
      // drag the on-time rate down as though it were late, which is the same
      // unsupported claim as the old `=== true` in the opposite direction.
      // `markedLateUnknown` is beside it so the gap can be shown rather than
      // absorbed.
      markedPct: latenessKnown ? Math.round((markedOnTime / latenessKnown) * 100) : null,
      // Design's README pins this as the mean of the marked COLUMN MEANS
      // rather than a pooled sum/sum, so that the digest's "mean of N class
      // means" is a mean of things that are themselves means. Kept, so the
      // chain from cell to digest stays the one Design documented.
      classMean: meansOfMarked.length
        ? Math.round(meansOfMarked.reduce(function (a, v) { return a + v; }, 0) / meansOfMarked.length)
        : null,
      byId: {}
    };
    rows.forEach(function (r) { out.byId[r.sid] = r; });
    return out;
  }

  /* The two paper fields Design's `papersFor` computes from the matrix, filled
     in once the matrix exists. `sub` is the one that carries the ruling:
     Design writes `mx.colSub[i] + '/' + k.n`, and `k.n` is the ACTIVE roster,
     which is the denominator that made "31/29" possible. It is `colAsked`
     here — submitted out of asked, both true. */
  function decoratePapers(papers, mx) {
    papers.forEach(function (p) {
      p.asked = mx.colAsked[p.idx];
      p.sub = mx.colSub[p.idx] + "/" + mx.colAsked[p.idx];
      p.mean = mx.colMean[p.idx] == null ? "—" : mx.colMean[p.idx] + "%";
      p.onTime = mx.colOnTime[p.idx];
      p.lateN = mx.colLate[p.idx];
      p.lateUnknown = mx.colLateUnknown[p.idx];
    });
    return papers;
  }

  function buildRoster(pack, mx, now) {
    return pack.members.map(function (m) {
      var row = mx.byId[m.student_id] || null;
      var avg = mx.studentAvg[m.student_id];
      var lastIso = null;
      if (row) {
        row.stamp.forEach(function (v) {
          if (v && (lastIso == null || v > lastIso)) { lastIso = v; }
        });
      }
      /* "Never active" is not "active a long time ago", and the two have to
         be told apart. The LABEL says so in words. The HOURS — which only the
         engagement chart reads, to bucket today / this week / 2+ weeks — fall
         back to how long the student has been ON THE ROLL without submitting
         anything, because that is the real elapsed time the chart is for
         ("worth chasing"). It is measured, not invented: two real timestamps.
         The bucket LABELS still say "last seen", which is not quite what this
         measures for a never-active student, and that wording is in the
         handover. */
      var hours = lastIso != null
        ? hoursSince(lastIso, now)
        : hoursSince(m.joined_at, now);
      var missingMarked = mx.markedIdx.some(function (i) {
        return !(row && row.submitted[i]);
      });
      return {
        id: m.student_id,
        name: fullName(m.first_name, m.last_name),
        first_name: m.first_name,
        last_name: m.last_name,
        avatar_url: m.avatar_url,
        avg: avg == null ? null : avg,
        inWeek: !!(row && row.inWeek),
        last: lastIso ? relativeTime(lastIso, now) : "No activity yet",
        lastIso: lastIso,
        hours: hours,
        joined_at: m.joined_at,
        /* Design's own "needs a look" rule, on real inputs: nothing in for
           this week's work, AND either a marked paper they never submitted or
           an average under half. The rule is Design's; only the numbers are
           new. Design's tile subtitle for it reads "Nothing in for two weeks",
           which is not what the rule tests — that mismatch is in the
           handover. */
        flag: !row ? false
          : (!row.inWeek && (missingMarked || (avg != null && avg < 50)))
      };
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE WEEK BAR — INDEXED BY TEACHING WEEK, NOT BY ASSIGNMENT
     ═════════════════════════════════════════════════════════════════════

     ⚑ RULED BY MIDE, 1 Sep 2026 (MRB-306). Design's v3 deleted the class
     screen's week rail; Mide overrode that and kept it: "twelve
     hairline-separated teaching weeks … picking one re-scopes the tiles, the
     roster column and the assignment tables", dated from real academic-year
     weeks. The named ruling is `WEEK_BAR_RESTORED` in `teacher_rulings.py`.

     ⛔ WHAT THIS REPLACES, AND WHY IT IS NOT A REFACTOR. Until today
     `buildWeeks` was `papers.map(...)` — ONE WEEK PER ASSIGNMENT, carrying
     the assignment's own index. That is Design's model, and inside Design's
     fiction it is exactly right: her sample class has one assignment per
     week for twelve weeks, so "week 3" and "the third paper" are the same
     object and nothing can tell them apart.

     They come apart completely on real data. `8r/Sc1` — the only class in
     the working year with any assignments at all — has TWO, against a
     thirty-nine-week year. Carried forward unchanged, the bar would have
     drawn two chips and called them the year, and a teacher stepping back
     through it would have been stepping through papers while reading week
     ranges. Weeks are the axis; papers map ONTO weeks.

     ⚠️ INDEX 0 IS THE WEEK THE BAR OPENS ON, AND THE LIST COUNTS BACKWARDS.
     That is Design's own direction (`wPast = wi > 0`, back = `wi + 1`,
     forward = `wi - 1`) and every consumer still reads it that way. While
     the year is running index 0 is THIS teaching week; in a year that has
     already finished — a teacher browsing 2025-26, which is read-only — it
     is that year's last teaching week, because "this week" is not a fact
     about a year you are only reading.

     ⚠️ NO WEEK FROM BEFORE THE YEAR BEGAN. Twelve is a cap, not a count: a
     year that is four weeks old has four chips, and on the first day of term
     it has one, marked "This week". Offering weeks from before the start
     date would be offering last year's teaching under this year's heading. */

  /* Whole weeks between two Monday-aligned dates.

     ⚠️ ROUNDED, NEVER FLOORED. Two Mondays either side of a clock change are
     7×24h−1h apart, so a floor divides 6.99 weeks down to 6 and every week
     label after the October change is off by one. `academicWeekOf` above
     still floors; that is a pre-existing defect recorded in the handover
     rather than changed under this ticket. */
  function weeksBetween(fromMon, toMon) {
    return Math.round((toMon.getTime() - fromMon.getTime()) / 604800000);
  }

  /* The teaching weeks of one academic year, newest first, at most twelve.

     `term` and the within-term number come from `seasonFor`'s own Sep–Dec /
     Jan–Mar / Apr–Aug boundaries applied to each week's OWN Monday, so
     "Autumn Week 1" is derived from the year's start date and nothing is
     typed. ⚠️ IT IS AN APPROXIMATION AND IT IS NOT A SMALL ONE: `academic_years`
     records a start and an end and NOTHING about half terms, and Easter
     moves, so the count runs straight through the holidays. Half-term weeks
     are counted as teaching weeks because the data cannot say otherwise. A
     `terms` table would make it exact; that is Mide's call and it is in the
     handover. */
  function buildWeeks(year, now) {
    if (!year || !year.start_date) { return []; }
    var startD = new Date(String(year.start_date) + "T00:00:00");
    if (isNaN(startD.getTime())) { return []; }
    var startMon = teachingWeek(startD).mon;

    var topMon = teachingWeek(new Date(now)).mon;
    if (topMon.getTime() < startMon.getTime()) { topMon = startMon; }
    if (year.end_date) {
      var endD = new Date(String(year.end_date) + "T00:00:00");
      if (!isNaN(endD.getTime())) {
        var lastMon = teachingWeek(endD).mon;
        if (topMon.getTime() > lastMon.getTime()) { topMon = lastMon; }
      }
    }
    var elapsed = weeksBetween(startMon, topMon) + 1;      // 1 on day one
    var count = Math.max(1, Math.min(12, elapsed));

    // Term numbering has to be counted FROM THE START OF THE YEAR, not from
    // the first chip: the twelfth week back is not the first week of its term
    // just because the bar stops there.
    var termN = {}, numberOf = {};
    for (var w = 0; w < elapsed; w += 1) {
      var m = new Date(startMon);
      m.setDate(startMon.getDate() + w * 7);
      var t = seasonFor(ymd(m), year);
      termN[t] = (termN[t] || 0) + 1;
      numberOf[ymd(m)] = { term: t, n: termN[t], week: w + 1 };
    }

    var thisMonYmd = ymd(teachingWeek(new Date(now)).mon);
    var out = [];
    for (var i = 0; i < count; i += 1) {
      var mon = new Date(topMon);
      mon.setDate(topMon.getDate() - i * 7);
      var fri = new Date(mon);
      fri.setDate(mon.getDate() + 4);
      var meta = numberOf[ymd(mon)] || { term: seasonFor(ymd(mon), year), n: 1, week: 1 };
      out.push({
        idx: i,
        weekOfYear: meta.week,
        term: meta.term,
        // "Autumn Week 1" — the chip's second line, and the sentence under
        // the bar. "This week" replaces it on the week a teacher is in.
        label: meta.term + " Week " + meta.n,
        // Design's own range format, which the chips are sized for.
        range: weekRangeLabel(mon),
        now: ymd(mon) === thisMonYmd,
        monYmd: ymd(mon),
        friYmd: ymd(fri)
      });
    }
    return out;
  }

  /* Which teaching week each assignment belongs to, written onto the paper as
     `weekIdx` — the same index the bar is keyed on.

     ⚑ `academic_week` FIRST, BECAUSE IT IS THE AUTHORED INTENT. Where the
     scheme of work put a number on the assignment, that number is the answer
     and nothing is derived. Only where it is NULL is the week worked out from
     the deadline.

     ⚠️ AND THE DERIVATION IS `due_at − 7`, NOT `created_at`. That is this
     file's own ruling of 24 Aug 2026, recorded on `buildPapers`, and it is
     the opposite of what the week-bar brief asked for: `created_at` is the
     row's insert stamp, so a term composed in one sitting gives every
     assignment in it the same one and the whole bar collapses onto a single
     week. It fails silently and it fails on exactly the data the platform
     has. Both rules agree on the two real assignments in the working year, so
     nothing observable turns on the choice today — but only one of them keeps
     agreeing once a teacher plans a term in an afternoon.

     ⚠️ A DATE BEFORE THE YEAR STARTS IS WEEK 1 — Mide's ruling, and it is the
     live default rather than an edge case: both real assignments on `8r/Sc1`
     were set in late August against a year that began on 1 September.

     ⚠️ A WEEK STILL AHEAD IS A NEGATIVE INDEX, DELIBERATELY. Teachers set work
     forward; clamping it back onto this week would date it wrongly, and
     dropping it would hide work that has been set. The class screen buckets
     everything at or ahead of the current week into the current week's view,
     so nothing ever vanishes, and the paper's own due date still says when it
     is for. An assignment with NO deadline and no `academic_week` has no week
     to be in and is treated the same way: it never closes, so it is open now. */
  function assignPaperWeeks(papers, weeks, year, now) {
    var topWeek = weeks.length ? weeks[0].weekOfYear : null;
    var startMon = null;
    if (year && year.start_date) {
      var d = new Date(String(year.start_date) + "T00:00:00");
      if (!isNaN(d.getTime())) { startMon = teachingWeek(d).mon; }
    }
    papers.forEach(function (p) {
      var wk = null;
      if (p.academic_week != null) {
        wk = Math.max(1, Number(p.academic_week));
      } else if (p.due_at && startMon) {
        var setD = asDate(p.due_at);
        if (setD) {
          setD.setDate(setD.getDate() - 7);
          wk = Math.max(1, weeksBetween(startMon, teachingWeek(setD).mon) + 1);
        }
      }
      /* NULL, NOT ZERO. A paper with no deadline and no `academic_week` has
         no week to be in, and saying "week 0" would be a claim rather than an
         absence. The class screen buckets a null into the current week — it
         never closes, so it is open now — but it does so knowingly, and
         anything else reading `weekIdx` can still tell the two apart. */
      p.weekOfYear = wk;
      p.weekIdx = (wk == null || topWeek == null) ? null : (topWeek - wk);
    });
    return papers;
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE CLASS × QUESTION GRID
     ═════════════════════════════════════════════════════════════════════

     Design INVENTS this: it takes each student's total mark, hashes eight
     fake question stems into a difficulty order, and lights up however many
     cells the mark says. The cells are consistent with the total by
     construction and correspond to nothing a student did. This builds it from
     `assignment_question_attempts` — what each student actually answered.

     ⚖️ THERE ARE FOUR STATES, NOT THREE. Design draws 1 correct, 0 incorrect,
     2 not attempted. `is_correct` is NULLABLE and NULL IS NOT FALSE: a
     self-marked or written response records no correctness claim, because the
     platform cannot know — a student can tick every criterion on gibberish.
     The column's NOT NULL was dropped on 20 Aug 2026 precisely so an honest
     row could exist. So NULL gets its OWN value, 3, and it must never be
     folded into 0 (a claim they got it wrong), into 2 (a claim they did not
     answer) or into 1.

         1  correct            2  not attempted
         0  incorrect          3  answered, not machine-marked   ← new

     ⚠️ `cellStyle(3)` DOES NOT EXIST YET. Design's `cellStyle` returns the
     dash for anything that is not 1 or 0, so a 3 currently draws as "not
     attempted" — which is exactly the misreading the state was added to
     prevent. Drawing the fourth glyph is a REQUIREMENT in the handover.

     ⚠️ AND THE JOIN IS BY ORDINAL, BECAUSE THERE IS NO KEY. `assignment_questions`
     carries `source_ref`, a LESSON path plus a rung; an attempt carries
     `question_ref`, the bank's per-question id. Different namespaces, by
     design — "a rung name is a difficulty, not a question". What lines them
     up is order: `question_index` is the 0-based index into the questions as
     the student was served them, and the server serves them `position` ASC.
     Where an attempt's index falls outside the question list the column is
     still created from the attempt, so a paper whose question rows were never
     written still produces a grid.

     ⚠️ `rung` IS CARRIED AND NEVER GROUPED ON. It rides along on each column
     as that one question's descriptor. Any breakdown BY rung — a recall
     split, a per-rung mean, a skills chart — is out, ruled: the recall round
     records nothing yet, so a split would be drawn from one corpus and read
     as covering both.                                                      */
  function buildGrid(roster, qpack) {
    var attempts = (qpack && qpack.attempts) || [];
    var questions = (qpack && qpack.questions) || [];
    var subs = (qpack && qpack.submissions) || [];

    var maxIdx = -1;
    attempts.forEach(function (a) {
      if (a.question_index != null && a.question_index > maxIdx) { maxIdx = a.question_index; }
    });
    var cols = Math.max(questions.length, maxIdx + 1);

    // One bucket per column, filled from the attempts, so a column's stem
    // text is the snapshot the students actually saw rather than anything
    // reconstructed. An unanswered question has no snapshot and so no text —
    // blank, not a placeholder.
    var stems = [];
    for (var i = 0; i < cols; i++) {
      var q = questions[i] || null;
      var mine = attempts.filter(function (a) { return a.question_index === i; });
      var text = "";
      var refTally = {};
      mine.forEach(function (a) {
        if (!text && a.question_text) { text = String(a.question_text); }
        if (a.question_ref) { refTally[a.question_ref] = (refTally[a.question_ref] || 0) + 1; }
      });
      var refs = Object.keys(refTally);
      refs.sort(function (x, y) { return refTally[y] - refTally[x]; });
      stems.push({
        id: "Q" + (i + 1),
        idx: i,
        text: text,
        question_ref: refs[0] || null,
        // Two different bank questions answered at the same ordinal means the
        // paper was recomposed between attempts and the column is comparing
        // apples with pears. Surfaced rather than averaged over.
        refConflict: refs.length > 1,
        source_ref: q ? q.source_ref : null,
        rung: q ? q.rung : (mine[0] ? mine[0].rung : null),
        position: q ? q.position : null
      });
    }

    var subByStudent = {};
    subs.forEach(function (s) { subByStudent[s.student_id] = s; });
    var attemptsBySub = {};
    attempts.forEach(function (a) {
      if (!attemptsBySub[a.submission_id]) { attemptsBySub[a.submission_id] = {}; }
      attemptsBySub[a.submission_id][a.question_index] = a;
    });

    var correctN = [], markedN = [], nullN = [], blankN = [];
    for (var c = 0; c < cols; c++) { correctN.push(0); markedN.push(0); nullN.push(0); blankN.push(0); }

    var submitted = 0;
    var rows = roster.map(function (r) {
      var s = subByStudent[r.id];
      var handedIn = !!(s && (s.completed_at || s.submitted_at || s.status === "complete"));
      var base = {
        id: r.id,
        name: r.name,
        initials: initialsOf(r.first_name, r.last_name),
        hue: hueFor(r.name)
      };
      if (!handedIn) {
        return Object.assign(base, {
          raw: stems.map(function () { return 2; }),
          score: "—",
          submitted: false
        });
      }
      submitted += 1;
      var mine = attemptsBySub[s.id] || {};
      var raw = stems.map(function (st, qi) {
        var a = mine[qi];
        if (!a) { blankN[qi] += 1; return 2; }               // never answered
        if (a.is_correct === true) { correctN[qi] += 1; markedN[qi] += 1; return 1; }
        if (a.is_correct === false) { markedN[qi] += 1; return 0; }
        nullN[qi] += 1;                                       // answered, unmarkable
        return 3;
      });
      return Object.assign(base, {
        raw: raw,
        score: (s.score != null && s.max_score != null)
          ? s.score + "/" + s.max_score
          : "—",
        submitted: true
      });
    });

    /* The denominator is the answers that WERE machine-marked, not everyone
       who handed the paper in. Dividing by `submitted` would count a written
       answer nobody can mark as a wrong one, which is the same lie in
       aggregate that state 3 exists to prevent per cell. `null` — never 0 —
       when there is nothing to divide by. */
    var qpct = stems.map(function (st, i) {
      return markedN[i] ? Math.round((correctN[i] / markedN[i]) * 100) : null;
    });

    var maxScore = null;
    subs.forEach(function (s) { if (s.max_score != null) { maxScore = s.max_score; } });

    return {
      rows: rows,
      qpct: qpct,
      stems: stems,
      submitted: submitted,
      roster: roster.length,
      qcount: cols,
      maxScore: maxScore,
      qCorrect: correctN,
      qMarked: markedN,
      // How many answers at this question could not be machine-marked, and
      // how many were left blank. Both are real facts about the paper and the
      // teacher wants them; neither may be quietly folded into the percentage.
      qUnmarkable: nullN,
      qBlank: blankN,
      // "8 questions, 1 mark each" is Design's literal. Real papers are not
      // all one mark a question, so the sentence is built from what the paper
      // is actually out of, and is blank when we do not know.
      qLine: !cols ? ""
        : (maxScore == null
            ? cols + (cols === 1 ? " question" : " questions")
            : (maxScore === cols
                ? cols + (cols === 1 ? " question, 1 mark" : " questions, 1 mark each")
                : cols + (cols === 1 ? " question, " : " questions, ") + maxScore + " marks"))
    };
  }

  /* Design's avatar tint, replicated here because `gridFor` is data-backed
     and its rows carry the colour. This is FNV-1a over the name into Design's
     own six-swatch palette — a colour, not a number about a child, and the
     one thing in this file that is allowed to come out of a hash. Kept
     identical to Design's `hueFor` so a student is the same colour in the
     grid as in the roster, which the roster gets from Design's own copy. */
  var HUE = ["#2F5CE0", "#A93411", "#0A6B36", "#5A31C0", "#7A5F00", "#2545A8"];

  function hueFor(name) {
    var h = 2166136261, s = String(name || "");
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = (h * 16777619) >>> 0; }
    return HUE[(h >>> 0) % HUE.length];
  }

  /* ═════════════════════════════════════════════════════════════════════
     WHICH SCREEN AM I ON?
     ═════════════════════════════════════════════════════════════════════

     ⊕ FIXED 24 Aug 2026 — THE SCREEN IS THE PATH, NOT A QUERY PARAMETER.

     ⛔ WHAT THIS REPLACES: `q.get("screen") || "classes"`. There is no
     `?screen=` anywhere and nothing emits one, so EVERY page loaded as
     "classes".

     ⚠️ AND IT DID NOT CRASH, WHICH IS WHY IT HAD TO BE FOUND BY READING. The
     porter pins the visible screen per page in the LOGIC rewrite, so the
     markup rendered correctly whatever this returned; the only thing that was
     wrong was the PREFETCH. `/teacher/assignment.html` drew the marking screen
     with no `GRID` prefetched and `/teacher/insights.html` drew the charts
     with no per-class grids, both then hit the deliberate `null` that means
     "not fetched yet", and a teacher got a page that stayed pending for ever
     with no error in the console and no error on screen — on a page that
     works perfectly in the fixture, where the data is handed over whole.

     The port emits one page per screen at its own URL, so the URL is the
     source of truth. `?screen=` survives as an explicit override for testing
     only. An unrecognised path falls back to "classes", which is the one
     screen that needs nothing prefetched and so cannot strand anybody. */
  var SCREEN_BY_PAGE = {
    "classes":        "classes",
    "class-detail":   "class",
    "student-detail": "student",
    "assignment":     "marking",
    "digest":         "digest",
    "import":         "import",
    "insights":       "insights"
  };

  function screenFromLocation() {
    var q = new URLSearchParams(window.location.search);
    var override = q.get("screen");
    if (override && SCREEN_BY_PAGE[override]) { return SCREEN_BY_PAGE[override]; }
    // An override may also name the SCREEN directly rather than the page.
    if (override) {
      for (var k in SCREEN_BY_PAGE) {
        if (SCREEN_BY_PAGE[k] === override) { return override; }
      }
    }
    var last = String(window.location.pathname || "").split("/").pop() || "";
    var base = last.replace(/\.html?$/i, "");
    return SCREEN_BY_PAGE[base] || "classes";
  }

  /* A paper index, or null. `?paper=` arrives as a STRING and three of its
     values are traps: `""` becomes 0 under `Number`, so an empty parameter
     would silently select the first paper; `"abc"` becomes NaN, which indexes
     nothing and stringifies into a `"<classId>:NaN"` cache key that can never
     be filled; and `"3.5"` would key differently from `3`. So the parse is
     strict — a non-negative integer or nothing — and EVERY entry point runs a
     value through it, so `"3"` and `3` cannot produce two different keys for
     one grid. */
  function paperIndex(v) {
    if (v == null || v === "") { return null; }
    var n = Number(v);
    if (!isFinite(n) || Math.floor(n) !== n || n < 0) { return null; }
    return n;
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE READ, MEMOISED
     ═════════════════════════════════════════════════════════════════════

     `load()` is called again on every screen change — the dashboard is one
     component switching `state.screen`, not seven pages — so the expensive
     reads happen once and are held. Two things are deliberately NOT held: the
     shoutout feed, which a teacher can post to and must see change, and the
     per-paper grids, which are keyed and accumulate.

     `reload()` drops everything; the porter calls it after a write.        */
  var cache = null;
  var profile = null;      // survives reset(): a re-read of rows is not a
                           // re-authentication, and the guard hands the
                           // profile over exactly once.
  /* ⊕ MRB-287, 24 Aug 2026 — the signed-in teacher's own auth id.

     Held for the same reason and on the same terms as `profile`: the guard
     validates the session once and hands `ctx.user` over once, so asking
     Supabase again would be a second answer to a question already answered.

     ⚠️ IT IS AN IDENTITY, NOT A PERMISSION. Nothing on the page may gate a
     WRITE on it — RLS does that, in the database, and `class_shoutouts`'s
     UPDATE policy is `author_id = auth.uid() AND
     auth_user_teaches_class(class_id)`. What it gates is whether a control
     is OFFERED: the shoutout delete appears only on a shoutout this teacher
     wrote, so that nothing on the page looks pressable and then fails RLS.
     Null when unknown, which offers nothing — the safe direction. */
  var viewerId = null;

  function reset() { cache = null; }

  /* ⊕ MRB-287 E1 — THE ACADEMIC YEAR BEING VIEWED.
     ...
     ⚠️ THIS IS NOT PERSISTENCE, AND MRB-261's RULING IS INTACT. The retired
     hand-written page held the selection in a plain local and said why:
     "a teacher who looked at 2025-26 on Friday lands on 2026-27 on Monday.
     Persisting it would silently hand someone a historical dashboard they
     believed was current." That property is unchanged — `run()` reads the
     year off the URL and nothing writes it anywhere, so a bare
     `/teacher/classes.html` resolves the WORKING year on every load, exactly
     as before.

     What a local cannot do is survive a NAVIGATION, and Design's one file is
     six URLs here. That is the same seam that left the week rail parked on
     June for a page opened cold. `teacher-data.loadTeacherClasses` already
     anticipates the caller naming a year — "the grid does, when a teacher has
     opened a past year" — and this is the grid doing it.                  */
  var selectedYearId = null;

  /* The year list, read once per page load. `base()` is dropped and rebuilt
     when the selection changes, and asking Supabase again for a list that
     cannot have moved inside one page load is a second answer to a settled
     question. */
  /* ⊕ 27 Aug 2026 — THE PROMISE IS CACHED, NOT THE RESULT. It used to be
     `yearsCache = await ...`, which dedupes two SEQUENTIAL callers and not two
     CONCURRENT ones: both would find the local still null and both would fire
     the query. `run()` now starts this read alongside the guard rather than
     after it, so concurrent callers are the normal case and not the exception.

     A rejection is not cached. The local is cleared on the way out, so a read
     that failed while the guard was still validating does not become the
     answer `base()` gets handed a second later — it simply asks again. */
  var yearsCache = null;
  function yearIndex() {
    if (!yearsCache) {
      yearsCache = window.MrBadmusTeacherData.loadAcademicYears()
        .catch(function (e) { yearsCache = null; throw e; });
    }
    return yearsCache;
  }

  /* Which year a URL is asking for, or the working one.

     ⚠️ A `?year=` NAMING A YEAR THAT DOES NOT EXIST IS NOT AN ERROR AND IS
     NOT HONOURED, and neither is a FUTURE one: a school that has created
     2027-28 early must not be viewable through a hand-typed URL, which is the
     same rule `loadAcademicYears` already applies when it tags a year
     `is_future` rather than `is_past`. Both fall through to the working year,
     which is where a bare URL lands — a wrong parameter gets you the right
     dashboard, never a blank one. */
  function pickYear(idx, wanted) {
    var hit = null;
    if (wanted) {
      (idx.years || []).forEach(function (y) {
        if (y.id === wanted && !y.is_future) { hit = y; }
      });
    }
    return hit || idx.working || null;
  }

  async function base() {
    if (cache) { return cache; }
    var TD = window.MrBadmusTeacherData;

    // The year first, on its own, because everything else is scoped by it and
    // because the year selector needs the full list. NEVER `is_current` and
    // never a bare `end_date >= today` — `workingAcademicYear` owns that rule
    // and carries the reasoning (MRB-261 / MRB-267).
    var years = await yearIndex();
    var viewing = pickYear(years, selectedYearId);
    selectedYearId = viewing ? viewing.id : null;

    /* The authorised, year-scoped class list. Reused rather than re-queried:
       this is the one function that knows which classes a teacher holds in a
       given year, and a second implementation of that is a second answer.

       ⊕ 27 Aug 2026 — `{ metrics: false }`, AND IT IS THE N+1 THIS PAGE WAS
       PAYING FOR NOTHING. `loadTeacherClasses` used to fan out four requests
       per class — a `class_members` count, an `assignments` list, a
       submissions count and a submissions max — and on a teacher with twelve
       classes that is up to forty-eight, in one serial wave, before the line
       below has asked for anything.

       Not one of the five numbers they produced was ever read. Look at the
       map below: every field this function takes off `c` is an identity
       (`name`, `year_group`, `key_stage`, `tier`, `pill_label`, the year), and
       every COUNT it publishes comes from `pack` — `pack.members.length`,
       `papers.length`, the roster's own `lastIso`. `loadClassMatrices` on the
       next line re-reads the same members, assignments and submissions IN
       BULK, four chunked requests for all twelve classes together, because
       that is what every screen in the redesign derives from.

       So the fan-out was forty-eight requests to compute five numbers that
       were then overwritten by better ones. They are filled back in below
       from the bulk data, so `cache.classRows` — which is exposed — still
       carries real values rather than the nulls the opt-out hands back. */
    var classRows = await TD.loadTeacherClasses(selectedYearId, { metrics: false });
    var classIds = classRows.map(function (c) { return c.id; });

    var packs = classIds.length ? await TD.loadClassMatrices(classIds) : {};

    /* The five deferred numbers, from the bulk read that superseded them. Done
       before anything reads `classRows` so no consumer — here, a ruling, or a
       future screen — can meet a `metrics_deferred` null. */
    classRows.forEach(function (c) {
      if (!c.metrics_deferred) { return; }
      // No pack means no data to derive from, and `loadClassMatrices` throws
      // rather than omitting a class, so this cannot happen. If it ever did,
      // the flag STAYS — a reader must keep being able to tell "not fetched"
      // from "genuinely zero", and clearing it here would erase exactly that.
      var pack = packs[c.id];
      if (!pack) { return; }
      var m = TD.deriveClassMetrics(pack);
      c.student_count = m.student_count;
      c.assignment_count = m.assignment_count;
      c.submission_count = m.submission_count;
      c.completion_pct = m.completion_pct;
      c.last_activity_at = m.last_activity_at;
      delete c.metrics_deferred;
    });

    var now = Date.now();
    var CLASSES = [], MATRIX = {}, ROSTER = {}, PAPERS = {}, WEEKS = {};

    /* ⊕ MRB-306 — ONE WEEK LIST FOR THE WHOLE PAGE, keyed per class because
       that is the shape `weeks()` reads (`MRB_PICK('WEEKS', k.id)`). The
       weeks are the VIEWED academic year's, not the working one: a teacher
       reading 2025-26 is reading that year's teaching weeks, and its last
       week — not this one — is the week the bar opens on. Every class on a
       page is in the year being viewed, so the list is computed once and
       shared by reference rather than rebuilt twelve times. */
    var yearWeeks = buildWeeks(viewing, now);

    classRows.forEach(function (c) {
      var pack = packs[c.id];
      if (!pack) { return; }                       // cannot happen: it throws
      var papers = buildPapers(pack, now);
      assignPaperWeeks(papers, yearWeeks, viewing, now);
      var mx = buildMatrix(pack, papers, now);
      decoratePapers(papers, mx);      // `sub` / `mean` / `asked`, from the matrix
      var roster = buildRoster(pack, mx, now);

      PAPERS[c.id] = papers;
      MATRIX[c.id] = mx;
      ROSTER[c.id] = roster;
      WEEKS[c.id] = yearWeeks;

      // Which of the three shapes this class is in. Design's states, and the
      // order matters: no roster beats no work, because a class with neither
      // needs the roster first and its card offers Import, not Set work.
      var state = pack.members.length === 0 ? "empty"
                : (papers.length === 0 ? "nowork" : "live");

      // The current teaching week's return: how many students have handed in
      // this week's work, out of the roster. Both real; `week[0]` is 0 for a
      // class with no work due this week, which is honest — nobody was asked.
      var inWeekN = roster.filter(function (r) { return r.inWeek; }).length;

      var lastIso = null;
      roster.forEach(function (r) {
        if (r.lastIso && (lastIso == null || r.lastIso > lastIso)) { lastIso = r.lastIso; }
      });

      CLASSES.push({
        id: c.id,
        code: c.name,
        year: c.year_group,
        ks: c.key_stage,
        // Off the class CODE, per Design's README — not `pill_label`, which
        // answers a different question. See subjectFromCode.
        subject: subjectFromCode(c.name, c.key_stage),
        n: pack.members.length,
        week: [inWeekN, pack.members.length],
        last: lastIso ? relativeTime(lastIso, now) : "No activity yet",
        lastIso: lastIso,
        state: state,
        // Carried but not part of Design's shape: the porter's rulings may
        // want them and re-deriving them would be a second answer.
        tier: c.tier,
        science_pathway: c.science_pathway,
        pill_label: c.pill_label,
        academic_year_id: c.academic_year_id,
        /* ⊕ MRB-287 E1 — THE CARD'S OWN YEAR, and it was being dropped here.
           `teacher-data.js` has returned `academic_year_name` since MRB-261;
           this map carried the id and not the name, so the card had nothing
           to state and the porter's ruling reached for the DASHBOARD's year
           instead. Right while the working year is the only one you can open,
           wrong the moment a past year is — twelve cards from 2025-26 each
           saying 2026-27.

           The retired page put it on every card and recorded the reason:
           10H/Ph1 and 11h/Ph1 are the same 17 students a year apart, and with
           no year on the card they read as a duplicate.

           Empty when the school has not named the year — the card drops the
           part rather than printing "undefined". */
        yearName: c.academic_year_name || "",
        departed: pack.departed_count,
        assignment_count: papers.length
      });
    });

    // Class code order, natural-number aware, so 9h/Sc5 comes before 10h/Ph1.
    CLASSES.sort(function (a, b) {
      return String(a.code).localeCompare(String(b.code), undefined, { numeric: true });
    });

    /* Every year a teacher may switch INTO, newest first, minus the one they
       are already looking at.

       ⚠️ THE CURRENT YEAR IS EXCLUDED ON PURPOSE, and it is not tidiness.
       Included, it would have to render as a disabled row with no handler —
       and `student-runtime.js` looks a handler up THROUGH the miss recorder
       (`lookup(node.on, scope, ctx.miss)`), so a looped button with no `on`
       writes `data-mrb-misses` and fails `teacher_behaviour`'s own binding
       check. Design's node 84 already names the year in view; this list is
       the years you can go TO, so every row rendered is pressable.

       ⚠️ AND FUTURE YEARS ARE NOT OFFERED. A school that has created 2027-28
       early has no classes in it and nothing to show; `loadAcademicYears`
       tags it `is_future` for exactly this. */
    var options = (years.years || []).filter(function (y) {
      return !y.is_future && y.id !== selectedYearId;
    }).map(function (y) { return { id: y.id, name: y.name }; });

    cache = {
      now: now,
      years: years,
      viewing: viewing,
      yearOptions: options,
      classRows: classRows,
      packs: packs,
      CLASSES: CLASSES,
      MATRIX: MATRIX,
      ROSTER: ROSTER,
      PAPERS: PAPERS,
      WEEKS: WEEKS,
      GRID: {}
    };
    return cache;
  }

  /* One paper's grid, fetched on demand and held. The key is the same one
     Design's own cache uses — `<classId>:<paperIdx>` — so a ruling that
     replaces `gridFor`'s body is a one-line lookup. */
  async function grid(classId, paperIdx) {
    var c = await base();
    // Canonicalised HERE as well as at the callers, so a ruling that calls
    // `grid()` with a raw query value cannot mint a second key for one paper.
    var idx = paperIndex(paperIdx);
    if (idx == null) { return null; }
    var key = classId + ":" + idx;
    if (c.GRID[key]) { return c.GRID[key]; }
    var papers = c.PAPERS[classId] || [];
    var paper = papers[idx];
    if (!paper) { return null; }
    var packs = await window.MrBadmusTeacherData.loadPaperQuestions([paper.id]);
    c.GRID[key] = buildGrid(c.ROSTER[classId] || [], packs[paper.id]);
    return c.GRID[key];
  }

  /* Several papers in one round trip — the insights screen's question chart
     wants the newest marked paper of EVERY live class at once, and one call
     per class would be a dozen. */
  async function grids(pairs) {
    var c = await base();
    var wanted = [];
    pairs.forEach(function (pr) {
      var idx = paperIndex(pr.idx);
      if (idx == null) { return; }
      var key = pr.classId + ":" + idx;
      if (c.GRID[key]) { return; }
      var paper = (c.PAPERS[pr.classId] || [])[idx];
      if (paper) { wanted.push({ key: key, pr: pr, paper: paper }); }
    });
    if (!wanted.length) { return; }
    var packs = await window.MrBadmusTeacherData.loadPaperQuestions(
      wanted.map(function (w) { return w.paper.id; }));
    wanted.forEach(function (w) {
      c.GRID[w.key] = buildGrid(c.ROSTER[w.pr.classId] || [], packs[w.paper.id]);
    });
  }

  /* The newest MARKED paper of a class — Design reaches for index 1 and
     assumes it exists and is closed. It is index 1 only when there is exactly
     one open paper, which is a property of the sample. */
  function newestMarkedIdx(papers) {
    for (var i = 0; i < papers.length; i++) {
      if (papers[i].when === "marked") { return i; }
    }
    return -1;
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE SEARCH OVERLAY
     ═════════════════════════════════════════════════════════════════════

     Design pools three students from each of five hardcoded classes and calls
     it a cross-class search. This is every student on every class the teacher
     holds this year, which is what the box says it is — and the count in the
     placeholder is the real class count, because "all 12 classes" is a
     literal that would go on saying twelve after the thirteenth arrived.   */
  function buildSearchPool(c) {
    var pool = [];
    c.CLASSES.forEach(function (k) {
      (c.ROSTER[k.id] || []).forEach(function (r) {
        pool.push({
          id: r.id,
          name: r.name,
          initials: initialsOf(r.first_name, r.last_name),
          hue: hueFor(r.name),
          klass: k.code,
          classId: k.id,
          avg: r.avg == null ? "—" : r.avg + "%"
        });
      });
    });
    pool.sort(function (a, b) {
      return a.name.localeCompare(b.name) || a.klass.localeCompare(b.klass);
    });
    return pool;
  }

  /* Real shoutouts for the class on screen, mapped into the shape Design's
     feed renders. Design invents two, complete with a fabricated "went from
     38% to 74%"; these are the ones a teacher actually wrote. The template
     LABELS come from the locked six-key enum in shoutouts.js, which mirrors
     the DB CHECK constraint, so the feed and the composer cannot disagree
     about what a template is called. */
  async function buildFeed(classId, now) {
    if (!classId) { return []; }
    var out;
    try {
      out = await window.MrBadmusTeacherData.loadClassShoutouts(classId, { limit: 20 });
    } catch (e) {
      // The feed is one region of one screen. A teacher who cannot read it can
      // still mark, set work and chase; failing the whole page over it would
      // be the wrong trade. Empty, logged, and the rest of the screen renders.
      console.error("[teacher-live] shoutout feed unavailable for class", classId, e);
      return [];
    }
    var tpl = {};
    ((window.MrBadmusShoutouts && window.MrBadmusShoutouts.SHOUTOUT_TEMPLATES) || [])
      .forEach(function (t) { tpl[t.key] = t.label; });
    return (out.shoutouts || []).map(function (s) {
      var r = s.recipient || {};
      var a = s.author || {};
      var name = fullName(r.first_name, r.last_name);
      /* ⊕ RULED BY MIDE, 3 Sep 2026 — ATTRIBUTED. The restored feed says
         whose sentence each shoutout is, and until now this map carried
         `author_id` and no name at all: a colleague's shoutout was unsigned,
         and on a co-taught class that is most of the feed. The RPC
         `class_shoutouts_for_viewer` already resolves the author's profile
         across the RLS gap — that is the whole reason it exists (teachers
         cannot read other teachers' profiles through a FK join, which
         surfaced as em-dash names) — so this is a field being READ, not a
         second query.
         ⚠️ THE FALLBACK IS "A teacher", NOT AN EM DASH. A row whose author
         profile could not be resolved is still a shoutout somebody wrote;
         "—" in a byline slot reads as a bug, and this line sits under a
         child's name where a bug is what a teacher will assume. */
      var by = fullName(a.first_name, a.last_name);
      return {
        id: s.id,
        name: name || "—",
        by: "by " + (by || "a teacher"),
        initials: initialsOf(r.first_name, r.last_name),
        hue: hueFor(name),
        when: relativeTime(s.created_at, now),
        template: tpl[s.template_key] || "",
        // The message a teacher typed, or nothing. A template-only shoutout
        // has no body and gets none — the template line already said it.
        body: s.message || "",
        template_key: s.template_key,
        recipient_id: s.recipient_id,
        author_id: s.author_id
      };
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     load(screen, params)
     ═════════════════════════════════════════════════════════════════════ */
  /* ⊕ MRB-287 E1 — which academic year a class belongs to.

     ⚠️ THIS IS ALSO THE AUTHORISATION CHECK, which is why it is this call and
     not a lighter one. `loadClassMatrices` drives off `class_teachers` under
     RLS and throws `not_authorised` for a class the caller does not teach, and
     it is year-agnostic — so it answers both halves of the question at once:
     is this class mine, and which year is it in. */
  async function yearOfClass(classId) {
    var packs = await window.MrBadmusTeacherData.loadClassMatrices([classId]);
    var pack = packs && packs[classId];
    return (pack && pack.class && pack.class.academic_year_id) || null;
  }

  function notMine(classId) {
    var e = new Error("[teacher-live] class not reachable: " + classId);
    e.code = "not_authorised";
    return e;
  }

  async function load(screen, params) {
    params = params || {};
    var c = await base();

    /* ⛔ THIS USED TO THROW `not_authorised` OUTRIGHT, AND IT WAS A DEAD END.
       A bookmark to last year's class, a link that lost its `?year=`, or a
       teacher whose classes are all past-year: every one of them landed on
       "That class is not one of yours" for a class that was entirely theirs.
       MRB-261 exists to keep that history reachable, so refusing to open it
       was the ticket's own rule inverted.

       ⚠️ THE AUTHORISATION IS NOT WEAKENED, IT IS ASKED SOMEWHERE THAT CAN
       ANSWER IT. A class this teacher does not teach still throws — from
       `yearOfClass`, with the same code and the same sentence — and a year
       that is not in this school's list is refused here. What changes is that
       a class that IS theirs, in a year they are not currently viewing, moves
       the view to that year instead of being disowned. */
    if (params.classId && !c.MATRIX[params.classId]) {
      var ay = await yearOfClass(params.classId);          // throws if foreign
      var known = (c.years.years || []).some(function (y) { return y.id === ay; });
      if (!ay || !known || ay === selectedYearId) { throw notMine(params.classId); }
      selectedYearId = ay;
      reset();
      c = await base();
      // Belt and braces: the year moved and the class still is not in it.
      if (!c.MATRIX[params.classId]) { throw notMine(params.classId); }
    }

    var now = c.now;
    var year = c.years.working;
    var viewing = c.viewing;
    var todayYmd = ymd(now);

    var classId = params.classId && c.MATRIX[params.classId]
      ? params.classId
      : (c.CLASSES[0] ? c.CLASSES[0].id : null);

    // ── prefetch only the grids this screen will actually draw ──────────
    if (screen === "marking" && classId) {
      var papers = c.PAPERS[classId] || [];
      var asked = paperIndex(params.paperIdx);
      var pi = asked == null ? newestMarkedIdx(papers) : asked;
      if (pi >= 0 && papers[pi]) { await grid(classId, pi); }
    } else if (screen === "insights") {
      /* ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 7) — UNCONDITIONAL, AND IT HAD
         TO BECOME SO. This branch used to be gated on
         `params.chartKind === "questions"` and on `params.chartScope`, and
         BOTH of those are read from query parameters that NOTHING ON THE SITE
         EVER SETS: `chartKind` is `q.get("chart")`, the page's own state
         initialiser hardcodes `chartKind: 'submissions'`, and pressing a
         chart chip is a `setState` with no navigation and no fetch. So the
         gate never opened, no grid was ever prefetched, and the Question
         difficulty chart drew "No class has a marked paper yet" on both
         scopes FOREVER — for a school with any amount of marked work.
         One of the six charts could not show data at all.

         (`params.chartScope` is `q.get("scope")` while the page reads
         `?class=`, so the two never agreed either. That mismatch is now
         moot here and is written up in the screen 7 report.)

         Every live class's newest marked grid, in ONE batched round trip —
         `grids()` exists for exactly this — because BOTH scopes of the
         question chart need it: the all-scope draws a row per class, and the
         class scope draws whichever class the teacher then picks. Fetching
         only the scoped class would make switching to All classes show one
         row out of eight and call it "per class".

         The cost is one batched query on an insights load for a teacher who
         never presses Question difficulty. The alternative was a chart that
         never worked. */
      var pairs = [];
      c.CLASSES.forEach(function (k) {
        if (k.state !== "live") { return; }
        var i = newestMarkedIdx(c.PAPERS[k.id] || []);
        if (i >= 0) { pairs.push({ classId: k.id, idx: i }); }
      });
      await grids(pairs);
    }

    var FEED = {};
    if (classId && (screen === "class" || screen === "student")) {
      FEED[classId] = await buildFeed(classId, now);
    }

    var pool = buildSearchPool(c);
    var classCount = c.CLASSES.length;
    var studentCount = c.CLASSES.reduce(function (a, k) { return a + k.n; }, 0);
    var season = seasonFor(todayYmd, year);
    var yearLabel = yearLabelOf(year);
    var week = teachingWeek(new Date(now));
    var academicWeek = academicWeekOf(now, year);

    /* ⊕ MRB-287 E1 — the year in view, and whether it is history.
       Design offers "Previous years" unconditionally and its handler pings
       "2025–26 is read-only". A school in its first year has no other year at
       all, so the strip is GATED in the markup (`teacher_rulings.WRAP` on
       `hasOtherYears`) rather than answered with a toast — a control that
       exists to tell you it should not exist is still a dead control. */
    var viewingName = viewing ? yearLabelOf(viewing) : "";
    var viewingIsPast = !!(viewing && viewing.is_past);

    return {
      // ── who and when ────────────────────────────────────────────────
      teacherName: (profile && profile.first_name) || "",
      envBadge: envBadge(),

      /* Design's "Autumn term · 2026–27", computed. Before the year starts it
         reads Autumn, not Summer — see seasonFor. Blank rather than a guess
         when the school has no academic year at all, which is a state the
         dashboard should show as blank rather than paper over. */
      termLabel: year ? (season + " term · " + yearLabel) : "",
      termSeason: year ? season : "",
      yearLabel: yearLabel,
      yearName: (year && year.name) || "",
      academicWeek: academicWeek,
      termWeekLabel: (year && academicWeek != null) ? season + " Week " + academicWeek : "",

      /* ── ⊕ MRB-287 E1 · THE YEAR IN VIEW ──────────────────────────────
         ⚠️ `yearLabel` ABOVE IS THE WORKING YEAR AND EVERYTHING HERE IS THE
         VIEWED ONE, and conflating the two is the defect this phase fixes.
         `termLabel`, `termSeason` and `termWeekLabel` describe NOW, which is
         always the working year — "Autumn Week 3" is not a fact about
         2025-26. Everything below describes what is on screen. */
      viewingYearLabel: viewingName
        ? ("Viewing " + viewingName + (viewingIsPast ? " · read-only" : ""))
        : "",
      viewingIsPast: viewingIsPast,
      yearOptions: c.yearOptions,
      hasOtherYears: c.yearOptions.length > 0,
      pastYearsLabel: c.yearOptions.length
        ? (viewingIsPast ? "Other years" : "Previous years") : "",

      /* MRB-261: a past year is read-only, and must SAY so. Both halves ship
         together — this sentence and the WRAP that takes the write controls
         off the page — because a page that suppresses a control silently
         reads as broken rather than as finished.

         ⚠️ A BINDING, NEVER A LITERAL. `teacher_tells` fails the build on a
         typed academic year and it is right to: Design's "2025–26 is
         read-only" was wrong from 1 September and wrong on day one for any
         school whose previous year is not 2025-26. */
      canWrite: !viewingIsPast,
      readOnlyLine: (viewingIsPast && viewingName)
        ? (viewingName + " is read-only") : "",

      /* Threaded onto the two navigations that would otherwise lose the year
         — a card into its class, and Back out of one. EMPTY on the working
         year so `MRB_GO` drops the parameter entirely: the ordinary URL is
         unchanged, and the bookmark a teacher keeps never pins a year they
         will have left by September. */
      yearParam: viewingIsPast ? selectedYearId : "",

      // ── this teaching week, in words ────────────────────────────────
      // Design's digest header literals: "Mon 17 – Fri 21 Aug 2026" and
      // "Week of Mon 17 Aug 2026". Both are today's real teaching week.
      weekRangeLabel: dowDayMonth(week.mon) + " – " + dowDayMonth(week.fri) +
                      " " + week.fri.getFullYear(),
      weekOfLabel: "Week of " + dowDayMonth(week.mon) + " " + week.mon.getFullYear(),
      printedOn: dayMonthYear(new Date(now)),

      // ── Design's primitives, real ───────────────────────────────────
      CLASSES: c.CLASSES,
      MATRIX: c.MATRIX,
      ROSTER: c.ROSTER,
      PAPERS: c.PAPERS,
      WEEKS: c.WEEKS,
      GRID: c.GRID,
      FEED: FEED,

      /* Who is looking. Design's delivery has no concept of a viewer at all;
         the ported page needs one synchronously, inside `renderVals`, to
         decide whether to draw the shoutout delete control — so it travels
         through this payload rather than being fetched again per render. */
      ME: viewerId,

      /* The six shoutout templates, from the locked enum that mirrors the DB
         CHECK constraint — `id` is the template KEY, not an ordinal, because
         the key is what an insert stores. Design's numeric ids and its
         `boTpl: 3` default are sample artefacts. */
      TEMPLATES: ((window.MrBadmusShoutouts &&
                   window.MrBadmusShoutouts.SHOUTOUT_TEMPLATES) || [])
        .map(function (t) { return { id: t.key, key: t.key, label: t.label }; }),

      /* ⛔ EMPTY ON PURPOSE. Design's Set-work sheet offers five topics with
         labels like "Set 3 weeks ago". There is no product behind it — the
         sheet composes nothing, and nothing in the schema answers "which
         topics could this class be set next" for a teacher. Five invented
         topics on a working instrument is worse than an empty sheet, because
         a teacher would pick one. In the handover. */
      TOPICS: [],

      /* ⛔ EMPTY ON PURPOSE. The CSV import screen's column mapping, row
         preview and "Import 26 students" button are all invented; Design's
         own README lists "real CSV parsing" as not built. */
      IMPORT_MAP_ROWS: [],
      IMPORT_PREVIEW_ROWS: [],
      importCountLabel: "",

      // ── counts, from data ───────────────────────────────────────────
      classCount: classCount,
      studentCount: studentCount,
      liveClassCount: c.CLASSES.filter(function (k) { return k.state === "live"; }).length,
      // Design: "Search students across all 12 classes".
      searchPlaceholder: classCount === 1
        ? "Search students in your class"
        : "Search students across all " + classCount + " classes",
      searchPool: pool,
      searchPoolCount: pool.length,

      // ── what the caller asked for ───────────────────────────────────
      screen: screen || "classes",
      classId: classId,
      studentId: params.studentId || null,
      paperIdx: paperIndex(params.paperIdx)
    };
  }

  /* ═════════════════════════════════════════════════════════════════════
     go
     ═════════════════════════════════════════════════════════════════════ */

  /* A wall clock on the whole read. Everything above is behind `await`, and a
     Supabase call that never answers leaves the boot line up for ever with no
     way to tell it from a slow one. 30 seconds is long enough for a cold
     start on school wifi and short enough that a teacher gets a sentence
     rather than a spinner. */
  function withDeadline(ms, work) {
    var timer = null;
    return Promise.race([
      work().then(function (v) { clearTimeout(timer); return v; },
                  function (e) { clearTimeout(timer); throw e; }),
      new Promise(function (_, reject) {
        timer = setTimeout(function () {
          var e = new Error("[teacher-live] timed out after " + ms + "ms");
          e.mrbSay = SAY.slow;
          reject(e);
        }, ms);
      })
    ]);
  }

  async function run() {
    boot();                        // ← before the first byte is asked for
    await loadDeps();

    /* ⊕ 27 Aug 2026 — THE YEAR LIST STARTS NOW, NOT AFTER THE GUARD.
       `base()` opens by awaiting `yearIndex()`, and `base()` cannot be called
       until the guard has finished validating — so this read used to be a
       serial wave of its own, waiting behind a round trip whose answer it does
       not use. It needs the client and the persisted token, both of which
       exist the moment the deps are loaded; it does not need to know the
       viewer is a teacher, because RLS decides that and would refuse the rows
       either way.

       `yearIndex()` caches the PROMISE, so `base()` a moment later joins this
       one rather than starting a second. The `.catch` here is only to keep an
       early failure from surfacing as an unhandled rejection — the same
       promise is awaited properly inside `base()`, where the failure belongs
       and where `say()` can act on it. */
    try { yearIndex().catch(function () {}); } catch (e) {}

    /* ⊕ 27 Aug 2026 — A CEILING ON THE GUARD ITSELF. `withDeadline` below has
       covered everything from `base()` onwards since MRB-287, but
       `requireTeacherRole` makes two network reads BEFORE it calls back and
       neither was ever bounded. A stalled one meant `onAllowed` never ran, the
       30-second umbrella was never even opened, and the boot line stayed up
       indefinitely — the one hang the umbrella could not see.

       A flag rather than a race, because the guard's other exits are
       REDIRECTS; a denied teacher navigates away and the timer leaves with the
       page. It fires only when the guard neither called back nor bounced. */
    var guardStarted = false;
    var guardTimer = setTimeout(function () {
      if (!guardStarted) { say(SAY.slow); }
    }, 30000);

    window.MrBadmusTeacherGuard.requireTeacherRole({
      onAllowed: async function (ctx) {
        guardStarted = true;
        clearTimeout(guardTimer);
        try {
          var data = await withDeadline(30000, async function () {
            // The teacher's own name, from the profile the guard already
            // fetched. No second read for a string we were handed, and it is
            // set BEFORE the rows are asked for so a screen that renders
            // early cannot render nameless.
            profile = ctx.profile || null;
            // ⊕ MRB-287 — and the id, from the same handover. The guard has
            // already validated this session; `ctx.user.id` IS `auth.uid()`.
            viewerId = (ctx.user && ctx.user.id) || null;

            /* ⊕ MRB-287 E1 — THE YEAR IS RESOLVED BEFORE THE FIRST ROW IS
               ASKED FOR, because `base()` scopes every read by it. A bare URL
               leaves this null and `pickYear` returns the working year. */
            var q = new URLSearchParams(window.location.search);
            selectedYearId = q.get("year") || null;

            var c = await base();

            /* ⛔ THIS USED TO THROW WHENEVER THE WORKING YEAR WAS EMPTY, and
               it put the one control that would have helped behind the
               sentence saying there was nothing to see. A teacher whose
               classes are ALL last year's — the exact person MRB-261's
               history is for — got "You are not teaching any classes this
               year", no grid, and no year selector, on every load.

               An empty SELECTED year is a STATE, not a failure: the page
               mounts, the grid draws Design's own "No classes" panel
               (`noneShownLine`), and the year strip stays reachable.

               The sentence survives for the case it is actually true of. With
               no other year to switch to, the working year IS every year, so
               "you are not teaching any classes" is exactly right — and that
               is a school in its first year, where there is no history to
               reach and nothing a selector could offer. */
            if (!c.CLASSES.length && !c.yearOptions.length) {
              var e = new Error("[teacher-live] no classes in any year");
              e.mrbSay = SAY.noClasses;
              throw e;
            }
            return load(screenFromLocation(), {
              classId: q.get("class"),
              studentId: q.get("student"),
              paperIdx: q.get("paper"),
              // The charts screen prefetches per-class grids only for the
              // question chart, so it needs to know which chart is opening.
              chartKind: q.get("chart"),
              chartScope: q.get("scope")
            });
          });

          window.__MRB_DATA__ = data;
          window.__MRB_MOUNT__();

          /* ⊕ MRB-306 WS-3 — the reminder control, drawn AFTER the mount.
             Design's v2 delivery (the one this port is pinned to) draws no
             reminder affordance of any kind, so there is no node to finish
             and nothing here is a departure from what she drew. Her v3
             delivery DOES draw "Send reminders" and "Remind all N"; when that
             port lands this injection is deleted and the real control takes
             over. It is written as an injection precisely so that swap is a
             deletion rather than an unpick. */
          if (screenFromLocation() === "class") {
            drawRemindControl(data, q.get("class"), ctx);
          }
        } catch (err) {
          console.error("[teacher-live]", err);
          if (err && err.mrbSay) { return say(err.mrbSay); }
          if (err && (err.code === "not_authorised" ||
                      err.code === "invalid_class_id")) {
            return say(SAY.notMine);
          }
          say(SAY.generic);
        }
      }
      /* No `onDenied`: the guard's own behaviour is the right one. No session
         goes to /auth.html with a return path; a signed-in non-teacher goes
         home. */
    });
  }

  window.MrBadmusTeacherLive = {
    load: load,
    grid: grid,
    grids: grids,
    reload: function () { reset(); return base(); },
    setProfile: function (p) { profile = p || null; },
    setViewer: function (id) { viewerId = id || null; },
    run: run,
    // Exposed for the porter's rulings, which need the same answers rather
    // than their own copies of them.
    subjectFromCode: subjectFromCode,
    relativeTime: relativeTime,
    weekRangeLabel: weekRangeLabel,
    newestMarkedIdx: newestMarkedIdx,
    screenFromLocation: screenFromLocation,
    paperIndex: paperIndex,
    initialsOf: initialsOf,
    hueFor: hueFor,
    SAY: SAY
  };

  /* ⊕ MRB-306 WS-3 — "Remind all N", and the small log beside it.

     WHO IS CHASED. Paper index 0 is this week's work — `buildPapers` sorts
     due_at DESC with nulls first and this file's own comment says index 0 is
     "the week it opens parked on" — and a student is chased when the matrix
     says they have not done it. That predicate is `cellOf()`'s, which is the
     UNION of completed_at, submitted_at and status==='complete': the same
     test the numbers printed beside this button already use, so the chase
     count cannot disagree with them, and one that can never nag a child whose
     own page reads Complete.

     NO FREE TEXT. This sends an identifier, not a message; the wording is
     composed on the student's own page from the class, the work and the
     sender's name. There is nothing here for a teacher to type into.

     THE RATE LIMIT IS THE DATABASE'S. This button does not decide whether a
     reminder is allowed — a unique index does. The control reflects that
     state rather than enforcing it, which is why it reads the log first. */
  async function drawRemindControl(data, classId, ctx) {
    if (!classId) { return; }
    var TD = window.MrBadmusTeacherData;
    if (!TD || !TD.sendReminders) { return; }

    var mx = data && data.MATRIX ? data.MATRIX[classId] : null;
    var papers = data && data.PAPERS ? data.PAPERS[classId] : null;
    var paper = papers && papers.length ? papers[0] : null;
    /* No work set means nobody can be behind on it. Say nothing rather than
       drawing a control that would have nothing to do. */
    if (!paper || !paper.id || !mx || !mx.rows) { return; }

    var chase = mx.rows.filter(function (r) { return !r.submitted[paper.idx]; })
                       .map(function (r) { return r.sid; })
                       .filter(Boolean);

    var host = document.querySelector("main") || document.body;
    if (!host) { return; }

    var box = document.createElement("div");
    box.setAttribute("data-mrb-remind", "1");
    box.style.cssText = [
      "display:flex", "align-items:center", "gap:12px", "flex-wrap:wrap",
      "margin:0 0 16px 0", "padding:12px 14px",
      "border:1px solid var(--st-rule,rgba(0,0,0,.14))",
      "border-radius:10px", "background:var(--st-paper,transparent)",
      "font:400 14px/1.4 var(--st-ui,inherit)"
    ].join(";");

    var line = document.createElement("span");
    line.style.flex = "1";
    box.appendChild(line);

    var btn = document.createElement("button");
    btn.type = "button";
    btn.style.cssText = [
      "flex:none", "cursor:pointer", "min-height:40px", "padding:0 14px",
      "border:1px solid var(--st-rule,rgba(0,0,0,.18))",
      "border-radius:8px", "background:transparent",
      "color:var(--st-accent-text,inherit)", "font:inherit"
    ].join(";");
    box.appendChild(btn);
    host.insertBefore(box, host.firstChild);

    /* The log decides the control's state, so it is read BEFORE the button is
       made pressable. A control that offered to send and then hit the unique
       index would be a lie told twice. */
    var sentToday = [];
    try {
      var log = await TD.remindersForClass(classId, paper.id);
      var today = todayInSchoolTz();
      sentToday = (log.byDay && log.byDay[today]) || [];
    } catch (e) {
      console.warn("[teacher-live] reminder log unavailable", e);
      /* Unknown is not zero. Without the log this cannot honestly say whether
         anyone was reminded today, so it says nothing and offers nothing. */
      box.remove();
      return;
    }

    function paint() {
      if (sentToday.length) {
        line.textContent = "Reminded today \u00B7 " + sentToday.length;
        btn.textContent = "Reminded today";
        btn.disabled = true;
        btn.style.opacity = ".55";
        btn.style.cursor = "default";
        return;
      }
      if (!chase.length) {
        line.textContent = "Everyone has handed this week's work in.";
        btn.remove();
        return;
      }
      line.textContent = chase.length === 1
        ? "1 student has not handed this week's work in."
        : chase.length + " students have not handed this week's work in.";
      btn.textContent = "Remind all " + chase.length;
      btn.disabled = false;
    }
    paint();

    btn.addEventListener("click", async function () {
      btn.disabled = true;
      btn.textContent = "Sending\u2026";
      try {
        var wrote = await TD.sendReminders({
          classId: classId,
          assignmentId: paper.id,
          studentIds: chase,
          teacherId: ctx && ctx.user ? ctx.user.id : null
        });
        /* Report what was WRITTEN, not what was attempted: an upsert that
           ignored a duplicate sent fewer than were asked for, and saying
           otherwise would overstate what the students actually got. */
        sentToday = wrote;
        paint();
      } catch (e) {
        console.error("[teacher-live] sendReminders failed", e);
        line.textContent = "Could not send just now. Try again in a moment.";
        btn.textContent = "Remind all " + chase.length;
        btn.disabled = false;
      }
    });
  }

  /* The school's calendar day, matching the `sent_on` default the database
     stamps. Not the device's date — the two disagree for anyone whose machine
     is on another timezone, and the button's state must follow the rate limit
     that is actually enforced. */
  function todayInSchoolTz() {
    try {
      return new Intl.DateTimeFormat("en-CA", {
        timeZone: "Europe/London",
        year: "numeric", month: "2-digit", day: "2-digit"
      }).format(new Date());
    } catch (e) {
      return new Date().toISOString().slice(0, 10);
    }
  }

  /* ⊕ 27 Aug 2026 — WAKE THE BACKEND, at the top of the file, before anything
     is awaited. Nothing on a teacher screen calls Render today, so this buys
     the teacher nothing directly — it is fired because a teacher opening the
     dashboard at 8:40 is the reliable signal that a school is about to start,
     and the instance carries a measured ~2.2s cold penalty after ~20 minutes
     idle which their students would otherwise each pay in full. Fire and
     forget: no retry, no logging, no await, and a failure is not a fact about
     this page. */
  try {
    fetch("https://mrbadmus-backend.onrender.com/api/health").catch(function () {});
  } catch (e) {}

  run().catch(function (err) {
    console.error("[teacher-live]", err);
    say(SAY.generic);
  });
})();
