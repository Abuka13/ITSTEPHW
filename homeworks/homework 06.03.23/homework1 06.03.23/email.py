import re
import datetime
import time
demands_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
demands_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,16}$"
val1 = datetime.datetime.now()

while True:
    email = input('Введите свой электронный адрес: ')
    if re.match(demands_email, email):
        print('Отлично!')
        break
    else:
        print('Электронный адрес неверного формата')
while True:
    password = input('Введите свой пароль: ')
    if re.match(demands_password, password):
        print('Отлично!')
        break
    else:
        print('Пароль неверного формата')
with open('data.txt', 'a',encoding='utf-8') as f:
    f.write(f'{val1}\n')
    f.write(f'Электронный адрес: {email}\n')

    f.write(f'Пароль: {password}')
