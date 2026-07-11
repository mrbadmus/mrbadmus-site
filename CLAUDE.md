# CLAUDE.md — MrBadmusAI Frontend Project Guide

This file gives Claude Code (the AI assistant) everything it needs to understand this project and work on it effectively.

---

## What is MrBadmusAI?

MrBadmusAI is a free GCSE Science revision website for UK secondary school students. It covers all three AQA sciences — Physics (spec 8463), Chemistry (spec 8462), and Biology (spec 8461) — at both Foundation and Higher tier, across Combined Science and Triple Science pathways.

The site features:
- Topic notes and subtopic pages for every AQA spec point
- A live AI tutor chat (powered by Claude via a backend API)
- A weekly challenge system with a leaderboard (Champion of the Week + per-track leaderboards)
- Past paper links
- User accounts (sign up / sign in) with personalised profiles

The name "MrBadmus" refers to Mide Badmus, the teacher who built this site for his students. Over 135 students actively use it.

---

## Tech Stack

| What | How |
|---|---|
| **Frontend** | Plain HTML, CSS, and vanilla JavaScript — no React, no framework |
| **Styling** | A single shared stylesheet: `shared/styles.css` |
| **AI chat engine** | `shared/mrbadmus.v2.js` — one JavaScript file shared across all pages |
| **AI model** | Claude (Anthropic) — accessed via a custom backend |
| **Backend API** | Separate Node/Express server at `https://mrbadmus-backend.onrender.com` — lives in a separate repo |
| **Auth & database** | Supabase — handles user sign-in, session tokens, profiles, and leaderboard data (project ID `urklkrwevjtlfbwnipjn`) |
| **Site generation** | A Python script (`generate_site_v5.py`) that builds all topic HTML pages from structured data |
| **Hosting** | Cloudflare Pages at mrbadmus.com (auto-deploys from GitHub) |
| **Email** | Resend.com from noreply@mrbadmus.com |

---

## Brand presentation rule

The site has TWO brand presentations. Always check which applies before adding nav markup to a new page.

**Why:** External pages need a visible brand for prospective students, parents, and schools (first impression, marketing). Dashboards stay clean and utilitarian — they're for authenticated users in a working context, no marketing surface needed.

| Surface | Brand markup |
|---|---|
| **External / public pages** | Orange chevron SVG **+** "MrBadmusAI" text. Uses `nav-brand` + `brand-logo` classes from `shared/styles.css`. Applies to: `index.html`, `auth.html`, `combined/index.html`, `triple/index.html`, all generator-output topic pages, and any future external/public page. |
| **Dashboards / school-operations pages** | Plain white text "MrBadmusAI", **no logo asset**, with the exact styling pinned below. Applies to: all `/teacher/*` pages, and all current/future student / HoD / SLT / admin dashboards. |

### Canonical external chevron markup

Copy this verbatim into the nav of any external page:

```html
<a class="nav-brand" href="/index.html"><svg class="brand-logo" width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M4 6l4-4 4 4" stroke="url(#navGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M4 6l4-4 4 4" stroke="url(#navGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" transform="translate(4,6)"/><defs><linearGradient id="navGrad" x1="4" y1="2" x2="16" y2="12" gradientUnits="userSpaceOnUse"><stop stop-color="#FFD93D"/><stop offset="1" stop-color="#FF6B35"/></linearGradient></defs></svg> MrBadmusAI</a>
```

Requires `shared/styles.css` to be loaded (for `.nav-brand` + `.brand-logo`).

### Canonical dashboard text markup

Copy this verbatim into the nav of any dashboard page:

```html
<a href="/index.html" style="font-family:'Sora',sans-serif;font-weight:700;font-size:1.2rem;color:var(--text);text-decoration:none;letter-spacing:0.01em;">MrBadmusAI</a>
```

No stylesheet dependency — fully inline-styled. This is the canonical dashboard brand styling — match it exactly on every new dashboard page.

### ⚠️ Retired placeholders — never use on a new page

- The green octopus logo (obsolete)
- The alembic emoji `⚗️` (quick stand-in, fully retired)

If you find either on a page, that's brand drift — flag it, don't propagate it.

---

## Key Files and Folders

