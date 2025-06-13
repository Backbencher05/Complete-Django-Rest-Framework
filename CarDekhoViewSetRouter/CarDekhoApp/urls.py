from django.urls import path,include
from rest_framework.routers import DefaultRouter
from CarDekhoApp import views

router = DefaultRouter()
router.register('showroom', views.Showroom_Viewset, basename='showroom')


urlpatterns =[
    # now we dont have to use multiple urls , we have combined two urls
    path('',include(router.urls)),
    # path('list/', views.ShowroomView.as_view(),name='sholost'),
    # path('detail/<id>', views.ShowroomDetailView.as_view(),name='showdetail')
    
]
