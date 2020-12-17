import time
from utils import open_file, get_adjacent_with_diag

dir_path = __file__.split('/')
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = '''.#.
..#
###'''
STRING = ''''''

class Qrtn:
    def __init__(self,slice,c):
        self.z =slice
        self.c = c

    def __repr__(self):
        return f"{self.z},{self.x},{self.y}"

    @property
    def x(self):
        return self.c.real

    @property
    def y(self):
        return self.c.imag

    def __eq__(self, o):
        return self.c == o.c and self.z == o.z


    def __hash__(self):
        return hash((self.z,self.c))

def get_adjacent(qrtn):
    adj = get_adjacent_with_diag(qrtn.c)
    slices = {qrtn.z +1, qrtn.z -1}
    adjacent = {Qrtn(s,qrtn.c) for s in slices}
    adjacent |= {Qrtn(qrtn.z,i) for i in get_adjacent_with_diag(qrtn.c)}
    for s in slices:
        for a in adj:
            adjacent.add(Qrtn(s,a))
    return adjacent

def get_adjacent_2(qrtn):
    adj = get_adjacent_with_diag(qrtn.c)
    slices = get_adjacent_with_diag(qrtn.z)
    adjacent = {Qrtn(s,qrtn.c) for s in slices}
    adjacent |= {Qrtn(qrtn.z,i) for i in get_adjacent_with_diag(qrtn.c)}
    for s in slices:
        for a in adj:
            adjacent.add(Qrtn(s,a))
    adjacent.discard(qrtn)
    return adjacent


def parse_input():
    f = open_file(day,year)
    # f=TESTSTRING.split('\n')
    inputs=[]
    for i,j in enumerate(f):
        for k,l in enumerate(j):
            if l =="#":
                inputs.append(Qrtn(0,complex(k,-i)))

    return set(inputs)

def run1(data,cycles,get_adj):
    actives = data.copy()
    for r in range(cycles):
        new_actives = set()
        adjs=set()
        for d in actives:

            adj = get_adj(d)
            if 2<=len(adj & actives) <=3:
              new_actives.add(d)

            for ad in adj:
                if ad in actives:
                    continue
                if adj in new_actives:
                    continue
                if len(get_adj(ad) & actives) == 3:
                    new_actives.add(ad)
        actives = new_actives
    return len(actives)

def run2(data):
    pass


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs,6,get_adjacent)
    g = run1(inputs,6,get_adjacent_2)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
