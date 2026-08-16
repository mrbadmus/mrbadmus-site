# ks3_parity.py — COMPONENTS entries for `scale-cards` (c1-05 #s-scale).
#
# Uses the same `C1_DIFF` page constant declared in the random-walk-bench
# fragment. No `drive` on any row: the panel is static and is on the page from
# the first paint, which is the whole character of the component.
#
# ⚠️ NOT mutation-tested by the authoring agent — no browser in this run. Each
# row would resolve differently if its rule were dropped; the commander should
# break each one once and confirm the row fails before these are kept.

    # ── scale-cards (c1-05 #s-scale) ──
    # A panel NESTED inside an ink-dark block, so it takes `--ks3-dark-panel`
    # on the muted rule. If it ever reports the block's own ground the three
    # cards stop reading as cards and the grid becomes three paragraphs.
    dict(name="scale card is a dark panel on the muted rule", on=C1_DIFF,
         sel=".ks3-scard",
         props={"background-color": "#3E3730",
                "border-top-color": "#C6B9A7", "border-top-width": "2px",
                "border-top-left-radius": "20px"}),

    # ⚑ REGISTERED BECAUSE IT IS FLAGGED, not because it is settled. PAYLOAD-MAP
    # §5.5.2: amber on ink is established for CONTROLS since B1 and for
    # misconception BLOCKS; this is amber for a body label, which is neither,
    # and the map flags it without resolving it. Pinning the value here means a
    # re-ruling arrives as a failing row that names itself, rather than as a
    # repaint nobody notices.
    dict(name="scale card distance is the flagged amber body label",
         on=C1_DIFF, sel=".ks3-scard-distance",
         props={"font-family": "DM Mono", "font-size": "12px",
                "text-transform": "uppercase", "color": "#FFC53D"}),

    # ⚠️ THE SPECIFICITY ROW. `.ks3-dark p` is (0,1,1) and a bare
    # `.ks3-scard-time` is (0,1,0): unscoped, this loses its `--ks3-on-dark`
    # and resolves to `#E7DECE` body copy, so the answer to the card's own
    # question renders as a caption. Same defect B1 shipped with the zoom
    # instrument and B2 was bitten by again.
    dict(name="scale card time is display 28px full on-dark, not body copy",
         on=C1_DIFF, sel=".ks3-scard-time",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "28px", "color": "#FBF3E6"}),
