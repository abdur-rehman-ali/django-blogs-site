# Django Imports 
from django.contrib import admin

# Local Imports 
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'content']
