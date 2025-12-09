from functools import reduce
import itertools
import os
from math import sqrt
from pathlib import Path
import sys
from AOC_Helpers.dsa import DSU

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN = """

7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

IN = (
    (TEST_IN if len(sys.argv) > 1 else open(os.path.join(cur_path, "in.input")).read())
    .strip()
    .split("\n")
)



def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def size_of_square(a,b):
    s1 = abs(a[0]-b[0])+1
    s2 = abs(a[1]-b[1])+1
    print(s1,s2,a,b)
    return s1*s2

IN = [tuple(map(int, k.split(","))) for k in IN]

distances = [(a,b, size_of_square(a, b)) for a,b in itertools.combinations(IN, 2)]

a,b,d = max(distances, key=lambda x: x[2])
