# Teacher dashboard redesign — MrBadmusAI

A clickable prototype of the teacher side of MrBadmusAI, rebuilt on the studio (`--st-*`) cream
system from the bound MrBadmusAI design system. One file, seven screens, real navigation.

## Open it

Open `Teacher Dashboard.dc.html` in a browser. Keep the folder intact — the page loads
`support.js` (runtime) and the design system from `_ds/…/` (tokens, fonts, component bundle).
Moving the HTML out on its own will strip its fonts and colours.

## What's in the box

| File | What it is |
| --- | --- |
| `Teacher Dashboard.dc.html` | The whole prototype — markup, logic and seeded data |
| `support.js` | Component runtime the page loads |
| `_ds/mrbadmusai-design-system-…/` | Bound design system: tokens, self-hosted fonts, component bundle |
| `github.md` | Link to the source repo (`mrbadmus/mrbadmus-site`) + screen → file map |
| `uploads/` | The four screenshots of the current teacher UI this redesign started from |

## Screens

1. **My classes** — 12 class cards, every class equal weight. Each card carries class code,
   year + key stage, submissions this week and last activity. Filters (All / KS3 / KS4), sort
   by code or most missing. Actions: Set work, Weekly digest, Import students.
2. **Class detail** — a week bar (twelve teaching weeks, oldest to newest, hairline-separated date
   ranges with arrows at both ends, the current week marked "This week") scopes the page; four headline tiles, students table (the
   selected week, avg, last active, needs a look), assignments split Upcoming / Marked with the
   selected week's row marked "Viewing", shoutout composer and feed.
3. **Student detail** — tiles derived from the submission rows below them, full history.
4. **Assignment / marking** — question breakdown by skill with the lowest scoring question
   flagged, plus a class × question grid (filled dot correct, ring incorrect, dash not attempted).
5. **Charts** — six chart kinds, either scope (all classes / one class), regenerating on pick:
   submissions, class means, score spread, on time, question difficulty, engagement.
6. **Weekly digest / class report** — printable. Digest lists every class; "Print report" from a
   class scopes the whole document to that class's assignments.
7. **Import students (CSV)** — upload, column mapping, row check with warnings.

Sheets: Set work (topic → questions/due/release → multi-class), bulk shoutouts, and a
`/`-key style student search across all classes.

## Rules the design follows

- **Subject label comes from the class code, not tier.** KS3 `/Sc` → Science, KS4 `/Sc` →
  Combined Science, `/Ph` → Physics, `/Ch` → Chemistry, `/Bi` → Biology. Tier and pathway are
  deliberately absent. Multi-subject labels carry a three-hue pip (blue / orange / green),
  separates carry a single dot — colour is never the only signal.
- **Design system, not invention.** Cream ground `--st-ground`, paper cards, Bricolage Grotesque
  600 for display, Instrument Sans for UI, DM Mono for eyebrows and numerals. `--st-accent` is
  graphic-only; small orange text is `--st-accent-text`. Arrows, ticks and crosses are drawn as
  inline SVG (the font subsets don't carry those glyphs).
- **Copy is terse and functional** — no reassurance copy, no platform meta-text.
- **One number, one source.** Each class has a single seeded score matrix (student × paper,
  marks out of 8). A student's average is the mean of their row, a paper's mean is the mean of
  its column, the class mean is the mean of the marked columns, the digest mean is the mean of
  the class means, and the question grid is built from the same marks. No two screens can
  disagree, and open work (not yet due) is never counted as late or judged as finished.
- **The term is twelve weeks deep.** Each week owns one assignment (set Wednesday, due the
  next), so a teacher can step back to 1–5 Jun and every screen still adds up.
- **Past weeks read the same matrix.** Switching to an earlier week re-derives the tiles
  (submitted, week mean and its gap to the term average, on time, not submitted) and the roster
  column from that paper's marks — a past week can't disagree with the term view. Classes with
  no work set have no week bar.
- **Empty states are states, not blanks.** A class with no roster reads "No students yet" with an
  Import action; a class with students but no work set has its own detail-page state.

## Data

All data is generated, seeded and deterministic — the same class always produces the same
students and scores. Realistic mix: 8 live classes, 1 with students but no work set, 3 awaiting
a roster; 227 students on roll; 12 weeks of assignments per live class.

## Tweaks

Teacher name · card meter (bar or numbers) · hide empty classes · table density.

## Not built

Live data, auth, real CSV parsing, and the KS4 vs KS3 content targeting the repo leaves as a
future column. Shoutout templates dropped their emoji to fit the design system — say the word
if they should come back.
