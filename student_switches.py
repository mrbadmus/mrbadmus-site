#!/usr/bin/env python3
"""student_switches.py — Design's discrete breakpoint switches, MEASURED.

    python3 student_switches.py            # extract, print the table, write it
    python3 student_switches.py --check    # extract and compare to the written
                                           # table; exit 1 on any difference

Writes `student_switches.json`, which `build_student.py` embeds in the two
generated pages and a small runtime shim applies.

── Why this measures rather than transcribes ─────────────────────────────

Design publishes the switch table in §6 of both handoff notes, and the brief
that asked for this said the job was "transcription, not invention". It is
not, quite, and the difference matters twice.

**It is not complete.** Design's class-view note lists ten switches and says
"that is the whole list; there are no others". Driven at 1460 and at 390, the
file changes THIRTEEN (element, property) pairs across ELEVEN elements, and two
of those elements are not in the table:

  * the docket's inner grid, `minmax(0,1fr)` → `repeat(auto-fit,minmax(148px,1fr))`
  * the docket's four fact rows, `row`/`baseline` → `column`/`flex-start`

Both are real discrete switches — no clamp interpolates `row` into `column` —
and a transcription of the ten would have shipped a docket that stays in four
rigid columns on a phone. The note is a good-faith summary written by hand
beside a logic class; this is the logic class.

**And a transcribed table cannot be re-derived.** A value typed out of a README
is a claim about a file as it was on 19 August. A value read out of the file is
the file. When Design ships v2, `--check` says what moved.

── What it does ──────────────────────────────────────────────────────────

For every band, and for every view-state that has to be DRIVEN to exist, it
records each element's inline style keyed by `data-dc-tpl` — Claude Design's
own compile-time template index, stamped by `support.js` in document order and
carried into the rendered DOM. Then it diffs the bands. An element whose inline
style differs between two bands is, by definition, an element a discrete switch
drives; everything continuous is a `clamp()` and reads identically at every
width because the container query resolves it in CSS, not here.

⚠️ KEYED ON `data-dc-tpl`, NOT ON A DOM PATH. The first attempt keyed on the
child-index path from the design root and produced nonsense — at 390 the header
sheds nodes, so every path after that point compares two unrelated elements and
"changes" in ways no switch causes. The template index is stable precisely
because it identifies the element in the TEMPLATE rather than in the tree.
"""

import json
import os
import sys
import time

REF = os.path.join("docs", "ks3", "design-reference", "student")
OUT = "student_switches.json"

# 360 and 390 are the primary targets; 820 and 1460 are the tablet and desktop
# bands. The bands are named for the width because Design's own table is, and
# because a name like "phone" would have to be kept in step with the number.
BANDS = [360, 390, 820, 1460]

# ⚠️ THE WIDTH `build_student.py` PHOTOGRAPHS AT, and it is load-bearing here.
# A node is HIDEABLE if it is in the snapshot and UNCREATABLE if it is not, so
# moving the snapshot moves which half of the presence gap is fixable. Kept in
# one place rather than two, because two would eventually disagree.
SNAPSHOT_BAND = 1460

# ⚠️ THE PROPERTIES A SWITCH CAN DRIVE. Everything else in an inline style is
# either a `clamp()` (continuous, and correct at every width without help) or a
# colour, and neither belongs in this table. Without this filter the diff also
# reports the full longhand expansion of `all: unset` on Design's buttons,
# which is 300 declarations of noise per element.
DRIVEN = (
    "grid-template-columns", "grid-template-rows", "grid-column", "grid-row",
    "display", "flex", "flex-direction", "flex-basis", "order",
    "align-items", "justify-content", "position", "right", "left", "top",
)

