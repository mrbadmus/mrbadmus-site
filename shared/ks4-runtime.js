/* ============================================================================
   shared/ks4-runtime.js — Claude Design's KS4 pilot templates and logic,
   without React. Generated ONCE by hand (this is engine code, not a compiled
   artifact — build_ks4.py compiles the 14 lessons' and 11 blocks' TEMPLATES
   and LOGIC through this runtime, but this file itself is not derived from
   any single .dc.html).

   Derived from shared/student-runtime.js (pilot-build-contract.md §1). Same
   base class shape (`DCLogic`: props, state, setState, forceUpdate, the three
   lifecycle hooks, renderVals), same three template constructs (`sc-if`,
   `sc-for`, `{{ }}`), same onClick/style-hover/ref handling — extended here
   for what the KS3 student runtime never needed:

     1. CHILD COMPONENTS. A lesson's template can `<dc-import name="Ks4Choice"
        …>` any of the 11 shared blocks, and a block can itself import another
        block (Ks4Ladder imports Ks4Chain and Ks4Write). Each import mounts
        its OWN `DCLogic` instance, with its own `state` that survives the
        parent's re-renders, keyed by its position in the compiled template
        (see `patchNode`'s `t === 'child'` branch) — not by anything the
        parent computes, so two imports of the same block at two different
        template positions are two independent instances.

     2. PATCH-IN-PLACE RENDERING, not a full rebuild. `shared/student-
        runtime.js`'s `draw()` does `host.textContent = ''` and rebuilds from
        scratch on every state change — correct for KS3, where a redraw is a
        deliberate, infrequent user action. KS4's electron-sea and heating-
        curve benches redraw on a 90ms wall-clock tick while animating
        (`ks4-chemistry-5.2.1.5-metallic-bonding.dc.html`'s `this.tick =
        setInterval(…, 90)`), and CLAUDE.md already records what a full
        rebuild under a fast tick does: the set-work sheet's scroll-jump
        defect. So this runtime keeps ONE PERSISTENT DOM element per template
        POSITION across renders and only touches what changed — an attribute
        whose resolved value differs, a text node whose string differs, a
        child list whose length or membership differs. Focus, scroll and
        typed-but-not-yet-submitted input text are consequences of this, not
        separate machinery: nothing that did not change is ever touched.

     3. THE FIGURE MARKER. React appears in exactly four places in the pilot
        (KS4.fig in ks4-lib.js, the `figure` prop on Ks4Choice/Ks4Write, and
        Ks4Ladder's own `svg()` method) — all four call
        `React.createElement('div', {role:'img','aria-label',
        style:{maxWidth}, dangerouslySetInnerHTML:{__html}})` and are
        rewritten by ks4_rulings.py (R2) to return a plain marker object
        instead: `{__mrbFig:true, __html, alt, max}`. This runtime is the
        other half of that rewrite — see `isFigMarker`/`buildFig` below: a
        `{{ }}` interpolation that resolves to a marker object is mounted as
        the div React would have produced, not stringified as "[object
        Object]".

   ── What this file is, in one sentence ──────────────────────────────────
   A ~700-line replacement for `support.js` (1911 lines) + React + ReactDOM +
   Babel, none of which ship. Design's compiled templates and her logic
   classes ship verbatim (extracted by build_ks4.py, corrected only through
   ks4_rulings.py's exact-match, fails-loud rulings); this is the renderer
   underneath both.
   ============================================================================ */
