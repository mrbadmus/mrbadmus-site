// 3D Studio shell (MRB-186). One entry point, no client-side router (ruling
// on MRB-194): specimen selection is in-memory state. Everything on screen
// resolves from a single specimen record through a single id (spec §3.2).

import { useEffect, useState } from 'react'
import type { CapabilityReport } from './studio/capability'
import { detectCapability } from './studio/capability'
import type { QualitySetting } from './studio/quality'
import { effectiveRenderTier } from './studio/quality'
import { getSpecimen } from './studio/content'
import { createFlatRenderer } from './renderer/flat'
import type { Renderer } from './renderer/types'
import { Stage, type StageMode } from './components/Stage'
import { TopBar, ModeToggle } from './components/TopBar'
import { LibraryColumn, LibraryDrawer, LibraryFullScreen } from './components/Library'
import { InfoPanel, TabletPanel } from './components/InfoPanel'
import { RetrievalPanel } from './components/RetrievalPanel'
import { PhoneSheet } from './components/PhoneSheet'

type Layout = 'desktop' | 'tablet' | 'phone'

/** Which renderer answers for each kind of stage — the shell's whole renderer
 * policy, in one line. Injectable because gate 5 has to drive the tier journey
 * in an environment with no WebGL at all, where the honest production answer
 * is the flat route and so no tiered renderer would ever mount.
 *
 * ASYNC as of Stage 5 (ruling on MRB-190). The mesh renderer sits behind a
 * dynamic import, so the shell asks for one and waits — which is the whole
 * point: a Tier D device, which is exactly the device on the worst connection,
 * never requests the Three chunk at all. Nothing else about the policy moved;
 * `meshFailed` and the tier-D check still make the same decision, and the
 * import only changes when the module arrives. */
export type RendererFactory = (kind: 'viewport' | 'paper') => Promise<Renderer>

const defaultRenderer: RendererFactory = async (kind) => {
  if (kind !== 'viewport') return createFlatRenderer()
  const { createMeshRenderer } = await import('./renderer/mesh')
  return createMeshRenderer()
}

/** Start fetching the mesh chunk while the shell is still drawing, so the
 * split costs a capable device nothing. Tier D is deliberately excluded: on
 * that route the chunk would never be executed, and §5's load story already
 * has a 3MB asset budget to spend on a school connection. */
export function prefetchMeshRenderer(tier: CapabilityReport['tier']): void {
  if (tier === 'D') return
  void import('./renderer/mesh')
}

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

  const [renderer, setRenderer] = useState<Renderer | null>(null)
  useEffect(() => {
    let live = true
    void createRenderer(stageKind).then((next) => {
      if (live) setRenderer(next)
    })
    return () => {
      live = false
    }
  }, [createRenderer, stageKind])

  useEffect(() => {
    if (!renderer) return
    return renderer.onStatus((status) => {
      // The flat renderer is the last route there is. If its own plate will
      // not load there is nowhere further to fall, so a failure there must not
      // send the shell round the loop again looking for one.
      if (status.state === 'failed' && renderer.stage === 'viewport') setMeshFailed(true)
    })
  }, [renderer])

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

  // Between the shell drawing and the renderer module arriving (MRB-190's
  // code split) there are a few frames with no renderer. The Stage is still
  // the thing that draws them: the dark room, the container and the hint line
  // are the shell's furniture, and swapping in a substitute stage would give
  // the container a new element the moment the module landed — exactly the
  // remount gate 5 exists to forbid.
  const stage = (
    <Stage
      renderer={renderer}
      stageKind={stageKind}
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

      {/* The keys are load-bearing (MRB-187). Without them React matches these
          children by position, so entering the retrieval room — where the
          library is removed and the stage becomes the first child — remounts
          the stage, which destroys and rebuilds the WebGL context and reloads
          the specimen on every mode toggle. Keyed, the stage survives the
          switch: the specimen stays loaded and the camera keeps the view the
          student had turned it to, which is what "rotate freely, labels return
          after the round" implies. */}
      {mode === 'retrieve' ? (
        <main className="main main--retrieve">
          <div className="stagewrap" key="stage">{stage}</div>
          <RetrievalPanel
            key="side"
            specimen={specimen}
            targetIndex={0}
            roundSize={Math.max(retrievable.length, 1)}
          />
        </main>
      ) : layout === 'phone' ? (
        <main className="main">
          <div className="stagewrap" key="stage" style={{ flex: 1, position: 'relative' }}>
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
          <div className="stagewrap" key="stage">{stage}</div>
          <TabletPanel
            key="side"
            specimen={specimen}
            openHotspotId={openHotspotId}
            onOpenHotspot={setOpenHotspotId}
            onStartRetrieval={() => setMode('retrieve')}
          />
        </main>
      ) : (
        <main className="main main--explore">
          <LibraryColumn key="library" selectedId={specimenId} onSelect={selectSpecimen} />
          <div className="stagewrap" key="stage">{stage}</div>
          <InfoPanel
            key="side"
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
