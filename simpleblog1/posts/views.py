from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def homepage(request):
    resp = {'msg': 'Hello World'}
    jsondata = json.dumps(resp)
    return HttpResponse(jsondata, 'application/json')

# using Django Rest 
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

def homepagerest(request):
    pass