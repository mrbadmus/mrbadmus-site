# Baseline / bootstrap scripts

SQL to recreate a database from a known baseline state. Lives outside
`supabase/migrations/` so the Supabase CLI does **not** treat these
files as forward migrations to auto-apply on `db push`.

The CLI only reads `supabase/migrations/` — everything in this folder
is ignored by `supabase db push` and `supabase migration list`. Apply
baselines manually only.

## When to use

- Bootstrapping a fresh environment from scratch (new local dev DB,
  staging clone, disaster recovery).
- Reproducing the production baseline schema in a clean environment
  before the migration history is replayed on top.

## How to apply

Run manually via `psql` or the Supabase SQL Editor. Do **not** run via
`supabase db push`.

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f supabase/baselines/<file>.sql
```

After the baseline is applied, run `supabase db push` to apply the
forward migrations from `supabase/migrations/` on top.

## Never

- Do **not** move baseline files into `supabase/migrations/`. The CLI
  would interpret them as forward migrations and try to apply them
  alongside the real migration history — likely a `CREATE TABLE
  already exists` failure or worse.
