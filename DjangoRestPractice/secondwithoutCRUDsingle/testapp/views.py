from django.shortcuts import render
from django.views.generic import View
from testapp.utils import is_json, get_object_by_id
import json
from testapp.mixin import HttpResponseMixin,SerializeMixin
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View,HttpResponseMixin,SerializeMixin):
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_data = is_json(data)
        if not valid_data:
            json_data = json.dumps({'msg': 'Please provide the valid json data only'})
            return self.response_message(json_data,status=400)
        
        pdata = json.loads(data)
        id = pdata.get('id',None)
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
    
    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json =is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide the valid JSON'})
            return self.response_message(json_data, status=400)
        
        # if valid data is there 
        # Now to save this data we required Form(model form )
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Rosourse Created Successfully'})
            return self.response_message(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.response_message(json_data,status=400)


    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide valid json data only'})
            return self.response_message(json_data,status=400)
        p_data = json.loads(data)
        id = p_data.get('id', None)

        if id is None:
            json_data = json.dumps({'msg': 'To Perform updation ID is mendatory, Please provide the ID'})
            return self.response_message(json_data,status=400)
       
        if id is not None:
            emp = get_object_by_id(id)
            if emp is None:
                json_data= json.dumps({'msg': 'The requested Resource not available with Matched ID, Not possible to perform Updation'})
                return self.response_message(json_data,status=400)
            provided_data = json.loads(data)
            original_data = {
                'eno': emp.eno,
                'ename': emp.ename,
                'esal': emp.esal,
                'eaddr': emp.eaddr
            }
            original_data.update(provided_data)
            form = EmployeeForm(original_data, instance=emp)
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




