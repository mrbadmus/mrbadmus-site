"""P12 lesson 05 — Seasons and the tilt: twelve questions (MRB-223).

Written against Design's page. The January hook, the four dates and the
three places are hers.

The discriminations, in the order the lesson builds them:

  · the axis is tilted about 23.4° and the tilt does not move (`SPACE-16`);
  · the two hemispheres are opposite at the same moment, which is what
    rules distance out (`SPACE-15`, `SPACE-17`);
  · a high Sun warms more because the same beam covers less ground, not
    because it is nearer (`SPACE-18`);
  · latitude decides how big the swing is at all, which is why the equator
    barely has seasons. The harder band sits here.

⚠️ POSITION IS AUTHORED — 2,0,1,3 · 1,3,2,0 · 3,1,0,2, three of each.

⚠️ Neither marked rung is restated: the January-perihelion question and
the high-Sun-versus-low-Sun question are the ladder's, and nothing here
reuses either. Rung 4's Arctic Circle is the ladder's too and is not
reused.
"""

UNIT = "P12"
LESSON = "seasons-and-the-tilt"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p12-05-e01",
        "band": "easier",
        "text": "By roughly how much is the Earth's axis tilted?",
        "options": [
            {"text": "About 5°", "correct": False,
             "why": "That would be almost upright, and the seasons would be "
                    "far weaker than they are."},
            {"text": "About 90°", "correct": False,
             "why": "At 90° the axis would lie in the plane of the orbit and "
                    "each pole would face the Sun directly for months."},
            {"text": "About 23.4°", "correct": True},
            {"text": "It has no tilt — the axis is upright", "correct": False,
             "why": "With no tilt there would be no seasons at all: twelve "
                    "hours of daylight everywhere, every day."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-e02",
        "band": "easier",
        "text": "It is July in the UK. What season is it in Australia?",
        "options": [
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "Winter, with that half leaning away",
             "correct": True},
            {"text": "Summer", "correct": False,
             "why": "The two hemispheres are always opposite, because only "
                    "one of them can lean towards the Sun at a time."},
            {"text": "The same season, because the date is the same",
             "correct": False,
             "why": "The date is the same and the lean is not. The southern "
                    "hemisphere is tilted away in July."},
            {"text": "It depends on how far Australia is from the Sun that "
                     "week", "correct": False,
             "why": "Australia and Britain are the same distance from the Sun "
                    "to within a few thousand kilometres out of 150 million."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-e03",
        "band": "easier",
        "text": "Which hemisphere has its longest day around 21 June?",
        "options": [
            {"text": "The southern hemisphere", "correct": False,
             "why": "The southern hemisphere is leaning AWAY from the Sun in "
                    "June, so that is its shortest day."},
            {"text": "The northern hemisphere", "correct": True},
            {"text": "Both, because the day is longest everywhere at the "
                     "solstice", "correct": False,
             "why": "A solstice is the longest day in one hemisphere and the "
                    "shortest in the other, on the same date."},
            {"text": "Neither — day length is the same all year", "correct": False,
             "why": "Day length changes through the year everywhere except "
                    "very close to the equator."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-e04",
        "band": "easier",
        "text": "As the Earth travels round its orbit, what happens to the "
                "direction its axis points in?",
        "options": [
            {"text": "It swings round to keep the tilt facing the Sun",
             "correct": False,
             "why": "If it did that, the leaning hemisphere would never "
                    "change and there would be no seasons."},
            {"text": "It flips over twice a year", "correct": False,
             "why": "Nothing flips. The Earth moves and the axis holds its "
                    "direction."},
            {"text": "It changes randomly from month to month", "correct": False,
             "why": "The seasons are utterly regular, which they could not be "
                    "if the axis wandered."},
            {"text": "It stays pointing the same way in space all year",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p12-05-s01",
        "band": "standard",
        "text": "Two things happen together in the hemisphere that is "
                "leaning towards the Sun. What are they?",
        "options": [
            {"text": "The Earth is closer to the Sun, and the Sun gives out "
                     "more energy", "correct": False,
             "why": "Neither is true. Distance changes for the whole planet "
                    "at once, and the Sun's output is very nearly constant."},
            {"text": "The Sun is above the horizon for longer, and it climbs "
                     "higher at noon", "correct": True},
            {"text": "The Earth spins more slowly, and the days are longer as "
                     "a result", "correct": False,
             "why": "The spin rate does not change. The day is longer because "
                    "of where the Sun sits relative to the horizon, not "
                    "because the rotation slowed."},
            {"text": "The atmosphere thins, and more sunlight reaches the "
                     "ground", "correct": False,
             "why": "The atmosphere does not thin seasonally. What changes is "
                    "the angle the light arrives at."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-s02",
        "band": "standard",
        "text": "On the same date, London has 16.5 hours of daylight and "
                "Sydney has 9.7. What date is it likely to be?",
        "options": [
            {"text": "21 March", "correct": False,
             "why": "At an equinox both places get close to twelve hours. "
                    "These two are as far apart as they get."},
            {"text": "23 September", "correct": False,
             "why": "That is the other equinox, and it gives both places "
                    "about twelve hours as well."},
            {"text": "21 December", "correct": False,
             "why": "In December it is the southern hemisphere with the long "
                    "day. The figures would be the other way round."},
            {"text": "21 June", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-s03",
        "band": "standard",
        "text": "Why does the same beam of sunlight warm the ground less "
                "when the Sun is low in the sky?",
        "options": [
            {"text": "Because the Sun is further away when it is low, and a "
                     "source further off always delivers less to a surface",
             "correct": False,
             "why": "The change in distance across a day is a few thousand "
                    "kilometres out of 150 million — nothing at all."},
            {"text": "Because low sunlight carries less energy than high "
                     "sunlight, since the Sun radiates hardest straight "
                     "downwards", "correct": False,
             "why": "It is the same sunlight from the same Sun. Only its "
                    "angle of arrival has changed."},
            {"text": "Because the beam is spread across a larger patch of "
                     "ground, so each square metre gets less", "correct": True},
            {"text": "Because the ground reflects more of it back at a low "
                     "angle, so less of it is absorbed at all",
             "correct": False,
             "why": "A little more is reflected, and the main effect is the "
                    "beam being spread out over more ground."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-s04",
        "band": "standard",
        "text": "At the equator, day length and the noon Sun barely change "
                "through the year. Why?",
        "options": [
            {"text": "Because the equator is the part of the Earth nearest "
                     "the Sun, and nearness is what sets how warm a place is",
             "correct": False,
             "why": "It is nearest by about 6000 km out of 150 million, which "
                    "changes nothing. Nearness is not what sets a season."},
            {"text": "Because the tilt leans the equator neither towards nor "
                     "away from the Sun by much, wherever the Earth is",
             "correct": True},
            {"text": "Because the equator is always in daylight, so it never "
                     "has a shorter or a longer day", "correct": False,
             "why": "The equator has about twelve hours of daylight and "
                    "twelve of darkness, every day of the year."},
            {"text": "Because the Earth's tilt does not affect the southern "
                     "hemisphere, and the equator sits on the line between "
                     "them", "correct": False,
             "why": "The tilt affects the southern hemisphere exactly as much "
                    "as the northern, in the opposite sense."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p12-05-h01",
        "band": "harder",
        "text": "A student says the seasons must come from the Earth's "
                "distance to the Sun, because summer is warmer and warmth "
                "comes from the Sun. What single fact is enough to refute "
                "this?",
        "options": [
            {"text": "The Sun's output varies slightly over an eleven-year "
                     "cycle, which is enough to set the rhythm of the "
                     "seasons", "correct": False,
             "why": "True, and far too small and far too slow to produce a "
                    "summer and a winter each year."},
            {"text": "The Earth's orbit is very nearly a circle, so the "
                     "distance can hardly change through the year at all",
             "correct": False,
             "why": "Close, and not enough on its own: a small distance "
                    "change could still be argued for. The killing fact is "
                    "the two hemispheres disagreeing."},
            {"text": "The Earth is closest to the Sun in January, so on its "
                     "own the distance idea already gets the sign wrong",
             "correct": False,
             "why": "Suggestive, and a determined student could reply that "
                    "the seasons lag. The hemispheres are the fact that "
                    "cannot be argued round."},
            {"text": "It is summer in one hemisphere while it is winter in "
                     "the other, at the same distance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-h02",
        "band": "harder",
        "text": "Imagine the Earth's tilt were increased to 40°. What would "
                "happen to the seasons in Britain?",
        "options": [
            {"text": "They would disappear, because the axis would be too far "
                     "from upright for the tilt to matter any more",
             "correct": False,
             "why": "Seasons come from the tilt, so more tilt gives more "
                    "season, not less."},
            {"text": "Summers would be hotter and winters colder, because the "
                     "lean would be more extreme both ways", "correct": True},
            {"text": "Only the summers would change, because winter depends "
                     "on distance rather than on the lean", "correct": False,
             "why": "Both ends of the year come from the same tilt, so both "
                    "would change together."},
            {"text": "The seasons would swap round, so June would be winter, "
                     "because a larger tilt points the axis the other way",
             "correct": False,
             "why": "The direction of the lean is unchanged; only its size "
                    "has grown. June would still be northern summer."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-h03",
        "band": "harder",
        "text": "In Britain the longest day is 21 June, but the hottest "
                "weeks usually come in late July. Why?",
        "options": [
            {"text": "Land, sea and air take weeks to warm through, so the "
                     "temperature keeps climbing while the surplus lasts",
             "correct": True},
            {"text": "The Earth is closest to the Sun in late July, and that "
                     "extra closeness is what makes it the hottest time",
             "correct": False,
             "why": "It is at its FURTHEST in early July. The lag happens "
                    "despite that, not because of it."},
            {"text": "Day length keeps increasing until late July, so the "
                     "hottest weeks arrive with the longest days",
             "correct": False,
             "why": "Days start shortening from 21 June. The warming "
                    "continues anyway, because the ground is still gaining "
                    "more than it loses."},
            {"text": "The Sun climbs higher at noon in July than in June, so "
                     "its light is more concentrated then", "correct": False,
             "why": "The noon Sun is at its highest on the solstice and "
                    "starts dropping afterwards."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-h04",
        "band": "harder",
        "text": "At the North Pole the Sun stays above the horizon for about "
                "six months and below it for about six. Why does that not "
                "make it the warmest place on Earth in July?",
        "options": [
            {"text": "Because the Sun there gives out less energy than it "
                     "does over the tropics", "correct": False,
             "why": "It is the same Sun everywhere. What differs is the angle "
                    "its light arrives at."},
            {"text": "Because six months of darkness cools it faster than six "
                     "months of daylight can warm it", "correct": False,
             "why": "That explains the annual average, and not why July "
                    "itself is cool while the Sun never sets."},
            {"text": "Because the Sun never climbs high, so its light is "
                     "spread thinly however long it is up", "correct": True},
            {"text": "Because the ice reflects all of the sunlight that "
                     "arrives", "correct": False,
             "why": "Ice does reflect a great deal, which makes the effect "
                    "worse rather than causing it. Even bare ground there "
                    "would stay cold."},
        ],
        "figure": None,
    },
]
