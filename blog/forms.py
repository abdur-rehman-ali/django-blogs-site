# Django Imports
from django import forms

# Local Imports
from blog.models import Blog

class BlogForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = ('title', 'content')
    labels = {
      'title': 'Blog title',
      'content': 'Blog content'
    }
    widgets = {
      'title' : forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Please enter title here'
        }),
      'content' : forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Please enter content here'
        })
    }
