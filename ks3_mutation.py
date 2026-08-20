#!/usr/bin/env python3
"""ks3_mutation.py — source-level mutation testing for the KS3 parity assertions.

WHY THIS EXISTS
---------------
`ks3_parity.py` asserts that a named component resolves a named value. A green
row proves the value is *there*. It does NOT prove the assertion is attached to
the declaration the row is named after — and those are different claims.

The failure mode is quiet and total. A row called "tasting bench WHY line is
band-on-ink" measures `.ks3-tbench-why { color }` and passes. But if the only
rule in `shared/ks3.css` that ever set that colour is `.ks3-dark p { color:
… }`, then repainting `.ks3-tbench-why` to hot pink would not fail the gate,
because there is no `.ks3-tbench-why` colour declaration to repaint — the row
is watching a component it does not actually cover. It reads as a gate and
behaves as a comment. `_HAIRLINE_PX` in `ks3_parity.py` exists because exactly
this was found once by hand, on a border.

`mutation_test_correct_state()` in `ks3_parity.py` already mutation-tests one
state, but it mutates the RENDERED PAGE — it injects a `!important` override on
top of everything. That is the right bar for the question it asks ("can these
assertions see the MRB-202 defect at all?"), and it is a weaker bar than this
one: an injected override moves the value no matter which rule supplied it, so
it can never tell you that the supplying rule was the wrong one.

⊕ NEW, 16 Aug 2026 (MRB-228). This harness mutates the SOURCE instead. For each
asserted (selector, property) it finds, through the CSSOM, the shipped
declaration(s) that actually supply the value — on the element, or on the
ancestor the value is inherited from — breaks THAT declaration to a sentinel,
re-reads, and asks whether the assertion notices. If the assertion still passes
with its own supplying declaration destroyed, the assertion is DEAD: whatever
it is testing, it is not testing what its name says.

The most valuable output is not the verdict column. It is the supplying-selector
column, which answers "what is actually holding this value up?" for every row in
the unit — and flags every row named after a scoped class whose value in fact
arrives from a broad rule.

WHAT IT WILL NOT TELL YOU
-------------------------
A LIVE verdict means the assertion is wired to a real declaration. It does not
mean the assertion is *well chosen*, and it does not mean the declaration is on
the right selector — a row supplied by a broad rule can still be LIVE (breaking
`.ks3-dark p` does move `.ks3-tbench-why`). That is precisely why the broad-rule
flag is printed for LIVE rows too, and why it is worth reading even when the
run exits 0.

USAGE
-----
    python3 ks3_mutation.py            # default unit: B3
    python3 ks3_mutation.py B3 C1
    python3 ks3_mutation.py B3 --ks3-root mrbadmus_site/ks3

Exit 1 if any assertion is DEAD (or has no shipped source at all), 0 otherwise.
Exit 2 if the harness itself could not be trusted — a failed restore, a page
that would not load, a stylesheet that did not apply.

Nothing here is copied from `ks3_parity.py`. `COMPONENTS`, `DRIVES`,
`_JS_HELPERS`, `_JS_SETTLE`, `same_colour` and `close_length` are imported, so
this harness cannot drift away from the gate it is auditing.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import OrderedDict

import ks3_browser
from ks3_parity import (
    COMPONENTS,
    DRIVES,
    _JS_HELPERS,
    _JS_SETTLE,
    close_length,
    same_colour,
)


# ── which pages belong to a unit ──────────────────────────────────────────
#
# The unit boundary is not recorded anywhere as data — it lives in the
# page-path constants at the top of `ks3_parity.py` (`B3_DIET`, `B3_GUT`, …),
# which all sit in one directory per unit. Deriving the directory from those
# constants means a unit gaining a lesson is picked up automatically, and a
# unit this harness has never heard of works on the day it is registered.

def unit_dirs(unit: str) -> list[str]:
    """Directory prefixes owned by `unit`, read off ks3_parity's own constants."""
    import ks3_parity

    dirs = []
    for name in dir(ks3_parity):
        if not name.startswith(unit.upper() + "_"):
            continue
        value = getattr(ks3_parity, name)
        if not isinstance(value, str) or not value.endswith(".html"):
            continue
        d = os.path.dirname(value)
        if d and d not in dirs:
            dirs.append(d)
    return dirs


def rows_for_units(units: list[str]) -> tuple[list[dict], list[str]]:
    """The COMPONENTS rows belonging to these units, plus the dirs matched."""
    dirs: list[str] = []
    for u in units:
        for d in unit_dirs(u):
            if d not in dirs:
                dirs.append(d)
    if not dirs:
        return ([], [])
    rows = [c for c in COMPONENTS
            if any(c["on"].startswith(d + "/") for d in dirs)]
    return (rows, dirs)


# ── sentinels ─────────────────────────────────────────────────────────────
#
# A sentinel has one job: be a value the assertion must reject. It is chosen
# per property rather than globally because `font-weight: rgb(1,2,3)` is not a
# broken declaration, it is an ignored one — and an ignored declaration leaves
# the computed value exactly where it was, which would report every weight
# assertion as DEAD for a reason that has nothing to do with the assertion.

_SENTINEL_COLOUR = "rgb(1, 2, 3)"
_SENTINEL_FONT = '"MutantSentinelFace"'
_SENTINEL_LENGTH = "97px"
_SENTINEL_LENGTH_ALT = "43px"


