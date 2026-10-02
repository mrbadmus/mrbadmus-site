# Examination — Mains Electricity (mains-electricity) — AQA 8464 6.2.3.2 / 8463 4.2.3.2
Verdict: SOURCE OK WITH FLAGS (fuses, circuit breakers, RCDs and double insulation are not on the current spec; the spec's two "explain" points are thin)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.3.2-mains-electricity.md`.
Spec sources read: `AQA-8464-spec.txt` §6.2.3.2; `AQA-8463-spec.txt` §4.2.3.2. A text search of both spec files for "fuse" and "circuit breaker" returns nothing (they were in the pre-2016 AQA spec, not in 8463/8464). Route audit row `mains-electricity` (base / base). No equation applies.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both). All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.2.3.2** | Mains electricity | base |
| 8463 | **4.2.3.2** | Mains electricity | base |

Spec statements (verbatim, 8463 = 8464): "Most electrical appliances are connected to the mains using three-core cable. The insulation covering each wire is colour coded for easy identification: live wire – brown; neutral wire – blue; earth wire – green and yellow stripes. The live wire carries the alternating potential difference from the supply. The neutral wire completes the circuit. The earth wire is a safety wire to stop the appliance becoming live. The potential difference between the live wire and earth (0 V) is about 230 V. The neutral wire is at, or close to, earth potential (0 V). The earth wire is at 0 V, it only carries a current if there is a fault. Students should be able to explain: • that a live wire may be dangerous even when a switch in the mains circuit is open • the dangers of providing any connection between the live wire and earth." WS 1.5.

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | three-core cable; colours (theory 1; key_note) | base | 6.2.3.2 | OK |
| R2 | live carries alternating pd, ~230 V to earth (theory 1) | base | 6.2.3.2 | OK |
| R3 | neutral completes circuit, ~0 V (theory 1; common_mistake) | base | 6.2.3.2 | IMPRECISE (ME-F3) |
| R4 | earth: safety wire, 0 V, current only in a fault, to the metal case (theory 1; common_mistake; q2) | base | 6.2.3.2 | OK |
| R5 | fault: current through earth → fuse blows (theory 1; q2) | base (earth path) + beyond spec (fuse) | 6.2.3.2 | OK / OFF-SPEC |
| R6 | fuses, ratings, circuit breakers, RCDs, double insulation, fuse example (theory 2; key_note) | none — beyond spec | — | OFF-SPEC (ME-F1) |
| R7 | live dangerous: body at 0 V, current through body (theory 3) | base | 6.2.3.2 | OK |
| R8 | fuses and switches in the live wire (theory 3; common_mistake; key_note; q1) | switch: base (feeds "live wire dangerous even when switch open"); fuse: beyond spec | 6.2.3.2 | OFF-SPEC for fuse (ME-F1) |
| R9 | hazards: frayed cables, overloaded sockets, water, damaged plugs (theory 3) | base context ("dangers of any connection between live and earth") | 6.2.3.2 | OK |
| R10 | q1 (fuse in live) | beyond spec | — | not usable (ME-F1) |
| R11 | q2 (earthed fault) | base | 6.2.3.2 | OK, usable all routes |
| — | equations, FIFA, RP, `higher` | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | live brown, neutral blue, earth green-and-yellow stripes | OK | Spec. | 6.2.3.2 |
| C2 | theory 1 | live carries the alternating pd, ~230 V relative to earth | OK | Spec. | 6.2.3.2 |
| C3 | theory 1 | "NEUTRAL … Completes the circuit. Normally at 0 V. Can still carry current — still potentially dangerous." | IMPRECISE | The neutral carries the circuit's current every time the appliance is on — that is what "completes the circuit" means. Spec: "at, or close to, earth potential (0 V)". | 6.2.3.2 |
| C4 | theory 1 | earth carries no current in normal operation; connected to metal case | OK | Spec. | 6.2.3.2 |
| C5 | theory 1 | fault: live → case → current through earth → fuse blows → safe | OK / OFF-SPEC | Correct physics; the fuse is beyond spec. On-spec reading: current flows to earth through the earth wire, so the case does not stay live. | 6.2.3.2 |
| C6 | theory 2 | fuse = thin wire in series with live, melts above rating; 1, 3, 5, 13 A | OFF-SPEC | Correct; not on 8463/8464. | — |
| C7 | theory 2 | circuit breaker trips, resettable; RCD detects imbalance | OFF-SPEC | Correct; not on spec. | — |
| C8 | theory 2 | double insulation, no earth, square-in-square symbol | OFF-SPEC | Correct; not on spec. | — |
| C9 | theory 2 | 1 kW at 230 V: I ≈ 4.3 A → 5 A fuse | OK / OFF-SPEC | 1000 ÷ 230 = 4.35 ✓. Fuse choice beyond spec. | — |
| C10 | theory 3 | touching live while connected to earth → current through body | OK | Body is at 0 V; ~230 V across it. | 6.2.3.2 |
| C11 | theory 3 | switch/fuse in neutral → appliance still at 230 V when "off" | OK | Correct physics. Feeds the spec point; the spec's own point is wider (see ME-F2). | 6.2.3.2 |
| C12 | theory 3 | hazards: frayed cable, overload → heat → fire, water conducts, damaged plugs | OK | Tap water conducts because of dissolved ions. Context. | 6.2.3.2 |
| C13 | common_mistake | earth no current except in a fault; neutral ~0 V but carries current; fuse/switch in live | OK / OFF-SPEC | Fuse beyond spec. | 6.2.3.2 |
| C14 | key_note | as above; "Double insulation = no earth needed" | OK / OFF-SPEC | — | — |
| C15 | q1 key | fuse in neutral → appliance stays at 230 V when fuse blows | OK / OFF-SPEC | Correct physics; the whole item tests fuse placement, which is beyond spec. | — |
| C16 | q1 opt 2 / wx1 | "neutral has too much resistance" / "Neutral wire resistance is very low…" | OK | Aligned. | — |
| C17 | q1 opt 3 / wx2 | "Fuses only work with DC" / "Both wires carry AC — fuses work with AC" | OK | Aligned. | — |
| C18 | q1 opt 4 / wx3 | "neutral is at 230 V" / "Neutral is at ~0 V…" | OK | Aligned. | 6.2.3.2 |
| C19 | q2 key | earthed fault: large current through earth wire, fuse blows, case safe | OK | Earth path on spec; fuse is accepted context. | 6.2.3.2 |
| C20 | q2 opt 2 / wx1 | "metal is a poor conductor" / "Metal is an excellent conductor" | OK | Aligned. | — |
| C21 | q2 opt 3 / wx2 | "earth permanently absorbs fault current" / "low-resistance path … surge blows the fuse … does not permanently carry current" | OK | Aligned. | — |
| C22 | q2 opt 4 / wx3 | "only in thunderstorms" / "activates whenever live connects to earth" | OK | Aligned. | — |
| C23 | matching (to be replaced) | wire roles; fuse | OK / OFF-SPEC | — | — |
| C24 | coverage | spec's two "explain" bullets | GAP | Present only indirectly (ME-F2). Spec core added to the source file. | 6.2.3.2 |

Count: **0 WRONG**. OFF-SPEC: theory 2 throughout, q1. IMPRECISE: C3. GAP: C24.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct physics, but tests fuse placement — not on 8463/8464 | Not usable as a rung on any route. |
| q2 | correct; base | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking:** "you only get a shock if you touch two wires"; "switched off means nothing in the flex is live"; "the earth wire carries current all the time"; "the neutral is at 230 V too"; "earth wire stops the fault"(it gives the fault current a path to earth so the case is not left live).

**Typical questions** ⚑ examiner-drafted
- *Give the colour of the insulation on the earth wire. [1]* — green and yellow (stripes).
- *State the potential difference between the live wire and earth. [1]* — about 230 V.
- *Explain why touching the live wire is dangerous even when the switch is open. [3]* — the live wire is still at 230 V (1); your body is at 0 V / earth potential (1); so there is a large pd across the body and a current flows through it (1).
- *Explain why a connection between the live wire and earth is dangerous. [2]* — a large current flows (1); can cause a shock / heating and fire (1).

## 6. Verdict
SOURCE OK WITH FLAGS. Spec facts right. The protective-device material is off-spec and q1 should not be used. Teach the two "explain" points directly. Nothing for Mide.
