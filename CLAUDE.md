# CLAUDE.md — MrBadmusAI Project Guide

This file gives Claude Code (the AI assistant) everything it needs to understand this project and work on it effectively.

---

## What is MrBadmusAI?

MrBadmusAI is a free GCSE Science revision website for UK secondary school students. It covers all three AQA sciences — Physics (spec 8463), Chemistry (spec 8462), and Biology (spec 8461) — at both Foundation and Higher tier, including Combined Science and Triple Science.

The site features:
- Topic notes and subtopic pages for every AQA spec point
- A live AI tutor chat (powered by Claude via a backend API)
- A weekly challenge system with a leaderboard
- Past paper links
- User accounts (sign up / sign in) with personalised profiles

The name "MrBadmus" refers to Mide Badmus, the teacher who built this site for his students.

---

## Tech Stack

| What | How |
|---|---|
| **Frontend** | Plain HTML, CSS, and vanilla JavaScript — no React, no framework |
| **Styling** | A single shared stylesheet: `shared/styles.css` |
| **AI chat engine** | `shared/mrbadmus.v2.js` — one JavaScript file shared across all pages |
| **AI model** | Claude (Anthropic) — accessed via a custom backend |
| **Backend API** | A separate server hosted on Render at `https://mrbadmus-backend.onrender.com` |
| **Auth & database** | Supabase — handles user sign-in, session tokens, profiles, and leaderboard data |
| **Site generation** | A Python script (`generate_site_v5.py`) that builds all topic HTML pages from structured data |
| **Hosting** | Static site hosting (previously Netlify) |

---

## Key Files and Folders

```
mrbadmus-site/
│
├── index.html              — Homepage
├── auth.html               — Sign in / sign up page
├── profile-setup.html      — User profile page
├── weekly-challenge.html   — Weekly quiz challenge
├── leaderboard.html        — Student leaderboard
├── my-challenges.html      — A student's personal challenge history
├── past-papers.html        — Links to AQA past papers
│
├── shared/
│   ├── styles.css          — All site-wide CSS styles
│   └── mrbadmus.v2.js      — Core AI chat engine (shared by every page)
│
├── biology/                — Biology topic pages (auto-generated)
├── chemistry/              — Chemistry topic pages (auto-generated)
├── physics/                — Physics topic pages (auto-generated)
├── triple/                 — Triple Science pages (auto-generated)
├── combined/               — Combined Science pages (auto-generated)
│
├── generate_site_v5.py     — Python script that generates all topic pages
├── all_subtopics_*.py      — Python files defining subtopic content per subject/tier
│
└── mrbadmus_site/          — Output folder produced by the generator (a copy of the built site)
```

---

## How the Site is Generated

The topic pages (e.g. `/physics/energy.html`, `/biology/bioenergetics/photosynthesis.html`) are **not written by hand**. Instead, they are produced automatically by running:

```
python3 generate_site_v5.py
```

This script reads structured data — topics, subtopics, equations, required practicals, higher-tier flags, triple-only flags — and outputs complete HTML files for every spec point across all three sciences.

The `all_subtopics_*.py` files contain the detailed subtopic lists. For example:
- `all_subtopics_physics_higher.py` — all Physics Higher tier subtopics
- `all_subtopics_biology_triple_foundation.py` — Triple Biology Foundation subtopics

**If you want to add or edit topic content, the right place to do it is in the generator script or the subtopic files — not by editing the HTML output directly**, because the HTML will be overwritten the next time the generator runs.

---

## How the AI Chat Backend Works

Every topic page embeds a chat panel powered by `shared/mrbadmus.v2.js`. Here is what happens when a student sends a message:

1. The JavaScript builds a system prompt that tells the AI it is "Mr Badmus AI — an expert AQA GCSE Science teacher". The prompt includes the current subject context and detailed AQA spec content.
2. It sends the message to the backend: `POST https://mrbadmus-backend.onrender.com/api/chat`
3. The backend (a separate Node/Express server running on Render) forwards the request to the **Claude API** (Anthropic).
4. The response comes back in Claude's standard format: `data.content[].text`.
5. The JavaScript displays the reply in the chat panel and appends it to `chatHistory`.
6. Chat history is capped at 20 messages to keep token usage manageable.

The AI is instructed to always use the **FIFA method** for calculations (Formula → Insert → Fix → Answer), always include units, use encouraging language, keep replies short, and label Higher Tier and Triple-only content clearly.

If the backend is unreachable, the chat falls back to a static message pointing students to ask their teacher.

---

## Conventions Noticed in the Code

- **No build tools.** There is no npm, no webpack, no bundler. Everything runs as plain files in the browser.
- **Shared JS via `window.MrBadmus`.** The chat engine exposes itself as a global object (`window.MrBadmus`) so any HTML page can call `MrBadmus.init(...)` to activate the chat.
- **Supabase auth is client-side.** User sessions are stored in `localStorage` under the key `sb-urklkrwevjtlfbwnipjn-auth-token`. The frontend reads this directly without a library import — the Supabase JS SDK is loaded via a CDN script tag.
- **Inline scripts for auth checks.** Each HTML page has a small inline `<script>` block at the top of the `<nav>` that checks localStorage and swaps out the nav buttons (Sign In / Sign Up) for the logged-in user's name and avatar.
- **Color-coded subjects.** Physics uses teal (`#4ECDC4`), Chemistry uses orange/amber, Biology uses green. This is consistent across pages.
- **Higher tier content is labelled ⭐**, triple-only content is labelled 🔬 — both in the AI's system prompt and in the generated HTML.
- **Backend URL is hardcoded** as `https://mrbadmus-backend.onrender.com` in `mrbadmus.v2.js`. There is no environment variable system on the frontend (because there is no build step).

---

## Working with Mide

Mide is a teacher and creative founder, not a developer. Keep this in mind at all times:

- **Always explain what you're about to do before doing it.** Never make a change silently.
- **Explain technical things in plain English.** Avoid jargon. If a technical term is necessary, define it in the same sentence.
- **Prefer small, reversible changes over big rewrites.** Make one change at a time so it's easy to undo if something goes wrong.
- **When suggesting terminal commands, always explain what each command does** — not just what to type, but what will actually happen when it runs.
- **Flag anything that could break the live site** before proceeding. Mide's students rely on this site, so stability matters.