def sentinel_for(prop: str, want: str) -> str:
    """A clearly-different, syntactically VALID value for `prop`."""
    w = (want or "").strip().lower()

    if prop == "font-family":
        return _SENTINEL_FONT
    if want.startswith("#"):
        return _SENTINEL_COLOUR
    if w.endswith("px") and " " not in w:
        return _SENTINEL_LENGTH if w != _SENTINEL_LENGTH else _SENTINEL_LENGTH_ALT
    if prop == "font-weight":
        return "333" if w != "333" else "444"
    if prop == "opacity":
        return "0.13" if w != "0.13" else "0.29"
    if prop == "text-transform":
        return "lowercase" if w != "lowercase" else "capitalize"
    if prop == "box-shadow":
        return "rgb(1, 2, 3) 41px 41px 0px 0px"
    if prop in ("line-height", "letter-spacing"):
        return _SENTINEL_LENGTH
    if prop in ("display", "position", "text-align", "flex-direction",
                "justify-content", "align-items", "white-space", "overflow"):
        # Enumerated keywords: `revert` walks the declaration back to the UA
        # sheet, which is a genuine break of the shipped rule whatever the
        # keyword happened to be.
        return "revert"
    # Anything unanticipated. `revert` is the honest general answer — it undoes
    # author styling for that property on that declaration — and the sentinel
    # is printed in the detail block so a reader can judge it.
    return "revert"


# ── the comparison, mirrored exactly from run_browser_layers().measure_c ──
#
# Mirrored, not approximated. If this harness compared more loosely than the
# gate it would report DEAD rows that the gate would actually catch; if it
# compared more tightly it would report LIVE rows the gate would sleep through.
# Either way the output would be about this file rather than about the gate.

def gate_ok(prop: str, want: str, got: str) -> bool:
    if prop == "font-family":
        return want.lower() in (got or "").lower()
    if want.startswith("#"):
        return bool(same_colour(got, want))
    if want.endswith("px") and " " not in want.strip():
        return bool(close_length(got, want))
    return (got or "").lower() == want.lower()


# ── the browser-side source locator ───────────────────────────────────────
#
# Everything below runs in the page. It has to: only the CSSOM knows which of
# the ~1400 rules in `shared/ks3.css` the element matches, and only the CSSOM
# can edit one in place and put it back.
#
# Three things it must handle that a naive walk gets wrong:
#
#   1. Grouping rules. `@media`, `@supports`, `@layer` and `@container` hold
#      their own `cssRules`, and KS3's responsive work lives inside them. A
#      walk that only reads top-level rules would report "no source" for any
#      property whose only declaration is inside a media query.
#   2. Shorthands carrying a variable. `background: var(--ks3-band)` cannot be
#      expanded by the CSSOM, so `getPropertyValue('background-color')` on that
#      rule returns "" — the declaration is invisible to a longhand lookup even
#      though it is the one supplying the colour. So each longhand also asks
#      its shorthands, and mutation appends the longhand (which wins, being
#      later in the same block) rather than trying to rewrite the shorthand.
#   3. Inline styles. KS3 pages carry hundreds, and `ks3.js` writes more at
#      runtime, so an element's own `style` attribute is a first-class source.
#
# Restore is by whole-declaration `cssText` rather than by property. Removing a
# longhand that was never declared as a longhand (case 2) is not well-defined
# across engines; putting the entire block back verbatim is.

