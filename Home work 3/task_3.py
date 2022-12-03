# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91


import random

def create_random_list(num):
    """
    функция по созданию списка рандомным путем

    arg:
    num - длинна списка

    return:
    list - список, сформированный рандомным путем    
    
    """

    result_list = []
    for i in range(num):
        f = random.uniform(0,9)
        fl_part = random.randint(1,3)
        result_list.append(round(f,fl_part))
    return result_list

def float_part(num):
    """
    функция по нахождению дробной части числа

    arg:
    num - элемент списка

    return:
    result - дробная часть, окргленная до 3-х знаков    
    
    """
    result = num - int(num)
    return round(result,3)

def dif_max_min_float(list):
    """
    функция нахождения разницы между максим-ой и миним-ой дробной частью вещественных чисел списка

    arg:
    list - список вещест-х чисел, созданных рандомным путем

    return:
    dif_max_min_float - разницы между максим-ой и миним-ой дробной частью    
    
    """
    min_float = float_part(list[0])
    max_float = float_part(list[0])
    for i in range(len(list)):
        if float_part(list[i]) > max_float:
            max_float = float_part(list[i])
        if float_part(list[i]) < min_float:
            min_float = float_part(list[i])
        result = max_float - min_float
    return round(result,3)

number = int(input('введите число - длину списка:\n'))
my_list = create_random_list(number)
print(my_list)

diff_float = dif_max_min_float(my_list)
print(f'разница = {diff_float}')


