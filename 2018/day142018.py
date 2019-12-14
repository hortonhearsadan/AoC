import string

import numpy as np
import time


def new_recipes(a, b):
    return [int(i) for i in str(a + b)]


q = time.time()
a = 3
b = 7
i_a = 0
i_b = 1
recipe_list = [a, b]
sub_list = [2, 9, 3, 8, 0, 1]
found = False
while not found:
    recipes = new_recipes(a, b)
    recipe_list += recipes
    i_a = (i_a + 1 + a) % len(recipe_list)
    i_b = (i_b + 1 + b) % len(recipe_list)
    a = recipe_list[i_a]
    b = recipe_list[i_b]
    if len(recipe_list) > 10:
        if recipe_list[-6:] == sub_list:
            found = True
            idx = len(recipe_list) - 6
            break
        if recipe_list[-7:-1] == sub_list:
            found = True
            idx = len(recipe_list) - 7
            break
# last_recipes = recipe_list[-10:]
# print(last_recipes)
# last_recipes_string = [str(i) for i in last_recipes]
# digits = int(''.join(last_recipes_string))
# print(digits)
#
print(idx, time.time() - q)
# print(idx)
# print(s[idx:idx + 7])
# print(recipe_list[idx/4:idx/4 +10])
