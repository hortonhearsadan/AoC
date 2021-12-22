import time
from copy import deepcopy
from dataclasses import dataclass

from utils import open_file

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10"""
STRING = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682"""


ON = "on"
OFF = "off"


@dataclass
class Cuboid:
    switch: str
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int

    def __and__(self, o):
        x_min = max(self.x_min, o.x_min)
        x_max = min(self.x_max, o.x_max)
        if x_max < x_min:
            return
        y_min = max(self.y_min, o.y_min)
        y_max = min(self.y_max, o.y_max)
        if y_max < y_min:
            return
        z_min = max(self.z_min, o.z_min)
        z_max = min(self.z_max, o.z_max)
        if z_max < z_min:
            return

        return Cuboid("", x_min, x_max, y_min, y_max, z_min, z_max)

    def unwrap(self):
        return {
            (x, y, z)
            for x in range(self.x_min, self.x_max + 1)
            for y in range(self.y_min, self.y_max + 1)
            for z in range(self.z_min, self.z_max + 1)
        }

    def within_bounds(self, x_l, x_u, y_l, y_u, z_l, z_u):
        return (
            self.x_min >= x_l
            and self.x_max <= x_u
            and self.y_min >= y_l
            and self.y_max <= y_u
            and self.z_min >= z_l
            and self.z_max <= z_u
        )

    def __sub__(self, o):
        ixn = self & o
        if not ixn:
            return [self]

        cuboids = []

        if self.x_min < ixn.x_min:
            cuboids.append(self.clone(x_max=ixn.x_min - 1))
        if self.x_max > ixn.x_max:
            cuboids.append(self.clone(x_min=ixn.x_max + 1))

        if self.y_min < ixn.y_min:
            cuboids.append(
                self.clone(x_min=ixn.x_min, x_max=ixn.x_max, y_max=ixn.y_min - 1)
            )
        if self.y_max > ixn.y_max:
            cuboids.append(
                self.clone(x_min=ixn.x_min, x_max=ixn.x_max, y_min=ixn.y_max + 1)
            )

        if self.z_min < ixn.z_min:
            cuboids.append(
                self.clone(
                    x_min=ixn.x_min,
                    x_max=ixn.x_max,
                    y_min=ixn.y_min,
                    y_max=ixn.y_max,
                    z_max=ixn.z_min - 1,
                )
            )
        if self.z_max > ixn.z_max:
            cuboids.append(
                self.clone(
                    x_min=ixn.x_min,
                    x_max=ixn.x_max,
                    y_min=ixn.y_min,
                    y_max=ixn.y_max,
                    z_min=ixn.z_max + 1,
                )
            )

        return cuboids

    def clone(self, **kwargs):
        c = deepcopy(self)
        for k, v in kwargs.items():
            c.__setattr__(k, v)
        return c

    @property
    def size(self):
        return self.x * self.y * self.z

    @property
    def x(self):
        return self.x_max - self.x_min + 1

    @property
    def y(self):
        return self.y_max - self.y_min + 1

    @property
    def z(self):
        return self.z_max - self.z_min + 1


def parse_input():
    f = open_file(day, year)
    # f = STRING.split('\n')
    # f = TESTSTRING.split('\n')
    inputs = []
    for s in f:
        switch, dims = s.strip().split(" ")
        x, y, z = [d[2:] for d in dims.split(",")]
        x_min, x_max = [int(i) for i in x.split("..")]
        y_min, y_max = [int(i) for i in y.split("..")]
        z_min, z_max = [int(i) for i in z.split("..")]
        inputs.append(Cuboid(switch, x_min, x_max, y_min, y_max, z_min, z_max))

    return inputs


def run1(data, bounds=None):
    on_cubes = []
    for cuboid in data:
        if bounds and not cuboid.within_bounds(*bounds):
            continue
        new_on_cubes = []
        for c in on_cubes:
            new_on_cubes.extend(c - cuboid)

        if cuboid.switch == ON:
            new_on_cubes.append(cuboid)

        on_cubes = new_on_cubes

    return sum(c.size for c in on_cubes)


def run2(data):
    pass


def test_subtract():
    a = Cuboid("on", 10, 15, 10, 15, 10, 15)
    b = Cuboid("off", 11, 12, 11, 12, 11, 12)

    c = a - b
    for i in c:
        print(i)
    assert len(c) == 6


if __name__ == "__main__":
    # test_subtract()
    a = time.time()
    inputs = parse_input()
    f = run1(inputs, (-50, 50, -50, 50, -50, 50))
    g = run1(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
