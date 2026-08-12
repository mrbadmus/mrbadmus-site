// The stage — a container the renderer mounts into, plus everything the shell
// owns on top of it: hotspot layer, callout, tool rail, quality chip, hint
// line. The shell talks to the renderer only through the Renderer interface.

import { useEffect, useMemo, useRef, useState } from 'react'
import type { Renderer, RendererStatus, RenderTier, ToolId } from '../renderer/types'
import type { HotspotRecord, SpecimenRecord } from '../studio/types'
import type { CapabilityTier } from '../studio/capability'
import type { QualitySetting } from '../studio/quality'
import { HotspotDot } from './HotspotDot'
import { QualityChip, QualityPanel } from './Quality'
import { ToolRail } from './ToolRail'

export type StageMode = 'explore' | 'retrieve'

export function Stage({
  renderer,
  specimen,
  mode,
  renderTier,
  quality,
  detectedTier,
  onQuality,
  openHotspotId,
  onOpenHotspot,
  targetHotspotId,
  hint,
}: {
  renderer: Renderer
  specimen: SpecimenRecord
  mode: StageMode
  renderTier: RenderTier
  quality: QualitySetting
  detectedTier: CapabilityTier
  onQuality: (q: QualitySetting) => void
  openHotspotId: string | null
  onOpenHotspot: (id: string | null) => void
  targetHotspotId?: string | null
  hint: string
}) {
  const containerRef = useRef<HTMLDivElement>(null)
  const [status, setStatus] = useState<RendererStatus>({ state: 'idle' })
  const [hoverId, setHoverId] = useState<string | null>(null)
  const [panelOpen, setPanelOpen] = useState(false)
  const [, setViewportTick] = useState(0)

  const surface = renderer.stage === 'viewport' ? 'dark' : 'paper'

  // mount / unmount
  useEffect(() => {
    const el = containerRef.current
    if (!el) return
    renderer.mount(el)
    const unsubscribe = renderer.onStatus(setStatus)
    return () => {
      unsubscribe()
      renderer.unmount()
    }
  }, [renderer])

  // load the selected specimen. A rejection is already reported through
  // onStatus, and the shell's answer to it is a different renderer, so the
  // promise is caught here rather than surfacing as an unhandled rejection.
  useEffect(() => {
    renderer.loadSpecimen(specimen).catch(() => {})
  }, [renderer, specimen])

  // live tier — no reload, no remount (gate 5)
  useEffect(() => {
    renderer.setTier(renderTier)
  }, [renderer, renderTier])

  // reposition dots when the container resizes
  useEffect(() => {
    const el = containerRef.current
    if (!el || typeof ResizeObserver === 'undefined') return
    const ro = new ResizeObserver(() => setViewportTick((t) => t + 1))
    ro.observe(el)
    return () => ro.disconnect()
  }, [])

  const ready = status.state === 'ready'
  const dots = useHotspotDots(renderer, specimen, ready)

  const openDot = dots.find((d) => d.hotspot.id === openHotspotId) ?? null

  // While the specimen is on the wire the hint line carries the load rather
  // than the interaction: the stage has nothing to drag yet. No new furniture
  // — Design drew no loading state, and this one disappears at ready.
  const shownHint =
    status.state === 'loading'
      ? status.progress === undefined
        ? 'Loading specimen'
        : `Loading specimen · ${Math.round(status.progress * 100)}%`
      : hint

  return (
    <div className={`stage stage--${renderer.stage}`}>
      <div ref={containerRef} data-testid="renderer-container" style={{ position: 'absolute', inset: 0 }} />

      {/* §06: paper stage announces itself */}
      {renderer.stage === 'paper' && (
        <div className="flatchip">
          <span className="flatchip__mark" aria-hidden="true" />
          <span className="flatchip__word">FLAT DIAGRAM</span>
        </div>
      )}

      {/* hotspot layer */}
      {mode === 'explore' &&
        dots.map(({ hotspot, index, x, y }) => {
          const numeral = String(index + 1).padStart(2, '0')
          const isOpen = hotspot.id === openHotspotId
          const state = isOpen ? 'open' : hoverId === hotspot.id ? 'hover' : 'closed'
          return (
            <HotspotDot
              key={hotspot.id}
              state={state}
              surface={surface}
              numeral={numeral}
              x={x}
              y={y}
              label={hotspot.label}
              onOpen={() => onOpenHotspot(isOpen ? null : hotspot.id)}
              onHoverChange={(hovering) => setHoverId(hovering ? hotspot.id : null)}
            />
          )
        })}

      {mode === 'retrieve' &&
        dots.map(({ hotspot, index, x, y }) => {
          const numeral = String(index + 1).padStart(2, '0')
          if (hotspot.id === targetHotspotId) {
            return (
              <HotspotDot
                key={hotspot.id}
                state="target"
                surface={surface}
                numeral={numeral}
                x={x}
                y={y}
                label="Highlighted structure"
              />
            )
          }
          return (
            <HotspotDot key={hotspot.id} state="inert" surface={surface} numeral={numeral} x={x} y={y} />
          )
        })}

      {/* one callout at a time, leader line keeps the link explicit (§01) */}
      {mode === 'explore' && openDot && (
        <>
          <div
            className="leader"
            style={{ left: openDot.x + 20, top: openDot.y, width: 70 }}
            aria-hidden="true"
          />
          <div className="callout" style={{ left: openDot.x + 90, top: Math.max(12, openDot.y - 80) }}>
            <div className="callout__head">
              <span className="callout__dot" aria-hidden="true" />
              <span className="callout__eyebrow">
                STRUCTURE {String(openDot.index + 1).padStart(2, '0')}
              </span>
            </div>
            <div className="callout__title">{openDot.hotspot.label}</div>
            <div className="callout__detail">{openDot.hotspot.detail}</div>
            <div className="callout__foot">
              <button type="button">Isolate</button>
              <i aria-hidden="true">·</i>
              <button type="button" onClick={() => onOpenHotspot(null)}>Hide label</button>
            </div>
          </div>
        </>
      )}

      {/* tool rail renders from declared support; no-ops pending Stage 2 */}
      <StageTools renderer={renderer} mode={mode} />

      {/* quality chip only where tiers mean anything (§06) */}
      {renderer.supportsQualityTiers && (
        <>
          <QualityChip
            setting={quality}
            detected={detectedTier}
            open={panelOpen}
            onToggle={() => setPanelOpen((o) => !o)}
          />
          {panelOpen && (
            <QualityPanel
              setting={quality}
              detected={detectedTier}
              onSelect={(q) => {
                onQuality(q)
                setPanelOpen(false)
              }}
            />
          )}
        </>
      )}

      <div className="stagehint">{shownHint}</div>
    </div>
  )
}

