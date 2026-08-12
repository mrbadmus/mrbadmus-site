// 3D Studio shell (MRB-186). One entry point, no client-side router (ruling
// on MRB-194): specimen selection is in-memory state. Everything on screen
// resolves from a single specimen record through a single id (spec §3.2).

import { useEffect, useMemo, useState } from 'react'
import type { CapabilityReport } from './studio/capability'
import { detectCapability } from './studio/capability'
import type { QualitySetting } from './studio/quality'
import { effectiveRenderTier } from './studio/quality'
import { getSpecimen } from './studio/content'
import { createPlaceholderRenderer } from './renderer/placeholder'
import { createMeshRenderer } from './renderer/mesh'
import type { Renderer } from './renderer/types'
import { Stage, type StageMode } from './components/Stage'
import { TopBar, ModeToggle } from './components/TopBar'
import { LibraryColumn, LibraryDrawer, LibraryFullScreen } from './components/Library'
import { InfoPanel, TabletPanel } from './components/InfoPanel'
import { RetrievalPanel } from './components/RetrievalPanel'
import { PhoneSheet } from './components/PhoneSheet'

type Layout = 'desktop' | 'tablet' | 'phone'

/** Which renderer answers for each kind of stage — the shell's whole renderer
 * policy, in one line. `paper` is the placeholder until the flat renderer
 * lands at Stage 5. Injectable because gate 5 has to drive the tier journey
 * in an environment with no WebGL at all, where the honest production answer
 * is the flat route and so no tiered renderer would ever mount. */
export type RendererFactory = (kind: 'viewport' | 'paper') => Renderer

const defaultRenderer: RendererFactory = (kind) =>
  kind === 'viewport' ? createMeshRenderer() : createPlaceholderRenderer('paper')

function layoutFor(width: number): Layout {
  if (width >= 1024) return 'desktop'
  if (width >= 700) return 'tablet'
  return 'phone'
}

function useLayout(): Layout {
  const [layout, setLayout] = useState<Layout>(() => layoutFor(window.innerWidth))
  useEffect(() => {
    const onResize = () => setLayout(layoutFor(window.innerWidth))
    window.addEventListener('resize', onResize)
    return () => window.removeEventListener('resize', onResize)
  }, [])
  return layout
}

