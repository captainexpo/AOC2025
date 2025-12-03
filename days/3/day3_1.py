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

from concurrent.futures import ProcessPoolExecutor
from itertools import combinations

def process_bank(bank):
    bank = list(map(int, bank))
    best = 0
    n = len(bank)

    for idx, jdx, kdx in combinations(range(n), 3):
        nb = bank.copy()
        nb.pop(idx)
        nb.pop(jdx - 1)
        nb.pop(kdx - 2)
        s = int("".join(map(str, nb)))

        if s > best:
            best = s

    return best


total = 0
with ProcessPoolExecutor() as ex:
    for g in ex.map(process_bank, IN):
        total += g
print(total)

