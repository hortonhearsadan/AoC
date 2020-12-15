import time
from functools import reduce

from utils import open_file

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """939
7,13,x,x,59,x,31,19"""
STRING = """"""


class Data:
    def __init__(self, arrival, buses, idx):
        self.arrival = arrival
        self.buses = buses
        self.idx = idx


def parse_input():
    f = open_file(day, year)
    # f=TESTSTRING.split('\n')
    arrival = int(f[0])
    buses = []
    idx = []
    for i, b in enumerate(f[1].split(",")):
        if b.isdigit():
            b = int(b)
            buses.append(b)
            idx.append(i)
    return Data(arrival, buses, idx)


def run1(data):
    return reduce(lambda x, y: x * y, min(((bus - data.arrival % bus, bus) for bus in data.buses), key=lambda x: x[0]))


def run2(data):
    n = reduce(lambda x, y: x * y, data.buses)
    return sum((y - x) * n // y * pow(n // y, y - 2, y) for x, y in zip(data.idx, data.buses)) % n



if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
