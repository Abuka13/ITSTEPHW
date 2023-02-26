# class Human:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def get_name(self):
#         return "Person's name is " + str(self.name)
#     def get_age(self):
#         return "Person's age is " + str(self.age)
#     def get_gender(self):
#         return "Person's gender is " + str(self.gender)
#     def print_full_info(self):
#         print("Person: ",self.name)
#         print("Person: ", self.age)
#         print("Person: ", self.gender)
# human1 = Human(name="Abuka",age = 45, gender = 'Male')
# print(human1.get_age())
# class Person:
#     name = 'Abuka'
#     age = 16
# print(Person.name) #Abuka
# print(getattr(Person,'name')) #Abuka
# print(getattr(Person,'x',100)) #100
# Person.name = 'Mai'
# print(Person.name) #Mai
# Person.x = 100
# print(Person.x) #100
# Person.x = 200
# print(Person.x) #200
# print('\n\n\n\n\n\n\n\n\n\n')
# #МЕТОДЫ
# #Создать, Поменять
# setattr(Person,'y',300)
# print(Person.y) #300
# print('\n\n')
# #Удалить
# del Person.y
# print(Person.__dict__)
# delattr(Person,'x')
# print(Person.__dict__)
# print('\n\n')
#
# class Car:
#     model = 'BMW'
#     color = 'red'
# a = Car()
# b = Car()
# print(a.model) #BMW
# print(Car.__dict__) #есть много чего
# print(a.__dict__) #ничего нету
# # Создание атрибутов для a
# setattr(a,'model','Toyota')
# print(a.__dict__) #{model: Toyota}
# #Если что-нибудь добавить в класс Car то оно тоже добавиться в a и b
# Car.engine = 1.6
# print(a.engine) #1.6
# #ВАЖНАЯ ВЕЩЬ
# del a.model #удаляет бмв и атрибут из dict
# print(a.model) #достает бвм в из класса Car
# ФУНКЦИЯ КАК АТРИБУТ КЛАССА
class Car:

    model = 'BMW'
    color = 'red'

    @staticmethod
    def drive():
        print("Let's go!!!")
getattr(Car,'drive')() #Let's go!!!
a = Car()
# print(a.drive()) #ОШИБКА

print(a.drive()) #staticmethod программа выдает ошибку