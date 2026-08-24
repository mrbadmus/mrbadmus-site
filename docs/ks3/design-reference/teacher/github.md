repo: mrbadmus/mrbadmus-site
branch: main
path: teacher

## Last sync
date: 2026-08-20T11:40:00Z

### Updated in this project
- Class detail gained a week bar: twelve teaching weeks, hairline-separated, with arrows at both ends; the current week is marked "This week" and the rail opens on the selected week. Picking one re-scopes tiles, the roster column and the assignment tables.
- Class history extended from 4 to 12 assignment weeks, dates generated from the term rather than hardcoded.
- Rebuilt the teacher dashboard as one clickable prototype on the studio (`--st-*`) cream system.
- Class cards now show code, year + key stage, submissions this week and last activity only — no tier/pathway.
- Subject label derived from the class code: KS3 `/Sc` → Science, KS4 `/Sc` → Combined Science, `/Ph` `/Ch` `/Bi` → the separate science.
- Added quick-assign (Set work), weekly digest / printable class report, cross-class student search and bulk shoutouts.

## Screen map
| Project screen | Repo files |
| --- | --- |
| My classes (landing) | teacher/classes.html, shared/teacher-data.js |
| Class detail | teacher/class-detail.html, shared/shoutouts.js |
| Student detail | teacher/student-detail.html |
| Assignment / marking | teacher/class-detail.html, supabase/migrations/20260818231201_assignment_questions.sql |
| Set work | supabase/migrations/20260509073615_add_assignment_day_of_week.sql |
| Shoutouts (single + bulk) | shared/shoutouts.js, teacher/class-detail.html |
| Import students (CSV) | teacher/import.html, supabase/functions/roster-import/index.ts |
