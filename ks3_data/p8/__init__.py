"""P8 — *Electric circuits*, as one module per lesson.

Seven lessons, a complete unit. The package layout follows `ks3_data/p6/`
exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p8/`. Her page wins outright.

── ⚖️ THE OWNERSHIP MAP — THREE STATEMENTS OVER SEVEN SLOTS ───────────

P8 is the most surplus-slot unit in physics: three statements, seven
lessons, ratio 0.43. Both compound statements are split at the clause;
`CUR.03` is whole and `p8-07` owns a Working Scientifically statement.

    p8-01  current-and-circuits     CUR.01a "electric current, measured in
                                    amperes, in circuits; current as a flow
                                    of charge"
    p8-02  series-and-parallel      CUR.01b "series and parallel circuits"
    p8-03  current-at-a-junction    CUR.01c "currents add where branches
                                    meet"
    p8-04  potential-difference     CUR.02a "potential difference, measured
                                    in volts; battery and bulb ratings"
    p8-05  resistance               CUR.02b "resistance, measured in ohms,
                                    as the ratio of p.d. to current"
    p8-06  conductors-and-...       CUR.03 whole
    p8-07  building-and-measuring   KS3.WS.EXP.03 — planning an enquiry and
                                    identifying its variables

The `.a` / `.b` / `.c` sub-IDs are minted in `ks3_data/substatements.py`
under the rule that file already carries. This is the fourth unit in this
run to use it; Design's FLAG 1 is its third repeat and asks for a notation
that already existed, because the file is not in the read-only reference
set she works from.

── ⚖️ HER FLAG 2 IS HONOURED: `p8-07` OWNS NO SUBJECT-CONTENT CLAUSE ──

Her sentence: *"If a coverage gate requires every slot to own something,
`p8-07` needs either a WS tag it can count or a split of `CUR.02`."* The
WS tag is what it takes. `KS3.WS.EXP.03` — *select, plan and carry out the
most appropriate types of scientific enquiries to test predictions,
including identifying independent, dependent and control variables* — is
exactly what rung 4 asks for and exactly what the lesson teaches. §5.7
exempts WS statements from the exactly-once rule, so nothing else in the
key stage is disturbed by the claim.

The alternative — `beyond_statutory: True` with empty `covers` — would
have been WRONG rather than merely uglier: §7.6 is for OFF-SPEC content,
and Working Scientifically is on the spec.

── ⚖️ FOUR RAIL STOPS PER LESSON ─────────────────────────────────────

Measured off Design's own `RAIL` constant on each page:

    p8-01  s-hook s-loop     s-think   s-ladder
    p8-02  s-hook s-bench    s-compare s-ladder
    p8-03  s-hook s-junction s-bar     s-ladder
    p8-04  s-hook s-volt     s-bar     s-ladder
    p8-05  s-hook s-bench    s-triangle s-ladder
    p8-06  s-hook s-test     s-scale   s-ladder
    p8-07  s-hook s-wire     s-fault   s-ladder

⚠️ **FOUR BAND STOPS TICK EARLIER THAN THEIR BENCH** — `s-think`,
`s-compare`, `s-scale` and `s-fault` all take `gate !== null` while the
bench needs the gate AND a control touched. Each bench marks its own
sibling, as in P4 and P6; `mirrors` would tick them late, and MRB-249
derives its mirror map from IDENTICAL expressions, which these are not.

⚠️ **`p8-01`'s `s-think` IS A MISCONCEPTION BLOCK ON THE RAIL**, which is
new in this key stage. See the note in `ks3_art/p8.py` on `circ-think`:
the block has to ship `data-stage-done="0"` in the BUILT BYTES for
`check_rail_reachable`, and neither `confrontation` nor `predict` emits
one. Every other page's `s-think` is an ordinary `predict` block, because
Design does not put it on their rails.

⚠️ **MRB-208** — on `p8-03`, `p8-04` and `p8-05` the formula stop goes on
the ATTEMPT PANEL, because `s.q[0].open && s.q[1].open` is what her own
`DONE` reads. `p8-06`'s formula section takes no rail stop at all: her
`RAIL` for that page is `s-hook s-test s-scale s-ladder` and `#s-formula`
is not among them.

── ⚖️ THE `CIRC` FAMILY OPENS HERE ───────────────────────────────────

See the ruling in `docs/ks3/misconception-register.md`. `CIRC-01` …
`CIRC-28` are minted by these seven lessons, sixteen of them on the
numbers Design's §7 gave them and in her words.

── ⚠️ POSITION IS AUTHORED, AND ON THE MARKED RUNGS IT MOVED ─────────

Every one of Design's fourteen marked rungs in P8 has its correct answer
at index 0 — the exact defect MRB-278 exists for, measured before a line
was written. Engine policy, not a departure: the OPTIONS ARE REORDERED so
that across the unit's fourteen rungs no index holds more than half and
none is unused (4 / 3 / 4 / 3 across indices 0–3). Every option's text is
hers to the character and so is every correction; only the order changed,
and each lesson's docstring records the indices it takes.
"""

