#!/usr/bin/env python3
"""build_student_port.py — the PORTED student pages: Design's markup and logic,
rendered by our own vanilla runtime with no React and no `support.js`.

    python3 build_student_port.py

Writes:

    mrbadmus_site/shared/student-ds.css        Design's six stylesheets, once
    mrbadmus_site/shared/student-fixture-class.js       Design's example data
    mrbadmus_site/shared/student-fixture-assignment.js  Design's example data
    mrbadmus_site/student/class-ported.html        production — NO data in it
    mrbadmus_site/student/assignment-ported.html  production — NO data in it
    mrbadmus_site/student/class-fixture.html       the gates' page
    mrbadmus_site/student/assignment-fixture.html  the gates' page
    student/*.html, shared/*.js                (mirror)

── TWO PAGES, BECAUSE ONE CANNOT BE BOTH ────────────────────────────────

A single page that renders Design's example data when the database is quiet
is a page that shows one child's marks to another the first time a fetch
fails. So the split is structural rather than conditional:

  *-ported.html   Design's markup and Design's logic with every data literal
                  lifted out. It defines `window.__MRB_MOUNT__` and DOES NOT
                  CALL IT, and it ends by loading `shared/student-live.js`.
                  There is no fixture in this file to fall back to, so there
                  is no code path that could fall back to one.
  *-fixture.html  the same file but for its banner comment and its last two
                  script tags, which load Design's extracted values and mount.
                  This is what `student_behaviour.py` drives.

Design's data is lifted BY SOURCE TRANSFORMATION, never retyped — the five
class-view fields and the five assignment fields by balanced-literal scan out
of the logic class, the eleven identity strings by exact match against the
compiled template. Anything on either list that cannot be found stops the
build; see `find_field` and `bindings_for`.

⛔ It writes no live page. `_REFUSED` in `build_student.py` is the same list and
the same reason: swapping a preview onto a live path is a separate, deliberate
change, gated on the whole Phase 5 checklist.

── Why this exists beside build_student.py rather than replacing it ──────

`build_student.py` photographs Design's rendered DOM. That was the right first
move — it made parity a property rather than an effort — and it has two limits
that no amount of care removes:

  * IT IS ONE STATE. 52 nodes Design renders below desktop are simply not in a
    desktop photograph, and no runtime shim can conjure them. Neither is the
    recall round, the expanded work row, the marker sheet or the end screen.
  * IT IS 558 KB, of which 306 KB is Chrome's longhand expansion of `all:
    unset` on 25 buttons and 223 KB is CSS inlined once per page.

This renders from Design's TEMPLATE instead, so every state exists, `all:unset`
stays two words, and the stylesheets are linked and cached. The two builds are
kept side by side until the ported pages pass the same parity gate the
snapshots do — at which point the snapshot build retires, with a note, rather
than being deleted.

── What is Design's ─────────────────────────────────────────────────────

The markup (Design's template, compiled by `student_template.py`, not retyped),
the behaviour (Design's logic class, extracted verbatim), the styling (Design's
own six stylesheets, concatenated in Design's own link order), and the brand
mark (captured from Design's render). What is ours is `shared/student-runtime.js`
— a 30-line base class and a renderer for three constructs.
"""

import html
import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join("docs", "ks3", "design-reference", "student")
DS = os.path.join(REF, "source", "_ds",
                  "mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1")
SITE_OUT = os.path.join("mrbadmus_site", "student")
MIRROR_OUT = "student"
SHARED_OUT = os.path.join("mrbadmus_site", "shared")

TEMPLATES = "student_templates.json"
DS_CSS_NAME = "student-ds.css"
DS_CSS_URL = "/shared/" + DS_CSS_NAME
SERVED_FONTS = "/shared/fonts/"

_REFUSED = {"class.html", "assignment.html", "classes.html", "settings.html",
            "claim-confirm.html"}

RUNTIME_JS_NAME = "student-runtime.js"
LIVE_JS_NAME = "student-live.js"
LIVE_JS_URL = "/shared/" + LIVE_JS_NAME

PAGES = [
    dict(page="class view", out="class-ported.html",
         fixture_out="class-fixture.html",
         fixture_js="student-fixture-class.js",
         title="8r/Sc1 · My class · MrBadmusAI",
         fields=["work", "roster", "weekPts", "lessonDefs", "questions"],
         state_fields=["streak"]),
    dict(page="assignment", out="assignment-ported.html",
         fixture_out="assignment-fixture.html",
         fixture_js="student-fixture-assignment.js",
         title="Assignment · 8r/Sc1 · MrBadmusAI",
         fields=["questions", "wrongPlan", "figCaptions", "KEY", "DUE"],
         state_fields=[]),
]

