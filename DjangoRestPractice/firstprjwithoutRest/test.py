import requests

BASE_URL = 'http://127.0.0.1:8001/'
END_POINT = 'apijson5/'

res = requests.delete(BASE_URL + END_POINT)
# we got the response 
print(res, type(res))
# convert response into dict 
data = res.json()
print(data)
print(res.text)
# print(data, type(data))
# print('Employee Number:',data['eno'])
# print('Employee Name:',data['ename'])
# print('Employee Salary:',data['esal'])
# print('Employee Address:',data['eaddr'])

