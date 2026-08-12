// Texture budget per tier (spec §5: half resolution at B, "aggressive
// downscale" at C).
//
// A GPU texture cannot be resized in place, so the source image is redrawn at
// the tier's scale and handed back to the same THREE.Texture. The original
// image is kept, so moving back up a tier restores full resolution rather
// than resampling something already resampled.
//
// Spec §4 caps a specimen's textures at 1024², so tier C's quarter scale is a
// 256² working set — the point of the exercise on a phone.

import * as THREE from 'three'

interface TextureRecord {
  texture: THREE.Texture
  source: TexImageSource
  width: number
  height: number
  /** the scale currently applied, so no-op changes cost nothing */
  applied: number
}

export class TextureBudget {
  private records: TextureRecord[] = []

  /** Called once per loaded specimen. */
  collect(root: THREE.Object3D): void {
    this.records = []
    const seen = new Set<THREE.Texture>()
    root.traverse((node) => {
      const mesh = node as THREE.Mesh
      if (!mesh.isMesh) return
      const materials = Array.isArray(mesh.material) ? mesh.material : [mesh.material]
      for (const material of materials) {
        if (!material) continue
        for (const value of Object.values(material)) {
          const texture = value as THREE.Texture
          if (!value || !texture.isTexture || seen.has(texture)) continue
          seen.add(texture)
          const image = texture.image as TexImageSource & { width?: number; height?: number }
          if (!image || !image.width || !image.height) continue
          this.records.push({
            texture,
            source: image,
            width: image.width,
            height: image.height,
            applied: 1,
          })
        }
      }
    })
  }

  apply(scale: number, anisotropy: number): void {
    for (const record of this.records) {
      record.texture.anisotropy = anisotropy
      if (record.applied === scale) continue
      const resized = scale >= 1 ? record.source : resample(record, scale)
      if (!resized) continue
      record.texture.image = resized
      record.texture.needsUpdate = true
      record.applied = scale
    }
  }

  clear(): void {
    this.records = []
  }
}

function resample(record: TextureRecord, scale: number): TexImageSource | null {
  const width = Math.max(1, Math.round(record.width * scale))
  const height = Math.max(1, Math.round(record.height * scale))
  const canvas = makeCanvas(width, height)
  if (!canvas) return null
  const context = canvas.getContext('2d') as CanvasRenderingContext2D | null
  if (!context) return null
  context.drawImage(record.source as CanvasImageSource, 0, 0, width, height)
  return canvas as unknown as TexImageSource
}

function makeCanvas(width: number, height: number): HTMLCanvasElement | OffscreenCanvas | null {
  if (typeof OffscreenCanvas !== 'undefined') return new OffscreenCanvas(width, height)
  if (typeof document === 'undefined') return null
  const canvas = document.createElement('canvas')
  canvas.width = width
  canvas.height = height
  return canvas
}
