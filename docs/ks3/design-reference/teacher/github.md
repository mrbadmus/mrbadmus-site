repo: mrbadmus/mrbadmus-site
branch: main
path: teacher

## Last sync
date: 2026-08-31T00:00:00Z

### Updated in this project
- Timetable upload flow added (Today → Upload timetable): CSV / MIS export (SIMS, Arbor, Bromcom) or photo, lessons auto-matched to classes by class code, unmatched codes flagged for a manual pick. BACKEND NEEDED: a roster-import-style edge function + a timetable table (teacher, day, period, time, class_id); the Today screen derives its lesson list from it.
- Reminders ("Remind all" on the class screen, "Send reminders" on Today) assume automated delivery. BACKEND NEEDED: a scheduled job that messages every student without a submission on the open assignment (email/push, school-safe templates), plus rate-limiting so a student isn't nudged twice in a day.
- v3 rebuilt around the teacher's day: new "Today" landing (timetable with a walk-in-knowing line per lesson, students-to-chase, reteach and setup triage), class screen now answers chase / reteach / watch above the fold, week rail dropped in favour of a dated assignment table with weakest-question column.
- Class detail gained a week bar: twelve teaching weeks, hairline-separated, with arrows at both ends; the current week is marked "This week" and the rail opens on the selected week. Picking one re-scopes tiles, the roster column and the assignment tables.
- Class history extended from 4 to 12 assignment weeks, dates generated from the term rather than hardcoded.
- Rebuilt the teacher dashboard as one clickable prototype on the studio (`--st-*`) cream system.
- Class cards now show code, year + key stage, submissions this week and last activity only — no tier/pathway.
- Subject label derived from the class code: KS3 `/Sc` → Science, KS4 `/Sc` → Combined Science, `/Ph` `/Ch` `/Bi` → the separate science.
- Added quick-assign (Set work), weekly digest / printable class report, cross-class student search and bulk shoutouts.

## Screen map
| Project screen | Repo files |
| --- | --- |
| Today (landing) | teacher/classes.html, shared/teacher-data.js |
| My classes | teacher/classes.html, shared/teacher-data.js |
| Class detail | teacher/class-detail.html, shared/shoutouts.js |
| Student detail | teacher/student-detail.html |
| Assignment / marking | teacher/class-detail.html, supabase/migrations/20260818231201_assignment_questions.sql |
| Set work | supabase/migrations/20260509073615_add_assignment_day_of_week.sql |
| Shoutouts (single + bulk) | shared/shoutouts.js, teacher/class-detail.html |
| Import students (CSV) | teacher/import.html, supabase/functions/roster-import/index.ts |
