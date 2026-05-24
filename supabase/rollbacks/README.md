# Rollback scripts

Manual SQL to undo a specific forward migration. Lives outside
`supabase/migrations/` so the Supabase CLI does **not** treat these
files as forward migrations to auto-apply on `db push`.

The CLI only reads `supabase/migrations/` — everything in this folder is
ignored by `supabase db push` and `supabase migration list`. Apply
rollbacks manually only.

## Naming

Rollback files keep the original sequence prefix of the forward
migration they undo (e.g. `0001_schools_layer_rollback.sql` undoes the
migration that was originally named `0001_schools_layer.sql`, now
renamed to `20260501212106_schools_layer.sql` after MRB-84).

These files are not parsed by the CLI, so timestamp prefixes are
unnecessary. The sequence prefix is for human pairing only.

## To roll back a migration

1. Read the rollback SQL and confirm it's the right one for what
   you're undoing — check the header comment.
2. Apply it manually via `psql` or the Supabase SQL Editor against the
   target DB.
3. After the SQL succeeds, delete the corresponding row from the
   registry so the CLI no longer considers it applied:
   ```sql
   DELETE FROM supabase_migrations.schema_migrations
     WHERE version = 'YYYYMMDDHHMMSS';
   ```
4. Verify with `supabase migration list` that the row is gone.

## Never

- Do **not** move rollback files into `supabase/migrations/`. The CLI
  would interpret them as forward migrations and apply them on the next
  `db push`, dropping tables.
- Do **not** run rollbacks against production without a confirmed
  backup and a tested recovery plan.
