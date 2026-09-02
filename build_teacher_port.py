#!/usr/bin/env python3
"""build_teacher_port.py — the PORTED teacher dashboard: Claude Design's own
markup and Design's own logic class, rendered by shared/student-runtime.js.

    python3 build_teacher_port.py

Writes:

    mrbadmus_site/shared/teacher-ds.css          Design's six stylesheets, once
    mrbadmus_site/shared/teacher-fixture-*.js    Design's example data, per page
    mrbadmus_site/teacher/<six pages>.html       production — NO data in them
    mrbadmus_site/teacher/<six>-fixture.html     the gates' pages
    teacher/*.html, shared/*                     (mirror)

── SIX PAGES OUT OF ONE FILE ────────────────────────────────────────────

Design's teacher delivery is ONE `.dc.html` holding SEVEN SCREENS behind a
top-level `sc-if` on `s.screen`, plus four overlays. That is the right shape
for a prototype and the wrong shape for a website: a teacher who bookmarks a
class, or presses Back, or opens a child's page in a second tab, is asking for
a URL, and a single-page prototype has one.

So each emitted page keeps ITS OWN screen node and PRUNES the rest, and
every screen-changing handler in Design's logic is rewritten to a real
navigation (see `NAV` in teacher_rulings.py). Pruning is BY NODE INDEX and
REFUSES when an index is not found — a prune that silently matched nothing is
how a screen ships twice, on a page that looks correct because the second
screen is below the fold.

── TWO FILES PER PAGE, BECAUSE ONE CANNOT BE BOTH ───────────────────────

Exactly the split `build_student_port.py` documents, and for a sharper reason
here: Design's sample is fifty-four invented children with invented marks. A
single page that renders it when the database is quiet is a page that shows a
teacher a class they do not teach, with names that look real, the first time a
fetch fails.

  <page>.html          Design's markup and Design's logic with every data
                       literal lifted out. It DEFINES `window.__MRB_MOUNT__`
                       and DOES NOT CALL IT, and it ends by loading
                       `shared/teacher-live.js`. There is no fixture in this
                       file to fall back to, so there is no code path that
                       could fall back to one.
  <page>-fixture.html  the same bytes but for its banner and its last two
                       script tags, which load Design's extracted example data
                       and mount. This is what the behaviour gate drives.

── WHAT IS DESIGN'S, AND WHAT IS OURS ───────────────────────────────────

Design's: the markup (compiled by `student_template.py`, not retyped), the
behaviour (Design's logic class, extracted verbatim), the styling (Design's own
six stylesheets in Design's own link order). Ours: `shared/student-runtime.js`,
which is shared with the student pages and is not edited here, and the rulings
in `teacher_rulings.py`.

── ⛔ THE THREE LIVE PAGES ARE GENERATED OUTPUT NOW ──────────────────────

`teacher/classes.html`, `teacher/class-detail.html` and
`teacher/student-detail.html` are written by this build. The hand-written
originals are retired to `docs/ks3/retired/` under 24 Aug 2026 — out of
`teacher/`, so the generator does not publish them, and git holds them
regardless.

⛔ `teacher/import.html` IS THE EXCEPTION AND IS NOT THIS BUILD'S. It was
ported on 24 Aug 2026 and restored, byte for byte, the same day: Design's
import screen is a mock, the port kept its presentation and lost the CSV /
Excel engine behind it, and a teacher could not import students. It is
hand-written source again, it is named in `_REFUSED`, and the reasoning is
`IMPORT_NOT_PORTED` in teacher_rulings.py. Design's "Import students"
button still navigates to it and that link is correct.

⚠️ NONE OF THE SIX IS HAND-EDITABLE, and the warning at the top of each is
not a formality: a fix typed into one survives exactly until the next build.
That is not hypothetical — it is precisely what happened to the MRB-275
rulings on the student pages, and `student_rulings.py` exists to recover from
it. Changes to Design's logic belong in `teacher_rulings.py`, changes to what
the page renders belong in `shared/teacher-live.js`, and changes to the markup
belong to Design.
"""

import hashlib
import html
import json
import os
import re
import subprocess
import sys

# ⊕ IMPORTED, NOT RETYPED — the same reasoning build_student_port.py records
# at length. `build_ks3.py` owns the one substitution that gets cache-busting
# right (idempotent against a stale `?v=`, anchored on the trailing quote so a
# short name cannot match inside a longer one, agnostic about `src` vs `href`).
# generate_site_v5.py carries a second inline copy; a third here would be the
# copy that drifts.
from build_ks3 import stamp_versions

REPO = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join("docs", "ks3", "design-reference", "teacher")

# ⚠️ THE TEACHER'S OWN VENDORED BUNDLE, NOT THE STUDENT'S, and they are
# currently byte-identical — checked, same directory name, same six sheets. It
# is still read from here and emitted as its own file, because the day Design
# bumps the teacher design system is the day a shared file would silently
# restyle every student's class page. Two deliveries, two bundles, two
# stylesheets.
DS = os.path.join(REF, "source", "_ds",
                  "mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1")

SITE_OUT = os.path.join("mrbadmus_site", "teacher")
MIRROR_OUT = "teacher"

# ⚑ THE FIXTURES LIVE OUTSIDE `teacher/`, AND THIS IS LOAD-BEARING.
#
# They render Design's invented school — twelve classes, fifty-four children's
# names, a mark for every one — and `/teacher/*` has no edge auth, so anything
# inside `teacher/` reaches mrbadmus.com. Twelve of them did.
#
# ⚠️ TWO EARLIER ATTEMPTS AT THIS WERE WRONG, and the second was worse than
# the first. Deleting them from the output after the fact held only until the
# next generator run. Adding `ignore_patterns("*fixture*")` to
# generate_site_v5's teacher copytree then DELETED THEM FROM SOURCE, because
# that generator round-trips `mrbadmus_site/<dir>` back over `./<dir>` — and
# the safety net that exists to catch exactly that ("the round-trip would
# delete these from source") had been silenced by the same change, by me, to
# stop it reporting the withheld files. Silencing a guard to make a change
# look clean is how the change gets to be wrong quietly.
#
# So the fixtures are not in a published directory at all. `generate_site_v5`
# copies `shared/`, `teacher/` and `student/`; a directory it has never heard
# of is neither published nor round-tripped, and nothing has to be excluded,
# ignored or silenced for that to be true.
FIXTURE_OUT = "teacher_fixtures"
SHARED_OUT = os.path.join("mrbadmus_site", "shared")
RETIRED = os.path.join("docs", "ks3", "retired")

TEMPLATES = "student_templates.json"
TPL_KEY = "teacher"

DS_CSS_NAME = "teacher-ds.css"
DS_CSS_URL = "/shared/" + DS_CSS_NAME
SERVED_FONTS = "/shared/fonts/"

RUNTIME_JS_NAME = "student-runtime.js"
LIVE_JS_NAME = "teacher-live.js"
LIVE_JS_URL = "/shared/" + LIVE_JS_NAME

# ⊕ MRB-303 J2 — the scope-gated Admin entry. See `admin_nav` in page_html.
ADMIN_NAV_JS_NAME = "teacher-admin-nav.js"

# ── pages this build REFUSES to write ────────────────────────────────────
#
# ⚠️ NOT A CONVENTION — A GUARD, and it is the same one `build_student_port`
# carries. Nothing in `teacher/` outside the six below is this build's, and
# writing over a hand-written source file with generated output is the exact
# trap that ate the MRB-275 rulings: the live page LOOKS hand-editable,
# somebody hand-edits it, and the next rebuild reverts a teacher-facing fix
# without a word.
#
# ⛔ `import.html` IS ON THIS LIST AND MUST STAY ON IT. It is the hand-written
# CSV/Excel wizard — papaparse, SheetJS, column mapping, per-class settings,
# the dry run and the confirm POST — and this build ported it once, on
# 24 Aug 2026, into a page that carried Design's three-step PRESENTATION and
# none of the engine. A teacher could not import students. It was restored
# from `docs/ks3/retired/teacher-import-2026-08-24-retired.html` the same day
# and taken out of `PAGES`; this entry is what stops it being written over
# again by a future run that adds the row back without reading
# `IMPORT_NOT_PORTED` in teacher_rulings.py.
_REFUSED = {"import.html"}

# ── the five `teacher-live.js` will load for itself ──────────────────────
#
# ⚑ READ build_student_port.py's LONG COMMENT ON THIS. It closed a real
# four-hour defect that was hitting students, and every word of it applies
# here. Measured on mrbadmus.com: a page under `/teacher/` is served
# `max-age=0, must-revalidate` and every asset under `/shared/` is served
# `max-age=14400` — four hours. A page that links an unstamped script gets
# TODAY's HTML with YESTERDAY's JavaScript for up to four hours after every
# deploy, and the failure surfaces as a thrown key error the page reports as
# a transient "try again in a moment".
#
# Stamping only the tags in the HTML is not enough: `teacher-live.js` loads
# more scripts itself, through `<script>` elements this build never writes.
# They cannot be stamped by rewriting `teacher-live.js` (it is hand-written
# source, and rewriting the published copy would make the deployed bytes
# differ from the repo's). So the BUILD publishes the map and the RUNTIME
# reads it: `window.__MRB_ASSET_V__`, BARE NAME → hash.
#
# ⚠️ KEYED ON THE BARE NAME, ON PURPOSE. Keyed on the full `/shared/<name>`
# URL it would be rewritten by generate_site_v5.py's own cache-bust pass —
# that regex matches the path wherever it occurs, including inside a JSON key
# — turning the key into `"/shared/teacher-data.js?v=…"`, which
# `teacher-live.js` would then fail to look up. Silent, and it would look
# like the stamp simply had no effect.
# ⊕ `teacher-live.js` IS IN THE PUBLISHED MAP TOO, even though the page links
# it directly and `stamp_versions` already stamps that tag. It costs one entry
# and it closes the case where the runtime reaches for its own version — the
# map is the one place a bare name resolves, and a name missing from it
# resolves to nothing rather than to an error.
# ⊕ MRB-303 J2 — `teacher-admin-nav.js` IS IN THIS TUPLE BUT IS NOT ONE OF
# THE FIVE. The other entries are loaded by `teacher-live.js`'s `loadDeps()`
# and are here so the RUNTIME can resolve their hash; this one is linked by a
# real `<script>` tag that `page_html` emits (see `admin_nav` on the specs
# below), so `stamp_versions` would stamp it either way. It is listed anyway
# for the OTHER half of what this tuple buys: `_verify_stamps` re-hashes every
# name in it from disk, in both published trees, and refuses to finish if a
# stamp names bytes that are not what will be served. A tag that is stamped
# but never verified is exactly the asset that goes stale quietly.
STAMPED_DEPS = ("config.js", "class-entry.js", "teacher-guard.js",
                "teacher-data.js", "shoutouts.js", "teacher-admin-nav.js")


def asset_hash(text):
    """The repo's one stamping scheme: md5 of the bytes, first 8 hex chars.

    Identical to `build_ks3.asset_versions`, to generate_site_v5.py's inline
    pass and to `build_student_port.asset_hash`, which is what makes
    `class-entry.js?v=8be18391` read the same on a teacher page, a student
    page and a KS4 page. Four writers, one number.
    """
    if isinstance(text, str):
        text = text.encode("utf-8")
    return hashlib.md5(text).hexdigest()[:8]


# ── the six pages ────────────────────────────────────────────────────────
#
# `overlays` is what each page KEEPS. Everything else — the other six screens
# and the overlays not listed — is pruned by index, and a missing index stops
# the build.
#
# ⚠️ `setWorkOpen` IS KEPT BY NONE OF THEM. See `DEAD` in teacher_rulings.py:
# creating an assignment has no write path anywhere in the data layer, so the
# sheet is a control that would collect four answers, show a confirmation and
# set nothing.
#
# ⊕ RULED 24 Aug 2026 — `bulkOpen` IS GONE FROM `classes.html`. It used to be
# kept there because the brief named it, with a note that it had no opener.
# That note was right and keeping it was not: `openBulk` is on nodes 104 and
# 196 (class screen) and 232 (student screen) and NOWHERE on the classes
# screen, so the overlay was a sheet a teacher could never open, shipped on
# every load of the dashboard's first page. Markup that cannot be reached is
# not a feature in waiting; it is weight and a false positive for anybody
# reading the page. The other two pages keep it because they can open it.
#
# `retire` names the hand-written original this page replaces. Three of the
# six have one; `assignment.html`, `digest.html` and `insights.html` are new
# surfaces with no hand-written predecessor at all.
PAGES = [
    dict(screen="classes", node=30, out="classes.html", admin_nav=True,
         fixture_out="classes-fixture.html",
         fixture_js="teacher-fixture-classes.js",
         empty_out="classes-empty-fixture.html",
         empty_js="teacher-fixture-classes-empty.js",
         title="My classes \u00b7 MrBadmusAI",
         # ⊕ NO `bulkOpen`. See the note above the list: `openBulk` is on
         # nodes 104/196 (class) and 232 (student) and nowhere on the classes
         # screen, so on this page the sheet was markup that could never open.
         overlays=("searchOpen", "hasToast"),
         retire="classes.html"),
    dict(screen="class", node=87, out="class-detail.html", admin_nav=False,
         fixture_out="class-detail-fixture.html",
         fixture_js="teacher-fixture-class-detail.js",
         empty_out="class-detail-empty-fixture.html",
         empty_js="teacher-fixture-class-detail-empty.js",
         title="Class \u00b7 MrBadmusAI",
         overlays=("searchOpen", "bulkOpen", "hasToast"),
         retire="class-detail.html"),
    dict(screen="student", node=222, out="student-detail.html", admin_nav=True,
         fixture_out="student-detail-fixture.html",
         fixture_js="teacher-fixture-student-detail.js",
         empty_out="student-detail-empty-fixture.html",
         empty_js="teacher-fixture-student-detail-empty.js",
         title="Student \u00b7 MrBadmusAI",
         overlays=("searchOpen", "bulkOpen", "hasToast"),
         retire="student-detail.html"),
    dict(screen="marking", node=258, out="assignment.html", admin_nav=True,
         fixture_out="assignment-fixture.html",
         fixture_js="teacher-fixture-assignment.js",
         empty_out="assignment-empty-fixture.html",
         empty_js="teacher-fixture-assignment-empty.js",
         title="Assignment \u00b7 MrBadmusAI",
         overlays=("searchOpen", "hasToast"),
         retire=None),
    dict(screen="digest", node=312, out="digest.html", admin_nav=True,
         fixture_out="digest-fixture.html",
         fixture_js="teacher-fixture-digest.js",
         empty_out="digest-empty-fixture.html",
         empty_js="teacher-fixture-digest-empty.js",
         title="Weekly digest \u00b7 MrBadmusAI",
         overlays=("hasToast",),
         retire=None),
    # ⛔ THERE IS NO `import` ROW HERE, AND ITS ABSENCE IS A RULING.
    # See `IMPORT_NOT_PORTED` in teacher_rulings.py: `teacher/import.html` is
    # the hand-written CSV/Excel wizard and stays hand-written. Design's
    # import screen (node 346) is still in `SCREENS`, because every OTHER page
    # has to PRUNE it — it is simply never the screen a page keeps.
    dict(screen="insights", node=401, out="insights.html", admin_nav=True,
         fixture_out="insights-fixture.html",
         fixture_js="teacher-fixture-insights.js",
         empty_out="insights-empty-fixture.html",
         empty_js="teacher-fixture-insights-empty.js",
         title="Charts \u00b7 MrBadmusAI",
         overlays=("hasToast",),
         retire=None),
]


_BANNER = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED — do not edit. `python3 build_teacher_port.py`
  ══════════════════════════════════════════════════════════════════════════

  %s, PORTED: Claude Design's own template and Design's own logic class,
  rendered by shared/student-runtime.js. No React and none of Design's
  `support.js` ships here — that was ruled on 20 Aug 2026 for the student
  pages and this port follows it.

  The markup is not retyped and neither is the behaviour. Both are extracted
  from docs/ks3/design-reference/teacher/ by student_template.py, so the only
  way this can differ from Design's file is if Design's file changed.

  ⊕ THIS IS THE LIVE PAGE, as of 24 Aug 2026 (MRB-287). It follows that this
  file is NOT hand-editable, and the warning above is not a formality: a fix
  typed in here survives exactly until the next build. Changes to Design's
  logic belong in teacher_rulings.py, changes to what the page renders belong
  in shared/teacher-live.js, and changes to the markup belong to Design.

  THERE IS NO DATA IN THIS FILE. Design's delivery is a SAMPLE — twelve
  invented classes, fifty-four invented children and every mark on every
  screen derived from an FNV hash of a class id. All of it has been lifted out
  into `window.__MRB_DATA__`, and every read of it goes through `MRB_DATA(k)`
  or `MRB_PICK(map, id)`, both of which THROW when what they ask for is
  absent. So this page cannot show a teacher a class they do not teach: with
  no data source loaded it renders nothing at all and says why. The data
  arrives from %s, and from nowhere else.

  Its twin, %s, is this same file with two differences and no others — this
  comment, and the script tags at the end, where it loads Design's own
  extracted example values and mounts. That twin is what the gates drive,
  which is how Design's sample can still be exercised in full without being
  reachable from here.
  ══════════════════════════════════════════════════════════════════════════
-->
"""

_BANNER_FIXTURE = """<!--
  ══════════════════════════════════════════════════════════════════════════
  GENERATED — do not edit. `python3 build_teacher_port.py`
  ══════════════════════════════════════════════════════════════════════════

  %s, PORTED — THE FIXTURE PAGE. The same file as %s but for this comment and
  the script tags at the end: this one loads Design's own extracted example
  data and mounts, that one loads the live data source and does not.

  ⛔ NOT A CANDIDATE FOR ANY LIVE PATH, and not because it is unfinished — it
  is twelve invented classes and fifty-four invented children, hard-coded, for
  every visitor. It exists so the gates have something with known values to
  drive. A gate that drove the production page would be asserting against
  whatever the database happened to hold that morning.
  ══════════════════════════════════════════════════════════════════════════
