# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def primeNum(num):
    """
    функция, которая составляет список простых множителей заданного числа

    arg - вводимое пользователем натуральное число

    return - список простых множителей
    
    """
    primeList = []
    for i in range (2, num):
        while num % i == 0:
            num = num / i
            primeList.append(i)
    return primeList

num = int(input('введите натуральное число:\n'))
our_List = primeNum(num)
print(f'простые множители числа {num}: {our_List}')

        

