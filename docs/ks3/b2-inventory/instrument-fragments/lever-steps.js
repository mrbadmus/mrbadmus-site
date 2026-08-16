/* WIRE: each(root.querySelectorAll("[data-lstepblock]"), wireLeverSteps);
   — add to wireInstruments(), in the B2 group AFTER wireArmLever, so the rig
   has painted once and dispatched its first `ks3:lever` before this block
   subscribes. Uses each / toArray / setHidden / markStage, all already in
   scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── lever-steps (b2-04 #s-build) — MRB-204 step 4 ──

     Three commitments — the rule, the insertion, and a number with a unit
     — then the worked version of the STUDENT'S OWN rig beside what they
     wrote.

     ⚖️ IT IS THE SAME PROBLEM AS THE BENCH, AND IT SAYS SO IN NUMBERS.
     The heading, the second ladder's three options, all four reveal steps
     and the closing line are templates over the rig's live state, refilled
     whenever a control up there moves. That is the whole difference from
     c2-06's `fifa-pick`, whose eight strings are static, and it is why the
     rig broadcasts `ks3:lever` rather than this block polling for it.

     ⚠️ THE TEMPLATES ARE READ OFF `data-template`, NEVER REBUILT. Each
     option button and each step line carries the authored string it came
     from, so there is exactly one copy of every sentence on this page and
     it is the one the build rendered. Nothing here composes prose.

     ⊕ CORRECTION — THE RAIL STOP DEMANDS SOMETHING. Design ticks this
     stage on `buildOpen`, i.e. on pressing "Show the four steps", so a
     student who committed to nothing could tick it with one tap. MRB-208
     has a rail stop requiring the student to do something, so it ticks on
     the three commitments instead: formula picked, insertion picked, and a
     non-empty answer WITH a unit. Strictly earlier than the button, which
     needs the same three — nothing gets harder, the stop just stops being
     reachable by pressing one thing.

     ⚖️ THE UNIT IS ITS OWN COMMITMENT. "160" is not an answer to a
     question about force. The placeholder option carries an empty value,
     so `unit.value` is falsy until a real unit is chosen.

     ⚖️ NOTHING ANIMATES and nothing counts, so `prefers-reduced-motion`
     has nothing to degrade here and the reduced-motion experience is the
     complete one.
     ═══════════════════════════════════════════════════════════════ */
  function wireLeverSteps(sec) {
    var wrap = sec.querySelector("[data-lstep]");
    if (!wrap) { return; }

    var RIG = wrap.getAttribute("data-rig") || "";
    var HEAD = wrap.getAttribute("data-head") || "";
    var TPL = wrap.getAttribute("data-close") || "";
    var BLANK = wrap.getAttribute("data-blank") || "—";
    var FMT = wrap.getAttribute("data-progress") || "";
    var DONE = wrap.getAttribute("data-done-label") || "";
    var TOTAL = parseInt(wrap.getAttribute("data-total"), 10) || 3;

    var opts = toArray(wrap.querySelectorAll(".ks3-lstep-opt"));
    var lines = toArray(wrap.querySelectorAll("[data-template]"));
    var ans = wrap.querySelector("[data-lstep-ans]");
    var unit = wrap.querySelector("[data-lstep-unit]");
    var btn = wrap.querySelector("[data-lstep-open]");
    var progress = wrap.querySelector("[data-lstep-progress]");
    var reveal = wrap.querySelector("[data-reveal]");
    var closeEl = wrap.querySelector("[data-lstep-close]");
    /* The shell emits the block's <h2> before any instrument renderer runs,
       so the build fills it through `_lever_steps_heading` and this repaints
       the same element. It is the ONLY <h2> inside this section — the reveal
       head, the panel labels and the questions are all paragraphs — which is
       what makes the plain selector safe. */
    var head = sec.querySelector("h2");

    var picked = {};
    var open = false;
    var subs = {};

    function fill(s) {
      var out = s || "";
      for (var k in subs) {
        if (Object.prototype.hasOwnProperty.call(subs, k)) {
          out = out.split(k).join(subs[k]);
        }
      }
      return out;
    }

    function pad(v, places) { return Number(v).toFixed(places); }

    /* The rig's state, turned into the nine substitutions every template on
       this block is written against. Identical composition to
       `_lever_steps_rig` in build_ks3.py, which renders the resting page.

       ⚠️ Two decimal places on the distances and the turning effect, none on
       the weight or the force. `0.04` and `0.32` are the metre conversions a
       student writes down; a weight and a force are whole newtons here. */
    function adopt(d) {
      var dM = d.ins / 100, dL = d.hand / 100;
      subs = {
        "{load}": pad(d.load, d.dp.load),
        "{ins}": pad(d.ins, d.dp.ins),
        "{hand}": pad(d.hand, d.dp.hand),
        "{W}": pad(d.weight, 0),
        "{dM}": pad(dM, 2),
        "{dL}": pad(dL, 2),
        "{TE}": pad(d.weight * dL, 2),
        "{F}": pad(d.force, 0),
        "{ratio}": pad(d.hand / d.ins, 1)
      };
    }

    function committed() {
      var n = 0;
      if (picked["0"] !== undefined) { n += 1; }
      if (picked["1"] !== undefined) { n += 1; }
      if (ans && ans.value.trim() && unit && unit.value) { n += 1; }
      return n;
    }

    function repaintText() {
      if (head && HEAD) { head.textContent = fill(HEAD); }
      each(lines, function (el) {
        el.textContent = fill(el.getAttribute("data-template"));
      });
      if (open && closeEl && TPL) {
        closeEl.textContent = fill(TPL)
          .split("{answer}").join(ans && ans.value.trim() ? ans.value.trim() : BLANK)
          .split("{unit}").join(unit && unit.value ? unit.value : "");
      }
    }

    function refresh() {
      var n = committed();
      if (progress) {
        progress.textContent = open ? DONE : FMT.split("{n}").join(String(n));
      }
      if (btn) {
        if (open || n < TOTAL) { btn.setAttribute("disabled", ""); }
        else { btn.removeAttribute("disabled"); }
      }
      // ⊕ The corrected predicate. Three commitments, not `buildOpen`.
      markStage(sec, n >= TOTAL);
    }

    each(opts, function (b) {
      b.addEventListener("click", function () {
        if (open) { return; }
        var group = b.getAttribute("data-group");
        picked[group] = b.getAttribute("data-i");
        each(opts, function (x) {
          if (x.getAttribute("data-group") !== group) { return; }
          x.setAttribute("aria-pressed",
            x.getAttribute("data-i") === picked[group] ? "true" : "false");
        });
        refresh();
      });
    });
    each([ans, unit], function (el) {
      if (!el) { return; }
      each(["input", "change"], function (evt) {
        el.addEventListener(evt, refresh);
      });
    });
    if (btn) {
      btn.addEventListener("click", function () {
        if (open || committed() < TOTAL) { return; }
        open = true;
        // Everything locks. The model is on screen, so a changed pick would
        // be choosing after reading the answer.
        each(opts, function (x) { x.setAttribute("disabled", ""); });
        if (ans) { ans.setAttribute("disabled", ""); }
        if (unit) { unit.setAttribute("disabled", ""); }
        setHidden(reveal, false);
        repaintText();
        refresh();
      });
    }

    /* ⚠️ SEEDED FROM THE RIG'S OWN ATTRIBUTES, NOT FROM ITS FIRST BROADCAST.
       `wireArmLever` paints once at construction and dispatches `ks3:lever`
       there, and it is wired BEFORE this block — so the first event has
       already gone by the time this function runs. Subscribing alone left
       `subs` empty until a student happened to move a control, and the
       closing line then rendered a literal `{F}`.

       Found by `lsteps-opened`'s own `/[{}]/` check in a real browser, which
       is exactly what that assertion is for: nothing about this is visible
       from reading either file, because both are individually correct.

       Reading the rig's build-time attributes rather than re-ordering the two
       wire calls is the fix that survives: a future instrument wired between
       them, or a rig that moves further down the page, would break the
       ordering fix and not this one. */
    function seed() {
      var rig = document.querySelector(
        RIG ? '[data-lever][data-rig="' + RIG + '"]' : "[data-lever]");
      if (!rig) { return; }
      var load = parseFloat(rig.getAttribute("data-load"));
      var ins = parseFloat(rig.getAttribute("data-ins"));
      var hand = parseFloat(rig.getAttribute("data-hand"));
      var g = parseFloat(rig.getAttribute("data-g"));
      if (isNaN(load) || isNaN(ins) || isNaN(hand) || isNaN(g) || !ins) {
        return;
      }
      adopt({
        load: load, ins: ins, hand: hand, g: g,
        dp: {
          load: parseInt(rig.getAttribute("data-dp-load"), 10) || 0,
          ins: parseInt(rig.getAttribute("data-dp-ins"), 10) || 0,
          hand: parseInt(rig.getAttribute("data-dp-hand"), 10) || 0
        },
        weight: load * g,
        force: (load * g * (hand / 100)) / (ins / 100)
      });
    }

    /* The rig broadcasts; this listens. `document` rather than the rig
       element, because the two blocks are siblings far apart in the document
       and the event bubbles — and because a page where the rig is missing
       must still render this block's resting state rather than throwing. */
    document.addEventListener("ks3:lever", function (ev) {
      if (!ev.detail || (RIG && ev.detail.rig !== RIG)) { return; }
      adopt(ev.detail);
      repaintText();
    });

    seed();
    refresh();
  }
