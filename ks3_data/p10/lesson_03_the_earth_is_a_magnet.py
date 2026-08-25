"""P10 L3 — The Earth is a magnet (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p10/p10-03-the-earth-is-a-magnet.dc.html`.

Her page wins outright. The compass on an empty table, the nine latitudes, the
three bench objects, the two mountings, the three norths and all four rungs
are hers.

── ⚖️ THE NAMING PROBLEM IS THE LESSON, NOT AN ASIDE ─────────────────

The needle's NORTH-SEEKING end swings towards the Arctic; unlike poles
attract; therefore the magnetic pole up there is a SOUTH pole. Every part of
that argument is on the page, and rung 1 asks for it directly. `MAG-09` is the
belief it breaks, and it is one of the few misconceptions in the key stage
that a textbook's own wording created.

── ⚖️ THE MODEL, AND WHAT IT LEAVES OUT ──────────────────────────────

Her §9 ruling 3, applied: a CENTRED DIPOLE aligned with the spin axis. Dip
follows `tan(dip) = 2 tan(latitude)` and the sideways part of the field goes
as `cos(latitude)` — 100 at the equator, zero at the pole. Measured across her
nine latitudes:

    60 S   dip −73.9°   sideways  50.0        20 N   dip 36.1°   94.0
    40 S   dip −59.2°   sideways  76.6        40 N   dip 59.2°   76.6
    20 S   dip −36.1°   sideways  94.0        52 N   dip 68.7°   61.6
    equator dip   0.0°  sideways 100.0        70 N   dip 79.7°   34.2
                                              90 N   dip 90.0°    0.0

Her §8 makes the legal line's hedges load-bearing and they stay: the magnetic
axis is tilted about eleven degrees from the spin axis, so magnetic and
geographic latitude are not the same and dip measured in the field differs
from the figure here by several degrees in most places.

── ⚠️ TWO MEASURED CORRECTIONS, AND WHY ──────────────────────────────

Both found by enumerating her `renderVals` over all 54 states, and both are
`DEPARTURES-P10.md` rows.

**1. HER FLAT NOTE CONTRADICTS ITSELF AT THE EQUATOR.** It reads *"The angle
of dip reads zero because the mounting is holding it there, not because the
field is level — at {place} the field itself is running into the ground at
{dip}°"*, which is exactly right at eight of her nine latitudes and false at
the ninth: at the equator the field IS level, and the sentence renders
*"…running into the ground at 0°"* while denying that the field is level. Two
reachable states — clamped flat at the equator, with nothing or with the steel
stand on the bench. Its own branch here, so the mounting is still named and
the physics is still true.

**2. `barely — it is sluggish` COULD NOT BE REACHED.** Her threshold is a
sideways pull below 12, and no latitude on her own list is below 12 without
being the pole, which has its own branch. So the verdict is copy no student
can ever see — while her RUNG 4 asks the student to explain precisely that
state (*"the sideways part of the field … becomes very small there … the
needle therefore settles slowly"*). A bench that never shows it leaves the
rung with nothing behind it. The threshold is 40 here, which 70° north reaches
at 34.2 and 52° north does not at 61.6, so exactly one latitude reads it — the
one the rung is written about. Real compasses are sold in balancing zones for
this reason, so the claim is defensible as well as reachable.

── ⚖️ THE STATE SPACE ────────────────────────────────────────────────

    9 latitudes × 3 bench objects × 2 mountings      54
      the speaker magnet wins                        18
      the steel clamp stand wins, above 70°           4
      clamped flat, and the field is not level       13
      clamped flat at the equator                     2
      clamped flat on the pole                        1
      free to tip                                    15
      free to tip on the pole                         1

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's hook, gate and both rungs all put the correct answer at index 0.
**Her option TEXT and every correction are verbatim; only the ORDER moves.**
This lesson takes indices 3 (hook), 0 (gate, hers), 2 (rung 1) and 1 (rung 2).

── ⚠️ MRB-177 · ONE LENGTH TELL, REMEDIED AT THE DISTRACTOR ──────────

Rung 2's correct option is 19 words against a longest distractor of 13.
Remedied at the calibration distractor, which now states its wrong rule
completely — *compasses made today are calibrated to a different north from
the ones made forty years ago* — and which her own correction already answers
word for word. The correct answer is untouched.

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ─────────────────────
"""

