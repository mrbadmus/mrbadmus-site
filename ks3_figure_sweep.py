"""ks3_figure_sweep.py — every drawn figure, driven at three real widths.

⊕ MRB-254. The figure set went from four drawings to eighteen in one pass, at
five different widths (760, 860, 900 user units) against a stylesheet whose
`min-width` was a single number measured off the only width that existed. That
is a class of defect no existing gate could see:

  · `ks3_parity.py` measures COMPUTED STYLE against Design's table. A figure
    whose labels have been scaled to 10px still has the right font-size in the
    stylesheet — the shrinking happens in the SVG's own coordinate system, and
    computed style never learns about it.
  · `verify_ks3.py` sweeps the SERVED BYTES. A `<text font-size="15">` inside a
    viewBox scaled to 78% is 11.7px on screen and 15 in the file.
  · `ks3_smoke.py` drives interaction. A figure has none.

So this measures the RENDERED GEOMETRY, in a real browser, at a real device
width, on every page that carries a drawn figure — which is the only place the
question "can a twelve-year-old read this label on their phone" is actually
answerable.

Five assertions per figure per width:

  1. THE SCROLL CONTAINER IS THERE AND IS FOCUSABLE. `.ks3-figure-scroll` with
     `tabindex="0"`, `role="group"` and an `aria-label` ending "— scrollable
     diagram". WCAG 2.1.1: a scroll region only a finger can reach cannot be
     reached from a keyboard, and the audit found this treatment correct on the
     four figures that predate this set.
  2. NOTHING IS CLIPPED. Every drawn element's bounding box lies inside the
     viewBox. SVG does not warn when a shape leaves the box — it draws outside
     and is silently cut, which is how `3 · MICROVILLI ON EVERY CELL` shipped
     four units past the edge with its last letter gone, and how this figure
     set's own axis captions rendered as "bits counted" and "Foxes cou".
  3. NO LABEL BELOW 13px ON SCREEN. Measured after the viewBox scale, not from
     the attribute. This is the assertion `min-width` exists to satisfy and the
     one that silently failed while the stylesheet said 700 and the drawings
     were 900.
  4. NO PAGE-LEVEL HORIZONTAL SCROLL. MRB-229's rule. A figure that scrolls
     sideways INSIDE its own box is the treatment; a figure that makes the
     whole document scroll sideways is the defect it is there to prevent.
  5. THE EDGE CUE AGREES WITH THE OVERFLOW. `.is-overflowing` is set by
     `wireFigureCues()` from `scrollWidth > clientWidth`, so the fade is on
     exactly when the figure continues off the edge. Both directions, because
     a cue that is always there says nothing.
"""

import os
import sys
import functools
import http.server
import socketserver
import threading

import ks3_browser
import ks3_data

WIDTHS = (390, 768, 1440)
MIN_LABEL_PX = 13.0

