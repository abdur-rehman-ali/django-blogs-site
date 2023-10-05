# Django Imports 
from django.urls import path

# Local Imports
from authentication import views

urlpatterns = [
  path('registration/', views.registration, name='registration'),
]
