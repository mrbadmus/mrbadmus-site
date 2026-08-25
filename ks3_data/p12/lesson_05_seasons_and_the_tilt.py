"""P12 L5 — Seasons and the tilt (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p12/p12-05-seasons-and-the-tilt.dc.html`.

Her page wins outright. The January hook, the four dates, the three places
and all four rungs are hers.

── ⚖️ THE BENCH IS REAL ASTRONOMY, AND THE ARITHMETIC IS PORTED EXACTLY

Solar declination is 0° at the equinoxes and ±23.44° at the solstices.
Daylight comes from the standard sunrise equation — the hour angle is
`acos(−tan(latitude) × tan(declination))`, doubled and divided by 15 to
give hours. Noon altitude is `90 − |latitude − declination|`. Energy per
square metre is the sine of that altitude, which is the beam-spreading
argument the lesson is built on, done with a number.

**London on 21 June comes out at 16.5 hours and 61°, which is right**, and
those two figures are asserted by the unit's content-truth check rather
than taken on trust. Her legal line records what the model leaves out:
atmospheric refraction and the finite width of the Sun's disc, both of
which lengthen real daylight by several minutes, and absorption and
scattering on the intensity.

── ⚖️ THE SEASON VERDICT IS DERIVED FROM THE ANNUAL SWING, WHICH IS A
   FIX ───────────────────────────────────────────────────────────────

Design's verdict is `h > 13 || a > 60`, and at the equator the noon Sun
clears 60° on **every one of her four dates**. So her bench prints *"That
is summer."* at the equator in March, June, September and December — which
contradicts her own explainer three paragraphs above it: *"places on the
equator — where the Sun is high all year and the day is close to twelve
hours all year — barely have seasons at all."*

The quantity that actually decides it is the SWING between the two
solstices at that latitude: 0.0 hours at the equator, 4.5 at Sydney, 9.0
at London. Under one hour of swing there is no summer and no winter to
name, and the bench says so. Four verdicts now cover twelve reachable
states and every one of them is true. 5A.1's rule about comparatives,
applied to the one place on this page where it was broken. Registered in
`DEPARTURES-P12.md`.

── ⚖️ `#s-think` IS THE THIRD RAIL STOP, ON HER OWN PREDICATE ────────

Same shape as `p12-03` and `p12-04`, and the same `space-think` family.
See `ks3_data/p12/__init__.py`.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

This lesson takes indices **1 and 3**. Her option TEXT and every
correction are verbatim; only the ORDER moves.

── ⚠️ MRB-177 · TWO LENGTH TELLS, BOTH REMEDIED AT THE DISTRACTOR ────

Rung 1's correct option is 34 words against a longest distractor of 11,
and rung 2's is 25 against 12. Every distractor on both rungs is FINISHED
into a complete wrong rule; neither correct answer is touched and no
correction is edited.

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ──────────────────────
"""

