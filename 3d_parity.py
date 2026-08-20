#!/usr/bin/env python3
"""3d_parity.py — the MRB-186 visual parity gate for the 3D Studio shell.

Design's reference is frozen in two files: ``3d-studio/reference/shell-v1.html``
(§01–§07, MRB-186) and ``3d-studio/reference/crosssection-v1.html`` (§08–§10,
the cut face and its slider, MRB-189). The second redraws the first's seven
screens byte-identically before adding its own three, so shell-v1 remains the
reference for §01–§07 and layer A asserts that agreement rather than assuming
it. Stage 1
shipped five logical gates and none of them looks at pixels — and on KS3 the
parity gate (``ks3_parity.py``) caught three real defects that human review
missed. This module is the same idea pointed at the studio, and it follows
that module's approach deliberately: the same layers, the same colour maths
(imported from it, not re-implemented), the same browser harness
(``ks3_browser.py`` — stdlib CDP driving the installed Chrome).

═══════════════════════════════════════════════════════════════════════════
WHAT THIS GATE DOES, AND WHAT IT CANNOT DO — read before trusting it
═══════════════════════════════════════════════════════════════════════════

The reference is a single canvas page: every screen mocked inline at 1440px
with hardcoded lorem content, zero CSS classes. The app is a React build with
content-driven markup. A byte or DOM diff is impossible, so parity is
asserted in three layers (the fourth KS3 layer, contrast, lives in
``3d-studio/tests/gates/contrast.test.ts``, which recomputes WCAG ratios from
the token file on every vitest run — it is not duplicated here):

  A. PROVENANCE (no browser).  Every colour ``src/styles/tokens.css``
     declares must appear literally in the frozen references, read as one
     text — you cannot invent a colour Design never specified, or drift a
     hex by one digit, without the build failing. It also holds the two
     files to their overlap: §01–§07 must stay the same bytes in both, or
     the line numbers every row below cites have stopped meaning anything.
     The seven MRB-186 reconciled values are the
     documented exception: for those the gate asserts the OLD value is in
     the reference (the divergence is FROM something real) and that the old
     value appears nowhere in ``src/`` or ``.design-sync/`` — the sweep
     stays swept. A second, smaller exception is ADOPTED: a canonical token
     the reference has no counterpart for, where there is no old value to
     assert or sweep, only the shipped value to pin (entry 16).

  B. STRUCTURE (browser).  For each screen Stage 1 implements, the regions
     the reference draws exist, in the reference's containment and state:
     library / stage / panel composition, the retrieval room's inversions
     (library removed, hatch strip, one target + inert dots), the tablet
     drawer, the phone sheet detents, the flat stage's reduced rail. It also
     holds the two invariants that let a SPECIMEN GROW without deforming the
     shell: on desktop the page stays one viewport tall however many hotspots
     the record carries, and every rendered caption is whole and unbroken.
     Both of those were defects before they were rows — heart.json went from
     2 hotspots to 14, the page became 1942px inside a 900px viewport, and
     the library caption started reading VIEWING · 14 STRUCTU…

  C. COMPUTED STYLE (browser).  A real Chrome loads the BUILT app (dist/)
     and resolved styles are compared against the reference's values:
     colours exactly, lengths within 1px, font families by containment.
     Where one of the seven reconciled values applies, the expectation
     table carries the reconciled value — layer A is what stops that table
     drifting anywhere the reference does not license.

WHAT IT DOES NOT CATCH, stated plainly:

  * Pixel-identical composition. It asserts regions, order, dimensions and
    roles — not that the rendering as a whole looks right. Mide's eye at
    http://localhost:8899/3d/ covers that.
  * Content. Anatomy strings are Stage-8-gated TODOs; the gate asserts
    counts against ``content/heart.json``, never against the reference's
    lorem mock (six structures there, two records today).
  * The renderer's drawing. The placeholder stage art is asserted as
    present, not as art.

THE ALLOW-LIST — deliberate divergences, each with its reason. Nothing else
is tolerated; a mismatch outside this list is a failure.

  1–7. The seven reconciled colours (RECONCILED below): four canonical
       adoptions (ink, muted, rule, accent-text — Design was approximating
       shared/tokens.css by eye before /design-sync existed for this
       surface) and three WCAG darkenings (caption, faint, ghost — the
       reference's values measure 2.29–3.68:1 on the cream ground at
       caption sizes). Ruled in MRB-186 Finding 1; recorded in
       reference/design-notes.md § Divergences.
  8.   Library composition: the reference draws Lungs and Liver selectable
       (3 live rows + 5 coming-soon). The library is content-driven and
       only heart.json exists, so the app ships 1 viewing + 7 coming-soon.
       A specimen leaves the soon list by gaining a content record.
  9.   §03 (the sign-in moment) is absent: not built in Stage 1 — it needs
       the retrieval round result and the account flow, both later stages.
  10.  §07 (Parts) is excluded: a component sheet, not a screen. Its
       hotspot state table is enforced by the no-hue-only gate reading
       hotspotVisual() directly, at exact §07 values.
  11.  Hotspot/structure/fact counts follow content/heart.json, not the
       reference's six-structure mock (see rule 8's principle).
  12.  The reference's phone mocks draw iOS device chrome (status bar,
       9:41, battery). Device chrome is the device's, not the app's.
  13.  The §02 reference draws mid-round state (two answered squares, one
       missed chip). The app opens a round at its start: square 1 current,
       none done, no missed chips yet. Same structure, minute zero.
  14.  The panel's "Record" section has no drawn slot in the reference. It
       is now ONE .fact row — system — and the key-facts count is therefore
       still asserted on the FIRST .facts block only.
       It carried six until MRB-186: renderer, licence, source and acquired
       were implementation and provenance detail on a page whose job is to
       teach biology, and `RENDERER: mesh` is the platform narrating its own
       internals — the standing rule that student-facing pages carry no
       explanatory meta-text about how the platform works. Spec points went
       with them: the ruling puts statement IDs on a teacher-facing surface
       rather than the default student view, and MRB-193 made the
       specimen-level array a fallback a hotspot may override, so the row
       would have stated something untrue about any structure that did.
       All five now live in docs/3d_studio_asset_manifest.md, generated from
       the content records by 3d-studio/tools/asset_manifest.py.
       This block being undrawn is also why nothing caught it rendering
       SYSTEM as SYSTE / M — see the mid-word-break sweep in Layer B, which
       asserts the property across the whole document on every screen rather
       than trusting a selector list to stay complete.
  15.  Accent fills behind small text ship as --st-accent-text #A93411,
       not the reference's #E4572E: .cta (14px), .btn--primary (14.5px,
       panel + tablet + phone sheet), .rbtn-check (15px), the retrieve-mode
       .modeseg .is-on chip (13.5px) and .structchip.is-open .structchip__num
       (10px); the VIEWING caption (.libcard.is-viewing .libcard__meta,
       10.5px) is the same divergence with the accent used AS the text.
       Paper on the raw accent measures 3.62:1 and fails WCAG at these
       sizes — the identical 3.62:1 the accent measures as text on paper,
       which is why Mide ruled (MRB-186) that --st-accent is never a
       contrast partner for text under 24px in either direction. The cream
       label is unchanged, so Design's light-on-warm relationship holds and
       only the depth of the orange moves: 3.62:1 → 6.48:1. The accent is
       untouched wherever it is not a small-text partner — hotspots and the
       §07 table, .railbtn.is-active, .hatch, the .psq--current ring, card
       borders, focus rings, the leader line, the chevron mark — and those
       rows below still assert #E4572E.
  16.  --st-accent-hover #7F2408 is ADDED, with no reference counterpart to
       diverge from (ADOPTED below, not RECONCILED). The reference hovers
       links to the raw accent (a:hover{color:#E4572E}), which rule 15
       disallows: the one link that inherits it is the phone library's
       "Create account" at 13.5px, 3.34:1 on the cream ground. Links now
       deepen instead of brightening, using the canonical
       --ks3-accent-hover the KS3 system already defines for this role
       (8.83:1 on ground). Same reconciliation logic as entries 1–4, but
       an addition rather than a substitution, so the sweep in layer A
       cannot ban the old value — #E4572E remains the live accent.
  17.  The live specimen's library caption wraps to a SECOND LINE, so that
       card stands one row taller than the coming-soon cards beneath it. The
       reference draws a 3-row library whose captions are a system name and
       nothing else — one line each, every card the same height — because the
       reference has no structure count to carry. The app does: MRB-193's
       key-stage ruling makes the count per-viewer (a KS3 student is offered
       nine of the heart's fourteen structures), and the caption is where the
       viewer is told what they will actually find before they open it. A
       card promising fourteen and opening onto nine is the defect that
       ruling exists to prevent, so the count is not optional furniture that
       could be dropped to keep the rows even. Truncating it instead —
       VIEWING · 14 STRUCTU… — deleted precisely the count, which is why the
       nowrap that made it fit is gone. Not compressed, not abbreviated: the
       uneven row is the accepted cost, and the caption is now watched by
       Layer B's metaIntegrity row.
  18.  §10 (Parts — slider) is not driven as a screen, following §07's
       precedent that a component sheet is not a screen. Where §07's state
       table lives in TypeScript and the no-hue-only gate reads it directly,
       §10's lives in CSS — `:hover`, `[data-drag]`, `[data-key]` — which
       jsdom cannot resolve, so its four states are pinned as layer C rows
       driven through the real states in a real browser instead: a pointer
       moved onto the plate, a pointer pressed on it, and arrows sent to it
       once it has focus. Same principle, different place, because that is
       where the values are.
  19.  The materials sheet annotates the cut wall against the cavity as 17:1;
       measured with the WCAG formula the pair is 15.62:1. Design's figure is
       generous by about 9% and the argument — extremes of the frame, not
       neighbours in a family — is unaffected. The measured value is asserted
       in `3d-studio/tests/gates/section.test.ts`; this entry records that
       the reference's own figure is not the one that holds.
  20.  The plane rule is drawn at the strength its geometry earns, not at
       the strength the reference draws. §08 draws a cut face fully facing
       the viewer AND the plane seen edge-on as a crisp vertical rule beside
       it; those two cannot both be true of one plane in three dimensions,
       because a plane is a line on screen only when it is edge-on and covers
       the frame when it is not. A 2D mock can hold both at once and a
       projection cannot. So the rule is drawn where it is true: the default
       camera is a three-quarter view, about 26 degrees off face-on, and the
       rule is there at partial strength, fading out altogether if the
       student turns the specimen to face the cut squarely and coming to full
       strength while the slider is dragged. The s08 rows measure it at the
       default camera, which is where a student meets it; the values pinned
       are its construction — 1.5px, the accent, two 16px end ticks — and not
       an opacity, which is the part that legitimately moves.
  21.  The tablet plate sits at `left: 82px` — the rail's own geometry (18px
       inset + 48px column) plus the drawn 16px gap — rather than the
       reference's literal `calc(50% + 22px)`, which is that same rule
       measured inside its 645px illustration tile. The rule travels; the
       number does not.
  22.  The plane's end ticks are drawn at rest as well as while dragging.
       §08's hero draws them at rest, §09's three at-rest tiles omit them and
       its three dragging tiles draw them; built as one plane-strength
       variable at 0.75 at rest and full strength while dragging, which
       satisfies §08's hero, §09's dragging tiles and both prose lines.

Provenance for every value in the expectation tables below is the frozen
reference itself — section and line cited in each screen's comment.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
import tempfile

import ks3_browser as cdp
from ks3_parity import close_length, parse_rgb, parse_rgba, same_colour

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(HERE, "3d-studio")
TOKENS_CSS = os.path.join(APP, "src", "styles", "tokens.css")

# Design froze the shell at `shell-v1.html` (§01–§07, MRB-186) and the cut at
# `crosssection-v1.html` (§08–§10, MRB-189). BOTH are the reference now, and
# layer A reads them as one text: a colour that exists only because the
# cross-section treatment needed it — the cut wall, the cavity, the plate's
# own chrome — has its provenance in the second file and nowhere in the
# first, so a sweep that only read the first would call it invented.
SHELL_REF = os.path.join(APP, "reference", "shell-v1.html")
CROSSSECTION_REF = os.path.join(APP, "reference", "crosssection-v1.html")
REFERENCE = [SHELL_REF, CROSSSECTION_REF]

# `crosssection-v1.html` redraws §01–§07 before it draws §08–§10, and that
# redrawing is the reason shell-v1.html is still the frozen reference for
# those seven screens rather than being superseded by the newer file: over
# its first 911 lines the two are the same bytes, save the HTML comment on
# line 8 that names the version. Asserted below, because the claim is load
# bearing in both directions — it is what lets every §01–§07 row keep citing
# shell-v1, and it is the only thing that would notice either frozen file
# being edited.
SHARED_PREFIX_LINES = 911
SHARED_PREFIX_COMMENT_LINE = 8
DIST = os.path.join(APP, "dist")
HEART = os.path.join(APP, "content", "heart.json")
RETRIEVAL_TS = os.path.join(APP, "src", "studio", "retrieval.ts")

# Design drew SIX progress squares. Until MRB-191's round-length ruling the
# built round was specimen-length, so the rail drew one square per retrievable
# hotspot — fourteen on the authored heart — and the gate asserted that number,
# which meant the gate agreed with the build and neither agreed with the
# reference. A round is now six, and this is the number the reference drew.
REFERENCE_ROUND_SQUARES = 6

# ── the seven reconciled values (allow-list entries 1–7) ─────────────────
# token, reference value, shipped value, reason
RECONCILED = [
    ("--st-ink", "#1A140E", "#1A1714",
     "adopted canonical --ink (shared/tokens.css); Design's near-miss"),
    ("--st-muted", "#6E6255", "#6E655D",
     "adopted canonical --ks3-ink-faint; Design's near-miss"),
    ("--st-rule", "#E4D6BF", "#E0D2B9",
     "adopted canonical --ks3-rule; Design's near-miss"),
    ("--st-accent-text", "#A63A18", "#A93411",
     "adopted canonical --ks3-accent-text; Design's near-miss"),
    ("--st-caption", "#8A7C6B", "#7A6E5F",
     "darkened: reference value 3.68:1 on ground (fails 4.5), canonical "
     "near-miss --ink-faint is itself 3.81:1; now 4.51:1"),
    ("--st-faint", "#9C8E7B", "#7B6E5C",
     "darkened: reference value 2.90:1 on ground; now 4.51:1"),
    ("--st-ghost", "#B0A18B", "#7D6D55",
     "darkened: reference value 2.29:1 on ground; now 4.55:1"),
]

# ── canonical additions (allow-list entry 16) ────────────────────────────
# A token with no reference counterpart to diverge FROM: the reference
# solved the role with a value the accent-contrast ruling disallows, and the
# canonical system already had a token for it. Unlike RECONCILED these carry
# no old value, so they add nothing to the sweep below — the superseded form
# here is a *usage* (a:hover), not a hex that must vanish from src/.
# token, shipped value, reason
ADOPTED = [
    ("--st-accent-hover", "#7F2408",
     "adopted canonical --ks3-accent-hover; the reference hovers links to "
     "the raw accent (#E4572E, 3.34:1 on ground at 13.5px), which the "
     "MRB-186 accent-contrast ruling disallows for text under 24px"),
]

# the ink alpha forms that follow the ink adoption (swept alongside it)
SUPERSEDED_RGBA = re.compile(r"rgba\(\s*26\s*,\s*20\s*,\s*14\b", re.I)


# ── A. provenance ────────────────────────────────────────────────────────

def studio_tokens():
    """Every --st- hex declared in the app's token file."""
    with open(TOKENS_CSS, encoding="utf-8") as fh:
        css = fh.read()
    return dict(re.findall(r"(--st-[a-z0-9-]+)\s*:\s*(#[0-9A-Fa-f]{6})\s*;", css))


