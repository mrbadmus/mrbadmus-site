KS3 Physics P10 — Magnetism and electromagnetism
MrBadmusAI · Key Stage 3 Science

Five lessons, one standalone viewable HTML each. Open any file directly in a
browser; nothing needs a server.

  p10-01-magnets-and-poles.dc.html
  p10-02-magnetic-fields.dc.html
  p10-03-the-earth-is-a-magnet.dc.html
  p10-04-electromagnets.dc.html
  p10-05-how-a-motor-works.dc.html

Alongside them:
  support.js   the runtime every page loads
  _ds/         the MrBadmusAI design system (tokens, fonts, component CSS)

Slugs, titles, families and the lesson count are taken from ks3_data/structure.py
character for character. Every lesson teaches from nothing and assumes no other
lesson has been taught.

Delivery notes are in NOTES-P10.md.


Changed 23 Aug 2026
-------------------
The bench caption on the pages listed below was a template hole inside an SVG
<text> element, which renders nothing — the caption was invisible on every
state. Each one is now an absolutely-positioned HTML <span> over the diagram,
the same technique those pages already use for their other live labels. No
caption wording, diagram geometry or bench logic changed.
  p10-05-how-a-motor-works.dc.html            the axle caption

Packaged 21 Aug 2026, repackaged 23 Aug 2026 with the caption fix above.
