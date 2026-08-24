"""ks3_art — the per-unit art and instrument registry.

═══════════════════════════════════════════════════════════════════════════
WHY THIS PACKAGE EXISTS
═══════════════════════════════════════════════════════════════════════════

Every KS3 unit used to register its drawers and its instruments inside
``build_ks3.py``. That made the generator a file every content lane had to
edit, which made two lanes building two units at the same time a merge
conflict by construction — and worse than a conflict, because the conflicting
hunks are dict entries whose "keep both sides" resolution LOOKS correct while
silently keeping one lane's renderer and dropping the other's.

``splice_instruments.py`` was the workaround: authors wrote fragment files and
a script spliced them into the engine, "because five of the engine's files
have a single-writer rule and several agents editing build_ks3.py concurrently
is how you lose a renderer without noticing". That script is now disarmed and
kept only as a record. This package is the structural fix it was standing in
for.

═══════════════════════════════════════════════════════════════════════════
THE RULE
═══════════════════════════════════════════════════════════════════════════

**One unit, one module. Two units never appear in one file.**

A unit module (``b1.py`` … ``c2.py``) owns that unit's drawers, its component
families, and its registrations. Adding a unit means adding ONE NEW FILE:
modules are DISCOVERED, not listed, so there is no shared manifest to edit and
therefore nothing for two lanes to collide on.

Two modules are shared, and both say so at the top of themselves:

  ``kit.py``   primitives used by more than one unit
  ``core.py``  registrations for kinds that more than one unit authors

Changing either changes more than one unit's output. See
``docs/ks3/worktrees.md`` before you do.

═══════════════════════════════════════════════════════════════════════════
WHAT A UNIT MODULE MAY DECLARE
═══════════════════════════════════════════════════════════════════════════

All optional; all plain dicts at module scope.

  ``ART``              figure art name  -> drawer function
  ``KIND_SHELL``       instrument kind  -> (modifier class, marker attributes)
  ``KIND_FN``          instrument kind  -> the function that draws it
  ``KIND_HEAD_START``  kind -> the head counter's resting count
  ``KIND_HEAD_TOTAL``  kind -> the head counter's denominator
  ``KIND_HEAD_FROM``   kind -> a callable deriving the head readout

═══════════════════════════════════════════════════════════════════════════
THE GATES, AND WHAT EACH ONE IS FOR
═══════════════════════════════════════════════════════════════════════════

1. DUPLICATE FAMILY ACROSS MODULES → ``load()`` raises.
   A silent last-one-wins is exactly how two lanes ship a component neither
   intended: both register ``bench``, import order decides, and the loser's
   instrument renders as the winner's with nobody told.

2. REGISTERED BUT NEVER PLACED → ``check_placements()`` reports.
   A family nothing places is on no built page, so the parity gate cannot see
   it and cannot contradict it. That is the hole SYSTEM and CLASSIFY came
   through.

3. PLACED BUT UNREGISTERED → ``check_placements()`` reports.
   The other half of the same hole, and the half that reaches students: a
   figure whose art has no drawer, or an instrument kind nothing draws.
"""

import collections
import importlib
import pkgutil

TABLES = ("ART", "KIND_SHELL", "KIND_FN",
          "KIND_HEAD_START", "KIND_HEAD_TOTAL", "KIND_HEAD_FROM")

# Which tables name a FAMILY — a thing a lesson can place on a page, and so a
# thing gates 2 and 3 apply to. The head-counter tables are metadata ABOUT a
# kind rather than a declaration of one, so they are checked differently: a key
# there must name a kind that IS registered, but it need not itself be placed.
FAMILY_TABLES = ("ART", "KIND_SHELL", "KIND_FN")

_ATTR = {"ART": "art", "KIND_SHELL": "kind_shell", "KIND_FN": "kind_fn",
         "KIND_HEAD_START": "kind_head_start",
         "KIND_HEAD_TOTAL": "kind_head_total",
         "KIND_HEAD_FROM": "kind_head_from"}


