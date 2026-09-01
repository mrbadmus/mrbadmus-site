# KS3 design system — the build spec

**This file is what the generator is built against. The frozen HTML beside it is what the build is
checked against.** Where the two disagree, the HTML is evidence of intent and this file is the
ruling; every place they diverge is recorded in §9 with the reason.

## 0. Provenance and authority

Four artifacts from Claude Design, frozen verbatim in this directory on 9 August 2026. Nothing in
them has been tidied, reformatted or corrected — they are evidence.

| File | md5 | What it is |
|---|---|---|
| `KS3 Reference Set (offline).html` | `ba4c98e5feaea46ad4dac59aaa18c666` | The authority. Ten screens: Foundations, Browse layer, Canonical lesson, Block library, Activity kinds, Simulations, States, Families, Stress tests, Rules. |
| `KS3 Parts Library (offline).html` | `9eadbc09bad92b697fe38103adcf5030` | Component states in isolation. |
| `KS3 Mastery Ladder (offline).html` | `53ca56ff963f0b8902a5fd64de4eef58` | The ladder. **Visual reference only — its behaviour is superseded, see §9.2.** |
| `KS3 Simulation (offline).html` | `1baffdd3f9b71b09f58087f9c2a913b1` | The three simulations, six configurations. |

**Order of authority, highest first:**

1. **Mide's rulings on the tickets** — MRB-183 (adopt as KS3-only visual world), MRB-184 comment of
   9 Aug (the ladder), MRB-181 (no platform self-explanation).
2. **`KS3 Reference Set (offline).html`** — the newest and broadest artifact.
3. The other three artifacts, for the components they specialise in.
4. **MRB-183's ticket description.** Superseded on values: it was written from Design's earlier
   five-screen prototype and lists `#231F1C` ink, `#B33A1E` link and a 1240px width. The Reference
   Set ships `#221E1B`, `#A93411` and 1320px. The Reference Set is later and the integration prompt
   independently names its values, so it wins.

**Format of the artifacts.** React prototypes using `x-dc` templating (`sc-for`, `sc-if`,
`dc-import`), styled with inline `style` attributes and **zero CSS classes**. The gas-pressure
lesson's prose is written literally into the markup. This is therefore a **translation** — inline
styles cannot be shared across 183 lessons — and the deliverable is real classes in
`shared/ks3.css` consuming tokens, plus renderers in `build_ks3.py` that emit them.

---

## 1. Colour

Design's own rule, quoted from the Foundations screen: *"Two accents per hue: a **fill** token for
borders, rules, large text and focus rings at 3:1, and a **text** token for body-size type at
4.5:1. Body-size accent text always uses the darker token."*

### 1.1 The eight measured swatches

These are Design's own measurements, carried verbatim as comments in `tokens.css`.

| Token | Hex | Use | Design's measured ratio |
|---|---|---|---|
| Ink | `#221E1B` | All body text | **14.2:1** on cream ✓ AAA |
| Ink muted | `#5F564F` | Secondary text, captions | **5.6:1** on cream ✓ AA |
| Accent fill | `#E4572E` | Borders, rules, focus, large text | **3.4:1** — large text only |
| Accent text | `#A93411` | Accent-coloured body text | **6.0:1** on cream ✓ AA |
| Success fill | `#12A150` | Correct-answer borders and fills | **3.0:1** — never body text |
| Success text | `#0A6B36` | The word "Correct." | **5.9:1** on tint ✓ AA |
| Alert | `#FFC53D` | Misconception blocks only | Ink on top: **11.4:1** ✓ |
| Stretch | `#6B3FD4` | Going further / Need a hand? | Text token `#5A31C0`: **6.4:1** ✓ |

### 1.2 The full palette, as used across the reference set

**Grounds and surfaces**

| Token | Hex | Where |
|---|---|---|
| `--ks3-ground` | `#FBF3E6` | Page background |
| `--ks3-card` | `#FFFCF5` | Panels, cards, block surfaces |
| `--ks3-band` | `#F4E9D8` | Table header bands, secondary buttons, number chips |
| `--ks3-inset` | `#F7EFE1` | Inset panels, criteria list ground, simulation canvas fill |
| `--ks3-row-dim` | `#FBF6EC` | A dimmed row (coming-soon, spent option) |
| `--ks3-rule` | `#E0D2B9` | Hairline rules, row dividers |
| `--ks3-rule-strong` | `#C3B191` | Dashed placeholder frames, stronger dividers |
| `--ks3-option-border` | `#DDCFB6` | Resting answer-button border |

**Ink**

