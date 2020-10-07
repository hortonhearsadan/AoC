import time
from collections import defaultdict, deque

from utils import open_file
day = 9
year = 2018

TESTSTRING = ''''''
STRING = ''''''


def strip_input():
    with open('../inputs/inputs92018') as file:
        string = file.readline().split(' ')
    return int(string[0]), int(string[-2]) * 100
    # return  10, 1618

def run1():
    scores = defaultdict(int)
    circle = deque([0])
    max_players, last_marble = strip_input()
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
