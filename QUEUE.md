# QUEUE — lane: content/bonding-p2b

**Worktree:** `~/Documents/GitHub/mrbadmus-worktrees/bonding-p2b`
**Branch:** `content/bonding-p2b` (cut from `main` @ `14d9d405d`, 25 Jul 2026)
**Purpose:** Phase 2B — build the exam engines for the bonding pages and wire the already-approved
authored content onto them. The content is done and signed off; this lane is engineering.

---

## Standing rules for this lane

1. **Work only inside this worktree.** Never edit, stage, or read-modify files in
   `~/Documents/GitHub/mrbadmus-site` or in any other worktree under
   `~/Documents/GitHub/mrbadmus-worktrees/` — note especially that `content/bonding` is a separate
   worktree; leave it alone.
2. **One session per worktree.** If another Code session is already open here, do not start a second.
3. **Commit freely.** You do not need permission to commit.
4. **NEVER push.** Mide pushes via GitHub Desktop, always.
5. **Follow the AUTONOMY CONTRACT** at the top of `CLAUDE.md` — act, don't ask.
6. **The authored content is approved — do not rewrite it.** Fixing an engine is your call. Changing
   a mark scheme, a chain, or a distractor is Mide's (science/content accuracy is his sole gate).
   If an item genuinely cannot be expressed by the engine, adapt the *engine*, and flag the item.
7. **Run the generator before you commit** — `python3 generate_site_v5.py`. Verified clean on this
   branch: zero diff from a fresh run, so any diff afterwards is yours.
8. **Deviations go in the final report, one line each** — not mid-run.

---

## Read these first

1. `~/Documents/mrb-authoring/phase2-exam/engine_content_spec.md` — **read before anything else.**
   Defines the three engines and holds the authored items. The five page HTML/RTF files alongside it
   are the authored content per page.
2. `docs/redesign/architecture_v2.md` — **Law 6** is the governing law for this work:
   > Every page ends in the four-rung ladder: ① recall check → ② apply (deduce/calculate) →
   > ③ explain (chain assembly) → ④ extended response (write-then-self-mark), tariff-tagged, with
   > per-question persistence and "retry my misses". Recognition (MCQ) feeds the ladder; production
   > tops it — because AQA pays for production. The misconception-tagged distractor bank is
   > preserved and mined, never gamified away.
3. `shared/quiz.js` — the existing quiz engine. Match its conventions; extend the design language
   (architecture_v2 Law 7) rather than inventing a second one.

---

## Task 1 — build the three engines and wire the five pages

### The engines (vanilla shared modules — no framework, no build step)

- **ChainBuilder** — student orders scrambled causal links; red herrings included.
- **WriteThenMark** — student writes free text, then reveals the mark scheme and self-awards.
  **BeTheExaminer is a thin layer over this**, not a fourth engine: same core, different framing
  (student marks a supplied answer rather than their own).
- **FormulaDeducer** — student balances ion charges to build a formula.

Ship them as shared modules in the style of `shared/quiz.js`, loaded per page. No npm, no bundler —
this site runs as plain files in the browser.

### Wire onto these five pages

`properties-ionic-compounds`, `giant-covalent-structures`, `metals-alloys`,
`properties-small-molecules`, `ionic-bonding`

Then **assemble the exam ladder per Law 6** on each: recall → apply → explain → extended response,
tariff-tagged, per-question persistence, and a working "retry my misses".

---

## Constraints that actually matter

### The 8 frozen content fields are off limits

The authored items are **net-new**. They must **not** be pushed into the eight frozen content fields:

`quiz`, `matching`, `common_mistake`, `key_note`, `theory`, `fifas`, `higher`, `triple_only`

Put the authored content in a **separate authored-content module** and join it to the pages by slug.

### The four chemistry data files must stay byte-identical

Baseline SHA-256, recorded 25 Jul 2026 at branch creation:

```
b44669d443c18683  all_subtopics_chemistry.py
4d13b977a2fa9956  all_subtopics_chemistry_higher.py
a3614f4e278812b1  all_subtopics_chemistry_triple_foundation.py
edf241e7d45f1096  all_subtopics_chemistry_triple_higher.py
```

Check before every commit:

```bash
shasum -a 256 all_subtopics_chemistry*.py | cut -c1-16
git status --porcelain -- 'all_subtopics_chemistry*.py'   # expect: no output
```

Any diff on those four files means the design has gone wrong — the content has leaked into the
frozen layer. Back it out and re-route through the authored-content module.

### Misconception slugs are verbatim, always

Every slug (`electrons-carry-ionic-current`, `melting-creates-ions`, `charges-swapped-to-subscripts`,
`missing-brackets`, …) is the **join key to the MRB-135 MCQ banks**. Do not rename, normalise,
re-case, pluralise, or "tidy" a single one. A silently-renamed slug breaks the clustering with no
error anywhere — it just quietly stops matching. Copy them across mechanically and diff the set
against the spec when you are done.

### Mide's rulings — already decided, do not re-open

- **Ship the constructed composite 6-markers.** Yes, they are constructed rather than lifted from a
  past paper. That is the call.
- **Ship the polyatomic FormulaDeducer set as a Higher-weighted optional group** — not core, not cut.
- **Never auto-grade free text.** Self-marking against the scheme *is* the pedagogy. Do not add
  fuzzy matching, keyword scoring, or an LLM grader to WriteThenMark, however tempting. The student
  reading the mark scheme against their own words is the learning event.

### One discrepancy to reconcile

The lane brief describes **83** authored items. `engine_content_spec.md` totals **78**
(WriteThenMark 26 + BeTheExaminer 10 + ChainBuilder 15 + FormulaDeducer 27), with the 6-item
polyatomic set marked `[CHECK]`. Count the items in the five authored files yourself and treat the
**authored files as the authority**. Report the number you actually wired, and note the gap.

---

## Verification before you commit

- All five pages open in a browser with **zero console errors**.
- Each engine works: ChainBuilder accepts a correct order and rejects red herrings; WriteThenMark
  reveals the scheme and records a self-award; BeTheExaminer marks a supplied answer; FormulaDeducer
  builds correct formulae and catches the charge-swap misconception.
- Persistence survives a page reload; "retry my misses" returns only the missed items.
- The four frozen data files are byte-identical (hashes above).
- Every authored misconception slug appears verbatim in the shipped output.

## When you are done

Write a short report: engines built, pages wired, item count actually shipped vs 78 vs 83, the
frozen-file hash check result, browser verification, and any one-line deviations. Leave the work
committed on `content/bonding-p2b`. **Do not push.**
