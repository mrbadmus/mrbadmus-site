/* simulations/simulations.js — draws one subject page from simulations.json.
   A subject with at least one entry shows its list; a subject with none shows
   "Coming soon". To add a simulation: one entry in simulations.json plus its
   files under simulations/<subject>/<slug>/. */
(function () {
  'use strict';
  var main = document.getElementById('sim-main');
  if (!main) return;
  var subject = main.getAttribute('data-subject');

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function draw(all) {
    var mine = all.filter(function (s) { return s.subject === subject; });
    if (!mine.length) {
      main.innerHTML = '<h1>Coming soon</h1>';
      return;
    }
    main.innerHTML = '<h1>' + esc(main.getAttribute('data-title')) + '</h1><ul class="sim-list">' +
      mine.map(function (s) {
        return '<li><a class="sim-item" href="' + esc(s.path) + '"><span>' + esc(s.name) + '</span>' +
          '<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" ' +
          'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3l5 5-5 5"/></svg></a></li>';
      }).join('') + '</ul>';
  }

  fetch('/simulations/simulations.json', { cache: 'no-cache' })
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(draw)
    .catch(function () {
      main.innerHTML = '<h1>Could not load</h1><p class="sim-retry"><a href="">Try again</a></p>';
    });
})();
