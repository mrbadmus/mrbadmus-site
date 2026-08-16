# ks3_parity.COMPONENTS entries for `state-matrix` (c1-02 #s-matrix).
#
# Same page constant as the bench — add it once:
#
#     C1_STATES = "chemistry/particles-and-their-behaviour/solids-liquids-and-gases.html"
#
# ⚠️ NO `drive` on any of these, and that is the assertion. The matrix is NOT
# behind the bench's commit gate — Design draws the table in full from the
# first paint and lights the `arrangement` row at rest — so every row below is
# measurable on a page nobody has touched. If one of these ever needs a driver,
# the table has been moved behind something and the section that promised "the
# highlighted row is the one your current bench setting is showing" has stopped
# being able to keep that promise on arrival.

    # ── state-matrix (c1-02 #s-matrix) ──
    # Column heads and row heads share one treatment, because in a matrix the
    # first column is a head as much as the first row is. Mono on band, at the
    # 13px the rest of the key stage's small mono uses.
    dict(name="matrix column head is mono uppercase on band", on=C1_STATES,
         sel=".ks3-smatrix-table thead th",
         props={"font-family": "DM Mono", "font-size": "13px",
                "text-transform": "uppercase",
                "background-color": "#F4E9D8",
                "border-top-color": "#221E1B", "border-top-width": "2px"}),
    # ⚖️ THE LIT ROW, MEASURED AT REST. `arrangement` is lit on arrival —
    # `r_state_matrix` emits it lit at build time by the same rule the runtime
    # uses, so there is no unlit instant before the JS runs. Accent TINT and
    # never the accent fill, and never amber: this is "the bench is showing you
    # this one", not a verdict and not a wrong idea.
    dict(name="the lit matrix row is accent TINT, on arrival", on=C1_STATES,
         sel='.ks3-smatrix-row[data-lit="1"]',
         props={"background-color": "#FCE7DE"}),
    # And the row beside it, so the pair proves there is a visible difference
    # rather than a tint that resolves to the same cream as the card.
    dict(name="an unlit matrix row is CARD", on=C1_STATES,
         sel='.ks3-smatrix-row[data-lit="0"]',
         props={"background-color": "#FFFCF5"}),
    # ⚖️ CORRECTED (MRB-228). This assertion was written on the ROW and asked
    # it for `border-top-width: 2px`. It resolved 0px and the gate failed —
    # correctly, and on the assertion rather than on the stylesheet. The 2px
    # ink grid is set on `.ks3-smatrix-table th, td`, which is where a table
    # grid belongs; a `<tr>` carries no border of its own. Measuring the row
    # was asking the wrong element for someone else's property.
    #
    # Kept as its own row rather than folded into the one above, because the
    # grid and the row ground are two different claims and a merged row would
    # not say which of them broke.
    dict(name="the matrix grid is a 2px ink rule on the cells", on=C1_STATES,
         sel='.ks3-smatrix-row[data-lit="0"] > td',
         props={"border-top-color": "#221E1B", "border-top-width": "2px"}),
    # The footnote. Scoped `.ks3-smatrix .ks3-smatrix-foot` at (0,2,0) for the
    # standing `.ks3-dark p` reason (0,1,1) — c1-02 has no dark block today and
    # this is what keeps the rule winning if the table is ever reused on a page
    # that does.
    dict(name="matrix footnote is ink-muted at 18px", on=C1_STATES,
         sel=".ks3-smatrix-foot",
         props={"color": "#5F564F", "font-size": "18px"}),
