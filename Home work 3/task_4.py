# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def decimal_to_binary(num):
    """
    функция перевода 10-тичного числа в 2-чное при помощи рекурсивного метода

    Args:
        num - вводимое число для преобразования
    Return: 
        строка с двоичным числом
    """ 
    if num > 1:
        decimal_to_binary(num//2)
    print(num % 2, end = '')


user_input = int(input("Введите число:"))
decimal_to_binary(user_input)

