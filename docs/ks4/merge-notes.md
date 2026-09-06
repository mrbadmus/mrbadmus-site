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
easy to satisfy per-subject and easy to get wrong per-*run*, and it was got
wrong once in this build:

> Physics was exported to TEST the moment its authoring finished, while two of
> its four cold reviewers were still working. The SQL therefore carried a wrong
> answer key (√240 keyed as 15), a radio wave travelling faster than light, two
> Higher-tier leaks into Foundation questions, and ~90 questions still
> reproducing lesson-page material — every one of which the reviewers had
> already fixed in the authored files.

Nothing was lost, because the export is `on conflict (id) do update` and the
reviewers preserve ids: regenerating and re-applying corrected every row in
place, with no cleanup and no duplicates. But the load was done twice, and a
verification run against the first load would have certified content that no
longer existed.

**The rule: a subject is exported only when every reviewer holding one of its
files has reported.** The reviewers rewrite in place, so an export taken mid-
review is a snapshot of a file someone is still editing — the same hazard the
loader's own half-written-file handling exists for, one level up.

---

## Order of operations at merge

1. Rebase `feat/ks4-pool` onto `main` (with MRB-331 already in).
2. Apply the two migrations to production, one at a time.
3. Run `python3 export_ks4_questions.py` against production.
4. Fix the three checks in `set_work_drive.py` (§1, §2).
5. Merge the backend branch `feat/mrb332-ks4-pool` and deploy it **before**
   the frontend, per CLAUDE.md's API-contract rule.
6. Run `ks4_pool_drive.py` and `set_work_drive.py`. Both green, or stop.