LESSON = {
    "slug": "the-earth-is-a-magnet",
    "title": "The Earth is a magnet",
    "discipline": "physics",
    "unit": "Magnetism and electromagnetism",
    "family": "SYSTEM",

    "covers": ["KS3.P.MAG.03"],
    # ⚠️ `touches`, NOT a second `covers`. Design's §1 claims `MAG.02` here as
    # well as on `p10-02` and records that as needing no notation; `covers` is
    # exactly-once across the key stage and `verify_ks3` asserts it. The page
    # genuinely USES plotting — the whole bench is a compass reading a field —
    # so the statement is carried as a touch, which is what the register has
    # for exactly this.
    "touches": ["KS3.P.MAG.02", "KS3.WS.MEA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "forces-and-fields", "level": 3},
                {"id": "earth-and-universe", "level": 2}],
    "typical_year": 9,
    "typical_minutes": 60,

    # ⚠️ Design's §3: this page restates that a compass needle is a small
    # magnet that lines up with a field, and restates like-repels-unlike-
    # attracts in one clause, because the naming of the Arctic pole turns on
    # it. The edge is declared as the honest reading order and nothing is
    # assumed.
    "requires": ["magnetic-fields"],
    "assumes": [],
    "references": [{"unit": "P9", "lesson": "electric-fields"},
                   {"unit": "P8", "lesson": "current-and-circuits"}],
    "ks4_links": [],

    "meta_description": "A compass settles the same way on an empty table in "
                        "an empty field — because the whole planet has a "
                        "magnetic field, and the pole in the Arctic is "
                        "magnetically a south pole.",

    "big_question": "Nothing is near the compass and it still finds north, so "
                    "what is it lining up with — and why does the pole it "
                    "turns towards have to be a magnetic south pole?",

    "rail": [
        {"anchor": "s-hook",  "short": "COMPASS",
         "label": "It still finds north",  "done_when": "committed"},
        {"anchor": "s-bench", "short": "BENCH",
         "label": "Take it somewhere else", "done_when": "gate_and_a_control"},
        # ⚠️ Design's `DONE` gives this stop the GATE alone; the bench marks
        # it through `band_anchor` / `band_at`. See `ks3_art/p10.py`.
        {"anchor": "s-earth", "short": "NORTHS",
         "label": "Three norths",          "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Nothing is near it. It still finds north.",
        "prompt": "Put a compass on an empty table in the middle of an empty "
                  "field. There is no magnet within a mile of it, and no "
                  "metal. Spin it, and it settles pointing the same way every "
                  "single time. Carry it a hundred kilometres and it still "
                  "settles the same way.",
        "commit": "What is the needle finding?",
        # ⚠️ MRB-278 — position 3.
        "options": [
            "The needle is attracted to the North Star, which is why it works "
            "outdoors",
            "North is the direction the Earth spins towards, and the needle "
            "is dragged round with it",
            "There is a mass of iron ore at the North Pole strong enough to "
            "pull the needle from anywhere",
            "The Earth itself has a magnetic field, and the needle is a "
            "magnet lining up with it",
        ],
        "answer": 3,
        "reveal": "The planet. The Earth has a magnetic field that reaches "
                  "everywhere on its surface and out into space, and a "
                  "compass needle is simply a small magnet free to turn, so "
                  "it does what any magnet in a field does and lines up with "
                  "it. Nothing has to be nearby, because the field is not "
                  "made nearby — it is made in the Earth's core, thousands of "
                  "kilometres down.",
    },

    "misconceptions": [
        {"id": "MAG-09",
         "statement": "The Earth's North Pole is a magnetic north pole.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "MAG-10",
         "statement": "A compass points at the North Pole.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        # ⚠️ `elicited_by` IS THE BENCH, AND THAT IS HONEST RATHER THAN
        # CONVENIENT: its globe draws a bar magnet inside the Earth, which is
        # the picture that plants the belief. It is confronted in the
        # explainer that has an id for exactly this reason.
        {"id": "MAG-11",
         "statement": "There is a bar of iron inside the Earth.",
         "elicited_by": "dip",
         "confronted_by": "no-bar-down-there"},
        # ⊕ MINTED FROM THE COMMIT GATE'S THIRD OPTION. Separate from
        # `MAG-10`: a student who has given up "it points AT the pole"
        # entirely can still expect the reading to be best where the pole is,
        # and it is the exact opposite of what happens — the bench's own
        # at-the-pole state is what breaks it, and rung 4 asks for it.
        {"id": "MAG-12",
         "statement": "A compass works better at the magnetic pole than "
                      "anywhere else, because that is what it has been "
                      "pointing at all along.",
         "elicited_by": "dip",
         "confronted_by": "dip"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A compass needle is a small magnet, balanced so it can "
                 "turn. A magnet turns until it lies along a magnetic field. "
                 "Since the needle settles the same way everywhere on Earth, "
                 "there must be a magnetic field covering the whole planet — "
                 "and there is. <strong>The Earth behaves as though a huge "
                 "bar magnet were buried inside it</strong>, tilted a little "
                 "from the axis it spins on."},
        # ⚠️ THIS BLOCK CARRIES AN `anchor` AND IT IS LOAD-BEARING. `MAG-11`
        # is confronted here and nowhere else on the page, and MRB-244
        # requires every `confronted_by` to name a real element on its own
        # page. The anchor is an anchor and nothing else: no treatment
        # changes, and Design's own explainer stack is untouched.
        #
        # ⚠️ `anchor`, NOT `id`. `_id_attr` reads `anchor` alone — `id` names
        # the ACTIVITY a block renders, and reading it as an anchor would put
        # an activity's name in the URL. Authored as `id` first, this emitted
        # NOTHING and the misconception's `confronted_by` pointed at an
        # element that was never on the page. Caught by MRB-244's gate, which
        # is exactly what it exists for.
        {"type": "explainer",
         "anchor": "no-bar-down-there",
         "text": "There is no actual bar of iron down there. The Earth's core "
                 "is far too hot for that: above a few hundred degrees a "
                 "magnet loses its magnetism altogether. What is down there "
                 "is an ocean of liquid iron, and its slow churning carries "
                 "electric currents, and moving charge makes a magnetic "
                 "field. The buried-bar-magnet picture is a model of the "
                 "field's shape, not a description of the rock."},
        {"type": "explainer",
         "text": "Now the part that catches people out. The needle's "
                 "<strong>north-seeking</strong> end points towards the "
                 "Arctic. Unlike poles attract. So the magnetic pole up there "
                 "must be a <strong>south</strong> pole, and the Earth's "
                 "field runs from the far south, round through space, and "
                 "back into the north. The naming is historical: the ends of "
                 "the needle were named for where they pointed, centuries "
                 "before anybody knew why."},
        {"type": "explainer",
         "text": "The magnetic pole is also not in the same place as the "
                 "geographic one, and it wanders — by tens of kilometres in a "
                 "year. The angle between the way the needle points and true "
                 "north is called the <strong>declination</strong>, it is "
                 "different in different countries, and any map used for "
                 "serious navigation prints the local value and the date it "
                 "was measured."},

        # ── #s-bench · a compass free to swing in any direction ────────
        {"type": "dip-circle",
         "id": "dip",
         "anchor": "s-bench",
         "eyebrow": "At the bench · a compass free to swing in any direction",
         "heading": "Take the same compass somewhere else.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Three controls live"},
         # ⚠️ HER SECOND SENTENCE IS CUT. It read "Choose how far north or
         # south you take it, choose what is sitting on the bench beside it,
         # and choose whether it is clamped flat or left free" — three clauses
         # naming three controls already on screen (5A.1). The set-up sentence
         # stays: how this compass is hung is the one thing that makes the
         # tipping readable at all.
         "lead": "This compass is hung at its centre so it can tip as well as "
                 "turn.",
         "band_anchor": "s-earth",
         "band_at": 1,
         # ⚖️ THE LATITUDE ABOVE WHICH A STEEL CLAMP STAND BEATS WHAT IS LEFT
         # OF THE EARTH. The bench says so out loud: the same stand at the
         # equator loses, because there the sideways pull is at its strongest.
         "steel_wins_at": 70,
         # ⚖️ THE SIDEWAYS-PULL READING BELOW WHICH THE NEEDLE IS CALLED
         # SLUGGISH. Design's 12 is unreachable on her own list of latitudes;
         # 40 is reached by 70° north at 34.2 and by nothing else. See the
         # module docstring.
         "nav_at": 40,
         "start_near": 0,
         "start_mount": 1,
         "near_label": "On the bench beside it",
         "mount_label": "How it is mounted",
         "lat_control": {"label": "Where you are", "min": 0, "max": 8,
                         "step": 1, "start": 6,
                         "value": "52° north — southern England"},
         "gate": {
             "prompt": "Commit first. A walker carries an ordinary compass to "
                       "a point directly above the Earth's magnetic pole in "
                       "the Arctic. What does it do?",
             # ⚠️ Design's own order, and her own index 0 — kept, because this
             # unit's five gates take 3, 2, 0, 2, 1 and index 0 is used once.
             "options": [
                 "It points down into the ground and gives no direction along "
                 "the surface at all",
                 "It spins round and round, because every direction is south",
                 "It points more strongly than anywhere else, because the "
                 "pole is right there",
                 "It reverses and points south, because it has passed the "
                 "pole",
             ],
             "answer": 0,
         },
         "lats": [
             {"deg": -60, "name": "60° south — the Southern Ocean"},
             {"deg": -40, "name": "40° south — southern New Zealand"},
             {"deg": -20, "name": "20° south — northern Australia"},
             {"deg": 0, "name": "the equator"},
             {"deg": 20, "name": "20° north — southern Egypt"},
             {"deg": 40, "name": "40° north — Madrid"},
             {"deg": 52, "name": "52° north — southern England"},
             {"deg": 70, "name": "70° north — northern Norway"},
             {"deg": 90, "name": "90° north — the magnetic pole itself"},
         ],
         "near": [
             {"id": "none", "label": "Nothing at all"},
             {"id": "steel", "label": "A steel clamp stand"},
             {"id": "magnet", "label": "A speaker magnet"},
         ],
         "mounts": [
             {"id": "flat", "label": "Clamped flat"},
             {"id": "free", "label": "Free to tip"},
         ],
         "readouts": [
             {"id": "turn", "label": "Which way it turns", "sub": "—"},
             {"id": "dip", "label": "Angle of dip", "sub": "—"},
             {"id": "horiz", "label": "Sideways pull to work with",
              "sub": "where 100 is the strongest here"},
             {"id": "nav", "label": "Can you navigate by it"},
         ],
         # ⚠️ `{place}` is the latitude's own name, `{dip}` the angle of dip
         # in whole degrees with no sign, and `{horiz}` the sideways pull on
         # the declared scale.
         "branches": {
             "captured_magnet": {
                 "turn": "towards the speaker magnet",
                 "sub": "the Earth has been overruled",
                 "nav": "no — it is reading the bench",
                 "note": "A speaker magnet a few centimetres away is "
                         "enormously stronger, where the compass is sitting, "
                         "than the whole Earth is. The needle lines up with "
                         "the total field, and this close that total is "
                         "almost entirely the speaker. It has not broken and "
                         "it is not lying: it is doing exactly what it always "
                         "does, which is why a compass has to be used away "
                         "from loudspeakers, phones, car bodywork and steel "
                         "railings. Take the magnet off the bench and the "
                         "Earth is back in charge."},
             "captured_steel": {
                 "turn": "pulled towards the clamp stand",
                 "sub": "steel nearby, weak field here",
                 "nav": "no — the steel wins",
                 "note": "At {place} the sideways part of the Earth’s field "
                         "is down to {horiz} on this scale, and a steel clamp "
                         "stand beside the compass has been magnetised by "
                         "that same field into a small magnet of its own. "
                         "Close up, the stand beats what is left of the "
                         "Earth, and the needle goes to the stand. The same "
                         "stand at the equator would lose, because there the "
                         "Earth’s sideways pull is at its strongest."},
             "flat": {
                 "turn": "settles to magnetic north",
                 "sub": "held level, so it cannot tip",
                 "note": "Held flat, the needle can only turn, not tip, so it "
                         "lines up with the sideways part of the Earth’s "
                         "field and settles on magnetic north. The angle of "
                         "dip reads zero because the mounting is holding it "
                         "there, not because the field is level — at {place} "
                         "the field itself is running into the ground at "
                         "{dip}°. What matters for navigation is the sideways "
                         "pull, and here that is {horiz} on this scale. This "
                         "is why an ordinary walking compass is built flat."},
             # ⊕ THE EQUATOR, WHERE HER SENTENCE WOULD BE FALSE. The mounting
             # is still named, because the reading is still a fact about the
             # clamp — but here it agrees with the field instead of hiding it,
             # and saying so is the whole difference between a reading and a
             # coincidence.
             "flat_level": {
                 "turn": "settles to magnetic north",
                 "sub": "held level, so it cannot tip",
                 "note": "Held flat, the needle can only turn, not tip, so it "
                         "lines up with the sideways part of the Earth’s "
                         "field and settles on magnetic north. The angle of "
                         "dip reads zero — and at {place} that is the one "
                         "place where the mounting and the field agree, "
                         "because the field really is level here. Take the "
                         "clamp off and the needle would still hang level. "
                         "Everywhere else the zero is the clamp’s doing. The "
                         "sideways pull is {horiz} on this scale, which is as "
                         "large as it gets anywhere on the planet."},
             "flat_at_pole": {
                 "turn": "settles nowhere",
                 "sub": "held level, and nothing to turn it",
                 "nav": "no — no direction to find",
                 "note": "Clamping the compass flat stops it tipping, but at "
                         "the magnetic pole the field points straight down "
                         "and has no sideways part at all. There is no "
                         "direction for the needle to find, so it drifts and "
                         "settles nowhere. Every direction from here is "
                         "south, and a compass has run out of anything to "
                         "say."},
             "at_pole": {
                 "turn": "stands straight up",
                 "sub": "the field is vertical here",
                 "nav": "no — no direction to find",
                 "note": "Directly over the magnetic pole the field goes "
                         "straight down into the ground, so a freely hung "
                         "needle stands vertical: dip is 90° and the sideways "
                         "pull is zero. There is no horizontal direction for "
                         "it to point in and nothing to navigate by. Polar "
                         "crews are taught this and switch to satellite "
                         "positioning or a gyroscopic compass well before "
                         "they get here."},
             "tipped": {
                 "turn": "settles to magnetic north and tips",
                 "sub": "{tipword}",
                 "note": "Hung freely at {place}, the needle turns to lie "
                         "along the Earth’s field and tips over by {dip}° "
                         "from level, with its {tipend}. That happens because "
                         "the field is not parallel to the ground: it comes "
                         "out of the ground in the far south and goes into it "
                         "in the far north, so the further from the equator "
                         "you go the steeper it runs. Only the sideways part "
                         "of it turns the needle to a bearing, and that reads "
                         "{horiz} here against 100 at the equator. A walking "
                         "compass avoids the tipping altogether by being "
                         "built flat, with a counterweight under the card."},
         },
         "words": {
             "not_a_reading": "not a field reading",
             "on_bench": "the needle is on the bench object",
             "held_level": "the mounting is holding it level",
             "north_down": "north end down",
             "north_up": "north end up",
             "level_label": "LEVEL",
             "dip_tag": "{dip}° DIP",
             "nav_yes": "yes",
             "nav_barely": "barely — it is sluggish",
             "nav_none": "no — no direction to find",
             # ⚠️ TWO PHRASINGS OF ONE FACT, AND BOTH ARE NEEDED. `north end
             # down` is a readout under a tile; `north-seeking end down` is
             # what a sentence says. Design uses both, in those two places,
             # and one string in both would read as an abbreviation in the
             # note or as a mouthful in the tile.
             "tips_down": "north-seeking end tips downwards",
             "tips_up": "north-seeking end tips upwards",
             "end_down": "north-seeking end down",
             "end_up": "north-seeking end up",
         }},

        # ── #s-earth · three norths ────────────────────────────────────
        {"type": "mag-band",
         "id": "norths",
         "anchor": "s-earth",
         "eyebrow": "The figure",
         "heading": "Three norths, and only one of them is a magnetic north",
         "tiles": [
             {"id": "north-true", "eyebrow": "True north",
              "title": "The end of the spin axis",
              "body": "Where the lines of longitude meet. It is a fact about "
                      "how the Earth turns and has nothing to do with "
                      "magnetism. It does not move."},
             {"id": "north-magnetic", "eyebrow": "Magnetic north",
              "accent": True,
              "title": "Where the needle points",
              "body": "Hundreds of kilometres away from true north, and "
                      "moving year by year. In magnetic terms this place is a "
                      "<strong>south</strong> pole, because the needle's "
                      "north end is attracted to it."},
             {"id": "north-grid", "eyebrow": "Grid north",
              "title": "Straight up the map",
              "body": "The direction the squares on a printed map run. "
                      "Flattening a curved planet onto paper bends things "
                      "slightly, so this is a third answer again."},
         ],
         "close": "The angle between the needle and true north is the "
                  "<strong>declination</strong>. Walking maps print it in the "
                  "corner with the year it was measured and how fast it is "
                  "changing, because a bearing taken from an old map and "
                  "followed with a modern compass will put you in the wrong "
                  "valley."},

        {"type": "key-fact", "ref": "the-planet-has-a-field"},

        {"type": "misconception", "id": "think-north-pole",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-north-pole",
         "kind": "predict",
         "demand": "explain",
         "targets": "MAG-09",
         "statements": [
             {"quote": "The compass points north, so the Earth's North Pole "
                       "is a magnetic north pole.",
              "targets": "MAG-09",
              "body": [
                  "It cannot be. Unlike poles attract, and it is the "
                  "north-seeking end of the needle that swings towards the "
                  "Arctic — so whatever is up there has to be magnetically a "
                  "<em>south</em> pole. The wording is the leftover of an old "
                  "decision: the ends of a needle were named for the "
                  "direction they pointed long before anybody knew a field "
                  "was involved, and by the time the physics was understood "
                  "the names were on every chart in Europe and were not going "
                  "to be changed. Read “north pole of a magnet” as “the end "
                  "that seeks north” and the contradiction disappears.",
              ]},
             {"quote": "A compass points at the North Pole.",
              "targets": "MAG-10",
              "body": [
                  "It points along the Earth's field where you are standing, "
                  "which is a different thing. In Britain that happens to be "
                  "within a degree or so of true north at the moment, which "
                  "makes the two easy to confuse; in parts of Canada and New "
                  "Zealand the gap is more than twenty degrees, and following "
                  "a compass bearing there without correcting for it puts you "
                  "kilometres off over a day's walk. The needle is not aiming "
                  "at a place. It is lying along a line, and the line only "
                  "has to reach the pole eventually.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "the-planet-has-a-field",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "The Earth has a magnetic field shaped as though a bar "
                 "magnet were buried inside it, made by moving liquid iron in "
                 "the core rather than by any solid magnet. A compass needle "
                 "is a small magnet lining up with that field. The magnetic "
                 "pole in the Arctic is a magnetic south pole, which is why "
                 "the needle's north-seeking end turns towards it — and it "
                 "sits some way from true north, and moves."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. Rungs take indices 2 and 1. Design
    # put both at 0; her option TEXT and every correction are verbatim and
    # only the ORDER moves — except rung 2's calibration distractor, which is
    # FINISHED under MRB-177. See the module docstring.
    "ladder": {
        "recall": {
            "q": "The north-seeking end of a compass needle turns towards the "
                 "Arctic. What does that make the Earth’s magnetic pole in "
                 "the Arctic?",
            "options": [
                "A magnetic north pole, because it is at the north of the "
                "Earth",
                "A magnetic north pole, because like poles attract over long "
                "distances",
                "A magnetic south pole, because unlike poles attract",
                "Neither — the Earth attracts the needle the way it attracts "
                "a falling ball",
            ],
            "answer": 2,
            "feedback": {
                0: "Where it is on the map does not decide what kind of pole "
                   "it is. Two north poles would repel, and the needle is "
                   "clearly attracted, so it must be a south pole "
                   "magnetically.",
                1: "Like poles repel at every distance. There is no range at "
                   "which the rule reverses.",
                3: "Gravity pulls everything downwards, not northwards, and "
                   "it does not care which end of a needle it is pulling. "
                   "This is a magnetic effect on a magnet.",
            },
            "title": "Rung 1 · Name the pole"},
        "apply": {
            "q": "A walker in Britain takes a bearing from a map printed "
                 "forty years ago and follows it exactly with a modern "
                 "compass. Why might they end up off course?",
            "options": [
                "The Earth’s field has become weaker, so the needle points "
                "less accurately",
                "The magnetic pole has moved since the map was printed, so "
                "the declination on it is out of date",
                # ⚠️ MRB-177 — Design's distractor, FINISHED. Her rung 2's
                # correct option is 19 words against a longest distractor of
                # 13, which is a tell at the ≥4-word threshold. The added
                # clause states the wrong rule completely rather than padding
                # it, and her correction below answers it word for word.
                "Compasses made today are calibrated to a different north "
                "from the ones that were made forty years ago",
                "The map’s grid north has moved, because the squares are "
                "redrawn each edition",
            ],
            "answer": 1,
            "feedback": {
                0: "The field does change strength slowly, but a weaker field "
                   "still points the same way. What has changed is the "
                   "direction, not the reliability.",
                2: "A compass is not calibrated at all — it is a magnet on a "
                   "pivot. Any compass in the same place points the same way.",
                3: "Grid north is fixed by how the map projection is drawn "
                   "and does not wander. It is magnetic north that moves.",
            },
            "title": "Rung 2 · Use the model"},
        "explain": {
            "q": "Explain why a compass works at all, starting from what the "
                 "needle is and ending with what it is lining up with.",
            "field_label": "Your explanation",
            "placeholder": "The needle is…",
            "success": [
                "Says the needle is a small magnet, balanced so that it can "
                "turn freely.",
                "Says a magnet turns until it lies along a magnetic field.",
                "Says the Earth has a magnetic field covering the whole "
                "planet.",
                "Says that field is shaped like the field of a bar magnet "
                "inside the Earth, tilted from the spin axis.",
                "Says the needle settles along the Earth’s field where it is, "
                "which is why it gives the same answer every time.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Aircraft flying polar routes have used the same magnetic "
                 "compass as everyone else, but crews are trained not to rely "
                 "on it above a certain latitude. Explain what goes wrong "
                 "with a compass close to the magnetic pole, and suggest what "
                 "a crew could use instead.",
            "field_label": "Your answer",
            "placeholder": "Close to the pole the field…",
            "success": [
                "Says that close to the pole the Earth’s field points steeply "
                "downwards rather than along the ground.",
                "Says the sideways part of the field is what turns the needle "
                "to a direction, and it becomes very small there.",
                "Says the needle therefore settles slowly, or not to any "
                "useful direction at all, and directly over the pole there is "
                "no horizontal direction to find.",
                "Says the magnetic pole is not at true north anyway, so "
                "bearings near it are badly out even when the needle does "
                "settle.",
                "Suggests something not magnetic — satellite positioning, a "
                "gyroscopic compass, or fixes from the Sun or stars.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A compass needle is a magnet, and a magnet lines up with "
                "whatever field it is in. The needle settles everywhere on "
                "Earth because the whole planet has a field, shaped like the "
                "field of a bar magnet buried inside it and tilted from the "
                "spin axis. Nothing solid down there is magnetised — the core "
                "is far too hot — and the field comes instead from currents "
                "carried by churning liquid iron. Because unlike poles "
                "attract, the magnetic pole in the Arctic is a magnetic south "
                "pole. It does not sit at true north and it moves, so a "
                "bearing worth trusting comes with a declination and a date.",

    "stretch": [
        {"id": "the-field-has-reversed",
         "type": "explainer",
         "text": "The field has swapped ends many times. When lava cools, the "
                 "iron minerals in it set with the field of the moment frozen "
                 "into them, so a stack of old lava flows is a stack of dated "
                 "compasses — and reading down a stack shows the direction "
                 "flipping over and over, hundreds of times, at intervals of "
                 "a few hundred thousand years. The last reversal was about "
                 "780,000 years ago. Nobody can predict the next one, and "
                 "during a reversal the field does not vanish so much as "
                 "become tangled, with several poles at once for a few "
                 "thousand years."},
        {"id": "animals-that-read-it",
         "type": "explainer",
         "text": "Plenty of animals read the field. Robins, sea turtles and "
                 "salmon all navigate by it, and some bacteria grow a chain "
                 "of tiny magnetic crystals inside themselves that swings "
                 "them into line like a compass needle, so that swimming "
                 "forwards takes them down into the mud they need. It is "
                 "worth being careful with the claim, though: exactly which "
                 "organ does the sensing is still argued about for most of "
                 "these species, and it is one of the genuinely unsettled "
                 "questions in biology rather than a finished piece of "
                 "textbook science."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "compass needle",
         "definition": "A small magnet balanced so that it can turn freely. "
                       "It settles along whatever magnetic field it is in, "
                       "which is why it gives the same answer every time in "
                       "the same place."},
        {"term": "angle of dip",
         "definition": "How far the Earth's field runs into the ground rather "
                       "than along it, measured from level. It is zero at the "
                       "equator and ninety degrees at the magnetic pole, "
                       "where the field points straight down."},
        {"term": "declination",
         "definition": "The angle between the way a compass needle points and "
                       "true north. It is different in different countries "
                       "and it changes slowly, so a map for serious "
                       "navigation prints the local value and the date it was "
                       "measured."},
        {"term": "true north",
         "definition": "The end of the axis the Earth spins on, where the "
                       "lines of longitude meet. It has nothing to do with "
                       "magnetism and it does not move — unlike the magnetic "
                       "pole, which does."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Confused about why magnetic north is a south pole?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The Earth's field as evidence for a dynamo in the core, "
                   "and magnetic striping on the sea floor as evidence for "
                   "plate tectonics.",

    "convention_note": "The bench is a teaching model. The Earth's field is "
                       "treated as that of a single bar magnet at the centre, "
                       "lined up with the spin axis, which is the standard "
                       "first model: the angle of dip is then given by a "
                       "fixed relationship between dip and latitude, and the "
                       "sideways pull is what is left of the field once the "
                       "tipping is taken out. A real field is not that tidy. "
                       "The magnetic axis is tilted about eleven degrees from "
                       "the spin axis, so magnetic latitude and geographic "
                       "latitude are not the same and dip measured in the "
                       "field differs from the figure here by several degrees "
                       "in most places; the field also has large local "
                       "variations from the rocks below, and the poles move "
                       "by tens of kilometres a year. Whether a steel object "
                       "beside the compass wins is decided here by a single "
                       "latitude, which is a stand-in for a comparison that "
                       "really depends on how big the steel is and how close "
                       "it sits. No value in tesla is given, because the unit "
                       "is beyond this stage. Angles are rounded to the "
                       "nearest degree and the sideways pull is a relative "
                       "figure with the strongest value on this model set to "
                       "100.",

    "ws": ["measurement", "analysis"],
}
