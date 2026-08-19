"""The oak wood, drawn once, used by b9-01 and b9-03.

⊕ Mide's diagram ruling of 18 Aug 2026: code draws the diagrams itself, inline,
in Design's KS3 world. This module holds the DATA for the one food web the unit
teaches; `build_ks3.py::_food_web` holds the drawing.

**Why one module rather than a copy in each lesson.** b9-01 ends `#s-roles`
with *"A food chain is one route through an ecosystem. A food web is all the
routes at once… The web is the truthful picture; the chain is a single thread
pulled out of it so it can be talked about."* b9-03 then puts the student to
work on a wood and asks them to remove a species from it. Those two pages are
about the SAME wood, and the second lesson only lands if the web is recognisably
the one from the first. Two copies of this list would drift, and the drift would
be invisible: nothing checks that b9-01's caterpillars eat what b9-03's do. So
the wood is defined once and the two lessons differ by exactly one key —
b9-01 numbers a thread through it, b9-03 does not.

**Where the content comes from.** Design's `WEB_LINES` on
`docs/ks3/design-reference/b9/b9-03-disturbing-a-food-web.dc.html`, which states the
web in eight sentences. Every node and every feeding link below is one of those
sentences turned into geometry. Three notes on what is NOT a straight
transcription, because each is a science decision and they belong on the record:

1. **Trophic rows are assigned from what each organism eats, not from how
    dangerous it sounds.** Owls eat mice, and mice eat acorns and seeds, so owls
    are SECONDARY consumers and sit on the same row as the blue tits — not on a
    "top predator" row above the sparrowhawk. Sparrowhawks eat blue tits
    (tertiary) *and* mice (which would make them secondary), and that link is
    drawn crossing a row on purpose: it is the clearest thing on the diagram
    about why a web is not a ladder.

2. **`wildflowers → bees` is a feeding arrow this build ADDED.** Design's line
    7 says only *"Bees pollinate the wildflowers"*, which is not a feeding
    relationship and is drawn dashed. But a bee sitting in the primary-consumer
    row with no feeding arrow into it reads as an animal that eats nothing,
    which is a worse error than the one it avoids: bees feed on nectar and
    pollen from those flowers. Added under the science authority for this run
    and reported. It is true, it is KS3-appropriate, and it contradicts nothing
    on Design's page.

3. **Decomposers are drawn OFF the ladder, and the row says so in words.**
    Fungi and bacteria feed on dead material from every level, so there is no
    single trophic row they belong on. Two feeding arrows are drawn into them,
    from the oak and from the mice — a producer and a plant eater — because two
    arrows from two different levels say "every level" more legibly than ten
    arrows would, and the row note carries the general claim.

    ⊕ The second arrow was `sparrowhawk → fungi` first, and `_food_web`'s
    routing check REFUSED it: with one node on the tertiary row and one on the
    decomposer row, both sit at the row centre, and so does the middle node of
    any three-node row between them — so the link crossed the ladybirds on
    every route it tried, which reads as *the sparrowhawk eats ladybirds*. That
    is a claim the web does not make. `mice → fungi` is the same science on a
    line a student can actually follow.

⊕ **THE COUNT DISCREPANCY, RESOLVED — MRB-251 §2 / MRB-255 S14 (19 Aug 2026).**
This module raised it and deliberately did not resolve it: Design's page said
*"one oak wood, eight species"* in the bench eyebrow and *"a teaching web of
eight species"* in the legal note, while her own eight sentences name **eleven
organisms** — the oak, wildflowers, caterpillars, aphids, ladybirds, blue tits,
mice, owls, sparrowhawks, bees, and fungi and bacteria. The strings were lifted
byte-identical and left, because it is a copy finding and not a science one.

MRB-251 rules it: *the count must equal what the page draws, and the arithmetic
must follow it.* Eleven is this module's own count, arrived at here independently
of the audit, and b9-03 now uses it. The judgement MRB-251 leaves to Code is
whether the two collectives count as species: `wildflowers` and `fungi and
bacteria` are each drawn as ONE node standing for many species, so "species" is
the wrong noun for them. b9-03 therefore says *organisms* in the prose and drops
the count from the eyebrow entirely, which MRB-251 names as a valid fix.

The drawing itself still states no count of its own — no title, desc or caption
says "eight" or "eleven" — so it could not have contradicted the page and does
not now. **Nothing in this module changed; only its reasoning did.** If a count
is ever drawn into the SVG it must be eleven, and it must say organisms.
"""

# Rows are authored TOP-DOWN — tertiary consumers first, decomposers last —
# because that is the order an assistive technology traversing the SVG meets
# them, and reading down the trophic levels is the order that makes sense.
# `_food_web` draws them bottom-up from this same list, which is the order that
# makes sense to the eye: energy climbing.
OAK_WOOD_ROWS = [
    {"label": "TERTIARY", "note": "eats a predator",
     "tint": "var(--ks3-band)",
     "nodes": [{"id": "hawk", "name": "Sparrowhawk"}]},
    {"label": "SECONDARY", "note": "eats a plant eater",
     "tint": "var(--ks3-inset)",
     "nodes": [{"id": "bluetits", "name": "Blue tits"},
               {"id": "ladybirds", "name": "Ladybirds"},
               {"id": "owls", "name": "Owls"}]},
    {"label": "PRIMARY", "note": "eats a producer",
     "tint": "var(--ks3-band)",
     "nodes": [{"id": "caterpillars", "name": "Caterpillars"},
               {"id": "aphids", "name": "Aphids"},
               {"id": "mice", "name": "Mice"},
               {"id": "bees", "name": "Bees"}]},
    {"label": "PRODUCERS", "note": "captures sunlight",
     "tint": "var(--ks3-ok-tint)",
     "nodes": [{"id": "oak", "name": "The oak"},
               {"id": "flowers", "name": "Wildflowers"}]},
    {"label": "DECOMPOSERS", "note": "off the ladder — every level",
     "tint": "var(--ks3-inset)",
     "nodes": [{"id": "fungi", "name": "Fungi and bacteria"}]},
]

# (prey, eater) — and the order of the pair IS the arrow direction. `ECO-01` is
# that the arrow points at what the animal eats; it points the other way, and
# every pair here is written prey-first so that the data reads the way the
# drawing must.
OAK_WOOD_EATS = [
    ("oak", "caterpillars"),      # leaves
    ("oak", "aphids"),            # sap
    ("oak", "mice"),              # acorns
    ("flowers", "mice"),          # seeds
    ("flowers", "bees"),          # ADDED — see docstring note 2
    ("caterpillars", "bluetits"),
    ("aphids", "bluetits"),
    ("aphids", "ladybirds"),      # and nothing else
    ("mice", "owls"),
    ("bluetits", "hawk"),
    ("mice", "hawk"),             # crosses a row, on purpose
    ("oak", "fungi"),             # see docstring note 3
    ("mice", "fungi"),
]

# Not a feeding link, so not a solid arrow and not an energy claim.
OAK_WOOD_OTHER = [("bees", "flowers", "pollinates")]


def oak_wood(fig_id, title, desc, caption, thread=None):
    """One figure record for the wood. `thread` numbers a chain through it."""
    return {
        "id": fig_id,
        "kind": "diagram",
        "status": "drawn",
        "art": "food-web",
        "title": title,
        "desc": desc,
        "caption": caption,
        "data": {"rows": OAK_WOOD_ROWS,
                 "eats": OAK_WOOD_EATS,
                 "other": OAK_WOOD_OTHER,
                 "thread": thread or [],
                 "legend_other": "dashed: pollination, which moves no energy"},
    }