| Token | Hex | Where |
|---|---|---|
| `--ks3-ink` | `#221E1B` | Body text, all 2px outlines |
| `--ks3-ink-body` | `#3B342E` | Slightly softened body copy in panels |
| `--ks3-ink-muted` | `#5F564F` | Captions, meta, eyebrows |
| `--ks3-ink-faint` | `#6E655D` | Dimmed row text |
| `--ks3-on-dark` | `#FBF3E6` | Text on ink-dark blocks |
| `--ks3-on-dark-body` | `#E7DECE` | Body copy on ink-dark blocks |
| `--ks3-on-dark-muted` | `#C6B9A7` | Captions on ink-dark blocks |
| `--ks3-dark-panel` | `#3E3730` | A panel nested inside an ink-dark block |

**Accent (orange) — the platform's own voice, and Chemistry's subject tint**

| Token | Hex |
|---|---|
| `--ks3-accent` | `#E4572E` |
| `--ks3-accent-text` | `#A93411` |
| `--ks3-accent-tint` | `#FCE7DE` |
| `--ks3-accent-link-hover` | `#7F2408` |

**Success (green) — only the ladder marks correctness**

| Token | Hex |
|---|---|
| `--ks3-ok` | `#12A150` |
| `--ks3-ok-text` | `#0A6B36` |
| `--ks3-ok-tint` | `#E4F7EB` |

**Alert (amber) — a wrong idea being confronted, never "you got it wrong"**

| Token | Hex |
|---|---|
| `--ks3-alert` | `#FFC53D` |
| `--ks3-alert-text` | `#5A430A` |
| `--ks3-alert-tint` | `#FFF3D4` |
| `--ks3-alert-border` | `#D9821A` |

**Stretch (violet) — an optional layer the student chose**

| Token | Hex |
|---|---|
| `--ks3-stretch` | `#6B3FD4` |
| `--ks3-stretch-text` | `#5A31C0` |
| `--ks3-stretch-tint` | `#F0EAFC` |
| `--ks3-stretch-rule` | `#D8CBF5` |
| `--ks3-stretch-dash` | `#B9A6E8` |
| `--ks3-stretch-wash` | `#FAF7FF` |

**Physics blue — subject tint, and the cross-reference row**

| Token | Hex |
|---|---|
| `--ks3-blue` | `#2F5CE0` |
| `--ks3-blue-text` | `#2545A8` |
| `--ks3-blue-tint` | `#E1E8FE` |
| `--ks3-blue-light` | `#8FB7FF` |

**Subject identity**

| Subject | Hue |
|---|---|
| Biology | `#12A150` (shares the success hue) |
| Chemistry | `#E4572E` (shares the accent hue) |
| Physics | `#2F5CE0` |

### 1.3 What each colour is allowed to mean

Quoted from the Foundations screen, and binding:

- **Green · verified correct.** Only the mastery ladder marks correctness. Always paired with the
  word "Correct." and a ✓ mark.
- **Amber · a wrong idea being confronted.** Misconception blocks only. *Never* used for "you got it
  wrong" — the student is not the error.
- **Orange · the platform's own voice.** Brand, the big question, chosen answers, focus rings, the
  draft marker. Chemistry also owns it as a subject tint.
- **Violet · optional depth.** "Going further" and "Need a hand?" only. It marks a layer the student
  chose, never a level they were put in.

**Selection is never amber — on either ground.** ⊕ Ruled by Mide, 30 August 2026.

Amber is reserved for warning and loss: a wrong idea being confronted, a caution, a thing given up.
**A colour that means "careful" must not also mean "you picked this."** A student who has learned
across a term that amber means "careful, this is a wrong idea" cannot then meet amber meaning "the
tab you are on" without the first meaning wearing away — and it is the first meaning that is
load-bearing.

So selection takes the **orange accent on both grounds**. On a light ground that is an accent border
over an accent tint, which is what the light branch already did. On an ink-dark ground it is the same
shape read for the dark: the dark panel as the fill, the accent as the border, cream as the label.

⚠️ **The dark treatment is a border and not a slab, and that is arithmetic rather than taste.**
`--ks3-accent` #E4572E is a large-text-only colour, and ink #221E1B measured on an accent fill is
**4.49:1** — under the 4.5:1 body floor. A solid accent slab would ship control labels below AA, so
the amber slab is not simply recoloured; it is re-expressed as a border, which needs only the 3:1 of
WCAG 1.4.11 and clears it (3.18:1 on the dark panel, 4.49:1 on the ink ground behind).

⚠️ **This moves selection only.** It does not move **category** — "this column, not that one", "this
is the field you are looking at" — which stays on `--ks3-data` where MRB-252 put it. Recolouring a
category under cover of this rule is the one way to get it wrong.

Three separate units stopped at this question before it was ruled, which is why it is written here.
It is settled. Do not re-raise it.

---

## 2. Type

