import time
s = 00
m = 0
h = 0
f = int(input())
while True:

    time.sleep(1)
    s+=1*f


    if s > 59:
        m+=1
        s = 0
    elif s == 59 and m == 59:
        h+=1
        s = 0
        m = 0
    if s < 9:
        s1 = '0'+str(s)
    else:
        s1 = s
    if m < 9:
        m1 = '0'+str(m)
    else:
        m1 = m
    if h < 9:
        h1 = '0'+str(h)
    else:
        h1 = h
    print(f'{h1}:{m1}:{s1}')