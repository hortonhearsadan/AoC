import time
from enum import IntEnum

import numpy as np

STRING = """"""
TESTSTRING = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""


class Status(IntEnum):
    UNCLAIMED = -1
    CONTESTED = -2


class Coord:
    def __init__(self, idx, x, y):
        self.index = idx
        self.x = x
        self.y = y
        self.point = (x, y)
        self.used_points = set()


class Expander:
    def __init__(self, space, x_max, y_max):
        self.space = space
        self.x_min = 0
        self.x_max = x_max
        self.y_max = y_max
        self.y_min = 0
        self.claimed_points = set()

    def expand(self, coord: Coord, radius):
        x, y = coord.point
        points = []
        for r in range(-radius, radius + 1):
            x1 = min(self.x_max, max(self.x_min, x + r))
            dist = radius - abs(x1 - x)
            for s in range(-dist, dist + 1):
                y1 = min(self.y_max, max(y + s, self.y_min))
                t = (x1, y1)
                if t not in coord.used_points:
                    points.append((x1, y1))
        return set(points)

    def check_points_for_coord(self, coord: Coord, points):

        i = coord.index
        for x, y in points:
            self.check_point(x, y, i)

        coord.used_points |= points
        self.claimed_points |= points

    def check_point(self, x, y, i):
        p = self.space[y, x]
        if p == Status.UNCLAIMED:
            self.space[y, x] = i
        elif p == i:
            return
        elif not p == Status.CONTESTED:
            self.space[y, x] = Status.CONTESTED

    def process_coords(self, coords):
        for radius in range(10):
            for c in coords:
                points = self.expand(c, radius)
                self.check_points_for_coord(c, points)


def run1():
    import numpy as np
    from scipy.spatial import distance

    # read the data using scipy
    points = np.loadtxt('input6.txt', delimiter=', ')

    # build a grid of the appropriate size - note the -1 and +2 to ensure all points
    # are within the grid
    xmin, ymin = points.min(axis=0) - 1
    xmax, ymax = points.max(axis=0) + 2

    # and use mesgrid to build the target coordinates
    xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
    targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

    # happily scipy.spatial.distance has cityblock (or manhatten) distance out
    # of the box
    cityblock = distance.cdist(points, targets, metric='cityblock')
    # the resulting array is an input points x target points array
    # so get the index of the maximum along axis 0 to tie each target coordinate
    # to closest ID
    closest_origin = np.argmin(cityblock, axis=0)
    # we need to filter out points with competing closest IDs though
    min_distances = np.min(cityblock, axis=0)
    competing_locations_filter = (cityblock == min_distances).sum(axis=0) > 1
    # note, integers in numpy don't support NaN, so make the ID higher than
    # the possible point ID
    closest_origin[competing_locations_filter] = len(points) + 1
    # and those points around the edge of the region for "infinite" regions
    closest_origin = closest_origin.reshape(xgrid.shape)
    infinite_ids = np.unique(np.vstack([
        closest_origin[0],
        closest_origin[-1],
        closest_origin[:, 0],
        closest_origin[:, -1]
    ]))
    closest_origin[np.isin(closest_origin, infinite_ids)] = len(points) + 1

    # and because we know the id of the "null" data is guaranteed to be last
    # in the array (it's highest) we can index it out before getting the max
    # region size
    print(np.max(np.bincount(closest_origin.ravel())[:-1]))


def run2():
    import numpy as np
    from scipy.spatial import distance

    # read the data using scipy
    points = np.loadtxt('input6.txt', delimiter=', ')

    # build a grid of the appropriate size - note the -1 and +2 to ensure all points
    # are within the grid
    xmin, ymin = points.min(axis=0) - 1
    xmax, ymax = points.max(axis=0) + 2

    # and use mesgrid to build the target coordinates
    xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
    targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

    # happily scipy.spatial.distance has cityblock (or manhatten) distance out
    # of the box
    cityblock = distance.cdist(points, targets, metric='cityblock')

    # turns out using this method the solution is easier that before - simply
    # sum the distances for each possible grid location
    origin_distances = cityblock.sum(axis=0)
    # set the value of appropriate distances to 1, with the remainder as zero
    region = np.where(origin_distances < 10000, 1, 0)
    # and the sum is the result.
    print(region.sum())


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"sleepiest_guard id * minutes asleep", f)
    print(f"guard id * minutes asleep:", g)
