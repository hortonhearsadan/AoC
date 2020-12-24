import time
from collections import deque, defaultdict

from utils import open_file

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
STRING = """"""

directions = {
    "se": 0.5 - 1j,
    "e": 1,
    "w": -1,
    "ne": 0.5 + 1j,
    "sw": -0.5 - 1j,
    "nw": -0.5 + 1j,
}


def parse_input():
    f = open_file(day, year)
    # f=TESTSTRING.split("\n")
    inputs = []
    for line in f:
        l = deque(line.strip())
        tiles = []
        while l:
            d = l.popleft()
            if d in {"s", "n"}:
                d += l.popleft()
            tiles.append(directions[d])
        inputs.append(tiles)

    return inputs


def run1(data):
    tile_flips = defaultdict(int)
    for d in data:
        pos = sum(d)
        tile_flips[pos] += 1

    return {k for k, v in tile_flips.items() if v % 2 == 1}


def get_adj_tiles(t):
    return {t - 1, t + 1, t + 0.5 - 1j, t + 0.5 + 1j, t - 0.5 + 1j, t - 0.5 - 1j}


def run2(black_tiles):

    for i in range(1, 101):
        new_black_tiles = set()

        for t in black_tiles:
            adj = get_adj_tiles(t)
            adj_black_tiles = len(adj & black_tiles)

            if 0 < adj_black_tiles < 3:
                new_black_tiles.add(t)

            for ad in adj:
                if ad in black_tiles:
                    continue
                new_adj = get_adj_tiles(ad)
                if len(new_adj & black_tiles) == 2:
                    new_black_tiles.add(ad)
        black_tiles = new_black_tiles
        # print(f"{len(black_tiles)} Black Tiles after {i} days")
    return len(black_tiles)


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(f)
    print(f"Part 1: {len(f)}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
