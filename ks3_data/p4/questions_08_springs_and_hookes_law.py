"""P4 lesson 08 — Springs and Hooke's law: twelve questions (MRB-223).

Written against Design's page. The 10 N prediction, the loading bench and
the beam-and-graph are hers.

The discriminations, in the order the lesson builds them:

  · extension is the INCREASE in length, not the length (`FORCE-40`);
  · proportional means the ratio is constant, so scaling up multiplies
    rather than adds (`FORCE-41`);
  · the graph is a straight line THROUGH THE ORIGIN, which is why the
    zero reading matters;
  · the limit of proportionality is not a breaking point (`FORCE-42`);
  · past it the deformation is permanent and does not recover
    (`FORCE-43`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — index cycles 0, 2, 3, 1, giving three of each.

⚠️ Rung 1 (30 mm under 3 N, find 7 N) and Rung 2 (unloading past the
limit) are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "springs-and-hookes-law"
LESSON_NUMBER = 8

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-08-e01",
        "band": "easier",
        "text": "A spring is 50 mm long with nothing on it and 90 mm long "
                "with a load. What is its extension?",
        "options": [
            {"text": "40 mm", "correct": True},
            {"text": "90 mm", "correct": False,
             "why": "That is the stretched LENGTH. Extension is how much "
                    "longer it has become."},
            {"text": "50 mm", "correct": False,
             "why": "That is the natural length — the length before "
                    "anything was hung on it."},
            {"text": "140 mm", "correct": False,
             "why": "That adds the two. Extension is stretched length "
                    "MINUS natural length."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e02",
        "band": "easier",
        "text": "While a spring obeys Hooke's law, a graph of extension "
                "against load is…",
        "options": [
            {"text": "a curve that gets steeper", "correct": False,
             "why": "That is what happens PAST the limit. Within it the "
                    "line is straight."},
            {"text": "a horizontal line", "correct": False,
             "why": "Then adding load would change nothing, which is not "
                    "what a spring does."},
            {"text": "a straight line through the origin", "correct": True},
            {"text": "a straight line that starts partway up the axis",
             "correct": False,
             "why": "That is what you get if you plot total LENGTH instead "
                    "of extension. With no load the extension is zero."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e03",
        "band": "easier",
        "text": "A spring extends 15 mm under 1 N. Staying on the straight "
                "line, what is its extension under 4 N?",
        "options": [
            {"text": "19 mm", "correct": False,
             "why": "That adds the extra 4 on to 15. Load and extension are "
                    "PROPORTIONAL, so they multiply."},
            {"text": "3.75 mm", "correct": False,
             "why": "That is 15 ÷ 4. Four times the load gives four times "
                    "the extension."},
            {"text": "15 mm", "correct": False,
             "why": "More load gives more extension. Nothing would be "
                    "proportional if it stayed the same."},
            {"text": "60 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e04",
        "band": "easier",
        "text": "Why is the first reading in this investigation taken with "
                "NO load on the spring?",
        "options": [
            {"text": "To warm the spring up before it is used.",
             "correct": False,
             "why": "Springs need no warming up, and nothing about the "
                    "reading depends on temperature here."},
            {"text": "To check the ruler is straight.", "correct": False,
             "why": "Useful, but not the reason. The zero reading is a "
                    "measurement in its own right."},
            {"text": "Because it is the natural length, which every "
                     "extension is measured from.", "correct": True},
            {"text": "Because the spring might already be broken.",
             "correct": False,
             "why": "That would show up later. The zero is needed even for a "
                    "perfect spring."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-08-s01",
        "band": "standard",
        "text": "A spring extends 4.5 cm under 3 N. Staying on the straight "
                "line, what is the extension under 8 N, in millimetres?",
        "options": [
            {"text": "12 mm", "correct": False,
             "why": "That works in centimetres and reports millimetres. "
                    "4.5 cm is 45 mm, so each newton gives 15 mm."},
            {"text": "36 mm", "correct": False,
             "why": "That is 4.5 × 8 — the centimetre figure scaled up and "
                    "the unit swapped. Convert first."},
            {"text": "120 mm", "correct": True},
            {"text": "1 200 mm", "correct": False,
             "why": "That multiplies by 10 twice. 4.5 cm is 45 mm, not "
                    "450 mm."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s02",
        "band": "standard",
        "text": "A student plots TOTAL LENGTH against load instead of "
                "extension. What is wrong with the graph?",
        "options": [
            {"text": "It will be a curve rather than a straight line.",
             "correct": False,
             "why": "It is still straight, and that is what makes the error "
                    "so easy to miss."},
            {"text": "It will slope the wrong way.", "correct": False,
             "why": "It slopes upwards exactly as before. The gradient is "
                    "unchanged."},
            {"text": "It will have the axes the wrong way round.",
             "correct": False,
             "why": "The axes are fine. It is the quantity that is wrong."},
            {"text": "It will not go through the origin — it starts at the "
                     "natural length with no load on it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s03",
        "band": "standard",
        "text": "A spring's readings are 20 mm at 1 N, 40 mm at 2 N, 60 mm "
                "at 3 N and 112 mm at 5 N. What does the fourth reading "
                "tell you?",
        "options": [
            {"text": "That the reading was taken wrongly.", "correct": False,
             "why": "It might have been — but the pattern is exactly what "
                    "a spring does past its limit, so the honest first "
                    "reading is that something real has changed."},
            {"text": "That the spring has snapped.", "correct": False,
             "why": "A snapped spring gives no reading at all. This one is "
                    "still holding the load."},
            {"text": "That the limit of proportionality lies somewhere "
                     "between 3 N and 5 N.", "correct": True},
            {"text": "That the spring has become stiffer.", "correct": False,
             "why": "It has become EASIER to stretch — each newton is now "
                    "adding more than 20 mm, not less."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s04",
        "band": "standard",
        "text": "Why can a newton meter have equally spaced marks all the "
                "way along its scale?",
        "options": [
            {"text": "Because the marks are printed before the spring is "
                     "fitted.", "correct": False,
             "why": "They could be printed any way at all. They are equally "
                    "spaced because of what the spring does."},
            {"text": "Because equal increases in force give equal increases "
                     "in extension, while the spring obeys Hooke's law.",
             "correct": True},
            {"text": "Because the spring stretches the same amount whatever "
                     "the load.", "correct": False,
             "why": "Then the scale would be useless — every load would "
                    "read the same."},
            {"text": "Because the scale is a rough guide rather than a "
                     "measurement.", "correct": False,
             "why": "It is a real measurement, and its accuracy depends on "
                    "the proportionality holding."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-08-h01",
        "band": "harder",
        "text": "A spring is loaded past its limit of proportionality and "
                "then completely unloaded. What is true afterwards?",
        "options": [
            {"text": "It is permanently longer than it started.",
             "correct": True},
            {"text": "It has snapped.", "correct": False,
             "why": "The limit is where the arithmetic stops being neat, not "
                    "where the metal fails. Breaking happens much later, if "
                    "at all."},
            {"text": "It returns to its natural length, but more slowly.",
             "correct": False,
             "why": "It is not a matter of time. Wait as long as you like "
                    "and it is still longer."},
            {"text": "It becomes stiffer, so later readings are too small.",
             "correct": False,
             "why": "The problem is the new zero, not the stiffness — the "
                    "instrument reads wrongly even with nothing on it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h02",
        "band": "harder",
        "text": "Someone stands on kitchen scales that weigh up to 5 kg. "
                "What should the owner check afterwards?",
        "options": [
            {"text": "Whether the dial still turns freely.",
             "correct": False,
             "why": "It probably does. The damage is to the reading, not to "
                    "the movement."},
            {"text": "Whether the scales still weigh a 1 kg bag correctly.",
             "correct": False,
             "why": "Closer, but a single check partway up the range can "
                    "still miss a shifted zero."},
            {"text": "Whether the dial still reads zero with nothing on it.",
             "correct": True},
            {"text": "Nothing — kitchen scales are not springs.",
             "correct": False,
             "why": "A dial with equal steps needs something inside "
                    "deforming in proportion, which is exactly a spring."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h03",
        "band": "harder",
        "text": "Hooke published his law in Latin as “as the extension, so "
                "the force”, and only for springs and wires within a certain "
                "range. What does that narrowness show?",
        "options": [
            {"text": "That he had not tested it properly.", "correct": False,
             "why": "He had tested it carefully. The narrowness is a "
                    "consequence of testing carefully, not of failing to."},
            {"text": "That the law was later found to be wrong.",
             "correct": False,
             "why": "It is still used, exactly as he stated it, within the "
                    "range he stated."},
            {"text": "That laws in physics that apply to everything are the "
                     "best kind.", "correct": False,
             "why": "The opposite lesson. A law with no stated range is "
                    "usually one whose limits have not been found yet."},
            {"text": "That an honest law comes with a range attached, and "
                     "the interesting science starts at the edge of it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h04",
        "band": "harder",
        "text": "A car's suspension spring and its crumple zone both deform "
                "under a force. What is the important difference?",
        "options": [
            {"text": "The crumple zone deforms and the spring does not.",
             "correct": False,
             "why": "Both deform. That is the whole point of a suspension "
                    "spring."},
            {"text": "The spring is designed to return to shape and give the "
                     "energy back; the crumple zone is designed NOT to.",
             "correct": True},
            {"text": "The spring is stronger than the crumple zone.",
             "correct": False,
             "why": "Strength is not the difference. Both are engineered for "
                    "the load they meet."},
            {"text": "Only the crumple zone stores energy.", "correct": False,
             "why": "The spring stores it and returns it. The crumple zone "
                    "absorbs it and keeps it, which is what makes it safe."},
        ],
        "figure": None,
    },
]
