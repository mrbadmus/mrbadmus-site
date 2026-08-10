// The §01 desktop info panel, fed a specimen record shaped exactly like the
// Stage 0 content schema. Anatomy-shaped strings mirror the frozen
// reference's own placeholder convention (no invented science — real
// strings arrive via Mide's Stage 8 gate); UI copy is real.
import { InfoPanel } from 'mrbadmus-3d-studio'

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
  description:
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim.',
  keyFacts: [
    { label: 'Lorem', value: '000 ipsum' },
    { label: 'Dolor sit', value: '0.0 × 0.0 amet' },
    { label: 'Consectetur', value: 'Lorem adipiscing' },
    { label: 'Eiusmod', value: '00 tempor' },
  ],
  callouts: {
    importance:
      'Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt.',
    didYouKnow:
      'Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi.',
  },
  lessonUrl: '/biology/organisation.html',
  specPoints: ['KS4.B.ORG.04', 'KS3.B.BOD.02'],
  hotspots: [
    { id: 'heart.item-01', label: 'Lorem ipsum', detail: 'Lorem ipsum dolor sit amet.', position3d: [0.1, 0.2, 0.3] as [number, number, number], position2d: [120, 90] as [number, number], tiers: ['foundation', 'higher'] as ('foundation' | 'higher')[], retrievable: true },
    { id: 'heart.item-02', label: 'Dolor sit', detail: 'Consectetur adipiscing elit sed.', position3d: [0.2, 0.1, 0.4] as [number, number, number], position2d: [200, 60] as [number, number], tiers: ['foundation', 'higher'] as ('foundation' | 'higher')[], retrievable: true },
    { id: 'heart.item-03', label: 'Amet consect.', detail: 'Sed do eiusmod tempor incididunt.', position3d: [0.3, 0.3, 0.2] as [number, number, number], position2d: [160, 150] as [number, number], tiers: ['higher'] as ('foundation' | 'higher')[], retrievable: true },
    { id: 'heart.item-04', label: 'Adipiscing', detail: 'Ut labore et dolore magna aliqua.', position3d: [0.15, 0.4, 0.1] as [number, number, number], position2d: [90, 170] as [number, number], tiers: ['foundation', 'higher'] as ('foundation' | 'higher')[], retrievable: false },
  ],
}

// 740pt — the reference's own panel height (§01)
const frame: React.CSSProperties = { width: 372, height: 740, display: 'flex' }

export const Resting = () => (
  <div style={frame}>
    <InfoPanel
      specimen={specimen}
      openHotspotId={null}
      onOpenHotspot={() => {}}
      onStartRetrieval={() => {}}
    />
  </div>
)

export const StructureOpen = () => (
  <div style={frame}>
    <InfoPanel
      specimen={specimen}
      openHotspotId="heart.item-03"
      onOpenHotspot={() => {}}
      onStartRetrieval={() => {}}
    />
  </div>
)
