import functools
from pprint import pprint
import itertools
import collections
import math
import os
from pathlib import Path
import sys
from typing import Optional
from AOC_Helpers import *
 # from sympy import symbols, Eq, solve
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


print(lights[0])
pprint(buttons[0])
print()
# print(joltages)


def solve_machine(light, btns, joltage) -> int:
    light = list(map(lambda x: -1 if x == "." else 1, light))
    dp = {}
    def dfs(state: list[int], seq: list[int], depth: int, states_hit: set) -> Optional[int]:
        if state == light:
            # print(seq)
            return depth
        ts = tuple(state)
        if ts in dp:
            return depth + dp[ts]
        if tuple(state) in states_hit:
            return None
        m = 1000000
        states_hit.add(tuple(state))
        for i in btns:
            n_state = state[:]
            for k in i:
                n_state[k] *= -1
            res = dfs(n_state, seq + [i], depth+1, states_hit.copy())
            if res is not None and res < m:
                m = res
        dp[ts] = m-depth
        return m
    return dfs([-1]*len(light), [], 0, set())

n = []
for l,b,j in zip(lights,buttons,joltages):
    n.append(solve_machine(l,b,j))
print(n, sum(n))

