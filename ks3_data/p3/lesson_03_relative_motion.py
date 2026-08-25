"""P3 L3 — Relative motion (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p3/p3-03-relative-motion.dc.html`.

Her page wins outright. The two trains, the three viewpoints, the four
passes and all four rungs are hers.

── ⚖️ MRB-204 · NO TRIANGLE, AND THIS IS THE ONE THAT MATTERS ────────

The arithmetic on this page is `30 + 30 = 60`, `30 − 30 = 0`,
`25 − 20 = 5` and `30 + 1.5 = 31.5`. **Those are SUMS and
DIFFERENCES.** A triangle encodes `A = B × C`, so a triangle over a
relative speed would teach a relationship that does not exist — the
exact failure MRB-204 was written to prevent.

Design draws none: the word "triangle" appears zero times on her page, and
there is no formula figure of any kind. Checked against her drawing AND
against the arithmetic, twice. This is the lesson where getting MRB-204
wrong would have been easiest, because the unit's first lesson has a
triangle and the habit is to carry it forward.

⚠️ No beam either, and that is also right: a beam is for a SUM that
BALANCES — `total before = total after`. Here the sum is a
combination, not an equality, so neither figure fits and the lesson
carries none. The relationship is taught in words, which is what
`KS3.P.MOT.03` asks for.

── ⚖️ RULED · DIRECTION IN WORDS, NEVER AS A NEGATIVE NUMBER ────────

Design's flag 6 asks for the line to be held, and it is held: the word
"velocity" appears nowhere in this unit, and direction is carried as "the
same way" and "the opposite way" throughout. `KS3.P.MOT.03` names relative
motion and no more; direction-as-sign is P4's to open, and opening it here
would make every rung in this lesson a sign-convention question rather
than a motion one.

── ⚖️ RULED · GALILEAN RELATIVITY, UNNAMED, STAYS ───────────────────

Design's flag 9. Her stretch says no experiment inside a smoothly moving
room can tell you how fast it is going, and that people looked for a
stationary frame for two hundred years and there isn't one. That is true
for uniform motion, and her wording — "smoothly moving" — is what
keeps acceleration out. Kept exactly, including the unnamed attribution:
naming Galileo would add a fact to memorise in place of an idea to hold.

── ⚖️ RULED · THE PLANE-AND-WIND RUNG STAYS ────────────────────────

Design's flag 10 asks whether rung 4 is too hard for KS3. It stays. It is
a SELF-MARKED rung with five criteria, so a student who cannot finish it
loses nothing, and its last criterion — total distance ÷ total time
rather than averaging 300 and 200 — is `FORCE-03` from `p3-01` seen
from the other side. That is the unit closing its own loop, and cutting it
would leave the loop open.

── ⚠️ FOUR RAIL STOPS · `s-think` IS NOT ONE ───────────────────────

    s-hook · s-frames · s-pass · s-ladder

`#s-think` keeps its id — this page's tutor link points at `#s-pass`,
but the anchor is kept for the in-page nav regardless.

── ⚠️ SHELLS ARE MEASURED OFF DESIGN'S CLASS ATTRIBUTE ────────────

    #s-frames  `ks3-block ks3-dark ks3-practical` → `practical`
    #s-pass    `ks3-block`                        → `check`
    #s-think   `ks3-block ks3-misconception`      → `misconception`

── ⚠️ A CAR DOES NOT TURN ROUND WHEN YOU CHANGE VIEWPOINT ─────────

Design's flag 11, kept, and worth writing down because it looks like a
bug: in `relative-frames` a car's drawn ORIENTATION follows its ground
velocity while its MOTION follows its relative velocity. So from car B's
seat, car A can be drawn facing right while drifting left. That is
correct — a car does not physically turn round because you changed
who was watching — and it is exactly the sort of thing a reviewer
flags. It is deliberate, and `r_relative_frames` carries the note so the
next lane does not "fix" it.

── ⚖️ THREE MINTS IN THE `FORCE` FAMILY ──────────────────────────

    FORCE-09  an object has ONE true speed;      `#s-hook`
              a speed from a moving train is
              an illusion
    FORCE-10  two things moving towards each     `#s-think` quote 1
              other pass at the speed of one
    FORCE-11  sitting still in a seat, you are   `#s-think` quote 2
              not moving

Design's proposed table names the first two (as her `FORCE-08`/`FORCE-09`).
`FORCE-11` arrived with her 23 Aug second quote and is a separate belief:
it is about whether "moving" is a property an object HAS, which a student
can hold while adding and subtracting relative speeds perfectly well.
"""

