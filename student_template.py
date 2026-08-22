#!/usr/bin/env python3
"""student_template.py — Design's template, compiled. Design's logic, extracted.

    python3 student_template.py            # compile, write, report
    python3 student_template.py --check    # recompile and diff; exit 1 on any change

Writes `student_templates.json`: for each page, the compiled template tree and
the logic-class source, ready for `shared/student-runtime.js` to render without
React and without Claude Design's `support.js`.

── The ruling this implements ────────────────────────────────────────────

*"PORT DESIGN'S LOGIC TO VANILLA JAVASCRIPT. Do not ship Design's compiled
React bundle onto a student page."* (20 Aug 2026.)

The reasons given were a second paradigm on the surface students use most, a
runtime we neither control nor can patch, and page weight.

⚑ ONE OF THOSE THREE WAS MEASURING THE WRONG ARTEFACT, and it is worth
recording because it makes the ruling MORE right rather than less. The "551 KB
against the live page's 56 KB" is the SNAPSHOT's weight, and there is no React
in it at all — the previews contain none. Measured on the 558 KB class view:

    306 KB (55%)  10,924 `: unset;` declarations — Chrome's longhand expansion
                  of `all: unset` on Design's 25 buttons, which the snapshot
                  baked in because it read back computed inline styles
    223 KB (40%)  the `_ds` CSS bundle, inlined, which should be one cached
                  stylesheet shared by both pages
     28 KB ( 5%)  the actual markup

So the weight was never React's and never Design's; it was the photograph's.
Emitting Design's own template puts the page back in the same order as the
live one.

── What "porting the logic" means here, precisely ────────────────────────

Design's logic class is PLAIN JAVASCRIPT. It has no JSX in it and touches React
exactly once, for `React.createRef()`. Everything React about the delivery lives
in `support.js`, which is the rendering layer — and the rendering layer is the
part being replaced.

So the logic is EXTRACTED VERBATIM, not retyped. `build_student.py` already
argues this at length for the markup and the argument is identical here: 492
lines of view-model computation, hand-copied, would satisfy "reproduce Design's
behaviour" only for as long as nobody made a mistake, and every future edit
would be a fresh chance to drift. What ships is Design's own computation on a
runtime of ours — `shared/student-runtime.js`, a ~30-line `DCLogic` base and a
renderer for the three template constructs.

⚠️ THE TEMPLATE IS PARSED IN THE BROWSER, NOT IN PYTHON. An earlier attempt at
mapping this template with `html.parser` produced element indices that did not
match the rendered DOM at all — the browser applies implicit fixups and
`support.js` runs the source through an `encodeCase` pass first. Loading the
markup into a real `<template>` and walking it is the only way the tree this
emits is the tree the browser would build.
"""

import json
import os
import re
import sys

REF = os.path.join("docs", "ks3", "design-reference", "student")
OUT = "student_templates.json"

AMEND = os.path.join("docs", "ks3", "design-reference", "class-view-amendments")

# ⊕ 22 Aug 2026 — THE DONOR. Design's class-view amendments compile as a THIRD
# page that is never emitted. Nothing renders it; `build_student_port.py` reads
# its tree and grafts the changed regions onto the live class view.
#
# It is compiled rather than hand-copied for the same reason the brand SVG is
# captured rather than retyped: the amended regions are 70 KB of Design's
# markup, and a merge that retyped any of it would drift the first time
# somebody tidied a style string.
PAGES = [
    dict(page="class view", src="source/Class View.dc.html"),
    dict(page="assignment", src="source/Assignment.dc.html"),
    dict(page="class view amendments", src="source/KS3 Class View.dc.html",
         ref=AMEND, standalone="standalone/ks3-class-view-bench-open.html"),
]

