#TODO task1
#
# login = 'user'
# password = 'qwerty'
# log = input('Введите имя: ')
# pasw = input('Введите пароль: ')
# if log == login and pasw == password:
#     print('Authentication completed')
# else:
#     print('Invalid login or password')
#TODO task2
tenge = int(input('Insert amount in KZT: '))
select = int(input('Choose currency:'
                '\n[1] USD'
                '\n[2] EUR'
                '\n[3] RUB\n'))
USD,EUR,RUB = tenge / 420, tenge / 510, tenge / 5.8
if select == 1:
    print(round(USD,2),'EUR')
elif select ==2:
    print(round(EUR,2),'')
elif select == 3:
    print(round(RUB,2))
#TODO task2
