s = [1,2,3]
try:
    index = int(input('введите число: '))
    print(s[index])
except IndexError:
    print('Данный индекс выходит из границы')