_PROBE = r"""(function () {
  var root = document.querySelector('.rd[data-mode="ks3"]');
  if (!root) { return JSON.stringify({error: 'no design root'}); }
  var out = [], seen = {};
  (function walk(el) {
    var d = el.getAttribute('data-dc-tpl');
    if (d !== null) {
      seen[d] = (seen[d] || 0) + 1;
      /* THE SWAPPABLE TEXT, found by walking DOWN A SINGLE-CHILD CHAIN to a
         lone text node.

         Not `innerText`: writing that back would flatten every child element
         into a string, and the node would still READ correctly while having
         lost all its structure.

         And not "a sole direct text child" either, which was the first rule
         and found nothing. Design's compiler wraps every `{{ }}` in an
         interpolation span, so the breadcrumb note — the one string that
         demonstrably changes — is an ELEMENT child holding a text child, not a
         text child. The chain walk reaches it and, on the way back, gives the
         shim an exact address to write to, so the wrapper survives the swap
         instead of being replaced by a bare text node. */
      var txt = null, depth = 0, cur = el;
      while (cur && cur.childNodes.length === 1) {
        cur = cur.childNodes[0];
        depth += 1;
        if (cur.nodeType === 3) { txt = cur.nodeValue; break; }
        if (cur.nodeType !== 1) { cur = null; break; }
        if (cur.getAttribute && cur.getAttribute('data-dc-tpl') !== null) {
          /* A child the table addresses in its own right. Its text belongs to
             it, not to this element, and recording it twice would have two
             rows fighting over one string. */
          txt = null; break;
        }
      }
      out.push({k: d + '#' + seen[d], t: el.tagName,
                s: el.getAttribute('style') || '', x: txt,
                xd: txt === null ? 0 : depth});
    }
    for (var i = 0; i < el.children.length; i++) { walk(el.children[i]); }
  })(root);
  return JSON.stringify({error: '', els: out});
})()"""

_CLICK = """(function (label) {
  var hit = null;
  document.querySelectorAll('button,a').forEach(function (e) {
    if (!hit && (e.innerText || '').trim() === label) { hit = e; }
  });
  if (!hit) { return 'MISS:' + label; }
  hit.click(); return 'ok';
})(%s)"""

# ── the view-states, and how to reach each one ────────────────────────────
#
# A state that cannot be reached is a state whose switches are not in the
# table, and a switch that is not in the table is a switch the shim will not
# apply. `recallCols` and `optCols` live on the recall view and `wrongCols`
# lives on the end screen; none of the three is on the page at rest.
STATES = [
    dict(page="class view",
         src="standalone/MrBadmusAI Class View.html",
         view="class", drive=[]),
    dict(page="class view",
         src="standalone/MrBadmusAI Class View.html",
         view="recall", drive=[("click", "Recall")]),
    dict(page="assignment",
         src="standalone/MrBadmusAI Assignment.html",
         view="question", drive=[]),
    dict(page="assignment",
         src="standalone/MrBadmusAI Assignment.html",
         view="done", drive=[("hash", "#done")]),
]


def _decls(style):
    out = {}
    for chunk in style.split(";"):
        if ":" not in chunk:
            continue
        k, v = chunk.split(":", 1)
        k = k.strip()
        if k in DRIVEN:
            out[k] = v.strip()
    return out


def _grab(cdp, src, drive, band):
    server, port = cdp.serve(REF)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(band, 900)
            url = "http://127.0.0.1:%d/%s" % (port, src.replace(" ", "%20"))
            hashes = [v for kind, v in drive if kind == "hash"]
            page.goto(url + (hashes[0] if hashes else ""))
            time.sleep(3.0)
            for kind, val in drive:
                if kind == "click":
                    got = page.eval(_CLICK % json.dumps(val))
                    if str(got).startswith("MISS"):
                        raise SystemExit(
                            "student_switches: could not reach the state — no "
                            "control labelled %r on %s at %dpx. A state this "
                            "cannot drive is a state whose switches will be "
                            "missing from the table, and the shim will then "
                            "leave those elements frozen at their desktop "
                            "values, silently." % (val, src, band))
                    time.sleep(1.0)
            got = json.loads(page.eval(_PROBE))
            if got.get("error"):
                raise SystemExit("student_switches: %s in %s"
                                 % (got["error"], src))
            return {e["k"]: (e["t"], _decls(e["s"]), e.get("x"), e.get("xd"))
                    for e in got["els"]}
    finally:
        server.shutdown()


