// ─────────────────────────────────────────────────────────────────────────────
// The renderer interface — the only door between the shell and any 3D library.
//
// The shell NEVER imports Three.js (gate 1 enforces this mechanically). Two
// real implementations will exist: `mesh` (R3F/Three, Stage 2) and `flat`
// (SVG/PNG plate, full content parity). Stage 1 ships `placeholder`, which
// draws a soft grey form and returns fixed coordinates.
//
// This contract is what a renderer owes the shell — nothing more:
//   · mount into a container / unmount
//   · load a specimen
//   · resolve a hotspot id to a screen coordinate
//   · report readiness and failure
//   · declare which tools it supports and how the stage should be dressed
// ─────────────────────────────────────────────────────────────────────────────

import type { SpecimenRecord } from '../studio/types'

/** Every tool the shell knows how to draw. A renderer declares the subset it
 * honours; the rail renders from that declaration, never from a fixed list.
 * Absent means absent — not greyed out (reference §06: "a disabled tool is a
 * promise the device cannot keep"). */
export type ToolId =
  | 'rotate'
  | 'zoom'
  | 'isolate'
  | 'cross-section'
  | 'layers'
  | 'labels'
  | 'reset'
  | 'auto-rotate'

/** Render-quality tiers a renderer can be asked for. Tier D deliberately does
 * not appear here: D is the shell's capability floor (no WebGL2 ⇒ use the flat
 * renderer), not a quality a renderer can be set to. Ruling on MRB-186. */
export type RenderTier = 'A' | 'B' | 'C'

export interface RendererStatus {
  state: 'idle' | 'loading' | 'ready' | 'failed'
  /** Present when state is 'failed'. The shell reacts by switching renderer. */
  error?: string
}

export interface ScreenPoint {
  /** px from the container's left edge */
  x: number
  /** px from the container's top edge */
  y: number
  /** false when the hotspot is on the far side of the model (occluded) —
   * always true for flat/placeholder renderers */
  visible: boolean
}

export interface Renderer {
  /** Which stage dressing the shell should use: 'viewport' is the dark room,
   * 'paper' is the flat plate on light ground (reference §06). */
  readonly stage: 'viewport' | 'paper'

  /** Tools this renderer honours. The rail draws exactly these. */
  readonly supportedTools: readonly ToolId[]

  /** Whether render-quality tiers mean anything here. The flat renderer has no
   * render load, so the quality chip disappears entirely (§06: "no quality
   * chip … the control goes rather than showing a fifth state"). */
  readonly supportsQualityTiers: boolean

  /** Attach to a container element. Idempotent per instance; the shell calls
   * unmount before re-mounting elsewhere. */
  mount(container: HTMLElement): void

  unmount(): void

  /** Load a specimen's geometry (mesh path or fallback plate — the renderer
   * picks its own asset from the record). Resolves when drawable; rejects on
   * load failure, after which status is 'failed'. */
  loadSpecimen(specimen: SpecimenRecord): Promise<void>

  /** Resolve a hotspot id to container-relative pixels for the current camera.
   * Returns null for ids the renderer has no anchor for. */
  hotspotToScreen(hotspotId: string): ScreenPoint | null

  /** Apply a render-quality tier. Must take effect live — no reload, no
   * remount (gate 5 asserts this). No-op when supportsQualityTiers is false. */
  setTier(tier: RenderTier): void

  /** Subscribe to readiness/failure. Returns an unsubscribe function. The
   * current status is delivered immediately on subscribe. */
  onStatus(cb: (status: RendererStatus) => void): () => void
}
