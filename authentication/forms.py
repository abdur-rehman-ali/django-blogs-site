# Django Imports
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
  UserCreationForm
)

class RegisterUser(UserCreationForm):
  """
    A user registration form
  """
  username = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  email = forms.EmailField(
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  password1 = forms.CharField(
    label='Password',
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )
  password2 = forms.CharField(
    label='Password(Confirmation)',
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password1']
