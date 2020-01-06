import time
from utils import open_file
import string
day = 0
year = 0

TESTSTRING = ''''''
STRING = '''""
"abc"
"aaa\"aaa"
"\x27"'''

def run1():
    strings = open_file(8,2015)
    strings = STRING
    for s in strings.split('\n'):
        p=-2
        s = s.replace('\n','')
        chars = len(s)
        for i in s:
            if i in string.punctuation:
                p +=1
        chars+=p

        length=chars - 2 - p
        pass


def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