# ── the identity strings, which are NOT in the logic ──────────────────────
#
# Design's example data lives in two places and only one of them is a field.
# `8r/Sc1`, `Ayo`, `Mr Badmus`, `28 students` are TEXT NODES in Design's
# template — typed into the markup, not computed — so seaming the logic class
# alone leaves a page that reads its work from the database and still greets
# every student as Ayo.
#
# ⚠️ THEY ARE BOUND AS LITERALS AND MUST STAY LITERALS. Design's compiler wraps
# every `{{ }}` in text position in `<span class="sc-interp">`; rewriting these
# nodes into interpolations would therefore ADD one element per binding and the
# parity gate counts elements. So the binding happens to the compiled template
# at mount time — the node's `v` is replaced with a different plain string —
# and the node count is untouched. See `applyBindings` in student-runtime.js.
#
# Each entry is (exact literal, data key). EVERY node whose text is exactly
# that literal is bound, which is deliberate: `8r/Sc1` appears twice in the
# class view's markup and both are the same class. Whitespace is part of the
# match, which is why the padded third occurrence is a separate key rather than
# a third match — binding it to `className` would silently eat its indentation.
BINDINGS = {
    "class view": [
        ("8r/Sc1", "className"),
        ("8r/Sc1\n        ", "classNamePadded"),
        ("Ayo", "studentFirstName"),
        ("Welcome back, Ayo · your class", "welcomeLine"),
        ("AY", "studentInitials"),
        ("Mr Badmus", "teacherName"),
        ("MB", "teacherInitials"),
        ("28 students", "classSize"),
        ("Biology", "subjectLabel"),
        ("Cells & microscopy", "topicTitle"),
        ("AUTUMN TERM", "termLabel"),
    ],
    "assignment": [
        ("8r/Sc1", "className"),
        ("Back to 8r/Sc1", "backToClass"),
        ("Cells & microscopy", "topicTitle"),
    ],
}

_BANNER = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED — do not edit. `python3 build_student_port.py`
  ══════════════════════════════════════════════════════════════════════════

  %s, PORTED: Claude Design's own template and Design's own logic class,
  rendered by shared/student-runtime.js. No React and none of Design's
  `support.js` ships here — that was ruled on 20 Aug 2026.

  The markup is not retyped and neither is the behaviour. Both are extracted
  from docs/ks3/design-reference/student/ by student_template.py, so the only
  way this can differ from Design's file is if Design's file changed.

  STILL NOT THE LIVE PAGE: the live pages are student/class.html and
  student/assignment.html and this build never writes them.

  THERE IS NO DATA IN THIS FILE. Design's example values — the work list, the
  roster, the week points, the questions, and the identity strings that were
  typed into the markup — have been lifted out into `window.__MRB_DATA__`, and
  every read of them goes through `MRB_DATA(k)`, which THROWS when the key is
  absent. So this page cannot render one child's homework to a different
  child: with no data source loaded it renders nothing at all and says why.
  The data arrives from %s, and from nowhere else.

  Its twin, %s, is this same file with two differences and no others — this
  comment, and the script tags at the end, where it loads Design's own
  extracted example values and mounts. That twin is what student_parity.py and
  student_behaviour.py drive, which is how Design's data can still be exercised
  in full without being reachable from here.
  ══════════════════════════════════════════════════════════════════════════
-->
"""

_BANNER_FIXTURE = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED — do not edit. `python3 build_student_port.py`
  ══════════════════════════════════════════════════════════════════════════

  %s, PORTED — THE FIXTURE PAGE. The same file as %s but for this comment and
  the script tags at the end: this one loads Design's own extracted example
  data and mounts, that one loads the live data source and does not.

  ⛔ NOT A CANDIDATE FOR ANY LIVE PATH, and not because it is unfinished — it
  is one real class, hard-coded, for every visitor. It exists so the gates have
  something with known values to drive: `student_parity.py` compares its render
  against Design's own file and `student_behaviour.py` drives both through the
  same 28 journeys. A gate that drove the production page would be asserting
  against whatever the database happened to hold that morning.
  ══════════════════════════════════════════════════════════════════════════
-->
"""


def _refuse(path):
    if os.path.basename(path) in _REFUSED:
        raise SystemExit(
            "build_student_port.py REFUSES to write %s — that is a LIVE "
            "student page." % path)


