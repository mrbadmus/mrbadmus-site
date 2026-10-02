# Examination — Electromagnetism (electromagnetism) — AQA 8464 6.7.2.1 / 8463 4.7.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.7.2.1-electromagnetism.md`.
Spec sources read: `AQA-8464-spec.txt` 6.7.2.1–6.7.2.3 and the RP list; `AQA-8463-spec.txt` 4.7.2.1–4.7.3.1; route audit `physics.md` row `electromagnetism` (base, base).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. Route copies: the `higher` field differs — TH copy (canonical; also served on CH) vs CF/TF copy (identical to each other). Both checked below.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.7.2.1** | Electromagnetism | base |
| 8463 | **4.7.2.1** | Electromagnetism | base, plus one "(Physics only)" bullet |
| Related (not this lesson) | 8464 6.7.2.2 / 6.7.2.3 (HT only); 8463 4.7.2.4 (physics only)(HT only); 8463 4.7.3.1 (physics only)(HT only) | motor effect; motors; loudspeakers; induced potential | where the `higher` field's content belongs |

Spec statements (verbatim, 8463 = 8464): "When a current flows through a conducting wire a magnetic field is produced around the wire. The strength of the magnetic field depends on the current through the wire and the distance from the wire. Shaping a wire to form a solenoid increases the strength of the magnetic field created by a current through the wire. The magnetic field inside a solenoid is strong and uniform. The magnetic field around a solenoid has a similar shape to that of a bar magnet. Adding an iron core increases the strength of the magnetic field of a solenoid. An electromagnet is a solenoid with an iron core." "Students should be able to: • describe how the magnetic effect of a current can be demonstrated • draw the magnetic field pattern for a straight wire carrying a current and for a solenoid (showing the direction of the field) • explain how a solenoid arrangement can increase the magnetic effect of the current." 8463 only: "(Physics only) Students should be able to interpret diagrams of electromagnetic devices in order to explain how they work."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Wire: concentric circles, depends on current and distance (theory 1; key_note) | base | 6.7.2.1 | OK |
| R2 | Demonstrating the magnetic effect (Oersted's compass deflection, theory 1) | base | 6.7.2.1 | OK |
| R3 | Grip rule for direction round a wire and solenoid poles (theory 1, 2) | base | 6.7.2.1 | OK — naming IMPRECISE (F7) |
| R4 | Solenoid: uniform inside, bar-magnet shape outside; current, turns, iron core (theory 2) | base | 6.7.2.1 | OK |
| R5 | Why the solenoid shape strengthens the field | base | 6.7.2.1 | GAP (F8) |
| R6 | Electromagnet = solenoid + iron core; soft iron switches off (theory 3; common_mistake) | base | 6.7.2.1; 6.7.1.1 | OK |
| R7 | Advantages over permanent magnets (theory 3) | base (context) | 6.7.2.1 | OK |
| R8 | Device explanations: bell, crane, relay/circuit breaker, maglev, MRI (theory 3) | triple | 8463 4.7.2.1 (physics only) | ROUTE (F5); relay IMPRECISE (F6) |
| R9 | Speakers (theory 3) | triple-higher | 8463 4.7.2.4 | ROUTE (F5) |
| R10 | `higher` TH copy (also on CH) | higher / triple-higher / not in spec | 6.7.2.2; 4.7.2.4; 4.7.3.1 | ROUTE + OFF-SPEC (F1) |
| R11 | `higher` CF/TF copy | higher / triple-higher, on Foundation routes | 6.7.2.2–6.7.2.3; 4.7.3.1 | ROUTE (F2) |
| R12 | `rp` "RP21" | not an AQA RP | — | OFF-SPEC (F4) |
| R13 | q1 (iron not steel core) | base | 6.7.2.1 | OK — usable all routes |
| R14 | q2 (double current → field "doubles, directly proportional") | base topic | 6.7.2.1 | OFF-SPEC key (F3) — do not use as written |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | current-carrying conductor produces a field; concentric circles in a plane perpendicular to the wire | OK | — | 6.7.2.1 |
| C2 | theory 1 | "RIGHT-HAND RULE — thumb along conventional current, fingers curl with field" | IMPRECISE | Correct rule; name it the "right-hand grip rule" so it is not confused with Fleming's rules. (F7) | 6.7.2.1 |
| C3 | theory 1 | stronger with more current; weaker further away | OK | Spec-exact. | 6.7.2.1 |
| C4 | theory 1 | Oersted 1820, compass deflection | OK | Serves "describe how the magnetic effect of a current can be demonstrated". | 6.7.2.1 |
| C5 | theory 2 | solenoid: uniform field inside; bar-magnet shape outside; N and S ends | OK | — | 6.7.2.1 |
| C6 | theory 2 | grip rule for solenoid → thumb = N; anticlockwise end = N, clockwise = S | OK | — | 6.7.2.1 |
| C7 | theory 2 | more current, more turns, iron core → stronger | OK | Spec states current and iron core; turns follows. | 6.7.2.1 |
| C8 | theory 2 | — | GAP | Missing the "explain" bullet: in a solenoid the fields of all the turns add together, concentrating the field inside the coil. (F8) | 6.7.2.1 |
| C9 | theory 3 | electromagnet = solenoid + iron core; iron soft, loses magnetism when current off; steel would keep it | OK | — | 6.7.2.1; 6.7.1.1 |
| C10 | theory 3 | switchable; strength adjustable; polarity reversible | OK | — | — |
| C11 | theory 3 | electric bell cycle | OK | Device explanation = physics-only bullet. (F5) | 8463 4.7.2.1 |
| C12 | theory 3 | scrapyard crane | OK | As C11. | 8463 4.7.2.1 |
| C13 | theory 3 | "CIRCUIT BREAKER (relay): electromagnet pulls a switch to break a circuit" | IMPRECISE | Two different devices. A relay lets a small current switch a separate (usually larger) circuit on or off; a circuit breaker trips open when the current is too large. (F6) | 8463 4.7.2.1 |
| C14 | theory 3 | maglev: track electromagnets repel train magnets | OK (simplified) | Some systems attract from below; enrichment. | — |
| C15 | theory 3 | MRI uses superconducting electromagnets | OK | Enrichment. | — |
| C16 | theory 3 | "SPEAKERS: varying current → changing force on cone" | OK science, ROUTE | That is the motor effect in a loudspeaker: 8463 4.7.2.4 (physics only)(HT only). (F5) | 8463 4.7.2.4 |
| C17 | common_mistake | iron (soft) not steel (hard); current or turns increase strength | OK | — | 6.7.2.1 |
| C18 | key_note | as theory | OK | — | 6.7.2.1 |
| C19 | rp | "RP21 (Physics) — Investigate the factors affecting the strength of an electromagnet…" | OFF-SPEC | Not an AQA required practical. 8464 RP21 = infrared (6.6.2.2); 8463 RPs 1–10, none on magnetism. Fine as an investigation, no RP badge. (F4) | 8464 6.6.2.2 |
| C20 | `higher` TH copy | "a current-carrying conductor in a magnetic field experiences a force F = BIl. Apply Fleming's Left-Hand Rule…" | OK science, ROUTE | 8464 6.7.2.2 (HT only) — the next lesson's content. (F1) | 6.7.2.2 |
| C21 | `higher` TH copy | "Explain how the motor effect is used in loudspeakers" | OK science, ROUTE | 8463 4.7.2.4 (physics only)(HT only) — served on CH too. (F1) | 8463 4.7.2.4 |
| C22 | `higher` TH copy | "a conductor moving in a magnetic field induces an EMF — Fleming's Right-Hand Rule gives induced current direction" | OFF-SPEC + ROUTE | Generator effect is 8463 4.7.3.1 (physics only)(HT only); AQA says "induced potential difference", not EMF; Fleming's right-hand rule is not in the AQA spec. (F1) | 8463 4.7.3.1 |
| C23 | `higher` CF/TF copy | "F = BIl (force = flux density × current × length). Fleming's Left-Hand Rule: thumb = force direction, index = field, middle finger = current." | OK science, ROUTE | Finger assignments correct. But this is HT content (8464 6.7.2.2) served to Foundation routes. (F2) | 6.7.2.2 |
| C24 | `higher` CF/TF copy | "Applications: electric motors (rotating coil in field)." | OK science, ROUTE | HT (6.7.2.3) on Foundation routes. (F2) | 6.7.2.3 |
| C25 | `higher` CF/TF copy | "Induced EMF (generator effect)." | ROUTE | Physics-only HT content shown to Combined Foundation, where it is on no Combined route. Note: `_extract-notes.md` note 7 says this copy "omits the generator effect entirely" — it does not; it ends with this sentence. (F2) | 8463 4.7.3.1 |
| C26 | q1 key | iron is soft — loses magnetism when switched off | OK | — | 6.7.2.1 |
| C27 | q1 opt 1 / wx1 | "Iron is harder than steel" / mechanical vs magnetic "hard" | OK | Aligned. | — |
| C28 | q1 opt 2 / wx2 | conductivity / current flows in the coil, not the core | OK | Aligned. | — |
| C29 | q1 opt 3 / wx3 | steel too strong / aim is switching off, not limiting strength | OK | Aligned. | — |
| C30 | q2 key | "The field doubles in strength — magnetic field strength is directly proportional to current" | OFF-SPEC | The spec says only that strength "depends on the current". For an electromagnet (iron core, the spec's own definition) the field is not proportional to current — the core's magnetisation is non-linear and saturates. Proportionality holds only for an air-cored solenoid. A pupil taught "doubles" is learning a claim AQA does not make. (F3) | 6.7.2.1 |
| C31 | q2 opt 1 / wx1 | halves "more resistance" / proportional to current and turns | OFF-SPEC (as C30) | Rebuttal aligned; repeats the proportionality claim. | — |
| C32 | q2 opt 2 / wx2 | stays same / both current and turns matter | OK | Aligned; "doubling current doubles the field" repeats C30. | — |
| C33 | q2 opt 3 / wx3 | quadruples / not current squared | OFF-SPEC (as C30) | Aligned. | — |
| C34 | matching (to be replaced) | five pairs | OK | — | — |

Count: **0 WRONG**; OFF-SPEC: C19, C22, C30 (q2); ROUTE: C16, C20–C25 and the device explanations; IMPRECISE: C2, C13; GAP: C8.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| `higher` (TH copy, served on CH and TH) | All of it is other lessons' content; part is triple-only, part not in spec (F1) | Do not use on this page on any route. 6.7.2.1 has no HT content. |
| `higher` (CF + TF copy) | HT and triple-HT content on Foundation routes (F2) | Do not use on any route. |
| q2 | OFF-SPEC key (F3) | Do not use as written. |
| q1 | Correct, base | Usable on all four routes. |
| `rp` | Not an AQA RP (F4) | No RP badge. |

## 5. For the lesson author
**Misconceptions seen in AQA marking:** field lines round a wire drawn as radial spokes or as a single loop; no arrows / wrong arrow direction; solenoid field drawn only outside; "steel core is better because it is stronger"; "the current flows through the iron core"; "more turns means more resistance so a weaker field".
**Command words:** Describe (how to demonstrate the magnetic effect), Draw (wire and solenoid patterns with direction), Explain (how a solenoid increases the effect; TF TH: how a device works from its diagram).
**Required practical:** none (F4).
**Equations:** none.

## 6. Verdict
SOURCE OK WITH FLAGS. Base science correct. Both `higher` copies are wrong for this page on every route (the CF/TF copy puts HT and triple-HT content on Foundation routes). The device explanations are a physics-only layer the source does not tag. q2's key states a proportionality AQA does not teach and that is untrue for an iron-cored electromagnet. **For Mide:** nothing — the route facts are the spec's own labels.