-->
"""


def _refuse(path):
    if os.path.basename(path) in _REFUSED:
        raise SystemExit(
            "build_teacher_port.py REFUSES to write %s — that is a "
            "hand-written teacher page, not this build's output." % path)


# ══════════════════════════════════════════════════════════════════════════
#  Design's stylesheets
# ══════════════════════════════════════════════════════════════════════════

def ds_css():
    """Design's six stylesheets, in Design's own link order, as one file.

    The order is not chosen here — it is read off the compiled `sheets` key,
    which is the order Design's own `<link>` tags appear in. A cascade
    reordered by this build is a cascade Design never checked.

    ⚠️ NOT THE SITE'S OWN COPIES, for the reason `build_student_port.ds_css`
    records: `shared/tokens.css` and `shared/ks3.css` have both grown well
    past the versions in Design's bundle, so linking the site's files would
    give the page a cascade Design never drew.

    ⚠️ AND NOT `student-ds.css` EITHER, even though the two bundles are
    byte-identical today. Sharing the file would mean a teacher-only design
    system bump silently restyling every student's class page, which is a
    coupling nobody asked for and nobody would look for.
    """
    order = ["tokens/src-styles-tokens.css", "tokens/shared-tokens.css",
             "tokens/shared-ks3.css", "fonts/fonts.css", "_ds_bundle.css",
             "styles.css"]
    out, sizes = [], []
    for rel in order:
        path = os.path.join(DS, rel)
        if not os.path.exists(path):
            raise SystemExit("build_teacher_port.py: missing %s" % path)
        css = open(path, encoding="utf-8").read()
        if rel.endswith("fonts.css"):
            # The faces point at `./` inside the bundle; the site self-hosts
            # every one of the seven at /shared/fonts/.
            css = css.replace("./", SERVED_FONTS)
        out.append("/* ── %s ── */\n%s" % (rel, css))
        sizes.append((rel, len(css)))
    return "\n\n".join(out), sizes


# ── every token the page references must resolve ──────────────────────────
#
# ⚑ THIS EXISTS BECAUSE ONE DID NOT, ON THE STUDENT PAGES, AND THE PAGE STILL
# LOOKED FINE. A ruled label pointed at `--ks3-ok-dark`, minted after Design's
# bundle was cut; it resolved to the INHERITED ink instead, and a green word
# quietly became a black one with no error and no warning anywhere.
#
# An undefined custom property is the quietest failure CSS has. So the build
# collects every `var(--…)` the template and the logic reference, checks each
# against what the stylesheets actually define, and tops up the difference
# from the site's own `shared/tokens.css` — BY NAME, read out of that file,
# never retyped. Anything still unresolved stops the build.

def referenced_tokens(tpl):
    """Every `--custom-property` the template or the logic asks for."""
    blob = json.dumps(tpl["roots"]) + tpl["logic"] + json.dumps(tpl["imports"])
    return set(re.findall(r"var\(\s*(--[a-zA-Z0-9-]+)", blob))


def defined_tokens(css, tpl=None):
    """Every custom property the page can resolve — from CSS AND from markup.

    ⚠️ THE MARKUP HALF IS NOT OPTIONAL. Design declares tokens inline on the
    design root's own `style` attribute rather than in a stylesheet — node 9
    opens `--rowpad:` that way — and a scan that read only the stylesheets
    would call them undefined and stop the build on a token that resolves
    perfectly well.
    """
    found = set(re.findall(r"(--[a-zA-Z0-9-]+)\s*:", css))
    if tpl:
        found |= set(re.findall(r"(--[a-zA-Z0-9-]+)\s*:",
                                json.dumps(tpl["roots"])))
    return found


def top_up(css, wanted, tpl):
    """Define, from shared/tokens.css, any token the bundle is missing."""
    have = defined_tokens(css) | defined_tokens("", tpl)
    missing = sorted(wanted - have)
    if not missing:
        return css, []
    site = open(os.path.join("shared", "tokens.css"), encoding="utf-8").read()
    lines, still = [], []
    for name in missing:
        m = re.search(r"%s\s*:\s*([^;]+);" % re.escape(name), site)
        if m:
            lines.append("  %s: %s;" % (name, m.group(1).strip()))
        else:
            still.append(name)
    if still:
        raise SystemExit(
            "build_teacher_port.py: %d token(s) the teacher pages reference "
            "are defined NOWHERE — not in Design's bundle and not in "
            "shared/tokens.css: %s.\n"
            "  An undefined custom property does not error; it falls back to "
            "the inherited value and the page looks almost right. Define them "
            "or stop referencing them." % (len(still), ", ".join(still)))
    block = ("\n\n/* ── minted since Design's bundle, read out of "
             "shared/tokens.css ──\n"
             "   Values are COPIED FROM the site's token file at build time\n"
             "   rather than retyped, so they cannot drift from it. */\n"
             ":root,\n.rd[data-mode=\"ks3\"] {\n%s\n}\n" % "\n".join(lines))
    return css + block, missing


# ══════════════════════════════════════════════════════════════════════════
#  Design's logic, seamed
# ══════════════════════════════════════════════════════════════════════════

def _balanced(src, start, opener, closer):
    """Index just past the `closer` matching the `opener` at `start`.

    A BALANCED SCAN and not a regex, because every literal this has to walk
    contains its own terminator: `NAMES` holds apostrophes, `TITLES` holds
    braces inside strings, and `chartFor` holds four hundred lines of nested
    object literals. A regex that stopped at the first `}` would truncate a
    method in the middle of a string and produce a syntax error four hundred
    lines further down, where nothing would point back here.
    """
    depth, i, n = 0, start, len(src)
    while i < n:
        ch = src[i]
        if ch in "'\"`":
            q, i = ch, i + 1
            while i < n:
                if src[i] == "\\":
                    i += 2
                    continue
                if src[i] == q:
                    break
                i += 1
            i += 1
            continue
        if src.startswith("//", i):
            j = src.find("\n", i)
            i = n if j < 0 else j + 1
            continue
        if src.startswith("/*", i):
            j = src.find("*/", i)
            i = n if j < 0 else j + 2
            continue
        if ch == opener:
            depth += 1
        elif ch == closer:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise SystemExit("build_teacher_port.py: unbalanced %r from offset %d "
                     "in Design's logic." % (opener, start))


# ── ⊕ MRB-306 · A NAV RULING ANCHORS ON A NAME, NOT ON ITS NEIGHBOURS ────
#
# ⛔ WHAT BROKE. Every `NAV` entry used to carry `frm`: a VERBATIM span of
# Design's logic, replaced exactly once. Six of the sixteen are loop-scoped
# closures called `open`, and their bodies are byte-identical to each other —
# `open: () => this.setState({ screen: 'student', studentId: r.id })` is four
# different controls in four different builders. So `frm` was PADDED with the
# lines that happened to follow it (`\n      };\n    });\n\n    const
# paperRow`) purely to tell them apart.
#
# That padding is not part of the ruling. It is a photograph of Design's file
# at one moment, and it breaks whenever she touches a line NEAR the handler
# rather than the handler itself. On the v3 delivery ELEVEN of the sixteen
# stopped matching, and not one of them because the handler had changed: she
# added a Today screen above them and the neighbours moved.
#
# ⚑ WHAT REPLACES IT. `anchor`, in one of these forms:
#
#     anchor=dict(key="goClass")                 a top-level handler
#     anchor=dict(builder="cards", key="open")   a closure inside a `.map(`
#     anchor=dict(method="renderVals",           a statement inside a method
#                 key="const flagged")            ⊕ MRB-306
#     anchor=dict(method="renderVals",           a property inside a property
#                 key="klass.meta")               ⊕ MRB-306
#
# The builder form is the whole point: it says WHICH LIST the row belongs to,
# which is the thing that actually distinguishes six identical closures, and
# it is a name Design chose deliberately rather than a line she happened to
# type underneath. `cards`, `roster`, `assignments`, `grid`, `stHistory`,
# `digestRows`, `results` all survived v2 → v3 unrenamed while every one of
# their `frm` spans died.
#
# ⚠️ EXACTLY ONE MATCH IS REQUIRED, and that is the safety property, not a
# convenience. A key form that matched twice would rewire whichever came
# first and leave the other a dead control; a builder form that matched zero
# means Design has renamed the list, and the ruling must be re-read by a
# human before it is re-pointed. Both refuse the build, by name.
#
# `frm` still works, unchanged, for any entry that has no `anchor` — this
# mechanism was added incrementally and the two paths are allowed to coexist.
#
# ⊕ 1 Sep 2026 (MRB-306) — `LOGIC` TAKES ANCHORS TOO, and the same failure
# mode is what put it there. `LOGIC` was 55 exactly-once source replacements
# and NINE stopped matching on Design's v3. Five of the nine changed nothing
# a ruling was about: `const swSel` was followed by one blank line instead of
# two, `const flagged` lost a `.length`, `late: late,` became the `late,`
# shorthand one line above the span's real target, `state = {` gained a key,
# `meta` gained a subject. Three genuinely need the week rail rebuilt. One —
# `longMeta` — was renamed, and is re-expressed onto the key that replaced it.
#
# An anchored `LOGIC` entry writes its anchor WHERE `frm` GOES: the first
# element of the triple is either a string (verbatim source, the old path) or
# a dict (an anchor). Nothing else about the entry changes, and the 46 whose
# `frm` is genuinely self-identifying were LEFT ALONE — converting a ruling
# that already works is risk with no reward.


def _logic_lines(logic):
    """Design's logic as [(start, end, text, depth_after)], one per line.

    `start`/`end` are byte offsets into `logic`; `end` excludes the newline.
    `depth_after` is the bracket nesting depth at the END of that line.

    ⚠️ STRING- AND COMMENT-AWARE, because a bare bracket count is wrong on
    this file and wrong QUIETLY. `this.ping('No students in ' + c.code + '
    yet')` sits inside the digest builder and `/* ── Today ── */` sits
    between two others; a scan that counts a bracket inside either drifts by
    one and then swallows every builder after it, so the block it hands back
    would be the whole rest of the file and the "exactly one match" check
    would refuse a handler that is perfectly fine.
    """
    out, depth, i, n = [], 0, 0, len(logic)
    in_block_comment = False
    line_start, line_no_end = 0, None
    while i <= n:
        if i == n or logic[i] == "\n":
            out.append((line_start, i, logic[line_start:i], depth))
            line_start = i + 1
            i += 1
            continue
        ch = logic[i]
        if in_block_comment:
            if logic.startswith("*/", i):
                in_block_comment = False
                i += 2
            else:
                i += 1
            continue
        if logic.startswith("//", i):
            j = logic.find("\n", i)
            i = n if j < 0 else j
            continue
        if logic.startswith("/*", i):
            in_block_comment = True
            i += 2
            continue
        if ch in "'\"`":
            q, i = ch, i + 1
            while i < n:
                if logic[i] == "\\":
                    i += 2
                    continue
                if logic[i] == q:
                    break
                i += 1
            i += 1
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        i += 1
    return out


def _anchor_refusal(head, name, anchor, what, tail):
    """The one refusal every anchor failure routes through.

    Same shape as the `frm` refusal it replaces: name the ruling, say what
    was looked for, say what was found, and say where to fix it. The two
    lists differ ONLY in the closing paragraph, because they fail
    differently — see the two wrappers below.
    """
    return SystemExit(
        "build_teacher_port.py: %s for %r %s.\n"
        "    anchor = %r\n"
        "  %s" % (head, name, what, anchor, tail))


def _nav_refusal(handler, anchor, what):
    """A NAV anchor that resolved to nothing, or to two things.

    A NAV rewire that silently does not happen leaves a button that changes
    `s.screen` on a page where `s.screen` is fixed — it draws perfectly and
    does nothing, and no static check downstream can see that.
    """
    return _anchor_refusal(
        "the navigation ruling", handler, anchor, what,
        "Design has redrawn or renamed that handler. Re-anchor it in "
        "teacher_rulings.NAV — do NOT drop it, and do NOT widen the anchor "
        "until it matches something: a skipped rewire is a dead control that "
        "every gate calls green.")


def _logic_refusal(ruling, anchor, what):
    """⊕ 1 Sep 2026 (MRB-306) — the same failure, for an anchored LOGIC entry.

    Word for word the paragraph the `frm` path has always printed, because
    the consequence is identical and the reader is the same person: a LOGIC
    ruling that matches nothing ships a page in which Mide's correction is
    simply absent, and every gate downstream calls that green.
    """
    return _anchor_refusal(
        "an MRB-287 ruling", ruling, anchor, what,
        "The ruling is Mide's and still stands. Design has redrawn that "
        "span; re-anchor it in teacher_rulings.LOGIC rather than dropping "
        "it, and do NOT hand-edit the built page — that is exactly how the "
        "MRB-275 rulings were lost.\n"
        "  ⚠️ SKIPPING IS NOT AVAILABLE. A ruling that silently matched "
        "nothing is the same failure as the hand-edit it replaces: the "
        "build goes green and the ruling is not in the page.")


# A key segment shaped like a JS identifier is a PROPERTY (`meta` → `meta:`);
# anything else is a STATEMENT, matched as a literal line prefix (`const
# flagged`). `_PATH` is the dotted form — a property inside a property.
_IDENT = re.compile(r"^[A-Za-z_$][A-Za-z0-9_$]*$")
_PATH = re.compile(r"^[A-Za-z_$][A-Za-z0-9_$]*(\.[A-Za-z_$][A-Za-z0-9_$]*)+$")


# The ceiling on a resolved anchor span. Every anchored ruling in
# teacher_rulings.py spans at most seven lines; see the note in
# `resolve_anchor` for the 97-line runaway this exists to refuse.
_MAX_ANCHOR_LINES = 40


def resolve_anchor(logic, spec, refusal=_nav_refusal):
    """(start, end) of the source span one `anchor` names.

    `start` is the beginning of the anchored line, at column 0, so the caller
    can read Design's indentation off it. `end` is just past the last
    character of the span, excluding its newline.

    ── SCOPES ───────────────────────────────────────────────────────────
    `method="renderVals"`   the body of that method, closer excluded
    `builder="cards"`       the `const cards = ….map(…)` declaration
    both                    the builder, looked for only inside the method
    neither                 all of Design's logic

    ── KEYS ─────────────────────────────────────────────────────────────
    `key="open"`            a PROPERTY: the line beginning `open:`
    `key="klass.meta"`      `meta:` inside the `klass:` object, and nowhere
                            else — the narrowing that lets one anchor pick
                            `klass.meta` out of a `renderVals` that returns
                            four different `meta:` lines
    `key="const flagged"`   a STATEMENT: the line beginning with that text

    The two shapes END differently, and that is the whole reason they are
    distinguished. A property ends at the first line back at its starting
    depth that is FINISHED AS A PROPERTY — it ends with a comma, or the line
    after it closes the enclosing object. Bracket balance alone is not
    enough for that, and the class card is the proof:

        open: () => c.n > 0                                     ← balanced
          ? this.setState({ screen: 'class', classId: c.id })   ← balanced
          : this.setState({ screen: 'import', importStep: 1 }), ← balanced

    Every line closes what it opens; a depth-only rule would replace the
    first and leave a ternary with no consequent, which is a syntax error on
    six pages. A STATEMENT ends at the first line back at its starting depth
    that ends with `;` — which is what carries `state = { … };` and any
    other multi-line initialiser across its own closing brace.

    ⚠️ EXACTLY ONE MATCH IS REQUIRED at every step, scopes included. That is
    the safety property and not a convenience; never widen it, and never add
    a first-match-wins path.
    """
    name = spec.get("_name", "?")
    anchor = spec["anchor"]
    key = anchor["key"]
    lines = _logic_lines(logic)

    def refuse(what):
        return refusal(name, anchor, what)

    # `decl` is the line that OPENED the current scope — a builder
    # declaration or a container property. It is never itself the match.
    # `scope` is how a refusal NAMES where it looked, innermost first.
    lo, hi, decl, scope = 0, len(lines), None, []

    if "method" in anchor:
        lo, hi = _method_scope(lines, anchor["method"], refuse)
        scope.append("`%s()`" % anchor["method"])

    if "builder" in anchor:
        builder = anchor["builder"]
        decl_re = re.compile(r"^\s*const\s+%s\s*=" % re.escape(builder))
        hits = [n for n in range(lo, hi) if decl_re.match(lines[n][2])]
        # ⚠️ `.map(` IS PART OF THE ANCHOR, not a sanity check. `const
        # chaseAll = [];` … `forEach(… push(…))` builds rows the same way and
        # would answer to a bare `const <name> =`; the ruling says a MAP
        # builder, so a list built some other way must refuse rather than be
        # silently accepted at the wrong extent.
        #
        # ⚠️ AND THE LOOK-AHEAD STOPS AT THE END OF THE DECLARATION, NOT AFTER
        # SOME NUMBER OF LINES. Design declares `const roster` TWICE — once as
        # `this.rosterFor(k)` inside `gridFor()` and once as the class
        # screen's `rosterSorted.map(…)` — and the line directly under the
        # first is `const diff = this.STEMS.map(…)`. A fixed-window scan sees
        # that neighbour's `.map(` and calls the wrong `roster` a builder,
        # which is exactly the neighbour-sensitivity this mechanism removes.
        mapped = []
        for n in hits:
            head = []
            for _, _, text, _ in lines[n:_builder_block_end(lines, n, refuse,
                                                            builder)]:
                head.append(text)
                if ".map(" in text:
                    break
            if ".map(" in "\n".join(head):
                mapped.append(n)
        if len(mapped) != 1:
            raise refuse(
                "anchors on a `.map(` builder named %r, and Design's logic "
                "declares %d of them, not one" % (builder, len(mapped)))
        n = mapped[0]
        lo, hi, decl = n, _builder_block_end(lines, n, refuse, builder), n
        scope.append("`const %s`" % builder)

    segs = key.split(".") if _PATH.match(key) else [key]
    for seg in segs[:-1]:
        n = _one_line(lines, lo, hi, seg + ":", decl, scope, refuse)
        lo = n
        hi = _prop_span_end(lines, n, seg + ":", refuse) + 1
        decl = n
        scope.append("`%s`" % seg)

    last = segs[-1]
    prop = bool(_IDENT.match(last))
    want = last + ":" if prop else last
    n = _one_line(lines, lo, hi, want, decl, scope, refuse)
    end = (_prop_span_end(lines, n, want, refuse) if prop
           else _stmt_span_end(lines, n, want, refuse))

    # ── ⊕ MRB-306, 2 Sep 2026 — HOW FAR DID THE SPAN ACTUALLY REACH? ─────
    #
    # Everything above finds WHERE a ruling applies and nothing measured HOW
    # MUCH it would replace. That gap nearly deleted six kilobytes of
    # Design's logic in silence.
    #
    # `dict(builder="stHistory", key="late, pct")` is the obvious anchor for
    # a line v3 writes as a shorthand pair, and it resolved — to NINETY-SEVEN
    # LINES, 5,414 characters, starting at `late, pct:`, escaping `stHistory`
    # entirely and ending inside the nav-tab code. A one-line ruling
    # replacing that span deletes all of it AND THE BUILD GOES GREEN: every
    # other ruling still matches, the page still renders, and the loss shows
    # up as behaviour nobody wired.
    #
    # The cause is that a STATEMENT ends "at the first line back at base
    # depth ending `;`", and inside an object literal there is no such line
    # until long after the builder has closed. So the two guards below are
    # different questions, and both are needed:
    #
    #   CONTAINMENT — a scoped anchor must not resolve past its own scope.
    #     This is the precise one. `builder=`/`method=`/a dotted path all
    #     narrow to `hi`, and a span that crosses it has stopped describing
    #     the thing the ruling named.
    #   EXTENT — an unscoped anchor has no `hi` to cross, so it gets a
    #     ceiling instead. All 47 anchored rulings in this file span at most
    #     SEVEN lines (the state initialiser); 40 is far above anything
    #     legitimate and far below a runaway.
    #
    # Both refuse rather than warn. A span this wrong is never what was
    # meant, and the whole value of this machinery is that it stops instead
    # of guessing.
    if scope and end >= hi:
        raise refuse(
            "resolves a span that ESCAPES its own scope — it starts at line "
            "%d and runs to line %d, past the end of %s at line %d. A "
            "statement anchor inside an object literal does this: it looks "
            "for a `;` at base depth and does not find one until long after "
            "the scope has closed. Replacing that span would delete "
            "everything in between and still build green. Anchor on the "
            "property (`key=\"%s\"`) rather than the shorthand pair, or "
            "give the ruling a verbatim `frm`"
            % (n + 1, end + 1, scope[-1], hi, last.split(",")[0].strip()))

    if (end - n + 1) > _MAX_ANCHOR_LINES:
        raise refuse(
            "resolves a span of %d lines, and nothing this file anchors is "
            "longer than seven. That is a runaway, not a ruling: the span "
            "starts at line %d with `%s` and ends at line %d with `%s`. "
            "Replacing it would delete everything in between and the build "
            "would still be green"
            % (end - n + 1, n + 1, lines[n][2].strip()[:60],
               end + 1, lines[end][2].strip()[:60]))

    return lines[n][0], lines[end][1]


def resolve_nav_anchor(logic, spec):
    """`resolve_anchor` with the NAV refusal. Kept as the NAV entry point."""
    return resolve_anchor(logic, spec, _nav_refusal)


def _scope_words(scope):
    """How the refusal names the scope it searched, innermost first."""
    if not scope:
        return " in Design's logic"
    return " inside " + " in ".join(reversed(scope))


def _one_line(lines, lo, hi, want, decl, scope, refuse):
    """The single line in [lo, hi) that begins `want`. Refuses on 0 or 2+."""
    found = [n for n in range(lo, hi)
             if n != decl and lines[n][2].lstrip().startswith(want)]
    if len(found) != 1:
        raise refuse(
            "anchors on a line beginning `%s`, and there are %d of them%s"
            % (want, len(found), _scope_words(scope)))
    return found[0]


def _line_delta(lines, n):
    """The depth CHANGE across line `n`."""
    before = lines[n - 1][3] if n else 0
    return lines[n][3] - before


def _prop_span_end(lines, n, want, refuse):
    """The LAST line index of the property that starts at line `n`."""
    start_depth = lines[n][3] - _line_delta(lines, n)
    for i in range(n, len(lines)):
        text = lines[i][2].rstrip()
        if lines[i][3] == start_depth:
            nxt = lines[i + 1][2].lstrip() if i + 1 < len(lines) else ""
            if text.endswith(",") or nxt[:1] in ("}", ")", "]"):
                return i
    raise refuse(
        "anchors on a line beginning `%s` whose arrow body never closes"
        % want)


def _stmt_span_end(lines, n, want, refuse):
    """The LAST line index of the statement that starts at line `n`.

    Ends on the first line back at the statement's own starting depth that
    terminates it with `;`. That is what carries a multi-line initialiser —
    `state = {` opens a brace on its first line and closes it four lines
    later on `};`, and a depth-only rule would hand back the opening line
    alone and splice a `to` in on top of an orphaned object literal.
    """
    base = lines[n][3] - _line_delta(lines, n)
    for i in range(n, len(lines)):
        if lines[i][3] == base and lines[i][2].rstrip().endswith(";"):
            return i
    raise refuse(
        "anchors on a statement beginning `%s` that never ends" % want)


def _method_scope(lines, method, refuse):
    """(lo, hi): the line range of `method`'s BODY, its closer excluded.

    ⊕ 1 Sep 2026 (MRB-306). `builder=` says WHICH LIST a row belongs to;
    `method=` says WHICH METHOD a statement belongs to, which is the scope a
    plain statement needs — `const flagged` is not a property of anything
    and has no builder above it, but it is unambiguously one line of
    `renderVals`, and `renderVals` is a name Design has never renamed.
    """
    decl = re.compile(r"^  %s\s*\(" % re.escape(method))
    hits = [n for n in range(len(lines)) if decl.match(lines[n][2])]
    if len(hits) != 1:
        raise refuse(
            "anchors inside a method named %r, and Design's class declares "
            "%d of them, not one" % (method, len(hits)))
    n = hits[0]
    base = lines[n][3] - _line_delta(lines, n)
    if lines[n][3] == base:          # `klass() { return …; }` — one line
        return n, n + 1
    for i in range(n + 1, len(lines)):
        if lines[i][3] == base:
            return n + 1, i
    raise refuse("anchors inside `%s()`, whose body never closes" % method)


def _builder_block_end(lines, n, refuse, builder):
    """The line index just past `const <builder> = …;`.

    Ends on the first line that is back at the declaration's own starting
    depth AND terminates the statement with `;`. The `;` half is load-bearing
    for a CHAINED builder — `liveClasses.map(…)` on one line, `.filter(…)`
    and `.sort(…).slice(…).map(…)` on the next three — where the depth is
    already back to base at the end of the first line and a depth-only rule
    would hand back a one-line block with no handler in it.
    """
    base = lines[n][3] - _line_delta(lines, n)
    for i in range(n, len(lines)):
        if lines[i][3] == base and lines[i][2].rstrip().endswith(";"):
            return i + 1
    raise refuse(
        "anchors inside `const %s`, whose declaration never ends" % builder)


def _reindent(text, indent):
    """`to` re-laid at Design's own indentation.

    ⚠️ THE RULING OWNS THE CODE; DESIGN OWNS THE MARGIN. `to` is written once
    and must survive a redelivery, and Design reindents freely — the class
    roster's `open` moved from eight spaces to six between v2 and v3 without
    a character of it changing. Pinning the margin inside `to` would make
    every such move a hand-edit of the rulings, which is the padding problem
    this mechanism exists to remove.
    """
    body = text.split("\n")
    lead = len(body[0]) - len(body[0].lstrip())
    out = []
    for line in body:
        if not line.strip():
            out.append("")
            continue
        keep = line[lead:] if line[:lead].strip() == "" else line.lstrip()
        out.append(indent + keep)
    return "\n".join(out)


def replace_method(logic, name, body, why):
    """Replace a method's whole body, found by balanced-brace scan."""
    m = re.search(r"\n  %s\s*\(" % re.escape(name), logic)
    if not m:
        raise SystemExit(
            "build_teacher_port.py: the MRB-287 seam replaces the body of "
            "`%s()`, and Design's logic has no such method.\n"
            "  The ruling stands (%s); Design has renamed or removed it, so "
            "re-anchor it in teacher_rulings.METHODS rather than dropping "
            "it. Skipping is not available: a seam that silently matched "
            "nothing leaves the page reading its marks from Design's "
            "imagination while every gate stays green."
            % (name, why.split(".")[0]))
    args_open = logic.index("(", m.start())
    args_end = _balanced(logic, args_open, "(", ")")
    brace = logic.index("{", args_end - 1)
    end = _balanced(logic, brace, "{", "}")
    return logic[:brace] + "{\n" + body + "\n  }" + logic[end:]


def drop_field(logic, name, why):
    """Delete a class field initialiser, found by balanced scan."""
    m = re.search(r"\n  %s\s*=\s*" % re.escape(name), logic)
    if m:
        i = m.end()
        while logic[i] in " \t\r\n":
            i += 1
        if logic[i] in "[{":
            end = _balanced(logic, i, logic[i], "]" if logic[i] == "[" else "}")
        else:
            end = logic.index(";", i)
        end = logic.index(";", end - 1) + 1
        while end < len(logic) and logic[end] == "\n":
            end += 1
        return logic[:m.start() + 1] + logic[end:]
    # a method, not a field — `rnd` is the only one
    m = re.search(r"\n  %s\s*\(" % re.escape(name), logic)
    if not m:
        raise SystemExit(
            "build_teacher_port.py: the MRB-287 seam deletes `%s`, and it is "
            "not in Design's logic as either a field or a method.\n"
            "  The ruling stands (%s). Re-anchor it in "
            "teacher_rulings.DROP_FIELDS: a deletion that deletes nothing is "
            "invisible, and this list is the only thing standing between a "
            "real teacher and a hashed number."
            % (name, why.split(".")[0]))
    args_open = logic.index("(", m.start())
    args_end = _balanced(logic, args_open, "(", ")")
    brace = logic.index("{", args_end - 1)
    end = _balanced(logic, brace, "{", "}")
    while end < len(logic) and logic[end] == "\n":
        end += 1
    return logic[:m.start() + 1] + logic[end:]


def drop_key(logic, key):
    """Delete one key from `renderVals`'s returned object literal.

    Balanced from the value's first token to the comma that closes it, so a
    key whose value is a multi-line array of objects (`swClassList`) comes out
    whole rather than up to its first comma.
    """
    m = re.search(r"\n      %s:\s*" % re.escape(key), logic)
    if not m:
        raise SystemExit(
            "build_teacher_port.py: the MRB-287 seam removes the `renderVals` "
            "key `%s`, and it is not there. Every key on that list is read by "
            "the Set-work sheet, which is pruned — most of them also read "
            "`this.TOPICS`, which is deleted, so leaving one in place does "
            "not merely compute something nobody looks at: it throws at "
            "mount, on all six pages. Re-anchor it." % key)
    i = m.end()
    depth = 0
    n = len(logic)
    while i < n:
        ch = logic[i]
        if ch in "'\"`":
            q, i = ch, i + 1
            while i < n:
                if logic[i] == "\\":
                    i += 2
                    continue
                if logic[i] == q:
                    break
                i += 1
            i += 1
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            if depth == 0:
                break
            depth -= 1
        elif ch == "," and depth == 0:
            i += 1
            break
        i += 1
    while i < n and logic[i] == "\n":
        i += 1
    return logic[:m.start() + 1] + logic[i:]


