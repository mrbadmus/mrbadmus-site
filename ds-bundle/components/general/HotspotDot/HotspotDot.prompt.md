HotspotDot from mrbadmus-3d-studio. Use via `window.MrBadmusDS.HotspotDot` (bundle loaded from the root `_ds_bundle.js`).

## Examples

### Closed

```jsx
() => (
  <div style={dark}>
    <HotspotDot state="closed" surface="dark" numeral="01" x={75} y={55} label="Structure 01" />
  </div>
)
```

### Hover

```jsx
() => (
  <div style={dark}>
    <HotspotDot state="hover" surface="dark" numeral="01" x={75} y={55} label="Structure 01" />
  </div>
)
```

### Open

```jsx
() => (
  <div style={dark}>
    <HotspotDot state="open" surface="dark" numeral="03" x={75} y={55} label="Structure 03" />
  </div>
)
```

### InertDuringRetrieval

```jsx
() => (
  <div style={dark}>
    <HotspotDot state="inert" surface="dark" numeral="02" x={75} y={55} />
  </div>
)
```

### RetrievalTarget

```jsx
() => (
  <div style={dark}>
    <HotspotDot state="target" surface="dark" numeral="04" x={75} y={55} label="Highlighted structure" />
  </div>
)
```

### PaperClosed

```jsx
() => (
  <div style={paper}>
    <HotspotDot state="closed" surface="paper" numeral="01" x={75} y={55} label="Structure 01" />
  </div>
)
```

### PaperOpen

```jsx
() => (
  <div style={paper}>
    <HotspotDot state="open" surface="paper" numeral="01" x={75} y={55} label="Structure 01" />
  </div>
)
```
