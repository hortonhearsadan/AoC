import re
import time
from utils import open_file, remove_excess_and_filter_none

day = 2
year = 2020

TESTSTRING = """"""
STRING = """"""


class PolicyPW:
    def __init__(self, least, most, letter, pw):
        self.least = least
        self.most = most
        self.letter = letter
        self.pw = pw

    def is_valid_1(self):
        return self.least <= self.pw.count(self.letter) <= self.most

    def is_valid_2(self):
        return (self.pw[self.least - 1] + self.pw[self.most - 1]).count(self.letter) == 1


def parse_input():
    input = open_file(day, year)
    ppw = []
    for i in input:
        s = i.split(":")
        pw = s[1].replace("\n", "").replace(" ", "")
        t = s[0].split(" ")
        letter = t[1]
        least, most = t[0].split("-")

        #cleaner but slower

        # m=remove_excess_and_filter_none(i,', |_|-|:| |\n')
        # least, most, letter, pw = m

        #cleaner but slower again
        # m = re.match(r'(?P<least>.*)-(?P<most>.*) (?P<letter>.*): (?P<pw>[a-z]*)',i)
        # least = int(m.group('least'))
        # most = int(m.group('most'))
        # letter = m.group('letter')
        # pw = m.group('pw')

        ppw.append(PolicyPW(int(least), int(most), letter, pw))
    return ppw


def run1(inputs):
    return sum(p.is_valid_1() for p in inputs)


def run2(inputs):
    return sum(p.is_valid_2() for p in inputs)


if __name__ == "__main__":
    a = time.time()
    input = parse_input()
    f = run1(input)
    g = run2(input)
    print(f"Runtime: {time.time() - a}")
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
