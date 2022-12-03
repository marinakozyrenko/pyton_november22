# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring

def fibbonacci_positive(num):
    """
    функция находит положит.значения списка Фибоначчи
    
    args:
        num - длина списка Фибоначчи

    return: 
        список Фибоначчи
    """ 
    if num in [1,2]:
        return 1
    else:
        return fibbonacci_positive(num-1) + fibbonacci_positive(num-2)


def fibbonacci_negative(num):
    """
    функция находит отрицат.значения списка Фибоначчи
    
    args:
        num - длина списка Фибоначчи

    return: 
        список Фибоначчи
    """ 
    if num == 1:
        return 1
    elif num == 2:
        return -1
    else:
        num1,num2 = 1, -1
    for elements in range(2, num):
        num1,num2 = num2, num1-num2
    return num2

def add_two_fibbonacci(num):
    """
    функция склеивает два списка Фибоначчи
    
    args:
        num - длина списка Фибоначчи

    return: 
        положит.+отрицат. списки Фибоначчи
    """ 
    result = []
    result.append(0)
    for i in range(1, num+1):
        result.append(fibbonacci_positive(i))
        result.insert(0, fibbonacci_negative(i))
    return result
    
number = int(input('введите длину списка:\n'))
print(add_two_fibbonacci(number))