import time
from utils import open_file

day = 0
year = 0

TESTSTRING = """"""
STRING = """"""


class Seat:
    def __init__(self, code):
        self.row = code[:7]
        self.column = code[7:]

    def parse_row(self):
        return "".join([str(int(i == "B")) for i in self.row])

    def parse_column(self):
        return "".join([str(int(i == "R")) for i in self.column])

    def get_seat_id(self):
        return self.get_row() * 8 + self.get_column()

    def get_row(self):
        return int(self.parse_row(), 2)

    def get_column(self):
        return int(self.parse_column(), 2)


def parse_input():
    inputs = open_file(5, 2020)
    seats = [Seat(i.strip()) for i in inputs]
    return seats


def run1(seats):
    return [s.get_seat_id() for s in seats]


def run2(ids):
    ids = set(ids)
    free_seats = set(range(15, 1017)) - ids
    return next(s for s in free_seats if (s + 1 in ids and s - 1 in ids))


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(f)

    print(f"Part 1: {max(f)}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
