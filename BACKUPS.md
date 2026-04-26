# Backups

This document describes how the MrBadmusAI database is backed up, where backups are stored, and how to restore from one.

**Status: live as of 26 April 2026.**

---

## What's backed up

The entire Supabase PostgreSQL database, daily, as a plain SQL dump compressed with gzip. This includes:

- All application tables (students, profiles, leaderboard scores, weekly quiz results, etc.)
- The `auth` schema — Supabase user accounts, hashed passwords, sessions
- All schemas, tables, indexes, functions, triggers, and row-level security policies

Format: `backup-YYYY-MM-DD.sql.gz` — for example, `backup-2026-04-26.sql.gz`.

---

## What's NOT backed up

**Supabase Storage files (avatars).** The `avatars` bucket contains user-uploaded profile pictures. These are stored as files in Supabase Storage, not as rows in the database, and are NOT covered by this workflow.

If avatars are critical to recover, they would need to be re-uploaded by users, OR a separate storage backup workflow would need to be built. Track this as Lane 4 follow-up work.

**Render environment variables.** The Resend API key, Supabase service role key, and other backend secrets live in Render's environment settings. They are not backed up — but they're recoverable from the source services (Supabase dashboard, Resend dashboard) and from Mide's notes app.

**The frontend codebase.** That's what GitHub itself is for — the `mrbadmus-site` repo IS the backup of the frontend.

---

## Where backups live

