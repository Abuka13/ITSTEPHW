def plus_two(number):

    return number + 2
try:
    print(plus_two(int(input('Введите число: '))))
except ValueError:
    print('Ожидаемый тип данных — число!')
