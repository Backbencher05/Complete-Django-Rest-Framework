import requests
import json 

BASE_URL = 'http://127.0.0.1:8000/'

def get_resourse():
    ENDPOINT = 'api/'
    res = requests.get(BASE_URL+ENDPOINT)
    print(res)
    print(res.status_code)
    print(res.json())

def get_resoursewithId(id):
    # ENDPOINT = 'api/'
    ENDPOINT = 'apis/'
    # ENDPOINT = 'apiss/'
    res = requests.get(BASE_URL+ENDPOINT+id)
    print(res)
    print(res.status_code)
    print(res.json())
    # if res.status_code == requests.codes.ok:
    #     print(res.json())
    # else:
    #     print("Something goes wrong")

# id = input("Enter Some Id: ")
# get_resoursewithId(id)


def getall():
    # ENDPOINT = 'apiall/'
    # ENDPOINT = 'apialls/'
    ENDPOINT = 'apiallss/'
    res = requests.get(BASE_URL+ENDPOINT)
    print(res.status_code)
    print(res.json()) #to convert into dict

# getall()

def create_resourse():
    ENDPOINT = 'apiallss/'
    new_emp = {
        'eno': 105,
        'ename': 'Shiva',
        'esal': 5500,
        'eadd': 'Naraini',
    }
    json_data = json.dumps(new_emp)
    resp = requests.post(BASE_URL+ENDPOINT,data=json_data)
    print(resp.status_code)
    print(resp.json())

# create_resourse()

def update_resourse(id):
    ENDPOINT = 'apis/'
    emp = {
        'esal': 25000,
        'eadd': 'pushkar'
    }
    json_data = json.dumps(emp)
    res = requests.put(BASE_URL+ENDPOINT+str(id),data=json_data)
    print(res.status_code)
    print(res.json())

# update_resourse(3)

def delete_resourse(id):
    ENDPOINT = 'apis/'
    res = requests.delete(BASE_URL+ENDPOINT+str(id))
    print(res.status_code)
    print(res.json())

delete_resourse(5)