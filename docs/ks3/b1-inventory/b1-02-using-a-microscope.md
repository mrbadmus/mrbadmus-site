# B1 L2 · Using a microscope · INVESTIGATION

Inventory of `docs/ks3/design-reference/b1/b1-02-using-a-microscope.dc.html` (1,003 lines, delivered
unmodified). Method, viewports, generator vocabulary and standing law: see `README.md` in this
folder — not restated here. Cross-page value collisions: `00-delivery-drift.md`. Everything b1-01
established that is true of all six pages is **confirmed, not re-derived** — see
`b1-01-life-processes.md` §1.1, §1.3, §2.2, §2.3, §6 and the citations below.

Measured 13 Aug 2026 in headless Chrome via `ks3_browser.py`, serving
`docs/ks3/design-reference/b1/` over HTTP, at **1280 · 1340 · 820 · 390** with
`page.set_viewport(w, h)` (`Emulation.setDeviceMetricsOverride`). Two extra widths were probed where
the page needed them: 360 (overflow, finding F7) and the 1339/1340 and 544/545 bisections. Every
number below was read from `getComputedStyle` / `getBoundingClientRect` in that browser, or out of
the file's own source. Where a value could not be measured it says so.

⚠️ **Settle discipline, learned the hard way on this page.** The DC runtime defers its style recalc,
and `.ks3-option` carries `transition: border-color .16s`. A 450ms settle — enough on b1-01 — read
the **pre-transition** border colour here and produced a false "the chosen dark option never changes
border". Every state below was re-measured with a forced reflow (`void document.body.offsetHeight`)
plus a 700ms settle, after which the chosen hook option resolves correctly to `--ks3-alert`. Recorded
because the same trap will produce false parity failures in the build run.

⚠️ **Console is NOT clean.** Four errors at load, at every viewport:
`Error: <rect> attribute x: Expected length, "{{ coverX }}"` and the same for `y`, `width`,
`height`. SVG geometry attributes are typed and reject the DC placeholder during the pre-hydration
parse. After hydration the rect carries real values (`x=62 y=62 w=136 h=52`, measured), so nothing is
visually wrong — but this is the only place on the page where Design's own toolchain cannot express a
binding, and it is a note about the **formula triangle** specifically. Finding F1.

**Content payload lives in the file's `<script data-dc-script>` block** and must be lifted
**byte-identical** from these lines, not retyped: `RAIL` 497–504 · `RAIL_SHORT` 506 · `isDone`
508–516 · `METHOD` 518–537 · `WORKED` 539–544 · `MY_FIELDS` 546–551 · `MY_CRITERIA` 553–558 ·
`OBJECTIVES` 560–564 · `LAYERS` 566 · `RUNGS` 568–589 · `SELF_RUNGS` 591–616 · `coverBoxes` 737–741 ·
`coverText` 742–746 · `hookOptions` 852–856 · `coverButtons` 891–894 · `modelLines` 931–936 ·
`labPredictOptions` 951–954 · `sharpnessNote` 975–979. Static prose: header 69–71, hook 79–80,
figcaptions 87 + 93, commit 98, hook reveal 111, method intro 120, **formula statement 149**,
triangle eyebrow/heading 153–154, triangle closing line 174, KEY FACT 182–183, worked heading 188,
yours heading/intro 215–216, lab heading/aside 257–259, veil 266, lab commit 273, table-complete
reveal 351, misconception 364–366, `.ks3-fifa` 388–391, keynote 448–449, stretch 458, endmatter
462–484, safety line 486.

**1,139 words live in the data constants** (181 string literals, counted per constant in §3.6);
**951 words are in the DOM at rest** and **1,571 with every stage revealed** — see §3.6 for the
per-block breakdown, which is the number MRB-205 needs.

---

## 1. Page skeleton

### 1.1 The spine

b1-01 §1.1's finding holds exactly: `.rd` is a **DIV, not `<body>`**, so `shared/ks3.css`'s
`body.rd[data-mode="ks3"]` page-shell rule does not match, and Design compensates with the same 8
inline declarations on the div — byte-identical to b1-01's (source line 23; measured
`background #FBF3E6`, `color #221E1B`, `--ks3-font-body`, `19px`, `line-height 30.4px`,
`min-height 100vh`, `antialiased`, `text-wrap: pretty`). All 60 `--ks3-*` tokens resolve normally
because the token block is `.rd[data-mode="ks3"]` (no `body`). **Nothing for the generator to
change**; recorded again only so a parity probe reading inline styles knows where they are.

One structural difference from b1-01's account: `<body>` here holds **two** children — `div#dc-root`
(the runtime mount, no class) and the logic `<script>`. `<x-dc>` is gone from the DOM by the time
anything is measurable, and `.ks3-lesson` is unique (`document.querySelectorAll('.rd').length === 1`,
measured). No hidden template copy to mis-select.

`.rd` children, in order (5 top-level landmarks — same five as b1-01):

| # | Element | Position | Height 1280 |
|---|---|---|---|
| 1 | `nav.ks3-nav` | static | 63.19 |
| 2 | `nav[data-rail="top"]` | **sticky, top 0, z-index 20** | 46.59 |
| 3 | `nav[data-rail="side"]` | **fixed, top 150px, left calc(50% − 632px), width 104px, z-index 20** | 0 (`display:none` <1340) |
| 4 | `main.ks3-main` | static | 8398.28 |
| 5 | `footer.ks3-footer` | static | 107.59 |

### 1.2 The measure

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| `.ks3-main` width | 1280 | **1320** (capped, margin-left 10px) | 820 | 390 |
| `.ks3-main` max-width | 1320px = `--ks3-page` | same | same | same |
| `.ks3-main` padding | 44px 24px 90px | 44px 24px 90px | 44px 24px 90px | **28px 16px 64px** |
| `.ks3-lesson` width | **960** | **960** | 772 | 358 |
| `.ks3-lesson` max-width | 960px = `--ks3-wide` (60rem) | same | same | same |
| document height | 8616 | 8569 | 8851 | **11908** |
| document `scrollWidth` | 1280 | 1340 | 820 | **405 — 15px wider than the viewport** ⚠ |

Narrow breakpoint re-verified by bisection: `.ks3-main` padding and `.ks3-block` padding change
between **545 (wide) and 544 (narrow)** — `@media (max-width: 34rem)` in `shared/ks3.css`. **The page
adds exactly one media query of its own** — `@media (min-width: 1340px)` for the rail swap (source
line 19). No `prefers-reduced-motion` query, because there is no animation to suppress: measured
`data-motion = null` on `.rd` and **0 `[data-anim]` elements**. So b1-01's motion toggle (its G13)
does **not** recur here, and neither does the `prefers-reduced-motion` desync (its behaviour 2).

The 390 `scrollWidth` overflow is the recording table. Finding F7, §8.

### 1.3 Header carries the lesson trail INLINE — confirmed, and it wraps later here

Structure, classes, colours, gap and type are byte-identical to b1-01 §1.3 (brand tile 34×34
`--ks3-accent` r10 + chevron, 2×26 `--ks3-rule` divider at `margin 0 20px`, `ol` 17px/22.1px gap 9px,
`a.ks3-nav-link` "KS3" 16px/700 `--ks3-accent-text`, 7 `<li>` = 4 crumbs + 3 `›`, last crumb
`aria-current="page"` `--ks3-ink-muted` 500). **b1-01's finding F1 — Design's inline trail vs the
generator's separate mono `nav.ks3-crumbs` row — applies unchanged and is not re-argued here.**

What differs is only the trail's length, and it changes the nav's height profile:

| | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| breadcrumb `<ol>` width | 495.02 | 495.02 | 495.02 | 342 |
| breadcrumb `<ol>` height | 22.09 | 22.09 | **22.09** | **53.19** (2 rows) |
| `nav.ks3-nav` height | 63.19 | 63.19 | **63.19** | **153.97** |

Trail tail is "Using a microscope" against b1-01's "Life processes and what living things are made
of", so the `<ol>` is 229px narrower and **does not wrap at 820** — b1-01's nav grew to 94.78 there,
this one stays 63.19. At 390 it wraps to 2 rows (nav 153.97) where b1-01 took 3 (176.06). Consequence
for F1: **the nav's height is a function of the lesson title's length**, so any layout that depends on
it (the sticky rail sits directly under it) varies per lesson. Worth stating in F1's resolution.

### 1.4 Lesson body, document order (14 direct children of `.ks3-lesson`)

| # | Element | id | classes | margin-top | scroll-margin-top | h 1280 | h 390 |
|---|---|---|---|---|---|---|---|
| 1 | `header` | — | `ks3-lesson-head` | — | — | 322.19 | 356.16 |
| 2 | `section` | `s-hook` | `ks3-block ks3-dark ks3-hook` | 28px | 92px | 898.56 | 1334.06 |
| 3 | `section` | `s-method` | `ks3-block` | 28px | 92px | 779.44 | 1173.91 |
| 4 | `section` | `s-formula` | **none** | 28px | 92px | 590.27 | 972.39 |
| 5 | **`div`** | — | **none** | **24px** | none | 97.48 | 156.86 |
| 6 | `section` | `s-worked` | `ks3-block` | 28px | 92px | 606.47 | 738.47 |
| 7 | `section` | `s-yours` | `ks3-block` | 28px | 92px | 757.19 | 879.58 |
| 8 | `section` | `s-lab` | `ks3-block ks3-dark ks3-practical` | 28px | 92px | 784.75 | 770.8 |
| 9 | `section` | `s-think` | `ks3-block ks3-misconception` | 28px | 92px | 319.95 | 516.69 |
| 10 | `section` | `s-ladder` | `ks3-ladder` | 28px | 92px | 1898 | 2845.2 |
| 11 | `section` | `s-keynote` | `ks3-block ks3-dark ks3-keynote` | 28px | 92px | 248 | 290.31 |
| 12 | `section` | — | `ks3-layer` | 34px | — | 189.69 | 415.77 |
| 13 | `div` | — | `ks3-endmatter` | 34px | — | 354.8 | 617.28 |
| 14 | `p` | — | `ks3-legal` | 34px | — | 39.5 | 62 |

Row 5 is the KEY FACT box, and it repeats b1-01's structural oddity exactly: **an unclassed, un-id'd
`<div>` between two sections**, source lines 181–184, indented two spaces deeper than its siblings
with a blank line at 179–180 where a `</section>` would sit. Not a section, no anchor, not addressable
by the rail. Same on two pages now, so it is a pattern in the hand-authoring rather than a one-off.

Row 4 is a `<section>` with **no class at all** that holds two independently-shelled panels — the only
row on the page where one `<section>` renders two blocks. See §3.2.

`class` audit of the template: **68 distinct class names — 67 `ks3-*` plus `rd`. Exactly one
(`ks3-hook-h`) exists nowhere in `shared/ks3.css`** and is inert (that `<h2>` is styled by
`.ks3-hook h2`) — the same single dead class b1-01 carries. Everything else resolves against the
shipped stylesheet. Beyond the classes the page carries **124 inline `style=` attributes** and **12
JS-built style-string keys** (`cellStyle`, `chipStyle`, `letterStyle`, `lineStyle`, `linkStyle`,
`methodBtnStyle`, `numStyle`, `railBarStyle`, `style`, `textStyle`, `verdictStyle`, `workedBtnStyle`),
plus 21 `<sc-if>` and 15 `<sc-for>` bindings.

**Three vocabulary types the page never renders**: `.ks3-explainer` (0 occurrences), the keyword
flip-card grid (0), and a standalone `figure` block (0). The two figures on this page live **inside the
hook**. The authored record declares two `explainer` blocks, a `keyword` block and three `figure`
blocks — none of which appears. Finding, §8(b).

---

## 2. The progress rail — same component as b1-01, six stages instead of four

Both variants are byte-for-byte the shape b1-01 §2.2 and §2.3 specify. Confirmed by measurement here,
not re-derived: threshold bisected at **1339 → side hidden / top shown; 1340 and 1341 → the reverse**
(same two authored rules, source lines 18–19, byte-identical); side rail `fixed / top 150px /
left calc(50% − 632px) → 38px / width 104px / z-index 20`; chip **32×32 r10 Bricolage 16px/800
border 2px**; chip current `box-shadow 0 0 0 4px --ks3-accent-tint`, chip future border
`--ks3-rule-strong` + colour `--ks3-ink-ghost`; label **MONO 11px/500 ls .99px uppercase lh 13.2px**;
connector **2×20 margin 7px 0**, `--ks3-accent` when done else `--ks3-rule`; link `gap 7px padding
2px 0`. Top bar `sticky top 0 z-index 20`, `--ks3-ground`, `border-bottom 2px --ks3-rule`,
`padding 9px 16px 10px`, inner flex `gap 12px max-width 60rem`, count MONO 15px/500
`--ks3-ink-muted`, current label 16px/700 with `overflow:hidden; text-overflow:ellipsis;
white-space:nowrap`, track `flex 0 0 96px` height **8px** r99 `--ks3-band` on `2px --ks3-ink`, fill
`--ks3-accent`. Same dead `railFillHeight` is absent here (the page does not compute one).

### 2.1 What is different: six stages, and every one of them can tick

| # | anchor | side label (`RAIL_SHORT`) | top-bar label (`RAIL[].label`) | `done_when` (source 508–516) |
|---|---|---|---|---|
| 1 | `#s-hook` | HOOK | Two photographs | `s.hookChoice !== null` |
| 2 | `#s-method` | METHOD | Sam's method | `!!s.methodOpened` |
| 3 | `#s-worked` | WATCH | Watch it done | `s.workedStep >= 4` |
| 4 | `#s-yours` | YOU | Now you | `!!s.mineChecked` |
| 5 | `#s-lab` | BENCH | The bench | `(s.recorded \|\| []).length >= 3` |
| 6 | `#s-ladder` | LADDER | Mastery ladder | `r1 !== null && r2 !== null && checked.r3 && checked.r4` |

Two label sets again, neither derivable from the block titles. Stage-1 count text `"1 / 6"`, fill
`(active+1)/6` → measured **15.33px of 92px** at stage 1 (the 96px track less its 2px borders).

**All six predicates are reachable** — driven and confirmed one at a time:
`marks = [T,F,F,F,F,F]` after one hook click; `[T,T,…]` after "Open the steps I picked";
`marks[2]` after the fourth worked step; `marks[3]` after "Check my working"; `marks[4]` after the
third recorded row; `marks[5]` after both self-rungs are checked. **b1-01's finding F3 — a rail stage
whose predicate can never fire — does not recur on this page.** That is worth stating positively: the
`done_when` shapes here are all "a state the block already owns", which is what §2.6 of b1-01 asks
for.

Two of them are looser than they read, and both are consequences of defects further down:

- **Stage 4 (`YOU`) ticks on an empty submission.** `mineChecked` is set by the Check button, which
  works with all four fields blank (§4 behaviour 11, F5). So the rail can read "you did the
  calculation" for a student who wrote nothing.
