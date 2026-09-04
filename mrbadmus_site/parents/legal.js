/* ═══════════════════════════════════════════════════════════════════════
   parents/legal.js — the shared furniture of the two legal pages.
   MRB-317 Night 4, lane C (item C2).

   ── WHAT THESE PAGES ARE TONIGHT, STATED PLAINLY ───────────────────────
   ⚠️ THE CONSUMER TERMS AND THE CONSUMER PRIVACY POLICY DO NOT EXIST.
   Mide's text is not on disk: there is no `docs/b2c/legal/`, no `terms.md`,
   no `privacy.md`. The only privacy document in the estate is the
   SCHOOL-facing `MrBadmusAI_Privacy_Policy.docx`, which is the B2B one and
   is not this. Writing the missing text here was considered and refused:
   invented terms and an invented privacy policy would be false statements
   about a real company's obligations, published to paying parents, and
   they would be believed. A visible gap is recoverable; a plausible lie is
   not. This is Mide's ruling 7 on MRB-317 and an owner item on MRB-319 —
   **beta does not open until he supplies both.**

   So each page is FURNITURE plus a SCAFFOLD:
   · the nav, footer, heading, last-updated line and contact route are
     finished and styled, so landing the real text is a paste;
   · an unmissable notice says the text is not published yet;
   · the section headings from MRB-319's owner checklist are listed, each
     with the one line saying what it has to cover, so Mide can see the
     shape of what he is being asked for rather than a blank page.

   ── WHY A SHARED RENDERER RATHER THAN TWO PAGES ────────────────────────
   The same reason `public.js` holds the nav: two copies of the notice is
   one copy that gets updated when the text lands. When the real text
   arrives, `sections` grows a `body` per entry and `PLACEHOLDER` is deleted
   in one place — and the day it is deleted, BOTH pages stop claiming to be
   unfinished, which is the failure mode that would otherwise ship.
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  var C = window.MrBadmusConsumer;
  var P = window.MrBadmusPublic;
  var esc = C.escapeHtml;

  /* The one address on these pages. `support@mrbadmus.com` is the inbox
     MRB-319 is standing up for launch; both a complaint under the terms and
     a data-rights request under the privacy notice have to reach a human,
     and until Mide names separate routes they are the same human. */
  var INBOX = 'support@mrbadmus.com';

  /* ── the notice ────────────────────────────────────────────────────────
     Alert tokens, a 3px border and the accent block shadow: this is the
     loudest treatment the KS3 design system has, and it is used here for
     the only thing on the estate that is genuinely not finished. It is
     ABOVE the section list, not below it, so it cannot be scrolled past. */
  function placeholder(what) {
    return '<section role="note" style="margin-top:32px;padding:clamp(22px,3vw,30px);' +
      'border:3px solid var(--ks3-alert-border);border-radius:var(--ks3-r-card);' +
      'background:var(--ks3-alert-tint);box-shadow:6px 6px 0 var(--ks3-alert)">' +
      '<p style="margin:0;font-family:var(--ks3-font-mono);font-size:13px;letter-spacing:.14em;' +
      'text-transform:uppercase;color:var(--ks3-alert-text)">Not published yet</p>' +
      '<p style="margin:10px 0 0;font-family:var(--ks3-font-display);font-weight:800;' +
      'font-size:clamp(24px,3vw,30px);letter-spacing:-.03em;line-height:1.1;color:var(--ks3-ink)">' +
      'The ' + esc(what) + ' has not been published.</p>' +
      '<p style="margin:12px 0 0;font-size:17px;color:var(--ks3-ink-body);max-width:46em">' +
      'This page is ready for it and the wording is being finalised. Nothing here is a ' +
      'summary of the ' + esc(what) + ' and nothing here should be relied on. Until it is ' +
      'published, ask us directly and we will answer in writing.</p>' +
      '<p style="margin:14px 0 0;font-size:17px">' +
      '<a href="mailto:' + esc(INBOX) + '" style="font-weight:700">' + esc(INBOX) + '</a></p>' +
      '</section>';
  }

  /* ── the scaffold ──────────────────────────────────────────────────────
     Each entry renders as a real `<h2>` in the real type, with its
     "must cover" line beneath it in the muted colour and in italics, so
     that a reader can tell at a glance which words are the document and
     which are the note about the document. When the text lands, the note is
     replaced by the clause and the italics go with it.

     Numbered because a legal document is cited by clause number and because
     a numbered gap is obviously a gap. */
  function sections(list) {
    return '<div style="margin-top:56px">' + list.map(function (s, i) {
      return '<section style="padding:26px 0;border-top:2px solid var(--ks3-rule)">' +
        '<p style="margin:0;font-family:var(--ks3-font-mono);font-size:13px;letter-spacing:.12em;' +
        'color:var(--ks3-ink-muted)">' + (i + 1) + '</p>' +
        '<h2 style="margin:6px 0 0;font-family:var(--ks3-font-display);font-weight:800;' +
        'font-size:clamp(22px,2.6vw,28px);letter-spacing:-.03em;line-height:1.1">' +
        esc(s.h) + '</h2>' +
        '<p style="margin:10px 0 0;font-size:17px;font-style:italic;color:var(--ks3-ink-muted);' +
        'max-width:52em;text-wrap:pretty">To cover: ' + esc(s.must) + '</p>' +
        '</section>';
    }).join('') + '</div>';
  }

  /* ── the tail ──────────────────────────────────────────────────────────
     The entity line is the same string `public.js` puts in the footer, and
     it is repeated here on purpose: on a legal page the counterparty is
     part of the content, not the chrome. */
  function tail(extra) {
    return '<section style="margin-top:48px;padding:clamp(22px,3vw,30px);' +
      'border:2px solid var(--ks3-ink);border-radius:var(--ks3-r-card);background:var(--ks3-card)">' +
      '<h2 style="margin:0;font-family:var(--ks3-font-display);font-weight:800;font-size:24px;' +
      'letter-spacing:-.03em;line-height:1.1">Who you are dealing with</h2>' +
      '<p style="margin:12px 0 0;font-size:17px;color:var(--ks3-ink-body);max-width:46em">' +
      'MrBadmus is a trading name of <strong>3rd Eye Ltd</strong>, registered in England. ' +
      'Write to <a href="mailto:' + esc(INBOX) + '" style="font-weight:700">' + esc(INBOX) +
      '</a>' + (extra ? ' ' + esc(extra) : '') + '</p>' +
      /* The registered number and address are deliberately NOT typed here.
         Both are facts about a real company and neither is on disk; a
         guessed company number on a legal page is the same failure as
         guessed terms, in miniature. They land with the text. */
      '<p style="margin:10px 0 0;font-size:15px;color:var(--ks3-ink-muted)">' +
      'Company number and registered address are published with the full text.</p>' +
      '</section>';
  }

  /* ── the whole page ────────────────────────────────────────────────── */
  function render(host, spec) {
    host.innerHTML =
      '<p style="margin:0;font-family:var(--ks3-font-mono);font-size:13px;letter-spacing:.14em;' +
      'text-transform:uppercase;color:var(--ks3-ink-muted)">' + esc(spec.eyebrow) + '</p>' +
      '<h1 style="margin:14px 0 0;font-family:var(--ks3-font-display);font-weight:800;' +
      'font-size:clamp(40px,5.5vw,64px);line-height:.95;letter-spacing:-.04em;max-width:16em;' +
      'text-wrap:balance">' + esc(spec.title) + '</h1>' +
      '<p style="margin:22px 0 0;font-size:20px;color:var(--ks3-ink-body);max-width:34em;' +
      'text-wrap:pretty">' + esc(spec.intro) + '</p>' +
      /* The last-updated line of a legal document is load-bearing — it is
         what tells a parent which version they agreed to — so it is here
         from the start, saying the true thing rather than a date. */
      '<p style="margin:18px 0 0;font-family:var(--ks3-font-mono);font-size:14px;' +
      'color:var(--ks3-ink-muted)">Last updated: not yet published</p>' +
      placeholder(spec.what) +
      '<h2 style="margin:56px 0 0;font-family:var(--ks3-font-display);font-weight:800;' +
      'font-size:clamp(26px,3vw,34px);letter-spacing:-.035em;line-height:1">What this page will cover</h2>' +
      sections(spec.sections) +
      tail(spec.tailExtra);
  }

  window.MrBadmusLegal = {
    INBOX: INBOX,
    render: render
  };
})();