class Registry(object):
    """The merged tables, plus which module registered each key."""

    __slots__ = ("art", "kind_shell", "kind_fn", "kind_head_start",
                 "kind_head_total", "kind_head_from", "source", "modules")

    def __init__(self):
        self.art = {}
        self.kind_shell = {}
        self.kind_fn = {}
        self.kind_head_start = {}
        self.kind_head_total = {}
        self.kind_head_from = {}
        self.source = {}          # (table, key) -> module name
        self.modules = []


def discover():
    """Every module in this package, unit modules and shared ones alike.

    Discovered rather than listed ON PURPOSE. A hand-written module list is a
    shared file, and a shared file is the thing this package exists to remove:
    two lanes adding two units would both append a line to it and conflict on
    the very edit the split was supposed to make unnecessary.
    """
    return sorted(m.name for m in pkgutil.iter_modules(__path__)
                  if not m.name.startswith("_"))


def load():
    """Import every module, merge the tables, refuse a duplicate family."""
    reg = Registry()
    clashes = []
    for name in discover():
        mod = importlib.import_module("%s.%s" % (__name__, name))
        reg.modules.append(name)
        for table in TABLES:
            entries = getattr(mod, table, None)
            if not entries:
                continue
            target = getattr(reg, _ATTR[table])
            for key, value in entries.items():
                prev = reg.source.get((table, key))
                if prev is not None:
                    clashes.append((table, key, prev, name))
                    continue
                reg.source[(table, key)] = name
                target[key] = value

    if clashes:
        raise SystemExit(
            "ks3_art: %d family name(s) registered by two modules:\n%s\n"
            "One family, one owner. Rename one of them — a silent "
            "last-one-wins ships whichever module imported second and drops "
            "the other, with nothing said."
            % (len(clashes), "\n".join(
                "   %-16s %-24s registered by %s AND %s" % c for c in clashes)))

    # ── ⊕ MRB-279, 21 Aug 2026 · TWO FAMILIES MAY NOT WEAR ONE SHELL CLASS ──
    #
    # The check above compares family NAMES — the dict keys. This one compares
    # the CSS class each family renders into, which is a VALUE, and which
    # nothing was looking at.
    #
    # THE NEAR MISS. c5-02's decomposition sorter was assigned the family
    # `decomp-sort` and reached for the shell class `ks3-dsort-block` — which
    # `ks3_art/b5.py` had already registered for `disperse-sort`. Two families
    # wearing one class means one unit's stylesheet block lands on the other
    # unit's instrument, and it lands SILENTLY: both pages render, and only a
    # browser open on the biology page would ever show it.
    #
    # It was caught by a human reading b5.py, not by a gate. The documented
    # pre-check is a grep across `ks3_art/*.py`, `shared/ks3.js` and
    # `shared/ks3.css` — and it structurally CANNOT see this case, because a
    # shell-only family has no CSS rule and no JS wiring to grep for. It
    # exists in KIND_SHELL and nowhere else.
    #
    # So the pre-check is replaced by an assertion over KIND_SHELL itself,
    # which is the only place the truth lives. Cheap now; cheaper than the
    # next collision, which would be found in a browser or not at all.
    shells = {}
    shell_clashes = []
    for fam, value in getattr(reg, _ATTR["KIND_SHELL"]).items():
        cls = value[0] if isinstance(value, (tuple, list)) and value else value
        if not isinstance(cls, str):
            continue
        first = cls.split()[0] if cls.split() else cls
        if first in shells:
            other = shells[first]
            shell_clashes.append(
                (first, other, reg.source.get(("KIND_SHELL", other), "?"),
                 fam, reg.source.get(("KIND_SHELL", fam), "?")))
        else:
            shells[first] = fam

    if shell_clashes:
        raise SystemExit(
            "ks3_art: %d shell class(es) registered by two FAMILIES:\n%s\n"
            "One shell class, one family. A shared class puts one unit's "
            "stylesheet block on another unit's instrument, and does it "
            "silently — both pages still render, and only a browser open on "
            "the other page would show it. Rename one family's class."
            % (len(shell_clashes), "\n".join(
                "   %-22s %s (ks3_art/%s.py) AND %s (ks3_art/%s.py)" % c
                for c in shell_clashes)))
    return reg


