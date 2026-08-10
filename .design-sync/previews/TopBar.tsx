// Header at the three breakpoints (§01/§02/§05). Brand: two accent chevrons,
// second at 34% opacity, Bricolage wordmark — the public-page treatment for
// this surface.
import { TopBar } from 'mrbadmus-3d-studio'

export const DesktopExplore = () => (
  <div style={{ width: 1160, background: '#FBF3E6', borderRadius: 12, overflow: 'hidden', border: '1px solid #D9C9AC' }}>
    <TopBar layout="desktop" mode="explore" onMode={() => {}} onOpenLibrary={() => {}} />
  </div>
)

export const DesktopRetrieve = () => (
  <div
    className="app"
    data-mode="retrieve"
    style={{ width: 1160, minHeight: 0, background: '#15110C', borderRadius: 12, overflow: 'hidden', border: '1px solid #2E271F' }}
  >
    <TopBar layout="desktop" mode="retrieve" onMode={() => {}} onOpenLibrary={() => {}} />
  </div>
)

export const TabletExplore = () => (
  <div style={{ width: 800, background: '#FBF3E6', borderRadius: 12, overflow: 'hidden', border: '1px solid #D9C9AC' }}>
    <TopBar layout="tablet" mode="explore" onMode={() => {}} onOpenLibrary={() => {}} />
  </div>
)

export const PhoneExplore = () => (
  <div style={{ width: 390, background: '#FBF3E6', borderRadius: 12, overflow: 'hidden', border: '1px solid #D9C9AC' }}>
    <TopBar layout="phone" mode="explore" onMode={() => {}} onOpenLibrary={() => {}} phoneTitle={null} />
  </div>
)