def ds_css():
    """Design's six stylesheets, in Design's own link order, as one file.

    ⚠️ NOT THE SITE'S OWN COPIES. `shared/tokens.css` and `shared/ks3.css` have
    both grown well past the versions in Design's bundle — measured, 31.8 KB
    against 24.5 KB and 548 KB against 42.5 KB — so linking the site's files
    would give the page a cascade Design never drew and never checked. Design's
    are vendored, which is also what makes the parity gate meaningful.

    Reconciling the two is real work and it is NOT this build's: it would
    change what KS3 lesson pages render as well, and it belongs with the
    already-open note about `--ks3-data` being in the engine's tokens and not
    in Design's.
    """
    order = ["tokens/src-styles-tokens.css", "tokens/shared-tokens.css",
             "tokens/shared-ks3.css", "fonts/fonts.css", "_ds_bundle.css",
             "styles.css"]
    out, sizes = [], []
    for rel in order:
        path = os.path.join(DS, rel)
        if not os.path.exists(path):
            raise SystemExit("build_student_port.py: missing %s" % path)
        css = open(path, encoding="utf-8").read()
        if rel.endswith("fonts.css"):
            # The faces point at `./` inside the bundle; the site self-hosts
            # every one of the seven at /shared/fonts/ and they are
            # byte-identical (verified by sha256 in build_student.py).
            css = css.replace("./", SERVED_FONTS)
        out.append("/* ── %s ── */\n%s" % (rel, css))
        sizes.append((rel, len(css)))
    return "\n\n".join(out), sizes


# ── every token the page references must resolve ──────────────────────────
#
# ⚑ THIS EXISTS BECAUSE ONE DID NOT, AND THE PAGE STILL LOOKED FINE. The ruled
# fix to the recall `CORRECT` label points it at `--ks3-ok-dark`, minted under
# MRB-252 in `shared/tokens.css`. Design's `_ds` bundle predates that mint and
# does not define it, so the label resolved to the INHERITED ink — measured,
# rgb(34,30,27) where #40DD84 was intended. No error, no warning; a green word
# quietly became a black one, and the token-contract gate went green because a
# black word is not a `--st-ok-room` violation either.
#
# An undefined custom property is the quietest failure CSS has. So the build
# collects every `var(--…)` the template and the logic reference, checks each
# against what the stylesheets actually define, and tops up the difference from
# the site's own `shared/tokens.css` — by NAME, read out of that file, never
# retyped. Anything still unresolved stops the build.
_VAR_RE = None


def referenced_tokens(tpl):
    """Every `--custom-property` the template or the logic asks for."""
    import re as _re
    blob = json.dumps(tpl["roots"]) + tpl["logic"] + json.dumps(tpl["imports"])
    return set(_re.findall(r"var\(\s*(--[a-zA-Z0-9-]+)", blob))


def defined_tokens(css, tpl=None):
    """Every custom property the page can resolve — from CSS AND from markup.

    ⚠️ THE MARKUP HALF IS NOT OPTIONAL. Design declares `--st-ok-room` inline on
    the design root (`--st-ink:var(--ks3-ink);--st-ok-room:#55B36A` in the
    root's own style attribute) rather than in a stylesheet, which is exactly
    what the handoff note says it did — "Declared on the design root, not in
    the token files". A scan that read only the stylesheets called it undefined
    and stopped the build on a token that resolves perfectly well.

    (The canonical copy now lives in `3d-studio/src/styles/tokens.css` under the
    20 Aug 2026 ruling. The inline declaration is byte-identical to it and is
    what actually paints, being on the element; the token-file entry is what
    makes Design's NEXT delivery inherit the value instead of re-declaring it.)
    """
    import re as _re
    found = set(_re.findall(r"(--[a-zA-Z0-9-]+)\s*:", css))
    if tpl:
        blob = json.dumps(tpl["roots"])
        found |= set(_re.findall(r"(--[a-zA-Z0-9-]+)\s*:", blob))
    return found


def top_up(css, wanted, tpls):
    """Define, from shared/tokens.css, any token the bundle is missing."""
    import re as _re
    have = defined_tokens(css)
    for t in tpls.values():
        have |= defined_tokens("", t)
    missing = sorted(wanted - have)
    if not missing:
        return css, []
    site = open(os.path.join("shared", "tokens.css"), encoding="utf-8").read()
    lines, still = [], []
    for name in missing:
        m = _re.search(r"%s\s*:\s*([^;]+);" % _re.escape(name), site)
        if m:
            lines.append("  %s: %s;" % (name, m.group(1).strip()))
        else:
            still.append(name)
    if still:
        raise SystemExit(
            "build_student_port.py: %d token(s) the page references are "
            "defined NOWHERE — not in Design's bundle and not in "
            "shared/tokens.css: %s.\n"
            "  An undefined custom property does not error; it falls back to "
            "the inherited value and the page looks almost right. Define them "
            "or stop referencing them." % (len(still), ", ".join(still)))
    block = ("\n\n/* ── minted since Design's bundle, read out of "
             "shared/tokens.css ──\n"
             "   Design's `_ds` drop predates MRB-252, which minted the two\n"
             "   body-size greens. Values are COPIED FROM the site's token\n"
             "   file at build time rather than retyped, so they cannot\n"
             "   drift from it. */\n:root,\n.rd[data-mode=\"ks3\"] {\n%s\n}\n"
             % "\n".join(lines))
    return css + block, missing


