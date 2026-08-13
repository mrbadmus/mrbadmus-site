# B1 per-lesson inventory — what the next run builds from

Produced 13 Aug 2026. **This is a specification, not a build.** The six lessons
are not built here. Each file in this folder is the complete account of one
approved page, so the run that builds it is working from a read specification
rather than guessing at a half-read one.

## Why this exists in this shape

MRB-205 ruled that Design plans every KS3 lesson in full and draws its screens,
and Code renders to them and never invents a shape. MRB-203 built the registry
that fails the build when a lesson renders a block type with no registered
component. Between them, the thing standing between B1's six approved pages and
a correct build is an exhaustive component-by-component reading of each page —
and the previous attempt lost three of its four inventory agents to a session
limit part-way through, which is why these are written and committed **one
lesson at a time**.

## Source of truth

`docs/ks3/design-reference/b1/*.dc.html` — Design's approved delivery, committed
unmodified as the provenance anchor. Every measurement in these files was taken
from those pages, in a real browser, at four viewports:

| Viewport | Why |
|---|---|
| **1280** | the reference-set width; most components' resting measurements |
| **1340** | the progress rail's `min-width` threshold — the rail exists only at and above this |
| **820** | the narrow-layout threshold (see `00-delivery-drift.md`, drift 2) |
| **390** | a true layout viewport for a phone, via device-metrics override |

⚠️ **Narrow widths must be measured by overriding device metrics, never by
shrinking a container.** Design's own words, kept in `ks3_parity.py`'s gate
documentation: *"Shrinking `.ks3-main` in a probe does not fire a `max-width`
media query — the viewport is still wide. Container-driven wrapping is testable
that way; viewport queries are not."* Design's first attempt at one of these
fixes measured as a no-op for exactly this reason.

## The generator's current vocabulary, for the "new or existing?" column

**Block types the authored data emits** (count across all KS3 content):
`check` 64 · `explainer` 30 · `figure` 27 · `misconception` 19 · `practical` 15
· `summary` 12 · `quiz` 12 · `keyword` 12 · `hook` 12 · `worked-example` 2

**Sim kinds:** `particle-states`, `gas-pressure`, `diffusion`, `microscope`,
`system-parts`

**Registered components:** 60 in `ks3_parity.COMPONENTS`, 65 contrast pairs in
`ks3_parity.CONTRAST`. §10.2 of `docs/ks3/design-coverage-manifest.md` maps each
block type to the components that gate it.

**Tokens** live in `shared/tokens.css` and `shared/ks3.css` under the
`--ks3-*` prefix (61 of them). A measurement "traces to tokens" only if it
resolves to one of those; a bare px value that happens to equal a token's value
is still a new measurement until it is expressed as the token.

## What each lesson file contains

1. **Blocks and components** — every distinct one, with all its states, and
   whether the generator has an equivalent or it is new.
2. **Interactive behaviours** — each one and its trigger.
3. **Schema gaps** — every field the page implies that §4.8's lesson record does
   not have. §4.8 is authoritative: *"Fields not listed here do not exist
   without an amendment to this document."*
4. **Measurements** — every one, and whether it traces to a token or is new.
5. **For each new component** — exactly what it takes to generate it from data.
6. **Ambiguities** — flagged, never resolved. Where a page is unclear about
   behaviour, that is a finding for Design or Mide, not something to improvise
   around.

## Files

| File | Lesson |
|---|---|
| `00-delivery-drift.md` | the five cross-page drifts, ruled |
| `b1-01-life-processes.md` | L1 · CLASSIFY |
| `b1-02-using-a-microscope.md` | L2 · INVESTIGATION |
| `b1-03-animal-and-plant-cells.md` | L3 · MODEL |
| `b1-04-specialised-cells.md` | L4 · SYSTEM |
| `b1-05-levels-of-organisation.md` | L5 · SYSTEM |
| `b1-06-unicellular-organisms.md` | L6 · CONTRAST |

## Standing law these files are written under

As amended by Mide on 12–13 Aug 2026 (MRB-205, MRB-210):

- Design's approved page is the specification and Code reproduces it exactly.
- Code **may add** behaviour, physics, detail or refinement **inside a component
  Design has drawn**, where the approved pages are silent. It states what it
  added and why. No round trip.
- Code **may not invent** a component, block type, layout or page structure
  Design has not drawn. MRB-203's registry fails the build over this.
- An addition **may not contradict** the approved page. Where the page teaches
  one thing in words and the engine does another, **the page wins**.
- Where the generator cannot reproduce something from data, that is a
  **finding**, not a licence to approximate.
