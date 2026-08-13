// The mesh renderer (MRB-187) — React Three Fiber behind the imperative
// Renderer interface Stage 1 fixed.
//
// The shell hands this a container and a specimen record and gets back
// pixels, hotspot coordinates and a status stream. It never learns that
// Three.js exists: React lives inside this boundary too, in a root of its own
// mounted into the container, which is why `mount`/`unmount` can stay the
// plain imperative pair the interface promises.

import { createRoot, type Root } from 'react-dom/client'
import { createElement } from 'react'
import * as THREE from 'three'
import type {
  Renderer,
  RendererStatus,
  RenderTier,
  ScreenPoint,
  SectionRule,
  ToolId,
  ToolState,
} from '../types'
import type { SpecimenRecord } from '../../studio/types'
import { createBridge, SceneRoot, type SceneBridge } from './scene'
import { frameSpecimen, resolveAnchors, type DefaultView } from './anchors'
import { projectAnchor } from './project'
import { disposeTree, loadSpecimenMesh } from './load'
import { TextureBudget } from './textures'
import { TIER_RIGS } from './tiers'
import { isStandIn, resolveMeshUrl } from './standin'
import {
  FRAME_DURATION_MS,
  framePosition,
  frameStep,
  needsFraming,
} from './framing'
import {
  isClipped,
  sectionConstant,
  sectionPlane,
  sectionRule,
  SECTION_REST,
  type SectionState,
} from './section'
import {
  applyView,
  collectParts,
  isShown,
  layerCount,
  partAt,
  partLabel,
  stepIsolate,
  stepLayers,
  WHOLE_SPECIMEN,
  type PartView,
  type SpecimenPart,
} from './parts'

/** Same seven the placeholder's viewport stage declares. `cross-section` is
 * declared because the mesh renderer is the one that will honour it (Stage 4);
 * `invokeTool` ignores it for now rather than the rail pretending it is
 * missing. `isolate` and `layers` became real at Stage 3 (MRB-188). */
const MESH_TOOLS: readonly ToolId[] = [
  'rotate',
  'zoom',
  'isolate',
  'cross-section',
  'layers',
  'reset',
  'auto-rotate',
]

class MeshRenderer implements Renderer {
  readonly stage = 'viewport' as const
  readonly supportedTools = MESH_TOOLS
  readonly supportsQualityTiers = true

  private container: HTMLElement | null = null
  private root: Root | null = null
  /** the shell container the React root's host sits in; outlives a scheduled
   * teardown */
  private rootContainer: HTMLElement | null = null
  /** the element React owns — ours, not the shell's */
  private host: HTMLDivElement | null = null
  private teardown: ReturnType<typeof setTimeout> | null = null
  /** bumped on every fresh mount, so a deferred teardown can tell whether the
   * instance state is still the one it was scheduled for */
  private generation = 0
  private bridge: SceneBridge = createBridge()

  private status: RendererStatus = { state: 'idle' }
  private listeners = new Set<(s: RendererStatus) => void>()

  private tier: RenderTier = 'A'
  private autoRotate = false

  private model: THREE.Object3D | null = null
  private view: DefaultView | null = null
  private anchors = new Map<string, THREE.Vector3>()
  private disposeModel: (() => void) | null = null
  private textureBudget = new TextureBudget()

  /** the parts the loaded asset declares, and which of them are drawn */
  private parts: SpecimenPart[] = []
  private partView: PartView = WHOLE_SPECIMEN
  /** hotspot id → the part its anchor sits on, resolved geometrically */
  private anchorParts = new Map<string, SpecimenPart>()

  /** cross-section (MRB-189). The plane is ONE object for the specimen's
   * lifetime and is mutated as the cut is dragged: every clipped material
   * holds a reference to it, so a drag costs no material recompile. `version`
   * is what tells React that something inside it moved. */
  private section: SectionState = SECTION_REST
  private plane: THREE.Plane | null = null
  private box: THREE.Box3 | null = null
  private sceneVersion = 0

  /** Bumped per load so a specimen swapped mid-fetch cannot be overtaken by
   * its predecessor arriving late. */
  private loadToken = 0

