# Django Imports
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
  UserCreationForm,
  AuthenticationForm,
  PasswordChangeForm
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


class LoginUser(AuthenticationForm):
  """
    A user login form
  """
  username = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  password = forms.CharField(
    label='Password',
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )

class ChangePasswordUser(PasswordChangeForm):
  """
    A user password change form
  """
  old_password = forms.CharField(
    label="Please enter old password",
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )
  new_password1 = forms.CharField(
    label="Please enter new password",
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )
  new_password2 = forms.CharField(
    label="Please confirm new password",
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )
