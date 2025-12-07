import os
from pathlib import Path
import sys
import itertools as it
import re

import AOC_Helpers as help

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN = """

.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

IN = (
    (TEST_IN if len(sys.argv) > 1 else open(os.path.join(cur_path, "in.input")).read())
    .strip()
    .split("\n")
)
IN = [list(x) for x in IN]

res = 0

start_pos = 0+0j
for idx in range(len(IN)):
    f = False
    for jdx in range(len(IN[idx])):
        if IN[idx][jdx] == "S":
            start_pos =complex(jdx, idx)
            f = True
            break
    if f: break

beams = [start_pos]
# all_splits = set()
while len(beams) > 0:
    # print(beams)
    topop = []
    inserts = []
    for idx, k in enumerate(beams):
        if int(k.imag) >= len(IN)-1:
            topop.append(k)
            break
        c = IN[int(k.imag+1)][int(k.real)]
        if c in ".S":
             beams[idx] += 1j
        elif c == "^":
            # all_splits.add(k)
            res += 1
            inserts.extend(i for i in [k+1+1j, k-1+1j] if i not in beams and i not in inserts)
            topop.append(k)
    for p in topop:
        beams.remove(p)
    for k in inserts:
        beams.append(k)
print("Result:", res)