  /** the in-flight framing move (MRB-191), if any */
  private frameMove: {
    from: THREE.Vector3
    to: THREE.Vector3
    target: THREE.Vector3
    started: number
    raf: number
  } | null = null

  private canvasReady = false
  private canvasWaiters: Array<{ resolve: () => void; reject: (e: Error) => void }> = []

  mount(container: HTMLElement): void {
    // React StrictMode mounts, unmounts and remounts every effect in
    // development. Throwing away a WebGL context and a React root on that
    // rehearsal — then building both again — is waste at best, and at worst
    // two roots fighting over one container. So unmount SCHEDULES the
    // teardown and a remount of the same container cancels it.
    if (this.teardown !== null && this.rootContainer === container && this.host?.isConnected) {
      clearTimeout(this.teardown)
      this.teardown = null
      this.container = container
      this.stamp()
      this.renderScene()
      return
    }

    // React renders into a host of our own, never straight into the shell's
    // container. Unmounting a React root clears its container's children, and
    // on the failure route the flat renderer has already drawn into that
    // container by the time our teardown runs — this keeps the two from
    // wiping each other.
    const host = document.createElement('div')
    host.className = 'mesh-host'
    host.style.position = 'absolute'
    host.style.inset = '0'
    container.appendChild(host)

    this.generation += 1
    this.container = container
    this.rootContainer = container
    this.host = host
    this.stamp()
    this.root = createRoot(host)
    this.renderScene()
  }

  unmount(): void {
    const container = this.container
    this.container = null
    if (container) {
      delete container.dataset.renderer
      delete container.dataset.tier
      delete container.dataset.state
      delete container.dataset.progress
      delete container.dataset.specimenSource
    }

    const root = this.root
    const host = this.host
    // Already on its way out: one teardown is enough.
    if (!root || this.teardown !== null) return
    // Deferred for the reason above, and because React forbids unmounting a
    // root while another root is rendering — which is exactly where the
    // shell's effect cleanup calls us from.
    const generation = this.generation
    this.teardown = setTimeout(() => {
      this.teardown = null
      root.unmount()
      host?.remove()
      // The shell may have re-mounted us into a DIFFERENT container in the
      // meantime — switching mode remounts the stage — in which case this
      // teardown owns the root it just disposed of and nothing else. Touching
      // the instance state here would wipe the live mount's model, anchors and
      // canvas out from under it.
      if (this.generation !== generation) return
      this.root = null
      this.rootContainer = null
      this.host = null
      this.releaseModel()
      this.bridge = createBridge()
      this.canvasReady = false
      this.rejectWaiters(new Error('renderer unmounted'))
    }, 0)
  }

  async loadSpecimen(specimen: SpecimenRecord): Promise<void> {
    const token = ++this.loadToken
    this.releaseModel()
    this.renderScene()
    this.setStatus({ state: 'loading' })

    const url = resolveMeshUrl(specimen)

    try {
      const result = await loadSpecimenMesh(url, (fraction) => {
        if (token !== this.loadToken) return
        this.setStatus({ state: 'loading', progress: fraction })
      })

      if (token !== this.loadToken) {
        result.dispose()
        return
      }

      this.adopt(result.scene, specimen)
      this.disposeModel = result.dispose
      this.renderScene()

      // "Drawable" means the canvas exists too, not merely that bytes
      // arrived — the interface promises the load resolves when the shell can
      // start asking for hotspot coordinates.
      await this.whenCanvasReady()
      if (token !== this.loadToken) return

      this.setStatus({ state: 'ready' })
    } catch (error) {
      if (token !== this.loadToken) return
      const message = error instanceof Error ? error.message : String(error)
      this.setStatus({ state: 'failed', error: message })
      throw error instanceof Error ? error : new Error(message)
    }
  }

  hotspotToScreen(hotspotId: string): ScreenPoint | null {
    const anchor = this.anchors.get(hotspotId)
    const { camera } = this.bridge
    if (!anchor || !camera || !this.model || !this.view || !this.container) return null

    const width = this.container.clientWidth || this.bridge.width
    const height = this.container.clientHeight || this.bridge.height
    if (!width || !height) return null

    const clip = this.activePlane()

    // A label on material that is no longer on the stage is a label pointing
    // at nothing — whether isolate and layers took the part away (MRB-188) or
    // the cross-section cut the anchor's own half off (MRB-189). The anchor
    // keeps its coordinate; the shell decides what to do with an invisible
    // dot.
    const part = this.anchorParts.get(hotspotId)
    const gone = (part && !isShown(part.object, this.model)) || isClipped(anchor, clip)

    const point = projectAnchor(anchor, {
      camera,
      model: this.model,
      width,
      height,
      radius: this.view.radius,
      clip,
    })
    return gone ? { x: point.x, y: point.y, visible: false } : point
  }

