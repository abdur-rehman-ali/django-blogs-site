# Django imports 
from django.shortcuts import (
  render,
  redirect
)
from django.contrib.auth import login

# Local imports 
from authentication.forms import (
  RegisterUser
)

# Create your views here.
def registration(request):
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
