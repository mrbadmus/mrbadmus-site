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
  /** 0–1 while state is 'loading', where the transport reports a total size.
   * Absent when the server sends no content-length (spec §4 caps a GLB at 3MB,
   * so a school connection can spend real seconds here). Added at Stage 2
   * (MRB-187): a renderer that fetches needs somewhere to say how far it has
   * got, and 'loading' alone cannot. */
  progress?: number
}

/** The live position of a stepped tool (MRB-188). */
export interface ToolState {
  /** false when the tool is honoured but currently doing nothing */
  active: boolean
  /** 1-based position, when the tool steps through a fixed set */
  step?: number
  steps?: number
  /** what is being shown, in the ASSET's own words — a declared node name, or
   * an index when the asset names nothing. Never invented. */
  label?: string
  /** where a continuous tool sits, 0–1. Only `cross-section` has one: its
   * position is dragged rather than stepped (MRB-189 acceptance). */
  offset?: number
}

export interface ScreenPoint {
  /** px from the container's left edge */
  x: number
  /** px from the container's top edge */
  y: number
  /** false when the hotspot is on the far side of the model (occluded) —
   * always true for flat/placeholder renderers */
  visible: boolean
  /** true when the dot is drawn over the cut face rather than over the
   * specimen's exterior: the cross-section removed the material that was in
   * front of this anchor, so what the dot sits on is the cap.
   *
   * The cut face is a LIGHT ground inside a dark stage, so a dot there flips
   * to the §07 paper variant (crosssection-v1.html §08: "Dots keep their one
   * meaning on the cut face; on that light ground they flip to the paper
   * variant from §07, dark outline and all"). Absent or false everywhere a
   * renderer has no cut — the flat renderer does not declare cross-section at
   * all. Added at MRB-189. */
  onCut?: boolean
}

/** Below this, the plane is being seen too nearly face-on for a rule through
 * it to be true, and the renderer draws none. `edgeOn` is |sin| of the angle
 * between the plane's normal and the view direction: 1 is exactly edge-on, 0
 * exactly face-on. 0.30 is about 17° off face-on; full strength by 0.55 (33°).
 *
 * Here rather than in `mesh/section.ts` because the shell fades the rule in
 * across this band and must not import anything that pulls Three.js with it
 * (gate 1). The geometry stays in the renderer; only the two numbers the two
 * halves must agree on live at the door. */
export const RULE_EDGE_ON_FLOOR = 0.3
export const RULE_EDGE_ON_FULL = 0.55

/** Where the shell should draw the accent rule that marks the cut plane
 * (MRB-189, §08 of `reference/crosssection-v1.html`).
 *
 * The rule is the ONLY place the accent lives in the cross-section treatment —
 * §08 takes it off the tissue entirely, because the plane is the interactive
 * thing and tissue is substance that never highlights itself. It is geometry,
 * so the renderer computes it; it is furniture, so the shell draws it. */
export interface SectionRule {
  /** the rule's midpoint, in container pixels */
  x: number
  y: number
  /** CSS rotation in degrees; 0 draws it vertical, as the reference does */
  angle: number
  /** how long to draw it across the specimen, in pixels, before the ticks */
  length: number
  /** 0–1, how edge-on the plane is seen. A plane is a LINE on screen only when
   * seen edge-on; face-on it covers the frame and has no position to mark, so
   * the shell fades the rule out as this falls and the renderer returns null
   * once it would be a fiction. */
  edgeOn: number
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

  /** Fire a tool the renderer declared in `supportedTools`. The declaration
   * side of that pair existed from Stage 1; this is the other half — the rail
   * draws from `supportedTools` and presses back through here, so a renderer
   * cannot advertise a tool the shell has no way to invoke.
   *
   * Toggle tools (`auto-rotate`) carry their desired state in `on`; momentary
   * tools (`reset`) ignore it. A renderer ignores any tool it did not declare.
   * Added at Stage 2 (MRB-187) — see the Linear comment for why the Stage 1
   * interface could not carry reset or auto-rotate without it. */
  invokeTool(tool: ToolId, on?: boolean): void

  /** Turn until a named hotspot is on screen, and animate the turn.
   *
   * The retrieval round asks the student to name a highlighted structure. With
   * honest occlusion (Stage 2), a target on the far side of the specimen is
   * highlighted with nothing visible — not a hard question, an unanswerable
   * one, and indistinguishable from the app being broken. So the round frames
   * its target before asking (ruling on MRB-191).
   *
   * Two things the implementation owes:
   *   · ANIMATE, don't cut. A camera that teleports between questions loses
   *     the student's orientation on the specimen, which is the thing the 3D
   *     view is for.
   *   · FRAME, don't zoom in. The surrounding structure is what makes the
   *     question answerable: same distance, different angle.
   *
   * Called when a question is PRESENTED, never continuously — a camera that
   * fought the student's hands would be worse than the problem. A renderer
   * with no camera does nothing. Added at Stage 6. */
  frameHotspot(hotspotId: string): void

  /** Drag the cross-section's plane along its axis, 0–1 across the specimen's
   * bounds. Ignored when the tool is not engaged, and by any renderer that
   * does not declare `cross-section`.
   *
   * Separate from `invokeTool` because this one is continuous: MRB-189's
   * acceptance is "plane drags smoothly, cut updates in real time", and a
   * press is not a drag. Added at Stage 4. */
  setSectionOffset(offset: number): void

  /** Where to draw the accent rule marking the cut plane, in container pixels,
   * or null when there is no cut engaged — or when the plane is being seen too
   * nearly face-on for a rule through it to be true. A renderer that does not
   * declare `cross-section` returns null always. Added at MRB-189. */
  sectionRule(): SectionRule | null

  /** Show only the structure a named hotspot sits on.
   *
   * The rail's isolate button steps blindly through the parts the asset
   * declares, because at that moment the shell has nothing in mind. The
   * callout's `Isolate` action (reference §01) does have something in mind —
   * the structure whose label is open — and there is no way to say that
   * through `invokeTool`. Added at Stage 3 (MRB-188).
   *
   * A renderer that cannot resolve the hotspot to a part leaves the view
   * alone; it never guesses at one. */
  isolateHotspot(hotspotId: string): void

  /** What a stepped tool is currently showing, so the shell can caption it.
   *
   * Added at Stage 3 (MRB-188). `isolate` and `layers` step through positions
   * the RENDERER knows about and the shell does not — how many parts the asset
   * declares, what they are called — and a control that steps silently is a
   * control a student cannot follow. Returns null for a tool this renderer
   * does not honour or that carries no state.
   *
   * `label` is always a string the ASSET declares, never one the studio wrote:
   * see the naming note at the head of `mesh/parts.ts`. */
  toolState(tool: ToolId): ToolState | null

  /** Subscribe to readiness/failure. Returns an unsubscribe function. The
   * current status is delivered immediately on subscribe. */
  onStatus(cb: (status: RendererStatus) => void): () => void
}