# The three constructs, plus interpolation, plus the one imported component.
# Counted on the class-view template: 47 `sc-if`, 18 `sc-for`, 1 `x-import`,
# 222 distinct `{{ }}` expressions, 26 `onClick`, 20 `style-hover`. Every
# expression is a plain property path (`benchCols`, `c.barWidth`, `r.isMarked`)
# — there is no arithmetic in the template, which is why the renderer needs a
# property lookup and not an expression evaluator.
_COMPILE_JS = r"""
(function (html) {
  var t = document.createElement('template');
  t.innerHTML = html;

  function interp(s) {
    // A string is either constant or a list of literal/expression parts.
    if (s.indexOf('{{') === -1) { return s; }
    var parts = [], re = /\{\{\s*([^}]+?)\s*\}\}/g, last = 0, m;
    while ((m = re.exec(s)) !== null) {
      if (m.index > last) { parts.push(s.slice(last, m.index)); }
      parts.push({e: m[1]});
      last = m.index + m[0].length;
    }
    if (last < s.length) { parts.push(s.slice(last)); }
    return {parts: parts};
  }

  var n = 0;
  function walk(node) {
    if (node.nodeType === 3) {
      var v = node.nodeValue;
      if (!v.trim()) { return null; }
      return {t: '#', v: interp(v)};
    }
    if (node.nodeType !== 1) { return null; }

    var tag = node.tagName.toLowerCase();
    var idx = n++;

    // sc-if / sc-for are control flow, not elements. They keep an index
    // because `support.js` stamps every element node including these, and the
    // indices have to line up with the ones already measured in
    // student_switches.json.
    if (tag === 'sc-if') {
      return {t: 'if', i: idx, e: (node.getAttribute('value') || '')
                .replace(/^\{\{\s*|\s*\}\}$/g, ''),
              c: kids(node)};
    }
    if (tag === 'sc-for') {
      return {t: 'for', i: idx,
              e: (node.getAttribute('list') || '')
                 .replace(/^\{\{\s*|\s*\}\}$/g, ''),
              as: node.getAttribute('as') || 'it', c: kids(node)};
    }
    if (tag === 'x-import') {
      return {t: 'import', i: idx,
              from: node.getAttribute('component-from-global-scope') || '',
              size: node.getAttribute('size') || ''};
    }

    var out = {t: tag, i: idx, a: {}, c: kids(node)};
    for (var k = 0; k < node.attributes.length; k++) {
      var at = node.attributes[k], name = at.name, val = at.value;
      if (name === 'hint-placeholder-count' || name === 'hint-placeholder-val' ||
          name === 'hint-size' || name === 'sc-name') { continue; }
      if (name === 'onclick') { out.on = val.replace(/^\{\{\s*|\s*\}\}$/g, ''); continue; }
      if (name === 'ref') { out.ref = val.replace(/^\{\{\s*|\s*\}\}$/g, ''); continue; }
      if (name === 'style-hover') { out.hov = val; continue; }
      out.a[name] = interp(val);
    }
    if (!Object.keys(out.a).length) { delete out.a; }
    if (!out.c.length) { delete out.c; }
    return out;
  }

  function kids(node) {
    var out = [];
    for (var i = 0; i < node.childNodes.length; i++) {
      var c = walk(node.childNodes[i]);
      if (c) { out.push(c); }
    }
    return out;
  }

  var roots = [];
  for (var i = 0; i < t.content.childNodes.length; i++) {
    var r = walk(t.content.childNodes[i]);
    if (r) { roots.push(r); }
  }
  return JSON.stringify({n: n, roots: roots});
})(%s)
"""


# ── camelCase attributes, and why they cannot just be lowercased ─────────
#
# HTML parsing lowercases attribute names. `strokeWidth` becomes `strokewidth`,
# which is not an SVG attribute at all — the SVG name is `stroke-width` — so
# every stroke on the page would silently fall back to its default of 1px.
# Measured before this was fixed: 126 `strokeWidth`, 36 `strokeLinecap`, 26
# `strokeLinejoin`, 17 `textAnchor`, 12 `dominantBaseline`, 2 `strokeDasharray`
# across the two templates, all of them going nowhere.
#
# Design's `support.js` has the same problem and solves it the other way: it
# rewrites camel to kebab with a marker prefix and decodes back to CAMEL at
# render time, because React wants React's names. This renderer sets attributes
# on real SVG elements, so it wants SVG's names, and rewrites them once here.
#
# ⚠️ `viewBox` AND `preserveAspectRatio` ARE GENUINELY camelCase IN SVG and are
# deliberately absent from this map. They survive the parse untouched because
# an `<svg>` subtree is parsed in the SVG namespace, where the parser
# case-corrects both from the lowercase form. Kebab-casing them would break
# them exactly as surely as leaving `strokeWidth` alone breaks that.
CAMEL_TO_SVG = {
    "strokeWidth": "stroke-width",
    "strokeLinecap": "stroke-linecap",
    "strokeLinejoin": "stroke-linejoin",
    "strokeDasharray": "stroke-dasharray",
    "strokeDashoffset": "stroke-dashoffset",
    "strokeOpacity": "stroke-opacity",
    "strokeMiterlimit": "stroke-miterlimit",
    "fillOpacity": "fill-opacity",
    "fillRule": "fill-rule",
    "clipPath": "clip-path",
    "clipRule": "clip-rule",
    "textAnchor": "text-anchor",
    "dominantBaseline": "dominant-baseline",
    "vectorEffect": "vector-effect",
    "paintOrder": "paint-order",
    "fontSize": "font-size",
    "fontFamily": "font-family",
    "fontWeight": "font-weight",
    "letterSpacing": "letter-spacing",
    "shapeRendering": "shape-rendering",
}

# camelCase attribute names that are correct as they stand. Anything camelCase
# that is in NEITHER this set nor the map above stops the build, rather than
# being guessed at in one direction or the other.
CAMEL_KEEP = {"viewBox", "preserveAspectRatio", "gradientUnits",
              "gradientTransform", "patternUnits", "clipPathUnits",
              "markerWidth", "markerHeight", "refX", "refY", "spreadMethod",
              "startOffset", "textLength", "lengthAdjust", "baseFrequency",
              "numOctaves", "stdDeviation", "onClick"}


# ── the one ruled correction to the delivery ──────────────────────────────
#
# ⚖️ RULED 20 Aug 2026: `--st-ok-room` is GRAPHIC ONLY. Design's recall feedback
# panel gives one value, `fbEdge`, two jobs — the panel's 3px left edge, which
# is a legal graphic use, and the 9.5px `CORRECT` label's ink, which is not.
# Found by DRIVING Design's file (Recall → pick the right option → Check), not
# by reading it; it is behind two interactions and no snapshot contains it.
#
# It is not a contrast defect: 6.68:1 on `--st-room-panel`, which passes AA for
# text twice over. It is a system defect — the family already has the token for
# that job, `--ks3-ok-dark` #40DD84 at 9.88:1 on the same panel, minted under
# MRB-252 as "body-size green on an INK-DARK ground".
#
# So the two jobs are split: the EDGE keeps Design's value, the LABEL takes the
# text green. Both rewrites are guarded — if either pattern moves in a future
# delivery this build stops rather than silently shipping the violation again.
# This is the same shape as the `React.createRef()` rewrite below: a documented,
# minimal, failing-loud transformation of the delivery, and the only two in the
# build.
FB_LOGIC_FROM = "fbEdge: rightPick ? 'var(--st-ok-room)' : 'var(--st-ember)',"
FB_LOGIC_TO = (
    "fbEdge: rightPick ? 'var(--st-ok-room)' : 'var(--st-ember)',\n"
    "      // ⊕ MRB-270 phase 3, RULED 20 Aug 2026: the LABEL is text, and\n"
    "      // --st-ok-room is graphic-only. The 3px edge above keeps it.\n"
    "      fbLabelColor: rightPick ? 'var(--ks3-ok-dark)' : 'var(--st-ember)',")
