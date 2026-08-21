"""KS3 half-term placement — *where in the year* the default sequence lands.

**Ruled by Mide, MRB-176 ruling 2.** ``default_sequence.py`` says which YEAR a
unit is taught in. That is the right grain for an architecture document and the
wrong grain for a teacher: nobody plans a year, they plan six half terms. A
head of department asking "what am I teaching after October half term?" cannot
answer it from a year number, and a school comparing its own scheme against the
platform default cannot see where it actually diverges. This module supplies
the missing half of the answer.

**It changes nothing about what a lesson IS.** §4.5's invariant governs here
exactly as it governs the year:

    "year and sequence are metadata, never structure"

Half term is the same kind of fact, and inherits the same prohibition. It must
never reach a URL, a folder, a file name, a navigation structure, a content
branch, or a single byte of a lesson page. It exists to be written into a
scheme-of-work row and read back by a teacher. ``verify_ks3.py`` proves the
page bytes are untouched, which is the only proof that matters.

---

**What this module is for, in one line:** it turns the default sequence's
33 units into 185 (year, half term) placements, derived rather than authored,
so that the placement cannot drift from the sequence it came from.

**Derived, not transcribed.** A hand-written half-term table would be a third
copy of the curriculum — after ``structure.py`` and ``default_sequence.py`` —
and the third copy is where drift lives. Everything below is computed from
those two, with exactly one authored deviation (``ORDER_OVERRIDES``) and one
authored edge list (``SAME_YEAR_PREREQS``), both of which are small enough to
read and both of which fail the import if they stop matching reality.

---

**RULED TRADE-OFF — what the split optimises, and in what order.**

Three things are wanted from a half-term split and they do not all fit. The
ruled priority is:

1. **Prerequisite order.** A lesson is never taught before something it
   requires. Non-negotiable — a combination that breaks a `SAME_YEAR_PREREQS`
   edge is discarded, not scored.
2. **Interleaving.** All three sciences appear in every half term of every
   year. Also non-negotiable: a school timetables all three every half term,
   so a default that drops one for six weeks is not teachable.
3. **Balance.** The six half terms of a year carry roughly equal totals.

**Unit coherence — not slicing a unit across a half-term boundary — is a
fourth thing, and it deliberately loses to balance.** It is a nice-to-have:
finishing C6 Acids and alkalis before the October break reads better than
splitting it, but a teacher can teach a unit across a holiday, and cannot
conjure time for a half term carrying 60% more content than the one before it.
So coherence is expressed as a **tie-break**, applied only among splits that
are already equally balanced.

Concretely, each of a year's 15 internal cuts (3 disciplines × 5 cuts) either
stays where the arithmetic put it or moves onto a unit boundary within one
lesson. All ≤ 2^15 combinations are enumerated for the whole year **jointly**,
invalid ones discarded, and the winner chosen by, in strict order:

1. minimise ``max(year totals) − min(year totals)``
2. then **maximise** the number of snapped cuts — coherence, as the tie-break
3. then prefer no-snap on the lowest-indexed cut, so no tie survives

**Why joint and not per-discipline.** The first version of this module decided
each discipline's snaps independently, each within ±1 of even. That is fine per
discipline and bad per year: when two or three lanes happen to snap the same
way, the deviations compound. Year 8 came out at 16 lessons in HT1 against 10
in HT5. Balance is a property of the YEAR — it is what a child's week actually
feels like — so it has to be decided at the year level.

---

**Slot identity is `(unit_code, lesson_slug)`, not the slug alone.**

There are **185 lesson slots and, today, 185 distinct slugs** — but the pair
key is the §4.6 reference slot's requirement, not an optimisation for a
duplicate that happens to exist. ``energy-in-food`` was the worked example:
declared once in B3 as a reference slot owned by P2 and once in P2 as the
lesson itself, two slots in two different years — B3 is Year 7 biology, P2 is
Year 9 physics — and a teacher teaches both of them, per
``ks3_seed_sow.py``'s row rule. A dict keyed on the slug alone would silently
lose one of them and quietly place the Year 7 biology slot in Year 9. B3's slot
has since been renamed ``energy-in-food-and-what-you-need`` and no reference
slot is declared at present, so no slug currently collides. **Do not relax the
key on that basis** — the next reference slot reintroduces the collision, and
it would be reintroduced silently. So the placement is keyed on the pair, and
``half_term_of(slug)`` resolves to the
**owning** slot unless a unit code is given.

---

**Circular imports.** This module imports ``structure`` and
``default_sequence`` only — never the ``ks3_data`` package itself, whose
``__init__`` runs ``build_units()`` at module level. That means authored
lesson-level ``requires`` edges cannot be checked here at import time. They are
checked instead by ``check_authored_requires(units)``, which
``verify_ks3.py`` §10 calls with the units it has already built, and a
non-empty return there is a build failure. Everything else in this module is
asserted at import.
"""

import bisect
import itertools

from . import structure
from .default_sequence import DEFAULT_SEQUENCE_V1

# An English school year is six half terms. Not five, not three terms: six is
# the unit a department actually plans in, and it is the grain a scheme of work
# is written at.
HALF_TERMS = (1, 2, 3, 4, 5, 6)

