#1. Напишите функцию superset(), которая принимает 2 множества. Результат работы
#функции: вывод в консоль одного из сообщений в зависимости от ситуации:
#1 - «Супермножество не обнаружено»
# – «Объект {X} является чистым супермножеством»
#3 – «Множества равны»
# def superset(set_1, set_2):
#     if set_1 > set_2:
#         print(f'Объект {set_1} является чистым супермножеством')
#     elif set_1 == set_2:
#         print(f'Множества равны')
#     elif set_1 < set_2:
#         print(f'Объект {set_2} является чистым супермножеством')
#     else:
#         print('Супермножество не обнаружено')
#
# # Тесты
# set_1 = {1, 4, 7, 8}
# set_2 = {7, 8}
# print(superset(set_1,set_2))
#TODO task2
# d = {}
# def add(english_word, french_word):
#     d[english_word] = french_word
# def remove(english_word):
#     if english_word in d:
#         del d[english_word]
# def find(english_word):
#     if english_word in d:
#         return d[english_word]
#     else:
#         return None
# def replace(english_word, french_word):
#     if english_word in d:
#         d[english_word] = french_word
# add("dog", "chien")
# add("bird", "oiseau")
# remove("dog")
# print(find("cat"))
# replace("bird", "oiseaux")
# print(d)
#task3
# Предоставлен список натуральных чисел. Требуется сформировать из них множество.
# Если какое-либо число повторяется, то преобразовать его в строку по образцу: например, если
# число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4, строка
# «44» (второе повторение, т.е. число дублируется в строке), строка «444» (третье повторение,
# т.е. строка множится на 3).
# Реализуйте вывод множества через функцию set_gen().

st = set()

def set_gen(s):
    n = 0
    for i in s:
        for j in s:
            if i == j:
                n+=1
            else:
                n+=0
        st.add(str(i)*n)
        n = 0
    return st
s = [1, 2, 3, 3, 2, 3, 5, 5]
print(set_gen(s))