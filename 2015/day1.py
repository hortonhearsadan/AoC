import time

from utils import open_file

day = 1
year = 2015

TESTSTRING = ''')())())'''
STRING = ''''''


def run1():
    string = open_file(day, year)
    floor = string.count('(') - string.count(')')
    return floor


def run2():
    string = open_file(day, year)
    floor = 0
    for i, s in enumerate(string):
        if s == '(':
            floor += 1
        elif s == ')':
            floor -= 1

        if floor < 0:
            return i + 1


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
