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
    "/shared/student-data.js"
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
  function loadScript(src) {
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

  /* Autumn / Spring / Summer, from the SERVER's clock (the `Date` header of
     the backend response), read in school-local time. The database records no
     term boundaries; the months are how the English school year actually runs
     and are the same for every school on the platform. */
  function termLabelFrom(serverNow) {
    var month = Number(new Intl.DateTimeFormat("en-GB", {
      timeZone: LONDON, month: "numeric"
    }).format(new Date(serverNow)));
    if (month >= 9 && month <= 12) { return "AUTUMN TERM"; }
    if (month >= 1 && month <= 3)  { return "SPRING TERM"; }
    return "SUMMER TERM";
  }

  /* ── the backend ───────────────────────────────────────────────────────
     Bearer token from the live session. The response's `Date` header is the
     SERVER clock, and it is the only "now" this file trusts for deciding what
     is due — never `new Date()`, which is the device's opinion. The device
     clock is used for nothing but choosing how to print a timestamp. */
  var serverNow = null;

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
        detailLine = "HANDED IN " + fmtDay(c.submitted_at) +
                     " · " + c.score + " OF " + c.max_score + " MARKS";
      } else if (status === "pending") {
        detailLine = "HANDED IN " + fmtDay(c.submitted_at) + " · NOT MARKED YET";
      } else if (status === "missed") {
        detailLine = fmtDue(c.due_at) + " · NOT HANDED IN";
      } else {
        detailLine = fmtDue(c.due_at);
      }

      var row = {
        id: c.id,
        week: weekOf(c),
        title: c.title || "",
        brief: brief,
        status: status,
        detail: detailLine
      };
      if (status === "marked" && c.max_score > 0) {
        row.score = Math.round((c.score / c.max_score) * 100);
      }
      if (c.is_submitted && c.due_at && !c.on_time) { row.late = true; }
      return row;
    });

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
        on: true
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
    var first = (v.first_name || "").trim();
    var name = klass.name || "";

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

      subjectLabel: klass.pill_label || "",
      termLabel: termLabelFrom(serverNow),
      topicTitle: current && current.assignment
        ? (current.assignment.topic || current.assignment.title || "")
        : ""
    };
  }

  // ── the assignment ────────────────────────────────────────────────────
  async function buildAssignment(klass, token) {
    var current = await api("/api/class/current-assignment?class_id=" + klass.id, token);

    /* `assignment: null` with a reason is a NORMAL state — no current week, no
       scheme row, nothing banked yet. It means no work is set, not an error. */
    if (!current || !current.assignment) {
      var none = new Error(current && current.reason ? current.reason : "no assignment");
      none.mrbSay = SAY.noWork;
      throw none;
    }

    var a = current.assignment;
    var questions = [];
    (current.questions || []).forEach(function (q) {
      if (q.retired) { return; }        // the bank no longer has it; do not draw a blank
      var n = normalise(q.options, null);
      if (!n) { return; }
      questions.push({
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

    /* The page's own floor is six (`count()` returns at least 6 and then
       indexes that far), so a shorter set would run off the end of the array
       mid-assignment. */
    if (questions.length < 6) {
      var short = new Error("assignment has " + questions.length + " usable questions");
      short.mrbSay = SAY.workNotSet;
      throw short;
    }

    var name = klass.name || "";
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

      className: name,
      backToClass: "Back to " + name,
      topicTitle: a.topic || a.title || ""
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

          /* The assignment page routes off the URL hash and falls back to
             'Mid-way' — a DEMO scenario that pre-fills six answers, three of
             them deliberately wrong. On a real student's assignment that is
             not a default, it is a lie. '#live' is the page's own name for
             "this student's saved answers and nothing else", so that is what
             it gets. Replaced, not pushed, so Back still leaves the page.
             ⚠️ This is a workaround for a default in the page; see handover. */
          if (page === "assignment" && window.location.hash !== "#live") {
            window.history.replaceState(null, "", "#live");
          }

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
