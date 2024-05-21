import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijson4'
res = requests.get(BASE_URL+ENDPOINT)
# we got the response 
print(res,type(res))
# convert response into dict 
data = res.json()
print(type(data))
print('Data from django Application:')
print('#'*50)
print(data)
print('Employee Number:',data['eno'])
print('Employee Name:',data['ename'])
print('Employee Salary:',data['esal'])
print('Employee Address:',data['eaddr'])