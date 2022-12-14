# 5 - Есть список случайных чисел в промежутке от 1 до 200, количеством 200. Создайте список кортежей, 
# первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

import random
from random import randint

rand_list = list(map(lambda x: random.randint(1,201), range(200)))
print(rand_list)

cort_list = [(index,element) for index,element in enumerate(rand_list) if index!=element]
print(cort_list)