  /** The clipping plane in force right now, or null. */
  private activePlane(): THREE.Plane | null {
    return this.section.enabled ? this.plane : null
  }

  setTier(tier: RenderTier): void {
    if (this.tier === tier) return
    this.tier = tier
    if (this.container) this.container.dataset.tier = tier
    const rig = TIER_RIGS[tier]
    this.textureBudget.apply(rig.textureScale, rig.anisotropy)
    this.renderScene()
  }

  invokeTool(tool: ToolId, on?: boolean): void {
    if (!this.supportedTools.includes(tool)) return
    switch (tool) {
      case 'reset':
        this.cancelFraming()
        this.resetView()
        // Reset means the view a student came in on, which includes the form
        // being whole. Leaving a structure isolated, or the specimen cut in
        // half, behind a pressed Reset is the kind of half-restored state that
        // reads as a broken control.
        this.setPartView(WHOLE_SPECIMEN)
        this.setSection(SECTION_REST)
        break
      case 'auto-rotate':
        this.autoRotate = on ?? !this.autoRotate
        this.renderScene()
        break
      case 'isolate':
        this.setPartView(stepIsolate(this.partView, this.parts))
        break
      case 'layers':
        this.setPartView(stepLayers(this.partView, this.parts))
        break
      case 'cross-section':
        this.setSection({
          enabled: on ?? !this.section.enabled,
          offset: this.section.offset,
        })
        break
      default:
        // rotate and zoom are the pointer's, always live.
        break
    }
  }

  setSectionOffset(offset: number): void {
    if (!this.section.enabled) return
    this.setSection({ enabled: true, offset })
  }

  sectionRule(): SectionRule | null {
    const plane = this.activePlane()
    const { camera } = this.bridge
    if (!plane || !camera || !this.box || !this.container) return null
    const width = this.container.clientWidth || this.bridge.width
    const height = this.container.clientHeight || this.bridge.height
    return sectionRule(plane, this.box, camera, width, height)
  }

  frameHotspot(hotspotId: string): void {
    const anchor = this.anchors.get(hotspotId)
    const { controls, camera } = this.bridge
    if (!anchor || !controls || !camera) return

    const target = controls.target.clone()
    const from = camera.position.clone()
    if (!needsFraming(anchor, target, from)) {
      this.cancelFraming()
      return
    }
    const to = framePosition(anchor, target, from)
    if (!to) return

    // Auto-rotate would fight the move and then carry the camera straight back
    // off the target; a student who asked for it can switch it on again.
    if (this.autoRotate) this.invokeTool('auto-rotate', false)

    this.cancelFraming()
    this.frameMove = {
      from,
      to,
      target,
      started: performance.now(),
      raf: requestAnimationFrame(() => this.stepFraming()),
    }
  }

  private stepFraming(): void {
    const move = this.frameMove
    const { controls, camera } = this.bridge
    if (!move || !controls || !camera) return

    const t = (performance.now() - move.started) / FRAME_DURATION_MS
    camera.position.copy(frameStep(move.from, move.to, move.target, Math.min(t, 1)))
    controls.target.copy(move.target)
    controls.update()

    if (t >= 1) {
      this.frameMove = null
      return
    }
    move.raf = requestAnimationFrame(() => this.stepFraming())
  }

  /** Stop mid-turn and leave the camera where it is. The student's hands win:
   * the ruling is explicit that framing happens when a question is presented,
   * not continuously. */
  private cancelFraming(): void {
    if (!this.frameMove) return
    cancelAnimationFrame(this.frameMove.raf)
    this.frameMove = null
  }