_JS_MUTATOR = r"""
window.__ks3mut = (function () {

  var SHORTHANDS = {
    "background-color": ["background"],
    "background-image": ["background"],
    "border-top-color": ["border-top", "border-color", "border"],
    "border-right-color": ["border-right", "border-color", "border"],
    "border-bottom-color": ["border-bottom", "border-color", "border"],
    "border-left-color": ["border-left", "border-color", "border"],
    "border-top-width": ["border-top", "border-width", "border"],
    "border-bottom-width": ["border-bottom", "border-width", "border"],
    "border-top-style": ["border-top", "border-style", "border"],
    "border-top-left-radius": ["border-radius"],
    "border-top-right-radius": ["border-radius"],
    "border-bottom-left-radius": ["border-radius"],
    "border-bottom-right-radius": ["border-radius"],
    "font-size": ["font"],
    "font-family": ["font"],
    "font-weight": ["font"],
    "line-height": ["font"],
    "padding-top": ["padding"],
    "padding-bottom": ["padding"],
    "padding-left": ["padding"],
    "padding-right": ["padding"],
    "margin-top": ["margin"],
    "margin-bottom": ["margin"],
    "gap": ["gap"],
    "row-gap": ["gap"],
    "column-gap": ["gap"]
  };

  // ⊕ A computed style is a USED value, and a used value can be supplied by a
  // property that is not the one being asserted. `.ks3-tbench-tube` declares
  // `flex: 0 0 62px` and never declares `width` at all, yet
  // getComputedStyle().width reads 62px because that is what layout resolved.
  // Looking only for `width` declarations reports "nothing supplies this",
  // which would brand a perfectly live assertion DEAD and send someone off to
  // fix a gate that is working. So each asserted property also knows the
  // properties that can stand in for it, and the mutation breaks THAT one.
  var SUPPLIERS = {
    "width": ["flex-basis", "inline-size"],
    "height": ["flex-basis", "block-size"],
    "min-height": ["min-block-size"],
    "min-width": ["min-inline-size"],
    "max-height": ["max-block-size"],
    "max-width": ["max-inline-size"]
  };

  function shorthandsFor(prop) { return SHORTHANDS[prop] || []; }
  function suppliersFor(prop) { return SUPPLIERS[prop] || []; }

  function describe(el) {
    if (!el) { return "?"; }
    var s = el.tagName ? el.tagName.toLowerCase() : "?";
    if (el.id) { s += "#" + el.id; }
    var cn = el.getAttribute ? (el.getAttribute("class") || "") : "";
    if (cn) { s += "." + cn.trim().split(/\s+/).join("."); }
    return s;
  }

  function elPath(el) {
    // Index path from documentElement down, by `children` position. Stable for
    // the life of one document, which is all we need: mutate and restore both
    // happen before the next navigation.
    var path = [];
    while (el && el.parentElement) {
      var kids = el.parentElement.children, i = 0;
      for (; i < kids.length; i++) { if (kids[i] === el) { break; } }
      path.unshift(i);
      el = el.parentElement;
    }
    return path;
  }

  function elAt(path) {
    var el = document.documentElement;
    for (var i = 0; i < path.length; i++) {
      if (!el) { return null; }
      el = el.children[path[i]];
    }
    return el || null;
  }

  function walk(rules, path, out) {
    for (var i = 0; i < rules.length; i++) {
      var r = rules[i], p = path.concat([i]);
      var kids = null;
      try { kids = r.cssRules; } catch (e) { kids = null; }
      if (r.selectorText && r.style) {
        out.push({ rule: r, path: p });
      } else if (kids && kids.length) {
        walk(kids, p, out);          // @media / @supports / @layer / @container
      }
    }
  }

  function sheets() {
    // Rebuilt per call rather than cached: `_JS_SETTLE` and any drive may have
    // appended a <style>, and a stale cache would hand back rule objects whose
    // recorded index path no longer resolves.
    var out = [], unreadable = 0;
    for (var s = 0; s < document.styleSheets.length; s++) {
      var sheet = document.styleSheets[s], rules = null;
      try { rules = sheet.cssRules; } catch (e) { unreadable++; continue; }
      if (!rules) { continue; }
      var flat = [];
      walk(rules, [], flat);
      for (var i = 0; i < flat.length; i++) {
        out.push({
          sheet: s,
          href: sheet.href || "(inline <style>)",
          path: flat[i].path,
          rule: flat[i].rule
        });
      }
    }
    return { rules: out, unreadable: unreadable };
  }

  function ruleAt(sheetIndex, path) {
    var sheet = document.styleSheets[sheetIndex];
    if (!sheet) { return null; }
    var list;
    try { list = sheet.cssRules; } catch (e) { return null; }
    var rule = null;
    for (var i = 0; i < path.length; i++) {
      if (!list || path[i] >= list.length) { return null; }
      rule = list[path[i]];
      try { list = rule.cssRules; } catch (e) { list = null; }
    }
    return rule || null;
  }

  function declares(decl, prop) {
    // Returns null, or { value, via, priority, target, supplier } where:
    //   via      — "" for a real longhand, else the shorthand or stand-in the
    //              declaration was found through (printed, so a reader can see
    //              what is really holding the value up)
    //   target   — the property the mutation must actually set. For a shorthand
    //              that is still the longhand (appending it to the same block
    //              wins, being later); for a stand-in it is the stand-in.
    //   supplier — true when the value comes from a different property entirely
    var v = decl.getPropertyValue(prop);
    if (v) {
      return { value: v, via: "", priority: decl.getPropertyPriority(prop),
               target: prop, supplier: false };
    }
    var sh = shorthandsFor(prop);
    for (var i = 0; i < sh.length; i++) {
      var sv = decl.getPropertyValue(sh[i]);
      if (sv) {
        return { value: sv, via: sh[i],
                 priority: decl.getPropertyPriority(sh[i]),
                 target: prop, supplier: false };
      }
    }
    var su = suppliersFor(prop);
    for (var j = 0; j < su.length; j++) {
      var uv = decl.getPropertyValue(su[j]);
      if (uv && uv !== "auto") {
        return { value: uv, via: su[j],
                 priority: decl.getPropertyPriority(su[j]),
                 target: su[j], supplier: true };
      }
    }
    return null;
  }

  function hitsOn(el, prop, all) {
    var hits = [];

    var inline = declares(el.style, prop);
    if (inline) {
      hits.push({
        kind: "inline",
        href: "(style attribute)",
        selectorText: "[style] on " + describe(el),
        ownerPath: elPath(el),
        value: inline.value,
        via: inline.via,
        target: inline.target,
        supplier: inline.supplier,
        priority: inline.priority
      });
    }

    for (var i = 0; i < all.length; i++) {
      var entry = all[i], m = false;
      try { m = el.matches(entry.rule.selectorText); } catch (e) { m = false; }
      if (!m) { continue; }
      var d = declares(entry.rule.style, prop);
      if (!d) { continue; }
      hits.push({
        kind: "rule",
        sheet: entry.sheet,
        path: entry.path,
        href: entry.href,
        selectorText: entry.rule.selectorText,
        value: d.value,
        via: d.via,
        target: d.target,
        supplier: d.supplier,
        priority: d.priority
      });
    }
    return hits;
  }

  return {
    find: function (sel, prop) {
      var el = document.querySelector(sel);
      if (!el) { return { source: "missing", hits: [] }; }
      var s = sheets();
      var node = el, level = 0;
      while (node) {
        var hits = hitsOn(node, prop, s.rules);
        if (hits.length) {
          return {
            source: level === 0 ? "self" : "ancestor",
            level: level,
            owner: describe(node),
            unreadable: s.unreadable,
            hits: hits
          };
        }
        node = node.parentElement;
        level++;
      }
      return { source: "none", unreadable: s.unreadable, hits: [] };
    },

    mutate: function (hits, prop, sentinel) {
      var saved = [];
      for (var i = 0; i < hits.length; i++) {
        var h = hits[i], decl = null;
        if (h.kind === "inline") {
          var e = elAt(h.ownerPath);
          if (!e) { return { error: "lost the inline-styled element" }; }
          decl = e.style;
        } else {
          var r = ruleAt(h.sheet, h.path);
          if (!r || !r.style) { return { error: "rule path no longer resolves" }; }
          decl = r.style;
        }
        saved.push(decl.cssText);
        // Keep whatever priority the shipped declaration had. Adding
        // !important where there was none could override a supplying rule this
        // walk failed to find, and would then report LIVE for the wrong reason.
        decl.setProperty(h.target || prop, sentinel, h.priority || "");
      }
      return { saved: saved };
    },

    restore: function (hits, saved) {
      for (var i = 0; i < hits.length; i++) {
        var h = hits[i], decl = null;
        if (h.kind === "inline") {
          var e = elAt(h.ownerPath);
          if (!e) { return { error: "lost the inline-styled element" }; }
          decl = e.style;
        } else {
          var r = ruleAt(h.sheet, h.path);
          if (!r || !r.style) { return { error: "rule path no longer resolves" }; }
          decl = r.style;
        }
        decl.cssText = saved[i];
      }
      return { error: "" };
    }
  };
})();
true
"""


