from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from testapp.mixin import HttpResponseMixin,SerializeMixin
from testapp.utils import is_json, get_objects_by_id
from testapp.forms import EmployeeForm

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
class EmployeeDetailsCBV(View):
    def get(self,request, *args, **kwargs):
        emp = Employee.objects.get(id=2)
        emp_data = {
            'eno': emp.eno,
            'eanme': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eadd,
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data, content_type= 'application/json')
    

class EmployeeDetailsCBV1(View):
    def get(self,request,id,*args, **kwargs):
        emp = Employee.objects.get(id=id)
        emp_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eadd,
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data, content_type = 'application/json')

from django.core.serializers import serialize  

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetailsCBV2(View,HttpResponseMixin,SerializeMixin):
    def get(self, request, id, *args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The request Resourse not available'})
            return self.response_message(json_data,status=404)
        else:
            # json_data = serialize('json', [emp,])
            json_data = self.serializedata([emp,])
            return self.response_message(json_data)
        
    def put(self,request,id,*args,**kwargs):
        # check if the object is availbale or not
        emp = get_objects_by_id(id=id)
        if emp is None:
            json_data = json.dumps({'msg': 'No Matched Resources Found, Not possible to perform Update Operation'})
            return self.response_message(json_data, status=404)
        data = request.body
        print(data)
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please sent the valid Json'})
            return self.response_message(json_data,status=400)
        # if valid json convert it into python 
        provided_data = json.loads(data)
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eadd': emp.eadd,
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resourse updated Successfully'})
            return self.response_message(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.response_message(json_data,status=400)

    def delete(self,request,id,*args,**kwargs):
        emp = get_objects_by_id(id=id)
        if emp is None:
            json_data = json.dumps({'msg': 'No matched Resourse availbale'})
            return self.response_message(json_data,status=404)
        
        status, deleted_item =emp.delete()
        if status == 1:
            json_data = json.dumps({'msg': 'Resourse deleted successfully'})
            return self.response_message(json_data)
        json_data = json.dumps({'msg': 'Unabvle to delete... Plz try again Later'})
        return self.response_message(json_data,status=404)


class EmployeeDetailsCBV3(View):
    def get(self, request, id, *args,**kwargs):
        emp = Employee.objects.get(id=id)
        # if you want particular field 
        json_data = serialize('json', [emp,],fields=('ename','eadd'))
        return HttpResponse(json_data,content_type='application/json')



#Get the List of all the Employee

class EmployeeListCBV(View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = serialize('json',qs)
        return HttpResponse(json_data,content_type='application/json')
    

class EmployeeListCBV2(View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = serialize('json',qs)
        p_data = json.loads(json_data)
        final_data = []
        for obj in p_data:
            emp_data = obj['fields']
            final_data.append(emp_data)
        json_data = json.dumps(final_data)
        return HttpResponse(json_data,content_type='application/json')
    
from testapp.mixin import SerializeMixin, HttpResponseMixin
from testapp.utils import is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV3(View,SerializeMixin,HttpResponseMixin):
    def get(self,request,*args,**kwargs):
        try:
            qs = Employee.objects.all()
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource not available'})
            return self.response_message(json_data,status=404)
        else:
            json_data = self.serializedata(qs)
            return self.response_message(json_data)


    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send the valid Data'})
            return self.response_message(json_data,status=400)
        
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created Succesfully'})
            return self.response_message(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.response_message(json_data,status=400)