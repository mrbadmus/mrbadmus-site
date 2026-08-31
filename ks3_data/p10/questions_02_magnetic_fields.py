"""P10 lesson 02 — Magnetic fields: twelve questions (MRB-223).

Written against Design's page. The four layouts, the twenty-five plotting
positions, the four rule cards and the four rungs are hers.

The discriminations, in the order the lesson builds them:

  · a field is a REGION, and it is there whether or not anything is in it;
  · a field line records the direction a compass settles to — the compass is
    the measurement and the line is the drawing (`MAG-06`);
  · the field fills the gaps between drawn lines as much as the lines
    (`MAG-05`), and how many lines get drawn is a choice (`MAG-08`);
  · lines never cross, because a compass cannot point two ways (`MAG-07`) —
    the harder band sits on the consequences of that.

⚠️ NO VALUE IN TESLA APPEARS IN ANY QUESTION, and no force in newtons. Ruled
for the whole unit: every comparison here is relative or in words, and every
angle is a real bearing in degrees.

⚠️ POSITION IS AUTHORED — 1,2,3,0 · 2,3,0,1 · 3,0,1,2, three of each.

⚠️ NO RUNG IS RESTATED. The ladder owns the crowded-versus-spread reading, the
crossing lines, the plotting method and the bare patch between two north
poles; nothing here reuses any of the four.
"""

