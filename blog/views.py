# Django Imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Local Imports
from blog.forms import BlogForm
from blog.models import Blog

def index(request):
  blogs = Blog.objects.all()
  context = {
    'blogs': blogs
  }
  template = 'blog/index.html'
  return render(request, template, context)


def new(request):
  if request.method == 'POST':
    form = BlogForm(request.POST)
    if form.is_valid():
      title = form.cleaned_data.get('title')
      content = form.cleaned_data.get('content')
      Blog.objects.create(title=title, content=content, user=request.user)
      return HttpResponseRedirect(reverse('blogs_index'))
  else: 
    form = BlogForm(label_suffix='')
  template = 'blog/new.html'
  context = {
    'form': form
  }
  return render(request, template, context)

def edit(request, pk):
  blog = Blog.objects.get(pk=pk)
  if request.method == 'POST':
    form = BlogForm(request.POST, instance=blog)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('blogs_index'))
  else: 
    form = BlogForm(label_suffix='', instance=blog)
  template = 'blog/new.html'
  context = {
    'form': form
  }
  return render(request, template, context)

def destroy(request, pk):
  blog = Blog.objects.get(pk=pk)
  blog.delete()
  return HttpResponseRedirect(reverse('blogs_index'))
