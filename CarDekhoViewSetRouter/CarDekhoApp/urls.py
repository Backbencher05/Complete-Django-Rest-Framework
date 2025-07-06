from django.urls import path,include
from rest_framework.routers import DefaultRouter
from CarDekhoApp import views


"""
DefaultRouter automatically generates all the standard URL routes 
(like list, create, retrieve, update, delete) for your ViewSet classes.

Without it:
You’d need to manually write URL patterns for each action like:
urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
]

"""

router = DefaultRouter()
router.register('showroom', views.Showroom_Viewset, basename='showroom')


urlpatterns =[
    # now we dont have to use multiple urls , we have combined two urls
    path('',include(router.urls)),
    # path('list/', views.ShowroomView.as_view(),name='sholost'),
    # path('detail/<id>', views.ShowroomDetailView.as_view(),name='showdetail')
"""
This creates:

GET /posts/ → list

POST /posts/ → create

GET /posts/<id>/ → retrieve

PUT/PATCH /posts/<id>/ → update

DELETE /posts/<id>/ → delete

No manual URLs needed. Cleaner, less prone to bugs, and instantly DRF-compliant.
"""
]
