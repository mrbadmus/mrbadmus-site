"""KS3 content package — architecture.md §8.3.

    "KS3 uses a package with one module per unit. ~183 lessons across three
     files would be unreviewable, unmergeable, and impossible to gate. One
     module per unit matches the release increment and the review gate."

**How a unit becomes a page.** `structure.py` declares all 33 units and all 183
lesson slots. Authored units live in their own modules and export a single
`UNIT` dict. `build_units()` merges the authored content over the skeleton:

- a lesson present in an authored module  → a full lesson page
- a lesson slot with no authored content  → an honest **coming soon** page

Structure-first (§11 decision 8): every unit and lesson slot is routable from
day one. A student never meets a broken link, and a teacher can see the whole
shape of the curriculum before it is written.

Authored modules are discovered by name, in sorted order, so the build is
deterministic.
"""

import importlib
import pkgutil

from . import structure
from .default_sequence import DEFAULT_SEQUENCE_V1

# Modules in this package that are NOT unit modules.
_NON_UNIT_MODULES = {"structure", "default_sequence", "half_terms",
                     "school_schemes", "substatements", "quantities"}


def _authored_modules():
    """Unit modules present in this package, in sorted (deterministic) order."""
    found = {}
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if mod in _NON_UNIT_MODULES or mod.startswith("_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        unit = getattr(m, "UNIT", None)
        if unit is None:
            continue
        found[unit["code"]] = unit
    return found


def build_units():
    """All 33 units, skeleton merged with whatever has been authored.

    Every unit dict has `lessons`, a list in default teaching order. Each lesson
    carries `authored: True|False`. Unauthored lessons carry only identity
    fields — slug, title, family — which is exactly what a coming-soon page
    needs.
    """
    skeleton = structure.unit_index()
    authored = _authored_modules()
    units = []

    for code, sk in skeleton.items():
        auth = authored.get(code)
        auth_lessons = {l["slug"]: l for l in (auth or {}).get("lessons", [])}

        lessons = []
        for slot in sk["lesson_slots"]:
            # §4.6 single-source: a referenced slot renders as a cross-link to
            # the owning unit's page. It is never a second copy of the lesson.
            if slot.get("owned_by"):
                lessons.append({
                    "slug": slot["slug"],
                    "title": slot["title"],
                    "family": slot["family"],
                    "unit": sk["slug"],
                    "discipline": sk["discipline"],
                    "authored": False,
                    "reference_to": slot["owned_by"],
                })
                continue

            lesson = auth_lessons.get(slot["slug"])
            if lesson is not None:
                lesson = dict(lesson)
                lesson["authored"] = True
                # Slot title/family are the skeleton's record; an authored
                # lesson may legitimately refine the title but never the slug.
                lesson.setdefault("family", slot["family"])
                lessons.append(lesson)
            else:
                lessons.append({
                    "slug": slot["slug"],
                    "title": slot["title"],
                    "family": slot["family"],
                    "unit": sk["slug"],
                    "discipline": sk["discipline"],
                    "authored": False,
                })

        # An authored module must not invent lessons the structure does not know
        # about — that would be a silent scope change.
        unknown = set(auth_lessons) - {s["slug"] for s in sk["lesson_slots"]}
        if unknown:
            raise ValueError(
                "Unit %s authors lessons not present in structure.py: %s. "
                "Add the slot to structure.py first — the topic map is the "
                "single record of scope (§7)." % (code, sorted(unknown)))

        units.append({
            "code":            code,
            "slug":            sk["slug"],
            "title":           sk["title"],
            "discipline":      sk["discipline"],
            "statutory_area":  sk["statutory_area"],
            "split_rationale": sk["split_rationale"],
            "references":      sk["references"],
            # The published default (§7, ruled 2026-07-26). There is no
            # fallback layer any more: `default_sequence.py` asserts at import
            # that DEFAULT_SEQUENCE_V1 and structure.py's typical_year are the
            # same mapping for all 33 units, so reading either gives the same
            # answer and a `.get(code, sk["typical_year"])` would be theatre.
            # It is read from the default because the default is the artifact.
            #
            # Still advisory (§4.5): a school's real order comes from
            # scheme_of_work_overrides, and no page path or byte depends on
            # this value. School schemes live in `school_schemes.py` and are
            # deliberately NOT merged in here — a Rainford note must never
            # render on a platform page.
            "typical_year":    DEFAULT_SEQUENCE_V1[code],
            "intro":           (auth or {}).get("intro"),
            "lessons":         lessons,
            "authored_count":  sum(1 for l in lessons if l["authored"]),
        })

    return units


def lesson_registry(units=None):
    """slug → lesson, across the whole key stage. Slugs are globally unique."""
    units = units if units is not None else build_units()
    reg = {}
    for u in units:
        for l in u["lessons"]:
            # Referenced slots point at a lesson owned elsewhere; they are not
            # registry entries of their own (§4.6).
            if l.get("reference_to"):
                continue
            if l["slug"] in reg:
                raise ValueError(
                    "Duplicate lesson slug %r (in %s and %s). Slugs are "
                    "permanent and must be unique across KS3 (§8.4)."
                    % (l["slug"], reg[l["slug"]]["_unit"], u["code"]))
            entry = dict(l)
            entry["_unit"] = u["code"]
            entry["_unit_slug"] = u["slug"]
            reg[l["slug"]] = entry
    return reg


KS3_UNITS = build_units()
