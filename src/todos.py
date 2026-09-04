import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
if response.status_code == 200:
    todos = response.json()
    completed_todos = []
    uncompleted_todos = []
    for todo in todos:
        completed = todo['completed']
        if completed:
            completed_todos.append(todo)
        else:
            uncompleted_todos.append(todo)
    print(completed_todos)
else:
    print("no todos found")
