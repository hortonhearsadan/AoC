import time
from collections import Counter

from utils import open_file, increment_bounded

day = 0
year = 0

TESTSTRING = ''''''
STRING = ''''''


def check(check_sum, code):
    code_set = set(code)
    sum_set = set(check_sum)
    if not code_set & sum_set == sum_set:
        return False

    sort = [item for items, c in Counter(sorted(code)).most_common()
              for item in [items]]
    checked_code = ''.join(sort[:5])
    # sort=sorted(sorted(code),key=lambda x: -code.count(x))
    # checked_code = ''
    # for x in sort:
    #     if not x in checked_code:
    #         checked_code += x
    #         if len(checked_code) == 5:
    #             break
    return checked_code == check_sum


def run1():
    string = open_file(4, 2016)
    real_sectors=[]
    for s in string:
        s = s.replace(']\n', '').replace('[', '-').split('-')
        check_sum = s[-1]
        sector_code = int(s[-2])
        code = ''.join(s[:-2])
        if check(check_sum, code):
            real_sectors.append(sector_code)

    return sum(real_sectors)

def run2():
    string = open_file(4, 2016)
    rooms = []
    for t in string:
        s = t.replace(']\n', '').replace('[', '-').split('-')
        check_sum = s[-1]
        sector_code = int(s[-2])
        code = ' '.join(s[:-2])
        # if check(check_sum, code):
        rooms.append((code,sector_code))

    decryptions = []
    for room, rotation in rooms:
        decrypt = []
        for word in room.split(' '):
            w = ''.join(increment_bounded(x,rotation) for x in word)
            decrypt.append(w)
        if 'northpole' in decrypt:
            return rotation

if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
