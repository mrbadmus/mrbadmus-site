// The section slider and the rule that marks the plane — reference §09 and
// §10 of `crosssection-v1.html` (MRB-189).
//
// Stage 4 built a plain range input here and flagged it for Design, because
// §01–§07 never show the cross-section engaged and so drew no control for
// where the plane sits. Design has now drawn it, and this is the translation.
//
// WHAT THE DRAWING DECIDES, and why each one is not an implementation detail:
//
//   THE HANDLE IS A BAR, NOT A KNOB. "The thing it moves is a plane. It reads
//   as the plane's edge seen end-on, and the shape alone distinguishes it from
//   every round hotspot on the stage." Cream fill, dark 2px ring — the hotspot
//   construction, inherited rather than argued again, because that pairing is
//   what survived the washed-projector test.
//
//   DRAG EMPHASIS LANDS ON THE CUT, NOT ON THE FURNITURE. Dragging thickens
//   the handle, hatches the travelled track to match the cut face, promotes
//   the readout from caption to 15px, and brings the plane rule to full
//   strength. Four changes, three of them quiet.
//
//   NO LEADER LINE from the handle to the cut, though §01 draws one from a
//   hotspot to its callout. The handle's x and the plane's x do not genuinely
//   coincide, so a connector would be a lie — the drag emphasis on the plane
//   is what replaces it.
//
//   NO LIGHT-GROUND VARIANT. Retrieval keeps the stage dark, and the flat
//   renderer does not declare `cross-section` at all, so a light-ground state
//   cannot occur and is not drawn. Do not add one.
//
//   KEYBOARD OPERABILITY IS DRAWN, SO IT IS REQUIRED. §10's fourth state is
//   the keyboard one: arrows step 2%, the handle takes a notch, the plate
//   takes a visible focus ring. A native range input carries all of that
//   correctly — name, value announcement, arrow stepping — so it is still the
//   control underneath; it is made transparent and the drawn parts are laid
//   over it, rather than a div being taught to be a slider.

import { useEffect, useState } from 'react'
import { RULE_EDGE_ON_FLOOR, RULE_EDGE_ON_FULL, type Renderer } from '../renderer/types'

export type StageLayout = 'desktop' | 'tablet' | 'phone'

/** §10: "ARROWS STEP 2%". */
const KEY_STEP = 0.02

/** How strong the plane rule is when nobody is touching the slider. Full
 * strength is the drag state (§09). */
const RULE_REST_STRENGTH = 0.75

