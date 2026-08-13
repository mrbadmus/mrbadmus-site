# 3D Studio shell — design notes extracted from the frozen references

Sources, both frozen (Claude Design — never edit either):

- `3d-studio/reference/shell-v1.html` — §01–§07, frozen under MRB-186.
- `3d-studio/reference/crosssection-v1.html` — §08–§10, frozen under MRB-189.
  It redraws §01–§07 as well; that redrawing is **byte-identical** to
  `shell-v1.html` (the two files differ only in the HTML comment on line 8,
  `design reference` → `design reference v2`), so `shell-v1.html` remains the
  frozen reference for those seven screens and nothing about them is restated
  or superseded here.

Every annotation block in the references is reproduced here as a checklist item;
these are binding intent, not decoration. Check an item only when the build
genuinely satisfies it.

Conventions the whole reference shares:

- Palette: `#FBF3E6` cream ground · `#FFFDF8` paper/card · `#E4572E` accent ·
  `#A63A18` accent-text (links, small accent type) · `#1A140E` ink ·
  `#6E6255` muted body · `#8A7C6B` caption · `#E4D6BF` hairline rule ·
  dark room `#15110C` / stage viewport radial `#2C261F → #191510 → #100D0A`.
- Type: Bricolage Grotesque (display, 600, tight tracking), Instrument Sans
  (UI/body), DM Mono (eyebrows, captions, numerals — uppercase, letterspaced).
- Brand: two-chevron mark, both `#E4572E`, second at 34% opacity, +
  "MrBadmusAI" wordmark in Bricolage 600. (This is the reference's own drawing
  of the public-page brand for this surface.)

## §01 Desktop — exploration (1440)

Layout: library 232 / stage fluid / panel 372, 24px gutters. Header 64px;
breadcrumb strip 56px (`3D STUDIO / CIRCULATORY / HUMAN HEART`) with the
Explore/Retrieve segmented MODE control on the right.

- [ ] **HOTSPOTS** — "28px, 2.5px cream ring, 3px dark halo — legible on any
  model colour. Numeral carries identity, not hue."
- [ ] **OPEN LABEL** — "Dot grows to 38px and inverts to cream fill. One callout
  at a time; leader line keeps the link explicit."
- [ ] **TOOL RAIL** — "Rotate, zoom, isolate, cross-section, layers, reset,
  auto-rotate. Tooltips carry the keyboard/pointer verb."
- [ ] **QUALITY TIER** — "Bottom-right, four-bar meter + word. Deliberately the
  quietest element on the stage. Opens the override in §07."

Also in the drawing (in-situ specifics):

- [ ] Library: `LIBRARY` eyebrow + count; viewing card = paper bg + 1.5px accent
  border + `VIEWING` caption in accent; coming-soon rows at 52% opacity with
  `· SOON`; hairline divider between available and soon.
- [ ] Stage hint line, DM Mono caption, bottom-centre: "DRAG TO ROTATE · CLICK A
  DOT TO LABEL".
- [ ] Callout card: dark `rgba(16,13,10,.95)`, 216px, structure eyebrow in
  `#F0885F`, Bricolage title, muted detail, `ISOLATE · HIDE LABEL` footer row.
- [ ] Auto-rotate is a labelled toggle (pill switch + `AUTO`) at the rail foot,
  separated by a rule.
- [ ] Panel order: key-stage chips (+ structure count chip in accent) → name
  (Bricolage 36) → epithet (italic, muted) → description → STRUCTURES 2-col
  chip grid (numbered; open structure highlighted in accent) → KEY FACTS rows →
  WHY IT MATTERS (ink block, `#F2946E` eyebrow) → DID YOU KNOW (`#F5EAD6`,
  dashed border) → pinned footer: `Open lesson` (outline) + `Start retrieval`
  (accent fill), with a fade-out gradient above the footer.

## §02 Desktop — retrieval

