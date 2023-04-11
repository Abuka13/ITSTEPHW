import json
import requests
class Json:
    with open(f'json1.json','w') as file:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        todos = json.loads(response.text)
        file.write(str(todos))
print(Json())