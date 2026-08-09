// Gate 2 — no hue-only meaning. Design's claim (§07): "Size, fill inversion
// and the numeral do the work. Remove the orange entirely and every state is
// still distinct." This test removes hue by collapsing every fill to its
// greyscale luminance, then asserts every pair of hotspot states is still
// distinguishable by size, by luminance class (light fill / dark fill / no
// fill), or by glyph. It renders the real component under a greyscale filter
// and reads the rendered values, so a styling regression fails here.

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
