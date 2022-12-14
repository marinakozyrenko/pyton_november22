# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

import random
from random import randint

rand_list = list(map(lambda x: random.randint(10,20), range(10)))
print(rand_list)

def sum_numbers(number:int):  
    """
    функция по нахождению суммы цифр числа
    arg - число
    return - сумма цифр числа

    """
    res = 0
    while (number != 0):
        last_number = number % 10
        res = res + last_number
        number = number // 10 
    return res
    
# с помощью map - применяем функцию суммы цифр числа к рандомному списку и формируем список из этих сумм
new_list = list(map(sum_numbers, rand_list)) 
print(new_list)

def filter_even_num(num): 
    """
    функция-фильт к четным числам
    arg - число (в нашем случае это сумма цифр числа)
    return - true, в случае выполнения условия четности / false - в противном случае

    """
    if(num % 2) == 0:
        return True
    else:
        return False

# с помощью filter - применяем функцию фильтра к списку с суммами цифр и формируем список из четных суммы с помощью filter
even_sum = list(filter(filter_even_num,new_list))
print(even_sum)




