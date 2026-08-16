// WIRE: each(root.querySelectorAll("[data-smatrixblock]"), wireStateMatrix);
//
// ⚠️ Wire this AFTER `wireStateBench` in `wireInstruments()`, beside it. The
// order is tidiness rather than correctness: the matrix does a standing read of
// its own at wire time and the bench's resting attributes are in the markup
// from the build, so a matrix wired first still opens on the right row.

  /* ── state-matrix (c1-02 #s-matrix) ──
     Six properties against three states, with ONE ROW LIT by the bench
     above it.

     ⚖️ CROSS-BLOCK STATE, AND NO SECOND COPY OF IT. This is the first
     component in the key stage that reads another block's state, and the
     obvious build — keep `squash` and `trails` here too and update both
     from one handler — is the wrong one: two copies of a fact are two
     places for it to drift, and the bug that produces (a table lighting
     the row the bench stopped showing) is silent. So the bench PUBLISHES
     on `[data-sbench]` and the matrix READS. The broadcast it listens for
     carries no payload at all; it means "look again", nothing more.

     ⚖️ NOT A RAIL STOP. `markStage` is never called from here and the
     renderer emits no `data-stage-done`: this section asks the student for
     nothing, and MRB-208 rules the rail carries only sections that do.
     Design's own stage 3 ticks on the bench's predicate — see the
     renderer's docstring and the lesson module. */

  function wireStateMatrix(sec) {
    var wrap = sec.querySelector("[data-smatrix]");
    if (!wrap) { return; }
    var rows = toArray(wrap.querySelectorAll(".ks3-smatrix-row"));
    if (!rows.length) { return; }

    var from = wrap.getAttribute("data-from") || "";
    var LIT = {
      squash: wrap.getAttribute("data-lit-squash") || "",
      trails: wrap.getAttribute("data-lit-trails") || "",
      rest:   wrap.getAttribute("data-lit-rest") || ""
    };

    function bench() {
      var host = from ? document.getElementById(from) : null;
      return host ? host.querySelector("[data-sbench]") : null;
    }

    function paint() {
      var b = bench();
      // No bench on the page — a lesson that dropped it, or a build that
      // renamed the section. The table still reads correctly: it stays on the
      // resting row rather than lighting nothing, because the footnote under
      // it promises a highlight and an unlit table would make that a lie.
      var key = LIT.rest;
      if (b) {
        if (b.getAttribute("data-squash") === "1") { key = LIT.squash; }
        else if (b.getAttribute("data-trails") === "1") { key = LIT.trails; }
      }
      each(rows, function (tr) {
        var on = tr.getAttribute("data-row") === key;
        tr.setAttribute("data-lit", on ? "1" : "0");
        var head = tr.querySelector("th");
        if (!head) { return; }
        // R2 — the tint is never the only signal. Design draws colour alone
        // and the footnote promises the student a highlight, so the lit row
        // says so to a screen reader too.
        if (on) { head.setAttribute("aria-current", "true"); }
        else { head.removeAttribute("aria-current"); }
      });
    }

    document.addEventListener("ks3:statebench", paint);
    paint();
  }
