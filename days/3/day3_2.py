import os
from pathlib import Path
import sys
import itertools

cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN="""
987654321111111
811111111111119
234234234234278
818181911112111
"""

IN = (
    (
        TEST_IN if len(sys.argv) > 1
        else open(os.path.join(cur_path, "day3.input")).read()
    )
    .strip().split('\n')
)
sum = 0
def highest_val(j, n):
    g = 0
    k = None
    for i in range(len(j)):
        v = j[i]*10**min(len(j)-i, 12-n)
        if v > g:
            g = v
            k = i

    return k
for b in IN:
    b = [int(i) for i in b]

    k = ""
    l_v = 0
    for i in range(12):
        v = highest_val(b[l_v:],i)
        k += str(b[l_v+v])
        l_v = l_v+(v+1)
        print(l_v)
    print(k)
    sum += int(k)



print(sum)

