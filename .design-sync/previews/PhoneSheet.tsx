// The §05 phone sheet — two detents; at rest here. The stage never fully
// leaves on the real screen; the sheet pins Start retrieval at every detent
// with the lesson link shrunk to a glyph beside it.
import { PhoneSheet } from 'mrbadmus-3d-studio'

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
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.',
  keyFacts: [
    { label: 'Lorem', value: '000 ipsum' },
    { label: 'Dolor sit', value: '0.0 × 0.0 amet' },
    { label: 'Eiusmod', value: '00 tempor' },
  ],
  callouts: {
    importance: 'Lorem ipsum dolor sit amet consectetur adipiscing elit.',
    didYouKnow: 'Ut enim ad minim veniam quis nostrud exercitation.',
  },
  lessonUrl: '/biology/organisation.html',
  specPoints: ['KS4.B.ORG.04', 'KS3.B.BOD.02'],
  hotspots: [
    { id: 'heart.item-01', label: 'Lorem ipsum', detail: 'Lorem ipsum dolor sit amet.', position3d: [0.1, 0.2, 0.3] as [number, number, number], position2d: [120, 90] as [number, number], tiers: ['foundation', 'higher'] as ('foundation' | 'higher')[], retrievable: true },
    { id: 'heart.item-02', label: 'Dolor sit', detail: 'Consectetur adipiscing elit sed.', position3d: [0.2, 0.1, 0.4] as [number, number, number], position2d: [200, 60] as [number, number], tiers: ['higher'] as ('foundation' | 'higher')[], retrievable: true },
    { id: 'heart.item-03', label: 'Amet consect.', detail: 'Sed do eiusmod tempor.', position3d: [0.3, 0.3, 0.2] as [number, number, number], position2d: [160, 150] as [number, number], tiers: ['foundation', 'higher'] as ('foundation' | 'higher')[], retrievable: false },
  ],
}

const phone: React.CSSProperties = {
  position: 'relative',
  width: 390,
  height: 700,
  borderRadius: 22,
  overflow: 'hidden',
  border: '1px solid #D9C9AC',
  background: 'radial-gradient(95% 80% at 50% 42%, #2C261F 0%, #191510 55%, #100D0A 100%)',
}

export const SheetAtRest = () => (
  <div style={phone}>
    <PhoneSheet
      specimen={specimen}
      raised={false}
      onRaisedChange={() => {}}
      openHotspotId={null}
      onOpenHotspot={() => {}}
      onStartRetrieval={() => {}}
    />
  </div>
)

export const SheetRaised = () => (
  <div style={phone}>
    <PhoneSheet
      specimen={specimen}
      raised={true}
      onRaisedChange={() => {}}
      openHotspotId={null}
      onOpenHotspot={() => {}}
      onStartRetrieval={() => {}}
    />
  </div>
)
