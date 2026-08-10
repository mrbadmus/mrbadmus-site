var __dsPreview = (() => {
  var __create = Object.create;
  var __defProp = Object.defineProperty;
  var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
  var __getOwnPropNames = Object.getOwnPropertyNames;
  var __getProtoOf = Object.getPrototypeOf;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __esm = (fn, res, err) => function __init() {
    if (err) throw err[0];
    try {
      return fn && (res = (0, fn[__getOwnPropNames(fn)[0]])(fn = 0)), res;
    } catch (e) {
      throw err = [e], e;
    }
  };
  var __commonJS = (cb, mod) => function __require() {
    try {
      return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
    } catch (e) {
      throw mod = 0, e;
    }
  };
  var __export = (target, all) => {
    for (var name in all)
      __defProp(target, name, { get: all[name], enumerable: true });
  };
  var __copyProps = (to, from, except, desc) => {
    if (from && typeof from === "object" || typeof from === "function") {
      for (let key of __getOwnPropNames(from))
        if (!__hasOwnProp.call(to, key) && key !== except)
          __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
    return to;
  };
  var __reExport = (target, mod, secondTarget) => (__copyProps(target, mod, "default"), secondTarget && __copyProps(secondTarget, mod, "default"));
  var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
    // If the importer is in node compatibility mode or this is not an ESM
    // file that has been converted to a CommonJS file using a Babel-
    // compatible transform (i.e. "__esModule" has not been set), then set
    // "default" to the CommonJS "module.exports" for node compatibility.
    isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
    mod
  ));
  var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

  // <define:import.meta.env>
  var init_define_import_meta_env = __esm({
    "<define:import.meta.env>"() {
    }
  });

  // ds-raw:__ds_raw__
  var require_ds_raw = __commonJS({
    "ds-raw:__ds_raw__"(exports, module) {
      init_define_import_meta_env();
      module.exports = window.MrBadmusDS;
    }
  });

  // shim:react-shim
  var require_react_shim = __commonJS({
    "shim:react-shim"(exports, module) {
      init_define_import_meta_env();
      var R = window.React;
      function np(p, k) {
        var o = {};
        for (var x in p) if (x !== "children") o[x] = p[x];
        if (k !== void 0) o.key = k;
        return o;
      }
      function jsx2(t, p, k) {
        var c = p && p.children;
        return c === void 0 ? R.createElement(t, np(p, k)) : R.createElement(t, np(p, k), c);
      }
      function jsxs(t, p, k) {
        return R.createElement.apply(R, [t, np(p, k)].concat(p.children));
      }
      module.exports = R;
      module.exports.jsx = jsx2;
      module.exports.jsxs = jsxs;
      module.exports.jsxDEV = function(t, p, k, s) {
        return (s ? jsxs : jsx2)(t, p, k);
      };
      module.exports.Fragment = R.Fragment;
    }
  });

  // .design-sync/previews/HotspotDot.tsx
  var HotspotDot_exports = {};
  __export(HotspotDot_exports, {
    Closed: () => Closed,
    Hover: () => Hover,
    InertDuringRetrieval: () => InertDuringRetrieval,
    Open: () => Open,
    PaperClosed: () => PaperClosed,
    PaperOpen: () => PaperOpen,
    RetrievalTarget: () => RetrievalTarget
  });
  init_define_import_meta_env();

  // ds-shim:ds
  var ds_exports = {};
  __export(ds_exports, {
    default: () => ds_default
  });
  init_define_import_meta_env();
  __reExport(ds_exports, __toESM(require_ds_raw()));
  var g = window.MrBadmusDS;
  var ds_default = "default" in g ? g.default : g;

  // .design-sync/previews/HotspotDot.tsx
  var import_jsx_runtime = __toESM(require_react_shim());
  var dark = {
    position: "relative",
    width: 150,
    height: 110,
    borderRadius: 11,
    background: "radial-gradient(90% 90% at 50% 40%, #2C261F, #131009)"
  };
  var paper = {
    position: "relative",
    width: 150,
    height: 110,
    borderRadius: 11,
    background: "#FFFDF8",
    border: "1px solid #E4D6BF"
  };
  var Closed = () => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: dark, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ds_exports.HotspotDot, { state: "closed", surface: "dark", numeral: "01", x: 75, y: 55, label: "Structure 01" }) });
  var Hover = () => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: dark, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ds_exports.HotspotDot, { state: "hover", surface: "dark", numeral: "01", x: 75, y: 55, label: "Structure 01" }) });
  var Open = () => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: dark, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ds_exports.HotspotDot, { state: "open", surface: "dark", numeral: "03", x: 75, y: 55, label: "Structure 03" }) });
  var InertDuringRetrieval = () => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: dark, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ds_exports.HotspotDot, { state: "inert", surface: "dark", numeral: "02", x: 75, y: 55 }) });
  var RetrievalTarget = () => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: dark, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ds_exports.HotspotDot, { state: "target", surface: "dark", numeral: "04", x: 75, y: 55, label: "Highlighted structure" }) });
  var PaperClosed = () => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: paper, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ds_exports.HotspotDot, { state: "closed", surface: "paper", numeral: "01", x: 75, y: 55, label: "Structure 01" }) });
  var PaperOpen = () => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: paper, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ds_exports.HotspotDot, { state: "open", surface: "paper", numeral: "01", x: 75, y: 55, label: "Structure 01" }) });
  return __toCommonJS(HotspotDot_exports);
})();