def seam_logic(tpl_logic):
    """Design's logic class with every MRB-287 ruling applied.

    Returns (logic, counts). Page-independent: the only per-page value is the
    screen name, left as the token `MRB_SCREEN` for `page_logic` to fill in.
    """
    import teacher_rulings as R

    logic = tpl_logic
    counts = dict(logic=0, methods=0, fields=0, keys=0, nav=0)

    # ── 1. the navigation rewires ────────────────────────────────────────
    #
    # ⚠️ BEFORE THE OTHER REWRITES, AND THE ORDER IS LOAD-BEARING. Three of the
    # NAV anchors carry TRAILING CONTEXT — `\n\n    const flagged`,
    # `\n\n    const paperRow` — because the closure bodies alone are
    # byte-identical to each other and an exactly-once replacement would refuse
    # on a count of two. `LOGIC` inserts two helpers immediately above
    # `const flagged`, so run the other way round the context no longer
    # follows and the build stops with "appears 0 times", naming a handler
    # Design had not touched. Found by the build stopping, which is the check
    # working.
    #
    # ⊕ 1 Sep 2026 (MRB-306) — AND THAT ORDERING HAZARD IS GONE FOR ANY ENTRY
    # THAT CARRIES AN `anchor`. The paragraph above is kept because it is the
    # reason the trailing context existed at all, and because the `frm` path
    # below still honours it. An `anchor` names the BUILDER and the KEY, so
    # nothing about the lines around the handler is load-bearing any more —
    # see `resolve_nav_anchor`. All sixteen entries are anchored today; the
    # `frm` path stays for the next ruling that needs it.
    #
    # Same refusal, and the same reason. The NODES these are anchored to are
    # asserted separately, in `apply_rulings` — here it is only the source.
    for handler, spec in R.NAV.items():
        if "anchor" in spec:
            start, end = resolve_nav_anchor(logic, dict(spec, _name=handler))
            span = logic[start:end]
            indent = span[:len(span) - len(span.lstrip(" \t"))]
            logic = logic[:start] + _reindent(spec["to"], indent) + logic[end:]
            counts["nav"] += 1
            continue
        n = logic.count(spec["frm"])
        if n != 1:
            raise SystemExit(
                "build_teacher_port.py: the navigation ruling for %r anchors "
                "on a span that appears %d times in Design's logic, not "
                "once:\n    %s…\n"
                "  Design has redrawn that handler. Re-anchor it in "
                "teacher_rulings.NAV. A skipped rewire leaves a button that "
                "changes `s.screen` on a page where `s.screen` is fixed — it "
                "draws perfectly and does nothing, and no static check here "
                "can see that." % (handler, n,
                                   spec["frm"].strip().split("\n")[0][:78]))
        logic = logic.replace(spec["frm"], spec["to"], 1)
        counts["nav"] += 1

    # ── 2. the guarded exactly-once source replacements ──────────────────
    #
    # ⊕ 1 Sep 2026 (MRB-306) — the first element is `frm` OR an `anchor`.
    # A dict means the ruling names the node it corrects rather than
    # photographing the source around it; see the block comment above
    # `_logic_lines`. The `frm` branch below is unchanged and still carries
    # the 46 entries whose span is self-identifying text.
    for frm, to, why in R.LOGIC:
        if isinstance(frm, dict):
            spec = dict(anchor=frm, _name=why.split(".")[0][:72])
            start, end = resolve_anchor(logic, spec, _logic_refusal)
            span = logic[start:end]
            indent = span[:len(span) - len(span.lstrip(" \t"))]
            logic = logic[:start] + _reindent(to, indent) + logic[end:]
            counts["logic"] += 1
            continue
        n = logic.count(frm)
        if n != 1:
            raise SystemExit(
                "build_teacher_port.py: an MRB-287 ruling anchors on a span "
                "that appears %d times in Design's logic, not once:\n"
                "    %s…\n"
                "  The ruling is Mide's and still stands (%s). Design has "
                "redrawn that span; re-anchor it in teacher_rulings.LOGIC "
                "rather than dropping it, and do NOT hand-edit the built "
                "page — that is exactly how the MRB-275 rulings were lost.\n"
                "  ⚠️ SKIPPING IS NOT AVAILABLE. A ruling that silently "
                "matched nothing is the same failure as the hand-edit it "
                "replaces: the build goes green and the ruling is not in the "
                "page." % (n, frm.strip().split("\n")[0][:78],
                           why.split(".")[0]))
        logic = logic.replace(frm, to, 1)
        counts["logic"] += 1

    # ── 3. whole method bodies ───────────────────────────────────────────
    for name, (body, why) in R.METHODS.items():
        logic = replace_method(logic, name, body, why)
        counts["methods"] += 1

    # ── 4. `renderVals` keys, then class fields ──────────────────────────
    #
    # ⚠️ THE KEYS COME FIRST, AND THE ORDER IS LOAD-BEARING. `topics` and
    # `swClassList` read `this.TOPICS` and `this.CLASSES`; dropping the FIELD
    # first would leave a reader of a field that no longer exists, and the
    # only thing that would notice is a teacher's browser at mount.
    for key in R.DROP_KEYS:
        logic = drop_key(logic, key)
        counts["keys"] += 1
    for name, why in R.DROP_FIELDS:
        logic = drop_field(logic, name, why)
        counts["fields"] += 1

    # ── 5. THE ASSERTION THE WHOLE PORT TURNS ON ─────────────────────────
    #
    # See `SEED_GUARD` in teacher_rulings.py. `rnd` invents every number in
    # Design's delivery; `seed` also backs `hueFor`, which is derivation and
    # stays. If `rnd` survives anywhere, a real teacher's dashboard is showing
    # at least one hashed number and nothing about the page looks wrong.
    for token in R.SEED_GUARD["forbidden"]:
        if token in logic:
            raise SystemExit(
                "build_teacher_port.py: ⛔ %r IS STILL IN THE LOGIC THIS "
                "BUILD IS ABOUT TO SHIP.\n"
                "  Every mark, percentage, submission count and chart column "
                "in Design's delivery comes out of `rnd()`. If it can still "
                "be called, at least one number on a real teacher's "
                "dashboard is invented — and an invented number looks exactly "
                "like a real one. Find the caller and seam it; do not delete "
                "this check." % token)
    callers = len(re.findall(r"this\.seed\(", logic))
    if callers != R.SEED_GUARD["seed_callers"]:
        raise SystemExit(
            "build_teacher_port.py: `this.seed(` is called %d time(s) in the "
            "shipped logic; exactly %d is expected.\n"
            "  `seed` survives for ONE reason — `hueFor(name)` hashes a "
            "child's name to a stable avatar colour, which is derivation and "
            "not invention. A second caller means somebody has started "
            "inventing numbers again, and `rnd` was deleted precisely so that "
            "this count is the whole check. (%s)"
            % (callers, R.SEED_GUARD["seed_callers"], R.SEED_GUARD["why"]))

    return logic, counts


# ══════════════════════════════════════════════════════════════════════════
#  Design's template, ruled
# ══════════════════════════════════════════════════════════════════════════

def index_tree(roots):
    found, parent = {}, {}

    def walk(n, p):
        if isinstance(n, dict):
            if n.get("i") is not None:
                found[n["i"]] = n
                parent[n["i"]] = p
            for kid in n.get("c") or []:
                walk(kid, n)

    for r in roots:
        walk(r, None)
    return found, parent


def apply_rulings(spec, roots, logic):
    """Design's template with MRB-287's rulings applied, for ONE page.

    `logic` is the SEAMED logic for this build — it is here so step 6 can
    assert every `WRAP` expression is a key that actually exists. See there
    for why an unchecked one is invisible rather than fatal.

    Returns (roots, stats). Every index every ruling names must be found, or
    the build stops. A prune that silently matched nothing is how a screen
    ships twice; an attribute set on a node that has moved names some other
    element for a gate that will then pass against the wrong thing.
    """
    import teacher_rulings as R

    roots = json.loads(json.dumps(roots))
    full, _ = index_tree(roots)

    # ── 0. assert, against the FULL template, everything the rulings name ─
    #
    # ⚠️ THIS RUNS BEFORE ANY PRUNING, AND THAT IS THE WHOLE POINT. Six of the
    # seven screens are in Design's file and six of them come out of every
    # emitted page, so a dead control living on
    # another page's screen is legitimately absent AFTER pruning and would
    # make a per-page assertion useless — it would pass by accident on six
    # pages out of six. Asserted here, against Design's whole delivery, a
    # control Design has removed stops EVERY page's build.
    for flag, node in list(R.SCREENS.items()) + list(R.OVERLAYS.items()):
        if node not in full:
            raise SystemExit(
                "build_teacher_port.py: the screen/overlay %r is template "
                "node %s, and that node is not in Design's delivery. Design "
                "has redrawn the file; re-anchor teacher_rulings.SCREENS / "
                ".OVERLAYS. Guessing would emit a page with two screens on "
                "it." % (flag, node))
    for (node, after), (_sub, why) in R.INSERT_AT.items():
        for which, n in (("into", node), ("after", after)):
            if n is None or n in full:
                continue
            raise SystemExit(
                "build_teacher_port.py: the MRB-287 ruling inserts markup "
                "%s template node %s — %s — and that node is not in "
                "Design's delivery.\n"
                "  Design has redrawn it. Re-anchor teacher_rulings."
                "INSERT_AT: an insertion that silently went nowhere is a "
                "state a teacher never sees, on a page that still builds."
                % (which, n, why.split(".")[0]))
    for node, why in R.DEAD:
        if node not in full:
            raise SystemExit(
                "build_teacher_port.py: the MRB-287 ruling prunes template "
                "node %s — %s — and it is not in Design's delivery.\n"
                "  The ruling stands: creating an assignment has no write "
                "path. Re-anchor it, or if Design has removed the control "
                "itself, remove the row from teacher_rulings.DEAD and say so "
                "in the commit." % (node, why))

    # ── 1. prune: the six other screens, the unkept overlays, the dead ───
    keep_screen = R.SCREENS[spec["screen"]]
    prune = {n for f, n in R.SCREENS.items() if n != keep_screen}
    prune |= {n for f, n in R.OVERLAYS.items() if f not in spec["overlays"]}
    prune |= {n for n, _why in R.DEAD}

    # A dead control inside a screen this page does not keep is already gone
    # with its screen. Only assert the ones that CAN be here.
    surviving = set()
    for node in prune:
        p = node
        gone = False
        # walk up: is this node inside a screen we are pruning?
        _, parents = index_tree(roots)
        while p is not None:
            if p in prune and p != node:
                gone = True
                break
            par = parents.get(p)
            p = par.get("i") if isinstance(par, dict) else None
        if not gone:
            surviving.add(node)

    removed = [0]
    want = set(surviving)

    def walk(node):
        if not isinstance(node, dict) or not node.get("c"):
            return
        kept = []
        for kid in node["c"]:
            if isinstance(kid, dict) and kid.get("i") in want:
                removed[0] += 1
                want.discard(kid["i"])
                continue
            walk(kid)
            kept.append(kid)
        node["c"] = kept

    for root in roots:
        walk(root)
    if want:
        raise SystemExit(
            "build_teacher_port.py: %s prunes template node(s) %s and they "
            "were not found. A prune that silently matches nothing is how a "
            "screen ships twice — on a page that looks correct because the "
            "second screen is below the fold. Re-anchor them."
            % (spec["out"], sorted(want)))

    here, _ = index_tree(roots)

    # ── 1b. the two states Design drew no counterpart for ────────────────
    #
    # ⚑ THE ONLY MECHANISM HERE THAT ADDS MARKUP, and it is deliberately the
    # last resort. `SET_ON`, `SET_ATTR`, `BIND_ATTR` and `RETEXT_AT` all work
    # on something Design drew; these two have nothing to work on, because
    # Design's sample cannot reach either state — its class list always has
    # both key stages in it, and its question grid has only three of the four
    # cell states the seam can now produce.
    #
    # Design's own README: "Empty states are states, not blanks." A filter
    # that matches nothing rendering an empty rectangle breaks Design's own
    # stated rule, so finishing it is not new scope. Both insertions copy
    # Design's own type treatment off a node Design DID draw — see the `why`
    # on each — rather than inventing a register.
    #
    # ⚠️ INSERTED AFTER THE PRUNE AND BEFORE THE BINDINGS. After, so a node
    # cannot be inserted into a screen that is about to be deleted; before, so
    # `bindings_for` computes its child-index paths over the tree that will
    # actually ship. Nothing inserted carries an `i`, so Design's numbering —
    # which every other ruling in this file is anchored on — does not move.
    # ⊕ MRB-304 — keyed by (parent, after) rather than by parent alone,
    # because node 10 (the sticky top bar) now takes two insertions and a
    # parent-keyed dict would have kept one and dropped the other in silence.
    # `after` is sorted with None first so the ordering is total; the
    # positions themselves do not depend on it, because an inserted node
    # carries no `i` and cannot be the anchor of a later insertion.
    inserted = 0
    for (parent, after_node), (subtree, why) in sorted(
            R.INSERT_AT.items(), key=lambda kv: (kv[0][0], kv[0][1] is not None,
                                                 kv[0][1] or 0)):
        if parent not in here:
            continue
        kids = here[parent].setdefault("c", [])
        pos = len(kids)
        if after_node is not None:
            hit = [j for j, kid in enumerate(kids)
                   if isinstance(kid, dict) and kid.get("i") == after_node]
            if len(hit) != 1:
                raise SystemExit(
                    "build_teacher_port.py: the insertion into node %s goes "
                    "after node %s, and that node is %d of node %s's "
                    "children, not one.\n"
                    "  Re-anchor teacher_rulings.INSERT_AT. Appended to the "
                    "wrong place this puts an empty state in the middle of a "
                    "screen, and the page still builds. (%s)"
                    % (parent, after_node, len(hit), parent, why))
            pos = hit[0] + 1
        kids.insert(pos, json.loads(json.dumps(subtree)))
        inserted += 1

    # ── 2. `data-port-region`, on what survived ──────────────────────────
    #
    # Refuses to overwrite an attribute Design already wrote, for the reason
    # `student_rulings.SET_ATTR` records: the page would still look and gate
    # exactly right while one of Design's own values had been replaced.
    attred = 0
    for node, bag in R.SET_ATTR.items():
        if node not in here:
            continue
        a = here[node].setdefault("a", {})
        for k, v in bag.items():
            if k in a:
                raise SystemExit(
                    "build_teacher_port.py: the region ruling sets %s=%r on "
                    "template node %s, and Design already gives that node "
                    "%s=%r. Re-anchor rather than overwriting one of "
                    "Design's own values." % (k, v, node, k, a[k]))
            a[k] = v
        attred += 1

    # ── 3. the ONE attribute whose value is sample data ──────────────────
    attr_bound = 0
    for node, (attr, expect, repl, why) in R.BIND_ATTR.items():
        if node not in here:
            continue
        got = (here[node].get("a") or {}).get(attr)
        if got != expect:
            raise SystemExit(
                "build_teacher_port.py: the attribute binding replaces %s=%r "
                "on template node %s, and that node reads %r.\n"
                "  The index has drifted or Design has redrawn it. Re-anchor "
                "it: applied to the wrong node this overwrites one of "
                "Design's own attributes with a placeholder, and the page "
                "still builds. (%s)" % (attr, expect, node, got, why))
        here[node]["a"][attr] = repl
        attr_bound += 1

    # ── 3b. sample data with NO seam key ─────────────────────────────────
    #
    # See `RETEXT_AT` in teacher_rulings.py. These are the import wizard's five
    # invented figures, which cannot be bound because the seam deliberately
    # does not compute them — the LIVE wizard already does — and cannot be
    # left, because they are a file nobody uploaded and counts nobody ran.
    #
    # Replaced at BUILD time, not bound at mount: a binding needs a key, and
    # inventing one here would put a value into `MRB_DATA` that
    # `teacher-live.js` never supplies, which is a thrown error on a real page.
    retexted = 0
    for node, (expect, repl, why) in R.RETEXT_AT.items():
        if node not in here:
            continue
        kids = [c for c in (here[node].get("c") or [])
                if isinstance(c, dict) and c.get("t") == "#"]
        if len(kids) != 1 or kids[0].get("v") != expect:
            raise SystemExit(
                "build_teacher_port.py: the MRB-287 ruling replaces the text "
                "of node %s (%r) with %r, and that node reads %r.\n"
                "  Re-anchor teacher_rulings.RETEXT_AT. Applied to the wrong "
                "node this overwrites a HEADING, and the page still builds. "
                "(%s)" % (node, expect, repl,
                          kids[0].get("v") if len(kids) == 1
                          else "%d text children" % len(kids), why))
        kids[0]["v"] = repl
        retexted += 1

    # ── 4. handlers Design left inert ────────────────────────────────────
    wired = 0
    for node, handler in R.SET_ON.items():
        if node not in here:
            continue
        if here[node].get("on"):
            raise SystemExit(
                "build_teacher_port.py: the MRB-287 ruling attaches %r to "
                "template node %s, but Design already gives that node the "
                "handler %r. Design has redrawn it; re-anchor the ruling "
                "rather than overwriting a live control."
                % (handler, node, here[node]["on"]))
        here[node]["on"] = handler
        wired += 1

    # ── 4b. ⊕ MRB-304 · a node moved from one of Design's handlers to
    #        another ────────────────────────────────────────────────────
    #
    # ⚑ THE CASE `NAV` STRUCTURALLY CANNOT SERVE. `NAV` redefines a handler by
    # NAME, once, in the logic — every node carrying that name gets the new
    # behaviour, and there is no per-node arm. Design shares `goClasses`
    # between the brand mark (11) and the class screen's Back (83), and those
    # two now want different destinations. Rewriting `goClasses` would take
    # the Back button to the homepage with it.
    #
    # ⚠️ THE HANDLER IT IS MOVING OFF IS ASSERTED. That is the property
    # `SET_ON` gives for free and a bare `here[node]["on"] = …` would lose: if
    # Design redraws the top bar and node 11 becomes some other control, this
    # stops the build instead of silently pointing that control at the
    # homepage — which would look and gate exactly right.
    #
    # ⚠️ AND THE HANDLER IT MOVES ONTO MUST EXIST IN THE EMITTED LOGIC. The
    # runtime looks a node's `on` up through the miss recorder, so a typo here
    # is a control wired to nothing — caught by `teacher_behaviour`'s
    # `data-mrb-misses` check, but only after the page had been written. This
    # is the same guard step 6 makes for `WRAP`, for the same reason.
    retargeted = 0
    for node, (expect, handler, why) in R.RETARGET_ON.items():
        if node not in here:
            continue
        on = here[node].get("on")
        if on != expect:
            raise SystemExit(
                "build_teacher_port.py: the MRB-304 ruling moves template "
                "node %s from %r to %r, and that node carries %r.\n"
                "  Design has redrawn it, or the index now names a different "
                "control. Re-anchor teacher_rulings.RETARGET_ON: applied to "
                "the wrong node this repoints one of Design's own controls at "
                "somewhere it was never meant to go, and the page still "
                "builds. (%s)"
                % (node, expect, handler, on or "no handler at all",
                   why.split(".")[0]))
        if not re.search(r"\b%s\b\s*:" % re.escape(handler), logic):
            raise SystemExit(
                "build_teacher_port.py: the MRB-304 ruling moves template "
                "node %s onto the handler %r, and no `renderVals` key of that "
                "name is anywhere in the emitted logic.\n"
                "  Add it in teacher_rulings.LOGIC, or fix the spelling. "
                "Unchecked, this ships a control that resolves to nothing — a "
                "brand mark a teacher presses and nothing happens. (%s)"
                % (node, handler, why.split(".")[0]))
        here[node]["on"] = handler
        retargeted += 1

    # ── 5. the navigation rewires, asserted at their NODES ───────────────
    #
    # ⚑ THE HALF A SOURCE REPLACEMENT CANNOT GIVE. `seam_logic` has already
    # redefined these handlers; this proves the nodes that CALL them are still
    # the nodes the ruling was written against. Without it, Design could move
    # `c.open` off the class card onto something else and the port would
    # cheerfully navigate from whatever now carries it.
    #
    # Only nodes that survived this page's pruning are checked — the rest are
    # legitimately on another page — and every node is checked on at least one
    # page, which the summary line at the end of the build reports.
    checked = 0
    for handler, nav in R.NAV.items():
        for node in nav["nodes"]:
            if node not in here:
                continue
            on = here[node].get("on")
            expect = handler.split(" ")[0]
            if on != expect:
                raise SystemExit(
                    "build_teacher_port.py: the navigation ruling for %r is "
                    "anchored on template node %s, and that node carries the "
                    "handler %r.\n"
                    "  Design has redrawn it, or the index now names a "
                    "different control. The rewiring itself has already been "
                    "applied to the logic, so leaving this unchecked would "
                    "point %r at a destination meant for something else and "
                    "the page would still build. Re-anchor "
                    "teacher_rulings.NAV[%r]['nodes']."
                    % (handler, node, on or "no handler at all", handler,
                       handler))
            checked += 1

    # ── 6. one of Design's nodes, made conditional ───────────────────────
    #
    # ⚑ See `teacher_rulings.WRAP`. The node is REPLACED IN ITS PARENT by an
    # `<if>` whose single child is the node itself, so its subtree, its index,
    # its handlers and its bindings are all untouched — the only change is
    # that it now renders when the expression is truthy and not otherwise.
    # The wrapper carries no `i`: `student-runtime` renders an `<if>` as a
    # BRANCH and never as an element, so there is nothing to hang a
    # `data-dc-tpl` on, and Design's numbering must not move.
    #
    # ⚠️ IT RUNS LAST, AFTER THE INSERTS AND THE NAV CHECK, AND BEFORE
    # `bindings_for`. After, so an insert cannot land inside a node that has
    # just become an `<if>`'s only child and so the NAV assertion still reads
    # Design's own node; before, because `bindings_for` computes child-index
    # PATHS over the tree that ships, and a wrapper adds a level.
    #
    # ⛔ AND EVERY EXPRESSION IS ASSERTED INTO THE LOGIC, WHICH THE STUDENT
    # PORT DOES NOT DO. `student-runtime.js:146` evaluates an `<if>` with
    # `lookup(node.e, scope, null)` — WITHOUT the miss recorder — so a key
    # that is not in `renderVals` is not an error and does not register as a
    # missed binding. It is silently FALSE. A typo here would take the
    # shoutout composer off every class page, leave `data-mrb-misses` at
    # zero, and pass every gate in the set.
    wraps = dict(R.WRAP.get(spec["out"], {}))
    for node, expr in sorted(wraps.items()):
        name = expr.split(".")[0].strip()
        if not re.search(r"\b%s\b" % re.escape(name), logic):
            raise SystemExit(
                "build_teacher_port.py: %s wraps template node %s in `<if "
                "%s>`, and no `renderVals` key of that name is anywhere in "
                "the emitted logic.\n"
                "  `student-runtime` looks an `<if>` expression up WITHOUT "
                "the miss recorder, so a key that does not exist is not an "
                "error — it is silently FALSE, and the node simply never "
                "renders. Add the key in teacher_rulings.LOGIC, or fix the "
                "spelling here: unchecked, this ships a page with the "
                "control missing and every gate green."
                % (spec["out"], node, expr))

    wrapped = [0]

    def enclose(node):
        if not isinstance(node, dict) or not node.get("c"):
            return
        kids = node["c"]
        for pos, kid in enumerate(kids):
            if isinstance(kid, dict) and kid.get("i") in wraps:
                kids[pos] = {"t": "if", "e": wraps.pop(kid["i"]), "c": [kid]}
                wrapped[0] += 1
            enclose(kid)

    for root in roots:
        if isinstance(root, dict) and root.get("i") in wraps:
            raise SystemExit(
                "build_teacher_port.py: the MRB-287 E1 ruling wraps template "
                "node %s in a conditional on %s, and that node is a template "
                "ROOT with no parent to hold the wrapper. Wrap something "
                "further in." % (root.get("i"), spec["out"]))
        enclose(root)
    if wraps:
        raise SystemExit(
            "build_teacher_port.py: %s wraps template node(s) %s in a "
            "conditional and they are not in the tree.\n"
            "  Either Design has redrawn them, or they were pruned by DEAD / "
            "by another screen before the wrap ran. A silently skipped wrap "
            "leaves a WRITE control on a read-only academic year — which is "
            "the MRB-261 breach this ruling exists to close — and the build "
            "stays green. Re-anchor teacher_rulings.WRAP[%r]."
            % (spec["out"], sorted(wraps), spec["out"]))

    return roots, dict(pruned=removed[0], attred=attred, wired=wired,
                       attr_bound=attr_bound, nav_checked=checked,
                       retexted=retexted, inserted=inserted,
                       wrapped=wrapped[0], retargeted=retargeted)