def extract(cdp, verbose=True):
    """Return {page: {"styles": ..., "hide": ..., "absent": ...}}.

    ── THE THREE MECHANISMS, and which two a snapshot can be fixed for ──

    Design switches discretely three ways, measured rather than assumed:

      "styles"  an inline declaration changes between bands. 19 of these. A
                snapshot froze them at desktop; they are simply reapplied.

      "hide"    a node EXISTS at desktop and does not exist below. The snapshot
                has it, so it can be hidden — which is what Design's own file
                does to it, by not rendering it. 26 nodes on the class view, 69
                on the assignment. This is the half that was causing every
                remaining pixel of horizontal overflow at 390px: an account
                cluster reading `PROD AY Ayo Settings Sign out` is 256px wide
                and Design shows only the avatar.

      "absent"  a node does NOT exist at desktop and does exist below. The
                snapshot has no such node and no shim can conjure one. 6 on the
                class view (the work rows' mono meta line), 46 on the
                assignment (the marker strip and the readout row). RECORDED,
                not approximated — this is the part that closes when the
                behaviour is ported and the page renders from data.

    ⚠️ "absent" IS AN OUTPUT, NOT AN ERROR. Writing it down is the whole point:
    a gap that is measured and named is a gap somebody can close, and a gap
    that is only implied by a screenshot is one that gets argued about.
    """
    table, notes = {}, []
    per_state = {}
    for st in STATES:
        per_band = {}
        for band in BANDS:
            per_band[band] = _grab(cdp, st["src"], st["drive"], band)
        per_state.setdefault(st["page"], []).append((st["view"], per_band))

    for page_name, states in per_state.items():
        page = table.setdefault(page_name, {"styles": {}, "text": {},
                                            "hide": {}, "absent": {}})
        for view, per_band in states:
            keys_at = {b: set(per_band[b]) for b in BANDS}
            common = set.intersection(*keys_at.values())
            everything = set.union(*keys_at.values())

            # ── styles ────────────────────────────────────────────────
            n_sw = 0
            for k in sorted(common, key=_order):
                tpl = k.split("#")[0]
                props = set()
                for band in BANDS:
                    props |= set(per_band[band][k][1])
                for prop in sorted(props):
                    vals = {b: per_band[b][k][1].get(prop) for b in BANDS}
                    if len(set(vals.values())) == 1:
                        continue
                    slot = page["styles"].setdefault(tpl, {}).setdefault(prop, {})
                    for b in BANDS:
                        prev = slot.get(str(b), vals[b])
                        if prev != vals[b]:
                            raise SystemExit(
                                "student_switches: two nodes share "
                                "data-dc-tpl=%s and disagree on `%s` at %dpx "
                                "(%r vs %r). The table is keyed on the "
                                "template index, so it cannot represent that."
                                % (tpl, prop, b, prev, vals[b]))
                        slot[str(b)] = vals[b]
                    n_sw += 1

            # ── text ──────────────────────────────────────────────────
            #
            # Design's THIRD mechanism, and the one nothing had named. The
            # breadcrumb note reads `AUTUMN TERM · WEEK 04 / 12` at desktop and
            # `WK 04 / 12` below. At 360px the long string measures 206px
            # inside a 360px page, and after the styles and the presence were
            # both applied it was the last pixel of horizontal overflow left on
            # either page.
            #
            # THIS IS A SWAP, NOT A REWRITE. Both strings are Design's and both
            # are measured out of Design's file. Nothing here abbreviates
            # anything, which is the whole difference between reproducing a
            # design and redesigning it inside a shim.
            n_text = 0
            for k in sorted(common, key=_order):
                vals = {str(b): per_band[b][k][2] for b in BANDS}
                if len(set(vals.values())) == 1:
                    continue
                if any(v is None for v in vals.values()):
                    # A node with a sole text child at one band and element
                    # children at another is not a text swap; something inside
                    # it appeared or went, and the presence pass owns that.
                    continue
                depths = {per_band[b][k][3] for b in BANDS}
                if len(depths) != 1:
                    # The string moved to a different place in the subtree
                    # between bands. That is not a swap this can address, and
                    # guessing which node to write would be worse than saying
                    # so.
                    continue
                vals["_d"] = depths.pop()
                page["text"][k] = vals
                n_text += 1

            # ── presence ──────────────────────────────────────────────
            #
            # The snapshot is taken at SNAPSHOT_BAND. A node in it can be
            # hidden; a node not in it cannot be created.
            snap = str(SNAPSHOT_BAND)
            n_hide = n_absent = 0
            for k in sorted(everything - common, key=_order):
                missing = [str(b) for b in BANDS if k not in keys_at[b]]
                if k in keys_at[SNAPSHOT_BAND]:
                    page["hide"].setdefault(k, sorted(
                        set(page["hide"].get(k, [])) | set(missing)))
                    n_hide += 1
                else:
                    have = [str(b) for b in BANDS if k in keys_at[b]]
                    page["absent"].setdefault(k, sorted(
                        set(page["absent"].get(k, [])) | set(have)))
                    n_absent += 1

            notes.append((page_name, view, len(common), n_sw, n_text,
                          n_hide, n_absent))
            if verbose:
                print("     %-11s %-9s %4d common · %2d styled · %d text · "
                      "%2d hideable · %2d UNCREATABLE"
                      % (page_name, view, len(common), n_sw, n_text, n_hide,
                         n_absent))
    return table, notes


