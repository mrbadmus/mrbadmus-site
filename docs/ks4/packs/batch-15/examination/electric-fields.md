# Examination — Electric Fields (electric-fields) — AQA 8463 4.2.5.2 (physics only)
Verdict: SOURCE OK WITH FLAGS (no WRONG science; E = F/q, multi-charge and parallel-plate fields and q2 are off-spec; the spec's distance statements are not stated)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.6-electric-fields.md`.
Spec sources read: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.2.5.1, §4.2.5.2, Appendix equation list; `8463-equation-sheet-Jun26.txt`; `AQA-8464-spec.txt` (no electric fields section). Route audit `physics.md` row `electric-fields`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both items). The data's `spec` field "6.2.6 (physics only)" is the site's internal number; the true ref is **8463 4.2.5.2**.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.2.5.2** | Electric fields | **(physics only)** — from the 4.2.5 heading; no HT statement |
| 8464 | — | — | not in Combined Trilogy |
| Neighbour | 8463 4.2.5.1 | Static charge | (physics only); lesson `static-charge` |

Spec statements (verbatim): "A charged object creates an electric field around itself. The electric field is strongest close to the charged object. The further away from the charged object, the weaker the field. A second charged object placed in the field experiences a force. The force gets stronger as the distance between the objects decreases." Students should be able to: "draw the electric field pattern for an isolated charged sphere"; "explain the concept of an electric field"; "explain how the concept of an electric field helps to explain the non-contact force between charged objects as well as other electrostatic phenomena such as sparking."