FB_TPL_FROM = 'letter-spacing:0.13em;color:{{ fbEdge }}"'
FB_TPL_TO = 'letter-spacing:0.13em;color:{{ fbLabelColor }}"'


def split_feedback_edge(tpl, logic, where):
    """Give the CORRECT label its own, text-legal green. Refuse if it moved."""
    if where != "class view":
        return tpl, logic, False
    if FB_LOGIC_FROM not in logic:
        raise SystemExit(
            "student_template.py: the recall feedback edge no longer reads\n"
            "    %s\n"
            "  in Design's logic. That line is where `--st-ok-room` was being\n"
            "  painted as `color:` on the 9.5px CORRECT label, which the 20 Aug\n"
            "  2026 ruling forbids. If Design has fixed it, delete this rewrite\n"
            "  and the ST_DELIVERY_KNOWN entry in ks3_parity.py together. Do not\n"
            "  skip it: a rewrite that silently matches nothing is how the\n"
            "  violation comes back." % FB_LOGIC_FROM)
    if tpl.count(FB_TPL_FROM) != 1:
        raise SystemExit(
            "student_template.py: expected exactly one `color:{{ fbEdge }}` in "
            "the class-view template and found %d. The label and the panel edge "
            "share one value and this rewrite splits them; it cannot do that "
            "safely if the shape has changed." % tpl.count(FB_TPL_FROM))
    return (tpl.replace(FB_TPL_FROM, FB_TPL_TO, 1),
            logic.replace(FB_LOGIC_FROM, FB_LOGIC_TO, 1), True)


def kebab_svg_attrs(tpl, where):
    """Rewrite React-cased SVG attributes to their SVG names, or refuse."""
    seen = set(re.findall(r"\b([a-z]+[A-Z][A-Za-z]*)=", tpl))
    unknown = sorted(seen - set(CAMEL_TO_SVG) - CAMEL_KEEP)
    if unknown:
        raise SystemExit(
            "student_template.py: %s carries camelCase attribute(s) this "
            "compiler has no ruling for: %s.\n"
            "  Add each to CAMEL_TO_SVG (if SVG spells it with a hyphen) or to "
            "CAMEL_KEEP (if SVG spells it in camelCase). Guessing is not "
            "available: lowercasing a hyphenated one makes it inert and the "
            "page still renders, just wrong."
            % (where, ", ".join(unknown)))
    for camel, svg in CAMEL_TO_SVG.items():
        tpl = re.sub(r"\b%s=" % camel, "%s=" % svg, tpl)
    return tpl, sorted(seen & set(CAMEL_TO_SVG))


def template_and_logic(path):
    """Split a `.dc.html` into (template markup, logic-class source)."""
    src = open(path, encoding="utf-8").read()
    # ⚠️ THE TEMPLATE STARTS AT `<helmet>`, NOT AFTER IT, and the reason is
    # arithmetic. `support.js` compiles the whole component source and stamps
    # `data-dc-tpl` in document order from zero, so the helmet's nine element
    # nodes — one `<helmet>`, six `<link>`, one `<script>`, one `<style>` —
    # consume indices 0..8 before the design root is reached.
    #
    # Starting after `</helmet>` was the first attempt and it put every index
    # NINE LOW: the brand's `x-import` compiled to 4 where Design's rendered
    # DOM carries 13. That is not a cosmetic difference. `student_switches.json`
    # is keyed on Design's indices, the breakpoint table is looked up by them,
    # and the parity gate compares them — so a nine-off template would have
    # applied every switch to the wrong element while still rendering a page
    # that looked broadly right.
    #
    # The helmet is not RENDERED into the page; the runtime skips it and the
    # build turns its `<link>` list into real stylesheet links. It is parsed so
    # that the numbering matches.
    a = src.index("<helmet")
    m = re.search(r'<script[^>]*data-dc-script[^>]*>', src)
    if not m:
        raise SystemExit(
            "student_template.py: %s has no `<script data-dc-script>`. That "
            "tag is where Design's logic class lives and without it there is "
            "nothing to port." % path)
    tpl = src[a:m.start()]
    logic = src[m.end():]
    logic = logic[:logic.rindex("</script>")]
    return tpl.strip(), logic.strip()


