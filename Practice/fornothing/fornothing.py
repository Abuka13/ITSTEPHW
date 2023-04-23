#Задание 2.
import json
import requests
import os
response = requests.get("https://jsonplaceholder.typicode.com/todos")
# for i in range(1,11):
#     with open(f'json{i}.json','w') as file:
#
#         todos = json.loads(response.text)
#         file.write(str(todos[i-1:i]))
for i in range(1,10):
    print(response.json())
#Задание 3
#3.1)
sec = 0