# ── page plumbing ─────────────────────────────────────────────────────────

def load_page(browser, url, rel):
    """Load, install helpers, freeze transitions, and prove the stylesheet applied.

    The stylesheet check is the same one `run_browser_layers()` makes, for the
    same reason: served from the wrong root, every KS3 page loads with no CSS,
    and this harness would then report every assertion in the unit as
    source: none — a harness fault wearing the costume of ninety findings.
    """
    page = browser.page(url)
    page.eval(_JS_HELPERS + "true")
    page.eval(_JS_MUTATOR)
    # Contract gate 7: `.ks3-option` transitions background over 160ms, so a
    # read straight after a click (or straight after a mutation) returns the
    # colour it is leaving. Freeze first, always.
    page.eval(_JS_SETTLE)
    token = page.eval("getComputedStyle(document.body)"
                      ".getPropertyValue('--ks3-ground').trim()")
    if not token:
        raise SystemExit(
            "HARNESS FAULT: shared/ks3.css did not apply on /%s. Every "
            "measurement below would be meaningless, so none were taken." % rel)
    return page


def sel_leaf_class(sel: str) -> str:
    """The most specific class in a selector — what the row is named after."""
    classes = re.findall(r"\.([A-Za-z0-9_-]+)", sel or "")
    return classes[-1] if classes else ""


def classify_supply(sel: str, prop: str, found: dict) -> tuple[str, str]:
    """(label, note) describing WHERE the value came from, relative to the row.

    The interesting case is a row named for a scoped class whose value in fact
    arrives from a rule that does not mention that class at all. That row is
    not covering its component; it is covering whatever the broad rule covers,
    and the day someone gives the component its own declaration the row will
    keep passing while measuring the wrong thing.
    """
    leaf = sel_leaf_class(sel)
    hits = found.get("hits") or []
    if not hits:
        return ("NO-SOURCE", "nothing in any stylesheet declares it")

    mentions_leaf = leaf and any(("." + leaf) in (h.get("selectorText") or "")
                                for h in hits)
    if found.get("source") == "ancestor":
        if mentions_leaf:
            return ("INHERITED", "inherited from %s" % found.get("owner"))
        return ("SUPPLIED-BY-BROAD-RULE",
                "inherited from %s — no rule on the element itself declares it"
                % found.get("owner"))
    if leaf and not mentions_leaf:
        return ("SUPPLIED-BY-BROAD-RULE",
                "no rule mentioning .%s declares this property" % leaf)
    # The selector is right; the PROPERTY is a stand-in. Worth naming, because
    # anyone reading the row and then grepping the stylesheet for it will find
    # nothing and conclude the row is bogus.
    if hits and all(h.get("supplier") for h in hits):
        vias = sorted({h.get("via") for h in hits if h.get("via")})
        return ("SUPPLIED-BY-OTHER-PROPERTY",
                "no `%s` declaration exists; the used value comes from %s"
                % (prop, ", ".join(vias)))
    return ("SCOPED", "")


def short_href(href: str) -> str:
    if not href or href.startswith("("):
        return href or ""
    return href.rsplit("/", 1)[-1].split("?", 1)[0]


# ── the run ───────────────────────────────────────────────────────────────