- **Stage 2 (`METHOD`) ticks on one pick.** `methodOpened` needs `pickedCount > 0`, so tapping any
  one of the six steps and pressing Open completes the stage. That is arguably right — the block's own
  progress text is "Pick at least one" — but it means the stage does not mean "critiqued the method".

### 2.2 Completion vs scroll — b1-01's F2 reproduced on six stages

Driven with `scrollIntoView` at each of the nine id-bearing anchors on a fresh load, interacting with
nothing:

| scrolled to | count | fill | current label | side marks |
|---|---|---|---|---|
| `#s-hook` | 1 / 6 | 16.6667% | Two photographs | all false |
| `#s-method` | 2 / 6 | 33.3333% | Sam's method | all false |
| `#s-formula` | 2 / 6 | 33.3333% | Sam's method | all false |
| `#s-worked` | 3 / 6 | 50% | Watch it done | all false |
| `#s-yours` | 4 / 6 | 66.6667% | Now you | all false |
| `#s-lab` | 5 / 6 | 83.3333% | The bench | all false |
| `#s-think` | 6 / 6 | 100% | Mastery ladder | all false |
| `#s-ladder` / `#s-keynote` / page bottom | 6 / 6 | 100% | Mastery ladder | all false |

So the <1340 variant reads **6 / 6 with a full accent bar for a student who has answered nothing** —
b1-01's F2, measured again, on the variant every student under 1340px gets. Not re-argued; the extra
datum this page contributes is that `#s-formula` (a real, anchored section that is **not** a rail
stage) leaves the count on the previous stage, which is the correct behaviour of the observer and
confirms the rail's stage list is authored, not derived from the sections present.

### 2.3 Anchors

**Nine elements carry `scroll-margin-top: 92px`** — every `<section>` with an id (`s-hook`,
`s-method`, `s-formula`, `s-worked`, `s-yours`, `s-lab`, `s-think`, `s-ladder`, `s-keynote`), authored
individually as an inline style on each (9 occurrences in source). The rail references **6 of the 9**.
The KEY FACT div, `.ks3-layer`, `.ks3-endmatter`, `.ks3-legal`, the four `#my-*` inputs, the two
`#ans-r*` textareas and `#dc-root` carry none. Value confirmed by driving it: clicking the side rail's
BENCH link at 1340 puts `#s-lab` at **top: 91.78px** with `location.hash = "#s-lab"`.
`scroll-behavior` resolves to `auto`.

### 2.4 What the generator needs to emit it

The `rail` field b1-01 §2.6 proposes covers this page unchanged — six entries instead of four, the
same four keys, `len(rail)` driving the count and the fill. Nothing new. The one addition this page
argues for is a **validation rule**: every `done_when` must name a state the block owns *and* that
state must not be settable without the student producing something. Stage 4's `mineChecked` fails the
second half today.

---

## 3. Every block in document order

`GEN?` — **E** the generator has this block type · **E★** existing type, but this page uses it in a
shape the renderer cannot produce · **N** new. Component names in the last column are
`ks3_parity.COMPONENTS` entries (60 registered) that would gate it.

| # | Block | GEN? | States | Gating components |
|---|---|---|---|---|
| 1 | `header.ks3-lesson-head` — eyebrow "Cells and organisation · Investigation", h1, `.ks3-bigq`, `.ks3-review-flag` | **E** | draft flag present / absent | lesson title · big question · eyebrow · draft badge |
| 2 | `#s-hook` — ink-dark: eyebrow, `h2.ks3-hook-h`, `.ks3-hook-prompt`, **a 2-up pending-figure pair**, then `.ks3-hook-commit` with 4 `.ks3-option`s and a gated `.ks3-reveal` | **E★** | option resting / chosen; reveal hidden / shown | hook is ink-dark, accent shadow · dark-block option resting/CHOSEN (+badges) · standard block shell |
| 3 | `#s-method` — **the critique instrument** (see §3.1) | **N** | per-step unpicked / picked; whole block locked / opened; per-step verdict hidden / shown ("Costs him" / "Sound") | none |
| 4a | `#s-formula` panel 1 — **the formula statement** (see §3.2) | **N** | static, one state | none (closest: `#s-rule` from b1-01 §7.5) |
| 4b | `#s-formula` panel 2 — **the formula triangle** (see §3.2) | **N** | 3 cover states, one always on | none |
| 5 | **KEY FACT box** — `--ks3-band`, `2px --ks3-ink`, `box-shadow 5px 5px 0 --ks3-accent`, r20, `18px 22px`, MONO 13px label + DISPLAY 22px/700 statement | **N** | static | none — **byte-identical to b1-01's**, see §7.0 |
| 6 | `#s-worked` — **the staged FIFA worked example** (see §3.3) | **N** | 0..4 steps open; button first / next / spent | none (closest: `.ks3-fifa`, which is a different shape) |
| 7 | `#s-yours` — **the parallel FIFA attempt** (see §3.4) | **N** | 4 text fields; unchecked / checked; 0..4 ticks; tally not-yet / met | R8 check-my-answer button · `.ks3-ticks` / `.ks3-tally` |
| 8 | `#s-lab` — **the bench microscope** (see §3.5) | **E★** engine, **N** surface | locked / open; 3 objectives; 101 focus positions; 0..3 recorded rows; table complete / not | practical is ink-dark, blue shadow · dark-block option resting/CHOSEN · sim cover is a light veil |
| 9 | `#s-think` — misconception: `.ks3-mis-head` (badge + eyebrow), `.ks3-mis-quote`, **two prose paragraphs and nothing else** | **E★** | static | misconception is amber |
| 10 | `#s-ladder` — `.ks3-ladder`, head + score, 2 page-marked rungs (rung 2 carrying `.ks3-fifa`), 2 self-marked rungs, `.ks3-retry-wrap` | **E** | option resting / correct / wrong / spent; feedback; ticks 0..4; tally; retry | ladder shell · heading · option ×6 states+badges · feedback CORRECT/WRONG · page-marked rung is accent · self-marked rung is violet · R8 answer box · R8 check button |
| 11 | `#s-keynote` — ink-dark, alert-yellow shadow, `p.ks3-eyebrow` + one paragraph | **E** | static | key note is ink-dark · key note type drops to 700 |
| 12 | `.ks3-layer` — "Going further" violet stretch layer, one paragraph | **E** | static | stretch layer is violet |
| 13 | `.ks3-endmatter` — 4 cards: "Before this lesson" (**a link**), "Connects to" (a link), "At GCSE this becomes" (**prose**), `.ks3-tutor` (**live `<a href="#s-worked">`**) | **E★** | static | tutor card is accent · tutor text is large-bold |
| 14 | `p.ks3-legal` — **lesson-specific safety line** | **E★** | static | none |

Totals: **4 blocks the generator can already produce (E)** · **5 it produces in the wrong shape
(E★)** · **6 new components across 4 rows (N)**. Four of the six rail stages sit inside N blocks.

### 3.1 `#s-method` — "Sam's method", the critique instrument

The family's *"lead with a flawed investigation → critique before construct"* (§6, INVESTIGATION).
Real mechanics, driven.

**What the student manipulates.** Six full-width toggle buttons, one per method step, in a
`<ol style="list-style:none; display:flex; flex-direction:column; gap:10px; counter-reset:step">`.
Each is `width:100%; text-align:left; padding 15px 18px; min-height 44px; border-radius
var(--ks3-r-option)` holding a 32×32 r10 Bricolage-17px/800 number badge (gap 14px) and the step text
(**18px/600, lh 1.45**).

| Step button | ground | border | number badge |
|---|---|---|---|
| unpicked | `--ks3-ground` | `2px --ks3-option-border` | `--ks3-band` / `--ks3-ink-muted` |
| picked | `--ks3-accent-tint` | `2px --ks3-accent` | `--ks3-accent` / `--ks3-on-dark` |

`aria-pressed` carries the state and **picks are freely toggleable both before and after opening** —
measured: pick step 2, un-pick it (`pressed` returns to false, progress drops from "2 picked" to
"1 picked"), re-pick it. This is a **checkbox set, not a radio group**, and it is the first control on
either B1 page to be one.

**The gate.** `.ks3-reveal-btn` "Open the steps I picked" + a MONO 15px progress span.
Locked at zero picks: `disabled` attribute present, `opacity .45`, `cursor default`, progress reads
**"Pick at least one"**; clicking it while locked does nothing (measured, verdict count stays 0). At
≥1 pick the attribute is removed, `opacity 1`, progress reads **"N picked"**.

**Feedback, and when.** Pressing Open reveals a verdict panel **only under the steps the student
picked** — measured: 2 picked → 2 panels; pick a third afterwards → 3 panels, immediately, without
pressing Open again (`methodOpened` is sticky). Each panel is
`margin: 10px 0 0 46px` (indented past the number badge), `padding 16px 18px`,
`border-radius var(--ks3-r-panel)`, and takes one of **two tones from the step's `fault` boolean**:

