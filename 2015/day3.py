import time
from enum import Enum

from utils import open_file

day = 3
year = 2015

TESTSTRING = '''^v^v^v^v^v'''
STRING = ''''''


class Movement(Enum):
    Up = '^'
    Down = 'v'
    Left = '<'
    Right = '>'


def movement(direction):
    if direction == Movement.Up.value:
        return 1j
    elif direction == Movement.Down.value:
        return -1j
    elif direction == Movement.Left.value:
        return -1
    elif direction == Movement.Right.value:
        return 1


def run1():
    string = open_file(day, year)
    position = complex(0)
    houses = {position}
    for s in string:
        position += movement(s)
        houses.add(position)
    return len(houses)


def run2():
    string = open_file(day, year)

    s_1 = string[::2]
    s_2 = string[1::2]
    strings = [s_1, s_2]
    houses = {complex(0)}
    for s_i in strings:
        position = complex(0)
        for s in s_i:
            position += movement(s)
            houses.add(position)
    return len(houses)


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
