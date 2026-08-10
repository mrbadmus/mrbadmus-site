ToolRail from mrbadmus-3d-studio. Use via `window.MrBadmusDS.ToolRail` (bundle loaded from the root `_ds_bundle.js`).

## Examples

### ViewportSevenTools

```jsx
() => (
  <div style={viewportStage} className="stage stage--viewport">
    <ToolRail
      renderer={viewport}
      activeTool="rotate"
      autoRotate={false}
      onTool={() => {}}
      onAutoRotate={() => {}}
    />
  </div>
)
```

### PaperFourTools

```jsx
() => (
  <div style={paperStage} className="stage stage--paper">
    <ToolRail
      renderer={paper}
      activeTool={null}
      autoRotate={false}
      onTool={() => {}}
      onAutoRotate={() => {}}
    />
  </div>
)
```