| Setting | Value |
|---|---|
| Storage provider | Cloudflare R2 |
| Bucket name | `mrbadmus-supabase-backups` |
| Region | Auto (Cloudflare's global edge) |
| Access | Account-scoped API token (read+write) stored in GitHub Secrets |

R2 was chosen over AWS S3 because it has zero egress fees — restores are free, and the 10GB free tier covers years of daily backups for a database this size.

---

## Schedule and retention

| Setting | Value |
|---|---|
| Schedule | Every day at 03:00 UTC |
| In UK time | 03:00 GMT (winter) / 04:00 BST (summer) |
| Retention | 30 days. Backups older than 30 days are auto-deleted by the same workflow. |
| Manual triggers | Always allowed via the GitHub Actions tab |

---

## Failure notifications

If a backup workflow run fails, GitHub automatically emails `aayobadmus@gmail.com` with a link to the failed run. Subject line will look like:

> `[mrbadmus/mrbadmus-site] Run failed: Daily Supabase Backup - main`

**When you receive a failure email, do this:**

1. Click the link in the email — it opens the run logs on GitHub
2. Find the step marked with a red X — that's the one that failed
3. Click to expand the logs for that step
4. The error message is at the bottom of the expanded log
5. Cross-reference against the **Troubleshooting** section below

Don't ignore failure emails. A workflow failing silently means you have no recent backup, and that's the worst possible state to discover during a real incident.

---

## How to verify a backup is working

Three ways, in increasing thoroughness:

### Quick check (5 seconds) — was today's run green?

1. Go to: `https://github.com/mrbadmus/mrbadmus-site/actions`
2. Look at the most recent "Daily Supabase Backup" run
3. Green tick = success, red X = failure

### Medium check (30 seconds) — is today's file actually in R2?

1. Log into Cloudflare → R2 → `mrbadmus-supabase-backups` bucket
2. Look for `backup-YYYY-MM-DD.sql.gz` matching today (or yesterday, if before 03:00 UTC)
3. Confirm the file size looks reasonable (at least a few MB; should not be empty)

### Full check (5 minutes) — does the backup actually restore?

This is the only check that proves the backup is genuinely usable. Do this **at least once per quarter** and **always before relying on a backup in a real recovery scenario**. See "How to restore from a backup" below — restore to a local PostgreSQL database, NOT production.

---

## How to manually trigger a backup

Useful for testing changes to the workflow, or for taking a snapshot before a risky migration.

1. Go to: `https://github.com/mrbadmus/mrbadmus-site/actions`
2. In the left sidebar, click "Daily Supabase Backup"
3. On the right, click the "Run workflow" dropdown
4. Leave branch as `main`, click the green "Run workflow" button
5. Wait ~2 minutes — refresh the page to see progress
6. Green tick = success. Verify the new file appears in R2.

---

## How to restore from a backup

**⚠️ Restoring is destructive. Read this whole section before running anything.**

### Before you start

- Decide WHERE you're restoring TO. **Almost never** restore directly to production. Restore to a fresh local database first, verify the data, then plan the production cutover.
- Have the backup file already downloaded to your local machine.
- Have `psql` and `gunzip` available (`brew install postgresql` on Mac if not).

### Step 1 — Download the backup from R2

Easiest way: log into the Cloudflare dashboard → R2 → `mrbadmus-supabase-backups` → click the file you want → click "Download".

Save it to a known location, e.g. `~/Downloads/backup-2026-04-26.sql.gz`.

### Step 2 — Decompress it

\`\`\`bash
cd ~/Downloads
gunzip backup-2026-04-26.sql.gz
\`\`\`

You'll now have `backup-2026-04-26.sql` (no `.gz`). Inspect it with `head` or `less` to confirm it looks like SQL:

\`\`\`bash
head -50 backup-2026-04-26.sql
\`\`\`

You should see lines like `CREATE TABLE`, `INSERT INTO`, etc.

### Step 3 — Restore into a fresh local database

\`\`\`bash
# Create a clean local database
createdb mrbadmus_restore_test

# Load the backup into it
psql mrbadmus_restore_test < backup-2026-04-26.sql
\`\`\`

This will print a lot of output. Errors about extensions or roles not existing are usually safe to ignore (they happen because Supabase has things your local Postgres doesn't). What matters is whether the data lands.

### Step 4 — Verify the data

\`\`\`bash
psql mrbadmus_restore_test
\`\`\`

Then in the psql prompt, run:

\`\`\`sql
\dt                                    -- list all tables
SELECT count(*) FROM auth.users;       -- count user accounts
SELECT count(*) FROM public.profiles;  -- count profiles
\q                                     -- quit
\`\`\`

If the counts look right, the backup is good.

### Step 5 — Restore to production (only if absolutely necessary)

This is rarely the right move. Usually a real recovery means:
- Identify the specific tables/rows that were lost
- Pull just those rows from the local restore
- INSERT them back into production manually

Full production restoration would wipe ALL current data and replace it with the backup snapshot. **Only consider this if production is fully corrupted and you've consulted Supabase support first.**

The Supabase project has a built-in "Point in time restore" feature on paid plans which is preferable to a destructive `psql` restore.

---

## How to rotate the credentials

Do this whenever:
- A credential leaks (e.g. accidentally committed to git, sent in a chat)
- A staff member with access leaves
- It's been more than 12 months since the last rotation (good hygiene)

### To rotate \`SUPABASE_DB_URL\`

1. Supabase dashboard → Project settings → Database → Reset database password
2. Copy the new connection string
3. GitHub repo → Settings → Secrets → click \`SUPABASE_DB_URL\` → Update secret
4. Manually trigger the backup workflow to confirm the new credential works

### To rotate the R2 credentials

1. Cloudflare dashboard → R2 → Manage R2 API Tokens → Roll the token
2. Save the new Access Key ID and Secret Access Key
3. Update both \`R2_ACCESS_KEY_ID\` and \`R2_SECRET_ACCESS_KEY\` in GitHub Secrets
4. Manually trigger the backup workflow to confirm

The \`R2_ACCOUNT_ID\` and \`R2_ENDPOINT_URL\` don't usually change — only update those if Cloudflare migrates the account.

---

## Troubleshooting

### "pg_dump: error: connection failed"
The Supabase database is unreachable. Possible causes:
- Database password rotated and \`SUPABASE_DB_URL\` not updated → rotate the secret
- Supabase project paused → log into Supabase, unpause
- Supabase having an outage → check status.supabase.com

### "An error occurred (InvalidAccessKeyId)"
R2 credentials are wrong. Either:
- The R2 token was rolled and \`R2_ACCESS_KEY_ID\` / \`R2_SECRET_ACCESS_KEY\` weren't updated → rotate them
- Typo in the secret values → re-paste them carefully

### "Could not connect to endpoint URL"
\`R2_ENDPOINT_URL\` is malformed. Should look like \`https://[account-id].r2.cloudflarestorage.com\`. No trailing slash, no bucket name in the URL.

### Workflow runs but file size is suspiciously small (<1 MB)
The dump may be incomplete. Check the run logs for warnings during the \`pg_dump\` step. Don't trust a sudden 10x size drop — investigate before relying on it.

### "permission denied for schema X"
The connection string is using the wrong role. The \`SUPABASE_DB_URL\` should use the \`postgres\` user (the project owner), not \`anon\` or \`authenticated\`. Verify in Supabase → Project settings → Database → Connection string.

---

## Workflow file location

The workflow itself lives at \`.github/workflows/backup.yml\` in this repo. Edit there if you need to adjust the schedule, retention, or steps. Always test changes by manually triggering a run before relying on the schedule.

---

*Last updated: 26 April 2026 by Mide. Update this date whenever you change the workflow or the procedures.*