# ── Mide's rulings, applied to Design's delivery at build time ────────────
#
# ⚑ THESE WERE HAND-EDITED INTO THE GENERATED PAGES ONCE, AND A REBUILD ATE
# THEM. Commit 895f34766 applied three of Mide's rulings to
# `student/class-ported.html` and `student/assignment-ported.html` — files this
# script writes and whose own banner says "GENERATED — do not edit". They
# survived until the next build, which is this one, and the behaviour gate went
# red in thirteen places naming a divergence that had been correctly applied
# hours earlier.
#
# So they are applied HERE now, from `student_rulings.py`, on the way from
# Design's delivery to the page. See that file for what each ruling is and for
# the full account of the recovery. Nothing about their content changed.


def apply_rulings(page, logic, roots):
    """Design's logic and template with Mide's rulings applied.

    Returns (logic, roots, replacements, pruned). Every `old` must appear
    EXACTLY ONCE — not zero times, and not twice. A ruling that silently
    matched nothing is the same failure as the hand-edit it replaces: the build
    goes green and the ruling is not in the page.
    """
    import student_rulings

    reps = student_rulings.LOGIC.get(page, ())
    for old, new in reps:
        n = logic.count(old)
        if n != 1:
            raise SystemExit(
                "build_student_port.py: the MRB-275 ruling for %r anchors on a "
                "span that appears %d times in Design's logic, not once:\n"
                "    %s…\n"
                "Design has redrawn that span. The ruling is Mide's and still "
                "stands; re-anchor it in student_rulings.py rather than "
                "dropping it, and do NOT hand-edit the built page — that is "
                "exactly how it was lost the first time."
                % (page, n, old.strip().split("\n")[0][:78]))
        logic = logic.replace(old, new, 1)

    prune = set(student_rulings.PRUNE.get(page, ()))
    removed = [0]

    def walk(node):
        if not isinstance(node, dict) or not node.get("c"):
            return
        kept = []
        for kid in node["c"]:
            if isinstance(kid, dict) and kid.get("i") in prune:
                removed[0] += 1
                prune.discard(kid.get("i"))
                continue
            walk(kid)
            kept.append(kid)
        node["c"] = kept

    roots = json.loads(json.dumps(roots))
    for root in roots:
        walk(root)
    if prune:
        raise SystemExit(
            "build_student_port.py: the MRB-275 ruling for %r prunes template "
            "node(s) %s, and they are not in Design's template. The ruling "
            "stands; re-read the delivery and re-anchor it."
            % (page, sorted(prune)))
    return logic, roots, len(reps), removed[0]


# ── lifting Design's data out of Design's logic ───────────────────────────
#
# The fields are welded into the class body as initialisers:
#
#     work = [ { id: 'a5', … }, … ];
#
# so the seam is a source transformation and not a hand edit. The literal is
# found by BALANCED SCAN rather than by regex, because every one of these
# contains the terminator: `questions` holds apostrophes, `figCaptions` holds
# semicolons inside strings, and `work` holds braces sixteen deep. A regex that
# stopped at the first `;` would truncate the class view's work list in the
# middle of a note and produce a syntax error four hundred lines later.
#
# ⚠️ A FIELD THAT CANNOT BE FOUND STOPS THE BUILD. The failure this refuses to
# have is the quiet one: a rename in Design's next delivery, a field silently
# left unseamed, and a production page that reads four lists from the database
# and the fifth from Design's imagination. There is no fallback path here on
# purpose — see `MRB_DATA` in the emitted page, which has none either.

def _skip_ws(src, i):
    """Advance past whitespace and both comment forms."""
    while i < len(src):
        ch = src[i]
        if ch in " \t\r\n":
            i += 1
        elif src.startswith("//", i):
            j = src.find("\n", i)
            i = len(src) if j < 0 else j + 1
        elif src.startswith("/*", i):
            j = src.find("*/", i)
            if j < 0:
                raise SystemExit("build_student_port.py: unterminated comment")
            i = j + 2
        else:
            return i
    return i


def balanced_literal(src, start):
    """From `start`, the literal that runs to its terminating top-level `;`.

    Returns (literal_text, index_of_the_semicolon). Strings, escapes and
    comments are all respected, so a `;` or a `}` inside `'…'` is just text.
    """
    depth, i, n = 0, start, len(src)
    while i < n:
        ch = src[i]
        if ch in "'\"`":
            quote, i = ch, i + 1
            while i < n:
                if src[i] == "\\":
                    i += 2
                    continue
                if src[i] == quote:
                    i += 1
                    break
                i += 1
            continue
        if src.startswith("//", i) or src.startswith("/*", i):
            i = _skip_ws(src, i)
            continue
        if ch in "[{(":
            depth += 1
        elif ch in "]})":
            depth -= 1
            if depth < 0:
                raise SystemExit(
                    "build_student_port.py: unbalanced %r at offset %d" % (ch, i))
        elif ch == ";" and depth == 0:
            return src[start:i].rstrip(), i
        i += 1
    raise SystemExit(
        "build_student_port.py: no terminating `;` for the literal at offset "
        "%d — Design's logic class does not parse the way this build assumes."
        % start)


