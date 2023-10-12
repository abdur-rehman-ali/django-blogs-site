# Django Imports 
from django.db import models
from django.core import validators
from django.contrib.auth.models import User

class Blog(models.Model):
  title = models.CharField(
    max_length=100,
    validators=[validators.MinLengthValidator(3)]
  )
  content = models.TextField(validators=[validators.MinLengthValidator(5)])
  published_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return f"{self.id} - {self.title}"
