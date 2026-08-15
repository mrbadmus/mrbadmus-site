// 3D Studio shell (MRB-186). One entry point, no client-side router (ruling
// on MRB-194): specimen selection is in-memory state. Everything on screen
// resolves from a single specimen record through a single id (spec §3.2).

import { useEffect, useMemo, useRef, useState } from 'react'
import type { CapabilityReport } from './studio/capability'
import { detectCapability } from './studio/capability'
import type { QualitySetting } from './studio/quality'
import { effectiveRenderTier } from './studio/quality'
import { getSpecimen, specimenForKeyStage, viewingKeyStage } from './studio/content'
import { createFlatRenderer } from './renderer/flat'
import type { Renderer } from './renderer/types'
import {
  PROVISIONAL_ANONYMOUS_PROFILE,
  createMemoryAdapter,
  type AttemptSubmitter,
  type LearnerProfile,
} from './studio/attempts'
import { FRESH_ACCESS, canStartRound, completeRound, shouldPersist } from './studio/access'
import {
  answerQuestion,
  currentQuestion,
  isCorrect as isCorrectAnswer,
  eligibleHotspots,
  pointsFor,
  askedStructures,
  startRound,
  ROUND_SIZE,
  type RoundDeps,
  type RoundState,
} from './studio/retrieval'
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

/** The in-memory adapter is the ONLY submitter tonight (MRB-191 scope): the
 * table, its RLS and the real submitter are a later stage with Mide present.
 * Injectable so that later stage swaps one object and the round never learns
 * that anything changed. */
const memoryAttempts = createMemoryAdapter()

