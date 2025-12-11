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

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN = """

"""


IN = (
    (TEST_IN if len(sys.argv) > 1 else open(os.path.join(cur_path, "in.input")).read())
    .strip()
    .split("\n")
)
