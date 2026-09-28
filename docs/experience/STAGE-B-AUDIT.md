# Stage B audit runbook — the pupil phone pass on TEST

For the Stage B auditor. Everything here runs against the **TEST** Supabase
project (`qeppkiswvclkkwbxmlok`); nothing touches production.

## 1. Start a backend and serve the site

The backend's CORS allowlist is `mrbadmus.com`, `localhost:3000` and
`localhost:5500`, so the site must be served on **5500**.

```bash
# a backend at origin/main, on its own port (its .env is the TEST project)
cd /path/to/mrbadmus---backend && git fetch && git worktree add --detach /tmp/be origin/main
cp .env /tmp/be/.env && cd /tmp/be && npm ci && PORT=3401 node server.js &
# the built site
cd /path/to/mrbadmus-site/mrbadmus_site && python3 -m http.server 5500 &
```

Every URL below carries `?env=test&api=http://localhost:3401`
(written `?Q` below).

## 2. Pupils

- **Pupil A** `mrb326_pupil_a@throwaway.test`: class 7z/Sc9, one open set
  (Forces, 15 questions), flashcard homework, unread reminders (bell 9+).
- **Pupil B** `mrb326_pupil_b@throwaway.test`: same class. It has open work
  on TEST today, so the **empty bench** state is not reachable with real
  data. To see it, either close B's open work on TEST or use the harness
  in the Stage B builder's scratch `bn.py`, which runs `drawBenchNext`
  against the live bench frame for the missed / practice / lesson cases.

Sign in without touching a password: mint a session from a magic link with
the TEST service key (`/auth/v1/admin/generate_link` → `/auth/v1/verify`)
and plant it with `student_bell_drive.plant()`. Never set
`MRB_DRIVE_PASSWORD` or `MRB_TEST_STUDENT_PASSWORD`.

## 3. The walk (390×844, then 360×780; light, then dark)

1. `/student/classes.html?Q`: bar = brand · bell · avatar · theme, one row.
2. `/student/class.html?Q` as A: no crumb strip; "Welcome back, NAME"; four
   stats; bench = docket (QUESTIONS, DUE) + topic + "Open the assignment" +
   "0 OF 15 ANSWERED"; no checklist, no Practice button, no "3 days left".
3. The same as B: the same today (see §2), or the fallback card.
4. "Open the assignment" → question 1: bar one row (‹ brand 7z/Sc9 · bell ·
   avatar · theme), the clock in the progress strip, no ANSWERED readout.
5. Answer to question 2, then Back: the question number is the only counter.
6. Hand in → results: eyebrow, h1, score fraction, marks row, WRONG /
   MISSED / TIME TAKEN, "Where it went wrong", buttons. No 70%, no MARKED
   kicker, no "03 OF 10", no header clock.
7. The bar's back button (‹ 7z/Sc9) → the class page (not /ks3/).
8. Class → the flashcards card → overlay title "Flashcards".
9. `/ks3/biology/cells-and-organisation/animal-and-plant-cells.html?Q`:
   one row, "‹ Cells and organisation" → the unit index; avatar menu:
   My class · Settings · Sign out. Signed out: brand · title · Sign in · theme.
10. `/combined/higher/chemistry/bonding/ionic-bonding.html?Q`: one row;
    the title → `/combined/higher/chemistry/bonding.html`.
11. `/leaderboard.html?Q`: one row, no title.
12. Bell → the panel lists messages; avatar → Settings → settings page
    (its menu hides Settings); Sign out → `/auth.html?env=test`.

Pass bar: every header ≤64px and one row, no sideways scroll, nothing
repeated on a screen, contrast fine in dark.
