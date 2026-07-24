# MRB-137 / MRB-138 — Recon (Part A)

_Recorded at HEAD `b98db13146cf36e4feba981c5735495d4fd62466` (branch `main`), working tree clean._

This is the fact base for the landing + leaderboard redesign (MRB-137) and the
usernames feature (MRB-138). Everything below was read from source, not assumed.

---

## 1. How the two pages are produced

Both target pages are **hand-written static HTML at the repo root**, then copied
into `mrbadmus_site/` (the folder Cloudflare serves) by the generator:

- `index.html` — written by `generate_site_v5.py` at line ~4247 (`open(f"{output_dir}/index.html", "w")`).
- `leaderboard.html` — in the generator's copy list at `generate_site_v5.py:4184-4185`
  (alongside `auth.html`, `profile-setup.html`, `weekly-challenge.html`, etc.).
- `shared/*` is auto-copied wholesale (`generate_site_v5.py:4194+`), so a new
  `shared/username-generator.js` lands in the output with no generator edit.

**Workflow:** edit the root file → run `python3 generate_site_v5.py` → it copies into
`mrbadmus_site/`. Never edit `mrbadmus_site/` directly. **Zero subtopic pages are
touched** by editing these root files + shared assets.

---

## 2. Leaderboard data — where it comes from and its exact shape

All ranking data comes from the **Render backend** (`https://mrbadmus-backend.onrender.com`),
a **separate repo** (`mrbadmus---backend`). The frontend never reads leaderboard
names from Supabase directly.

Backend source: `server.js`. Every leaderboard query joins
`profiles!inner(first_name, school_name, avatar_url)` and maps
**`name: profiles.first_name || 'Student'`**. **There is no `username` anywhere in
the backend** (grep: zero matches).

| Endpoint | Entry fields |
|---|---|
| `GET /api/weekly-leaderboard/landing` | `champion` object (`name, school, avatar_url, score, max_score, percentage, subjects_done`) + `foundation_top3` / `higher_top3` arrays (`rank, name, school, avatar_url, score, max_score, subjects_done`). **Top 3 only.** |
| `GET /api/weekly-leaderboard/champion` | `champion`: `name, school, avatar_url, score, max_score, percentage, subjects_done, time_taken`. **No `rank`.** |
| `GET /api/weekly-leaderboard?overall=true&pathway=&tier=` | `week_start` + `leaderboard[]`: `rank, name, school, avatar_url, score, max_score, time_taken, subjects_done`. **No `percentage`.** |
| `GET /api/weekly-leaderboard?subject=&pathway=&tier=` | same as overall but **no `subjects_done`** and **no `percentage`**. |

**Consequences for the redesign:**

1. **Percentage is not served** by the per-view endpoints — only `score`/`max_score`.
   We compute `pct = score / max_score` **client-side** to rank fairly across /30
   (Combined) and /45 (Triple) totals. Ties break by faster `time_taken`.
2. **Endpoints are per-pathway** — `pathway` is a *required* query param
   (`server.js:819-824`). To drop the Combined/Triple filter (Part C) we fetch
   **both** pathways for the current (tier, subject), tag each row with its pathway,
   **merge client-side**, sort by pct, re-rank 1..N. 2 GETs per view; read-only.
3. Pathway/tier for leaderboards come from **query params** (these endpoints are
   public/unauthenticated). The weekly-*challenge* endpoint, by contrast, reads
   pathway+tier from the authenticated profile and ignores params — unchanged here.

### ⚠️ Usernames on the public board are blocked on a backend change
Because `name` is hardwired to `first_name` server-side and the entries carry **no
user id**, the frontend cannot swap in usernames on its own. The display seam
(`displayName`) is built so handles appear **automatically** the moment the backend
adds `username` to its four leaderboard selects. That backend edit is a small,
documented follow-up (separate repo, coordinated deploy) — **out of scope for this
frontend session.** Until it ships, the public board keeps showing first names.
_Mitigation already in the redesign:_ the new public surfaces **drop the school-name
column entirely**, removing school as a public identifier immediately.

---

## 3. Supabase profiles + signup

**Table `public.profiles`** (baseline + later migrations). Relevant columns:
`id (uuid PK → auth.users)`, `first_name`, `last_name`, `avatar_url`, `school_name`,
`science_pathway`, `tier`, `role` (default `student`; added `schools_layer.sql:55`),
`key_stage` (`schools_layer.sql:57`), `display_name` (present in prod, used by
teacher shoutouts; not in a repo migration — added out-of-band). **No `username`.**

