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


def open_file(day,year):
    with open(f'../inputs/input{day}{year}') as f:
        string = f.readlines()
    if len(string) == 1:
        return string[0]
    else:
        return string