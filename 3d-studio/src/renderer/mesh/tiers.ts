// What a render tier actually costs, in one table (spec §5).
//
// Tier A  full: shadow maps, a local image-based light, screen-space ambient
//         occlusion, a contact shadow under the specimen, full-size textures.
// Tier B  shadows off, post-processing off, textures at half, lower pixel
//         ratio. Same three-light key/fill/rim rig, so the form still reads.
// Tier C  simplified lighting (ambient + one key), aggressive texture
//         downscale, pixel ratio pinned to 1.
//
// Every field here is applied live by the scene — nothing is a Canvas prop
// that would need a remount to change (gate 5).

import type { RenderTier } from '../types'

export type LightRig = 'full' | 'reduced' | 'simple'

export interface TierRig {
  /** upper bound on devicePixelRatio; the real ratio is min(dpr, this) */
  maxPixelRatio: number
  /** shadow maps on the key light */
  shadows: boolean
  shadowMapSize: number
  /** drei ContactShadows under the specimen */
  contactShadow: boolean
  /** screen-space ambient occlusion — the only post-processing pass we run */
  ambientOcclusion: boolean
  /** local RoomEnvironment IBL (no network: generated in-process) */
  environment: boolean
  lights: LightRig
  /** longest texture edge as a fraction of the source; 1 leaves it alone */
  textureScale: number
  anisotropy: number
}

export const TIER_RIGS: Record<RenderTier, TierRig> = {
  A: {
    maxPixelRatio: 2,
    shadows: true,
    shadowMapSize: 2048,
    contactShadow: true,
    ambientOcclusion: true,
    environment: true,
    lights: 'full',
    textureScale: 1,
    anisotropy: 4,
  },
  B: {
    maxPixelRatio: 1.5,
    shadows: false,
    shadowMapSize: 1024,
    contactShadow: false,
    ambientOcclusion: false,
    environment: false,
    lights: 'reduced',
    textureScale: 0.5,
    anisotropy: 2,
  },
  C: {
    maxPixelRatio: 1,
    shadows: false,
    shadowMapSize: 512,
    contactShadow: false,
    ambientOcclusion: false,
    environment: false,
    lights: 'simple',
    textureScale: 0.25,
    anisotropy: 1,
  },
}
