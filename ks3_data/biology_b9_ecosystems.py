"""B9 — Ecosystems and interdependence. Six lessons, Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b9/`, authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/b9/` under the MRB-220 build contract, and against the payload
schema written before dispatch at `docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md`.

    L1 food-chains-and-food-webs        chain-ledger
    L2 predator-and-prey                cycle-runner
    L3 disturbing-a-food-web            remove-a-species
    L4 pollinators-and-food-security    supermarket-shelf
    L5 toxic-build-up-in-a-food-chain   bioaccumulation
    L6 sampling-an-ecosystem            quadrat-bench

**Slugs match `ks3_data/structure.py` character for character.** They are the
join for scheme-of-work rows, progress records and every `requires` edge, and
they are permanent (§8.4).

**Four rail stops per page, all four tick (MRB-249).** The third stop is the
band section and borrows its completion from the instrument via `mirrors`. Full
treatment in `ks3_data/b9/__init__.py`.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10); `draft` → `examiner-reviewed` → `frozen`. Since MRB-221 the field no
longer gates publishing and no page carries a review marker — it records review
position, nothing more.
"""

from .b9 import lessons as _b9_lessons

UNIT = {
    "code":            "B9",
    "slug":            "ecosystems-and-interdependence",
    "title":           "Ecosystems and interdependence",
    "discipline":      "biology",
    "statutory_area":  "Interactions and interdependencies",
    "split_rationale": None,
    "intro":           "Nothing in a habitat feeds itself alone. This unit "
                       "follows the energy from the plants that capture it up "
                       "through everything that eats, watches what happens when "
                       "one species is taken out, and ends with the problem of "
                       "counting a field you cannot count all of.",
    "lessons": _b9_lessons(),
}
