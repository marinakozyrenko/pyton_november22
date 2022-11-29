
# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('введите число N:\n'))
new_list = []
prev_list = 1
for i in range(1, number + 1):
    new_list.append((prev_list)*i)
    prev_list = prev_list*i
print('При N =', number, 'получается список', new_list)