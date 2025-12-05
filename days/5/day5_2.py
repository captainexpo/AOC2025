import os
from pathlib import Path
import sys
import itertools as it
import re

import AOC_Helpers as help

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN="""

3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

IN = (
    (
        TEST_IN if len(sys.argv) > 1
        else open(os.path.join(cur_path, "day5.input")).read()
    )
    .strip().split('\n\n')
)

5-10
6-9 # total
6-10 # total
5-11


def intersect(a, b):
    return a[0] <= b[1] and b[0] <= a[1]

ranges = [i.split("-") for i in IN[0].split("\n")]
ranges = [[int(i[0]), int(i[1])] for i in ranges]
changes = True
while changes:
    changes = False
    for i, a in enumerate(ranges):

        # a_min > b_min = b_min
        # a_max > b_max = a_max
        # a_min < b_min = a_min
        for j, b in enumerate(ranges):
            i = intersect(a,b)
            if not i: continue
            # if j == i:
            #     ranges.pop(j)
            #     changes = True
            #     break
            prev = b.copy()
            b[0] = min(a[0],b[0])
            b[1] = max(a[1], b[1])
            if prev != b: changes = True

# deduplicate
t = []
for k in ranges:
    if k not in t: t.append(k)

print(sum(map(lambda x: x[1] - x[0] + 1, t)))