- [ ] **MODE READS AS A ROOM** — "Ground inverts to ink, library is removed
  rather than dimmed, hatch strip runs the full width. Nothing about it is
  'explore minus labels'." (Hatch: 7px, repeating -45° `#E4572E`/`#B33E1C`.)
- [ ] **TARGET** — "52px, cream fill, '?' glyph, one slow ring pulse. Other
  hotspots drop to 13px inert outlines so orientation survives."
- [ ] **FREE RECALL FIRST** — "Typed answer, not multiple choice. Reveal is
  present but demoted below the fold of the decision."
- [ ] **PROGRESS** — "Six squares: solid + tick = named, accent ring + numeral =
  current, hollow = ahead. Shape carries state, colour only reinforces."

In situ: rail shrinks to rotate/zoom/reset; stage hint becomes "ROTATE FREELY ·
LABELS RETURN AFTER THE ROUND"; `End round` button in the header; MISSED SO FAR
chips + "Missed structures come back at the end of the round."

## §03 The sign-in moment

- [ ] **RESULT BEFORE ASK** — "The top half of the card is entirely theirs —
  score, per-structure marks, time. The invitation is below the perforation."
- [ ] **NOT A WALL** — "Scrim is 55%, the stage stays visible, 'Carry on without
  one' is a full-width button — not a grey link under the fold."
- [ ] **ONE REASON, CONCRETE** — "A single sentence about what the account does
  for the next round. No feature list, no benefit grid."
- [ ] **A ROAD ONWARD** — "The next specimen sits in the footer, so the moment
  reads as a milestone in a sequence rather than a stop."

## §04 Tablet — 834pt portrait

- [ ] **DRAWER** — "372pt, overlays from the left, scrim at 42%. Tapping a
  specimen loads it and closes the drawer in one action — no confirm step.
  Closed by default; the trigger sits first in the header so it reads before
  the brand."
- [ ] **STAGE** — "Fixed 520pt tall, full content width. The rail stays vertical
  and keeps all seven tools — a tablet has the room and often is the teacher's
  device."
- [ ] **PANEL** — "Reflows to two columns under the stage. Actions rise to sit
  beside the title where they stay above the fold; callouts continue below the
  visible cut."
- [ ] **HIT TARGETS** — "Hotspots keep the 28px visual but carry a 48pt
  transparent touch area. Rail buttons are 36px in a 46pt column."
- [ ] **LANDSCAPE** — "Above 1024pt wide the desktop three-column layout returns
  and the drawer trigger disappears."

## §05 Phone — 390pt

- [ ] **SHEET** — "Two detents: rest at 428pt, raised at 608pt. The stage never
  fully leaves — 150pt of it stays so the model keeps its context."
- [ ] **RAIL GOES HORIZONTAL** — "Five tools on a scrollable strip at the foot of
  the stage, 40pt targets, right edge faded to show there is more."
- [ ] **ONE FIXED ACTION** — "Start retrieval is pinned to the bottom of the
  sheet at every detent; the lesson link shrinks to a glyph beside it."
- [ ] **LIBRARY IS FULL-SCREEN** — "Not a half sheet — choosing a specimen is a
  deliberate move, and eight rows want the height."

In situ: quality chip moves to the stage's top-right on phone; header shows the
specimen name (not the brand) once the sheet is raised; library footer carries
"More specimens soon" + "Create account".

## §06 Stage — 2D fallback

- [ ] **WHAT CHANGES** — "The plate is drawn on paper rather than in a dark
  viewport — a flat diagram has no depth to light, so the studio surround would
  be a costume. Everything outside this rectangle is identical to §01."
- [ ] **RAIL: FOUR TOOLS** — "Zoom, isolate, labels, reset. Rotate,
  cross-section, layers and auto-rotate are absent — a disabled tool is a
  promise the device cannot keep. Labels earns its slot here because it is the
  only way to clear a busy plate."
