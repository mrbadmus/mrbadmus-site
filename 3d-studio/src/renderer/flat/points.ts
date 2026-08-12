// Where a hotspot sits on the plate (MRB-190).
//
// The mirror of `mesh/anchors.ts`, and it answers the same question the same
// way. Content authors `position2d` at Stage 8; until then every value in
// heart.json is [0, 0], which taken literally is the plate's top-left corner —
// every dot stacked in one place, which is not a fallback, it is a bug wearing
// one. So an all-zero position reads as UNAUTHORED and gets a deterministic
// stand-in, exactly as the mesh renderer does.
//
// Authored coordinates win outright the moment they exist.

import type { HotspotRecord } from '../../studio/types'

/** The plate's own coordinate space. `position2d` is authored in these units,
 * so a diagram drawn at any size still places its dots correctly: the
 * renderer scales this space onto the stage, it does not scale the numbers. */
export const PLATE_WIDTH = 720
export const PLATE_HEIGHT = 560

export interface PlatePoint {
  /** fraction of the plate's width, 0–1 */
  fx: number
  /** fraction of the plate's height, 0–1 */
  fy: number
}

/** An all-zero position2d is the unauthored sentinel, not a genuine anchor at
 * the plate's corner. Same rule and same reasoning as `isAuthoredPosition` on
 * the mesh side; they are separate functions because they take different
 * shapes, not because the rule differs. */
export function isAuthoredPoint(p: readonly number[]): boolean {
  return p.length === 2 && p.some((v) => v !== 0)
}

const GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5))

/** Deterministic spread across the plate, in the hotspot's index.
 *
 * Duplicated in `tools/make_test_plate.py`, which draws the stand-in plate's
 * discs at these same points so the fixture's dots land on its forms. The two
 * cite each other; if they drift, dots sit off a grey disc on a fixture, which
 * is cosmetic and not worth a shared build step to prevent. */
export function standInPoint(index: number, count: number): PlatePoint {
  const radius = 0.3 * Math.sqrt((index + 0.5) / Math.max(count, 1))
  const angle = index * GOLDEN_ANGLE
  return {
    fx: 0.5 + radius * Math.cos(angle),
    fy: 0.48 + radius * Math.sin(angle),
  }
}

/** A point per hotspot id, as fractions of the plate.
 *
 * Every hotspot in the record gets one. That is the fallback-parity rule from
 * spec §10 stated in code: the flat renderer exposes the same hotspot ID set
 * as the mesh renderer, for every specimen, with only the coordinates authored
 * per view. */
export function resolvePlatePoints(
  hotspots: readonly HotspotRecord[],
): Map<string, PlatePoint> {
  const points = new Map<string, PlatePoint>()
  hotspots.forEach((hotspot, index) => {
    if (isAuthoredPoint(hotspot.position2d)) {
      points.set(hotspot.id, {
        fx: hotspot.position2d[0] / PLATE_WIDTH,
        fy: hotspot.position2d[1] / PLATE_HEIGHT,
      })
      return
    }
    points.set(hotspot.id, standInPoint(index, hotspots.length))
  })
  return points
}

/** Where the plate lands inside a container, preserving its aspect ratio.
 * Returned rather than done with CSS so the hotspot layer and the plate agree
 * on one rectangle — the binding defect spec §3.2 is written against is
 * exactly this kind of "two independent calculations of the same thing". */
export function plateRect(
  containerWidth: number,
  containerHeight: number,
  zoom = 1,
): { x: number; y: number; width: number; height: number } {
  // Margin so the plate never touches the stage edge: the rail overhangs the
  // left and the flat chip the top-right, same as on the viewport stage.
  const usableWidth = Math.max(containerWidth - 132, 40)
  const usableHeight = Math.max(containerHeight - 96, 40)
  const scale =
    Math.min(usableWidth / PLATE_WIDTH, usableHeight / PLATE_HEIGHT) * zoom
  const width = PLATE_WIDTH * scale
  const height = PLATE_HEIGHT * scale
  return {
    x: (containerWidth - width) / 2,
    y: (containerHeight - height) / 2,
    width,
    height,
  }
}
