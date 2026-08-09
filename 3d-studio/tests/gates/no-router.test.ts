// @vitest-environment node
// Gate 3 — no client-side router in v1 (ruling on MRB-194: Cloudflare
// _redirects is broken on this project, so deep paths would 404; specimen
// selection is in-memory state, one entry point). Fails if a routing library
// appears anywhere in dependencies.

import { describe, expect, it } from 'vitest'
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

const pkg = JSON.parse(
  readFileSync(fileURLToPath(new URL('../../package.json', import.meta.url)), 'utf8'),
)

const ROUTER_PACKAGES = [
  'react-router',
  'react-router-dom',
  '@tanstack/react-router',
  '@tanstack/router',
  'wouter',
  '@reach/router',
  'react-location',
  'navi',
]

describe('gate 3 — no client-side router', () => {
  it('no routing library in dependencies or devDependencies', () => {
    const declared = Object.keys({
      ...(pkg.dependencies ?? {}),
      ...(pkg.devDependencies ?? {}),
      ...(pkg.peerDependencies ?? {}),
    })
    const offenders = declared.filter((name) =>
      ROUTER_PACKAGES.some((r) => name === r || name.startsWith(`${r}/`)),
    )
    expect(offenders).toEqual([])
  })
})
