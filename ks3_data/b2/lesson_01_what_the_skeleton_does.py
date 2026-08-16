"""B2 L1 — What the skeleton does (SYSTEM).

Authored against Design's approved page,
`docs/ks3/design-reference/b2/b2-01-what-the-skeleton-does.dc.html` (727 lines),
and its measured specification, `docs/ks3/b2-inventory/PAYLOAD-MAP.md` §1.
Schema per architecture.md §4.8 as amended by §4.8.1 and §4.8.2.

Every student-facing string below is byte-identical to the approved page. The
named constants (`PARTS`, `JOBS`, `SORT`, `RUNGS`, `SELF_RUNGS`, `RAIL`) were
lifted with `node tools/extract_design_payload.js`; the strings that live
INSIDE `renderVals()` — the hook options, the think options, the progress
formats, the button labels and the three switch hints — were lifted from the
line ranges the payload map records, because a lift that copies only the
top-level constants loses between 240 and 900 words per lesson.

── Two things this record does that Design's page does not ──────────────

1. **`#s-think` is a rail stop that ticks** (contract R1). B1's `confrontation`
   kind deliberately emits no completion contract, because on B1's pages
   `#s-think` is static markup with nothing to complete. Here it asks for a
   commitment and then reveals, which is a `predict` — and MRB-208 says the
   rail is completion-based. So it is authored as `predict`, and the rail's
   fourth stop is reachable exactly as Design's own tick condition
   (`thinkChoice !== null`) says it should be.

2. **The `#s-think` reveal is TWO paragraphs.** Design draws two `<p>`s and the
   generic shell carried one `reveal` string; `reveal` accepts a list now, and
   the list form takes Design's own card-on-ink panel rather than the accent
   tint a one-line reveal takes.

Nothing else diverges. No `figures`: NOTES flag 17 rules that no anatomical
diagram appears anywhere in this unit, and the page draws none.
"""

