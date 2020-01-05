import math
import re
import time
from typing import List

from utils import open_file

day = 0
year = 0

TESTSTRING = ''''''
WEAPONS = '''Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0'''

ARMOR = '''Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5'''

RINGS = '''Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''


class Item:
    def __init__(self, name, cost, damage, armour):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armour = armour


class Character:
    def __init__(self, name: str, hp, damage=0, armor=0):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.damage = damage
        self.equipment = None

    def _equip(self, item: Item):
        self.armor += item.armour
        self.damage += item.damage

    def equip_items(self, items: [Item]):
        for i in items:
            self._equip(i)
        self.equipment = items


def parse_items(string,mandatory = True):
    items = {}
    for s in string.split('\n'):
        s = s.replace(' +', '+')
        s = re.split(' +', s)
        name, cost, damage, armour = s
        items[name] = Item(name, float(cost), float(damage), float(armour))
    if not mandatory:
        items['None'] = Item('None',0,0,0)
    return items


def get_turns_until_dead(attacker: Character, defender: Character):
    damage_per_turn = max(attacker.damage - defender.armor, 1)
    turns = math.ceil(defender.hp / damage_per_turn)
    return turns


def make_chars():
    return Character('you', 100), Character('boss', 100, 8, 2)


def run1():
    weapons = parse_items(WEAPONS)
    armors = parse_items(ARMOR,False)
    rings = parse_items(RINGS,False)
    min_cost = 100000000000
    best_set = None
    for w, weapon in weapons.items():
        for a, armor in armors.items():
            for r1, ring1 in rings.items():
                for r2, ring2 in rings.items():
                    if r2 == r1 and r1 != 'None':
                        continue
                    you, boss = make_chars()
                    equipment = (weapon, armor, ring1, ring2)
                    cost= sum(i.cost for i in equipment)
                    if cost > min_cost:
                        continue
                    you.equip_items(equipment)
                    you_kill_boss = get_turns_until_dead(you, boss)
                    boss_kill_you = get_turns_until_dead(boss, you)
                    if you_kill_boss <= boss_kill_you:
                        min_cost = cost
                        best_set = w, a, r1, r2
    return min_cost, best_set


def run2():
    weapons = parse_items(WEAPONS)
    armors = parse_items(ARMOR, False)
    rings = parse_items(RINGS, False)
    max_cost = 0
    best_set = None
    for w, weapon in weapons.items():
        for a, armor in armors.items():
            for r1, ring1 in rings.items():
                for r2, ring2 in rings.items():
                    if r2 == r1 and r1 != 'None':
                        continue
                    you, boss = make_chars()
                    equipment = (weapon, armor, ring1, ring2)
                    cost = sum(i.cost for i in equipment)
                    if cost < max_cost:
                        continue
                    you.equip_items(equipment)
                    you_kill_boss = get_turns_until_dead(you, boss)
                    boss_kill_you = get_turns_until_dead(boss, you)
                    if you_kill_boss > boss_kill_you:
                        max_cost = cost
                        best_set = w, a, r1, r2
    return max_cost, best_set


if __name__ == "__main__":
    start = time.time()
    f = run1()
    g = run2()
    print(time.time() - start)
    print(f"Part 1", f)
    print(f"Part 2", g)
