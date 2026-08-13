// The flat renderer (MRB-190, Stage 5).
//
// A SECOND RENDERER, not a degraded error state. It consumes the same specimen
// record, exposes the same hotspot ids, drives the same panel and — once Stage
// 6 lands — runs the same retrieval round. A student on a locked-down school
// machine gets the same content and the same points as one on a gaming laptop.
// Only the coordinates are authored per view (reference §06: "SHARED").
//
// Plain DOM and one <img>. No Three.js, no React, no canvas: the whole reason
// this renderer exists is that some devices cannot run any of that, and the
// code split at this stage means a Tier D device never downloads it either.
//
// What the rail loses is what a plate genuinely cannot do — rotate,
// cross-section, layers, auto-rotate are ABSENT, not greyed (reference §06:
// "a disabled tool is a promise the device cannot keep"). Labels earns its
// slot here because it is the only way to clear a busy plate.

import type {
  Renderer,
  RendererStatus,
  ScreenPoint,
  ToolId,
  ToolState,
} from '../types'
import type { HotspotRecord, SpecimenRecord } from '../../studio/types'
import { plateRect, resolvePlatePoints, type PlatePoint } from './points'
import { isPlateStandIn, resolvePlateUrl } from './standin'

/** Reference §06: zoom, isolate, labels, reset. */
const FLAT_TOOLS: readonly ToolId[] = ['zoom', 'isolate', 'labels', 'reset']

/** What the zoom tool steps through. Discrete rather than continuous because
 * a plate has no camera to fly — pressing zoom steps the plate up a size and
 * wraps back to fitted, which is the whole of what zoom can honestly mean
 * here. */
const ZOOM_STEPS = [1, 1.4, 1.9] as const

/** How long a plate takes to be "loaded" when it will never load at all — a
 * missing fallback is still a failure the shell must route on, even though
 * there is nowhere left to route TO. */
const LOAD_TIMEOUT_MS = 15_000

class FlatRenderer implements Renderer {
  readonly stage = 'paper' as const
  readonly supportedTools = FLAT_TOOLS
  /** §06: "Tiers describe render load. With no renderer there is no tier, so
   * the control goes rather than showing a fifth state." */
  readonly supportsQualityTiers = false

  private container: HTMLElement | null = null
  private plate: HTMLImageElement | null = null

  private status: RendererStatus = { state: 'idle' }
  private listeners = new Set<(s: RendererStatus) => void>()

  private hotspots: readonly HotspotRecord[] = []
  private points = new Map<string, PlatePoint>()

  private zoom = 0
  private labelsHidden = false
  private isolated: string | null = null
  private loadToken = 0
  private loadTimer: ReturnType<typeof setTimeout> | null = null

  mount(container: HTMLElement): void {
    this.container = container
    container.dataset.renderer = 'flat'
    container.dataset.state = this.status.state
    if (isPlateStandIn()) container.dataset.specimenSource = 'test-plate'
    this.draw()
  }

  unmount(): void {
    if (this.container) {
      delete this.container.dataset.renderer
      delete this.container.dataset.state
      delete this.container.dataset.specimenSource
      delete this.container.dataset.zoom
      delete this.container.dataset.isolate
      delete this.container.dataset.labels
      this.container.replaceChildren()
    }
    this.container = null
    this.plate = null
    // An unmounted renderer has no business still holding a timeout: the
    // shell drops this instance whenever the route changes, and a pending
    // 15-second timer would outlive it.
    if (this.loadTimer !== null) {
      clearTimeout(this.loadTimer)
      this.loadTimer = null
    }
    this.loadToken += 1
  }

  loadSpecimen(specimen: SpecimenRecord): Promise<void> {
    const token = ++this.loadToken
    this.hotspots = specimen.hotspots
    this.points = resolvePlatePoints(specimen.hotspots)
    this.zoom = 0
    this.labelsHidden = false
    this.isolated = null
    this.setStatus({ state: 'loading' })
    this.draw()

    const url = resolvePlateUrl(specimen)

    return new Promise<void>((resolve, reject) => {
      let settled = false
      const finish = (fn: () => void) => {
        if (settled || token !== this.loadToken) return
        settled = true
        clearTimeout(timer)
        if (this.loadTimer === timer) this.loadTimer = null
        fn()
      }
      const timer = (this.loadTimer = setTimeout(() => {
        finish(() => {
          const message = `fallback plate timed out: ${url}`
          this.setStatus({ state: 'failed', error: message })
          reject(new Error(message))
        })
      }, LOAD_TIMEOUT_MS))

      const image = new Image()
      image.decoding = 'async'
      image.alt = ''
      image.className = 'plate__image'
      image.addEventListener('load', () =>
        finish(() => {
          this.plate = image
          this.draw()
          this.setStatus({ state: 'ready' })
          resolve()
        }),
      )
      image.addEventListener('error', () =>
        finish(() => {
          // There is no third renderer to fall back to, so the honest answer
          // is a failure the shell can see rather than a blank stage that
          // claims to be ready.
          const message = `fallback plate failed to load: ${url}`
          this.setStatus({ state: 'failed', error: message })
          reject(new Error(message))
        }),
      )
      image.src = url
    })
  }

