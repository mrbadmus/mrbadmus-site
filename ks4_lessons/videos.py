#!/usr/bin/env python3
"""ks4_lessons/videos.py — the KS4 lesson-video manifest, keyed by SITE slug.

`Ks4Video` (docs/ks4/design-reference/pilot/.../Ks4Video.dc.html) renders
nothing when `window.KS4.VIDEOS[slug]` has no `src` — true for all 14 lessons
today, and that empty state is itself one of the 14 lessons' shipped states
(NOTES-KS4-pilot.md §4 "the empty state renders nothing (all 14 lessons
today)"). This file exists so that turning a video on later is a data change
here, not a page rebuild of any kind beyond re-running build_ks4.py.

⚠️ Keyed by SITE slug, not by whatever string a lesson's own `const slug = …`
happens to hold. Three lessons' internal slug differs from the site slug
(metals-alloys / series-parallel-circuits / resistors — see ks4_rulings.py
R-SLUG) and `ks4_rulings.py` rewrites `const slug = …` to the site slug as
part of the same ruling that fixes `KS4.find`/`KS4.bank`/`KS4.tip`, so by the
time `K.video(slug)` runs on a compiled page, `slug` IS the site slug and this
dict's keys line up without a second alias table.

Shape, from Ks4Video.dc.html's own prop type and NOTES-KS4-pilot.md §4:

    VIDEOS[slug] = {
        "src": "https://…",       # required; a falsy value = "no video"
        "poster": "https://…",
        "captions": "https://….vtt",
        "title": "…",
        "duration": "4:12",
        "transcript": ["paragraph one", "paragraph two", …],
    }
"""

VIDEOS = {}
