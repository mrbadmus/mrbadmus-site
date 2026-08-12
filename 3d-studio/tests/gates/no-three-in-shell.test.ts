// @vitest-environment node
// Gate 1 — the door between the shell and Three.js, asserted in both
// directions.
//
// Outward: no file under src/ outside src/renderer/ may import three,
// @react-three/* or drei. Unchanged since Stage 1.
//
// Inward: no file under src/renderer/ may import from src/components/. This
// half is new at Stage 2 (MRB-187). Stage 1's second assertion — that even
// the renderer directory was Three-free — was only ever true because there
// was no real renderer yet; it retired the moment one arrived, and something
// had to take its place. A renderer that reaches back into shell components
// is how the separation dies quietly: the interface stays intact on paper
// while the two halves grow a second, undeclared coupling.

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

  it('the renderer is where Three.js lives — at least one file there imports it', () => {
    // The outward rule above passes trivially if nobody imports Three.js at
    // all, which is exactly the state Stage 1 was in. This keeps the first
    // assertion honest: it is only meaningful while a real renderer exists.
    const importers = walk(join(SRC, 'renderer')).filter((file) =>
      FORBIDDEN.some((rx) => rx.test(readFileSync(file, 'utf8'))),
    )
    expect(importers.length).toBeGreaterThan(0)
  })

  it('no file under src/renderer/ imports from src/components/', () => {
    const SHELL_IMPORT = [
      /from\s+['"][^'"]*\/components\//,
      /from\s+['"]\.\.\/components\//,
      /import\s*\(\s*['"][^'"]*\/components\//,
      /require\(\s*['"][^'"]*\/components\//,
    ]
    const offenders: string[] = []
    for (const file of walk(join(SRC, 'renderer'))) {
      const text = readFileSync(file, 'utf8')
      if (SHELL_IMPORT.some((rx) => rx.test(text))) offenders.push(relative(SRC, file))
    }
    expect(offenders).toEqual([])
  })
})
