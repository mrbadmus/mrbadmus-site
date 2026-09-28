# Theme run: Light / Dark / System everywhere, and the KS4 pilot polish

This was an unattended run on 26–28 Sep 2026, working to Mide's rulings of 26 Sep 2026. Sonnet built it in six lanes, and Opus audited the live site at the end.

The work shipped as four units, each its own commit and push, and each verified live:

| unit | main | what |
|---|---|---|
| 1 | `b41a18176` | Harness fix: the `edit_shows_the_questions` flake |
| 2 | `d7debf861` | Part 2: KS4 pilot route chip and switcher, approved exam tips, per-route spec numbers |
| 3 | `c6abc686c` | Part 1: Light / Dark / System on every page |
| 4 | `01c9f32d8` | Part 1 follow-up: every defect from the final live audit, plus a gate that sees interaction states |
| 5 | `11bafaab6` | The Opus live re-check's residuals (N1, D9 remainder, N2, N3) and this report |

## Part 1: Light / Dark / System on every page

### How it works

There is one pre-paint snippet, one shared script, and a set of tokens for each family.

**`theme_head.py`** holds the one pre-paint snippet.
- Every generator imports it, and every hand-written page carries it byte for byte.
- It sits immediately after `<meta charset>`, before any stylesheet.
- It reads `localStorage['mrb-theme']` inside a try/catch.
- It writes `<html data-theme="light|dark" data-theme-pref="light|dark|system">` before first paint.
- **Light is the default**, and the fallback for anything it can't read, whatever the device says.

**`shared/theme.js`** is the one control. It is a native radio group with the legend "Colour theme" and three options, Light / Dark / System. The icons carry screen-reader text.
- Tab lands on the chosen option, and the arrow keys move and choose. That is the browser's own keyboard contract.
- It saves the choice and follows `prefers-color-scheme` live under System.
- It keeps other open tabs in step and re-applies after a back/forward-cache restore.
- It re-mounts into any header slot a page's code redraws. A slot counts as mounted only if the control is actually inside it. That matters because the KS4 pilot's renderer emptied the slot but kept the flag.

The control has two forms:
- **Full:** a three-segment control, used on most headers.
- **Compact:** used where a slot asks for it (`data-mrb-theme="compact"`). Below 600px it becomes one button, labelled "Colour theme: *mode*", which opens the same three choices. Esc closes it, and so does a tap outside it.

Its CSS is self-contained and uses `currentColor`, so it fits every header without per-family styling.

Placement depends on the header:

| header | where the control sits |
|---|---|
| KS4 chrome, KS3, KS4 pilot (`Ks4Chrome` nav), teacher top bar, leaderboard | in the header |
| classic nav (older KS4 lessons and the root pages) | in the bar above 960px; in the menu drawer's "Theme" row at 960px and below |
| student top bar | full above 600px, compact below |
| KS3 below about 700px | wraps to its own header row |
| 18 B2C pages with hand-written headers | a small fixed badge, top right |

The classic nav moves the control into the drawer for a measured reason. With a pupil signed in and the notification bell showing, the bar had no room left; see Deviations.

**Dark lives at the tokens**, keyed on `html[data-theme="dark"]` only.
- No `prefers-color-scheme` block can fire on its own any more.
- Every dark rule is limited to `@media screen`, so printing is dark text on white whatever the theme.

### Families