export default function App({
  capability,
  createRenderer = defaultRenderer,
}: {
  capability?: CapabilityReport
  createRenderer?: RendererFactory
}) {
  const [probe] = useState<CapabilityReport>(() => capability ?? detectCapability())
  const layout = useLayout()

  const [specimenId, setSpecimenId] = useState('heart')
  const [mode, setMode] = useState<StageMode>('explore')
  const [openHotspotId, setOpenHotspotId] = useState<string | null>(null)
  const [quality, setQuality] = useState<QualitySetting>('auto')
  const [libraryOpen, setLibraryOpen] = useState(false)
  const [sheetRaised, setSheetRaised] = useState(false)

  const specimen = getSpecimen(specimenId)

  // Failure is a route, not an error (spec §3.1): a mesh that will not load,
  // times out, or loses its WebGL context drops the whole stage to the flat
  // renderer rather than showing a broken viewport. The flat renderer itself
  // arrives at Stage 5, so until then that route lands on the paper
  // placeholder — which is the designed §06 stage, not a gap.
  const [meshFailed, setMeshFailed] = useState(false)
  useEffect(() => {
    // A different specimen deserves its own attempt.
    setMeshFailed(false)
  }, [specimenId])

  // Tier D (no WebGL2) or a flat-content specimen ⇒ paper stage.
  const stageKind: 'viewport' | 'paper' =
    probe.tier === 'D' || specimen.renderer === 'flat' || meshFailed ? 'paper' : 'viewport'
  const renderer = useMemo(() => createRenderer(stageKind), [createRenderer, stageKind])

  useEffect(
    () =>
      renderer.onStatus((status) => {
        if (status.state === 'failed') setMeshFailed(true)
      }),
    [renderer],
  )

  const renderTier = effectiveRenderTier(quality, probe.tier)

  const retrievable = specimen.hotspots.filter((h) => h.retrievable)
  const targetHotspotId = retrievable[0]?.id ?? null

  const hint =
    mode === 'retrieve'
      ? 'Rotate freely · labels return after the round'
      : stageKind === 'paper'
        ? layout === 'desktop'
          ? 'Click a dot to label'
          : 'Tap a dot to label'
        : layout === 'desktop'
          ? 'Drag to rotate · click a dot to label'
          : 'Drag to rotate · tap a dot to label'

  const selectSpecimen = (id: string) => {
    setSpecimenId(id)
    setOpenHotspotId(null)
  }

  const stage = (
    <Stage
      renderer={renderer}
      specimen={specimen}
      mode={mode}
      renderTier={renderTier}
      quality={quality}
      detectedTier={probe.tier}
      onQuality={setQuality}
      openHotspotId={openHotspotId}
      onOpenHotspot={setOpenHotspotId}
      targetHotspotId={targetHotspotId}
      hint={hint}
    />
  )

  return (
    <div className="app" data-mode={mode} data-layout={layout} data-detected-tier={probe.tier}>
      <TopBar
        layout={layout}
        mode={mode}
        onMode={(m) => {
          setMode(m)
          setOpenHotspotId(null)
        }}
        onOpenLibrary={() => setLibraryOpen(true)}
        phoneTitle={layout === 'phone' && sheetRaised ? specimen.name : null}
      />

      {mode === 'explore' && layout === 'desktop' && (
        <div className="crumbstrip">
          <div className="crumb">
            3D Studio<i>&nbsp;&nbsp;/&nbsp;&nbsp;</i>
            {specimen.system}
            <i>&nbsp;&nbsp;/&nbsp;&nbsp;</i>
            <b>{specimen.name}</b>
          </div>
          <ModeToggle
            mode={mode}
            onMode={(m) => {
              setMode(m)
              setOpenHotspotId(null)
            }}
          />
        </div>
      )}

      {mode === 'retrieve' && <div className="hatch" aria-hidden="true" />}

      {mode === 'retrieve' ? (
        <main className="main main--retrieve">
          <div className="stagewrap">{stage}</div>
          <RetrievalPanel
            specimen={specimen}
            targetIndex={0}
            roundSize={Math.max(retrievable.length, 1)}
          />
        </main>
      ) : layout === 'phone' ? (
        <main className="main">
          <div className="stagewrap" style={{ flex: 1, position: 'relative' }}>
            {stage}
            <PhoneSheet
              specimen={specimen}
              raised={sheetRaised}
              onRaisedChange={setSheetRaised}
              openHotspotId={openHotspotId}
              onOpenHotspot={setOpenHotspotId}
              onStartRetrieval={() => setMode('retrieve')}
            />
          </div>
        </main>
      ) : layout === 'tablet' ? (
        <main className="main">
          <div className="stagewrap">{stage}</div>
          <TabletPanel
            specimen={specimen}
            openHotspotId={openHotspotId}
            onOpenHotspot={setOpenHotspotId}
            onStartRetrieval={() => setMode('retrieve')}
          />
        </main>
      ) : (
        <main className="main main--explore">
          <LibraryColumn selectedId={specimenId} onSelect={selectSpecimen} />
          <div className="stagewrap">{stage}</div>
          <InfoPanel
            specimen={specimen}
            openHotspotId={openHotspotId}
            onOpenHotspot={setOpenHotspotId}
            onStartRetrieval={() => setMode('retrieve')}
          />
        </main>
      )}

      {libraryOpen && layout === 'tablet' && (
        <LibraryDrawer
          selectedId={specimenId}
          onSelect={selectSpecimen}
          onClose={() => setLibraryOpen(false)}
        />
      )}
      {libraryOpen && layout === 'phone' && (
        <LibraryFullScreen
          selectedId={specimenId}
          onSelect={selectSpecimen}
          onClose={() => setLibraryOpen(false)}
        />
      )}
    </div>
  )
}
