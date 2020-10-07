import time

import numpy

from utils import open_file, remove_excess_and_filter_none

day = 10
year = 2018

TESTSTRING = ''''''
STRING = ''''''


class Star:
    def __init__(self, px, py, vx, vy):
        self.pos = complex(px, py)
        self.vel = complex(vx, vy)

    def move(self, t):
        self.pos += (self.vel) * t


def get_stars():
    stars = []
    with open('../inputs/input102018') as file:
        for string in file.readlines():
            st = string.replace('<', ' ').replace('>', ' ').replace(',', ' ')
            s = list(remove_excess_and_filter_none(st, ' '))
            px = int(s[1])
            py = int(s[2])
            vx = int(s[4])
            vy = int(s[5])
            stars.append(Star(px, py, vx, vy))

    return stars


def run1():
    stars = get_stars()
    t=0
    while True:
        for star in stars:
            star.move(1)
        t+=1


        pos_y = [s.pos.imag for s in stars]
        pos_x = [s.pos.real for s in stars]
        maxy = max(pos_y)
        miny = int(min(pos_y))
        maxx= max(pos_x)
        minx = int(min(pos_x))
        if max(pos_y) - min(pos_y)< 10:
            # print('woah')
            n = numpy.zeros(shape=(100,150))
            for s in stars:
                n[int(s.pos.real)-minx,int(s.pos.imag)-miny]=1
            print('woah')
            break
    return t

def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
