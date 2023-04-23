

class Roman:

    def __init__(self,number1,number2,x,z):
        self.dg1 = x
        self.dg2 = z
        self.digit1 = number1
        self.digit2 = number2


        for i in range(len(self.digit1)):
            if self.digit1 == 'IV':
                self.dg1 = self.dg1 + 3
            elif self.digit1 == 'IX':
                self.dg1 = self.dg1 + 8
            elif self.digit1[i] == 'I':
                self.dg1 = self.dg1 + 1

            if self.digit1 != 'IV' and self.digit1[i] == 'V':
                self.dg1 = self.dg1 + 5

            if self.digit1 != 'IX' and self.digit1[i] == 'X':
                self.dg1 = self.dg1 + 10

            elif self.digit1[i] == 'L':
                self.dg1 = self.dg1 + 50
            elif self.digit1[i] == 'C':
                self.dg1 = self.dg1 + 100
            elif self.digit1[i] == 'D':
                self.dg1 = self.dg1 + 500
            elif self.digit1[i] == 'M':
                self.dg1 = self.dg1 + 1000
        for i in range(len(self.digit2)):
            if self.digit2 == 'IV':
                self.dg2 = self.dg2 + 3
            elif self.digit2 == 'IX':
                self.dg2 = self.dg2 + 8
            if self.digit2[i] == 'I':
                self.dg2 = self.dg2 + 1

            if self.digit2 != 'IV' and self.digit2[i] == 'V':
                self.dg2 = self.dg2 + 5


            if self.digit2 != 'IX' and self.digit2[i] == 'X':
                self.dg2 = self.dg2 + 10

            elif self.digit2[i] == 'L':
                self.dg2 = self.dg2 + 50
            elif self.digit2[i] == 'C':
                self.dg2 = self.dg2 + 100
            elif self.digit2[i] == 'D':
                self.dg2 = self.dg2 + 500
            elif self.digit2[i] == 'M':
                self.dg2 = self.dg2 + 1000
        if self.digit1 == 'IV':
            self.dg1 = 4
        if self.digit1 == 'IX':
            self.dg1 = 9
        if self.digit2 == 'IV':
            self.dg2 = 4
        if self.digit2 == 'IX':
            self.dg2 = 9
    def add(self):
        return self.dg1 + self.dg2
    def minus(self):
        return self.dg1 - self.dg2
    def divide(self):
        return self.dg1 / self.dg2
    def multiply(self):
        return self.dg1 * self.dg2





n = input('Введите число: ')
n1 = input('Введите число: ')
Roman1 = Roman(number1=n,number2=n1,x=0,z=0)
h = int(input('Какой метод вы хотите использовать?: сложение - 1, вычитание - 2, умножение - 3, деление - 4'))
if h == 1:
    print(Roman1.add())
elif h == 2:
    print(Roman1.minus())
elif h == 3:
    print(Roman1.multiply())
elif h == 4:
    print(Roman1.divide())