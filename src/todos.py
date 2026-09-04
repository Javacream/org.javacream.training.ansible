import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
if response.status_code == 200:
    todos = response.json()
    for todo in todos:
        title = str(todo["title"])
        if title.startswith('q') :
            print(f'Completed ToDo: {todo["title"]} , Completed: {todo["completed"]}')
else:
    print("no todos found")
