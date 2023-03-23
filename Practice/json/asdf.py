import json
import os
import shutil
# file1 = open('z_new.txt', mode='w')
# file1.close()
# with open('z_new.txt', 'w') as file2:
#     file2.write("Python is awesome!123\n\thi")
# dict1 = {"name": "Bogdan"}
# # запись
# # with open('data/new.json', 'w') as file1:
# # #     # todo сразу запись словаря в файл
# # #     json.dump(dict1, file1)
with open('data/new.json', 'r') as file2:
    # todo сразу чтение словаря из файла
    dict3 = json.load(file2)
    print(dict3)


