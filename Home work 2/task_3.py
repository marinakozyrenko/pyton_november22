# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random 

n = int(input('введите число N:\n'))
new_list = []

for i in range(n):
    new_list.append(random.randint(-100,100)) 
print(new_list)
for m, item in enumerate(new_list):
    if item < 0:
        new_list.insert(m+ 1, 0)
print(new_list)



