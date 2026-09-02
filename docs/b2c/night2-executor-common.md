# Night 2 — common brief for every executor (read fully before starting)

## Where things are
- Frontend worktree: `/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/launch` (branch `b2c/launch`)
- Backend worktree:  `/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/backend` (branch `b2c/launch`), `.env` already carries: SUPABASE_URL (the TEST project), SUPABASE_SERVICE_ROLE_KEY, SUPABASE_ANON_KEY, CONSUMER_SIGNUP_ENABLED=true, STRIPE_SECRET_KEY (Stripe **test** mode), CONSUMER_CRON_SECRET, FRONTEND_ORIGIN, PORT=3100.
  Absent on purpose: ANTHROPIC_API_KEY, RESEND_API_KEY, UPSTASH_*. Every module must run correctly without them (stub / dry-run adapters) and say so on `/api/health`.
- The contract: `docs/b2c/night2-api.md` in the frontend worktree. Build to it exactly; if you must deviate, write the deviation in your report.
- Schema: all nine Night 2 migrations are APPLIED on the TEST project. Read the SQL in `supabase/migrations/20260902000100_*.sql` … `20260902000900_*.sql` for the exact columns, functions and policies. Do not write migrations; if you need a schema change, STOP that piece and report what you need — the commander applies migrations.

## Hard rules
1. **TEST project only** (`qeppkiswvclkkwbxmlok`). Never production. Never `git commit`, never `git push`.
2. **Zero residue.** Every fixture you create (auth users, families, children, messages, answers, Stripe customers) you delete when you are done. Keep a list of ids as you go. The night ends with `select count(*) from schools where kind <> 'school'` = 0.
3. **server.js is shared by five executors at once.** Edit it ONLY with the `Edit` tool (exact-string replace), never `Write`, and only in the spots your brief names. Re-read the lines you are about to change immediately before each edit. Keep those edits tiny; everything else goes in your own `consumer/<module>.js`.
4. **Run your own backend instance on your own port** for testing: `PORT=31xx node server.js` from the backend worktree (E1: 3101, E2: 3102, E3: 3103, E4: 3104, frontend E5: 3105). Never assume 3100 is yours. Kill your instance when done.
5. Modules: `module.exports = function (app, ctx) { …register routes…; return { …functions other modules may call… }; }`. `ctx` carries: `supabase` (service role), `createClient`, `getUser`, `getUserWithProfile`, `callerClient(req)` (RLS-bound client as the caller), `consumerGate`, `requireParent`, `requireGuardian` (`:id` = child), `requireChild`, `requireConsumerUser`, `requireOperator`, `requireWritable`, `orgAccess(orgId)`, `invalidateAccess(orgId)`, `rateLimit`, `UUID_RE`, `ANTHROPIC_MODEL`, `compose` (assignment-compose.js), `schemeLessons`, `bankFor`, `currentTeachingWeek`, `STRIPE_WEBHOOK_PATH`, and — after mounting — `ctx.limits`, `ctx.email`, `ctx.notify`, `ctx.stripe`, `ctx.work`, `ctx.chat`, `ctx.checks`, `ctx.report`, `ctx.marking` (mounted in that order; a module may call an earlier one at request time, and a later one lazily via `ctx.<name>` inside handlers, never at mount time).
6. Every consumer route: `consumerGate` first, then the identity gate, then `requireWritable` on anything that submits/sends/marks/generates. Errors as JSON `{ error, message }` with the codes in the contract.
7. Style: plain CommonJS, no new dependencies beyond `stripe` (already installed) unless your brief allows it; comments explain WHY like the rest of server.js.
8. Report at the end: what you built (routes, functions), what you drove and the results (exact requests and responses), anything unverified, deviations, and the fixture ids you deleted. Do not say "done" for anything you did not run.

## Making test users (the only way — hand-inserted auth rows cannot sign in)
```js
const { createClient } = require('@supabase/supabase-js');
const admin = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY);
const { data } = await admin.auth.admin.createUser({ email: 'n2-e1-parent@example.com', password: 'Passw0rd!x', email_confirm: true, user_metadata: { first_name: 'Funmi' } });
// sign in as that parent to get a JWT:
const anon = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_ANON_KEY);
const { data: s } = await anon.auth.signInWithPassword({ email, password });
const jwt = s.session.access_token;
// then POST /api/consumer/family/ensure with Authorization: Bearer <jwt> → org_id
// then POST /api/consumer/children { first_name, year_group, username, password, mode, intensity, exam_board } → child_id
// child JWT: POST /api/consumer/child/login { username, password }
```
Cleanup: `DELETE /api/consumer/children/:id` for each child, then `admin.auth.admin.deleteUser(id)` for children and parent; then delete the family: `delete from staff_scopes where school_id=…; delete from subscriptions where org_id=…; delete from academic_years where school_id=…; delete from schools where id=…` (and any rows in tonight's tables for that org first). Use `mcp__supabase-test__execute_sql` for SQL (load with ToolSearch "select:mcp__supabase-test__execute_sql").

## The one thing that will bite you
The Night 1 `DELETE /children/:id` soft-deletes via `parent_remove_child`; the auth user remains. Delete auth users explicitly. `profiles.id` FKs onto `auth.users` with no cascade — delete the profile's dependent rows (class_members, class_teachers, tonight's tables) before the auth user, or the delete 500s.
