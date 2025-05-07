from django.shortcuts import render
from django.http import HttpResponse

def emp_data_view(request):
    # Ths is python dict 
    emp_data = {
        'eno': 100,
        'ename': 'Aditya',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }

    res = "<h1>Employee Number: {} <br> Employee Name: {} <br> Employee Salary: {} <br> Employee Address: {}".format(emp_data['eno'], emp_data['ename'], emp_data['eaddr'], emp_data['esal']) 
    return HttpResponse(res)

import json
def emp_data_jsonView(request):
    # This is python Dict 
    emp_data = {
        'eno': 100,
        'ename': 'Aditya',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type = 'application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    # This is python Dict 
    emp_data = {
        'eno': 100,
        'ename': 'Alok',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }

    return JsonResponse(emp_data)


from django.views.generic import View

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        emp_data = {
            'eno': 100,
            'ename': 'Anjali',
            'esal': 10000,
            'eaddr': 'Naraini'
        }
        return JsonResponse(emp_data)
    

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
    


# Mixin
from testapp.mixin import HttpResponseMixin

class JsonCBV3(View, HttpResponseMixin):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'Hello This is from get method'})
        return self.rendertoHttpResponse(json_data)
    

    # This is post Request: CSRF Token Required 
    # For Testing Purpose comment CSRF Middleware in settings.py
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'Hello This is from post method'})
        return self.rendertoHttpResponse(json_data)
    

    def put(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'Hello This is from put method'})
        return self.rendertoHttpResponse(json_data)
    

    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'Hello This is from Delete method'})
        return self.rendertoHttpResponse(json_data)

