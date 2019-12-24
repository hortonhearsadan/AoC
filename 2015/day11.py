import string
import time
from unittest import TestCase

from utils import *

STRING = '''hxbxwxba'''

TEST_STRING = '''abcdefgh'''
TEST_STRING2 = '''ghijklmn'''
TEST_STRING3 = ''''''

alphabet = string.ascii_lowercase
chain_of_threes = {''.join(increment(a,n) for n in range(3)) for a in alphabet[:-2]}
banned_letters ={'i','o','l'}

def has_doube_double_letter(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            for j in range(i+2,len(s)-1):
                if s[j] == s[j+1]:
                    return True
            return False
    return False


def has_straight(pwd):
    for i in range(len(pwd)-2):
        if pwd[i:i+3] in chain_of_threes:
            return True
    return False


def has_banned_letters(pwd):
    for b in banned_letters:
        if b in pwd:
            return True
    return False


def is_password_valid(pwd):
    return has_straight(pwd) and not has_banned_letters(pwd) and has_doube_double_letter(pwd)


def increment_password(password):
    pwd = list(password)
    for s in range(len(pwd)):
        if pwd[s] in banned_letters:
            pwd[s] = increment(pwd[s],1)
            for t in range(s+1,len(pwd)):
                pwd[t] = 'a'
            return ''.join(p for p in pwd)
    i=1
    while True:
        if pwd[-i] =='z':
            pwd[-i] = 'a'
            i+=1

        else:
            pwd[-i] = increment(pwd[-i],1)
            return ''.join(p for p in pwd)


def run1(pwd=STRING):
    valid = False
    while not valid:
        pwd = increment_password(pwd)
        valid = is_password_valid(pwd)

    return pwd


def run2():
    pass


def test_password_valid():
    pwd= 'hijklmmn'
    pwd1= 'abbceffg'
    pwd2 = 'abbcegjk'
    pwd3='abcdffaa'
    for p in [pwd,pwd1,pwd2,pwd3]:
        a = has_straight(p)
        b = has_banned_letters(p)
        c = has_doube_double_letter(p)
        print(p,a,b,c)
        print(is_password_valid(p))



if __name__ == "__main__":
    # test_password_valid()
    start_time = time.time()
    f = run1()
    g = run1(f)
    print(f"Part 1:", f)
    print(f"Part2:", g)
    print(time.time() - start_time)