def _shared_prefix_divergences():
    """Every line on which the two frozen files stop agreeing over §01–§07.

    Returns a list of (line number, shell-v1 line, crosssection-v1 line), or
    None when a file is missing. One entry is expected and correct — line 8,
    where the newer file names itself `design reference v2`. Anything else
    means one of the two has been edited, and a frozen file that has moved is
    not a reference: every row in this module cites a line number in one of
    them.
    """
    for path in REFERENCE:
        if not os.path.exists(path):
            return None
    with open(SHELL_REF, encoding="utf-8", errors="replace") as fh:
        shell = fh.read().splitlines()
    with open(CROSSSECTION_REF, encoding="utf-8", errors="replace") as fh:
        cross = fh.read().splitlines()
    out = []
    for i in range(SHARED_PREFIX_LINES):
        a = shell[i] if i < len(shell) else None
        b = cross[i] if i < len(cross) else None
        if a != b:
            out.append((i + 1, a, b))
    return out


def check_provenance():
    """Layer A. Returns (problems, notes)."""
    problems, notes = [], []
    missing = [p for p in REFERENCE if not os.path.exists(p)]
    if missing:
        return (["frozen reference missing: %s"
                 % ", ".join(os.path.relpath(p, HERE) for p in missing)], notes)
    ref = ""
    for path in REFERENCE:
        with open(path, encoding="utf-8", errors="replace") as fh:
            ref += fh.read().lower()

    # The two frozen files agree over §01–§07, which is what keeps shell-v1
    # the reference for those seven screens (design-notes.md says so in its
    # first paragraph, and every §01–§07 row below cites it). Read the claim
    # rather than trust it: it is also the only assertion in this module that
    # would catch an accidental edit to EITHER frozen file.
    diverged = _shared_prefix_divergences()
    expected = [SHARED_PREFIX_COMMENT_LINE]
    if [n for n, _a, _b in diverged] != expected:
        for n, a, b in diverged:
            if n in expected:
                continue
            problems.append(
                "the two frozen references disagree at line %d of their "
                "shared §01–§07 — shell-v1 has %r, crosssection-v1 has %r. "
                "Only line %d (the version comment) may differ; one of the "
                "two files has been edited, and every row here cites a line "
                "number in them" % (n, a, b, SHARED_PREFIX_COMMENT_LINE))
        if SHARED_PREFIX_COMMENT_LINE not in [n for n, _a, _b in diverged]:
            problems.append(
                "line %d of the two frozen references is now identical — the "
                "version comment that told `design reference` from `design "
                "reference v2` has gone, so one of them has been edited"
                % SHARED_PREFIX_COMMENT_LINE)
    else:
        notes.append(
            "the frozen references are byte-identical over lines 1–%d "
            "(§01–§07), differing only in the version comment on line %d — "
            "shell-v1.html remains the reference for those seven screens"
            % (SHARED_PREFIX_LINES, SHARED_PREFIX_COMMENT_LINE))

    tokens = studio_tokens()
    reconciled = {name: (old, new) for name, old, new, _ in RECONCILED}
    adopted = {name: new for name, new, _ in ADOPTED}
    for name, hexval in sorted(tokens.items()):
        if name in reconciled:
            old, new = reconciled[name]
            if hexval.lower() != new.lower():
                problems.append(
                    "%s = %s but the MRB-186 reconciliation ruled %s — the "
                    "reconciled value has drifted" % (name, hexval, new))
            if old.lower() not in ref:
                problems.append(
                    "%s claims to diverge from reference value %s, but that "
                    "value is not in the reference — the allow-list entry is "
                    "wrong" % (name, old))
        elif name in adopted:
            # No reference presence to assert — that is the point of the
            # entry. Pin the value so the addition cannot drift either.
            if hexval.lower() != adopted[name].lower():
                problems.append(
                    "%s = %s but the MRB-186 adoption ruled %s — the adopted "
                    "value has drifted" % (name, hexval, adopted[name]))
        elif hexval.lower() not in ref:
            problems.append(
                "%s = %s does not appear anywhere in the frozen reference — "
                "invented or drifted, and not in the reconciliation "
                "allow-list" % (name, hexval))
    notes.append("%d tokens checked against the reference, %d on the "
                 "reconciliation allow-list, %d on the canonical-addition "
                 "allow-list" % (len(tokens), len(RECONCILED), len(ADOPTED)))

    # The sweep stays swept: superseded values must not reappear in the
    # app source or the design-sync durable set (the reference and the
    # divergence record legitimately cite them).
    sweep_roots = [os.path.join(APP, "src"), os.path.join(HERE, ".design-sync")]
    old_hexes = [old.lower() for _, old, _, _ in RECONCILED]
    hits = []
    for root in sweep_roots:
        for dirpath, _dirs, files in os.walk(root):
            for f in files:
                if not f.endswith((".ts", ".tsx", ".css", ".md", ".json", ".html")):
                    continue
                p = os.path.join(dirpath, f)
                with open(p, encoding="utf-8", errors="replace") as fh:
                    text = fh.read().lower()
                for old in old_hexes:
                    if old in text:
                        hits.append("%s carries superseded %s" %
                                    (os.path.relpath(p, HERE), old))
                if SUPERSEDED_RGBA.search(text):
                    hits.append("%s carries superseded rgba(26,20,14,…) ink" %
                                os.path.relpath(p, HERE))
    problems.extend(hits)

    # The rail and the round have to be the same number. Counting squares on
    # the built page (layer B) proves the rail matches the reference; this
    # proves the round the rail is drawing matches it too.
    size = _round_size_in_source()
    if size is None:
        problems.append(
            "could not read ROUND_SIZE out of src/studio/retrieval.ts — the "
            "round length and Design's rail can no longer be compared")
    elif size != REFERENCE_ROUND_SQUARES:
        problems.append(
            "ROUND_SIZE = %d but the frozen reference draws %d progress "
            "squares — a round of %d would either overflow the rail or leave "
            "it short (MRB-191)"
            % (size, REFERENCE_ROUND_SQUARES, size))
    else:
        notes.append("round length %d matches the reference's %d squares"
                     % (size, REFERENCE_ROUND_SQUARES))

    return (problems, notes)


# ── C. computed-style expectations ───────────────────────────────────────
#
# `on` names the screen (driven by SCREENS below); `sel` is the first match.
# Colours exact (reconciled values where allow-listed), lengths within 1px
# (ks3_parity.TOL_PX), font-family by containment, anything else by string.
# Provenance: shell-v1.html, section cited per block.

