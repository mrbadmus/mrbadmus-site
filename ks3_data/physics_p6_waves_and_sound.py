"""P6 — Waves and sound. The unit where a disturbance travels and nothing
else does.

The lesson records live in `ks3_data/p6/`, one module each; this file is
the unit's identity and the seam `ks3_data._authored_modules()` discovers.

── THE UNIT IS ONE ARGUMENT ───────────────────────────────────────────

**A wave carries energy from one place to another and leaves the material
where it found it. Everything else in the unit — pitch, loudness, echoes,
what a bat can hear, what a scanner can see — is a consequence of that one
sentence plus the question of how often and how far.**

L1 and L2 build the idea on water, where you can watch it: the buoy that
bobs and stays, and two ripples that pass through each other unchanged.
L3 and L4 move it into air, where you cannot see it, and pay for that by
being precise about what a compression is. L5 separates the two
measurements a vibration has. L6 shows what happens when the material is
taken away. L7 sends it back off a wall. L8 says which of it any
particular ear can respond to. L9 puts the whole chain to work inside a
girder and inside a body.

A student who finishes the unit should stop saying that the water, or the
air, travels along.

⚠️ **THERE ARE EXACTLY TWO TRIANGLES, AND MRB-204 ALLOWS BOTH.**
`p6-05`'s `N = f × t` and `p6-06`'s `d = v × t` are genuine products.
`p6-07` is a SUM — the path out plus the path back — and takes a
part-whole bar, which is how Design drew it before anyone asked. `p6-09`
computes and carries no block at all; see her FLAG 3 in `ks3_data/p6/`.

⚠️ **`p6-01` NAMES NO FREQUENCY, ON PURPOSE.** A wave has one, and
`SND.01` belongs to `p6-05`. The ripple tank reports amplitude and
wavelength in millimetres and describes its paddle in words. `p6-03` does
report vibrations per second, because a bench that names a quantity and
will not let a student read it teaches nothing; it claims no clause of
`SND.01` and teaches no pitch.

⚠️ **THE WORD "WAVELENGTH" IS USED, THE WAVE EQUATION IS NOT.**
`v = f λ` is KS4. Every page that needs the connection makes it in words —
a higher frequency means a shorter wavelength in the same material — and
says so in the `ks4_becomes` line rather than putting a third relationship
in front of a Year 8 class.

⚠️ **`p6-08` AND `p6-09` CARRY SAFEGUARDING NOTES.** Hearing damage is the
student's own body and the loss is permanent; a scan is a thing to be
anxious about. Both use the engine's `safeguarding_note` slot, in small
type above the legal line, which is the treatment §8.10 rules for it.
"""

from .p6 import lessons as _p6_lessons

UNIT = {
    "code":            "P6",
    "slug":            "waves-and-sound",
    "title":           "Waves and sound",
    "discipline":      "physics",
    # ⚠️ DECORATIVE HERE, AND DELIBERATELY MATCHING `structure.py`.
    "statutory_area":  "Waves",
    "split_rationale": "Six statutory statements over nine slots — the "
                       "surplus case, and the widest of the three physics "
                       "units in this run at 0.67. Three statements are "
                       "split at the clause: OBW.01 because reflection and "
                       "superposition are two different ideas in one "
                       "sentence, SND.01 because frequency and echoes are "
                       "four lessons apart in any scheme of work, and "
                       "SND.03 because production, detection and "
                       "longitudinality are three separate lessons' worth. "
                       "SND.02, SND.04 and EAW.01 are whole.",
    "intro":           "A wave carries energy across a room, an ocean or a "
                       "steel girder and leaves everything where it found "
                       "it. Follow that one idea from a bobbing buoy to a "
                       "crack nobody can see.",
    "lessons": _p6_lessons(),
}
