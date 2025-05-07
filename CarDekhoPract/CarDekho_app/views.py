from django.shortcuts import render
from CarDekho_app.models import CarModel
from CarDekho_app.api.serializer import CarSerializer
from django.http import HttpResponse
import json 

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

# def CarListView(request):
#     if request.method == 'GET':        
#         car = CarModel.objects.all()
#         # we got the car object not we have to send python data 
#         serializer = CarSerializer(car,many=True)
#         json_data = json.dumps(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

@api_view(['GET','POST'])
def CarListView(request):
    if request.method == 'GET':
        car = CarModel.objects.all()
        serializer = CarSerializer(car,many=True)
        # print(type(serializer.data))
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT', 'DELETE'])
def car_detail_view(request,id):
    if request.method == 'GET': 
        try:
            car = CarModel.objects.get(id=id)
        except:
            return Response({'Error': 'Car Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        try:
            car = CarModel.objects.get(id=id)
        except:
            return Response({'Error': 'Car not found please send valid id'})
        serializer = CarSerializer(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            car = CarModel.objects.get(id=id)
        except:
            return Response({'Error': 'Car not found please send valid id'})
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)