# ── the binding table: text nodes Design typed that are sample data ──────

def path_to(roots, index):
    """The `c`-index path from the roots array to a node, for the runtime."""
    found = []

    def walk(node, path):
        if not isinstance(node, dict):
            return
        if node.get("i") == index:
            found.append(list(path))
            return
        for j, kid in enumerate(node.get("c") or []):
            walk(kid, path + [j])

    for r, root in enumerate(roots):
        walk(root, [r])
    if len(found) != 1:
        raise SystemExit(
            "build_teacher_port.py: template node %s is at %d paths in the "
            "tree, not one." % (index, len(found)))
    return found[0]


def bindings_for(spec, roots):
    """(binding table, {key: Design's own value}) for the nodes on this page.

    ⚠️ INDEX-ANCHORED AND LITERAL-ASSERTED, BOTH, and `student_rulings` binds
    by literal alone. That difference is deliberate: on the student pages one
    value (`8r/Sc1`) is typed in several places and every one of them means
    the same class, so a literal key binds them all for free. Here the
    opposite is true — `24`, `2` and `1` are three DIFFERENT import counts,
    and a literal-keyed table would bind every text node reading `2` anywhere
    on the page to the "matched existing" figure.
    """
    import teacher_rulings as R

    here, _ = index_tree(roots)
    table, values = [], {}
    for node, (expect, key) in sorted(R.BINDINGS_AT.items()):
        if node not in here:
            continue
        kids = [c for c in (here[node].get("c") or [])
                if isinstance(c, dict) and c.get("t") == "#"]
        if len(kids) != 1 or kids[0].get("v") != expect:
            raise SystemExit(
                "build_teacher_port.py: %s binds template node %s to %r, and "
                "that node's text is %r.\n"
                "  Design has redrawn it, or the index has drifted onto "
                "another node. Re-anchor teacher_rulings.BINDINGS_AT: applied "
                "to the wrong node this replaces a HEADING with a data value, "
                "and the page still builds."
                % (spec["out"], node, key,
                   kids[0].get("v") if len(kids) == 1 else
                   "%d text children" % len(kids)))
        p = path_to(roots, node)
        # +index of the text child within the element
        p = p + [(here[node]["c"]).index(kids[0])]
        table.append({"k": key, "p": p})
        values[key] = expect
    return table, values


def scrub(roots, table):
    """Blank every bound text node, so the PRODUCTION page carries no sample.

    ⚑ THE POINT OF THE WHOLE BINDING MECHANISM. Without this the literal is
    still in the shipped template and the binding merely overwrites it at
    mount — so a page whose data source fails to load renders Design's sample,
    which for a teacher dashboard means a class list that is not theirs.
    """
    out = json.loads(json.dumps(roots))
    for b in table:
        node = out[b["p"][0]]
        for j in b["p"][1:]:
            node = node["c"][j]
        node["v"] = ""
    return out


# ══════════════════════════════════════════════════════════════════════════
#  Design's example data, evaluated rather than retyped
# ══════════════════════════════════════════════════════════════════════════

_FIXTURE_RUNNER = r"""
/* Written and run by build_teacher_port.py. Not checked in.

   Design's ORIGINAL logic class — seed, rnd and all — evaluated once, then
   ADAPTED into the shapes `shared/teacher-live.js` hands the live page. Both
   halves are necessary and neither is retyping:

     · Design's numbers cannot be LIFTED, because Design's delivery does not
       contain them. It contains twelve classes and an FNV hash, and every
       roster, mark, percentage and grid is computed from those. There is no
       literal to lift, and retyping the results is tens of thousands of
       numbers a fixture would then disagree with by one.
     · Design's SHAPES are not the seam's shapes. The matrix now carries
       `pct[]`, `max[]`, `stampShort[]`, `colAsked[]`, `colLate[]`,
       `colLateUnknown[]` and `markedIdx` — because real papers are not out of
       8, real lateness is tri-state, and the denominator is who was ASKED
       rather than who is still on the roster. A fixture in Design's old shape
       would drive none of the code the rulings just wrote.

   ⚠️ THE ADAPTATION INVENTS NOTHING. Every added field is DERIVED from a value
   Design already computed: `max` is 8 because Design's papers are out of 8,
   `pct` is that division done once here instead of five times downstream,
   `stampShort` is the date Design's own history row would have shown, and the
   lateness split puts all of Design's lateness in `colLate` with `unknown` at
   zero — because Design's sample has no unknowns, which is the whole reason
   the state had to be added. */
class DCLogic { constructor(){ this.props = {}; } setState(){} }
/*__DESIGN_LOGIC__*/
const c = new Component();
const out = { CLASSES: c.CLASSES, MATRIX: {}, ROSTER: {}, PAPERS: {},
              WEEKS: {}, GRID: {}, FEED: {} };

/* Design's own month labels and Design's own `lab()` format, so a shifted
   stamp is written exactly the way every other date in this fixture is.
   The year is Design's: `weeks()` seeds `new Date(2026, 8, 2)` and the whole
   sample runs Jun–Sep of that one year, so a ±2-day shift can roll a month
   but never a year. Returns the input unchanged if it is not a "D Mon". */
const FX_M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
function fxShiftShort(short, days) {
  if (!short) { return null; }
  const m = /^(\d+)\s+([A-Za-z]{3})$/.exec(short);
  if (!m || FX_M.indexOf(m[2]) < 0) { return short; }
  const d = new Date(2026, FX_M.indexOf(m[2]), parseInt(m[1], 10) + days);
  return d.getDate() + ' ' + FX_M[d.getMonth()];
}

function adaptMatrix(k, mx, papers) {
  const cols = papers.length;
  const markedIdx = papers.filter(p => p.when === 'marked').map(p => p.idx);
  const rows = mx.rows.map(function (r) {
    const max = r.scores.map(v => (v == null ? null : 8));
    const pct = r.scores.map(v => (v == null ? null : Math.round((v / 8) * 100)));
    const submitted = r.scores.map(v => v != null);
    /* ⊕ MRB-306 Phase 2a screen 4, 2 Sep 2026 — A STAMP THE CLOCK COULD
       ACTUALLY HAVE PRODUCED.

       ⛔ THIS USED TO BE `r.late[i] ? papers[i].lateShort : papers[i].dueShort`
       with the note "it keeps the fixture rendering what Design drew". That
       was the wrong goal, and it made the fixture model a state real data
       cannot reach.

       Design's `lateShort` is `due − 5 days` — the FRIDAY BEFORE the
       Wednesday deadline, the end of the week the work was SET in. It is not
       a submission date at all. So every LATE row in this fixture carried a
       stamp EARLIER than its own deadline: "Energy stores and transfers, due
       Wed 26 Aug, submitted 21 Aug, LATE". And every on-time row carried the
       deadline itself, to the day, for nine rows running.

       The live seam cannot produce either. `buildMatrix` takes the stamp from
       `completed_at`/`submitted_at`, and where `is_late` is null it DERIVES
       lateness as `stamp > paper.due_at` — so a late stamp is after the
       deadline by construction, and an on-time one is not.

       ⚠️ AND IT MADE THE GATE BLIND TO ITS OWN RULING. #11's whole point is
       that the SUBMITTED column must show the real stamp rather than the
       deadline. A fixture that feeds it the deadline anyway renders exactly
       what the unfixed code rendered, so no gate could tell the ruling had
       been applied.

       So the stamp is now derived from the deadline CONSISTENTLY WITH `late`:
       a day before it when the work was on time, two days after when it was
       late. Still Design's dates, still invented like everything else here —
       but no longer self-contradictory, and now distinguishable from
       `dueShort`, which is the whole thing the ruling is about. */
    const stampShort = r.scores.map(function (v, i) {
      if (v == null || !papers[i]) { return null; }
      return fxShiftShort(papers[i].dueShort, r.late[i] ? 2 : -1);
    });
    return { sid: r.sid, scores: r.scores, max: max, pct: pct,
             late: r.late.slice(), stampShort: stampShort,
             submitted: submitted, inWeek: r.inWeek };
  });
  const colAsked = [], colLate = [], colLateUnknown = [];
  for (let p = 0; p < cols; p++) {
    colAsked.push(k.n);
    colLate.push(Math.max(0, mx.colSub[p] - mx.colOnTime[p]));
    colLateUnknown.push(0);            // Design's sample has no unknowns
  }
  let markedLate = 0;
  markedIdx.forEach(function (i) { markedLate += colLate[i]; });
  const o = {
    rows: rows, cols: cols,
    colSub: mx.colSub, colMean: mx.colMean, colOnTime: mx.colOnTime,
    colAsked: colAsked, colLate: colLate, colLateUnknown: colLateUnknown,
    markedIdx: markedIdx, studentAvg: mx.studentAvg,
    markedSub: mx.markedSub, markedOnTime: mx.markedOnTime,
    markedLate: markedLate, markedLateUnknown: 0,
    markedPct: mx.markedPct, classMean: mx.classMean, byId: {}
  };
  rows.forEach(function (r) { o.byId[r.sid] = r; });
  return o;
}

c.CLASSES.forEach(function (k) {
  const papers = c.papersFor(k);
  const mx = adaptMatrix(k, c.matrixFor(k), papers);
  /* Design's `papersFor` already writes `sub` as `colSub + '/' + k.n`, which
     with `colAsked === k.n` is exactly the seam's `colSub/colAsked`. */
  out.PAPERS[k.id] = papers;
  out.MATRIX[k.id] = mx;
  out.ROSTER[k.id] = c.rosterFor(k);
  /* ⊕ MRB-306 — THE FIXTURE'S WEEKS ARE WEEKS, not assignments, because the
     live seam's are. `buildWeeks` in `shared/teacher-live.js` returns the
     ACADEMIC YEAR's teaching weeks and papers carry a `weekIdx` onto them;
     a fixture still shaped like the old one-week-per-paper list would draw a
     two-chip bar beside a live page's twelve and nothing would say why.

     Design's twelve weeks are twelve papers, so `weekIdx` is the paper's own
     index — true inside her fiction, and the reason the two models were
     indistinguishable until real data arrived.

     ⚠️ NO TERM NAME, DELIBERATELY. The live label ("Autumn Week 6") is
     derived from an `academic_years` row's start date, and Design's sample
     has no academic year at all — it has a hardcoded first date. Inventing a
     term here would put a season into a fixture that no data supports, so
     the chip's second line reads "Week 11" and the newest chip reads "This
     week", which is Design's own wording. */
  const wks = c.weeks();
  out.WEEKS[k.id] = wks.map(function (w, i) {
    return { idx: i, weekOfYear: wks.length - i, term: '',
             label: 'Week ' + (wks.length - i), range: w.range,
             now: i === 0, monYmd: '', friYmd: '' };
  });
  papers.forEach(function (p) {
    p.weekIdx = p.idx;
    p.weekOfYear = wks.length - p.idx;
  });
});

/* The grid travels with `stems`, because `renderVals` labels the question
   list from what used to be the STEMS class field and a paper's questions
   belong to the paper. `qLine` is Design's own "8 questions, 1 mark each",
   built from the paper rather than typed. */
__IDS__.forEach(function (id) {
  const k = c.klassById(id);
  out.PAPERS[id].forEach(function (p, i) {
    const g = c.gridFor(k, i);
    const stems = c.STEMS.map(function (q, qi) {
      return { id: q.id, idx: qi, text: q.text, rung: null,
               question_ref: null, refConflict: false };
    });
    out.GRID[id + ':' + i] = {
      rows: g.rows.map(function (r) {
        return { id: r.id, name: r.name, initials: r.initials, hue: r.hue,
                 raw: r.raw, score: r.score, submitted: r.score !== '—' };
      }),
      qpct: g.qpct, stems: stems, submitted: g.submitted,
      roster: k.n, qcount: stems.length, maxScore: stems.length,
      qCorrect: [], qMarked: [], qUnmarkable: [], qBlank: [],
      qLine: stems.length + ' questions, 1 mark each'
    };
  });
});

/* Design's two sample shoutouts, against the roster the run just computed. */
__IDS__.forEach(function (id) {
  const k = c.klassById(id);
  const roster = out.ROSTER[id];
  const pick = function (n) {
    return roster.length ? roster[Math.min(n, roster.length - 1)].name : '—';
  };
  /* ⊕ MRB-287, 24 Aug 2026 — `id` and `author_id`, which Design's sample has
     no concept of. `teacher-live.buildFeed` carries both on every real row,
     and the delete control is drawn only where `author_id` is the signed-in
     teacher's. ⚑ THE FIRST IS MINE AND THE SECOND IS NOT, deliberately: a
     fixture where every row is deletable proves the control renders and
     proves nothing about the author check, and one where none is leaves
     `teacher_behaviour` with no button to press. */
  out.FEED[id] = [
    { id: id + ':shout-1', author_id: '__MRB_FIXTURE_ME__',
      name: pick(9), when: '2 days ago',
      template: 'Top of the class this week',
      body: 'Highest mean in ' + k.code + ' on the last set — and showed ' +
            'working on every question.',
      initials: c.initials(pick(9)), hue: c.hueFor(pick(9)) },
    { id: id + ':shout-2', author_id: '__MRB_FIXTURE_OTHER__',
      name: pick(12), when: '1 week ago',
      template: 'Bounced back strong',
      body: 'Went from 38% to 74% after one reteach of the lowest-scoring ' +
            'question.',
      initials: c.initials(pick(12)), hue: c.hueFor(pick(12)) }
  ];
});

/* Design's search pool: three students from each of five hardcoded classes.
   Rebuilt from the rosters this run computed rather than retyped as fifteen
   names, so the fixture cannot drift from them. */
out.searchPool = [];
c.POOL_CLASSES.forEach(function (id) {
  const k = c.klassById(id);
  out.ROSTER[id].slice(0, 3).forEach(function (r) {
    out.searchPool.push({ id: r.id, name: r.name,
      initials: c.initials(r.name), hue: c.hueFor(r.name),
      klass: k.code, classId: k.id,
      avg: r.avg == null ? '—' : r.avg + '%' });
  });
});
process.stdout.write(JSON.stringify(out));
"""


def shoutout_templates():
    """The six shoutout templates, READ out of shared/shoutouts.js.

    ⚠️ READ, NOT RETYPED. That list mirrors the DB CHECK constraint
    `class_shoutouts_template_key_chk`, and a fixture carrying a stale key
    would gate green against a composer that fails on insert.
    """
    src = open(os.path.join("shared", "shoutouts.js"), encoding="utf-8").read()
    m = re.search(r"SHOUTOUT_TEMPLATES\s*=\s*\[(.*?)\];", src, re.S)
    if not m:
        raise SystemExit(
            "build_teacher_port.py: shared/shoutouts.js does not define "
            "SHOUTOUT_TEMPLATES. It is the client-side mirror of "
            "class_shoutouts_template_key_chk and the only honest source for "
            "the composer's six templates.")
    out = []
    for key, label in re.findall(r"key:\s*'([^']+)'.*?label:\s*'([^']+)'",
                                 m.group(1)):
        out.append(dict(id=key, key=key, label=label))
    if len(out) != 6:
        raise SystemExit(
            "build_teacher_port.py: shared/shoutouts.js lists %d shoutout "
            "template(s); the DB constraint has six. Either the enum has "
            "moved and the migration is missing, or this reader has stopped "
            "matching the file." % len(out))
    return out


def design_data(logic, class_id, scratch):
    """Design's own sample, computed by RUNNING Design's own logic in node.

    ⚠️ THE ORIGINAL LOGIC, NOT THE SEAMED LOGIC. Running the seamed copy would
    call `MRB_PICK` for the very maps it is trying to produce.
    """
    # ⚠️ `.replace`, NOT `%`-FORMATTING. Design's logic and this runner are
    # both full of `%` — "38% to 74%", `+ '%'` — and a `%`-format template
    # fails on them with "not enough arguments for format string", which is
    # what it did.
    ids = json.dumps([class_id])
    src = (_FIXTURE_RUNNER.replace("/*__DESIGN_LOGIC__*/", logic)
                          .replace("__IDS__", ids)
                          .replace("__MRB_FIXTURE_ME__", FIXTURE_ME)
                          .replace("__MRB_FIXTURE_OTHER__", FIXTURE_OTHER))
    path = os.path.join(scratch, "_teacher_fixture_runner.js")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(src)
    try:
        res = subprocess.run(["node", path], capture_output=True, text=True)
    except FileNotFoundError:
        raise SystemExit(
            "build_teacher_port.py: `node` is not on PATH, and Design's "
            "example data can only be produced by RUNNING Design's own logic "
            "— it is computed from an FNV hash, not written down anywhere. "
            "Without it the fixture pages cannot be built, and the fixture "
            "pages are what the behaviour gate drives.")
    if res.returncode != 0:
        raise SystemExit(
            "build_teacher_port.py: evaluating Design's own logic to extract "
            "the sample failed.\n  %s" % res.stderr.strip()[:2000])
    os.remove(path)
    return json.loads(res.stdout)


# ── the scalars Design typed rather than computed ────────────────────────
#
# ⚠️ THE ONLY VALUES IN THIS BUILD THAT ARE TYPED RATHER THAN EXTRACTED, and
# every one is a literal this port has just taken OUT of Design's markup. They
# are here so the populated fixture still renders byte-for-byte what Design
# drew — which is the whole point of a fixture — and nothing on a live path
# reads them.
#
# `build_student_port.py` makes the same trade for three values and gives the
# same warning: if this grows past a handful, the seam has stopped being a
# seam.
# ── the fixture's signed-in teacher ──────────────────────────────────────
#
# ⛔ NOT A UUID, ON PURPOSE. `auth.users.id` is a uuid and these two are not
# shaped like one, so neither can be mistaken for an account or pasted into a
# query that would then match a real row. They exist so the populated fixture
# has ONE shoutout the viewer wrote and ONE they did not — which is what makes
# `teacher_behaviour`'s press of the delete control mean something, and what
# proves the author check is a check rather than a constant.
FIXTURE_ME = "fixture-signed-in-teacher"
FIXTURE_OTHER = "fixture-other-teacher"

DESIGN_SCALARS = dict(
    teacherName="Ayomide",
    # The signed-in teacher's own auth id. On a live page `teacher-live.js`
    # supplies it from the session the guard already validated; `MRB_ME()`
    # reads it through the seam like everything else.
    ME=FIXTURE_ME,
    envBadge="PROD",
    termLabel="Autumn term · 2026–27",
    termSeason="Autumn",
    yearLabel="2026–27",
    yearName="2026–27",
    viewingYearLabel="Viewing 2026–27",
    academicWeek=1,
    termWeekLabel="Autumn Week 1",
    # ── ⊕ MRB-287 E1 · THE YEAR IN VIEW ──────────────────────────────────
    #
    # ⊕ `hasPastYears` AND `pastYears` WERE HERE AND ARE GONE. They shipped
    # as `hasPastYears=True` beside `pastYears=[]` — a fixture asserting that
    # previous years exist and naming none of them, which is a shape no seam
    # can produce. Both are superseded: `hasOtherYears` asks the question the
    # control actually needs ("is there another year to reach"), which is
    # also true in the direction the old key could not express — the way BACK
    # from a past year to the working one.
    #
    # ⚠️ `yearOptions` EXCLUDES THE YEAR IN VIEW, mirroring the seam. The
    # fixture views 2026-27, so the one option is 2025-26. The id is not a
    # uuid, on the same terms as FIXTURE_ME above: every real academic year
    # id is one, so this cannot be mistaken for a row or pasted into a query
    # that would match one.
    pastYearsLabel="Previous years",
    yearOptions=[dict(id="fixture-year-2025-26", name="2025–26")],
    hasOtherYears=True,
    viewingIsPast=False,
    canWrite=True,
    readOnlyLine="",
    yearParam="",
    weekRangeLabel="Mon 17 – Fri 21 Aug 2026",
    weekOfLabel="Week of Mon 17 Aug 2026",
    printedOn="24 Aug 2026",
    # ⛔ EMPTY ON PURPOSE, AND THIS IS THE ONE PLACE THE FIXTURE DELIBERATELY
    # DIFFERS FROM DESIGN'S RENDER. The Set-work sheet is pruned, and the CSV
    # mapping and preview must bind to the LIVE wizard's own values — filling
    # them here would put four invented children back on the confirm step of a
    # gate that exists to prove they are gone.
    TOPICS=[],
    IMPORT_MAP_ROWS=[],
    IMPORT_PREVIEW_ROWS=[],
    importCountLabel="",
)


def fixture_payload(data, templates, class_id):
    """Design's sample plus the scalars, as one `window.__MRB_DATA__`."""
    classes = data["CLASSES"]
    payload = dict(data)
    payload.update(DESIGN_SCALARS)
    # ⊕ MRB-287 E1 — THE CARD'S OWN ACADEMIC YEAR, DERIVED AND NOT TYPED.
    #
    # Design's classes have no year at all: the string lives once, in her
    # markup, as the welded "· 2026–27" this port took out. So the fixture's
    # per-card value is derived from the ONE scalar that already states the
    # fixture's year rather than written twelve times — twelve literals would
    # be twelve chances to disagree with `yearLabel`, and the card meta's
    # whole defect was a year that disagreed with the class it described.
    classes = [dict(c, yearName=DESIGN_SCALARS["yearLabel"]) for c in classes]
    # ⊕ MRB-306 Phase 2a — AND A CLASS THAT IS NOT LIVE HAS NO ACTIVITY.
    # Design's `11h/Sc5` is `state: 'nowork'` with `last: '2 days ago'`, which
    # is a class with no work set and a submission against it. The seam cannot
    # produce it (no papers means no matrix columns means no stamps), so the
    # populated fixture would otherwise be the ONLY classes page in existence
    # where the non-live activity line is never drawn. See `_no_activity`.
    classes = [c if c["state"] == "live" else _no_activity(c) for c in classes]
    payload["CLASSES"] = classes
    payload.update(
        TEMPLATES=templates,
        classCount=len(classes),
        studentCount=sum(c["n"] for c in classes),
        liveClassCount=len([c for c in classes if c["state"] == "live"]),
        searchPoolCount=len(data["searchPool"]),
        searchPlaceholder="Search students across all %d classes"
                          % len(classes),
        classId=class_id,
        # ⊕ MRB-306 Phase 2a screen 4, 2 Sep 2026 — WAS `-3`, AND `-3` LEFT
        # THE SCREEN'S ONLY WRITE CONTROL UNDRIVEN.
        #
        # The index is this port's arbitrary pick, not Design's. `-3` is Ben
        # Whitcombe, whose `flag` is false — and Design gates "Send a
        # reminder" on `student.flagged`, so the button did not exist on any
        # fixture. `teacher_behaviour` reported "20/20 control(s) pressed"
        # and had never once pressed the reminder, because a control that
        # does not render cannot be counted as missing.
        #
        # `-12` is Kaleb Anderson, and he is chosen for COVERAGE rather than
        # for being flagged alone: 5 marked, 2 of them late, 6 never
        # submitted and row 0 open. That is every history state the screen
        # can draw — on time, late, nothing in, in progress — where `-3` had
        # only one missing row and no reminder. Strictly more states, none
        # lost.
        studentId=class_id + "-12",
        # Design's `paperId` was `'8rsc1:p1'` — index 1.
        paperIdx=1,
        screen="classes",
    )
    return payload


