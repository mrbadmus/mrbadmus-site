// Gate 2 — no hue-only meaning. Design's claim (§07): "Size, fill inversion
// and the numeral do the work. Remove the orange entirely and every state is
// still distinct." This test removes hue by collapsing every fill to its
// greyscale luminance, then asserts every pair of hotspot states is still
// distinguishable by size, by luminance class (light fill / dark fill / no
// fill), or by glyph. It renders the real component under a greyscale filter
// and reads the rendered values, so a styling regression fails here.

import { readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { describe, expect, it } from 'vitest'
import { render } from '@testing-library/react'
import {
  HotspotDot,
  hotspotVisual,
  type HotspotState,
  type HotspotSurface,
} from '../../src/components/HotspotDot'

const STATES: HotspotState[] = ['closed', 'hover', 'open', 'inert', 'target']
const SURFACES: HotspotSurface[] = ['dark', 'paper']

/** Rec. 601 luma of a CSS colour — hue is discarded, exactly what a greyscale
 * filter does. */
function luminance(color: string): number | null {
  if (color === 'transparent' || color === '') return null
  const hex = color.match(/^#([0-9a-f]{6})$/i)
  if (hex) {
    const n = parseInt(hex[1], 16)
    return (0.299 * (n >> 16) + 0.587 * ((n >> 8) & 255) + 0.114 * (n & 255)) / 255
  }
  const rgb = color.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/)
  if (rgb) {
    if (rgb[4] !== undefined && parseFloat(rgb[4]) === 0) return null
    return (0.299 * +rgb[1] + 0.587 * +rgb[2] + 0.114 * +rgb[3]) / 255
  }
  return null
}

// Three legible greyscale bands: near-black, mid-grey, near-white. A washed
// projector still separates these (§07 projection floor).
type FillClass = 'none' | 'dark' | 'mid' | 'light'

function fillClass(background: string): FillClass {
  const l = luminance(background)
  if (l === null) return 'none'
  if (l < 0.25) return 'dark'
  if (l > 0.6) return 'light'
  return 'mid'
}

interface GreyscaleSignature {
  size: number
  fill: FillClass
  glyph: string
}

function signature(state: HotspotState, surface: HotspotSurface): GreyscaleSignature {
  // Render the real component under a greyscale filter and read back what a
  // colour-blind projector actually gets.
  const { container, unmount } = render(
    <div style={{ filter: 'grayscale(1)' }}>
      <HotspotDot state={state} surface={surface} numeral="01" />
    </div>,
  )
  const dot = container.querySelector('.hotspot') as HTMLElement
  expect(dot, `${surface}/${state} did not render`).toBeTruthy()
  const style = getComputedStyle(dot)
  const sig: GreyscaleSignature = {
    size: parseFloat(style.width),
    fill: fillClass(style.backgroundColor || dot.style.background),
    glyph: state === 'inert' ? '' : (dot.textContent ?? '').trim(),
  }
  unmount()
  return sig
}

function distinguishable(a: GreyscaleSignature, b: GreyscaleSignature): boolean {
  const bySize = Math.abs(a.size - b.size) >= 3
  const byFill = a.fill !== b.fill
  const byGlyph = a.glyph !== b.glyph
  return bySize || byFill || byGlyph
}

describe('gate 2 — hotspot identity survives greyscale (size, fill inversion, numeral — never hue)', () => {
  for (const surface of SURFACES) {
    it(`every pair of states is distinct without hue on the ${surface} stage`, () => {
      const sigs = STATES.map((state) => ({ state, sig: signature(state, surface) }))
      for (let i = 0; i < sigs.length; i++) {
        for (let j = i + 1; j < sigs.length; j++) {
          expect(
            distinguishable(sigs[i].sig, sigs[j].sig),
            `${surface}: '${sigs[i].state}' vs '${sigs[j].state}' collapse under greyscale — ` +
              `${JSON.stringify(sigs[i].sig)} vs ${JSON.stringify(sigs[j].sig)}`,
          ).toBe(true)
        }
      }
    })
  }

  it('every pair of states is distinct without hue ACROSS the two surfaces at once', () => {
    // Until §08 the two variants were alternatives — a page was dark or it was
    // paper, and a viewer never saw both. The cross-section treatment ends that:
    // "Dots keep their one meaning on the cut face; on that light ground they
    // flip to the paper variant from §07, dark outline and all." So a dot on the
    // cut face and a dot on the exterior are on screen together, and the table
    // this gate pins is now the full (state × surface) cross product rather than
    // two independent five-state tables.
    //
    // PAIRS THAT SHARE A STATE ARE SKIPPED, DELIBERATELY. A closed dot on the
    // cut face and a closed dot on the exterior are the same dot saying the same
    // thing; looking alike is the intent of the flip, not a failure of it. The
    // flip exists so the dot stays LEGIBLE on a light ground, and legibility
    // against the ground is what the next test measures. What must never
    // collapse is two dots that MEAN different things.
    const sigs = SURFACES.flatMap((surface) =>
      STATES.map((state) => ({ state, surface, sig: signature(state, surface) })),
    )
    for (let i = 0; i < sigs.length; i++) {
      for (let j = i + 1; j < sigs.length; j++) {
        if (sigs[i].state === sigs[j].state) continue
        expect(
          distinguishable(sigs[i].sig, sigs[j].sig),
          `${sigs[i].surface}/'${sigs[i].state}' vs ${sigs[j].surface}/'${sigs[j].state}' ` +
            `collapse under greyscale, and they mean different things — ` +
            `${JSON.stringify(sigs[i].sig)} vs ${JSON.stringify(sigs[j].sig)}`,
        ).toBe(true)
      }
    }
  })

  it('rendered sizes match the §07 state table exactly', () => {
    expect(hotspotVisual('closed', 'dark').size).toBe(28)
    expect(hotspotVisual('hover', 'dark').size).toBe(32)
    expect(hotspotVisual('open', 'dark').size).toBe(38)
    expect(hotspotVisual('inert', 'dark').size).toBe(13)
    expect(hotspotVisual('target', 'dark').size).toBe(52)
  })

  it('open state is a fill INVERSION — a real greyscale separation, not a hue change', () => {
    for (const surface of SURFACES) {
      const closed = luminance(hotspotVisual('closed', surface).background)
      const open = luminance(hotspotVisual('open', surface).background)
      expect(closed, surface).not.toBeNull()
      expect(open, surface).not.toBeNull()
      // dark stage: accent (~0.49) → cream (~0.94); paper: accent → ink
      // (~0.09). Either way the greyscale gap must be unmistakable.
      expect(
        Math.abs(closed! - open!),
        `${surface}: closed→open fill luminance gap too small to read without hue`,
      ).toBeGreaterThanOrEqual(0.25)
    }
  })

  it('the target state carries the ? glyph', () => {
    const { container } = render(
      <HotspotDot state="target" surface="dark" numeral="03" />,
    )
    expect(container.querySelector('.hotspot')?.textContent).toContain('?')
  })
})

// ── the cut-face flip is NECESSARY, not merely allowed ────────────────
//
// §08 hands the hotspot layer a second ground: "This also frees the hotspots.
// Dots keep their one meaning on the cut face; on that light ground they flip
// to the paper variant from §07, dark outline and all." The stage is dark and
// the cut wall is `#F0E9DC` — the lightest value in the frame — so a dot that
// lands on the cut is standing on paper whatever the rest of the stage is doing.
//
// The tests above would all still pass if the flip were deleted: the dark
// variant's five states stay perfectly distinguishable FROM EACH OTHER on any
// ground, because size and glyph do not care what is behind them. What would go
// is the dot's edge against the thing it sits on. So the flip needs an assertion
// of its own, and it has to be two-sided — that the paper construction clears
// the cut wall, AND that the dark one does not. One-sided, this would pass just
// as happily on a "simplification" that took the flip out again.
//
// The ground is read out of cap.tsx rather than transcribed here, so the two
// files cannot drift apart: if Design repaints the cut wall, this measures the
// value the renderer actually paints. Read as TEXT rather than imported —
// `capColour` lives in the mesh renderer, and importing it would pull three and
// @react-three/fiber into a jsdom gate about DOM components, and a second copy
// of three into the page, to obtain one hex. `section.test.ts` owns the
// assertions that need the function; this file only needs the ground.

const CUT_WALL: string = (() => {
  const source = readFileSync(
    resolve(dirname(fileURLToPath(import.meta.url)), '../../src/renderer/mesh/cap.tsx'),
    'utf8',
  )
  // Comments stripped first: cap.tsx's prose recounts the retired accent pair,
  // and a hex in a paragraph must never be mistaken for a hex in the table.
  const table = source
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/\/\/.*$/gm, '')
    .match(/const\s+CAP_COLOURS\s*=\s*\[\s*'(#[0-9A-Fa-f]{6})'/)
  if (!table) {
    throw new Error(
      "cannot read the cut wall out of cap.tsx — CAP_COLOURS has been renamed or reshaped, " +
        'and this gate is measuring against a ground that may no longer exist',
    )
  }
  return table[1]
})()

/** A CSS colour's alpha — 1 unless an `rgba()` says otherwise. */
function alphaOf(color: string): number {
  const rgba = color.match(/rgba\([^)]*,\s*([\d.]+)\s*\)/)
  return rgba ? parseFloat(rgba[1]) : 1
}

