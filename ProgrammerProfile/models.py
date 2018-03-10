from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    Name = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    Description = models.TextField()
    ProfilePic = models.FileField()

    def __str__(self):
        return self.Name
class Posts(models.Model):
    

    Name = models.CharField(max_length=255)
    post = models.TextField()
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name 
