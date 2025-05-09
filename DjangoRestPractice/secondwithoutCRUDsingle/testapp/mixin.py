from django.http import HttpResponse
from django.core.serializers import serialize
import json


class SerializeMixin(object):
    def serializedata(self,qs):
        json_data = serialize('json',qs)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data =obj['fields']
            final_list.append(emp_data)
        # again convert this python data into dict 
        json_data = json.dumps(final_list)
        return json_data
    
class HttpResponseMixin(object):
    def response_message(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json', status=status)