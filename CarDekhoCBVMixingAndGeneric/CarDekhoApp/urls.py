from django.urls import path
from CarDekhoApp import views

urlpatterns = [
    path('review', views.ReviewList.as_view()),
    path('review/<pk>', views.ReviewDetail.as_view()),
    # Concrete View Classes
    path('reviews', views.ReviewLists.as_view()),
    path('reviews/<pk>', views.ReviewDetails.as_view()),

]