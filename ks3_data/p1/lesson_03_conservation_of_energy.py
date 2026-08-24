"""p1-03 — *Conservation of energy*.

Ported from Claude Design's `p1-03-conservation-of-energy.dc.html`.

── WHAT THIS LESSON OWNS ───────────────────────────────────────────────

`KS3.P.CIS.01` and `KS3.P.CIS.03`. The `CIS.03` allocation — use physical
processes and mechanisms, RATHER THAN ENERGY, to explain the intermediate
steps — sits here rather than on its own because it only becomes a
reasonable instruction once a student knows the total never changes: if
energy is conserved it cannot have been consumed, and a quantity that is
never consumed can never be why anything happened. Conservation is the
premise and "name the mechanism" is the conclusion, so they are one lesson.
Design draws it that way, with `#s-think` doing exactly that work.

── ⚖️ MRB-204 · THIS PAGE CARRIES A BEAM, AND IT IS A BEAM ON PURPOSE ──

`#s-balance` is the unit's first formula block and Design argues the choice
in her own prose: *"Conservation is a balance, not a triangle."* The
arithmetic under it is a SUM — her four splits are

    120 = 120 +   0 +   0     just released
    120 =  62 +  55 +   3     halfway down
    120 =   0 + 114 +   6     at the bottom
    120 =   0 +   0 + 120     long after it stops

— and all four total 120, checked. A triangle encodes `A = B × C`; drawn
over a sum it teaches a relationship that does not exist, which is the
`c2-06` precedent NOTES-C2 §8 flag 14 recorded for conservation of mass.
BEAM here, and the beam stays level in every configuration.

⚠️ Arrows inside the block are SVG. Typed arrows stay in prose.

── ⚖️ MRB-278 · WHERE THE CORRECT ANSWER SITS ─────────────────────────

`p1-01` took indices 0 and 2, `p1-02` took 1 and 3. This lesson takes
**0 and 2**, which is the plan that lands 4/4/4/4 across the unit's sixteen
marked rungs. Design puts the correct option first in both; her option text
and every correction are verbatim, and only the button order moves.

── ⚑ MISCONCEPTION · `ENER-12`, AND THE LOCK WITH `PART-05` ───────────

Design's `NOTES-P1.md` §1 calls this `ENERGY-04` and locks it to `PART-05`:
both are the belief that a quantity stops existing when it stops being
visible. The lock stands — separate ids because the confrontations genuinely
differ, a balance for mass and a thermometer for energy, but neither
`c1-03` nor `p1-03` may drop its confrontation on the grounds that the other
covers it. Same shape as the `CELL-08` lock.

The id is `ENER-12`, not `ENERGY-04`: the register's prefix table forbids
opening `ENERGY`, and the register already anticipates `ENER-12` for this
lesson by name.

`#s-think` names the `c1-03` sealed-bag result explicitly and calls the two
"the same belief in different clothes". That cross-reference is deliberate
and load-bearing — it is the only place in the key stage where a physics
lesson and a chemistry lesson are said to be confronting one belief.
"""

