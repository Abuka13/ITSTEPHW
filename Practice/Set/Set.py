#
# a = {1,2,3}
# print(a) #{1,2,3}
b = {1,2,3,4,1,2,3,4,1,2,3,4}
print(b) #{1,2,3,4}
c = set('abracadabra')
d = set([1,2,3,4,4,3,2,1])
print(c) #{'c', 'd', 'r', 'b', 'a'}
print(d) #{1, 2, 3, 4}
#TODO МНОЖЕСТВО НЕ ИЗМЕНЯЕТСЯ
## a[1] = 100
# print(a)
print('\n\n\n\n\n')




#TODO ДОБАВЛЕНИЕ
# print('ДОбавление')
# a = {54,32,54,3,4,2} #{32, 2, 3, 4, 54, 9}
# a.add(9)
# print(a)
# a.update([5,6,7])
# print(a) #{2, 3, 4, 5, 6, 7, 9, 32, 54}
# a.update('hello')
# print(a) #{'l', 2, 3, 4, 5, 6, 7, 'e', 9, 32, 'o', 'h', 54}
# print('\n\n\n\n\n')



print('Удаление')
#TODO УДАЛЕНИЕ
l = {54,32,54,3,4,2}
l.discard((4))
print(l.pop()) #Удаляет рандомный элемент
print(l)
print('\n\n\n\n')



# #TODO ОПЕРАЦИИ
# a = {54,32,3,2,4,32}
# print(len(a)) #6
# print(4 in a, 7 not in a) #True False
#
m = {4,3,2,1}
n = {3,4,5,6,7}
# #TODO общие элементы (intersection)
# print(m & n) #{3, 4} общие элементы (intersection)
# # m.intersection_update(n)
# # print(m) #{3, 4}
# #TODO уникальные элементы (union)
print(m | n) #or print(m.union(n))
# print(m - n) #{1, 2} из множества m удалились 4 и 3 которые также есть в множетсе m
# print(n - m) #{5, 6, 7}
# print(m ^ n) #Выводит все уникальные элементы БЕЗ ОБЩИХ {1, 2, 5, 6, 7}
# print(m == n) #False



#TODO FOR
a = {1,2,3,4}
for i in a:
    print(i)



# #TODO ЗАДАЧА узнать сколько уникальных слов в множестве
# text = input()
# a = set()
# while text!='':
#     words = text.split()
#     a.update(words)
#     print(a)
#     text = input()
# print(len(a))


k = {1,2,3,4}
o = {4,3,2,1}
print(k ==   o)


