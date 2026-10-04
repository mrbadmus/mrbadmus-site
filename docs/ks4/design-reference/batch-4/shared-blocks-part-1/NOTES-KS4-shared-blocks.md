# KS4 shared blocks — Part 1 of the batch-4 brief

2 Oct 2026 rules (Mide), drawn once so every lesson mounts them and Code ports each block once.
Same runtime, tokens, dark remap (`ks4-theme.css`) and visual language as the pilot. `Ks4Chain` and `Ks4Write` are the pilot's own files, copied unmodified; `ks4-lib.js` likewise (only `load`/`save` are used here).

Status: **Part 2 delivered 4 Oct 2026** in `Design's Output/KS4 Batch 4/` (13 lessons, written from the batch-4 pack on main).

## Demo pages

Each demo opens as a canvas with four live frames: Light · 1280, Dark · 1280, Light · 390, Dark · 390. Each frame is the same file loaded with `?frame=light` or `?frame=dark`, so media queries really run at 390. Open a frame URL on its own to review one state full-screen.

| Page | Rule | Shows |
|---|---|---|
| Demo 1 - Formula triangle | 2 | Equation block for E = m c Δθ, P = E ÷ t, V = I R, Ek = ½ m v²; then the equation-sheet panel with all four, compact |
| Demo 2 - Start here guess | 1 | A Foundation opener (two spoons in soup) and a Triple Higher opener (braking at twice the speed) |
| Demo 3 - Chained worked example | 3 | Kettle: E = m c Δθ, then P = E ÷ t. Worked, then the pupil's attempt in the same shape |
| Demo 4 - Practice shape | 4 | The exam ladder at 2 · 2 · 2 · 1, with seven demo questions |

## 1 · Ks4Triangle — formula triangle (rule 2)

**How it works.** The quantity on top, the others side by side underneath. The pupil taps the quantity they want. The letters sit bare inside their regions, with no boxes, so nothing crosses a dividing line; an underline marks them as tappable. The tapped region fills with ink and its letter turns ground-coloured (a fill inversion); the regions left over tint with the accent. Next to the triangle, the rearranged form appears as a line:

- tap the top: side by side, multiply (E = m × c × Δθ);
- tap a bottom cell: the top over the rest, divide (m = E ÷ (c × Δθ)). Brackets go round the divisor whenever it has more than one quantity.

**½ and squares.** The ½ sits in the triangle as a fixed cell; it cannot be tapped. When it ends up in the divisor, the block adds its own line: "Extra step · ÷ ½ is the same as × 2". A squared cell (v², e²) carries `root: 'v'`; tapping it adds "Extra step · square-root both sides". The extra lines have a dashed border so they look different from the triangle line. Ek = ½ m v², tap v²:

1. One over the other · divide: v² = Ek ÷ (½ × m)
2. Extra step · ÷ ½ is the same as × 2: v² = 2 × Ek ÷ m
3. Extra step · square-root both sides: v = √(2 × Ek ÷ m)

Ee = ½ k e² works the same way with no new code: `bottom: [{s:'½',half:true},{s:'k',…},{s:'e²',root:'e',…}]`.

