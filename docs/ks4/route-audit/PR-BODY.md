## Summary

Mide's ruling (2 Oct 2026): every KS4 subtopic the site flagged Triple-only that AQA Combined (8464) teaches gets its route corrected, with the 8464 spec point cited; the same rule in reverse for base content the spec marks HT or separate-science only.

The spec audit is committed with this PR: `docs/ks4/route-audit/{biology,chemistry,physics}.md`. Eight subtopics move. Chemistry has no moves.

Mechanics: a subtopic's routes are which of the twelve `all_subtopics_<subject>[_higher|_triple_foundation|_triple_higher].py` files contain it. Each moved subtopic's dict was copied verbatim (source text, not re-serialised) into the extra route files, in the same position as in the triple file. Foundation files got the TF copy and Higher files got the TH copy. `dark-matter-dark-energy` exists only as a TH copy, so that is what TF got. `ks4_data.classify()` re-derives `tier`/`triple_only` from these files, and its nesting assertion (CF⊆CH⊆TH, CF⊆TF⊆TH) still holds.

## Route table

| subtopic | before | after | citation |
|---|---|---|---|
| `meiosis` | TF TH | **CF CH TF TH** | 8464 4.6.1.2 *Meiosis* (no HT marker); 8461 4.6.1.2 is unmarked |
| `classification-living-organisms` | TF TH | **CF CH TF TH** | 8464 4.6.4 *Classification of living organisms*; 8461 4.6.4 is unmarked |
| `thermal-conductivity` | TF TH | **CF CH TF TH** | 8464 6.1.2.1 *Energy transfers in a system* (thermal conductivity, wall thickness). RP2 (thermal insulators) is still a physics-only layer |
| `resolving-forces` | TH | **CH TH** | 8464 6.5.1.4 (HT only): resolving into components, vector diagrams |
| `free-body-diagrams` | TH | **CH TH** | 8464 6.5.1.4 (HT only): free body diagrams |
| `motion-in-a-circle` | TH | **CH TH** | 8464 6.5.4.1.3 (HT only): constant speed, changing velocity |
| `wave-front-refraction` | TH | **CH TH** | 8464 6.6.2.2 (HT only): wave front diagrams; 6.6.2.3 (HT) radio waves |
| `dark-matter-dark-energy` | TH | **TF TH** | 8463 4.8.2 *Red-shift* (physics only, **not** HT) |

**Considered, not changed:**
- `decomposition` stays CF CH TF TH. Its Combined core is 8464 4.7.2.2 (the role of microorganisms in cycling materials). It is a live batch-2 lesson, and its Combined pages already teach only 4.7.2.2. The audit's MOVE NARROWER verdict was overruled.
- `gravity-stable-orbits` stays TH. Its content is the HT bullets of 8463 4.8.1.3.
- Chemistry: 93 subtopics checked, 0 moves.

Page counts after the change: biology CF/CH 67→69, TF 87, TH 89. Physics CF 50→51, CH 53→58, TF 64→65, TH 82. The physics audit's "TF 64 → 66" was one too many: `thermal-conductivity` was already on TF.

## Every page whose route set changes (11 new pages)

- `combined/foundation/biology/inheritance/meiosis.html`
- `combined/higher/biology/inheritance/meiosis.html`
- `combined/foundation/biology/inheritance/classification-living-organisms.html`
- `combined/higher/biology/inheritance/classification-living-organisms.html`
- `combined/foundation/physics/energy/thermal-conductivity.html`
- `combined/higher/physics/energy/thermal-conductivity.html`
- `combined/higher/physics/forces/resolving-forces.html`
- `combined/higher/physics/forces/free-body-diagrams.html`
- `combined/higher/physics/forces/motion-in-a-circle.html`
- `combined/higher/physics/waves/wave-front-refraction.html`
- `triple/foundation/physics/space/dark-matter-dark-energy.html`

Each exists in `mrbadmus_site/` and in its round-tripped repo-root mirror.

### Fields corrected on the NEW copies only