Three families. **Bricolage Grotesque** carries every heading; **Instrument Sans** carries every
word a student reads; **DM Mono** carries numbers that change. Nothing on a KS3 page is smaller
than 15px.

Base: **19px / 1.6** for page chrome; lesson prose is **20px / 1.75**.

### The seven-row scale

| # | Row | Family | Weight | Size | Line height | Letter spacing |
|---|---|---|---|---|---|---|
| 1 | Lesson title | Bricolage Grotesque | 800 | `clamp(44px, 6vw, 74px)` | `.94` | `-.035em` |
| 2 | Big question | Instrument Sans | 600 | `25px` | `1.35` | `0` |
| 3 | Block heading | Bricolage Grotesque | 800 | `30px` | `1.2` | `-.025em` |
| 4 | Body | Instrument Sans | 400 | `20px` | `1.75` | `0` |
| 5 | Answer button | Instrument Sans | 600 | `18px` | `1.4` | `0` |
| 6 | Eyebrow | Instrument Sans | 700 | `13px` | `1.4` | `.16em`, uppercase |
| 7 | Live number | DM Mono | 500 | `15px`–`44px` | `1` | `0` |

The big question additionally takes `--ks3-accent-text` and `max-width: 24ch`.
Screen-level `h1` outside a lesson is `clamp(40px, 5.4vw, 66px)` / `.96` / `-.035em`.
Section `h2` on index pages is Bricolage 800 `32px` / `-.025em`.

### Self-hosted fonts (MRB-183 knock-on; see §9.4 on MRB-130)

Five woff2 files in `shared/fonts/`, extracted from Design's own bundle so the bytes are the ones
the reference was designed against. `font-display: swap`, explicit `unicode-range`, preloaded.

| File | Family | Style | Weight axis |
|---|---|---|---|
| `bricolage-grotesque-var-latin.woff2` | Bricolage Grotesque | normal | 400–800 variable |
| `instrument-sans-var-latin.woff2` | Instrument Sans | normal | 400–700 variable |
| `instrument-sans-var-italic-latin.woff2` | Instrument Sans | italic | 400–600 variable |
| `dm-mono-400-latin.woff2` | DM Mono | normal | 400 |
| `dm-mono-500-latin.woff2` | DM Mono | normal | 500 |

`unicode-range` for all five, the Google latin subset:

```
U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304,
U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215,
U+FEFF, U+FFFD
```

**No Google Fonts link, no preconnect.** KS4's Space Grotesk / IBM Plex Sans / IBM Plex Mono keep
loading exactly as they do today and are not touched.

---

## 3. Shape, spacing and measure

| Dial | Value |
|---|---|
| **Reading column (prose)** | `46rem` |
| **Break-out (simulations, card grids, ladder)** | `60rem` |
| **Lesson page container** | `60rem`, centred |
| **Index page container** | `1320px`, padding `44px 24px 90px` |
| Radius — block | `28px` (ink-dark blocks `30px`) |
| Radius — nested panel | `20px` |
| Radius — card | `22px` |
| Radius — control | `14px` |
| Radius — chip / pill | `999px` |
| Radius — focus ring | `6px` |
| Border — anything actionable | `2px solid var(--ks3-ink)` |
| Border — the ladder | `3px solid var(--ks3-ink)` |
| Border — lesson header underline | `3px solid var(--ks3-ink)` |
| Shadow — standard block | `5px 5px 0 var(--ks3-ink)` |
| Shadow — ink-dark block | `6px 6px 0 <accent for that block>` |
| Shadow — card | `4px 4px 0 #E0D2B9` |
| Shadow | **hard offset, no blur, no gradient** |
| Touch target | `44px` minimum on every control |
| Block gap | `28px` between sections |
| Hairline rule | `1px solid var(--ks3-rule)` |

Design's reason for the hard shadow, quoted: *"No blur, no gradient — it renders identically on a
five-year-old Chromebook."*

Design's reason for 46rem, quoted: *"The old 44rem cap applied at 16px; at 19px it produced a
narrow, tiring column."*

### Hover and focus

- Hover on a card or button: `transform: translate(-2px, -2px)` or `translateY(-2px)`, transition
  `.14s`–`.16s`. Answer buttons use `translateX(3px)`.
- **Focus:** `outline: 3px solid var(--ks3-accent); outline-offset: 2px; border-radius: 6px`, on
  every interactive element without exception.

### Motion

| Keyframe | Duration | Used for |
|---|---|---|
| `reveal` | `.22s` | A reveal or criteria list appearing (opacity + 4px slide) |
| `popIn` | `.35s` | The correct option landing (scale .9 → 1.03 → 1) |
| `secIn` | `.4s` | A screen entering |
| `drift` | `2.1–3.4s` alternate | Ambient air particles on the hook — the one decorative loop |

