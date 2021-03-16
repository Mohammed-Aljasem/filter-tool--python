from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
  first_name = models.CharField(max_length=30)
  last_name  = models.CharField(max_length=30)
  email      = models.CharField(max_length=30)
  age        = models.CharField(max_length=4)
  gender     = models.CharField(max_length=30)

  def __str__(self):
        return self.first_name

  
        