import time
from utils import open_file

day = 0
year = 0

TESTSTRING = ''''''
STRING = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''


class Sue:
    def __init__(self, _id):
        self.id = _id
        self.children = None
        self.cats = None
        self.samoyeds = None
        self.pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.perfumes = None


def get_sues(string):
    sues = {}
    for s in string:
        s = list(filter(None, s.replace(',', '').replace(':', '').split(' ')))
        i = int(s[1])
        sue = Sue(i)
        for j in range(2, len(s) - 1, 2):
            setattr(sue, s[j], int(s[j + 1]))
        sues[i] = sue

    return sues


def parse_attributes(string):
    attr = {}
    string = string.replace(':', '')
    string = string.split('\n')
    for s in string:
        name, value = s.split(' ')
        attr[name] = int(value)
    return attr


def run1():
    string = open_file(16, 2015)
    sue_dict = get_sues(string)
    sues = set(sue_dict.values())
    attributes = parse_attributes(STRING)
    sue_ids = {k for k in sue_dict.keys()}
    for a, v in attributes.items():
        sue_ids -= {s.id for s in sues if getattr(s, a) not in {None, v}}
    return list(sue_ids)[0]


def run2():
    string = open_file(16, 2015)
    sue_dict = get_sues(string)
    sues = set(sue_dict.values())
    attributes = parse_attributes(STRING)
    sue_ids = {k for k in sue_dict.keys()}
    gt = {'cats', 'trees'}
    lt = {'pomeranians', 'goldfish'}
    for a, v in attributes.items():
        if a in gt:
            sue_ids -= {s.id for s in sues if getattr(s, a) is not None and getattr(s, a) <= v}
        elif a in lt:
            sue_ids -= {s.id for s in sues if getattr(s, a) is not None and getattr(s, a) >= v}
        else:
            sue_ids -= {s.id for s in sues if getattr(s, a) not in {None, v}}
    return list(sue_ids)[0]


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
