# Monday 14 September 2026 — 07:30 checklist

Rainford's automatic weekly work starts today. Nothing runs on a timer.
**Each class's week-3 work is composed the first time one of its pupils opens
their class page today** (from 01:00 UK, see the note under 1), and it stays for
the week. So at 07:30 most classes will show nothing yet, and that is normal.

For each line: what to open · what it should show · what wrong looks like · the
ONE reversible action. None of the actions needs Code.

## 1. The hold — Teacher → Admin → Assignments

- **Should show:** `Assignments are running normally — they started on 14 Sep 2026.`
- **Wrong looks like:** `Automatic weekly work is on hold until …` with a date after today, or the card blank.
- **Action:** tap **Start now** (sets the date to today).
- ⚠️ **Start now / Save may answer** `Could not check your access.` That route needs the backend's `SUPABASE_ANON_KEY`, which MRB-335 recorded as absent from the Render environment (reading the card does not need it; only saving does). If you see that message: Render → mrbadmus-backend → Environment → add `SUPABASE_ANON_KEY` = the production anon key (the same public key every page carries), save, wait for "Live" (~2 min), retry. No code changes. Fallback: Supabase SQL editor (production), `update schools set assignments_open_from = current_date where name = 'Rainford High School';`.
- **Note on 00:00–01:00:** the hold compares the UTC date, so between midnight and 01:00 UK on the 14th a pupil still sees "not live yet". Self-clears at 01:00. Nothing to do.

## 2. A class with pupils — Teacher → My classes → 7h/Sc5 (or any class you teach with auto on)

- **Should show (once a pupil has opened their page):** one card, slot A, titled `Cells and organisation · Describing motion · Particles and their behaviour` (Year 7; other years differ), `0 of N in`, due **Thu 17 Sep 18:00**. Assignments table: one **Open** row, source automatic, no Edit/Delete on it.
- **Should show (before any pupil has opened):** no automatic card yet; the table has no week-3 row. Normal.
- **Wrong looks like:** a pupil has opened their page and the class still shows nothing; or the pupil's page says `This week's work isn't live yet`.
- **Action:** check line 1 first (the hold). If the hold reads correctly, that class's own dial: class page → **Automatic weekly work: on** — if it is off, switch it on (the next pupil read composes). The reverse also holds: to STOP a class getting automatic work, switch it off; work already composed stays (the switch never retracts).
- **Optional positive check using only dials:** on **8r/Sc1** switch **Automatic weekly work** ON, open the class page as your test pupil — the week-3 card appears within a second — then switch it OFF again. The row stays for the week; nothing else is affected.

## 3. Your test pupil — 8r/Sc1 pupil class page

- **Should show:** the teacher-set work you left there (auto is OFF on 8r/Sc1, so no automatic card). No "isn't live yet" line beside live work.
- **Wrong looks like:** `This week's work isn't live yet` with nothing else, or an empty bench with live sets only in the list below.
- **Action:** nothing here is Monday-critical; it is the sandbox. Note it and carry on.

## 4. The reminders banner and the bell — pupil page

- **Should show:** no banner unless a teacher has pressed **Remind all** for that pupil today; the bell shows a count only for unread reminders, feedback, shoutouts and **New work** (teacher-set only — automatic work never rings the bell, by design).
- **Wrong looks like:** a banner or bell item naming work that is deleted or not yet released.
- **Action:** none available on the page; it is read-only. Report which class and pupil.

## 4b. ⚠️ The fifteen separate-science classes will show NOTHING this week — expected

Shipped Sat 12 Sep (MRB-341). Until now a triple class was composed all three
sciences: `10h/Ph1`, a physics class, was getting eight of its fifteen questions
from biology and chemistry, and its set was byte-identical to the combined
classes'. It now draws its own science only.

**The consequence for THIS WEEK, and only this week:** at week 3 a class's own
science has three lessons behind it, which is twelve questions in the pool
against a set size of fifteen. Short sets are not allowed outside week one, so
these classes compose nothing and their pupils' pages say
`No work has been set for this week yet.` **That is correct, not broken.**
From **Sunday 20 September (week 4)** there are four lessons, sixteen
questions, and they compose normally with no action from anyone.

- **Should show:** no automatic card on these fifteen classes; pupils see "no
  work set yet"; teacher-set work is unaffected and appears as normal.
- **Wrong looks like:** one of these classes showing an automatic card whose
  title names a science it is not taught (e.g. `10h/Ph1` titled
  `Cell Biology · …`). That would mean Render is still serving the old build —
  check `https://mrbadmus-backend.onrender.com/api/health`, whose `build` field
  should read `8217010…`.
- **Action:** tell those fifteen teachers to set this week's work by hand. The
  Set work sheet already scopes correctly to their subject, so it is the normal
  three taps. Nothing to switch, nothing to reverse.

10A/Bi1 · 10D/Bi1 · 10r/Ch1 · 10r/Ch3 · 10h/Ph1 · 10r/Ph2 · 10r/Ph3 ·
11A/Bi1 · 11D/Bi1 · 11h/Ch1 · 11r/Ch1 · 11r/Ch3 · 11h/Ph1 · 11r/Ph1 · 11r/Ph2
(379 pupil-places; all higher tier, all auto on.)

**One decision waiting on you** (READINESS.md §5, MRB-341): allow these classes
a SHORT twelve-question set in week 3 instead of nothing? Twelve right-subject
questions beats none, week one is already allowed to be short, and it is one
condition in the composer. Say the word Monday morning and it ships that
evening. It stops mattering after this week either way.

## 5. The leaderboard — /leaderboard.html

- **Should show:** the KS4 weekly challenge board on its own week (it keeps KS4's Friday clock, not the Sunday teaching week). On a first week with no scores the board is empty rows with `—` tiles, which is correct, not broken; a `LOADING` cut line that never resolves is the failure.
- **Action:** none; the leaderboard has nothing to do with assignments. Report it.

## 6. The 21 classes with no pupils

Nothing composes for them and nobody can open them: the route needs a pupil or a
class teacher, and 20 of the 21 have neither. (`11B/Bi1` has one teacher and no
pupils; if that teacher opens the pupil page nothing composes for anyone else.)
These fill as rosters are imported — no Monday action. Names are in READINESS.md.

## If in doubt

Every action above is a dial that composes or stops composing FUTURE work; none
of them deletes anything a pupil can already see. Nothing on this page needs a
push, a build, or a migration.
