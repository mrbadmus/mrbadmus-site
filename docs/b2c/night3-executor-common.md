# Night 3 — common brief for every executor (read fully before starting)

MRB-317 (consumer UI) and MRB-318 (organisation variant). Design authored;
you compile. Her copy, structure, states and data shapes are the spec. You
transcribe them onto the Night 1–2 plumbing and replace every mock constant
with a real call.

## Where things are
- Frontend worktree: `/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/launch` (branch `b2c/launch`). Use absolute paths; never `cd` into another checkout.
- Backend worktree: `/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/b2c/backend` (branch `b2c/launch`). `.env` is the TEST project, `CONSUMER_SIGNUP_ENABLED=true`, Stripe TEST key, `PORT=3100`. Absent on purpose: `ANTHROPIC_API_KEY`, `RESEND_API_KEY`, `UPSTASH_*` — everything runs with the stub / dry-run adapters.
- Design's delivery: `docs/b2c/design/drop1/B2C consumer front door design/*.dc.html` + `MANIFEST.md`. There is NO drop2 — drop1 holds all nineteen surfaces from her three drops. **Compare by the JS constants and `renderVals()` in the `<script type="text/x-dc">` block, never by the HTML** — she renders interactive elements from `{{ holes }}`, `<sc-if>`, `<sc-for>`.
- The shipped API: `backend/API-CONTRACT.md` §v3.4 + §v3.5 (lines 834–2230) PLUS tonight's additions in `docs/b2c/night3-api.md`. Where the contract and her shape differ, the contract's extra fields are fine; where her shape needs something the contract lacks, `night3-api.md` names the addition — build to it. If you find a gap neither covers, STOP that one field, fake nothing, and report it.
- Existing scaffold pages under `consumer/` (Night 1–2) are FUNCTIONAL references for the plumbing — session, `boot()`, `api()`, `guard()`, realtime — not for the look. Read `consumer/consumer-common.js` fully before writing a page.

## Hard rules
1. **TEST project only** (`qeppkiswvclkkwbxmlok`). Never production. **Never `git commit`, never `git push`.** The commander commits.
2. **Zero residue.** Delete every fixture you create (auth users, families, children, orgs, messages, answers, Stripe customers). Keep a list of ids as you go.
3. **Shared files** — `consumer/consumer-common.js`, `consumer/consumer.css`, `shared/config.js`, backend `server.js`, `consumer/index.js` — are edited ONLY with the `Edit` tool (exact-string replace), never `Write`, and only with small additions in a clearly-commented block that names your lane. Re-read the lines immediately before each edit. Everything else goes in files your brief names as yours.
4. **Run your own backend on your own port** for testing: `PORT=31xx node server.js` from the backend worktree (backend executor 3106; frontend executors 3107 public, 3108 dashboard, 3109 child, 3110 org/admin). Serve the frontend with `python3 -m http.server 8xxx` from the frontend worktree ROOT (so `/shared/…` and `/consumer/…` resolve) and open pages with `?env=test&api=http://localhost:31xx`. Kill both when done. Do not run `build_all.py` — the commander does, once, at the end.
5. **Everything stays behind `CONSUMER_SIGNUP_ENABLED`.** Every page you write starts `display:none`, calls `MrBadmusConsumer.boot()`, and with the flag off renders "Not found" with ZERO network requests (no Supabase SDK, no fetch, no fonts beyond the stylesheet). Public pages too. Public pages additionally carry `<meta name="robots" content="noindex">` statically, which `boot()` removes when enabled (see the `boot` addition in night3-api.md §F).
6. **Brand.** Chevron + "MrBadmus" on every consumer and public surface (parent, child, public, signup). Plain "MrBadmus" wordmark, NO chevron, on staff and admin surfaces (Org Sign In, Org Dashboard, Admin Accounts, Admin Marking Queue — Mide's ruling 1 on MRB-316 overriding Design's drawing). **No "AI" in any wordmark anywhere.** Nothing student-facing carries meta-text about the platform.
7. **Design system: reuse what the site already serves.** Every consumer page loads, in this order:
   ```html
   <link rel="stylesheet" href="/shared/tokens.css"/>
   <link rel="stylesheet" href="/shared/ks3.css"/>
   <link rel="stylesheet" href="/consumer/consumer.css"/>
   ```
   and puts `class="rd" data-mode="ks3"` on the page root `<div>` exactly as her files do. Design's `_ds/tokens/shared-tokens.css` and `shared-ks3.css` are byte-identical to the repo's `shared/tokens.css` and `shared/ks3.css` apart from font URL prefixes (verified with `cmp`); `_ds_bundle.css` contains zero rules any of her surfaces use; the only component she imports is `MrBadmusDS.BrandMark`, whose SVG is already in `MrBadmusConsumer.BRANDMARK`. So nothing from `_ds/` is vendored. Fonts come from `/shared/fonts/` via tokens.css; preload Bricolage + Instrument Sans as `consumer/today.html` already does. The admin dark-room tokens (`--st-room`, `--st-room-panel`, `--st-room-text`, `--st-ember`, …) live in Design's `_ds/tokens/src-styles-tokens.css` (the 3D-studio file, not in shared/) — the admin executor copies ONLY the `--st-*` values the two admin surfaces use into the admin page's own `<style>`.
   Her per-element inline styles are the design: transcribe them faithfully. Lift repeated ones into a per-page `<style>` with page-prefixed classes (she already uses `pb-`, `dk-`, `su-`, `og-`, `rpt-`); keep her breakpoints (900 for public nav, 960 for parent desktop, 760 for the sign-in cards; child surfaces and the report single-column at any width). Ticks/crosses/arrows are inline SVG (`.ks3-mark`), never typed characters.
