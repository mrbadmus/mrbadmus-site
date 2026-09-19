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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p12-05-e05",
        "band": "easier",
        "text": "What causes the seasons?",
        "options": [
            {"text": "The Earth's distance from the Sun changing through the "
                     "year",
             "correct": False,
             "why": "The Earth is nearest the Sun in January, during northern "
                    "winter."},
            {"text": "The tilt of the Earth's axis", "correct": True},
            {"text": "The Sun giving out more energy in summer",
             "correct": False,
             "why": "The Sun's output barely changes, and the two hemispheres "
                    "have opposite seasons at once."},
            {"text": "The Earth spinning faster in summer", "correct": False,
             "why": "The spin rate is effectively constant, and it sets the "
                    "day rather than the year."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-e06",
        "band": "easier",
        "text": "When the northern hemisphere leans towards the Sun, it is…",
        "options": [
            {"text": "winter there", "correct": False,
             "why": "Leaning towards the Sun brings longer days and a higher "
                    "noon Sun, which is summer."},
            {"text": "summer there", "correct": True},
            {"text": "summer in both hemispheres at once", "correct": False,
             "why": "If one leans towards, the other leans away, so their "
                    "seasons are opposite."},
            {"text": "spring everywhere on Earth", "correct": False,
             "why": "The two hemispheres are never in the same season at the "
                    "same time."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-e07",
        "band": "easier",
        "text": "In which month is the Earth CLOSEST to the Sun?",
        "options": [
            {"text": "July", "correct": False,
             "why": "July is when it is furthest — during northern summer, "
                    "which is the point."},
            {"text": "January", "correct": True},
            {"text": "March", "correct": False,
             "why": "March is near an equinox, and the distance is between "
                    "its extremes."},
            {"text": "The distance never changes", "correct": False,
             "why": "It does change a little; it is simply not what causes "
                    "the seasons."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-e08",
        "band": "easier",
        "text": "As the Earth goes round the Sun, what happens to the "
                "direction its axis points in?",
        "options": [
            {"text": "It leans towards the Sun in summer and away in winter",
             "correct": False,
             "why": "The axis keeps one direction; it is the Earth's position "
                    "in its orbit that changes which hemisphere leans in."},
            {"text": "It keeps pointing the same way in space", "correct": True},
            {"text": "It turns to follow the Sun through the year",
             "correct": False,
             "why": "Nothing turns it; it holds its direction throughout the "
                    "orbit."},
            {"text": "It flips over twice a year", "correct": False,
             "why": "It never flips; the seasons come from where the Earth "
                    "is, not from the axis moving."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p12-05-s05",
        "band": "standard",
        "text": "Why are the days longer in summer?",
        "options": [
            {"text": "Because the Earth spins more slowly in summer",
             "correct": False,
             "why": "The spin rate does not change; a day is still 24 hours "
                    "long."},
            {"text": "Because the leaning hemisphere spends more of each "
                     "rotation in sunlight",
             "correct": True},
            {"text": "Because the Earth is closer to the Sun", "correct": False,
             "why": "It is furthest away during northern summer, and distance "
                    "would not change the day length anyway."},
            {"text": "Because the Sun rises earlier when it is warmer",
             "correct": False,
             "why": "The warmth follows from the longer day rather than "
                    "causing it."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-s06",
        "band": "standard",
        "text": "It is December. Which hemisphere is leaning towards the Sun?",
        "options": [
            {"text": "The northern", "correct": False,
             "why": "December is northern winter, so the north is leaning "
                    "away."},
            {"text": "The southern", "correct": True},
            {"text": "Both equally", "correct": False,
             "why": "That happens at the equinoxes, in March and September."},
            {"text": "Neither, because the tilt is sideways in December",
             "correct": False,
             "why": "The axis holds one direction all year; in December the "
                    "south leans in."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-s07",
        "band": "standard",
        "text": "On the same day the UK has winter and Argentina has summer. "
                "Why?",
        "options": [
            {"text": "Because Argentina is closer to the Sun", "correct": False,
             "why": "Both are on the same planet at essentially the same "
                    "distance."},
            {"text": "Because the two hemispheres lean opposite ways at any "
                     "moment",
             "correct": True},
            {"text": "Because Argentina is nearer the equator",
             "correct": False,
             "why": "Being nearer the equator softens the seasons; it does "
                    "not reverse them."},
            {"text": "Because the Earth's tilt is different in the south",
             "correct": False,
             "why": "There is one tilt for the whole planet; the two "
                    "hemispheres simply lean opposite ways."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-s08",
        "band": "standard",
        "text": "Why is the noon Sun higher in the sky in June than in "
                "December, in Britain?",
        "options": [
            {"text": "Because the Sun is physically higher above the solar "
                     "system in June",
             "correct": False,
             "why": "The Sun does not move up and down; the Earth's lean is "
                    "what changes the angle."},
            {"text": "Because the northern hemisphere is leaning towards the "
                     "Sun in June",
             "correct": True},
            {"text": "Because the Earth is closer to the Sun in June",
             "correct": False,
             "why": "It is furthest away then, and distance would not raise "
                    "the Sun in the sky."},
            {"text": "Because the atmosphere bends the light more in summer",
             "correct": False,
             "why": "Refraction shifts the Sun's apparent position by a "
                    "fraction of a degree, nothing like this."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p12-05-h05",
        "band": "harder",
        "text": "What would the seasons be like if the Earth had no tilt at "
                "all?",
        "options": [
            {"text": "Summer everywhere at once, then winter everywhere at "
                     "once",
             "correct": False,
             "why": "That would need the distance to drive the seasons, and "
                    "it does not."},
            {"text": "Almost no seasons — each place much the same all year",
             "correct": True},
            {"text": "Stronger seasons, because nothing would soften them",
             "correct": False,
             "why": "The tilt is what creates them; removing it takes them "
                    "away."},
            {"text": "The same seasons, since they come from the orbit",
             "correct": False,
             "why": "The orbit sets the year; the tilt is what makes parts of "
                    "it warmer than others."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-h06",
        "band": "harder",
        "text": "Why does a high Sun deliver more energy to each square metre "
                "of ground?",
        "options": [
            {"text": "Because it is closer to the ground when it is high",
             "correct": False,
             "why": "The change in distance is a few thousand kilometres out "
                    "of 150 million — nothing."},
            {"text": "Because the same beam is spread over a smaller patch of "
                     "ground",
             "correct": True},
            {"text": "Because sunlight travels faster when it comes straight "
                     "down",
             "correct": False,
             "why": "Light travels at the same speed however it arrives."},
            {"text": "Because a high Sun is hotter than a low one",
             "correct": False,
             "why": "It is the same Sun; only the angle at which its light "
                    "lands has changed."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-h07",
        "band": "harder",
        "text": "Suppose the Earth had no tilt but a strongly stretched "
                "orbit. Would there be seasons?",
        "options": [
            {"text": "No, because seasons need a tilt and nothing else",
             "correct": False,
             "why": "A varying distance would change the warmth, so something "
                    "season-like would happen."},
            {"text": "Yes, and they would be the same in both hemispheres at "
                     "once",
             "correct": True},
            {"text": "Yes, and they would still be opposite in the two "
                     "hemispheres",
             "correct": False,
             "why": "Opposite seasons come from the tilt; with none, both "
                    "hemispheres would change together."},
            {"text": "No, because the orbit's shape does not affect "
                     "temperature at all",
             "correct": False,
             "why": "A strongly stretched orbit would change the distance a "
                    "great deal, and with it the warmth."},
        ],
        "figure": None,
    },
    {
        "id": "p12-05-h08",
        "band": "harder",
        "text": "A student says summer comes when the tilt brings your "
                "hemisphere physically nearer the Sun. Why is that wrong?",
        "options": [
            {"text": "Because the tilt moves you further away, not nearer",
             "correct": False,
             "why": "It moves you a little each way through the year, and the "
                    "amount is what makes it irrelevant."},
            {"text": "Because a few thousand kilometres is nothing against "
                     "150 million; the angle and day length do it",
             "correct": True},
            {"text": "Because the tilt does not move any part of the Earth "
                     "closer or further",
             "correct": False,
             "why": "It does, very slightly — the point is how small that is."},
            {"text": "Because the Sun's energy does not depend on distance at "
                     "all",
             "correct": False,
             "why": "It certainly does; the distances involved here are just "
                    "far too similar to matter."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ─────────────────────────────────────────
    {
            "id": 'p12-05-e09',
            "band": 'easier',
            "text": "What is the Earth's axis?",
            "options": [
                {"text": 'The imaginary line the Earth spins about', "correct": True},
                {"text": 'The path the Earth follows around the Sun', "correct": False, "why": 'That path is the orbit; the axis is the line the Earth turns about, not the path it travels.'},
                {"text": 'The line marking the edge of the atmosphere', "correct": False, "why": "The atmosphere's edge is a height above the ground, unrelated to the spin axis."},
                {"text": 'The boundary between day and night on the globe', "correct": False, "why": 'That boundary shifts constantly as the Earth turns; the axis is a fixed line through the middle.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e10',
            "band": 'easier',
            "text": 'The Earth turns once on its own axis roughly every 24 hours. What does that motion give us?',
            "options": [
                {"text": 'The cycle of the seasons', "correct": False, "why": 'Seasons come from the year-long orbit and the tilt, a separate motion from the daily spin.'},
                {"text": 'The cycle of day and night', "correct": True},
                {"text": 'The change from one year to the next', "correct": False, "why": 'A year is set by one full orbit of the Sun, not by the daily spin.'},
                {"text": 'The changing phases of the Moon', "correct": False, "why": "Those come from the Moon's own orbit around Earth, not from Earth's daily spin."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e11',
            "band": 'easier',
            "text": 'Why does the Sun appear to move across the sky during the day?',
            "options": [
                {"text": 'The Sun is travelling across the sky above us', "correct": False, "why": 'The Sun barely moves relative to Earth over a day; the apparent motion comes from our own spin.'},
                {"text": 'The atmosphere carries its image slowly sideways', "correct": False, "why": "The atmosphere bends light only slightly near the horizon; it does not carry the Sun's image across the sky."},
                {"text": 'The Earth is turning underneath it, so it seems to move', "correct": True},
                {"text": 'The Sun itself circles around the Earth once each day', "correct": False, "why": 'It is the Earth that orbits the Sun, over a year, while spinning on its own axis every day.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e12',
            "band": 'easier',
            "text": 'Which two motions of the Earth are being described here: spinning once a day, and orbiting the Sun once a year?',
            "options": [
                {"text": 'The orbit gets under way once the daily spin has completely stopped', "correct": False, "why": 'The Earth spins continuously while it orbits; neither motion waits for the other to stop.'},
                {"text": 'The very same motion, described twice', "correct": False, "why": 'A day and a year are very different lengths of time, so these are two distinct motions.'},
                {"text": 'The daily spin causes the yearly orbit', "correct": False, "why": 'Spinning on an axis and travelling round the Sun are independent; one does not cause the other.'},
                {"text": 'Two completely separate motions, happening together', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e13',
            "band": 'easier',
            "text": "Roughly how much does the Sun's own output vary over its eleven-year cycle of activity?",
            "options": [
                {"text": 'By about a tenth of one per cent', "correct": True},
                {"text": 'By about ten per cent', "correct": False, "why": "That would be a hundred times larger a swing than the Sun's real cycle produces."},
                {"text": 'By about half', "correct": False, "why": "A change that large would be a dramatic event, far beyond the Sun's normal, gentle cycle."},
                {"text": "By nothing at all", "correct": False, "why": 'It does vary, just by a very small amount over the eleven-year cycle.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e14',
            "band": 'easier',
            "text": "The Earth's axis currently points towards which star?",
            "options": [
                {"text": 'Proxima Centauri', "correct": False, "why": 'Proxima Centauri is simply the nearest star to the Sun; the axis does not point towards it.'},
                {"text": 'Polaris', "correct": True},
                {"text": 'The Sun itself', "correct": False, "why": 'The axis stays roughly fixed in direction; it does not track the Sun as the Earth orbits.'},
                {"text": 'A different star every night', "correct": False, "why": 'The axis holds almost the same direction night after night, for a human lifetime.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e15',
            "band": 'easier',
            "text": "Over about 41 000 years, the size of the Earth's tilt drifts between roughly 22.1° and 24.5°. What does this tell you about the 23.4° figure usually quoted?",
            "options": [
                {"text": 'The tilt cannot be changing, since seasons stay regular', "correct": False, "why": "The drift is far too slow to disturb any single person's lifetime of seasons."},
                {"text": 'It must be a rounding mistake in the figure', "correct": False, "why": '23.4° is simply the tilt as it stands today; there is no mistake in quoting it.'},
                {"text": "It is today's value, not a fixed constant for all time", "correct": True},
                {"text": 'The 41 000-year figure must refer to something else entirely', "correct": False, "why": 'That figure names how long the tilt itself takes to drift through its full range.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e16',
            "band": 'easier',
            "text": "Besides the tilt drifting, the direction the Earth's axis points also slowly sweeps around in a circle. About how long does one full sweep take?",
            "options": [
                {"text": 'It stays fixed', "correct": False, "why": 'It does change, only extremely slowly compared with a human lifetime.'},
                {"text": 'About 26 years', "correct": False, "why": 'That is far too fast a sweep; nobody would notice the pole star staying fixed for that short a time.'},
                {"text": 'About 26 days', "correct": False, "why": 'That length of time belongs to something like a lunar month, not a slow axis sweep.'},
                {"text": 'About 26 000 years', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e17',
            "band": 'easier',
            "text": "Besides the tilt's size and the axis sweeping round, what third thing changes over roughly 100 000 years?",
            "options": [
                {"text": "The shape of the Earth's orbit", "correct": True},
                {"text": "The Earth's total mass", "correct": False, "why": "The planet's mass is not what the 100 000-year cycle concerns; it is about the orbit's shape."},
                {"text": 'The fixed speed at which light travels through a vacuum', "correct": False, "why": "That speed is a fixed constant of nature, unrelated to Earth's orbit changing shape."},
                {"text": 'The number of hours in a day', "correct": False, "why": "A day's length is set by Earth's spin rate, a separate matter from the orbit's shape."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e18',
            "band": 'easier',
            "text": 'In Britain, the hottest weeks usually come after the longest day. In which month do they typically fall?',
            "options": [
                {"text": 'Late June, on the longest day itself', "correct": False, "why": 'The peak comes some weeks after the solstice, not on the longest day itself.'},
                {"text": 'Late July', "correct": True},
                {"text": 'Late September', "correct": False, "why": 'That is close to the autumn equinox, well past the usual peak of summer heat.'},
                {"text": 'Late December', "correct": False, "why": 'December is the middle of the British winter, the coldest part of the year, not the hottest.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e19',
            "band": 'easier',
            "text": 'February is often colder than December in Britain, even though the days are already getting longer by February. What kind of effect is this an example of?',
            "options": [
                {"text": 'A sign that the tilt has changed since December', "correct": False, "why": 'The tilt barely moves within one winter; this pattern is far too fast to be a tilt change.'},
                {"text": 'A random, unpredictable swing in the weather', "correct": False, "why": 'This pattern happens reliably most years, which points to a real cause rather than pure randomness.'},
                {"text": 'Seasonal lag — the ground keeps losing heat for a while after the shortest day', "correct": True},
                {"text": 'Clear evidence that the Earth moves closer to the Sun in February', "correct": False, "why": 'Distance changes only slightly across these months and does not drive this particular pattern.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e20',
            "band": 'easier',
            "text": 'Mid-afternoon is often warmer than midday, even though the Sun is highest at midday. What kind of effect does this match?',
            "options": [
                {"text": 'A change in the tilt during the afternoon', "correct": False, "why": 'The tilt is fixed over any single day; it plays no part in an afternoon warming up.'},
                {"text": 'The Earth briefly moving closer to the Sun each afternoon', "correct": False, "why": "The Earth's distance from the Sun does not shift over the course of a single afternoon."},
                {"text": 'The Sun climbing even higher after midday', "correct": False, "why": "The Sun's height in the sky peaks at midday and falls afterwards, the opposite of climbing higher."},
                {"text": 'The same kind of lag that makes late July hotter than the longest day', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e21',
            "band": 'easier',
            "text": 'On 21 June, the noon Sun in London reaches about 61° above the horizon. Is that higher or lower than directly overhead?',
            "options": [
                {"text": 'Lower — directly overhead would be 90°', "correct": True},
                {"text": 'Higher — nothing can climb past 61° from London', "correct": False, "why": 'Directly overhead is 90°, so 61° sits well below that, not above it.'},
                {"text": 'Exactly the same as overhead', "correct": False, "why": 'Overhead means 90°; 61° is a good deal lower than that.'},
                {"text": 'It cannot be compared without knowing the date', "correct": False, "why": 'Overhead is always 90° wherever you measure from, so the comparison needs no extra date.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e22',
            "band": 'easier',
            "text": "Over a year, London's day length swings by about 9 hours between its shortest and longest days. At the equator, roughly how big is that same yearly swing?",
            "options": [
                {"text": 'About 9 hours, the same as London', "correct": False, "why": "The equator barely leans towards or away from the Sun, so its swing is far smaller than London's."},
                {"text": 'Close to 0 hours', "correct": True},
                {"text": "About 18 hours, twice London's swing", "correct": False, "why": "That would make the equator's seasons more extreme than London's, the opposite of what happens there."},
                {"text": 'It cannot be worked out without more data', "correct": False, "why": "The equator's tiny lean towards or away from the Sun is already enough to say its swing is small."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e23',
            "band": 'easier',
            "text": 'Roughly how far is the Earth from the Sun, on average?',
            "options": [
                {"text": 'About 150 thousand km', "correct": False, "why": 'That is less than half way to the Moon, nowhere near the Sun.'},
                {"text": 'About 150 million km', "correct": True},
                {"text": 'About 150 billion km', "correct": False, "why": 'That is a thousand times too far, well beyond the outermost planet.'},
                {"text": 'About 1.5 million km', "correct": False, "why": 'That is a hundred times too close; the Earth could not survive there.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e24',
            "band": 'easier',
            "text": 'What is a solstice?',
            "options": [
                {"text": 'The day the Earth is furthest from the Sun', "correct": False, "why": 'The furthest point in the orbit falls in early July, which does not line up with every solstice date.'},
                {"text": 'A date when day and night are equal everywhere', "correct": False, "why": 'That description matches an equinox, not a solstice.'},
                {"text": 'The single coldest day ever recorded anywhere on the whole of planet Earth', "correct": False, "why": "A solstice is fixed by the Earth's tilt and orbit, not by which day happens to record the lowest temperature."},
                {"text": 'A date when one hemisphere has its longest or shortest day of the year', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e25',
            "band": 'easier',
            "text": 'What is an equinox?',
            "options": [
                {"text": 'A date when day and night are close to equal everywhere', "correct": True},
                {"text": 'A date when one hemisphere has its longest day of the year', "correct": False, "why": 'That description matches a solstice, not an equinox.'},
                {"text": 'The day the Earth is closest to the Sun', "correct": False, "why": 'The closest point in the orbit falls in early January, separate from either equinox date.'},
                {"text": 'A date that happens in leap years', "correct": False, "why": 'Equinoxes happen every year, in March and September, leap year or not.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e26',
            "band": 'easier',
            "text": 'A student says the pole star will always be Polaris, forever, because the axis always points there. Given that the axis direction sweeps a full circle roughly every 26 000 years, is that right?',
            "options": [
                {"text": 'Yes — the axis direction stays fixed in place across the whole of time', "correct": False, "why": 'The 26 000-year sweep means the direction does change, just far too slowly to notice day to day.'},
                {"text": 'No — over thousands of years the axis will point at other stars instead', "correct": True},
                {"text": 'Yes — Polaris itself moves to stay in line with the axis', "correct": False, "why": "Polaris stays roughly fixed in the sky; it is the Earth's axis direction that slowly changes instead."},
                {"text": 'No — the axis stopped sweeping thousands of years ago', "correct": False, "why": 'The sweep is an ongoing, continuous process, not one that has already finished.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e27',
            "band": 'easier',
            "text": "A student says the Sun's eleven-year activity cycle must be what causes summer and winter each year. What is the simplest problem with that idea?",
            "options": [
                {"text": 'Seasons repeat every eleven years too, so the timing matches', "correct": False, "why": "Seasons repeat every single year, a far shorter cycle than the Sun's eleven-year one."},
                {"text": 'The Sun has no such cycle of activity', "correct": False, "why": 'The Sun genuinely does have a roughly eleven-year cycle of activity; the timing is the real problem with the idea.'},
                {"text": 'The cycle repeats every eleven years', "correct": True},
                {"text": 'The eleven-year cycle affects the southern hemisphere', "correct": False, "why": "Any change in the Sun's output would reach both hemispheres equally, not just one of them."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e28',
            "band": 'easier',
            "text": "The Earth's orbit changes shape over about 100 000 years, and its tilt changes size over about 41 000 years. Which cycle is slower?",
            "options": [
                {"text": 'Neither cycle has a fixed length', "correct": False, "why": 'Both are given as roughly fixed lengths of time, even if the true values vary a little.'},
                {"text": 'The tilt-size cycle, at about 41 000 years', "correct": False, "why": '41 000 is the smaller of the two figures, so that cycle completes faster, not slower.'},
                {"text": 'Both cycles take exactly the same length of time', "correct": False, "why": '100 000 years and 41 000 years are different lengths, so the two cycles do not match.'},
                {"text": 'The orbit-shape cycle, at about 100 000 years', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e29',
            "band": 'easier',
            "text": 'Which of these is the odd one out: the daily spin, the yearly orbit, or the tilt of the axis?',
            "options": [
                {"text": 'The daily spin — it repeats far more often than the other two change', "correct": True},
                {"text": 'The yearly orbit — of the three, it is the one that repeats without any variation', "correct": False, "why": 'The yearly orbit repeats every year, just as regularly as the daily spin repeats every day.'},
                {"text": 'The tilt of the axis — of the three, it is the one responsible for day and night', "correct": False, "why": 'Day and night come from the daily spin, not from the tilt of the axis.'},
                {"text": 'None of the three is different from the others in any way', "correct": False, "why": "The daily spin's timescale is vastly shorter than the other two, which is a real difference."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-e30',
            "band": 'easier',
            "text": 'Which of these changes in a matter of hours, rather than months or thousands of years: the season, the size of the tilt, or whether it is day or night where you are?',
            "options": [
                {"text": 'The season', "correct": False, "why": 'A season lasts months, changing far more slowly than a matter of hours.'},
                {"text": 'Whether it is day or night', "correct": True},
                {"text": 'The size of the tilt', "correct": False, "why": "The tilt's size drifts over tens of thousands of years, far slower than a matter of hours."},
                {"text": 'All three change equally fast', "correct": False, "why": "Day and night, the season, and the tilt's size all change on very different timescales."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s09',
            "band": 'standard',
            "text": 'A student says the Sun rises because it moves upward into the sky each morning. Using the daily spin, explain what is actually happening.',
            "options": [
                {"text": "The Earth's spin carries your location round into the sunlit half", "correct": True},
                {"text": 'The Sun does climb upward every morning, at a fixed and measurable speed', "correct": False, "why": "The Sun's own position barely shifts over a single morning; the apparent climb comes from our own spin."},
                {"text": "The atmosphere lifts the Sun's image higher as the morning warms up", "correct": False, "why": "Warming air bends light only slightly, nowhere near enough to explain the Sun's apparent rise."},
                {"text": 'The Sun orbits the Earth once every 24 hours, rising as it comes round', "correct": False, "why": 'It is the Earth that spins once every 24 hours; the Sun does not orbit the Earth.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s10',
            "band": 'standard',
            "text": "The Sun's output varies by about a tenth of one per cent over its eleven-year cycle. Why is that far too small to cause summer and winter?",
            "options": [
                {"text": "A tenth of one per cent is in truth a huge change in the Sun's output", "correct": False, "why": 'A tenth of one per cent is a very small fraction; the seasons need a far larger effect than that to explain them.'},
                {"text": 'Too tiny a change to produce the swing between summer and winter', "correct": True},
                {"text": 'The cycle affects stars other than the Sun, leaving the Sun itself untouched', "correct": False, "why": 'The eleven-year cycle described is a real property of the Sun itself, not of other stars.'},
                {"text": 'A small change in output produces an equally large change in temperature', "correct": False, "why": 'A small change in output produces a correspondingly small effect, not a large one.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s11',
            "band": 'standard',
            "text": 'The tilt drifts between about 22.1° and 24.5° over roughly 41 000 years. Roughly how large is that full range of drift?',
            "options": [
                {"text": 'About 0.24°', "correct": False, "why": 'That divides the true range by ten; 24.5 minus 22.1 comes to a good deal more than that.'},
                {"text": 'About 24°', "correct": False, "why": 'That is close to the whole tilt value itself, ten times larger than the actual range of drift.'},
                {"text": 'About 2.4°', "correct": True},
                {"text": 'About 46.6°', "correct": False, "why": 'That adds the two figures together rather than subtracting the smaller from the larger.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s12',
            "band": 'standard',
            "text": "The axis sweeps a full circle roughly every 26 000 years, and the tilt's size cycles roughly every 41 000 years. Which motion completes more cycles in a million years?",
            "options": [
                {"text": 'Neither completes a whole number of cycles in a million years', "correct": False, "why": 'A whole number of cycles is not what the question is asking; it only asks which is quicker to repeat.'},
                {"text": 'The tilt-size cycle, since its cycle is the shorter of the two', "correct": False, "why": '41 000 is the LARGER of the two figures, so that cycle is the slower one, not the shorter.'},
                {"text": 'Both complete exactly the same number of cycles', "correct": False, "why": '26 000 and 41 000 are different lengths, so the two cycles cannot complete the same number of times.'},
                {"text": 'The axis sweep, since its cycle is the shorter of the two', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s13',
            "band": 'standard',
            "text": 'In Britain, the hottest weeks come in late July, roughly a month after the longest day. What keeps the ground warming during that month?',
            "options": [
                {"text": 'The ground still gains more heat each day than it loses', "correct": True},
                {"text": 'The Sun keeps climbing higher in the sky right through July', "correct": False, "why": 'The noon Sun peaks on the solstice itself and drops a little afterwards, not the other way round.'},
                {"text": 'The Earth becomes measurably closer to the Sun during July', "correct": False, "why": 'The Earth is actually at its furthest from the Sun in early July, not closer.'},
                {"text": 'Day length keeps increasing throughout July', "correct": False, "why": 'Days begin shortening from 21 June onward, not increasing through July.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s14',
            "band": 'standard',
            "text": 'February is often colder than December, even though days are longer by February. Explain the parallel with why late July is hotter than late June.',
            "options": [
                {"text": 'There is no real parallel — the two patterns have entirely separate causes', "correct": False, "why": 'Both are the same seasonal-lag effect, simply running in opposite directions.'},
                {"text": 'In both cases, the ground keeps responding for weeks after the extreme day', "correct": True},
                {"text": 'December must have shorter days than February has, which explains the cold', "correct": False, "why": 'Days are shorter around the December solstice and grow longer by February, not the reverse.'},
                {"text": 'The tilt briefly increases each February, cooling the ground further', "correct": False, "why": 'The tilt does not shift meaningfully within a single winter; the lag comes from slow warming and cooling of the ground.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s15',
            "band": 'standard',
            "text": 'Mid-afternoon is often warmer than midday. Using the idea of lag, explain why, even though the Sun is highest at midday.',
            "options": [
                {"text": 'The afternoon has more hours of daylight than the morning does', "correct": False, "why": 'Morning and afternoon split the same day roughly evenly; that is not what drives this warming.'},
                {"text": 'The Sun is higher in the afternoon than at midday', "correct": False, "why": "The Sun's height peaks at midday and falls afterwards through the afternoon."},
                {"text": "The ground and air keep gaining heat after the Sun's peak", "correct": True},
                {"text": 'The atmosphere thins out each afternoon, letting more heat through', "correct": False, "why": 'The atmosphere does not thin over the course of an afternoon; the lag is about heat building up in the ground and air.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s16',
            "band": 'standard',
            "text": "London's noon Sun reaches about 61° on 21 June. If it were genuinely overhead at 90° instead, what would that mean for the beam's spread on the ground?",
            "options": [
                {"text": 'The beam would vanish completely at 90°', "correct": False, "why": 'An overhead Sun still delivers a beam; it simply concentrates it onto the smallest patch possible.'},
                {"text": 'The beam would spread out over a larger patch of ground than it does at 61°', "correct": False, "why": 'A higher Sun concentrates the beam onto a smaller patch, not a larger one.'},
                {"text": "The beam's spread would stay identical either way", "correct": False, "why": 'The angle of arrival changes how spread out a beam lands; a steeper angle concentrates it further.'},
                {"text": 'The same beam would cover an even smaller patch of ground than it does at 61°', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s17',
            "band": 'standard',
            "text": "London's annual swing in day length is about 9.0 hours, and Sydney's is about 4.5 hours. Roughly how many times bigger is London's swing?",
            "options": [
                {"text": 'About twice as big', "correct": True},
                {"text": 'About four times as big', "correct": False, "why": '9.0 divided by 4.5 comes to two, not four.'},
                {"text": "About the same size as Sydney's", "correct": False, "why": '9.0 hours is a clear, measurable amount larger than 4.5 hours, not roughly the same.'},
                {"text": "About half the size of Sydney's swing", "correct": False, "why": "That has the comparison backwards; London's swing is the larger of the two figures."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s18',
            "band": 'standard',
            "text": 'At the equator, the yearly swing in day length is close to 0 hours. Why does that mean the equator gets neither a clear summer nor a clear winter?',
            "options": [
                {"text": 'The equator has the most dramatic seasons on Earth', "correct": False, "why": 'A swing close to 0 hours is the smallest kind of swing there is, giving the weakest seasons, not the strongest.'},
                {"text": 'With almost no swing in day length, there is no season worth naming', "correct": True},
                {"text": 'The equator has no daylight for part of the year', "correct": False, "why": 'The equator gets close to twelve hours of daylight every single day, all year round.'},
                {"text": 'It means the tilt has no effect anywhere on Earth', "correct": False, "why": "The tilt has a large effect at latitudes such as London's; it is only weak right at the equator."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s19',
            "band": 'standard',
            "text": 'The Earth is about 147 million km from the Sun in January and about 152 million km away in July. Roughly what percentage change in distance is that?',
            "options": [
                {"text": 'About 0.3%', "correct": False, "why": 'That divides the real percentage change by ten, far too small a figure.'},
                {"text": 'About 30%', "correct": False, "why": 'That is ten times too large; the actual gap between the two figures is a small fraction of the total distance.'},
                {"text": 'About 3%', "correct": True},
                {"text": 'About 50%', "correct": False, "why": "A 50% change would put July's distance far beyond the figure actually given."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s20',
            "band": 'standard',
            "text": 'A student argues that because the Earth is 3% further from the Sun in July, British summers must be a little cooler than they would be with no such gap. What is wrong with that argument?',
            "options": [
                {"text": 'Distance from the Sun has no effect whatsoever, on any scale', "correct": False, "why": 'A big enough distance change would matter; the point here is that 3% is far too small to matter.'},
                {"text": 'A 3% change in distance is a huge effect', "correct": False, "why": '3% is a small fraction; it cannot come close to cancelling the much larger tilt effect.'},
                {"text": 'The Earth is not 3% further away in July', "correct": False, "why": 'The two given distances genuinely differ by about that much; the flaw lies elsewhere in the argument.'},
                {"text": 'The tilt effect at British latitudes is far larger than a 3% distance gap', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s21',
            "band": 'standard',
            "text": 'Why is a solstice defined by day length reaching an extreme, rather than by the calendar date alone?',
            "options": [
                {"text": "Because it names day length's furthest point from the equinox value", "correct": True},
                {"text": 'Because the calendar date of a solstice changes by several months each year', "correct": False, "why": 'Solstices fall within a day or two of the same dates each year, around 21 June and 21 December.'},
                {"text": 'Because a solstice can happen on any day depending on the weather that year', "correct": False, "why": "Weather does not set the solstice date; the Earth's position in its orbit does."},
                {"text": "Because the word simply means 'a date in the calendar' and nothing more", "correct": False, "why": 'A solstice names a specific astronomical event, the extreme of day length, not any date at all.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s22',
            "band": 'standard',
            "text": 'Why does an equinox give close to twelve hours of daylight everywhere, while a solstice does not?',
            "options": [
                {"text": 'At an equinox the Earth is exactly halfway round its orbit from where it started the year', "correct": False, "why": 'It is the DIRECTION of the lean that matters here, not how far round the orbit the Earth has travelled.'},
                {"text": 'Neither hemisphere leans towards or away from the Sun at an equinox', "correct": True},
                {"text": 'At an equinox the Sun briefly stops giving out any light', "correct": False, "why": 'The Sun shines exactly as normal at an equinox; nothing about its light output changes.'},
                {"text": 'At an equinox every place on Earth is the same distance from the Sun', "correct": False, "why": 'Distance from the Sun is set by where the Earth sits on its ORBIT, not by which places on Earth are being compared.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s23',
            "band": 'standard',
            "text": 'A student says the axis pointing at Polaris today proves it has always pointed there. Using the 26 000-year sweep, explain why that reasoning fails.',
            "options": [
                {"text": 'Polaris itself is what moves, tracking the axis wherever it happens to point', "correct": False, "why": "It is the Earth's axis direction that sweeps round; Polaris stays roughly fixed in the sky."},
                {"text": "The reasoning is sound, since Polaris has permanently sat at the axis's fixed direction", "correct": False, "why": 'The sweep means the axis direction changes over thousands of years; it has not always pointed at Polaris.'},
                {"text": 'An ongoing sweep means the direction was different in the past', "correct": True},
                {"text": "The sweep began recently, so the past direction matched today's", "correct": False, "why": 'The 26 000-year sweep is described as an ongoing cycle, not one that began only recently.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s24',
            "band": 'standard',
            "text": "The orbit's shape changes over about 100 000 years and the tilt's size over about 41 000. Which cycle would a person notice change WITHIN a single human lifetime?",
            "options": [
                {"text": 'Both cycles complete several times within one lifetime', "correct": False, "why": 'Both cycles run tens of thousands of years or more, far longer than any single lifetime.'},
                {"text": 'The tilt-size cycle, since 41 000 years is short enough for one lifetime', "correct": False, "why": '41 000 years is still hundreds of times longer than any human lifetime.'},
                {"text": 'The orbit-shape cycle, since it is the more dramatic of the two changes', "correct": False, "why": 'Being more dramatic over its full cycle does not make it fast; 100 000 years is even slower than the tilt cycle.'},
                {"text": 'Neither — both cycles are far too slow for one lifetime to notice', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s25',
            "band": 'standard',
            "text": "Why does the seasonal-lag effect that delays Britain's hottest weeks until late July also explain why late January, not the solstice itself, is often the coldest point of winter?",
            "options": [
                {"text": 'The ground keeps losing heat for a while after the shortest day', "correct": True},
                {"text": 'Late January is closer to the June solstice than to the December one', "correct": False, "why": 'Late January sits only a few weeks after the December solstice, not close to the June one.'},
                {"text": 'The tilt reaches its most extreme value in late January, later than the solstice itself', "correct": False, "why": "The tilt's extreme lean is exactly what defines the solstice date; it does not shift into late January."},
                {"text": 'The Earth is at its closest point to the Sun in late January, which happens to make it colder', "correct": False, "why": 'Being closer to the Sun would tend to add warmth, not cold, and the lag effect explains the delay either way.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s26',
            "band": 'standard',
            "text": 'Two places share the same latitude, one at sea level and one high in the mountains. Would you expect their annual swing in day length to differ?',
            "options": [
                {"text": 'Yes — height above sea level changes the tilt of a place', "correct": False, "why": "The tilt's lean is set by latitude and the time of year, not by how high a place sits."},
                {"text": 'No — day length at a given latitude depends on the tilt and orbit', "correct": True},
                {"text": 'Yes — mountain air changes the length of the solar day itself', "correct": False, "why": 'Thinner mountain air affects temperature and light intensity, not how long the Sun stays above the horizon.'},
                {"text": 'It cannot be judged without knowing the season', "correct": False, "why": "The ANNUAL swing compares the whole year's extremes, so a single season is not what is being asked about."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s27',
            "band": 'standard',
            "text": 'A student claims the daily spin and the yearly orbit must be linked, since both involve the Earth moving. Why are they treated as separate motions?',
            "options": [
                {"text": 'Because the spin causes the orbit to speed up each day', "correct": False, "why": 'The spin rate and the orbital speed do not drive each other in this way.'},
                {"text": 'Because one of the two motions is real, and the other is an illusion', "correct": False, "why": 'Both the daily spin and the yearly orbit are real motions of the Earth.'},
                {"text": 'Because they run on wildly different timescales, independent of each other', "correct": True},
                {"text": 'Because they are not separate — a day and a year are the same length of time', "correct": False, "why": 'A day and a year are vastly different lengths of time, which is part of why they are separate motions.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s28',
            "band": 'standard',
            "text": 'Suppose the axis swept its full 26 000-year circle twice as fast. Would that change how long a single YEAR lasts?',
            "options": [
                {"text": 'It cannot be answered without knowing the size of the tilt', "correct": False, "why": 'The length of a year depends on the orbit, not on the size of the tilt.'},
                {"text": 'Yes — a faster sweep would shorten every year to match it', "correct": False, "why": 'The axis sweep and the length of one orbit are different quantities; changing one does not change the other.'},
                {"text": 'Yes — the sweep and the year are the same cycle, just described differently', "correct": False, "why": 'They differ enormously in length — thousands of years against one — so they are not the same cycle.'},
                {"text": 'No — a year is set by the orbit, separate from how fast the axis sweeps', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s29',
            "band": 'standard',
            "text": "London's noon Sun reaches about 61° on 21 June and a lower angle on 21 December. Which date gives the more concentrated beam on the ground?",
            "options": [
                {"text": '21 June, since its higher noon angle spreads the beam over less ground', "correct": True},
                {"text": '21 December, since a lower Sun always concentrates its beam more tightly', "correct": False, "why": 'A lower Sun spreads its beam over MORE ground, which is the opposite of concentrating it.'},
                {"text": 'Both dates give exactly the same concentration', "correct": False, "why": 'A higher noon angle genuinely concentrates the beam more; the two dates are not equal in this respect.'},
                {"text": "Neither — beam concentration has nothing to do with the Sun's angle", "correct": False, "why": "The Sun's angle is exactly what decides how concentrated or spread out its beam lands."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-s30',
            "band": 'standard',
            "text": "A student says the seasonal lag that delays summer's peak heat must also delay the shortest day of the year. Why is that a confusion between two different things?",
            "options": [
                {"text": 'The reasoning is correct — the shortest day does shift by weeks', "correct": False, "why": 'The solstice dates stay close to the same day each year; only the temperature peak is delayed by the lag.'},
                {"text": 'The shortest day is fixed by the tilt and orbit; the lag delays the temperature alone', "correct": True},
                {"text": 'Lag affects hot weather, so winter has no lag to consider', "correct": False, "why": 'The same lag effect applies to winter too, which is why late January, not the solstice, is often coldest.'},
                {"text": 'The shortest day and the lag are simply two names for one single event', "correct": False, "why": 'One is a fixed astronomical date and the other a delayed temperature response — two different things.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h09',
            "band": 'harder',
            "text": 'A student argues that because the Sun appears to cross the sky, the Sun must be what is doing the moving. Explain what evidence about the daily spin shows this is backwards.',
            "options": [
                {"text": 'Every point on Earth passes through day and night on a fixed 24-hour cycle', "correct": True},
                {"text": 'The Sun is simply too bright for its true motion to be measured by anyone', "correct": False, "why": "Brightness does not prevent astronomers from measuring the Sun's actual motion relative to Earth."},
                {"text": 'The stars at night prove the Sun is moving, appearing in different places', "correct": False, "why": "The stars shifting position through the night is itself caused by Earth's spin, the same evidence pointing the other way."},
                {"text": 'Nothing about the daily spin can settle which object is doing the moving', "correct": False, "why": 'The steady 24-hour cycle of day and night at every location is exactly the evidence that settles it.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h10',
            "band": 'harder',
            "text": "Suppose a planet's own output varied by 5% over an eleven-year cycle, a far bigger swing than the Sun's real one. Would that cycle then explain that planet's yearly seasons?",
            "options": [
                {"text": 'Yes — a large swing in output can match any pattern', "correct": False, "why": 'The TIMING is the problem here, not just the size of the swing: an eleven-year cycle cannot produce a one-year pattern.'},
                {"text": 'No — even a larger swing still repeats every eleven years', "correct": True},
                {"text": 'Yes, provided the planet also had zero tilt to begin with', "correct": False, "why": 'Removing the tilt would not fix the timing mismatch between an eleven-year cycle and one-year seasons.'},
                {"text": 'It depends entirely on how far the planet is from its star', "correct": False, "why": 'Distance from the star does not resolve the basic mismatch between an eleven-year cycle and yearly seasons.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h11',
            "band": 'harder',
            "text": "The tilt drifts across roughly 2.4° over 41 000 years, while today's tilt causes London's summer noon Sun to reach about 61°. Would a 2.4° tilt swing ever move London's noon Sun by anywhere near that same 2.4°?",
            "options": [
                {"text": 'No — a 2.4° tilt swing would move the noon Sun by tens of degrees instead', "correct": False, "why": 'Noon Sun height changes roughly in step with the tilt itself, not by some far larger multiple of it.'},
                {"text": 'No — noon Sun height is completely unrelated to the size of the tilt', "correct": False, "why": 'Noon Sun height is set directly by the tilt and latitude, so the two are closely linked.'},
                {"text": 'Roughly, yes — noon Sun height tracks the tilt fairly directly', "correct": True},
                {"text": 'It cannot be judged without knowing the exact date chosen', "correct": False, "why": 'The comparison is about how MUCH the noon height shifts for a given tilt shift, which does not need one particular date.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h12',
            "band": 'harder',
            "text": 'Explain why the 41 000-year tilt cycle, the 26 000-year axis sweep, and the 100 000-year orbit-shape cycle are all far too slow to explain why last winter felt colder than the one before.',
            "options": [
                {"text": 'One winter feeling colder than another is itself caused directly by one of these three cycles', "correct": False, "why": "A single year's difference happens on far too short a timescale for any of these slow cycles to be the cause."},
                {"text": 'These three cycles affect the southern hemisphere, not Britain', "correct": False, "why": "All three cycles affect the whole planet's climate pattern, not one hemisphere alone."},
                {"text": 'These cycles do not exist; they were invented to explain long-term climate change', "correct": False, "why": 'These are genuine, measured cycles; the issue is purely that their timescales are far too slow.'},
                {"text": 'Year-to-year weather differences happen far faster than any of these slow cycles', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h13',
            "band": 'harder',
            "text": "Late July is Britain's hottest period and late January is often its coldest, both roughly a month after the nearest solstice. What does that symmetry suggest about the lag's size in each direction?",
            "options": [
                {"text": 'The lag applies by a similar amount in both directions, warming and cooling alike', "correct": True},
                {"text": "It suggests the lag applies to summer alone, and January's cold has another cause", "correct": False, "why": 'The parallel timing in both directions points to the same lag mechanism running each way, not two separate causes.'},
                {"text": 'It suggests winter has no lag, since cold air responds to the Sun instantly', "correct": False, "why": 'Air, land and sea all take time to lose heat too, producing a lag in winter just as in summer.'},
                {"text": 'It suggests the two solstices are the same date, since the delays match so closely', "correct": False, "why": 'The solstices remain six months apart; what matches is the roughly similar SIZE of the delay in each case.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h14',
            "band": 'harder',
            "text": 'A pupil claims that because mid-afternoon is warmer than midday, the Sun itself must still be climbing after midday. Using the lag idea, explain the flaw.',
            "options": [
                {"text": 'The claim is correct — the Sun does keep climbing for a while after midday', "correct": False, "why": "The Sun's height peaks exactly at midday under this model and drops steadily after that."},
                {"text": "The Sun's height already peaks at midday and falls afterwards", "correct": True},
                {"text": "Mid-afternoon warmth has nothing to do with the Sun's height at any point in the day", "correct": False, "why": "The Sun's earlier height still matters — it is what delivered the heat that keeps building up afterwards."},
                {"text": 'The lag idea applies across whole seasons, never within a single day', "correct": False, "why": 'The very same lag mechanism plays out on the timescale of a single day, as well as across a season.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h15',
            "band": 'harder',
            "text": "London's day-length swing is about 9.0 hours a year, and Sydney's is about 4.5. If a third city's swing were measured at about 2.25 hours, what would that suggest about its latitude compared with the other two?",
            "options": [
                {"text": 'Its latitude cannot be judged from its swing', "correct": False, "why": 'The swing size given for London and Sydney already shows swing tracks how far a place sits from the equator.'},
                {"text": 'It sits further from the equator than London, since smaller swings always mean higher latitudes', "correct": False, "why": 'The pattern in the numbers runs the other way: smaller swings go with places closer to the equator.'},
                {"text": 'It sits closer to the equator than either London or Sydney', "correct": True},
                {"text": "It must sit exactly halfway between London's latitude and Sydney's", "correct": False, "why": 'Halving the swing again does not mean the latitude is exactly halfway between the other two; the relationship is not that simple.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h16',
            "band": 'harder',
            "text": "A student says that since the equator's yearly swing is close to 0 hours, the equator must get no sunlight at all for part of the year. What is wrong with that conclusion?",
            "options": [
                {"text": 'Day length at the equator cannot be measured', "correct": False, "why": 'Day length at the equator is measured just as it is anywhere else on Earth.'},
                {"text": 'The conclusion is correct — no daylight for part of the year', "correct": False, "why": 'A small swing means little CHANGE in day length, not an absence of daylight.'},
                {"text": 'The equator has the largest day-length swing of anywhere on Earth', "correct": False, "why": 'The equator has close to the SMALLEST swing of anywhere on Earth, the opposite of the largest.'},
                {"text": 'A tiny swing means day length barely CHANGES there, not that daylight disappears', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h17',
            "band": 'harder',
            "text": 'The Earth is about 3% further from the Sun in July than in January. Suppose that gap were instead 30%. Would distance then plausibly compete with the tilt as a cause of British seasons?',
            "options": [
                {"text": 'It becomes far more plausible, since 30% would noticeably change the energy received', "correct": True},
                {"text": 'No — distance from the Sun is incapable of affecting seasons at any size of gap', "correct": False, "why": 'A large enough distance swing would matter; the issue with the REAL Earth is that 3% is far too small, not that distance can never matter.'},
                {"text": 'It makes no difference, since the tilt cancels out any distance effect', "correct": False, "why": 'Nothing about the tilt automatically cancels a distance effect; a large enough distance swing would still be felt.'},
                {"text": 'Yes, but in the southern hemisphere', "correct": False, "why": 'A change in distance from the Sun affects the whole planet at once, not one hemisphere alone.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h18',
            "band": 'harder',
            "text": "Explain why calling the December solstice 'midwinter' makes more sense from the tilt's point of view than from the temperature's point of view.",
            "options": [
                {"text": 'Because the coldest temperature of the whole winter arrives precisely on the solstice date itself', "correct": False, "why": 'The coldest point typically lags the solstice by weeks, landing closer to late January.'},
                {"text": "The solstice marks the tilt's most extreme lean; the cold lags behind into late January", "correct": True},
                {"text": 'Because the tilt has no connection to the solstice date', "correct": False, "why": 'The solstice date is defined directly by the tilt reaching its most extreme lean.'},
                {"text": "Because 'midwinter' is simply a name with no connection to either the tilt or the temperature", "correct": False, "why": "The name reflects the tilt's extreme point, even though the coldest weather itself lags a little behind it."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h19',
            "band": 'harder',
            "text": 'A student says the axis sweeping its 26 000-year circle must eventually flip the seasons, so that June becomes midwinter in the northern hemisphere. Evaluate that claim.',
            "options": [
                {"text": 'Entirely right — June will become midwinter within a single human lifetime, quite soon', "correct": False, "why": 'The sweep takes about 26 000 years for a full circle, far too slow for such a shift within one lifetime.'},
                {"text": 'Entirely wrong — the axis sweep has no effect whatsoever on the seasons', "correct": False, "why": 'The sweep genuinely changes the axis direction over thousands of years, which does eventually shift which month lines up with which lean.'},
                {"text": 'Partly right — over thousands of years the sweep will shift which lean lines up with June', "correct": True},
                {"text": 'Wrong, since the hemispheres stay locked into opposite seasons', "correct": False, "why": 'Over a long enough timescale the sweep can shift which month aligns with which lean, so the claim is not simply impossible.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h20',
            "band": 'harder',
            "text": "A pupil argues: 'The Earth is closer to the Sun in January, and Britain's coldest weather often falls in late January too, so distance must be involved after all.' Explain the flaw.",
            "options": [
                {"text": "The argument is correct, and distance is the real cause of Britain's cold January", "correct": False, "why": "The same closeness to the Sun coincides with Australia's warm midsummer, which distance alone cannot explain."},
                {"text": 'The Earth is not closer to the Sun in January', "correct": False, "why": 'The Earth genuinely is closest to the Sun in early January, around 147 million km.'},
                {"text": "Late January's cold has nothing to do with the December solstice", "correct": False, "why": 'The lag from the December solstice is exactly why late January is often the coldest point.'},
                {"text": 'The timing is a coincidence of the lag from the December solstice', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h21',
            "band": 'harder',
            "text": 'Explain why a solstice is defined by an extreme in day length rather than by the Earth reaching its closest or furthest point from the Sun.',
            "options": [
                {"text": 'Because the tilt itself controls day length and noon height, not distance', "correct": True},
                {"text": 'Because the closest and furthest points in the orbit happen to fall on the solstice dates anyway', "correct": False, "why": 'The closest point falls in early January and the furthest in early July, neither matching a solstice date closely.'},
                {"text": 'Because distance from the Sun cannot be measured precisely enough to define anything', "correct": False, "why": "Distance is measured precisely; the reason is that the tilt, not distance, is what sets a hemisphere's day length."},
                {"text": 'Because day length is easier to see than distance, even though distance is the true cause', "correct": False, "why": 'Distance is not the true cause of the seasons; the tilt is, which is exactly why day length is used to define a solstice.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h22',
            "band": 'harder',
            "text": 'Two planets have identical tilts but very different orbit shapes: one nearly circular, one strongly stretched. Would you expect their seasonal patterns to be identical?',
            "options": [
                {"text": 'Yes, categorically — orbit shape has no bearing on seasons', "correct": False, "why": 'A strongly stretched orbit changes the distance a great deal through the year, which can add its own effect on top of the tilt.'},
                {"text": 'Not necessarily — a stretched orbit could add its own distance-driven swing in warmth', "correct": True},
                {"text": "No — a stretched orbit would remove the tilt's effect on that planet entirely", "correct": False, "why": "The tilt keeps producing its usual effect regardless of the orbit's shape; a stretched orbit adds to it rather than removing it."},
                {"text": "It cannot be judged without knowing the length of each planet's day", "correct": False, "why": 'Day length affects daily temperature swings, not the seasonal comparison being asked about here.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h23',
            "band": 'harder',
            "text": "Explain why comparing London's 9.0-hour swing with Sydney's 4.5-hour swing is a fairer way to compare their seasons than comparing a single date's day length at each place.",
            "options": [
                {"text": "The swing and a single date's day length give exactly the same comparison, in every case", "correct": False, "why": "A swing measures the year's full range, while one date shows only that day, which is a narrower picture."},
                {"text": "A single date's day length is identical everywhere on Earth on that date, regardless of latitude", "correct": False, "why": "A single date's day length does differ by latitude; the swing is still the fairer year-round measure."},
                {"text": "The swing captures the WHOLE year's range; one date shows a single snapshot", "correct": True},
                {"text": "Because Sydney's day length cannot be measured on any single date", "correct": False, "why": "Sydney's day length on any chosen date can be measured perfectly well; the swing is simply a broader comparison."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h24',
            "band": 'harder',
            "text": "A pupil suggests testing whether distance causes seasons by checking if Earth's climate this July differs noticeably from last July. Explain why this test could never settle the question.",
            "options": [
                {"text": "Because July always falls in the southern hemisphere's winter, ruining the comparison", "correct": False, "why": "July is a date shared by both hemispheres; the real problem is that the Earth's distance barely changes from one July to the next."},
                {"text": 'Climate cannot be measured accurately enough for any July-to-July comparison', "correct": False, "why": 'Climate is measured with good accuracy; the flaw is in what the comparison can actually test, not in measurement precision.'},
                {"text": 'The test would work perfectly well and could settle the question either way', "correct": False, "why": 'Comparing near-identical distances each July cannot reveal what a genuinely different distance would do.'},
                {"text": 'The Earth is at roughly the same point in its orbit each July', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h25',
            "band": 'harder',
            "text": "The tilt stays fixed in direction through the year, yet the axis sweeps a full circle every 26 000 years. Explain why 'fixed in direction' is only true across a single human lifetime.",
            "options": [
                {"text": 'The direction shifts too little to notice within decades, yet adds up over time', "correct": True},
                {"text": 'The two facts flatly contradict each other, so one of them must be wrong', "correct": False, "why": 'Both can be true together: the change per year is tiny, yet it accumulates into a full sweep over 26 000 years.'},
                {"text": "The tilt's direction stays fixed for exactly 26 000 years, then sweeps round in one sudden jump", "correct": False, "why": 'The sweep is continuous and gradual throughout, not a fixed pause followed by a sudden shift.'},
                {"text": 'Both facts describe the SIZE of the tilt, not its direction, so there is no tension to explain', "correct": False, "why": 'One fact is about the tilt staying fixed in DIRECTION, and the sweep is a change in that same direction — they are about the same thing.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h26',
            "band": 'harder',
            "text": "A student proposes that Britain's seasonal lag and the 26 000-year axis sweep must be the same underlying process, just measured on different timescales. Assess that claim.",
            "options": [
                {"text": 'The claim is correct, since both processes eventually repeat and therefore must share one cause', "correct": False, "why": 'Sharing the property of repeating does not make two processes the same; their underlying mechanisms are entirely different.'},
                {"text": "They are unrelated — one is heat building up in the ground, the other the axis's direction shifting", "correct": True},
                {"text": 'The claim is correct, because both processes involve the tilt in exactly the same way', "correct": False, "why": "The lag is about heat storage in land, sea and air; the sweep is about the axis's direction changing — different mechanisms."},
                {"text": 'Neither process is real, so the comparison cannot be assessed', "correct": False, "why": 'Both the seasonal lag and the axis sweep are real, well-established effects; the claim fails for a different reason.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h27',
            "band": 'harder',
            "text": "Explain why 'the Earth is closer to the Sun in January' and 'January is often cold in Britain' can both be true statements without one causing the other.",
            "options": [
                {"text": 'The closeness in January is what causes the cold, confirming a direct link between the two', "correct": False, "why": 'The closeness would, if anything, add warmth rather than cold; the real cause of the cold is the tilt.'},
                {"text": 'They cannot both be true at once, so one of the two statements must be false', "correct": False, "why": 'Both statements are independently well established; the issue is only whether one CAUSES the other.'},
                {"text": 'Two things can happen at the same time without either one causing the other', "correct": True},
                {"text": 'Being cold in January is what makes the Earth move closer to the Sun that month', "correct": False, "why": "Temperature on Earth has no influence on the planet's own orbit around the Sun."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h28',
            "band": 'harder',
            "text": 'A textbook states three cycles — 41 000, 26 000 and 100 000 years — and calls them all parts of the same family of long-term changes. Explain what they share despite having different lengths.',
            "options": [
                {"text": 'Each one repeats exactly once every human lifetime', "correct": False, "why": 'All three take tens of thousands of years at least, vastly longer than any human lifetime.'},
                {"text": 'They share nothing beyond being roughly measured in thousands of years', "correct": False, "why": 'They share a deeper link too: each is a slow change in the geometry between the Earth and the Sun.'},
                {"text": 'Each one directly changes the length of a single day', "correct": False, "why": 'None of the three changes how long a single day lasts; they concern tilt, axis direction and orbit shape instead.'},
                {"text": 'Each is a slow change in the Earth-Sun geometry', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h29',
            "band": 'harder',
            "text": "A student says that because Sydney's swing (4.5 hours) is exactly half London's (9.0 hours), Sydney's latitude must be exactly half of London's. Explain the flaw in that reasoning.",
            "options": [
                {"text": "Matching swing sizes by a ratio doesn't mean the latitudes follow that same ratio", "correct": True},
                {"text": 'The reasoning is entirely correct, and latitude and swing scale together in perfect step forever', "correct": False, "why": 'The relationship between latitude and swing is not a simple straight-line ratio like that.'},
                {"text": 'Swing size has no connection whatsoever to latitude', "correct": False, "why": 'Swing size does track latitude in a general sense; the flaw is assuming the relationship is a simple direct ratio.'},
                {"text": "The flaw is that Sydney's swing is not half of London's", "correct": False, "why": 'The two figures given, 4.5 and 9.0 hours, genuinely are in a two-to-one ratio; the flaw is elsewhere.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-05-h30',
            "band": 'harder',
            "text": "Summarise, using both the tilt and the lag, why Britain's coldest and hottest points of the year do not land exactly on the December and June solstices.",
            "options": [
                {"text": 'The solstice dates themselves are inaccurate and should fall in late January and late July', "correct": False, "why": "The solstice dates correctly mark the tilt's most extreme lean; it is the temperature response that lags behind them."},
                {"text": "The solstices mark the tilt's extreme lean; the ground then keeps responding for weeks", "correct": True},
                {"text": "Britain's coldest and hottest points do land exactly on the two solstices", "correct": False, "why": 'The extremes typically arrive some weeks after each solstice, not on the solstice dates themselves.'},
                {"text": 'The tilt has no bearing on when the coldest and hottest points of the year occur', "correct": False, "why": 'The tilt sets which weeks are warming or cooling in the first place; the lag then delays the extremes within that pattern.'},
            ],
            "figure": None,
        },
]
