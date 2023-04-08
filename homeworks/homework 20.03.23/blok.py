#TODO task1
#s = int(input())
#p = int(input())
#salary = int(input())
#if s + p <= salary:
#    print("Да")
#else:
#    print("Нет")
#TODO task2
def ferz(x1,y1,x2,y2):
    if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
        print('YES')
    else:
        print('NO')
def horse(x1,y1,x2,y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        print('YES')
    else:
        print('NO')
try:

    choice = int(input("ход конем или ферзем? 1 - конь 2 - ферзь: "))
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if choice == 2:
        print(ferz(x1, y1, x2, y2))
    if choice == 1:
        print(horse(x1, y1, x2, y2))
except ValueError:
    print("Нужно ввести цифру")
