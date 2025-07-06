from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse

from testapp.mixin import SerializeMixin, HttpResponseMixin
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json, get_object_by_id
from testapp.forms import EmployeeForm
# Create your views here.

# CRUD Opertaions

# 1. Read

# (Detail)get data of particular Employee 
class EmployeeDetailsCBV(View):
    def get(self,request,*args,**kwargs):
        emp = Employee.objects.get(id=2)
        # to send this information to another application, my data should be in json
        # to create json, dictionary must be required
        emp_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eadd,
        }
        # now convert this dict into json 
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data,content_type='application/json')
    
class EmployeeDetailsCBV1(View):
    def get(self,request,id,*args,**kwargs):
        emp = Employee.objects.get(id=id) 
        # to send this information to another application, my data should be in json
        # to create json, dictionary must be required
        emp_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eadd,
        }
        # now convert this dict into json 
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data,content_type='application/json')
    
# Get operation using Serializations    
from django.core.serializers import serialize
# Serialization: The process of converting object from one form to another form is called serialization.

from django.core.serializers import serialize   
class EmployeeDetailsCBV4(View):
    def get(self, request, id, *args,**kwargs):
        emp = Employee.objects.get(id=id)
        json_data = serialize('json', [emp,])
        return HttpResponse(json_data,content_type='application/json')

class EmployeeDetailsCBV2(View,HttpResponseMixin):
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id) 
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource not available'})
            return HttpResponse(json_data,content_type='application/json', status =404)

        # if there is no exceptions 
        else:
            json_data = serialize('json',[emp,]) #can you convert this list of employee into json  
            return HttpResponse(json_data,content_type='application/json', status =200)

      
    
# How to add status code to the response 
        #  return HttpResponse(json_data,content_type='application/json', status =200)
   

# when we run this code we we get o/p like 
#     200(status code)
# [{'model': 'testapp.employee', 'pk': 2, 'fields': {'eno': 300, 'ename': 'chiny', 'eadd': 'banglore'}}]
class EmployeeDetailsCBV3(View):
    def get(self,request,id,*args,**kwargs):
        emp = Employee.objects.get(id=id) 
        # if you want particular field 
        json_data = serialize('json',[emp,],fields=('eno','ename','eadd'))
        return HttpResponse(json_data,content_type='application/json')
 
  
##########################################################
    
# Get the list of all the Employee 
class EmployeeListCBV(View):
    def get(self,request,*args,**kwargs):
        # To get all the records
        qs = Employee.objects.all() 
        # o/p: <QuerySet [<Employee: Employee object (1)>, <Employee: Employee object (2)>, <Employee: Employee object (3)>, <Employee: Employee object (4)>]> <class 'django.db.models.query.QuerySet'>
        # print(qs, type(qs))
        json_data = serialize('json', qs) #(qs: because weare already getting the list of Employee)
        return HttpResponse(json_data,content_type='application/json')


class EmployeeListCBV2(View):
    def get(self,request,*args,**kwargs):
        # To get all the records
        qs = Employee.objects.all() 
        # o/p: <QuerySet [<Employee: Employee object (1)>, <Employee: Employee object (2)>, <Employee: Employee object (3)>, <Employee: Employee object (4)>]> <class 'django.db.models.query.QuerySet'>
        # print(qs, type(qs))
        json_data = serialize('json', qs) #(qs: because weare already getting the list of Employee)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data =obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return HttpResponse(json_data,content_type='application/json')


from testapp.mixin import SerializeMixin,HttpResponseMixin

class EmployeeListCBV3(SerializeMixin, HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        # To get all the records
        try:
            qs = Employee.objects.all() 
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource not available'})
            return self.response_message(json_data,status=404)
        else:
            # o/p: <QuerySet [<Employee: Employee object (1)>, <Employee: Employee object (2)>, <Employee: Employee object (3)>, <Employee: Employee object (4)>]> <class 'django.db.models.query.QuerySet'>
            # print(qs, type(qs))
            json_data = self.serializedata(qs) #call mixin function
            return self.response_message(json_data)
        

# Now , is it possible to dumps complete data to my console
        
        # 1. python manage.py dumpdata testapp.Employee
        # it is going to provide Employee data to console in JSON(default) format 

        # To display with some indentation 
        # 2.. python manage.py dumpdata testapp.Employee --indent 4

        # 3.To Display in another format 
        # python manage.py dumpdata testapp.Employee --format xml --indent 4

        # 4.To save this dump data into some file 
        # python manage.py dumpdata testapp.Employee --format xml > emp.xml --indent 4
        # python manage.py dumpdata testapp.Employee --format YAML > emp.xml --indent 4


# POST Method

# while in POST method we must have to handle/varify the CSRF 
        # 3-ways are available 
        # 1. Method Level
        # 2. Class Level ()
        # 3. Project Level  (Not recomended)

    # 1. To disable at method level 
            # from django.views.decorators.csrf import csrf_exempt
            # # for which function you want 
            # @csrf_exempt
            # def my_app(request):
            #     -----
            #     ----
    # 2. To Disable at class level 
            # from django.views.decorators.csrf import csrf_exempt
            # from django.utils.decorators import method_decorator
            # @method_decorator(csrf_exempt, name='dispatch')
            # class EmployeeListCBV(View):
                # noramlly we apply for the POST method , but if we give
                # name='dispatch' , than it is applcable for all the http request 
    # 3. To Disable at project level 
        # - settings.py ---> middleware ---> comment csrf 
        



# 2: Create Record 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')   #Disable CSRF varification         
class EmployeeListCBV3(SerializeMixin, HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        # To get all the records
        try:
            qs = Employee.objects.all() 
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource not available'})
            return self.response_message(json_data,status=404)
        else:
            # o/p: <QuerySet [<Employee: Employee object (1)>, <Employee: Employee object (2)>, <Employee: Employee object (3)>, <Employee: Employee object (4)>]> <class 'django.db.models.query.QuerySet'>
            # print(qs, type(qs))
            json_data = self.serializedata(qs) #call mixin function
            return self.response_message(json_data)
        
    # def post(self,request,*args, **kwargs):
    #     json_data = json.dumps({'msg': 'This is from post method'})
    #     return self.response_message(json_data)
    """
    post() Method Logic: 
     Inside post method we can access data sent by partner application by using 
    "request.body". 
     First we have to check whether this data is json or not.
    """
    def post(self,request,*args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send the valid Data'})
            return self.response_message(json_data,status=400)
        # if data is valid , get the data and save, we are getting json data, so first convert and then save
        # Now to save this data we required Form(model form )
        # json_data = json.dumps({'msg': 'You have sended  the valid Data'})
        empdata = json.loads(data) # convert data into python 
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)  
            json_data = json.dumps({'msg': 'Resource Created Successfully'}) 
            return self.response_message(json_data)
        if form.errors:
            json_data = json.dumps(form.errors) 
            return self.response_message(json_data,status=400)
        
# PUT and DELETE
        
@method_decorator(csrf_exempt, name='dispatch')   #Disable CSRF varification         
class EmployeeDetailsCBV2(View,HttpResponseMixin):
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id) 
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource not available'})
            return HttpResponse(json_data,content_type='application/json', status =404)

        # if there is no exceptions 
        else:
            json_data = serialize('json',[emp,]) #can you convert this list of employee into json  
            return HttpResponse(json_data,content_type='application/json', status =200)

    # Update Information 
    def put(self,request,id,*args, **kwargs):
        # check if object is available with this id 
        emp = get_object_by_id(id=id)
        if emp is None:
            json_data = json.dumps({'msg': 'No Matched Resourece Found, Not possible to perform Updation '})
            return self.response_message(json_data,status=404)
        # if emp exist/present 
        data = request.body
        print(data)
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send the valid Data'})
            return self.response_message(json_data,status=400)
        # if valid json data, convert it into python 
        provided_data = json.loads(data) #convert into python dict 
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eadd': emp.eadd,

        }
        original_data.update(provided_data) #dict opration
        form = EmployeeForm(original_data, instance=emp) # if we are not passing "instance" than it will create new object 
        if form.is_valid():
            form.save(commit=True)  
            json_data = json.dumps({'msg': 'Resource Updated Successfully'}) 
            return self.response_message(json_data)
        if form.errors:
            json_data = json.dumps(form.errors) 
            return self.response_message(json_data,status=400)
        
    def delete(self,request,id,*args,**kwargs):
        # check if object is available with this id 
        emp = get_object_by_id(id=id)
        if emp is None:
            json_data = json.dumps({'msg': 'No Matched Resourece Found, Not possible to perform Deletion '})
            return self.response_message(json_data,status=404)
        
        # t=emp.delete()
        # # The return type of ,emp.delete is a tuple
        # # it contain 2-value 1. status 2.deleted-item
        # # o/p: (1, {'testapp.Employee': 1})
        # print(t)
        status, deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg': 'Resource Deleted sucessfully '})
            return self.response_message(json_data)
        json_data = json.dumps({'msg': 'Unable to Delete...plz try again '})
        return self.response_message(json_data,status=404)
  