The eight frozen content fields are verbatim except for `triple_only`, which was corrected where its text is false on the new route. Two non-frozen fields were also corrected. The existing TF/TH copies are untouched, so those pages stay byte-identical.

| copy | field | change | why |
|---|---|---|---|
| meiosis CF, CH | `triple_only` | omitted (None) | "biology-only — not in Combined Science" is false. The box never renders on Combined anyway |
| classification CF, CH | `triple_only` | omitted | same |
| thermal-conductivity CF, CH | `triple_only` | omitted | "not in Combined Science" is false |
| thermal-conductivity CF, CH | `spec` | `6.1.3 (physics only)` → `6.1.2.1` | the "physics only" label is false on Combined (audit §2.1) |
| thermal-conductivity CF, CH | `rp` | omitted | RP2 is physics-only. Commander: it "stays a physics-only layer", so the Required Practical box is not served on Combined |
| resolving-forces, free-body-diagrams, motion-in-a-circle, wave-front-refraction CH | `triple_only` | omitted | "physics-only" / "not in Combined Science" is false on CH |
| dark-matter-dark-energy TF | `triple_only` | "…(HT only, physics only)…" → "Dark matter and dark energy (physics only) — not in Combined Science." | "HT only" is false on TF. This box renders on TF |
| dark-matter-dark-energy TF | `spec` | `6.8.4 (HT only, physics only)` → `6.8.4 (physics only)` | "HT only" is false on TF |

The `higher` field is kept on the CH copies. It is true there, and it only renders at Higher tier.

## Changed pages, with reasons

**21 pages, content diff** (each in `mrbadmus_site/` and the root mirror):

- **Topic index pages** (new row(s) added, rows renumbered, subtopic count tag):
  - `combined/{foundation,higher}/biology/inheritance.html`
  - `combined/{foundation,higher}/physics/energy.html`
  - `combined/higher/physics/forces.html`
  - `combined/higher/physics/waves.html`
  - `triple/foundation/physics/space.html`
- **Neighbours whose Previous/Next arrow now points at a new page** (one-line change each):
  - `combined/{foundation,higher}/biology/inheritance/{sexual-asexual-reproduction,dna-genome,resistant-bacteria}.html`
  - `combined/{foundation,higher}/physics/energy/energy-resources.html`
  - `combined/higher/physics/forces/{resultant-forces,work-done-energy-transfer,stopping-distance-braking,momentum}.html`
  - `combined/higher/physics/waves/uses-em-waves.html`
  - `triple/foundation/physics/space/red-shift-big-bang.html`

**`shared/ks4-nav.js`** (+ `mrbadmus_site/` copy): `FULL_NAV` is generated from `all_subtopics_*.py`. Exactly 8 entries' `routes` changed, the eight slugs above, and nothing else in the file.

**96 pages, cache-bust stamp only.** These are the batch-2/batch-3 lesson pages that load `ks4-nav.js`. The only diff on each is `ks4-nav.js?v=1e068c64` → `?v=a938aae0`. Slugs and how many pages each: atom-economy 2, atoms-elements-compounds 4, carbon-cycle 4, carbonates-halides-sulfates 2, changes-in-energy 4, chromosomes-mitosis 4, concentration-of-solutions 4, conservation-of-mass 4, decomposition 4, early-atmosphere 4, enzymes 4, eukaryotes-prokaryotes 4, greenhouse-gases 4, internal-energy 4, lenses 2, metal-hydroxides 2, microscopy 4, mixtures 4, particle-motion-pressure 4, percentage-yield 2, power 4, relative-formula-mass 4, sound-waves-hearing 1, specific-latent-heat 4, temperature-changes-shc 4, titrations 2, types-of-em-waves 4, using-moles-calculations 2, waves-detection-exploration 1.

