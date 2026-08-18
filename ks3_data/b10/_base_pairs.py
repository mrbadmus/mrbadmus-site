"""The base-pairing figure record for b10-03. One helper, no data of its own.

Separated from the lesson module for the same reason `ks3_data/b9/_oak_wood.py`
is: the figure record is a fixed shape with one variable part, and a helper that
names its arguments is easier to read in the lesson than a nested dict is.

Unlike the oak wood, this one is NOT shared — b10-03 is the only lesson that
draws it, and the rungs are passed in rather than held here, so a second caller
would supply its own. The drawing itself lives in `build_ks3.py::_base_pairs`.
"""


def base_pairs(fig_id, title, desc, caption, rungs, guide_label=None):
    """One `figures[]` record for the base-pairing diagram.

    `rungs` is a list of `(left_base, right_base)` pairs. The drawer raises on a
    rung that pairs two big bases or two small ones, because a constant-width
    molecule is the whole argument the drawing makes.
    """
    return {
        "id": fig_id,
        "kind": "diagram",
        "status": "drawn",
        "art": "base-pairs",
        "title": title,
        "desc": desc,
        "caption": caption,
        "data": {"rungs": rungs,
                 "guide_label": guide_label or "every rung the same width"},
    }
