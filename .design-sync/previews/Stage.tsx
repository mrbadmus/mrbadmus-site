// The stage — the shell's own furniture (dark room or paper, hotspot layer,
// callout, tool rail, quality chip, hint line) with a renderer mounted into
// it. Driven here by the placeholder renderer the repo ships for exactly this
// purpose: plain DOM, synchronous, and it satisfies the whole Renderer
// contract, so the card shows the real stage rather than an empty room.
// Anatomy-shaped strings follow the frozen reference's placeholder convention;
// UI copy is real.
import { Stage, createPlaceholderRenderer } from 'mrbadmus-3d-studio'

type Tiers = ('foundation' | 'higher')[]
const both = ['foundation', 'higher'] as Tiers

// One renderer per cell — a shared instance would be mounted and unmounted by
// whichever card rendered last, and the others would come up empty.
const roomRenderer = createPlaceholderRenderer('viewport')
const calloutRenderer = createPlaceholderRenderer('viewport')
const paperRenderer = createPlaceholderRenderer('paper')

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
    { id: 'heart.item-01', label: 'Lorem ipsum', detail: 'Lorem ipsum dolor sit amet consectetur.', position3d: [0.1, 0.2, 0.3] as [number, number, number], position2d: [120, 90] as [number, number], tiers: both, retrievable: true },
    { id: 'heart.item-02', label: 'Dolor sit', detail: 'Consectetur adipiscing elit sed do eiusmod.', position3d: [0.2, 0.1, 0.4] as [number, number, number], position2d: [200, 60] as [number, number], tiers: both, retrievable: true },
    { id: 'heart.item-03', label: 'Amet consectetur', detail: 'Sed do eiusmod tempor incididunt ut labore et dolore magna.', position3d: [0.3, 0.3, 0.2] as [number, number, number], position2d: [160, 150] as [number, number], tiers: both, retrievable: true },
    { id: 'heart.item-04', label: 'Adipiscing elit', detail: 'Ut labore et dolore magna aliqua.', position3d: [0.15, 0.4, 0.1] as [number, number, number], position2d: [90, 170] as [number, number], tiers: both, retrievable: true },
  ],
}

// .stage is flex:1 / min-height:420 — it fills the frame the shell gives it
const frame: React.CSSProperties = {
  width: 760,
  height: 460,
  display: 'flex',
  padding: 12,
  background: '#15110C',
  borderRadius: 14,
}

const noop = () => {}

export const Viewport = () => (
  <div style={frame}>
    <Stage
      renderer={roomRenderer}
      stageKind="viewport"
      specimen={specimen}
      mode="explore"
      renderTier="A"
      quality="auto"
      detectedTier="A"
      onQuality={noop}
      openHotspotId={null}
      onOpenHotspot={noop}
      targetHotspotId={null}
      hint="Drag to rotate · click a dot to label"
    />
  </div>
)

export const StructureOpen = () => (
  <div style={frame}>
    <Stage
      renderer={calloutRenderer}
      stageKind="viewport"
      specimen={specimen}
      mode="explore"
      renderTier="A"
      quality="high"
      detectedTier="A"
      onQuality={noop}
      openHotspotId="heart.item-01"
      onOpenHotspot={noop}
      targetHotspotId={null}
      hint="Drag to rotate · click a dot to label"
    />
  </div>
)

export const FlatDiagram = () => (
  <div style={frame}>
    <Stage
      renderer={paperRenderer}
      stageKind="paper"
      specimen={specimen}
      mode="explore"
      renderTier="A"
      quality="auto"
      detectedTier="C"
      onQuality={noop}
      openHotspotId={null}
      onOpenHotspot={noop}
      targetHotspotId={null}
      hint="Click a dot to label"
    />
  </div>
)
