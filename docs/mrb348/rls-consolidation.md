# MRB-348 WS-3 — consolidating `multiple_permissive_policies`

**Status:** rehearsed on TEST (`qeppkiswvclkkwbxmlok`), all three proofs green.
**Production (`urklkrwevjtlfbwnipjn`) has NOT been touched.** Nothing in this
workstream was applied, read or written against production. See
[Landing on production](#landing-on-production) — the migration must be
**regenerated** against production's own catalogue, not copied across.

**Date:** 22 September 2026
**Tool:** `tools/rls_consolidate.py`
**Forward:** `supabase/migrations/20260922030507_mrb348_rls_consolidate.sql`
**Rollback:** `supabase/rollbacks/20260922030507_mrb348_rls_consolidate_rollback.sql`

---

## 1. The problem

Supabase's performance linter raises `multiple_permissive_policies` once per
**(table, role, command)** cell holding more than one PERMISSIVE policy.
Production reports **251** findings.

The multiplier is the role grant. Nearly every policy on this estate is granted
to `public`, and the linter expands `public` across the concrete roles (`anon`,
`authenticated`, `authenticator`, `dashboard_user`, `service_role`), so one
table with 5 permissive SELECT policies is reported 20 times.

Permissive policies are OR'd, and Postgres walks every branch until one is true.
MRB-347 made each branch cheap by hoisting the per-request auth calls into
InitPlans; it did not reduce the **number** of branches, nor fix their **order**.
This ticket does both: one policy per (table, command), cheapest branch first.

---

## 2. The transform

### Step 1 — normalise `ALL`

A PERMISSIVE policy with `cmd='ALL'` also applies to SELECT, so it cannot be
folded into a SELECT-only policy without losing its write coverage. Each `ALL`
policy is first expanded into four per-command equivalents:

| command | clause |
|---|---|
| SELECT | `USING (qual)` |
| DELETE | `USING (qual)` |
| UPDATE | `USING (qual)` + `WITH CHECK (with_check IF PRESENT ELSE qual)` |
| INSERT | `WITH CHECK (with_check IF PRESENT ELSE qual)` |

⚠️ **That `ELSE qual` is Postgres semantics, not a convenience.** When an
ALL/UPDATE/INSERT policy carries no `WITH CHECK`, Postgres uses the `USING`
expression *as* the check. Dropping it would narrow writes; substituting the
obvious-looking `true` would hand every authenticated user the right to write
any row. It fired for real on this estate — `classes_teacher_update` has
`with_check = NULL`, and its merged `WITH CHECK` branch is its own `qual`.

### Step 2 — merge per (table, command)

```
merged USING      = OR over every policy's USING            (SELECT/UPDATE/DELETE)
merged WITH CHECK = OR over every policy's EFFECTIVE check  (INSERT/UPDATE)
                    effective check = with_check if present else qual
```

⚠️ **Why OR-ing the two clauses separately is exact, and not an approximation.**
For an UPDATE under several permissive policies, Postgres requires the OLD row
to satisfy at least one policy's `USING` and the NEW row to satisfy at least one
policy's `WITH CHECK` — **and they need not be the same policy**. So
`(U1 OR U2)` with `(C1 OR C2)` is precisely the original behaviour. Had Postgres
instead required a single policy to satisfy both, this merge would be a real
widening and the whole transform would be unsound. This is the load-bearing fact
the ticket rests on.

### Step 3 — order the branches cheapest first

| cost | shape |
|---|---|
| 0 | pure column predicate, no auth call at all |
| 1 | bare self-check — `<col> = (SELECT auth_user_id())`, `(SELECT auth.uid()) = <col>` |
| 2 | request-constant — `auth_user_has_scope('…')`, `auth_user_operator_active()`, … |
| 3 | school equality — `school_id = (SELECT auth_user_school_id())` |
| 4 | row-dependent call — `auth_user_teaches_class(…)`, `auth_user_is_member_of_class(…)`, … |
| 5 | `EXISTS (…)` — always last |

A composite branch takes the cost of its **most expensive** component. Ties keep
the original catalogue order, so the output is byte-reproducible.

`profiles` is the case MRB-347's header quoted at 23.9 ms for a one-row
primary-key read. Its five SELECT policies now merge into one, ordered:

```
1: Users can view own profile            ← the cheap self-check, now FIRST
2: profiles_operator_read
3: profiles_admin_read_school
4: profiles_hod_read_dept
5: profiles_teacher_read_students        ← the EXISTS into class_members, now LAST
```

### Step 4 — what is deliberately not touched

See [§6](#6-what-i-left-alone-and-why).

---

## 3. The three proofs

### Proof A — inverse transform (static, offline, runs before anything is applied)

Every generated merged expression is split back into its top-level OR branches
and the multiset of recovered branches is compared against the multiset of the
original per-policy expressions.

The splitter is a real paren-, string-literal- and identifier-aware scanner
(`split_top_level_or`), **not** a regex on `" OR "`. A regex splits inside
string literals, inside nested subqueries, and inside identifiers — and every
one of those would make this proof pass for the wrong reason. `ORDER`,
`auth_user_operator_active` and a column named `or_flag` all contain the
letters; none is a top-level `OR`. Dollar-quoting is refused outright rather
than guessed at.

```
clauses checked        : 96
branches checked       : 188
round-trip failures    : 0
```

Proof A also runs inside `merge_cell`, so an unprovable merge never reaches the
emitter at all — it becomes a skip with a reason, not a silent output.

### Proof B — visibility digest on TEST (dynamic)

10 real fixture users spanning every role sign in **with the anon key** so RLS
actually applies (never the service-role key, which bypasses RLS entirely), and
for each of the 25 affected tables the full visible row set is fetched ordered
by primary key and hashed.

| user | role / standing |
|---|---|
| `hz_s1`, `hz_s2` | student, 1 class membership each |
| `hz_snull` | student with **no school** — the empty-standing edge |
| `hz_amy`, `hz_ben`, `hz_t2` | teacher, 1 class each |
| `hz_rich` | teacher + `hod` scope |
| `hz_slt` | teacher + `slt` scope |
| `hz_admin` | teacher + `school_admin` scope |
| `hz_legacyadmin` | legacy `admin` role, no scope rows |

```
users signed in        : 10 / 10
cells captured         : 250   (10 users x 25 tables)
NON-EMPTY cells        : 106   <- the cells that actually prove something
rows fingerprinted     : 8,256
row-count mismatches   : 0
digest mismatches      : 0
```

⚠️ **The non-empty count is reported separately on purpose.** A table a user
sees 0 rows in before and 0 rows in after proves nothing; a proof made only of
empty sets is not a proof. 106 of the 250 cells carried real rows, covering
8,256 rows in total.

### Proof C — rollback

The rollback was exercised end to end on TEST, not merely emitted.

```
policies before        : 141
policies after rollback: 141
missing                : 0
extra                  : 0
differing roles/cmd/permissive/expression : 0
byte-identical qual + with_check          : 141 / 141
```

Proof B was then re-run against the **original** baseline:

```
cells compared         : 250
NON-EMPTY cells        : 106
rows fingerprinted     : 8,256
row-count mismatches   : 0
digest mismatches      : 0
```

⚠️ Unlike MRB-347's rollback, this one cannot be a simple `ALTER`: the forward
migration **drops** policies and **creates** differently-named ones, so restoring
means recreating objects — including their `permissive` flag, their roles and
their command. All four are stored in `public.mrb348_policy_backup` for exactly
that reason. A rollback that restored the expressions but not the GRANT set
would quietly change who each policy reaches.

### The drift guard, proven by firing

MRB-347's migration rewrote whatever it found at apply time, because its
transform was idempotent and per-policy. **This transform is neither** — it
depends on the exact set of policies present, so a self-applying version run
against a catalogue it was not generated from would merge the wrong set and say
nothing.

So the migration carries the expected `qual`/`with_check` of every policy it
drops, and a guard block that aborts if the live catalogue differs by a byte.
That guard was tested in **both** directions:

- **Passes** on a matching catalogue — including after the rollback, which is
  itself independent evidence the restore was byte-exact.
- **Fires** on a mismatched one. Re-applying the migration to the
  already-merged database aborted with
  `MRB-348 aborted: policy academic_years.academic_years_admin_write not found.
  This migration is pinned to the catalogue it was generated from` — and the
  catalogue was left untouched (122 policies, 78 merged, unchanged).

A guard never seen to fire is not a proven guard.

### Production-refusal, proven by refusing

`tools/rls_consolidate.py` decides which project it is pointed at by
base64-decoding the `ref` claim out of the service-role JWT — never from the
`--project` flag, a filename, or a label beside the credential. Both refusal
paths were exercised:

| case | result |
|---|---|
| `--project prod`, no flag | refused, exit 1 |
| `--project test` but the credential is production (**the label lie**) | refused, exit 1 — the JWT wins over the flag |

This is the MRB-338 lesson applied: on 9 Sep 2026 TEST and production held
*identical* row counts in both question banks, so no count and no glance at a
table could have told them apart. The key's own `ref` claim could.

---

## 4. Results

### Linter findings

Modelled with the linter's own rule (`public` expanded across the concrete
roles), then confirmed against the real advisor output:

| | findings |
|---|---|
| TEST before | **231** |
| TEST after | **1** |
| Real `get_advisors(performance)` on TEST after | **1** — the same one |

The single survivor is `school_invitations` / `authenticated` / `SELECT`, which
is one I deliberately left alone — see [§6](#6-what-i-left-alone-and-why). The
model reproducing the real linter exactly is what gives confidence that
production's 251 will fall to a comparable residue.

### Policy counts on TEST

| | |
|---|---|
| policies before | 141 |
| policies after | 122 |
| of which merged | 78 |
| restrictive policies, before and after | 0 |
| rows in `mrb348_policy_backup` | 141 |
| multi-permissive **public** cells after | 0 |

---

## 5. What I consolidated

25 tables, **97 policies → 78**. Command column shows which merged policies were
created (S/I/U/D).

| table | dropped | created | commands |
|---|---|---|---|
| `academic_years` | 2 | 4 | S/I/U/D |
| `assignment_question_attempts` | 5 | 4 | S/I/U/D |
| `assignment_questions` | 4 | 4 | S/I/U/D |
| `assignment_submissions` | 7 | 4 | S/I/U/D |
| `assignments` | 7 | 4 | S/I/U/D |
| `audit_log` | 3 | 1 | S |
| `class_members` | 7 | 2 | S/I |
| `class_shoutouts` | 6 | 3 | S/I/U |
| `class_teachers` | 6 | 4 | S/I/U/D |
| `classes` | 8 | 4 | S/I/U/D |
| `family_messages` | 2 | 1 | S |
| `pending_staff` | 2 | 4 | S/I/U/D |
| `platform_flags` | 2 | 4 | S/I/U/D |
| `platform_operator_activations` | 2 | 4 | S/I/U/D |
| `platform_operators` | 2 | 4 | S/I/U/D |
| `profiles` | 5 | 1 | S |
| `scheme_of_work_overrides` | 3 | 4 | S/I/U/D |
| `school_period_times` | 2 | 4 | S/I/U/D |
| `school_subject_settings` | 3 | 4 | S/I/U/D |
| `schools` | 2 | 1 | S |
| `staff_scopes` | 4 | 4 | S/I/U/D |
| `student_notifications` | 5 | 2 | S/I |
| `submission_feedback` | 4 | 2 | I/U |
| `subscriptions` | 2 | 1 | S |
| `timetable_entries` | 2 | 4 | S/I/U/D |

### ⚠️ Nine tables GREW in policy count, and that is correct

`academic_years`, `pending_staff`, `platform_flags`,
`platform_operator_activations`, `platform_operators`,
`scheme_of_work_overrides`, `school_period_times`, `school_subject_settings`
and `timetable_entries` all end with **more** policy objects than they started
with (typically 2 → 4).

This is Step 1 working, not a defect. Each of those tables has an `ALL` policy
whose SELECT branch had to be merged with a separate SELECT policy. Splitting
the `ALL` into four per-command equivalents is the only way to do that, and
Postgres has no "INSERT, UPDATE and DELETE" command to fold the three write
halves back into one.

The count is not the metric — **cells** are. Every one of those tables goes from
1 multi-permissive cell to 0, and because each command only ever consults its own
cell, the extra policy objects cost nothing at runtime.

### Coverage audit

A separate check confirmed, for every table in the plan, that the set of
commands covered by the dropped policies is exactly the set covered by the
created ones, and that clause shapes are legal (SELECT/DELETE carry `USING`
only; INSERT carries `WITH CHECK` only; UPDATE carries both):

```
command-coverage defects : 0
clause-shape defects     : 0
```

Single-policy cells were left alone, which the live catalogue confirms:
`submission_feedback_select` and `class_members_staff_update` both survive
untouched beside their merged siblings.

---

## 6. What I left alone, and why

**Nothing here is a failure.** Each of these is a case where equivalence could
not be proven, so the policy stays exactly as it was.

### 6.1 Eleven policies granted to a role other than `public` (11 skips, 10 tables)

Merging across differing GRANT sets changes **who** a policy reaches, which is a
security change rather than a performance one.

| table | policy | roles |
|---|---|---|
| `account_deletion_requests` | `account_deletion_requests_read_own_org` | `{authenticated}` |
| `ks3_assignment_bank` | `ks3_assignment_bank_read` | `{authenticated}` |
| `ks3_cards` | `ks3_cards_read` | `{authenticated}` |
| `ks3_ladder_questions` | `ks3_ladder_questions_read` | `{authenticated}` |
| `ks4_assignment_bank` | `ks4_assignment_bank_read` | `{authenticated}` |
| `revision_materials` | `revision_materials_public_read` | `{anon,authenticated}` |
| `rum_timings` | `rum_timings_insert_self` | `{authenticated}` |
| `rum_timings` | `rum_timings_read_admin` | `{authenticated}` |
| `scheme_of_work_entries` | `sow_entries_authenticated_read` | `{authenticated}` |
| `school_invitations` | `invitations_invitee_read` | `{authenticated}` |
| `subjects` | `subjects_authenticated_read` | `{authenticated}` |

### 6.2 `school_invitations` — the one linter finding that survives

This is the residue, and it is worth naming precisely because it looks like a
miss and is not one.

`school_invitations` holds `invitations_admin_all` (`ALL`, granted to `public`)
and `invitations_invitee_read` (`SELECT`, granted to `{authenticated}`). For the
**public** role there is only one SELECT policy, so my plan correctly saw no
multi-permissive cell. But the linter expands `public` to include
`authenticated`, and for *that* role both policies apply to SELECT — hence one
finding.

Closing it would mean merging a `public` policy with an `authenticated` one,
which is exactly the change §6.1 refuses to make. **Left as is, deliberately.**
Closing it is a separate decision about whether `invitations_admin_all` should
be narrowed to `authenticated`, and that is a product/security call, not a
performance refactor.

### 6.3 Restrictive policies — none found, but the refusal is implemented

TEST carries **0** RESTRICTIVE policies, so this rule never fired. It is
implemented and guarded anyway, in two places, because **production's policy set
is not identical to TEST's** (153 vs 141) and a restrictive policy could exist
there:

- `build_plan` skips the **whole table** if any restrictive policy is present.
- The migration's guard block independently re-checks `permissive` at apply time
  and aborts if a policy it is about to drop is restrictive on the target.

Restrictive policies AND rather than OR; folding one into the OR would widen
access. This is the failure mode most worth being paranoid about, which is why
it is checked twice.

### 6.4 Unparseable expressions — none found

No policy expression on TEST defeated the scanner. Had one (dollar-quoting,
unbalanced parens, a failed round-trip), its whole table would have been skipped
with the reason recorded, rather than emitted and hoped for.

---

## 7. Landing on production

⚠️ **Do not apply
`supabase/migrations/20260922030507_mrb348_rls_consolidate.sql` to production as
it stands.** It is pinned to TEST's catalogue. Production has 153 policies to
TEST's 141, and MRB-347 already documented that the two differ in expression
(`profiles_teacher_read_students` carries an extra `cm.deleted_at IS NULL` on
production). The guard would abort — which is the safe direction, but it is not
the intended workflow.

Regenerate it against production's own catalogue:

```bash
export MRB_PROD_URL=...            # production URL
export MRB_PROD_SERVICE_KEY=...    # production service-role key
python3 tools/rls_consolidate.py --project prod --check        # Proof A first
python3 tools/rls_consolidate.py --project prod --emit --i-am-sure-production
```

`--check` runs Proof A against production's real expressions and applies no
change. Review the emitted file, then apply through the Supabase CLI
(`supabase db push`) so it is recorded in `schema_migrations` — the CLI honours
the file's own `begin`/`commit`.

Per CLAUDE.md, *"Migrations are applied to production only at merge time, or when
Mide has explicitly ruled the migration in the current prompt."* This one has not
been ruled, and it has not been applied.

Before and after, run Proof B against production users, the way MRB-347 did —
do not infer production equivalence from the TEST run.

---

## 8. Rehearsal aids used, and their teardown

### The arbitrary-SQL seam

PostgREST cannot reach `pg_catalog`, and this machine has no usable `psql`
credential (`psql` is installed and the Supabase CLI is linked to TEST, but the
CLI's access token lives in the macOS Keychain, which a non-interactive shell
cannot unlock — CLAUDE.md records this). No `exec_sql`-style RPC existed on TEST;
I checked all 61 exposed RPCs.

So I created two functions on TEST, `public.mrb348_exec_sql(text)` and
`public.mrb348_exec_ddl(text)`.

⚠️ **The trap, and why the grants are the whole safety of these objects:** a
SECURITY DEFINER arbitrary-SQL function reachable by `anon` is a total
compromise of the database — the anon key is public by design and ships in
`shared/config.js`. Execute was revoked from `public`, `anon` and
`authenticated`, and granted only to `service_role`, and that was **verified
from `has_function_privilege`** rather than assumed:

```
mrb348_exec_sql : anon=false  authenticated=false  service_role=true
mrb348_exec_ddl : anon=false  authenticated=false  service_role=true
```

**Both were dropped at the end of the rehearsal.** The SQL is kept, for
reproducibility, at `supabase/seeds/mrb348_rehearsal_exec_seam.sql` — the
`seeds/` folder is test-only fixture SQL that the Supabase CLI never reads, so
`supabase db push` cannot pick it up. Re-apply it by hand against TEST if you
need to re-run the tool, and drop it again afterwards.

### Fixture passwords

Proof B needs a user per role. The prompt supplied the password for `hz_amy`,
`hz_rich` and `hz_s1` only — teacher, HoD and student — which leaves
`school_admin`, `slt` and the no-school edge unproven. I set the same password on
seven further `hz_*` TEST fixtures via the Auth admin API so the matrix covers
every role. **TEST only**, and all of them are `@test.mrbadmus` fixtures.

### State TEST is left in

**TEST is left in the CONSOLIDATED state**, so it mirrors what production would
become and can be inspected directly. `public.mrb348_policy_backup` holds all
141 originals, and the rollback is proven to restore them byte-for-byte.

The migration was applied through the rehearsal RPC, **not** the Supabase CLI, so
it is **not** recorded in TEST's `schema_migrations`. A later `supabase db push`
against TEST will therefore try to apply it and — correctly — abort at the guard,
because the catalogue no longer matches. Run the rollback first if you want TEST
to take it through the CLI.

---

## 9. Deviations and surprises

- **Deviation: `psql` *is* installed on this machine**, contrary to the brief —
  but with no reachable password (Keychain access is blocked to this shell), so
  it was unusable anyway. I reached the catalogue through the Supabase connector,
  which takes an explicit `project_id` on every call and therefore has no ambient
  default to be wrong about — the shape CLAUDE.md §8 now prefers over the swap
  dance. I still cross-proved the target: the connector's `project_id=TEST` call
  and the JWT-verified TEST service key report identical counts (54 profiles,
  12 classes), and those are TEST's figures, not production's (1,193 / 73).

- **Surprise: nine tables grow in policy count.** Covered in §5. Benign, and the
  consequence of Step 1 being done correctly rather than incorrectly.

- **Surprise: the linter's residue is a `public` × `authenticated` overlap, not
  a missed merge.** §6.2. Worth knowing before someone reads "251 → small
  number" and goes hunting for the gap.

- **Transient, not a finding:** the first Proof B "after" capture died on a
  socket read timeout part-way through, losing every cell already measured. The
  harness now retries transport errors (never HTTP statuses, which are real
  answers) with backoff, per the MRB-346 gate contract. The re-run was clean.

- **The `ELSE qual` rule fired for real**, on `classes_teacher_update` and on
  every `ALL` policy with a NULL `with_check` (`assignments_admin_write`,
  `assignments_teacher_write`, and 11 others). Had it been implemented as
  `true`, the merge would have silently granted every authenticated user write
  access to those tables, and Proof B would **not** have caught it — Proof B
  reads, and this is a write-path widening. That is the single most dangerous
  part of this transform, and it is why Step 1 is written out explicitly in the
  migration header rather than left as an implementation detail.

---

## 10. Interaction with WS-2 (noted, no action taken)

`supabase/migrations/20260922114500_mrb348_teacher_class_summaries.sql` (WS-2,
another lane in this checkout — not mine) creates a SECURITY DEFINER function
that **replicates** the RLS predicates of `classes`, `class_members`,
`assignments` and `assignment_submissions` in SQL, so it can aggregate without
the caller's policies applying.

It does **not** create, drop or alter any policy, so it does not disturb this
ticket's catalogue-pinned guard. In the other direction its header explicitly
says it was written against *"the live policies (TEST, **post-WS-3
consolidation**)"* — that lane read the merged state this workstream left on
TEST, and the predicates it lists match the merged branches exactly. That is
independent corroboration that the merge preserved the boolean.

⚠️ **Standing coupling worth knowing.** WS-2's gate is a hand-maintained copy of
what these policies grant. If a future ticket changes any of those four tables'
merged policies, that function must change with them or it will return numbers
the reader could not have computed themselves. The consolidation makes this
easier, not harder — there is now one policy per (table, command) to read
instead of up to seven — but the copy is still a copy.

**Timestamps do not collide:** WS-3 is `20260922030507`, WS-2 is
`20260922114500`, so WS-3 applies first in a fresh environment. That ordering is
inert either way, since neither reads the other's objects at apply time.
