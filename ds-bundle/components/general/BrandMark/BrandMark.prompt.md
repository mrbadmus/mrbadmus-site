BrandMark from mrbadmus-3d-studio. Use via `window.MrBadmusDS.BrandMark` (bundle loaded from the root `_ds_bundle.js`).

## Examples

### WithWordmark

```jsx
() => (
  <div style={{ display: 'flex', alignItems: 'center', gap: 9, padding: '22px 26px', background: '#FBF3E6', borderRadius: 12 }}>
    <BrandMark size={21} />
    <span style={wordmark}>MrBadmusAI</span>
  </div>
)
```

### OnDarkRoom

```jsx
() => (
  <div style={{ display: 'flex', alignItems: 'center', gap: 9, padding: '22px 26px', background: '#15110C', borderRadius: 12 }}>
    <BrandMark size={21} />
    <span style={{ ...wordmark, color: '#FBF3E6' }}>MrBadmusAI</span>
  </div>
)
```

### Sizes

```jsx
() => (
  <div style={{ display: 'flex', alignItems: 'center', gap: 22, padding: '22px 26px', background: '#FBF3E6', borderRadius: 12 }}>
    <BrandMark size={21} />
    <BrandMark size={19} />
    <BrandMark size={17} />
  </div>
)
```
