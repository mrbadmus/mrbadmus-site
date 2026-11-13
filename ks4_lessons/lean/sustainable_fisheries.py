# -*- coding: utf-8 -*-
"""Sustainable fisheries, in the lean shape. Spec table: ks4-sustainable-fisheries.md.

Legacy lesson (batch 10). The ladder and the practice set stay from the live page; the
logic_edits below fix the faults the audit found (see the table's audit section).
"""

LESSON = {
    "slug": "sustainable-fisheries",
    "start": {
        "setup": "Two boats fish for cod. One net has small holes. The other has large holes.",
        "question": "If you had to guess, which net leaves the cod stock in better shape for next "
                    "year?",
        "options": [
            ("Small holes",
             "Large holes. Young fish escape, grow up and breed, so the stock keeps going."),
            ("Large holes",
             "Large holes. Young fish escape, grow up and breed, so the stock keeps going."),
        ],
        "answer": 1,
    },
    "words": ["fish stock", "sustainable", "fishing quota", "mesh size"],
    "knowledge": [
        {"kind": "card", "title": "Declining stocks",
         "body": ["Fish stocks in the oceans are declining.",
                  "Fish are being caught faster than they can breed. Fewer adults are left to "
                  "replace the fish that are caught."]},
        {"kind": "card", "title": "Why it matters",
         "body": ["It is important to maintain fish stocks at a level where breeding continues, "
                  "or certain species may disappear altogether in some areas.",
                  "If too few adults are left to breed, the stock collapses.",
                  "Fish is an important source of protein for many people."]},
        {"kind": "card", "title": "Fishing quotas",
         "body": ["A fishing quota is a limit on how many fish of a species may be caught each "
                  "year.",
                  "Scientists estimate the size of the stock. The quota is set so that enough "
                  "adults are left to breed."]},
        {"kind": "card", "title": "Net size",
         "body": ["Rules set a minimum mesh size: the holes in the net must be big enough for "
                  "young fish to escape.",
                  "The young fish grow to breeding age and reproduce, so new fish join the stock "
                  "each year."]},
        {"kind": "card", "title": "Using stock data",
         "body": [{"slot": "fig:cod-stock-recovery"},
                  {"points": [
                      "Quote the values before and after the measures began.",
                      "Link each measure to more fish being left to breed.",
                      "Recovery takes years. The fish left must grow to breeding age, and their "
                      "young must grow too.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Nets with small holes are better because they catch more.",
              "They catch young fish before they can breed, so the stock falls."),
             ("Stop fishing for one year and the stock is back.",
              "Recovery takes as long as the fish take to grow up and breed: often several "
              "years."),
             ("A quota is a rule about net size.",
              "A quota limits how many fish are caught. Mesh size is the rule about the net."),
         ]}]},
    ],
    "key_fact": "Fish stocks must be kept at a level where breeding continues. Control of net "
                "size and fishing quotas help conserve fish stocks at a sustainable level: quotas "
                "limit the catch, and a larger mesh lets young fish escape to grow and breed.",
    "deeper": [
        {"kind": "card", "title": "Sustainable food",
         "body": ["Fishing to quotas, with nets of the right mesh size, is an example of "
                  "sustainable food production: the stock can be fished year after year."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong>: link a quota or a mesh size to more fish being left to "
             "breed.",
             "<strong>Describe</strong>: say what the data shows, with values and years.",
             "<strong>Evaluate</strong>: weigh the catch today against the stock in future.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-10",
        "logic_edits": [
            # Ladder r1 Q1: credited option 53 characters against 13 and 33.
            ("'Keeping the stock at a level where breeding continues'",
             "'Keeping enough fish so that breeding continues'"),
            ("['Catching as many fish as possible', 'That drives the stock down.']",
             "['Catching as many fish as you can every year', 'That drives the stock down.']"),
            ("['Never fishing', 'Sustainable fishing allows a limited catch.']",
             "['Stopping all fishing in the area for ever', 'Sustainable fishing allows a limited catch.']"),
            # Ladder r1 Q2: the prompt and a reply named "the spec"; "fish farming" is arguable.
            ("'Name the two methods the spec gives for conserving fish stocks.'",
             "'Name two methods used to conserve fish stocks at a sustainable level.'"),
            ("['Fish farming and fences', 'Not the spec’s methods.']",
             "['Smaller nets and longer fishing seasons', 'Both of these would catch more fish, not fewer.']"),
            ("['Bigger boats and sonar', 'Those catch more, not fewer.']",
             "['Bigger boats and better sonar', 'Those catch more, not fewer.']"),
            # Ladder r2 Q1: credited option 54 characters against 22 and 26.
            ("['It makes fish breed faster', 'Breeding rate does not change; the number left does.']",
             "['It makes the fish breed much faster than they did before', 'Breeding rate does not change; the number left does.']"),
            ("['It increases the catch', 'It limits it.']",
             "['It lets the boats catch more fish each year than before', 'A quota limits the catch.']"),
            # Ladder r2 Q2: "Use the data" is not a command word; the why line claimed
            # "slowly at first", which two values cannot show.
            ("MCQ('Use the data', 'Information (made up): a stock fell",
             "MCQ('Describe', 'Information (made up): a stock fell"),
            ("'The stock rose, slowly at first, from 60 000 to 160 000 tonnes.'",
             "'After 2001 the stock rose from 60 000 to 160 000 tonnes.'"),
            ("['It kept falling', 'It rose.']",
             "['It kept falling, to below 60 000 tonnes', 'It rose to 160 000 tonnes.']"),
            ("['It recovered fully in 2002', 'Recovery took about fifteen years.']",
             "['It rose to 160 000 tonnes in 2002', 'It took until 2015 to reach 160 000 tonnes.']"),
            # Ladder r3 Q2 herring: no "spec" talk on a pupil page.
            ("'The spec’s mechanism is breeding failure.'",
             "'They are caught faster than they can breed, so too few are left.'"),
            # Practice set item 1 (stem kept, so its id is kept): dash tails, credited option
            # the longest, a fuel-cost distractor that is partly true.
            ('"Young fish can escape through larger mesh — they reach adulthood, reproduce and maintain future stocks"',
             '"Young fish escape, grow to breeding age and reproduce"'),
            ('"Larger mesh catches more adult fish per trawl — increasing fishing efficiency"',
             '"Larger holes catch more of the big adult fish in each trawl"'),
            ('"Small fish are inedible — minimum mesh size prevents catching commercially worthless fish"',
             '"Small fish are not safe for people to eat, so are left alone"'),
            ('"Larger mesh allows water to flow through more easily — reducing fuel costs"',
             '"It lets the boats catch more fish in a shorter time"'),
            ('"Larger mesh actually catches FEWER fish per trawl — the benefit is conservation, not efficiency."',
             '"A larger mesh catches fewer fish, not more. The point is that young fish escape."'),
            ('"Small fish ARE edible and have commercial value — but catching them prevents them from reaching reproductive age."',
             '"Small fish can be eaten. Catching them stops them reaching breeding age."'),
            ('"Water flow through mesh is a minor consideration — conservation of juvenile fish is the primary reason for minimum mesh size rules."',
             '"A larger mesh catches fewer fish. It is there so young fish can escape and breed."'),
            # Practice set item 2 (stem kept): credited option 93 characters against 13 to 34.
            ("'A limit on how many fish of a species may be caught each year, set so that breeding continues'",
             "'A limit on how many fish may be caught each year'"),
            ("['A rule about the size of net holes', 'That is mesh size.']",
             "['A rule about the size of the holes in nets', 'That is mesh size.']"),
            ("['A tax on fish', 'A quota limits the catch, not the price.']",
             "['A tax that fishing boats pay on each fish', 'A quota limits the catch, not the price.']"),
            ("['A ban on all fishing', 'A quota allows a limited catch.']",
             "['A ban on all fishing in one area of sea', 'A quota allows a limited catch.']"),
            # Practice set item 3 (stem kept): credited option 71 characters against 15 to 31.
            ("'After the quota, enough fish were left to breed and the stock recovered'",
             "'The stock rose after the quota, so the quota may have helped'"),
            ("['The quota made the stock fall', 'The fall came before the quota; the rise after.']",
             "['The quota made the stock fall even further than before', 'The fall came before the quota; the rise after.']"),
            ("['The stock recovered in one year', 'It took ten years to reach 120 000.']",
             "['The stock recovered fully within a single year of the quota', 'It took ten years to reach 120 000.']"),
            ("['Nothing changed', 'The stock more than doubled after 2000.']",
             "['The stock stayed the same in the years after the quota', 'The stock more than doubled after 2000.']"),
            # Practice set item 4 (stem kept): credited option 76 characters against 16 to 38;
            # "The sea is too big to fish out" is a claim, not a cause.
            ("'Fish are caught faster than they can reproduce, so too few are left to breed'",
             "'Fish are caught faster than they can breed'"),
            ("['The sea is too big to fish out', 'Stocks are declining in many areas.']",
             "['Larger nets let the young fish escape', 'That helps a stock recover.']"),
            ("['Quotas kill fish', 'Quotas protect them.']",
             "['Too few boats fish in the area', 'Fewer boats catch fewer fish.']"),
            # Practice set item 5 (stem kept): credited option 76 characters against 24 to 31.
            ("'The remaining fish must reach breeding age, spawn, and their young must grow'",
             "'The fish left must grow to breeding age first'"),
            ("['Fish only live for a year', 'Many fish live for years and must mature first.']",
             "['Fish only live for about one year, so none are left', 'Many fish live for years and must mature first.']"),
            ("['The water has to warm up', 'Temperature is not the reason.']",
             "['The water has to warm up again before fish can breed', 'Temperature is not the reason.']"),
            ("['It does not: one year is enough', 'Most species need several years.']",
             "['It does not: one year without fishing is always enough', 'Most species need several years.']"),
        ],
    },
}
