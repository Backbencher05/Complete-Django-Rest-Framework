from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import *
from .api.serializer import *
from rest_framework import status
# Create your views here.


# Viewsets    
# class Showroom_Viewset(viewsets.ViewSet):
#     def list(self,request):
#         queryset = ShowroomList.objects.all()
#         serializer = ShowroomSerializer(queryset,many=True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         queryset = ShowroomList.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = ShowroomSerializer(user)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = ShowroomSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Model View Set 

# class Showroom_Viewset(viewsets.ModelViewSet):
#     queryset = ShowroomList.objects.all()
#     serializer_class = ShowroomSerializer

class Showroom_Viewset(viewsets.ReadOnlyModelViewSet):
    queryset = ShowroomList.objects.all()
    serializer_class = ShowroomSerializer