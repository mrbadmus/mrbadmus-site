# C1 rebuild — build brief (MRB-228)

Repo root: `/Users/midebadmus/Documents/GitHub/mrbadmus-site`
Scratch:   `/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-site/9562ab7b-637a-4aca-a758-38c6d14f4b1b/scratchpad`

You are building ONE C1 lesson. The commander integrates. **Do not edit
`build_ks3.py`, `shared/ks3.css`, `shared/ks3.js`, `ks3_parity.py` or
`verify_ks3.py` — you have no write access to them in this run and an edit
there will be discarded.** You write your lesson module, and you write your
instruments as FRAGMENT files that the commander splices in.

---

## 1. Your sources, in priority order

1. **The frozen approved page** — `docs/ks3/design-reference/c1/<your file>.dc.html`.
   This is the authority. Read it in full. Every number, every string, every
   control, every branch of every note is in there.
2. **The payload map** — `docs/ks3/c1-inventory/PAYLOAD-MAP.md`, YOUR section
   (§1 = c1-01, §2 = c1-02, §3 = c1-03, §4 = c1-04, §5 = c1-05, §6 = c1-06).
   It gives you line ranges, the block sequence, the rail table, and a
   `payload` block per instrument. **Adopt the payload shapes it names.**
3. **The extracted constants** — `scratchpad/payloads/c1/<your file>.json`.
   These are the module-scope `const`s, lifted byte-identical by
   `node tools/extract_design_payload.js`. USE THESE, do not retype them.

⚠️ Some payload lives INSIDE `renderVals`, not at module scope, so it is NOT in
the JSON: c1-03's `PHASE` (lines 633–644), c1-04's wrong-answer fallback note
(line 738), c1-06's `VERDICTS` (lines 490–499). Lift those by hand from the
frozen page, byte-identical.

**Every student-facing string is lifted, never retyped.** A typo in retyped
prose is invisible and crosses the examiner gate. Static prose (headings,
ledes, reveals, key fact, keynote, going further, endmatter) is in the frozen
page's markup — the payload map's §x.2 gives you the line numbers.

---

## 2. The exemplar to copy

`ks3_data/c2/lesson_04_chemical_symbols.py` is the shape. Read it before you
start. Your module exports one `LESSON` dict. The canonical field list is
`docs/ks3/architecture.md` §4.8 with amendments §4.8.1 and §4.8.2.

Write to: `ks3_data/c1/lesson_NN_<slug_with_underscores>.py`

`ks3_data/c1/__init__.py` already exists (the commander created it) and
discovers `lesson_*.py` in sorted order. You do not touch it.

---

## 3. Rulings that bind you (settled — apply, do not re-litigate)

- **R1** — `#s-think` on every C1 page asks for a commitment, so it is authored
  as a **`predict`** activity and it DOES tick its rail stage. This is not B1's
  static `confrontation`.
- **R3** — the shipped stylesheet wins over per-page KEY FACT drift. Author
  `key_facts` with `ground: "card"`; do NOT chase the page's 6px/25px/22-26px
  numbers. One stylesheet serves 183 lesson slots.
- **R5** — **no key is authored without a read site, in the same pass.** If you
  author a payload key, your renderer fragment must read it. "It documents
  intent" is not a read site — use a comment.
- **MRB-208** — rail is completion-based, nothing ticked on load, on BOTH the
  ≥1340px and narrow variants. KEY FACT is never amber.
- **MRB-196 R10** — no per-option feedback except where the map says so.
- **MRB-225** — evidence quality, method criticism and history of science live
  in GOING FURTHER. Nothing in a lesson body may be retracted by a later
  sentence in the same lesson.
- Ladder marks correctness only: green tint + drawn ✓, dark ✕. Never the accent.
  Amber is a wrong IDEA, never the student.
- Year and half-term never appear in a lesson URL or a lesson page's bytes.
  "A student your age", never "a Year 7".
- Every lesson carries `"review_state": "draft"`.
- No platform self-explanation on a student page.

### Two corrections you APPLY, because they are already ruled

- **c1-03 only — the plateau ratio.** Design's `KEYS` draws boiling:melting at
  2.29:1; the page's own prose says about seven times, and the prose is right
  (L_v 2260 kJ/kg vs L_f 334 kJ/kg ≈ 6.8:1). NOTES flag 4 claims the drawing is
  correct; it is not. **Correct the drawing to the prose.** Keep the melting
  plateau where it is and extend the boiling plateau so the drawn ratio is
  ≈6.8:1, rescaling the x-axis so the curve still ends at 100. State in a
  comment what you changed and what the new ratio measures.
