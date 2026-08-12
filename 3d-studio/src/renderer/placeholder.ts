// Stage 1 placeholder renderer — a soft grey form and fixed hotspot anchors.
// Plain DOM on purpose: proves the renderer contract leaks neither Three.js
// nor React into the shell boundary. Replaced by the real `mesh` renderer at
// Stage 2; the `paper` variant stands in for the future `flat` renderer.

import type {
  Renderer,
  RendererStatus,
  RenderTier,
  ScreenPoint,
  ToolId,
} from './types'
import type { SpecimenRecord } from '../studio/types'

const VIEWPORT_TOOLS: readonly ToolId[] = [
  'rotate',
  'zoom',
  'isolate',
  'cross-section',
  'layers',
  'reset',
  'auto-rotate',
]

// Reference §06: zoom, isolate, labels, reset. Rotate, cross-section, layers
// and auto-rotate are absent, not greyed.
const PAPER_TOOLS: readonly ToolId[] = ['zoom', 'isolate', 'labels', 'reset']

/** Fixed anchor fractions, cycled by hotspot index. Real coordinates arrive
 * with authored content (position3d/position2d are all-zero until Stage 8);
 * the placeholder's job is to give the shell believable, deterministic points
 * to hang dots on. */
const ANCHORS: ReadonlyArray<[number, number]> = [
  [0.38, 0.29],
  [0.57, 0.25],
  [0.61, 0.47],
  [0.34, 0.52],
  [0.47, 0.64],
  [0.59, 0.71],
]

class PlaceholderRenderer implements Renderer {
  readonly stage: 'viewport' | 'paper'
  readonly supportedTools: readonly ToolId[]
  readonly supportsQualityTiers: boolean

  private container: HTMLElement | null = null
  private tier: RenderTier = 'A'
  private status: RendererStatus = { state: 'idle' }
  private listeners = new Set<(s: RendererStatus) => void>()
  private hotspotIds: string[] = []

  constructor(stage: 'viewport' | 'paper') {
    this.stage = stage
    this.supportedTools = stage === 'viewport' ? VIEWPORT_TOOLS : PAPER_TOOLS
    this.supportsQualityTiers = stage === 'viewport'
  }

  mount(container: HTMLElement): void {
    this.container = container
    container.dataset.renderer = `placeholder-${this.stage}`
    container.dataset.state = this.status.state
    this.draw()
  }

  unmount(): void {
    if (this.container) {
      delete this.container.dataset.renderer
      delete this.container.dataset.tier
      delete this.container.dataset.state
      this.container.replaceChildren()
    }
    this.container = null
  }

  async loadSpecimen(specimen: SpecimenRecord): Promise<void> {
    this.setStatus({ state: 'loading' })
    this.hotspotIds = specimen.hotspots.map((h) => h.id)
    this.draw()
    this.setStatus({ state: 'ready' })
  }

  hotspotToScreen(hotspotId: string): ScreenPoint | null {
    const index = this.hotspotIds.indexOf(hotspotId)
    if (index === -1 || !this.container) return null
    const [fx, fy] = ANCHORS[index % ANCHORS.length]
    return {
      x: fx * this.container.clientWidth,
      y: fy * this.container.clientHeight,
      visible: true,
    }
  }

  setTier(tier: RenderTier): void {
    if (!this.supportsQualityTiers) return
    this.tier = tier
    this.draw()
  }

  /** Nothing to drive: the placeholder has no camera. Present so the
   * declaration and invocation halves of the tool contract stay paired. */
  invokeTool(): void {}

  /** No geometry to take apart and no plane to drag, so these are no-ops
   * rather than absent — the placeholder keeps satisfying the whole contract
   * (MRB-188, MRB-189). */
  isolateHotspot(): void {}

  setSectionOffset(): void {}

  toolState(): null {
    return null
  }

  onStatus(cb: (status: RendererStatus) => void): () => void {
    this.listeners.add(cb)
    cb(this.status)
    return () => this.listeners.delete(cb)
  }

  private setStatus(status: RendererStatus): void {
    this.status = status
    // Readable from outside the app: the parity harness waits on this rather
    // than on a fixed sleep, now that one of the two renderers loads over the
    // network (MRB-187).
    if (this.container) this.container.dataset.state = status.state
    this.listeners.forEach((cb) => cb(status))
  }

  /** The tier genuinely changes what gets drawn (gate 5): A keeps the ground
   * shadow, the specular highlight and full shading; B drops the shadow; C
   * drops the highlight and flattens the form's shading. */
  private draw(): void {
    if (!this.container) return
    this.container.dataset.tier = this.supportsQualityTiers ? this.tier : ''
    this.container.replaceChildren()

    if (this.stage === 'viewport') {
      if (this.tier === 'A') {
        const shadow = document.createElement('div')
        shadow.className = 'ph-shadow'
        this.container.appendChild(shadow)
      }
      const form = document.createElement('div')
      form.className = `ph-form ph-form--${this.tier.toLowerCase()}`
      this.container.appendChild(form)
      if (this.tier !== 'C') {
        const glint = document.createElement('div')
        glint.className = 'ph-glint'
        this.container.appendChild(glint)
      }
    } else {
      const grid = document.createElement('div')
      grid.className = 'ph-grid'
      this.container.appendChild(grid)
      const plate = document.createElement('div')
      plate.className = 'ph-plate'
      const lobeA = document.createElement('div')
      lobeA.className = 'ph-lobe ph-lobe--a'
      const lobeB = document.createElement('div')
      lobeB.className = 'ph-lobe ph-lobe--b'
      this.container.append(plate, lobeA, lobeB)
    }
  }
}

export function createPlaceholderRenderer(stage: 'viewport' | 'paper'): Renderer {
  return new PlaceholderRenderer(stage)
}
