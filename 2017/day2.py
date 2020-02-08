import time
from utils import open_file
day = 2
year = 2017

TESTSTRING = ''''''
STRING = open_file(day,year)


def parse_table(table):
    new_table = []
    for t in table:
        t= t.split('\t')
        new_table.append([int(i) for i in t])
    return new_table

def run1():
    sheet = parse_table(STRING)
    checksum = 0
    for row in sheet:
        checksum+= max(row) - min(row)
    return checksum

def run2():
    sheet = parse_table(STRING)
    checksum = 0
    for row in sheet:
        row.sort()
        for i in row:
            for j in row:
                if i == j:
                    continue
                if i % j == 0:
                    checksum += i / j
    return checksum


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
