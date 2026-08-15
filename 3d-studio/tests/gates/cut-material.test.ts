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
// order, both inheritance steps, and the fallback.
//
// THE HEART'S MAP IS NOW AUTHORED (MRB-222). It was deliberately left blank in
// MRB-217, and the reason was recorded here: every part in that assembly was a
// blood-volume cast, so an honest map would have marked all twelve `cavity` and
// the cut face would have read as pure void. That is no longer the assembly.
// The heart now carries `Ventricular myocardium` — real muscle, from
// BodyParts3D's isa tree — beside the four casts, so the specimen defaults to
// `wall` and only the four chambers declare `cavity`. There is finally a
// distinction on the specimen for the cut face to draw.

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

describe('gate 15 — the heart’s authored map (MRB-222)', () => {
  const heart = specimens.find((s) => s.id === 'heart')!
  const index = indexHotspots(heart.hotspots)

  /** The four blood-volume casts, and the ONLY parts that are cavity. Written
   * out rather than derived from the record, or this would assert the record
   * equals itself. */
  const CAVITIES = [
    'heart.right-atrium',
    'heart.right-ventricle',
    'heart.left-atrium',
    'heart.left-ventricle',
  ]

  it('the specimen defaults to wall — most of a heart is muscle', () => {
    expect((heart as { cutMaterial?: CutMaterial }).cutMaterial).toBe('wall')
  })

  it('exactly the four chambers declare cavity, and nothing else does', () => {
    const declared = heart.hotspots.filter((h) => h.cutMaterial)
    expect(declared.map((h) => h.id).sort()).toEqual([...CAVITIES].sort())
    for (const h of declared) expect(h.cutMaterial).toBe('cavity')
  })

  it('the four chambers cut as CAVITY regardless of nesting depth', () => {
    // The defect this whole mechanism exists for: a cast ventricle is a
    // top-level solid at depth 0, which the heuristic would paint as wall.
    for (const part of ['Right atrium', 'Right ventricle', 'Left atrium', 'Left ventricle']) {
      expect(resolveCutMaterial(part, heart, index)).toBe('cavity')
      expect(cutFaceColour(resolveCutMaterial(part, heart, index), 0)).toBe(CAVITY)
    }
  })

  it('every other part cuts as WALL, including the three with no hotspot', () => {
    // The myocardium and the two atrial walls are real GLB parts that the
    // record names no hotspot for. They inherit the specimen's default, which
    // is exactly the inheritance step this gate exists to protect.
    for (const part of [
      'Ventricular myocardium', 'Right atrial wall', 'Left atrial wall',
      'Aorta', 'Vena cava', 'Tricuspid valve', 'Coronary arteries',
    ]) {
      expect(resolveCutMaterial(part, heart, index)).toBe('wall')
      expect(cutFaceColour(resolveCutMaterial(part, heart, index), 0)).toBe(WALL)
    }
  })

  it('THE MYOCARDIUM IS NOT A CAVITY — the wall must read as solid', () => {
    // The single reading MRB-222 exists to produce. If the ventricular wall
    // ever cut as void, the cross-section would show the left ventricle's
    // 9.4mm of muscle as empty space and teach the opposite of the point.
    expect(resolveCutMaterial('Ventricular myocardium', heart, index)).toBe('wall')
    expect(resolveCutMaterial('Ventricular myocardium', heart, index)).not.toBe('cavity')
  })

  it('an unauthored specimen still falls all the way to the heuristic', () => {
    // Authoring the heart must not have switched the fallback off for anything
    // else. Asserted on a synthetic record, since the heart is now authored.
    const bare = specimen([hotspot('other.thing')])
    for (const depth of [0, 1, 5]) {
      expect(resolveCutMaterial('Thing', bare)).toBeNull()
      expect(cutFaceColour(resolveCutMaterial('Thing', bare), depth)).toBe(capColour(depth))
    }
  })
})
