# Django Imports 
from django.urls import path

# Local Imports
from blog import views

urlpatterns = [
  path('', views.index, name='blogs_index'),
  path('new/', views.new, name='blogs_new'),
  path('edit/<int:pk>', views.edit, name='blogs_edit'),
  path('destroy/<int:pk>', views.destroy, name='blogs_destroy'),
]