YEARS = (7, 8, 9)

# Display names and URL slugs for the six half terms, in one place.
#
# **This module is the single source for these names.** The browse layer
# (architecture.md §4.5.2) puts the slug in an index-page URL, so a second copy
# living in the generator would be free to drift from this one — and a drifted
# slug is a 404 that only appears for one half term of one year, which is
# exactly the kind of defect nobody finds by clicking around. The generator
# imports from here.
#
# The slug appears in browse-layer INDEX pages only. It must never reach a
# lesson URL, folder or page byte — §4.5 forbids it and §9's reorder proof
# fails if it happens.
HALF_TERM_NAMES = {
    1: ("autumn-1", "Autumn First Half"),
    2: ("autumn-2", "Autumn Second Half"),
    3: ("spring-1", "Spring First Half"),
    4: ("spring-2", "Spring Second Half"),
    5: ("summer-1", "Summer First Half"),
    6: ("summer-2", "Summer Second Half"),
}

assert set(HALF_TERM_NAMES) == set(HALF_TERMS), (
    "HALF_TERM_NAMES must name every half term and no others")


def half_term_slug(ht):
    """URL slug for a half term — browse-layer index pages only (§4.5.2)."""
    return HALF_TERM_NAMES[ht][0]


def half_term_name(ht):
    """Display name for a half term, e.g. 'Autumn First Half'."""
    return HALF_TERM_NAMES[ht][1]

# ═══════════════════════════════════════════════════════════════════════════
# Intra-year unit order
# ═══════════════════════════════════════════════════════════════════════════
#
# The default order within a year is ``structure.py``'s declaration order,
# filtered to the units the default sequence puts in that year. Declaration
# order is not an accident — §7's tables are written in teaching order, and
# ``ks3_seed_sow.py`` has always used it to number ``academic_week``.
#
# ORDER_OVERRIDES holds the deviations where the prerequisite graph, not the
# order the table happens to be written in, decides.

ORDER_OVERRIDES = {
    # ── P5 Pressure moves ahead of P1 Energy, Year 8 physics ─────────────
    #
    # B4 `how-breathing-works` (Biology, Year 8) requires P5 Pressure — §7.1
    # marks it ⇄, and the reason is not a curriculum convention: breathing IS
    # a pressure-difference mechanism, and a student who has not met pressure
    # is being asked to accept the diaphragm as a fact rather than understand
    # it. B4 is biology's FIRST Year 8 unit, so breathing falls in half term 1,
    # so P5 has to be reachable by then. Under declaration order it is not:
    # P1 Energy is eight lessons long and would push P5 into half term 2.
    #
    # Nothing resists the move. P5's own prerequisite is P4 Forces, which the
    # default finishes in Year 7, and no Year 8 physics unit requires P1 before
    # P5. The prerequisite graph decides this, and declaration order has no
    # claim on it.
    #
    # It also simply reads better: Year 7 physics ends on Forces and Year 8
    # opens on Pressure, which is the same idea one step further on.
    #
    # The alternative considered was moving B5 Reproduction ahead of B4 in
    # biology, pushing breathing later instead of pressure earlier. Rejected:
    # it is the larger change — eight lessons moved instead of four — and it
    # buys no pedagogical gain, because there is no argument that reproduction
    # belongs before gas exchange. It only shuffles the problem.
    (8, "physics"): ["P5", "P1", "P6", "P7", "P8"],
}

# ═══════════════════════════════════════════════════════════════════════════
# The GCSE-bridge rule (§7.6)
# ═══════════════════════════════════════════════════════════════════════════
#
# §7.6 designs a Year 9 group of `beyond_statutory` bridge units for schools
# that start GCSE in Year 9. Both real schools in `school_schemes.py` teach
# their bridge content last in the year, and §7.6's own framing — "an autumn
# term" swapped in for the remaining statutory content — only makes sense at
# one end of the year. So the rule is: a beyond-statutory unit placed in
# Year 9 is taught in half term 6, and is ordered last within its discipline.
#
# No bridge unit exists in `structure.py` yet — §7.6 is design-only and says so
# — so this rule currently places exactly zero lessons. It is written now, as a
# live branch rather than a comment, so that the first bridge unit inherits a
# placement instead of needing a second ruling. A branch that never runs is a
# branch that was never tested, which is why `derive()` reports the count.

BRIDGE_HALF_TERM = 6


def beyond_statutory_units():
    """Unit codes declared beyond-statutory (§7.6 bridge units).

    Read defensively from ``structure.py`` in both of the shapes a bridge unit
    could plausibly arrive in — a module-level set, or a per-unit flag surfaced
    by ``unit_index()``. Today both are absent and this returns an empty set.
    Guessing which shape §7.6 will land in is cheaper than the alternative,
    which is this rule silently not applying to the first bridge unit written.
    """
    declared = set(getattr(structure, "BEYOND_STATUTORY_UNITS", ()) or ())
    flagged = {code for code, u in structure.unit_index().items()
               if u.get("beyond_statutory")}
    return declared | flagged


