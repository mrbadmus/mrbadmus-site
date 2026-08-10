InfoPanel from mrbadmus-3d-studio. Use via `window.MrBadmusDS.InfoPanel` (bundle loaded from the root `_ds_bundle.js`).

Desktop right-hand panel (§01)

## Examples

### Resting

```jsx
() => (
  <div style={frame}>
    <InfoPanel
      specimen={specimen}
      openHotspotId={null}
      onOpenHotspot={() => {}}
      onStartRetrieval={() => {}}
    />
  </div>
)
```

### StructureOpen

```jsx
() => (
  <div style={frame}>
    <InfoPanel
      specimen={specimen}
      openHotspotId="heart.item-03"
      onOpenHotspot={() => {}}
      onStartRetrieval={() => {}}
    />
  </div>
)
```
