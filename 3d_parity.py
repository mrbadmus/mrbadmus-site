#!/usr/bin/env python3
"""3d_parity.py — the MRB-186 visual parity gate for the 3D Studio shell.

Design's reference is frozen at ``3d-studio/reference/shell-v1.html``. Stage 1
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
     declares must appear literally in the frozen reference — you cannot
     invent a colour Design never specified, or drift a hex by one digit,
     without the build failing. The seven MRB-186 reconciled values are the
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
     drawer, the phone sheet detents, the flat stage's reduced rail.

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
  14.  The panel's "Record" provenance section (six .fact rows: system,
       spec points, renderer, licence, source, acquired) has no drawn slot
       in the reference — a Stage 1 acceptance addition (every record field
       rendered). The key-facts count is therefore asserted on the FIRST
       .facts block only.
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

Provenance for every value in the expectation tables below is the frozen
reference itself — section and line cited in each screen's comment.
"""

from __future__ import annotations

import json
import os
import re
import sys
import tempfile

import ks3_browser as cdp
from ks3_parity import close_length, parse_rgb, parse_rgba, same_colour

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(HERE, "3d-studio")
TOKENS_CSS = os.path.join(APP, "src", "styles", "tokens.css")
REFERENCE = os.path.join(APP, "reference", "shell-v1.html")
DIST = os.path.join(APP, "dist")
HEART = os.path.join(APP, "content", "heart.json")

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


def check_provenance():
    """Layer A. Returns (problems, notes)."""
    problems, notes = [], []
    if not os.path.exists(REFERENCE):
        return (["frozen reference missing: %s" % REFERENCE], notes)
    with open(REFERENCE, encoding="utf-8", errors="replace") as fh:
        ref = fh.read().lower()

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
        # hotspots are content-driven (allow-list rule 11)
        need(".hotspot", counts["hotspots"])
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
        need(".psq", counts["retrievable"], "one square per retrievable hotspot")
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
        need('.hotspot[data-state="inert"]', counts["hotspots"] - 1,
             "non-target hotspots drop to inert outlines")
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

    return p


# ── the driver ───────────────────────────────────────────────────────────

SCREENS = ["s01", "s01open", "s01narrow", "s02", "s04", "s04drawer", "s05",
           "s05raised", "s05lib", "s06"]


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


def run_browser_layers(url, tokens, counts):
    problems, style_rows = [], []
    checked = []

    def visit(page, screen):
        page.eval(_JS + "true")
        state = _await_stage(page)
        if state != "ready":
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

    # §06 — a separate Chrome with WebGL off, so the REAL capability probe
    # lands on tier D and the paper stage is exercised end to end.
    with cdp.Browser(extra_args=["--disable-webgl", "--disable-webgl2"]) as b:
        page = b.attach()
        page.set_viewport(1440, 900)
        page.goto(url)
        visit(page, "s06")

    return problems, style_rows, checked


def main():
    print("3D Studio parity gate — reference: %s"
          % os.path.relpath(REFERENCE, HERE))

    tokens = studio_tokens()
    counts = _content_counts()

    # layer A
    a_problems, a_notes = check_provenance()
    for note in a_notes:
        print("  A: " + note)

    if not os.path.isdir(DIST) or not os.path.exists(
            os.path.join(DIST, "index.html")):
        print("FAIL: no built app at %s — run `npm run build` in 3d-studio/"
              % os.path.relpath(DIST, HERE))
        return 1

    # serve dist under /3d/ so the app's absolute asset URLs resolve
    root = tempfile.mkdtemp(prefix="st-parity-")
    os.symlink(DIST, os.path.join(root, "3d"))
    server, port = cdp.serve(root)
    try:
        url = "http://127.0.0.1:%d/3d/" % port
        b_problems, style_rows, checked = run_browser_layers(url, tokens, counts)
    finally:
        server.shutdown()

    ok_rows = sum(1 for r in style_rows if r[5])
    print("  B: screens driven: %s" % ", ".join(checked))
    print("  C: %d/%d style expectations hold" % (ok_rows, len(style_rows)))

    problems = a_problems + b_problems
    if problems:
        print("\n%d problem(s):" % len(problems))
        for pr in problems:
            print("  ✗ " + pr)
        return 1
    print("PARITY PASS — %d screens, %d style rows, %d tokens provenanced"
          % (len(checked), len(style_rows), len(studio_tokens())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
