
import json
# d = {
#     #key:value
#     'Astana':1,
#     'Almaty':2,                     #TODO Первый способ создать словарь
#     'Shymkent':13
# }
# print(d)
#{'Astana': 1, 'Almaty': 2, 'Shymkent': 13}

r = dict(Astana=1, Almaty=2, Shymkent=13)
print(r)                                    #TODO Второй способ создать словарь
#{'Astana': 1, 'Almaty': 2, 'Shymkent': 13}

a = [['Astana',1], ['Almaty',2], ['Shymkent',13]]
print(dict(a))
#{'Astana': 1, 'Almaty': 2, 'Shymkent': 13}         #TODO Третий способ создать словарь





#TODO
q = dict.fromkeys(['a','b','c'],1)        #TODO fromkeys() создает ключи
#{'a': None, 'b': None, 'c': None}
print(q)

#TODO ограничения
# d = {
#     1:'one',
#     [1,2]:'two',              key:value - key не может быть изменяемым элеменотом а value может
#     3:[1,2,3]
# }
# print(d)


print('\n\n\n')

#TODO Как обращаться к ключам или value