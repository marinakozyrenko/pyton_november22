# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def create_random_list(num):
    """
    функция создает список рандомным путем с элементами от 0 до 9

    arg:
    num - длина списка, которую вводит пользователь

    return:
    list - возвращает список, заполненный рандомным путем

    """

    new_list = []
    for number in range(num):
        new_list.append(random.randint(0,9))
    return new_list

def SumElements(list):
    """
    функция находит сумму элементов на нечетных индексах

    arg:
    list - список, из которого будет произведена выборка

    return:
    сумма элементов списка, стоящих на нечётной позиции

    """
    result = 0
    for i in range(len(list)):
        if i % 2 == 1:
            result += list[i]
    return result

amount_of_elements = int(input('введите число - кол-во элем-ов:\n'))
my_list = create_random_list(amount_of_elements)
print(my_list)
sum_elements = SumElements(my_list)
print(sum_elements)

