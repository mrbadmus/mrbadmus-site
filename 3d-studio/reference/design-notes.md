# 3D Studio shell — design notes extracted from the frozen reference

Source: `3d-studio/reference/shell-v1.html` (Claude Design, frozen under MRB-186 —
never edit it). Every annotation block in the reference is reproduced here as a
checklist item; these are binding intent, not decoration. Check an item only when
the build genuinely satisfies it.

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

## Rulings applied on top of the reference (Linear beats reference where they touch)

- Quality options map Ultra→A, High→B, Balanced→C, **Lite→C**. Tier D is the
  capability floor (no WebGL ⇒ flat renderer) and is **not user-selectable** —
  the reference's 1-bar Lite meter visually implies a step below Balanced, but
  no such render tier exists to select. Flagged in the Stage 1 report.
- No client-side router (MRB-194): one entry point, in-memory specimen state.
- Copy discipline: the only prose in the UI is functional instruction, terse.
