// @vitest-environment node
// Gate 16 — the outer surface can be AUTHORED, and two palettes stand over one
// record (MRB-218).
//
// The acquired heart's GLB declares ONE material and points all twelve parts at
// it, so the specimen renders as a single pale solid — "looks like a model, I
// want to see it as a proper heart". The fix is the same shape as MRB-217's:
// the record carries a SEMANTIC TOKEN per structure, the renderer owns the
// mapping from token to colour and finish, and the join is the one that already
// exists rather than a second lookup.
//
// What this file pins:
//   1. the resolution order and both inheritance steps, plus the fallback
//   2. the twelve authored assignments, by name — including the pulmonary
//      exception, which is the whole reason the colouring teaches anything
//   3. that BOTH palettes cover ALL SIX tokens with no gaps and no overlap
//   4. that the hotspot numerals still read against all twelve surface colours
//   5. that the cut face is untouched
//
// The mutations this gate was proved against are recorded at the foot of the
// file.

import { describe, expect, it } from 'vitest'
import { readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import {
  APPEARANCES,
  DEFAULT_PALETTE,
  PALETTES,
  PALETTE_IDS,
  resolveAppearance,
  surfaceColour,
  surfaceFinish,
  type PaletteId,
} from '../../src/renderer/mesh/appearance'
import { capColour } from '../../src/renderer/mesh/cap'
import { TIER_RIGS } from '../../src/renderer/mesh/tiers'
import { indexHotspots } from '../../src/renderer/mesh/cutmaterial'
import { specimens } from '../../src/studio/content'
import { hotspotVisual, type HotspotState } from '../../src/components/HotspotDot'
import type { Appearance, HotspotRecord, SpecimenRecord } from '../../src/studio/types'

function hotspot(id: string, appearance?: Appearance): HotspotRecord {
  return {
    id,
    label: id,
    detail: 'x',
    position3d: [0, 0, 0],
    position2d: [0, 0],
    tiers: ['foundation'],
    retrievable: true,
    ...(appearance ? { appearance } : {}),
  } as HotspotRecord
}

function specimen(
  hotspots: HotspotRecord[],
  appearance?: Appearance,
): Pick<SpecimenRecord, 'id' | 'hotspots'> & { appearance?: Appearance } {
  return { id: 'heart', hotspots, ...(appearance ? { appearance } : {}) }
}

const heart = specimens.find((s) => s.id === 'heart')!

// ─────────────────────────────────────────────────────────────────────────────

describe('gate 16 — resolution order, and it is MRB-217’s', () => {
  it('1. the hotspot’s own declaration wins over the specimen’s', () => {
    const record = specimen([hotspot('heart.left-ventricle', 'valve')], 'blood-oxygenated')
    expect(resolveAppearance('Left ventricle', record)).toBe('valve')
  })

  it('2. a silent hotspot inherits the specimen’s', () => {
    const record = specimen([hotspot('heart.left-ventricle')], 'blood-oxygenated')
    expect(resolveAppearance('Left ventricle', record)).toBe('blood-oxygenated')
  })

  it('3. neither declared resolves to null — the fallback tone decides', () => {
    expect(resolveAppearance('Left ventricle', specimen([hotspot('heart.left-ventricle')])))
      .toBeNull()
  })

  it('a part with NO matching hotspot falls through silently, not to an error', () => {
    const record = specimen([hotspot('heart.left-ventricle', 'valve')])
    expect(resolveAppearance('Some unnamed shell', record)).toBeNull()
  })

  it('a part with no matching hotspot still takes the specimen default', () => {
    const record = specimen([hotspot('heart.left-ventricle')], 'valve')
    expect(resolveAppearance('Some unnamed shell', record)).toBe('valve')
  })

  it('a nameless part is not a lookup failure, it is no lookup at all', () => {
    expect(resolveAppearance('', specimen([], 'valve'))).toBe('valve')
    expect(resolveAppearance('', specimen([]))).toBeNull()
  })

  it('the indexed and unindexed paths agree', () => {
    const hotspots = [hotspot('heart.aorta', 'vessel-oxygenated'), hotspot('heart.left-atrium')]
    const record = specimen(hotspots, 'valve')
    const index = indexHotspots(hotspots)
    for (const part of ['Aorta', 'Left atrium', 'Nothing at all']) {
      expect(resolveAppearance(part, record, index)).toBe(resolveAppearance(part, record))
    }
  })

  it('it binds by the SAME slug rule as the cut material — one lookup, two fields', () => {
    // Not a restatement: this is the assertion that fails if someone gives
    // `appearance` a lookup of its own that drifts from `cutMaterial`'s.
    const record = specimen([hotspot('heart.vena-cava', 'vessel-deoxygenated')])
    expect(resolveAppearance('Vena cava', record)).toBe('vessel-deoxygenated')
    expect(resolveAppearance('  VENA   CAVA  ', record)).toBe('vessel-deoxygenated')
  })
})

// ─────────────────────────────────────────────────────────────────────────────

describe('gate 16 — the authored map for the heart (Mide, 15 Aug)', () => {
  /** part name → token, exactly as signed off. Written out rather than derived
   * from the record, or this would assert the record equals itself. */
  const AUTHORED: ReadonlyArray<readonly [string, Appearance]> = [
    ['Right atrium', 'blood-deoxygenated'],
    ['Right ventricle', 'blood-deoxygenated'],
    ['Left atrium', 'blood-oxygenated'],
    ['Left ventricle', 'blood-oxygenated'],
    ['Vena cava', 'vessel-deoxygenated'],
    ['Pulmonary artery', 'vessel-deoxygenated'],
    ['Aorta', 'vessel-oxygenated'],
    ['Pulmonary vein', 'vessel-oxygenated'],
    ['Coronary arteries', 'vessel-oxygenated'],
    ['Tricuspid valve', 'valve'],
    ['Bicuspid valve', 'valve'],
    ['Semilunar valves', 'valve'],
  ]

  const index = indexHotspots(heart.hotspots)

  for (const [part, token] of AUTHORED) {
    it(`${part} is ${token}`, () => {
      expect(resolveAppearance(part, heart, index)).toBe(token)
    })
  }

  it('all twelve GLB parts are authored — none falls through to the fallback', () => {
    const unauthored = AUTHORED.filter(([part]) => resolveAppearance(part, heart, index) === null)
    expect(unauthored.map(([p]) => p)).toEqual([])
  })

  it('THE PULMONARY EXCEPTION: the artery is deoxygenated, the vein oxygenated', () => {
    // The most-examined exception in the topic, and the reason the colouring is
    // teaching rather than decoration. Written as its own assertion so that
    // "correcting" it to the artery=red / vein=blue intuition fails loudly here
    // instead of quietly teaching the wrong thing to 135 students.
    expect(resolveAppearance('Pulmonary artery', heart, index)).toBe('vessel-deoxygenated')
    expect(resolveAppearance('Pulmonary vein', heart, index)).toBe('vessel-oxygenated')
    // And they must not agree with each other under either palette.
    for (const palette of PALETTE_IDS) {
      expect(surfaceColour('vessel-deoxygenated', palette)).not.toBe(
        surfaceColour('vessel-oxygenated', palette),
      )
    }
  })

  it('the chambers take BLOOD tokens, because the geometry IS the blood', () => {
    // BodyParts3D models chambers as blood-volume casts. This file used to say
    // the four would MOVE to muscle tokens once a shell-modelled mesh landed.
    // That is not what happened (MRB-222): the wall arrived as a SEPARATE part
    // beside them, so the casts keep their blood tokens and the reading is now
    // literal rather than a convenient one.
    for (const part of ['Right atrium', 'Right ventricle', 'Left atrium', 'Left ventricle']) {
      expect(resolveAppearance(part, heart, index)!.startsWith('blood-')).toBe(true)
    }
  })

  it('THE WALL AND THE BLOOD ARE DIFFERENT SURFACES (MRB-222)', () => {
    // The whole point of the sixth token. If the myocardium ever painted as
    // blood, the specimen would go back to being one undifferentiated red mass
    // and the wall a student is meant to SEE would disappear into the chamber
    // it surrounds.
    expect(resolveAppearance('Ventricular myocardium', heart, index)).toBe('muscle')
    for (const palette of PALETTE_IDS) {
      for (const blood of ['blood-oxygenated', 'blood-deoxygenated'] as const) {
        expect(surfaceColour('muscle', palette)).not.toBe(surfaceColour(blood, palette))
      }
    }
  })

  it('the three wall parts with no hotspot inherit the specimen’s muscle', () => {
    // These are real GLB parts the record names no hotspot for — naming one
    // would be authoring anatomy outside the science gate. They rely on the
    // specimen default, which is why it is set.
    for (const part of ['Ventricular myocardium', 'Right atrial wall', 'Left atrial wall']) {
      expect(heart.hotspots.find((h) => h.id === `heart.${part.toLowerCase().replace(/ /g, '-')}`))
        .toBeUndefined()
      expect(resolveAppearance(part, heart, index)).toBe('muscle')
    }
  })

  it('the two coordinate-anchored hotspots declare nothing', () => {
    // The septum and the sino-atrial node have no part in the GLB, so there is
    // no surface of theirs to paint. Silence here is correct, not an omission.
    for (const id of ['heart.septum', 'heart.sino-atrial-node']) {
      expect(heart.hotspots.find((h) => h.id === id)!.appearance).toBeUndefined()
    }
  })

  it('the specimen defaults to muscle, and that default is load-bearing', () => {
    // It was `undefined` until MRB-222, when three real GLB parts arrived with
    // no hotspot of their own. Without this the myocardium and both atrial
    // walls would fall through to the palette's neutral unauthored tone and the
    // heart would render its muscle as "no claim made".
    expect((heart as { appearance?: Appearance }).appearance).toBe('muscle')
    expect(resolveAppearance('Ventricular myocardium', heart)).toBe('muscle')
  })

  it('the default does not silently repaint anything that authors its own', () => {
    // The risk of introducing a specimen-level default: a hotspot that used to
    // resolve to null now inherits instead. Every one of the twelve authored
    // parts must still win over it.
    for (const [part, token] of AUTHORED) {
      expect(resolveAppearance(part, heart, index)).toBe(token)
      expect(resolveAppearance(part, heart, index)).not.toBe('muscle')
    }
  })
})

// ─────────────────────────────────────────────────────────────────────────────

describe('gate 16 — two palettes over one record', () => {
  it('realistic is the default (Mide, 15 Aug)', () => {
    expect(DEFAULT_PALETTE).toBe('realistic')
  })

  for (const palette of PALETTE_IDS) {
    it(`the ${palette} palette covers all six tokens with no gaps`, () => {
      const table = PALETTES[palette]
      for (const token of APPEARANCES) {
        const colour = table.colours[token]
        expect(colour, `${palette} has no colour for '${token}'`).toBeTruthy()
        expect(colour).toMatch(/^#[0-9A-F]{6}$/)
      }
      // …and no colours BEYOND the six, so a token cannot be quietly retired
      // from the type while its colour lingers.
      expect(Object.keys(table.colours).sort()).toEqual([...APPEARANCES].sort())
    })

    it(`the ${palette} palette gives six DISTINCT colours`, () => {
      const values = APPEARANCES.map((t) => surfaceColour(t, palette))
      expect(new Set(values).size).toBe(APPEARANCES.length)
    })

    it(`the ${palette} palette's unauthored tone is NOT one of the six`, () => {
      // Unauthored geometry must never claim to be oxygenated or deoxygenated
      // anything — that would be the studio inventing anatomy.
      const values = APPEARANCES.map((t) => surfaceColour(t, palette))
      expect(values).not.toContain(PALETTES[palette].unauthored)
      expect(surfaceColour(null, palette)).toBe(PALETTES[palette].unauthored)
    })
  }

  it('the two palettes really are different mappings, not one table twice', () => {
    const differing = APPEARANCES.filter(
      (t) => surfaceColour(t, 'realistic') !== surfaceColour(t, 'schematic'),
    )
    expect(differing).toEqual([...APPEARANCES])
  })

  it('deoxygenated is DARK RED in realistic and BLUE in schematic', () => {
    // The teaching point the realistic palette exists to carry: blue is a
    // diagram convention, not a fact about blood. Asserted by channel order
    // rather than by hex, so a retune of either palette that kept the meaning
    // still passes and one that inverted the meaning does not.
    const chan = (hex: string) => ({
      r: parseInt(hex.slice(1, 3), 16),
      b: parseInt(hex.slice(5, 7), 16),
    })
    for (const token of ['blood-deoxygenated', 'vessel-deoxygenated'] as const) {
      const real = chan(surfaceColour(token, 'realistic'))
      expect(real.r, `realistic '${token}' must be red-dominant`).toBeGreaterThan(real.b)
      const schematic = chan(surfaceColour(token, 'schematic'))
      expect(schematic.b, `schematic '${token}' must be blue-dominant`).toBeGreaterThan(schematic.r)
    }
    // Oxygenated stays red-dominant in BOTH — the convention only moves the
    // deoxygenated half.
    for (const token of ['blood-oxygenated', 'vessel-oxygenated'] as const) {
      for (const palette of PALETTE_IDS) {
        const c = chan(surfaceColour(token, palette))
        expect(c.r, `${palette} '${token}'`).toBeGreaterThan(c.b)
      }
    }
  })

  it('in REALISTIC, deoxygenated is DARKER than its oxygenated partner', () => {
    // Hue-dominance alone cannot see a swap inside the realistic palette:
    // both halves of each pair are red-dominant there, so exchanging them
    // leaves every channel test happy while teaching the inverse of the truth.
    // (This gate shipped without this assertion and a deliberate swap passed
    // all 53 tests — which is why the mutation run at the foot of this file
    // exists at all.)
    //
    // Lightness is the relation that actually carries the science: oxygenated
    // haemoglobin is BRIGHT red and deoxygenated is DARK red. That is the fact
    // the realistic palette is for, and it is directional, so a swap inverts it.
    for (const [oxy, deoxy] of [
      ['blood-oxygenated', 'blood-deoxygenated'],
      ['vessel-oxygenated', 'vessel-deoxygenated'],
    ] as const) {
      const light = luma(surfaceColour(oxy, 'realistic'))
      const dark = luma(surfaceColour(deoxy, 'realistic'))
      expect(
        dark,
        `realistic '${deoxy}' (${dark.toFixed(3)}) must be darker than '${oxy}' ` +
          `(${light.toFixed(3)}) — oxygenated blood is the brighter red`,
      ).toBeLessThan(light)
    }
  })

  it('a palette switch changes colour ONLY — finish is palette-independent', () => {
    // This is what makes the swap cost one colour write per material with no
    // shader recompile, and what lets it happen mid-cross-section without
    // disturbing the clipping planes.
    for (const token of APPEARANCES) {
      expect(surfaceFinish(token)).toBe(surfaceFinish(token))
    }
    expect(surfaceFinish('valve').roughness).toBeGreaterThan(
      surfaceFinish('blood-oxygenated').roughness,
    )
  })
})

// ─────────────────────────────────────────────────────────────────────────────
// The hotspot numerals against every new surface.
//
// Numerals are MARKS, exempt from the 4.5:1 text rule — but size, fill
// inversion and ring must still carry identity (§07, gate 2). Two things have
// to hold, and they are different questions:
//
//   a. the numeral against ITS OWN FILL. Tissue-independent: the glyph sits on
//      the dot, not on the specimen. Unchanged by this work.
//   b. the DOT against the tissue. The dark variant's construction is a cream
//      ring INSIDE a near-black halo — a two-sided rim — so the dot keeps an
//      edge on a light ground via the halo and on a dark ground via the ring.
//
// (b) is asserted with the same Rec. 601 separation gate 2 uses on the cut
// face, and it is asserted TWO-SIDED: neither rim alone clears all twelve, so a
// "simplification" that drops either one fails here.

const GROUND_SEPARATION = 0.25

function luma(hex: string): number {
  const n = parseInt(hex.slice(1), 16)
  return (0.299 * (n >> 16) + 0.587 * ((n >> 8) & 255) + 0.114 * (n & 255)) / 255
}

/** The near-black halo composited over the tissue behind it. Rec. 601 luma is
 * linear in the encoded channels, so blending the levels equals blending the
 * channels and taking the luma of the result. */
function haloOver(tissue: string, halo = '#080604', alpha = 0.6): number {
  return alpha * luma(halo) + (1 - alpha) * luma(tissue)
}

const RING = '#FBF3E6' // the dark variant's ring, every state
const SURFACES: ReadonlyArray<readonly [PaletteId, Appearance, string]> = PALETTE_IDS.flatMap(
  (palette) => APPEARANCES.map((token) => [palette, token, surfaceColour(token, palette)] as const),
)

describe('gate 16 — hotspot numerals still read against all twelve surfaces', () => {
  it('there are exactly twelve surfaces to check', () => {
    expect(SURFACES).toHaveLength(12)
    expect(new Set(SURFACES.map(([, , hex]) => hex)).size).toBe(12)
  })

  for (const [palette, token, hex] of SURFACES) {
    it(`the dot keeps an edge on ${palette}/${token} (${hex})`, () => {
      const ground = luma(hex)
      const ring = Math.abs(luma(RING) - ground)
      const halo = Math.abs(haloOver(hex) - ground)
      expect(
        Math.max(ring, halo),
        `${palette}/${token} ${hex}: ring Δ${ring.toFixed(3)}, halo Δ${halo.toFixed(3)} — ` +
          'the dot has no edge on this tissue',
      ).toBeGreaterThanOrEqual(GROUND_SEPARATION)
    })
  }

  it('BOTH rims are load-bearing — neither alone clears all twelve', () => {
    // The assertion that keeps the ring-inside-halo construction from being
    // "simplified" to one rim. The cream ring closes up on the pale valve
    // tones; the dark halo closes up on deoxygenated blood and on muscle. Each
    // covers where the other cannot, which is precisely why the dot is
    // ground-independent.
    const ringFails = SURFACES.filter(([, , hex]) => Math.abs(luma(RING) - luma(hex)) < GROUND_SEPARATION)
    const haloFails = SURFACES.filter(([, , hex]) => Math.abs(haloOver(hex) - luma(hex)) < GROUND_SEPARATION)
    expect(ringFails.length, 'the ring alone would suffice — check this gate still means anything')
      .toBeGreaterThan(0)
    expect(haloFails.length, 'the halo alone would suffice — check this gate still means anything')
      .toBeGreaterThan(0)
    // …and they never fail on the SAME surface, which is the property that
    // makes max(ring, halo) clear everywhere.
    const both = ringFails.filter((r) => haloFails.some((h) => h[2] === r[2]))
    expect(both.map(([p, t]) => `${p}/${t}`)).toEqual([])
  })

  it('the numeral’s own contrast is tissue-independent and unmoved by this work', () => {
    // The glyph sits on the dot's fill. Repainting the specimen cannot touch
    // it, and this pins that it did not.
    const states: HotspotState[] = ['closed', 'hover', 'open', 'target']
    for (const state of states) {
      const v = hotspotVisual(state, 'dark')
      expect(Math.abs(luma(v.color) - luma(v.background))).toBeGreaterThanOrEqual(
        GROUND_SEPARATION,
      )
    }
  })
})

// ─────────────────────────────────────────────────────────────────────────────

describe('gate 16 — the finish is roughness, and that was measured', () => {
  it('the three tissue finishes are ordered wet → fibrous → matte', () => {
    // The relation, not the numbers: blood is the wettest thing on the
    // specimen, a vessel wall is drier than the blood inside it, and a valve
    // is the matte exception. Asserted as an ordering so a retune that keeps
    // the meaning passes and one that flattens everything to a single value
    // does not.
    const blood = surfaceFinish('blood-oxygenated').roughness
    const vessel = surfaceFinish('vessel-oxygenated').roughness
    const valve = surfaceFinish('valve').roughness
    expect(blood).toBeLessThan(vessel)
    expect(vessel).toBeLessThan(valve)
  })

  it('the two blood tokens and the two vessel tokens share a finish', () => {
    // Oxygenation is a fact about the blood, not about how the surface takes
    // the light. If these ever diverge, the palette has leaked into the finish.
    expect(surfaceFinish('blood-oxygenated')).toEqual(surfaceFinish('blood-deoxygenated'))
    expect(surfaceFinish('vessel-oxygenated')).toEqual(surfaceFinish('vessel-deoxygenated'))
  })

  it('nothing is metal, and everything is in range', () => {
    for (const token of APPEARANCES) {
      const finish = surfaceFinish(token)
      expect(finish.metalness).toBe(0)
      expect(finish.roughness).toBeGreaterThan(0)
      expect(finish.roughness).toBeLessThanOrEqual(1)
    }
    expect(surfaceFinish(null).metalness).toBe(0)
  })

  it('the unauthored tone is flatter than every authored tissue but the valve', () => {
    // Unauthored geometry must not read as more confidently rendered than the
    // structures Mide has actually signed off.
    const unauthored = surfaceFinish(null).roughness
    expect(unauthored).toBeGreaterThan(surfaceFinish('blood-oxygenated').roughness)
    expect(unauthored).toBeGreaterThan(surfaceFinish('vessel-oxygenated').roughness)
  })

  it('THE SHEEN LOBE IS GONE, and must not come back unmeasured', () => {
    // MeshPhysicalMaterial + sheen cost 100.0→116.6ms at Tier A and
    // 33.4→50.0ms at Tier B on 3d_render_check.py, reproducibly. The cost was
    // the `physical` shader itself, not the lobe — gating the lobe by tier
    // changed nothing, which is why TierRig has no `sheen` flag. Roughness
    // alone reads wetter anyway.
    //
    // Written as a shape assertion so that reintroducing sheen fields here
    // fails, and whoever does it has to come back through the numbers above.
    const finish = surfaceFinish('blood-oxygenated') as unknown as Record<string, unknown>
    expect(Object.keys(finish).sort()).toEqual(['metalness', 'roughness'])
    expect((TIER_RIGS.A as unknown as Record<string, unknown>).sheen).toBeUndefined()
  })

  it('the renderer builds MeshStandardMaterial, not MeshPhysicalMaterial', () => {
    const source = readFileSync(
      resolve(dirname(fileURLToPath(import.meta.url)), '../../src/renderer/mesh/surface.ts'),
      'utf8',
    )
    expect(source).toMatch(/new THREE\.MeshStandardMaterial\(/)
    expect(source).not.toMatch(/new THREE\.MeshPhysicalMaterial\(/)
  })
})

describe('gate 16 — the cut face is untouched', () => {
  it('no surface colour collides with either cut-face value', () => {
    // Flatness is what says "cut". If a tissue colour ever equalled a cap
    // colour the section would stop reading as a section.
    const cut = [capColour(0), capColour(1)]
    for (const [, , hex] of SURFACES) expect(cut).not.toContain(hex)
  })

  it('the cut face’s own pair is still §08’s, at 15.62:1', () => {
    expect(capColour(0)).toBe('#F0E9DC')
    expect(capColour(1)).toBe('#141109')
  })

  it('nothing here introduces --st-accent as a surface', () => {
    // #E4572E marks the PLANE and the hotspots; it is barred as a contrast
    // partner for text under 24px and must never become tissue.
    const accent = '#E4572E'
    for (const [, , hex] of SURFACES) expect(hex).not.toBe(accent)
    for (const palette of PALETTE_IDS) {
      expect(PALETTES[palette].unauthored).not.toBe(accent)
    }
  })

  it('the renderer never paints the cap: SectionCap builds its own materials', () => {
    // Read as text rather than executed — importing cap.tsx's component would
    // pull R3F into a node gate. What matters is the structural fact that the
    // cap's mesh is constructed with a material of its own, so the surface coat
    // laid over the MODEL cannot reach it.
    const source = readFileSync(
      resolve(dirname(fileURLToPath(import.meta.url)), '../../src/renderer/mesh/cap.tsx'),
      'utf8',
    )
    expect(source).toMatch(/new THREE\.MeshBasicMaterial\(\{[\s\S]*?toneMapped: false/)
    expect(source).not.toMatch(/appearance|surfaceColour|PALETTES/)
  })
})

// ─────────────────────────────────────────────────────────────────────────────
// MUTATIONS THIS GATE WAS PROVED AGAINST
//
// A gate nobody has watched fail is a spell-check that is switched off. Each of
// these was applied, the suite run, and the failure observed before the change
// was reverted:
//
//   1. inheritance inverted (specimen ?? hotspot)      → 1 failed
//        'the hotspot's own declaration wins over the specimen's'
//   2. the `?? null` fallback replaced with a token     → 3 failed
//        'neither declared resolves to null', and both no-matching-hotspot cases
//   3. 'valve' deleted from the schematic palette       → 3 failed
//        'the schematic palette covers all six tokens with no gaps', plus the
//        surface sweep, which stops being a sweep of twelve
//   4. realistic oxy/deoxy swapped, blood then vessel   → 1 failed each
//        'in REALISTIC, deoxygenated is DARKER than its oxygenated partner'
//   5. the validator's APPEARANCES enum widened         → 3 failed
//        content-validation.test.ts's three rejection cases
//   6. the pulmonary artery re-authored as oxygenated   → 2 failed
//        'Pulmonary artery is vessel-deoxygenated' and 'THE PULMONARY EXCEPTION'
//
// MUTATION 4 IS WHY THIS LIST IS WORTH KEEPING. On the first run it PASSED all
// 53 tests: both halves of each realistic pair are red-dominant, so the
// hue-dominance assertion could not see them exchanged, and the gate would have
// shipped believing it protected a relation it did not. The lightness assertion
// was added in response, and only then did the swap fail. A gate nobody has
// watched fail is a spell-check that is switched off.
