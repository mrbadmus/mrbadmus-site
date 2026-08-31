"""P12 L3 — Gravity between Earth, Moon and Sun (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p12/p12-03-gravity-earth-moon-and-sun.dc.html`.

Her page wins outright. The falling Moon, the four gravitational pairs,
the separation multiplier and all four rungs are hers.

── ⚖️ `#s-think` IS THE THIRD RAIL STOP, ON HER OWN PREDICATE ────────

    if (id === 's-think') return s.answers.r1 !== null ||
                                 s.hookChoice !== null;

The hook is ABOVE this section and the ladder is BELOW it, so the stop is
completable from either side without touching the confrontation itself.
That is right for a block whose job is to be READ, and it is why the
section takes P12's own `space-think` family and its own wire function
rather than `mirrors` (her expression is not the bench's, so
`ks3_rail_manifest` derives no mirror and a declared one fails
`check_rail_matches_design`) or `band_anchor` (the bench cannot satisfy her
predicate). See `ks3_data/p12/__init__.py`.

── ⚖️ RULED · THE FORCES STAND IN `10^20` NOTATION ───────────────────

Her NOTES §6 asks whether `1.98 × 10^20 N` is too early for KS3, or
whether words would be better. **It stands as drawn.** The figures are
READOUTS the bench computes rather than arithmetic a student is asked to
do; rung 2 asks whether the two pulls in a pair are equal, which is a
question about equality and not about a calculation; and standard form is
KS3 maths. Powers of ten are typed `10^20`, which is her own §5
convention: U+2070 and U+2074–U+2079 are absent from every shipped font
subset.

── ⚖️ THE FRACTION IS A WORD, AND THAT IS A FIX ──────────────────────

Design's bar sub-line is built as `'a ' + (n * n) + 'th of full strength'`,
which renders **"a 4th"**, **"a 9th"** and **"a 16th"** — while her own
`aria-label` for the same three bars says *"a quarter, a ninth and a
sixteenth"*. Her note is worse: `'it does not fall to a ' + V + 'th of its
value'` renders *"a 2th"* at the second position. The words are authored
on the slider positions now, and the drawing is otherwise untouched.
Registered in `DEPARTURES-P12.md`.

── ⚠️ `CHRG-07` IS THE SAME SHAPE AND IS NOT REUSED ──────────────────

The `CHRG` family's own note predicts this arrival: *"`CHRG-07` is the
same shape as any inverse-square belief and will reappear in P12's gravity
lessons."* It is not reused, because `CHRG-07`'s statement names CHARGES
and that sentence is not true of gravity — an id is one belief in one set
of words. `SPACE-10` is minted and the cross-family edge is recorded, on
the `ENER-03` / `PTAB-07` precedent.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

This lesson takes indices **3 and 1**. Her option TEXT and every
correction are verbatim; only the ORDER moves.

── ⚠️ MRB-177 · ONE LENGTH TELL, REMEDIED AT THE DISTRACTOR ──────────

Rung 2's correct option is 24 words against a longest distractor of 13.
All three distractors are FINISHED into complete wrong rules; the correct
answer and every correction are untouched.

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ──────────────────────
"""