import importlib
import pkgutil
import re

_INSTRUMENT_SEGMENTS = {
    # Every P8 bench is `ks3-block ks3-dark ks3-practical`.
    "circuit-loop":         "practical",
    "two-arrangement-loop": "practical",
    "junction-bench":       "practical",
    "voltmeter-tap":        "practical",
    "component-under-test": "practical",
    "test-gap":             "practical",
    "meter-placement":      "practical",
    # The fixed figures are bare `ks3-block` on the band ground.
    "circ-band":            "check",
    # ⚠️ AND THE ONE CONFRONTATION THAT IS A RAIL STOP. `misconception` is
    # the shell Design draws it in — the amber badge and the "Think again"
    # eyebrow — and routing it through the segment map is what gets the
    # `data-stage-done="0"` marker into the same tag.
    "circ-think":           "misconception",
}

# ⚠️ `p8-attempt` IS NOT IN THE TABLE ABOVE, for the same reason it is not
# in P4's, P5's or P6's: it is authored in `activities[]` beside the two
# worked examples and placed in `core` as a `check` naming its id.

_BLOCK_KEYS = ("type", "anchor", "id")


def _normalise(lesson):
    """Lift inline instrument blocks into `activities[]`. Returns the lesson."""
    core = lesson.get("core") or []
    acts = list(lesson.get("activities") or [])
    known = {a.get("id") for a in acts}
    out = []

    for block in core:
        kind = block.get("type")
        segment = _INSTRUMENT_SEGMENTS.get(kind)
        if segment is None:
            out.append(block)
            continue

        act_id = block.get("id") or block.get("anchor") or kind
        if act_id in known:
            raise ValueError(
                "%s: instrument %r collides with an existing activity id"
                % (lesson.get("slug"), act_id))
        known.add(act_id)

        payload = {k: v for k, v in block.items() if k not in _BLOCK_KEYS}
        payload.update({"id": act_id, "kind": kind})
        payload.setdefault("demand", "investigate")
        acts.append(payload)
        out.append({"type": segment, "id": act_id,
                    "anchor": block.get("anchor")})

    lesson["core"] = out
    lesson["activities"] = acts
    return lesson


