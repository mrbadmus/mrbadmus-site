# Design-reference addenda — fonts and tokens

Ruled and documented this run. The packed `KS3 Reference Set (offline).html` in this
folder is a bundled artefact and cannot be edited in place; this file carries the law
until that set is regenerated from its source.

## Font law (R7)

1. **The ohm sign is U+03A9 GREEK CAPITAL LETTER OMEGA (Ω), never U+2126 OHM SIGN.**
   The shipped latin subsets of Bricolage Grotesque, Instrument Sans and DM Mono carry
   the Greek omega and do not carry U+2126, so U+2126 falls back to a system font and
   silently changes typeface mid-word. Measured before P8 was authored; confirmed.

2. **Subscript digits (U+2081 and up) are absent** from Bricolage Grotesque and
   Instrument Sans. Where a diagram needs to distinguish two like quantities, label the
   parts `a` and `b` in body type rather than reaching for subscripts. This is the
   accepted workaround and is in use in `p8-03` and `p8-04`.

3. Already accepted and unchanged: **no `→`, `✓` or `✕` characters anywhere.** The
   same subsets lack all three. Draw arrows, ticks and crosses as inline SVG. A build
   check for those three characters must pass on every authored page.

4. Present and safe to use: `µ` (U+00B5), `−` (U+2212), `×` (U+00D7), `÷` (U+00F7),
   `°` (U+00B0), `·` (U+00B7).

## Token law (R8)

**`--ks3-data` is the token for live instrument values.** Granted this run. It applies
from P10 onward.

Two cautions for whoever regenerates the reference set:

- The token is **not present in the design-system copy bound to this project**
  (`_ds/.../tokens/shared-tokens.css` and `shared-ks3.css` define no `--ks3-data`).
  Until the shipped token file carries it, any use must be written with a fallback:
  `var(--ks3-data, var(--ks3-blue-light))` on ink-dark surfaces and
  `var(--ks3-data, var(--ks3-accent-text))` on cream.
- P8 and P9 use the substitution recorded in `NOTES-P8-P9.md` §9 and are **not** being
  reworked.

Unchanged: identity is never carried by hue alone. Every state that a colour marks also
carries a word in the readout.
