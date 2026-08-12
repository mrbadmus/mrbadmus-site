// The R3F scene. Everything Three.js-shaped lives behind this file and its
// siblings; the shell sees only the Renderer interface (gate 1).
//
// The canvas is transparent on purpose. The stage's dark room is a CSS radial
// gradient authored in the frozen reference, so the specimen is composited
// onto Design's ground rather than onto a background invented in JavaScript.

import { Component, useEffect, useMemo, type ErrorInfo, type ReactNode } from 'react'
import * as THREE from 'three'
import { Canvas, useThree } from '@react-three/fiber'
import { ContactShadows, OrbitControls } from '@react-three/drei'
import { EffectComposer, SSAO } from '@react-three/postprocessing'
import { BlendFunction } from 'postprocessing'
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js'
import type { OrbitControls as OrbitControlsImpl } from 'three-stdlib'
import { FOV, type DefaultView } from './anchors'
import { TIER_RIGS, type TierRig } from './tiers'
import { SectionCap, useClippedMaterials } from './cap'
import type { SpecimenPart } from './parts'
import type { RenderTier } from '../types'

/** The mutable handle the imperative Renderer keeps into the live scene.
 * React writes it; hotspotToScreen and the tool commands read it. */
export interface SceneBridge {
  camera: THREE.Camera | null
  gl: THREE.WebGLRenderer | null
  controls: OrbitControlsImpl | null
  model: THREE.Object3D | null
  view: DefaultView | null
  width: number
  height: number
}

export function createBridge(): SceneBridge {
  return {
    camera: null,
    gl: null,
    controls: null,
    model: null,
    view: null,
    width: 0,
    height: 0,
  }
}

export interface SceneProps {
  bridge: SceneBridge
  model: THREE.Object3D | null
  view: DefaultView | null
  tier: RenderTier
  autoRotate: boolean
  /** the cross-section, when one is engaged (MRB-189) */
  section: SectionProps | null
  onCreated: () => void
  onFailure: (message: string) => void
}

export interface SectionProps {
  /** stable instance, mutated as the cut is dragged */
  plane: THREE.Plane
  box: THREE.Box3
  /** the parts the asset declares — one cap face each, coloured by depth */
  parts: readonly SpecimenPart[]
  /** bumped whenever the plane moved or the drawn part set changed */
  version: number
  isDrawn: (object: THREE.Object3D) => boolean
  /** false where the tier cannot carry the stencil pass: the cut still
   * happens, it just is not capped (MRB-189's stated fallback) */
  capped: boolean
}

export function SceneRoot(props: SceneProps) {
  const rig = TIER_RIGS[props.tier]
  return (
    <SceneErrorBoundary onFailure={props.onFailure}>
      <Canvas
        gl={{
          alpha: true,
          antialias: true,
          powerPreference: 'high-performance',
          preserveDrawingBuffer: false,
          // three stopped allocating a stencil buffer by default at r163, and
          // the capped cut is drawn with one. Asked for here rather than per
          // tier: it is part of the context, and changing it would mean
          // rebuilding the canvas — which gate 5 forbids.
          stencil: true,
        }}
        // The camera is re-aimed from the specimen's bounds the moment one
        // loads; these are only sane defaults for the empty stage.
        camera={{ fov: FOV, near: 0.1, far: 100, position: [0, 0, 5] }}
        dpr={[1, rig.maxPixelRatio]}
        onCreated={({ gl }) => {
          gl.setClearAlpha(0)
          gl.toneMapping = THREE.ACESFilmicToneMapping
          gl.toneMappingExposure = 1.05
          props.onCreated()
        }}
        style={{ position: 'absolute', inset: 0 }}
      >
        <SceneContents {...props} rig={rig} />
      </Canvas>
    </SceneErrorBoundary>
  )
}

