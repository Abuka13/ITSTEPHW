
#timer:
import time
import time
t = ''
sec = int(input("Введите секунды(максимально - 60): "))
min = int(input("Введите минуты(максимально - 60): "))
h = int(input("Введите часы(максимально - 24): "))
t+=str(h)+':'
t+=str(min)+':'
t+=str(sec)
while True:
    print(f'{h}:{min}:{sec}')
    time.sleep(1.0)
    if sec > 0:
        sec-=1
    elif sec == 0 and min > 0:
        sec = 59
        min-=1
    elif sec == 00 and min == 0 and h > 0:
        h-=1
        sec =59
        min = 59
    elif sec == 00 and min == 0 and h == 0:
        print("Отсчет закончен")
        break



