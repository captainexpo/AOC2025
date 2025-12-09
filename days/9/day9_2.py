from collections import defaultdict
from functools import reduce
import itertools
import os
from math import sqrt
import pathlib as pl
import sys
from typing import DefaultDict, assert_never

from AOC_Helpers.dsa import DSU
import AOC_Helpers
import AOC_Helpers.matrix_utils as mat

cur_path = os.path.dirname(__file__)
parent_dir = pl.Path(__file__).resolve().parents[2]

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
    # print(s1,s2,a,b)
    return s1*s2

IN = list(reversed([(int(k.split(",")[0]), int(k.split(',')[1])) for k in IN]))

bounds = set()
bounds_xs = defaultdict(set)

for k in range(len(IN)):
    p1 = IN[k]
    p2 = IN[(k+1)%len(IN)]
    share_x = p1[0] == p2[0]
    share_y = p1[1] == p2[1]

    if share_x:
        is_up = p2[1] > p1[1]
        for y in range(min(p1[1],p2[1]), max(p1[1],p2[1])+1):
            bounds.add((p1[0], y))
            bounds_xs[y].add(p1[0])
    elif share_y:
        is_down = p2[0] > p1[0]
        for x in range(min(p1[0],p2[0]), max(p1[0],p2[0])+1):
            bounds.add((x, p1[1]))
            bounds_xs[p1[1]].add(x)
    else:
        raise ValueError("Non axis aligned edge")


shape_max_x = max(x for x,y in bounds)
print("Shape max x:", shape_max_x)
for k in bounds_xs:
    bounds_xs[k] = list(sorted(list(bounds_xs[k])))


# key = y value, value = list of ranges of x inside shape
insides = defaultdict(list)

# print("BX:", bounds_xs)
# print("BX:", bounds_xs)
for y in bounds_xs:
    ranges = []
    xs = bounds_xs[y]
    for i in range(0, len(xs)-1, 1):
        if xs[i]+1 < xs[i+1]:
            ranges.append( (xs[i], xs[i+1]) )
    insides[y] = ranges
# print("Insides:", insides)

def other_corners(a,b):
    return (a[0],b[1]), (b[0],a[1])
def in_range(val, r):
    return r[0] <= val <= r[1]
def point_in_bounds(p):

    for r in insides.get(p[1], []):
        if in_range(p[0], r):
            return True
    return False

def line_in_bounds(a,b):
    if a[0] == b[0]:
        x = a[0]
        for y in range(min(a[1],b[1]), max(a[1],b[1])+1):
            if (x,y) not in bounds and not point_in_bounds((x,y)):
                return False
        return True
    elif a[1] == b[1]:
        y = a[1]
        for x in range(min(a[0],b[0]), max(a[0],b[0])+1):
            if (x,y) not in bounds and not point_in_bounds((x,y)):
                return False
        return True
    else:
        raise ValueError("Non axis aligned line")
import itertools
from concurrent.futures import ProcessPoolExecutor


def check_pair(pair):
    a, b = pair
    oc1, oc2 = other_corners(a, b)
    if (
        line_in_bounds(a, oc1)
        and line_in_bounds(oc1, b)
        and line_in_bounds(b, oc2)
        and line_in_bounds(oc2, a)
    ):
        size = size_of_square(a, b)
        return (size, (a, b, oc1, oc2))
    return (0, None)


def parallel_max_square(IN, workers=None):
    combos = list(itertools.combinations(IN, 2))
    max_size = 0
    max_square = None

    with ProcessPoolExecutor(max_workers=workers) as ex:
        for idx, result in enumerate(ex.map(check_pair, combos)):
            size, square = result
            if size > max_size:
                max_size = size
                max_square = square
            print(f"Processed {idx+1}/{len(combos)} pairs.")

    return max_size, max_square

max_size, max_square = parallel_max_square(IN)
print("Max square size:", max_size)
print("Corners:", max_square)
