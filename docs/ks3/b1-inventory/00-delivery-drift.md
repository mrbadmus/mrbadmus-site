# B1 delivery drift — five values the generator needs one of

Measured 13 Aug 2026 against `docs/ks3/design-reference/b1/`, the six approved
pages as delivered (provenance commit: Design's B1 unit, exactly as delivered).

Design hand-writes each lesson as a standalone HTML file. Six files written in
sequence drift, and they have. None of these five is a decision anybody made —
they are the residue of hand-authoring, which is exactly what a generator
removes. Each needs one value. Below: every occurrence, the count, the ruled
value, and why it wins.

Where the count and the better answer disagree I have said so explicitly rather
than hiding behind the majority, so Mide can overrule in one line.

---

## Drift 1 — the bench grid's control column: 232px or 240px

`[data-bench-grid]` is the practical block's two-column layout: a fixed control
column beside a flexible canvas.

| Page | Line | Declaration |
|---|---|---|
| b1-03 animal-and-plant-cells | 20 | `[data-bench-grid] { grid-template-columns: minmax(0, 240px) minmax(0, 1fr); }` |
| b1-04 specialised-cells | 20 | `[data-bench-grid] { grid-template-columns: minmax(0, 232px) minmax(0, 1fr); }` |
| b1-06 unicellular-organisms | 20 | `[data-bench-grid] { grid-template-columns: minmax(0, 232px) minmax(0, 1fr); }` |

**Count: 232px × 2, 240px × 1.**

### ⚖️ Ruled: `232px`

Majority, and nothing else distinguishes them. The difference is 8px on a
control column and carries no semantic content — both are on the 8px step the
rest of the system uses. b1-03 is the earliest of the three pages to declare the
grid, and the two later ones agree with each other.

**Not to be confused with** a separate `repeat(auto-fit, minmax(Npx, 1fr))` on
b1-01 line 222 (232px), b1-02 line 274 (240px) and b1-04 line 217 (232px). That
is the **options grid**, a different element with its own job. It carries the
same 232/240 split and wants the same ruling for the same reason, but it is a
second component, not more evidence about this one.

---

## Drift 2 — the bench grid's collapse breakpoint: 780px or 820px

| Page | Line | Declaration |
|---|---|---|
| b1-03 animal-and-plant-cells | 21 | `@media (max-width: 780px) { [data-bench-grid] { grid-template-columns: minmax(0, 1fr); } }` |
| b1-04 specialised-cells | 21 | `@media (max-width: 780px) { … }` |
| b1-06 unicellular-organisms | 21 | `@media (max-width: 820px) { … }` |

**Count: 780px × 2, 820px × 1.**

### ⚖️ Ruled: `820px` — against the count, deliberately

This is the one place I have not followed the majority, and the reason is on the
record rather than in taste.

MRB-210 records that Design went back to B1-06 specifically to fix its
narrow-width behaviour, and fixed the comparison rows to restyle under
`max-width: 820px` — the dark header row hides and each content cell grows its
own mono caption. So **820px is already a ruled threshold on that page**, for a
different component, and it is the most recently considered narrow-width
decision in the delivery.

Two thresholds 40px apart on one page means a viewport between 780 and 820 gets
a two-column bench grid beside stacked comparison rows. One threshold per page
is the coherent outcome, and 820 is the one that was actually thought about.

It is also the kinder of the two. Collapsing *earlier* means that at an 800px
viewport the student gets a full-width stacked layout instead of a 232px control
column crushing the canvas into ~500px. The failure mode of collapsing too late
is a cramped instrument; of collapsing too early, a slightly tall page.

**If Mide prefers the majority, 780px costs nothing to adopt** — it is one
number in one place once the generator owns it.

---

## Drift 3 — four type sizes for one statement role

| Page | Line | Declaration | Role |
|---|---|---|---|
| b1-01 life-processes | 238 | `font-size: clamp(30px, 4.2vw, 46px)` | statement |
| b1-02 using-a-microscope | 149 | `font-size: clamp(26px, 3.6vw, 40px)` | **formula** statement (`ks3-font-display`) |
| b1-03 animal-and-plant-cells | 227 | `font-size: clamp(28px, 3.9vw, 44px)` | statement |
| b1-04 specialised-cells | 214 | `font-size: clamp(28px, 3.9vw, 44px)` | statement |
| ~~b1-05 levels-of-organisation~~ | ~~132~~ | ~~`font-size: 30px`~~ | ⊖ **not a statement — see the correction below** |
| b1-06 unicellular-organisms | 217 | `font-size: clamp(26px, 3.6vw, 40px)` | statement |

### ⚖️ Ruled: `clamp(28px, 3.9vw, 44px)` for the statement role

Four distinct declarations, but they are not four candidates for one role:

- **b1-02 is a different role.** It is the formula statement carrying
  `ks3-font-display` under MRB-204's triangle treatment, not a prose statement.
  It should follow whatever MRB-204's formula components rule, and it is not
  evidence about this one. Excluding it leaves three clamp families and one
  page with no clamp.
- Of the three, `clamp(28px, 3.9vw, 44px)` is both the **modal** value (b1-03,
  b1-04) and the **median** of the three (46 / 44 / 40 at the cap). It is the
  middle answer and the most common one, which is as close to consensus as six
  hand-written pages get.

### ⊖ CORRECTION, 13 Aug 2026 — the b1-05 row was the wrong element

**Withdrawn: the ⚑ flag this section originally carried.** It read that b1-05's
statement is a flat un-clamped 30px and that the ruling would take it to 44px —
"a visible change to an approved page". That was wrong, and it was wrong in the
direction that would have cost Mide a decision he does not need to make.

b1-05 line 132 is not a statement. It is `{{ levelName }}` — a **templated live
readout heading inside the zoom instrument's panel**, on `--ks3-inset` behind a
2px ink border. **b1-05 has no statement panel at all**: zero hits for `#s-rule`
or "What settles it". Verified directly in the source.

So the statement role has **four** occurrences across the delivery, not six, and
they are b1-01, b1-03, b1-04 and b1-06. `clamp(28px, 3.9vw, 44px)` is still both
the modal and the median of those, so **the ruling itself is unchanged and its
basis is now cleaner** — it no longer rests on a mis-read row.

Applying the ruling touches nothing on b1-05, because there is nothing there to
apply it to. **b1-05 is an exclusion from this role, exactly as b1-02's formula
statement is** — one page has a formula where the statement would go, and this
one has an instrument.

The measured cost of applying the clamp to that readout anyway, had anyone: +16px
of document height at 1280 and 1340, +2px at 820, and **−5px at 390** (the 28px
floor makes it smaller on a phone). Nothing wraps that did not already wrap. The
objection is not layout, it is meaning — it would make an instrument caption the
largest body-level type on the page, above the 22px key fact.

**How it happened, since the class of error matters more than the instance.** The
role column in the table above was assigned by pattern-matching a large
display-font declaration, not by asking what the element *is*. Four of the six
rows were statements; two were not. A generator built from the original table
would have emitted a statement component into an instrument panel.

---

## Drift 4 — `seg()`, four incompatible light variants under one name

Every page defines `seg(on, dark)` to style a segmented control. **The `dark`
branch is byte-identical in all four.** Only the light branch differs.

| Page | Line | Light branch |
|---|---|---|
| b1-03 | 934 | 17px / `11px 17px` / 44px / `r-control`; on-state **inverted** — `background: var(--ks3-ink)`, `color: var(--ks3-on-dark)` |
| b1-04 | 967 | `width:100%`, `text-align:left`, `12px 14px`, **56px**, `r-option`; accent tint |
| b1-05 | 739 | **16px** / `9px 13px` / 44px / `r-control`; accent tint |
| b1-06 | 887 | 17px / `11px 17px` / 44px / `r-control`; accent tint |

### ⚖️ Ruled: b1-06's variant is the segmented control

```
cursor:pointer; font:inherit; font-size:17px; font-weight:700;
padding:11px 17px; min-height:44px; border-radius:var(--ks3-r-control);
border:2px solid  <on ? --ks3-accent : --ks3-option-border>;
background:        <on ? --ks3-accent-tint : --ks3-ground>;
color:             var(--ks3-ink);
```

It wins on a real property rather than a headcount: **it is the only light
branch whose geometry matches the dark branch of the same helper.** Both are
17px, `11px 17px`, 44px, `r-control`. One helper should produce one control in
both grounds, differing in colour and not in size — otherwise a segment
physically moves when it lands on a dark block. b1-05's 16px/`9px 13px` is the
same control 1px smaller for no stated reason.

### Two of the four are not drift, and must not be folded in

- **b1-04's is not a segmented control at all.** `width:100%`,
  `text-align:left`, `min-height:56px`, `border-radius:var(--ks3-r-option)` is
  a full-width **option row** — an answer button. It shares the name `seg` and
  nothing else. Generating it as a segment would produce the wrong component;
  generating the segment from it would produce the wrong control everywhere
  else. It needs its own component in the registry.
- **b1-03's inverted on-state is a third visual treatment**, not a size drift:
  ink ground with light text for "this one is chosen", against everyone else's
  accent tint. That is a legible design choice and it may be deliberate. It
  changes what a chosen segment *means* visually, so it is **Design's call, not
  mine** — flagged, not resolved.

---

## Drift 5 — the KEY FACT box ground

| Page | Line | Background |
|---|---|---|
| b1-01 | 210 | `var(--ks3-band)` |
| b1-02 | 181 | `var(--ks3-band)` |
| b1-03 | 357 | `var(--ks3-band)` |
| b1-04 | 260 | `var(--ks3-band)` |
| b1-05 | 232 | `var(--ks3-band)` |
| b1-06 | 240 | `var(--ks3-card)` |

**Count: `--ks3-band` × 5, `--ks3-card` × 1.**

### ⚖️ Ruled: `var(--ks3-band)`

Five to one, and no reason to prefer the outlier. Neither choice is forced by
accessibility — `--ks3-band` (`#F4E9D8`) and `--ks3-card` (`#FFFCF5`) are both
light grounds and ink text clears 4.5:1 on either — so this is purely which
value the generator emits. b1-06 is the single page out of step.

Worth keeping in mind that `--ks3-band` is also the ground a **chosen-wrong**
ladder option takes (MRB-202). That is not a collision — a KEY FACT box is not
an option button and carries no badge or border in common — but it means the
KEY FACT box must never grow anything that reads as a mark.

---

## Summary

| # | Drift | Count | Ruled | Basis |
|---|---|---|---|---|
| 1 | bench grid column | 232 × 2, 240 × 1 | **232px** | majority; 8px, no semantics |
| 2 | bench grid collapse | 780 × 2, 820 × 1 | **820px** | *against count* — 820 already ruled on b1-06 under MRB-210; one threshold per page; kinder at 800px |
| 3 | statement type | 4 occurrences of the role | **clamp(28px, 3.9vw, 44px)** | modal and median of the four real statements; b1-02 (formula) and b1-05 (instrument readout) are excluded — see the correction |
| 4 | `seg()` light branch | 4 variants | **b1-06's** | only one whose geometry matches its own dark branch; b1-04 and b1-03 are not drift |
| 5 | KEY FACT ground | band × 5, card × 1 | **`--ks3-band`** | 5:1, no accessibility driver |

Three of the five are clean majorities. Drift 2 goes against its count on
recorded evidence. Drift 3's ruling stands but its evidence was corrected on
13 Aug — one of its six rows was an instrument readout misread as a statement,
and the ⚑ that asked for Mide's eye is withdrawn: applying it changes nothing on
b1-05. Drift 4 resolves one value and surfaces two separate components that were
hiding under one helper name.