/** The greyscale level a dot's construction actually lays on a given ground.
 *
 * A filled dot lays its fill there. An inert dot has no fill at all — the only
 * mark it makes is its ring, at 42% — so what reaches the ground is the ring
 * composited over it. Rec. 601 luma is a linear combination of the encoded
 * channels, so blending the two LEVELS gives the same number as blending the
 * channels and taking the luma of the result. */
function levelOn(state: HotspotState, surface: HotspotSurface, ground: string): number {
  const v = hotspotVisual(state, surface)
  const fill = luminance(v.background)
  if (fill !== null) return fill

  const ring = v.border.match(/rgba?\([^)]+\)|#[0-9a-f]{6}/i)
  expect(ring, `${surface}/${state} has neither a fill nor a ring — it draws nothing`).toBeTruthy()
  const level = luminance(ring![0])
  expect(level, `${surface}/${state}'s ring is fully transparent`).not.toBeNull()
  const alpha = alphaOf(ring![0])
  return alpha * level! + (1 - alpha) * luminance(ground)!
}

/** The greyscale gap between what a dot lays down and the ground under it. */
function gapOnCut(state: HotspotState, surface: HotspotSurface): number {
  return Math.abs(levelOn(state, surface, CUT_WALL) - luminance(CUT_WALL)!)
}

