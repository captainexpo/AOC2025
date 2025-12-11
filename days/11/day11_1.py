import functools
from pprint import pprint
import itertools
import collections
import math
import os
from pathlib import Path
import sys
from typing import Optional
import networkx as nx
from networkx import Graph, all_simple_paths
from AOC_Helpers import *

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN = """


svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out

"""


IN = (
    (TEST_IN if len(sys.argv) > 1 else open(os.path.join(cur_path, "in.input")).read())
    .strip()
    .split("\n")
)


devices = {}
for i in IN:
    d, rest = i.split(": ")
    devices[d] = rest.split(" ")

G = nx.DiGraph(devices)

dp = {}
def dfs(cur: str, fft: bool, dac: bool) -> int:
    if (cur, fft, dac) in dp:
        return dp[(cur,fft,dac)]
    if cur == "out" and fft and dac:
        return 1
    if cur == "fft":
        fft = True
    if cur == "dac":
        dac = True


    s = 0
    for k in G[cur]:
        s += dfs(k, fft, dac)
    dp[(cur,fft,dac)] = s
    return s


print(dfs("svr", False, False))

