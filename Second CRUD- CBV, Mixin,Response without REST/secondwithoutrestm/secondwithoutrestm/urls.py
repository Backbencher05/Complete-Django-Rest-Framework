"""secondwithoutrestm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.EmployeeDetailsCBV.as_view()),
    path('api/<id>/', views.EmployeeDetailsCBV1.as_view()),
    path('apis/<id>/', views.EmployeeDetailsCBV2.as_view()),
    path('apiss/<id>/', views.EmployeeDetailsCBV3.as_view()),
    # to list all the data 
    path('apiall/', views.EmployeeListCBV.as_view()),
    path('apialls/', views.EmployeeListCBV2.as_view()),
    path('apiallss/', views.EmployeeListCBV3.as_view()),
    # create 
]