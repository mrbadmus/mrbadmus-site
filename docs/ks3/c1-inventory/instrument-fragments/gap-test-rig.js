/* WIRE: each(root.querySelectorAll("[data-gapblock]"), wireGapTestRig); */

  /* ── gap-test-rig (c1-01 #s-gap) ──

     ⚖️ THE RIG NEVER MARKS THE CHOICE. It packs the gap with whatever the
     student said is in it and then runs a test they already know the
     answer to from the top of the page. Three tests, and every wrong
     answer fails all three — which is an argument, not a verdict, and it
     stays an argument only as long as nothing here goes green or red.

     ⚠️ The discriminator is POSITIONAL and comes from the markup
     (`data-empty-choice`), never from the option's text. Design compares
     against a literal 3 written three lines from the list it indexes.

     Nothing animates: the two boxes are a before-and-after, not a
     process, so reduced motion loses nothing at all here. */
  function wireGapTestRig(sec) {
    var wrap = sec.querySelector("[data-gap]");
    if (!wrap) { return; }

    var EMPTY = parseInt(wrap.getAttribute("data-empty-choice"), 10);
    var ALT = wrap.getAttribute("data-alt") || "";
    var ALT_FILLED = wrap.getAttribute("data-alt-filled") || "";
    var ALT_EMPTY = wrap.getAttribute("data-alt-empty") || "";
    var L_EMPTY = wrap.getAttribute("data-label-empty") || "";
    var L_FILLED = wrap.getAttribute("data-label-filled") || "";
    var F_EMPTY = wrap.getAttribute("data-foot-empty") || "";
    var F_FILLED = wrap.getAttribute("data-foot-filled") || "";

    var rig = wrap.querySelector("[data-gap-rig]");
    var canvas = wrap.querySelector("[data-gap-canvas]");
    var opts = toArray(wrap.querySelectorAll(".ks3-option"));
    var testBtns = toArray(wrap.querySelectorAll(".ks3-gap-test"));
    var notes = toArray(wrap.querySelectorAll("[data-note]"));

    var choice = null;
    var test = null;

    // "Something is in the gap" — the state every test is about to
    // contradict. A choice not yet made is not a filled gap.
    function filled() { return choice !== null && choice !== EMPTY; }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 260;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);

      var half = W / 2;
      var packed = filled();

      function drawBox(x0, label, solid) {
        ctx.save();
        ctx.beginPath();
        ctx.rect(x0 + 34, 52, half - 68, H - 108);
        ctx.clip();
        // The fill IS the answer: the space between the particles stops
        // being space. Clipped to the box so it cannot read as a
        // background, and the particles are drawn identically in both
        // boxes so the only difference on screen is the gap.
        if (solid) {
          ctx.fillStyle = "#4A4038";
          ctx.fillRect(x0 + 34, 52, half - 68, H - 108);
        }
        for (var row = 0; row < 4; row++) {
          for (var col = 0; col < 7; col++) {
            var x = x0 + 62 + col * 54 + (row % 2 ? 16 : 0);
            var y = 78 + row * 44;
            ctx.beginPath();
            ctx.arc(x, y, 17, 0, Math.PI * 2);
            ctx.fillStyle = "#D98A4A";
            ctx.fill();
            ctx.strokeStyle = "#5A3212";
            ctx.lineWidth = 2;
            ctx.stroke();
          }
        }
        ctx.restore();
        ctx.strokeStyle = "#5C5249";
        ctx.lineWidth = 2;
        ctx.strokeRect(x0 + 34, 52, half - 68, H - 108);
        ctx.fillStyle = solid ? "#FF8A5B" : "#FFC53D";
        ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "center";
        ctx.fillText(label, x0 + half / 2, 40);
      }

      drawBox(0, L_EMPTY, false);
      drawBox(half, packed ? L_FILLED : L_EMPTY, packed);

      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 13px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "center";
      ctx.fillText(packed ? F_FILLED : F_EMPTY, W / 2, H - 20);

      if (canvas.setAttribute) {
        canvas.setAttribute("aria-label",
          ALT.replace("{right}", packed ? ALT_FILLED : ALT_EMPTY));
      }
    }

    function repaint() {
      // Which of the eight authored paragraphs is on screen. With a test
      // running it is that test's outcome — `on` when the gap is genuinely
      // empty, `off` when the student filled it — and before any test it
      // is one of the two opening lines.
      var want = test === null ? (filled() ? "filled" : "empty")
        : test + (filled() ? "-off" : "-on");
      each(notes, function (p) {
        setHidden(p, p.getAttribute("data-note") !== want);
      });
      draw();
      // One test run is the stage: the student has taken the model
      // somewhere it can be checked. Changing the answer afterwards
      // re-runs the same test against the new gap, which is the point.
      if (test !== null) { markStage(sec, true); }
    }

    each(opts, function (btn, i) {
      btn.addEventListener("click", function () {
        choice = i;
        each(opts, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        // Gating by absence, as everywhere else in the key stage: the rig
        // is not there to be looked at until a claim has been made about
        // what it is going to show.
        if (rig) { setHidden(rig, false); }
        repaint();
      });
    });

    each(testBtns, function (btn) {
      btn.addEventListener("click", function () {
        test = btn.getAttribute("data-test");
        each(testBtns, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        repaint();
      });
    });

    draw();
  }