COMPONENTS = [
    # ── §01 desktop exploration (reference lines 44–233) ──
    dict(name="page ground + UI type", on="s01", sel="body",
         props={"background-color": "#FBF3E6", "color": "#1A1714",
                "font-family": "Instrument Sans"}),
    dict(name="top bar", on="s01", sel=".topbar",
         props={"height": "64px", "border-bottom-color": "#E0D2B9"}),
    dict(name="brand wordmark", on="s01", sel=".brand",
         props={"font-family": "Bricolage Grotesque", "font-weight": "600",
                "font-size": "18px", "color": "#1A1714"}),
    dict(name="nav resting item", on="s01", sel=".topbar__nav span",
         props={"color": "#6E655D", "font-size": "15px"}),
    dict(name="nav current item", on="s01", sel=".topbar__nav .is-here",
         props={"color": "#1A1714"}),
    # accent-text fill, not the reference's #E4572E (allow-list rule 15)
    dict(name="create-account CTA", on="s01", sel=".cta",
         props={"background-color": "#A93411", "color": "#FFFDF8",
                "font-size": "14px", "font-weight": "600",
                "border-top-left-radius": "8px"}),
    dict(name="breadcrumb strip", on="s01", sel=".crumbstrip",
         props={"height": "56px", "background-color": "#F7EDDC"}),
    dict(name="breadcrumb is mono caption", on="s01", sel=".crumb",
         props={"font-family": "DM Mono", "font-size": "12px",
                "color": "#7A6E5F"}),
    dict(name="mode trough", on="s01", sel=".modeseg",
         props={"background-color": "#EBDDC5", "border-top-left-radius": "9px"}),
    dict(name="mode selected chip", on="s01", sel=".modeseg .is-on",
         props={"background-color": "#FFFDF8", "color": "#1A1714",
                "font-weight": "600", "font-size": "13.5px"}),
    dict(name="LIBRARY eyebrow", on="s01", sel=".library__head .eyebrow",
         props={"font-family": "DM Mono", "font-size": "10.5px",
                "color": "#7A6E5F"}),
    dict(name="library count is ghost", on="s01", sel=".library__count",
         props={"color": "#7D6D55", "font-size": "11px"}),
    dict(name="viewing card", on="s01", sel=".libcard.is-viewing",
         props={"background-color": "#FFFDF8", "border-top-color": "#E4572E",
                "border-top-width": "1.5px", "border-top-left-radius": "10px"}),
    # the accent used AS text — accent-text, not #E4572E (allow-list rule 15)
    dict(name="viewing card meta is accent", on="s01",
         sel=".libcard.is-viewing .libcard__meta",
         props={"color": "#A93411", "font-family": "DM Mono"}),
    dict(name="coming-soon card dims", on="s01", sel=".libcard.is-soon",
         props={"opacity": "0.52"}),
    dict(name="stage viewport frame", on="s01", sel=".stage--viewport",
         props={"border-top-left-radius": "12px", "border-top-color": "#C9B896"}),
    # ── §01 with a structure open (screen s01open) ──
    # Carried forward from Stage 2: the harness never opened a callout, which
    # is how a clipping defect survived it. Driven by a real click on the
    # panel's structure chip, which is also the only way to measure the
    # is-open numeral well the accent-contrast ruling changed (entry 15).
    dict(name="open callout card", on="s01open", sel=".callout",
         props={"width": "216px", "background-color": "rgba(16, 13, 10, 0.95)",
                "border-top-color": "#4A4136"}),
    dict(name="callout structure eyebrow", on="s01open", sel=".callout__eyebrow",
         props={"color": "#F0885F"}),
    dict(name="callout title is cream display", on="s01open", sel=".callout__title",
         props={"color": "#FBF3E6", "font-family": "Bricolage Grotesque"}),
    dict(name="callout detail is muted on dark", on="s01open", sel=".callout__detail",
         props={"color": "#A99B89"}),
    dict(name="leader line runs from the dot", on="s01open", sel=".leader",
         props={"height": "1.5px"}),
    dict(name="open structure numeral well", on="s01open",
         sel=".structchip.is-open .structchip__num",
         props={"background-color": "#A93411", "color": "#FFFDF8"}),
    dict(name="open hotspot inverts to cream", on="s01open",
         sel='.hotspot[data-state="open"]',
         props={"background-color": "#FBF3E6", "color": "#1A1714",
                "width": "38px"}),
    dict(name="tool rail", on="s01", sel=".rail",
         props={"width": "48px", "border-top-left-radius": "15px"}),
    dict(name="active tool is accent", on="s01", sel=".railbtn.is-active",
         props={"background-color": "#E4572E", "width": "36px", "height": "36px"}),
    dict(name="quality chip word", on="s01", sel=".chip__word",
         props={"font-family": "DM Mono", "font-size": "10.5px",
                "color": "#B7AA98"}),
    dict(name="stage hint", on="s01", sel=".stagehint",
         props={"font-family": "DM Mono", "font-size": "11.5px",
                "color": "#8A7E6E"}),
    dict(name="info panel shell", on="s01", sel=".panel",
         props={"background-color": "#FFFDF8", "border-top-color": "#E0D2B9",
                "border-top-left-radius": "12px"}),
    dict(name="key-stage chip", on="s01", sel=".kchip",
         props={"font-family": "DM Mono", "font-size": "10.5px",
                "color": "#7A6E5F", "border-top-color": "#E0D2B9"}),
    dict(name="accent chip is tinted", on="s01", sel=".kchip--accent",
         props={"color": "#A93411", "background-color": "#FCEFE9",
                "border-top-color": "#F0C9B8"}),
    dict(name="specimen name", on="s01", sel=".panel__name",
         props={"font-family": "Bricolage Grotesque", "font-weight": "600",
                "font-size": "36px"}),
    dict(name="epithet", on="s01", sel=".panel__epithet",
         props={"color": "#7A6E5F", "font-style": "italic", "font-size": "16px"}),
    dict(name="description", on="s01", sel=".panel__desc",
         props={"color": "#3D352C", "font-size": "16.5px"}),
    dict(name="structure numeral well", on="s01", sel=".structchip__num",
         props={"background-color": "#F2E8D6", "color": "#7A6E5F"}),
    dict(name="structure label", on="s01", sel=".structchip__label",
         props={"color": "#6E655D", "font-size": "13.5px"}),
    dict(name="fact label", on="s01", sel=".fact__label",
         props={"font-family": "DM Mono", "font-size": "11.5px",
                "color": "#7A6E5F"}),
    dict(name="why-it-matters is ink block", on="s01", sel=".matters",
         props={"background-color": "#1A1714", "border-top-left-radius": "11px"}),
    dict(name="why-it-matters eyebrow is ember", on="s01",
         sel=".matters__eyebrow", props={"color": "#F2946E"}),
    dict(name="why-it-matters body", on="s01", sel=".matters__body",
         props={"color": "#C9BDAC", "font-size": "13.5px"}),
    dict(name="did-you-know note", on="s01", sel=".didyouknow",
         props={"background-color": "#F5EAD6", "border-top-color": "#D8C7A9",
                "border-top-style": "dashed"}),
    dict(name="open lesson button", on="s01", sel=".btn--outline",
         props={"color": "#1A1714", "background-color": "#FFFDF8",
                "border-top-color": "#DECCAE", "font-weight": "600",
                "font-size": "14.5px"}),
    dict(name="start retrieval button", on="s01", sel=".btn--primary",
         props={"background-color": "#A93411", "color": "#FFFDF8",
                "border-top-left-radius": "9px"}),  # rule 15
    dict(name="hotspot numeral is mono", on="s01", sel=".hotspot",
         props={"font-family": "DM Mono", "font-weight": "500"}),

    # ── §02 desktop retrieval (reference lines 258–335) ──
    dict(name="the room goes dark", on="s02", sel=".app",
         props={"background-color": "#15110C"}),
    dict(name="brand flips to cream", on="s02", sel=".brand",
         props={"color": "#FBF3E6"}),
    dict(name="hatch strip", on="s02", sel=".hatch", props={"height": "7px"}),
    dict(name="retrieve trough darkens", on="s02", sel=".modeseg",
         props={"background-color": "#241E17"}),
    dict(name="retrieve selected chip is accent", on="s02",
         sel=".modeseg .is-on",
         props={"background-color": "#A93411", "color": "#FFFDF8"}),  # rule 15
    dict(name="end round button", on="s02", sel=".endround",
         props={"color": "#B7AA98", "border-top-color": "#3E362C"}),
    dict(name="question panel", on="s02", sel=".rpanel",
         props={"background-color": "#1E1913", "border-top-color": "#3A322A",
                "border-top-left-radius": "12px", "padding-top": "26px"}),
    dict(name="ROUND eyebrow", on="s02", sel=".rpanel__round",
         props={"font-family": "DM Mono", "color": "#8E8272"}),
    dict(name="current progress square", on="s02", sel=".psq--current",
         props={"border-top-color": "#E4572E", "background-color": "#2A2119",
                "width": "34px", "height": "34px",
                "border-top-left-radius": "7px"}),
    dict(name="ask line is ember", on="s02", sel=".rpanel__ask",
         props={"color": "#F2946E", "font-family": "DM Mono"}),
    dict(name="answer well", on="s02", sel=".rinput",
         props={"background-color": "#120F0B", "border-top-color": "#4A4036",
                "height": "64px", "border-top-left-radius": "11px"}),
    dict(name="check button", on="s02", sel=".rbtn-check",
         props={"background-color": "#A93411", "color": "#FFFDF8",
                "font-weight": "600", "font-size": "15px"}),  # rule 15
    dict(name="skip button", on="s02", sel=".rbtn-skip",
         props={"color": "#B7AA98", "border-top-color": "#4A4036"}),
    dict(name="reveal link is ember", on="s02", sel=".rreveal__link",
         props={"color": "#F2946E"}),
    dict(name="missed note is room-faint", on="s02", sel=".rmissed__note",
         props={"color": "#7E7263", "font-size": "13px"}),
    dict(name="target hotspot", on="s02", sel='.hotspot[data-state="target"]',
         props={"width": "52px", "background-color": "#FBF3E6",
                "border-top-width": "4px", "border-top-color": "#E4572E",
                "font-size": "22px"}),
    dict(name="inert hotspot", on="s02", sel='.hotspot[data-state="inert"]',
         props={"width": "13px"}),

    # ── §04 tablet 834pt (reference lines 435–556) ──
    dict(name="tablet top bar drops to 60", on="s04", sel=".topbar",
         props={"height": "60px"}),
    dict(name="Specimens trigger", on="s04", sel=".libtrigger",
         props={"border-top-color": "#DECCAE", "border-top-width": "1.5px",
                "background-color": "#FFFDF8", "border-top-left-radius": "9px",
                "font-size": "13.5px"}),
    dict(name="stage fixed at 520", on="s04", sel=".stage",
         props={"height": "520px"}),
    dict(name="tablet panel", on="s04", sel=".tpanel",
         props={"background-color": "#FFFDF8", "border-top-color": "#E0D2B9",
                "border-top-left-radius": "12px"}),
    dict(name="tablet name drops to 34", on="s04", sel=".tpanel .panel__name",
         props={"font-size": "34px"}),
    dict(name="drawer is 372", on="s04drawer", sel=".drawer",
         props={"width": "372px", "background-color": "#FBF3E6",
                "border-right-color": "#D9C9AC"}),
    dict(name="drawer title", on="s04drawer", sel=".drawer__title",
         props={"font-family": "Bricolage Grotesque", "font-size": "22px",
                "font-weight": "600"}),
    dict(name="drawer rows are roomier", on="s04drawer",
         sel=".drawer .libcard--big .libcard__name",
         props={"font-size": "16px"}),

    # ── §05 phone 390pt (reference lines 589–737) ──
    dict(name="phone top bar drops to 52", on="s05", sel=".topbar",
         props={"height": "52px"}),
    dict(name="menu trigger is square", on="s05", sel=".libtrigger--square",
         props={"width": "38px", "height": "38px",
                "border-top-left-radius": "10px"}),
    dict(name="phone sign-in is accent text", on="s05", sel=".signin",
         props={"color": "#A93411", "font-size": "13px", "font-weight": "600"}),
    dict(name="sheet", on="s05", sel=".sheet",
         props={"background-color": "#FFFDF8", "border-top-left-radius": "18px",
                "border-top-color": "#E0D2B9"}),
    dict(name="sheet handle", on="s05", sel=".sheet__handle",
         props={"width": "44px", "height": "4px", "background-color": "#DECCAE"}),
    dict(name="sheet name drops to 32", on="s05", sel=".sheet .panel__name",
         props={"font-size": "32px"}),
    dict(name="horizontal rail button", on="s05", sel=".railbtn",
         props={"width": "40px", "height": "40px",
                "border-top-left-radius": "11px"}),
    dict(name="pinned primary action", on="s05", sel=".sheet__foot .btn--primary",
         props={"background-color": "#A93411", "color": "#FFFDF8"}),  # rule 15
    dict(name="raised sheet handle darkens", on="s05raised",
         sel=".sheet.is-raised .sheet__handle",
         props={"background-color": "#C9B79A"}),
    dict(name="phone library close is ink", on="s05lib", sel=".phonelib__close",
         props={"background-color": "#1A1714", "width": "38px",
                "border-top-left-radius": "10px"}),
    dict(name="phone library title", on="s05lib", sel=".phonelib__title",
         props={"font-family": "Bricolage Grotesque", "font-size": "20px"}),
    dict(name="phone library CTA", on="s05lib", sel=".phonelib__cta",
         props={"color": "#A93411", "font-weight": "600"}),

    # ── §06 flat stage (reference lines 758–795) ──
    dict(name="paper stage", on="s06", sel=".stage--paper",
         props={"background-color": "#FFFDF8", "border-top-color": "#D9C9AC",
                "border-top-left-radius": "12px"}),
    # Selector changed at Stage 5 (MRB-190), values unchanged. `.ph-plate`
    # was the Stage 1 PLACEHOLDER's drawn form; the flat renderer replaces it
    # with a real plate frame around the specimen's own diagram. Same role,
    # same reference values, real element. Flagged in the Stage 5 report.
    dict(name="plate outline", on="s06", sel=".plate",
         props={"border-top-color": "#B6AC9C", "border-top-width": "2px",
                "background-color": "#DED7CB"}),
    dict(name="FLAT DIAGRAM chip", on="s06", sel=".flatchip",
         props={"background-color": "#F5EAD6", "border-top-color": "#D8C7A9"}),
    dict(name="flat chip mark is ink", on="s06", sel=".flatchip__mark",
         props={"background-color": "#1A1714", "width": "8px", "height": "8px"}),
    dict(name="paper rail", on="s06", sel=".rail",
         props={"background-color": "#FFFDF8", "border-top-color": "#DECCAE"}),
    dict(name="paper hint is faint", on="s06", sel=".stagehint",
         props={"color": "#7B6E5C"}),
    dict(name="paper hotspot keeps accent fill", on="s06", sel=".hotspot",
         props={"background-color": "#E4572E", "border-top-color": "#FFFDF8",
                "width": "28px"}),

    # ── §10 Parts — slider (crosssection-v1.html lines 1305–1415) ──
    #
    # §10 is the component sheet for the slider the way §07 is for the
    # hotspot, and it is read the same way: as the source of truth for every
    # state rather than as one more screen to drive. The difference is where
    # the states live. §07's are a TypeScript table, so the no-hue-only gate
    # reads the function and needs no browser; §10's are CSS — `:hover`,
    # `[data-drag]`, `[data-key]` — and a stylesheet only answers to a real
    # engine. So the four rows are driven here, through a real pointer moved
    # onto the plate, a real press on it, and real arrow keys once it has
    # focus (allow-list entry 18).
    #
    # Rest is the sheet's first row (line 1320) and also the §08 hero's
    # slider (line 975) and §09's AT REST tile (line 1109) — three drawings
    # of the same plate, which is why the values below are cited once.
    dict(name="section plate at rest", on="s08", sel=".secplate",
         props={"width": "392px", "height": "44px",
                "background-color": "rgba(22, 18, 14, 0.86)",
                "border-top-color": "#3E362C",
                "border-top-left-radius": "11px"}),
    dict(name="SECTION eyebrow", on="s08", sel=".secplate__word",
         props={"font-family": "DM Mono", "font-size": "10.5px",
                "color": "#8A7E6E"}),
    dict(name="slider track", on="s08", sel=".secplate__track",
         props={"height": "4px"}),
    dict(name="travelled track", on="s08", sel=".secplate__travel",
         props={"background-color": "#C4B8A7"}),
    # "The handle is a bar, not a knob, because the thing it moves is a
    # plane." Cream fill and a dark ring — the hotspot construction, which is
    # what survived the washed-projector test, inherited rather than argued
    # again (§10 HANDLE ANATOMY).
    dict(name="handle is a bar", on="s08", sel=".secplate__handle",
         props={"width": "10px", "height": "30px",
                "border-top-left-radius": "3px",
                "background-color": "#FBF3E6"}),
    dict(name="readout is a caption at rest", on="s08", sel=".secplate__value",
         props={"font-family": "DM Mono", "font-size": "11.5px",
                "color": "#B7AA98"}),
    # ── §10 hover (line 1332) ──
    dict(name="plate lifts under the pointer", on="s08hover", sel=".secplate",
         props={"background-color": "rgba(22, 18, 14, 0.92)",
                "border-top-color": "#4A4036"}),
    dict(name="handle thickens on hover", on="s08hover",
         sel=".secplate__handle", props={"width": "11px", "height": "34px"}),
    # ── §10 dragging (line 1344) ──
    # "Dragging thickens the handle, hatches the travelled track to match the
    # cut face, promotes the value from caption to 15px, and brings the plane
    # rule up to full strength. Emphasis lands on the cut, not on the
    # furniture" (§09) — this is the loudest the furniture is allowed to get.
    dict(name="plate deepens while dragging", on="s08drag", sel=".secplate",
         props={"background-color": "rgba(18, 14, 10, 0.96)",
                "border-top-color": "#5C5347"}),
    dict(name="handle thickens again while dragging", on="s08drag",
         sel=".secplate__handle", props={"width": "12px", "height": "38px"}),
    dict(name="readout is promoted while dragging", on="s08drag",
         sel=".secplate__value",
         props={"font-size": "15px", "font-weight": "500",
                "color": "#FBF3E6"}),
    # The reference deepens the eyebrow to #6E6255 while dragging; that is
    # the value --st-muted reconciles to #6E655D, so it ships as the token
    # (allow-list entry 2) rather than as the reference's near-miss.
    dict(name="eyebrow deepens while dragging", on="s08drag",
         sel=".secplate__word", props={"color": "#6E655D"}),
    # ── §10 keyboard (line 1356) ──
    # "ARROWS STEP 2%, NOTCHED HANDLE". Drawn, therefore required: the notch
    # is the state's own mark — the ring says this has focus, the notch says
    # this is the thing the arrows move.
    dict(name="keyboard handle is notched", on="s08key",
         sel=".secplate__notch",
         props={"width": "2px", "height": "14px", "opacity": "1"}),
    dict(name="keyboard focus ring is on the plate", on="s08key",
         sel=".secplate",
         props={"outline-color": "#FBF3E6", "outline-width": "2px"}),
    # ── §08 the plane's own mark (lines 942–944) ──
    # The only accent in the whole cross-section treatment: "Orange comes off
    # the organ entirely. It marks the plane — the rule through the specimen,
    # its end ticks, and the slider being dragged — because the plane is the
    # interactive thing. Tissue is substance and never highlights itself."
    # Drawn at rest as well as while dragging (allow-list entry 22); how
    # strongly is a function of how edge-on the plane is (entry 20).
    dict(name="plane rule", on="s08", sel=".planerule",
         props={"width": "1.5px"}),
    dict(name="plane end tick", on="s08", sel=".planerule__tick",
         props={"width": "16px", "height": "1.5px",
                "background-color": "#E4572E"}),
    # ── §09 tablet (line 1176) ──
    # "Same plate, narrower … Height stays 44 because it is now a touch
    # target." Where it sits is layer B's row; that it did not also shrink is
    # this one.
    dict(name="tablet plate is narrower", on="s09t", sel=".secplate",
         props={"width": "320px", "height": "44px"}),
    # ── §09 phone (lines 1247–1255) ──
    # ONE BAR, SHARED WITH THE RAIL. The collapsed tool is "orange, cream
    # dot, 44 square", and the plate is the rest of that same bar at the same
    # height and the same radius — one bar, drawn as one.
    dict(name="phone plate keeps its 44", on="s09p", sel=".secplate",
         props={"height": "44px", "border-top-left-radius": "12px"}),
    dict(name="collapsed rail is the running tool", on="s09p",
         sel=".rail[data-collapsed] .railbtn.is-active",
         props={"width": "44px", "height": "44px",
                "border-top-left-radius": "12px",
                "background-color": "#E4572E"}),
    # ── §09 phone, dragging (line 1273) ──
    # The readout lifted out of the bar carries the dragging plate's own
    # chrome, because it is the plate's readout wearing the plate's state.
    dict(name="lifted readout", on="s09pdrag", sel=".secreadout",
         props={"background-color": "rgba(18, 14, 10, 0.96)",
                "border-top-color": "#5C5347"}),
    dict(name="lifted readout value", on="s09pdrag", sel=".secreadout__value",
         props={"font-size": "15px", "color": "#FBF3E6"}),
]


