// The §01 library column, driven by the real Stage 0 content records —
// available specimens select, the rest of the approved v1 set shows
// coming-soon treatment at 52% opacity.
import { LibraryColumn } from 'mrbadmus-3d-studio'

export const EightSpecimens = () => (
  <div
    style={{
      width: 232,
      height: 620,
      display: 'flex',
      padding: 12,
      background: '#FBF3E6',
      borderRadius: 12,
    }}
  >
    <LibraryColumn selectedId="heart" onSelect={() => {}} />
  </div>
)