def run(units: list[str], ks3_root: str) -> int:
    rows, dirs = rows_for_units(units)
    if not rows:
        print("No COMPONENTS rows found for unit(s) %s — nothing to mutate."
              % ", ".join(units))
        print("(unit is matched by the page-path constants in ks3_parity.py, "
              "e.g. B3_DIET -> biology/nutrition-and-digestion/)")
        return 1

    print("KS3 SOURCE-LEVEL MUTATION HARNESS")
    print("unit(s): %s" % ", ".join(units))
    for d in dirs:
        print("  pages under: %s/" % d)
    print("rows: %d" % len(rows))
    print()

    # Group by (page, drive): one document per combination, every row in it
    # mutated and restored in turn so no two mutations are ever live together.
    groups: "OrderedDict[tuple, list]" = OrderedDict()
    parked = []
    for spec in rows:
        if spec.get("parked"):
            parked.append(spec)
            continue
        groups.setdefault((spec["on"], spec.get("drive")), []).append(spec)

    served_root = os.path.dirname(os.path.abspath(ks3_root))
    prefix = os.path.basename(os.path.abspath(ks3_root))
    server, port = ks3_browser.serve(served_root)

    results = []   # (name, rel, drive, prop, want, label, supply, verdict, note)
    details = []
    control = None

    try:
        for (rel, drive), specs in groups.items():
            url = "http://127.0.0.1:%d/%s/%s" % (port, prefix, rel)

            # ⊕ A FRESH BROWSER PER PAGE/DRIVE, not a shared one. The KS3 canvas
            # loops keep running after the driver moves on; one shared Chrome
            # accumulates enough of them to drop the DevTools socket around the
            # twelfth page (mrb-220-build-contract §6). B3 alone is fourteen
            # combinations, which is well past that.
            browser = ks3_browser.Browser()
            try:
                browser.start()
                page = load_page(browser, url, rel)

                if drive:
                    err = page.eval(DRIVES[drive])
                    if err:
                        for spec in specs:
                            for prop, want in sorted(spec["props"].items()):
                                results.append((spec["name"], rel, drive, prop,
                                                want, "DRIVE-FAILED", "—",
                                                "UNTESTED", err))
                        continue
                    page.eval(_JS_SETTLE)

                for spec in specs:
                    sel = spec["sel"]
                    for prop, want in sorted(spec["props"].items()):
                        r = mutate_one(page, spec, sel, prop, want, rel, drive)
                        results.append(r[0])
                        details.append(r[1])

                # ⊕ MRB-270 phase 7 — THE CONTROL RUNS ON ITS OWN CLEAN
                # PAGE, and it runs both halves. See `control_check`.
                #
                # It used to run HERE, on `specs[0]`, after every mutation in
                # the group had already been applied and restored — and it
                # reported FAIL on C1 for two reasons that were both about the
                # control rather than about the harness. That is a control that
                # proves less than it claims, which is worse than no control:
                # a run whose control says "cannot be trusted" gets read as
                # "the harness is broken" and the 281 LIVE verdicts beside it
                # get thrown away with it.
                if control is None and specs and not drive:
                    control = control_check(
                        ks3_browser, url, rel, specs, page)
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()

    return report(results, details, parked, control)


# ⊕ MRB-270 phase 7 — sentinels that are guaranteed to MOVE a value, per
# property family. The positive half of the control needs a mutation that
# really bites; `rgb(1, 2, 3)` is no use against an assertion that wants a
# length, and `12345px` is no use against a colour.
# How many candidates have to survive a real mutation UNMOVED before the
# verdict is about the mutator rather than about the rows.
#
# Three, and the number is measured rather than picked. One unmoved candidate
# is ordinary and expected: C1's real run has exactly one — `page ground + body
# type / background-color`, whose painted value comes from
# `body.rd[data-mode="ks3"]` while `find` locates the lower-specificity
# `body { background }` in styles.css. That is a fact about that row, and the
# run reports it as DEAD, correctly. But three separate properties on three
# separate declarations all refusing to move is not three coincidences — it is
# `mutate` not applying its sentinel, or `find` returning declarations that
# supply nothing. Demonstrated by making `mutate()` ignore its sentinel: four
# candidates come back unmoved and the control reports FAIL.
_UNMOVED_IS_THE_MUTATOR = 3


def _live_sentinel(prop, want):
    if prop == "font-family":
        return '"__ks3_control_sentinel__"'
    if want.startswith("#"):
        return "rgb(1, 2, 3)"
    if want.endswith("px"):
        return "12345px"
    return "__ks3_control_sentinel__"


