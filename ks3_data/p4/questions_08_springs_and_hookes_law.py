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
            {"text": "To warm the spring up before it is used, because a "
                     "cold spring would not stretch at all.",
             "correct": False,
             "why": "A spring at room temperature stretches perfectly well. "
                    "Nothing here depends on how warm it is."},
            {"text": "To check the ruler is straight, because a bent scale "
                     "would spoil every reading.", "correct": False,
             "why": "Useful, but not the reason. The zero reading is a "
                    "measurement in its own right."},
            {"text": "Because it is the natural length, which every "
                     "extension is measured from.", "correct": True},
            # ⊕ MRB-297 · 1 Sep 2026 — THIS `why` TAUGHT THE NEGATION OF THE
            # LESSON'S OWN CREDITED CRITERION, AND THIS RUN WROTE IT. It
            # read "A broken spring shows itself the moment a load goes on.
            # The zero is needed even for a perfect spring." The first
            # sentence is false: a permanently stretched spring reads
            # plausibly UNDER load — that is exactly why it is dangerous —
            # and what gives it away is that it no longer returns to zero.
            # `lesson_08_springs_and_hookes_law.py` credits precisely that:
            # "Says to check that the dial still reads zero with nothing on
            # it, because a permanently deformed spring reads wrongly for
            # ever." So a student who had learnt the lesson was told here
            # that the check they had just been taught looks the wrong way.
            # The rebuttal stands without the false claim: spotting a ruined
            # spring is a real use of the zero reading, but it is not the
            # REASON you always take one.
            {"text": "Because the spring might already be broken, which "
                     "only a zero reading would reveal.",
             "correct": False,
             "why": "True as far as it goes — a stretched spring reads "
                    "plausibly under load and only gives itself away at "
                    "zero. But that is not the reason: the zero is needed "
                    "on a perfect spring too."},
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
            {"text": "It will be a curve rather than a straight line, "
                     "because springs get harder to stretch from the very "
                     "first newton",
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
            {"text": "That the reading was taken wrongly and should be "
                     "measured again", "correct": False,
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
                     "measurement, so any reading off it is an estimate", "correct": False,
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
                     "best kind, and one with a limit is a weaker law", "correct": False,
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
            {"text": "The crumple zone deforms and the spring does not, "
                     "which is the whole of the difference between the two "
                     "of them",
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-08-e05",
        "band": "easier",
        "text": "A spring is 60 mm long with nothing on it and 105 mm long "
                "with a load hanging from it. What is its extension?",
        "options": [
            {"text": "105 mm, the length with the load on", "correct": False,
             "why": "That is the total length. Extension is the INCREASE in "
                    "length."},
            {"text": "165 mm, the two lengths added", "correct": False,
             "why": "Adding the two lengths gives a spring longer than it "
                    "ever was."},
            {"text": "45 mm, the increase in length", "correct": True},
            {"text": "60 mm, the length it started at", "correct": False,
             "why": "That is the natural length, which is what the extension "
                    "is measured from."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-08-s05",
        "band": "standard",
        "text": "A spring extends 24 mm under a 4 N load. Staying on the "
                "straight line, which load gives an extension of 42 mm?",
        "options": [
            {"text": "7 N", "correct": True},
            {"text": "18 N, the difference in the extensions",
             "correct": False,
             "why": "42 − 24 is a difference in millimetres, not a load in "
                    "newtons."},
            {"text": "6 N, because 42 is 18 more than 24", "correct": False,
             "why": "Adding 18 mm as if it were 2 N ignores that each newton "
                    "adds 6 mm."},
            {"text": "10.5 N", "correct": False,
             "why": "That is 42 ÷ 4, dividing the extension by the load "
                    "instead of using 6 mm per newton."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-08-h05",
        "band": "harder",
        "text": "A spring gives 10 mm at 2 N, 20 mm at 4 N, 30 mm at 6 N and "
                "48 mm at 8 N. What has happened by the last reading?",
        "options": [
            {"text": "The spring has snapped", "correct": False,
             "why": "A snapped spring gives no reading at all, and this one "
                    "gave 48 mm."},
            {"text": "The last reading must be a mistake and should be "
                     "discarded",
             "correct": False,
             "why": "It is a real result, and throwing it away would hide the "
                    "very thing it shows."},
            {"text": "The limit of proportionality has been passed",
             "correct": True},
            {"text": "The spring has become stiffer, so it extends less than "
                     "expected",
             "correct": False,
             "why": "40 mm was expected and 48 mm was measured, so it "
                    "extended MORE, not less."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · easier ────────────────────────────────
    {
        "id": "p4-08-e06",
        "band": "easier",
        "text": "Before any weight is hung on it, a garage door spring "
                "measures 20 mm. Once weighted, a ruler alongside it reads "
                "48 mm. By how much has the spring stretched?",
        "options": [
            {"text": "28 mm", "correct": True},
            {"text": "48 mm", "correct": False,
             "why": "That is the stretched length, not how much longer it "
                    "has become."},
            {"text": "20 mm", "correct": False,
             "why": "That is the natural length, which is what the "
                    "extension is measured from."},
            {"text": "68 mm", "correct": False,
             "why": "That adds the two lengths together — extension is the "
                    "stretched length minus the natural length."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e07",
        "band": "easier",
        "text": "What does it mean to say a spring's extension is "
                "'proportional' to the load?",
        "options": [
            {"text": "That the two add up to a constant total", "correct": False,
             "why": "Proportional means they keep the same RATIO, not a "
                    "constant sum."},
            {"text": "That doubling the load doubles the extension, and so "
                     "on", "correct": True},
            {"text": "That the extension eventually becomes bigger than the "
                     "load", "correct": False,
             "why": "Being bigger is not what proportional means — it is "
                    "about the ratio staying the same as both change."},
            {"text": "That the extension stays the same no matter what load "
                     "is added", "correct": False,
             "why": "If the extension never changed, it would not be "
                    "following the load in any proportional way at all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e08",
        "band": "easier",
        "text": "A bungee cord extends 8 mm under a 2 N pull. Staying on "
                "the straight line, what is its extension under 6 N?",
        "options": [
            {"text": "12 mm", "correct": False,
             "why": "That adds the extra load onto the extension rather "
                    "than scaling the whole reading by the same ratio."},
            {"text": "2.67 mm", "correct": False,
             "why": "That divides instead of multiplying by the load "
                    "ratio."},
            {"text": "24 mm", "correct": True},
            {"text": "8 mm", "correct": False,
             "why": "That leaves the extension unchanged, but three times "
                    "the load gives three times the extension."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e09",
        "band": "easier",
        "text": "An elastic exercise band stretches 12 mm under a 3 N pull. "
                "Staying on the straight line, what extension would 9 N "
                "give?",
        "options": [
            {"text": "15 mm", "correct": False,
             "why": "That adds the extra load rather than scaling the "
                    "extension by the same factor."},
            {"text": "4 mm", "correct": False,
             "why": "That divides instead of multiplying by the load "
                    "ratio."},
            {"text": "12 mm", "correct": False,
             "why": "That leaves it unchanged, but three times the load "
                    "gives three times the extension."},
            {"text": "36 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e10",
        "band": "easier",
        "text": "A fishing line's stretch is measured before and after a "
                "catch. It reads 250 mm with no fish on it and 268 mm with "
                "the fish hanging from it. What is the extension?",
        "options": [
            {"text": "18 mm", "correct": True},
            {"text": "268 mm", "correct": False,
             "why": "That is the stretched length, not the increase."},
            {"text": "250 mm", "correct": False,
             "why": "That is the natural length, before the fish was "
                    "attached."},
            {"text": "518 mm", "correct": False,
             "why": "That adds the two lengths together — the extension is "
                    "the difference between them."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e11",
        "band": "easier",
        "text": "What does the word 'extension' mean for a stretched "
                "spring?",
        "options": [
            {"text": "The total length of the stretched spring",
             "correct": False,
             "why": "That is the stretched length. Extension is how much "
                    "LONGER it has become."},
            {"text": "How much longer the spring has become", "correct": True},
            {"text": "The natural length of the spring before anything is "
                     "hung on it", "correct": False,
             "why": "That is the starting length, which extension is "
                    "measured from, not the extension itself."},
            {"text": "The weight of anything hanging from the spring",
             "correct": False,
             "why": "Weight is the load causing the stretch, not the "
                    "stretch itself."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e12",
        "band": "easier",
        "text": "What is the limit of proportionality?",
        "options": [
            {"text": "The exact point at which the spring is expected to "
                     "snap completely in two", "correct": False,
             "why": "Breaking happens much later, if at all — the limit is "
                    "not a breaking point."},
            {"text": "The heaviest load that a spring's manufacturer ever "
                     "designs it to carry safely", "correct": False,
             "why": "Design limits are set by engineers; the limit of "
                    "proportionality is a property of how the spring "
                    "itself behaves."},
            {"text": "The load beyond which extension stops being "
                     "proportional to load", "correct": True},
            {"text": "The particular load at which a spring is expected "
                     "to visibly change its shape or colour", "correct": False,
             "why": "Nothing changes to look at — the coils still look the "
                    "same. What changes is whether the graph stays a "
                    "straight line."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e13",
        "band": "easier",
        "text": "What does Hooke's law state, while it applies?",
        "options": [
            {"text": "Load and extension add up to a fixed total",
             "correct": False,
             "why": "They do not add to a fixed total — they stay in the "
                    "same RATIO as each other."},
            {"text": "Extension consistently exceeds load", "correct": False,
             "why": "Being bigger than the load is not what the law says — "
                    "it is about the two staying in proportion."},
            {"text": "The spring gets stiffer the more it is loaded",
             "correct": False,
             "why": "While Hooke's law holds, the spring's stiffness does "
                    "not change — that is exactly why the graph is a "
                    "straight line."},
            {"text": "Extension is proportional to load", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e14",
        "band": "easier",
        "text": "A curtain spring is 15 mm long with no curtain on it and "
                "52 mm long once the curtain is hung. What is its "
                "extension?",
        "options": [
            {"text": "37 mm", "correct": True},
            {"text": "52 mm", "correct": False,
             "why": "That is the stretched length, not the increase."},
            {"text": "15 mm", "correct": False,
             "why": "That is the natural length, before the curtain was "
                    "hung."},
            {"text": "67 mm", "correct": False,
             "why": "That adds the two lengths together."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e15",
        "band": "easier",
        "text": "A chest-expander exerciser stretches 15 mm under a 5 N "
                "pull. Staying on the straight line, what extension would "
                "15 N give?",
        "options": [
            {"text": "45 mm", "correct": True},
            {"text": "20 mm", "correct": False,
             "why": "That adds the extra load rather than scaling by the "
                    "same ratio."},
            {"text": "5 mm", "correct": False,
             "why": "That divides instead of multiplying by the load "
                    "ratio."},
            {"text": "15 mm", "correct": False,
             "why": "That leaves it unchanged, but three times the load "
                    "gives three times the extension."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e16",
        "band": "easier",
        "text": "Which of these is proportional to which, while a spring "
                "obeys Hooke's law?",
        "options": [
            {"text": "Extension is proportional to the spring's natural "
                     "length", "correct": False,
             "why": "The natural length is fixed for a given spring — it "
                    "does not change with the load."},
            {"text": "Load is proportional to the spring's stiffness",
             "correct": False,
             "why": "Stiffness is a fixed property of the spring — it is "
                    "not something that changes as more load is added."},
            {"text": "Extension is proportional to load", "correct": True},
            {"text": "The natural length is proportional to the extension",
             "correct": False,
             "why": "The natural length is fixed and does not grow as more "
                    "load is added — it is the extension that grows in "
                    "proportion to the load."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e17",
        "band": "easier",
        "text": "A spring's natural length is 25 mm. Once stretched under a "
                "load it measures 61 mm. What is the extension?",
        "options": [
            {"text": "61 mm", "correct": False,
             "why": "That is the stretched length, not the increase."},
            {"text": "25 mm", "correct": False,
             "why": "That is the natural length, before any load."},
            {"text": "86 mm", "correct": False,
             "why": "That adds the two lengths together."},
            {"text": "36 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e18",
        "band": "easier",
        "text": "A luggage scale's hook drops 8 mm under a 2 N pull. "
                "Staying on the straight line, what drop would 8 N give?",
        "options": [
            {"text": "32 mm", "correct": True},
            {"text": "14 mm", "correct": False,
             "why": "That adds the extra load onto the drop rather than "
                    "scaling it by the ratio."},
            {"text": "2 mm", "correct": False,
             "why": "That divides instead of multiplying by the load "
                    "ratio."},
            {"text": "8 mm", "correct": False,
             "why": "That leaves it unchanged, but four times the load "
                    "gives four times the drop."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e19",
        "band": "easier",
        "text": "A newton meter is used correctly and gently, well within "
                "its marked range. What should happen if you remove the "
                "load and check the reading?",
        "options": [
            {"text": "It should read a small positive number", "correct": False,
             "why": "A spring behaving properly returns exactly to its "
                    "starting point once the load is removed."},
            {"text": "It should read a small negative number", "correct": False,
             "why": "A normal, undamaged spring returns exactly to zero — "
                    "it does not overshoot the other way."},
            {"text": "It should read zero", "correct": True},
            {"text": "It depends on how heavy the load was", "correct": False,
             "why": "As long as the spring was kept within its limit of "
                    "proportionality, it returns to zero whatever the load "
                    "was."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e20",
        "band": "easier",
        "text": "What does the very first reading, taken with no load "
                "hanging on the spring, actually measure?",
        "options": [
            {"text": "How much the spring will eventually stretch",
             "correct": False,
             "why": "A single reading with no load says nothing about how "
                    "far the spring will stretch under any load — it only "
                    "fixes a starting point."},
            {"text": "The overall weight of the spring itself",
             "correct": False,
             "why": "A ruler reading tells you a length, not a weight — "
                    "the spring's own weight is not being measured here."},
            {"text": "The natural length of the spring", "correct": True},
            {"text": "The limit of proportionality", "correct": False,
             "why": "The limit is found much later, from readings taken as "
                    "load is added, not from the very first, unloaded "
                    "one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e21",
        "band": "easier",
        "text": "A spring extends from 55 mm to 88 mm when a load is hung "
                "on it. What is its extension?",
        "options": [
            {"text": "88 mm", "correct": False,
             "why": "That is the stretched length, not the increase."},
            {"text": "55 mm", "correct": False,
             "why": "That is the natural length, before the load."},
            {"text": "143 mm", "correct": False,
             "why": "That adds the two lengths together."},
            {"text": "33 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e22",
        "band": "easier",
        "text": "A trampoline mat is fitted with springs around its edge. "
                "What property must these springs have, while a jumper is "
                "bouncing gently, for the bounce to feel consistent?",
        "options": [
            {"text": "Their extension should stay proportional to the "
                     "load", "correct": True},
            {"text": "They should stretch by the same fixed amount no "
                     "matter what weight is on the mat", "correct": False,
             "why": "A fixed stretch whatever the load would mean heavier "
                    "and lighter jumpers felt exactly the same, which is "
                    "not how a trampoline behaves."},
            {"text": "They should have no natural length whatsoever",
             "correct": False,
             "why": "Every real spring has a natural length before any "
                    "load is applied — a spring cannot start at zero "
                    "length."},
            {"text": "They should be designed to snap easily, so that no "
                     "energy ends up being wasted", "correct": False,
             "why": "A snapped spring stores and returns no energy at all "
                    "— the opposite of what a trampoline needs."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e23",
        "band": "easier",
        "text": "A spring balance shows 9 mm of stretch for a 2 N weight. "
                "Staying on the straight line, how much stretch would a "
                "6 N weight give?",
        "options": [
            {"text": "27 mm", "correct": True},
            {"text": "13 mm", "correct": False,
             "why": "That adds the extra load onto the stretch rather "
                    "than scaling the whole reading by the load ratio."},
            {"text": "3 mm", "correct": False,
             "why": "That divides instead of multiplying by the load "
                    "ratio."},
            {"text": "9 mm", "correct": False,
             "why": "That leaves it unchanged, but three times the load "
                    "gives three times the stretch."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e24",
        "band": "easier",
        "text": "A dynamometer (a spring-based force meter) has equally "
                "spaced marks on its scale. What does this rely on?",
        "options": [
            {"text": "The idea that the spring involved has no natural "
                     "length of its own whatsoever to speak of",
             "correct": False,
             "why": "Every spring has some length before any load is "
                    "applied — this is not what makes the marks equal."},
            {"text": "The spring gradually getting stiffer and stiffer as "
                     "more and more load is steadily added to it",
             "correct": False,
             "why": "If the spring got stiffer, later marks would need to "
                    "be closer together, not equally spaced."},
            {"text": "Extension staying proportional to load, so equal "
                     "loads give equal extra stretch", "correct": True},
            {"text": "The scale itself simply being printed before the "
                     "spring has even been fitted into the case",
             "correct": False,
             "why": "The marks could be printed any way at all — they are "
                    "equally spaced because of how the spring itself "
                    "behaves."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e25",
        "band": "easier",
        "text": "A door-closer spring measures 80 mm at rest and 101 mm "
                "when the door is fully open. What is its extension?",
        "options": [
            {"text": "101 mm", "correct": False,
             "why": "That is the stretched length, not the increase."},
            {"text": "80 mm", "correct": False,
             "why": "That is the natural length, at rest."},
            {"text": "181 mm", "correct": False,
             "why": "That adds the two lengths together."},
            {"text": "21 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e26",
        "band": "easier",
        "text": "Two quantities are 'proportional' to each other. What does "
                "that mean?",
        "options": [
            {"text": "They keep the same ratio — double one and the other "
                     "doubles too", "correct": True},
            {"text": "They consistently add up together to make exactly "
                     "the same fixed total amount", "correct": False,
             "why": "Keeping the same ratio is different from adding to a "
                    "fixed total — proportional quantities can both grow "
                    "without limit."},
            {"text": "One of the two quantities involved must "
                     "consistently stay exactly the same size", "correct": False,
             "why": "If one never changed, the other could not be "
                    "changing in proportion to it — both have to be free "
                    "to grow together."},
            {"text": "They are consistently exactly equal to one another "
                     "in size, no matter what", "correct": False,
             "why": "Proportional quantities keep the same RATIO, which "
                    "does not have to be one-to-one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e27",
        "band": "easier",
        "text": "What happens to the energy used to stretch a spring, when "
                "the spring is allowed to spring back?",
        "options": [
            {"text": "It disappears completely", "correct": False,
             "why": "Energy is not simply lost — the stored energy is "
                    "given back as the spring returns."},
            {"text": "Most of it is given back as the spring returns to "
                     "shape", "correct": True},
            {"text": "It turns permanently into heat before the spring can "
                     "move", "correct": False,
             "why": "A spring returning to shape converts its stored "
                    "energy back into movement, not into heat before it "
                    "even moves."},
            {"text": "It builds up further inside the spring every time it "
                     "is used", "correct": False,
             "why": "Stretching and releasing does not keep adding energy "
                    "inside the spring — the stored energy is given back "
                    "each time."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e28",
        "band": "easier",
        "text": "A tension spring in a screen door stretches 5 mm under a "
                "2 N pull. Staying on the straight line, what stretch "
                "would 10 N give?",
        "options": [
            {"text": "13 mm", "correct": False,
             "why": "That adds the extra load onto the stretch rather than "
                    "scaling the whole thing by the load ratio."},
            {"text": "1 mm", "correct": False,
             "why": "That divides instead of multiplying by the load "
                    "ratio."},
            {"text": "25 mm", "correct": True},
            {"text": "5 mm", "correct": False,
             "why": "That leaves it unchanged, but five times the load "
                    "gives five times the stretch."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e29",
        "band": "easier",
        "text": "A wound clock spring, a bow, and a trampoline all rely on "
                "the same idea when they are stretched or bent out of "
                "shape. What is that idea?",
        "options": [
            {"text": "That deforming any one of them destroys a "
                     "noticeable amount of its own strength", "correct": False,
             "why": "None of these are weakened by being used as intended "
                    "— that would defeat their purpose."},
            {"text": "That deforming any one of them consistently leaves "
                     "it permanently longer than it was before", "correct": False,
             "why": "These are all meant to be used well within their "
                    "limit of proportionality, springing back completely "
                    "rather than staying deformed."},
            {"text": "That deforming any one of them uses up the force "
                     "that was needed to do it in the first place",
             "correct": False,
             "why": "Force is not a fuel that gets used up — it is the "
                    "energy that gets stored, and returned."},
            {"text": "That the work done stretching or bending them is "
                     "stored and given back", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-e30",
        "band": "easier",
        "text": "Which of these is measured in the unit millimetres or "
                "metres?",
        "options": [
            {"text": "Extension", "correct": True},
            {"text": "Load", "correct": False,
             "why": "A load is a force, so it is measured in newtons, not "
                    "a length unit."},
            {"text": "Proportionality", "correct": False,
             "why": "Proportionality describes a relationship between two "
                    "quantities — it is not itself something with a "
                    "length."},
            {"text": "Hooke's law", "correct": False,
             "why": "Hooke's law is a relationship, not a quantity that "
                    "could be measured in millimetres."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · standard ───────────────────────────────
    {
        "id": "p4-08-s06",
        "band": "standard",
        "text": "A luggage strap's built-in spring stretches 2 cm under a "
                "4 N pull. Staying on the straight line, what is the "
                "stretch under 12 N, in millimetres?",
        "options": [
            {"text": "60 mm", "correct": True},
            {"text": "6 mm", "correct": False,
             "why": "That uses the unconverted 2 rather than 20 mm before "
                    "scaling up."},
            {"text": "20 mm", "correct": False,
             "why": "That repeats the original reading rather than "
                    "scaling it up to 12 N."},
            {"text": "80 mm", "correct": False,
             "why": "That scales by four times rather than three times "
                    "the original load."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s07",
        "band": "standard",
        "text": "A retractable tape measure's return spring stretches 2 cm "
                "under a 5 N pull. What is the extension under 10 N, in "
                "millimetres?",
        "options": [
            {"text": "4 mm", "correct": False,
             "why": "That uses the unconverted 2 rather than 20 mm before "
                    "scaling up."},
            {"text": "40 mm", "correct": True},
            {"text": "20 mm", "correct": False,
             "why": "That repeats the reading at 5 N rather than scaling "
                    "it up to 10 N."},
            {"text": "60 mm", "correct": False,
             "why": "That scales by three times rather than two times the "
                    "original load."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s08",
        "band": "standard",
        "text": "A student records some extension readings in centimetres "
                "and others in millimetres, without converting, then plots "
                "them all on one graph. What goes wrong?",
        "options": [
            {"text": "Nothing much — a properly drawn graph does not mind "
                     "what unit the individual numbers happen to be "
                     "written in", "correct": False,
             "why": "Mixed units break the straight-line pattern "
                    "completely, because a reading written in the wrong "
                    "unit is out of scale with the rest."},
            {"text": "The graph becomes a smooth curve instead of a "
                     "straight line", "correct": False,
             "why": "Not quite — an unconverted reading does not curve the "
                    "line so much as throw individual points wildly out of "
                    "place."},
            {"text": "Points recorded in the wrong unit end up wildly out "
                     "of place, breaking the straight-line pattern",
             "correct": True},
            {"text": "The limit of proportionality appears to move to a "
                     "different load", "correct": False,
             "why": "The apparent limit is not what shifts — a units "
                    "mistake scatters individual points rather than moving "
                    "where the whole line bends."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s09",
        "band": "standard",
        "text": "A luggage scale gives readings of 15 mm at 1 N, 30 mm at 2 N, 45 mm at 3 N and 95 mm at 5 N. What does the fourth reading show?",
        "options": [
            {"text": "The scale reading here must simply be misread and "
                     "certainly ought to be checked again carefully",
             "correct": False,
             "why": "It might be worth double-checking, but this exact "
                    "pattern — an extra jump beyond what proportionality "
                    "predicts — is what happens once a spring passes its "
                    "limit."},
            {"text": "The scale has completely snapped and can no longer "
                     "give any sensible reading", "correct": False,
             "why": "A snapped scale gives no sensible reading at all — "
                    "this one is still responding, just no longer "
                    "proportionally."},
            {"text": "The scale has gradually become noticeably stiffer "
                     "than it was before today", "correct": False,
             "why": "It has become EASIER to stretch, not stiffer — each "
                    "newton is now adding more than 15 mm, not less."},
            {"text": "The limit of proportionality lies somewhere between "
                     "3 N and 5 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s10",
        "band": "standard",
        "text": "A newton meter is dropped and its spring becomes slightly "
                "bent out of shape, though it still moves smoothly. What "
                "should be checked before trusting its readings again?",
        "options": [
            {"text": "Whether it now reads zero with nothing hanging on "
                     "it", "correct": True},
            {"text": "Whether the case is still the right colour",
             "correct": False,
             "why": "Cosmetic damage has nothing to do with whether the "
                    "spring inside still reads correctly."},
            {"text": "Whether it is the same length as it was when new",
             "correct": False,
             "why": "A spring's original natural length is not something "
                    "a user could check without already knowing it — "
                    "checking the zero reading is the practical test."},
            {"text": "Whether the hook on the end has rusted", "correct": False,
             "why": "Rust on the hook does not affect the spring's own "
                    "proportionality — that is a separate matter."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s11",
        "band": "standard",
        "text": "A trampoline mat's springs return almost all of the "
                "energy used to stretch them; a car's crumple zone does "
                "not. Why is that difference useful in each case?",
        "options": [
            {"text": "Because a trampoline is meant to be kept as light "
                     "as possible for jumping safely, while a car's "
                     "crumple zone has completely different design "
                     "demands", "correct": False,
             "why": "Weight is not the reason for the difference — it is "
                    "about whether returning the energy is wanted or "
                    "not."},
            {"text": "Because a trampoline needs to give the jumper energy "
                     "back, while a crash needs the energy absorbed rather "
                     "than returned", "correct": True},
            {"text": "Because springs are generally safer than crumple "
                     "zones", "correct": False,
             "why": "Neither is safer in general — each is suited to a "
                    "different job, returning energy or absorbing it."},
            {"text": "Because a crumple zone is a type of spring that has been damaged in advance, so it gives its energy back slowly instead of quickly", "correct": False,
             "why": "A crumple zone is not a damaged spring — it is "
                    "deliberately designed to deform once and stay "
                    "deformed, absorbing energy rather than returning it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s12",
        "band": "standard",
        "text": "A curtain spring extends 8 mm for every 2 N applied. What "
                "load would be needed for a 36 mm extension, staying on "
                "the straight line?",
        "options": [
            {"text": "18 N", "correct": False,
             "why": "That halves the target extension instead of dividing it by the 4 mm-per-newton figure."},
            {"text": "72 N", "correct": False,
             "why": "That multiplies the extension by the load instead of "
                    "dividing by the extension-per-newton figure."},
            {"text": "9 N", "correct": True},
            {"text": "4 N", "correct": False,
             "why": "That is the extension-per-newton figure itself, not "
                    "the load needed for a 36 mm extension."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s13",
        "band": "standard",
        "text": "Spring X stretches 5 cm under 2 N. Spring Y stretches "
                "30 mm under 2 N. Which spring is easier to stretch, and "
                "by how much extension per newton?",
        "options": [
            {"text": "Spring Y, by 10 mm per newton", "correct": False,
             "why": "Spring Y stretches LESS for the same load, so it is "
                    "the stiffer of the two, not the easier to stretch."},
            {"text": "Spring X, by 5 mm per newton", "correct": False,
             "why": "That is not the actual difference between the two "
                    "extension-per-newton figures."},
            {"text": "Spring Y, by 15 mm per newton", "correct": False,
             "why": "That is Spring Y's own extension per newton, not the "
                    "difference between the two springs, and Y is the "
                    "stiffer spring in any case."},
            {"text": "Spring X, by 10 mm per newton", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s14",
        "band": "standard",
        "text": "A bow is drawn back and held before an arrow is "
                "released. What is happening to the energy used to draw "
                "it back?",
        "options": [
            {"text": "It is being stored in the bent bow, ready to be "
                     "given back to the arrow", "correct": True},
            {"text": "It has already been lost as heat in the archer's "
                     "arms", "correct": False,
             "why": "The energy used to draw the bow is stored in the bow "
                    "itself, not lost before the arrow is even released."},
            {"text": "It stays trapped in the string alone and is not "
                     "passed on to the arrow during the shot",
             "correct": False,
             "why": "The stored energy transfers to the arrow through the "
                    "string as the bow springs back, which is the whole "
                    "point of drawing it."},
            {"text": "It builds up permanently inside the bow with each "
                     "shot", "correct": False,
             "why": "A bow used within its limits returns to the same "
                    "shape each time — the energy is given back on "
                    "release, not stored up shot after shot."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s15",
        "band": "standard",
        "text": "A spring stretches 21 mm for a 3 N load. Staying on the "
                "straight line, what load would give a 63 mm extension?",
        "options": [
            {"text": "3 N", "correct": False,
             "why": "That repeats the original load rather than scaling it "
                    "up to match the new extension."},
            {"text": "9 N", "correct": True},
            {"text": "441 N", "correct": False,
             "why": "That multiplies the extension by the load rather than "
                    "dividing by the extension-per-newton figure."},
            {"text": "18 N", "correct": False,
             "why": "That subtracts the original 3 N load from the original 21 mm extension, rather than dividing the target extension by 7 mm per newton."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s16",
        "band": "standard",
        "text": "A bungee cord's readings are 40 mm at 2 N, 80 mm at 4 N, "
                "120 mm at 6 N and 210 mm at 8 N. What does the last "
                "reading tell you?",
        "options": [
            {"text": "The cord has completely snapped in two and can no "
                     "longer stretch any further", "correct": False,
             "why": "A snapped cord would give no sensible reading — this "
                    "one is still stretching, just no longer "
                    "proportionally."},
            {"text": "The cord has gradually become noticeably stiffer "
                     "than it was before", "correct": False,
             "why": "It has become easier to stretch, since it added more "
                    "than 40 mm for the last 2 N rather than less."},
            {"text": "The limit of proportionality lies somewhere between "
                     "6 N and 8 N", "correct": True},
            {"text": "The reading must simply be some kind of error and "
                     "should be ignored completely", "correct": False,
             "why": "It might be worth re-checking, but this exact pattern "
                    "— extra stretch beyond what proportionality predicts "
                    "— is what a cord does once it passes its limit."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s17",
        "band": "standard",
        "text": "A spring-based bathroom scale has equally spaced kilogram "
                "marks all the way round its dial. What would happen to "
                "that spacing if the spring did not obey Hooke's law?",
        "options": [
            {"text": "Nothing much — the marks printed on the dial would "
                     "still come out perfectly equally spaced",
             "correct": False,
             "why": "Equal spacing relies directly on extension being "
                    "proportional to load — without that, equal loads "
                    "would not give equal extra movement."},
            {"text": "The dial would need fewer marks overall",
             "correct": False,
             "why": "The number of marks is not the issue — it is whether "
                    "the gaps between them stay equal."},
            {"text": "The scale would work well merely for very light "
                     "loads", "correct": False,
             "why": "A non-proportional spring causes uneven spacing "
                    "across the whole range, not just a failure at high "
                    "loads."},
            {"text": "The marks would have to be unevenly spaced, closer "
                     "together in some places than others", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s18",
        "band": "standard",
        "text": "A model railway coupling spring stretches 18 mm under a "
                "6 N pull. What load would stretch it by 30 mm, staying on "
                "the straight line?",
        "options": [
            {"text": "10 N", "correct": True},
            {"text": "18 N", "correct": False,
             "why": "That uses the given 18 directly as though it were "
                    "already the load, rather than working from the "
                    "extension-per-newton figure."},
            {"text": "5 N", "correct": False,
             "why": "That divides the target extension by 6 rather than "
                    "by the 3 mm-per-newton figure."},
            {"text": "90 N", "correct": False,
             "why": "That multiplies the target extension by the 3 mm-per-newton figure instead of dividing by it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s19",
        "band": "standard",
        "text": "A mousetrap's spring and a screen door's closing spring "
                "are both stretched or twisted before being released. What "
                "do they have in common with a stretched bow?",
        "options": [
            {"text": "None of them store any energy whatsoever", "correct": False,
             "why": "All three do store the energy used to deform them, "
                    "which is exactly why they can do something once "
                    "released."},
            {"text": "All three give back the energy used to deform them, "
                     "snapping back to do work", "correct": True},
            {"text": "All three are in truth designed to deform "
                     "permanently and stay that way, exactly like a "
                     "crumple zone", "correct": False,
             "why": "The opposite is true — each of these is designed to "
                    "spring all the way back, not to stay deformed."},
            {"text": "None of them obey Hooke's law", "correct": False,
             "why": "Within their working range, each of these behaves "
                    "like any other spring, with extension proportional to "
                    "the force used to set it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s20",
        "band": "standard",
        "text": "A parcel alone stretches a luggage scale's spring by "
                "40 mm. A book alone would stretch it by 24 mm. Staying on "
                "the straight line, what extension should the parcel and "
                "the book together give?",
        "options": [
            {"text": "16 mm", "correct": False,
             "why": "That subtracts the two instead of adding them — "
                    "together they should stretch it further, not less."},
            {"text": "960 mm", "correct": False,
             "why": "That multiplies the two extensions together rather "
                    "than adding them."},
            {"text": "64 mm", "correct": True},
            {"text": "48 mm", "correct": False,
             "why": "That doubles the smaller extension rather than adding "
                    "the two actual readings together."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s21",
        "band": "standard",
        "text": "Spring P stretches 5 mm for every newton applied. Spring "
                "Q stretches 20 mm for every newton applied. Which spring "
                "needs the bigger force to reach a 100 mm extension, and "
                "what force does it need?",
        "options": [
            {"text": "Spring P, needing 20 N", "correct": True},
            {"text": "Spring Q, needing 20 N", "correct": False,
             "why": "Spring Q is the easier of the two to stretch, so it "
                    "actually needs the SMALLER force, not the bigger "
                    "one."},
            {"text": "Spring P, needing 5 N", "correct": False,
             "why": "5 N would only give Spring P a 25 mm extension, well "
                    "short of 100 mm."},
            {"text": "Spring Q, needing 5 N", "correct": False,
             "why": "The force is right, but Spring Q is the easier one "
                    "to stretch, needing the smaller force — the "
                    "harder-to-stretch spring is P."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s22",
        "band": "standard",
        "text": "In the spring investigation, why is the SAME spring used "
                "for every reading, rather than swapping to a fresh one "
                "partway through?",
        "options": [
            {"text": "Because different springs can behave slightly "
                     "differently, and swapping would mix up two "
                     "different sets of results", "correct": True},
            {"text": "Because a school science laboratory can typically "
                     "keep just one single spring of this particular type "
                     "available for lessons", "correct": False,
             "why": "Schools can have as many spare springs as needed — "
                    "that is not the reason for using just one "
                    "throughout."},
            {"text": "Because a spring wears out after a single reading",
             "correct": False,
             "why": "A spring behaving properly can be loaded and "
                    "unloaded many times within its limit without wearing "
                    "out."},
            {"text": "Because the ruler is designed to work with just one "
                     "particular spring", "correct": False,
             "why": "A ruler measures length regardless of which spring "
                    "is next to it — it has no connection to a specific "
                    "spring."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s23",
        "band": "standard",
        "text": "A gate-closer spring extends by 2 mm for every newton "
                "applied. What load, in newtons, would be needed to reach "
                "an extension of 5 cm?",
        "options": [
            {"text": "10 N", "correct": False,
             "why": "That uses the unconverted 5 rather than the 50 mm "
                    "the 5 cm actually represents."},
            {"text": "25 N", "correct": True},
            {"text": "100 N", "correct": False,
             "why": "That multiplies the converted extension by 2 instead "
                    "of dividing by it."},
            {"text": "2.5 N", "correct": False,
             "why": "That divides the unconverted 5 by 2, missing the "
                    "conversion from centimetres to millimetres "
                    "altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s24",
        "band": "standard",
        "text": "Spring A has a limit of proportionality of 8 N. Spring B "
                "has a limit of proportionality of 15 N. A load of 10 N is "
                "hung from each in turn. What can you say?",
        "options": [
            {"text": "Neither spring is behaving proportionally at 10 N",
             "correct": False,
             "why": "Spring B's limit is 15 N, so at 10 N it is still "
                    "safely on its straight-line part."},
            {"text": "Both springs are still behaving proportionally at "
                     "10 N", "correct": False,
             "why": "Spring A's limit is only 8 N, so at 10 N it has "
                    "already passed its limit and stopped behaving "
                    "proportionally."},
            {"text": "Spring A has passed its limit, but Spring B has not",
             "correct": True},
            {"text": "Spring B has already passed its own limit, but "
                     "Spring A apparently has not", "correct": False,
             "why": "That is the wrong way round — Spring A's lower limit "
                    "of 8 N is the one that gets passed first, not Spring "
                    "B's higher one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s25",
        "band": "standard",
        "text": "Hooke tested his law using springs and wires of many "
                "different sizes, always staying within a certain range of "
                "loads for each one. Why was staying within a range "
                "important for his conclusion?",
        "options": [
            {"text": "Because outside that range the equipment would "
                     "simply break instantly", "correct": False,
             "why": "Breaking happens much later, if at all — the range "
                    "he found is about where the neat proportional pattern "
                    "holds, not about safety."},
            {"text": "Because a bigger range would have made his law more "
                     "impressive to publish", "correct": False,
             "why": "The reason for the range is scientific, not about "
                    "how the discovery would be received."},
            {"text": "Because completely different materials would need "
                     "entirely different laws to describe them outside "
                     "any stated range at any time", "correct": False,
             "why": "Within its own range, the same simple law describes "
                    "many different springs and wires — the range is "
                    "about where that pattern holds, not about needing a "
                    "different law altogether."},
            {"text": "Because outside that range, the simple proportional "
                     "pattern he had found no longer held true",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · harder ─────────────────────────────────
    {
        "id": "p4-08-h06",
        "band": "harder",
        "text": "Two identical springs are joined end to end and a 6 N "
                "load is hung from the bottom. Each spring alone stretches "
                "10 mm under a 6 N load. What is the total extension of "
                "the joined pair, and why?",
        "options": [
            {"text": "5 mm, because the load is now supposedly shared "
                     "equally between the two joined springs", "correct": False,
             "why": "Joined end to end, each spring carries the FULL 6 N, "
                    "not half of it — sharing the load is what happens if "
                    "springs sit side by side, not joined in a line."},
            {"text": "10 mm, because joining springs does not change "
                     "anything", "correct": False,
             "why": "Joining two springs end to end gives the load two "
                    "lots of stretching to add together, not just one."},
            {"text": "20 mm, because each spring feels the full 6 N and "
                     "adds its own 10 mm stretch", "correct": True},
            {"text": "3 mm, because each spring is assumed to feel just "
                     "half the load", "correct": False,
             "why": "Joined end to end, each spring carries the whole 6 N "
                    "on its own — nothing about the arrangement halves the "
                    "load."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h07",
        "band": "harder",
        "text": "A spring's readings are 12 mm at 1 N, 24 mm at 2 N, 36 mm "
                "at 3 N, and 15.4 cm at 6 N. If the spring were still "
                "perfectly proportional at 6 N, what extension would you "
                "expect, and by how much does the actual reading exceed "
                "it?",
        "options": [
            {"text": "72 mm expected, exceeding it by 82 mm", "correct": True},
            {"text": "72 mm expected, exceeding it by 15.4 mm",
             "correct": False,
             "why": "That compares the expected reading with the "
                    "unconverted 15.4 rather than the actual 154 mm."},
            {"text": "144 mm expected, exceeding it by 10 mm",
             "correct": False,
             "why": "That doubles the correct expected reading rather "
                    "than simply scaling 12 mm by 6."},
            {"text": "154 mm expected, exceeding it by 0 mm", "correct": False,
             "why": "That treats the actual reading as if it were also "
                    "the expected one, missing that the spring has passed "
                    "its limit entirely."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h08",
        "band": "harder",
        "text": "A spring's natural length is 60 mm. It is loaded past its "
                "limit and, once fully unloaded, measures 76 mm. It is "
                "then loaded again with a small load well within its "
                "limit, giving a further 9 mm of stretch on top. What does "
                "the spring now measure in total?",
        "options": [
            {"text": "85 mm", "correct": True},
            {"text": "76 mm", "correct": False,
             "why": "That ignores the further 9 mm this new load adds on "
                    "top of the already-deformed spring."},
            {"text": "69 mm", "correct": False,
             "why": "That adds the further stretch to the ORIGINAL 60 mm "
                    "natural length, rather than to the 76 mm the spring "
                    "now starts from."},
            {"text": "9 mm", "correct": False,
             "why": "That is only the new stretch — it needs adding to "
                    "the 76 mm the spring already measured before this "
                    "load was applied."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h09",
        "band": "harder",
        "text": "A manufacturer wants a newton meter accurate to within 1% "
                "across its whole scale. Why must the maximum reading be "
                "kept safely below the spring's limit of proportionality, "
                "rather than right up against it?",
        "options": [
            {"text": "Because springs near their limit vibrate too much to "
                     "get a steady reading", "correct": False,
             "why": "Vibration is not the reason — the issue is whether "
                    "extension is still reliably proportional to load."},
            {"text": "Because close to the limit, small manufacturing "
                     "differences between springs make the proportionality "
                     "less reliable, risking inaccurate readings",
             "correct": True},
            {"text": "Because the limit of proportionality of any given "
                     "spring is thought to change unpredictably each and "
                     "every time that exact same spring is used again in "
                     "a later reading", "correct": False,
             "why": "For a given spring the limit is a fixed property, not "
                    "something that changes reading to reading — the "
                    "concern is how consistent different springs are near "
                    "it."},
            {"text": "Because a scale cannot be printed with marks that go "
                     "all the way to the limit", "correct": False,
             "why": "Marks can be printed anywhere — the concern is "
                    "whether the reading they give is trustworthy near the "
                    "limit, not whether they can be drawn there."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h10",
        "band": "harder",
        "text": "A luggage spring extends 0.6 cm for every newton applied, "
                "while it obeys Hooke's law. A porter needs it to extend "
                "by exactly 45 mm to lift a case clear of a shelf. What "
                "load does that require, and is it more or less than a "
                "60 N case's own weight?",
        "options": [
            {"text": "0.75 N, which is much less than the case's 60 N "
                     "weight", "correct": False,
             "why": "That misplaces a decimal point in the "
                    "extension-per-newton figure — 0.6 cm is 6 mm, not "
                    "0.6 mm."},
            {"text": "7.5 N, which is more than the case's 60 N weight",
             "correct": False,
             "why": "7.5 N is far smaller than 60 N, not bigger — the "
                    "load needed here is much less than the case's own "
                    "weight."},
            {"text": "75 N, which is very clearly more than the case's "
                     "60 N weight", "correct": False,
             "why": "That uses the unconverted 0.6 rather than the 6 "
                    "mm-per-newton figure the conversion actually gives."},
            {"text": "7.5 N, which is much less than the case's 60 N "
                     "weight", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h11",
        "band": "harder",
        "text": "Spring A stretches 4 mm per newton; Spring B stretches "
                "9 mm per newton. They are joined end to end and a 5 N "
                "load is hung from the pair. What is the pair's total "
                "extension?",
        "options": [
            {"text": "65 mm", "correct": True},
            {"text": "45 mm", "correct": False,
             "why": "That uses only Spring B's own extension, leaving out "
                    "Spring A's contribution to the joined pair."},
            {"text": "32.5 mm", "correct": False,
             "why": "That averages the two springs' extension-per-newton "
                    "figures instead of adding them, which is not how two "
                    "springs in series stretch."},
            {"text": "180 mm", "correct": False,
             "why": "That multiplies the two springs' extension-per-newton "
                    "figures together instead of adding them."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h12",
        "band": "harder",
        "text": "A car is fitted with a very stiff crumple zone that "
                "barely deforms in a crash, transferring most of the "
                "impact straight to the passenger compartment instead. "
                "What has gone wrong with the design, in terms of energy?",
        "options": [
            {"text": "Nothing — a stiffer crumple zone is generally a "
                     "safer design", "correct": False,
             "why": "A crumple zone that barely deforms is not doing its "
                    "job of absorbing the crash energy — it has been made "
                    "too much like a rigid structure."},
            {"text": "The crumple zone is failing to absorb the crash "
                     "energy by deforming, so more of it reaches the "
                     "passengers instead", "correct": True},
            {"text": "The crumple zone has instead been cleverly designed "
                     "to store its energy and return it afterwards, in "
                     "exactly the way that a spring does", "correct": False,
             "why": "A crumple zone that barely deforms is not storing and "
                    "returning energy either — it is simply failing to "
                    "absorb it in the first place."},
            {"text": "The crumple zone has passed its limit of "
                     "proportionality too early", "correct": False,
             "why": "The problem described is the opposite — the zone is "
                    "too stiff and is not deforming nearly enough, not "
                    "deforming too easily."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h13",
        "band": "harder",
        "text": "Two makes of luggage scale both claim a maximum reading "
                "of 30 kg. Scale P's spring has a limit of proportionality "
                "equivalent to 32 kg; Scale Q's spring has a limit "
                "equivalent to 29 kg. What is true of Scale Q, and why "
                "does it matter?",
        "options": [
            {"text": "Nothing is wrong with Scale Q, because 29 kg is "
                     "close enough to 30 kg to make no real difference",
             "correct": False,
             "why": "A maximum reading set above the spring's own limit of "
                    "proportionality means the scale can be asked to give "
                    "readings where it is no longer reliably "
                    "proportional."},
            {"text": "Scale Q's marked maximum of 30 kg lies just past its "
                     "own limit of proportionality, so readings near the "
                     "top of its scale may not be accurate", "correct": True},
            {"text": "Scale Q is, if anything, the more accurate of the "
                     "two scales overall, simply because its limit of "
                     "proportionality happens to be the lower of the two "
                     "numbers given", "correct": False,
             "why": "A lower limit of proportionality relative to the "
                    "marked maximum is the problem here, not an "
                    "advantage."},
            {"text": "Scale Q cannot be used in any way, at any load",
             "correct": False,
             "why": "Well within its limit, at low loads for instance, "
                    "Scale Q behaves perfectly normally — the issue is "
                    "only near its marked maximum."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h14",
        "band": "harder",
        "text": "A cord's readings are 18 mm at 3 N and 42 mm at 7 N, both "
                "on the straight line. Using these two readings, what "
                "extension would you predict at 9 N?",
        "options": [
            {"text": "60 mm", "correct": False,
             "why": "That adds the two given readings together instead of "
                    "using them to find a steady rate to scale from."},
            {"text": "44 mm", "correct": False,
             "why": "That adds the extra 2 N directly onto the 42 mm "
                    "reading, rather than scaling by the 6 mm-per-newton "
                    "rate the two readings agree on."},
            {"text": "54 mm", "correct": True},
            {"text": "66 mm", "correct": False,
             "why": "That repeats the full jump from 3 N to 7 N once "
                    "more, rather than scaling by the 2 extra newtons "
                    "actually needed to reach 9 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h15",
        "band": "harder",
        "text": "Two springs look identical, but Spring M's limit of "
                "proportionality is much higher than Spring N's. Both are "
                "loaded steadily from 0 N up to a high load, well past "
                "both limits. Which spring gives a straight-line graph "
                "over a larger range of loads?",
        "options": [
            {"text": "Spring M, because its limit is reached later",
             "correct": True},
            {"text": "Spring N, because a lower limit means a longer "
                     "straight part", "correct": False,
             "why": "A lower limit means the straight part of the graph "
                    "ends SOONER, not later — Spring M's higher limit "
                    "gives the longer straight section."},
            {"text": "Both give exactly the same length of straight line",
             "correct": False,
             "why": "Different limits of proportionality mean the "
                    "straight-line part ends at different loads for the "
                    "two springs."},
            {"text": "Neither gives a straight line of any kind, because "
                     "they look identical", "correct": False,
             "why": "Looking identical says nothing about their limits of "
                    "proportionality — each still has its own "
                    "straight-line region up to its own limit."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h16",
        "band": "harder",
        "text": "A spring stretches 8 mm for every newton, while it obeys "
                "Hooke's law. Taking a kilogram as weighing about 10 N, "
                "what extension would a 2.5 kg mass produce?",
        "options": [
            {"text": "250 mm", "correct": False,
             "why": "That multiplies 2.5 by 10 correctly to get newtons, "
                    "but then uses 10 rather than 8 as the "
                    "extension-per-newton figure."},
            {"text": "20 mm", "correct": False,
             "why": "That uses 2.5 directly as though it were already in "
                    "newtons, without converting the kilograms first."},
            {"text": "80 mm", "correct": False,
             "why": "That uses 10 N as though it were the mass's whole "
                    "weight, rather than converting the full 2.5 kg."},
            {"text": "200 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h17",
        "band": "harder",
        "text": "A spring's limit of proportionality is 5 N. Loaded to "
                "11 N and back to zero, it keeps a permanent 20 mm set. "
                "Loaded only to 7 N and back to zero instead, would you "
                "expect the permanent set to be bigger, smaller, or the "
                "same, and why?",
        "options": [
            {"text": "Smaller, because a smaller load past the limit "
                     "generally leaves less permanent deformation behind",
             "correct": True},
            {"text": "Bigger, because taking any spring past its limit is "
                     "thought to do the maximum possible amount of damage "
                     "immediately, however far past it is taken",
             "correct": False,
             "why": "How far past the limit a spring is taken generally "
                    "makes a difference — going less far past it should be "
                    "expected to leave less permanent stretch, not more."},
            {"text": "The same, because the limit has already been passed "
                     "either way", "correct": False,
             "why": "Passing the limit at all is not an on/off switch to "
                    "one fixed amount of damage — how far past it the "
                    "spring is taken also matters."},
            {"text": "It cannot be estimated in any way without testing "
                     "this exact spring", "correct": False,
             "why": "While the exact number cannot be found without "
                    "testing, the DIRECTION of the change can be reasoned "
                    "about — a smaller excursion past the limit should "
                    "leave less permanent set."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h18",
        "band": "harder",
        "text": "A toy catapult's elastic may safely be pulled with no "
                "more than a 15 N force. Between an elastic that gives "
                "200 mm of stretch at 15 N and one that gives 80 mm of "
                "stretch at 15 N, which stores more energy for the same "
                "safe pull, and why?",
        "options": [
            {"text": "Both elastics store exactly the same amount of "
                     "energy overall, simply because the maximum safe "
                     "pulling force is the same for each of them",
             "correct": False,
             "why": "Even with the same maximum pull, the two elastics do "
                    "not store the same energy — the one that moves "
                    "further while being pulled stores more."},
            {"text": "The 80 mm elastic, because a stiffer elastic holds its stretch more tightly and so keeps more energy inside it", "correct": False,
             "why": "Stiffness alone does not decide it — for the same "
                    "maximum pull, the elastic that stretches FURTHER is "
                    "the one storing more energy."},
            {"text": "The 200 mm elastic, because for the same maximum "
                     "pull it stretches further, storing more energy",
             "correct": True},
            {"text": "Neither stores any energy until the pellet is "
                     "released", "correct": False,
             "why": "The energy is stored throughout the stretching, "
                    "before release — release is when it is given back, "
                    "not when it is first stored."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h19",
        "band": "harder",
        "text": "A spring's readings, taken in this order, are: 10 mm at "
                "1 N, 35 mm at 3 N, 20 mm at 2 N, 40 mm at 4 N. All are on "
                "the straight line except one, which was clearly "
                "misrecorded. Which reading does not fit the pattern, and "
                "what should it read instead?",
        "options": [
            {"text": "35 mm at 3 N is out of place; it should read 30 mm",
             "correct": True},
            {"text": "10 mm at 1 N is out of place; it should read 15 mm",
             "correct": False,
             "why": "10 mm at 1 N fits the steady 10 mm-per-newton pattern "
                    "shown by the other three readings perfectly."},
            {"text": "20 mm at 2 N is out of place; it should read 25 mm",
             "correct": False,
             "why": "20 mm at 2 N fits the steady 10 mm-per-newton pattern "
                    "shown by the other three readings perfectly."},
            {"text": "40 mm at 4 N is out of place; it should read 45 mm",
             "correct": False,
             "why": "40 mm at 4 N fits the steady 10 mm-per-newton pattern "
                    "shown by the other three readings perfectly."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h20",
        "band": "harder",
        "text": "Hooke kept his discovery secret for a while by "
                "publishing it as a scrambled anagram of Latin letters, "
                "rather than announcing the law outright. What does this "
                "show about how scientific priority worked at the time?",
        "options": [
            {"text": "That the law could not be written down in an "
                     "equation, so a code was needed instead", "correct": False,
             "why": "The law could easily be written in words or symbols, "
                    "as it later was — the coded form was about secrecy, "
                    "not about the law being hard to express."},
            {"text": "That Hooke did not trust his own result enough to "
                     "state it plainly", "correct": False,
             "why": "He was confident enough in the result to want credit "
                    "for it straight away — the anagram was about claiming "
                    "priority, not about doubting the finding."},
            {"text": "That anagram puzzles of this kind were a "
                     "completely normal, everyday part of how all "
                     "scientific results were reported and shared at "
                     "that time", "correct": False,
             "why": "The anagram trick was Hooke's own way of claiming "
                    "priority for this discovery — it was not the "
                    "standard way results were generally published."},
            {"text": "That a scientist could publicly claim credit for a "
                     "discovery by registering it, without yet revealing "
                     "what it actually said", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h21",
        "band": "harder",
        "text": "In the spring investigation, a student wants to find out "
                "whether a THICKER wire spring has a higher limit of "
                "proportionality than a thinner one made of the same "
                "metal. What must stay the same between the two springs "
                "being compared, for the comparison to be fair?",
        "options": [
            {"text": "Everything else about the two springs — for example "
                     "their coiled length and the metal they are made "
                     "from — except the thickness of the wire",
             "correct": True},
            {"text": "The load applied to each spring", "correct": False,
             "why": "The load is meant to be increased identically as it "
                    "is applied to each spring — what must stay fixed is "
                    "everything about the springs themselves apart from "
                    "wire thickness."},
            {"text": "The ruler used to measure the extension",
             "correct": False,
             "why": "Using the same ruler is sensible practice, but it is "
                    "not what makes the COMPARISON between the two springs "
                    "fair — that depends on the springs being alike apart "
                    "from the one thing being tested."},
            {"text": "The particular room the whole investigation happens "
                     "to be carried out in, together with the time of day "
                     "and the weather outside", "correct": False,
             "why": "The room has no bearing on which spring has the "
                    "higher limit of proportionality — what matters is "
                    "keeping the springs alike apart from wire thickness."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h22",
        "band": "harder",
        "text": "Spring R and Spring S are stretched by the same unknown "
                "load. Spring R extends 18 mm; Spring S extends 27 mm. If "
                "Spring R's extension-per-newton is 6 mm, what is Spring "
                "S's extension-per-newton?",
        "options": [
            {"text": "162 mm per newton", "correct": False,
             "why": "That multiplies Spring S's extension by Spring R's "
                    "rate instead of dividing by the load found from "
                    "Spring R's own reading."},
            {"text": "6 mm per newton", "correct": False,
             "why": "That simply repeats Spring R's rate; Spring S stretched further under the same load, so its rate has to be bigger."},
            {"text": "13.5 mm per newton", "correct": False,
             "why": "That halves Spring S's extension rather than "
                    "dividing it by the shared load the two springs "
                    "actually felt."},
            {"text": "9 mm per newton", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h23",
        "band": "harder",
        "text": "A luggage scale has drifted so that it now reads 15 mm "
                "even with nothing hanging on it, though it still "
                "stretches proportionally beyond that. If it reads 95 mm "
                "with a bag attached, and the scale is calibrated at 4 mm "
                "per newton, what is the bag's actual weight?",
        "options": [
            {"text": "20 N", "correct": True},
            {"text": "23.75 N", "correct": False,
             "why": "That divides the full 95 mm reading by 4, without "
                    "first subtracting the 15 mm drift."},
            {"text": "3.75 N", "correct": False,
             "why": "That divides only the 15 mm drift by 4, rather than "
                    "the bag's own 80 mm share of the reading."},
            {"text": "27.5 N", "correct": False,
             "why": "That adds the drift and the reading together before "
                    "dividing, rather than subtracting the drift from the "
                    "reading first."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h24",
        "band": "harder",
        "text": "A student says: 'If a spring extends 40 mm under 8 N, it "
                "must extend 20 mm under 4 N, because that is "
                "proportional.' Is this reasoning safe to rely on in "
                "general?",
        "options": [
            {"text": "Yes, in general, because proportional relationships "
                     "are supposed to work for any two loads whatsoever on "
                     "any given spring", "correct": False,
             "why": "The reasoning only holds provided both loads stay on "
                    "the straight-line part of the graph — a spring "
                    "already past its limit at 8 N would not behave this "
                    "way."},
            {"text": "Only if both 8 N and 4 N are within the spring's "
                     "limit of proportionality — otherwise the ratio may "
                     "not hold", "correct": True},
            {"text": "No, because halving the load never exactly halves "
                     "the extension", "correct": False,
             "why": "Within the limit of proportionality, halving the "
                    "load genuinely does halve the extension — that part "
                    "of the reasoning is sound."},
            {"text": "No, because 4 N is too small a load to measure "
                     "accurately", "correct": False,
             "why": "A small load is not itself a problem for "
                    "proportionality — the real condition is staying "
                    "within the spring's limit, whatever the size of the "
                    "load."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h25",
        "band": "harder",
        "text": "A manufacturer could calibrate a newton meter's scale by "
                "(a) working out the marks mathematically from one "
                "accurate reading and the assumption that Hooke's law "
                "holds, or (b) measuring dozens of actual readings across "
                "the whole range and marking exactly what was measured "
                "each time. Which approach copes better with a spring "
                "that starts to leave its straight-line region partway up "
                "the scale?",
        "options": [
            {"text": "Approach (a), because a calculation from one accurate reading is more reliable than dozens of separate measurements", "correct": False,
             "why": "Approach (a) assumes Hooke's law holds all the way "
                    "up, so it would print wrong, evenly-spaced marks "
                    "exactly where the spring stops behaving that way."},
            {"text": "Approach (b), because it records what the spring "
                     "actually does, including anywhere it stops being "
                     "proportional", "correct": True},
            {"text": "Neither copes with it especially well — both would "
                     "tend to give completely random and unreliable "
                     "results wherever the spring is not behaving "
                     "proportionally", "correct": False,
             "why": "Approach (b) still gives sensible marks throughout, "
                    "since it records the spring's real behaviour rather "
                    "than assuming proportionality."},
            {"text": "Both cope equally well, because both are ultimately "
                     "using the same spring", "correct": False,
             "why": "Using the same spring does not make the two "
                    "approaches equally reliable — approach (a) trusts an "
                    "assumption that approach (b) does not need to make."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · standard (top-up to 30) ────────────────
    {
        "id": "p4-08-s26",
        "band": "standard",
        "text": "A trainer's foam sole squashes when you land and pushes back as you push off. Why can this be compared to a stretched spring?",
        "options": [
            {"text": "Because the foam is actually a spring hidden inside "
                     "the shoe", "correct": False,
             "why": "There is no literal spring — it is the same "
                    "principle at work in a different material, not a "
                    "hidden mechanical spring."},
            {"text": "Because squashing a material also stores energy in "
                     "it, which can be given back, just as stretching a "
                     "spring does", "correct": True},
            {"text": "Because foam and springs are made of exactly the "
                     "same material", "correct": False,
             "why": "They are different materials entirely — what they "
                    "share is the physics of storing and returning energy "
                    "when deformed."},
            {"text": "Because compressing foam has nothing to do with "
                     "extension, so the comparison is misleading",
             "correct": False,
             "why": "The underlying idea — deforming something stores "
                    "energy that can be given back — is the same whether "
                    "the material is stretched or squashed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s27",
        "band": "standard",
        "text": "A spring extends 6 mm for every newton applied. If two "
                "7 N weights are both hung from it at the same time, what "
                "is the total extension, staying on the straight line?",
        "options": [
            {"text": "42 mm", "correct": False,
             "why": "That uses only ONE of the two 7 N weights rather than "
                    "their combined 14 N."},
            {"text": "84 mm", "correct": True},
            {"text": "12 mm", "correct": False,
             "why": "That doubles the extension-per-newton figure rather "
                    "than using the combined load."},
            {"text": "168 mm", "correct": False,
             "why": "That doubles the correct answer, using 28 N rather "
                    "than the actual combined 14 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s28",
        "band": "standard",
        "text": "A tow spring in a caravan hitch stretches 4 mm for every "
                "newton it carries, up to its limit of 60 N. What is the "
                "maximum extension it can reach while still obeying "
                "Hooke's law?",
        "options": [
            {"text": "15 mm", "correct": False,
             "why": "That divides the limit by the extension-per-newton "
                    "figure instead of multiplying."},
            {"text": "64 mm", "correct": False,
             "why": "That adds the two figures together instead of "
                    "multiplying them."},
            {"text": "240 mm", "correct": True},
            {"text": "24 mm", "correct": False,
             "why": "That misplaces a decimal point, treating the 4 "
                    "mm-per-newton figure as 0.4."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s29",
        "band": "standard",
        "text": "Two model-making elastics both lift a 20 N load. Elastic "
                "X extends 100 mm doing this; Elastic Y extends 40 mm "
                "doing this. Which one is stiffer, and what does that "
                "mean for the space it needs?",
        "options": [
            {"text": "Elastic X is stiffer and needs less space to fit",
             "correct": False,
             "why": "Elastic X stretches FURTHER for the same load, which "
                    "marks it as the less stiff of the two, not the "
                    "stiffer."},
            {"text": "Elastic Y is stiffer but needs more space to fit",
             "correct": False,
             "why": "Being stiffer here means it extends LESS for the "
                    "same load, so it actually needs less space, not "
                    "more."},
            {"text": "Neither is stiffer, because both lift the same 20 N "
                     "load", "correct": False,
             "why": "Stiffness compares how much each one stretches for "
                    "that same load, and the two extensions here are very "
                    "different."},
            {"text": "Elastic Y is stiffer and needs less space to fit, "
                     "since it extends less for the same load",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-s30",
        "band": "standard",
        "text": "A luggage scale's box states 'Maximum 25 kg — do not "
                "exceed'. Why might exceeding this figure, even briefly, "
                "cause a lasting problem with the scale?",
        "options": [
            {"text": "Because the numbers printed on the dial would rub "
                     "off", "correct": False,
             "why": "Printed numbers are not affected by the load on the "
                    "spring — the concern is what the load does to the "
                    "spring itself."},
            {"text": "Because the load may push the spring past its "
                     "limit of proportionality, leaving it permanently "
                     "stretched", "correct": True},
            {"text": "Because the hook on the end would become magnetic",
             "correct": False,
             "why": "Stretching a spring has nothing to do with "
                    "magnetism — that is an unrelated property of a "
                    "material altogether."},
            {"text": "Because the scale would need recharging like a "
                     "battery", "correct": False,
             "why": "A spring-based scale has no battery to recharge — it "
                    "works from the load's own force on the spring."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · harder (top-up to 30) ──────────────────
    {
        "id": "p4-08-h26",
        "band": "harder",
        "text": "Two identical springs are hung side by side, in "
                "parallel, supporting a single 20 N weight between them "
                "and sharing the load equally. Each spring alone would "
                "stretch 8 mm under the full 20 N. What is the actual "
                "extension of each spring in this arrangement?",
        "options": [
            {"text": "8 mm, because each spring still behaves as if it "
                     "alone held the full load", "correct": False,
             "why": "Sharing the load between two springs means each one "
                    "only carries half of it, not the whole 20 N."},
            {"text": "16 mm, because the two springs add their individual "
                     "stretches together", "correct": False,
             "why": "Springs side by side sharing a load do not add their "
                    "stretches — that happens when springs are joined end "
                    "to end, not side by side."},
            {"text": "4 mm, because each spring only carries half the "
                     "20 N load", "correct": True},
            {"text": "2 mm, because the load is divided by four rather "
                     "than two", "correct": False,
             "why": "Sharing between exactly two springs divides the load "
                    "by two, not four."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h27",
        "band": "harder",
        "text": "A designer must choose between a steel spring and a "
                "rubber cord for a bungee-style ride, both able to stretch "
                "safely to the same maximum extension under the same "
                "maximum force. What is one genuine advantage a measured, "
                "well-tested spring has over a rubber cord for this job?",
        "options": [
            {"text": "It never needs replacing, however many times it is "
                     "used", "correct": False,
             "why": "Every real spring eventually wears out or fatigues "
                    "with enough repeated use — that is not the genuine "
                    "advantage here."},
            {"text": "It weighs nothing whatsoever, unlike rubber",
             "correct": False,
             "why": "A steel spring is not weightless — if anything it "
                    "typically weighs more than an equivalent rubber "
                    "cord."},
            {"text": "It stores no energy, so it cannot fail",
             "correct": False,
             "why": "A spring storing no energy would be useless for a "
                    "bungee-style ride — storing and returning energy is "
                    "exactly its job."},
            {"text": "Its extension stays more reliably proportional to "
                     "the force across repeated use, so its behaviour is "
                     "easier to predict", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h28",
        "band": "harder",
        "text": "A found spring, with no manufacturer's label, gives "
                "22 mm at 2 N and 55 mm at 5 N, both apparently on the "
                "straight line. Using both readings, is the spring's "
                "behaviour actually consistent with being on the straight "
                "line, and why?",
        "options": [
            {"text": "No — the two readings give different amounts per "
                     "newton, so one of them must be wrong", "correct": False,
             "why": "Both readings actually give exactly the same 11 mm "
                    "per newton, so they are consistent with each other."},
            {"text": "Yes — both readings give exactly 11 mm per newton, "
                     "confirming the same straight-line rate", "correct": True},
            {"text": "Yes — but only because both extensions happen to be "
                     "odd numbers", "correct": False,
             "why": "Being odd numbers is a coincidence of the units "
                    "chosen and has nothing to do with whether the "
                    "readings are proportional."},
            {"text": "No — a spring's readings cannot be trusted without "
                     "a manufacturer's label", "correct": False,
             "why": "A spring's behaviour can be tested directly from its "
                    "own readings, whether or not it has a label."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h29",
        "band": "harder",
        "text": "A shop sells a 'super-stretch' novelty spring advertised "
                "as having 'no limit of proportionality — it stays "
                "perfectly straight-line however far you pull it.' Is "
                "this a believable claim?",
        "options": [
            {"text": "Yes — some springs really do behave perfectly for "
                     "any extension", "correct": False,
             "why": "Every real material eventually stops behaving "
                    "proportionally once stretched enough — that is a "
                    "property of real materials, not just marketing."},
            {"text": "Yes — a limit of proportionality only applies to "
                     "metal springs, not novelty ones", "correct": False,
             "why": "A limit of proportionality is a property of how a "
                    "material deforms, not something limited to one type "
                    "of spring."},
            {"text": "No — every real spring eventually leaves its "
                     "straight-line behaviour if stretched far enough",
             "correct": True},
            {"text": "It cannot be judged either way without buying one "
                     "first", "correct": False,
             "why": "The claim can be judged from what is already known "
                    "about how real materials behave under load, without "
                    "needing to test that particular product."},
        ],
        "figure": None,
    },
    {
        "id": "p4-08-h30",
        "band": "harder",
        "text": "Spring C stretches 3 mm per newton; Spring D stretches "
                "0.7 cm per newton. They are joined end to end, and the "
                "pair is stretched until the total extension reaches "
                "exactly 100 mm. What load produced this, and which "
                "spring contributed the larger share of the stretch?",
        "options": [
            {"text": "10 N, and Spring C contributed the larger share",
             "correct": False,
             "why": "Spring C only contributes 30 mm of the 100 mm total "
                    "— Spring D, at 7 mm per newton, contributes the "
                    "larger 70 mm share."},
            {"text": "10 N, and Spring D contributed the larger share",
             "correct": True},
            {"text": "1000 N, and Spring D contributed the larger share",
             "correct": False,
             "why": "That divides the combined rate into the total the "
                    "wrong way round, giving a load a hundred times too "
                    "large."},
            {"text": "10 N, and both springs contributed exactly equal "
                     "shares", "correct": False,
             "why": "The two springs have different extension-per-newton "
                    "rates, 3 mm and 7 mm, so they do not contribute "
                    "equally."},
        ],
        "figure": None,
    },
]