Under `prefers-reduced-motion: reduce`, every animation and transition collapses to `.001ms` and
`scroll-behavior` becomes `auto`.

---

## 4. The canonical lesson, block by block

Lesson container `60rem`; prose sections `46rem`; sections separated by `28px`.

| Order | Block | Surface | Radius | Shadow | Eyebrow | Notes |
|---|---|---|---|---|---|---|
| — | Breadcrumb | none | — | — | — | DM Mono 14px, `--ks3-ink-muted` |
| — | Header | none | — | — | `<unit> · <Family>` | `h1` row 1; big question row 2; draft pill; `border-bottom: 3px solid ink`, `padding-bottom: 28px` |
| 1 | `hook` | **ink dark** `#221E1B` on `--ks3-on-dark` | `30px` | `6px 6px 0 var(--ks3-accent)` | "Start here" in `--ks3-alert` | Two-column at ≥285px: copy + phenomenon figure. Commit question, full-width option buttons with letter badges, then a reveal panel on `--ks3-dark-panel` with a `2px` alert border |
| 2 | `explainer` | none | — | — | — | `46rem`, body row 4 |
| 3 | `figure` (pending) | `--ks3-inset` | `24px` | — | — | `3px dashed --ks3-rule-strong`, `52px 24px`, centred "Diagram coming soon" pill; caption 17px below |
| 4 | `misconception` | `--ks3-alert-tint` | `28px` | `5px 5px 0 ink` | "Think again" in `--ks3-alert-text` | `!` badge 32px, ink ground, alert glyph. The misconception quoted at 22px/700 *italic*. Then the confronting instrument |
| 5 | `keyword` | cards on `--ks3-card` | `22px` | `4px 4px 0 #E0D2B9` | — | Grid `minmax(268px, 1fr)`, gap 16px, min-height 150px. Term Bricolage 800 27px. Accent **dog-ear** top-right. Resting hint "Say it, then tap →" in `--ks3-accent-text` |
| 6 | `practical` | **ink dark** | `30px` | `6px 6px 0 var(--ks3-blue)` | "Investigate" in `--ks3-blue-light` | Heading 34px; instruction line right-aligned; simulation below |
| 7 | `check` | `--ks3-card` | `28px` | `5px 5px 0 ink` | "Your turn · write it" | Prompt as `h2` 28px. Ink "Check your answer" button. Criteria on `--ks3-inset`, `20px` radius, numbered green badges |
| 8 | `quiz` | see §5 | | | | |
| 9 | `summary` (key note) | **ink dark** | `30px` | `6px 6px 0 var(--ks3-alert)` | "Key note" in `--ks3-alert` | Text Bricolage **700** 30px / 1.3 |
| 10 | stretch layer | `--ks3-stretch-tint` | `26px` | — | "Going further" in `--ks3-stretch-text` + `2px` rule | |
| 11 | support layer | — | — | — | — | **R12: when empty, renders nothing at all.** The dashed frame is reference-only |
| 12 | End matter | 4-card grid `minmax(250px, 1fr)` | `22px` | — | — | Before this lesson · Connects to · At GCSE this becomes · **Ask Mr Badmus AI on `--ks3-accent`** |
| 13 | Footer line | none | — | — | — | 15px muted, `border-top: 1px solid --ks3-rule`, `padding-top: 16px` |

**Draft pill:** ⛔ **REVOKED — MRB-221, 16 Aug 2026. Not built, not transcribed.** Design drew an
inline-flex `999px` pill on `--ks3-accent-tint` with a `2px solid --ks3-accent` border,
`--ks3-accent-text` text at 16px/700 and a 9px accent dot. Architecture §5.10.1 is revoked, the
build emits no such element, `.ks3-review-flag` is deleted from `shared/ks3.css`, and `verify_ks3.py`
asserts its absence. The measurement is kept as a record of what Design drew; its wording is not
reproduced, because MRB-221 requires the marker string to return zero hits across the docs.

> This is a transcription, not the archive. The frozen artifacts under `docs/ks3/design-reference/`
> still contain the pill as Design shipped it, and are **deliberately not edited** — they are
> byte-exact provenance whose md5s are recorded in §1 above, and rewriting them to tidy a revoked
> component would destroy the evidence the layer-A gate reads.

**Activity option buttons (all activities):** full width, `min-height: 44px`, radius `16px`,
18px/600, letter badge (A/B/C/D) 28px at radius `9px`. Resting `--ks3-ground` on
`--ks3-option-border`. Chosen: `--ks3-accent-tint` ground, `2px solid --ks3-accent`. **R3: never
green, never red, never disabled.**

---

## 5. The mastery ladder

Visual shell from Design's Mastery Ladder artifact; **behaviour from MRB-184's ruling of 9 Aug**
(see §9.2).