def control_check(ks3_browser, url, rel, specs, _page=None):
    """Prove the harness can report BOTH verdicts, on a page nothing has touched.

    A mutation harness that reports "0 dead" is only worth reading if it is
    capable of reporting a dead one — AND of reporting a live one. This runs
    both halves against the same assertion:

      NEGATIVE — rewrite the supplying declaration(s) to the value they already
          resolve to. The declaration really is rewritten, so `find`, `mutate`
          and `restore` are all exercised; the computed value simply does not
          move, so a working harness MUST call it DEAD.

      POSITIVE — rewrite the same declaration(s) to a sentinel that cannot be
          the wanted value. The computed value MUST move and the assertion MUST
          fail, so a working harness calls it LIVE.

    Either half coming back the other way means `find` is locating the wrong
    declaration, or the re-read is not seeing the mutation, and every other
    verdict in the run is worthless.

    ── WHY THIS WAS REWRITTEN (it reported FAIL on C1, wrongly) ────────────

    Two faults, and neither was in the mutation machinery it exists to police:

    1. IT RAN ON A USED PAGE. The old call site fired after every spec in the
       group had been mutated and restored, on that same document. A control
       measured downstream of the thing it is controlling for is not a control.

    2. IT TOOK `specs[0]` WITHOUT CHECKING THE ASSERTION WAS GREEN. On C1 that
       drew "page ground + body type / background-color" — an assertion the
       run itself reports DEAD, because `body`'s painted #FBF3E6 comes from
       `body.rd[data-mode="ks3"]` while the declaration `find` locates is the
       lower-specificity `body { background }` in styles.css. A no-op mutation
       on an assertion that is ALREADY FAILING fails again, for a reason that
       has nothing to do with the mutation, and the harness then indicts
       itself: "a no-op mutation made the assertion FAIL (rgb(231, 225, 212)
       -> rgb(231, 225, 212))" — the same value on both sides, which is the
       tell that nothing moved and the verdict was about the baseline.

    So the candidate is now CHOSEN rather than taken: the first assertion on a
    clean page that is green at baseline AND that a real mutation can move. If
    no assertion satisfies both, that is reported as SKIPPED with the reason —
    never as a harness fault, because "this unit has no controllable row" and
    "the harness is broken" are different sentences.

    The restore is VERIFIED both times. A restore that silently did not put the
    declaration back would poison every later measurement in the run, which is
    exactly the class of fault a control is for.
    """
    browser = ks3_browser.Browser()
    tried = []
    # Candidates rejected specifically because a REAL mutation did not move
    # them. One of those is a fact about that row. All of them is a fact about
    # the mutator — see the return at the bottom.
    unmoved = []
    try:
        browser.start()
        page = load_page(browser, url, rel)

        for spec in specs:
            sel = spec["sel"]
            if not page.eval("!!document.querySelector(%r)" % sel):
                continue
            for prop, want in sorted(spec["props"].items()):
                label = "%s / %s" % (spec["name"], prop)
                before = (page.eval("window.__ks3.style(%r, %r)"
                                    % (sel, prop)) or "").strip()
                if not before:
                    continue
                if not gate_ok(prop, want, before):
                    tried.append("%s (red at baseline: wanted %s, got %s)"
                                 % (label, want, before))
                    continue
                found = page.eval("window.__ks3mut.find(%r, %r)" % (sel, prop))
                hits = found.get("hits") or []
                if not hits:
                    tried.append("%s (no locatable source)" % label)
                    continue

                # ── NEGATIVE: a no-op mutation must leave the assertion green
                res = page.eval("window.__ks3mut.mutate(%s, %r, %r)"
                                % (_js(hits), prop, before))
                if res.get("error"):
                    raise SystemExit("HARNESS FAULT: control mutation failed "
                                     "on /%s — %s" % (rel, res["error"]))
                page.eval(_JS_SETTLE)
                after_noop = (page.eval("window.__ks3.style(%r, %r)"
                                        % (sel, prop)) or "").strip()
                rest = page.eval("window.__ks3mut.restore(%s, %s)"
                                 % (_js(hits), _js(res["saved"])))
                if rest.get("error"):
                    raise SystemExit("HARNESS FAULT: control restore failed "
                                     "on /%s — %s" % (rel, rest["error"]))
                page.eval(_JS_SETTLE)
                back = (page.eval("window.__ks3.style(%r, %r)"
                                  % (sel, prop)) or "").strip()
                if back != before:
                    return ("FAIL",
                            "%s on /%s — the RESTORE did not put the "
                            "declaration back (%s -> %s). Every measurement "
                            "taken after a mutation would be polluted."
                            % (label, rel, before, back))
                if not gate_ok(prop, want, after_noop):
                    return ("FAIL",
                            "%s on /%s — a no-op mutation made the assertion "
                            "FAIL (%s -> %s). The harness cannot be trusted."
                            % (label, rel, before, after_noop))

                # ── POSITIVE: a real mutation must make the assertion fail
                sentinel = _live_sentinel(prop, want)
                res2 = page.eval("window.__ks3mut.mutate(%s, %r, %r)"
                                 % (_js(hits), prop, sentinel))
                if res2.get("error"):
                    raise SystemExit("HARNESS FAULT: control mutation failed "
                                     "on /%s — %s" % (rel, res2["error"]))
                page.eval(_JS_SETTLE)
                after_real = (page.eval("window.__ks3.style(%r, %r)"
                                        % (sel, prop)) or "").strip()
                rest2 = page.eval("window.__ks3mut.restore(%s, %s)"
                                  % (_js(hits), _js(res2["saved"])))
                if rest2.get("error"):
                    raise SystemExit("HARNESS FAULT: control restore failed "
                                     "on /%s — %s" % (rel, rest2["error"]))
                page.eval(_JS_SETTLE)
                back2 = (page.eval("window.__ks3.style(%r, %r)"
                                   % (sel, prop)) or "").strip()
                if back2 != before:
                    return ("FAIL",
                            "%s on /%s — the RESTORE did not put the "
                            "declaration back after the live half (%s -> %s)."
                            % (label, rel, before, back2))
                if gate_ok(prop, want, after_real):
                    # This row's value does not come from the declaration
                    # `find` located. Real, but it is a fact about THIS row,
                    # not about the harness — so try the next candidate.
                    unmoved.append(label)
                    tried.append("%s (a real mutation to %s did not move it: "
                                 "%s -> %s, so `find` is not on its supplying "
                                 "declaration)" % (label, sentinel, before,
                                                   after_real))
                    continue

                return ("PASS",
                        "%s on /%s — rewrote %d declaration(s) twice. A NO-OP "
                        "(to %s) left the assertion passing, so the harness "
                        "reports DEAD when a mutation does not bite; a REAL "
                        "mutation (to %s) moved it to %s and made the "
                        "assertion fail, so it reports LIVE when one does. "
                        "Both restores verified."
                        % (label, rel, len(hits), before, sentinel, after_real))
    finally:
        browser.close()

    # ⚖️ SKIPPED AND FAIL ARE DIFFERENT SENTENCES, and which one this is turns
    # on WHY the candidates were rejected.
    #
    # Rejected because they were red at baseline, or had no locatable source →
    # this unit simply offered nothing to control against. SKIPPED, honestly.
    #
    # Rejected because a real mutation MOVED NOTHING, every time → that is not
    # a fact about the rows, it is a fact about the mutator: `mutate` is not
    # applying the sentinel, or `find` is locating nothing that matters, and
    # every LIVE verdict in the run is unearned. FAIL. Demonstrated by making
    # `mutate()` ignore its sentinel: all four candidates come back unmoved and
    # this reports FAIL rather than shrugging.
    if len(unmoved) >= _UNMOVED_IS_THE_MUTATOR:
        return ("FAIL",
                "on /%s a real mutation moved NOTHING, on all %d candidate(s) "
                "tried. That is the mutator, not the rows: either `mutate` is "
                "not applying its sentinel or `find` is locating declarations "
                "that supply nothing. Every LIVE verdict in this run is "
                "unearned. Candidates: %s"
                % (rel, len(unmoved), "; ".join(tried[:3])))
    return ("SKIPPED",
            "no assertion on /%s was both green at baseline and movable by a "
            "real mutation, so there was nothing to control against. "
            "Candidates rejected: %s"
            % (rel, "; ".join(tried[:4]) or "none matched a selector"))


