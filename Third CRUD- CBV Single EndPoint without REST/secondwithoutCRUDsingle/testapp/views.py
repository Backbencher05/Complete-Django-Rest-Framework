from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
import json
from testapp.forms import EmployeeForm

from testapp.mixin import HttpResponseMixin,SerializeMixin
from testapp.utils import get_object_by_id, is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.



@method_decorator(csrf_exempt, name='dispatch')   #Disable CSRF varification         
class EmployeeCRUDCBV(HttpResponseMixin, SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        data = request.body #we got JSON data
        # check for json
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide valid json data only'})
            return self.response_message(json_data,status=400)
        # if valid json data than convert it into python dict 
        pdata =json.loads(data)
        # get id from dict
        id = pdata.get('id',None) #if id not available than None
        if id is not None:
            emp = get_object_by_id(id)
            if emp is None: #No data available with this id
                json_data= json.dumps({'msg': 'The requested Resource not available with Matched ID'})
                return self.response_message(json_data,status=400)
        
            # if ID data is available
            json_data=self.serializedata([emp,])
            return self.response_message(json_data)
        
        # if id is None(Client is not sending any id )
        # we have to provide all the data 
        qs = Employee.objects.all()
        json_data = self.serializedata(qs)
        return self.response_message(json_data)

    # post method
    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send the valid Data'})
            return self.response_message(json_data,status=400)
        
        # if valid data is there 
        # Now to save this data we required Form(model form )
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource Created Successfully'})
            return self.response_message(json_data)
        if form.errors:
            json_data= json.dumps(form.errors)
            return self.response_message(json_data,status=400)


    def put(self,request,*args,**kwargs):
        data = request.body #we got JSON data
        # check for json
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide valid json data only'})
            return self.response_message(json_data,status=400)
        # if valid json data than convert it into python dict 
        pdata =json.loads(data)
        # get id from dict
        id = pdata.get('id',None) #if id not vaailable than None
        
        if id is None:
            json_data = json.dumps({'msg': 'To Perform updation ID is mendatory, Please provide the ID'})
            return self.response_message(json_data,status=400)
        
        if id is not None:
            emp = get_object_by_id(id)
            if emp is None: #No data available with this id
                json_data= json.dumps({'msg': 'The requested Resource not available with Matched ID, Not Possible to permorm Updation'})
                return self.response_message(json_data,status=400)
            provided_data = json.loads(data)
            original_data ={
                'eno': emp.eno,
                'ename': emp.ename,
                'esal': emp.esal,
                'eaddr': emp.eaddr,
            }
            original_data.update(provided_data)
            # Now data is updated , to save this data 
            form = EmployeeForm(original_data,instance=emp)
            if form.is_valid():
                form.save(commit=True)
                json_data=json.dumps({'msg': 'Resource updated Successfully'})
                return self.response_message(json_data)
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.response_message(json_data,status=400)
            
    def delete(self,request,*args,**kwargs):
        data = request.body #we got JSON data
        # check for json
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide valid json data only'})
            return self.response_message(json_data,status=400)
        # if valid json data than convert it into python dict 
        pdata =json.loads(data)
        # get id from dict
        id = pdata.get('id',None) #if id not vaailable than None
        
        if id is None:
            json_data = json.dumps({'msg': 'To Perform Deletion ID is mendatory, Please provide the ID'})
            return self.response_message(json_data,status=400)
        
        if id is not None:
            emp = get_object_by_id(id)
            if emp is None: #No data available with this id
                json_data= json.dumps({'msg': 'The requested Resource not available with Matched ID, Not Possible to permorm Updation'})
                return self.response_message(json_data,status=400)
            
            status,deleted_item=emp.delete()
            if status == 1:
                json_data = json.dumps({'msg': 'Resource Deleted Successfully'})
                return self.response_message(json_data)
            json_data = json.dumps({'msg': 'Unable to Delete...Plz try Again'})
            return self.response_message(json_data,status=400)























# 1. Read
# get data of particular id 
class EmployeeDetailsCBV(View):
    def get(self,request,*args,**kwargs):
        emp = Employee.objects.get(id=1)
        print(emp,type(emp))
        emp_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data,content_type='application/json')
    
# get data depend on id 
class EmployeeDetailsCBV1(View):
    def get(self,request,id, *args,**kwargs):
        # get data 
        emp = Employee.objects.get(id=id)
        emp_data ={
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr,
        }
        # convert this dict to the JSON to send to the response 
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data,content_type ='application/json')

