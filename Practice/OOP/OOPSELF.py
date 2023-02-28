# class Car:
#     model = 'BMW'
#     color = 'red'
#     def Abuka_uchit(self):
#         return self.model
#
# a = Car()
# b = Car()
# print(a.Abuka_uchit())
# class Car:
#
#     model = 'BMW'
#     color = 'red'
#     number = 1500
#     def Abuka_uchit(self,n):
#         return self.number + n
#
#
# a = Car()
# a.year = 1904
# b = Car()
# b.year = 1950
# print(a.Abuka_uchit(1000)) #число n = 1000

class Person:
    def get_age(self, current):
        return current - self.year
a = Person()
a.year = 1904
b = Person()
b.year = 1950
print(a.get_age(2023),b.get_age(2023))


