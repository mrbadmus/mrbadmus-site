// Gate 5 — the tier override changes render output live: no page reload, no
// remount of the renderer's container. Drives the real UI path: quality chip
// → override panel → Balanced, then asserts the placeholder renderer redrew
// at the new tier inside the SAME mounted container.

import { describe, expect, it } from 'vitest'
import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import App from '../../src/App'
import type { CapabilityReport } from '../../src/studio/capability'

const TIER_A: CapabilityReport = {
  tier: 'A',
  webgl2: true,
  deviceMemory: 8,
  cores: 8,
  viewport: { width: 1440, height: 900 },
  pointer: 'fine',
}

describe('gate 5 — tier override changes render output without a reload', () => {
  it('Auto(A) → Balanced redraws the stage in place', async () => {
    const href = window.location.href
    render(<App capability={TIER_A} />)

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
    render(<App capability={TIER_A} />)
    const container = screen.getByTestId('renderer-container')
    await waitFor(() => expect(container.dataset.tier).toBe('A'))

    fireEvent.click(screen.getByRole('button', { name: /render quality/i }))
    fireEvent.click(screen.getByRole('menuitemradio', { name: 'Lite' }))

    await waitFor(() => expect(container.dataset.tier).toBe('C'))
    // still the viewport placeholder — the flat renderer is a capability
    // floor, not a quality option
    expect(container.dataset.renderer).toBe('placeholder-viewport')
  })
})