# ── the empty shapes, which no real database can be relied on to hold ────
#
# ⚑ EMPTY STATES ARE THE HALF OF A PRODUCT THAT SHIPS BROKEN, because the
# person building it always has data. Design's delivery cannot express any of
# them: its sample always has twelve classes, always has marked papers and
# always has eight machine-marked questions, so every guard the rulings just
# added is unreachable from the populated fixture.
#
# These five are CONSTRUCTED rather than found, and that is better than a real
# empty class would be: the shape is exactly the one being tested rather than
# whatever happens to exist in the database this week.
#
# ⛔ NOT A CANDIDATE FOR ANY LIVE PATH, for the same reason the populated
# fixtures are not, and one more: several of these are shapes a real teacher's
# data could never be in at the same time.
# ── ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 2) — ONE FILE, N EMPTY SHAPES ──
#
# ⚑ THE CONTRACT CHANGED FROM ONE SHAPER PER FILE TO ONE OR MORE, and the
# value is now a TUPLE OF `(slug, note, shaper)` TRIPLES rather than a bare
# `(note, shaper)` pair. Every page still MUST appear here — the build reads
# `EMPTY_SHAPES[spec["out"]]` and a missing page is still a KeyError, which is
# the refusal that made the old shape worth having — but a page may now name
# more than one empty state.
#
# ⚠️ `slug` NAMES THE FILE, so it is not decoration. The slug `empty` is
# special: it keeps the spec's OWN `empty_out`/`empty_js`, so all twelve
# existing fixture filenames are byte-identical to what they were and nothing
# downstream moves. Any other slug derives
# `<stem>-<slug>-fixture.html` / `teacher-fixture-<stem>-<slug>.js`.
#
# ⚠️ EXACTLY ONE `empty` SLUG PER PAGE, asserted below. Two would both claim
# the same filename and the second would silently overwrite the first — which
# is precisely the failure the one-shaper-per-file rule was protecting
# against, so the protection is kept rather than dropped along with the rule.
EMPTY_SHAPES = {
    "classes.html": (("empty",
        "no classes IN THE YEAR BEING VIEWED, and that year is a PAST one. "
        "⊕ MRB-287 E1 — THIS FIXTURE CARRIES TWO PROPERTIES, deliberately, "
        "and they are the same teacher: someone whose classes are all last "
        "year's. Before E1 that person could not reach the dashboard at all "
        "— `teacher-live.js` threw `noClasses` whenever the WORKING year was "
        "empty, so the one control that would have helped them was behind "
        "the sentence telling them there was nothing to see. It now throws "
        "only when no OTHER year exists, and this is the state that proves "
        "it: the page mounts, the grid draws Design's own \"No classes\" "
        "panel, the year strip is on screen and pressable, and \"Import "
        "students\" is ABSENT because a finished year is read-only. It is "
        "also the only fixture in the set where `canWrite` is false on the "
        "classes screen.",
        lambda p: _shape_past_year(_shape_no_classes(p))),),
    "class-detail.html": (("empty",
        "a class with no roster — `ROSTER: []`, `n: 0`, `state: 'empty'`. "
        "Design DREW this one (\"No students yet\" and an Import action), so "
        "it should render Design's own empty state rather than a blank. "
        "⊕ MRB-287 E1 — AND IT IS A PAST-YEAR CLASS, a second property on "
        "one fixture rather than a thirteenth and fourteenth. It is what "
        "drives MRB-261's read-only rule on this screen: the shoutout "
        "composer and the bulk-send opener are ABSENT (not disabled), the "
        "header says which year it is with `readOnlyLine`, and the feed "
        "stays — a past year is read-only, not invisible. The four "
        "`shoutout-delete` additions carry `needs_data` and are already "
        "skipped on this fixture, so nothing that was pressed here stops "
        "being pressed.",
        lambda p: _shape_past_year(_shape_no_roster(p))),

     # ── ⊕ THE THIRTEENTH FIXTURE, 2 Sep 2026 (MRB-306 Phase 2a screen 2) ──
     #
     # A LIVE class, with a roster, with work set, and NOBODY HAS HANDED
     # ANYTHING IN. It is the state every class is in between the moment a
     # teacher sets work and the moment the first child answers — so on a
     # normal week it is what this screen looks like on Monday morning — and
     # until now NO fixture in the set held it on THIS screen.
     #
     # ⚠️ WHAT IT ACTUALLY EXERCISES, and why the hole mattered: on this
     # shape `openIn` is "0 of N in", `wMean` is null, `lastP` is null
     # (nothing is marked, so `markedIdx` is empty), `worstTwo` is `[]`,
     # `best` and `imp` are both null so `praise` is empty, and `kChase` is
     # EVERY CHILD IN THE CLASS. Half a dozen null and divide-by-length paths
     # that the populated fixture never reaches and the no-roster fixture
     # cannot reach either — it has no roster to divide by.
     #
     # ⚠️ MY BRIEF SAID THIS IS "`8r/Sc1`'S EXACT SHAPE ON PROD". IT IS NOT,
     # and the fixture is justified WITHOUT that claim rather than on top of
     # it. Measured on prod 2 Sep 2026, `8r/Sc1` (2 members, 2 papers) has
     # submissions on BOTH papers: "Particle model" 1 of 2 in, and
     # "Breathing and gas exchange" 2 of 2 in — the latter from three
     # submission ROWS, because one child has `attempt_no` 1 and 2 and
     # `pickFirstAttempts` collapses them to the earlier. So no class in the
     # working year is currently in this state. It is added because it is a
     # SHAPE THE SEAM REALLY PRODUCES on any ordinary week, not because a
     # class is sitting in it today — which is the honest reason, and the
     # only kind that survives the data changing.
     #
     # ⚠️ AND IT REUSES `_shape_no_submissions` RATHER THAN INVENTING ONE.
     # That shaper already zeroes the matrix AND rewrites each paper's `sub`
     # to "0/N" and `mean` to an em-dash, because a fixture whose paper row
     # says "13/16 · 67%" over a matrix holding nothing is a state no real
     # data can produce. That is exactly the scepticism this fixture is
     # supposed to be built with, already written down and already tested by
     # the assignment screen.
     ("nosubs",
      "a LIVE class with a roster and work set that NOBODY has handed in "
      "\u2014 `colSub: 0`, every cell null, every paper `0/N` and a class "
      "mean of `\u2014`. The Monday-morning shape. It is the only fixture "
      "on this screen where the chase list is the WHOLE class and nothing "
      "is marked, so `lastP`, `worstTwo` and `praise` are all empty at "
      "once.",
      lambda p: _shape_no_submissions(p)),

     # ── ⊕ THE SIXTEENTH, 2 Sep 2026 (screen 5) — THE 26 AUG SHAPE ──────
     #
     # ⚠️ NOT AN EDGE CASE. `load()` prefetches a grid for the marking screen
     # and the questions chart and for nothing else, so EVERY class-detail
     # render in production has `GRID: {}`. The other three class-detail
     # fixtures ship a populated map, which this page can never have — which
     # is exactly why the gate was green through the outage.
     ("gridmissing",
      "no grid fetched at all — `GRID: {}`, which is what this screen "
      "ALWAYS has in production. `renderVals` computes the marking screen's "
      "`paper` block here too, so this is the shape that threw mid-mount on "
      "26 Aug 2026 and put \"Your classes could not be loaded\" over the one "
      "class in the school with work set. It also shows the assignments "
      "table's weak column as it really is on this page: an em-dash on "
      "every row, because the grids it would need are not here.",
      lambda p: _shape_grid_absent(p)),),
    "digest.html": (("empty",
        "a class with students and no work set — `PAPERS: []`, `WEEKS: []`, "
        "`state: 'nowork'`. Design's README: \"classes with no work set have "
        "no week bar\", so the rail must be ABSENT and not drawn empty.",
        lambda p: _shape_no_work(p)),),
    "assignment.html": (("empty",
        "a paper nobody submitted — the grid is present, `submitted: 0` and "
        "every `qpct` is null. This is where \"blanks over invented numbers\" "
        "is tested: nothing may render as 0%, as `null%`, or as a full bar. "
        "⊕ 2 Sep 2026 — IT NO LONGER CARRIES THE FOURTH GLYPH, and the "
        "reason is in `_shape_no_submissions`: a whole ROW of "
        "`is_correct IS NULL` is a shape the seam cannot produce, and it "
        "contradicted this fixture's own SUBMITTED 0/16 tile.",
        lambda p: _shape_no_submissions(p)),

     # ── ⊕ THE FOURTEENTH FIXTURE, 2 Sep 2026 (screen 5) ─────────────────
     ("written",
      "a REAL-SHAPED paper: FIVE questions, SEVEN marks, and Q4 written. "
      "It is the only fixture in the set whose `max` is not 8 and whose "
      "question count is not 8, so it is the only one that can tell the "
      "`/max` ruling apart from the `/8` hardcode it replaced, the only one "
      "that renders `qLine`'s \"N questions, M marks\" branch, and the only "
      "one that puts a column template other than eight on the class grid. "
      "It also carries the fourth grid state where the seam really puts it "
      "— one COLUMN, every child who submitted — and a lowest-scoring "
      "question with NO stem snapshot, which is what drives the reteach "
      "banner's empty-text guard.",
      lambda p: _shape_written_paper(p)),

     # ── ⊕ THE FIFTEENTH, 2 Sep 2026 (screen 5) ─────────────────────────
     ("gridmissing",
      "ONE assignment, still open, and no grid fetched for it — so "
      "`gridFor` asks for a key that is NOT IN THE MAP. Key-absent is a "
      "different branch from `insights-empty`'s key-present-null, and it is "
      "the branch that threw live on 26 Aug 2026. Reachable here because "
      "`load()` prefetches `newestMarkedIdx(papers)` and skips the fetch at "
      "-1, while `paper()` falls back to `list[0]` — a class whose papers "
      "are all still open lands between the two.",
      lambda p: _shape_no_marked_paper(p)),),
    "insights.html": (("empty",
        "a grid that was never prefetched — `GRID[key]: null`, the seam's "
        "deliberate \"not fetched yet\". It must render as PENDING and never "
        "as a grid of zeros.",
        lambda p: _shape_grid_pending(p)),),
    "student-detail.html": (("empty",
        "a student with no submissions at all, on a class that has papers — "
        "every cell null, so the history renders four \"Nothing in\" rows "
        "rather than a fabricated date.",
        lambda p: _shape_no_submissions(p)),),
}

# ⚠️ THE `empty` SLUG IS UNIQUE PER PAGE, AND THE BUILD REFUSES OTHERWISE.
# Two `empty` variants on one page would both resolve to that page's
# `empty_out`, and the second would overwrite the first with no error at all
# — a fixture silently replaced by a different one, which is the exact class
# of failure the one-shaper-per-file rule used to make impossible. Dropping
# that rule without replacing its guarantee would have been a downgrade, so
# the guarantee is asserted here instead.
for _out, _variants in EMPTY_SHAPES.items():
    _slugs = [v[0] for v in _variants]
    if len(_slugs) != len(set(_slugs)):
        raise SystemExit(
            "build_teacher_port.py: EMPTY_SHAPES[%r] names the same slug "
            "twice (%s). Each slug names a filename, so a duplicate "
            "overwrites a fixture rather than adding one." % (_out, _slugs))
    if _slugs.count("empty") != 1:
        raise SystemExit(
            "build_teacher_port.py: EMPTY_SHAPES[%r] must name exactly one "
            "`empty` variant — that is the one keeping the spec's own "
            "`empty_out`/`empty_js` filenames — and it names %d."
            % (_out, _slugs.count("empty")))


def variant_files(spec, slug):
    """(page filename, data filename) for one empty variant of one screen.

    `empty` keeps the spec's own names so the twelve original fixtures do not
    move; anything else derives from the page's stem.
    """
    if slug == "empty":
        return spec["empty_out"], spec["empty_js"]
    stem = spec["out"][:-len(".html")]
    return ("%s-%s-fixture.html" % (stem, slug),
            "teacher-fixture-%s-%s.js" % (stem, slug))


def _no_activity(k):
    """Design's `last` string, corrected where the seam could not produce it.

    ⊕ MRB-306 Phase 2a, 2 Sep 2026. `last` is `relativeTime(lastIso)` OR the
    words "No activity yet", and `teacher-live.js` derives `lastIso` from the
    newest submission across the roster. A class with no roster has no
    submissions, and a class with no papers has no matrix columns to hold a
    submission stamp — so for BOTH non-live states the seam can only ever
    produce the words.

    Design's sample says otherwise: her `nowork` class carries "2 days ago",
    which is a class with no work set and a submission against it. That is not
    a value the live page can reach, and a fixture that carries it hides every
    defect on the path that renders the words — which is how "Last activity No
    activity yet" survived a week of green gates. See the `cards`/`activity`
    ruling.

    ⚠️ THE `live` PATH IS NOT COVERED BY THIS. A class with students and work
    set that nobody has handed in yet is `live` with `lastIso` null, and no
    fixture in the set holds that shape — Design's twelve are all populated.
    Stated rather than implied.
    """
    return dict(k, last="No activity yet")


def _blank_class(payload, cid, state, keep_papers):
    k = [c for c in payload["CLASSES"] if c["id"] == cid][0]
    k = _no_activity(dict(k, state=state, n=0 if state == "empty" else k["n"],
                          week=[0, 0] if state != "live" else k["week"]))
    payload["CLASSES"] = [k if c["id"] == cid else c
                          for c in payload["CLASSES"]]
    if state == "empty":
        payload["ROSTER"][cid] = []
    if not keep_papers:
        payload["PAPERS"][cid] = []
        payload["WEEKS"][cid] = []
        payload["MATRIX"][cid] = dict(
            rows=[], cols=0, colSub=[], colMean=[], colOnTime=[], colAsked=[],
            colLate=[], colLateUnknown=[], markedIdx=[], studentAvg={},
            markedSub=0, markedOnTime=0, markedLate=0, markedLateUnknown=0,
            markedPct=None, classMean=None, byId={})
        payload["GRID"] = {kk: v for kk, v in payload["GRID"].items()
                           if not kk.startswith(cid + ":")}
    return payload


def _shape_past_year(p):
    """The year in view is a FINISHED one — MRB-261's read-only state.

    ⚑ THE ONLY SHAPE IN THIS FILE THAT MAKES A PAGE LESS CAPABLE, and it is
    the one no live test can be relied on to reach: it needs a school with two
    academic years and a teacher holding classes in the older one, which is a
    fact about a database rather than about the code.

    Everything here is what `teacher-live.js` computes when `pickYear` lands
    on a past year — `canWrite` false, the read-only sentence, and the options
    list flipped so the way BACK to the working year is what the selector
    offers. That last one is why `hasOtherYears` replaced `hasPastYears`: from
    here the year a teacher wants is a FUTURE one relative to the one in view.
    """
    p = json.loads(json.dumps(p))
    past = DESIGN_SCALARS["yearOptions"][0]           # the 2025-26 row
    p.update(
        viewingIsPast=True,
        canWrite=False,
        # A binding, never a literal — the same rule the live seam follows.
        readOnlyLine="%s is read-only" % past["name"],
        viewingYearLabel="Viewing %s · read-only" % past["name"],
        # Viewing the past year, so the option is the working one.
        yearOptions=[dict(id="fixture-year-2026-27",
                          name=DESIGN_SCALARS["yearLabel"])],
        hasOtherYears=True,
        pastYearsLabel="Other years",
        yearParam=past["id"],
    )
    # Every class on screen belongs to the year being viewed, so the cards
    # say so too. Derived from the same row, never typed per card.
    p["CLASSES"] = [dict(c, yearName=past["name"]) for c in p["CLASSES"]]
    return p


def _shape_no_classes(p):
    p = json.loads(json.dumps(p))
    p.update(CLASSES=[], MATRIX={}, ROSTER={}, PAPERS={}, WEEKS={}, GRID={},
             FEED={}, searchPool=[], searchPoolCount=0, classCount=0,
             studentCount=0, liveClassCount=0, classId=None, studentId=None,
             paperIdx=None,
             searchPlaceholder="Search students across all 0 classes")
    return p


def _shape_no_roster(p):
    p = json.loads(json.dumps(p))
    cid = p["classId"]
    p = _blank_class(p, cid, "empty", keep_papers=False)
    p["FEED"] = {cid: []}
    p["studentId"] = None
    return p


def _shape_no_work(p):
    p = json.loads(json.dumps(p))
    cid = p["classId"]
    p = _blank_class(p, cid, "nowork", keep_papers=False)
    p["FEED"] = {cid: []}
    p["studentId"] = None
    return p


def _shape_no_submissions(p):
    """Every cell null, and ONE cell holding the fourth grid state."""
    p = json.loads(json.dumps(p))
    cid = p["classId"]
    mx = p["MATRIX"][cid]
    n = mx["cols"]
    for r in mx["rows"]:
        r["scores"] = [None] * n
        r["max"] = [None] * n
        r["pct"] = [None] * n
        r["stampShort"] = [None] * n
        r["submitted"] = [False] * n
        # ⚠️ TRI-STATE, AND THE FIXTURE HAS TO CARRY THE THIRD VALUE. `null`
        # is "no stamp and no deadline", which is every pre-22-Aug-2026 row —
        # and Design's sample has none, so nothing else in the set drives the
        # branch that must NOT render it as "on time".
        r["late"] = [None] * n
        r["inWeek"] = False
    mx["byId"] = {r["sid"]: r for r in mx["rows"]}
    mx["colSub"] = [0] * n
    mx["colMean"] = [None] * n
    mx["colOnTime"] = [0] * n
    mx["colLate"] = [0] * n
    mx["colLateUnknown"] = [0] * n
    mx["studentAvg"] = {r["sid"]: None for r in mx["rows"]}
    mx["markedSub"] = 0
    mx["markedOnTime"] = 0
    mx["markedLate"] = 0
    mx["markedLateUnknown"] = 0
    mx["markedPct"] = None
    mx["classMean"] = None
    # ⊕ THE PAPER ROW HAS TO AGREE WITH THE MATRIX, and it did not. `sub` and
    # `mean` are strings Design's `papersFor` built from Design's own
    # numbers ("13/16", "67%"), and zeroing the matrix underneath them left
    # the marking screen showing SUBMITTED 13/16 and CLASS MEAN 67% beside an
    # ON TIME tile reading "Nothing submitted yet". A fixture that contradicts
    # itself is a frame a reviewer cannot trust, and it is the frame this
    # empty shape exists to produce.
    for i, paper in enumerate(p["PAPERS"].get(cid, [])):
        paper["sub"] = "0/" + str(mx["colAsked"][i] if i < len(mx["colAsked"])
                                  else 0)
        paper["mean"] = "\u2014"
    for r in p["ROSTER"][cid]:
        r["avg"] = None
        r["inWeek"] = False
        r["last"] = "No activity yet"
    for key, g in list(p["GRID"].items()):
        if not key.startswith(cid + ":") or g is None:
            continue
        g["submitted"] = 0
        g["qpct"] = [None] * len(g["stems"])
        g["qCorrect"] = [0] * len(g["stems"])
        g["qMarked"] = [0] * len(g["stems"])
        g["qUnmarkable"] = [0] * len(g["stems"])
        g["qBlank"] = [0] * len(g["stems"])
        for row in g["rows"]:
            row["raw"] = [2] * len(g["stems"])
            row["score"] = "—"
            row["submitted"] = False
        # ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 5) — THE FOURTH GLYPH WAS
        # PARKED HERE AND IT COULD NOT BE HERE.
        #
        # ⛔ WHAT THIS USED TO DO: `g["rows"][0]["raw"] = [3] * len(stems)`,
        # `submitted = True`, `g["submitted"] = 1`. Two things were wrong with
        # it, and the second is the one that matters.
        #
        # It contradicted its own screen. This shape is "a paper NOBODY
        # submitted"; the tile above the grid read SUBMITTED 0/16 while the
        # grid underneath showed one child with eight answered cells.
        #
        # And a WHOLE ROW of `is_correct IS NULL` is a shape the seam cannot
        # produce. Whether an answer can be machine-marked is a property of
        # the QUESTION — a written or self-marked question is written for
        # every child who answers it — so NULL clusters in a COLUMN. One
        # child self-marking all eight of eight machine-markable questions
        # is Design-fiction geometry, and it was the only place any gate had
        # ever seen `cellStyle(3)`.
        #
        # The fourth state now lives on `assignment-written-fixture.html`, as
        # Q4 of a five-question paper, for every child who handed it in. See
        # `_shape_written_paper`.
    p["FEED"] = {cid: []}
    return p


def _mean(vals):
    """Design's own averages are recomputed with ONE formula, not two.

    Design rounds a percentage per cell and then averages, and its
    `studentAvg` disagrees with the mean of its own `pct[]` on 9 of 16 rows.
    That is harmless in a sample nobody adds up; it is not harmless in a
    fixture that exists to prove a number on screen came from the row beneath
    it. Every average a reshaped fixture touches is therefore rebuilt from the
    cells with this one function, so the fixture cannot disagree with itself.
    """
    vals = [v for v in vals if v is not None]
    return round(sum(vals) / len(vals)) if vals else None


def _reaverage(p, cid):
    """Recompute every average in one class from its own matrix cells."""
    mx = p["MATRIX"][cid]
    for c in range(mx["cols"]):
        mx["colMean"][c] = _mean([r["pct"][c] for r in mx["rows"]])
        mx["colSub"][c] = sum(1 for r in mx["rows"] if r["submitted"][c])
    mx["studentAvg"] = {r["sid"]: _mean(r["pct"]) for r in mx["rows"]}
    mx["classMean"] = _mean(mx["colMean"])
    marked = mx["markedIdx"]
    mx["markedSub"] = sum(mx["colSub"][i] for i in marked)
    mx["markedOnTime"] = sum(mx["colOnTime"][i] for i in marked)
    mx["markedLate"] = sum(mx["colLate"][i] for i in marked)
    mx["markedLateUnknown"] = sum(mx["colLateUnknown"][i] for i in marked)
    mx["markedPct"] = (round(mx["markedOnTime"] / mx["markedSub"] * 100)
                       if mx["markedSub"] else None)
    mx["byId"] = {r["sid"]: r for r in mx["rows"]}
    for r in p["ROSTER"][cid]:
        r["avg"] = mx["studentAvg"].get(r["id"])
    return p


# ⚑ THE PAPER THAT IS NOT EIGHT QUESTIONS OUT OF EIGHT MARKS ─────────────
#
# ⛔ EVERY OTHER FIXTURE IN THE SET IS 8 QUESTIONS, 8 MARKS, 1 MARK EACH,
# because Design's `STEMS` is one list of eight used for every paper in every
# subject and its every score is `n/8`. Three separate rulings exist to take
# that apart — `qLine` built from the paper, `score` over the row's own `max`,
# and the grid's column template — and NONE of them could be told apart from
# the hardcode it replaced, because on 8-questions-out-of-8 the right answer
# and the wrong one print the same characters. A gate cannot see a fix it
# cannot distinguish from the bug.
#
# ⚠️ MEASURED, NOT GUESSED. On the TEST project, 2 Sep 2026: every
# `assignment_submissions.max_score` in the database is 10, and the only
# assignment carrying `assignment_questions` rows has FOUR of them. So a real
# paper is neither eight questions nor out of eight, and the branch that says
# "5 questions, 7 marks" — the one real data takes — had never been rendered
# anywhere.
#
# ⚠️ AND IT CARRIES THE FOURTH GRID STATE, WHICH USED TO SIT SOMEWHERE IT
# COULD NOT REALLY BE. `_shape_no_submissions` put `is_correct IS NULL` on one
# CHILD'S WHOLE ROW. Whether an answer can be machine-marked is a property of
# the QUESTION, not of the child: a written or self-marked question is written
# for everyone who answers it, so NULL clusters in a COLUMN and never in a
# row. (It also sat under a tile reading "SUBMITTED 0/16" while the grid it
# was in said one child had submitted.) Here it is Q4, for every child who
# handed the paper in, which is the shape the seam actually produces.
#
# ⚠️ AND Q2 CARRIES NO STEM TEXT. `assignment_question_attempts.question_text`
# is nullable and `buildGrid` leaves a column's `text` empty rather than
# inventing a placeholder. Q2 is also the lowest-scoring question, so this is
# the fixture that drives the reteach banner with nothing to name — the
# "Q4 — . Only 23% …" sentence.
#
# WHERE THE MARKS COME FROM, stated rather than implied: Q1-Q3 are worth 2
# each and Q5 is worth 1, so the paper's automatic total is 7. Q4 is the
# written question and contributes NOTHING to it — which is what the
# SUBMITTED tile's own subtitle, "Marked automatically", means. Nothing here
# invents a self-mark.
_WRITTEN_TARIFF = (2, 2, 2, None, 1)          # None = the written question
_WRITTEN_FROM = (0, 3, 2, None, 7)            # which of Design's 8 each maps


