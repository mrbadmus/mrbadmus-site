"""ks3_art.c10 — C10's instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may
be added to any other unit's module. C10 is *The Earth and its atmosphere*:
six lessons, ELEVEN instrument families and no drawn figure so far, all DOM,
no canvas and no animation loop anywhere in the unit.

═══════════════════════════════════════════════════════════════════════════
⊕ WAVE 6 — ALL ELEVEN FAMILIES IMPLEMENTED. THE UNIT IS COMPLETE.
═══════════════════════════════════════════════════════════════════════════

Wave 1 built the unit spine and the reference lesson `c10-04`; wave 2 added
`c10-01`; wave 3 added `c10-02`; wave 4 added `c10-03`; wave 5 added `c10-05`;
wave 6 adds `c10-06` and closes the unit. Eleven families are implemented and
all eleven are registered:

    material-loop   ks3-mloop-block   c10-04  #s-loop    ← INK-DARK
    stock-limits    ks3-stock-block   c10-04  #s-stock
    earth-layers    ks3-elay-block    c10-01  #s-layers
    depth-evidence  ks3-edep-block    c10-01  #s-evidence
    rock-bench      ks3-rockb-block   c10-02  #s-bench
    grain-journey   ks3-grain-block   c10-03  #s-journey
    process-arrows  ks3-parrow-block  c10-03  #s-processes
    air-mix          ks3-amix-block    c10-05  #s-mix
    atmos-history    ks3-ahist-block   c10-05  #s-history
    greenhouse-steps ks3-ghouse-block  c10-06  #s-how
    climate-evidence ks3-cev-block     c10-06  #s-evidence

⊖ **THE LAST TWO ROWS WERE HELD BACK UNTIL THEY EXISTED, and this paragraph is
kept because it is the reason they were.** `ks3_art.check_placements` gate 2
fails a family that is registered and never placed, and gate 3 fails one that
is placed and never registered. A stub row added "ready" for a later lane
would have shipped the shell around the generic prompt/options branch — the C1
defect (MRB-228) — the moment a lesson named it. Each lane registered its own;
`c10-06` was the last, and both of its renderers land in this file beside their
rows.

The eleven shell classes above were checked free against every `KIND_SHELL`
value in `ks3_art` before minting (MRB-279). `c10-02`'s `#s-table` is NOT on
the list: it is a controlless REFERENCE stop mirroring the hook, which is a
`rule` block and not an instrument, and `c10-04`'s `#s-words` is the existing
vocabulary block.

═══════════════════════════════════════════════════════════════════════════
⚖️ RULED · `#s-loop` TAKES THE `practical` SHELL, NOT A `ks3-dark` MODIFIER
═══════════════════════════════════════════════════════════════════════════

Design drew `c10-04`'s bench as `class="ks3-block ks3-dark"` — and that exact
attribute appears **once in the whole design-reference tree**. Every other
ink-dark instrument in the key stage, on all four B4 pages, all four B11
pages, all six B9 pages and the rest, is `class="ks3-block ks3-dark
ks3-practical"`, which is what `ACTIVITY_SHELLS["practical"]` emits and what
the unit's `_INSTRUMENT_SEGMENTS` map therefore selects.

**Taken as `practical`.** The alternative — segment `check` plus a second
class inside this family's `KIND_SHELL` value — was measured and rejected:

1. **The bare pair is the ABSENCE of a shadow, not a fourth treatment.**
   `.ks3-block` sets `box-shadow: var(--ks3-shadow-block)`, which is
   `5px 5px 0 var(--ks3-ink)`, and `.ks3-dark` sets the block's ground to
   `--ks3-ink`. Ink on ink is invisible. `shared/ks3.css` says so in its own
   words at the three inverting blocks: "Each takes a different shadow colour,
   which is what tells them apart at a glance while the ground stays
   constant." A dark block with no third class has not chosen a colour; it has
   left the choice out.
2. **A two-class `KIND_SHELL` value would be a NEW mechanism in a shared
   contract.** All 145 registered families across `ks3_art/` carry exactly one
   modifier class, and MRB-279's collision gate reads the FIRST class of the
   value — so a second class in that slot is a string nothing checks. The
   sanctioned way for a block to name its ground is the segment, and MRB-245
   made a disagreement between the declared segment and the rendered shell a
   build failure precisely so that there is one answer.
3. The `practical` shell also keeps the block's fixed eyebrow ("Investigate")
   as a FALLBACK only — c10-04 authors its own, so the drawn words are the
   words that ship.

⚑ **THE TWO VISIBLE DELTAS, STATED RATHER THAN HIDDEN.** Against Design's file
the built block gains `box-shadow: 6px 6px 0 var(--ks3-blue)` and its eyebrow
moves from `--ks3-alert` to `--ks3-blue-light`. Both come from
`.ks3-practical`, both are the treatment every other dark bench in the key
stage already wears, and neither is a shape she did not draw.

⚑ **AND ONE MORE, FOR THE SAME REASON.** Design's `seg(on, dark)` paints the
lit segmented button `--ks3-accent` with `--ks3-on-dark` text. The shared
`.ks3-dark .ks3-seg-btn[aria-pressed="true"]` paints it `--ks3-alert` with ink
text, which is MRB-242 — a recorded correction applied to sixteen buttons
across three B1 pages after they fell through to the light branch at 1.35:1.
The house control is used unchanged rather than overridden for one unit.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS FILE IS RESPONSIBLE FOR, AND WHAT IT IS NOT
═══════════════════════════════════════════════════════════════════════════

MARKUP ONLY, on C7's, C8's and C9's conventions and for their reasons.

  · EMIT-BOTH-SHOW-ONE. The loop bench's twenty states are all in the
    document, each with its own bars, stats and verdict, and `shared/ks3.js`
    chooses which one is `hidden`. Nothing is composed at runtime.
  · NUMBERS ARE DERIVED, NEVER AUTHORED TWICE. Every mass, every percentage
    and every multiplier below is computed here from `recovery`, `rate`,
    `e_primary` and `e_recycled`. The payload states none of them.
  · COMPARATIVE LABELS ARE DERIVED TOO. The verdict sentences are authored
    with `{mult}` / `{saving}` / `{rate}` slots and filled per state, so a
    branch reached at three different collection rates says three different
    true things rather than one sentence that is true at one of them.
  · ONLY THE LADDER MARKS. Both benches give their verdict in WORDS.
  · Every family ticks a rail stop, so every family carries
    `data-stage-done="0"`. NOTHING IS TICKED ON LOAD (MRB-208) — which is not
    the same as nothing being SELECTED on load; see `start_material`.
  · Arrows are drawn as SVG by `t()`, never typed as U+2192.

⚠️ **`--ks3-ember` DOES NOT EXIST.** NOTES-C10's closing note records it: the
on-dark accent token people reach for is `--st-ember`, which belongs to the
studio surface, and an undefined custom property is dropped in silence — the
label inherits `--ks3-on-dark`, contrast stays fine and no gate trips. The
mono control-group labels on this bench are `--ks3-on-dark-muted`.
"""

import re

from ks3_art.kit import e, rich, t


# ═══ shared inside C10 ═══════════════════════════════════════════════════

def _c10_seg(cls, label, pressed=False, **attrs):
    """One segmented-control button. No `correct`, ever.

    ⚠️ `pressed` IS REAL STATE, NOT A DECORATION. C9's equivalent hard-codes
    `aria-pressed="false"` because every C9 bench opens empty. This one does
    not: Design's loop bench opens on a material and a collection rate, and
    the readout under it is a real answer to a real pair of settings before
    the student touches anything. Emitting the opening selection as
    `aria-pressed="true"` is what makes the resting page HONEST — the shown
    panel and the lit button then agree in the HTML, rather than agreeing only
    after `shared/ks3.js` has run. MRB-208 is untouched by this: what may not
    be ticked on load is the RAIL STOP, and `data-stage-done` still opens at 0.
    """
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="%s">%s</button>'
            % (e(cls), extra, "true" if pressed else "false", t(label)))


def _group(cls, label, buttons):
    """A mono label over a row of segmented buttons, as Design stacks them."""
    return ('<p class="%s-glabel">%s</p><div class="%s-group">%s</div>'
            % (cls, t(label), cls, "".join(buttons)))


def _unique_ids(rows, act_id, family, what):
    """Ids inside one payload are unique, because they become DOM keys."""
    ids = [r.get("id") for r in rows]
    if not all(ids):
        raise ValueError(
            "%s %r: a %s has no id. The id is half of the `data-*-out` key "
            "that selects its panel, so a missing one silently collapses two "
            "states into one." % (family, act_id, what))
    if len(set(ids)) != len(ids):
        raise ValueError(
            "%s %r repeats a %s id in %s. Two rows with one key means one of "
            "them can never be shown." % (family, act_id, what, ids))
    return ids


def _no_correct_flags(rows, act_id, family):
    """Refuse a `correct` key on any control, anywhere in C10."""
    for row in rows:
        if isinstance(row, dict) and ("correct" in row or "correction" in row):
            raise ValueError(
                "%s %r: %r carries a marking key. Nothing outside the mastery "
                "ladder marks in C10 — every bench gives its verdict in words."
                % (family, act_id, row.get("id") or row.get("label")))


# ═══ c10-04 · material-loop ══════════════════════════════════════════════

# The six verdict branches, in the order they are tested. ORDER IS THE
# ARGUMENT: `floor` is tested before `strong` because the crisp packet at nine
# in ten is a collection success and a recycling failure at the same time, and
# a page that reported the multiplier first would praise it.
_MLOOP_BRANCHES = ("none", "floor", "strong", "real", "degraded",
                   "poor_collection")

# The material whose `recovery` is at or below this comes back as essentially
# nothing, whatever is collected. Design's own threshold, and it is read twice
# — once to choose the branch and once by the assertion that every branch is
# reachable.
_MLOOP_FLOOR = 0.05
_MLOOP_STRONG = 5.0
_MLOOP_REAL = 1.7
_MLOOP_DEGRADED = 0.5


def _mloop_branch(rate, recovery, mult):
    """Which of the six verdicts this state gets. COMPUTED, NEVER STORED.

    ⚖️ THE VERDICT IS A FUNCTION OF THE TWO READINGS AND OF NOTHING ELSE.
    NOTES-C10 is explicit that it must not be stored per state, and the reason
    is the one the bench exists to teach: a per-state table would let the
    aluminium row and the glass row say different things at the same
    multiplier, which is exactly the belief ("recycling saves about 95%") that
    the glass row is on the bench to break.
    """
    if rate <= 0:
        return "none"
    if recovery <= _MLOOP_FLOOR:
        return "floor"
    if mult >= _MLOOP_STRONG:
        return "strong"
    if mult >= _MLOOP_REAL:
        return "real"
    if recovery <= _MLOOP_DEGRADED:
        return "degraded"
    return "poor_collection"


def _mloop_mass(kg, unit):
    """Design's own four-way mass format, and it is four-way for a reason.

    A bar at 1000 kg and a bar at 0.4 kg are on the same list, so one number
    format cannot serve both: `1000.00 kg` is noise and `0 kg` at the fourth
    pass of an aluminium run is a lie. Below 0.05 kg it prints a bare zero,
    which is the honest reading at this scale — 40 g of a starting tonne.
    """
    if kg >= 100:
        body = "%d" % round(kg)
    elif kg >= 1:
        body = "%.1f" % kg
    elif kg < 0.05:
        body = "0"
    else:
        body = "%.2f" % kg
    return "%s %s" % (body, unit)


