// Library — sidebar column (§01), tablet drawer (§04), phone full-screen
// (§05). Rows are driven by the content records from Stage 0; the rest of the
// approved v1 set renders at coming-soon treatment and is not selectable.
// Selecting a specimen is one action — it loads and the drawer closes, no
// confirm step (§04).

import { comingSoon, librarySize, specimens } from '../studio/content'
import { CloseIcon } from './icons'

function LibraryRows({
  selectedId,
  onSelect,
  big,
}: {
  selectedId: string
  onSelect: (id: string) => void
  big?: boolean
}) {
  const cardClass = big ? 'libcard libcard--big' : 'libcard'
  return (
    <>
      {specimens.map((s) => {
        const viewing = s.id === selectedId
        return (
          <button
            key={s.id}
            type="button"
            className={`${cardClass}${viewing ? ' is-viewing' : ''}`}
            aria-current={viewing || undefined}
            onClick={() => onSelect(s.id)}
          >
            <span className="libcard__thumb" aria-hidden="true" />
            <span className="libcard__text">
              <span className="libcard__name">{s.name}</span>
              <span className="libcard__meta">{viewing ? 'Viewing' : s.system}</span>
            </span>
          </button>
        )
      })}
      <div className="library__divider" aria-hidden="true" />
      {comingSoon.map((s) => (
        <div key={s.name} className={`${cardClass} is-soon`}>
          <span className="libcard__thumb" aria-hidden="true" />
          <span className="libcard__text">
            <span className="libcard__name">{s.name}</span>
            <span className="libcard__meta">{s.system} · Soon</span>
          </span>
        </div>
      ))}
    </>
  )
}

/** Desktop column (§01) */
export function LibraryColumn({
  selectedId,
  onSelect,
}: {
  selectedId: string
  onSelect: (id: string) => void
}) {
  return (
    <aside className="library" aria-label="Specimen library">
      <div className="library__head">
        <span className="eyebrow">Library</span>
        <span className="library__count">{librarySize}</span>
      </div>
      <div className="library__list">
        <LibraryRows selectedId={selectedId} onSelect={onSelect} />
      </div>
    </aside>
  )
}

/** Tablet drawer (§04): 372pt, scrim at 42%, closes on select */
export function LibraryDrawer({
  selectedId,
  onSelect,
  onClose,
}: {
  selectedId: string
  onSelect: (id: string) => void
  onClose: () => void
}) {
  return (
    <>
      <button type="button" className="scrim" aria-label="Close library" onClick={onClose} />
      <div className="drawer" role="dialog" aria-label="Specimen library">
        <div className="drawer__head">
          <span className="drawer__title">Library</span>
          <span className="drawer__count">{librarySize}</span>
          <button type="button" className="drawer__close" aria-label="Close" onClick={onClose}>
            <CloseIcon />
          </button>
        </div>
        <div className="drawer__list">
          <LibraryRows
            big
            selectedId={selectedId}
            onSelect={(id) => {
              onSelect(id)
              onClose()
            }}
          />
        </div>
      </div>
    </>
  )
}

/** Phone full-screen library (§05): not a half sheet */
export function LibraryFullScreen({
  selectedId,
  onSelect,
  onClose,
}: {
  selectedId: string
  onSelect: (id: string) => void
  onClose: () => void
}) {
  return (
    <div className="phonelib" role="dialog" aria-label="Specimen library">
      <div className="phonelib__head">
        <button type="button" className="phonelib__close" aria-label="Close" onClick={onClose}>
          <CloseIcon color="#FBF3E6" />
        </button>
        <span className="phonelib__title">Library</span>
        <span className="drawer__count">{librarySize}</span>
      </div>
      <div className="phonelib__list">
        <LibraryRows
          big
          selectedId={selectedId}
          onSelect={(id) => {
            onSelect(id)
            onClose()
          }}
        />
      </div>
      <div className="phonelib__foot">
        <span className="phonelib__note">More specimens soon</span>
        <a className="phonelib__cta" href="/auth.html">Create account</a>
      </div>
    </div>
  )
}
