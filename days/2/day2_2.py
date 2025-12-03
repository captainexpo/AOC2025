import os
from pathlib import Path
import sys


cur_path = os.path.dirname(__file__)
parent_dir = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(parent_dir))

TEST_IN="""

"""

IN = (
    (
        TEST_IN if len(sys.argv) > 1
        else open(os.path.join(cur_path, "day2.txt")).read()
    )
    .strip()
)
