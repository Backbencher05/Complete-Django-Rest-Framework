from django.urls import path
from CarDekho_app import views

urlpatterns = [
    path('list/', views.car_list_view, name='car_list'),
    path('<int:id>', views.car_detail_view, name='car_detail')
]