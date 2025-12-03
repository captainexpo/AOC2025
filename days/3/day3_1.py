import os
from pathlib import Path
import sys


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
for bank in IN:
    bank = [int(x) for x in bank]
    g = 0
    for idx in range(len(bank)):
        for j in bank[idx:]:
            v = bank[idx]*10 + j
            if v > g:
                g = v
    sum += g
print(sum)