- **c1-04 only — the canvas aria-label.** The readouts are drawn INSIDE the
  canvas, so they reach a screen reader only through `aria-label`, and Design's
  label reports temperature, container and particle count but NOT the wall-hit
  number — the one number the lesson is about. **Add the count to the label.**
  That is an addition inside a component Design drew, which is permitted.

---

## 4. What you may and may not do

- You MAY add behaviour, physics, detail or refinement INSIDE a component
  Design has drawn, where the page is silent. Keep it, and say so in your
  report.
- You may NOT invent a component, block type, layout or page structure Design
  has not drawn.
- An addition may not contradict the page. **The page wins over the engine.**
- Where Design is wrong and you are sure, correct it and report it.

---

## 5. Your instrument fragments

For EACH new activity kind you own, write four files into
`scratchpad/c1/frag/`:

| File | Contents |
|---|---|
| `<kind>.renderer.py` | the `r_<name>(a, act_id)` function, complete, plus a one-line `DISPATCH:` comment at the top giving the exact `ACTIVITY_KIND_RENDERERS` entry |
| `<kind>.css` | the complete CSS block for the instrument |
| `<kind>.js` | the complete `wire<Name>(sec)` function, plus a one-line `WIRE:` comment giving the dispatch selector |
| `<kind>.parity.py` | 2–4 `dict(...)` COMPONENTS entries measuring the instrument's real, resolved styling |

### Renderer house style — copy `r_claim_switch` in `build_ks3.py` (~line 3207)

- Validate payload keys up front and `raise ValueError` naming the kind and id.
- Helpers available: `e()` escape, `t()` text, `rich()` inline-HTML,
  `r_bench_gate(gate)` → `(html, hide)` for the 4-option commit gate,
  `_head_counter(...)` for the "N of M" section-head counter,
  `r_activity_options(...)` for a standard option list.
- Emit `data-*` attributes for JS to read; never assemble science-bearing text
  from an attribute — use **emit-both-show-one** with `hidden` so `<em>`
  survives and no string is rebuilt in JS.
- Emit `data-stage-done="0"` on the instrument root if it is a rail stop.
- `role="status"` on the live note paragraph, never on the instrument root.
- Return ONE concatenated string.

### CSS conventions

- Root class `.ks3-<short>`; children `.ks3-<short>-<part>`.
- ⚠️ **`.ks3-dark p` is (0,1,1) and beats a bare instrument class at (0,1,0).**
  Every instrument that can sit on a dark ground MUST scope its text rules
  strongly enough to win. This has bitten two separate builds. If your block is
  `practical` (ink-dark), test it.
- Do not restyle anything outside your own class tree.

### JS conventions

- One `wire<Name>(sec)` per kind, found by a `[data-<x>block]` selector.
- Read configuration from `data-*` attributes, never from an inline script.
- Respect `prefers-reduced-motion` **inside the tick**, not only at
  construction — R4 corrected exactly that slip on b2-03. For a counting
  instrument, scale the rate rather than stopping, so the count still runs.
- Canvas: design space is `900 × H`, backing store `1800 × 2H`,
  `setTransform(2,0,0,2,0,0)`. `role="img"` + a state-bound `aria-label`.

---

## 6. Rail and `done_when`

Author `rail` with the five stages from the payload map's §x.4 table, with
`anchor`, `short` (≤6 chars), `label`, and `done_when`.

`done_when` is a GATE field, not a runtime field (R2) — the runtime ticks from
`data-stage-done`. Author it as the real predicate the map names. **Every rail
anchor must name a section your lesson actually emits.**

Three rail defects the map found in Design's own pages — fix them, they are
engine defects not science:
- **c1-02 stage 3** and **c1-05 stage 4** tick on the PREVIOUS stage's state,
  for a section that demands nothing. Under MRB-208 a rail stop must require
  the student to do something. Give the section its own demand if the page has
  one, otherwise take it off the rail. Say which you did and why.
- **c1-04 stage 2** uses `Math.max(touched, N)`, so pressing only the
  particle-count button reads "all controls tried". The predicate wants a SET.
- **c1-06 stage 4** ticks on `history !== 1` and UNTICKS when the student
  returns to the default. Wants "has visited more than the default" — a set.
- **c1-02 `benchProgress`** counts the current state as seen before it is
  chosen, so a fresh page reads "1 of 3 states seen". Start at zero.
- **c1-03** `state.thinkSeen` is initialised and never read or written. Dead
  state — do not carry it into the module.

---

## 7. When you are done, report

1. The lesson module path and its line count.
2. Each fragment file you wrote.
3. **Every string you could not lift byte-identical and had to retype**, with
   why.
4. **Every addition you made inside a drawn component.**
5. **Every Design decision you corrected**, and why you were sure.
6. Any authored key you could not find a read site for.
7. Anything in the frozen page you could not express.
