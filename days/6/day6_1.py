import os
from pathlib import Path
import sys
import itertools as it
import re

import AOC_Helpers as help
from AOC_Helpers import matrix_utils

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN="""

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""

IN = (
    (
        TEST_IN if len(sys.argv) > 1
        else open(os.path.join(cur_path, "day6.input")).read()
    )
    .strip().split('\n')
)

IN = [re.split(r"\s+", i.strip()) for i in IN]
print(IN)
nums = IN[0:-1]
problems = IN[-1]
t = 0
for idx, k in enumerate(matrix_utils.transpose(nums)):
    s = int(k[0])
    for m in k[1:]:
        v= int(m)
        if problems[idx] == "*":
            s *= v
        elif problems[idx] == "+":
            s += v
    t += s
print(t)






