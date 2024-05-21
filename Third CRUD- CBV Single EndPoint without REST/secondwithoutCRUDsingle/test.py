import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


# if we are passing id than i want paricular id data , but 
# if we are not passing id we want all data 
def get_resource(id=None):
    data ={}
    if id is not None:
        data={
            'id': id
        }
    # if we pass id than one dict is there , if not that emplty dict
    json_data = json.dumps(data)
    resp = requests.get(BASE_URL+ENDPOINT,data=json_data)
    print(resp)
    print(resp.status_code)
    print(resp.json())

# get_resource()

def create_resource():
    new_emp = {
        'eno': 500,
        'ename': 'Gaurav',
        'esal': 7000,
        'eaddr': 'Banda',
    }
    json_data = json.dumps(new_emp)
    resp = requests.post(BASE_URL+ENDPOINT,data=json_data)
    print(resp)
    print(resp.status_code)
    print(resp.json())

# create_resource()

def update_resource(id):
    new_emp = {
        'id': id,
        'esal': 6500,
        'eaddr': 'Naraini',
    }
    json_data = json.dumps(new_emp)
    resp = requests.put(BASE_URL+ENDPOINT,data=json_data)
    print(resp)
    print(resp.status_code)
    print(resp.json())

# update_resource(5)

def delete_resource(id):
    data = {
        'id': id
    }
    resp = requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp)
    print(resp.status_code)
    print(resp.json())

delete_resource(5)




# def get_resource():
#     resp = requests.get(BASE_URL+ENDPOINT)
#     print(resp)
#     print(resp.status_code)
#     print(resp.json(), type(resp), type(resp.json()))

# # get_resource()

# def get_resourcewithid(id):
#     resp = requests.get(BASE_URL+ENDPOINT+id)
#     print(resp)
#     print(resp.status_code)
#     print(resp.json())

# # get_resourcewithid('3')