def r_material_loop(a, act_id):
    """⊕ c10-04 `#s-loop` — 1000 kg in, five materials, four collection rates.

    TWENTY REACHABLE STATES, ALL ENUMERATED, and every combination legal
    including a collection rate of zero. Each state carries six mass bars, a
    lifetimes multiplier, two energy figures and one of six verdicts — all of
    them computed here, none of them authored.

    THE ARITHMETIC, ONCE. With `f = collection × recovery`, one kilogram of
    new material delivers `1 + f + f² + …` lifetimes of service, which
    converges to `1/(1 − f)`. The bars are `1000 × fⁿ`. The energy saving is
    `1 − e_recycled/e_primary`.

    ⚖️ **`order_claim` IS THE CLAIM THE BENCH MAKES, AND IT IS CHECKED.**
    NOTES-C10 says in as many words that "the ordering is the claim, not the
    second decimal place" — the five materials are on the bench to be read
    against each other, and if a yield is ever edited, the thing that must not
    move silently is which material beats which. The authored order is checked
    against the order the multipliers actually produce at the highest
    collection rate. A payload re-sorted for layout cannot change it, and a
    figure edited without thinking fails the build instead of re-teaching the
    lesson.

    ⚖️ **EVERY BRANCH MUST BE REACHABLE.** Six verdicts are authored and the
    twenty states are swept to prove every one of them is used. An unreachable
    branch is a sentence a student can never see, and an unused branch usually
    means a threshold moved rather than that the sentence was wrong.

    HOOKS: `data-mloop` (wrapper, `data-total`, `data-target`) ·
    `data-mloop-mat` · `data-mloop-rate` · `data-mloop-out` (valued
    `material:rate`) · `data-mloop-hint`.
    """
    mats = a.get("materials") or []
    rates = a.get("rates") or []
    verdicts = a.get("verdicts") or {}

    if len(mats) < 3 or len(rates) < 3:
        raise ValueError(
            "material-loop %r has %d material(s) and %d rate(s). The bench is "
            "a comparison in two directions; with fewer than three of either "
            "there is no range to read." % (act_id, len(mats), len(rates)))
    _unique_ids(mats, act_id, "material-loop", "material")
    _unique_ids(rates, act_id, "material-loop", "rate")
    _no_correct_flags(mats + rates, act_id, "material-loop")

    missing = [b for b in _MLOOP_BRANCHES if not verdicts.get(b)]
    if missing:
        raise ValueError(
            "material-loop %r authors no verdict for branch(es) %s. Each "
            "branch says something the others cannot, and a state that "
            "reaches an empty one shows the student a blank line under a "
            "bench they have just worked." % (act_id, missing))
    extra = sorted(set(verdicts) - set(_MLOOP_BRANCHES))
    if extra:
        raise ValueError(
            "material-loop %r authors verdict(s) %s that no branch selects. A "
            "sentence nothing can reach is content that never arrives."
            % (act_id, extra))

    # ── the payload's own numbers, checked before anything is drawn ──────
    for m in mats:
        for key in ("label", "name", "what"):
            if not m.get(key):
                raise ValueError(
                    "material-loop %r material %r has no %r."
                    % (act_id, m["id"], key))
        rec = float(m.get("recovery", -1))
        if not 0 < rec <= 1:
            raise ValueError(
                "material-loop %r material %r has recovery %r. It is the "
                "fraction of COLLECTED material that comes back usable, so it "
                "lives in (0, 1] — and a zero would make the bench say "
                "nothing comes back even at perfect collection, which is a "
                "claim no material on this bench makes."
                % (act_id, m["id"], m.get("recovery")))
        ep, er = float(m.get("e_primary", 0)), float(m.get("e_recycled", -1))
        if ep <= 0 or er < 0:
            raise ValueError(
                "material-loop %r material %r has energy figures %r / %r. "
                "Both are printed as a number with a unit on the panel."
                % (act_id, m["id"], m.get("e_primary"), m.get("e_recycled")))
        if er > ep:
            raise ValueError(
                "material-loop %r material %r costs MORE energy from recycled "
                "(%s) than new from ore (%s). The stat under it reads "
                "'x%% less than new', and a negative saving would print a "
                "minus sign into a sentence that promises a saving."
                % (act_id, m["id"], er, ep))

    seen_rates = set()
    for r in rates:
        if not r.get("label") or not r.get("phrase"):
            raise ValueError(
                "material-loop %r rate %r has no label or no phrase. The "
                "label is the button; the phrase is what the verdict "
                "sentence calls it mid-sentence, and one cannot do both jobs "
                "— 'Even at 9 in 10' and 'Even at nine in ten' are not the "
                "same register." % (act_id, r["id"]))
        v = float(r.get("rate", -1))
        if not 0 <= v <= 1:
            raise ValueError(
                "material-loop %r rate %r is %r, and a collection rate is a "
                "fraction between 0 and 1." % (act_id, r["id"], r.get("rate")))
        seen_rates.add(v)
    if 0 not in seen_rates:
        raise ValueError(
            "material-loop %r offers no zero collection rate. Nothing "
            "collected is the state the whole bench is measured against, and "
            "§5A requires the zero to be modelled rather than assumed."
            % act_id)

    start_mass = float(a.get("start_mass") or 0)
    passes = int(a.get("passes") or 0)
    if start_mass <= 0 or not 3 <= passes <= 8:
        raise ValueError(
            "material-loop %r starts at %r over %r pass(es). The mass is the "
            "quantity every bar is a fraction of, and three passes is the "
            "fewest that shows a loop leaking." % (act_id, start_mass, passes))

    mass_unit = a.get("mass_unit") or "kg"
    pass_label = a.get("pass_label") or "Use {n}"
    if "{n}" not in pass_label:
        raise ValueError(
            "material-loop %r's pass_label %r names no {n}, so all %d bars "
            "would carry the same word." % (act_id, pass_label, passes))

    start_mat = a.get("start_material") or mats[0]["id"]
    start_rate = a.get("start_rate") or rates[-1]["id"]
    if start_mat not in [m["id"] for m in mats] \
            or start_rate not in [r["id"] for r in rates]:
        raise ValueError(
            "material-loop %r opens on %r / %r, and one of those is not on "
            "the bench. The opening state is what a student reads before "
            "touching anything." % (act_id, start_mat, start_rate))

    target = int(a.get("materials_to_tick") or 0)
    if not 2 <= target <= len(mats):
        raise ValueError(
            "material-loop %r ticks its rail stop at %r of %d materials. Two "
            "is the fewest that is a comparison and more than the set is a "
            "stop that can never tick." % (act_id, target, len(mats)))

    # ── the twenty states ────────────────────────────────────────────────
    branches_used = set()
    outs = []
    top = max(rates, key=lambda r: float(r["rate"]))
    tops = {}

    for m in mats:
        rec = float(m["recovery"])
        ep, er = float(m["e_primary"]), float(m["e_recycled"])
        saving = int(round((1 - er / ep) * 100))
        for r in rates:
            rate = float(r["rate"])
            f = rate * rec
            mult = 1.0 / (1.0 - f)
            if r["id"] == top["id"]:
                tops[m["id"]] = mult
            branch = _mloop_branch(rate, rec, mult)
            branches_used.add(branch)

            bars = []
            for n in range(passes):
                frac = f ** n
                bars.append(
                    '<li class="ks3-mloop-bar">'
                    '<span class="ks3-mloop-blabel">%s</span>'
                    '<span class="ks3-mloop-track">'
                    '<span class="ks3-mloop-fill" style="width:%.2f%%">'
                    '</span></span>'
                    '<span class="ks3-mloop-mass">%s</span></li>'
                    % (t(pass_label.replace("{n}", str(n + 1))),
                       max(frac * 100.0, 0.0),
                       t(_mloop_mass(start_mass * frac, mass_unit))))

            stats = [
                (a["stat_lifetimes"]["label"], "%.2f×" % mult,
                 a["stat_lifetimes"]["note_zero"] if rate <= 0
                 else a["stat_lifetimes"]["note"]),
                (a["stat_primary"]["label"],
                 "%s %s" % (_num(ep), a["energy_unit"]),
                 a["stat_primary"]["note"]),
                (a["stat_recycled"]["label"],
                 "%s %s" % (_num(er), a["energy_unit"]),
                 (a["stat_recycled"]["note"].replace("{saving}", str(saving))
                  if saving > 0 else a["stat_recycled"]["note_none"])),
            ]
            stats_html = "".join(
                '<div class="ks3-mloop-stat">'
                '<p class="ks3-mloop-slabel">%s</p>'
                '<p class="ks3-mloop-svalue">%s</p>'
                '<p class="ks3-mloop-snote">%s</p></div>'
                % (t(lab), t(val), rich(note)) for lab, val, note in stats)

            verdict = (verdicts[branch]
                       .replace("{mult}", "%.2f" % mult)
                       .replace("{mult_round}", "%.1f" % mult)
                       .replace("{saving}", str(saving))
                       .replace("{rate}", r["phrase"]))

            outs.append(
                '<div class="ks3-mloop-one" data-mloop-out="%s" '
                'data-branch="%s"%s>'
                '<div class="ks3-mloop-panel">'
                '<p class="ks3-mloop-name">%s</p>'
                '<p class="ks3-mloop-what">%s</p>'
                '<ul class="ks3-mloop-bars">%s</ul>'
                '<div class="ks3-mloop-stats">%s</div></div>'
                '<p class="ks3-mloop-verdict">%s</p></div>'
                % (e("%s:%s" % (m["id"], r["id"])), e(branch),
                   "" if (m["id"] == start_mat and r["id"] == start_rate)
                   else " hidden",
                   t(m["name"]), rich(m["what"]), "".join(bars), stats_html,
                   rich(verdict)))

    unused = [b for b in _MLOOP_BRANCHES if b not in branches_used]
    if unused:
        raise ValueError(
            "material-loop %r authors verdict branch(es) %s that none of its "
            "%d states reaches. A sentence no student can arrive at is not a "
            "branch, and an unused one usually means a threshold moved rather "
            "than that the sentence was wrong."
            % (act_id, unused, len(mats) * len(rates)))

    claim = a.get("order_claim")
    if claim is not None:
        derived = sorted(tops, key=lambda mid: (-tops[mid], mid))
        if list(claim) != derived:
            raise ValueError(
                "material-loop %r claims the order %s and its own figures at "
                "%s give %s. The ORDERING is what this bench asserts — the "
                "second decimal place is not — so a payload whose numbers no "
                "longer produce the claimed order has quietly re-taught the "
                "lesson." % (act_id, list(claim), top["label"], derived))

    hint = ""
    if a.get("rate_hint"):
        hint = ('<p class="ks3-mloop-hint" data-mloop-hint>%s</p>'
                % rich(a["rate_hint"]))

    mat_btns = [_c10_seg("ks3-mloop-mat", m["label"], m["id"] == start_mat,
                         data_mloop_mat=m["id"]) for m in mats]
    rate_btns = [_c10_seg("ks3-mloop-rate", r["label"], r["id"] == start_rate,
                          data_mloop_rate=r["id"]) for r in rates]

    return ('<div class="ks3-mloop" data-mloop data-total="%d" '
            'data-target="%d">%s%s%s'
            '<div class="ks3-mloop-readout">%s</div></div>'
            % (len(mats), target,
               _group("ks3-mloop", a.get("materials_label") or "", mat_btns),
               _group("ks3-mloop", a.get("rates_label") or "", rate_btns),
               hint, "".join(outs)))


def _num(v):
    """A teaching figure printed as it was authored: 45, not 45.0."""
    return ("%d" % v) if float(v) == int(v) else ("%g" % v)


# ═══ c10-04 · stock-limits ═══════════════════════════════════════════════

def r_stock_limits(a, act_id):
    """⊕ c10-04 `#s-stock` — five things we take out of the ground.

    A reference shelf: pick one, read what it is for, what its limit actually
    is, and whether recycling touches it. No numbers, no verdict, no marking.

    ⚖️ **NO TWO OF THEM RUN OUT THE SAME WAY, AND THAT IS ASSERTED.** The set
    is not five examples of one idea; it is five different KINDS of limit —
    bauxite's is energy rather than rock, iron's is grade, oil's carbon leaves
    the loop the moment it is burnt, phosphate has no substitute at all, and
    helium physically leaves the planet. `limit_kind` names which, and the
    build refuses a set in which two entries share one. A shelf of five rows
    that all say "there is only so much of it" would be one row printed five
    times, and the student would be right to stop reading after the second.

    HOOKS: `data-stock` (wrapper, `data-total`, `data-target`) ·
    `data-stock-item` · `data-stock-out`.
    """
    entries = a.get("entries") or []
    if len(entries) < 4:
        raise ValueError(
            "stock-limits %r has %d entr(y/ies). The point of the set is that "
            "no two limits are alike, and that needs a set."
            % (act_id, len(entries)))
    _unique_ids(entries, act_id, "stock-limits", "entry")
    _no_correct_flags(entries, act_id, "stock-limits")

    kinds = []
    for x in entries:
        for key in ("label", "name", "use", "limit", "recycle", "limit_kind"):
            if not x.get(key):
                raise ValueError(
                    "stock-limits %r entry %r has no %r. Every one of the "
                    "three lines is on the panel, and a missing one leaves a "
                    "heading over nothing." % (act_id, x["id"], key))
        kinds.append(x["limit_kind"])
    if len(set(kinds)) != len(kinds):
        raise ValueError(
            "stock-limits %r has two entries whose limit is the same KIND "
            "(%s). The shelf's whole claim is that no two of these run out "
            "the same way." % (act_id, kinds))

    start = a.get("start_entry") or entries[0]["id"]
    if start not in [x["id"] for x in entries]:
        raise ValueError(
            "stock-limits %r opens on %r, which is not on the shelf."
            % (act_id, start))

    target = int(a.get("entries_to_tick") or 0)
    if not 2 <= target <= len(entries):
        raise ValueError(
            "stock-limits %r ticks its rail stop at %r of %d. Two is the "
            "fewest that is a comparison and more than the set is a stop that "
            "can never tick." % (act_id, target, len(entries)))

    limit_label = a.get("limit_label") or "The limit:"
    recycle_label = a.get("recycle_label") or "Does recycling help?"

    shelf = "".join(_c10_seg("ks3-stock-item", x["label"], x["id"] == start,
                             data_stock_item=x["id"]) for x in entries)
    outs = "".join(
        '<div class="ks3-stock-one" data-stock-out="%s"%s>'
        '<p class="ks3-stock-name">%s</p>'
        '<p class="ks3-stock-use">%s</p>'
        '<p class="ks3-stock-row"><strong>%s</strong> %s</p>'
        '<p class="ks3-stock-row"><strong>%s</strong> %s</p></div>'
        % (e(x["id"]), "" if x["id"] == start else " hidden",
           t(x["name"]), rich(x["use"]),
           t(limit_label), rich(x["limit"]),
           t(recycle_label), rich(x["recycle"]))
        for x in entries)

    return ('<div class="ks3-stock" data-stock data-total="%d" '
            'data-target="%d"><div class="ks3-stock-shelf">%s</div>'
            '<div class="ks3-stock-readout">%s</div></div>'
            % (len(entries), target, shelf, outs))


# ═══ c10-01 · earth-layers ═══════════════════════════════════════════════

# The two states a layer may be in. The set is closed on purpose: the bar
# paints the liquid one differently and the evidence section three blocks
# below rests entirely on there being a solid/liquid BOUNDARY to find, so a
# third value would be a colour nothing defines and a claim nothing checks.
_ELAY_STATES = ("solid", "liquid")


def _elay_share(thickness, total):
    """One layer's share of the distance from the surface to the centre.

    Printed as a number AND used as the bar's `flex-grow`, from the same
    expression, so the figure under the panel and the width above it cannot
    drift apart. §5A: the drawn geometry has to express the ratio it claims.
    """
    return 100.0 * float(thickness) / float(total)


