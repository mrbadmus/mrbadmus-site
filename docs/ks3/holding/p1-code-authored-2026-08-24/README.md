# P1 — *Energy transfers*, as Code authored it. HOLDING ONLY. NOT SHIPPED.

**Date authored:** 23–24 August 2026 (MRB-223, run 1).
**Status: SUPERSEDED. Nothing in this folder is in the build path.**

## What this is

Eight complete KS3 physics lessons — records, questions, instruments, styling
and rendered pages — written by Claude Code **against no drawing**.

Run 1 globbed `docs/ks3/design-reference/*/*.dc.html`, found no physics folder,
and concluded Design had drawn nothing for physics. That conclusion was wrong:
Design has authored the physics lessons, and they were in the repo the whole
time — absence found in one location is not absence.

Because run 1 believed there was no drawing, it invented the shapes: the
instruments, the layouts, the benches, the CSS. **MRB-205 forbids invented
shapes**, so none of it ships. Design's pages win outright, element for
element, and P1 is being rebuilt from her delivery.

This folder exists because Mide asked to see the work before it was stood
down. It is kept, not deleted.

## What is here

| Path | What |
|---|---|
| `pages/` | **The eight rendered lesson pages + the unit index.** Open these in a browser — this is the part to look at. Self-contained: the CSS, JS and fonts they need sit in `pages/shared/`, and the asset paths have been rewritten to relative so they render from `file://`. Site-wide nav links (`/index.html`, `/ks3/index.html`) still point at the live site and will not resolve locally — that is expected and harmless. |
| `ks3_data/p1/` | The eight lesson records, the eight question files (96 questions), and the package wrapper `__init__.py`. |
| `ks3_data/physics_p1_energy_transfers.py` | The earlier single-file draft of the unit, kept for completeness. |
| `ks3_art/p1.py` | P1's drawers, instruments and family registrations. |
| `shared-blocks/` | The `BEGIN P1` / `END P1` blocks lifted out of `shared/ks3.js` and `shared/ks3.css`, plus the `build_ks3.py` diff. Extracts only — never the whole file. |
| `p1_drive.py` | Run 1's instrument-drive harness. |

## The eight lessons — slug → page file

| # | Slug | Page |
|---|---|---|
| 1 | `energy-stores` | [pages/energy-stores.html](pages/energy-stores.html) |
| 2 | `energy-transfers-before-and-after` | [pages/energy-transfers-before-and-after.html](pages/energy-transfers-before-and-after.html) |
| 3 | `conservation-of-energy` | [pages/conservation-of-energy.html](pages/conservation-of-energy.html) |
| 4 | `heating-and-thermal-equilibrium` | [pages/heating-and-thermal-equilibrium.html](pages/heating-and-thermal-equilibrium.html) |
| 5 | `conduction` | [pages/conduction.html](pages/conduction.html) |
| 6 | `radiation` | [pages/radiation.html](pages/radiation.html) |
| 7 | `insulation` | [pages/insulation.html](pages/insulation.html) |
| 8 | `simple-machines` | [pages/simple-machines.html](pages/simple-machines.html) |
|  | *(unit index)* | [pages/index.html](pages/index.html) |

## Known defects in this version

- The self-check buttons on `energy-stores` are **inert** — nothing generic
  wires `.ks3-option` inside `[data-selfcheck]`, and run 1 never wired it.
- The 96 questions were written against this invented content, so their
  wording assumes screens Design did not draw.

## What was carried forward out of run 1

Three things from run 1 are real and independent of the authoring error, and
are being kept in the build:

1. The `g.ks3-bar-cover` open-before-JS fix — a live C2 defect since MRB-220.
2. Two ladder questions with escaped `<em>`.
3. Any other genuine gate or CSS fix not tied to invented content.
