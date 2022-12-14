# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

def create_random_list(num):
    """
    ф-я создает список рандомным путем длиной, которую задает пользователь
    arg: num - длина списка, которую вводит польз-ль
    return: list - сформированный список
    
    """
    new_list = []
    for number in range(num):
        new_list.append(random.randint(0,9))
    return new_list

def multiply_pairs(first_list):
    """
    ф-ция умножает пары в списке след.образом - 1-ый с последним, 2-ой с предпосл. и т.д.
    arg: first_list - список, сформиро-ый рандомным путем
    return: новый список, состоящий из произведений элементов

    """
    result = [first_list[i]*first_list[-1-i] for i in range(len(first_list)//2 + len(first_list)%2)]
    return result

amount_of_elements = int(input('введите число элементов в списке:\n'))
our_list = create_random_list(amount_of_elements)
print(our_list)
list_of_multyply_pairs = multiply_pairs(our_list)
print(list_of_multyply_pairs)