- [ ] **NO QUALITY CHIP** — "Tiers describe render load. With no renderer there
  is no tier, so the control goes rather than showing a fifth state."
- [ ] **HOTSPOT ON PAPER** — "Same 28px dot; the halo flips to a 2px ink ring so
  it holds on a light ground. The open state inverts to ink fill instead of
  cream."
- [ ] **SHARED** — "Hotspot ids, structure names, panel content and retrieval
  rounds come from one specimen record. Only the coordinates are authored per
  view."

In situ: paper stage is `#FFFDF8` with a 36px `#F2E8D6` grid; `FLAT DIAGRAM`
chip top-right.

## §07 Parts (component source of truth)

Hotspot states, dark stage:

| State  | Size | Fill      | Ring                    | Halo                        | Content |
|--------|------|-----------|-------------------------|-----------------------------|---------|
| Closed | 28px | `#E4572E` | 2.5px `#FBF3E6`         | 3px `rgba(8,6,4,.6)`        | numeral |
| Hover  | 32px | `#E4572E` | 2.5px `#FBF3E6`         | + 9px `rgba(251,243,230,.16)` glow | numeral |
| Open   | 38px | `#FBF3E6` | 3px `#E4572E`           | 4px `rgba(8,6,4,.55)`       | numeral (ink) |
| Inert  | 13px | none      | 1.5px `rgba(251,243,230,.42)` | —                     | none    |
| Target | 52px | `#FBF3E6` | 4px `#E4572E`           | 5px `rgba(8,6,4,.6)`        | `?` 22px + one slow ring pulse |

Hotspot states, paper stage: closed = same 28px accent dot, ring flips to
`#FFFDF8`, halo to 2px `#1A140E`; open = 38px **ink** fill, 3px accent ring,
cream numeral.

- [ ] "Size, fill inversion and the numeral do the work. Remove the orange
  entirely and every state is still distinct." (This is the no-hue-only gate.)

Quality override panel (262px, dark):

- [ ] "The chip on the stage is the whole affordance: a four-bar meter and one
  word, bottom-right, at the contrast of a caption. Tapping it opens this."
- [ ] "Auto is selected until a person overrides it, and the detected tier stays
  visible so the override is a choice against something known."
  (`RENDER QUALITY` header + `DETECTED · <word>` caption; Auto row marked
  RECOMMENDED; Ultra/High/Balanced/Lite rows with 4/3/2/1-bar meters.)
- [ ] "no toast · no banner · no first-run tour"

Projection floor:

- [ ] "The cream ring survives because it is the lightest value in the frame and
  the dark halo is the darkest — the orange is decoration." (Washed-projector
  simulation tile; the sim toggle itself is a canvas handoff control, not a
  product feature.)

## §08 The cut face (`crosssection-v1.html`)

Header note: "Clipping plane at 46%. Near half gone, cap solid. Wall and cavity
are separate materials, and neither is the accent."

Materials sheet — three swatches, exactly these values:

| Material | Value | Treatment |
|---|---|---|
| Cut wall | `#F0E9DC` | `FLAT, HATCHED` — no shading of any kind; 1.5px `#100D0A` outline |
| Cavity & lumen | `#141109` | annotated `17:1 AGAINST WALL` |
| Outer wall, uncut | radial gradient `#A9A198 → #857D73 40% → #565048 78% → #3D3830` | `SHADED · UNCHANGED` |

- [ ] **THE TWO VALUES ARE THE EXTREMES OF THE FRAME** — "not neighbours in a
  family: lightest thing on the stage against darkest. Same argument that
  carried the hotspot ring. A cavity is an absence of material, so it takes the
  void end — nothing to invent, and nothing to unlearn when a student meets a
  printed plate."
- [ ] **FLAT AGAINST SHADED IS THE LOAD-BEARING PART** — "The cut face is *flat
  and unshaded* while the exterior keeps its gradient. That alone says *cut*
  before any colour is read, and it holds in greyscale." If an implementation
  choice forces a trade, flatness is preserved over hue.
