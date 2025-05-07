from django.shortcuts import render
from rest_framework.views import APIView
from CarDekhoApp.models import *
from .api.serializers import CarListSerializer,ShowroomSerializer
from rest_framework.response import Response
from rest_framework import status
# authentication and permission 
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser

# Create your views here.


# if we want to apply Authentication and permission to all the classes 
# than go to the setting and add at the last 

class ShowroomView(APIView):
    # 1. BasicAuthentication
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]  #we have to login
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser] #for admin only

    # 2. SessionAuthentication
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    
    def get(self,request):
        showroom = ShowroomList.objects.all()
        serializer = ShowroomSerializer(showroom,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        # we got the data in post
        serializer = ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ShowroomDetailView(APIView):
    def get(self,request,id):
        try:
            showroom = ShowroomList.objects.get(id=id)
        except:
            return Response("Given Id data not Present", status=status.HTTP_404_NOT_FOUND)
        serializer = ShowroomSerializer(showroom)
        return Response(serializer.data)
    
    def put(self,request,id):
        try:
            showroom = ShowroomList.objects.get(id=id)
        except:
            return Response("Given Id data not Present", status=status.HTTP_404_NOT_FOUND)
        serializer = ShowroomSerializer(showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,id):
        try:
            showroom = ShowroomList.objects.get(id=id)
        except:
            return Response("Given Id data not Present", status=status.HTTP_404_NOT_FOUND)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)