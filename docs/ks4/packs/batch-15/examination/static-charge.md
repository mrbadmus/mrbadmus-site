# Examination — Static Charge (static-charge) — AQA 8463 4.2.5.1 (physics only)
Verdict: SOURCE OK WITH FLAGS (no WRONG science; q2 and most of theory 3 are off-spec; the `higher` field is not HT)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.5-static-charge.md`.
Spec sources read: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.2.5.1, §4.2.5.2; `AQA-8464-spec.txt` (no static electricity section). No equation applies. Route audit `physics.md` row `static-charge`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both items). The data's `spec` field "6.2.5 (physics only)" is the site's internal number; the true ref is **8463 4.2.5.1**.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.2.5.1** | Static charge | **(physics only)** — from the 4.2.5 heading; no HT statement |
| 8464 | — | — | not in Combined Trilogy |
| Neighbour | 8463 4.2.5.2 | Electric fields (sparking explained) | (physics only); lesson `electric-fields` |

Spec statements (verbatim): "When certain insulating materials are rubbed against each other they become electrically charged. Negatively charged electrons are rubbed off one material and on to the other. The material that gains electrons becomes negatively charged. The material that loses electrons is left with an equal positive charge. When two electrically charged objects are brought close together they exert a force on each other. Two objects that carry the same type of charge repel. Two objects that carry different types of charge attract. Attraction and repulsion between two charged objects are examples of non-contact force." Students should be able to: "describe the production of static electricity, and sparking, by rubbing surfaces"; "describe evidence that charged objects exert forces of attraction or repulsion on one another when not in contact"; "explain how the transfer of electrons between objects can explain the phenomena of static electricity."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Rubbing insulators transfers electrons; gainer −, loser + (theory 1; common_mistake; key_note; q1) | triple | 4.2.5.1 | OK |
| R2 | Equal and opposite charges; charge conserved (theory 1) | triple | 4.2.5.1 ("equal positive charge") | OK |
| R3 | Only electrons move; protons fixed (theory 1; common_mistake) | triple | 4.2.5.1 | OK |
| R4 | Insulators hold charge; conductors cannot (theory 1) | triple | 4.2.5.1 ("certain insulating materials") | IMPRECISE (C6) |
| R5 | Like repel, unlike attract; non-contact force (theory 2; key_note) | triple | 4.2.5.1 | OK |
| R6 | Evidence: rods repel, hair stands up, balloon on wall (theory 2) | triple | 4.2.5.1 ("describe evidence") | OK; balloon-on-wall mechanism beyond spec |
| R7 | Induction / charge separation in a conductor (theory 2; key_note; `higher`) | beyond spec | — | OFF-SPEC (STATIC-CHARGE-F2) |
| R8 | Sparking: fuel-tanker flow, lightning (theory 2) | triple | 4.2.5.1 ("sparking"); 4.2.5.2 | OK |
| R9 | ESD hazard, antistatic wristbands (theory 2) | beyond spec (context) | — | OK science; OFF-SPEC |
| R10 | Applications: inkjet, laser printer, precipitator, spray painting, defibrillator (theory 3; key_note; `higher`; q2) | beyond spec | — | OFF-SPEC (STATIC-CHARGE-F1, STATIC-CHARGE-F2) |
| R11 | `higher` field (served TH only) | **not HT**: sparking = triple; induction/applications = off-spec | 4.2.5.1 has no HT | ROUTE (STATIC-CHARGE-F3) |
| R12 | q1 (rod rubbed with wool) | triple | 4.2.5.1 | OK; usable TF TH |
| R13 | q2 (precipitators) | beyond spec | — | OFF-SPEC; not a rung (STATIC-CHARGE-F1) |
| — | RP, equations, fifas | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | static builds up on an insulating material | OK | — | 4.2.5.1 |
| C2 | theory 1 | rubbing two insulators transfers electrons; gainer negative, loser positive | OK | Spec wording. | 4.2.5.1 |
| C3 | theory 1 | charge conserved; charges equal and opposite | OK | — | 4.2.5.1 |
| C4 | theory 1 | plastic rod + cloth → rod −, cloth + | OK | True for polythene with wool/cloth (acetate goes +; leave "plastic" generic or say polythene). | — |
| C5 | theory 1 | only electrons move; + made by removing electrons | OK | — | 4.2.5.1 |
| C6 | theory 1 | "Conductors: charge spreads across the surface immediately — cannot build up static" | IMPRECISE | An insulated conductor can hold charge (a Van de Graaff dome does). A conductor held in the hand or touching the ground cannot, because the charge flows away through you to earth. STATIC-CHARGE-F4. | 4.2.5.1 |
| C7 | theory 2 | like repel, opposite attract; non-contact force | OK | Spec wording. | 4.2.5.1 |
| C8 | theory 2 | balloon "induces an opposite charge on the wall surface" | OK (beyond spec) | A wall is an insulator, so this is polarisation, not free electrons moving; the spec does not ask for the mechanism. | — |
| C9 | theory 2 | same-material rods repel; hair stands up (all same charge) | OK | Good "evidence" examples. | 4.2.5.1 |
| C10 | theory 2 | induction: free electrons move in a neutral conductor; near end opposite charge → attraction | OK (OFF-SPEC) | Correct physics, not on the spec. | — |
| C11 | theory 2 | fuel flowing through pipes builds static → spark → fire risk | OK | A sparking example; on spec. | 4.2.5.1 |
| C12 | theory 2 | ESD damages electronics; antistatic wristbands | OK (context) | — | — |
| C13 | theory 2 | lightning = massive electrostatic discharge cloud–earth | OK | — | 4.2.5.2 |
| C14 | theory 3 | inkjet, laser printer/photocopier, precipitator, spray painting descriptions | OK (OFF-SPEC) | Accurate outlines. AQA's 2016 spec dropped these applications. | — |
| C15 | theory 3 | defibrillators: capacitors store and discharge charge | OK (OFF-SPEC) | Correct but it is capacitor discharge, not rubbing-produced static. | — |
| C16 | `higher` | induction, applications, hazards, sparks as air ionisation | ROUTE | 4.2.5.1 has no HT. Sparking (air ionised in a strong field) is triple base and belongs to TF as well — and is taught in `electric-fields`. STATIC-CHARGE-F3. | 4.2.5.1; 4.2.5.2 |
| C17 | common_mistake | only electrons move; gainer −, loser +; like repel; charges ≠ magnetic poles | OK | — | 4.2.5.1 |
| C18 | key_note | as above | OK | Includes off-spec applications and induction. | — |
| C19 | q1 key | electrons cloth → rod; rod −, cloth + | OK | — | 4.2.5.1 |
| C20 | q1 wx1 | protons fixed in nucleus | OK | Aligned with opt 1. | 4.2.5.1 |
| C21 | q1 wx2 | charge conserved; not created | OK | Aligned with opt 2. | — |
| C22 | q1 wx3 | only electrons move | OK | Aligned with opt 3. | 4.2.5.1 |
| C23 | q2 key | precipitators charge soot, collected on oppositely charged plates | OK (OFF-SPEC) | Correct; off-spec. | — |
| C24 | q2 wx1–wx3 | not heat; electric not magnetic; scrubbers dissolve gases | OK | All aligned and correct. | — |
| C25 | matching (to be replaced) | rod −, cloth +, balloon/wall, hair | OK | — | — |

Count: **0 WRONG**; IMPRECISE: C6; OFF-SPEC: induction, applications, q2.

Chained calculations (rule 3): none — the lesson has no calculation.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | Off-spec (precipitators are not in 8463 4.2.5). | Not a rung. Design may keep it as an optional "real world" extra, or drop it. |
| `higher` | Not HT; mostly off-spec. | No Higher layer. TF and TH get the same page. |

## 5. Verdict
SOURCE OK WITH FLAGS. The spec core (electron transfer, equal and opposite charges, like/unlike forces, non-contact force, sparking) is present and correct. Theory 3's applications, induction and q2 are off-spec. One imprecision about conductors. Only q1 is usable as a rung.

**For Mide:** nothing.