**Props.** `eq` = `{ name, written, source?: 'sheet'|'none', route?, top:{s,name,unit}, bottom:[{s,name,unit,half?,root?}] }`, with 2 or 3 bottom cells. `variant` = `full` (equation block: eyebrow, "On the sheet" chip, route chip, triangle, rule caption, legend) or `compact` (the equation-sheet panel and CFIFA's Formula step). `pick` preselects a quantity by symbol (`'t'`, or `'v'` for a squared cell). `onPick(symbol)`.

**Where it mounts.**
- Equation block: `variant="full"` inside the lesson's `equation` section. This replaces the pilot's static "V = I R / R = V ÷ I" card.
- Equation-sheet panel: a grid of `variant="compact"` triangles, one per equation in the lesson, beside the existing "View the full equation sheet" link.
- CFIFA Formula step: `Ks4Steps` mounts it automatically under any line labelled `Formula` when its step has `eq`, with `pick` = the step's `find`. The pilot's `Ks4Cfifa` can do the same on port: add `eq`/`find` to an example and render the triangle under its Formula line. That's the only change it needs.

**Port notes.** The triangle is one SVG (outline, divider lines, region fills) under absolutely placed buttons. Geometry is fixed in `G` (2 or 3 bottom cells). Hit targets are at least 44 px compact and 54 px full. The √ is drawn (an SVG radical plus a top rule), not typed: the house fonts' latin subsets have no U+221A. A screen-reader copy of the root line is in the DOM.

## 2 · Ks4Guess — "Start here" (rule 1)

Replaces `Ks4Choice` in the hook. It always has exactly two options (any more are ignored). The guess line always starts "If you had to guess, …" and ends with the lesson's own explicit question (`question` prop), e.g. "which handle is hotter?" Ask exactly what the two options answer; never a bare "which do you think?". The cards are tagged "This" and "Or this". The chosen card becomes "Your guess" (ink border, offset accent shadow), and the answer gets an ink "The answer" pill with a drawn tick. The reveal panel is always the accent (friendly) treatment, never the alert one, whichever option was picked. It shows `rightWord` ("Good guess.") or `wrongWord` ("Fair guess."), then the option's own reply, then the shared `bridge`, which leads into the first explainer.

Props: `title`, `scene` (one short paragraph, optional), `question`, `options` [2 × {text, correct, reply}], `bridge`, `rightWord`, `wrongWord`, `figureSvg`, `onCommit(i, correct)`.

**Authoring test for every opener.** (a) Can a Combined Foundation pupil make a sensible guess from everyday life, with nothing untaught? (b) Would a Triple Higher pupil find it worth a second's thought? (c) Does each reply stay friendly and point at the teaching? (d) Is the answer not given away by the title or the scene?

## 3 · Ks4Steps — "Step 1 … Step 2 …" (rule 3)

`mode="worked"`: both step headers show from the start, so the plan is visible. Lines are revealed one at a time across both steps, CFIFA on each step, and each step's Formula line has its triangle. When Step 1 finishes, a dashed "Into Step 2: E = 168 000 J" strip appears, and Step 2's Insert line points back to it.
`mode="attempt"`: the same two cards with an input on each line. "Check your working" opens once all ten lines are written. It shows each model line under the pupil's own, with "I had this" ticks, as `Ks4Cfifa` does.

Props: `mode`, `id`, `head`, `lead`, `steps` [{title, find, eq, carry, lines:[{letter,label,line,note?,placeholder?}]}], `next`, `close`, `onDone()`.

**Rule 3 in the lesson order:** any rung-2 or practice question that chains two equations must come after a `Ks4Steps` worked example of that chain, and must have a `Ks4Steps` attempt before the ladder. One-step equations keep the pilot's `Ks4Cfifa` (two worked examples, two attempts).

## 4 · Ks4Practice — the fixed practice shape (rule 4)

**The number: 2 · 2 · 2 · 1. Seven ladder questions in every lesson, on every route.**

- Rungs 1–3 take two questions each. One right answer can be a lucky guess; two shows the pupil can do it. A rung scores only when both its questions score, so the ladder is still scored out of 4 (KS3 ruling, 9 Aug).
- Rung 4 takes one 4- or 6-mark answer. Writing and self-marking a 6-marker takes 8–10 minutes, so two would push the lesson past 45 minutes.
- Seven is above the content-standards floor of five.
- **The practice set after the ladder (`Ks4QuizBank`) is fixed at five verbatim quiz questions per route**, with "Show more" removed. If a pack has more than five for a route, pick the five that cover the most named misconceptions. If it has fewer, that's a science flag for Code, not a shorter set.

The block enforces the shape: if a lesson passes a different number of questions for a rung, that rung shows a "Shape:" alert, so the defect shows on the page. Question kinds are `mcq`, `calc` (CFIFA convert choice + number + unit, with the five-line model), `chain` (mounts `Ks4Chain`) and `write` (mounts `Ks4Write`). "Retry my misses" resets only the questions that didn't score. The best score is stored as `ks4-best-<slug>`, as in the pilot.

Props: `slug`, `rungs` = `{ r1:[q,q], r2:[q,q], r3:[q,q], r4:[q] }`, `onDone(score)`.

## Science flags (demo content only — not pack science)

These demos are on everyday topics. No demo string goes into a lesson. Batch-4 lessons take their science from `docs/ks4/packs/batch-4/04-checked-science-source/`.

1. **Equation status (corrected 4 Oct).** From the 2027 exams every GCSE Physics and Combined Science paper carries the full equation sheet, so every physics equation is "On the sheet"; nothing renders "Learn this one". `source: 'none'` (no chip) exists only for biology equations, which are on no sheet.
2. **Units.** c in J/kg °C, Δθ in °C, as AQA writes them.
3. **Demo 2, Foundation opener.** Metal is a better thermal conductor than wood (AQA energy, efficiency and thermal conductivity; Code to confirm the route tag against the pack). The opener is a demo of the format, not batch 4's thermal-conductivity hook.
4. **Demo 2, Triple Higher opener.** At twice the speed with the same braking force, braking distance is about four times as far, because work done by the brakes = Ek = ½ m v² (AQA 6.5.2.1 / 6.1.1.2). Thinking distance is excluded on purpose in the scene.
5. **Demo 3.** 0.50 × 4200 × 80 = 168 000 J; 168 000 ÷ 2000 = 84 s. Attempt: 1.5 × 4200 × 80 = 504 000 J; 504 000 ÷ 3000 = 168 s. Both assume no energy is lost to the surroundings, as the question says.
6. **Demo 4.** 2.0 × 900 × 15 = 27 000 J; 1200 × 120 = 144 000 J. The rung-4 method follows AQA required practical 1 (specific heat capacity). E = V I t is offered as the alternative to a joulemeter.
7. **Greek letters.** Δ, θ and Ω are not in the house fonts' latin subsets, so they render in the system fallback. This matches the pilot (Ω). Code may want a Greek subset of Bricolage / DM Mono.

## Hand-off for Part 2

Each batch-4 lesson will mount `Ks4Guess` (hook), `Ks4Triangle` (equation block + sheet panel), `Ks4Steps` (wherever two equations chain) and `Ks4Practice` (ladder), plus the pilot blocks it already uses (`Ks4Chrome`, `Ks4Cfifa`, `Ks4Sort`, `Ks4KeyNote`, `Ks4QuizBank` at five, `Ks4End`, `Ks4Video`).