# ── B. structural rules, per screen ──────────────────────────────────────

_JS = r"""
window.__st = {
  q: function (s) { return document.querySelector(s); },
  n: function (s) { return document.querySelectorAll(s).length; },
  text: function (s) {
    var el = document.querySelector(s);
    return el ? (el.textContent || '').trim() : null;
  },
  style: function (s, p, pseudo) {
    var el = document.querySelector(s);
    if (!el) { return null; }
    return getComputedStyle(el, pseudo || null).getPropertyValue(p);
  },
  visible: function (s) {
    var el = document.querySelector(s);
    if (!el) { return false; }
    var cs = getComputedStyle(el);
    return cs.display !== 'none' && cs.visibility !== 'hidden';
  },
  click: function (s) {
    var el = document.querySelector(s);
    if (!el) { return false; }
    el.click();
    return true;
  },
  keyFactRows: function () {
    var blocks = document.querySelectorAll('.facts');
    return blocks.length ? blocks[0].querySelectorAll('.fact').length : 0;
  },
  /** Every edge of `sel` inside every edge of `within`, in px overflow.
   *  The clipping defect MRB-187 found — a callout placed at dot + 90px
   *  unconditionally, which fell off the stage the moment real geometry put a
   *  dot near the right edge — is invisible to every count and every colour
   *  in this file, and was only caught by driving the app by hand. */
  overflow: function (sel, within) {
    var a = document.querySelector(sel);
    var b = document.querySelector(within);
    if (!a || !b) { return null; }
    var r = a.getBoundingClientRect();
    var s = b.getBoundingClientRect();
    return {
      left: Math.max(0, s.left - r.left),
      top: Math.max(0, s.top - r.top),
      right: Math.max(0, r.right - s.right),
      bottom: Math.max(0, r.bottom - s.bottom)
    };
  },
  rect: function (sel) {
    var el = document.querySelector(sel);
    if (!el) { return null; }
    var r = el.getBoundingClientRect();
    return { x: r.x, y: r.y, w: r.width, h: r.height };
  },
  /** Every place the rendered text breaks INSIDE a word, anywhere on the page.
   *
   *  MRB-186: the panel's label column rendered SYSTEM as SYSTE / M, LICENCE as
   *  LICE / NCE and SOURCE as SOU / RCE, on desktop at full width, through
   *  every screenshot of the build. No row caught it, because the Record block
   *  is furniture the frozen reference does not draw, so nothing was asserting
   *  anything about it. A rendered-output gate that cannot catch a mid-word
   *  break is not doing its job — so this asserts the PROPERTY over the whole
   *  document rather than a list of selectors somebody has to remember to
   *  extend. It costs nothing on text that does not wrap.
   *
   *  Method: walk the line boxes. For each text node, ask for one rect per
   *  character; a break is a jump in the rect's top edge. A jump between two
   *  non-space characters is a break inside a word. Wrapping at a space is
   *  normal and never reported, and a break after a hyphen or a slash is a
   *  legitimate break opportunity, so those are allowed too. */
  midWordBreaks: function () {
    var out = [];
    var AFTER_OK = '-‐‑‒–—―­/​';
    var walker = document.createTreeWalker(
      document.body, NodeFilter.SHOW_TEXT, null);
    var node, range = document.createRange();
    while ((node = walker.nextNode())) {
      var s = node.nodeValue;
      if (!s || !/\S/.test(s)) { continue; }
      var el = node.parentElement;
      if (!el) { continue; }
      var cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') { continue; }
      // One line box means nothing wrapped: nothing to look at.
      range.selectNodeContents(node);
      if (range.getClientRects().length <= 1) { continue; }
      var prevTop = null, prevCh = null;
      for (var i = 0; i < s.length; i++) {
        var ch = s.charAt(i);
        range.setStart(node, i);
        range.setEnd(node, i + 1);
        var rects = range.getClientRects();
        if (!rects.length) { prevTop = null; prevCh = ch; continue; }
        var top = Math.round(rects[0].top * 10) / 10;
        if (prevTop !== null && top > prevTop + 1
            && /\S/.test(ch) && prevCh !== null && /\S/.test(prevCh)
            && AFTER_OK.indexOf(prevCh) === -1) {
          var word = (s.slice(0, i).split(/\s/).pop() || '')
            + ' / ' + (s.slice(i).split(/\s/)[0] || '');
          var where = el.tagName.toLowerCase()
            + (el.className && typeof el.className === 'string'
               ? '.' + el.className.trim().split(/\s+/).join('.') : '');
          out.push({ sel: where, split: word });
          break;  // one report per text node is enough to fail it
        }
        prevTop = top; prevCh = ch;
      }
    }
    return out;
  },
  /** The document's own scroll extent against the viewport. */
  pageHeight: function () {
    return {
      body: document.body.scrollHeight,
      doc: document.documentElement.scrollHeight,
      vh: window.innerHeight,
      appH: Math.round(
        (document.querySelector('.app') || document.body)
          .getBoundingClientRect().height),
      panelScrolls: (function () {
        var el = document.querySelector('.panel__scroll');
        return el ? el.scrollHeight > el.clientHeight + 1 : null;
      })()
    };
  },
  /** Every .libcard__meta: is it whole, and does it wrap between words only?
   *
   *  MRB-186 asked for exactly this on the RECORD label column and noted the
   *  parity gate had nothing watching it. This is that watch, pointed at the
   *  library caption — which broke the same way from the other end: with
   *  `white-space: nowrap` the caption did not split a word, it silently
   *  DELETED one, VIEWING · 14 STRUCTU…, and what it deleted was the
   *  structure count, the single thing that caption exists to tell the
   *  viewer (MRB-193: a card promising fourteen structures must not open
   *  onto nine).
   *
   *  WHAT IT CAN CATCH
   *    a. Truncation: rendered content wider than the box that holds it.
   *       True whether or not an ellipsis is drawn, so `overflow: hidden`
   *       without `text-overflow` — a silent clip — fails the same way.
   *    b. A break that falls inside a word, measured off the REAL line boxes
   *       one character at a time. Not a string-length guess: a guess would
   *       need the font metrics this is measuring, and would go wrong the
   *       first time the tracking or the webfont changed.
   *    c. A computed wrap property that licenses (b) even where today's
   *       string happens to fit — `overflow-wrap` and `word-break` both
   *       inherit, so this can be handed in from an ancestor.
   *
   *  WHAT IT CANNOT CATCH
   *    * Composition. That the live card now stands one line taller than the
   *      coming-soon cards is asserted nowhere and cannot be: whether that
   *      reads well is Mide's eye at localhost:8899/3d/, not a measurement.
   *    * A break that is legal but reads badly — "· 14" left stranded at the
   *      end of a line breaks no word and passes here.
   *    * Text hidden by an ANCESTOR's clipping rather than the caption's own
   *      overflow. (b) walks this element's line boxes, not its visibility
   *      inside .library__list.
   *    * Anything at all before the mono webfont lands, which is why the
   *      driver waits on document.fonts before any of this is measured. */
  metaIntegrity: function () {
    var out = [];
    var AFTER_OK = '-‐‑‒–—―­/​';
    var els = document.querySelectorAll('.libcard__meta');
    var range = document.createRange();
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      var cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') { continue; }
      var rec = {
        text: (el.textContent || '').trim(),
        over: Math.round(el.scrollWidth - el.clientWidth),
        ws: cs.whiteSpace, ow: cs.overflowWrap, wb: cs.wordBreak,
        lines: 1, split: null
      };
      var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null);
      var node, tops = {};
      while ((node = walker.nextNode())) {
        var s = node.nodeValue || '';
        var prevTop = null, prevCh = null;
        for (var j = 0; j < s.length; j++) {
          var ch = s.charAt(j);
          range.setStart(node, j);
          range.setEnd(node, j + 1);
          var rects = range.getClientRects();
          if (!rects.length) { prevTop = null; prevCh = ch; continue; }
          var top = Math.round(rects[0].top * 10) / 10;
          tops[top] = true;
          if (prevTop !== null && top > prevTop + 1
              && /\S/.test(ch) && prevCh !== null && /\S/.test(prevCh)
              && AFTER_OK.indexOf(prevCh) === -1 && !rec.split) {
            rec.split = (s.slice(0, j).split(/\s/).pop() || '')
              + ' / ' + (s.slice(j).split(/\s/)[0] || '');
          }
          prevTop = top;
          prevCh = ch;
        }
      }
      rec.lines = Object.keys(tops).length || 1;
      out.push(rec);
    }
    return out;
  },
  order: function (parent, sels) {
    var p = document.querySelector(parent);
    if (!p) { return null; }
    var pos = [];
    for (var i = 0; i < sels.length; i++) {
      var el = p.querySelector(sels[i]);
      if (!el) { return 'missing:' + sels[i]; }
      var all = Array.prototype.slice.call(p.querySelectorAll('*'));
      pos.push(all.indexOf(el));
    }
    for (var j = 1; j < pos.length; j++) {
      if (pos[j] <= pos[j - 1]) { return 'out-of-order:' + sels[j]; }
    }
    return 'ok';
  }
};
"""


