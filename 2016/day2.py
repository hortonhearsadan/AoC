import time
from utils import open_file

day = 0
year = 0

TESTSTRING = ''''''
STRING = ''''''


def move(l, b):
    if l == 'L':
        return b - 1 if b.real > 0 else b
    if l == 'R':
        return b + 1 if b.real < 2 else b
    if l == 'U':
        return b + 1j if b.imag < 0 else b
    if l == 'D':
        return b - 1j if b.imag > -2 else b
    else:
        return None


def manipulate(c):
    return int(-3 * c.imag +c.real +1)


def run1():
    string = open_file(2, 2016)
    button = complex(1, -1)
    code = []
    for s in string:
        s= s.replace('\n','')
        for l in s:
            button = move(l, button)
        code.append(button)
    return [manipulate(c) for c in code]


def simple_move(l, b):
    if l == 'L':
        return b - 1
    if l == 'R':
        return b + 1
    if l == 'U':
        return b + 1j
    if l == 'D':
        return b - 1j


def move_complex(l, b):
    if abs(b.imag) + abs(b.real) < 2:
        return simple_move(l,b)
    else:
        pass


def run2():
    string = open_file(2, 2016)
    button = complex(0, 0)
    code = []
    for s in string:
        s = s.replace('\n', '')
        for l in s:
            button = move_complex(l, button)
        code.append(button)
    return [manipulate(c) for c in code]


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
