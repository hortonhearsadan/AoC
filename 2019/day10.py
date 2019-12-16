import cmath
import itertools
import math
import time
from collections import defaultdict

STRING = '''#.#.###.#.#....#..##.#....
.....#..#..#..#.#..#.....#
.##.##.##.##.##..#...#...#
#.#...#.#####...###.#.#.#.
.#####.###.#.#.####.#####.
#.#.#.##.#.##...####.#.##.
##....###..#.#..#..#..###.
..##....#.#...##.#.#...###
#.....#.#######..##.##.#..
#.###.#..###.#.#..##.....#
##.#.#.##.#......#####..##
#..##.#.##..###.##.###..##
#..#.###...#.#...#..#.##.#
.#..#.#....###.#.#..##.#.#
#.##.#####..###...#.###.##
#...##..#..##.##.#.##..###
#.#.###.###.....####.##..#
######....#.##....###.#..#
..##.#.####.....###..##.#.
#..#..#...#.####..######..
#####.##...#.#....#....#.#
.#####.##.#.#####..##.#...
#..##..##.#.##.##.####..##
.##..####..#..####.#######
#.#..#.##.#.######....##..
.#.##.##.####......#.##.##'''

TEST_STRING = '''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####'''
TEST_STRING2 = '''#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.'''
TEST_STRING3 = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''


class System:
    def __init__(self):
        self.asteroids = []
        self.laser = None


def is_asteroid(s):
    return s == '#'


def get_asteroids(string):
    string_rows = len(string.split('\n'))
    string = string.replace('\n', '')
    elements = len(string)
    asteroids = []
    for i, s in enumerate(string):
        if is_asteroid(s):
            y, x = divmod(i, string_rows)
            asteroids.append(complex(x, -y))
    return asteroids


def get_polar(p0):
    x, y = p0
    return math.hypot(x, y), math.degrees(math.atan2(y, x))


def invert_deg(deg):
    return (deg + 180) % 360


def get_polar_deg(x, y):
    return math.degrees(math.atan2(y, x))


def run1():
    system = System()
    string = STRING
    # p = time.time()
    asteriods = get_asteroids(string)
    # print('asteroids', time.time()-p)
    # p = time.time()

    asteroid_pairs = itertools.combinations(asteriods, 2)
    # print('pairs',time.time()-p)
    # p = time.time()

    asteroid_gradients = defaultdict(list)
    for p1, p2 in asteroid_pairs:
        p0 = p2 - p1
        deg = cmath.phase(p0)
        opp_deg = cmath.phase(-p0)

        asteroid_gradients[p1].append(deg)
        asteroid_gradients[p2].append(opp_deg)

    # print('gradients', time.time()-p)
    # p = time.time()

    max_detected = 0
    best_ast = complex()
    for ast, detected in asteroid_gradients.items():
        det = len(set(detected))
        if det > max_detected:
            max_detected = det
            best_ast = ast
    system.asteroids = asteriods
    system.laser = best_ast
    # print('laser_find',time.time()-p)

    return max_detected, system


def normalise(deg):
    return (-deg + 90) % 360


def run2(system):
    laser = system.laser
    asteroids = system.asteroids
    asteroids.remove(laser)
    polars = []
    polar_dict = defaultdict(list)
    ast_dict = {}
    for asteroid in asteroids:
        p0 = asteroid - laser
        dist, deg = cmath.polar(p0)
        deg = math.degrees(deg)
        deg = normalise(deg)
        ast_dict[dist, deg] = asteroid
        polar_dict[deg].append(dist)

    degs = sorted(polar_dict.keys())
    i = 0
    while i < 200:
        for d in degs:
            _d = d
            if len(polar_dict[d]) > 0:
                dis = sorted(polar_dict[d])[0]
                polar_dict[d].remove(dis)
                i += 1
                if i == 200:
                    break

    _200_ast = ast_dict[dis, _d]

    return 100 * _200_ast.real - _200_ast.imag


if __name__ == "__main__":
    start_time = time.time()
    f, system = run1()
    g = run2(system)
    print(f"Part 1:", f)
    print(time.time() - start_time)
    start_time = time.time()
    print(f"Part2:", g)
    print(time.time() - start_time)

    a = ()
