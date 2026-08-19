# KS3 Biology — WS1 figures package

19 August 2026. Twelve figures for the WS1 diagram gaps, plus the review notes
and everything needed to open them offline.

## Two ways to open

1. **`KS3 biology figures (offline).html`** — one self-contained file, 6.2 MB.
   Double-click it. No other file in this zip is needed; fonts, tokens and all
   twelve figures are embedded. Click a card to open a figure, Esc or *Back* to
   return. This is the copy to send to a reviewer.
2. **`figures-ks3-biology/00-index.dc.html`** — the source index. Needs the rest
   of the folder structure intact (`support.js` and `_ds/` sit beside it at the
   package root, which is where the files expect them). Use this copy to edit.

## What is in here

| Path | What it is |
| --- | --- |
| `NOTES-FIGURES.md` | The review notes: what every figure does the same way, what was left out and why, where I would argue with the brief, and **six things I would like ruled** (§4). Read this first. |
| `figures-ks3-biology/` | `00-index.dc.html` + the twelve figure files + `support.js`. Same `NOTES-FIGURES.md` sits inside too. |
| `_ds/mrbadmusai-…/` | The design-system subset the figures load: `styles.css`, tokens, component CSS/JS, and the seven self-hosted `woff2` fonts. |
| `support.js` | Runtime for the `.dc.html` files. Must stay at the package root — the figures reference `../support.js`. |
| `docs/diagram-manifest.md` | The project-wide diagram manifest, for cross-reference. |

## The twelve figures

Filename numbers follow the **audit's** numbering, not delivery order, so
`fig-08` and `fig-12` are absent by design and `fig-15` (rest vs inspiration) is
deferred.

- `fig-01-b10-nested-scale` — one strand, five magnifications (flagship)
- `fig-02-b5-reproductive-systems` — nine structures, where the body puts them
- `fig-03-b7-leaf-section` — a leaf, sliced through
- `fig-04-b3-villus-labelled` — folds on folds on folds
- `fig-05-b5-placenta-exchange` — two bloodstreams, never joined (flagship)
- `fig-06-b3-gut-tube` — one tube, coiled, three organs alongside
- `fig-07-b4-thorax-labelled` — the route in, and the machinery around it
- `fig-09-b5-flower-parts` — held inside, or dangling outside
- `fig-10-b5-gametes-journey` — two different places, five days apart
- `fig-11-b4-guard-cells` — the same pair, twice
- `fig-13-b5-pollen-tube` — the ovule is inside the ovary, before and after
- `fig-14-b5-dispersal-specimens` — eight specimens, one scale, no answers

## For whoever implements these

The figures are self-contained SVG — no external assets, no new fonts, no
raster. Font families are named inline (`'Bricolage Grotesque'`,
`'Instrument Sans'`, `'DM Mono'`) because SVG presentation attributes will not
take `var(--ks3-font-display)`.

The **review switcher** (Full / 768 / 390) and the **"what has to be checkable"
band** in each header are review affordances, not part of the figure. The
assumption is that they are dropped on implementation, keeping the `<title>`,
`<desc>`, `<figcaption>` and the scroll container. That assumption is item 6 in
§4 of the notes and wants confirming.
