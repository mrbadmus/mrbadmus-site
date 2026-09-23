# Figure system — architecture decision (from the serving-path trace)

## What the trace established
- `assignment_questions` stores only `source_ref` (the bank id). Questions are
  RE-FETCHED from the bank on every serve. => a figure attached to a bank row
  flows through to assignments ALREADY SET, with no backfill.
- `bankFor()` (auto composition) selects `figure` and forwards it into the
  `GET /api/class/current-assignment` payload. Live that far.
- `shared/student-live.js` throws it away: `g: null`, unconditionally.
  The template's figure slot is wired to 7 hard-coded Design demo keys.
- `bankForScope()` (Set work) EXCLUDES figure rows at the query
  (`.is('figure', null)`) precisely because the renderer cannot draw one.
- Practice reads `ks3_ladder_questions` — no figure column at all.
- Question text/options render via `createTextNode` only. There is NO
  innerHTML sink attached to question data. A figure needs NEW plumbing.

## LIVE DEFECT found (not in the audit)
All six figure-bearing KS3 bank rows sit at bank_position 1,2,3,4,6,8 — every
one inside the auto window (<12). Set work is sealed; the weekly auto-composer
is not. So `b9-03-e02` ("Use the web. Which animal feeds on only one thing?")
can reach a child today with no web on the page. Fixing the render path
removes the landmine; the Set work exclusion can then be lifted.

## DECISION: `figure` is an ID, never an SVG blob
The column holds a figure id. The drawing is generated at BUILD TIME by Python
drawers into a single manifest that BOTH consumers read by id:
  - site:    `shared/figures.js`  (id -> {svg, alt})
  - backend: `figures.json`, mirrored from this repo

Why not store SVG in the column:
  - it would bloat every bank row and every md5 proof;
  - a drawing fix would require re-loading the bank;
  - alt text would be duplicated per row rather than living with the figure.

Why a mirrored manifest: this repo ALREADY exports `curriculum-tree.json` to
the backend with a `curriculum_tree_mirror` gate (`tools/export_curriculum_tree.py
--check`). Same proven pattern, same gate shape. No new idea needed.

## Consequences
1. Site needs a figure node in the question renderer (new plumbing, an
   innerHTML sink for TRUSTED build-time SVG only — never for question data).
2. Backend needs the manifest for worksheets (PDF vector + DOCX raster).
3. Set work's `.is('figure', null)` exclusion is LIFTED once rendering exists.
4. Both sides must work WITH OR WITHOUT the KS4 `figure` column (the column
   ships separately; the chat applies it to prod).

## Worksheet constraints (from the renderer trace)

**PDF (PDFKit).** Manual layout: `blockHeight()` measures, then
`if (doc.y + h > bottomLimit()) doc.addPage()`, then `drawQuestion()` draws.
A figure must be added to BOTH — measured before it is drawn, or the layout
silently overflows. PDFKit has a native vector API, so a figure goes in as
real vectors, no rasterisation.

⚠️ **A documented gap this feature reopens.** `blockHeight` has no guard for a
block taller than one page. It was safe because the tallest real question is
203pt (28% of a page). A diagram changes that, so this run adds the guard —
it is a consequence of the feature, not unrelated tidying.

**DOCX (`docx` lib).** No vector API; only a raster `ImageRun`. So SVG→PNG is
needed. The brief names `@resvg/resvg-js` or `sharp`; taking
**`@resvg/resvg-js`** — sharp is far heavier native baggage for a job that is
only ever "small SVG in, small PNG out".

⚠️ **Memory is the binding constraint, and it is already tight.** Render
Starter is 512MB. Measured: peak RSS 331MB at 2 concurrent large renders
(~180MB headroom), 485MB at 5. The existing guard
(`MRB_WORKSHEET_LARGE_THRESHOLD=200`, `MRB_WORKSHEET_MAX_CONCURRENT_LARGE=2`)
was sized for pure text+vector drawing, cold.

**Therefore: rasterise once per figure id, per process, and cache** — exactly
the `_markPng` precedent. A 1,450-question worksheet references only a handful
of DISTINCT figures, so the raster cost is bounded by the size of the figure
catalogue (tens), never by question count. That keeps the existing thresholds
honest instead of quietly invalidating them.

**Brand-freeness is test-enforced**, not just conventional: `test_worksheet.js`
greps raw PDF bytes and every non-image DOCX part for `MrBadmus`. Figure SVG
must carry no wordmark, no title naming the site, nothing in metadata.

## Three layers currently seal Set work against figures — all three lift
1. the query filter `.is('figure', null)` (`server.js:3894`, count read too)
2. `rowIsSettable()` (`set-work-scope.js:608`)
3. the worksheet route's per-question object literal, which never copies
   `figure` across (`server.js:6756`)
Lifting fewer than all three leaves the feature invisible.
