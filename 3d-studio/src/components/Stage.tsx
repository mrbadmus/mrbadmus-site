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
import { SectionPlate, type StageLayout } from './SectionPlate'
import { ToolRail } from './ToolRail'

export type StageMode = 'explore' | 'retrieve'

/** .callout is a fixed 216px in studio.css; the gap to the dot is 90px, and
 * the rail occupies the first 78px of the stage (18px inset + 48px + air). */
const CALLOUT_WIDTH = 216
const CALLOUT_GAP = 90
const STAGE_PAD = 12
const RAIL_CLEAR = 78

/** Where the callout goes. Right of the dot as the frozen reference draws it;
 * left when the right will not fit; pinned to the stage's right edge with no
 * leader when neither side will, which is the narrow-stage case where a left
 * flip would bury the tool rail. */
function calloutPlacement(
  x: number,
  container: HTMLElement | null,
): { left: number; leader: number | null } {
  const width = container?.clientWidth ?? 0
  if (!width || x + CALLOUT_GAP + CALLOUT_WIDTH + STAGE_PAD <= width) {
    return { left: x + CALLOUT_GAP, leader: x + 20 }
  }
  const flipped = x - CALLOUT_GAP - CALLOUT_WIDTH
  if (flipped >= RAIL_CLEAR) return { left: flipped, leader: x - CALLOUT_GAP }
  return { left: Math.max(RAIL_CLEAR, width - CALLOUT_WIDTH - STAGE_PAD), leader: null }
}

