import os
from pathlib import Path
import sys


cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN="""
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

IN = (
    (
        TEST_IN if len(sys.argv) > 1
        else open(os.path.join(cur_path, "day2.txt")).read()
    )
    .strip().split(",")
)

IN = [tuple(i.split("-")) for i in IN]

sum = 0

for k in IN:
    a,b = k
    for i in range(int(a), int(b)+1):
        i = str(i)
        il = len(i)
        for k in range(len(i)-1):
            if il % (k+1) != 0: continue
            sub = i[:k+1]
            if sub*(len(i)//len(sub)) == i:
                sum += int(i)
                break


print(sum)
