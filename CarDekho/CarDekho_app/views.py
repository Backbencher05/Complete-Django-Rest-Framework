from django.shortcuts import render
from CarDekho_app.models import CarList
import json
# from django.http import JsonResponse
from CarDekho_app.api.serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

# def car_list_view(request):
#     cars = CarList.objects.all()
#     # we can't pass object/complex data 
#     # so convert it into python
#     data ={
#         'cars': list(cars.values()),
#     }
#     return JsonResponse(data)

# def car_detail_view(request,id):
#     car = CarList.objects.get(id=id)
#     data = {
#         'name': car.name,
#         'Description': car.description,
#         'active': car.active
#     }
#     If we have huge ammount of data , getting data will become heavy task
    #   so we use serializers 
#     return JsonResponse(data)

"""
1) Serialization:  The process of converting complex objects like "Model objects and QuerySets"
                    to Python native data types like dictionary etc,is called Serialization.

        The main advantage of converting to python native data types is we can convert(render) 
       very easily to JSON,XML etc

"""

# which type of request you are sending, By default 'GET' 
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

@api_view(['GET', 'PUT'])
def car_detail_view(request,id):
    if request.method == 'GET': 
        try:
            car = CarList.objects.get(id=id)
        except: 
            return Response({'Error': 'Car not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        car = CarList.objects.get(id=id)
        serializer = CarSerializer(car,data=request.data) #we are passing "car" so it will uodate in the existing data
        # serializer = CarSerializer(data=request.data) # in this case new object will be create 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        car =CarList.objects.get(id=id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




