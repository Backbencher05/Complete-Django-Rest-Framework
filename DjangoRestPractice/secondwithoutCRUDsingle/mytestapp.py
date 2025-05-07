import requests
import json


BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = 'api/'


def get_resourse(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id 
        }
    json_data = json.dumps(data)
    resp = requests.get(BASE_URL+ENDPOINT,data=json_data)
    print(resp.status_code)
    print(resp)
    print(resp.json())

# get_resourse()

def create_resourse():
    data = {
        'eno': 105,
        'ename': 'Asad',
        'esal': 260,
        'eaddr': 'Manad'
    }
    json_data = json.dumps(data)
    resp = requests.post(BASE_URL+ENDPOINT, data=json_data)
    print(resp.status_code)
    print(resp)
    print(resp.json())


create_resourse()


def update_resourse(id):
    data = {
        'id': id,
        'esal': 65000,
        'eaddr': 'Chidwada', 
    }
    json_data = json.dumps(data)
    resp = requests.put(BASE_URL+ENDPOINT,data= json_data)
    print(resp.status_code)
    print(resp)
    print(resp.json())