def r_earth_layers(a, act_id):
    """⊕ c10-01 `#s-layers` — four layers, drawn from four thicknesses.

    FOUR REACHABLE STATES, ALL ENUMERATED, plus the scale panel that opens
    once every layer has been read. Each state carries the layer's name, its
    depth range, its state, its composition facts, its share of the depth and
    its note — and NOT ONE DEPTH, SHARE OR TOTAL IS AUTHORED.

    THE ARITHMETIC, ONCE. The payload gives four thicknesses. The boundary at
    the bottom of layer *n* is the running sum; the total is the whole sum;
    a layer's share is `thickness / total`. The bar's `flex-grow` is that same
    share, so the widths are the proportions rather than a drawing of them.

    ⚖️ **`radius` IS A CLAIM, AND IT IS CHECKED.** The lesson states the
    Earth's radius and the four thicknesses separately, and the build refuses
    a set whose thicknesses no longer sum to it. Without this, one edited
    thickness moves every boundary on the page, silently, and the caption
    under the bar goes on saying 6371 km because nothing joins the two.

    ⚖️ **`thinnest_claim` IS THE OTHER CLAIM, AND IT IS CHECKED TOO.** The
    lesson's prose calls the crust a sliver, a skin and a strip you can barely
    see, and the scale panel admits the bar draws it wider than it is. All of
    that is true only while one layer is in a different league from the rest,
    so the named layer must be the thinnest AND the next thinnest must be at
    least five times it. A payload that no longer supports the sentence fails
    the build instead of leaving the sentence standing over a bar that
    contradicts it.

    ⚠️ **THE ONE PLACE THE DRAWING IS NOT TO SCALE.** A segment at half of one
    per cent is under four pixels wide on a phone and is not a tappable
    target, so `.ks3-elay-seg` carries a `min-width` floor in
    `shared/ks3.css`. Only the thinnest layer is ever affected by it, and the
    scale panel says so in the same breath as it gives the true share — which
    is why `{thin_share}` is REQUIRED to appear in that panel's text.

    HOOKS: `data-elay` (wrapper, `data-total`, `data-target`) ·
    `data-elay-layer` · `data-elay-out` · `data-elay-scale`.
    """
    layers = a.get("layers") or []
    if len(layers) < 3:
        raise ValueError(
            "earth-layers %r has %d layer(s). The instrument is a comparison "
            "of proportions, and with fewer than three there is no set to "
            "read one against." % (act_id, len(layers)))
    _unique_ids(layers, act_id, "earth-layers", "layer")
    _no_correct_flags(layers, act_id, "earth-layers")

    seen_states = set()
    for l in layers:
        for key in ("label", "name", "note", "state_detail"):
            if not l.get(key):
                raise ValueError(
                    "earth-layers %r layer %r has no %r. Every one of them is "
                    "on the panel, and a missing one leaves a heading over "
                    "nothing." % (act_id, l.get("id"), key))
        if l.get("state") not in _ELAY_STATES:
            raise ValueError(
                "earth-layers %r layer %r has state %r, and the closed set is "
                "%s. The bar paints the liquid layer differently and the "
                "evidence section rests on there being a boundary between the "
                "two, so a third value is a claim nothing checks."
                % (act_id, l.get("id"), l.get("state"), list(_ELAY_STATES)))
        seen_states.add(l["state"])
        facts = l.get("facts") or []
        if len(facts) < 2 or any(len(f) != 2 for f in facts):
            raise ValueError(
                "earth-layers %r layer %r authors %d fact pair(s). The grid is "
                "label/value pairs and the panel is a composition readout, so "
                "two is the fewest that says anything."
                % (act_id, l.get("id"), len(facts)))
        if float(l.get("thickness") or 0) <= 0:
            raise ValueError(
                "earth-layers %r layer %r is %r %s thick. The thickness is "
                "what draws the bar and what every depth on the page is "
                "derived from." % (act_id, l.get("id"), l.get("thickness"),
                                   a.get("depth_unit") or "km"))
    if set(_ELAY_STATES) - seen_states:
        raise ValueError(
            "earth-layers %r has no %s layer. The whole evidence section "
            "below it turns on a wave that crosses one state and stops at the "
            "other, and a set that is all one state has nothing for it to "
            "have found."
            % (act_id, sorted(set(_ELAY_STATES) - seen_states)[0]))

    unit = a.get("depth_unit") or "km"
    total = sum(float(l["thickness"]) for l in layers)
    claimed = a.get("radius")
    if claimed is not None and int(round(total)) != int(claimed):
        raise ValueError(
            "earth-layers %r claims a radius of %s %s and its own thicknesses "
            "sum to %s. Every boundary, every share and the caption under the "
            "bar are derived from those thicknesses, so a set that no longer "
            "reaches the stated centre has quietly moved the whole planet."
            % (act_id, claimed, unit, int(round(total))))

    thin_id = a.get("thinnest_claim")
    if thin_id is not None:
        by_thickness = sorted(layers, key=lambda l: float(l["thickness"]))
        if by_thickness[0]["id"] != thin_id:
            raise ValueError(
                "earth-layers %r claims %r is the thinnest layer and its own "
                "figures make that %r. The lesson's prose calls the named "
                "layer a sliver you can barely see."
                % (act_id, thin_id, by_thickness[0]["id"]))
        if float(by_thickness[1]["thickness"]) < 5 * float(
                by_thickness[0]["thickness"]):
            raise ValueError(
                "earth-layers %r claims %r is a sliver, and the next thinnest "
                "layer is only %.1f times it. The page says skin, sliver and "
                "strip you can barely see, and admits the bar draws it wider "
                "than it is; none of that survives the two being the same "
                "order of size."
                % (act_id, thin_id,
                   float(by_thickness[1]["thickness"])
                   / float(by_thickness[0]["thickness"])))

    start = a.get("start_layer") or layers[0]["id"]
    if start not in [l["id"] for l in layers]:
        raise ValueError(
            "earth-layers %r opens on %r, which is not a layer on the bar. "
            "The opening state is what a student reads before touching "
            "anything." % (act_id, start))

    target = int(a.get("layers_to_tick") or 0)
    if not 2 <= target <= len(layers):
        raise ValueError(
            "earth-layers %r ticks its rail stop at %r of %d. Two is the "
            "fewest that is a comparison and more than the set is a stop that "
            "can never tick." % (act_id, target, len(layers)))

    scale = a.get("scale_panel") or {}
    scale_text = scale.get("text") or []
    if isinstance(scale_text, str):
        scale_text = [scale_text]
    if not scale.get("title") or not scale_text:
        raise ValueError(
            "earth-layers %r authors no scale panel title or text. The panel "
            "is the payoff of opening every layer, and an empty one is a "
            "reward for finishing that says nothing." % act_id)
    if not any("{thin_share}" in p for p in scale_text):
        raise ValueError(
            "earth-layers %r's scale panel never names {thin_share}. The bar "
            "draws the thinnest layer WIDER than its share, because half of "
            "one per cent of a screen is not a tappable target — so the true "
            "share has to be printed as a number in the one panel that talks "
            "about the scale, or the page is asserting a proportion it is "
            "visibly not drawing." % act_id)

    # ── the four states ──────────────────────────────────────────────────
    state_label = a.get("state_label") or "State"
    share_label = a.get("share_label") or "Share of the depth"

    segs, outs, top = [], [], 0.0
    shares = {}
    for l in layers:
        thickness = float(l["thickness"])
        bottom = top + thickness
        share = _elay_share(thickness, total)
        shares[l["id"]] = share
        depth = "%d %s %d %s" % (int(round(top)), "–",
                                 int(round(bottom)), unit)
        pressed = l["id"] == start

        # The accessible name carries the same three numbers the panel does,
        # spoken rather than punctuated: a screen reader gets the depth and
        # the proportion without having to open the panel to find them.
        segs.append(
            '<button type="button" class="ks3-elay-seg%s" data-elay-layer="%s"'
            ' aria-pressed="%s" aria-label="%s" style="flex-grow:%.4f">'
            '<span class="ks3-elay-slabel">%s</span></button>'
            % (" ks3-elay-liquid" if l["state"] == "liquid" else "",
               e(l["id"]), "true" if pressed else "false",
               e("%s, %d to %d %s down, %.1f%% of the way to the centre"
                 % (l["name"], int(round(top)), int(round(bottom)), unit,
                    share)),
               share, t(l["label"])))

        cards = [(state_label, l["state_detail"])]
        cards += [(f[0], f[1]) for f in l["facts"]]
        cards += [(share_label, "%.1f%%" % share)]
        facts_html = "".join(
            '<div class="ks3-elay-fact">'
            '<p class="ks3-elay-flabel">%s</p>'
            '<p class="ks3-elay-fvalue">%s</p></div>' % (t(lab), t(val))
            for lab, val in cards)

        outs.append(
            '<div class="ks3-elay-one" data-elay-out="%s"%s>'
            '<div class="ks3-elay-head">'
            '<p class="ks3-elay-name">%s</p>'
            '<p class="ks3-elay-depth">%s</p></div>'
            '<div class="ks3-elay-facts">%s</div>'
            '<p class="ks3-elay-note">%s</p></div>'
            % (e(l["id"]), "" if pressed else " hidden",
               t(l["name"]), t(depth), facts_html, rich(l["note"])))
        top = bottom

    thin = min(layers, key=lambda l: float(l["thickness"]))
    fills = {"{thin_name}": thin["name"].lower(),
             "{thin_share}": "%.1f%%" % shares[thin["id"]],
             "{total}": "%d" % int(round(total)),
             "{unit}": unit}

    def _fill(text):
        for k, v in fills.items():
            text = text.replace(k, v)
        return text

    ends = "".join(
        '<p class="ks3-elay-end">%s</p>' % t(_fill(a.get(key) or ""))
        for key in ("surface_label", "centre_label") if a.get(key))

    scale_html = (
        '<div class="ks3-elay-scale" data-elay-scale hidden>'
        '<p class="ks3-elay-stitle">%s</p>%s</div>'
        % (t(scale["title"]),
           "".join('<p class="ks3-elay-stext">%s</p>' % rich(_fill(p))
                   for p in scale_text)))

    return ('<div class="ks3-elay" data-elay data-total="%d" '
            'data-target="%d"><div class="ks3-elay-bar">%s</div>'
            '<div class="ks3-elay-ends">%s</div>'
            '<div class="ks3-elay-readout">%s</div>%s</div>'
            % (len(layers), target, "".join(segs), ends, "".join(outs),
               scale_html))


# ═══ c10-01 · depth-evidence ═════════════════════════════════════════════

def r_depth_evidence(a, act_id):
    """⊕ c10-01 `#s-evidence` — three inferences, each committed to first.

    A commit-then-read set: a question, three readings of it, and the answer
    underneath, hidden until the student has picked one. NOTHING IS MARKED —
    every option opens the same answer, because what the block is for is
    making the student say what they think BEFORE the page says what is known,
    and a green tick would turn three inferences into three guesses with a
    score attached.

    ⚖️ **THREE READINGS, NOT TWO.** A two-option commitment is a coin flip and
    measures nothing, so the build refuses one. The third reading is what
    makes committing a decision rather than a toss.

    ⚠️ **THE CHOSEN BUTTON STAYS ENABLED; THE OTHERS DO NOT.** Design disables
    all three the moment one is pressed. That drops a keyboard user to
    `<body>` — the element they are standing on is disabled underneath them —
    which is MRB-257's finding reached by a different route. Disabling the
    two NOT chosen locks the commitment just as firmly, keeps focus on a live
    control, and is visually what Design drew anyway: her own `seg(on, dis)`
    dims a spent button only when it is not the chosen one.

    Nothing is disabled in the BYTES: the resting page has nothing chosen, so
    every button opens live and `shared/ks3.js` does the locking.

    HOOKS: `data-edep` (wrapper, `data-total`, `data-target`) ·
    `data-edep-pick` (valued `entry:choice`, with `data-edep-of`) ·
    `data-edep-answer`.
    """
    entries = a.get("entries") or []
    if len(entries) < 2:
        raise ValueError(
            "depth-evidence %r has %d entr(y/ies). The block's claim is that "
            "the structure was worked out from SEVERAL independent readings, "
            "and one reading is an assertion." % (act_id, len(entries)))
    _unique_ids(entries, act_id, "depth-evidence", "entry")
    _no_correct_flags(entries, act_id, "depth-evidence")

    for x in entries:
        for key in ("q", "answer"):
            if not x.get(key):
                raise ValueError(
                    "depth-evidence %r entry %r has no %r. The question is "
                    "what is committed to and the answer is what the "
                    "commitment buys." % (act_id, x.get("id"), key))
        choices = x.get("choices") or []
        if len(choices) < 3:
            raise ValueError(
                "depth-evidence %r entry %r offers %d reading(s). Two is a "
                "coin flip, and a commitment a student can make by tossing a "
                "coin is not a commitment." % (act_id, x["id"], len(choices)))
        _unique_ids(choices, act_id, "depth-evidence", "choice")
        _no_correct_flags(choices, act_id, "depth-evidence")
        for c in choices:
            if not c.get("label"):
                raise ValueError(
                    "depth-evidence %r entry %r has a reading with no label — "
                    "a blank button." % (act_id, x["id"]))

    target = int(a.get("entries_to_tick") or 0)
    if not 2 <= target <= len(entries):
        raise ValueError(
            "depth-evidence %r ticks its rail stop at %r of %d. Two is the "
            "fewest that is a pattern and more than the set is a stop that "
            "can never tick." % (act_id, target, len(entries)))

    cards = []
    for x in entries:
        picks = "".join(
            _c10_seg("ks3-edep-choice", c["label"], False,
                     data_edep_pick="%s:%s" % (x["id"], c["id"]),
                     data_edep_of=x["id"])
            for c in x["choices"])
        cards.append(
            '<div class="ks3-edep-one">'
            '<p class="ks3-edep-q">%s</p>'
            '<div class="ks3-edep-picks">%s</div>'
            '<p class="ks3-edep-answer" data-edep-answer="%s" hidden>%s</p>'
            '</div>' % (rich(x["q"]), picks, e(x["id"]), rich(x["answer"])))

    return ('<div class="ks3-edep" data-edep data-total="%d" '
            'data-target="%d">%s</div>'
            % (len(entries), target, "".join(cards)))


# ═══ c10-02 · rock-bench ═════════════════════════════════════════════════

