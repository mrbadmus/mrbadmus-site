# Examination — The Life Cycle of a Star (stellar-evolution) — AQA 8463 4.8.1.2 (physics only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/physics-8463-4.8.1.2-stellar-evolution.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.8.1, 4.8.1.1, 4.8.1.2 (the spec's life-cycle diagram does not survive as text; its content — nebula → protostar → main sequence → red giant → white dwarf → black dwarf; red super giant → supernova → neutron star / black hole — is from the published spec page 74). `AQA-8464-spec.txt` checked: Combined Science has no space physics. Route audit `ks4-routes/docs/ks4/route-audit/physics.md` row `stellar-evolution` (TF TH, 4.8.1.2, OK). `figlib/physics.py` `star_life_cycle()` labels checked against the spec diagram (match).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n, as `generate_site_v5.py` pairs them). T1–T3 = theory chunks. Route copies: `higher` is `null` on TF, text on TH. No `[NEW — to be examined]` Convert lines in the file (no calculations).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.8.1.2** | The life cycle of a star | physics only (whole of 4.8.1) |
| 8463 | 4.8.1.1 (supporting) | Our solar system — star formation, fusion equilibrium | physics only |
| 8464 | — | none (no space physics in Combined) | — |
| Header/site record | "6.8.2 (physics only)" | **no such section** | ROUTE (spec ref) flag F1 |

