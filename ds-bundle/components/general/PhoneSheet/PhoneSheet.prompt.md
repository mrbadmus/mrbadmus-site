PhoneSheet from mrbadmus-3d-studio. Use via `window.MrBadmusDS.PhoneSheet` (bundle loaded from the root `_ds_bundle.js`).

## Examples

### SheetAtRest

```jsx
() => (
  <div style={phone}>
    <PhoneSheet
      specimen={specimen}
      raised={false}
      onRaisedChange={() => {}}
      openHotspotId={null}
      onOpenHotspot={() => {}}
      onStartRetrieval={() => {}}
    />
  </div>
)
```

### SheetRaised

```jsx
() => (
  <div style={phone}>
    <PhoneSheet
      specimen={specimen}
      raised={true}
      onRaisedChange={() => {}}
      openHotspotId={null}
      onOpenHotspot={() => {}}
      onStartRetrieval={() => {}}
    />
  </div>
)
```
