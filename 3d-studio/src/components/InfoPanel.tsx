// Info panel — renders the student-facing fields of the specimen record.
// Content strings are Stage 0 placeholders and render exactly as-is: no lorem,
// no invented anatomy — every science string goes through Mide's gate at
// Stage 8. Sidebar label, stage caption and panel heading all derive from the
// one `name` field (spec §3.2).
//
// IT NO LONGER RENDERS EVERY FIELD, and that is the point. Stage 1 took
// "every field" as the acceptance and so put renderer, licence, source and
// acquired on the page. Ruled out on MRB-186: a student revising the heart has
// no use for any of them, and `RENDERER: mesh` is the platform narrating its
// own internals on a page whose job is to teach biology — the standing copy
// rule that student-facing pages carry no explanatory meta-text about how the
// platform works. Provenance is not deleted, it moved: `docs/3d_studio_asset_
// manifest.md`, generated from the same content records by
// tools/asset_manifest.py, is where a school's procurement question is
// answered. Spec points went with them (see RecordSection).

import type { KeyStage, SpecimenRecord } from '../studio/types'
import { offersLesson } from '../studio/content'
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

/**
 * The way out to the lesson — or nothing at all.
 *
 * TWO SEPARATE ABSENCES, and they are not the same thing:
 *
 *   `offersLesson(keyStage)` false → the control is NOT RENDERED. A KS3 viewer
 *     is not offered a triple-higher GCSE page (see `offersLesson`). Returning
 *     null here rather than at four call sites is what keeps the desktop panel,
 *     the tablet panel, the phone sheet and the sheet foot from drifting apart.
 *
 *   a TODO `lessonUrl` → the control renders and is DISABLED. That is the
 *     pre-acquisition state: the lesson exists as an intention, the record has
 *     not been pointed at it yet, and the disabled control carries the TODO in
 *     its title so it is visible to whoever is authoring. Dead for the heart
 *     since spec §11's map landed; still the right behaviour for the seven
 *     specimens that follow it.
 */
export function LessonLink({
  specimen,
  keyStage,
  className,
  children,
}: {
  specimen: SpecimenRecord
  keyStage: KeyStage | null
  className: string
  children: React.ReactNode
}) {
  if (!offersLesson(keyStage)) return null
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

/**
 * The one record field that is real content: which body system the specimen
 * belongs to. Circulatory, Digestive, and so on — a student answers with it.
 *
 * WHAT LEFT, AND WHERE IT WENT (MRB-186):
 *   renderer, licence, source, acquired → docs/3d_studio_asset_manifest.md,
 *   generated by tools/asset_manifest.py from these same records.
 *   spec points                         → the same manifest, per hotspot.
 *
 * Spec points are the judgement call of the three. They went for two reasons.
 * The ruling is that if they stay they belong on a teacher-facing surface
 * rather than the default student view, and no teacher surface exists yet — so
 * keeping them here keeps them in the one place the ruling excludes. And
 * MRB-193 made the specimen-level array a FALLBACK: a hotspot may now declare
 * its own, and where it does, it wins. A single specimen-level list in the
 * panel would therefore state something untrue about every structure that
 * overrides it — the row would not merely be surplus, it would be wrong.
 */
export function RecordSection({ specimen }: { specimen: SpecimenRecord }) {
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
      </div>
    </>
  )
}

/** Desktop right-hand panel (§01) */
export function InfoPanel({
  specimen,
  keyStage,
  openHotspotId,
  onOpenHotspot,
  onStartRetrieval,
}: {
  specimen: SpecimenRecord
  /** whose key stage decides whether the lesson link is offered (spec §11) */
  keyStage: KeyStage | null
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
        <RecordSection specimen={specimen} />
      </div>
      <div className="panel__foot">
        <LessonLink specimen={specimen} keyStage={keyStage} className="btn btn--outline">
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
  keyStage,
  openHotspotId,
  onOpenHotspot,
  onStartRetrieval,
}: {
  specimen: SpecimenRecord
  /** whose key stage decides whether the lesson link is offered (spec §11) */
  keyStage: KeyStage | null
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
          <LessonLink specimen={specimen} keyStage={keyStage} className="btn btn--outline">
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
      <RecordSection specimen={specimen} />
    </section>
  )
}

/** Phone sheet body content — the full record, scrollable; the sheet chrome
 * itself lives in PhoneSheet (§05) */
export function SheetContent({
  specimen,
  keyStage,
  openHotspotId,
  onOpenHotspot,
}: {
  specimen: SpecimenRecord
  /** whose key stage decides whether the lesson link is offered (spec §11) */
  keyStage: KeyStage | null
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
      {/* The divider goes with the link it heads. A "Related lesson" rule
          standing over nothing is worse than no rule: it reads as content that
          failed to load rather than as content this viewer is not offered. */}
      {offersLesson(keyStage) && (
        <>
          <div className="sectionrule">
            <span className="eyebrow">Related lesson</span>
            <span className="sectionrule__line" aria-hidden="true" />
          </div>
          <LessonLink specimen={specimen} keyStage={keyStage} className="lessonrow">
            <span className="lessonrow__thumb" aria-hidden="true" />
            <span>
              <span className="lessonrow__title">{specimen.name}</span>
              <span className="lessonrow__meta">{specimen.keyStages.join(' · ')}</span>
            </span>
            <span className="lessonrow__arrow" aria-hidden="true">
              <ArrowIcon size={18} />
            </span>
          </LessonLink>
        </>
      )}
      <RecordSection specimen={specimen} />
      <div style={{ height: 16 }} aria-hidden="true" />
    </>
  )
}
