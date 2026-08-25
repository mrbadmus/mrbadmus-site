# KS4 Weekly Leaderboard

Open `KS4 Weekly Leaderboard.dc.html` in a browser. Keep the folder structure intact —
the page loads `support.js` and the design-system tokens, fonts and bundle from `_ds/`.

Contents
- `KS4 Weekly Leaderboard.dc.html` — the design (markup + logic in one file)
- `support.js` — runtime needed to render it
- `_ds/mrbadmusai-design-system-…/` — MrBadmusAI tokens, self-hosted fonts, component bundle

Board rule: ranks 1–3 on the podium, ranks 4–10 in the table. Nothing below rank 10 is
listed; a viewer outside the top 10 sees only their own standing.

Tweaks: `topCount` (board size, default 10), `density`, `showPodium`, `showWeekTops`.
