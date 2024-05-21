from django.http import HttpResponse



# Mixin:
    # - it is a seprate class which contains severals instance method 
    # - is a child class of object
    # - contains instance method
    # - don't have instance variable
    # service provider to the child class 

class HttpResponseMixin(object):
    def rendertoHttpResponse(self,json_data):
         return HttpResponse(json_data,content_type='application/json')