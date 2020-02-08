import time
from utils import open_file

day = 10
year = 2016

TESTSTRING = ''''''
STRING = open_file(day, year)


class Bot:
    def __init__(self, id, low, high):
        self._id = id
        self.low = low
        self.high = high
        self.chips = []


def parse_instructions(instructions):
    bots = {}
    values = {}
    for i in instructions:
        i = i.strip().split(' ')
        if i[0] == 'bot':
            bots[int(i[1])] = Bot(int(i[1]), (i[5], int(i[6])), (i[10], int(i[11])))
        elif i[0] == 'value':
            values[int(i[1])] = int(i[5])
    return bots, values


def run1():
    bots, values = parse_instructions(STRING)
    targets = [61,17]
    for t in targets:
        initial_bot = values[t]
        bot = bots[initial_bot]


def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
