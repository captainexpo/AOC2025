from collections import defaultdict
from functools import reduce
import os
from pprint import pprint
from math import sqrt
from pathlib import Path
import sys
import itertools as it
import re
from disjoint_union import DisjointUnion
import AOC_Helpers as help
from AOC_Helpers.dsa import DSU
import AOC_Helpers.graph_utils as gu
import AOC_Helpers.matrix_utils as mu
import AOC_Helpers.tuple_utils as tu
import AOC_Helpers.file_utils as fu
import AOC_Helpers.utils as ut

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN = """

162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689

"""

IN = (
    (TEST_IN if len(sys.argv) > 1 else open(os.path.join(cur_path, "in.input")).read())
    .strip()
    .split("\n")
)

IN = [i.split(",") for i in IN]

boxes = [(int(i), int(j), int(k)) for i, j, k in IN]

def dist(a, b):
    s = 0
    for k, j in zip(a, b):
        s += (k - j) ** 2
    return sqrt(s)

def get_all_dist():
    l = []
    for a in boxes:
        for b in boxes:
            if a == b:
                continue
            l.append((a,b,dist(a,b)))
    return list(sorted(l, key=lambda x: x[2]))[0::2]

all_dist = get_all_dist()

ds = DSU()
for k in boxes:
    ds.make_set(k)
pos = -1
for i in all_dist:
    a,b,_ = i
    ds.union(a,b)
    if len(ds.components()) == 1:
        print(a,b,a[0]*b[0])
        exit(0)
print(ds)
print(reduce(lambda a,b: a*b, list(sorted([len(i) for i in ds.components()], reverse=True))[0:3]))
