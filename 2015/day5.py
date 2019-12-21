import time
from utils import open_file

day = 5
year = 2015

TESTSTRING = '''qjhvhtzxzqqjkmpb'''
T = '''xxyxx'''
TESTSTRING2 = '''uurcxstgmygtbstg'''
TESTSTRING3 = '''ieodomkazucvgmuy'''
TESTSTRING4 = '''dvszwmarrgswjxmb'''

STRING = ''''''

bad_strings = {'ab', 'cd', 'pq', 'xy'}
vowels = {'a', 'e', 'i', 'o', 'u'}


def has_badstrings(s):
    for b in bad_strings:
        if b in s:
            return True
    return False


def has_double_letter(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def has_vowels(num, s):
    count = 0
    for t in s:
        if t in vowels:
            count += 1
    return count >= 3


def has_sandwich(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False


def is_string_nice(s):
    return not has_badstrings(s) and has_double_letter(s) and has_vowels(3, s)


def has_pair_repetition(s):
    for i in range(len(s) - 1):
        pair = s[i:i + 2]
        sliced_s = s[i + 2:]
        if pair in sliced_s:
            return True
    return False


def is_string_nice_new(s):
    return has_sandwich(s) and has_pair_repetition(s)


def run1():
    strings = open_file(day, year)
    nices = 0
    for s in strings:
        nice = is_string_nice(s)
        if nice:
            nices += 1
    return nices


def run2():
    strings = open_file(day, year)

    nices = 0
    for s in strings:
        s = s.replace('\n', '')
        nice = is_string_nice_new(s)
        print(s, nice)
        if nice:
            nices += 1
    return nices


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