Spec statements (verbatim):
- 4.8.1.1: "The Sun was formed from a cloud of dust and gas (nebula) pulled together by gravitational attraction. Students should be able to explain: how, at the start of a star's life cycle, the dust and gas drawn together by gravity causes fusion reactions; that fusion reactions lead to an equilibrium between the gravitational collapse of a star and the expansion of a star due to fusion energy."
- 4.8.1.2: "A star goes through a life cycle. The life cycle is determined by the size of the star. Students should be able to describe the life cycle of a star: the size of the Sun; much more massive than the Sun. [diagram] Fusion processes in stars produce all of the naturally occurring elements. Elements heavier than iron are produced in a supernova. The explosion of a massive star (supernova) distributes the elements throughout the universe. Students should be able to explain how fusion processes lead to the formation of new elements."
- No "(HT only)" statement in 4.8.1.1 or 4.8.1.2.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Nebula → protostar (gravity, heating) → fusion starts → main sequence (T1) | triple | 4.8.1.1; 4.8.1.2 | TF TH | OK |
| R2 | Main-sequence stability: outward (fusion) vs inward (gravity) in equilibrium (T1, T2; key_note; q1) | triple | 4.8.1.1 | TF TH | OK |
| R3 | Sun-sized: red giant → (planetary nebula) → white dwarf → black dwarf (T2; common_mistake; key_note) | triple | 4.8.1.2 | TF TH | OK |
| R4 | Massive: red supergiant → supernova → neutron star or black hole (T3; key_note) | triple | 4.8.1.2 | TF TH | OK |
| R5 | Mass determines the life cycle (T1, T3; key_note) | triple | 4.8.1.2 | TF TH | OK |
| R6 | Fusion makes new elements; heavier than iron in supernovae; supernova scatters them (T3; key_note; q2) | triple | 4.8.1.2 | TF TH | OK (C21) |
| R7 | `higher`: force balance; remnant conditions; nucleosynthesis in supernovae | **triple (not HT)** for force balance and nucleosynthesis; remnant mass thresholds beyond spec | 4.8.1.1; 4.8.1.2 | TH only | ROUTE (C24) |
| R8 | q1 | triple | 4.8.1.1 | TF TH | OK — usable (C19) |
| R9 | q2 | triple | 4.8.1.2 | TF TH | OK — usable (C21–C22) |
| — | RP, FIFA, equations, `examiner_tip`, variables | none | — | — | correct: none on spec |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | stars form from nebulae of gas and dust, remnants of previous stars | OK | — | 4.8.1.1 |
| C2 | T1 | protostar: gravity pulls gas together; heats as gravitational PE → thermal | OK | — | 4.8.1.1 |
| C3 | T1 | fusion begins at ~10 million °C in the core; H → He | OK | Order of magnitude right. | 4.8.1.1 |
| C4 | T1 | outward radiation pressure from fusion balances inward gravity | OK | Spec: "equilibrium between the gravitational collapse … and the expansion … due to fusion energy". AQA mark schemes credit "outward force/pressure from fusion energy balances gravity". | 4.8.1.1 |
| C5 | T1 | Sun main sequence ~4.6 billion years; ~5 billion more | OK | — | — |
| C6 | T1 | mass determines life cycle and fate | OK | Spec says "size"; mass is the intended meaning. | 4.8.1.2 |
| C7 | T2 | red giant when core H runs out; shell H fusion; He fusion in core; outer layers expand, cool, redder | OK | Detail beyond spec, correct. | 4.8.1.2 |
| C8 | T2 | Sun expands ~200× | OK | Estimates ~100–250×. | — |
| C9 | T2 | planetary nebula: outer layers ejected | OK | Not on the spec diagram; correct context. Design may keep it as a named step or drop it; the examined sequence is red giant → white dwarf. | 4.8.1.2 |
| C10 | T2 | white dwarf: hot, dense, Earth-sized, no fusion, cools → black dwarf, longer than age of universe | OK | — | 4.8.1.2 |
| C11 | T3 | massive stars >8× Sun's mass | OK | Context; spec says "much more massive than the Sun". | 4.8.1.2 |
| C12 | T3 | massive: hotter core, faster fusion, millions of years | OK | — | — |
| C13 | T3 | red supergiant fuses He → C → O → … → iron; iron fusion needs energy input | OK | Spec: "red super giant". | 4.8.1.2 |
| C14 | T3 | core collapses when iron builds up → supernova | OK | — | 4.8.1.2 |
| C15 | T3 | "Briefest moment can outshine entire galaxy" | IMPRECISE (minor) | A supernova can outshine its galaxy for weeks, not a moment. | — |
| C16 | T3 | supernova creates all elements heavier than iron; scattered into space; origin of heavy elements on Earth | OK (spec wording) | Matches 4.8.1.2. (Current astrophysics also credits neutron-star mergers and slow neutron capture in giant stars; AQA examines the spec sentence — see C21.) | 4.8.1.2 |
| C17 | T3 | neutron star: teaspoon ~1 billion tonnes; black hole: light cannot escape | OK | ~10¹⁷ kg/m³ × 5 cm³ ≈ 10⁹ t ✓. | 4.8.1.2 |
| C18 | T3 | complete cycle; ejected material → new nebulae and star systems | OK | Spec: "distributes the elements throughout the universe". | 4.8.1.2 |
| C19 | q1 key | radiation pressure from fusion balances gravity → equilibrium | OK | — | 4.8.1.1 |
| C20 | q1 wx1 → opt 1 "gains mass from surrounding gas"; wx2 → opt 2 "both decrease"; wx3 → opt 3 "fuel not used up" | each rebuts its own option | OK paired; **wx1 IMPRECISE** | Paired ✓ (no shift). wx1 concedes "Stars do gain some mass from surrounding material" — not true of a main-sequence star in any useful sense (it loses mass through fusion and stellar wind; mass gain is a protostar's). Concession is misleading but does not alter the key. | 4.8.1.1 |
| C21 | q2 key | heavier than iron "can only be created in supernova explosions — relatively rare events" | OK (spec) / IMPRECISE ("only") | Matches the spec: "Elements heavier than iron are produced in a supernova." The word "only" overstates real science but is what AQA examines; creditable. | 4.8.1.2 |
| C22 | q2 wx1 → opt 1 "unstable"; wx2 → opt 2 "sink to centres"; wx3 → opt 3 "primordial leftovers" | each rebuts its own option | OK paired; **wx2 IMPRECISE** | Paired ✓ (no shift). wx2 gives "iron, nickel" as heavy elements in planetary cores — iron is not heavier than iron, so the examples do not fit the question's category. wx3 "Big Bang produced only H and He" — plus traces of lithium; fine at GCSE. | 4.8.1.2 |
| C23 | common_mistake | planetary nebula not about planets; white dwarf no fusion; Sun → red giant → white dwarf, not supernova | OK | — | 4.8.1.2 |
| C24 | `higher` (TH) | force-balance mechanism; "specific conditions that determine whether a stellar remnant becomes a white dwarf, neutron star or black hole"; nucleosynthesis of heavy elements | ROUTE / OFF-SPEC (part) | No HT in 4.8.1. Force balance (4.8.1.1) and fusion forming elements (4.8.1.2) are triple base — TF pupils need them. Remnant mass thresholds beyond "much more massive than the Sun → neutron star or black hole" are off-spec. | 4.8.1.1; 4.8.1.2 |
| C25 | key_note | summary; Sun ~10 billion years main sequence | OK | — | 4.8.1.2 |
| C26 | matching (to be replaced) | "Red giant … Sun's eventual fate" | IMPRECISE | The Sun's end state is a white dwarf (then black dwarf); red giant is a stage. Replaced anyway. | 4.8.1.2 |

Count: **0 WRONG**; IMPRECISE C15, C20 (wx1), C21 ("only"), C22 (wx2), C26; ROUTE C24 and header spec ref. **Wrong-explanation alignment checked on both items: every key n explains option n — no one-option-late shift.**

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| None wrong. q1 (wx1 concession imprecise) and q2 (key's "only" is spec wording; wx2 example mismatch) are correct in stem, options and key, and paired correctly. | | Usable on TF and TH. Design may prefer to rebuild q1 with a corrected wx1 (flag F3). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- The Sun will become a supernova / black hole.
- A white dwarf is a small main-sequence star still fusing.
- Main-sequence stability explained as "no forces" rather than balanced forces (gravity in, fusion energy out).
- Stages out of order (red giant before main sequence; white dwarf before red giant); "protostar" omitted.
- Elements heavier than iron made in ordinary main-sequence fusion.
- Planetary nebula = where planets form.

**Command words**: Describe the life cycle (of a star the size of the Sun / much more massive), Explain why the star is stable, Explain how elements are formed, Compare.

**Typical questions** ⚑ examiner-drafted
- *Describe the life cycle of a star much more massive than the Sun, after the main sequence. [3]* — red super giant (1); supernova (1); neutron star or black hole (1).
- *Explain why a main-sequence star is stable. [2]* — inward force of gravity (1); balanced by outward force/pressure from fusion energy (1).
- *Explain how elements heavier than iron are distributed through the universe. [2]* — made in a supernova (1); the explosion scatters them through space (1).
- *Describe how a star forms. [4]* (6-mark lead-in common) — nebula of dust and gas (1); pulled together by gravity (1); heats up / protostar (1); hot enough for fusion of hydrogen nuclei (1).

**Required practical**: none.

**Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All science correct at GCSE; both quiz items usable on TF and TH, explanations paired to their own options. The header's "6.8.2" does not exist — the lesson is 8463 4.8.1.2 (with 4.8.1.1). The TH-only `higher` box holds triple base content (force balance, element formation) that TF pupils also need. Minor imprecisions in two wrong-answer explanations and one theory line.

**For Mide:** nothing. (q2's "only in supernovae" is the spec's own sentence; real astrophysics adds neutron-star mergers, but AQA examines the spec — settled, not a conflict between AQA sources.)