**Derived files:**
- `ks4_batch-2_manifest.json` and `ks4_batch-3_manifest.json`: the page and asset hashes for the stamp change above.
- `docs/ks4/BATCH-PLAN.md`: regenerated with `tools/ks4_batch_plan.py --write`, and `--check` is green. Only the 8 rows' route columns changed.
- `ks4_data/questions/**` (15 files): `tier`/`triple_only` re-stated on the 468 questions of the 8 subtopics, because `load_pool()` refuses any authored flag that disagrees with `classify()`. No other field changed: the diff is 468 `-`/468 `+` lines, all `"tier"` or `"triple_only"` values.

## Byte-identity statement

The build is `python3 build_all.py` with `CONSUMER_SIGNUP_ENABLED=true`, because main's committed config is flag-on (1fe25d395; rebased onto 1ac969940). I compared it with the committed tree at origin/main. **Every other built file is byte-identical**: everything except the 11 new pages, the 21 + 96 pages above, and `shared/ks4-nav.js`, in both `mrbadmus_site/` and the root mirror.

**No B2C file differs** (`consumer/`, `parents/`, `go/`, `org/`, `robots.txt`, `sitemap.xml`). The sitemap lists only `/parents/` pages, so the new route pages do not appear in it. `shared/search-index.js` is unchanged.

## Follow-ups for the chat (after merge)

### Backend: `curriculum-tree.json`

Not committed here. In `mrbadmus---backend`:

```
cd /Users/midebadmus/Documents/GitHub/mrbadmus-site && python3 tools/export_curriculum_tree.py   # writes ../mrbadmus---backend/curriculum-tree.json
```

(or copy the pre-generated `/private/tmp/claude-501/curriculum-tree.json`, sha1 `a81cb1926170310035335d7552bbc6d4c8c75704`)

The diff against backend origin/main is **8 lines, flags only**. Counts are unchanged (KS4 25 topics / 264 subtopics):
- `triple_only: true → false` for meiosis, classification-living-organisms, thermal-conductivity, resolving-forces, free-body-diagrams, motion-in-a-circle, wave-front-refraction.
- `tier: "higher" → "foundation"` for dark-matter-dark-energy.

The Set work tree then offers these subtopics to Combined classes (and dark matter to TF). Redeploy Render.

### DB: `ks4_assignment_bank`

Run `docs/ks4/route-audit/BANK-FLAGS.sql` on TEST and then on PROD after merge. It is not a migration. It has a pre-check, three UPDATEs, an abort-unless-468 guard and a commented rollback.

| slug | rows | before | after |
|---|---|---|---|
| meiosis | 64 | foundation, triple | foundation, base |
| classification-living-organisms | 64 | foundation, triple | foundation, base |
| thermal-conductivity | 70 | foundation, triple | foundation, base |
| resolving-forces | 54 | higher, triple | higher, not triple |
| free-body-diagrams | 54 | higher, triple | higher, not triple |
| motion-in-a-circle | 54 | higher, triple | higher, not triple |
| wave-front-refraction | 54 | higher, triple | higher, not triple |
| dark-matter-dark-energy | 54 | higher, triple | foundation, triple |

- **468 rows in total, 96 of them inside the frozen window** (`bank_position` 0–11).
- No id, band, position or text changes.
- **`frozen_window_guard` trips:** it compares `tier`/`triple_only` of every frozen row against PRODUCTION, and reports exactly those 96 rows. It goes green once BANK-FLAGS.sql is applied. The 96 rows cannot go on the 28-id allowlist, because that allowlist forbids flag changes. Applying the SQL is the fix.
- **`ks4_pool_check` does not trip.** The window's shape is unchanged: four per band, and positions are untouched.
- Auto composition is affected after apply: Combined classes' automatic weekly sets can now draw these subtopics (positions 0–11). That is intended by the ruling. All 54 dark-matter questions become Foundation-tier for TF classes, including the ones authored in the `harder` band.

## Gates

Fast gates, all run:

| gate | result |
|---|---|
| verify_questions, ks3_smoke_static, brand_one_mark, answer_positions, answer_lengths, teacher_tells, flashcard_engine_test, **pool_ownership**, leaderboard_tells, week_truth, leaderboard_seam, **ks4_pool_check**, **set_work_scope_check** (no `--db`), set_work_unit, figure_manifest, ks4_export_prod_figure_guard, figures_mirror, ks4_chrome_tells, gate_coverage, gate_watches_check, ks3_statutory, ks3_key_audit, ks3_rail_manifest, seating_tells, theme_wiring_check, contrast_audit, **ks4_pilot_check**, **ks4_batch_check** (batch-2 52 pages, batch-3 44 pages), student_lessons_cards_check, ks4_science_rulings_check | ✅ |
| **curriculum_tree_mirror** | ❌ **expected.** The backend's tree still carries the old 8 flags; green once the backend follow-up lands |
| **frozen_window_guard** | ❌ **expected.** 96 frozen KS4 rows differ from PROD in `tier`/`triple_only` only (KS3 clean, 0 order mismatches); green once BANK-FLAGS.sql is applied |
| 3d_isolation | ⚠️ could not run: `3d-studio/dist` does not exist in this worktree (environment, unrelated) |
| export_ks3_questions_verify | ⏭️ skipped by design: needs `MRB_TEST_STUDENT_PASSWORD`, which this run must not set (KS3, unaffected) |

KS4 drives:

| gate | result |
|---|---|
| `ks4_parity --batch batch-2` | ✅ 728 PASS, 0 FAIL |
| `ks4_parity --batch batch-3` | ✅ 616 PASS, 0 FAIL |
| `ks4_parity` (pilot) | ⚠️ harness crash, twice: headless Chrome CDP timeout (`timed out waiting for 2 bytes from chrome`) after 54 PASS / 0 FAIL. None of the 14 pilot lessons' 54 pages and none of their assets differ from origin/main, so this PR cannot move its outcome. Not a finding about this change |

Slow gates recorded by the pre-push guard: `ks4_chrome_drive` ✅ PASS, `verify_ks3` ✅ PASS. `ks4_pool_drive`, `set_work` and the MRB_BACKEND-bound gates were skipped by the guard because their credentials or backend were not set, and this run must not set them.

The commit carries `GATE-OVERRIDE` lines for `frozen_window_guard` and `curriculum_tree_mirror` only, for the reasons above.

## Found, not changed (content, not routes)

**Biology**
- `meiosis`: the meiosis I/II stage detail goes beyond both specs ("Knowledge of the stages of meiosis is not required"). It is now served on CF/CH. The TH copy's `higher` (chiasmata, independent assortment) is served on CH.
- `meiosis`, `classification-living-organisms`: the TF/TH copies still carry the now-false `triple_only` note "not in Combined Science". It was left so those pages stay byte-identical. `classification` spec label `4.6.5` should be 4.6.4.
- `decomposition`: RP labelled "RP7"; the decay practical is 8461 **RP10**. Biology-only content (rate factors, compost/biogas, RP) is served on Combined and should be a TF TH layer.
- Biology-only content leaking onto base pages:
  - `sexual-asexual-reproduction` (8461 4.6.1.3)
  - `dna-genome` (nucleotides/base pairing, 8461 4.6.1.5)
  - `evolution-natural-selection` (Wallace, 8461 4.6.3.1)
- No page exists for 8461 4.5.3.3 (water/nitrogen balance, kidney, dialysis), 4.5.4 (plant hormones, RP8), or 4.6.3.2 (speciation).
- `site_spec` labels that differ from AQA's numbering: cloning, understanding-genetics, classification, environmental-change, heart.

**Physics**
- `thermal-conductivity`: the frozen `theory` still contains a "Required Practical — Thermal Insulation (RP2 — physics only)" section, and the frozen `key_note` mentions RP2. Both are now shown on Combined (correctly labelled physics only) and need a layer.
- `resolving-forces` / `free-body-diagrams`: the pages use trigonometry (F cosθ, F sinθ). 8464/8463 say "scale drawings only". This is a content point for Mide, now on CH too.
- `motion-in-a-circle`: the orbit material (8463 4.8.1.3, HT, physics only) should be a TH layer. It is now served on CH. Its spec label `6.5.6` should be 6.5.4.1.3.
- `dark-matter-dark-energy`: the percentages, rotation curves and lensing go beyond the spec. Spec label `6.8.4` does not exist (8463 4.8.2). The TH copy still says "HT only".
- Layers shown on the wrong routes:
  - pV = constant on `particle-motion-pressure`
  - F = mΔv/Δt on `momentum`
  - p = hρg and upthrust on `pressure-in-a-fluid`
  - HT orbit material on `solar-system-gravity`
