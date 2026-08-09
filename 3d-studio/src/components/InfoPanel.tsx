// Info panel — renders EVERY field of the specimen record (MRB-186
// acceptance). Content strings are Stage 0 placeholders and render exactly
// as-is: no lorem, no invented anatomy — every science string goes through
// Mide's gate at Stage 8. Sidebar label, stage caption and panel heading all
// derive from the one `name` field (spec §3.2).

import type { SpecimenRecord } from '../studio/types'
import { ArrowIcon } from './icons'

function isPlaceholder(value: string): boolean {
  return value.startsWith('TODO')
}

export function PanelChips({ specimen }: { specimen: SpecimenRecord }) {
  return (
    <div className="panel__chips">
      {specimen.keyStages.map((ks) => (
        <span key={ks} className="kchip">
          {ks === 'KS4' ? 'KS4 AQA' : ks}
        </span>
      ))}
      <span className="kchip kchip--accent">
        {specimen.hotspots.length} structure{specimen.hotspots.length === 1 ? '' : 's'}
      </span>
    </div>
  )
}

export function TitleBlock({ specimen, size }: { specimen: SpecimenRecord; size?: 'sheet' }) {
  return (
    <>
      <h1 className="panel__name" style={size === 'sheet' ? undefined : undefined}>
        {specimen.name}
      </h1>
      <p className="panel__epithet">{specimen.epithet}</p>
    </>
  )
}

export function StructuresSection({
  specimen,
  openHotspotId,
  onOpenHotspot,
}: {
  specimen: SpecimenRecord
  openHotspotId: string | null
  onOpenHotspot: (id: string | null) => void
}) {
  return (
    <>
      <div className="sectionrule">
        <span className="eyebrow">Structures</span>
        <span className="sectionrule__line" aria-hidden="true" />
        <span className="sectionrule__count">{openHotspotId ? '1 SHOWN' : '0 SHOWN'}</span>
      </div>
      <div className="structures">
        {specimen.hotspots.map((h, index) => {
          const numeral = String(index + 1).padStart(2, '0')
          const open = h.id === openHotspotId
          return (
            <button
              key={h.id}
              type="button"
              className={`structchip${open ? ' is-open' : ''}`}
              onClick={() => onOpenHotspot(open ? null : h.id)}
            >
              <span className="structchip__num">{numeral}</span>
              <span className="structchip__label">{h.label}</span>
            </button>
          )
        })}
      </div>
    </>
  )
}

export function KeyFactsSection({ specimen }: { specimen: SpecimenRecord }) {
  return (
    <>
      <div className="sectionrule">
        <span className="eyebrow">Key facts</span>
        <span className="sectionrule__line" aria-hidden="true" />
      </div>
      <div className="facts">
        {specimen.keyFacts.map((fact, i) => (
          <div key={i} className="fact">
            <span className="fact__label">{fact.label}</span>
            <span className="fact__value">{fact.value}</span>
          </div>
        ))}
      </div>
    </>
  )
}

export function Callouts({ specimen }: { specimen: SpecimenRecord }) {
  return (
    <>
      <div className="matters">
        <div className="matters__eyebrow">WHY IT MATTERS</div>
        <div className="matters__body">{specimen.callouts.importance}</div>
      </div>
      <div className="didyouknow">
        <div className="didyouknow__eyebrow">DID YOU KNOW</div>
        <div className="didyouknow__body">{specimen.callouts.didYouKnow}</div>
      </div>
    </>
  )
}

export function LessonLink({
  specimen,
  className,
  children,
}: {
  specimen: SpecimenRecord
  className: string
  children: React.ReactNode
}) {
  const placeholder = isPlaceholder(specimen.lessonUrl)
  return (
    <a
      className={className}
      href={placeholder ? '#' : specimen.lessonUrl}
      aria-disabled={placeholder || undefined}
      onClick={placeholder ? (e) => e.preventDefault() : undefined}
      title={placeholder ? specimen.lessonUrl : undefined}
    >
      {children}
    </a>
  )
}

/** Remaining record fields with no drawn slot in the reference — rendered
 * (acceptance: every field), quietly, as provenance rows. */