# ═══════════════════════════════════════════════════════════════════════════
# Cross-discipline prerequisites that fall inside one year
# ═══════════════════════════════════════════════════════════════════════════
#
# §7 marks these ⇄. They are the edges that make half-term placement a real
# constraint rather than arithmetic: a Year 8 biology lesson can depend on a
# Year 8 physics lesson, and "same year" is not good enough if biology meets it
# in half term 1 and physics teaches it in half term 4.
#
# Cross-YEAR edges are not here. Those are `verify_ks3.py`'s forward-reference
# gate (check 5b) and a different question — this list is only about edges the
# year number already permits and the half term could still break.
#
# Each row is (dependent, prerequisite, why). The `why` is not decoration: an
# edge with no stated reason is an edge nobody can safely delete later.

SAME_YEAR_PREREQS = (
    ("biomechanics-forces-in-the-body", "drawing-and-adding-forces",
     "§7.1 B2 ⇄ requires P4 Forces — you cannot compute a moment in an arm "
     "without adding forces first."),
    ("how-breathing-works", "pressure-force-over-area",
     "§7.1 B4 ⇄ requires P5 Pressure — breathing IS a pressure-difference "
     "mechanism."),
    ("the-photosynthesis-reaction", "reactions-rearrange-atoms",
     "default_sequence.py: B7 requires the cell (Y7 B1) and the reaction "
     "(Y8 C4). Photosynthesis is a chemical reaction before it is a plant "
     "process."),
    ("aerobic-respiration", "reactions-rearrange-atoms",
     "As B7 — respiration is a chemical reaction and cannot precede what a "
     "reaction is."),
)


# ═══════════════════════════════════════════════════════════════════════════
# Reading structure.py
# ═══════════════════════════════════════════════════════════════════════════

def _unit_lessons():
    """unit code → [lesson slug, ...] in declared slot order."""
    return {code: [s[0] for s in lessons]
            for code, _s, _t, _d, _a, _y, lessons in structure.UNITS}


def _owner_of_slug():
    """slug → the unit code that OWNS it.

    A §4.6 reference slot is not an owner — it points at a lesson written
    somewhere else. Every distinct slug must have exactly one owner, or a
    ``requires`` edge naming that slug has no single answer.
    """
    owners = {}
    for code, _s, _t, _d, _a, _y, lessons in structure.UNITS:
        for slot in lessons:
            if len(slot) > 3:          # owned_by present → a reference slot
                continue
            if slot[0] in owners:
                raise ValueError(
                    "half_terms: lesson slug %r is owned by both %s and %s. "
                    "Slugs are permanent and globally unique (§8.4); two "
                    "owners means a `requires` edge naming it has no single "
                    "answer." % (slot[0], owners[slot[0]], code))
            owners[slot[0]] = code
    return owners


_UNIT_LESSONS = _unit_lessons()
_OWNER = _owner_of_slug()
_UNIT_DISCIPLINE = {code: disc
                    for code, _s, _t, disc, _a, _y, _l in structure.UNITS}


# ═══════════════════════════════════════════════════════════════════════════
# INTRA_YEAR_UNIT_ORDER
# ═══════════════════════════════════════════════════════════════════════════

def _declaration_order():
    """(year, discipline) → unit codes, in structure.py declaration order."""
    out = {}
    for code, _s, _t, disc, _a, _y, _lessons in structure.UNITS:
        out.setdefault((DEFAULT_SEQUENCE_V1[code], disc), []).append(code)
    return out


def _apply_overrides(order, strict=True):
    """Lay ORDER_OVERRIDES over declaration order, permutation-checked.

    A typo in an override — a dropped unit, a duplicate, a code that belongs to
    another year — must stop the import. Silently dropping a unit here would
    delete four to nine lessons from the scheme of work and nothing downstream
    would notice: the counts would simply be smaller.

    ``strict=False`` is for one caller only: ``recompute()``, running under a
    SUBSTITUTED sequence (a real school's scheme, in §9's reorder proof). There
    the permutation check is wrong rather than lenient — the override describes
    the DEFAULT's Year 8 physics, and a school that teaches those units in other
    years genuinely has a different set in that lane. Raising would mean the
    module could not be imported under any sequence but its own, which is the
    opposite of what §4.5 promises. So the override is applied to the part of
    itself that still exists, and the rest of the lane keeps declaration order.
    """
    for key, override in sorted(ORDER_OVERRIDES.items()):
        year, disc = key
        declared = order.get(key)

        if not strict:
            if not declared:
                continue
            present = [c for c in override if c in declared]
            rest = [c for c in declared if c not in present]
            order[key] = present + rest
            continue

        if declared is None:
            raise ValueError(
                "half_terms.ORDER_OVERRIDES names (Y%d, %s), which the default "
                "sequence has no units in. Either the override is stale or "
                "default_sequence.py moved something." % (year, disc))
        seen = set()
        dupes = sorted({c for c in override if c in seen or seen.add(c)})
        missing = sorted(set(declared) - set(override))
        extra = sorted(set(override) - set(declared))
        if dupes or missing or extra:
            parts = []
            if dupes:
                parts.append("listed twice: %s" % ", ".join(dupes))
            if missing:
                parts.append("dropped: %s" % ", ".join(missing))
            if extra:
                parts.append("not in this year/discipline: %s"
                             % ", ".join(extra))
            raise ValueError(
                "half_terms.ORDER_OVERRIDES[(%d, %r)] is not a permutation of "
                "the %d units the default sequence puts there (%s) — %s. An "
                "override may REORDER units; it may never change which units "
                "are taught." % (year, disc, len(declared),
                                 ", ".join(declared), "; ".join(parts)))
        order[key] = list(override)
    return order


