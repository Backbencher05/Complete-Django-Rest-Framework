from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required
class HomePageView(TemplateView):
    template_name = 'dashboard/home.html'

class LogoutView(TemplateView):
    template_name = 'dashboard/logout.html'

class SignUpView(TemplateView):
    pass

class InstagramHomeView(TemplateView):
    template_name = 'dashboard/home.html'