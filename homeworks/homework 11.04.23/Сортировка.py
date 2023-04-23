# n = int(input())
# a = []
# for i in range(n):
#     i = int(input())
#     a.append(i)
# a = sorted(a)
# for j in range(1,n+1):
#     if j % 3 == 0:
#         print(a)


#TODO task2
s = []
a = [9,4,1,6]
a = sorted(a)
for i in range(len(a)):
    for j in range(1,len(a)):
        s.append(a[j]-a[i])
for i in range(len(s)):
    if s >=0:
print(s)
