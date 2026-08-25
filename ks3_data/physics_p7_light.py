"""P7 — Light. The unit where a wave crosses nothing at all.

The lesson records live in `ks3_data/p7/`, one module each; this file is
the unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**Light is a transverse wave that needs no material, travels in straight
lines at 300 000 000 m/s, and every other thing in this unit is what
happens when one of those straight lines meets a surface.** Reflection is
a straight line turned; refraction is a straight line bent because the
speed changed; an image is a bundle of straight lines put back together;
colour is which of them a surface lets go again.

L1 builds the wave and the speed against sound, which the student has
just met. L2 and L3 are the two things a boundary can do to a ray — send
it back, or let it in slowly. L4 turns rays into a picture. L5 puts the
picture inside two instruments and follows the energy to an absorber. L6
splits the light by frequency. L7 uses the split to say why anything is
any colour at all.

A student who finishes the unit should stop saying that an object HAS a
colour, and should stop saying that light is instant.

⚠️ **THERE IS ONE TRIANGLE AND ONE BEAM, AND MRB-204 ALLOWS BOTH.**
`p7-01`'s `d = c × t` is a genuine product. `p7-02`'s `r = i` is an
EQUALITY — two equal pans, no cover buttons, the `p1-08` precedent — and
Design drew it that way before anyone asked. `p7-03` … `p7-07` carry no
formula block at all; see her FLAG 4 on `p7-04` in `ks3_data/p7/`.

⚠️ **`p7-02` CARRIES ONE WORKED EXAMPLE AND ONE ATTEMPT QUESTION.**
Its quantities are angles in degrees, so a conversion cannot arise: her
own README says so in terms, and the C step reads as the no-conversion
case. `ks3_art.kit.r_cfifa_attempt` refuses fewer than two questions, so
the payload declares `one_question_because` and the helper lifts that one
check and nothing else. Inventing a second question would have been
inventing content Design did not write.

⚠️ **THE WORD "FREQUENCY" IS USED, THE WAVE EQUATION IS NOT.** `v = f λ`
is GCSE, and so are refractive index, magnification and the critical
angle. `p7-03`, `p7-04` and `p7-06` are qualitative on purpose — the
statute says *qualitative only* for the prism in terms — and every page
puts the connection in words and in `ks4_becomes` instead.

⚠️ **`p7-05` CARRIES A SAFEGUARDING NOTE.** The eye is the student's own
body and retinal damage is painless and permanent. It uses the engine's
`safeguarding_note` slot, in small type above the legal line, which is
the treatment §8.10 rules for it — and it closes the third of the three
pages Design's audit finding 6.4 names (`p6-08` and `p6-09` are P6's).
"""

from .p7 import lessons as _p7_lessons

UNIT = {
    "code":            "P7",
    "slug":            "light",
    "title":           "Light",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Waves",
    "split_rationale": "Six statutory statements over seven slots — the "
                       "surplus case, at 0.86. Three statements are split at "
                       "the clause: LGT.03 because what a surface sends back "
                       "and what it keeps are two lessons apart, LGT.04 "
                       "because the ray model is used by four different "
                       "lessons and the mirror, the block, the pinhole and "
                       "the eye are not one idea, and LGT.06 because white "
                       "light being a mixture and a surface choosing from "
                       "that mixture are the two halves of colour. LGT.01, "
                       "LGT.02 and LGT.05 are whole.",
    "intro":           "Light crosses empty space at three hundred million "
                       "metres a second and travels in straight lines. "
                       "Follow one of those lines into a mirror, a block of "
                       "glass, a pinhole, an eye and a prism.",
    "lessons": _p7_lessons(),
}
