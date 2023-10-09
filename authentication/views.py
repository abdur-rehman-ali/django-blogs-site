# Django imports 
from django.shortcuts import (
  render,
  redirect
)
from django.contrib.auth import (
  login,
  logout,
  authenticate
)

# Local imports 
from authentication.forms import (
  RegisterUser,
  LoginUser
)

# Create your views here.
def registration_view(request):
  if request.method == 'POST':
    form = RegisterUser(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('blogs_index')
  else:
    form = RegisterUser(label_suffix='')
  context = {
    'form': form
  }
  template_name = 'auth/registration.html'
  return render(request, template_name, context)

def login_view(request):
  if request.method == 'POST':
    form = LoginUser(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('blogs_index')
      else: 
        return redirect('login')
  else:
    form = LoginUser()
  context = {
    'form': form
  }
  template_name = 'auth/login.html'
  return render(request, template_name, context)

def logout_view(request):
  logout(request)
  return redirect('blogs_index')