| `fault` | verdict word | word colour | panel ground | panel border |
|---|---|---|---|---|
| `true` | **"Costs him"** | `--ks3-alert-text` (#5A430A) | `--ks3-alert-tint` | `2px --ks3-alert-border` (#D9821A) |
| `false` | **"Sound"** | `--ks3-ink-muted` | `--ks3-inset` (#F7EFE1) | `2px --ks3-rule-strong` |

Word type: 17px/700, `ls .04em` (0.68px), uppercase. Body: 18px, lh 1.55 (27.9px).
The panels carry `data-reveal="1"` but **not** `class="ks3-reveal"`, so `animation-name` resolves to
`none` — b1-01's F7, recurring here on a different component.

**Does it mark correctness?** Yes, and this is the one place on the page where a non-ladder block
does. A picked *sound* step is answered with "SOUND" on a neutral inset ground; a picked *faulty* step
with "COSTS HIM" on the amber alert ground. There is no ✓/✗ glyph and no score, so **R3's letter
holds** (only the ladder marks), but the two-tone treatment is a verdict on the student's pick in
everything but name. Three of the six steps are faults (`METHOD[0]`, `[2]`, `[3]`); the block's own
prose says so out loud — *"Three of the six steps will cost him."* Recorded, not resolved: F3.

**Word cost.** 272 words fully opened, 134 at rest — the wordiest block on the page outside the
ladder. §3.6.

### 3.2 `#s-formula` — MRB-204's first two formula components

One classless `<section>` holding **two independently-shelled panels**, 22px apart. This is the only
row on the page where one section renders two blocks, and it is the reason the row has no class: there
is nothing for a class to describe.

#### 3.2.1 Panel 1 — the formula statement

```
background var(--ks3-band); border 3px solid var(--ks3-ink);
border-radius var(--ks3-r-block) (28px); padding 40px 32px; text-align: center
```

One `<p>`, no class, no eyebrow, no cards, no closing prose. Just the formula:

> **total magnification = eyepiece × objective**

| Property | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| font-size (`clamp(26px, 3.6vw, 40px)`) | **40** (cap) | 40 | **29.52** (3.6vw) | **26** (floor) |
| family / weight | `--ks3-font-display` Bricolage / 800 | = | = | = |
| line-height | 46px (1.15) | = | 33.95 | 29.9 |
| letter-spacing | −1.2px (−.03em) | = | −0.89 | −0.78 |
| padding | 40px 32px | = | = | **40px 32px — no narrow rule** |

**`00-delivery-drift.md` drift 3's ruling is confirmed against measurement.** The panel's shell is the
same shell as b1-01's `#s-rule` statement panel (`--ks3-band`, `3px --ks3-ink`, `--ks3-r-block`) — so
the temptation to fold them together is real — but three measured properties separate them:

1. **`text-align: center`.** b1-01's statement is left-aligned with `max-width: 20ch`. This one is
   centred with **`max-width: none`** (measured). A formula is a centred object; a sentence is not.
2. **Its own clamp**, `clamp(26px, 3.6vw, 40px)` against b1-01's `clamp(30px, 4.2vw, 46px)` — and the
   ruled statement clamp is `clamp(28px, 3.9vw, 44px)`, which is neither.
3. **Nothing else in the panel.** b1-01's `#s-rule` carries an eyebrow, a 3-card grid and a closing
   20px paragraph, and its padding is `34px 32px`. This one carries one line and `40px 32px` — 6px
   more top and bottom, which is what a single centred line needs to sit in the middle of a box.

So: **a distinct component with its own type ramp**, exactly as drift 3 rules, and the drift file's
decision to exclude b1-02 from the statement-role count was correct. It should take a formula clamp,
not the statement clamp. Whether `clamp(26px, 3.6vw, 40px)` is *the* formula clamp cannot be settled
from one page — b1-02 is the only B1 lesson with a formula. Flagged for Design, F2.

#### 3.2.2 Panel 2 — the formula triangle

`--ks3-card` on `2px --ks3-ink`, `--ks3-r-block`, `box-shadow var(--ks3-shadow-block)` (5px 5px 0
`--ks3-ink`), `padding 30px` — i.e. **an ordinary `.ks3-block` shell**, hand-written rather than
classed. Inside: `p.ks3-eyebrow` "The triangle", `h2` (30px/800, lh 1.2, ls −.025em) "Cover the one
you want", then a 2-column grid `repeat(auto-fit, minmax(260px, 1fr))` gap 26px, `align-items:center`.

**Left column — the SVG.** `viewBox="0 0 260 216"`, `width="260" height="216"` (measured 260×216 at
**every** viewport — see F6), `role="img"`, `aria-label="Formula triangle: total magnification on top,
eyepiece and objective below"`.

| Element | Geometry | Paint |
|---|---|---|
| triangle | `M130 8 L252 208 L8 208 Z` | fill `--ks3-inset`, stroke `--ks3-ink`, `stroke-width 4`, `stroke-linejoin: round` |
| horizontal divider | `x1 42 y1 130 → x2 218 y2 130` | `--ks3-ink`, sw 4 |
| vertical divider | `x1 130 y1 130 → x2 130 y2 208` | `--ks3-ink`, sw 4 |
| "total" | x 130 y 98, `text-anchor: middle` | Bricolage 800, **font-size 27**, `--ks3-ink` |
| "eye" | x 86 y 180, middle | Bricolage 800, **23**, `--ks3-ink` |
| "obj" | x 175 y 180, middle | Bricolage 800, **23**, `--ks3-ink` |
| cover rect | `rx 10`, `opacity 0.92` | fill `--ks3-ink` |

The three text labels are **abbreviated** — "total" / "eye" / "obj" — while the formula above says
"total magnification = eyepiece × objective" and the button labels say "Cover eyepiece" /
"Cover objective". Three vocabularies for the same two quantities on one screen. Recorded, F4.

**The staging — this is the component's whole mechanism.** The cover rect's four geometry attributes
come from a per-state box (source 737–741), driven and confirmed:

| state (`s.cover`) | button (pressed) | rect x, y, w, h | text shown |
|---|---|---|---|
| **`total`** (default at mount) | Cover total | **62, 62, 136, 52** | "Total is on its own at the top, with the other two side by side underneath. Cover it and you are left with eyepiece × objective — multiply." |
| `eye` | Cover eyepiece | **46, 146, 78, 48** | "Cover the eyepiece and you are left with total over objective. Divide the total by the objective." |
| `obj` | Cover objective | **136, 146, 78, 48** | "Cover the objective and you are left with total over eyepiece. Divide the total by the eyepiece." |

**One state is always on** — `total` at mount, and there is no "uncovered" state. The rect's
`opacity` is a constant `0.92` (`coverOn`), never 0, so a student never sees the bare triangle. That
is a design decision worth surfacing: the triangle is only ever taught *covered*.

**Right column.** Three `aria-pressed` buttons in a `flex; gap:10px; flex-wrap:wrap` row —
`16px/700`, `padding 11px 16px`, `min-height 44px`, `border-radius var(--ks3-r-control)` (14px),
widths 120.31 / 152.72 / 154.97. On-state is an **ink fill** (`--ks3-ink` ground + border,
`--ks3-on-dark` text); off is `--ks3-card` on `2px --ks3-option-border` with `--ks3-ink` text.
Then the live rearrangement sentence (**20px/600, lh 1.6, `--ks3-ink`**) and a fixed closing line
(17px/400, lh 1.55, `--ks3-ink-body`): *"Two things side by side means multiply. One thing over another
means divide."*

**Drift 4 note.** These three buttons are a sixth `seg()`-shaped control across the delivery: b1-06's
ruled geometry at **16px** rather than 17px, `11px 16px` rather than `11px 17px`, on `--ks3-r-control`
with **b1-03's inverted ink on-state**. Same family as b1-01's specimen tabs (which took the inversion
on a 999px pill). `00-delivery-drift.md` flagged the inversion as Design's call; this is the third page
carrying it, so the inversion is clearly deliberate and the drift file's flag should be closed rather
than left open.

### 3.3 `#s-worked` — MRB-204's third formula component, the staged worked example

`.ks3-block` shell. Eyebrow "Watch it done · one step at a time"; the `<h2>` **is the question**
("Riya's eyepiece says ×10. The objective clicked into place says ×40. Calculate the total
magnification.") — a 30px/800 display heading carrying a full sentence of physics, which is worth
noting because the generator's activity renderer puts the prompt in a `<p>` under a fixed eyebrow.

Four `<li>` in a flex column, gap 12px. Each holds a 40×40 r12 Bricolage-20px/800 letter badge
(**F · I · F · A**) beside an uppercase 16px/700 `ls .1em` `--ks3-ink-muted` step name
(**Formula · Insert · Fine-tune · Answer**), and — once open — two revealed paragraphs.

| li state | ground | border | letter badge |
|---|---|---|---|
| closed | `--ks3-row-dim` (#FBF6EC) | `2px --ks3-rule` | `--ks3-band` / `--ks3-ink-ghost` |
| open | `--ks3-inset` (#F7EFE1) | **`2px --ks3-ink`** | **`--ks3-accent` / `--ks3-on-dark`** |

Shell is `padding 16px 18px`, `border-radius var(--ks3-r-panel)` (20px) in both states.

**Revealed content, per step.** Two paragraphs, both `data-reveal="1"` and neither carrying
`class="ks3-reveal"` (so again no animation — F7 of b1-01):

- **the working line** — MONO **21px**/500, lh 1.4 (29.4px), `--ks3-ink`, `margin 6px 0 0`
- **the note** — 17px/400, lh 1.5, `--ks3-ink-body`, `margin 6px 0 0`

**The staging.** One `.ks3-reveal-btn` walks `s.workedStep` 0 → 4, one step per press. Driven through
all five states:

| `workedStep` | button label | button state | progress |
|---|---|---|---|
| 0 | **"Show the first step"** | live | "0 of 4 shown" |
| 1–3 | **"Show the next step"** | live | "N of 4 shown" |
| 4 | **"All four steps shown"** | `disabled`, `opacity .45`, `cursor default` | "4 of 4 shown" |

Pressing it again at 4 is a no-op (measured). There is **no way back** — no collapse, no reset. The
rail's stage 3 ticks at `workedStep >= 4`.

The four working lines, verbatim (source 540–543): `total magnification = eyepiece × objective` ·
`total magnification = 10 × 40` · `nothing to convert — both are already "times"` · `×400`. The
Fine-tune note is the longest single string on the page (44 words) and carries the lesson's
misconception in numbers: *"multiply, never add. 10 + 40 = 50 is the commonest wrong answer on this
calculation."*

### 3.4 `#s-yours` — MRB-204's fourth formula component, the parallel attempt

Law 5's *"the same artifact, produced by the student"*, and the generator has no shape for it.
`.ks3-block` shell; eyebrow "Now you · same four steps"; the `<h2>` is again the question ("Your
eyepiece says ×10. You click the ×4 objective into place…"); then a 19px/1.6 `max-width 52ch`
(658.008px measured) instruction.

**Four labelled fields**, in a flex column gap 14px. Each row is a
`grid-template-columns: 46px minmax(0, 1fr)` with `gap 14px; align-items:center`:

- a 40×40 r12 Bricolage-20px/800 letter badge, `--ks3-band` ground, **`--ks3-accent-text` text**
  (note: the worked example's badge is accent-on-cream when open; this one is accent-*text*-on-band
  always — a deliberately quieter, "yours to fill" treatment)
- a `label.ks3-answer-label` (16px/700 `--ks3-ink-muted`) + an `<input type="text">`:
  `19px`, `padding 13px 16px`, `min-height 44px`, `border-radius var(--ks3-r-option)`,
  `2px --ks3-option-border`, `--ks3-card` ground, `width 100%` (836px at 1280, 258px at 390)

| id | label | placeholder |
|---|---|---|
| `my-f` | Formula | `total magnification = …` |
| `my-i` | Insert | `total magnification = … × …` |
| `my-t` | Fine-tune | `anything to convert?` |
| `my-a` | Answer | `×…` |

**`.ks3-check-btn` "Check my working"** — 17px/700, `13px 20px`, 44px, r14, `--ks3-band` ground on
`2px --ks3-ink`, `margin-top 14px`. Pressing it reveals a `.ks3-crit-wrap` (`--ks3-inset`,
`2px --ks3-ink`, `--ks3-r-panel`, `padding 22px`, `margin-top 18px`, **`animation-name: ks3-reveal`** —
this one does animate, because `.ks3-crit-wrap` is a shipped class) holding:

1. `p.ks3-crit-lead` "Riya's working, with your numbers" — 15px/700, `ls .12em` (1.8px), uppercase,
   `--ks3-ink-muted`
2. four `<li>` of **MONO 19px/500 lh 1.5** model lines, `margin 0 0 16px`:
   `F   total magnification = eyepiece × objective` · `I   total magnification = 10 × 4` ·
   `F   nothing to convert — multiply, do not add` · `A   ×40`
3. `ul.ks3-ticks` — four real 25×25 checkboxes (`accent-color --ks3-ok`) with numbered labels
4. `p.ks3-tally` role="status" — `--ks3-band` ground, `--ks3-ink-body`, `padding 11px 16px`, r13,
   17px/700 → **`.ks3-tally.is-met`** `--ks3-ok-tint` / `--ks3-ok-text` at 4/4

Tally copy is **its own wording, not the ladder's**: `"N of 4 ticked — not yet."` →
**`"All 4 ticked — you can do this one on your own."`** (the ladder's self-rungs say "rung met").
Confirmed it does **not** feed the ladder score (`"You got 0 of 4."` unchanged at 4/4 ticks).

**Two defects, both measured, both b1-01's F8/F9 recurring on `<input>` instead of `<textarea>`:**

- **The typed working is lost on the next re-render.** `<input value="{{ f.value }}">` sets an
  attribute the element only reads as a default. Measured: set `my-f` and fire `change` → the value
  survives one render (`"total magnification = eyepiece x objective"`); tick the first criterion → all
  four inputs read `""` while `state.mine` still holds the string. So the student's own working
  vanishes at the exact moment they start marking it against the model.
- **"Check my working" works on four empty boxes.** Measured: press it with nothing typed → the full
  model working and all four criteria appear, and ticking all four yields "you can do this one on your
  own." The model answer is the one thing that must be behind a written attempt, and it is not.

### 3.5 `#s-lab` — the bench microscope

`.ks3-block ks3-dark ks3-practical` — ink ground, r30, `box-shadow 6px 6px 0 var(--ks3-blue)`
(#2F5CE0, from the shipped `.ks3-practical` rule), `padding 32px` / `22px 18px` narrow.

Head row: `flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 20px` —
eyebrow "Investigate" + `h2` **34px/800 lh 1.1 ls −.03em** "The bench microscope" on the left
(351.58px), and a right-aligned 17px `--ks3-on-dark-muted` `max-width 30ch` (339.66px) aside:
*"Eyepiece fixed at ×10. Turret, focus and a slide of onion skin."* At 390 both children take the full
322px and the aside stays `text-align: right`.

#### 3.5.1 The R5 lock, as this page draws it

| | measured |
|---|---|
| canvas | `width="1120" height="560"` attributes; CSS `896×450` at 1280, `708×356` at 820, `322×163` at 390 (`width:100%; height:auto`) |
| canvas ground | `#100D0A` — **a bare hex matching nothing in the palette** |
| canvas frame | `2px solid var(--ks3-on-dark-muted)`, `border-radius var(--ks3-r-panel)` |
| locked filter | **`blur(2px) saturate(0.65)`** on the canvas itself |
| veil | `position:absolute; inset:0`, `border-radius var(--ks3-r-panel)`, `padding 16px`, `text-align:center`, ground **`color-mix(in srgb, var(--ks3-card) 85%, transparent)`** → measured `color(srgb 1 0.988235 0.960784 / 0.85)` |
| veil copy | 18px/700 `--ks3-ink`, `max-width 34ch` (417.384px): *"Answer the question underneath first. The lens will not tell you anything you have not already guessed at."* |
| the gate | `.ks3-commit` (22px/700 `--ks3-on-dark-body`) *"Turn from the ×4 objective to the ×40. What happens to the amount of slide you can see?"* + **3 `.ks3-option`s** in `.ks3-options` overridden to `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))` → 291.33 ×3 at 1280, 291.33 ×3 at 820, 1-up at 390 |
| options | A "You see more of the slide" · B "You see less of the slide" · C "You see the same amount, bigger" |

The veil ground and the `color-mix()` expression are **byte-identical to the shipped
`.ks3-sim-cover`** rule, so this traces to an existing token expression. What differs is the geometry
(`inset:0` vs the shipped `aspect-ratio: 560 / 220`) and the copy.

**Choosing an option removes the gate entirely** — measured: the whole predict block leaves the DOM
(`labLocked: !s.labPrediction`), the canvas filter goes to `none`, and the controls, readouts, record
button and table all appear at once. The student cannot see or change what they predicted, and
**nothing is ever scored against it**: `labPredictOptions` carries no correct index, and there is no
reveal panel answering the prediction. b1-01's F4 and F5 recur here verbatim; the authored payload
*does* carry `"answer": 1` for `microscope-lab`, so the data has a right answer the approved page
deliberately never uses. §5 gap G12, finding F8.

#### 3.5.2 The complete control surface, as this page draws it

`.ks3-sim-controls` — the shipped class, `display:flex; flex-wrap:wrap; gap:14px 26px`. **Two
controls, and no third:**

| # | Control | Type | Label (as drawn) | Range / options | Default |
|---|---|---|---|---|---|
| 1 | Objective | **3 `aria-pressed` buttons** in a `flex; gap:8px` span | `<span>Objective</span>` — **not a `<label>`, no `for`** | `×4` · `×10` · `×40` (widths 55.58 / 63.30 / 67.17) | **`×4`, the lowest** |
| 2 | Focus | `<input type="range">` | `<label for="focus-rack">` **"Focus — rack through the layers"** | `min="0" max="100"`, no `step` (implicit 1 → 101 positions) | **`50`** |

Button geometry: 17px/700, `padding 10px 16px`, `min-height 44px`, `border-radius
var(--ks3-r-control)`. On-state is an **alert fill** (`--ks3-alert` ground **and** border, `--ks3-ink`
text); off is `background: transparent` on `2px --ks3-on-dark-muted` with `--ks3-on-dark` text.
Control labels are 17px/600 `--ks3-on-dark-body` (from the shipped `.ks3-dark .ks3-sim-control` rule).
Slider width 240px at every viewport ≥390 (`min-width 11rem; max-width 15rem; height 44px;
accent-color var(--ks3-accent)`, shipped).

> ### ⚑ **There is no specimen selector on this page, and the authored payload declares three
> specimens.**
>
> Measured: `.ks3-sim-control` count is **2**. Design's instrument is objectives + focus, on one
> slide ("a slide of onion skin", named only in the aside).
>
> `ks3_data/biology_b1_cells.py` (activity `microscope-lab`, lines 801–810) declares
> `"controls": ["specimen", "magnification", "focus"]` and
> `"specimens": ["onion skin — well made", "onion skin — coverslip dropped flat",
> "human cheek cells"]`, and its `reveal` **depends on the selector existing**: *"Now put the badly
> made slide on and compare the two onion slides at the same magnification — same onion, same lens,
> and only one of them shows you a cell."* The lesson's first misconception (CELL-01,
> `confronted_by: "bubble-or-cell"`) is the bubbles-are-not-cells idea, and the bubble slide is how
> the instrument confronts it.
>
> `build_ks3.py:r_sim` also **hard-fails** a microscope sim with no `specimens[]`, and `wireMicroscope`
> returns early on an empty payload — so the field is structurally required by both sides even when
> the control is not drawn.
>
> This is a **divergence, recorded and not resolved.** Design's approved page wins under standing law,
> which would delete the bubble slide, the cheek slide and the authored reveal that turns on them;
> keeping the payload adds a control Design has not drawn to a component Design has drawn. Both
> readings are defensible under different clauses of the same law. **Finding F9 — Design's call.**

#### 3.5.3 Every readout the page emits, and what drives it

| # | Readout | Element | Type | Driven by | Values measured |
|---|---|---|---|---|---|
| 1 | **Total magnification** | `p.ks3-sim-figure` under an uppercase 16px `ls .1em` `--ks3-on-dark-muted` label | MONO **40px**/500, `--ks3-alert` (from `.ks3-dark .ks3-sim-figure`) | objective | `×40` · `×100` · `×400` |
| 2 | **Field of view** | same | same | objective | `4.50 mm` · `1.80 mm` · `0.45 mm` |
| 3 | **Cells across it** | same | same | objective | `15` · `6` · **`1½`** |
| 4 | **focus position** | `span.ks3-sim-value` beside the slider | MONO 15px/500 `--ks3-on-dark-muted` | focus **and** objective | `the top layer — sharp` / `the middle layer — sharp` / `the bottom layer — sharp` / `between layers — nothing sharp` |
| 5 | **the sharpness note** | `p.ks3-sim-caption`, `margin 12px 0 0` | 17px lh 1.5 `--ks3-on-dark-muted` | **objective only** — see below | 3 fixed strings |
| 6 | record progress | MONO 15px/500 `--ks3-on-dark-muted` | | recorded count | `"N of 3 rows recorded"` |

Readout grid: `repeat(auto-fit, minmax(180px, 1fr))` gap 18px → **3 columns at 1280 (286.66 each) and
at 820 (224 each), 1 column at 390**. The 40px MONO figure survives the 322px narrow column.

Readouts 1–3 are pure functions of the objective — all three come straight out of `OBJECTIVES`
(source 560–564: `fov` and `cells` are authored literals, `total` is authored too). Readout 4 is the
only one the focus wheel moves.

##### The per-objective sharpness note — one of the three lines is wrong under the ruled table

The note is a **static string chosen by objective and nothing else** (source 975–979). It does not
change as the wheel turns. Verbatim, all three:

| Objective | Total | Sharpness note (verbatim) |
|---|---|---|
| ×4 | ×40 | *"At ×40 the whole thickness of the skin is in focus at once. Easy to find things; not much detail in them."* |
| ×10 | ×100 | ⚠ *"At ×100 two layers are nearly sharp together. There is still depth to spare."* |
| ×40 | ×400 | *"At ×400 the slice in focus is thinner than one cell. Rack the focus and the layers arrive one at a time — that thin slice is the depth of field."* |

**The ×100 line is false under the depth-of-field table Mide ruled on 13 Aug 2026** (0.100 / 0.040 /
0.008 mm at ×40 / ×100 / ×400, `OBJ_DOF_MM` in `shared/ks3.js:1257`, an engine constant and not a
payload field). Measured in the running engine and independently verified by arithmetic over the
page's own `LAYERS = [-0.055, 0, 0.055]`:

- sharp window at ×100 = `SHARP_FRACTION × dof` = `0.6 × 0.040` = **±0.024 mm**
- adjacent layers are **0.055 mm** apart
- two layers can only be inside one window together if `2 × window > 0.055`, i.e. `window > 0.0275 mm`
- **0.024 < 0.0275, so at ×100 the engine holds AT MOST ONE layer sharp — at every one of the 101
  wheel positions, never two.** Confirmed by enumerating all 101 positions with the engine's
  non-parfocal offset (`OBJ_FOCUS_SHIFT[1] = 10`): maximum layers inside the window = **1**, and 76 of
  101 positions have any layer sharp at all.

The line was **true on the page's own inline table** (0.30 / 0.09 / 0.012), where the ×100 window is
`0.6 × 0.09` = **±0.054 mm** > 0.0275, so two layers really did sit inside it over part of the wheel.
The claim did not become wrong through carelessness; it became wrong when the two approved
implementations were reconciled onto one instrument. **The page's own table is superseded and is not
reported here as a requirement.**

The other two lines survive, with one qualification each:

- **×40 holds.** Ruled window `0.6 × 0.100 = ±0.060 mm` against a 0.110 mm layer span, so all three
  layers are inside it — but only near the middle of the wheel (the focal plane has to sit within
  0.005 mm of centre). "In focus at once" is true where the lesson starts (`focus: 50`) and stops
  being true at the ends of the travel. Worth a sentence, not a rewrite.
- **×400 holds and gets stronger.** Ruled window `±0.0048 mm` against a 0.115 mm cell depth — a slice
  ~24× thinner than one cell, and only **12 of 101** wheel positions have anything sharp. "The layers
  arrive one at a time" is exactly what the engine does.

**The corrected ×100 copy is deliberately not written here.** It is a science correction on a line a
student reads as settled, so it belongs to the next run with Mide's eye on it. What is specified is
the defect and the true behaviour: at ×100 the depth of field is 0.040 mm, the sharp window is
±0.024 mm, the layers are 0.055 mm apart, exactly one layer can be sharp at a time, and the honest
teaching point at ×100 is that **the outer layers have already gone** — the loss of depth begins at
×100 rather than arriving at ×400. Finding F10, §8(b).

#### 3.5.4 The recording table

A `<button>` "Record this row" — 17px/700, `13px 20px`, 44px, r14, **`--ks3-alert` ground and border**,
`--ks3-ink` text — appends the current objective to `s.recorded` and is **idempotent** (measured:
pressing it twice on the same objective leaves "3 of 3 rows recorded"). It sits above a
`border-top: 2px solid var(--ks3-dark-panel)` divider with the progress span.

The table is `width:100%; border-collapse: collapse; font-size: 18px` with a real `<thead>`:

| header | scope | style |
|---|---|---|
| Objective · Total · Field of view · Cells across | `col` | `--ks3-dark-panel` ground, `--ks3-on-dark` text, 16px, `ls .06em`, uppercase, `padding 10px 12px`, `text-align:left`; first cell `border-radius 10px 0 0 10px`, last `0 10px 10px 0` |

Body cells: `padding 11px 12px`, `border-bottom 1px solid var(--ks3-dark-panel)`, MONO 500 18px,
**`--ks3-on-dark-muted` before the row is recorded and `--ks3-on-dark` after** — the only two-state
paint in the table. Three rows exist from the start, all four cells reading `—`.

Recorded, all three (measured):

| Objective | Total | Field of view | Cells across |
|---|---|---|---|
| ×4 | ×40 | 4.50 mm | 15 |
| ×10 | ×100 | 1.80 mm | 6 |
| ×40 | ×400 | 0.45 mm | **1½** |

At 3/3 a `data-reveal="1"` panel appears — `--ks3-dark-panel` ground, `2px --ks3-alert`,
`--ks3-r-panel`, `padding 20px 22px`, one 19px/1.6 `--ks3-on-dark` paragraph: *"Ten times the
magnification. A tenth of the field of view. A tenth of the cells in front of you — and a slice of
depth so thin that most of the cell is out of focus at once."* No `class="ks3-reveal"`, so no
animation (F7 again).

**Table rows are keyed by objective, not by observation** — the student cannot record two rows at the
same lens, and `recorded.length === OBJECTIVES.length` is the completion test. So the table is a
**checklist of lenses visited**, not a data table the student fills in. Worth knowing before it is
generated: nothing the student types ever enters it.

#### 3.5.5 Payload field vs engine constant

The repo now has one unified engine (`wireMicroscope`, `shared/ks3.js:1291`), reconciled against this
page and B1-06 under MRB-210. Splitting this page's numbers against it:

**Engine constants — ruled, and must not become payload fields:**

| Constant | Value | Where |
|---|---|---|
| eyepiece | `10` | `EYEPIECE` |
| objectives | `[4, 10, 40]` | `OBJECTIVES` |
| field of view | `180 / magnification` | `FIELD_AT_1X_MM = 180` |
| **depth of field** | **`[0.100, 0.040, 0.008]` mm** | `OBJ_DOF_MM` — ruled 13 Aug 2026, a table not a law |
| focus travel | `−0.09 … +0.09 mm` over slider 0–100 | `FOCUS_MIN_MM`, `FOCUS_SPAN_MM` |
| sharp test | `\|focal − depth\| < 0.6 × dof` | `SHARP_FRACTION` |
| non-parfocality | `[0, 10, 22]` slider units | `OBJ_FOCUS_SHIFT` — Code's addition, ruled to stay |
| onion cell | 0.30 × 0.115 mm | `CELL_W`, `CELL_H` |
| blur laws | cap/factor per specimen kind | `BLUR_ONION` etc. |

Note that the engine **derives** field of view (`180/mag`) and cells-across (`fov / cellMm`, printing
`1½` as a half) where this page **authors them as literals** in `OBJECTIVES` (`fov: 4.5, cells: '15'`).
Both land on the same numbers — 180/40 = 4.5, 4.5/0.30 = 15, 1.8/0.30 = 6, 0.45/0.30 = 1.5 → `1½` —
which is why MRB-210 could reconcile them. **The generator should emit neither: it should let the
engine compute them, and the parity gate should assert the engine's output equals this page's
literals.** An authored `fov` is a number that can drift from the optics; a derived one cannot.

**What genuinely varies per lesson** — the only fields the payload needs:

| Field | This lesson | Why it varies |
|---|---|---|
| `specimens[]` | one onion slide as drawn (three declared in the data — F9) | B1-06 uses pond water and a cheek smear; the slide is the lesson's subject |
| `controls[]` | `["magnification", "focus"]` as drawn | B1-06 needs the specimen selector; L2 as drawn does not |
| the commit question + its options | 1 question, 3 options | Law 4's gate is per lesson |
| the veil copy | *"Answer the question underneath first…"* | lesson voice |
| the per-objective note | 3 strings (one needing correction) | the teaching point at each lens is per lesson |
| the recording table's columns | 4 | a different lesson might record different columns |
| the table-complete reveal | 1 paragraph | this is the lesson's conclusion |
| the aside | *"Eyepiece fixed at ×10…"* | names the apparatus |

Everything else on this instrument is optics, and optics live in one table.

#### 3.5.6 How far the generator's `microscope` sim is from this surface

The sim *kind* exists (`SIM_ARIA["microscope"]`, `wireMicroscope`), so this row is E★ rather than N —
but the surface around it is new in seven measured ways:

| | Generator (`r_sim`, `wireMicroscope`) | This page |
|---|---|---|
| canvas | `560 × 220` attributes, class `.ks3-sim-canvas` | **`1120 × 560`**, no class, driven by `canvasRef` |
| veil | `p.ks3-sim-cover`, `aspect-ratio: 560 / 220`, "Make your prediction first — then the lab runs." | absolute `inset: 0` div, own copy |
| lock signal | veil only | veil **plus `filter: blur(2px) saturate(.65)` on the canvas** |
| magnification control | a `<select>` with "×40 — lowest lens" / "×100" / "×400 — highest lens" | **3 `aria-pressed` buttons** labelled by *objective* (`×4 ×10 ×40`) |
| focus control | a range with **deliberately no number beside it** | a range **with** a `.ks3-sim-value` naming which layer is sharp |
| readout | **one** `p.ks3-sim-readout` prose line, `"Total magnification ×N · field of view N mm. <what you see>"` | **three** `.ks3-sim-figure` numerals + a live focus value + a per-objective caption |
| `.ks3-sim-caption` | the **authored static** caption | the **live per-objective** sharpness note |
| recording | none | Record button + 4-column table + 3/3 reveal |

The `.ks3-sim-caption` collision is the sharpest of these: one shipped class doing two different jobs.
Code's call, §8(c).

### 3.6 Word counts — what MRB-205 needs

MRB-205 records Mide's verdict that this lesson was *"far too wordy"* and needed replanning; this
approved page **is** the replan, so the counts are reported rather than judged. Measured in the
browser: `.ks3-lesson` text at rest, then again with every stage driven open.

| # | Block | at rest | fully revealed | Δ |
|---|---|---|---|---|
| 1 | `header.ks3-lesson-head` | 26 | 26 | — |
| 2 | `#s-hook` | 108 | **134** | +26 (reveal) |
| 3 | **`#s-method`** | 134 | **272** | **+138 (6 verdicts)** |
| 4 | `#s-formula` | 63 | 63 | — (one `coverText` at a time; the other two are 41 more words) |
| 5 | KEY FACT | 15 | 15 | — |
| 6 | **`#s-worked`** | 40 | **159** | **+119 (4 lines + 4 notes)** |
| 7 | `#s-yours` | 47 | **133** | +86 (lead + 4 model lines + 4 criteria + tally) |
| 8 | `#s-lab` | 73 | **143** | +70 (controls, readouts, note, table, reveal) |
| 9 | `#s-think` | 77 | 77 | — |
| 10 | **`#s-ladder`** | 224 | **405** | **+181 (corrections + 8 criteria)** |
| 11 | `#s-keynote` | 26 | 26 | — |
| 12 | `.ks3-layer` | 58 | 58 | — |
| 13 | `.ks3-endmatter` | 45 | 45 | — |
| 14 | `p.ks3-legal` | 15 | 15 | — |
| | **total** | **951** | **1,571** | **+620** |

Authored strings in the data constants, counted per constant (181 literals, 1,139 words):

| Constant | strings | words |
|---|---|---|
| `SELF_RUNGS` (2 questions + 8 criteria) | 18 | **224** |
| `METHOD` (6 × text + word + verdict) | 18 | **223** |
| `RUNGS` (2 questions + 8 options + 6 corrections) | 20 | **201** |
| `WORKED` (4 × line + note) | 16 | **127** |
| `sharpnessNote` (3) | 3 | 67 |
| tally / progress / score chrome | 41 | 64 |
| `coverText` (3) | 3 | 62 |
| `MY_CRITERIA` (4) | 4 | 45 |
| `MY_FIELDS` (labels + placeholders) | 16 | 26 |
| `RAIL` + `RAIL_SHORT` | 18 | 25 |
| `modelLines` (4) | 4 | 25 |
| `hookOptions` (4) | 8 | 23 |
| `labPredictOptions` (3) | 6 | 21 |
| `OBJECTIVES` (labels) | 6 | 6 |

**What the next run needs to know about the verdict.** §5.2's budget is *"~90 words of continuous
prose maximum before a commitment; whole-lesson body prose under 450 words, excluding activity copy,
ladder questions and the key note."*

- **Prose before the first commitment: 74 words** — the h1 + big question + hook eyebrow + heading +
  prompt, ending at the four hook options. Inside 90.
- **Continuous body prose, on the strictest reading (the four paragraphs that are neither activity
  copy nor ladder nor key note): 42 + 13 + 68 + 58 = 181 words** — the hook prompt, the triangle's
  closing line, the misconception's two paragraphs, and the stretch layer. Comfortably inside 450, and
  **the page renders no `explainer` block at all**.
- **So the replan did address the verdict on the metric §5.2 measures.** What it did not reduce is
  **activity copy**, which §5.2 explicitly excludes and which is where 1,139 of the words live. Four
  blocks each grow by 70–181 words on interaction, and `#s-method` alone reveals 138 words of verdict
  prose in one press — six panels at once, averaging 23 words each, all of them appearing below the
  fold. That is the wordiness a reader would still feel, and it is invisible to the §5.2 gate.

Recorded as a measurement, not a verdict. If Mide reads 1,571 revealed words as still too wordy, the
lever is `#s-method`'s six verdicts and the ladder's 405, not the prose.

---

## 4. Interactive behaviours

All 16 driven in the browser with a forced reflow plus a 700ms settle after each click (see the
settle warning at the top — a 450ms settle reads pre-transition values on this page).

| # | Trigger | What changes | Notes |
|---|---|---|---|
| 1 | Click a hook option | `aria-pressed="true"` → border `--ks3-alert` (dark rule), badge `--ks3-alert`/`--ks3-ink`; `.ks3-reveal` appears — `--ks3-dark-panel`, `2px --ks3-alert`, r18, `padding 18px 20px`, **`animation-name: ks3-reveal`** | **Re-choosable**, no lock, no correctness. Rail stage 1 ticks. 4 options, letters A–D |
| 2 | Click a method step | Toggles `picked[i]`: ground `--ks3-ground`↔`--ks3-accent-tint`, border `--ks3-option-border`↔`--ks3-accent`, badge `--ks3-band`/`--ks3-ink-muted`↔`--ks3-accent`/`--ks3-on-dark`; progress "Pick at least one"→"N picked" | **A checkbox set** — verified toggling off drops the count. First multi-select control in B1 |
| 3 | Click "Open the steps I picked" while locked | Nothing (verdict count stays 0) | `disabled` attr + `opacity .45` + `cursor default` |
| 4 | Click it unlocked | Verdict panel under **every picked step**; rail stage 2 ticks | Two-tone by `fault` (§3.1) |
| 5 | Pick another step after opening | Its verdict appears **immediately**, no second press | `methodOpened` is sticky and one-way |
| 6 | Click a cover button | SVG rect jumps to that quantity's box; the 20px/600 rearrangement sentence swaps; the other two buttons return to `--ks3-card`/`--ks3-option-border` | Radio-like, one always on, default `total`. No "uncovered" state |
| 7 | Click "Show the first / next step" | Next `<li>` goes `--ks3-row-dim`/`--ks3-rule` → `--ks3-inset`/`--ks3-ink`, badge → `--ks3-accent`/`--ks3-on-dark`, two `data-reveal` paragraphs appear; label and progress advance | One-way. At 4: label "All four steps shown", `disabled`, `opacity .45` |
| 8 | Click it again at 4 of 4 | Nothing | Verified |
| 9 | Type in a `#my-*` field | `state.mine[id]` updates on `change` | ⚠ **the value is lost on the next re-render** — F5 |
| 10 | Click "Check my working" | `.ks3-crit-wrap` appears (animates) with the lead, 4 MONO model lines, 4 checkboxes, tally; rail stage 4 ticks | ⚠ **works with all four fields empty** — F5 |
| 11 | Tick all 4 criteria | `.ks3-tally.is-met` → `--ks3-ok-tint` / `--ks3-ok-text`, "All 4 ticked — you can do this one on your own." | Does **not** touch the ladder score (verified) |
| 12 | Click a lab predict option | Whole predict block leaves the DOM; canvas filter → `none`; controls, readouts, note, record button and table all appear | Irreversible, unrecorded, unscored — b1-01 F4/F5 |
| 13 | Click an objective button | Alert fill moves; all three figure readouts and the sharpness note change; the canvas redraws | The focus value can change too (the sharp window narrows) |
| 14 | Drag the focus slider | `.ks3-sim-value` names the nearest layer and whether it is sharp; the canvas re-blurs per layer | 101 positions. The **sharpness note does not change** — it is per-objective only |
| 15 | Click "Record this row" | That objective's row fills, cells go `--ks3-on-dark-muted` → `--ks3-on-dark`, progress increments; at 3/3 the reveal panel appears and rail stage 5 ticks | **Idempotent** — re-pressing on a recorded objective is a no-op (verified) |
| 16 | Ladder: option / check / tick / retry | Identical to b1-01 behaviours 10–12, measured again: wrong → `.is-wrong` (`--ks3-band` on `--ks3-ink`, badge ink/on-dark, drawn ✗ `M6.5 6.5l11 11M17.5 6.5l-11 11`); correct → `.is-correct` (`--ks3-ok-tint` on `--ks3-ok`, badge `--ks3-ok`/white, drawn ✓ `M5 12.5l4.6 4.5L19 7`); others `.is-spent`; all 4 `disabled`; `.ks3-feedback is-wrong` = `--ks3-band` on `2px --ks3-ink`, `is-correct` = `--ks3-ok-tint` on `2px --ks3-ok`; score 0 → 1 → 2 → 3 | ⚠ **b1-01's F8, F9 and F10 all recur verbatim.** `<textarea value="{{…}}">` loses the text on re-render (measured: "Field of view gets smaller." present after `change`, `""` after the first tick). "Check my answer" works on an empty box. "Retry my misses" resets **everything** — score 3 → 0, both self-rung texts to `""`, all four r1/r2 options re-enabled — while its own note says "keeps what you wrote" |

Rung shells, measured: `.ks3-rung` is `border-left: 4px solid` + `padding-left 22px`, **`--ks3-accent`
for the two page-marked rungs and `--ks3-stretch` (#6B3FD4) for the two self-marked**. Rung 2 carries
`.ks3-fifa` (`--ks3-inset`, `2px --ks3-ink`, `--ks3-r-panel`, `padding 20px 22px`, 19px) holding the
**method as instructions** — *"F — write the formula down before anything else."* etc. — not the
answer. `.ks3-answer` is `rows="2"` with `min-height: 136px`.

Keyboard/focus, real `Tab` via `Input.dispatchKeyEvent`: **the R15 ring reaches Design's
inline-styled buttons** — landed on the "Cover total" button and measured
`outline: 3px solid rgb(228, 87, 46)` (`--ks3-accent`) with `outline-offset: 2px`, from
`[data-mode="ks3"] :focus-visible`. **The top rail contains 0 focusable elements** (measured), so
b1-01's F11 recurs: under 1340px there is no keyboard route to a section; the side rail's 6 anchors
provide one above it.

---

## 5. Schema gaps against §4.8

§4.8 is authoritative — *"Fields not listed here do not exist without an amendment to this
document."* Existing coverage first, then the gaps.

### 5.1 Already covered

| Page content | §4.8 field |
|---|---|
| h1, breadcrumb tail, eyebrow left half | `title`, `unit`, `discipline` |
| eyebrow right half "Investigation" | `family` |
| `.ks3-bigq` | `big_question` |
| draft flag | `review_state` |
| hook eyebrow / heading / prompt / commit | `phenomenon` (`{kind,title,prompt,commit}`) |
| `.ks3-mis-quote` | `misconceptions[].statement` |
| keynote paragraph | `key_note` |
| block order + types | `core[]` |
| "Going further" | `stretch[]` |
| ladder rungs, options, corrections, criteria | `ladder{recall,apply,explain,produce}` — per-option `correction` maps 1:1 onto `feedback` keyed by option index |
| "Before this lesson" **link** | `requires: ["life-processes"]` — the generator can already emit this card as a link, so **b1-01's G10 does not recur** |
| "Connects to" link | `references` / `requires` |
| the two hook figures' *existence* | `figures[]` — but see G4, G5 |
| the lab's existence and sim kind | `activities[].sim{kind: "microscope", controls, specimens, caption}` |

Not surfaced on the page at all: `covers`, `touches`, `beyond_statutory`, `threads`, `typical_year`,
`typical_minutes`, `assumes`, `ws`, `support`. **`vocabulary` is declared with four terms and the page
renders no keyword block.**

### 5.2 Gaps — 14

Two are carried from b1-01 unchanged and are listed for completeness rather than re-argued.

| # | What the page needs | §4.8 today | Proposed field + shape | Sits inside |
|---|---|---|---|---|
| G1 | 6 progress-rail stages, two label sets, completion predicates | nothing | **`rail: [{anchor, short, label, done_when}]`** — b1-01 §2.6's shape, unchanged, 6 entries. Add the validation in §2.4 | top level |
| G2 | KEY FACT box, one per lesson, mid-page | nothing | **block type `key-fact`** — b1-01 G1's shape, unchanged; confirmed byte-identical here | `core[]` — §5.1.1 amendment |
| G3 | The method critique: 6 steps, each with a fault flag, a two-word verdict label and a verdict paragraph | `investigation` kind has `prompt` + `success` only; nothing expresses a per-item verdict | **`activities[] {kind: "critique-steps", intro, steps: [{text, fault: bool, word, verdict}], reveal_label, progress_zero}`** | `activities[]` |
| G4 | Figure `kind: "micrograph"` | §4.10's enum is `schematic \| graph \| photo \| apparatus` | **`figures[].kind += "micrograph"`** — the authored data already uses it and nothing validates the enum, so this is a **live silent gap in shipped data**, not a new want | `figures[]` (§4.10) |
| G5 | A **2-up figure pair inside the hook**, on the dark ground, with a "Photo coming soon" tag | `figure` is a top-level `core` block; the placeholder is `.ks3-figure-slot` (light, `52px 24px`, tag "Diagram coming soon") | **`{"type": "hook", "figures": ["id", "id"]}`** plus **`figures[].slot_label`** ("Photo coming soon" vs "Diagram coming soon") and a dark placeholder variant (§7.6) | the `hook` block record + `figures[]` |
| G6 | The formula statement panel: one centred display line, its own clamp | nothing; not an `explainer`, and **not** b1-01's `rule` block (§3.2.1 measures three differences) | **block type `formula`**: `{"type": "formula", "statement": "total magnification = eyepiece × objective"}` | `core[]` — §5.1.1 amendment |
| G7 | The formula triangle: 3 quantities, per-quantity cover geometry and rearrangement text | nothing | **`{"type": "formula", "triangle": {"top": {...}, "left": {...}, "right": {...}, "close": "..."}}`** — each quantity needs `label` (the SVG's short word), `button` ("Cover eyepiece") and `text`. **The cover-box geometry must be derived, not authored** — see §7.3 | the `formula` block record |
| G8 | The staged worked example: 4 steps, each with a letter, a name, a working line and a note; revealed one at a time | `fifa: {formula, insert, fix, answer}` — 4 flat strings, all shown at once, labelled Formula/Insert/Fix/Answer inside `.ks3-fifa` | **`fifa: [{letter, name, line, note}]`** (a list, not a dict) plus **`"staged": true`** and the three button labels | the `worked-example` activity record |
| G9 | The parallel attempt: 4 labelled/placeholdered fields, a model working, 4 criteria, its own tally copy | `construct` kind has `prompt` + `success[]`; nothing expresses fields or a model | **`activities[] {kind: "fifa-construct", fields: [{id, letter, label, placeholder}], model: ["F   …", …], success: [...], tally_met: "…"}`** | `activities[]` |
| G10 | The bench microscope's surface: objective segment, 3 figure readouts, live focus value, per-objective note, record table, 3/3 reveal, veil copy, eyepiece | `sim{kind, controls, readouts, specimens, caption}` — `readouts` is a list of **prose names the renderer ignores** (`r_sim` never reads it) | **`sim{... , "eyepiece": 10, "objective_control": "segment", "notes": {"40": "…", "100": "…", "400": "…"}, "record": {"columns": [...], "complete": "…"}, "veil": "…"}`** — and `readouts` either gains meaning or is removed | the `sim` record (§5.5) |
| G11 | Lab commit question + 3 options, **never scored** | `microscope-lab` carries `prompt`, `options`, **`answer: 1`** and a `reveal` — none of which the page uses; its own question and options differ | A ruling, not a field: either the gate's `answer`/`reveal` are dropped for `lab` kinds, or the page is wrong to omit the reveal. **F8** | the `lab` activity record |
| G12 | `.ks3-legal` = "Microscope lamps get hot and slides are glass…" | `LEGAL_LINE` is a fixed copyright/provenance line | **`safety_note: "…"`** — b1-01 G11's shape, unchanged, and a ruling on whether both lines render | top level |
| G13 | "At GCSE this becomes" as **prose**, while `ks4_links` is **non-empty** | `ks4_links: ["biology/cell-biology/microscopy"]` renders a link | **`ks4_becomes: "Magnification = image size ÷ actual size, and the electron microscope."`** — b1-01 proposed this as an *empty-list fallback*; here the list is populated and the page still renders prose, so **the prose is not a fallback, it is the field** | top level |
| G14 | Tutor card copy "Stuck on the calculation?" + CTA label + `href="#s-worked"` | generator hard-codes generic copy and a non-interactive `<span>` (`build_ks3.py:1013`) | **`tutor: {"prompt": "…", "cta": "…", "anchor": "s-worked"}`** — b1-01 G8's shape; note this page anchors at a **different** section, confirming the anchor is per lesson | top level |

Two of these (G2, G6) are new **block types**, which under MRB-203 cannot be rendered until the
registry knows them. G7, G8 change the shape of existing records (`fifa` from dict to list is a
**breaking** change to shipped data — two other KS3 lessons carry a `fifa` dict). G3, G9, G10 are new
shapes inside `activities[]`. G4 is a defect in shipped data that nothing currently catches.

---

## 6. Measurements

`--ks3-*` tokens in play: **60 resolvable on `.rd[data-mode="ks3"]`**, plus `--ks3-hue` and
`--ks3-season` empty — **identical to b1-01 §6**, enumerated the same way (walking every `@import`ed
sheet and reading `getPropertyValue` off `.rd`). The bundled `_ds/…/tokens/shared-ks3.css` was
verified **byte-identical to the repo's `shared/ks3.css`** (`diff` exit 0), and `styles.css` is five
`@import`s: `src-styles-tokens.css`, `shared-tokens.css`, `shared-ks3.css`, `fonts/fonts.css`,
`_ds_bundle.css`. So the page and the generator share one palette **and one stylesheet**.

b1-01's F13 confirmed and quantified here: `_ds_bundle.css` (1,312 lines) is the **3D Studio**
stylesheet (`--st-*` tokens). Its only rules that match anything on this page are
`* { box-sizing: border-box }` and `button { font: inherit; color: inherit; background: none;
border: none; padding: 0; cursor: pointer; text-align: inherit }` — enumerated by walking every sheet
and testing `Element.matches()` against a hook option. Both are outranked by every `.ks3-*` class
rule (the `button` reset is specificity 0,0,1). **It affects nothing**, and the generator loads no
such bundle.

### 6.1 Shell and type

| Property | 1280 | 1340 | 820 | 390 | Token or new |
|---|---|---|---|---|---|
| root font-size / line-height | 19px / 30.4px | = | = | = | bare (matches the inline `.rd` rule) |
| `.ks3-main` padding | 44px 24px 90px | = | = | 28px 16px 64px | bare (ks3.css) |
| `.ks3-main` max-width | 1320px | = | = | = | `--ks3-page` |
| `.ks3-lesson` max-width | 960px | = | = | = | `--ks3-wide` |
| `nav.ks3-nav` padding / border-bottom | 14px 24px 12px / 2px `--ks3-ink` | = | = | = | bare / token |
| nav height | 63.19 | 63.19 | **63.19** | **153.97** | measured |
| `.ks3-brand` | Bricolage 22px/800, lh 35.2, gap 10px, tile 34×34 r10 `--ks3-accent` | = | = | = | tokens + bare |
| breadcrumb `<ol>` | 17px / 22.1px, gap 9px, w 495.02 | = | = | w 342, h 53.19 | bare |
| h1 (`clamp(44px, 6vw, 74px)`, lh .94, ls −.035em) | **74px** / 69.56 | 74px | **49.2px** | **44px** | bare |
| `.ks3-bigq` | 25px/600, lh 1.35 (33.75), `--ks3-accent-text`, max-width 24ch = 406px | = | = | 358 | token colour |
| `.ks3-eyebrow` | 13px/700, ls .16em = 2.08px, uppercase, `--ks3-ink-muted` | = | = | = | token colour |
| `.ks3-lesson-head` | border-bottom 3px `--ks3-ink`, padding-bottom 28px | = | = | = | token |
| `.ks3-review-flag` | 16px/700 `--ks3-accent-text`, 313.41 wide | = | = | = | tokens |
| `.ks3-legal` | 15px/22.5 `--ks3-ink-muted`, border-top 1px `--ks3-rule`, padding-top 16px | = | = | = | tokens |
| `.ks3-footer` | 16px `--ks3-ink-muted`, `--ks3-card`, border-top 2px `--ks3-ink`, h 107.59 | = | = | = | tokens |

### 6.2 Block shells

| Block | radius | border | shadow | padding 1280 | padding 390 | ground |
|---|---|---|---|---|---|---|
| `.ks3-block` (`#s-method`, `#s-worked`, `#s-yours`) | 28px `--ks3-r-block` | 2px `--ks3-ink` | `5px 5px 0 --ks3-ink` (`--ks3-shadow-block`) | 30px | 22px 18px | `--ks3-card` |
| `.ks3-dark.ks3-hook` | 30px `--ks3-r-dark` | none | **`6px 6px 0 --ks3-accent`** | 32px | 22px 18px | `--ks3-ink` |
| `.ks3-dark.ks3-practical` (`#s-lab`) | 30px | none | **`6px 6px 0 --ks3-blue`** (#2F5CE0) | 32px | 22px 18px | `--ks3-ink` |
| `.ks3-dark.ks3-keynote` | 30px | none | **`6px 6px 0 --ks3-alert`** | 32px | 22px 18px | `--ks3-ink` |
| `.ks3-misconception` | 28px | 2px `--ks3-ink` | `5px 5px 0 --ks3-ink` | 30px | 22px 18px | **`--ks3-alert-tint`** |
| `#s-formula` (the `<section>`) | 0 | none | none | **0** | 0 | transparent |
| **formula statement** (inline) | 28px `--ks3-r-block` | **3px `--ks3-ink`** | none | **40px 32px** | 40px 32px (no narrow rule) | **`--ks3-band`** |
| **formula triangle** (inline) | 28px `--ks3-r-block` | 2px `--ks3-ink` | `--ks3-shadow-block` | 30px | 30px (no narrow rule) | `--ks3-card` |
| KEY FACT div (inline) | **20px `--ks3-r-panel`** | 2px `--ks3-ink` | **`5px 5px 0 --ks3-accent`** | **18px 22px** | 18px 22px | **`--ks3-band`** ✔ drift 5 |
| `.ks3-ladder` | 30px | **3px `--ks3-ink`** | **`6px 6px 0 --ks3-ok`** | 32px | 22px 18px | `--ks3-card` |
| `.ks3-layer-body` | **26px** | 2px `--ks3-stretch` | none | **26px 28px** | = | `--ks3-stretch-tint` |
| `.ks3-endmatter > section` | 22px `--ks3-r-card` | 2px `--ks3-ink` | none | 22px | = | `--ks3-card` (`.ks3-tutor`: `--ks3-accent`) |

Block spacing: `margin-top 28px` between sections, **24px** above the KEY FACT div, **34px** above
`.ks3-layer` / `.ks3-endmatter` / `.ks3-legal` — identical to b1-01. **Two panels take no narrow
padding rule**: the formula statement (40px 32px) and the triangle (30px), because they are inline
styles rather than `.ks3-block`. At 390 that leaves a 26px statement inside 32px of horizontal padding
in a 358px column. Not a defect; recorded because the generator emitting them as `.ks3-block` would
change them.

### 6.3 Grids

| Grid | 1280 | 1340 | 820 | 390 |
|---|---|---|---|---|
| hook figure pair (`auto-fit, minmax(230px,1fr)`, gap 16px) | 440 ×2 | = | 346 ×2 | **322 ×1** |
| hook options (`.ks3-options` flex column, gap 11px) | 896 | 896 | 708 | 322 |
| method list (flex column, gap 10px) | 896 ×6 | = | 708 ×6 | 318 ×6 |
| triangle grid (`auto-fit, minmax(260px,1fr)`, gap 26px) | 435 ×2 | = | 341 ×2 | **294 ×1** |
| worked list (flex column, gap 12px) | 896 ×4 | = | 708 ×4 | 318 ×4 |
| yours field rows (`46px minmax(0,1fr)`, gap 14px) | 46 + 836 | = | 46 + 648 | 46 + 258 |
| lab head (`flex, wrap, space-between, gap 20px`) | 351.58 + 339.66 | = | = | **322 + 322** |
| lab predict options (`auto-fit, minmax(240px,1fr)`, gap 11px) | 291.33 ×3 | = | 291.33 ×3 | 1-up |
| `.ks3-sim-controls` (flex wrap, gap 14px 26px) | 202.05 + 253 | = | = | 202.05 + 253 (wraps) |
| lab readouts (`auto-fit, minmax(180px,1fr)`, gap 18px) | 286.66 ×3 | = | 224 ×3 | **322 ×1** |
| recording table | 896 | 896 | 708 | **371.34 in a 322px parent** ⚠ F7 |
| ladder options (`.ks3-ladder .ks3-options`) | 280.66 ×3 | = | 332.5 ×2 | **296 ×1** |
| `.ks3-endmatter` (`auto-fit, minmax(250px,1fr)`, gap 16px) | 309.33 ×3 | = | 378 ×2 | 358 ×1 |

**Everything on this page collapses at 390 except the recording table and the triangle SVG.** Note
this differs from b1-01, whose hook split never collapsed — Design used `auto-fit` here, so that
finding does not recur.

### 6.4 Controls

| Control | size | radius | border | resting ground | chosen ground |
|---|---|---|---|---|---|
| `.ks3-option` (light, ladder) | 18px/600, `16px 18px`, 44px (`--ks3-tap`), gap 14px | `--ks3-r-option` 16px | 2px `--ks3-option-border` | `--ks3-ground` | `--ks3-accent-tint` + `--ks3-accent` |
| `.ks3-option` (on `.ks3-dark`) | same | 16px | 2px `--ks3-on-dark-muted` | `--ks3-dark-panel` | same panel, border → **`--ks3-alert`**; badge → `--ks3-alert`/`--ks3-ink` |
| `.ks3-opt-mark` | 28×28, r9, 15px/800 | — | — | `--ks3-band`/`--ks3-ink-muted` (dark: `--ks3-on-dark-muted`/`--ks3-ink`) | — |
| **method step** | 19px inherited / text span 18px/600 lh 1.45, `15px 18px`, 44px, `width:100%`, `text-align:left` | `--ks3-r-option` | 2px | `--ks3-ground`/`--ks3-option-border` | `--ks3-accent-tint`/`--ks3-accent` |
| **method step number** | 32×32, r10, Bricolage 17px/800 | — | — | `--ks3-band`/`--ks3-ink-muted` | `--ks3-accent`/`--ks3-on-dark` |
| **cover button** | **16px**/700, `11px 16px`, 44px, w 120.31/152.72/154.97 | `--ks3-r-control` 14px | 2px | `--ks3-card`/`--ks3-option-border` | **`--ks3-ink` fill** (inverted; drift 4) |
| **worked letter badge** | 40×40, r12, Bricolage 20px/800 | — | — | `--ks3-band`/`--ks3-ink-ghost` | `--ks3-accent`/`--ks3-on-dark` |
| **yours letter badge** | 40×40, r12, Bricolage 20px/800 | — | — | `--ks3-band`/**`--ks3-accent-text`** | (no second state) |
| **yours text input** | 19px, `13px 16px`, 44px, `width:100%` | `--ks3-r-option` | 2px `--ks3-option-border` | `--ks3-card` | — |
| **objective button** | 17px/700, `10px 16px`, 44px, w 55.58/63.30/67.17 | `--ks3-r-control` | 2px | `transparent`/`--ks3-on-dark-muted`, text `--ks3-on-dark` | **`--ks3-alert` fill** + `--ks3-ink` text |
| **focus range** | `min-width 11rem; max-width 15rem` → 240px, height 44px, `accent-color --ks3-accent` | — | — | — | — |
| **Record this row** | 17px/700, `13px 20px`, 44px | `--ks3-r-control` | 2px `--ks3-alert` | **`--ks3-alert` fill**, `--ks3-ink` text | — |
| `.ks3-reveal-btn` | 17px/700, `14px 22px`, 44px, `--ks3-ink` fill, `--ks3-on-dark` text | 14px | 2px `--ks3-ink` | — | locked: `disabled` + `opacity .45` + `cursor default` |
| `.ks3-check-btn` | 17px/700, `13px 20px`, 44px, `--ks3-band`, 2px `--ks3-ink`, `margin-top 14px` | 14px | — | — | — |
| `.ks3-retry` | 18px/700, `14px 24px`, 44px, `--ks3-ink` fill | 14px | 2px | — | — |
| `.ks3-answer` | 19px/30.4, `16px 18px`, **`rows="2"`, min-height 136px**, w 864 | 16px | 2px `--ks3-option-border` | `--ks3-card` | — |
| `.ks3-tick` checkbox | **25×25**, `accent-color --ks3-ok` | — | — | — | — |
| `.ks3-tutor-cta` | 18px/600 `--ks3-accent-text` on `--ks3-card`, `10px 17px`, `inline-flex` | **12px** | — | — | — |

Every interactive control on the page clears `--ks3-tap` (44px). **There is no 34px control here** —
b1-01's motion pill was the only sub-tap control in B1 and this page has no motion toggle.

### 6.5 Type inventory (resolved)

| Role | family | size | weight | line-height | ls | colour |
|---|---|---|---|---|---|---|
| h1 | DISPLAY | 74 / 49.2 / 44 | 800 | .94 | −.035em | `--ks3-ink` |
| `.ks3-hook-h` (`.ks3-hook h2`) | DISPLAY | 38 (30 ≤544) | 800 | 39.9 | −1.14px | `--ks3-on-dark` |
| `.ks3-block h2` (`#s-method`, `#s-formula`, `#s-worked`, `#s-yours`) | DISPLAY | 30 | 800 | 36 | −.75px | `--ks3-ink` |
| `#s-lab h2` (inline override) | DISPLAY | **34** | 800 | 37.4 (1.1) | −1.02px | `--ks3-on-dark` |
| `.ks3-ladder h2` | DISPLAY | 36 | 800 | 57.6 | −1.08px | `--ks3-ink` |
| `.ks3-rung h3` | DISPLAY | 23 | 800 | 36.8 | normal | `--ks3-accent-text` |
| **formula statement** | DISPLAY | **40 / 40 / 29.52 / 26** (`clamp(26px,3.6vw,40px)`) | 800 | 1.15 (46) | −.03em | `--ks3-ink`, **centred** |
| triangle SVG labels | DISPLAY | **27 / 23 / 23** (SVG units) | 800 | — | — | `--ks3-ink` |
| KEY FACT statement | DISPLAY | 22 | 700 | 29.7 | −.015em | `--ks3-ink` |
| `.ks3-keynote p` + its eyebrow | DISPLAY | 30 (24 ≤544) | 700 | 39 | −.02em | `--ks3-on-dark` / `--ks3-alert` |
| `.ks3-endmatter h2` | DISPLAY | 21 | 800 | 26.25 | −.01em | `--ks3-ink` |
| `.ks3-mis-badge` | DISPLAY | 19 | 800 | — | — | `--ks3-alert` on `--ks3-ink`, 32×32 r10 |
| body | BODY | 19 | 400 | 30.4 | — | `--ks3-ink` |
| `#s-method` / `#s-yours` intro (`max-width 52ch` = 658.008) | BODY | 19 | 400 | 30.4 (1.6) | — | `--ks3-ink` |
| method step text | BODY | 18 | 600 | 26.1 (1.45) | — | `--ks3-ink` |
| method verdict word | BODY | 17 | 700 | — | .04em (.68px) | `--ks3-alert-text` / `--ks3-ink-muted`, uppercase |
| method verdict body | BODY | 18 | 400 | 27.9 (1.55) | — | `--ks3-ink` |
| `.ks3-commit` | BODY | 22 | 700 | 29.7 | — | `--ks3-on-dark-body` |
| `.ks3-hook-prompt` | BODY | 19 | 400 | 31.35 (1.65) | — | `--ks3-on-dark-body` |
| hook figcaption | BODY | 17 | 400 | 27.2 | — | `--ks3-on-dark-muted` |
| figure placeholder tag | BODY | 14 | 700 | — | .1em (1.4px) | `--ks3-on-dark-muted`, uppercase |
| triangle rearrangement text | BODY | **20** | **600** | 32 (1.6) | — | `--ks3-ink` |
| triangle closing line | BODY | 17 | 400 | 26.35 (1.55) | — | `--ks3-ink-body` |
| worked step name | BODY | 16 | 700 | 25.6 | .1em (1.6px) | `--ks3-ink-muted`, uppercase |
| worked note | BODY | 17 | 400 | 25.5 (1.5) | — | `--ks3-ink-body` |
| `.ks3-crit-lead` | BODY | 15 | 700 | — | .12em (1.8px) | `--ks3-ink-muted`, uppercase |
| `.ks3-answer-label` | BODY | 16 | 700 | 25.6 | — | `--ks3-ink-muted` |
| `.ks3-mis-quote` | BODY | 19 | 700 | 30.4 | — | `--ks3-ink` |
| `.ks3-rung-q` | BODY | 21 | 600 | 29.4 | — | `--ks3-ink` |
| `.ks3-score` | BODY | 22 | 700 | 35.2 | — | `--ks3-ink`, right |
| `.ks3-fifa p` | BODY | 19 | 400 | 30.4 | — | `--ks3-ink` (its `<strong>` is DISPLAY) |
| `.ks3-tally` | BODY | 17 | 700 | — | — | `--ks3-ink-body` → `--ks3-ok-text` when met |
| `.ks3-layer-body p` | BODY | 19 | 400 | 32.3 (1.7) | — | `--ks3-ink` |
| lab aside (`max-width 30ch` = 339.66) | BODY | 17 | 400 | 27.2 | — | `--ks3-on-dark-muted`, right |
| lab veil (`max-width 34ch` = 417.384) | BODY | 18 | 700 | — | — | `--ks3-ink` |
| readout label | BODY | 16 | 400 | — | .1em (1.6px) | `--ks3-on-dark-muted`, uppercase |
| table `<th>` | BODY | 16 | — | — | .06em (.96px) | `--ks3-on-dark` on `--ks3-dark-panel`, uppercase |
| `.ks3-sim-figure` | MONO | **40** | 500 | 1 | — | **`--ks3-alert`** (on dark) |
| worked working line | MONO | **21** | 500 | 29.4 (1.4) | — | `--ks3-ink` |
| `.ks3-crit-wrap` model lines | MONO | **19** | 500 | 28.5 (1.5) | — | `--ks3-ink` |
| table body cell | MONO | 18 | 500 | — | — | `--ks3-on-dark-muted` → `--ks3-on-dark` |
| `.ks3-sim-value` | MONO | 15 | 500 | — | — | `--ks3-on-dark-muted` |
| rail count / method + worked + record progress | MONO | 15 | 500 | 24 | — | `--ks3-ink-muted` (`--ks3-on-dark-muted` in the lab) |
| KEY FACT label | MONO | 13 | 500 | 20.8 | .09em (1.17px) | `--ks3-accent-text` |
| rail node label | MONO | 11 | 500 | 13.2 | .09em (.99px) | state-dependent |

**Three MONO sizes are new relative to b1-01's inventory**: 40px (`.ks3-sim-figure`, a shipped class
b1-01 never rendered), 21px (the worked working line) and 19px (the model lines). Two BODY sizes are
new: 20px/600 (the triangle's rearrangement text) and the 14px/.1em placeholder tag.

### 6.6 Non-palette colours

Only one, and it is inside the canvas: **`#100D0A`**, the microscope's field ground, set both as the
canvas element's CSS `background` and by `ctx.fillStyle` in `draw()`. It matches nothing in the
60-token palette. `wireMicroscope` in the repo does not use it (it paints the outside of the field
with `#100D0A` in D6's renderer — worth a check when the two are joined). The inline engine's other
literals are all inside the drawing and were not measured through `getComputedStyle`: `#F2E4CB` (the
lit field), `#8A6A3C` / `#A98A5E` (cell walls, mid and outer layers), `#7A5A2E` (nuclei), `#4A4038`
(the inner eyepiece ring). **All five already live in `shared/ks3.js` as `ONION_MID`, `ONION_EDGE`,
`ONION_NUCLEUS` and the field paints**, with the comment that they are pigment on a slide rather than
interface chrome — so nothing new is needed.

---

## 7. New components — how to generate each

Seven components, in page order. Each states its data, markup, CSS, states and parity assertions.
Anything marked "assert" is a new `ks3_parity.COMPONENTS` entry.

### 7.0 Two carried from b1-01 unchanged

- **`rail`** — b1-01 §7.1's specification stands. Confirmed here at 6 stages: same threshold, same
  chip/label/connector geometry and tokens, same top-bar parts, same 92px anchors. The only additions
  are the §2.4 validation rule and the fact that `len(rail)` is genuinely variable across lessons.
- **`key-fact`** — b1-01 §7.2's specification stands, and this page's box is **byte-identical**:
  `--ks3-band`, `2px --ks3-ink`, `--ks3-r-panel`, `5px 5px 0 --ks3-accent`, `18px 22px`,
  `margin-top 24px`, MONO 13px/500 `.09em` uppercase `--ks3-accent-text` label, DISPLAY 22px/700
  lh 1.35 ls −.015em body. Two pages agreeing exactly is the strongest evidence in the delivery that
  this is a settled component.

### 7.1 `critique-steps` — the method critique

- **Data:** G3. Validate: `len(steps) >= 3`; every step supplies `fault`, `word` and `verdict`; at
  least one `fault: true` and at least one `false` (a critique with no sound steps teaches nothing);
  if the intro states a count of faults, it must equal `sum(fault)` — this page says "Three of the six
  steps will cost him" and three are flagged, and that agreement is exactly the kind of thing that
  drifts.
- **Markup:** `<section class="ks3-block" id="s-method" data-activity="…"><p class="ks3-eyebrow">…</p>
  <h2>…</h2><p class="ks3-method-intro">…</p><ol class="ks3-steps"><li><button type="button"
  class="ks3-step" aria-pressed="false"><span class="ks3-step-num" aria-hidden="true">1</span>
  <span class="ks3-step-text">…</span></button><div class="ks3-step-verdict ks3-reveal"
  data-reveal hidden><p class="ks3-verdict-word">…</p><p>…</p></div></li>…</ol>
  <div class="ks3-step-foot"><button class="ks3-reveal-btn">…</button><span
  class="ks3-progress">…</span></div></section>`
- **CSS:** step per §6.4 with `.is-picked`; number badge 32×32 r10 DISPLAY 17px/800;
  verdict `margin: 10px 0 0 46px; padding: 16px 18px; border-radius: var(--ks3-r-panel)` and two
  variants — `.is-fault { background: var(--ks3-alert-tint); border: 2px solid var(--ks3-alert-border) }`
  with the word in `--ks3-alert-text`, `.is-sound { background: var(--ks3-inset); border: 2px solid
  var(--ks3-rule-strong) }` with the word in `--ks3-ink-muted`. The `46px` indent is `32px badge +
  14px gap` — derive it, do not hard-code it twice.
- **States:** step unpicked / picked (2) × verdict hidden / fault / sound (3) × button locked /
  unlocked (2). Full matrix 2⁶ picks.
- **Assert:** (a) the step control is a **checkbox set** — more than one `aria-pressed="true"` is
  legal and toggling off decrements the counter; (b) the reveal button carries `disabled` at zero
  picks and the counter reads a words form ("Pick at least one"), not "0 picked"; (c) a verdict panel
  exists **only** under a picked step; (d) picking after opening reveals that step's verdict without a
  second press; (e) **no ✓/✗ glyph anywhere in the block** (R3 — the two-tone verdict is as far as
  this goes, and F3 must be settled before it goes further); (f) the verdict carries
  `class="ks3-reveal"` so the 220ms animation fires (F7).

### 7.2 `formula` — the statement panel

- **Data:** G6 — `{"type": "formula", "statement": "…"}`.
- **Markup:** `<div class="ks3-formula-statement"><p>…</p></div>` inside the `formula` section.
- **CSS:** `background: var(--ks3-band); border: 3px solid var(--ks3-ink); border-radius:
  var(--ks3-r-block); padding: 40px 32px; text-align: center`; the `<p>` DISPLAY 800
  `clamp(26px, 3.6vw, 40px)` lh 1.15 ls −.03em `--ks3-ink`, **no `max-width`**.
- **States:** one.
- **Assert:** `text-align: center` and `max-width: none` — these are what distinguish it from b1-01's
  `rule` statement, which is left-aligned at `20ch`; the border is 3px (not the 2px of a
  `.ks3-block`); there is **no shadow**; and the clamp is the **formula** clamp, not drift 3's ruled
  statement clamp. A parity pair asserting "formula statement ≠ rule statement" is worth having,
  because the two shells are otherwise identical and a future tidy-up will merge them.

### 7.3 `formula-triangle` — the covered triangle

- **Data:** G7. Three quantities, each `{label, button, text}`, plus a `close` line, plus which
  quantity is the numerator. Validate: exactly 3 quantities; the top one is the product of the other
  two (statable, since the statement is `a = b × c`); every `label` is ≤ 6 characters (they sit inside
  an SVG at 23–27 units and will not wrap).
- **Markup:** the `.ks3-block` shell, then eyebrow, `<h2>`, then a 2-column grid with
  `<svg class="ks3-triangle" viewBox="0 0 260 216" role="img" aria-label="Formula triangle: …">`
  (path, two dividers, three `<text>`, one `<rect class="ks3-triangle-cover">`) and a control column
  of three `aria-pressed` buttons + `<p class="ks3-triangle-text">` + `<p class="ks3-triangle-close">`.
- **CSS:** shell `--ks3-card` on `2px --ks3-ink`, `--ks3-r-block`, `var(--ks3-shadow-block)`,
  `padding 30px`; grid `repeat(auto-fit, minmax(260px, 1fr))` gap 26px `align-items:center`; buttons
  per §6.4 (16px/700, `11px 16px`, 44px, `--ks3-r-control`, inverted ink on-state); triangle fill
  `--ks3-inset`, stroke `--ks3-ink` sw 4 `stroke-linejoin: round`; cover fill `--ks3-ink` at
  `opacity .92`.
- **Cover geometry must be DERIVED, not authored.** The three boxes (`62,62,136,52` · `46,146,78,48` ·
  `136,146,78,48`) are a function of the fixed 260×216 viewBox and the divider positions at y=130 and
  x=130 — the top box spans the upper cell, the two lower boxes the halves of the lower cell.
  Authoring twelve magic numbers per lesson is exactly the hand-authoring the generator removes, and
  it is the thing that produced F1's four console errors. **Emit them from the geometry.**
- **States:** three, one always on; default = the numerator.
- **Assert:** (a) exactly one button `aria-pressed="true"` at all times, including at first paint;
  (b) the cover rect is never `opacity: 0` — there is no uncovered state; (c) the rect's box lies
  wholly inside the triangle path; (d) the three SVG `<text>` labels, the three button labels and the
  statement's three quantity names are **checked against each other** (F4 — the page has three
  vocabularies today); (e) the SVG has a `role="img"` and an `aria-label` naming all three positions,
  because the whole mechanism is spatial; (f) the SVG scales below 260px (F6).

### 7.4 `worked-stepper` — the staged FIFA worked example

- **Data:** G8 — `fifa: [{letter, name, line, note}]`, 2–6 steps, plus `staged: true` and the three
  button labels. Validate: every step has all four keys (the existing dict has no `name` and no
  `note`); `letter` is 1 character; `line` is the working, `note` the teaching.
- **Markup:** `.ks3-block` shell, eyebrow, `<h2>` **carrying the question** (see §3.3), then
  `<ol class="ks3-worked"><li class="ks3-worked-step"><div><span class="ks3-worked-letter"
  aria-hidden="true">F</span><div><p class="ks3-worked-name">Formula</p><p class="ks3-worked-line
  ks3-reveal" data-reveal hidden>…</p><p class="ks3-worked-note ks3-reveal" data-reveal
  hidden>…</p></div></div></li>…</ol>` + the foot (button + MONO progress).
- **CSS:** `li` `padding 16px 18px`, `--ks3-r-panel`, closed `--ks3-row-dim` on `2px --ks3-rule`,
  `.is-open` `--ks3-inset` on `2px --ks3-ink`; letter 40×40 r12 DISPLAY 20px/800, closed
  `--ks3-band`/`--ks3-ink-ghost`, open `--ks3-accent`/`--ks3-on-dark`; name 16px/700 `.1em` uppercase
  `--ks3-ink-muted`; line MONO 21px/500 lh 1.4; note 17px lh 1.5 `--ks3-ink-body`.
- **States:** `0 … len(fifa)` (5 here), and the button's three labels.
- **Assert:** (a) at step 0 **no** `line` or `note` is in the DOM — Law 5's model must not be readable
  before the student asks for it; (b) exactly `n` steps are open after `n` presses; (c) the button
  carries `disabled` at the end and its label changes to a completed form; (d) the working lines are
  MONO and the notes are BODY (the line is a live-number role, §6.5); (e) both revealed paragraphs
  carry `class="ks3-reveal"` (F7); (f) **this component and `.ks3-fifa` are not the same thing** —
  see F11.

### 7.5 `fifa-construct` — the parallel attempt

- **Data:** G9 — `fields`, `model`, `success`, `tally_met`. Validate: `len(fields) == len(model) ==
  len(success)` (four here, and the criteria are written one per FIFA step); every field has a
  placeholder; the model's letters match the fields' letters in order; **the paired
  `worked-example`'s `fifa` letters match these fields' letters** — Law 5's "the same artifact" is a
  checkable claim.
- **Markup:** `.ks3-block` shell, eyebrow, `<h2>` (the question), intro `<p class="ks3-measure-52">`,
  then a column of `<div class="ks3-fifa-row"><span class="ks3-fifa-letter" aria-hidden="true">F</span>
  <span><label class="ks3-answer-label" for="…">Formula</label><input type="text" id="…"
  class="ks3-fifa-input" placeholder="…"></span></div>`, then `.ks3-check-btn`, then the
  `.ks3-crit-wrap` (existing class) holding `.ks3-crit-lead`, `<ol class="ks3-model">` of MONO lines,
  `ul.ks3-ticks` and `p.ks3-tally`.
- **CSS:** row `grid-template-columns: 46px minmax(0, 1fr); gap: 14px; align-items: center`; letter
  40×40 r12 DISPLAY 20px/800 `--ks3-band`/**`--ks3-accent-text`**; input 19px `13px 16px` 44px
  `--ks3-r-option` `2px --ks3-option-border` on `--ks3-card`; model line MONO 19px/500 lh 1.5.
  Everything from `.ks3-crit-wrap` down is already shipped.
- **States:** unchecked / checked (2) × 0..4 ticks (5) × per-field empty / filled.
- **Assert:** (a) **the Check button is gated on at least one non-empty field** — the model working is
  the answer and it must not be free (F5; this is an addition inside a component Design drew and
  contradicts nothing on the page); (b) **the typed value survives a re-render** — emit
  `<input>` without a `value` attribute and hold the text in the DOM, exactly as the generator's
  `_rung_self` already does for `<textarea>` (F5); (c) the tally's met copy is the **block's own**, not
  the ladder's ("you can do this one on your own" ≠ "rung met"); (d) this block's tally never changes
  the ladder score; (e) the letter badge is `--ks3-accent-text` on `--ks3-band`, i.e. quieter than the
  worked example's open badge — that contrast is the "yours to fill" signal.

### 7.6 `bench-microscope` — the instrument's surface

The engine is already the repo's (`wireMicroscope`, reconciled under MRB-210). What is new is
everything around the canvas.

- **Data:** G10, plus the ruling on F9 (specimen selector or not).
- **Markup:** `<div class="ks3-sim" data-sim="microscope" data-controls="magnification,focus"
  data-specimens="[…]"><canvas class="ks3-sim-canvas" width="1120" height="560" role="img"
  aria-label="…"></canvas><p class="ks3-sim-cover">…</p><div class="ks3-sim-controls"></div>
  <ul class="ks3-sim-figures">…</ul><p class="ks3-sim-caption"></p>
  <div class="ks3-sim-record">…<table>…</table><div class="ks3-reveal" data-reveal hidden>…</div>
  </div></div>` inside the `[data-activity]` section so R5's gate still runs on the adjacency.
- **Three things the shipped CSS/JS must change**, each a one-line consequence of the measurements:
  1. **`.ks3-sim-cover`'s `aspect-ratio: 560 / 220` is wrong for this canvas.** The generator's canvas
     is 560×220 (2.545:1); Design's is 1120×560 (2:1). The shipped comment says the two numbers are
     "one number in two files" — they now need to be one number in *one* file, or the veil stops
     covering the frame. Cleanest fix: `inset: 0` on a positioned wrapper, as Design does, which
     removes the coupling entirely.
  2. **The magnification control must be able to render as a segment**, labelled by *objective*
     (`×4 ×10 ×40`), not as a `<select>` labelled by total (`×40 — lowest lens`). Both namings are
     defensible and Design chose the objective, which is what is written on a real turret.
  3. **`.ks3-sim-caption` cannot be both** the authored static caption and the live per-objective
     note. Two classes, or one class and a second element. Code's call, §8(c).
- **Readouts:** three `.ks3-sim-figure` numerals with uppercase labels, **derived by the engine**
  (`mag()`, `fovText()`, `cellsAcross(CELL_W)`) rather than authored, plus the existing
  `.ks3-sim-value` beside the slider, plus the per-objective note. The prose `.ks3-sim-readout` the
  generator emits today has no home on this page — but it is the accessible summary, so it should
  stay as a visually-hidden `role="status"` rather than be dropped.
- **States:** locked / open (2) × 3 objectives × 101 focus positions × 2⁰..2³ recorded rows ×
  table complete / not.
- **Assert:** (a) the canvas is blurred **and** veiled while locked, and neither alone; (b) the
  controls, readouts, record button and table are **absent from the DOM** until a prediction exists
  (Law 4); (c) every figure readout the page prints equals what the engine computes — assert
  `fov == 180/mag` and `cells == fov/0.30` printed with the half (`1½`, not `2`), because that
  disagreement is the defect MRB-210 exists to prevent; (d) the depth-of-field figures the readouts
  quote come from `OBJ_DOF_MM` and from nowhere else; (e) **the per-objective note's claim about how
  many layers hold at once is checked against the engine** — a parity assertion that recomputes
  `nSharp` over all 101 wheel positions and fails if the copy claims a number the optics cannot
  produce. This is the assertion that would have caught F10; (f) recording is idempotent per
  objective; (g) no ✓/✗ anywhere in the block (R3) and the gate's options are never marked.

### 7.7 `photo-placeholder` — the dark pending-figure variant

- **Data:** G5 — `figures[].slot_label` plus a hook that can carry `figures: [id, id]`.
- **Markup:** the existing `figure.ks3-figure.ks3-figure-pending` shape, with the slot and tag classes
  gaining a dark variant through `.ks3-dark` context rather than a new class.
- **CSS:** `.ks3-dark .ks3-figure-slot { height: 168px; padding: 0; border-radius: 20px;
  border: 3px dashed var(--ks3-on-dark-muted); background: var(--ks3-dark-panel) }` and
  `.ks3-dark .ks3-figure-tag { background: var(--ks3-ink); border-color: var(--ks3-on-dark-muted);
  color: var(--ks3-on-dark-muted); padding: 8px 15px; border-radius: var(--ks3-r-pill) }`; caption
  `.ks3-dark .ks3-figure figcaption { color: var(--ks3-on-dark-muted) }` at 17px/1.6.
  Note the **fixed 168px height** rather than the light variant's `padding: 52px 24px` — a 2-up pair
  needs equal heights, which padding alone cannot guarantee.
- **States:** `needed` / `drafted` / `final` (the existing `status` enum), × light / dark ground.
- **Assert:** the tag word comes from data ("Photo coming soon" here, "Diagram coming soon" in the
  light default) — a micrograph is not a diagram and §4.10's own note says the two sourcing efforts
  must not be merged; the dark variant's dashed frame is `--ks3-on-dark-muted`, never `--ks3-rule-strong`
  (which is invisible on ink); both figures in a pair resolve to the same height.

---

## 8. Ambiguities and findings

**(a) Needs Design.**

- **F2 — the formula clamp.** `clamp(26px, 3.6vw, 40px)`, centred, `max-width: none`. Confirmed a
  distinct role from drift 3's statement clamp, exactly as `00-delivery-drift.md` ruled. But b1-02 is
  the only B1 lesson with a formula, so one page is the entire evidence base for what a formula
  statement's type ramp is. Is `26 / 3.6vw / 40` the formula role, or is it b1-01's statement clamp
  with the numbers nudged? Not resolvable from the delivery.
- **F4 — three vocabularies for two quantities on one screen.** The statement says
  "eyepiece × objective"; the triangle's SVG says "eye" and "obj"; the buttons say "Cover eyepiece"
  and "Cover objective". The abbreviations are forced by the SVG's 260-unit width, so this is a real
  constraint rather than carelessness — but a student reading "obj" has to map it back twice. Does the
  triangle want a wider viewBox and the full words, or is the abbreviation deliberate?
- **F6 — the triangle SVG does not scale.** Measured `260×216` at 1280, 1340, 820, **390 and 360** —
  fixed `width`/`height` attributes with no `max-width: 100%`. It fits at 390 (294px column) and at
  360 (264px column) with 4px to spare, so **nothing is broken today**; below ~356px viewport width it
  would overflow. One `max-width: 100%; height: auto` fixes it, but that changes an approved page's
  narrow rendering, so it is stated rather than assumed.
- **F8 — Law 4's second clause, again.** The lab's prediction gates the instrument and is then erased
  from the DOM, never scored, never answered. The authored payload carries `answer: 1` and a `reveal`
  for this exact activity and the page uses neither; the table-complete panel is the closest thing to
  a reveal and it never refers to what was predicted. b1-01's F5 asked this about its board; two
  pages agreeing means it is a **pattern**, and the question is whether Law 4's "the reveal answers
  the prediction right/wrong in tone tokens" has been superseded in practice.
- **F9 — the missing specimen selector.** Fully stated in §3.5.2. Design's page draws two controls;
  the authored payload declares three specimens, `build_ks3.py` hard-fails without them, and the
  authored reveal depends on switching between two onion slides to confront CELL-01. Both readings of
  standing law are defensible. **Recorded, not resolved.**
- **Drift 4, third sighting.** The cover buttons are b1-06's ruled segment geometry at 16px with
  b1-03's inverted ink on-state. b1-01's specimen tabs were the second sighting. Three pages carrying
  the inversion is enough to close the drift file's open flag one way or the other.

**(b) Needs Mide (science / content).**

- **F10 — the ×100 sharpness note is false under the ruled table.** Verbatim: *"At ×100 two layers are
  nearly sharp together. There is still depth to spare."* Under `OBJ_DOF_MM = [0.100, 0.040, 0.008]`
  the ×100 sharp window is **±0.024 mm** against layers **0.055 mm** apart, so two layers can never be
  inside it — measured in the running engine and verified by enumerating all 101 wheel positions
  (maximum layers sharp = **1**, at every position; 76 of 101 positions have any layer sharp). The
  line was **true on the page's own superseded table** (window ±0.054 mm), so this is reconciliation
  fallout, not authoring error. The ×40 line survives (all three layers hold, but only near the middle
  of the travel); the ×400 line survives and strengthens (window ±0.0048 mm, ~24× thinner than one
  cell, 12 of 101 positions sharp). **The corrected copy is deliberately not written here** — it is a
  science correction on a line a student reads as settled. The true behaviour to write from: at ×100
  the loss of depth has *already started*, not "there is depth to spare".
- **The approved page and the authored data teach overlapping but different lessons.**
  `ks3_data/biology_b1_cells.py` L2 opens on *"a real student's slide"* covered in bubbles, with
  `big_question: "Why does almost everybody's first slide show nothing at all?"`, and its spine is
  bubbles → drawing standards → the lab. Design's approved page opens on **two photographs of the
  same onion at ×100 and ×400**, asks *"Turn it up to the highest magnification and you see almost
  nothing. Why?"*, and its spine is critique-the-method → the formula → the bench. **Under standing
  law the approved page wins**, which re-authors the record — roughly **1,139 words of new
  science-bearing content** (six method verdicts, four worked notes, three sharpness notes, three
  rearrangement texts, six ladder corrections, twelve success criteria) and drops the bubbles framing
  that CELL-01 and the `bubble-or-cell` confrontation both hang on. It arrives at once and needs the
  examiner gate.
- **Two specific claims worth Mide's eye because the page teaches them as settled.** (i) The method
  verdict on step 3: *"That is 0.45 mm of slide in view. He is hunting for something the width of a
  hair in the dark. Start on ×4, where he can see 4.5 mm at once."* — the 0.45/4.5 mm figures agree
  with the engine (`180/400` and `180/40`), so the arithmetic is sound; the "width of a hair"
  comparison is the part to check. (ii) The stretch layer's derivation: *"Printed on the eyepiece is a
  field number — on these ones, 18. Divide it by the objective and you get the field of view in
  millimetres. Because this eyepiece is ×10, dividing 180 by the total magnification gives the same
  answer."* This is the only place in KS3 that explains where `FIELD_AT_1X_MM = 180` comes from, and
  it is correct as written — but it is doing real optics in a stretch box, and Mide should see it.
- **`covers` is `["KS3.WS.EXP.05", "KS3.B.CELLS.01b"]`.** §5.7.1 requires an INVESTIGATION lesson to
  anchor on WS, which this does. Whether the approved page — which now spends its middle on a
  *calculation* rather than on method-and-measurement — still teaches `KS3.WS.EXP.05` is a curriculum
  judgement. The critique block does; the formula/worked/yours trio (three of the six rail stages) is
  QUANTITATIVE work inside an INVESTIGATION lesson.

**(c) Code's call — recorded, not asked.**

- **F1 — four console errors at load.** `<rect> attribute x/y/width/height: Expected length,
  "{{ coverX }}"`. SVG geometry attributes are typed and reject the DC placeholder in the
  pre-hydration parse. The generator emits static values, so the errors do not survive the port. The
  useful signal is §7.3's: the cover geometry should be **derived from the viewBox**, not authored as
  twelve numbers. Code takes that.
- **F3 — the method critique marks the student's picks in two tones.** "COSTS HIM" on amber vs "SOUND"
  on inset is a verdict on a pick, with no glyph and no score. R3 says only the ladder marks. This
  reads as inside the line (a critique block that never told you whether you were right would be
  useless), and the page wins under standing law either way — but it is the first non-ladder block in
  B1 to evaluate a choice, and it should be recorded as a **deliberate exception with a boundary**:
  two tones and a word, never a glyph, never a count.
- **F5 — `#s-yours` loses the typed working and checks an empty attempt.** Both measured. `<input
  value="{{…}}">` sets an attribute the element reads only as a default, so the student's working
  disappears on the first tick while `state.mine` still holds it; and "Check my working" reveals the
  full model with four blank fields. The generator's own `_rung_self` already avoids the first defect
  for `<textarea>`, so the port fixes it by construction — but it must be **tested, not assumed**, and
  the empty-check gate is an addition inside a component Design drew that contradicts nothing on the
  page. Recommend both.
- **F7 — five `data-reveal` elements without `class="ks3-reveal"`.** The six method verdicts, the eight
  worked lines/notes, and the table-complete panel all carry `data-reveal="1"` alone, so
  `animation-name` resolves to `none` and `shared/ks3.css`'s 220ms reveal never fires. Two of the
  page's reveals *do* animate (the hook's `.ks3-reveal`, and `.ks3-crit-wrap`) — so the page is
  internally inconsistent, not deliberately still. b1-01 found the same on its sort evidence. Add the
  class.
- **F11 — `.ks3-fifa` is doing a second job.** `build_ks3.py` emits the *worked answer* into
  `.ks3-fifa` (Formula / Insert / Fix / Answer, all four lines at once). Design uses `.ks3-fifa` inside
  **ladder rung 2** to hold the *method as instructions* ("F — write the formula down before anything
  else."), and puts the worked answer in `#s-worked`'s staged stepper instead. Both are legitimate; one
  class cannot be both. Recommend `.ks3-fifa` keeps the **scaffold** job Design gives it (it is the
  better use — a reminder beside a question the student is about to answer) and the worked answer moves
  to §7.4's component. Note that changing `fifa` from a dict to a list (G8) is a **breaking change to
  two other shipped KS3 lessons**, so it needs a migration in the same commit.
- **F7b — `.ks3-sim-caption` is doing a second job.** The generator's is the authored static caption;
  Design's is the live per-objective note. Two elements or two classes. Code's call.
- **F12 — the recording table overflows the viewport below ~405px.** Measured: `documentElement
  .scrollWidth = 405` against a 390px viewport, and 405 against 360 — the table is 371.34px wide in a
  322px parent with `overflow-x: visible`, and the four uppercase 16px `<th>` cells with `10px 12px`
  padding cannot compress below ~96.8px each. **The whole page scrolls sideways by 15px on a phone**,
  which is the one measured defect on this page that a student would actually feel. The fix is a
  `overflow-x: auto` wrapper round the table (README's own rule for wide content), which changes an
  approved page's narrow layout only in the direction of working. Recommend it; state it in the build
  report.
- **F13 — the misconception block has no activity.** `#s-think` is `.ks3-mis-head` + `.ks3-mis-quote` +
  two prose paragraphs. The generator's `misconception` renderer emits eyebrow + badge + quote +
  prompt + gated reveal, and Law 3 asks for a *confrontation*, not a paragraph. This block confronts
  nothing — it summarises the lab that came before it ("Your own table says it: at ×400 there are
  fewer than two cells in front of you"). Arguably the confrontation already happened in `#s-lab` and
  this is the debrief, which is a coherent reading of Law 3 with the lab in front of it. Recorded so
  the port does not silently add a prompt-and-reveal Design did not draw.
- **`ks3-hook-h` is an inert class** (styled by `.ks3-hook h2`), on a second page now. Drop it.
- **Class-set note, confirmed again:** Design writes `class="ks3-ladder"` where the generator writes
  `class="ks3-block ks3-ladder"`, and both resolve to the same painted shell (3px ink, r30,
  `6px 6px 0 --ks3-ok`) — measured here for the single-class case, same as b1-01. Worth a parity
  assertion rather than a change.
- **The settle trap.** Recorded at the top of this file and repeated here because it will bite the
  build run: a 450ms settle is **not** enough on this page. Any state driven by
  `aria-pressed` + a `transition: border-color .16s` reads its pre-transition value unless the probe
  forces a reflow and waits ~700ms. b1-01's numbers were taken at 450ms and happened to be right;
  this page's were not, and the first pass produced a false "the chosen dark option never changes
  border" that took four probes to unwind.

**Could not measure.**

- **Rail geometry above 1341px** — checked arithmetically from the measured `left: calc(50% − 632px)`
  and the 1320px `--ks3-page` cap, not by device-metrics override. Same gap as b1-01.
- **`:hover` states** — `.ks3-option:hover { transform: translateX(3px); border-color: var(--ks3-accent) }`
  is read from the shipped stylesheet, not driven; CDP mouse-move hover was not exercised. Note that
  the hover rule sets `border-color: --ks3-accent` even on `.ks3-dark`, where the chosen state is
  `--ks3-alert` — so hovering a dark option briefly shows the *light* chosen colour. Read from source,
  **not measured**, and worth a probe in the build run.
- **The canvas drawing itself.** The onion field is painted by the page's inline `draw()` and was not
  pixel-compared against `wireMicroscope`'s output. Two full focus sweeps (3 objectives × 101
  positions) **crashed the headless renderer** — `ctx.filter = 'blur(Npx)'` over ~2,300 rounded rects
  per frame at ×4 exhausted it and Chrome closed the websocket mid-frame. The focus-value sweep in
  §3.5.3 was therefore computed from the page's own source (a pure function of `focus`, `LAYERS` and
  `dof`) and **spot-verified in the browser at 7 wheel positions × 3 objectives**, all 21 agreeing.
  The blur *rendering* is unverified. Recorded because it also predicts a real performance problem: a
  1120×560 canvas with per-layer canvas filters is heavy enough to kill a renderer, and students'
  phones are slower than this machine.
- **Reduced motion** — nothing to measure. `data-motion` is absent, `[data-anim]` count is 0, and the
  page authors no `prefers-reduced-motion` query. Once the repo's engine (which animates the pond and
  the zoom transition) replaces the inline one, Law 9's reduced-motion path becomes live on this page
  and will need measuring for the first time.
- **The `320px` viewport** was out of scope; 360 was probed only for F12. No `print` stylesheet exists.