export function SectionPlate({
  renderer,
  layout,
  onChange,
}: {
  renderer: Renderer
  layout: StageLayout
  onChange: () => void
}) {
  const [dragging, setDragging] = useState(false)
  const [keyed, setKeyed] = useState(false)

  // A pointer released outside the input still ends the drag. Without this the
  // plate stays in its dragging state until the next press, which reads as the
  // cut still being worked on when it is not.
  useEffect(() => {
    if (!dragging) return
    const end = () => setDragging(false)
    window.addEventListener('pointerup', end)
    window.addEventListener('pointercancel', end)
    return () => {
      window.removeEventListener('pointerup', end)
      window.removeEventListener('pointercancel', end)
    }
  }, [dragging])

  const state = renderer.toolState('cross-section')
  const active = state?.active === true

  // The tool went away under a live drag — a mode change, a new specimen, or
  // the student tapping the collapsed tool on phone.
  useEffect(() => {
    if (!active && dragging) setDragging(false)
  }, [active, dragging])

  if (!active) return null

  const offset = state?.offset ?? 0.5
  const percent = Math.round(offset * 100)
  const pct = `${offset * 100}%`

  // On phone the readout cannot stay in the bar: a thumb covers it. It lifts
  // to the stage's top-left corner, opposite the quality chip, and only while
  // dragging (§09).
  const readoutLifts = layout === 'phone' && dragging

  return (
    <>
      <PlaneRule renderer={renderer} dragging={dragging} />

      {readoutLifts && (
        <div className="secreadout">
          <span className="secreadout__word">SECTION</span>
          <span className="secreadout__value">{percent}%</span>
        </div>
      )}

      <div
        className="secplate"
        data-drag={dragging ? '' : undefined}
        data-key={keyed ? '' : undefined}
        data-percent={percent}
      >
        {/* The eyebrow is the plate's only label. §08: "no legend · no key ·
            label reads SECTION". It goes on phone, where the bar is shared
            with the rail and the width belongs to the track. */}
        {layout !== 'phone' && <span className="secplate__word">SECTION</span>}

        <span className="secplate__track">
          <span className="secplate__travel" style={{ width: pct }} aria-hidden="true" />
          <span className="secplate__handle" style={{ left: pct }} aria-hidden="true">
            <span className="secplate__notch" />
          </span>
          <input
            className="secplate__input"
            type="range"
            min={0}
            max={1}
            step={KEY_STEP}
            value={offset}
            aria-label="Cross-section position"
            aria-valuetext={`${percent} per cent`}
            onPointerDown={() => setDragging(true)}
            onPointerUp={() => setDragging(false)}
            // :focus-visible rather than :focus, so a pointer press does not
            // also raise the keyboard state — §10 draws them as two states.
            onFocus={(e) => setKeyed(e.currentTarget.matches(':focus-visible'))}
            onBlur={() => setKeyed(false)}
            onChange={(e) => {
              renderer.setSectionOffset(Number(e.target.value))
              onChange()
            }}
          />
        </span>

        {!readoutLifts && <span className="secplate__value">{percent}%</span>}
      </div>
    </>
  )
}

/** The accent rule through the specimen, with its end ticks.
 *
 * This is the ONLY place the accent appears in the cross-section treatment
 * (§08: "Orange comes off the organ entirely. It marks the plane … because the
 * plane is the interactive thing. Tissue is substance and never highlights
 * itself"). The renderer decides where it goes and whether it can honestly be
 * drawn at all; see `sectionRule` in `renderer/mesh/section.ts` for why a plane
 * seen face-on has no line to draw.
 */
function PlaneRule({ renderer, dragging }: { renderer: Renderer; dragging: boolean }) {
  const [, setTick] = useState(0)

  // The rule follows a camera the shell does not own, exactly as the hotspot
  // dots do, so it samples on the same schedule they do.
  useEffect(() => {
    let frame = 0
    const sample = () => {
      setTick((t) => t + 1)
      frame = requestAnimationFrame(sample)
    }
    frame = requestAnimationFrame(sample)
    return () => cancelAnimationFrame(frame)
  }, [renderer])

  const rule = renderer.sectionRule()
  if (!rule) return null

  // Fade in over the band where the plane stops being face-on, so the rule
  // arrives as the specimen turns rather than popping into existence.
  const edge = Math.min(
    1,
    (rule.edgeOn - RULE_EDGE_ON_FLOOR) / (RULE_EDGE_ON_FULL - RULE_EDGE_ON_FLOOR),
  )
  const strength = Math.max(0, edge) * (dragging ? 1 : RULE_REST_STRENGTH)
  if (strength <= 0) return null

  return (
    <div
      className="planerule"
      data-drag={dragging ? '' : undefined}
      style={{
        left: rule.x,
        top: rule.y,
        height: rule.length + 2 * RULE_TICK_REACH,
        opacity: strength,
        transform: `translate(-50%, -50%) rotate(${rule.angle}deg)`,
      }}
      aria-hidden="true"
    >
      <span className="planerule__tick planerule__tick--start" />
      <span className="planerule__tick planerule__tick--end" />
    </div>
  )
}

/** How far past the specimen each end of the rule reaches, where its tick
 * sits. 34px in the reference's 1440 drawing. */
const RULE_TICK_REACH = 34
