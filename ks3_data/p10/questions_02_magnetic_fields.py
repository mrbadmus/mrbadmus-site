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
            {"text": "Where the field is strong and where it is weak across "
                     "the map",
             "correct": False,
             "why": "That is shown by how crowded the lines are, which the "
                    "arrowheads do not affect."},
            {"text": "Which way round the field runs — the poles are lost",
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
        "options": [
            {"text": "So that it records the field at one place only",
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
        "options": [
            {"text": "Because a compass shows which way round the field runs",
             "correct": True},
            {"text": "Because filings are far too heavy to be moved by a weak "
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
    {
        "id": "p10-02-e12",
        "band": "easier",
        "text": "A place where two magnets' fields cancel out exactly is called a…",
        "options": [
            {"text": "neutral point", "correct": True},
            {"text": "dead zone, where no field has ever reached", "correct": False,
             "why": "Both fields do reach that spot; they simply arrive equal and "
                    "opposite, which is a different thing from never having "
                    "reached it at all."},
            {"text": "blank spot, left empty deliberately by whoever drew the map", "correct": False,
             "why": "It is not a gap in the drawing. It is a genuine physical "
                    "place where the total field really is zero."},
            {"text": "weak point, because both fields are small there", "correct": False,
             "why": "The fields there are not necessarily small on their own — "
                    "they can be strong and still cancel each other out "
                    "completely."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e13",
        "band": "easier",
        "text": "At a neutral point, what does a compass placed there do?",
        "options": [
            {"text": "It spins round and round continuously", "correct": False,
             "why": "Nothing keeps turning it. With no field acting on it, it "
                    "simply stays wherever it is left."},
            {"text": "It stays wherever it is left, because nothing is turning it", "correct": True},
            {"text": "It points straight down into the page", "correct": False,
             "why": "Pointing straight down is not something a compass needle on a "
                    "flat map does at all, whatever the field."},
            {"text": "It settles firmly on a bearing, exactly as it would "
                     "anywhere else", "correct": False,
             "why": "A neutral point is exactly the one place a compass cannot "
                    "settle to a direction, because there is no field left to turn "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e14",
        "band": "easier",
        "text": "Inside a bar magnet itself, which way do the field lines run?",
        "options": [
            {"text": "They stop completely at each pole and do not continue "
                     "inside the metal", "correct": False,
             "why": "A field line never simply stops. It continues inside the "
                    "magnet, closing the loop it started outside."},
            {"text": "Sideways, at right angles to the direction outside", "correct": False,
             "why": "The direction inside is still along the bar, from south to "
                    "north, not sideways."},
            {"text": "From the south pole back round to the north pole", "correct": True},
            {"text": "From the north pole through to the south pole, the same "
             "direction as outside", "correct": False,
             "why": "Outside the magnet they run north to south. Inside, they "
                    "carry on the other way, from south back to north, so that "
                    "every line forms a closed loop."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e15",
        "band": "easier",
        "text": "A field line outside a magnet is drawn leaving the north pole. "
                "Does that same line eventually stop, or does it carry on "
                "somewhere?",
        "options": [
            {"text": "It simply stops in the space around the magnet, at the "
                     "point where the field is finally too weak to draw", "correct": False,
             "why": "A field line never just ends in open space. Every one closes "
                    "up into a loop, running back into the magnet at the south "
                    "pole."},
            {"text": "It carries on forever, getting weaker without ever "
                     "reaching anywhere, since nothing out in open space can "
                     "stop a line", "correct": False,
             "why": "It reaches a definite place — the south pole — and carries on "
                    "through the magnet, rather than fading away for ever."},
            {"text": "It splits into two separate lines part way along, so that "
                     "each of the magnet's two poles is given one", "correct": False,
             "why": "A single field line does not split into two. It runs as one "
                    "continuous loop from pole to pole and back."},
            {"text": "It carries on, all the way round into the magnet's south pole, "
             "forming one closed loop", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e16",
        "band": "easier",
        "text": "Does a magnetic field pass through a sheet of glass placed between "
                "a magnet and a compass?",
        "options": [
            {"text": "Yes — glass is not a magnetic material, so it does not "
                     "block the field", "correct": True},
            {"text": "No — glass is transparent, so light passes through it but the "
             "field cannot", "correct": False,
             "why": "Being transparent to light has nothing to do with magnetism. "
                    "The field passes straight through glass exactly as it does "
                    "through paper."},
            {"text": "No — air is the one thing a magnetic field can pass "
                     "through, and nothing solid", "correct": False,
             "why": "The field passes through plenty of solids, as long as they "
                    "are not magnetic materials. Glass is one of them."},
            {"text": "Only a little of it gets through, weakened by the glass", "correct": False,
             "why": "An ordinary non-magnetic material like glass does not weaken "
                    "the field at all as it passes through."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e17",
        "band": "easier",
        "text": "On a field map, what does the SPACING between neighbouring lines "
                "represent?",
        "options": [
            {"text": "How far the field reaches out into space", "correct": False,
             "why": "Reach is not what spacing shows. Crowded or spread out, the "
                    "lines cover the whole mapped region either way."},
            {"text": "How strong the field is at that point", "correct": True},
            {"text": "How old the magnet is, since fields fade with age", "correct": False,
             "why": "A field map has nothing to do with the age of the magnet. "
                    "Spacing is purely about strength."},
            {"text": "How many separate magnets are contributing to the field at "
             "that point", "correct": False,
             "why": "Spacing says nothing about how many magnets are involved. It "
                    "is about how strong the total field is there."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e18",
        "band": "easier",
        "text": "A student draws longer arrows for the parts of a field map where "
                "the field is stronger. Is arrow LENGTH the correct way to show "
                "strength on this kind of map?",
        "options": [
            {"text": "No — strength cannot be shown on this kind of drawing", "correct": False,
             "why": "Strength absolutely can be shown, and is — through how "
                    "crowded the lines are, not through their length."},
            {"text": "Yes, longer arrows are the standard way to show a "
                     "stronger field, and the spacing between the lines is only "
                     "decoration", "correct": False,
             "why": "On this kind of field map, strength is shown by how closely "
                    "the lines are spaced, not by how long each arrow is drawn."},
            {"text": "No — strength is shown by how closely the lines are spaced, "
             "not by arrow length", "correct": True},
            {"text": "Yes, but only if the arrowheads are also made bigger at "
                     "the same time, so that the head size matches the new "
                     "length", "correct": False,
             "why": "Bigger arrowheads are not part of the convention either. "
                    "Spacing between lines is what carries the strength."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e19",
        "band": "easier",
        "text": "Which of these is the correct name for the point where two "
                "opposing fields add up to exactly zero?",
        "options": [
            {"text": "The cancel line, named after the two fields cancelling "
                     "there", "correct": False,
             "why": "That is not the term used either. The place where the fields "
                    "cancel is called a neutral point."},
            {"text": "The dead spot, named for the bare patch that iron filings "
                     "leave there", "correct": False,
             "why": "That is an informal description, not the term this lesson "
                    "uses. The correct name is a neutral point."},
            {"text": "The zero line, since the total field reads zero along it", "correct": False,
             "why": "That is not the term used. The correct name is a neutral "
                    "point."},
            {"text": "The neutral point", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e20",
        "band": "easier",
        "text": "A magnetic field line and an electric field line both run between "
                "two poles or charges on a diagram. Do BOTH kinds close up into a "
                "loop inside the source?",
        "options": [
            {"text": "No — a magnetic field line closes into a loop, but an electric "
             "field line starts and ends on charges instead", "correct": True},
            {"text": "No — neither kind of line ever closes into a loop", "correct": False,
             "why": "A magnetic field line genuinely does close into a loop, "
                    "running back through the magnet from south to north."},
            {"text": "Yes, but only for very strong magnets and charges", "correct": False,
             "why": "This is not about strength at all. It is a difference in KIND "
                    "between a magnetic field and an electric one."},
            {"text": "Yes, both magnetic and electric field lines always close into "
             "loops, since both are drawn with curved arrows joining two "
             "points", "correct": False,
             "why": "Only a magnetic field line closes into a loop. An electric "
                    "field line simply starts on a positive charge and ends on a "
                    "negative one."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e21",
        "band": "easier",
        "text": "A magnet is completely embedded inside a block of plastic. Does "
                "its magnetic field still reach a compass held outside the block?",
        "options": [
            {"text": "Only if the block is left open at one end, so that the "
                     "field has somewhere to get out", "correct": False,
             "why": "An open end is not needed. The field passes straight through "
                    "the solid plastic itself."},
            {"text": "Yes — plastic is not a magnetic material, so the field passes "
             "straight through it", "correct": True},
            {"text": "No — the plastic seals the field inside the block "
                     "completely, because a solid casing leaves it nowhere to "
                     "escape", "correct": False,
             "why": "Nothing about being a non-magnetic material lets it seal a "
                    "field in. The field passes through plastic just as it does "
                    "through paper or glass."},
            {"text": "Only if the plastic block is thin enough to see through", "correct": False,
             "why": "Thickness and transparency make no difference here. The field "
                    "passes through, thick or thin, clear or opaque."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e22",
        "band": "easier",
        "text": "Two identical bar magnets sit many metres apart, far too far for "
                "either to affect the other. What does the field map around EACH "
                "one look like?",
        "options": [
            {"text": "Doubled in strength everywhere, because two magnets are "
                     "now present and a field map counts every magnet in the "
                     "room", "correct": False,
             "why": "Each magnet's own field is unaffected by a second magnet too "
                    "far away to reach it. Nothing doubles."},
            {"text": "Missing entirely, because two identical magnets cancel "
                     "each other out whatever distance is left between them, "
                     "near or far", "correct": False,
             "why": "Two magnets cancel only where their fields actually overlap "
                    "and oppose. Far enough apart, there is no overlap at all."},
            {"text": "Exactly like a single bar magnet's ordinary field, with no "
             "sign of the other magnet at all", "correct": True},
            {"text": "Squashed flat on the side facing the other magnet", "correct": False,
             "why": "That squashing only happens when two magnets are close enough "
                    "to actually interact. Far enough apart, each field looks "
                    "completely undisturbed."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e23",
        "band": "easier",
        "text": "A student's field map shows the lines evenly spaced everywhere, "
                "with no extra crowding near either pole. What is wrong with this "
                "map?",
        "options": [
            {"text": "The lines should all be drawn the same length instead of "
                     "spaced evenly, since it is length that shows the strength", "correct": False,
             "why": "Length is not the issue being tested here — spacing is, and "
                    "even spacing fails to show where the field is stronger."},
            {"text": "There should be no lines drawn near the poles, since the "
                     "field is too strong to draw there", "correct": False,
             "why": "The poles are exactly where the most lines should appear, "
                    "crowded together, not where lines are left out."},
            {"text": "Nothing — even spacing is the correct way to draw any "
                     "field map, since a field fills its whole region evenly", "correct": False,
             "why": "Even spacing hides exactly the information a field map is "
                    "meant to show: that the field is stronger near the poles."},
            {"text": "The lines should crowd together near the poles, where the "
             "field is strongest", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e24",
        "band": "easier",
        "text": "Which of these is measured with a plotting compass at ONE point at "
                "a time?",
        "options": [
            {"text": "The direction of the field there", "correct": True},
            {"text": "The total number of field lines in the whole map", "correct": False,
             "why": "A compass at one point cannot count anything across the whole "
                    "map. It only ever gives a direction, right there."},
            {"text": "The exact strength of the field in tesla", "correct": False,
             "why": "A plotting compass gives no number at all, in tesla or any "
                    "other unit — only a direction."},
            {"text": "The distance to the nearest magnetic pole", "correct": False,
             "why": "A compass does not measure distance. It only shows which way "
                    "the field points at the spot where it sits."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e25",
        "band": "easier",
        "text": "A field map has been drawn with arrows but no crowding anywhere, "
                "so it is impossible to tell where the field is strongest. What "
                "single change would fix this?",
        "options": [
            {"text": "Adding colour to the strongest-looking lines", "correct": False,
             "why": "Colour is not part of the convention at all. Spacing is what "
                    "carries the information about strength."},
            {"text": "Spacing the lines closer together near the poles and "
                     "further apart elsewhere", "correct": True},
            {"text": "Making the arrowheads bigger near the poles", "correct": False,
             "why": "Arrowhead size is not the convention used for strength. "
                    "Spacing between the lines is."},
            {"text": "Drawing extra lines at the very centre of the magnet, "
                     "where the field builds up", "correct": False,
             "why": "The centre of the magnet is not where the field outside is "
                    "strongest — the poles are, and that is where the lines should "
                    "crowd."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e26",
        "band": "easier",
        "text": "A compass is placed exactly at a neutral point and given a gentle "
                "nudge. What happens next?",
        "options": [
            {"text": "It swings back to the same bearing as before the nudge", "correct": False,
             "why": "There is no field there to swing it back to any particular "
                    "bearing. It simply stays wherever the nudge leaves it."},
            {"text": "It settles slowly onto magnetic north, taking longer than "
             "usual", "correct": False,
             "why": "There is no field pulling it towards any direction at all at "
                    "a true neutral point, however long it is left."},
            {"text": "It stays at whatever new angle the nudge left it at", "correct": True},
            {"text": "It spins continuously until it is removed from the spot", "correct": False,
             "why": "Nothing is left to keep turning it. With zero field acting on "
                    "it, it simply comes to rest and stays put."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e27",
        "band": "easier",
        "text": "A steel paperclip is placed exactly at a neutral point between two "
                "magnets. Is it pulled towards either magnet?",
        "options": [
            {"text": "Yes, it is pulled towards both magnets at once, "
                     "stretching it, since two equal pulls add together rather "
                     "than cancel", "correct": False,
             "why": "The two pulls cancel rather than adding destructively. There "
                    "is no stretching effect at all."},
            {"text": "No, because steel stops responding to a field once two magnets "
             "are involved", "correct": False,
             "why": "Steel responds to a magnetic field however many sources are "
                    "involved. Here the total field itself happens to be zero."},
            {"text": "Yes, towards whichever magnet is slightly stronger, since "
                     "a neutral point balances distance but not strength", "correct": False,
             "why": "At a true neutral point the two contributions are exactly "
                    "equal and opposite, so there is no overall pull either way."},
            {"text": "No — the two fields cancel there, so there is no overall pull "
             "on it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e28",
        "band": "easier",
        "text": "On a hand-drawn field map with no letters marked, the arrows on "
                "one line all point INTO a certain end of a bar magnet. What pole "
                "must that end be?",
        "options": [
            {"text": "The south pole, since lines run into the south pole", "correct": True},
            {"text": "Either pole — arrow direction does not identify which end is "
             "which", "correct": False,
             "why": "Arrow direction is exactly what identifies the poles: lines "
                    "always leave north and arrive at south."},
            {"text": "Neither — arrows pointing inward mean that end is not a "
                     "pole of any kind", "correct": False,
             "why": "An end that lines arrive at is a genuine pole — specifically "
                    "the south pole, not a sign that it has no pole."},
            {"text": "The north pole, since lines point into the north pole", "correct": False,
             "why": "Lines run OUT of the north pole, not into it. An end that "
                    "lines point into must be the south pole instead."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e29",
        "band": "easier",
        "text": "A person's hand is placed between a magnet and a compass. Does the "
                "compass still respond to the magnet through the hand?",
        "options": [
            {"text": "Only weakly, because a hand is mostly water", "correct": False,
             "why": "Water is not a magnetic material either, so it does not "
                    "weaken the field passing through it."},
            {"text": "Yes — living tissue is not a magnetic material, so the field "
             "passes straight through it", "correct": True},
            {"text": "No — a hand is warm, and warmth blocks a magnetic field", "correct": False,
             "why": "Temperature has nothing to do with whether a field passes "
                    "through something. What matters is whether the material is "
                    "magnetic, and living tissue is not."},
            {"text": "No — only dry, non-living material lets a field through, "
                     "as the water in tissue soaks it up", "correct": False,
             "why": "Being alive or dry makes no difference at all. The field "
                    "passes through a hand exactly as it does through paper or "
                    "plastic."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-e30",
        "band": "easier",
        "text": "Which single instrument tells you the DIRECTION of a magnetic "
                "field at a point, rather than just its shape?",
        "options": [
            {"text": "A magnifying glass, which shows the field lines close up", "correct": False,
             "why": "A magnifying glass has nothing to do with detecting a "
                    "magnetic field at all."},
            {"text": "Iron filings", "correct": False,
             "why": "Filings show the overall shape of a field very well, but not "
                    "which way along a line it points."},
            {"text": "A plotting compass", "correct": True},
            {"text": "A steel paperclip, which swings round to lie along the "
                     "field like a needle", "correct": False,
             "why": "A paperclip shows only that a field is present by being "
                    "pulled towards it, not which direction the field runs."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s12",
        "band": "standard",
        "text": "A bar magnet's field line is traced starting from outside the "
                "north pole. If you kept following that exact same line all the way "
                "round, where would it eventually lead?",
        "options": [
            {"text": "Back into the magnet at the south pole, and then through the "
             "magnet to the north pole again", "correct": True},
            {"text": "Out into space, getting weaker and weaker, without ever "
                     "reaching anywhere else, until it fades below anything a "
                     "compass could pick up", "correct": False,
             "why": "A field line does not simply fade away in open space. It "
                    "closes into a loop, running back into the magnet at the south "
                    "pole."},
            {"text": "Back to the same north pole it started from, without ever "
                     "reaching the south pole, since each pole keeps its own "
                     "lines to itself", "correct": False,
             "why": "A single field line always runs from one pole to the other. "
                    "It cannot loop back to the same pole it left without passing "
                    "the other one."},
            {"text": "Into the nearest OTHER magnet in the room, however far "
                     "away it is, because lines join up the strongest poles "
                     "nearby", "correct": False,
             "why": "A field line belongs to its own magnet and closes through "
                    "that same magnet. It is not drawn towards a distant, "
                    "unconnected magnet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s13",
        "band": "standard",
        "text": "An electric field line starts on a positive charge and ends on a "
                "negative one. A magnetic field line has no matching start and end "
                "point. Why not?",
        "options": [
            {"text": "Because a magnetic field does not exist in the space "
                     "between two separate poles", "correct": False,
             "why": "A magnetic field absolutely exists between the two poles of a "
                    "magnet — that is most of what a field map shows."},
            {"text": "Because a magnetic field line always closes into a loop, "
             "running back through the magnet from south to north", "correct": True},
            {"text": "Because a magnetic field has no direction anywhere along its "
             "length", "correct": False,
             "why": "A magnetic field line has a clear direction at every point — "
                    "the issue is that it forms a closed loop, not that it lacks a "
                    "direction."},
            {"text": "Because a north pole and a south pole are the same thing "
                     "as each other, unlike positive and negative charge", "correct": False,
             "why": "A north pole and a south pole behave in genuinely opposite "
                    "ways. The real reason is that the line forms a closed loop "
                    "rather than starting and stopping."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s14",
        "band": "standard",
        "text": "A magnet is fully sealed inside a thick glass paperweight. Explain "
                "why a compass held next to the paperweight still responds to the "
                "magnet inside.",
        "options": [
            {"text": "The compass is responding to the glass itself becoming "
                     "weakly magnetised after months sealed around a magnet", "correct": False,
             "why": "Glass cannot be magnetised — it is not one of the four "
                    "magnetic materials. The compass responds to the magnet's own "
                    "field passing straight through."},
            {"text": "The paperweight must have a thin gap or seam that the field "
             "escapes through", "correct": False,
             "why": "No gap is needed. The field passes through the solid glass "
                    "itself, since glass is not a magnetic material."},
            {"text": "Glass is not a magnetic material, so the field passes straight "
             "through it to reach the compass", "correct": True},
            {"text": "The glass slowly leaks tiny amounts of the field out through "
             "microscopic cracks", "correct": False,
             "why": "No leaking or cracking is needed. An ordinary non-magnetic "
                    "material simply does not block a magnetic field at all, whole "
                    "or cracked."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s15",
        "band": "standard",
        "text": "Two bar magnets are brought slowly from far apart to close "
                "together, unlike poles facing. How does the field in the gap "
                "between them change as they approach?",
        "options": [
            {"text": "It weakens steadily, because the gap left for the field "
                     "to occupy keeps shrinking as the two magnets close in", "correct": False,
             "why": "A smaller gap does not mean a weaker field there — quite the "
                    "opposite, since the two fields are adding together over less "
                    "distance."},
            {"text": "It stays weak until they touch, then suddenly becomes very "
             "strong", "correct": False,
             "why": "The strengthening happens gradually as the magnets approach, "
                    "not suddenly only at the moment of contact."},
            {"text": "It stays exactly the same throughout, since neither "
                     "magnet's own strength has changed on the way in", "correct": False,
             "why": "Each magnet's own field is unchanged, but the COMBINED field "
                    "in the gap grows steadily stronger as the two magnets get "
                    "nearer to each other."},
            {"text": "It grows steadily stronger, as the two magnets' fields add "
             "together over a shrinking gap", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s16",
        "band": "standard",
        "text": "A horseshoe magnet's field between its two jaws is drawn as almost "
                "parallel, evenly-spaced lines. Why do scientists value a region of "
                "field shaped like this?",
        "options": [
            {"text": "Because the field is nearly the same strength and direction "
             "everywhere in that region, which makes results there easier to "
             "predict", "correct": True},
            {"text": "Because parallel lines mean the field there is zero, "
                     "which is safer to work in, in the same way a neutral "
                     "point is drawn with lines curving away from a bare patch", "correct": False,
             "why": "Parallel, evenly-spaced lines mean a strong, steady field, "
                    "not a zero one — a genuinely zero field would show as a bare, "
                    "uncrossed gap instead."},
            {"text": "Because a horseshoe shape is the only shape that can be "
                     "magnetised at all, since bending a bar round is what "
                     "locks the magnetism into it", "correct": False,
             "why": "Bar magnets and every other shape can be magnetised too. The "
                    "horseshoe shape is chosen for the useful field pattern it "
                    "gives between its jaws."},
            {"text": "Because it is the only shape of field that can be "
                     "detected with a plotting compass, since a curved field "
                     "turns the needle too far", "correct": False,
             "why": "A compass detects any field shape perfectly well. What makes "
                    "this one useful is that it is nearly the SAME everywhere in "
                    "that region."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s17",
        "band": "standard",
        "text": "A hand-drawn field map shows arrows leaving one end of a bar "
                "magnet and none of the letters N or S are marked anywhere. How "
                "could you work out which end is the north pole?",
        "options": [
            {"text": "It cannot be worked out without a real compass on the actual "
             "magnet", "correct": False,
             "why": "The map itself carries enough information: the direction of "
                    "the arrows alone tells you which end is north."},
            {"text": "Whichever end the arrows LEAVE from must be the north "
                     "pole", "correct": True},
            {"text": "Whichever end has the most crowded lines must be the north "
             "pole", "correct": False,
             "why": "Both poles usually have crowded lines, so crowding alone "
                    "cannot tell the two ends apart. The direction of the arrows "
                    "can."},
            {"text": "Whichever end is drawn on the left of the page is always the "
             "north pole", "correct": False,
             "why": "A magnet's poles do not depend on which way round the page "
                    "happens to be drawn. Only the arrow direction identifies "
                    "north."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s18",
        "band": "standard",
        "text": "A student says a strong magnet has 'more field lines' than a weak "
                "one, and that is what a field map shows. Explain what a field map "
                "ACTUALLY shows about the difference between the two.",
        "options": [
            {"text": "A stronger magnet's lines are drawn thicker, not more numerous", "correct": False,
             "why": "Line thickness is not part of the convention at all. Spacing "
                    "between the lines is what carries the information."},
            {"text": "There is no real difference — any two magnets give "
             "identical-looking maps", "correct": False,
             "why": "The maps genuinely differ: a stronger magnet's lines sit more "
                    "closely together in the region around it."},
            {"text": "A stronger magnet's map has more closely spaced lines in the "
             "same region, not necessarily a different total count", "correct": True},
            {"text": "A stronger magnet has exactly double the number of lines "
                     "drawn on its map", "correct": False,
             "why": "There is no fixed ratio like doubling. How many lines get "
                    "drawn is a choice; what changes with strength is how closely "
                    "they are spaced."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s19",
        "band": "standard",
        "text": "A compass is carried in a straight line from far away right up to "
                "a bar magnet's side. How does the reading change along the way?",
        "options": [
            {"text": "It stays exactly the same strength throughout, only the "
             "bearing changes", "correct": False,
             "why": "Strength grows the closer the compass gets, as well as the "
                    "bearing possibly changing — it is not just direction that "
                    "varies."},
            {"text": "It gets weaker the closer the compass gets, since compasses "
             "work best far from any magnet", "correct": False,
             "why": "A compass reads a magnet's field MORE strongly closer in, not "
                    "more weakly — that is exactly how a field behaves near its "
                    "source."},
            {"text": "It reads the same everywhere until it is almost touching the "
             "magnet, then changes suddenly", "correct": False,
             "why": "The reading changes gradually the whole way, growing stronger "
                    "bit by bit as the compass gets closer, not suddenly at the "
                    "very end."},
            {"text": "It gets steadily stronger, and possibly changes bearing, the "
             "closer the compass gets", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s20",
        "band": "standard",
        "text": "A neutral point is found between two bar magnets placed with like "
                "poles facing. One of the two magnets is then replaced with a much "
                "stronger one, same distance apart. What happens to the exact "
                "position of the neutral point?",
        "options": [
            {"text": "It moves closer to the WEAKER of the two magnets", "correct": True},
            {"text": "It moves closer to the STRONGER of the two magnets", "correct": False,
             "why": "The balance point moves AWAY from the stronger magnet, not "
                    "towards it, since the stronger source needs less distance to "
                    "match the weaker one."},
            {"text": "It disappears completely, because a neutral point needs two "
             "EQUAL magnets to exist at all", "correct": False,
             "why": "A neutral point can exist between two unequal magnets too — "
                    "it simply sits closer to the weaker one rather than exactly "
                    "half way between them."},
            {"text": "It stays in exactly the same place, since a neutral point "
             "never moves once found", "correct": False,
             "why": "A neutral point is simply wherever the two contributions "
                    "happen to balance. Change one magnet's strength and that "
                    "balance point shifts."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s21",
        "band": "standard",
        "text": "A plotting compass gives readings all the way round a bar magnet, "
                "but never once points directly AT either pole from any distance. "
                "What does this show about how the field behaves near a pole?",
        "options": [
            {"text": "This only happens with weak magnets, and a stronger one would "
             "behave differently", "correct": False,
             "why": "Field lines curve into a pole for any bar magnet, weak or "
                    "strong. This is about the shape of the field, not its "
                    "strength."},
            {"text": "The field lines curve as they approach a pole, rather than "
             "pointing straight at it from every direction", "correct": True},
            {"text": "The compass must be faulty, since it should always point "
             "straight at the nearest pole", "correct": False,
             "why": "A working compass never simply points straight at a pole from "
                    "a distance — it follows the curved field line running through "
                    "wherever it is placed."},
            {"text": "The pole itself is not where the field is strongest", "correct": False,
             "why": "The pole really is where the field is strongest. What this "
                    "shows is about the SHAPE of the lines approaching it, not "
                    "about where the strength lies."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s22",
        "band": "standard",
        "text": "Two field maps of the same bar magnet are drawn by two different "
                "students: one with 10 lines, one with 50 lines. Do the two maps "
                "disagree about the SHAPE of the field?",
        "options": [
            {"text": "It cannot be answered without measuring the magnet's strength "
             "first", "correct": False,
             "why": "The magnet's strength is not needed to answer this — the two "
                    "maps of the SAME magnet describe the same shape regardless."},
            {"text": "Yes — more lines means a different and more detailed "
                     "shape, with extra curves that the sparser map misses out", "correct": False,
             "why": "Extra lines add detail to the picture but do not change the "
                    "underlying shape being represented — both maps describe the "
                    "same field."},
            {"text": "No — both maps show the same underlying shape, just sampled "
             "with a different number of lines", "correct": True},
            {"text": "Yes — the map with fewer lines is simply wrong", "correct": False,
             "why": "A map with fewer lines is not wrong. Choosing how many lines "
                    "to draw is a decision about how densely to sample, not a "
                    "source of error."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s23",
        "band": "standard",
        "text": "A student claims that field lines are real physical threads that "
                "could, in principle, be picked up with tweezers. What is the best "
                "response to this claim?",
        "options": [
            {"text": "The claim is correct, but only for very strong magnets", "correct": False,
             "why": "Strength makes no difference here. Field lines are a drawing "
                    "convention, whatever the strength of the magnet being mapped."},
            {"text": "The claim is correct, and iron filings are small pieces "
                     "of the lines themselves, broken off wherever the field is "
                     "strongest", "correct": False,
             "why": "Iron filings are ordinary iron that lines UP with the field; "
                    "they are not fragments of the lines, which are not physical "
                    "objects at all."},
            {"text": "The claim cannot be tested either way, since nobody has ever "
             "tried using tweezers on a field, so the question is left "
             "completely open until someone actually attempts it", "correct": False,
             "why": "It can be answered directly from what a field line actually "
                    "is: a record of compass readings, not a physical thread."},
            {"text": "Lines are a drawing that represents readings taken with a "
             "compass; nothing physical exists along them to be picked up", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s24",
        "band": "standard",
        "text": "A single bar magnet's field map is compared with a map of two "
                "identical bar magnets placed end to end, unlike poles facing, "
                "right where they touch. Is the field exactly at the touching point "
                "the same as at either magnet's own pole alone?",
        "options": [
            {"text": "No — at the touching point the two fields add together, so it "
             "is stronger there than either pole alone would be", "correct": True},
            {"text": "Yes — touching two magnets together changes nothing about the "
             "field where they meet, since each magnet is assumed to carry "
             "on exactly as it would completely on its own", "correct": False,
             "why": "Where the two poles meet, both fields are present and add "
                    "together, making that point stronger than a single pole on "
                    "its own."},
            {"text": "No — it is weaker there, because the two fields partly "
                     "cancel, one pole pushing back against the other", "correct": False,
             "why": "Unlike poles facing each other ADD their fields in the gap "
                    "between them; they do not cancel. Cancelling happens with "
                    "like poles facing instead."},
            {"text": "It depends entirely on which pole is on the left of the "
                     "drawing, since a map is read from its left-hand pole "
                     "first", "correct": False,
             "why": "Which side each pole is drawn on makes no physical "
                    "difference. What matters is that the poles are unlike and "
                    "their fields add where they meet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s25",
        "band": "standard",
        "text": "A field map correctly shows lines crowding near a magnet's poles. "
                "A second student redraws the SAME magnet but makes the crowding "
                "near the poles even tighter than reality, to make the drawing look "
                "more dramatic. What is wrong with doing this?",
        "options": [
            {"text": "Nothing — a field map is a rough impression, so exact "
                     "spacing does not matter", "correct": False,
             "why": "Spacing is not just decoration — it is meant to represent, "
                    "honestly, how the field's strength actually compares from "
                    "place to place on the real magnet."},
            {"text": "It exaggerates how much stronger the field near the poles "
             "really is, compared with the rest of the map", "correct": True},
            {"text": "It makes the lines point the wrong way, reversing the poles", "correct": False,
             "why": "Changing how tightly the lines are spaced does not affect "
                    "which way the arrows point. The poles are not reversed by "
                    "this."},
            {"text": "It turns the magnetic field into an electric one by mistake", "correct": False,
             "why": "Redrawing spacing more tightly has no bearing on whether the "
                    "field being shown is magnetic or electric."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s26",
        "band": "standard",
        "text": "A compass needle is placed at a point exactly half way along the "
                "straight line joining two identical bar magnets, like poles facing "
                "each other. Predict what happens to the needle as it is moved a "
                "tiny distance off that exact centre line.",
        "options": [
            {"text": "It reverses to point at the OTHER magnet instead of either "
             "original direction", "correct": False,
             "why": "There is no reversal effect here. The needle simply begins to "
                    "follow whichever magnet's field now slightly outweighs the "
                    "other's."},
            {"text": "It suddenly points at full strength in a completely random "
             "direction", "correct": False,
             "why": "The change is gradual, not sudden or random. Moving slightly "
                    "off the balance point lets one magnet's contribution edge "
                    "ahead smoothly."},
            {"text": "It begins to settle to a definite bearing, as the fields no "
             "longer balance exactly", "correct": True},
            {"text": "It stays exactly as unsettled as before, since any point near "
             "the centre line is also neutral", "correct": False,
             "why": "Only the exact centre line balances the two fields. Moving "
                    "off it tips the balance, and the needle starts to settle."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s27",
        "band": "standard",
        "text": "A field map is drawn using dashed lines instead of solid ones, but "
                "everything else about the spacing and direction is identical to a "
                "normal map. Does this change what the map represents "
                "scientifically?",
        "options": [
            {"text": "Yes — dashed lines represent a field that switches on and "
                     "off repeatedly, with a gap drawn in for each off moment", "correct": False,
             "why": "Dashed lines are simply a drawing style. They do not "
                    "represent a field that comes and goes — the field described "
                    "is exactly the same as a solid-line map."},
            {"text": "Yes — dashed lines mean the field is weaker along that "
             "particular line", "correct": False,
             "why": "Strength is shown by spacing between lines, not by whether an "
                    "individual line is drawn solid or dashed."},
            {"text": "Yes — a dashed line means the map is a rough guess rather "
                     "than a measured result, drawn before any compass was used", "correct": False,
             "why": "Line style says nothing about how carefully the readings were "
                    "taken. It is a stylistic choice, not a scientific one."},
            {"text": "No — the style of the line is not part of the scientific "
             "convention; spacing and direction are what matter", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s28",
        "band": "standard",
        "text": "A compass placed near a bar magnet's SIDE, half way between the "
                "two poles, gives a bearing at right angles to the magnet's own "
                "length. Is the field there weaker, stronger, or the same as right "
                "at the poles?",
        "options": [
            {"text": "Weaker — the side, half way along, is further from both poles "
             "than the region right at either pole", "correct": True},
            {"text": "Stronger — the side of a magnet is always the strongest part "
             "of its field, since that is the widest, most solid-looking "
             "part of the metal itself", "correct": False,
             "why": "The poles are the strongest parts of a bar magnet's field, "
                    "not the side half way along, which sits further from both of "
                    "them."},
            {"text": "Exactly the same — field strength does not vary around a "
                     "single magnet, since one magnet has one strength", "correct": False,
             "why": "Field strength does vary considerably around one magnet: it "
                    "is strongest at the poles and weaker away from them, "
                    "including at the side."},
            {"text": "It cannot be compared, since the two spots have different "
                     "bearings, and strength can only be compared along one "
                     "line", "correct": False,
             "why": "Direction and strength are two separate things read from a "
                    "compass and a field map — having different bearings does not "
                    "stop a strength comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s29",
        "band": "standard",
        "text": "A neutral point sits between two magnets. A thin sheet of steel is "
                "slid into the gap, touching neither magnet, exactly at the neutral "
                "point. What happens to the sheet?",
        "options": [
            {"text": "It becomes permanently magnetised because it sits exactly "
             "between two magnets", "correct": False,
             "why": "With zero field acting on it at that exact point, there is "
                    "nothing there to magnetise the steel at all."},
            {"text": "Nothing pulls it either way, since the field is zero at that "
             "exact spot", "correct": True},
            {"text": "It is pulled strongly towards whichever magnet is nearer", "correct": False,
             "why": "At the true neutral point neither magnet's pull wins out — "
                    "the two are balanced, so there is no overall pull on the "
                    "steel there."},
            {"text": "It is pulled equally towards BOTH magnets at once, and is "
                     "stretched thin between them", "correct": False,
             "why": "The two pulls cancel rather than adding destructively. There "
                    "is no stretching or tearing effect on the sheet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-s30",
        "band": "standard",
        "text": "A magnet's field map is measured and drawn at room temperature. "
                "The same magnet is then gently warmed, without reaching anywhere "
                "near the temperature that would destroy its magnetism. Would you "
                "expect the map to change noticeably?",
        "options": [
            {"text": "Yes — warming a magnet always doubles the crowding of its "
             "field lines", "correct": False,
             "why": "There is no such doubling effect from a small temperature "
                    "rise. The field stays essentially unchanged until heating is "
                    "severe."},
            {"text": "Yes — the field disappears completely the moment the "
                     "magnet is warmed", "correct": False,
             "why": "The field only disappears once the magnet is heated well "
                    "beyond the point that scrambles its magnetic regions, not "
                    "from gentle warming."},
            {"text": "No, not noticeably — a small temperature rise well below the "
             "danger point leaves the magnet's field essentially the same", "correct": True},
            {"text": "Yes — any rise in temperature at all instantly reverses the "
             "magnet's poles", "correct": False,
             "why": "Reversing the poles is not something ordinary warming does. "
                    "Only heating far enough to destroy the alignment altogether "
                    "changes the magnetism seriously."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h12",
        "band": "harder",
        "text": "A field map shows two magnets placed with like poles facing, and a "
                "neutral point exactly half way between them. One magnet is then "
                "made stronger while the distance between them stays fixed. Explain "
                "which way the neutral point shifts, and why.",
        "options": [
            {"text": "Towards the WEAKER magnet, because the stronger magnet's field "
             "now reaches further before it drops to match the weaker one's", "correct": True},
            {"text": "Towards the STRONGER magnet, because a stronger magnet always "
             "pulls the balance point towards itself, in the same way a "
             "heavier weight drags a see-saw down on its own side", "correct": False,
             "why": "A stronger source needs LESS distance to weaken down to the "
                    "other's level, so the balance point actually moves away from "
                    "it, towards the weaker magnet."},
            {"text": "It stays exactly half way, since a neutral point is always the "
             "midpoint between two magnets", "correct": False,
             "why": "The neutral point is only exactly at the midpoint when the "
                    "two magnets are equally strong. Making one stronger shifts "
                    "the balance."},
            {"text": "The neutral point vanishes entirely, because it can only "
                     "exist between two identical magnets of exactly matched "
                     "strength", "correct": False,
             "why": "A neutral point still exists between two unequal magnets — it "
                    "is simply no longer exactly in the middle."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h13",
        "band": "harder",
        "text": "A field map is drawn showing a magnetic field line that starts on "
                "the north pole and simply fades away into nothing, without "
                "reaching the south pole. An examiner marks this map as "
                "scientifically wrong. Explain the reasoning.",
        "options": [
            {"text": "The examiner is being too strict — a line can "
                     "legitimately fade away like this, since the field does "
                     "run out of strength eventually", "correct": False,
             "why": "A field never simply fades to nothing in open space around a "
                    "magnet. Every line genuinely closes into a loop, so the "
                    "examiner's mark is correct."},
            {"text": "Every magnetic field line must close into a loop, running back "
             "to the south pole and through the magnet; one that fades away "
             "breaks that rule", "correct": True},
            {"text": "The line should have started at the south pole instead of "
                     "the north pole, since outside a magnet the lines run from "
                     "south to north", "correct": False,
             "why": "Starting at the north pole and running towards the south is "
                    "correct. The actual fault is that the line was drawn stopping "
                    "in mid-air rather than reaching the south pole."},
            {"text": "Field lines are always straight, so a fading, curving "
                     "line is automatically wrong, exactly as the rule taught "
                     "for two flat parallel plates shows", "correct": False,
             "why": "Curved lines are completely normal around a bar magnet. The "
                    "real problem is that this one never reaches the south pole at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h14",
        "band": "harder",
        "text": "A student argues: \"A magnetic field and an electric field must "
                "work in exactly the same way, since both are drawn with lines that "
                "show direction and crowding.\" What is the flaw in this argument?",
        "options": [
            {"text": "Electric fields are not drawn with lines of any kind, so "
                     "the comparison is meaningless", "correct": False,
             "why": "Electric fields are drawn with lines too, which is exactly "
                    "why the comparison can be made — and why the "
                    "loop-versus-open-ended difference matters."},
            {"text": "Magnetic fields do not have a direction, unlike electric "
                     "ones", "correct": False,
             "why": "A magnetic field line has a clear direction at every point, "
                    "shown by its arrow — the real difference is about closed "
                    "loops versus open ends."},
            {"text": "Sharing a drawing convention does not mean the two fields "
             "behave identically — a magnetic line closes into a loop, while "
             "an electric one starts and stops on charges", "correct": True},
            {"text": "There is no flaw — the two fields are identical in every "
                     "way, and the source is the one thing that differs", "correct": False,
             "why": "The two fields differ in a genuine, structural way: one forms "
                    "closed loops and the other does not. That is more than just a "
                    "difference of source."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h15",
        "band": "harder",
        "text": "A magnet is fully enclosed in a sealed steel box, thick enough "
                "that a compass held outside shows no response at all. Does this "
                "prove that a magnetic field cannot pass through solid materials?",
        "options": [
            {"text": "Yes — this proves that no solid material anywhere lets a "
                     "magnetic field through it, in the same way that a solid "
                     "wall stops light or sound from reaching the far side", "correct": False,
             "why": "Plenty of solids, such as glass, plastic and paper, let a "
                    "field straight through undisturbed. It is specifically "
                    "steel's own magnetic behaviour that explains this box."},
            {"text": "Yes, for fields stronger than a certain size", "correct": False,
             "why": "The result has nothing to do with the field's strength. It is "
                    "about the material of the box, which happens to be one of the "
                    "magnetic ones."},
            {"text": "No — the compass has simply broken from being too close to the "
             "magnet", "correct": False,
             "why": "There is no reason to assume the compass is broken. The steel "
                    "box genuinely can redirect the field away from the outside."},
            {"text": "No — it shows that STEEL specifically can redirect and trap a "
             "field within itself; non-magnetic solids like glass or plastic "
             "still let a field straight through", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h16",
        "band": "harder",
        "text": "A field map correctly shows crowding near the poles of a bar "
                "magnet. A second, completely separate map of the SAME magnet is "
                "drawn with twice as many lines throughout, still correctly crowded "
                "near the poles in the same proportion. Do the two maps disagree "
                "about anything physical?",
        "options": [
            {"text": "No — both represent the identical underlying field; only the "
             "density of sampling differs between them", "correct": True},
            {"text": "Yes — the map with more lines shows a physically stronger "
             "magnet", "correct": False,
             "why": "Drawing more lines is a choice about how densely to sample "
                    "the SAME field. It does not mean the magnet itself is any "
                    "stronger."},
            {"text": "Yes — doubling the lines doubles the actual number of field "
             "lines that physically exist, the same way doubling the marks "
             "on a ruler would double the actual length being measured", "correct": False,
             "why": "Field lines are not physical objects with a fixed real count "
                    "to double. They are a drawing convention chosen by whoever is "
                    "mapping the field."},
            {"text": "It cannot be decided without also doubling the strength "
                     "of the real magnet, so that the extra lines have "
                     "something to show", "correct": False,
             "why": "Nothing about the real magnet needs to change for two "
                    "differently-sampled maps of it to both be correct."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h17",
        "band": "harder",
        "text": "A compass is walked in a large circle at a fixed distance all the "
                "way around a single bar magnet, and its bearing is recorded at "
                "every point. Would you expect the STRENGTH reading to be the same "
                "at every point on that circle?",
        "options": [
            {"text": "It is impossible to say without knowing the exact "
                     "material the magnet is made from, since different metals "
                     "spread their field round a circle differently", "correct": False,
             "why": "The material affects how strong the magnet is overall, but "
                    "the SHAPE of the variation around a bar magnet's own field "
                    "follows from its shape, not its material."},
            {"text": "No — points on the circle nearer a pole read stronger than "
             "points nearer the middle of the magnet's side, even at the "
             "same fixed distance", "correct": True},
            {"text": "Yes — a fixed distance from the magnet's centre always gives a "
             "fixed strength, wherever you are on the circle, in the same "
             "way a ball's surface is the same distance from its centre at "
             "every point around it", "correct": False,
             "why": "A bar magnet's field is not evenly spread around it like a "
                    "ball. Points level with a pole are far closer to where the "
                    "field concentrates than points level with the middle."},
            {"text": "Yes, provided the bearing recorded is also the same "
                     "everywhere on the circle, since a steady bearing is a "
                     "sign of a steady strength", "correct": False,
             "why": "The bearing genuinely changes around the circle too, but that "
                    "is a separate fact from strength — strength still varies with "
                    "how close a point is to a pole."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h18",
        "band": "harder",
        "text": "Two bar magnets are placed end to end, like poles facing, with a "
                "neutral point between them. A THIRD identical magnet is then "
                "brought up and placed exactly at the neutral point, aligned along "
                "the same line, without touching either of the first two. What is "
                "most likely to happen?",
        "options": [
            {"text": "The third magnet becomes permanently fixed in place, unable to "
             "be moved by hand, the way objects are sometimes assumed to get "
             "stuck once caught between two opposing pulls", "correct": False,
             "why": "Nothing about a neutral point locks an object in place. With "
                    "no net field there, the third magnet is free to be moved as "
                    "normal."},
            {"text": "The neutral point instantly moves to a completely different, "
             "unrelated location", "correct": False,
             "why": "Introducing a third magnet does shift the overall picture in "
                    "principle, but the ORIGINAL two magnets' own cancellation at "
                    "that spot is not erased by it."},
            {"text": "The third magnet feels no net force from the first two, since "
             "their fields still cancel at that spot, though it interacts "
             "with each of them individually", "correct": True},
            {"text": "The third magnet is instantly repelled away from both of the "
             "others at once", "correct": False,
             "why": "There is no combined field at that point to repel it with — "
                    "the first two magnets' fields still cancel there, whatever is "
                    "placed at the spot."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h19",
        "band": "harder",
        "text": "A student proposes testing whether a mystery block is a magnet by "
                "wrapping it in several layers of cling film and checking whether a "
                "compass still responds through the wrapping. Is this a fair test "
                "of whether the block is magnetic?",
        "options": [
            {"text": "No — any wrapping would block a magnetic field "
                     "completely, so a compass held outside the cling film "
                     "could never answer the question either way", "correct": False,
             "why": "Cling film is not a magnetic material, so it does not block a "
                    "field at all. A genuinely magnetic block would still be "
                    "detected through it."},
            {"text": "No — cling film itself becomes magnetised and would give a "
             "false positive result", "correct": False,
             "why": "Cling film cannot be magnetised, since it is not one of the "
                    "four magnetic materials. It has no effect on the test either "
                    "way."},
            {"text": "It depends on how many layers of film are used, since each "
             "layer weakens the field a little", "correct": False,
             "why": "Non-magnetic wrapping does not weaken a magnetic field at "
                    "all, however many layers are added — only distance and "
                    "magnetic materials matter."},
            {"text": "Yes — cling film is not a magnetic material, so it cannot "
             "block a real field, making the compass response a fair test of "
             "the block itself", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h20",
        "band": "harder",
        "text": "A field map of two magnets shows a neutral point. Nearby, at a "
                "different location entirely, a compass held near a single "
                "unrelated third magnet gives a perfectly normal, settled reading. "
                "Explain why finding a neutral point in one part of a set-up does "
                "not mean the field is zero everywhere.",
        "options": [
            {"text": "A neutral point is a specific location where two particular "
             "fields happen to cancel; away from that exact spot, and around "
             "unrelated magnets, the field is whatever it normally would be", "correct": True},
            {"text": "A neutral point spreads outward and gradually cancels "
                     "every field in the whole room", "correct": False,
             "why": "A neutral point is a single location, not a spreading effect. "
                    "Fields elsewhere, especially around unrelated magnets, are "
                    "completely unaffected by it."},
            {"text": "The third magnet's compass reading must be a mistake, "
                     "since a neutral point has already been found nearby and "
                     "cancels the field for the whole bench", "correct": False,
             "why": "There is no reason to doubt the third reading. A neutral "
                    "point is local to the two magnets that produced it, not a "
                    "property of the whole room."},
            {"text": "Every set-up has just one neutral point in total, so the "
                     "third magnet cannot be sitting in a field of its own", "correct": False,
             "why": "A neutral point belongs to whichever combination of sources "
                    "produced it. An unrelated third magnet has its own ordinary "
                    "field, unaffected by the first two."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h21",
        "band": "harder",
        "text": "A student draws a field map showing lines that are evenly spaced "
                "everywhere but bent into random wavy shapes for artistic effect, "
                "with the crowding and general direction still scientifically "
                "correct. Is this map scientifically acceptable?",
        "options": [
            {"text": "No — because wavy lines mean the field is changing over "
                     "time, and this drawing is of a magnet whose field is "
                     "perfectly steady", "correct": False,
             "why": "Wavy, inaccurate lines are simply a drawing error here, not a "
                    "sign of a field that changes with time — this is a static bar "
                    "magnet's field."},
            {"text": "No — the exact PATH each line takes between readings should "
             "follow the field's own smooth curve, not an arbitrary wavy "
             "shape chosen for effect", "correct": True},
            {"text": "Yes — as long as the crowding and the general direction "
                     "of the lines are right, the exact path each line takes "
                     "can be drawn however the artist likes", "correct": False,
             "why": "The path a line takes is not free to choose — it should "
                    "follow the smooth curve the compass readings actually trace "
                    "out, not an arbitrary wavy shape."},
            {"text": "Yes, provided the map is clearly labelled as artistic "
                     "rather than scientific, which frees it from the usual "
                     "plotting rules", "correct": False,
             "why": "A label does not fix the underlying problem — the path drawn "
                    "should genuinely reflect the readings taken, whatever the map "
                    "is called."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h22",
        "band": "harder",
        "text": "A neutral point exists between two bar magnets with like poles "
                "facing. Both magnets are then moved, keeping the same distance "
                "apart, so that the whole pair slides two metres to the left. What "
                "happens to the neutral point?",
        "options": [
            {"text": "It disappears entirely, since a neutral point belongs to "
                     "one specific location in a room", "correct": False,
             "why": "A neutral point is not tied to a particular spot in the room. "
                    "It exists wherever the two magnets' fields happen to balance, "
                    "and moves if they do."},
            {"text": "It splits into two separate neutral points, one for each "
             "magnet", "correct": False,
             "why": "A neutral point is a single location where the combined field "
                    "is zero. Moving both magnets together does not create a "
                    "second one."},
            {"text": "It slides two metres to the left along with the magnets, since "
             "nothing about the balance between them has changed", "correct": True},
            {"text": "It stays fixed in its original position in the room, now no "
             "longer between the two magnets", "correct": False,
             "why": "A neutral point is set by the two magnets' own positions "
                    "relative to each other, not by any fixed point in the room, "
                    "so it moves with them."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h23",
        "band": "harder",
        "text": "A magnetic field line and a stretched piece of string both form "
                "smooth curves in a diagram. Give one clear scientific reason it "
                "would be a mistake to treat a field line as though it behaved like "
                "a real, physical piece of string.",
        "options": [
            {"text": "A piece of string can be curved but a field line must always "
             "be perfectly straight, the same rule sometimes wrongly applied "
             "to the electric field lines between flat charged plates", "correct": False,
             "why": "Field lines around a bar magnet are curved almost everywhere, "
                    "so straightness is not the distinguishing feature here."},
            {"text": "A field line can be seen with the naked eye without any "
             "equipment, unlike string", "correct": False,
             "why": "It is the opposite way round — a field line cannot be seen "
                    "directly at all; it has to be mapped using a compass or "
                    "filings."},
            {"text": "String only exists indoors, while field lines only exist "
             "outdoors", "correct": False,
             "why": "Neither claim about location is true or relevant — field "
                    "lines exist around any magnet, indoors or outdoors, exactly "
                    "as string can be found in either."},
            {"text": "A field line has no tension, thickness or actual material — it "
             "represents a series of DIRECTIONS, not an object that could be "
             "cut, pulled or measured for length", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h24",
        "band": "harder",
        "text": "A steel disc is placed at a neutral point between two magnets and "
                "left there. Weeks later, is the disc likely to have become "
                "magnetised by either magnet?",
        "options": [
            {"text": "Very little, if at all — with the two fields cancelling at "
             "that exact point, there is almost nothing there to magnetise "
             "it", "correct": True},
            {"text": "Yes, strongly — a neutral point is where magnetism builds "
                     "up over time from both magnets combined, collecting in "
                     "whatever is left sitting there", "correct": False,
             "why": "A neutral point is where the field cancels, not where it "
                    "builds up. There is very little field present there to "
                    "magnetise anything, even over a long time."},
            {"text": "Yes, by whichever magnet happens to be slightly closer", "correct": False,
             "why": "At a true neutral point the contributions are exactly "
                    "balanced, leaving essentially nothing to magnetise the disc "
                    "from either side."},
            {"text": "It becomes magnetised only if it is left there for more "
                     "than a year, since weak magnetism needs a long time to "
                     "soak in", "correct": False,
             "why": "Time is not the deciding factor here. With the field already "
                    "essentially zero at that spot, waiting longer does not change "
                    "the outcome."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h25",
        "band": "harder",
        "text": "A student says: \"Since a compass always settles somewhere, a truly "
                "zero magnetic field is impossible in real life.\" Using what this "
                "lesson has shown about neutral points, explain what is wrong with "
                "this claim.",
        "options": [
            {"text": "Neutral points are a theoretical idea, not found on a "
                     "real bench, since two magnets cannot be matched closely "
                     "enough", "correct": False,
             "why": "A neutral point is a real, reachable state on a plotting "
                    "bench, not merely a theoretical idea — a compass placed there "
                    "genuinely fails to settle."},
            {"text": "A neutral point is a genuine, real location where the field "
             "really is zero, shown by a compass staying wherever it is left "
             "rather than settling anywhere", "correct": True},
            {"text": "The claim is correct — a compass always finds SOME "
                     "direction, however faint the field, because a needle "
                     "balanced on a pivot has to come to rest pointing "
                     "somewhere", "correct": False,
             "why": "At a genuine neutral point a compass does not settle to any "
                    "direction at all — it simply stays at whatever angle it is "
                    "left, which is exactly the evidence for a real zero field."},
            {"text": "A compass settles at a neutral point because a needle is "
                     "itself a magnet, and a magnet makes the very field it "
                     "then lines up with", "correct": False,
             "why": "A needle's own field travels round with it and cannot turn "
                    "the needle itself. What turns a needle is the field of "
                    "everything else, and at a neutral point that adds to zero."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h26",
        "band": "harder",
        "text": "A field map shows a bar magnet's lines all correctly leaving the "
                "north pole and entering the south pole outside the metal. A "
                "student then adds extra lines INSIDE the drawn outline of the "
                "magnet, running from north to south, the same direction as "
                "outside. Is this addition correct?",
        "options": [
            {"text": "Yes, provided the lines inside are drawn shorter than the ones "
             "outside", "correct": False,
             "why": "Length of the lines is not the issue — the direction drawn "
                    "inside the magnet is the wrong way round, whatever length is "
                    "used."},
            {"text": "It cannot be judged without knowing exactly how strong the "
             "magnet is", "correct": False,
             "why": "Strength does not decide which way the lines run inside a "
                    "magnet. Every magnet's internal lines run from south to "
                    "north, regardless of strength."},
            {"text": "No — inside the magnet the lines run the OTHER way, from "
                     "south back to north, to close the loop", "correct": True},
            {"text": "Yes — the direction inside a magnet is the same as the "
                     "direction just outside, since a line cannot turn round", "correct": False,
             "why": "The direction reverses inside the magnet: lines run from "
                    "south back to north there, which is what closes each line "
                    "into a loop."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h27",
        "band": "harder",
        "text": "A single bar magnet's field is mapped at two points the same "
                "distance from its centre: point X level with a pole, and point Y "
                "level with the middle of the magnet's side. Explain which point "
                "reads stronger, and why.",
        "options": [
            {"text": "Point Y reads stronger, because the middle of a magnet is "
             "always its most powerful part", "correct": False,
             "why": "The middle of a bar magnet's LENGTH is actually where the "
                    "field outside is weakest, not strongest — the poles are where "
                    "it concentrates."},
            {"text": "Both points read exactly the same, since the two of them "
                     "sit at the same distance from the magnet's own centre as "
                     "each other", "correct": False,
             "why": "Distance from the centre alone does not decide strength here "
                    "— being level with a pole puts a point far closer to where "
                    "the field actually concentrates."},
            {"text": "Neither point gives a meaningful reading without also knowing "
             "the magnet's total length", "correct": False,
             "why": "The comparison between the two points can be made directly "
                    "from their position relative to the poles, without needing "
                    "the magnet's exact length."},
            {"text": "Point X reads stronger, because it sits much closer to the "
             "concentrated field right at a pole than point Y does to "
             "anything", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h28",
        "band": "harder",
        "text": "A student claims that because iron filings and a plotting compass "
                "both reveal the SAME field, either instrument gives exactly the "
                "same information. What key piece of information does a compass "
                "give that filings do not?",
        "options": [
            {"text": "The compass gives the DIRECTION the field points in at a spot; "
             "filings only show the overall shape, not which way along it "
             "the field runs", "correct": True},
            {"text": "The compass shows where the field is strongest; filings cannot "
             "show strength at all, since loose filings are assumed to "
             "gather just as thickly wherever they happen to fall", "correct": False,
             "why": "Filings actually show strength reasonably well, through how "
                    "thickly they gather. What a compass adds is the DIRECTION, "
                    "which filings cannot show."},
            {"text": "The compass works even where there is no field at all, unlike "
             "filings", "correct": False,
             "why": "A compass at a place with genuinely no field simply fails to "
                    "settle, exactly as filings would show a bare patch there. "
                    "Neither works where there is nothing to detect."},
            {"text": "The compass can be used without a magnet present; filings "
                     "need a magnet to work, since a needle carries its own "
                     "north-seeking end with it", "correct": False,
             "why": "Both instruments need an actual field to respond to in the "
                    "first place — neither reveals anything without one."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h29",
        "band": "harder",
        "text": "Two identical bar magnets are placed side by side, both pointing "
                "the same way (north ends both on the same side). A field line "
                "leaving one magnet's north pole is traced. Explain why it does NOT "
                "simply run straight into the neighbouring magnet's south pole, the "
                "way it would with a single unlike pair.",
        "options": [
            {"text": "Placing two magnets side by side cancels both of their "
                     "fields completely, since each one's north pole pushes the "
                     "other's field flat", "correct": False,
             "why": "With both norths on the same side, the fields add up there "
                    "rather than cancelling — cancelling needs opposing "
                    "directions, which this arrangement does not give on that "
                    "side."},
            {"text": "Both magnets have their north poles on the same side, so there "
             "is never a nearby south pole for that line to run into — it "
             "curves round through the wider space instead", "correct": True},
            {"text": "Field lines from two side-by-side magnets never interact "
                     "with each other at all, since every line belongs to one "
                     "magnet alone and keeps strictly to its own half of the "
                     "space", "correct": False,
             "why": "The two fields absolutely do interact and add together on the "
                    "shared side. The reason the line avoids the other magnet is "
                    "that both norths sit on the same side, with no nearby south "
                    "to enter."},
            {"text": "The line stops entirely once it leaves the first magnet's "
                     "north pole, blocked by the second magnet's own field "
                     "pushing back at it", "correct": False,
             "why": "A field line never simply stops in space. It still closes "
                    "into a loop eventually — it is only prevented from taking the "
                    "short route into a neighbouring south pole that is not there."},
        ],
        "figure": None,
    },
    {
        "id": "p10-02-h30",
        "band": "harder",
        "text": "A field map shows a single neutral point between two unequal "
                "magnets, like poles facing. Explain, using the idea of the field "
                "falling off with distance, why the neutral point sits closer to "
                "the WEAKER magnet rather than exactly in the middle.",
        "options": [
            {"text": "It is a fixed rule that a neutral point always sits exactly "
             "one third of the way from the stronger magnet", "correct": False,
             "why": "There is no fixed fraction like one third. Exactly where the "
                    "point sits depends on how much stronger one magnet is than "
                    "the other."},
            {"text": "The weaker magnet's field reaches further than the "
                     "stronger one's, which is why it wins nearer to itself, "
                     "since a weak field spreads out over a wider space instead "
                     "of staying close in", "correct": False,
             "why": "The weaker magnet's field does not reach further — it is "
                    "weaker at every distance. The neutral point sits near it only "
                    "because it needs less room to fall to match the far stronger "
                    "source."},
            {"text": "The stronger magnet's field is still large even further away, "
             "so the balance point has to sit nearer the weaker magnet, "
             "where its own field has less distance left to fall over", "correct": True},
            {"text": "The neutral point sits closer to the weaker magnet simply "
             "because weaker magnets are usually smaller in size", "correct": False,
             "why": "Physical size is not what decides this — it is purely about "
                    "how each magnet's field strength falls off with distance from "
                    "it, regardless of how big it is."},
        ],
        "figure": None,
    },
]