export default function App({
  capability,
  createRenderer = defaultRenderer,
  profile = PROVISIONAL_ANONYMOUS_PROFILE,
  submitter = memoryAttempts,
  now = () => Date.now(),
  makeRoundId = () => `r${Date.now().toString(36)}`,
  random = Math.random,
}: {
  capability?: CapabilityReport
  createRenderer?: RendererFactory
  /** provisional until sign-in is wired — see studio/attempts.ts */
  profile?: LearnerProfile
  submitter?: AttemptSubmitter
  now?: () => number
  makeRoundId?: () => string
  /** which six a round draws — injectable so a gate can drive a reproducible
   * round, exactly as makeRoundId and now are */
  random?: () => number
}) {
  const [probe] = useState<CapabilityReport>(() => capability ?? detectCapability())
  const layout = useLayout()

  const [specimenId, setSpecimenId] = useState('heart')
  const [mode, setMode] = useState<StageMode>('explore')
  const [openHotspotId, setOpenHotspotId] = useState<string | null>(null)
  const [quality, setQuality] = useState<QualitySetting>('auto')
  const [libraryOpen, setLibraryOpen] = useState(false)
  const [sheetRaised, setSheetRaised] = useState(false)
  // The sheet covers the lower part of the stage, so the renderer has to be
  // told how much in order to frame the specimen where it can be seen. Handed
  // over as an element to MEASURE rather than as the detent, so the sheet's
  // 55% and its 150px stay in the stylesheet and are not copied into TS where
  // they would drift (MRB-216).
  const sheetRef = useRef<HTMLDivElement>(null)

  // The key-stage filter is applied ONCE, here, at the top (MRB-193/186). What
  // flows on from this line is the specimen as THIS viewer sees it, so the
  // stage, both renderers, the panel, the sheet, the library and the retrieval
  // round cannot disagree about what is on the heart — a KS3 student is not
  // asked about a structure the stage never drew for them.
  //
  // The memo is load-bearing, not tidiness: `Stage` reloads the specimen and
  // resamples its dots whenever this identity changes, so a fresh object every
  // render would re-fetch the GLB continuously. `getSpecimen` returns a stable
  // module-level record and `specimenForKeyStage` returns that same object
  // untouched when nothing is filtered out, so both dependencies are stable.
  const record = getSpecimen(specimenId)
  const keyStage = viewingKeyStage(profile)
  const specimen = useMemo(() => specimenForKeyStage(record, keyStage), [record, keyStage])

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

  // ── the retrieval round (MRB-191) ───────────────────────────────────────
  const [access, setAccess] = useState(FRESH_ACCESS)
  const [gate, setGate] = useState<'sign-in' | null>(null)
  const [round, setRound] = useState<RoundState | null>(null)
  const [revealed, setRevealed] = useState<{ label: string; detail: string } | null>(null)
  const [points, setPoints] = useState(0)
  // Structures asked in this browser session, so a second round prefers the
  // ones the first did not reach (MRB-191). Session-scoped on purpose:
  // attempts do not persist yet, and a reload is a fresh start.
  const [seenStructures, setSeenStructures] = useState<ReadonlySet<string>>(
    () => new Set<string>(),
  )

  const roundDeps: RoundDeps = {
    now,
    roundId: round?.id ?? '',
    profile,
    submitter,
    random,
    seen: seenStructures,
  }

  const eligible = eligibleHotspots(specimen, profile)
  // The rail draws squares for the round's own first pass. Before a round
  // exists there is nothing to draw, so this is only the panel's fallback.
  const roundSize = round?.size ?? Math.max(Math.min(eligible.length, ROUND_SIZE), 1)
  const question = round ? currentQuestion(round) : null
  const targetHotspotId = question?.hotspot.id ?? null

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

  const enterRetrieval = () => {
    setMode('retrieve')
    setOpenHotspotId(null)
    setRevealed(null)
    // The free round is spent: the sign-in moment (§03) is due, and no second
    // round starts behind it. Structured, not wired — see studio/access.ts.
    if (!canStartRound(access, profile)) {
      setGate('sign-in')
      setRound(null)
      return
    }
    setGate(null)
    const started = startRound(specimen, { ...roundDeps, roundId: makeRoundId() })
    setRound(started)
    // Recorded at the START of the round: a student who abandons halfway has
    // still met these structures, and asking them again first would be the
    // re-run this ruling exists to prevent.
    const asked = askedStructures(started)
    setSeenStructures((prev) => new Set([...prev, ...asked]))
  }

  const leaveRetrieval = () => {
    setMode('explore')
    setRound(null)
    setRevealed(null)
    setOpenHotspotId(null)
  }

  /** Grade, submit, and let the round move on. A reveal produces no payload —
   * the contract is explicit that giving up is not an attempt (§1). */
  const respond = (outcome: 'correct' | 'wrong' | 'skipped' | 'revealed', response: string) => {
    if (!round) return
    const asked = currentQuestion(round)
    const next = answerQuestion(round, specimen, outcome, response, roundDeps)
    setRound(next.round)

    if (next.attempt && shouldPersist(profile)) {
      void submitter.submit(next.attempt)
    }

    if (outcome === 'correct' || outcome === 'revealed') {
      setRevealed(
        asked ? { label: asked.hotspot.label, detail: asked.hotspot.detail } : null,
      )
    }
    setPoints(pointsFor(next.round.results))

    if (next.round.complete) {
      const done = completeRound(access, profile)
      setAccess(done.access)
      setGate(done.gate)
    }
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
      layout={layout}
      overlayRef={layout === 'phone' ? sheetRef : undefined}
    />
  )

  return (
    <div
      className="app"
      data-mode={mode}
      data-layout={layout}
      // The phone sheet overlays the stage's lower half, so the stage's own
      // bottom-edge furniture — the horizontal rail, and now the section plate
      // — has to sit above whichever detent the sheet is at. Which detent that
      // is lives in this component; the stylesheet cannot see a class on a
      // sibling's descendant, and the alternative was a `:has()` selector
      // reaching across the tree for a fact the shell already knows (MRB-189).
      data-sheet={layout === 'phone' ? (sheetRaised ? 'raised' : 'rest') : undefined}
      data-detected-tier={probe.tier}
      // Points are COMPUTED and not persisted (MRB-191 scope): the reward
      // layer is MRB-148's, and the attempts contract is explicit (§3) that no
      // points column belongs on the row. They are not drawn either — §03 owns
      // how a result is presented, and that screen is deliberately not
      // improvised here. Surfaced only so the gates can read them.
      data-round-points={round ? points : undefined}
      data-round-gate={gate ?? undefined}
    >
      <TopBar
        layout={layout}
        mode={mode}
        onMode={(m) => (m === 'retrieve' ? enterRetrieval() : leaveRetrieval())}
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
            onMode={(m) => (m === 'retrieve' ? enterRetrieval() : leaveRetrieval())}
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
          {round && (
            <RetrievalPanel
              key="side"
              specimen={specimen}
              round={round}
              roundSize={roundSize}
              revealed={revealed}
              gate={gate}
              onCheck={(answer) =>
                respond(
                  question && isCorrectAnswer(answer, question.hotspot)
                    ? 'correct'
                    : 'wrong',
                  answer,
                )
              }
              onSkip={() => respond('skipped', '')}
              onReveal={() => respond('revealed', '')}
              onNext={() => setRevealed(null)}
            />
          )}
        </main>
      ) : layout === 'phone' ? (
        <main className="main">
          <div className="stagewrap" key="stage" style={{ flex: 1, position: 'relative' }}>
            {stage}
            <PhoneSheet
              rootRef={sheetRef}
              specimen={specimen}
              raised={sheetRaised}
              onRaisedChange={setSheetRaised}
              openHotspotId={openHotspotId}
              onOpenHotspot={setOpenHotspotId}
              onStartRetrieval={enterRetrieval}
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
            onStartRetrieval={enterRetrieval}
          />
        </main>
      ) : (
        <main className="main main--explore">
          <LibraryColumn
            key="library"
            selectedId={specimenId}
            onSelect={selectSpecimen}
            keyStage={keyStage}
          />
          <div className="stagewrap" key="stage">{stage}</div>
          <InfoPanel
            key="side"
            specimen={specimen}
            openHotspotId={openHotspotId}
            onOpenHotspot={setOpenHotspotId}
            onStartRetrieval={enterRetrieval}
          />
        </main>
      )}

      {libraryOpen && layout === 'tablet' && (
        <LibraryDrawer
          selectedId={specimenId}
          onSelect={selectSpecimen}
          onClose={() => setLibraryOpen(false)}
          keyStage={keyStage}
        />
      )}
      {libraryOpen && layout === 'phone' && (
        <LibraryFullScreen
          selectedId={specimenId}
          onSelect={selectSpecimen}
          onClose={() => setLibraryOpen(false)}
          keyStage={keyStage}
        />
      )}
    </div>
  )
}
