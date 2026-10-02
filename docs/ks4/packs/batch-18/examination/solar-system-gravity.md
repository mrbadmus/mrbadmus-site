# Examination — Our Solar System and Gravity (solar-system-gravity) — AQA 8463 4.8.1.1 + 4.8.1.3 (physics only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.8.1-solar-system-gravity.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.8 intro, 4.8.1.1, 4.8.1.2, 4.8.1.3, 4.8.2, and 4.5.6.1.3 (circular motion, HT); `AQA-8464-spec.txt` (Combined has no space physics); `8463-equation-sheet-Jun26.txt` (no space equation). Route audit row `solar-system-gravity` (TF TH / TF TH, OK; "HT layer: orbit speed and radius") and §3 note on `gravity-stable-orbits`. Neighbours read: batch-6 `examination/stellar-evolution.md` (owns 4.8.1.1 star formation and fusion equilibrium), batch-5 `examination/red-shift-big-bang.md`.

Conventions: T1–T3 = theory chunks; q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. Quiz identical on TF and TH. TF `higher` copy is `null`. No fifas, no equations, no `[NEW — to be examined]` lines.

**Spec ref settled.** The frozen "6.8.1" is the site's 6.x numbering; there is no Combined space content. True refs: **8463 4.8.1.1 Our solar system** and the non-HT core of **8463 4.8.1.3 Orbital motion, natural and artificial satellites**, both "(physics only)" via 4.8.1. The HT bullets of 4.8.1.3 are a TH layer here and the whole of `gravity-stable-orbits`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | — | none (Combined Science has no space physics) | — |
| 8463 | **4.8.1.1** | Our solar system | physics only |
| 8463 | **4.8.1.3** (first two sentences) | Orbital motion, natural and artificial satellites | physics only |
| 8463 | 4.8.1.3 (HT bullets) | as above | physics only, HT only → TH layer |
| Supporting | 8463 4.5.6.1.3 Velocity (HT) — circular motion: constant speed, changing velocity | | HT |

