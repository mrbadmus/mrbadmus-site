/* ═══════════════════════════════════════════════════════════════════════
   class-membership.js — add, move and remove pupils (school admins).

   Surface:  window.MrBadmusClassMembership.openClass(classId)
             window.MrBadmusClassMembership.openPupil(studentId)

   Two entries:
     • teacher/class-detail.html — a "Pupils" button in Design's class action
       row (node 213), the same row "Add pupils (CSV)" joins. Admins get the
       full sheet; every other viewer of a class with pupils who have left
       gets a read-only "Left this class" button instead.
     • teacher/student-detail.html — a "Classes" button beside the pupil's
       name: their current classes, with Move and Remove for an admin.

   ⚠️ NOT THE SECURITY BOUNDARY. Every write is a call to a SECURITY DEFINER
   function (class_membership_batch, undo_membership_change — migration
   20261127120000) that re-checks the caller is a school admin of both
   classes, in the working academic year. This file never writes
   class_members; whether to show a button at all is ALSO the database's
   answer (can_manage_class_membership), so the button and the boundary
   cannot disagree the way the CSV entry's client predicate once did.

   Same shape as class-csv-upload.js and set-work.js: one overlay appended to
   <body>, outside `#mrb-teacher`, because the compiled runtime rebuilds the
   mount host on every setState; the trigger is re-injected by a
   MutationObserver after every redraw.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var CLASS_PAGE = "/teacher/class-detail.html";
  var PUPIL_PAGE = "/teacher/student-detail.html";
  var MARK = "data-mrb-added";
  var ROW_SEL = '[data-dc-tpl="213"]';
  var UNDO_MS = 20000;

  /* The class action row's own secondary-button string (see
     class-csv-upload.js `BTN`), so the row reads as one set of buttons. */
  var BTN = "height:40px;padding:0 16px;font:600 17px/1.2 var(--st-ui);" +
            "color:var(--st-ink);background:var(--st-paper);" +
            "border:1px solid var(--st-btn-border);border-radius:9px;" +
            "cursor:pointer";

  var SAY = {
    pupils: "Pupils",
    leftTrigger: "Left this class",
    classes: "Classes",
    find: "Add a pupil",
    findHint: "Name or admission number",
    noMatch: "No pupil found.",
    notOnYet: "Not on MrBadmus yet? Add by email",
    first: "First name",
    last: "Last name",
    email: "School email",
    addByEmail: "Add pupil",
    inClass: "In this class",
    add: "Add",
    move: "Move",
    remove: "Remove",
    moveTo: "Move to",
    cancel: "Cancel",
    close: "Close",
    undo: "Undo",
    all: "Select all",
    empty: "No pupils yet.",
    left: "Left this class",
    leftOn: "Left the class on ",
    movedTo: "Moved to ",
    on: " on ",
    working: "Saving…",
    sameYear: "Same year",
    otherYears: "Other years",
    notAdmin: "Only a school admin can change classes.",
    generic: "That didn't go through. Try again.",
    expired: "Too late to undo.",
    badEmail: "Enter a school email address.",
    current: "Current classes",
    noClasses: "Not in any class."
  };

  var state = {
    mode: "",            // class | pupil
    classId: "",
    className: "",
    studentId: "",
    canManage: false,
    roster: [],
    past: [],
    picked: {},
    targets: null,
    busy: false,
    lastAudit: null,
    undoTimer: null,
    view: "list"         // list | move | confirm | email
  };
  var els = null;

  /* ── helpers ────────────────────────────────────────────────────────── */

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) { n.className = cls; }
    if (text != null) { n.textContent = text; }
    return n;
  }
  function btn(text, cls, onClick) {
    var b = el("button", "cm-btn" + (cls ? " " + cls : ""), text);
    b.type = "button";
    if (onClick) { b.addEventListener("click", onClick); }
    return b;
  }
  function qs() { return new URLSearchParams(window.location.search); }
  function client() {
    var g = window.MrBadmusTeacherGuard;
    return (g && g.getClient) ? g.getClient() : null;
  }
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
  function fullName(f, l) {
    return (String(f || "") + " " + String(l || "")).trim() || "Pupil";
  }
  function shortDate(iso) {
    var d = iso ? new Date(iso) : null;
    if (!d || isNaN(d)) { return ""; }
    return d.toLocaleDateString("en-GB", { day: "numeric", month: "short",
                                           timeZone: "Europe/London" });
  }
  function rpc(name, args) {
    var sb = client();
    if (!sb) { return Promise.reject(new Error("no_client")); }
    return sb.rpc(name, args).then(function (r) {
      if (r.error) { throw r.error; }
      return r.data;
    });
  }
  function friendly(e) {
    var m = String((e && (e.message || e.code)) || "");
    if (/not_admin/.test(m)) { return SAY.notAdmin; }
    if (/undo_expired/.test(m)) { return SAY.expired; }
    return SAY.generic;
  }
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

  /* ── the sheet ──────────────────────────────────────────────────────── */

  var CSS = [
    ".cm-scrim{position:fixed;inset:0;z-index:9000;display:flex;",
    "align-items:flex-end;justify-content:center;background:rgba(20,18,16,.44)}",
    "@media(min-width:600px){.cm-scrim{align-items:center}}",
    ".cm-sheet{width:min(560px,calc(100vw - 24px));max-height:88vh;overflow:auto;",
    "box-sizing:border-box;margin:12px;padding:18px;border-radius:14px;",
    "background:var(--st-paper,#fff);border:1px solid var(--st-rule-soft,#e6e1d9);",
    "box-shadow:0 18px 48px rgba(20,18,16,.22);color:var(--st-ink,#1a1714);",
    "font:400 15.5px/1.45 var(--st-ui,system-ui)}",
    ".cm-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap}",
    ".cm-title{font:600 20px/1.25 var(--st-ui,system-ui);margin:0}",
    ".cm-code{font:500 13px/1.2 var(--st-mono,ui-monospace);letter-spacing:.04em;",
    "color:var(--st-caption,#8a8178)}",
    ".cm-sec{margin-top:16px}",
    ".cm-label{display:block;font:600 13px/1.3 var(--st-ui,system-ui);",
    "color:var(--st-muted,#6b635a);margin:0 0 6px}",
    ".cm-input{width:100%;box-sizing:border-box;height:42px;padding:0 12px;",
    "font:400 16px/1.2 var(--st-ui,system-ui);color:var(--st-ink,#1a1714);",
    "background:var(--st-paper,#fff);border:1px solid var(--st-btn-border,#d9d2c8);border-radius:10px}",
    ".cm-list{list-style:none;margin:0;padding:0}",
    ".cm-row{display:flex;align-items:center;gap:10px;min-height:48px;padding:6px 0;",
    "border-bottom:1px solid var(--st-rule-soft,#e6e1d9)}",
    ".cm-row:last-child{border-bottom:0}",
    ".cm-row input[type=checkbox]{width:20px;height:20px;flex:none;margin:0;accent-color:var(--st-ink,#1a1714)}",
    ".cm-who{flex:1 1 auto;min-width:0}",
    ".cm-name{font-weight:600;overflow-wrap:anywhere}",
    ".cm-sub{font-size:13.5px;color:var(--st-muted,#6b635a);overflow-wrap:anywhere}",
    ".cm-acts{display:flex;gap:6px;flex:none}",
    ".cm-btn{height:38px;padding:0 12px;box-sizing:border-box;font:600 15px/1.2 var(--st-ui,system-ui);",
    "border-radius:9px;cursor:pointer;border:1px solid var(--st-btn-border,#d9d2c8);",
    "background:var(--st-paper,#fff);color:var(--st-ink,#1a1714)}",
    ".cm-btn[disabled]{opacity:.45;cursor:default}",
    ".cm-primary{background:var(--st-ink,#1a1714);border-color:var(--st-ink,#1a1714);color:var(--st-paper,#fff)}",
    ".cm-danger{color:var(--danger,#c0392b)}",
    ".cm-primary.cm-danger{background:var(--danger,#c0392b);border-color:var(--danger,#c0392b);color:#fff}",
    ".cm-link{background:none;border:0;padding:6px 0;font:600 14.5px/1.3 var(--st-ui,system-ui);",
    "color:var(--st-ink,#1a1714);text-decoration:underline;cursor:pointer}",
    ".cm-bar{position:sticky;bottom:-18px;display:flex;gap:8px;align-items:center;flex-wrap:wrap;",
    "margin:12px -18px -18px;padding:12px 18px;background:var(--st-paper,#fff);",
    "border-top:1px solid var(--st-rule-soft,#e6e1d9)}",
    ".cm-bar .cm-count{flex:1 1 auto;font-weight:600}",
    ".cm-foot{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}",
    ".cm-foot .cm-btn{flex:1 1 auto;height:42px;min-width:120px}",
    ".cm-msg{margin:10px 0 0;font-size:14.5px}",
    ".cm-warn{color:var(--danger,#c0392b)}",
    ".cm-group{font:600 12.5px/1.2 var(--st-mono,ui-monospace);letter-spacing:.08em;",
    "text-transform:uppercase;color:var(--st-caption,#8a8178);margin:14px 0 4px}",
    ".cm-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}",
    "@media(max-width:420px){.cm-grid{grid-template-columns:1fr}}",
    ".cm-toast{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:9100;",
    "display:flex;gap:14px;align-items:center;width:max-content;max-width:calc(100vw - 32px);box-sizing:border-box;",
    "padding:10px 12px 10px 16px;border-radius:12px;background:var(--st-ink,#1a1714);",
    "color:var(--st-paper,#fff);font:500 15px/1.35 var(--st-ui,system-ui);",
    "box-shadow:0 10px 30px rgba(20,18,16,.3)}",
    ".cm-toast span{flex:1 1 auto;min-width:0}",
    /* On a phone the sheet is a bottom sheet with its own action bar: the
       toast sits above it rather than on top of it. */
    "@media(max-width:599px){.cm-toast{bottom:96px}}",
    ".cm-toast .cm-btn{background:transparent;color:inherit;border-color:currentColor;height:34px}"
  ].join("");

  function shell() {
    if (els) { return els; }
    var style = el("style");
    style.textContent = CSS;
    document.head.appendChild(style);
    var scrim = el("div", "cm-scrim");
    scrim.hidden = true;
    var sheet = el("div", "cm-sheet");
    sheet.setAttribute("role", "dialog");
    sheet.setAttribute("aria-modal", "true");
    sheet.tabIndex = -1;
    scrim.appendChild(sheet);
    document.body.appendChild(scrim);
    scrim.addEventListener("click", function (e) {
      if (e.target === scrim && !state.busy) { close(); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !scrim.hidden && !state.busy) {
        if (state.view !== "list") { state.view = "list"; draw(); } else { close(); }
      }
    });
    els = { scrim: scrim, sheet: sheet, toast: null };
    return els;
  }

  function close() {
    if (els) { els.scrim.hidden = true; }
  }

  function head(title, code) {
    var h = el("div", "cm-head");
    var t = el("h2", "cm-title", title);
    t.id = "cm-title";
    h.appendChild(t);
    if (code) { h.appendChild(el("div", "cm-code", code)); }
    els.sheet.setAttribute("aria-labelledby", "cm-title");
    return h;
  }

  function msg(text, warn) {
    var p = els.sheet.querySelector(".cm-msg");
    if (!p) { return; }
    p.textContent = text || "";
    p.classList.toggle("cm-warn", !!warn);
  }

  /* ── data ───────────────────────────────────────────────────────────── */

  function loadRoster() {
    var sb = client();
    return sb.from("class_members")
      .select("student_id, joined_at, student:student_id ( first_name, last_name, external_student_id )")
      .eq("class_id", state.classId)
      .is("left_at", null)
      .is("deleted_at", null)
      .then(function (r) {
        if (r.error) { throw r.error; }
        state.roster = (r.data || []).map(function (m) {
          var s = m.student || {};
          return { id: m.student_id, name: fullName(s.first_name, s.last_name),
                   last: s.last_name || "", adm: s.external_student_id || "",
                   joined: m.joined_at };
        }).sort(function (a, b) {
          return (a.last || a.name).localeCompare(b.last || b.name);
        });
      });
  }
  function loadPast() {
    return rpc("class_past_members", { p_class_id: state.classId }).then(function (rows) {
      state.past = (rows || []).map(function (r) {
        return {
          id: r.student_id, name: fullName(r.first_name, r.last_name),
          line: r.moved_to_name
            ? SAY.movedTo + r.moved_to_name + SAY.on + shortDate(r.left_at)
            : SAY.leftOn + shortDate(r.left_at),
          work: r.done ? (r.done + (r.done === 1 ? " piece of work" : " pieces of work") +
                          (r.avg_pct != null ? " · " + r.avg_pct + "%" : "")) : ""
        };
      });
    }, function () { state.past = []; });
  }
  function loadTargets() {
    if (state.targets) { return Promise.resolve(state.targets); }
    return rpc("membership_targets", { p_class_id: state.classId }).then(function (rows) {
      state.targets = rows || [];
      return state.targets;
    });
  }

  /* ── writes (all through the database functions) ───────────────────── */

  function apply(ops, done) {
    state.busy = true;
    msg(SAY.working);
    return rpc("class_membership_batch", { p_ops: ops, p_source: state.mode === "pupil" ? "pupil_page" : "admin" })
      .then(function (res) {
        state.busy = false;
        var ids = (res && res.audit_ids) || [];
        afterWrite(done, ids);
      }, function (e) {
        state.busy = false;
        console.error("[class-membership]", e);
        msg(friendly(e), true);
      });
  }

  function afterWrite(text, auditIds) {
    state.picked = {};
    state.view = "list";
    reloadSheet(true).then(function () { toast(text, auditIds); });
  }

  /* Re-read the sheet, then repaint the page behind it. On the pupil page the
     address names ONE class; once the pupil has left it, the page must be
     re-pointed at a class they are still in before it re-reads, or it asks
     for a pupil who is no longer on that roster. With no class left there is
     nothing for staff to show, so the page is left as it is. */
  function reloadSheet() {
    if (state.mode !== "pupil") {
      refreshPage();
      return Promise.all([loadRoster(), loadPast()]).then(draw);
    }
    return openPupil(state.studentId, true).then(function (rows) {
      rows = rows || [];
      var q = qs();
      var here = q.get("class");
      var still = rows.some(function (r) { return String(r.class_id) === String(here); });
      if (!still && rows.length) {
        q.set("class", rows[0].class_id);
        try { window.history.replaceState(null, "", window.location.pathname + "?" + q.toString()); }
        catch (e) { /* not fatal */ }
      }
      if (still || rows.length) { refreshPage(); }
    });
  }

  function toast(text, auditIds) {
    shell();
    if (els.toast) { els.toast.remove(); els.toast = null; }
    if (state.undoTimer) { clearTimeout(state.undoTimer); }
    var t = el("div", "cm-toast");
    t.setAttribute("role", "status");
    t.appendChild(el("span", null, text));
    if (auditIds && auditIds.length) {
      t.appendChild(btn(SAY.undo, "", function () {
        t.remove(); els.toast = null;
        rpc("undo_membership_change", { p_audit_ids: auditIds }).then(function () {
          reloadSheet();
        }, function (e) { toast(friendly(e), null); });
      }));
    }
    document.body.appendChild(t);
    els.toast = t;
    state.undoTimer = setTimeout(function () {
      if (els.toast === t) { t.remove(); els.toast = null; }
    }, UNDO_MS);
  }

  /* Repaint the page behind the sheet (same hook class-csv-upload uses). */
  function refreshPage() {
    try {
      var TD = window.MrBadmusTeacherData;
      if (TD && TD.forgetOwnClasses) { TD.forgetOwnClasses(); }
    } catch (e) { /* not fatal */ }
    try {
      if (typeof window.MRB_SET_WORK_DONE === "function") { window.MRB_SET_WORK_DONE({}); }
    } catch (e) { /* not fatal */ }
  }

  /* ── the class sheet ────────────────────────────────────────────────── */

  function pickedIds() {
    return Object.keys(state.picked).filter(function (k) { return state.picked[k]; });
  }
  function nameOf(id) {
    for (var i = 0; i < state.roster.length; i++) {
      if (state.roster[i].id === id) { return state.roster[i].name; }
    }
    return "Pupil";
  }
  function who(ids) {
    return ids.length === 1 ? nameOf(ids[0]) : ids.length + " pupils";
  }

  function draw() {
    shell();
    var s = els.sheet;
    s.textContent = "";
    if (state.view === "move") { return drawMove(); }
    if (state.view === "confirm") { return drawConfirm(); }
    if (state.view === "email") { return drawEmail(); }

    s.appendChild(head(state.canManage ? SAY.pupils : SAY.left, state.className));

    if (state.canManage) {
      var find = el("div", "cm-sec");
      var lab = el("label", "cm-label", SAY.find);
      lab.htmlFor = "cm-find";
      var inp = el("input", "cm-input");
      inp.id = "cm-find";
      inp.type = "search";
      inp.autocomplete = "off";
      inp.placeholder = SAY.findHint;
      var res = el("ul", "cm-list");
      find.appendChild(lab);
      find.appendChild(inp);
      find.appendChild(res);
      find.appendChild(btn(SAY.notOnYet, "cm-link", function () {
        state.view = "email"; draw();
      }));
      s.appendChild(find);
      var timer = null, seq = 0;
      inp.addEventListener("input", function () {
        clearTimeout(timer);
        var q = inp.value.trim();
        if (q.length < 2) { res.textContent = ""; return; }
        timer = setTimeout(function () {
          var mine = ++seq;
          rpc("membership_pupil_search", { p_class_id: state.classId, p_query: q })
            .then(function (rows) {
              if (mine !== seq) { return; }
              drawResults(res, rows || []);
            }, function (e) { if (mine === seq) { msg(friendly(e), true); } });
        }, 180);
      });

      var rs = el("div", "cm-sec");
      var rh = el("div", "cm-head");
      rh.appendChild(el("span", "cm-label", state.roster.length + (state.roster.length === 1 ? " pupil" : " pupils")));
      if (state.roster.length > 1) {
        var allLab = el("label", "cm-sub");
        var all = el("input");
        all.type = "checkbox";
        all.checked = state.roster.length > 0 && pickedIds().length === state.roster.length;
        all.addEventListener("change", function () {
          state.roster.forEach(function (p) { state.picked[p.id] = all.checked; });
          draw();
        });
        allLab.appendChild(all);
        allLab.appendChild(document.createTextNode(" " + SAY.all));
        rh.appendChild(allLab);
      }
      rs.appendChild(rh);
      var list = el("ul", "cm-list");
      if (!state.roster.length) { rs.appendChild(el("p", "cm-sub", SAY.empty)); }
      state.roster.forEach(function (p) {
        var li = el("li", "cm-row");
        var cb = el("input");
        cb.type = "checkbox";
        cb.checked = !!state.picked[p.id];
        cb.setAttribute("aria-label", p.name);
        cb.addEventListener("change", function () { state.picked[p.id] = cb.checked; draw(); });
        var w = el("div", "cm-who");
        w.appendChild(el("div", "cm-name", p.name));
        if (p.adm) { w.appendChild(el("div", "cm-sub", p.adm)); }
        var acts = el("div", "cm-acts");
        acts.appendChild(btn(SAY.move, "", function () { startMove([p.id]); }));
        acts.appendChild(btn(SAY.remove, "cm-danger", function () { startRemove([p.id]); }));
        li.appendChild(cb); li.appendChild(w); li.appendChild(acts);
        list.appendChild(li);
      });
      rs.appendChild(list);
      s.appendChild(rs);
    }

    if (state.past.length) {
      var ps = el("div", "cm-sec");
      if (state.canManage) { ps.appendChild(el("span", "cm-label", SAY.left)); }
      var pl = el("ul", "cm-list");
      state.past.forEach(function (p) {
        var li = el("li", "cm-row");
        var w = el("div", "cm-who");
        w.appendChild(el("div", "cm-name", p.name));
        w.appendChild(el("div", "cm-sub", p.line + (p.work ? " · " + p.work : "")));
        li.appendChild(w);
        pl.appendChild(li);
      });
      ps.appendChild(pl);
      s.appendChild(ps);
    }

    s.appendChild(el("p", "cm-msg"));
    var ids = pickedIds();
    if (state.canManage && ids.length) {
      var bar = el("div", "cm-bar");
      bar.appendChild(el("span", "cm-count", ids.length + " selected"));
      bar.appendChild(btn(SAY.move, "", function () { startMove(ids); }));
      bar.appendChild(btn(SAY.remove, "cm-danger", function () { startRemove(ids); }));
      s.appendChild(bar);
    } else {
      var foot = el("div", "cm-foot");
      foot.appendChild(btn(SAY.close, "", close));
      s.appendChild(foot);
    }
  }

  function drawResults(ul, rows) {
    ul.textContent = "";
    if (!rows.length) {
      var li0 = el("li", "cm-row");
      li0.appendChild(el("span", "cm-sub", SAY.noMatch));
      ul.appendChild(li0);
      return;
    }
    rows.forEach(function (r) {
      var li = el("li", "cm-row");
      var w = el("div", "cm-who");
      var name = fullName(r.first_name, r.last_name);
      w.appendChild(el("div", "cm-name", name));
      var sub = [r.admission_no].concat((r.classes || []).map(function (c) { return c.name; }))
        .filter(Boolean).join(" · ");
      if (sub) { w.appendChild(el("div", "cm-sub", sub)); }
      li.appendChild(w);
      if (r.in_class) {
        li.appendChild(el("span", "cm-sub", SAY.inClass));
      } else {
        li.appendChild(btn(SAY.add, "cm-primary", function () {
          apply([{ op: "add", class_id: state.classId, student_id: r.student_id }],
                name + " added");
        }));
      }
      ul.appendChild(li);
    });
  }

  var pending = null;   // { kind: move|remove, ids: [], to: {id,name} }

  function startMove(ids) {
    pending = { kind: "move", ids: ids, to: null };
    state.view = "move";
    loadTargets().then(draw, function (e) { state.view = "list"; draw(); msg(friendly(e), true); });
  }
  function startRemove(ids) {
    pending = { kind: "remove", ids: ids };
    state.view = "confirm";
    draw();
  }

  function drawMove() {
    var s = els.sheet;
    s.appendChild(head(SAY.moveTo + "…", who(pending.ids)));
    var same = state.targets.filter(function (t) { return t.same_year; });
    var other = state.targets.filter(function (t) { return !t.same_year; });
    function group(label, rows) {
      if (!rows.length) { return; }
      if (same.length && other.length) { s.appendChild(el("div", "cm-group", label)); }
      var g = el("div", "cm-grid");
      rows.forEach(function (t) {
        var b = btn(t.name, "", function () {
          pending.to = { id: t.class_id, name: t.name };
          state.view = "confirm"; draw();
        });
        b.style.height = "44px";
        b.style.justifyContent = "flex-start";
        b.style.textAlign = "left";
        g.appendChild(b);
      });
      s.appendChild(g);
    }
    group(SAY.sameYear, same);
    group(SAY.otherYears, other);
    var foot = el("div", "cm-foot");
    foot.appendChild(btn(SAY.cancel, "", function () { state.view = "list"; draw(); }));
    s.appendChild(foot);
  }

  function drawConfirm() {
    var s = els.sheet;
    var ids = pending.ids;
    var fromName = state.className;
    var q = pending.kind === "move"
      ? "Move " + who(ids) + " to " + pending.to.name + "?"
      : "Remove " + who(ids) + " from " + fromName + "?";
    s.appendChild(head(q));
    s.appendChild(el("p", "cm-msg"));
    var foot = el("div", "cm-foot");
    foot.appendChild(btn(SAY.cancel, "", function () { state.view = "list"; draw(); }));
    var go = btn(pending.kind === "move" ? SAY.move : SAY.remove,
                 pending.kind === "move" ? "cm-primary" : "cm-primary cm-danger", function () {
      go.disabled = true;
      var fromId = pending.fromId || state.classId;
      var ops = ids.map(function (id) {
        return pending.kind === "move"
          ? { op: "move", student_id: id, class_id: fromId, to_class_id: pending.to.id }
          : { op: "remove", student_id: id, class_id: fromId };
      });
      var done = pending.kind === "move"
        ? who(ids) + " moved to " + pending.to.name
        : who(ids) + " removed from " + fromName;
      apply(ops, done).then(function () { go.disabled = false; });
    });
    foot.appendChild(go);
    s.appendChild(foot);
    go.focus();
  }

  function drawEmail() {
    var s = els.sheet;
    s.appendChild(head(SAY.find, state.className));
    var g = el("div", "cm-sec cm-grid");
    function field(label, id, type) {
      var w = el("div");
      var l = el("label", "cm-label", label); l.htmlFor = id;
      var i = el("input", "cm-input"); i.id = id; i.type = type || "text";
      w.appendChild(l); w.appendChild(i); g.appendChild(w);
      return i;
    }
    var f = field(SAY.first, "cm-first");
    var l = field(SAY.last, "cm-last");
    s.appendChild(g);
    var ew = el("div", "cm-sec");
    var el2 = el("label", "cm-label", SAY.email); el2.htmlFor = "cm-email";
    var e = el("input", "cm-input"); e.id = "cm-email"; e.type = "email"; e.autocomplete = "off";
    ew.appendChild(el2); ew.appendChild(e);
    s.appendChild(ew);
    s.appendChild(el("p", "cm-msg"));
    var foot = el("div", "cm-foot");
    foot.appendChild(btn(SAY.cancel, "", function () { state.view = "list"; draw(); }));
    var go = btn(SAY.addByEmail, "cm-primary", function () {
      var email = e.value.trim().toLowerCase();
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { return msg(SAY.badEmail, true); }
      go.disabled = true;
      state.busy = true;
      msg(SAY.working);
      var sb = client();
      sb.functions.invoke("roster-import", { body: {
        dryRun: false,
        source: { fileName: "add-one", rowCount: 1 },
        classes: [{ id: state.classId, name: state.className }],
        students: [{ rowIndex: 1, email: email, firstName: f.value.trim() || null,
                     lastName: l.value.trim() || null, className: state.className }]
      } }).then(function (r) {
        state.busy = false;
        go.disabled = false;
        var d = r && r.data;
        if (r.error || !d || !d.ok) { throw (r.error || new Error((d && d.error) || "failed")); }
        var iss = (d.issues || [])[0];
        if (iss && iss.reason === "email_belongs_to_staff") {
          return msg("That email is a staff account.", true);
        }
        if (iss && iss.reason === "pupil_in_other_school") {
          return msg("That pupil belongs to another school.", true);
        }
        if (d.plan && d.plan.already && !(d.plan.add || []).length) {
          return msg(SAY.inClass + ".", false);
        }
        var added = d.plan && ((d.plan.add || [])[0] || (d.plan.moveIn || [])[0]);
        var nm = (added && added.name && added.name !== email) ? added.name
          : fullName(f.value.trim(), l.value.trim());
        afterWrite((nm === "Pupil" ? email : nm) + " added",
                   (d.plan && d.plan.auditIds) || []);
      }).catch(function (err) {
        state.busy = false;
        go.disabled = false;
        console.error("[class-membership] add by email", err);
        msg(SAY.generic, true);
      });
    });
    foot.appendChild(go);
    s.appendChild(foot);
    f.focus();
  }

  function openClass(classId) {
    shell();
    state.mode = "class";
    state.classId = String(classId || state.classId || "");
    state.className = classNameFor(state.classId) || state.className;
    state.view = "list";
    state.picked = {};
    state.targets = null;
    return Promise.all([state.canManage ? loadRoster() : Promise.resolve(), loadPast()])
      .then(function () {
        draw();
        els.scrim.hidden = false;
        els.sheet.focus({ preventScroll: true });
      }, function (e) { console.error("[class-membership]", e); });
  }

  /* ── the pupil sheet (student-detail) ──────────────────────────────── */

  function openPupil(studentId, keepOpen) {
    shell();
    state.mode = "pupil";
    state.studentId = String(studentId || state.studentId || "");
    return rpc("pupil_current_classes", { p_student_id: state.studentId }).then(function (rows) {
      rows = rows || [];
      var canManage = rows.some(function (r) { return r.can_manage; });
      var s = els.sheet;
      s.textContent = "";
      s.appendChild(head(SAY.current, state.pupilName || ""));
      var list = el("ul", "cm-list cm-sec");
      if (!rows.length) { list.appendChild(el("li", "cm-sub", SAY.noClasses)); }
      rows.forEach(function (r) {
        var li = el("li", "cm-row");
        var w = el("div", "cm-who");
        w.appendChild(el("div", "cm-name", r.name));
        w.appendChild(el("div", "cm-sub", "Joined " + shortDate(r.joined_at)));
        li.appendChild(w);
        if (canManage) {
          var acts = el("div", "cm-acts");
          acts.appendChild(btn(SAY.move, "", function () {
            state.classId = r.class_id; state.className = r.name; state.targets = null;
            state.roster = [{ id: state.studentId, name: state.pupilName || "Pupil" }];
            pending = { kind: "move", ids: [state.studentId], to: null, fromId: r.class_id };
            state.view = "move";
            loadTargets().then(function () { s.textContent = ""; drawMove(); });
          }));
          acts.appendChild(btn(SAY.remove, "cm-danger", function () {
            state.classId = r.class_id; state.className = r.name;
            state.roster = [{ id: state.studentId, name: state.pupilName || "Pupil" }];
            pending = { kind: "remove", ids: [state.studentId], fromId: r.class_id };
            s.textContent = ""; drawConfirm();
          }));
          li.appendChild(acts);
        }
        list.appendChild(li);
      });
      s.appendChild(list);
      s.appendChild(el("p", "cm-msg"));
      var foot = el("div", "cm-foot");
      foot.appendChild(btn(SAY.close, "", close));
      s.appendChild(foot);
      if (!keepOpen || els.scrim.hidden) {
        els.scrim.hidden = false;
        els.sheet.focus({ preventScroll: true });
      }
      return rows;
    }, function (e) { console.error("[class-membership]", e); return []; });
  }

  /* In the pupil sheet, Escape from move/confirm goes back to the list. */
  var baseDraw = draw;
  draw = function () {
    if (state.mode === "pupil" && state.view === "list") { return openPupil(state.studentId, true); }
    return baseDraw();
  };

  /* ── triggers ───────────────────────────────────────────────────────── */

  function makeTrigger(label, kind, onClick) {
    var b = el("button", null, label);
    b.type = "button";
    b.setAttribute(MARK, kind);
    b.style.cssText = BTN;
    b.addEventListener("click", onClick);
    return b;
  }

  function injectClass(label) {
    var row = document.querySelector(ROW_SEL);
    if (!row || row.querySelector("[" + MARK + '="members-open"]')) { return; }
    row.appendChild(makeTrigger(label, "members-open", function () { openClass(state.classId); }));
  }

  function injectPupil() {
    var host = document.getElementById("mrb-teacher");
    var h = host && host.querySelector("h1");
    if (!h || (h.parentNode && h.parentNode.querySelector("[" + MARK + '="pupil-classes"]'))) { return; }
    state.pupilName = (h.textContent || "").trim();
    var b = makeTrigger(SAY.classes, "pupil-classes", function () { openPupil(state.studentId); });
    b.style.marginTop = "8px";
    b.style.height = "36px";
    b.style.fontSize = "15px";
    h.insertAdjacentElement("afterend", b);
  }

  function watch(fn) {
    fn();
    var mount = document.getElementById("mrb-teacher") || document.body;
    if (!window.MutationObserver) { return; }
    var queued = false;
    new MutationObserver(function () {
      if (queued) { return; }
      queued = true;
      (window.requestAnimationFrame || window.setTimeout)(function () { queued = false; fn(); }, 0);
    }).observe(mount, { childList: true, subtree: true });
  }

  function boot() {
    var path = window.location.pathname;
    if (path !== CLASS_PAGE && path !== PUPIL_PAGE) { return; }
    var q = qs();
    waitForClient().then(function (sb) {
      if (!sb) { return; }
      return sb.auth.getSession().then(function (s) {
        if (!(s && s.data && s.data.session)) { return; }
        if (path === CLASS_PAGE) {
          state.classId = q.get("class") || "";
          if (!state.classId) { return; }
          return Promise.all([
            rpc("can_manage_class_membership", { p_class_id: state.classId }).catch(function () { return false; }),
            rpc("class_past_members", { p_class_id: state.classId }).catch(function () { return []; })
          ]).then(function (r) {
            state.canManage = r[0] === true;
            var anyPast = (r[1] || []).length > 0;
            if (state.canManage) { watch(function () { injectClass(SAY.pupils); }); }
            else if (anyPast) { watch(function () { injectClass(SAY.leftTrigger); }); }
          });
        }
        state.studentId = q.get("student") || "";
        if (!state.studentId) { return; }
        return rpc("pupil_current_classes", { p_student_id: state.studentId }).then(function (rows) {
          if ((rows || []).length) { watch(injectPupil); }
        }, function () { /* no button */ });
      });
    }).catch(function (e) { console.error("[class-membership] boot", e); });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  window.MrBadmusClassMembership = { openClass: openClass, openPupil: openPupil, close: close };
})();