LESSON = {
    "slug": "seasons-and-the-tilt",
    "title": "Seasons and the tilt",
    "discipline": "physics",
    "unit": "Space",
    "family": "MODEL",

    "covers": ["KS3.P.SPACE.03"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["the-sun-stars-and-galaxies"],
    "assumes": [],
    "references": [{"unit": "P1", "lesson": "radiation"}],
    "ks4_links": [],

    "meta_description": "Seasons come from a 23.4° tilt that never moves, "
                        "not from the distance to the Sun — which is smallest "
                        "in the northern winter.",

    "big_question": "The Earth is five million kilometres closer to the Sun "
                    "in January than in July, and January is the cold one. "
                    "Whatever causes seasons, it is not how far away we are.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Closer in January",    "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Four dates, three places",
         "done_when": "gate_and_a_control"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "It is not the distance",
         "done_when": "hook_or_first_rung"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",       "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "We are closest to the Sun in the first week of January.",
        "prompt": "The Earth’s orbit is very slightly oval. It reaches its "
                  "closest point — about 147 million km — around 3 January, "
                  "and its furthest — about 152 million km — in early July.",
        "commit": "So what causes summer?",
        "options": [
            "Summer happens when the Earth is closest to the Sun",
            "Summer happens when your half of the Earth is tilted towards the "
            "Sun",
            "Summer happens when the Earth spins more slowly",
            "Summer happens when the Sun gives out more energy",
        ],
        "answer": 1,
        "reveal": "When your half is tilted towards the Sun. The Earth is "
                  "actually about 5 million km closer to the Sun in early "
                  "January — northern midwinter — than in early July, so "
                  "distance cannot be the answer, and in any case it is "
                  "summer in Australia while it is winter here. What changes "
                  "is the tilt: 23.4° of it, fixed in direction, so that for "
                  "half the year one hemisphere leans sunwards and for the "
                  "other half it leans away.",
    },

    "misconceptions": [
        {"id": "SPACE-15",
         "statement": "It is summer when the Earth is closer to the Sun.",
         "elicited_by": "s-hook",
         "confronted_by": "think-not-the-distance"},
        {"id": "SPACE-16",
         "statement": "The Earth’s tilt changes through the year, leaning "
                      "towards the Sun in summer and away in winter.",
         "confronted_by": "think-not-the-distance"},
        {"id": "SPACE-17",
         "statement": "It is the same season everywhere on the Earth on the "
                      "same date.",
         "elicited_by": "bench",
         "confronted_by": "bench"},
        {"id": "SPACE-18",
         "statement": "A high Sun warms the ground more because it is closer "
                      "to it.",
         "elicited_by": "s-ladder",
         "confronted_by": "bench"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "The Earth’s axis is <strong>tilted by about 23.4°</strong> "
                 "away from upright, and that tilt keeps pointing in the same "
                 "direction in space all year round. It does not wobble to "
                 "follow the Sun. What changes is where the Earth is in its "
                 "orbit, and therefore which hemisphere the fixed tilt "
                 "happens to be leaning towards."},
        {"type": "explainer",
         "text": "When your hemisphere leans towards the Sun, two things "
                 "happen together. The Sun is above the horizon for longer, "
                 "so there are more hours of warming. And it climbs higher at "
                 "noon, so its light strikes the ground more squarely and the "
                 "same beam is concentrated onto a smaller patch. More hours "
                 "and stronger sunlight is summer."},
        {"type": "explainer",
         "text": "Six months later the Earth is on the other side of its "
                 "orbit, the same unchanged tilt now leans the other way, and "
                 "both effects reverse. This is also why the two hemispheres "
                 "always have opposite seasons, and why places on the equator "
                 "— where the Sun is high all year and the day is close to "
                 "twelve hours all year — barely have seasons at all."},

        # ── #s-bench · four dates in the orbit, three places ───────────
        {"type": "space-bench",
         "id": "bench",
         "anchor": "s-bench",
         "eyebrow": "At the bench · four dates in the orbit, three places on "
                    "the Earth",
         "heading": "Same Sun, same year, three different experiences of it.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Pick a date and a place. The tilt never changes and the Sun "
                 "never changes — everything on this bench follows from which "
                 "way your part of the Earth happens to be leaning.",
         "model": "seasons",
         "gate": {
             "prompt": "Commit first. It is 21 June. What is happening in "
                       "Sydney?",
             "options": [
                 "Midsummer, like everywhere else on that date",
                 "Midwinter, because the southern hemisphere is tilted away",
                 "Spring, because seasons run three months late there",
                 "Nothing special — Sydney is too close to the equator to "
                 "have seasons",
             ],
             "answer": 1,
         },
         "tabs_label": "Date in the orbit",
         "start_tab": 1,
         "tabs": [
             {"id": "mar", "label": "21 March", "name": "21 March",
              "dec": 0, "season": "equinox"},
             {"id": "jun", "label": "21 June", "name": "21 June",
              "dec": 23.44, "season": "June solstice"},
             {"id": "sep", "label": "23 September", "name": "23 September",
              "dec": 0, "season": "equinox"},
             {"id": "dec", "label": "21 December", "name": "21 December",
              "dec": -23.44, "season": "December solstice"},
         ],
         "slider": {
             "id": "lat",
             "label": "Where you are standing",
             "value_label": "{label}",
             "start": 2,
             "values": [
                 {"id": "sydney",  "label": "Sydney, 34° S",   "lat": -34},
                 {"id": "equator", "label": "The equator, 0°",  "lat": 0},
                 {"id": "london",  "label": "London, 52° N",    "lat": 52},
             ],
         },
         "bars_caption": "What the tilt does at each of the three places, on "
                         "this date",
         "bars_alt": "Daylight length at three places on {date}: {list}. "
                     "{place} is highlighted.",
         "bars": [
             {"id": "sydney",  "label": "Sydney, 34° S"},
             {"id": "equator", "label": "The equator, 0°"},
             {"id": "london",  "label": "London, 52° N"},
         ],
         "readouts": [
             {"id": "date",     "label": "Date"},
             {"id": "daylight", "label": "Daylight"},
             {"id": "noon",     "label": "Sun at noon"},
             {"id": "energy",   "label": "Energy per square metre"},
         ],
         "words": {
             "date_sub":     "in the orbit",
             "daylight_sub": "out of 24",
             "noon_sub":     "straight up would be 90°",
             "energy_sub":   "of what a Sun overhead would give",
             "bar_value":    "{h} h of daylight",
             "bar_sub":      "Sun reaches {a}° at noon",
             # ⚠️ FOUR VERDICTS, AND THE FOURTH IS THE FIX. Design has three
             # and the equator falls into the wrong one on all four dates.
             "verdict_summer":  "That is summer.",
             "verdict_winter":  "That is winter.",
             "verdict_between": "That is a season in between.",
             "verdict_even":    "That is neither summer nor winter: this "
                                "close to the equator the day barely changes "
                                "length all year and the Sun is always high, "
                                "so there is no seasonal swing to name.",
             "list_join":       "and",
         },
         "notes": {
             "season": "On {date} at {place} the Sun is up for {h} hours and "
                       "climbs to {a}° at noon. Two things follow from that "
                       "and both point the same way: the longer the Sun is up "
                       "the more hours it has to warm the ground, and the "
                       "higher it climbs the more concentrated its light is — "
                       "the same beam spread over a smaller patch. At {a}° "
                       "each square metre of ground receives about {pct}% of "
                       "what it would get with the Sun straight overhead. "
                       "{verdict} Change the date and the tilt has not moved "
                       "at all — the Earth has simply travelled to the other "
                       "side of its orbit, so the same fixed lean now points "
                       "the other way.",
         }},

        {"type": "key-fact", "ref": "seasons-come-from-the-tilt"},

        {"type": "misconception", "id": "think-not-the-distance",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-not-the-distance",
         "kind": "space-think",
         "demand": "explain",
         "targets": "SPACE-15",
         "statements": [
             {"quote": "It is summer when the Earth is closer to the Sun.",
              "targets": "SPACE-15",
              "body": [
                  "The Earth is closest in early January, which is midwinter "
                  "in the northern hemisphere and midsummer in the southern. "
                  "One distance, two opposite seasons — so distance cannot be "
                  "the cause. The variation is about 3% anyway, which is far "
                  "too small to produce the difference between a January and "
                  "a July in Britain. The idea survives because it sounds "
                  "sensible and because nobody ever checks the date.",
              ]},
             {"quote": "The Earth’s tilt changes through the year, leaning "
                       "towards the Sun in summer and away in winter.",
              "targets": "SPACE-16",
              "body": [
                  "The axis holds an almost constant direction in space — it "
                  "currently points at Polaris, which is why that star sits "
                  "nearly still while the rest of the sky wheels around it. "
                  "The tilt does not move; the Earth does. In June the planet "
                  "happens to be on the side of its orbit where that fixed "
                  "northward lean points sunwards, and in December it is on "
                  "the opposite side, where the same fixed lean points away.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "seasons-come-from-the-tilt",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Seasons are caused by the Earth’s 23.4° axial tilt, which "
                 "stays pointing the same way as the Earth orbits. The "
                 "hemisphere leaning towards the Sun gets longer days and a "
                 "higher noon Sun, so each square metre receives more energy. "
                 "Distance from the Sun has nothing to do with it — the two "
                 "hemispheres have opposite seasons at the same distance."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 1 and 3.
    #
    # ⚠️ MRB-177 · EVERY DISTRACTOR ON BOTH MARKED RUNGS IS FINISHED into a
    # complete wrong rule. Neither correct answer is touched and no
    # correction is edited.
    "ladder": {
        "recall": {
            "q": "The Earth is closest to the Sun in early January. Why is "
                 "that not the reason for summer?",
            "options": [
                "Because the difference in distance is far too small to "
                "measure, and an effect nobody can measure cannot cause "
                "anything a person is able to feel from one month to the "
                "next.",
                "Because it is winter in the northern hemisphere in January "
                "and summer in the southern one at the same time — distance "
                "is the same for both, so it cannot be what causes seasons.",
                "Because the Earth’s orbit is a perfect circle, so the "
                "distance to the Sun is the same on every day of the year.",
                "Because the Sun gives out less energy in January, and that "
                "drop is what cancels out the effect of being closer.",
            ],
            "answer": 1,
            "feedback": {
                0: "It is about 5 million km, which is measurable. The reason "
                   "it is not the cause is that it applies to the whole "
                   "planet at once.",
                2: "It is very slightly elliptical, which is why the distance "
                   "changes at all. That change is not what makes seasons.",
                3: "The Sun’s output is very nearly constant. The change is "
                   "in how our part of the Earth is angled.",
            },
            "title": "Rung 1 · Read the model"},
        "apply": {
            "q": "Why does a high Sun warm the ground more than a low one, "
                 "even for the same length of time?",
            "options": [
                "A high Sun is closer to the ground than a low one, and a "
                "closer source always delivers more energy to a surface.",
                "A high Sun gives out more energy than a low one, because the "
                "Sun radiates hardest straight downwards.",
                "A low Sun is blocked by clouds more often, so less of its "
                "light gets through to warm anything.",
                "The same beam of sunlight is spread over a smaller patch of "
                "ground when the Sun is high, so each square metre receives "
                "more energy.",
            ],
            "answer": 3,
            "feedback": {
                0: "The change in distance to the Sun across a day is nothing "
                   "— a few thousand kilometres out of 150 million.",
                1: "It is the same Sun, giving out the same amount. What "
                   "changes is the angle the light arrives at.",
                2: "Light does pass through more atmosphere at a low angle, "
                   "which absorbs a little. The main effect is the beam being "
                   "spread over a larger area.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why the UK has summer in June and Australia has "
                 "summer in December, using the tilt.",
            "field_label": "Your explanation",
            "placeholder": "The Earth’s axis is tilted by about 23.4°, and…",
            "success": [
                "Says the axis is tilted by about 23.4 degrees.",
                "Says the tilt keeps pointing the same way in space as the "
                "Earth orbits.",
                "Says in June the northern hemisphere leans towards the Sun "
                "and the southern leans away.",
                "Says in December the situation is reversed.",
                "Says the leaning hemisphere gets longer days and a higher "
                "noon Sun, which is what makes it summer.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Inside the Arctic Circle the Sun does not set for weeks in "
                 "summer, and does not rise for weeks in winter. Explain why, "
                 "and predict what the seasons would be like if the Earth had "
                 "no tilt at all.",
            "field_label": "Your answer",
            "placeholder": "Near the pole the tilt means…",
            "success": [
                "Says that near the pole the tilt can keep a place in "
                "sunlight through a whole rotation.",
                "Says the same tilt keeps it in darkness through a whole "
                "rotation six months later.",
                "Says the Arctic Circle marks the latitude where this first "
                "happens, at about 66.5°.",
                "Predicts that with no tilt every place would have twelve "
                "hours of daylight every day of the year.",
                "Predicts there would be no seasons — just a permanent "
                "climate set by latitude alone.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "The Earth’s axis is tilted about 23.4° and keeps pointing "
                "the same way in space throughout the year. As the Earth "
                "orbits, first one hemisphere and then the other leans "
                "towards the Sun. The leaning hemisphere gets more hours of "
                "daylight and a higher Sun at noon, so sunlight arrives more "
                "concentrated and for longer, and that is summer. The other "
                "hemisphere has winter at the same moment. Distance from the "
                "Sun plays no part: the Earth is nearest in January, during "
                "northern winter.",

    "stretch": [
        {"id": "seasonal-lag",
         "type": "explainer",
         "text": "The hottest weeks of the year come well after midsummer — "
                 "usually late July in Britain, a month after the longest "
                 "day. Land, sea and air take time to warm through, and while "
                 "the Sun is still delivering more energy each day than the "
                 "ground is losing, the temperature keeps climbing. The same "
                 "lag runs the other way in winter, which is why February is "
                 "often colder than December. It is called seasonal lag, and "
                 "the same effect makes mid-afternoon warmer than noon."},
        {"id": "the-tilt-is-not-permanent",
         "type": "explainer",
         "text": "The tilt is not permanent. Over about 41 000 years it "
                 "drifts between roughly 22.1° and 24.5°, the orbit’s shape "
                 "varies over about 100 000 years, and the direction of the "
                 "axis swings round a full circle every 26 000. Together "
                 "these Milankovitch cycles change how sunlight is shared "
                 "between the hemispheres and across the year, and their "
                 "rhythm shows up clearly in the timing of ice ages."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "axis",
         "definition": "The imaginary line the Earth spins about. It is "
                       "tilted about 23.4° from upright and keeps pointing "
                       "the same way in space all year."},
        {"term": "tilt",
         "definition": "The angle between the Earth’s axis and upright. It is "
                       "what gives the seasons, because it makes each "
                       "hemisphere lean towards the Sun for half the year."},
        {"term": "equinox",
         "definition": "A date when the Sun is overhead at the equator, so "
                       "everywhere on Earth gets close to twelve hours of "
                       "daylight. Around 21 March and 23 September."},
        {"term": "solstice",
         "definition": "A date when one hemisphere leans as far towards the "
                       "Sun as it ever does, giving that hemisphere its "
                       "longest day. Around 21 June and 21 December."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to check why the two hemispheres disagree about the "
                "season?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The Earth–Sun geometry behind insolation, energy balance "
                   "and the greenhouse effect, and orbital forcing of "
                   "long-term climate change.",

    "convention_note": "The bench is a teaching model. Solar declination is "
                       "taken as 0° at the equinoxes and ±23.44° at the "
                       "solstices, and daylight length is calculated from the "
                       "standard sunrise equation for those declinations. "
                       "That calculation ignores atmospheric refraction and "
                       "the finite width of the Sun’s disc, both of which "
                       "lengthen real daylight by several minutes, and it "
                       "takes no account of altitude or local horizon. Noon "
                       "Sun altitude is 90° minus the difference between "
                       "latitude and declination. Energy per square metre is "
                       "the sine of that altitude, which ignores absorption "
                       "and scattering in the atmosphere.",

    "ws": ["measurement"],
}