def mutate_one(page, spec, sel, prop, want, rel, drive):
    """Break the shipped declaration behind one assertion, and see if it notices."""
    name = spec["name"]

    if not page.eval("!!document.querySelector(%r)" % sel):
        row = (name, rel, drive, prop, want, "MISSING", "—", "UNTESTED",
               "selector %s not present on the page" % sel)
        return (row, dict(row=row, sel=sel, hits=[], sentinel="",
                          before="", after=""))

    before = (page.eval("window.__ks3.style(%r, %r)" % (sel, prop)) or "").strip()
    baseline_ok = gate_ok(prop, want, before)

    found = page.eval("window.__ks3mut.find(%r, %r)" % (sel, prop))
    label, note = classify_supply(sel, prop, found)
    hits = found.get("hits") or []
    supply = "; ".join(
        "%s  [%s]" % (h.get("selectorText"), short_href(h.get("href")))
        + ("  (via %s)" % h["via"] if h.get("via") else "")
        + ("  !important" if h.get("priority") else "")
        for h in hits) or "—"

    if not baseline_ok:
        # The gate is already red here. Mutating would prove nothing — a value
        # that is wrong before the mutation cannot become more wrong after it.
        row = (name, rel, drive, prop, want, label, supply, "BASELINE-FAIL",
               "gate itself is red: expected %s, resolved %s" % (want, before))
        return (row, dict(row=row, sel=sel, hits=hits, sentinel="",
                          before=before, after=""))

    if not hits:
        # No author declaration anywhere on the element or its ancestors. The
        # value is arriving from the UA sheet or from a source the CSSOM cannot
        # attribute, and there is nothing for the assertion to be guarding.
        row = (name, rel, drive, prop, want, label, supply, "DEAD",
               "no shipped declaration supplies this property — "
               "nothing to break, so nothing this row can catch")
        return (row, dict(row=row, sel=sel, hits=hits, sentinel="",
                          before=before, after=before))

    sentinel = sentinel_for(prop, want)
    res = page.eval("window.__ks3mut.mutate(%s, %r, %r)"
                    % (_js(hits), prop, sentinel))
    if res.get("error"):
        raise SystemExit("HARNESS FAULT: could not mutate %s / %s on /%s — %s"
                         % (name, prop, rel, res["error"]))
    saved = res["saved"]

    page.eval(_JS_SETTLE)   # the mutation can itself start a transition
    after = (page.eval("window.__ks3.style(%r, %r)" % (sel, prop)) or "").strip()
    still_passes = gate_ok(prop, want, after)

    rest = page.eval("window.__ks3mut.restore(%s, %s)" % (_js(hits), _js(saved)))
    if rest.get("error"):
        raise SystemExit("HARNESS FAULT: restore failed for %s / %s on /%s — %s. "
                         "The document is now dirty and every later measurement "
                         "would be untrustworthy."
                         % (name, prop, rel, rest["error"]))
    back = (page.eval("window.__ks3.style(%r, %r)" % (sel, prop)) or "").strip()
    if back != before:
        raise SystemExit(
            "HARNESS FAULT: %s / %s on /%s did not return to its original "
            "computed value after restore (%s -> %s). Aborting rather than "
            "reporting results measured against a dirty document."
            % (name, prop, rel, before, back))

    verdict = "DEAD" if still_passes else "LIVE"
    if still_passes:
        note = ("broke %d declaration(s) to %s and the value stayed %s — "
                "the assertion cannot see its own source change"
                % (len(hits), sentinel, after)) + (" | " + note if note else "")
    row = (spec["name"], rel, drive, prop, want, label, supply, verdict, note)
    return (row, dict(row=row, sel=sel, hits=hits, sentinel=sentinel,
                      before=before, after=after))