def _bridge_last(order):
    """§7.6: a Year 9 beyond-statutory unit is taught last in its discipline.

    Applied after ORDER_OVERRIDES, and deliberately wins over them: half term 6
    is where the bridge group goes, and an order that put it elsewhere would
    make ``academic_week`` and ``half_term`` disagree on the same row.
    """
    bridge = beyond_statutory_units()
    if not bridge:
        return order
    for (year, disc), codes in order.items():
        if year != 9:
            continue
        core = [c for c in codes if c not in bridge]
        tail = [c for c in codes if c in bridge]
        if not core:
            raise ValueError(
                "half_terms: Y9 %s is entirely beyond-statutory bridge units "
                "(%s). §7.6's bridge group is what a Shape-B school swaps IN "
                "alongside statutory content, never the whole of a year — "
                "there is nothing left to spread across half terms 1–5."
                % (disc, ", ".join(tail)))
        order[(year, disc)] = core + tail
    return order


INTRA_YEAR_UNIT_ORDER = _bridge_last(_apply_overrides(_declaration_order()))


# ═══════════════════════════════════════════════════════════════════════════
# The split
# ═══════════════════════════════════════════════════════════════════════════

def split_sizes(n, parts=len(HALF_TERMS)):
    """Split ``n`` lessons into ``parts`` chunks, largest remainder, big first.

    A pure function of n, so the same stream length always splits the same way
    and the placement can be reasoned about without reading the curriculum.

    Chunk sizes differ by at most one. The larger chunks come first because the
    autumn half terms are the longest uninterrupted teaching stretch an English
    school year has, and the summer ones are the most heavily eaten by
    assessment weeks, transition days and trips. Front-loading is the shape a
    department plans to anyway.
    """
    if n < parts:
        raise ValueError(
            "half_terms.split_sizes: cannot spread %d lessons across %d half "
            "terms without leaving one empty. A discipline with fewer lessons "
            "than half terms is a curriculum finding, not an arithmetic one."
            % (n, parts))
    base, rem = divmod(n, parts)
    return [base + 1] * rem + [base] * (parts - rem)


def _cuts_from_sizes(sizes):
    """The internal cut positions — 5 of them for 6 chunks.

    Chunk k covers stream positions ``(cuts[k-1], cuts[k]]``, 1-indexed.
    """
    cuts, run = [], 0
    for size in sizes[:-1]:
        run += size
        cuts.append(run)
    return cuts


def _unit_boundaries(codes):
    """Cumulative lesson counts at the end of each unit, ends excluded.

    Position 0 and position n are not boundaries a cut can usefully move to —
    they are the ends of the stream, and a cut there empties a chunk.
    """
    out, run = [], 0
    for code in codes[:-1]:
        run += len(_UNIT_LESSONS[code])
        out.append(run)
    return out


def _sizes_from_cuts(cuts, n):
    edges = [0] + list(cuts) + [n]
    return [edges[i + 1] - edges[i] for i in range(len(edges) - 1)]


def _cuts_valid(cuts, n):
    """Strictly increasing, and no chunk empty at either end."""
    prev = 0
    for cut in cuts:
        if cut <= prev:
            return False
        prev = cut
    return prev < n


def _half_term_at(cuts, position):
    """Which chunk a 1-indexed stream position falls in."""
    return bisect.bisect_left(cuts, position) + 1


# ═══════════════════════════════════════════════════════════════════════════
# The snap search — unit coherence, subject to balance
# ═══════════════════════════════════════════════════════════════════════════
#
# Each internal cut may either stay where the arithmetic put it or move onto a
# unit boundary within SNAP_DISTANCE. That is a per-cut binary choice, and the
# first version of this module made each choice locally and greedily: snap
# whenever you can. It produced a defensible split per discipline and a bad one
# per YEAR, because three disciplines snapping in the same direction stack their
# deviations — Year 8 came out with 16 lessons in HT1 against 10 in HT5, which a
# real school would feel.
#
# The fix is to stop deciding one lane at a time. A year has three disciplines
# and five internal cuts each, so at most 2^15 = 32768 combinations — small
# enough to enumerate exhaustively and pick the genuinely best one, with no
# heuristic to be wrong about. See RULED TRADE-OFF in the module docstring for
# the objective and its priority order.

SNAP_DISTANCE = 1