export function Stage({
  renderer,
  stageKind,
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
  layout,
  overlayRef,
}: {
  /** null while the renderer module is still arriving (MRB-190's code split).
   * The Stage still draws: the dark room, the hint line and the container are
   * the SHELL's furniture, not the renderer's, and keeping this component
   * mounted across the wait is what keeps the container one element — which
   * gate 5 asserts and a swapped-in placeholder stage would quietly break. */
  renderer: Renderer | null
  /** which dressing to use before a renderer has answered */
  stageKind: 'viewport' | 'paper'
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
  /** The rail and the plate share the bottom edge, and on phone they share one
   * bar — which is a rendering decision, not a styling one, so the breakpoint
   * has to reach the components rather than only the stylesheet (MRB-189). */
  layout: StageLayout
  /** The element the shell draws OVER the stage, if any — the §05 phone sheet.
   * Measured rather than derived from the detent, because the quantity the
   * renderer needs is a pixel height, and deriving it would mean copying the
   * sheet's 55% and its 150px out of the stylesheet into TypeScript where they
   * would drift (MRB-216). Null at every layout that overlays nothing. */
  overlayRef?: React.RefObject<HTMLElement>
}) {
  const containerRef = useRef<HTMLDivElement>(null)
  const stageRootRef = useRef<HTMLDivElement>(null)
  const [status, setStatus] = useState<RendererStatus>({ state: 'idle' })
  const [hoverId, setHoverId] = useState<string | null>(null)
  const [panelOpen, setPanelOpen] = useState(false)
  const [, setViewportTick] = useState(0)
  // Bumped whenever a tool is pressed. A stepped tool's position lives inside
  // the renderer, so the shell has no state change of its own to re-render on
  // and would otherwise caption a step behind (MRB-188).
  const [, setToolTick] = useState(0)

  const dressing = renderer?.stage ?? stageKind
  const surface = dressing === 'viewport' ? 'dark' : 'paper'
  const ready = status.state === 'ready'

  // mount / unmount
  useEffect(() => {
    const el = containerRef.current
    if (!el || !renderer) return
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
    renderer?.loadSpecimen(specimen).catch(() => {})
  }, [renderer, specimen])

  // live tier — no reload, no remount (gate 5)
  useEffect(() => {
    renderer?.setTier(renderTier)
  }, [renderer, renderTier])

  // Frame the retrieval target before asking about it (ruling on MRB-191).
  //
  // Occlusion is honest, so a target on the far side of the specimen would be
  // "highlighted" with nothing on screen — not a hard question, an
  // unanswerable one. The camera turns to put it in view when the question is
  // PRESENTED, which is what this effect's dependencies say: a new target, or
  // a renderer that has just become ready. Not continuously — the student can
  // turn away again mid-question, and a camera that fought their hands would
  // be worse than the problem.
  useEffect(() => {
    if (!renderer || !ready || mode !== 'retrieve' || !targetHotspotId) return
    renderer.frameHotspot(targetHotspotId)
  }, [renderer, ready, mode, targetHotspotId])

  // And frame a structure the student picks from the panel, for the same
  // reason (MRB-187).
  //
  // The callout is drawn from `openDot`, which comes out of `dots` — and
  // `dots` drops anything the occlusion test says is hidden. So selecting a
  // structure facing away from the camera marked its chip open, said "1
  // SHOWN", and put nothing on the stage. With the two-hotspot placeholder
  // both anchors faced the camera and this never happened; the acquired heart
  // has fourteen spread over a concave form, about half of them hidden at any
  // moment, so half the panel's chips did nothing when clicked and gave no
  // reason why.
  //
  // Same ruling, same mechanism: an invisible highlight is not a highlight, so
  // the camera turns to bring the structure into view. On the flat renderer
  // frameHotspot is a no-op, which is correct — a paper plate has no camera
  // and its dots are never occluded.
  useEffect(() => {
    if (!renderer || !ready || mode !== 'explore' || !openHotspotId) return
    renderer.frameHotspot(openHotspotId)
  }, [renderer, ready, mode, openHotspotId])

  // reposition dots when the container resizes
  useEffect(() => {
    const el = containerRef.current
    if (!el || typeof ResizeObserver === 'undefined') return
    const ro = new ResizeObserver(() => setViewportTick((t) => t + 1))
    ro.observe(el)
    return () => ro.disconnect()
  }, [])

  // Declared up here rather than beside the hint line it also governs: the
  // inset effect below depends on it, and a const read from a dependency
  // array before its own initialiser is a temporal-dead-zone crash.
  const sectionOn = renderer?.toolState('cross-section')?.active === true

  // Tell the renderer how much of the stage the shell is covering, so it can
  // frame the specimen where a student can see it (MRB-216).
  //
  // PHONE ONLY, and the layout test is load-bearing rather than an
  // optimisation. Furniture floating over the stage is the design at every
  // width — on desktop the rail is a vertical column over the stage's left
  // edge and the specimen is centred behind it quite deliberately. What is
  // different on phone is that all of it becomes one BAND across the full
  // width of the bottom: the sheet, the rail turned horizontal on top of it
  // (§05), and the hint line above that. A band takes the bottom of the stage
  // away in a way a floating column does not.
  //
  // Measured as the union of those boxes rather than as the sheet alone. The
  // first cut inset only the sheet, and at the raised detent that was visibly
  // wrong: 150px of stage remains, the rail is 54px of it, so the specimen was
  // framed into the band and landed squarely behind the rail and the hint.
  //
  // Observing the sheet also means the camera re-frames ACROSS its 0.22s
  // detent transition rather than snapping at the end of it — the sheet
  // reports every intermediate height, and the offset is only a projection
  // matrix, so following it costs nothing.
  useEffect(() => {
    const el = containerRef.current
    const root = stageRootRef.current
    if (!renderer || !el) return
    if (layout !== 'phone') {
      renderer.setStageInsets({ bottom: 0 })
      return
    }

    const furniture = (): HTMLElement[] => {
      const found: HTMLElement[] = []
      const sheet = overlayRef?.current
      if (sheet) found.push(sheet)
      for (const sel of ['.rail', '.stagehint', '.secplate']) {
        const node = root?.querySelector<HTMLElement>(sel)
        if (node) found.push(node)
      }
      return found
    }

    const publish = () => {
      const stage = el.getBoundingClientRect()
      if (stage.height <= 0) {
        renderer.setStageInsets({ bottom: 0 })
        return
      }
      // The highest top edge among the bottom-anchored furniture is where the
      // covered strip begins. Anything sitting above the stage, or clear of it
      // entirely, contributes nothing.
      let top = stage.bottom
      for (const node of furniture()) {
        const box = node.getBoundingClientRect()
        if (box.height <= 0 || box.bottom <= stage.top) continue
        top = Math.min(top, Math.max(box.top, stage.top))
      }
      renderer.setStageInsets({ bottom: Math.min(stage.bottom - top, stage.height) })
    }

    publish()
    if (typeof ResizeObserver === 'undefined') return
    const ro = new ResizeObserver(publish)
    ro.observe(el)
    for (const node of furniture()) ro.observe(node)
    return () => {
      ro.disconnect()
      // Leaving an inset behind when the sheet goes — a rotation to tablet, or
      // the renderer being swapped — would frame every later specimen into a
      // band that is not covered by anything.
      renderer.setStageInsets({ bottom: 0 })
    }
    // sectionOn is a dependency because §09 swaps the hint line for the section
    // plate on that same edge, and the two are not the same height.
  }, [renderer, overlayRef, layout, sectionOn, ready])

  const dots = useHotspotDots(renderer, specimen, ready)

  const openDot = dots.find((d) => d.hotspot.id === openHotspotId) ?? null

  // While the specimen is on the wire the hint line carries the load rather
  // than the interaction: the stage has nothing to drag yet. No new furniture
  // — Design drew no loading state, and this one disappears at ready.
  //
  // It carries a stepped tool's position the same way, and for the same
  // reason: isolate and layers step through positions only the renderer knows
  // (how many parts the asset declares, what it calls them), and a control
  // that steps silently is one a student cannot follow. Same line, no new
  // furniture, gone the moment the tool is back at rest.
  // The plate owns the bottom edge whenever the cut is engaged, and the hint
  // line and the rail both answer to that (§09).

  const shownHint =
    status.state === 'loading'
      ? status.progress === undefined
        ? 'Loading specimen'
        : `Loading specimen · ${Math.round(status.progress * 100)}%`
      : ((renderer && toolCaption(renderer)) ?? hint)

  return (
    <div ref={stageRootRef} className={`stage stage--${dressing}`}>
      <div ref={containerRef} data-testid="renderer-container" style={{ position: 'absolute', inset: 0 }} />

      {/* §06: paper stage announces itself */}
      {dressing === 'paper' && (
        <div className="flatchip">
          <span className="flatchip__mark" aria-hidden="true" />
          <span className="flatchip__word">FLAT DIAGRAM</span>
        </div>
      )}

      {/* hotspot layer */}
      {mode === 'explore' &&
        dots.map(({ hotspot, index, x, y, onCut }) => {
          const numeral = String(index + 1).padStart(2, '0')
          const isOpen = hotspot.id === openHotspotId
          const state = isOpen ? 'open' : hoverId === hotspot.id ? 'hover' : 'closed'
          return (
            <HotspotDot
              key={hotspot.id}
              state={state}
              surface={onCut ? 'paper' : surface}
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
        dots.map(({ hotspot, index, x, y, onCut }) => {
          const numeral = String(index + 1).padStart(2, '0')
          const ground = onCut ? 'paper' : surface
          if (hotspot.id === targetHotspotId) {
            return (
              <HotspotDot
                key={hotspot.id}
                state="target"
                surface={ground}
                numeral={numeral}
                x={x}
                y={y}
                label="Highlighted structure"
              />
            )
          }
          return (
            <HotspotDot key={hotspot.id} state="inert" surface={ground} numeral={numeral} x={x} y={y} />
          )
        })}

      {/* one callout at a time, leader line keeps the link explicit (§01).
          It sits to the right of the dot as the reference draws it, and flips
          to the left when there is no room — the stage clips at its own edge,
          and dots go wherever the geometry puts them now that a real camera
          decides (MRB-187). */}
      {mode === 'explore' && openDot && renderer && (
        <>
          {calloutPlacement(openDot.x, containerRef.current).leader !== null && (
            <div
              className="leader"
              style={{
                left: calloutPlacement(openDot.x, containerRef.current).leader!,
                top: openDot.y,
                width: 70,
              }}
              aria-hidden="true"
            />
          )}
          <div
            className="callout"
            style={{
              left: calloutPlacement(openDot.x, containerRef.current).left,
              top: Math.max(12, openDot.y - 80),
            }}
          >
            <div className="callout__head">
              <span className="callout__dot" aria-hidden="true" />
              <span className="callout__eyebrow">
                STRUCTURE {String(openDot.index + 1).padStart(2, '0')}
              </span>
            </div>
            <div className="callout__title">{openDot.hotspot.label}</div>
            <div className="callout__detail">{openDot.hotspot.detail}</div>
            <div className="callout__foot">
              <button
                type="button"
                onClick={() => {
                  renderer.isolateHotspot(openDot.hotspot.id)
                  setToolTick((t) => t + 1)
                }}
              >
                Isolate
              </button>
              <i aria-hidden="true">·</i>
              <button type="button" onClick={() => onOpenHotspot(null)}>Hide label</button>
            </div>
          </div>
        </>
      )}

      {/* tool rail renders from declared support */}
      {renderer && (
        <StageTools
          renderer={renderer}
          mode={mode}
          collapse={sectionOn && layout === 'phone'}
          onInvoked={() => setToolTick((t) => t + 1)}
        />
      )}

      {/* The cut's position, present only while the cut is (§09). */}
      {renderer && (
        <SectionPlate
          renderer={renderer}
          layout={layout}
          onChange={() => setToolTick((t) => t + 1)}
        />
      )}

      {/* quality chip only where tiers mean anything (§06) */}
      {renderer?.supportsQualityTiers && (
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

      {/* §09: "The rotate hint at bottom centre yields to the plate — one
          thing lives on that edge at a time." */}
      {!sectionOn && <div className="stagehint">{shownHint}</div>}
    </div>
  )
}

interface Dot {
  hotspot: HotspotRecord
  index: number
  x: number
  y: number
  /** the dot is sitting on the cut face, which is a light ground (MRB-189) */
  onCut: boolean
}

/** Hotspot dots follow a camera that moves. The renderer resolves each anchor
 * on demand, so the shell samples once a frame and re-renders only when a dot
 * actually moved a whole pixel or changed visibility — an orbiting specimen
 * would otherwise re-render the tree at 60fps for sub-pixel drift, and a
 * still one would re-render for nothing at all. */
function useHotspotDots(
  renderer: Renderer | null,
  specimen: SpecimenRecord,
  ready: boolean,
): Dot[] {
  const [dots, setDots] = useState<Dot[]>([])

  useEffect(() => {
    if (!ready || !renderer) {
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
        next.push({
          hotspot,
          index,
          x: Math.round(point.x),
          y: Math.round(point.y),
          onCut: point.onCut === true,
        })
      })
      // The ground a dot stands on is part of what re-renders it: a dot that
      // has not moved a pixel but has just come to sit on the cut face is a
      // different drawing (MRB-189).
      const signature = next
        .map((d) => `${d.hotspot.id}@${d.x},${d.y}${d.onCut ? '#cut' : ''}`)
        .join('|')
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

/** The hint-line caption for whichever stepped tool is engaged, or null when
 * none is. `label` is the asset's own node name, passed straight through — the
 * shell never writes a structure's name (see `mesh/parts.ts`). */
function toolCaption(renderer: Renderer): string | null {
  const isolate = renderer.toolState('isolate')
  if (isolate?.active) {
    const named = isolate.label ? `Isolated: ${isolate.label}` : 'Isolated'
    return isolate.steps ? `${named} · ${isolate.step} of ${isolate.steps}` : named
  }
  const layers = renderer.toolState('layers')
  if (layers?.active) {
    return `Layer ${layers.step} of ${layers.steps} · outer layers removed`
  }
  // Cross-section is deliberately absent: it has a plate of its own at the
  // foot of the stage carrying the same percentage, and §09 rules that one
  // thing lives on that edge at a time. The hint yields; it does not echo.
  return null
}

function StageTools({
  renderer,
  mode,
  collapse,
  onInvoked,
}: {
  renderer: Renderer
  mode: StageMode
  /** §09, phone: "THE RAIL YIELDS, IT DOES NOT STACK." Both the rail and the
   * slider want the bottom edge and there is room for one, so turning
   * cross-section on collapses the five-icon rail to the single tool that is
   * running and the slider takes the rest of that same bar. Tapping the tool
   * exits and the rail returns. No second row, no sheet, and the stage keeps
   * its height. */
  collapse: boolean
  onInvoked: () => void
}) {
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

  // §02: the retrieval room keeps a reduced rail. §09 on phone: while the cut
  // is running, the rail is that one tool. Both are the same move — the rail
  // draws from `supportedTools` and never from a list of its own, so narrowing
  // the rail is narrowing what the renderer declares to it.
  const railRenderer = useMemo(() => {
    const keep: ToolId[] | null = collapse
      ? ['cross-section']
      : mode === 'retrieve'
        ? ['rotate', 'zoom', 'reset']
        : null
    if (!keep) return renderer
    return new Proxy(renderer, {
      get(target, prop, receiver) {
        if (prop === 'supportedTools') {
          return target.supportedTools.filter((t) => keep.includes(t))
        }
        return Reflect.get(target, prop, receiver)
      },
    })
  }, [renderer, mode, collapse])

  return (
    <ToolRail
      renderer={railRenderer}
      collapsed={collapse}
      activeTool={activeTool}
      autoRotate={autoRotate}
      onTool={(tool) => {
        // Reset is momentary — it fires and the rail keeps its previous
        // selection. A stepped tool (isolate, layers) reports its own
        // engaged/at-rest state through toolState, so the rail reads that
        // rather than remembering the last press: pressing isolate past its
        // last part returns the whole specimen, and a button still lit at
        // that point would be describing something that is no longer true.
        // Everything else the renderer honours is a pointer mode.
        if (tool !== 'reset' && renderer.toolState(tool) === null) setActiveTool(tool)
        renderer.invokeTool(tool)
        onInvoked()
      }}
      onAutoRotate={() => {
        const next = !autoRotate
        setAutoRotate(next)
        renderer.invokeTool('auto-rotate', next)
        onInvoked()
      }}
    />
  )
}
