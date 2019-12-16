
import time
import numpy as np


def has_consecutive(number):
    for x in range(10):
        str_x = str(x)
        if str_x + str_x in number and not str_x + str_x + str_x in number:
            return True
    return False


def doesnt_decrease(number):
    return list(number) == sorted(number)


def filter_numbers(start,end):
    valid_numbers =0
    for number in range(start,end):

        if has_consecutive(str(number)) and doesnt_decrease(str(number)):
            valid_numbers+= 1

    print(valid_numbers)

# print(has_consecutive(str('112233')))
# print(has_consecutive(str('1233345')))
# print(has_consecutive(str('111122')))

# filter_numbers(['111111'])
# filter_numbers(['223450'])
# filter_numbers(['123789'])
# numbers = [str(x) for x in range(273025, 767253 + 1)]
a = time.time()
# filter_numbers(273025, 767253 + 1)



# passwords_1 = { i for i in range(273025, 767253 + 1)
#                 if (list(str(i)) == sorted(str(i))
#                     and np.any(np.bincount(list(map(int, list(str(i))))) >= 2) == True) }
#
passwords_2 = { i for i in range(273025, 767253 + 1)
                if (list(str(i)) == sorted(str(i))
                    and np.any(np.bincount(list(map(int, list(str(i))))) == 2) == True) }

# print(len(passwords_1)) # part one
print(len(passwords_2)) # part two

print(time.time()-a)
