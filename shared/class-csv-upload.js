/* ═══════════════════════════════════════════════════════════════════════
   class-csv-upload.js — "Add pupils (CSV)" on a class's own page.

   Surface:  window.MrBadmusClassCsvUpload.open({classId, className})
             window.MrBadmusClassCsvUpload.close()

   One job: put a few more children into a class that ALREADY EXISTS, from
   a CSV, without leaving the class page. It creates nothing else — no
   class, no removal, no move between classes. The pipeline underneath is
   the one `teacher/import.html` has always used
   (`supabase/functions/roster-import`), entered by CLASS ID rather than by
   class name, which is the backend's `ClassSpec.id` path.

   ── WHY IT IS NOT A COMPILED COMPONENT ────────────────────────────────

   The same reason `shared/set-work.js` is not one, in its own words:
   `shared/student-runtime.js`'s `draw()` empties the ENTIRE `#mrb-teacher`
   mount host and rebuilds it from the template on every `setState`
   (student-runtime.js:497-498). It restores the document's scroll and no
   element's `scrollTop`. So this module owns ONE overlay, appended to
   `document.body`, a SIBLING of the mount host: `draw()` cannot see it and
   a page-level `setState` cannot disturb it.

   ── WHY THE TRIGGER IS INJECTED RATHER THAN DRAWN ─────────────────────

   Design drew no such button — the feature did not exist when she
   delivered the template — and the button is ADMIN-ONLY, which the
   compiled tree has no way to express: an `<if>` in `teacher_rulings.
   INSERT_AT` resolves against `renderVals`, a synchronous object built
   before any scope question has been asked. The repo's own precedent for a
   SCOPE-GATED entry on a ported page is `shared/teacher-admin-nav.js`,
   which appends its link after the runtime has drawn and re-appends it
   after every redraw through a MutationObserver. This follows it exactly,
   including the observer — a one-shot append survives until the teacher's
   first click and then vanishes, which is precisely the defect a
   screenshot taken straight after load reports as working.

   ── THE ADMIN GATE, AND WHAT IT IS NOT ────────────────────────────────

   `window.MrBadmusAdminScope.isAdmin(sb, uid)` — ONE predicate, borrowed
   rather than re-derived, exactly as `teacher-live.js` borrows it and
   `teacher/admin.html` does. ⚠️ `class-detail.html` does not carry that
   script (its spec has `admin_nav=False`, MRB-303's deliberate exclusion),
   so this module LOADS it on demand. Its own boot then runs: on this page
   "Today" is already in the tab strip so `todayAlreadyInBar` refuses the
   duplicate, and the only visible consequence is that an admin-scoped
   viewer also gets the "Admin" link the other five ported screens already
   show. A non-admin sees no change of any kind.

   ⚠️ NOT THE SECURITY BOUNDARY — same standing as the note in
   `teacher-admin-nav.js`. Hiding a button hides a button. The boundary is
   the edge function, which re-derives the caller's standing server-side
   and refuses the id path with `admin_only`; a 403 is surfaced here in
   plain English rather than swallowed.

   ── THE COUNTS ARE THE PIPELINE'S, NOT OURS ───────────────────────────

   No dedup, no matching and no counting happens in this file. The three
   numbers the confirm step reads are derived from the response's own
   `counts`:

       newlyCreated     = counts.studentsCreated
       existingAttached = counts.studentsAttached - counts.studentsCreated
       alreadyInClass   = counts.studentsAlreadyAttached

   ⚠️ ON A DRY RUN `alreadyInClass` IS STRUCTURALLY ZERO, and that is the
   pipeline's shape rather than a bug here: roster-import's dry-run branch
   (index.ts:466-469) returns before the `class_members` lookup and counts
   every row as a fresh attach. So a child already in the class shows up in
   `existingAttached` on the PREVIEW and moves to `alreadyInClass` on the
   real run. The same derived line is therefore rendered again, in the past
   tense, from the real response — the truthful number is shown rather than
   the predicted one being left standing.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  /* The class screen, and nothing else. */
  var PAGE = "/teacher/class-detail.html";
  var MARK = "data-mrb-added";                 // the port's own marker attr
  var TRIGGER = "csv-open";
  /* Design's class action row (node 213 in the compiled tree). Its buttons
     are 214-217 plus the port's two additions; this is the eighth. */
  var ROW_SEL = '[data-dc-tpl="213"]';
  /* The same build, pinned, that `teacher/import.html` loads. */
  var PAPA = "https://cdn.jsdelivr.net/npm/papaparse@5/papaparse.min.js";

  /* ⚠️ BUTTON STYLE READ OFF THE ROW, NOT INVENTED. `_PICK_ENTRY_BTN` in
     teacher_rulings.py is node 216's string verbatim and the row's four
     secondaries all carry it; this is the same string, so the row cannot
     read as three buttons and a newcomer. */
  var BTN = "height:40px;padding:0 16px;font:600 17px/1.2 var(--st-ui);" +
            "color:var(--st-ink);background:var(--st-paper);" +
            "border:1px solid var(--st-btn-border);border-radius:9px;" +
            "cursor:pointer";

  var SAY = {
    trigger: "Add pupils (CSV)",
    title: "Add pupils from a file",
    pick: "Choose a CSV file",
    preview: "Preview",
    confirm: "Add these pupils",
    cancel: "Cancel",
    done: "Done",
    notCsv: "That doesn't look like a CSV file. Choose a .csv file.",
    noHeaders: "We couldn't find any column headers in that file. " +
               "Make sure the first row names each column.",
    noRows: "That file has headers but no pupil rows.",
    noEmail: "We couldn't find an email column in that file.",
    unreadable: "We couldn't read that CSV. Check the file and try again.",
    checking: "Checking the file…",
    adding: "Adding…",
    adminOnly: "Only a school admin can add pupils from a file.",
    wrongYear: "That class belongs to a different academic year.",
    notFound: "We couldn't find that class.",
    generic: "That didn't go through. Try again in a moment.",
    issues: "Rows we skipped or changed"
  };

  var state = {
    classId: "",
    className: "",
    isAdmin: false,
    file: null,
    rows: [],
    headers: [],
    map: null,
    hash: "",
    busy: false,
    stage: "pick"            // pick | preview | done
  };
  var els = null;
  var papaPromise = null;

  /* ═════════════════════════════════════════════════════════════════════
     1. SMALL HELPERS
     ═════════════════════════════════════════════════════════════════════ */

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) { n.className = cls; }
    if (text != null) { n.textContent = text; }
    return n;
  }

  /* `pluralPart`, verbatim from teacher/import.html:2285. */
  function pluralPart(n, singular, plural) {
    return n + " " + (n === 1 ? singular : (plural || singular + "s"));
  }

  function qs() { return new URLSearchParams(window.location.search); }

  function client() {
    var g = window.MrBadmusTeacherGuard;
    return (g && g.getClient) ? g.getClient() : null;
  }

  /* Bounded wait for teacher-guard.js, which `teacher-live.js` loads for
     itself through `loadDeps()` — reading once and giving up is why an
     injector like this works on the hand-written pages and silently does
     nothing on the ported ones. A timeout is simply "no button", which on
     a fixture (no config, no SDK, no session) is the correct outcome. */
  function waitForClient(ms) {
    var deadline = Date.now() + (ms || 15000);
    return new Promise(function (resolve) {
      (function tick() {
        var sb = client();
        if (sb) { return resolve(sb); }
        if (Date.now() > deadline) { return resolve(null); }
        setTimeout(tick, 120);
      })();
    });
  }

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var have = document.querySelector('script[src="' + src + '"]');
      if (have && have.getAttribute("data-mrb-loaded") === "1") {
        return resolve();
      }
      var s = document.createElement("script");
      s.src = src;
      s.onload = function () { s.setAttribute("data-mrb-loaded", "1"); resolve(); };
      s.onerror = function () { reject(new Error("could not load " + src)); };
      document.head.appendChild(s);
    });
  }

  function papa() {
    if (window.Papa) { return Promise.resolve(window.Papa); }
    if (!papaPromise) {
      papaPromise = loadScript(PAPA).then(function () { return window.Papa; });
    }
    return papaPromise;
  }

  /* SHA-256 hex, the same `source.fileHash` teacher/import.html sends
     (import.html:1605-1613). */
  function sha256Hex(text) {
    return crypto.subtle.digest("SHA-256", new TextEncoder().encode(text))
      .then(function (d) {
        return Array.from(new Uint8Array(d)).map(function (b) {
          return b.toString(16).padStart(2, "0");
        }).join("");
      });
  }

  /* ═════════════════════════════════════════════════════════════════════
     2. THE CLASS — ITS ID AND ITS REAL DB NAME

     ⚠️ THE NAME MUST BE THE DB ROW'S OWN. roster-import matches a student
     row to a class by `className` string equality against the name it read
     out of the `classes` row, so a name that is merely close attaches
     nobody and reports every row `unknown_class`.

     `window.__MRB_DATA__.CLASSES[].code` IS that string —
     `shared/teacher-live.js:2005` sets `code: c.name` straight off the
     row — so this is a read of data the page has already fetched, not a
     second query and not a scrape.
     ═════════════════════════════════════════════════════════════════════ */

  function classNameFor(id) {
    var d = window.__MRB_DATA__;
    var lists = [d && d.CLASSES, d && d.SET_WORK_CLASSES];
    for (var i = 0; i < lists.length; i++) {
      var rows = lists[i] || [];
      for (var j = 0; j < rows.length; j++) {
        if (rows[j] && String(rows[j].id) === String(id) && rows[j].code) {
          return String(rows[j].code);
        }
      }
    }
    return "";
  }

  /* ═════════════════════════════════════════════════════════════════════
     3. THE TRIGGER — injected after draw, re-injected after every redraw
     ═════════════════════════════════════════════════════════════════════ */

  function injectTrigger() {
    var row = document.querySelector(ROW_SEL);
    if (!row) { return false; }
    if (row.querySelector("[" + MARK + '="' + TRIGGER + '"]')) { return true; }
    var b = el("button", null, SAY.trigger);
    b.type = "button";
    b.setAttribute(MARK, TRIGGER);
    b.style.cssText = BTN;
    b.addEventListener("mouseenter", function () {
      b.style.borderColor = "var(--st-edge)";
    });
    b.addEventListener("mouseleave", function () { b.style.borderColor = ""; });
    b.addEventListener("click", function () {
      open({ classId: state.classId, className: classNameFor(state.classId) });
    });
    row.appendChild(b);
    return true;
  }

  function watch() {
    injectTrigger();
    var mount = document.getElementById("mrb-teacher") || document.body;
    if (!mount || !window.MutationObserver) { return; }
    var pending = false;
    new MutationObserver(function () {
      if (pending) { return; }
      pending = true;
      (window.requestAnimationFrame || window.setTimeout)(function () {
        pending = false;
        injectTrigger();
      }, 0);
    }).observe(mount, { childList: true, subtree: true });
  }

  /* ═════════════════════════════════════════════════════════════════════
     4. THE OVERLAY

     One node, built once, appended to <body>. Everything below 390px is a
     single column: the sheet is `min(520px, 100vw - 24px)` and nothing
     inside it carries a fixed width.
     ═════════════════════════════════════════════════════════════════════ */

  var CSS = [
    ".ccu-scrim{position:fixed;inset:0;z-index:9000;display:flex;",
    "align-items:flex-end;justify-content:center;",
    "background:rgba(20,18,16,.44)}",
    "@media(min-width:600px){.ccu-scrim{align-items:center}}",
    ".ccu-sheet{width:min(520px,calc(100vw - 24px));max-height:88vh;",
    "overflow:auto;box-sizing:border-box;margin:12px;padding:18px;",
    "border-radius:14px;background:var(--st-paper,#fff);",
    "border:1px solid var(--st-rule-soft,#e6e1d9);",
    "box-shadow:0 18px 48px rgba(20,18,16,.22)}",
    ".ccu-head{display:flex;align-items:baseline;justify-content:space-between;",
    "gap:12px;flex-wrap:wrap}",
    ".ccu-title{font:600 20px/1.25 var(--st-ui,system-ui);",
    "color:var(--st-ink,#1a1714);margin:0}",
    ".ccu-code{font:500 13px/1.2 var(--st-mono,ui-monospace);",
    "letter-spacing:.1em;text-transform:uppercase;",
    "color:var(--st-caption,#8a8178)}",
    ".ccu-body{margin-top:16px;font:400 15.5px/1.45 var(--st-ui,system-ui);",
    "color:var(--st-ink,#1a1714)}",
    ".ccu-body p{margin:0 0 10px}",
    ".ccu-file{display:block;width:100%;box-sizing:border-box;margin-top:4px;",
    "font:400 15px/1.3 var(--st-ui,system-ui);color:var(--st-ink,#1a1714)}",
    ".ccu-note{font:400 14px/1.4 var(--st-ui,system-ui);",
    "color:var(--st-muted,#6b635a)}",
    ".ccu-warn{color:var(--danger,#FF6B6B)}",
    ".ccu-issues{margin:12px 0 0;padding:0 0 0 18px;",
    "font:400 14px/1.45 var(--st-ui,system-ui);color:var(--st-muted,#6b635a)}",
    ".ccu-issues li{margin:0 0 4px;overflow-wrap:anywhere}",
    ".ccu-foot{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}",
    ".ccu-btn{flex:1 1 auto;min-width:120px;height:42px;padding:0 14px;",
    "box-sizing:border-box;font:600 16px/1.2 var(--st-ui,system-ui);",
    "border-radius:10px;cursor:pointer;",
    "border:1px solid var(--st-btn-border,#d9d2c8);",
    "background:var(--st-paper,#fff);color:var(--st-ink,#1a1714)}",
    ".ccu-btn[disabled]{opacity:.45;cursor:default}",
    ".ccu-btn.ccu-primary{background:var(--st-ink,#1a1714);",
    "border-color:var(--st-ink,#1a1714);color:var(--st-paper,#fff)}"
  ].join("");

  function buildShell() {
    if (els) { return; }
    var style = el("style");
    style.textContent = CSS;
    document.head.appendChild(style);

    var scrim = el("div", "ccu-scrim");
    scrim.hidden = true;
    var sheet = el("div", "ccu-sheet");
    sheet.setAttribute("role", "dialog");
    sheet.setAttribute("aria-modal", "true");
    sheet.tabIndex = -1;

    var head = el("div", "ccu-head");
    var title = el("h2", "ccu-title", SAY.title);
    var code = el("div", "ccu-code");
    head.appendChild(title);
    head.appendChild(code);

    var body = el("div", "ccu-body");
    var file = el("input", "ccu-file");
    file.type = "file";
    file.accept = ".csv";
    var note = el("p", "ccu-note");
    var summary = el("p");
    var issues = el("ul", "ccu-issues");
    issues.hidden = true;
    body.appendChild(file);
    body.appendChild(note);
    body.appendChild(summary);
    body.appendChild(issues);

    var foot = el("div", "ccu-foot");
    var cancel = el("button", "ccu-btn", SAY.cancel);
    cancel.type = "button";
    var primary = el("button", "ccu-btn ccu-primary", SAY.preview);
    primary.type = "button";
    primary.disabled = true;
    foot.appendChild(cancel);
    foot.appendChild(primary);

    sheet.appendChild(head);
    sheet.appendChild(body);
    sheet.appendChild(foot);
    scrim.appendChild(sheet);

    /* ⚠️ APPENDED TO <body>, NOT INTO `#mrb-teacher` — see the header. */
    document.body.appendChild(scrim);

    els = { scrim: scrim, sheet: sheet, code: code, file: file, note: note,
            summary: summary, issues: issues, cancel: cancel,
            primary: primary };

    cancel.addEventListener("click", close);
    scrim.addEventListener("click", function (e) {
      if (e.target === scrim && !state.busy) { close(); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !scrim.hidden && !state.busy) { close(); }
    });
    file.addEventListener("change", function () {
      onFile(file.files && file.files[0]);
    });
    primary.addEventListener("click", function () {
      if (state.stage === "done") { return close(); }
      if (state.stage === "preview") { return send(false); }
      send(true);
    });
  }

  function note(text, warn) {
    els.note.textContent = text || "";
    els.note.classList.toggle("ccu-warn", !!warn);
  }

  /* ═════════════════════════════════════════════════════════════════════
     5. THE FILE — parsed and column-matched exactly as import.html does

     ⚠️ `GUESS_RE` IS teacher/import.html:1845-1852 VERBATIM, minus the
     `className` entry: the class is fixed by the page this opened from, so
     a class column here would be a second answer to a settled question.
     `external` deliberately does not match email/upn.
     ═════════════════════════════════════════════════════════════════════ */

  var GUESS_RE = {
    email:     /e-?mail/i,
    firstName: /first|forename|given/i,
    lastName:  /last|surname|family/i,
    external:  /synergy|admission|adm(\s*no)?|uln|mis|student\s*id|candidate|pupil/i
  };

  function guess(headers, re, optional) {
    var m = headers.find(function (h) { return re.test(h); });
    if (m) { return m; }
    return optional ? "" : (headers[0] || "");
  }

  function resetResult() {
    state.stage = "pick";
    els.summary.textContent = "";
    els.issues.textContent = "";
    els.issues.hidden = true;
    els.primary.textContent = SAY.preview;
    els.primary.disabled = !state.rows.length;
  }

  function onFile(f) {
    state.file = null;
    state.rows = [];
    state.headers = [];
    state.map = null;
    state.hash = "";
    resetResult();
    if (!f) { return note(""); }
    if (!/\.csv$/i.test(f.name) && f.type !== "text/csv") {
      return note(SAY.notCsv, true);
    }
    note(SAY.checking);

    var reader = new FileReader();
    reader.onerror = function () { note(SAY.unreadable, true); };
    reader.onload = function () {
      var text = String(reader.result || "");
      sha256Hex(text).then(function (h) { state.hash = h; },
                          function () { state.hash = ""; });
      papa().then(function (P) {
        var res = P.parse(text, { header: true, skipEmptyLines: true });
        var headers = (res.meta && res.meta.fields) || [];
        var rows = res.data || [];
        if (!headers.length) { return note(SAY.noHeaders, true); }
        if (!rows.length) { return note(SAY.noRows, true); }
        var map = {
          email: guess(headers, GUESS_RE.email, true),
          firstName: guess(headers, GUESS_RE.firstName),
          lastName: guess(headers, GUESS_RE.lastName),
          external: guess(headers, GUESS_RE.external, true)
        };
        if (!map.email) { return note(SAY.noEmail, true); }
        state.file = f;
        state.headers = headers;
        state.rows = rows;
        state.map = map;
        note(f.name + " · " + pluralPart(rows.length, "row") +
             " · email from “" + map.email + "”");
        els.primary.disabled = false;
      }, function () { note(SAY.unreadable, true); });
    };
    reader.readAsText(f);
  }

  /* ═════════════════════════════════════════════════════════════════════
     6. THE REQUEST

     `sb.functions.invoke` — roster-import is a Supabase EDGE FUNCTION, not
     a Render route, so it is invoked through the SDK exactly as
     teacher/import.html invokes it (import.html:2435, :2565) and never
     with a raw fetch.
     ═════════════════════════════════════════════════════════════════════ */

  function cell(row, key) {
    if (!key) { return null; }
    var v = row[key];
    return String(v == null ? "" : v).trim() || null;
  }

  function payload(dry) {
    var m = state.map;
    var students = state.rows.map(function (r, i) {
      var s = {
        rowIndex: i + 1,
        email: cell(r, m.email),
        firstName: cell(r, m.firstName),
        lastName: cell(r, m.lastName),
        /* ⚠️ EQUAL TO `classes[0].name` BY CONSTRUCTION, not by typing —
           the backend keys its maps on this string. */
        className: state.className
      };
      if (m.external) { s.externalStudentId = cell(r, m.external); }
      return s;
    });
    return {
      dryRun: !!dry,
      source: { fileName: state.file ? state.file.name : "",
                fileHash: state.hash,
                rowCount: state.rows.length },
      /* The id is what makes this the EXISTING-class path; the name rides
         along because every student row is matched to it. */
      classes: [{ id: state.classId, name: state.className }],
      students: students
    };
  }

  /* supabase-js reports a non-2xx edge response as a FunctionsHttpError
     whose message is the fixed "…non-2xx status code" line; the real code
     is on `e.context`. teacher/import.html:2565ff does this same read. */
  function reason(e) {
    if (e && e.context && typeof e.context.json === "function") {
      return e.context.json().then(function (b) {
        return (b && b.error) || "";
      }, function () { return ""; });
    }
    return Promise.resolve((e && e.message) || "");
  }

  function friendly(code) {
    if (code === "admin_only" || code === "not_staff_of_school") {
      return SAY.adminOnly;
    }
    if (code === "class_wrong_year") { return SAY.wrongYear; }
    if (code === "class_not_found") { return SAY.notFound; }
    return SAY.generic;
  }

  /* reason-code → plain English, the rows import.html names (:2270-2283)
     trimmed to the ones this entry can produce. */
  function issueText(iss) {
    var where = iss.rowIndex != null ? "Row " + iss.rowIndex + ": " : "";
    var d = iss.detail || "";
    switch (iss.reason) {
      case "missing_email": return where + "no email address — skipped.";
      case "invalid_email": return where + "that email doesn't look valid — skipped.";
      case "duplicate_in_file": return where + "this email appears more than once — only the first was used.";
      case "duplicate_external_id": return where + "that pupil ID is on more than one row — added without the ID.";
      case "unknown_class": return where + "class “" + d + "” didn't match — skipped.";
      case "email_belongs_to_staff": return where + "that email is a staff account — left untouched.";
      case "name_updated": return where + "name updated" + (d ? " (" + d + ")" : "") + ".";
      case "auth_create_failed": return where + "we couldn't create that account — skipped.";
      default: return where + (iss.reason || "needs a look") + ".";
    }
  }

  function showIssues(list) {
    els.issues.textContent = "";
    if (!list || !list.length) { els.issues.hidden = true; return; }
    var head = el("li", null, SAY.issues + ":");
    els.issues.appendChild(head);
    list.forEach(function (iss) {
      els.issues.appendChild(el("li", null, issueText(iss)));
    });
    els.issues.hidden = false;
  }

  /* The three numbers, derived from the pipeline's own counts and from
     nothing else. See the header on the dry-run's zero. */
  function line(counts, past) {
    var c = counts || {};
    var created = c.studentsCreated || 0;
    var attached = Math.max(0, (c.studentsAttached || 0) - created);
    var already = c.studentsAlreadyAttached || 0;
    return pluralPart(created, "new pupil") +
      (past ? " created, " : " will be created, ") +
      pluralPart(attached, "pupil") +
      (past ? " already existed and " + (attached === 1 ? "was" : "were") +
              " attached, "
            : " already " + (attached === 1 ? "exists" : "exist") +
              " and will be attached, ") +
      pluralPart(already, "pupil") +
      (past ? " " + (already === 1 ? "was" : "were") +
              " already in this class and " +
              (already === 1 ? "was" : "were") + " skipped."
            : " already in this class and will be skipped.");
  }

  function send(dry) {
    var sb = client();
    if (!sb) { return note(SAY.generic, true); }
    if (!state.isAdmin) { return note(SAY.adminOnly, true); }
    state.busy = true;
    els.primary.disabled = true;
    els.cancel.disabled = true;
    note(dry ? SAY.checking : SAY.adding);

    sb.functions.invoke("roster-import", { body: payload(dry) })
      .then(function (r) {
        if (r.error) { throw r.error; }
        var d = r.data;
        if (!d || !d.ok) { throw new Error((d && d.error) || "unknown_error"); }
        return d;
      })
      .then(function (d) {
        state.busy = false;
        els.cancel.disabled = false;
        note("");
        els.summary.textContent = line(d.counts, !dry);
        showIssues(d.issues);
        if (dry) {
          state.stage = "preview";
          els.primary.textContent = SAY.confirm;
          els.primary.disabled = false;
          return;
        }
        state.stage = "done";
        els.primary.textContent = SAY.done;
        els.primary.disabled = false;
        refresh();
      })
      .catch(function (e) {
        state.busy = false;
        els.cancel.disabled = false;
        els.primary.disabled = false;
        console.error("[class-csv-upload]", e);
        reason(e).then(function (code) { note(friendly(code), true); });
      });
  }

  /* ═════════════════════════════════════════════════════════════════════
     7. AFTER THE WRITE — the page repaints itself

     `MRB_SET_WORK_DONE` is the ported pages' own "re-read this screen and
     redraw it" hook (build_teacher_port.py, MRB-335): it calls
     `MrBadmusTeacherLive.reload()` — the `reset(); base();` pair, without
     which `load()` is served out of a memoised base and repaints the same
     rows — then re-loads the screen and forces one redraw. A CSV import is
     the same shape of event as a set: a write the screen behind the sheet
     is now out of date about. Rather than a second refresh path.

     ⚠️ THE CACHE OF "MY CLASSES" GOES TOO, for the reason import.html
     records at :2565ff: this is a write that changes who is in a class, and
     `teacher-data.js` remembers the viewer's class ids in `sessionStorage`
     for two minutes. Never fatal — a cache that will not clear must not
     turn a successful import into an error.
     ═════════════════════════════════════════════════════════════════════ */

  function refresh() {
    try {
      var TD = window.MrBadmusTeacherData;
      if (TD && TD.forgetOwnClasses) { TD.forgetOwnClasses(); }
    } catch (e) { /* not fatal */ }
    try {
      if (typeof window.MRB_SET_WORK_DONE === "function") {
        window.MRB_SET_WORK_DONE({});
        return;
      }
    } catch (e) { /* fall through to the reload */ }
    window.location.reload();
  }

  /* ═════════════════════════════════════════════════════════════════════
     8. OPEN / CLOSE
     ═════════════════════════════════════════════════════════════════════ */

  function open(opts) {
    /* Defence in depth: the trigger is only injected for an admin, and
       `open()` called any other way refuses the same question again. The
       edge function refuses it a third time, server-side, and that one is
       the boundary. */
    if (!state.isAdmin) { return false; }
    var o = opts || {};
    buildShell();
    state.classId = String(o.classId || state.classId || "");
    state.className = String(o.className || classNameFor(state.classId) || "");
    if (!state.classId || !state.className) { return false; }
    state.file = null;
    state.rows = [];
    state.headers = [];
    state.map = null;
    state.hash = "";
    state.busy = false;
    els.file.value = "";
    els.cancel.disabled = false;
    els.code.textContent = state.className;
    note("");
    resetResult();
    els.scrim.hidden = false;
    els.sheet.focus({ preventScroll: true });
    return true;
  }

  function close() {
    if (!els || state.busy) { return; }
    els.scrim.hidden = true;
  }

  /* ═════════════════════════════════════════════════════════════════════
     9. BOOT
     ═════════════════════════════════════════════════════════════════════ */

  function ensurePredicate() {
    if (window.MrBadmusAdminScope && window.MrBadmusAdminScope.isAdmin) {
      return Promise.resolve(window.MrBadmusAdminScope);
    }
    /* ONE predicate for the whole estate — loaded rather than copied. See
       the header for what its own boot does on this page. */
    var map = window.__MRB_ASSET_V__ || {};
    var v = map["teacher-admin-nav.js"];
    return loadScript("/shared/teacher-admin-nav.js" + (v ? "?v=" + v : ""))
      .then(function () { return window.MrBadmusAdminScope; },
            function () { return null; });
  }

  function boot() {
    if (window.location.pathname !== PAGE) { return; }
    var id = qs().get("class");
    if (!id) { return; }
    state.classId = id;

    waitForClient().then(function (sb) {
      if (!sb) { return; }
      return sb.auth.getSession().then(function (s) {
        var user = s && s.data && s.data.session ? s.data.session.user : null;
        if (!user || !user.id) { return; }
        return ensurePredicate().then(function (mod) {
          if (!mod || !mod.isAdmin) { return; }
          return mod.isAdmin(sb, user.id).then(function (ok) {
            if (!ok) { return; }
            state.isAdmin = true;
            watch();
          });
        });
      });
    }).catch(function (e) {
      // Fail CLOSED and silently: no button is the correct outcome.
      console.error("[class-csv-upload] boot", e);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  window.MrBadmusClassCsvUpload = { open: open, close: close };
})();
