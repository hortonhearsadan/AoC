import time

from utils import get_adjacent_with_diag

day = 0
year = 0

TEST1 = 1024
TEST2 = 23
STRING = 277678


def run1():
    center = complex()
    position = center
    step = -1j
    turn = 1j
    paths = set()
    for i in range(STRING - 1):
        paths.add(position)

        new_step = step * turn
        if position + new_step not in paths:
            position += new_step
            step = new_step
        else:
            position += step

    return abs(position.real) + abs(position.imag)


def run2():
    center = complex()
    position = center
    step = -1j
    turn = 1j
    paths = set()
    values = {center: 1}
    while values.get(position, 0) < STRING:
        paths.add(position)

        new_step = step * turn
        if position + new_step not in paths:
            position += new_step
            step = new_step
        else:
            position += step
        adj = get_adjacent_with_diag(position)
        values[position] = sum(values.get(a, 0) for a in adj)

    return values[position]


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