```
mrbadmus-site/
│
├── index.html              — Homepage (shows landing leaderboard with Champion of the Week)
├── auth.html               — Sign in / sign up page
├── profile-setup.html      — User profile wizard (collects science_pathway + tier)
├── weekly-challenge.html   — Weekly quiz challenge (subject picker only, pathway+tier from profile)
├── leaderboard.html        — Student leaderboard (Champion + 12 per-track views)
├── my-challenges.html      — Student's personal challenge history
├── past-papers.html        — Links to AQA past papers
│
├── shared/
│   ├── styles.css          — All site-wide CSS styles
│   └── mrbadmus.v2.js      — Core AI chat engine (shared by every page, SINGLE SOURCE OF TRUTH)
│
├── biology/                — Biology topic pages (auto-generated)
├── chemistry/              — Chemistry topic pages (auto-generated)
├── physics/                — Physics topic pages (auto-generated)
├── triple/                 — Triple Science pages (auto-generated)
├── combined/               — Combined Science pages (auto-generated)
│
├── generate_site_v5.py     — Python script that generates all topic pages AND copies files into mrbadmus_site/
├── all_subtopics_*.py      — Python files defining subtopic content per subject/tier
│
└── mrbadmus_site/          — OUTPUT FOLDER. Cloudflare Pages serves from HERE, not from the repo root.
                               Never edit files in here directly — they get overwritten by the generator.
```

⚠️ **Critical file location rule:** Cloudflare Pages serves the site from `mrbadmus_site/`, not from the repo root. The generator copies root-level HTML files into `mrbadmus_site/` automatically. Always edit root-level files, then run the generator.

---

## The Weekly Challenge System (v3.0 — 12-track)

The quiz is split across **12 tracks**: 3 subjects × 2 pathways × 2 tiers.

- Subjects: Biology, Chemistry, Physics
- Pathways: Combined, Triple
- Tiers: Foundation, Higher

**How a student takes the quiz:**
1. They must be registered with `science_pathway` AND `tier` set in their profile
2. On weekly-challenge.html they pick ONLY the subject — pathway and tier come from their profile silently
3. Backend returns the correct quiz for their (subject, pathway, tier) combo
4. One attempt per (student, week, subject, pathway, tier) — locked at attempt time

**The leaderboard structure:**
- **Champion of the Week** at the top (hero section) — cross-all-tracks, raw score, tiebreak by time, ≥1 subject completed
- Pathway toggle (Combined / Triple)
- Tier toggle (Foundation / Higher)
- Subject tabs (Overall / Biology / Chemistry / Physics)
- Auto-lands on the student's own track

**Content scoping rules (critical):**

| Pathway + Tier | Content shown |
|---|---|
| Combined Foundation | Base only (shared AQA Combined Science content, Foundation difficulty) |
| Combined Higher | Base + Higher (NO Triple-only topics) |
| Triple Foundation | Base + Triple-only topics (Foundation difficulty) |
| Triple Higher | Everything (full AQA Triple spec, full difficulty range) |

The backend's Claude API prompt enforces this via 4-way branching in `generateWeeklyChallenge`. The frontend must never send `tier` or `pathway` as query params — the backend reads them from the authenticated user's profile.

---

## Frontend–Backend Coordination

The backend lives in a **separate repo**: `mrbadmus---backend` (three dashes) at `/Users/midebadmus/Documents/GitHub/mrbadmus---backend`.

The two repos share an API contract documented in **`API-CONTRACT.md` in the backend repo**. If you're making changes that touch API endpoints, open that file FIRST.

**Rule: frontend and backend changes that affect the API contract must be deployed together.** A breaking change pushed to only one side will cause student-visible errors. The correct deployment sequence:
1. Run any required SQL migrations in Supabase
2. Push backend repo (Render auto-deploys, wait for "Live")
3. Run `python3 generate_site_v5.py`
4. Push frontend repo (Cloudflare auto-deploys)
5. Smoke test

---

## How the Site is Generated

Topic pages (e.g. `/physics/energy.html`, `/biology/bioenergetics/photosynthesis.html`) are **not written by hand** — they're produced by:

```bash
python3 generate_site_v5.py
```

The script reads structured data from `all_subtopics_*.py` files (topics, subtopics, equations, required practicals, higher-tier flags, triple-only flags) and outputs complete HTML files for every spec point. It also copies hand-edited root HTML files (weekly-challenge.html, leaderboard.html, etc.) into `mrbadmus_site/` which Cloudflare serves.

