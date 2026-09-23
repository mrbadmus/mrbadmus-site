"""figlib — Mide's diagram library, as the ONE source of question figures.

Provenance, the changes made on the way in, and how to add a figure:
`figlib/README.md`.

A catalogue record (declarative, no drawing code) names an `art` from
`ART` below and carries that builder's keyword arguments in `params`:

    {"id": "ks4-fig-…", "art": "circuit", "title": "…", "desc": "…",
     "params": {"netlist": [["cell"], ["lamp"]]}}

`draw(rec)` returns the library's own SVG; `figlib.web.to_manifest_svg`
turns that into the manifest's SVG; `figlib.checks` decides whether it may
ship. `build_figures.py` does all three, in that order, for every record.
"""

from . import biology, charts, chemistry, physics

ART = {
    # physics — circuits and symbols (AQA 8463 §4.2.1.1 only)
    "symbol":              physics.symbol_figure,
    "symbol-panel":        physics.symbol_panel,
    "circuit":             physics.question_circuit,
    # physics — forces, fields, waves
    "force-beam":          physics.force_beam,
    "crate-forces":        physics.crate_forces,
    "horseshoe-gap":       physics.horseshoe_gap,
    "motor-coil":          physics.motor_coil_forces,
    "field-point":         physics.field_point,
    "resolution-triangle": physics.resolution_triangle,
    "oscilloscope":        physics.oscilloscope_compare,
    "particle-states":     physics.states_of_matter,
    # chemistry
    "dot-cross":           chemistry.covalent_dotcross,
    "box-monomers":        chemistry.box_monomers,
    # biology
    "food-web":            biology.food_web,
    "dna-ladder":          biology.dna_ladder,
    "moth-pair":           biology.moth_pair,
    "plant-cell":          biology.plant_cell,
    # any subject — data
    "graph":               charts.line_graph,
    "hbar":                charts.hbar_chart,
    "columns":             charts.column_chart,
    "table":               charts.table,
}


def draw(rec):
    """The library SVG for one catalogue record."""
    art = rec.get("art")
    if art not in ART:
        raise ValueError("figure %r names art %r, which figlib does not draw. "
                         "Known: %s" % (rec.get("id"), art, ", ".join(sorted(ART))))
    return ART[art](**(rec.get("params") or {}))
