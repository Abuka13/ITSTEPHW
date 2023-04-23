import re

pattern_speed = re.compile(r'^(?=.*[0-9].*)')
class Car:

    def __init__(self,speed,color):
        self.speed = speed
        self.color = color

    def check(self):

        if bool(pattern_speed.match(self.speed)) == True:
            print(f'Скорость машины {self.speed}')
        else:
            print('Не правильный ввод')
emp1 = Car(input(), 'red')
emp1.check()