**RLS on profiles** (baseline 3 + schools layer 3):
- Own-row `insert` / `update` / `select` (`auth.uid() = id`).
- `profiles_teacher_read_students`, `profiles_hod_read_dept`,
  `profiles_admin_read_school` (`schools_layer.sql:914-938`) — staff read their own students.
- **A public/anon visitor or a plain student cannot read another user's profile.**
  → a username **availability check must be a `SECURITY DEFINER` RPC** returning only
  a boolean (no PII leak). There are established `SECURITY DEFINER` patterns in the
  migrations to copy.

**Signup** (`auth.html`): `sb.auth.signUp({ email, password, options: { data: { first_name }}})`.
No client profile write (no session yet in the email-confirm flow; RLS would block it).
A DB trigger **`handle_new_user` seeds the profile row** from the auth metadata.
`handle_new_user` is **not in the repo** — it lives only in the live DB, so any change
to it (e.g. auto-assigning a username) must be fetched from the DB and edited there.

**Env switching** (`shared/config.js`): PROD by default; TEST project
(`qeppkiswvclkkwbxmlok`) when host is localhost or `?env=test`. `window.MrBadmusConfig`
exposes `SUPABASE_URL / SUPABASE_ANON_KEY / BACKEND_URL`. Existing pages (leaderboard,
index) still hardcode the prod anon key inline; new code should prefer `config.js`.

---

## 4. Every place a user's name is rendered

**PUBLIC ranking surfaces → these get the `displayName` seam (usernames target):**
- `index.html:124` (+champion `:142`) — landing rail names, from backend `.name`.
- `leaderboard.html:277,336,355` — champion/podium/rest names, from backend `.name`.

**Self-facing name (the signed-in user seeing their OWN name — not privacy-sensitive, left as-is):**
- `shared/nav.js:64-65` — nav auth chip: `user_metadata.first_name` → `#nav-auth-area`.
  Signed-in state = presence of a valid `sb-urklkrwevjtlfbwnipjn-auth-token` in
  localStorage (`nav.js:55`); role fetched from `profiles.role` to pick profile link.
- `shared/mrbadmus.v2.js:17,20` — AI chat header "Hey {first_name}".
- `profile-setup.html:627-628` — the student's own dashboard name. **This page is the
  home for the username Change UI (D4).**

**SCHOOL surfaces → keep REAL names (teachers must identify their own students; RLS-isolated, never on the public board). DO NOT change:**
- `student/class.html`, `student/settings.html`
- `teacher/classes.html`, `teacher/class-detail.html`, `teacher/student-detail.html`, `teacher/import.html`
- `teacher-profile.html` (`display_name` = teacher's public shoutout name)
- `shared/shoutouts.js`, `shared/student-data.js`, `shared/teacher-data.js`

---

## 5. Build plan implied by recon

- **Display seam (D1):** `displayName(u) => u.username || u.name || u.first_name || 'Student'`.
  Applied only in `index.html` + `leaderboard.html`. Picks up backend `username` when it ships.
- **Landing rail (Part B):** ONE `/landing` call kept (homepage is perf-sensitive).
  Champion row from `champion`; per-tier lists from `foundation_top3`/`higher_top3`,
  re-sorted by pct client-side, rendered up to 5 (backend currently returns 3 — extending
  `/landing` to top-5 is a trivial backend follow-up; rail degrades gracefully to 3).
- **Leaderboard table (Part C):** 2 GETs (both pathways) per (tier, subject) view,
  merged + ranked by pct client-side, re-ranked 1..10, row 1 crown, rows 1-3 medal chips,
  per-row pathway badge (C/T). Drop the separate `/champion` call — champion collapses
  into table row 1.
- **DB (D6, gated):** `ALTER TABLE profiles ADD username citext UNIQUE`, `last_username_change_at timestamptz`,
  lookup index; `SECURITY DEFINER` RPCs: `username_available(text)`, `set_username(text)`
  (moderation + availability + 30-day lock); a `username_rejection_reason(text)` SQL moderation
  fn reused server-side; `handle_new_user` updated to auto-assign a safe handle (metadata
  preference if valid, else generated). Backfill assigns generated handles with collision retry.
  RLS policies unchanged. Test on TEST project; **gate production (STOP #1).**