def find_field(logic, name):
    """(literal, start, end_of_statement) for `^  <name> = …;`."""
    import re as _re
    m = _re.search(r"(?m)^  %s\s*=\s*" % _re.escape(name), logic)
    if not m:
        raise SystemExit(
            "build_student_port.py: the field %r is NOT in Design's logic "
            "class. It is on this build's seam list, which means either "
            "Design has renamed it or it has gone. Seaming four of five data "
            "fields and leaving the fifth welded shut is the failure mode this "
            "refuses to have — reconcile the list against the delivery."
            % name)
    lit, semi = balanced_literal(logic, m.end())
    return lit, m.start(), semi + 1


def seam_logic(spec, logic):
    """Design's logic with every data literal replaced by a `MRB_DATA` read.

    Returns (seamed_logic, {key: js_literal_source}). The literal is carried to
    the fixture as SOURCE, not re-serialised through JSON — Design wrote
    `\\u00B7` and `\\u2019` by hand in a hundred places and a round trip
    through json would rewrite every one of them into a raw character. Same
    bytes in, same bytes out.
    """
    fixture, edits = {}, []
    for name in spec["fields"]:
        lit, start, end = find_field(logic, name)
        fixture[name] = lit
        edits.append((start, end, "  %s = MRB_DATA(%s);" % (name, _q(name))))

    # ── `state` is not lifted; ONE PROPERTY INSIDE IT IS ──────────────────
    #
    # `streak` is a student's recall streak and belongs to the student;
    # everything else in that initialiser is view state — which tab is open,
    # how wide the window is — and belongs to the page. Lifting the whole
    # initialiser would have made the data source responsible for `w: 1200`,
    # which is not data, and would have put a render-time constant behind a
    # throw.
    if spec["state_fields"]:
        lit, start, end = find_field(logic, "state")
        new = lit
        import re as _re
        for name in spec["state_fields"]:
            m = _re.search(r"\b%s\s*:\s*([^,}\s]+)" % _re.escape(name), new)
            if not m:
                raise SystemExit(
                    "build_student_port.py: `%s` is not a property of the "
                    "`state` initialiser in Design's logic. It is on the seam "
                    "list; reconcile it against the delivery." % name)
            fixture[name] = m.group(1)
            new = new[:m.start(1)] + "MRB_DATA(%s)" % _q(name) + new[m.end(1):]
        edits.append((start, end, "  state = %s;" % new))

    for start, end, text in sorted(edits, reverse=True):
        logic = logic[:start] + text + logic[end:]
    return logic, fixture


def _q(s):
    return json.dumps(s)


# ── binding a literal text node without becoming an interpolation ─────────

def text_paths(roots, literal):
    """Every path to a text node whose value is EXACTLY `literal`.

    A path is [root index, child index, child index, …] into `c`.
    """
    hits = []

    def walk(node, path):
        if not isinstance(node, dict):
            return
        if node.get("t") == "#" and node.get("v") == literal:
            hits.append(path)
        for i, kid in enumerate(node.get("c") or []):
            walk(kid, path + [i])

    for i, root in enumerate(roots):
        walk(root, [i])
    return hits


def bindings_for(page, tpl):
    """The binding table, and the values Design typed, for one page."""
    table, values = [], {}
    for literal, key in BINDINGS.get(page, ()):
        paths = text_paths(tpl["roots"], literal)
        if not paths:
            raise SystemExit(
                "build_student_port.py: %s — the literal %r is not a text node "
                "in Design's template. It is on the binding list, so either "
                "Design has redrawn that line or the whitespace has moved. "
                "Nothing is guessed here: an approximate match would bind the "
                "wrong node and the page would say the right thing in the "
                "wrong place." % (page, literal))
        if key in values and values[key] != literal:
            raise SystemExit(
                "build_student_port.py: %s — the key %r is claimed by two "
                "different literals, %r and %r. One key is one value; give "
                "them separate keys." % (page, key, values[key], literal))
        values[key] = literal
        for path in paths:
            table.append({"p": path, "k": key})
    return table, values


