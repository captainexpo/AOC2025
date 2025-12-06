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

TEST_IN="""123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """

IN = (
    (
        TEST_IN if len(sys.argv) > 1
        else open(os.path.join(cur_path, "day6.input")).read()
    )
    .split('\n')
)


def split_every_n(input_string, n): return [input_string[i:i+n] for i in range(0, len(input_string), n)]
def lpad(s, thing, width):
    return thing*(width-len(s))+s
def rpad(s, thing, width):
    return s+thing*(width-len(s))

IN = [i for i in IN]
l = len(max(IN, key=lambda x: len(x)))
IN = [rpad(i, " ", l) for i in IN]
nums = IN[0:-1]
problems = IN[-1]
t = 0
tr = matrix_utils.transpose(nums)
ntr = []
c = []
for idx in range(len(tr)):
    if len(c) > 1 and problems[idx] != " ":
        ntr.append(c)
        c = []
    c.append(tr[idx])
ntr.append(c)

s = 0
problems = list(reversed(re.split("\s+", problems.strip())))
for idx, i in enumerate(reversed(ntr)):
    i = list(reversed([int(re.sub("\s+", "", "".join(k).strip())) for k in i if not all(m == " " for m in k)]))
    v = i[0]
    for l in i[1:]:
        if problems[idx] == "+":
            v += l
        else:
            v *= l
    s += v

print(s)






