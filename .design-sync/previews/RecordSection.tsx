// The §01 panel's Record section — the provenance block, reduced by MRB-186
// to the one row that is the student's business. Composed inside the panel
// that owns it, which is the only place it is ever rendered and the only
// context in which its rule and fact styling read correctly.
// Anatomy-shaped strings follow the frozen reference's placeholder
// convention; UI copy is real.
import { RecordSection } from 'mrbadmus-3d-studio'

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
  hotspots: [],
}

export const InPanel = () => (
  <div style={{ width: 372, height: 148, display: 'flex' }}>
    <aside className="panel" aria-label="Specimen information">
      <div className="panel__scroll">
        <RecordSection specimen={specimen} />
      </div>
    </aside>
  </div>
)