| family | pages | light | dark | control | contrast (light / dark) |
|---|---|---|---|---|---|
| Landing + KS4 chrome (hub, pathway, tier, subject, topic) | 118 | unchanged | built at `--k4-*` tokens (`ks4-chrome.css`) | header | 0 / 0 |
| Older KS4 lessons | 811 | unchanged except the fixes below | token-driven; "Test Yourself" result, FIFA letters and symbols tokenised | classic nav / drawer | 0 / 0 |
| KS4 pilot lessons | 54 | unchanged except the Part 2 changes | `ks4-theme.css`, now keyed on `data-theme` only | `Ks4Chrome` header nav | 0 / 0 |
| KS3 (hub, years, units, lessons) | 297 | unchanged except two season inks and the "Commit first" prompt | new `shared/ks3-theme.css` | header (own row on phones) | 0 / 0 |
| Student (class, assignment, classes, settings, claim-confirm) | 5 | unchanged (pixel diff) | `THEME_DARK_CSS` in `student_rulings.py`; all six bench themes work | top bar (compact on phones) | 0 / 0 |
| Teacher (6 generated, 4 hand-written, seating, decks, flashcards) | 13 | unchanged (pixel diff) | `THEME_DARK_CSS` in `teacher_rulings.py`; Set work sheet, breakdown and toast | top bar | 0 / 0 |
| Leaderboard | 1 | unchanged | `THEME_DARK_CSS` in `build_leaderboard_port.py` | classic nav / drawer | 0 / 0 |
| Root pages (auth, profile-setup, weekly-challenge, my-challenges, past-papers, revision, reset-password, teacher-profile, 404) | 9 | unchanged | shared tokens | own nav, or top right on reset-password | 0 / 0 |
| B2C (consumer, parents, go, org) | 23 | unchanged (pixel diff on the flag-off screen) | `ks3-theme.css` and their own tokens | 5 in the `public.js` header; 18 as a fixed badge | 0 / 0 |
| Worksheet preview / Set work sheet | overlay | unchanged | `set-work.css` | the teacher page's control | 0 / 0 |
| Printed worksheets and print of any page | print | always light | none, by design | none | n/a |
| 3D Studio (`/3d/`) | Vite app | unchanged | **not built**; see Left | none | not measured |

`theme_wiring_check.py` is a new fast gate. It passes with 1331 pages wired, 0 not wired and 5 exempt; the exemptions are gate fixtures, preview snapshots and 3D, each named with a reason.

### Contrast

**Pages at rest:** `contrast_audit.py --themes light,dark` measures 73 pages × 1280 and 390 × both themes, which is 292 combinations. Result: **0 failures and 0 page errors.** It stores the choice and reloads the page, with the device preference pinned to the opposite theme. It finishes entrance animations before measuring.

**Interaction states:** `contrast_audit.py --interactions` is new, and registered as the slow gate `contrast_audit_interactions`. It covers the states a pupil reaches only by doing something:
- the KS3 tutor chat, open and with messages;
- the safeguarding boxes;
- all 42 answered-instrument panel pairings;
- flashcards, flipped;
- the leaderboard week chip;
- the Set work toast;
- an older KS4 lesson after checking answers.

Its first run found 13 failures. All are fixed, and it now reads **0 failures in both themes.**

Some light values did change, each because it failed AA in light (the target was 0 failures in light too). Each is listed below with its measurements:

| value | was | now | contrast |
|---|---|---|---|
| `--ks3-autumn-ink` | #4A3410 | #422E0E | 4.37 → 4.80 |
| `--ks3-summer-ink` | #0B4954 | #09414B | 4.21 → 4.72 |

- The two season inks are minted in `ks3_parity.MINTED_TOKENS`.
- KS3's "Commit first…" prompt was amber on cream at 1.38–1.54:1; it is now ink.
- The older KS4 variable symbols move 20% toward the text colour, fixing 4.25:1.
- The KS4 pilot's disabled-control fade and placeholder grey failed in light as well as dark; both are fixed.

Every other light value is byte-identical. The proof, per lane:
- KS3, student, teacher, leaderboard and B2C: pixel diff against the base commit;
- core: token diff;
- pilot: `ks4_parity` layers A–D in light.

Figures on cream plates stay cream in both themes, and the KS3 instrument trays stay their own dark plates.

### The final live audit (Opus) and what it changed

The audit walked every family live, in all three modes, at 1280, 390 and 360, using real keyboard input. It checked the choice across navigation, reload, redirects and tabs, looked for a flash of the wrong theme in the first 60 frames, and read the console.

What passed:
- **Light is the default everywhere,** even with the device set to dark.
- **No flash on any page.**
- System follows the device live, and the choice survives navigation, reload and redirects, and syncs between tabs.
- The keyboard works.
- Nothing scrolls sideways.
- The console is clean.
- Part 2 is correct on all 54 pages.

It found 17 defects, all in Dark or pre-existing, all appearing only after a pupil acts:

| # | defect | severity | outcome |
|---|---|---|---|
| D1 | KS3 tutor chat unreadable (1.15:1) | blocks a pupil | fixed (unit 4) |
| D2 | KS3 safeguarding box (1.11:1) | blocks a pupil | fixed (unit 4) |
| D3 | about 15 KS3 instruments' answer panels went cream-on-cream | blocks a pupil | fixed (unit 4) |
| D5 | flashcards Next button | wrong | fixed (unit 4) |
| D6 | leaderboard week chip | wrong | fixed (unit 4) |
| D7 | Set work toast | wrong | fixed (unit 4) |
| D8 | printing in Dark | wrong | fixed (unit 4) |
| D9 | older-KS4 quiz result | wrong | fixed (unit 4) |
| D10 | "Commit first…" prompt in light | wrong | fixed (unit 4) |
| D11 | pilot control sat in the lesson hero | confusing | moved to the shared header |
| D12 | the classic nav's closed drawer was still Tab-reachable | confusing | now `inert` and `aria-hidden` while closed |
| D13 | Combined spec labels lacked "(8464)" | confusing | fixed |
| D14–D16 | cosmetic | cosmetic | fixed |
| D4 | the KS4 pilot tutor panel is unstyled | pre-existing | left; see Left |
| D17 | flashcards "Reveal" label spacing | pre-existing, cosmetic | left |

Evidence is in `$MRB_SHOTS/audit/` (`AUDIT.md`, `data/`, `shots/`).

### Profile storage: parked, no DDL

`profiles` has no suitable column on production:
- `mode` is the B2C education mode;
- `bench_theme` is the student palette.

So the choice lives in localStorage only, per browser. The migration that would add a column is written, rehearsed on TEST, and parked:

| file | branch | md5 |
|---|---|---|
| `supabase/migrations/20260927010000_profiles_colour_scheme.sql` | `park/profiles-colour-scheme` (`c716db707`, not pushed) | `25d9f624e47e173c4d061e844241d64a` |
| `supabase/rollbacks/20260927010000_profiles_colour_scheme_rollback.sql` | same | `fbd984bbd0cc1b25bb8aac1ae26426f3` |

What it does:
- Adds `profiles.colour_scheme text`, with a check allowing `light`, `dark`, `system` or NULL.
- **Grants `update (colour_scheme)` to `authenticated`.** I found this need while rehearsing: UPDATE on `profiles` is granted column by column, as `bench_theme` is, so without the grant a pupil's save is refused with 42501.

The rehearsal on TEST ran under real RLS as a pupil:

| check | result |
|---|---|
| update own row | 1 row changed |
| update another pupil's row | 0 rows changed |
| set `purple` | refused by the check |

Then the rollback ran. TEST has no `colour_scheme` column now.

Once the migration is applied, `theme.js` needs a small follow-up to read and write the column for signed-in users. It is not wired now, because a request for a missing column would log a 400 on every page.

## Part 2: KS4 pilot polish (live, `d7debf861`, labels completed in unit 4)

**1. Route chip.** The two chips that listed every route are replaced by one chip naming this page's route in words, for example "Triple Science · Higher tier".
- It is a native `<details>` switcher to the same lesson on the other routes that exist. Nanoparticles offers only Triple.
- It opens with the keyboard, and Esc closes it and returns focus.
- Its options are real links baked into the prerendered page.
- "Contains Higher/Triple" appears only on the routes where that content shows (R9 kept).
- It lives in the engine as rulings R11–R12, so all 54 pages and every future lesson inherit it.

Proof:
- `ks4_pilot_check` asserts the chip and that every switcher link exists.
- `ks4_parity` gained a keyboard check and theme checks, and now passes **1514 PASS, 0 FAIL**.
- The Opus audit confirmed it on all 54 live pages.

**2. Exam tips.** The two approved tips are word for word in the fixed tip slot above the ladder (ruling R13). They come from the Triple Higher record, which serves all four routes.

Proof:
- `ks4_parity` compares the rendered tip byte for byte.
- The live `ks4-source.js` carries it.
- The audit confirmed both tips on all four routes.

**3. Spec numbers per route.**

| route | shows | example |
|---|---|---|
| Triple (chemistry) | 8462 section numbers | |
| Triple (physics) | 8463 section numbers | "AQA Physics (8463) 4.2.1.4" |
| Combined | 8464 section numbers, labelled "(8464)" | "AQA Physics (8464) 6.2.1.4" |

The numbers appear in the eyebrow and the key note, and in the tutor's context line. That line was still telling the tutor the Combined number on Triple pages until this run fixed it.
- Every mapping was looked up by heading in the AQA PDFs, including the two extended ranges the builder had inferred. They're in `docs/theme/spec-numbers.md`.
- The audit found no "8464" anywhere on a Triple page.
- Required-practical numbers ("RP15 (Combined) / RP3 (Physics)") are frozen, examined text and are untouched. They name both specs already.