# The rendered markup of every `x-import`, captured from Design's own
# standalone rather than retyped. There is exactly one on each page —
# `MrBadmusDS.BrandMark`, the student-surface brand ruled on 20 Aug 2026 — and
# hand-copying an SVG is precisely the kind of small transcription that goes
# wrong quietly and is then defended as "it looks the same".
STANDALONE = {
    "class view": "standalone/MrBadmusAI Class View.html",
    "assignment": "standalone/MrBadmusAI Assignment.html",
}

_IMPORT_JS = r"""
(function () {
  var r = document.querySelector('.rd[data-mode="ks3"]');
  if (!r) { return JSON.stringify({error: 'no design root'}); }
  var out = {};
  var hosts = r.querySelectorAll('.sc-host-x');
  for (var i = 0; i < hosts.length; i++) {
    out[String(hosts[i].getAttribute('data-dc-tpl'))] = hosts[i].innerHTML;
  }
  return JSON.stringify({error: '', hosts: out});
})()
"""


def capture_imports(cdp, spec, roots):
    """{componentName: rendered innerHTML} for every x-import in the template."""
    wanted = {}

    def walk(n):
        if isinstance(n, dict):
            if n.get("t") == "import":
                wanted[str(n.get("i"))] = n.get("from")
            for c in n.get("c") or []:
                walk(c)

    for r in roots:
        walk(r)
    if not wanted:
        return {}

    server, port = cdp.serve(spec.get("ref", REF))
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(1460, 1200)
            standalone = spec.get("standalone") or STANDALONE[spec["page"]]
            page.goto("http://127.0.0.1:%d/%s"
                      % (port, standalone.replace(" ", "%20")))
            import time
            time.sleep(2.5)
            got = json.loads(page.eval(_IMPORT_JS))
    finally:
        server.shutdown()
    if got.get("error"):
        raise SystemExit("student_template.py: %s" % got["error"])

    hosts = got.get("hosts") or {}

    out, missing = {}, []
    for tpl_i, name in sorted(wanted.items()):
        html = hosts.get(tpl_i)
        if not html:
            missing.append("%s (data-dc-tpl=%s)" % (name, tpl_i))
        else:
            out[name] = html

    # ⊕ 22 Aug 2026 — THE STANDALONE DOES NOT ALWAYS NUMBER LIKE THE SOURCE.
    #
    # Design's class-view amendments compiled cleanly and then failed here:
    # the template puts the brand's `x-import` at 13, the delivered standalone
    # renders it at 12. Neither is wrong. The standalone is a BUNDLE — it
    # inlines the design system, so its helmet no longer carries the
    # `<script src="_ds_bundle.js">` node that the source's does, and every
    # index after the helmet shifts down by one.
    #
    # Index equality was never the property being relied on. This function
    # wants ONE THING from the standalone: the rendered innerHTML of an
    # `x-import`, because hand-copying an SVG is the kind of transcription
    # that goes wrong quietly. The index is a convenience for finding it.
    #
    # So when every index misses and the two sides carry the SAME NUMBER of
    # hosts, they are matched in document order instead — and the fallback
    # says so on stdout every time it fires. A silent positional match is
    # precisely the thing that would map the wrong SVG into the brand slot on
    # some future page with two imports and never mention it.
    if missing and not out and len(wanted) == len(hosts):
        by_order = [hosts[k] for k in sorted(hosts, key=int)]
        names = [wanted[k] for k in sorted(wanted, key=int)]
        print("                 ⚠️  standalone numbering is offset from the "
              "source (template %s vs standalone %s); matched the %d "
              "x-import(s) in document order instead"
              % (sorted(wanted, key=int), sorted(hosts, key=int), len(names)))
        out = dict(zip(names, by_order))
        missing = [n for n, h in zip(names, by_order) if not h]

    if missing:
        raise SystemExit(
            "student_template.py: %s — could not capture the rendered markup "
            "of %s from Design's standalone. An x-import that renders nothing "
            "would leave a hole on the page where the brand goes, and it would "
            "look like a styling problem."
            % (spec["page"], ", ".join(missing)))
    return out


