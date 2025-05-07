from django.shortcuts import render
from CarDekho_app.models import CarList
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from CarDekho_app.serializers import CarSerializer
# Create your views here.

"""
def car_list_view(request):
    cars = CarList.objects.all()
    print(cars)
    data = {
        'cars': list(cars.values()),
    }
    return JsonResponse(data)


def car_detail_view(request,id):
    car = CarList.objects.get(id=id)
    data = {
        'name': car.name,
        'Descriptions': car.description,
        'price': car.price,
        'active': car.active
    }
    return JsonResponse(data)
"""

@api_view(['GET','POST'])
def car_list_view(request):
    if request.method == 'GET':
        car = CarList.objects.all()
        serializer = CarSerializer(car,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request,id):
    if request.method == 'GET':
        try:
            car = CarList.objects.get(id=id)
        except:
            return Response({'Error': 'Car not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    

    if request.method == 'PUT':
        try:
            car = CarList.objects.get(id = id)
        except:
            return Response({'Error': 'Car not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        try:
            car = CarList.objects.get(id = id)
        except:
            return Response({'Error': 'Car not Found'}, status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