- [ ] **ACCENT IS THE TOOL, NOT THE TISSUE** — "Orange comes off the organ
  entirely. It marks the plane — the rule through the specimen, its end ticks,
  and the slider being dragged — because the plane is the interactive thing.
  Tissue is substance and never highlights itself."
- [ ] **HOTSPOTS ON THE CUT FACE FLIP TO PAPER** — "This also frees the
  hotspots. Dots keep their one meaning on the cut face; on that light ground
  they flip to the paper variant from §07, dark outline and all."
- [ ] "no legend · no key · label reads SECTION"

The hatch is optional: "The hatch on the chosen tile is optional decoration —
strip it and nothing is lost." (As drawn:
`repeating-linear-gradient(45deg, rgba(26,20,14,.07) 0 3px, rgba(26,20,14,0) 3px 7px)`
over the flat fill.)

WHY NOT THE OTHER TWO — four comparison tiles, and the verdict on each:

- [ ] `AS BUILT — TWO ACCENT VALUES · WALL/CAVITY 2.8:1 · READS AS SELECTED`.
  "The two accent values sit close enough in lightness that the projector
  merges them, and the whole cut reads as one selected object rather than
  material."
- [ ] `ONE FLAT FILL · GEOMETRICALLY TRUE · NO CHAMBERS` — rejected.
- [ ] `WALL / CAVITY — CHOSEN · 17:1 · SURVIVES NESTED SHAPES`.
- [ ] `CHOSEN, WASHED · SAME SIMULATION AS §07` — the chosen pair under the
  projector wash.

In situ (the §08 hero, 1440): plane drawn as a 1.5px vertical rule through the
specimen, `#E4572E` fading to zero at both ends
(`rgba(228,87,46,0) → .75 at 18% → .75 at 82% → 0`), with two 16×1.5px `#E4572E`
end ticks; cross-section tool active in the rail (accent fill, cream icon) with
its `Cross-section` / `C` tooltip; quality chip bottom-right unchanged; section
slider bottom-centre (§09).

## §09 The section slider (`crosssection-v1.html`)

Header note: "Quality-chip chrome, foot of the stage. Present at a glance,
recessive until touched. **Only shown while the tool is on.**"

- [ ] **DESKTOP 1440** — `PLATE 392×44 · BOTTOM CENTRE`. Plate is quality-chip
  chrome: `rgba(22,18,14,.86)`, 1px `#3E362C`, radius 11, 18px from the bottom,
  padding `0 14px`, gap 12. `SECTION` eyebrow (DM Mono 10.5px/500, `.16em`,
  `#8A7E6E`) · track · readout (DM Mono 11.5px, `#B7AA98`, 40px right-aligned).
- [ ] **DRAG EMPHASIS LANDS ON THE CUT** — "Dragging thickens the handle,
  hatches the travelled track to match the cut face, promotes the value from
  caption to 15px, and brings the plane rule up to full strength with its end
  ticks. Emphasis lands on the cut, not on the furniture."
- [ ] **THE ROTATE HINT YIELDS** — "The rotate hint at bottom centre yields to
  the plate — one thing lives on that edge at a time."
- [ ] **TABLET 1024** — `PLATE 320×44 · CLEARS THE RAIL BY 16`. "Same plate,
  narrower, and no longer centred on the stage — it centres on the space left
  of the rail so the two never touch. Height stays 44 because it is now a touch
  target." (Drawn at `left:calc(50% + 22px)`, 16px from the bottom, padding
  `0 13px`, gap 11, readout 38px/11px.)
- [ ] **PHONE 390 — ONE BAR, SHARED WITH THE RAIL.** "THE RAIL YIELDS, IT DOES
  NOT STACK. Both want the bottom edge and there is room for one. Turning
  cross-section on collapses the five-icon rail from §05 to the single tool that
  is running — orange, cream dot, 44 square — and the slider takes the rest of
  that same bar. Tap the tool to exit and the rail returns."