# Small counts written as words, because the two sentences this instrument
# derives are prose ("Two of these six...") and "2 of these 6" in the middle of
# a paragraph reads as a spreadsheet. Nine is more than any bench will hold.
_ROCKB_WORDS = ("zero", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine")


def _rockb_word(n):
    return _ROCKB_WORDS[n] if 0 <= n < len(_ROCKB_WORDS) else str(n)


def r_rock_bench(a, act_id):
    """⊕ c10-02 `#s-bench` — six samples, three groups, one decision each.

    EIGHTEEN REACHABLE VERDICTS, ALL ENUMERATED (six samples × three groups),
    every one of them in the document from the moment the page loads and
    exactly one of them unhidden per decided sample. `shared/ks3.js` chooses
    which; it composes nothing.

    ⚖️ **THE VERDICT IS TWO TEMPLATES, NOT EIGHTEEN SENTENCES.** The payload
    authors `verdict_right` and `verdict_wrong` once and this fills `{choice}`
    and `{answer}` from the group's own label, lower-cased, per branch. A
    per-panel sentence would let two samples in the same group be marked with
    different words, which on a classification bench is the page disagreeing
    with itself about what the group is called.

    ⚖️ **THE "TWO OF THESE SIX" CLAIM IS DERIVED AND CHECKED, NOT TYPED.** The
    lesson says twice — once over the bench and once in the panel that opens
    at the end — that two of the samples are the same chemical compound as
    each other and are in different groups. That is the sentence the whole
    lesson turns on (marble and limestone are both calcium carbonate), so it
    is not allowed to be a number an author remembered. Samples carry
    `compound`; this counts the ones that share theirs with another sample,
    refuses a payload where none do, and refuses one where the sharers all sit
    in the SAME group — which would leave both sentences standing over a bench
    that no longer makes the point.

    ⚖️ **EVERY GROUP MUST BE SOME SAMPLE'S ANSWER.** A button that is never
    right is MRB-278's defect wearing a bench's clothes: a three-way choice a
    student can play as a two-way one.

    ⚠️ **THE CHOSEN BUTTON STAYS ENABLED; THE OTHER TWO DO NOT.** Design
    disables all three the moment one is pressed, which disables the element a
    keyboard user is standing on and drops them to `<body>` — MRB-257's
    finding, and `c10-01`'s `depth-evidence` reached it by the same route.
    Locking the two NOT chosen closes the decision just as firmly and is what
    her own `seg(on, dis)` draws anyway: a spent button is dimmed only when it
    is not the one that was pressed.

    Nothing is disabled in the BYTES and nothing is decided in them: the
    resting page opens with six live rows, a counter at zero and the pattern
    panel hidden, which is the on-load state modelled rather than assumed.

    HOOKS: `data-rockb` (wrapper, `data-total`, `data-target`) ·
    `data-rockb-row` · `data-rockb-pick` (valued `sample:group`, with
    `data-rockb-of`) · `data-rockb-out` (valued `sample:group`) ·
    `data-rockb-pattern`.
    """
    samples = a.get("samples") or []
    groups = a.get("groups") or []

    if len(samples) < 4:
        raise ValueError(
            "rock-bench %r has %d sample(s). The bench's claim is that one "
            "clue rarely closes a classification, and that needs enough "
            "samples for the clues to cut across each other."
            % (act_id, len(samples)))
    if len(groups) < 3:
        raise ValueError(
            "rock-bench %r offers %d group(s). Two is a coin flip, and a "
            "classification a student can make by tossing a coin measures "
            "nothing." % (act_id, len(groups)))
    _unique_ids(samples, act_id, "rock-bench", "sample")
    _unique_ids(groups, act_id, "rock-bench", "group")
    _no_correct_flags(samples + groups, act_id, "rock-bench")

    by_group = {}
    for g in groups:
        if not g.get("label"):
            raise ValueError(
                "rock-bench %r group %r has no label — a blank button."
                % (act_id, g.get("id")))
        by_group[g["id"]] = g

    for s in samples:
        for key in ("code", "found", "why"):
            if not s.get(key):
                raise ValueError(
                    "rock-bench %r sample %r has no %r. The code names the "
                    "row, the find names where it came from and the why is "
                    "what the decision buys — a missing one leaves a heading "
                    "over nothing." % (act_id, s.get("id"), key))
        facts = s.get("facts") or []
        if len(facts) < 2:
            raise ValueError(
                "rock-bench %r sample %r lists %d observation(s). One "
                "observation is not evidence a student can weigh; it is a "
                "label with the answer in it."
                % (act_id, s["id"], len(facts)))
        if s.get("answer") not in by_group:
            raise ValueError(
                "rock-bench %r sample %r answers %r, which is not a group on "
                "the bench (%s)."
                % (act_id, s["id"], s.get("answer"), sorted(by_group)))

    unused = [g["id"] for g in groups
              if not any(s["answer"] == g["id"] for s in samples)]
    if unused:
        raise ValueError(
            "rock-bench %r offers group(s) %s that no sample belongs to. A "
            "button that is never the answer turns a %d-way decision into a "
            "%d-way one, which is MRB-278's defect at a bench."
            % (act_id, unused, len(groups), len(groups) - len(unused)))

    # ── the shared-compound claim, derived and checked ───────────────────
    counts = {}
    for s in samples:
        if s.get("compound"):
            counts.setdefault(s["compound"], []).append(s)
    sharers = [s for c, rows in counts.items() if len(rows) > 1 for s in rows]
    if not sharers:
        raise ValueError(
            "rock-bench %r has no two samples sharing a `compound`. The "
            "lesson says twice — over the bench and in the panel that opens "
            "at the end — that two of these are the same compound and are in "
            "different groups, and neither sentence is authored as a number: "
            "both are derived from this. A bench with no shared compound "
            "leaves both sentences standing over a set that cannot support "
            "them." % act_id)
    for compound, rows in sorted(counts.items()):
        if len(rows) > 1 and len({r["answer"] for r in rows}) < 2:
            raise ValueError(
                "rock-bench %r puts every sample made of %r in the group %r. "
                "The whole point of the shared compound is that what a rock "
                "is MADE OF does not decide its group, and a set that agrees "
                "with itself teaches the opposite."
                % (act_id, compound, rows[0]["answer"]))

    # `{N}` is the same derived word with a capital, because both sentences
    # that quote it OPEN with it. Without it the note ships "two of these six
    # …" mid-paragraph-cased at the start of its own paragraph, and the only
    # alternatives are capitalising the whole filled string (which would also
    # capitalise a slot used mid-sentence) or authoring the number.
    fills = {"{n}": _rockb_word(len(sharers)),
             "{N}": _rockb_word(len(sharers)).capitalize(),
             "{total}": _rockb_word(len(samples))}

    def _fill(text):
        for k, v in fills.items():
            text = text.replace(k, v)
        return text

    note = a.get("shared_note") or ""
    if note and not (("{n}" in note or "{N}" in note) and "{total}" in note):
        raise ValueError(
            "rock-bench %r's shared_note %r names no count slot ({n} or {N}) "
            "or does not name {total}. Both are facts about the payload "
            "rather than numbers an author chose, and a sentence that "
            "hard-codes one of them goes on saying it after the bench has "
            "changed." % (act_id, note))

    right = a.get("verdict_right") or ""
    wrong = a.get("verdict_wrong") or ""
    if "{choice}" not in right:
        raise ValueError(
            "rock-bench %r's verdict_right %r never names {choice}. The "
            "student has just pressed a button and the sentence has to say "
            "which one." % (act_id, right))
    if "{answer}" not in wrong:
        raise ValueError(
            "rock-bench %r's verdict_wrong %r never names {answer}. A wrong "
            "decision that is not told what the answer is has been marked and "
            "not taught." % (act_id, wrong))

    target = int(a.get("samples_to_tick") or 0)
    if not 2 <= target <= len(samples):
        raise ValueError(
            "rock-bench %r ticks its rail stop at %r of %d. Two is the fewest "
            "that is a pattern and more than the set is a stop that can never "
            "tick." % (act_id, target, len(samples)))

    panel = a.get("pattern_panel") or {}
    panel_text = panel.get("text") or []
    if isinstance(panel_text, str):
        panel_text = [panel_text]
    if not panel.get("title") or not panel_text:
        raise ValueError(
            "rock-bench %r authors no pattern panel title or text. The panel "
            "is the payoff of deciding every sample, and an empty one is a "
            "reward for finishing that says nothing." % act_id)

    # ── the six rows, each carrying all three of its verdicts ────────────
    rows = []
    for s in samples:
        picks = "".join(
            _c10_seg("ks3-rockb-pick", g["label"], False,
                     aria_label="%s — %s" % (s["code"], g["label"]),
                     data_rockb_pick="%s:%s" % (s["id"], g["id"]),
                     data_rockb_of=s["id"])
            for g in groups)

        answer_word = by_group[s["answer"]]["label"].lower()
        outs = "".join(
            '<div class="ks3-rockb-out" data-rockb-out="%s" hidden>'
            '<p class="ks3-rockb-verdict">%s</p>'
            '<p class="ks3-rockb-why">%s</p></div>'
            % (e("%s:%s" % (s["id"], g["id"])),
               t((right if g["id"] == s["answer"] else wrong)
                 .replace("{choice}", g["label"].lower())
                 .replace("{answer}", answer_word)),
               rich(s["why"]))
            for g in groups)

        rows.append(
            '<div class="ks3-rockb-row" data-rockb-row="%s">'
            '<div class="ks3-rockb-head">'
            '<p class="ks3-rockb-code">%s</p>'
            '<p class="ks3-rockb-found">%s</p></div>'
            '<ul class="ks3-rockb-facts">%s</ul>'
            '<div class="ks3-rockb-picks">%s</div>%s</div>'
            % (e(s["id"]), t(s["code"]), t(s["found"]),
               "".join("<li>%s</li>" % rich(f) for f in s["facts"]),
               picks, outs))

    pattern = (
        '<div class="ks3-rockb-pattern"%s data-rockb-pattern hidden>'
        '<p class="ks3-rockb-ptitle">%s</p>%s</div>'
        % ((' id="%s"' % e(a["pattern_anchor"])) if a.get("pattern_anchor")
           else "",
           t(panel["title"]),
           "".join('<p class="ks3-rockb-ptext">%s</p>' % rich(_fill(p))
                   for p in panel_text)))

    head = ('<p class="ks3-rockb-note">%s</p>' % rich(_fill(note))) if note \
        else ""

    return ('<div class="ks3-rockb" data-rockb data-total="%d" '
            'data-target="%d">%s<div class="ks3-rockb-list">%s</div>%s</div>'
            % (len(samples), target, head, "".join(rows), pattern))


# ═══ c10-03 · grain-journey ══════════════════════════════════════════════
#
# ⚠️ `_rockb_word` ABOVE IS C10'S NUMBER-WORD HELPER, not the bench's — the
# prefix records where it was first needed. Both instruments below quote a
# count in a drawn sentence, and both check that sentence against their own
# payload rather than trusting it.


def _c10_count_word_agrees(text, n, act_id, family, where):
    """Refuse a drawn sentence whose number word disagrees with the payload.

    §5A forbids hard-coding a figure the instrument computes. Design types the
    size of both sets into her own headings — "Seven stages, shuffled" and
    "the six processes" — and those are HER words, so they ship. What must not
    ship is those words surviving an edit to the payload underneath them: a
    seventh process added to `processes` would leave the eyebrow saying six,
    on the page, with every gate green.

    So the number is not authored twice; it is authored once and the sentence
    is CHECKED against it. A heading naming no count is fine — nothing to
    disagree with.

    ⚠️ ONLY "three" TO "nine" COUNT AS COUNTS, and that is a real limit rather
    than an oversight. "One" and "two" are ordinary English words long before
    they are numbers — Design's own heading here reads "Tap a process. Each
    ONE is an arrow on the diagram", which is not a claim about the size of
    anything — and a check that read them as counts would fail a correct page
    on a pronoun. Both instruments in this unit refuse a payload smaller than
    four, so nothing checkable is lost by the narrowing.
    """
    words = re.findall(r"[a-z]+", (text or "").lower())
    want = _rockb_word(n)
    countable = _ROCKB_WORDS[3:]
    found = [w for w in words if w in countable]
    if found and want not in found:
        raise ValueError(
            "%s %r: the %s says %r but the payload holds %d. The count is a "
            "fact about the payload, not a number an author chose, and a "
            "sentence that disagrees with it goes on saying so after the set "
            "has changed." % (family, act_id, where, found[0], n))


def _c10_head_agrees(a, act_id, family, total, start):
    """The block's head counter is DERIVED FROM THE PAYLOAD, then checked.

    `head_counter` is rendered by the shell in `build_ks3.py`, which never
    sees the instrument's payload, so its `total` and `start` have to be
    authored on the block. Authoring a number the instrument owns is exactly
    what §5A forbids, so both are asserted here: `total` is the size of the
    set and `start` is how many panels the RESTING page has open. A payload
    that gains a row and a counter that does not is a denominator that lies.
    """
    hc = a.get("head_counter")
    if not hc:
        return
    if int(hc.get("total") or 0) != total:
        raise ValueError(
            "%s %r: head_counter counts to %r and the payload holds %d. The "
            "denominator is a fact about the set."
            % (family, act_id, hc.get("total"), total))
    if int(hc.get("start") or 0) != start:
        raise ValueError(
            "%s %r: head_counter opens at %r and the resting page opens with "
            "%d open. The opening number is what the HTML already shows, not "
            "a number an author chose."
            % (family, act_id, hc.get("start"), start))


def r_grain_journey(a, act_id):
    """⊕ c10-03 `#s-journey` — one grain, seven stages, put them in order.

    A SEQUENCER, and the only one in C10. The student taps the stages in the
    order they think they happen; the badge on each row records the position
    it was placed in, and when the set is full the panel underneath opens with
    the journey in its real order and the name of every stage.

    ⚖️ **THE TWO VERDICTS ARE BOTH IN THE DOCUMENT AND ONE IS UNHIDDEN.** The
    handler in `shared/ks3.js` compares the ranks this renderer emitted
    against the positions the student pressed them in and chooses which of two
    AUTHORED sentences stops being `hidden`. It composes nothing, and the list
    of stages under it is the same list either way — the order is the answer,
    so it is printed in full whether the student got it or not. A wrong order
    that is only told it is wrong has been marked and not taught.

    ⚖️ **THE CYCLE CLOSING IS DERIVED AND CHECKED, NOT TYPED.** The closing
    sentence says the rock at the end is the rock at the beginning, which is
    the whole reason this is a cycle and not a list. It is not allowed to be a
    word an author remembered: the first and last stage each carry `rock`,
    `{rock}` in `close` is filled from them, and a payload whose journey does
    not return to where it started fails the build rather than shipping a
    sentence that is no longer true of it.

    ⚠️ **A PLACED ROW STAYS ENABLED.** Design sets `disabled` on it, which
    disables the element the student has just pressed and drops a keyboard
    user to `<body>` — MRB-257's finding, and `depth-evidence` and
    `rock-bench` both reached it by the same route. A second press is a
    genuine no-op instead, and nothing is lost visually: her placed row is LIT
    (accent border, accent tint, accent badge), not dimmed, so the two look
    identical.

    Nothing is placed in the BYTES: the resting page opens with every row
    live, every badge empty, the counter at zero and the panel hidden, which
    is the on-load state modelled rather than assumed.

    HOOKS: `data-grain` (wrapper, `data-total`, `data-target`) ·
    `data-grain-pick` (valued with the stage id, with `data-grain-rank`) ·
    `data-grain-badge` · `data-grain-reset` · `data-grain-panel` ·
    `data-grain-verdict` (valued `right` / `wrong`).
    """
    stages = a.get("stages") or []
    shuffled = list(a.get("shuffled") or [])

    if len(stages) < 4:
        raise ValueError(
            "grain-journey %r has %d stage(s). A cycle a student can put in "
            "order needs enough stages for the order to be a decision rather "
            "than a guess." % (act_id, len(stages)))
    ids = _unique_ids(stages, act_id, "grain-journey", "stage")
    _no_correct_flags(stages, act_id, "grain-journey")

    for s in stages:
        for key in ("text", "why"):
            if not s.get(key):
                raise ValueError(
                    "grain-journey %r stage %r has no %r. The text is the row "
                    "a student presses and the why is the name of the process "
                    "— a missing one is a button with nothing behind it."
                    % (act_id, s.get("id"), key))
    texts = [s["text"] for s in stages]
    if len(set(texts)) != len(texts):
        raise ValueError(
            "grain-journey %r repeats a stage's text. Two rows that read the "
            "same are two rows a student cannot order." % act_id)

    if sorted(shuffled) != sorted(ids):
        raise ValueError(
            "grain-journey %r shuffles %s over stages %s. The display order "
            "must be exactly the stages, every one of them once, or a stage "
            "is either unreachable or offered twice."
            % (act_id, shuffled, ids))
    if shuffled == ids:
        raise ValueError(
            "grain-journey %r displays the stages in their answer order. "
            "There is nothing to put in order." % act_id)

    # ── the cycle closes, derived from the payload's own ends ────────────
    first, last = stages[0].get("rock"), stages[-1].get("rock")
    if not first or not last:
        raise ValueError(
            "grain-journey %r: the first and last stage must each name the "
            "`rock` the grain is in. The closing sentence says the journey "
            "comes back to where it started and fills its name from these; "
            "without them the claim is a word an author remembered."
            % act_id)
    if first != last:
        raise ValueError(
            "grain-journey %r starts in %r and ends in %r, so the journey "
            "does not close. This block is what makes the cycle a cycle, and "
            "a set that does not return to its own beginning teaches the "
            "opposite." % (act_id, first, last))

    close = a.get("close") or ""
    if "{rock}" not in close:
        raise ValueError(
            "grain-journey %r's close %r never names {rock}. The sentence's "
            "whole claim is that the rock at the end is the rock at the "
            "beginning, and hard-coding the name lets the payload change "
            "under it." % (act_id, close))

    right = a.get("verdict_right") or ""
    wrong = a.get("verdict_wrong") or ""
    if not right or not wrong:
        raise ValueError(
            "grain-journey %r authors no verdict_right or verdict_wrong. Both "
            "are in the document from the moment the page loads and the "
            "runtime chooses between them; a blank one is a student who "
            "finishes and is told nothing." % act_id)
    if right == wrong:
        raise ValueError(
            "grain-journey %r gives the same verdict either way, which tells "
            "a student who got the order right nothing they did not already "
            "know." % act_id)

    _c10_count_word_agrees(a.get("heading"), len(stages), act_id,
                           "grain-journey", "heading")
    _c10_head_agrees(a, act_id, "grain-journey", len(stages), 0)

    rank = dict((sid, i) for i, sid in enumerate(ids))
    by_id = dict((s["id"], s) for s in stages)

    rows = "".join(
        '<li><button type="button" class="ks3-grain-step" '
        'data-grain-pick="%s" data-grain-rank="%d" aria-pressed="false">'
        '<span class="ks3-grain-badge" data-grain-badge aria-hidden="true">'
        '</span><span class="ks3-grain-text">%s</span></button></li>'
        % (e(sid), rank[sid], rich(by_id[sid]["text"]))
        for sid in shuffled)

    answer = "".join('<li><strong>%s</strong> — %s</li>'
                     % (rich(s["text"]), rich(s["why"])) for s in stages)

    reset = a.get("reset_label") or "Start the order again"

    return ('<div class="ks3-grain" data-grain data-total="%d" '
            'data-target="%d">'
            '<ol class="ks3-grain-list">%s</ol>'
            '<div class="ks3-grain-tools">'
            '<button type="button" class="ks3-grain-reset" data-grain-reset>'
            '%s</button></div>'
            '<div class="ks3-grain-panel" data-grain-panel hidden>'
            '<p class="ks3-grain-verdict" data-grain-verdict="right" hidden>'
            '%s</p>'
            '<p class="ks3-grain-verdict" data-grain-verdict="wrong" hidden>'
            '%s</p>'
            '<ol class="ks3-grain-answer">%s</ol>'
            '<p class="ks3-grain-close">%s</p></div></div>'
            % (len(stages), len(stages), rows, t(reset), t(right), t(wrong),
               answer, rich(close.replace("{rock}", first))))


# ═══ c10-03 · process-arrows ═════════════════════════════════════════════

# Design's arrow between the two ends of a route. DRAWN, never typed: the
# fonts in `shared/fonts/` carry no U+2192, which is why `kit.MARKS` exists at
# all — and this one is wider than the 1em mark, because it spans a gap
# between two display-weight phrases rather than sitting inside a sentence.
_PARROW_SVG = ('<svg class="ks3-parrow-arrow" viewBox="0 0 44 24" width="44" '
               'height="24" aria-hidden="true"><path '
               'd="M4 12h30M26 5l8 7-8 7" fill="none" stroke="currentColor" '
               'stroke-width="2.6" stroke-linecap="round" '
               'stroke-linejoin="round"></path></svg>')


def r_process_arrows(a, act_id):
    """⊕ c10-03 `#s-processes` — six processes, six arrows, one open at a time.

    The reference half of the lesson. Each process is one arrow on the rock
    cycle: what it takes in, what it turns that into, what it actually does,
    and how long it takes. Every panel is in the document from the moment the
    page loads and `shared/ks3.js` chooses which one is `hidden`.

    ⚖️ **THE RAIL STOP TICKS AT FOUR OF SIX, WHICH IS DESIGN'S OWN NUMBER.**
    Her `DONE('s-processes')` is `Object.keys(s.seen).length >= 4` while the
    set is six, and it is not a slip: the block is a REFERENCE a student keeps
    open, and requiring all six would make the stop a reading receipt rather
    than a record of having used it. `processes_to_open` carries it, and it is
    checked against the set rather than assumed.

    ⚠️ **THIS BLOCK DOES NOT OPEN EMPTY**, which it shares with `c10-04`'s two
    benches and not with `c10-01`'s or `c10-02`'s. Design opens on the first
    process with its panel showing, so the build emits that button
    `aria-pressed="true"` and that panel unhidden — the resting HTML and the
    runtime then agree, rather than agreeing one frame later. MRB-208 is
    untouched: what may not be ticked on load is the RAIL STOP, and
    `data-stage-done` still opens at 0.

    ⚠️ **NOTHING IS DISABLED AND NOTHING IS MARKED.** Every button stays live
    for the whole block, a press on the open process is a genuine no-op, and
    the panel gives its answer in words. `_no_correct_flags` refuses a payload
    that tries to mark one.

    HOOKS: `data-parrow` (wrapper, `data-total`, `data-target`) ·
    `data-parrow-pick` (valued with the process id) · `data-parrow-out`
    (valued with the process id).
    """
    procs = a.get("processes") or []

    if len(procs) < 4:
        raise ValueError(
            "process-arrows %r has %d process(es). The claim the block is "
            "making is that there are many routes between the three rock "
            "types, and a handful of arrows cannot make it."
            % (act_id, len(procs)))
    _unique_ids(procs, act_id, "process-arrows", "process")
    _no_correct_flags(procs, act_id, "process-arrows")

    for p in procs:
        for key in ("label", "name", "from", "to", "note", "time"):
            if not p.get(key):
                raise ValueError(
                    "process-arrows %r process %r has no %r. The label names "
                    "the button, the name and the two ends are the arrow, the "
                    "note is what the process does and the time is what stops "
                    "the cycle reading as a schedule — a missing one leaves a "
                    "panel with a hole in it." % (act_id, p.get("id"), key))
        if p["from"] == p["to"]:
            raise ValueError(
                "process-arrows %r process %r goes from %r to %r. An arrow "
                "that ends where it started is not a process."
                % (act_id, p["id"], p["from"], p["to"]))

    labels = [p["label"] for p in procs]
    if len(set(labels)) != len(labels):
        raise ValueError(
            "process-arrows %r repeats a button label in %s. Two buttons that "
            "read the same are one process a student can never reach."
            % (act_id, labels))

    target = int(a.get("processes_to_open") or 0)
    if not 2 <= target <= len(procs):
        raise ValueError(
            "process-arrows %r ticks its rail stop at %r of %d. Two is the "
            "fewest that is more than the one already open, and more than the "
            "set is a stop that can never tick."
            % (act_id, target, len(procs)))

    _c10_count_word_agrees(a.get("eyebrow"), len(procs), act_id,
                           "process-arrows", "eyebrow")
    _c10_count_word_agrees(a.get("heading"), len(procs), act_id,
                           "process-arrows", "heading")
    # One panel is open in the resting bytes, so the counter opens at one.
    _c10_head_agrees(a, act_id, "process-arrows", len(procs), 1)

    picks = "".join(
        _c10_seg("ks3-parrow-pick", p["label"], i == 0,
                 data_parrow_pick=p["id"])
        for i, p in enumerate(procs))

    panels = "".join(
        '<div class="ks3-parrow-panel" data-parrow-out="%s"%s>'
        '<p class="ks3-parrow-name">%s</p>'
        '<p class="ks3-parrow-route"><span>%s</span>%s<span>%s</span></p>'
        '<p class="ks3-parrow-note">%s</p>'
        '<p class="ks3-parrow-time">%s</p></div>'
        % (e(p["id"]), "" if i == 0 else " hidden", t(p["name"]),
           t(p["from"]), _PARROW_SVG, t(p["to"]), rich(p["note"]),
           t(p["time"]))
        for i, p in enumerate(procs))

    return ('<div class="ks3-parrow" data-parrow data-total="%d" '
            'data-target="%d"><div class="ks3-parrow-picks">%s</div>%s</div>'
            % (len(procs), target, picks, panels))


# ═══ c10-05 · air-mix ════════════════════════════════════════════════════
#
# ⚠️ WHAT HAPPENS TO A GAS IN A PAIR OF LUNGS is a CLOSED SET, and it is closed
# because the block's lead sentence is derived from it. Design writes "Two of
# these four are gases that do nothing at all in your body"; the two are
# nitrogen and argon, and the reason carbon dioxide is not a third is that you
# breathe out far more of it than you breathed in. A fourth value would be a
# category the lead sentence cannot count.
_AMIX_LUNGS = ("absorbed", "unchanged", "added")


def _amix_pct(v):
    """A share printed at the precision it was authored to, and no further.

    78 → "78%", 0.9 → "0.9%", 0.04 → "0.04%", 78.9 → "78.9%". One formatter for
    every printed percentage on the block — the panel's, the lead's and the
    scale note's — so a figure cannot be rounded one way in a sentence and
    another way in the readout above it.
    """
    v = float(v)
    if abs(v - round(v)) < 1e-9:
        return "%d%%" % int(round(v))
    if v >= 1:
        return "%.1f%%" % v
    return ("%.2f" % v).rstrip("0").rstrip(".") + "%"


def _c10_join(items):
    """"argon and carbon dioxide" — a list read as a sentence, not as a list.

    The scale note names the gases the bar cannot draw honestly, and that set
    is DERIVED, so the sentence has to be built from however many there turn
    out to be rather than from however many there are today.
    """
    items = [x for x in items if x]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " and " + items[-1]


def r_air_mix(a, act_id):
    """⊕ c10-05 `#s-mix` — four gases, a bar drawn from their shares.

    FOUR REACHABLE STATES, ALL ENUMERATED. Each carries the gas's name, its
    share, and its note — and NOT ONE PERCENTAGE IS PRINTED AS AUTHORED. The
    payload states four shares; every figure on the page, every bar width and
    both derived sentences are computed here.

    THE ARITHMETIC, ONCE. A gas's `pct` is its `flex-grow` on a bar whose items
    have `flex-basis: 0`, so the widths ARE the proportions rather than a
    drawing of them. The same number is formatted into the panel's readout and
    into the button's accessible name, from `_amix_pct`, so the bar and the
    caption cannot drift apart.

    ⚖️ **`accounts_for` IS A CLAIM, AND IT IS CHECKED.** The explainer above
    the block says almost all of the air is just a few gases. That is true of
    78 + 21 + 0.9 + 0.04, and it would stop being true if a gas were removed
    from the set. The build refuses a payload whose shares no longer reach the
    claimed floor, and refuses one that exceeds 100 per cent — which is the
    other way the same edit goes wrong.

    ⚖️ **THE LEAD SENTENCE IS DERIVED FROM `lungs`, NOT AUTHORED.** Design
    writes "Two of these four ... together they are 79 per cent of every
    breath", and both numbers are facts about the payload. Each gas declares
    what happens to it in a pair of lungs; this counts the ones that come back
    out unchanged and adds their shares. A payload that gained a fifth gas
    would move both numbers, and the sentence would move with them.

    ⚠️ **THE ONE PLACE THE DRAWING IS NOT TO SCALE.** Argon is 0.9% of the air
    and carbon dioxide is 0.04%. At any width that makes nitrogen readable
    those two are a hairline and a sub-pixel, and neither is a tappable target,
    so `.ks3-amix-seg` carries a `min-width` floor in `shared/ks3.css` — the
    same solution `c10-01`'s crust segment takes, reused rather than
    reinvented. The floored gases and their TRUE combined share are therefore
    derived here and the block REFUSES a `scale_note` that does not name both.
    A distortion a page admits to is a scale lesson; the same distortion
    unremarked is the misconception being taught.

    ⚠️ **AND `dry_note` IS REQUIRED.** MRB-225: the 78/21 figures are for DRY
    air, and the reason they are quoted dry is that water vapour is variable.
    Four percentages with no qualifier teach a student that the air has a fixed
    recipe — which is the belief the lesson's own key fact is trying to break,
    arriving four lines later by the back door. A block that cannot say so does
    not build.

    ⚠️ **THIS BLOCK DOES NOT OPEN EMPTY.** Design opens on nitrogen with its
    panel showing, so the build emits that button `aria-pressed="true"` and
    that panel unhidden — the resting HTML and the runtime then agree rather
    than agreeing one frame later. MRB-208 is untouched: what may not be ticked
    on load is the RAIL STOP, and `data-stage-done` still opens at 0. There is
    no zero state to model: a gas is always selected, which is what makes the
    resting page a readout rather than a blank.

    HOOKS: `data-amix` (wrapper, `data-total`, `data-target`) ·
    `data-amix-gas` · `data-amix-out`.
    """
    gases = a.get("gases") or []
    if len(gases) < 3:
        raise ValueError(
            "air-mix %r has %d gas(es). The block is a comparison of "
            "proportions, and with fewer than three there is no set to read "
            "one against." % (act_id, len(gases)))
    _unique_ids(gases, act_id, "air-mix", "gas")
    _no_correct_flags(gases, act_id, "air-mix")

    seen_lungs = set()
    for g in gases:
        for key in ("label", "name", "note"):
            if not g.get(key):
                raise ValueError(
                    "air-mix %r gas %r has no %r. The label is the strip on "
                    "the bar, the name is the panel's heading and the note is "
                    "what tapping it buys — a missing one leaves a heading "
                    "over nothing." % (act_id, g.get("id"), key))
        if g.get("lungs") not in _AMIX_LUNGS:
            raise ValueError(
                "air-mix %r gas %r says %r happens to it in a pair of lungs, "
                "and the closed set is %s. The block's lead sentence COUNTS "
                "the gases that come back out unchanged and adds their "
                "shares, so a fourth value is a category that sentence cannot "
                "count." % (act_id, g.get("id"), g.get("lungs"),
                            list(_AMIX_LUNGS)))
        seen_lungs.add(g["lungs"])
        pct = float(g.get("pct") or 0)
        if not 0 < pct <= 100:
            raise ValueError(
                "air-mix %r gas %r has a share of %r. It is what draws the "
                "bar and what every percentage on the block is derived from, "
                "so it lives in (0, 100]." % (act_id, g["id"], g.get("pct")))
    for want in ("absorbed", "unchanged"):
        if want not in seen_lungs:
            raise ValueError(
                "air-mix %r has no gas that is %r in the lungs. The lead "
                "sentence contrasts the gas a body takes with the gases it "
                "does not, and a set that is all one thing has nothing for it "
                "to contrast." % (act_id, want))

    total_pct = sum(float(g["pct"]) for g in gases)
    if total_pct > 100.0 + 1e-9:
        raise ValueError(
            "air-mix %r's gases add up to %s%% of the air. A bar whose "
            "segments are the proportions cannot hold more than the whole."
            % (act_id, _amix_pct(total_pct)))
    floor_claim = a.get("accounts_for")
    if floor_claim is not None and total_pct < float(floor_claim) - 1e-9:
        raise ValueError(
            "air-mix %r claims these gases account for at least %s%% of the "
            "air and its own shares reach %s%%. The explainer above the block "
            "says almost all of the air is just these few gases, and a set "
            "that no longer supports it leaves the sentence standing over a "
            "bar that contradicts it."
            % (act_id, _num(floor_claim), _amix_pct(total_pct)))

    start = a.get("start_gas") or gases[0]["id"]
    if start not in [g["id"] for g in gases]:
        raise ValueError(
            "air-mix %r opens on %r, which is not a gas on the bar. The "
            "opening state is what a student reads before touching anything."
            % (act_id, start))

    target = int(a.get("gases_to_tick") or 0)
    if not 2 <= target <= len(gases):
        raise ValueError(
            "air-mix %r ticks its rail stop at %r of %d. Two is the fewest "
            "that is a comparison and more than the set is a stop that can "
            "never tick." % (act_id, target, len(gases)))

    # ── the derived sentences ────────────────────────────────────────────
    unchanged = [g for g in gases if g["lungs"] == "unchanged"]
    floor_below = float(a.get("floor_below") or 0)
    wide = [g for g in gases if float(g["pct"]) < floor_below]

    lead = a.get("lead") or ""
    if not lead:
        raise ValueError(
            "air-mix %r authors no lead. Design's lead is the sentence that "
            "tells a student what they are about to find on the bar, and "
            "without it the block opens on a wall of four buttons." % act_id)
    if "{share_unchanged}" not in lead or not (
            "{n_unchanged}" in lead or "{N_unchanged}" in lead):
        raise ValueError(
            "air-mix %r's lead %r names no {share_unchanged}, or no count "
            "slot ({n_unchanged} / {N_unchanged}). Both are facts about the "
            "payload rather than numbers an author chose, and a sentence that "
            "hard-codes either goes on saying it after the set has changed."
            % (act_id, lead))

    note = a.get("scale_note") or ""
    if wide and not note:
        raise ValueError(
            "air-mix %r draws %s below its own %s%% floor and authors no "
            "scale_note. A segment that thin is not a tappable target, so the "
            "bar gives it a minimum width and stops being to scale — and a "
            "page that exaggerates a share without saying so is teaching the "
            "misconception it is on the page to break."
            % (act_id, [g["id"] for g in wide], _num(floor_below)))
    if note and not wide:
        raise ValueError(
            "air-mix %r authors a scale_note and no gas falls below its %s%% "
            "floor. The note tells a student the bar is drawn wider than the "
            "truth somewhere; on this payload it is not, so the note is a "
            "distortion the page is confessing to and has not made."
            % (act_id, _num(floor_below)))
    if note and ("{share_wide}" not in note or not (
            "{drawn_wide}" in note or "{Drawn_wide}" in note)):
        raise ValueError(
            "air-mix %r's scale_note %r never names {share_wide}, or names no "
            "gas slot ({drawn_wide} / {Drawn_wide}). The bar draws the thinnest gases WIDER than their "
            "share, so the true share has to be printed as a number in the "
            "one sentence that talks about the scale, and the gases it "
            "applies to have to be named — or the page is asserting a "
            "proportion it is visibly not drawing." % (act_id, note))

    dry = a.get("dry_note") or ""
    if not dry:
        raise ValueError(
            "air-mix %r authors no dry_note. The shares on this bar are the "
            "composition of DRY air, and the reason they are quoted dry is "
            "that water vapour is variable. Four percentages with no "
            "qualifier teach a student that the air has a fixed recipe, which "
            "is the belief this lesson's own key fact exists to break."
            % act_id)

    fills = {
        "{n_unchanged}": _rockb_word(len(unchanged)),
        "{N_unchanged}": _rockb_word(len(unchanged)).capitalize(),
        "{share_unchanged}": _amix_pct(sum(float(g["pct"])
                                           for g in unchanged)),
        "{total}": _rockb_word(len(gases)),
        # `{Drawn_wide}` is the same derived list with a capital, because the
        # sentence that quotes it OPENS with it. Without the pair, the note
        # ships "argon and carbon dioxide are drawn wider…" mid-sentence-cased
        # at the start of its own paragraph — and the alternatives are
        # capitalising the whole filled string (which would also capitalise a
        # slot used mid-sentence) or authoring the gas names. Same treatment
        # as `rock-bench`'s `{n}` / `{N}`.
        "{drawn_wide}": _c10_join([g["name"].lower() for g in wide]),
        "{Drawn_wide}": _c10_join([g["name"].lower()
                                   for g in wide]).capitalize(),
        "{share_wide}": _amix_pct(sum(float(g["pct"]) for g in wide)),
    }

    def _fill(text):
        for k, v in fills.items():
            text = text.replace(k, v)
        return text

    _c10_count_word_agrees(a.get("heading"), len(gases), act_id,
                           "air-mix", "heading")
    # One panel is open in the resting bytes, so the counter opens at one.
    _c10_head_agrees(a, act_id, "air-mix", len(gases), 1)

    suffix = a.get("share_suffix") or "of the air"

    segs, outs = [], []
    for g in gases:
        pct = float(g["pct"])
        shown = _amix_pct(pct)
        pressed = g["id"] == start
        thin = pct < floor_below

        # The accessible name carries the share the panel prints, spoken
        # rather than drawn: a screen reader gets the proportion without
        # having to open the panel to find it.
        segs.append(
            '<button type="button" class="ks3-amix-seg%s%s" '
            'data-amix-gas="%s" '
            'aria-pressed="%s" aria-label="%s" style="flex-grow:%.4f">'
            '<span class="ks3-amix-slabel">%s</span></button>'
            % (" ks3-amix-thin" if thin else "",
               # ⊕ Design paints ONE strip on the bar a different ground, and
               # it is oxygen's. Hers tests `g.id === 'o2'` — a gas id written
               # into the drawing code. Taken off `lungs` instead, so the tint
               # means "the gas your body actually takes" and follows the
               # payload rather than a hard-coded name.
               " ks3-amix-used" if g["lungs"] == "absorbed" else "",
               e(g["id"]),
               "true" if pressed else "false",
               e("%s, %s %s" % (g["name"], shown, suffix)),
               pct, t(g["label"])))

        outs.append(
            '<div class="ks3-amix-one" data-amix-out="%s"%s>'
            '<div class="ks3-amix-head">'
            '<p class="ks3-amix-name">%s</p>'
            '<p class="ks3-amix-pct">%s %s</p></div>'
            '<p class="ks3-amix-note">%s</p></div>'
            % (e(g["id"]), "" if pressed else " hidden",
               t(g["name"]), t(shown), t(suffix), rich(g["note"])))

    feet = ['<p class="ks3-amix-foot">%s</p>' % rich(_fill(note))] if note \
        else []
    feet.append('<p class="ks3-amix-foot">%s</p>' % rich(dry))

    return ('<div class="ks3-amix" data-amix data-total="%d" data-target="%d">'
            '<p class="ks3-amix-lead">%s</p>'
            '<div class="ks3-amix-bar">%s</div>'
            '<div class="ks3-amix-readout">%s</div>%s</div>'
            % (len(gases), target, rich(_fill(lead)), "".join(segs),
               "".join(outs), "".join(feet)))


# ═══ c10-05 · atmos-history ══════════════════════════════════════════════

def _ahist_when(mya):
    """A date in millions of years, printed the way a geologist would say it.

    4600 → "4.6 bya", 400 → "400 mya". The payload states ONE number per stage
    and this writes the label, so a stage cannot carry a date and a caption
    that disagree — which is the failure `c10-01`'s derived boundaries exist to
    stop, arriving at a timeline instead of at a bar.
    """
    mya = float(mya)
    if mya >= 1000:
        return "%.1f bya" % (mya / 1000.0)
    return "%d mya" % int(round(mya))


def r_atmos_history(a, act_id):
    """⊕ c10-05 `#s-history` — five stages, revealed one at a time.

    A STEPPER, and the only one in C10. Every stage is in the document from the
    moment the page loads with its explanation `hidden`; `shared/ks3.js`
    unhides them in order and swaps the button's label between three AUTHORED
    strings. It composes nothing and it computes nothing.

    ⚖️ **THE ORDER IS THE CLAIM, AND IT IS CHECKED.** The block asserts that
    the atmosphere arrived at today's composition through a sequence: volcanic
    gases, then oceans, then carbon dioxide dissolving, then photosynthesis,
    then carbon buried in rock. Every stage carries `mya` and the build refuses
    a set that does not run forwards in time. A payload re-sorted for layout
    cannot quietly re-teach the lesson, and an edited date fails the build
    instead of shipping a history that runs backwards.

    ⚖️ **THE THREE BUTTON LABELS ARE AUTHORED AND THE DONE ONE IS CHECKED.**
    Design's own button reads "Reveal the first stage", then "Reveal the next
    stage", then "All five shown" — and the third names the size of the set,
    which §5A forbids an author to hard-code. It is not authored twice: it is
    authored once and CHECKED against the payload by
    `_c10_count_word_agrees`, so a sixth stage fails the build rather than
    leaving the button saying five.

    ⚠️ **THE BUTTON IS NEVER DISABLED.** Design dims it once every stage is
    open. Disabling the control a keyboard user is standing on drops them to
    `<body>` — MRB-257, and `depth-evidence`, `rock-bench` and `grain-journey`
    all reached it by the same route. A press once the set is exhausted is a
    genuine no-op, and the label already says so in words.

    ⚠️ **NOTHING IS REVEALED IN THE BYTES.** The resting page opens with five
    closed stages, the counter at zero, the first label on the button and the
    closing panel hidden, which is the on-load state modelled rather than
    assumed.

    ⊕ **THE DATE IS NOT `aria-hidden`, AND DESIGN'S IS.** Her mono date chip
    carries `aria-hidden="true"`, which on this block removes the timeline
    from a screen reader entirely — the stages are five undated sentences, and
    the sequence is the whole content. It is read here, in the same words a
    sighted reader sees.

    HOOKS: `data-ahist` (wrapper, `data-total`, `data-target`) ·
    `data-ahist-step` (valued with the stage's index, with `data-open`) ·
    `data-ahist-why` · `data-ahist-reveal` (with `data-l-first`, `data-l-next`,
    `data-l-done`) · `data-ahist-panel`.
    """
    stages = a.get("stages") or []
    if len(stages) < 4:
        raise ValueError(
            "atmos-history %r has %d stage(s). The block's claim is that the "
            "air arrived at today's composition through a SEQUENCE, and a "
            "handful of steps cannot make it." % (act_id, len(stages)))
    _unique_ids(stages, act_id, "atmos-history", "stage")
    _no_correct_flags(stages, act_id, "atmos-history")

    for s in stages:
        for key in ("what", "why"):
            if not s.get(key):
                raise ValueError(
                    "atmos-history %r stage %r has no %r. The what is the "
                    "headline a student reads before revealing anything and "
                    "the why is what revealing it buys — a missing one is a "
                    "row with nothing behind it." % (act_id, s.get("id"), key))
        if s.get("mya") is None or float(s["mya"]) <= 0:
            raise ValueError(
                "atmos-history %r stage %r is dated %r. Every date LABEL on "
                "the block is written from this one number, and the order of "
                "the whole history is checked against it."
                % (act_id, s["id"], s.get("mya")))

    for prev, nxt in zip(stages, stages[1:]):
        if float(nxt["mya"]) >= float(prev["mya"]):
            raise ValueError(
                "atmos-history %r puts %r (%s) after %r (%s), so the history "
                "runs backwards. The ORDER is what this block asserts — that "
                "the air arrived at today's composition through a sequence — "
                "and a set that no longer runs forwards has quietly re-taught "
                "the lesson."
                % (act_id, nxt["id"], _ahist_when(nxt["mya"]),
                   prev["id"], _ahist_when(prev["mya"])))

    target = int(a.get("stages_to_reveal") or 0)
    if not 2 <= target <= len(stages):
        raise ValueError(
            "atmos-history %r ticks its rail stop at %r of %d. Two is the "
            "fewest that is a sequence and more than the set is a stop that "
            "can never tick." % (act_id, target, len(stages)))

    labels = {}
    for key, default in (("label_first", "Reveal the first stage"),
                         ("label_next", "Reveal the next stage"),
                         ("label_done", "All of them shown")):
        labels[key] = a.get(key) or default
    if len(set(labels.values())) != 3:
        raise ValueError(
            "atmos-history %r gives the button the same label in two of its "
            "three states (%s). The label is the only thing that tells a "
            "student whether there is another stage to come."
            % (act_id, sorted(set(labels.values()))))
    _c10_count_word_agrees(labels["label_done"], len(stages), act_id,
                           "atmos-history", "label_done")
    _c10_count_word_agrees(a.get("heading"), len(stages), act_id,
                           "atmos-history", "heading")
    # Nothing is revealed in the resting bytes, so the counter opens at zero.
    _c10_head_agrees(a, act_id, "atmos-history", len(stages), 0)

    panel = a.get("close_panel") or {}
    panel_text = panel.get("text") or []
    if isinstance(panel_text, str):
        panel_text = [panel_text]
    if not panel.get("title") or not panel_text:
        raise ValueError(
            "atmos-history %r authors no close panel title or text. The panel "
            "is the payoff of revealing every stage, and an empty one is a "
            "reward for finishing that says nothing." % act_id)

    rows = "".join(
        '<li class="ks3-ahist-step" data-ahist-step="%d" data-open="0">'
        '<div class="ks3-ahist-head">'
        '<span class="ks3-ahist-when">%s</span>'
        '<p class="ks3-ahist-what">%s</p></div>'
        '<p class="ks3-ahist-why" data-ahist-why hidden>%s</p></li>'
        % (i, t(_ahist_when(s["mya"])), rich(s["what"]), rich(s["why"]))
        for i, s in enumerate(stages))

    close = ('<div class="ks3-ahist-panel" data-ahist-panel hidden>'
             '<p class="ks3-ahist-ptitle">%s</p>%s</div>'
             % (t(panel["title"]),
                "".join('<p class="ks3-ahist-ptext">%s</p>' % rich(p)
                        for p in panel_text)))

    return ('<div class="ks3-ahist" data-ahist data-total="%d" '
            'data-target="%d"><ol class="ks3-ahist-list">%s</ol>'
            '<div class="ks3-ahist-tools">'
            '<button type="button" class="ks3-ahist-reveal" data-ahist-reveal '
            'data-l-first="%s" data-l-next="%s" data-l-done="%s">%s</button>'
            '</div>%s</div>'
            % (len(stages), target, rows,
               e(labels["label_first"]), e(labels["label_next"]),
               e(labels["label_done"]), t(labels["label_first"]), close))


# ═══ c10-06 · greenhouse-steps ═══════════════════════════════════════════
#
# ⚠️ WHAT A STEP IS ABOUT IS A CLOSED SET, and it is closed because the whole
# mechanism is an ASYMMETRY: the gases are transparent to what arrives and
# opaque to what leaves. Every step therefore declares which direction it is
# about and whether the gases absorb what is moving, and the build refuses a
# set that no longer states the asymmetry — including, specifically, a set
# that says greenhouse gases absorb sunlight, which is the wrong picture this
# whole block exists to replace.
_GHOUSE_DIRS = {"in": "Coming in", "out": "Going out", "balance": "In and out"}
_GHOUSE_BANDS = {"visible": "visible light", "infrared": "infrared"}

# ⚠️ `fate` IS THREE-VALUED AND NOT A BOOLEAN, and the difference is a science
# error caught while this was being written. A boolean "do the gases absorb
# this?" forces a false claim onto the step where the warmed ground EMITS
# infrared: at that point the radiation has not met a gas, so answering the
# question either way asserts something the step is not saying — and answering
# it "no" contradicts the step immediately below, which is the one where the
# gases absorb exactly that radiation.
_GHOUSE_FATES = {
    "passes":   "passes straight through",
    "emitted":  "emitted by the warmed surface",
    "absorbed": "absorbed and re-emitted",
}


def _ghouse_chip(step):
    """The mono line under a step's headline, DERIVED from what it claims.

    "Coming in · visible light · passes straight through" / "Going out ·
    infrared · absorbed and re-emitted". The balance step has no band and no
    fate — it is about the temperature the two settle at rather than about one
    beam — so its chip is the direction alone. Nothing here is authored: a
    step that changed from infrared to visible relabels itself.
    """
    where = _GHOUSE_DIRS[step["direction"]]
    if step["direction"] == "balance":
        return where
    return "%s · %s · %s" % (where, _GHOUSE_BANDS[step["band"]],
                             _GHOUSE_FATES[step["fate"]])


def r_greenhouse_steps(a, act_id):
    """⊕ c10-06 `#s-how` — four steps of a mechanism, revealed one at a time.

    C10's SECOND stepper, and it is not `atmos-history` with different words.
    The history block asserts a SEQUENCE IN TIME and is checked against dates;
    this one asserts a CHAIN OF CAUSE, and what it is checked against is the
    asymmetry that makes the chain work.

    ⚖️ **THE ASYMMETRY IS THE LESSON, SO IT IS THE THING THE BUILD REFUSES TO
    LOSE.** Every step declares a `direction` and, unless it is the closing
    balance step, a `band` and whether the gases absorb it. Four rules follow,
    and each of them is a misconception with a build failure attached:

      1. Visible light has to ARRIVE and pass straight through. Without that
         step the block starts with a warm ground and never says where the
         warmth came from — and it is the step that says the gases do nothing
         at all to the sunlight.
      2. Infrared has to LEAVE and be ABSORBED. That is the only step at which
         a greenhouse gas does anything, and a set without it has described a
         planet with no greenhouse effect.
      3. ⚑ **NOTHING MAY ABSORB VISIBLE LIGHT.** "The gases trap the Sun's
         rays" is the single most common wrong picture of this mechanism, it
         is what Design's own step one exists to kill, and a payload that
         quietly re-asserted it would leave every other gate green.
      4. The BALANCE step comes last, and there is exactly one of it. The
         chain's conclusion is the last thing revealed; a stepper that opens
         with its conclusion has stopped being an argument.

    ⚖️ **THE STEP NUMBER AND THE STEP'S CHIP ARE BOTH DERIVED.** Design numbers
    her steps 1–4 in the drawing and states in prose what each one is about.
    The number is the index and the chip is `_ghouse_chip`, so a fifth step
    numbers itself and a step whose science is edited relabels itself.

    ⚠️ **THE BUTTON IS NEVER DISABLED** — MRB-257, the ruling `depth-evidence`,
    `rock-bench`, `grain-journey` and `atmos-history` all reached before this
    one. Design dims it once every step is open; disabling the control a
    keyboard user is standing on drops them to `<body>`. A press once the set
    is exhausted is a genuine no-op and the label says so in words.

    ⚠️ **NOTHING IS REVEALED IN THE BYTES.** The resting page opens with four
    closed steps, the counter at zero, the first label on the button and the
    closing panel hidden — the on-load state modelled rather than assumed.

    ⊕ **THE CLOSING PANEL IS AN ADDITION TO WHAT DESIGN DREW, and it is where
    the lesson pays for keeping the word "greenhouse".** See the lesson
    record's docstring: the name is the specification's own and cannot be
    dropped, the analogy behind it is wrong, and the honest place to say so is
    the moment a student has just watched the real mechanism four steps in a
    row. It is `close_panel`, the same shape `atmos-history` already uses, and
    it is REQUIRED rather than optional.

    HOOKS: `data-ghouse` (wrapper, `data-total`, `data-target`) ·
    `data-ghouse-step` (valued with the step's index, with `data-open`) ·
    `data-ghouse-why` · `data-ghouse-reveal` (with `data-l-first`,
    `data-l-next`, `data-l-done`) · `data-ghouse-panel`.
    """
    steps = a.get("steps") or []
    if len(steps) < 3:
        raise ValueError(
            "greenhouse-steps %r has %d step(s). The block's claim is that the "
            "greenhouse effect is a CHAIN — something arrives, something "
            "leaves, something absorbs what leaves — and fewer than three "
            "cannot make it." % (act_id, len(steps)))
    _unique_ids(steps, act_id, "greenhouse-steps", "step")
    _no_correct_flags(steps, act_id, "greenhouse-steps")

    for s in steps:
        for key in ("what", "why"):
            if not s.get(key):
                raise ValueError(
                    "greenhouse-steps %r step %r has no %r. The what is the "
                    "headline a student reads before revealing anything and "
                    "the why is what revealing it buys — a missing one is a "
                    "row with nothing behind it." % (act_id, s.get("id"), key))
        if s.get("direction") not in _GHOUSE_DIRS:
            raise ValueError(
                "greenhouse-steps %r step %r is about %r and the closed set "
                "is %s. Every step's mono chip is written from this, and the "
                "asymmetry the block exists to teach is checked against it."
                % (act_id, s["id"], s.get("direction"), list(_GHOUSE_DIRS)))
        if s["direction"] == "balance":
            if s.get("band") is not None or s.get("fate") is not None:
                raise ValueError(
                    "greenhouse-steps %r step %r is the balance step and also "
                    "names a band or a fate. The balance step is about the "
                    "temperature the incoming and outgoing energy settle at, "
                    "not about one beam, and giving it either would print a "
                    "claim the step is not making." % (act_id, s["id"]))
            continue
        if s.get("band") not in _GHOUSE_BANDS:
            raise ValueError(
                "greenhouse-steps %r step %r carries the band %r and the "
                "closed set is %s. The band is a third of what the step's chip "
                "says and half of what rule 3 below checks."
                % (act_id, s["id"], s.get("band"), list(_GHOUSE_BANDS)))
        if s.get("fate") not in _GHOUSE_FATES:
            raise ValueError(
                "greenhouse-steps %r step %r says %r happens to the radiation "
                "it is about, and the closed set is %s. What happens to each "
                "beam IS the greenhouse effect, and the block's asymmetry is "
                "checked against these three values."
                % (act_id, s["id"], s.get("fate"), list(_GHOUSE_FATES)))
        if s["band"] == "visible" and s["fate"] == "absorbed":
            raise ValueError(
                "greenhouse-steps %r step %r says greenhouse gases absorb "
                "VISIBLE light. They do not — they are transparent to it, "
                "which is why sunlight reaches the ground at all. \"The gases "
                "trap the Sun's rays\" is the wrong picture this block exists "
                "to replace, and a payload asserting it would leave every "
                "other gate on this page green." % (act_id, s["id"]))

    if not any(s["direction"] == "in" and s["band"] == "visible"
               and s["fate"] == "passes"
               for s in steps if s["direction"] != "balance"):
        raise ValueError(
            "greenhouse-steps %r has no step in which visible light ARRIVES "
            "and passes straight through. Without it the chain opens on a "
            "warm ground and never says where the warmth came from — and it "
            "is the step that says the gases do nothing at all to the "
            "sunlight." % act_id)
    if not any(s["direction"] == "out" and s["band"] == "infrared"
               and s["fate"] == "absorbed"
               for s in steps if s["direction"] != "balance"):
        raise ValueError(
            "greenhouse-steps %r has no step in which outgoing INFRARED is "
            "absorbed. That is the only step at which a greenhouse gas does "
            "anything at all, and a set without it has described a planet "
            "with no greenhouse effect." % act_id)

    balance = [i for i, s in enumerate(steps) if s["direction"] == "balance"]
    if len(balance) != 1 or balance[0] != len(steps) - 1:
        raise ValueError(
            "greenhouse-steps %r puts its balance step(s) at %s of %d. There "
            "is exactly one conclusion and it is revealed last — a stepper "
            "that opens with its conclusion has stopped being an argument."
            % (act_id, [i + 1 for i in balance], len(steps)))

    target = int(a.get("steps_to_reveal") or 0)
    if not 2 <= target <= len(steps):
        raise ValueError(
            "greenhouse-steps %r ticks its rail stop at %r of %d. Two is the "
            "fewest that is a chain and more than the set is a stop that can "
            "never tick." % (act_id, target, len(steps)))

    labels = {}
    for key, default in (("label_first", "Reveal the first step"),
                         ("label_next", "Reveal the next step"),
                         ("label_done", "All of them shown")):
        labels[key] = a.get(key) or default
    if len(set(labels.values())) != 3:
        raise ValueError(
            "greenhouse-steps %r gives the button the same label in two of "
            "its three states (%s). The label is the only thing that tells a "
            "student whether there is another step to come."
            % (act_id, sorted(set(labels.values()))))
    _c10_count_word_agrees(labels["label_done"], len(steps), act_id,
                           "greenhouse-steps", "label_done")
    _c10_count_word_agrees(a.get("heading"), len(steps), act_id,
                           "greenhouse-steps", "heading")
    # Nothing is revealed in the resting bytes, so the counter opens at zero.
    _c10_head_agrees(a, act_id, "greenhouse-steps", len(steps), 0)

    panel = a.get("close_panel") or {}
    panel_text = panel.get("text") or []
    if isinstance(panel_text, str):
        panel_text = [panel_text]
    if not panel.get("title") or not panel_text:
        raise ValueError(
            "greenhouse-steps %r authors no close panel title or text. This "
            "page keeps the word \"greenhouse\" because it is the "
            "specification's own, and the panel is where it says what the "
            "name does and does not share with an actual greenhouse. Without "
            "it the block has taught the mechanism and left the analogy "
            "standing." % act_id)

    rows = "".join(
        '<li class="ks3-ghouse-step" data-ghouse-step="%d" data-open="0">'
        '<div class="ks3-ghouse-head">'
        '<span class="ks3-ghouse-num" aria-hidden="true">%d</span>'
        '<p class="ks3-ghouse-what">%s</p></div>'
        '<p class="ks3-ghouse-chip">%s</p>'
        '<p class="ks3-ghouse-why" data-ghouse-why hidden>%s</p></li>'
        % (i, i + 1, rich(s["what"]), t(_ghouse_chip(s)), rich(s["why"]))
        for i, s in enumerate(steps))

    close = ('<div class="ks3-ghouse-panel" data-ghouse-panel hidden>'
             '<p class="ks3-ghouse-ptitle">%s</p>%s</div>'
             % (t(panel["title"]),
                "".join('<p class="ks3-ghouse-ptext">%s</p>' % rich(p)
                        for p in panel_text)))

    return ('<div class="ks3-ghouse" data-ghouse data-total="%d" '
            'data-target="%d"><ol class="ks3-ghouse-list">%s</ol>'
            '<div class="ks3-ghouse-tools">'
            '<button type="button" class="ks3-ghouse-reveal" '
            'data-ghouse-reveal data-l-first="%s" data-l-next="%s" '
            'data-l-done="%s">%s</button></div>%s</div>'
            % (len(steps), target, rows,
               e(labels["label_first"]), e(labels["label_next"]),
               e(labels["label_done"]), t(labels["label_first"]), close))


# ═══ c10-06 · climate-evidence ═══════════════════════════════════════════
#
# ⚠️ WHAT A PIECE OF EVIDENCE ESTABLISHES ON ITS OWN is a CLOSED SET, and it
# is closed because the whole point of the block is that the four pieces do
# DIFFERENT jobs. Four measurements of the same kind are one measurement
# repeated; four independent kinds agreeing is an argument. The set is checked
# rather than trusted, and the closing panel is written from it.
_CEV_ROLES = {
    "trend":     "that the amount really is changing, and by how much",
    "context":   "how the present compares with the whole past record",
    "source":    "where the extra carbon dioxide came from",
    "mechanism": "why carbon dioxide should warm anything at all",
}


def r_climate_evidence(a, act_id):
    """⊕ c10-06 `#s-evidence` — four pieces of evidence, each committed to.

    A commit-then-read set, the same contract as `depth-evidence`: a question,
    three readings of it, and the answer underneath, hidden until the student
    has picked one. NOTHING IS MARKED — every reading opens the same answer,
    because what the block is for is making the student say what they think
    BEFORE the page says what is known.

    ⚖️ **THE INSTRUMENT EXPRESSES "CORRELATION IS NOT CAUSATION" RATHER THAN
    ASSERTING IT, AND THAT IS WHY `establishes` EXISTS.** Every entry declares
    what it can establish ON ITS OWN, from a closed set, and the build refuses:

      · a set with no `mechanism` entry — because then the page is offering
        agreeing correlations as proof of a cause, which is the reasoning
        error the whole block is built to inoculate against;
      · a set with more than one, because "the mechanism" is what the other
        three lack and naming two of them makes the word mean nothing;
      · a set whose non-mechanism entries are all the same role, because four
        measurements of one kind are one measurement repeated.

    The role is then printed INSIDE the answer, under `role_line`, so a
    student who has committed reads what their piece of evidence can and
    cannot carry — and the closing panel names the mechanism entry by its own
    tag rather than by a sentence an author typed.

    ⚖️ **THE CLOSING PANEL IS COMPOSED FROM THE ENTRIES.** Design's middle
    paragraph is four sentences, one per piece — "A rising curve on its own
    could be natural. Ice cores on their own only give the past…" — and each
    of them is a fact about the entry it describes. They are authored on the
    entries as `alone` and joined here in payload order, so a fifth piece of
    evidence appears in the panel instead of leaving a paragraph that names
    four. The count in the panel's title is derived for the same reason.

    ⚠️ **THE CHOSEN BUTTON STAYS ENABLED; THE OTHERS DO NOT** — MRB-257 and
    `depth-evidence`'s ruling, unchanged. Nothing is disabled in the BYTES:
    the resting page has nothing chosen, so every button opens live.

    ⊕ **"Evidence 1 ·" IS DERIVED.** Design types the ordinal into each tag.
    The payload states the descriptor alone and the prefix is the index, so a
    reordered set renumbers itself.

    HOOKS: `data-cev` (wrapper, `data-total`, `data-target`) ·
    `data-cev-pick` (valued `entry:choice`, with `data-cev-of`) ·
    `data-cev-answer` · `data-cev-panel`.
    """
    entries = a.get("entries") or []
    if len(entries) < 3:
        raise ValueError(
            "climate-evidence %r has %d entr(y/ies). The block's claim is that "
            "the case rests on SEVERAL independent lines pointing the same "
            "way, and two lines are a coincidence." % (act_id, len(entries)))
    _unique_ids(entries, act_id, "climate-evidence", "entry")
    _no_correct_flags(entries, act_id, "climate-evidence")

    for x in entries:
        for key in ("tag", "q", "answer", "alone"):
            if not x.get(key):
                raise ValueError(
                    "climate-evidence %r entry %r has no %r. The tag names the "
                    "kind of evidence, the question is what is committed to, "
                    "the answer is what the commitment buys, and `alone` is "
                    "this entry's own sentence in the closing panel."
                    % (act_id, x.get("id"), key))
        if x.get("establishes") not in _CEV_ROLES:
            raise ValueError(
                "climate-evidence %r entry %r establishes %r and the closed "
                "set is %s. What each piece can carry on its own is the whole "
                "argument of the block, and it is printed from this."
                % (act_id, x["id"], x.get("establishes"), list(_CEV_ROLES)))
        choices = x.get("choices") or []
        if len(choices) < 3:
            raise ValueError(
                "climate-evidence %r entry %r offers %d reading(s). Two is a "
                "coin flip, and a commitment a student can make by tossing a "
                "coin is not a commitment." % (act_id, x["id"], len(choices)))
        _unique_ids(choices, act_id, "climate-evidence", "choice")
        _no_correct_flags(choices, act_id, "climate-evidence")
        for c in choices:
            if not c.get("label"):
                raise ValueError(
                    "climate-evidence %r entry %r has a reading with no "
                    "label — a blank button." % (act_id, x["id"]))

    mech = [x for x in entries if x["establishes"] == "mechanism"]
    if len(mech) != 1:
        raise ValueError(
            "climate-evidence %r carries %d entries establishing a MECHANISM. "
            "Exactly one is right. With none, the page offers a pile of "
            "agreeing correlations as proof of a cause, which is the reasoning "
            "error this block exists to inoculate against; with two, the word "
            "stops distinguishing the piece of evidence that says WHY from the "
            "pieces that say WHAT." % (act_id, len(mech)))
    others = {x["establishes"] for x in entries if x is not mech[0]}
    if len(others) < 2:
        raise ValueError(
            "climate-evidence %r has %d kind(s) of non-mechanism evidence. "
            "Four measurements of the same kind are one measurement repeated, "
            "and the panel's claim is that INDEPENDENT lines agree."
            % (act_id, len(others)))

    target = int(a.get("entries_to_tick") or 0)
    if not 2 <= target <= len(entries):
        raise ValueError(
            "climate-evidence %r ticks its rail stop at %r of %d. Two is the "
            "fewest that is a comparison and more than the set is a stop that "
            "can never tick." % (act_id, target, len(entries)))

    role_line = a.get("role_line") or ""
    if "{role}" not in role_line:
        raise ValueError(
            "climate-evidence %r's role_line %r names no {role}. The line "
            "under each answer says what that piece of evidence can carry on "
            "its own, and hard-coding it would let an entry's declared role "
            "and its printed role drift apart." % (act_id, role_line))

    panel = a.get("close_panel") or {}
    panel_text = panel.get("text") or []
    if isinstance(panel_text, str):
        panel_text = [panel_text]
    title = panel.get("title") or ""
    if not title or not panel_text:
        raise ValueError(
            "climate-evidence %r authors no close panel title or text. The "
            "panel is the payoff of judging every piece — it is where four "
            "separate commitments become one argument — and an empty one is a "
            "reward for finishing that says nothing." % act_id)
    if "{Total}" not in title and "{total}" not in title:
        raise ValueError(
            "climate-evidence %r's panel title %r names no {Total}. The title "
            "says how many independent lines agree, which is a fact about the "
            "payload, and a hard-coded number goes on saying four after the "
            "fifth is added." % (act_id, title))
    joined = " ".join(panel_text)
    if "{alone}" not in joined:
        raise ValueError(
            "climate-evidence %r's panel names no {alone}. Each entry carries "
            "its own sentence saying what it cannot do by itself, and the "
            "panel is those sentences in payload order — authored as a "
            "paragraph instead, it would describe the set that existed on the "
            "day it was written." % act_id)
    if "{mechanism}" not in joined:
        raise ValueError(
            "climate-evidence %r's panel names no {mechanism}. The point of "
            "the panel is that one of these pieces is doing a different job "
            "from the others, and naming it by hand is the page asserting "
            "what the payload is supposed to be showing." % act_id)

    fills = {
        "{Total}": _rockb_word(len(entries)).capitalize(),
        "{total}": _rockb_word(len(entries)),
        "{alone}": " ".join(x["alone"] for x in entries),
        "{mechanism}": mech[0]["tag"],
    }

    def _fill(text):
        for k, v in fills.items():
            text = text.replace(k, v)
        return text

    _c10_count_word_agrees(a.get("heading"), len(entries), act_id,
                           "climate-evidence", "heading")
    # Nothing is judged in the resting bytes, so the counter opens at zero.
    _c10_head_agrees(a, act_id, "climate-evidence", len(entries), 0)

    prefix = a.get("label") or "Evidence"

    cards = []
    for i, x in enumerate(entries):
        picks = "".join(
            _c10_seg("ks3-cev-choice", c["label"], False,
                     data_cev_pick="%s:%s" % (x["id"], c["id"]),
                     data_cev_of=x["id"])
            for c in x["choices"])
        cards.append(
            '<div class="ks3-cev-one">'
            '<p class="ks3-cev-tag">%s</p>'
            '<p class="ks3-cev-q">%s</p>'
            '<div class="ks3-cev-picks">%s</div>'
            '<div class="ks3-cev-answer" data-cev-answer="%s" hidden>'
            '<p class="ks3-cev-role">%s</p>'
            '<p class="ks3-cev-atext">%s</p></div></div>'
            % (t("%s %d · %s" % (prefix, i + 1, x["tag"])),
               rich(x["q"]), picks, e(x["id"]),
               t(role_line.replace("{role}", _CEV_ROLES[x["establishes"]])),
               rich(x["answer"])))

    close = ('<div class="ks3-cev-panel" data-cev-panel hidden>'
             '<p class="ks3-cev-ptitle">%s</p>%s</div>'
             % (t(_fill(title)),
                "".join('<p class="ks3-cev-ptext">%s</p>' % rich(_fill(p))
                        for p in panel_text)))

    return ('<div class="ks3-cev" data-cev data-total="%d" data-target="%d">'
            '%s%s</div>'
            % (len(entries), target, "".join(cards), close))


# ═══ registration ════════════════════════════════════════════════════════
#
# ⊕ ELEVEN ROWS, AND THE UNIT IS COMPLETE. This block said "nine rows, because
# nine renderers exist" for five waves; wave 6 lands the last two and there is
# no longer a family named in this module's header and absent from here.
# `ks3_art.check_placements` gate 2 fails a family registered and never placed
# and gate 3 fails one placed and never registered, so the two lists agreeing
# is now checkable rather than promised.

KIND_SHELL = {
    'earth-layers': ("ks3-elay-block",
                     ' data-instrument data-elayblock data-stage-done="0"'),
    'depth-evidence': ("ks3-edep-block",
                       ' data-instrument data-edepblock data-stage-done="0"'),
    'material-loop': ("ks3-mloop-block",
                      ' data-instrument data-mloopblock data-stage-done="0"'),
    'stock-limits': ("ks3-stock-block",
                     ' data-instrument data-stockblock data-stage-done="0"'),
    'rock-bench': ("ks3-rockb-block",
                   ' data-instrument data-rockbblock data-stage-done="0"'),
    'grain-journey': ("ks3-grain-block",
                      ' data-instrument data-grainblock data-stage-done="0"'),
    'process-arrows': ("ks3-parrow-block",
                       ' data-instrument data-parrowblock data-stage-done="0"'),
    'air-mix': ("ks3-amix-block",
                ' data-instrument data-amixblock data-stage-done="0"'),
    'atmos-history': ("ks3-ahist-block",
                      ' data-instrument data-ahistblock data-stage-done="0"'),
    'greenhouse-steps': ("ks3-ghouse-block",
                         ' data-instrument data-ghouseblock '
                         'data-stage-done="0"'),
    'climate-evidence': ("ks3-cev-block",
                         ' data-instrument data-cevblock data-stage-done="0"'),
}

KIND_FN = {
    'earth-layers': r_earth_layers,
    'depth-evidence': r_depth_evidence,
    'material-loop': r_material_loop,
    'stock-limits': r_stock_limits,
    'rock-bench': r_rock_bench,
    'grain-journey': r_grain_journey,
    'process-arrows': r_process_arrows,
    'air-mix': r_air_mix,
    'atmos-history': r_atmos_history,
    'greenhouse-steps': r_greenhouse_steps,
    'climate-evidence': r_climate_evidence,
}
