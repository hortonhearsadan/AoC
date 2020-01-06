import re
import time
from collections import defaultdict

from utils import open_file
day = 19
year = 2015

TESTSTRING = '''H => HO
H => OH
O => HH'''
STRING = '''HOHOHO'''


def get_replacements(string):

    r = defaultdict(list)
    for s in string:
    # for s in string.split('\n'):
        if '=>' in s:
            s= s.replace('\n','')
            a, b  = s.split(' => ')
            r[a].append(b)
    return r


def run1():
    string = open_file(day,year)
    # string = TESTSTRING
    replacements = get_replacements(string)
    molecule = string[-1]
    # molecule = STRING
    new_strings =set()
    for r, s in replacements.items():
        hits = [m.start() for m in re.finditer(r, molecule)]
        offset = len(r)
        for reps in s:
            for h in hits:
                new_string = molecule[:h]+reps + molecule[h+offset:]
                new_strings.add(new_string)



    return len(new_strings)

def run2():
    string = open_file(day, year)
    # string = TESTSTRING
    replacements = get_replacements(string)
    molecule = string[-1]
    return len(molecule)

if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
