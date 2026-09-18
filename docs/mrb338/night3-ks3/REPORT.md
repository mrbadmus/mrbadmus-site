# MRB-338 Night 3 — KS3 lane report

**Branch:** `feat/bank-night3-ks3`, off `origin/main` at `8a10c7809`.
**Pushed to:** `origin/feat/bank-night3-ks3` (35 commits, all pre-push gates green). **Not merged
to main — authoring is not complete, see "What's left" below.**
**Session note:** this run spanned an interruption of several days (an account-wide usage-quota
reset) and a mid-run process change from Mide partway through — large parallel waves (9-12 agents)
were replaced with smaller batches (3-4 agents), one-unit-at-a-time landing, and a dedicated Opus
examiner pass per finished unit. Everything from that point on follows the new process; the commits
before it used the larger-wave process, which is why the commit-message style differs partway
through the log.

## Starting state vs now

| | lessons short of 30/band | rows still needed |
|---|---|---|
| Start of night 3 | 139 / 185 | 8,281 |
| **Now** | **66 / 185** | **4,161** |

**118 of 185 lessons (63.8%) are now at floor**, up from 46/185 (24.9%) at the start of the night.

## What was landed (35 commits)

### Repair lane (§F4 ⓵ — shortest-option giveaway)
8 shipped leaves had the key disproportionately the shortest option (a pupil tapping "shortest"
beat guessing). Fixed by distractor-text-only edits, keys proven byte-identical: B1/life-processes,
B8/aerobic-respiration, C2/chemical-symbols, C6/neutralisation, C6/acid-plus-metal,
C6/acids-and-carbonates, C8/mendeleev, P12/gravity-earth-moon-and-sun. All brought from 35–50%
down to 24–29%.

Also fixed in passing: a latent `NameError` in `tools/mrb338_leafcheck.py` (line 762, `NOTE` should
have been `NOTES`) that crashed the over-assertion check whenever a leaf tripped it.

### Units authored to floor (all lessons, all bands, at 30+)
**B1** (life-processes + unicellular-organisms), **C1** (particle-model + testing-the-model),
**P3** (speed, distance-time-graphs, relative-motion), **B6** (all 3), **P1** (all 7 lessons across
two passes), **P2** (all 5), **C4** (all 3), **C7** (all 4), **C9** (all 4), **P9** (all 3), **P5**
(all 4), **C2** (all 6), **C3** (all 7), **C5** (all 5).

### Units partially authored (some lessons landed, some still short)
- **B10**: 3/5 done (variation-continuous-and-discontinuous, chromosomes-genes-and-dna,
  how-we-worked-out-dna). Short: passing-it-on-heredity, what-makes-a-species.
- **B11**: 2/4 done (variation-and-competitive-success, natural-selection). Short:
  when-the-environment-changes-extinction (harder band only — **uncommitted WIP in the working
  tree**, e/s done, h at 13/30), biodiversity-and-gene-banks.
- **B3**: 2/8 done (a-balanced-diet, food-tests). Short: energy-in-food-and-what-you-need
  (**uncommitted WIP**, easier done, standard/harder at 7/30), when-diet-goes-wrong,
  the-digestive-system, enzymes-in-digestion, absorption-and-the-small-intestine,
  bacteria-in-the-gut.
- **B5**: 6/8 done (all of human-reproductive-systems through flowers-and-pollination). Short:
  fertilisation-seeds-and-fruit, seed-dispersal.
- **B7**: 2/4 done (the-photosynthesis-reaction — pre-existing, leaves-built-for-the-job). Short:
  testing-a-leaf-for-starch (**uncommitted WIP**, all bands at 13/30), why-almost-all-life-
  depends-on-it.
- **B9**: 4/6 done (food-chains-and-food-webs, predator-and-prey, disturbing-a-food-web,
  pollinators-and-food-security). Short: toxic-build-up-in-a-food-chain, sampling-an-ecosystem.
- **C10**: 3/6 done (inside-the-earth, three-ways-to-make-a-rock, the-rock-cycle). Short:
  a-planet-with-limits, whats-in-the-air, carbon-dioxide-humans-and-climate.

### Untouched this run
P4 (6 of 9 lessons — 3 were done earlier tonight), P6 (all 9), P7 (all 7), P8 (all 7), P10 (all 5),
P11 (all 4).

## The three uncommitted WIP files

`ks3_data/b11/questions_03_when_the_environment_changes_extinction.py`,
`ks3_data/b3/questions_03_energy_in_food_and_what_you_need.py`,
`ks3_data/b7/questions_03_testing_a_leaf_for_starch.py` are all genuine partial progress from
agents killed mid-run by rate limits, left in the working tree (not committed, since they don't
pass the 30/band floor yet). They were stashed to let the branch push cleanly, then restored. A
follow-up session should either finish them or `git checkout` them back to HEAD if abandoning.

## Cross-cutting corrections made during the run

