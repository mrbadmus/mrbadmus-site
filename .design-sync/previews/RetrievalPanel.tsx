// The §02 retrieval round panel, driven by a RoundState shaped exactly like
// studio/retrieval.ts builds one (MRB-191): a specimen-length queue, results
// accumulating in front of it, missed structures held for the tail.
// Anatomy-shaped strings mirror the frozen reference's own placeholder
// convention (no invented science — real strings arrive via Mide's Stage 8
// gate); UI copy is real.
import { RetrievalPanel } from 'mrbadmus-3d-studio'

type Tiers = ('foundation' | 'higher')[]
const both = ['foundation', 'higher'] as Tiers

const specimen = {
  id: 'heart',
  renderer: 'mesh' as const,
  name: 'Human heart',
  epithet: 'Lorem ipsum dolor sit amet',
  system: 'Circulatory',
  keyStages: ['KS3', 'KS4'] as ('KS3' | 'KS4')[],
  assets: {
    mesh: '/3d/assets/heart.glb',
    fallback: '/3d/assets/heart-2d.svg',
    thumbnail: '/3d/assets/heart-thumb.webp',
    licence: 'royalty-free-perpetual',
    source: 'Reference placeholder',
    acquired: '2026-08-09',
  },
  description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  keyFacts: [{ label: 'Lorem', value: '000 ipsum' }],
  callouts: { importance: 'Lorem ipsum dolor sit.', didYouKnow: 'Ut enim ad minim veniam.' },
  lessonUrl: '/biology/organisation.html',
  specPoints: ['KS4.B.ORG.04'],
  hotspots: [
    { id: 'heart.item-01', label: 'Lorem ipsum', detail: 'Lorem ipsum dolor sit amet.', position3d: [0.1, 0.2, 0.3] as [number, number, number], position2d: [120, 90] as [number, number], tiers: both, retrievable: true },
    { id: 'heart.item-02', label: 'Dolor sit', detail: 'Consectetur adipiscing elit sed.', position3d: [0.2, 0.1, 0.4] as [number, number, number], position2d: [200, 60] as [number, number], tiers: both, retrievable: true },
    { id: 'heart.item-03', label: 'Amet consectetur', detail: 'Sed do eiusmod tempor incididunt ut labore.', position3d: [0.3, 0.3, 0.2] as [number, number, number], position2d: [160, 150] as [number, number], tiers: both, retrievable: true, accept: ['Amet consect'] },
    { id: 'heart.item-04', label: 'Adipiscing elit', detail: 'Ut labore et dolore magna aliqua.', position3d: [0.15, 0.4, 0.1] as [number, number, number], position2d: [90, 170] as [number, number], tiers: both, retrievable: true },
    { id: 'heart.item-05', label: 'Tempor incid.', detail: 'Quis nostrud exercitation ullamco.', position3d: [0.25, 0.35, 0.3] as [number, number, number], position2d: [180, 200] as [number, number], tiers: ['higher'] as Tiers, retrievable: true },
    { id: 'heart.item-06', label: 'Magna aliqua', detail: 'Duis aute irure dolor in reprehenderit.', position3d: [0.05, 0.15, 0.25] as [number, number, number], position2d: [140, 230] as [number, number], tiers: both, retrievable: true },
    { id: 'heart.item-07', label: 'Veniam quis', detail: 'Excepteur sint occaecat cupidatat.', position3d: [0.35, 0.2, 0.15] as [number, number, number], position2d: [210, 130] as [number, number], tiers: both, retrievable: false },
  ],
}

const queue = specimen.hotspots
  .filter((h) => h.retrievable)
  .map((hotspot) => ({ hotspot, attemptNo: 1 }))

// specimen-length, as startRound builds it — six retrievable structures here,
// which is also the six squares the frozen reference draws
const roundSize = queue.length

const asking = {
  id: 'round-preview-01',
  specimenId: 'heart',
  queue,
  index: 2,
  results: [
    { hotspotId: 'heart.item-01', outcome: 'correct' as const, response: 'Lorem ipsum', latencyMs: 4200, attemptNo: 1 },
    { hotspotId: 'heart.item-02', outcome: 'wrong' as const, response: 'Dolor amet', latencyMs: 6100, attemptNo: 1 },
  ],
  missed: ['heart.item-02'],
  complete: false,
  askedAt: 0,
}

const finished = {
  ...asking,
  index: roundSize,
  results: [
    ...asking.results,
    { hotspotId: 'heart.item-03', outcome: 'correct' as const, response: 'Amet consect', latencyMs: 5200, attemptNo: 1 },
    { hotspotId: 'heart.item-04', outcome: 'correct' as const, response: 'Adipiscing elit', latencyMs: 3800, attemptNo: 1 },
    { hotspotId: 'heart.item-05', outcome: 'skipped' as const, response: '', latencyMs: null, attemptNo: 1 },
    { hotspotId: 'heart.item-06', outcome: 'correct' as const, response: 'Magna aliqua', latencyMs: 4600, attemptNo: 1 },
  ],
  missed: ['heart.item-02', 'heart.item-05'],
  complete: true,
}

// 404 × 660 — the reference's own §02 panel frame, on the room's ground
const frame: React.CSSProperties = {
  width: 404,
  height: 660,
  display: 'flex',
  padding: 16,
  background: '#15110C',
  borderRadius: 14,
}

const noop = () => {}

export const Asking = () => (
  <div style={frame}>
    <RetrievalPanel
      specimen={specimen}
      round={asking}
      roundSize={roundSize}
      revealed={null}
      onCheck={noop}
      onSkip={noop}
      onReveal={noop}
      onNext={noop}
      gate={null}
    />
  </div>
)

export const Named = () => (
  <div style={frame}>
    <RetrievalPanel
      specimen={specimen}
      round={asking}
      roundSize={roundSize}
      revealed={{
        label: 'Amet consectetur',
        detail: 'Sed do eiusmod tempor incididunt ut labore et dolore magna.',
      }}
      onCheck={noop}
      onSkip={noop}
      onReveal={noop}
      onNext={noop}
      gate={null}
    />
  </div>
)

export const RoundComplete = () => (
  <div style={frame}>
    <RetrievalPanel
      specimen={specimen}
      round={finished}
      roundSize={roundSize}
      revealed={null}
      onCheck={noop}
      onSkip={noop}
      onReveal={noop}
      onNext={noop}
      gate="sign-in"
    />
  </div>
)
