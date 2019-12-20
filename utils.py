import re


def split_string(string: str, sep):
    return string.split(sep)


def remove_character(string: str, char):
    return string.replace(char, '')


def remove_excess_and_filter_none(string: str, regs):
    return filter(None, re.split(regs, string))


def get_adjacent(x):
    return {x + 1, x - 1, x + 1j, x - 1j}


def get_2_adjacent(x):
    return {(x + 1, x + 2), (x - 2, x - 1), (x + 2j, x + 1j), (x - 1j, x - 2j)}
