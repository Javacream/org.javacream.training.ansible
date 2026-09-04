import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
if response.status_code == 200:
    todos = response.json()
    for todo in todos:
        completed = todo["completed"]
        if completed:
            print(f'Completed ToDo: {todo["title"]} , Completed: {todo["completed"]}')
else:
    print("no todos found")
