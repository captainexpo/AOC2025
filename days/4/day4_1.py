import os
from pathlib import Path
import sys
import itertools as it
import re

import AOC_Helpers.matrix_utils as mat

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN="""

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

IN = (
    (
        TEST_IN if len(sys.argv) > 1
        else open(os.path.join(cur_path, "day4.input")).read()
    )
    .strip().split('\n')
)

IN = [list(i) for i in IN]

a = 0
for idx in range(len(IN)):
    for jdx in range(len(IN[idx])):
        n = mat.get_neighbors(jdx, idx, IN)
        k = list(map(lambda x: IN[x[1]][x[0]], n))
        print(k)
        if IN[idx][jdx] == "@" and k.count("@") < 4:
            print(idx, jdx)
            a += 1
print(a)

