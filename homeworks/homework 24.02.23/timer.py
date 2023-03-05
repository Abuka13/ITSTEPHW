import time
t = ''
sec = int(input())
min = int(input())
h = int(input())
t+=str(h)
t+=str(min)
t+=str(sec)
while True:
    print(f'{h}:{min}:{sec}')
    time.sleep(1.0)
    if sec > 0:
        sec-=1
    elif sec == 0 and min > 0:
        sec = 59
        min-=1
    elif sec == 0 and min == 0 and h > 0:
        sec = 59
        min = 59
        h-=1
