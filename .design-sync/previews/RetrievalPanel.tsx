// The §02 retrieval question panel — free recall first: typed answer,
// Reveal demoted below the fold of the decision. Structure only in Stage 1.
import { RetrievalPanel } from 'mrbadmus-3d-studio'

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
    { id: 'heart.item-01', label: 'Lorem ipsum', detail: 'Lorem ipsum dolor.', position3d: [0.1, 0.2, 0.3] as [number, number, number], position2d: [120, 90] as [number, number], tiers: ['foundation', 'higher'] as ('foundation' | 'higher')[], retrievable: true },
  ],
}

export const RoundInProgress = () => (
  <div
    style={{
      width: 404,
      height: 660,
      display: 'flex',
      padding: 16,
      background: '#15110C',
      borderRadius: 14,
    }}
  >
    <RetrievalPanel specimen={specimen} targetIndex={2} roundSize={6} />
  </div>
)