def _round_size_in_source():
    """ROUND_SIZE as the shell actually ships it.

    Counting squares on the built page proves the rail matches the reference.
    It does not prove the ROUND SIZE matches — a build could draw six squares
    over a round of fourteen. Reading the constant closes that, and makes a
    future change to it a deliberate re-reading of Design's rail rather than a
    silent divergence from it.
    """
    with open(RETRIEVAL_TS, encoding="utf-8") as fh:
        m = re.search(r"export const ROUND_SIZE\s*=\s*(\d+)", fh.read())
    return int(m.group(1)) if m else None


def plate_blocker():
    """The reason §06 cannot be measured, or None when it can.

    ⚠️ THIS IS THE ONE PLACE THIS GATE IS ALLOWED NOT TO MEASURE A SCREEN, and
    it exists because of a ruling, not because a check was inconvenient.

    MRB-215 took the generated fixtures out of the production build: a
    `_`-prefixed file never reaches dist/, and the stand-in resolvers return
    null when the command is `build`. `heart.glb` is acquired so the mesh path
    is unaffected — but `assets.fallback` is still a Stage-8 TODO, so the flat
    renderer now has NO plate in a production build and reports 'failed'.

    §06 is the flat stage. Two of its rows (`.plate__image`, and one `.hotspot`
    per structure) exist only once a plate has loaded, so the screen is not
    merely failing — it is unmeasurable until a drawn diagram lands in
    public/assets/. Measuring it against a fixture instead is exactly what the
    ruling refused: a thing that looks like a diagram, carrying no anatomy,
    hiding the gap.

    So the screen is reported BLOCKED and named in the summary, never silently
    dropped and never counted as driven. The trigger is deliberately narrow:
    only an unacquired `assets.fallback` blocks it. If a plate lands and §06
    then fails or diverges, that is an ordinary failure and this returns None.
    """
    with open(HEART, encoding="utf-8") as fh:
        fallback = (json.load(fh).get("assets") or {}).get("fallback") or ""
    if not fallback.startswith("TODO"):
        return None
    return ("assets.fallback in content/heart.json is still an unacquired "
            "TODO, so a production build ships no plate — a drawn heart plate "
            "in 3d-studio/public/assets/ is a Tier D launch blocker")


def _content_counts():
    with open(HEART, encoding="utf-8") as fh:
        heart = json.load(fh)
    hotspots = heart["hotspots"]
    return {
        "hotspots": len(hotspots),
        "retrievable": sum(1 for h in hotspots if h.get("retrievable")),
        "facts": len(heart["keyFacts"]),
        # 1 real record + the 7 approved coming-soon names in
        # src/studio/content.ts (allow-list rule 8)
        "library": 8,
        "soon": 7,
    }


# Screens driven at a desktop viewport. On these the page is exactly one
# screen tall and the panel scrolls inside itself; tablet and phone are absent
# deliberately, because below 1024 the whole column scrolls with the document
# and that is the design, not a defect (studio.css, the two max-width blocks).
DESKTOP_SCREENS = {"s01", "s01open", "s01narrow", "s02", "s06",
                   "s08", "s08hover", "s08drag", "s08key"}

# The rail button that is the door to every §08–§10 screen. Identified by the
# accessible name rather than by position, because position is what the rail
# changes: §02 narrows it to three tools and §09 collapses it to one, and a
# gate that reached for the fourth child would follow the rail into being
# wrong rather than notice.
CUT_BUTTON = '.railbtn[aria-label="Cross-section"]'


def check_page_height(page, screen):
    """The specimen's hotspot count must not lengthen the page.

    The info panel renders one structure chip per hotspot, so its height IS
    the content record's size. heart.json going from 2 hotspots to 14 put
    body.scrollHeight at 1942px inside a 900px viewport — the panel stretched
    the grid row, the row stretched .main, and .main stretched an .app whose
    only height rule was a `min-height` floor. Nothing was watching, and the
    next specimen would have stretched it further.
    """
    m = page.eval("window.__st.pageHeight()")
    if not m:
        return ["%s: could not measure the page against the viewport" % screen]
    grew = max(m["body"], m["doc"]) - m["vh"]
    if grew <= 2:
        return []
    return ["%s: the page scrolls — %dpx of content in a %dpx viewport (%dpx "
            "over), with .app measuring %dpx. The panel is stretching the grid "
            "row instead of scrolling inside it: the structure list is one "
            "chip per hotspot, so the page now grows with the specimen and a "
            "40-structure record would draw a 5000px page. .panel and "
            ".panel__scroll already carry the internal scroll — it engages "
            "only when the column above has a definite height, not a "
            "min-height floor (panel__scroll scrolling: %r)."
            % (screen, max(m["body"], m["doc"]), m["vh"], grew, m["appH"],
               m["panelScrolls"])]


def check_meta_integrity(page, screen):
    """The library caption is whole, and wraps between words only.

    Two failure modes, one row. Truncation is what MRB-186's ruling was
    aimed at from the other side: a label column that cannot fit its content
    either splits a word or eats one, and both leave the student reading
    something the record does not say. See metaIntegrity's own comment for
    what this measurement can and cannot see.
    """
    p = []
    metas = page.eval("window.__st.metaIntegrity()") or []
    # Per-caption rows: which string was damaged, and how.
    for m in metas:
        if m["over"] > 0:
            p.append("%s: library caption %r is cut off by %dpx — the "
                     "structure count is the part that goes, and the count is "
                     "what the caption is for (MRB-193). It must wrap, not "
                     "truncate." % (screen, m["text"], m["over"]))
        if m["split"]:
            p.append("%s: library caption %r breaks INSIDE a word — %r. "
                     "MRB-186 ruled a label column never splits a token."
                     % (screen, m["text"], m["split"]))
    # Property rows: ONCE per screen, however many cards carry them. These are
    # a property of one CSS rule, not of eight strings; eight identical lines
    # about `.libcard__meta` would bury the caption that actually broke.
    nowrap = [m for m in metas if m["ws"] == "nowrap"]
    if nowrap:
        p.append("%s: %d of %d library captions are white-space:nowrap, so "
                 "they can only ever truncate — no second line to use "
                 "(.libcard__meta)" % (screen, len(nowrap), len(metas)))
    breaks = sorted({(m["ow"], m["wb"]) for m in metas
                     if m["ow"] != "normal" or m["wb"] != "normal"})
    for ow, wb in breaks:
        p.append("%s: library captions compute overflow-wrap:%s "
                 "word-break:%s — both properties INHERIT, so this may have "
                 "been handed in from an ancestor, and either value licenses "
                 "the mid-word break MRB-186 forbids on the next string long "
                 "enough to need it (.libcard__meta)" % (screen, ow, wb))
    return p


