import json
# f = "user_sttings.txt"
# myfile = open(f,mode='w',encoding='Latin-1')
# player1 = {
#     'PlfyerName': 'Abuka',
#     'Score': 13,
#     'awards': None
# }
# player2 = {
#     'PlayerName': 'Miras',
#     'Score': 9,
#     'awards': None
# }
# players = []
# players.append(player1)
# players.append(player2)
# #TODO SAVE
# json.dump(players, myfile)
# myfile.close()
# JSON в виде строки (часто приходит из "интернет" запросов)
dict_str2 = """
[{"IIN": "14124152452", "age": 24, "Name": "Bogdan1", "married": false},
{"IIN": "14124152453", "age": 24, "Name": "Bogdan2", "married": false},
{"IIN": "14124152454", "age": 24, "Name": "Bogdan3", "married": true},
{"IIN": "14124152455", "age": 24, "Name": "Bogdan4", "married": false}]
"""
print(dict_str2,type(dict_str2))
dict2 = json.loads(dict_str2)
print(dict2,type(dict2)) #[{'IIN': '14124152452', 'age': 24, 'Name': 'Bogdan1', 'married': False}, {'IIN': '14124152453', 'age': 24, 'Name': 'Bogdan2', 'married': False}, {'IIN': '14124152454', 'age': 24, 'Name': 'Bogdan3', 'married
print(dict2[0], type(dict2[0])) #{'IIN': '14124152452', 'age': 24, 'Name': 'Bogdan1', 'married': False} <class 'dict'>





print('\n\n\n\n')

dict1 = {"name": "Bogdan"}
with open('data/new.json', 'w') as file1:
    # todo сразу запись словаря в файл
    json.dump(dict1, file1)
# чтение
# with open('data/new.json', 'r') as file2:
#     # todo сразу чтение словаря из файла
#     dict3 = json.load(file2)
#     print(dict3)
#
#     # todo сначала сериализуем json_строку в словарь
#     # dict4 = json.loads(file2.read())
#     # print(dict4, type(dict4))