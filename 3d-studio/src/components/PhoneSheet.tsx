// §05 phone sheet — two detents (rest / raised); the stage never fully
// leaves: at the raised detent 150pt of stage stays visible so the model
// keeps its context. Start retrieval is pinned at every detent; the lesson
// link shrinks to a glyph beside it.

import { useRef } from 'react'
import type { SpecimenRecord } from '../studio/types'
import { SheetContent, LessonLink } from './InfoPanel'
import { BookIcon } from './icons'

export function PhoneSheet({
  specimen,
  raised,
  onRaisedChange,
  openHotspotId,
  onOpenHotspot,
  onStartRetrieval,
}: {
  specimen: SpecimenRecord
  raised: boolean
  onRaisedChange: (raised: boolean) => void
  openHotspotId: string | null
  onOpenHotspot: (id: string | null) => void
  onStartRetrieval: () => void
}) {
  const dragStartY = useRef<number | null>(null)

  return (
    <div className={`sheet${raised ? ' is-raised' : ''}`}>
      <button
        type="button"
        className="sheet__grab"
        aria-label={raised ? 'Lower panel' : 'Raise panel'}
        onClick={() => onRaisedChange(!raised)}
        onPointerDown={(e) => {
          dragStartY.current = e.clientY
        }}
        onPointerUp={(e) => {
          const start = dragStartY.current
          dragStartY.current = null
          if (start === null) return
          const dy = e.clientY - start
          if (dy < -24) onRaisedChange(true)
          else if (dy > 24) onRaisedChange(false)
        }}
      >
        <span className="sheet__handle" aria-hidden="true" />
      </button>
      <div className="sheet__body">
        <SheetContent
          specimen={specimen}
          openHotspotId={openHotspotId}
          onOpenHotspot={onOpenHotspot}
        />
      </div>
      <div className="sheet__foot">
        <LessonLink specimen={specimen} className="lessonglyph">
          <BookIcon />
        </LessonLink>
        <button type="button" className="btn btn--primary" onClick={onStartRetrieval}>
          Start retrieval
        </button>
      </div>
    </div>
  )
}
