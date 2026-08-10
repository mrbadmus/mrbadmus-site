QualityChip from mrbadmus-3d-studio. Use via `window.MrBadmusDS.QualityChip` (bundle loaded from the root `_ds_bundle.js`).

## Examples

### AutoDetectedHigh

```jsx
() => (
  <div style={stage}>
    <QualityChip setting="auto" detected="B" open={false} onToggle={() => {}} />
  </div>
)
```

### AutoDetectedBalanced

```jsx
() => (
  <div style={stage}>
    <QualityChip setting="auto" detected="C" open={false} onToggle={() => {}} />
  </div>
)
```

### OverriddenToLite

```jsx
() => (
  <div style={stage}>
    <QualityChip setting="lite" detected="A" open={false} onToggle={() => {}} />
  </div>
)
```
