from django.urls import path,include
from dashboard import views

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    # login 
    path('accounts/', include('django.contrib.auth.urls')),
    # path('logout/', views.logout_view),
    # path('signup/', views.signup_views),
]