function SceneContents({
  bridge,
  model,
  view,
  rig,
  autoRotate,
  section,
  onFailure,
}: SceneProps & { rig: TierRig }) {
  useClippedMaterials(model, section ? section.plane : null)
  return (
    <>
      <BridgeSync bridge={bridge} onFailure={onFailure} />
      <TierEffects rig={rig} />
      {rig.environment && <RoomIBL />}
      <Lights rig={rig} view={view} />
      {model && <primitive object={model} />}
      {model && section && section.capped && (
        <SectionCap
          model={model}
          plane={section.plane}
          box={section.box}
          parts={section.parts}
          version={section.version}
          isDrawn={section.isDrawn}
        />
      )}
      {model && view && rig.contactShadow && <Ground view={view} model={model} />}
      {view && <Framing bridge={bridge} view={view} />}
      <OrbitControls
        makeDefault
        // Panning is what loses a specimen off the edge of the stage, so it is
        // off: the model stays centred and the camera orbits it (MRB-187).
        enablePan={false}
        enableDamping
        dampingFactor={0.075}
        rotateSpeed={0.85}
        zoomSpeed={0.75}
        autoRotate={autoRotate}
        autoRotateSpeed={0.9}
        // Stopping short of the poles keeps the specimen from tumbling
        // through upside-down as the drag crosses the top.
        minPolarAngle={Math.PI * 0.08}
        maxPolarAngle={Math.PI * 0.92}
        minDistance={view ? view.radius * 1.05 : 0.5}
        maxDistance={view ? view.radius * 8 : 40}
        ref={(controls) => {
          bridge.controls = (controls as OrbitControlsImpl | null) ?? null
        }}
      />
      {/* stencilBuffer: the composer renders the scene into a target of its
          own, and without one the capped cut would silently stop being capped
          at Tier A only — the tier with the most capable hardware behind it
          (MRB-189). */}
      {rig.ambientOcclusion && (
        <EffectComposer enableNormalPass multisampling={0} stencilBuffer>
          <SSAO
            blendFunction={BlendFunction.MULTIPLY}
            samples={16}
            rings={4}
            radius={0.08}
            intensity={14}
            luminanceInfluence={0.5}
            worldDistanceThreshold={64}
            worldDistanceFalloff={8}
            worldProximityThreshold={0.4}
            worldProximityFalloff={0.1}
          />
        </EffectComposer>
      )}
    </>
  )
}

/** Publishes the live camera, renderer and container size to the bridge, and
 * turns a lost WebGL context into a renderer failure the shell can route on. */
function BridgeSync({
  bridge,
  onFailure,
}: {
  bridge: SceneBridge
  onFailure: (message: string) => void
}) {
  const camera = useThree((s) => s.camera)
  const gl = useThree((s) => s.gl)
  const size = useThree((s) => s.size)

  useEffect(() => {
    bridge.camera = camera
    bridge.gl = gl
  }, [bridge, camera, gl])

  useEffect(() => {
    bridge.width = size.width
    bridge.height = size.height
  }, [bridge, size])

  useEffect(() => {
    const canvas = gl.domElement
    const onLost = (event: Event) => {
      // Preventing the default is what would let the context be restored; we
      // deliberately do not, because the shell's answer to a lost context is
      // the flat renderer, not a half-recovered stage (spec §3.1).
      onFailure(`WebGL context lost: ${(event as WebGLContextEvent).statusMessage || 'no reason given'}`)
    }
    canvas.addEventListener('webglcontextlost', onLost)
    return () => canvas.removeEventListener('webglcontextlost', onLost)
  }, [gl, onFailure])

  return null
}

/** Everything a tier changes that lives on the renderer rather than in the
 * scene graph. Applied in an effect, so a tier change is a re-render of this
 * component — never a remount of the canvas (gate 5). */
function TierEffects({ rig }: { rig: TierRig }) {
  const gl = useThree((s) => s.gl)
  const scene = useThree((s) => s.scene)
  const setDpr = useThree((s) => s.setDpr)

  useEffect(() => {
    gl.shadowMap.enabled = rig.shadows
    gl.shadowMap.type = THREE.PCFSoftShadowMap
    gl.shadowMap.needsUpdate = true
    // Toggling shadows changes the shader programs, so materials already on
    // the GPU have to be told to recompile.
    scene.traverse((node) => {
      const mesh = node as THREE.Mesh
      if (!mesh.isMesh) return
      const materials = Array.isArray(mesh.material) ? mesh.material : [mesh.material]
      for (const material of materials) if (material) material.needsUpdate = true
    })
  }, [gl, scene, rig.shadows])

  useEffect(() => {
    const device = typeof window !== 'undefined' ? window.devicePixelRatio || 1 : 1
    setDpr(Math.min(device, rig.maxPixelRatio))
  }, [setDpr, rig.maxPixelRatio])

  return null
}

/** Image-based light generated in-process from three's RoomEnvironment — no
 * HDR file, no CDN. Tier A only: it costs one PMREM render up front. */
function RoomIBL() {
  const gl = useThree((s) => s.gl)
  const scene = useThree((s) => s.scene)
  useEffect(() => {
    const pmrem = new THREE.PMREMGenerator(gl)
    const environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture
    scene.environment = environment
    scene.environmentIntensity = 0.22
    return () => {
      scene.environment = null
      environment.dispose()
      pmrem.dispose()
    }
  }, [gl, scene])
  return null
}

