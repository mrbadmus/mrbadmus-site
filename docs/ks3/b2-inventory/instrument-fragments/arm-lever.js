/* WIRE: each(root.querySelectorAll("[data-leverblock]"), wireArmLever);
   — add to wireInstruments(), in the B2 group beside wireMusclePair. Uses
   each / toArray / setHidden / setCount / markStage / wireBenchGate, all
   already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── arm-lever (b2-04 #s-bench) — the forearm rig ──

     ⚖️ THE INSTRUMENT WITHHOLDS ONE NUMBER AND THAT IS THE LESSON. Three
     readouts are handed over; the fourth says "not measured — you work it
     out" until the meter is fitted, and the muscle arrow on the canvas is
     labelled with a word and no magnitude. Both routes to the answer are
     closed by the same flag, so there is one thing to get wrong rather
     than two. If a future change makes the force readable before the
     meter, the lesson is gone and every gate on this page still passes.

     ⚖️ THE RAIL STOP IS A SET, NOT A COUNT. `touched` keys on the control
     NAME, so dragging the mass slider twenty times is one control moved.
     Design's own predicate is already a set and this keeps it one —
     `Math.max(touched, n)` is the shape that let c1-04 read "all controls
     tried" after a single button.

     ⚖️ NOTHING ANIMATES. The rig is a static drawing repainted when a
     control moves, so `prefers-reduced-motion` has nothing to degrade
     here (the same note `wireHalvingBench` and `wireClaimSwitch` carry)
     and the reduced-motion experience is the COMPLETE one rather than a
     lesser one. There is no tick to scale, and adding one would animate
     an arm that is deliberately held still — the whole page is about the
     case where nothing is moving.

     The number formatter and the aria-label composition are duplicated in
     `build_ks3.py` (`_lever_num`, `_lever_alt`) on purpose: the resting
     page has to render "20 N" and its label before any JS runs. Two
     implementations, one composition, checked at both ends of both
     sliders.
     ═══════════════════════════════════════════════════════════════ */
  function wireArmLever(sec) {
    var wrap = sec.querySelector("[data-lever]");
    if (!wrap) { return; }

    var G = parseFloat(wrap.getAttribute("data-g")) || 10;
    var DONE_AT = parseInt(wrap.getAttribute("data-done-at"), 10) || 2;
    var UNMEASURED = wrap.getAttribute("data-unmeasured") || "";
    var ALT = wrap.getAttribute("data-alt") || "";
    var ALT_MEASURED = wrap.getAttribute("data-alt-measured") || "";
    var C_TITLE = wrap.getAttribute("data-canvas-title") || "";
    var C_JOINT = wrap.getAttribute("data-canvas-joint") || "";
    var C_MUSCLE = wrap.getAttribute("data-canvas-muscle") || "";
    var C_LOAD = wrap.getAttribute("data-canvas-load") || "{n} N";
    var M_LABEL = wrap.getAttribute("data-meter-label") || "";
    var M_DONE = wrap.getAttribute("data-meter-done") || "";
    var M_NOTE = wrap.getAttribute("data-meter-note") || "";
    var M_NOTE_DONE = wrap.getAttribute("data-meter-note-done") || "";

    var canvas = wrap.querySelector("[data-lever-canvas]");
    var values = toArray(wrap.querySelectorAll("[data-lever-value]"));
    var outs = toArray(wrap.querySelectorAll("[data-lever-out]"));
    var inputs = toArray(wrap.querySelectorAll("[data-lever-input]"));
    var tabs = toArray(wrap.querySelectorAll("[data-lever-tab]"));
    var meterBtn = wrap.querySelector("[data-lever-meter]");
    var note = wrap.querySelector("[data-lever-note]");

    var dp = {
      load: parseInt(wrap.getAttribute("data-dp-load"), 10) || 0,
      ins: parseInt(wrap.getAttribute("data-dp-ins"), 10) || 0,
      hand: parseInt(wrap.getAttribute("data-dp-hand"), 10) || 0
    };
    var state = {
      load: parseFloat(wrap.getAttribute("data-load")),
      ins: parseFloat(wrap.getAttribute("data-ins")),
      hand: parseFloat(wrap.getAttribute("data-hand"))
    };
    var touched = {};
    var meterShown = false;

    /* Weight is mass × g; the turning effect of the load is weight × its
       distance from the joint; and the muscle, attached far closer in, must
       produce the same turning effect over a much smaller distance. Both
       distances go into metres, which cancels — the ratio is what matters —
       but they are converted anyway so the arithmetic here is the same
       arithmetic the student is asked to write down. */
    function weight() { return state.load * G; }
    function muscleForce() {
      return (weight() * (state.hand / 100)) / (state.ins / 100);
    }

    function num(v, places, fmt) {
      return (fmt || "{n}").replace("{n}", Number(v).toFixed(places));
    }

    /* ⚠️ "after 1 halvings" is why this exists. No control on this rig can
       currently reach a bare 1 — the two sliders render to one decimal and
       the tabs offer 32 and 16 — but the guard is cheap and a plural that
       breaks for one authored value is exactly the defect that ships. */
    function altText() {
      var out = ALT.replace("{load}", num(state.load, dp.load))
        .replace("{ins}", num(state.ins, dp.ins))
        .replace("{hand}", num(state.hand, dp.hand));
      if (meterShown && ALT_MEASURED) {
        out += ALT_MEASURED.replace("{force}", num(muscleForce(), 0));
      }
      return out.split(" 1 kilograms").join(" 1 kilogram")
        .split(" 1 centimetres").join(" 1 centimetre")
        .split(" 1 newtons").join(" 1 newton");
    }

    function arrow(ctx, x, y, dy, colour, label) {
      ctx.strokeStyle = colour;
      ctx.fillStyle = colour;
      ctx.lineWidth = 5;
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x, y + dy);
      ctx.stroke();
      var s = dy > 0 ? 1 : -1;
      ctx.beginPath();
      ctx.moveTo(x, y + dy + s * 14);
      ctx.lineTo(x - 11, y + dy);
      ctx.lineTo(x + 11, y + dy);
      ctx.closePath();
      ctx.fill();
      ctx.font = '500 16px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "center";
      ctx.fillText(label, x, y + dy + s * 34);
    }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 350;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);

      var scale = 17;                       // px per cm
      var elx = 150, ely = 190;
      var handX = elx + state.hand * scale;
      var insX = elx + state.ins * scale;

      // Upper arm: an ink outline under a bone-coloured core, which is what
      // gives every limb on this canvas a drawn edge against the ink ground.
      ctx.lineCap = "round";
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 30;
      ctx.beginPath();
      ctx.moveTo(elx, ely);
      ctx.lineTo(elx, ely - 128);
      ctx.stroke();
      ctx.strokeStyle = "#F4E9D8";
      ctx.lineWidth = 24;
      ctx.beginPath();
      ctx.moveTo(elx, ely);
      ctx.lineTo(elx, ely - 128);
      ctx.stroke();

      // The muscle, curving from high on the upper arm down to its
      // attachment. The attachment point MOVES with the slider — that is the
      // whole variable, and a muscle drawn at a fixed angle would hide it.
      ctx.strokeStyle = "#FFC53D";
      ctx.lineWidth = 15;
      ctx.beginPath();
      ctx.moveTo(elx + 16, ely - 118);
      ctx.quadraticCurveTo(elx + 34, ely - 60, insX, ely - 12);
      ctx.stroke();

      // Forearm, held level.
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 28;
      ctx.beginPath();
      ctx.moveTo(elx, ely);
      ctx.lineTo(handX, ely);
      ctx.stroke();
      ctx.strokeStyle = "#F4E9D8";
      ctx.lineWidth = 22;
      ctx.beginPath();
      ctx.moveTo(elx, ely);
      ctx.lineTo(handX, ely);
      ctx.stroke();

      // The joint, named on the drawing: every distance on this page is
      // measured from it and an unlabelled pivot leaves "from the elbow"
      // pointing at nothing.
      ctx.beginPath();
      ctx.arc(elx, ely, 16, 0, Math.PI * 2);
      ctx.fillStyle = "#C6B9A7";
      ctx.fill();
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "center";
      ctx.fillText(C_JOINT, elx, ely + 44);

      // The hand, and the load hanging from it. The block grows with the
      // mass so the slider has something to say on the drawing as well as in
      // the readout.
      ctx.fillStyle = "#F4E9D8";
      ctx.beginPath();
      ctx.arc(handX, ely, 15, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 3;
      ctx.stroke();
      var bw = 34 + state.load * 7;
      ctx.fillStyle = "#8FB7FF";
      ctx.fillRect(handX - bw / 2, ely + 24, bw, 26 + state.load * 3);
      ctx.strokeRect(handX - bw / 2, ely + 24, bw, 26 + state.load * 3);

      // ⚖️ THE TWO ARROWS ARE NOT SYMMETRICAL, AND THAT IS THE GATE. The load
      // arrow carries its magnitude, because the rig measured it. The muscle
      // arrow carries a WORD and never a number, in every state including
      // after the meter is fitted — the meter reading lands in the tile,
      // where the student can hold it against their own working, and putting
      // it on the arrow would let them read the answer off the picture.
      arrow(ctx, insX, ely - 26, -58, "#FFC53D", C_MUSCLE);
      arrow(ctx, handX + 46, ely + 30, 62, "#8FB7FF",
            num(weight(), 0, C_LOAD));

      // The two distances, drawn as dimension lines in each one's own colour
      // so the muscle's short reach and the load's long one are one glance
      // apart. These exist only on the canvas, which is why the aria-label
      // has to carry both numbers.
      function dim(x1, x2, y, colour, label) {
        ctx.strokeStyle = colour;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(x1, y - 8); ctx.lineTo(x1, y + 8);
        ctx.moveTo(x2, y - 8); ctx.lineTo(x2, y + 8);
        ctx.moveTo(x1, y); ctx.lineTo(x2, y);
        ctx.stroke();
        ctx.fillStyle = colour;
        ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "center";
        ctx.fillText(label, (x1 + x2) / 2, y - 14);
      }
      dim(elx, insX, ely + 92, "#FFC53D",
          num(state.ins, dp.ins) + " cm");
      dim(elx, handX, ely + 132, "#8FB7FF",
          num(state.hand, dp.hand) + " cm");

      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillText(C_TITLE, 30, 34);

      if (canvas.setAttribute) { canvas.setAttribute("aria-label", altText()); }
    }

    function repaint() {
      each(values, function (p) {
        var key = p.getAttribute("data-lever-value");
        p.textContent = num(state[key], dp[key],
                            p.getAttribute("data-format"));
      });
      each(outs, function (p) {
        var key = p.getAttribute("data-lever-out");
        var fmt = p.getAttribute("data-format");
        if (key === "force") {
          p.textContent = meterShown ? num(muscleForce(), 0, fmt) : UNMEASURED;
        } else if (key === "weight") {
          p.textContent = num(weight(), 0, fmt);
        } else {
          p.textContent = num(state[key], dp[key], fmt);
        }
      });
      each(tabs, function (b) {
        var key = b.getAttribute("data-lever-tab");
        b.setAttribute("aria-pressed",
          parseFloat(b.getAttribute("data-value")) === state[key]
            ? "true" : "false");
      });
      if (meterBtn) {
        meterBtn.textContent = meterShown ? M_DONE : M_LABEL;
        if (meterShown) { meterBtn.setAttribute("disabled", ""); }
      }
      if (note) { note.textContent = meterShown ? M_NOTE_DONE : M_NOTE; }
      setCount(sec, meterShown ? 1 : 0);
      draw();
      // ⚖️ A SET AND A FLAG, both required. Two DIFFERENT controls moved says
      // the student explored the trade; the meter says they committed to an
      // answer first and then checked it. Either alone is half the block.
      markStage(sec,
        Object.keys(touched).length >= DONE_AT && meterShown);
      // The steps block downstream is built out of this rig's live state, so
      // it is told rather than left to poll. `bubbles` so a listener on the
      // document catches it wherever the two blocks sit.
      if (wrap.dispatchEvent && window.CustomEvent) {
        wrap.dispatchEvent(new window.CustomEvent("ks3:lever", {
          bubbles: true,
          detail: {
            rig: wrap.getAttribute("data-rig"),
            load: state.load, ins: state.ins, hand: state.hand,
            g: G, dp: dp, weight: weight(), force: muscleForce()
          }
        }));
      }
    }

    each(inputs, function (input) {
      input.addEventListener("input", function () {
        var key = input.getAttribute("data-lever-input");
        state[key] = parseFloat(input.value);
        touched[key] = true;
        repaint();
      });
    });
    each(tabs, function (b) {
      b.addEventListener("click", function () {
        var key = b.getAttribute("data-lever-tab");
        state[key] = parseFloat(b.getAttribute("data-value"));
        touched[key] = true;
        repaint();
      });
    });
    if (meterBtn) {
      // One-way. What a student found out by fitting the meter cannot be
      // un-found by pressing it again, and re-hiding the reading would offer
      // a way to pretend the check never happened.
      meterBtn.addEventListener("click", function () {
        if (meterShown) { return; }
        meterShown = true;
        repaint();
      });
    }

    repaint();
    wireBenchGate(sec);
  }