  isolateHotspot(hotspotId: string): void {
    const part = this.anchorParts.get(hotspotId)
    if (!part) return
    const index = this.parts.indexOf(part)
    if (index === -1) return
    // Pressing it again on the same structure puts the specimen back, so the
    // callout's action is its own way out.
    const already = this.partView.isolated === index
    this.setPartView({ isolated: already ? null : index, peeled: 0 })
  }

  toolState(tool: ToolId): ToolState | null {
    if (tool === 'isolate') {
      if (this.parts.length < 2) return { active: false }
      const index = this.partView.isolated
      if (index === null) return { active: false, steps: this.parts.length }
      return {
        active: true,
        step: index + 1,
        steps: this.parts.length,
        label: partLabel(this.parts[index]),
      }
    }
    if (tool === 'layers') {
      const levels = layerCount(this.parts)
      if (levels < 2) return { active: false }
      if (this.partView.peeled === 0) return { active: false, steps: levels }
      return { active: true, step: this.partView.peeled + 1, steps: levels }
    }
    if (tool === 'cross-section') {
      if (!this.plane) return { active: false }
      return { active: this.section.enabled, offset: this.section.offset }
    }
    return null
  }

  onStatus(cb: (status: RendererStatus) => void): () => void {
    this.listeners.add(cb)
    cb(this.status)
    return () => this.listeners.delete(cb)
  }

  // ── internals ──────────────────────────────────────────────────────────

  /** What the stage container says about itself, for the shell's CSS hooks
   * and for the browser-driven gates, which wait on `data-state` rather than
   * on a sleep. */
  private stamp(): void {
    const container = this.container
    if (!container) return
    container.dataset.renderer = 'mesh'
    container.dataset.tier = this.tier
    container.dataset.state = this.status.state
    if (isStandIn()) container.dataset.specimenSource = 'test-mesh'
  }

  /** Return the camera to the authored default view, exactly. OrbitControls'
   * own `reset()` restores the state saved when the specimen was framed, so
   * the returned view is the same floating-point values every time; damping
   * is suspended across the call so a half-decayed drag cannot carry the
   * camera a few thousandths past it on the next frame. */
  private resetView(): void {
    const { controls, camera } = this.bridge
    const view = this.view
    if (!controls || !camera || !view) return

    const damping = controls.enableDamping
    controls.enableDamping = false
    controls.reset()
    camera.position.copy(view.position)
    controls.target.copy(view.target)
    controls.update()
    controls.enableDamping = damping
  }

  /** Change which parts are drawn and stamp it where the browser gate can
   * read it. No re-render: part visibility lives on the scene graph objects
   * R3F already has mounted, so R3F's own frame loop picks it up. */
  private setPartView(next: PartView): void {
    this.partView = next
    applyView(this.parts, next)
    this.stampParts()
    // The cap has to hear about it: a part that has left the stage must not
    // leave its cut face behind (MRB-189).
    this.sceneVersion += 1
    this.renderScene()
  }

  /** Engage, move or release the cut. The plane object is mutated rather than
   * replaced, so a drag never touches a material — see the note on `plane`. */
  private setSection(next: SectionState): void {
    this.section = next
    if (this.plane && this.box) {
      this.plane.constant = sectionConstant(this.box, next.offset)
    }
    this.sceneVersion += 1
    this.stampSection()
    this.renderScene()
  }

  private stampSection(): void {
    const container = this.container
    if (!container) return
    if (this.section.enabled) {
      container.dataset.section = String(Math.round(this.section.offset * 100))
      container.dataset.sectionCapped = String(this.capsAvailable())
    } else {
      delete container.dataset.section
      delete container.dataset.sectionCapped
    }
  }

  /** Whether the cut is capped at the current tier.
   *
   * MRB-189 anticipated the stencil pass being too much for Tier C and named
   * the fallback: an uncapped clip with a clear visual treatment, never the
   * tool switched off. It is capped at every tier today — the pass is two
   * extra colour-write-off draws per mesh and it measured no differently on
   * the software renderer — so this is one named place to change rather than
   * a decision spread through the scene. */
  private capsAvailable(): boolean {
    return true
  }

  private stampParts(): void {
    const container = this.container
    if (!container) return
    const isolate = this.toolState('isolate')
    const layers = this.toolState('layers')
    container.dataset.isolate =
      isolate?.active && isolate.label ? isolate.label : 'off'
    container.dataset.layer = layers?.active ? String(layers.step) : 'off'
    container.dataset.partsShown = String(
      this.parts.filter((p) => p.object.visible).length,
    )
  }

