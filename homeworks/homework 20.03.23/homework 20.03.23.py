# task1
# number = input()
# s = []
# sum1 = 0
# sum2 = 0
# for i in range(len(number)):
#     s.append(int(number[i]))
# for j in range(len(s)//2):
#     sum1 += s[j]
# for h in range(len(s)//2,len(s)):
#     sum2 += s[h]
# if sum1 == sum2:
#     print("Счастливый")
# else:
#     print('Обычный')
#TODO TASK2
a = int(input())
b = int(input())
c = a
while c % b != 0:
    c += a
print(c)
#TODO TASK3