def check_placements(reg, units, generic_kinds=(), block_type_kinds=()):
    """Gates 2 and 3: registration and placement must agree, both ways.

    ``units`` is ``ks3_data.build_units()``. ``generic_kinds`` are kinds drawn
    by the generic prompt/options branch and so legitimately unregistered;
    ``block_type_kinds`` are drawn by their block type (``confrontation``).

    Returns a list of problem strings — the caller decides when to raise, so
    these join the rest of ``validate()``'s findings in one report rather than
    killing the build on the first one.
    """
    placed_kinds, placed_art = set(), set()
    where = collections.defaultdict(set)
    for unit in units:
        for lesson in unit["lessons"]:
            for a in (lesson.get("activities") or []):
                if a.get("kind"):
                    placed_kinds.add(a["kind"])
                    where[a["kind"]].add(unit["code"])
            for f in (lesson.get("figures") or []):
                if f.get("art"):
                    placed_art.add(f["art"])
                    where[f["art"]].add(unit["code"])
            # ⊕ P4 (MRB-223), 24 Aug 2026 — A FORMULA BLOCK MAY NAME ART.
            #
            # `figures[]` was the only place a drawer could be placed from,
            # because `balance` was the only figure `r_formula` could draw
            # and it needed no drawer. Physics arrives with five formula
            # figures that are neither a triangle nor a balance — three
            # aligned bars, two opposed panels, a beam beside a graph that
            # bends, a stack of fluid layers — and each is drawn by its own
            # unit's module and named from `core[].figure.art`.
            #
            # Without this the gate reports every one of them as "registered
            # but never placed", which is FALSE and, worse, false in the
            # direction that reads as a real finding: a lane would delete a
            # drawer that is on four built pages. Scanning the block is the
            # honest fix — the gate asks whether a family reaches a page,
            # and this is one of the ways a family reaches a page.
            for b in (lesson.get("core") or []):
                fig = b.get("figure") if isinstance(b, dict) else None
                if isinstance(fig, dict) and fig.get("art"):
                    placed_art.add(fig["art"])
                    where[fig["art"]].add(unit["code"])

    problems = []
    excused = set(generic_kinds) | set(block_type_kinds)

    # ── gate 3 · placed but unregistered ────────────────────────────────
    for kind in sorted(placed_kinds - set(reg.kind_fn) - excused):
        problems.append(
            "activity kind %r is authored in %s but no ks3_art module "
            "registers a KIND_FN for it, so the page would ship the shell "
            "around the generic branch — the C1 defect (MRB-228)."
            % (kind, ", ".join(sorted(where[kind]))))

    # ── gate 2 · registered but never placed ────────────────────────────
    for table in FAMILY_TABLES:
        entries = getattr(reg, _ATTR[table])
        placed = placed_art if table == "ART" else placed_kinds
        for key in sorted(set(entries) - placed):
            problems.append(
                "%s registers %r (in ks3_art/%s.py) but no lesson places it. "
                "An unplaced family is on no built page, so the parity gate "
                "cannot see it and cannot contradict it."
                % (table, key, reg.source.get((table, key), "?")))

    # ── head-counter metadata must describe a kind that exists ──────────
    for table in ("KIND_HEAD_START", "KIND_HEAD_TOTAL", "KIND_HEAD_FROM"):
        for key in sorted(set(getattr(reg, _ATTR[table]))
                          - set(reg.kind_fn) - excused):
            problems.append(
                "%s carries a row for %r, which no module registers as an "
                "instrument. The head counter would describe nothing."
                % (table, key))

    return problems
