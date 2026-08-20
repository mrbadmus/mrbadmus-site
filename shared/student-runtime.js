/* ═══════════════════════════════════════════════════════════════════════
   student-runtime.js — Claude Design's templates and logic, without React.

   RULED 20 Aug 2026: port Design's logic to vanilla JavaScript; do not ship
   Design's compiled React bundle onto a student page.

   This is the whole runtime that replaces it. It is ~250 lines against
   `support.js`'s ~1900 plus React, and it does three things:

     1. `MrbLogic`   — the base class Design's logic extends. Design's file
                       says `extends DCLogic`; `DCLogic` is aliased to this.
                       Surface: props, state, setState, forceUpdate, the three
                       lifecycle hooks, renderVals. That is all `support.js`
                       exposes to a logic class, so that is all this needs.
     2. `render`     — the three template constructs (`sc-if`, `sc-for`,
                       `{{ }}`) plus onClick, style-hover and refs.
     3. `mount`      — first paint, then re-render on state change.

   ── What is Design's and what is ours ──────────────────────────────────

   Design's logic class ships VERBATIM, extracted by `student_template.py`.
   It is 492 lines of view-model computation for the class view and 612 for the
   assignment, it contains no JSX, and it touched React exactly once —
   `React.createRef()`, rewritten to `MrbRef()` at compile time. Retyping it
   would satisfy "reproduce Design's behaviour" only for as long as nobody made
   a mistake, which is the same argument `build_student.py` already makes about
   the markup.

   So the BEHAVIOUR is Design's and the RUNTIME is ours. Nothing of Claude
   Design's rendering layer ships.

   ── The re-render is a full rebuild, deliberately ──────────────────────

   No virtual DOM, no reconciliation, no keys. The class view is 395 template
   nodes; rebuilding it costs well under a frame on the phones this is for, and
   a reconciler is a large amount of subtle code whose bugs look like "the page
   is occasionally wrong". What a rebuild costs instead is focus and scroll,
   and both are restored explicitly below — which is a dozen lines that can be
   read and checked, rather than a diffing algorithm that cannot.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var SVG_NS = "http://www.w3.org/2000/svg";

  function MrbRef() { return {current: null}; }

  /* ── the base class Design's logic extends ─────────────────────────── */
  function MrbLogic(props) {
    this.props = props || {};
    this.state = {};
    this.__host = null;
  }
  MrbLogic.prototype.setState = function (update, cb) {
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
  MrbLogic.prototype.forceUpdate = function (cb) {
    if (this.__host) { this.__host.schedule(cb); } else if (cb) { cb(); }
  };
  MrbLogic.prototype.componentDidMount = function () {};
  MrbLogic.prototype.componentDidUpdate = function () {};
  MrbLogic.prototype.componentWillUnmount = function () {};
  MrbLogic.prototype.renderVals = function () { return {}; };

  /* ── expression lookup ─────────────────────────────────────────────────
     Every `{{ }}` in both templates is a plain property path — `benchCols`,
     `c.barWidth`, `r.isMarked`. Counted: 222 distinct on the class view, not
     one of them containing an operator. So this is a lookup, not an evaluator,
     and deliberately: an evaluator on a student page is a much larger surface
     for no benefit Design's templates ask for.

     A path that does not resolve returns undefined rather than throwing, which
     matches what the template would have rendered under React, and `__miss`
     records it so the gate can see a binding that silently renders nothing. */
  function lookup(expr, scope, miss) {
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
      /* A single expression keeps its TYPE — `{{ r.items }}` must stay an
         array and `{{ o.ok }}` must stay a boolean. Only a mixed
         literal/expression run becomes a string. */
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

  /* ── the renderer ──────────────────────────────────────────────────── */
  function build(node, scope, ctx, into, svg) {
    var i;
    if (node.t === "#") {
      var txt = resolve(node.v, scope, ctx.miss);
      txt = (txt === null || txt === undefined) ? "" : String(txt);
      /* ⚠️ AN INTERPOLATION GETS A WRAPPER SPAN AND A LITERAL DOES NOT.
         Design's compiler emits `<span class="sc-interp">` around every `{{ }}`
         in text position — 132 of them on the class view, which was exactly
         the node-count delta when this renderer emitted bare text nodes
         instead. They carry no styling, so the page LOOKED right either way;
         what they carry is structure, and structure is what the parity gate
         is for. A reproduction that is visually identical and structurally 132
         nodes short is not a reproduction, and the difference would have shown
         up later as a selector that matched nothing. */
      if (node.v && node.v.parts) {
        var w = document.createElement("span");
        w.className = "sc-interp";
        w.appendChild(document.createTextNode(txt));
        into.appendChild(w);
      } else {
        into.appendChild(document.createTextNode(txt));
      }
      return;
    }
    if (node.t === "if") {
      if (lookup(node.e, scope, null)) {
        kids(node, scope, ctx, into, svg);
      }
      return;
    }
    if (node.t === "for") {
      var list = lookup(node.e, scope, ctx.miss);
      if (!list || !list.length) { return; }
      for (i = 0; i < list.length; i++) {
        /* A shallow child scope: the loop variable shadows, everything else
           falls through to the parent. `Object.create` rather than a copy so a
           twelve-week spine does not clone the whole view model twelve times. */
        var sub = Object.create(scope);
        sub[node.as] = list[i];
        sub[node.as + "Index"] = i;
        kids(node, sub, ctx, into, svg);
      }
      return;
    }
    if (node.t === "import") {
      /* The one imported design-system component, `MrBadmusDS.BrandMark`.
         Its rendered markup is captured from Design's own file at compile time
         rather than retyped, for the same reason as everything else here. */
      var host = document.createElement("div");
      host.className = "sc-host-x";
      host.setAttribute("style", "display: contents;");
      if (node.i !== undefined) { host.setAttribute("data-dc-tpl", node.i); }
      host.innerHTML = ctx.imports[node.from] || "";
      into.appendChild(host);
      return;
    }

    /* THE HELMET IS PARSED AND NOT RENDERED. `student_template.py` compiles
       from `<helmet>` so that the `data-dc-tpl` numbering matches Design's —
       the helmet's nine element nodes take indices 0..8 — but its contents are
       six `<link>`, a `<script>` and a `<style>` that belong in <head>, and
       the build has already put the stylesheet there. Rendering them into the
       body gave six 404s per load, because their hrefs are relative to
       Design's bundle and not to the site. */
    if (node.t === "helmet" || node.t === "sc-helmet") { return; }

    var isSvg = svg || node.t === "svg";
    var el = isSvg ? document.createElementNS(SVG_NS, node.t)
                   : document.createElement(node.t);
    if (node.i !== undefined) { el.setAttribute("data-dc-tpl", node.i); }

    if (node.a) {
      for (var name in node.a) {
        if (!Object.prototype.hasOwnProperty.call(node.a, name)) { continue; }
        var val = resolve(node.a[name], scope, ctx.miss);
        if (val === null || val === undefined || val === false) { continue; }
        el.setAttribute(name, String(val));
      }
    }

    if (node.on) {
      var fn = lookup(node.on, scope, ctx.miss);
      if (typeof fn === "function") {
        el.addEventListener("click", fn);
      } else if (ctx.miss) {
        ctx.miss.push("onClick:" + node.on);
      }
    }

    /* `style-hover` — Design's own attribute, 20 uses on the class view.
       Applied with listeners rather than a generated stylesheet rule: the
       declarations are inline and per-element, so there is no selector to hang
       a rule on that would not need inventing one. Restores exactly the
       declarations it set, so it cannot leak into the base style. */
    if (node.hov) {
      hover(el, node.hov);
    }

    if (node.ref && ctx.vals && ctx.vals[node.ref] &&
        typeof ctx.vals[node.ref] === "object") {
      ctx.vals[node.ref].current = el;
    }

    kids(node, scope, ctx, el, isSvg);
    into.appendChild(el);
  }

  function kids(node, scope, ctx, into, svg) {
    if (!node.c) { return; }
    for (var i = 0; i < node.c.length; i++) {
      build(node.c[i], scope, ctx, into, svg);
    }
  }

  function hover(el, css) {
    var decls = [];
    css.split(";").forEach(function (chunk) {
      var j = chunk.indexOf(":");
      if (j > 0) {
        decls.push([chunk.slice(0, j).trim(), chunk.slice(j + 1).trim()]);
      }
    });
    if (!decls.length) { return; }
    var prev = null;
    el.addEventListener("mouseenter", function () {
      prev = decls.map(function (d) {
        return [d[0], el.style.getPropertyValue(d[0]),
                el.style.getPropertyPriority(d[0])];
      });
      decls.forEach(function (d) { el.style.setProperty(d[0], d[1]); });
    });
    el.addEventListener("mouseleave", function () {
      if (!prev) { return; }
      prev.forEach(function (d) {
        if (d[1]) { el.style.setProperty(d[0], d[1], d[2]); }
        else { el.style.removeProperty(d[0]); }
      });
      prev = null;
    });
  }

  /* ── binding Design's identity strings, without adding a node ────────
     Design typed `8r/Sc1`, `Ayo`, `Mr Badmus` and `28 students` straight into
     the markup, so they are LITERAL text nodes and not `{{ }}`. The obvious
     fix — rewrite them into interpolations — is the wrong one: Design's
     compiler wraps every interpolation in text position in a
     `<span class="sc-interp">`, so eleven rewrites would be eleven extra
     elements and the parity gate counts elements. A page that says the right
     name and has a different shape from Design's is not the port.

     So the value is swapped in the COMPILED TEMPLATE instead, before the first
     render. The node stays exactly the node Design compiled — same position,
     same kind, still a literal — and only its text differs. The shipped
     template carries an empty string at each of these paths; the value comes
     from the data source, and there is no path by which it comes from
     anywhere else.

     `get` is either the page's `MRB_DATA` (which throws on a missing key) or a
     plain object. Both are accepted, neither is defaulted: a binding whose key
     is absent must be loud, because the failure it would otherwise cause is a
     student greeted by name as somebody else. */
  function applyBindings(roots, bindings, get) {
    if (!roots) { throw new Error("student-runtime: applyBindings: no roots"); }
    if (!bindings || !bindings.length) { return roots; }
    var read = (typeof get === "function") ? get : function (k) {
      if (!get || !(k in get)) {
        throw new Error('student-runtime: no data for binding "' + k + '"');
      }
      return get[k];
    };
    var out = JSON.parse(JSON.stringify(roots));
    for (var i = 0; i < bindings.length; i++) {
      var b = bindings[i], node = out[b.p[0]], j;
      for (j = 1; j < b.p.length; j++) {
        node = node && node.c && node.c[b.p[j]];
      }
      if (!node || node.t !== "#") {
        throw new Error('student-runtime: the binding path for "' + b.k +
                        '" does not land on a text node — the template and ' +
                        'the binding table were built from different sources.');
      }
      var v = read(b.k);
      node.v = (v === null || v === undefined) ? "" : String(v);
    }
    return out;
  }

  /* ── focus and scroll across a rebuild ─────────────────────────────── */
  function focusPath(root) {
    var el = document.activeElement, path = [];
    if (!el || el === document.body || !root.contains(el)) { return null; }
    while (el && el !== root) {
      var p = el.parentElement;
      if (!p) { return null; }
      path.unshift(Array.prototype.indexOf.call(p.children, el));
      el = p;
    }
    return path;
  }

  function refocus(root, path) {
    if (!path) { return; }
    var el = root, i;
    for (i = 0; i < path.length; i++) {
      if (!el.children || !el.children[path[i]]) { return; }
      el = el.children[path[i]];
    }
    if (el && el.focus) { el.focus({preventScroll: true}); }
  }

  function shallow(o) {
    var out = {};
    for (var k in o) {
      if (Object.prototype.hasOwnProperty.call(o, k)) { out[k] = o[k]; }
    }
    return out;
  }

  /* ── mount ─────────────────────────────────────────────────────────── */
  function mount(opts) {
    var host = document.querySelector(opts.into);
    if (!host) { throw new Error("student-runtime: no mount point " + opts.into); }

    var logic = new opts.Component(opts.props || {});
    var pending = null, queued = [], lastProps = shallow(logic.props);

    var api = {
      logic: logic,
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
          /* ⚠️ `componentDidUpdate` TAKES prevProps, and it is not decorative.
             The assignment's reads `prev.scenario` and `prev.questionCount` on
             the first line of its body, so calling it with nothing threw a
             TypeError on every state change — the page still rendered, because
             the throw happened AFTER the draw, which is exactly the shape of
             bug that survives a screenshot. Props do not change on these two
             pages today (they are Design's editor tweaks), so a snapshot of
             the previous props is enough and a deep clone would be pretending
             to solve a problem nobody has. */
          var prevProps = lastProps;
          lastProps = shallow(logic.props);
          logic.componentDidUpdate(prevProps);
        }, 0);
      },
      draw: function () {
        var vals = logic.renderVals() || {};
        var scope = Object.create(vals);
        for (var k in logic.props) {
          if (!(k in vals)) { scope[k] = logic.props[k]; }
        }
        var ctx = {vals: vals, miss: [], imports: opts.imports || {}};
        var frag = document.createDocumentFragment();
        for (var i = 0; i < opts.template.roots.length; i++) {
          build(opts.template.roots[i], scope, ctx, frag, false);
        }
        var keepFocus = focusPath(host);
        var keepScroll = window.scrollY;
        host.textContent = "";
        host.appendChild(frag);
        refocus(host, keepFocus);
        if (window.scrollY !== keepScroll) { window.scrollTo(0, keepScroll); }
        api.misses = ctx.miss;
        api.renders += 1;
        /* Counted onto the mount point so a gate reads a number instead of
           inferring from a screenshot that a binding rendered nothing. */
        host.setAttribute("data-mrb-renders", String(api.renders));
        host.setAttribute("data-mrb-misses", String(ctx.miss.length));
      }
    };

    logic.__host = api;
    api.draw();
    logic.componentDidMount();
    return api;
  }

  window.MrbRef = MrbRef;
  window.MrBadmusStudentRuntime = {
    MrbLogic: MrbLogic, mount: mount, lookup: lookup, resolve: resolve,
    applyBindings: applyBindings
  };
})();
