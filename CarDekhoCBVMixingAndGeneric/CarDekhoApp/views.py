from django.shortcuts import render
from rest_framework.views import APIView
from CarDekhoApp.models import *
from .api.serializer import *

from rest_framework import mixins
from rest_framework import generics

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions
# we need queryset to apply DjangoModelPermissions and we can modify the permission for the perticular user
# Create your views here.


# generics and mixins

class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,
                 generics.GenericAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # authentication_classes =[SessionAuthentication]
    # permission_classes = [DjangoModelPermissions]

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,*kwargs)
    
class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    

# Concrete View Classes
class ReviewLists(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

"""
now we don't have to write extra code like 
    def get():
        ....
        ...
    def post():
        ....
        ....
these lines are enough, if we are using concreate View classes
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

behind the scene in using using this only 
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,*kwargs)

https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py
search any functions like , ListCreateAPIView etc.
"""
