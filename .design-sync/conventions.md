# MrBadmusAI — how to build with this design system

**Setup.** No provider or wrapper is needed — every component is self-contained and styled by the `styles.css` closure. Components live on `window.MrBadmusDS`. Two that need composition: `ToolRail` and `Stage` take a `renderer` — create one with `MrBadmusDS.createPlaceholderRenderer('viewport')` (dark 3D stage, 7 tools) or `('paper')` (flat diagram stage, 4 tools).

**Fonts — one hard trap.** Bricolage Grotesque (display, weight 600, tight tracking), Instrument Sans (UI/body), DM Mono (uppercase eyebrows, captions, numerals) ship self-hosted. Their latin subsets do NOT contain `→` (U+2192), `✓` (U+2713) or `✕` (U+2715): never type those characters — draw arrows, ticks and crosses as inline SVG or they silently fall back to a system font. `Space Grotesk` / `IBM Plex` appear in the legacy token file but are runtime-provided on the live site only — do not build new surfaces with them.

**Styling idiom: CSS custom properties, no utility classes.** Three token families, each scoped to a surface:

- **3D Studio (`--st-*`, in `tokens/src-styles-tokens.css`)** — use for studio screens. Cream world: `--st-ground` #FBF3E6, `--st-paper` #FFFDF8, `--st-ink` #1A1714, `--st-muted`, `--st-caption`, `--st-rule`. Accent: `--st-accent` #E4572E for large/graphic use ONLY; `--st-accent-text` #A93411 is the only orange at body/small sizes. Dark room: `--st-room` #15110C, `--st-room-panel`, `--st-room-text`, `--st-ember` (accent text on dark). Radii `--st-r-stage`/`--st-r-card`, shadows `--st-shadow-frame`.
- **KS3 (`--ks3-*`, in `tokens/shared-ks3.css` + the KS3 block of `tokens/shared-tokens.css`)** — the dials only apply under BOTH hooks: the root element must carry `class="rd"` AND `data-mode="ks3"`, or every `--ks3-*` value is inert. Two tokens per hue: the fill token (e.g. `--ks3-accent`) is large-text/graphic only; the `-text` variant (e.g. `--ks3-accent-text`) is the only one legal at body size.
- **Site-wide (`tokens/shared-tokens.css` `:root`)** — `--bg`, `--card`, `--accent` #A63C12, subject identity `--physics`/`--chemistry`/`--biology`, `--danger` (red-as-warning is never `--chemistry`). The KS4 legacy page chrome (`shared/styles.css` in the repo) is deliberately not shipped here.

Component class vocabulary comes from `_ds_bundle.css` (real names: `.eyebrow`, `.btn.btn--primary` / `.btn--outline`, `.kchip`, `.stage.stage--viewport` / `.stage--paper`, `.callout`, `.panel`, `.railbtn`). For your own layout glue use inline styles or your own classes fed by the tokens above — this system has no utility-class layer.

**House rules (binding).** Identity is never carried by hue alone — hotspot states differ by size, fill inversion and numeral. The brand is the two-chevron `BrandMark` + "MrBadmusAI" wordmark in Bricolage 600 (never an octopus or alembic glyph). Copy discipline: no platform meta-text, no methodology notes, no reassurance copy — the only prose is terse functional instruction. Data model vocabulary is `specimen` and `item`, never `organ`. Anatomy strings in mocks stay lorem-style placeholder — real science text is examiner-gated.

**Where the truth lives.** Read `styles.css` and its imports (`tokens/*.css`, `fonts/fonts.css`, `_ds_bundle.css`) before styling. Per-component API + usage: each `components/general/<Name>/<Name>.prompt.md`. The frozen reference's binding layout/interaction annotations: `guidelines/reference/design-notes.md`.

**Idiomatic snippet** — a stage fragment on studio tokens:

```jsx
const { HotspotDot, QualityChip } = window.MrBadmusDS;

<div style={{ position: 'relative', height: 420,
  borderRadius: 'var(--st-r-stage)', border: '1px solid var(--st-viewport-edge)',
  background: 'radial-gradient(90% 75% at 50% 38%, #2C261F 0%, #191510 55%, #100D0A 100%)' }}>
  <HotspotDot state="closed" surface="dark" numeral="01" x={180} y={120} label="Structure 01" />
  <HotspotDot state="open" surface="dark" numeral="02" x={300} y={210} label="Structure 02" />
  <QualityChip setting="auto" detected="B" open={false} onToggle={() => {}} />
  <div className="stagehint">Drag to rotate · click a dot to label</div>
</div>
```