**Shell:** `--ks3-card`, `3px solid ink`, radius `30px`, padding `32px`,
`box-shadow: 6px 6px 0 var(--ks3-ok)`. Header row: `h2` "Mastery ladder" Bricolage 800 36px, a
sub-line, and a right-aligned live score region (`min-width: 220px`, `aria-live="polite"`), over
`border-bottom: 2px solid --ks3-rule`, `padding-bottom: 20px`. Rungs `28px` apart.

**Rung 1 and 2 (page-marked):** `border-left: 4px solid var(--ks3-accent)`, `padding-left: 22px`.
`h3` "1 · Recall" Bricolage 800 23px in `--ks3-accent-text`. Question 21px/600. Options in a
`minmax(250px, 1fr)` grid, gap 11px, radius `15px`, 18px/600, `min-height: 44px`, 27px mark badge.

| Option state | Ground | Border | Badge | Mark |
|---|---|---|---|---|
| Resting | `--ks3-ground` | `--ks3-option-border` | `--ks3-band` / `--ks3-ink-muted` | A B C D |
| Correct (after answering) | `--ks3-ok-tint` | `--ks3-ok` | `--ks3-ok` / white | **✓**, `popIn .35s` |
| Chosen but wrong | `--ks3-band` | `--ks3-ink` | `--ks3-ink` / `--ks3-on-dark` | **✕** |
| Not chosen, spent | `--ks3-row-dim` | `#EBDFCB` | `--ks3-band` / `#9A8F86` | letter, `--ks3-ink-faint` |

Feedback line: `role="status"`, 19px, radius `15px`, `14px 18px`. Correct → the word "Correct." on
`--ks3-ok-tint` / `2px --ks3-ok`. Wrong → that option's own written correction on `--ks3-band` /
`2px --ks3-ink`.

**Rung 3 and 4 (self-marked):** `border-left: 4px solid var(--ks3-stretch)`, `h3` in
`--ks3-stretch-text`. Per MRB-184:

1. A **labelled `<textarea>`** and nothing else. The criteria are not on the page yet.
2. Below it a **"Check my answer"** button (`--ks3-band`, `2px solid ink`, radius `14px`, 17px/700,
   `min-height: 44px`).
3. Pressing it reveals the numbered criteria, **each with a real `<input type="checkbox">`**.
4. The rung counts as met **only when every criterion is ticked**. Partial reads
   **"2 of 4 ticked — not yet"** — honest, never a failure.
5. Criteria rows: numbered badge 25px, radius `8px`, `--ks3-ok-tint` on `2px --ks3-ok`, number in
   `--ks3-ok-text`; text 19px/1.55.

**Score:** out of **4**. Line reads e.g. *"You got 3 of 4."* with one small line naming who marked
what: *"You marked rungs 3 and 4 yourself."* Live region.

**Retry my misses:** ink button, radius `14px`, 18px/700, above `border-top: 2px solid --ks3-rule`.
Reopens missed rungs **including self-marked ones** — clears the ticks, **keeps the written
answer**, and moves focus to the first reopened rung.

**Storage:** a **new** key (`ks3_ladder4_<slug>`) holding best-out-of-four, plus the written answers
and tick state per lesson. The old out-of-two key is left alone and never compared against the new
scale.

---

## 6. The simulations

Canvas fill `--ks3-inset`. Particles `--ks3-accent`; the second diffusion population
`--ks3-blue`. Wall/piston in `--ks3-ink`. Diffusion centre line: `2px` dashed
`--ks3-rule-strong`, dash `[6, 6]`.

Populations, from Design: `particle-states` **64**, `gas-pressure` **90**, `diffusion` **120** (60
per side). Particle radius 4.4px, except `particle-states` which sizes from a 16 × 4 lattice cell.

### R18 — one model drives both readings

Anchored at **100 kPa with every slider at default**, scaling by the gas law:

```
factor   = (particles / 100) × (kelvin / 300) × (100 / space)
pressure = 100 kPa × factor
wall hits per second = factor × 60
```

The two figures are computed from **the same factor**, so they cannot drift apart. Particle speed
is driven from **absolute temperature** for the same reason.

**Units toggle:** kPa / Pa / N/m², default **kPa**. `N/m²` is the KS3 statutory phrasing and keeps
force-per-area visible.

### R19 — each simulation shows temperature differently

| Simulation | Slider maps | Displays | Why |
|---|---|---|---|
| `gas-pressure` | 0–100 → **100 K – 500 K** | **°C computed from kelvin**: −173 °C, **27 °C at default**, 227 °C | Pressure is proportional to *absolute* temperature. Scaling in Celsius is the classic error and would make every pressure figure wrong. |
| `diffusion` | 0–100 → **0 °C – 100 °C** | °C | The range a real school experiment spans; an INVESTIGATION lesson cannot record a result against "warm". |
| `particle-states` | 0–100, unlabelled | **No number at all** — words only, plus a **solid / liquid / gas band strip** under the slider | A Celsius reading would imply a melting and boiling point for a model that names no substance. The band strip makes the changes findable by dragging. |

