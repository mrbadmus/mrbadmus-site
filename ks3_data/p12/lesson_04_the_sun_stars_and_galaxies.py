"""P12 L4 — The Sun, stars and galaxies (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p12/p12-04-the-sun-stars-and-galaxies.dc.html`.

Her page wins outright. The star you can see in daylight, the five rungs
of the distance ladder and all four rungs of the mastery ladder are hers.

── ⚖️ `#s-think` IS THE THIRD RAIL STOP, ON HER OWN PREDICATE ────────

Same shape as `p12-03` and `p12-05`, and the same `space-think` family.
See `ks3_data/p12/__init__.py`.

── ⚖️ RULED · THE STAR COUNTS STAND ──────────────────────────────────

Her NOTES §6 asks whether to quote figures at all rather than an order of
magnitude. **They stand.** "About 200 billion" for the Milky Way, "about a
trillion" for Andromeda and "around two trillion galaxies" are hedged in
her own words, the legal line records that galaxy star counts are
estimates with wide error bars, and an order of magnitude with no number
attached is harder for a student to hold, not easier.

── ⚖️ THE BENCH HAS NO SLIDER, AND THAT IS DRAWN ────────────────────

Her `SLIDER` on this page is the empty array and her `bSliderLabel` is the
empty string, so `Bench.dc.html`'s `hasSlider` is false and the component
draws no slider at all. `r_space_bench` refuses a `distance-ladder`
payload that grows one, because a control Design did not draw is exactly
what MRB-205 forbids.

── ⚖️ TWO FORMATTERS PRINT NUMBERS NO STUDENT SHOULD BE SHOWN ───────

Her `fmtKm` sends anything under a million kilometres through the
million-kilometre branch, so Proxima Centauri — 210 000 km across — reads
**"0.21 million km across"**; and it prints a galaxy width to eight
significant figures, **"100411 ly across"**, for a quantity known to about
ten per cent. Both are fixed and her VALUES are untouched. Registered in
`DEPARTURES-P12.md`.

── ⚖️ THE SOLAR SYSTEM RUNG'S NOTE DISAGREED WITH ITS OWN READOUT ───

Her tab note reads *"Measured out to Neptune. Sunlight takes about four
hours to cross it."* while the same tab's `ly` value is 0.00126, which the
distance readout renders as **11.0 light hours**. Four hours is the light
time from the Sun to Neptune; 11 light hours is about 80 astronomical
units, well beyond it. 5A.1's rule settles which side moves — *the
instrument is the measurement and the prose is what changes* — so the note
now names the boundary the readout actually computes. Her `ly` and her
`dia` are untouched. Registered.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

This lesson takes indices **0 and 2**. Her option TEXT and every
correction are verbatim; only the ORDER moves. Index 0 is used here
because MRB-278 asks that every index be USED across the unit, not that
index 0 be avoided — a student who learns that the first option is never
right has learned a tell of the opposite sign.

── ⚠️ MRB-177 · ONE LENGTH TELL, REMEDIED AT THE DISTRACTOR ──────────

Rung 2's correct option is 28 words against a longest distractor of 14.
All three distractors are FINISHED into complete wrong rules; the correct
answer and every correction are untouched.

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ──────────────────────
"""

