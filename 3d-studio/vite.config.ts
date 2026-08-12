/// <reference types="vitest/config" />
import { copyFileSync, existsSync, mkdirSync, readdirSync, statSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vite'
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
function standInFor(extension: string, fixture: string): string | null {
  const assets = resolve(here, 'public/assets')
  const acquired =
    existsSync(assets) &&
    readdirSync(assets).some(
      (file) => file.endsWith(extension) && !file.startsWith('_'),
    )
  return acquired ? null : `${BASE}assets/${fixture}`
}

stageDracoDecoder()
const MESH_STANDIN = standInFor('.glb', '_test-specimen.glb')
// The flat renderer's counterpart (MRB-190). assets.fallback is a Stage-8
// TODO exactly as assets.mesh is, so the flat path gets the same treatment:
// a generated fixture that carries no anatomy, and evaporates the moment a
// drawn diagram lands in public/assets/.
const PLATE_STANDIN = standInFor('.svg', '_test-plate.svg')
if (MESH_STANDIN) {
  console.log(`[3d-studio] no acquired specimen mesh on disk — using ${MESH_STANDIN}`)
}
if (PLATE_STANDIN) {
  console.log(`[3d-studio] no acquired fallback diagram on disk — using ${PLATE_STANDIN}`)
}

// base is architecturally fixed: the app is served from mrbadmus.com/3d, and the
// Stage 9 publication step copies 3d-studio/dist/ to mrbadmus_site/3d/ (MRB-194).
export default defineConfig({
  base: BASE,
  plugins: [react()],
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
        // The mesh renderer is behind a dynamic import (ruling on MRB-190), so
        // Three lands in a chunk of its own. Naming it is not cosmetic: the
        // browser gate asserts that a Tier D load requests NO three chunk, and
        // it can only assert that against a name it can recognise.
        manualChunks(id) {
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
})