# ⚖️ MRB-297 / P8-03, RULED 30 Aug 2026 — A PRINTED `a ÷ b = c` MUST BE
# TRUE, AND THE BUILD IS WHERE THAT IS SETTLED.
#
# `p8-06`'s "your turn" printed the MANTISSA of the prefixed answer as the
# quotient — "6.0 ÷ 0.0000012 = 5.0" for an answer of 5.0 MΩ, and
# "6.0 ÷ 0.0015 = 4.0" for 4.0 kΩ — in seven of its fourteen states, with a
# step note directly beneath saying "volts divided by amps leaves ohms". A
# student who did the division correctly and wrote 5 000 000 marked
# themselves wrong against the model answer. It is the exact unit-prefix
# error the five-step method exists to prevent, and nothing could see it,
# because every gate in the estate reads the vocabulary of a line rather
# than its arithmetic.
#
# So the arithmetic is read. Every string in every P8 lesson is scanned for
# a fully numeric division and the division is done. A line whose numbers
# are still `{tokens}` cannot be checked here, so the attempt panels are
# checked a second time with their own `rest` defaults substituted, which
# is the state the page ships in.
#
# ⚠️ THIS COVERS P8 AND ONLY P8. The class is estate-wide and the check
# belongs beside the FIFA renderer in `ks3_art/kit.py`, where every unit's
# worked examples and attempts pass through one function. That file is
# shared and this lane may not edit it; the extension is written up in the
# MRB-297 report.

_NUM = r"\d+(?: \d{3})+|\d+(?:\.\d+)?(?:[eE][-+]?\d+)?"
_TAIL = r"(?:\s*[^\s0-9÷=][^\s÷=]*)?"
_DIVIDE = re.compile(
    "(%s)%s\\s*÷\\s*(%s)%s\\s*=\\s*(%s)" % (_NUM, _TAIL, _NUM, _TAIL, _NUM))

# Three significant figures on either side of a division leaves about half
# a per cent of slack; 1.5% is comfortably outside rounding and nowhere
# near the thousandfold errors this exists to catch.
_DIVIDE_TOL = 0.015


def _check_divisions(text, where, slug):
    for a, b, c in _DIVIDE.findall(str(text)):
        top = float(a.replace(" ", ""))
        bot = float(b.replace(" ", ""))
        got = float(c.replace(" ", ""))
        if bot == 0:
            raise ValueError(
                "%s: %s prints a division by zero — %r ÷ %r."
                % (slug, where, a, b))
        want = top / bot
        if abs(want - got) > _DIVIDE_TOL * max(abs(want), 1e-30):
            raise ValueError(
                "%s: %s prints “%s ÷ %s = %s”, and %s ÷ %s is %r.\n"
                "⚖️ MRB-297 / P8-03, ruled 30 Aug 2026: a printed division "
                "must be TRUE in the units it is printed in. The commonest "
                "way to break this is to print the MANTISSA of a prefixed "
                "answer as the quotient — 6.0 ÷ 0.0000012 = 5.0 beside an "
                "answer of 5.0 MΩ — which teaches the student that dividing "
                "gives you a small number you then rename, and marks a "
                "correct answer of 5 000 000 wrong. Print the quotient in "
                "BASE UNITS and let the answer line do the prefixing; that "
                "is what the answer line is for."
                % (slug, where, a, b, c, a, b, want))


def _refuse_false_division(lesson):
    slug = lesson.get("slug", "?")

    def walk(v, where):
        if isinstance(v, str):
            _check_divisions(v, where, slug)
        elif isinstance(v, dict):
            for k, sub in v.items():
                walk(sub, "%s.%s" % (where, k))
        elif isinstance(v, (list, tuple)):
            for i, sub in enumerate(v):
                walk(sub, "%s[%d]" % (where, i))

    walk(lesson, "the lesson")

    # And again with each attempt panel's own defaults filled in, because
    # `{ibare}` and `{rohms}` hide the arithmetic from the pass above and
    # the filled line is what the page ships showing.
    for act in lesson.get("activities") or []:
        rest = act.get("rest")
        if not isinstance(rest, dict):
            continue
        for qi, q in enumerate(act.get("questions") or []):
            for si, st in enumerate(q.get("steps") or []):
                filled = str(st.get("line", ""))
                for key, val in rest.items():
                    filled = filled.replace("{%s}" % key, str(val))
                _check_divisions(
                    filled,
                    "%s question %d step %d, with its own `rest` defaults"
                    % (act.get("id", "?"), qi + 1, si + 1), slug)
    return lesson


def lessons():
    """The authored P8 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_refuse_false_division(_normalise(dict(record))))
    return found