LESSON = {
    "slug":  "conservation-of-energy",
    "title": "Conservation of energy",
    "discipline": "physics",
    "unit": "Energy transfers",
    "family": "MODEL",

    "covers": ["KS3.P.CIS.01", "KS3.P.CIS.03"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 55,

    "requires": ["energy-transfers-before-and-after"],
    "assumes": ["changes-of-state"],
    "references": [],
    "ks4_links": [],

    "meta_description": "A pendulum swings lower every time and finally "
                        "hangs still. Energy is supposed to be conserved — "
                        "so what happened? Keep score on all four stores "
                        "and watch the total never move.",

    "big_question": "A pendulum comes back almost as high, but only almost, "
                    "and after a few hundred swings it hangs straight down. "
                    "Energy is supposed to be conserved. What happened?",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "The swing that stops",  "done_when": "committed"},
        {"anchor": "s-bench",   "short": "TOTAL",
         "label": "Running total",         "done_when": "run_to_rest_or_hidden"},
        {"anchor": "s-balance", "short": "BALANCE",
         "label": "Balance, not triangle", "done_when": "split_moved"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The swing that gives up.",
        "prompt": "Pull a pendulum to one side and let go. It comes back "
                  "almost as high — but only almost. Every swing is a "
                  "little lower than the last, and after a few hundred "
                  "swings it is hanging straight down, motionless.",
        "commit": "Commit. Energy is supposed to be conserved. What "
                  "happened?",
        "options": [
            "The energy was gradually destroyed by friction",
            "It moved into the air and the pivot as a tiny temperature rise",
            "The pendulum used up its energy swinging",
            "Conservation of energy only works for perfect systems",
        ],
        "reveal": "Nothing happened to the total. Every joule that left the "
                  "swinging is now in the air of the room and the pivot of "
                  "the pendulum, as a rise in temperature far too small to "
                  "feel. <strong>The pendulum stopped; the energy did "
                  "not.</strong> This lesson gives you an instrument that "
                  "keeps score, so you can watch that being true instead of "
                  "taking it on trust.",
    },

    "misconceptions": [
        {"id": "ENER-12",
         "statement": "The car has stopped, so it has run out of energy — a "
                      "quantity that stops being visible has stopped "
                      "existing.",
         "elicited_by": "s-hook",
         "confronted_by": "running-total"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Conservation of energy is the most tested claim in physics "
                 "and it has never once failed. It is not a rule about how "
                 "machines behave, or an ideal that real systems fall short "
                 "of — <strong>it is exact, every time</strong>, with no "
                 "exceptions found in two hundred years of looking. What "
                 "makes it feel false is that the stores energy ends up in "
                 "are usually invisible. So the instrument below shows them "
                 "all."},

        # ── #s-bench — bare `ks3-block` on Design's markup → `check`.
        {"type": "running-total", "id": "running-total",
         "anchor": "s-bench",
         "demand": "investigate",
         "targets": "ENER-12",
         "eyebrow": "The running total · keep score through the whole swing",
         # ⚠️ HER HEADING SAYS "Four stores" AND HER BENCH DRAWS THREE.
         # Measured off her canvas: `seg(grav,…) seg(kin,…) seg(th,…)` —
         # GRAV, KIN, THERMAL, and a Total readout beside them. Her NOTES §3
         # repeats the four. A student counts three bars and reads four.
         # Corrected to three; see DEPARTURES-P1.md row 3.
         "heading": "Three stores. One total that never moves.",
         "prompt": "Release the pendulum and watch the top of the bar rather "
                   "than the bob. Then try hiding the thermal store, and "
                   "see what the law looks like without it.",
         "total": 120,
         "gate": {
             "prompt": "Commit first. At the very bottom of the swing, which "
                       "store holds the most?",
             "options": [
                 "Gravitational — it is closest to the Earth",
                 "Kinetic — it is moving fastest there",
                 "They are equal at the bottom",
                 "Elastic — the string is under most tension",
             ],
         },
         # ⚖️ Design's science flag 7: the hide-thermal control DELIBERATELY
         # makes the law look false, and that is the confrontation of
         # ENER-12. It must not be removed as a "confusing" control.
         # Flag 8: friction-off is physically impossible and is labelled as
         # idealised rather than presented as a real pendulum.
         "controls": [
             # ⚠️ NO `alt2`. It was authored here as "Continue" and read by
             # nothing — `wireRunningTotal` derives that third label from
             # state (`everRan`) rather than from the payload. ks3_key_audit
             # caught it: "a key with no read site is content that never
             # reaches a student."
             {"id": "run",      "label": "Release it", "alt": "Pause"},
             {"id": "reset",    "label": "Pull it back and release"},
             {"id": "friction", "label": "Switch friction off",
              "alt": "Switch friction on"},
             {"id": "hide",     "label": "Hide the thermal store",
              "alt": "Show the thermal store"},
         ],
         "readouts": [
             {"id": "grav",  "label": "Gravitational"},
             {"id": "kin",   "label": "Kinetic"},
             {"id": "therm", "label": "Thermal, surroundings", "accent": True},
             {"id": "total", "label": "Total"},
         ],
         "notes": {
             "rest":     "Held at 120 J, all of it gravitational. Press "
                         "start and keep your eye on the top of the bar "
                         "rather than the pendulum.",
             "running":  "Watch the two lower blocks trade places twice a "
                         "swing while the orange one creeps up and never "
                         "falls. Nothing takes the total past the line, and "
                         "nothing lets it drop below.",
             "stopped":  "Stopped — and the bar still reaches the top line. "
                         "Every joule that was in the swinging is now in "
                         "the thermal store of the air and the pivot. The "
                         "pendulum ran down; the total did not.",
             "no_friction": "Friction off. The swing never dies down and "
                            "nothing enters the thermal store, so "
                            "gravitational and kinetic simply trade back "
                            "and forth forever. No real pendulum does this "
                            "— but it makes the trade visible without the "
                            "complication.",
             "hidden":   "With the thermal store hidden, the bar no longer "
                         "reaches the total line and the law looks false. "
                         "This is exactly the mistake behind “the "
                         "energy was lost” — the store is real, it "
                         "is just not one you would have thought to look "
                         "at.",
         }},

        {"type": "key-fact", "id": "total-is-fixed",
         "ground": "card",
         "text": "Energy is never created and never destroyed. In a closed "
                 "system the total before a change equals the total after; "
                 "all that alters is which stores are holding it."},

        # ── #s-balance — bare `ks3-block` → `check`. THE FORMULA BLOCK.
        {"type": "conservation-beam", "id": "conservation-beam",
         "anchor": "s-balance",
         "demand": "explain",
         "eyebrow": "Writing it down · the shape of the relationship matters",
         "heading": "Conservation is a balance, not a triangle",
         "prompt": "You will meet formula triangles in this course and they "
                   "are genuinely useful — but only for a relationship "
                   "built from multiplying and dividing. Conservation of "
                   "energy is not one of those. It is a sum on each side of "
                   "an equals sign, and a triangle drawn over it would "
                   "teach you a relationship that does not exist.",
         "control_label": "Move energy between the stores on the right — "
                          "the beam stays level",
         "total": 120,
         "alt": "A level balance beam. Left pan: one 120 joule block. Right "
                "pan: the same 120 joules split between gravitational, "
                "kinetic and thermal stores. The beam stays level in every "
                "configuration.",
         "splits": [
             {"id": "b1", "label": "Just released",
              "grav": 120, "kin": 0, "therm": 0,
              "note": "All of it in the gravitational store, at the top of "
                      "the swing. The beam is level because 120 = 120 + 0 "
                      "+ 0."},
             {"id": "b2", "label": "Halfway down",
              "grav": 62, "kin": 55, "therm": 3,
              "note": "Split between two stores, with a few joules already "
                      "in the air. Still level: 62 + 55 + 3 is still 120. "
                      "Notice the beam does not care how many stores you "
                      "use."},
             {"id": "b3", "label": "At the bottom",
              "grav": 0, "kin": 114, "therm": 6,
              "note": "Gravitational empty, kinetic nearly full. This is "
                      "the moment most people get wrong — the pendulum is "
                      "lowest and fastest at the same instant."},
             {"id": "b4", "label": "Long after it stops",
              "grav": 0, "kin": 0, "therm": 120,
              "note": "Everything in the thermal store of the room. The "
                      "pendulum is motionless and the sum is still exactly "
                      "120. Nothing about the beam has changed — which is "
                      "the whole point of drawing it as a balance rather "
                      "than a triangle."},
         ]},

        # ── #s-think — `ks3-block ks3-misconception` → `misconception`.
        # A REFERENCE; the payload is in `activities[]`. Authored inline the
        # section renders NOTHING and `#s-think` lands on no element.
        # ⚠️ A SECTION, NOT A RAIL STOP, on this page.
        {"type": "misconception", "id": "think-run-out",
         "anchor": "s-think", "targets": "ENER-12"},

        {"type": "key-fact", "id": "dissipated-not-lost",
         "ground": "card",
         "text": "A machine that seems to lose energy has dissipated it "
                 "into thermal stores. “Lost” names your "
                 "attention, not the energy."},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "activities": [
        # ⊕ #s-think — one "Think again", two wrong ideas, the second behind
        # the amber divider. The `c1-03` cross-reference in the first body is
        # deliberate and load-bearing: it is the only place in the key stage
        # where a physics lesson and a chemistry lesson are said to be
        # confronting one belief (`ENER-12` and `PART-05`).
        {"id": "think-run-out",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-12",
         "statements": [
             {"targets": "ENER-12",
              "quote": "The car has stopped, so it has run out of energy.",
              "body": [
                  "First: a stopped car has not run out of anything. Its "
                  "kinetic store is empty, which is a different statement — "
                  "its fuel tank may be full, and the brake discs are now "
                  "hot enough to boil water. Second, and this is the deeper "
                  "one: “ran out” treats energy as a supply "
                  "that gets consumed. It is not. It is a number that "
                  "moved.",
                  "You have met this exact belief before wearing different "
                  "clothes. When a sealed bag of ice melted, the mass did "
                  "not change — and the temptation was to say some of it "
                  "had gone. Same instinct, same error: a quantity stops "
                  "being <em>visible</em> and we conclude it has stopped "
                  "<em>existing</em>. A balance answered it for mass. A "
                  "thermometer on the brake discs answers it for energy.",
              ]},
             {"quote": "Efficient machines conserve energy and wasteful ones "
                       "do not.",
              "body": [
                  "Both conserve it exactly. A 20% efficient petrol engine "
                  "and a 90% efficient electric motor obey the same law to "
                  "the same precision — the difference is where the energy "
                  "ends up, not how much of it survives. Efficiency is the "
                  "fraction that arrives in the store you wanted; the rest "
                  "still exists, warming the engine, the road and the air. "
                  "Conservation is not something a machine can be good or "
                  "bad at.",
              ]},
         ]},
    ],

    "figures": [],
    "key_facts": [],

    "ladder": {
        "recall": {
            "q": "Complete the law: energy cannot be created or destroyed, "
                 "only…",
            # MRB-278: correct at index 0 (Design's own order here).
            "options": [
                "transferred between stores",
                "used up by machines",
                "turned into heat and lost",
                "made more efficient",
            ],
            "answer": 0,
            "feedback": {
                1: "Machines transfer energy. Nothing uses it up — that is "
                   "exactly what the law forbids.",
                2: "The first half is often true and the word "
                   "“lost” ruins it. It goes into a thermal "
                   "store you can point at.",
                3: "Efficiency describes how the energy is shared out "
                   "afterwards, not what happens to the total.",
            }},
        "apply": {
            "q": "A pendulum swings until it hangs still. What is true of "
                 "the total energy at the end compared with the start?",
            # MRB-278: correct at index 2.
            # ⚠️ MRB-177: her set runs 15w against 7/7/9 — gap 6, ratio 1.67
            # — and trips BOTH limbs of the gate. Fixed AT THE DISTRACTOR per
            # MRB-177's ruling and the c10 precedent, never by trimming her
            # correct answer. Now 13/13/15/14: gap 1, ratio 1.07. Every one
            # of her three corrections still answers its re-worded distractor,
            # and no claim has changed.
            "options": [
                "It is less, because friction gradually destroyed some of "
                "it on every swing",
                "It is zero now, because nothing is moving and the pendulum "
                "hangs still",
                "It is exactly the same — it is just all in the thermal "
                "store now",
                "It is less, but only by the tiny amount that friction "
                "managed to remove",
            ],
            "answer": 2,
            "feedback": {
                0: "Friction moves energy into thermal stores. It has no "
                   "mechanism for destroying it.",
                1: "Nothing moving means the kinetic store is empty. The "
                   "total is not the kinetic store.",
                3: "Not by any amount. The sum is exact, not approximately "
                   "right.",
            }},
        "explain": {
            "q": "A skateboarder drops into a half-pipe from the top of one "
                 "side and rises up the other. They never quite reach the "
                 "height they started from. Explain what has happened to "
                 "the energy, and why the law of conservation is not "
                 "broken.",
            "field_label": "Your explanation",
            "placeholder": "At the start all the energy is in…",
            "success": [
                "Says the energy starts in the gravitational store, at the "
                "highest point.",
                "Says it fills the kinetic store on the way down, and the "
                "gravitational store again on the way up.",
                "Says friction and air resistance move some of it into "
                "thermal stores.",
                "Names where the thermal stores are — the wheels, the ramp, "
                "the air.",
                "Says the total is unchanged, so a lower finish means "
                "energy relocated, not energy destroyed.",
            ]},
        "produce": {
            "q": "Someone advertises a machine with magnets that, once "
                 "started, turns forever and powers a light with no fuel. "
                 "Using conservation of energy, explain why it cannot work "
                 "— and say what you would measure to test it.",
            "field_label": "Your answer",
            "placeholder": "For the light to stay on, energy must be…",
            "success": [
                "Says the light requires energy to be supplied "
                "continuously.",
                "Says that energy must come from some store, because none "
                "can be created.",
                "Says friction and air resistance always move energy into "
                "thermal stores, so the machine must run down.",
                "Identifies that the claim requires a store nobody can name "
                "— the giveaway.",
                "Names a measurement: run it in a sealed insulated box and "
                "check whether anything gets warmer, or simply time how "
                "long it runs.",
            ]},
    },

    "key_note": "The total is fixed. A store emptying is never a store "
                "disappearing — find where it went. “Stopped” "
                "and “out of energy” are different statements, "
                "and only the first one is ever true.",

    "stretch": [
        # ⚖️ Design's science flag 9 asked for the dates to be verified.
        # Checked: Pauli's letter is 1930, the neutrino was detected by
        # Cowan and Reines in 1956, and the gap is twenty-six years.
        {"type": "explainer", "id": "the-neutrino-shortfall",
         "text": "Twice in history the sum has looked broken, and both "
                 "times the gap turned out to be a discovery rather than a "
                 "mistake. In the 1920s energy appeared to go missing "
                 "during a particular kind of radioactive decay — always a "
                 "bit short, always by a varying amount. Rather than "
                 "abandon the sum, Wolfgang Pauli proposed in 1930 that an "
                 "undetected particle was carrying the difference away, an "
                 "idea so hard to test he apologised for it. The neutrino "
                 "was finally detected in 1956, twenty-six years later, and "
                 "the sum balanced exactly. <strong>Conservation of energy "
                 "has been trusted enough to predict a new particle from "
                 "nothing but a shortfall in the arithmetic</strong> — that "
                 "is how strong the evidence for it is."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "conservation of energy",
         "definition": "The rule that the total energy before a change is "
                       "exactly equal to the total after it. No exception "
                       "has ever been found."},
        {"term": "closed system",
         "definition": "Everything involved in a change, drawn widely "
                       "enough that no energy crosses the boundary. The "
                       "total inside it is fixed."},
        {"term": "dissipated",
         "definition": "Spread out into thermal stores in the surroundings, "
                       "too thinly to be useful. Dissipated energy still "
                       "exists and still counts in the total."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why a stopped pendulum has not run "
                      "out of energy?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Closed systems and dissipation quantified — efficiency "
                   "as a calculated fraction, and the idea that dissipated "
                   "energy is no longer useful even though it is still "
                   "there.",

    "ws": ["analysis-and-evaluation", "scientific-attitudes"],
}
