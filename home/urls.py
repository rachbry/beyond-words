from django.urls import path, include
from .views import Index, About, Services
from . import views

urlpatterns = [
    path('', Index.as_view(), name = 'home'),
    path('accounts/', include('allauth.urls')),
    path('about/', About.as_view(), name = 'about'),
    path('services/', Services.as_view(), name = 'services'),
]