from django.urls import path
from CarDekhoApp import views

urlpatterns =[
    path('list/', views.ShowroomView.as_view(),name='sholost'),
    path('detail/<id>', views.ShowroomDetailView.as_view(),name='showdetail')

]