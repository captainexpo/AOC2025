import functools
from pprint import pprint
import itertools
import collections
import math
import os
from pathlib import Path
import sys
from typing import Optional
import pulp
from AOC_Helpers import *

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN = """

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

sys.setrecursionlimit(20000000)


IN = (
    (TEST_IN if len(sys.argv) > 1 else open(os.path.join(cur_path, "in.input")).read())
    .strip()
    .split("\n")
)

lights = []
buttons = []
joltages = []


for k in IN:
    l, *b, j = k.split(" ")
    l = l[1:-1]
    b = [tuple(map(int, x[1:-1].split(","))) for x in b]
    j = tuple(map(int, j[1:-1].split(",")))
    lights.append(l)
    buttons.append(b)
    joltages.append(j)


def solve_machine(jt, bt):
    r_bt = []
    for k in bt:
        l = [0] * len(jt)
        for j in k:
            l[j] = 1
        r_bt.append(l)

    but_len = len(r_bt)
    jolt_num = len(jt)


    # THANK THE LORD FOR PULP
    prob = pulp.LpProblem("GoofyAssMachine", pulp.LpMinimize)
    coefficents = [
        pulp.LpVariable(f"a_{i}", lowBound=0, cat=pulp.LpInteger)
        for i in range(but_len)
    ]
    prob += pulp.lpSum(coefficents)
    for j in range(jolt_num):
        prob += pulp.lpSum(coefficents[i] * r_bt[i][j] for i in range(but_len)) == jt[j]

    status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

    solution = [int(var.value()) for var in coefficents]
    return solution


n = 0
for j, b in zip(joltages, buttons):
    n += sum(solve_machine(j, b))
print(n)
