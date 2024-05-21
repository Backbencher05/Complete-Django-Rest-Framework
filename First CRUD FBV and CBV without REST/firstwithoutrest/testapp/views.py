from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def emp_data_view(request):
    # This is python Dict 
    emp_data = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'mumbai',
    }
    res = "<h1>Employee Number: {} Employee Name: {} Employee Salary:{} Employee Address: {}".format(emp_data['eno'],emp_data['ename'],emp_data['esal'], emp_data['eaddr'])
    # this is html response, understand by end user in web
    return HttpResponse(res)



# two application can communicat with each other using http protocol
# they exchange the data with each other using json 
import json
def emp_data_jsonview(request):
    # this is python Dict 
    emp_data = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'mumbai',
    }
    # we need to send the json data 
    # json.dumps() function convert python data into into json 
    # json.loads() function will convert the json data into python dict  
    json_data = json.dumps(emp_data)
    # Default content type is html 
    return HttpResponse(json_data, content_type='application/json')


# Note: This way of sending JSON response is very old. Newer versions of Django 
# dprovided a special class JsonResponse.
from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'mumbai',
    }
    return JsonResponse(emp_data)  

# we can access this json data from browser or create a python app
# From python if we want to send http request we should go for requests module.



# Class Based View to send JSON Response:
"""
Every Class based View is the child class of View i.e
Every class based view in django should extends "View" class.
It present in the following package.
"django.views.generic"
Within the class we have to provide http methods like get(),post() etc Whenever we are sending the request,
the corresponding method will be executed.
"""

from django.views.generic import View
class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data = {
        'eno': 100,
        'ename': 'aditya',
        'esal': 1000,
        'eaddr': 'mumbai',
        }
        return JsonResponse(emp_data)
    

# GET(), POST(), PUT(), DELETE() (CRUD)-> views.generic 
class JsonCBV2(View):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'This is from get method'})
        return HttpResponse(json_data,content_type='application/json')
    
    # This is post Request: CSRF Token Required 
    # For Testing Purpose comment CSRF Middleware in settings.py 
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'This is from post method'})
        return HttpResponse(json_data,content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'This is from put method'})
        return HttpResponse(json_data,content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'This is from Delete method'})
        return HttpResponse(json_data,content_type='application/json')
    

# Note: Here we have written content_type 4 times  
# there is a concept called mixin 
    
# Mixin: is a supportive person for child class but not to itself(parent) as we don't create object
    # - class which act as a parent class to provide functionality to the child class
    # - it is a seprate class which contains severals instance method
    # - itself a parent class
    # - is a child class of object
from testapp.mixin import HttpResponseMixin

class JsonCBV3(View,HttpResponseMixin):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'This is from get method'})
        return self.rendertoHttpResponse(json_data)    
    
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'This is from post method'})
        return self.rendertoHttpResponse(json_data)    
    
    def put(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'This is from put method'})
        return self.rendertoHttpResponse(json_data)    
    
    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'This is from Delete method'})
        return self.rendertoHttpResponse(json_data)    
    