// @vitest-environment node
// Gate 1 — the shell never imports Three.js. Only src/renderer/ may ever
// touch a 3D library (and at Stage 1 even it does not). Fails on any import
// of three, @react-three/*, or drei anywhere else under src/.

import { describe, expect, it } from 'vitest'
import { readdirSync, readFileSync, statSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { join, relative, sep } from 'node:path'

const SRC = fileURLToPath(new URL('../../src', import.meta.url))

const FORBIDDEN = [
  /from\s+['"]three['"]/,
  /from\s+['"]three\//,
  /require\(\s*['"]three['"]?/,
  /from\s+['"]@react-three\//,
  /from\s+['"]drei['"]/,
  /from\s+['"]@react-three\/drei['"]/,
  /import\s*\(\s*['"]three/,
]

function walk(dir: string): string[] {
  return readdirSync(dir).flatMap((name) => {
    const path = join(dir, name)
    if (statSync(path).isDirectory()) return walk(path)
    return /\.(ts|tsx|js|jsx)$/.test(name) ? [path] : []
  })
}

describe('gate 1 — zero direct Three.js imports in the shell', () => {
  it('no file under src/ outside src/renderer/ imports three/@react-three/drei', () => {
    const offenders: string[] = []
    for (const file of walk(SRC)) {
      const rel = relative(SRC, file)
      if (rel.split(sep)[0] === 'renderer') continue
      const text = readFileSync(file, 'utf8')
      if (FORBIDDEN.some((rx) => rx.test(text))) offenders.push(rel)
    }
    expect(offenders).toEqual([])
  })

  it('at Stage 1 even the renderer directory is Three-free (placeholder only)', () => {
    const rendererDir = join(SRC, 'renderer')
    const offenders: string[] = []
    for (const file of walk(rendererDir)) {
      const text = readFileSync(file, 'utf8')
      if (FORBIDDEN.some((rx) => rx.test(text))) offenders.push(relative(SRC, file))
    }
    expect(offenders).toEqual([])
  })
})
