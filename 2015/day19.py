import time
from utils import open_file
day = 19
year = 2015

TESTSTRING = ''''''
STRING = ''''''

def run1():
    string = open_file(day,year)


def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