interface Dot {
  hotspot: HotspotRecord
  index: number
  x: number
  y: number
}

/** Hotspot dots follow a camera that moves. The renderer resolves each anchor
 * on demand, so the shell samples once a frame and re-renders only when a dot
 * actually moved a whole pixel or changed visibility — an orbiting specimen
 * would otherwise re-render the tree at 60fps for sub-pixel drift, and a
 * still one would re-render for nothing at all. */
function useHotspotDots(renderer: Renderer, specimen: SpecimenRecord, ready: boolean): Dot[] {
  const [dots, setDots] = useState<Dot[]>([])

  useEffect(() => {
    if (!ready) {
      setDots([])
      return
    }
    let frame = 0
    let previous = ''

    const sample = () => {
      const next: Dot[] = []
      specimen.hotspots.forEach((hotspot, index) => {
        const point = renderer.hotspotToScreen(hotspot.id)
        if (!point || !point.visible) return
        next.push({ hotspot, index, x: Math.round(point.x), y: Math.round(point.y) })
      })
      const signature = next.map((d) => `${d.hotspot.id}@${d.x},${d.y}`).join('|')
      if (signature !== previous) {
        previous = signature
        setDots(next)
      }
      frame = requestAnimationFrame(sample)
    }

    sample()
    return () => cancelAnimationFrame(frame)
  }, [renderer, specimen, ready])

  return dots
}

function StageTools({ renderer, mode }: { renderer: Renderer; mode: StageMode }) {
  const [activeTool, setActiveTool] = useState<ToolId | null>(
    renderer.supportedTools.includes('rotate') ? 'rotate' : null,
  )
  // Off by default at every tier. Spec §5 requires that at Tier C; the frozen
  // reference draws the toggle off at Tier A too, so the reference sets the
  // default and Tier C's requirement is met by it (Stage 2 report).
  const [autoRotate, setAutoRotate] = useState(false)

  // A new renderer instance starts from its own defaults, so the toggle must
  // not carry a stale "on" across a switch to the flat stage and back.
  useEffect(() => {
    setAutoRotate(false)
    setActiveTool(renderer.supportedTools.includes('rotate') ? 'rotate' : null)
  }, [renderer])

  // §02: the retrieval room keeps a reduced rail
  const retrieveRenderer = useMemo(() => {
    if (mode !== 'retrieve') return renderer
    const keep: ToolId[] = ['rotate', 'zoom', 'reset']
    return new Proxy(renderer, {
      get(target, prop, receiver) {
        if (prop === 'supportedTools') {
          return target.supportedTools.filter((t) => keep.includes(t))
        }
        return Reflect.get(target, prop, receiver)
      },
    })
  }, [renderer, mode])

  return (
    <ToolRail
      renderer={retrieveRenderer}
      activeTool={activeTool}
      autoRotate={autoRotate}
      onTool={(tool) => {
        // Reset is momentary — it fires and the rail keeps its previous
        // selection. Everything else the renderer honours is a mode.
        if (tool !== 'reset') setActiveTool(tool)
        renderer.invokeTool(tool)
      }}
      onAutoRotate={() => {
        const next = !autoRotate
        setAutoRotate(next)
        renderer.invokeTool('auto-rotate', next)
      }}
    />
  )
}
