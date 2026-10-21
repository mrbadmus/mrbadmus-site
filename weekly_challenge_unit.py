#!/usr/bin/env python3
"""weekly_challenge_unit.py -- Unit C's three pure Node suites, run as one gate.

    python3 weekly_challenge_unit.py

  tools/set_work_challenge_test.js     the teacher's sheet (shared/set-work.js):
                                       invisible until ready, exact POST body,
                                       Undo -> DELETE, error words, the closing
                                       instant in BST and GMT
  tools/student_challenge_rows_test.js the pupil class page's rows
                                       (shared/student-live.js)
  tools/teacher_challenge_cards_test.js the teacher class page's card and its
                                       week bucketing (shared/teacher-live.js)

Each loads the REAL file in a bare vm / `require` sandbox; none touches a
network, a database or a browser, so this stays `fast`.
"""

import os
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)

SUITES = ("tools/set_work_challenge_test.js",
          "tools/student_challenge_rows_test.js",
          "tools/teacher_challenge_cards_test.js")


def main():
    bad = 0
    for s in SUITES:
        r = subprocess.run(["node", s], capture_output=True, text=True)
        tail = (r.stdout.strip().splitlines() or [""])[-1]
        print("   %s  %s  (%s)" % ("PASS" if r.returncode == 0 else "FAIL", s, tail))
        if r.returncode != 0:
            bad += 1
            print(r.stdout[-1500:], r.stderr[-800:])
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
