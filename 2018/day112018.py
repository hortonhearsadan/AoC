import time
from utils import open_file
SERIALNUMBER=8772
import numpy as np

TESTSTRING = ''''''
STRING = ''''''


def get_power_level(x, y):
    x +=1
    y+=1
    p1 = ((x + 10) * y + SERIALNUMBER) *(x+10)
    p2 =p1 // 100 % 10

    p3 = p2 -5

    return p3

def build_grid(width,height):
    # n = np.zeros(shape=(width,height))
    # for x in range(width):
    #     for y in range(height):
    #         v = get_power_level(x,y)
    #         n[y,x] = v

    n = np.fromfunction(get_power_level,(300,300),dtype=int)

    return n

def sum_sub_grid(size,grid,width,height):
    max_total=-100000000
    coord=None
    for x in range(width - size +1):
        for y in range(height-size+1):
            sub_grid = grid[y:y+size,x:x+size]
            total = sub_grid.sum()
            if total > max_total:
                max_total = total
                coord = x+1,y+1
    return max_total, coord[::-1]


def run1():
    width = 300
    height = 300
    grid = build_grid(width,height)

    return sum_sub_grid(3,grid,width,height)


def run2():
    # return 3
    width = 300
    height = 300
    grid = build_grid(width,height)
    max_total=0
    max_coord= (0,0)
    for s in range(2,297):
        total, coord = sum_sub_grid(s,grid,width,height)

        if total > max_total:
            max_total = total
            max_coord= coord
            best_s = s
        if total < 0:
            break
    return max_total,max_coord, best_s


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
