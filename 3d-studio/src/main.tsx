import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './styles/fonts.css'
import './styles/tokens.css'
import './styles/studio.css'
import App, { prefetchMeshRenderer } from './App'
import { detectCapability } from './studio/capability'

// The capability probe runs once, here, and two things use it: the shell, and
// the decision to start fetching the mesh chunk. Kicking the fetch off BEFORE
// React renders is the whole of the prefetch — the split would otherwise cost
// a capable device one round-trip in front of a 3MB specimen, on top of a
// school connection (ruling on MRB-190). A Tier D device asks for nothing.
const capability = detectCapability()
prefetchMeshRenderer(capability.tier)

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App capability={capability} />
  </StrictMode>,
)
