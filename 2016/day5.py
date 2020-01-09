import string
import time
from utils import open_file
import hashlib

day = 0
year = 0

TESTSTRING = ''''''
STRING = '''reyedfim'''


def run1():
    i = 0
    pwd = []
    while len(pwd) < 8:
        s = STRING + str(i)
        h = hashlib.md5(s.encode()).hexdigest()
        if h.startswith('00000'):
            pwd.append(h[5])
        i += 1
    return ''.join(pwd)


def run2():
    i = 0
    pwd = ['_'] * 8
    rep = set()
    while len(rep) < 8:
        i += 1
        s = STRING + str(i)
        h = hashlib.md5(s.encode()).hexdigest()
        if h.startswith('00000'):
            pos = int(h[5],16)
            if pos > 7 or pos in rep:
                continue
            pwd[pos] = h[6]
            print(''.join(pwd))
            rep.add(pos)

    return ''.join(pwd)


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