(function () {
  "use strict";

  var SVG_NS = "http://www.w3.org/2000/svg";

  function MrbRef() { return { current: null }; }

  /* ── the base class every Design `Component` extends as `DCLogic` ──────
     Exposed as `window.DCLogic` — Design's own lessons and blocks write
     `class Component extends DCLogic { … }`, so the global name is fixed by
     her delivery, not chosen by us. */
  function DCLogic(props) {
    this.props = props || {};
    this.state = {};
    this.__host = null;
  }
  DCLogic.prototype.setState = function (update, cb) {
    var next = (typeof update === "function")
      ? update(this.state, this.props) : update;
    for (var k in next) {
      if (Object.prototype.hasOwnProperty.call(next, k)) {
        this.state[k] = next[k];
      }
    }
    if (this.__host) { this.__host.schedule(cb); }
    else if (cb) { cb(); }
  };
  DCLogic.prototype.forceUpdate = function (cb) {
    if (this.__host) { this.__host.schedule(cb); } else if (cb) { cb(); }
  };
  DCLogic.prototype.componentDidMount = function () {};
  DCLogic.prototype.componentDidUpdate = function () {};
  DCLogic.prototype.componentWillUnmount = function () {};
  DCLogic.prototype.renderVals = function () { return {}; };

  /* ── expression lookup ──────────────────────────────────────────────────
     Every `{{ }}` across the 14 lessons + 11 blocks was checked (engine-
     report.md has the count): a plain dotted property path, in every case
     but one shape — `{{ true }}`, used four times on <video>/<track> boolean
     attributes in Ks4Video and once as a literal prop value
     (`scored="{{ true }}"` on Ks4Ladder's own Ks4Chain import). `support.js`'s
     real `resolve()` (§support.js `resolve`/`resolvePath`) is a small
     expression language — equality, `!`, quoted strings, bracket indexing —
     and none of the rest of it is exercised anywhere in the pilot (checked by
     grepping every `{{ }}` for an operator character: zero hits outside
     `hint-placeholder-val`, which is stripped at compile time and never
     reaches this runtime at all). So this stays a lookup with ONE deliberate
     widening over the KS3 runtime's `lookup()`: the three JS literals. Adding
     the rest of support.js's expression grammar for content nothing in this
     pilot uses would be a bigger runtime surface for no lesson it renders. */
  function lookup(expr, scope, miss) {
    if (expr === "true") { return true; }
    if (expr === "false") { return false; }
    if (expr === "null") { return null; }
    var parts = expr.split("."), cur = scope, i;
    for (i = 0; i < parts.length; i++) {
      if (cur === null || cur === undefined) {
        if (miss) { miss.push(expr); }
        return undefined;
      }
      cur = cur[parts[i]];
    }
    if (cur === undefined && miss) { miss.push(expr); }
    return cur;
  }

  function resolve(v, scope, miss) {
    if (v === null || v === undefined) { return v; }
    if (typeof v === "string") { return v; }
    if (v.parts) {
      if (v.parts.length === 1 && typeof v.parts[0] !== "string") {
        return lookup(v.parts[0].e, scope, miss);
      }
      var out = "";
      for (var i = 0; i < v.parts.length; i++) {
        var p = v.parts[i];
        if (typeof p === "string") { out += p; }
        else {
          var got = lookup(p.e, scope, miss);
          out += (got === null || got === undefined) ? "" : got;
        }
      }
      return out;
    }
    return v;
  }

  function camel(s) {
    return s.replace(/-([a-z0-9])/g, function (_, c) { return c.toUpperCase(); });
  }

  function isFigMarker(v) {
    return v !== null && typeof v === "object" && v.__mrbFig === true;
  }

  function shallow(o) {
    var out = {};
    for (var k in o) {
      if (Object.prototype.hasOwnProperty.call(o, k)) { out[k] = o[k]; }
    }
    return out;
  }

  /* ── boolean DOM PROPERTIES that diverge from their attribute after the
     user (or a previous render) touches them ─────────────────────────────
     `setAttribute('value', …)` on an <input> only sets the DEFAULT value —
     once the live value has been set once (by the user typing, or by an
     earlier patch), the attribute stops reflecting what is on screen.
     `<textarea>` has no `value` ATTRIBUTE at all — HTML only recognises its
     child text as an initial value, so `setAttribute` is silently a no-op
     and the box would never show state. `<select value>` is a React-only
     convenience with no HTML equivalent. `checked` on a checkbox/radio has
     the identical "default only" problem `value` does. A full-rebuild
     renderer (shared/student-runtime.js) never meets any of this, because
     every element it ever touches is brand new; a patch-in-place renderer
     meets it on every keystroke. */
  function isValueProp(tag, name) {
    return name === "value" && (tag === "input" || tag === "textarea" || tag === "select");
  }
  function isCheckedProp(tag, name) {
    return name === "checked" && tag === "input";
  }

  /* ── attribute patch: set/remove, and only touch the DOM when it changed ── */
  function patchAttr(el, tag, name, val) {
    if (isValueProp(tag, name)) {
      var s = (val === null || val === undefined) ? "" : String(val);
      if (el.value !== s) { el.value = s; }
      return;
    }
    if (isCheckedProp(tag, name)) {
      var b = !!val;
      if (el.checked !== b) { el.checked = b; }
      return;
    }
    if (val === null || val === undefined || val === false) {
      if (el.hasAttribute(name)) { el.removeAttribute(name); }
      return;
    }
    var str = String(val);
    if (el.getAttribute(name) !== str) { el.setAttribute(name, str); }
  }

  /* `style-hover` — Design's own attribute (2 uses in the pilot, both on the
     physics equation-sheet links). The declaration string is a template
     LITERAL (never `{{ }}`), so it is bound once, at element creation, and
     never re-examined on a patch — there is nothing to update. */
  function bindHover(el, css) {
    var decls = [];
    css.split(";").forEach(function (chunk) {
      var j = chunk.indexOf(":");
      if (j > 0) { decls.push([chunk.slice(0, j).trim(), chunk.slice(j + 1).trim()]); }
    });
    if (!decls.length) { return; }
    var prev = null;
    el.addEventListener("mouseenter", function () {
      prev = decls.map(function (d) {
        return [d[0], el.style.getPropertyValue(d[0]), el.style.getPropertyPriority(d[0])];
      });
      decls.forEach(function (d) { el.style.setProperty(d[0], d[1]); });
    });
    el.addEventListener("mouseleave", function () {
      if (!prev) { return; }
      prev.forEach(function (d) {
        if (d[1]) { el.style.setProperty(d[0], d[1], d[2]); } else { el.style.removeProperty(d[0]); }
      });
      prev = null;
    });
  }

  /* Click handlers are rebound on EVERY patch (a fresh closure per render is
     the normal shape of Design's code — see e.g. Ks4Choice's `onClick: () =>
     {…}` inside a `.map()`), so the element keeps ONE listener and the
     runtime swaps which function it calls by updating an expando the
     listener reads at call time — never adding a second listener. */
  function bindClick(el) {
    if (el.__mrbClickBound) { return; }
    el.__mrbClickBound = true;
    el.addEventListener("click", function (e) {
      if (typeof el.__mrbOnClick === "function") { el.__mrbOnClick(e); }
    });
    /* ⊕ carried from shared/student-runtime.js (experience run, 25 Sep 2026,
       Mide's items 2/3) — Enter/Space activate a clickable non-<button> that
       opted in with `tabindex`. Bound once; reads the current handler at
       call time so a rebind never needs to re-attach this. */
    el.addEventListener("keydown", function (e) {
      if (!el.hasAttribute("tabindex")) { return; }
      if (e.key === "Enter" || e.key === " " || e.key === "Spacebar") {
        e.preventDefault();
        if (typeof el.__mrbOnClick === "function") { el.__mrbOnClick(e); }
      }
    });
  }
  function bindChange(el, eventName) {
    if (el.__mrbChangeBound === eventName) { return; }
    el.__mrbChangeBound = eventName;
    el.addEventListener(eventName, function (e) {
      if (typeof el.__mrbOnChange === "function") { el.__mrbOnChange(e); }
    });
  }

  /* ============================================================================
     THE PATCH-BASED RENDERER

     `patchNode(tplNode, scope, ctx, live, svg)` renders/updates ONE compiled
     template node and returns `{live, doms}` — `live` is the (possibly new,
     possibly the same, mutated) persistent record to pass back in next time;
     `doms` is the flat, in-order list of actual DOM nodes this template node
     currently contributes to its parent (0 nodes for a false `sc-if`, N
     nodes for an `sc-for` list, exactly 1 for everything else).

     `patchKids(tplChildren, scope, ctx, liveArr, svg)` does this for a whole
     array of template children in parallel with a same-length array of live
     records, and hands back the concatenation of every child's `doms` — the
     desired child-node list for whatever element or fragment owns them.
     `reconcileDom(parentDom, desired)` then makes `parentDom`'s actual
     children match `desired`, moving/inserting/removing rather than
     recreating (a DOM node that is already the right one at the right
     position is never touched at all; a node that exists but has moved is
     relocated with `insertBefore`, which the DOM defines as a move, not a
     clone).
     ============================================================================ */

  function patchKids(tplChildren, scope, ctx, liveArr, svg) {
    var doms = [];
    for (var i = 0; i < tplChildren.length; i++) {
      var res = patchNode(tplChildren[i], scope, ctx, liveArr[i], svg);
      liveArr[i] = res.live;
      for (var j = 0; j < res.doms.length; j++) { doms.push(res.doms[j]); }
    }
    return doms;
  }

  function reconcileDom(parentDom, desired) {
    for (var i = 0; i < desired.length; i++) {
      var have = parentDom.childNodes[i];
      if (have !== desired[i]) {
        parentDom.insertBefore(desired[i], have || null);
      }
    }
    while (parentDom.childNodes.length > desired.length) {
      parentDom.removeChild(parentDom.lastChild);
    }
  }

  /* Tear down anything a shrinking `sc-for` or a falsified `sc-if` is
     discarding, so a child component's timers/listeners do not keep running
     against a detached instance (Ks4Chrome's `componentDidMount` registers a
     `window.addEventListener('scroll', …)`, which is exactly this case if a
     Chrome instance were ever conditionally mounted — none is in the pilot,
     but a shrinking `sc-for` of anything with a `dc-import` inside it is a
     real, current case, e.g. Ks4QuizBank's per-question option list). */
  function disposeLive(live) {
    if (!live) { return; }
    if (live.kind === "child" && live.inst) {
      try { live.inst.logic.componentWillUnmount(); } catch (e) { /* a child's teardown must not take the page down */ }
    }
    if (live.kids) { for (var i = 0; i < live.kids.length; i++) { disposeLive(live.kids[i]); } }
    if (live.sub) { for (var j = 0; j < live.sub.length; j++) { disposeLive(live.sub[j]); } }
    if (live.items) {
      for (var k = 0; k < live.items.length; k++) {
        var it = live.items[k];
        if (it && it.sub) { for (var m = 0; m < it.sub.length; m++) { disposeLive(it.sub[m]); } }
      }
    }
  }

  function patchNode(node, scope, ctx, live, svg) {
    var t = node.t;

    if (t === "helmet" || t === "sc-helmet") {
      return { live: live || { kind: "helmet" }, doms: [] };
    }

    if (t === "#") {
      var resolved = resolve(node.v, scope, ctx.miss);
      if (isFigMarker(resolved)) {
        return patchFig(node, resolved, live);
      }
      var txt = (resolved === null || resolved === undefined) ? "" : String(resolved);
      var isInterp = !!(node.v && node.v.parts);
      if (!live || live.kind !== "text" || live.interp !== isInterp) {
        disposeLive(live);
        var dom, textNode;
        if (isInterp) {
          dom = document.createElement("span");
          dom.className = "sc-interp";
          textNode = document.createTextNode(txt);
          dom.appendChild(textNode);
        } else {
          textNode = document.createTextNode(txt);
          dom = textNode;
        }
        return { live: { kind: "text", interp: isInterp, dom: dom, textNode: textNode, last: txt }, doms: [dom] };
      }
      if (live.last !== txt) { live.textNode.nodeValue = txt; live.last = txt; }
      return { live: live, doms: [live.dom] };
    }

    if (t === "if") {
      var on = !!lookup(node.e, scope, null);
      if (!live || live.kind !== "if") {
        disposeLive(live);
        live = { kind: "if", active: false, sub: new Array(node.c ? node.c.length : 0) };
      }
      if (!on) {
        if (live.active) {
          var subLive = live.sub;
          for (var d = 0; d < subLive.length; d++) { disposeLive(subLive[d]); }
          live.sub = new Array(node.c ? node.c.length : 0);
          live.active = false;
        }
        return { live: live, doms: [] };
      }
      live.active = true;
      var ifDoms = node.c ? patchKids(node.c, scope, ctx, live.sub, svg) : [];
      return { live: live, doms: ifDoms };
    }

    if (t === "for") {
      var list = lookup(node.e, scope, ctx.miss) || [];
      if (!live || live.kind !== "for") {
        disposeLive(live);
        live = { kind: "for", items: [] };
      }
      /* ⚠️ MATCHED BY INDEX, not by a key. None of the pilot's `sc-for` lists
         are reordered in place (checked: Sort/Chain move an item between a
         TRAY and a BIN/CHAIN array — two distinct `sc-for` lists — rather
         than permuting one list; the option/rung lists never reorder at
         all). Index matching is exact for grow/shrink at the tail, which is
         every case this pilot exercises, and is documented here as a real,
         bounded simplification rather than a silent one. */
      while (live.items.length > list.length) {
        var extra = live.items.pop();
        for (var e2 = 0; e2 < extra.sub.length; e2++) { disposeLive(extra.sub[e2]); }
      }
      while (live.items.length < list.length) {
        live.items.push({ sub: new Array(node.c ? node.c.length : 0) });
      }
      var forDoms = [];
      for (var idx = 0; idx < list.length; idx++) {
        var itemScope = Object.create(scope);
        itemScope[node.as] = list[idx];
        itemScope[node.as + "Index"] = idx;
        var itemDoms = node.c ? patchKids(node.c, itemScope, ctx, live.items[idx].sub, svg) : [];
        for (var f = 0; f < itemDoms.length; f++) { forDoms.push(itemDoms[f]); }
      }
      return { live: live, doms: forDoms };
    }

    if (t === "import") {
      /* The one design-system import the KS4 pilot inherited the SHAPE of
         from KS3 (`x-import`) — unused in this pilot (its brand mark is
         drawn inline by Ks4Chrome, not imported), kept only so a template
         compiled by the same browser-side walker as KS3's never hits an
         unhandled node type if one ever appears. */
      if (!live || live.kind !== "importx") {
        disposeLive(live);
        var xhost = document.createElement("div");
        xhost.className = "sc-host-x";
        xhost.setAttribute("style", "display: contents;");
        xhost.innerHTML = (ctx.imports && ctx.imports[node.from]) || "";
        live = { kind: "importx", dom: xhost };
      }
      return { live: live, doms: [live.dom] };
    }

    if (t === "child") {
      return patchChild(node, scope, ctx, live);
    }

    /* a plain HTML/SVG element */
    var isSvg = svg || t === "svg";
    if (!live || live.kind !== "el" || live.tag !== t || live.svg !== isSvg) {
      disposeLive(live);
      var el = isSvg ? document.createElementNS(SVG_NS, t) : document.createElement(t);
      if (node.i !== undefined) { el.setAttribute("data-dc-tpl", String(node.i)); }
      live = { kind: "el", tag: t, svg: isSvg, dom: el, kids: new Array(node.c ? node.c.length : 0) };
    }

    var elDom = live.dom;
    if (node.a) {
      for (var name in node.a) {
        if (!Object.prototype.hasOwnProperty.call(node.a, name)) { continue; }
        var aval = resolve(node.a[name], scope, ctx.miss);
        patchAttr(elDom, t, name, aval);
      }
    }
    if (node.on) {
      var fn = lookup(node.on, scope, ctx.miss);
      elDom.__mrbOnClick = (typeof fn === "function") ? fn : null;
      if (elDom.__mrbOnClick === null && ctx.miss && typeof fn !== "function" && fn !== undefined) {
        ctx.miss.push("onClick:" + node.on);
      }
      bindClick(elDom);
    }
    if (node.onch) {
      var chFn = lookup(node.onch, scope, ctx.miss);
      elDom.__mrbOnChange = (typeof chFn === "function") ? chFn : null;
      bindChange(elDom, t === "select" ? "change" : "input");
    }
    if (node.hov) { bindHover(elDom, node.hov); }
    if (node.ref && ctx.vals && ctx.vals[node.ref] && typeof ctx.vals[node.ref] === "object") {
      ctx.vals[node.ref].current = elDom;
    }

    /* ⊕ THEME RUN (26 Sep 2026) — a `data-mrb-theme` slot's children are
       owned by shared/theme.js, not by this template. The template authors
       ZERO children for this node on purpose (theme.js decides what a slot
       holds, mounts a live control into it, and manages that subtree
       itself — persistence, keyboard, System-mode updates); reconciling
       children against that empty authored list on every render would
       DELETE whatever theme.js has mounted the moment ANY re-render fires
       after it — proven live: `componentDidMount`'s own first re-render
       wiped the control while LEAVING theme.js's `data-mrb-theme-ready`
       flag behind (attributes are patched from the template, which never
       mentions that flag, so patchAttr above never clears it), which then
       poisons theme.js's OWN idempotency check (`build()` returns early
       once that flag reads "1") — so the control could never be re-mounted
       for the rest of that page's life. Skipping child reconciliation for
       this one attribute is the fix: the slot's own attributes still patch
       normally exactly as any other node's do; its children are simply
       never touched, by this render or any later one. */
    if (node.a && Object.prototype.hasOwnProperty.call(node.a, "data-mrb-theme")) {
      return { live: live, doms: [elDom] };
    }

    var childDoms = node.c ? patchKids(node.c, scope, ctx, live.kids, isSvg) : [];
    reconcileDom(elDom, childDoms);
    return { live: live, doms: [elDom] };
  }

  /* A `{{ }}` that resolved to a figure marker (see `isFigMarker` above) —
     the runtime's one primitive standing in for React's `dangerouslySet
     InnerHTML`. `innerHTML` is reassigned only when the SVG string actually
     changed, which is every tick while a bench is mid-animation (that IS
     the content changing) and never otherwise. */
  function patchFig(node, marker, live) {
    if (!live || live.kind !== "fig") {
      disposeLive(live);
      var div = document.createElement("div");
      if (node.i !== undefined) { div.setAttribute("data-dc-tpl", String(node.i)); }
      live = { kind: "fig", dom: div, lastHtml: null };
    }
    var el = live.dom;
    if (marker.alt !== undefined) {
      if (el.getAttribute("role") !== "img") { el.setAttribute("role", "img"); }
      var wantAlt = marker.alt || "";
      if (el.getAttribute("aria-label") !== wantAlt) { el.setAttribute("aria-label", wantAlt); }
    }
    var wantMax = marker.max || "100%";
    if (el.style.maxWidth !== wantMax) { el.style.maxWidth = wantMax; }
    var html = marker.__html || "";
    if (live.lastHtml !== html) { el.innerHTML = html; live.lastHtml = html; figFit(el, html); }
    return { live: live, doms: [el] };
  }

  /* ⊕ Loose-ends run, 17 Oct 2026 (fix 7a) — figure text floor on phones.
     Design's figures are `<svg viewBox="0 0 W H" style="width:100%">` whose text is sized in
     viewBox units, so on a 390px phone a 13-unit label in a 620-unit figure draws at ~7.5px. This
     does NOT change a word or move a label: it reads the figure's viewBox width and its smallest
     font-size out of the SVG string and publishes them as `--fig-vb` / `--fig-fs`; ks4-lesson.css
     (KS4_FIG_CSS, phones only, max-width 719.98px) then gives the <svg> a min-width of
     11px x vb / fs, so its smallest text is >= 11px, and the frame scrolls sideways when that is
     wider than the screen. A figure that already reads at >= 11px gets a min-width below 100% and
     is untouched; desktop (>= 720px) never matches the media query. `data-fig-over` is set only
     while the frame really overflows (it draws the right-edge fade and makes the frame
     keyboard-scrollable); `data-fig-end` drops the fade once the pupil has reached the end. */
  var FIG_RO = (typeof ResizeObserver === "function") ? new ResizeObserver(function (entries) {
    for (var i = 0; i < entries.length; i++) { figRefine(entries[i].target); figOver(entries[i].target); }
  }) : null;
  function figOver(el) {
    var over = el.scrollWidth > el.clientWidth + 1;
    if (over !== el.hasAttribute("data-fig-over")) {
      if (over) { el.setAttribute("data-fig-over", ""); el.setAttribute("tabindex", "0"); }
      else { el.removeAttribute("data-fig-over"); el.removeAttribute("tabindex"); }
    }
    var end = over && el.scrollLeft + el.clientWidth >= el.scrollWidth - 2;
    if (end !== el.hasAttribute("data-fig-end")) {
      if (end) { el.setAttribute("data-fig-end", ""); } else { el.removeAttribute("data-fig-end"); }
    }
  }
  function figFit(el, html) {
    var vb = /<svg[^>]*\sviewBox="\s*[\d.\-]+[ ,]+[\d.\-]+[ ,]+([\d.]+)[ ,]+[\d.]+/.exec(html);
    var min = Infinity, re = /font-size[=:]\s*"?([\d.]+)/g, m;
    while ((m = re.exec(html)) !== null) {
      var f = parseFloat(m[1]);
      if (f > 0 && f < min) { min = f; }
    }
    if (!vb || min === Infinity) {
      el.removeAttribute("data-fig-fit"); el.style.removeProperty("--fig-vb"); el.style.removeProperty("--fig-fs");
      figOver(el);
      return;
    }
    el.setAttribute("data-fig-fit", "");
    el.style.setProperty("--fig-vb", vb[1]);
    el.style.setProperty("--fig-fs", String(min));
    if (!el.__figWired) {
      el.__figWired = true;
      el.addEventListener("scroll", function () { figOver(el); }, { passive: true });
      if (FIG_RO) { FIG_RO.observe(el); }
    }
    figOver(el);
    if (typeof requestAnimationFrame === "function") {
      requestAnimationFrame(function () { figRefine(el); figOver(el); });
    }
  }
  /* The string scan above cannot see a `transform="scale()"` on a group, so a label written at 20 units can still
     draw at 0.79 of that. Once the figure is laid out, measure every drawn <text> / <tspan> in the real DOM, as
     font-size x (its screen scale / the figure's own viewBox scale), i.e. its size in viewBox units, and lower
     --fig-fs to the smallest. Subscript tspans (baseline-shift, written at 75% by ks4-ext) are part of a label that
     already clears the floor and are left out. */
  function figRefine(el) {
    var svg = el.querySelector("svg");
    if (!svg || !svg.getScreenCTM || !el.hasAttribute("data-fig-fit")) { return; }
    var base = svg.getScreenCTM();
    if (!base) { return; }
    var b = Math.hypot(base.a, base.b);
    if (!(b > 0)) { return; }
    var min = parseFloat(el.style.getPropertyValue("--fig-fs")) || Infinity;
    var nodes = svg.querySelectorAll("text, tspan");
    for (var i = 0; i < nodes.length; i++) {
      var t = nodes[i];
      if (t.hasAttribute("baseline-shift") || !(t.textContent || "").trim()) { continue; }
      if (t.tagName.toLowerCase() === "text" && t.querySelector("tspan")) { continue; }
      var m = t.getScreenCTM();
      var fs = parseFloat(getComputedStyle(t).fontSize);
      if (!m || !(fs > 0)) { continue; }
      var eff = fs * Math.hypot(m.a, m.b) / b;
      if (eff > 0 && eff < min) { min = eff; }
    }
    if (min !== Infinity && String(min) !== el.style.getPropertyValue("--fig-fs")) {
      el.style.setProperty("--fig-fs", String(min));
    }
  }

  /* ── child components: one persistent instance per `dc-import` position ──
     `node.comp` names one of the 11 registered blocks (ks4_lessons/
     blocks.py's COMPONENTS, and `ks4_pilot_check.py`'s gate refuses any page
     that imports a name outside it). `node.a` is the SAME shape a plain
     element's attrs are — `{kebab-name: {parts:[…]}}` — so building the
     child's props is: resolve every value against the PARENT's scope, then
     camelCase the key (`right-word` → `rightWord`, `on-commit` →
     `onCommit`). A prop that resolves to a function IS the parent's handler
     — `resolve()` returns it unstringified, same as any other value, so
     `on-commit="{{ onHook }}"` needs no separate "this one is an event"
     branch the way a plain element's `onClick=` attribute does. */
  function patchChild(node, scope, ctx, live) {
    var reg = ctx.components && ctx.components[node.comp];
    if (!reg) {
      throw new Error("ks4-runtime: no registered component " + node.comp
        + " (dc-import at template index " + node.i + "). Registered: "
        + Object.keys(ctx.components || {}).join(", "));
    }
    var props = {};
    for (var name in node.a) {
      if (!Object.prototype.hasOwnProperty.call(node.a, name)) { continue; }
      props[camel(name)] = resolve(node.a[name], scope, ctx.miss);
    }
    if (!live || live.kind !== "child" || live.comp !== node.comp) {
      disposeLive(live);
      var host = document.createElement("div");
      host.setAttribute("style", "display: contents;");
      if (node.i !== undefined) { host.setAttribute("data-dc-tpl", String(node.i)); }
      var inst = createInstance(reg.Component, props, reg.template, ctx.components, host, node.comp);
      live = { kind: "child", comp: node.comp, dom: host, inst: inst };
      return { live: live, doms: [host] };
    }
    /* ⚠️ ALWAYS re-draws the child, deliberately, rather than shallow-
       comparing old vs new props first. Design's `renderVals()` methods
       build a FRESH closure for every callback prop on every call (e.g.
       `onClick: () => this.setState({pick: i})` inside a `.map()`), so a
       reference-equality prop comparison would read "changed" on every
       single parent render regardless of whether anything the child cares
       about actually moved — it would never skip a redraw, only add the
       bookkeeping cost of computing that. The child's OWN `state` lives on
       `live.inst.logic.state`, never reassigned here, so it survives this
       exactly as it survives any other parent redraw — that is the part of
       "re-renders when its props change" that is actually load-bearing, and
       it holds regardless of how often `setProps` below runs. */
    live.inst.setProps(props);
    return { live: live, doms: [live.dom] };
  }

  /* ============================================================================
     INSTANCE — shared by the root `mount()` and every child `dc-import`.
     Owns one `DCLogic` instance, its persistent live tree (parallel to
     `template.roots`), and the render scheduler `setState` posts to.
     ============================================================================ */
  function createInstance(ComponentClass, initialProps, template, components, hostDom, compName) {
    var logic = new ComponentClass(initialProps);
    var liveRoots = new Array(template.roots.length);
    var pending = null, queued = [], lastProps = shallow(logic.props);
    var api = {
      logic: logic,
      // ⊕ Parent truth — the block's registered name ("Ks4Ladder", …) and
      // its host and compiled template, so the read-only tap above can tell
      // one block from another, find a block's own Ks4Chain / Ks4Write
      // inside it, and number a lesson's blocks in their AUTHORED order
      // (template order). `comp` is undefined on the page's root instance.
      comp: compName,
      host: hostDom,
      template: template,
      misses: [],
      renders: 0,
      schedule: function (cb) {
        if (cb) { queued.push(cb); }
        if (pending) { return; }
        pending = (window.requestAnimationFrame || window.setTimeout)(function () {
          pending = null;
          api.draw();
          var cbs = queued; queued = [];
          cbs.forEach(function (f) { f(); });
          var prevProps = lastProps;
          lastProps = shallow(logic.props);
          logic.componentDidUpdate(prevProps);
          /* ⊕ Parent truth (11 Oct 2026) — a read-only look at the state a
             setState just drew, for a consumer child's answer capture
             (mrbadmus.v2.js sets MrBadmusKS4Tap on a child session and on
             nothing else). It is handed this instance and may only READ it:
             it never sets state, never touches the DOM, and a throw from it
             is swallowed here so it can never break a lesson. Absent — every
             school pupil — this is one typeof and nothing happens. */
          var tap = window.MrBadmusKS4Tap;
          if (typeof tap === "function") {
            try { tap(api); } catch (e) { /* capture never breaks a lesson */ }
          }
        }, 0);
      },
      setProps: function (newProps) {
        var prevProps = shallow(logic.props);
        logic.props = newProps;
        api.draw();
        logic.componentDidUpdate(prevProps);
      },
      draw: function () {
        var vals = logic.renderVals() || {};
        var scope = Object.create(vals);
        for (var k in logic.props) { if (!(k in vals)) { scope[k] = logic.props[k]; } }
        var ctx = { vals: vals, miss: [], imports: {}, components: components };
        var doms = patchKids(template.roots, scope, ctx, liveRoots, false);
        reconcileDom(hostDom, doms);
        api.misses = ctx.miss;
        api.renders += 1;
        hostDom.setAttribute("data-mrb-renders", String(api.renders));
        hostDom.setAttribute("data-mrb-misses", String(ctx.miss.length));
      }
    };
    logic.__host = api;
    // A JS property, not an attribute: nothing is added to the markup.
    hostDom.__mrbKs4 = api;
    api.draw();
    logic.componentDidMount();
    return api;
  }

  /* ── mount: the page's own entry point ──────────────────────────────── */
  function mount(opts) {
    var host = document.querySelector(opts.into);
    if (!host) { throw new Error("ks4-runtime: no mount point " + opts.into); }
    var components = opts.components || window.KS4_BLOCKS || {};
    return createInstance(opts.Component, opts.props || {}, opts.template, components, host);
  }

  /* ⊕ KS4-CHIP-2 (Mide's ruling, 27 Sep 2026; ks4_rulings.py R12) — the
     header route switcher is a native <details>/<summary> disclosure,
     which already gives Enter/Space to toggle it and Tab to reach the
     menu's plain links with NO script at all — the links are already
     static <a> elements in the prerendered HTML (see shared/ks4-lesson.css's
     own comment on this). This delegated listener adds only what native
     disclosure does not supply on its own: keeping the chip's aria-expanded
     in sync with the open state, and (below) Esc closing the switcher and
     returning focus to its chip. Runs once, at script load: the switcher is
     part of the STATIC, prerendered markup, already in the DOM by the time
     this script tag runs (it sits after #ks4-mount in every page's
     <body>), so there is nothing to wait for.

     ⚠️ Deliberately a 'click' listener, not the native 'toggle' event.
     Native <summary> click/keyboard activation queues 'toggle' as an
     ASYNC task (HTML spec's "details notification task steps") — it does
     NOT fire in the same tick as the click, confirmed empirically: a gate
     that clicks then reads aria-expanded synchronously (one eval, no
     await) always saw the STALE value. A 'click' listener runs BEFORE the
     browser's own default action (the toggle itself) on ANY interactive
     element, so `d.open` read here is still the PRE-click value — the
     click is ABOUT to flip it — and the new value can be set synchronously
     with no race at all. Bubble phase suffices (chip clicks always reach
     document); delegated via `.closest()` so a click anywhere inside the
     chip (its label text, its caret svg) still resolves to the chip. */
  document.addEventListener("click", function (e) {
    var chip = e.target && e.target.closest && e.target.closest(".ks3-route-chip");
    if (!chip) { return; }
    var d = chip.closest(".ks3-route-switch");
    if (!d) { return; }
    chip.setAttribute("aria-expanded", d.open ? "false" : "true");
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape" && e.key !== "Esc") { return; }
    var openSwitch = document.querySelector(".ks3-route-switch[open]");
    if (!openSwitch) { return; }
    var summary = openSwitch.querySelector("summary");
    openSwitch.removeAttribute("open");
    // Chrome does not fire 'toggle' for a script-driven attribute removal
    // (confirmed empirically — only a real user click on <summary> fires
    // it), so aria-expanded is set directly here rather than left to the
    // listener above.
    if (summary) {
      summary.setAttribute("aria-expanded", "false");
      summary.focus();
    }
  });

  window.MrbRef = MrbRef;
  window.DCLogic = DCLogic;
  window.MrBadmusKS4Runtime = {
    DCLogic: DCLogic, mount: mount, lookup: lookup, resolve: resolve,
    createInstance: createInstance
  };
})();
