import functools
from pprint import pprint
import itertools
import collections
import math
import os
from pathlib import Path
import sys
from typing import Optional
# import networkx as nx
# import pulp
from AOC_Helpers import *
import AOC_Helpers.matrix_utils as mat

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))


# THIS PROBLEM WAS SO ANNOYING, THE SOLUTION IS SO SIMPLE BUT I TRIED TO IMPLEMENT A PACKING ALGORITHM :((((((
# I FEEL SO STUPID :(((((


TEST_IN = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

IN = (
    (TEST_IN if len(sys.argv) > 1 else open(os.path.join(cur_path, "in.input")).read())
    .strip()
    .split("\n\n")
)


shapes = []
regions = []
for k in IN[:-1]:
    m = k.split("\n")[1:]
    area = 0
    for i in m:
        area += i.count('#')
    shapes.append(area)

print(shapes)


for m in IN[-1].split('\n'):
    i, *j =  m.split(" ")
    i = tuple(map(int, i[:-1].split('x')))
    j = list(map(int, j))

    regions.append((i[0]*i[1],j))
c = 0
for reg in regions:
    a0 = 0
    for idx, k in enumerate(reg[1]):
        a0 += shapes[idx]*k
    print(a0, reg)
    if a0 < reg[0]:
        print("DO")
        c += 1
print(c)


