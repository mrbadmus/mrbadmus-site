# MrBadmus Wrapped — build plan (commander, 14 Oct 2026)

Source: Mide's prompt of 14 Oct (wins) + `wrapped-spec.md` (rulings of 8 Oct).
Branch `feat/wrapped` (site), migration parked on `feat/wrapped-migrations`.

## 0. Facts established in recon (do not re-derive)

- `flashcard_card_state` is a FUNCTION (not a table), identical on TEST and
  prod (md5(prosrc) `ec4834b787ec5c7e4b3408c9876457bb`). Its `secured` column
  = "ANY `got_it` rating this pupil ever gave this card on this assignment"
  (Y2 / MRB-354, "once secured, stays secured"). That is THE secured truth —
  the bench's `securedInfo()` is its JS twin. Wrapped calls
  `flashcard_card_state(assignment, pupil)` from inside its definer
  functions; it never re-implements the rule.
- A deck = a flashcard ASSIGNMENT (`assignments.kind = 'flashcards'`, cards in
  `assignment_flashcards`). Human name = `assignments.title`. Deck finished =
  every card in it secured.
- Homework topic name = `assignments.topic` for `kind <> 'flashcards'`
  (real values: "Particle Model of Matter", "Cells and organisation").
- "Handed in" = `assignment_submissions.submitted_at IS NOT NULL AND
  deleted_at IS NULL`. First attempt per (assignment, pupil) =
  `ORDER BY coalesce(attempts, 2147483647), coalesce(submitted_at,'infinity')
  LIMIT 1` (the class board's rule).
- STARS = the class board's points (`class_stars_board_for_member`, live on
  prod and TEST): per (class, teaching week) `round(sum(score)/sum(max_score)
  *100)` over COUNTED first attempts — `submitted_at <= due_at`, `due_at` not
  null, score/max not null, max > 0. Week = `coalesce(a.academic_week,
  _mrb_week_number(ay.start_date, coalesce(a.release_at, a.created_at)))`.
  A pupil's stars = sum of their per-week points. The pupil page labels these
  "points"; the Wrapped card calls them stars (Mide's word).
- Teaching week: `public._mrb_week_number(year_start date, instant)` exists
  on both projects (Sunday 00:00 Europe/London roll).
- Auth helpers: `auth_user_is_member_of_class(uuid)`,
  `auth_user_teaches_class(uuid)` (both definer, live).
- Year group = `classes.year_group` (smallint 7–13), comparison group = same
  `school_id`, same `academic_year_id`, same `year_group`.
- `quiz_scores(user_id, created_at, ...)` exists (2 pupils on prod). Counts
  toward the week streak only.
- No term dates exist anywhere in the repo or DB. Rainford Oct half term:
  last day Fri 23 Oct 2026, back Mon 2 Nov (St Helens dates). Christmas: last
  day Fri 18 Dec 2026 — CONFIRMED by Mide 15 Oct 2026 (card keeps "by Christmas"); a setting.
- Prod preview ids: AY `b0308282-5429-4050-827f-4707286a88aa` (pupil, 8r/Sc1
  `d9740ab8-c4e3-4c22-bce9-629b650782c5`, username WolfBeam); Mide
  `74db2bf7-7c0d-47e6-9479-5cee3cda610e` (teacher of 8r/Sc1). The other
  8r/Sc1 teacher must NOT get the preview.
- The class pages load supabase-js from jsDelivr already (pre-existing).
  Wrapped itself adds NOTHING from a CDN.

## 1. Database (one migration, parked)

`supabase/migrations/20261014120000_wrapped.sql`, rollback
`supabase/rollbacks/20261014120000_wrapped_rollback.sql`, sheet
`supabase/WRAPPED-APPLY.md`. Additive only. No existing object altered.

### 1a. `public.wrapped_settings` — the one date setting

Singleton (`id boolean primary key default true check (id)`):

| column | value on insert |
|---|---|
| `release_at timestamptz` | `'2026-10-20 08:00:00 Europe/London'` |
| `close_at timestamptz` | `NULL` (button stays until someone sets it) |
| `window_start timestamptz` | `'2026-09-01 00:00:00 Europe/London'` |
| `half_term_from date` / `half_term_to date` | `2026-10-24` / `2026-11-01` |
| `christmas_on date` | `2026-12-18` |
| `show_zero_card boolean` | `true` |
| `preview_profile_ids uuid[]` | the two prod ids above |

RLS enabled, NO policies, `revoke all from anon, authenticated`. Only the
definer functions read it.

### 1b. Functions — all `SECURITY DEFINER SET search_path = public`,
`revoke all from public, anon`, `grant execute to authenticated`.
`STABLE`. CTEs only (no temp tables in a STABLE function).

The gate, shared by all three (write it once as an internal helper
`_wrapped_gate(p_preview boolean) returns text` → `'open'|'preview'|'closed'`,
revoked from authenticated):
`open` when `now() >= release_at and (close_at is null or now() < close_at)`;
else `preview` when `p_preview and auth.uid() = any(preview_profile_ids)`;
else `closed`.

**`wrapped_status(p_class_id uuid, p_preview boolean default false) → jsonb`**
Cheap; called on every class-page load.
`{open, preview, role: 'pupil'|'teacher'|null, has_activity, show_zero}`.
role = pupil if `auth_user_is_member_of_class`, teacher if
`auth_user_teaches_class`, else null (→ open false). `has_activity` only
computed (EXISTS probes) when open and role = pupil; null otherwise.

**`wrapped_pupil(p_class_id uuid, p_preview boolean default false) → jsonb`**
There is NO pupil parameter: the pupil is always `auth.uid()`. Not a member
of `p_class_id` → `{"state":"not_member"}`. Gate closed →
`{"state":"closed"}`. Otherwise:

```json
{ "state": "open", "preview": false, "zero": false,
  "name": {"first": "AY", "username": "WolfBeam"},
  "class": {"id": "…", "name": "8r/Sc1"},
  "window": {"from": "2026-09-01", "to": "2026-10-20"},
  "cards": [ … only the cards that have good news … ] }
```

Data scope = ALL the pupil's own activity in the window (every class), so a
separate-sciences pupil gets one Wrapped, not three. Window = `window_start`
to `now()`.

Cards (each emitted only when its condition holds; order as listed):

1. `{"kind":"opener"}` — always (when not zero).
2. `{"kind":"flashcards","secured":N,"decks_finished":M}` — N = count of
   (assignment, card) with `secured` per `flashcard_card_state`, over
   flashcard assignments the pupil has ≥1 review on in the window. M = those
   assignments where every card is secured. Emit when N > 0.
3. `{"kind":"homework","handed_in":N,"stars":S}` — N = hand-ins (non-flashcard
   assignments, first attempt, `submitted_at` in window). S = stars (board
   rule, all assignments incl. flashcards, exactly as the board counts).
   Emit when N > 0; S may be 0 (frontend omits the line).
4. `{"kind":"best_topic","topic":"…","source":"homework","pct":86}` or
   `{"kind":"best_topic","topic":"…","source":"deck","cards":12}`.
   Rule: best homework topic by pct (ties → more hand-ins, then name) when
   pct ≥ 70; else a fully secured deck (most cards); else best homework topic
   when pct ≥ 50; else omit.
5. `{"kind":"streak","weeks":N,"current":bool}` — longest run of
   consecutive teaching weeks (week numbers from `_mrb_week_number(window
   start date, instant)`) with any hand-in, any flashcard review, or any
   quiz_scores row. `current` = the run includes this week or last week.
   Emit when N ≥ 2.
6. Top band — exactly one of:
   - `{"kind":"top_band","scope":"year","band":10,"year_group":11,"topic":"…"}`
   - `{"kind":"top_band","scope":"class","top":3,"class_name":"11r/Sc1","topic":"…"}`
   - `{"kind":"top_band","scope":"personal","topic":"…","cards":N}` (a fully
     secured deck that is NOT the deck already named on card 4)
   - omitted.
   Per homework topic the pupil has a hand-in on: group = pupils in the same
   year group (same school + academic year) with ≥1 first-attempt hand-in on
   that same `assignments.topic` in the window; per-pupil pct as card 4.
   HONEST TOP: a pupil is in the top X if the number of group members with
   pct ≥ theirs (themselves included) ≤ X. Year: n ≥ 10 and in top
   `ceil(n*b/100)` for the smallest b in (1, 5, 10) that qualifies. Class
   fallback (the class of that topic's assignment): n ≥ 10 in that class and
   in the honest top 3. Pick the best result across topics (year beats class;
   smaller band beats larger). Only the band leaves the database — never
   another pupil's numbers, never n, never a rank.
7. `{"kind":"forward","metric":"cards"|"homework","now":C,"projected":P}` —
   metric = cards if card 2 exists else homework if card 3 exists. pace =
   C / greatest(1, weeks since window_start). weeks_left = days from today
   to `christmas_on` minus days overlapping the half term, / 7. P = C +
   floor(pace × weeks_left). Emit when P > C.

Zero activity (no hand-in, no review, no quiz row in the window) →
`{"state":"open","zero":true,"show_zero":true|false,"name":…,"class":…}` with
no cards.

**`wrapped_class(p_class_id uuid, p_preview boolean default false) → jsonb`**
Not a teacher of `p_class_id` (`auth_user_teaches_class`) →
`{"state":"not_teacher"}`. Gate closed → `{"state":"closed"}`. Otherwise,
over CURRENT members of the class and THIS class's assignments in the window:

```json
{ "state":"open", "class":{"id","name","year_group"},
  "cards":[
   {"kind":"opener","pupils":30,"active":12},
   {"kind":"homework","handed_in":N},
   {"kind":"flashcards","secured":N,"decks":M},
   {"kind":"most_secured","topic":"…","pct":82},
   {"kind":"revisit","topic":"…","pct":41},
   {"kind":"top3","pupils":[{"first_name":"AY","stars":312}, …]} ] }
```

`most_secured` = flashcard deck with the highest secured share (secured
cards ÷ (cards × pupils who started it)), ties → more secured. `revisit` =
the class's lowest pct homework topic with ≥ 3 hand-ins. `top3` = up to three
pupils with stars > 0 by stars desc (ties as the board breaks them), first
name only (append surname initial ONLY when two of the three share a first
name — teacher-only screen). Cards with nothing behind them are omitted.

**Catch-ups (from the parallel catch-up session, 14 Oct):** an assignment
with a non-empty `assignments.recipient_ids` (a parked column, absent on
prod) is a catch-up and does NOT count in `wrapped_class` totals. Tested
without naming the column:
`coalesce(jsonb_typeof(to_jsonb(a)->'recipient_ids'),'null') = 'null'`.
A pupil's own `wrapped_pupil` still counts it.

### 1c. TEST rehearsal + proof (all on `qeppkiswvclkkwbxmlok`)

- Apply via MCP; record the version it mints; rename files to match only if
  needed (the parked file keeps its own timestamp — see project memory).
- Fixture world (snapshotted id list for teardown, never a predicate
  delete): one class shaped like 8r/Sc1 with ≥ 12 pupils who have data on
  one homework topic (so the n ≥ 10 rule is exercised), a second class in
  the same year group, a busy pupil, a light pupil (one hand-in), a zero
  pupil, a teacher. Set TEST `preview_profile_ids` to the fixture busy /
  light / zero pupils and the fixture teacher; leave `release_at` in the
  future so the PREVIEW path is what the walks prove.
- RLS proof by impersonation (`request.jwt.claims` + `set local role
  authenticated`): pupil A → `wrapped_pupil(B's class)` = not_member, no
  numbers; pupil A → `wrapped_class(any)` = not_teacher; pupil A's own
  payload contains no other pupil's id/name/number; non-preview pupil with
  `p_preview=true` → closed; anon → permission denied; authenticated →
  `select * from wrapped_settings` returns 0 rows / denied.
- Read-only prod replay: AY's cards computed as a plain SELECT (no DDL on
  prod) to show Mide what his preview will contain.

## 2. Frontend

`shared/wrapped.js` + `shared/wrapped.css` (plain JS, no framework, no CDN,
Web Animations API + CSS — no GSAP: ~0 KB of dependency on an old Android,
and reduced motion is one branch).

- Loaded on `student/class.html` (class view only) and
  `teacher/class-detail.html` (live pages; fail-closed on fixtures, which
  have no Supabase config). `<script src="/shared/wrapped.js"
  data-wrapped="pupil|teacher">`. Add both names to the builders'
  `STAMPED_DEPS`.
- On load (idle, never on the page's critical path): class id from
  `?class=`, `p_preview` = `?wrapped=preview`, call `wrapped_status`. If the
  RPC is missing (prod before the migration) or errors → do nothing,
  silently. If open and (teacher, or has_activity, or show_zero) → inject a
  button ("Your half-term Wrapped" / "Class Wrapped") into the class header,
  idempotently, surviving runtime redraws (`__MRB_AFTER_DRAW__` on the pupil
  page, MutationObserver on the teacher page, as class-csv-upload.js does),
  `data-mrb-added="wrapped-open"`. `?wrapped=preview` also auto-opens.
- Story overlay appended to `document.body` (like set-work): full screen,
  thin progress segments, tap right = next, tap left = back, hold = pause,
  ~7 s auto-advance, pause when the tab is hidden, Esc/arrow keys, close
  button. One idea per card, huge Bricolage type, DM Mono numbers that count
  up, own colour field + own motion per card, all from the design tokens.
  No typed arrow/tick/cross glyphs — SVG. `prefers-reduced-motion`: same
  cards, fades only, numbers land at their value.
- Summary card = share card. Drawn straight to a 1080×1920 `<canvas>` after
  `document.fonts.load(...)` for every face used; mark from
  `/shared/brand/mrbadmus-chevron.svg` as an Image (never path data — the
  brand gate); wordmark "MrBadmus" Bricolage 600; `mrbadmus.com`. Name =
  first name, or "first (username)". The image NEVER carries a surname,
  photo, school, or class code — so a class-scope top band is left OFF the
  image (it names the class). `navigator.share({files})` when
  `canShare` says yes, else download `mrbadmus-wrapped.png`.
- Teacher Class Wrapped: same player, class cards, NO share (it names pupils).
- Zero pupil: one card "Your Wrapped starts now", one line on what
  December's Wrapped could show, a button back to the class.

## 3. Proof

- Playwright (python, `channel="chrome"` — drives the installed Chrome, no
  browser download) walks on TEST against the locally built site:
  busy / light / zero pupil + teacher, at 390×844 and 1440×900, light and
  dark; every card screenshotted to `--shots` (default outside the repo).
- Share PNG opened at full size: 1080×1920, right fonts, nothing cut off,
  no surname.
- All gates green incl. `frozen_window_guard`.
