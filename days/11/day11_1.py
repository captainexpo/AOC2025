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



aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
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

print(len(list(all_simple_paths(G, "you", "out"))))
