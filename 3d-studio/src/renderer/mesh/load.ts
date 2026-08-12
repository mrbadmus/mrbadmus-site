// GLB loading: Draco-compressed, progress-reporting, and time-bounded.
//
// The decoder is served from our own origin (public/draco, wired in
// vite.config.ts), never three.js's default gstatic CDN — a school network
// that blocks a Google domain must not be able to break the studio, and a
// third-party fetch on a page for under-16s is not something to add casually.

import * as THREE from 'three'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js'

/** A load that has not finished by now is treated as a failure and routed to
 * the flat renderer. Spec §4 caps a GLB at 3MB; a minute of blank stage is
 * worse for a class than a diagram that works. */
export const LOAD_TIMEOUT_MS = 30_000

export interface LoadResult {
  scene: THREE.Group
  dispose: () => void
}

let sharedLoader: GLTFLoader | null = null

function loader(): GLTFLoader {
  if (sharedLoader) return sharedLoader
  const draco = new DRACOLoader()
  draco.setDecoderPath(`${import.meta.env.BASE_URL}draco/`)
  const gltf = new GLTFLoader()
  gltf.setDRACOLoader(draco)
  sharedLoader = gltf
  return gltf
}

export function loadSpecimenMesh(
  url: string,
  onProgress: (fraction: number | undefined) => void,
  timeoutMs = LOAD_TIMEOUT_MS,
): Promise<LoadResult> {
  return new Promise<LoadResult>((resolve, reject) => {
    let settled = false
    const timer = setTimeout(() => {
      if (settled) return
      settled = true
      reject(new Error(`specimen mesh timed out after ${timeoutMs}ms: ${url}`))
    }, timeoutMs)

    const finish = (fn: () => void) => {
      if (settled) return
      settled = true
      clearTimeout(timer)
      fn()
    }

    loader().load(
      url,
      (gltf) => {
        finish(() => resolve({ scene: gltf.scene, dispose: () => disposeTree(gltf.scene) }))
      },
      (event) => {
        if (settled) return
        onProgress(
          event.lengthComputable && event.total > 0 ? event.loaded / event.total : undefined,
        )
      },
      (error) => {
        finish(() =>
          reject(
            error instanceof Error ? error : new Error(`specimen mesh failed to load: ${url}`),
          ),
        )
      },
    )
  })
}

/** Give back every GPU resource the specimen holds. Called on unmount and
 * before loading a different specimen — eight specimens are coming, and a
 * studio a teacher leaves open all lesson must not accumulate them. */
export function disposeTree(root: THREE.Object3D): void {
  root.traverse((node) => {
    const mesh = node as THREE.Mesh
    if (!mesh.isMesh) return
    mesh.geometry?.dispose()
    const materials = Array.isArray(mesh.material) ? mesh.material : [mesh.material]
    for (const material of materials) {
      if (!material) continue
      for (const value of Object.values(material)) {
        if (value && (value as THREE.Texture).isTexture) (value as THREE.Texture).dispose()
      }
      material.dispose()
    }
  })
}
