from CarDekho_app import views
from django.urls import path

urlpatterns = [
    path('list/', views.CarListView),
    path('<id>', views.car_detail_view),
]