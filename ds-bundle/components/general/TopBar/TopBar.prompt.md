TopBar from mrbadmus-3d-studio. Use via `window.MrBadmusDS.TopBar` (bundle loaded from the root `_ds_bundle.js`).

## Examples

### DesktopExplore

```jsx
() => (
  <div style={{ width: 1160, background: '#FBF3E6', borderRadius: 12, overflow: 'hidden', border: '1px solid #D9C9AC' }}>
    <TopBar layout="desktop" mode="explore" onMode={() => {}} onOpenLibrary={() => {}} />
  </div>
)
```

### DesktopRetrieve

```jsx
() => (
  <div
    className="app"
    data-mode="retrieve"
    style={{ width: 1160, minHeight: 0, background: '#15110C', borderRadius: 12, overflow: 'hidden', border: '1px solid #2E271F' }}
  >
    <TopBar layout="desktop" mode="retrieve" onMode={() => {}} onOpenLibrary={() => {}} />
  </div>
)
```

### TabletExplore

```jsx
() => (
  <div style={{ width: 800, background: '#FBF3E6', borderRadius: 12, overflow: 'hidden', border: '1px solid #D9C9AC' }}>
    <TopBar layout="tablet" mode="explore" onMode={() => {}} onOpenLibrary={() => {}} />
  </div>
)
```

### PhoneExplore

```jsx
() => (
  <div style={{ width: 390, background: '#FBF3E6', borderRadius: 12, overflow: 'hidden', border: '1px solid #D9C9AC' }}>
    <TopBar layout="phone" mode="explore" onMode={() => {}} onOpenLibrary={() => {}} phoneTitle={null} />
  </div>
)
```