def _snap_options(base_cuts, boundaries):
    """Per cut, the options in a FIXED order: ``(stay,)`` or ``(stay, snap)``.

    Order matters and is load-bearing twice over: option 0 is always "stay", so
    "did this cut snap?" is just ``chosen != options[0]``, and the search's
    final tie-break can prefer not-snapping without a second lookup.

    A boundary exactly on the cut is not an option — there is nothing to
    decide. Ties (a boundary one lesson either side) take the earlier boundary.
    """
    options = []
    for cut in base_cuts:
        near = [b for b in boundaries
                if b != cut and abs(b - cut) <= SNAP_DISTANCE]
        if near:
            options.append((cut, min(near, key=lambda b: (abs(b - cut), b))))
        else:
            options.append((cut,))
    return options


def _search_year(year, lanes, edges):
    """Choose the snap combination for one whole year.

    ``lanes`` is an ordered list of per-discipline dicts (``n``, ``options``);
    ``edges`` are the SAME_YEAR_PREREQS constraints that live inside this year,
    pre-resolved to (lane, position) pairs.

    Returns ``(cuts_per_lane, flags, totals)``. Deterministic by construction:
    lanes arrive in ``structure.DISCIPLINES`` order, options are ordered tuples,
    ``itertools.product`` is ordered, and the winner is chosen by ``min`` over a
    total order with no ties left in it.
    """
    flat_options = [opt for lane in lanes for opt in lane["options"]]
    best = None

    for combo in itertools.product(*flat_options):
        cuts_per_lane, ok, at = [], True, 0
        for lane in lanes:
            cuts = combo[at:at + len(lane["options"])]
            at += len(lane["options"])
            # Guard, unchanged in intent: a snap may not reorder cuts or empty
            # a chunk. Now it rejects a whole combination rather than one move,
            # which is stricter and simpler — there is no half-applied state.
            if not _cuts_valid(cuts, lane["n"]):
                ok = False
                break
            cuts_per_lane.append(cuts)
        if not ok:
            continue

        if not all(_edge_ok(edge, cuts_per_lane) for edge in edges):
            continue

        totals = [0] * len(HALF_TERMS)
        for lane, cuts in zip(lanes, cuts_per_lane):
            for i, size in enumerate(_sizes_from_cuts(cuts, lane["n"])):
                totals[i] += size

        flags = tuple(chosen != opts[0]
                      for chosen, opts in zip(combo, flat_options))
        key = (max(totals) - min(totals), -sum(flags), flags)
        if best is None or key < best[0]:
            best = (key, cuts_per_lane, flags, totals)

    if best is None:
        raise ValueError(
            "half_terms: no half-term split of Year %d satisfies its "
            "cross-discipline prerequisites (%s). Every one of the %d snap "
            "combinations was rejected. This is an ORDER_OVERRIDES problem, not "
            "an arithmetic one: a unit has to move so the prerequisite is "
            "taught earlier." % (
                year, ", ".join(e["label"] for e in edges) or "none",
                len(list(itertools.product(*flat_options)))))

    return best[1], best[2], best[3]


def _edge_ok(edge, cuts_per_lane):
    """One SAME_YEAR_PREREQS edge, evaluated against a candidate combination."""
    dep = _edge_ht(edge["dependent"], cuts_per_lane)
    pre = _edge_ht(edge["prerequisite"], cuts_per_lane)
    return dep >= pre


def _edge_ht(side, cuts_per_lane):
    lane, position = side
    if lane is None:                     # a §7.6 bridge lesson — fixed at HT6
        return position
    return _half_term_at(cuts_per_lane[lane], position)


# ═══════════════════════════════════════════════════════════════════════════
# derive()
# ═══════════════════════════════════════════════════════════════════════════

def _assert_prereq_slugs_resolve():
    """Run BEFORE derive(), which reads SAME_YEAR_PREREQS as a constraint.

    A slug that resolves to nothing would otherwise be silently dropped from
    the search — the split would still be produced, and the constraint it was
    supposed to enforce would simply not exist.
    """
    for dependent, prereq, _why in SAME_YEAR_PREREQS:
        for slug, role in ((dependent, "dependent"), (prereq, "prerequisite")):
            if slug not in _OWNER:
                raise ValueError(
                    "half_terms.SAME_YEAR_PREREQS names %r as the %s of an "
                    "edge, and no unit in structure.py owns that slug. Slugs "
                    "are permanent (§8.4): if a lesson was renamed, its slug "
                    "was not." % (slug, role))


