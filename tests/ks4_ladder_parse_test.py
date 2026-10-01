#!/usr/bin/env python3
"""R16 (ks4_rulings.py): run the EXACT parse function the Ks4Ladder Apply
rung ships, in Node, against the approved cases. Exit 1 on any mismatch."""
import json, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ks4_rulings  # noqa: E402

CASES = [("63000", 63000), ("63 000", 63000), ("63,000", 63000),
         ("63 000.5", 63000.5), ("6,3", 6.3), ("1,234,567", 1234567),
         ("-0.25", -0.25), (" 42 ", 42), ("63 000", 63000),
         ("63 000", 63000), ("+42", 42), ("0,500", 0.5),
         ("63 000,5", 63000.5), ("1,234.5", 1234.5)]

js = ("var f = %s; var c = %s; process.stdout.write(JSON.stringify(c.map(function (x) { return f(x[0]); })));"
      % (ks4_rulings.R16_PARSE_FN, json.dumps(CASES)))
got = json.loads(subprocess.check_output(["node", "-e", js]))
bad = 0
for (raw, want), g in zip(CASES, got):
    ok = g is not None and abs(g - want) < 1e-9
    bad += not ok
    print("%s  %-14r -> %r (want %r)" % ("ok  " if ok else "FAIL", raw, g, want))
print("%d/%d passed" % (len(CASES) - bad, len(CASES)))
sys.exit(1 if bad else 0)
