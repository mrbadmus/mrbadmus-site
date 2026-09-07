# MRB-332 — what the rebase onto MRB-331 has to do

This lane (`feat/ks4-pool`) merges **after** MRB-331 (`feat/set-work`), rebased.
Most of it is additive and rebases cleanly. Four things do not, and each one is
a place where MRB-331 is currently *correct* and this ticket makes it wrong.

---

## 1. Three checks in `set_work_drive.py` invert

MRB-331's drive asserts, correctly for its own branch, that KS4 has no bank:

| line | assertion | after this ticket |
|---|---|---|
| `record(trip.get("has_bank") is False, …)` | KS4 `has_bank` is false | **must become `is True`** |
| `record(all(r.get("available", 0) == 0 …))` | every KS4 lesson offers nothing | **must become `> 0`** for seeded subtopics |
| the colliding-slug check | the eight report `available == 0` | **changes shape — see §2** |

The first two are one-line inversions. Leaving them is a red drive that looks
like this ticket broke something, when in fact it delivered the thing the
assertion was waiting for.

## 2. ⚠️ The collision check must change SHAPE, not its number

This is the one that matters, and the tempting fix is the wrong one.

Eight KS4 subtopic slugs are byte-identical to KS3 lesson slugs:

```
aerobic-respiration   catalysts             changes-of-state      chromatography
conservation-of-mass  distance-time-graphs  electric-fields       magnetic-fields
```

Each holds **twelve KS3 bank rows**. Each now also holds **twelve KS4 pool
rows**. So `available == 12` is true whether the route read the right table or
the wrong one, and changing the assertion from `== 0` to `== 12` would produce
a check that passes on the bug it exists to catch — the worst possible outcome,
because it would look like coverage.

**What separates the two pools is row IDENTITY, not row count.** A KS4 pool id
begins `ks4-`; a KS3 bank id looks like `c1-04-h02`. So the check must assert
that every question served to a KS4 class carries a `ks4-` id and that no KS3
id appears in a KS4 payload at all.

`ks4_pool_drive.py::check_collision` is written that way and is the reference.

## 3. `bankRefusalFor` no longer returns `no_ks4_bank`

The backend (`feat/mrb332-ks4-pool`, off `feat/mrb331-set-work`) renamed the
refusal reason to `no_bank_for_key_stage`, because `no_ks4_bank` had become a
false statement — KS4 has a bank; KS5 is what has none. `has_bank` is
unchanged and is what the set-work page keys on. No frontend reads either
string today; grep before assuming that is still true at merge time.

## 4. Two migrations apply to production at merge, not before

| migration | what it does |
|---|---|
| `20260906230000_mrb332_ks4_assignment_bank.sql` | the pool table, its indexes and its RLS read policy |
| `20260906230500_mrb332_overrides_ks4_week_ceiling.sql` | `scheme_of_work_overrides.academic_week` 1..39 → 1..60 above KS3 |

Both are rehearsed on TEST. Both have rollback pairs in `supabase/rollbacks/`.
Per CLAUDE.md, they reach production **at merge**, one at a time via
`apply_migration`, never `db push`.

⚠️ The two week ceilings are deliberately different numbers and it is not an
oversight: `scheme_of_work_entries` (the generated AQA default) is capped at
**52**, because that sequence's length is knowable; `scheme_of_work_overrides`
(a real school's own sequence) is capped at **60**, because a school counts
taught lessons — tests, reviews, practicals split over two periods — and
Rainford's Year 11 Biology runs to 55. Do not "harmonise" them.

## 5. The scheme was already seeded — do not re-seed it

`scheme_of_work_entries` already holds all **865** KS4 rows on TEST *and* on
production, seeded by MRB-310 with zero omissions. MRB-332's brief said prod
had none; that was stale. `ks4_seed_sow.py` was re-run to confirm it still
generates the same 865 with 0 omitted, and nothing was written.

Rainford's own sequence is a **`scheme_of_work_overrides`** matter and never
touches the platform default. See `rainford-sow-mapping.md`.

---

## ⚠️ Export AFTER review, never alongside it

`docs/ks4/pool-authoring.md` opens with "nothing exports unreviewed". That is
easy to satisfy per-subject and easy to get wrong per-*run*.

**What happened in this build, stated accurately.** Physics was exported to
TEST as soon as its authoring finished, while two of its four cold reviewers
had not yet reported. I assumed the export was therefore stale — carrying the
wrong answer key, the faster-than-light radio wave and the tier leaks those
reviewers went on to describe — and ordered a regeneration.

**The assumption was wrong.** The regenerated export was byte-identical to the
first: 0 of 934 rows differed, same byte counts on all four files. The reason
is that a reviewer writes its fixes to disk as it works and *reports* only at
the end, so the files were already final when the export ran; only the reports
were outstanding. Verified after the fact — `ks4-wave-front-refraction-h01`
already read 2.4 × 10⁸ m/s, and `ks4-changes-in-energy-h03` already read
50 J / 0.20 kg / 20 m/s.

**The rule survives the correction, for a different reason than I first gave.**
It is not that a mid-review export is *observably* stale — it may well not be.
It is that you cannot tell from the outside, and an export is the input to a
verification run that then certifies content. Certifying a snapshot you cannot
prove is final is the defect, whether or not the snapshot happens to be right.

**So: a subject is exported only when every reviewer holding one of its files
has reported.** Cheap to obey, and it removes the need to reason about mtimes
against report times at all — which is what I found myself doing, and got
wrong.

⚠️ The recovery cost nothing, and that is worth knowing too: the export is
`on conflict (id) do update` and reviewers preserve ids, so re-running and
re-applying is always safe. There is no state to clean up and no way to create
a duplicate. If in doubt, re-export.

---

## Order of operations at merge

1. Rebase `feat/ks4-pool` onto `main` (with MRB-331 already in).
2. Apply the two migrations to production, one at a time.
3. Run `python3 export_ks4_questions.py` against production.
4. Fix the three checks in `set_work_drive.py` (§1, §2).
5. Merge the backend branch `feat/mrb332-ks4-pool` and deploy it **before**
   the frontend, per CLAUDE.md's API-contract rule.
6. Run `ks4_pool_drive.py` and `set_work_drive.py`. Both green, or stop.
