from django.urls import path,include
from rest_framework.routers import DefaultRouter
from CarDekhoApp import views

router = DefaultRouter()
router.register('showroom', views.Showroom_Viewset, basename='showroom')


urlpatterns =[
    path('',include(router.urls)),
]