### The sanity table — must hold exactly

| Condition | Expected pressure |
|---|---|
| All sliders at default | **100 kPa** |
| Half the space | **200 kPa** |
| Double the particles | **200 kPa** |
| Hot end of the slider (500 K) | **167 kPa** |
| Half space **and** hot end | **333 kPa** |

### Locked state — R5

Blur `2px`, desaturate to `65%`, veil **the canvas area only**, hide the control panel entirely,
**keep the caption fully readable** (it holds the instructions for the prediction). One frozen frame
is drawn behind the veil so the student can see something real is waiting.

### Reduced motion — R6

No animation loop. Settle internally for **1,400 steps**, draw one representative frame that matches
the current sliders, and let the written readout carry the entire result. **Every control change
re-settles from scratch.**

---

## 7. The browse layer

Seven levels. Container `1320px`. Cards `2px solid ink`, hard offset shadow, hover lift.

| Level | Page | Cards | Shadow colour |
|---|---|---|---|
| L0 | Site chooser | Key Stage 3 (on `--ks3-accent`) / GCSE (on `--ks3-card`), Bricolage 800 36px | `5px 5px 0 ink` |
| L1 | KS3 landing | 3 year cards + 3 subject cards | `5px 5px 0 ink` / `4px 4px 0 <subject hue>` |
| L2 | Year | 6 half-term cards, season-tinted, 42px numbered tile | `5px 5px 0 ink` |
| L3 | Half term | 3 subject cards with a hue dot | `5px 5px 0 <subject hue>` |
| L4 | Lesson rows | unit-grouped rows | — |
| B2 | Subject hub | unit cards | `4px 4px 0 <subject hue>` |
| B3 | Unit index | lesson rows in a bordered list | — |

**Row states**, and every one carries a word as well as a colour (R2):

| State | Ground | Badge |
|---|---|---|
| Written | `--ks3-card` | none |
| Draft | `--ks3-card` | "Draft" — `--ks3-accent-tint` / `2px --ks3-accent` / `--ks3-accent-text` |
| Coming soon | `--ks3-row-dim`, text `#5F564F` | "Coming soon" — `--ks3-band` / `2px --ks3-rule-strong` |
| Cross-reference | `--ks3-card`, number tile `--ks3-blue-tint` / `2px --ks3-blue` | "from P4" — blue tint, plus the pointer sentence |

**Cross-reference pointer, verbatim and load-bearing (R13):** *"Taught in Physics — Forces and
their effects. You'll meet the full lesson there."* It says **where**, never **when**.

**Season tints:** autumn → `--ks3-accent`, spring → `--ks3-ok`, summer → `--ks3-blue`.

---

## 8. The rules — R1 to R19, verbatim

Design shipped **nineteen** rules, `R1`–`R19`. There is no R20; see §9.1. Each carries Design's own
classification: **Build-checkable**, **Design ruling**, or **Flagged for Mide**.

