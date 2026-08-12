// Gate 7 — failure is a route, not an error (spec §3.1, MRB-187).
//
// Whatever goes wrong in the mesh renderer — no WebGL context, a GLB that
// 404s, a load that times out, a context lost mid-lesson — the shell answers
// by switching renderer, never by leaving a broken stage or printing an
// error at a class. The flat renderer lands at Stage 5; until then the route
// ends at the paper placeholder, which IS the designed §06 stage.
//
// This drives the real thing: the default renderer policy, a capability
// report that says tier A, and an environment (jsdom) that cannot give the
// mesh renderer a canvas. The renderer reports 'failed'; the shell must have
// re-dressed the stage by the time the test looks.
//
// The other half — a genuinely missing GLB over HTTP, in a browser that does
// have WebGL — is driven by `3d_render_check.py`, which serves a build with
// the specimen asset removed.

import { describe, expect, it } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import App from '../../src/App'
import type { CapabilityReport } from '../../src/studio/capability'
import { createMeshRenderer } from '../../src/renderer/mesh'
import type { RendererStatus } from '../../src/renderer/types'
import { getSpecimen } from '../../src/studio/content'

const TIER_A: CapabilityReport = {
  tier: 'A',
  webgl2: true,
  deviceMemory: 8,
  cores: 8,
  viewport: { width: 1440, height: 900 },
  pointer: 'fine',
}

describe('gate 7 — a renderer that fails routes to the flat stage', () => {
  it('the mesh renderer reports failure rather than throwing at the shell', async () => {
    const container = document.createElement('div')
    document.body.appendChild(container)

    const renderer = createMeshRenderer()
    const seen: RendererStatus[] = []
    renderer.onStatus((status) => seen.push(status))
    renderer.mount(container)

    await expect(renderer.loadSpecimen(getSpecimen('heart'))).rejects.toBeInstanceOf(Error)

    const last = seen[seen.length - 1]
    expect(last.state).toBe('failed')
    expect(last.error).toBeTruthy()
    renderer.unmount()
    container.remove()
  })

  it('the shell answers that failure with the flat stage', async () => {
    render(<App capability={TIER_A} />)

    await waitFor(() => {
      expect(screen.getByTestId('renderer-container').dataset.renderer).toBe('placeholder-paper')
    })

    // The mesh renderer's own teardown is deferred by a tick; give it time to
    // run. It must not take the flat stage's drawing with it — both renderers
    // are handed the same container, and React clears whatever container its
    // root owns.
    await new Promise((resolve) => setTimeout(resolve, 20))

    // The stage is dressed as the flat stage, not as a broken viewport.
    expect(screen.getByText('FLAT DIAGRAM')).toBeTruthy()
    expect(document.querySelector('.ph-plate')).toBeTruthy()
    expect(document.querySelector('.ph-grid')).toBeTruthy()
    expect(document.querySelector('canvas')).toBeNull()
    // No quality chip: there is no render load to tune (§06).
    expect(screen.queryByRole('button', { name: /render quality/i })).toBeNull()
    // Nothing anywhere says "error".
    expect(document.body.textContent).not.toMatch(/error|failed|sorry/i)
  })
})
