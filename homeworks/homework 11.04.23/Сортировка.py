


# #TODO task2
# n = int(input())
# a = []
# r = 2
# c = 0
# total = 0
# for i in range(n):
#     i = int(input())
#     a.append(i)
# a.sort(reverse=True)
# while len(a) > c:
#     total +=sum(a[c:r])
#     c+=3
#     r+=3
# print(total)
#task2
s = [9,4,1,6]
s = sorted(s)
min = 1000
n = []
for i in range(len(s) - 1):
    d = s[i+1] - s[i]
    if d < min:
        min = d
        n = s[i], s[i+1]
print(n)




