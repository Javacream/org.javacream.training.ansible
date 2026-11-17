import requests
url = 'http://10.160.1.85:8080/people'
response = requests.get(url)
data = response.json()
print(data)