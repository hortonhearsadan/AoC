import itertools
import math
import time

import numpy as np

from utils import *

STRING = '''<x=-14, y=-4, z=-11>
<x=-9, y=6, z=-7>
<x=4, y=1, z=4>
<x=2, y=-14, z=-9>'''

TEST_STRING = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

TEST_STRING2 = '''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''
TEST_STRING3 = ''''''


def get_velocity(axis, m):
    pass


class System:
    def __init__(self, n_bodies, dim):
        self.space = None
        self.n_bodies = n_bodies
        self.dim = dim
        self.energy = 0

    def gen_space(self):
        self.space = np.zeros((self.n_bodies, self.dim))
        self.velocity_space = np.zeros((self.n_bodies, self.dim))

    def populate_space(self, moons):
        for m in moons:
            self.space[m.i] = m.position

    def get_new_velocities(self):
        for d in range(self.dim):
            axis = self.space[:, d]
            for i in range(self.n_bodies):
                self.velocity_space[(i, d)] += self.get_velocity(axis, i)

    def get_velocity(self, axis, i):
        p = axis[i]
        return np.count_nonzero(axis > p) - np.count_nonzero(axis < p)

    def apply_velocities(self):
        self.space += self.velocity_space

    def calculate_energy(self):
        s = np.absolute(self.space)
        v = np.absolute(self.velocity_space)
        self.energy = sum(np.sum(s[i]) * np.sum(v[i]) for i in range(self.n_bodies))


class Moon2:
    def __init__(self, i, x, y, z):
        self.i = i
        self.position = np.array([x, y, z])
        self.velocity = np.array([0, 0, 0])
        self.pot = 0
        self.kin = 0
        self.energy = 0

    # def move(self):
    #     self.position.x += self.velocity.x
    #     self.position.y += self.velocity.y
    #     self.position.z += self.velocity.z

    def get_energy(self):
        self.pot = self.position.sum()
        self.kin = self.velocity.sum()
        self.energy = self.pot * self.kin


def get_moons2(string):
    string = string.split('\n')
    moons = []
    i = 0
    for s in string:
        x, y, z = tuple(remove_excess_and_filter_none(s, "[<>=xyz, ]"))
        moons.append(Moon2(i, int(x), int(y), int(z)))
        i += 1
    return moons


def run1():
    string = TEST_STRING2
    moons = get_moons2(string)
    pairs = list(itertools.combinations(moons, 2))
    steps = 100
    system = System(4, 3)
    system.gen_space()
    system.populate_space(moons)
    for i in range(steps):
        system.get_new_velocities()
        system.apply_velocities()
    system.calculate_energy()
    return system.energy


def run2():
    string = STRING
    moons = get_moons2(string)
    pairs = list(itertools.combinations(moons, 2))
    steps = 0
    states = set()
    system = System(4, 3)
    system.gen_space()
    system.populate_space(moons)
    x_p = np.array2string(system.space[:,0])
    x_v = np.array2string(system.velocity_space[:,0])
    y_p = np.array2string(system.space[:,1])
    y_v = np.array2string(system.velocity_space[:,1])
    z_p = np.array2string(system.space[:,2])
    z_v = np.array2string(system.velocity_space[:,2])
    s = np.concatenate([system.space, system.velocity_space])
    x_states =set()
    y_states = set()
    z_states = set()
    x_states.add((x_p,x_v))
    y_states.add((y_p,y_v))
    z_states.add((z_p,z_v))
    match_x = 0
    match_y = 0
    match_z = 0
    step_list=[]
    l_step=0
    r_x, r_y, r_z = None, None, None
    xx,yy,zz =None,None,None
    while True:
        steps += 1
        system.get_new_velocities()
        system.apply_velocities()
        x_p = np.array2string(system.space[:, 0])
        x_v = np.array2string(system.velocity_space[:, 0])
        y_p = np.array2string(system.space[:, 1])
        y_v = np.array2string(system.velocity_space[:, 1])
        z_p = np.array2string(system.space[:, 2])
        z_v = np.array2string(system.velocity_space[:, 2])
        x= (x_p,x_v)
        y= (y_p,y_v)
        z= (z_p,z_v)

        if not match_x:
            if x in x_states:
                match_x = True
                l_step = steps
                r_x= x
                print('x found',steps)
                step_list.append(steps)
            else:
                x_states.add(x)
        if not match_y:
            if y in y_states:
                match_y = True
                l_step = steps
                r_y = y
                print('y found',steps)
                step_list.append(steps)
            else:
                y_states.add(y)
        if not match_z:
            if z in z_states:
                r_z = z
                match_z = True
                l_step=steps
                print('z found',steps)
                step_list.append(steps)

            else:
                z_states.add(z)

        if x== r_x and not l_step == steps:
            print('x found',steps)
            xx= True
            step_list.append(steps)
        if y== r_y and not l_step == steps:
            print('y found',steps)
            yy=True
            step_list.append(steps)
        if z== r_z and not l_step == steps:
            print('z found',steps)
            zz=True
            step_list.append(steps)

        if xx and yy and zz:
            break


    print(step_list)
    return 3


if __name__ == "__main__":
    start_time = time.time()
    f = run1()
    g = run2()
    # h = run3()
    print(f"Part 1:", f)
    print(f"Part2:", g)
    print(time.time() - start_time)
