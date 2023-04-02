import json
import requests
for i in range(1,11):
    with open(f'json{i}.json','w') as file:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        todos = json.loads(response.text)
        file.write(str(todos[i-1:i]))