LESSON = {
    "slug": "gravity-earth-moon-and-sun",
    "title": "Gravity between Earth, Moon and Sun",
    "discipline": "physics",
    "unit": "Space",
    "family": "MODEL",

    "covers": ["KS3.P.SPACE.01c"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["mass-vs-weight"],
    "assumes": [],
    "references": [{"unit": "P4", "lesson": "non-contact-forces"},
                   {"unit": "P4", "lesson": "what-forces-do-to-motion"}],
    "ks4_links": [],

    "meta_description": "Gravity pulls between any two masses, in equal and "
                        "opposite pairs, and falls off as the square of the "
                        "distance — which is what an orbit is made of.",

    "big_question": "The Earth pulls the Moon with two hundred billion "
                    "billion newtons and the Moon has not moved any closer in "
                    "four billion years. Both of those statements are true, "
                    "and understanding why is most of what orbits are.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Why the Moon does not fall", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Four pulls, one law",  "done_when": "gate_and_a_control"},
        # ⚠️ Design's `DONE` gives this stop the HOOK or ladder rung 1 —
        # neither of which the bench can see — so it is ticked by
        # `wireSpaceThink` and not by `mirrors` or `band_anchor`.
        {"anchor": "s-think",  "short": "THINK",
         "label": "Pulls come in pairs",  "done_when": "hook_or_first_rung"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",       "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The Moon has been falling towards us since before there "
                 "were fish.",
        "prompt": "The Earth’s gravity reaches the Moon and pulls on it hard "
                  "— about 2 × 10^20 N, every second of every day. The Moon "
                  "is 384 400 km away and has stayed at roughly that distance "
                  "for four billion years.",
        "commit": "Why has it not arrived?",
        "options": [
            "The Earth is not really pulling it — it is far too far away",
            "Something is pushing it outwards and balancing the pull exactly",
            "It is falling, and missing the Earth because it is moving "
            "sideways",
            "It is held up by the Sun pulling it the other way instead",
        ],
        "answer": 2,
        "reveal": "It is falling, and missing. The Earth pulls the Moon with "
                  "about 2 × 10^20 N, which is enormous, and the Moon is "
                  "moving sideways at about 1 km/s. Left alone the pull would "
                  "bring it straight down; left alone the sideways motion "
                  "would take it off into space in a straight line. The two "
                  "together curve its path into an orbit, and the Moon spends "
                  "every moment falling towards a planet that keeps curving "
                  "away underneath it. Nothing pushes outwards and nothing "
                  "balances anything.",
    },

    "misconceptions": [
        {"id": "SPACE-08",
         "statement": "The Moon is held up by a balance between gravity "
                      "pulling it in and a force flinging it out.",
         "elicited_by": "s-hook",
         "confronted_by": "think-orbit-is-not-a-balance"},
        # ⚠️ FORCE-45 IS NOT RE-MINTED. Her second quote is word for word the
        # belief `p4-09 non-contact-forces` already owns, so it takes a
        # second register row with the IDENTICAL statement and no new number.
        {"id": "FORCE-45",
         "statement": "There is no gravity in space.",
         "confronted_by": "think-orbit-is-not-a-balance"},
        {"id": "SPACE-09",
         "statement": "The bigger body pulls harder, so the Sun pulls the "
                      "Earth far more than the Earth pulls the Sun.",
         "elicited_by": "bench",
         "confronted_by": "bench"},
        {"id": "SPACE-10",
         "statement": "Gravity falls in step with the distance, so twice as "
                      "far apart means half the pull.",
         "elicited_by": "s-ladder",
         "confronted_by": "bench"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Gravity is an <strong>attraction between any two "
                 "masses</strong>. It never pushes, it never switches off, "
                 "and it acts across empty space with nothing in between. "
                 "Every object in the universe is pulling on every other "
                 "object, including you and this page."},
        {"type": "explainer",
         "text": "Two things set how strong the pull is. Bigger masses pull "
                 "harder — both masses count, not just the larger one. And "
                 "distance weakens it fast: <strong>double the separation and "
                 "the pull falls to a quarter</strong>, treble it and the "
                 "pull falls to a ninth. That is called an inverse square "
                 "law, and it is why gravity dominates at the scale of "
                 "planets and is undetectable between two people standing "
                 "next to each other."},
        {"type": "explainer",
         "text": "A gravitational pull always comes as a pair of equal and "
                 "opposite forces. The Sun pulls the Earth and the Earth "
                 "pulls the Sun, with exactly the same number of newtons. "
                 "What differs is the result: the same force barely stirs a "
                 "body of two thousand trillion trillion kilograms and swings "
                 "a smaller one right round it."},

        # ── #s-bench · four gravitational pulls, and distance ───────────
        {"type": "space-bench",
         "id": "bench",
         "anchor": "s-bench",
         "eyebrow": "At the bench · four gravitational pulls, and what "
                    "distance does to them",
         "heading": "Double the distance, quarter the pull.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Choose a pull and then move the two bodies further apart. "
                 "Every bar is the same pull at a different separation, and "
                 "the drop-off is steeper than most people expect.",
         "model": "inverse-square",
         "gate": {
             "prompt": "Commit first. The Sun pulls the Earth. How hard does "
                       "the Earth pull the Sun?",
             "options": [
                 "Far less, because the Earth is far smaller",
                 "Exactly as hard, in the opposite direction",
                 "About a third as hard",
                 "Not at all — only the bigger body pulls",
             ],
             "answer": 1,
         },
         "tabs_label": "The pull you are looking at",
         "start_tab": 0,
         "tabs": [
             {"id": "em", "label": "Earth pulls the Moon",
              "name": "the pull of the Earth on the Moon", "f": 1.98e20,
              "partner": "the Moon pulls the Earth with exactly the same "
                         "force"},
             {"id": "me", "label": "The Moon pulls the Earth",
              "name": "the pull of the Moon on the Earth", "f": 1.98e20,
              "partner": "the Earth pulls the Moon with exactly the same "
                         "force"},
             {"id": "se", "label": "The Sun pulls the Earth",
              "name": "the pull of the Sun on the Earth", "f": 3.54e22,
              "partner": "the Earth pulls the Sun with exactly the same "
                         "force"},
             {"id": "sm", "label": "The Sun pulls the Moon",
              "name": "the pull of the Sun on the Moon", "f": 4.36e20,
              "partner": "the Moon pulls the Sun with exactly the same "
                         "force"},
         ],
         "slider": {
             "id": "sep",
             "label": "Separation, as a multiple of the real one",
             "value_label": "{label}",
             "start": 0,
             # ⚠️ `frac` AND `inv` ARE WORDS, NOT DIGITS. See the module note:
             # Design builds both from `n` and `n * n` with the suffix "th",
             # which renders "a 2th" and "a 4th".
             "values": [
                 {"id": "x1", "label": "× 1", "n": 1},
                 {"id": "x2", "label": "× 2", "n": 2,
                  "inv": "a half", "frac": "a quarter"},
                 {"id": "x3", "label": "× 3", "n": 3,
                  "inv": "a third", "frac": "a ninth"},
                 {"id": "x4", "label": "× 4", "n": 4,
                  "inv": "a quarter", "frac": "a sixteenth"},
             ],
         },
         "bars_caption": "The same pull at one, two, three and four times the "
                         "real separation",
         "bars_alt": "One gravitational pull at four separations: {list}. "
                     "{name} is being shown.",
         "bars": [
             {"id": "x1", "label": "The real separation"},
             {"id": "x2", "label": "2 × further apart"},
             {"id": "x3", "label": "3 × further apart"},
             {"id": "x4", "label": "4 × further apart"},
         ],
         "readouts": [
             {"id": "pull",     "label": "The pull"},
             {"id": "real",     "label": "At the real distance"},
             {"id": "multiple", "label": "At × {n} the distance"},
             {"id": "partner",  "label": "The partner pull"},
         ],
         "words": {
             "pull_value":    "gravity",
             "real_sub":      "attraction, always",
             "multiple_sub":  "divided by {n2}",
             # ⚠️ THE RESTING STATE OF THIS TILE IS THE ONE A STUDENT MEETS
             # FIRST, and Design's template renders it "divided by 1" — true,
             # empty, and the first thing on a bench whose whole subject is
             # division. Her own bar list already has a word for the
             # undivided case ("full strength"), so this is her treatment
             # applied one tile over rather than a new idea.
             "multiple_sub_real": "not divided at all",
             "partner_value": "the same size",
             "partner_sub":   "in the opposite direction",
             "bar_full":      "full strength",
             "bar_frac":      "{frac} of full strength",
             "list_join":     "and",
         },
         "notes": {
             "real": "Gravity is an attraction between any two masses, and it "
                     "never pushes. {Name} is about {f} at the real "
                     "separation, and {partner} — the two are a pair, and "
                     "always equal. Move the slider and watch what distance "
                     "does.",
             "moved": "Gravity is an attraction between any two masses, and "
                      "it never pushes. {Name} is about {f} at the real "
                      "separation, and {partner} — the two are a pair, and "
                      "always equal. Move the bodies {n} times further apart "
                      "and the pull does not fall to {inv} of its value; it "
                      "falls to {frac}, because doubling the distance "
                      "quarters the pull. That is the inverse square law, and "
                      "it is why the Sun can dominate the whole solar system "
                      "and still let Pluto crawl round it once every 248 "
                      "years.",
         }},

        {"type": "key-fact", "ref": "gravity-pulls-in-pairs"},

        {"type": "misconception", "id": "think-orbit-is-not-a-balance",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        # ⚠️ P12's OWN `space-think`, NOT the ordinary `predict`. `#s-think`
        # IS a rail stop on this page, so the section has to declare
        # `data-stage-done="0"` in the shipped bytes and has to be tickable.
        # See `ks3_art/p12.py`.
        {"id": "think-orbit-is-not-a-balance",
         "kind": "space-think",
         "demand": "explain",
         "targets": "SPACE-08",
         "statements": [
             {"quote": "The Moon is held up by a balance between gravity "
                       "pulling in and a force flinging it out.",
              "targets": "SPACE-08",
              "body": [
                  "There is no outward force. If the pull were balanced the "
                  "Moon would travel in a straight line, and a straight line "
                  "leaves the Earth behind. Gravity is unbalanced, "
                  "constantly, and that is precisely why the Moon’s path "
                  "curves. The outward feeling you get on a fairground ride "
                  "is your body carrying on straight while the ride turns you "
                  "— nothing is pulling you outwards there either.",
              ]},
             {"quote": "There is no gravity in space.",
              "targets": "FORCE-45",
              "body": [
                  "Gravity is what holds every moon to its planet, every "
                  "planet to its star and every star to its galaxy — all of "
                  "which happens in space. It gets weaker with distance and "
                  "never reaches zero. What astronauts experience is not the "
                  "absence of gravity but free fall: they and their "
                  "spacecraft are falling together, so nothing presses them "
                  "against anything, and the sensation of weight vanishes "
                  "while the pull continues.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "gravity-pulls-in-pairs",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Gravity is an attraction between any two masses. It gets "
                 "stronger with either mass and weaker with distance as an "
                 "inverse square — double the distance, quarter the pull. The "
                 "two forces in a gravitational pair are always equal and "
                 "opposite. An orbit is a body falling towards another and "
                 "moving sideways fast enough to keep missing it."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 3 and 1.
    #
    # ⚠️ MRB-177 · RUNG 2'S THREE DISTRACTORS ARE FINISHED into complete
    # wrong rules. The correct answer and every correction are untouched.
    "ladder": {
        "recall": {
            "q": "Two spacecraft drift apart until they are three times as "
                 "far from each other as they started. What has happened to "
                 "the gravitational pull between them?",
            "options": [
                "It has fallen to a third of what it was.",
                "It has fallen to nothing, because they are no longer "
                "touching.",
                "It has trebled, because there is more space for gravity to "
                "act across.",
                "It has fallen to a ninth of what it was.",
            ],
            "answer": 3,
            "feedback": {
                0: "Gravity follows an inverse square law: divide by the "
                   "distance factor squared, so three times the distance "
                   "means a ninth of the pull.",
                1: "Gravity is a non-contact force and never falls to "
                   "nothing. It gets weaker with distance, however far you "
                   "go.",
                2: "More distance means less pull, not more.",
            },
            "title": "Rung 1 · Read the model"},
        "apply": {
            "q": "The Sun pulls the Earth with about 3.5 × 10^22 N. How hard "
                 "does the Earth pull the Sun?",
            "options": [
                "Far less, because the Earth has a tiny fraction of the "
                "Sun’s mass, and how hard a body pulls is set by its own "
                "mass.",
                "With the same 3.5 × 10^22 N, in the opposite direction. "
                "Gravitational pulls always come in equal pairs, however "
                "different the two masses are.",
                "It does not pull the Sun at all — only large bodies pull, "
                "and a small one simply responds to whatever is pulling it.",
                "About a millionth as hard, in proportion to the masses, "
                "because each body pulls in the same ratio as the matter it "
                "holds.",
            ],
            "answer": 1,
            "feedback": {
                0: "The two masses both appear in the same calculation, so "
                   "the pair of forces is equal. What differs is the effect: "
                   "the same force moves the small body far more.",
                2: "Every mass attracts every other mass. You are pulling the "
                   "Earth up as hard as it is pulling you down.",
                3: "The forces are equal. The accelerations are what differ "
                   "in proportion to the masses.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why the Moon stays in orbit rather than falling "
                 "into the Earth or flying off into space.",
            "field_label": "Your explanation",
            "placeholder": "The Earth pulls the Moon, and the Moon is also…",
            "success": [
                "Says the Earth’s gravity pulls the Moon towards the Earth.",
                "Says the Moon is also moving sideways, at about 1 km/s.",
                "Says that without the pull the Moon would carry on in a "
                "straight line.",
                "Says that without the sideways motion the Moon would fall "
                "straight in.",
                "Says the combination curves the path into an orbit — the "
                "Moon is falling and continually missing.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "The Sun pulls the Moon about twice as hard as the Earth "
                 "does. Explain why the Moon still orbits the Earth rather "
                 "than being pulled away.",
            "field_label": "Your answer",
            "placeholder": "Both the Earth and the Moon are being pulled by "
                           "the Sun, so…",
            "success": [
                "Says the Sun pulls the Earth and the Moon at almost the same "
                "strength, because they are almost the same distance from it.",
                "Says both bodies are therefore accelerated towards the Sun "
                "by almost the same amount.",
                "Says what matters for the Moon’s orbit is the difference "
                "between the two pulls, not the size of either.",
                "Says that difference is small, so relative to the Earth the "
                "Moon feels mainly the Earth’s pull.",
                "Says the Earth and Moon together orbit the Sun, with the "
                "Moon orbiting the Earth at the same time.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Gravity is an attractive force between any two masses, "
                "acting across empty space. It is stronger for larger masses "
                "and falls off as an inverse square with distance, so twice "
                "as far apart means a quarter of the pull. The forces come in "
                "equal and opposite pairs: the Sun pulls the Earth exactly as "
                "hard as the Earth pulls the Sun. An orbit is the result of a "
                "gravitational pull and a sideways motion together — the "
                "orbiting body is permanently falling and permanently "
                "missing.",

    "stretch": [
        {"id": "the-barycentre",
         "type": "explainer",
         "text": "The Moon does not go round the Earth so much as the two go "
                 "round each other, about a point called the barycentre. "
                 "Because the Earth is eighty-one times the more massive, "
                 "that point lies inside the Earth, about 1700 km below the "
                 "surface — so the wobble is real but hidden. For Pluto and "
                 "Charon the barycentre is outside both bodies, and the pair "
                 "genuinely circle a point in empty space."},
        {"id": "tides-are-a-difference",
         "type": "explainer",
         "text": "The same pull, arriving slightly harder on the near side of "
                 "the Earth than the far side, is what raises the tides. The "
                 "difference between those two pulls is what does the work, "
                 "which is why the Moon — far smaller than the Sun but far "
                 "closer — has more than twice the tidal effect. When the two "
                 "line up you get the large spring tides, and when they pull "
                 "at right angles you get the small neap ones."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "gravity",
         "definition": "An attraction between any two masses. It never "
                       "pushes, never switches off, and acts across empty "
                       "space with nothing in between."},
        {"term": "inverse square law",
         "definition": "A relationship in which doubling the distance cuts "
                       "the effect to a quarter and trebling it cuts the "
                       "effect to a ninth. Gravity follows one."},
        {"term": "orbit",
         "definition": "The curved path of a body that is being pulled "
                       "towards another while moving sideways fast enough to "
                       "keep missing it."},
        {"term": "free fall",
         "definition": "Moving under gravity alone, with nothing pushing "
                       "back. Everything in a falling spacecraft falls "
                       "together, which is why nothing presses on anything."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Wondering why an orbit is not a balance of forces?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Circular motion at constant speed with a changing "
                   "velocity, gravity as the centripetal force, and orbital "
                   "radius against orbital speed.",

    "convention_note": "The bench is a teaching model. Forces are calculated "
                       "from Newton’s law of gravitation using accepted "
                       "masses and mean separations, and are rounded to three "
                       "significant figures: Earth–Moon 1.98 × 10^20 N, "
                       "Sun–Earth 3.54 × 10^22 N and Sun–Moon 4.36 × 10^20 N. "
                       "Real separations vary over each orbit, so the true "
                       "forces vary by a few per cent through the month and "
                       "the year. The separation multiplier is a thought "
                       "experiment: moving these bodies apart would change "
                       "their orbits entirely.",

    "ws": ["measurement"],
}
