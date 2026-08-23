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
    /* ⊕ 23 Aug 2026 — the TIMEOUT sentence, and it is deliberately not
       `generic`. `generic` says "just now" and "in a moment", which is right
       for a request that was refused and wrong for one that was never
       answered: a backend that has just spent 75 seconds not replying will not
       be ready a moment later. This says what actually happened — we waited,
       it did not come — and gives the advice that matches it. It is about the
       student's class and the waiting they did, not about requests, servers or
       timeouts (CLAUDE.md §8.10). */
    slow:       "We waited for your class and it did not arrive. Try again in a minute or two.",
    pastYear:   "That class finished at the end of last year.",
    notMine:    "That class is not one of yours.",
    noRecall:   "There is nothing to look back over yet. Check again after your next lesson.",
    noWork:     "No work has been set for this week yet.",
    workNotSet: "This week’s work is not ready yet. Check again later today."
  };

  function host() { return document.getElementById(HOST_ID); }

  /* One centred line in the host, in the page's own typeface. Both of the two
     states this file can draw are made of it — the boot line below and `say()`
     underneath — so they cannot drift apart in shape, only in colour.

     ⚠️ EVERY TOKEN NAMED HERE CARRIES A LITERAL FALLBACK, and that is
     load-bearing for the boot line rather than defensive. `--pg-*` and every
     other page token live in a `:root` block INSIDE the compiled template, so
     they do not exist until the page mounts; only `/shared/student-ds.css` —
     a real `<link>` in the head — is loaded when the boot line paints, and
     `--ks3-ink` / `--ks3-ink-muted` come from there. */
  function panel(text, state, colour) {
    var wrap = document.createElement("div");
    wrap.setAttribute("data-mrb-state", state);
    wrap.style.cssText =
      "min-height:60vh;display:flex;align-items:center;justify-content:center;" +
      "padding:32px;box-sizing:border-box;";
    var p = document.createElement("p");
    p.style.cssText =
      "margin:0;max-width:34ch;text-align:center;font:400 17px/1.55 " +
      "'IBM Plex Sans',system-ui,-apple-system,'Segoe UI',sans-serif;" +
      "color:" + colour + ";";
    p.textContent = text;
    wrap.appendChild(p);
    return wrap;
  }

  function say(line) {
    var el = host();
    if (!el) { return; }
    el.textContent = "";
    el.appendChild(panel(line, "unavailable", "var(--ks3-ink,#2A2018)"));
  }

  /* ── the boot line ─────────────────────────────────────────────────────
     ⊕ 23 Aug 2026. Nothing on this page paints until every request has come
     back — `window.__MRB_MOUNT__()` is the first thing that draws anything —
     so a slow load was a WHITE PAGE with no explanation and no way to tell it
     from a broken one. A student cannot wait for something that is not
     visibly happening.

     ⚠️ IT SAYS ONLY WHAT IS TRUE BEFORE ANY DATA HAS ARRIVED, WHICH IS TWO
     WORDS. CLAUDE.md §8.10 forbids the page explaining itself to a student, so
     "Loading your class…", a spinner's caption, "Connecting", "One moment" and
     every other sentence about the software, the network or a wait are all
     out. What is left is what the student came for: this is their class, and
     on the assignment page it is their work. Both are true the instant the
     page opens, both are true whatever comes back, and neither is a value —
     under this file's own rule that nothing may INVENT student-visible
     content, the only honest line at boot is one that contains no data at all.
     Not a class name, not a teacher, not a count of anything.

     It is drawn in the muted ink rather than the body ink so it reads as a
     page that has not finished rather than as a message that has been given.

     ⚠️ IT CANNOT SURVIVE THE MOUNT, structurally, and not by being tidied up.
     It is a child of the host, and BOTH of the two ways out of `run()` empty
     the host before they write into it: `student-runtime.js`'s `draw()` opens
     with `host.textContent = ""` and then appends synchronously inside
     `__MRB_MOUNT__()`, and `say()` above does the same. There is no third
     exit, so there is no path on which a student sees this line beside real
     content — including the case where the mount throws half-way, because that
     lands in the catch, which calls `say()`. Removing it here as well would
     add a blank frame between the clear and the paint and would look like the
     guarantee while not being it. */
  var BOOT = {
    "class":      "Your class",
    "assignment": "Your work"
  };

  function boot(page) {
    var el = host();
    if (!el || el.firstChild) { return; }   // never over the top of anything
    el.appendChild(panel(BOOT[page] || BOOT["class"], "boot",
                         "var(--ks3-ink-muted,#5F564F)"));
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

  /* ═══════════════════════════════════════════════════════════════════════
     THE PRACTICE ORDER — ONE DEFINITION, AND TWO THINGS WILL READ IT
     ═══════════════════════════════════════════════════════════════════════

     ⊕ 23 Aug 2026 — PHASE 2. Ruled: *"wrongly-answered sources first (with the
     FROM YOUR WORK chip), then least-seen, then random."*

     ⚠️ THIS IS WRITTEN ONCE ON PURPOSE. The flashcard deck below uses it now;
     the recall round's question bank is the next unit and uses the IDENTICAL
     rule. Two implementations of "what should this student practise next"
     would drift, and they would drift INVISIBLY — nothing on the page states
     the order, so a divergence between the cards and the round is not
     something a student or a gate could see. `rankForPractice` is the one
     place. Both callers hand it `{id, lesson}` and nothing else about the
     item's shape matters here.

     THE THREE KEYS, IN ORDER:

       1  `wrong` — a lesson the student has got a question wrong in. This is
          the chip Design draws (`FROM YOUR WORK`), and it is deliberately at
          LESSON grain: a card id is `<lesson>#def#<term>` and a question ref
          is `<lesson>#recall` or a bank id, so the two corpora share no ids at
          all and can only ever be joined through the lesson they belong to.
          Confirmed against real rows before it was written.

       2  `seen` — how many times this student has REVEALED this card. Least
          first, so a fresh open lands on what they have practised least
          rather than on the same six cards for ever.

       3  a deterministic jitter, from a SEED THE CALLER FIXES. Not
          `Math.random()`: the deck must not reshuffle under the student's
          fingers, and a random tiebreak would give a different order on every
          re-render. The seed is the class and the school-local DATE, so the
          order is stable for a session and stable across a reload, and it
          moves tomorrow.

       4  and finally the item's ORIGINAL index, so the sort is total. Two
          cards with the same lesson, the same count and the same 32-bit hash
          would otherwise be ordered by the engine's sort stability, which is
          a guarantee in modern engines and was not always one. */

  /* FNV-1a, 32-bit. A hash and not a PRNG: the same id under the same seed
     must give the same number on every render, on every device, for ever. */
  function hash32(str) {
    var h = 0x811c9dc5, i;
    for (i = 0; i < str.length; i += 1) {
      h ^= str.charCodeAt(i);
      h = (h + ((h << 1) + (h << 4) + (h << 7) + (h << 8) + (h << 24))) >>> 0;
    }
    return h >>> 0;
  }

  function rankForPractice(items, opts) {
    var wrong = (opts && opts.wrong) || {};
    var seen = (opts && opts.seen) || {};
    var seed = String((opts && opts.seed) || "");
    return (items || []).map(function (it, i) {
      return {
        it: it, i: i,
        mine: wrong[it.lesson] ? 0 : 1,
        seen: Number(seen[it.id]) || 0,
        jitter: hash32(seed + "|" + String(it.id))
      };
    }).sort(function (a, b) {
      if (a.mine !== b.mine) { return a.mine - b.mine; }
      if (a.seen !== b.seen) { return a.seen - b.seen; }
      if (a.jitter !== b.jitter) { return a.jitter - b.jitter; }
      return a.i - b.i;
    }).map(function (r) { return r.it; });
  }

  /* ── HOW MANY TIMES HAS THIS STUDENT SEEN THIS CARD? ────────────────────

     ⚠️ NOTHING RECORDS IT TODAY, and this is where the answer is decided.

     THE CHOICE, AND THE REASON. A table would be the durable answer and it is
     the wrong one for THIS value, on three counts:

       · it is a PREFERENCE OF ORDER, not a fact about the student's work.
         Nothing on the screen ever says "you have seen this three times". A
         count that is lost degrades the ORDER of a revision stack; it does not
         make the page say anything untrue. That is the whole difference
         between this and the answer queue, where a lost entry meant a tick the
         student had already been shown was a lie, and where localStorage was
         chosen for exactly the opposite reason — because only a synchronous
         store could be asked in time to keep the page honest.
       · it would be a WRITE PER FLIP. A student turning thirty cards over in a
         revision session is thirty round trips on school wifi, for a number
         nobody reads.
       · it is a PRODUCTION MIGRATION, and this run is not allowed to apply
         one. Deferring the whole unit behind a migration Mide has to apply by
         hand would have shipped a deck with no least-seen half at all.

     THE KEY, AND IT FOLLOWS THE ANSWER QUEUE'S DISCIPLINE EXACTLY:

         mrbadmusai.cardseen.v1.<auth user id>.<class id>

     A school machine is shared. A second child signing in on the same browser
     profile computes a DIFFERENT key, reads nothing, and has no code path to
     the first child's counts. The blob repeats BOTH ids inside itself and a
     read whose ids disagree with the key is discarded unread, so even a key
     collision could not survive being opened. Per class, because the deck is
     per class.

     ⚠️ IT IS A CACHE AND IT MAY BE EMPTY. Every read is wrapped, every write
     is wrapped, and a store that refuses (private mode, disabled by policy,
     full) costs the least-seen tiebreak and nothing else — the deck still
     ranks by wrong-answer first and by the fixed jitter after it. There is no
     state in which a missing count can produce a wrong sentence, because there
     is no sentence. */
  var SEEN_PREFIX = "mrbadmusai.cardseen.v1.";

  /* ⊕ 23 Aug 2026 — PHASE 3. A SECOND CORPUS, THE SAME STORE SHAPE.

     The recall round needs the identical "how many times has this student seen
     this" count, keyed on a LADDER QUESTION REF rather than on a card id, and
     `rankForPractice` reads `opts.seen[it.id]` for both. So `seenStore` takes
     the prefix as a parameter and there is still ONE implementation of the
     store, the key discipline and the ownership check.

     ⚠️ THEY ARE SEPARATE KEYS AND NOT ONE SHARED MAP, and the ids being
     provably disjoint (`<lesson>#def#<term>` against `<lesson>#recall`) is not
     a reason to merge them. A card is SEEN when it is revealed; a question is
     SEEN when it is answered. Two different events, two different corpora, two
     different blobs — and one growing without bound because the other is busy
     is a bug nobody would ever look for. */
  var QSEEN_PREFIX = "mrbadmusai.recallseen.v1.";

  function seenStore(userId, classId, prefix) {
    var owner = String(userId || "anon");
    var kls = String(classId || "");
    var key = (prefix || SEEN_PREFIX) + owner + "." + kls;

    function ls() {
      try { return window.localStorage || null; } catch (e) { return null; }
    }
    function read() {
      var st = ls();
      if (!st) { return {}; }
      try {
        var raw = st.getItem(key);
        if (!raw) { return {}; }
        var d = JSON.parse(raw);
        if (!d || typeof d !== "object" || !d.n) { return {}; }
        if (d.u !== owner || d.k !== kls) { return {}; }
        return d.n;
      } catch (e) { return {}; }
    }
    return {
      all: read,
      /* Returns whether the count really moved, so a caller that wanted to say
         something about it could — nothing does today, and the shape is here
         because a write that silently does nothing is what this file keeps
         refusing to ship. */
      bump: function (cardId) {
        var st = ls();
        if (!st || !cardId) { return false; }
        try {
          var n = read();
          n[cardId] = (Number(n[cardId]) || 0) + 1;
          st.setItem(key, JSON.stringify({ u: owner, k: kls, n: n }));
          return true;
        } catch (e) { return false; }
      }
    };
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

  /* ── THE DEADLINE EVERY BACKEND CALL NOW CARRIES ───────────────────────
     ⊕ 23 Aug 2026. What was here was a bare `await fetch(...)`, and a bare
     fetch has no timeout of any kind. A request that is never ANSWERED is
     never REJECTED either, so `run()`'s catch — which only fires on a
     rejection — never fires, `__MRB_MOUNT__()` is never reached, and nothing
     is ever said. Driven and measured: a held-open backend request left this
     page blank for 58 seconds and would have stayed blank for ever. The page
     did not fail. It waited, silently, with no end.

     THE TWO BUDGETS ARE NOT A TUNING PREFERENCE.

     Render's free tier spins the backend down, and this repo already writes
     down what that costs: `student_page_drive.wait_for_mount()` budgets
     SEVENTY-FIVE SECONDS for the whole mount, because "the first request of
     the day takes the better part of a minute to come back". A deadline
     shorter than that would turn a slow-but-working cold start into a
     failure — the page would tell a student it could not load a class that
     was on its way. So the first request of a page load is given that whole
     75 seconds to itself: strictly more generous than the budget the drive
     already allows for every request put together, which is what makes it
     impossible for this change to fail a load that used to succeed.

     THE SPIN-UP IS PAID ONCE. After any request has come back the instance is
     awake, and a second request still unanswered 25 seconds later is stuck,
     not starting up — the measured warm response on these routes is under two
     seconds, so the warm budget is more than ten times the worst seen.
     Carrying the cold budget into every request would cost a student 75
     seconds PER REQUEST in front of a dead backend instead of 75 once.

     ⚠️ WRITES KEEP THE COLD BUDGET, ALWAYS — see `post()` in the sink. A tab
     left open long enough for the instance to spin down again is not a cold
     start, it is a cold RESTART, and the warm budget would abort a save that
     was going to succeed. Nothing is watching a save the way a student watches
     a paint. */
  var COLD_MS = 75000;
  var WARM_MS = 25000;
  var backendWoken = false;

  /* ⚠️ A TIMEOUT MUST BE TELLABLE FROM EVERY OTHER FAILURE, or the page says
     "try again in a moment" about a backend that is not coming back for
     minutes. `signal.aborted` is the test rather than the error's name: only
     this timer ever aborts these requests, so it cannot be confused with a
     network error that happens to be called something similar. */
  async function withDeadline(ms, path, go) {
    var ctl = new AbortController();
    var timer = setTimeout(function () { ctl.abort(); }, ms);
    try {
      var out = await go(ctl.signal);
      backendWoken = true;
      return out;
    } catch (err) {
      if (ctl.signal.aborted) {
        var late = new Error("no answer within " + Math.round(ms / 1000) +
                             "s on " + path);
        late.code = "backend_timeout";
        late.mrbSay = SAY.slow;
        throw late;
      }
      throw err;
    } finally {
      clearTimeout(timer);
    }
  }

  async function api(path, token) {
    var cfg = window.MrBadmusConfig || {};
    var base = cfg.BACKEND_URL || "https://mrbadmus-backend.onrender.com";
    return withDeadline(backendWoken ? WARM_MS : COLD_MS, path,
      async function (signal) {
        var res = await fetch(base + path, {
          headers: { Authorization: "Bearer " + token },
          signal: signal
        });
        var stamp = res.headers.get("date");
        if (stamp) {
          var t = Date.parse(stamp);
          if (!isNaN(t)) { serverNow = t; }
        }
        if (!res.ok) {
          throw new Error("backend " + res.status + " on " + path);
        }
        /* ⚠️ THE BODY READ IS INSIDE THE DEADLINE ON PURPOSE. A response whose
           HEADERS arrive and whose BODY never does is the same blank page as a
           request that was never answered at all, and a deadline that stopped
           at the headers would not see it. `signal` aborts a body read in
           progress, so both halves are covered by one timer. */
        return res.json();
      });
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

  /* ── the address must name the class that is on the screen ─────────────
     ⊕ RULED 23 Aug 2026. `pickClass` above already ignores a `?class=` that
     names a class this student is not in, and shows them their own instead.
     That behaviour is right and it stays. What was wrong is that the ADDRESS
     BAR went on reading the other class's id — the page showed 8r/Sc1 while
     the URL said 9m/Sc2 — and `carryParams()` then copied that id onto every
     internal link, so the wrong class travelled with the student all the way
     to the assignment page.

     ⛔ NO BANNER AND NO MESSAGE. Ruled explicitly. A student who followed a
     friend's link gets their own class and an honest address, and is told
     nothing at all: there is nothing they did wrong and nothing for them to
     act on. `SAY.notMine` stays unreachable from here — it belongs to the
     backend's own `not_authorised` / `class_not_found` codes in the catch.

     THE CORRECTION DROPS THE PARAMETER RATHER THAN REWRITING IT, and the
     reason is that when this fires the class on screen is ALWAYS `classes[0]`,
     because that is the only thing `pickClass` can fall back to. A bare
     `/student/class` is precisely what "the default class" means, so removing
     the parameter is the URL telling the truth rather than the URL being
     tidied. Writing the real id in instead would encode a choice the student
     never made, and would pin any bookmark of it to one class id that stops
     being in the working academic year next September — at which point the
     address is lying again. The bare address resolves to whatever class the
     student is in, in whatever year they open it.

     Everything else in the query survives, `env` above all: `carryParams`
     carries it deliberately so a tester is not moved from the test project to
     production mid-journey, and this must not undo that.

     `replaceState`, never `pushState`. The lying URL is REPLACED, so it is not
     left behind in the history for Back to return to, and Back still goes
     wherever the student came from on one press — exactly as it did before. */
  function correctAddress(shown) {
    if (!window.history || !window.history.replaceState) { return; }
    var q = new URLSearchParams(window.location.search);
    if (!q.has("class")) { return; }
    if (q.get("class") === shown.id) { return; }      // already honest
    q.delete("class");
    var rest = q.toString();
    window.history.replaceState(window.history.state, "",
      window.location.pathname + (rest ? "?" + rest : "") +
      window.location.hash);
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

  function makeSink(assignment, questions, progress, token, userId) {
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

    /* ═══ THE OFFLINE QUEUE — ON THE DEVICE, NOT IN THE PAGE ══════════
       ⊕ RULED 23 Aug 2026 by Mide. "Queued answers survive reload
       (localStorage or equivalent), drain on reconnect, and the held state is
       honest — nothing shows as held unless it genuinely survives a tab close."

       ⛔ WHAT THIS REPLACES: `var queue = []`. A plain array in the page's
       memory. An answer given offline was shown to the student as
       `OFFLINE · 01 HELD ON THIS DEVICE` and was on no device at all: a reload,
       a tab close, a phone locking itself and killing the tab, and the answer
       was gone with no trace, no retry and no message. The student had seen a
       tick. That is the same shape as the hardcoded hand-in stamp — a false
       confirmation, which is worse than a visible failure because the student
       stops worrying about it.

       ⚠️ localStorage, NOT IndexedDB, and the reason is the honesty rule
       rather than convenience. `confirm` has to decide, in the same turn the
       answer is given, whether it is allowed to SHOW that answer as held — and
       only a SYNCHRONOUS store can be asked. IndexedDB would force the page to
       claim the answer is held and then take the claim back a tick later,
       which is the defect wearing a different hat. Capacity is not close: one
       entry is a few hundred bytes, a whole 15-question assignment under
       10 KB, against a 5 MB budget. Design's own page already keeps its state
       here, so this adds no failure surface the page did not have.

       ⚠️ THE KEY IS PER STUDENT AND PER ASSIGNMENT. This is the single most
       important line in the unit:

           mrbadmusai.answerqueue.v1.<auth user id>.<assignment id>

       A school machine is shared. `<auth user id>` is the Supabase auth id of
       the student whose session built this page, so a second child signing in
       on the same browser profile computes a DIFFERENT key, reads nothing, and
       has no path of any kind to the first child's queued answers. The stored
       blob repeats both ids INSIDE it and a read whose ids disagree with the
       key is discarded unread, so even a key collision could not survive being
       opened. The assignment id keeps two pieces of work apart for one child.

       ⚠️ AT MOST ONE ENTRY PER QUESTION, which is what makes a superseded
       answer unresurrectable BY CONSTRUCTION rather than by ordering. The
       queue is a MAP keyed by question index, never a list: answering Q3 a
       second time REPLACES Q3's entry instead of queueing behind it. There is
       no "must not overwrite C with B" problem to get right, because B stops
       existing the moment C is given. Each entry lands in its own
       `(submission_id, question_index)` row, so the order entries drain in
       cannot change the result either. */
    var QOWNER = String(userId || "anon");
    var QPREFIX = "mrbadmusai.answerqueue.v1.";
    var QKEY = QPREFIX + QOWNER + "." + String(assignment.id);

    /* Every access below can throw — private mode, a store disabled by policy,
       a full one. None of them may take the page down, and none of them may be
       allowed to LOOK like success. */
    function lstore() {
      try { return window.localStorage || null; } catch (e) { return null; }
    }

    function readStored() {
      var ls = lstore();
      if (!ls) { return {}; }
      try {
        var raw = ls.getItem(QKEY);
        if (!raw) { return {}; }
        var d = JSON.parse(raw);
        if (!d || typeof d !== "object" || !d.e) { return {}; }
        if (d.u !== QOWNER || d.a !== String(assignment.id)) { return {}; }
        return d.e;
      } catch (e) { return {}; }
    }

    var pending = readStored();     // question index → entry, in memory
    var seen = {};                  // every index THIS sink has ever held
    Object.keys(pending).forEach(function (k) { seen[k] = 1; });
    var flushing = false;
    /* ⊕ 23 Aug 2026 — THE PROMISE A CONCURRENT CALLER WAITS ON. See `flush`. */
    var flushWait = null;

    /* A write keeps any entry for a question this sink has never touched — a
       second tab on the same assignment — and drops the ones it HAS touched
       and no longer holds, which are exactly the ones it has just delivered.
       Merging blindly would resurrect what `delete` was for; overwriting
       blindly would throw away another tab's work. `seen` is the difference.
       Returns whether the write actually happened. */
    function persist() {
      var ls = lstore();
      if (!ls) { return false; }
      try {
        var out = {};
        var stored = readStored();
        Object.keys(stored).forEach(function (k) {
          if (!seen[k]) { out[k] = stored[k]; }
        });
        Object.keys(pending).forEach(function (k) { out[k] = pending[k]; });
        if (!Object.keys(out).length) { ls.removeItem(QKEY); return true; }
        ls.setItem(QKEY, JSON.stringify({
          u: QOWNER, a: String(assignment.id), e: out
        }));
        return true;
      } catch (e) { return false; }
    }

    /* ⚠️ THE CLAIM IS VERIFIED, NOT ASSUMED. `setItem` not throwing is very
       nearly a guarantee, and "very nearly" is what a child is being asked to
       trust with a lesson's work. The entry is READ BACK and matched before
       the page is allowed to say the word held. */
    function keptOnDevice(index, ts) {
      var e = readStored()[String(index)];
      return !!(e && e.ts === ts);
    }

    /* ⚠️ PRUNED AGAINST THE SERVER BEFORE ANYTHING IS SENT. This runs at
       CONSTRUCTION, before the first `flush()` and before `resume()`, because
       a drain that started first could deliver a stale entry over a newer
       answer in the half-second before the pruning caught up.

       An entry whose question the SERVER ALREADY HAS AN ANSWER FOR is dropped,
       without comparing what either one says. Two different histories arrive
       at that state and dropping is right for both:

         · THE `keepalive` DUPLICATE. The answer WAS delivered — by the request
           `keepalive` let outlive the tab — and the queue was killed before it
           could hear so. Re-sending is a harmless upsert of an identical value,
           but it is a write nobody needs and a tick nobody should have to
           trust twice.

         · THE SUPERSEDED ANSWER. The student answered that question again
           somewhere this queue cannot see — the school computer at lunchtime,
           the other phone — and THAT answer is on the server. Replaying the
           stranded one would overwrite a NEWER answer with an OLDER one, which
           is the one thing a queue must never do. No timestamps are needed to
           prevent it: an entry is only ever written by a page that had just
           found the server holding nothing for that question, so a server that
           now holds something is always holding something later.

       And an entry is dropped if the question it names has MOVED. The index is
       positional, and a retired question shifts every index after it, so the
       stored `question_ref` and option letter are checked against the question
       list THIS page loaded. A mismatch means the answer can no longer be
       attributed with certainty — and a confidently wrong attribution is worse
       than a lost answer, because it marks a child against a question they
       never saw. */
    var serverHas = {};
    ((progress || {}).answers || []).forEach(function (a) {
      serverHas[String(a.question_index)] = 1;
    });
    (function prune() {
      var changed = false;
      Object.keys(pending).forEach(function (k) {
        var e = pending[k] || {};
        var src = (questions[Number(k)] && questions[Number(k)].__src) || null;
        var opts = (src && src.options) || [];
        var chosen = opts[e.opt] || null;
        var ok = !serverHas[k] && !!src && !!chosen &&
                 (!e.ref || !src.question_ref || e.ref === src.question_ref) &&
                 (chosen.letter || LETTERS[e.opt]) === e.letter;
        if (!ok) { delete pending[k]; changed = true; }
      });
      if (changed) { persist(); }
    }());

    /* ⚠️ SNAPSHOTTED HERE, and read by `resume()` from the snapshot rather than
       from the live map. `resume()` runs inside the first render and the
       construction `flush()` below is asynchronous, so in principle a fast
       drain could empty an entry out of `pending` between the two — and the
       student would see that question blank, because `progress` was fetched
       before it landed and the queue no longer holds it. Nothing is lost from
       the database by that race, but the paint would be wrong for one load.
       A snapshot cannot race. */
    var atLoad = {};
    Object.keys(pending).forEach(function (k) { atLoad[k] = pending[k].opt; });

    /* ⚠️ AND A BOUND ON A SHARED MACHINE. Queues belonging to ANOTHER student
       or another assignment are never read and never drained by this sink —
       that is the key scoping above — but left alone they would accumulate on a
       classroom computer until the store was full, at which point THIS
       student's writes start failing and the honest held state starts saying
       no. So keys under this prefix that are not ours and whose newest entry
       is over 30 days old are removed. Never our own, whatever its age: the
       work of the child in front of us is not something to tidy. Thirty days
       is well past any assignment's deadline, and it is also the answer to how
       long one child's answers should sit on a machine other children use. */
    (function sweep() {
      var ls = lstore();
      if (!ls) { return; }
      try {
        var cut = Date.now() - 30 * 86400000;
        var kill = [];
        for (var i = 0; i < ls.length; i += 1) {
          var k = ls.key(i);
          if (!k || k.indexOf(QPREFIX) !== 0 || k === QKEY) { continue; }
          var d = JSON.parse(ls.getItem(k) || "null");
          var e = (d && d.e) || {};
          var newest = 0;
          Object.keys(e).forEach(function (j) {
            if (e[j] && e[j].ts > newest) { newest = e[j].ts; }
          });
          if (newest < cut) { kill.push(k); }
        }
        kill.forEach(function (k) { ls.removeItem(k); });
      } catch (e) { /* a store that cannot be swept still works */ }
    }());

    /* ⊕ 23 Aug 2026 — this carries a deadline too, and it is the COLD one,
       always. A hung save is not a blank page, but it is the same silence: a
       `post` that never settles leaves `flushing` true for the rest of the
       session, so `flush()` returns immediately for every answer after it and
       NOTHING is ever saved again while the page goes on showing ticks. Both
       routes behind it are idempotent by construction — the answer route
       upserts on `(submission_id, question_index)` and the complete route
       guards its update on `status = 'in_progress'` and serves the winning row
       — so the queue's retry after an aborted write cannot double anything.

       ⚠️ THE DEADLINE DOES NOT WEAKEN `keepalive` BELOW. The abort is fired by
       a `setTimeout` inside this document; when the document unloads its
       timers never run, so the request that `keepalive` exists to let outlive
       the page is exactly the one this can never abort. */
    async function post(path, body) {
      var cfg = window.MrBadmusConfig || {};
      var base = cfg.BACKEND_URL || "https://mrbadmus-backend.onrender.com";
      return withDeadline(COLD_MS, path, async function (signal) {
        var res = await fetch(base + path, {
          signal: signal,
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
      });
    }

    /* One drain at a time, and it always ends. The `flushing` flag is the same
       one the last unit found stuck true for ever behind a hung `post`; it is
       safe now for the same reason it was made safe then — `post` carries a
       deadline, so every path out of this loop reaches the `finally`. */
    /* ⚠️ ⊕ 23 Aug 2026 — A CONCURRENT CALLER NOW WAITS FOR THE DRAIN, AND THAT
       IS A DATA-LOSS FIX, NOT A TIDY-UP.

       This used to read `if (flushing) { return; }`, which resolves INSTANTLY.
       `complete()` opens with `flush().then(...)` and a comment promising
       "answers first" — but every answer also calls `flush()` un-awaited, so
       when a student pressed Complete a drain was almost always already in
       flight. `complete`'s flush then no-opped, resolved on the spot, and the
       completion POST overtook the answers still draining.

       `/api/assignment/complete` flips the submission off `in_progress`, and
       the answer route then REFUSES the stragglers with a 409. They are not
       retried into existence later: the row will not accept them again.

       Measured on production, one completion in four: the student was shown
       `3 / 4 · 75%` and the database recorded `score 2, max_score 2` with two
       of the four attempts missing. The last answer POSTed 240ms AFTER
       `completed_at`. Answer POSTs measured 386–2605ms and drain serially, so
       a cold backend or a phone on 4G widens the window rather than closing it.

       Returning the in-flight promise makes `complete`'s own comment true. */
    function flush() {
      if (flushing) { return flushWait; }
      flushing = true;
      flushWait = (async function () {
      try {
        for (;;) {
          var keys = Object.keys(pending);
          if (!keys.length) { break; }
          /* Oldest first. Ordering is a courtesy rather than a correctness
             property here — one entry per question, one row per question — but
             a queue that drains in the order the answers were given is the one
             a teacher watching the marks appear would expect. */
          keys.sort(function (a, b) {
            return (pending[a].ts - pending[b].ts) || (Number(a) - Number(b));
          });
          var k = keys[0];
          var entry = pending[k];
          await post("/api/assignment/answer",
                     { assignment_id: assignment.id, answer: entry.body });
          /* ⚠️ REMOVED ONLY IF IT IS STILL THE ANSWER THAT WAS SENT. A newer
             answer to the same question, given while this request was in
             flight, must not be deleted by this request's success — it has not
             been sent. The loop comes round and sends it. */
          if (pending[k] && pending[k].ts === entry.ts) {
            delete pending[k];
            persist();
          }
        }
      } catch (err) {
        /* Nothing is lost here. The entry is still in `pending` AND still on
           the device, and the next `online`, the next answer, or simply the
           next time this page opens will send it. */
        console.error("[student-live] answer not saved yet", err);
      } finally {
        flushing = false;
        flushWait = null;
      }
      })();
      return flushWait;
    }

    if (typeof window.addEventListener === "function") {
      window.addEventListener("online", function () { flush(); });
    }

    /* ⚠️ AND ON THE WAY IN, WHICH IS THE CASE `online` CANNOT COVER. `online`
       fires on a TRANSITION. A student who answered on the bus, closed the
       tab, and opened it again at home is never in one: the page simply starts
       up connected with answers already on the device. Without this the queue
       would sit there until they happened to lose signal and find it again. */
    if (!(typeof navigator === "object" && navigator &&
          navigator.onLine === false)) {
      flush();
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
        /* ⊕ 23 Aug 2026 — AND THE DEVICE'S OWN UNSENT ANSWERS. Already pruned
           against the server at construction, so what is left is work the
           server has never been told about and the student is entitled to see
           exactly where they left it: answered, and hatched as held.

           This does not soften W2. The server is still the truth; the queue is
           not a cached copy of the truth competing with it, it is the sink's
           own unfinished business — writes it accepted and has not yet
           delivered. Every question the server HAS an answer for was dropped
           before this line ran, so the two can never disagree. */
        var heldNow = {};
        Object.keys(atLoad).forEach(function (k) {
          answers[Number(k)] = atLoad[k];
          heldNow[Number(k)] = 1;
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
          held: heldNow,
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
        var k = String(ev.index);
        var ts = Date.now();
        /* A REPLACEMENT, never an addition — see the map note above. */
        pending[k] = {
          ts: ts, opt: ev.option, ref: body.question_ref,
          letter: body.selected_option_letter, body: body
        };
        seen[k] = 1;
        var kept = persist() && keptOnDevice(ev.index, ts);
        flush();
        /* ⚠️ WHAT THE PAGE IS ALLOWED TO SAY, AND IT IS A FACT RATHER THAN AN
           INTENTION. `held` drives the hatch and the "HELD ON THIS DEVICE"
           count. It is true here or it is not said: an answer that could not
           be written to the device is still sent from memory if this tab lives
           long enough, but it will NOT survive the tab being closed — so it is
           not held, and the student is not told it is. */
        return { held: !!(ev.offline && kept), kept: kept };
      },

      /* Which questions are still waiting ON THIS DEVICE. `drain` reads this
         so a hatch clears when the answer has actually gone, rather than when
         a timer says it has. */
      pending: function () {
        var out = {};
        Object.keys(pending).forEach(function (k) { out[k] = 1; });
        return out;
      },

      complete: function (elapsed) {
        /* Answers first. A completion that overtook the last answer would mark
           the work finished without the answer that finished it.

           ⊕ 23 Aug 2026 — AND THE SECOND HALF OF THAT FIX. `flush` now waits
           for an in-flight drain, which closes the race that was actually
           losing marks. This closes the remaining one: a drain that ENDED
           because a send FAILED leaves entries in `pending`, and completing on
           top of them asks the backend to freeze a submission the student's
           answers can never be added to afterwards.

           So the emptiness is CHECKED rather than assumed. If the queue will
           not drain, the completion is not sent: the answers stay queued on
           the device, the submission stays `in_progress`, and the next visit —
           which reads its state from the server — sends them and can complete
           for real. A completion is the one thing on this page that cannot be
           taken back.

           ⚠️ AND IT IS ONE DRAIN, NOT TWO. The first draft re-drove the queue
           before checking, which read as belt-and-braces and was not: `flush`
           already loops until the queue is empty or a send throws, so a second
           call repeats the failure that just happened — and it does so behind
           `post`'s own 75s cold deadline, chaining two of them. Measured, that
           held the button's spinner for up to two and a half minutes where the
           old code returned instantly. A retry that cannot succeed is not
           worth a minute of a child staring at a spinner; the recovery path is
           the next page load, and it is driven. */
        return flush().then(function () {
          var stuck = Object.keys(pending).length;
          if (stuck) {
            var e = new Error("answers still queued: " + stuck);
            e.code = "answers_unsaved";
            throw e;
          }
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
    /* ⊕ 23 Aug 2026 — PHASE 2. THE SAME RESOLUTION, READ TWICE OVER.
       `lessonsFor` answers "which lesson does THIS piece of work draw on", and
       drops any slug this build has no PAGE for, because its reader is a link.
       The flashcard deck asks a different question of the same walk — "which
       lessons has this class covered AT ALL" — and must NOT drop those: a card
       comes out of `ks3_cards`, not out of a lesson page, so a lesson with no
       page still has cards worth revising. Both are declared out here so the
       one walk can fill both, rather than the deck growing a second resolution
       that would drift the first time either changed. */
    var coveredSlugs = {};
    var bySlug = {};
    var assignmentIds = (aw.data || []).map(function (r) { return r.id; });
    try {
      var ids = assignmentIds;
      if (ids.length) {
        var aq = await sb.from("assignment_questions")
          .select("assignment_id, position, source_ref")
          .in("assignment_id", ids).order("position");

        var refs = [];
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
          if (slug) { coveredSlugs[slug] = true; }
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

    /* ── ⊕ 23 Aug 2026 — PHASE 4. DESIGN'S DONE BENCH, FROM THE REAL ROW ──
       Every value the grafted done bench shows is derived HERE, from
       `benchCard` — this student's own `assignment_submissions` row as the
       data layer returns it — and from the `progress` block the
       current-assignment endpoint carries. Nothing on that surface is a
       constant, and nothing is computed twice: `benchCard`, `benchMarked` and
       `benchLate` are the same three facts the work list two hundred lines
       below reads for its own `marked` / `score` / `detail`, resolved once,
       above both readers.

       ⚠️ THE SCORE IS THE SAME PAIR TWICE, AND THAT IS THE POINT. Design draws
       `SCORE 50%` and `RIGHT 2 of 4` as two rows, and they are two READINGS of
       `(score, max_score)` — the percentage and the raw marks. Deriving the
       percentage from anything else would let the docket disagree with itself
       on the same card. `row.score` in the work list is `Math.round((score /
       max_score) * 100)` and this is the identical expression, on the identical
       pair, which is why the bench and the row can never differ. */
    var benchPct = (benchMarked && benchCard.max_score > 0)
      ? Math.round((benchCard.score / benchCard.max_score) * 100) : null;

    /* OPENED · ANSWERED · COMPLETED, and it is a count of MILESTONES rather
       than a drawing. Design's sample says `3 / 3`.

         OPENED     a submission row exists, so it was opened. Certain.
         ANSWERED   every question has an answer. `progress` carries
                    `answered` and `total`; where it does not, the submission
                    itself is the only evidence and it says yes.
         COMPLETED  `is_submitted`, which is what put this branch on screen.

       A student who completes with blanks therefore reads `2 / 3`, which is
       true, rather than `3 / 3`, which is Design's sample. */
    var benchProg = (current && current.progress) || null;
    var benchAllAnswered = !(benchProg && benchProg.total != null)
      || benchProg.answered >= benchProg.total;
    var benchSteps = 2 + (benchAllAnswered ? 1 : 0);

    /* The topic, resolved once for the two headings that show it — the open
       bench's and the done bench's. Design's two deliveries drew two different
       sample topics in that slot, so the port carries two bound KEYS; there is
       still exactly one FACT, and it is this. */
    var benchTopic = (current && current.assignment)
      ? (current.assignment.topic || current.assignment.title || "") : "";

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
    /* ⊕ 23 Aug 2026 — PHASE 3. THE THROW THAT USED TO BE HERE IS GONE, AND
       ITS REMOVAL IS THE POINT OF THE UNIT RATHER THAN A SIDE EFFECT.

       ⛔ What stood here read:

           if (!questions.length) {
             var e = new Error("no recall questions");
             e.mrbSay = SAY.noRecall;   // "There is nothing to look back over
             throw e;                   //  yet. Check again after your next
           }                            //  lesson."

       It was correct for the page it was written against. Design's ORIGINAL
       recall round is a VIEW, always mounted, and its logic opened with
       `const q = this.questions[qi]` — so an empty list meant `q.o.map` threw
       during the first render and NOTHING drew, not even the class view. The
       throw turned a crash into a sentence.

       The amended round is a CONDITIONAL SURFACE (`if recallOpen`) and the
       class view no longer reads `this.questions` at all — the old round's
       renderVals block is retired with its markup, see student_rulings.py. So
       a class with no ladder rungs behind its lessons now gets its CLASS PAGE:
       its work, its lessons, its leaderboard, its flashcards. What it does not
       get is a recall button, because `recallLabel` is empty and the binding
       is marked `drop`.

       That is the whole trade, stated plainly: a student whose class has no
       recall bank used to lose the entire page over it. Now they lose one
       button. */

    /* ═══════════════════════════════════════════════════════════════════
       ── ⊕ 23 Aug 2026 — PHASE 2. THE FLASHCARD DECK ────────────────────
       ═══════════════════════════════════════════════════════════════════

       Design's C2 puts a deck of cards where the dark RECALL card was. This
       builds it, out of `ks3_cards` — the mirror this run authored, 582 rows,
       `SELECT to authenticated USING (true)`, so the client reads it directly
       with no backend route in between.

       ── WHICH LESSONS. THE UNION OF THE TWO THE PRODUCT ALREADY HAS ──────

       There is no `class_lessons` table; "the lessons this class has covered"
       is not a stored fact, and TWO parts of the page already answer it from
       different directions:

         a  every `assignment_questions.source_ref` behind every assignment the
            class has ever been set, resolved through `ks3_bank_questions` /
            `ks3_ladder_questions` to a lesson slug. That is `coveredSlugs`
            above — the SAME walk the work rows' "Open the lesson" button uses,
            read a second time rather than repeated.
         b  the lessons behind `/api/class/recall`, which is the endpoint whose
            own blurb on this page says "questions from the lessons this class
            has covered". The backend computes it from the class's scheme.

       Neither contains the other, measured on 8r/Sc1: (a) is
       `the-gas-exchange-system` + `particle-model`, from two assignments; (b)
       is `the-gas-exchange-system` alone. So the deck is their UNION — a
       lesson the class has been set work on, or one the scheme says they have
       been taught, is a lesson worth revising either way. Taking only (a)
       would lose a lesson taught but not yet assessed; taking only (b) would
       lose the hand-seeded May work, which is still the only marked work on
       the platform.

       ── AND THE DECK IS NOT CAPPED ───────────────────────────────────────

       `pad()` is two digits and the row of pips runs out of room, and neither
       of those is a reason to hide cards from a student. The pip row drops
       past 24 (see `PIP_MAX` in student_rulings.py); the counter stays right
       at any length; the deck itself is every card those lessons carry.

       ── A FAILURE HERE EMPTIES THE CARD; IT DOES NOT TAKE THE PAGE DOWN ──

       Same rule as `lessonsFor` above and the shout-outs below: the work is
       the page, and a card is a card. */
    (recall && recall.questions ? recall.questions : []).forEach(function (q) {
      if (q.lesson_slug) { coveredSlugs[q.lesson_slug] = true; }
    });
    var deckSlugs = Object.keys(coveredSlugs);

    /* ── WHICH LESSONS DID THIS STUDENT GET SOMETHING WRONG IN? ───────────

       ⚠️ A CARD ID IS NOT A QUESTION REF, AND THE JOIN IS AT LESSON GRAIN.
       Checked against the real rows rather than taken from the brief: a card
       is `the-gas-exchange-system#def#trachea`, an attempt's `question_ref` is
       a bank id (`b4-01-s01`) or a ladder ref (`<lesson>#recall`) or, for the
       hand-seeded May work, the lesson PATH. The two corpora share no id of
       any kind, so nothing finer than the lesson is available — and the lesson
       is the right grain anyway: a student who got the trachea question wrong
       needs that lesson's vocabulary, not only the one term they missed.

       Readable client-side under `attempts_self_all`, which is scoped through
       `assignment_submissions.student_id = auth_user_id()`. The submissions
       are read first and the attempts by `submission_id`, rather than through
       an embedded join, so the RLS the policy describes is the RLS the query
       relies on and nothing depends on PostgREST resolving a relationship. */
    var wrongLessons = {};
    try {
      if (assignmentIds.length) {
        var mySubs = await sb.from("assignment_submissions")
          .select("id").eq("student_id", user.id)
          .in("assignment_id", assignmentIds);
        if (mySubs.error) { throw mySubs.error; }
        var subIds = (mySubs.data || []).map(function (r) { return r.id; });
        if (subIds.length) {
          var att = await sb.from("assignment_question_attempts")
            .select("question_ref, is_correct")
            .in("submission_id", subIds).eq("is_correct", false);
          if (att.error) { throw att.error; }
          (att.data || []).forEach(function (r) {
            var slug = bySlug[r.question_ref] || slugFromRef(r.question_ref);
            if (slug) { wrongLessons[slug] = true; }
          });
        }
      }
    } catch (wrongErr) {
      console.error("[student-live] could not read this student's wrong "
                    + "answers; the deck loses its FROM YOUR WORK ordering "
                    + "and nothing else", wrongErr);
    }

    var cards = [];
    try {
      if (deckSlugs.length) {
        var cq = await sb.from("ks3_cards")
          .select("id, lesson_slug, kind, card_position, topic, front, back, "
                  + "equation_left, equation_arrow, equation_right, "
                  + "equation_condition")
          .in("lesson_slug", deckSlugs)
          .order("lesson_slug").order("card_position");
        /* A refusal here is silent otherwise — supabase-js RESOLVES with an
           `error` rather than rejecting, so `.data` would simply be null and
           the deck would be empty with nothing said anywhere. The card's own
           empty state is honest either way; the console line is what tells
           whoever is looking that it is empty for a REASON. */
        if (cq.error) { throw cq.error; }
        cards = (cq.data || []).map(function (r) {
          var eq = r.kind === "equation";
          var card = {
            id: r.id,
            lesson: r.lesson_slug,
            /* Design's own two tags. `KEY FACT` is Design's third and there
               are no key-fact rows: the exporter deliberately ships none,
               because a key fact is a statement with no authored front, and
               writing 107 science prompts is Mide's gate rather than an
               export's. A tag with no rows behind it is not emitted. */
            tag: eq ? "EQUATION" : "DEFINITION",
            topic: String(r.topic || deslug(r.lesson_slug)).toUpperCase(),
            front: r.front || "",
            /* ⚠️ AN EQUATION CARD'S ANSWER IS THE EQUATION ROW, NOT THE PROSE
               SLOT. Design draws an equation card with `back: ''` and lets the
               left → right row below it be the answer, and printing the
               right-hand side twice would be the page saying the same thing in
               two type sizes. What DOES go in the prose slot is the authored
               CONDITION where the lesson wrote one ("energy is transferred
               from the glucose to the cell") — verbatim, because it is part of
               the answer and it is somebody's sentence, not a composed one. */
            back: eq ? (r.equation_condition || "") : (r.back || ""),
            /* Design's chip. True for every card from a lesson this student
               has got a question wrong in — see the join above. */
            mine: !!wrongLessons[r.lesson_slug]
          };
          if (eq) {
            /* ⚠️ `arrow` IS A FLAG, NOT THE WORD, and that is Design's reading
               rather than an assumption: Design's `<if card.arrow>` gates the
               whole equation ROW, and the row draws the arrow as an SVG (donor
               357/358) and never prints `card.arrow` anywhere. So the mirror's
               `equation_arrow` — a WORD like 'gives', or NULL — is exactly what
               its own column comment says it is: NULL means DRAW the arrow and
               do not read it, not "there is no arrow". Five of the nine
               equation rows carry NULL and all nine must draw one.
               ⛔ AND NOTHING HERE MAY TYPE ONE. A CHECK constraint refuses
               U+2192 in the mirror; the page draws Design's path and never a
               glyph. */
            card.arrow = true;
            card.eqLeft = r.equation_left || "";
            card.eqRight = r.equation_right || "";
          }
          /* `triangle` is DELIBERATELY NEVER SET. Design draws a formula
             triangle for `p = F / A` with the letters F, p and A typed into
             the SVG — a drawing of ONE equation, not a component — and the
             mirror has no triangle content of any kind to drive it with. A
             branch with no data behind it renders nothing, which is the
             correct outcome; faking one would put Design's pressure triangle
             on a chemistry card. */
          return card;
        });
      }
    } catch (cardErr) {
      console.error("[student-live] could not build the flashcard deck", cardErr);
      cards = [];
    }

    /* ── AND THE ORDER, WHICH IS WRITTEN IN ONE PLACE ────────────────────
       `rankForPractice` — wrong first, then least-seen, then a fixed jitter.
       The seed is the class and the school-local DATE, so the deck is stable
       for a session AND across a reload (a student who refreshes does not get
       a reshuffled stack under their finger) and moves tomorrow. */
    var deckSeen = seenStore(user.id, klass.id);
    cards = rankForPractice(cards, {
      wrong: wrongLessons,
      seen: deckSeen.all(),
      seed: klass.id + "|" + londonYmd(serverNow)
    });

    /* ═══════════════════════════════════════════════════════════════════
       ── ⊕ 23 Aug 2026 — PHASE 3. THE RECALL BANK ───────────────────────
       ═══════════════════════════════════════════════════════════════════

       Design's C2b round draws from "the recall and apply rungs of every
       lesson the class has covered". Two sources could answer that, and both
       were measured on 8r/Sc1 before one was chosen:

         a  `/api/class/recall`, already called at the top of this function.
            It returns the rungs of the lessons the class's SCHEME says have
            been taught — for 8r/Sc1, `the-gas-exchange-system` alone, so TWO
            questions.
         b  `ks3_ladder_questions` read directly, filtered by `deckSlugs` —
            the covered-lesson set Phase 2 already assembled, which is the
            UNION of the scheme's lessons and every lesson behind every
            assignment this class has ever been set. For 8r/Sc1 that is
            `the-gas-exchange-system` + `particle-model`, so FOUR.

       (b), and the reason is not that it is bigger. It is that (a) cannot see
       the hand-seeded May work at all — the only marked work on the platform —
       and a round drawn from (a) would leave a student unable to practise the
       one lesson they have a mark in. (a) is a strict SUBSET of (b) here; the
       endpoint stays exactly where it is and still supplies `questions` and
       the teaching week.

       ⚠️ AND THE COVERED-LESSON SET IS NOT RESOLVED A THIRD TIME. `deckSlugs`
       is the same variable the flashcard deck reads, filled by the same single
       walk of `assignment_questions.source_ref` that the work rows' "Open the
       lesson" button uses. Three surfaces, one answer to "which lessons has
       this class covered".

       ⚠️ THE TABLE HAS NO `topic` COLUMN — checked against the schema, not
       assumed. `/api/class/recall` composes one; a direct read has to derive
       it, and `deslug(lesson_slug)` is what this file already falls back to
       for exactly that value, so the two routes agree.

       ⛔ NOTHING HERE IS HANDED IN. This is a SELECT and there is no writer
       anywhere in the round: no submission row, no attempt row, no score. The
       only thing a round writes is a per-device seen count, in localStorage,
       for the ordering — see `QSEEN_PREFIX`. */
    var recallBank = [];
    try {
      if (deckSlugs.length) {
        var lq = await sb.from("ks3_ladder_questions")
          .select("question_ref, lesson_slug, unit_code, rung, text, "
                  + "answer_letter, options")
          .in("lesson_slug", deckSlugs)
          .in("rung", ["recall", "apply"])
          .order("lesson_slug").order("rung");
        /* supabase-js RESOLVES with an `error` rather than rejecting, so
           without this the bank would simply be empty and nothing would say
           why — the same silence the deck's own read documents. */
        if (lq.error) { throw lq.error; }
        (lq.data || []).forEach(function (r) {
          var n = normalise(r.options, r.answer_letter);
          if (!n) { return; }
          recallBank.push({
            /* ⚠️ THE ID IS `question_ref`, AND IT IS THE ONLY id this corpus
               has. `rankForPractice` keys `opts.seen` on `it.id` and
               `opts.wrong` on `it.lesson`, so this is what a seen count is
               recorded against and what a second round is stopped from
               repeating. It is stable across a re-export: it is composed from
               the lesson slug and the rung, never from a position. */
            id: r.question_ref,
            lesson: r.lesson_slug,
            topic: deslug(r.lesson_slug).toUpperCase(),
            q: r.text || "",
            options: n.o,
            answer: n.a,
            /* ⚠️ `notes`, PLURAL, AND DESIGN'S IS SINGULAR. Design's amended
               sample carries ONE teaching note per question and shows it
               whatever the student picked. This corpus carries a `why` per
               OPTION and — measured across both content sources, and recorded
               in the 21 Aug ruling — the ones that exist are always the
               DISTRACTORS. So the round shows the line written against the
               answer the student actually gave, which is where the teaching
               lands, and a correct answer gets the verdict word and nothing
               else. `recallVals` reads whichever shape it is handed, so the
               fixture keeps Design's behaviour byte for byte. */
            notes: n.f
          });
        });
      }
    } catch (bankErr) {
      console.error("[student-live] could not build the recall bank", bankErr);
      recallBank = [];
    }

    /* ── THE SAME ORDER, FROM THE SAME FUNCTION ───────────────────────────
       `rankForPractice` — wrong first, then least-seen, then a fixed jitter.
       Written once, in this file, and called by the deck above and the round
       here; a second implementation of "what should this student practise
       next" would drift invisibly, because nothing on the page states the
       order.

       The seed carries `|recall` so the two corpora do not receive the same
       jitter for the same lesson and end up correlated — the deck and the
       round should not agree about which lesson to lead with just because
       they happen to hash the same slug. */
    var recallSeen = seenStore(user.id, klass.id, QSEEN_PREFIX);
    recallBank = rankForPractice(recallBank, {
      wrong: wrongLessons,
      seen: recallSeen.all(),
      seed: klass.id + "|recall|" + londonYmd(serverNow)
    });

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
      },
      /* ⊕ 23 Aug 2026 — PHASE 2. A card was REVEALED. It writes to this
         device and reaches no network at all, which is the whole argument for
         where the count lives — see `seenStore`. It returns whether the write
         landed; nothing reads that today, and it is returned rather than
         swallowed because a writer that cannot report a refusal is how the
         held-state defect got shipped once already. */
      cardSeen: function (cardId) {
        return deckSeen.bump(cardId);
      },
      /* ⊕ 23 Aug 2026 — PHASE 3. A recall question was ANSWERED. Same store
         shape, same device-only argument, different corpus and a different
         event: a card counts as seen when it is REVEALED, a question when it
         is CHECKED. Reaches no network, writes no row — the round hands
         nothing in, and this is the only thing it records anywhere. */
      questionSeen: function (questionRef) {
        return recallSeen.bump(questionRef);
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

      /* ── ⊕ 23 Aug 2026 — PHASE 2. THE DECK, AND ITS TWO WORDS ──────────
         `cards` is every card behind every lesson this class has covered,
         already in practice order. The page does not sort it, cap it or
         choose from it — it reads `MRB_DATA('cards')` and shows what is
         there, which keeps the one definition of "what should this student
         practise next" in this file where the next unit can call it too. */
      cards: cards,

      /* ⛔ WHAT THE CARD SAYS WITH AN EMPTY DECK, and it says nothing about
         the software. It is the sentence this file already uses for the same
         condition one panel over — there is nothing to look back over yet —
         rather than a second wording of the same fact. The card's button
         refuses to open an empty overlay (see `openCards` in
         student_rulings.py), so a student is never taken to a surface with a
         counter reading 00 / 00 on it. */
      cardsEmpty: SAY.noRecall,

      /* ── ⊕ 23 Aug 2026 — PHASE 3. THE ROUND'S THREE KEYS ───────────────

         `recallBank` is every recall and apply rung behind every lesson this
         class has covered, already in practice order. The page does not sort
         it, cap it or choose from it: `recallVals` in student_rulings.py takes
         the first `min(6, length)` of it, which is ruling P2's round size, and
         states that size in the two places the round prints a number.

         Design's `bank()` on the fixture is eight authored samples; this is
         the real one, and on 8r/Sc1 today it is FOUR. */
      recallBank: recallBank,

      /* ⊕ RULED 22 Aug 2026 — P2, HONOURED BY THE NEW SURFACE. "The round is
         min(6, pool), and the page has to say the size it is actually going to
         show." The two text nodes that used to state it in a WORD — Design's
         `SIX QUESTIONS · UNLIMITED ROUNDS` eyebrow and its `OF SIX` caption —
         are retired with the old round's markup. What states the size now is
         `qPos` ("QUESTION 01 / 04") and `roundScore` ("2 / 4"), both computed
         from the real length, so there is no wording left that CAN be wrong. */

      /* Design typed `8r/Sc1 \u00a0·\u00a0 RECALL` into the round's band as
         ONE text node with NON-BREAKING spaces — the same trap
         `flashcardsTitle` and `accountClassLine` both document, and it would
         have shipped one real class's name at the top of every student's
         round. Composed here from the class name this function already holds;
         the separator is Design's typography and is carried verbatim. */
      recallTitle: name + " \u00a0\u00b7\u00a0 RECALL",

      /* ⛔ THE BENCH BUTTON GOES WHEN THERE IS NOTHING TO PRACTISE. Design's
         `Practise recall` is a real control, and a class whose covered lessons
         carry no ladder rungs would have one that opens nothing — the dead
         control P7 exists to prevent. The binding is marked `drop`, so an
         empty value takes the BUTTON with it rather than leaving an empty
         bordered box, which is the `envBadge` shape exactly.

         Not a disabled button and not an explanatory sentence: §8.10 forbids
         the page explaining itself, and a greyed-out control a student cannot
         act on is a worse answer than a bench that simply offers what it has. */
      recallLabel: recallBank.length ? "Practise recall" : "",

      /* Design typed `FLASHCARDS \u00a0·\u00a0 8r/Sc1` into the overlay's
         header as ONE text node with NON-BREAKING spaces, which is why it
         cannot bind to the `8r/Sc1` already on the binding list — the same
         trap `accountClassLine` documents. Composed from the class name this
         function already holds; the separator is Design's typography and is
         carried through verbatim. */
      flashcardsTitle: "FLASHCARDS \u00a0\u00b7\u00a0 " + name,

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
      /* ⊕ 23 Aug 2026 — PHASE 4. THE `benchDone ?` ARM IS GONE, and the
         ruling it served is kept by the graft instead: the docket this key
         feeds is node 91, inside the grid that no longer renders once the week
         is finished. Design's done bench draws its OWN docket with its own
         chip — `benchDoneFlag` below — so keeping the arm would have been two
         answers to one question, in two elements that are never both there.
         What it used to read:

             benchDone ? (benchMarked ? "MARKED" : "COMPLETE") : …

         and the MARKED / COMPLETE distinction survives verbatim, on the
         surface Design drew for it. */
      docketFlag: (benchCard && benchCard.due_at
                   && Date.parse(benchCard.due_at) < serverNow)
        ? "MISSED" : "OPEN",
      /* Once the work is done the deadline is not the story, and the slot is
         directly above the answered-progress bar — so it LABELS that bar
         instead, which is the other half of the 22 Aug progress ruling
         ("'5 of 15 answered' and the same as a percentage"). An unlabelled
         full bar was what emptying it left behind, and a graphic with no
         words is not an honest blank. */
      /* ⊕ 23 Aug 2026 — PHASE 4. Same removal, same reason: this slot is on
         the OPEN docket, and once the week is done that docket is not drawn.
         The finished-week reading it used to carry — "5 of 15 answered" — is
         now the done bench's OPENED · ANSWERED · COMPLETED row, which says the
         same thing about the same numbers in the place Design put it. */
      docketLeft: current && current.assignment
        ? daysLeft(current.assignment.due_at, serverNow) : "",

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
      /* ── ⊕ 23 Aug 2026 — PHASE 4. THE INTERIM DONE STATE COMES OFF ────
         These two are the OPEN bench's eyebrow and paragraph, and until
         tonight they carried the done state too. What they used to say when
         the week was finished:

             "Good week, Ayo · completed SAT 23 AUG · late"
             "You scored 2 out of 4. Go back over the lesson whenever you
              want, or practise your recall."

         Both were P4 arranging Design's OPEN bench into a done one, which was
         the right answer while there was no done bench to draw. There is one
         now — `benchDoneLead` below is the sentence, the score is in the
         docket where Design put it, and the two actions are two controls
         rather than a clause. The arms come off here, in the same commit as
         the graft, so there is never a build with both.

         ⚠️ AND THE OPEN ARMS ARE UNTOUCHED. Nothing about a student with work
         still on the bench changes tonight. */
      benchLead: current && current.assignment && current.assignment.due_at
        ? "On the bench now · due " + fmtDueMixed(current.assignment.due_at)
        : "On the bench now",
      benchBlurb: (currentCount && current && current.assignment
                   && current.assignment.due_at)
        ? (currentCount + " questions, set from this week's lessons. " +
           "Open it, answer them, and complete it before " +
           weekdayName(current.assignment.due_at) + ".")
        : "Set from this week's lessons. Open it, answer the questions, "
          + "and complete it.",

      /* W5, in the readings strip. */
      handedLabel: "Completed",
      handedCaption: "OF COMPLETED",

      /* ⊕ RULED 22 Aug 2026 — P4. THE CHECKLIST DOES NOT RENDER when the
         week is done.
         ⊕ 23 Aug 2026 — PHASE 4, AND IT NO LONGER NEEDS TO SAY SO. The empty
         array was `benchDone ? [] : […]`; the checklist lives inside the grid
         that is now gated on `benchOpen`, so on a finished week the whole
         branch above it is absent and there is no list to empty. The ruling is
         kept by the structure instead of by a flag — which is what P4's own
         note asked for: "when Design's redraw is ported it replaces markup,
         not logic". */
      benchTasks: [
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
      /* ⊕ 23 Aug 2026 — PHASE 4. ONE FACT, ONE NEGATION. Design's amended
         bench is two branches and names them `benchOpen` and `benchDone`;
         `build_student_port.py` wraps the live grid in the first and grafts
         the second beside it. Emitting the negation here rather than writing
         `!benchDone` into the template is what makes it impossible for the two
         to disagree — there is no state in which both branches or neither is
         on the page. */
      benchOpen: !benchDone,

      /* ── the done bench, from the real submission ─────────────────────
         ⊕ 23 Aug 2026 — PHASE 4. Design's `bench-done` region, donor 101. The
         three booleans gate parts of it that are only sometimes true; the rest
         are the values themselves. Every one is derived above, from
         `benchCard` and from `progress`, and from nothing else. */
      benchDoneMarked: benchMarked,
      benchDoneLessons: benchLessons.length > 0,
      /* The destination for "Read the feedback", and the flag that decides
         whether the link is drawn at all — one string doing both jobs, so
         there is no way to show a link with nowhere to go. It is the
         ASSIGNMENT page: a returning student with a completed submission lands
         on its done screen, which is the only surface on the platform that
         shows their own answer, the authored explanation for it and the right
         answer beside it. The work list's rows carry none of that — `notes`
         and `items` are omitted a hundred lines above, because nothing records
         a teacher's written feedback and this page does not read the
         per-question attempts. */
      benchDoneFeedback: (current && current.assignment) ? assignmentHref() : "",
      benchDoneTitle: benchTopic,
      benchDoneLead: first ? "Good week, " + first + "." : "Good week.",
      benchDoneSteps: benchSteps + " / 3",
      benchDoneFlag: benchMarked ? "MARKED" : "COMPLETE",
      /* Empty rather than a dash when there is no mark yet: the two rows that
         hold these are gated on `benchDoneMarked` and are not on the page at
         all in that state, so an empty string here can never be rendered. */
      benchDoneScore: benchPct == null ? "" : benchPct + "%",
      benchDoneRight: benchMarked
        ? (benchCard.score + " of " + benchCard.max_score) : "",
      /* The completion stamp, in the docket's own mixed-case shape — the same
         `fmtDueMixed` the OPEN docket prints its deadline with, so the two
         dockets speak about time the same way. Lateness rides with it because
         Design's done bench draws no other slot for it, and a completion time
         with no note that it was after the deadline is a fact with the
         interesting half missing. */
      benchDoneAt: fmtDueMixed(benchCard && benchCard.submitted_at)
        + (benchLate ? " · late" : ""),

      /* ⊕ 23 Aug 2026 — PHASE 4. ONE VALUE AGAIN, AND IT IS DESIGN'S. The
         interim forked this label — "Revisit the lesson" / "Practise recall"
         once the week was done — because the same button had to serve both
         states. Design's done bench has its own two controls, and the button
         this names is inside the branch that no longer renders beside them. */
      benchPrimaryLabel: "Open the assignment",
      benchPrimaryHref: (current && current.assignment) ? assignmentHref() : "",
      /* ⊕ 23 Aug 2026 — PHASE 4. `benchPct` and `benchDoneText` are GONE from
         this object. They filled the open bench's meter and its caption with
         the MARK once the week was done; that meter is not drawn on a finished
         week any more, and the ruled override that read them through
         `MRB_DATA` came off in the same commit, so Design's own expressions
         (how much of the checklist is ticked) are the only readings left and
         they are computed in Design's own logic. What they used to say:

             benchPct:      "50%" — the mark, or "100%" unmarked
             benchDoneText: "2 / 4 MARKS", or "NOT MARKED YET"

         Both facts survive, on the done bench's docket, as `benchDoneScore`
         and `benchDoneRight`. */

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
  async function buildAssignment(klass, token, userId) {
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
    pendingSink = makeSink(a, questions, progress, token, userId);

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
    boot(page);                     // ← before the first byte is asked for
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
          correctAddress(klass);

          var data = page === "assignment"
            ? await buildAssignment(klass, token, ctx.user.id)
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