**4. Pupils' KS4 ladder scores reaching teachers: not now (logged).** This comes after Mide has used the pilot with a class for a week. Today the ladder keeps its best score locally and posts nothing, for two reasons:
- `/api/quiz-score` has no key-stage field;
- eight KS4 slugs are byte-identical to KS3 lesson slugs.

It needs a backend change first.

**5. Harness flake (live, `b41a18176`).** `edit_shows_the_questions` polled for a fixed 3.0 s. The Edit sheet's stored questions arrive after `/api/class/current-assignment`, which measured 3.3–4.5 s against a local backend.
- The check now waits up to 20 s for the fetch to finish inside `[data-sw="qlist"]`, either rendered rows or the "Unavailable" tag, and it reports the wait.
- The assertion itself is unchanged.
- **Proof: 10 consecutive full drives green on this check.** The waits were 3.3–4.5 s.

## Landing

Each unit went through the same steps:
1. rebase or merge onto `origin/main`;
2. a full `build_all.py`;
3. `prepush_gate.py --record-all`, for affected gates only;
4. `--check`;
5. push;
6. live proof by bytes and stamps.

### Overrides and flakes

The overrides on the tip commits are all inherited:
- **`figures_mirror`:** the sibling backend checkout has no `figures.json`.
- **`set_work`:** the three standing small-pool reds since MRB-335.

The `set_work` names come from a full-output run each time, never from a truncated one.

Some reds appeared only under concurrent recording load, then passed alone with receipts:
- `verify_ks3`: the headless Chrome connection reset;
- `consumer_flag_off`: 100/100 checks when run alone;
- `teacher_admin_real`: a sign-in crash under load.

### Live proof

After unit 3:
- 33 sample pages, one per family, and all 47 shared assets matched the build byte for byte and carried the snippet;
- `check_ks4_pilot_live.py`: 54 of 54 pages;
- `check_ks3_live.sh`: 185 lessons, on this build's assets.

After unit 4: the same 33 pages + 47 assets byte-equal, 54/54 pilot pages, KS3 185 lessons on
this build's assets. Then an **Opus live re-check** of every fixed defect with its original
repro (`$MRB_SHOTS/audit/RECHECK.md`): 13 of 15 PASS outright (before → now: D1 1.15 → 14.7,
D2 1.11 → 14.27, D3 28/42 pairs failing → 0/42, D5 1.87 → 9.36, D6 1.07 → 15.75, D7 1.05 → 15.75,
D10 1.38 → 14.48, D14 4.35 → 4.84, D15 1.64 → 9.05; D11, D12, D13 (all 54 pages by curl), D16
behaviourally); a regression sweep of 17 live families + 5 fixtures in five theme/OS
combinations clean. It found four residuals, all fixed in unit 5: **N1** KS3 rule-card badge
(2.35:1 dark, 4.49:1 light — pages the first audit never visited), the **D9** remainder (wrong
option + partial result, 4.47:1 dark), **N2** the pilot head ground printing dark, and **N3** the
flashcards gate state that opened nothing (so measured nothing) — it now fails if the deck
does not open. After unit 5 (`11bafaab6`): the same 33 pages and 47 assets byte-equal, 54/54 pilot pages, KS3
on this build (`ks3.css?v=c00fc5b8` live = built). The rule-card badge's registered ink in
`ks3_parity` follows the N1 change (verify_ks3: 778 components, 1991 assertions, all pass).

## Left, with reasons

- **3D Studio (`/3d/`)** has no dark tokens. It has 65 light-only `--st-*` values and hard-coded colours in 9 TSX files, and its header is inside the React app. It is exempt from the wiring gate with that reason. **Estimate: one working day.**
- **The KS4 pilot tutor panel (D4) is unstyled in both themes.** The pilot pages never load `shared/styles.css`. This predates the run (since commit 3b2047b74). **Estimate: 2–3 hours** to give it its own styles and tokens.
- **About 40 more KS3 instrument labels** hard-code `#C6B9A7` in `ks3_art` p3–p9. Most sit on the safe overlay pattern, but none has been individually checked. **Estimate: 1–2 hours.**
- **18 B2C pages** carry the control as a fixed top-right badge rather than in their hand-written headers. Their real content couldn't be checked locally, because with the consumer flag off they show the not-found screen. Put it in each header before the consumer flag goes on. **Estimate: 2 hours.**
- **Profile storage** is parked (above).
- **D17** is cosmetic and pre-existing.
- **N4 is not a theme defect; it is reported for the MRB-351 owner.** Signed out, live `/teacher/decks.html`, `/teacher/flashcards.html` and `/teacher/today.html` stay blank instead of redirecting to `/auth`. Each logs a 401 from the check at `shared/teacher-admin-nav.js:347`. `/teacher/classes.html` redirects correctly. I didn't touch it: it's another session's in-flight work, and nothing in this run changed that check.
- **A wording question for Mide.** Combined pilot eyebrows now read, for example, "AQA Physics (8464) 6.2.1.4". The subject name is Design's; the code is the Trilogy spec's. If "AQA Combined Science (8464) 6.2.1.4" reads better, it's one line in `build_ks4.SPEC_TEXT`.

