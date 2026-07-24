/* ============================================================
   MrBadmus — KEYED RENDER  (Bonding v2 · MRB-134 Phase 1.6 · Law 9)

   "Motion is meaning." The root cause of the frame-swap bug was
   every hero doing `vizSlot.innerHTML = ''` per render, so the CSS
   transitions already declared on atoms / electrons / ions never had
   a prior rendered state to animate FROM — every change looked like
   an instant jump.

   This is a small keyed reconciler. Each viz element carries a stable
   `key`. On render the caller passes a fresh descriptor list; existing
   nodes with a matching key are REUSED and their mutable props
   (position / size / value / colour) updated — so the transition
   already on the node fires — new keys are created, dead keys removed.
   Node identity is preserved across a state change; that preserved
   identity is exactly what lets the browser animate the change instead
   of repainting it.

   The pure geometry functions in each engine are untouched: they still
   compute coordinates. Only the rendering layer changes — from
   "build a bag of fresh DOM nodes" to "describe keyed nodes and let
   the reconciler diff them."

   PUBLIC API:
     MrbKeyedRender.reconcile(container, descriptors, opts)

   descriptor: {
     key    : string,                 // stable across renders
     create : function() -> Node,     // build the node once (no per-frame state)
     update : function(node, isNew),  // set mutable props; transitions fire here
     enter  : function(node)?         // optional spawn state for a NEW node, so it
                                      //   animates INTO place from a pre-move position
                                      //   (ignored under reduced motion)
   }
   opts: {
     reduceMotion : bool?,            // default = the media query
     exit         : function(node)?   // optional teardown for a dead key (e.g. fade
                                      //   then remove); under reduced motion the node
                                      //   is removed immediately instead
   }

   Reduced motion: NEW nodes are placed directly at their end state (no
   enter animation), dead nodes are removed instantly (no exit fade),
   and because persisted nodes get their end props set with the CSS
   transition still declared, the caller is responsible for making that
   transition a no-op under reduced motion where required (the engines
   do: their transitions are on transform/position only and reduced
   users still land on the correct end-state instantly because the same
   props are set — see each engine's reduced-motion handling).
============================================================ */
(function () {
  'use strict';
  if (window.MrbKeyedRender) return;

  function reduceMotion() {
    return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  }

  function reconcile(container, descriptors, opts) {
    if (!container) return {};
    opts = opts || {};
    var reduce = (opts.reduceMotion != null) ? opts.reduceMotion : reduceMotion();
    var prev = container.__mrbKeyed || {};   // key -> node (from the last render)
    var next = {};
    var i, d, node;

    for (i = 0; i < descriptors.length; i++) {
      d = descriptors[i];
      if (!d || d.key == null) continue;
      node = prev[d.key];
      if (node) {
        /* REUSE — same DOM node. Updating its position/size/value now
           fires the transition already declared on it (it has a prior
           rendered state to move from). This is the whole point. */
        if (d.update) d.update(node, false);
        delete prev[d.key];
      } else {
        /* NEW — create once. If an enter state is given and motion is
           allowed, place the node at the enter state, commit that frame
           with a forced reflow, then move it to the real state on the
           next animation frame so the transition animates it in. */
        node = d.create();
        if (node && node.setAttribute) node.setAttribute('data-k', d.key);
        if (d.enter && !reduce) {
          d.enter(node);
          container.appendChild(node);
          void node.offsetWidth;            // flush the enter frame
          (function (n, dd, key) {
            requestAnimationFrame(function () {
              if (!n.parentNode) return;                       // removed before we ran
              if (container.__mrbKeyed && container.__mrbKeyed[key] !== n) return; // superseded
              if (dd.update) dd.update(n, true);
            });
          })(node, d, d.key);
        } else {
          if (d.update) d.update(node, true);
          container.appendChild(node);
        }
      }
      next[d.key] = node;
    }

    /* REMOVE dead keys (present last render, absent now). */
    for (var k in prev) {
      node = prev[k];
      if (!node) continue;
      if (!reduce && typeof opts.exit === 'function') {
        opts.exit(node);                    // caller fades + removes on its own timer
      } else if (node.parentNode) {
        node.parentNode.removeChild(node);
      }
    }

    container.__mrbKeyed = next;
    return next;
  }

  window.MrbKeyedRender = { reconcile: reconcile, reduceMotion: reduceMotion };
})();
