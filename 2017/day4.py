import time
from utils import open_file
day = 4
year = 2017

TESTSTRING = ''''''
STRING = open_file(day,year)

def run1():
    count= 0
    for line in STRING:
        line = line.strip().split(' ')
        if len(set(line)) == len(line):
            count+=1
    return count

def run2():
    count = 0
    for line in STRING:
        line = line.strip().split(' ')
        line = [''.join(sorted(l)) for l in line]

        if len(set(line)) == len(line):
            count += 1
    return count


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