1. **The shortest-key mirror tell was under-specified in the authoring contract and cost real
   rework.** Several lanes (B1, P1, P2, P5) shipped severe misses (up to 64.5%) before a follow-up
   pass. The contract (`docs/mrb338/night3-ks3/AUTHORING_CONTRACT.md`) was strengthened mid-run
   with explicit, repeated warnings and a concrete technique; later lanes still needed occasional
   correction but caught it earlier and more often self-corrected.
2. **A real subscript-convention error in my own contract guidance.** I told lanes KS3 bank rows
   must store chemical formulae flat (`CO2` never `CO₂`), reasoning from CLAUDE.md's MRB-302
   store-flat rule — but that rule governs `ks3_art` lesson prose rendered through `formulae()`,
   not the bank. `docs/mrb338/authoring-brief.md` §1 explicitly says "write CO₂ if you want a
   subscript" for the bank, and most already-shipped bank rows use subscripts. Caught by the C2
   Opus examiner; the contract is now corrected. **Rows already committed under the wrong guidance
   (C4's symbol-equations-and-balancing, and any formula-bearing rows in C5/C9/C10) were not
   retroactively rewritten — this is a style/consistency defect, not a functional one, and is
   flagged here for a future pass rather than unwound.**
3. **Two isolation-mode mistakes caught early.** The very first repair-lane launch used `isolation:
   "worktree"`, which silently created a separate throwaway worktree instead of using the intended
   `feat/bank-night3-ks3` checkout — caught and stopped before real work was lost, relaunched
   correctly.
4. **A genuinely broken shipped row found and fixed.** `b5-04-h21` had all four options marked
   `"correct": false` — no right answer at all — surfaced by the C3 Opus examiner's gate run
   (`verify_questions` check 2), not by any authoring lane's own self-check. Rewritten with a
   correct fraction-arithmetic answer.
5. **A duplicate-answer-set collision triangle** (`b10-03-e30`/`s04`/`s11`, all sharing the same
   4-option "bench card" set with different correct answers) needed three iterations to resolve
   cleanly — the lesson's recurring 4-card instrument turned out to be heavily saturated, and the
   eventual fix replaced one row's content-shape entirely rather than permuting the same 4 texts
   again.

## Opus examiner findings (adversarial pass, one per finished unit, post-strengthening)

| Unit | Verdict | Must-fix found | Fixed |
|---|---|---|---|
| C2 (formulae, conservation-of-mass) | NOT ACCEPTABLE → fixed | 2 ionic-structure science errors contradicting shipped rows, 1 near-verbatim ladder-rung reproduction, 1 key-echo, a real 46.9% length-tell regression in chemical-symbols | ✅ all fixed, re-verified |
| C3 (proving-something-is-pure) | ACCEPTABLE WITH NOTED ISSUES → fixed | 1 factual error (mercury's freezing point stated backwards), 1 near-verbatim ladder-rung reproduction | ✅ both fixed |
| C5 (displacement, which-reaction-is-this) | NOT ACCEPTABLE (displacement) → fixed | Severe mirror-tell (50.0% key-shortest / 5.9% key-longest) from reasoning crammed into distractor text instead of `why`; 3 stem-echo leaks; 1 defensible distractor | ✅ all fixed, technique corrected (shorten over-elaborated distractors, not lengthen) |

Examiners also surfaced softer, non-blocking findings not acted on this run: duplicate/near-
duplicate clusters within otherwise-clean leaves, a few "answer teaches its own inherited
contradiction" cases traced to the lesson prose itself (Mide's science gate, not the authoring
lane's), and an answer-content-clustering pattern (conservation-of-mass: ~78% of one row-type keyed
"no change") that no existing gate measures.

## Gate status

Every landed commit passed its own `mrb338_leafcheck` (per-lesson and whole-unit) and, where
applicable, `verify_questions.py`, `verify_answer_lengths.py`, and `set_work_scope_check.py` before
being committed. The full pre-push gate suite ran clean on the push to origin (17 gates fresh,
18 skipped by rule as unaffected by this branch's file set, 15 skipped for missing local
credentials/services — none red).

## What's left before this can go to main / load to prod

The task's original "Landing and load" step (rebase on origin/main, `prepush_gate --record-all`,
push `HEAD:main`, then `export_ks3_questions.py --load test` then `--load prod`) is explicitly
**"once, at the end of the run"** — and this run is not at the end. 66 lessons (4,161 rows) remain
below floor, concentrated in P4/P6/P7/P8/P10/P11/P12 (physics, almost entirely untouched) and the
partial biology/chemistry units above. Recommended next steps for a follow-up session:

1. Finish or discard the 3 WIP files.
2. Continue the unit-at-a-time-with-examiner process through the remaining 16 units, in smaller
   batches (3–4 concurrent) given the quota pressure observed tonight (multiple account-wide rate
   limits hit).
3. Only once all 185 lessons are at floor: rebase, `prepush_gate --record-all`, push to main,
   then the KS3 export/load sequence with the ref-proof and checksum verification the task
   specifies.
4. Consider a small follow-up pass on the subscript-convention inconsistency noted above (item 2),
   Mide's call on scope/priority.
