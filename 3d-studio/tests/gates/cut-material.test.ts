// @vitest-environment node
// Gate 15 — the cut face's material can be AUTHORED (MRB-217).
//
// `capColour(depth)` decides the cut face geometrically: outermost is wall,
// anything nested inside it is cavity. Correct for a solid specimen, and it
// inverts on the acquired heart — BodyParts3D models chambers as blood-volume
// CASTS with no myocardium shell, so a ventricle is a top-level solid, comes
// out at depth 0, and is painted as wall. The one thing on the specimen that is
// unambiguously a cavity reads as the most solid thing there.
//
// The information is not in the geometry, so the fix is authoring, and the
// heuristic stays for everything unauthored. This file asserts the resolution
// order, both inheritance steps, and the fallback — and that the fallback is
// what the heart still gets today, because its map is deliberately NOT authored
// in this run: every part in the current assembly is a cast, so an honest map
// would mark all twelve cavity and the cut face would read as pure void.
// Authoring against geometry that is being replaced is wasted work.

import { describe, expect, it } from 'vitest'
import { capColour, cutFaceColour } from '../../src/renderer/mesh/cap'
import {
  hotspotIdForPart,
  indexHotspots,
  resolveCutMaterial,
  slugify,
} from '../../src/renderer/mesh/cutmaterial'
import { specimens } from '../../src/studio/content'
import type { CutMaterial, HotspotRecord, SpecimenRecord } from '../../src/studio/types'

const WALL = '#F0E9DC'
const CAVITY = '#141109'

function hotspot(id: string, cutMaterial?: CutMaterial): HotspotRecord {
  return {
    id,
    label: id,
    detail: 'x',
    position3d: [0, 0, 0],
    position2d: [0, 0],
    tiers: ['foundation'],
    retrievable: true,
    ...(cutMaterial ? { cutMaterial } : {}),
  } as HotspotRecord
}

function specimen(
  hotspots: HotspotRecord[],
  cutMaterial?: CutMaterial,
): Pick<SpecimenRecord, 'id' | 'hotspots'> & { cutMaterial?: CutMaterial } {
  return { id: 'heart', hotspots, ...(cutMaterial ? { cutMaterial } : {}) }
}

describe('gate 15 — the binding is the one that already exists', () => {
  it('slugify matches the rule the recipe and the validator record', () => {
    expect(slugify('Right atrium')).toBe('right-atrium')
    expect(slugify('Left ventricle')).toBe('left-ventricle')
    expect(slugify('Sino-atrial node')).toBe('sino-atrial-node')
    expect(slugify('  Vena  cava  ')).toBe('vena-cava')
    expect(slugify('Semilunar valves')).toBe('semilunar-valves')
  })

  it('a part name resolves to a hotspot id in the specimen’s namespace', () => {
    expect(hotspotIdForPart('heart', 'Right atrium')).toBe('heart.right-atrium')
  })

  it('every part name in the heart recipe hits a real hotspot id', () => {
    // The join is only worth building on if it actually joins. These are the
    // twelve parts tools/recipes/heart.recipe.json declares.
    const parts = [
      'Right atrium', 'Right ventricle', 'Left atrium', 'Left ventricle',
      'Tricuspid valve', 'Bicuspid valve', 'Semilunar valves', 'Aorta',
      'Vena cava', 'Pulmonary artery', 'Pulmonary vein', 'Coronary arteries',
    ]
    const heart = specimens.find((s) => s.id === 'heart')!
    const ids = new Set(heart.hotspots.map((h) => h.id))
    for (const part of parts) {
      expect(ids.has(hotspotIdForPart('heart', part))).toBe(true)
    }
  })
})

describe('gate 15 — resolution order', () => {
  it('1. the hotspot’s own declaration wins over the specimen’s', () => {
    const record = specimen([hotspot('heart.left-ventricle', 'cavity')], 'wall')
    expect(resolveCutMaterial('Left ventricle', record)).toBe('cavity')
  })

  it('2. a silent hotspot inherits the specimen’s', () => {
    const record = specimen([hotspot('heart.left-ventricle')], 'wall')
    expect(resolveCutMaterial('Left ventricle', record)).toBe('wall')
  })

  it('3. neither declared resolves to null — the heuristic decides', () => {
    const record = specimen([hotspot('heart.left-ventricle')])
    expect(resolveCutMaterial('Left ventricle', record)).toBeNull()
  })

  it('a part with NO matching hotspot falls through silently, not to an error', () => {
    const record = specimen([hotspot('heart.left-ventricle', 'cavity')])
    expect(resolveCutMaterial('Some unnamed shell', record)).toBeNull()
  })

  it('a part with no matching hotspot still takes the specimen default', () => {
    const record = specimen([hotspot('heart.left-ventricle')], 'cavity')
    expect(resolveCutMaterial('Some unnamed shell', record)).toBe('cavity')
  })

  it('a nameless part is not a lookup failure, it is no lookup at all', () => {
    expect(resolveCutMaterial('', specimen([], 'wall'))).toBe('wall')
    expect(resolveCutMaterial('', specimen([]))).toBeNull()
  })

  it('the indexed and unindexed paths agree', () => {
    const hotspots = [hotspot('heart.left-ventricle', 'cavity'), hotspot('heart.aorta')]
    const record = specimen(hotspots, 'wall')
    const index = indexHotspots(hotspots)
    for (const part of ['Left ventricle', 'Aorta', 'Nothing at all']) {
      expect(resolveCutMaterial(part, record, index)).toBe(
        resolveCutMaterial(part, record),
      )
    }
  })
})

describe('gate 15 — what gets painted', () => {
  it('authored material picks its colour regardless of depth', () => {
    // The whole point: a cast ventricle sits at depth 0 and must still be void.
    expect(cutFaceColour('cavity', 0)).toBe(CAVITY)
    expect(cutFaceColour('wall', 3)).toBe(WALL)
  })

  it('unauthored falls back to the depth heuristic, unchanged', () => {
    for (const depth of [0, 1, 2, 7, 99]) {
      expect(cutFaceColour(null, depth)).toBe(capColour(depth))
    }
  })

  it('the two materials are the two values §08 ruled, not a new palette', () => {
    expect(cutFaceColour('wall', 0)).toBe(capColour(0))
    expect(cutFaceColour('cavity', 0)).toBe(capColour(1))
  })
})

describe('gate 15 — the heart is deliberately UNAUTHORED in this run', () => {
  const heart = specimens.find((s) => s.id === 'heart')!

  it('declares no specimen-level cutMaterial', () => {
    expect((heart as { cutMaterial?: CutMaterial }).cutMaterial).toBeUndefined()
  })

  it('declares no hotspot-level cutMaterial', () => {
    expect(heart.hotspots.filter((h) => h.cutMaterial).map((h) => h.id)).toEqual([])
  })

  it('so every part still resolves to the heuristic — no behaviour changed', () => {
    for (const part of ['Right atrium', 'Left ventricle', 'Aorta', 'Septum']) {
      expect(resolveCutMaterial(part, heart)).toBeNull()
    }
  })
})
