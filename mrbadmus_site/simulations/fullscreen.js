/* simulations/fullscreen.js — the Full screen button on every lab.
   Click puts the lab in full screen (the browser's Fullscreen API where it
   exists; on iPhone Safari, which has none, the page simply fills the screen)
   and fullscreen.css hides everything except the simulation, its controls and
   its key tickboxes. Esc or the same button leaves it. */
(function () {
  'use strict';
  var root = document.documentElement;
  var btn = document.querySelector('.sim-fs');
  if (!btn) return;

  function api() {
    return root.requestFullscreen ? 'std' : root.webkitRequestFullscreen ? 'webkit' : '';
  }
  function fsElement() { return document.fullscreenElement || document.webkitFullscreenElement || null; }

  function paint(on) {
    root.classList.toggle('sim-full', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    var label = on ? 'Exit full screen' : 'Full screen';
    btn.setAttribute('aria-label', label);
    btn.querySelector('.sim-fs__text').textContent = label;
    btn.querySelector('.sim-fs__in').hidden = on;
    btn.querySelector('.sim-fs__out').hidden = !on;
    // the canvases size themselves from the window
    window.dispatchEvent(new Event('resize'));
  }

  function enter() {
    paint(true);
    try {
      var p = root.requestFullscreen ? root.requestFullscreen() : root.webkitRequestFullscreen && root.webkitRequestFullscreen();
      if (p && p.catch) p.catch(function () {});
    } catch (e) {}
  }
  function leave() {
    paint(false);
    if (fsElement()) {
      try { (document.exitFullscreen || document.webkitExitFullscreen).call(document); } catch (e) {}
    }
  }

  btn.addEventListener('click', function () {
    if (root.classList.contains('sim-full')) leave(); else enter();
  });

  // The browser left full screen by itself (Esc, a swipe, F11): follow it.
  function onChange() {
    if (!fsElement() && root.classList.contains('sim-full') && api()) paint(false);
  }
  document.addEventListener('fullscreenchange', onChange);
  document.addEventListener('webkitfullscreenchange', onChange);

  // Without the API there is no browser Esc, so supply one.
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && root.classList.contains('sim-full') && !fsElement()) leave();
  });
})();