def _shape_written_paper(p):
    """A 5-question paper out of 7 marks, with one written question."""
    p = json.loads(json.dumps(p))
    cid = p["classId"]
    idx = p["paperIdx"]
    key = "%s:%d" % (cid, idx)
    g = p["GRID"][key]
    mx = p["MATRIX"][cid]
    n = len(_WRITTEN_TARIFF)
    max_score = sum(t for t in _WRITTEN_TARIFF if t is not None)

    stems = []
    for i, src in enumerate(_WRITTEN_FROM):
        old = g["stems"][src] if src is not None else g["stems"][3]
        stems.append(dict(old, id="Q%d" % (i + 1), idx=i))
    # Q2's snapshot was never written. Q4 is the written question and its own
    # stem text is Design's; only its ANSWERS are unmarkable.
    stems[1]["text"] = ""

    correct = [0] * n
    marked = [0] * n
    unmarkable = [0] * n
    blank = [0] * n
    rows, submitted = [], 0
    for old in g["rows"]:
        if not old["submitted"]:
            # ⚠️ `qBlank` COUNTS BLANKS AMONG THE CHILDREN WHO HANDED IN, and
            # not the children who did not. `buildGrid` increments it only
            # inside its submitted branch, so a fixture that counted the
            # absentees here would carry a number the seam cannot produce —
            # which is the whole failure mode this fixture exists to correct.
            rows.append(dict(old, raw=[2] * n, score="—"))
            continue
        submitted += 1
        raw, score = [], 0
        for qi, src in enumerate(_WRITTEN_FROM):
            if src is None:                       # the written question
                raw.append(3)
                unmarkable[qi] += 1
                continue
            v = old["raw"][src]
            raw.append(v)
            if v == 1:
                correct[qi] += 1
                marked[qi] += 1
                score += _WRITTEN_TARIFF[qi]
            elif v == 0:
                marked[qi] += 1
            else:
                blank[qi] += 1
        rows.append(dict(old, raw=raw,
                         score="%d/%d" % (score, max_score)))

    qpct = [round(correct[i] / marked[i] * 100) if marked[i] else None
            for i in range(n)]
    p["GRID"] = {key: dict(
        rows=rows, qpct=qpct, stems=stems, submitted=submitted,
        roster=g["roster"], qcount=n, maxScore=max_score,
        qCorrect=correct, qMarked=marked,
        qUnmarkable=unmarkable, qBlank=blank,
        # The seam's own sentence, on the branch `maxScore != qcount` takes.
        qLine="%d questions, %d marks" % (n, max_score),
    )}

    # The matrix column and the paper row have to agree with those cells.
    for r in mx["rows"]:
        gr = [x for x in rows if x["id"] == r["sid"]][0]
        if gr["score"] == "—":
            r["scores"][idx] = r["max"][idx] = r["pct"][idx] = None
            r["submitted"][idx] = False
        else:
            got = int(gr["score"].split("/")[0])
            r["scores"][idx] = got
            r["max"][idx] = max_score
            r["pct"][idx] = round(got / max_score * 100)
            r["submitted"][idx] = True
    _reaverage(p, cid)
    paper = p["PAPERS"][cid][idx]
    paper["sub"] = "%d/%d" % (submitted, mx["colAsked"][idx])
    paper["mean"] = "%d%%" % mx["colMean"][idx]
    return p


# ⚑ A GRID KEY THAT IS NOT THERE AT ALL ──────────────────────────────────
#
# ⛔ THIS IS THE 26 AUGUST 2026 BREAKAGE, AND NO FIXTURE HELD IT.
# `insights-empty` covers key-PRESENT-and-null; nothing covered key-ABSENT,
# which is a different branch of `gridFor` and was the one that threw.
# `renderVals` computes the marking screen's `paper` block on EVERY screen,
# `load()` prefetches grids only for marking and insights, and the first
# `gridFor` body read `MRB_PICK('GRID', key)` — which throws on an absent key.
# So opening class-detail on any class WITH an assignment died mid-mount and
# showed "Your classes could not be loaded". It hit the one class in the
# school that had work set, which is the only class anybody opened.
#
# ⚠️ AND `GRID: {}` IS NOT AN EDGE CASE ON THIS SCREEN — IT IS THE ONLY STATE
# IT EVER HAS. `load()` fetches a grid for the marking screen and for the
# questions chart, and for nothing else. Every class-detail render in
# production therefore has an EMPTY grid map. The populated class-detail
# fixtures ship a full one, which that page cannot have, and that is precisely
# why `teacher_behaviour` could be green through the outage.
def _shape_grid_absent(p):
    """No grid fetched at all — every class-detail render in production."""
    p = json.loads(json.dumps(p))
    p["GRID"] = {}
    return p


# ⚑ THE MARKING SCREEN'S OWN KEY-ABSENT STATE ────────────────────────────
#
# ⛔ AND IT IS REACHABLE, WHICH TOOK FINDING. On marking, `load()` prefetches
# `asked == null ? newestMarkedIdx(papers) : asked`, and skips the fetch
# entirely when that is -1. `METHODS["paper"]` then falls back to
# `newestMarkedIdx(list) >= 0 ? list[n] : list[0]` — so a class whose papers
# are ALL still open prefetches nothing and then asks for `<class>:0`. The
# seam and the page disagree by exactly one paper, and the answer has to be
# the documented null rather than a throw.
#
# ⚠️ ONE PAPER, NOT TWELVE. The obvious shaping — flip all twelve of Design's
# papers to `when: 'upcoming'` — encodes a state real data cannot hold: their
# deadlines run backwards a week at a time, so eleven of the twelve would be
# "still open" with a due date already past. A class with ONE open paper is
# both the honest reading and the real one: it is `8r/Sc1` in the week work
# is first set, and on 2 Sep 2026 that class's newest paper is due tomorrow
# with both children already in.
#
# Everything downstream of "nothing is past its deadline" follows: nothing is
# marked, nothing can be late, and `markedIdx` is empty.
def _shape_no_marked_paper(p):
    """One assignment, still open, and no grid fetched for it."""
    p = json.loads(json.dumps(p))
    cid = p["classId"]
    papers = p["PAPERS"][cid]
    keep = 0
    for i, pr in enumerate(papers):
        if pr["when"] == "upcoming":
            keep = i
            break
    paper = dict(papers[keep], idx=0, weekIdx=0, weekOfYear=1)
    p["PAPERS"][cid] = [paper]

    mx = p["MATRIX"][cid]
    for r in mx["rows"]:
        for f in ("scores", "max", "pct", "stampShort", "submitted", "late"):
            r[f] = [r[f][keep]]
        # An open paper cannot be late: there is no deadline behind it yet.
        r["late"] = [False if r["submitted"][0] else None]
    mx["cols"] = 1
    for f in ("colSub", "colMean", "colOnTime", "colAsked",
              "colLate", "colLateUnknown"):
        mx[f] = [mx[f][keep]]
    mx["colOnTime"] = [mx["colSub"][0]]
    mx["colLate"] = [0]
    mx["colLateUnknown"] = [0]
    mx["markedIdx"] = []
    _reaverage(p, cid)

    wks = p["WEEKS"].get(cid) or []
    if wks:
        p["WEEKS"][cid] = [dict(wks[0], idx=0, weekOfYear=1, label="Week 1",
                                range=paper["range"], now=True)]
    # Nothing fetched, and no paper asked for — the two facts together are
    # what makes `gridFor` reach for a key that is not there.
    p["GRID"] = {}
    p["paperIdx"] = None
    return p


def _shape_grid_pending(p):
    """Every grid present as a KEY and null as a VALUE — "not fetched yet"."""
    p = json.loads(json.dumps(p))
    p["GRID"] = {k: None for k in p["GRID"]}
    return p


# ══════════════════════════════════════════════════════════════════════════
#  live regions Design drew no counterpart for
# ══════════════════════════════════════════════════════════════════════════

def _element_by_id(src, el_id):
    """The outer HTML of the one element carrying `id="<el_id>"`.

    A tag-depth scan rather than a parser: the four originals are hand-written
    HTML with no self-closing custom elements and no `<script>` inside any of
    the regions named, which was checked rather than assumed.
    """
    m = re.search(r'<(\w+)([^>]*\sid="%s")' % re.escape(el_id), src)
    if not m:
        return None
    tag = m.group(1)
    # ⚠️ VOID ELEMENTS HAVE NO CLOSING TAG, and the depth scan below waits for
    # one for ever. `import.html`'s real `<input type="file">` is the whole
    # reason the import wizard survives the port, and it was the first thing
    # this refused to find.
    if tag.lower() in ("input", "img", "br", "hr", "meta", "link", "source"):
        return src[m.start():src.index(">", m.end()) + 1]
    i, depth = m.start(), 0
    pat = re.compile(r"</?%s\b" % re.escape(tag), re.I)
    while True:
        mm = pat.search(src, i)
        if not mm:
            return None
        if src[mm.start():mm.start() + 2] == "</":
            depth -= 1
            if depth == 0:
                return src[m.start():src.index(">", mm.end()) + 1]
        else:
            depth += 1
        i = mm.end()


def live_regions(spec, source_html):
    """Every live region this page's hand-written original carried alone.

    ⚑ "LIVE LOGIC WINS, DESIGN'S PRESENTATION WINS" — and these are the
    regions where there is no Design presentation to win. Lifted VERBATIM, by
    element id, so the port DELETES NOTHING a teacher can currently reach.

    ⚠️ THEY ARRIVE WITHOUT THE ORIGINAL'S CSS, DELIBERATELY. Each hand-written
    page carries a ~600-line `<style>` block that opens
    `* { box-sizing: border-box; margin: 0; padding: 0 }` and
    `body { display: none }`. Emitting it beside Design's stylesheet would not
    keep the live styling — it would reset Design's own page out from under
    it, and the port would ship a dashboard that no longer looks like Design's
    at all.

    So these are a SAFETY NET rather than a finished surface: nothing is
    deleted, `shared/teacher-live.js` can reach any of them by the id it
    always used, and the right long-term home for each is Design's own
    presentation. Every one is named in the build's own output so the list
    cannot quietly grow or shrink.
    """
    import teacher_rulings as R

    wanted = R.LIVE_REGIONS.get(spec.get("retire") or "", ())
    if not wanted:
        return "", []
    kept, names = [], []
    for el_id, why in wanted:
        frag = _element_by_id(source_html, el_id)
        if frag is None:
            raise SystemExit(
                "build_teacher_port.py: %s carries the live region #%s "
                "(%s), and it is not in the hand-written original at %s.\n"
                "  An id that has been renamed silently carries NOTHING, and "
                "a region that silently carries nothing is a deleted error "
                "state. Re-anchor teacher_rulings.LIVE_REGIONS."
                % (spec["out"], el_id, why.split(".")[0], spec["retire"]))
        if source_html.count('id="%s"' % el_id) != 1:
            raise SystemExit(
                "build_teacher_port.py: id=\"%s\" occurs %d times in %s. A "
                "region is lifted by id and an ambiguous id lifts the wrong "
                "one." % (el_id, source_html.count('id="%s"' % el_id),
                          spec["retire"]))
        kept.append("  <!-- %s -->\n  %s" % (why, frag))
        names.append(el_id)
    return ("<!-- ── LIVE REGIONS Design drew no counterpart for ──────────\n"
            "     Lifted verbatim, by element id, out of the hand-written\n"
            "     %s that this page replaces (now retired under\n"
            "     docs/ks3/retired/). Hidden by default and WITHOUT the\n"
            "     original's stylesheet — see `live_regions` in\n"
            "     build_teacher_port.py for why carrying that CSS would\n"
            "     reset Design's page out from under it.\n"
            "     Nothing here is deleted; shared/teacher-live.js reaches\n"
            "     each by the id it always used. -->\n"
            "<div id=\"mrb-teacher-live-regions\" hidden>\n%s\n</div>\n"
            % (spec["retire"], "\n".join(kept))), names


# ══════════════════════════════════════════════════════════════════════════
#  the page
# ══════════════════════════════════════════════════════════════════════════