def _order(k):
    return (int(k.split("#")[0]), int(k.split("#")[1]))


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ks3_browser as cdp

    check = "--check" in sys.argv
    print("\n🎚  student_switches — Design's discrete switches, measured\n")
    print("     bands: %s\n" % ", ".join("%dpx" % b for b in BANDS))
    table, _notes = extract(cdp)

    n_style = sum(len(props) for pg in table.values()
                  for props in pg["styles"].values())
    n_text = sum(len(pg["text"]) for pg in table.values())
    n_hide = sum(len(pg["hide"]) for pg in table.values())
    n_absent = sum(len(pg["absent"]) for pg in table.values())
    print("\n     %d switched declaration(s) across %d element(s); "
          "%d text swap(s); %d hideable node(s); %d UNCREATABLE node(s)"
          % (n_style,
             sum(len(pg["styles"]) for pg in table.values()),
             n_text, n_hide, n_absent))

    for page in sorted(table):
        print("\n  %s — styles" % page)
        for tpl in sorted(table[page]["styles"], key=int):
            for prop, vals in sorted(table[page]["styles"][tpl].items()):
                bands = " · ".join("%d:%s" % (b, vals.get(str(b)))
                                   for b in BANDS)
                print("    tpl=%-4s %-22s %s" % (tpl, prop, bands[:130]))
        for k, vals in sorted(table[page]["text"].items(),
                              key=lambda x: _order(x[0])):
            print("  %s — text swap %s (depth %s): %s"
                  % (page, k, vals.get("_d"),
                     " · ".join("%d:%r" % (b, vals[str(b)])
                                for b in BANDS)[:120]))
        if table[page]["hide"]:
            print("  %s — hidden below the band(s) shown (%d node(s))"
                  % (page, len(table[page]["hide"])))
        if table[page]["absent"]:
            print("  %s — ⚑ UNCREATABLE, not in the snapshot (%d node(s)): %s"
                  % (page, len(table[page]["absent"]),
                     ", ".join(sorted(table[page]["absent"], key=_order)[:8])))

    blob = json.dumps(table, indent=2, sort_keys=True) + "\n"
    if check:
        if not os.path.exists(OUT):
            print("\n  FAIL  %s does not exist." % OUT)
            return 1
        if open(OUT, encoding="utf-8").read() != blob:
            print("\n  FAIL  the measured table differs from %s. Design's "
                  "delivery has moved, or the extraction has. Re-run without "
                  "--check to adopt it, and read the diff first." % OUT)
            return 1
        print("\n  PASS  the measured table matches %s exactly." % OUT)
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(blob)
    print("\n     → %s\n" % OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
