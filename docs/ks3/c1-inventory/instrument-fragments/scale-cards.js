// WIRE: (none — `scale-cards` registers no wire function and takes no line in
//        `wireInstruments()`.)
//
// This file exists so the question "where is the JS for scale-cards?" is
// answered once, in the place someone will look, instead of being re-asked
// every time the kind is touched.
//
// The component is STATIC. Three cards and a closing paragraph: no control, no
// state, no canvas, nothing to reveal and nothing to count. There is no
// behaviour to attach, so attaching an empty `wireScaleCards(sec)` would be a
// dispatch-table entry pretending to be a component — the exact thing the
// comment above `ACTIVITY_KIND_RENDERERS` warns about.
//
// Two consequences worth stating, because both look like omissions:
//
//   1. The section carries `data-instrument`, which has a real job even with
//      no wiring: it keeps `wirePredictions` out. There are no `.ks3-option`
//      elements inside this block today, so nothing would be mis-wired — but
//      the exclusion is a property of the kind, not of this instance, and a
//      future card that gained a control would otherwise inherit the generic
//      Law 4 wiring silently.
//
//   2. `data-scalecards` is the marker attribute the dispatch table names. It
//      selects nothing in `shared/ks3.js` and is not meant to: it is the hook
//      the stylesheet and the parity rows and any future behaviour attach to,
//      and having it means the day this kind DOES gain a control the selector
//      already exists rather than being invented then.
//
// The block is not a rail stop either, so it declares no `data-stage-done` and
// there is no `markStage` call to make. See the renderer's docstring.