def derive():
    """Place every lesson slot in a half term.

    Returns ``{(unit_code, lesson_slug): (year, half_term)}`` — 183 entries,
    one per slot declared in ``structure.py``, including §4.6 reference slots.
    See the module docstring for why the key is a pair and not a slug.

    Deterministic and total: no randomness, no I/O, and no dependence on set or
    dict iteration order anywhere in the search.
    """
    bridge = beyond_statutory_units()
    placement = {}
    report = {}

    for year in YEARS:
        lanes = []
        for disc in structure.DISCIPLINES:
            codes = INTRA_YEAR_UNIT_ORDER.get((year, disc))
            if not codes:
                continue
            # §7.6 branch: Year 9 bridge units are lifted out of the arithmetic
            # entirely and stamped with half term 6. They are already last in
            # the order (see _bridge_last), so the stream stays monotonic.
            #
            # They are also excluded from the BALANCE objective, deliberately.
            # A bridge group is what a Shape-B school swaps IN for statutory
            # content it is not teaching (§7.6), so counting it would balance a
            # year no single school actually teaches.
            if year == 9 and bridge:
                core_codes = [c for c in codes if c not in bridge]
                bridge_codes = [c for c in codes if c in bridge]
            else:
                core_codes, bridge_codes = list(codes), []

            stream = [(code, slug)
                      for code in core_codes for slug in _UNIT_LESSONS[code]]
            base_cuts = _cuts_from_sizes(split_sizes(len(stream)))
            lanes.append({
                "discipline":   disc,
                "stream":       stream,
                "n":            len(stream),
                "options":      _snap_options(base_cuts,
                                              _unit_boundaries(core_codes)),
                "bridge_codes": bridge_codes,
            })

        cuts_per_lane, flags, totals = _search_year(
            year, lanes, _year_edges(year, lanes))

        for lane, cuts in zip(lanes, cuts_per_lane):
            edges = [0] + list(cuts) + [lane["n"]]
            for ht in HALF_TERMS:
                for slot in lane["stream"][edges[ht - 1]:edges[ht]]:
                    placement[slot] = (year, ht)
            for code in lane["bridge_codes"]:
                for slug in _UNIT_LESSONS[code]:
                    placement[(code, slug)] = (year, BRIDGE_HALF_TERM)

        report[year] = {
            "totals":    totals,
            "spread":    max(totals) - min(totals),
            "snapped":   sum(flags),
            "available": sum(1 for lane in lanes
                             for opt in lane["options"] if len(opt) > 1),
        }

    return placement, report


def _year_edges(year, lanes):
    """SAME_YEAR_PREREQS constraints that live entirely inside one year.

    Resolved once, to (lane index, stream position), so the inner search loop
    does arithmetic rather than lookups.
    """
    out = []
    for dependent, prereq, why in SAME_YEAR_PREREQS:
        dep = _locate(dependent, year, lanes)
        pre = _locate(prereq, year, lanes)
        if dep is None or pre is None:
            continue                      # cross-year: a different gate's job
        out.append({"dependent": dep, "prerequisite": pre,
                    "label": "%s requires %s (%s)" % (dependent, prereq, why)})
    return out


def _locate(slug, year, lanes):
    """(lane index, position) for a slug in this year, or None if it is not.

    A §7.6 bridge lesson has no position in the arithmetic at all — it is
    stamped HT6 whatever the cuts do — so it comes back as ``(None, HT6)``.
    """
    unit = _OWNER[slug]
    if DEFAULT_SEQUENCE_V1[unit] != year:
        return None
    for i, lane in enumerate(lanes):
        if unit in lane["bridge_codes"]:
            return (None, BRIDGE_HALF_TERM)
        for position, (code, s) in enumerate(lane["stream"], start=1):
            if code == unit and s == slug:
                return (i, position)
    return None


_assert_prereq_slugs_resolve()
_PLACEMENT, SEARCH_REPORT = derive()


def recompute():
    """Re-derive the placement from the CURRENT ``DEFAULT_SEQUENCE_V1``.

    ⚠️ **This exists for §9's reorder proof and for nothing else.** Normal code
    reads the placement computed once at import; a caller that recomputes
    mid-run is changing the published curriculum underneath everything that has
    already read it.

    Why it has to exist. The proof substitutes a real school's whole sequence
    into ``DEFAULT_SEQUENCE_V1`` and rebuilds, asserting that lesson pages do
    not move. Before this function, the placement stayed frozen at its
    import-time value, so the browse layer rendered the ORIGINAL sequence no
    matter what the proof substituted — and the proof passed **for a reason
    unrelated to the invariant it claims to test**, while quietly measuring
    nothing about the browse layer at all.

    That is the same shape of latent flaw §12 already records once, when the
    proof snapshotted its baseline off disk instead of building it. A proof
    that cannot fail is not evidence.

    Returns the new placement; also refreshes ``INTRA_YEAR_UNIT_ORDER`` so the
    two cannot disagree.

    ⚠️ **Not every sequence can be recomputed, and that is correct.** A lane
    with fewer lessons than half terms raises out of ``split_sizes`` — and
    Rainford's real Year 9 biology (three lessons) is exactly such a lane. The
    strict guard is not weakened to let this function run: a six-half-term
    browse layer genuinely cannot be rendered for that year, which is a true
    statement about Rainford, not a bug in the arithmetic. Serving a school its
    own browse layer needs the Phase 5 runtime scheme lookup (§4.5.2), so
    §9's reorder proof uses this only with a perturbation the default's own
    contract can hold.
    """
    global _PLACEMENT, SEARCH_REPORT, INTRA_YEAR_UNIT_ORDER
    INTRA_YEAR_UNIT_ORDER = _bridge_last(
        _apply_overrides(_declaration_order(), strict=False))
    _PLACEMENT, SEARCH_REPORT = derive()
    return _PLACEMENT