PROBE = r"""
new Promise(function (res) {
  requestAnimationFrame(function () { requestAnimationFrame(function () {
    var out = {figures: [], docOverflow:
      document.documentElement.scrollWidth - document.documentElement.clientWidth};
    var boxes = document.querySelectorAll('.ks3-figure-scroll');
    for (var i = 0; i < boxes.length; i++) {
      var box = boxes[i];
      var svg = box.querySelector('svg.ks3-figure-svg');
      if (!svg) { out.figures.push({id: null}); continue; }
      var vb = svg.viewBox.baseVal;
      var rect = svg.getBoundingClientRect();
      /* the scale the viewBox is actually rendered at */
      var k = vb.width ? rect.width / vb.width : 0;
      var cs = getComputedStyle(box);
      var small = [], clipped = [];
      var texts = svg.querySelectorAll('text');
      for (var t = 0; t < texts.length; t++) {
        var px = parseFloat(getComputedStyle(texts[t]).fontSize) * k;
        if (px < %(minpx)s - 0.05) {
          small.push({s: texts[t].textContent.slice(0, 40),
                      declared: getComputedStyle(texts[t]).fontSize,
                      onScreen: Math.round(px * 100) / 100});
        }
      }
      /* clipping, in the SVG's own units — getBBox is untransformed */
      var drawn = svg.querySelectorAll('path,rect,circle,ellipse,line,text');
      for (var d = 0; d < drawn.length; d++) {
        var b;
        try { b = drawn[d].getBBox(); } catch (e) { continue; }
        if (!b || (!b.width && !b.height)) { continue; }
        if (b.x < vb.x - 0.6 || b.y < vb.y - 0.6 ||
            b.x + b.width > vb.x + vb.width + 0.6 ||
            b.y + b.height > vb.y + vb.height + 0.6) {
          clipped.push({tag: drawn[d].tagName,
                        s: (drawn[d].textContent || '').slice(0, 40),
                        x: Math.round(b.x * 10) / 10,
                        y: Math.round(b.y * 10) / 10,
                        r: Math.round((b.x + b.width) * 10) / 10,
                        bt: Math.round((b.y + b.height) * 10) / 10});
        }
      }
      /* ── 6 · does a line run through a word? ──────────────────────────
         The one defect class these plates keep producing, because a leader
         and the label it leads to are authored as two independent
         coordinates: the villus port shipped three crossing arrows drawn
         straight through "glucose", "amino acids" and "fatty acids", and it
         was only found by looking. A struck-through label is not a small
         blemish — it is the label the figure exists to attach to a shape,
         made unreadable by the mark that attaches it.

         Thin strokes only (≤2.2 units): those are leaders, dimension lines
         and dashed links, and they are the ones that are placed relative to
         a shape rather than to the text. A thick stroke crossing a label is
         usually the drawing itself and is Design's composition.

         Sampled along the stroke rather than compared bbox-to-bbox, because
         a long diagonal leader's bounding box covers a great deal of paper it
         never touches. The text box is inset 2.5 units vertically before
         testing, so a leader that merely grazes the ascender line — which is
         how most of them are deliberately drawn — is not a hit. */
      var words = [];
      for (var q = 0; q < texts.length; q++) {
        var tb;
        try { tb = texts[q].getBBox(); } catch (e) { continue; }
        if (!tb || !tb.width) { continue; }
        var str = (texts[q].textContent || '').trim();
        if (!str) { continue; }
        words.push({x: tb.x, y: tb.y + 2.5, r: tb.x + tb.width,
                    b: tb.y + tb.height - 2.5, s: str.slice(0, 40)});
      }
      var struck = [], strokes = svg.querySelectorAll('path,line');
      for (var p = 0; p < strokes.length; p++) {
        var el = strokes[p];
        var sw = parseFloat(el.getAttribute('stroke-width') || '1');
        if (!(sw <= 2.2)) { continue; }
        var pts = [], L;
        if (el.tagName === 'line') {
          var ax = parseFloat(el.getAttribute('x1')),
              ay = parseFloat(el.getAttribute('y1')),
              bx2 = parseFloat(el.getAttribute('x2')),
              by2 = parseFloat(el.getAttribute('y2'));
          for (var t2 = 0; t2 <= 40; t2++) {
            pts.push({x: ax + (bx2 - ax) * t2 / 40,
                      y: ay + (by2 - ay) * t2 / 40});
          }
        } else {
          try { L = el.getTotalLength(); } catch (e) { continue; }
          if (!L) { continue; }
          for (var t3 = 0; t3 <= 40; t3++) {
            pts.push(el.getPointAtLength(L * t3 / 40));
          }
        }
        for (var w2 = 0; w2 < words.length; w2++) {
          var word = words[w2], hits2 = [];
          for (var k2 = 0; k2 < pts.length; k2++) {
            if (pts[k2].x > word.x && pts[k2].x < word.r &&
                pts[k2].y > word.y && pts[k2].y < word.b) { hits2.push(k2); }
          }
          if (hits2.length < 3) { continue; }
          /* ⚠️ A LEADER THAT ENDS AT ITS LABEL IS NOT A DEFECT, and the first
             version of this check reported sixteen figures because it could
             not tell the two apart. A leader necessarily enters the box of
             the thing it points at; that is what pointing IS. What is a
             defect is a stroke that goes IN ONE SIDE AND OUT THE OTHER —
             a strikethrough — or one that lies wholly inside the word, which
             is the same thing seen from closer up.

             So: flag only if the inside run touches NEITHER end of the
             sampled stroke (a traverse), or if every sample is inside it. */
          var first = hits2[0], last2 = hits2[hits2.length - 1];
          var traverse = (first > 0 && last2 < pts.length - 1);
          var wholly = (hits2.length === pts.length);
          if (traverse || wholly) {
            struck.push({s: word.s, tag: el.tagName, w: sw,
                         n: hits2.length,
                         how: wholly ? 'lies wholly inside' : 'crosses'});
          }
        }
      }

      out.figures.push({
        struck: struck,
        id: svg.getAttribute('aria-labelledby'),
        vbw: vb.width, vbh: vb.height,
        scale: Math.round(k * 1000) / 1000,
        tabindex: box.getAttribute('tabindex'),
        role: box.getAttribute('role'),
        label: box.getAttribute('aria-label'),
        overflow: box.scrollWidth - box.clientWidth,
        cued: box.classList.contains('is-overflowing'),
        mask: (cs.maskImage || cs.webkitMaskImage || 'none'),
        small: small, clipped: clipped, nText: texts.length});
    }
    res(out);
  }); });
})
""" % {"minpx": MIN_LABEL_PX}


