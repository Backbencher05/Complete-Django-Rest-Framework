import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apis/'

def get_resource():
    resp = requests.get(BASE_URL+ENDPOINT)
    print(resp)
    print(resp.status_code)
    print(resp.json()) #this JSON function will convert the information into dict

# get_resource()

def get_resourcewithid(id):
    resp = requests.get(BASE_URL+ENDPOINT+id)
    print(resp)
    print(resp.status_code)
    print(resp.json()) #give/convert into dict

# id = input("Enter Some ID: ")
# get_resourcewithid(id)

# Exception Handling at User side 
def get_resourcewithid(id):
    resp = requests.get(BASE_URL+ENDPOINT+id)
    print(resp)
    print(resp.status_code)
    # if resp.status_code in range(200,300):
    if resp.status_code  == requests.codes.ok:
        print(resp.json()) #give/convert into dict
    else:
        print('Something goes wrong')


# id = input("Enter Some ID: ")
# get_resourcewithid(id)

def get_all():
    resp = requests.get(BASE_URL+ENDPOINT)
    print(resp)
    print(resp.status_code)
    print(resp.json()) #give/convert into dict

# get_all()


# 2. create 
def create_resource():
    new_emp = {
        'eno': 500,
        'ename': 'shiva',
        'esal': 25,
        'eadd': 'Banglore',
    }
    json_data = json.dumps(new_emp)
    resp = requests.post(BASE_URL+ENDPOINT,data=json_data)
    print(resp.status_code)
    print(resp.json())

# create_resource()

# 3. update record 
# to which reccord you want to update 
def update_resource(id):
    new_emp = {
        'esal': 27,
        'eadd': 'Bhagalpur',
    }
    # we have dict data let convert it into json 
    json_data = json.dumps(new_emp)
    res = requests.put(BASE_URL+ENDPOINT+str(id)+'/', data=json_data)
    print(res.status_code)
    # jo bhi response aaya usko fhir convert krr lete hai
    print(res.json())

# id = input("Enter Some id: ")
# update_resource(5)

def delete_resource(id):
    res = requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
    print(res.status_code)
    # jo bhi response aaya usko fhir convert krr lete hai
    print(res.json())

# id = input("Enter Some id: ")
delete_resource(5)


