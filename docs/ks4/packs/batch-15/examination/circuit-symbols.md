# Examination — Standard Circuit Diagram Symbols (circuit-symbols) — AQA 8463 4.2.1.1 / 8464 6.2.1.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.1.1-circuit-symbols.md`.
Spec sources read as text: `AQA-8464-spec.txt` 6.2.1.1–6.2.1.4 (incl. RP15, RP16); `AQA-8463-spec.txt` 4.2.1.1–4.2.1.4 (incl. RP3, RP4). The spec's symbol table is a figure, not text. The symbol shapes were checked against the AQA-checked drawing notes in `figlib/physics.py` (lines 80–101, "AQA 8463 p.24").

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). One route copy.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.2.1.1** | Standard circuit diagram symbols | base |
| 8463 | **4.2.1.1** | Standard circuit diagram symbols | base |
| Supporting | 8464 6.2.1.3 RP15 / 8463 4.2.1.3 RP3 (resistance); 8464 6.2.1.4 RP16 / 8463 4.2.1.4 RP4 (I–V characteristics); 8464 6.2.2 / 8463 4.2.2 (series and parallel) | | base |

Spec statements (verbatim, 8463 = 8464): "Circuit diagrams use standard symbols." [figure: switch (open), switch (closed), cell, battery, diode, resistor, variable resistor, LED, lamp, fuse, voltmeter, ammeter, thermistor, LDR] "Students should be able to draw and interpret circuit diagrams."

RPs (not at this section): 8464 RP15 = 8463 RP3, "use circuit diagrams to set up and check appropriate circuits to investigate the factors affecting the resistance of electrical circuits…"; 8464 RP16 = 8463 RP4, "use circuit diagrams to construct appropriate circuits to investigate the I–V characteristics of a variety of circuit elements, including a filament lamp, a diode and a resistor at constant temperature."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Why standard symbols; drawing rules (theory 1) | base | 6.2.1.1 | OK |
| R2 | The 14 AQA symbols (theory 2; key_note) | base | 6.2.1.1 | OK — the list is complete and exact |
| R3 | Interpreting and drawing (theory 3) | base | 6.2.1.1 | OK |
| R4 | Ammeter series / voltmeter parallel (theory 2–3; common_mistake; q1, q2) | base | 6.2.1.3 (RP context) | OK |
| R5 | `rp` RP15 / RP16 | not this spec point | 6.2.1.3 / 6.2.1.4 | ROUTE (C14) |
| R6 | q1 ammeter | base | 6.2.1.1 / 6.2.1.3 | OK — usable all routes |
| R7 | q2 voltmeter (series circuit, pd shared) | base | 6.2.1.1 / 6.2.2 | OK — usable all routes once "pd is shared in series" has been said |
| — | `higher` | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | standard symbols → universally readable; schematic, not a layout | OK | — | 6.2.1.1 |
| C2 | theory 1 | ruler; straight lines; closed loop; components not on corners | OK | Drawing conventions, not spec text; harmless. | — |
| C3 | theory 2 | cell: long line (+), short line (−) | OK | AQA marks only "+"; the plates are the same thickness, the short one just shorter. | figlib notes |
| C4 | theory 2 | battery: two cells joined by a dashed line | OK | — | figlib notes |
| C5 | theory 2 | switch open / closed | OK | — | — |
| C6 | theory 2 | lamp: circle with a cross | OK | — | — |
| C7 | theory 2 | LED: diode symbol with two arrows pointing out | OK | — | — |
| C8 | theory 2 | ammeter A in series, voltmeter V in parallel | OK | — | 6.2.1.3 |
| C9 | theory 2 | resistor rectangle; variable resistor with diagonal arrow | OK | — | — |
| C10 | theory 2 | thermistor: diagonal line through, short horizontal tail | OK | Matches AQA's drawing: no arrowhead. | figlib notes |
| C11 | theory 2 | LDR: rectangle in a circle, two arrows pointing in | OK | — | — |
| C12 | theory 2 | diode: "triangle pointing to a bar (current flows in the direction of the triangle)" | IMPRECISE (minor) | AQA draws the diode inside a circle, with the wire running through. Design must draw from the figlib symbols, not from these words. Direction statement OK. | figlib notes |
| C13 | theory 2 | fuse: rectangle with a line through its length | OK | — | — |
| C14 | rp | "RP15 (Physics) — Use circuit diagrams to set up and investigate circuits. RP16 — Construct circuits to investigate I–V characteristics." | ROUTE | Not this spec point's RP. RP15/RP16 are the Combined numbers (Physics: RP3/RP4), and they live at 6.2.1.3 and 6.2.1.4. "(Physics)" is wrong. This lesson has no RP. | 8464 6.2.1.3–4 / 8463 4.2.1.3–4 |
| C15 | theory 3 | trace from + terminal; series = same path, parallel = different branches; meters | OK | — | 6.2.2 |
| C16 | common_mistake | ammeter in series, voltmeter in parallel; swapping gives wrong readings or damage; ruler | OK | — | — |
| C17 | key_note | the 13 named symbol types (14 with open + closed switch) | OK | Matches AQA's list exactly. | 6.2.1.1 |
| C18 | q1 key | ammeter in series with the lamp | OK | — | — |
| C19 | q1 opt 1 / wx1 | parallel = voltmeter; ammeter in parallel would short the component | OK, aligned | — | — |
| C20 | q1 opt 2 / wx2 | position matters in branched circuits | OK, aligned | — | — |
| C21 | q1 opt 3 / wx3 | ammeter across battery would short-circuit it | OK, aligned | — | — |
| C22 | q2 key | voltmeter in parallel with the lamp | OK | — | — |
| C23 | q2 opt 1 / wx1 | voltmeter has very high resistance; in series it stops almost all current | OK, aligned | — | — |
| C24 | q2 opt 2 / wx2 | across the cell reads the cell's pd, which is shared in series | OK, aligned | Relies on "pd is shared in series" (6.2.2). Say it in the lesson before q2 (rule 3). | 6.2.2 |
| C25 | q2 opt 3 / wx3 | pd is shared, not the same everywhere, in series | OK, aligned | As C24. | 6.2.2 |
| C26 | matching (to be replaced) | LDR/thermistor behaviour, diode one-way | OK | Behaviour is 6.2.1.4 content; being replaced anyway. | 6.2.1.4 |
| C27 | Convert lines | none | — | — | — |

Count: **0 WRONG**. **ROUTE**: C14. **IMPRECISE**: C12.

## 4. Frozen items wrong for their route
None. q1 and q2 are usable verbatim on all four routes. For q2, the lesson must first say that pd is shared between components in series.

## 5. For the lesson author
**Misconceptions seen in AQA marking**: ammeter drawn in parallel; voltmeter drawn in the loop; thermistor drawn with an arrow (that is a variable resistor); LDR arrows pointing out (that is an LED); gaps left in wires; a battery drawn as one cell; curved freehand wires.

**Command words**: Draw (a circuit diagram), Complete, Identify, Name (the component).

**Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. The symbol list exactly matches AQA's 14. Both quiz items are usable on all routes. The `rp` field names the Combined RP numbers as "(Physics)" and attaches them to the wrong spec point. This lesson has no RP. The diode is described without its circle.

**For Mide:** nothing.
