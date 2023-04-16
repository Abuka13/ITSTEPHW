#TODO task1
# select = int(input("1 - Фибоначчи\n"
#                    "2 - Факториал\n"
#                    "3 - Арифматическое действие\n"
#                    "4 - Возведение в степень\n"))
# if select == 1:
#     def fibonacci(n):
#         if n <= 1:
#             return 1
#         else:
#             return fibonacci(n-1) + fibonacci(n-2)
#     n = int(input('Введите число: '))
#     for i in range(n+1):
#         print(f'fibonacci number {i} =', fibonacci(i), end='\n')
# elif select == 2:
#     def factorial(f):
#         if f<=1:
#             return 1
#         else:
#             return f * factorial(f-1)
#     f = int(input('Введите число: '))
#     print(f'factorial number {f} = ', factorial(f))
# if select == 3:
#     def arithmetic(b):
#         if b == 1:
#             task1 = lambda x,y: x - y
#             return task1(int(input('Введите число: ')), int(input('Введите число: ')))
#         elif b == 2:
#             task2 = lambda x,y: x * y
#             return task2(int(input('Введите число: ')), int(input('Введите число: ')))
#         elif b == 3:
#             task3 = lambda x,y: x ** y
#             return task3(int(input('Введите число: ')), int(input('Введите число: ')))
#         elif b == 4:
#             task4 = lambda x,y: x / y
#             return task4(int(input('Введите число: ')),int(input('Введите число: ')))
#         elif b == 5:
#             task5 = lambda x, y: x // y
#             return task5(int(input('Введите число: ')), int(input('Введите число: ')))
#         elif b == 6:
#             task6 = lambda x, y: x % y
#             return task6(int(input('Введите число: ')), int(input('Введите число: ')))
#     print(arithmetic(int(input("1 - Вычитание\n"
#               "2 - Умножение\n"
#               "3 - возведение степень\n"
#               "4 - деление\n"
#               "5 - целочисленное деление\n"
#               "6 - остаток от деления\n"))))
# elif select == 4:
#     a = int(input('Введите число: '))
#     b = int(input('Введите число: '))
#     print(a ** b)
#TODO task2
print('********** Игра Крестики-нолики для двух игроков **********')
print('-------------')
maps = [1,2,3,
        4,5,6,
        7,8,9]
def print_maps():
    print('|',maps[0],'|',maps[1],'|',maps[2],'|',end='\n')
    print('-------------')
    print('|', maps[3], '|', maps[4], '|', maps[5], '|', end='\n')
    print('-------------')
    print('|', maps[6], '|', maps[7], '|', maps[8], '|', end='\n')
    print('-------------')
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
def get_result():
    win = ""
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win
game_over = False
player1 = True
while game_over == False:
    print_maps()
    if player1 == True:
        symbol = "X"
        step = int(input("Куда поставим? "))
    else:
        symbol = "O"
        step = int(input("Куда поставим? "))

    step_maps(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)
print_maps()
print(win,'Выиграл')