/** How far a dot's construction must sit from its ground, in Rec. 601 luma,
 * before the dot has an edge at all. The same 0.25 the closed→open inversion is
 * held to above, and for the same reason: it is the gap that still reads once a
 * projector has washed the picture out. Measured on the cut wall, the paper
 * variant's tightest state clears it by 0.10 and the dark variant's cream fill
 * misses it by 0.21, so nothing here sits near the line. */
const GROUND_SEPARATION = 0.25

describe('gate 2 — a dot on the cut face MUST flip to paper (§08)', () => {
  it('the cut wall is a light ground — which is why the dark variant cannot stay', () => {
    // Not a restatement of the colour: the point is the CLASS. `#F0E9DC` lands
    // in this file's own 'light' band, the same band the dark variant's open and
    // target fills land in. A dot cannot invert against a ground it matches.
    expect(fillClass(CUT_WALL)).toBe('light')
    expect(fillClass(hotspotVisual('open', 'dark').background)).toBe('light')
  })

  for (const state of STATES) {
    it(`the paper '${state}' dot keeps its edge on the cut wall`, () => {
      const gap = gapOnCut(state, 'paper')
      expect(
        gap,
        `paper/'${state}' lays ${levelOn(state, 'paper', CUT_WALL).toFixed(3)} on a ` +
          `${luminance(CUT_WALL)!.toFixed(3)} ground — a gap of ${gap.toFixed(3)}, ` +
          'which is not an edge',
      ).toBeGreaterThanOrEqual(GROUND_SEPARATION)
    })
  }

  it('the dark variant does NOT — the flip is required, not a preference', () => {
    // This is the assertion that makes the flip load-bearing. The dark open dot
    // is a cream `#FBF3E6` fill: on the `#F0E9DC` cut wall that is a gap of
    // about 0.04, cream on cream, invisible. The paper open dot is an ink
    // `#1A1714` fill on the same ground — about 0.82. Twenty times the
    // separation, from the same state, on the same pixel of specimen.
    //
    // Written as a FAILURE so that deleting the flip and letting the cut-face
    // dots render dark — the obvious simplification, since the stage is dark —
    // fails here rather than shipping invisibly.
    const dark = gapOnCut('open', 'dark')
    const paper = gapOnCut('open', 'paper')
    expect(
      dark,
      `the dark 'open' dot now clears ${GROUND_SEPARATION} on the cut wall (${dark.toFixed(3)}). ` +
        'If that is a deliberate repaint, this gate needs rewriting; if the flip was ' +
        'removed, the cut-face dots have gone invisible',
    ).toBeLessThan(GROUND_SEPARATION)
    expect(paper).toBeGreaterThanOrEqual(GROUND_SEPARATION)
    expect(paper / dark).toBeGreaterThan(10)

    // Target is the same construction as open, and inert is a cream ring at 42%
    // over cream — three of the five dark states disappear on the cut face.
    expect(gapOnCut('target', 'dark')).toBeLessThan(GROUND_SEPARATION)
    expect(gapOnCut('inert', 'dark')).toBeLessThan(GROUND_SEPARATION)

    // The other two survive, because they are accent-filled and the accent is
    // no longer anywhere on the tissue for them to collide with. That is why
    // the flip is decided PER DOT by `raysight().throughCut` rather than per
    // state or per stage: two dark states would have been fine, and three
    // would have vanished.
    expect(gapOnCut('closed', 'dark')).toBeGreaterThanOrEqual(GROUND_SEPARATION)
    expect(gapOnCut('hover', 'dark')).toBeGreaterThanOrEqual(GROUND_SEPARATION)
  })
})
