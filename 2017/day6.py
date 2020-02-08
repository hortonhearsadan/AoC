import time
from collections import defaultdict

from utils import open_file
import numpy as np

day = 0
year = 0

TESTSTRING = '''0   2   7   0'''
STRING = open_file(6, 2017)


def run1():
    banks = np.array(STRING.split('\t'), dtype=np.int)
    length = len(banks)
    layouts = set()
    count = 0
    while True:
        max_blocks_idx = np.argmax(banks)
        blocks_to_distribute = banks[max_blocks_idx]
        banks[max_blocks_idx] = 0
        for i in range(blocks_to_distribute):
            banks[(max_blocks_idx + 1 + i) % length] += 1
        count += 1
        b = banks.tostring()
        if b in layouts:
            return count
        else:
            layouts.add(b)


def run2():
    banks = np.array(STRING.split('\t'), dtype=np.int)
    length = len(banks)
    layouts = set()
    layout_dict = defaultdict(int)
    count = 0
    while True:
        max_blocks_idx = np.argmax(banks)
        blocks_to_distribute = banks[max_blocks_idx]
        banks[max_blocks_idx] = 0
        for i in range(blocks_to_distribute):
            banks[(max_blocks_idx + 1 + i) % length] += 1
        count += 1
        b = banks.tostring()
        if b in layouts:
            return count - layout_dict[b]

        else:
            layouts.add(b)
            layout_dict[b] = count


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
