# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random 

welcome_text = ('Хотите сыграть в игру Конфеты?\n'
                'У вас есть 2021 конфета, вы берете их по очереди\n' 
                'За один ход можно взять не более 28 конфет\n'
                'Выигрывает тот, кто последним заберет все конфеты\n')

print(welcome_text)

def player_vs_player():
    sweets_total = 43
    max_take = 28
    count = 0
    
    player_1 = input('Введите Ваше имя: ')
    player_2 = input('Как зовут Вашего противника: ')
    
    print('Кто первым начнет игру:\n')
    x = random.randint(1,2)
    if x == 1:
        start_first = player_1
        start_second = player_2
    else:
        start_first = player_2
        start_second = player_1
    
    print(f'Первым начинает {start_first}')

    while sweets_total > 0:
        if count == 0:
            step = int(input(f'{start_first} Ваш ход ='))
            if step > sweets_total:
                step = int(input(f'{start_first} Желаемое количество больше оставшегося ='))
            if step > max_take:
                step = int(input(f'{start_first} Можно взять не более 28 конфет за раз ='))
            if sweets_total > 0:
                sweets_total = sweets_total - step
                print(f'Осталось = {sweets_total} штук')
                count = 1
        else:
            print('Осталось 0 конфет')
            print(f'Победил {start_first}!')
        
        if count == 1:
            step = int(input(f'{start_second} Ваш ход ='))
            if step > sweets_total:
                step = int(input(f'{start_second} Желаемое количество больше оставшегося ='))
            if step > max_take:
                step = int(input(f'{start_second} Можно взять не более 28 конфет за раз ='))
            if sweets_total > 0:
                sweets_total = sweets_total - step
                print(f'Осталось = {sweets_total} штук')
                count = 0
            if sweets_total == 0:
                print(f'Победил {start_second}!')

        else:
            print('Осталось 0 конфет')
            print(f'Победил {start_second}!')
    
player_vs_player()
        
            
def player_vs_bot():
    sweets_total = 43
    max_take = 28
    count = 0
    
    player_1 = input('Введите Ваше имя: ')
    player_2 = input('С Вами играет Компьютер')
    
    print('Кто первым начнет игру:\n')
    x = random.randint(1,2)
    if x == 1:
        start_first = player_1
        start_second = player_2
    else:
        start_first = player_2
        start_second = player_1
    
    print(f'Первым начинает {start_first}')

    while sweets_total > 0:
        if count == 0:
            step = int(input(f'{start_first} Ваш ход ='))
            if step > sweets_total:
                step = int(input(f'{start_first} Желаемое количество больше оставшегося ='))
            if step > max_take:
                step = int(input(f'{start_first} Можно взять не более 28 конфет за раз ='))
            if sweets_total > 0:
                sweets_total = sweets_total - step
                print(f'Осталось = {sweets_total} штук')
                count = 1
        else:
            print('Осталось 0 конфет')
            print(f'Победил {start_first}!')
        
        if count == 1:
            step = int(input(f'{start_second} Ваш ход ='))
            if step > sweets_total:
                step = int(input(f'{start_second} Желаемое количество больше оставшегося ='))
            if step > max_take:
                step = int(input(f'{start_second} Можно взять не более 28 конфет за раз ='))
            if sweets_total > 0:
                sweets_total = sweets_total - step
                print(f'Осталось = {sweets_total} штук')
                count = 0
            if sweets_total == 0:
                print(f'Победил {start_second}!')

        else:
            print('Осталось 0 конфет')
            print(f'Победил {start_second}!')




        

