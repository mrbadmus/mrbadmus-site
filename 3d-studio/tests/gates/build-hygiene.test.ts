// @vitest-environment node
// ONE POLICY, NO EXCEPTIONS: a generated fixture never reaches a production
// build (MRB-215).
//
// `public/` is copied wholesale into `dist/`, and `dist/` is published to
// mrbadmus_site/3d/ (MRB-194). So on any machine where `npm run test-specimen`
// or `npm run test-plate` had been run, `_test-specimen.glb` and
// `_test-plate.svg` shipped to production. They are gitignored, which hid the
// problem rather than fixing it — and gitignore is exactly the wrong tool,
// because the file still exists on the machine that does the publishing.
//
// The policy has two halves and this gate asserts both, because either alone
// is worse than neither:
//
//   1. NO FIXTURE FILE survives into dist/.
//   2. NO REFERENCE to one is emitted. A build that stripped the file but kept
//      the reference would leave the app fetching an asset it had just
//      deleted — a 404 at runtime instead of an honest missing-asset state.
//
// This runs the REAL build, through Vite's own JS API, into a scratch outDir.
// A gate that asserted against a hand-rolled imitation of the build would
// prove nothing about the build that actually ships. It costs a few seconds;
// the alternative costs a fixture on mrbadmus.com.

import { afterAll, beforeAll, describe, expect, it } from 'vitest'
import { existsSync, mkdtempSync, readdirSync, readFileSync, rmSync, statSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join, relative, sep } from 'node:path'
import { fileURLToPath } from 'node:url'
import { build } from 'vite'

const ROOT = fileURLToPath(new URL('../..', import.meta.url))

/** A fixture is a file whose BASENAME begins with an underscore. The
 * convention is `tools/make_test_*.py`'s, and vite.config.ts's stripper reads
 * it the same way. */
const FIXTURE = /^_/

/** How the app would ASK for one: the served path, not the bare filename.
 * Deliberately narrower than "does the string `_test-plate` appear anywhere" —
 * content/heart.json's TODO prose is entitled to describe the situation in
 * words, and a gate that could not tell prose from a fetch would be traded
 * away the first time it fired on a comment. This matches a URL. */
const SERVED_REFERENCE = /["'`(]\/3d\/assets\/_/

function walk(dir: string): string[] {
  return readdirSync(dir).flatMap((name) => {
    const path = join(dir, name)
    return statSync(path).isDirectory() ? walk(path) : [path]
  })
}

let out: string
let files: string[]

beforeAll(async () => {
  out = mkdtempSync(join(tmpdir(), 'mrb-3d-build-'))
  await build({
    root: ROOT,
    logLevel: 'silent',
    build: { outDir: out, emptyOutDir: true },
  })
  files = walk(out).map((f) => relative(out, f).split(sep).join('/'))
}, 180_000)

afterAll(() => {
  if (out && existsSync(out)) rmSync(out, { recursive: true, force: true })
})

describe('build hygiene — generated fixtures never ship', () => {
  it('the build produced something, so the assertions below mean something', () => {
    // A stripper that deleted the whole of dist/ would pass every other
    // assertion in this file.
    expect(files).toContain('index.html')
    expect(files.some((f) => /^assets\/index-.*\.js$/.test(f))).toBe(true)
    expect(files.some((f) => /^assets\/three-.*\.js$/.test(f))).toBe(true)
  })

  it('no underscore-prefixed file survives into the build', () => {
    const survivors = files.filter((f) => FIXTURE.test(f.slice(f.lastIndexOf('/') + 1)))
    expect(survivors).toEqual([])
  })

  it('the acquired assets are NOT stripped — only the fixtures are', () => {
    // The stripper's predicate excludes Rollup's own output by consulting the
    // bundle; this is the other side of that care. `heart.glb` is acquired and
    // must ship.
    expect(files).toContain('assets/heart.glb')
  })

  it('no emitted file references a fixture by its served path', () => {
    const offenders = files
      .filter((f) => /\.(js|css|html)$/.test(f))
      .filter((f) => SERVED_REFERENCE.test(readFileSync(join(out, f), 'utf8')))
    expect(offenders).toEqual([])
  })

  it('both stand-in resolvers compile to null in a production build', () => {
    // The define-substituted half. `standInFor` returns null when the command
    // is `build`, so `__MESH_STANDIN__ ?? specimen.assets.mesh` collapses to
    // the record's own path and `isStandIn()` is statically false. If a future
    // edit reinstated a disk probe here, the served-path assertion above would
    // catch the plate but not necessarily the mesh, so this is asserted
    // directly: no bundled chunk may contain a stand-in URL at all.
    const scripts = files.filter((f) => f.endsWith('.js'))
    expect(scripts.length).toBeGreaterThan(0)
    for (const f of scripts) {
      const source = readFileSync(join(out, f), 'utf8')
      expect(source).not.toMatch(/\/3d\/assets\/_test-specimen\.glb/)
      expect(source).not.toMatch(/\/3d\/assets\/_test-plate\.svg/)
    }
  })
})