def check_structure(page, screen, counts):
    """Layer B for one driven screen. Returns a list of problems."""
    p = []

    def n(sel):
        return page.eval("window.__st.n(%r)" % sel)

    def need(sel, count=None, label=None):
        got = n(sel)
        want = 1 if count is None else count
        if got != want:
            p.append("%s: expected %d of %s, found %d%s"
                     % (screen, want, sel, got,
                        (" — " + label) if label else ""))

    def absent(sel, label):
        got = n(sel)
        if got:
            p.append("%s: %s must be absent (%s), found %d"
                     % (screen, sel, label, got))

    def hidden(sel, label):
        if page.eval("window.__st.visible(%r)" % sel):
            p.append("%s: %s must be hidden at this width (%s)"
                     % (screen, sel, label))

    if screen == "s01":
        # Harness sanity first: with WebGL absent the probe lands on tier D
        # and every screen silently renders the PAPER stage — a harness
        # fault wearing the costume of a dozen parity defects. The main
        # browser launches with --enable-unsafe-swiftshader precisely so
        # this cannot happen; if it does anyway, say so, loudly and once.
        tier = page.eval(
            "window.__st.q('.app') && "
            "window.__st.q('.app').getAttribute('data-detected-tier')")
        if tier == "D":
            p.append("s01: capability probe landed on tier D — headless "
                     "Chrome has no WebGL despite --enable-unsafe-swiftshader,"
                     " so §01/§02/§04/§05 would all measure the paper stage. "
                     "Harness fault, not app fault.")
            return p
        # Same trap by a different door (MRB-187): the mesh renderer can reach
        # tier A and still fail — a GLB that 404s, a lost context — and the
        # shell answers by routing to the flat stage. Correct behaviour, but
        # it would silently re-point §01–§05 at the paper stage. Name it once.
        mounted = page.eval(
            "window.__st.q('[data-testid=renderer-container]') && "
            "window.__st.q('[data-testid=renderer-container]').dataset.renderer")
        if mounted != "mesh":
            p.append("s01: the mounted renderer is %r, not 'mesh' — the mesh "
                     "renderer failed and the shell routed to the flat stage, "
                     "so §01/§02/§04/§05 would all measure the paper stage."
                     % mounted)
            return p
        # §01: header → crumb strip → library / stage / panel, in order
        need(".topbar .brand")
        need(".topbar__nav span", 3, "Lessons / Practice / 3D Studio")
        need(".topbar__nav .is-here")
        if page.eval("window.__st.text('.topbar__nav .is-here')") != "3D Studio":
            p.append("s01: the current nav item is not '3D Studio'")
        need(".topbar .signin")
        need(".topbar .cta")
        need(".crumbstrip .crumb")
        need(".crumbstrip .modeseg")
        order = page.eval(
            "window.__st.order('.app', ['.topbar', '.crumbstrip', '.main'])")
        if order != "ok":
            p.append("s01: header/crumb/main order broken (%s)" % order)
        order = page.eval(
            "window.__st.order('.main--explore', "
            "['.library', '.stagewrap', '.panel'])")
        if order != "ok":
            p.append("s01: library/stage/panel order broken (%s)" % order)
        cols = page.eval(
            "window.__st.style('.main--explore', 'grid-template-columns')") or ""
        parts = cols.split()
        if len(parts) != 3 or parts[0] != "232px" or parts[2] != "372px":
            p.append("s01: explore grid is %r, reference says 232 / fluid / "
                     "372 with the stage fluid" % cols)
        # library: 1 viewing + 7 soon, divider between (allow-list rule 8)
        need(".libcard", counts["library"])
        need(".libcard.is-viewing")
        need(".libcard.is-soon", counts["soon"])
        need(".library__divider")
        # stage furniture (§01 rail): seven tools = six icon buttons plus
        # the AUTO toggle at the rail foot, exactly as the reference draws
        # them (rotate, zoom, isolate, cross-section, layers, reset + auto)
        need(".rail")
        need(".rail .railbtn", 6, "six icon tools on the desktop rail")
        need(".rail .autorot")
        need(".chip")
        need(".stagehint")
        hint = (page.eval("window.__st.text('.stagehint')") or "").lower()
        if "drag to rotate" not in hint:
            p.append("s01: stage hint %r does not carry the rotate verb" % hint)
        # HOW MANY DOTS IS NOT THE HOTSPOT COUNT, and asserting that it was
        # contradicted the feature. Occlusion is honest (MRB-187): an anchor on
        # the far side reports visible:false and the shell drops its dot. With
        # the two-hotspot placeholder both anchors happened to face the camera,
        # so "one dot per hotspot" held by accident. The acquired heart has
        # fourteen spread over a concave form and shows five to eight at a
        # time — which IS the feature working, and a renderer that always
        # reported visible:true would be the thing that showed all fourteen.
        #
        # What is asserted instead: some are drawn and some are not. The
        # structure-chip row below still holds the panel to one chip per
        # record, so a content record losing hotspots is still caught there.
        drawn = n(".hotspot")
        if not 0 < drawn < counts["hotspots"]:
            p.append("%s: %d of %d hotspot(s) drawn — with honest occlusion a "
                     "concave specimen shows some and hides the rest; all of "
                     "them is a renderer reporting visible:true for "
                     "everything, none of them is a stage with no dots at all"
                     % (screen, drawn, counts["hotspots"]))
        bad = n('.hotspot[data-state="inert"]') + n('.hotspot[data-state="target"]')
        if bad:
            p.append("s01: %d retrieval-state hotspot(s) on the explore "
                     "stage" % bad)
        # panel: chips → name → structures → facts → callouts → actions
        need(".panel .kchip--accent")
        need(".panel__name")
        need(".structchip", counts["hotspots"],
             "one structure chip per hotspot record")
        # first .facts block only — the Record section reuses the class
        # for its provenance rows (allow-list rule 14)
        got_facts = page.eval("window.__st.keyFactRows()")
        if got_facts != counts["facts"]:
            p.append("s01: expected %d key-fact rows, found %d"
                     % (counts["facts"], got_facts))
        need(".matters")
        need(".didyouknow")
        need(".panel__foot .btn--outline")
        need(".panel__foot .btn--primary")

    elif screen == "s01narrow":
        # The same open callout on the NARROWEST desktop the layout supports.
        # The reference's 232 / fluid / 372 grid leaves a 308px stage at 1024,
        # so a 216px card placed at dot + 90px unconditionally — what Stage 1
        # did, and what MRB-187 found by hand — runs off the edge. At 1440 the
        # stage is 724px and the same defect fits on screen, which is why this
        # screen exists at all.
        need(".callout", 1)
        # No leader here, and that is correct: with neither side able to take
        # the card it is pinned to the stage's right edge, and a leader to a
        # card that is not beside the dot would be a line to nowhere.
        over = page.eval("window.__st.overflow('.callout', '.stage')")
        if not over:
            p.append("s01narrow: could not measure the callout against the stage")
        elif any(v > 0.5 for v in over.values()):
            p.append("s01narrow: the callout hangs off the stage by %r — a "
                     "label clipped at the stage edge is a label the student "
                     "cannot read" % {k: round(v) for k, v in over.items() if v > 0.5})
        # and it still clears the tool rail rather than burying it
        rail = page.eval("window.__st.rect('.rail')")
        card = page.eval("window.__st.rect('.callout')")
        if rail and card and card["x"] < rail["x"] + rail["w"]:
            p.append("s01narrow: the callout (x=%.0f) overlaps the tool rail "
                     "(ends at %.0f)" % (card["x"], rail["x"] + rail["w"]))

    elif screen == "s01open":
        # §01 OPEN LABEL: "Dot grows to 38px and inverts to cream fill. One
        # callout at a time; leader line keeps the link explicit."
        need(".callout", 1, "one callout at a time")
        need(".callout__title")
        need(".callout__detail")
        need(".leader", 1, "the leader line keeps the link explicit")
        need('.hotspot[data-state="open"]', 1)
        need(".structchip.is-open", 1,
             "the panel chip and the stage dot are one selection")
        # the panel heading and the callout title are the same string from the
        # same field (spec §3.2) — this is the liver/lungs/"Hepar" defect
        chip = page.eval("window.__st.text('.structchip.is-open .structchip__label')")
        title = page.eval("window.__st.text('.callout__title')")
        if chip != title:
            p.append("s01open: the panel chip says %r and the callout says %r "
                     "— two lookups of one field" % (chip, title))
        # AND it stays on the stage. The defect this screen exists for.
        over = page.eval("window.__st.overflow('.callout', '.stage')")
        if not over:
            p.append("s01open: could not measure the callout against the stage")
        elif any(v > 0.5 for v in over.values()):
            p.append("s01open: the callout hangs off the stage by %r — a label "
                     "clipped at the stage edge is a label the student cannot "
                     "read" % {k: round(v) for k, v in over.items() if v > 0.5})

    elif screen == "s02":
        # §02: the room inverts — library removed, not dimmed
        absent(".library", "library is removed in retrieval")
        absent(".crumbstrip", "crumb strip is removed in retrieval")
        need(".hatch")
        need(".endround")
        need(".rpanel")
        cols = page.eval(
            "window.__st.style('.main--retrieve', 'grid-template-columns')") or ""
        parts = cols.split()
        if len(parts) != 2 or parts[1] != "404px":
            p.append("s02: retrieve grid is %r, reference says fluid / 404" % cols)
        need(".rpanel__round")
        need(".rpanel__of")
        need(".psq", REFERENCE_ROUND_SQUARES,
             "Design drew six squares; a round is six (MRB-191)")
        need(".psq--current")
        absent(".psq--done", "round starts at minute zero (allow-list rule 13)")
        need(".rpanel__ask")
        need(".rinput input")
        need(".rbtn-check")
        need(".rbtn-skip")
        need(".rreveal__link")
        need(".rmissed")
        # the stage: one target with a ping, everything else inert
        need('.hotspot[data-state="target"]')
        need(".hotspot__ping")
        # Every OTHER dot that is drawn is inert — not every other hotspot.
        # Same reason as s01: occlusion drops the ones facing away, so the
        # count is what the camera can see minus the target, and the claim
        # worth making is that nothing else is wearing the target's treatment.
        inert = n('.hotspot[data-state="inert"]')
        if inert != n(".hotspot") - n('.hotspot[data-state="target"]'):
            p.append("s02: %d inert of %d drawn hotspot(s) — every dot that is "
                     "not the target must drop to an inert outline"
                     % (inert, n(".hotspot")))
        bad = n('.hotspot[data-state="closed"]') + n('.hotspot[data-state="open"]')
        if bad:
            p.append("s02: %d labelled hotspot(s) survive into retrieval" % bad)

    elif screen == "s04":
        # §04: library becomes a drawer; panel flows under the stage
        need(".libtrigger")
        if "specimens" not in (page.eval(
                "window.__st.text('.libtrigger')") or "").lower():
            p.append("s04: the drawer trigger does not say Specimens")
        hidden(".topbar__nav", "site nav leaves at tablet")
        absent(".crumbstrip", "crumb strip leaves at tablet")
        hidden(".library", "library column becomes the drawer")
        need(".tpanel")
        need(".tpanel__actions .btn--outline")
        need(".tpanel__actions .btn--primary")
        need(".tpanel__cols")
        need(".rail .railbtn", 6, "tablet keeps all seven tools (6 + auto)")
        need(".rail .autorot")
        absent(".drawer", "drawer is closed by default")

    elif screen == "s04drawer":
        need(".scrim")
        need(".drawer")
        need(".drawer__close")
        need(".drawer .libcard--big", counts["library"])
        # scrim carries the reconciled ink at 42% (§04 annotation)
        scrim = page.eval("window.__st.style('.scrim', 'background-color')")
        got = parse_rgba(scrim or "")
        if not got or got[0] != (26, 23, 20) or abs(got[1] - 0.42) > 0.01:
            p.append("s04drawer: scrim is %r, expected reconciled ink at "
                     "0.42 (rgba(26, 23, 20, 0.42))" % scrim)

    elif screen == "s05":
        need(".libtrigger--square")
        need(".topbar .brand")
        need(".signin")
        need(".sheet")
        need(".sheet__grab .sheet__handle")
        need(".sheet__foot .lessonglyph")
        need(".sheet__foot .btn--primary")
        absent(".sheet.is-raised", "sheet rests by default")
        rail_dir = page.eval("window.__st.style('.rail', 'flex-direction')")
        if rail_dir != "row":
            p.append("s05: the rail is %r, reference says it goes horizontal "
                     "at the stage foot" % rail_dir)
        chip_top = page.eval("window.__st.style('.chip', 'top')")
        if close_length(chip_top, "12px") is not True:
            p.append("s05: quality chip sits at top %r, reference pins it to "
                     "the stage top on phone (12px)" % chip_top)

    elif screen == "s05raised":
        need(".sheet.is-raised")
        # the stage never fully leaves: 150pt keeps the model in context
        h = page.eval("window.__st.style('.sheet.is-raised', 'height')")
        try:
            sheet_h = float((h or "0px").replace("px", ""))
        except ValueError:
            sheet_h = 0.0
        viewport_h = page.eval("window.innerHeight")
        stage_kept = viewport_h - 52 - sheet_h  # 52px phone topbar
        if not 130 <= stage_kept <= 170:
            p.append("s05raised: raised sheet leaves %.0fpx of stage, "
                     "reference says 150" % stage_kept)
        # §05 B: the specimen name replaces the brand once the sheet raises
        title = page.eval("window.__st.text('.topbar .brand')")
        if title == "MrBadmusAI":
            p.append("s05raised: top bar still shows the brand; the raised "
                     "sheet swaps it for the specimen name (§05 B)")

    elif screen == "s05lib":
        need(".phonelib")
        need(".phonelib__close")
        need(".phonelib .libcard--big", counts["library"])
        need(".phonelib__foot")
        # full-screen, not a half sheet (§05 annotation)
        w = page.eval("window.__st.style('.phonelib', 'width')")
        if close_length(w, "390px") is not True:
            p.append("s05lib: phone library width %r is not full-screen" % w)

    elif screen == "s06":
        tier = page.eval(
            "window.__st.q('.app') && "
            "window.__st.q('.app').getAttribute('data-detected-tier')")
        if tier != "D":
            p.append("s06: detected tier is %r — WebGL was not actually "
                     "disabled, so the flat stage was never exercised" % tier)
        need(".stage--paper")
        # See the note on the "plate outline" style row: these are the flat
        # renderer's elements now, not the placeholder's.
        need(".plate-grid")
        need(".plate")
        need(".plate__image")
        need(".flatchip")
        word = (page.eval("window.__st.text('.flatchip__word')") or "").lower()
        if word != "flat diagram":
            p.append("s06: flat chip says %r, not FLAT DIAGRAM" % word)
        # §06: four tools — zoom, isolate, labels, reset. No auto-rotate,
        # no quality chip (no renderer ⇒ no tier).
        need(".rail .railbtn", 4, "flat rail is four tools")
        absent(".rail .autorot", "auto-rotate is absent on the flat stage")
        absent(".chip", "no quality chip without a renderer")
        hint = (page.eval("window.__st.text('.stagehint')") or "").lower()
        if "rotate" in hint:
            p.append("s06: hint %r promises rotation on a flat plate" % hint)
        need(".hotspot", counts["hotspots"])

    elif screen == "s08":
        # §08/§09 desktop, the cut engaged and the slider untouched. The
        # plate exists only while the tool does — "Only shown while the tool
        # is on" — so every row here is downstream of a real press on the
        # rail, which is how the screen is driven.
        need(".secplate")
        # §09: "The rotate hint at bottom centre yields to the plate — one
        # thing lives on that edge at a time." Two captions stacked on one
        # edge is the defect this forbids, and it is a rule about the EDGE,
        # not about the hint: whichever of them is drawn, the other is not.
        absent(".stagehint", "the rotate hint yields to the plate (§09)")
        need(CUT_BUTTON + ".is-active", 1,
             "the rail says which tool is running")
        # The rail yields the bar on PHONE and nowhere else (§09). A desktop
        # that collapsed would be answering a phone's problem with a
        # desktop's room.
        need(".rail .railbtn", 6, "desktop keeps all six icon tools")
        need(".chip", 1, "the quality chip keeps its corner")
        stage = page.eval("window.__st.rect('.stage')")
        plate = page.eval("window.__st.rect('.secplate')")
        chip = page.eval("window.__st.rect('.chip')")
        if not stage or not plate:
            p.append("s08: could not measure the plate against the stage")
        else:
            off = abs((plate["x"] + plate["w"] / 2.0)
                      - (stage["x"] + stage["w"] / 2.0))
            if off > 2:
                p.append("s08: the plate's centre is %.0fpx off the stage's "
                         "— §09 says PLATE 392×44 · BOTTOM CENTRE, and the "
                         "plate centres on the stage until the tablet moves "
                         "it off centre to clear the rail" % off)
        # Both of them live on the bottom edge of the stage, and the
        # reference draws them clear of one another. A plate wide enough to
        # reach the chip would bury the one control §07 calls "deliberately
        # the quietest element on the stage".
        if plate and chip and plate["x"] + plate["w"] > chip["x"]:
            p.append("s08: the plate ends at x=%.0f and the quality chip "
                     "starts at x=%.0f — they overlap on the bottom edge"
                     % (plate["x"] + plate["w"], chip["x"]))

    elif screen == "s08hover":
        # This screen exists only to resolve §10's hover row, which is a CSS
        # `:hover` and therefore an answer only the engine can give. Assert
        # the pointer actually landed: without this, a harness that missed
        # the plate would report the hover row as a colour drift, and a
        # colour drift is the one thing it would not be.
        need(".secplate")
        if not page.eval("!!document.querySelector('.secplate:hover')"):
            p.append("s08hover: the pointer is not over the plate — §10's "
                     "hover row would measure the resting state and blame "
                     "the stylesheet for a harness fault")

    elif screen == "s08drag":
        # §10's third state, reached the way a student reaches it: a real
        # pointerdown on the real control. `data-drag` is React's answer to
        # an event it actually received, so nothing short of a dispatched
        # pointer event puts the plate here.
        need(".secplate[data-drag]", 1,
             "a real press on the input puts the plate in its drag state")

    elif screen == "s08key":
        # §10's fourth state: "ARROWS STEP 2%, NOTCHED HANDLE". Drawn,
        # therefore required — and required as BEHAVIOUR, not only as
        # treatment, which is why the step is counted rather than the notch
        # merely being looked at. A native range input carries the stepping,
        # so this is also the row that would notice the drawn parts being
        # laid over something that is no longer a range input.
        need(".secplate[data-key]", 1,
             "arrow keys on a focused plate raise the keyboard state")
        was = page.eval("window.__stKeyFrom")
        now = page.eval("document.querySelector('.secplate') && Number("
                        "document.querySelector('.secplate')"
                        ".getAttribute('data-percent'))")
        if was is None or now is None:
            p.append("s08key: could not read the plate's percentage before "
                     "and after the arrows")
        elif now - was != 6:
            p.append("s08key: three ArrowRights moved the cut from %s%% to "
                     "%s%%, a step of %s — §10 says ARROWS STEP 2%%, so "
                     "three of them is 6" % (was, now, now - was))

    elif screen == "s09t":
        # §09 TABLET: "Same plate, narrower, and no longer centred on the
        # stage — it centres on the space left of the rail so the two never
        # touch." The rail is still the vertical desktop rail here (§04: a
        # tablet has the room and often is the teacher's device), so the
        # clearance is horizontal and the number Design gives it is 16.
        need(".secplate")
        absent(".rail[data-collapsed]",
               "the rail yields the bar on phone, not on tablet")
        plate = page.eval("window.__st.rect('.secplate')")
        rail = page.eval("window.__st.rect('.rail')")
        if not plate or not rail:
            p.append("s09t: could not measure the plate against the rail")
        else:
            if abs(plate["w"] - 320) > 1 or abs(plate["h"] - 44) > 1:
                p.append("s09t: the plate renders %.0f×%.0f, §09 says PLATE "
                         "320×44 — height stays 44 because it is now a touch "
                         "target" % (plate["w"], plate["h"]))
            gap = plate["x"] - (rail["x"] + rail["w"])
            if gap < 16:
                p.append("s09t: the plate leaves %.0fpx between itself and "
                         "the rail; §10's own summary line says gap to rail "
                         "16, and below that the two read as one control"
                         % gap)

    elif screen == "s09p":
        # §09 PHONE: "THE RAIL YIELDS, IT DOES NOT STACK. Both want the
        # bottom edge and there is room for one."
        need(".rail[data-collapsed]", 1,
             "turning the cut on collapses the rail")
        need(".rail .railbtn", 1,
             "collapsed to the single tool that is running (§09)")
        need(".rail .railbtn.is-active", 1,
             "and the one that is left is the one that is running")
        need(".secplate")
        # "the slider pill … carries no SECTION eyebrow" — on a shared bar
        # the width belongs to the track, and the label is what goes.
        absent(".secplate__word",
               "the eyebrow goes on phone; the width belongs to the track")
        plate = page.eval("window.__st.rect('.secplate')")
        btn = page.eval("window.__st.rect('.rail .railbtn')")
        if not plate or not btn:
            p.append("s09p: could not measure the plate against the rail")
        else:
            # ONE bar means one row: the two sit on the same centre line.
            drift = abs((plate["y"] + plate["h"] / 2.0)
                        - (btn["y"] + btn["h"] / 2.0))
            if drift > 4:
                p.append("s09p: the plate's centre line is %.0fpx off the "
                         "rail button's — §09 draws them sharing one bar, "
                         "and two centre lines is the second row it forbids"
                         % drift)
            if plate["x"] < btn["x"] + btn["w"] and btn["x"] < plate["x"] + plate["w"]:
                p.append("s09p: the plate (x %.0f–%.0f) and the rail button "
                         "(x %.0f–%.0f) overlap — they share the bar side by "
                         "side, not stacked"
                         % (plate["x"], plate["x"] + plate["w"],
                            btn["x"], btn["x"] + btn["w"]))
        # "Nothing scrolls behind a thumb, the stage keeps its height, and
        # the bar never gains a second row." The stage height is measured
        # BEFORE the tool is pressed and again after: a bar that took its
        # room from the stage would satisfy every other row on this screen.
        before = page.eval("window.__stStageH0")
        after = plate and page.eval("window.__st.rect('.stage')")
        if before is None or not after:
            p.append("s09p: could not measure the stage either side of the "
                     "cut being engaged")
        elif abs(after["h"] - before) > 1:
            p.append("s09p: engaging the cut moved the stage from %.0fpx to "
                     "%.0fpx tall — §09 is explicit that the stage keeps its "
                     "height, because the bar is shared rather than added"
                     % (before, after["h"]))

    elif screen == "s09pdrag":
        # §09: "The readout cannot stay in the bar — a thumb covers it. It
        # lifts to the top-left corner of the stage, opposite the quality
        # chip, and only while dragging."
        need(".secreadout", 1, "the readout lifts out of the bar")
        absent(".secplate__value",
               "and it is not still in the bar under the thumb")
        stage = page.eval("window.__st.rect('.stage')")
        readout = page.eval("window.__st.rect('.secreadout')")
        chip = page.eval("window.__st.rect('.chip')")
        if not stage or not readout:
            p.append("s09pdrag: could not measure the readout against the "
                     "stage")
        else:
            dx = readout["x"] - stage["x"]
            dy = readout["y"] - stage["y"]
            if dx > 16 or dy > 16:
                p.append("s09pdrag: the lifted readout sits %.0fpx from the "
                         "stage's left edge and %.0fpx from its top — §09 "
                         "puts it in the top-left corner" % (dx, dy))
            # OPPOSITE the quality chip, which is the whole reason it lifts
            # to that corner rather than the nearest free one: the two are
            # the only things on the stage's top edge, and a student holding
            # the phone must be able to read both at once.
            if chip:
                mid = stage["x"] + stage["w"] / 2.0
                if not (readout["x"] + readout["w"] / 2.0 < mid < chip["x"]
                        + chip["w"] / 2.0):
                    p.append("s09pdrag: the readout and the quality chip are "
                             "not on opposite sides of the stage — readout "
                             "centred at x=%.0f, chip at x=%.0f, stage "
                             "midline %.0f"
                             % (readout["x"] + readout["w"] / 2.0,
                                chip["x"] + chip["w"] / 2.0, mid))

    # ── every screen: the two ways a growing record deforms the shell ─────
    # Both arrived with heart.json going from 2 hotspots to 14, and neither
    # had anything watching it. Deliberately outside the per-screen branches
    # above, for the same reason the mid-word sweep is: a rule that only runs
    # where somebody remembered to list it is a rule with holes.
    if screen in DESKTOP_SCREENS:
        p.extend(check_page_height(page, screen))
    p.extend(check_meta_integrity(page, screen))

    # ── every screen, every breakpoint: nothing breaks inside a word ──────
    # Deliberately not scoped to a selector list. The defect this exists for
    # (MRB-186) was in a block no row mentioned, so a gate that only watches
    # the selectors somebody remembered would have missed it in exactly the
    # same way. It runs on all eight driven screens, which is what makes it a
    # breakpoint sweep rather than a desktop check.
    for hit in page.eval("window.__st.midWordBreaks()") or []:
        p.append("%s: text breaks mid-word in %s — %r (the label column is too "
                 "narrow for its content, or the element is wrapping with "
                 "overflow-wrap:anywhere as a flex item)"
                 % (screen, hit["sel"], hit["split"]))

    return p


