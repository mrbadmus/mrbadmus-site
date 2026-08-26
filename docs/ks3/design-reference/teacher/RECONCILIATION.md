# Vendoring record — Teacher dashboard redesign (MRB-287, Phase 0)

Vendored 24 Aug 2026 from the untracked delivery folder at the repo root,
named `Teacher dashboard redesign ` — **with a trailing space**, which is why
every command that touches it here quotes the path.

## Layout

Mirrors `../student/` and `../class-view-amendments/`, so the compiler's
`ref` + `src` convention needs no special case:

    teacher/
      README.md          Design's own, verbatim
      github.md          Design's own, verbatim — repo/branch/path + screen map
      RECONCILIATION.md  this file
      .thumbnail         Design's own
      source/
        Teacher Dashboard.dc.html   the delivery proper
        support.js                  Design's component runtime (NOT shipped)
        _ds/mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1/
      uploads/           the five screenshots of the CURRENT teacher UI that
                         Design worked from

## Reconciliations made

The delivery re-ships the bound design system, and two copies of that same
system (same UUID, `53dad5ae-…`) were already vendored — under `../student/`
and under `../class-view-amendments/`. All three were compared file by file
by MD5.

**16 of the 17 files are byte-identical across all three copies.** One is not.

### 1. `tokens/shared-tokens.css` — font URLs. VENDORED COPY WINS.

Design's fresh export carries seven absolute font URLs:

    src: url('/shared/fonts/fraunces-var-latin.woff2') format('woff2');

The copy already vendored under `../student/` carries the relative form:

    src: url('../fonts/fraunces-var-latin.woff2') format('woff2');

Same seven `@font-face` blocks, same 529 lines, no other difference.

**Resolved to the relative form**, i.e. the vendored copy, on two independent
grounds that agree:

- **The Phase 0 rule** — on any difference the vendored copy wins, because it
  may carry fixes a fresh export does not. It does here.
- **It is the only form that works.** A design reference is served with its
  own directory as the web root (`cdp.serve(ref)` in `student_template.py`).
  From that root, `../fonts/` resolves to `source/_ds/…/fonts/` — correct —
  while `/shared/fonts/` resolves to `docs/ks3/design-reference/teacher/shared/
  fonts/`, which does not exist. All seven faces would 404.

  That failure is worth naming precisely, because it is invisible in a diff
  and loud in a measurement: missing webfonts fall back to a system face with
  different metrics, so every text box changes width and height. Any parity,
  overflow or screenshot gate driven against this reference would then be
  measuring the fallback font, not Design's.

`/shared/fonts/` is not wrong in itself — it is the SERVED path, and it is
what the built pages must link (`build_student_port.SERVED_FONTS`). It is
wrong *here*, in an offline reference. The fresh export appears to have picked
it up from the repo's own deployed `shared/tokens.css`, which correctly uses
it.

Note the third copy, `../class-view-amendments/`, carries the absolute form
too and is therefore also affected. **Not changed under this ticket** — it is
another lane's vendored reference and nothing in MRB-287 reads it. Recorded
here so it is not mistaken for a difference this port introduced.

After the reconciliation, `teacher/source/_ds/…` is byte-identical to
`student/source/_ds/…` — verified with `diff -r`.

### 2. No `standalone/` in this delivery, and none needed.

`../student/` and `../class-view-amendments/` both ship a `standalone/`
bundle, which `student_template.capture_imports` reads to recover the rendered
markup of each `<x-import>`. This delivery ships none.

It needs none. The delivery carries exactly one `x-import` —
`MrBadmusDS.BrandMark` — and that mark is **stripped**, because `/teacher/*`
is a staff surface and the staff brand is the plain text wordmark with no logo
asset (CLAUDE.md, four brand presentations). See `strip_brand_mark` in
`student_template.py`, which refuses the build if the delivery ever carries a
second import — at which point a standalone would genuinely be required.

## Not vendored

Nothing was dropped. The delivery's five `uploads/*.png` are screenshots of
the *existing* teacher UI that Design worked from, not assets the redesign
uses; they are kept because they are the before-picture this port is measured
against.

---

# Re-vendoring record — Design's v2 (MRB-287, 26 Aug 2026)

Mide dropped a corrected delivery at the repo root as `teacher dashboard
redesign` — lowercase t, **no** trailing space, so it sat beside the old
folder rather than merging into it. Its contents are the 24 Aug delivery
re-shipped **byte-identical** (README, github.md, support.js, `_ds`, uploads —
all MD5-equal) **plus one new file: `Teacher Dashboard v2.dc.html`**. That
file is the corrected design and now replaces `source/Teacher Dashboard.dc.html`
here, under the same filename so the compiler's `src` needs no change.

⚠️ THIS REVERSES THE PHASE-0 RULE, ON MIDE'S INSTRUCTION. "Vendored copy
wins" exists because the vendored copy may carry fixes; this time the fresh
drop IS the fixes — Mide's corrections with Design are the point of the run.
The rule reversal covers the `.dc.html` only: `_ds` was not re-vendored
(the drop's copy is identical to the unreconciled v1 export, so re-vendoring
it would have UNDONE reconciliation #1's relative font URLs).

## What v2 changed vs v1 (and what the port did about it)

Presentation, wholesale: body 16.5→18px, container 1340→1460px, padding
32→40px, headings +4px, cards `minmax(310px,1fr)`, and equivalent bumps on
every screen. All flow through the compiled template untouched.

Structure and logic, specifically:

- **Nav**: the `Teacher` crumb label and the permanent `PROD` chip are gone.
  The crumb follows v2. The env chip is reinstated as a CONDITIONAL insertion
  (`teacher_rulings.INSERT_AT` node 10) because its job was never "say PROD
  on prod" — `envBadge()` now returns "" on the live production origin, so
  prod renders exactly v2's drawing and TEST/LOCAL still warn.
- **Class cards**: the subject badge (dots + name) is gone, and the card meta
  is now `c.n ? c.n + ' students' : 'No students yet'` — v1's
  `Year N · KS · <year>` line is gone with it. Mide's E1 ruling (every card
  states ITS OWN academic year) survives the redraw: the year name is
  appended to v2's count. Year group and key stage were v1's drawing and
  follow it out.
- **Class header**: `longMeta` likewise lost its `Year N · KS · <year>`
  prefix; the ruled year name now leads v2's counts. The read-only chip's
  insertion point moved to v2's header identity block (template node 91).
- **Marking screen**: "Lowest scoring — worth reteaching" → "Reteach"; a
  Correct / Incorrect / Not attempted legend is new (the ruled fourth key,
  "Self-marked or written", inserts after it); the score column is fixed
  100px.
- **Node indices**: v2 renumbers essentially the whole tree. Every index in
  `teacher_rulings` (~75 across SCREENS / OVERLAYS / INSERT_AT / DEAD /
  BINDINGS_AT / BIND_ATTR / RETEXT_AT / SET_ATTR / SET_ON / WRAP / NAV /
  AMENDED_ADDITIONS / IMPORT_NOT_PORTED) was remapped by structural diff of
  the two compiled trees and each landing verified same-tag same-handler.

No new sample data: v2's fixture values are v1's, so `teacher_tells` needed
no new tells.