- [ ] **NO SECOND ROW, NO SHEET, NO LOST STAGE HEIGHT** — "Nothing scrolls
  behind a thumb, the stage keeps its height, and the bar never gains a second
  row. While you are cutting, the other four tools are not what you want
  anyway."
- [ ] **THE READOUT LIFTS ON PHONE** — "The readout cannot stay in the bar — a
  thumb covers it. It lifts to the top-left corner of the stage, opposite the
  quality chip, and only while dragging."
- [ ] "44 targets · no sheet · no second row"

In situ (phone): the collapsed tool is a 44×44 `#E4572E` square, radius 12,
cream icon, with a 9×9 `#FBF3E6` running dot ringed 2px `#100D0A` at its top
right; the bar is 60px tall over
`linear-gradient(rgba(16,13,10,0), rgba(16,13,10,.94) 45%)`, padding `0 12px`,
gap 8; the slider pill is `flex:1`, 44 tall, radius 12, and carries **no**
`SECTION` eyebrow. The dragging readout chip sits at `left:12 top:12` —
`SECTION` 9.5px + value 15px `#FBF3E6` on `rgba(18,14,10,.96)` / `#5C5347`.
Phone handle is 11×32 at rest, 13×40 with a 9px halo while dragging.

## §10 Parts — slider (component source of truth)

Header note: "Every state at full size, then the same handle under the
projector."

Slider states, dark stage (plate 392×44 in every row):

| State | Handle | Handle extras | Plate | Travelled track | Readout |
|---|---|---|---|---|---|
| Rest | 10×30 r3 | ring 2px `#100D0A`, drop `0 4px 10px rgba(0,0,0,.6)` | `rgba(22,18,14,.86)` / `#3E362C` | `#C4B8A7` | 11.5px `#B7AA98` |
| Hover | 11×34 r3 | + 6px halo `rgba(251,243,230,.11)` | `rgba(22,18,14,.92)` / `#4A4036` | `#C4B8A7` | 11.5px `#B7AA98` |
| Dragging | 12×38 r3 | + 8px halo `rgba(251,243,230,.15)` | `rgba(18,14,10,.96)` / `#5C5347` | hatched `repeating-linear-gradient(45deg,#C4B8A7 0 3px,#8A7E6E 3px 6px)` | **15px/500 `#FBF3E6`** |
| Keyboard | 10×30 r3 + 2×14 `#100D0A` notch | plate `outline:2px #FBF3E6`, offset 3 | `rgba(22,18,14,.86)` / `#3E362C` | `#C4B8A7` | 11.5px `#B7AA98` |

The `SECTION` eyebrow deepens to `#6E6255` while dragging (from `#8A7E6E`).

- [ ] **KEYBOARD** — "ARROWS STEP 2%, NOTCHED HANDLE". Drawn, therefore
  required.
- [ ] **HANDLE ANATOMY** — `HIT 44`, `10×30 R3`. "The handle is a bar, not a
  knob, because the thing it moves is a plane. It reads as the plane's edge seen
  end-on, and the shape alone distinguishes it from every round hotspot on the
  stage."
- [ ] **IT INHERITS THE HOTSPOT CONSTRUCTION** — "Cream fill with a dark 2px
  ring, exactly the hotspot construction: lightest value, darkest halo. That
  pairing is what survived the washed-projector test, so the handle inherits it
  rather than arguing again."
- [ ] "track 4 · plate 44 · gap to rail 16"
- [ ] **PROJECTION FLOOR** — "Washed, the plate loses its edge and the track
  loses half its depth — the cream bar and the light travelled segment both
  hold, so position is still readable from the back of the room. The percentage
  is a courtesy for whoever is at the keyboard."

