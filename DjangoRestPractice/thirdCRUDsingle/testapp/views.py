from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class StudentCRUDAWS(View):
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if valid:
            pass