UNIT = "P10"
LESSON = "magnetic-fields"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p10-02-e01",
        "band": "easier",
        "text": "What does a single field line on a map actually show?",
        "options": [
            {"text": "Where a thin strip of iron has been laid down on the "
                     "paper",
             "correct": False,
             "why": "There is nothing on the paper. The line is a record of "
                    "readings, drawn afterwards in pencil."},
            {"text": "The direction a compass needle would point at each spot "
                     "along it", "correct": True},
            {"text": "The outer edge of the region that the magnet is able "
                     "to reach",
             "correct": False,
             "why": "Lines are drawn all through the region, not around it. "
                    "The field does not stop at a line."},
            {"text": "How far away from the magnet an object can still be "
                     "pulled",
             "correct": False,
             "why": "A line carries a direction, not a distance. How far the "
                    "magnet reaches is shown by how the lines spread."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e02",
        "band": "easier",
        "text": "Outside a bar magnet, which way round are field lines drawn?",
        "options": [
            {"text": "Into the north pole and out of the south pole",
             "correct": False,
             "why": "That is the right idea the wrong way round. Check it "
                    "with a compass: the needle's north end points away from "
                    "the magnet's north pole."},
            {"text": "Out of both poles, in every direction",
             "correct": False,
             "why": "Only one pole has lines leaving it. Every line that "
                    "leaves the north pole arrives at the south."},
            {"text": "Out of the north pole and into the south pole",
             "correct": True},
            {"text": "Round and round the middle of the magnet, never "
                     "reaching the ends", "correct": False,
             "why": "The lines bunch at the ends, which is where the field is "
                    "strongest. The middle is the weakest part."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e03",
        "band": "easier",
        "text": "A bar magnet sits alone on a table with nothing near it. Is "
                "there a magnetic field around it?",
        "options": [
            {"text": "No — a field only appears when something is put in it",
             "correct": False,
             "why": "The field is what acts on the object you bring up. It "
                    "has to be there first."},
            {"text": "No — a field needs iron filings or a compass to exist",
             "correct": False,
             "why": "Filings and compasses are detectors. Taking a detector "
                    "away does not remove what it was detecting."},
            {"text": "Only if the magnet is a strong one", "correct": False,
             "why": "Every magnet has a field. A weaker magnet has a weaker "
                    "one, not none."},
            {"text": "Yes — the field is there whether or not anything is in "
                     "it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e04",
        "band": "easier",
        "text": "What is a plotting compass used for?",
        "options": [
            {"text": "Measuring the direction of a field at one point at a "
                     "time", "correct": True},
            {"text": "Making the field lines appear on the paper",
             "correct": False,
             "why": "Nothing makes lines appear. You mark where the needle "
                    "settled and join your own marks up."},
            {"text": "Measuring how strong a magnet is",
             "correct": False,
             "why": "A plotting compass gives a direction, not a size, and no "
                    "number at all."},
            {"text": "Finding which end of a bar is the north pole of the "
                     "Earth", "correct": False,
             "why": "It finds a direction where you put it. Which end of a "
                    "bar is which is read off the letters on the bar."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p10-02-s01",
        "band": "standard",
        "text": "One student draws a field map of a bar magnet with eight "
                "lines. Another draws the same magnet with forty. Whose "
                "magnet has the stronger field?",
        "options": [
            {"text": "The one with forty lines, because there is more field "
                     "on the page", "correct": False,
             "why": "Both drew the same magnet. Nothing about it changed when "
                    "the second student picked up a pencil."},
            {"text": "The one with eight lines, because each line carries "
                     "more of the field", "correct": False,
             "why": "A line does not carry a share of anything. It records a "
                    "direction, and how many you draw is up to you."},
            {"text": "Neither — how many lines to draw is a choice made by "
                     "whoever is drawing", "correct": True},
            {"text": "It cannot be decided without knowing the size of the "
                     "paper", "correct": False,
             "why": "The paper is irrelevant. Neither map tells you anything "
                    "about the magnet that the other does not."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s02",
        "band": "standard",
        "text": "Iron filings have been scattered over a magnet and are then "
                "swept off the paper. What happens to the field?",
        "options": [
            {"text": "It goes with them, because the filings were the field",
             "correct": False,
             "why": "The filings only showed you where the field already was. "
                    "They are the detector, not the cause."},
            {"text": "It gets weaker, because some of it was used up lining "
                     "them up", "correct": False,
             "why": "Nothing was used up. A magnet lines up a filing and "
                    "keeps everything it had."},
            {"text": "It stays but changes shape, because the filings were "
                     "holding the lines in place", "correct": False,
             "why": "Nothing was holding anything. The shape is set by the "
                    "magnet and by nothing else on the paper."},
            {"text": "Nothing — the field is exactly as it was before",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s03",
        "band": "standard",
        "text": "Between the jaws of a horseshoe magnet the arrows on a field "
                "map are nearly parallel and nearly the same length. What "
                "does that tell you about the field there?",
        "options": [
            {"text": "It is nearly the same strength and direction all "
                     "through that gap", "correct": True},
            {"text": "It is nearly zero, because parallel lines cancel out",
             "correct": False,
             "why": "Cancelling shows up as lines curving away and a bare "
                    "patch. Parallel arrows of a good length mean a steady, "
                    "real field."},
            {"text": "It is about to become uneven, because the lines are on "
                     "the point of crossing", "correct": False,
             "why": "Parallel lines never meet, and lines never cross "
                    "anywhere in any case."},
            {"text": "It is weaker there than anywhere else on the map",
             "correct": False,
             "why": "The gap between the jaws is the strongest part of a "
                    "horseshoe's map, which is the reason for the shape."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s04",
        "band": "standard",
        "text": "A plotting compass is put down on a blank part of the paper, "
                "half way between two drawn field lines. What does it do?",
        "options": [
            {"text": "It spins slowly, because there is no line for it to "
                     "follow", "correct": False,
             "why": "It settles as firmly there as anywhere. The blank space "
                    "on the paper is blank; the field is not."},
            {"text": "It settles to a definite direction, the same as it "
                     "would anywhere else", "correct": True},
            {"text": "It settles, but only if it is nudged onto one of the "
                     "drawn lines first", "correct": False,
             "why": "It has never needed a drawn line. The lines were drawn "
                    "from readings like this one."},
            {"text": "It points at the nearest drawn line, because that is "
                     "where the field is", "correct": False,
             "why": "The field is everywhere between the lines at full "
                    "strength. There is nothing special about a pencil mark."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p10-02-h01",
        "band": "harder",
        "text": "Two bar magnets are laid end to end a few centimetres apart, "
                "with a north pole facing a south pole. Where on the map is "
                "the field strongest?",
        "options": [
            {"text": "At the two far ends, away from the gap",
             "correct": False,
             "why": "The far ends are ordinary poles with only their own "
                    "magnet contributing. The gap has both."},
            {"text": "Out at the sides, where the lines have most room",
             "correct": False,
             "why": "Room is what a weak field has. The strongest place is "
                    "the most crowded one."},
            {"text": "Nowhere in particular — two magnets share the field out "
                     "evenly", "correct": False,
             "why": "Nothing is shared out. Each magnet's field adds to the "
                    "other's, and where they add best is the gap."},
            {"text": "In the gap between them, where the lines run straight "
                     "across", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h02",
        "band": "harder",
        "text": "A field map is drawn on a flat sheet of paper. Why is that "
                "drawing only part of the story?",
        "options": [
            {"text": "The field fills space in three dimensions, and the "
                     "paper shows one flat slice of it", "correct": True},
            {"text": "The paper blocks part of the field, so some of it never "
                     "reaches the pencil", "correct": False,
             "why": "A magnetic field goes straight through paper. That is "
                    "why the filings work with the magnet underneath."},
            {"text": "A drawing can only show the strong parts, so the weak "
                     "ones are missing", "correct": False,
             "why": "Weak regions are drawn too — as lines spread far apart. "
                    "Nothing is left out for being weak."},
            {"text": "The lines are only guesses until they are checked with "
                     "a stronger magnet", "correct": False,
             "why": "Each line is a record of real compass readings. It is a "
                    "measurement, not a guess."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h03",
        "band": "harder",
        "text": "Two students plot the same bar magnet and draw lines in the "
                "same places, but their arrowheads point opposite ways. How "
                "would you settle which map is right?",
        "options": [
            {"text": "Count the lines on each map — the one with more has "
                     "followed the field more carefully", "correct": False,
             "why": "How many lines you draw is a choice. It says nothing "
                    "about which way they run."},
            {"text": "Put a compass on a line and see which way its "
                     "north-seeking end points", "correct": True},
            {"text": "Look at which map has the lines more crowded near the "
                     "poles", "correct": False,
             "why": "Both maps have the lines in the same places, so both are "
                    "crowded identically. Only the arrowheads differ."},
            {"text": "Neither is right, because the arrow direction on a "
                     "field line is only a convention", "correct": False,
             "why": "Which end of the needle is called north is the "
                    "convention. Given that, the arrow direction is a "
                    "measurement, and one of the two maps has it wrong."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h04",
        "band": "harder",
        "text": "On a field map the same lines are drawn near the magnet and "
                "far from it, yet the field really is weaker further away. "
                "How does the drawing manage to show that?",
        "options": [
            {"text": "The lines are drawn thinner as they get further away",
             "correct": False,
             "why": "Thickness carries nothing on a field map. What carries "
                    "the strength is spacing."},
            {"text": "Some of the lines are left out further away, so fewer "
                     "reach that far", "correct": False,
             "why": "Every line runs the whole way from one pole to the "
                    "other. None of them stops part way."},
            {"text": "The same lines are spread over more space, so they are "
                     "further apart there", "correct": True},
            {"text": "The arrowheads are drawn smaller further away, showing "
                     "a smaller field", "correct": False,
             "why": "An arrowhead only shows direction. It is the gap between "
                    "neighbouring lines that shows the strength."},
        ],
        "figure": None,
    },
]
