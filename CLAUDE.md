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

⚠️ **Netlify is legacy** — fully cancelled. Ignore any mention of Netlify, netlify.app, or Netlify functions in old briefs or comments. The stack is Cloudflare Pages + Render only.

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
- **Color-coded subjects:** Physics teal (`#4ECDC4`), Chemistry red (`#FF6B6B`), Biology green (`#6BCB77`)
- **Pathway colours:** Combined teal (same as Physics), Triple red (same as Chemistry)
- **Tier colours:** Foundation green, Higher yellow (`#FFD93D`)
- **Backend URL is hardcoded** as `https://mrbadmus-backend.onrender.com` in `mrbadmus.v2.js`. No environment variables on the frontend (no build step).
- **Supabase anon key is hardcoded** in pages that need it (e.g. leaderboard.html for profile reads). Anon keys are designed to be public — safe to commit.
- **Cloudflare `_redirects` proxy is broken** — all API calls point directly at the Render URL, not through the frontend domain.

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