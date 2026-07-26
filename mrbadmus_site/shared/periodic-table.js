/* ============================================================
   MrBadmus — PERIODIC TABLE  (Bonding v2 Phase 2B · MRB-136)

   A shared, self-contained periodic table students can pull up
   from any exam-ladder card that needs one. HTML + CSS, never an
   image: it stays legible when zoomed, works with a screen
   reader, and scrolls sideways inside its own box on a phone
   instead of breaking the page layout.

   PUBLIC API:
     MrbPeriodicTable.button(opts)  -> a ready-to-append <button>
                                       that opens the overlay.
                                       opts.label overrides the text.
     MrbPeriodicTable.open()        -> open the overlay
     MrbPeriodicTable.close()       -> close it

   ONE overlay per document. It is built lazily on the first open
   and reused by every button on the page.

   TEACHING DECISIONS (deliberate, see report):
     · Group numbers are labelled the AQA way — 1, 2, 3, 4, 5, 6,
       7, 0 — large, with the modern IUPAC 1–18 shown small
       underneath, so a student can read either exam board style.
     · Hydrogen sits in the group 1 column (its usual place) but
       is coloured as a NON-METAL, because it is one.
     · Group 7 is coloured as halogens all the way down (F, Cl,
       Br, I, At, Ts) and group 0 as noble gases all the way down,
       because that is how group trends are taught.
     · Metalloids are the conventional teaching six: B, Si, Ge,
       As, Sb, Te. Polonium is grouped with the other metals.
     · Elements 104–118 are placed by group; their chemistry is
       barely known. The footnote says so.

   Palette is light-scoped on purpose: the redesign token block
   (--surface-panel, --ink*, --accent-*) is cream-only, so the
   category hues are tuned for dark-ink-on-cream contrast.
============================================================ */
(function () {
  'use strict';
  if (window.MrbPeriodicTable) return;

  /* ---------------------------------------------------------
     STYLES — injected once
  --------------------------------------------------------- */
  var STYLE_ID = 'mrb-pt-styles';

  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      /* --- the toggle button (lives inside a ladder card) --- */
      '.mrb-pt-toggle{display:inline-flex;align-items:center;gap:8px;font-family:var(--font-display,sans-serif);font-weight:600;font-size:calc(13.5px * var(--rd-fs-scale,1));line-height:1.2;color:var(--ink-body,#2A241E);background:var(--surface-inset,#F7F2E8);border:1px solid var(--border,#E4DCCB);border-radius:var(--r-control,12px);padding:10px 16px;cursor:pointer;min-height:44px}',
      '.mrb-pt-toggle:hover{background:var(--accent-wash,#FBEEE9);border-color:var(--accent-tint-border,#F0BBA9)}',
      '.mrb-pt-toggle:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',

      /* --- overlay shell --- */
      '.mrb-pt,.mrb-pt *{box-sizing:border-box}',
      '.mrb-pt{position:fixed;top:0;right:0;bottom:0;left:0;z-index:9999;display:none;align-items:center;justify-content:center;padding:24px;background:var(--pt-scrim,rgba(26,23,20,.62))}',
      '.mrb-pt.is-open{display:flex;animation:mrb-pt-fade .16s ease-out}',
      '@keyframes mrb-pt-fade{from{opacity:0}to{opacity:1}}',
      '@keyframes mrb-pt-rise{from{transform:translateY(14px)}to{transform:none}}',
      '.mrb-pt__sheet{display:flex;flex-direction:column;width:100%;max-width:1260px;max-height:100%;background:var(--surface-panel,#FFFDF8);border:1px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);box-shadow:var(--shadow-panel,0 22px 50px -35px rgba(60,30,20,.5));overflow:hidden;outline:none}',
      '.mrb-pt.is-open .mrb-pt__sheet{animation:mrb-pt-rise .2s ease-out}',

      /* --- header --- */
      '.mrb-pt__head{display:flex;align-items:center;gap:12px;padding:14px 20px;border-bottom:1px solid var(--surface-inset,#EFE7D8);flex:none}',
      '.mrb-pt__title{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(17px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);margin:0}',
      '.mrb-pt__close{margin-left:auto;flex:none;width:44px;height:44px;border-radius:var(--r-pill,999px);border:1px solid var(--border,#E4DCCB);background:var(--surface-inset,#F7F2E8);color:var(--ink-body,#2A241E);font-family:var(--font-body,system-ui,sans-serif);font-size:calc(17px * var(--rd-fs-scale,1));line-height:1;cursor:pointer}',
      '.mrb-pt__close:hover{background:var(--accent-wash,#FBEEE9);border-color:var(--accent-tint-border,#F0BBA9)}',
      '.mrb-pt__close:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',

      /* --- legend --- */
      '.mrb-pt__legend{display:flex;flex-wrap:wrap;gap:7px 16px;margin:0;padding:11px 20px;list-style:none;border-bottom:1px solid var(--surface-inset,#EFE7D8);flex:none}',
      '.mrb-pt__lg{display:inline-flex;align-items:center;gap:7px;font-family:var(--font-body,system-ui,sans-serif);font-size:calc(11.5px * var(--rd-fs-scale,1));line-height:1.3;color:var(--ink-body,#2A241E)}',
      '.mrb-pt__sw{flex:none;width:14px;height:14px;border-radius:4px;background:var(--pt-f,#F7F2E8);border:1.5px solid var(--pt-c,#6B635A)}',

      /* --- scroll box: the table scrolls sideways in HERE, never the page --- */
      /* the inset lives on the grid, not on the scroll box, so the pinned period
         column and group header sit flush against the scrollport edge and no
         cell can peek through a gutter beside them */
      '.mrb-pt__scroll{flex:1 1 auto;min-height:0;overflow:auto;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;padding:0}',
      '.mrb-pt__scroll:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:-2px}',

      /* --- the grid: 1 label column + 18 group columns --- */
      '.mrb-pt{--pt-cell:60px;--pt-gap:3px;--pt-lbl:30px;--pt-head:34px;--pt-split:14px}',
      '.mrb-pt__grid{display:grid;width:max-content;padding:16px 20px 6px;gap:var(--pt-gap);grid-template-columns:var(--pt-lbl) repeat(18,var(--pt-cell));grid-template-rows:var(--pt-head) repeat(7,var(--pt-cell)) var(--pt-split) repeat(2,var(--pt-cell))}',

      /* --- category colours: hue + soft fill, one token pair each --- */
      '.mrb-pt-c-alkali{--pt-c:var(--pt-alkali,#A63C12);--pt-f:var(--pt-alkali-fill,rgba(166,60,18,.13))}',
      '.mrb-pt-c-alkaline{--pt-c:var(--pt-alkaline,#8C5209);--pt-f:var(--pt-alkaline-fill,rgba(140,82,9,.13))}',
      '.mrb-pt-c-transition{--pt-c:var(--pt-transition,#7A5F00);--pt-f:var(--pt-transition-fill,rgba(122,95,0,.13))}',
      '.mrb-pt-c-othermetal{--pt-c:var(--pt-othermetal,#6E6257);--pt-f:var(--pt-othermetal-fill,rgba(110,98,87,.13))}',
      '.mrb-pt-c-metalloid{--pt-c:var(--pt-metalloid,#2A6F7B);--pt-f:var(--pt-metalloid-fill,rgba(42,111,123,.13))}',
      '.mrb-pt-c-nonmetal{--pt-c:var(--pt-nonmetal,#237A3B);--pt-f:var(--pt-nonmetal-fill,rgba(35,122,59,.13))}',
      '.mrb-pt-c-halogen{--pt-c:var(--pt-halogen,#B02342);--pt-f:var(--pt-halogen-fill,rgba(176,35,66,.12))}',
      '.mrb-pt-c-noble{--pt-c:var(--pt-noble,#5B4B8A);--pt-f:var(--pt-noble-fill,rgba(91,75,138,.13))}',
      '.mrb-pt-c-lanthanide{--pt-c:var(--pt-lanthanide,#7A4A62);--pt-f:var(--pt-lanthanide-fill,rgba(122,74,98,.13))}',
      '.mrb-pt-c-actinide{--pt-c:var(--pt-actinide,#6A4A2A);--pt-f:var(--pt-actinide-fill,rgba(106,74,42,.13))}',

      /* --- element cell --- */
      '.mrb-pt__cell{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;padding:2px;min-width:0;overflow:hidden;text-align:center;cursor:pointer;border:1px solid var(--pt-c,#6B635A);border-radius:7px;background:var(--pt-f,#F7F2E8);font-family:var(--font-body,system-ui,sans-serif)}',
      '.mrb-pt__cell:hover{border-width:2px;padding:1px}',
      '.mrb-pt__cell:focus-visible{outline:3px solid var(--accent-strong,#C0392B);outline-offset:1px}',
      '.mrb-pt__cell.is-sel{box-shadow:inset 0 0 0 2px var(--accent-strong,#C0392B)}',
      '.mrb-pt__z{font-family:var(--font-mono,monospace);font-size:calc(var(--pt-cell) * .175);line-height:1;color:var(--ink-muted,#6B635A)}',
      '.mrb-pt__sym{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(var(--pt-cell) * .34);line-height:1.05;color:var(--pt-c,#1A1714)}',
      '.mrb-pt__name{max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:calc(var(--pt-cell) * .14);line-height:1.1;color:var(--ink-body,#2A241E)}',

      /* --- labels, band, f-block placeholders --- */
      /* the group header row and the period column stay pinned while the table scrolls */
      '.mrb-pt__gh{position:sticky;top:0;z-index:3;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:2px;padding-bottom:4px;background:var(--surface-panel,#FFFDF8);font-family:var(--font-mono,monospace)}',
      '.mrb-pt__gh-aqa{font-size:calc(13.5px * var(--rd-fs-scale,1));font-weight:700;line-height:1;color:var(--ink,#1A1714)}',
      '.mrb-pt__gh-iu{font-size:calc(9.5px * var(--rd-fs-scale,1));line-height:1;color:var(--ink-faint,#8A8074)}',
      '.mrb-pt__plbl{position:sticky;left:0;z-index:2;display:flex;align-items:center;justify-content:center;background:var(--surface-panel,#FFFDF8);font-family:var(--font-mono,monospace);font-size:calc(11.5px * var(--rd-fs-scale,1));font-weight:600;color:var(--ink-faint,#8A8074)}',
      '.mrb-pt__band{display:flex;align-items:center;justify-content:center;padding:4px;text-align:center;text-transform:uppercase;letter-spacing:.09em;font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));color:var(--ink-muted,#6B635A);border:1px dashed var(--rule,#D8CFBD);border-radius:10px}',
      '.mrb-pt__ph{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;line-height:1.2;border:1px dashed var(--pt-c,#6B635A);border-radius:7px;background:var(--pt-f,#F7F2E8);font-family:var(--font-mono,monospace);font-size:calc(var(--pt-cell) * .155);color:var(--ink-muted,#6B635A)}',
      '.mrb-pt__fcap{display:flex;align-items:center;justify-content:flex-end;padding-right:7px;text-align:right;line-height:1.2;font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));color:var(--ink-muted,#6B635A)}',
      '.mrb-pt__note{max-width:78ch;margin:4px 20px 18px;font-family:var(--font-body,system-ui,sans-serif);font-size:calc(11.5px * var(--rd-fs-scale,1));line-height:1.55;color:var(--ink-muted,#6B635A)}',

      /* --- detail strip (visual aid; cells carry their own aria-label) --- */
      '.mrb-pt__detail{flex:none;display:flex;flex-wrap:wrap;align-items:baseline;gap:3px 10px;min-height:46px;padding:11px 20px;border-top:1px solid var(--surface-inset,#EFE7D8);background:var(--surface-inset,#F7F2E8);font-family:var(--font-body,system-ui,sans-serif);font-size:calc(13px * var(--rd-fs-scale,1));color:var(--ink-body,#2A241E)}',
      '.mrb-pt__d-sym{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(16px * var(--rd-fs-scale,1));color:var(--pt-c,#1A1714)}',
      '.mrb-pt__d-name{font-weight:600}',
      '.mrb-pt__d-meta{color:var(--ink-muted,#6B635A)}',
      '.mrb-pt__sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}',

      /* --- responsive: full-screen sheet + smaller cells on a phone --- */
      '@media (max-width:1100px){.mrb-pt{--pt-cell:54px}}',
      '@media (max-width:760px){.mrb-pt{padding:0}.mrb-pt__sheet{max-width:none;height:100%;max-height:100%;border:none;border-radius:0}}',
      '@media (max-width:620px){.mrb-pt{--pt-cell:46px;--pt-gap:2px;--pt-lbl:22px}.mrb-pt__grid{padding:12px 14px 4px}.mrb-pt__note{margin:4px 14px 16px}.mrb-pt__name{display:none}.mrb-pt__z{font-size:calc(9px * var(--rd-fs-scale,1))}.mrb-pt__sym{font-size:calc(17px * var(--rd-fs-scale,1))}.mrb-pt__ph{font-size:calc(8.5px * var(--rd-fs-scale,1))}.mrb-pt__legend{gap:6px 12px;padding:9px 14px}.mrb-pt__head{padding:11px 14px}.mrb-pt__detail{padding:10px 14px}}',
      /* no smaller than 46px below this: cells stay a comfortable tap target,
         and the table scrolls sideways anyway so shrinking buys nothing */
      '@media (prefers-reduced-motion:reduce){.mrb-pt.is-open,.mrb-pt.is-open .mrb-pt__sheet{animation:none}}'
    ].join('');
    document.head.appendChild(s);
  }

  /* ---------------------------------------------------------
     ELEMENT DATA
     [ atomic number, symbol, name (UK spelling), category,
       row, column ]
     row 1-7  = periods 1-7 of the main block
     row 8    = lanthanide row      row 9 = actinide row
     column   = 1-18 (IUPAC group columns)
  --------------------------------------------------------- */
  var ELEMENTS = [
    [1, 'H', 'hydrogen', 'nonmetal', 1, 1],
    [2, 'He', 'helium', 'noble', 1, 18],
    [3, 'Li', 'lithium', 'alkali', 2, 1],
    [4, 'Be', 'beryllium', 'alkaline', 2, 2],
    [5, 'B', 'boron', 'metalloid', 2, 13],
    [6, 'C', 'carbon', 'nonmetal', 2, 14],
    [7, 'N', 'nitrogen', 'nonmetal', 2, 15],
    [8, 'O', 'oxygen', 'nonmetal', 2, 16],
    [9, 'F', 'fluorine', 'halogen', 2, 17],
    [10, 'Ne', 'neon', 'noble', 2, 18],
    [11, 'Na', 'sodium', 'alkali', 3, 1],
    [12, 'Mg', 'magnesium', 'alkaline', 3, 2],
    [13, 'Al', 'aluminium', 'othermetal', 3, 13],
    [14, 'Si', 'silicon', 'metalloid', 3, 14],
    [15, 'P', 'phosphorus', 'nonmetal', 3, 15],
    [16, 'S', 'sulfur', 'nonmetal', 3, 16],
    [17, 'Cl', 'chlorine', 'halogen', 3, 17],
    [18, 'Ar', 'argon', 'noble', 3, 18],
    [19, 'K', 'potassium', 'alkali', 4, 1],
    [20, 'Ca', 'calcium', 'alkaline', 4, 2],
    [21, 'Sc', 'scandium', 'transition', 4, 3],
    [22, 'Ti', 'titanium', 'transition', 4, 4],
    [23, 'V', 'vanadium', 'transition', 4, 5],
    [24, 'Cr', 'chromium', 'transition', 4, 6],
    [25, 'Mn', 'manganese', 'transition', 4, 7],
    [26, 'Fe', 'iron', 'transition', 4, 8],
    [27, 'Co', 'cobalt', 'transition', 4, 9],
    [28, 'Ni', 'nickel', 'transition', 4, 10],
    [29, 'Cu', 'copper', 'transition', 4, 11],
    [30, 'Zn', 'zinc', 'transition', 4, 12],
    [31, 'Ga', 'gallium', 'othermetal', 4, 13],
    [32, 'Ge', 'germanium', 'metalloid', 4, 14],
    [33, 'As', 'arsenic', 'metalloid', 4, 15],
    [34, 'Se', 'selenium', 'nonmetal', 4, 16],
    [35, 'Br', 'bromine', 'halogen', 4, 17],
    [36, 'Kr', 'krypton', 'noble', 4, 18],
    [37, 'Rb', 'rubidium', 'alkali', 5, 1],
    [38, 'Sr', 'strontium', 'alkaline', 5, 2],
    [39, 'Y', 'yttrium', 'transition', 5, 3],
    [40, 'Zr', 'zirconium', 'transition', 5, 4],
    [41, 'Nb', 'niobium', 'transition', 5, 5],
    [42, 'Mo', 'molybdenum', 'transition', 5, 6],
    [43, 'Tc', 'technetium', 'transition', 5, 7],
    [44, 'Ru', 'ruthenium', 'transition', 5, 8],
    [45, 'Rh', 'rhodium', 'transition', 5, 9],
    [46, 'Pd', 'palladium', 'transition', 5, 10],
    [47, 'Ag', 'silver', 'transition', 5, 11],
    [48, 'Cd', 'cadmium', 'transition', 5, 12],
    [49, 'In', 'indium', 'othermetal', 5, 13],
    [50, 'Sn', 'tin', 'othermetal', 5, 14],
    [51, 'Sb', 'antimony', 'metalloid', 5, 15],
    [52, 'Te', 'tellurium', 'metalloid', 5, 16],
    [53, 'I', 'iodine', 'halogen', 5, 17],
    [54, 'Xe', 'xenon', 'noble', 5, 18],
    [55, 'Cs', 'caesium', 'alkali', 6, 1],
    [56, 'Ba', 'barium', 'alkaline', 6, 2],
    [57, 'La', 'lanthanum', 'lanthanide', 8, 3],
    [58, 'Ce', 'cerium', 'lanthanide', 8, 4],
    [59, 'Pr', 'praseodymium', 'lanthanide', 8, 5],
    [60, 'Nd', 'neodymium', 'lanthanide', 8, 6],
    [61, 'Pm', 'promethium', 'lanthanide', 8, 7],
    [62, 'Sm', 'samarium', 'lanthanide', 8, 8],
    [63, 'Eu', 'europium', 'lanthanide', 8, 9],
    [64, 'Gd', 'gadolinium', 'lanthanide', 8, 10],
    [65, 'Tb', 'terbium', 'lanthanide', 8, 11],
    [66, 'Dy', 'dysprosium', 'lanthanide', 8, 12],
    [67, 'Ho', 'holmium', 'lanthanide', 8, 13],
    [68, 'Er', 'erbium', 'lanthanide', 8, 14],
    [69, 'Tm', 'thulium', 'lanthanide', 8, 15],
    [70, 'Yb', 'ytterbium', 'lanthanide', 8, 16],
    [71, 'Lu', 'lutetium', 'lanthanide', 8, 17],
    [72, 'Hf', 'hafnium', 'transition', 6, 4],
    [73, 'Ta', 'tantalum', 'transition', 6, 5],
    [74, 'W', 'tungsten', 'transition', 6, 6],
    [75, 'Re', 'rhenium', 'transition', 6, 7],
    [76, 'Os', 'osmium', 'transition', 6, 8],
    [77, 'Ir', 'iridium', 'transition', 6, 9],
    [78, 'Pt', 'platinum', 'transition', 6, 10],
    [79, 'Au', 'gold', 'transition', 6, 11],
    [80, 'Hg', 'mercury', 'transition', 6, 12],
    [81, 'Tl', 'thallium', 'othermetal', 6, 13],
    [82, 'Pb', 'lead', 'othermetal', 6, 14],
    [83, 'Bi', 'bismuth', 'othermetal', 6, 15],
    [84, 'Po', 'polonium', 'othermetal', 6, 16],
    [85, 'At', 'astatine', 'halogen', 6, 17],
    [86, 'Rn', 'radon', 'noble', 6, 18],
    [87, 'Fr', 'francium', 'alkali', 7, 1],
    [88, 'Ra', 'radium', 'alkaline', 7, 2],
    [89, 'Ac', 'actinium', 'actinide', 9, 3],
    [90, 'Th', 'thorium', 'actinide', 9, 4],
    [91, 'Pa', 'protactinium', 'actinide', 9, 5],
    [92, 'U', 'uranium', 'actinide', 9, 6],
    [93, 'Np', 'neptunium', 'actinide', 9, 7],
    [94, 'Pu', 'plutonium', 'actinide', 9, 8],
    [95, 'Am', 'americium', 'actinide', 9, 9],
    [96, 'Cm', 'curium', 'actinide', 9, 10],
    [97, 'Bk', 'berkelium', 'actinide', 9, 11],
    [98, 'Cf', 'californium', 'actinide', 9, 12],
    [99, 'Es', 'einsteinium', 'actinide', 9, 13],
    [100, 'Fm', 'fermium', 'actinide', 9, 14],
    [101, 'Md', 'mendelevium', 'actinide', 9, 15],
    [102, 'No', 'nobelium', 'actinide', 9, 16],
    [103, 'Lr', 'lawrencium', 'actinide', 9, 17],
    [104, 'Rf', 'rutherfordium', 'transition', 7, 4],
    [105, 'Db', 'dubnium', 'transition', 7, 5],
    [106, 'Sg', 'seaborgium', 'transition', 7, 6],
    [107, 'Bh', 'bohrium', 'transition', 7, 7],
    [108, 'Hs', 'hassium', 'transition', 7, 8],
    [109, 'Mt', 'meitnerium', 'transition', 7, 9],
    [110, 'Ds', 'darmstadtium', 'transition', 7, 10],
    [111, 'Rg', 'roentgenium', 'transition', 7, 11],
    [112, 'Cn', 'copernicium', 'transition', 7, 12],
    [113, 'Nh', 'nihonium', 'othermetal', 7, 13],
    [114, 'Fl', 'flerovium', 'othermetal', 7, 14],
    [115, 'Mc', 'moscovium', 'othermetal', 7, 15],
    [116, 'Lv', 'livermorium', 'othermetal', 7, 16],
    [117, 'Ts', 'tennessine', 'halogen', 7, 17],
    [118, 'Og', 'oganesson', 'noble', 7, 18]
  ];

  /* Legend order + the singular wording used in aria labels. */
  var CATS = [
    ['alkali', 'Alkali metals', 'alkali metal'],
    ['alkaline', 'Alkaline earth metals', 'alkaline earth metal'],
    ['transition', 'Transition metals', 'transition metal'],
    ['othermetal', 'Other metals', 'other metal'],
    ['metalloid', 'Metalloids', 'metalloid'],
    ['nonmetal', 'Non-metals', 'non-metal'],
    ['halogen', 'Halogens (group 7)', 'halogen'],
    ['noble', 'Noble gases (group 0)', 'noble gas'],
    ['lanthanide', 'Lanthanides', 'lanthanide'],
    ['actinide', 'Actinides', 'actinide']
  ];

  var CAT_ONE = {};
  (function () {
    for (var i = 0; i < CATS.length; i++) CAT_ONE[CATS[i][0]] = CATS[i][2];
  })();

  /* AQA (old) group numbers by column. Blank = transition block. */
  var AQA_GROUP = {
    1: '1', 2: '2', 13: '3', 14: '4', 15: '5', 16: '6', 17: '7', 18: '0'
  };

  /* ---------------------------------------------------------
     TINY DOM HELPER
  --------------------------------------------------------- */
  function el(tag, opts, kids) {
    var n = document.createElement(tag);
    if (opts) {
      if (opts.className) n.className = opts.className;
      if (opts.text != null) n.textContent = opts.text;
      if (opts.style) n.setAttribute('style', opts.style);
      if (opts.attrs) {
        for (var k in opts.attrs) {
          if (Object.prototype.hasOwnProperty.call(opts.attrs, k)) {
            n.setAttribute(k, opts.attrs[k]);
          }
        }
      }
    }
    if (kids) {
      for (var i = 0; i < kids.length; i++) if (kids[i]) n.appendChild(kids[i]);
    }
    return n;
  }

  /* data row -> CSS grid row (row 1 of the grid is the group header,
     and rows 8/9 sit below a spacer row) */
  function gridRow(row) { return row <= 7 ? row + 1 : row + 2; }
  /* data column -> CSS grid column (column 1 of the grid is the period label) */
  function gridCol(col) { return col + 1; }

  function periodOf(row) {
    if (row === 8) return 6;
    if (row === 9) return 7;
    return row;
  }

  function placeLabel(row, col) {
    if (row === 8) return 'lanthanides row';
    if (row === 9) return 'actinides row';
    if (AQA_GROUP[col]) return 'group ' + AQA_GROUP[col];
    return 'transition metals block';
  }

  /* ---------------------------------------------------------
     OVERLAY STATE (one overlay, built lazily, reused)
  --------------------------------------------------------- */
  var overlay = null;
  var sheet = null;
  var detail = null;
  var cellByPos = null;   /* 'row:col' -> button */
  var current = null;     /* the roving-tabindex cell */
  var isOpen = false;
  var lastFocus = null;
  var prevOverflow = '';
  var toggles = [];

  function setDetail(rec) {
    if (!detail) return;
    while (detail.firstChild) detail.removeChild(detail.firstChild);
    if (!rec) {
      detail.className = 'mrb-pt__detail';
      detail.appendChild(el('span', {
        className: 'mrb-pt__d-meta',
        text: 'Tap an element for its details. Arrow keys move around the table.'
      }));
      return;
    }
    detail.className = 'mrb-pt__detail mrb-pt-c-' + rec[3];
    detail.appendChild(el('span', { className: 'mrb-pt__d-sym', text: rec[1] }));
    detail.appendChild(el('span', { className: 'mrb-pt__d-name', text: rec[2] }));
    detail.appendChild(el('span', {
      className: 'mrb-pt__d-meta',
      text: 'atomic number ' + rec[0] +
        ' · ' + placeLabel(rec[4], rec[5]) +
        ' · period ' + periodOf(rec[4]) +
        ' · ' + CAT_ONE[rec[3]]
    }));
  }

  function setCurrent(cell) {
    if (current === cell) return;
    if (current) {
      current.setAttribute('tabindex', '-1');
      current.className = current.className.replace(' is-sel', '');
    }
    current = cell;
    if (current) {
      current.setAttribute('tabindex', '0');
      if (current.className.indexOf('is-sel') === -1) current.className += ' is-sel';
      setDetail(ELEMENTS[+current.getAttribute('data-i')]);
    }
  }

  function step(cell, dr, dc) {
    var r = +cell.getAttribute('data-r');
    var c = +cell.getAttribute('data-c');
    for (var n = 1; n <= 20; n++) {
      var nr = r + dr * n;
      var nc = c + dc * n;
      if (nr < 1 || nr > 9 || nc < 1 || nc > 18) return null;
      var hit = cellByPos[nr + ':' + nc];
      if (hit) return hit;
    }
    return null;
  }

  function rowEdge(cell, dir) {
    var r = +cell.getAttribute('data-r');
    var found = null;
    for (var c = 1; c <= 18; c++) {
      var hit = cellByPos[r + ':' + (dir > 0 ? c : 19 - c)];
      if (hit) { found = hit; break; }
    }
    return found;
  }

  function onGridKey(e) {
    var cell = e.target;
    if (!cell || !cell.getAttribute || cell.getAttribute('data-r') == null) return;
    var key = e.key;
    var next = null;
    if (key === 'ArrowRight' || e.keyCode === 39) next = step(cell, 0, 1);
    else if (key === 'ArrowLeft' || e.keyCode === 37) next = step(cell, 0, -1);
    else if (key === 'ArrowDown' || e.keyCode === 40) next = step(cell, 1, 0);
    else if (key === 'ArrowUp' || e.keyCode === 38) next = step(cell, -1, 0);
    else if (key === 'Home' || e.keyCode === 36) next = rowEdge(cell, 1);
    else if (key === 'End' || e.keyCode === 35) next = rowEdge(cell, -1);
    else return;
    if (next) {
      e.preventDefault();
      setCurrent(next);
      next.focus();
    }
  }

  function buildGrid() {
    var grid = el('div', {
      className: 'mrb-pt__grid',
      attrs: {
        role: 'group',
        'aria-label': 'Periodic table of the elements',
        'aria-describedby': 'mrb-pt-hint'
      }
    });

    /* group headers: AQA number large, IUPAC number small */
    for (var c = 1; c <= 18; c++) {
      var kids = [];
      if (AQA_GROUP[c]) {
        kids.push(el('span', { className: 'mrb-pt__gh-aqa', text: AQA_GROUP[c] }));
      }
      kids.push(el('span', { className: 'mrb-pt__gh-iu', text: String(c) }));
      grid.appendChild(el('div', {
        className: 'mrb-pt__gh',
        style: 'grid-row:1;grid-column:' + gridCol(c),
        attrs: { 'aria-hidden': 'true' }
      }, kids));
    }

    /* period labels down the left */
    for (var p = 1; p <= 7; p++) {
      grid.appendChild(el('div', {
        className: 'mrb-pt__plbl',
        style: 'grid-row:' + gridRow(p) + ';grid-column:1',
        text: String(p),
        attrs: { 'aria-hidden': 'true' }
      }));
    }

    /* transition-metal band, parked in the empty block of periods 2-3 */
    grid.appendChild(el('div', {
      className: 'mrb-pt__band',
      style: 'grid-row:' + gridRow(2) + ' / span 2;grid-column:' + gridCol(3) + ' / span 10',
      text: 'transition metals',
      attrs: { 'aria-hidden': 'true' }
    }));

    /* f-block placeholders in the main block */
    grid.appendChild(el('div', {
      className: 'mrb-pt__ph mrb-pt-c-lanthanide',
      style: 'grid-row:' + gridRow(6) + ';grid-column:' + gridCol(3),
      attrs: { 'aria-hidden': 'true' }
    }, [
      el('span', { text: '57–71' }),
      el('span', { text: 'La–Lu' })
    ]));
    grid.appendChild(el('div', {
      className: 'mrb-pt__ph mrb-pt-c-actinide',
      style: 'grid-row:' + gridRow(7) + ';grid-column:' + gridCol(3),
      attrs: { 'aria-hidden': 'true' }
    }, [
      el('span', { text: '89–103' }),
      el('span', { text: 'Ac–Lr' })
    ]));

    /* captions for the two detached rows */
    grid.appendChild(el('div', {
      className: 'mrb-pt__fcap',
      style: 'grid-row:' + gridRow(8) + ';grid-column:1 / span 3',
      text: 'lanthanides',
      attrs: { 'aria-hidden': 'true' }
    }));
    grid.appendChild(el('div', {
      className: 'mrb-pt__fcap',
      style: 'grid-row:' + gridRow(9) + ';grid-column:1 / span 3',
      text: 'actinides',
      attrs: { 'aria-hidden': 'true' }
    }));

    /* the elements */
    cellByPos = {};
    for (var i = 0; i < ELEMENTS.length; i++) {
      var rec = ELEMENTS[i];
      var label = 'Element ' + rec[0] + ', ' + rec[2] + ', ' + rec[1] +
        ', ' + placeLabel(rec[4], rec[5]) +
        ', period ' + periodOf(rec[4]) +
        ', ' + CAT_ONE[rec[3]];
      var cell = el('button', {
        className: 'mrb-pt__cell mrb-pt-c-' + rec[3],
        style: 'grid-row:' + gridRow(rec[4]) + ';grid-column:' + gridCol(rec[5]),
        attrs: {
          type: 'button',
          tabindex: '-1',
          'aria-label': label,
          'data-i': String(i),
          'data-r': String(rec[4]),
          'data-c': String(rec[5])
        }
      }, [
        el('span', { className: 'mrb-pt__z', text: String(rec[0]) }),
        el('span', { className: 'mrb-pt__sym', text: rec[1] }),
        el('span', { className: 'mrb-pt__name', text: rec[2] })
      ]);
      cellByPos[rec[4] + ':' + rec[5]] = cell;
      grid.appendChild(cell);
    }

    grid.addEventListener('keydown', onGridKey);
    grid.addEventListener('click', function (e) {
      var t = e.target;
      while (t && t !== grid && (!t.getAttribute || t.getAttribute('data-i') == null)) {
        t = t.parentNode;
      }
      if (t && t !== grid) { setCurrent(t); t.focus(); }
    });

    return grid;
  }

  function buildLegend() {
    var list = el('ul', {
      className: 'mrb-pt__legend',
      attrs: { 'aria-label': 'Colour key' }
    });
    for (var i = 0; i < CATS.length; i++) {
      list.appendChild(el('li', { className: 'mrb-pt__lg mrb-pt-c-' + CATS[i][0] }, [
        el('span', { className: 'mrb-pt__sw', attrs: { 'aria-hidden': 'true' } }),
        el('span', { text: CATS[i][1] })
      ]));
    }
    return list;
  }

  function focusables() {
    if (!sheet) return [];
    var all = sheet.querySelectorAll(
      'button:not([disabled]),[href],input,select,textarea,[tabindex]'
    );
    var out = [];
    for (var i = 0; i < all.length; i++) {
      if (all[i].getAttribute('tabindex') === '-1') continue;
      if (all[i].offsetParent === null && all[i] !== sheet) continue;
      out.push(all[i]);
    }
    return out;
  }

  function trapTab(e) {
    var list = focusables();
    if (!list.length) { e.preventDefault(); return; }
    var first = list[0];
    var last = list[list.length - 1];
    var active = document.activeElement;
    if (!sheet.contains(active)) { e.preventDefault(); first.focus(); return; }
    if (e.shiftKey && active === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && active === last) { e.preventDefault(); first.focus(); }
  }

  function onKeydown(e) {
    if (!isOpen) return;
    if (e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27) {
      e.preventDefault();
      close();
      return;
    }
    if (e.key === 'Tab' || e.keyCode === 9) trapTab(e);
  }

  function buildOverlay() {
    ensureStyles();

    var closeBtn = el('button', {
      className: 'mrb-pt__close',
      text: '✕',
      attrs: { type: 'button', 'aria-label': 'Close the periodic table' }
    });
    closeBtn.addEventListener('click', function () { close(); });

    var head = el('div', { className: 'mrb-pt__head' }, [
      el('h2', { className: 'mrb-pt__title', text: 'Periodic table' }),
      closeBtn
    ]);

    var note = el('p', {
      className: 'mrb-pt__note',
      attrs: { id: 'mrb-pt-hint' },
      text: 'Big group numbers are the ones AQA uses (1, 2, 3, 4, 5, 6, 7, 0); ' +
        'the small grey numbers are the modern 1–18 labels. Hydrogen sits above ' +
        'group 1 but is a non-metal, so it is coloured as one. Elements 104–118 ' +
        'are placed by group — almost nothing is known about their chemistry. ' +
        'Use the arrow keys to move between elements.'
    });

    var scroll = el('div', {
      className: 'mrb-pt__scroll',
      attrs: { tabindex: '0', role: 'region', 'aria-label': 'Periodic table, scrolls sideways' }
    }, [buildGrid(), note]);

    detail = el('div', {
      className: 'mrb-pt__detail',
      attrs: { 'aria-hidden': 'true' }
    });
    setDetail(null);

    sheet = el('div', {
      className: 'mrb-pt__sheet',
      attrs: {
        role: 'dialog',
        'aria-modal': 'true',
        'aria-label': 'Periodic table',
        tabindex: '-1'
      }
    }, [head, buildLegend(), scroll, detail]);

    overlay = el('div', { className: 'mrb-pt' }, [sheet]);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) close();
    });

    document.body.appendChild(overlay);

    /* start the roving tabindex on hydrogen */
    setCurrent(cellByPos['1:1']);
    setDetail(null);
    return overlay;
  }

  function syncToggles() {
    for (var i = 0; i < toggles.length; i++) {
      toggles[i].setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    }
  }

  function open(trigger) {
    if (!overlay) buildOverlay();
    if (isOpen) return;
    lastFocus = (trigger && trigger.focus) ? trigger : document.activeElement;
    prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    overlay.className = 'mrb-pt is-open';
    isOpen = true;
    syncToggles();
    document.addEventListener('keydown', onKeydown, true);
    sheet.focus();
  }

  function close() {
    if (!isOpen || !overlay) return;
    overlay.className = 'mrb-pt';
    document.body.style.overflow = prevOverflow;
    isOpen = false;
    syncToggles();
    document.removeEventListener('keydown', onKeydown, true);
    if (lastFocus && lastFocus.focus) {
      try { lastFocus.focus(); } catch (err) { /* element may be gone */ }
    }
    lastFocus = null;
  }

  function button(opts) {
    ensureStyles();
    var label = (opts && opts.label) ? opts.label : 'Show periodic table';
    var b = el('button', {
      className: 'mrb-pt-toggle',
      text: label,
      attrs: {
        type: 'button',
        'aria-haspopup': 'dialog',
        'aria-expanded': isOpen ? 'true' : 'false'
      }
    });
    b.addEventListener('click', function () { open(b); });
    toggles.push(b);
    return b;
  }

  window.MrbPeriodicTable = {
    button: button,
    open: function () { open(null); },
    close: function () { close(); }
  };
})();
