import time
from utils import *

STRING = '''3113322113'''

TEST_STRING = '''1'''
TEST_STRING2 = '''11'''
TEST_STRING3 = '''111221'''
TEST_STRING4 = '''1211'''


def run1():
    string = STRING

    for j in range(40):
        new_string = ''
        i=0
        while i <= len(string) -1:
            num = string[i]
            count = 1
            if i == len(string)-1:
                new_string += str(count) + str(num)
                break
            while string[i + count] == num:

                count +=1
                if i + count >= len(string) - 1:
                    break
            new_string += str(count) + str(num)

            i +=count
        string = new_string
        new_string = ''

    return len(string)




def run2():
    string = STRING

    for j in range(50):
        new_string = ''
        i = 0
        while i <= len(string) - 1:
            num = string[i]
            count = 1
            if i == len(string) - 1:
                new_string += str(count) + str(num)
                break
            while string[i + count] == num:

                count += 1
                if i + count >= len(string) - 1:
                    break
            new_string += str(count) + str(num)

            i += count
        string = new_string
        new_string = ''

    return len(string)


if __name__ == "__main__":
    start_time = time.time()
    f = run1()
    g = run2()
    print(f"Part 1:", f)
    print(f"Part2:", g)
    print(time.time() - start_time)
