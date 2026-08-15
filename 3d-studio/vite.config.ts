/// <reference types="vitest/config" />
import { copyFileSync, existsSync, mkdirSync, readdirSync, rmSync, statSync } from 'node:fs'
import { dirname, join, relative, resolve, sep } from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig, type Plugin } from 'vite'
import react from '@vitejs/plugin-react'

const here = dirname(fileURLToPath(import.meta.url))
const BASE = '/3d/'

// ── Draco decoder, self-hosted ───────────────────────────────────────────────
// three's DRACOLoader defaults to fetching its decoder from a Google CDN.
// Neither a school network that blocks it nor a page for under-16s should
// depend on that, so the decoder ships with the app: copied out of the
// installed three package into public/draco/ (gitignored — it is a build
// input restored by npm install, not source).
const DRACO_FILES = ['draco_decoder.js', 'draco_decoder.wasm', 'draco_wasm_wrapper.js']

function stageDracoDecoder(): void {
  const from = resolve(here, 'node_modules/three/examples/jsm/libs/draco/gltf')
  const to = resolve(here, 'public/draco')
  if (!existsSync(from)) return
  mkdirSync(to, { recursive: true })
  for (const file of DRACO_FILES) {
    const source = join(from, file)
    const target = join(to, file)
    if (!existsSync(source)) continue
    const stale = !existsSync(target) || statSync(target).mtimeMs < statSync(source).mtimeMs
    if (stale) copyFileSync(source, target)
  }
}

// ── Specimen mesh stand-in ───────────────────────────────────────────────────
// The heart GLB has not been acquired (MRB-187). While no acquired mesh is on
// disk, the renderer loads the generated test specimen instead, so it is
// exercised on chambered geometry rather than on nothing. Drop an acquired
// `.glb` into public/assets/ and this evaporates on the next build — no code
// change in src/. Underscore-prefixed files are generated test assets and do
// not count as acquired.
// ONE POLICY, NO EXCEPTIONS: a generated fixture never reaches a production
// build. `public/` is copied wholesale into `dist/`, and `dist/` is published
// to mrbadmus_site/3d/ (MRB-194), so on any machine where `npm run test-specimen`
// or `npm run test-plate` had been run, the fixtures shipped to production.
// They are gitignored, which hid that rather than fixing it.
//
// The policy is enforced HERE rather than at publication, because publication
// stays a one-policy opaque blob: it copies dist/ and asks no questions. Two
// halves, and both are needed — this one, and `stripGeneratedFixtures` below.
// A build that stripped the file but kept the reference would be worse than
// either: the app would ask for an asset that had just been deleted.
function standInFor(
  extension: string,
  fixture: string,
  isBuild: boolean,
): string | null {
  if (isBuild) return null
  const assets = resolve(here, 'public/assets')
  const acquired =
    existsSync(assets) &&
    readdirSync(assets).some(
      (file) => file.endsWith(extension) && !file.startsWith('_'),
    )
  return acquired ? null : `${BASE}assets/${fixture}`
}

// ── The other half: nothing underscore-prefixed survives into dist/ ──────────
//
// THE PREDICATE IS NOT "basename starts with _", and the difference matters.
// Rollup emits its own chunks into the same directory, and some of them are
// underscore-prefixed by convention — `_commonjsHelpers-<hash>.js`,
// `_virtual_<id>.js` — the moment a dependency graph produces one. Deleting a
// real chunk would break the app silently and only on the machine where that
// dependency landed. So the set of files Rollup wrote is collected from the
// bundle itself, and only underscore-prefixed files that are NOT in it are
// removed. What is left is exactly the staged-from-public/ fixtures.
function stripGeneratedFixtures(): Plugin {
  const rollupOwned = new Set<string>()
  let outDir = resolve(here, 'dist')

  const walk = (dir: string): string[] =>
    readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
      const full = join(dir, entry.name)
      return entry.isDirectory() ? walk(full) : [full]
    })

  return {
    name: 'mrb-strip-generated-fixtures',
    apply: 'build',
    configResolved(config) {
      outDir = resolve(config.root, config.build.outDir)
    },
    writeBundle(_options, bundle) {
      // Keys are paths relative to outDir — `assets/index-<hash>.js`,
      // `index.html`. Everything Rollup itself produced is in here; nothing
      // copied out of public/ ever is.
      for (const name of Object.keys(bundle)) rollupOwned.add(name)
    },
    // Last hook in the build, and therefore after public/ has been copied.
    closeBundle() {
      if (!existsSync(outDir)) return
      for (const file of walk(outDir)) {
        const rel = relative(outDir, file).split(sep).join('/')
        const base = rel.slice(rel.lastIndexOf('/') + 1)
        if (!base.startsWith('_') || rollupOwned.has(rel)) continue
        rmSync(file)
        console.log(`[3d-studio] generated fixture stripped from the build: ${rel}`)
      }
    },
  }
}