LESSON = {
    "slug":  "relative-motion",
    "title": "Relative motion",
    "discipline": "physics",
    "unit": "Describing motion",
    "family": "MODEL",

    "covers": ["KS3.P.MOT.03"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "motion", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["distance-time-graphs"],
    "assumes": [],
    "references": ["speed"],
    "ks4_links": [],

    "meta_description": "A train pulls alongside yours at the same speed and "
                        "hangs there, motionless, close enough to read over "
                        "someone's shoulder. It is doing 100 km/h. It is "
                        "doing 0 km/h. Both are right.",

    "big_question": "Your train is doing 100 km/h. A second train pulls "
                    "alongside, also doing 100 km/h, and through the window "
                    "it hangs there motionless. How fast is it going?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Relative to what",  "done_when": "committed"},
        {"anchor": "s-frames", "short": "FRAMES",
         "label": "Change who watches", "done_when": "all_three_observers"},
        {"anchor": "s-pass",   "short": "PASSES",
         "label": "Four passes",        "done_when": "all_four_answered"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",     "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "For a few seconds, the other train is parked.",
        "prompt": "Your train is doing 100 km/h. A second train pulls "
                  "alongside, also doing 100 km/h. Through the window it "
                  "hangs there, motionless, close enough to read a book over "
                  "someone's shoulder. Then it edges ahead and slides away.",
        "commit": "Commit. How fast is that train going?",
        "options": [
            "100 km/h — that is what the driver was told",
            "0 km/h — it is not moving, you can see that",
            "200 km/h",
            "The question cannot be answered as it stands",
        ],
        "answer": 3,
        "reveal": "Both of the first two answers are right, and neither is "
                  "complete. 100 km/h measured from the platform. 0 km/h "
                  "measured from your seat. <strong>The question was missing "
                  "the only words that would let it have one answer: "
                  "relative to what?</strong> Every speed in the last two "
                  "lessons was secretly measured against the ground, and "
                  "nobody said so because nobody needed to.",
    },

    "misconceptions": [
        {"id": "FORCE-09",
         "statement": "An object has one true speed; a speed measured from a "
                      "moving train is an illusion.",
         "elicited_by": "s-hook",
         "confronted_by": "relative-frames"},
        {"id": "FORCE-10",
         "statement": "Two things moving towards each other pass at the "
                      "speed of one of them.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
        {"id": "FORCE-11",
         "statement": "Sitting still in a train seat, you are not moving.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every speed in the last two lessons was secretly measured "
                 "against the ground — the corridor, the runway, the "
                 "road. Nobody said so, because nobody needed to. "
                 "<strong>As soon as the thing you measure from is itself "
                 "moving, you do.</strong>"},

        # ── #s-frames · change who watches ───────────────────────────
        {"type": "relative-frames",
         "id": "relative-frames",
         "anchor": "s-frames",
         "eyebrow": "Same road, same two cars, three different answers",
         "heading": "Change who is watching.",
         "prompt": "Nothing about the cars changes when you switch "
                   "viewpoint. Only the numbers do — and one of the "
                   "three viewpoints always makes something look "
                   "stationary.",
         "gate": {
             "prompt": "Commit first. Two cars both travel at 25 m/s in the "
                       "same direction, side by side. What is the speed of "
                       "one measured by the driver of the other?",
             "options": ["0 m/s", "25 m/s", "50 m/s",
                         "It depends which car you ask"],
             "answer": 0,
         },
         "speed_min": 0,
         "speed_max": 30,
         "speed_step": 5,
         "a_start": 25,
         "b_start": 20,
         "observers": [
             {"id": "ground", "label": "From the roadside"},
             {"id": "a",      "label": "From car A"},
             {"id": "b",      "label": "From car B"},
         ],
         "same_direction_label": "Same way",
         "opposite_direction_label": "Opposite ways",
         "start_same_direction": True,
         "readouts": [
             {"id": "a_ground", "label": "A from the roadside"},
             {"id": "b_ground", "label": "B from the roadside"},
             {"id": "b_from_a", "label": "B from car A"},
             {"id": "a_from_b", "label": "A from car B"},
         ],
         "alt": "A road with two cars, drawn from a chosen viewpoint. When a "
                "car is chosen, that car is held still and the road slides "
                "underneath it.",
         "close": "One of the four readings is always zero — whichever "
                  "one belongs to the viewpoint you are sitting in. Nothing "
                  "about either car changed to make it so."},

        {"type": "key-fact", "ref": "relative-to-what"},

        # ── #s-pass · four passes ────────────────────────────────────
        {"type": "passing-speeds",
         "id": "passing-speeds",
         "anchor": "s-pass",
         "eyebrow": "Four passes · decide the direction first",
         "heading": "Same way, subtract. Opposite ways, add.",
         "prompt": "Decide whether the two are going the same way or "
                   "opposite ways before you touch the numbers.",
         # ⚖️ MRB-204 — every `sum` below is an ADDITION or a SUBTRACTION.
         # There is no product anywhere on this page, which is why there is
         # no triangle on it.
         "passes": [
             {"id": "c1", "label": "Pass 1",
              "question": "Two trains both travel at 30 m/s in the same "
                          "direction on parallel tracks, side by side. How "
                          "fast does one pass the other?",
              "options": ["0 m/s", "30 m/s", "60 m/s"],
              "answer": 0,
              "sum": "30 − 30 = 0 m/s",
              "why": "They never pass. Each one sits in the other's window, "
                     "apparently parked, for as long as both hold that "
                     "speed."},
             {"id": "c2", "label": "Pass 2",
              "question": "The same two trains, still 30 m/s each, now "
                          "travelling towards each other. How fast does one "
                          "pass the other?",
              "options": ["0 m/s", "30 m/s", "60 m/s"],
              "answer": 2,
              "sum": "30 + 30 = 60 m/s",
              "why": "Opposite directions add. Nothing has changed about "
                     "either train's own speed — the gap between them "
                     "is closing twice as fast."},
             {"id": "c3", "label": "Pass 3",
              "question": "A car at 25 m/s overtakes a lorry doing 20 m/s. "
                          "How fast does the car pass the lorry?",
              "options": ["5 m/s", "20 m/s", "45 m/s"],
              "answer": 0,
              "sum": "25 − 20 = 5 m/s",
              "why": "Walking pace. A 15 m overtake therefore takes about "
                     "three seconds, which is why it feels like nothing is "
                     "happening."},
             {"id": "c4", "label": "Pass 4",
              "question": "You walk at 1.5 m/s towards the front of a train "
                          "that is doing 30 m/s. How fast are you moving "
                          "relative to the ground?",
              "options": ["28.5 m/s", "30 m/s", "31.5 m/s"],
              "answer": 2,
              "sum": "30 + 1.5 = 31.5 m/s",
              "why": "Your speed relative to the train is 1.5 m/s, and the "
                     "train's speed relative to the ground is 30. Walk "
                     "towards the back instead and it is 28.5."},
         ],
         "close": "Four passes, and not one of them was a multiplication. "
                  "Relative speed is a sum or a difference — which is "
                  "why this lesson has no formula triangle."},

        # ── #s-think · NOT a rail stop ───────────────────────────────
        {"type": "misconception", "id": "think-head-on",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "activities": [
        {"id": "think-head-on",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-10",
         "statements": [
             {"quote": "The other train was doing 100 km/h and mine was "
                       "doing 100 km/h the other way, so it went past me at "
                       "100 km/h.",
              "targets": "FORCE-10",
              "body": [
                  "In one hour your train covers 100 km one way and the "
                  "other covers 100 km the other way, so the gap between "
                  "them closes by 200 km. <strong>From your seat, that train "
                  "is doing 200 km/h.</strong>",
                  "You have felt the difference. A train overtaking yours on "
                  "the next line takes ten seconds to slide past because the "
                  "two speeds nearly cancel. A train coming the other way is "
                  "a bang and a blur, and it is gone — same trains, same "
                  "speeds, and 200 km/h between them instead of 5.",
              ]},
             {"quote": "Sitting still in a train seat, you are not moving.",
              "targets": "FORCE-11",
              "body": [
                  "Relative to the seat, correct. Relative to the platform "
                  "you are doing 100 km/h, relative to the Sun the whole "
                  "train is doing about 30 km every second, and "
                  "<strong>none of those answers is more true than the "
                  "others</strong>. The question is only complete once a "
                  "frame of reference is named — which is why every "
                  "speed in physics quietly carries the words “relative "
                  "to the ground” unless it says otherwise.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "relative-to-what",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Every speed is measured relative to something. Say what it "
                 "is, or the number does not mean anything."},
    ],

    "ladder": {
        "recall": {
            # ⚠️ MRB-278 — across P3's six ladder sets the answer sits at
            # 0, 1, 2 and 3. Feedback keys move with their own option.
            "q": "A cyclist rides at 6 m/s. A bus going the same way "
                 "overtakes at 14 m/s. What is the bus's speed relative to "
                 "the cyclist?",
            "options": ["20 m/s", "14 m/s", "6 m/s", "8 m/s"],
            "answer": 3,
            "feedback": {
                0: "That is 14 + 6. Adding is for objects going opposite "
                   "ways; these two are going the same way.",
                1: "That is the bus relative to the ground. The question "
                   "asks what the cyclist sees, and the cyclist is moving "
                   "too.",
                2: "That is the cyclist relative to the ground, which is not "
                   "what was asked.",
            }},
        "apply": {
            "q": "A passenger sits still in her seat on a train travelling "
                 "at 30 m/s. Which statement is true?",
            # ⚠️ MRB-177 — Design's correct option runs to nineteen words
            # against a longest distractor of fourteen, which the gate reads
            # as a length tell: the longest option is the answer and a
            # student need not read any of them. Her four CLAIMS are
            # unchanged and in her order; the weights are evened so the set
            # is decided by reading. Engine policy, not a science departure
            # — see DEPARTURES-P3.md.
            "options": [
                "She is not really moving at all; only the train is moving",
                "She is doing 30 m/s from the platform and 0 m/s from her "
                "seat",
                "She is doing 30 m/s, full stop; the train's viewpoint is "
                "just an illusion",
                "She is doing 30 m/s relative to the train she is sitting "
                "in",
            ],
            "answer": 1,
            "feedback": {
                0: "Relative to the ground she covers 30 m every second, "
                   "seat and all. “Really” is doing no work in that "
                   "sentence.",
                2: "The train's viewpoint is as good as the ground's. In it "
                   "she is stationary — which is why she can read a "
                   "book.",
                3: "Relative to the train she is not moving at all. 30 m/s "
                   "is her speed relative to the ground.",
            }},
        "explain": {
            "q": "Two trains passing in opposite directions are gone in a "
                 "second, but a train overtaking yours on the next track "
                 "seems to take forever. Explain both, using relative speed "
                 "and numbers of your own choosing.",
            "field_label": "Your explanation",
            "placeholder": "Say the two trains each travel at…",
            "success": [
                "Gives a ground speed for each train, and keeps them "
                "similar.",
                "Adds the two speeds for the head-on case and gives the "
                "number.",
                "Subtracts the two speeds for the overtaking case and gives "
                "the number.",
                "Says the time it takes to pass depends on the relative "
                "speed, not on either ground speed.",
                "Says neither train's own speed changed between the two "
                "situations.",
            ]},
        "produce": {
            "q": "A plane flies at 250 m/s relative to the air. It flies "
                 "900 km east with a 50 m/s wind behind it, then straight "
                 "back west against the same wind. Work out its speed "
                 "relative to the ground on each leg, and explain why the "
                 "round trip takes longer than it would with no wind at all.",
            "field_label": "Your answer",
            "placeholder": "Going east, relative to the ground…",
            "success": [
                "Gives 250 + 50 = 300 m/s for the leg with the wind.",
                "Gives 250 − 50 = 200 m/s for the leg against it.",
                "Says the speed is now being measured relative to the air "
                "first, and then relative to the ground.",
                "Says the slow leg takes more extra time than the fast leg "
                "saves, because the slow leg lasts longer.",
                "Uses total distance ÷ total time for the round trip "
                "rather than averaging 300 and 200.",
            ]},
    },

    "key_note": "Every speed is relative to something, and for ordinary "
                "questions that something is the ground. Two objects going "
                "the same way: subtract. Two objects going opposite ways: "
                "add. Changing who measures changes the number, never the "
                "object.",

    "stretch": [
        {"id": "no-stationary-thing",
         "type": "explainer",
         "text": "Sitting still, you are travelling about 30 km every second "
                 "around the Sun, and you cannot feel any of it. That is not "
                 "a trick of the senses: <strong>no experiment done inside a "
                 "smoothly moving room can tell you how fast the room is "
                 "going, or whether it is moving at all.</strong> Physicists "
                 "spent two hundred years hunting for the one truly "
                 "stationary thing to measure everything else against. There "
                 "isn't one."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "relative speed",
         "definition": "The speed of one object measured from another. Same "
                       "way: subtract. Opposite ways: add."},
        {"term": "frame of reference",
         "definition": "The thing a speed is measured against. Usually the "
                       "ground, and usually not said out loud."},
        {"term": "stationary",
         "definition": "Not moving — relative to something. Nothing is "
                       "stationary in every frame at once."},
    ],

    "tutor": {
        "anchor": "s-pass",
        "prompt": "Ask Mr Badmus AI",
        "body": "Not sure when to add and when to subtract?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Vectors and resultant velocity, and — much later "
                   "— the reason light refuses to play by these rules.",

    "ws": ["analysis-and-evaluation"],
}
