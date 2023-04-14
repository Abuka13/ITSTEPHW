summa = 0
l = []
while True:
    n = int(input())
    l.append(n**2)
    summa += n
    if summa == 0:
        break
print(sum(l))

