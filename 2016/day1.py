import time
from utils import open_file

day = 1
year = 2016

TESTSTRING = ''''''
STRING = ''''''


def get_direction(direction, dir):
    if dir == 'L':
        return direction * 1j
    elif dir == 'R':
        return direction * -1j


def run1():
    string = open_file(day, year)
    string = string.split(', ')
    position = complex(0)
    direction = 1j
    for s in string:
        dir = s[0]
        dist = int(s[1:])
        direction = get_direction(direction, dir)
        position += dist * direction
    return get_dist(position)


def get_dist(position):
    return int(abs(position.imag) + abs(position.real))


def run2():
    string = open_file(day, year)
    string = string.split(', ')
    position = complex(0)
    locations = {position}
    direction = 1j
    for s in string:
        dir = s[0]
        dist = int(s[1:])
        direction = get_direction(direction, dir)
        for d in range(dist):
            position += 1 * direction
            if position in locations:
                return get_dist(position)
            else:
                locations.add(position)


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
