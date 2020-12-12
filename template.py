import time
from utils import open_file
dir_path = __file__.split('/')
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = ''''''
STRING = ''''''

def parse_input():
    pass

def run1(inputs):
    pass


def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