**If you want to edit topic content:** change the generator or the subtopic `.py` files — never edit the HTML output directly, because the generator will overwrite it.

**If you want to edit hand-written pages (weekly-challenge.html, leaderboard.html, etc.):** edit the root-level file, then run the generator so it copies into `mrbadmus_site/`.

---

## How the AI Chat Backend Works

Every topic page embeds a chat panel powered by `shared/mrbadmus.v2.js`. When a student sends a message:

1. JavaScript builds a system prompt telling the AI it's "Mr Badmus AI — an expert AQA GCSE Science teacher", including current subject context and detailed AQA spec content
2. Sends to: `POST https://mrbadmus-backend.onrender.com/api/chat`
3. Backend forwards to Claude API
4. Response comes back as `data.content[].text`
5. Displayed and appended to `chatHistory` (capped at 20 messages)

The AI is instructed to always use the **FIFA method** for calculations (Formula → Insert → Fix → Answer), always include units, use encouraging language, label Higher Tier (⭐) and Triple-only (🔬) content clearly, and answer across all three sciences regardless of the current page.

If the backend is unreachable, the chat falls back to a static message.

---

## Known Conventions and Gotchas

- **No build tools.** No npm, no webpack, no bundler. Everything runs as plain files in the browser.
- **Shared JS via `window.MrBadmus`.** The chat engine exposes itself as a global so any page can call `MrBadmus.init(...)`.
- **Supabase auth is client-side.** Sessions in `localStorage` under `sb-urklkrwevjtlfbwnipjn-auth-token`. Supabase JS SDK loaded via CDN — no import system.
- **Inline auth-check scripts.** Each HTML page has a small inline `<script>` at the top of `<nav>` that swaps Sign In / Sign Up for the logged-in user's name + avatar.
- **Color-coded subjects:** Physics teal (`#4ECDC4`), Chemistry pastel pink (`#FFD2E6`), Biology green (`#6BCB77`)
- **Pathway colours:** Combined teal (same as Physics), Triple pastel pink (same as Chemistry)
- **`--chemistry` vs `--danger` split** (MRB-46 Phase 3 v3, 2026-05-25):
  Chemistry used to be `#FF6B6B` red, which was being conflated with
  "warning" UI semantics (overdue tones, error text, delete-X hover).
  Swapped Chemistry to pastel pink `#FFD2E6`; introduced a paired
  `--danger: #FF6B6B` token for destructive UI. **For NEW code: use
  `var(--chemistry)` only for chemistry-subject identity; use
  `var(--danger)` for everything red-as-warning** (overdue, missed,
  error states, destructive button hovers). Existing files outside
  `student/class.html` still route destructive UI through
  `var(--chemistry)` — that's a known limitation, not a desired
  state. Route to `var(--danger)` when you next touch each surface.
- **Tier colours:** Foundation green, Higher yellow (`#FFD93D`)
- **Backend URL is hardcoded** as `https://mrbadmus-backend.onrender.com` in `mrbadmus.v2.js`. No environment variables on the frontend (no build step).
- **Supabase anon key is hardcoded** in pages that need it (e.g. leaderboard.html for profile reads). Anon keys are designed to be public — safe to commit.
- **Cloudflare `_redirects` proxy is broken** — all API calls point directly at the Render URL, not through the frontend domain.

---

## Supabase migrations toolchain

Established by MRB-84 (2026-05-24). Future migration work follows this pattern.

### Folder taxonomy

Four sibling folders under `supabase/`, each with a `README.md`. The Supabase CLI only reads `migrations/`; the other three are invisible to `supabase db push` and `supabase migration list`.

- **`supabase/migrations/`** — forward migrations. Files named `YYYYMMDDHHMMSS_description.sql` where the timestamp matches the `schema_migrations.version` they register as. CLI parses the version from the filename.
- **`supabase/rollbacks/`** — manual undo SQL for specific migrations. Apply manually only. Files keep the original `NNNN_` sequence prefix (CLI never reads them).
- **`supabase/baselines/`** — bootstrap/recovery SQL (recreate from scratch, disaster recovery). Apply manually only.
- **`supabase/seeds/`** — test-only fixture SQL (fake users, fake submissions). Never applied on prod via CLI; manual psql only against test.

### Apply path

