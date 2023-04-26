#task1
# n = int(input())
# s = input()
# for i in s:
#     d = ord(i) - n
#     if d < 97:
#         d+=26
#     print(chr(d), end='')
#TODo task2
#
# a = ('banana','apple','pear','banana','banana','apple')
# r = input("Введите фрукт: ")
# sum = 0
# for i in range(len(a)):
#     if r == a[i]:
#         sum+=1
# print(sum)
#TODO task3
#
# a = ('banana','apple','bananamango','banana','strawberry-banana','apple')
# r = input("Введите фрукт: ")
# sum = 0
# for i in range(len(a)):
#     if r in a[i]:
#         sum+=1
# print(sum)
#TODO task4
car = ["Toyota", "BMW", "Ford", "Honda", "Toyota", "Chevrolet"]
old = input("Введите название производителя: ")
new = input("Введите слово для замены: ")

for i in range(len(car)):
    if car[i] == old:
        car[i] = new
print(car)
