import json
import re
from functools import reduce


def split_string(string: str, sep):
    return string.split(sep)

def prod(iterable):
    return reduce(lambda x, y: x*y, iterable)

def remove_character(string: str, char):
    return string.replace(char, '')


def remove_excess_and_filter_none(string: str, regs):
    return list(filter(None, re.split(regs, string)))


def get_adjacent(x):
    return {x + 1, x - 1, x + 1j, x - 1j}


def get_adjacent_with_diag(x):
    return {x + 1, x - 1, x + 1j, x - 1j, x + 1 + 1j, x + 1 - 1j, x - 1 - 1j, x - 1 + 1j}


def get_2_adjacent(x):
    return {(x + 1, x + 2), (x - 2, x - 1), (x + 2j, x + 1j), (x - 1j, x - 2j)}


def open_file(day, year):
    with open(f'../inputs/input{day}{year}') as f:
        string = f.readlines()
    if len(string) == 1:
        return string[0]
    else:
        return string


def open_file_json(day, year):
    with open(f'../inputs/input{day}{year}') as f:
        data = json.load(f)
    return data


def has_double_letter(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def increment(s, n):
    return chr(ord(s) + n)


def increment_bounded(s, n):
    return chr(97 + ((ord(s) % 96) + n - 1) % 26)


def get_group_size(packages, target):
    j = 0
    t = 0
    for i in packages:
        j += 1
        t += i
        if t >= target:
            return j
