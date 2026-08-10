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

  // .design-sync/previews/PhoneSheet.tsx
  var PhoneSheet_exports = {};
  __export(PhoneSheet_exports, {
    SheetAtRest: () => SheetAtRest,
    SheetRaised: () => SheetRaised
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

  // .design-sync/previews/PhoneSheet.tsx
  var import_jsx_runtime = __toESM(require_react_shim());
  var specimen = {
    id: "heart",
    renderer: "mesh",
    name: "Human heart",
    epithet: "Lorem ipsum dolor sit amet",
    system: "Circulatory",
    keyStages: ["KS3", "KS4"],
    assets: {
      mesh: "/3d/assets/heart.glb",
      fallback: "/3d/assets/heart-2d.svg",
      thumbnail: "/3d/assets/heart-thumb.webp",
      licence: "royalty-free-perpetual",
      source: "Reference placeholder",
      acquired: "2026-08-09"
    },
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.",
    keyFacts: [
      { label: "Lorem", value: "000 ipsum" },
      { label: "Dolor sit", value: "0.0 × 0.0 amet" },
      { label: "Eiusmod", value: "00 tempor" }
    ],
    callouts: {
      importance: "Lorem ipsum dolor sit amet consectetur adipiscing elit.",
      didYouKnow: "Ut enim ad minim veniam quis nostrud exercitation."
    },
    lessonUrl: "/biology/organisation.html",
    specPoints: ["KS4.B.ORG.04", "KS3.B.BOD.02"],
    hotspots: [
      { id: "heart.item-01", label: "Lorem ipsum", detail: "Lorem ipsum dolor sit amet.", position3d: [0.1, 0.2, 0.3], position2d: [120, 90], tiers: ["foundation", "higher"], retrievable: true },
      { id: "heart.item-02", label: "Dolor sit", detail: "Consectetur adipiscing elit sed.", position3d: [0.2, 0.1, 0.4], position2d: [200, 60], tiers: ["higher"], retrievable: true },
      { id: "heart.item-03", label: "Amet consect.", detail: "Sed do eiusmod tempor.", position3d: [0.3, 0.3, 0.2], position2d: [160, 150], tiers: ["foundation", "higher"], retrievable: false }
    ]
  };
  var phone = {
    position: "relative",
    width: 390,
    height: 700,
    borderRadius: 22,
    overflow: "hidden",
    border: "1px solid #D9C9AC",
    background: "radial-gradient(95% 80% at 50% 42%, #2C261F 0%, #191510 55%, #100D0A 100%)"
  };
  var SheetAtRest = () => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: phone, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(
    ds_exports.PhoneSheet,
    {
      specimen,
      raised: false,
      onRaisedChange: () => {
      },
      openHotspotId: null,
      onOpenHotspot: () => {
      },
      onStartRetrieval: () => {
      }
    }
  ) });
  var SheetRaised = () => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { style: phone, children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(
    ds_exports.PhoneSheet,
    {
      specimen,
      raised: true,
      onRaisedChange: () => {
      },
      openHotspotId: null,
      onOpenHotspot: () => {
      },
      onStartRetrieval: () => {
      }
    }
  ) });
  return __toCommonJS(PhoneSheet_exports);
})();