# ── the driver ───────────────────────────────────────────────────────────

SCREENS = ["s01", "s01open", "s01narrow", "s02", "s04", "s04drawer", "s05",
           "s05raised", "s05lib", "s06",
           "s08", "s08hover", "s08drag", "s08key", "s09t", "s09p", "s09pdrag"]


def _mouse(page, sel, kind):
    """Dispatch a real mouse event at the centre of `sel`.

    Every other screen's door is `element.click()`, which is enough when the
    thing being opened is a handler. §10's states are not handlers: `:hover`
    is the engine's own answer to where the pointer is, and `[data-drag]` is
    React's answer to a pointer event it actually received. Neither can be
    reached by calling a method on an element, so these go through the input
    pipeline instead. Returns the rect it aimed at, or None.
    """
    r = page.eval("window.__st.rect(%r)" % sel)
    if not r:
        return None
    params = {"type": kind, "pointerType": "mouse",
              "x": r["x"] + r["w"] / 2.0, "y": r["y"] + r["h"] / 2.0}
    if kind == "mouseMoved":
        params.update(button="none", buttons=0)
    else:
        params.update(button="left", clickCount=1,
                      buttons=1 if kind == "mousePressed" else 0)
    page.send("Input.dispatchMouseEvent", params)
    return r


def _key(page, key, code, vk):
    """One real key press and release, through the input pipeline.

    rawKeyDown rather than keyDown: the range input steps on the key event
    itself, and rawKeyDown is the one that does not also generate a char
    event for a control that has no text to take it.
    """
    for kind in ("rawKeyDown", "keyUp"):
        page.send("Input.dispatchKeyEvent",
                  {"type": kind, "key": key, "code": code,
                   "windowsVirtualKeyCode": vk, "nativeVirtualKeyCode": vk})


def _engage_cut(page, timeout=6.0):
    """Press the rail's cross-section button and wait for the plate.

    Pressed, not simulated. The plate is rendered only while the RENDERER
    reports the tool active (§09: "Only shown while the tool is on"), so a
    harness that set a class or forced a state would be measuring markup no
    student can reach — and would keep passing after the tool stopped
    engaging at all, which is the one failure worth catching here.
    """
    import time
    page.eval(_JS + "window.__st.click(%r)" % CUT_BUTTON)
    deadline = time.time() + timeout
    while time.time() < deadline:
        if page.eval("window.__st.n('.secplate')"):
            return True
        time.sleep(0.05)
    return False


def _sanity(page, screen, tokens):
    """The stylesheet applied AND the dist is fresh: the resolved ink token
    must equal the token file's. A stale dist otherwise wears the costume of
    a hundred parity defects (see ks3_parity's docstring on this)."""
    resolved = page.eval(
        "getComputedStyle(document.body).getPropertyValue('--st-ink').trim()")
    if not resolved:
        return ("%s: STYLESHEET DID NOT APPLY — no --st-ink on body; every "
                "measurement would be meaningless, page skipped" % screen)
    if parse_rgb(resolved) != parse_rgb(tokens["--st-ink"]):
        return ("%s: dist resolves --st-ink to %s but tokens.css says %s — "
                "the built app is STALE; run `npm run build` in 3d-studio/ "
                "and re-run this gate" % (screen, resolved, tokens["--st-ink"]))
    return None


def _check_styles(page, screen, style_rows, problems):
    for spec in [c for c in COMPONENTS if c["on"] == screen]:
        sel = spec["sel"]
        if not page.eval("!!window.__st.q(%r)" % sel):
            problems.append("PARITY: %s — selector %s not present on %s"
                            % (spec["name"], sel, screen))
            continue
        for prop, want in sorted(spec["props"].items()):
            got = (page.eval("window.__st.style(%r, %r)" % (sel, prop)) or "").strip()
            if prop == "font-family":
                ok = want.lower() in got.lower()
            elif want.startswith("#"):
                ok = same_colour(got, want)
            elif want.endswith("px"):
                ok = close_length(got, want) is True
            else:
                ok = got.lower() == want.lower()
            style_rows.append((screen, spec["name"], prop, want, got, ok))
            if not ok:
                problems.append("PARITY: %s — %s expected %s, resolved %s "
                                "(%s on %s)" % (spec["name"], prop, want,
                                                got or "<empty>", sel, screen))


def _console(page, screen, problems):
    for e in page.console_errors():
        if "favicon" in e.lower():
            continue
        problems.append("console error on %s: %s" % (screen, e))


def _settle(page, seconds=0.35):
    import time
    time.sleep(seconds)


def _await_stage(page, timeout=25.0):
    """Wait until the mounted renderer has finished loading.

    Stage 1's renderers drew synchronously, so a fixed settle was enough to
    measure them. The mesh renderer fetches a Draco-compressed GLB over HTTP
    (MRB-187), and the hotspot layer does not exist until that resolves — so a
    fixed sleep turns this gate into a race whose failure mode is a handful of
    missing hotspots rather than an honest "the stage was still loading".

    Both renderers publish their state on the stage container, so this waits
    on the app rather than on the clock. A renderer that reports 'failed' is
    not waited out: the shell answers a failure by mounting a different
    renderer, which will report 'ready' in its turn, and s01 asserts which one
    ended up mounted.
    """
    import time
    deadline = time.time() + timeout
    state = None
    while time.time() < deadline:
        state = page.eval(
            "(() => { const el = document.querySelector("
            "'[data-testid=renderer-container]');"
            " return el ? (el.dataset.state || 'none') : 'no-container' })()")
        if state == "ready":
            return state
        time.sleep(0.1)
    return state or "timeout"


def _await_fonts(page, timeout=10.0):
    """Wait for the webfonts, because two rows now measure LINE BOXES.

    Where the text wraps, and whether it fits its column at all, are answers
    in the shipped font's metrics. Measured against the fallback they are
    answers about a font the student never sees — and the failure mode is the
    worst kind: a caption that fits in Helvetica and truncates in DM Mono
    would pass this gate every time. Failed font loads settle too, so this
    cannot hang on a 404.
    """
    import time
    deadline = time.time() + timeout
    while time.time() < deadline:
        if page.eval("document.fonts && document.fonts.status") == "loaded":
            return True
        time.sleep(0.05)
    return False


def run_browser_layers(url, tokens, counts):
    problems, style_rows = [], []
    checked = []
    blocked = []

    def visit(page, screen):
        page.eval(_JS + "true")
        if not _await_fonts(page):
            problems.append(
                "%s: the webfonts never settled — every line-box measurement "
                "on this screen would be about the fallback font, not the "
                "shipped one" % screen)
        state = _await_stage(page)
        if state != "ready":
            # The one sanctioned exception — see plate_blocker(). Narrow on
            # purpose: this screen only, this state only, and only while the
            # record itself says the asset has not been acquired.
            reason = plate_blocker() if screen == "s06" and state == "failed" else None
            if reason:
                blocked.append((screen, reason))
                return False
            problems.append(
                "%s: the renderer never reached ready (state=%r) — the stage "
                "would have been measured mid-load" % (screen, state))
            return False
        sane = _sanity(page, screen, tokens)
        if sane:
            problems.append(sane)
            return False
        checked.append(screen)
        problems.extend(check_structure(page, screen, counts))
        _check_styles(page, screen, style_rows, problems)
        _console(page, screen, problems)
        return True

    # --enable-unsafe-swiftshader: headless Chrome's default launch has no
    # WebGL at all, which lands the capability probe on tier D and swaps
    # every stage for the paper fallback. Software WebGL keeps the probe
    # honest for §01–§05; §06 then disables it deliberately.
    with cdp.Browser(extra_args=["--enable-unsafe-swiftshader"]) as b:
        page = b.attach()

        # §01 desktop exploration
        page.set_viewport(1440, 900)
        page.goto(url)
        if visit(page, "s01"):
            # §02 — the mode toggle is the door (reference: header control)
            page.eval(_JS + "window.__st.click('.modeseg button:nth-child(2)')")
            _settle(page)
            visit(page, "s02")

        # §01 with a structure open. Driven through the panel's own structure
        # chip, because that is the path a student takes and the only one that
        # puts BOTH the chip and the stage dot into their open state from one
        # action. Carried forward from Stage 2: the harness never opened a
        # callout, which is how a clipping defect survived it.
        page.set_viewport(1440, 900)
        page.goto(url)
        page.eval(_JS + "true")
        _await_stage(page)
        page.eval(_JS + "window.__st.click('.structchip')")
        _settle(page)
        visit(page, "s01open")

        # And again at the NARROWEST desktop the layout supports (1024, where
        # §04's landscape note says the three-column layout returns), which is
        # where the clipping actually bites. See the screen's own note.
        page.set_viewport(1024, 900)
        page.goto(url)
        page.eval(_JS + "true")
        _await_stage(page)
        page.eval(_JS + "window.__st.click('.structchip')")
        _settle(page)
        visit(page, "s01narrow")

        # §04 tablet — fresh navigation at the tablet width
        page.set_viewport(834, 1042)
        page.goto(url)
        if visit(page, "s04"):
            page.eval(_JS + "window.__st.click('.libtrigger')")
            _settle(page)
            visit(page, "s04drawer")

        # §05 phone
        page.set_viewport(390, 844)
        page.goto(url)
        if visit(page, "s05"):
            page.eval(_JS + "window.__st.click('.sheet__grab')")
            _settle(page)
            visit(page, "s05raised")
            page.eval(_JS + "window.__st.click('.sheet__grab')")
            _settle(page)
            page.eval(_JS + "window.__st.click('.libtrigger--square')")
            _settle(page)
            visit(page, "s05lib")

        # ── §08–§10, the cut engaged ─────────────────────────────────────
        # Every screen below starts by pressing the cross-section tool,
        # because the plate and the plane rule exist only while the tool
        # does. Desktop first: the plate at rest, then the three states §10
        # draws that a stylesheet will only enter for a real pointer and a
        # real keyboard.
        page.set_viewport(1440, 900)
        page.goto(url)
        page.eval(_JS + "true")
        _await_stage(page)
        if not _engage_cut(page):
            problems.append(
                "s08: pressing the rail's cross-section button never brought "
                "up the plate — §08, §09 and §10 are all downstream of that "
                "one control, so none of them could be measured")
        else:
            visit(page, "s08")
            _mouse(page, ".secplate", "mouseMoved")
            _settle(page)
            visit(page, "s08hover")
            _mouse(page, ".secplate__input", "mousePressed")
            _settle(page)
            visit(page, "s08drag")
            _mouse(page, ".secplate__input", "mouseReleased")
            _settle(page)
            # The keyboard state is `:focus-visible`, not `:focus` — §10
            # draws the pointer and the keyboard as two states, and a press
            # must not raise the ring. So the press above has to be undone as
            # a MODE, not just as a focus: Tab is what tells the engine the
            # person has moved to the keyboard, and the focus that follows it
            # is the one that shows a ring. Without it the plate would sit in
            # its resting state and the row would blame the stylesheet.
            page.eval("document.activeElement && document.activeElement.blur()")
            _key(page, "Tab", "Tab", 9)
            _settle(page, 0.15)
            page.eval("document.querySelector('.secplate__input').focus()")
            _settle(page)
            page.eval("window.__stKeyFrom = Number(document.querySelector("
                      "'.secplate').getAttribute('data-percent'))")
            for _ in range(3):
                _key(page, "ArrowRight", "ArrowRight", 39)
                _settle(page, 0.1)
            visit(page, "s08key")

        # §09 tablet — the plate stops centring on the stage and centres on
        # the space left of the rail instead.
        page.set_viewport(834, 1042)
        page.goto(url)
        page.eval(_JS + "true")
        _await_stage(page)
        if _engage_cut(page):
            visit(page, "s09t")

        # §09 phone — ONE BAR, SHARED WITH THE RAIL. The stage is measured
        # before the tool is pressed, because the claim the reference makes
        # loudest here is about what does NOT change.
        page.set_viewport(390, 844)
        page.goto(url)
        page.eval(_JS + "true")
        _await_stage(page)
        page.eval("window.__stStageH0 = document.querySelector('.stage')"
                  " ? document.querySelector('.stage')"
                  ".getBoundingClientRect().height : null")
        if _engage_cut(page):
            visit(page, "s09p")
            _mouse(page, ".secplate__input", "mousePressed")
            _settle(page)
            visit(page, "s09pdrag")
            _mouse(page, ".secplate__input", "mouseReleased")

    # §06 — a separate Chrome with WebGL off, so the REAL capability probe
    # lands on tier D and the paper stage is exercised end to end.
    with cdp.Browser(extra_args=["--disable-webgl", "--disable-webgl2"]) as b:
        page = b.attach()
        page.set_viewport(1440, 900)
        page.goto(url)
        visit(page, "s06")

    return problems, style_rows, checked, blocked


def dist_staleness():
    """The newest file under src/ or content/, when it is newer than the build.

    Returns (path, seconds_ahead) or None.

    FATAL, not a note — ruled on MRB-191. `npm run build` is `tsc && vite
    build`, so a type error aborts BEFORE Vite writes anything and leaves
    dist/ holding the PREVIOUS build. Every screen this gate then drives
    measures code that is not running, and the gate reports green about it.
    That is worse than having no gate: it converts a build failure into a
    false pass, and a false pass is believed. It cost the overnight session
    an hour while it was still only a warning.
    """
    index = os.path.join(DIST, "index.html")
    if not os.path.exists(index):
        return None
    built = os.path.getmtime(index)
    newest, newest_at = None, 0.0
    for root in (os.path.join(APP, "src"), os.path.join(APP, "content")):
        for dirpath, _dirs, files in os.walk(root):
            for f in files:
                path = os.path.join(dirpath, f)
                try:
                    mtime = os.path.getmtime(path)
                except OSError:
                    continue
                if mtime > newest_at:
                    newest, newest_at = path, mtime
    if newest and newest_at > built:
        return newest, newest_at - built
    return None


def refuse_if_stale(gate):
    """Print the refusal and return True when the build cannot be trusted."""
    if not os.path.isdir(DIST) or not os.path.exists(
            os.path.join(DIST, "index.html")):
        print("FAIL: no built app at %s — run `npm run build` in 3d-studio/"
              % os.path.relpath(DIST, HERE))
        print("NO RESULTS — nothing was measured.")
        return True
    stale = dist_staleness()
    if stale:
        newest, behind = stale
        print("FAIL: the built app is STALE. %s is %.0fs newer than dist/."
              % (os.path.relpath(newest, HERE), behind))
        print("      `npm run build` is `tsc && vite build` — a type error "
              "aborts before Vite writes, so dist/ keeps the previous build "
              "and this gate would measure code that is not running.")
        print("      %s refuses rather than report green about it (MRB-191)."
              % gate)
        print("      Run `npm run build` in 3d-studio/ and re-run. If the "
              "build fails, THAT is the defect this was hiding.")
        print("NO RESULTS — nothing was measured.")
        return True
    return False


def main():
    print("3D Studio parity gate — references: %s"
          % ", ".join(os.path.relpath(p, HERE) for p in REFERENCE))

    # Before anything is measured, and before layer A prints a single note:
    # a refusal that still emitted partial results would be read as results.
    if refuse_if_stale("The parity gate"):
        return 1

    tokens = studio_tokens()
    counts = _content_counts()

    # layer A
    a_problems, a_notes = check_provenance()
    for note in a_notes:
        print("  A: " + note)

    # serve dist under /3d/ so the app's absolute asset URLs resolve
    #
    # ⊕ MRB-270. `root` was never removed — not on failure, not on success. One
    # abandoned directory a run is small, but it is the same class of defect
    # that filled the volume on 19 Aug, and the fix is the same: put it under
    # the named gate root and remove it in a `finally`. The symlink is unlinked
    # BY HAND first: the real dist/ is on the other end of it and must never be
    # within reach of a recursive delete.
    root = tempfile.mkdtemp(prefix="st-parity-", dir=cdp.gate_tmp())
    link = os.path.join(root, "3d")
    os.symlink(DIST, link)
    server, port = cdp.serve(root)
    try:
        url = "http://127.0.0.1:%d/3d/" % port
        b_problems, style_rows, checked, blocked = run_browser_layers(
            url, tokens, counts)
    finally:
        server.shutdown()
        if os.path.islink(link):
            os.unlink(link)
        shutil.rmtree(root, ignore_errors=True)

    ok_rows = sum(1 for r in style_rows if r[5])
    print("  B: screens driven: %s" % ", ".join(checked))
    print("  C: %d/%d style expectations hold" % (ok_rows, len(style_rows)))

    problems = a_problems + b_problems
    if blocked:
        # Loud, and above the verdict rather than below it: a blocked screen is
        # coverage this gate is NOT providing, and the moment that reads as
        # ordinary the gate has quietly shrunk.
        print("\n%d screen(s) BLOCKED — not measured, not passed:" % len(blocked))
        for screen, reason in blocked:
            print("  ⊘ %s: %s" % (screen, reason))
    if problems:
        print("\n%d problem(s):" % len(problems))
        for pr in problems:
            print("  ✗ " + pr)
        return 1
    print("PARITY PASS — %d screens, %d style rows, %d tokens provenanced%s"
          % (len(checked), len(style_rows), len(studio_tokens()),
             ("  ·  %d screen(s) BLOCKED, see above" % len(blocked))
             if blocked else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
