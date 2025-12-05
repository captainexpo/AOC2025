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


ranges = [i.split("-") for i in IN[0].split("\n")]
ranges = [(int(i[0]), int(i[1])) for i in ranges]
ids = [int(i) for i in IN[1].split("\n")]

f = 0
for i in ids:
    ok = False
    for k in ranges:
        if i >= k[0] and i <= k[1]:
            ok = True
            break
    if ok: f += 1

print(f)
