# Examination — Contact and Non-Contact Forces (contact-noncontact-forces) — AQA 8464 6.5.1.2 / 8463 4.5.1.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.5.1.2-contact-noncontact-forces.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.5.1.2, §6.5.4.2.1, §6.5.4.2.3; `AQA-8463-spec.txt` (v1.1) §4.5.1.2, §4.2.5.1, §4.5.5.1.2, §4.5.6.2.3. Route audit row `contact-noncontact-forces`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8463 | **6.5.1.2 / 4.5.1.2** | Contact and non-contact forces | base |
| Supporting | 6.5.4.2.3 / 4.5.6.2.3 Newton's Third Law | | base |
| Supporting | 6.5.4.2.1 / 4.5.6.2.1 Newton's First Law | | base |
| Supporting | 8463 4.2.5.1 Static charge | | physics only |
| Supporting | 8463 4.5.5.1.2 Pressure in a fluid 2 — upthrust | | (HT only) (physics only) |

Spec statements (6.5.1.2 = 4.5.1.2, verbatim): "A force is a push or pull that acts on an object due to the interaction with another object. All forces between objects are either: • contact forces – the objects are physically touching • non-contact forces – the objects are physically separated. Examples of contact forces include friction, air resistance, tension and normal contact force. Examples of non-contact forces are gravitational force, electrostatic force and magnetic force. Force is a vector quantity. Students should be able to describe the interaction between pairs of objects which produce a force on each object. The forces to be represented as vectors."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Force = push/pull from an interaction; vector; newtons (theory 1; key_note) | base | 6.5.1.2 | all four | OK |
| R2 | Forces change speed, direction, shape (theory 1; key_note) | base | 6.5.1.2 context; 6.5.3 | all four | OK |
| R3 | Interaction pairs, equal and opposite (theory 1) | base | 6.5.1.2; 6.5.4.2.3 | all four | OK |
| R4 | Contact: friction, air resistance, tension, normal contact (theory 2; key_note) | base | 6.5.1.2 | all four | OK |
| R5 | Contact: compression (theory 2) | base (context) | — | all four | IMPRECISE (C6) |
| R6 | Contact: upthrust (theory 2; key_note; q2 opt 4) | term defined in 8463 4.5.5.1.2 (HT, physics only) | 8463 4.5.5.1.2 | all four | OK as an example; ROUTE minor (F3) |
| R7 | Non-contact: gravitational, electrostatic, magnetic (theory 3; key_note) | base | 6.5.1.2 | all four | OK |
| R8 | Balloon-on-wall static example (theory 3) | triple (static charge, 8463 4.2.5.1) | 8463 4.2.5.1 | all four | IMPRECISE + ROUTE (F1) |
| R9 | Gravity always attracts; others attract or repel (theory 3; key_note) | base | 6.5.1.2 | all four | IMPRECISE wording (F2) |
| R10 | Weight is gravitational; normal force ≠ weight (common_mistake) | base | 6.5.1.2–6.5.1.3 | all four | IMPRECISE (F2) |
| R11 | q1 (book on table) | base | 6.5.1.2; 6.5.4.2.1 | all four | OK |
| R12 | q2 (which is non-contact) | base | 6.5.1.2 | all four | OK |
| — | rp, fifas, equations, `higher`, examiner_tip | none | — | — | correct: no HT, no calculation |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | force = push or pull due to interaction with another object | OK | Spec wording. | 6.5.1.2 |
| C2 | theory 1 | vector, newtons | OK | — | 6.5.1.2 |
| C3 | theory 1 | forces change speed, direction, shape | OK | — | — |
| C4 | theory 1 | A on B, B on A equal and opposite (N3) | OK | — | 6.5.4.2.3 |
| C5 | theory 2 | friction; air resistance as friction with air; tension; normal contact force (perpendicular) | OK | — | 6.5.1.2 |
| C6 | theory 2 | "COMPRESSION — a pushing force through a solid. A compressed spring." | IMPRECISE | Not one of AQA's named forces; compression is a state of the spring, the force is the spring's push (a contact force). Cut, or say "the push of a compressed spring". | 6.5.3 |
| C7 | theory 2 | upthrust = upward force from a fluid; contact | OK | Correct classification. The term upthrust is defined only in 8463 4.5.5.1.2 (HT, physics only); explain it in a phrase if kept. | 8463 4.5.5.1.2 |
| C8 | theory 3 | "Three fundamental non-contact forces at GCSE" | IMPRECISE | Not "fundamental" (electrostatic and magnetic are both electromagnetic). Say "AQA names three non-contact forces". | 6.5.1.2 |
| C9 | theory 3 | gravity attracts any two masses; Earth pulls to its centre; Sun holds planets | OK | — | 6.5.1.3; 4.8.1 |
| C10 | theory 3 | "charged balloon sticks to a wall (different charges attract)" | IMPRECISE | The wall is uncharged; the charged balloon induces an opposite charge on the wall's surface, which then attracts. As written it implies the wall carries an opposite charge. Static charge is physics only (8463 4.2.5.1). Use "two charged objects attract or repel without touching" for base. | 8463 4.2.5.1 |
| C11 | theory 3 | magnets: opposite poles attract, like repel; act at a distance | OK | — | 6.7.1.1 |
| C12 | theory 3 | "All three non-contact forces can attract or repel (except gravity — gravity is always attractive)." | IMPRECISE | Self-contradicting. Say: "Electrostatic and magnetic forces can attract or repel. Gravity only ever attracts." | — |
| C13 | common_mistake | gravity non-contact; weight = gravitational force; normal force ≠ weight, it is "a REACTION from the surface" | IMPRECISE | Correct, but "reaction" (with theory 1's N3 sentence) invites the classic error that weight and normal force are a Newton's-third-law pair. They are not: they act on the same object. The N3 partner of the book's weight is the book's pull on the Earth. Add that sentence. | 6.5.4.2.3 |
| C14 | key_note | lists | OK | Compression and upthrust as per C6, C7. | — |
| C15 | q1 key | weight (non-contact, down) + normal contact (contact, up), balanced | OK | — | 6.5.1.2; 6.5.4.2.1 |
| C16 | q1 opt 2 / wx1 | friction upward → wx: friction acts parallel to surfaces | OK, aligned | — | — |
| C17 | q1 opt 3 / wx2 | tension → wx: tension acts through strings/ropes | OK, aligned | — | — |
| C18 | q1 opt 4 / wx3 | only weight → wx: N1, balanced forces | OK, aligned | — | 6.5.4.2.1 |
| C19 | q2 key | Sun's gravitational pull on Earth | OK | — | 6.5.1.2 |
| C20 | q2 opt 2 / wx1 | air resistance → contact | OK, aligned | — | — |
| C21 | q2 opt 3 / wx2 | tension → contact | OK, aligned | — | — |
| C22 | q2 opt 4 / wx3 | upthrust → contact | OK, aligned | Upthrust term HT physics-only (C7); the option explains itself. | — |
| C23 | matching (to be replaced) | friction, tension, normal contact = contact; gravity, magnetic = non-contact | OK | — | — |

Count: **0 WRONG**; IMPRECISE: C6, C8, C10, C12, C13. No calculations. No CFIFA Convert line in this file.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1, q2 | correct, base | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: gravity "needs air" or "doesn't act in space"; friction holds a resting book up; weight and normal contact force named as a Newton's-third-law pair; magnetic force thought to need touching; air resistance or upthrust called non-contact; "force" used for energy or speed.

**Command words**: Name / Give (a contact force, a non-contact force), Describe (the interaction pair), Draw (forces as arrows).

**Typical questions** ⚑ examiner-drafted
- *Which of these is a non-contact force? friction / magnetic force / tension / air resistance [1]* — magnetic force.
- *A book rests on a table. Name the two forces acting on the book and state whether each is a contact or non-contact force. [2]* — weight/gravitational force, non-contact (1); normal contact force, contact (1).

**Required practical**: none. **Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. The spec core is fully present and both quiz items are correct and usable everywhere. Five wording fixes in the re-cuttable theory (balloon example, the "all three … except gravity" sentence, "fundamental", compression, and the normal-force/N3 trap).

**For Mide:** nothing.