export function ProvenanceSection({ specimen }: { specimen: SpecimenRecord }) {
  return (
    <>
      <div className="sectionrule">
        <span className="eyebrow">Record</span>
        <span className="sectionrule__line" aria-hidden="true" />
      </div>
      <div className="facts">
        <div className="fact">
          <span className="fact__label">System</span>
          <span className="fact__value">{specimen.system}</span>
        </div>
        <div className="fact">
          <span className="fact__label">Spec points</span>
          <span className="fact__value">{specimen.specPoints.join(', ')}</span>
        </div>
        <div className="fact">
          <span className="fact__label">Renderer</span>
          <span className="fact__value">{specimen.renderer}</span>
        </div>
        <div className="fact">
          <span className="fact__label">Licence</span>
          <span className="fact__value">{specimen.assets.licence}</span>
        </div>
        <div className="fact">
          <span className="fact__label">Source</span>
          <span className="fact__value">{specimen.assets.source}</span>
        </div>
        <div className="fact">
          <span className="fact__label">Acquired</span>
          <span className="fact__value">{specimen.assets.acquired}</span>
        </div>
      </div>
    </>
  )
}

/** Desktop right-hand panel (§01) */
export function InfoPanel({
  specimen,
  openHotspotId,
  onOpenHotspot,
  onStartRetrieval,
}: {
  specimen: SpecimenRecord
  openHotspotId: string | null
  onOpenHotspot: (id: string | null) => void
  onStartRetrieval: () => void
}) {
  return (
    <aside className="panel" aria-label="Specimen information">
      <div className="panel__scroll">
        <PanelChips specimen={specimen} />
        <TitleBlock specimen={specimen} />
        <p className="panel__desc">{specimen.description}</p>
        <StructuresSection
          specimen={specimen}
          openHotspotId={openHotspotId}
          onOpenHotspot={onOpenHotspot}
        />
        <KeyFactsSection specimen={specimen} />
        <Callouts specimen={specimen} />
        <ProvenanceSection specimen={specimen} />
      </div>
      <div className="panel__foot">
        <LessonLink specimen={specimen} className="btn btn--outline">
          Open lesson
        </LessonLink>
        <button type="button" className="btn btn--primary" onClick={onStartRetrieval}>
          Start retrieval
        </button>
      </div>
    </aside>
  )
}

/** Tablet panel: flows under the stage, two columns, actions beside the
 * title so they stay above the fold (§04) */
export function TabletPanel({
  specimen,
  openHotspotId,
  onOpenHotspot,
  onStartRetrieval,
}: {
  specimen: SpecimenRecord
  openHotspotId: string | null
  onOpenHotspot: (id: string | null) => void
  onStartRetrieval: () => void
}) {
  return (
    <section className="tpanel" aria-label="Specimen information">
      <div className="tpanel__top">
        <div className="tpanel__title">
          <PanelChips specimen={specimen} />
          <TitleBlock specimen={specimen} />
        </div>
        <div className="tpanel__actions">
          <LessonLink specimen={specimen} className="btn btn--outline">
            Open lesson
          </LessonLink>
          <button type="button" className="btn btn--primary" onClick={onStartRetrieval}>
            Start retrieval
          </button>
        </div>
      </div>
      <p className="tpanel__desc">{specimen.description}</p>
      <div className="tpanel__cols">
        <div>
          <StructuresSection
            specimen={specimen}
            openHotspotId={openHotspotId}
            onOpenHotspot={onOpenHotspot}
          />
        </div>
        <div>
          <KeyFactsSection specimen={specimen} />
        </div>
      </div>
      <Callouts specimen={specimen} />
      <ProvenanceSection specimen={specimen} />
    </section>
  )
}

/** Phone sheet body content — the full record, scrollable; the sheet chrome
 * itself lives in PhoneSheet (§05) */
export function SheetContent({
  specimen,
  openHotspotId,
  onOpenHotspot,
}: {
  specimen: SpecimenRecord
  openHotspotId: string | null
  onOpenHotspot: (id: string | null) => void
}) {
  return (
    <>
      <PanelChips specimen={specimen} />
      <TitleBlock specimen={specimen} size="sheet" />
      <p className="panel__desc">{specimen.description}</p>
      <StructuresSection
        specimen={specimen}
        openHotspotId={openHotspotId}
        onOpenHotspot={onOpenHotspot}
      />
      <KeyFactsSection specimen={specimen} />
      <Callouts specimen={specimen} />
      <div className="sectionrule">
        <span className="eyebrow">Related lesson</span>
        <span className="sectionrule__line" aria-hidden="true" />
      </div>
      <LessonLink specimen={specimen} className="lessonrow">
        <span className="lessonrow__thumb" aria-hidden="true" />
        <span>
          <span className="lessonrow__title">{specimen.name}</span>
          <span className="lessonrow__meta">{specimen.keyStages.join(' · ')}</span>
        </span>
        <span className="lessonrow__arrow" aria-hidden="true">
          <ArrowIcon size={18} />
        </span>
      </LessonLink>
      <ProvenanceSection specimen={specimen} />
      <div style={{ height: 16 }} aria-hidden="true" />
    </>
  )
}