# ── the four jobs, offered against all six sorted items ─────────────────
# Shared across every item, which is what makes b2-01's sorter the "shared
# category set" case; b2-02 and b2-03 offer a per-item set instead.
JOBS = [
    {"id": "support", "label": "Support"},
    {"id": "protect", "label": "Protection"},
    {"id": "move", "label": "Movement"},
    {"id": "blood", "label": "Making blood cells"},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 71 character for character. Slugs are
    # permanent (§8.4) and are the join for scheme-of-work rows, progress
    # records and every `requires` edge.
    "slug":        "what-the-skeleton-does",
    "title":       "What the skeleton does",
    "discipline":  "biology",
    "unit":        "movement-skeleton-and-muscles",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚑ `KS3.B.SKEL.01a`, not the parent. The bullet is compound — it names a
    # structure AND four functions — and `joints` needs the structure half or
    # it owns nothing at all. See `ks3_data/substatements.py` and the flag in
    # `ks3_data/biology_b2_movement.py`; this is Mide's to confirm.
    "covers":      ["KS3.B.SKEL.01a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    # `requires` is non-empty, so the endmatter's first card renders as a link
    # to B1's levels-of-organisation — which is exactly what the approved page
    # draws (line 319).
    "requires":    ["levels-of-organisation"],
    "assumes":     [],
    # ⊕ The endmatter's MIDDLE card. Design heads it "Next in this unit" and
    # points FORWARD, where the generator's fixed heading was "Connects to".
    # A same-unit pointer is a bare slug (§4.6's dict form stays required the
    # moment a reference crosses a unit boundary).
    "references":  ["joints"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A broken finger is an inconvenience. A broken rib makes "
                    "every breath hurt. Same material — so what makes the "
                    "difference?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, from the page's own RAIL constant (lines 348–354). `done_when`
    # names the condition the page's own tick function checks (lines 555–562):
    # `#s-switch` ticks when all four parts are SWITCHED OFF, not merely
    # predicted, and `#s-sort` when all six are decided.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Two broken bones",
         "done_when": "committed"},
        {"anchor": "s-switch", "short": "SWITCH", "label": "Switch a part off",
         "done_when": "all_parts_opened"},
        {"anchor": "s-sort",   "short": "SORT",   "label": "Which job is this",
         "done_when": "all_items_decided"},
        {"anchor": "s-think",  "short": "THINK",  "label": "Living or dead",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, deliberately (R3:
    # only the ladder marks). Page lines 82–104; options at 584–587.
    "phenomenon": {
        "kind": "narrative",
        "title": "Two broken bones, two completely different disasters.",
        "prompt": "Break a finger and you tape it to the next one and carry "
                  "on. Break a femur and you are in hospital, off your feet "
                  "for months, and at real risk from a blood clot. Both are "
                  "bone. Both heal.",
        "commit": "What actually decides how serious a broken bone is?",
        "options": [
            "How big the bone is",
            "How much it hurts",
            "What job that bone was doing, and what depended on it",
            "How long it takes to heal",
        ],
        "reveal": "Not the size, and not the pain. What matters is the job "
                  "that bone was doing, and how many other things were relying "
                  "on it. The skeleton is doing four jobs at once, and they "
                  "fail in four different ways.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ BODY-01's statement here is the PAGE's line (line 208), not the
    # register's paraphrase — the two differ, and the page's is the one a
    # student reads. r_confrontation resolves the quote from this list.
    "misconceptions": [
        {"id": "BODY-01",
         "statement": "Bones are dead. They are the hard bits left over — "
                      "like the frame of a tent.",
         "elicited_by": "bones-are-dead",
         "confronted_by": "bones-are-dead"},
        {"id": "BODY-02",
         "statement": "The skeleton’s job is holding you up; the other things "
                      "bones do are extras.",
         "elicited_by": "switch-off-chains",
         "confronted_by": "switch-off-chains"},
        {"id": "BODY-03",
         "statement": "How bad a break is depends on how big the bone is.",
         "elicited_by": "hook",
         "confronted_by": "hook"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    # Eight blocks → the page's eight rendered lesson sections plus the layer
    # and the end matter. The KEY FACT box is the one block with no anchor:
    # Design draws it as an unclassed, un-id'd <div> between two sections.
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "The way to find out what a part does is not to label it. It "
                 "is to switch it off and follow what breaks next."},

        # #s-switch — the flagship. A LIGHT `.ks3-block` (→ `check`), with the
        # ink-dark chain panel INSIDE it and only after the reveal. That is the
        # measured difference from `sabotage`, whose whole shell is dark.
        {"type": "system-switch", "id": "switch-off-chains", "anchor": "s-switch",
         "eyebrow": "Your turn · four parts, switched off",
         "heading": "Take one part away and follow the damage",
         "head_counter": {"format": "{n} of 4 parts switched off", "total": 4},
         "demand": "predict",
         "targets": "BODY-02",
         "labels": {
             "switch": "Switch this part off",
             "switched": "Switched off",
             "hint_locked": "Commit to a prediction first.",
             "hint_ready": "Ready.",
             "hint_done": "Now try another part.",
         },
         # ⚠️ The chains DO NOT ALL CLIMB, and that is the data rather than a
         # rendering accident: skull runs Cell→Tissue→Organ→Organism, ribs
         # Organ→Organ→Tissue→Cell, femur Tissue→Organ→Organism→Cell, marrow
         # Cell→Tissue→Organ→Cell. The level chip is a rendering of the level
         # string, never a claim about direction — which is why the chip's
         # colour is keyed on the word "Cell" and not on the row's position.
         "parts": [
             {
              "id": "skull",
              "tab": "The skull",
              "name": "The skull",
              "does": "Eight curved plates, fused into a single box around the brain, with holes only where nerves and blood vessels have to pass through.",
              "prompt": "Switch it off. What is the first thing that goes wrong?",
              "title": "Skull switched off",
              "close": "Protection is the only job on this list where nothing happens at all until something goes wrong — and then everything does.",
              "options": [
                  "Nothing much — the brain floats in fluid anyway",
                  "A knock that skin would survive now damages brain tissue",
                  "You could not hold your head upright",
                  "You would not be able to see",
              ],
              "chain": [
                  {"level": "Cell",
                   "text": "Nerve cells are torn or crushed by an impact that the skin above them survives easily."},
                  {"level": "Tissue",
                   "text": "Unlike skin, nerve tissue does not replace what it loses. The damaged patch stops carrying signals for good."},
                  {"level": "Organ",
                   "text": "Whatever that region of the brain controlled — a hand, speech, balance, breathing — is weakened or gone."},
                  {"level": "Organism",
                   "text": "A bump that would have been a bruise is now permanent, and it can be fatal."},
              ]},
             {
              "id": "ribs",
              "tab": "The ribcage",
              "name": "The ribcage",
              "does": "Twelve pairs of curved bones hinged at the spine, with muscles slung between them. It is the only reason the space inside your chest can be made bigger.",
              "prompt": "Switch it off. What is the first thing that goes wrong?",
              "title": "Ribcage switched off",
              "close": "This one is fast. Minutes, not months. The ribcage is doing protection and movement at the same time, and it is the movement you die without.",
              "options": [
                  "You would breathe normally using the diaphragm",
                  "The heart would be exposed, but breathing would carry on",
                  "Nothing can lift the chest wall, so air stops coming in",
                  "You would simply breathe faster",
              ],
              "chain": [
                  {"level": "Organ",
                   "text": "Nothing lifts and swings the chest wall outwards, so the volume of the chest cannot be increased."},
                  {"level": "Organ",
                   "text": "Air only moves into the lungs because that volume increases. It stops moving in."},
                  {"level": "Tissue",
                   "text": "No fresh oxygen reaches the blood at the alveoli, so the blood leaving the lungs is no better than the blood arriving."},
                  {"level": "Cell",
                   "text": "Within minutes every cell in the body — brain cells first — has no oxygen for respiration."},
              ]},
             {
              "id": "femur",
              "tab": "Femur and hip",
              "name": "The femur and hip",
              "does": "The thigh bone is the longest and strongest bone you have. Standing still, it carries the entire weight of everything above it into the ground.",
              "prompt": "Switch it off. What is the first thing that goes wrong?",
              "title": "Femur and hip switched off",
              "close": "Support and movement are the same job seen from two sides: a rigid bar to hold you up, and a rigid bar for muscles to pull on.",
              "options": [
                  "You would sit down more often",
                  "Leg muscles contract, but with nothing rigid to pull on, nothing moves",
                  "You would be shorter but otherwise fine",
                  "It would hurt, but you could still walk on it",
              ],
              "chain": [
                  {"level": "Tissue",
                   "text": "The big muscles of the leg still contract and shorten. There is nothing rigid for them to pull against."},
                  {"level": "Organ",
                   "text": "The leg cannot straighten or take weight, so it cannot hold up the body above it."},
                  {"level": "Organism",
                   "text": "No standing, no walking, no carrying. Nothing can be reached, and nothing can be escaped from."},
                  {"level": "Cell",
                   "text": "The route to food is gone, and within days the cells that depend on it have nothing to respire."},
              ]},
             {
              "id": "marrow",
              "tab": "The marrow inside",
              "name": "The marrow inside the bones",
              "does": "The soft tissue in the hollow middle of the big bones. It makes about two million new red blood cells every second, for your whole life.",
              "prompt": "Switch it off. What is the first thing that goes wrong?",
              "title": "Marrow switched off",
              "close": "Slow, invisible, and it ends up in exactly the same place as the ribcage. This is the job nobody guesses, because it is the only one you cannot see from the outside.",
              "options": [
                  "Nothing — the blood you have already is permanent",
                  "You would run out of blood immediately",
                  "No new red blood cells are made, and the old ones wear out",
                  "Your bones would become hollow",
              ],
              "chain": [
                  {"level": "Cell",
                   "text": "No new red blood cells are made anywhere in the body."},
                  {"level": "Tissue",
                   "text": "The red blood cells you already have wear out and are removed after about four months. Nothing replaces them."},
                  {"level": "Organ",
                   "text": "The blood carries less and less oxygen with every week that passes."},
                  {"level": "Cell",
                   "text": "Every cell in the body is short of the oxygen it needs to respire, and the whole organism slows down and fails."},
              ]},
         ],
         "close_all": "Four parts, four different routes, one destination. The "
                      "ribcage kills in minutes and the marrow takes months, "
                      "and both end in exactly the same place: cells with no "
                      "oxygen to respire with."},

        # the KEY FACT box — a direct child of .ks3-lesson, between two
        # sections. `card` ground is B2's unit-wide choice and differs from the
        # shipped `band` default, which is authorable. The 6px shadow / 25px
        # body / 22px 26px padding Design draws are NOT adopted — contract R3:
        # one stylesheet serves 183 lesson slots and the shipped values already
        # satisfy every clause of MRB-208's ruled identity for this box.
        {"type": "key-fact", "ref": "four-jobs"},

        # #s-sort — the per-item sorter, on inset ground.
        {"type": "job-sort", "id": "which-job", "anchor": "s-sort",
         "ground": "inset",
         "eyebrow": "Your turn · six things people notice",
         "heading": "Which job is this?",
         "head_counter": {"format": "{n} of 6 decided", "total": 6},
         "demand": "classify",
         "prompt": "Every one of these is something you could see or measure. "
                   "Decide which of the four jobs it is evidence for. One of "
                   "them is evidence for two.",
         "categories": JOBS,
         # ⚠️ `i4` answers a fifth string that is NOT one of the four job
         # labels, and that is the item's whole point. `sort-task` would refuse
         # this payload at build time; `job-sort` deliberately does not
         # validate answers against the offered options.
         "items": [
             {"id": "i1",
              "text": "A doctor takes a sample from inside the hip bone of a patient who is short of red blood cells.",
              "answer": "Making blood cells.",
              "why": "The marrow is the factory, so it is the marrow you sample when the supply has failed."},
             {"id": "i2",
              "text": "A 60 kg person stands still for an hour and does not fold up.",
              "answer": "Support.",
              "why": "Soft tissue cannot hold that load. Rigid bars, stacked in line, carry it into the ground."},
             {"id": "i3",
              "text": "A cyclist’s helmet is designed to crush and be thrown away after one impact.",
              "answer": "Protection.",
              "why": "The helmet is doing the skull’s job, more slowly. Both work by taking the energy so the brain does not."},
             {"id": "i4",
              "text": "Your ribs swing up and outwards every time you breathe in.",
              "answer": "Movement and protection — both.",
              "why": "This is the one that is evidence for two jobs at once. The same cage that shields the heart is also the thing that pulls air in."},
             {"id": "i5",
              "text": "A tennis player’s racket arm has denser bone than the other arm.",
              "answer": "Support.",
              "why": "The bone has been loaded harder, so it has built more material where the force goes. That only makes sense for something alive."},
             {"id": "i6",
              "text": "A sprinter’s heel bone has a tendon attached to the back of it, well behind the ankle joint.",
              "answer": "Movement.",
              "why": "A muscle needs something rigid to pull on, and where it attaches decides what the pull does."},
         ]},

        {"type": "misconception", "id": "bones-are-dead", "anchor": "s-think",
         "targets": "BODY-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "four-jobs",
         "text": "The skeleton does four jobs at once: support, protection, "
                 "movement, and making blood cells. Every one of them, when it "
                 "fails, ends at the same place — cells that can no longer "
                 "work.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # The two instruments are authored inline in `core` above and lifted here
    # by `ks3_data/b2/__init__.py`. What is left is the confrontation.
    "activities": [
        # ── #s-think · commit, then two paragraphs (contract R1) ────────────
        # `predict`, not `confrontation`: the block asks for a commitment and
        # gates a reveal behind it, so it IS a completed activity and the rail
        # ticks on it. The quote comes from BODY-01's statement above, which is
        # the page's own line.
        {"id": "bones-are-dead",
         "kind": "predict",
         "demand": "explain",
         "targets": "BODY-01",
         "prompt": "The skeleton in the corner of the lab is dead. The one you "
                   "are sitting on is not. Commit to an answer before you read "
                   "on.",
         "options": [
             "A broken bone heals itself",
             "Bone has its own blood supply",
             "Bone gets thicker where it is used hardest",
             "All three of these are true",
         ],
         "reveal": [
             "All four are true, and every one of them is impossible for "
             "something dead. Bone is a living tissue: it is made of cells, it "
             "has its own blood supply, it repairs itself when it breaks, and "
             "it is rebuilt continuously — you replace roughly a tenth of your "
             "skeleton every year.",
             "It also responds to what you do with it. Load a bone regularly "
             "and it lays down more material exactly where the force goes; "
             "stop loading it and it thins. That is why a tennis player's "
             "racket arm has measurably denser bone than the other one, and "
             "why astronauts come home with weaker skeletons than they left "
             "with.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Two rungs the page marks, two the student marks — decided by the data
    # (options vs success), not by rung number. Every `correction` string is
    # science-bearing and is lifted verbatim.
    "ladder": {
        "recall": {
            "q": "Where are new red blood cells made?",
            "options": [
                "In the marrow inside the bones",
                "In the heart",
                "In the lungs",
                "In the liver",
            ],
            "answer": 0,
            "feedback": {
                1: "The heart pumps blood; it does not make any of it. Nothing "
                   "about a pump implies a factory.",
                2: "The lungs load oxygen onto red blood cells that already "
                   "exist. They do not build them.",
                3: "A reasonable guess — the liver does make them before you "
                   "are born. After birth the job moves to the marrow for "
                   "good.",
            }},
        "apply": {
            "q": "Why would damage to the ribcage stop oxygen reaching the "
                 "cells in your toes?",
            "options": [
                "Because the chest cannot be made bigger, so air stops "
                "entering the lungs",
                "Because the ribs carry oxygen to the rest of the body",
                "Because the ribs protect the heart, and the heart would stop",
                "Because the ribs contain marrow, so blood cells would stop "
                "being made",
            ],
            "answer": 0,
            "feedback": {
                1: "Bone carries loads, not oxygen. Blood carries oxygen, and "
                   "blood needs the lungs to be filled first.",
                2: "That is a different job of the same bones. The chain here "
                   "starts with air, not with the heart.",
                3: "Ribs do contain marrow, which makes this tempting. But "
                   "that failure takes months; the breathing one takes "
                   "minutes.",
            }},
        "explain": {
            "q": "\"The skeleton is a frame that holds you up.\" Explain why "
                 "that is not good enough, using two jobs a frame does not do.",
            "field_label": "Your explanation",
            "placeholder": "Holding you up is only one of…",
            "success": [
                "Names protection, with an example of an organ and the bone "
                "that shields it.",
                "Names making blood cells, and says where in the bone it "
                "happens.",
                "Says bone is living tissue — it has cells, a blood supply, "
                "and it heals.",
                "Says muscles need something rigid to pull against, so "
                "movement is a skeletal job too.",
                "Says a frame is fixed and does none of these, while a "
                "skeleton rebuilds itself.",
            ]},
        "produce": {
            "q": "Astronauts lose roughly 1 to 2% of their bone mass every "
                 "month in orbit, even though they eat well and exercise. "
                 "Explain which of the skeleton’s four jobs is being lost, "
                 "which are not, and why weightlessness causes it.",
            "field_label": "Your answer",
            "placeholder": "In orbit, the job that stops being needed is…",
            "success": [
                "Says support is the job that is not being demanded, because "
                "nothing has to be held up.",
                "Says bone responds to the forces put through it, and thins "
                "when they are removed.",
                "Says protection and making blood cells are still needed and "
                "still happening.",
                "Says bone must be living for any of this to happen.",
                "Predicts a consequence on return to Earth — a weakened "
                "skeleton and a higher risk of breaks.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Support, protection, movement, blood cells. Bone is living "
                "tissue with its own cells and blood supply, and it rebuilds "
                "itself around the forces you put through it. Switch any part "
                "of the skeleton off and the failure ends at the cells.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    "stretch": [
        {"type": "explainer", "id": "why-a-femur-is-hollow",
         "text": "A femur is hollow. So is every long bone you own, and so is "
                 "the wing bone of a bird. Filling it in would add weight "
                 "everywhere and strength almost nowhere, because a bar loaded "
                 "from the side is barely stressed down its middle — the work "
                 "happens near the surface. Engineers reached the same answer "
                 "independently: scaffolding poles, bicycle frames and "
                 "aircraft spars are all tubes. And the space inside the tube "
                 "is not wasted. That is where your blood is made."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # Design heads the card "Ask Mr Badmus AI" and puts the lesson's own
    # sticking point in the paragraph under it, where B1 puts the question in
    # the heading. `body` is the slot for the second line.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure how one broken bone reaches every cell?",
              "cta": "Ask about this lesson",
              "anchor": "s-switch"},

    # Design's third card is PROSE, not a link list, on all four B2 pages.
    "ks4_becomes": "Bone as a tissue, osteoporosis, and the transport system "
                   "that carries what the marrow makes.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
