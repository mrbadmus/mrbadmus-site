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
            # ⊕ MRB-297 · 1 Sep 2026 — the third option was widened so the
            # correct answer stops being resolvable as the second-longest.
            {"text": "It is nearly zero, because parallel lines cancel each "
                     "other out", "correct": False,
             "why": "Cancelling shows up as lines curving away and a bare "
                    "patch. Parallel arrows of a good length mean a steady, "
                    "real field, not two fields undoing each other."},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p10-02-e05",
        "band": "easier",
        "text": "Where field lines are crowded closely together, the field "
                "is…",
        "options": [
            {"text": "strong", "correct": True},
            {"text": "weak", "correct": False,
             "why": "Spread-out lines mean a weak field; crowding means the "
                    "opposite."},
            {"text": "pointing the other way", "correct": False,
             "why": "Direction is shown by the arrowheads, not by how close "
                    "the lines are."},
            {"text": "the same as everywhere else", "correct": False,
             "why": "Crowding is exactly how a map shows that the field "
                    "varies from place to place."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e06",
        "band": "easier",
        "text": "Can two field lines cross on a map?",
        "options": [
            {"text": "Yes, where the field is strongest", "correct": False,
             "why": "A strong field crowds the lines but never makes them "
                    "meet."},
            {"text": "Yes, between two magnets", "correct": False,
             "why": "The two fields add there to give one direction, so the "
                    "lines still do not cross."},
            {"text": "No — a compass cannot point two ways at once",
             "correct": True},
            {"text": "No, because there are too few lines drawn",
             "correct": False,
             "why": "Drawing more lines would not let them cross; the field "
                    "has one direction at each point."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e07",
        "band": "easier",
        "text": "Field lines outside a bar magnet run…",
        "options": [            {"text": "from the north pole to the south pole", "correct": True},
            {"text": "from the south pole to the north pole", "correct": False,
             "why": "That is the direction INSIDE the magnet; outside they "
                    "run the other way."},
            {"text": "out of both poles", "correct": False,
             "why": "They leave the north and enter the south, so only one "
                    "end has them coming out."},
            {"text": "into both poles", "correct": False,
             "why": "They enter at the south only; the north is where they "
                    "leave."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e08",
        "band": "easier",
        "text": "Is there a magnetic field in the space BETWEEN two drawn "
                "field lines?",
        "options": [            {"text": "No — the field is only along the lines themselves",
             "correct": False,
             "why": "Put a compass there and it turns, which shows the field "
                    "is present."},
            {"text": "Only if a magnetic material is placed there",
             "correct": False,
             "why": "The field is there whether or not anything is in it to "
                    "feel it."},
            {"text": "No, unless more lines are drawn in", "correct": False,
             "why": "Drawing a line does not create a field; the line records "
                    "one that is already there."},
            {"text": "Yes, just as much as on the lines", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e09",
        "band": "easier",
        "text": "What lines itself up along the field at a point?",
        "options": [            {"text": "A plotting compass needle", "correct": True},
            {"text": "A copper wire", "correct": False,
             "why": "Copper is not magnetic, so a field does nothing to it."},
            {"text": "A thermometer", "correct": False,
             "why": "A thermometer measures temperature and is unaffected by "
                    "a magnetic field."},
            {"text": "A plastic ruler", "correct": False,
             "why": "Plastic is not magnetic and is ignored completely."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e10",
        "band": "easier",
        "text": "Iron filings sprinkled on paper over a magnet show…",
        "options": [
            {"text": "the shape of a field that was already there",
             "correct": True},
            {"text": "the field that the filings themselves create",
             "correct": False,
             "why": "The filings only line up in it; sweep them off and the "
                    "field is unchanged."},
            {"text": "where the magnet has been damaged", "correct": False,
             "why": "The pattern appears round any magnet, damaged or not."},
            {"text": "which way round the field runs", "correct": False,
             "why": "Filings show the shape but not the direction; a compass "
                    "is needed for that."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e11",
        "band": "easier",
        "text": "A magnetic field is…",
        "options": [            {"text": "a substance that pours out of the poles",
             "correct": False,
             "why": "Nothing flows out; the field is a state the space is "
                    "in."},
            {"text": "the iron filings that gather round a magnet",
             "correct": False,
             "why": "The filings reveal the field; the field is there without "
                    "them."},
            {"text": "the lines drawn on a diagram", "correct": False,
             "why": "The lines are a record of the field, not the field "
                    "itself."},
            {"text": "the region where a magnet would feel a force",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p10-02-s05",
        "band": "standard",
        "text": "A plotting compass is moved slowly along a curved field "
                "line. What does the needle do?",
        "options": [            {"text": "Turns steadily, staying lined up with the line",
             "correct": True},
            {"text": "Stays pointing the same way throughout",
             "correct": False,
             "why": "The line curves, and the needle follows the field's "
                    "direction at each point."},
            {"text": "Spins freely, because the field has no direction along "
                     "a line",
             "correct": False,
             "why": "It has a definite direction at every point, which is why "
                    "the needle settles."},
            {"text": "Points at the nearest pole all the way round",
             "correct": False,
             "why": "It follows the field, which curves away from the "
                    "straight line to the pole."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s06",
        "band": "standard",
        "text": "Where is a bar magnet's field strongest?",
        "options": [            {"text": "Halfway along its side", "correct": False,
             "why": "That is where the lines are furthest apart, so the field "
                    "is weakest."},
            {"text": "At the very centre, inside the magnet", "correct": False,
             "why": "The question is about the field outside, and the poles "
                    "are where it is most concentrated."},
            {"text": "Everywhere equally, since it is one magnet",
             "correct": False,
             "why": "The map shows it varying a great deal from place to "
                    "place."},
            {"text": "Close to the two poles", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s07",
        "band": "standard",
        "text": "Why can two field lines never cross?",
        "options": [            {"text": "Because a compass there would have to point two ways at "
                     "once",
             "correct": True},
            {"text": "Because the lines would break the magnet if they met",
             "correct": False,
             "why": "Lines are a drawing and cannot damage anything."},
            {"text": "Because there is not enough room on the paper",
             "correct": False,
             "why": "A bigger sheet would not let them cross; the physics "
                    "forbids it."},
            {"text": "Because crossing lines would mean the field was zero "
                     "there",
             "correct": False,
             "why": "A zero field is drawn as a gap in the lines, not as a "
                    "crossing."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s08",
        "band": "standard",
        "text": "Two bar magnets are laid end to end with their NORTH poles "
                "facing. What happens to the field between them?",
        "options": [            {"text": "The two fields add, so it is very strong between them",
             "correct": False,
             "why": "They point towards each other there, so they oppose "
                    "rather than add."},
            {"text": "The lines cross between the two magnets",
             "correct": False,
             "why": "Lines never cross; where two fields cancel the map shows "
                    "a gap instead."},
            {"text": "The field disappears everywhere around both magnets",
             "correct": False,
             "why": "Each magnet's field is unchanged elsewhere; only between "
                    "them do they cancel."},
            {"text": "The two fields oppose, and somewhere between them they "
                     "cancel",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s09",
        "band": "standard",
        "text": "A field map is drawn with every arrowhead left off. What has "
                "been lost?",
        "options": [
            {"text": "The shape of the field", "correct": False,
             "why": "The shape is in the lines themselves, and it survives "
                    "perfectly well."},
            {"text": "Where the field is strong and where it is weak",
             "correct": False,
             "why": "That is shown by how crowded the lines are, which the "
                    "arrowheads do not affect."},
            {"text": "Which way round the field runs, so the poles cannot be "
                     "told apart",
             "correct": True},
            {"text": "Nothing at all — arrowheads are decoration",
             "correct": False,
             "why": "They carry the direction, which is half of what a field "
                    "map records."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s10",
        "band": "standard",
        "text": "Why must a plotting compass be small?",
        "options": [            {"text": "So that it records the field at one place rather than "
                     "an average",
             "correct": True},
            {"text": "So that it is light enough to turn freely",
             "correct": False,
             "why": "A well-made large compass turns freely too; the reason "
                    "is about where it samples."},
            {"text": "So that it does not add its own field to the magnet's",
             "correct": False,
             "why": "It has a field of its own whatever its size, and that is "
                    "not what limits it."},
            {"text": "So that it fits between the iron filings",
             "correct": False,
             "why": "Filings and compasses are used separately, not at the "
                    "same time."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s11",
        "band": "standard",
        "text": "The same magnet is replaced with a much stronger one of the "
                "same shape. How does the map change?",
        "options": [
            {"text": "The shape changes completely", "correct": False,
             "why": "The pattern round a bar magnet is set by its shape, and "
                    "that has not changed."},
            {"text": "The lines run the other way round", "correct": False,
             "why": "The poles are still at the same ends, so the direction "
                    "is unchanged."},
            {"text": "The same shape, but the lines are more crowded",
             "correct": True},
            {"text": "Nothing changes, because a map cannot show strength",
             "correct": False,
             "why": "Crowding is exactly how a map shows strength."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p10-02-h05",
        "band": "harder",
        "text": "A bar magnet is sealed inside a cardboard box. How could you "
                "find its poles without opening the box?",
        "options": [
            {"text": "Weigh the box at each end and compare", "correct": False,
             "why": "Mass tells you nothing about which end is which pole."},
            {"text": "Shake the box and listen for which end it slides "
                     "towards",
             "correct": False,
             "why": "Sliding depends on how it is packed, not on its "
                    "magnetism."},
            {"text": "Move a plotting compass round the outside and record "
                     "the directions",
             "correct": True},
            {"text": "Sprinkle iron filings on the box and read the "
                     "direction off",
             "correct": False,
             "why": "Filings show the shape but never which way round it "
                    "runs, so the poles stay unidentified."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h06",
        "band": "harder",
        "text": "Two bar magnets are laid side by side with both north poles "
                "at the same end. What is the field like at that end?",
        "options": [
            {"text": "Stronger than either magnet on its own", "correct": True},
            {"text": "Zero, because the two magnets cancel", "correct": False,
             "why": "Cancelling needs the fields to point opposite ways, and "
                    "here they point the same way."},
            {"text": "The same as one magnet, because they are identical",
             "correct": False,
             "why": "Both contribute at every point, so the two add up."},
            {"text": "Reversed, so that end behaves as a south pole",
             "correct": False,
             "why": "Nothing reverses a pole by putting another north beside "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h07",
        "band": "harder",
        "text": "A student says the magnet must make extra lines at its ends, "
                "because they are crowded there. What is right?",
        "options": [            {"text": "The magnet does make more lines at the poles",
             "correct": False,
             "why": "There is no fixed stock of lines; a mapmaker chooses how "
                    "many to draw."},
            {"text": "The crowding is a mistake and the lines should be "
                     "evenly spaced",
             "correct": False,
             "why": "Even spacing would hide the fact that the field is "
                    "stronger near the poles."},
            {"text": "The lines are real, and they gather at the poles",
             "correct": False,
             "why": "The field is real; the lines are our way of recording "
                    "it."},
            {"text": "The lines are a drawing, and crowding is how a map "
                     "shows a strong field",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h08",
        "band": "harder",
        "text": "A student's map shows a line leaving the north pole and "
                "stopping in mid-air. What is wrong?",
        "options": [            {"text": "The line should carry on round and enter the south "
                     "pole",
             "correct": True},
            {"text": "Lines should always be straight", "correct": False,
             "why": "They curve almost everywhere round a bar magnet, and "
                    "that is correct."},
            {"text": "The line should have gone into the north pole instead",
             "correct": False,
             "why": "Outside a magnet the lines leave the north; entering it "
                    "would reverse the whole map."},
            {"text": "Nothing is wrong — lines stop where the field runs out",
             "correct": False,
             "why": "The field fades but never stops abruptly, so a line "
                    "ending in space is a drawing error."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h09",
        "band": "harder",
        "text": "From a field map alone, how would you find where the field "
                "is strongest?",
        "options": [
            {"text": "Look for where the lines are most crowded",
             "correct": True},
            {"text": "Look for where the lines are longest", "correct": False,
             "why": "A field line has no length of its own; it is drawn as "
                    "far as the mapmaker chooses."},
            {"text": "Look for where the lines cross", "correct": False,
             "why": "They never cross, so there is nothing to look for."},
            {"text": "Look for where the arrowheads are largest",
             "correct": False,
             "why": "Arrowheads mark direction; their size is not part of the "
                    "convention."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h10",
        "band": "harder",
        "text": "Why do the field lines round a bar magnet spread out widely "
                "at its sides?",
        "options": [            {"text": "Because the magnet is thinner there", "correct": False,
             "why": "The shape of the metal is not what sets the spacing; the "
                    "strength of the field is."},
            {"text": "Because the field points sideways there", "correct": False,
             "why": "Which way it points is shown by the arrows, not by how "
                    "far apart the lines are."},
            {"text": "Because the lines are running out of room",
             "correct": False,
             "why": "There is more room at the sides, not less, and spacing "
                    "records strength."},
            {"text": "Because the field is weaker at the sides",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h11",
        "band": "harder",
        "text": "Why is a plotting compass better than iron filings for "
                "recording a field?",
        "options": [            {"text": "Because a compass shows which way round the field runs, "
                     "and filings do not",
             "correct": True},
            {"text": "Because filings are too heavy to be moved by a weak "
                     "field",
             "correct": False,
             "why": "They line up readily; what they cannot show is the "
                    "direction."},
            {"text": "Because filings give the wrong shape", "correct": False,
             "why": "They give the shape very well, which is why they are "
                    "used at all."},
            {"text": "Because a compass works without the magnet being "
                     "present",
             "correct": False,
             "why": "It needs a field to line up with, just as the filings "
                    "do."},
        ],
        "figure": None,
    },
]