def figure_pages(units):
    """Every built page carrying at least one `drawn` figure."""
    seen = []
    for u in units:
        for l in u["lessons"]:
            drawn = [f for f in (l.get("figures") or [])
                     if f.get("status") == "drawn"]
            refs = {b.get("ref") for b in (l.get("core") or [])
                    if isinstance(b, dict) and b.get("type") == "figure"}
            shown = [f for f in drawn if f["id"] in refs]
            if shown:
                seen.append(("%s/%s/%s.html" % (u["discipline"], u["slug"],
                                                l["slug"]),
                             [f["id"] for f in shown]))
    return sorted(seen)


def sweep(site_root="mrbadmus_site", prefix="ks3", widths=WIDTHS):
    """⚠️ SERVED FROM THE SITE ROOT, NOT FROM `ks3/`.

    A KS3 page links its stylesheet as `/shared/ks3.css`, absolute from the
    SITE root. Serving `mrbadmus_site/ks3` as `/` makes every one of those a
    404 — no tokens, no `ks3.css`, no `ks3.js` — and the sweep then measures an
    unstyled document: no `min-width`, no scroll box, no `wireFigureCues`, and
    every label at the browser default. It does not error. It reports whatever
    a naked SVG happens to do, and on the first run it reported nothing at all
    wrong, which is the most dangerous answer a gate can give.
    """
    ks3_root = os.path.join(site_root, prefix)
    units = ks3_data.build_units()
    pages = figure_pages(units)
    problems, rows = [], []

    handler = functools.partial(http.server.SimpleHTTPRequestHandler,
                                directory=site_root)
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    try:
        with ks3_browser.Browser() as b:
            for rel, ids in pages:
                if not os.path.exists(os.path.join(ks3_root, rel)):
                    problems.append(
                        "FIGURE SWEEP: /%s declares %s and is not in the built "
                        "tree, so nothing about it was measured."
                        % (rel, ", ".join(ids)))
                    continue
                for w in widths:
                    page = b.page("http://127.0.0.1:%d/%s/%s"
                                  % (port, prefix, rel))
                    page.set_viewport(w, 900)
                    got = page.eval(PROBE)
                    logs = [m for m in (page.console_errors()
                                        if hasattr(page, "console_errors")
                                        else [])]
                    figs = got["figures"]
                    if len(figs) != len(ids):
                        problems.append(
                            "FIGURE SWEEP: /%s at %dpx renders %d figure(s) "
                            "for %d declared and placed. A figure block whose "
                            "drawer emitted nothing leaves no trace on the "
                            "page — which is the hole `status: drawn` exists "
                            "to close."
                            % (rel, w, len(figs), len(ids)))
                    for f in figs:
                        # ⚠️ `aria-labelledby` is "<id>-t <id>-d", and
                        # `.split("-t")[0]` cuts at the FIRST "-t" anywhere in
                        # the string — so `b5-pollen-tube-t` came out as
                        # `b5-pollen`, and every problem this gate reported
                        # about that figure named a figure that does not
                        # exist. A gate whose message sends the reader to the
                        # wrong file is worse than one that says nothing.
                        fid = (f.get("id") or "?").split()[0]
                        if fid.endswith("-t"):
                            fid = fid[:-2]
                        if f.get("id") is None:
                            problems.append(
                                "FIGURE SWEEP: /%s at %dpx has a scroll "
                                "container with no `svg.ks3-figure-svg` in it."
                                % (rel, w))
                            continue
                        if f["tabindex"] != "0" or f["role"] != "group":
                            problems.append(
                                "FIGURE SWEEP: /%s (%s) at %dpx — the scroll "
                                "box is tabindex=%r role=%r. A scrollable "
                                "region only a finger can reach is unreachable "
                                "from a keyboard (WCAG 2.1.1)."
                                % (rel, fid, w, f["tabindex"], f["role"]))
                        if not (f["label"] or "").endswith(
                                "— scrollable diagram"):
                            problems.append(
                                "FIGURE SWEEP: /%s (%s) at %dpx — the scroll "
                                "box announces %r. It must end \"— scrollable "
                                "diagram\", or the focus stop arrives with no "
                                "hint that it moves."
                                % (rel, fid, w, f["label"]))
                        for s in f["small"]:
                            problems.append(
                                "FIGURE SWEEP: /%s (%s) at %dpx — %r is "
                                "declared %s and lands at %.2fpx on screen "
                                "(viewBox scaled to %.0f%%). The floor is "
                                "%gpx; below it the label has stopped being a "
                                "label, which is what the scroll container "
                                "exists to prevent."
                                % (rel, fid, w, s["s"], s["declared"],
                                   s["onScreen"], f["scale"] * 100,
                                   MIN_LABEL_PX))
                        for st in f.get("struck") or []:
                            problems.append(
                                "FIGURE SWEEP: /%s (%s) at %dpx — a <%s> "
                                "stroked %s %s the label %r (%d of the "
                                "sampled points). A leader that ENDS at its "
                                "label is pointing; one that crosses it, or "
                                "lies inside it, is a strikethrough through "
                                "the word the figure exists to attach."
                                % (rel, fid, w, st["tag"], st["w"],
                                   st.get("how", "crosses"), st["s"],
                                   st["n"]))
                        for c in f["clipped"]:
                            problems.append(
                                "FIGURE SWEEP: /%s (%s) at %dpx — a <%s> %sruns "
                                "from (%s, %s) to (%s, %s), outside the %g×%g "
                                "viewBox. SVG draws outside the box and is "
                                "silently cut; nothing warns."
                                % (rel, fid, w, c["tag"],
                                   ("carrying %r " % c["s"]) if c["s"] else "",
                                   c["x"], c["y"], c["r"], c["bt"],
                                   f["vbw"], f["vbh"]))
                        # The cue, both directions.
                        over = f["overflow"] > 1
                        if over and not f["cued"]:
                            problems.append(
                                "FIGURE SWEEP: /%s (%s) at %dpx hides %dpx of "
                                "the drawing and carries no edge cue. The "
                                "visible window can end exactly at a panel "
                                "boundary, and it then reads as a complete "
                                "diagram (audit 3.9)."
                                % (rel, fid, w, f["overflow"]))
                        if not over and f["cued"]:
                            problems.append(
                                "FIGURE SWEEP: /%s (%s) at %dpx draws the edge "
                                "cue where the figure fits. A cue that is "
                                "always there says nothing."
                                % (rel, fid, w, ))
                        rows.append((rel, fid, w, f["scale"], f["overflow"],
                                     f["nText"]))
                    if got["docOverflow"] > 0:
                        problems.append(
                            "FIGURE SWEEP: /%s at %dpx scrolls the whole "
                            "DOCUMENT sideways by %dpx. A figure scrolling "
                            "inside its own box is the treatment; the page "
                            "scrolling is the defect it exists to prevent "
                            "(MRB-229)."
                            % (rel, w, got["docOverflow"]))
                    for m in logs:
                        problems.append(
                            "FIGURE SWEEP: /%s at %dpx logged a console error: "
                            "%s" % (rel, w, m))
    finally:
        srv.shutdown()
    return problems, rows, pages


def main():
    problems, rows, pages = sweep()
    print("KS3 figure sweep — %d page(s), %d width(s), %d measurement(s)"
          % (len(pages), len(WIDTHS), len(rows)))
    for rel, fid, w, k, over, n in rows:
        print("  %-58s %5dpx  scale %-6s overflow %-5d %2d labels"
              % (fid, w, k, over, n))
    if problems:
        print("\n%d problem(s):" % len(problems))
        for p in problems:
            print("  ·", p)
        return 1
    print("\n✅ every drawn figure reads at 390, 768 and 1440")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
