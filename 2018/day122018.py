import time
from enum import Enum

from utils import open_file
INIT= '#....##.#.#.####..#.######..##.#.########..#...##...##...##.#.#...######.###....#...##..#.#....##.##'
COMBS= '''.#.## => #
.#.#. => #
#.#.# => .
.#### => .
.#... => .
#..## => .
..#.# => #
#.#.. => .
##### => .
....# => .
...## => .
..##. => .
##.#. => #
##..# => .
##... => #
..### => #
.##.. => #
###.. => .
#..#. => .
##.## => .
..#.. => #
.##.# => #
####. => #
#.### => .
#...# => #
###.# => #
...#. => #
.###. => .
.#..# => #
..... => .
#.... => .
#.##. => #'''

class Status(Enum):
    Plant="#"
    NoPlant="."

def get_pot_recipes():
    recipes=[]
    for x in COMBS.split('\n'):
        recipe, result = x.split('=>')
        recipe = recipe.strip()
        result = result.strip()
        if result== Status.Plant.value:
            recipes.append(recipe)

    return set(recipes)


def run1():
    pot_recipes = get_pot_recipes()
    active_state = '.'*50+INIT+'.'*50
    for i in range(20):
        next_state = ['.']*(len(active_state))
        for x in range(len(active_state)-4):
            s = active_state[x:x+5]
            centre =x+2
            if s in pot_recipes:
                next_state[centre] = Status.Plant.value

        active_state = ''.join(next_state)

    total = 0
    for i, x in enumerate(active_state):
        if x == Status.Plant.value:
            total+=(i - 50)
    return total

def run2():
    pot_recipes = get_pot_recipes()
    active_state = '.'*5000+INIT+'.'*5000
    base = active_state
    t=0
    while t==0 or base != active_state:
        next_state = ['.']*(len(active_state))
        for x in range(len(active_state)-4):
            s = active_state[x:x+5]
            centre =x+2
            if s in pot_recipes:
                next_state[centre] = Status.Plant.value

        active_state = ''.join(next_state)
        t+=1
        if t %1000 == 0:
            print(t)

    cycle = t
    cycles_left = 50000000000 %t
    print(cycles_left)
    total = 0
    for i, x in enumerate(active_state):
        if x == Status.Plant.value:
            total+=(i - 50)
    return total



if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
