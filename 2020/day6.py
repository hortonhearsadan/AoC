import time
from utils import open_file

day = 6
year = 2020

TESTSTRING = """abc

a
b
c

ab
ac

a
a
a
a

b"""
STRING = """"""


def parse_input():
    with open(f"../inputs/input{day}{year}") as f:
        strings = f.read()
    strings = strings.split("\n\n")
    for i, s in enumerate(strings):
        new_s = s.replace("\n", ",").replace(" ", ",")
        if new_s[-1] == ",":
            new_s = new_s[:-1]
        strings[i] = new_s

    return strings


def get_num_people(i):
    return i.count(",") + 1


def get_unique_answers(i):
    return set(i) - {","}


def run1():
    return sum(len(get_unique_answers(i)) for i in inputs)


def run2():
    count = 0
    for i in inputs:
        people = get_num_people(i)
        answers = get_unique_answers(i)
        for ans in answers:
            if i.count(ans) == people:
                count += 1
    return count
    # return sum(i.count(ans) == get_num_people(i) for i in inputs for ans in set(i)-{','}) # One line


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1()
    g = run2()
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
