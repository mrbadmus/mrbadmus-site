// Framing the specimen in the part of the stage a student can actually see.
//
// THE DEFECT. On phone the §05 sheet is drawn OVER the lower part of the stage
// — 55% of it at rest, all but 150px raised — but the camera framed the
// specimen against the geometric centre of the canvas, because that is what a
// camera does. So the specimen sat half behind the sheet, and worse: a
// retrieval target that `framePosition` had just turned to face the camera
// could end up underneath it. That does not make the question hard, it makes
// it unanswerable, and it is indistinguishable from the app being broken.
//
// THE FIX IS PROJECTION ONLY, and that is the load-bearing decision here.
//
// Moving the camera, or the orbit target, or the fit distance would all frame
// the specimen correctly and all be wrong:
//
//   * `reset` must return the camera to the authored default view EXACTLY —
//     the same floating-point values every time (MRB-187 acceptance, and the
//     note on `resetView` in index.ts). Anything that recomputed the default
//     view per detent would make "exactly" mean "exactly, for the detent you
//     happen to be at".
//   * `framePosition`'s contract is that the camera ends a turn exactly as far
//     from the specimen as it started — frame, never zoom in. A fit distance
//     that changed with the sheet would break that silently.
//   * a detent change would YANK THE CAMERA away from wherever the student had
//     rotated it to, which is a worse bug than the one being fixed.
//
// An off-axis projection has none of those problems. `camera.position`,
// `controls.target` and the saved reset state are never touched; only the
// frustum the projection matrix describes moves. Everything downstream —
// `hotspotToScreen`, the occlusion raycast, the section rule — reads the
// camera's projection, so all of them follow for free and stay consistent with
// what is on the glass.
//
// Desktop and tablet have no sheet, so they take no offset at all: the
// function returns null and the renderer calls `clearViewOffset()`, which
// leaves the projection byte-for-byte the one that shipped.

import type { StageInsets } from '../types'

export type { StageInsets }

/** The arguments to `PerspectiveCamera.setViewOffset`, in its own order. */
export interface ViewOffset {
  fullWidth: number
  fullHeight: number
  offsetX: number
  offsetY: number
  width: number
  height: number
}

/** Never frame into less than this much stage, however far the furniture
 * reaches. The raised detent leaves 150px so this is not reached in practice;
 * it exists so a bad inset degrades to a squeezed view rather than to a
 * divide-by-zero. */
const MIN_VISIBLE_PX = 24

/**
 * The off-axis projection that frames the specimen inside the unobscured band,
 * or null when none is needed.
 *
 * Two properties, and the whole derivation is these two:
 *
 *   1. CENTRED IN THE BAND. The camera's optical axis — where the orbit target
 *      sits, and therefore the specimen — lands at the middle of the visible
 *      strip rather than the middle of the canvas.
 *   2. FITTED TO THE BAND. The specimen fills the same fraction of the band's
 *      binding axis that it filled of the canvas's binding axis. `frameSpecimen`
 *      fits the bounding sphere to `min(width, height)` with a margin; this
 *      re-fits it to `min(width, visible)` by the ratio between them, which is
 *      why the scale is that ratio and nothing more elaborate.
 *
 * The mechanism is `setViewOffset`'s sub-window. Because `width`/`height` are
 * passed through unchanged, one virtual pixel is one canvas pixel and the
 * mapping is a pure translate: a point at the virtual image's centre lands at
 * canvas `(fullWidth/2 - offsetX, fullHeight/2 - offsetY)`. Solving that for
 * `(width/2, visible/2)` gives the two offsets below.
 */
export function stageViewOffset(
  width: number,
  height: number,
  insets: StageInsets,
): ViewOffset | null {
  if (!(width > 0) || !(height > 0)) return null
  const covered = Math.min(Math.max(insets.bottom, 0), height - MIN_VISIBLE_PX)
  if (covered <= 0) return null

  const visible = height - covered
  const scale = Math.min(width, visible) / Math.min(width, height)

  return {
    fullWidth: width * scale,
    fullHeight: height * scale,
    offsetX: (width * (scale - 1)) / 2,
    offsetY: (height * scale) / 2 - visible / 2,
    width,
    height,
  }
}

/** Where a point on the camera's optical axis lands, in container pixels,
 * under this offset. The orbit target is on the axis, so this is where the
 * specimen is centred — which is the thing worth asserting. */
export function axisPoint(
  offset: ViewOffset | null,
  width: number,
  height: number,
): { x: number; y: number } {
  if (!offset) return { x: width / 2, y: height / 2 }
  return {
    x: offset.fullWidth / 2 - offset.offsetX,
    y: offset.fullHeight / 2 - offset.offsetY,
  }
}

/** How much larger or smaller everything is drawn under this offset. 1 is
 * unchanged; below 1 the specimen is drawn smaller, which is what fitting it
 * into a shorter band means. */
export function magnification(offset: ViewOffset | null): number {
  return offset ? offset.fullWidth / offset.width : 1
}
