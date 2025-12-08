import os
from pathlib import Path
import sys
import itertools as it
import re

import AOC_Helpers as help
import AOC_Helpers.graph_utils as gu
import AOC_Helpers.matrix_utils as mu
import AOC_Helpers.tuple_utils as tu
import AOC_Helpers.file_utils as fu
import AOC_Helpers.utils as ut

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

res = 0

print("Result:", res)
