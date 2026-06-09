# Stage 3 — Schools Onboarding: SSO + CSV bulk import + account reconciliation

Branch: `schools/stage-3-onboarding`. Built + tested against the **TEST**
Supabase project (`qeppkiswvclkkwbxmlok`) only. Nothing in this stage has
touched production beyond a single read-only account audit.

---

## What this stage adds

1. **Provider-agnostic school SSO** — "Sign in with Microsoft" and "Sign in
   with Google" on `auth.html`, behind one shared handler. Everything after
   the returned email (domain allowlist, role resolution, account linking) is
   provider-neutral.
2. **CSV bulk import** — a 3-screen teacher wizard (`teacher/import.html`) +
   an idempotent, re-runnable reconciliation engine (the `roster-import` Edge
   Function).
3. **Account reconciliation (Branch B)** — a self-service "claim a previous
   account" flow so students who used a personal email before SSO can move
   their old progress onto their school account, verified by a single-use,
   time-limited email link, with idempotent + logged reparenting.
4. **Audit logging** — every CSV import, SSO login, and account merge writes
   to the existing Stage-1 `audit_log` table.

### Branch B was chosen from the prod audit

Read-only audit of the 42 production accounts (2026-05-30):

| Bucket | Count | % |
|---|---|---|
| Personal email (gmail/icloud/yahoo) | 24 | 57% |
| Rainford school domain | 14 | 33% |
| Other school domains (4 schools) | 4 | 10% |
| Blank / malformed | 0 | 0% |

57% on personal email is far below the 90%-school-domain threshold, so we
built the **full self-service claim/merge flow**, not just auto-link.
(Also noted for reconciliation: `last_name` is NULL on all 42 prod accounts —
the consumer site only ever collected first names — so imports will be
*adding* surnames, and casing/spelling drift in first names is common.)

---

## Files

**Migrations** (`supabase/migrations/`, applied to TEST, **need prod approval**):
- `20260530140000_stage3_sso_domain_hook.sql` — `school_id_for_email_domain()` + `hook_before_user_created()` + grants.
- `20260530140100_stage3_audit_writers.sql` — `write_audit_event()` (service_role) + `log_my_event()` (authenticated, whitelisted).
- `20260530140200_stage3_account_claims_merge.sql` — `account_claims` table + RLS + `reparent_student()` + `create_account_claim()` + `confirm_account_claim_and_reparent()`.
- `20260530140400_stage3_import_helpers.sql` — `user_id_for_email()`.
- (a tiny follow-up `REVOKE` on `school_id_for_email_domain` from anon/public was applied to TEST inline; it is folded into migration `…140000` for a clean prod apply.)

Rollback: `supabase/rollbacks/stage3_onboarding_rollback.sql` (manual only).

**Edge Functions** (`supabase/functions/`, deployed to TEST, **need prod deploy**):
- `roster-import` (verify_jwt) — the reconciliation engine.
- `account-claim-request` (verify_jwt) — mints token, emails the old address.
- `account-claim-confirm` (verify_jwt = false; the token is the proof) — reparents.

**Frontend**:
- `auth.html` — two SSO buttons + shared `signInWithSSO()` handler + `sso_login` audit on return.
- `teacher/import.html` — 3-screen CSV wizard (upload+preview → mapping+per-class settings → dry-run preview + single confirm). Loads papaparse.
- `student/settings.html` — "claim a previous account".
- `student/claim-confirm.html` — sessionless email-link landing page.
- `teacher/classes.html` — "Import students (CSV)" entry point.

