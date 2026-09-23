"""ks4_art — the KS4 figure-drawer registry.

Mirrors `ks3_art`'s discover/merge pattern (adapted — KS4 has one family
table, `ART`, not the six KS3 carries for its instrument shells) rather than
re-implementing it: modules are DISCOVERED, not listed, so adding a module is
adding one new file, and a figure id registered by two modules is a hard
build error rather than a silent last-one-wins.

Every module's primitives come from `ks3_art.kit` — nothing is copied. See
each module's own header for which primitives it reaches for.
"""

import importlib
import pkgutil


class Registry(object):
    __slots__ = ("art", "source", "modules")

    def __init__(self):
        self.art = {}
        self.source = {}       # figure id -> module name
        self.modules = []


def discover():
    """Every module in this package, catalogue included, excluding `_`-prefixed
    private helpers — discovered rather than listed, for the reason
    `ks3_art.discover()` gives: a hand-written module list is a second place
    for a new module's name to go missing from."""
    return sorted(m.name for m in pkgutil.iter_modules(__path__)
                  if not m.name.startswith("_") and m.name != "catalogue")


def load():
    """Import every drawer module, merge their `ART` tables, refuse a
    duplicate id — the same gate `ks3_art.load()` applies to `ART`, for the
    same reason: a figure id registered twice is a silent last-one-wins,
    and whichever module imported second would win with nothing said."""
    reg = Registry()
    clashes = []
    for name in discover():
        mod = importlib.import_module("%s.%s" % (__name__, name))
        reg.modules.append(name)
        entries = getattr(mod, "ART", None)
        if not entries:
            continue
        for key, fn in entries.items():
            prev = reg.source.get(key)
            if prev is not None:
                clashes.append((key, prev, name))
                continue
            reg.source[key] = name
            reg.art[key] = fn

    if clashes:
        raise SystemExit(
            "ks4_art: %d art name(s) registered by two modules:\n%s\n"
            "One art name, one drawer. A silent last-one-wins ships "
            "whichever module imported second and drops the other, with "
            "nothing said."
            % (len(clashes), "\n".join(
                "   %-28s registered by %s AND %s" % c for c in clashes)))
    return reg
