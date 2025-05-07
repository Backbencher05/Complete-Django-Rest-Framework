import json
from testapp.models import Employee

def is_json(data):
    try:
        p_data = json.loads(data)
        valid = True
    except:
        valid = False
        
    return valid

def get_objects_by_id(id):
    try:
        emp = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        emp = None
    return emp