def compile_page(cdp, spec):
    ref = spec.get("ref", REF)
    path = os.path.join(ref, spec["src"])
    if not os.path.exists(path):
        raise SystemExit("student_template.py: missing %s" % path)
    tpl, logic = template_and_logic(path)
    tpl, kebabbed = kebab_svg_attrs(tpl, spec["src"])
    tpl, logic, fb_split = split_feedback_edge(tpl, logic, spec["page"])

    server, port = cdp.serve(ref)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.goto("http://127.0.0.1:%d/%s"
                      % (port, spec["src"].replace(" ", "%20")))
            got = json.loads(page.eval(_COMPILE_JS % json.dumps(tpl)))
    finally:
        server.shutdown()

    # ⚠️ THE ONE REACT CALL IN 492 LINES. `React.createRef()` is used for the
    # root ref and nothing else; the runtime provides the same two-line object.
    # Rewritten here rather than in the runtime so that what ships is plain
    # JavaScript a reader can follow without knowing what React is.
    n_ref = logic.count("React.createRef()")
    logic = logic.replace("React.createRef()", "MrbRef()")
    if "React." in logic:
        leftover = sorted(set(re.findall(r"React\.\w+", logic)))
        raise SystemExit(
            "student_template.py: %s still references React after the "
            "createRef rewrite: %s. The port ships no React, so every one of "
            "these needs a runtime equivalent before this can be trusted."
            % (spec["page"], ", ".join(leftover)))

    imports = capture_imports(cdp, spec, got["roots"])

    # The stylesheets Design's own page links, in Design's own order. The
    # snapshot inlined all six (223 KB, 40% of the page, once per page); the
    # port links them, so the browser caches one copy across both.
    sheets = re.findall(r'<link[^>]*href="([^"]+)"', tpl)

    return dict(nodes=got["n"], roots=got["roots"], logic=logic,
                imports=imports, sheets=sheets, fbSplit=fb_split,
                refs=n_ref, tplChars=len(tpl), logicChars=len(logic),
                kebabbed=kebabbed)


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ks3_browser as cdp

    check = "--check" in sys.argv
    print("\n🧩  student_template — Design's template compiled, "
          "Design's logic extracted\n")
    out = {}
    for spec in PAGES:
        got = compile_page(cdp, spec)
        out[spec["page"]] = got
        print("     %-11s %4d template node(s) · %6d chars of markup · "
              "%6d chars of logic · %d React.createRef rewritten"
              % (spec["page"], got["nodes"], got["tplChars"],
                 got["logicChars"], got["refs"]))
        print("                 SVG attributes rewritten to their SVG names: %s"
              % (", ".join(got["kebabbed"]) or "none"))
        print("                 x-import(s) captured from Design's render: %s"
              % (", ".join(sorted(got["imports"])) or "none"))
        print("                 stylesheet(s) Design links: %d" % len(got["sheets"]))
        if got["fbSplit"]:
            print("                 ⊕ RULED: the recall CORRECT label split off "
                  "`fbEdge` onto --ks3-ok-dark (graphic-only ruling)")

    blob = json.dumps(out, indent=1, sort_keys=True) + "\n"
    if check:
        if not os.path.exists(OUT):
            print("\n  FAIL  %s does not exist." % OUT)
            return 1
        if open(OUT, encoding="utf-8").read() != blob:
            print("\n  FAIL  the compiled template differs from %s. Design's "
                  "delivery moved, or the compiler did. Re-run without "
                  "--check to adopt it, and read the diff first." % OUT)
            return 1
        print("\n  PASS  the compiled template matches %s exactly." % OUT)
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(blob)
    print("\n     → %s\n" % OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
