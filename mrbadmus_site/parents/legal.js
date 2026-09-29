/* ═══════════════════════════════════════════════════════════════════════
   parents/legal.js — renders the consumer Terms and Privacy Policy.

   The text is Mide's and is FINAL. It lives, unedited, in
   docs/b2c/legal/{terms,privacy}.md. `docs/` is not published, so the same
   bytes are served from parents/legal/{terms,privacy}.md and this file
   fetches and renders them. Those two pairs must stay byte-identical: change
   the wording in docs/b2c/legal/ first, then copy it over the served copy.
   Never edit the wording in this file — it has none.

   The renderer covers exactly what the two documents use: # and ## headings,
   paragraphs, **bold**, "- " lists, pipe tables and a horizontal rule. Every
   character is HTML-escaped before the bold pass, so the markdown cannot
   inject markup.
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  var C = window.MrBadmusConsumer;
  var esc = C.escapeHtml;

  /* The one address on these pages; used only if the text cannot load. */
  var INBOX = 'support@mrbadmus.com';

  var H1 = 'margin:14px 0 0;font-family:var(--ks3-font-display);font-weight:800;' +
    'font-size:clamp(40px,5.5vw,64px);line-height:.95;letter-spacing:-.04em;text-wrap:balance';
  var H2 = 'margin:44px 0 0;padding-top:24px;border-top:2px solid var(--ks3-rule);' +
    'font-family:var(--ks3-font-display);font-weight:800;font-size:clamp(22px,2.6vw,28px);' +
    'letter-spacing:-.03em;line-height:1.1';
  var P = 'margin:14px 0 0;font-size:17px;color:var(--ks3-ink-body);max-width:52em;text-wrap:pretty';
  var UL = 'margin:12px 0 0;padding-left:1.3em;font-size:17px;color:var(--ks3-ink-body);max-width:52em';
  var TABLE = 'width:100%;border-collapse:collapse;margin-top:16px;font-size:15px;color:var(--ks3-ink-body)';
  var CELL = 'text-align:left;vertical-align:top;padding:10px 12px;border:1px solid var(--ks3-rule)';

  function inline(text) {
    return esc(text).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  }

  function cells(line) {
    return line.replace(/^\s*\|/, '').replace(/\|\s*$/, '').split('|').map(function (c) { return c.trim(); });
  }

  function table(rows) {
    var head = cells(rows[0]);
    var body = rows.slice(2).map(cells);
    return '<div style="overflow-x:auto"><table style="' + TABLE + '"><thead><tr>' +
      head.map(function (c) { return '<th style="' + CELL + ';background:var(--ks3-card)">' + inline(c) + '</th>'; }).join('') +
      '</tr></thead><tbody>' +
      body.map(function (r) {
        return '<tr>' + r.map(function (c) { return '<td style="' + CELL + '">' + inline(c) + '</td>'; }).join('') + '</tr>';
      }).join('') + '</tbody></table></div>';
  }

  function markdown(src) {
    var lines = src.replace(/\r\n?/g, '\n').split('\n');
    var out = [];
    var i = 0;
    while (i < lines.length) {
      var line = lines[i];
      var m;
      if (!line.trim()) { i += 1; continue; }
      if ((m = /^(#{1,2})\s+(.*)$/.exec(line))) {
        out.push(m[1].length === 1
          ? '<h1 style="' + H1 + '">' + inline(m[2]) + '</h1>'
          : '<h2 style="' + H2 + '">' + inline(m[2]) + '</h2>');
        i += 1;
      } else if (/^-{3,}\s*$/.test(line)) {
        i += 1;
      } else if (/^\s*\|/.test(line)) {
        var rows = [];
        while (i < lines.length && /^\s*\|/.test(lines[i])) { rows.push(lines[i]); i += 1; }
        out.push(table(rows));
      } else if (/^-\s+/.test(line)) {
        var items = [];
        while (i < lines.length && /^-\s+/.test(lines[i])) { items.push(lines[i].replace(/^-\s+/, '')); i += 1; }
        out.push('<ul style="' + UL + '">' + items.map(function (t) {
          return '<li style="margin-top:6px">' + inline(t) + '</li>';
        }).join('') + '</ul>');
      } else {
        var para = [];
        while (i < lines.length && lines[i].trim() && !/^(#{1,2}\s|-\s|\s*\||-{3,}\s*$)/.test(lines[i])) { para.push(lines[i]); i += 1; }
        out.push('<p style="' + P + '">' + inline(para.join(' ')) + '</p>');
      }
    }
    return out.join('');
  }

  function render(host, spec) {
    fetch(spec.src, { credentials: 'omit' })
      .then(function (r) { if (!r.ok) throw new Error(String(r.status)); return r.text(); })
      .then(function (text) { host.innerHTML = markdown(text); })
      .catch(function () {
        host.innerHTML = '<p style="' + P + '">This page could not be loaded. Write to <a href="mailto:' +
          esc(INBOX) + '" style="font-weight:700">' + esc(INBOX) + '</a> and we will send it to you.</p>';
      });
  }

  window.MrBadmusLegal = { INBOX: INBOX, render: render, markdown: markdown };
})();