stageDracoDecoder()

// base is architecturally fixed: the app is served from mrbadmus.com/3d, and the
// Stage 9 publication step copies 3d-studio/dist/ to mrbadmus_site/3d/ (MRB-194).
export default defineConfig(({ command }) => {
  // `vite dev` and `vite preview` keep the stand-ins, so local review at
  // localhost:8899/3d/ is exactly as it was. Only a production build goes
  // without.
  const isBuild = command === 'build'
  const MESH_STANDIN = standInFor('.glb', '_test-specimen.glb', isBuild)
  // The flat renderer's counterpart (MRB-190). assets.fallback is a Stage-8
  // TODO exactly as assets.mesh was, so the flat path gets the same treatment:
  // a generated fixture that carries no anatomy, and evaporates the moment a
  // drawn diagram lands in public/assets/.
  //
  // WHAT THIS COSTS, STATED RATHER THAN PAPERED OVER: heart.glb is acquired, so
  // MESH_STANDIN is already null in every build and stripping the mesh fixture
  // is pure win. The plate is different — PLATE_STANDIN was live, so the flat
  // renderer now has no plate in production and lands in its missing-asset
  // state on Tier D. That is the intended outcome. The fixture carried no
  // anatomy and said so on its face, so hotspot positions on it were
  // meaningless; it was never usable teaching, and an honest missing-asset
  // state makes the gap visible instead of hiding it behind something that
  // looks like a diagram. There is deliberately no bypass, env flag or
  // exception for it. A drawn heart plate in public/assets/ is a Tier D
  // launch blocker.
  const PLATE_STANDIN = standInFor('.svg', '_test-plate.svg', isBuild)
  if (MESH_STANDIN) {
    console.log(`[3d-studio] no acquired specimen mesh on disk — using ${MESH_STANDIN}`)
  }
  if (PLATE_STANDIN) {
    console.log(`[3d-studio] no acquired fallback diagram on disk — using ${PLATE_STANDIN}`)
  }

  return {
    base: BASE,
    plugins: [react(), stripGeneratedFixtures()],
    // drei reaches three through three-stdlib; two copies of three in one
    // bundle break every instanceof check inside it.
    resolve: { dedupe: ['three'] },
    define: {
      __MESH_STANDIN__: JSON.stringify(MESH_STANDIN),
      __PLATE_STANDIN__: JSON.stringify(PLATE_STANDIN),
    },
    build: {
      rollupOptions: {
        output: {
          // The mesh renderer is behind a dynamic import (ruling on MRB-190),
          // so Three lands in a chunk of its own. Naming it is not cosmetic:
          // the browser gate asserts that a Tier D load requests NO three
          // chunk, and it can only assert that against a name it recognises.
          manualChunks(id: string) {
            if (/node_modules[/\\](three|three-stdlib|postprocessing)[/\\]/.test(id)) {
              return 'three'
            }
            return undefined
          },
        },
      },
    },
    server: { port: 8899, strictPort: true },
    preview: { port: 8899, strictPort: true },
    test: {
      environment: 'jsdom',
      setupFiles: ['tests/setup.ts'],
      include: ['tests/**/*.test.{ts,tsx}'],
      testTimeout: 20000,
    },
  }
})
