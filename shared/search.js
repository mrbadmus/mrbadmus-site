/* ═══════════════════════════════════════════════════════════════
   MrBadmusAI — shared search overlay (MRB-26)
   Search from any page. Backed by window.MRB_SEARCH_INDEX
   (loaded from /shared/search-index.js). Opened by the nav 🔍 icon
   via MRBSearch.open(). Self-contained; themes via CSS tokens.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  if (window.MRBSearch) return; // guard against double-inclusion

  var overlay, input, results, built = false;

  function injectStyles() {
    if (document.getElementById('mrb-search-styles')) return;
    var css = ''
      + '.mrb-search-overlay{position:fixed;inset:0;z-index:300;display:none;'
      + 'background:rgba(36,28,20,0.45);backdrop-filter:blur(2px);padding:12vh 16px 16px;}'
      + '.mrb-search-overlay.open{display:block;}'
      + '.mrb-search-box{max-width:600px;margin:0 auto;background:var(--card);'
      + 'border:1px solid var(--border-strong);border-radius:var(--radius-lg);'
      + 'box-shadow:var(--shadow-pop);overflow:hidden;}'
      + '.mrb-search-box input{width:100%;border:none;outline:none;background:var(--card);'
      + 'color:var(--text);font-family:var(--font-sans);font-size:1.05rem;padding:18px 20px;}'
      + '.mrb-search-box input::placeholder{color:var(--muted);}'
      + '.mrb-search-results{max-height:52vh;overflow-y:auto;border-top:1px solid var(--border);}'
      + '.mrb-search-results:empty{display:none;}'
      + '.mrb-sr-item{display:flex;align-items:center;gap:10px;padding:12px 20px;'
      + 'border-bottom:1px solid var(--border);font-size:0.92rem;color:var(--text);text-decoration:none;}'
      + '.mrb-sr-item:last-child{border-bottom:none;}'
      + '.mrb-sr-item:hover,.mrb-sr-item.active{background:var(--accent-soft);}'
      + '.mrb-sr-chip{font-size:0.72rem;padding:2px 8px;border-radius:10px;font-weight:600;flex-shrink:0;}'
      + '.mrb-sr-empty{padding:16px 20px;color:var(--muted);font-size:0.9rem;font-style:italic;}'
      + '.mrb-sr-hint{padding:10px 20px;color:var(--muted);font-size:0.78rem;border-top:1px solid var(--border);}';
    var s = document.createElement('style');
    s.id = 'mrb-search-styles';
    s.textContent = css;
    document.head.appendChild(s);
  }

  function build() {
    if (built) return;
    injectStyles();
    overlay = document.createElement('div');
    overlay.className = 'mrb-search-overlay';
    overlay.id = 'mrbSearchOverlay';
    overlay.innerHTML =
      '<div class="mrb-search-box">' +
      '<input type="text" id="mrbSearchInput" placeholder="🔍 Search topics e.g. photosynthesis, forces…" autocomplete="off" autocapitalize="off" spellcheck="false"/>' +
      '<div class="mrb-search-results" id="mrbSearchResults"></div>' +
      '</div>';
    document.body.appendChild(overlay);
    input = overlay.querySelector('#mrbSearchInput');
    results = overlay.querySelector('#mrbSearchResults');

    // Close when the backdrop (not the box) is clicked.
    overlay.addEventListener('mousedown', function (e) {
      if (e.target === overlay) close();
    });
    input.addEventListener('input', render);
    input.addEventListener('keydown', onKey);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && overlay.classList.contains('open')) close();
    });
    built = true;
  }

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s;
    return d.innerHTML;
  }

  function render() {
    var q = input.value.trim().toLowerCase();
    var index = window.MRB_SEARCH_INDEX || [];
    if (q.length < 2) {
      results.innerHTML = '<div class="mrb-sr-hint">Type at least 2 letters to search ' + index.length + ' topics.</div>';
      return;
    }
    var matches = index.filter(function (m) {
      return m.t.toLowerCase().indexOf(q) !== -1 || m.s.toLowerCase().indexOf(q) !== -1;
    }).slice(0, 10);
    if (!matches.length) {
      results.innerHTML = '<div class="mrb-sr-empty">No topics match “' + esc(input.value.trim()) + '”. Try another word.</div>';
      return;
    }
    results.innerHTML = matches.map(function (m, i) {
      return '<a class="mrb-sr-item' + (i === 0 ? ' active' : '') + '" href="' + m.url + '">' +
        '<span class="mrb-sr-chip" style="background:' + m.c + '22;color:' + m.c + '">' + esc(m.s) + '</span>' +
        '<span>' + esc(m.t) + '</span></a>';
    }).join('');
  }

  function onKey(e) {
    var items = results.querySelectorAll('.mrb-sr-item');
    if (!items.length) return;
    var active = results.querySelector('.mrb-sr-item.active');
    var idx = Array.prototype.indexOf.call(items, active);
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (active) active.classList.remove('active');
      items[Math.min(idx + 1, items.length - 1)].classList.add('active');
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (active) active.classList.remove('active');
      items[Math.max(idx - 1, 0)].classList.add('active');
    } else if (e.key === 'Enter') {
      e.preventDefault();
      (active || items[0]).click();
    }
  }

  function open() {
    build();
    overlay.classList.add('open');
    input.value = '';
    render();
    setTimeout(function () { input.focus(); }, 30);
  }
  function close() {
    if (overlay) overlay.classList.remove('open');
  }

  window.MRBSearch = { open: open, close: close };
})();