**Sample CSVs** (`supabase/seeds/stage3_sample_roster_*.csv`) — clean + messy,
with non-obvious headers ("Email Address / Forename / Surname / Teaching
Group") to exercise the wizard's column auto-detection.

---

## How the identity model works (the important bit)

`profiles.id` is a hard FK to `auth.users.id`, and email lives only in
`auth.users`. So a `class_member` requires a real auth user. The importer
therefore **pre-provisions** each new student as a *confirmed* auth user via
the Admin API (no email is sent). On the student's first school SSO login,
their verified email matches the pre-provisioned account and Supabase **links
the OAuth identity automatically** — this is the "auto-link-on-first-login".

The **Before-User-Created hook** only ever fires for *genuinely new* user
creation. It:
- passes through `provider = email` (existing public email/password signup AND the Admin-API importer);
- for `azure`/`google`: rejects unknown email domains, and rejects on-domain users with no pre-assignment (strict), **except** a valid pending staff invitation.

Because rostered students already exist, they *link* (hook doesn't fire). Any
OAuth user that reaches the hook is by definition not pre-assigned → rejected.

---

## ⚠️ Mide-owned setup (must be done before SSO works for real students)

These are dashboard/registration steps — no secrets are in code.

1. **Microsoft Entra ID app registration** → put Client ID + Secret in
   Supabase Dashboard > Authentication > Providers > Azure. Redirect URI
   (Azure side, "Web"): `https://<project>.supabase.co/auth/v1/callback`.
2. **Google Cloud OAuth client** → Client ID + Secret in Supabase Dashboard >
   Authentication > Providers > Google. Same callback URL.
3. **Register the auth hook**: Dashboard > Authentication > Hooks > Before
   User Created → Postgres function → `public.hook_before_user_created`
   (or config.toml `[auth.hook.before_user_created]`,
   `uri = "pg-functions://postgres/public/hook_before_user_created"`).
   **Until registered, the domain/role gate is not enforced.** Conversely,
   **un-register it before running the rollback** or all sign-ups break.
4. **Confirm Supabase identity-linking** is enabled (link identities with the
   same verified email) so pre-provisioned students link on first SSO.
5. **Edge Function secrets** (Dashboard > Edge Functions > Secrets):
   `RESEND_API_KEY` (for the claim email; without it the claim is recorded but
   no email is sent), and optionally `CLAIM_SITE_URL` (defaults to
   `https://mrbadmus.com`).
6. **Privacy / DPA / DPIA** — the privacy notice, DPA addendum, and DPIA
   refresh for Microsoft/Google SSO are a **parallel Mide-owned track**. They
   are NOT a code dependency, but **must land before SSO ships to real
   students**.

---

## Prod deployment sequence (Mide's call — do NOT run from here)

1. Apply the 4 Stage-3 migrations to prod (in filename order) via the
   established CLI path (`supabase db push`) or MCP.
2. Deploy the 3 Edge Functions to prod (`roster-import`,
   `account-claim-request` with verify_jwt on; `account-claim-confirm` with
   verify_jwt off).
3. Set the OAuth providers + Edge secrets + register the hook (above).
4. `python3 generate_site_v5.py` then push frontend (Cloudflare).
   The new `teacher/import.html`, `student/settings.html`,
   `student/claim-confirm.html` are auto-copied (they live under `teacher/`
   and `student/`, which the generator copies wholesale).
5. Smoke test: one SSO login, one tiny CSV dry-run + real import, one claim.

---

## Test results (TEST DB, 2026-05-30) — all green

- **SSO hook** (unit, synthetic events): email-provider allowed; off-domain
  google → 403; on-domain-no-assignment azure → 403; missing email → 400;
  Rainford domain resolves case-insensitively.
- **roster-import** (end-to-end via deployed function, real teacher JWT) with
  a messy 9-row roster: dry-run wrote nothing (`auditId: null`); real run
  created 1 class, 2 students, 2 profile updates, 4 attaches, 5 skipped;
  **re-running the same file was a true no-op** (0 created, 0 attached, 4
  already-attached, 0 profile updates, no duplicate memberships). Messy rows
  correctly classified: missing/invalid email, in-file duplicate, unknown
  class, staff-email, name-mismatch.
  - Found + fixed a real bug during testing: a KS3 student imported into a KS4
    class violated `profiles_tier_only_ks4_check` (swallowed error, non-
    convergent count). Fix: the class governs key_stage, tier/pathway gated to
    KS4, single write path, write errors surfaced as row issues.
- **Merge engine** (SQL, synthetic loser+canonical with a deliberate class
  collision): reparented memberships (collision superseded, no duplicate
  active membership), moved submissions, merged XP (20+100→120, loser→0),
  carried tier/pathway, soft-deleted loser, consumed claim. **Idempotent**:
  re-confirm = `already_consumed`, re-reparent = all-zero no-op, XP stayed 120.
- **Audit**: `csv_import`, `account_claim_requested`, `account_merge_confirmed`,
  `sso_login` all logged with payloads. `log_my_event` rejects non-whitelisted
  actions.
- Test DB **restored to pristine seed state** after testing (34 profiles, 29
  active members, mutated seed students reverted, all test artifacts removed).

---

## Linear — Stage 3 tickets to create (under "Schools Layer Rollout", team MRB)

The Linear MCP needs a one-time OAuth authorization (still pending), so these
could not be created automatically. Ready to create:

- **MRB-S3-AUDIT** — Existing-account audit (prod, read-only). *Done* — 42
  accounts, 57% personal email → Branch B. Close on creation.
- **MRB-S3-SSO** — Provider-agnostic SSO (Microsoft + Google). **Blocked on**
  Mide's Entra app registration AND Google Cloud OAuth client registration.
  Note: privacy notice / DPA addendum / DPIA refresh is a parallel Mide-owned
  track, not a code dependency, but must land before SSO ships to students.
- **MRB-S3-CSV-SCHEMA** — Import schema helpers (`user_id_for_email`, audit
  writers). Done (TEST), needs prod migration approval.
- **MRB-S3-CSV-ENGINE** — Idempotent reconciliation engine (`roster-import`).
  Done + tested (TEST), needs prod deploy.
- **MRB-S3-CSV-FRONTEND** — 3-screen import wizard + classes entry point.
  Done (TEST/source), needs generator run + frontend deploy.
- **MRB-S3-MERGE** — Account claim + reparent (`account_claims`,
  `reparent_student`, claim Edge Functions, student settings + claim-confirm).
  Done + tested (TEST), needs prod migration + deploy.
- **MRB-S3-AUDIT-LOG** — Audit logging for imports / SSO logins / merges.
  Done + tested (TEST).

---

## Deferred / follow-ups (not blockers)

- Teacher autocomplete in the importer only lists staff the caller can see via
  RLS (a plain teacher sees themselves; admins see all). A broader staff-list
  RPC could be added later.
- `weekly_scores` does not exist in TEST; `reparent_student` has a guarded,
  column-auto-detecting block for it so the same function is correct on prod
  (where it exists). Confirm the prod `weekly_scores` owner column before the
  first prod merge.
- Brand drift (pre-existing, NOT touched here): `auth.html` still uses the
  retired `⚗️` alembic in its nav/logo. Flag for the brand-drift ticket; do
  not propagate.
- The org-scoped Supabase MCP was used (pinned to the TEST ref) for this run
  because the `remove`+`add` etiquette dance wiped the `supabase-test` MCP's
  OAuth token. Re-authorize `supabase-test` via `/mcp` to restore the
  test-pinned safeguard.