def count_nodes(roots):
    """Nodes in the compiled template — reported after the ruling, not before.

    `student_templates.json` records Design's count; the class view's ruling
    prunes seven subtrees out of it, so quoting the stored number would report
    404 for a page that ships 384.
    """
    n = [0]

    def walk(node):
        if not isinstance(node, dict):
            return
        # Element nodes only — the same thing `student_templates.json` counts,
        # so the two numbers are comparable. Text nodes carry no `i`.
        if "i" in node:
            n[0] += 1
        for kid in node.get("c") or []:
            walk(kid)

    for root in roots:
        walk(root)
    return n[0]


def scrub_roots(roots, bind_table):
    """Design's template with every bound literal emptied.

    ⚑ THIS IS THE HALF THAT IS EASY TO MISS, and missing it makes the whole
    seam cosmetic. Binding at mount time replaces the text node's value in
    memory — it does NOT remove the value from the compiled template that
    SHIPS. Without this, `class-ported.html` reads its work list from the
    database and still has the string `Ayo` sitting in it, four hundred
    kilobytes down, waiting for the day somebody renders the template without
    the bindings.

    So the shipped template carries an EMPTY string at each bound path and the
    value arrives with the data. Empty rather than a placeholder because a
    placeholder is a thing that can be shipped by accident; empty is not
    mistakable for a real name. The node itself stays — a text node with no
    text is still a text node, and the parity gate counts nodes.
    """
    out = json.loads(json.dumps(roots))
    for b in bind_table:
        node = out[b["p"][0]]
        for i in b["p"][1:]:
            node = node["c"][i]
        if node.get("t") != "#":
            raise SystemExit(
                "build_student_port.py: the binding path for %r does not land "
                "on a text node." % b["k"])
        node["v"] = ""
    return out


# Keys whose value appearing anywhere in the shipped production page is a
# BUILD FAILURE rather than a note. These are the ones that name a person or a
# class: if `Ayo` survives the seam, the seam did not happen.
_MUST_NOT_LEAK = {"className", "classNamePadded", "studentFirstName",
                  "welcomeLine", "studentInitials", "teacherName",
                  "teacherInitials", "classSize", "backToClass"}


def fixture_js(spec, page, data_literals, bind_values):
    """`window.__MRB_DATA__ = {…}` — Design's own values, once, for the gates."""
    rows = []
    for name in list(spec["fields"]) + list(spec["state_fields"]):
        rows.append("  %s: %s" % (_q(name), data_literals[name]))
    for key in sorted(bind_values):
        rows.append("  %s: %s" % (_q(key), _q(bind_values[key])))
    return (
        "/* ══════════════════════════════════════════════════════════════\n"
        "   GENERATED — do not edit. `python3 build_student_port.py`\n"
        "   ══════════════════════════════════════════════════════════════\n"
        "\n"
        "   Claude Design's own example data for the %s, lifted out of\n"
        "   Design's logic class and out of Design's template by source\n"
        "   transformation — not retyped, and not re-serialised. Every value\n"
        "   below is the same bytes Design wrote.\n"
        "\n"
        "   ⛔ FOR THE GATES ONLY. This is one real class's homework with one\n"
        "   real child's name on it, frozen. It is loaded by %s and by nothing\n"
        "   that a student can reach: the production page loads %s instead,\n"
        "   and `MRB_DATA` throws rather than falling back to this.\n"
        "   ══════════════════════════════════════════════════════════════ */\n"
        "window.__MRB_DATA__ = {\n%s\n};\n"
        % (page, spec["fixture_out"], LIVE_JS_NAME, ",\n".join(rows)))


