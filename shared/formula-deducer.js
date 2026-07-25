/* ============================================================
   MrBadmus — FORMULA DEDUCER  (Bonding v2 Phase 2B · MRB-136)

   Rung ② engine for the exam ladder. Registers as 'formula' and
   renders the inside of one ladder card per authored §5 item
   (window.MrbExamContent[<page>].formula).

   THE IDEA: the live charge meter.
   The student sets how many of each ion they are using with real
   + / − buttons. The meter shows the running arithmetic
       3 × (2+)  +  2 × (3−)  =  0
   and updates on every tap. Balance is the visible, learnable
   thing — but balance alone is NOT the answer: the formula must
   also be the lowest whole-number ratio (F7/F8 encode that trap
   as the not-simplified distractor, and a meter reading 0 at 2:2
   is still graded a miss).

   WRONG BUILDS GET A NAMED MISCONCEPTION, NEVER "try again".
   The build is composed to a plain-ASCII formula and matched
   against the authored item.distractors[]. On a match the item's
   own slug is printed verbatim in a .mrb-slug span — those slugs
   are join keys into the MRB-135 MCQ banks and must reach the
   shipped DOM character-for-character. The statement is looked up
   from ctx.content.misconceptions (by m.slug or m.slugs[]); the
   four §5-only slugs (wrong-ratio, not-simplified,
   wrong-charge-used, missing-brackets) have no register entry, so
   there is a local fallback statement for each.

   POLYATOMIC IONS (5C, optional set): an ion is treated as
   polyatomic when its symbol is NOT a single element symbol —
   test: /^[A-Z][a-z]?$/ fails. Na, Mg, Cl, X all pass (monatomic);
   OH, SO4, NO3, NH4 all fail (polyatomic). Those need brackets at
   count 2+ — Ca(OH)2, not CaOH2 — so their tile carries a bracket
   toggle, defaulted OFF, and leaving it off at count 2+ is what
   surfaces the missing-brackets misconception.

   TILE START: both counts start at 1, and 1 is the floor.
   An ionic compound always contains at least one of each ion, so
   0 is not a chemically meaningful build; worse, 0:0 would read
   "= 0 · balanced" on the meter and teach zero-by-emptiness as if
   it were zero-by-balance. Starting at 1:1 also puts the
   one-of-each-ion misconception on screen as the default, so the
   student has to actively decide whether it is right (F1/F2/F9
   are the authored starter items where it is).

   Never mutates item or anything under ctx.content.
   ES5 only — no build step exists on this site.
============================================================ */
(function () {
  'use strict';
  if (!window.MrbExamLadder) return;

  /* ---------- helpers (house style: shared/tap-match.js) ---------- */
  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) {
      if (attrs.className) n.className = attrs.className;
      if (attrs.style) for (var k in attrs.style) n.style[k] = attrs.style[k];
      if (attrs.on) for (var ev in attrs.on) n.addEventListener(ev, attrs.on[ev]);
      if (attrs.attrs) for (var a in attrs.attrs) n.setAttribute(a, attrs.attrs[a]);
    }
    if (kids != null) {
      if (!Array.isArray(kids)) kids = [kids];
      kids.forEach(function (c) { if (c != null) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    }
    return n;
  }

  var MIN_COUNT = 1;
  var MAX_COUNT = 6;   /* largest authored count is 3; 6 leaves room to build the 2:4 style non-simplified traps */

  /* ---------- pure core (composer + matcher) ----------
     Kept free of the DOM so the node harness can drive it directly. */

  /* A single element symbol is one capital plus an optional lower-case
     letter. Anything else — OH (two capitals), SO4/NO3/NH4 (a digit) —
     is a group that travels together and needs brackets above one.
     Structural, so it does not depend on a display field being
     authored (a future bank could add display to a monatomic ion). */
  function isPolyatomic(ion) {
    if (!ion || ion.symbol == null) return false;
    return !/^[A-Z][a-z]?$/.test(String(ion.symbol));
  }

  function part(ion, n, brackets) {
    var sym = String(ion.symbol);
    var body = (brackets && n > 1 && isPolyatomic(ion)) ? '(' + sym + ')' : sym;
    return body + (n > 1 ? String(n) : '');
  }

  /* Plain-ASCII formula for a build. The two bracket decisions are
     separate because each polyatomic tile carries its own toggle.
     Both true is the chemist's form, which is what the answer key
     (item.correctFormula) is written in. */
  function compose(cation, nc, anion, na, bCation, bAnion) {
    return part(cation, nc, bCation) + part(anion, na, bAnion);
  }

  function gcd(a, b) {
    a = Math.abs(a); b = Math.abs(b);
    while (b) { var t = b; b = a % b; a = t; }
    return a || 1;
  }

  function netCharge(item, nc, na) {
    return nc * item.cation.charge + na * item.anion.charge;
  }

  /* Exact string match against the authored distractor bank. */
  function findDistractor(item, formula) {
    var list = item.distractors || [];
    for (var i = 0; i < list.length; i++) {
      if (list[i] && list[i].formula === formula) return list[i];
    }
    return null;
  }

  /* The whole grading decision for one build.
     Authored data always wins; the generic diagnostics only run for a
     build the author did not anticipate. Order matters:
       correct → authored distractor → brackets → simplification → balance */
  function classify(item, nc, na, bCation, bAnion) {
    var built = compose(item.cation, nc, item.anion, na, bCation, bAnion);
    var canonical = compose(item.cation, nc, item.anion, na, true, true);
    var out = { formula: built, canonical: canonical, correct: false, slug: null, distractor: null, kind: null };

    if (built === item.correctFormula) { out.correct = true; out.kind = 'correct'; return out; }

    var d = findDistractor(item, built);
    if (d) { out.distractor = d; out.slug = d.slug || null; out.kind = 'authored'; return out; }

    /* right ratio, written without the brackets the group ion needs */
    if (canonical === item.correctFormula) { out.slug = 'missing-brackets'; out.kind = 'brackets'; return out; }

    var net = netCharge(item, nc, na);
    if (net === 0 && gcd(nc, na) > 1) { out.slug = 'not-simplified'; out.kind = 'ratio'; return out; }
    out.slug = net === 0 ? 'missing-brackets' : 'wrong-ratio';
    out.kind = net === 0 ? 'brackets' : 'ratio';
    return out;
  }

  /* ---------- naming (presentation only — the §5 bank carries no
     name field, so tiles fall back to this table; item.cation.name /
     item.anion.name always win if a future bank supplies them) ---------- */
  var ION_NAMES = {
    Li: 'lithium', Na: 'sodium', K: 'potassium', Mg: 'magnesium', Ca: 'calcium',
    Al: 'aluminium', Fe: 'iron', Cu: 'copper', Zn: 'zinc', Ag: 'silver', Pb: 'lead',
    F: 'fluoride', Cl: 'chloride', Br: 'bromide', I: 'iodide',
    O: 'oxide', S: 'sulfide', N: 'nitride',
    OH: 'hydroxide', NO3: 'nitrate', SO4: 'sulfate', CO3: 'carbonate', NH4: 'ammonium'
  };
  /* metals that need a Roman numeral because they form more than one ion */
  var VARIABLE_VALENCY = { Fe: 1, Cu: 1, Mn: 1, Co: 1, Ni: 1, Cr: 1, Pb: 1, Sn: 1, Ti: 1, V: 1 };
  var ROMAN = ['', 'I', 'II', 'III', 'IV', 'V', 'VI'];

  function ionNoun(ion, item, isCation) {
    if (ion.name) return ion.name;
    if (item.abstract) return String(ion.symbol);
    var base = ION_NAMES[String(ion.symbol)];
    if (!base) return String(ion.symbol);
    if (isCation && item.chargeGiven && VARIABLE_VALENCY[String(ion.symbol)]) {
      var r = ROMAN[Math.abs(ion.charge)] || String(Math.abs(ion.charge));
      return base + '(' + r + ')';
    }
    return base;
  }

  function ionPhrase(ion, item, isCation, n) {
    return ionNoun(ion, item, isCation) + (n === 1 ? ' ion' : ' ions');
  }

  /* ---------- charge formatting ---------- */
  var MINUS = '−';   /* the authored content uses the true minus sign */

  function chargeText(c) { return String(Math.abs(c)) + (c < 0 ? MINUS : '+'); }
  function chargeSup(c) { return (Math.abs(c) === 1 ? '' : String(Math.abs(c))) + (c < 0 ? MINUS : '+'); }
  function totalText(t) { return t === 0 ? '0' : (t < 0 ? MINUS : '+') + String(Math.abs(t)); }
  function chargeWords(c) { return String(Math.abs(c)) + (c < 0 ? ' minus' : ' plus'); }
  function totalWords(t) { return t === 0 ? 'zero' : chargeWords(t); }

  /* ---------- DOM builders for chemistry ---------- */
  function ionGlyph(ion) {
    /* authored display wins verbatim (polyatomic ions carry it); otherwise
       compose symbol + a real <sup> charge */
    if (ion.display) return el('span', null, String(ion.display));
    return el('span', null, [String(ion.symbol), el('sup', null, chargeSup(ion.charge))]);
  }

  /* Plain-ASCII formula to DOM with real <sub> digits: Ca(OH)2 → Ca(OH)₂ */
  function formulaNode(ascii, className) {
    var node = el('span', { className: className || 'mrb-fd__f' });
    var buf = '';
    var s = String(ascii);
    for (var i = 0; i < s.length; i++) {
      var ch = s.charAt(i);
      if (ch >= '0' && ch <= '9') {
        if (buf) { node.appendChild(document.createTextNode(buf)); buf = ''; }
        var run = '';
        while (i < s.length && s.charAt(i) >= '0' && s.charAt(i) <= '9') { run += s.charAt(i); i++; }
        i--;
        node.appendChild(el('sub', null, run));
      } else { buf += ch; }
    }
    if (buf) node.appendChild(document.createTextNode(buf));
    return node;
  }

  /* Authored display strings (unicode subscripts) go in verbatim; only
     fall back to composing from the ASCII form when none was authored. */
  function authoredFormulaNode(ascii, display, className) {
    if (display) return el('span', { className: className || 'mrb-fd__f' }, String(display));
    return formulaNode(ascii, className);
  }

  /* ---------- misconception copy ---------- */
  function lookupStatement(ctx, slug) {
    var list = (ctx && ctx.content && ctx.content.misconceptions) || [];
    for (var i = 0; i < list.length; i++) {
      var m = list[i];
      if (!m) continue;
      if (m.slug === slug) return m.statement;
      if (m.slugs && m.slugs.indexOf(slug) !== -1) return m.statement;
    }
    return null;
  }

  /* Only reached for slugs the page's misconception register does not
     print — §5 carries wrong-ratio / not-simplified / wrong-charge-used /
     missing-brackets in the formula bank alone. */
  var FALLBACK_STATEMENT = {
    'wrong-ratio': 'The numbers of each ion do not cancel the charges — the total positive and the total negative have to be equal.',
    'not-simplified': 'The charges balance, but the formula is not written in its lowest whole-number ratio.',
    'wrong-charge-used': 'A remembered default charge was used instead of the charge the question supplies.',
    'missing-brackets': 'The brackets round a group ion were left out, so the subscript no longer applies to the whole group.'
  };

  function statementFor(ctx, slug) {
    return lookupStatement(ctx, slug) || FALLBACK_STATEMENT[slug] || null;
  }

  window.MrbExamLadder.register('formula', {
    label: 'Build the formula',
    rung: 2,
    tariff: function () { return 1; },   /* one mark per formula */

    build: function (item, ctx) {
      ensureStyles();

      var cation = item.cation;
      var anion = item.anion;
      var cPoly = isPolyatomic(cation);
      var aPoly = isPolyatomic(anion);
      var anyPoly = cPoly || aPoly;

      /* ---- per-build state (fresh on every build(), including the
         kernel's "retry my misses" re-render) ---- */
      var nc = MIN_COUNT;
      var na = MIN_COUNT;
      var cBrackets = false;
      var aBrackets = false;
      var graded = false;

      var saved = null;
      try { saved = ctx.store && ctx.store.readItem ? ctx.store.readItem(item.id) : null; } catch (e) { saved = null; }

      var root = el('div', { className: 'mrb-fd' });

      /* ---- the task ---- */
      var cNoun = ionNoun(cation, item, true);
      var aNoun = ionNoun(anion, item, false);
      root.appendChild(el('p', { className: 'mrb-lc__stem' },
        'Build the formula of the compound made from ' + cNoun + ' ions and ' + aNoun + ' ions.'));

      var meta = 'Set how many of each ion the formula contains. The charges must cancel exactly — and the answer must be the lowest whole-number ratio.';
      if (item.abstract) {
        meta = 'X and Y are not real elements — there is nothing to recall here. Work from the charges alone: set how many of each ion the formula contains so they cancel exactly, in the lowest whole-number ratio.';
      } else if (item.chargeGiven) {
        meta = 'The charge on the ' + cNoun + ' ion is given to you below. Use the charge you are given, not one you remember. The charges must cancel exactly, in the lowest whole-number ratio.';
      } else if (anyPoly) {
        meta = 'This compound contains an ion that travels as a whole group — the group carries the charge as one unit. Balance the charges exactly, in the lowest whole-number ratio, and decide how the group should be written when you need more than one.';
      }
      root.appendChild(el('p', { className: 'mrb-lc__meta' }, meta));

      /* ---- tiles ---- */
      var cCountEl = el('span', { className: 'mrb-fd__count', attrs: { 'aria-hidden': 'true' } }, String(nc));
      var aCountEl = el('span', { className: 'mrb-fd__count', attrs: { 'aria-hidden': 'true' } }, String(na));
      var cMinus, cPlus, aMinus, aPlus, cBrBtn, aBrBtn;

      function stepBtn(sign, ion, isCation) {
        var verb = sign > 0 ? 'Add one ' : 'Remove one ';
        return el('button', {
          className: 'mrb-fd__step',
          attrs: { type: 'button', 'aria-label': verb + ionNoun(ion, item, isCation) + ' ion' },
          on: { click: function () {
            if (graded) return;
            if (isCation) nc = Math.min(MAX_COUNT, Math.max(MIN_COUNT, nc + sign));
            else na = Math.min(MAX_COUNT, Math.max(MIN_COUNT, na + sign));
            sync();
          } }
        }, sign > 0 ? '+' : MINUS);
      }

      function bracketBtn(ion, isCation) {
        return el('button', {
          className: 'mrb-fd__brackets',
          attrs: {
            type: 'button', 'aria-pressed': 'false',
            'aria-label': 'Write brackets round ' + String(ion.symbol) + ' in the formula'
          },
          on: { click: function () {
            if (graded) return;
            if (isCation) cBrackets = !cBrackets; else aBrackets = !aBrackets;
            sync();
          } }
        }, 'brackets: off');
      }

      function tile(ion, isCation) {
        var poly = isCation ? cPoly : aPoly;
        var kids = [
          el('div', { className: 'mrb-fd__role' }, isCation ? 'Positive ion' : 'Negative ion'),
          el('div', { className: 'mrb-fd__ion' }, ionGlyph(ion))
        ];
        if (!item.abstract && ION_NAMES[String(ion.symbol)]) {
          kids.push(el('div', { className: 'mrb-fd__name' }, ionNoun(ion, item, isCation) + ' ion'));
        }
        if (isCation && item.chargeGiven) {
          kids.push(el('div', { className: 'mrb-fd__given' }, 'charge given · ' + chargeText(ion.charge)));
        }
        var minus = stepBtn(-1, ion, isCation);
        var plus = stepBtn(1, ion, isCation);
        if (isCation) { cMinus = minus; cPlus = plus; } else { aMinus = minus; aPlus = plus; }
        kids.push(el('div', { className: 'mrb-fd__counter' }, [minus, isCation ? cCountEl : aCountEl, plus]));
        kids.push(el('div', { className: 'mrb-fd__counter-lbl' }, 'how many'));
        if (poly) {
          var b = bracketBtn(ion, isCation);
          if (isCation) cBrBtn = b; else aBrBtn = b;
          kids.push(b);
        }
        return el('div', {
          className: 'mrb-fd__tile',
          attrs: item.chargeGiven && isCation ? { 'data-given': '1' } : null
        }, kids);
      }

      root.appendChild(el('div', { className: 'mrb-fd__build' }, [
        tile(cation, true),
        el('div', { className: 'mrb-fd__join', attrs: { 'aria-hidden': 'true' } }, '+'),
        tile(anion, false)
      ]));

      /* ---- the charge meter: the visual centre of the widget ---- */
      var termC = el('span', { className: 'mrb-fd__term' });
      var termA = el('span', { className: 'mrb-fd__term' });
      var totalEl = el('span', { className: 'mrb-fd__total' });
      var verdictEl = el('div', { className: 'mrb-fd__verdict' });
      var meterSay = el('span', { className: 'mrb-sr' });
      var sum = el('div', { className: 'mrb-fd__sum', attrs: { 'aria-hidden': 'true' } }, [
        termC,
        el('span', { className: 'mrb-fd__op' }, '+'),
        termA,
        el('span', { className: 'mrb-fd__op' }, '='),
        totalEl
      ]);
      verdictEl.setAttribute('aria-hidden', 'true');
      var meter = el('div', {
        className: 'mrb-fd__meter',
        attrs: { 'aria-live': 'polite', 'aria-atomic': 'true' }
      }, [
        el('div', { className: 'mrb-fd__meter-lbl', attrs: { 'aria-hidden': 'true' } }, 'Charge meter'),
        sum, verdictEl, meterSay
      ]);
      root.appendChild(meter);

      /* ---- live preview of the formula they have built ---- */
      var previewSlot = el('span', { className: 'mrb-fd__preview-f' });
      root.appendChild(el('div', { className: 'mrb-fd__preview' }, [
        el('span', { className: 'mrb-fd__preview-lbl' }, 'You are writing'),
        previewSlot
      ]));

      /* ---- actions ---- */
      var checkBtn = el('button', {
        className: 'mrb-btn', attrs: { type: 'button' },
        on: { click: function () { grade(); } }
      }, '✓ Check this formula');
      var resetBtn = el('button', {
        className: 'mrb-btn mrb-btn--quiet', attrs: { type: 'button' },
        on: { click: function () {
          if (graded) return;
          nc = MIN_COUNT; na = MIN_COUNT; cBrackets = false; aBrackets = false;
          sync();
        } }
      }, '↻ Reset tiles');
      root.appendChild(el('div', { className: 'mrb-lc__actions' }, [checkBtn, resetBtn]));

      /* empty at build time, filled on check — so the marking note is
         announced to a screen reader without stealing focus */
      var resultSlot = el('div', { attrs: { 'aria-live': 'polite' } });
      root.appendChild(resultSlot);

      /* ---- live sync ---- */
      function currentFormula() {
        return part(cation, nc, cBrackets) + part(anion, na, aBrackets);
      }

      var lastMeterKey = '';
      function sync() {
        cCountEl.textContent = String(nc);
        aCountEl.textContent = String(na);

        var net = netCharge(item, nc, na);

        /* The meter is an aria-atomic live region: only touch it when the
           numbers actually change, or every unrelated re-sync re-announces. */
        var key = nc + '/' + na;
        if (key !== lastMeterKey) {
          lastMeterKey = key;
          termC.textContent = nc + ' × (' + chargeText(cation.charge) + ')';
          termA.textContent = na + ' × (' + chargeText(anion.charge) + ')';
          totalEl.textContent = totalText(net);
          totalEl.className = 'mrb-fd__total' + (net === 0 ? ' is-zero' : '');
          verdictEl.textContent = net === 0
            ? 'the charges cancel — balanced'
            : 'not balanced yet — the total has to reach 0';
          verdictEl.className = 'mrb-fd__verdict' + (net === 0 ? ' is-zero' : '');
          meter.className = 'mrb-fd__meter' + (net === 0 ? ' is-zero' : '');
          meterSay.textContent = nc + ' ' + ionPhrase(cation, item, true, nc) + ' at ' + chargeWords(cation.charge) +
            ' and ' + na + ' ' + ionPhrase(anion, item, false, na) + ' at ' + chargeWords(anion.charge) +
            '. Total charge ' + totalWords(net) + '. ' + (net === 0 ? 'Balanced.' : 'Not balanced.');
        }

        previewSlot.innerHTML = '';
        previewSlot.appendChild(formulaNode(currentFormula(), 'mrb-fd__f mrb-fd__f--big'));

        cMinus.disabled = graded || nc <= MIN_COUNT;
        cPlus.disabled = graded || nc >= MAX_COUNT;
        aMinus.disabled = graded || na <= MIN_COUNT;
        aPlus.disabled = graded || na >= MAX_COUNT;
        checkBtn.disabled = graded;
        resetBtn.disabled = graded;

        if (cBrBtn) syncBracketBtn(cBrBtn, cBrackets, nc);
        if (aBrBtn) syncBracketBtn(aBrBtn, aBrackets, na);
      }

      function syncBracketBtn(btn, on, n) {
        btn.textContent = 'brackets: ' + (on ? 'on' : 'off');
        btn.setAttribute('aria-pressed', on ? 'true' : 'false');
        btn.className = 'mrb-fd__brackets' + (on ? ' is-on' : '');
        btn.disabled = graded || n < 2;
        btn.title = n < 2 ? 'Brackets only change the formula when you use more than one of this ion.' : '';
      }

      /* ---- grading ---- */
      function ratioLine(a, b) { return a + ' : ' + b; }

      function slugLine(slug) {
        return el('p', { className: 'mrb-fd__slugline' }, [
          'misconception · ',
          el('span', { className: 'mrb-slug' }, String(slug))
        ]);
      }

      function line(text) { return el('p', { className: 'mrb-fd__line' }, text); }

      function correctionLines(slug, res) {
        var out = [];
        var net = netCharge(item, nc, na);
        var cc = chargeText(cation.charge);
        var ac = chargeText(anion.charge);

        if (slug === 'charges-swapped-to-subscripts' || slug === 'charges-as-own-subscript') {
          out.push(line('The swap only runs one way: each ion takes the OTHER ion’s charge as its subscript, and then you simplify. ' +
            'Putting each charge on its own ion looks harmless when the two charges are the same size — 1+ with 1' + MINUS + ', or 2+ with 2' + MINUS + ' — ' +
            'because the two numbers are identical, so the wrong way round and the right way round give the same thing. That is why the trick seems to work. ' +
            'The moment the charges differ in size it turns the formula upside down: ' + cation.symbol + ' at ' + cc + ' with ' + anion.symbol + ' at ' + ac +
            ' gives ' + res.formula + ', whose total charge is ' + totalText(net) + ', not 0.'));
          out.push(line('Safest habit: forget the trick. Count up until the meter reads 0, then take the lowest whole-number ratio.'));
        } else if (slug === 'one-of-each-ion') {
          out.push(line('One of each only balances when the two charges are the same size. Here ' + cc + ' against ' + ac +
            ' leaves a total of ' + totalText(net) + ', so the compound would carry a charge — and ionic compounds are neutral.'));
        } else if (slug === 'not-simplified') {
          var g = gcd(nc, na);
          out.push(line('The meter reads 0, so your charges do balance — that part is right. But a formula has to be given in its lowest whole-number ratio: ' +
            ratioLine(nc, na) + ' divides by ' + g + ' down to ' + ratioLine(nc / g, na / g) + '. Balanced is necessary; simplest is what earns the mark.'));
        } else if (slug === 'missing-brackets') {
          var polyIon = cPoly && nc > 1 ? cation : anion;
          out.push(line('Your ratio is right, but ' + polyIon.symbol + ' is a group of atoms that carries one charge as a unit. ' +
            'Written without brackets the subscript lands on the last atom only — ' + res.formula +
            ' says something different from what you built. Brackets put the number on the whole group.'));
        } else if (slug === 'wrong-charge-used') {
          out.push(line('This question gives you the charge: ' + cation.symbol + ' at ' + cc + '. ' +
            'What you have built is the formula you would get from a different charge on ' + cation.symbol + ', which is why the meter reads ' +
            totalText(net) + ' and not 0. A transition metal has no default charge to fall back on — read the Roman numeral or the stated charge, and balance against that one.'));
        } else {
          out.push(line('Your build comes to ' + totalText(net) + ', not 0. Change the counts until the positive total and the negative total cancel exactly, then check it is the lowest whole-number ratio.'));
        }
        return out;
      }

      function reveal() {
        var box = el('div', { className: 'mrb-note mrb-note--plain' });
        box.appendChild(el('b', null, 'Answer · '));
        box.appendChild(authoredFormulaNode(item.correctFormula, item.correctFormulaDisplay, 'mrb-fd__f mrb-fd__f--ans'));
        if (item.reasoning) {
          box.appendChild(el('div', { className: 'mrb-fd__reason' }, String(item.reasoning)));
        }
        return box;
      }

      function grade() {
        if (graded) return;
        var res = classify(item, nc, na, cBrackets, aBrackets);
        graded = true;
        sync();

        resultSlot.innerHTML = '';
        if (res.correct) {
          var ok = el('div', { className: 'mrb-note mrb-note--ok' });
          ok.appendChild(el('b', null, 'Correct · '));
          ok.appendChild(authoredFormulaNode(item.correctFormula, item.correctFormulaDisplay, 'mrb-fd__f'));
          ok.appendChild(document.createTextNode(' — balanced at ' + ratioLine(nc, na) + ', and that is the lowest whole-number ratio.'));
          if (item.reasoning) ok.appendChild(el('div', { className: 'mrb-fd__reason' }, String(item.reasoning)));
          resultSlot.appendChild(ok);
          ctx.report(item.id, 1, 1);
          return;
        }

        var err = el('div', { className: 'mrb-note mrb-note--err' });
        err.appendChild(el('b', null, 'Not this one · '));
        err.appendChild(formulaNode(res.formula));
        var stmt = res.slug ? statementFor(ctx, res.slug) : null;
        if (stmt) err.appendChild(el('div', { className: 'mrb-fd__stmt' }, String(stmt)));
        correctionLines(res.slug, res).forEach(function (n) { err.appendChild(n); });
        if (res.distractor && res.distractor.note) {
          err.appendChild(el('p', { className: 'mrb-fd__line mrb-fd__line--note' }, String(res.distractor.note)));
        }
        if (res.slug) err.appendChild(slugLine(res.slug));
        resultSlot.appendChild(err);
        resultSlot.appendChild(reveal());
        resultSlot.appendChild(el('p', { className: 'mrb-fd__retry' },
          'Use ↻ Retry my misses at the foot of the ladder when you want this one back.'));
        ctx.report(item.id, 0, 1);
      }

      /* ---- already answered in a previous session: show the settled
         state rather than a blank widget under a filled-in score chip.
         The kernel's "retry my misses" / "start over" clear it. ---- */
      if (saved) {
        graded = true;
        nc = (item.ratio && item.ratio[0]) || 1;
        na = (item.ratio && item.ratio[1]) || 1;
        cBrackets = cPoly && nc > 1;
        aBrackets = aPoly && na > 1;
        sync();
        var back = el('div', { className: 'mrb-note ' + (saved.a >= saved.o ? 'mrb-note--ok' : 'mrb-note--err') });
        back.appendChild(el('b', null, saved.a >= saved.o ? 'Answered · ' : 'Recorded as a miss · '));
        back.appendChild(document.createTextNode(saved.a + ' / ' + saved.o +
          (saved.a >= saved.o ? ' — the tiles show the correct build.'
                              : ' — the tiles show the correct build. Retry my misses, at the foot of the ladder, gives you this one back.')));
        resultSlot.appendChild(back);
        resultSlot.appendChild(reveal());
      } else {
        sync();
      }

      return root;
    }
  });

  /* ---------- styles ---------- */
  var STYLE_ID = 'mrb-formula-styles';
  function ensureStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '.mrb-fd,.mrb-fd *{box-sizing:border-box}',
      '.mrb-fd{font-family:var(--font-body,system-ui,sans-serif);color:var(--ink-body,#2A241E)}',

      /* tiles */
      '.mrb-fd__build{display:grid;grid-template-columns:1fr auto 1fr;gap:12px;align-items:stretch;margin:4px 0 0}',
      '@media (max-width:560px){.mrb-fd__build{grid-template-columns:1fr}.mrb-fd__join{display:none}}',
      '.mrb-fd__join{align-self:center;font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(20px * var(--rd-fs-scale,1));color:var(--ink-faint,#8A8074)}',
      '.mrb-fd__tile{border:1px solid var(--border,#E4DCCB);border-radius:var(--r-callout,18px);background:var(--surface-inset,#F7F2E8);padding:14px 16px 16px;text-align:center}',
      '.mrb-fd__tile[data-given="1"]{border-color:var(--accent-tint-border,#F0BBA9);background:var(--accent-wash,#FBEEE9)}',
      '.mrb-fd__role{font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-muted,#6B635A);margin-bottom:8px}',
      '.mrb-fd__ion{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(28px * var(--rd-fs-scale,1));line-height:1.1;color:var(--ink,#1A1714)}',
      '.mrb-fd__ion sup{font-size:.6em;vertical-align:super;line-height:0}',
      '.mrb-fd__name{font-size:calc(12.5px * var(--rd-fs-scale,1));color:var(--ink-muted,#6B635A);margin-top:3px}',
      '.mrb-fd__given{display:inline-block;margin-top:9px;font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent-deep,#B5341A);border:1px solid var(--accent-tint-border,#F0BBA9);background:var(--surface-panel,#FFFDF8);border-radius:999px;padding:4px 11px}',
      '.mrb-fd__counter{display:flex;align-items:center;justify-content:center;gap:12px;margin-top:12px}',
      '.mrb-fd__counter-lbl{font-family:var(--font-mono,monospace);font-size:calc(10px * var(--rd-fs-scale,1));letter-spacing:.09em;text-transform:uppercase;color:var(--ink-faint,#8A8074);margin-top:4px}',
      '.mrb-fd__step{width:40px;height:40px;border-radius:12px;border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);color:var(--accent-deep,#B5341A);font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(20px * var(--rd-fs-scale,1));line-height:1;cursor:pointer}',
      '.mrb-fd__step:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-fd__step[disabled]{opacity:.35;cursor:default}',
      '.mrb-fd__count{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(30px * var(--rd-fs-scale,1));line-height:1;min-width:1.3em;color:var(--ink,#1A1714)}',
      '.mrb-fd__brackets{margin-top:11px;font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));font-weight:600;letter-spacing:.05em;color:var(--ink-muted,#6B635A);border:1px solid var(--border,#E4DCCB);background:var(--surface-panel,#FFFDF8);border-radius:999px;padding:6px 13px;cursor:pointer}',
      '.mrb-fd__brackets.is-on{color:var(--accent-deep,#B5341A);border-color:var(--accent-tint-border,#F0BBA9);background:var(--accent-wash,#FBEEE9)}',
      '.mrb-fd__brackets:focus-visible{outline:2px solid var(--accent-strong,#C0392B);outline-offset:2px}',
      '.mrb-fd__brackets[disabled]{opacity:.45;cursor:default}',

      /* the meter — visual centre */
      '.mrb-fd__meter{margin-top:16px;border:2px solid var(--border,#E4DCCB);border-radius:var(--r-panel,22px);background:var(--surface-card,#F5F1E8);padding:16px 20px 14px;text-align:center}',
      '.mrb-fd__meter.is-zero{border-color:var(--ok-border,#7FB98A);background:var(--ok-bg,#E7F3EA)}',
      '.mrb-fd__meter-lbl{font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-muted,#6B635A);margin-bottom:8px}',
      '.mrb-fd__sum{display:flex;align-items:baseline;justify-content:center;gap:9px;flex-wrap:wrap;font-family:var(--font-mono,monospace);font-size:calc(19px * var(--rd-fs-scale,1));color:var(--ink,#1A1714)}',
      '.mrb-fd__op{color:var(--ink-muted,#6B635A)}',
      '.mrb-fd__total{font-family:var(--font-display,sans-serif);font-weight:700;font-size:calc(30px * var(--rd-fs-scale,1));color:var(--ink,#1A1714);padding:0 4px}',
      '.mrb-fd__total.is-zero{color:var(--ok,#2E6B3A)}',
      '.mrb-fd__verdict{margin-top:7px;font-size:calc(12.5px * var(--rd-fs-scale,1));color:var(--ink-muted,#6B635A)}',
      '.mrb-fd__verdict.is-zero{color:var(--ok,#2E6B3A);font-weight:600}',

      /* preview */
      '.mrb-fd__preview{display:flex;align-items:baseline;justify-content:center;gap:10px;margin-top:14px;flex-wrap:wrap}',
      '.mrb-fd__preview-lbl{font-family:var(--font-mono,monospace);font-size:calc(10.5px * var(--rd-fs-scale,1));font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-muted,#6B635A)}',
      '.mrb-fd__f{font-family:var(--font-display,sans-serif);font-weight:700;color:var(--ink,#1A1714)}',
      '.mrb-fd__f sub{font-size:.66em;vertical-align:baseline;position:relative;bottom:-.22em}',
      '.mrb-fd__f--big{font-size:calc(24px * var(--rd-fs-scale,1))}',
      '.mrb-fd__f--ans{font-size:calc(19px * var(--rd-fs-scale,1))}',

      /* result copy */
      '.mrb-fd__stmt{margin-top:8px;font-style:italic}',
      '.mrb-fd__line{margin:9px 0 0}',
      '.mrb-fd__line--note{color:var(--ink-muted,#6B635A)}',
      '.mrb-fd__reason{margin-top:8px;font-family:var(--font-mono,monospace);font-size:calc(12.5px * var(--rd-fs-scale,1));line-height:1.5}',
      '.mrb-fd__slugline{margin:11px 0 0;font-family:var(--font-mono,monospace);font-size:calc(11px * var(--rd-fs-scale,1));color:var(--ink-faint,#8A8074)}',
      '.mrb-fd__retry{margin:11px 0 0;font-size:calc(12.5px * var(--rd-fs-scale,1));color:var(--ink-muted,#6B635A)}'
    ].join('');
    document.head.appendChild(s);
  }

  /* The pure core, exposed for the node harness and console debugging.
     The engine itself is reached through MrbExamLadder. */
  window.MrbFormulaDeducer = {
    compose: compose,
    part: part,
    classify: classify,
    findDistractor: findDistractor,
    isPolyatomic: isPolyatomic,
    gcd: gcd,
    netCharge: netCharge
  };
})();