  hotspotToScreen(hotspotId: string): ScreenPoint | null {
    const point = this.points.get(hotspotId)
    if (!point || !this.container) return null
    // A plate has no depth, so nothing can be behind anything: `visible` is
    // about the hotspot being ON the stage, and the only thing that takes one
    // off is a tool the student pressed.
    if (this.labelsHidden) return null
    if (this.isolated !== null && this.isolated !== hotspotId) return null

    const rect = plateRect(
      this.container.clientWidth,
      this.container.clientHeight,
      ZOOM_STEPS[this.zoom],
    )
    return {
      x: rect.x + point.fx * rect.width,
      y: rect.y + point.fy * rect.height,
      visible: true,
    }
  }

  /** No render load, so no tier to set. */
  setTier(): void {}

  invokeTool(tool: ToolId, on?: boolean): void {
    if (!this.supportedTools.includes(tool)) return
    switch (tool) {
      case 'zoom':
        this.zoom = (this.zoom + 1) % ZOOM_STEPS.length
        break
      case 'labels':
        this.labelsHidden = on ?? !this.labelsHidden
        break
      case 'isolate':
        this.isolated = this.stepIsolate()
        break
      case 'reset':
        this.zoom = 0
        this.labelsHidden = false
        this.isolated = null
        break
    }
    this.draw()
  }

  isolateHotspot(hotspotId: string): void {
    if (!this.points.has(hotspotId)) return
    this.isolated = this.isolated === hotspotId ? null : hotspotId
    this.draw()
  }

  /** No plane to drag. */
  setSectionOffset(): void {}

  /** No cut on a flat plate: `cross-section` is not in `supportedTools`, so
   * there is never a plane to mark (MRB-189, §08). */
  sectionRule(): null {
    return null
  }

  /** Nothing to turn: the plate has no far side, so a retrieval target is
   * always already on screen. The round calls this on every question and this
   * renderer's honest answer is that the work is already done — which is why
   * the ruling on MRB-191 works identically in both renderers. */
  frameHotspot(): void {}

  toolState(tool: ToolId): ToolState | null {
    if (tool === 'zoom') {
      return {
        active: this.zoom > 0,
        step: this.zoom + 1,
        steps: ZOOM_STEPS.length,
      }
    }
    if (tool === 'labels') return { active: this.labelsHidden }
    if (tool === 'isolate') {
      if (this.hotspots.length < 2) return { active: false }
      const index = this.hotspots.findIndex((h) => h.id === this.isolated)
      if (index === -1) return { active: false, steps: this.hotspots.length }
      return {
        active: true,
        step: index + 1,
        steps: this.hotspots.length,
        // The structure's own label from the content record — the single
        // source of record (spec §3.2), never a second lookup.
        label: this.hotspots[index].label,
      }
    }
    return null
  }

  onStatus(cb: (status: RendererStatus) => void): () => void {
    this.listeners.add(cb)
    cb(this.status)
    return () => this.listeners.delete(cb)
  }

  // ── internals ──────────────────────────────────────────────────────────

  private stepIsolate(): string | null {
    if (this.hotspots.length < 2) return null
    if (this.isolated === null) return this.hotspots[0].id
    const next = this.hotspots.findIndex((h) => h.id === this.isolated) + 1
    return next >= this.hotspots.length ? null : this.hotspots[next].id
  }

  private draw(): void {
    const container = this.container
    if (!container) return

    container.dataset.zoom = String(this.zoom + 1)
    container.dataset.labels = this.labelsHidden ? 'hidden' : 'shown'
    container.dataset.isolate = this.isolated ?? 'off'

    container.replaceChildren()

    // §06 in situ: paper stage is #FFFDF8 with a 36px #F2E8D6 grid.
    const grid = document.createElement('div')
    grid.className = 'plate-grid'
    container.appendChild(grid)

    if (!this.plate) return

    // The diagram sits inside a PLATE, which is the reference's own §06
    // treatment — 2px rule, warm fill — kept as chrome around whatever
    // diagram loads. Design drew a lobed form there because they were
    // drawing a heart; the app cannot draw a heart, it loads one, so the
    // shape becomes the asset's and the frame stays ours.
    const rect = plateRect(
      container.clientWidth,
      container.clientHeight,
      ZOOM_STEPS[this.zoom],
    )
    const plate = document.createElement('div')
    plate.className = 'plate'
    plate.style.left = `${rect.x}px`
    plate.style.top = `${rect.y}px`
    plate.style.width = `${rect.width}px`
    plate.style.height = `${rect.height}px`
    plate.appendChild(this.plate)
    container.appendChild(plate)
  }

  private setStatus(status: RendererStatus): void {
    this.status = status
    if (this.container) this.container.dataset.state = status.state
    this.listeners.forEach((cb) => cb(status))
  }
}

export function createFlatRenderer(): Renderer {
  return new FlatRenderer()
}