def page_html(spec, tpl, roots, bind_table, logic, fixture=False):
    tail = (
        "<script src=\"/shared/%s\"></script>\n"
        "<script>window.__MRB_MOUNT__();</script>\n" % spec["fixture_js"]
    ) if fixture else (
        "<script src=\"%s\"></script>\n" % LIVE_JS_URL
    )
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, "
        "initial-scale=1\">\n"
        "<title>%s</title>\n"
        "%s"
        "<link rel=\"stylesheet\" href=\"%s\">\n"
        "<style>body{margin:0;background:#FBF3E6}"
        "a{color:var(--ks3-accent-text);text-decoration:none}"
        "a:hover{color:var(--ks3-accent-hover)}"
        "button{font-family:inherit}</style>\n"
        "</head>\n<body>\n"
        "<div id=\"mrb-student\" style=\"background:var(--st-ground);"
        "min-height:100vh\"></div>\n"
        "<script src=\"/shared/student-runtime.js\"></script>\n"
        "<script>window.__MRB_TPL__=%s;</script>\n"
        "<script>window.__MRB_BIND__=%s;</script>\n"
        "<script>\n%s\n</script>\n"
        "<script>\n%s\n</script>\n"
        "%s"
        "</body>\n</html>\n"
        % (html.escape(spec["title"]),
           (_BANNER_FIXTURE % (spec["page"].capitalize(), spec["out"]))
           if fixture else
           (_BANNER % (spec["page"].capitalize(), LIVE_JS_NAME,
                       spec["fixture_out"])),
           DS_CSS_URL,
           json.dumps({"roots": roots, "imports": tpl["imports"]},
                      separators=(",", ":")).replace("<", "\\u003c"),
           json.dumps(bind_table, separators=(",", ":")),
           # Design's logic class, with DCLogic bound to our base and with
           # Design's example data lifted out to `MRB_DATA`. Everything else
           # about it is still verbatim.
           "/* No data reaches this page except through here, and there is no\n"
           "   fallback. A missing key is a THROWN ERROR and a blank page,\n"
           "   deliberately: the alternative to a blank page is one child's\n"
           "   marks shown to a different child, and a page that is confidently\n"
           "   wrong about a child's homework is worse than a page that is\n"
           "   plainly broken. */\n"
           "function MRB_DATA(k){var d=window.__MRB_DATA__;"
           "if(!d||!(k in d))throw new Error('student page: no data for \"'"
           "+k+'\"');return d[k];}\n"
           "var DCLogic = window.MrBadmusStudentRuntime.MrbLogic;\n"
           "var StreamableLogic = DCLogic;\n" + logic,
           # ⚠️ DECLARED, NOT CALLED. Whoever loads the data calls it, which is
           # what makes "the production page cannot mount without a data
           # source" a property of the file rather than a promise about it.
           "window.__MRB_MOUNT__ = function () {\n"
           "  var R = window.MrBadmusStudentRuntime;\n"
           "  var tpl = window.__MRB_TPL__;\n"
           "  return R.mount({\n"
           "    into: '#mrb-student',\n"
           "    template: {roots: R.applyBindings(tpl.roots, "
           "window.__MRB_BIND__, MRB_DATA), imports: tpl.imports},\n"
           "    imports: tpl.imports,\n"
           "    Component: Component,\n"
           "    props: {}\n"
           "  });\n"
           "};",
           tail)
    )


def write(path, body):
    _refuse(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)