- Wrong RP numbers:
  - `properties-em-waves-1` shows RP9 refraction (physics-only) as "RP20" to Combined.
  - The base infrared RP (8464 RP21 / 8463 RP10) is on no page.
  - "RP21" is attached to magnetic-field plotting and electromagnets, which are not AQA RPs.
- No page exists for 8463 4.3.3.3 (bicycle pump), 4.6.1.3 (reflection + RP9), or 4.6.2.6 (visible light).

**Chemistry**
- Spec labels:
  - `nanoparticles` (5.2.3.3 → 4.2.4.1–2)
  - `oxidation-reduction` (5.4.1.4 → 5.4.1.1/5.4.1.3 + HT). Its CF/TF key note teaches electron transfer unlabelled.
  - `giant-covalent-structures` (understated)
- Chemistry-only HT content in `higher` fields served on CH: concentration-of-solutions, using-moles-calculations, cracking-alkenes.
- No page exists for 8462 4.3.5 (gas volumes, TH).

## Landing: rebase onto main after the frozen corrections (4 Oct 2026)

### The rebase

`fix/ks4-route-flags` was cut from `1ac969940`. By 4 Oct, `origin/main` had moved 29 commits to `e417fb16b` (Merge PR #24, `feat/ks4-frozen-corrections`). It was rebased onto `e417fb16b`. The pre-rebase tip `31fb3e786` is kept as the tag `pre-rebase-ks4-routes`.

- **Text conflicts: 2 files**, `ks4_batch-2_manifest.json` and `ks4_batch-3_manifest.json`. Both are build output (page and asset sha256s). Both branches rewrote them for different reasons: the corrections changed `ks4-source-batch-{2,3}.js`, and this branch changed `ks4-nav.js`.
- **How they were resolved:** not by hand. Both were reset to main's copy, then `python3 build_all.py` (exit 0, all 8 generators) rewrote them. The result has the same keys as main's manifests. The only values that differ are `shared/ks4-nav.js`'s hash and the batch pages that carry its cache-bust stamp, which is this branch's change and nothing else.
- **Everything else merged as text**, including the five `all_subtopics_*.py` files both branches edit. After the build, **no other file changed**: every auto-merged page and script was already byte-identical to fresh build output.

### The frozen corrections survive

Checked against the data, not the text. Each route file was parsed as data, and every value was given an address (topic → subtopic id → field → index). An inserted subtopic cannot shift another value's address that way.

- **The seven route files this branch does not touch match `FROZEN-CORRECTIONS.md`'s after-md5s exactly:** `biology_triple_foundation`, `biology_triple_higher`, all four chemistry files, and `physics_triple_higher`. Both chemistry triple files are among them, so **atom economy's text (AE-1…AE-6, TF and TH) is byte-for-byte as corrected.**
- **The five it does touch** (`biology`, `biology_higher`, `physics`, `physics_higher`, `physics_triple_foundation`): the changed values between `1ac969940` and `origin/main` come to exactly **163**, matching the report. **All 163 are present at their own address with the corrected text** (64 of them are in these five files). **No pre-correction text came back:** no "before" string occurs more often in any file than it does on main.
- **Outside the eight moved subtopics, every value in all twelve files equals `origin/main`.** None of the 16 corrected subtopics is one of the eight moved ones, so no dict copied for a new route can carry old text.
- **The eight moved subtopics' 1,150 values are identical to the reviewed branch** (`pre-rebase-ks4-routes`). `ks4_data/`, the audit docs and `BATCH-PLAN.md` are unchanged by the rebase.
- `shared/ks4-source-batch-{2,3}.js` and `ks4_lessons/` are identical to main, so the served banks and the removed `withhold` entries are as PR #24 left them.

### Pages, arrows, nav, classify()

- **11 new pages** exist in both trees, are byte-identical between them, and did not exist on main.
- **Previous/Next on every KS4 subtopic page:** 876 pages on all four routes. Old-design pages use `nav-arrow` anchors; batch lessons use `mrbPrevNext`. Within each topic, the chain follows the route file's order exactly. No first or last page's outer arrow changed, and no arrow is a dead link. **Arrows changed on exactly 14 existing pages**, the neighbours listed above.
- **Pages whose content changed:** exactly the 21 listed above (7 topic indexes + 14 neighbours). Every other changed page differs from main only in the `ks4-nav.js?v=` stamp.
- **`shared/ks4-nav.js`:** `FULL_NAV` was parsed on both sides. **8 values change, the `routes` of the eight slugs**, as in the route table. The `mrbadmus_site/` copy is identical.
- **`ks4_data.classify()`** runs its CF⊆CH⊆TH and CF⊆TF⊆TH assertion inside the call, and it passes. Flags: meiosis, classification and thermal-conductivity are foundation/base. Resolving-forces, free-body-diagrams, motion-in-a-circle and wave-front-refraction are higher/not-triple. Dark-matter is foundation/triple. Decomposition and gravity-stable-orbits are unchanged.

### Gates on the rebased tree

Run with `MRB_BACKEND`/`MRB_BACKEND_DIR` pointed at a backend worktree at backend `main` (`4bdc783`). The shared backend checkout has someone's uncommitted edit, so it was not used.

- `prepush_gate.py --record-all`: **`verify_ks3` ✅, `ks4_chrome_drive` ✅** (the two affected slow gates). Every other slow gate was skipped by rule, or for a missing credential as before.
- `prepush_gate.py --check`: **every fast gate ✅**, including `ks4_pilot_check`, `ks4_batch_check`, `ks4_pool_check`, `pool_ownership`, `set_work_scope_check`, `figures_mirror` and `ks4_science_rulings_check`. **Two are red, both expected, both overridden in the merge commit:**
  - `frozen_window_guard`: the 96 frozen rows' flags, as above, until `BANK-FLAGS.sql` is applied.
  - `curriculum_tree_mirror`: now red for **two** files. One is the backend's `curriculum-tree.json`, as before. **New since this branch was cut:** `consumer/curriculum-index.json`, the B2C topic picker's index, added on main by `cf693ee76`. The same exporter writes it.

### ⚠️ New for the follow-up: `consumer/curriculum-index.json`

`python3 tools/export_curriculum_tree.py` (the backend follow-up above) **also rewrites `consumer/curriculum-index.json`**. It was not regenerated in this landing because it is B2C data, and B2C is outside this unit. Regenerating it changes 15 subtopics' year maps:

- **The 8 moved subtopics gain their new route keys**, e.g. meiosis `{tf:11, th:11}` → `{cf:11, ch:11, tf:11, th:11}`.
- **7 Combined Higher physics subtopics move from Year 11 to Year 10:** structure-of-atom, mass-number-isotopes, development-atomic-model, radioactive-decay, nuclear-equations, half-lives and radioactive-contamination. This is mechanical. `ks4_seed_sow.split_index` cuts each block at the topic boundary nearest halfway. CH physics grew from 53 to 58 subtopics, so the cut now falls after Atomic Structure instead of before it. **For Mide:** the B2C picker would then show Atomic Structure as Year 10 for a Combined Higher child. The seeded scheme-of-work rows in the database are not regenerated by any of this, so schools' automatic weekly sets are unaffected.

Until that follow-up runs, the new Combined pages are live, but Set work and the B2C picker do not yet offer the eight subtopics on their new routes. Nothing breaks.

### Merge

Merged to `main` with `--no-ff` and pushed as a fast-forward of `main`. The merge commit is recorded in the next section. The remote `fix/ks4-route-flags` still points at the pre-rebase `31fb3e786`. It was not force-pushed, because a force-push is a stop item.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
