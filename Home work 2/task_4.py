# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. 
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные 
# получили по две монеты. Далее человек, на котором остановился счет, отдает все свои 
# монеты следующему по счету человеку, а сам выбывает из круга. Процесс продолжается 
# с места остановки аналогичным образом до последнего человека в круге. Составьте 
# алгоритм, который проводит эту игру. Если хотите делать паузы, то импортируйте 
# библиотеку time и используйте оттуда функцию sleep. Определите номер этого 
# человека и количество монет, которые оказались у него в конце игры.

# num_players = int(input('Введите количество игроков:\n'))
# coins_for_players = int(input('Сколько получит по 1 монете?:\n'))

# list_of_players = []
# list_of_coins = []

# list_of_players = [i for i in range(1, num_players+1)]
# print(list_of_players)

# while len(list_of_coins) < len(list_of_players):
#     for i in range(1, num_players+1):
#         if len(list_of_coins) < coins_for_players:
#             list_of_coins.insert(i, 1)
#         else:
#             list_of_coins.insert(i, 2)
# i += 1

# print(list_of_coins)


# all_people, all_money = get_people_money_lists()
# stop_word = ""
# while len(all_people) != 1:
# all_people, all_money = game(all_people, all_money)
# show_results(all_people, all_money)
# input('Для продолжения нажмите Enter')