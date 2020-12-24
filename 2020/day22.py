import time
from collections import deque
from itertools import islice

from utils import open_file
import numpy as np
import networkx as nx
import scipy as sp

dir_path = __file__.split('/')
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''
STRING = ''''''

def parse_input():
    with open(f"../inputs/input{day}{year}") as f:
        strings = f.read()
        # strings = TESTSTRING
    player1,player2 = strings.split('\n\n')
    player1 = player1.strip().split('\n')[1:]
    player2 = player2.strip().split('\n')[1:]

    player1 = deque(int(p1) for p1 in player1)
    player2 = deque(int(p2) for p2 in player2)
    return player1,player2

def draw(player1,player2):
    p1 = player1.popleft()
    p2 = player2.popleft()
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)


def run1(player1,player2):
    while player1 and player2:
        draw(player1,player2)
    scores = player1+ player2
    score = sum(i*s for i,s in enumerate(reversed(scores),1))
    return score


def run2(player1, player2):
    deck_tracker_p1 = set()
    deck_tracker_p2 = set()
    while player1 and player2:
        q1 = False
        q2 = False

        if tuple(player1) in deck_tracker_p1 and tuple(player2) in deck_tracker_p2:
            return player1, None
        deck_tracker_p1.add(tuple(player1))
        deck_tracker_p2.add(tuple(player2))

        p1 = player1.popleft()
        p2 = player2.popleft()

        if p1 <= len(player1) and p2 <= len(player2):
            s1, s2 = deque(islice(player1, 0, p1)), deque(islice(player2, 0, p2))
            if max(s1) > max(s2):
                q1 = True
            else:
                q1, q2 = run2(s1, s2)
                if q2 is None:
                    q1 = True
        else:
            q1 = p1 > p2
            q2 = p1 < p2

        if q1:
            player1.append(p1)
            player1.append(p2)
        elif q2:
            player2.append(p2)
            player2.append(p1)
    return player1, player2

if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    deck1,deck2 = inputs
    f = run1(deck1.copy(),deck2.copy())
    g,h = run2(deck1.copy(),deck2.copy())
    scores = g+ h
    score = sum(i*s for i,s in enumerate(reversed(scores),1))


    print(f"Part 1: {f}")
    print(f"Part 2: {score}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
