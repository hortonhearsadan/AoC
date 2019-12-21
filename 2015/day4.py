import time
import hashlib

from utils import open_file
day = 4
year = 2015

TESTSTRING = '''pqrstuv'''
STRING = '''yzbqklnj'''

def run1():
    key = STRING
    x=0
    while True:
        m = hashlib.md5(bytes(key+str(x),encoding='UTF-8'))
        b=m.hexdigest()
        if b[:5] == '00000':
            return x
        x+=1


def run2():
    key = STRING
    x = 0
    while True:
        m = hashlib.md5(bytes(key + str(x), encoding='UTF-8'))
        b = m.hexdigest()
        if b[:6] == '000000':
            return x
        x += 1


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
