#Создание кортежа
# a = (1,2,3,4,5)
# # b = tuple(range(3)) #0,1,2
# print(a,type(a))
# print(2 in a, 6 in a, 7 not in a) #True False True
# Todo Слияние
# a = (1,2,3)
# b = (4,5)
# print(a+b,b+a)  #(1, 2, 3, 4, 5) (4, 5, 1, 2, 3)
# print(a * 4)  #(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
# print(min(a),max(a)) #1 and 3
# print(sum(a)) #6
# TOdo Кортеж неизменяемый обьект
a = (1,'hello',3,[10,20,30],False,5)
print(a[1]) #hello
# a[1] = 3 невозможно изменить элемент
print(a.index('hello')) #1
print(a.count(6)) #0
# print(a.append(5)) #ошибка
a[3].append(100)
print(a) #(1, 'hello', 3, [10, 20, 30, 100], False, 5)
