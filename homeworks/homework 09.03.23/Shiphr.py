class Shiphr:
    def __init__(self,text: str,shift: int):

        self.text = text
        self.shift = shift
    def spihr(self):
        space = ''
        for i in range(len(self.text)):
            ch = self.text[i]

            if ch.isalpha():
                d = ord(ch) + self.shift

                if ch.isupper():
                    if d > ord('Z'):
                        d -= 26
                    elif d < ord('A'):
                        d += 26
                elif ch.islower():
                    if d > ord('z'):
                        d -= 26
                    elif d < ord('a'):
                        d += 26

            space += chr(d)
        else:
            space += ch
        return space

    def despiphr(self):
        space = ''
        for i in self.text:
            if i.isalpha():
                d = ord(i.lower())
                despiphr= (d - self.shift - 97) % 26 + 97
                despiphr_i = chr(despiphr)
                if i.isupper():
                    despiphr_i = despiphr_i.upper()
                space += despiphr_i
            else:
                space += i
        return space
s = input("Шифрование или Дешифрование?: ")
tx = input('Введите текст: ')
sh = int(input('Введите число шифта: '))
c1 = Shiphr(tx, sh)
if s == 'Шифрование':
    print(c1.spihr())
if s == 'Дешифрование':
    print(c1.despiphr())