def search_report():
    """Per year: the chosen totals, the spread, and snapped-vs-available cuts.

    Exists so the trade-off is inspectable rather than asserted. ``verify_ks3``
    prints it, which is how anyone notices the day a snap stops being possible.
    """
    return {y: dict(r) for y, r in SEARCH_REPORT.items()}


def placement():
    """The derived placement, computed once at import.

    A copy, because callers that mutate a shared curriculum map are exactly the
    bug ``default_sequence.py``'s drift guard exists to prevent.
    """
    return dict(_PLACEMENT)


def half_term_of(slug, unit_code=None):
    """Half term for a lesson.

    ``slug`` alone resolves to the **owning** slot (§4.6): asking for
    ``energy-in-food`` gives you P2's placement, because that is where the
    lesson is written. Pass ``unit_code`` to ask about a particular slot,
    including a reference slot such as B3's copy of that same slug.
    """
    return _resolve(slug, unit_code)[1]


def year_of(slug, unit_code=None):
    """Year for a lesson slot. Same resolution rule as ``half_term_of``."""
    return _resolve(slug, unit_code)[0]


def _resolve(slug, unit_code=None):
    if unit_code is None:
        unit_code = _OWNER.get(slug)
        if unit_code is None:
            raise KeyError(
                "half_terms: %r is not an owned KS3 lesson slug. If you meant "
                "a §4.6 reference slot, pass its unit code — a reference slot "
                "is taught in a different year from the lesson it points at."
                % (slug,))
    try:
        return _PLACEMENT[(unit_code, slug)]
    except KeyError:
        raise KeyError(
            "half_terms: no lesson slot %r in unit %s." % (slug, unit_code))


def by_year_half_term():
    """``{(year, half_term): [lesson_slug, ...]}``, in teaching order.

    ``energy-in-food`` appears twice across the whole mapping — once for B3's
    reference slot and once for P2's lesson — because a teacher teaches both.
    Callers that need slot identity rather than a reading list want
    ``slots_by_year_half_term()``.
    """
    return {k: [slug for _code, slug in v]
            for k, v in slots_by_year_half_term().items()}


def slots_by_year_half_term():
    """``{(year, half_term): [(unit_code, lesson_slug), ...]}``.

    Disciplines are laid out one after another — biology, then chemistry, then
    physics — each in its own teaching order. A half term is three parallel
    streams, not one, and interleaving them would invent a lesson order no
    timetable actually has.
    """
    out = {}
    for _key, codes in sorted(INTRA_YEAR_UNIT_ORDER.items()):
        for code in codes:
            for slug in _UNIT_LESSONS[code]:
                key = _PLACEMENT[(code, slug)]
                out.setdefault(key, []).append((code, slug))
    return out


def counts_by_half_term():
    """``{(year, discipline): [n1, n2, n3, n4, n5, n6]}`` — the distribution.

    What a person actually wants to look at to decide whether the split is
    sane, and what ``verify_ks3.py`` prints.
    """
    out = {(y, d): [0] * len(HALF_TERMS)
           for y in YEARS for d in structure.DISCIPLINES}
    for (code, _slug), (year, ht) in _PLACEMENT.items():
        out[(year, _UNIT_DISCIPLINE[code])][ht - 1] += 1
    return {k: v for k, v in out.items() if sum(v)}


def units_by_half_term(year=None):
    """``{(year, half_term): [unit_code, ...]}`` — which units a half term touches.

    A unit appears under every half term any of its lessons falls in, so a unit
    split across a boundary is visible rather than rounded away.
    """
    out = {}
    for (code, _slug), (yr, ht) in sorted(_PLACEMENT.items()):
        if year is not None and yr != year:
            continue
        seen = out.setdefault((yr, ht), [])
        if code not in seen:
            seen.append(code)
    # Sorted by discipline then by that discipline's own teaching order, so the
    # list reads the way a timetable does rather than the way a dict iterates.
    for key, codes in out.items():
        codes.sort(key=lambda c: (
            _UNIT_DISCIPLINE[c],
            INTRA_YEAR_UNIT_ORDER[(key[0], _UNIT_DISCIPLINE[c])].index(c)))
    return out


# ═══════════════════════════════════════════════════════════════════════════
# Import-time gates
# ═══════════════════════════════════════════════════════════════════════════
#
# Everything below fails the import, naming the offender. A half-term map that
# is wrong in a way nothing checks is worse than no half-term map at all: it
# would be seeded into scheme_of_work_entries and read by a teacher as fact.

def _assert_every_slot_placed():
    declared = set()
    for code, _s, _t, _d, _a, _y, lessons in structure.UNITS:
        for slot in lessons:
            declared.add((code, slot[0]))

    expected = structure.totals()["lessons"]
    if len(declared) != expected:
        raise ValueError(
            "half_terms: structure.py declares %d lesson slots but only %d are "
            "distinct (unit, slug) pairs — a unit lists the same slug twice."
            % (expected, len(declared)))

    missing = sorted(declared - set(_PLACEMENT))
    extra = sorted(set(_PLACEMENT) - declared)
    if missing or extra:
        parts = []
        if missing:
            parts.append("never placed: %s" % ", ".join(
                "%s/%s" % s for s in missing[:10]))
        if extra:
            parts.append("placed but not declared: %s" % ", ".join(
                "%s/%s" % s for s in extra[:10]))
        raise ValueError(
            "half_terms: the placement does not cover structure.py's %d lesson "
            "slots exactly once — %s. Every slot is taught, including §4.6 "
            "reference slots." % (expected, "; ".join(parts)))


