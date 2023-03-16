# #task1
# def shiph(step, text):
#     total = ""
#     for char in text:
#         if char == " ":
#             total += " "
#         elif char.isupper():
#             total += chr((ord(char) + step- 65) % 26 + 65)
#         else:
#             total += chr((ord(char) + step - 97) % 26 + 97)
#     return total
#
# step = int(input())
# text = input()
# print(shiph(step, text))
#task2
# a = ('Банан','Яблоко','Персик','Яблоко','Яблоко','Персик')
# fruit = input('Название фрукта: ')
# print(a.count(fruit))
#task3
# a = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
# b= 'banana'
# sum = 0
# for i in range(len(a)):
#     if b in a[i]:
#         sum+=1
# print(sum)
#task4
a = ('toyota', 'mercedes', 'hyundai', 'honda', 'audi', 'honda', 'audi','honda','mercedes','toyota','hyundai')
car = input("Enter the name of a car: ")
change = input("Enter any name to change particular car: ")
a = list(a)
for i in range(len(a)):
    if car == a[i]:
        a[i] = change
a = tuple(a)
print(a)


