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
  ToolId,
} from '../types'
import type { SpecimenRecord } from '../../studio/types'
import { createBridge, SceneRoot, type SceneBridge } from './scene'
import { frameSpecimen, resolveAnchors, type DefaultView } from './anchors'
import { projectAnchor } from './project'
import { disposeTree, loadSpecimenMesh } from './load'
import { TextureBudget } from './textures'
import { TIER_RIGS } from './tiers'
import { isStandIn, resolveMeshUrl } from './standin'

/** Same seven the placeholder's viewport stage declares. `isolate`,
 * `cross-section` and `layers` are declared because the mesh renderer is the
 * renderer that will honour them (Stages 3–4); `invokeTool` ignores them for
 * now rather than the rail pretending they are missing. */
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

  /** Bumped per load so a specimen swapped mid-fetch cannot be overtaken by
   * its predecessor arriving late. */
  private loadToken = 0

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
    if (!root) return
    // Deferred for the reason above, and because React forbids unmounting a
    // root while another root is rendering — which is exactly where the
    // shell's effect cleanup calls us from.
    this.teardown = setTimeout(() => {
      this.teardown = null
      this.root = null
      this.rootContainer = null
      this.host = null
      this.releaseModel()
      this.bridge = createBridge()
      this.canvasReady = false
      this.rejectWaiters(new Error('renderer unmounted'))
      root.unmount()
      host?.remove()
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

    return projectAnchor(anchor, {
      camera,
      model: this.model,
      width,
      height,
      radius: this.view.radius,
    })
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
        this.resetView()
        break
      case 'auto-rotate':
        this.autoRotate = on ?? !this.autoRotate
        this.renderScene()
        break
      default:
        // rotate and zoom are the pointer's, always live; isolate,
        // cross-section and layers arrive at Stages 3–4.
        break
    }
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

    this.textureBudget.collect(scene)
    const rig = TIER_RIGS[this.tier]
    this.textureBudget.apply(rig.textureScale, rig.anisotropy)
  }

  private releaseModel(): void {
    if (this.disposeModel) this.disposeModel()
    else if (this.model) disposeTree(this.model)
    this.disposeModel = null
    this.model = null
    this.view = null
    this.anchors = new Map()
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