def _assert_every_half_term_used():
    """The interleaving guarantee.

    An empty half term means a discipline vanishes for six or seven weeks. A
    school timetables biology, chemistry and physics every half term of KS3, so
    a default that does not is not a default anybody can teach from.
    """
    empty = []
    for (year, disc), counts in sorted(counts_by_half_term().items()):
        for ht, n in zip(HALF_TERMS, counts):
            if n == 0:
                empty.append("Y%d %s HT%d" % (year, disc, ht))
    if empty:
        raise ValueError(
            "half_terms: %d (year, discipline, half term) slot(s) are empty — "
            "%s. Every discipline must appear in every half term of every "
            "year, or the default silently drops a subject off a timetable."
            % (len(empty), ", ".join(empty)))


def _assert_monotonic():
    """Half term never goes backwards along a discipline's teaching stream."""
    for (year, disc), codes in sorted(INTRA_YEAR_UNIT_ORDER.items()):
        last, last_slot = 0, None
        for code in codes:
            for slug in _UNIT_LESSONS[code]:
                ht = _PLACEMENT[(code, slug)][1]
                if ht < last:
                    raise ValueError(
                        "half_terms: Y%d %s goes backwards — %s/%s is HT%d but "
                        "%s/%s before it is HT%d. Teaching order and half-term "
                        "order are the same order."
                        % (year, disc, code, slug, ht,
                           last_slot[0], last_slot[1], last))
                last, last_slot = ht, (code, slug)


def _assert_same_year_prereqs():
    """Every ⇄ edge inside one year is honoured by the half-term split.

    The search already refuses any combination that breaks one of these, so
    this can only fail if the search itself is wrong. That is exactly why it is
    here: it checks the OUTPUT, not the intention.
    """
    problems = []
    for dependent, prereq, why in SAME_YEAR_PREREQS:
        dy, dht = _resolve(dependent)
        py, pht = _resolve(prereq)
        if dy != py:
            problems.append(
                "%s (Y%d) and %s (Y%d) are not in the same year — this list is "
                "for edges INSIDE one year; a cross-year edge belongs to "
                "verify_ks3.py's forward-reference gate"
                % (dependent, dy, prereq, py))
        elif dht < pht:
            problems.append(
                "%s is taught in Y%d HT%d but requires %s, which is not taught "
                "until Y%d HT%d — %s" % (dependent, dy, dht, prereq, py, pht, why))
    if problems:
        raise ValueError(
            "half_terms: %d cross-discipline prerequisite(s) broken by the "
            "half-term split — %s. Fix ORDER_OVERRIDES; do not delete the edge."
            % (len(problems), "; ".join(problems)))


def check_authored_requires(units):
    """Authored lesson-level ``requires`` edges, checked within one year.

    Called by ``verify_ks3.py`` §10 rather than run at import: reading authored
    lessons means ``ks3_data.build_units()``, and importing the package from
    inside one of its own modules is the circular import this module refuses to
    create (see the module docstring).

    Returns a list of problem strings — empty means clean. Cross-year edges are
    skipped: those are ``verify_ks3.py``'s forward-reference gate, and a year
    boundary already orders them.
    """
    problems = []
    for unit in units:
        code = unit["code"]
        for lesson in unit["lessons"]:
            slot = (code, lesson["slug"])
            if slot not in _PLACEMENT:
                continue
            dy, dht = _PLACEMENT[slot]
            # ⊕ MRB-245 — a `requires` edge may be a bare slug or a
            # `{unit, lesson}` record, which is the shape `references` has
            # taken since B1 and the one b7-03 uses to require B3's
            # `food-tests`. Only the slug is a key here: `_OWNER` and
            # `_PLACEMENT` are keyed by slug and already know which unit owns
            # it, so the `unit` field is confirmation rather than information.
            # Normalised locally rather than imported from `build_ks3`, because
            # this module deliberately imports nothing from the package it
            # describes — see the module docstring.
            for req in [r.get("lesson") if isinstance(r, dict) else r
                        for r in (lesson.get("requires") or [])]:
                owner = _OWNER.get(req)
                if owner is None:
                    problems.append(
                        "%s/%s requires %r, which no unit owns"
                        % (code, lesson["slug"], req))
                    continue
                py, pht = _PLACEMENT[(owner, req)]
                if py != dy:
                    continue
                if dht < pht:
                    problems.append(
                        "%s/%s is Y%d HT%d but requires %s/%s, taught Y%d HT%d"
                        % (code, lesson["slug"], dy, dht, owner, req, py, pht))
    return problems


_assert_every_slot_placed()
_assert_every_half_term_used()
_assert_monotonic()
_assert_same_year_prereqs()
