"""ks4_art — the KS4 figure CATALOGUE (declarative records only).

⊕ MRB-352 run 2. This package used to hold KS4 drawers of its own
(`circuits.py`, `forces.py`, `graphs.py`, `bonding*.py`,
`oscilloscope_compare.py`) that duplicated what Mide's diagram library
already drew. They are retired: every question figure is now drawn by
`figlib/` (the library, brought into the repo as one package). What stays
here is the declarative layer — `catalogue.py` and any per-lane
`catalogue_<lane>.py` beside it, each a list `CATALOGUE` of records whose
`art` names a builder in `figlib.ART`.

`catalogue_modules()` DISCOVERS those files rather than listing them, so a
lane adds a file and nothing else; `build_figures.py` refuses an id that two
of them declare.
"""

import importlib
import pkgutil


def catalogue_modules():
    """`catalogue` and every `catalogue_*` module in this package, sorted."""
    return sorted(m.name for m in pkgutil.iter_modules(__path__)
                  if m.name == "catalogue" or m.name.startswith("catalogue_"))


def load_catalogue():
    """Every record from every catalogue module, with the module that
    declared it: `[(module_name, record), ...]`."""
    out = []
    for name in catalogue_modules():
        mod = importlib.import_module("%s.%s" % (__name__, name))
        out.extend((name, rec) for rec in getattr(mod, "CATALOGUE", ()))
    return out
