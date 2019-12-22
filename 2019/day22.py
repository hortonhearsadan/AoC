import time

from numpy.testing import assert_array_equal

from utils import open_file
import numpy as np
from unittest import TestCase

day = 22
year = 2019

TESTSTRING = '''deal with increment 7
deal into new stack
deal into new stack'''
TESTSTRING2 = '''deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1'''


def deal_new(deck):
    return deck[::-1]


def cut_deck(deck, cards):
    return np.roll(deck, -cards)


def increment_n(deck, inc):
    l = len(deck)
    columns, spill = divmod(l, inc)
    tmp_deck = np.zeros(l, dtype=int)
    for i in range(l):
        tmp_deck[(i * inc) % l] = deck[i]
    return tmp_deck


class Shuffle:
    def __init__(self, action, cards=0):
        self.action = action
        self.cards = int(cards)


def get_instructions(string):
    i = []
    for s in string:
        s = list(
            filter(None, s.replace('deal', '').replace('\n', '').replace('with', '').replace('into', '').replace('new',
                                                                                                                 '').split(
                ' ')))
        i.append(Shuffle(*s))
    return i


def run1():
    string = open_file(day, year)
    instructions = get_instructions(string)

    deck = np.arange(10007)
    for i in instructions:
        if i.action == 'increment':
            deck = increment_n(deck, i.cards)
        elif i.action == 'cut':
            deck = cut_deck(deck, i.cards)
        elif i.action == 'stack':
            deck = deal_new(deck)

    return np.where(deck == 2019)[0][0]


def run2():
    string = open_file(day, year)
    instructions = get_instructions(string)

    deck_size = 119315717514047
    repeats = 101741582076661

    p = 0
    # for j in range(repeats):
    #     for i in instructions:
    #         if i.action == 'increment':
    #             p = (p * i.cards) % deck_size
    #         elif i.action == 'cut':
    #             p = (p - i.cards) % deck_size
    #         elif i.action == 'stack':
    #             p = (deck_size - p) % deck_size

    return p


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)

# class DeckTest(TestCase):
#     def test_deal_new(self):
#         deck = np.arange(10)
#         new_deck = deal_new(deck)
#         expected = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
#         self.assertTrue(np.allclose(expected, new_deck))
#
#     def test_cut_deck_forwards(self):
#         deck = np.arange(10)
#         new_deck = cut_deck(deck, 3)
#         expected = np.array([3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
#         self.assertTrue(np.allclose(expected, new_deck))
#
#     def test_cut_deck_backwards(self):
#         deck = np.arange(10)
#         new_deck = cut_deck(deck, -4)
#         expected = np.array([6, 7, 8, 9, 0, 1, 2, 3, 4, 5])
#         self.assertTrue(np.allclose(expected, new_deck))
#
#     def test_increment_n(self):
#         deck = np.arange(10)
#         new_deck = increment_n(deck,3)
#         expected = np.array([0, 7, 4, 1, 8, 5, 2, 9, 6, 3,])
#         self.assertTrue(np.allclose(expected, new_deck))
