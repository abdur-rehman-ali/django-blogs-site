# Django Imports 
from django.urls import path

# Local Imports
from authentication import views

urlpatterns = [
  path('registration/', views.registration_view, name='registration'),
  path('login/', views.login_view, name='login'),
  path('change_password/', views.change_password_view, name='change_password'),
  path('logout/', views.logout_view, name='logout')
]
