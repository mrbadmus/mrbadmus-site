QualityPanel from mrbadmus-3d-studio. Use via `window.MrBadmusDS.QualityPanel` (bundle loaded from the root `_ds_bundle.js`).

## Examples

### AutoOnDetectedHigh

```jsx
() => (
  <div style={stage}>
    <QualityPanel setting="auto" detected="B" onSelect={() => {}} />
  </div>
)
```

### OverriddenToBalanced

```jsx
() => (
  <div style={stage}>
    <QualityPanel setting="balanced" detected="A" onSelect={() => {}} />
  </div>
)
```