# ── the data seam ────────────────────────────────────────────────────────
#
# No fallbacks, no defaults, no `||`. A missing key is a THROWN ERROR and a
# blank page, deliberately: the alternative to a blank page is one teacher
# shown another teacher's class list, or a child's marks under the wrong
# child's name, and a page that is confidently wrong about a class is worse
# than a page that is plainly broken.
_SEAM = """/* No data reaches this page except through here, and there is no
   fallback. A missing key is a THROWN ERROR and a blank page, deliberately:
   Design's delivery is a SAMPLE — twelve invented classes and fifty-four
   invented children — and the alternative to a blank page is a teacher shown
   a class they do not teach, with names that look real. */
function MRB_DATA(k){var d=window.__MRB_DATA__;
  if(!d||!(k in d))throw new Error('teacher page: no data for "'+k+'"');
  return d[k];}
/* Several of Design's methods look a value up PER CLASS — the score matrix,
   the roster, the assignment list, one paper's question grid, one class's
   weeks. The id is part of the question, so it is part of the error. */
function MRB_PICK(mapKey, id){var m=MRB_DATA(mapKey);
  if(!m||!(id in m))throw new Error('teacher page: no '+mapKey+' for "'+id+'"');
  return m[id];}
/* One query parameter, read once. `teacher-live.js` reads the same three
   (`class`, `student`, `paper`) and derives the screen from the PATH, so
   these two must not disagree about what a URL means. */
function MRB_Q(name){
  return new URLSearchParams(window.location.search).get(name) || '';}
/* The sandbox thread. `teacher/classes.html` has always done this on every
   card click; dropping it would send a teacher testing against the test
   project back into production data one navigation later. */
function MRB_ENV(){var c=window.MrBadmusConfig;
  return (c&&c.environment==='test')?'test':'';}
/* ⚠️ THE FILENAMES ARE THE CONTRACT. `teacher-live.js` maps the PATH back to a
   screen (`SCREEN_BY_PAGE`) and prefetches only the grids that screen draws,
   so a link to the wrong file is a page that stays pending for ever with
   nothing in the console. The two maps are inverses and must stay so. */
/* ⊕ 2 Sep 2026 (MRB-306) — `today` and `timetable` are on this map and are
   NOT emitted by this generator. They are the two HAND-WRITTEN teacher pages
   of those names, and v3's chrome links to them: the top-bar tab strip and
   the class screen's "Back to today". The filenames are the ones the port
   will emit when Design's Today and Timetable screens are ported, so these
   links survive that unit unchanged. `teacher-live.js`'s `SCREEN_BY_PAGE`
   does not name either — it falls back to `"classes"` for an unknown page,
   which is what those two hand-written pages have always been served. */
var MRB_PAGE = {classes:'classes.html', 'class':'class-detail.html',
  student:'student-detail.html', marking:'assignment.html',
  digest:'digest.html', 'import':'import.html', insights:'insights.html',
  today:'today.html', timetable:'timetable.html'};
function MRB_GO(screen, params){
  var f = MRB_PAGE[screen];
  if(!f)throw new Error('teacher page: no page for screen "'+screen+'"');
  var q = [], env = MRB_ENV(), k;
  for(k in params){ if(params[k]!=null&&params[k]!=='')
    q.push(encodeURIComponent(k)+'='+encodeURIComponent(params[k])); }
  if(env)q.push('env='+env);
  window.location.href = '/teacher/'+f+(q.length?('?'+q.join('&')):'');}
/* ⊕ MRB-304 — the wordmark leaves the teacher portal entirely. Design hung
   `goClasses` on the brand mark, which on classes.html was a press that
   reloaded the page the teacher was already on; Mide's ruling is that
   "MrBadmusAI" is the site's name and goes to the site's front door, from
   every teacher page, unconditionally. A NAMED helper rather than an inline
   `location.href`, like every other navigation here, so `teacher_behaviour`
   can stub it and press the control for real without navigating the fixture
   away mid-sweep. No `env` thread and no query string: the homepage is public
   and has no teacher state to carry. */
function MRB_HOME(){window.location.href = '/index.html';}
/* Design's Back buttons chose between two screens from state. Six URLs later
   the browser knows the real answer — and a page opened from a bookmark has no
   state to consult. Falls through to the class list rather than being a dead
   press. */
function MRB_BACK(){if(window.history.length>1){window.history.back();return;}
  MRB_GO('classes',{});}
/* The composer opens on a template, and Design opens it on `3`. The six
   templates are the DB enum now and their ids are strings, so `3` selects
   nothing and looks like a rendering bug rather than a data one. */
function MRB_FIRST_TEMPLATE(){var t=MRB_DATA('TEMPLATES');
  return (t&&t[0])?t[0].id:'';}
/* Which paper is "the newest marked one". Taken from teacher-live.js rather
   than reimplemented: Design reaches for index 1 and assumes it exists and is
   closed, which is true only when there is exactly one open paper. Two answers
   to this question is how the page and the prefetch disagree about which grid
   was fetched. */
function MRB_NEWEST_MARKED(papers){
  var L=window.MrBadmusTeacherLive;
  if(L&&L.newestMarkedIdx)return L.newestMarkedIdx(papers||[]);
  for(var i=0;i<(papers||[]).length;i++){
    if(papers[i].when==='marked')return i;}
  return -1;}
/* "N late of M marked". ⚠️ AND THE UNKNOWNS ARE SHOWN, NOT HIDDEN. `is_late`
   is NULL on every submission written before 22 Aug 2026 and on any with no
   deadline, so "unknown" is a real population and not a rounding error. Folded
   into "late" it overstates; folded into "on time" it understates; left out
   entirely it is a number a teacher reads as a zero. */
/* A matrix for NO CLASS. `renderVals` reads `matrixFor(k)` unconditionally on
   every screen, and a teacher with no classes at all is a real first day
   rather than an error — so the shape exists and every figure in it is empty.
   Zero is NOT the same as empty here: `classMean: 0` would be a claim about
   how a class did, and there is no class. */
/* A class for NO CLASS. `renderVals` reads `k.code` in seven places, so a
   null cannot travel: `crumb`, `backToClass`, `student.meta`, `insSub`,
   `insScopeTabs`, `digestSub` and `chart.scopeLabel` all dereference it
   unconditionally. An em dash and zeros, so the page draws itself with
   nothing in it rather than throwing. */
function MRB_NO_CLASS(){return {id:'',code:'\u2014',subject:'',year:'',
  ks:'',n:0,week:[0,0],last:'No activity yet',state:'empty'};}
function MRB_EMPTY_MATRIX(){return {rows:[],cols:0,colSub:[],colMean:[],
  colOnTime:[],colAsked:[],colLate:[],colLateUnknown:[],markedIdx:[],
  studentAvg:{},markedSub:0,markedOnTime:0,markedLate:0,markedLateUnknown:0,
  markedPct:null,classMean:null,byId:{}};}
function MRB_LATE_LINE(late, unknown, total, noun){
  var s = (late||0) + ' late of ' + (total||0) + ' ' + noun;
  return unknown ? (s + ' · ' + unknown + ' timing unknown') : s;}
/* "N on time", where UNKNOWN is neither. The companion to MRB_LATE_LINE and
   the same ruling seen from the other side: `is_late` is NULL on every
   submission written before 22 Aug 2026, so a paper can have thirteen
   submissions and nothing known about the timing of any of them. Counting
   those as on time flatters; counting them as late accuses; printing the raw
   `colOnTime` prints 0 and tells a teacher that nobody was on time. When
   nothing is known there is no answer, and an em dash is what "no answer"
   looks like everywhere else on this dashboard. */
function MRB_ONTIME_VALUE(onTime, late){
  var known = (onTime||0) + (late||0);
  return known ? String(onTime||0) : '—';}
function MRB_ONTIME_SUB(onTime, late, unknown, noun){
  var known = (onTime||0) + (late||0);
  if(!known){ return (unknown||0)
    ? ((unknown||0) + ' submission' + ((unknown||0) === 1 ? '' : 's') +
       ', timing not recorded')
    : 'Nothing submitted yet'; }
  return MRB_LATE_LINE(late, unknown, known, noun || 'submitted');}

/* == THE SHOUTOUT COMPOSER, WIRED =======================================

   Design's composer and its bulk sheet both ended in `this.ping(...)`: a
   confirmation of a write that never happened. The write path exists and
   always did - `MrBadmusTeacherData.insertClassShoutout` - and these six
   helpers are the whole of what the ported page needed to reach it.

   WARNING: NOTHING HERE REJECTS. Every one of them resolves, with a count and
   the first error, because the callers are Design's SYNCHRONOUS `renderVals`
   closures: an unhandled rejection out of one is a console error a teacher
   never sees, in front of a composer that still looks like it sent. */

/* The signed-in teacher. `MrBadmusTeacherGuard` validates the JWT at boot and
   hands `ctx.user` to `teacher-live.js`, which keeps only `ctx.profile` -
   `first_name`, `role`, `school_id`, and no id. So the id is asked for again
   here, once, and held. RLS enforces `author_id = auth.uid()`, so a wrong one
   is refused by the database rather than written. */
function MRB_AUTHOR_ID(){
  if(MRB_AUTHOR_ID._id){return Promise.resolve(MRB_AUTHOR_ID._id);}
  var g=window.MrBadmusTeacherGuard;
  var sb=(g&&g.getClient)?g.getClient():null;
  if(!sb){return Promise.reject(new Error('teacher page: no data layer'));}
  return sb.auth.getUser().then(function(r){
    var u=r&&r.data&&r.data.user;
    if(!u||!u.id){throw new Error('teacher page: not signed in');}
    MRB_AUTHOR_ID._id=u.id;
    return u.id;});}

/* What went wrong, in a sentence a teacher can act on. The two named branches
   are the ones the hand-written composer already surfaced, kept word for word
   in meaning: an RLS refusal is about access, a CHECK refusal is about the
   message or the template. Anything else is "try again", because guessing
   further would be putting words in the database's mouth. */
function MRB_SHOUTOUT_WHY(e){
  var m=(e&&e.message)||'';
  if(/row-level security/i.test(m))
    return "Couldn't send — you may have lost access to this class.";
  if(/check constraint/i.test(m))
    return "Couldn't send — the message is too long, or the template is " +
           "not one this school uses.";
  if(/no data layer|not signed in/i.test(m))
    return "Couldn't send — this page is not signed in. Reload and try " +
           "again.";
  return "Couldn't send the shoutout. Try again.";}

/* `#compose-error` is the hand-written page's own validation line, carried
   into this page as a live region - inside `#mrb-teacher-live-regions`, which
   is `hidden`, and WITHOUT the stylesheet that used to lay it out. So it is
   written here for the region to hold and it is NOT the visible surface; the
   TOAST is, because the toast is the one notice surface Design drew. Stated
   rather than implied: if Design ever draws an inline error in the composer,
   this is the line to move onto it. */
function MRB_COMPOSE_ERROR(msg){
  var el=document.getElementById('compose-error');
  if(!el){return;}
  if(msg){el.hidden=false;el.textContent=msg;}
  else{el.hidden=true;el.textContent='';}}

/* Design's select and textarea are UNCONTROLLED, and `student-runtime` now
   carries field values ACROSS a redraw on purpose - it had to, because every
   keystroke schedules one. So clearing `s.note` clears the STATE and leaves
   the typed text on screen. The DOM is cleared first, then the state. */
function MRB_COMPOSE_RESET(){
  var els=document.querySelectorAll('[data-compose-field]'), i;
  for(i=0;i<els.length;i++){els[i].value='';}}

/* N inserts, one per recipient, and an honest count back. Resolves
   `{ok, fail, error}` - never rejects, and never reports a bare success. */
function MRB_SEND_SHOUTOUTS(classId, ids, templateKey, message){
  ids=ids||[];
  var no=function(e){return Promise.resolve({ok:0,fail:ids.length||1,error:e});};
  if(!classId){return no(new Error('teacher page: no class'));}
  if(!ids.length){return no(new Error('teacher page: no recipient'));}
  var TD=window.MrBadmusTeacherData;
  if(!TD||!TD.insertClassShoutout){
    return no(new Error('teacher page: no data layer'));}
  return MRB_AUTHOR_ID().then(function(authorId){
    return Promise.all(ids.map(function(rid){
      return TD.insertClassShoutout({classId:classId, authorId:authorId,
        recipientId:rid, templateKey:templateKey||null,
        message:message||null})
        .then(function(){return null;}, function(e){return e;});
    })).then(function(res){
      var errs=res.filter(function(e){return e;});
      return {ok:ids.length-errs.length, fail:errs.length,
              error:errs[0]||null};});
  }, no);}

/* == THE PER-STUDENT REMINDER, WIRED ====================================

   ⊕ MRB-306 Phase 2a screen 4, 2 Sep 2026.

   Design draws "Send a reminder" on the student page, gated on
   `student.flagged`, and her handler is `this.ping('Reminder sent to ' +
   st.name)` - a confirmation of a write that never happened. Exactly the
   shape the shoutout composer was in before it was wired, and it was pressed
   and photographed in this state before this helper existed.

   ⚠️ THIS DOES NOT RE-IMPLEMENT THE CLASS SCREEN'S CONTROL. `teacher-live.js`
   already owns the reminder machinery - `drawRemindControl`, and behind it
   `MrBadmusTeacherData.sendReminders` / `remindersForClass` - and this calls
   the SAME data layer with a one-element list. The class control chases
   everyone who has not handed this week's work in; this one chases the child
   whose page is open. Two surfaces, one write path, one rate limit.

   THE RATE LIMIT IS THE DATABASE'S, and it is a unique index on
   `(student_id, assignment_id, sent_on)` - one reminder per child per
   assignment per day, across ALL teachers of a co-taught class. This does
   not test it and must not: `sendReminders` upserts with `ignoreDuplicates`,
   so a second press writes NOTHING and comes back with an empty array. That
   is the honest signal, and it is reported as "already reminded today"
   rather than as a fresh send. Nothing here decides who may be reminded;
   RLS's `teacher_send` policy does.

   WHICH ASSIGNMENT: `kPapers[0]`, this week's work - the same paper
   `drawRemindControl` chases on, so the two controls cannot disagree about
   what a child is being reminded OF, and so both presses hit the same
   rate-limit key. A student with no papers is never flagged, so the button
   Design gates on `flagged` cannot be reached with no assignment to name.

   WARNING: IT NEVER REJECTS, like the six shoutout helpers above. Resolves
   `{ok, already, error}` and the caller says a sentence for each. */
function MRB_REMIND_STUDENT(classId, assignmentId, studentId){
  var no=function(e){return Promise.resolve({ok:0,already:false,error:e});};
  if(!classId){return no(new Error('teacher page: no class'));}
  if(!assignmentId){return no(new Error('teacher page: no assignment'));}
  if(!studentId){return no(new Error('teacher page: no student'));}
  var TD=window.MrBadmusTeacherData;
  if(!TD||!TD.sendReminders){
    return no(new Error('teacher page: no data layer'));}
  return TD.sendReminders({classId:classId, assignmentId:assignmentId,
      studentIds:[studentId], teacherId:MRB_ME()||null})
    .then(function(wrote){
      /* Report what was WRITTEN, not what was attempted - `drawRemindControl`
         takes the same care and for the same reason. An upsert that ignored
         a duplicate sent nothing, and saying otherwise overstates what the
         child actually got. */
      var n=(wrote&&wrote.length)||0;
      return {ok:n, already:n===0, error:null};},
      function(e){return {ok:0,already:false,error:e};});}

/* Why a reminder failed, in a sentence a teacher can act on. The companion
   to MRB_SHOUTOUT_WHY, and separate for the same reason: a different verb
   and a different set of refusals. */
function MRB_REMIND_WHY(e){
  var m=(e&&e.message)||'';
  if(/row-level security|permission|policy/i.test(m))
    return "Couldn't send - you may no longer teach this class.";
  if(/no data layer|not signed in/i.test(m))
    return "Couldn't send - this page is not signed in. Reload and try again.";
  if(/no assignment/i.test(m))
    return "Couldn't send - there is no work set to remind them about.";
  if(/failed to fetch|network/i.test(m))
    return "Couldn't send - no connection just now. Try again in a moment.";
  return "Couldn't send the reminder. Try again.";}

/* The feed a teacher has just written to, re-read. `teacher-live.js` does not
   memoise `FEED` - it is the one thing `base()` deliberately leaves out of
   the cache, for exactly this - so `load()` returns the new row and the rest
   of the page costs nothing. Resolves false where there is no live data
   source, which is every fixture. */
/* WARNING: ON A DEADLINE, AND IT ALWAYS SETTLES. The write has already
   happened by the time this runs, and the only thing waiting on it is the
   form being cleared. `teacher-live.load` has no timeout of its own — only
   its `run()` boot does — so a Supabase call that never answers would leave a
   composer full of text the teacher has already successfully sent. Eight
   seconds, then the form clears anyway with a stale feed, because a stale
   feed is a refresh away and a stuck form is not. */
function MRB_REFRESH_FEED(classId){
  var L=window.MrBadmusTeacherLive, D=window.__MRB_DATA__;
  if(!L||!L.load||!classId||!D){return Promise.resolve(false);}
  return Promise.race([
    L.load('class', {classId:classId}).then(function(d){
      D.FEED = d.FEED; return true;}, function(){return false;}),
    new Promise(function(r){setTimeout(function(){r(false);}, 8000);})
  ]);}

/* "N matches, showing 12". ⚠️ AND IT IS ONLY SAID WHEN IT IS TRUE.

   Design's search caps its results at twelve and said nothing about it — see
   teacher_rulings, the third silent cap this port has had to take a view on.
   The cap stays (a dropdown is refined by typing, not paged); what changes is
   that the number withheld is DECLARED.

   ⚠️ THE "SHOWING" CLAUSE APPEARS ONLY WHERE THE CAP ACTUALLY BIT. "Showing
   12 of 12" is noise on every ordinary search, and noise is how a teacher
   learns to stop reading the one line that will later matter.

   ⚠️ BLANKS OVER INVENTED NUMBERS, here as everywhere: a count this cannot
   be sure of renders NOTHING rather than a guess. An empty caption strip is
   a missing sentence; a wrong count is a false one.

   ⚠️ AND ZERO IS A STATE. Design's line would read "0 OF 60 STUDENTS" for a
   search that found nobody — a number beside a number, with no sentence. */
function MRB_SEARCH_FOOT(matched, shown, pool, q){
  if(matched==null||shown==null||pool==null){return '';}
  if(!pool){return 'No students in your classes yet';}
  if(!matched){return 'No students match';}
  var head = q ? (matched===1 ? '1 match' : matched + ' matches')
               : (matched + (matched===1 ? ' student' : ' students'));
  if(shown < matched){ head += ' · showing ' + shown; }
  if(matched > 1){ head += ' · type to narrow'; }
  return head;}

/* == THE SHOUTOUT DELETE ================================================

   ⊕ MRB-287, 24 Aug 2026. Mide's instruction: a teacher who can post a
   shoutout can remove one. Design drew no delete affordance, so the markup
   is an AMENDED ADDITION (teacher_rulings.AMENDED_ADDITIONS) and these three
   helpers are what stands behind it.

   WARNING: NOTHING HERE REJECTS EITHER, for the same reason the six above do
   not. */

/* WHO IS LOOKING, synchronously. The delete control is drawn per feed row
   inside Design's `renderVals`, which is not async, so the author check
   cannot wait on `sb.auth.getUser()` the way `MRB_AUTHOR_ID` does. The
   signed-in teacher's id therefore travels through the SEAM like every other
   fact on this page — `teacher-live.js` puts `ME` in the payload from the
   `ctx.user` the guard already validated, and a fixture supplies its own.
   ⚠️ It is NOT a permission. RLS decides; this only decides whether to offer
   a control that RLS would then allow. */
function MRB_ME(){return MRB_DATA('ME') || '';}

/* Why a removal failed, in a sentence a teacher can act on — the companion
   to MRB_SHOUTOUT_WHY and separate from it because the verb is different and
   because `no_rows_affected` has no equivalent on the write path.
   ⚠️ `no_rows_affected` IS THE SILENT ONE. `softDeleteClassShoutout` forces
   RETURNING with `.select('id')` precisely so an UPDATE that RLS matched
   nothing for cannot come back as `{data:null, error:null}` and be read as
   success. It is a real refusal and it gets a real sentence. */
function MRB_DELETE_WHY(e){
  var m=(e&&e.message)||'', c=(e&&e.code)||'';
  if(c==='no_rows_affected')
    return "Couldn't remove it — it may already be gone, or you may no " +
           "longer teach this class.";
  if(/row-level security/i.test(m))
    return "Couldn't remove it — only the teacher who wrote a shoutout can " +
           "remove it.";
  if(/no data layer|not signed in/i.test(m))
    return "Couldn't remove it — this page is not signed in. Reload and try " +
           "again.";
  return "Couldn't remove the shoutout. Try again.";}

/* The removal itself. `MrBadmusTeacherData.softDeleteClassShoutout` has
   existed since MRB-46 and is used rather than re-implemented: it sets
   `deleted_at`, forces RETURNING, and throws `no_rows_affected` where RLS
   refused silently.
   ⚠️ SOFT IN THE DATABASE, REAL TO EVERY READER. There is no DELETE policy on
   `class_shoutouts` — a hard delete is denied by default — and the read RPC
   `class_shoutouts_for_viewer` filters `deleted_at IS NULL`, so the row
   leaves the feed for everyone including its author. The control may
   therefore promise a removal, because that is what a teacher gets.
   Resolves `{ok, error}`; never rejects. */
function MRB_DELETE_SHOUTOUT(shoutoutId){
  var no=function(e){return Promise.resolve({ok:false,error:e});};
  if(!shoutoutId){return no(new Error('teacher page: no shoutout'));}
  var TD=window.MrBadmusTeacherData;
  if(!TD||!TD.softDeleteClassShoutout){
    return no(new Error('teacher page: no data layer'));}
  try{
    return TD.softDeleteClassShoutout(shoutoutId).then(
      function(){return {ok:true,error:null};}, no);
  }catch(e){return no(e);}}
"""


def _fixture_js(payload, empty=False):
    head = ("/* GENERATED by build_teacher_port.py — Claude Design's own\n"
            "   example data, COMPUTED BY RUNNING Design's own logic class\n"
            "   rather than retyped, and adapted to the shapes\n"
            "   shared/teacher-live.js hands the live page.\n"
            "   ⛔ Not a candidate for any live path: twelve invented\n"
            "   classes and fifty-four invented children, for every\n"
            "   visitor. */\n") if not empty else (
           "/* GENERATED by build_teacher_port.py — AN EMPTY SHAPE.\n"
           "   Constructed rather than found: empty states are the half of a\n"
           "   product that ships broken, because the person building it\n"
           "   always has data, and Design's delivery cannot express a single\n"
           "   one of them. ⛔ Not a candidate for any live path. */\n")
    return head + ("window.__MRB_DATA__ = %s;\n"
                   % json.dumps(payload, separators=(",", ":"),
                                ensure_ascii=False))


def page_html(spec, roots, table, logic, imports, fixture, versions, regions):
    """`fixture` is the fixture JS filename, or None for the live page."""
    # ⚠️ RELATIVE, AND NOT `/shared/`. The fixture data sits beside the
    # fixture page in `teacher_fixtures/` — out of every directory
    # generate_site_v5 publishes and round-trips. An absolute `/shared/` src
    # would put it back in a published one, which is the whole thing being
    # avoided; the gate serves the repo root, so same-directory resolves.
    tail = (
        "<script src=\"%s\"></script>\n"
        "<script>window.__MRB_MOUNT__();</script>\n" % fixture
    ) if fixture else (
        "<script src=\"%s\"></script>\n" % LIVE_JS_URL
    )

    # ⊕ MRB-303 J2 — the Admin entry, on FIVE of the six.
    #
    # ⚠️ A PLAIN <script> TAG, AND IT TOUCHES NEITHER `__MRB_TPL__` NOR
    # `teacher_rulings.py`. The script appends one link to
    # `[data-port-region="topbar"]` after the runtime has drawn, and re-appends
    # it after every redraw. Design's compiled tree is not edited, so this
    # carries none of the risk that editing a `parts` attribute would.
    #
    # ⛔ `class-detail.html` IS DELIBERATELY EXCLUDED — `admin_nav` is False on
    # its spec. MRB-303's brief is explicit that the class detail page is not
    # modified by this run: it is what Admin LINKS TO, and nothing more. A user
    # on that page reaches Admin via the brand mark or the browser's back
    # button, which is an accepted, named gap rather than an oversight.
    #
    # Emitted on the FIXTURE as well as the live page, on purpose: the gates
    # describe the fixture as "the same bytes apart from its banner and its
    # last two script tags", and that sentence is what lets them measure the
    # fixture and report on the production page. On a fixture there is no
    # config.js, no SDK and no session, so the script waits for a client that
    # never arrives and adds nothing — which is the correct outcome, not a
    # failure.
    admin_nav = ("<script src=\"/shared/%s\"></script>\n" % ADMIN_NAV_JS_NAME
                 if spec.get("admin_nav") else "")
    # ⚠️ EMITTED ON BOTH PAGES, including the fixture, which never reads it.
    # The gates document the fixture as "the same bytes apart from its banner
    # and its last two script tags", and that sentence is what lets them
    # measure the fixture and report on the production page. A tag on one and
    # not the other would make it false, for a JSON blob nobody can see.
    dep_map = ("<script>window.__MRB_ASSET_V__=%s;</script>\n"
               % json.dumps({k: v for k, v in sorted(versions.items())
                             if k in STAMPED_DEPS
                             or k == LIVE_JS_NAME}, separators=(",", ":")))
    return stamp_versions((
        # ⚑ THE <title> CARRIES NO CLASS AND NO CHILD'S NAME. The runtime
        # renders into `#mrb-teacher` and never touches `<head>`, so no
        # binding can reach a `<title>` — which on the student pages meant one
        # real class's name shipped in a file whose own banner said it held no
        # data. Here the static title says only what is true of every teacher,
        # and `teacher-live.js` is free to write a better one at mount.
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, "
        "initial-scale=1\">\n"
        "<title>%s</title>\n"
        "%s"
        "<link rel=\"stylesheet\" href=\"%s\">\n"
        "<style>body{margin:0;background:var(--st-ground,#FBF3E6)}"
        "a{color:var(--ks3-accent-text);text-decoration:none}"
        "a:hover{color:var(--ks3-accent-hover)}"
        "button{font-family:inherit}"
        "#mrb-teacher-live-regions[hidden]{display:none}"
        "@media print{.noprint{display:none!important}}"
        "</style>\n"
        "</head>\n<body>\n"
        "<div id=\"mrb-teacher\" style=\"background:var(--st-ground);"
        "min-height:100vh\"></div>\n"
        "%s"
        "<script src=\"/shared/student-runtime.js\"></script>\n"
        "<script>window.__MRB_TPL__=%s;</script>\n"
        "<script>window.__MRB_BIND__=%s;</script>\n"
        "<script>\n%s\n</script>\n"
        "<script>\n%s\n</script>\n"
        "%s"
        "%s"
        "</body>\n</html>\n"
        % (html.escape(spec["title"]),
           (_BANNER_FIXTURE % (spec["out"][:-5].replace("-", " ").title(),
                               spec["out"])) if fixture else
           (_BANNER % (spec["out"][:-5].replace("-", " ").title(),
                       LIVE_JS_NAME, spec["fixture_out"])),
           DS_CSS_URL,
           regions,
           json.dumps({"roots": roots, "imports": imports},
                      separators=(",", ":")).replace("<", "\\u003c"),
           json.dumps(table, separators=(",", ":")),
           # Design's logic class, with DCLogic bound to our base and with
           # Design's sample lifted out to MRB_DATA / MRB_PICK. Everything
           # else about it is still verbatim.
           _SEAM
           + "var DCLogic = window.MrBadmusStudentRuntime.MrbLogic;\n"
           + "var StreamableLogic = DCLogic;\n" + logic,
           # ⚠️ DECLARED, NOT CALLED. Whoever loads the data calls it, which
           # is what makes "the production page cannot mount without a data
           # source" a property of the file rather than a promise about it.
           "window.__MRB_MOUNT__ = function () {\n"
           "  var R = window.MrBadmusStudentRuntime;\n"
           "  var tpl = window.__MRB_TPL__;\n"
           "  return R.mount({\n"
           "    into: '#mrb-teacher',\n"
           "    template: {roots: R.applyBindings(tpl.roots, "
           "window.__MRB_BIND__, MRB_DATA), imports: tpl.imports},\n"
           "    imports: tpl.imports,\n"
           "    Component: Component,\n"
           "    props: {}\n"
           "  });\n"
           "};",
           dep_map + admin_nav,
           tail)),
        versions)


def write(path, body):
    _refuse(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)


def _verify_stamps(stamped):
    """Re-read from disk and refuse to finish if any stamp names other bytes.

    ⚑ THE ORDERING IS THE WHOLE UNIT, so it is asserted rather than commented.
    A `?v=` naming content that is NOT the content being served is worse than
    no `?v=` at all: the page looks fixed, the browser caches the wrong bytes
    under a URL that will never change again, and every gate stays green. The
    only way to know a stamp is honest is to hash the file that will actually
    be deployed, AFTER everything that writes it has run.
    """
    # ⚠️ THE INVARIANT IS PER TREE: every asset a page names must exist
    # WHERE THAT PAGE IS SERVED FROM. The fixture data is deliberately not
    # published (see the note on unpublishing, above) — it lives in `shared/`
    # and is read by `teacher_behaviour.py`, which serves the repo root. So a
    # fixture asset absent from `mrbadmus_site/shared/` is the intended state,
    # not a broken stamp, and checking it there reported twelve failures for
    # twelve files that are correctly missing.
    #
    # The check is NOT weakened: each fixture asset is still hashed and still
    # compared, in the one tree its page is served from. A fixture asset that
    # went missing from `shared/` would still stop the build.
    # ⊕ 2 Sep 2026 — EVERY empty variant's data file, not just `empty_js`.
    # Derived from EMPTY_SHAPES through `variant_files`, the same call the
    # build writes them with, so a new variant cannot be added without this
    # set knowing about it.
    fixture_assets = set()
    for spec in PAGES:
        fixture_assets.add(spec["fixture_js"])
        for slug, _note, _shaper in EMPTY_SHAPES[spec["out"]]:
            fixture_assets.add(variant_files(spec, slug)[1])

    bad = []
    for name, want in sorted(stamped.items()):
        trees = (FIXTURE_OUT,) if name in fixture_assets else (SHARED_OUT, "shared")
        for tree in trees:
            path = os.path.join(tree, name)
            if not os.path.exists(path):
                if tree == SHARED_OUT and name in STAMPED_DEPS:
                    print("        ⚠️  %s/%s is missing — generate_site_v5.py "
                          "has not run here, so the stamp could not be "
                          "checked against the deployed copy" % (tree, name))
                    continue
                bad.append("%s/%s does not exist, but a page stamps it ?v=%s"
                           % (tree, name, want))
                continue
            with open(path, "rb") as fh:
                got = asset_hash(fh.read())
            if got != want:
                bad.append(
                    "%s hashes %s but the pages shipped ?v=%s — the stamp "
                    "names content that is not what will be served. Run "
                    "`python3 build_all.py`, which publishes shared/ before "
                    "this build stamps it." % (path, got, want))

    # ⚠️ AN OPTIONAL GROUP, NOT A NEGATIVE LOOKAHEAD. `/shared/[\w.-]+(?!\?v=)`
    # is satisfied by BACKTRACKING one character and reports a perfectly
    # stamped page as unstamped — build_student_port.py records that it did
    # exactly that, twelve times. Matching the stamp optionally and testing
    # whether it was captured has no such ambiguity.
    linked = re.compile(r"/shared/[A-Za-z0-9._/-]+(\?v=[0-9a-f]+)?")
    for tree in (SITE_OUT, MIRROR_OUT):
        for spec in PAGES:
            for key in ("out", "fixture_out"):
                path = os.path.join(tree, spec[key])
                if not os.path.exists(path):
                    continue
                page = open(path, encoding="utf-8").read()
                for m in linked.finditer(page):
                    if m.group(1) or m.group(0).startswith("/shared/fonts/"):
                        continue
                    bad.append(
                        "%s links %s with no cache-bust stamp, at offset %d. "
                        "Every asset a teacher page names must be in the "
                        "version map — see STAMPED_DEPS and build()."
                        % (path, m.group(0), m.start()))
    if bad:
        raise SystemExit(
            "build_teacher_port.py: the cache-bust stamps are not honest.\n  "
            + "\n  ".join(bad))
    print("     ✅ cache-bust: %d asset(s) stamped from their own content, "
          "each re-hashed from disk" % len(stamped))


def retire_originals():
    """Move the four hand-written teacher pages out of `teacher/`.

    ⛔ OUT OF `teacher/`, so the KS4 generator does not publish them, and into
    `docs/ks3/retired/` with today's date, so git holds them regardless. This
    is the same move the student port made on 22 Aug 2026 and for the same
    reason: a hand-written source file sitting beside its generated
    replacement is a file somebody will edit.

    Returns {out name: the original's HTML}, read BEFORE the move so the live
    regions can be lifted out of it either way.
    """
    os.makedirs(RETIRED, exist_ok=True)
    sources = {}
    for spec in PAGES:
        if not spec.get("retire"):
            continue
        live = os.path.join(MIRROR_OUT, spec["retire"])
        dest = os.path.join(RETIRED, "teacher-%s-2026-08-24-retired.html"
                            % spec["retire"][:-5])
        if os.path.exists(dest):
            sources[spec["out"]] = open(dest, encoding="utf-8").read()
            continue
        if not os.path.exists(live):
            raise SystemExit(
                "build_teacher_port.py: %s is neither in teacher/ nor "
                "retired at %s. Its live regions cannot be lifted, and "
                "lifting nothing would silently delete every error state on "
                "this page." % (spec["retire"], dest))
        text = open(live, encoding="utf-8").read()
        if "GENERATED — do not edit" in text[:4000]:
            raise SystemExit(
                "build_teacher_port.py: %s is already this build's own "
                "output, and there is no retired copy at %s to lift the live "
                "regions from. Restore the hand-written original from git "
                "before rebuilding." % (live, dest))
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.remove(live)
        sources[spec["out"]] = text
        print("     ⊕ retired  %-22s → %s" % (spec["retire"], dest))
    return sources


