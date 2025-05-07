import requests

BASEURL = 'http://127.0.0.1:8000/'
ENDPOINT = 'car/list'

def getlist():
    resp = requests.get(BASEURL+ENDPOINT)
    print(resp)
    print(resp.status_code)
    print(resp.json())

getlist()