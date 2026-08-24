"""P1 — Energy transfers. Eight lessons, Year 7 Physics.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/p1/`.

    L1 energy-stores                      KS3.P.CIS.02a
    L2 energy-transfers-before-and-after  KS3.P.CIS.02b + KS3.P.ECT.03
    L3 conservation-of-energy             KS3.P.CIS.01  + KS3.P.CIS.03
    L4 heating-and-thermal-equilibrium    KS3.P.ECT.02a
    L5 conduction                         KS3.P.ECT.02b
    L6 radiation                          KS3.P.ECT.02c
    L7 insulation                         KS3.P.ECT.02d
    L8 simple-machines                    KS3.P.ECT.01

`KS3.P.CIS.02` and `KS3.P.ECT.02` are clause-split under §11.11; both mints,
the bullets in full and the reasoning that chose the seams are in
`ks3_data/substatements.py`. Which lesson takes which clause is ruled in
`ks3_data/p1/__init__.py`.

── THE UNIT IS ONE ARGUMENT ─────────────────────────────────────────────

Energy is an accounting system, and the unit teaches it as one. L1 gives the
student the accounts — five stores, and what fills and empties each. L2 makes
them read a situation as a transfer between two of those accounts. L3 closes
the books: the total never changes, which is exactly why energy can never be
the REASON anything happened, so an explanation has to name a mechanism
instead.

L4-L7 then run one mechanism all the way down. A temperature difference is the
only thing that drives a thermal transfer (L4); it can travel by contact (L5)
or with no contact at all (L6); and slowing it down is a design problem you
test rather than argue about (L7). L8 comes back to the accounts with a
number: a machine can give you more force, and the ledger says exactly what it
charges you for it.

⚠️ **THE UNIT ASSUMES NOTHING.** It is the first unit of Year 7 physics on the
default sequence and it is written for a student who has met none of it. Where
it needs a particle, it draws one (L5) rather than pointing at C1 — a
`references` edge to `ks3_data/c1/` would be a link a Year 7 in week two
cannot yet follow. The edge is declared on L5 as a `references` entry, which
renders as a cross-link and never as prose (§4.6).
"""

from .p1 import lessons as _p1_lessons

UNIT = {
    "code":            "P1",
    "slug":            "energy-transfers",
    "title":           "Energy transfers",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Energy",
    "intro":           "Energy is not a substance and not a fuel. It is a set "
                       "of accounts, and every change moves some between two "
                       "of them without ever changing the total.",
    "lessons": _p1_lessons(),
}
