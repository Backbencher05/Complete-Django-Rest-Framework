import requests

BASE_URL = 'http://127.0.0.1:8000/car/'
ENDPOINT = 'list/'

res = requests.get(BASE_URL+ENDPOINT)
print(res)
print(res.status_code)
print(res.json())