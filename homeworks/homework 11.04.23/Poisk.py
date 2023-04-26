# m = int(input())
# a = []
# for i in range(m):
#     i = input('Введите строку')
#     a.append(i)
# for i in range(len(a)):
#     print('*' * (len(a) - i) + a[i])
#TODO task2
n = int(input())
a = []
for i in range(n):
    i = int(input())
    a.append(i)
r = int(input())
b = r - sum(a)
print('need',b)
a.append(b)
print(a)