def _js(value) -> str:
    import json
    return json.dumps(value)


# ── output ────────────────────────────────────────────────────────────────

def report(results, details, parked, control) -> int:
    def trunc(s, n):
        s = s or ""
        return s if len(s) <= n else s[:n - 1] + "…"

    print("─" * 118)
    print("%-34s %-26s %-22s %-7s %s"
          % ("ROW", "PAGE", "PROP", "VERDICT", "SUPPLIED BY"))
    print("─" * 118)
    for (name, rel, drive, prop, want, label, supply, verdict, note) in results:
        page_col = os.path.basename(rel).replace(".html", "")
        if drive:
            page_col += " @" + drive
        print("%-34s %-26s %-22s %-7s %s"
              % (trunc(name, 34), trunc(page_col, 26), trunc(prop, 22),
                 verdict, trunc(supply, 46)))
    print("─" * 118)
    print()

    # The supplying-selector detail. This is the part worth reading even when
    # every verdict is LIVE.
    print("WHERE EACH ASSERTED VALUE ACTUALLY COMES FROM")
    print("=" * 118)
    for (name, rel, drive, prop, want, label, supply, verdict, note) in results:
        head = "%s · %s" % (name, prop)
        if drive:
            head += " (drive: %s)" % drive
        print(head)
        print("    page      /%s" % rel)
        print("    expects   %s" % want)
        print("    supply    %s" % supply)
        print("    kind      %s%s" % (label, ("  — " + note) if note and
                                      verdict in ("LIVE", "BASELINE-FAIL",
                                                  "MISSING", "UNTESTED")
                                      else ""))
        print("    verdict   %s%s" % (verdict,
                                      ("  — " + note) if note and
                                      verdict == "DEAD" else ""))
        print()

    broad = [r for r in results if r[5] == "SUPPLIED-BY-BROAD-RULE"]
    if broad:
        print("SUPPLIED-BY-BROAD-RULE — rows named after a scoped class whose")
        print("value is in fact supplied by a rule that never mentions it:")
        for (name, rel, drive, prop, want, label, supply, verdict, note) in broad:
            print("  · %s / %s  [%s]" % (name, prop, verdict))
            print("      %s" % supply)
        print()

    standin = [r for r in results if r[5] == "SUPPLIED-BY-OTHER-PROPERTY"]
    if standin:
        print("SUPPLIED-BY-OTHER-PROPERTY — the selector is right, but no")
        print("declaration of the asserted property exists anywhere; the used")
        print("value is resolved by layout from a different property:")
        for (name, rel, drive, prop, want, label, supply, verdict, note) in standin:
            print("  · %s / %s  [%s]" % (name, prop, verdict))
            print("      %s" % supply)
        print()

    dead = [r for r in results if r[7] == "DEAD"]
    live = [r for r in results if r[7] == "LIVE"]
    other = [r for r in results if r[7] not in ("DEAD", "LIVE")]

    print("=" * 118)
    if control is None:
        print("CONTROL:  not run — no group had a locatable first assertion.")
    else:
        print("CONTROL:  %s — %s" % control)
    print("=" * 118)
    print("SUMMARY: %d assertion(s) tested — %d LIVE, %d DEAD%s"
          % (len(results), len(live), len(dead),
             ", %d not testable" % len(other) if other else ""))
    if parked:
        print("         %d parked row(s) skipped: %s"
              % (len(parked), ", ".join(p["name"] for p in parked)))
    if other:
        for (name, rel, drive, prop, want, label, supply, verdict, note) in other:
            print("         %-9s %s / %s — %s" % (verdict, name, prop, note))
    if dead:
        print()
        print("DEAD ASSERTIONS — each of these passes with its own supplying")
        print("declaration destroyed, so it is not testing what it names:")
        for (name, rel, drive, prop, want, label, supply, verdict, note) in dead:
            print("  · %s / %s on /%s" % (name, prop, rel))
            print("      %s" % note)
    print("=" * 118)

    if control is not None and control[0] == "FAIL":
        return 2
    return 1 if dead else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Source-level mutation testing for the KS3 parity assertions.")
    ap.add_argument("units", nargs="*", default=None,
                    help="unit codes, e.g. B3 C1 (default: B3)")
    ap.add_argument("--ks3-root", default="mrbadmus_site/ks3",
                    help="built KS3 tree (default: mrbadmus_site/ks3)")
    args = ap.parse_args(argv)

    units = args.units or ["B3"]
    root = args.ks3_root
    if not os.path.isdir(root):
        print("no such KS3 root: %s (run python3 generate_site_v5.py first)" % root)
        return 2
    return run(units, root)


if __name__ == "__main__":
    sys.exit(main())
