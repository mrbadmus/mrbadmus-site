"""figlib.ks3_catalogue — every KS3 question-figure record, from every file.

⊕ MRB-352 run 2 (batch 2). `figlib/catalogue_ks3.py` was the one file of
KS3 question figures. Lanes working in parallel now add their records in a
file of their own, `figlib/catalogue_ks3_<lane>.py`, so two lanes never
edit the same list — the pattern `ks4_art.catalogue_modules()` already
uses for KS4. This module DISCOVERS those files rather than listing them,
so a lane adds a file and nothing else.

`CATALOGUE` is `catalogue_ks3.CATALOGUE` followed by every lane file's, in
sorted module order. An id declared twice is refused here, naming both
files — one id, one owner.
"""

import importlib
import os
import pkgutil

_HERE = os.path.dirname(os.path.abspath(__file__))


def catalogue_modules():
    """`catalogue_ks3` and every `catalogue_ks3_*` module in figlib, sorted
    (the base file first)."""
    lanes = sorted(m.name for m in pkgutil.iter_modules([_HERE])
                   if m.name.startswith("catalogue_ks3_"))
    return ["catalogue_ks3"] + lanes


def load():
    records, owner = [], {}
    for name in catalogue_modules():
        mod = importlib.import_module("figlib." + name)
        for rec in getattr(mod, "CATALOGUE", ()):
            fid = rec.get("id")
            if fid in owner:
                raise SystemExit(
                    "figlib: KS3 figure id %r is declared in BOTH figlib/%s.py "
                    "and figlib/%s.py. One id, one owner." % (fid, owner[fid],
                                                             name))
            owner[fid] = name
            records.append(rec)
    return records


CATALOGUE = load()
