import os
from pathlib import Path
import sys
import itertools as it
import re

import AOC_Helpers as help
import AOC_Helpers.matrix_utils as mat
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

beams = [[1, start_pos]]
counts = [[0 for _ in i] for i in IN]
# all_splits = set()


# Shoutout to my math teacher for this DP solution.
# He taught me this method for finding number of possible paths between two points on a grid, and this is essentially the same thing

def in_inserts(val):
    for k in inserts:
        if k[1] == val:
            return k
    return None
while len(beams) > 0:
    # print(beams)
    topop = []
    inserts = []

    # print(len(beams))
    for idx, (count, k) in enumerate(beams):
        # print(idx, count, k)
        if int(k.imag) >= len(IN)-1:
            topop.append([count, k])
            break
        c = IN[int(k.imag+1)][int(k.real)]
        if c in ".S":
            beams[idx][1] += 1j
            k = beams[idx][1]
            counts[int(k.imag)][int(k.real)] += count
        elif c == "^":
            # all_splits.add(k)
            prospects = [k+1+1j, k-1+1j]
            for m in prospects:
                v = in_inserts(m)
                if v is not None:
                    v[0] += count
                    continue
                else:
                    inserts.append([count, m])
            topop.append([count, k])
    for p in topop:
        beams.remove(p)
    # print(len(inserts))
    for k in inserts:
        beams.append(k)
# print("Result:", res)
# for i in counts:
#     print(" ".join(map(str, i)))
print(sum(counts[-1]))
