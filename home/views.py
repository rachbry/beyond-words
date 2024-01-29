from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from allauth.socialaccount.models import SocialApp

# Create your views here.
class Index(TemplateView):
    template_name = "home/index.html"

def home(request):
    return render(request, 'home/index.html')

class About(TemplateView):
    template_name = "home/about.html"

class Services(TemplateView):
    template_name = "home/services.html"