  private adopt(scene: THREE.Group, specimen: SpecimenRecord): void {
    scene.traverse((node) => {
      const mesh = node as THREE.Mesh
      if (!mesh.isMesh) return
      mesh.castShadow = true
      mesh.receiveShadow = true
    })

    const aspect =
      this.container && this.container.clientHeight > 0
        ? this.container.clientWidth / this.container.clientHeight
        : 16 / 9

    this.model = scene
    this.bridge.model = scene
    this.view = frameSpecimen(scene, aspect)
    this.anchors = resolveAnchors(specimen.hotspots, scene, this.view)

    // The parts the asset declares, and which part each anchor sits on — both
    // read off the geometry, so neither needs a binding authored in content
    // and both stay right when Stage 8 authors real coordinates (MRB-188).
    this.parts = collectParts(scene)
    this.anchorParts = new Map()
    for (const [id, anchor] of this.anchors) {
      const part = partAt(anchor, this.parts)
      if (part) this.anchorParts.set(id, part)
    }
    this.box = new THREE.Box3().setFromObject(scene)
    this.plane = sectionPlane(this.box, SECTION_REST.offset)
    this.section = SECTION_REST
    this.setPartView(WHOLE_SPECIMEN)

    this.textureBudget.collect(scene)
    const rig = TIER_RIGS[this.tier]
    this.textureBudget.apply(rig.textureScale, rig.anisotropy)
  }

  private releaseModel(): void {
    this.cancelFraming()
    if (this.disposeModel) this.disposeModel()
    else if (this.model) disposeTree(this.model)
    this.disposeModel = null
    this.model = null
    this.view = null
    this.anchors = new Map()
    this.parts = []
    this.anchorParts = new Map()
    this.partView = WHOLE_SPECIMEN
    this.section = SECTION_REST
    this.plane = null
    this.box = null
    this.bridge.model = null
    this.bridge.view = null
    this.textureBudget.clear()
  }

  private renderScene(): void {
    if (!this.root) return
    this.root.render(
      createElement(SceneRoot, {
        bridge: this.bridge,
        model: this.model,
        view: this.view,
        tier: this.tier,
        autoRotate: this.autoRotate,
        section:
          this.section.enabled && this.plane && this.box
            ? {
                plane: this.plane,
                box: this.box,
                parts: this.parts,
                version: this.sceneVersion,
                capped: this.capsAvailable(),
                isDrawn: (object: THREE.Object3D) =>
                  !this.model || isShown(object, this.model),
              }
            : null,
        onCreated: () => this.onCanvasReady(),
        onFailure: (message: string) => this.fail(message),
      }),
    )
  }

  private onCanvasReady(): void {
    this.canvasReady = true
    const waiters = this.canvasWaiters
    this.canvasWaiters = []
    waiters.forEach((w) => w.resolve())
  }

  private whenCanvasReady(): Promise<void> {
    if (this.canvasReady) return Promise.resolve()
    if (this.status.state === 'failed') {
      return Promise.reject(new Error(this.status.error || 'renderer failed'))
    }
    return new Promise<void>((resolve, reject) => {
      this.canvasWaiters.push({ resolve, reject })
    })
  }

  private rejectWaiters(error: Error): void {
    const waiters = this.canvasWaiters
    this.canvasWaiters = []
    waiters.forEach((w) => w.reject(error))
  }

  /** Anything that makes the scene unusable — context lost, canvas refused —
   * is reported as a failure so the shell can route to the flat renderer. */
  private fail(message: string): void {
    this.rejectWaiters(new Error(message))
    if (this.status.state === 'failed') return
    this.setStatus({ state: 'failed', error: message })
  }

  private setStatus(status: RendererStatus): void {
    this.status = status
    if (this.container) {
      this.container.dataset.state = status.state
      if (status.progress === undefined) delete this.container.dataset.progress
      else this.container.dataset.progress = String(Math.round(status.progress * 100))
    }
    this.listeners.forEach((cb) => cb(status))
  }
}

export function createMeshRenderer(): Renderer {
  return new MeshRenderer()
}
