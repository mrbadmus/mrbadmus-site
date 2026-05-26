# Test-only seed scripts

Test-fixture SQL — fake users, fake submissions, fake auth state — that
must NEVER run on production. Lives outside `supabase/migrations/` so
the Supabase CLI does not auto-apply it on `db push`.

The CLI only reads `supabase/migrations/` — everything in this folder
is ignored by `supabase db push` and `supabase migration list`. Apply
manually only, and only against the test project.

## When to use

- Bootstrapping a fresh test environment with the fake-data universe
  the schools-layer features were built against (Sarah Whitfield,
  Mide Badmus, J Okonkwo, 7 + 13 students, 6 classes).
- Restoring a wiped test database to a known state.

## To apply (test only)

The Supabase CLI auto-applies any `.sql` in `supabase/migrations/` on
`db push`. This folder is excluded — apply seeds via direct psql/SQL
against the test project's session pooler URL.

Apply in filename order (timestamp-sorted). Seeds have internal
dependencies (`stage2_test_passwords` extends users created by
`stage2_test_seeds`, etc.) — out-of-order application will fail.

All seeds use `ON CONFLICT (id) DO NOTHING` with deterministic UUIDs,
so re-applying produces the same data without duplicates.

## Never

- Do **not** move seed files into `supabase/migrations/`. The CLI
  would auto-apply them on `db push` and create fake users in prod.
- Do **not** apply these to production. Headers in each file say
  `DO NOT APPLY ON: PRODUCTION` — believe them.
- Do **not** add a seed file here without `DO NOT APPLY ON: PRODUCTION`
  in its header. The header is the load-bearing safety mechanism.