Spec statements (verbatim):
- 4.8.1.1: "Within our solar system there is one star, the Sun, plus the eight planets and the dwarf planets that orbit around the Sun. Natural satellites, the moons that orbit planets, are also part of the solar system. Our solar system is a small part of the Milky Way galaxy. The Sun was formed from a cloud of dust and gas (nebula) pulled together by gravitational attraction." (The fusion/equilibrium bullets of 4.8.1.1 are taught on `stellar-evolution`, batch 6.)
- 4.8.1.3: "Gravity provides the force that allows planets and satellites (both natural and artificial) to maintain their circular orbits. Students should be able to describe the similarities and distinctions between the planets, their moons, and artificial satellites. (HT only) Students should be able to explain qualitatively how: (HT only) for circular orbits, the force of gravity can lead to changing velocity but unchanged speed; (HT only) for a stable orbit, the radius must change if the speed changes."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | One star, 8 planets, dwarf planets, moons (T1; key_note) | triple | 4.8.1.1 | TF TH | OK |
| R2 | Asteroid belt, comets, planet order + mnemonic (T1) | triple (context) | — | TF TH | OK, not assessed |
| R3 | Scale: AU, Proxima 4.25 ly, Milky Way 100,000 ly, 1 ly = 9.46 × 10¹⁵ m (T1; key_note) | none — off-spec | — | TF TH | OFF-SPEC (F6) |
| R4 | All masses attract; gravity non-contact; Sun's gravity holds planets, Earth's holds Moon (T2) | triple | 4.8.1.3; 4.5.1.2 | TF TH | OK |
| R5 | Gravity directed to centre, "centripetal" (T2; key_note) | triple-higher | 4.8.1.3 HT bullet 1 | TF TH | ROUTE (F1) |
| R6 | Closer → faster; higher orbit = slower, longer period (T2; key_note; q1) | triple-higher | 4.8.1.3 HT bullet 2 | TF TH | ROUTE (F1); IMPRECISE (F4) |
| R7 | Natural satellites; Moon 27 days; geostationary vs LEO uses (T2; common_mistake; key_note; q2) | triple | 4.8.1.3 ("similarities and distinctions … artificial satellites") | TF TH | OK; GPS WRONG (F2) |
| R8 | Stars, galaxies, Milky Way, universe size/age, AU/ly/parsec, probes, telescopes (T3) | triple for "solar system is a small part of the Milky Way"; rest off-spec | 4.8.1.1 | TF TH | OK / OFF-SPEC (F6); Andromeda WRONG (F3) |
| R9 | `higher` (TH): gravity as centripetal force; radius vs speed; GEO vs LEO; periods | triple-higher (first two); triple context (GEO/LEO); off-spec (periods) | 4.8.1.3 | TH only (TF `null`) | OK on TH; keep brief — owned by `gravity-stable-orbits` (F1) |
| R10 | common_mistake: GEO above equator, 24 h; Sun at focus of ellipse | triple (GEO); off-spec (ellipse) | 4.8.1.3 | TF TH | IMPRECISE (F5) |
| R11 | q1 | triple-higher | 4.8.1.3 HT bullet 2 | TF TH | usable TH only |
| R12 | q2 | triple | 4.8.1.3 | TF TH | usable TF TH |
| R13 | Sun formed from nebula by gravity; similarities/distinctions planets–moons–artificial satellites | triple | 4.8.1.1; 4.8.1.3 | — | GAP (F7) |
| — | RP, equations, fifas | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | Sun ~99.8% of Solar System mass | OK | 99.86% | — |
| C2 | T1 | 8 planets, approximately circular or elliptical orbits | OK | Spec models orbits as circular. | 4.8.1.3 |
| C3 | T1 | dwarf planets e.g. Pluto, Ceres; moons = natural satellites | OK | Spec wording. | 4.8.1.1 |
| C4 | T1 | asteroid belt between Mars and Jupiter; comets icy, highly elliptical | OK | Context. | — |
| C5 | T1 | order Mercury … Neptune; mnemonic | OK | — | — |
| C6 | T1 | 1 AU = 1.5 × 10¹¹ m | OK (off-spec) | 1.496 × 10¹¹ m | — |
| C7 | T1 | Proxima Centauri ~4.25 ly | OK (off-spec) | 4.24 ly | — |
| C8 | T1 | Milky Way ~100,000 ly across | OK (off-spec) | Conventional figure. | — |
| C9 | T1; key_note | 1 ly = 9.46 × 10¹⁵ m | OK (off-spec) | "light-year" appears nowhere in 8463. | — |
| C10 | T2 | all masses attract; gravity non-contact | OK | — | 4.5.1.2 |
| C11 | T2 | Sun's gravity keeps planets in orbit; Earth's keeps Moon | OK | Spec core. | 4.8.1.3 |
| C12 | T2 | gravity is the centripetal force, always towards the centre | OK, HT | "Centripetal" is not a spec word; the idea (force to centre changes direction, not speed) is the HT bullet. | 4.8.1.3 HT |
| C13 | T2 | closer planets move faster "to balance the stronger gravitational pull" | IMPRECISE | Nothing is balanced: gravity is the resultant force, changing the direction of motion. Say: gravity is stronger closer in, so a planet there must move faster to stay in a stable orbit at that radius. | 4.8.1.3 HT |
| C14 | T2 | Moon period ~27 days | OK | 27.3 d (sidereal) | — |
| C15 | T2 | hundreds of moons known | OK | ~290+ | — |
| C16 | T2 | geostationary 35,786 km altitude, 24 h, appears stationary, comms and weather | OK | Period is Earth's rotation period (23 h 56 min); "24 hours" is credited at GCSE. | — |
| C17 | T2 | LEO 200–2000 km, ~90 min | OK | 88–127 min across that range; ~90 min at ISS height. | — |
| C18 | T2 | LEO "Used for: ISS, Earth observation, GPS" | **WRONG** | GPS satellites are in medium Earth orbit, ~20,200 km, period ~12 h. ISS and Earth observation are correct. | — |
| C19 | T2 | higher orbit = slower speed, longer period | OK, HT | Period is not in the spec; speed vs radius is HT. | 4.8.1.3 HT |
| C20 | T3 | Sun = star, plasma, fusion | OK | — | 4.8.1.1 |
| C21 | T3 | stars grouped into galaxies; Milky Way 200–400 billion stars | OK | Estimates 100–400 bn. | 4.8.1.1 |
| C22 | T3 | "Nearest galaxy to us: Andromeda (~2.5 million light-years)" | **WRONG** | Andromeda is the nearest large (spiral) galaxy, ~2.5 million ly. Nearer galaxies exist: dwarf satellites of the Milky Way (Sagittarius Dwarf ~70,000 ly; Large Magellanic Cloud ~160,000 ly). | — |
| C23 | T3 | ~2 trillion galaxies | IMPRECISE (off-spec) | 2016 estimate, revised down (2021) to a few hundred billion. Say "hundreds of billions" or drop. | — |
| C24 | T3 | observable universe ~93 bn ly across; age ~13.8 bn yr | OK (off-spec) | Belongs to `red-shift-big-bang` context. | — |
| C25 | T3 | AU average Earth–Sun distance; parsec = 3.26 ly | OK (off-spec) | — | — |
| C26 | T3 | Voyager, New Horizons, Mars rovers; Hubble visible, JWST infrared, Chandra X-ray; ISS crewed since 2000 | OK (off-spec) | Hubble also observes UV and near-IR; "visible" acceptable. ISS crewed since Nov 2000. | — |
| C27 | `higher` | gravity as centripetal force; radius changes if speed changes; compare GEO/LEO; lower orbit shorter period, higher speed | OK on TH | First two are the HT bullets; periods off-spec. Its depth is `gravity-stable-orbits`' job. | 4.8.1.3 HT |
| C28 | common_mistake | GEO above the equator, "period of exactly 24 hours" | IMPRECISE | Period equals Earth's rotation period; "exactly 24 hours" is not exact (23 h 56 min). Say "24 hours — the same time Earth takes to turn once". | — |
| C29 | common_mistake | Sun not at exact centre; orbits slightly elliptical, Sun at one focus | OK science, OFF-SPEC | 8463 states "circular orbits". Teaching the ellipse as the "mistake" fights the spec's model. Drop, or one aside. | 4.8.1.3 |
| C30 | key_note | GEO 36,000 km, LEO 200–2000 km 90 min, 1 ly | OK | 36,000 = rounded 35,786 ✓. | — |
| C31 | q1 key | gravity stronger closer → higher orbital speed needed "to prevent being pulled into the Sun" | OK (IMPRECISE wording) | AQA credits "gravity is stronger so higher speed needed to stay in orbit". "Prevent being pulled in" is a simplification; acceptable. HT content. | 4.8.1.3 HT |
| C32 | q1 wx1 → opt 1 "closer planets are smaller" | size/mass doesn't decide orbital speed; same radius → same speed | OK, paired | True for a body much less massive than the Sun. | — |
| C33 | q1 wx2 → opt 2 "radiation pressure" | negligible vs gravity | OK, paired | — | — |
| C34 | q1 wx3 → opt 3 "Sun's rotation drags planets" | orbits set by gravity and initial velocity | OK, paired | — | — |
| C35 | q2 key | GEO stays over a fixed point; dishes need no tracking | OK | — | 4.8.1.3 |
| C36 | q2 wx1 → opt 1 "GEO closer" | GEO ~36,000 km vs ISS ~400 km; delay greater | OK, paired | — | — |
| C37 | q2 wx2 → opt 2 "GEO faster" | GEO slower (24 h vs 90 min) | OK, paired | GEO ≈ 3.1 km/s vs LEO ≈ 7.7 km/s. | — |
| C38 | q2 wx3 → opt 3 "more GEO than LEO" | more LEO; moving ones need tracking | OK, paired | — | — |
| C39 | matching (to be replaced) | GEO, LEO, asteroid belt, light-year | OK | — | — |
| C40 | spec coverage | nebula formation; similarities/distinctions planets–moons–artificial satellites | GAP | Neither is taught as a statement (F7). | 4.8.1.1; 4.8.1.3 |

Count: **2 WRONG** (C18 GPS in LEO; C22 Andromeda nearest galaxy) — both in re-cuttable theory, no frozen quiz item affected. IMPRECISE: C13, C23, C28, C31. All `wrong_explanations` paired to their own options (read by hand, 6/6).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | HT content (4.8.1.3 HT bullet 2) served on TF | TH only. |
| q2 | — | usable TF TH. |

## 5. Verdict
SOURCE HAS ERRORS — two wrong facts in theory (GPS orbit; nearest galaxy), both re-cuttable; both quiz items correct and correctly paired. The speed-vs-radius material is HT and must be a TH layer, kept short because `gravity-stable-orbits` owns it. Two spec statements are absent (nebula formation; planet–moon–artificial-satellite comparison). Most of T3 and all scale figures are off-spec context.

**For Mide:** nothing — all settled from the 8463 text.
