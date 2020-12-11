import time
from utils import open_file
import numpy as np

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
STRING = """"""


def parse_input():
    f = open_file(day, year)
    # f = TESTSTRING.split('\n')
    matrix = np.array([list(s.strip()) for s in f])
    return matrix


def run1(plan):
    plan = np.pad(plan, [(1, 1), (1, 1)], "constant", constant_values=".")
    while True:
        next_plan_full = []
        next_plan_free = []

        for row_idx, row in enumerate(plan[1:-1], 1):
                for col_idx, seat in enumerate(row[1:-1], 1):
                    if seat == '.':
                        continue
                    adj = plan[row_idx - 1 : row_idx + 2, col_idx - 1 : col_idx + 2]
                    occupied = np.count_nonzero(adj == "#")

                    if seat == "L":
                        if occupied == 0:
                            next_plan_full.append((row_idx,col_idx))

                    elif seat == "#":
                        if occupied >= 5:
                            next_plan_free.append((row_idx,col_idx))

        if next_plan_free or next_plan_full:
            for y,x in next_plan_free:
                plan[y,x] = 'L'
            for y, x in next_plan_full:
                plan[y,x] = '#'

        else:
            return np.count_nonzero(plan == "#")


def count_occupied(plan,row,col):
    h,w= plan.shape
    left = plan[row,:col][::-1]
    right = plan[row,col+1:]
    up = plan[:row,col][::-1]
    down = plan[row+1:,col]
    count = 0

    for i in range(1,min(row,col)+1):
        x = plan[row-i,col-i]
        if x=='.':
            continue
        elif x =='#':
            count+=1
            break
        else:
            break

    for i in range(1,min(h-row,w-col)):
        x = plan[row+i,col+i]
        if x=='.':
            continue
        elif x =='#':
            count+=1
            break
        else:
            break

    for i in range(1,min(h-row,col)):
        x=plan[row+i,col-i]
        if x=='.':
            continue
        elif x =='#':
            count+=1
            break
        else:
            break

    for i in range(1,min(row,w-col)):
        x=plan[row-i,col+i]
        if x=='.':
            continue
        elif x =='#':
            count+=1
            break
        else:
            break

# lu = [plan[row-i,col-i] for i in range(1,min(row,col)+1)]
    # rd = [plan[row+i,col+i] for i in range(1,min(h-row,w-col))]
    # ld = [plan[row+i,col-i] for i in range(1,min(h-row,col))]
    # ru = [plan[row-i,col+i] for i in range(1,min(row,w-col))]

    for sight in [left,right,up,down]:
        for seat in sight:
            if seat =='.':
                continue
            elif seat =='#':
                count +=1
                break
            else:
                break
    return count


def run2(plan):
    plan = np.pad(plan, [(1, 1), (1, 1)], "constant", constant_values=".")
    while True:
        next_plan_full = []
        next_plan_free = []

        for row_idx, row in enumerate(plan[1:-1], 1):
                for col_idx, seat in enumerate(row[1:-1], 1):
                    if seat == '.':
                        continue
                    occupied = count_occupied(plan,row_idx,col_idx)

                    if seat == "L":
                        if occupied == 0:
                            next_plan_full.append((row_idx,col_idx))

                    elif seat == "#":
                        if occupied >= 5:
                            next_plan_free.append((row_idx,col_idx))

        if next_plan_free or next_plan_full:
            for y,x in next_plan_free:
                plan[y,x] = 'L'
            for y, x in next_plan_full:
                plan[y,x] = '#'

        else:
            return np.count_nonzero(plan == "#")




if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