- **Primary:** `supabase db push` against a linked project. Faster and more durable than the MCP, and produces a clean local migration file as part of the workflow. Use this for all routine forward migrations from MRB-46 Phase 2 onward.
- **Fallback:** MCP `apply_migration` for one-off ad-hoc SQL where a checked-in migration file isn't warranted (e.g. emergency hotfix). MCP auth is fragile — tokens expire, `remove` + `add` cycles wipe the token. Use sparingly.

### Auth setup for the CLI

The CLI's OAuth flow stores its token in macOS Keychain, which isn't accessible to Claude Code's Bash tool (non-interactive shell can't unlock the keychain). Use a Personal Access Token instead, stashed in a tmp file:

```bash
read -rs SUPABASE_ACCESS_TOKEN
printf '%s' "$SUPABASE_ACCESS_TOKEN" > /tmp/sb_token && chmod 600 /tmp/sb_token
unset SUPABASE_ACCESS_TOKEN
```

Then prefix CLI commands with `SUPABASE_ACCESS_TOKEN="$(cat /tmp/sb_token)"`. DB password follows the same pattern (`/tmp/sb_pw`). Clean both up at end of session. Generate the PAT from `supabase.com/dashboard/account/tokens`.

### Other Supabase-related operational notes

- `supabase-test` MCP stays permanently write-enabled. Never swap its `read_only` URL flag — project-scope (`project_ref=qeppkiswvclkkwbxmlok`) is the actual safeguard; toggling `read_only` costs an OAuth re-auth per swap.
- Production project ref: `urklkrwevjtlfbwnipjn`. Test project ref: `qeppkiswvclkkwbxmlok`. Never confuse them; the test project is the safe sandbox.
- Pooler maintenance for `eu-west-1` on 2026-06-01 14:00 UTC. Test DB is in this region. During the window, expect intermittent failures via the session pooler (`aws-0-eu-west-1.pooler.supabase.com:5432`). Avoid migration apply or DB verification work during the window.

---

## Working with Mide

Mide is a teacher and creative founder, not a developer. Keep this in mind at all times:

- **Always explain what you're about to do before doing it.** Never make a change silently.
- **Explain technical things in plain English.** Avoid jargon. If a technical term is necessary, define it in the same sentence.
- **Investigate before changing.** Read the code first. Don't guess at schemas or file structures. Ask "are you sure that's everything?" before multi-file changes. Ask "what could go wrong?" before structural changes.
- **Show before/after diffs before editing.** Mide must understand the why before approving.
- **One change at a time.** Strict scope discipline — slow and thorough beats fast and patchy.
- **Prefer small, reversible changes over big rewrites.**
- **When suggesting terminal commands, always explain what each one does** — not just what to type, but what will happen when it runs.
- **Flag anything that could break the live site** before proceeding. 135+ students rely on this site.
- **Never `git push` in Terminal** — Mide uses GitHub Desktop exclusively for commits and pushes.
- **For Supabase admin tasks**, give Mide direct SQL to paste into the Supabase SQL Editor. Never try to migrate schemas from code.

---

## Working pattern (how Mide and Claude operate)

Captured 12 May 2026 mid-way through MRB-38 build. This is how Mide
and chat-Claude have been operating across the schools layer rollout.
Future-Mide and future-Claude (and any new collaborator) should keep
to this.

**1. Three-way workflow with clear lanes.** Mide directs (product,
scope, priorities). Chat-Claude architects (plans, writes prompts,
gates between phases, plain-English translator). Claude Code executes
(queries, code, file edits, Linear writes). Each lane does what it's
best at. None of us tries to do the others' jobs.

**2. Investigate before editing.** Read the current state first. No
"I'll just change this" without recon. Diffs shown before approval.
The work moves faster long-term because we don't waste time undoing
wrong assumptions.

**3. Gate-driven phases.** Big tasks split into sub-phases. Each
phase has an explicit gate where chat-Claude pauses for Mide's
approval. No barrelling through. Catches divergence early when it's
cheap to fix.

**4. "What could go wrong?" before structural changes.** Standard
pre-flight check before any migration, refactor, or scope change.
Catches edge cases that would otherwise become Phase 6 bugs.

**5. "Are you sure that's everything?" before approving multi-file
changes.** Specifically catches scope-creep in batches.

**6. Linear is source of truth.** Every decision, gotcha, deferred
item gets pinned. No "remind me why we did this" 6 weeks later.
Comments on the right ticket so context lives with the work.

