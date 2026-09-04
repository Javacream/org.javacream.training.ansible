import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
people = response.json()

for person in people:
    print(person["id"], person["name"], person["username"])
