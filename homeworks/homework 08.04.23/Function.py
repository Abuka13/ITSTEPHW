# n = int(input())
# odd = 0 #нечетный
# even = 0
# for i in range(n):
#     i = int(input())
#     if i % 2 ==0:
#         even+=1
#     else:
#         odd+=1
#
# if odd > even:
#     print("Нет")
# else:
#     print("Да")
###############################################################3
#tODO task2
# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sum = 0
# for i in range(len(l)):
#     sum += l[i][i]
# print(sum)
##############################################################33
#TODO task3
def authorization(name,surname,objective,education,experience):
    print(f'Your name is {name}\nYour surname is {surname}\nYour objective is {objective}\nYour education is {education}\nYour education is {experience}')

authorization(input('Your name: '),input('Your surname: '),input('Your objective: '),input('Your education: '),input('Your experience: '))


