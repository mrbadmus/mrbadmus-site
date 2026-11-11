# -*- coding: utf-8 -*-
"""KS4 lean records: one module per lesson, every route in one record.

    ks4_lessons/lean/<slug with underscores>.py   exports LESSON (docs/lessons/LEAN-RECORD.md)

Read by ks4_lessons/batch_lean.py (which registers the lessons) and lean_ks4.py
(which builds their page source). `ks4_lessons/lean/blocks/` holds the lean
batch's own copies of the shared KS4 blocks, so the other batches keep their
bytes.
"""
import importlib
import os
import pkgutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_RECORDS = None


def records():
    """{slug: LESSON}, only for slugs whose record file exists."""
    global _RECORDS
    if _RECORDS is None:
        found = {}
        for m in sorted(m.name for m in pkgutil.iter_modules([_HERE])):
            if m.startswith("_"):
                continue
            mod = importlib.import_module("%s.%s" % (__name__, m))
            rec = getattr(mod, "LESSON", None)
            if rec is None:
                continue
            if m != rec["slug"].replace("-", "_"):
                raise ValueError("ks4_lessons.lean: %s.py holds the record for %r; the file "
                                 "must be named %s.py" % (m, rec["slug"],
                                                          rec["slug"].replace("-", "_")))
            if rec["slug"] in found:
                raise ValueError("ks4_lessons.lean: two records for %r" % rec["slug"])
            found[rec["slug"]] = rec
        _RECORDS = found
    return _RECORDS