E = F/q is not in 4.2.5.2, not in the 8463 recall list and not on the June 2026 8463 sheet.

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Field = region where another charge feels a force (theory 1; key_note) | triple | 4.2.5.2 | OK |
| R2 | Field lines + → −, direction of force on a + charge; closer = stronger; never cross (theory 1; common_mistake; q1) | triple | 4.2.5.2 (drawing the sphere's pattern) | OK |
| R3 | Isolated + and − charge: radial out / in (theory 1; matching) | triple | 4.2.5.2 | OK — the spec's one required pattern |
| R4 | Two opposite / two like charges; neutral point; parallel-plate uniform field (theory 1, 2; common_mistake; key_note; `higher`) | beyond spec | — | OFF-SPEC (ELECTRIC-FIELDS-F2) |
| R5 | Field is a vector (theory 1) | beyond spec | — | OFF-SPEC |
| R6 | + charge pushed along field, − against (theory 2) | triple | 4.2.5.2 | OK |
| R7 | "P.d. drives the movement of charge through an electric field" (theory 2; `higher` "link to p.d.") | beyond spec | — | OFF-SPEC / IMPRECISE (ELECTRIC-FIELDS-F2) |
| R8 | Non-contact force; like magnetic and gravitational fields (theory 2) | triple | 4.2.5.2 | OK |
| R9 | E = F/q; units N/C (theory 2; equations; variables; key_note; `higher`) | beyond spec | — | OFF-SPEC (ELECTRIC-FIELDS-F1) |
| R10 | Field strongest near the charge, weaker further away; force grows as distance falls | triple | 4.2.5.2 | **not stated** — only implied by "closer lines = stronger" (ELECTRIC-FIELDS-F3) |
| R11 | Sparks: strong field ionises air → discharge (theory 3; key_note) | triple | 4.2.5.2 ("sparking") | OK |
| R12 | Lightning; lightning conductors (theory 3; q2) | beyond spec (context) | — | OFF-SPEC; one imprecision (C15) |
| R13 | Fuel tankers earthed before refuelling (theory 3) | triple (sparking context) | 4.2.5.1 | OK |
| R14 | `higher` field (served TH only) | **not HT**: sphere diagram = triple; rest off-spec | 4.2.5.2 has no HT | ROUTE (ELECTRIC-FIELDS-F4) |
| R15 | q1 (field-line direction) | triple | 4.2.5.2 | OK; usable TF TH |
| R16 | q2 (lightning conductor) | beyond spec | — | OFF-SPEC; not a rung (ELECTRIC-FIELDS-F5) |
| — | RP, fifas | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | field = region around a charged object where another charged object feels a force | OK | — | 4.2.5.2 |
| C2 | theory 1 | arrows + → −, the way a + charge would move | OK | "the direction of the force on a positive charge" is the safer phrasing. | 4.2.5.2 |
| C3 | theory 1 | closer lines = stronger; lines never cross | OK | — | — |
| C4 | theory 1 | single + radiates out; single − points in | OK | Matches `radial_field()` in figlib. | 4.2.5.2 |
| C5 | theory 1 | opposite pair arcs + to −; like pair curves apart with a neutral point; parallel plates uniform | OK (OFF-SPEC) | Correct, not required. | — |
| C6 | theory 1 | field is a vector | OK (OFF-SPEC) | — | — |
| C7 | theory 2 | + charge: force along the field; − charge: opposite | OK | — | 4.2.5.2 |
| C8 | theory 2 | "The POTENTIAL DIFFERENCE (voltage) drives the movement of charge through an electric field" | IMPRECISE / OFF-SPEC | Not wrong in A-level terms, but at GCSE p.d. belongs to circuits and this sentence links nothing. Leave it out. | — |
| C9 | theory 2 | non-contact force; same principle as magnetic and gravitational fields | OK | — | 4.2.5.2; 4.5.1.2 |
| C10 | theory 2; equations; variables | E = F/q, N/C | OK physics, OFF-SPEC | Not in 8463 at all; no equation on the 8463 sheet. ELECTRIC-FIELDS-F1. | 8463 Appendix; sheet |
| C11 | theory 2 | parallel plates: uniform field, constant force; capacitors, CRTs, particle accelerators | OK (OFF-SPEC) | — | — |
| C12 | theory 3 | strong field near a sharp point; air ionised; ionised air conducts → spark | OK | The spec's "sparking". | 4.2.5.2 |
| C13 | theory 3 | lightning: cloud charge → very strong field → air breaks down | OK | — | — |
| C14 | theory 3 | lightning conductor: pointed rod, low-resistance path to earth | OK (context) | — | — |
| C15 | theory 3 | conductor "reduces risk of building being struck" | IMPRECISE | It makes a strike more likely to hit the rod, and so protects the building from damage. Say "protects the building from damage". | — |
| C16 | theory 3 | charged object near an earthed conductor → strong field → spark; tankers earth before refuelling | OK | — | 4.2.5.1; 4.2.5.2 |
| C17 | `higher` | field diagrams for single, pairs, plates; uniform field; E = F/q; variation with distance; link to p.d. | ROUTE | No HT in 4.2.5.2. "Variation with distance" is the spec core and belongs to TF too. ELECTRIC-FIELDS-F4. | 4.2.5.2 |
| C18 | common_mistake | lines + → −; don't confuse with magnetic N → S; uniform field equal spacing | OK | Last clause off-spec. | — |
| C19 | key_note | as above + E = F/q | OK | Contains off-spec E = F/q. | — |
| C20 | q1 key | + → −, the direction of force on a + test charge | OK | — | 4.2.5.2 |
| C21 | q1 wx1 | + → −, conventional direction, not − → + | OK | Aligned with opt 1. | — |
| C22 | q1 wx2 | fixed by convention and geometry, not random | OK | Aligned with opt 2. | — |
| C23 | q1 wx3 | can point any direction | OK | Aligned with opt 3. | — |
| C24 | q2 key | pointed conductor makes a strong local field and channels discharge to earth via a low-resistance path | OK (OFF-SPEC) | The common textbook account; lightning conductors are not on the spec. | — |
| C25 | q2 wx1–wx3 | don't block or absorb; provide a path; "deliberately attract lightning"; not into the structure | OK | Aligned. | — |
| C26 | matching (to be replaced) | single +, single −, opposite pair, plates | OK | Two of four pairs are off-spec patterns. | — |

Count: **0 WRONG**; IMPRECISE: C8, C15; OFF-SPEC: E = F/q, multi-charge and plate fields, q2.

Chained calculations (rule 3): none on spec. E = F/q is off-spec, so the lesson has no calculation.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | Off-spec (lightning conductors not in 8463 4.2.5). | Not a rung. Optional real-world extra or drop. |
| equations `E = F ÷ q` | Off-spec. | No equation block, no triangle, no CFIFA. |
| `higher` | Not HT. | No Higher layer; TF and TH get the same page. |

## 5. Verdict
SOURCE OK WITH FLAGS. All physics is correct, but much of it is A-level (E = F/q, plates, field pairs). The spec's own core — strongest near the charge, weaker further away, force grows as distance falls — is only implied; it has been added to the source as a "Spec core missing" section. Only q1 is usable as a rung.

**For Mide:** nothing.