## Decisions I made

1. **One pre-paint snippet, and `data-theme` always written.** Always writing the attribute switched off the KS4 pilot's device-following for free, because its rule already stands down under `data-theme="light"`. It also gives one selector for dark everywhere.
2. **A native radio group for the control**, not a custom widget. The keyboard and screen-reader behaviour are the browser's own. It needed one change in `focus_audit` (a radio group is one Tab stop), where the two lanes' duplicate fixes had merged into code that would throw on every page.
3. **localStorage only; the profile column is parked.** No suitable column exists. I found and added the column grant while rehearsing.
4. **The migration is parked on its own unpushed branch**, not in `supabase/migrations` on main, so a later `db push` can't apply it by accident.
5. **Built in six lanes** (core, KS3+B2C, runtimes, KS4 pilot, polish, flake), each with its own worktree, under one written contract. I merged the lanes and rebuilt once for each merge.
6. **Part 2 landed before Part 1, as its own unit.** Both touch the pilot header, and landing them separately kept each live proof clean.
7. **Light values changed only where they failed AA in light.** The target was 0 failures in light, and each change is listed with its measurements. Colours outside Design's reference were minted in `ks3_parity`, not slipped through.
8. **The contrast audit measures the real stored-choice path.** It pins the device preference to the opposite theme, finishes animations first, and has an interaction mode, because "0 at rest" proved not to be enough.
9. **The classic nav moves the control into the drawer at 960px and below, and the student bar uses the compact form below 600px.** Both were measured against signed-in pages with the bell showing. The fixtures had hidden the overflow.
10. **The tutor's context line follows the per-route spec numbers,** because "anywhere a section number appears" includes what the tutor is told. Combined pages now carry "(8464)" explicitly.
11. **Left RP numbering alone:** it is frozen, examined text, and already names both specs.
12. **Worksheets and print stay light by design:** paper is light.

## Deviations

- Deviation: a gate (`student_bell_drive`) found that the new control made the classic nav scroll sideways, by 7–42px at 360–430, for signed-in pupils with the bell showing. I moved the control into the menu drawer at 960px and below, and probed 21 widths on 8 pages with no overflow, because the nav's phone breakpoints were already measured to the pixel.
- Deviation: `set_work_drive` found the real student class page at 413px wide on a 390px screen; the fixture had hidden it. I added the compact form of the control for the student top bar, because the page has no drawer to move the control into.
- Deviation: the lanes' "0 at rest" contrast result hid 17 interaction-state defects, which the final audit found. I fixed them all and added `contrast_audit_interactions`, whose first run found 13 more, since fixed. Measuring only pages at rest was the wrong method.
- Deviation: a subagent (the dark-audit fixer) was cut off before its gate sweep and kept re-sending its report. I stopped it, then finished and recorded its sweep myself.
- Deviation: Chrome updated itself mid-session (153 → 154), and headless connections reset under load. I re-ran every affected gate alone; each passed with a receipt.
- Deviation: GitHub dropped the SSH connection while the push hook's 10-minute check ran. I pushed with SSH keepalives instead, never skipping the hook.
- Deviation: disk fell to 2.5 GB free. I removed seven merged, idle worktrees (checked for live processes first; a live session's worktree was kept), killed four orphaned headless Chromes by PID after checking their profile folders were this run's, and deleted this run's screenshot scratch.
- Deviation: the dark-audit fixes had to be merged with two other sessions' landings (MRB-351
  and "Set from class") that reached main mid-run → merged, rebuilt, re-ran every affected
  gate and both contrast audits on the merged tree before each push → one session's work must
  never ship over another's untested.
- Deviation: the Opus re-check found the new interaction gate's flashcards state had measured
  nothing (N3) → it now fails if the deck does not open → a gate that passes by not looking is
  the failure this run kept meeting.

