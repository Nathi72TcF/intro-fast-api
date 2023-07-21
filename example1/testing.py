import requests

requests = requests.get('http://127.0.0.1:8000/random/144')
print(requests.json())
