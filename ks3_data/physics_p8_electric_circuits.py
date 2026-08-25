"""P8 — Electric circuits. The unit where nothing is used up.

The lesson records live in `ks3_data/p8/`, one module each; this file is
the unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**A circuit hands ENERGY to a component and gets all its charge back.
Everything else in the unit — why a gap anywhere stops everything, why
two bulbs in series dim and two in parallel do not, why the readings at a
junction add, what a volt measures, what an ohm is, and why a cable is
copper inside and plastic outside — is a consequence of that one sentence
plus the question of how hard it is to get through.**

L1 establishes the loop and the thing that flows round it. L2 asks the
only structural question there is — one path or two — and shows what each
answer costs. L3 does the arithmetic of a junction. L4 turns from what is
flowing to what is pushing, and to the fact that the push is SHARED. L5
puts the two measurements together and divides one by the other. L6 takes
that division to both ends of the range and finds no boundary in it. L7
puts the meters in a student's hands and gets them wrong on purpose.

A student who finishes the unit should stop saying that the bulb uses up
the current.

⚠️ **TWO PART–WHOLE BARS AND TWO TRIANGLES, AND MRB-204 ALLOWS ALL FOUR.**
`p8-03`'s `I = a + b` and `p8-04`'s `V = a + b` are SUMS and take bars;
`p8-05`'s and `p8-06`'s `V = I × R` is a genuine product and takes the
triangle. Design's FLAG 5 asks a reviewer to confirm the two bars three
slots apart read as a designed pairing rather than a copied component —
current splits at a junction, p.d. splits round a loop, and they are the
pair of rules students most often swap. They are kept, and each block
states its own relationship from nothing.

⚠️ **`p8-06` CARRIES A SECOND `V = I × R` TRIANGLE, RULED BY MIDE.** Her
FLAG 3 asked whether a page that computes on every state must carry a
block and warned that the answer means a duplicate. The answer is yes and
the duplicate is a feature: `p8-06` divides 6.0 V by an ammeter reading in
five different unit prefixes, and doing that without the shape in front of
you is arithmetic rather than physics. ⊕ Her DELIVERED PAGE had already
drawn it; only her notes still say otherwise.

⚠️ **`p8-05`'s FILAMENT LAMP IS A STRAIGHT LINE AND THE PAGE NEVER CALLS
THE RISE EVEN.** Ruled by Mide, 21 Aug 2026. The model — about 6 Ω at
1.5 V rising to about 18 Ω at 12 V — stays, because the teaching point is
that resistance is not fixed and the true concave curve is GCSE. What the
page may not do is claim the climb is steady: it fixes the two ENDS and
makes no claim about the shape between them. `r_component_under_test`
sweeps the payload and refuses one that says otherwise.

⚠️ **`p8-06` DOES NOT PRINT 120 A FOR COPPER.** 6.0 V ÷ 0.05 Ω is a
division result, not a reading: no school supply delivers it, because the
supply's own internal resistance is what limits the current there. The
resistance readout keeps its real value; the current readout reads
*limited by the supply, not by the wire*. Copper still draws its bar on
the chart, because it is the reference every other specimen is measured
against.

⚠️ **`p8-07` OWNS NO SUBJECT-CONTENT CLAUSE, DELIBERATELY** (her FLAG 2).
It is the unit's Working Scientifically slot: where each meter goes and
why, fault-finding from a symptom, repeating a reading, planning a fair
test. Every quantity it uses is owned by `p8-01`, `p8-04` or `p8-05`. It
claims `KS3.WS.EXP.03`, which §5.7 exempts from the exactly-once rule.

⚠️ **SAFEGUARDING IS ON `p8-06` AND NOWHERE ELSE IN THE UNIT.** That page
ends on why a cable is copper inside and plastic outside, and mains cables
and sockets at home are where that stops being an abstraction. `p8-07` is
practical safety — cells and a lamp, no body at risk — and lab safety is
not safeguarding.
"""

from .p8 import lessons as _p8_lessons

UNIT = {
    "code":            "P8",
    "slug":            "electric-circuits",
    "title":           "Electric circuits",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Electricity and electromagnetism",
    "split_rationale": "Three statements over seven slots — the most "
                       "surplus-slot unit in physics at 0.43. Both compound "
                       "statements are split at the clause: CUR.01 because "
                       "what a current IS, the two arrangements and the "
                       "junction rule are three lessons in any scheme of "
                       "work, and CUR.02 because the semicolon in the source "
                       "separates what a volt measures from the ratio that "
                       "defines an ohm. CUR.03 is whole. `p8-07` owns a "
                       "Working Scientifically statement instead, which is "
                       "Design's FLAG 2 and is legal under §5.7.",
    "intro":           "Put an ammeter either side of a bulb and both read "
                       "the same. Follow that one fact from a torch to a "
                       "junction, a voltmeter, an ohm and a cable that is "
                       "copper inside and plastic outside.",
    "lessons": _p8_lessons(),
}