def build():
    if not os.path.exists(TEMPLATES):
        raise SystemExit(
            "build_student_port.py: %s is missing. Run `python3 "
            "student_template.py` — the template and the logic are compiled "
            "out of Design's delivery, never typed." % TEMPLATES)
    tpls = json.load(open(TEMPLATES, encoding="utf-8"))

    print("\n🎓  build_student_port — Design's template and logic, "
          "on our runtime\n")

    css, sizes = ds_css()

    wanted = set()
    for spec in PAGES:
        t = tpls.get(spec["page"])
        if t:
            wanted |= referenced_tokens(t)
    css, topped = top_up(css, wanted, tpls)
    print("     %d token(s) referenced by the two pages; %d not in Design's "
          "bundle and topped up from shared/tokens.css%s"
          % (len(wanted), len(topped),
             (": " + ", ".join(topped)) if topped else ""))

    for out_dir in (SHARED_OUT, "shared"):
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, DS_CSS_NAME), "w",
                  encoding="utf-8") as fh:
            fh.write(css)
    print("     ✅ %-24s %7d bytes, %d sheet(s), linked and cached once"
          % (DS_CSS_NAME, len(css), len(sizes)))

    for spec in PAGES:
        tpl = tpls.get(spec["page"])
        if not tpl:
            raise SystemExit("build_student_port.py: %s has no entry for %r"
                             % (TEMPLATES, spec["page"]))

        # ⚠️ THE RULINGS COME FIRST, and the order is load-bearing in one
        # direction only: the class view's ruling deletes template nodes, and
        # the binding paths are index paths into `c`. Binding against the raw
        # template and then pruning would leave every path after node 275
        # pointing one sibling to the left — the class name would appear where
        # the term label belongs, and it would look like a data bug.
        logic, ruled_roots, n_rep, n_pruned = apply_rulings(
            spec["page"], tpl["logic"], tpl["roots"])
        ruled_tpl = {"roots": ruled_roots, "imports": tpl["imports"]}

        logic, data_literals = seam_logic(spec, logic)
        bind_table, bind_values = bindings_for(spec["page"], ruled_tpl)
        roots = scrub_roots(ruled_roots, bind_table)

        body = page_html(spec, tpl, roots, bind_table, logic, fixture=False)
        for out_dir in (SITE_OUT, MIRROR_OUT):
            write(os.path.join(out_dir, spec["out"]), body)

        fix_body = page_html(spec, tpl, roots, bind_table, logic, fixture=True)
        for out_dir in (SITE_OUT, MIRROR_OUT):
            write(os.path.join(out_dir, spec["fixture_out"]), fix_body)

        js = fixture_js(spec, spec["page"], data_literals, bind_values)
        for out_dir in (SHARED_OUT, "shared"):
            with open(os.path.join(out_dir, spec["fixture_js"]), "w",
                      encoding="utf-8") as fh:
                fh.write(js)

        # ⚑ ASSERTED, NOT ASSUMED — and precise about what is asserted.
        # ── what this build GUARANTEES, and what it only reports ─────────
        #
        # GUARANTEED, on pain of SystemExit: no bound identity string survives
        # in the template the production page ships. That is the half this
        # unit owns — the binding table and the scrub are both its work, so a
        # leak there is its bug and not a finding about somebody else's.
        #
        # REPORTED, not failed: Design's example data does not live only in
        # the class fields. `renderVals()` on the class view builds the
        # shout-outs inline (`{ who: 'MB', text: 'Best score in the class on
        # digestion this week.' }`), and the docket strings, and the leader's
        # figures. Lifting those is a different and larger job — they are
        # interleaved with computation rather than sitting in an initialiser —
        # and a build that REFUSED TO COMPLETE until it was done would simply
        # mean nothing shipped. So each is named, counted, and left.
        tpl_blob = json.dumps(roots, ensure_ascii=False)
        stuck = []
        for key, val in sorted(bind_values.items()):
            if not val.strip():
                continue
            if json.dumps(val, ensure_ascii=False) in tpl_blob:
                raise SystemExit(
                    "build_student_port.py: %s — the literal %r is STILL a "
                    "text node in the shipped template after the scrub, so "
                    "the binding for %r is cosmetic and the production page "
                    "carries the value anyway. The binding table and the "
                    "scrub disagree." % (spec["out"], val, key))
            for form in ("'%s'" % val.strip(), '"%s"' % val.strip()):
                if form in logic:
                    stuck.append((key, val.strip()))
                    break
        for key, val in stuck:
            print("        ⚠️  %-16s is bound in the markup but Design's logic "
                  "also writes %r inline (not a field — %s)"
                  % (key, val, "renderVals"))
        if stuck:
            print("        ⚠️  those are Design's example data too, welded "
                  "into method bodies rather than into initialisers. This "
                  "unit lifted the initialisers; the method bodies are a "
                  "separate seam and are NOT done.")

        if n_rep or n_pruned:
            print("        ⊕ MRB-275: %d ruled edit(s) to Design's logic, "
                  "%d template subtree(s) pruned — from student_rulings.py, "
                  "not from a hand edit to the built page"
                  % (n_rep, n_pruned))
        print("     ✅ %-24s %7d bytes  (%d template node(s), "
              "%d chars of Design's logic, 0 bytes of data)"
              % (spec["out"], len(body), count_nodes(roots), len(logic)))
        print("        %-21s %7d bytes  (+%d binding(s) applied at mount)"
              % (spec["fixture_out"], len(fix_body), len(bind_table)))
        print("        %-21s %7d bytes  (%d field(s) lifted from the logic, "
              "%d identity string(s) from the markup)"
              % (spec["fixture_js"], len(js),
                 len(spec["fields"]) + len(spec["state_fields"]),
                 len(bind_values)))

    # ── the runtime is mirrored HERE, not left to the KS4 generator ──────
    #
    # ⚑ THIS COST A RED GATE. Both pages load `/shared/student-runtime.js`, and
    # until now nothing in this build put it there — `generate_site_v5.py`
    # glob-copies `shared/` into the output, so the served copy was whatever
    # the last full site build happened to leave. Editing the runtime and
    # re-running this build therefore produced a page that loaded the OLD
    # runtime, and the failure arrived as `R.applyBindings is not a function`
    # from a file that plainly contained `applyBindings`.
    #
    # A build that emits a page depending on a file it does not publish is a
    # build with a hidden prerequisite. This one publishes it.
    for name in (RUNTIME_JS_NAME, LIVE_JS_NAME):
        src = os.path.join("shared", name)
        if not os.path.exists(src):
            raise SystemExit(
                "build_student_port.py: shared/%s does not exist, and both "
                "pages load it. Without it they mount nothing at all — which "
                "is the correct failure and still a failure." % name)
        text = open(src, encoding="utf-8").read()
        with open(os.path.join(SHARED_OUT, name), "w", encoding="utf-8") as fh:
            fh.write(text)
        print("     ✅ %-24s %7d bytes  (%s)"
              % (name, len(text),
                 "STUB — throws; the live data source is not wired yet"
                 if "not wired yet" in text else "published, not assumed"))


    print("\n     → %s/  and  %s/  (mirror)" % (SITE_OUT, MIRROR_OUT))
    print("\n     ⚠️  *-ported.html carry NO data and do not mount themselves; "
          "%s does that.\n         *-fixture.html carry Design's example data "
          "and are what the gates drive.\n         Neither is a candidate to "
          "replace a live page.\n" % LIVE_JS_NAME)


if __name__ == "__main__":
    sys.path.insert(0, REPO)
    build()
