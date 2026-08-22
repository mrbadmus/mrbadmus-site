"""ks3_art.c10 — C10's instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may
be added to any other unit's module. C10 is *The Earth and its atmosphere*:
six lessons, ELEVEN instrument families and no drawn figure so far, all DOM,
no canvas and no animation loop anywhere in the unit.

═══════════════════════════════════════════════════════════════════════════
⚠️ WAVE 2 — FOUR FAMILIES IMPLEMENTED, SEVEN STILL TO COME
═══════════════════════════════════════════════════════════════════════════

Wave 1 built the unit spine and the reference lesson `c10-04`; wave 2 adds
`c10-01`. Four families are implemented and only those four are registered:

    material-loop   ks3-mloop-block   c10-04  #s-loop    ← INK-DARK
    stock-limits    ks3-stock-block   c10-04  #s-stock
    earth-layers    ks3-elay-block    c10-01  #s-layers
    depth-evidence  ks3-edep-block    c10-01  #s-evidence

⊖ **THE OTHER SEVEN ARE NOT REGISTERED, AND MUST NOT BE UNTIL THEY EXIST.**
`ks3_art.check_placements` gate 2 fails a family that is registered and never
placed, and gate 3 fails one that is placed and never registered. A stub row
added "ready" for a later lane would ship the shell around the generic
prompt/options branch — the C1 defect (MRB-228) — the moment a lesson named
it. Each lane registers its own:

    rock-bench        ks3-rockb-block   c10-02  #s-bench
    grain-journey     ks3-grain-block   c10-03  #s-journey
    process-arrows    ks3-parrow-block  c10-03  #s-processes
    air-mix           ks3-amix-block    c10-05  #s-mix
    atmos-history     ks3-ahist-block   c10-05  #s-history
    greenhouse-steps  ks3-ghouse-block  c10-06  #s-how
    climate-evidence  ks3-cev-block     c10-06  #s-evidence

The eleven shell classes above were checked free against every `KIND_SHELL`
value in `ks3_art` before minting (MRB-279), so a later lane may take its row
without re-checking. `c10-02`'s `#s-table` is NOT on the list: it is a
controlless REFERENCE stop mirroring the hook, which is a `rule` block and not
an instrument, and `c10-04`'s `#s-words` is the existing vocabulary block.

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


# ═══ registration ════════════════════════════════════════════════════════
#
# ⚠️ FOUR ROWS, BECAUSE FOUR RENDERERS EXIST. The other seven C10 families
# are listed in this module's header and are registered by their own lesson's
# author, in this file, when the renderer lands beside the row.

KIND_SHELL = {
    'earth-layers': ("ks3-elay-block",
                     ' data-instrument data-elayblock data-stage-done="0"'),
    'depth-evidence': ("ks3-edep-block",
                       ' data-instrument data-edepblock data-stage-done="0"'),
    'material-loop': ("ks3-mloop-block",
                      ' data-instrument data-mloopblock data-stage-done="0"'),
    'stock-limits': ("ks3-stock-block",
                     ' data-instrument data-stockblock data-stage-done="0"'),
}

KIND_FN = {
    'earth-layers': r_earth_layers,
    'depth-evidence': r_depth_evidence,
    'material-loop': r_material_loop,
    'stock-limits': r_stock_limits,
}
