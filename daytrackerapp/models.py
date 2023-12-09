
from django.db import models
from django.contrib.auth.models import User, Group



# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    notes = models.CharField(max_length=300)
    timestart = models.CharField(max_length=7)
    timeend = models.CharField(max_length=7)