def build():
    if not os.path.exists(TEMPLATES):
        raise SystemExit(
            "build_teacher_port.py: %s is missing. Run `python3 "
            "student_template.py` — the template and the logic are compiled "
            "out of Design's delivery, never typed." % TEMPLATES)
    tpls = json.load(open(TEMPLATES, encoding="utf-8"))
    tpl = tpls.get(TPL_KEY)
    if not tpl:
        raise SystemExit("build_teacher_port.py: %s has no %r entry."
                         % (TEMPLATES, TPL_KEY))

    import teacher_rulings as R

    print("\n🧑‍🏫  build_teacher_port — Design's teacher dashboard, "
          "six pages\n")

    # ── the six templates, read out of the live enum for the fixture ─────
    #
    # ⚠️ READ, NOT RETYPED. `SHOUTOUT_TEMPLATES` in shared/shoutouts.js mirrors
    # the DB CHECK constraint `class_shoutouts_template_key_chk`, and a
    # fixture carrying a seventh key or a stale one would gate green against a
    # composer that fails on insert. Design's own six labels are word-for-word
    # the live ones; only the ids differ, and the id is what gets stored.
    templates = shoutout_templates()

    css, sizes = ds_css()
    wanted = referenced_tokens(tpl)
    css, topped = top_up(css, wanted, tpl)
    print("     %d token(s) referenced by the six pages; %d not in "
          "Design's bundle and topped up from shared/tokens.css%s"
          % (len(wanted), len(topped),
             (": " + ", ".join(topped)) if topped else ""))

    for out_dir in (SHARED_OUT, "shared"):
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, DS_CSS_NAME), "w",
                  encoding="utf-8") as fh:
            fh.write(css)
    print("     ✅ %-26s %7d bytes, %d sheet(s), linked and cached once"
          % (DS_CSS_NAME, len(css), len(sizes)))

    # ⚑ EVERY ASSET IS PUBLISHED BEFORE THE PAGE THAT NAMES IT IS WRITTEN,
    # and the version map is built from CONTENT. Both halves matter — see
    # `_verify_stamps`, which re-reads all of it from disk and refuses to
    # finish if any hash disagrees with the stamp that shipped.
    versions = {DS_CSS_NAME: asset_hash(css)}

    src = os.path.join("shared", RUNTIME_JS_NAME)
    if not os.path.exists(src):
        raise SystemExit(
            "build_teacher_port.py: shared/%s does not exist, and all six "
            "pages load it. Without it they mount nothing at all — which is "
            "the correct failure and still a failure." % RUNTIME_JS_NAME)
    runtime = open(src, encoding="utf-8").read()
    with open(os.path.join(SHARED_OUT, RUNTIME_JS_NAME), "w",
              encoding="utf-8") as fh:
        fh.write(runtime)
    versions[RUNTIME_JS_NAME] = asset_hash(runtime)

    # ⚠️ `teacher-live.js` IS ANOTHER UNIT'S FILE AND MAY NOT EXIST YET. The
    # pages link it either way, and they must: a page that only links its data
    # source once the data source exists is a page whose contract changes
    # under it. Missing, the stamp is skipped and the build says so once,
    # loudly, rather than emitting a `?v=` for bytes that are not there.
    live_src = os.path.join("shared", LIVE_JS_NAME)
    if os.path.exists(live_src):
        live_js = open(live_src, encoding="utf-8").read()
        with open(os.path.join(SHARED_OUT, LIVE_JS_NAME), "w",
                  encoding="utf-8") as fh:
            fh.write(live_js)
        versions[LIVE_JS_NAME] = asset_hash(live_js)
    else:
        print("     ⚠️  shared/%s DOES NOT EXIST. Every page links it and "
              "none of them can mount without it — the live pages will render "
              "nothing at all until it lands. Emitted UNSTAMPED, so it is on "
              "the four-hour cache skew until the next build after it "
              "arrives." % LIVE_JS_NAME)

    for name in STAMPED_DEPS:
        dep = os.path.join("shared", name)
        if not os.path.exists(dep):
            raise SystemExit(
                "build_teacher_port.py: shared/%s does not exist, and "
                "teacher-live.js loads it on every teacher page. A missing "
                "dependency is a blank dashboard." % name)
        with open(dep, "rb") as fh:
            versions[name] = asset_hash(fh.read())

    # ── Design's logic, seamed once ──────────────────────────────────────
    logic, counts = seam_logic(tpl["logic"])
    print("     ⊕ logic: %d ruled edit(s), %d navigation rewire(s), "
          "%d method(s) reseamed, %d invented field(s) deleted, "
          "%d Set-work key(s) removed"
          % (counts["logic"], counts["nav"], counts["methods"],
             counts["fields"], counts["keys"]))
    print("     ✅ no `rnd(` survives; `this.seed(` has exactly one caller "
          "(hueFor), which is derivation and not invention")

    originals = retire_originals()

    # ── Design's sample, computed by running Design's own logic ──────────
    scratch = os.path.join(REPO, ".teacher-port-tmp")
    os.makedirs(scratch, exist_ok=True)
    fixture_class = "8rsc1"
    data = design_data(tpl["logic"], fixture_class, scratch)
    try:
        os.rmdir(scratch)
    except OSError:
        pass
    payload = fixture_payload(data, templates, fixture_class)
    print("     ⊕ Design's sample EVALUATED (not retyped) and adapted to the "
          "seam's shapes: %d class(es), %d matrix/roster/paper map(s), "
          "%d grid(s), %d template(s) read from shoutouts.js"
          % (len(data["CLASSES"]), len(data["MATRIX"]), len(data["GRID"]),
             len(templates)))

    stamped = dict(versions)
    nav_nodes_seen = set()
    retarget_seen = set()
    # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — the same accumulator, for the four
    # node-anchored tables that never had one. See `KNOWN_UNAPPLIED`.
    ruling_seen = {"SET_ATTR": set(), "BIND_ATTR": set(),
                   "RETEXT_AT": set(), "SET_ON": set()}
    region_report = {}
    empty_report = {}

    for spec in PAGES:
        roots, stats = apply_rulings(spec, tpl["roots"], logic)
        table, bind_values = bindings_for(spec, roots)
        shipped = scrub(roots, table)

        page_logic = logic.replace("'MRB_SCREEN'", "'%s'" % spec["screen"], 1)
        if "MRB_SCREEN" in page_logic:
            raise SystemExit(
                "build_teacher_port.py: the screen token is still in the "
                "logic for %s. Every page must name its own screen exactly "
                "once — a page whose `screen` does not match the one node it "
                "kept renders a blank body." % spec["out"])

        regions, region_ids = live_regions(spec, originals.get(spec["out"], ""))
        region_report[spec["out"]] = region_ids

        # ⚑ THE FIXTURE DATA IS WRITTEN BEFORE THE PAGE THAT LINKS IT. The
        # page carries `teacher-fixture-<page>.js?v=<hash>`, and the only
        # honest hash is of the bytes this build is about to write; computed
        # after, it would name the previous run's example data.
        mine = dict(payload)
        mine["screen"] = spec["screen"]
        # ⚠️ `paperIdx` IS NULL EVERYWHERE BUT THE MARKING SCREEN, and that is
        # not tidiness. `paper()` throws on a paper index the class does not
        # have, and a class-detail fixture carrying `paperIdx: 1` would be
        # asserting a fact about a screen it does not draw.
        if spec["screen"] != "marking":
            mine["paperIdx"] = None
        if spec["screen"] not in ("class", "student"):
            mine["FEED"] = {}
        js = _fixture_js(mine)

        # ⊕ 2 Sep 2026 — ONE OR MORE empty variants per screen. `empty` is
        # first and keeps the spec's own filenames; see EMPTY_SHAPES.
        variants = []
        for slug, note, shaper in EMPTY_SHAPES[spec["out"]]:
            v_out, v_js_name = variant_files(spec, slug)
            variants.append((slug, v_out, v_js_name,
                             _fixture_js(shaper(dict(mine)), empty=True)))
            empty_report[v_out] = note

        # The fixture DATA follows the fixture PAGES out of the published
        # tree. Unpublishing the HTML alone would have left twelve JS files
        # on mrbadmus.com still carrying the fifty-four invented children and
        # every mark — not renderable as a dashboard, but fetchable, and the
        # thing that actually holds the content.
        # Beside the pages that read them, in the unpublished directory.
        # Earlier versions wrote these to `shared/`, which is published AND
        # round-tripped — so the invented data reached the public site and
        # the correction then risked deleting it from source.
        os.makedirs(FIXTURE_OUT, exist_ok=True)
        for stale in ([spec["fixture_js"]] + [v[2] for v in variants]):
            for tree in (SHARED_OUT, "shared"):
                gone = os.path.join(tree, stale)
                if os.path.exists(gone):
                    os.remove(gone)
        with open(os.path.join(FIXTURE_OUT, spec["fixture_js"]), "w",
                  encoding="utf-8") as fh:
            fh.write(js)
        for _slug, _v_out, v_js_name, v_js in variants:
            with open(os.path.join(FIXTURE_OUT, v_js_name), "w",
                      encoding="utf-8") as fh:
                fh.write(v_js)
        page_versions = dict(versions)
        page_versions[spec["fixture_js"]] = asset_hash(js)
        for _slug, _v_out, v_js_name, v_js in variants:
            page_versions[v_js_name] = asset_hash(v_js)
        stamped.update(page_versions)

        body = page_html(spec, shipped, table, page_logic, tpl["imports"],
                         None, page_versions, regions)
        fix = page_html(spec, shipped, table, page_logic, tpl["imports"],
                        spec["fixture_js"], page_versions, regions)
        empties = [(v_out, page_html(spec, shipped, table, page_logic,
                                     tpl["imports"], v_js_name,
                                     page_versions, regions))
                   for _slug, v_out, v_js_name, _v_js in variants]
        # ⚠️ THE LIVE PAGE IS PUBLISHED; THE FIXTURES ARE NOT.
        #
        # `mrbadmus_site/` is what Cloudflare serves, and `/teacher/*` has no
        # edge auth — the guard runs in the page, after the bytes have already
        # been handed over. Publishing the fixtures therefore put twelve URLs
        # on mrbadmus.com, each rendering Design's invented school: twelve
        # classes, fifty-four children's names and a mark for every one of
        # them, with no sign-in and no `noindex`.
        #
        # None of those children exist, so this is not a safeguarding matter.
        # It is worse-looking than it is: a page at
        # `mrbadmus.com/teacher/classes-fixture.html` showing "Amara Okonkwo
        # 61%" is indistinguishable, to a parent or a school, from real pupil
        # data leaking. `teacher_tells.py` exists to keep exactly that content
        # off a live page and would have been satisfied one directory away.
        #
        # The fixtures are only ever DRIVEN, by `teacher_behaviour.py`, which
        # serves the repo root and reads `teacher/<page>` — the mirror, not
        # the published tree. So nothing needs them in `mrbadmus_site/` and
        # they are written to the mirror alone.
        #
        # ⊕ The two STUDENT fixtures are still published, because
        # `student_themes` is registered against
        # `mrbadmus_site/student/class-fixture.html` and drives that copy.
        # Same exposure, smaller, pre-existing, and not this ticket's to
        # change — recorded in the MRB-287 report rather than fixed here.
        # A fixture written by an EARLIER build is still served until
        # something removes it. Unpublishing has to delete, not just stop
        # writing — otherwise the change is invisible until the next full
        # `generate_site_v5` wipe, and reads as done when it is not.
        for stale in ([spec["fixture_out"]] + [v[0] for v in variants]):
            gone = os.path.join(SITE_OUT, stale)
            if os.path.exists(gone):
                os.remove(gone)
        write(os.path.join(SITE_OUT, spec["out"]), body)
        write(os.path.join(MIRROR_OUT, spec["out"]), body)
        write(os.path.join(FIXTURE_OUT, spec["fixture_out"]), fix)
        for v_out, v_body in empties:
            write(os.path.join(FIXTURE_OUT, v_out), v_body)

        # ── ⊕ MRB-287 · the additions, asserted against the BYTES ──────
        #
        # ⚑ "I INSERTED IT" AND "IT IS IN THE PAGE" ARE DIFFERENT CLAIMS.
        # An INSERT_AT entry whose parent node is not on this page is skipped
        # SILENTLY — that is deliberate, because two of the four insertions
        # belong to other screens — so the register in teacher_rulings could
        # name a control that is nowhere in the emitted file and nothing
        # would say so. This reads the finished HTML.
        #
        # Both directions: on its own page every marker must be PRESENT, and
        # on every other page it must be ABSENT. The second half is what
        # catches an addition that has drifted onto a screen it was never
        # ruled onto — an inert confirm sheet on five pages that cannot open
        # it, which is the orphaned hidden element MRB-287 has just removed
        # one of.
        # ⚠️ THE JSON FORM, NOT THE HTML FORM. These pages ship Design's
        # template as `window.__MRB_TPL__` and the runtime draws it in the
        # browser, so there is no `data-mrb-added="…"` in the file — there is
        # `"data-mrb-added":"…"` inside the serialised roots. Looking for the
        # HTML spelling finds nothing on a page that carries the control
        # perfectly well, which is what the first version of this check did.
        # ⊕ MRB-304 — `pages` is a tuple, always. The "My classes" link is on
        # all six; every other addition names exactly one. Both halves of the
        # check are unchanged by that: present on every page it names, absent
        # on every page it does not.
        for add in R.AMENDED_ADDITIONS:
            tag = '"data-mrb-added":"%s"' % add["marker"]
            if spec["out"] in add["pages"]:
                if tag not in body:
                    raise SystemExit(
                        "build_teacher_port.py: %s — teacher_rulings."
                        "AMENDED_ADDITIONS names %r (%s), inserted at "
                        "Design's node %s, and it is NOT in the emitted "
                        "page.\n  The insertion was skipped or the node was "
                        "pruned. A registered addition that is not on the "
                        "page is a control nobody can press and a register "
                        "nobody can trust. (%s)"
                        % (spec["out"], add["label"], add["marker"],
                           add["node"], add["why"].split(".")[0]))
            elif tag in body:
                raise SystemExit(
                    "build_teacher_port.py: %s — the addition %r is ruled "
                    "onto %s and it is in THIS page too. An addition on a "
                    "screen it was not ruled onto is markup a teacher can "
                    "reach by accident, or cannot reach at all."
                    % (spec["out"], add["marker"],
                       ", ".join(add["pages"])))

        # ── ⊕ MRB-287 E1 · EVERY CLASS STATES ITS OWN ACADEMIC YEAR ──────
        #
        # ⛔ THE DEFECT THIS CATCHES CANNOT BE CAUGHT BY DRIVING THE PAGE, and
        # that is why it is a byte check. The grid is year-scoped, so every
        # card in one payload legitimately carries the SAME year string — a
        # drive watching those strings cannot tell "each card states its own
        # year" from "every card states the dashboard's year", because on
        # correct data the two render identically. It only diverges on a past
        # year, which no fixture can hold alongside a current one without
        # inventing a shape the database cannot be in.
        #
        # What CAN be checked exactly is which value the expression reads. The
        # card meta and the class header must read the CLASS's year
        # (`c.yearName` / `k.yearName`) and must not reach for the dashboard's
        # (`MRB_DATA('yearLabel')`), which is what both did until E1 and what
        # made twelve cards out of 2025-26 each say 2026-27.
        # ⊕ 2 Sep 2026 (MRB-306 Phase 1c) — BOTH ANCHORS RE-CUT, and the
        # second one was WATCHING A KEY THAT NO LONGER EXISTS. Design's v3
        # deleted `longMeta` and rebuilt the class header as `klass.meta`;
        # the ruling was re-expressed onto `klass.meta` on 1 Sep and this
        # guard was not, so it searched for a string absent from every page
        # and refused all six builds. The FIRST anchor was worse: a bare
        # `find("meta:")` takes whichever `meta:` comes first in the file,
        # and v3 put the Today screen's lesson meta ahead of the card's — so
        # for one afternoon it was checking `t.room` for an academic year.
        #
        # Each row now names the DECLARATION it belongs under and searches
        # forward from there, so neither can drift onto a neighbour's key.
        for what, own, decl, line in (
                ("the class card's meta line", "c.yearName",
                 "const cards = ", "meta:"),
                ("the class header's meta line", "k.yearName",
                 "      klass: {", "meta:")):
            seg = ""
            base = page_logic.find(decl)
            if base == -1:
                raise SystemExit(
                    "build_teacher_port.py: %s — %s cannot be checked: "
                    "`%s` is not in the emitted logic.\n"
                    "  Design has renamed or removed the declaration this "
                    "guard reads. An E1 check that cannot find its own "
                    "anchor must refuse; skipping it would let the working "
                    "year back onto a past year's class."
                    % (spec["out"], what, decl.strip()))
            at = page_logic.find(line, base)
            if at != -1:
                seg = page_logic[at:at + 260]
            if own not in seg:
                raise SystemExit(
                    "build_teacher_port.py: %s — %s does not read %r.\n"
                    "  Every class must state ITS OWN academic year, not the "
                    "one the dashboard is scoped to. The retired page put it "
                    "on every card and recorded why: 10H/Ph1 and 11h/Ph1 are "
                    "the same 17 students a year apart and must never read "
                    "as a duplicate. Re-anchor teacher_rulings.LOGIC."
                    % (spec["out"], what, own))
            if "MRB_DATA('yearLabel')" in seg:
                raise SystemExit(
                    "build_teacher_port.py: %s — %s reads "
                    "MRB_DATA('yearLabel'), which is the WORKING year and "
                    "not this class's.\n"
                    "  Correct while the working year is the only one a "
                    "teacher can open, and wrong the moment a past year is. "
                    "That is the E1 defect exactly; it is a byte check "
                    "because no drive can see it (the grid is year-scoped, "
                    "so both readings render the same string on correct "
                    "data)." % (spec["out"], what))

        # ⚑ ASSERTED, NOT ASSUMED. No bound literal may survive in the
        # template the PRODUCTION page ships — otherwise the binding is
        # cosmetic, the page carries the sample anyway, and a failed data load
        # renders Design's invented values instead of nothing.
        blob = json.dumps(shipped, ensure_ascii=False)
        for key, val in sorted(bind_values.items()):
            if val.strip() and json.dumps(val, ensure_ascii=False) in blob:
                raise SystemExit(
                    "build_teacher_port.py: %s — the literal %r is STILL a "
                    "text node in the shipped template after the scrub, so "
                    "the binding for %r is cosmetic and the production page "
                    "carries Design's sample anyway."
                    % (spec["out"], val, key))

        here, _ = index_tree(roots)
        for handler, nav in R.NAV.items():
            nav_nodes_seen |= {n for n in nav["nodes"] if n in here}
        retarget_seen |= {n for n in R.RETARGET_ON if n in here}
        for _t, _tbl in (("SET_ATTR", R.SET_ATTR), ("BIND_ATTR", R.BIND_ATTR),
                         ("RETEXT_AT", R.RETEXT_AT), ("SET_ON", R.SET_ON)):
            ruling_seen[_t] |= {n for n in _tbl if n in here}

        print("     ✅ %-24s %7d bytes  (%d node(s) pruned, %d inserted, "
              "%d wrapped, %d retargeted, %d binding(s), %d retext(s), "
              "%d region(s) named, %d live region(s) carried)"
              % (spec["out"], len(body), stats["pruned"], stats["inserted"],
                 stats["wrapped"], stats["retargeted"], len(table),
                 stats["retexted"], stats["attred"], len(region_ids)))
        print("        %-30s %7d" % (spec["fixture_out"], len(fix)))
        for v_out, v_body in empties:
            print("        %-30s %7d" % (v_out, len(v_body)))

    # ⚠️ EVERY NAVIGATION NODE MUST HAVE BEEN CHECKED ON AT LEAST ONE PAGE.
    # `apply_rulings` skips a node pruned with its screen, which is correct
    # per page and would let a node Design DELETED go unchecked on all six.
    # This is the sweep that closes that hole.
    all_nav = {n for nav in R.NAV.values() for n in nav["nodes"]}
    missed = sorted(all_nav - nav_nodes_seen)
    if missed:
        raise SystemExit(
            "build_teacher_port.py: navigation node(s) %s were never present "
            "on ANY of the six pages, so the ruling anchored on them was "
            "never checked. Design has removed those controls; re-anchor "
            "teacher_rulings.NAV." % missed)

    # ⊕ MRB-304 — and the same sweep for the retargets, for the same reason.
    # `apply_rulings` skips a node that is not on the page it is building, so
    # a node Design DELETED would be skipped on all six and the ruling never
    # checked anywhere. The brand mark is in the top bar on every page, so
    # this is only ever red if the top bar itself has been redrawn.
    missed = sorted(set(R.RETARGET_ON) - retarget_seen)
    if missed:
        raise SystemExit(
            "build_teacher_port.py: retarget node(s) %s were never present "
            "on ANY of the six pages, so the ruling anchored on them was "
            "never checked. Design has removed those controls; re-anchor "
            "teacher_rulings.RETARGET_ON." % missed)

    # ── ⊕ 2 Sep 2026 (MRB-306 Phase 1c) · THE UNGUARDED-RULING SWEEP ────
    #
    # ⛔ FOUR TABLES HAD NO SWEEP AT ALL. `apply_rulings` skips a node that is
    # not on the page it is building — right per page, and it meant a node
    # Design had DELETED was skipped on all six and its ruling checked
    # nowhere. `NAV` and `RETARGET_ON` were already swept; `SET_ATTR`,
    # `BIND_ATTR`, `RETEXT_AT` and `SET_ON` were not, and that is the same
    # silent failure as the hand-edit this file replaced: green build, ruling
    # not in the page.
    #
    # ⚠️ BOTH DIRECTIONS. A node in `KNOWN_UNAPPLIED` that DOES appear on a
    # page fails too — an exemption list that can only ever excuse is a switch
    # for turning the guard off.
    for table, seen in sorted(ruling_seen.items()):
        named = R.KNOWN_UNAPPLIED.get(table, {})
        all_nodes = set(getattr(R, table))
        missed = sorted((all_nodes - seen) - set(named))
        if missed:
            raise SystemExit(
                "build_teacher_port.py: teacher_rulings.%s names node(s) %s "
                "and NONE of the six pages carries them, so those rulings "
                "were never applied and never checked.\n"
                "  Design has redrawn or deleted those nodes. Re-anchor "
                "them, or — if they belong to a screen this port "
                "deliberately does not emit — name them in "
                "teacher_rulings.KNOWN_UNAPPLIED with the reason. A ruling "
                "that silently applied to nothing is the hand-edit failure "
                "this file exists to prevent." % (table, missed))
        rotted = sorted(set(named) & seen)
        if rotted:
            raise SystemExit(
                "build_teacher_port.py: teacher_rulings.KNOWN_UNAPPLIED[%r] "
                "excuses node(s) %s as unreachable, and they ARE on an "
                "emitted page.\n"
                "  The exemption is stale. Remove those rows: an exemption "
                "list that is never checked back is a way of switching a "
                "guard off." % (table, rotted))
    print("     ✅ unguarded-ruling sweep: %d node-anchored ruling(s) across "
          "6 table(s) proved applied on at least one page; %d named "
          "unapplied and why"
          % (len(nav_nodes_seen) + len(retarget_seen)
             + sum(len(v) for v in ruling_seen.values()),
             sum(len(v) for v in R.KNOWN_UNAPPLIED.values())))

    _verify_stamps(stamped)

    print("\n     → %s/  and  %s/  (mirror)" % (SITE_OUT, MIRROR_OUT))
    print("     ⚠️  the six pages carry NO data and do not mount "
          "themselves; %s does that." % LIVE_JS_NAME)
    print("     ⚠️  *-fixture.html and *-empty-fixture.html carry INVENTED "
          "data and are what the gates drive.\n         Neither is a "
          "candidate for a live path.\n")
    for out, ids in sorted(region_report.items()):
        if ids:
            print("     live regions on %-24s %s"
                  % (out, ", ".join("#" + i for i in ids)))
    print()
    for out, note in sorted(empty_report.items()):
        print("     %-30s %s" % (out, note.split(".")[0]))
    print()


if __name__ == "__main__":
    sys.path.insert(0, REPO)
    build()
