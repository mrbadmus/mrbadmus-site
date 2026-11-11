# The lean lesson record

One lesson = one Python file of words. Layout lives in `lean_blocks.py`, `shared/lean.css`
and `shared/lean.js`, used by KS3 and KS4 alike. A batch writes records. It never touches layout.

    KS3   ks3_data/lean/<slug with _>.py    merged over the lesson by ks3_data.build_units()
    KS4   ks4_lessons/lean/<slug with _>.py one record, every route, built by the `lean` batch

## The record

    LESSON = {
      "slug": "efficiency",
      "start": {
        "setup": "An old filament bulb and an LED light a room equally well.",   # or None
        "question": "If you had to guess, which one wastes more energy?",
        "options": [("The LED", "reply"), ("The filament bulb", "reply")],       # exactly 2
        "answer": 1,
      },
      "words": ["efficiency", "useful energy", "wasted energy", "dissipated"],   # 3 or 4
      "knowledge": [ <card or reveal>, ... ],
      "key_fact": "One or two sentences that carry the science.",
      "deeper": [ <card>, ... ],
      "try": None,      # or {"label": "Ripple tank", "href": "/simulations/physics/wave-motion-lab/"}
    }

KS3 adds `"ladder_feedback": {"recall": {1: "...", 2: "...", 3: "..."}, "apply": {...}}`.
It changes what the lesson page shows and nothing else: the ladder questions, answer keys and
the database mirror stay exactly as they are.

KS3 may also add `"ladder_stem": {"produce": "..."}`, again at render time only, where a stem
names something the lean page no longer has (for example "Using the bench").

KS4 adds `"legacy"` (see `lean_ks4.py`). A lesson with no legacy page adds:

    "rungs": {"r1": [...], "r2": [...], "r3": [...], "r4": [...]},   # 2·2·2·1, the Ks4Practice item shapes
    "equations": {"EQ_SHC": {"name": "...", "written": "...", "source": "none",
                             "top": {"s": "ΔE", "name": "...", "unit": "J"},
                             "bottom": [{"s": "m", "name": "...", "unit": "kg"}, ...]}},
    "cfifa": {"examples": [{"tab": "...", "eq": "EQ_SHC", "find": "ΔE", "head": "...",
                            "steps": [["C", "Convert", "line", "optional note"], ...]}],
              "questions": [...]},   # the Ks4Cfifa question shape, optional

A slot named `triangle:EQ_SHC` places that equation's triangle. A slot named `cfifa` places the
worked examples. A legacy lesson can use the same two fields to add what its old page lacked.

## A card

    {"kind": "card", "title": "Where wasted energy goes",
     "body": [ <part>, ... ],
     "routes": ["CH", "TH"]}          # optional. Omit for every route.

A part is one of:

    "A plain sentence or two."             a paragraph (may use <strong>, <em>, <sub>, <sup>)
    {"points": ["...", "..."]}             a bullet list
    {"mistakes": [("wrong", "right")]}     Easy mistakes: ✗ line then ✓ line
    {"slot": "name"}                       KS4 only: a compiled block placed here (triangle, CFIFA…)
    {"figure": "id"}                       KS3 only: a drawn figure from the lesson's figures[]

## A reveal table

    {"kind": "reveal", "title": "Breathing in and breathing out",
     "cols": ["Breathing in", "Breathing out"],
     "rows": [("Ribs", "Move up and out", "Move down and in"), ...]}

Each answer cell is hidden until tapped. A "Show all" button opens the whole table.

## Routes

CF, CH, TF, TH. Foundation pages never show Higher-only cards. Combined pages never show
Triple-only cards. Check every route separately.