**7. New scope goes in new tickets or comments, never folded silently
into the current ticket.** Avatar bank → MRB-55. Multi-attempts →
comment on Stage 4 ticket. Brand drift → MRB-54. The thing in front
of us stays the thing in front of us.

**8. Production-touching work uses the MCP swap dance.** Both
Supabase MCPs (prod + test) are never live simultaneously.
`claude mcp remove supabase-test` before any prod step, re-add after.

**9. Never `git push` from terminal.** GitHub Desktop only. Always.

**10. Mide manages his own schedule.** Chat-Claude does not project
fatigue or advise breaks unless Mide explicitly raises it. Speed of
ideation→execution is the priority.

**11. Supabase tooling discipline.** Hard-won from MRB-46 Phase 1
(24 May 2026) after ~2 hours of MCP auth churn. Apply paths, folder
taxonomy, CLI auth pattern, and operational notes (test/prod refs,
pooler maintenance, `supabase-test` MCP write-enabled rationale)
live in the "Supabase migrations toolchain" section above. With
MRB-84 landed, the CLI (`supabase db push`) is the primary apply
path; MCP `apply_migration` is the one-off ad-hoc fallback. The
swap-dance in item 8 above applies only when explicitly switching
to prod, not for read/write toggles within test. Gotchas observed
in the wild:

- **RLS soft-delete gotcha.** If a SELECT policy filters by a column
  the UPDATE will set (e.g. `deleted_at IS NULL`), the UPDATE fails
  with `42501: new row violates row-level security policy` even when
  the UPDATE policy passes. Postgres applies SELECT USING to the
  post-update row state to prevent information-leak via update-into-
  invisibility. Fix: widen the SELECT policy to cover the legitimate
  post-update state (e.g. allow author to see their own deleted rows),
  or use a SECURITY DEFINER function. The frontend can continue
  filtering defensively — UX stays the same. Discovered in MRB-46
  Phase 2 when wiring author-only soft-delete on `class_shoutouts`;
  fix lives in migration `20260524195500_fix_class_shoutouts_soft_delete.sql`.

Mide's stated principle: "Slow and thorough beats fast and patchy" —
applied to *correctness*, not pace. Ideation cycles stay short;
verification stays rigorous.

---

## Known Deferred Items

Small things to tighten when you're next in the relevant area — not urgent, not blockers:

1. **`auth.html` redirect check:** currently only checks `science_pathway`, not `tier`. A user with `tier=null` slips past the redirect and only hits the backend's 400 on the weekly-challenge page. Fix when next editing auth.html: check both fields.

2. **`profile-setup.html` edit mode:** the Save button in edit mode bypasses step 2 validation. Safe today because existing profiles have pathway/tier pre-filled, but add a finish() guard when next editing profile-setup.

3. **`/api/weekly-leaderboard/landing` champion:** doesn't include `subjects_done`, unlike `/api/weekly-leaderboard/champion`. The landing page hardcodes "all 3 subjects" in the display copy — slightly inaccurate if the champion only did 1–2 subjects. Tighten when next touching the landing section of index.html.

---

## Supabase Schema (key tables)

- `profiles` — user data. Key columns: `id`, `first_name`, `school_name`, `avatar_url`, **`science_pathway`** (values: `combined` / `triple`), **`tier`** (values: `foundation` / `higher`)
- `weekly_challenges` — generated quizzes. Unique constraint: `(week_start, subject, pathway, tier)`. **Note: profile column is `science_pathway`, but here it's just `pathway`.**
- `weekly_scores` — student attempts. Stores pathway, tier, subject, score, max_score, time_taken. `pathway` is locked at attempt time (copied from the challenge row, not from profile).

⚠️ **Schema naming gotcha:** the profile table uses `science_pathway`, but `weekly_challenges` and `weekly_scores` use just `pathway`. Don't confuse them in queries.
## How to work (commander, executor, scout)

You are the commander. Hand work off instead of doing it yourself:
- Reads, searches, "where is X" -> the scout.
- Content authoring, porting, any file edits -> the executor.
- You keep your focus for planning and judgement.

Act, do not ask. Only stop for Mide on: anything touching the live site,
anything that cannot be undone, a real product or scope decision, and the
merge decision. Everything else, just do it and say what you did.

Never git push. Mide pushes via GitHub Desktop. One session works one worktree.