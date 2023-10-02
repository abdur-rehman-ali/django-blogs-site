# Django Imports 
from django.db import models
from django.core import validators

class Blog(models.Model):
  title = models.CharField(
    max_length=100,
    validators=[validators.MinLengthValidator(3)]
  )
  content = models.TextField(validators=[validators.MinLengthValidator(5)])
  published_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.id} - {self.title}"
