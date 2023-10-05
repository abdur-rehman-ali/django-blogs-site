# Django Imports 
from django.urls import path

# Local Imports
from authentication import views

urlpatterns = [
  path('registration/', views.registration_view, name='registration'),
  path('logout/', views.logout_view, name='logout')
]
