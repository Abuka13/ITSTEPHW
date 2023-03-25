def decorator_authentificator(func):
    def wrapper(**kwargs):
        password = func(**kwargs)
        if password == '':
            return "Пароль не найден"
        else:
            return func(**kwargs)
    return wrapper
@decorator_authentificator
def password_check(password):
    return password
passw = input('Введите пароль: ')
print(password_check(password = passw))