8. **No mock data survives.** Every `const` in her file becomes a real read. Copy strings, empty states and validation strings are hers verbatim, except the three rulings and the corrections listed in your brief. If a field has no source, it is NOT rendered with a placeholder — it is omitted and reported.
9. **MRB-278 gate applies to any question rendering**: options render in the order the server sent them; never re-sort so the right answer sits first; `verify_answer_positions.py` is the commander's gate.
10. **Every failure a human can read.** No status codes, no stacks, no blank panels. `MrBadmusConsumer.fail/section` already do this — use them.
11. Style: plain HTML + vanilla JS (no frameworks, no build step), CommonJS on the backend, comments that explain WHY.
12. **Report at the end**: what you built (files, routes), what you drove and the exact results, anything unverified, deviations from Design and why, fixture ids deleted. Never say "done" for something you did not run.

## Paths (chosen tonight — use these exactly)
| surface | path |
|---|---|
| Public Home | `/parents/index.html` |
| Public How It Works | `/parents/how-it-works.html` |
| Public Pricing | `/parents/pricing.html` |
| Public Home Education | `/parents/home-education.html` |
| Public Sign In (chooser + parent form) | `/parents/sign-in.html` |
| Public Organisations | **not delivered by Design — skipped** (Sign In's "organisation sign in" link goes to `/org/sign-in.html`) |
| Parent Signup (account → verify → child → unit → children → plan → Stripe → return) | `/consumer/signup.html` (verify landing `/consumer/verify.html`, Stripe return `/consumer/checkout-return.html`) |
| Parent Dashboard (overview / child / set work / chat / answers / manage) | `/consumer/overview.html` (`?child=<id>&view=…`) |
| Parent Account | `/consumer/account.html` |
| Termly Report | `/consumer/report.html?child=<id>&term=<key>` |
| Child Login | `/go/index.html` — the URL a child types is **mrbadmus.com/go** |
| Child Today (+ chat) | `/consumer/today.html` |
| Child Exam Questions | `/consumer/exam.html` |
| Child Unit Check | `/consumer/unit-check.html?unit=<code>` |
| Org Sign In | `/org/sign-in.html` |
| Org Dashboard | `/org/index.html` |
| Admin Accounts + Marking Queue | inside `/teacher/admin.html` (the consumer card), flag-gated |

Retired scaffolds (delete them in your lane): `consumer/add-child.html`, `consumer/child.html`, `consumer/child-login.html`. `generate_site_v5.py` already copies `parents/`, `go/`, `org/`.

## Making test users (the only way — hand-inserted auth rows cannot sign in)
```js
const { createClient } = require('@supabase/supabase-js');
const admin = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY);
const { data } = await admin.auth.admin.createUser({ email: 'n3-<lane>-parent@example.com', password: 'Passw0rd!x', email_confirm: true, user_metadata: { first_name: 'Funmi' } });
const anon = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_ANON_KEY);
const { data: s } = await anon.auth.signInWithPassword({ email, password });   // s.session.access_token
// POST /api/consumer/family/ensure → org_id; POST /api/consumer/children → child_id; POST /api/consumer/child/login → child JWT
```
Billing states for a page drive are set by SQL on `subscriptions` (`status`, `trial_end`, `current_period_end`, `locked_at`, `retry_at`, `last_payment_failed_at`, `canceled_at`) — the Night 2 drive `backend/scripts/night2-drive.js` shows every transition. To put a REAL session into headless Chrome, sign in with the Supabase JS SDK on the page itself (the `ks3_browser.py` CDP harness can `eval` that), or write the session JSON to `localStorage['sb-qeppkiswvclkkwbxmlok-auth-token']` — it must be a real session, the SDK deletes a fake one.
Cleanup order: `DELETE /api/consumer/children/:id` each child → `admin.auth.admin.deleteUser` for children and parent (delete `profiles` dependants first; `profiles.id` FKs onto `auth.users` with no cascade) → rows in tonight's tables for the org → `staff_scopes`, `subscriptions`, `academic_years`, `classes`, `schools`.

⊕ **6 Sep 2026 (MRB-327) — the dependants, named.** The paragraph above says
"delete `profiles` dependants first" and then names none of them, so every lane
rediscovers the list one `23503` at a time. There are **43 foreign keys onto
`profiles(id)` and 26 onto `schools(id)` that are not `ON DELETE CASCADE`**. The
ones that actually bite a consumer fixture, in the order they bite:

```sql
-- with o = the org id and p = the profile id
delete from public.email_log              where org_id = o or recipient_id = p;
delete from public.consumer_notifications where org_id = o or recipient_id = p;
delete from public.parent_prefs           where profile_id = p;
delete from public.ai_usage_events        where org_id = o or profile_id = p;
-- ⚠️ The work generator writes a REAL assignment per practice item, so these
-- four come before work_items and before classes. Found by the MRB-327
-- marketing lane, whose teardown tripped on them.
delete from public.assignment_question_attempts where submission_id in
  (select id from public.assignment_submissions where student_id = p);
delete from public.assignment_submissions where student_id = p;
delete from public.assignment_questions   where assignment_id in
  (select id from public.assignments where class_id in
     (select id from public.classes where school_id = o));
delete from public.assignments            where class_id in
  (select id from public.classes where school_id = o);
delete from public.work_items             where org_id = o or child_id = p or removed_by = p;
delete from public.work_generation_runs   where child_id = p;
delete from public.child_plans            where org_id = o or child_id = p or paused_by = p;
delete from public.family_messages        where org_id = o or sender_id = p or recipient_id = p;
delete from public.exam_answers           where org_id = o or child_id = p or mb_marked_by = p;
delete from public.unit_check_attempts    where org_id = o or child_id = p;
delete from public.child_flashcard_queue  where org_id = o or child_id = p;
delete from public.report_notes           where child_id = p or written_by = p;
delete from public.org_limits             where org_id = o or updated_by = p;
delete from public.stripe_events          where org_id = o;
delete from public.subscriptions          where org_id = o;
delete from public.class_members          where student_id = p;
delete from public.class_teachers         where teacher_id = p;
delete from public.classes                where school_id = o;
delete from public.staff_scopes           where school_id = o or granted_by = p;
delete from public.academic_years         where school_id = o;
delete from public.audit_log              where school_id = o or actor_id = p;
delete from public.account_deletion_requests where org_id = o;
delete from public.profiles               where id = p;   -- only now
delete from public.schools                where id = o;   -- and only then
-- and last, over the auth Admin API, the auth.users row
```

⚠️ **`audit_log` is the one that surprises people.** `POST /api/consumer/family/ensure`
writes an `audit_log` row with `actor_id` = the parent, so the very first call of
every drive plants a blocker on the very last step of its teardown.

⚠️ Run the whole thing as ONE statement (a `do $$ … $$` block). The MCP runs a
query as a single transaction, so if any one delete fails the entire batch rolls
back and the earlier deletes you thought had succeeded did not.

⚠️ `class_shoutouts` and `submission_feedback` are `RESTRICT`, not `NO ACTION` —
they will refuse rather than defer. A consumer fixture should never write either;
if teardown trips on one, something has crossed into the school layer. SQL via `mcp__supabase-test__execute_sql` (ToolSearch `select:mcp__supabase-test__execute_sql`). If the Bash permission layer refuses an authenticated write from your script, say so in the report and the commander will run it.

## Traps already found (do not rediscover them)
- Two `postgres_changes` bindings on one channel deliver nothing; `subscribeMessages()` in consumer-common.js is the one correct binding — use it.
- `requireWritable` on guardian routes is `writableHere` (order actor → parent → child); the 423 body is the same.
- On the family payload BOTH `billing.state` and `billing.access` exist and only `access` is the permission — `guard()` reads `access` first.
- A 404 with no body on `/api/consumer/*` is the flag being off, not a missing route.
- `mins` on Today items is a STRING. `profiles.year_group` is TEXT; coerce before comparing.
- In zsh a word beginning with `=` (e.g. `echo ====`) expands `=cmd` and kills the chain.
- The weekly cron and `sendDigests` sweep every consumer org on the TEST project — do not fire `/cron/weekly` while another lane is driving.
