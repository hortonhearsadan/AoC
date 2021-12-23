import time
from collections import defaultdict
from copy import copy

dir_path = __file__.split("/")
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""
STRING = """#############
#...........#
###A#D#A#C###
  #C#D#B#B#
  #########"""

A = "A"
B = "B"
C = "C"
D = "D"

# BOARD1 = [
#     (0, 0),
#     (1, 0),
#     (2, 0),
#     (3, 0),
#     (4, 0),
#     (5, 0),
#     (6, 0),
#     (7, 0),
#     (8, 0),
#     (9, 0),
#     (10, 0),
#     (2, 1),
#     (2, 2),
#     (4, 1),
#     (4, 2),
#     (6, 1),
#     (6, 2),
#     (8, 1),
#     (8, 2),
# ]

PIECES1 = [(A, 1), (A, 2), (B, 1), (B, 2), (C, 1), (C, 2), (D, 1), (D, 2)]
FINISHED = {A: 2, B: 4, C: 6, D: 8}
COSTS = {A: 1, B: 10, C: 100, D: 1000}
ROOM_ENTRACES = [(2, 0), (4, 0), (6, 0), (8, 0)]
ROOM_CAPACITY = 2


def parse_input():
    # f = open_file(day,year)
    f = TESTSTRING.split("\n")
    starting_positions = {}

    for j in range(ROOM_CAPACITY):

        for i, c in enumerate(f[2 + j]):
            if c in ("#", " "):
                continue
            else:
                for k in range(1, ROOM_CAPACITY + 1):
                    if (c, k) in starting_positions.keys():
                        continue
                    else:
                        starting_positions[(c, k)] = (i - 1, j + 1)
                        break

    return starting_positions


def is_piece_in_room(k, v):
    return v[1] in (1, 2)


def get_non_blocked_hallway(k, v, positions):
    if v[1] == 2 and (v[0], 1) in positions.values():
        return []
    left = []
    for i in range(v[0], -1, -1):
        p = (i, 0)
        if p in positions.values():
            break
        if p in ROOM_ENTRACES:
            continue
        left.append(p)

    right = []
    for r in range(v[0], 11, 1):
        p = (r, 0)
        if p in positions.values():
            break
        if p in ROOM_ENTRACES:
            continue
        right.append(p)
    return left + right


def get_correct_room(k, v, positions):
    room = FINISHED[k[0]]
    rooms = [(room, i) for i in range(1, ROOM_CAPACITY + 1)]
    pieces_using_rooms = [k for k, v1 in positions.items() if v1 in rooms]
    if any(j[0] != k[0] for j in pieces_using_rooms):
        return []
    path = (
        [(v[0], i) for i in range(v[1] - 1, -1, -1)]
        + [(j, 0) for j in range(v[0], room, 1 if v[0] < room else -1)]
        + [(room, i) for i in range(0, 2)]
    )
    if any(v in path for k1, v in positions.items() if k1 != k):
        return []
    return [r for r in rooms if r not in positions.values()]


def is_piece_in_corridor(k, v):
    return v[1] == 0


def get_valid_moves(positions):
    moves = defaultdict(list)
    for k, v in positions.items():
        m = []
        if is_piece_finished(k, v, positions):
            continue
        elif is_piece_in_room(k, v):
            m.extend(
                get_non_blocked_hallway(k, v, positions)
                + get_correct_room(k, v, positions)
            )
        elif is_piece_in_corridor(k, v):
            m.extend(get_correct_room(k, v, positions))

        if m:
            moves[k].extend(m)
    return moves


def run1(positions):
    all_valid_moves = get_valid_moves(positions)
    turns = 0
    completions = []
    completed_costs = []
    costs = 0
    for k, moves in all_valid_moves.items():
        print(f"starting node: {k}")
        for m in moves:
            new_positions = copy(positions)
            new_positions[k] = m
            new_costs = copy(costs)
            # new_costs.append(move_cost(k,m,positions[k]))
            new_costs += move_cost(k, m, positions[k])
            new_turns = copy(turns)
            new_turns += 1
            # new_turns.append((k,positions[k],m))
            go(new_positions, new_turns, new_costs, completions, completed_costs)

    print(len(completions))
    print(min(completed_costs))


def get_best_valid_moves(all_valid_moves):
    best_moves = {
        k: [move for move in moves if move[1] > 0]
        for k, moves in all_valid_moves.items()
    }
    if any(v for v in best_moves.values()):
        for k, v in best_moves.items():
            if not v:
                continue
            best_moves[k] = sorted([m for m in v], key=lambda x: -x[1])[:1]
        return best_moves
    else:
        return all_valid_moves


def go(positions, turns, costs, completions, completed_costs):
    if completions and costs >= min(completed_costs):
        # print(turns)
        return
    if is_finished(positions):
        completions.append(turns)
        # completed_costs.append(sum(costs))
        completed_costs.append(costs)
        print(turns)
        print(min(completed_costs))
        return

    all_valid_moves = get_valid_moves(positions)

    next_moves = get_best_valid_moves(all_valid_moves)
    for k, moves in next_moves.items():
        for m in moves:
            new_positions = copy(positions)
            new_positions[k] = m
            new_costs = copy(costs)
            # new_costs.append(move_cost(k,m,positions[k]))
            # new_costs = copy(costs)
            new_costs += move_cost(k, m, positions[k])
            new_turns = copy(turns)
            new_turns += 1
            # new_turns.append((k,positions[k],m))
            go(new_positions, new_turns, new_costs, completions, completed_costs)


def is_finished(positions):
    for k, v in positions.items():
        if not is_piece_finished(k, v, positions):
            return False

    return True


def is_piece_finished(piece, position, positions):
    if FINISHED[piece[0]] != position[0]:
        return False
    if position[1] == 2:
        return True

    p = (position[0], 2)
    ks = [k for k, v in positions.items() if v == p]
    if not ks:
        return False
    elif ks[0][0] == piece[0]:
        return True
    return False


def run2(data):
    pass


def move_cost(k, v1, v2):
    return (abs(v1[0] - v2[0]) + abs(v1[1] - 0) + abs(v2[1] - 0)) * COSTS[k[0]]


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