> **R1 · Two tokens per hue, never one** — *Build-checkable*
> Every accent exists twice: a fill token for borders, rules, focus rings and text above 24px, and a darker text token for anything at body size. The orange fill (#E4572E) measures 3.4:1 on cream and must never carry body text; #A93411 measures 6.0:1 and is the only orange allowed under 24px. The same split applies to green. This is the single most common way an accessible palette gets broken at integration.

> **R2 · Colour is never the only signal** — *Build-checkable*
> Correct carries a ✓ and the word "Correct."; wrong carries a ✕ and its own written correction; draft carries the word "Draft"; the cross-reference row carries the word "Taught in". Every state survives being printed in greyscale.

> **R3 · Activity buttons never mark correctness** — *Build-checkable*
> Only the mastery ladder marks right and wrong. An activity button takes an accent border and an accent wash to show it was chosen, stays enabled, and unhides the reveal. Green and red must not appear on an activity button — if they do, the student reads the whole page as a test, and the point of committing before revealing is lost.

> **R4 · The dog-ear is the affordance** — *Build-checkable*
> A flip card is identified as interactive by an accent dog-ear in its top-right corner, and by nothing else. When the card opens the dog-ear is removed, because there is no longer anything underneath. No hover reveal, no auto flip, one tap flips one card.

> **R5 · The locked simulation is blurred, not hidden** — *Build-checkable*
> Blur 2px and desaturate to 65%, veil the canvas area only, hide the control panel entirely, and keep the caption fully readable — the caption holds the instructions for the prediction. One frozen frame is drawn behind the veil so the student can see there is something real waiting.

> **R6 · Reduced motion is a complete experience** — *Build-checkable*
> Simulations settle internally for 1,400 steps and draw one representative frame that matches the current sliders; every control change re-settles from scratch. The written readout carries the entire result. No information anywhere on a KS3 page exists only in motion.

> **R7 · Motion only where motion is the meaning** — *Design ruling*
> Particles travel; states change by movement. Everything else is a 140–220ms fade with a 4px slide, and nothing loops. The ambient drift on the marshmallow hero is the one decorative exception, and it is the phenomenon itself rather than an effect on top of it.

> **R8 · Write, then check, then mark** — *Design ruling*
> Rungs 3 and 4 open on a text area and nothing else — the criteria are not on the page until the student presses Check my answer, so the answer cannot be read before it is attempted. The rung is met only when every criterion is ticked; a partial reads "2 of 4 ticked — not yet" and never as a failure. All four rungs count, the score reads out of 4, and Retry my misses reopens a self-marked rung with the written answer kept.

> **R9 · predict-then-reveal is not a distinct kind** — *Flagged for Mide*
> It carries an identical key set to predict and renders identically. It is an authoring label, not a component. Recommend collapsing it in the data model rather than in the stylesheet.

> **R10 · Per-option feedback on activities is worth adding** — *Flagged for Mide*
> The data already records which option is correct, but activities never use it. Every wrong answer on the ladder carries its own written correction, and that is the most valuable thing on the page. Recommend extending the same authoring field to activity options — a wrong prediction is the single best moment to say something specific. This would need Mide's ruling, because it changes what an activity is.

> **R11 · The reading column is 46rem, not 44** — *Design ruling*
> At 19px base, 44rem gives a cramped measure and forces a five-line paragraph where three would do. Prose sits at 46rem; simulations, card grids and the ladder break out to 60rem. The break-out is what stops a long page feeling like a column of receipts.

> **R12 · An empty layer leaves no gap** — *Build-checkable*
> The support slot is required on every lesson and empty on all six. When empty it renders nothing at all — no heading, no rule, no placeholder. The dashed frame shown on the canonical lesson exists only in this reference set.

> **R13 · Where, never when** — *Build-checkable*
> A cross-reference says "Taught in Physics — Forces and their effects". It must never say a year, a term or a position, because a school teaching a different order would be told something false, and lesson pages must regenerate byte-for-byte when the browse order changes.

> **R14 · The page never explains itself** — *Build-checkable*
> No methodology notes, no reassurance about sequencing, no family glosses. Kept: the draft marker, the Coming soon tag, the cross-reference pointer, the browse-route invitation and the KS3/GCSE helper line — each answers a question the reader is actually holding. Anything legal or safeguarding sits small at the bottom edge, never as a callout.

> **R15 · Every control is a real control** — *Build-checkable*
> Buttons are `<button>`, sliders are `<input type="range">` with accent-color set, the medium picker is a `<select>`. Nothing is a clickable div. Focus is a 3px accent outline at 2px offset, and it is visible on every one of them.

> **R16 · A hook is a phenomenon and it gets paid off** — *Design ruling*
> The hook opens on something observed, ends in a committed answer, and the same phenomenon returns before the ladder for the student to explain in full. The marshmallow opens Gas pressure and the marshmallow closes it. Never leave a Year 7 to infer the link.

> **R17 · PROCESS lessons need a stepper** — *Flagged for Mide*
> The longest lesson in the system is a PROCESS lesson at 17 blocks, and it currently renders as a flat stack. A mechanism that unfolds in steps should look like it unfolds. This is a real gap, not a styling preference — flagged for the build rather than solved here, because it changes the block sequence.

> **R18 · One model drives both pressure readings** — *Design ruling*
> The gas simulation is anchored at 100 kPa with every slider at its default and scales by the gas law from there: particles ÷ 100 × kelvin ÷ 300 × 100 ÷ space. Wall hits per second is that same factor × 60, so the two figures are locked and can never drift apart. Particle speed is driven from absolute temperature for the same reason. Units toggle between kPa, Pa and N/m² — N/m² is the KS3 statutory phrasing and keeps force-per-area visible.

> **R19 · Temperature is shown differently by each simulation** — *Design ruling*
> Gas pressure reads °C computed from kelvin — −173 °C to 227 °C, 27 °C at default — because pressure is only proportional to absolute temperature and scaling in Celsius is the classic way to get this wrong. Diffusion reads 0 °C to 100 °C, the range a real school experiment spans, because an INVESTIGATION lesson cannot record a result against "warm". Particle states carries no number at all: a Celsius reading would imply a melting and boiling point for a model that names no substance. Its slider gets a solid / liquid / gas band strip instead, so the changes are findable by dragging.

### Which rules are in scope this run

| In scope, implemented | Out of scope, by instruction |
|---|---|
| R1–R8, R11–R16, R18, R19 | **R10** (per-option activity feedback) — needs Mide's ruling |
| **R9** — collapsed in the data model, as recommended | **R17** (PROCESS stepper) — changes the block sequence |

---

## 9. Translation decisions and divergences

Every place this spec departs from a literal reading of the artifacts, with the reason.

### 9.1 There is no R20

The integration prompt asks for "the twenty numbered rules R1 to R20". Design shipped **nineteen**.
Verified by extracting the rules array from all four artifacts: ids run `R1` … `R19`, and the string
`R20` appears nowhere in any of the four files. All nineteen are carried verbatim in §8.

### 9.2 The ladder artifact's behaviour is superseded, its look is not

Design's `KS3 Mastery Ladder (offline).html` still implements the **old** behaviour: it scores
`"You got N of 2 marked rungs."`, rungs 3 and 4 are a collapsed "Mark your answer against this
list" disclosure with no text area and no tick controls, and `canRetry` can only ever be true for
rungs 1 and 2. Design independently arrived at MRB-184's *option 2* and labelled the component
*"Four rungs. Two the page marks, two you mark."*

MRB-184 was ruled **option 1** on 9 August, after that artifact was exported. The ruling says
plainly: *"Design's Mastery Ladder artifact is the visual reference; this ruling changes its
behaviour, not its look."*

So: **the ladder is built to §5, not to the artifact.** The parity gate must not assert the
artifact's score string or its rung-3/4 structure — see §9.5.

### 9.3 ✓, ✕ and → are drawn, not typed

The five latin woff2 subsets — Design's own font bytes — do **not** contain `→` (U+2192), `✓`
(U+2713) or `✕` (U+2715). Confirmed by reading the `cmap` of each file: 208–226 glyphs each, all
three absent. Google's latin subset includes U+2191 and U+2193 but skips U+2192.

Design's system depends on all three: `→` in every call-to-action and card hint, and `✓`/`✕` as the
ladder's option marks — which R2 makes load-bearing, since colour must never be the only signal.
Typed as characters they fall back to a system font, and inside a 27px Bricolage-800 badge that is a
visible defect, not a subtlety.

**Resolution: all three are emitted as inline SVG paths using `currentColor`.** This keeps R2
satisfied with a real mark, keeps the marks metrically consistent with the badge, and removes a
webfont dependency the subset cannot honour. It is the same defect class MRB-130 exists to fix,
found again in the new fonts, and fixed at the point of use rather than by shipping a wider subset
we do not have the upstream files to build.

### 9.4 MRB-130 is not closed by this run, and cannot be

The integration prompt describes MRB-130 as "self-host Bricolage Grotesque, Instrument Sans and DM
Mono". That is **not what MRB-130 is.** The ticket is *"Self-host Space Grotesk / IBM Plex Sans /
IBM Plex Mono"* — the three **KS4** families currently pulled from Google Fonts by
`generate_site_v5.py`, with a hard acceptance criterion that the subsets must include U+2070–U+209C
so that the chemistry super/subscripts on 19 of the 23 bonding pages stop falling back.

Those are KS4 fonts on KS4 pages. Doing MRB-130 would change `generate_site_v5.py` and the rendered
bytes of every `.rd` bonding page — which **directly contradicts Phase 2's own hard test** that KS4
pages differ only by their cache-bust stamp, and contradicts the instruction that "KS4's Space
Grotesk and IBM Plex are unaffected and must keep loading exactly as they do".

So this run does the job the prompt operationally asked for — self-hosting the three **KS3** fonts,
no Google Fonts link, which is MRB-183's own knock-on — and leaves MRB-130 open. The KS3 font work
is recorded on MRB-183. MRB-130 keeps its real scope and gets a comment explaining why it was not
closed here.

### 9.5 What the parity gate can and cannot assert

Recorded here because it is a property of the artifacts, not a shortcut:

- The artifacts are React prototypes with **zero CSS classes** and one hardcoded lesson. They will
  never be byte-comparable to generated HTML, so the gate compares **resolved computed style** per
  component against the reference's values, within a stated tolerance.
- The **ladder** is excluded from behavioural parity by §9.2 and gated on §5 instead.
- The **hook's marshmallow illustration** is bespoke artwork for one lesson, hand-built from 12
  positioned drifting spans and a scaling marshmallow. It is not a generator component and cannot be
  produced from lesson data. The generator emits the hook's structure, copy, commit question and
  reveal; the bespoke illustration is not reproduced and is reported rather than faked.
- Design's `dc-import` boundaries mean the reference renders the ladder and simulations in nested
  iframes at fixed heights. Parity is asserted against the component's own resolved styles, not
  against the iframe box.