Two things Design removed deliberately, recorded so they are not reintroduced:

- [ ] **No leader line from handle to cut.** The handle's x and the plane's x do
  not genuinely coincide, so a connector would be a lie. Drag emphasis lives on
  the plane instead.
- [ ] **No light-ground variant of the slider.** Retrieval keeps the stage dark
  and cross-section is absent from the flat renderer, so a light-ground state
  cannot occur.

## Reconciliations within §08–§10 (MRB-189 build)

The reference draws the plane's end ticks in the §08 hero at rest, and omits
them from the three at-rest tiles in §09 while drawing them in all three
dragging tiles. §09's own caption reads "brings the plane rule up to full
strength with its end ticks", and §08's prose lists "the rule through the
specimen, its end ticks" as things the accent marks, unconditionally. Built as
one plane-strength variable: rule **and** ticks are drawn at both states, at
0.75 strength at rest and full strength while dragging. That satisfies the §08
hero, both prose lines, and the §09 dragging tiles; the §09 at-rest tiles are
1440-to-176px reductions where the 16px ticks would be sub-pixel.

The materials sheet annotates the wall/cavity pair as `17:1`. Measured with the
WCAG formula the pair is **15.62:1** (`#F0E9DC` L=0.81970, `#141109` L=0.00569).
Design's figure is generous by about 9%; the argument — extremes of the frame,
not neighbours — is unaffected, and 15.62:1 clears every threshold the claim is
used to support. The built value is the drawn value; only the annotation is
approximate. Recorded in the parity allow-list rather than silently tolerated.

## Rulings applied on top of the reference (Linear beats reference where they touch)

- Quality options map Ultra→A, High→B, Balanced→C, **Lite→C**. Tier D is the
  capability floor (no WebGL ⇒ flat renderer) and is **not user-selectable** —
  the reference's 1-bar Lite meter visually implies a step below Balanced, but
  no such render tier exists to select. Flagged in the Stage 1 report.
- No client-side router (MRB-194): one entry point, in-memory specimen state.
- Copy discipline: the only prose in the UI is functional instruction, terse.

## Divergences from the frozen reference (MRB-186 reconciliation, 10 Aug 2026)

Everything above documents the reference as Design drew it, and the reference
stays frozen — including its §07 table and in-situ colour citations. Seven
colours ship differently in `src/styles/tokens.css`, ruled in the MRB-186
Linear thread (Stage 1 report, Finding 1); one token is added and the accent
is applied more narrowly than the reference applies it, ruled in the same
thread (the accent-contrast ruling, below). Wherever this document or the
reference names a value on the left, the app ships the value on the right.

**Adopted canonical.** Design authored the reference before `/design-sync`
existed for this surface, so its palette approximates the MRB-183 KS3 system
by eye. These four are near-misses of real tokens; the canonical value is
what Design was aiming at:

| Reference | Ships as | Token | Canonical source (`shared/tokens.css`) |
|---|---|---|---|
| `#1A140E` | `#1A1714` | `--st-ink` | `--ink` |
| `#6E6255` | `#6E655D` | `--st-muted` | `--ks3-ink-faint` |
| `#E4D6BF` | `#E0D2B9` | `--st-rule` | `--ks3-rule` |
| `#A63A18` | `#A93411` | `--st-accent-text` | `--ks3-accent-text` |

**Darkened for contrast.** The reference's caption tier fails WCAG on the
cream ground at the 10.5–12px sizes it carries text: faint `#9C8E7B` 2.90:1,
ghost `#B0A18B` 2.29:1, caption `#8A7C6B` 3.68:1. Caption is also a
near-miss of canonical `--ink-faint #8A8074`, but the canonical value is
itself 3.81:1, so adoption could not fix it — all three were darkened at the
same hue and saturation until they clear 4.5:1 on both light grounds
(measured on ground `#FBF3E6` / paper `#FFFDF8`):

