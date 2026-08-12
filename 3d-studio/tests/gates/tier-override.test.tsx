// Gate 5 — the tier override changes render output live: no page reload, no
// remount of the renderer's container. Drives the real UI path: quality chip
// → override panel → Balanced.
//
// Stage 2 note (MRB-187). jsdom has no WebGL, so the mesh renderer cannot
// mount here and the shell — correctly — routes the whole stage to the flat
// renderer, which declares no quality tiers and therefore draws no chip.
// That is the app being right, not the gate being wrong, so the gate now
// works in two places:
//
//   · here, the shell's half of the contract: the chip's choice reaches the
//     mounted renderer's setTier, on the same instance, in the same
//     container, with no reload — asserted both against the placeholder's
//     drawn output (as at Stage 1) and against a renderer that records what
//     it was actually asked to do.
//   · in `3d_render_check.py`, the mesh renderer's half: the same journey in
//     a real browser with real WebGL, asserting the canvas element survives
//     and the rendered pixels genuinely change.

import { describe, expect, it } from 'vitest'
import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import App from '../../src/App'
import type { CapabilityReport } from '../../src/studio/capability'
import { createPlaceholderRenderer } from '../../src/renderer/placeholder'
import type { Renderer, RenderTier } from '../../src/renderer/types'

const TIER_A: CapabilityReport = {
  tier: 'A',
  webgl2: true,
  deviceMemory: 8,
  cores: 8,
  viewport: { width: 1440, height: 900 },
  pointer: 'fine',
}

/** A tiered renderer that can exist in jsdom. Same instance across the whole
 * journey, so "no remount" is a fact the test can read rather than infer. */
const viewportPlaceholder = () => createPlaceholderRenderer('viewport')

describe('gate 5 — tier override changes render output without a reload', () => {
  it('Auto(A) → Balanced redraws the stage in place', async () => {
    const href = window.location.href
    render(<App capability={TIER_A} createRenderer={viewportPlaceholder} />)

    const container = screen.getByTestId('renderer-container')
    await waitFor(() => expect(container.dataset.tier).toBe('A'))
    const before = container.innerHTML
    expect(before).toContain('ph-form--a')

    // the chip is the whole affordance — open the override panel
    fireEvent.click(screen.getByRole('button', { name: /render quality/i }))
    // detected tier stays visible so the override is a choice against
    // something known
    expect(screen.getByText(/DETECTED · ULTRA/)).toBeTruthy()

    fireEvent.click(screen.getByRole('menuitemradio', { name: 'Balanced' }))

    await waitFor(() => expect(container.dataset.tier).toBe('C'))
    const after = container.innerHTML
    expect(after).not.toBe(before)
    expect(after).toContain('ph-form--c')
    expect(after).not.toContain('ph-form--a')

    // same document, same mounted container — nothing reloaded or remounted
    expect(screen.getByTestId('renderer-container')).toBe(container)
    expect(window.location.href).toBe(href)
  })

  it('Lite maps to tier C, never to tier D (ruling: D is not user-selectable)', async () => {
    render(<App capability={TIER_A} createRenderer={viewportPlaceholder} />)
    const container = screen.getByTestId('renderer-container')
    await waitFor(() => expect(container.dataset.tier).toBe('A'))

    fireEvent.click(screen.getByRole('button', { name: /render quality/i }))
    fireEvent.click(screen.getByRole('menuitemradio', { name: 'Lite' }))

    await waitFor(() => expect(container.dataset.tier).toBe('C'))
    // still the viewport placeholder — the flat renderer is a capability
    // floor, not a quality option
    expect(container.dataset.renderer).toBe('placeholder-viewport')
  })

  it('the tier reaches the SAME renderer instance — never a fresh mount', async () => {
    const log: string[] = []
    const seen: { container: HTMLElement | null } = { container: null }
    let instances = 0

    const recording = (): Renderer => {
      const inner = createPlaceholderRenderer('viewport')
      instances += 1
      return {
        stage: inner.stage,
        supportedTools: inner.supportedTools,
        supportsQualityTiers: inner.supportsQualityTiers,
        mount(container: HTMLElement) {
          seen.container = container
          log.push('mount')
          inner.mount(container)
        },
        unmount() {
          log.push('unmount')
          inner.unmount()
        },
        setTier(tier: RenderTier) {
          log.push(`setTier:${tier}`)
          inner.setTier(tier)
        },
        loadSpecimen: (s) => inner.loadSpecimen(s),
        hotspotToScreen: (id) => inner.hotspotToScreen(id),
        invokeTool: (tool, on) => inner.invokeTool(tool, on),
        isolateHotspot: (id) => inner.isolateHotspot(id),
        toolState: (tool) => inner.toolState(tool),
        onStatus: (cb) => inner.onStatus(cb),
      }
    }

    render(<App capability={TIER_A} createRenderer={recording} />)
    const container = screen.getByTestId('renderer-container')
    await waitFor(() => expect(log).toContain('setTier:A'))

    fireEvent.click(screen.getByRole('button', { name: /render quality/i }))
    fireEvent.click(screen.getByRole('menuitemradio', { name: 'Balanced' }))
    await waitFor(() => expect(log).toContain('setTier:C'))

    expect(instances).toBe(1)
    expect(log.filter((entry) => entry === 'mount')).toHaveLength(1)
    expect(log).not.toContain('unmount')
    expect(seen.container).toBe(container)
  })
})