/** Key / fill / rim, thinned by tier. Positions scale with the specimen so a
 * model authored in millimetres lights the same as one authored in metres. */
function Lights({ rig, view }: { rig: TierRig; view: DefaultView | null }) {
  const r = view?.radius ?? 1
  const centre = view?.target ?? new THREE.Vector3()
  const at = (x: number, y: number, z: number): [number, number, number] => [
    centre.x + x * r,
    centre.y + y * r,
    centre.z + z * r,
  ]

  if (rig.lights === 'simple') {
    return (
      <>
        <ambientLight intensity={0.9} />
        <directionalLight position={at(1.4, 2, 2.2)} intensity={1.7} />
      </>
    )
  }

  return (
    <>
      <hemisphereLight args={['#FFF6E6', '#2A2119', rig.lights === 'full' ? 0.45 : 0.7]} />
      <directionalLight
        position={at(1.6, 2.4, 2.4)}
        intensity={1.75}
        castShadow={rig.shadows}
        shadow-mapSize-width={rig.shadowMapSize}
        shadow-mapSize-height={rig.shadowMapSize}
        shadow-bias={-0.0012}
        shadow-normalBias={r * 0.02}
        shadow-camera-near={r * 0.5}
        shadow-camera-far={r * 10}
        shadow-camera-left={-r * 2}
        shadow-camera-right={r * 2}
        shadow-camera-top={r * 2}
        shadow-camera-bottom={-r * 2}
      />
      <directionalLight position={at(-2.2, 0.6, 1.2)} intensity={0.45} />
      <directionalLight position={at(-0.6, 0.8, -2.6)} intensity={0.8} color="#FFE9CC" />
    </>
  )
}

/** The contact shadow under the specimen — tier A only (MRB-187 scope).
 *
 * It lands on the dark room, not on a cream plane: the spec's "soft cream
 * ground" predates the MRB-183 palette ruling, and the frozen reference
 * authors this stage as a dark viewport with a soft shadow beneath the form
 * (the placeholder's `.ph-shadow`). The reference wins; see the Stage 2
 * report. No ground mesh is drawn, so the CSS gradient stays visible. */
function Ground({ view, model }: { view: DefaultView; model: THREE.Object3D }) {
  const floor = useMemo(() => {
    const box = new THREE.Box3().setFromObject(model)
    return box.min.y - view.radius * 0.06
  }, [model, view])

  return (
    <ContactShadows
      position={[view.target.x, floor, view.target.z]}
      scale={view.radius * 5}
      resolution={512}
      blur={2.6}
      opacity={0.62}
      far={view.radius * 2.2}
      frames={Infinity}
      color="#000000"
    />
  )
}

/** Depth range and initial placement for the loaded specimen. Runs once per
 * view: putting the camera back is `invokeTool('reset')`, not a re-render. */
function Framing({ bridge, view }: { bridge: SceneBridge; view: DefaultView }) {
  const camera = useThree((s) => s.camera) as THREE.PerspectiveCamera
  const controls = useThree((s) => s.controls) as unknown as OrbitControlsImpl | null

  useEffect(() => {
    camera.near = Math.max(view.radius * 0.02, 0.001)
    camera.far = view.radius * 60
    camera.position.copy(view.position)
    camera.updateProjectionMatrix()
    if (controls) {
      controls.target.copy(view.target)
      controls.update()
      // Make THIS the state OrbitControls returns to. Without it, reset()
      // restores wherever the camera happened to be when the controls were
      // constructed — before the specimen had loaded and anything had been
      // framed.
      controls.saveState()
    }
    bridge.view = view
  }, [bridge, camera, controls, view])

  return null
}

/** A canvas that cannot be created — no WebGL, a driver refusal, a device out
 * of memory — is a renderer failure, which the shell answers by switching to
 * the flat renderer. It is never an error message on the stage (spec §3.1). */
class SceneErrorBoundary extends Component<
  { children: ReactNode; onFailure: (message: string) => void },
  { failed: boolean }
> {
  state = { failed: false }

  static getDerivedStateFromError() {
    return { failed: true }
  }

  componentDidCatch(error: Error, _info: ErrorInfo) {
    this.props.onFailure(error?.message || 'the 3D scene could not be created')
  }

  render() {
    return this.state.failed ? null : this.props.children
  }
}