| Reference | Ships as | Token | Measures |
|---|---|---|---|
| `#8A7C6B` | `#7A6E5F` | `--st-caption` | 4.51:1 / 4.89:1 |
| `#9C8E7B` | `#7B6E5C` | `--st-faint` | 4.51:1 / 4.89:1 |
| `#B0A18B` | `#7D6D55` | `--st-ghost` | 4.55:1 / 4.93:1 |

The ink alpha forms follow the ink adoption: `rgba(26,20,14,…)` ships as
`rgba(26,23,20,…)` — the §04 drawer scrim and the §07 paper-stage hotspot
halo and inert ring. The §07 paper-stage ink fill and ink halo likewise ship
at `#1A1714`.

**The accent is never a small-text partner.** `#E4572E` is a graphic value:
fills, borders, rings, marks, and text at 24px and up. The reference also
stands it opposite text below that — as the fill behind five cream labels,
and once as the label itself — and both directions measure the same 3.62:1,
under the 4.5:1 those sizes need. Mide ruled the pairing out entirely, so
these ship on `--st-accent-text`. The label stays cream, so Design's
light-on-warm relationship is untouched and only the depth of the orange
moves:

| Selector | Role | Size | Reference | Ships as | Measures |
|---|---|---|---|---|---|
| `.cta` | fill behind "Create free account" | 14px | `#E4572E` | `#A93411` | 3.62:1 → 6.48:1 |
| `.btn--primary` | fill behind "Start retrieval" (panel, tablet, phone sheet) | 14.5px | `#E4572E` | `#A93411` | 3.62:1 → 6.48:1 |
| `.rbtn-check` | fill behind "Check" | 15px | `#E4572E` | `#A93411` | 3.62:1 → 6.48:1 |
| `.modeseg .is-on` (retrieve) | fill behind the selected mode | 13.5px | `#E4572E` | `#A93411` | 3.62:1 → 6.48:1 |
| `.structchip.is-open .structchip__num` | fill behind the open numeral | 10px | `#E4572E` | `#A93411` | 3.62:1 → 6.48:1 |
| `.libcard.is-viewing .libcard__meta` | the `VIEWING` caption itself | 10.5px | `#E4572E` | `#A93411` | 3.62:1 → 6.48:1 |

**Links deepen rather than brighten.** The reference's `a:hover{color:#E4572E}`
is the same pairing in the same direction as the `VIEWING` row above — the one
link inheriting it is the phone library's "Create account" at 13.5px, 3.34:1 on
the cream ground. There is no reference value to reconcile here, so this is an
addition rather than a substitution, taking the canonical token the KS3 system
already defines for the role:

| Reference | Ships as | Token | Canonical source (`shared/tokens.css`) | Measures |
|---|---|---|---|---|
| `#E4572E` (`a:hover`) | `#7F2408` | `--st-accent-hover` | `--ks3-accent-hover` | 3.34:1 → 8.83:1 |

The accent is unchanged everywhere it is not a small-text partner: hotspots and
the §07 state table (numerals are marks — identity is size, fill inversion, the
cream ring and the dark halo, pinned by the no-hue-only gate), `.railbtn.is-active`,
`.hatch`, the `.psq--current` ring, the viewing card's border, the chevron mark,
focus rings and the leader line.

Enforced by the parity gate (`3d_parity.py` layer A): the shipped values are
allow-listed there with these reasons, every other token must appear
literally in the reference, and the superseded seven must not reappear
anywhere in `src/` or `.design-sync/previews/`. The accent-contrast ruling
is allow-list entries 15 and 16 there, with the changed selectors asserted at
`#A93411` in layer C and the marks still asserted at `#E4572E`. Contrast is
enforced separately by `tests/gates/contrast.test.ts`, which recomputes ratios
from `tokens.css` on every run and now holds the ruling as a rule — no pair
under 24px may name `--st-accent` on either side — rather than as six
corrected rows.