LESSON = {
    "slug": "the-sun-stars-and-galaxies",
    "title": "The Sun, stars and galaxies",
    "discipline": "physics",
    "unit": "Space",
    "family": "SYSTEM",

    "covers": ["KS3.P.SPACE.02"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["gravity-earth-moon-and-sun"],
    "assumes": [],
    "references": [{"unit": "P7", "lesson": "light-travels"}],
    "ks4_links": [],

    "meta_description": "A star, a solar system, a galaxy and the universe, "
                        "in order of size — and the steps between them are "
                        "far bigger than they look.",

    "big_question": "Everything you can see with your eyes on a dark night, "
                    "apart from a smudge or two, is inside one galaxy out of "
                    "two trillion. Getting the sizes of things straight is "
                    "most of the work.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "A star you can see in daylight",
         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Five rungs of the ladder",
         "done_when": "gate_and_a_control"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Stars are not in the solar system",
         "done_when": "hook_or_first_rung"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "There is a star you can see in the daytime.",
        "prompt": "It is 150 million kilometres away, it is 1.4 million "
                  "kilometres across, and it is so bright you must never look "
                  "at it directly.",
        "commit": "What kind of object is the Sun?",
        "options": [
            "A planet, because it is round and gives out light",
            "A star, and the only one close enough to see as a disc",
            "A galaxy, because it is so large",
            "Something else entirely — stars are only visible at night",
        ],
        "answer": 1,
        "reveal": "A star, and an ordinary one. The Sun is a ball of hydrogen "
                  "and helium about 1.4 million km across, fusing hydrogen in "
                  "its core and pouring the energy out as light. It looks "
                  "completely unlike the stars you see at night for one "
                  "reason only: it is 270 000 times closer than the next "
                  "nearest. Move the Sun to where Proxima Centauri is and it "
                  "would be a faint dot you would need a dark night to "
                  "notice.",
    },

    "misconceptions": [
        {"id": "SPACE-11",
         "statement": "The Sun is not a star — stars are the small twinkling "
                      "things at night.",
         "elicited_by": "s-hook",
         "confronted_by": "think-the-sun-is-a-star"},
        {"id": "SPACE-12",
         "statement": "Stars are all about the same, and the brighter ones "
                      "are the closer ones.",
         "elicited_by": "s-ladder",
         "confronted_by": "think-the-sun-is-a-star"},
        {"id": "SPACE-13",
         "statement": "The stars you can see at night are part of our solar "
                      "system.",
         "elicited_by": "s-ladder",
         "confronted_by": "bench"},
        {"id": "SPACE-14",
         "statement": "A galaxy is something inside a solar system, because "
                      "the solar system is the whole system.",
         "elicited_by": "bench",
         "confronted_by": "bench"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A <strong>star</strong> is a ball of gas massive enough for "
                 "its own gravity to squeeze the core until hydrogen nuclei "
                 "fuse into helium, releasing energy. The Sun is one, and an "
                 "unremarkable one: hotter and brighter than most stars, far "
                 "cooler and dimmer than the largest."},
        {"type": "explainer",
         "text": "A <strong>solar system</strong> is a star together with "
                 "everything held in orbit around it — planets, moons, "
                 "asteroids, comets and dust. Ours has one star. Most of the "
                 "stars you can see at night have planets of their own, so "
                 "most of them are the middle of a solar system too."},
        {"type": "explainer",
         "text": "A <strong>galaxy</strong> is an enormous collection of "
                 "stars — hundreds of billions of them — held together by "
                 "gravity. Ours is the Milky Way, and the faint band of light "
                 "it is named after is what the disc of it looks like seen "
                 "edge-on from inside. Beyond that there are around two "
                 "trillion other galaxies, and the whole lot together is the "
                 "<strong>universe</strong>."},

        # ── #s-bench · five rungs of the distance ladder ────────────────
        {"type": "space-bench",
         "id": "bench",
         "anchor": "s-bench",
         "eyebrow": "At the bench · five rungs of the distance ladder",
         "heading": "Every step is a huge jump, and the ladder does not stop.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Pick something and see how far away it is, how big it is, "
                 "and how long its light has been travelling. The bars are on "
                 "a scale where each step is ten times the last — otherwise "
                 "the first two would be invisible.",
         "model": "distance-ladder",
         # Design's own log placement, in her own constants. Eleven orders of
         # magnitude on one axis; there is no honest linear way to do it.
         "scale": {"log_offset": 5, "log_span": 11.5, "min_pct": 3},
         "gate": {
             "prompt": "Commit first. Which of these is the correct order, "
                       "smallest first?",
             "options": [
                 "Solar system, galaxy, star, universe",
                 "Star, solar system, galaxy, universe",
                 "Galaxy, universe, solar system, star",
                 "Star, galaxy, solar system, universe",
             ],
             "answer": 1,
         },
         "tabs_label": "What you are looking at",
         "start_tab": 0,
         "tabs": [
             {"id": "sun", "label": "The Sun", "name": "the Sun",
              "kind": "a star", "ly": 0.0000158, "dia": 1.39e6,
              "count": "1 star",
              "note": "An ordinary yellow dwarf, and the only star close "
                      "enough to look like a disc rather than a point."},
             {"id": "system", "label": "The solar system",
              "name": "the solar system",
              "kind": "one star and everything bound to it",
              "ly": 0.00126, "dia": 9e9, "count": "1 star, 8 planets",
              # ⚠️ HER NOTE SAID "Measured out to Neptune. Sunlight takes
              # about four hours to cross it." — which disagrees with the
              # `ly` value beside it, and it is the READOUT that is the
              # measurement (5A.1). See the module note.
              "note": "Measured out well beyond Neptune, whose orbit alone "
                      "is 9000 million km across. Light crosses the whole of "
                      "this in hours rather than years."},
             {"id": "proxima", "label": "Proxima Centauri",
              "name": "Proxima Centauri",
              "kind": "the nearest star to the Sun",
              "ly": 4.24, "dia": 2.1e5, "count": "1 star",
              "note": "A red dwarf. Its light left in the year you were "
                      "about ten."},
             {"id": "milkyway", "label": "The Milky Way",
              "name": "the Milky Way", "kind": "our galaxy",
              "ly": 100000, "dia": 9.5e17,
              "count": "about 200 billion stars",
              "note": "A barred spiral. The Sun is one star in it, about two "
                      "thirds of the way out."},
             {"id": "andromeda", "label": "Andromeda",
              "name": "the Andromeda galaxy",
              "kind": "the nearest large galaxy",
              "ly": 2500000, "dia": 2e18,
              "count": "about a trillion stars",
              "note": "The furthest thing you can see with your eyes alone, "
                      "on a dark night."},
         ],
         "bars_caption": "Distance from Earth in light years — each bar step "
                         "is ten times the one before",
         "bars_alt": "Five bars on a ten-times scale showing distance from "
                     "Earth: {list}. {label} is highlighted.",
         "bars": [
             {"id": "sun",       "label": "The Sun"},
             {"id": "system",    "label": "The solar system"},
             {"id": "proxima",   "label": "Proxima Centauri"},
             {"id": "milkyway",  "label": "The Milky Way"},
             {"id": "andromeda", "label": "Andromeda"},
         ],
         "readouts": [
             {"id": "what",     "label": "What it is"},
             {"id": "distance", "label": "Distance from Earth"},
             {"id": "size",     "label": "Size"},
             {"id": "stars",    "label": "Stars in it"},
         ],
         "words": {
             "what_sub":     "what kind of object this is",
             "distance_sub": "how long its light has been travelling",
             "size_sub":     "across its widest part",
             "stars_sub":    "counted or estimated",
             "list_join":    "and",
         },
         "notes": {
             "rung": "{note} At {dist} from Earth, the light reaching you "
                     "from {name} set out that long ago — so every one of "
                     "these bars is also a look into the past. Notice the "
                     "shape of the ladder: the whole solar system is a "
                     "rounding error next to the gap to the nearest star, and "
                     "that gap is a rounding error next to the width of one "
                     "galaxy. Each rung is not a little further than the "
                     "last. It is thousands of times further.",
         }},

        {"type": "key-fact", "ref": "what-sits-inside-what"},

        {"type": "misconception", "id": "think-the-sun-is-a-star",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-the-sun-is-a-star",
         "kind": "space-think",
         "demand": "explain",
         "targets": "SPACE-11",
         "statements": [
             {"quote": "The Sun is not a star — stars are the small twinkling "
                       "things at night.",
              "targets": "SPACE-11",
              "body": [
                  "The Sun is a star and the twinkling is not even a property "
                  "of the star. It is caused by our own atmosphere: pockets "
                  "of air at different temperatures bend the light this way "
                  "and that on its way down, and a point of light appears to "
                  "shimmer. Planets, which show a tiny disc rather than a "
                  "point, average that shimmer out and shine steadily — which "
                  "is one way of telling a planet from a star without a "
                  "telescope.",
              ]},
             {"quote": "Stars are all about the same, and the brighter ones "
                       "are the closer ones.",
              "targets": "SPACE-12",
              "body": [
                  "Brightness in our sky mixes up two completely different "
                  "things: how much light a star actually gives out, and how "
                  "far away it is. Betelgeuse is around 500 light years away "
                  "and looks bright because it is a red supergiant putting "
                  "out something like 100 000 times the Sun’s light. Proxima "
                  "Centauri is our nearest neighbour at 4.24 light years and "
                  "is far too faint to see without a telescope. Untangling "
                  "those two is one of the central problems of astronomy.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "what-sits-inside-what",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A star is a ball of gas fusing hydrogen in its core; the "
                 "Sun is one. A solar system is a star and everything "
                 "orbiting it. A galaxy is hundreds of billions of stars "
                 "bound together by gravity; ours is the Milky Way. The "
                 "universe is every galaxy there is — around two trillion of "
                 "them."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 2.
    #
    # ⚠️ MRB-177 · RUNG 2'S THREE DISTRACTORS ARE FINISHED into complete
    # wrong rules. The correct answer and every correction are untouched.
    "ladder": {
        "recall": {
            "q": "Put these in order from smallest to largest: galaxy, star, "
                 "solar system, universe.",
            "options": [
                "Star, solar system, galaxy, universe.",
                "Solar system, star, galaxy, universe.",
                "Star, galaxy, solar system, universe.",
                "Solar system, galaxy, star, universe.",
            ],
            "answer": 0,
            "feedback": {
                1: "A star sits inside a solar system, along with its "
                   "planets, so the star is the smaller of the two.",
                2: "A galaxy holds billions of solar systems, so it is far "
                   "larger than one of them.",
                3: "A star is smaller than the solar system around it and "
                   "vastly smaller than the galaxy holding both.",
            },
            "title": "Rung 1 · Order the scales"},
        "apply": {
            "q": "A student says the stars in the night sky are part of our "
                 "solar system. What is wrong?",
            "options": [
                "Nothing is wrong — the solar system contains all the stars "
                "we can see, because a solar system is everything that "
                "surrounds a star.",
                "The stars are in other galaxies, not in our solar system or "
                "our galaxy, because a galaxy holds only one star and its "
                "planets.",
                "The solar system contains exactly one star, the Sun. Every "
                "other star you can see is light years away, far outside it, "
                "and belongs to the Milky Way.",
                "They are part of the solar system, but only the brightest "
                "ones are, because brightness is what shows a star is close "
                "enough to belong.",
            ],
            "answer": 2,
            "feedback": {
                0: "The solar system is the Sun and the objects orbiting it. "
                   "The next star along is 270 000 times further away than "
                   "the Sun.",
                1: "The verdict is right and the detail is wrong. Almost "
                   "every star visible to the naked eye is in the Milky Way.",
                3: "None of them is. Brightness in the sky depends on "
                   "distance as much as on the star itself.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why the Sun looks so different from every other "
                 "star, even though it is an ordinary one.",
            "field_label": "Your explanation",
            "placeholder": "The Sun is a star like the others, but…",
            "success": [
                "Says the Sun is a star, of a fairly ordinary size and "
                "brightness.",
                "Says it is about 150 million km away while the next nearest "
                "star is 4.24 light years away.",
                "Gives a sense of that ratio — roughly 270 000 times "
                "further.",
                "Says brightness falls off sharply with distance, so the Sun "
                "looks overwhelmingly bright.",
                "Says it appears as a disc rather than a point only because "
                "it is close enough to resolve.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Andromeda is 2.5 million light years away. Explain what you "
                 "are actually seeing when you look at it, and why "
                 "astronomers call large telescopes time machines.",
            "field_label": "Your answer",
            "placeholder": "The light entering your eye left Andromeda…",
            "success": [
                "Says the light entering your eye left Andromeda 2.5 million "
                "years ago.",
                "Says you are seeing the galaxy as it was then, not as it is "
                "now.",
                "Says light travels fast but not instantly, so all seeing is "
                "seeing into the past.",
                "Notes that the effect is unnoticeable at everyday distances "
                "and enormous at astronomical ones.",
                "Says looking further away therefore means looking further "
                "back, which is how the early universe is studied.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "The Sun is an ordinary star: a ball of gas fusing hydrogen "
                "into helium in its core. The solar system is the Sun plus "
                "everything orbiting it, and it contains exactly one star. A "
                "galaxy is hundreds of billions of stars held together by "
                "gravity, and ours is the Milky Way. The universe holds "
                "around two trillion galaxies. The steps between these scales "
                "are not small — the nearest star is about 270 000 times "
                "further away than the Sun, and one galaxy is tens of "
                "thousands of light years across.",

    "stretch": [
        {"id": "where-the-sun-sits",
         "type": "explainer",
         "text": "The Milky Way is a barred spiral roughly 100 000 light "
                 "years across, and the Sun sits about 26 000 light years "
                 "from the centre, in a minor spiral arm, taking about 230 "
                 "million years to complete one lap. The last time the Sun "
                 "was in this part of its orbit, the first dinosaurs were "
                 "appearing. At the centre is a black hole of about four "
                 "million solar masses, photographed for the first time in "
                 "2022."},
        {"id": "made-in-a-star",
         "type": "explainer",
         "text": "Almost everything you are made of was made inside a star. "
                 "The hydrogen dates from the first few minutes of the "
                 "universe; the carbon, oxygen, nitrogen and iron were fused "
                 "in stellar cores and scattered by the deaths of stars that "
                 "lived and died before the Sun formed. Heavier elements "
                 "still — gold, platinum, uranium — appear to need the "
                 "collision of two neutron stars. There is no ordinary "
                 "chemistry that makes them."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "star",
         "definition": "A ball of gas massive enough for its own gravity to "
                       "squeeze the core until hydrogen fuses into helium, "
                       "releasing energy. The Sun is one."},
        {"term": "solar system",
         "definition": "A star together with everything held in orbit around "
                       "it — planets, moons, asteroids, comets and dust. Ours "
                       "contains exactly one star."},
        {"term": "galaxy",
         "definition": "An enormous collection of stars, hundreds of billions "
                       "of them, held together by gravity. Ours is the Milky "
                       "Way."},
        {"term": "universe",
         "definition": "Every galaxy there is, and everything in them — "
                       "around two trillion galaxies on current estimates."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Muddled about what sits inside what out there?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Stellar life cycles from nebula to main sequence to white "
                   "dwarf or supernova, nuclear fusion as the source of a "
                   "star’s energy, and red shift as evidence for an expanding "
                   "universe.",

    "convention_note": "The bench is a teaching model. Distances and sizes "
                       "are accepted current figures rounded for display: the "
                       "Sun 150 million km away and 1.39 million km across; "
                       "Neptune’s orbit about 4.5 billion km from the Sun; "
                       "Proxima Centauri 4.24 light years; the Milky Way "
                       "about 100 000 light years across; Andromeda about 2.5 "
                       "million light years away. Star counts for galaxies "
                       "are estimates with wide error bars. The bars use a "
                       "logarithmic scale so that quantities spanning eleven "
                       "orders of magnitude can be shown together.",

    "ws": ["measurement"],
}
